# Hacker News 热门文章摘要 (2025-04-15)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 如何赢得与幼儿的争论

**原文标题**: How to Win an Argument with a Toddler

**原文链接**: [https://seths.blog/2025/04/how-to-win-an-argument-with-a-toddler/](https://seths.blog/2025/04/how-to-win-an-argument-with-a-toddler/)

与幼儿或行为如幼儿者争论，不可能“获胜”，因为他们的动机与真正的智识交流不同。幼儿（以及行为类似者）对发掘洞察力或达成结论不感兴趣；相反，他们寻求联系、娱乐、地位或施展权力的机会。

本文将此与真正的争论进行对比，真正的争论涉及思想的交流，从而可能导致理解的转变。改变主意的意愿被认为是富有成效的争论的关键指标，表明智力增长源于对新观点的开放。

“幼儿”策略包括保留一场发脾气，要么在他们“获胜”时避免，要么在他们“失败”时通过指责对方不愿倾听来辩解。

作者建议通过询问过去因讨论而改变坚定信念的例子，以及询问哪些信息可能导致视角转变来发起真正的讨论。最终，本文建议避免争论那些对个人身份至关重要的信念。核心信息是区分真正的智识交流和反对的表演，尤其是在与那些不愿意考虑替代观点的人打交道时。

---

## 2. 本·乔丹的人工智能毒丸与对抗噪声的怪异世界

**原文标题**: Benn Jordan's AI poison pill and the weird world of adversarial noise

**原文链接**: [https://cdm.link/benn-jordan-ai-poison-pill/](https://cdm.link/benn-jordan-ai-poison-pill/)

这篇CDM Create Digital Music文章讨论了Benn Jordan提出的“AI毒丸”——一种将对抗性噪声注入音乐以防止其被用于训练生成式AI模型的方法。该技术旨在通过导致模型误解或错误处理被污染的音频来扰乱AI训练。

文章强调了这种方法的潜在好处，包括它能够通过“模拟漏洞”运作以及通过不同方法进行调整，使AI服务难以反制。然而，目前的实现需要大量的计算能力，使得大规模使用不切实际。

文章还探讨了对抗性噪声的更广阔世界，讨论了其在保护音乐之外的潜在用途，例如入侵AI和监控系统。它提到了对“和谐隐身”和AI检测算法的研究。

文章强调了AI防御方法的快速发展，并引用了洛斯阿拉莫斯国家实验室和IBM Watson的例子。它还指出了定向压力波攻击的双刃剑性质，该攻击可以用来对付机器，但也与声波武器和“哈瓦那综合症”有关。

最终，作者主张开发和使用这种技术来保护艺术家的作品，设想未来发行商可以授权这些工具，为制作人提供安心。作者对Suno.ai创始人的观点表示沮丧，突出了开发AI音乐工具的人与艺术过程的内在乐趣之间可能存在的脱节。

---

## 3. 克洛格

**原文标题**: Clolog

**原文链接**: [https://github.com/bobschrag/clolog](https://github.com/bobschrag/clolog)

Clolog是一个嵌入在Clojure中的逻辑编程系统（类似于Prolog），它提供了一种Lispy的、自同构的语法。它强调表达能力和执行透明性，而非原始速度，使其适用于快速原型设计和外循环推理。

主要特性包括：

*   **Clojure集成：** 与Clojure无缝集成，允许与Clojure代码相互调用。
*   **复杂项：** 支持Clojure序列和向量中的逻辑变量。
*   **Clojure调用谓词：** 包括像`truthy?`、`evals-from?`和`do`这样的谓词，用于与Clojure交互。
*   **失败即否定：** 使用`not`实现否定。
*   **项匹配：** 提供内置谓词`same`和`different`用于项比较，以及`var`和`ground`用于项检查。
*   **逻辑运算符：** 支持可嵌套的运算符，如`and`、`or`、`not`和`if`。
*   **Cut运算符：** 包括`first`运算符，用于控制回溯。
*   **谓词转换：** 允许用户自定义转换，用于自定义逻辑。
*   **灵活的项类型：** 将符号、字符串、数字和复杂项视为逻辑项。
*   **变参谓词和项：** 支持具有可变元数的谓词和项。
*   **匿名变量：** 允许使用以`?`和`?_`为前缀的符号作为匿名变量。
*   **重复抑制：** 提供可选的重复和被包含答案抑制。

Clolog的语法定义了断言语句、谓词（内置的、转换的和基于断言的）以及项（透明的和不透明的）。搜索通常采用深度优先、从左到右的方式进行，并使用合一进行项匹配。API包括初始化、上下文设置、断言创建（通过宏和函数）以及断言检索。

---

## 4. 破解Postgres网络协议

**原文标题**: Hacking the Postgres Wire Protocol

**原文链接**: [https://pgdog.dev/blog/hacking-postgres-wire-protocol](https://pgdog.dev/blog/hacking-postgres-wire-protocol)

PgDog：通过操纵Postgres协议实现分片的网络代理

本文介绍了PgDog，一种网络代理，它通过操纵Postgres wire协议来实现Postgres的分片。PgDog拦截并分析SQL查询，根据分片键将它们路由到适当的数据库分片。

本文详细介绍了PgDog如何处理简单和扩展的Postgres协议。对于简单协议，它解析SQL查询以识别分片键并确定查询是读取还是写入数据。对于扩展协议（使用预处理语句），PgDog在“Parse”消息之后缓存解析后的AST，然后使用“Bind”消息来提取分片键值。

PgDog利用基于Rust的SQL解析器 (pg_query)，该解析器使用Postgres的C源代码，确保对SQL的全面理解。它还使用Postgres的哈希函数进行一致的分片，避免自定义实现。

本文还讨论了PgDog如何管理跨分片查询，处理诸如RowDescription、DataRow、CommandComplete和ReadyForQuery之类的响应消息，从而确保数据一致性和准确的行数。它还解释了如何操作客户端消息以进行分布式COPY操作，从而实现跨分片的并行数据摄取。

最后，本文强调了通过分布式COPY实现线性可扩展的摄取速度的潜力，并提到了未来扩展PgDog功能到逻辑复制流的计划。它还强调了PgDog的网络层方法使其可以与各种Postgres克隆和托管云服务一起使用。

---

## 5. 使用Veo 2在Gemini和Whisk中生成视频

**原文标题**: Generate videos in Gemini and Whisk with Veo 2

**原文链接**: [https://blog.google/products/gemini/video-generation/](https://blog.google/products/gemini/video-generation/)

谷歌将 Veo 2 视频生成模型整合到 Gemini Advanced 和 Whisk AI 实验项目中。Gemini Advanced 订阅者现在可以直接在 Gemini 界面内通过文本提示生成 8 秒、高分辨率 (720p) 的视频。文章强调了 Veo 2 创建逼真、细节丰富、人物动作流畅、场景栩栩如生的视频的能力。用户可以通过提供详细的文本描述来创建各种视频，从而进行不同风格和创意的探索。这些视频可以轻松地在 TikTok 和 YouTube Shorts 等平台上分享。

此外，Google One AI Premium 订阅者现在可以使用 Whisk Animate（现有 Whisk 图像生成工具的扩展），通过 Veo 2 将图像转换为 8 秒的动画视频。这允许用户对现有图像进行动画处理，或者创建新图像后再进行动画处理。

文章还强调了谷歌实施的安全措施，包括红队演练、内容评估以及使用 SynthID（嵌入到人工智能生成视频每一帧中的数字水印）来表明其人工智能来源。视频生成功能正在全球范围内面向 Gemini Advanced 和 Whisk 用户的 Web 和移动端推出，并支持 Gemini 支持的所有语言。

---

## 6. Teuken-7B-Base和Teuken-7B-Instruct：迈向欧洲大型语言模型

**原文标题**: Teuken-7B-Base and Teuken-7B-Instruct: Towards European LLMs

**原文链接**: [https://arxiv.org/abs/2410.03730](https://arxiv.org/abs/2410.03730)

本文（arXiv:2410.03730v2）介绍了Teuken-7B-Base和Teuken-7B-Instruct，这两个新的多语言大型语言模型（LLM），旨在更好地支持欧洲的语言多样性。这些模型在一个约60%为非英语数据的语料库上进行训练，从而解决了现有LLM中普遍存在的对英语和其他高资源语言的偏见。使用了定制的多语言分词器。

以Mehdi Ali为首的作者详细介绍了模型背后的开发原则，包括数据组成、分词器优化和训练方法。目标是创建在欧盟所有24种官方语言中表现良好的LLM。

这些模型在多语言基准测试中表现出竞争优势。欧洲语言版本的现有基准测试（如ARC、HellaSwag、MMLU和TruthfulQA）的结果证明了这一点。本文提供了PDF和HTML格式的论文链接，以及探索相关代码、数据、媒体和分析的选项。

---

## 7. Cohere 发布 Embed 4

**原文标题**: Cohere Launches Embed 4

**原文链接**: [https://cohere.com/blog/embed-4](https://cohere.com/blog/embed-4)

Cohere 发布 Embed 4，用于企业级多模态搜索。

---

## 8. 决定署名顺序的有趣方法

**原文标题**: Fun ways of deciding authorship order

**原文链接**: [https://dynamicecology.wordpress.com/2016/09/21/fun-ways-of-deciding-authorship-order/](https://dynamicecology.wordpress.com/2016/09/21/fun-ways-of-deciding-authorship-order/)

这篇博文幽默地探讨了生态学和进化生物学论文中决定作者署名顺序的非常规方法，超越了按字母顺序等标准做法。 起源于一条关于用篮球比赛决定署名的推文，并扩展成从Twitter和其他来源收集的创意解决方案集锦。

文章重点介绍了如下例子：

*   **体育比赛：**槌球比赛和掰手腕。
*   **随机方法：**抛硬币和使用代码进行随机抽样。
*   **实际考虑：**决定顺序的后勤因素。
*   **博弈论：**运用博弈论原理。
*   **石头剪刀布：**一种经典的概率游戏。
*   **布朗尼烘焙大赛：**一项烹饪比赛。
*   **狗狗辅助随机排序：**使用狗狗通过吃零食来随机排序。
*   **身高：**按身高排列作者顺序。

作者推崇布朗尼烘焙大赛为最有趣的方法，并戏谑地自荐担任此类比赛的评委。 该博文还涉及通过脚注解决作者贡献问题，并提及有趣的（合）著者，包括使用化名甚至动物。 作者鼓励读者分享他们所知道的其他非常规方法，并建议未来撰写关于论文最佳开篇语和有趣的致谢部分的博文。 该博文会持续更新在网上发现的新例子。 作者还讲述了一个因作者署名顺序争议而导致论文撤稿的警示故事。

---

## 9. Show HN: Resonate – 实时高时间分辨率频谱分析

**原文标题**: Show HN: Resonate – real-time high temporal resolution spectral analysis

**原文链接**: [https://alexandrefrancois.org/Resonate/](https://alexandrefrancois.org/Resonate/)

Resonate：一种用于音频信号实时频谱分析的新型低延迟算法。与基于FFT的方法不同，Resonate使用一系列调谐到特定频率的谐振器，以高效估计频谱内容。该算法的核心是对每个谐振器频率周围的信号应用指数加权移动平均（EWMA），赋予最近输入值更高的权重。这种迭代方法允许逐样本更新，从而最大限度地减少内存占用和计算成本。

Resonate的主要优势包括其低延迟、线性内存和计算复杂度（相对于谐振器数量），以及并行计算的能力。该算法特别适用于响应速度至关重要的实时应用。Resonate可以直接计算具有高时间分辨率和感知相关的频率尺度的频谱图。

本文展示了Resonate生成的频谱图与恒Q变换（CQT）频谱图的比较示例，证明了其在音乐和语音样本上的有效性。该算法将在即将举行的ICMS会议出版物中详细介绍。开源资源，包括`noFFT` Python模块、`Oscillators` Swift软件包、`Oscillators`应用程序和一个Resonate YouTube播放列表，提供了实现和演示。

---

## 10. 育碧内部用于模拟色盲的工具Chroma开源了

**原文标题**: Chroma, Ubisoft's internal tool used to simulate color-blindness, open sourced

**原文链接**: [https://github.com/ubisoft/Chroma](https://github.com/ubisoft/Chroma)

育碧开源Chroma，一款用于模拟色盲的内部工具，旨在提升游戏的可访问性。Chroma模拟三种主要色盲类型：红色盲、绿色盲和蓝色盲，使开发者能够了解游戏在患有这些情况的玩家眼中的呈现效果。

Chroma的关键特性包括：在游戏之上运行并可最大化的实时颜色模拟、与所有游戏引擎的兼容性、高达60FPS的高性能、准确的模拟结果、实时游戏画面捕捉、便于错误记录的屏幕截图、以及可配置的用户界面。Chroma被认为是唯一一款能够捕捉实时游戏画面并模拟色盲的解决方案。

该工具旨在帮助育碧的无障碍团队进行复杂的测试，提供一个不依赖特定游戏引擎的单显示器解决方案。CMake过程中与过时的CPPWinRT库相关的已知问题可以通过安装Microsoft.Windows.CppWinRT NuGet包或使用Visual Studio 2022来解决。用户指南提供了更多细节。

---

## 11. MeshCore：一种用于分组无线电的新型轻量级混合路由网格协议

**原文标题**: MeshCore, a new lightweight, hybrid routing mesh protocol for packet radios

**原文链接**: [https://github.com/ripplebiz/MeshCore](https://github.com/ripplebiz/MeshCore)

MeshCore 是一个轻量级的 C++ 库，专为使用 LoRa 和其他数据包无线电创建弹性、去中心化、多跳数据包路由网络而设计，非常适合嵌入式项目。它允许设备通过中间节点中继消息来进行远距离通信，无需依赖互联网或中央服务器。

主要特性包括多跳数据包路由、LoRa 无线电支持（Heltec、RAK Wireless 等）、低功耗以及通过预构建的示例应用程序轻松部署。 MeshCore 平衡了简单性和可扩展性，使其适用于定制嵌入式解决方案。

MeshCore 可用于离网通信、应急响应、户外活动、战术应用和物联网传感器网络。

入门步骤包括在 Visual Studio Code 中安装 PlatformIO，下载 MeshCore 仓库，选择一个示例应用程序（聊天、中继器等），并使用串口监视器进行通信。 示例应用程序包括 Terminal Chat、Simple Repeater、Companion Radio 和 Room Server。

该库在 MIT 许可证下开源。 欢迎贡献，对于有影响的更改，鼓励进行讨论。 可通过 GitHub Issues、外部指南和 Discord 服务器获得支持。

RAK Wireless 用户需要修补他们的 PlatformIO 包，并将固件转换为 .uf2 文件以进行刷写。

---

## 12. 线上传输 JSX

**原文标题**: JSX over the Wire

**原文链接**: [https://overreacted.io/jsx-over-the-wire/](https://overreacted.io/jsx-over-the-wire/)

本文探讨了一种替代传统REST API的方案，提倡API返回专为UI组件（ViewModels）定制的数据，而非通用的Resources。作者认为，REST API通常难以有效地提供不同UI屏幕所需的精确数据，导致过度获取、多次API调用以及难以随着UI变化演进API。

核心思想是将API的焦点从服务通用数据Resources转移到服务特定屏幕定制的数据。作者建议使用诸如`/screens/post-details/123`这样的端点，而非`/api/post/123`，前者将返回`PostDetails`屏幕所需的所有数据。这使得在适应UI变化时具有更大的灵活性，而不会影响应用程序的其他部分。API实际上变成了UI的“父组件”，提供其所需的精确props。

本文对比了模型（原始数据）和ViewModel（为UI准备的数据），并认为REST API常常模糊了两者之间的界限，导致效率低下和可维护性问题。通过专门为ViewModels创建API，可以解决数据存储方式与显示方式之间的矛盾，从而更容易随着UI设计变化来演进API。

---

## 13. 等等。每年有多少超新星爆发？

**原文标题**: Wait. HOW MANY supernova explode every year?

**原文链接**: [https://badastronomy.beehiiv.com/p/ban-447-wait-how-many-supernova-explode](https://badastronomy.beehiiv.com/p/ban-447-wait-how-many-supernova-explode)

这期“糟糕天文学”时事通讯深入探讨了每年观测到的数量惊人的超新星，起因是作者对SN2021 afdx的命名感到惊讶，这是一颗于2021年在车轮星系中发现的超新星。

文章解释了超新星的命名规则，即使用发现年份加上字母表中的字母。文章还解释了望远镜和摄影术发明后，超新星的数量急剧增加，因此开发命名系统变得十分重要。

作者随后进行计算，估计SN2021 afdx是当年探测到的第21760颗超新星。一个超新星目录证实了这一点，该目录显示2021年探测到21081颗超新星。作者将其与SN1987A的发现进行对比，SN1987A是1987年2月23日前发现的第一颗超新星。

文章强调了由于望远镜技术和自动化巡天调查的进步，超新星探测呈指数级增长。作者估计在可观测宇宙中，每秒大约发生30颗超新星。文章最后强调了我们在超新星观测方面取得了多么大的进步，但也说明了我们还有很长的路要走。

---

## 14. 日本文字排印要点：日文与拉丁文字之间的日文排印

**原文标题**: Japanese Typography Essentials: Japanese Type Between Japanese and Latin

**原文链接**: [https://www.researchgate.net/publication/383515797_JAPANESE_TYPOGRAPHY_ESSENTIALS_JAPANESE_TYPE_BETWEEN_JAPANESE_LATIN_CHARACTER](https://www.researchgate.net/publication/383515797_JAPANESE_TYPOGRAPHY_ESSENTIALS_JAPANESE_TYPE_BETWEEN_JAPANESE_LATIN_CHARACTER)

无法访问文章链接。

---

## 15. 月球信号：为月球任务打造4G网络

**原文标题**: Getting a Signal on the Moon: 4G network for lunar missions

**原文链接**: [https://spectrum.ieee.org/nokia-4g-cellular-network-moon](https://spectrum.ieee.org/nokia-4g-cellular-network-moon)

诺基亚在月球上开发和部署4G蜂窝网络——月球表面通信系统

---

## 16. 怪异 - 上网新途径

**原文标题**: WEIRD – a way to be on the web

**原文链接**: [https://a.weird.one](https://a.weird.one)

“WEIRD——一种在线方式”这个标题暗示着一篇文章探索一种可能非传统的网络存在或在线互动方式。然而，仅凭标题和标语“Weird a way to be on the web!”作为内容，无法确定这种方法的具体细节。

现有内容过于简短，无法提供全面总结。只能推断出：

* **WEIRD**是一个与在线相关的概念、平台、工具或方法。
* 它提出的方法可能不寻常或偏离常规（“weird”）。
* 该文章大概阐述了这种“weird”的上网方式*如何*以及*为什么*有益或值得关注。

在缺乏更多背景信息的情况下，无法更深入地理解“WEIRD”及其功能。完整的摘要需要全文，以确定与这种特殊的网络互动方式相关的精确方法、目标、目标受众和优势。

---

## 17. Nix 中的 RNG 与 Cosine

**原文标题**: RNG and Cosine in Nix

**原文链接**: [https://unnamed.website/posts/rng-cosine-nix/](https://unnamed.website/posts/rng-cosine-nix/)

在Nix语言中实现随机数生成和余弦函数的幽默探索：

**随机数生成：** 由于Nix的纯函数特性，标准的随机数生成方法存在问题。本文详细描述了获取真正随机数的艰难过程，强调了缓存和访问`/dev/random`等系统文件的问题。最终的，尽管令人痛苦的解决方案，涉及重复创建Nix派生，直到获得非缓存结果，丢弃字符串上下文以确保获得新的随机值，尽管此解决方案在纯评估模式下不起作用。

**余弦：** 本文随后探讨了使用无限列表实现余弦函数，灵感来自作者之前的作品。它演示了如何在Nix中创建无限链表，然后移植代码以通过级数展开计算余弦。该过程遇到了几个Nix特有的怪癖，包括lambda函数语法和负浮点数的解释。

在整篇文章中，作者强调了由于Nix的纯函数特性和特定的语法规则，在Nix中实现看似简单的任务的困难，导致产生令人痛苦但功能正常的解决方案。文章最后提供了一些酷炫的Nix资源链接。

---

## 18. eBPF的隔离执行环境

**原文标题**: Isolated Execution Environment for eBPF

**原文链接**: [https://ebpf.foundation/research-update-isolated-execution-environment-for-ebpf/](https://ebpf.foundation/research-update-isolated-execution-environment-for-ebpf/)

本文讨论了一个研究项目，该项目旨在通过在内核中隔离 BPF 程序来增强 eBPF 的安全性，而不是仅仅依赖于复杂的 eBPF 验证器。目前的验证器虽然对内核安全至关重要，但存在漏洞和复杂性，导致潜在的安全风险和对程序功能的限制。

本文分解了验证器的工作流程，重点介绍了执行大部分安全检查的“全路径分析”。它详细介绍了用于理解验证器安全属性的方法，并概述了其旨在执行的 20 个关键属性。这些属性涵盖了内存安全、信息泄漏预防和拒绝服务预防等领域。设计层面的相应安全目标是访问控制、信息隐藏和功能稳定性。

本文随后重点介绍了全路径分析的困境：为了防止状态爆炸而施加限制的“能力困境”，从而限制了程序的复杂性，以及由于不断增加的复杂性和代码量导致错误和漏洞的“正确性困境”。文章通过代码示例展示了对程序复杂性的限制以及旨在缓解这些限制的功能（例如 `bpf_loop()`）的安全问题。作者认为，验证器未经证实的完整性和健全性使得非特权 eBPF 程序使用起来过于不安全。

作者最后建议转变范式，转向隔离 BPF 程序，类似于用户模式进程，将验证与隔离机制相结合，以提高安全性和可扩展性。

---

## 19. 来自绿色撒哈拉的7000年前的骨骼揭示了一个神秘的人类谱系

**原文标题**: 7k-Year-Old Skeletons from the Green Sahara Reveal a Mysterious Human Lineage

**原文链接**: [https://www.smithsonianmag.com/smart-news/7000-year-old-skeletons-from-the-green-sahara-reveal-a-previously-unknown-human-lineage-180986403/](https://www.smithsonianmag.com/smart-news/7000-year-old-skeletons-from-the-green-sahara-reveal-a-previously-unknown-human-lineage-180986403/)

考古学家分析了来自利比亚境内现今“绿色撒哈拉”的7000年前骨骼的DNA，发现了一个此前未知且基因上独特的原始人类群体。这些骨骼发现于名为Takarkori的岩石庇护所，属于畜牧者，其中包括两名自然木乃伊化的女性。令人惊讶的是，DNA分析显示，他们受撒哈拉以南或近东/欧洲人口的基因影响极小，表明他们经历了很长的基因隔离期。

这一发现挑战了长期以来“绿色撒哈拉”曾是北非和撒哈拉以南非洲之间主要迁徙走廊的理论。相反，该研究表明，畜牧业的传播是通过文化交流而非大规模人口迁徙实现的。这些人可能通过狩猎、捕鱼和放牧山羊和绵羊来生存。

研究人员最初只能分析线粒体DNA，但最终对完整基因组进行了测序。这表明该群体可能在大约5万年前从撒哈拉以南非洲人的祖先中分离出来，然后在数万年内保持孤立。科学家强调，需要更大样本量的进一步研究，才能充分了解撒哈拉地区人类群体复杂的历史。然而，这项研究对揭示非洲的人口历史以及发现现代基因组中几乎无法检测到的谱系做出了重大贡献。

---

## 20. 破解智能家居设备 (2024)

**原文标题**: Hacking a Smart Home Device (2024)

**原文链接**: [https://jmswrnr.com/blog/hacking-a-smart-home-device](https://jmswrnr.com/blog/hacking-a-smart-home-device)

本文详细介绍了一个逆向工程项目，该项目旨在破解基于ESP32的智能家居空气净化器，并将其集成到Home Assistant中，从而绕过其对基于云的移动应用程序的依赖。作者首先概述了计划：拦截并模拟设备的网络流量。

最初的移动应用程序分析显示该应用程序使用安全的WebSocket连接，但进一步的探索转向使用Pi-hole和Wireshark进行网络检查，以分析设备和云服务器之间发送的UDP数据包。在这些数据包中遇到加密数据后，作者拆解了物理设备以调查ESP32微控制器。

使用Flipper Zero建立串行连接，使作者能够访问日志数据并识别关键信息，例如4MB闪存芯片、应用程序分区（工厂和OTA）、FAT文件系统以及键值存储分区（NVS）。然后，ESP32被引导至下载引导模式，并转储整个闪存。

使用`esp32knife`分析闪存转储，揭示了分区表结构和其他重要细节。作者计划进一步分析从闪存转储中提取的文件系统和应用程序逻辑，以了解数据包结构，并最终在不依赖云的情况下在本地控制空气净化器。免责声明强调了篡改设备的教育目的和潜在风险。

---

## 21. 光之旋轮

**原文标题**: Rotatum of Light

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.adr9092](https://www.science.org/doi/10.1126/sciadv.adr9092)

无法访问文章链接。

---

## 22. JSLinux

**原文标题**: JSLinux

**原文链接**: [https://www.bellard.org/jslinux/](https://www.bellard.org/jslinux/)

JSLinux是一个基于网页的模拟器，允许用户直接在网页浏览器中运行各种操作系统。它提供了基于x86和RISC-V架构的多种模拟系统选择。

可用的x86选项包括Alpine Linux（控制台和X Window版本）、Windows 2000和FreeDOS。 RISC-V选项包括Buildroot Linux（控制台和X Window）和Fedora 33 Linux（控制台和X Window）。 一些X Window系统使用鼠标右键来显示菜单。

该页面提供了启动每个模拟环境的链接，并指出某些系统，尤其是Fedora 33发行版，可能需要较长的启动时间。

这项服务由Fabrice Bellard开发，并包含新闻、虚拟机列表、常见问题解答和技术说明的链接。 该服务于2011年至2021年间开发。

---

## 23. API中的GPT-4.1

**原文标题**: GPT-4.1 in the API

**原文链接**: [https://openai.com/index/gpt-4-1/](https://openai.com/index/gpt-4-1/)

基于对OpenAI模型现有知识及相关公告内容的理解，这是对OpenAI文章“API中的GPT-4.1”的摘要。由于无法直接访问提供的URL，这是一个基于推测的总结。

该文章可能宣布通过API提供更高级版本的GPT-4，可能称为GPT-4.1。这代表了对原始GPT-4模型的迭代改进。

公告的关键方面可能包括：

*   **增强的性能：** 新模型可能在推理、理解上下文、生成更高质量的文本、编码和解决问题等领域拥有改进的能力。这可能涉及更高的准确性、减少的偏见和更连贯的输出。

*   **扩大的上下文窗口：** 一个关键的改进可能是增加的上下文窗口，允许模型处理和记住来自对话中先前轮次或来自其分析的文档的更多信息。这会带来更多上下文相关且准确的响应。

*   **成本和可用性：** 该公告可能详细说明通过API访问GPT-4.1的定价结构。它还可能描述与新模型相关的任何等待名单、访问层级或使用限制。可能存在基于使用量、每分钟令牌数以及对特定功能的访问权限的不同层级。

*   **API更新：** 该文章可能概述与GPT-4.1相关的OpenAI API的具体更改，包括使用新模型所需的新参数、端点或数据格式。

*   **使用案例：** 该公告可能突出显示GPT-4.1擅长的各种应用，例如复杂的推理任务、内容创建、客户服务和软件开发。

*   **安全和负责任的AI：** OpenAI可能强调其对安全和负责任的AI开发的承诺，提及为减轻与新模型相关的潜在风险（例如偏见、错误信息和滥用）而采取的措施。

简而言之，API中的GPT-4.1公告标志着对现有GPT-4模型的升级，提供了改进的性能、可能更大的上下文窗口以及API的改进，使开发人员能够将增强的功能集成到他们的应用程序中。重点是为广泛的用例提供更强大、更准确和更安全的AI解决方案。

---

## 24. Temu暂停其美国谷歌购物广告

**原文标题**: Temu pulls its U.S. Google Shopping ads

**原文链接**: [https://searchengineland.com/temu-pulls-us-google-shopping-ads-454260](https://searchengineland.com/temu-pulls-us-google-shopping-ads-454260)

Temu暂停美国谷歌购物广告致排名骤降，或长期损害中小企业

Temu是一家以补贴直销订单闻名的在线市场。2025年4月9日，该公司暂停了其在美国的谷歌购物广告，导致其App Store排名急剧下降。此次排名下降恰逢特朗普政府提高中国进口关税。

Temu对谷歌广告在用户获取方面的依赖性，在该应用停止广告活动后排名迅速下降一事中暴露无遗。该公司依赖大量补贴订单的商业模式，因新的关税和对进口漏洞的打击而进一步受到削弱。

文章指出，由于Temu退出竞价平台，其他电商广告商可能会在数字广告成本方面获得暂时的缓解，导致每次点击成本（CPC）和每次转化成本可能下降。然而，推动Temu撤退的关税最终可能会长期损害中小企业。

尽管遭遇了挫折，文章的结论是，Temu的母公司在财务上仍然稳定，并且根据未来贸易政策的变化，有可能重返美国市场。

---

## 25. Typewise (YC S22) 正在招聘机器学习工程师 (苏黎世，瑞士)

**原文标题**: Typewise (YC S22) Is Hiring an ML Engineer (Zurich, Switzerland)

**原文链接**: [https://www.ycombinator.com/companies/typewise/jobs/u4OdKNh-machine-learning-engineer-f-m-x](https://www.ycombinator.com/companies/typewise/jobs/u4OdKNh-machine-learning-engineer-f-m-x)

Typewise（YC S22）是一家瑞士-美国人工智能客户服务平台，正在瑞士苏黎世招聘机器学习工程师。他们正在寻找具有2年以上构建和部署机器学习算法经验，尤其是在自然语言处理和大型语言模型方面，并且精通Python和云系统（AWS、Docker、Kubernetes）的人才。

Typewise 致力于通过使用定制人工智能技术来提高企业的客户服务和销售生产力，在提高沟通质量和客户满意度的同时，减少高达 50% 的工作量。他们与现有系统集成，并优先考虑企业级安全。他们在人工智能开发方面与苏黎世联邦理工学院人工智能中心密切合作。

该职位涉及研究、开发和部署自然语言处理算法，与企业客户合作定制解决方案，并为 Typewise 人工智能技术的持续改进做出贡献。公司提供灵活、快节奏、远程优先的工作环境，每季度举行一次线下聚会，提供具有竞争力的薪酬和股票期权。Typewise 强调产生全球影响、精益开发和个人所有权。

理想的候选人拥有计算机科学学位（或同等经验）、强大的编程技能和团队合作精神。

---

## 26. 六位验证码背后的秘密：从零构建HOTP和TOTP

**原文标题**: Behind the 6-digit code: Building HOTP and TOTP from scratch

**原文链接**: [https://blog.dogac.dev/how-do-one-time-passwords-work/](https://blog.dogac.dev/how-do-one-time-passwords-work/)

本文解释了一次性密码（OTP），特别是基于HMAC的一次性密码（HOTP）和基于时间的一次性密码（TOTP）的工作原理，以及如何从头开始构建它们。 OTP优于静态密码，因为它们仅在一次使用或短时间内有效，从而减轻了重放攻击。 核心概念涉及用户和服务器之间的共享密钥，但算法不是直接使用密钥，而是基于密钥生成动态代码。

HOTP使用一个计数器，该计数器随着每个OTP请求而递增。 TOTP用当前时间替换计数器，从而更容易同步并减少代码的有效窗口（通常为30秒）。

本文详细介绍了TOTP是如何构建在HOTP之上的。 时间使用公式 \( c(t) = \left\lfloor \frac{t - t_0}{X} \right\rfloor \) 转换为计数器\(c(t)\)，其中\(t_0\)是起始时间（Unix纪元），\(X\)是时间间隔。

HOTP的生成涉及密钥、哈希函数和所需的位数。 基于哈希的消息认证码（HMAC）在保护过程中起着至关重要的作用，确保密钥不能轻易地从生成的代码中推导出来。 然后，本文将介绍HMAC-SHA1和DT（动态截断）函数，以缩小输出并产生最终结果。

最后，HOTP函数定义为 \(\text{HOTP}(K,C) = \text{DT}(\text{HMAC}(K,C)) \bmod 10^{\text{digits}} \)。 将计数器\(C\)替换为\(c(t)\)可将其转换为TOTP代码。

作者还提供了演示应用程序和GitHub存储库的链接，展示了HOTP和TOTP的Kotlin实现。

---

## 27. 《闪灵》诡异照片背后45年谜团据信已解开

**原文标题**: 45-year mystery behind eerie photo from The Shining is believed to be solved

**原文链接**: [https://www.cbc.ca/lite/story/1.7507349](https://www.cbc.ca/lite/story/1.7507349)

围绕斯坦利·库布里克《闪灵》中一张照片的45年谜团似乎已被退休学者阿拉斯代尔·斯帕克和《纽约时报》记者阿里克·托拉尔破解。这张标志性的照片拍摄于1921年7月4日，描绘了杰克·尼科尔森扮演的角色杰克·托兰斯叠加在一个聚会人群中的人物身上。

斯帕克和托拉尔的调查揭示了被尼科尔森的脸覆盖的人的身份：桑托斯·卡萨尼，20世纪20年代伦敦一位著名的舞厅舞蹈家。他们通过比对他在英国皇家空军服役期间面部受伤留下的疤痕与原照片中那人的毁容外观，证实了他的身份。卡萨尼的真名叫约翰·戈尔曼。

该团队还发现了照片本身的来源。起初人们认为它来自华纳兄弟的档案，但事实证明这是一个误解。实际来源是BBC霍顿照片图书馆（现在是盖蒂图片社的一部分）。这张照片拍摄于1921年2月14日情人节，地点在伦敦皇家宫殿酒店的皇后舞厅。斯帕克对解决围绕照片的主题、地点和日期的长期谜团表示满意。

---

## 28. 使用单个SQLite表和少量cron任务的可定制AI助手

**原文标题**: A hackable AI assistant using a single SQLite table and a handful of cron jobs

**原文链接**: [https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs](https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs)

本文介绍 Stevens，一个由作者构建的个人 AI 助手，它采用了一种出人意料的简单架构：一个单独的 SQLite 表作为“笔记本”来存储记忆，以及少量的 cron 任务用于数据摄取和更新，所有这些都托管在 Val.town 上。

Stevens 通过 Telegram 提供每日简报，包括日历安排、天气预报、邮件预览和提醒，所有内容都以正式、管家式的口吻编写。用户还可以通过 Telegram 或电子邮件按需与 Stevens 通信，转发信息或提出问题。

Stevens 的核心在于其 SQLite 表，该表存储包含文本和可选相关日期的日志条目。这些条目由各种数据导入器填充：Google 日历、天气 API、USPS 知情投递（通过 Claude 进行 OCR 处理），以及通过 Telegram 和电子邮件的直接用户输入。cron 任务定期从 SQLite 表中收集相关记忆，将其提供给 Claude API，并通过 Telegram 发送生成的更新。

作者强调了从多个信息来源获取更广泛上下文的力量，展示了一个简单的聊天机器人如何通过日历和天气感知成为有用的助手。他认为，“记忆”最初可以简单地实现，只有在信息池增长时才需要更复杂的 RAG 技术。作者还强调了“氛围编码”的价值，即定制助手的语气和 UI，以获得更愉悦的用户体验。

Stevens 的代码可供那些希望试验这种基本模式来构建自己的 AI 工具的人使用，该模式使用单个记忆表和可扩展的 cron 任务。

---

## 29. DeepSeek 推理引擎开源之路

**原文标题**: The path to open-sourcing the DeepSeek inference engine

**原文链接**: [https://github.com/deepseek-ai/open-infra-index/tree/main/OpenSourcing_DeepSeek_Inference_Engine](https://github.com/deepseek-ai/open-infra-index/tree/main/OpenSourcing_DeepSeek_Inference_Engine)

DeepSeek致力于为开源社区做出贡献，并决定分阶段开源其内部推理引擎。受之前开源库发布后获得的积极反响启发，DeepSeek认识到开源生态系统，尤其是像PyTorch和vLLM这样的项目，在推动AGI发展中的重要作用。

然而，直接开源其整个内部引擎面临着挑战：该引擎基于一个较旧、高度定制的vLLM分支，与DeepSeek的内部基础设施紧密集成，并且团队缺乏进行全面维护的资源。

DeepSeek将采取与现有开源项目合作的方式，以实现更可持续的方法，而不是完全发布。这包括：

*   **提取独立功能:** 将模块化、可重用的组件作为独立库贡献。
*   **分享优化:** 直接向现有项目贡献设计改进和实现细节。

DeepSeek旨在回馈开源社区，并将这种协作方式视为支持其发展和为AGI进步做出贡献的最佳途径。本文阐明，这种开源策略专门适用于推理引擎代码库。DeepSeek计划在新模型发布前主动同步推理相关的工程工作，致力于从一开始就在各种硬件平台上实现无缝集成和最先进的支持，从而促进协作生态系统。

---

## 30. Meta 反垄断审判在联邦法院开庭

**原文标题**: Meta antitrust trial kicks off in federal court

**原文链接**: [https://www.axios.com/pro/tech-policy/2025/04/14/ftc-meta-antitrust-trial-kicks-off-in-federal-court](https://www.axios.com/pro/tech-policy/2025/04/14/ftc-meta-antitrust-trial-kicks-off-in-federal-court)

无法访问文章链接。

---

## 31. JEP 506：作用域值在Java 25中定稿

**原文标题**: JEP 506: Scoped Values final for Java 25

**原文链接**: [https://openjdk.org/jeps/506](https://openjdk.org/jeps/506)

JEP 506 提议在 Java 25 中最终确定作用域值 (Scoped Values)，这是一种 API，旨在在线程内以及与子线程之间共享不可变数据，与线程局部变量相比具有优势。

作用域值旨在提高易用性、可理解性、稳健性和性能，优于线程局部变量。它们解决了与线程局部变量相关的未受约束的可变性、无界生命周期和昂贵的继承问题，尤其是在虚拟线程 (JEP 444) 和结构化并发 (JEP 505) 的背景下。

本文重点介绍了一种常见场景，即框架需要与应用程序代码共享上下文数据，传统上是通过方法参数或线程局部变量来实现的。作用域值提供了一种更简洁的替代方案，允许将数据绑定到定义代码块中的 `ScopedValue` 实例。在该代码块内直接或间接调用的任何方法都可以使用 `get()` 访问该值。这确保了数据仅在有限的时间内可访问，并防止不相关代码的修改。

与线程局部变量相比，作用域值提供不可变的共享，从而更好地推理数据流。它们还提供潜在的性能优势，尤其是在大量虚拟线程的情况下，因为可以有效地共享数据。本文强调，最终确定作用域值不会弃用线程局部变量，而是为特定用例提供更好的替代方案。

---

## 32. OpenAI正在构建一个社交网络

**原文标题**: OpenAI is building a social network

**原文链接**: [https://www.theverge.com/openai/648130/openai-social-network-x-competitor](https://www.theverge.com/openai/648130/openai-social-network-x-competitor)

据消息人士透露，OpenAI正在开发一个社交网络，这可能会加剧与埃隆·马斯克的X和Meta的竞争。该项目目前是一个内部原型，专注于ChatGPT的图像生成，并具有社交动态功能。据报道，CEO萨姆·奥特曼正在寻求关于该项目的外部反馈，但尚不清楚该社交网络将是一个独立的应用程序还是集成到ChatGPT中。

此举将升级OpenAI与马斯克的竞争，尤其是在马斯克主动提出收购OpenAI以及奥特曼反向提议收购X（前身为Twitter）之后。这也将OpenAI置于与Meta的竞争之中，据报道Meta计划在其即将推出的独立AI助手应用程序中添加社交动态。奥特曼此前曾暗示要开发一款社交应用，以回应Meta的ChatGPT竞争对手。

OpenAI涉足社交媒体的关键驱动因素是获取其自己的实时数据（目前由X和Meta持有），以进一步训练其AI模型。该原型探索了使用AI来改进内容共享。

虽然仍处于早期阶段且无法保证公开发布，但该项目表明了OpenAI的扩张雄心，因为人们对该公司的增长期望很高。

---

## 33. 简易Web服务器

**原文标题**: Simple Web Server

**原文链接**: [https://simplewebserver.org/](https://simplewebserver.org/)

此网络服务器设计易用且灵活，主要特性包括：

*   **配置简单：** 通过简洁的界面即可轻松调整服务器选项。
*   **后台执行：** 多个网络服务器可以同时运行，即使应用程序未主动打开。
*   **SPA支持：** 支持单页应用程序，一键启用mod rewrite。
*   **Chrome网络服务器的延续：** 本服务器是Chrome网络服务器的直接后续版本，旨在延续并在此基础上进行构建。
*   **致谢作者：** 本服务器由@terreng和@ethanaobrien开发，延续了@kzahel的工作。

---

## 34. 纯粹形态

**原文标题**: In Its Purest Form

**原文链接**: [https://lareviewofbooks.org/article/in-its-purest-form/](https://lareviewofbooks.org/article/in-its-purest-form/)

无法访问文章链接。

---

## 35. Notion邮箱已上线

**原文标题**: Notion Mail Is Out

**原文链接**: [https://www.notion.com/product/mail](https://www.notion.com/product/mail)

Notion 邮件已发布，iOS 优先体验“随时随地收发邮件”完整功能，“即将推出”更多平台版本。

---

## 36. 展示HN：MCP-Shield – 检测MCP服务器中的安全问题

**原文标题**: Show HN: MCP-Shield – Detect security issues in MCP servers

**原文链接**: [https://github.com/riseandignite/mcp-shield](https://github.com/riseandignite/mcp-shield)

MCP-Shield: 用于扫描模型上下文协议(MCP)服务器安全漏洞的命令行工具。它可以识别潜在威胁，如工具投毒、数据泄露、跨域违规和工具影子。

该工具可以配合或不配合Anthropic Claude API密钥运行，以进行增强的AI驱动分析。它扫描位于标准或指定目录中的MCP配置文件（例如，来自Cursor、Claude Desktop、VSCode的文件）。输出会突出显示存在漏洞的服务器和工具，详细说明风险等级、问题（例如，隐藏指令、敏感文件访问）以及总结潜在影响的AI分析。

MCP-Shield通过查找诸如工具描述中旨在欺骗LLM的隐藏指令、一个工具修改另一个工具行为的工具影子、可能导致数据泄露的可疑参数以及工具试图干扰其他应用程序（例如，拦截WhatsApp消息）的跨域违规等模式来检测漏洞。

该工具旨在用于添加新的MCP服务器之前、安全审计期间、整个MCP服务器开发过程中以及更新之后，以确保安全。它受到Invariant Labs安全研究的启发，并欢迎贡献。MCP-Shield遵循MIT许可证。

---

## 37. 什么是熵？

**原文标题**: What Is Entropy?

**原文链接**: [https://jasonfantl.com/posts/What-is-Entropy/](https://jasonfantl.com/posts/What-is-Entropy/)

杰森·范特尔的《什么是熵？》一文旨在对熵、其各种定义及其与时间的关系提供严谨而直观的理解。文章首先从信息论的角度探讨熵，解释熵如何量化不确定性。范特尔介绍了克劳德·香农的工作，并将信息定义为传达一种状态所需的比特数，而熵则是系统预期之外的惊喜程度。他提出了香农熵方程，并用公平和不公平的骰子等例子来说明，展示了不确定性如何与熵值相关。

文章随后转向物理熵，并用盒子里的球作类比。文章解释说，随着满足大规模测量（宏观状态）的方式数量增加，熵也会增加。宏观状态被定义为对系统的大规模测量（例如，左右两侧球的数量），而微观状态则是满足宏观状态的特定状态。然后，作者提出了一个关键点，即熵并非系统本身固有的，而是取决于我们对它的描述，即我们正在测量的粗粒化/宏观状态，以及我们观察它的分辨率。文章给出了一个例子，其中在更小的单元格中计算球会导致持续更高的熵。作者强调，我们如何选择/测量宏观状态取决于我们正在解决的问题。

---

## 38. 古墓引擎

**原文标题**: Tomb Engine

**原文链接**: [https://tombengine.com/](https://tombengine.com/)

古墓引擎1.8.1是一款开源引擎，旨在创建自定义的古墓丽影冒险。这是一个社区驱动的项目，与官方古墓丽影系列版权所有者（Core Design、Eidos Interactive和Embracer Group AB）无关。虽然古墓丽影是Embracer Group AB的注册商标，但古墓引擎本身是免费的，其代码也是开源的。

该项目的主要目标是鼓励社区贡献，并为教育目的提供资源。开发者强调，该引擎不得出售，他们不对源代码的任何非法使用负责。此外，该项目由无偿贡献者利用业余时间维护，代码按“原样”发布。

文章还提供了相关在线资源的链接：Github（用于代码访问和贡献）、Discord、X-twitter和Youtube。它包含一个目录。

---

## 39. 谷歌将拥抱MCP

**原文标题**: Google to embrace MCP

**原文链接**: [https://techcrunch.com/2025/04/09/google-says-itll-embrace-anthropics-standard-for-connecting-ai-models-to-data/](https://techcrunch.com/2025/04/09/google-says-itll-embrace-anthropics-standard-for-connecting-ai-models-to-data/)

谷歌将在其Gemini模型和SDK中采用Anthropic的Model Context Protocol (MCP)，此前OpenAI已采取类似举措。Google DeepMind首席执行官Demis Hassabis通过X宣布了这一决定，并表示MCP正迅速成为AI代理的开放标准。

MCP有助于将AI模型连接到数据源，如业务工具、内容存储库和应用程序开发环境。它允许开发者通过暴露数据的“MCP服务器”和构建“MCP客户端”，在这些数据源和AI驱动的应用程序（如聊天机器人）之间建立双向连接。

Anthropic已开源MCP，Block、Apollo、Replit、Codeium和Sourcegraph等公司已经将该协议集成到他们的平台中。谷歌采用MCP表明，行业内连接AI模型与外部数据的标准化协议的趋势日益增长，从而能够实现更强大和集成的AI应用程序。

---

## 40. 绘制托尔金奇幻世界的威斯康星州制图师

**原文标题**: The Wisconsin cartographer who mapped Tolkien's fantasy world

**原文链接**: [https://www.wpr.org/news/wisconsin-cartographer-karen-wynn-fonstad-mapped-tolkien-fantasy-world-oshkosh](https://www.wpr.org/news/wisconsin-cartographer-karen-wynn-fonstad-mapped-tolkien-fantasy-world-oshkosh)

本文介绍了威斯康星州地图制图师凯伦·温·丰斯塔德，她创作了详细的《中土世界地图集》，这是托尔金世界的官方地理指南。丰斯塔德是一位地理爱好者和托尔金迷，她根据《霍比特人》、《魔戒》和《精灵宝钻》中的地理细节，精心绘制了172幅手绘地图。

在她去世二十年后，她的丈夫托德和儿子马克（都是地理学家）正在努力将她的原始地图数字化，希望以此保存她的遗产并找到一个档案馆来收藏它们。马克在威斯康星大学麦迪逊分校的罗宾逊地图图书馆花了一周时间扫描了大量藏品，其中包括中土世界的地图，以及其他幻想世界的地图，包括未出版的纳尼亚地图和《龙与地下城》的地图。

丰斯塔德的《中土世界地图集》极具影响力，启发了彼得·杰克逊的《魔戒》电影背后的创作团队。J.R.R.托尔金的儿子克里斯托弗·托尔金称赞了她的作品。除了她的制图成就外，丰斯塔德还积极参与奥什科什社区的活动，在城市规划委员会和普通委员会任职。马克希望数字化副本能让人们以新的方式观看地图，可能通过虚拟现实。他指出，他母亲的作品被认为是幻想地图制作的标杆，她会很高兴它能继续激励人们。

---

## 41. 器官贩卖：德国人在肯尼亚购买新肾脏

**原文标题**: Organ Trafficking: How Germans Buy New Kidneys in Kenya

**原文链接**: [https://www.spiegel.de/international/world/organ-trafficking-how-germans-buy-new-kidneys-in-kenya-a-a16089cf-5bb6-40d3-ac38-fac8ef3eff4d](https://www.spiegel.de/international/world/organ-trafficking-how-germans-buy-new-kidneys-in-kenya-a-a16089cf-5bb6-40d3-ac38-fac8ef3eff4d)

《明镜周刊》调查：德国人在肯尼亚的非法器官交易

本文调查了非法器官贩运交易，重点讲述像萨宾娜·费舍尔-库格勒这样的德国人如何通过Medlead公司在肯尼亚获得肾脏移植。由于急于避免在德国漫长的透析等待名单，患者支付高达20万欧元的肾脏费用，这些肾脏通常来自阿塞拜疆等国的贫困捐赠者，他们只收到其中一小部分（2000-5000欧元）。

Medlead公司以隐蔽的结构和可疑的过去运营，在肯尼亚埃尔多雷特的Mediheal诊所促成这些移植。文章强调，Medlead公开在网上宣传“四到六周内完成肾脏移植”，引导客户通过WhatsApp进行安排。他们利用成功案例和推荐信来吸引德国患者。

调查揭露了Medlead老板罗伯特·施波兰斯基的犯罪背景，他此前因参与国际器官贩运网络在以色列被起诉。他涉嫌在肯尼亚继续从事这些活动，利用患者的绝望和捐赠者的脆弱性。虽然当局已经得到警报，但这种交易仍在继续，凸显了全球肾脏资本主义的伦理和法律复杂性。文章还谈到了患者面临的法律风险，因为德国法律禁止接受购买的器官，否则将处以监禁。该团队的调查揭示了德国患者和肯尼亚诊所之间的联系。

---

## 42. DolphinGemma：谷歌AI如何助力解读海豚交流

**原文标题**: DolphinGemma: How Google AI is helping decode dolphin communication

**原文链接**: [https://blog.google/technology/ai/dolphingemma/](https://blog.google/technology/ai/dolphingemma/)

本文探讨了DolphinGemma，这是一个由谷歌AI开发，旨在帮助科学家理解海豚交流的模型。DolphinGemma与野生海豚项目(WDP)和佐治亚理工学院合作开发，分析海豚的叫声，以识别模式、预测声音序列，并可能揭示其含义。

WDP数十年的研究提供了独特的水下视频和音频数据集，其中包含个体海豚的身份和行为信息。DolphinGemma建立在谷歌的Gemma模型之上，利用这些数据来学习海豚声音的结构并生成新的类海豚序列。它的大小经过优化，可以直接在野外使用的Pixel手机上运行，从而促进实时分析。

除了分析自然交流之外，该项目还探索使用CHAT（鲸类听觉增强遥测）系统进行双向互动。CHAT旨在通过将合成口哨声与海豚喜欢的物品联系起来，建立共享词汇，鼓励它们模仿口哨声来“请求”这些物品。谷歌Pixel手机为CHAT提供动力，为实时分析和响应提供必要的处理能力。

谷歌计划将DolphinGemma作为一个开放模型分享，允许研究其他鲸类物种的研究人员利用其功能。该项目希望加速海豚交流模式的搜索，加深我们对这些海洋哺乳动物的理解，并弥合人类与海豚互动之间的差距。

---

## 43. Omnom：可自托管的书签，带可搜索的所见即所得快照

**原文标题**: Omnom: Self-hosted bookmarking with searchable, wysiwyg snapshots

**原文链接**: [https://omnom.zone/?src=hn](https://omnom.zone/?src=hn)

Omnom是一个自托管的书签工具，允许用户保存和组织他们的网络书签。其关键功能是能够创建可搜索的、所见即所得 (WYSIWYG) 的书签页面快照。这意味着用户可以保存书签时网页的视觉呈现，确保即使原始页面更改或消失，他们也能访问内容。

本网站提供的只是该工具的只读演示，鼓励用户在 GitHub 上进一步探索该项目，以了解更多关于功能、安装和开发细节的信息。本质上，Omnom 旨在提供一个强大而可靠的书签解决方案，并增加可视化地保存书签内容的好处。

---

## 44. 使用 Podman Desktop 的 Podman 四元组

**原文标题**: Podman Quadlets with Podman Desktop

**原文链接**: [https://podman-desktop.io/blog/podman-quadlet](https://podman-desktop.io/blog/podman-quadlet)

本文介绍Podman Quadlets，这是一种轻量级解决方案，用于使用systemd以声明方式管理容器，非常适合单节点服务器或Kubernetes过度使用的开发环境。Quadlets是简化的配置文件（例如，*.container, *.pod），Podman使用它们生成systemd单元文件，从而简化容器管理，包括拉取镜像、创建卷和管理pod。

Quadlets的优势包括声明式配置、通过systemd与Linux的紧密系统集成以及易于自动化，例如在启动时自动启动容器或在失败时重新启动。

然后，本文重点介绍Podman Desktop中的Podman Quadlet扩展，该扩展简化了Quadlets的管理，尤其是在非Linux平台上。该扩展允许用户以可视方式列出、生成和编辑Quadlets。主要功能包括与Podlet集成，以便从现有Podman对象生成Quadlets，用于Quadlet管理的专用UI（启动、停止、编辑、删除）以及用于通过journalctl进行故障排除的日志查看器。

本文演示了如何安装扩展程序、列出现有Quadlets、使用Podlet从运行中的容器生成Quadlets、编辑Quadlet配置以及查看Quadlet日志。结论是，Podman Quadlets与Podman Desktop扩展相结合，提供了一种强大而便捷的方式，可以使用systemd以声明方式管理容器，从而弥合了基本容器管理和复杂编排工具之间的差距。

---

## 45. SQLite 文件格式查看器

**原文标题**: SQLite File Format Viewer

**原文链接**: [https://sqlite-internal.pages.dev](https://sqlite-internal.pages.dev)

此“文章”本质上只是一个标题“SQLite文件格式查看器”，以及正文中对该标题的重复。因此，可总结的内容很少。

核心要点是，该文档意在讨论一个名为“SQLite文件格式查看器”的应用程序或工具。我们可以推断，该工具的目的是允许用户：

*   **检查SQLite文件：** 该工具很可能允许用户打开并检查SQLite数据库文件的结构。
*   **理解SQLite文件格式：** 据推测，它提供了可视化和解释SQLite数据库文件底层二进制格式的功能，而不仅仅是以表格视图显示数据。这可能涉及理解页面结构、头部信息以及数据如何在文件中组织。

在没有更多信息的情况下，不可能知道具体的功能或特性，但标题表明它是一个用于深入分析SQLite文件底层结构的工具。

---

## 46. 美国如何成为科学强国

**原文标题**: How the U.S. Became a Science Superpower

**原文链接**: [https://steveblank.com/2025/04/15/how-the-u-s-became-a-science-superpower/](https://steveblank.com/2025/04/15/how-the-u-s-became-a-science-superpower/)

本文分析了二战后美国如何超越英国，成为全球科技超级大国并保持了85年领先地位。文章对比了美英两国在战争期间的不同策略，将美国的成功归功于范内瓦·布什的以大学为基础、由政府资助的武器实验室模式，而英国则依赖于由弗雷德里克·林德曼教授指导的政府运营军事实验室。

由于资源限制和战时压力，丘吉尔领导下的英国专注于利用现有政府实验室满足眼前的国防需求。受布什对政府实验室的不信任影响，美国将巨额联邦资金（按2025年币值计算为90亿美元）投入大学研究，使大学成为战时研究的全面合作伙伴，从而在各个领域取得快速进展并促进了创新集群的形成。

战后，英国的财政紧缩、国有化以及缺乏对商业化的投资阻碍了其利用科学突破的能力。与此同时，美国通过原子能委员会、国家科学基金会、DARPA和NASA等机构继续为研究提供政府资助，这受到了布什的报告《科学：无尽的前沿》的推动。这促成了一个蓬勃发展的大学-产业-政府合作伙伴关系，硅谷就是典范，并促进了战争期间开发的技术的商业化。间接成本报销制度使美国大学相对于其他所有国家都具有巨大优势。

文章总结认为，虽然英国在理论科学方面表现出色，但美国去中心化、协作的生态系统，在政府资助的推动下，促进了创新和经济增长。文章也提出了担忧，即2025年美国政府对大学研究的支持减少可能会危及其持续的主导地位，尤其是在中国对科学技术的巨额投资的背景下。

---

## 47. 谷歌员工... 前谷歌员工

**原文标题**: Googler... ex-Googler

**原文链接**: [https://nerdy.dev/ex-googler](https://nerdy.dev/ex-googler)

谷歌员工亚当（argyle@google.com）突然被解雇，这一决定甚至令他的经理和Chrome团队领导感到震惊。他对这次解雇的突然性以及缺乏明显的理由表示深深的悲伤、愤怒和难以置信。尽管他被告知有可能在谷歌内部找到其他职位，但他立即被剥夺了访问公司系统和资源的权限，这让他感到不受欢迎，并像个罪犯一样被对待。

这次裁员的时机尤其令人震惊，因为它发生在一次富有成效且鼓舞人心的Chrome团队外部会议之后不久。亚当强调了他积极参与的众多职责和项目，包括准备谷歌I/O大会（视频、舞台表演、展位管理和开发者主题演讲支持）、他的CSS工作组成员资格、开发者办公时间、Carousel Gallery代码访问以及对谷歌CSS工作的贡献。所有这些承诺都立即被取消。

亚当哀叹失去了他的工作以及他多年来建立的关系，感到被背叛、不被赏识，并且被简化为大型公司中的一个小小齿轮。他分享了他与失眠作斗争的经历以及羞愧和愤怒的感觉。他提供了他的Bluesky账号和个人邮箱（adam.is@nerdy.dev），以便那些想联系他的人联系，并承认由于情况的压倒性，他可能回复较慢。

---

## 48. LightlyTrain：更佳视觉模型，更快 – 无需标注

**原文标题**: LightlyTrain: Better Vision Models, Faster – No Labels Needed

**原文链接**: [https://github.com/lightly-ai/lightly-train](https://github.com/lightly-ai/lightly-train)

LightlyTrain：利用无标签数据加速计算机视觉模型开发。它通过利用无标签数据进行自监督预训练，加速计算机视觉模型的开发。无需大量手动标注，节省时间和资源。用户可以在其特定领域数据（例如，视频分析、医疗保健）上预训练模型，从而获得更好的性能和领域适应性。

LightlyTrain兼容各种模型架构和任务，包括检测、分类和分割，并且可以轻松地从单GPU扩展到多GPU设置。它支持流行的框架，如Torchvision、TIMM和Ultralytics。

该工具用户友好，只需极少的自监督学习专业知识。它可以自动化预训练过程，并以适合微调的格式导出模型。主要功能包括支持各种训练方法（DINOv2蒸馏，DINO，SimCLR），用于微调或推理的模型导出，以及与TensorBoard和Weights & Biases的集成以进行监控。

LightlyTrain非常适合标记数据有限、标记过程缓慢或公共可用的预训练模型不足以满足特定领域数据集的工程师和团队。它提供灵活的许可选项，包括用于开源项目的AGPL-3.0和用于专有开发的商业许可。

---

## 49. 激光发射入轨

**原文标题**: Laser Launch into Orbit

**原文链接**: [http://toughsf.blogspot.com/2017/03/laser-launch-into-orbit.html](http://toughsf.blogspot.com/2017/03/laser-launch-into-orbit.html)

本文探讨了激光发射系统作为一种潜在的入轨和超越轨道的方法，并将其与传统火箭技术进行了对比。激光发射的优势在于将能量源（地面激光器）与航天器分离，从而可能实现更高的比冲（Isp）和显著降低的每公斤入轨成本（1-100美元/公斤）。这是通过使用强大的激光直接加热推进剂或产生推力来实现的。

本文概述了几个挑战。激光发生器通常效率低下，并且激光束在穿过大气层时会因吸收而产生损耗，尤其是在多云条件下。千兆瓦级的激光器需要在硬件、电力存储、聚焦阵列和跟踪系统方面进行大量的预先投资，这可能会阻止潜在的投资者。大气畸变也需要自适应光学器件来实现精确的波束瞄准。

本文随后探讨了不同的激光推进方法：激光光帆（不适合地面发射）、烧蚀激光推进（使用脉冲激光烧蚀材料产生推力）、双脉冲激光烧蚀（一种更复杂的烧蚀方法，具有更高的比冲）、燃料丸烧蚀推进（使用激光加热的燃料丸作为推进剂）和激光加热等离子体推进（加热大气空气作为推进剂）。每种方法在比冲、效率和实施复杂性方面都有其自身的优势和劣势。总的来说，本文表明，虽然激光发射系统有望彻底改变太空通道，但仍存在重大的技术和财务障碍。

---

## 50. 你不能获取我们用户的数据。

**原文标题**: You cannot have our user's data

**原文链接**: [https://sourcehut.org/blog/2025-04-15-you-cannot-have-our-users-data/](https://sourcehut.org/blog/2025-04-15-you-cannot-have-our-users-data/)

SourceHut正积极使用Anubis等工具保护其服务免受侵略性LLM爬虫的侵害，并明确其数据使用立场。他们明确禁止将从SourceHut收集的数据用于盈利、训练机器学习模型或任何与改进开源软件无关的目的，除非获得明确许可。其服务条款和`robots.txt`文件反映了此政策。

他们已经注意到LLM抓取的效率低下和版权侵权问题，并驳斥了关于他们应该优化基础设施以适应这些爬虫的观点。SourceHut认为LLM公司无权使用他们的数据，并且他们对与这些公司谈判或提供定制解决方案不感兴趣。

SourceHut强调，可用的公共数据旨在供开源软件的用户和贡献者使用。他们的资金来自订阅，而不是数据销售，他们认为自己是用户数据的管理者，致力于服务于用户的最佳利益和公共利益。他们将自己与拥有LLM产品且可能存在利益冲突的GitHub等公司区分开来。最后，他们正在探索诸如“go-away”之类的替代方法，以在最大限度减少用户影响的情况下对抗抓取。

---

## 51. Show HN: 无需代码生成、无需编译，从Protobufs推断TypeScript类型

**原文标题**: Show HN: Zero-codegen, no-compile TypeScript type inference from Protobufs

**原文链接**: [https://github.com/nathanhleung/protobuf-ts-types](https://github.com/nathanhleung/protobuf-ts-types)

这个 "Show HN" 帖子介绍 `protobuf-ts-types`，一个 TypeScript 库，它可以直接从 Protobuf 定义推断 TypeScript 类型，而无需代码生成或编译。它利用 TypeScript 的模板字面量类型来解析 Protobuf 字符串并生成相应的 TypeScript 类型。

该库通过直接 GitHub 链接安装，并通过导入 `pbt` 命名空间使用。然后，您可以将 Protobuf schema 作为字符串传递给 `pbt.infer`，它会推断 TypeScript 类型。您可以获得所有消息名称到其类型的映射，也可以指定特定的消息名称以仅获取该消息的类型。

该帖子提供了一个清晰的示例，使用了 `Person` 和 `Group` Protobuf 消息，并演示了 TypeScript 如何使用推断的类型来验证传递给诸如 `greetPerson` 和 `greetGroup` 等函数的数据。这确保了基于 Protobuf 定义的类型安全。

作者强调这只是一个概念验证，尚未达到生产级别，并强调了诸如不支持 `services`、`rpcs`、`oneof`、`map` 字段和 `imports` 等限制。由于 TypeScript 的问题，如果没有 `ts-patch`，导入 .proto 文件也存在问题。最后，API 文档详细介绍了 `pbt.infer`，解释了它如何将 Protobuf 定义映射到 TypeScript 类型。

---

## 52. AudioX：万物到音频生成的扩散变换器

**原文标题**: AudioX: Diffusion Transformer for Anything-to-Audio Generation

**原文链接**: [https://zeyuet.github.io/AudioX/](https://zeyuet.github.io/AudioX/)

AudioX：用于生成通用音频和音乐的统一扩散Transformer模型

AudioX 引入了一种统一的扩散Transformer模型，可以根据文本、视频、图像、音乐和音频等多种输入模态生成通用音频和音乐。 这种方法解决了现有方法的局限性，这些方法通常是特定领域的、数据稀缺的，并且难以集成不同的输入。

其核心创新在于一种多模态掩码训练策略，该策略掩盖跨模态的输入，以培养稳健且统一的跨模态表征。 这使AudioX能够学习不同输入类型之间的关系并有效地生成相应的音频。

为了克服数据稀缺问题，作者创建了两个大型数据集：vggsound-caps（19万个音频字幕）和V2M-caps（600万个音乐字幕）。 这些数据集为模型提供了必要的训练数据，以实现高质量的音频和音乐生成。

实验结果表明，AudioX的性能与最先进的专用模型相当甚至超过了它们。 它的主要优势在于其多功能性：它可以处理不同的输入模态，并在一个统一的架构中生成通用音频和音乐，展示了其在各种应用中的潜力。

---

## 53. 伊夫林·沃的颓废救赎

**原文标题**: Evelyn Waugh’s Decadent Redemption

**原文链接**: [https://libertiesjournal.com/online-articles/evelyn-waughs-decadent-redemption/](https://libertiesjournal.com/online-articles/evelyn-waughs-decadent-redemption/)

伊夫林·沃的颓废式救赎：本文认为，伊夫林·沃的作品揭示了一个从两次世界大战期间颓废虚无的氛围到后来更具宗教基础和道德严肃性的复杂旅程。文章指出，沃早期的小说，如《衰落与瓦解》和《罪恶的肉身》，通过怪诞而常常残酷的幽默讽刺了英国上层阶级的荒谬和道德破产，但同时也流露出对秩序和意义的渴望。

作者认为，沃于1930年皈依天主教标志着一个转折点，影响了他后期的作品，尤其是《故园风雨后》。早期的沃沉迷于描绘社会的肤浅和道德堕落，而他后期的作品，虽然仍然具有讽刺意味，但探讨了信仰、传统以及在堕落的世界中美丽和恩典的持久力量等主题。

文章强调，沃后期的作品不仅仅是对他早期颓废的否定，而是一种转变。作者认为，他后来更为保守的世界观的种子早已存在于他早期的作品中，表现为对当时普遍存在的道德混乱的深刻不满。《故园风雨后》尤其被认为是这一旅程的顶峰，描绘了一个寻求救赎的精神之旅和天主教信仰的持久影响力。最终，文章提出，沃的轨迹是颓废的情感在传统和宗教信仰中找到慰藉和意义，从而产生了一种细致入微且常常自相矛盾的艺术视野。

---

## 54. 英特尔以87.5亿美元估值向私募股权公司出售Altera 51%的股份

**原文标题**: Intel sells 51% stake in Altera to private equity firm on a $8.75B valuation

**原文链接**: [https://newsroom.intel.com/corporate/intel-partner-deal-news-april2025](https://newsroom.intel.com/corporate/intel-partner-deal-news-april2025)

英特尔已同意以87.5亿美元的价格将旗下Altera业务51%的股份出售给私募股权公司银湖，从而使Altera成为一家运营上独立的公司以及最大的纯FPGA半导体解决方案供应商。英特尔将保留49%的股份，并参与Altera未来的成功。

Marvell前产品和技术总裁Raghib Hussain将于2025年5月5日生效，接替Sandra Rivera，成为Altera的新任CEO。

该交易旨在提高英特尔的专注度，降低开支并加强其资产负债表。预计银湖的投资将帮助Altera加强其技术领先地位，并投资于边缘计算和机器人等人工智能驱动的市场。英特尔将继续提供代工服务和客户互动。

该交易预计将于2025年下半年完成，尚待获得惯例性批准。在2024财年，Altera创造了15.4亿美元的收入，GAAP运营亏损为6.15亿美元，非GAAP运营收入为3500万美元。

---

## 55. 哈佛大学对联邦政府要求其做出改变的回应

**原文标题**: Harvard's response to federal government letter demanding changes

**原文链接**: [https://www.harvard.edu/president/news/2025/the-promise-of-american-higher-education/](https://www.harvard.edu/president/news/2025/the-promise-of-american-higher-education/)

哈佛大学校长艾伦·加伯就联邦政府致信要求针对校园内反犹太主义指控进行整改一事，向哈佛社群发表讲话。加伯强调，联邦政府与哈佛等高校之间长期保持富有成效的合作关系，促成了各领域的重大创新。他批评政府近期对这些合作关系发出的威胁，认为此类行动可能会阻碍科学进步并损害国家福祉。

加伯指出，政府以威胁哈佛资金为前提提出的要求，并非合作对抗反犹太主义，而是试图控制大学的学术环境。他概述称，政府的要求包括审查观点，并基于意识形态削弱某些个人的权力。

哈佛已告知政府，不会遵守这些要求，并声称这些要求侵犯了大学的独立性和第一修正案权利。加伯强调，任何政府都不应干涉私立大学的课程、招生、招聘或研究重点。

尽管拒绝了政府的具体要求，加伯重申了哈佛打击反犹太主义的决心，并概述了为促进公开探究、建设性互动、学术多样性和一致的纪律程序所做的持续努力。他承诺将继续维护言论自由，同时确保尊重学习和研究的环境，并遵守现有的反种族歧视法律。加伯最后强调了学术自由的重要性以及哈佛对追求真理的奉献。

---

## 56. 如何骑自行车横穿全国

**原文标题**: How to bike across the country

**原文链接**: [https://www.brooks.team/posts/how-to-bike-across-the-country/](https://www.brooks.team/posts/how-to-bike-across-the-country/)

很遗憾，所提供的内容不足以总结如何骑自行车横跨全国。内容仅包含标题、导航元素（“返回主页”）和一个“加载中...”的消息。 这表明实际的文章内容缺失或未成功检索。

因此，如果没有实际内容，我无法提供文章要点和关键信息的摘要。

---

## 57. 潜在空间中的生成建模

**原文标题**: Generative Modelling in Latent Space

**原文链接**: [https://sander.ai/2025/04/15/latents.html](https://sander.ai/2025/04/15/latents.html)

本文探讨了潜在空间生成建模这一流行方法，该方法作用于数据的紧凑、更高层次的表示，而不是直接作用于原始像素或波形。其核心思想是将过程分为两个阶段：

1.  **自编码器训练：** 训练一个自编码器（编码器和解码器），将输入信号映射到紧凑的潜在表示（编码），然后再映射回来。编码器捕获感知上有意义的信息，同时丢弃不太相关的细节。损失函数包括回归损失、感知损失和对抗损失，以确保高保真度和真实感。瓶颈损失可以进一步限制潜在空间的容量。

2.  **生成模型训练：** 在第一阶段的*冻结*编码器产生的潜在空间上训练一个生成模型（通常是自回归或基于扩散的模型）。这使得模型能够专注于学习数据的底层结构，而不会被不相关的噪声所困扰。解码器用于将生成的潜在空间转换回原始输入空间。

文章强调了历史背景，指出最初的生成模型直接作用于像素/波形，但由于高信息内容被难以察觉的噪声所主导，因此扩展变得具有挑战性。VQ-VAE和VQGAN通过引入离散潜在表示和对抗训练，显著推动了该领域的发展，从而实现了更高分辨率的图像生成。潜在扩散模型结合了潜在表示和扩散模型的优点，提高了效率，并能够生成高质量的感知信号。虽然已经尝试了同时学习潜在表示和生成模型的端到端方法，但由于其在改善感知结果以及管理计算和内存约束方面的实际优势，因此两阶段方法更受欢迎。

---

## 58. Grafana 基金会 SDK – 用编程语言构建仪表盘

**原文标题**: Grafana Foundation SDK – build dashboard in programming language

**原文链接**: [https://grafana.github.io/grafana-foundation-sdk/](https://grafana.github.io/grafana-foundation-sdk/)

Grafana基金会SDK是一组库，使开发人员能够使用各种编程语言将Grafana仪表板、警报和其他资源定义并生成为代码。它提供与不同Grafana版本兼容的类型、构建器库和JSON到代码的转换器。这些SDK使用“cog”工具从Grafana公开的模式自动生成。

本文展示了使用Go、Java、PHP、Python和TypeScript创建仪表板的示例，说明了如何以编程方式配置仪表板元素，例如标题、UID、标签、刷新间隔、时间范围、行、面板和数据查询（特别是Prometheus查询）。这些示例创建了一个简单的仪表板，该仪表板使用Prometheus查询显示来自Raspberry Pi的网络接收数据。

Grafana基金会SDK目前处于“公开预览”阶段，这意味着它在Grafana Labs内部使用，但仍在积极开发中。虽然可以供使用，但错误和问题由工程团队处理，不提供随叫随到的支持或SLA。该SDK采用Apache 2.0许可证授权。

---

## 59. Show HN: 便携式巨型文件查看器

**原文标题**: Show HN: Portable Giant File Viewer

**原文链接**: [https://github.com/sunny-chung/giant-log-viewer](https://github.com/sunny-chung/giant-log-viewer)

Show HN: 巨型日志查看器

这是一个便携工具，专为在缺少`less`分页器的平台上查看大型文本文件（高达 4TB）而设计。该软件占用内存小（JVM 限制为 80MB 堆），不受文件大小影响，可实现即时加载。它旨在为需要在`less`不可用时快速简便地检查日志的用户提供帮助。

主要限制包括仅支持 UTF-8 和 ASCII 编码，与长行（>= 1MB）和表情符号序列不兼容，以及仅在带有 GUI 的 Windows、macOS 和 Linux 上运行。该应用程序提供类似 `less` 的导航快捷键，可通过 UI 中的“？”按钮查看。

用户只需拖放文本文件即可打开它们。作者承认缺少代码签名，并建议检查源代码或自行构建应用程序。欢迎提交错误报告和贡献代码，但不太愿意使用第三方库。该项目鼓励捐款以支持未来的代码签名。

---

## 60. 蒙特卡洛速成课：采样

**原文标题**: Monte Carlo Crash Course: Sampling

**原文链接**: [https://thenumb.at/Sampling/](https://thenumb.at/Sampling/)

本文提供蒙特卡洛方法中采样技术的速成课程，重点介绍如何从各种分布中生成随机样本，这对于诸如蒙特卡洛积分之类的任务至关重要。文章首先解释了如何使用伪随机数生成器（PRNG）创建看似均匀随机的序列，并强调了均匀性、独立性和非周期性等属性。

然后，文章深入探讨了几种采样算法：

*   **拒绝采样：** 通过从更大的域中采样并拒绝落在所需区域之外的样本，将简单的域采样器转换为复杂域的采样器。文章解释了均匀拒绝采样和非均匀拒绝采样，后者需要PDF比率的有限上限。
*   **逆采样：** 对具有可逆累积分布函数（CDF）的一维分布进行采样。逆CDF将概率映射到对应的值。边缘逆采样通过迭代采样每个维度的边缘分布，将此方法扩展到更高的维度。
*   **坐标变换：** 一种转换随机变量的通用技术，使用诸如极坐标之类的变换来对单位圆盘进行采样。该方法通过考虑逆变换的雅可比行列式来调整面积扭曲，以保持所需的分布。

文章强调了高效采样的重要性，并解释了当目标分布没有使用初始分布的大部分概率密度时，拒绝采样可能效率低下。文章还提供了数学推导来支持每种方法。

---

## 61. Ada 中的 ASCII 查找工具

**原文标题**: ASCII Lookup Utility in Ada

**原文链接**: [https://coniferproductions.com/ada/ohyes/ascii-lookup-utility/](https://coniferproductions.com/ada/ohyes/ascii-lookup-utility/)

本文提供了一个循序渐进的指南，教你如何仅使用标准库在Ada中创建一个ASCII查询实用程序。作者详细介绍了构建一个命令行工具的过程，该工具在不带参数调用时打印完整的ASCII表，并在使用数字参数（十进制、十六进制、八进制或二进制格式）调用时提供有关特定字符代码的信息。

本教程首先概述项目的目的并设置Ada开发环境。然后逐步构建实用程序。初始框架包括一个用于打印ASCII表和显示第一个命令行参数的占位符。

下一阶段重点介绍如何打印完整的ASCII表，使用`Ada.Characters.Handling`包及其`ISO_646`子类型。文章介绍了一个`Print_Row`过程来格式化每个字符的输出，包括其十进制、十六进制、八进制和二进制表示形式。

为了提高输出的可读性，作者创建了一个自定义的`Print_Value`过程，用于处理零填充并删除不必要的基指示符。该过程使用了`Ada.Strings.Fixed`包中的字符串操作。

最后，本教程涵盖了命令行参数解析，包括识别数字前缀（0x、0b、0o）的函数以及无效输入的错误处理。完成后的实用程序允许用户从命令行快速查找ASCII字符信息。文章强调了标准Ada库的使用，并为每个步骤提供了可下载的代码示例。

---

## 62. 科学史上最令人发指的剽窃案之一——DNA之争

**原文标题**: One of the Most Egregious Ripoffs in the History of Science – The Race to DNA

**原文链接**: [https://nautil.us/one-of-the-most-egregious-ripoffs-in-the-history-of-science-238331/](https://nautil.us/one-of-the-most-egregious-ripoffs-in-the-history-of-science-238331/)

这篇《鹦鹉螺》杂志上凯文·伯杰的文章总结了霍华德·马克尔的著作《生命之秘》，该书深入探讨了发现DNA结构过程中充满争议的竞赛。文章突出了幕后发生的不道德行为和“莎士比亚式的阴谋诡计”，重点关注了罗莎琳德·富兰克林的遭遇和被低估的贡献。

尽管詹姆斯·沃森讲述了一个充满魅力的轶事，声称他受到与莫里斯·威尔金斯会面的启发，但文章揭露了一个更加卑鄙的开端，其背后充斥着私人事务和社会运作。沃森被描绘成故事中的“伊阿古”，对富兰克林进行人格诋毁，并在未获得适当承认的情况下从她的工作中获益。

文章详细描述了威尔金斯如何在未经富兰克林许可的情况下向沃森展示了“51号照片”，揭示了DNA的双螺旋结构。此外，马克斯·佩鲁茨也在未经她同意的情况下与沃森和克里克分享了富兰克林的分析报告。马克尔认为，这些行为构成了对富兰克林知识产权的“令人震惊的窃取”。虽然克里克最终对富兰克林表示了一定的尊重，但他和沃森最终都在他们1953年的论文中省略了对她数据的正式引用，并且在诺贝尔奖颁奖典礼上未能适当地承认她的贡献。马克尔强调，如果富兰克林还活着，她很可能会因其贡献而得到认可。文章还揭露了沃森长期存在的种族主义，进一步玷污了他的声誉。

---

## 63. Meilisearch – 提供AI驱动混合搜索的搜索引擎API

**原文标题**: Meilisearch – search engine API bringing AI-powered hybrid search

**原文链接**: [https://github.com/meilisearch/meilisearch](https://github.com/meilisearch/meilisearch)

Meilisearch：一款闪电般快速的开源搜索引擎，旨在轻松集成到应用程序、网站和工作流程中。它开箱即用，提供令人愉悦的搜索体验，具有混合搜索（语义和全文）、即时搜索、拼写容错、过滤/分面搜索、排序、同义词支持和地理搜索等功能。

主要功能包括广泛的语言支持、通过 API 密钥进行的安全管理、用于个性化搜索的多租户以及高度可定制性。它提供 RESTful API、插件和 SDK，以便于集成，并且支持 AI，可与 langchain 和模型上下文协议一起使用。

Meilisearch 易于安装、部署和维护，并提供云选项，以简化服务器管理和额外的功能，例如分析和监控。

该平台提供广泛的文档、高级功能指南以及在各种应用程序（如电子商务、电影流媒体和 SaaS）中的使用示例。Meilisearch 还会收集匿名用户数据以改进产品，但可以停用此功能，并提供用户请求删除数据的方式。该公司鼓励通过贡献、错误报告、功能请求及其 Discord 社区参与社区活动。版本发布和二进制文件均遵循 SemVer 约定。

---

## 64. 谷歌搜索将把其国家/地区顶级域名重定向至Google.com

**原文标题**: Google Search to redirect its country level TLDs to Google.com

**原文链接**: [https://searchengineland.com/google-search-to-redirect-its-country-level-tlds-to-google-com-454289](https://searchengineland.com/google-search-to-redirect-its-country-level-tlds-to-google-com-454289)

谷歌搜索将开始把用户从其国家代码顶级域名(ccTLD)，例如google.fr和google.ng，重定向到主域名Google.com。这项变更将在未来几个月内逐步推出。

谷歌表示，这是由于改进了提供本地化搜索结果的能力，无论使用哪个域名。他们认为ccTLD对于提供本地体验不再必要。

预计对大多数用户的影响将是最小的。用户可能需要在重定向后重新登录Google并重新配置搜索设置。谷歌强调，此更改影响浏览器地址栏，但不影响搜索的工作方式或他们如何处理国家法律义务。

Search Engine Land认为，短期内可能在引荐流量和登录体验方面存在细微差异。但是，预计不会有其他重大变化。

---

## 65. FPGA中的W65C832

**原文标题**: W65C832 in an FPGA

**原文链接**: [https://www.mikekohn.net/micro/w65c832_fpga.php](https://www.mikekohn.net/micro/w65c832_fpga.php)

Michael Kohn 在 FPGA 中实现了一个 W65C832 的 Verilog 版本，它是 6502 CPU 的 32 位版本。W65C832 核心利用 FPGA 内部少量块 RAM 作为 4KB 的 RAM、4KB 的 ROM，以及 4KB 页面来与 Winbond W25Q128J 闪存芯片 (16MB) 接口。指令集可以访问 16MB 的 RAM。Verilog 代码可在 GitHub 上获取，并使用开源 FPGA 工具构建。Joe Davisson 通过调试核心并创建一个带有 XMODEM 引导加载程序的图形演示来贡献力量，用于程序上传。

W65C832 具有 A、X 和 Y 寄存器，它们可以是 8 位、16 位或 32 位，以及 SP、PC、DR、DRB 和 PRB 寄存器。CPU 在不同的模式下运行，可以通过 XCE 指令选择，从而影响 A、X 和 Y 寄存器的大小。

FPGA 实现使用 Winbond W25Q128 闪存芯片进行扩展的 ROM 存储，根据需要将 4KB 的块分页到 RAM 中。CH341A 编程器和 flashrom 用于对闪存进行编程。

存储器映射包括 RAM、ROM、外围设备和闪存。外围设备包括按钮输入、SPI、UART 和输出引脚。UART 允许程序上传，而无需重新编程 FPGA。

作者讨论了使用寄存器模式的挑战以及编码过程中潜在的陷阱，尤其是在立即数值和状态寄存器操作方面。此核心与 W65C832 规范之间仍然存在一些差异，例如缺少指令时序和未实现的十进制模式。作者提出了一种受 Intel x86 基于前缀的指令启发的 32 位 6502 设计的替代方法，这可能会简化反汇编并减少寄存器大小错误。

---

## 66. 审查者忽略未加密的HTTP/2流量 (2024)

**原文标题**: Censors Ignore Unencrypted HTTP/2 Traffic (2024)

**原文链接**: [https://upb-syssec.github.io/blog/2024/http2/](https://upb-syssec.github.io/blog/2024/http2/)

此2024年博客文章揭示，尽管中国和伊朗积极审查未加密的HTTP/1.1流量，但未加密的HTTP/2流量目前在这两国未受审查。作者通过使用HTTP/2成功访问了在HTTP/1.1下被屏蔽的网站发现了这一点。

这种规避审查的关键原因似乎是HTTP/2的二进制格式，与基于文本的HTTP/1.1相比，这使得审查者更难以解析。此外，HTTP/2主要为加密的HTTPS连接而设计，导致浏览器中缺乏未加密的HTTP/2实现，并可能减少审查者的审查。

虽然没有主流浏览器支持未加密的HTTP/2，但作者发现高达6.28%的网站，特别是较小和受审查的域名，支持它。他们分析了Tranco排名前一百万的网站以及CitizenLab在中国和伊朗审查网站列表中的支持情况。

研究人员提供了一个名为“Does-It-Support-Unencrypted-Http”的工具，以帮助评估网站对未加密HTTP的支持。他们建议，HTTP更新代理可以通过在HTTP/1.1和HTTP/2之间进行转换来促进基于浏览器的规避审查。

作者警告说，未加密的HTTP/2 *不*提供隐私，不应用于传输敏感数据。虽然对HTTP/2的支持总体较低，但作者认为，这种方法可用于访问其他被阻止的网站，并增加了审查规避技术的手段。

---

## 67. 枯树能锁住大量碳，减少大气排放

**原文标题**: Dead trees keep surprisingly large amounts of carbon out of atmosphere

**原文链接**: [https://phys.org/news/2025-03-dead-trees-large-amounts-carbon.html](https://phys.org/news/2025-03-dead-trees-large-amounts-carbon.html)

佛蒙特大学文章：溪流中枯木的重要碳汇作用。研究人员发现，溪流中尤其是原始森林中的大型倒木储存了惊人的碳量，超过了森林地面上的倒木储碳量。原始森林中溪流木材的储碳量是成熟森林的四到五倍。这种碳储存归功于大型木材缓慢的分解速度，尤其是在浸没时。这些木材还起到水坝的作用，积累更多的有机物质，从而增强了它们的碳储存作用。

这项在哈伯德布鲁克实验森林和阿迪朗达克州立公园进行的研究测量了源头溪流中木材储存的碳量。研究人员发现，向原始森林条件发展的森林比通过分解损失的木材积累了更多的溪流木材，其中大型树木发挥了至关重要的作用。预计这种积累将随着成熟森林从过去的清理中恢复而继续，从而导致碳储存量大幅增加。

该研究强调了考虑溪流和森林之间动态关系对于准确碳建模的重要性。它还强调了佛蒙特州土地所有者将碳储存策略纳入其土地利用计划的潜力，从而为自然气候解决方案做出贡献。这些发现量化了一种以前被忽视的碳储存机制，为理解和管理森林生态系统以缓解气候变化提供了宝贵的见解。

---

## 68. 使用差分隐私理解苹果智能的聚合趋势

**原文标题**: Understanding Aggregate Trends for Apple Intelligence Using Differential Privacy

**原文链接**: [https://machinelearning.apple.com/research/differential-privacy-aggregate-trends](https://machinelearning.apple.com/research/differential-privacy-aggregate-trends)

苹果公司通过差分隐私和合成数据生成等技术，在提升Apple智能功能的同时，坚持保护用户隐私。

**要点：**

*   **隐私承诺：** 苹果强调其对用户隐私的承诺是一项基本权利。
*   **Genmoji的差分隐私：** 对于选择加入设备分析的用户，差分隐私用于识别流行的Genmoji提示语，而不会泄露个人用户数据。 这包括随机轮询设备以获取带有噪声信号的提示语片段，确保可以发现常见的提示语，同时保护独特的提示语和用户身份。
*   **文本生成的合成数据：** 对于诸如摘要和写作工具之类的功能，苹果使用合成数据来了解较长文本格式的趋势，而无需收集用户内容。
*   **合成电子邮件生成：** 他们创建代表真实用户数据的合成电子邮件，使用LLM生成涵盖常见主题的电子邮件。 这些合成消息的嵌入与设备上用户电子邮件样本的嵌入进行比较（无需与Apple共享电子邮件内容）。
*   **聚合趋势学习：** 通过使用差分隐私，Apple可以学习所有设备上最常选择的合成嵌入，这些嵌入代表聚合趋势。 这些用于改进文本生成模型的训练数据。
*   **合成数据的隐私保护：** 此过程确保没有用户电子邮件内容离开设备，并且Apple仅收到有关合成嵌入选择的汇总统计信息。 将噪声添加到信号中，进一步保护个人数据。
*   **应用扩展：** 差分隐私和合成数据方法还将用于改进Apple智能中的图像游乐场、图像魔棒、回忆创建和写作工具，以及视觉智能。

---

## 69. 马里奥·巴尔加斯·略萨去世

**原文标题**: Mario Vargas Llosa has died

**原文链接**: [https://www.nytimes.com/2025/04/13/books/review/mario-vargas-llosa-appraisal.html](https://www.nytimes.com/2025/04/13/books/review/mario-vargas-llosa-appraisal.html)

文章报道秘鲁作家马里奥·巴尔加斯·略萨逝世，享年89岁。文章着重指出著名文学评论家约翰·厄普代克对将巴尔加斯·略萨的作品介绍给北美读者的重大影响。厄普代克称赞巴尔加斯·略萨的智慧、多才多艺和想象力，并指出他能够生动地描绘各种人物和情境。

厄普代克宣称，巴尔加斯·略萨已经超越加西亚·马尔克斯，成为北美读者应该发现的南美小说家。文章提到巴尔加斯·略萨的一些主要作品，包括《城市与狗》、《绿房子》、《酒吧长谈》和《世界末日之战》，这些作品赢得了全球受众，但最初在美国的普及速度较慢。

巴尔加斯·略萨是拉丁美洲文学爆炸的关键人物，这是一场由具有社会意识和实验精神的作家组成的文学运动，其中包括加西亚·马尔克斯、卡洛斯·富恩特斯和胡里奥·科塔萨尔。

---

## 70. 关税：一个对Python导入征收关税的Python包

**原文标题**: Tariff: A Python package that imposes tariffs on Python imports

**原文链接**: [https://pypi.org/project/tariff/](https://pypi.org/project/tariff/)

本文描述了一个名为"Tariff"的Python包，该包旨在对Python导入施加"关税"。然而，由于内容缺失以及错误消息表明JavaScript问题阻止页面正确加载，关于该包功能的实际可用信息非常少。

根据标题，"Tariff"包的主要功能可能是控制或限制Python导入，隐喻性地对它们的使用施加"关税"（可能是费用或惩罚）。其预期目的可能是：

*   **控制依赖项：** 限制或规范项目中使用特定库或模块。
*   **跟踪导入成本：** 衡量或收取使用某些导入的费用，可能用于大型组织中的账单或会计目的。
*   **执行策略：** 确保遵守与依赖项相关的编码标准或许可要求。
*   **实验性：** 该工具可能旨在作为一种实验性功能、玩笑或一种新颖的包管理方法。

但是，如果没有完整的文章内容，就无法更深入地解释该软件包的功能、用法或动机。错误消息突出了阻止页面完全加载的问题，因此很难理解该软件包的详细信息。

---

## 71. ISP和骚扰电话者喜欢FCC尽可能“删除”更多规则的计划

**原文标题**: ISPs and robocallers love the FCC plan to "delete" as many rules as possible

**原文链接**: [https://arstechnica.com/tech-policy/2025/04/isps-and-robocallers-love-the-fcc-plan-to-delete-as-many-rules-as-possible/](https://arstechnica.com/tech-policy/2025/04/isps-and-robocallers-love-the-fcc-plan-to-delete-as-many-rules-as-possible/)

在布伦丹·卡尔主席的“删除、删除、删除”倡议下，联邦通信委员会（FCC）正寻求取消监管，促使行业团体提交解除管制愿望清单。互联网服务提供商（ISP）和骚扰电话拨打者都在倡导减少规则。

像AT&T和Verizon这样的ISP希望放松对维护旧网络的监管，并停止可能导致经济处罚的执法程序。Verizon还寻求延长手机锁定在其网络的时间，以打击欺诈。有线电视和电信游说团体正在推动取消要求电视服务采用“全包”定价的规则。

代表收债人和药房的团体希望放宽骚扰电话同意规则，认为目前的法规损害了消费者。相反，美国广播电视协会寻求结束联邦通信委员会的新闻扭曲政策，同时要求放宽所有权和许可规则。

SpaceX和亚马逊的Kuiper正在倡导卫星解除管制。监狱电话公司Securus正在寻求修改降低监狱电话费用的规则，并取消对“附加”费用的禁令。

虽然有些人主张迅速行动，但包括联邦通信委员会委员Anna Gomez在内的其他人则敦促采取更谨慎的方式，以避免法律挑战并确保消费者保护。争论的焦点在于在解除管制过程中是使用“手术刀”还是“电锯”。

---

## 72. 异想天开的投资者

**原文标题**: The Whimsical Investor

**原文链接**: [https://fi-le.net/stonks/](https://fi-le.net/stonks/)

奇想投资者

本文赞扬了小型、古怪且公开交易的公司，这些公司在今天的市场上日益减少。作者寻找其中“最愚蠢”的公司，重点介绍了具有独特特征和可爱的怪癖的企业。

本文介绍了五家公司：

*   **Schwälbchen Molkerei Jakob Berz AG：** 一家德国乳品公司，拥有迷人的标志和令人惊讶的多元化产品线，包括自制酸奶饮料和一款令人质疑的黑森奶酪酱。
*   **日本一软件公司：** 一家日本游戏发行商，拥有可爱的企鹅吉祥物（普利尼）和浮夸的年度报告。他们的游戏策略围绕着《魔界战记》系列和一系列移动应用程序展开。
*   **英格堡-特吕布湖-铁力士山缆车公司：** 一家瑞士山地缆车公司，拥有悠久的历史，并且对通过旅游和基础设施创造价值有着深刻的理解。
*   **株式会社不二家：** 一家标志性的日本糖果制造商，以其吉祥物Peko-chan和各种糖果、餐厅和商品而闻名。他们声称在日本推出了第一款圣诞蛋糕。
*   **智冠科技股份有限公司：** 一家台湾视频游戏公司，拥有复杂、垂直整合的结构和庞大的游戏目录。

最终，**智冠科技股份有限公司** 因其雄心勃勃地试图在其小型组织内涵盖整个视频游戏价值链而被评为“最愚蠢的上市公司”。

文章最后对上市公司数量的减少以及可能失去获得投资回报和信息的途径表示担忧，并敦促在私营企业和公共企业之间取得平衡。

---

## 73. 美国低估了制造业回流的难度

**原文标题**: America Underestimates the Difficulty of Bringing Manufacturing Back

**原文链接**: [https://www.molsonhart.com/blog/america-underestimates-the-difficulty-of-bringing-manufacturing-back](https://www.molsonhart.com/blog/america-underestimates-the-difficulty-of-bringing-manufacturing-back)

莫尔森·哈特认为，近期美国为重振制造业而对进口商品征收的关税注定会失败。他结合自己在制造业15年的经验（包括在中国的工作经历），提出了14个理由。

核心原因包括：关税不足以抵消美国本土制造业的更高成本；美国的工业供应链薄弱，缺乏必要的零部件供应商；美国已经失去了生产某些产品的技术；美国的实际劳动力成本高于表面，原因不仅在于工资，还包括职业道德和技能；美国缺乏支持制造业繁荣的基础设施（电力、道路）；以及建立美国制造业所需的时间过长。

哈特还强调了关税的不确定性和复杂性，这冻结了商业活动。他认为，大多数美国人不喜欢从事制造业，而且美国劳动力缺乏竞争所需的技能。

本质上，他认为将制造业带回美国所面临的挑战远比征收关税复杂得多。他强调需要采取整体方法，解决技能、基础设施、供应链和支持制造业的职业文化问题。如果缺乏这些根本性的改变，关税很可能会适得其反，损害美国经济。

---

## 74. GitHub Copilot、Cursor 新漏洞：黑客可利用代码助手发动攻击

**原文标题**: New Vulnerability in GitHub Copilot, Cursor: Hackers Can Weaponize Code Agents

**原文链接**: [https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents](https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents)

Pillar Security研究人员发现了一种名为“规则文件后门”的新型供应链攻击，该攻击利用GitHub Copilot和Cursor等AI编码助手。攻击者将恶意指令注入到这些工具使用的看似无害的配置文件（规则文件）中，操纵AI生成包含漏洞或后门的代码。

该攻击利用隐藏的Unicode字符和复杂的规避技术来绕过代码审查和人工监督。一旦受感染的规则文件被纳入项目中，它将影响所有未来的代码生成，可能会将漏洞传播到下游依赖项和最终用户。

文章详细介绍了攻击者如何使用上下文操纵、Unicode混淆和语义劫持来微妙地影响AI的代码生成。一个真实的演示展示了如何使用恶意规则文件将来自攻击者控制站点的脚本标签注入到由Cursor生成的简单HTML页面中，而AI从未在其响应中提及该添加。在GitHub Copilot环境中也演示了类似攻击流程。

缓解策略包括审计规则文件中的恶意指令、实施AI配置文件的验证流程、部署检测工具以及仔细审查AI生成的代码。Pillar Security已负责任地向Cursor和GitHub披露了该漏洞，但两家公司均表示，用户有责任审查AI生成的建议。文章强调需要发展安全模型，以应对基于AI的操纵，并将AI本身作为攻击面的一部分进行保护。

---

## 75. Janet的PEG模块工作原理

**原文标题**: How Janet's PEG module works

**原文链接**: [https://bakpakin.com/writing/how-janets-peg-works.html](https://bakpakin.com/writing/how-janets-peg-works.html)

本文解释了Janet的PEG（解析表达式文法）模块的工作原理，重点在于实现而非使用。作者详细介绍了一个使用Janet核心数据结构构建的简化PEG引擎，并强调其可移植到其他语言的特性。

文章首先概述了PEG，强调了有序选择运算符(+)及其确定性，并将其与传统的解析器生成器进行了对比。关键的PEG运算符包括字符串字面量、选择、序列(*)和布尔反转(!)。

解释的核心是一个简单的`match-peg`函数，该函数递归地将规则与字符串进行匹配。该函数最初没有可变参数运算符或递归，然后对其进行增强。首先，运算符变为可变参数，以实现更自然的语法。接下来，使用将关键字映射到PEG表达式的文法表引入递归，从而允许复杂、递归的文法。

最后，文章描述了如何通过简单地向`match-peg`函数的主要匹配表达式添加case来向PEG引擎添加新规则，例如字符类和可选匹配。演示了一个`:set`运算符，该运算符检查字符是否存在于集合中。

作者承认简化的`match-peg`实现存在局限性，例如缺乏捕获、优化和尾调用优化，但强调它为理解通用模式匹配提供了一个良好的基础。

---

## 76. SSD1306显示驱动及字体渲染

**原文标题**: SSD1306 display drivers and font rendering

**原文链接**: [https://subalpinecircuits.com/ssd1306-and-font-rendering/](https://subalpinecircuits.com/ssd1306-and-font-rendering/)

本文详细介绍了作者为ESP32项目寻找合适的SSD1306显示驱动程序的经历，旨在平衡速度和字体支持。最初，他们使用了乐鑫提供的快速但单字体驱动程序，该程序后来被弃用。随后，作者探索了以下几种替代方案：

*   **LVGL：** 一个完整的图形栈，支持字体，但速度太慢 (18-20 Hz) 且资源密集。
*   **U8G2：** 一个流行的库，包含许多字体，但速度也很慢 (约 18 Hz)。
*   **另一个SSD1306驱动程序：** 声称速度快并支持BDF字体，但存在字距调整问题且资源使用率高。
*   **AdafruitGFX：** 考虑过，但由于需要Arduino兼容层而被拒绝。

受挫之下，作者恢复使用了最初的快速乐鑫驱动程序，并将其更新到当前的ESP-IDF I2C API。为了增加字体支持，他们集成了 `nvbdflib`，一个BDF字体解析库。这使他们能够使用自定义绘图函数直接将字体渲染到帧缓冲区，而无需中间位图。作者将精简的 8x16 IBM VGA 字体 (10KB) 直接加载到内存中，认为这是增加字体便捷性的一种良好权衡，无需编译步骤。最终解决方案实现了快速刷新率 (40 Hz)，并具有灵活的BDF字体支持、现代I2C API且没有重大依赖项。

---

## 77. 展示HN：用Cosmopolitan复活Infocom的Unix Z-Machine

**原文标题**: Show HN: Resurrecting Infocom's Unix Z-Machine with Cosmopolitan

**原文链接**: [https://christopherdrum.github.io/posts/2025/04/porting-infocom-with-cosmo](https://christopherdrum.github.io/posts/2025/04/porting-infocom-with-cosmo)

这个“Show HN”帖子详细介绍了作者使用 Cosmopolitan 将 Infocom 原始 UNIX Z-Machine（Zork 和其他文字冒险游戏的虚拟机）移植到单个独立可执行文件的经验。Cosmopolitan 是一种工具，可以将 C 代码编译成“真正可移植的可执行文件”(APE)，无需虚拟机或单独构建，即可在多个操作系统（Windows、Mac、Linux、BSD）和架构（x86、ARM）上原生运行。

作者的动机是探索 Infocom 的历史以及 Cosmopolitan 的潜力。他们将 Z-Machine 的历史描述为一种跨多个系统交付游戏的平台无关方式。他们选择了 C 版本的解释器，而不是汇编语言。

移植过程包括将 1985 年的 K&R 风格的 C 代码适配到现代标准，特别是解决与 NULL 定义、函数声明和已弃用的系统调用相关的问题。必要的修复相对较小，主要集中在标准化 NULL 定义、现代化函数头以及将较旧的函数调用（如 `sys/termio.h`）替换为 `termios.h`。

生成的 APE 文件易于分发和运行。作者还解释了如何将游戏的 .z3 数据文件直接嵌入到 APE 可执行文件中，从而创建一个自包含的单文件发行版。他们最后提供了处理类似项目的建议，强调了对主题熟悉度和解决编译器错误的系统性方法的重要性。最终得到的可执行文件无需额外设置即可在多个系统上运行。

---

## 78. Cure ID App让临床医生报告现有药物的新用途

**原文标题**: Cure ID App Lets Clinicians Report Novel Uses of Existing Drugs

**原文链接**: [https://www.fda.gov/drugs/science-and-research-drugs/cure-id-app-lets-clinicians-report-novel-uses-existing-drugs](https://www.fda.gov/drugs/science-and-research-drugs/cure-id-app-lets-clinicians-report-novel-uses-existing-drugs)

以下是基于标题的文章摘要：

FDA的文章讨论了Cure ID应用程序，该平台旨在允许临床医生报告现有药物的新用途，特别是针对难以治疗的传染病。 Cure ID的核心功能是从世界各地的医生那里众包信息，了解他们如何以非常规的方式或“超适应症”使用已批准的药物来治疗标准治疗失败或不可用的疾病。

该应用程序旨在通过提供真实临床经验的中央数据库来弥补治疗罕见和新出现的传染病方面的知识差距。 临床医生可以输入详细的病例报告，包括患者人口统计学、诊断、治疗方案和结果。 然后，其他面临类似挑战的临床医生可以使用这些共享数据来指导他们的治疗决策。

Cure ID的益处包括加速识别可能对挑战性感染有效的治疗方法、为进一步研究和临床试验产生假设，以及可能导致现有药物用于新的适应症。 通过收集和传播这些信息，FDA希望促进更快地获得可能挽救生命的治疗方法，尤其是在时间紧迫的情况下。 该应用程序还可以促进全球医疗保健专业人员之间的协作和知识共享，从而能够对新兴健康威胁做出更协调的响应。

---

## 79. 将Luna-Terra崩盘事件研究为一个时序多层图

**原文标题**: Investigating the Luna-Terra Collapse as a Temporal Multilayer Graph

**原文链接**: [https://dl.acm.org/doi/10.1145/3726869](https://dl.acm.org/doi/10.1145/3726869)

无法访问文章链接。

---

## 80. 万倍速，万倍简

**原文标题**: 10k Times Faster, 10k Times Simpler

**原文链接**: [https://tailscale.com/blog/10000-times-faster](https://tailscale.com/blog/10000-times-faster)

Avery Pennarun 的文章《快一万倍，简单一万倍》指出，现代软件开发常常过度设计解决方案，模仿谷歌等科技巨头的复杂分布式架构，尽管硬件性能已大幅提升。Pennarun 认为，包括智能手机和云计算在内的当今现成硬件，远远超过了 15 年前的计算能力，因此对于大多数企业来说，互联网规模的复杂性是不必要的。

该文章倡导一种转向简单的范式转变，敦促开发人员通过边缘计算等方法来利用现代设备的强大功能。通过在设备本地处理数据，可以减少延迟，最小化带宽使用，并提高可靠性。Pennarun 强调，扩展应侧重于当前用户需求，而不是假设的未来增长，建议开发人员评估硬件能力，优先考虑可维护性，并利用现代库和工具，避免重复发明轮子。中心思想是，开发人员应抓住机会构建优雅而强大的系统，以反映现代技术带来的简洁性，避免“过度设计陷阱”及其相关的脆弱性、调试挑战和增加的运营成本。

---

## 81. MCP的种种问题

**原文标题**: Everything wrong with MCP

**原文链接**: [https://blog.sshh.io/p/everything-wrong-with-mcp](https://blog.sshh.io/p/everything-wrong-with-mcp)

本文探讨模型上下文协议 (MCP)，这是一个快速发展的标准，用于将第三方数据和工具与 LLM 驱动的助手集成。虽然 MCP 通过连接文件访问和任务执行等工具来简化上下文提供和代理自主性，但它也在安全性、UI/UX 和 LLM 可靠性方面存在漏洞和局限性。

作者重点介绍了协议安全问题，包括缺乏初始身份验证规范、在本地运行恶意代码的风险，以及服务器通常信任输入导致潜在的漏洞利用。UI/UX 局限性包括缺少工具风险等级，这可能导致意外的不可逆操作以及缺乏带宽使用成本控制。非结构化文本传输也可能在需要丰富的界面或异步更新时引起问题。

本文深入探讨了 LLM 安全风险，强调了提示注入的潜力，包括直接注入和通过受信任的第三方服务器进行的“第四方”注入。这可能会通过看似良性的工具暴露敏感数据或劫持工具请求。作者还指出，MCP 结合数据聚合能力，即使代理与用户具有相同的访问权限，也允许用户导出敏感材料。最后，本文承认 LLM 的局限性可能会夸大 MCP 集成的承诺，因为 LLM 的可靠性通常会随着更多指令性上下文而降低。

---

## 82. 如何编写Git提交信息（2014）

**原文标题**: How to write a Git commit message (2014)

**原文链接**: [https://cbea.ms/git-commit/](https://cbea.ms/git-commit/)

这篇2014年的文章强调了精心编写Git提交信息对于项目可维护性和协作的重要性。 它强调清晰一致的提交历史有助于理解代码更改、提高Git工具的效率，并有助于代码审查。

文章概述了编写有效提交信息的七个规则：

1.  **主题与正文之间用空行分隔：** 这是Git工具使用的区分方式。
2.  **将主题行限制在50个字符以内：** 提高简洁性和可读性。
3.  **主题行首字母大写：** 确保一致性。
4.  **主题行末尾不要加句点：** 不必要的标点符号。
5.  **主题行使用祈使语气：** 与Git的内部约定保持一致（例如，“修复错误”、“添加功能”）。
6.  **正文在72个字符处换行：** 适应Git的缩进并防止出现长行。
7.  **使用正文来解释原因和目的，而不是方法：** 重点关注解决的问题和更改背后的理由，而不是实现细节。

作者认为，遵守这些约定可以创建更具可读性和实用性的提交历史，最终使整个开发团队受益。他们将其比作遵守编程语言的代码风格指南，以确保项目的一致性和可维护性。

---

## 83. Show HN: ClipCapsule – 一款Linux剪贴板管理器 (使用Go和Wails构建)

**原文标题**: Show HN: ClipCapsule – A Clipboard Manager for Linux (Built with Go and Wails)

**原文链接**: [https://github.com/Victor-Evogor/clipcapsule](https://github.com/Victor-Evogor/clipcapsule)

ClipCapsule：一款使用 Go 和 WailsJS 构建的 Linux 键盘驱动剪贴板管理器。它旨在通过使用键盘快捷键 (CTRL + SHIFT + 1-9) 快速切换剪贴板条目来提高生产力，无需鼠标或 GUI 交互。该应用程序将剪贴板历史记录存储在本地数据库中，并在选择条目时动态地对其重新排序，确保最近使用的项目始终位于顶部。

目前 ClipCapsule 仍在开发中，需要打开 GUI 才能使快捷键生效，但开发人员正在积极开发后台守护程序。安装过程包括克隆存储库、安装 Wails 以及使用提升的权限构建应用程序，因为需要访问键盘输入。或者，用户可以授予对键盘输入设备路径的访问权限。

主要功能包括键盘优先的工作流程、剪贴板历史记录、动态重新排序和仅本地数据存储。技术栈包括 Go、Wails 和 X11 输入（通过原始设备读取）。路线图包括守护进程模式、托盘图标和首选项、可配置的快捷键、剪贴板预览 UI 以及排除敏感条目的功能。欢迎在 MIT 许可证下进行贡献和报告错误。一个已知的问题是需要提升的权限或手动键盘输入访问才能使应用程序正常运行。

---

## 84. 科学家：蛋白质IL-17抵抗感染，作用于大脑，诱发焦虑

**原文标题**: Scientists: Protein IL-17 fights infection, acts on the brain, inducing anxiety

**原文链接**: [https://medicalxpress.com/news/2025-04-scientists-protein-il-infection-brain.html](https://medicalxpress.com/news/2025-04-scientists-protein-il-infection-brain.html)

IL-17的双重作用：感染防御与行为调控

---

## 85. Kmart欺骗了我，所以我黑了他们的灯。

**原文标题**: Kmart lied to me, so I hacked their lamp

**原文链接**: [https://www.youtube.com/watch?v=E_6Y1iip3p0](https://www.youtube.com/watch?v=E_6Y1iip3p0)

此文章标题声称“凯马特欺骗了我，所以我黑了他们的灯”。然而，实际内容只是一个标准的YouTube页脚，显示版权信息、联系方式、服务条款和Google LLC的版权声明。这意味着提供的内容与标题毫无关联。这似乎要么是一个误导性的标题，要么是文章内容缺失的错误。

---

## 86. 变压器实验室

**原文标题**: Transformer Lab

**原文链接**: [https://transformerlab.ai/](https://transformerlab.ai/)

无法访问文章链接。

---

## 87. CT扫描可能导致5%的癌症，研究发现；专家指出存在不确定性

**原文标题**: CT scans could cause 5% of cancers, study finds; experts note uncertainty

**原文链接**: [https://arstechnica.com/health/2025/04/ct-scans-could-cause-5-of-cancers-study-finds-experts-note-uncertainty/](https://arstechnica.com/health/2025/04/ct-scans-could-cause-5-of-cancers-study-finds-experts-note-uncertainty/)

《美国医学会内科学》杂志最近的一项研究估计，CT扫描虽然对诊断至关重要，但由于辐射暴露，可能导致未来5%的癌症。研究人员分析了2023年进行的9300万次CT扫描的数据，预测约有103,000例未来的癌症与扫描有关，其风险与饮酒和肥胖相当。肺癌和结肠癌通常来自腹部和盆腔CT扫描，被认为是*常见的类型。

该研究的作者敦促医生谨慎使用CT扫描，在权衡风险和收益的同时，优化剂量，特别是考虑到自2007年以来CT扫描使用量增加了35%。然而，外部专家强调建模的不确定性，该建模将成年人的风险从原子弹幸存者和职业暴露的研究中推断出来。虽然一些研究将年轻人CT扫描与血液和脑癌联系起来，但成年人的总体风险似乎很小，每次CT扫描仅将终生癌症风险增加0.1%，而基线风险为40%。

专家们一致认为，必要CT扫描的诊断益处通常大于*小的癌症风险。尽管如此，CT扫描使用量的增加引起了人们的担忧。随附的评论建议采用诊断算法，考虑替代成像方案，如超声波和核磁共振成像，并让患者参与决策过程，以减少低价值的测试。重点是教育临床医生，以促进CT扫描使用的更平衡的方法。

---

## 88. Show HN: C++17单头文件性能分析器

**原文标题**: Show HN: Single-Header Profiler for C++17

**原文链接**: [https://github.com/DmitriBogdanov/UTL/blob/master/docs/module_profiler.md](https://github.com/DmitriBogdanov/UTL/blob/master/docs/module_profiler.md)

“Show HN”：`utl::profiler`，用于局部代码性能分析的单头文件C++17库。它使用简单的宏来测量代码段所花费的时间，构建调用图并提供每个线程的格式化输出。主要功能包括易于使用、低开销、不依赖于系统API、多线程、递归支持、CPU计数器时间戳、可导出结果和禁用选项。

该性能分析器使用诸如`UTL_PROFILER_SCOPE`、`UTL_PROFILER`、`UTL_PROFILER_BEGIN`和`UTL_PROFILER_END`之类的宏来标记代码区域。它提供了一个`Style`结构体，用于自定义输出格式（缩进、颜色、截止百分比）。全局`profiler`对象提供了用于在退出时打印结果、上传线程数据和格式化输出的方法。

该文章通过示例演示了其用法，包括性能分析代码段、递归、并行部分、分离线程和使用文件导出的自定义样式。 它强调通过使用`UTL_PROFILER_USE_INTRINSICS_FOR_FREQUENCY`宏来使用x86内在函数来降低开销，并显示了基准测试结果。 可以使用`UTL_PROFILER_DISABLE`禁用性能分析。 该库的内部调用图实现使用线程局部变量和整数ID来优化性能。 内存使用量取决于调用图的大小，但可以使用`UTL_PROFILER_USE_SMALL_IDS`减少。 该库是线程安全的，仅在线程创建、加入和手动结果上传期间使用锁。

---

## 89. 数据的关系模型 (1969)

**原文标题**: A Relational Model of Data (1969)

**原文链接**: [https://dl.acm.org/doi/pdf/10.1145/362384.362685](https://dl.acm.org/doi/pdf/10.1145/362384.362685)

好的，我将根据我对E.F. Codd的《大型共享数据库的关系数据模型》一文的广泛认知内容，提供一份摘要。

**《数据的关系模型 (1969)》摘要**

E.F. Codd的开创性论文《大型共享数据库的关系数据模型》提出了一种基于数学关系的新型数据管理方法。它提出了关系模型，旨在克服现有分层和网络模型的局限性，从而在大型共享数据库中表示和操作数据。

其核心思想是将数据表示为关系的集合（表），其中每个关系都有一组属性（列）和元组（行）。该论文定义了诸如域（属性的允许值集合）、主键（元组的唯一标识符）和外键（连接关系）等关键概念。数据通过关系代数访问和操作，关系代数是一组允许强大而灵活的查询和数据转换的操作（例如，选择、投影、连接）。

Codd认为，关系模型具有几个优点，包括数据独立性（应用程序与物理存储细节隔离）、简单性（数据以清晰直观的方式组织）以及数据完整性和一致性的健全理论基础。它强调规范化的重要性，规范化是分解关系以消除数据冗余和更新异常的过程。

该论文为关系数据库管理系统（RDBMS）奠定了基础，RDBMS成为数据库技术的主导范例。它引入了一种强大且通用的数据管理方法，对计算机科学领域产生了深远的影响。

---

## 90. Kmart骗了我，所以我黑了他们的灯。

**原文标题**: Kmart lied to me, so I hacked their lamp

**原文链接**: [https://www.youtube.com/watch?v=E_6Y1iip3p0](https://www.youtube.com/watch?v=E_6Y1iip3p0)

本文讲述了一位用户在Kmart的购物体验。该用户声称Kmart对其撒谎，导致其不得不采取行动，“破解”了从该商店购买的灯。虽然谎言的具体内容和破解的性质没有详细说明，但标题清楚地表明了在Kmart的负面体验促使了报复行为。然而，提供的内容突然转变为标准的YouTube免责声明和版权信息。这表明最初的声明可能是YouTube标题或开场白，其后是一个详细描述在Kmart的体验以及随后的灯具破解的视频。YouTube样板文本涵盖了版权、创作者指南、广告、服务条款、隐私以及关于NFL Sunday Ticket的信息等主题。

---

## 91. 研究人员称，AI尚未准备好取代人类程序员进行调试。

**原文标题**: AI isn't ready to replace human coders for debugging, researchers say

**原文链接**: [https://arstechnica.com/ai/2025/04/researchers-find-ai-is-pretty-bad-at-debugging-but-theyre-working-on-it/](https://arstechnica.com/ai/2025/04/researchers-find-ai-is-pretty-bad-at-debugging-but-theyre-working-on-it/)

微软研究表明AI尚无法取代人类程序员进行调试

---

## 92. 股权激励开放指南

**原文标题**: Open guide to equity compensation

**原文链接**: [https://github.com/jlevy/og-equity-compensation](https://github.com/jlevy/og-equity-compensation)

本指南全面概述股权激励，旨在帮助员工、招聘经理、创始人及学生理解其复杂性并做出明智决策。 本指南涵盖美国C类公司中的股权激励，侧重于私营公司，但也有限地涉及上市公司。

本指南解释了股权授予的不同形式，包括限制性股票、股票期权和限制性股票单位(RSU)，并详细说明了每种形式相关的税务影响。 它强调了理解普通所得税、资本利得税和替代性最低税等税务概念的重要性，因为它们会显著影响股权激励的财务结果。

本指南承认股权激励的固有风险，指出员工股权的价值与公司的成功相关，并且可能缺乏流动性或最终变得毫无价值。 本指南还警告了因不明智的决策而可能产生的潜在税务陷阱。 本指南涵盖了各种情况，例如谈判工作邀请、处理裁员或收购期间的股权，以及出售私人股票。

虽然本指南力求实用、周到和简洁，但它不能替代专业建议。 它鼓励读者咨询律师、税务专业人士和薪酬专家以获得个性化指导。 本指南作为雇主和雇员的共享资源，旨在促进公平并防止双方付出高昂代价的错误。

---

## 93. 武士失落之城

**原文标题**: Lost City of the Samurai

**原文链接**: [https://archaeology.org/issues/may-june-2025/features/lost-city-of-the-samurai/](https://archaeology.org/issues/may-june-2025/features/lost-city-of-the-samurai/)

失落的武士之城：探索一乘谷的考古发现。一乘谷曾是繁荣的中世纪日本城市，于1471年至1573年间作为朝仓氏的据点。这座城市被稻田掩埋了几个世纪，于20世纪60年代被重新发现，自此为考古学家提供了一个独特的时间胶囊，深入了解战国时代的生活。

在朝仓氏的统治下，一乘谷在文化和规模上可与京都媲美，成为逃离应仁之乱的难民的避难所，并吸引了艺术家、知识分子和工匠。该市拥有多元化的经济，有金属铸造工、陶工、纺织品染色工，甚至还有一名常驻医生，这得益于连接日本海的贸易路线。

该城市的布局包括武士庄园、防御工事和朝仓氏的宫殿（馆），反映了京都幕府的宏伟。考古发现，包括武器、茶道用具、陶瓷，甚至还有游戏棋子，揭示了武士和平民的生活，展示了即使在地方环境中，高雅文化也很盛行。

一乘谷的全面保存和出土的大量文物（超过170万件）为研究中世纪日本的城市生活提供了前所未有的机会，揭示了当时的社会结构、经济活动和文化习俗。然而，一乘谷的繁荣是短暂的，因为它于1573年被织田信长的军队夷为平地，导致它默默无闻，直到最近被重新发现。

---

## 94. 如何在不采用高铁的情况下，加速美国客运铁路

**原文标题**: How to speed up US passenger rail, without bullet trains

**原文链接**: [https://www.bloomberg.com/news/articles/2025-04-10/how-to-speed-up-us-passenger-rail-without-bullet-trains](https://www.bloomberg.com/news/articles/2025-04-10/how-to-speed-up-us-passenger-rail-without-bullet-trains)

无法访问文章链接。

---

## 95. 实验室首次培育出人类牙齿

**原文标题**: Human teeth grown in a lab for first time

**原文链接**: [https://www.independent.co.uk/news/science/lab-grown-human-teeth-scientists-dentist-b2732534.html](https://www.independent.co.uk/news/science/lab-grown-human-teeth-scientists-dentist-b2732534.html)

伦敦国王学院的科学家们取得了一项突破性进展，成功在实验室中培育出人类牙齿。这项突破为患者提供了再生缺失牙齿的潜力，为补牙和牙种植提供了天然替代方案。该研究团队开发了一种特殊的材料，能够模拟牙齿发育所需的环境，使细胞能够进行交流并启动牙齿形成。

与人工且存在局限性的补牙和牙种植体不同，由患者自身细胞制成的实验室培育牙齿可以无缝地整合到颌骨中，像天然牙齿一样发挥功能并自我修复。研究人员强调，补牙会削弱牙齿结构，而牙种植体需要侵入性手术，而实验室培育的牙齿则提供了一种更耐用、生物相容的解决方案。

研究团队正在探索两种实施途径：要么在实验室中培养完整的牙齿以进行植入，要么将早期牙齿细胞直接放入患者的颌骨中以使其自然发育。虽然之前在实验室中重建牙齿生长的尝试因细胞通讯问题而失败，但这种新方法克服了这一障碍。研究人员认为，这项创新有潜力彻底改变牙科护理，为牙齿修复和再生提供可持续且有效的解决方案。

---

## 96. Show HN: 不确定计算器 – 草稿纸上的概率计算器

**原文标题**: Show HN: Unsure Calculator – back-of-a-napkin probabilistic calculator

**原文链接**: [https://filiph.github.io/unsure/](https://filiph.github.io/unsure/)

Filip Hracek 推出“不确定计算器”，该工具旨在处理以范围（例如 4~6）表示的不确定数字的计算。它通过简化不确定性表示，旨在使更广泛的受众能够进行统计推理。该计算器将范围视为 95% 的置信区间。

Hracek 强调，承认不确定性至关重要，并提供了一个实际例子，说明一个家庭正在考虑在一个新的地方获得工作机会，但存在不确定的财务因素。使用“不确定计算器”，他们可以评估潜在结果的范围，而不是依赖于单个可能具有误导性的数字。

该计算器还支持基本算术以外的其他函数，例如指数、平方根和三角函数。

Hracek 对其局限性坦诚相待：这是一个单人项目，具有脆弱的解析器、缓慢的计算（由于蒙特卡洛方法）、基本的 UI，并假设所有范围都服从正态分布。他强调，它旨在用于快速、粗略的计算，而不是用于复杂的统计分析。

尽管存在局限性，Hracek 希望该工具对评估商业想法、未来收入、投资回报等方面的可行性有所帮助。他鼓励用户在 GitHub 上为该项目做出贡献，并提到还有一个更高级的“笔记本”版本可用。他经常使用该计算器，并发现它对新项目非常有价值。

---

## 97. 削ろう会 #39

**原文标题**: Kezurou-Kai #39

**原文链接**: [https://www.bigsandwoodworking.com/kezurou-kai-39/](https://www.bigsandwoodworking.com/kezurou-kai-39/)

乔恩参加了在日本新泻县糸鱼川市举办的第39届刨薄会，这是一个专注于使用日本刨刀（kanna）获得最薄木屑的日本木工活动。活动包括预备刨削和最终比赛，主要比赛使用扁柏木（宽55毫米，长1800毫米），配70毫米刨刀，决赛使用杉木（日本雪松）。参赛者每天有三次机会提交刨花进行测量，前5名晋级决赛。

乔恩和来自Somakosha的朋友们一起参加了，他们使用了自己的刨刀和数字千分尺。他们很难突破10微米大关，这突出了精细研磨和刨刀台调整的重要性。他注意到木材的质量和含水量对刨花厚度影响很大，参赛者非常注意保持木材的状况，有时会使用湿毛巾来保持湿度。

乔恩最好的刨花测量值为10、6和9微米。最后的挑战是在时间限制下刨削杉木，这是一种比扁柏木更难的木材。获胜的刨花厚度约为50微米。作者指出，虽然超薄刨削令人印象深刻，但它与实际木工相去甚远。他建议比赛应侧重于刨削带有节疤和纹理问题的难刨木材。活动还包括传统工艺的演示，如墨斗雕刻和刨刀台制作，以及销售工具和磨刀石的摊位。他最后建议其他人参加刨薄会或类似的活动，以学习并与木工爱好者交流。

---

## 98. 4chan被黑

**原文标题**: 4chan Hacked

**原文链接**: [https://www.the-sun.com/tech/14029069/4chan-down-updates-controversial-website-hacking/](https://www.the-sun.com/tech/14029069/4chan-down-updates-controversial-website-hacking/)

备受争议的在线留言板4chan于2025年4月15日美国东部时间凌晨4点左右发生重大故障，影响了数千名用户。故障报告激增，Downdetector上记录了超过1200起投诉。

立即出现了关于可能遭受黑客攻击的猜测，用户声称整个4chan数据库已被“转储”。报告表明，首席管理员和版务人员的电子邮件以及聊天记录可能已被泄露。这引发了用户之间的恐慌，他们担心潜在的后果，包括IP地址的暴露。

用户批评该网站代码过时，以及自创始人Christopher "Moot" Poole于2015年离职以来缺乏维护。一些人推测，糟糕的网站格式导致了漏洞。该文章还提醒读者4chan过往的争议历史，特别是2014年“Fappening”事件中泄露的名人亲密照片，包括Jennifer Lawrence的照片。

虽然4chan管理员没有发表官方声明，但该文章继续提供有关情况的实时更新，跟踪用户反应、来自美国和英国Downdetector的报告以及围绕黑客事件的新兴理论。黑客攻击的后果仍然不确定，意见从影响最小到重大事件不等。

---

## 99. Show HN: Tiptap UI 组件 – 用于构建编辑器 UI 的免费 React 组件

**原文标题**: Show HN: Tiptap UI Components – Free React Components for Building Editor UIs

**原文链接**: [https://github.com/ueberdosis/tiptap-ui-components](https://github.com/ueberdosis/tiptap-ui-components)

Tiptap UI 组件是一个免费、MIT 许可的 React 库，旨在加速使用无头 Tiptap 框架开发富文本编辑器 UI。它提供模块化组件、模板和基本元素，使开发者能够快速构建和定制编辑器界面。

主要特性包括：

*   **模块化组件：** 用于常见编辑器功能的独立 React 组件，例如标题、列表、图像上传、链接、文本对齐和撤销/重做。
*   **即用型模板：** 功能齐全的编辑器设置，例如提供响应式布局、“简单编辑器”模板、亮/暗模式支持、富文本格式和可自定义功能。
*   **基本元素：** 诸如按钮、下拉菜单、弹出框和工具提示等基本 UI 元素。
*   **Tiptap CLI：** 一个命令行工具，用于轻松搭建编辑器设置和安装单个组件（“npx @tiptap/cli init”或“npx @tiptap/cli add [component-name]”）。
*   **自定义：** 组件具有最少的样式，以便于集成和自定义，以匹配现有的设计系统。
*   **开源及社区驱动：** 鼓励通过 issue 和 Discord 进行贡献、错误报告和功能建议。

本质上，Tiptap UI 组件提供了一个工具包，可简化富文本编辑器的创建，既提供预构建的组件，又提供根据特定项目需求进行自定义的灵活性。

---

## 100. AMD 预告首款2纳米芯片，EPYC “威尼斯” 采用台积电N2工艺制造

**原文标题**: AMD teases its first 2nm chip, EPYC 'Venice' fabbed on TSMC N2 node

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/amds-first-2nm-chip-is-out-of-the-fab-epyc-venice-fabbed-on-tsmc-n2-node](https://www.tomshardware.com/pc-components/cpus/amds-first-2nm-chip-is-out-of-the-fab-epyc-venice-fabbed-on-tsmc-n2-node)

AMD发布首款2纳米级芯片，预计2026年推出第六代EPYC“威尼斯”处理器

---

