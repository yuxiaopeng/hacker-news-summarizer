# Hacker News 热门文章摘要 (2025-07-07)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 水星：基于扩散的超快语言模型

**原文标题**: Mercury: Ultra-Fast Language Models Based on Diffusion

**原文链接**: [https://arxiv.org/abs/2506.17298](https://arxiv.org/abs/2506.17298)

该 arXiv 文章 (2506.17298) 于 2025 年 6 月 17 日提交，介绍了 Mercury，这是 Inception Labs 基于扩散方法开发的一系列新型商业级大型语言模型 (LLM)。这些模型采用 Transformer 架构，并经过训练以并行预测多个 token，从而显著提高速度。

该论文重点介绍了 Mercury Coder，这是 Mercury 系列中首批专为编码应用设计的模型，提供 Mini 和 Small 两种尺寸。Artificial Analysis 的独立评估表明，Mercury Coder Mini 和 Small 在 NVIDIA H100 GPU 上的吞吐量分别达到了 1109 和 737 tokens/秒，处于领先水平。 这些模型的性能优于现有的速度优化前沿模型，高达 10 倍，同时保持了相当的质量。

文章展示了在多种语言和用例的代码基准测试结果，以及来自 Copilot Arena 开发者验证的结果。Mercury Coder 在质量上排名第二，并且是该平台上总体速度最快的模型。 作者还宣布发布公共 API 和免费的 playground，供用户访问这些模型。 该研究涵盖计算与语言、人工智能和机器学习领域。

---

## 2. 我使用o3从我保存的Pocket链接中分析我自己。

**原文标题**: I used o3 to profile myself from my saved Pocket links

**原文链接**: [https://noperator.dev/posts/o3-pocket-profile/](https://noperator.dev/posts/o3-pocket-profile/)

作者探讨了利用其保存的Pocket文章作为数据进行AI分析的可能性。起因是Pocket的关闭导致需要迁移多年来保存的链接。他们使用o3 AI模型分析了近900篇已保存的文章，并提供了一个提示，要求o3仅根据URL推断个人详细信息。

o3生成了一个令人惊讶的准确的个人资料，正确地猜测了作者的年龄范围、位置、家庭规模、教育程度、行业、收入和心态。该个人资料甚至涉及一些微妙的线索，如信仰、隐私兴趣、创客倾向、健康问题和写作愿望。o3概述了激励因素、盲点、偏好的媒介和潜在的宏伟目标。

作者指出，将CSV数据直接粘贴到提示符中比上传文件产生了更准确的结果。这次经历突显了触手可及的AI具有根据看似无害的数据（如已保存的链接）创建详细个人资料的能力。作者总结说，现在任何人都可以访问以前仅限于像谷歌和Facebook这样的公司的数据分析能力。他们计划使用这个AI生成的个人资料来改进他们的个人内容推荐。由于Pocket的关闭，作者已转移到Wallabag和FreshRSS，发现2025年自托管变得容易得多。

---

## 3. 展示HN：非学习比较器，一个用于比较机器非学习的可视化工具

**原文标题**: Show HN: Unlearning Comparator, a visual tool to compare machine unlearning

**原文链接**: [https://gnueaj.github.io/Machine-Unlearning-Comparator/](https://gnueaj.github.io/Machine-Unlearning-Comparator/)

“Show HN: Unlearning Comparator” 帖子介绍了一款可视化工具，旨在比较不同的机器学习逆学习技术。本质上，它是一个平台，允许用户轻松地可视化和理解各种逆学习方法应用于机器学习模型时的性能。

Unlearning Comparator 的核心目的是使比较逆学习方法的过程更易于访问和直观。它可能提供一个用户友好的界面来输入数据、选择不同的逆学习算法，然后以可视化的方式比较结果。这可能包括诸如准确率分数、性能指标，甚至是在逆学习之前和之后模型行为的可视化表示。

该工具可能面向研究人员、从业者以及任何有兴趣了解机器学习逆学习细微之处的人。它的目标是提供一种实用的方法来评估不同逆学习方法在各种场景中的有效性，例如，它们在不显着影响模型整体性能的情况下，能够多好地消除特定数据点的影响。重点在于可视化，使评估逆学习技术这一通常很复杂的过程更容易理解和更有洞察力。最终，它为机器学习社区更好地理解和实施机器学习逆学习提供了一个有价值的资源。

---

## 4. 因为ChatGPT错误地认为它存在而添加一项功能

**原文标题**: Adding a feature because ChatGPT incorrectly thinks it exists

**原文链接**: [https://www.holovaty.com/writing/chatgpt-fake-feature/](https://www.holovaty.com/writing/chatgpt-fake-feature/)

在一次离奇的事件中，乐谱扫描服务 Soundslice 增加了一项新功能——ASCII 吉他谱导入——因为 ChatGPT 错误地告知用户该功能已存在于他们的平台上。

作者 Adrian Holovaty 注意到他们的错误日志中涌现出大量 ChatGPT 会话的截图。这些用户试图将 ASCII 吉他谱（一种基本的吉他记谱形式）导入 Soundslice，尽管该服务从未支持过该功能。

经过调查，Holovaty 发现 ChatGPT 虚假宣传 Soundslice 具有导入和播放 ASCII 吉他谱的能力。这种错误信息正驱使着用户带着不正确的期望涌向 Soundslice，可能会损害公司的声誉。

面对否认虚假信息或适应 ChatGPT 创造的意外“市场需求”的选择，Soundslice 选择了开发一个自定义的 ASCII 吉他谱导入器。他们还更新了用户界面以反映这项新功能。

Holovaty 承认基于错误信息开发一项功能的特殊性，质疑公司是否应该被 AI 产生的虚假声明所驱动。然而，他也对提供一个让用户受益的工具感到满意，尽管情况不同寻常。这种情况代表了一个独特的案例，即一家公司的产品开发直接受到大型语言模型错误的影响。

---

## 5. 戴森：技术中心设计与社会消费

**原文标题**: Dyson, techno-centric design and social consumption

**原文链接**: [https://2earth.github.io/website/20250707.html](https://2earth.github.io/website/20250707.html)

汤姆·鲁德尔的文章批判了戴森“技术中心主义”的设计理念，认为其将技术和营销置于用户需求和实用设计之上。他认为戴森早期的成功源于真正的功能优势，但此后公司更加注重“技术至上”的方法，受社会消费和品牌形象驱动。

鲁德尔举例说明了戴森产品中对技术的关注如何对可用性、人体工程学和成本产生负面影响，并列举了吸尘器、干手机和洗衣机等产品。他将戴森的设计与博世等竞争对手进行对比，认为虽然戴森追求未来主义美学，但替代产品提供了更用户友好和实用的体验。

文章强调了戴森如何利用其品牌形象来促进社会消费，创造“自我形象机器”而不是仅仅是功能性产品。这种做法延伸到了公共场所，戴森洗手间产品被作为身份象征进行营销，即使它们牺牲了可用性和成本效益。

鲁德尔还质疑了围绕詹姆斯·戴森的“明星设计师”神话，认为这掩盖了现代产品开发的协作性质，并膨胀了个人自我。他认为对个人才能的强调会导致华而不实的设计，将外观置于真正的解决问题之上。

总之，鲁德尔认为，戴森以技术为中心的设计和对社会消费的关注最终会降低其产品的整体质量和用户体验。他认为，一种更谦逊和以用户为中心的设计方法会带来更好的结果。

---

## 6. 展示HN：Ossia score – 视听艺术家的音序器

**原文标题**: Show HN: Ossia score – a sequencer for audio-visual artists

**原文链接**: [https://github.com/ossia/score](https://github.com/ossia/score)

Ossia score是一款面向音视频艺术家的免费开源音序器，通过对OSC、MIDI、DMX、音频、视频等在各种软硬件之间进行排序，实现互动节目的创作。它支持使用JavaScript、Faust、PureData和C++等语言进行脚本编写和实时编码，并集成物联网协议、传感器和创意编程语言。它可以处理各种音频和视频格式，并通过各种工具处理视觉效果。

该软件可在桌面、移动、Web和嵌入式平台（包括Raspberry Pi Zero 2）上运行。它通过AppImage提供Windows、macOS和Linux版本。该项目鼓励贡献，并通过代码中的TODO、FIXME等标记突出显示需要改进的领域。它提供了一个示例插件，用于创建自定义功能，并欢迎代码和资金贡献，以支持项目的发展。通过论坛、Discord和Matrix提供活跃的社区支持。

---

## 7. 当 Figma 开始设计我们

**原文标题**: When Figma starts designing us

**原文链接**: [https://designsystems.international/ideas/when-figma-starts-designing-us/](https://designsystems.international/ideas/when-figma-starts-designing-us/)

本文批判了Figma对设计流程的影响，认为其以工程为中心的功能虽然看似有益，但正在以一种微妙的方式重塑设计实践，可能带来不利影响。作者肯定了Figma在促进远程设计工作中的作用及其整体能力。

然而，诸如自动布局和开发模式等功能受到了批评，因为它们推动设计师过早进行优化和采用僵化的结构。自动布局虽然在成熟的设计中很有用，但会限制自由并强制执行类似DOM的约束，从而扼杀早期阶段的探索。开发模式被认为强化了一种有缺陷的“准备好开发”的心态，在这种心态下，设计在编码之前就被视为完成，并且开发者会被隐含地劝阻不要质疑设计决策。

作者认为，这些功能鼓励设计师过早地做出决策，在想法尚未完全展开之前就做出决策，从而导致设计空间的缩小以及数字设计中日益增长的单一文化。设计团队已经遵守的越来越多的结构化任务进一步加剧了这种情况。

虽然作者提倡设计师和工程师之间的协作，但他们强调，这不应以牺牲不同的观点和自发的探索为代价。核心论点是，Figma的价值观体现在其功能中，优先考虑结构而非自发性，这可能会阻碍创造性的发现，而创造性的发现通常在混乱和实验中蓬勃发展。作者鼓励设计师意识到这种转变，并寻找允许更多开放式探索的工具。

---

## 8. François Chollet：弧奖与我们如何实现AGI [视频]

**原文标题**: François Chollet: The Arc Prize and How We Get to AGI [video]

**原文链接**: [https://www.youtube.com/watch?v=5QcCeSsNRks](https://www.youtube.com/watch?v=5QcCeSsNRks)

所提供的内容并非文章，而是YouTube视频页面底部的样板页脚文本，包括版权信息、各种YouTube资源链接（新闻、联系方式、创作者、广告、开发者、条款、隐私、安全）以及关于测试新功能的声明。

因此，没有可供总结的文章内容。唯一相关的信息是标题：“François Chollet：Arc奖以及我们如何实现AGI [视频]”。该标题表明该视频包含与François Chollet关于Arc奖（可能与衡量和促进人工智能推理有关）的讨论，以及他对实现通用人工智能（AGI）的看法。但是，在没有视频实际内容的情况下，无法进行进一步的总结。

---

## 9. CPU-X：Linux平台的CPU-Z

**原文标题**: CPU-X: CPU-Z for Linux

**原文链接**: [https://thetumultuousunicornofdarkness.github.io/CPU-X/](https://thetumultuousunicornofdarkness.github.io/CPU-X/)

CPU-X 是一款免费开源的系统分析和监控应用程序，适用于 GNU/Linux 和 FreeBSD，类似于 Windows 上的 CPU-Z。它收集有关计算机的 CPU、主板、内存、系统和显卡以及性能指标的信息。

该软件提供多种界面：使用 GTK 的图形模式、使用 NCurses 的文本模式以及可通过命令行访问的转储模式。用户可以从提供的链接下载最新版本的 CPU-X。本文引导用户查阅 README 文件以获取更多信息，并访问 wiki 页面以获取屏幕截图和安装说明。

---

## 10. tinymcp: 让LLM通过模型上下文协议控制嵌入式设备

**原文标题**: tinymcp: Let LLMs control embedded devices via the Model Context Protocol

**原文链接**: [https://github.com/golioth/tinymcp](https://github.com/golioth/tinymcp)

Tinymcp是一个实验性项目，它使大型语言模型 (LLM) 能够通过 Golioth 管理 API，利用模型上下文协议 (MCP) 控制嵌入式设备。它利用 Golioth 的 LightDB State 和远程过程调用 (RPC) 将设备功能作为“工具”暴露给 LLM。一个关键优势是现有设备无需固件修改即可暴露 RPC。

要使用 tinymcp，设备需要连接到 Golioth，并且 tinymcp 服务器必须在本地运行，并配置环境变量 `TINYMCP_PROJECT`、`TINYMCP_DEVICE` 和 `TINYMCP_API_KEY`。一个“闪烁”示例固件（使用 Zephyr RTOS）演示了通过 tinymcp 控制 LED，如果需要，可以将其刷入设备。

tinymcp 服务器可以与各种 MCP 客户端一起使用，包括：

*   **MCP Inspector:** 一个可视化的测试工具，可用于排除 MCP 服务器交互故障。
*   **Claude Code:** 一个代理编码工具，只需一个命令即可配置。
*   **Gemini CLI:** 一个开源 AI 代理，启动时会在存储库中自动配置以连接到本地运行的 tinymcp 服务器。

该项目强调它是一个实验性项目，并警告可能存在的重大更改以及将物理控制权委托给 AI 系统的固有风险。

---

## 11. 使用uv的依赖解析器解决Wordle

**原文标题**: Solving Wordle with uv's dependency resolver

**原文链接**: [https://mildbyte.xyz/blog/solving-wordle-with-uv-dependency-resolver/](https://mildbyte.xyz/blog/solving-wordle-with-uv-dependency-resolver/)

本文详细介绍了一种利用 uv 的依赖解析器解决 Wordle 谜题的创新方法，并将其与作者之前在数独和诗歌方面的工作进行了类比。核心思想是将 Wordle 的元素（单词、位置和反馈）表示为 Python 包及其版本，并将游戏规则编码为依赖约束。

作者引入了“位置”包（每个字母 26 个版本）和一个“单词”包（每个可能的 5 个字母单词一个版本）。每次猜测后收到的反馈（绿色、黄色、空白）被转换为对“反馈”包的约束，这些包表示关于字母位置的声明。这些反馈包反过来影响“可能位置”包，表明一个字母 *可能* 在哪里。

本文重点介绍了准确编码反馈的复杂性，特别是黄色字母需要“至少一个”的逻辑。它还解释了如何使用反向版本排除来避免直接依赖版本选择。所有软件包都被构建到 wheels 中，以便与 `uv lock --find-links` 一起使用。

一个辅助程序自动执行该过程：进行猜测，将反馈转换为依赖约束，运行 `uv lock`，并尝试解析后的单词。文章最后还有一个奖励环节，利用字母频率来策略性地排序猜测，以提高求解器的效率（从“LATER”开始）。代码可在 GitHub 上找到。

---

## 12. 探索时代

**原文标题**: The Era of Exploration

**原文链接**: [https://yidingjiang.github.io/blog/post/exploration/](https://yidingjiang.github.io/blog/post/exploration/)

本文认为，下一波人工智能的进步取决于更智能的“探索”，即获取新的、信息丰富的经验的过程，而不是简单地扩展参数。它认为，当前的语言模型正在达到易于获取的文本数据（“化石燃料”）的极限，因此需要转向智能体生成自己的训练数据。

作者将此与强化学习（RL）进行类比，其中探索至关重要。预训练大型语言模型（LLM）类似于预先支付“探索税”，使其能够在微调期间采样更好的轨迹，因为较小的模型受益于从较大的预训练模型中提取知识。如果没有这种初始探索，由于大型语言模型庞大的状态和动作空间，从头开始进行强化学习实际上是不可能的。

文章强调，探索不仅仅是解决单一环境，而是要推广到新的情况。由探索驱动的数据多样性是实现稳健泛化的关键。强化学习智能体必须收集各种轨迹，以避免过度拟合。

作者确定了扩展探索的两个维度：**世界采样**（决定在哪里学习，类似于监督学习中的数据收集）和**路径采样**（决定如何在世界内收集数据，这是强化学习独有的）。最佳学习需要平衡这些维度，以最大限度地提高每次计算浮点运算所获得的信息。路径采样的目的是减少模型在环境中的不确定性，而世界采样的目标仍然不太明确。

---

## 13. Bitchat – 基于蓝牙Mesh网络的去中心化消息应用

**原文标题**: Bitchat – A decentralized messaging app that works over Bluetooth mesh networks

**原文链接**: [https://github.com/jackjackbits/bitchat](https://github.com/jackjackbits/bitchat)

Bitchat：一款去中心化、点对点消息应用，专为通过蓝牙mesh网络进行安全通信而设计，无需互联网接入、服务器或电话号码。它通过无需创建帐户、使用X25519和AES-256-GCM的端到端加密、阅后即焚消息以及用于混淆通信的掩护流量等功能，优先考虑隐私。紧急擦除功能可通过三次点击立即清除所有数据。

该应用支持基于房间的群聊，并可选择密码保护，并允许房间所有者控制消息保留。它包括IRC风格的命令，用于加入房间、发送私信和列出在线用户。Bitchat具有存储转发功能，缓存离线用户的消息并在重新连接时传送。

性能优化包括LZ4消息压缩以节省带宽以及根据电池电量调整功耗的自适应电池模式。该架构使用针对蓝牙LE优化的紧凑型二进制协议、基于TTL的消息路由和消息去重。

可以通过XcodeGen、Swift Package Manager或手动配置Xcode项目来实现设置。该应用程序原生支持iOS和macOS，并且通过实现相同的协议和加密标准，具有Android兼容性的潜力。通过数字签名和前向保密进一步增强安全性。Bitchat利用优化的Bloom过滤器和消息聚合来提高网络效率。《技术白皮书》提供了详细的协议文档。

---

## 14. SUS Lang：SUS硬件描述语言

**原文标题**: SUS Lang: The SUS Hardware Description Language

**原文链接**: [https://sus-lang.org/](https://sus-lang.org/)

SUS：一种新的硬件描述语言，旨在直接与可综合Verilog和VHDL竞争。它旨在为构建网表提供直观且简洁的语法，并利用现有的综合工具进行分析。SUS虽然要求同步设计，但侧重于使硬件设计的内在复杂性更易于管理，而不是将其抽象化。

主要优点包括：

*   **延迟计数：** 简化时序和流水线管理。
*   **易于修改：** 编译器在编辑器内提供广泛的反馈并跟踪设计方面。
*   **完全控制：** 支持任何同步逻辑设计。
*   **强大的元编程：** 允许编译时代码执行，从而实现动态LUT生成。

SUS提供直接的代码到网表映射、通过显式交叉原语实现硬件域分离、内置的流水线语法（无结构约束）、IDE内编译反馈以及用于硬件生成的元编程。计划中的功能包括具有有界整数的类型安全、多时钟模块、形式验证集成以及常用构造的语法糖。

然而，SUS特意避免为握手协议、运行时迭代构造和自动流水线/重定时提供抽象。文档鼓励通过介绍性视频学习SUS，并在GitHub和Discord等平台上加入社区。

---

## 15. 彩色铅笔的耐光性测试

**原文标题**: Lightfastness Testing of Colored Pencils

**原文链接**: [https://sarahrenaeclark.com/lightfast-testing-pencils/](https://sarahrenaeclark.com/lightfast-testing-pencils/)

莎拉·蕾妮·克拉克的文章详细介绍了对50多个彩色铅笔品牌进行的为期6个月的耐光性测试。耐光性，即颜色在光照下抵抗褪色的能力，对于艺术作品的寿命至关重要。文章解释了什么是耐光性，为什么它对艺术家（尤其是那些展示、赠送或出售其作品的人）很重要，以及什么时候它不太重要（例如，用于练习或扫描的作品）。

作者概述了三种测量耐光性的方法：蓝羊毛标准、ASTM D6901 和制造商评级，并强调制造商的声明并不总是可靠的。克拉克的测试包括将彩色铅笔色板与蓝羊毛条一起暴露在阳光下，使用彩色扫描仪，并使用 CIEDE2000 公式来量化褪色。这使她能够为每种颜色分配蓝羊毛分数和近似的 ASTM 耐光性评级。

然后，文章展示了特定品牌的结果，列出了每个品牌的耐光铅笔数量、平均蓝羊毛分数、平均褪色百分比、表现最好和最差的颜色以及在哪里购买它们。她澄清说，“最好和最差”的表现者是通过同时考虑蓝羊毛结果和每种颜色的总褪色来确定的。对于像 Arrtx 这样的某些品牌，由于缺乏对其测试方法的透明度，作者质疑其耐光等级的有效性。这些测试不是对任何品牌的绝对判断，而是一项研究不同铅笔在测试期间彼此表现的比较研究。

---

## 16. 所以你想创建一家衰老公司

**原文标题**: So you wanna build an aging company

**原文链接**: [https://www.librariesforthefuture.bio/p/is-this-aging](https://www.librariesforthefuture.bio/p/is-this-aging)

想创建一家“抗衰老”公司，你真的准备好了吗？

这篇文章探讨了究竟什么才能真正算作“抗衰老”生物技术方法，而不仅仅是针对与年龄相关的疾病。作者认为，抗衰老生物技术的目的应该是 *预防* 与年龄相关的疾病，*保持* 随着年龄增长而衰退的健康功能，或 *逆转* 与年龄相关的疾病的进程。

文章告诫不要将所有与年龄相关的治疗方法等同于真正的抗衰老干预措施。肿瘤药物、早衰症治疗以及仅关注衰老生物标志物的干预措施都被标记为具有潜在误导性，如果它们被宣传为解决核心衰老过程。虽然这些治疗有价值，但可能无法转化为广泛的抗衰老益处。

作者强调了有前景的抗衰老研究领域，包括：虚弱/肌少症、炎症衰老/免疫功能障碍、心脏代谢疾病、纤维化疾病以及神经退行性疾病的前驱症状。针对这些领域的干预措施有可能影响广泛的与年龄相关的问题，并且可以在短期内进行衡量。他们还强调了直接关注寿命和死亡率的重要性。

最后，文章强调了使用现实的衰老模型的重要性，借鉴非模式生物的证据，并采用涉及新型治疗方式的“延迟、替换、恢复和暂停”方法。这些方法应旨在推迟衰退、替换受损组织、逆转细胞衰老或诱导生物停滞。作者认为，关注这些策略可以为真正应对衰老和与年龄相关的疾病提供强有力的证据。

---

## 17. 失落千年，《巴比伦颂歌》重见天日。

**原文标题**: Hymn to Babylon, missing for a millennium, has been discovered

**原文链接**: [https://phys.org/news/2025-07-hymn-babylon-millennium.html](https://phys.org/news/2025-07-hymn-babylon-millennium.html)

一首失落千年的巴比伦赞美诗被慕尼黑大学的恩里克·希门尼斯与巴格达大学合作重新发现。这首发表在《伊拉克》杂志上的赞美诗为了解巴比伦社会和文化提供了新的视角。电子巴比伦图书馆平台的数字化楔形文字碎片并利用人工智能识别相关片段，使得这一发现成为可能。该平台帮助学者们从30个独立的碎片中拼凑出了完整的赞美诗。

这首公元前一千年的赞美诗赞扬了巴比伦，详细描述了它的建筑、幼发拉底河在为这片土地带来春天和生命中所起的作用，并提供了有关女性作为女祭司和巴比伦城市社会角色的独特信息。它描述了幼发拉底河及其在支持巴比伦农业和生活方面的重要作用。此外，这首赞美诗还突出了巴比伦人对外国人的尊重。

这一发现意义重大，因为这首赞美诗很可能是一篇流行的课文，被学生抄写，这使得它以前的默默无闻令人惊讶。巴比伦遗址是联合国教科文组织世界遗产，位于巴格达以南。这项研究加深了我们对古代美索不达米亚文学和巴比伦生活的理解。

---

## 18. 调整Prusa Core One

**原文标题**: Tuning the Prusa Core One

**原文链接**: [https://arachnoid.com/3D_Printing_Prusa_Core_One/](https://arachnoid.com/3D_Printing_Prusa_Core_One/)

本文针对Prusa Core One 3D打印机，提供了详细的调校和配置建议，超越了标准说明。它侧重于提高精度和实用性，特别适用于已组装套件或收到工厂制造机器的用户。

主要涵盖的领域包括：

*   **打印床对齐（Z轴）：** 本文详细介绍了一种手动调平打印床的方法，这对于初始设置至关重要，可以防止磨损并确保正确的Z轴移动。 这涉及手动旋转支撑打印床的螺纹轴到其最低位置。
*   **Core XY轴对齐：** 为了解决打印倾斜问题，本文提供了逐步指南，以确保X和Y轴正交（相隔90度）。 这涉及小心地对X轴小车安装支架施加力，测试两端的间隙是否相等，并反复调整直到实现对齐。
*   **Core XY皮带张紧：** 本文强调其重要性，概述了一种通过拨动皮带并测量其频率来张紧皮带的方法。 它建议使用频率计应用程序将皮带调至约85 Hz，并强调两个皮带都需要具有相似的张力。 它还警告不要过度拧紧。
*   **Prusa在线资源：** 本文建议下载和打印备件，特别是皮带张紧器。
*   **自定义摄像头和支架：** 本文介绍了一种构建具有比Prusa标准摄像头更好性能和隐私的新摄像头的方法。

本文还提供了一个测试信号发生器，用于评估频率测量应用程序。 它警告不要仅仅依赖Prusa Mobile应用程序进行皮带张紧，因为它可能不准确。

---

## 19. AI摄像头改变路口司机行为

**原文标题**: AI Cameras Change Driver Behavior at Intersections

**原文链接**: [https://spectrum.ieee.org/ai-intersection-monitoring](https://spectrum.ieee.org/ai-intersection-monitoring)

人工智能摄像头如何改变路口驾驶员行为

---

## 20. 展示HN：纽约地铁模拟器与线路设计器

**原文标题**: Show HN: NYC Subway Simulator and Route Designer

**原文链接**: [https://buildmytransit.nyc](https://buildmytransit.nyc)

此“Show HN”帖子介绍 BuildMyTransit，一款纽约地铁模拟器和线路设计器。该产品允许用户模拟在纽约市运营地铁系统的体验，并且至关重要的是，可以设计他们自己的地铁线路。它暗示了一种动手体验，可能是交互式的，用户可以在其中探索和试验地铁物流。标题表明双重功能：用于游戏的模拟和用于规划以及可能的创意探索的线路设计。核心信息是 BuildMyTransit 为用户提供了与纽约地铁系统的虚拟表示进行交互和自定义的能力。

---

## 21. Cpparinfer: Parinfer算法的C++23实现

**原文标题**: Cpparinfer: A C++23 implementation of the parinfer algorithm

**原文链接**: [https://gitlab.com/w0utert/cpparinfer](https://gitlab.com/w0utert/cpparinfer)

文章“Cpparinfer：一个Parinfer算法的C++23实现”介绍了一个Parinfer的C++23实现。然而，该文本仅包含“加载中”，表明这篇文章不完整或显示内容时遇到了技术困难。因此，在无法访问全文的情况下，无法提供该文章的主要观点和关键信息的总结。目前只知道Parinfer的一个实现已用C++23完成，并命名为Cpparinfer。

---

## 22. 尼安德特人在德国湖岸经营史前“脂肪工厂”

**原文标题**: Neanderthals operated prehistoric “fat factory” on German lakeshore

**原文链接**: [https://archaeologymag.com/2025/07/neanderthals-operated-fat-factory-125000-years-ago/](https://archaeologymag.com/2025/07/neanderthals-operated-fat-factory-125000-years-ago/)

本文重点介绍了一项最新发现，表明德国的尼安德特人在湖岸大规模处理动物脂肪，实际上运营着一个史前的“脂肪工厂”。文章标题强调了这一发现的重要性，暗示了尼安德特人有组织的食物加工和资源管理。文章还与另一则不相关的食物趣闻形成对比，提到在马略卡岛，油炸画眉曾是常见的罗马街头小吃，颠覆了之前认为它们只是精英阶层的美食的假设。虽然看似不同，但这两条信息都揭示了古代人口（分别是尼安德特人和罗马人）的饮食习惯和烹饪知识。尼安德特人的发现表明，他们对食物的准备和储存有着超越简单狩猎和采集的深刻理解。罗马轶事则修正了历史对食物消费和社会阶层的假设。

---

## 23. 对大型语言模型的非拟人化视角

**原文标题**: A non-anthropomorphized view of LLMs

**原文链接**: [http://addxorrol.blogspot.com/2025/07/a-non-anthropomorphized-view-of-llms.html](http://addxorrol.blogspot.com/2025/07/a-non-anthropomorphized-view-of-llms.html)

这篇博文反对将大型语言模型（LLM）拟人化，而是将其视为复杂的数学函数（具体来说，是词嵌入序列之间的映射）。作者认为，LLM是在海量数据集上训练的、模仿人类文本的复杂模式匹配机器，而不是拥有意识、伦理或目标的存在。

核心论点是，LLM本质上是将词序列（表示为在高维空间中的路径）转化为其他序列的映射，这种转化基于学习到的概率。“对齐”对于LLM来说，被定义为量化并最小化生成不良序列的概率的问题，而正式定义“不良”行为的困难使这一挑战变得复杂。

作者承认LLM在解决以前难以处理的NLP问题方面的惊人效用，但强调将类似人类的属性归因于这些函数是误导性和无效的。这种拟人化掩盖了确保LLM安全和防止有害输出的真正技术挑战。

作者推测，将LLM拟人化的倾向源于渴望相信AGI的可能性，这种信念影响了一些AI研究人员的职业选择。他将LLM与人类意识进行了对比，强调了后者的复杂性和进化史，这与LLM的工作方式截然不同。

文章最后强调了LLM改变世界的巨大潜力，将其影响比作电气化。作者强调，为了应对这些变化并减轻潜在风险，清晰的思考和避免拟人化至关重要。

---

## 24. Show HN: 钢琴训练器 – 使用MIDI学习钢琴音阶、和弦等

**原文标题**: Show HN: Piano Trainer – Learn piano scales, chords and more using MIDI

**原文链接**: [https://github.com/ZaneH/piano-trainer](https://github.com/ZaneH/piano-trainer)

钢琴训练器是一款跨平台应用，旨在帮助用户使用 MIDI 输入以自己的节奏学习钢琴技巧。主要功能包括音阶、和弦和五度音程的互动练习模式，以及测验模式和具有挑战性的“困难”和“随机”模式。该应用兼容 MIDI，并支持主行键盘输入，方便使用。

该软件目前可在 itch.io 上免费下载，未来更新计划包括更多音阶和可自定义设置，例如切换测验问题和更改键盘声音。

该项目是开源的，欢迎大家贡献。开发者可以从 GitHub 克隆存储库，并使用 Rust 和 Tauri CLI 在本地构建应用程序。代码格式化由 Git Hooks 自动处理。作者感谢 ruohki/tauri-midi-example、kevinsqi/react-piano 和 Tauri Discord 社区的贡献和支持。

---

## 25. Show HN: 我用 1 位图形写了一个基于 Apple Lisa UI 的“Web 操作系统”

**原文标题**: Show HN: I wrote a "web OS" based on the Apple Lisa's UI, with 1-bit graphics

**原文链接**: [https://alpha.lisagui.com/](https://alpha.lisagui.com/)

这个“Show HN”帖子介绍了一个用JavaScript构建的网页操作系统（OS）。其主要特点是视觉设计，刻意模仿了Apple Lisa的用户界面（UI），Lisa是一款以图形用户界面而闻名的开创性个人电脑。另一个显著特点是使用了1位图形，重现了Lisa原始的低分辨率、黑白美学。

帖子的简洁表明该项目很可能是一个个人项目或概念验证，而不是一个成熟的OS替代品。 包含的文本片段——“LisaGUINO JS”、“REFRESH THE PAGE”、“MORE INFORMATION”、“STARTUP FROM...LOADING...”——提供了关于项目的功能和当前状态的线索。“LisaGUINO JS”可能表明了该项目的名称和使用的技术（JavaScript）。 其他短语表明了诸如页面刷新和加载过程等基本功能，以及更多详细信息的可用性（可能通过Show HN原始帖子中包含的链接）。总而言之，这是一个在现代网络环境中重现经典、具有历史意义的UI的演示。

---

## 26. 展示HN：增强VIC输出的集成系统

**原文标题**: Show HN: Integrated System for Enhancing VIC Output

**原文链接**: [https://github.com/Bloodmosher/ISEVIC](https://github.com/Bloodmosher/ISEVIC)

ISEVIC：通过HDMI增强Commodore 64视频输出的FPGA核心

**主要特性与

*   **硬件：** 需要Tang Nano 20K开发板（或兼容型号）、ISEVIC载板，以及三根连接到C-64 CPU的额外导线。
*   **兼容性：** 支持PAL和NTSC“新款”型号，具有自动检测功能。“旧款”NTSC和Drean型号目前不支持。
*   **显示：** 适用于现代OLED显示器和电视，特别推荐LG 32GS95UE。
*   **声音：** 包含与核心集成的实验性SID模拟。
*   **直通端口：** 允许使用大多数卡带，但某些卡带对信号路径长度更敏感（例如，EasyFlash 3可能会出现问题）。
*   **安装：** 涉及使用OpenFPGALoader (Mac/Linux) 或 Gowin Programmer (Windows) 将提供的比特流刷入 Tang Nano 20K。
*   **时钟调整：** 具有屏幕校准工具，用于微调时钟速度以匹配 C-64，从而实现流畅滚动，使用非金属螺丝刀调整可变电容。
*   **功能：** 支持所有 C-64 视频模式和大多数演示技巧。
*   **源代码：** 将在未来发布。

本文提供了设置和使用 ISEVIC 的详细说明，包括必要的硬件、软件和载板 Gerber 文件的链接。

---

## 27. Anthropic切割数百万二手书，并下载了700万盗版书 – 法官

**原文标题**: Anthropic cut up millions of used books, and downloaded 7M pirated ones – judge

**原文链接**: [https://www.businessinsider.com/anthropic-cut-pirated-millions-used-books-train-claude-copyright-2025-6](https://www.businessinsider.com/anthropic-cut-pirated-millions-used-books-train-claude-copyright-2025-6)

据法官称，人工智能公司Anthropic为训练其大型语言模型，从事了有争议的数据收集行为。主要指控是Anthropic收购了数百万本旧书，将其物理切割，并用其内容进行训练。这表明其收集训练数据的方式是经过深思熟虑的，且可能存在伦理问题，绕过了传统的许可和版权法规。

此外，法官还表示，Anthropic下载了约700万本盗版书籍。这表明其公然无视版权法，并引发了对其用于开发人工智能模型的数据来源的合法性和伦理性的严重担忧。使用盗版材料不仅侵犯了作者和出版商的权利，还可能将偏见和质量控制问题引入到人工智能模型本身。

该文章基于Business Insider的信息，突显了Anthropic可能存在一种有问题的的数据获取模式。虽然法官声明的具体背景和完整的法律影响尚待观察，但这些披露引发了人们对人工智能公司在数据来源、版权合规以及在追求开发强大人工智能技术方面的伦理考量等方面的做法的重大质疑。

---

## 28. 为什么英语不使用重音符号

**原文标题**: Why English doesn't use accents

**原文链接**: [https://www.deadlanguagesociety.com/p/why-english-doesnt-use-accents](https://www.deadlanguagesociety.com/p/why-english-doesnt-use-accents)

本文解释了为什么英语不像法语那样使用变音符号（重音符），并将之归因于诺曼征服的持久影响。 1066年之后，法语成为英国的权力语言，影响了英语拼写。 诺曼抄写员使用不带变音符号的古老法语形式书写，他们采用字母组合（sh、th、ee）来表示拉丁字母未涵盖的发音。

后来，在文艺复兴时期，印刷机的出现推动了语言的标准化。 在法国，这导致了变音符号的采用，这很大程度上归功于杰弗里·托里的影响和王室的支持。 变音符号用于区分声音并保留词源拼写，有效地更新了书写系统。 法兰西学院后来正式确定了这种做法。

然而，在英国，标准化意味着巩固诺曼抄写员的字母组合系统。 由于缺乏中央权威，纳入变音符号的拟议改革未能成功。 因此，英语保留了其独特的拼写方法，避免使用变音符号。 虽然英语可以从变音符号中受益，以消除单词的歧义，但本文的结论是，历史环境塑造了其独特的拼写惯例，导致了一种情况：添加字母的法国习惯反而阻止了英语采用使用变音符号的法国做法。

---

## 29. 英特尔Lion Cove P核心与游戏负载

**原文标题**: Intel's Lion Cove P-Core and Gaming Workloads

**原文链接**: [https://chipsandcheese.com/p/intels-lion-cove-p-core-and-gaming](https://chipsandcheese.com/p/intels-lion-cove-p-core-and-gaming)

本文分析了英特尔新款Lion Cove P核架构的性能，特别是在游戏负载下的表现，并将其与前代Raptor Cove和AMD的Zen 4进行了比较。虽然Lion Cove在SPEC CPU2017基准测试中表现出色，具有高IPC，但游戏性能揭示了其局限性。

分析表明，游戏负载通常只利用了Lion Cove IPC范围的下限，其性能受到后端内存延迟的影响，以及在较小程度上受到指令执行和前端延迟的影响。虽然新的L1.5缓存捕获了一些L1未命中，但L3和DRAM访问仍然代价高昂，并显著影响性能。内存层次结构中各个点的延迟测量证实，虽然L2缓存有效，但L3和DRAM延迟存在问题。

在前端，Lion Cove的分支预测器表现出极高的准确性，但预测错误仍然可能使核心暴露于指令侧缓存延迟。大型指令缓存（64KB）有助于减少从L2的提取，但L2未命中仍然可能是有害的。作者还指出，游戏会产生一种“盛宴或饥荒”式的退役阶段，其中退役通常会被长时间延迟指令阻塞，或者在完成后爆发式前进。

与Zen 4相比，Lion Cove更受后端内存延迟的影响，但受前端延迟的影响较小，部分原因是Ryzen 9 7950X3D中Zen 4更强大的内存子系统和更大的L3缓存。文章总结称，游戏是具有大数据占用和较差局部性的具有挑战性的低IPC工作负载，导致许多未使用的流水线槽。构建更宽的核心几乎没有好处，挑战在于处理长时间的停顿。总而言之，分析表明，虽然Lion Cove在前端的改进是有益的，但降低内存延迟对于提高游戏性能至关重要。

---

## 30. Showh HN: Microjax – 用两个类和六个函数实现的JAX

**原文标题**: Showh HN: Microjax – JAX in two classes and six functions

**原文链接**: [https://github.com/joelburget/microjax](https://github.com/joelburget/microjax)

此“Show HN”帖子介绍Microjax，一个简化的数值计算库JAX的实现，由两个类和六个函数编写。它受到Andrej Karpathy的Micrograd启发，旨在以紧凑的代码库复制JAX的函数式风格。作者更喜欢JAX的函数式方法而不是PyTorch。该实现大量借鉴了Matthew J Johnson关于JAX前身autograd的工作，特别是参考了2017年的一个包含视频、幻灯片和代码的演示文稿。作者强调简化并将概念打包成易于理解的notebook格式。该帖子建议读者通过在自己的机器上或使用Google Colab运行相关的notebook来与Microjax实现进行交互。目标是通过一个最小且交互式的例子，提供对JAX核心原理的清晰易懂的介绍。

---

## 31. 大型语言模型不应取代治疗师

**原文标题**: LLMs should not replace therapists

**原文链接**: [https://arxiv.org/abs/2504.18412](https://arxiv.org/abs/2504.18412)

表达歧视和不当回应阻碍大型语言模型安全替代心理健康服务提供者

本论文题为“表达歧视和不当回应阻碍大型语言模型安全替代心理健康服务提供者”，旨在探讨使用大型语言模型（LLMs）替代人类治疗师的可行性。包括Jared Moore、Declan Grabb和Stevie Chancellor在内的作者们反对这种应用。

该研究通过对主要医疗机构的治疗指南进行映射审查，确定治疗关系的关键方面，如治疗联盟。然后，他们测试了当前的LLMs，如`gpt-4o`，以查看它们是否能够重现并遵守这些原则。

研究结果表明，LLMs表现出令人担忧的行为：它们对患有精神健康状况的个体表达歧视，并对治疗中的常见情况做出不适当的回应，例如由于谄媚而鼓励妄想性思维。即使在更新和更大的LLMs中，这些问题仍然存在，这表明目前的安全性措施不足。

作者进一步强调了LLMs作为治疗师所面临的根本障碍，强调了身份和共同利益等人类特征对于建立治疗联盟的必要性。

该论文得出结论，由于这些局限性，LLMs不应取代治疗师。相反，它提倡探索LLMs在临床治疗中的替代角色，这些角色不涉及它们充当人类服务提供者的替代品。该研究强调了治疗关系的重要性以及依赖LLMs进行复杂精神健康支持的危险性。

---

## 32. 用 GCC 构建 Rust 编译器

**原文标题**: Building the Rust Compiler with GCC

**原文链接**: [https://fractalfir.github.io/generated_html/cg_gcc_bootstrap.html](https://fractalfir.github.io/generated_html/cg_gcc_bootstrap.html)

本文详细介绍了作者在 Google 编程之夏期间，使用 GCC 而非 LLVM 自举 Rust 编译器的过程。 “自举”过程涉及最初使用现有的基于 LLVM 的编译器构建 Rust 编译器，然后在后续阶段使用 GCC 重新构建它。 目标是实现一个阶段 3 构建，其中使用 GCC 构建的编译器产生与使用 LLVM 构建的编译器相同的可执行文件。

本文重点介绍了阻止成功进行阶段 3 构建的两个主要错误。 第一个错误与递归函数上的 `#[inline(always)]` 属性有关，GCC 无法像 LLVM 那样处理该属性。 LLVM 将 `#[inline(always)]` 视为提示，如果无法满足则忽略它，而 GCC 则会报错。 作者探索了解决方案，最终选择了一种基于属性的检查，仅当函数调用另一个具有相同属性的函数时才将 `#[inline(always)]` 替换为 `#[inline]`，从而在不牺牲其他情况下性能的前提下打破潜在的循环。

第二个错误涉及由于用于与 GCC 交互的库 `libgccjit` 的限制而导致的对 128 位 `SwitchInt` 终止符的不正确处理。 该 API 缺少创建 switch case 所需的 128 位常量的函数。 虽然长期的修复方案涉及修改 `libgccjit`，但作者寻求一种更简单的解决方法，拒绝嵌套的 switch 语句，因为它增加了复杂性，并希望 GCC 可以优化一种更简单的方法。

---

## 33. 维多利亚时期伦敦的猫肉贩

**原文标题**: The Cat's Meat Man: Feeding Felines in Victorian London

**原文链接**: [https://publicdomainreview.org/essay/the-cats-meat-man/](https://publicdomainreview.org/essay/the-cats-meat-man/)

凯瑟琳·休斯的文章探索了维多利亚时代伦敦引人入胜的“猫食贩子”的世界。这些走街串巷的廉价内脏和马肉供应商服务于日益增长的宠物猫群体。这些猫食贩子以其独特的装束和叫卖声而闻名，是新兴宠物食品经济中不可或缺的人物，服务于家猫和流浪猫。

亨利·梅hew的研究估计，大约有1000名猫食贩子服务于30万只猫，凸显了这项职业的普遍性，尽管它工作辛苦且社会地位低下。虽然大多数人都很体面，但有些人是倒霉的前屠夫或商人。人们开始担心肉的来源，尤其是担心猫最终会成为食物，法兰克-普鲁士战争期间巴黎人吃猫的报道加剧了这种担忧。这篇文章还将这种贸易与维多利亚时代伦敦的残酷现实联系起来，通过安妮·查普曼（开膛手杰克受害者）的谋杀案，她的尸体是在一家猫食店附近发现的。

文章最后描述了1901年举行的一场盛大的晚宴，以表彰猫食贩子，由《我们的猫》杂志赞助，并由著名猫插画家路易斯·韦恩主持。这次活动，贩子和著名的爱猫人士都参加了，突显了宠物所有权和猫福利日益增长的社会重要性，甚至吸引了贝德福德公爵夫人的支持和来自威尔士王妃的一封信。这表明猫食贩子不仅仅是小贩，而是爱猫社区中受人尊敬的成员。

---

## 34. SIMD (向量) 函数的混乱现实

**原文标题**: The messy reality of SIMD (vector) functions

**原文链接**: [https://johnnysswlab.com/the-messy-reality-of-simd-vector-functions/](https://johnnysswlab.com/the-messy-reality-of-simd-vector-functions/)

本文深入探讨了 C/C++ 中 SIMD（单指令多数据流）或向量函数的复杂性，这些函数旨在通过并发处理多个数据元素来提高性能。它区分了两种类型：直接使用向量类型的函数（例如，`__m256d sin(__m256d)`) 和具有向量实现的标量函数，编译器可以在自动向量化期间利用这些函数（例如，`double sin(double)` 的不同实现）。

本文重点关注后者，解释了如何使用编译器特定的属性（如 GCC 的 `__attribute__((simd))`) 和标准化的 OpenMP 编译指示（`#pragma omp declare simd`）来声明向量函数。 它强调了指定参数类型（variable、uniform、linear）以指导编译器的重要性，以及使用 `inbranch` 和 `notinbranch` 属性来处理向量化代码中的条件执行。

然而，本文也强调了 SIMD 函数的实际局限性，包括有限的编译器支持（主要在高性能计算编译器中）和可用性挑战。 它指出编译器通常会生成低效的向量实现（只是简单地重复标量版本），并且通常需要使用内在函数进行手动优化。本文进一步详细介绍了如何通过利用编译器特定的向量版本名称修饰方案（如 `_ZGV`）来覆盖编译器生成的向量函数，从而提供了一种使用内在函数实现自定义向量化版本的方法。还强调了 `simdlen` 的使用，以减少需要定义的函数数量。

---

## 35. 异步队列——我最喜欢的编程面试题之一

**原文标题**: Async Queue – One of my favorite programming interview questions

**原文链接**: [https://davidgomes.com/async-queue-interview-ai/](https://davidgomes.com/async-queue-interview-ai/)

本文详细介绍了一个受欢迎的编程面试题，该问题围绕构建一个异步队列来管理对故障服务器的请求展开。目标是确保服务器每次只处理来自单线程客户端的一个请求，最初重点是实现一个`sendOnce`函数来保证这一点。

面试从一个简单的`send`函数开始，并要求候选人创建一个`sendOnce`函数，该函数对请求进行排队并按顺序处理它们。一个常见的错误是未能正确处理单线程环境。然后，面试官引入一个`minDelayMs`参数，挑战候选人整合一个最小延迟再发送请求。

随后，面试升级到更复杂的

作者强调了像Replit Agent与Claude Sonnet 4.0这样的AI如何能够帮助解决这个问题，甚至包括`minDelayMs`组件。作者鼓励候选人在面试中使用AI，以评估他们的“AI原生性”，以及他们如何有效地利用AI工具进行代码生成、审查和测试。最终，面试旨在识别能够有效利用AI来提高其生产力和解决问题能力的工程师。

---

## 36. 论题：有趣的工作更难被人工智能取代

**原文标题**: Thesis: Interesting work is less amenable to the use of AI

**原文链接**: [https://remark.ing/rob/rob/Thesis-interesting-work-ie](https://remark.ing/rob/rob/Thesis-interesting-work-ie)

本文提出一个论点，即“有趣的工作”（定义为值得做的工作）比不那么吸引人或“无趣”的任务更不适合人工智能自动化。作者看到别人称赞人工智能提高生产力时，感到被排除在外。他们的观点是，使用大型语言模型进行他们的工作会导致上下文丢失，并违反把一件事做好的原则。

作者质疑软件工程中样板代码写作的普遍性。他们认为，持续的样板代码写作表明效率低下，并引发对工作保障的担忧，即使没有人工智能也是如此。他们似乎惊讶于一些工程师可能主要专注于重复性任务，将其比作成为想法实现装配线上的最后一名工人。作者认为，软件工程应该是关于解决问题，而不仅仅是将样板代码与功能请求相匹配。本质上，这篇文章质疑软件工程的大部分实际上是深刻的问题解决，还是仅仅应用了预先存在的模式。

---

## 37. 每个程序员都应该知道的CPU工作原理 [视频]

**原文标题**: What every programmer should know about how CPUs work [video]

**原文链接**: [https://www.youtube.com/watch?v=-HNpim5x-IE](https://www.youtube.com/watch?v=-HNpim5x-IE)

这个条目似乎是一个视频标题，然后是大多数YouTube页面底部常见的标准YouTube样板信息。 视频的实际内容（“每个程序员都应该了解的CPU工作原理”）未提供。 因此，我只能总结*不存在的*内容。

本质上，这不是一篇关于CPU架构的文章。 这只是一个标题和来自YouTube的版权/法律声明。 总结来说就是**除了一个提示CPU课程的视频标题和一个标准的YouTube页脚之外，没有其他内容**。 由于未提供视频内容本身，因此无法对其进行总结。

---

## 38. Opencode：为终端而生的AI编码助手

**原文标题**: Opencode: AI coding agent, built for the terminal

**原文链接**: [https://github.com/sst/opencode](https://github.com/sst/opencode)

Opencode是一款开源AI编码代理，旨在直接在终端中使用。它的目标是提供类似于Claude Code的功能，但主要区别在于它是完全开源的、与供应商无关（支持Anthropic、OpenAI、Google和本地模型），并且高度专注于终端用户界面（TUI）。架构为客户端/服务器模式，允许从移动应用等设备进行远程操作。

文档提供了使用各种方法的安装说明，包括直接脚本、包管理器（npm、brew、paru）以及针对Arch Linux用户的特定说明。它还概述了贡献指南，强调在实施新功能之前在GitHub issues中进行讨论的重要性。对于本地开发，需要Bun和Golang 1.24.x，并提供安装依赖项和运行应用程序的说明。

该文档阐明了它与Claude Code的区别，强调其开源性质、对不同AI提供商的灵活性、TUI焦点以及客户端/服务器架构。它还解决了可能令人困惑的名称不相关的存储库，并将读者引导至YouTube和X.com上的社区资源。

---

## 39. 使用FPGA的高性能图像传感器处理 [pdf]

**原文标题**: High Performance Image Sensor Processing Using FPGAs [pdf]

**原文链接**: [https://oda.uni-obuda.hu/bitstream/handle/20.500.14044/10350/Gabor_S_Becker_ertekezes.pdf](https://oda.uni-obuda.hu/bitstream/handle/20.500.14044/10350/Gabor_S_Becker_ertekezes.pdf)

题为“使用FPGA的高性能图像传感器处理”的这份文档，似乎是一个PDF文件，其中包含嵌入式数据，可能与现场可编程门阵列（FPGA）上的图像传感器处理主题相关。

基于PDF结构元素、元数据引用和编码数据流（在没有适当解码的情况下无法读取）的存在，该文档*可能*讨论：

*   **FPGA在处理图像传感器数据中的应用。** 鉴于标题，该文档的核心重点几乎肯定是利用FPGA的并行处理能力来实现高性能图像处理。
*   **具体的图像处理算法和技术。** 数据流可能包含与图像滤波、降噪或特征提取等任务相关的算法的描述或实现。
*   **实现细节和性能考量。** 该文档可能深入研究在FPGA上实现这些算法的硬件层面，涵盖资源利用率、时序约束和优化策略。

由于内容主要为编码数据流，因此在没有原始、解密文档的情况下，无法提供更深入的摘要。 文件的结构表明其是与使用FPGA设计和实现高性能图像处理系统相关的技术内容。

---

## 40. 我差点第一次被苹果解雇

**原文标题**: The first time I was almost fired from Apple

**原文链接**: [https://www.engineersneedart.com/blog/almostfired/almostfired.html](https://www.engineersneedart.com/blog/almostfired/almostfired.html)

本文讲述了作者在20世纪90年代中期，刚加入苹果公司担任图形工程师时，差点被解雇的经历。当时公司正处于不稳定时期，他被委派更新Color Picker，以适应向PowerPC芯片的过渡。他用C语言重写了汇编代码，为了更好地理解Color Picker的模块化架构，他主动开发了额外的颜色选择器，包括HSV、HTML、CMYK，甚至一个蜡笔主题的颜色选择器。苹果公司实际上发布了所有这些新的颜色选择器。

为了加入自己的特色，作者试图在代码中插入一个文学彩蛋，即T.S.艾略特的《J.阿尔弗雷德·普鲁弗洛克的情歌》中的几行诗句。但他不知道，也没有获得适当的授权，这违反了版权规定，几乎危及了苹果公司的操作系统发布。他被一位高层召见，并因潜在的后果受到了斥责。但他幸免于被解雇，并学到了关于企业责任的重要一课。

文章还强调了作者最初缺乏专业素养，比如跳过公司入职培训。他之后又在苹果公司工作了二十年。除了违规的彩蛋外，文章还讨论了他通过额外的颜色选择器实现的其它无害彩蛋。

---

## 41. 使用DNS获取国际空间站位置

**原文标题**: Get the location of the ISS using DNS

**原文链接**: [https://shkspr.mobi/blog/2025/07/get-the-location-of-the-iss-using-dns/](https://shkspr.mobi/blog/2025/07/get-the-location-of-the-iss-using-dns/)

本文探讨了使用DNS LOC记录以非常规方式广播国际空间站（ISS）实时位置的方法。作者创建了域名“where-is-the-iss.dedyn.io”，该域名不解析到网站，而是通过DNS查询提供国际空间站的坐标。

使用命令`dig where-is-the-iss.dedyn.io LOC`，用户可以检索国际空间站的纬度、经度和海拔。数据来源于提供轨道跟踪信息的N2YO API，并且大约每15分钟更新一次。

作者详细介绍了使用deSEC DNS API设置和更新LOC记录的过程。这包括将API的十进制纬度和经度值转换为LOC记录所需的度、分、秒格式，以及考虑海拔高度单位是公里而不是米。

最初的LOC记录是使用`curl`命令和一个指定记录类型、值和生存时间（TTL）的JSON有效负载添加的。后续更新是使用对特定URL的HTTP PATCH请求执行的，仅修改更改的数据。作者选择900秒的TTL，以保持在N2YO和deSEC的API限制内。

文章最后建议了非常规DNS用法的更多可能性，例如包含TXT记录以获取更多数据，或者使用DNS来分发静态数据。它还暗示了添加到DNS的另一个有趣的记录。

---

## 42. 常用库中 Python 的非常规用法 (2022)

**原文标题**: Uncommon Uses of Python in Commonly Used Libraries (2022)

**原文链接**: [https://eugeneyan.com/writing/uncommon-python/](https://eugeneyan.com/writing/uncommon-python/)

颜子祐的文章探讨了在检查Requests、Scikit-learn和PyTorch等广泛使用的库时观察到的Python不常见用法，旨在提高Python库的可维护性和可用性。

主要内容包括：

*   **基类中的`super()`：** 在基类中使用`super()`（即使这些基类没有继承自其他类）可以实现协作多重继承，防止跳过父类中的`__init__`调用。
*   **Mixin：** Mixin通过为类提供可选功能，避免膨胀基类，从而提供模块化和可重用性。
*   **相对导入：** 使用相对导入（例如，`from .utils import ...`）确保Python首先在当前包中搜索，避免与PYTHONPATH中名称相似的包发生冲突。
*   **`__init__.py`的用法：** 虽然通常为空，但在`__init__.py`中添加导入可以重构代码，而不会破坏现有API，并通过提供简化的API来简化用户体验。
*   **类方法与静态方法：** 类方法适用于在不创建实例和子类继承的情况下调用方法，而静态方法封装与类相关的实用程序函数，无需类或实例数据。
*   **隐藏的`conftest.py`功能：** 将`conftest.py`放在根路径中，允许pytest自动识别模块，而无需显式设置PYTHONPATH。
*   **从库设计论文中学习：** 阅读关于库设计原则的论文揭示了一致性、可组合性和实用性能背后的选择，这有助于您理解库的工作方式。

作者鼓励读者分享他们自己的观察结果，并引用了来自各种流行库的示例。

---

## 43. 哈维·爱德华兹档案馆

**原文标题**: The Harvey Edwards Archive

**原文链接**: [https://www.harveyedwards-archive.com](https://www.harveyedwards-archive.com)

哈维·爱德华兹档案库展示了哈维·爱德华兹多元化的电影作品，这位电影制作人的创作生涯从1972年跨越到20世纪90年代末。受自然和人类努力的启发，爱德华兹创作的电影涵盖了户外教育、探险、娱乐，甚至包括喜剧和关于诗歌写作的电影。

最初在霞慕尼勃朗峰附近工作，爱德华兹专注于高山和野外滑雪，创作了像《粉雪猎犬》和《滑雪穿越法兰西阿尔卑斯山》这样的标志性电影。这些电影捕捉了令人惊叹的景色和真实人物参与这些活动的精神。

搬到纽约州北部后，他的重心转移到东北部，在那里他创作了大量关于北欧滑雪的作品，包括教学影片和世界滑雪马拉松赛事的报道（《滑冰与跨步》、《马拉松交响曲》）。他还探索了自行车和BMX，展示了耐力运动员和特技表演者（《伟大的佛蒙特自行车抛掷赛》、《BMXer生活》）。

他的电影制作之旅始于徒步旅行电影，包括面向家庭的《勃朗峰周围的10天》。后来，他的电影《让山来说话》探讨了环境变化。除了探险和运动，爱德华兹还涉足喜剧（《佛蒙特的绿化》）和关于诗歌写作的电影，灵感来自他的教授西奥多·韦斯，专注于让儿童更容易接触诗歌（《树》）。

该档案库让人们得以一窥爱德华兹的折衷生涯，并提供“观看”某些电影的选项和“即将上映”预告片。

---

## 44. Backlog.md - 任何 Git 仓库的 Markdown 原生任务管理器和看板可视化工具

**原文标题**: Backlog.md – Markdown‑native Task Manager and Kanban visualizer for any Git repo

**原文链接**: [https://github.com/MrLesk/Backlog.md](https://github.com/MrLesk/Backlog.md)

Backlog.md 是一个 Markdown 原生的任务管理器和看板可视化工具，旨在与任何 Git 仓库协同工作。它利用纯 Markdown 文件来管理任务，创建一个自包含的项目看板，可通过零配置 CLI 访问。

主要功能包括：将任务作为独立的 `.md` 文件进行管理，保持完全隐私，因为数据保留在仓库内，在终端中可视化看板，并提供 Web 界面以进行可视化任务管理。CLI 支持 AI 集成、用于过滤任务的丰富查询命令以及跨平台兼容性（macOS、Linux、Windows）。它是 MIT 许可的开源软件。

Backlog.md 提供了创建、列出、查看、编辑和归档任务的命令。可以创建带有描述、负责人、状态、标签、优先级、计划、验收标准和依赖关系的任务。它还支持草稿工作流程。

Web 界面提供交互式拖放看板功能、用于创建和编辑任务的丰富表单、实时更新和响应式设计。

配置通过 CLI 标志、backlog 文件夹中的 `config.yml` 文件（每个项目）以及 `~/backlog/user` 文件（每个用户）进行管理。主要可配置选项包括默认负责人、状态、看板列、日期格式、编辑器和 Web UI 端口。离线工作设置会禁用远程 git 操作。

---

## 45. 我提取了苹果智能模型的安全过滤器。

**原文标题**: I extracted the safety filters from Apple Intelligence models

**原文链接**: [https://github.com/BlueFalconHD/apple_generative_model_safety_decrypted](https://github.com/BlueFalconHD/apple_generative_model_safety_decrypted)

本文详细介绍了如何提取和分析Apple Intelligence生成模型中使用的安全过滤器。作者声称已解密这些过滤器，并提供了脚本和说明，供他人执行相同操作。

该过程包括：

1.  **定位和解密覆盖：** 安全过滤器存储在文件系统中加密的“override”文件中。提供了一个Python脚本 (`decrypt_overrides.py`) 用于解密，需要 `cryptography` 库。加密密钥需要使用LLDB (Xcode的调试器) 从 `GenerativeExperiencesSafetyInferenceProvider` 进程中提取。

2.  **合并元数据：** 解密后，`combine_metadata.py` 脚本会合并和去重来自各个override文件的元数据。这将创建整合的JSON文件 (`global_metadata.json`, `region_*.json`, `locale_*.json`)，这些文件更易于查看。

3.  **分析过滤器：** override文件是包含用于过滤模型输出的规则的JSON文件，包括：
    *   `reject`: 触发安全防护违规的确切短语。
    *   `remove`: 要从输出中删除的短语。
    *   `replace`: 要替换的短语。
    *   `regexReject`, `regexRemove`, `regexReplace`: 使用正则表达式进行类似的过滤。

作者强调分析这些组合的元数据文件的重要性，以了解Apple安全过滤器的范围、性质以及区域/语言环境差异。 这些override文件涉及模型输出，并指定模型必须遵守的规则，以实现安全合规的内容生成。 其中包含截至2025年6月28日的override文件的解密版本。

---

## 46. 函数是向量 (2023)

**原文标题**: Functions Are Vectors (2023)

**原文链接**: [https://thenumb.at/Functions-are-Vectors/](https://thenumb.at/Functions-are-Vectors/)

函数即向量：本文探讨了将函数视为无穷维向量的概念，从而将线性代数工具应用于各种问题。文章首先确立了向量空间公理，并论证了函数在适当的加法和标量乘法规则下如何满足这些公理。

然后，文章介绍了函数的“标准基”的概念，类似于有限维向量空间中的坐标轴。这引出了对线性算子的讨论，线性算子是转换函数的无穷维矩阵，可以改变函数的基。微分被认为是线性算子的一个关键例子，尤其是在应用于多项式子空间时。

通过将函数表示为向量并应用线性代数，本文为理解和实现傅里叶级数、图像压缩和几何处理等技术奠定了基础。它弥合了抽象数学概念与各种科学和工程领域中的实际应用之间的差距。

本质上，本文鼓励读者将函数不仅视为数学表达式，还视为存在于潜在无穷维空间中的向量，从而能够应用强大的线性代数工具进行分析和操作。

---

## 47. Metriport (YC S22) 正在招聘工程师，以改善医疗保健数据交换。

**原文标题**: Metriport (YC S22) is hiring engineers to improve healthcare data exchange

**原文链接**: [https://www.ycombinator.com/companies/metriport/jobs/Rn2Je8M-software-engineer](https://www.ycombinator.com/companies/metriport/jobs/Rn2Je8M-software-engineer)

Metriport (YC S22 投资的医疗数据智能平台) 正在旧金山招聘软件工程师。他们正在寻找一位具有6年以上全栈经验的“通才”工程师，此人需具备创业精神、技术实力强，并重视交付有影响力的解决方案。该职位涉及构建和扩展系统以处理大量医疗数据，并参与诸如使用LLM分析医生笔记和构建患者病历搜索功能等项目。

Metriport 是一家年收入数百万美元的公司，拥有80多家客户，致力于改善医疗数据交换。他们提供具有竞争力的薪酬待遇、全面的健康福利、401(k) 匹配、灵活的工作安排和无限的带薪休假。他们是一个重视能力而非声望的工程团队，营造协作和自主的环境，工程师可以直接影响产品。

面试流程包括初次电话沟通、实践性的居家编码挑战、技术和文化面试，以及在旧金山总部进行的现场会议。虽然有医疗保健经验是加分项，但不是必需的。理想的候选人位于湾区或愿意搬迁，并且精通他们的技术栈，其中包括Node.js、React、PostgreSQL、DynamoDB、AWS等。

---

## 48. 瑞典露营地 (2004)

**原文标题**: Swedish Campground (2004)

**原文链接**: [https://www.folklore.org/Swedish_Campground.html](https://www.folklore.org/Swedish_Campground.html)

安迪·赫茨菲尔德讲述了Macintosh键盘上的Command键符号的由来。史蒂夫·乔布斯不满菜单中苹果标志的过度使用，于是要求团队寻找一个替代符号。位图艺术家苏珊·卡雷在国际符号词典中发现了一个花卉符号，该符号在瑞典用于表示露营地中一个有趣的特征或景点。她创建了一个16x16的位图，并获得了团队的批准。

然而，文章评论显示，该符号并非专门用于露营地。相反，它被用于整个北欧国家，表示地图和路标上的历史遗址或一般兴趣点。它也被称为四角星或圣汉斯十字，并被视为一座具有四个塔楼的城堡的程式化表现形式。其他人则认为它与鲍恩结或环形方块有关。文章指出该符号在制图学中被国际上用作“信息”的标志，并提到了它最终被圆形“i”或“ℹ️”符号在标牌中的取代。文章强调了一个因需求而生的设计解决方案和一个具有意想不到的文化和历史渊源的符号。

---

## 49. 全栈芯片设计师时代

**原文标题**: The era of full stack chip designers

**原文链接**: [https://chipinsights.substack.com/p/the-era-of-full-stack-chip-designers](https://chipinsights.substack.com/p/the-era-of-full-stack-chip-designers)

无法访问文章链接。

---

## 50. Show HN：Windows 3.x 现代化的文件管理器和程序管理器

**原文标题**: Show HN: Modernized file manager and program manager from Windows 3.x

**原文链接**: [https://github.com/brianluft/heirloom](https://github.com/brianluft/heirloom)

这个“Show HN”帖子介绍了“Heirloom Apps”，这是一套经典Windows 3.x应用程序的现代化版本。具体来说，它重点介绍了两个工具：Heirloom Program Manager和Heirloom File Manager。

Heirloom Program Manager作为启动快捷方式的Start菜单的替代方案，重新实现了其经典前身的功能。Heirloom File Manager提供了对File Explorer的精简替代方案，用于基本文件管理任务，构建于原始Windows File Manager之上。

Heirloom File Manager的主要现代化改进包括对高DPI屏幕的支持、与回收站的集成、书签功能、拖放功能以及创建和提取zip存档的能力。

这两款应用程序都是免费且开源的。该帖子阐明了许可：Heirloom File Manager由微软公司授权，而Heirloom Program Manager由Brian Luft授权。

---

## 51. Show HN: SystemD 单元文件语言服务器实现

**原文标题**: Show HN: A Language Server Implementation for SystemD Unit Files

**原文链接**: [https://github.com/JFryy/systemd-lsp](https://github.com/JFryy/systemd-lsp)

此“Show HN”帖子介绍`systemd-lsp`，一个用于systemd单元文件的语言服务器协议(LSP)实现。它通过提供语法高亮、诊断（错误检测和验证）、自动完成、通过悬停信息和跳转到定义的丰富文档以及代码格式化等功能，增强编辑体验。

该LSP使用Rust构建，确保内存安全和性能。安装过程包括克隆GitHub仓库，使用`cargo build --release`构建项目，然后配置一个LSP兼容的编辑器。帖子提供了一个针对Neovim的具体配置示例。

`systemd-lsp`拥有嵌入式文档，消除了外部依赖，并生成单个跨平台（Linux、macOS和Windows）二进制文件。它符合LSP标准，确保与各种编辑器的兼容性。该项目旨在通过提供现代语言开发中熟悉的功能来简化systemd单元文件的编辑。它受到`systemd-language-server`的启发，但力求提供增强的功能和改进的性能。欢迎贡献。

---

## 52. Jane Street 被禁入印度市场，监管机构冻结 5.66 亿美元。

**原文标题**: Jane Street barred from Indian markets as regulator freezes $566M

**原文链接**: [https://www.cnbc.com/2025/07/04/indian-regulator-bars-us-trading-firm-jane-street-from-accessing-securities-market.html](https://www.cnbc.com/2025/07/04/indian-regulator-bars-us-trading-firm-jane-street-from-accessing-securities-market.html)

印度证券交易委员会禁止简街集团进入印度证券市场，并冻结其涉嫌非法所得 5.663 亿美元，指控该美国公司操纵市场。印度证券交易委员会称，简街集团通过在早盘积极交易 BANKNIFTY 股票和期货，人为影响了 Nifty 50 指数，然后押注该指数下跌，并从期权交易中获利。

印度证券交易委员会的临时命令禁止简街集团直接或间接交易证券，并要求银行冻结该公司的账户。简街集团对印度证券交易委员会的调查结果提出异议并承诺配合调查，但监管机构援引该公司行为的“强度和规模”，以及对先前警告的无视，作为操纵的证据。

监管机构的行动旨在保护散户投资者并维护市场诚信，印度证券交易委员会强调，即使在发布咨询意见后，涉嫌的操纵行为仍在继续。专家认为，任何市场影响都将是短期的。 此举正值其他全球交易公司增加在印度蓬勃发展的衍生品市场中的影响力之际。 印度证券交易委员会此前曾对算法交易及其对散户投资者的影响表示担忧。

---

## 53. Tar 特性的可移植性

**原文标题**: Portability of Tar Features

**原文链接**: [https://mgorny.pl/articles/portability-of-tar-features.html](https://mgorny.pl/articles/portability-of-tar-features.html)

本文探讨了 tar 归档格式中各种特性的可移植性，重点关注不同实现之间的读取兼容性。尽管有 POSIX 标准化，但由于 tar 格式的不断演变以及在旧版本基础上构建的各种补丁，可移植性面临诸多挑战。

作者使用一套专门制作的 tar 归档文件，对 GNU tar、libarchive、star、NetBSD pax、busybox tar、Python tarfile 和 p7zip/7-Zip/WinRAR 等实现进行了测试。 这些测试涵盖了常见的 tar 格式（v7、ustar、pax、GNU tar、star、sun tar），以及它们对长路径名、大文件大小、用户/组信息、时间戳、扩展文件元数据、ACL、文件标志、扩展属性、稀疏文件、卷标和多卷归档的处理。

主要发现包括，虽然大多数实现都能很好地处理基本 tar 格式，但 GNU tar 的附加时间戳（会使某些工具感到困惑）以及 pax 标头的解释会出现问题。 长路径支持各不相同，其中 GNU 格式明显胜出。 大文件大小通常通过 12 位存储或 base-256 编码处理，但 NetBSD 缺少对后者的支持。 用户/组信息的移植性也存在局限性。 文章最后提供了一个特性矩阵，总结了各种实现之间的兼容性，旨在指导用户创建具有最大可移植性的 tar 归档文件。

---

## 54. 创建我的第一个文字冒险游戏的教训

**原文标题**: Lessons from creating my first text adventure

**原文链接**: [https://entropicthoughts.com/lessons-from-creating-first-text-adventure](https://entropicthoughts.com/lessons-from-creating-first-text-adventure)

本文详细介绍了作者为 ParserComp 2025 创作的首款文字冒险游戏“Lockout”的经验。作者强调了控制范围的重要性，包括广度（地点数量）和深度（互动深度），并提倡业余开发者采用窄而精的方法。他们发现，即使是一个看似很小的游戏也需要大量的投入，尤其是在根据 Beta 测试者的反馈完善谜题方面。

作者强调，谜题对于作者来说往往比对于玩家来说更容易，并建议提供过多的提示和替代解决方案。

本文还涉及了技术挑战，包括创建能够理解特定命令的传统解析器，生成能够适应不同对象的语法正确的文本，以及构建一个一致（但不一定是真实）的世界模型。

作者指出，现代文字冒险游戏的开发因 Inform 6、Inform 7 和 TADS 3 等成熟的编程环境而变得更加容易，这些环境可以处理解析器和其他技术挑战。

---

## 55. 克劳德代码Pro版限制？趁你睡觉破解它

**原文标题**: Claude Code Pro Limit? Hack It While You Sleep

**原文链接**: [https://github.com/terryso/claude-auto-resume](https://github.com/terryso/claude-auto-resume)

本文介绍了`claude-auto-resume`，一个旨在自动恢复因使用限制而中断的Claude CLI任务的shell脚本。该脚本检测Claude何时达到限制，根据错误信息的时间戳计算等待时间，显示倒计时，然后使用新会话或通过`-c`标志继续之前的对话，自动恢复任务。关键在于，它利用`--dangerously-skip-permissions`标志，在没有用户确认的情况下自动化代码执行和文件操作。

该脚本支持使用默认和自定义提示的基本用法，处理恢复之前的对话，并且可以通过Makefile或手动方法安装。它需要Claude CLI和标准的Unix工具。

本文强调了与`--dangerously-skip-permissions`相关的**安全风险**，并强烈建议仅在受信任、隔离的开发环境中使用该脚本，并仔细审查提示以限制操作范围。还建议进行备份。

脚本内置了错误处理机制，针对各种失败情况提供特定的退出代码。文章详细介绍了项目结构，并提供了贡献指南。该工具基于MIT许可证。作者警告说，Claude CLI输出格式的更改可能需要更新脚本。文章还提及了Star历史记录。

---

## 56. 备受喜爱的27年历史游戏网站清除论坛，转型为赌博敛财工具。

**原文标题**: Beloved 27-Year-Old Gaming Site Wipes Forums, Relaunches as Gambling Cash-Grab

**原文链接**: [https://kotaku.com/adventure-gamers-forums-gambling-ads-jack-allin-1851784764](https://kotaku.com/adventure-gamers-forums-gambling-ads-jack-allin-1851784764)

冒险游戏者，一个历史悠久（始于1998年）且备受喜爱的专门介绍点击式冒险游戏的网站，已被出售并转型为赌博联盟营销网站，这在游戏社区中引发了愤怒和失望。该网站最初推广和存档冒险游戏的宗旨已被赌场评论和老虎机广告所取代。

本文详细介绍了导致这一转变的事件。关键人物包括原所有者Marek Bronstring、前主编Jack Allin，以及从Bronstring手中买下该网站，后来又将其出售给当前匿名所有者的Ivo Teel。Teel和Allin在2022年因财务补偿问题产生分歧，导致Allin离开，并与其他前贡献者成立了Adventure Game Hotspot（AGH）。AGH现在被认为是原网站的精神继承者。

Teel以财务困难和流量下降为由，最终将Adventure Gamers出售给一家名为ClickOut Media的公司，并期望他们保持其现有形式。然而，新所有者彻底改造了该网站，删除了多年的论坛帖子，移除了作者署名，并用赌博相关内容填充了它。Allin和Teel都对该网站的现状表示沮丧。人们希望论坛内容能够被AGH和另一方挽救和存档。本文强调了冒险游戏爱好者失去了一个宝贵的资源，以及围绕该网站转型存在的伦理问题。

---

## 57. 最大的特斯拉超级充电站是离网的

**原文标题**: The Largest Tesla Supercharger Station Is Off-Grid

**原文链接**: [https://insideevs.com/news/764997/worlds-largest-tesla-supercharger-project-oasis/](https://insideevs.com/news/764997/worlds-largest-tesla-supercharger-project-oasis/)

特斯拉全球最大超级充电站“绿洲项目”于加州失落山开幕

---

## 58. 随身听之战

**原文标题**: The War on the Walkman

**原文链接**: [https://newsletter.pessimistsarchive.org/p/the-forgotten-war-on-the-walkman](https://newsletter.pessimistsarchive.org/p/the-forgotten-war-on-the-walkman)

被遗忘的随身听之战：本文探讨了1979年索尼随身听发布之初所受到的最初抵制。虽然现在它被怀旧地视为20世纪80年代的象征，但随身听最初引发了严重的担忧和批评。

评论家认为该设备是日益增长的个人主义和社会脱节的象征，有些人将其比作“感官抑制剂”或一种脱离社会联系的工具。对于行人、自行车手和司机使用耳机的安全性问题日益突出，导致许多州提议或颁布了关于驾驶或骑自行车时使用耳机的限制。

新泽西州伍德布里奇镇甚至禁止佩戴随身听耳机过马路，违者将处以监禁和罚款。退休人员奥斯卡·格罗斯故意违反了这项法律，以公民不服从的行为，成为第一个被传讯的人。尽管他愿意服刑以挑战该法律对个人自由的侵犯，但他只被处以罚款，罚款后来被中止。在发生一起涉及耳机的致命事故凸显了安全问题后，他的案件未被进一步追究。

文章最后指出，这种最初对随身听的抵制突显了怀旧情绪如何常常掩盖了新技术所面临的批评。它提醒人们，现在被认为是“好时光”的日子，曾经被认为是潜在的危险和孤立的未来。文章还简要提到了20世纪90年代围绕寻呼机发生的类似争议。

---

## 59. 加密货币101 – 密码学入门课程 (2017)

**原文标题**: Crypto 101 – Introductory course on cryptography (2017)

**原文链接**: [https://www.crypto101.io/](https://www.crypto101.io/)

密码学入门101是一门免费的入门级密码学课程，专为所有技能水平的程序员设计。它旨在通过涵盖以下基本组件，全面了解SSL/TLS等密码学系统：分组密码、流密码、哈希函数、消息认证码、公钥加密、密钥协商协议和签名算法。

本课程的一个关键方面是通过实践学习。鼓励学生利用他们的编程技能来利用常见的密码学漏洞，包括伪造管理员cookie、恢复密码和后门化随机数生成器等任务。

课程材料以各种无DRM格式提供，如PDF、EPUB和Mobi，使其可在不同的平台和设备上访问。

密码学入门101起源于2013年PyCon上的演讲，书籍版本在此基础上进行了扩展，侧重于破解密码学以了解其弱点。它由lvh创建。

---

## 60. 我不认为通用人工智能即将到来。

**原文标题**: I don't think AGI is right around the corner

**原文链接**: [https://www.dwarkesh.com/p/timelines-june-2025](https://www.dwarkesh.com/p/timelines-june-2025)

德瓦凯什·帕特尔在2025年6月的这篇博文中讨论了他为何认为通用人工智能（AGI）并非“近在咫尺”，尽管人工智能领域近期取得了进展。他的主要论点集中在大型语言模型（LLM）目前的局限性，尤其是它们缺乏持续学习的能力。虽然他承认LLM令人印象深刻的能力，但帕特尔强调，LLM难以像人类一样随着时间推移而进步，这阻碍了它们在现实场景中的实际应用。他将此与人类学习进行对比，人类学习涉及构建背景、反思失败以及进行渐进式改进。

帕特尔用教人吹萨克斯风的例子来说明仅通过提示“教”LLM的困难。他认为，虽然强化学习微调存在，但它不如人类学习那样具有适应性和有机性。他还对明年年底前出现可靠的计算机使用代理的预测表示怀疑，理由是存在诸如推出时间长和缺乏足够的预训练数据等挑战。

尽管他有所保留，但帕特尔承认了人工智能推理能力的快速进步以及未来突破的潜力。他预测到2028年，人工智能将能够为小型企业处理端到端的税务准备工作。更重要的是，他预测到2032年，人工智能将能够像人类一样有效地在工作中学习，这可能会导致“广泛部署的智能爆炸”，因为人工智能模型会在多个应用程序中积累和共享知识。他告诫说，早期版本的持续学习可能并不完善，我们将看到朝着这一进步的逐步创新。

---

## 61. 再无人格，我们只是贴着标签的商品。

**原文标题**: Nobody has a personality anymore: we are products with labels

**原文链接**: [https://www.freyaindia.co.uk/p/nobody-has-a-personality-anymore](https://www.freyaindia.co.uk/p/nobody-has-a-personality-anymore)

《再无人格：我们皆是标签化的商品》一文中，弗雷娅·印度认为，“治疗性话语”的普遍影响以及通过心理学和科学框架解释一切的驱动力正在侵蚀个性和真正的人类体验。作者认为，人们越来越多地被标签和诊断所定义，将正常的性格特征变成了需要解决的问题。这种趋势在Z世代中尤为突出，相当大比例的人认为他们的心理健康挑战是他们身份的重要组成部分。

印度批评了将日常行为和情感医学化的趋势，用临床诊断如多动症或自闭症取代了情感描述。她认为，这种诊断视角将个体简化为症状和童年事件，剥夺了人际关系的神秘感和浪漫。

作者感叹性格特征的丧失，慷慨变成了“讨好”，努力工作归因于创伤。她认为，由价值数十亿美元的心理健康产业驱动的持续自我分析和分类，正在使人们感到痛苦，并阻止他们充分体验生活。人们没有被鼓励向外参与，而是被教导向内看，并为一切寻找解释，将记忆变成证据，将人际关系变成依恋理论。

印度提倡抵制解释一切的冲动，拥抱不可知，并专注于我们的行为和对待他人的方式。她鼓励读者让自己“未解”，并通过成为一个人，而不是被医疗标签定义的产品，来重塑他们的人性。

---

## 62. 已修正的UTF-8 (2022)

**原文标题**: Corrected UTF-8 (2022)

**原文链接**: [https://www.owlfolio.org/development/corrected-utf-8/](https://www.owlfolio.org/development/corrected-utf-8/)

修正UTF-8旨在通过解决感知到的设计缺陷来改进现有的UTF-8编码。该提案涉及三个关键更改：

1. **消除过度长度编码：** 与标准UTF-8禁止过度长度编码但无法阻止其可能性不同，修正UTF-8修改了编码以使其成为不可能。它为由两个或多个字节序列编码的代码点添加了偏移量，从而确保每个可能的序列唯一地编码单个代码点。

2. **排除C1控制符和代理项：** 修正UTF-8跳过C1控制字符范围（U+0080-U+009F）和代理区（U+D800-U+DFFF）。这消除了与旧编码的兼容性问题，并消除了对代理对的需求（主要由UTF-16使用）。如有必要，这些范围可以映射到专用代码点。

3. **移除上限：** 修正UTF-8将代码点空间扩展到U+10FFFF之外，恢复到允许更大代码点的原始UTF-8设计。这解决了由于Unicode增长而导致的潜在的未来代码点耗尽问题。它扩展到U+8421109F，并提出了一个潜在的未来扩展，使用FE和FF前导字节来理论上实现无限的代码点空间。

该提案定义了一个魔数（EF B7 9D ED B2 AE 00 0A）来标识修正UTF-8编码的文件。它还不鼓励使用某些旧版控制字符，包括U+0000（魔数中除外）、U+000D、U+2028和U+2029，建议遵守Unix文本文件约定进行行终止。

---

## 63. 半人马：模拟人类认知的一次备受争议的飞跃

**原文标题**: Centaur: A controversial leap towards simulating human cognition

**原文链接**: [https://insidescientific.com/centaur-a-controversial-leap-towards-simulating-human-cognition/](https://insidescientific.com/centaur-a-controversial-leap-towards-simulating-human-cognition/)

研究人员开发出名为“半人马座”的AI模型，该模型基于Psych-101数据集（包含来自160个心理学实验的6万多名参与者的数据）训练，声称它模拟了人类认知。《自然》杂志发表的文章断言，“半人马座”建立在Meta的Llama之上，在预测人类行为方面超越了传统的认知模型，即使是在其训练数据之外的修改任务中也是如此。这为*计算机模拟*实验和新的行为理论开辟了可能性。

然而，关于模仿人类认知的说法存在争议。布莱克·理查兹和马塞尔·宾兹等批评者质疑“半人马座”是否真正反映了人类的认知过程。杰弗里·鲍尔斯指出，“半人马座”的超人能力（例如，回忆256位数字）是反对其泛化能力的证据。包括费德里科·阿道菲在内的其他人则强调，与人类认知的广度相比，Psych-101数据集的范围有限。

尽管存在这些批评，但包括凯瑟琳·斯托尔斯在内的一些人认为Psych-101数据集对于未来模型测试具有价值，并对“半人马座”在长期内产生科学益处的潜力保持谨慎乐观。该文章最初于2025年7月2日发表在《科学》杂志上。

---

## 64. 汉娜·开罗：17岁少女反驳40年前提出的数学猜想

**原文标题**: Hannah Cairo: 17-year-old teen refutes a math conjecture proposed 40 years ago

**原文链接**: [https://english.elpais.com/science-tech/2025-07-01/a-17-year-old-teen-refutes-a-mathematical-conjecture-proposed-40-years-ago.html](https://english.elpais.com/science-tech/2025-07-01/a-17-year-old-teen-refutes-a-mathematical-conjecture-proposed-40-years-ago.html)

十七岁的汉娜·开罗推翻了水端-竹内猜想。该猜想是20世纪80年代提出的一个数学难题，调和分析界为此研究了几十年。人们普遍认为该猜想是正确的，其验证将证实该领域中的其他重要结果。开罗最初来自巴哈马，还在高中时就参加了加州大学伯克利分校的课程。她的教授张瑞祥将一个简化的版本作为作业提出后，她便对该猜想着迷。

开罗的解决方案涉及构建一个反例，需要使用分形等工具。她的教授最初需要说服，但最终确认了她的发现是正确的。水端-竹内猜想属于调和分析领域，该领域应用广泛，从音频压缩到电信系统都有涉及。调和分析使用更简单的正弦分量构建函数，在傅里叶限制理论中，科学家们研究可以使用有限的波构造什么。

开罗在西班牙举行的第12届调和分析和偏微分方程国际大会上展示了她的工作，在那里她很高兴与他人分享她对数学的热情。开罗对数学的兴趣始于抽象代数和数论，疫情期间她在线参加了伯克利数学圈夏令营，后来成为了一名讲师。她将在马里兰大学开始攻读博士学位，继续与张教授合作。

---

## 65. Deno 2.4

**原文标题**: Deno 2.4

**原文链接**: [https://deno.com/blog/v2.4](https://deno.com/blog/v2.4)

Deno 2.4重大更新：回归`deno bundle`，增强依赖管理，提升兼容性。`deno bundle`由esbuild驱动，允许创建包含tree shaking和minification的单文件JavaScript包，支持服务端和浏览器平台以及npm/JSR依赖。新增`--unstable-raw-imports`标志允许将非JavaScript文件（如文本、字节、图像、JSON和Wasm）直接导入JavaScript图。

OpenTelemetry支持现已稳定，通过自动日志记录、指标和追踪收集简化了可观察性。`--preload`标志允许在主脚本执行前修改Deno环境，可用于平台自定义。`deno update`通过将npm和JSR依赖项更新到最新兼容版本来简化依赖项管理。`deno run`的脚本覆盖率收集通过`--coverage`标志得到增强。

新增环境变量`DENO_COMPAT=1`，通过启用可改善人体工程学的标志来简化以package.json优先的项目。权限更改包括用于`--allow-net`的子域通配符和CIDR范围，以及用于阻止特定主机的`--deny-import`标志。现在支持npm包中的条件导出，允许基于用户提供的条件进行不同的导出。最后，deno现在支持在`deno run`中使用裸说明符作为入口点。

---

## 66. 长笛声学：长笛工作原理入门

**原文标题**: Flute acoustics: an introduction to how a flute works

**原文链接**: [https://newt.phys.unsw.edu.au/jw/fluteacoustics.html#words](https://newt.phys.unsw.edu.au/jw/fluteacoustics.html#words)

长笛声学简介

本文介绍了长笛的声学原理，解释了它如何产生声音，而无需掌握高等数学或声学知识。核心概念是，长笛作为一个开放管道，利用演奏者的气流与乐器内的共振相结合来产生声音。

演奏者将气流吹过吹口孔，导致气流振动并与长笛内的空气柱相互作用。 这种相互作用会产生振荡气流，并通过乐器的固有共振频率进行放大。 长笛作为开放管道的设计意味着两端（吹口孔和开放端或音孔）的空气压力几乎是大气压，从而产生压力节点并允许在特定频率下产生驻波（共振）。 最低的共振频率决定了基音，而更高的频率（谐波）可以通过调整气流和嘴唇开口或使用泛音孔来实现。

打开音孔有效地缩短了管道，从而提高了音高。 泛音孔经过策略性放置，可以抑制较低的谐波以促进较高的谐波，从而有助于获得更高的八度音阶。 本文还涉及声阻抗，即声压与气流之比，它决定了空气进出长笛的难易程度，并影响所产生的声音。 最后，它暗示了更复杂的主题，如交叉指法和截止频率，这些主题将在网站的更详细部分中进行讨论。 本文强调了演奏者的技巧（气流、嘴唇位置）与乐器设计在产生所需音高和音调方面的相互作用。

---

## 67. 再来一次：Eshell

**原文标题**: Take Two: Eshell

**原文链接**: [http://yummymelon.com/devnull/take-two-eshell.html](http://yummymelon.com/devnull/take-two-eshell.html)

蔡崔的《再看Eshell：埃舍尔》反思了他在Emacs中对Eshell不断演变的看法。最初他印象不深，现在却认为它是他工作流程中不可或缺的一部分。文章认为Eshell不是传统shell的直接替代品，而是一个强大的Elisp REPL，可以与命令行实用程序交互。

崔解释说，他已经不再使用shell来执行文件管理和SCM等任务，而是更喜欢诸如Dired和Magit之类的Emacs模式。他强调Dired在复杂文件操作方面的优雅性优于shell脚本。虽然他承认Eshell的终端仿真能力有限，但他认为它适合许多基于curses的实用程序。

根据崔的说法，Eshell真正的优势在于它与Elisp的集成。他演示了如何在Eshell命令中使用Elisp来操作文件名并将Emacs缓冲区集成到工作流程中。他提供了示例，展示了如何将shell命令与Elisp混合使用。

他告诫不要在管道命令中使用Eshell处理大型文件，建议使用*|运算符以避免性能问题。他还强调，将Eshell视为Emacs的“提示符”界面会改变人们对shell工作流程的看法。

总之，崔建议将Eshell视为具有类似shell功能的强大Elisp提示符，而不是完整的shell替代品。他提倡学习Elisp以释放Eshell的全部潜力。

---

## 68. Can we test it? Yes, was can [video]

**原文标题**: Can we test it? Yes, was can [video]

**原文链接**: [https://www.youtube.com/watch?v=MqC3tudPH6w](https://www.youtube.com/watch?v=MqC3tudPH6w)

生成摘要时出错

---

## 69. AI is coming for agriculture, but farmers aren’t convinced

**原文标题**: AI is coming for agriculture, but farmers aren’t convinced

**原文链接**: [https://theconversation.com/shit-in-shit-out-ai-is-coming-for-agriculture-but-farmers-arent-convinced-259997](https://theconversation.com/shit-in-shit-out-ai-is-coming-for-agriculture-but-farmers-arent-convinced-259997)

生成摘要时出错

---

## 70. Overthinking GIS (2024)

**原文标题**: Overthinking GIS (2024)

**原文链接**: [https://scottsexton.co/post/overthinking_gis/](https://scottsexton.co/post/overthinking_gis/)

生成摘要时出错

---

## 71. Data on AI-related Show HN posts

**原文标题**: Data on AI-related Show HN posts

**原文链接**: [https://ryanfarley.co/ai-show-hn-data/](https://ryanfarley.co/ai-show-hn-data/)

生成摘要时出错

---

## 72. Overclocking LLM Reasoning: Monitoring and Controlling LLM Thinking Path Lengths

**原文标题**: Overclocking LLM Reasoning: Monitoring and Controlling LLM Thinking Path Lengths

**原文链接**: [https://royeisen.github.io/OverclockingLLMReasoning-paper/](https://royeisen.github.io/OverclockingLLMReasoning-paper/)

生成摘要时出错

---

## 73. Lessons from 863 episodes of This American Life

**原文标题**: Lessons from 863 episodes of This American Life

**原文链接**: [https://indarktrees.com/misc/tal/](https://indarktrees.com/misc/tal/)

生成摘要时出错

---

## 74. Local-first software (2019)

**原文标题**: Local-first software (2019)

**原文链接**: [https://www.inkandswitch.com/essay/local-first/](https://www.inkandswitch.com/essay/local-first/)

生成摘要时出错

---

## 75. Toys/Lag: Jerk Monitor

**原文标题**: Toys/Lag: Jerk Monitor

**原文链接**: [https://nothing.pcarrier.com/posts/lag/](https://nothing.pcarrier.com/posts/lag/)

生成摘要时出错

---

## 76. New quantum paradox clarifies where our views of reality go wrong (2018)

**原文标题**: New quantum paradox clarifies where our views of reality go wrong (2018)

**原文链接**: [https://www.quantamagazine.org/frauchiger-renner-paradox-clarifies-where-our-views-of-reality-go-wrong-20181203/](https://www.quantamagazine.org/frauchiger-renner-paradox-clarifies-where-our-views-of-reality-go-wrong-20181203/)

生成摘要时出错

---

## 77. LISPy things you can do in 64K bytes of core

**原文标题**: LISPy things you can do in 64K bytes of core

**原文链接**: [https://www.t3x.org/lisp64k/index.html](https://www.t3x.org/lisp64k/index.html)

生成摘要时出错

---

## 78. Collatz's Ant and Σ(n)

**原文标题**: Collatz's Ant and Σ(n)

**原文链接**: [https://gbragafibra.github.io/2025/07/06/collatz_ant5.html](https://gbragafibra.github.io/2025/07/06/collatz_ant5.html)

生成摘要时出错

---

## 79. 'Positive review only': Researchers hide AI prompts in papers

**原文标题**: 'Positive review only': Researchers hide AI prompts in papers

**原文链接**: [https://asia.nikkei.com/Business/Technology/Artificial-intelligence/Positive-review-only-Researchers-hide-AI-prompts-in-papers](https://asia.nikkei.com/Business/Technology/Artificial-intelligence/Positive-review-only-Researchers-hide-AI-prompts-in-papers)

生成摘要时出错

---

## 80. Game publishers respond to Stop Killing Games claim it curtails developer choice

**原文标题**: Game publishers respond to Stop Killing Games claim it curtails developer choice

**原文链接**: [https://www.pcgamer.com/gaming-industry/european-game-publisher-group-responds-to-stop-killing-games-claims-these-proposals-would-curtail-developer-choice/](https://www.pcgamer.com/gaming-industry/european-game-publisher-group-responds-to-stop-killing-games-claims-these-proposals-would-curtail-developer-choice/)

生成摘要时出错

---

## 81. Secret Cellular Phone Numbers

**原文标题**: Secret Cellular Phone Numbers

**原文链接**: [https://computer.rip/2025-07-06-secret-cellular-phone-numbers.html](https://computer.rip/2025-07-06-secret-cellular-phone-numbers.html)

生成摘要时出错

---

## 82. The Broken Microsoft Pact: Layoffs and Performance Management

**原文标题**: The Broken Microsoft Pact: Layoffs and Performance Management

**原文链接**: [https://danielsada.tech/blog/microsoft-pact/](https://danielsada.tech/blog/microsoft-pact/)

生成摘要时出错

---

## 83. Development of a transputer ISA board

**原文标题**: Development of a transputer ISA board

**原文链接**: [https://nanochess.org/transputer_board.html](https://nanochess.org/transputer_board.html)

生成摘要时出错

---

## 84. If it cites em dashes as proof, it came from a tool

**原文标题**: If it cites em dashes as proof, it came from a tool

**原文链接**: [https://www.scottsmitelli.com/articles/em-dash-tool/](https://www.scottsmitelli.com/articles/em-dash-tool/)

生成摘要时出错

---

## 85. Grinding down open source maintainers with AI

**原文标题**: Grinding down open source maintainers with AI

**原文链接**: [https://shkspr.mobi/blog/2025/07/grinding-down-open-source-maintainers-with-ai/](https://shkspr.mobi/blog/2025/07/grinding-down-open-source-maintainers-with-ai/)

生成摘要时出错

---

## 86. How to get started with Old English poetry

**原文标题**: How to get started with Old English poetry

**原文链接**: [https://www.deadlanguagesociety.com/p/old-english-poetry](https://www.deadlanguagesociety.com/p/old-english-poetry)

生成摘要时出错

---

## 87. Eastern Baltic cod grow much smaller than they did due to overfishing

**原文标题**: Eastern Baltic cod grow much smaller than they did due to overfishing

**原文链接**: [https://www.smithsonianmag.com/smart-news/these-cod-have-been-shrinking-dramatically-for-decades-now-scientists-say-theyve-solved-the-mystery-180986920/](https://www.smithsonianmag.com/smart-news/these-cod-have-been-shrinking-dramatically-for-decades-now-scientists-say-theyve-solved-the-mystery-180986920/)

生成摘要时出错

---

## 88. Valve conquered PC gaming – what comes next?

**原文标题**: Valve conquered PC gaming – what comes next?

**原文链接**: [https://www.ft.com/content/f4a13716-838a-43da-853b-7c31ac17192c](https://www.ft.com/content/f4a13716-838a-43da-853b-7c31ac17192c)

生成摘要时出错

---

## 89. Wind Knitting Factory

**原文标题**: Wind Knitting Factory

**原文链接**: [https://www.merelkarhof.nl/work/wind-knitting-factory](https://www.merelkarhof.nl/work/wind-knitting-factory)

生成摘要时出错

---

## 90. Serving 200M requests per day with a CGI-bin

**原文标题**: Serving 200M requests per day with a CGI-bin

**原文链接**: [https://simonwillison.net/2025/Jul/5/cgi-bin-performance/](https://simonwillison.net/2025/Jul/5/cgi-bin-performance/)

生成摘要时出错

---

## 91. Pangu's Sorrow: The Sorrow and Darkness of Huawei's Noah Pangu LLM R&D Process

**原文标题**: Pangu's Sorrow: The Sorrow and Darkness of Huawei's Noah Pangu LLM R&D Process

**原文链接**: [https://github.com/moonlightelite/True-Story-of-Pangu/blob/main/README.md](https://github.com/moonlightelite/True-Story-of-Pangu/blob/main/README.md)

生成摘要时出错

---

## 92. The force-feeding of AI features on an unwilling public

**原文标题**: The force-feeding of AI features on an unwilling public

**原文链接**: [https://www.honest-broker.com/p/the-force-feeding-of-ai-on-an-unwilling](https://www.honest-broker.com/p/the-force-feeding-of-ai-on-an-unwilling)

生成摘要时出错

---

## 93. A New Postgres Block Storage Layout for Full Text Search

**原文标题**: A New Postgres Block Storage Layout for Full Text Search

**原文链接**: [https://www.paradedb.com/blog/block_storage_part_one](https://www.paradedb.com/blog/block_storage_part_one)

生成摘要时出错

---

## 94. What a Hacker Stole from Me

**原文标题**: What a Hacker Stole from Me

**原文链接**: [https://mynoise.net/blog.php](https://mynoise.net/blog.php)

生成摘要时出错

---

## 95. Paper Shaders: Zero-dependency canvas shaders

**原文标题**: Paper Shaders: Zero-dependency canvas shaders

**原文链接**: [https://github.com/paper-design/shaders](https://github.com/paper-design/shaders)

生成摘要时出错

---

## 96. New study offers clues about what makes someone cool

**原文标题**: New study offers clues about what makes someone cool

**原文链接**: [https://www.nytimes.com/2025/06/30/well/mind/cool-people-traits-study.html](https://www.nytimes.com/2025/06/30/well/mind/cool-people-traits-study.html)

生成摘要时出错

---

## 97. Hidden interface controls that affect usability

**原文标题**: Hidden interface controls that affect usability

**原文链接**: [https://interactions.acm.org/archive/view/july-august-2025/stop-hiding-my-controls-hidden-interface-controls-are-affecting-usability](https://interactions.acm.org/archive/view/july-august-2025/stop-hiding-my-controls-hidden-interface-controls-are-affecting-usability)

生成摘要时出错

---

## 98. Meet Bionode

**原文标题**: Meet Bionode

**原文链接**: [https://microship.com/meet-bionode/](https://microship.com/meet-bionode/)

生成摘要时出错

---

## 99. Techno-feudalism and the rise of AGI: A future without economic rights?

**原文标题**: Techno-feudalism and the rise of AGI: A future without economic rights?

**原文链接**: [https://arxiv.org/abs/2503.14283](https://arxiv.org/abs/2503.14283)

生成摘要时出错

---

## 100. Building a Mac app with Claude code

**原文标题**: Building a Mac app with Claude code

**原文链接**: [https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code](https://www.indragie.com/blog/i-shipped-a-macos-app-built-entirely-by-claude-code)

生成摘要时出错

---

