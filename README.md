# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-04-15.md)

*最后自动更新时间: 2025-04-15 17:48:04*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 2 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 3 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 4 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 5 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 6 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 7 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 8 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 9 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 10 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 11 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 12 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 13 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 14 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 15 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 16 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 17 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 18 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 19 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 20 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 21 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 22 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 23 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 24 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 25 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 26 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 27 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
