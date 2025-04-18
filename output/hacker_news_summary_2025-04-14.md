# Hacker News 热门文章摘要 (2025-04-14)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. API中的GPT-4.1

**原文标题**: GPT-4.1 in the API

**原文链接**: [https://openai.com/index/gpt-4-1/](https://openai.com/index/gpt-4-1/)

API中的GPT-4.1标志着OpenAI通过其API提供更新后的GPT-4模型。虽然这次迭代不是一个根本不同的模型（比如GPT-5），但它代表了各个领域的显著改进。

主要改进包括：

*   **更高的可靠性：** 模型表现出更一致和可预测的性能，减少了生成无意义或矛盾回应的情况。
*   **更高的准确性：** GPT-4.1在更广泛的任务中表现出更高的准确性，特别是那些需要复杂推理或细致理解的任务。
*   **更高的安全性：** OpenAI已努力进一步减轻潜在的偏见和有害输出，使模型更安全和更负责任。
*   **扩展的上下文窗口：** 一项重大升级是扩展的上下文窗口（可能达到128k tokens），允许模型处理和保留来自更长输入的更多信息。 这使得分析整本书或处理大量文档等应用程序成为可能。
*   **更低的价格：** 尽管有所改进，OpenAI也降低了输入tokens的价格。

该公告强调，GPT-4 API的现有用户可以轻松访问更新后的模型，通常只需进行极少或无需任何代码更改。 OpenAI鼓励开发者利用增强的功能进行各种应用，从内容创建到复杂问题解决。 此次发布代表了OpenAI持续致力于改进和完善其基础模型，使其对开发者和用户而言更强大、更可靠和更易于访问。

---

## 2. DeepSeek推理引擎开源之路

**原文标题**: The Path to Open-Sourcing the DeepSeek Inference Engine

**原文链接**: [https://github.com/deepseek-ai/open-infra-index/tree/main/OpenSourcing_DeepSeek_Inference_Engine](https://github.com/deepseek-ai/open-infra-index/tree/main/OpenSourcing_DeepSeek_Inference_Engine)

DeepSeek 将其内部推理引擎专业知识回馈开源社区，这源于之前开源贡献的积极反馈以及回馈社会的承诺。 意识到 PyTorch 和 vLLM 等开源项目在其 AI 开发中的关键作用，DeepSeek 旨在促进 DeepSeek-V3 和 DeepSeek-R1 等模型的部署。

DeepSeek 不会直接开源整个引擎，因为这会带来代码分歧、基础设施依赖以及有限的维护带宽等挑战，而是将与现有开源项目合作。 他们的策略包括提取独立的、可重用的功能作为独立的库，并分享设计改进和实施细节。

DeepSeek 强调其对开源运动的感激之情，并致力于为其持续发展做出贡献。 该文章还明确指出，本次公告仅关注推理引擎代码库。 关于未来的模型发布，DeepSeek 承诺从新模型发布的第一天起，积极地将与推理相关的工程工作与开源社区和硬件合作伙伴同步，以确保在各种硬件平台上实现无缝实施。 他们的目标是促进一个同步的生态系统，从而从一开始就为 DeepSeek 模型提供最先进的支持。

---

## 3. 使用单个SQLite表和少量cron任务的可定制AI助手

**原文标题**: A hackable AI assistant using a single SQLite table and a handful of cron jobs

**原文链接**: [https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs](https://www.geoffreylitt.com/2025/04/12/how-i-made-a-useful-ai-assistant-with-one-sqlite-table-and-a-handful-of-cron-jobs)

史蒂文斯是一位由作者构建的个人AI助手，其架构异常简单：一个充当“管家笔记本”的SQLite表格，以及Val.town上的一些定时Cron任务。史蒂文斯通过Telegram向作者及其妻子提供每日简报，包含他们的日历、天气预报、预计邮件和提醒事项。他们也可以随时与史蒂文斯互动。

这个“笔记本”由各种数据导入器填充：每小时从Google Calendar和天气API拉取数据，对美国邮政Informed Delivery电子邮件进行OCR识别，以及接收Telegram/电子邮件消息。这些导入器在SQLite表中添加或编辑“记忆”，这些记忆可以是任何任意文本。

每日简报由一个Cron任务生成，该任务查询SQLite表格以获取相关的日志条目（未来一周的日期条目和未注明日期的背景条目），然后使用Claude API以正式的管家式语气编写更新。

作者强调了超出典型聊天机器人记忆的更广泛背景的重要性，这可以通过整合各种信息来源来实现。他还强调了初始记忆实现的简单性，依赖于直接查询，而不是更复杂的RAG方法。最后，作者谈到使用“氛围编码”为项目添加个性和乐趣，例如赋予史蒂文斯管家角色，并将管理仪表板设计成视频游戏。该代码可供其他人Fork和改编。

---

## 4. Show HN: 从 Protobufs 实现零代码生成、无需编译的 TypeScript 类型推断

**原文标题**: Show HN: Zero-codegen, no-compile TypeScript type inference from Protobufs

**原文链接**: [https://github.com/nathanhleung/protobuf-ts-types](https://github.com/nathanhleung/protobuf-ts-types)

这个“Show HN”帖子介绍了 `protobuf-ts-types`，一个 TypeScript 库，可以直接从 Protobuf 定义中推断类型，无需代码生成或编译。它允许开发者在 `.proto` 文件中定义消息类型，并自动推断相应的 TypeScript 类型，从而简化开发流程。

其核心功能依赖于高级 TypeScript 特性，特别是模板字面量类型，来解析 Protobuf 字符串并提取消息定义。该库提供了 `pbt.infer` 函数，它接受 Protobuf 字符串，可选地还可以接受消息名称作为输入。它返回消息名称到其推断类型的映射，或者返回特定消息的推断类型。

该帖子包含使用示例，演示了如何安装该包，定义 Protobuf 字符串，以及如何使用 `pbt.infer` 来获取 TypeScript 类型。它还强调了其优势，例如 TypeScript 强制执行的类型安全，可防止 Protobuf 定义和 TypeScript 代码之间的不匹配。

该帖子还承认了一些局限性，包括需要 TS 编译器补丁才能导入 `.proto` 文件（等待 TypeScript 更新）、不支持服务、RPC、`oneof` 和 `map` 字段，以及缺少导入功能（目前需要连接）。由于这些限制，该项目被视为一个概念验证，而不是生产就绪。

---

## 5. DolphinGemma：谷歌AI如何助力解码海豚交流

**原文标题**: DolphinGemma: How Google AI is helping decode dolphin communication

**原文链接**: [https://blog.google/technology/ai/dolphingemma/](https://blog.google/technology/ai/dolphingemma/)

本文详细介绍了谷歌与野生海豚项目(WDP)和佐治亚理工学院合作开发DolphinGemma的过程，DolphinGemma是一种旨在解码海豚交流的人工智能模型。几十年来，科学家们一直难以理解海豚使用的复杂咔哒声、口哨声和突发脉冲。WDP长达数十年的长期水下研究，提供了丰富的海豚发声数据集，并配有行为观察，这对于训练人工智能至关重要。

DolphinGemma建立在谷歌的Gemma模型之上，使用专门的音频技术处理海豚声音。它分析声音中的模式，以预测后续发声，类似于大型语言模型预测人类语言中的单词。该模型旨在在Pixel手机上运行，从而能够在现场进行实时分析。

除了分析自然交流，该项目还通过CHAT（鲸类听觉增强遥测）系统探索双向互动。CHAT使用与围巾或海草等物体相关的合成口哨声，旨在与海豚建立共享词汇。研究人员希望海豚能够模仿口哨声来“请求”这些物品。Pixel手机用于CHAT系统中的实时声音分析，从而能够快速响应海豚的发声。

谷歌计划将DolphinGemma作为开放模型共享，以赋能研究各种鲸类物种的研究人员。通过提供先进的人工智能工具，该项目旨在加速发现海豚交流中的模式，并促进对这些智能海洋哺乳动物的更深入理解。最终目标是弥合人类和海豚之间的沟通鸿沟。

---

## 6. 哈萨比斯称谷歌DeepMind将支持Anthropic的MCP用于Gemini及SDK。

**原文标题**: Hassabis Says Google DeepMind to Support Anthropic's MCP for Gemini and SDK

**原文链接**: [https://techcrunch.com/2025/04/09/google-says-itll-embrace-anthropics-standard-for-connecting-ai-models-to-data/](https://techcrunch.com/2025/04/09/google-says-itll-embrace-anthropics-standard-for-connecting-ai-models-to-data/)

谷歌DeepMind将支持Anthropic的Model Context Protocol (MCP)，用于其Gemini模型和SDK，据CEO Demis Hassabis称。 此公告是在OpenAI最近采用相同标准之后发布的，标志着行业互操作性日益增长的趋势。

MCP促进了AI模型与外部数据源之间的连接，使模型能够从业务工具、软件、内容存储库和开发环境中提取信息来完成任务。 它使开发人员能够在这些数据源与聊天机器人等AI驱动的应用程序之间创建双向连接。

该协议利用“MCP服务器”来暴露数据，并利用“MCP客户端”来构建连接到这些服务器的应用程序和工作流程。 自Anthropic开源MCP以来，Block、Apollo、Replit、Codeium和Sourcegraph等公司已将其集成到其平台中。 Hassabis认为MCP正迅速成为AI智能体时代的开放标准，并表示有兴趣进一步合作开发它。 谷歌DeepMind和OpenAI对MCP的采用表明了其成为连接AI模型与其所需数据的广泛使用标准的潜力。

---

## 7. SQLite 文件格式查看器

**原文标题**: SQLite File Format Viewer

**原文链接**: [https://sqlite-internal.pages.dev](https://sqlite-internal.pages.dev)

这篇文章本质上只是一个标题，因此几乎没有什么可总结的。

要点在于，这是关于一个名为“SQLite 文件格式查看器”的工具或应用程序。我们可以推断，该工具旨在让用户检查和理解 SQLite 数据库文件的内部结构和组织。

关键信息（几乎就是全部内容）包括：

*   **主题：**SQLite 数据库文件。
*   **功能：**查看这些文件的内部格式/结构。
*   **目标受众：**可能是需要更深入了解 SQLite 数据库如何组织的开发人员、数据库管理员或取证分析师。

在没有更多内容的情况下，我们只能推测具体功能，例如它是否提供十六进制查看、表格浏览或模式可视化。

---

## 8. 科学家：蛋白质IL-17抵抗感染，作用于大脑，诱发焦虑

**原文标题**: Scientists: Protein IL-17 fights infection, acts on the brain, inducing anxiety

**原文链接**: [https://medicalxpress.com/news/2025-04-scientists-protein-il-infection-brain.html](https://medicalxpress.com/news/2025-04-scientists-protein-il-infection-brain.html)

来自麻省理工学院和哈佛医学院的2025年文章重点介绍了关于细胞因子IL-17及其对大脑双重影响的新研究。科学家们发现IL-17是一种对抵抗感染至关重要的免疫分子，它也能影响大脑功能，从而影响焦虑和社交能力。

该研究表明，IL-17作用于两个不同的大脑区域：杏仁核和体感皮层。在杏仁核，特别是基底外侧杏仁核（BLA），IL-17通过增加某些神经元的兴奋性来促进焦虑。相反，在体感皮层，特别是S1DZ区域，IL-17通过降低神经元的兴奋性来促进社交行为。

研究人员确定了存在于这些大脑区域的特定IL-17受体（IL-17RA、IL-17RB和IL-17RE）以及与它们结合并介导不同行为结果的IL-17变体（IL-17A、IL-17C和IL-17E）。他们还发现，抗炎细胞因子IL-10可以抵消IL-17在杏仁核中引起的焦虑效应。

这些发现表明，免疫系统和神经系统之间的联系比以前认为的更为紧密，IL-17可能作为一种神经调节剂发挥作用。研究人员假设，IL-17的神经调节作用可能在其免疫功能之前就已经进化。该研究表明，操纵免疫系统可能为自闭症或抑郁症等神经系统疾病提供新的治疗方法。

---

## 9. Meilisearch – 具备人工智能混合搜索功能的搜索引擎API

**原文标题**: Meilisearch – search engine API bringing AI-powered hybrid search

**原文链接**: [https://github.com/meilisearch/meilisearch](https://github.com/meilisearch/meilisearch)

Meilisearch是一个快速、开源的搜索引擎，旨在轻松集成到应用程序、网站和工作流程中。它提供混合搜索（语义和全文搜索）、搜索即时显示、容错、过滤/分面搜索、排序、同义词支持和地理搜索等功能。它支持多种语言，并通过API密钥和多租户提供安全管理，以实现个性化的搜索结果。

Meilisearch具有高度可定制性，并提供RESTful API以及适用于各种语言和框架的SDK。它也已为AI做好准备，可与Langchain等工具无缝协作。

该平台提供了丰富的文档和指南，用于入门、高级用法和理解核心概念。Meilisearch Cloud提供具有分析和监控功能的托管部署。

该平台收集匿名用户数据以改进产品，可以选择退出并请求删除数据。Meilisearch团队鼓励社区参与，包括提出功能请求、提交错误报告以及参与其Discord社区。欢迎按照其贡献指南为开源项目做出贡献。

---

## 10. 削ろう会 #39

**原文标题**: Kezurou-Kai #39

**原文链接**: [https://www.bigsandwoodworking.com/kezurou-kai-39/](https://www.bigsandwoodworking.com/kezurou-kai-39/)

乔恩参加了在日本新泻县糸鱼川市举办的第39届削ろう会，这是一项使用日本刨刀比赛，旨在削出尽可能薄的木刨花。活动持续两天，参与者有多次机会提交刨花进行测量。主要比赛是使用70毫米鉋在扁柏木上进行。预备刨削允许参赛者使用自己的材料，而最终比赛则使用主办方提供的木材。

乔恩和他的朋友们从Somakosha一起参加了比赛，最初削出了10-12微米范围内的刨花。挑战在于突破10微米大关，这需要细致的磨刀和刨台调整。官方测量使用气动控制的数字卡尺进行。

第二天，竞争更加激烈，突显了木材质量和水分含量在获得超薄刨花方面的重要性。许多参赛者非常注意保持木材的水分。乔恩的团队尝试了不同的技术，最终发现刨削前稍微润湿木材可以显著改善结果。他最好的刨花测量结果为10、6和9微米。

排名前五的决赛选手随后使用杉木进行比赛，杉木比扁柏木更难刨削。本轮比赛的获胜者获得了大约50微米的刨花。该活动还包括墨壺雕刻、刨台切割、斧劈以及销售工具和磨刀石的商贩的演示。乔恩推荐任何对木工和手工工具有热情的人参加削ろう会。

---

## 11. Show HN: C++17 单头文件性能分析器

**原文标题**: Show HN: Single-Header Profiler for C++17

**原文链接**: [https://github.com/DmitriBogdanov/UTL/blob/master/docs/module_profiler.md](https://github.com/DmitriBogdanov/UTL/blob/master/docs/module_profiler.md)

`utl::profiler` 是一个单头文件、易于使用的 C++17 性能分析解决方案，可帮助测量代码段、作用域或表达式所花费的时间。它自动构建调用图，并呈现格式化的、按线程划分的结果。

主要特性包括低开销、不依赖系统 API、支持多线程和递归、CPU 计数器时间戳，以及可选的结果导出和禁用。它提供诸如 `UTL_PROFILER_SCOPE`、`UTL_PROFILER` 和 `UTL_PROFILER_BEGIN/END` 等宏，以便轻松进行性能分析。输出可以使用可自定义的缩进、颜色和显著/不显著运行时间的截止百分比进行样式化。

该性能分析器使用线程局部变量和整数 ID 来高效构建调用图，并最大限度地减少树遍历期间的开销，这对于小型任务至关重要。您可以通过定义 `UTL_PROFILER_USE_INTRINSICS_FOR_FREQUENCY` 来利用 CPU 计数器内联函数（如 `rdtsc`），从而进一步降低开销。要完全禁用性能分析，请在包含头文件之前定义 `UTL_PROFILER_DISABLE`。

内存开销主要由调用图矩阵决定，可以通过定义 `UTL_PROFILER_USE_SMALL_IDS` 以使用 16 位 ID 来减少。公共 API 是线程安全的，互斥锁仅在线程创建/加入和手动结果上传期间使用。

---

## 12. Janet的PEG模块工作原理

**原文标题**: How Janet's PEG module works

**原文链接**: [https://bakpakin.com/writing/how-janets-peg-works.html](https://bakpakin.com/writing/how-janets-peg-works.html)

本文阐述了Janet的PEG（解析表达式文法）模块的实现方式，着重强调其简洁性和适应性。受REBOL Parse和LPeg的启发，Janet的PEG模块提供了一种通用的文本和字节序列解析方法，因其通用性、可读性和错误位置捕获能力而优于正则表达式。

实现的核心围绕着`match-peg`函数，这是一个树状结构的解释器，它接受PEG规则和要匹配的文本。它支持基本的PEG运算符，如字符串字面量、有序选择（`+`）、序列（`*`）和布尔反转（`!`）。本文演示了如何在Janet中构建这些运算符，突出了它们到其他语言的轻松转换。

随后，本文通过使运算符变为可变参数来改进`match-peg`函数，以提高可读性，并使用Janet表将关键字映射到PEG表达式来引入递归。这允许定义更复杂的递归文法。

最后，本文展示了如何添加自定义规则，例如用于字符集的`:set`运算符，从而进一步扩展PEG引擎的功能。它承认简单实现中的局限性，例如缺少捕获和缺乏优化，但强调它是通用模式匹配函数的坚实基础。文章最后指出，Janet的实际PEG实现会将语法树编译成字节码以获得更好的性能。

---

## 13. Omnom：自托管书签，带可搜索的所见即所得快照[展示]

**原文标题**: Omnom: Self-hosted bookmarking with searchable, wysiwyg snapshots [showcase]

**原文链接**: [https://omnom.zone/?src=hn](https://omnom.zone/?src=hn)

这是一个Omnom的展示，一个自托管的书签工具。其主要亮点是能够对书签的网页进行快照，并以可搜索的、WYSIWYG（所见即所得）的形式保存。这使得用户能够保存并轻松检索网页内容，即使原始页面发生更改或消失。

提供的文本强调，展示的实例是一个只读演示，鼓励用户浏览项目的GitHub仓库以获取更多信息，并有可能自行托管自己的实例。该工具可能解决了常见的链接失效问题，以及以视觉上准确且可搜索的格式存档网页内容的需求。

---

## 14. OpenAI是科技行业的系统性风险

**原文标题**: OpenAI Is a Systemic Risk to the Tech Industry

**原文链接**: [https://www.wheresyoured.at/openai-is-a-systemic-risk-to-the-tech-industry-2/](https://www.wheresyoured.at/openai-is-a-systemic-risk-to-the-tech-industry-2/)

本文认为，OpenAI对其财务模式的不可持续性以及对可能无法完全兑现的大规模融资轮次的依赖，构成了对科技行业的系统性风险。作者质疑OpenAI估值的有效性，指出其估值远高于特斯拉的峰值，但收入却明显低于特斯拉。

一个主要担忧是OpenAI的高运营成本。作者估计，该公司在2025年的支出可能超过280亿美元，主要用于与微软和CoreWeave的计算资源，尽管预计收入为127亿美元，但可能导致超过140亿美元的亏损。估计耗资数十亿美元的星际之门数据中心项目进一步加剧了财务压力。

作者仔细审查了OpenAI的收入预测，并对“代理”等新收入来源的可行性表示怀疑。他们还强调，OpenAI在每个用户身上都在亏钱，因此依赖于吸引和留住大量付费用户至关重要。

本文表达了对软银对OpenAI和星际之门项目的财务承诺的担忧。软银必须借款才能履行义务，这可能导致其财务状况恶化。作者强调，即使OpenAI未能转化为营利性模式，软银也必须承担巨额资金，并强调了资金的或有性质。作者总结说，OpenAI的成本超过了其收入，并且其对外部资金的严重依赖是一个重大风险。

---

## 15. Socketcluster: 高度可扩展的发布/订阅和RPC SDK

**原文标题**: Socketcluster: Highly scalable pub/sub and RPC SDK

**原文链接**: [https://socketcluster.io](https://socketcluster.io)

SocketCluster是一个高度可扩展的发布/订阅和RPC SDK，专为实时应用程序设计，并针对使用async/await的异步操作进行了优化。它提供了构建可扩展和健壮应用程序的工具和特性。

主要特性包括：

*   **可扩展的发布/订阅：** 支持数百万个轻量级通道，并具有自动清理功能，确保高效的内存和CPU使用率。
*   **易于部署和扩展：** 通过CLI工具简化到Kubernetes的部署，并提供用于扩展工作进程和代理实例的命令。
*   **消息顺序保证：** 即使在沿套接字流进行异步操作的情况下，也能保持消息处理顺序。
*   **反压监控：** 允许监控入站和出站消息反压以优化性能。
*   **高效的身份验证：** 支持WebSockets的JWT身份验证，以最大限度地减少数据库查找。
*   **访问控制：** 使用中间件流强制执行访问控制，以阻止连接和单个套接字操作。
*   **数据转换：** 允许使用中间件流来限制和转换数据包。
*   **Async/Await和声明式代码：** 利用异步循环 (for-await-of) 来消除回调地狱，提高代码可读性，并促进声明式编程风格。
*   **故障恢复：** 客户端会自动处理丢失的连接，并在重新连接时重新订阅通道。
*   **自动内存管理：** 当不再使用时，会自动进行套接字和通道的垃圾回收。
*   **客户端库：** 提供 Javascript、Java/Android、Python、DotNet、Go、Swift/iOS、Ruby 和 Unity 的客户端库。

---

## 16. Cure ID App让临床医生报告现有药物的新用途

**原文标题**: Cure ID App Lets Clinicians Report Novel Uses of Existing Drugs

**原文链接**: [https://www.fda.gov/drugs/science-and-research-drugs/cure-id-app-lets-clinicians-report-novel-uses-existing-drugs](https://www.fda.gov/drugs/science-and-research-drugs/cure-id-app-lets-clinicians-report-novel-uses-existing-drugs)

Cure ID 应用程序，受到 FDA 的重点推荐，是一个平台，允许全球临床医生报告他们以新颖方式使用现有药物治疗难治性传染病的经验。这种众包方法旨在收集有关现有药物有效性和安全性的真实临床数据，特别是针对缺乏既定疗法或面临抗菌素耐药性的疾病。

该应用程序鼓励临床医生记录具体病例，详细说明患者的病情、使用的药物（包括剂量和疗程）以及观察到的结果（包括积极和消极）。虽然这些汇总数据是观察性的，不能替代随机对照试验，但它可以提供有价值的见解，并为进一步的研究生成假设。

Cure ID 的主要优势包括：

*   **促进临床经验的分享：** 它连接了全球的临床医生，使他们能够实时地从彼此的经验中学习。
*   **加速潜在疗法的识别：** 通过汇编关于非常规药物使用的报告，它可以突出显示有希望的候选药物，以供进一步研究。
*   **改善患者护理：** 临床医生可以访问不断增长的真实证据数据库，以指导他们的治疗决策，尤其是在具有挑战性的病例中。
*   **支持研究和药物开发：** 收集的数据可以为临床试验的设计和新疗法的开发提供信息。

FDA 认为 Cure ID 是一个有价值的工具，可以扩大药物再利用的证据基础，并解决传染病治疗中未满足的医疗需求。这是一项旨在通过医学界的集体智慧改善患者预后的合作努力。

---

## 17. MCP的全部问题

**原文标题**: Everything wrong with MCP

**原文链接**: [https://blog.sshh.io/p/everything-wrong-with-mcp](https://blog.sshh.io/p/everything-wrong-with-mcp)

Shrivu Shankar的文章《MCP的种种问题》批评了模型上下文协议 (MCP)，这是一种将第三方工具和数据与 LLM 驱动的聊天和代理集成的标准。文章承认 MCP 在提供上下文和代理自主性方面的作用，但同时也强调了几个潜在问题。

**安全问题** 包括缺乏强大的身份验证导致可能访问敏感数据、通过 stdio 在本地运行恶意代码的风险以及服务器信任输入，这可能导致代码执行漏洞。

**UI/UX 限制** 源于缺乏工具风险级别控制，使用户容易意外触发危险操作。文章还指出 LLM 带宽成本以及 MCP 的非结构化文本传输限制了其处理需要丰富界面和实时更新的复杂任务的能力。

**LLM 安全问题** 涉及提示注入的可能性，即工具可以覆盖系统提示并操纵代理行为。文章还指出了“第四方提示注入”、数据泄露的风险，以及 MCP 可能通过允许员工以非预期的方式聚合数据来打破传统数据访问控制模型的可能性。

最后，文章提到了 **LLM 局限性**，表明围绕 MCP 集成的过度期望常常与 LLM 当前的可靠性问题相冲突，尤其是在指令上下文增加的情况下。

---

## 18. 股权激励开放指南

**原文标题**: Open guide to equity compensation

**原文链接**: [https://github.com/jlevy/og-equity-compensation](https://github.com/jlevy/og-equity-compensation)

本指南全面概述股权激励，旨在帮助员工、招聘经理、创始人及学生做出明智的决策。内容涵盖美国C类公司中的股权激励，侧重于初创企业到大型公司的私营企业，对上市公司的覆盖有限。

本指南强调理解股权激励复杂性的重要性，包括术语、法律层面和潜在的财务后果。旨在实用、周全和简洁，提供具体的建议和专家观点。

主要议题包括：

*   **股权激励基础知识：** 是什么以及为什么使用。
*   **股份有限公司的基本原理：** 公司如何组织所有权和发行股票。
*   **股权授予方式：** 各种形式，如限制性股票、股票期权和限制性股票单位（RSU）。
*   **税务基础和股权激励税务：** 涵盖普通所得税、资本利得税和替代性最低税。
*   **计划和情景：** 评估股权价值和理解税务负担。
*   **录用通知和谈判：** 关于谈判工作录用通知中股权部分的建议。

本指南强调在做出重大决策前寻求律师或税务专业人士的专业建议的重要性。强调本指南虽提供有价值的信息，但不应取代个性化的专业指导。

---

## 19. 马里奥·巴尔加斯·略萨去世

**原文标题**: Mario Vargas Llosa has died

**原文链接**: [https://www.nytimes.com/2025/04/13/books/review/mario-vargas-llosa-appraisal.html](https://www.nytimes.com/2025/04/13/books/review/mario-vargas-llosa-appraisal.html)

文章宣布秘鲁作家马里奥·巴尔加斯·略萨去世，享年89岁，并回顾了他的文学意义，尤其是在美国。文章着重介绍了约翰·厄普代克在20世纪80年代对巴尔加斯·略萨的有力推崇，称赞了他的智慧、多才多艺和想象力，甚至认为他超越了加西亚·马尔克斯，成为北美读者最应该阅读的南美小说家。

虽然巴尔加斯·略萨已经发表了《城市与狗》、《绿房子》和《大教堂里的对话》等主要作品，但尽管在世界范围内广受赞誉，这些作品最初在美国的接受度较低。文章指出，巴尔加斯·略萨在拉丁美洲文学爆炸中扮演的角色，这场文学运动包括了加西亚·马尔克斯、卡洛斯·富恩特斯和胡里奥·科塔萨尔等著名作家。文章暗示，尽管略有姗姗来迟，厄普代克的认可在最终将巴尔加斯·略萨推到美国文学意识前沿方面发挥了作用。

---

## 20. Show HN: 用 Cosmopolitan 复活 Infocom 的 Unix Z-Machine

**原文标题**: Show HN: Resurrecting Infocom's Unix Z-Machine with Cosmopolitan

**原文链接**: [https://christopherdrum.github.io/posts/2025/04/porting-infocom-with-cosmo](https://christopherdrum.github.io/posts/2025/04/porting-infocom-with-cosmo)

作者在“Show HN”帖子中详细介绍了其使用Cosmopolitan复活Infocom原始UNIX Z-Machine（经典文本冒险游戏Zork的虚拟机）的项目。Cosmopolitan是一种工具，它允许C代码在多个操作系统上“一次编写，随处运行”，而无需传统的虚拟机。

作者移植了最初为UNIX系统设计的基于C的Z-Machine，为Windows、Mac、Linux和BSD上的x86和ARM架构创建了Zork的独立可执行文件。这些可执行文件无需安装或外部文件。

Cosmopolitan通过利用现代机器的ABI中的共性并创建“真正可移植的可执行文件”（APE）来实现可移植性，这些文件在单个文件中包含各种平台的本机代码。这消除了为每个操作系统单独构建的需要。

作者讨论了使用1985年的K&R风格C代码所面临的挑战，包括隐式类型声明和不寻常的语法。必要的修复包括处理NULL定义、现代化函数声明以及解决已弃用的函数（如播种`srand()`）。

该项目还演示了如何将游戏数据文件嵌入到APE可执行文件中，从而创建一个单一的、自包含的游戏包，类似于macOS应用程序包。该帖子最后为类似的项目提供了建议，强调了主题熟悉度的重要性以及采用有条不紊的方法来解决编译器错误和警告。

---

## 21. 函数式编程课程总结

**原文标题**: Functional Programming Lessons Conclusion

**原文链接**: [https://jerf.org/iri/post/2025/fp_lessons_conclusion/](https://jerf.org/iri/post/2025/fp_lessons_conclusion/)

本文反思了作者从函数式编程 (FP) 中学到的经验，以及它们如何应用于命令式语言。 核心论点是，虽然 FP 提供了宝贵的经验，但在微观层面应用它们（例如，在不考虑整体架构的情况下用 `map` 和 `reduce` 替换循环）可能是有害的。

作者强调在中到大型规模上理解和应用 FP 原则的重要性，重点关注架构方面的考虑，例如控制突变流、简化组件需求、协调类型以及利用类型系统来预防错误。 他们提倡优先考虑这些更高级别的问题，而不是微观优化。

虽然作者承认纯 FP 语言的优势（其中不变性和强大的类型系统提供了坚实的基础），但认为纯 FP 的“100/100”承诺（100% 的努力带来 100% 的收益）可能是不切实际的，并且会排除其他有价值的改进。 相反，作者提倡务实的“80/20”方法，表明多个不同领域的较小改进通常比在一个领域中追求绝对纯粹更能产生整体效益。 这种方法认识到现实世界编程的多样化需求，并避免对任何单一解决方案的教条式坚持。 作者最后鼓励读者利用 FP 知识来改进代码，即使在命令式环境中也是如此，通过关注软件设计和架构的全局。

---

## 22. 如何骑自行车横穿全国

**原文标题**: How to Bike Across the Country

**原文链接**: [https://www.brooks.team/posts/how-to-bike-across-the-country/](https://www.brooks.team/posts/how-to-bike-across-the-country/)

网页内容极其有限，仅包含标题“如何骑自行车横穿全国”并显示“加载中...”状态。

因此，无法进行总结。除了标题之外，该页面没有提供任何实际信息或内容。核心在于该页面*意图*提供关于骑自行车横穿全国的信息，但目前处于加载状态，没有提供任何可操作的见解或指示。

---

## 23. GitHub Copilot、Cursor 新漏洞：黑客可利用代码助手发动攻击

**原文标题**: New Vulnerability in GitHub Copilot, Cursor: Hackers Can Weaponize Code Agents

**原文链接**: [https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents](https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents)

Pillar Security 发现针对 AI 代码编辑器的“规则文件后门”供应链攻击，攻击 GitHub Copilot 和 Cursor 等工具。 攻击者将恶意指令注入看似无害的配置（“规则”）文件中，利用隐藏的 Unicode 字符和语义劫持等技术来操纵 AI 生成易受攻击的代码。 此攻击绕过了传统的代码审查，使开发人员几乎无法察觉。

这些规则文件在团队之间共享，有时会出现在公共存储库中，它们被隐式信任，但很少经过验证。 通过污染这些文件，攻击者可以入侵 AI 代码生成，注入后门，覆盖安全控制，导致数据泄露并创建长期持久性。 攻击可在不同的 AI 助手上生效，表明存在系统性漏洞。

文章演示了在 Cursor 和 GitHub Copilot 环境中的攻击，展示了 AI 如何在不提醒开发人员的情况下添加来自攻击者控制站点的恶意脚本。 该有效负载使用诸如“越狱故事讲述”之类的复杂方法来绕过 AI 伦理约束，并向开发人员隐藏日志。

Pillar Security 建议审计现有规则文件，为 AI 配置文件实施验证流程，部署检测工具，并仔细审查 AI 生成的代码。 尽管 Cursor 和 GitHub 都表示验证代码是用户的责任，但 Pillar Security 强调提高公众意识的重要性，以及发展安全模型以防止开发流程中基于 AI 的操纵的必要性。

---

## 24. 显示HN：我做了一个免费工具，可以分析SEC文件并发布详细报告

**原文标题**: Show HN: I made a free tool that analyzes SEC filings and posts detailed reports

**原文链接**: [https://www.signalbloom.ai/news/](https://www.signalbloom.ai/news/)

此“Show HN”帖子介绍一款免费工具，用于分析美国证券交易委员会 (SEC) 文件并生成详细报告。提供的示例侧重于 Certara Inc. 2025 年第一季度的业绩。该工具识别出 Certara 文件中的关键点，包括 10% 的收入增长和回购计划的启动。它将此增长主要归功于 Certara 的软件部门以及近期收购的贡献。该帖子鼓励用户访问“阅读完整分析”以获取更深入的信息。本质上，该工具承诺自动化 SEC 文件的分析，为用户提供对上市公司财务业绩的快速且易于理解的摘要。

---

## 25. 谷歌人... 前谷歌人

**原文标题**: Googler... ex-Googler

**原文链接**: [https://nerdy.dev/ex-googler](https://nerdy.dev/ex-googler)

谷歌Chrome团队成员Adam Argyle突然被裁，他被告知该决定与他的表现无关，甚至令他的经理们都感到震惊。他表示感到被背叛和被低估，尤其是在这个时间点上。他当时正积极参与Chrome团队的团建活动，参与创意创新，并为即将到来的Google I/O大会的重要角色做准备。

他的裁员立即切断了他对谷歌资源的访问，例如日历、文档和代码，这让他感到不受欢迎，尽管他被告知有可能在公司内部找到另一个职位。他感叹失去了他的职责，包括Google I/O的视频录制、在活动中的舞台亮相、运营展位、为开发者主题演讲做贡献、他的CSS工作组会员资格、开发者办公时间、Carousel Gallery的代码访问权限，以及参与谷歌的CSS工作，例如Overflow 5。

Argyle强调了多年来建立的职业关系的丧失，并感觉他的贡献被忽视了。最后，他分享了他在Bluesky上的联系方式和他个人的电子邮件，并表示由于情感负担，他可能回复较慢。他总结说，他感觉自己只是机器中的一个齿轮。

---

## 26. 黑客C语言实战指南

**原文标题**: Hacktical C: practical hacker's guide to the C programming language

**原文链接**: [https://github.com/codr7/hacktical-c](https://github.com/codr7/hacktical-c)

《Hacktical C》是一本C语言的实用指南，面向具备基础知识、希望利用C语言的强大功能和灵活性的程序员。作者以黑客的身份强调实际应用和使用强大工具解决问题。

本书推崇C语言作为一种可移植的汇编语言，在软件开发中提供自由和责任。它承认对C语言的批评，但认为归因于C语言的许多问题源于软件设计的不成熟，而不是C语言本身固有的缺陷。作者主张根据程序员的理解选择合适的工具，并拒绝被迫使用首选工具。

该指南使用GNU扩展，如cleanup属性、多行表达式和嵌套函数，以增强在缺乏标准替代方案时的功能，特别是对于像`hc_defer()`这样的功能。

内容以渐进的方式组织，后面的章节建立在前面的概念之上。该项目是开源的，欢迎贡献，包括捐款以支持作者的工作。作者建议使用Linux进行C语言开发，因为它方便访问Unix和Valgrind。本书包括基准测试、宏指南，以及关于定点算术、链表、并发任务、内存分配器、向量、异常、集合和映射、动态编译以及结构化日志等主题的章节。

---

## 27. AES与ChaCha

**原文标题**: AES and ChaCha

**原文链接**: [https://phase.dev/blog/chacha-and-aes-simplicity-in-cryptography/](https://phase.dev/blog/chacha-and-aes-simplicity-in-cryptography/)

本文对两种流行的对称加密算法AES（高级加密标准）和ChaCha20进行了技术比较。AES于2001年由NIST标准化，一直是保护网络流量的主要选择。ChaCha20由Daniel Bernstein于2008年发布，由于其简单性和效率，作为一种潜在的替代方案正日益受到关注。

本文首先介绍了对称加密的基础知识，解释了诸如明文、密文、密钥、随机数和密钥流等概念。它强调了简单地将密钥与明文进行异或运算的漏洞，从而激发了对像AES和ChaCha20这样复杂密码的需求。

AES和ChaCha20都作为流密码运行，使用密钥流生成器 (KSG) 将密钥、随机数和计数器组合以生成密钥流，然后将其与明文进行异或运算。

AES使用在 128 位块上运行的替换-置换网络，涉及每轮中复杂的转换，例如 SubBytes、ShiftRows、MixColumns 和 AddRoundKey。这些操作计算成本高昂，涉及查找表和有限域数学。

另一方面，ChaCha20 基于 ARX（加、旋转、异或）运算，这些运算计算成本更低，并且受到现代 CPU 的原生支持。它在一个 4x4 状态矩阵上运行，并使用四分之一轮函数迭代 20 轮以最大化位扩散。

主要结论是，AES 通过复杂的操作来实现加密强度，而 ChaCha20 则凭借其基于 ARX 的设计优先考虑简单性和效率。

---

## 28. 枯树能将大量碳锁在环境中，令人惊讶。

**原文标题**: Dead trees keep surprisingly large amounts of carbon out of atmosphere

**原文链接**: [https://phys.org/news/2025-03-dead-trees-large-amounts-carbon.html](https://phys.org/news/2025-03-dead-trees-large-amounts-carbon.html)

死亡树木在碳储存中的重要作用：一项研究揭示溪流中的碳汇效应

---

## 29. NoProp：无需反向传播或前向传播训练神经网络

**原文标题**: NoProp: Training neural networks without back-propagation or forward-propagation

**原文链接**: [https://arxiv.org/abs/2503.24322](https://arxiv.org/abs/2503.24322)

这篇于2025年3月31日提交至 arXiv 的论文介绍了“NoProp”，一种新颖的神经网络训练方法，它抛弃了传统深度学习的基石——前向和反向传播。相反，NoProp 从扩散和流匹配技术中汲取灵感，其中每一层学习独立地对目标表示的噪声版本进行去噪。这与标准神经网络的分层表示学习有所不同，在标准神经网络中，层建立在来自较低层的表示之上。

核心思想是每一层都被训练成执行局部去噪。 这需要将每一层的表示固定为带噪声的目标，使每一层成为一个独立的去噪过程，在推理过程中加以利用。

作者李沁瑜、Yee Whye Teh 和 Razvan Pascanu 证明了 NoProp 在 MNIST、CIFAR-10 和 CIFAR-100 图像分类数据集上的有效性。结果表明，NoProp 是一种可行的学习算法，可以实现有竞争力的准确性，更易于使用，并且在计算上比其他现有的无反向传播方法更有效。

作者认为，通过放弃基于梯度的学习，NoProp 为网络内的信用分配提供了一种新方法，这可能导致更有效的分布式学习，并可能影响其他学习过程的特征。该论文归类于机器学习 (cs.LG) 和机器学习 (stat.ML) 之下。

---

## 30. Zig 的新链表 API (是时候了解 fieldParentPtr 了)

**原文标题**: Zig's new LinkedList API (it's time to learn fieldParentPtr)

**原文链接**: [https://www.openmymind.net/Zigs-New-LinkedList-API/](https://www.openmymind.net/Zigs-New-LinkedList-API/)

本文讨论了 Zig 中 `SinglyLinkedList` 和 `DoublyLinkedList` API 的近期变更，重点关注侵入式链表的引入以及 `@fieldParentPtr` 内置函数的使用。

旧的泛型链表已被非泛型侵入式链表取代，其中链表节点直接嵌入在数据结构中。这种方法提高了性能并减少了分配开销。

关键的挑战是从给定的链表节点检索父数据结构。这就是 `@fieldParentPtr` 发挥作用的地方。它允许你获取包含特定字段（在本例中为链表节点）的结构的指针。它接受字段名称、指向该字段的指针和所需的父类型，计算必要的偏移量以找到父地址。

本文提供了一个代码示例，展示了如何使用新的 `SinglyLinkedList` API 和 `@fieldParentPtr`。它演示了如何创建一个 `User` 结构体的链表，每个结构体包含一个 `SinglyLinkedList.Node`，然后遍历该链表，使用 `@fieldParentPtr` 从节点访问 `User` 数据。

虽然承认 `@fieldParentPtr` 在解决某些问题上的实用性，但作者对其在链表这种基本数据结构中的必要性表达了复杂的感受，认为它可能会增加不必要的复杂性。作者总结说，开发者应该熟悉 @fieldParentPtr，因为它有助于解决原本棘手的问题。

---

## 31. 用光标规则编写光标规则

**原文标题**: Writing Cursor rules with a Cursor rule

**原文链接**: [https://www.adithyan.io/blog/writing-cursor-rules-with-a-cursor-rule](https://www.adithyan.io/blog/writing-cursor-rules-with-a-cursor-rule)

本文探讨了在Cursor等编码环境中，使用大型语言模型（LLM）时遇到的挑战，即它们缺乏“情景记忆”——跨会话保持知识的能力。这迫使开发者反复解释项目标准和偏好。提出的解决方案是创建“Cursor规则”，即驻留在存储库的`.cursor/rules/`目录中的项目特定指令文档，为AI提供持久指导。

作者强调了为AI构建系统的重要性，并以管理患有失忆症的开发者为例，使用文档、风格指南和模板来确保一致性。

本文的核心在于“元Cursor规则”的概念。这是一种主规则，用作创建所有其他规则的模板，从而简化规则创建过程。作者提供了一个详细的、即插即用的元规则模板，其中包括YAML frontmatter（标题、描述、glob、alwaysApply）、内容部分（介绍、模式描述、实施步骤、示例、陷阱）以及文件引用（`@file`）和正确的代码块格式等高级功能。

使用Cursor规则的好处包括减少重复解释、确保一致的AI行为以及加速开发。作者还提供了规则创建的最佳实践，例如从简单开始、关注模式并保持规则更新。通过使用元规则，开发者可以利用AI本身来生成结构良好的规则，从而节省时间和精力。

---

## 32. 阿尔伯特·爱因斯坦的四字相对论 (1999)

**原文标题**: Albert Einstein's theory of relativity in words of four letters or less (1999)

**原文链接**: [https://www.muppetlabs.com/~breadbox/txt/al.html](https://www.muppetlabs.com/~breadbox/txt/al.html)

本文用四个字母以内的单词，以通俗口语化的方式解释了爱因斯坦的相对论。

解释始于阐述运动的相对性。它断言，没有参照点，确定运动是不可能的。相对于一个物体，是你运动还是物体运动是随意的。

文章接着引入光速常数('c')，认为这是对此原则的挑战。最初，似乎测量相对于观察者的光速可以确定他们的运动。然而，实验证明，无论观察者如何运动，光速始终为'c'。

爱因斯坦的解决方案是抛弃绝对时间的观念。文章使用一个思想实验，让伯特和达娜在一辆行驶的公共汽车上，以证明同时性是相对的。事件是否同时发生取决于观察者的参照系。

时间的这种相对性延伸到大小和质量。这些属性的测量取决于观察者的相对运动。

文章然后讨论了“拉力”（引力或加速度）的概念。它介绍了惯性的历史理解（静止的物体保持静止，运动的物体保持运动），并强调外部影响（“拉力”）会破坏这种状态。例如，月球上的拉力使其保持在轨道上。

爱因斯坦将他的相对性扩展到拉力本身，将惯性拉力等同于引力拉力。这个“等效原理”表明，感受加速度与体验重力是无法区分的。因此，即使是拉力的感觉也是相对的。一个人总是可以将他们的参照系定义为“静止”，即使在体验加速度或重力时，因为他们可以想象整个宇宙都在拉着他们。

故事的结尾指出，其他科学家认为艾尔的理论有点疯狂。

---

## 33. 宇宙万物为何变得更复杂

**原文标题**: Why Everything in the Universe Turns More Complex

**原文链接**: [https://www.quantamagazine.org/why-everything-in-the-universe-turns-more-complex-20250402/](https://www.quantamagazine.org/why-everything-in-the-universe-turns-more-complex-20250402/)

菲利普·鲍尔的文章探讨了一个新的假设，该假设认为宇宙中的复杂性随着时间的推移而增加，不仅在生物体中，而且在非生物系统中也是如此。 这挑战了生物进化是一个独特过程的观点，而是提出了一种普遍的原则，即实体是根据其“功能信息”进行选择的，使其能够执行功能。

功能信息的概念源于杰克·绍斯塔克在量化生物分子信息方面的工作，它强调了执行特定任务的能力如何促进复杂性。 罗伯特·哈森和迈克尔·黄扩展了这个想法，认为它也适用于非生物系统。 例如，矿物根据其在特定环境中的稳定性演变为更大的复杂性，而元素通过恒星中的核聚变变得更加复杂。

作者提出，这种日益增长的复杂性驱动着时间的箭头，类似于熵，并且信息可能成为宇宙的基本参数。 他们还认为，类似于重大进化转变的复杂性跃迁，在这种框架内可能是不可避免的。 这些转变释放了新的可能性，并改变了选择的标准，从而创造了一种“进化物理学”。

批评者认为，“功能”的概念在生物学之外不太明确，并且功能信息难以量化，这使得该理论难以检验。

---

## 34. 从零开始实现DeepSeek R1的GRPO算法

**原文标题**: Implementing DeepSeek R1's GRPO algorithm from scratch

**原文链接**: [https://github.com/policy-gradient/GRPO-Zero](https://github.com/policy-gradient/GRPO-Zero)

本文从零开始介绍DeepSeek R1的组相对策略优化 (GRPO) 算法的实现，重点在于使用最少的依赖项通过强化学习训练大型语言模型。GRPO的核心思想是为每个问题采样多个答案，并根据归一化奖励定义答案的优势，从而无需价值估计网络。

所实现的GRPO算法包括token级别的策略梯度损失、移除KL散度以减少内存使用以及可选的超长episode过滤以提高训练稳定性等改进。该项目将GRPO应用于“倒计时”任务，其中模型根据给定的数字和目标值生成数学表达式。该模型经过训练，可以在给出最终答案之前生成“思维链”推理过程，并使用 `<think>` 和 `<answer>` 标签遵守特定格式。

奖励函数包括格式奖励（正确格式为 0.1）和答案奖励（正确且完整的答案为 1）。训练利用 Qwen2.5-3B-Instruct 模型，涉及设置环境，下载数据集和预训练模型，以及运行 `train.py` 脚本。该项目感谢DeepSeekMath、DAPO、TinyZero、nano-aha-moment和Qwen2.5的贡献。

---

## 35. 变压器实验室

**原文标题**: Transformer Lab

**原文链接**: [https://transformerlab.ai/](https://transformerlab.ai/)

无法访问文章链接。

---

## 36. 帕金森病是人造疾病

**原文标题**: 'Parkinson's is a man-made disease'

**原文链接**: [https://www.politico.eu/article/bas-bloem-parkinsons-pesticides-mptp-glyphosate-paraquat/](https://www.politico.eu/article/bas-bloem-parkinsons-pesticides-mptp-glyphosate-paraquat/)

帕金森病：环境因素与农药暴露的关联

文章认为，帕金森病很大程度上是一种由环境因素，特别是农药暴露驱动的“人造疾病”。文章强调了1982年海洛因使用者在接触神经毒素MPTP后出现类似帕金森病症状的案例，该毒素在化学成分上与除草剂百草枯相似。

顶尖帕金森病研究员巴斯·布鲁姆博士认为，全球帕金森病病例的快速增长不能仅用年龄和遗传因素来解释。他指出集约化农业与农药使用之间存在关联，并指出帕金森病在化学品广泛使用之前很罕见。

虽然欧洲已经禁止了一些农药，如百草枯，但包括美国在内的许多国家仍在继续使用。文章重点关注使用最广泛的除草剂草甘膦，并讨论了人们对其潜在危害的担忧，这些危害通过间接机制发挥作用，而目前的监管毒理学测试主要关注急性毒性和单一化学物质，而不是检查联合的、长期影响，因此未能充分评估草甘膦的潜在危害。

文章批评欧洲食品安全局（EFSA）依赖行业提供的数据和预先确定的方法，使其难以跟上关于微生物组破坏、化学协同作用和慢性低剂量暴露的不断发展的科学。文章强调，在评估环境毒素在帕金森病发病率上升中的风险时，需要采取更积极和全面的方法。

---

## 37. 为什么是茴香？

**原文标题**: Why Fennel?

**原文链接**: [https://fennel-lang.org/rationale](https://fennel-lang.org/rationale)

茴香 (Fennel) 是一种编译为 Lua 的编程语言，它利用 Lua 的速度、简洁性和可嵌入性。“为什么选择茴香？”一文认为，虽然 Lua 很出色，但它也有一些不足之处，而茴香通过替代语法和约定解决了这些不足，同时又不牺牲 Lua 的优势。

茴香采用 Lisp 风格的，以括号开头的语法，这消除了 Lua 中的语句、运算符优先级和提前返回，使语法更规范。茴香通过阻止意外的全局变量并要求显式声明 (`var`) 可重新赋值的局部变量来改进变量处理，从而促进更简洁的代码。

它还改进了 Lua 的表格表示法，使用方括号表示顺序表格，使用花括号表示键/值表格。茴香使用 `each` 区分数字 `for` 循环和基于迭代器的循环。此外，茴香还提供了使用 `lambda` 在函数中进行参数个数检查的选项，从而防止因参数不足而导致的意外行为，而 `fn` 没有参数个数检查，速度更快。

最后，茴香融入了 Lua 中没有但在现代语言中常见的特性：数据结构解构、条件语句的模式匹配以及用于扩展语言的宏系统。通过构建在 Lua 之上并解决其弱点，茴香提供了更现代和健壮的开发体验。

---

## 38. 梦想要将钻探触及莫霍面

**原文标题**: The Moho is in reach of ocean drilling with the Meng Xiang

**原文链接**: [https://www.nature.com/articles/s41561-025-01675-7](https://www.nature.com/articles/s41561-025-01675-7)

本文重点介绍了新近启用的中国“梦想”号科考船最终钻穿地球海洋地壳，抵达莫霍洛维奇不连续面（莫霍面），即地壳与地幔之间边界的潜力。“梦想”号是专门为此目的而设计的，配备了先进技术，如用于应对恶劣海况的动态稳定系统、钛合金钻杆和用于承受高温高压环境的金刚石钻头。它还配备了一个浮动实验室，用于快速处理岩心样本。

尽管承认存在挑战，需要耐心和多次探险，但本文对在2030年之前实现太平洋或印度洋海底莫霍面全尺寸钻探表示乐观。由此产生的钻探岩心样本将为海洋地壳的结构和形成、莫霍面的岩石学性质提供前所未有的见解，并将有助于完善板块构造理论。此外，这些样本将用于探索地球深处生命的极限。

除了抵达莫霍面，“梦想”号还将继续“决心”号大洋钻探船的工作，解决与大洋钻探相关的广泛科学问题。作者倡导围绕“莫霍面任务”进行国际合作，欢迎国际科学家参与钻探探险并分享样本，遵循类似于综合大洋钻探计划（IODP）的暂停期。预计首次科学考察将于明年开始。

---

## 39. 使用Ollama和LangChain快速入门MCP

**原文标题**: Quick Primer on MCP Using Ollama and LangChain

**原文链接**: [https://www.polarsparc.com/xhtml/MCP.html](https://www.polarsparc.com/xhtml/MCP.html)

本文简要介绍了模型上下文协议 (MCP)，这是一种将大型语言模型 (LLM) 应用程序与外部数据源和工具集成的行业标准。MCP 作为一个标准化层，使 LangChain 和 LlamaIndex 等代理框架能够一致地访问企业工具。

MCP 的核心组件包括：

*   **MCP 服务器：** 连接到数据源和工具，向 LLM 应用程序公开功能。
*   **MCP 客户端：** 以标准化方式连接并与 MCP 服务器交互。
*   **MCP 主机：** 利用 MCP 客户端访问 MCP 服务器的 LLM 应用程序。

本文然后提供了一个使用 Ollama、LangChain 和 Python 的实践演示。 首先，它设置环境，包括安装必要的 Python 模块并下载 LLM 模型 (IBM Granite 3.1)。 最初，展示了一个基于 LangChain 的简单 ReAct 应用，它在利息计算方面存在困难。

接下来，本文使用 `fastmcp` 库在 Python 中构建一个 MCP 服务器，以计算单利和复利。 它强调 MCP 支持标准 IO (stdio) 和服务器发送事件 (sse) 传输。 演示继续在 Python 中创建一个 MCP 主机（LLM 应用程序），利用 MCP 客户端与 MCP 服务器交互。 这使 LLM 应用程序能够成功计算单利和复利，从而证明了 MCP 在使 LLM 能够利用外部工具和数据方面的有效性。

---

## 40. Docker 模型运行器

**原文标题**: Docker Model Runner

**原文链接**: [https://www.docker.com/blog/introducing-docker-model-runner/](https://www.docker.com/blog/introducing-docker-model-runner/)

Docker 模型运行器是 Docker Desktop 中的一项新功能，旨在简化开发者在本地运行和测试 AI 模型的过程。它解决了当前本地 AI 模型开发中工具分散、硬件兼容性问题以及工作流程脱节的挑战。

主要功能包括：

*   **简化模型执行：** 像运行容器一样轻松地在本地运行 AI 模型，使用基于 llama.cpp 构建并通过 OpenAI API 访问的推理引擎。
*   **GPU 加速：** 利用 Apple silicon 上的 GPU 加速，实现更快的推理和更好的性能。
*   **标准化模型打包：** 使用 OCI Artifacts 进行模型分发和版本控制，从而能够与现有的容器注册表和 CI/CD 管道集成。
*   **生态系统合作：** 与 Google、HuggingFace、Continue、Dagger、Spring AI、VMware Tanzu 和 Qualcomm Technologies 合作推出，以提供对优化模型、框架和工具的访问。

Docker 模型运行器旨在通过推广本地优先的 LLM 开发来提高性能、降低成本并增强数据隐私。 最初的 Beta 版本侧重于简化本地模型执行，以实现更快的迭代和测试。 未来路线图包括支持更多平台（如支持 GPU 加速的 Windows）、模型定制和发布功能，以及与 Compose 和 Testcontainers 等工具的更紧密集成。 它作为 Docker Desktop 4.40 中适用于配备 Apple silicon 的 Mac 的 Beta 功能提供。

---

## 41. 中微子最大可能质量进一步缩小

**原文标题**: Neutrinos' maximum possible mass shrinks further

**原文链接**: [https://www.sciencenews.org/article/neutrino-mass-shrinks-katrin-electron](https://www.sciencenews.org/article/neutrino-mass-shrinks-katrin-electron)

本文报道了卡尔斯鲁厄氚中微子（KATRIN）实验的一项新成果，该成果进一步约束了中微子的最大可能质量。科学家们确定中微子的质量小于0.45电子伏特，这比KATRIN之前的上限有了显著降低。

中微子是一种质量极小的基本粒子，其精确值仍然未知，这在粒子物理学中构成了一个重要的谜题。位于德国的KATRIN实验研究了氚放射性衰变中产生的电子反中微子。通过分析数百万次衰变中释放的电子能量，科学家们可以根据中微子对最大电子能量的微妙影响来推断中微子的质量。

这项新成果来自于对3600万个电子的分析，为中微子质量提供了独立于假设的约束。虽然宇宙学观测也提供了中微子质量的估计值，但这些估计值取决于我们对宇宙演化的理解。KATRIN的直接测量提供了一种互补且稳健的方法。

该实验将持续收集数据到2025年底，研究人员计划分析现有数据，以进一步完善他们对中微子质量的约束。确定中微子的质量是理解为什么这些粒子的质量与其他基本粒子相比如此轻的重要一步。

---

## 42. 红色橙子包让橙子看起来有多橙？

**原文标题**: How much oranger do red orange bags make oranges look?

**原文链接**: [https://alexanderell.is/posts/orange/](https://alexanderell.is/posts/orange/)

本文探讨了常用于销售橘子的红色网袋是否会影响我们对水果颜色的感知。作者假设红色网袋会使橘子看起来更“橘”，因此更具吸引力。

为了验证这一点，作者在一致的光照和相机条件下，拍摄了有和没有红色网袋的橘子照片。然后，他们使用图像处理工具（sips、magick 和 OpenCV）来计算每张照片中橘子的平均像素颜色。出人意料的是，计算出的平均像素颜色比预期的要棕色得多。然而，分析确实揭示了一个一致的趋势，即当用红色网袋拍摄橘子时，会向更暖的色调（红色和蓝色增加，绿色减少）转变。

作者承认，平均像素值不能完全捕捉到人类的颜色感知，因为我们的眼睛会适应环境并记住颜色。他们引用了关于色适应和颜色恒常性的研究，以强调人类视觉的复杂性。

尽管平均像素结果不尽如人意，但作者仍然相信，由于人眼的错觉，红色网袋确实让橘子看起来更橘，并将其视为零售商使用的一种小伎俩。作者提出了一个未来的实验，让受试者直接测量有和没有红色网袋的橘子的感知平均颜色。

---

## 43. 用 Racket 编写我自己的抖动算法

**原文标题**: Writing my own dithering algorithm in Racket

**原文链接**: [https://amanvir.com/blog/writing-my-own-dithering-algorithm-in-racket](https://amanvir.com/blog/writing-my-own-dithering-algorithm-in-racket)

本文可能记录了使用Racket编程语言从头开始实现抖动算法的过程。作者可能首先解释抖动的概念——一种通过策略性地将不同颜色的像素紧密放置在一起，从而在有限的调色板中模拟比实际可用颜色更多的颜色的技术。

本文可能概述了选择用于实现的特定抖动算法，这可能是一种简单的算法（如阈值化），或者是一种更复杂的算法（如Floyd-Steinberg抖动）。作者可能会解释所选算法的数学基础，详细说明如何执行误差扩散或其他计算。

重点可能包括：

*   **Racket代码片段：** 作者可能提供Racket代码示例，说明如何实现抖动算法，包括像素操作、误差计算和颜色映射。
*   **挑战与解决方案：** 作者可能会讨论在实现过程中面临的挑战，例如处理边缘情况、优化性能或在Racket中准确表示颜色。将会描述这些挑战的解决方案。
*   **结果与可视化：** 本文可能包含视觉示例，展示抖动算法对图像的影响。可能会使用前后对比来证明所实现算法的有效性。
*   **潜在的优化和未来改进：** 作者可能会通过提出对算法的潜在改进或优化来结束，例如探索不同的误差扩散策略或调色板。

---

## 44. 数学 13 – 抽象数学导论 [pdf]

**原文标题**: Math 13 – An Introduction to Abstract Mathematics [pdf]

**原文链接**: [https://www.math.uci.edu/~ndonalds/math13/notes.pdf](https://www.math.uci.edu/~ndonalds/math13/notes.pdf)

该文档似乎是“数学13 – 抽象数学导论”的目录，基于PDF对象分析，特别是/GoTo操作。 它概述了课程涵盖的主题，从基础逻辑和证明技巧到更高级的集合论和基数。

课程从证明导论开始，深入研究逻辑，证明语言以及不同的证明方法和策略。 然后探讨可除性，欧几里德算法和同余。

课程的很大一部分侧重于集合，包括集合符号、子集、并集、交集、补集和函数。 数学归纳法和良序被认为是重要的证明技巧。

课程的后半部分进一步发展了集合论，研究了笛卡尔积、幂集和索引集合族。 最后，材料涉及关系、划分、二元关系、函数回顾、等价关系和良定义。 课程最终讨论基数和无限集，包括康托尔的基数概念和不可数集。

---

## 45. 卡吕普索：大型语言模型作为地下城主助理 [pdf]

**原文标题**: Calypso: LLMs as Dungeon Masters' Assistants [pdf]

**原文链接**: [https://andrewhead.info/assets/pdf/calypso.pdf](https://andrewhead.info/assets/pdf/calypso.pdf)

抱歉，我无法总结该文档。文档内容已编码，可能是一个PDF文件，并且似乎主要包含非人类可读的字符。

---

## 46. 展示：日产聆风App没有主屏幕小部件，所以我自己做了一个

**原文标题**: Show HN: Nissan's Leaf app doesn't have a home screen widget so I made my own

**原文链接**: [https://kevintechnology.com/posts/leaf-widget/](https://kevintechnology.com/posts/leaf-widget/)

本文详细介绍了作者如何创建一个自定义的iPhone主屏幕小组件，以显示其日产LEAF的电池充电状态，因为官方的NissanConnect应用程序缺少此功能。由于日产对第三方应用程序的限制导致一些有用的替代方案被取消，作者对此感到沮丧，并开始了一个“不花钱”的项目。

该解决方案涉及一个复杂的自动化流程，利用了多种技术。首先，一个GitHub Action下载NissanConnect应用程序，并使用Appium自动登录并从运行在Android设备上的应用程序中抓取电池状态。另一个GitHub Actions工作流程，按计划运行，使用Tailscale连接到运行Android的Raspberry Pi（充当Android设备），并触发第一个GitHub Action。抓取的数据随后通过电子邮件发送到IFTTT。 IFTTT反过来使用通知小组件在iPhone主屏幕上显示电池信息，并使用TinyURL链接启动一个自定义的Apple捷径，以便在点击小组件时打开NissanConnect应用程序。

由于NissanConnect应用程序在x86_64架构上的兼容性问题以及GitHub Actions runners上嵌套虚拟化的限制，作者在云端启动Android模拟器时遇到了挑战。他们也承认该设置的脆弱性，因为日产可能会通过未来的应用程序更新来破坏它。作者希望未来能有涉及GitHub Actions上的M3 Apple Silicon runners或拥有更好应用程序体验的不同汽车的解决方案。

---

## 47. Exwm：Emacs X窗口管理器

**原文标题**: Exwm: Emacs X Window Manager

**原文链接**: [https://github.com/emacs-exwm/exwm](https://github.com/emacs-exwm/exwm)

EXWM (Emacs X 窗口管理器) 是一个强大的平铺式 X 窗口管理器，完全运行在 Emacs 内部。它利用 XELB 提供完全键盘驱动的窗口管理体验。主要功能包括混合布局模式（平铺和堆叠）、动态工作区管理，以及符合 ICCCM/EWMH 标准，确保与其他 X 应用程序的兼容性。

EXWM 还提供可选功能以增强用户体验，例如支持多显示器设置的 RandR、系统托盘、输入法集成、背景设置功能，甚至可以充当 XSETTINGS 服务器。

建议潜在用户查看展示 EXWM 功能的屏幕截图，并查阅用户指南以获取全面的安装说明和详细的使用说明。本质上，EXWM 将 Emacs 转换为一个功能齐全且可定制的桌面环境。

---

## 48. 美国孕产妇死亡率在发达国家中最高。

**原文标题**: The US has highest rate of pregnancy-related death among high-income countries

**原文链接**: [https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2832320](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2832320)

《JAMA Network Open》文章“美国是高收入国家中孕产妇死亡率最高的国家”强调了美国孕产妇死亡率令人担忧的趋势。该研究证实，与其他高收入国家相比，美国的孕产妇死亡率明显更高。

主要发现包括：

*   **死亡率差异：** 与其他经济地位和医疗基础设施相似的发达国家相比，美国的孕产妇死亡率显著偏高。

*   **种族和民族差异：** 该研究可能重申了孕产妇死亡率方面已知的差异，尤其对黑人/非洲裔美国女性和美洲原住民女性影响较大。 这表明在获得医疗服务、医疗质量和社会健康决定因素方面存在系统性问题。

*   **关注可预防性：** 该文章可能探讨了被认为是可预防的孕产妇死亡比例很高这一问题。 这强调了需要改善产前和产后护理，更好地管理潜在的健康状况，并解决紧急产科护理问题。

*   **数据和方法：** 该研究可能使用了最新的孕产妇死亡率数据，将美国与同侪国家进行比较，同时控制相关变量。 作者分析了特定时期内的趋势，以证明美国情况的恶化。

*   **行动呼吁：** 该报告可能表明，需要采取紧急行动来解决这一公共卫生危机，包括政策变更，增加对孕产妇健康计划的资金投入，消除医疗保健中的偏见，并改善所有人群获得优质医疗保健服务的机会。

---

## 49. AWS 宣布 S3 Express One Zone 降价 85%

**原文标题**: AWS announces 85% price reductions for S3 Express One Zone

**原文链接**: [https://aws.amazon.com/blogs/aws/up-to-85-price-reductions-for-amazon-s3-express-one-zone/](https://aws.amazon.com/blogs/aws/up-to-85-price-reductions-for-amazon-s3-express-one-zone/)

AWS宣布Amazon S3 Express One Zone将于2025年4月10日生效大幅降价。这种高性能、单可用区存储类专为需要个位数毫秒级数据访问的延迟敏感型应用而设计。

降价幅度包括：

*   **存储（每GB每月）：** 降低31%（从0.16美元降至0.11美元）
*   **写入（PUT请求）：** 降低55%（从每1,000个请求0.0025美元降至0.00113美元）
*   **读取（GET请求）：** 降低85%（从每1,000个请求0.0002美元降至0.00003美元）
*   **数据上传/检索（每GB）：** 降低60%（分别从0.008美元/0.0015美元降至0.0032美元/0.0006美元），适用于所有字节。

S3 Express One Zone提供比S3 Standard快达10倍的数据访问速度，每个目录桶最多支持200万GET TPS和20万PUT TPS。它适用于交互式数据分析、媒体渲染、HPC和AI/ML等工作负载。自发布以来，增加了对象过期S3生命周期支持以及直接将数据附加到现有对象等功能。

这些降价适用于所有提供S3 Express One Zone的可用AWS区域，包括美国东部（弗吉尼亚北部）、美国东部（俄亥俄）、美国西部（俄勒冈）、亚太地区（孟买）、亚太地区（东京）、欧洲（爱尔兰）和欧洲（斯德哥尔摩）。

---

## 50. 使用 Aider 浪费推理

**原文标题**: Wasting Inferences with Aider

**原文链接**: [https://worksonmymachine.substack.com/p/wasting-inferences-with-aider](https://worksonmymachine.substack.com/p/wasting-inferences-with-aider)

无法访问文章链接。

---

## 51. Shadertoys移植到Rust GPU

**原文标题**: Shadertoys Ported to Rust GPU

**原文链接**: [https://rust-gpu.github.io/blog/2025/04/10/shadertoys/](https://rust-gpu.github.io/blog/2025/04/10/shadertoys/)

本文探讨了使用 Rust GPU 将 Shadertoy 着色器移植到 Rust 的经验。Rust GPU 是一个允许使用 Rust 编写 GPU 代码的项目。Rust GPU 将 Rust 代码编译为 SPIR-V，从而可以与 Vulkan 集成。

作者强调了使用 Rust GPU 的几个优点。由于 Rust 的数据布局控制和诸如 `bytemuck` 之类的 crate，CPU 和 GPU 之间的数据共享是无缝的。Rust GPU 支持 Rust 的强大功能，如 trait、泛型和宏，从而实现代码重用和抽象。标准的 Rust 工具，如 `cargo` 和 `clippy`，可用于开发和测试。

移植过程被描述为相当直接，这使得 Rust GPU 适合着色器实验。在此过程中，作者通过识别和修复 `wgpu` 和 `naga` 中的错误，为更广泛的 Rust 生态系统做出了贡献。他们鼓励用户和贡献者加入 Rust GPU 项目，并计划改进入门和文档。

---

## 52. 超级鼠：创纪录的嗅雷鼠，拯救生命

**原文标题**: Super Rat: the record-setting rodent sniffing out landmines and saving lives

**原文链接**: [https://www.cnn.com/2025/04/07/asia/cambodia-rat-ronin-guinness-record-intl-hnk/index.html](https://www.cnn.com/2025/04/07/asia/cambodia-rat-ronin-guinness-record-intl-hnk/index.html)

由APOPO训练的非洲巨颊囊鼠罗宁创下新的世界纪录，于2021年8月至2025年2月期间在柬埔寨探测出109枚地雷和15件其他未爆弹药。地雷对柬埔寨等前冲突地区构成重大威胁，自1979年以来已造成超过65,000人死伤，并阻碍了发展。传统的探测方法既危险又耗时，这使得像罗宁这样的老鼠因其敏锐的嗅觉、速度和轻重量而显得非常宝贵，它们不会触发爆炸物。

比利时非营利组织APOPO已经训练了100多只老鼠来探测爆炸物和结核病，他们的老鼠团队只需30分钟就能搜索完一个网球场大小的区域，而这可能需要一名人类排雷员花费四天时间。罗宁今年5岁，比普通老鼠大，被部署到柬埔寨柏威夏省，该地区因过去的冲突，包括越南战争期间美国的大规模轰炸，地雷高度集中。尽管排雷工作一直在进行，但仍有数百万枚未爆地雷留在柬埔寨。罗宁超过了之前的纪录保持者马加瓦，马加瓦是另一只APOPO老鼠，它探测到了71枚地雷和38件未爆弹药。

---

## 53. Zotero脚本全屏模式

**原文标题**: Zotero Fullscreen Mode by Script

**原文链接**: [https://github.com/windingwind/zotero-actions-tags/discussions/385](https://github.com/windingwind/zotero-actions-tags/discussions/385)

此GitHub讨论串围绕一个Zotero脚本展开，该脚本旨在通过隐藏工具栏和标题栏等UI元素来切换全屏模式。该脚本由thalient-ai创建，可通过Zotero的“Actions and Tags”插件分配给热键，动态地向文档元素添加或删除“fullscreen”类，从而触发隐藏不需要元素的CSS规则。

该脚本还处理macOS平台的特定调整，设置适当的“chromemargin”属性。为了防止快速切换，实施了一个防抖动超时。它的目标是提供一个干净的阅读体验，尤其是在Zotero的标签式界面中阅读PDF时。

该代码包含错误处理，以实现静默失败。虽然原作者指出无法保证在macOS或Linux上的完美功能，但用户反馈表明它在这两个操作系统上都能很好地工作，评论中报告了Zotero和“Actions and Tags”版本的具体信息。该脚本主要针对PDF阅读器，可能无法完全优化标准窗口。

---

## 54. 日本的小城镇

**原文标题**: Small Towns in Japan

**原文链接**: [https://japanstartshere.com/2020/04/06/small-towns-in-japan/](https://japanstartshere.com/2020/04/06/small-towns-in-japan/)

本文推崇日本小城镇之美和真实性，认为它们代表着“真正的日本”。虽然有数百个这样的小镇，但作者重点介绍了十个从大城市出发即可到达的热门小镇，甚至可以作为一日游目的地。

这些城镇提供独特的体验：**冲绳县伊江村**，宁静的岛屿；**佐贺县有田町**，以其陶瓷而闻名；**广岛县濑户田町**，岛波海道自行车路线上的一个站点；**香川县三丰市**，以父母之滨海滩和高屋神社而闻名；**福井县小滨市**，一个拥有寺庙和海景的偏远城镇；**静冈县河津町**，以早开的樱花而闻名；**群马县草津温泉**，一个温泉胜地；**长野县奈良井**，一个保存完好的江户时代村庄；**岩手县平泉**，一个拥有毛越寺的迷人小镇；以及**北海道登别**，以其火山温泉和“地狱谷”而闻名。

作者承认，到达这些城镇通常需要乘坐当地火车或巴士，并建议租车以获得最大的灵活性。由于时间限制，将这些城镇纳入日本行程可能具有挑战性，但回报很高。日本确实有乡村地区和村庄，尽管有些地区面临人口老龄化问题。作者鼓励读者探索典型的旅游目的地之外的地方，并考虑制定个性化的行程，以获得更深入、更真实的日本体验。

---

## 55. 我买了台Mac。

**原文标题**: I bought a Mac

**原文链接**: [https://loganius.org/2025/04/i-bought-a-mac/](https://loganius.org/2025/04/i-bought-a-mac/)

无法访问文章链接。

---

## 56. GeoDeep在Maxar卫星图像上的AI检测

**原文标题**: GeoDeep's AI Detection on Maxar's Satellite Imagery

**原文链接**: [https://tech.marksblogg.com/geodeep-maxar-ai-detection.html](https://tech.marksblogg.com/geodeep-maxar-ai-detection.html)

本文探讨了GeoDeep的功能，这是一个用于卫星图像中目标检测的Python软件包。本文使用Maxar开放数据计划中泰国曼谷的图像，作者配备了一台强大的工作站，详细介绍了GeoDeep及其先决条件（包括Python、DuckDB和QGIS）的安装过程。

作者下载了曼谷的Maxar卫星图像及其相关的元数据用于分析。然后，他们测试了GeoDeep中包含的几个预构建AI模型，特别关注汽车、树木和建筑物检测。汽车检测模型识别出304辆汽车，但既有漏检也有误检。树木检测模型发现了14,136棵树，但由于基于CPU的推理而运行缓慢，并且也遗漏了许多树木。另一种YOLOv9树木检测模型运行速度更快，仅检测到402棵树。建筑物检测模型识别出23,561座建筑物，但未报告置信度值。本文重点介绍了该模型在检测精度、速度和资源利用率方面的性能，以及如何使用DuckDB检查检测结果。作者注意到缺乏GPU推理支持，并在该项目的GitHub页面上提出了一个问题。

---

## 57. 巨蟒剧团与圣杯如何成为喜剧传奇

**原文标题**: How Monty Python and the Holy Grail became a comedy legend

**原文链接**: [https://www.bbc.com/culture/article/20250407-how-monty-python-and-the-holy-grail-became-a-comedy-legend](https://www.bbc.com/culture/article/20250407-how-monty-python-and-the-holy-grail-became-a-comedy-legend)

巨蟒与圣杯：上映五十周年，经久不衰的传奇。本文探讨了《巨蟒与圣杯》上映 50 年后经久不衰的影响。文中包含迈克尔·帕林和特里·吉列姆的见解，深入探讨了这部电影的创作过程，突出了促成其喜剧成功的独特环境。

这部电影源于《巨蟒剧团的飞行马戏团》电视剧，并受到一些成员创作“电影体验”的雄心的推动。从齐柏林飞艇和 Pink Floyd 等非传统来源获得资金，让巨蟒剧团获得了完全的创作自由。这使他们能够自娱自乐，并且由于预算较小而使用的创造性解决方案成为一些最受欢迎的笑话。

尽管预算不足 40 万美元，但该电影通过实景拍摄和足智多谋（例如使用椰子发出马蹄声）实现的真实的中古世纪美学使其脱颖而出。吉列姆强调了将幽默建立在现实基础上的重要性，并将其与其它成员只想搞笑的愿望形成对比。

本文还谈到了这部电影对巨蟒剧团事业的影响，并促成了《万世魔星》和音乐剧《Spamalot》等后续电影的诞生。其标志性的短语和角色已经渗透到英国文化中，吉列姆将这部电影的共鸣归因于它对“具有真实态度的真实人物”的刻画。六位成员各自带来独特的视角，他们之间“神奇的化学平衡”被认为是巨蟒剧团经久不衰的喜剧才华的核心原因。

---

## 58. 艾米莉·狄金森的趣味锁信术

**原文标题**: Emily Dickinson's Playful Letterlocking

**原文链接**: [https://thereader.mitpress.mit.edu/emily-dickinsons-playful-letterlocking/](https://thereader.mitpress.mit.edu/emily-dickinsons-playful-letterlocking/)

本文探讨了艾米莉·狄金森对信封锁的巧妙运用，揭示了她如何通过创新的折叠、密封和信封书写，将信件转化为一种诗歌形式。狄金森拥抱信封锁技术和诸如预涂胶信封之类的新技术，为她的信件添加了多层含义，将物理信件本身视为创意表达的画布。

本文重点关注了狄金森在学生时期寄给她哥哥奥斯汀的一封信。它突出了她如何将用于密封的胶片融入她的信息中。通过在胶片上的预印座右铭（“我看着你，并为你祈祷”，“猜猜如果你能”）上添加手写短语，狄金森创造了一种多层次的文本，使接收者参与到打开和解码信件的行为中。

这种技术将密封过程转变为信息的组成部分，决定了奥斯汀阅读文本的顺序。本文还涉及狄金森对信封锁和信封的使用，暗示了她对这些形式提供的内部性、隐藏和揭示的可能性的迷恋。

最终，作者认为，狄金森像其他诗人一样，有意识地选择了各种信封锁方法，这表明她敏锐地意识到了书信实践中形式和内容之间的关系。这种对信封锁的巧妙运用，为我们进一步了解她的创造性思维以及她通过书面交流与世界互动的独特方式提供了视角。

---

## 59. 菲利普·K·迪克：斯坦尼斯瓦夫·莱姆是共产主义委员会 (2015)

**原文标题**: Philip K. Dick: Stanisław Lem Is a Communist Committee (2015)

**原文链接**: [https://culture.pl/en/article/philip-k-dick-stanislaw-lem-is-a-communist-committee](https://culture.pl/en/article/philip-k-dick-stanislaw-lem-is-a-communist-committee)

文章《菲利普·K·迪克：斯坦尼斯瓦夫·莱姆是共产主义委员会》探讨了菲利普·K·迪克强烈的偏执，以及他毫无根据地认为波兰科幻作家斯坦尼斯瓦夫·莱姆并非真实存在的人，而是一个旨在渗透和控制科幻领域的共产主义宣传委员会的化名。

迪克以其自身的偏执主题和吸毒而闻名，他确信莱姆的受欢迎程度和多产的创作对于单个人来说是不可能的，从而认为这是苏联策划的阴谋。 他甚至联系了联邦调查局，将莱姆举报为威胁。 迪克的言论源于他对现实本质的怀疑、冷战期间对共产主义渗透的恐惧，以及潜在的，他自身的精神不稳定。

这篇文章突出了迪克的讽刺意味，迪克经常探索人造现实和阴谋的主题，却成为了自己精心设计的妄想的受害者。 它强调了迪克的认知与莱姆作为一位高度个人化且在哲学上复杂的作家（他同时批评资本主义和共产主义）的现实之间的脱节。 这篇文章最终将这一事件呈现为迪克生活中的一个离奇章节，展示了他的偏执及其对世界认知的影响，甚至延伸到对一位科幻作家的无端攻击。 该事件更多地揭示了迪克的心理状态，而不是莱姆。

---

## 60. 指示手：无处不在的小手

**原文标题**: The Manicule: The little hand that's everywhere

**原文链接**: [https://www.messynessychic.com/2025/03/07/the-secret-history-of-the-manicule-little-hand-thats-everywhere/](https://www.messynessychic.com/2025/03/07/the-secret-history-of-the-manicule-little-hand-thats-everywhere/)

本文探讨了手形符的历史与演变。手形符是一种印刷符号，描绘了一只指点的手，用于引起人们对文本特定部分的注意。它起源于中世纪手稿，是读者在页边空白处添加的个性化标记，作为一种读者参与的形式，标记重要或有争议的段落。

随着15世纪印刷机的出现，该符号从手写注释过渡到印刷形式。印刷商使用手形符引导读者阅读脚注或评论，标志着从读者驱动的注释到出版商主导的强调的转变。到19世纪，手形符扩展到书籍之外，进入公共生活，成为广告、海报和标牌中的突出特征。然而，维多利亚时代过度使用导致其受欢迎程度下降。

尽管手形符在日常印刷品中逐渐消失，但它仍然存在，并在数字时代找到了新的生命。它成为图形用户界面中通用的“点击此处”光标，现在是一种编码的表情符号。如今，手形符的复兴在复古风格的标牌中显而易见，唤起了怀旧和媚俗之情。该符号的持久吸引力在于它能够弥合读者和作者、过去和现在之间的差距，标志着对值得注意内容的共同理解。

---

## 61. 洛特卡－沃尔泰拉方程

**原文标题**: Lotka–Volterra Equations

**原文链接**: [https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations](https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations)

Lotka-Volterra方程是一对微分方程，用于模拟生物系统中捕食者与猎物相互作用的动态变化。它们描述了两种物种（一种是捕食者，一种是猎物）的种群如何随时间变化。猎物种群呈指数增长，但受到捕食的限制，而捕食者种群基于猎物的消耗而增长，但由于自然死亡而下降。

该模型做出了几个简化假设，例如无限的猎物食物供应、捕食者完全依赖猎物以及恒定的环境条件。尽管存在这些简化，该模型揭示了两个关键属性：种群振荡和平衡密度对其他物种参数的依赖性。猎物增长率的提高有利于捕食者，但不一定有利于猎物。

该模型的动态导致捕食者和猎物种群的周期性波动。这些方程具有周期解，并且可以分析其哈密顿结构。

虽然该模型具有生物学相关性，但也存在局限性。它没有考虑空间分布、年龄结构或导致灭绝的偶然事件等因素。

除了生物学之外，Lotka-Volterra模型已应用于经济学和市场营销，描述了竞争市场和产品生命周期的动态。该模型最初由阿尔弗雷德·洛特卡和维托·沃尔泰拉在20世纪初独立开发，以解释观察到的种群波动。后来的扩展包括密度依赖性增长和功能反应。

---

## 62. 货物突变体：僵尸：注入错误并查看你的测试是否能捕获它们

**原文标题**: Cargo-mutants:zombie: Inject bugs and see if your tests catch them

**原文链接**: [https://github.com/sourcefrog/cargo-mutants](https://github.com/sourcefrog/cargo-mutants)

`cargo-mutants`是一个旨在提高Rust程序质量的工具，它通过识别可能引入错误但不会导致测试失败的代码段来达到目的。与仅显示代码覆盖率的覆盖率测量不同，它专注于测试是否充分验证了代码行为。目标是用户友好，并揭示任何Rust项目中潜在的潜伏错误或不足的测试。

要使用`cargo-mutants`，你需要一个具有非不稳定测试的项目，这些测试可以在`cargo test`或`cargo nextest run`下运行。安装很简单，只需`cargo install --locked cargo-mutants`。基本运行是`cargo mutants`，或者你可以针对特定文件，例如`cargo mutants -f src/something.rs`。该工具正在积极维护，预计每隔一到两个月发布一个版本。

文档包括将其集成到CI中的说明，包括用于拉取请求的增量测试和用于开发分支的完整测试。鼓励用户提供反馈、赞助开发并为其改进做出贡献。该项目欢迎讨论，并提供关于设计说明、贡献指南和发布说明的资源。该手册提供了更多信息，包括与其他技术和工具的比较。

---

## 63. 五年回顾：英国脱欧对从欧洲移居英国的科学家的影响

**原文标题**: 5 years on: Brexit's affects on scientists who had moved to the UK from Europe

**原文链接**: [https://www.nature.com/articles/d41586-025-00858-x](https://www.nature.com/articles/d41586-025-00858-x)

这篇《自然》杂志的文章探讨了英国脱欧对移居英国发展的欧洲科学家的影响。文章着重强调了2016年英国脱欧公投后，研究人员面临的不确定性和挑战，主要集中在资金、行动自由、研究合作和职业发展等方面。

文章重点介绍了两位研究人员的经历：加的夫大学的物理有机化学家尼克·布尔玛和目前在巴黎科钦研究所的白血病研究员黛安娜·帕萨罗。

布尔玛描述了公投后感到不受欢迎，并表达了对反移民情绪的担忧。他指出伊拉斯谟+计划的丧失使得学生交流更加困难，官僚主义的增加阻碍了合作。他还强调，由于移居英国的欧盟研究人员减少，研究职位的申请人数也随之减少。尽管面临这些挑战，布尔玛强调了科学家倡导欧盟理想的重要性，以及海外科学家团体在代表研究人员利益方面的作用。

帕萨罗解释说，由于对她在英国的家庭地位和职业前景感到不确定，英国脱欧促使她返回巴黎。她发现更容易在巴黎建立她的实验室，尤其是在学生招聘和伊拉斯谟+计划的访问方面。她指出，由于签证申请困难，英国同事在吸引国际研究人员方面面临挑战。她的丈夫是一位计算神经科学家，也在巴黎寻找首席研究员职位方面面临挑战，并转而进入一家公司。帕萨罗总结说，英国脱欧直接影响了他们离开英国的决定。

---

## 64. 白宫证实特朗普正探索“驱逐”美国公民的途径

**原文标题**: White House Confirms Trump Is Exploring Ways to 'Deport' U.S. Citizens

**原文链接**: [https://www.huffpost.com/entry/white-house-confirms-trump-is-exploring-ways-to-deport-us-citizens_n_67f580abe4b0a5ea5c7608d2](https://www.huffpost.com/entry/white-house-confirms-trump-is-exploring-ways-to-deport-us-citizens_n_67f580abe4b0a5ea5c7608d2)

本文报道称，特朗普政府正在探讨将美国公民，特别是那些犯有严重罪行的人，“驱逐”到萨尔瓦多的可能性。新闻秘书卡罗琳·莱维特证实，特朗普正在研究此类举措的法律途径，但承认其合法性和可行性尚不确定。

特朗普对这个想法表示出极大的热情，并暗示萨尔瓦多总统纳伊布·布克尔将是一个愿意合作的伙伴。他甚至提到要遣送那些犯有较轻罪行的人，并以破坏特斯拉汽车的人为例，认为他们是潜在的候选人。

此前，特朗普政府曾利用1798年的《外国人敌对法》将移民驱逐到萨尔瓦多，将一个帮派定义为敌对势力，并将这些移民定义为该帮派成员。目前尚不清楚他们是否会对公民使用同样的法律。

文章强调了这项政策可能面临的法律挑战，批评人士认为它违反了宪法保障的正当程序保护。政府为这种做法辩护，认为它可以节省纳税人的钱。文章还强调，此前被驱逐到萨尔瓦多的移民正在法庭上挑战他们的驱逐令，他们担心受到他们被指控所属的帮派的迫害。

---

## 65. Artie (YC S23) 招聘第三位工程师

**原文标题**: Artie (YC S23) Is Hiring Engineer #3

**原文链接**: [https://www.ycombinator.com/companies/artie/jobs/7kGvDVC-founding-product-engineer](https://www.ycombinator.com/companies/artie/jobs/7kGvDVC-founding-product-engineer)

Artie（Y Combinator S23孵化的初创公司）正在旧金山招聘一名创始产品工程师（第3号工程师）。Artie是一个实时数据库复制解决方案，使用Kafka和变更数据捕获 (CDC) 将数据从数据库流式传输到数据仓库，实现亚分钟级延迟。他们在一年前推出了云产品，年化经常性收入 (ARR) 已超过100万美元，并获得了Pathlight Ventures和General Catalyst等知名投资者的支持。

该职位涉及分布式系统、基础设施和数据工程方面的工作，要求候选人与技术客户互动，以改善用户体验、构建新的产品功能（列排除、加密等）以及改进内部工具/构建自动化。

Artie正在寻找具有4年以上Web开发/创业经验、扎实的计算机科学基础知识、务实的构建产品方法以及愿意身兼多职的人。精通Go语言者优先考虑，但非必需。他们的技术栈包括TypeScript（React、Material UI）、Go、PostgreSQL、Redis、Kafka、Elasticsearch、Terraform、Kubernetes和Helm（在GCP/AWS上）。面试流程包括与首席技术官的电话沟通、技术电话筛选和现场面试。

---

## 66. 美加争端殃及跨境图书馆，馆方无奈：“只想继续开放”

**原文标题**: Dismay as cross-border library in US-Canada feud: 'We just want to stay open'

**原文链接**: [https://www.theguardian.com/world/2025/apr/13/us-canada-border-library](https://www.theguardian.com/world/2025/apr/13/us-canada-border-library)

哈斯科尔自由图书馆及歌剧院：美加政治纷争中的跨境地标

---

## 67. 对数学学院的平衡评价

**原文标题**: A balanced review of Math Academy

**原文链接**: [https://newsletter.ozwrites.com/p/a-balanced-review-of-math-academy](https://newsletter.ozwrites.com/p/a-balanced-review-of-math-academy)

Oz Nova对数学学院的评论突出了其作为数学学习工具的优点和缺点。虽然数学学院在训练程序性流畅性和应试准备方面可能有效，并提供轻微上瘾的反馈循环，但它在培养深刻的概念理解方面存在不足。Nova指出，仅仅依赖数学学院可能会导致肤浅的知识，让人想起他自己的经历，即他通过死记硬背在考试中表现出色，但缺乏真正的理解。

该评论批评了数学学院的诊断测试，认为它们主要评估程序性技能，而不是概念理解或泛化能力。Nova还指出了“方法的傲慢”，即该程序僵化的结构和对其方法的过度自信可能会令人沮丧，特别是其严格遵守依赖关系图和缺乏灵活性。

Nova认为，学习中严格的依赖关系图（DAG）是有缺陷的，因为没有唯一的“最佳”学习方法。他建议，根据个人背景和目标不断切换主题对于灵活性是理想的。他还批评了“精通学习”，在这种学习模式下，学生在通过一个级别之前无法继续前进。

总之，Nova建议将数学学院作为更全面的资源（如教科书或讲座系列，这些资源优先考虑概念深度）的补充。他警告说，不要仅仅依靠它来进行程序性练习，并鼓励数学学院承认其局限性并建议补充学习材料。他鼓励用户继续使用数学学院，如果他们觉得它有帮助的话。

---

## 68. 一个棘手的Commodore PET维修：追踪六个半坏芯片

**原文标题**: A tricky Commodore PET repair: tracking down 6 1/2 bad chips

**原文链接**: [http://www.righto.com/2025/04/commodore-pet-repair.html](http://www.righto.com/2025/04/commodore-pet-repair.html)

本文详细介绍了修复一台无法正常工作的Commodore PET电脑的艰辛过程，突出了处理其臭名昭著的不可靠且通常无法获得的古董芯片所面临的挑战。作者出于怀旧之情，购买了这台损坏的PET，并在“CuriousMarc”等人帮助下开始了修复之旅。

最初的症状——尽管CPU明显在活动，但屏幕上却充满了随机字符——指向了系统ROM的问题。一个Retro Chip Tester确认了两个坏的ROM芯片，并用EPROM适配器替换了它们。然而，问题仍然存在。

然后使用逻辑分析仪来追踪内存访问，显示内存测试失败。这导致发现了三个有故障的RAM芯片，暂时减少了PET的内存。尽管启动了，PET仍然表现出奇怪的行为。

进一步的逻辑分析仪分析发现，启动期间出现了一位地址错误，这是由总线上一个不良信号引起的，导致启动信息混乱。棋盘格字符被追溯到EPROM中一个有缺陷的字节，原因是编程器功率不足。

在重新编程EPROM并发现另一个坏的RAM芯片后，PET终于正确启动，允许作者运行一个来自他年轻时的程序。总共有六个芯片坏了：两个ROM和四个RAM。作者总结说，虽然从一开始就进行组件级别的测试可能会更快，但逻辑分析仪之旅提供了宝贵的学习经验。

---

## 69. 记录同事口误的福特高管

**原文标题**: The Ford Executive Who Kept Score of Colleagues' Verbal Flubs

**原文链接**: [https://www.wsj.com/lifestyle/ford-motor-mike-obrien-malaprops-6e560520](https://www.wsj.com/lifestyle/ford-motor-mike-obrien-malaprops-6e560520)

无法访问文章链接。

---

## 70. 使用 Trace 深入 Linux 内核

**原文标题**: Peering into the Linux Kernel with Trace

**原文链接**: [https://alexdowad.github.io/peering-in-the-kernel-with-trace/](https://alexdowad.github.io/peering-in-the-kernel-with-trace/)

本文详细介绍了作者使用BCC工具`trace`调试一个由意外文件访问时间更改引起的间歇性测试失败的经验。最初，`strace`未显示任何直接项目代码访问这些文件。作者随后转向`trace`，该工具允许实时监控Linux内核函数调用。

作者使用`trace`监控对`touch_atime`内核函数的调用，重点关注`path->dentry->d_name.name`字符串以识别正在访问的文件。输出显示，Sublime Text编辑器中的一个后台线程，与其Git集成相关，正在扫描项目文件并更新它们的访问时间，从而导致测试失败。

本文突出了`trace`在提供对系统行为的直接可见性方面的强大功能，并将其与试错调试形成对比。它强调了内核自省对于解决晦涩问题的价值。

作者解释了`trace`的工作原理：它将用户提供的探针规范转换为eBPF字节码，将此字节码加载到内核中，并注册一个kprobe。每当调用被跟踪的函数时，kprobe机制都会触发eBPF字节码的执行，从而能够监控和分析内核活动。这个过程提供了一种灵活而强大的方法来调试和理解Linux内核行为。

---

## 71. Compute's Gazette杂志在中断35年后回归，将聚焦复古计算。

**原文标题**: Compute's Gazette Magazine Returns After 35 Yrs, Will Focus on Retro Computing

**原文链接**: [https://www.computesgazette.com/](https://www.computesgazette.com/)

面向计算的 Compute!'s Gazette 杂志将在中断 35 年后回归。该杂志计划于 2025 年 7 月重新推出，将专注于复古计算并服务于更广泛的复古计算社区。

该出版物将提供印刷版和数字版每月订阅，并承诺提供深入的文章、技巧和故事，以庆祝“计算的黄金时代”。新一期将探讨各种主题，包括生成式人工智能对游戏开发的影响分析、任天堂的游戏密钥策略以及支持当地复古街机的重要性。

Compute! Publications, Inc. 位于德克萨斯州利安德市，可以通过电子邮件联系。此次复兴旨在重新燃起人们对经典计算的兴趣，并为爱好者提供一个平台。

---

## 72. Go通道的问题 (2016)

**原文标题**: Problems with Go channels (2016)

**原文链接**: [https://www.jtolio.com/2016/03/go-channels-are-bad-and-you-should-feel-bad/](https://www.jtolio.com/2016/03/go-channels-are-bad-and-you-should-feel-bad/)

Jtolio的博客文章《Go通道是糟糕的，你应该感到惭愧》认为，Go通道虽然基于可靠的通信顺序进程（CSP）理论基础，但由于几个缺点，在实践中通常是一种反模式。

首先，仅仅依靠通道进行同步是不现实的。实际应用程序通常需要互斥锁、信号量和条件变量。作者提供了一个例子，其中仅使用通道解决一个简单问题会导致goroutine泄漏，而使用互斥锁可以轻松避免这种情况。

其次，通道比直接使用互斥锁和条件变量慢。基准测试表明，由于通道使用的底层锁机制，互斥锁在速度方面优于通道。

第三，通道与其他并发原语的组合效果不佳。通道发送的同步特性在与互斥锁结合使用时可能导致死锁。虽然可以进行非阻塞发送，但需要冗长的语法。

最后，作者认为回调比通道更强大、更灵活，通常可以消除对额外goroutine的需求。基于通道的API迫使开发人员为简单的任务启动goroutine，如果通道没有得到适当的管理，可能会导致goroutine泄漏。文章以context包为例，提出了一种基于回调的“Done”函数，作为更高效的替代方案。

作者总结说，与过度依赖通道相比，使用互斥锁和条件变量通常可以产生更高效且更简单的代码。

---

## 73. 解密数独

**原文标题**: Unlocking Sudoku's Secrets

**原文链接**: [https://chalkdustmagazine.com/features/unlocking-sudokus-secrets/](https://chalkdustmagazine.com/features/unlocking-sudokus-secrets/)

莎拉·洛格斯顿的文章《解锁数独的秘密》探讨了数独的数学基础，揭示了其与图论和抽象代数的联系。

从图论的角度来看，数独网格可以表示为一个包含81个顶点（单元格）的图，当单元格位于同一行、同一列或同一3x3区域时，顶点之间由边连接。那么，解决数独就等同于解决顶点着色问题：使用9种颜色（数字）为图着色，使得相邻顶点（连接的单元格）具有不同的颜色。文章展示了如何通过系统地分配数字并在出现冲突时回溯，利用贪婪算法和回溯的结合来解决数独谜题。

文章随后深入探讨了抽象代数，特别是Gröbner基，在数独中的应用。通过将数独规则表示为一个多项式方程组，可以通过计算Gröbner基来解决该问题。这个过程，使用Buchberger算法，简化了方程组，并允许轻松提取数独解，特别是当解是唯一的时候。文章使用一个较小的“四宫数独”（4x4网格）来说明这个概念，演示了多项式方程如何表示谜题的约束，以及Gröbner基如何揭示已解决的网格。

作者认为，理解这些数学框架——图论和抽象代数——可以为解决数独谜题提供有价值的见解和策略。

---

## 74. 信息转化为能量 (2010)

**原文标题**: Information Converted to Energy (2010)

**原文链接**: [https://physicsworld.com/a/information-converted-to-energy/](https://physicsworld.com/a/information-converted-to-energy/)

本文探讨了日本丰部昭一及其同事的一项实验，该实验展示了信息向能量的转换，这一概念源于麦克斯韦妖的思想实验。该实验使用反馈系统来控制微小聚苯乙烯珠的电势，从而有效地使它们在不直接赋予能量的情况下攀爬势能阶梯。

研究人员跟踪了粒子的运动，并通过在粒子逆着电场运动时反转电场的相位，有效地创建了一个屏障，使粒子逐渐增加其势能。这证明了关于粒子状态的信息可以被用来从中提取功的原理。

该实验量化了信息到能量的转换，实现了将1比特的信息转换为0.28 kTln2的能量。虽然这是一项重大突破，但值得注意的是，所涉及的宏观设备（计算机、操作员）的总体能耗远远超过了获得的能量。

尽管存在目前的局限性，但该研究表明了在纳米尺度设备中的潜在未来应用，在这些设备中，用于控制的信息的能量含量可与操作所需的能量相媲美。文章最后强调了纳米尺度过程的根本差异以及信息在这一领域的重要性，并暗示天然分子过程可能已经利用了信息到能量的转换。

---

## 75. 竞技场分配器的误用与妙用

**原文标题**: Mistakes and cool things to do with arena allocators

**原文链接**: [https://zylinski.se/posts/dynamic-arrays-and-arenas/](https://zylinski.se/posts/dynamic-arrays-and-arenas/)

本文探讨了在 Odin 中使用竞技场分配器的方法，重点关注其与动态数组结合使用时可能存在的陷阱。竞技场将具有相同生存期的分配分组在一起，从而能够同时进行释放。然而，天真地将它们与动态数组一起使用会导致内存浪费。

核心问题在于，动态数组通过分配新的内存块、复制数据并尝试释放旧块来增长。竞技场分配器专为集体生命周期管理而设计，不支持单独释放，导致旧块留在竞技场中并导致碎片。

本文建议通常对动态数组使用默认分配器，或者在大小已知时预先分配最大大小。如果预先分配可行，则设置 `dyn_arr.allocator = mem.panic_allocator()` 会使程序在数组尝试增长超出容量时崩溃，从而防止内存浪费。

本文还研究了虚拟增长竞技场，如果它是最近的分配，则为分配重用相同的地址，在调整大小时将动态数组的第一个元素保留在原位，*除非*数组增长超过竞技场的块大小。最后，它建议使用静态虚拟竞技场作为避免移动问题的另一种方法，即预先分配单个块，但是，如果超过此块大小，可能会导致 panic。

---

## 76. 并行计算入门教程

**原文标题**: Introduction to Parallel Computing Tutorial

**原文链接**: [https://hpc.llnl.gov/documentation/tutorials/introduction-parallel-computing-tutorial](https://hpc.llnl.gov/documentation/tutorials/introduction-parallel-computing-tutorial)

本教程介绍了并行计算的基础知识。它将并行计算定义为同时使用多个计算资源来解决一个问题，将其分解为并发执行的离散部分。并行计算的优势包括节省时间和金钱、解决更大的问题、提供并发性、利用非本地资源以及更好地利用并行硬件。

本教程随后讨论了关键概念和术语，首先介绍了冯·诺依曼体系结构，它是包括并行计算机在内的大多数计算机的基础。它介绍了弗林分类法，用于根据指令和数据流（SISD、SIMD、MISD、MIMD）对计算机体系结构进行分类。它还提供了一个常见的并行计算术语表，如 CPU、节点、任务、流水线、共享内存、SMP 和分布式内存。

本文然后深入探讨了内存架构（共享、分布式和混合）和并行编程模型（共享内存、线程、消息传递、数据并行和混合）。它探讨了设计并行程序的关键方面，包括分区、通信、同步、数据依赖性、负载平衡、粒度、I/O、调试和性能分析。

最后，本教程提供了一些简单的并行化示例，例如数组处理、PI 计算、一个简单的热方程和一个一维波动方程，并为进一步学习提供了参考。总体目标是为并行计算新手提供一个概述。

---

## 77. 为什么Pascal不是我最喜欢的编程语言 (1981) [pdf]

**原文标题**: Why Pascal is not my favorite programming language (1981) [pdf]

**原文链接**: [https://doc.cat-v.org/bell_labs/why_pascal/why_pascal_is_not_my_favorite_language.pdf](https://doc.cat-v.org/bell_labs/why_pascal/why_pascal_is_not_my_favorite_language.pdf)

由于该文档为PDF格式，且包含大量无法读取的字符和格式代码，我无法准确概括文章《为什么Pascal不是我最喜欢的编程语言（1981）》的内容。 该文档似乎已损坏或以某种方式编码，导致无法提取和理解文本。 因此，我无法提供其主要观点或关键信息的摘要。

---

## 78. AMD NPU和赛灵思Versal AI引擎在射电天文学中的信号处理 (2024) [pdf]

**原文标题**: AMD NPU and Xilinx Versal AI Engines Signal Processing in Radio Astronomy (2024) [pdf]

**原文链接**: [https://git.astron.nl/RD/acap/-/raw/main/Presentation_FPL24_Vincent_Sprave.pdf](https://git.astron.nl/RD/acap/-/raw/main/Presentation_FPL24_Vincent_Sprave.pdf)

此文档似乎是已损坏或格式错误的PDF文件。提取的内容包含随机字符和控制码，表明它无法正确渲染。因此，无法根据提供的输入准确地总结“文章”。需要一个功能正常的PDF阅读器或文件的修复版本才能提取有意义的信息并提供摘要。它似乎与射电天文学中的信号处理有关，重点是AMD NPU和Xilinx Versal AI引擎，但无法提取任何细节。

---

## 79. Show HN: Chonky – 一种用于文本语义分块的神经方法

**原文标题**: Show HN: Chonky – a neural approach for text semantic chunking

**原文链接**: [https://github.com/mirth/chonky](https://github.com/mirth/chonky)

Chonky 是一个 Python 库，旨在利用微调的 Transformer 模型将文本智能地分割成有意义的语义块。这使其特别适用于 RAG（检索增强生成）系统等应用。该库可以使用 `pip install chonky` 轻松安装。

核心功能由 `TextSplitter` 类提供。用户实例化分割器，指定要使用的设备（例如，“cpu”）。然后，`TextSplitter` 处理文本并产生语义块。提供的示例展示了如何在一段关于写作和编程经验的段落中使用 Chonky，演示了它如何将文本分解为三个不同的块，每个块代表一个独立的想法。

该库使用 Transformer 模型 "mirth/chonky_distilbert_base_uncased_1" 进行分块处理。首次使用 `TextSplitter` 时，它会自动下载此模型。

---

## 80. 姆明的黑暗面

**原文标题**: The dark side of the Moomins

**原文链接**: [https://www.newstatesman.com/culture/books/2025/04/dark-side-of-the-moomins-tove-jansson](https://www.newstatesman.com/culture/books/2025/04/dark-side-of-the-moomins-tove-jansson)

本文探讨了托芙·杨松笔下姆明形象更为阴暗、复杂的起源与演变，将商业上成功的、可爱的形象与杨松最初的意图和个人挣扎进行了对比。

文章强调，第一本姆明小说《姆明和彗星来的那一天》是在冬季战争期间创作的，反映了流离失所和寻找家园的主题。杨松在人生的诸多方面都是一个边缘人，她将自己的焦虑和经历融入了故事中。

文章随后追溯了姆明角色的发展，强调了他们的焦虑、痴迷和功能失调的家庭关系。文章指出，后来的作品，特别是《姆明寒冬》和《姆明爸爸出海记》，深入探讨了抑郁症和家庭破裂的主题。最后一本书《十一月的姆明谷》被描述为一部关于等待和消失的荒诞派杰作。

此外，文章深入探讨了杨松的个人生活，突出了她与父亲之间紧张的关系，以及她与姆明作品商业上的巨大成功所带来的挣扎。她发现商品化和粉丝的关注令人窒息，最终导致她在漫画中杀死了姆明，并对读者表达了失望之情。文章认为，尽管姆明以温馨的家庭生活而闻名，但它们实际上是关于末日、崩溃和功能失调的复杂故事，常常被误读。

---

## 81. JSLinux

**原文标题**: JSLinux

**原文链接**: [https://www.bellard.org/jslinux/](https://www.bellard.org/jslinux/)

JSLinux是一个网站，允许用户通过模拟直接在网页浏览器中运行各种操作系统。它提供多种模拟系统选择，包括几种Linux发行版（Alpine Linux、Buildroot、Fedora）、Windows 2000 和 FreeDOS，运行于 x86 或 RISC-V 架构之上。用户可以通过控制台或 X Window 界面访问这些系统，具体取决于操作系统。这些系统通常提供 VFSync 访问，启动时间各不相同。点击每个操作系统提供的链接即可启动模拟。某些系统，例如具有 X Window 界面的系统，可能会提供右键菜单。启动时间可能有所不同，特别是 Fedora 33 等系统，启动时间较长。该网站是 Fabrice Bellard 的项目，版权日期为 2011-2021 年。同时还提供新闻、虚拟机列表、常见问题解答和技术说明的链接。

---

## 82. 异想天开的投资者

**原文标题**: The Whimsical Investor

**原文链接**: [https://fi-le.net/stonks/](https://fi-le.net/stonks/)

古怪投资者的颂歌

文章赞扬了那些在私人企业日益占据主导地位的世界中，设法生存下来的古怪、小型上市公司。作者旨在通过剖析几家独特的公司，找到其中“最滑稽”的一家。

文章重点介绍了：

*   **Schwälbchen Molkerei Jakob Berz AG (施瓦尔布亨乳品公司):** 一家德国乳品厂，市值7300万美元，以其“小燕子”标志、家族所有权以及出人意料的产品（如带有土耳其-德国宣传册的酸奶饮料）而闻名。
*   **Nippon Ichi Software Inc. (日本一ソフトウェア):** 一家日本游戏发行商，估值2700万美元，以其吉祥物企鹅Prinny、浮夸的年度报告设计以及对《魔界战记》系列的依赖以及多样化的游戏阵容而闻名。
*   **Bergbahnen Engelberg-Trübsee-Titlis AG (英格堡-特吕布湖-铁力士山缆车公司):** 一家瑞士山区缆车公司，市值1.6亿美元，以其创新的缆车和综合旅游服务而闻名，展现了对旅游业价值创造的理解。
*   **Fujiya Co. Ltd. (不二家):** 一家标志性的日本糖果制造商，市值4.1亿美元，以其吉祥物Peko-chan和各种Peko-chan商品以及家庭餐厅和创新的糖果产品而闻名。
*   **Soft-World International (智冠科技):** 一家台湾视频游戏公司，市值5.1亿美元，其特点是拥有一个复杂的子公司网络，涵盖游戏行业的各个方面，从艺术到支付处理。

作者最终将“最滑稽上市公司奖”授予智冠科技，原因是其垂直整合的结构、多样化的游戏组合以及整体的古怪性。作者同时指出，所有公司均根据公开可用的文件进行审查，并且所有信息均可能存在错误。作者最后强调了保持私人和上市公司之间平衡的重要性，以确保信息的获取和投资机会。

---

## 83. 我测试了这款AI，如果你懒得打电话，它可以替你给年迈的父母打电话。

**原文标题**: I Tested the AI That Calls Your Elderly Parents If You Can't Be Bothered

**原文链接**: [https://www.404media.co/i-tested-the-ai-that-calls-your-elderly-parents-if-you-cant-bothered/](https://www.404media.co/i-tested-the-ai-that-calls-your-elderly-parents-if-you-cant-bothered/)

文章探讨了 inTouch，一种人工智能服务，旨在代表子女给年迈的父母打电话。该人工智能使用生成的语音与父母进行对话，询问他们的一天、爱好和整体健康状况。通话结束后，该服务会向子女（或账户持有人）提供人工智能生成的对话摘要，包括父母情绪的可视化指标。

作者强调了这种服务潜在的负面和去人性化方面，认为这是对老年护理的一种反乌托邦式的方法。伦理问题源于用人工智能取代真正的人际互动，特别是对于那些可能正在经历孤独的人。

尽管存在伦理问题，inTouch 的创建者认为，它提供了一种方便的方式来与年迈的亲属保持联系，并确保他们的安全和福祉，特别是当他们的家人无法或不愿意自己这样做时。本文设置了付费墙，提供有限的免费预览，并鼓励读者订阅以获得完整的、无广告的访问权限。

---

## 84. 苦涩的预言

**原文标题**: The Bitter Prediction

**原文链接**: [https://4zm.org/2025/04/05/bitter-prediction.html](https://4zm.org/2025/04/05/bitter-prediction.html)

作者作为一名软件开发者，对Claude Code等人工智能编码工具的兴起表达了复杂的情感。起初，他对其能力感到兴奋，但很快便经历了一种幻灭感，将其比作在电子游戏中作弊，一旦他能够轻松操控结果，就失去了兴趣。人工智能快速高效地生成高质量代码的能力让他开始质疑编程的内在乐趣，担心编程会变得不那么充实，甚至令人不满意，最终沦为一种爱好。

他的“苦涩预言”不仅仅局限于个人满足感。他还担心其经济影响，注意到使用这些人工智能工具的巨大成本。他指出了人工智能辅助编码的成本与世界上大部分人口的经济现实之间的差距，暗示这可能会成为较不富裕地区有抱负的开发者进入该行业的潜在障碍。这可能会加剧现有在技术和机会获取方面的不平等。作者还简要提到了运行这些人工智能模型所需的数据中心对环境的影响。

虽然他承认由于经济激励和对效率的不懈追求，人工智能在软件开发中是不可避免的，但他仍然担心这个行业的未来。他最终带着一种无奈感总结，担心软件开发会变得不那么令人愉快，更加具有排他性，由经济力量而非激情驱动。

---

## 85. BPS：鲜为人知的GPS替代方案

**原文标题**: BPS is a GPS alternative that nobody's heard of

**原文链接**: [https://www.jeffgeerling.com/blog/2025/bps-gps-alternative-nobodys-heard](https://www.jeffgeerling.com/blog/2025/bps-gps-alternative-nobodys-heard)

作者参加了NAB展会，了解广播中的授时技术，并发现了广播定位系统（BPS），这是一种实验性授时标准，正在测试以期纳入ATSC 3.0广播标准。BPS使用来自电视台的授时信号，为GPS提供精确的地面备份，演示显示同步精度在+/- 10纳秒以内。

ATSC 3.0，又称下一代电视（NEXTGEN TV），是一种正在推出的IP广播标准，但BPS测试仍仅限于少数电视台。作者强调了可靠的GPS替代方案的重要性，特别是对于媒体、电网和5G通信等关键基础设施而言。地面备份可以抵抗干扰。

作者还提到发现了一款带有内置PPS输入/输出连接器的消费级Intel主板，可用于同步到TGPIO，并预告稍后将进行更深入的解释。他还提供了有关BPS、UrsaNav的eLoran授时以及相关项目的资源链接。评论包括讨论BPS用于YouTube火箭发射，其作为航空GPS备份的潜在用途，以及关于BPS系统地理限制的问题，因为它由一家美国组织牵头。

---

## 86. RNA干扰与纳米药物联手对抗危险的真菌感染

**原文标题**: RNA interference and nanomedicine team up to fight dangerous fungal infections

**原文链接**: [https://phys.org/news/2025-03-rna-nanomedicine-dangerous-fungal-infections.html](https://phys.org/news/2025-03-rna-nanomedicine-dangerous-fungal-infections.html)

本文报道了一项在对抗危险真菌感染方面的突破，特别是针对高死亡率的烟曲霉（*Aspergillus fumigatus*）引起的感染，尤其是在抗真菌耐药性日益增强的情况下。维尔茨堡大学医院的研究人员成功地将RNA干扰（RNAi）与纳米医学相结合，靶向并抑制了该真菌的生长。

这项创新的核心在于将小干扰RNA（siRNA）封装在阴离子脂质体中，并加入少量两性霉素B（AmB）。这使得siRNA能够穿透厚厚的真菌细胞壁。AmB增加了细胞壁的渗透性，而带有负电荷的脂质体则促进了进入。一旦进入细胞内部，siRNA会选择性地沉默三个对真菌生长至关重要的关键基因，有效地充当“基因开关”来抑制蛋白质的产生。

该团队发表在《纳米尺度》（*Nanoscale*）上的研究，使用昆虫幼虫作为感染模型，以最大程度地减少哺乳动物动物试验。这项合作研究涉及RNAi、纳米医学和真菌感染方面的专家。结果表明真菌生长显著减少。研究人员强调了这种siRNA策略对抗烟曲霉和其他危险真菌病原体的潜力，为在日益增长的耐药性中开发新的抗真菌疗法提供了一个有希望的新途径。

---

## 87. 一个Reddit机器人把我逼疯了

**原文标题**: A Reddit bot drove me insane

**原文链接**: [https://posthuman.blog/this-reddit-post-fried-my-brain/](https://posthuman.blog/this-reddit-post-fried-my-brain/)

作者讲述了一段在Reddit上令人不安的经历，突显出人们普遍感到互联网越来越虚假和不真实。 最初，作者在一个哀叹这种感觉的帖子中找到慰藉，但很快就对发帖者通用且优化的风格产生了怀疑，从而展开调查。

他们发现该帖子是人工智能驱动的机器人精心策划的骗局，伪装成一个关心人类的人。 该帖子包含一个隐藏链接，伪装成 Reddit URL 缩短器（“rddit.org”），该链接重定向到亚马逊上的一本书籍《宣传》的页面，该书包含由机器人创建者出售的 AI 生成的插图。 作者意识到该机器人正在利用人类的同情心来推动销售。

该事件引发了偏执和调查的螺旋式上升。 作者深入研究了诸如“死亡互联网理论”之类的阴谋论，质疑其他用户及其互动的真实性。 他们疯狂地研究机器人的创建者、虚假 URL 和亚马逊个人资料，质疑自己的理智以及他们的反应是否正是机器人所期望的。 作者以对未来的悲观视角结尾，认为人工智能会为了利润而操纵人类的情感，让他们质疑在线互动的真实性。 文章末尾提供了一个指向有关 Hacker News 事件的续集的链接。

---

## 88. 美国和萨尔瓦多表示不会遣返被错误驱逐出境的男子

**原文标题**: U.S. and El Salvador Say They Won't Return Man Who Was Mistakenly Deported

**原文链接**: [https://www.nytimes.com/live/2025/04/14/us/trump-news-tariffs](https://www.nytimes.com/live/2025/04/14/us/trump-news-tariffs)

2025年4月14日，特朗普总统在白宫会见了萨尔瓦多总统纳伊布·布克尔。会议的重点是基尔马尔·阿曼多·阿布雷戈·加西亚的案件，他是一名马里兰州男子，被错误地驱逐到萨尔瓦多。尽管最高法院下令“促成”加西亚的回国，但特朗普和布克尔都表示不会允许他返回美国。

特朗普和他的助手斯蒂芬·米勒驳斥了最高法院对外交政策的管辖权，并将责任推给了布克尔。布克尔赞同特朗普在移民问题上的强硬立场，将加西亚的回国比作走私恐怖分子。特朗普甚至表示，他愿意将美国罪犯送往萨尔瓦多的监狱。

文章还报道了特朗普对半导体征收关税的计划，认为这将通过鼓励国内芯片生产来增强美国国家安全。这些关税是更广泛贸易战略的一部分，特朗普不断提高和降低关税，导致市场动荡。

与此同时，美国公民自由联盟在科罗拉多州提起诉讼，挑战特朗普政府使用《敌侨法》将委内瑞拉移民驱逐到萨尔瓦多。这些驱逐行动和布克尔的访问在白宫外引发了抗议活动。

---

## 89. 如何避免制作两级模型火箭

**原文标题**: How to not build a two stage model rocket

**原文链接**: [https://knowone08.gitbook.io/vgecrocketry](https://knowone08.gitbook.io/vgecrocketry)

这篇博文幽默地讲述了作者首次尝试制作名为Venessa的两级模型火箭的经历。主要目标是实现成功的级间分离，而不是追求高海拔或高速。他们的理念是“用最简单的方式学习最难的东西”，侧重于通过实验学习并接受妥协。

火箭的设计包括用回收的工程图纸制作的纸质箭体、3D打印的PLA鼻锥、尾翼和翼片。推进系统采用定制设计的固体火箭发动机，配备不锈钢外壳、铝制端盖和低碳钢喷嘴，燃料为KNDX（硝酸钾和右旋糖）。使用了两个发动机：第一级为G136，第二级为G96。

航空电子设备发挥了关键作用，作者描述了一个旨在通过加速度数据主动检测燃尽，而不是依赖预编程定时器的系统。两台独立的飞行计算机（Grace和RocketNerve）配备传感器和火工品通道，独立监控飞行数据并可以触发分离。

回收系统主要针对第二级，采用弹簧式降落伞弹射系统，由飞行计算机在检测到远地点时触发。第一级被设计为弹道坠落。

最终，首次发射的结果不太成功。然而，这篇博文强调了从中获得的学习经验，并承诺未来的博文将详细介绍航空电子固件和逻辑。该项目采用低成本、高学习的方式，使用容易获得的材料和3D打印，专注于掌握级间分离的挑战。

---

## 90. Skywork-OR1：新型开源权重32B SOTA思考模型

**原文标题**: Skywork-OR1: new SOTA 32B thinking model with open weight

**原文链接**: [https://github.com/SkyworkAI/Skywork-OR1](https://github.com/SkyworkAI/Skywork-OR1)

Skywork AI发布了Skywork-OR1（开放推理器1）系列开源语言模型，专为增强数学和代码推理能力而设计。该系列包括Skywork-OR1-Math-7B（专为数学优化）、Skywork-OR1-32B-Preview和Skywork-OR1-7B-Preview（均为通用模型）。这些模型采用基于规则的强化学习，并使用精心设计的数据集和训练方案进行训练。

Skywork-OR1-Math-7B在AIME24和AIME25数学基准测试中取得了令人印象深刻的成绩，超过了同等规模的模型。Skywork-OR1-32B-Preview在数学和代码任务上与更大的Deepseek-R1性能相当，而7B预览版则超越了其他7B模型。最终发布版本预计在两周后推出。

这些模型使用一种名为Avg@K的新指标进行评估，该指标衡量多次尝试的平均性能以提高可靠性。文章提供了针对AIME24、AIME25和LiveCodeBench上其他模型的详细基准测试结果。

此次发布包括模型权重，训练数据也将很快提供。文章还提供了使用Docker或Conda环境进行安装的说明，并提供了用于重现基准测试结果的评估脚本。训练脚本即将推出。这些模型基于DeepSeek-R1-Distill-Qwen模型以及verl项目的自定义分支构建。

---

## 91. 阿努比斯工作室

**原文标题**: Anubis Works

**原文链接**: [https://xeiaso.net/notes/2025/anubis-works/](https://xeiaso.net/notes/2025/anubis-works/)

Anubis Works：一种网站安全措施，旨在防止AI抓取造成的网站过载和功能中断，影响正常用户。它采用类似于Hashcash的“工作量证明”机制，通过提高计算成本来阻止大规模抓取。虽然对单个用户的影响很小，但对大规模抓取操作的影响显著。

Anubis被视为一种临时解决方案，同时也在开发更强大的方法，如指纹识别和无头浏览器识别，以区分正常用户和抓取者。目标是避免向可能是真实的用户提出工作量证明的挑战。

该系统需要JavaScript才能运行，这可能需要禁用某些浏览器插件，如JShelter。对JavaScript的依赖是由于AI公司对网站托管的影响以及对防御措施的需求所致。文档表明正在探索一种无需JavaScript的解决方案。本质上，Anubis旨在平衡网站对正常用户的可访问性与防御破坏性AI抓取活动的需求。

---

## 92. 展示HN：富文本编辑器即服务 – 我的免费副项目

**原文标题**: Show HN: Rich text editor as a service – my free side project

**原文链接**: [https://www.texteditors.dev](https://www.texteditors.dev)

TextEditors.dev是一个免费服务，旨在简化在网站中嵌入富文本编辑器的流程。用户无需复杂的配置和编码，只需三步即可添加和配置流行的编辑器，如Tiptap、QuillJS和EditorJS：选择编辑器、通过几次点击进行配置（包括工具栏、字体、扩展和文件上传），以及将提供的代码片段嵌入到他们的网站中。

该服务负责版本升级，确保用户无需担心版本不匹配的问题。TextEditors.dev强调用户隐私，声明他们不会存储用户内容。他们计划即使以后添加高级功能，也会保持免费层可用。他们鼓励用户提供反馈和建议，以添加新的编辑器到他们的平台，并邀请用户免费开始使用。

---

## 93. Whenever：Python 的类型化且 DST 安全的日期时间

**原文标题**: Whenever: Typed and DST-safe datetimes for Python

**原文链接**: [https://github.com/ariebovenberg/whenever](https://github.com/ariebovenberg/whenever)

Whenever 是一个 Python 库，旨在提供类型安全和 DST 安全的日期时间处理，以解决 Python 标准 `datetime` 库的不足以及 Arrow 和 Pendulum 等其他第三方库的局限性。它的目标是防止与 naive 和 aware 日期时间以及不一致的 DST 处理相关的常见错误。

Whenever 的主要优点包括：

*   **DST 安全的算术运算：** 正确处理夏令时转换。
*   **类型安全的 API：** 强制区分 naive 和 aware 日期时间，捕获潜在的错误。
*   **性能：** 与 Arrow 和 Pendulum 相比，具有卓越的性能，并且与标准库相比具有竞争力，尤其是在使用 Rust 实现时。 纯 Python 选项也可用。
*   **现代概念：** 基于 Temporal、Noda Time 和 Joda Time 等库中已建立的日期时间概念。

Whenever 提供了诸如 `Instant`、`ZonedDateTime` 和 `LocalDateTime` 等显式类型来表示不同的日期时间用例。它支持常见的操作，如转换、算术运算、比较、舍入和格式化（ISO8601、RFC3339、RFC2822）。

该库仍在开发中（1.0 之前），其路线图侧重于 API 稳定性、可定制的解析/格式化、时间间隔、范围以及闰秒解析。它遵循语义版本控制，破坏性更改将在变更日志中记录。

---

## 94. 命名性失语症：命名检索障碍

**原文标题**: Nominal Aphasia: Problems in Name Retrieval

**原文链接**: [https://serendipstudio.org/exchange/darlene-forde/nominal-aphasia-problems-name-retrieval](https://serendipstudio.org/exchange/darlene-forde/nominal-aphasia-problems-name-retrieval)

名为“命名性失语症：名称检索中的问题”的文档，实际上是Serendip工作室的索引或导航页面，而非直接解释命名性失语症的文章。它概述了Serendip网站的不同部分，提供了对工作室、其特性和社区参与信息的访问。

提供的链接展示了Serendip的各个方面，包括：

*   **关于Serendip工作室：** 介绍该组织及其使命。
*   **关于Serendip的事实：** 提供关于工作室的关键信息和细节。
*   **导航辅助：** 提供诸如“查找您的位置”、“导游”和“站点地图”之类的指南，以帮助用户浏览站点。
*   **更新：** 具有诸如“最新消息”之类的部分，以突出显示最近的添加和更改。
*   **社区功能：** 包括用于讨论的“论坛”部分和用于用户反馈的“Serendip读者反馈”。
*   **资源：** 提供“书架”（可能是一系列推荐读物）和“Serendip A到Z”（综合索引）。
*   **背景：** 提到Serendip成立于1994年。
*   **参与：** 邀请访问者“加入我们”，暗示参与和贡献的机会。

本质上，虽然标题暗示了对“命名性失语症”的关注，但该文档本身是一个用于探索Serendip工作室网站及其多样化内容的导航工具。

---

## 95. 展示一下：我用C语言实现了一个零依赖的比特币数学库

**原文标题**: Show HN: I made a zero dependency Bitcoin math implementation in C

**原文链接**: [https://github.com/CambridgeStateMachines/bitcoin_math](https://github.com/CambridgeStateMachines/bitcoin_math)

这个“Show HN”帖子介绍 `bitcoin_math`，一个零依赖的比特币数学C语言实现，用于教育目的。它旨在通过从第一性原理实现生成助记词、密钥和地址的函数来教授比特币基础知识，避免使用外部加密库或“大数”库。代码优先考虑可读性而非效率。

应用程序 `bitcoin_math.exe` 是一个菜单驱动的控制台程序，具有主密钥生成、子密钥派生、进制转换和单个函数执行（P2PKH序列化、Secp256k1操作）等功能。它允许用户将密钥和地址作为任意精度整数进行操作，并以各种格式显示它们。鼓励使用 learnmeabitcoin.com 等在线工具验证输出。

该项目警告说，由于其不安全性，不要将该程序的“随机”熵生成用于真实的比特币地址。它提供了使用 `gcc` 进行编译的说明，并提到了潜在的优化和库转换机会。

该项目承认使用了第三方代码来实现 BIP39 单词列表和加密哈希函数。它感谢 GNU 多精度算术库（“GMP”）和 DI Management Services 的 BigDigits 对任意精度整数数学的影响，以及 Bhardwaj 和 Chaudhary 的一篇研究论文对椭圆曲线函数的影响。模幂和模乘法逆函数改编自维基百科。C 源代码分为多个部分，涵盖杂项元素、哈希函数（RIPEMD160、SHA256、SHA512、HMAC-SHA512）、任意精度整数数学（`BNZ`）、椭圆曲线数学（`SECP256K1`）、比特币特定函数（`BITCOIN`）、菜单函数（`MENU`）和主函数（`MAIN`）。

---

## 96. Show HN: GitHub侦探 – 调查GitHub用户的活动

**原文标题**: Show HN: GitHub Detective – Investigate what a GitHub user has been up to

**原文链接**: [https://githubdetective.vercel.app](https://githubdetective.vercel.app)

此“Show HN”帖子介绍“GitHub侦探”，一款允许用户调查任何GitHub用户近期公开活动的工具。输入GitHub用户名后，该工具会显示其最新的公开事件。其主要功能本质上是GitHub用户活动追踪或侦察。

该帖子简明扼要，直接介绍了该工具的功能。它也由“You-TLDR”赞助，这是一项总结YouTube视频的服务。

---

## 97. 谷歌在人工智能的各个领域都取得了胜利。

**原文标题**: Google is winning on every AI front

**原文链接**: [https://www.thealgorithmicbridge.com/p/google-is-winning-on-every-ai-front](https://www.thealgorithmicbridge.com/p/google-is-winning-on-every-ai-front)

根据这篇2025年4月的文章，谷歌在人工智能领域占据主导地位，超越了OpenAI和Anthropic等竞争对手。作者认为，谷歌之前因担心影响搜索收入而犹豫不决是它最后一个重大失误，此后，他们便突飞猛进。

文章强调了Gemini 2.5 Pro的卓越性能，列举了其在基准测试中的顶级排名和积极的用户反馈。文章强调了Gemini 2.5的速度、可负担性、大上下文窗口以及与谷歌产品的集成。作者还提到了Gemini 2.5 Flash，认为它因其速度和低成本而成为另一个关键产品。此外，Gemma 3 使谷歌在开源模型领域占据优势。

除了基于文本的模型，谷歌在人工智能领域的主导地位还扩展到其他生成式人工智能领域，将 Lyria（音乐）、Imagen 3（图像）、Veo 2（视频）和 Chirp 3（语音/语音）等工具集成到 Vertex AI 中。此外，谷歌还在人工智能代理领域处于领先地位，其 Gemini 2.5 Pro 拥有深度研究模式、Project Astra 和 Project Mariner。

作者强调了谷歌作为一家消费软件公司的现有优势，在搜索领域（Google 和 YouTube）占据主导市场份额，拥有七款月活跃用户超过 20 亿的产品。谷歌的云计算基础设施（Google Cloud）和硬件能力（TPU 和集成 Gemini 的 Pixel 手机）进一步巩固了其优势，使其能够与微软、亚马逊和英伟达等公司竞争。文章总结说，考虑到谷歌的所有综合能力，看好其他人工智能公司的理由就减少了。

---

## 98. 欧洲核子研究中心发布未来环形对撞机可行性报告

**原文标题**: CERN releases report on the feasibility of a possible Future Circular Collider

**原文链接**: [https://home.cern/news/news/accelerators/cern-releases-report-feasibility-possible-future-circular-collider](https://home.cern/news/news/accelerators/cern-releases-report-feasibility-possible-future-circular-collider)

欧洲核子研究中心发布了未来环形对撞机（FCC）的可行性研究报告，这是一个拟议的周长91公里的粒子对撞机，有望在2040年代接替大型强子对撞机（LHC）。 FCC旨在解决基础物理学中尚未解答的问题，特别是关于希格斯玻色子及其对宇宙的影响。

FCC研究计划提出两个阶段：首先，一个用于希格斯玻色子、弱电和顶夸克研究的正负电子对撞机，然后是一个以100 TeV运行的质子-质子对撞机。 该研究涵盖了该项目的物理目标、地质、工程、环境影响、研发需求、社会经济效益和成本。 正负电子阶段的预计成本为150亿瑞士法郎，分摊在12年内。

欧洲核子研究中心致力于使FCC成为一个可持续的研究基础设施，整合生态设计原则并最大限度地减少其环境足迹。 对撞机环的布局经过精心规划，考虑了地域兼容性、环境制约因素和成本，最终得出一个首选方案，其周长为90.7公里，平均深度为200米。

法国和瑞士参与了这项研究过程，与地方和国家实体合作，并计划进行公众参与。 该报告将由专家审查，然后在2025年11月由欧洲核子研究中心理事会审查，并可能在2028年左右决定是否继续进行FCC项目。 FCC还具有在医学应用、聚变能源和高级加速器等不同领域创造技术进步的潜力。

---

## 99. 垂直分片很糟糕

**原文标题**: Vertical Sharding Sucks

**原文链接**: [https://pgdog.dev/blog/vertical-sharding-sucks](https://pgdog.dev/blog/vertical-sharding-sucks)

Lev Kokotov 认为，纵向分片虽然最初看起来像是解决数据库过载的方案，但最终会产生比解决的问题更多的问题，导致正常运行时间减少、复杂性增加以及工程师的沮丧。

他解释说，将表拆分到不同的数据库会降低总体正常运行时间，因为应用程序现在依赖于多个数据库的可用性，而不仅仅是一个。正常运行时间的计算表明，添加更多必需的数据库会降低总体 SLA。

文章强调了纵向分片导致的代码复杂性增加。曾经简洁高效的简单数据库查询（例如，使用 JOIN）被冗长的应用程序级代码所取代，以便手动从不同的数据库中获取和组合数据。这会导致潜在的错误、增加开发时间并降低生产力。

作者认为，工程师在交付功能的驱动下，会采取有问题的方式，例如在数据库之间复制数据或创建“服务”来封装复杂的数据检索逻辑，这进一步复杂化了架构并影响了性能，增加了延迟。

他最后提出，由于 Postgres 缺乏原生的 OLTP 分片解决方案，往往导致纵向分片成为默认解决方案，但强调需要更好的替代方案。作者介绍了 PgDog，一个旨在提供 Postgres 分片解决方案的开源项目，并邀请大家贡献。

---

## 100. Pixel 9a 的 GrapheneOS 实验性版本发布

**原文标题**: Experimental release of GrapheneOS for Pixel 9a

**原文链接**: [https://grapheneos.social/@GrapheneOS/114327666433966529](https://grapheneos.social/@GrapheneOS/114327666433966529)

GrapheneOS发布了Pixel 9a的高度实验性操作系统版本。该公告通过其官方Mastodon账号发布。Mastodon平台需要启用Javascript才能使用Web应用程序，并建议用户，如果Web访问存在问题，可考虑使用其操作系统的原生Mastodon应用程序。核心信息是GrapheneOS现在可用于Pixel 9a，但仍处于实验阶段。

---

