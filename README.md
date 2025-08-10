# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-10.md)

*最后自动更新时间: 2025-08-10 17:46:51*
## 1. 美国在线关闭拨号上网服务

**原文标题**: AOL closes its dial up internet service

**原文链接**: [https://www.ispreview.co.uk/index.php/2025/08/after-34-years-aol-finally-closes-its-dial-up-internet-service.html](https://www.ispreview.co.uk/index.php/2025/08/after-34-years-aol-finally-closes-its-dial-up-internet-service.html)

以下是文章的简要总结：

在经过34年后，美国在线（AOL）将于2025年9月30日在美国和加拿大停止其拨号上网服务，标志着这一最早的消费者互联网服务提供商之一时代的终结。该公告悄无声息地发布，令许多原本以为该服务已经结束的人感到惊讶。虽然拨号服务及相关软件（AOL拨号器和AOL Shield浏览器）将被停止，但AOL的电子邮件服务将继续。

文章回顾了AOL在英国的早期发展，指出其“围墙花园”模式以及最终如何被竞争对手超越。Carphone Warehouse于2006年收购了AOL英国的互联网接入业务，将其更名为AOL Broadband，然后在2010年被TalkTalk收购。TalkTalk于2014年停止接收新的AOL Broadband客户。

文章包含了一些用户的趣闻轶事，他们还记得拨号上网的高昂费用、高价号码以及缓慢速度带来的挫败感。尽管存在局限性，但AOL在互联网市场早期发展中发挥了重要作用。ISPreview正在核实，以确认AOL英国（又名TalkTalk）是否仍然存在任何遗留的拨号客户。

---

## 2. 尝试一下

**原文标题**: Try and

**原文链接**: [https://ygdp.yale.edu/phenomena/try-and](https://ygdp.yale.edu/phenomena/try-and)

本文探讨了语言结构“try and”，其中“and”似乎取代了动词“try”之后的动词不定式“to”。虽然通常被认为在规范上是不正确的，但“try and”在英国和美国英语中都很常见，加拿大使用者也与美国用法相似。它的历史可以追溯到16世纪末，可能早于“try to”。

本文认为“try and”表现出区别于真正并列结构的特性。它允许提取疑问词，禁止动词重新排序，不允许使用“both”，并且主要与动词原形一起使用。某些方言在动词原形条件上有所不同，在加拿大东北部和南非英语等特定地区，屈折形式是可以接受的。此外，副词和否定词不能分隔“try”和“and”，并且“try and”之后不允许省略。

本文将这种现象称为“伪并列”。

最后，本文指出，类似的伪并列模式也存在于其他动词短语中，如“be sure”，以及运动动词中，如“come”和“go”，但后者在句法和语义上与“try and”不同。运动动词伪并列不遵守动词原形条件，并且暗示动作的完成，这与“go to”不同。

---

## 3. GPT-OSS 对比 Qwen3，以及 GPT-2 以来发展历程的详细分析

**原文标题**: GPT-OSS vs. Qwen3 and a detailed look how things evolved since GPT-2

**原文链接**: [https://magazine.sebastianraschka.com/p/from-gpt-2-to-gpt-oss-analyzing-the](https://magazine.sebastianraschka.com/p/from-gpt-2-to-gpt-oss-analyzing-the)

Sebastian Raschka 的这篇文章分析了 OpenAI 最近发布的开源权重 LLM，gpt-oss-20b 和 gpt-oss-120b，并将它们与 GPT-2 和其他模型（如 Qwen3）进行了比较。它探讨了自 GPT-2 以来的架构进步，强调虽然核心 Transformer 架构仍然占主导地位，但已经进行了许多调整和优化。

讨论的关键改进包括：

*   **移除 Dropout：** 现代 LLM 通常省略 Dropout，这与 GPT-2 不同，原因在于单轮训练机制和最小的过拟合风险。
*   **RoPE：** 旋转位置嵌入取代了绝对位置嵌入，用于编码 token 位置，自 Llama 以来已被广泛采用。
*   **SwiGLU：** 这取代了 GELU，提高了前馈模块的计算效率。 SwiGLU 涉及乘法交互，以在更少的参数下提高表达能力。
*   **混合专家 (MoE)：** 这用多个稀疏激活的模块取代了单个前馈模块，从而在保持推理效率的同时提高了容量。
*   **分组查询注意力 (GQA)：** GQA 是多头注意力 (MHA) 的更有效替代方案，它通过在多个查询头之间共享 key 和 value 投影来减少内存使用。
*   **滑动窗口注意力：** 这应用于交替层中，将注意力限制在较小的窗口（在 gpt-oss 中为 128 个 token），从而降低了内存和计算成本。

这篇文章强调，虽然没有发生革命性的架构变化，但这些优化、数据调整和算法调整的累积效应已大大提高了 LLM 的能力。文章最后指出，滑动窗口注意力早在 GPT-3 就已被采用。

---

## 4. Show HN: Engineering.fyi – 一站式搜索技术工程博客

**原文标题**: Show HN: Engineering.fyi – Search across tech engineering blogs in one place

**原文链接**: [https://engineering.fyi/](https://engineering.fyi/)

Engineering.fyi 展示了近期涵盖多种主题和技能水平（从入门到高级）的技术工程博客文章集锦。它允许按技术、难度和代码可用性进行筛选。

主要议题包括：

*   **人工智能与大型语言模型：** 很大一部分侧重于在各种应用中利用人工智能和大型语言模型 (LLM)。这包括：
    *   Google Gemini 的新功能和模型（例如，Gemini 2.5 Flash-Lite、嵌入、`logprobs`、通过 Vertex AI 和 Gemini API 的 API 访问）。
    *   OpenAI 的 ChatGPT 代理，能够主动完成任务。
    *   Meta 用于混凝土配合比设计的 AI 工具。
    *   Shopify 将多模态 LLM 用于其全球目录。
    *   使用 LangExtract 从文本中提取结构化信息。

*   **基础设施与工具：** 文章涵盖基础设施主题，例如：
    *   Airbnb 的 Istio 升级。
    *   Cloudflare 的数据管道框架 Jetflow。
    *   Kubernetes 上的分布式数据库高可用性。
    *   使用 Apigee 进行 API 管理。
    *   微软的 AI 驱动代码审查。

*   **框架与语言：** 提及的特定框架和语言包括：
    *   Shopify 的带有 FlashList v2 的 React Native。
    *   用于机器人和模拟的 JAX。
    *   用于设备上 ML 推理的 ExecuTorch。
    *   Go，重点介绍了 Uber 的 PerfInsights。

*   **开发者工具与平台：** 许多帖子重点介绍了新的开发者工具和平台更新，例如：
    *   具有 AI 功能的 Firebase Studio。
    *   Google Cloud 更新。
    *   Cursor 与 GPT-5 的集成。
    *   Opal（Google Labs 的 AI 迷你应用创建器）。

*   **开源：** 开源项目很普遍，包括 Meta 的混凝土配合比 AI、GenAI Processors 和 Marin 基础模型。

这些文章涵盖了各种公司（Google、Meta、Shopify、Cloudflare、Uber、Airbnb、Palantir、Stripe、Notion 等），反映了不同的工程挑战和解决方案。 这些内容迎合了软件工程领域内不同的技能水平和兴趣。

---

## 5. 扩散语言模型是超级数据学习者

**原文标题**: Diffusion Language Models Are Super Data Learners

**原文链接**: [https://jinjieni.notion.site/Diffusion-Language-Models-are-Super-Data-Learners-239d8f03a866800ab196e49928c019ac](https://jinjieni.notion.site/Diffusion-Language-Models-are-Super-Data-Learners-239d8f03a866800ab196e49928c019ac)

扩散语言模型是超级数据学习者

文章探讨扩散语言模型(DLMs)的数据学习能力，重点在于DLMs作为“超级数据学习者”的优势。

根据"Notion"标签，文章可能探讨：

*   **什么是扩散语言模型(DLMs)?** 简要解释架构和工作原理。DLMs学习反转逐渐向数据添加噪声的扩散过程，从而通过反转噪声来生成新数据。

*   **为什么它们是“超级数据学习者”?** 这是核心论点。文章可能详述DLMs相对于其他语言模型的优势，例如：

    *   **对噪声数据的鲁棒性:** 训练中固有的噪声添加过程使其对数据中的缺陷具有弹性。
    *   **高效的数据利用率:** DLMs可能从较小的数据集中学习有效的表示，或者在大数据集中表现出更好的泛化能力。
    *   **卓越的生成能力:** 它们的架构可能导致更具创造性、多样性和连贯性的文本生成。
    *   **改进的理解能力:** 扩散过程可能会迫使模型更深入地理解底层数据分布。

*   **应用和示例:** 文章可能会展示DLMs在性能上优于其他语言模型的具体用例。 这些可能包括文本生成、文本编辑、图像描述或数据增强。

*   **局限性和未来方向:** 文章可能承认计算成本和数据中潜在偏差等挑战。它也可能讨论未来改进DLMs的研究方向。

---

## 6. Type (YC W23) 正在招聘一位创始工程师来构建一款原生AI文档编辑器。

**原文标题**: Type (YC W23) is hiring a founding engineer to build an AI-native doc editor

**原文链接**: [https://www.ycombinator.com/companies/type/jobs/1idOunL-founding-product-engineer](https://www.ycombinator.com/companies/type/jobs/1idOunL-founding-product-engineer)

Type：招聘创始产品工程师
（获 Y Combinator (W23) 支持的 AI 原生文档编辑器 Type 正在寻找一名创始产品工程师加入其位于布鲁克林的小型团队。该公司的目标是通过将人们从写作中解放出来，专注于更高层次的思考，从而帮助人们自信地交流。该职位涉及构建高级富文本编辑、同步、离线优先和多人协作功能，以及基于 LLM 的写作和编辑工具。

理想的候选人拥有 4 年以上专注于复杂 Web 应用程序的软件工程经验、强大的产品直觉以及对卓越 UX 的热情。所需技术技能包括扎实的 JavaScript、React 和 TypeScript 技能，以及全栈能力。加分项包括熟悉富文本编辑框架、协同编辑技术（CRDT）、离线优先设计、LLM 经验以及后端技术，如 Node.js/Express 和 MongoDB。

Type 提供具有竞争力的薪资（17.5 万美元 - 25 万美元）、慷慨的股票期权（3.00% - 5.00%）以及 100% 雇主承担的医疗、牙科和视力保险。他们致力于多元化和包容性，并鼓励来自弱势群体的申请人。

Type.ai 是一款专为需要更大控制和精确度的专业人士设计的 AI 写作工具。该公司成立于 2023 年，正在积极组建团队。）

---

## 7. Zig的优美语法

**原文标题**: Zig's Lovely Syntax

**原文链接**: [https://matklad.github.io/2025/08/09/zigs-lovely-syntax.html](https://matklad.github.io/2025/08/09/zigs-lovely-syntax.html)

文章《Zig 的可爱语法》赞扬了 Zig 的语法，强调了它如何通过利用更简单的语言语义和周到的设计选择来改进 Rust 的语法。

作者详细介绍了 Zig 语法的几个方面：整数字面量具有隐式强制转换的通用类型 (`comptime_int`)；原始字符串是基于行的标记，可以优雅地处理缩进和转义；记录字面量反映赋值语法，从而更容易理解代码。 Zig 对类型使用前缀表示法，避免了 C 令人困惑的螺旋规则。函数声明类似于 Rust，但为了简单起见，避免了使用箭头表示返回类型。

Zig 通过显式导入以及没有命名空间、隐藏和隐式特性来强制执行清晰性，从而确保代码的可预测性。 用于布尔逻辑的 and 和 or 关键字突出了这些操作由于短路而产生的控制流特性。显式返回、强制性的 if 圆括号（带有可选的大括号）以及带有 else 子句的循环有助于代码的清晰性和可维护性。

Zig 语法的一个核心方面是万物皆表达式——类型、值和模式共享相同的语法，避免了其他语言中存在的语法复杂性和不一致性。 这也适用于函数调用的泛型形式，由于没有类型推断并且参数需要强制性，因此需要一种蛮力方法。

---

## 8. MCP：一个（偶然）通用的插件系统

**原文标题**: MCP: An (Accidentally) Universal Plugin System

**原文链接**: [https://worksonmymachine.ai/p/mcp-an-accidentally-universal-plugin](https://worksonmymachine.ai/p/mcp-an-accidentally-universal-plugin)

斯科特·维尔纳的文章《MCP：一个（意外的）通用插件系统》探讨了最初为人工智能应用设计的模型上下文协议（MCP）如何能像USB-C和其他协议一样，被应用于意想不到的用途，从而成为一个通用插件系统。维尔纳强调了“点烟器原则”，即技术超越其最初目的，演变为通用接口。

他指出，MCP的设计允许连接到各种数据源和工具，无意中创造了在人工智能之外广泛采用的可能性。他以NFT将数据直接存储在指针中的例子来说明协议如何被重新利用。

维尔纳强调，为人工智能构建的MCP服务器越多，任何支持MCP的应用程序就越能访问更多功能，从而创建一个“通用插件生态系统”。这允许应用程序通过一个以人工智能为中心的MCP服务器访问诸如Spotify播放列表之类的功能，即使没有直接为Spotify编写代码。

他将MCP比作USB-C，不是作为一个端口，而是作为一个功能的“可能性空间”。最后，维尔纳宣布了他的项目APM（每分钟动作数），这是一个任务管理应用程序，它利用MCP服务器作为插件，使其能够根据连接的服务转变为不同的工具。他鼓励开发者构建不寻常且有用的MCP服务器，呼应了协议经常在其最初设计之外找到应用的情感。

---

## 9. 在Ampere One 192核处理器上启动5000个Erlang进程

**原文标题**: Booting 5000 Erlangs on Ampere One 192-core

**原文链接**: [https://underjord.io/booting-5000-erlangs-on-ampere-one.html](https://underjord.io/booting-5000-erlangs-on-ampere-one.html)

本文详细介绍了Underjord在使用Nerves框架，在一台拥有1 TB内存的Ampere One 192核机器上运行大量虚拟Linux IoT设备的实验。目标是超越之前运行500个VM的成就。成功的关键在于引入了Frank Hunleth编写的自定义引导加载程序“little_loader”，它简化了启动过程并启用了Nerves的A/B升级功能。

作者解释了QEMU虚拟机的配置，重点是利用KVM进行硬件加速，并强调了通过模拟主机CPU实现的内存节省。他们成功运行了超过5000个VM，证明了Ampere CPU的功能和设置的内存效率。每个VM都运行一个引导加载程序、Linux、erlinit、BEAM/ERTS运行时、Nerves基本功能和NervesHubLink。

文章还描述了内存调优工作，包括调整BEAM VM（分配器、Erlang发布模式）和Linux内核（swappiness、dirty ratios、vfs_cache_pressure）。这些调整允许同时运行更多的VM。

该项目的实用性在于其能够在不需要物理硬件的情况下，模拟真实世界的设备工作负载，用于测试和开发目的。作者正在将这些发现集成到Nerves工具中，从而更容易创建和测试虚拟化嵌入式系统。未来的工作包括调查KVM和NUMA交互、工作负载图表以及进一步优化。

---

## 10. 为 Bash 和 Zsh 编写简单的 Tab 补全

**原文标题**: Writing simple tab-completions for Bash and Zsh

**原文链接**: [https://mill-build.org/blog/14-bash-zsh-completion.html](https://mill-build.org/blog/14-bash-zsh-completion.html)

本文提供了一份编写 Bash 和 Zsh 补全脚本的实用指南，旨在为两种 shell 提供一致的用户体验，包括补全描述。作者以 Mill 构建工具为灵感。

核心思想是注册一个在按下 <TAB> 键时触发的处理函数。该函数（`_generate_foo_completions`）根据当前单词及其在命令行中的索引来识别可能的补全项。特定于 shell 的包装函数（`_complete_foo_bash` 和 `_complete_foo_zsh`）随后获取这些补全项，并与各自 shell 的 API 进行交互（Bash 设置 `COMPREPLY`，Zsh 使用 `compadd`）。

文章随后讨论了如何为补全项添加描述。它描述了如何生成包含补全单词和描述的字符串，两者之间用分隔符分隔。虽然 Zsh 通过 `compadd -d` 原生支持描述，但 Bash 不支持。作者提出了一种巧妙的 Bash 技巧，即当存在多个可能的补全项时，附加描述，利用 Bash 只插入公共前缀的行为。

最后，文章解决了即使单词已经完成也显示描述的问题。这是通过人为地制造歧义来实现的，添加一个重复的“虚拟”补全项，以强制 shell 显示描述。这确保用户即使在完全键入标志或命令后，也可以通过按下 <TAB> 键快速查看其描述。文章最后展示了最终代码，并演示了由此产生的用户体验。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 2 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 3 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 4 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 5 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 6 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 7 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 8 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 9 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 10 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 11 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 12 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 13 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 14 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 15 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 16 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 17 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 18 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 19 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 20 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 21 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 22 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 23 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 24 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 25 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 26 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 27 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 28 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 29 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 30 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 31 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 32 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 33 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 34 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 35 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 36 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 37 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 38 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 39 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 40 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 41 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 42 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 43 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 44 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 45 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 46 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 47 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 48 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 49 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 50 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 51 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 52 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 53 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 54 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 55 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 56 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 57 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 58 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 59 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 60 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 61 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 62 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 63 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 64 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 65 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 66 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 67 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 68 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 69 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 70 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 71 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 72 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 73 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 74 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 75 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 76 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 77 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 78 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 79 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 80 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 81 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 82 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 83 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 84 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 85 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 86 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 87 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 88 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 89 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 90 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 91 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 92 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 93 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 94 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 95 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 96 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 97 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 98 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 99 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 100 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 101 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 102 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 103 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 104 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 105 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 106 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 107 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 108 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 109 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 110 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 111 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 112 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 113 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 114 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 115 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 116 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 117 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 118 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 119 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 120 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 121 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 122 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 123 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 124 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 125 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 126 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 127 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 128 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 129 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 130 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 131 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 132 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 133 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 134 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 135 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 136 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 137 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 138 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 139 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 140 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 141 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 142 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 143 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 144 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
