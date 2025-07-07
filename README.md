# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-07.md)

*最后自动更新时间: 2025-07-07 17:49:21*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 2 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 3 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 4 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 5 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 6 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 7 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 8 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 9 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 10 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 11 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 12 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 13 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 14 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 15 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 16 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 17 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 18 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 19 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 20 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 21 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 22 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 23 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 24 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 25 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 26 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 27 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 28 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 29 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 30 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 31 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 32 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 33 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 34 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 35 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 36 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 37 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 38 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 39 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 40 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 41 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 42 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 43 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 44 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 45 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 46 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 47 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 48 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 49 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 50 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 51 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 52 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 53 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 54 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 55 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 56 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 57 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 58 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 59 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 60 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 61 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 62 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 63 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 64 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 65 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 66 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 67 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 68 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 69 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 70 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 71 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 72 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 73 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 74 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 75 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 76 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 77 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 78 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 79 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 80 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 81 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 82 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 83 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 84 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 85 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 86 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 87 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 88 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 89 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 90 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 91 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 92 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 93 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 94 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 95 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 96 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 97 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 98 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 99 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 100 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 101 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 102 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 103 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 104 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 105 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 106 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 107 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 108 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 109 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 110 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
