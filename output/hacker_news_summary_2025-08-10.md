# Hacker News 热门文章摘要 (2025-08-10)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. OS/2 内部结构 (1987)

**原文标题**: Inside OS/2 (1987)

**原文链接**: [https://gitpi.us/article-archive/inside-os2/](https://gitpi.us/article-archive/inside-os2/)

这篇1987年12月发表的题为“OS/2 内幕”的文章介绍了 OS/2，认为它是 Intel 80286/80386 微型计算机未来潜在的操作系统，强调了其多任务处理能力、全面的 API 和可扩展性。微软设想 OS/2 成为办公自动化的平台，通过多任务处理和资源共享实现个人生产力，并通过网络实现团队生产力。

文章概述了 OS/2 的架构，包括内核和系统服务、Windows 演示管理器 (WPM) 和 OS/2 LAN Manager，重点介绍了内核。文章强调了 OS/2 API，一个高级编程接口，以及 WPM 和 LAN Manager 的可选性质。

OS/2 的抢占式调度器使用基于任务优先级的时分片，从而实现高效的上下文切换。API 通过动态链接 (dyn-link) 库实现，节省磁盘空间和 RAM。动态链接还有助于轻松更新和代码共享。OS/2 系统在受保护模式下进行多任务处理，在实模式下与 MS-DOS 兼容。

文章详细介绍了进程的创建和执行，强调 OS/2 执行的是线程，而不是直接执行进程。一个进程可以拥有多个共享资源的线程，从而实现异步执行。线程的加载速度比进程快。文章还讨论了屏幕组，这是由会话管理器管理的、用于多任务处理的用户友好功能。OS/2 的 API 是 MS-DOS 功能的超集，FAPI 通过“绑定”提供 MS-DOS 和 OS/2 之间的兼容性。

最后，文章涵盖了 OS/2 的进程创建、内存管理、设备服务、文件管理和进程间通信。它包含一个演示线程创建的代码片段。

---

## 12. Abogen – 从EPUB、PDF和文本生成有声书

**原文标题**: Abogen – Generate audiobooks from EPUBs, PDFs and text

**原文链接**: [https://github.com/denizsafak/abogen](https://github.com/denizsafak/abogen)

Abogen：一款文本转语音工具，可将EPUB、PDF和文本文件转换为带同步字幕的有声读物，使用Kokoro-82M模型提供自然语音。它专为创建适用于各种平台的有声读物和配音而设计。

可在Windows、Mac和Linux上安装，可通过处理依赖项的基于脚本的安装或使用`pip`进行安装。对于Windows，需要espeak-ng。该工具支持NVIDIA GPU，并在Linux上提供实验性的AMD GPU支持。

要使用Abogen，用户可以拖放文件，配置语音速度、声音选择（包括用于自定义声音的语音混合器）、字幕生成样式和输出格式（.WAV、.FLAC、.MP3、.OPUS、M4B）等设置。功能包括用于批量处理的队列模式、章节控制以及M4B文件的元数据标记。

Abogen支持多种语言（美式/英式英语、西班牙语、法语、印地语、意大利语、日语、巴西葡萄牙语、普通话）。该软件提供主题定制、缓存管理和更新检查选项。提供Dockerfile用于容器化。

主要功能包括与Kokoro集成进行TTS、为英语生成字幕（取决于Kokoro的时间戳支持）以及为文本文件添加章节标记和元数据标签，以增强有声读物的创建。它采用MIT许可证。

---

## 13. 开放可爱

**原文标题**: Open Lovable

**原文链接**: [https://github.com/mendableai/open-lovable](https://github.com/mendableai/open-lovable)

Open Lovable：一个允许用户通过与AI聊天即时构建React应用的开源项目。该项目可在GitHub上获取，需要克隆仓库并使用npm安装依赖项。

要运行该应用程序，用户需要创建`.env.local`文件，并提供E2B（用于沙箱）和Firecrawl（用于网络抓取）的API密钥。可以选择性地添加Anthropic、OpenAI或Groq等AI提供商的API密钥以增强AI功能。具体来说，需要从e2b.dev获取E2B_API_KEY，以及从firecrawl.dev获取FIRECRAWL_API_KEY。为了获得更好的AI体验，用户可以从各自的平台添加ANTHROPIC_API_KEY、OPENAI_API_KEY或GROQ_API_KEY。

配置环境后，可以使用`npm run dev`启动应用程序，并在`http://localhost:3000`访问。该项目以MIT许可证发布。总而言之，Open Lovable通过AI驱动的交互提供了一种简化的React应用开发方法。

---

## 14. 我是如何在预算有限/免费的情况下用AI编程的

**原文标题**: How I code with AI on a budget/free

**原文链接**: [https://wuu73.org/blog/aiguide1.html](https://wuu73.org/blog/aiguide1.html)

如何用免费/低成本AI辅助编程：作者分享了如何利用AI工具免费进行编码的方法。作者强调结合免费服务和策略性提示，以最大化效率和效果。

核心策略是使用AI编码助手（如GitHub Copilot，对学生和热门开源项目的维护者免费）的免费层级，并利用Ollama和LM Studio等服务提供的免费模型进行本地执行。这允许进行实验并提高隐私性，而无需产生费用。

作者强调了提示工程的重要性。他们提倡向AI模型提供清晰、具体的指令和示例，以获得所需的代码输出。技巧包括将复杂的任务分解为更小、更易于管理的提示，并使用代码片段作为上下文供AI在此基础上进行构建。

此外，文章还强调了使用AI执行特定任务（如生成样板代码、调试、提出改进建议以及在不同编程语言之间转换代码）的好处。作者警告不要盲目接受AI生成的代码，并强调需要仔细审查和测试。

总而言之，本指南概述了一种利用AI进行编码的实用方法，通过专注于免费工具、有效的提示策略和对AI生成代码的批判性评估，来平衡成本效益和生产力。这是一份面向希望将AI集成到工作流程中而又不想超支的开发人员的实践指南。

---

## 15. 燧发枪 (Flintlock) – 创建并管理 MicroVM 的生命周期，由 containerd 提供支持

**原文标题**: Flintlock – Create and manage the lifecycle of MicroVMs, backed by containerd

**原文链接**: [https://github.com/liquidmetal-dev/flintlock](https://github.com/liquidmetal-dev/flintlock)

Flintlock是社区驱动的微虚拟机生命周期创建和管理服务，利用containerd。它最初由Weaveworks开发，支持Cloud Hypervisor和Firecracker虚拟机监视器（VMM）。

Flintlock允许用户通过API请求（gRPC或HTTP）创建、删除、启动、停止和暂停微虚拟机。它通过cloud-init、ignition和OCI镜像为卷、内核和initrd提供配置选项。指标暴露以供Prometheus收集。CNI网络配置计划在未来实现。

Flintlock最初设计用于虚拟化Kubernetes集群中的裸机主机，作为Liquid Metal的一部分，它可以用于各种轻量级虚拟化场景，如隔离的工作负载和管道。与特定Firecracker和Cloud Hypervisor版本的兼容性至关重要，详细信息请参考表格。注意：不再支持Firecracker的macvtap分支。

欢迎贡献，并鼓励通过CNCF Slack #liquidmetal频道进行社区互动。

---

## 16. 想知道 OpenAI 新 GPT-OSS 模型的训练数据吗？我也是。

**原文标题**: Curious about the training data of OpenAI's new GPT-OSS models? I was too

**原文链接**: [https://twitter.com/jxmnop/status/1953899426075816164](https://twitter.com/jxmnop/status/1953899426075816164)

标题为《好奇OpenAI新款GPT-OSS模型的训练数据？我也是》的文章，可能探讨了OpenAI开源GPT模型所使用的训练数据。然而，可见内容仅为X.com（前身为Twitter）的一条通用消息，提示JavaScript已禁用，用户需要启用它或使用受支持的浏览器才能访问该网站。

因此，**无法从提供的摘录中获取任何关于OpenAI的GPT-OSS模型训练数据的信息。** 内容仅仅是一个阻止访问X.com上实际文章的错误消息。我们只能推断该文章存在，并且其作者表达了对模型训练数据的好奇。

---

## 17. GPT-5：它就是能做到

**原文标题**: GPT-5: It Just Does Stuff

**原文链接**: [https://www.oneusefulthing.org/p/gpt-5-it-just-does-stuff](https://www.oneusefulthing.org/p/gpt-5-it-just-does-stuff)

伊森·莫利克在《GPT-5：它就是能干事》一文中详细描述了他对OpenAI的GPT-5的早期使用体验。他强调，GPT-5标志着人工智能能力的显著进步，尤其是其自动化任务和主动提出解决方案的能力。

一个关键特性是GPT-5的智能模型选择。它会根据任务的复杂性自动选择合适的GPT-5模型（从快速、基础版本到强大的“推理器”）和推理时间。这减轻了用户手动选择模型的负担，并确保了最佳性能。

莫利克强调了GPT-5的主动性，它可以建议任务并自主执行。他讲述了GPT-5从一个简单的提示中生成具有详细着陆页、财务报表和研究计划的初创企业想法的例子。他还描述了仅通过提供模糊的鼓励就创建了一个功能齐全的3D城市建造器的过程。

文章指出，虽然人类仍然参与决策和错误检查，但GPT-5的智能和主动性引发了人们对未来人类参与角色的质疑。尽管存在潜在的错误，但该人工智能能够持续解决问题并避免陷入错误循环，从而使开发过程更加顺畅。

本质上，GPT-5代表着向更直观和自动化的AI体验的转变，用户可以提供最少的输入并获得实质性的结果。该AI“就是能干事”，以令人印象深刻的自主性和效率来预测需求并执行任务。

---

## 18. 展示HN：根据您的近似位置，用CSS渐变显示当前天空

**原文标题**: Show HN: The current sky at your approximate location, as a CSS gradient

**原文链接**: [https://sky.dlazaro.ca](https://sky.dlazaro.ca)

此"Show HN"帖子介绍了一个工具或项目，该工具或项目生成一个CSS渐变，表示用户大致位置的当前天空颜色。给定的例子使用了坐标41.85003, -87.65005，对应于芝加哥。其核心思想是将天空的样貌视觉化地表示为一个CSS渐变，很可能根据一天中的时间和潜在的其他因素（如天气）而变化。该项目可能利用位置数据来获取有关当前大气状况的信息，并使用这些信息来创建渐变的调色板。

该帖子是一个简洁的公告，缺乏关于渐变如何生成、使用什么数据源或任何交互功能的细节。然而，核心功能似乎是将天空的颜色动态地可视化为一个CSS渐变，潜在地允许用户根据地理位置将天空的实时表示嵌入到他们的Web项目中。可以推断，该项目可以用于美学目的，作为环境背景，甚至可以以视觉方式说明时间的流逝。

---

## 19. 滥用Entra OAuth以获取乐趣和访问微软内部应用

**原文标题**: Abusing Entra OAuth for fun and access to internal Microsoft applications

**原文链接**: [https://research.eye.security/consent-and-compromise/](https://research.eye.security/consent-and-compromise/)

本文重点介绍Microsoft Entra OAuth实现中发现的安全漏洞，该漏洞导致作者能够未经授权地访问Microsoft内部应用程序。虽然此片段未提供漏洞的具体细节，但标题强烈暗示该攻击利用了Entra OAuth身份验证流程中的弱点或错误配置。

第二行表明一个单独但可能相关的发现：Microsoft Copilot使用的Python沙盒中的root提权漏洞。这可能允许研究人员获得对Copilot运行所在容器的root访问权限。

这篇文章可能详细描述了研究人员如何组合或使用这些漏洞。它暗示了一个漏洞链：或许从滥用Entra OAuth获得初始访问权限开始，然后转向Copilot沙盒以提升权限，并可能进一步危害Microsoft内部系统。

本质上，本文描述了一次针对Microsoft基础设施的成功渗透测试，特别强调了其Entra OAuth实现和Copilot Python沙盒中的漏洞，最终导致重大的内部访问权限。标题作为一个吸引眼球的摘要，表明了潜在的损害和漏洞利用的深度。

---

## 20. 我在湾区人工智能安全聚会上的致命三连击演讲

**原文标题**: My Lethal Trifecta talk at the Bay Area AI Security Meetup

**原文链接**: [https://simonwillison.net/2025/Aug/9/bay-area-ai/](https://simonwillison.net/2025/Aug/9/bay-area-ai/)

提示注入的致命三要素

这篇博文总结了在湾区人工智能安全聚会上关于提示注入的演讲，重点介绍了作者创造的一个概念：“致命三要素”。提示注入被定义为人工智能工程中的罪过，即将受信任的指令与不受信任的输入连接起来，文章使用 SQL 注入的类比解释了提示注入。作者承认他们最初尝试定义提示注入时，由于误解而失败。

“致命三要素”包括：访问私有数据、暴露于不受信任的内容以及向外部通信的能力（数据泄露）。Invariant Labs 的一个例子说明了这种漏洞，在该示例中，LLM 被授予访问私有 GitHub 存储库的权限，通过公共问题暴露于恶意指令，并且能够创建拉取请求以泄露数据。

作者批评了常见的防御方法，如“提示恳求”（要求模型避免技巧）和人工智能驱动的过滤，认为在安全领域，99% 的有效性是不够的。缓解需要移除三要素中的至少一个。重点应放在限制数据泄露途径，以及避免可能造成损害的工具调用。谷歌 DeepMind 的 CaMeL 和论文《用于保护 LLM 代理免受提示注入的设计模式》被认为是可信的方法。

一个主要的担忧是模型上下文协议 (MCP) 的混合搭配性质，这迫使用户通过组合不同的 MCP 服务器来做出关键的安全决策。这种设置创造了一种大多数最终用户没有准备好承担的责任。作者最后提供了指向其相关博客文章和社交媒体个人资料的链接。

---

## 21. OpenFreeMap 每秒承受 10 万次请求

**原文标题**: OpenFreeMap survived 100k requests per second

**原文链接**: [https://blog.hyperknot.com/p/openfreemap-survived-100000-requests](https://blog.hyperknot.com/p/openfreemap-survived-100000-requests)

OpenFreeMap 创始人 Zsolt Ero 讲述了流量意外激增，导致该服务需处理每秒 10 万次请求的经历。Ero 最初因瓦片加载错误收到警报，随后发现 24 小时内涌入了 30 亿次请求，总流量达 215 TB。经追踪，流量来源是一个名为 Wplace.live 的新型协作绘图网站，用户显然通过脚本自动请求来规避像素放置限制。

尽管负载巨大，OpenFreeMap 仍保持了 96% 的成功率，这归功于高 CDN 缓存率和服务器处理剩余请求的能力。Ero 赞扬 Cloudflare 对其提供的带宽赞助和支持。

为缓解未来问题，Ero 实施了一条 Cloudflare 规则来限制来自 Wplace.live 的流量，并计划通过来源网址实施带宽限制。他还发现并打算修复导致空瓦片的服务器配置问题。

他已联系 Wplace.live，并主动帮助他们搭建自己的自托管 OpenFreeMap 实例。Ero 还怀疑 Wplace.live 的高请求率是由于脚本使用，而非真实用户交互所致。

Ero 正在寻求更多 OpenFreeMap 赞助，以便投入更多时间进行开发，并确保该服务保持稳健，为未来的挑战做好准备。

---

## 22. 马铃薯的演变

**原文标题**: How Potatoes Evolved

**原文链接**: [https://www.nhm.ac.uk/discover/news/2025/july/we-finally-solved-the-mystery-of-how-potatoes-evolved.html](https://www.nhm.ac.uk/discover/news/2025/july/we-finally-solved-the-mystery-of-how-potatoes-evolved.html)

乔什·戴维斯2025年7月31日发表的文章揭示了理解马铃薯进化的一项科学突破。该研究发现，马铃薯（如薯片和土豆泥）这种主要食物来源，起源于大约九百万年前的一次杂交事件。这一发现澄清了长期以来关于这种重要作物遗传起源的谜团。本质上，这篇文章强调了我们今天消费的马铃薯是来自祖先物种的特定遗传物质组合的结果，这一发现为这种全球重要食物的进化历史提供了关键见解。

---

## 23. Framework Desktop 是个狠家伙

**原文标题**: The Framework Desktop is a beast

**原文链接**: [https://world.hey.com/dhh/the-framework-desktop-is-a-beast-636fb4ff](https://world.hey.com/dhh/the-framework-desktop-is-a-beast-636fb4ff)

作者盛赞 Framework Desktop，这是一款紧凑型（4.5L）且静音的迷你 PC，搭载 AMD Ryzen AI Max 395+ 笔记本电脑 CPU。尽管桌面电脑市场拥挤，且 PC 本身具有可维修性，但 Framework 的产品凭借其性能、设计和独特功能脱颖而出。

该机器在多核工作负载方面表现出色，显著优于 Beelink SER8/9 等竞争对手，甚至在 Docker 繁重的开发任务中也优于 Apple 的 M4 Max/Pro。虽然 Apple 保持着单核性能的领先优势，但作者认为多核优势和更低的价格使 Framework Desktop 对开发者来说更具价值。

可定制的前面板瓷砖相比传统的 PC 设计，提供了一种令人耳目一新的美感。 凭借 64GB 或 128GB 的 RAM，它可以处理要求苛刻的任务，包括潜在的运行本地 LLM，尽管作者发现与 SaaS 解决方案相比，较小模型的准确性有所欠缺。

Framework Desktop 的售价为 1,876 美元，配备 64GB RAM 和 2TB NVMe，比同等配置的 Mac Studio 便宜得多。 虽然像 Beelink SER9 这样的替代品以更低的价格提供良好的性能，但 Framework 在静音运行和原始多核性能方面表现出色。

AMD 395+' 的集成显卡出人意料地强大，可与 RTX 4060 相媲美，并允许进行 1440p 游戏。文章总结说，Framework Desktop 对于重视性能、安静运行和可定制硬件的 Linux 用户来说，是一款出色的机器。

---

## 24. POML：提示编排标记语言

**原文标题**: POML: Prompt Orchestration Markup Language

**原文链接**: [https://github.com/microsoft/poml](https://github.com/microsoft/poml)

POML（提示编排标记语言）是一种新型标记语言，旨在简化和增强大型语言模型（LLM）的提示工程。它通过提供结构化、可维护和通用的方法来解决非结构化提示的挑战。

POML 的主要特性包括：

*   **结构化提示标记：** 使用类似 HTML 的语法将提示组件组织成模块。
*   **全面的数据处理：** 无缝集成各种数据类型，例如文本、表格和图像。
*   **解耦的呈现样式：** 使用类似 CSS 的系统将内容与呈现分离，无需更改核心提示逻辑即可进行样式修改。
*   **集成的模板引擎：** 支持使用变量、循环和条件语句的动态提示生成。
*   **丰富的开发工具包：** 包括带有语法高亮、自动完成和实时预览的 VS Code 扩展，以及用于 Node.js 和 Python 的 SDK。

开始使用 POML 包括安装 VS Code 扩展或 SDK，并配置 LLM 设置。 本文提供了一个基本的 POML 示例来演示其语法和功能。 文档、演示视频和研究论文（即将推出）提供了进一步的学习资源。 该项目鼓励贡献，并遵守 Microsoft 开源行为准则、负责任的 AI 标准，并根据 MIT 许可证获得许可。

---

## 25. 《空心人》百年

**原文标题**: “The Hollow Men” at 100

**原文链接**: [https://prufrock.substack.com/p/the-the-hollow-men-at-100](https://prufrock.substack.com/p/the-the-hollow-men-at-100)

无法访问文章链接。

---

## 26. LHC新型芯片应对辐射挑战

**原文标题**: LHC's New Chip Tackles Radiation Challenges

**原文链接**: [https://spectrum.ieee.org/lhc-radiation-chip](https://spectrum.ieee.org/lhc-radiation-chip)

《计算新闻期刊观察》文章宣布了大型强子对撞机（LHC）的一项重大技术升级：由徐瑞等人设计的新芯片。该芯片意义重大，因为它解决了LHC严酷辐射环境和粒子碰撞产生海量数据所带来的挑战。该芯片旨在精确转换每秒15亿次碰撞产生的数据，同时承受LHC的独特条件。这项升级有望提高LHC观测和分析粒子碰撞的能力，从而推进粒子物理学研究。米歇尔·汉普森撰写了这篇文章。

---

## 27. CT扫描仪揭示386处理器陶瓷封装内部的惊喜

**原文标题**: A CT scanner reveals surprises inside the 386 processor's ceramic package

**原文链接**: [https://www.righto.com/2025/08/intel-386-package-ct-scan.html](https://www.righto.com/2025/08/intel-386-package-ct-scan.html)

通过3D CT扫描揭示的Intel 386处理器陶瓷封装内部令人惊讶的复杂结构

---

## 28. 瓜王网站

**原文标题**: Melonking Website

**原文链接**: [https://melonking.net/](https://melonking.net/)

所提供的文本描述了一个名为“Melonking网站”的简单网页，它具有一种异想天开且过时的互联网美学风格。“永远是你的朋友，Melon！”的问候语立即建立了一种友好和个性化的语气。“您现在正要离开信息高速公路！”是对互联网早期时代的一种怀旧引用。

该网站还鼓励用户“启用自动播放音频”，并建议使用Firefox以获得“最佳”体验，这进一步强化了复古感。欢迎信息“欢迎来到Melonland :^]”附带一个表情符号，增添了轻松愉快的气氛。

最后，该页面将音乐归功于“johnny_ripper - by the sea ☺”，为背景音频提供了归属，并再次使用了表情符号。本质上，这段文字描绘了一个非常简单和老式的个人网站，旨在显得古怪而受欢迎。它可能是一个怀旧的回顾或一个幽默的个人项目。

---

## 29. LLM驱动开发的现状

**原文标题**: The current state of LLM-driven development

**原文链接**: [http://blog.tolki.dev/posts/2025/08-07-llms/](http://blog.tolki.dev/posts/2025/08-07-llms/)

本文回顾了当前LLM驱动开发的状态，强调了其潜力和局限性。作者强调，LLM并非万能药，需要熟练的开发者来引导，尤其是在阅读和理解生成的代码方面。它们擅长处理成熟、文档完善的代码库和主流语言，但在不太常见的技术栈或复杂功能方面表现不佳。

作者将LLM“代理”描述为本质上是协调对LLM的调用，并使用代码导航、shell命令和MCP服务器等外部工具，这些工具为LLM格式化数据。常见问题包括定价不稳定、模型快速更新以及缺乏确定性行为。

作者测试了包括Github Copilot、Claude Code Pro和Gemini CLI在内的几种LLM工具，发现它们都在一个复杂的Flutter组件上表现不佳。虽然LLM非常适合实现成熟的标准、编写集成测试、修复错误以及使用新的技术栈，但它们通常会引入不必要的复杂性和代码重复。Rust由于其编译器对可读性的强调，似乎特别适合LLM代理，而Python需要强类型才能有效。

作者总结说，LLM在强类型的后端应用程序中表现出色，但在前端开发中受到更多限制，尤其是对于自定义组件和复杂交互。他们推荐Github Copilot，因为它具有价值和可定制性，但也建议不要感到被迫使用LLM，因为它们具有固有的缺点。作者提倡使用更轻量、更专注的LLM，而不是当前大规模、通用模型的趋势。

---

## 30. Ch.at – 一个轻量级的LLM聊天服务，可通过HTTP、SSH、DNS和API访问

**原文标题**: Ch.at – A lightweight LLM chat service accessible through HTTP, SSH, DNS and API

**原文链接**: [https://ch.at/](https://ch.at/)

Ch.at 是一个轻量级、通用可访问的聊天服务，由大型语言模型 (LLM) 驱动，设计注重简洁和隐私。它被描述为“通用基础智能”，可以通过多种方式访问，包括标准 HTTP 接口、SSH、DNS 查询和传统 API。

主要特点包括：

*   **可访问性：** 用户可以使用网络浏览器、SSH 客户端、`curl` 甚至通过 `dig` 进行 DNS 查询与 LLM 交互。
*   **隐私性：** 该服务拥有“无日志”政策，无需用户帐户，强调用户隐私。
*   **开源：** Ch.at 是自由软件，表明透明度和社区参与。
*   **轻量级：** 旨在成为精简且随时可用的服务。

本质上，Ch.at 提供了一种易于访问且私密的与 LLM 交互的方式，提供多个入口点以满足不同的用户偏好和技术能力。

---

## 31. Quickshell – 桌面的构建块

**原文标题**: Quickshell – building blocks for your desktop

**原文链接**: [https://quickshell.org/](https://quickshell.org/)

Quickshell 0.2.0 于 2025-07-26 发布，是一个使用 QtQuick 构建桌面组件（如状态栏、小部件和锁屏）的工具包。它旨在为创建完整的桌面环境提供构建模块，与 Wayland 合成器或窗口管理器协同工作。

Quickshell 使用 QML 进行配置，QML 是一种用户友好的语言，具有 LSP 支持，专为创建灵活的用户界面而设计。主要功能包括实时更新（允许用户在保存后立即看到更改）和不断扩展的广泛集成。

该文档重点介绍了 QML 实现的代码示例，展示了创建交互元素（如根据计时器改变颜色的浮动窗口）的能力。文中提到了多个用户（soramane、end_4、outfoxxed、pfaj & bdebiase、flicko 和 vaxry）对 Quickshell 的不同配置，表明这是一种社区驱动和可定制的方法。该文档提供了安装和文档链接。

---

## 32. 不要让它崩溃，让它自愈

**原文标题**: Don't “let it crash”, let it heal

**原文链接**: [https://www.zachdaniel.dev/p/elixir-misconceptions-1](https://www.zachdaniel.dev/p/elixir-misconceptions-1)

扎克·丹尼尔的文章挑战了常见的Elixir短语“让它崩溃”，认为它经常被误解并导致不良的编码习惯。他认为，盲目地崩溃进程会对用户体验产生负面影响，尤其是在进程与现实世界的资源（如Web sockets或数据库连接）相关联时。突然崩溃可能导致UI重置、连接丢失，并且无法向用户提供有意义的错误反馈。

作者强调，虽然BEAM VM允许通过supervisor自动重启进程，但这并不能免除开发者优雅地处理错误的责任。他提倡通过特定的错误消息向用户表示失败的状态，而不是仅仅崩溃。

虽然承认崩溃适用于不可恢复的情况，例如接收到格式错误的输入，但丹尼尔强调设计页面以优雅地处理这些重新挂载的重要性。核心在于，BEAM的优势不仅在于重启进程的能力，还在于*每个*进程都有一个初始化例程，使其能够“治愈”并返回到已知的良好状态。他建议用“让它治愈”代替“让它崩溃”，以更好地反映BEAM的真正力量，并鼓励更周到的错误处理。

---

## 33. 长期暴露于室外空气污染与痴呆症风险增加有关

**原文标题**: Long-term exposure to outdoor air pollution linked to increased risk of dementia

**原文链接**: [https://www.cam.ac.uk/research/news/long-term-exposure-to-outdoor-air-pollution-linked-to-increased-risk-of-dementia](https://www.cam.ac.uk/research/news/long-term-exposure-to-outdoor-air-pollution-linked-to-increased-risk-of-dementia)

一项对近三千万人数据的综合分析显示，长期暴露于室外空气污染与痴呆症风险增加之间存在密切联系，包括阿尔茨海默病和血管性痴呆。剑桥大学的研究人员在《柳叶刀·星球健康》上发表的一项研究中指出，细颗粒物（PM2.5）、二氧化氮（NO2）和烟尘是导致风险增加的关键污染物。

这项包含主要来自高收入国家的51项研究的荟萃分析显示，这些污染物与痴呆症之间存在统计学上的显著关联。具体而言，PM2.5每增加10微克/立方米，痴呆症风险增加17%。二氧化氮和烟尘也出现了类似的增长。这些污染物来自车辆尾气、工业过程和木材燃烧等来源，据信会引发大脑炎症和氧化应激，从而导致痴呆症的发生和发展。

该研究强调迫切需要更严格的污染限制，以及涉及城市规划、交通政策和环境监管的跨学科方法，以有效对抗空气污染。研究人员强调，未来的研究应包括更多样化的人群，特别是来自边缘化社区以及中低收入国家的人群，因为这些群体通常遭受更高的污染暴露。减少空气污染可以带来显著的健康、社会、气候和经济效益，减轻个人、家庭和医疗保健系统的负担。

---

## 34. 加州快餐最低工资减少了就业吗？

**原文标题**: Did California's fast food minimum wage reduce employment?

**原文链接**: [https://www.nber.org/papers/w34033](https://www.nber.org/papers/w34033)

NBER工作论文《加州快餐最低工资是否降低了就业？》（作者：Jeffrey Clemens、Olivia Edwards和Jonathan Meer）分析了加州于2024年4月生效的20美元快餐最低工资的影响。

作者发现证据表明，最低工资的提高导致了加州快餐业就业岗位的减少。他们使用来自季度就业和工资普查的未经调整的数据，观察到2023年9月至2024年9月期间，加州快餐业的就业人数相对于美国其他地区下降了2.7%。考虑到先前存在的趋势并调整其他行业的变化后，估计降幅甚至更大，高达3.2%。

作者的中位数估计表明，与没有提高最低工资的情况相比，加州快餐业损失了大约18,000个工作岗位。该论文表明，实施的工资政策产生了负面的就业后果。

---

## 35. Debian 13 “Trixie”

**原文标题**: Debian 13 “Trixie”

**原文链接**: [https://www.debian.org/News/2025/20250809](https://www.debian.org/News/2025/20250809)

Debian 13 “Trixie” 于 2025 年 8 月 9 日发布，历经两年多的开发，并将获得五年支持。它拥有超过 14,100 个新软件包，总数达到 69,830 个，其中 44,326 个软件包已更新，8,840 个已被删除。关键软件更新包括 Apache 2.4.64、Bash 5.2.37、GCC 14.2、GIMP 3.0.4、LibreOffice 25.2、Linux kernel 6.12 LTS、MariaDB 11.8 和 Python 3.13。

Trixie 提供了诸如 GNOME 48、KDE Plasma 6.3、LXDE 13、LXQt 2.1.0 和 Xfce 4.20 等桌面环境。一项重大变化是为除 i386 之外的所有架构采用 64 位 time_t ABI，从而解决了 2038 年问题。此版本标志着对 riscv64 架构的首次官方支持，以及对 armel 的最后一次支持。

i386 架构不再获得官方支持，建议 i386 系统上的用户重新安装为 amd64 或淘汰其硬件。

Debian 为包括 Amazon EC2、Microsoft Azure 和 OpenStack 在内的各种平台提供云镜像。Live 镜像可用于带有各种桌面环境的 amd64 和 arm64。安装支持 78 种语言，并且可以通过蓝光光盘、DVD、CD、USB 闪存盘或网络连接执行。

从 Debian 12 “Bookworm” 的升级通过 APT 处理，强烈建议在升级前进行备份。OpenLDAP 客户端现在使用 OpenSSL 进行 TLS。鼓励用户在升级前查看发行说明，以了解潜在问题。多架构容器镜像可在 Docker Hub 上获得。

---

## 36. 考古学家称，庞贝遗址重现人迹

**原文标题**: People returned to live in Pompeii's ruins, archaeologists say

**原文链接**: [https://www.bbc.com/news/articles/c62wx23y2v1o](https://www.bbc.com/news/articles/c62wx23y2v1o)

考古学家发现新证据表明，公元79年维苏威火山爆发后，人们曾返回庞贝古城遗址居住。虽然之前有所推测，但新的研究证实了这一理论。幸存者，以及可能加入的寻求定居者，无力在别处开始新的生活。火山爆发后的定居点并非城市，而是一个“岌岌可危且灰暗的聚集地，一种营地，一个贫民窟”，建立在可辨认的废墟之中。这种非正式的聚居地一直持续到5世纪。

由于缺乏典型的罗马基础设施和服务，居民可能居住在受损房屋的较高楼层，并将较低楼层改造成地窖。废墟也提供了寻找贵重物品的机会。据遗址主管加布里埃尔·祖赫特里格尔称，这些重新占领的痕迹在早期的挖掘工作中经常被忽视和清除，当时的挖掘工作主要集中在保存完好的火山爆发前城市的文物上。庞贝古城在火山爆发前居住着超过2万人，现在是一个世界著名的旅游景点，可以一窥罗马生活。

---

## 37. 斯坦福将继续沿用传承录取政策并退出加州助学金计划

**原文标题**: Stanford to continue legacy admissions and withdraw from Cal Grants

**原文链接**: [https://www.forbes.com/sites/michaeltnietzel/2025/08/08/stanford-to-continue-legacy-admissions-and-withdraw-from-cal-grants/](https://www.forbes.com/sites/michaeltnietzel/2025/08/08/stanford-to-continue-legacy-admissions-and-withdraw-from-cal-grants/)

2025年，斯坦福大学宣布，尽管加州议会第1780号法案禁止此类做法，但该校仍将在2026年秋季班的招生中继续给予校友或捐赠者子女（即“传承生”）录取偏好。为了规避该法案，斯坦福大学将退出加州助学金计划（Cal Grant program），这是一项由州政府资助的加州学生经济援助来源。

第1780号法案最初威胁要对给予传承生优先权的大学处以罚款，但后来被修改为仅要求每年报告合规情况以及传承生录取率与普通学生群体的比较。斯坦福大学将用大学资金取代损失的加州助学金资金，以维持当前的学生经济援助水平。

斯坦福大学的决定受到了批评，特别是来自像“集体诉讼”(Class Action)这样的学生权益倡导团体的批评，他们认为这优先考虑了富裕校友的子女，而不是公共利益。尽管其他大学由于公平性考虑而停止了传承生录取，尤其是在最高法院对考虑种族因素的招生政策做出不利裁决之后，但斯坦福大学将继续这一做法。

文章还指出，特朗普政府正在指示国家教育统计中心收集申请人群体和录取队列的种族和性别数据，这引发了人们对大学招生做法（不仅仅是传承生偏好）的透明度和公平性的质疑。

---

## 38. 工程师的招聘视角

**原文标题**: An engineer's perspective on hiring

**原文链接**: [https://jyn.dev/an-engineers-perspective-on-hiring](https://jyn.dev/an-engineers-perspective-on-hiring)

本文从工程师的角度批判了常见的软件工程招聘实践，认为许多公司在招聘方面“很糟糕”，因为他们浪费时间、追逐潮流，并且未能准确评估人才。作者强调，区分候选人、与实际工作职责相关、关注长期价值、高效且尊重申请人的面试非常重要。他们还强调了经常被忽视的“品味”——创建干净、可维护代码的能力。

文章分析了诸如在线编程（LeetCode）、家庭作业和架构设计等流行面试形式的缺陷，强调了它们在区分候选人、反映实际工作职责和尊重申请人时间方面的失败。作者赞扬了Oxide Computer Company使用的扩展论文和工作示例，认为它们既全面又尊重，但也承认它们的时间效率较低。

作者建议了一种更好的方法，即结合代码审查面试（申请人批判预先编写的代码）和对申请人提供的工作示例的现场讨论。这种方法强调协作，评估人际交往能力、设计思维和品味，同时最大限度地减少时间不对称并表示尊重。最后，作者建议每位候选人都至少与他们的潜在经理进行一次面试，以确保良好的工作关系。 最终目标是为长期找到最好的员工，而不仅仅是为了下一个季度。

---

## 39. 对XSS犯罪论坛的突袭中，谁被捕了？

**原文标题**: Who got arrested in the raid on the XSS crime forum?

**原文链接**: [https://krebsonsecurity.com/2025/08/who-got-arrested-in-the-raid-on-the-xss-crime-forum/](https://krebsonsecurity.com/2025/08/who-got-arrested-in-the-raid-on-the-xss-crime-forum/)

文章详细介绍了在法国警方领导、欧洲刑警组织支持的长期调查之后，一名 38 岁的俄语网络犯罪论坛 XSS 的管理员被捕的情况。虽然当局尚未公布嫌疑人的姓名，但猜测指向网络犯罪界的关键人物“Toha”。

这次逮捕在 XSS 社区引发了恐慌。“Toha”是 XSS 和其他论坛的长期管理员，其历史可以追溯到 2005 年，当时他与人共同创立了 Hack-All。后来，他将其品牌重塑为 exploit[.]in，吸引了许多著名的网络罪犯。

虽然一些证据，包括与一位名叫 Anton Avdeev 的俄罗斯公民的电子邮件地址相关的宝马销售广告，都指向 Avdeev，但年龄上的不一致引起了人们的怀疑。另一种可能性是 Anton Medvedovskiy，他是基辅的一名 38 岁居民，他的详细信息与“Toha”的在线活动相符，包括域名注册和相符的年龄。

这次查抄震动了网络犯罪社区，人们担心当局现在掌握了从缴获的 Jabber 服务器中获得的多年私人信息、联系人列表和用户数据，这可能会暴露许多网络罪犯。一个新的 XSS 论坛已经出现，但受到了怀疑。文章的结论是，乌克兰当局最有可能逮捕了 Anton Medvedovskiy。

---

## 40. 阳光激活的材料将水中的 PFAS 转化为无害的氟化物

**原文标题**: Sunlight-activated material turns PFAS in water into harmless fluoride

**原文链接**: [https://phys.org/news/2025-08-sunlight-material-pfas-harmless-fluoride.html](https://phys.org/news/2025-08-sunlight-material-pfas-harmless-fluoride.html)

阿德莱德大学研究人员开发出一种阳光激活材料，可有效将水中全氟烷基和多氟烷基物质（PFAS）降解为无害成分，包括氟化物。这项发表在《小型》杂志上的突破性成果，为解决 PFAS 广泛污染问题提供了一种有前景的低能耗方案。

PFAS 广泛应用于不粘炊具和灭火泡沫等多种产品中，由于其强大的碳-氟键，在环境和人体内具有极强的持久性，导致发育障碍和癌症等健康问题。令人担忧的是，相当一部分人群的血液中可以检测到 PFAS，这促使人们制定了更严格的饮用水标准。

这种新材料可以靶向并分解 PFAS 分子中的保护性氟原子，从而实现对这些“永久化学品”的完全降解。由此产生的氟化物有可能被重新用于牙膏等医疗保健产品或作为肥料添加剂。研究团队设想将这种材料作为 PFAS 处理链的一部分，首先浓缩水中的 PFAS，然后使用光激活材料进行降解。目前的研究重点是提高材料的稳定性，以便大规模应用。

---

## 41. 员工发现问题有益于企业，但领导者却助长了奉承者。

**原文标题**: Employees spotting problems help the business, but leaders empower flatterers

**原文链接**: [https://phys.org/news/2025-07-employees-problems-bottom-line-leaders.html](https://phys.org/news/2025-07-employees-problems-bottom-line-leaders.html)

为什么溜须拍马者比摇船者更易获得授权？——通过威胁和目标一致性认知考察建言和帮助对授权型领导的影响

---

## 42. Ratfactor图解整理床笠指南

**原文标题**: Ratfactor's illustrated guide to folding fitted sheets

**原文链接**: [https://ratfactor.com/cards/fitted-sheets](https://ratfactor.com/cards/fitted-sheets)

本文是Ratfactor图文并茂的床笠折叠指南，旨在揭示折叠的奥秘，并提供一种简单有效的方法。文章认为床笠是可以被驯服并折叠成整齐的捆状物的。本指南强调理解原理是关键，而非仅仅追求速度。

文章首先介绍了一种简单但繁琐的方法：将床笠反面朝上铺平，然后像纸一样将其折叠成三等份。然后，文章转向一种更有效的“手臂操作，收集角部”的方法。这种方法包括收集角部，强调对齐和嵌套角部的重要性，以避免缠结和挫败感。这种手臂操作方法的核心是将你的双手放在两个角上，让它们“亲吻”，然后将其中一个角翻转到另一个角上。找到剩下的两个角，对齐它们，最后，将所有四个角都集中到一只手臂上。然后将床笠放下，拉直，并像普通床单一样折叠。

本指南还包括有用的插图，并警告了一种常见的错误技巧，即单独包裹每个角部，这会导致缠结。文章最后简要介绍了床笠设计的历史以及相关的专利信息。作者强调，在折叠之前将床笠整理成“四分之一床笠”的形状对于获得整洁、易于管理的捆状物至关重要。

---

## 43. 我想要一切本地化——构建我的离线AI工作空间

**原文标题**: I want everything local – Building my offline AI workspace

**原文链接**: [https://instavm.io/blog/building-my-offline-ai-workspace](https://instavm.io/blog/building-my-offline-ai-workspace)

本文介绍了构建完全本地化AI工作空间的历程，旨在实现隐私保护和摆脱对ChatGPT等云服务的依赖。其核心思想是在本地运行LLM，在隔离的容器中执行代码，并通过无头浏览器访问互联网，所有这些都不会泄露用户数据。

技术栈包括：

*   **LLM:** 用于本地模型的Ollama。
*   **前端UI:** assistant-ui。
*   **沙盒VM运行时:** Apple的`container`。
*   **编排:** coderunner。
*   **浏览器自动化:** Playwright。

作者最初尝试创建一个原生Mac应用程序，但最终选择了基于Web版本的assistant-ui。他们在使用Ollama的工具支持以及Apple `container`工具在镜像构建过程中的不稳定时遇到了挑战。

他们成功地在容器内部署了一个Jupyter服务器，将其作为MCP工具公开，并集成了Playwright进行浏览器自动化。这种设置支持在安全、容器化的环境中执行诸如研究、图表生成、视频/图像编辑以及从GitHub安装工具等任务。卷映射确保了主机和容器之间的数据持久性，而不会将主机系统暴露于代码执行。

该系统目前仅适用于Apple Silicon，需要改进UI，并且面临浏览器机器人检测方面的挑战。尽管存在这些限制，该项目代表着向本地、私有计算的转变，旨在为用户提供无需依赖云服务即可执行任务的工具。 coderunner-ui的代码可在GitHub上找到。

---

## 44. 更小的P快速Trie树

**原文标题**: P-fast trie, but smaller

**原文链接**: [https://dotat.at/@/2025-08-06-p-fast-trie.html](https://dotat.at/@/2025-08-06-p-fast-trie.html)

本文介绍了一种“p-快速 trie”的简化修订版，这是一种 x-快速 trie 的宽扇出变体，用于高效地存储和搜索按字典顺序排列的名称（来自小字符集的字符序列）。其目标是在 O(log k) 时间内找到查询字符串的最长匹配前缀、最近前驱或后继，其中 k 是键的长度。

该 trie 在哈希表中存储名称的前缀。每个条目都包含对按字典顺序大于或等于该前缀的最接近名称的引用、前缀长度（由名称和长度暗示）以及一个位图，指示在前缀之后可能存在的下一个字符，这些字符也是 trie 中的前缀。

搜索涉及对查询字符串长度进行二分查找，检查哈希表中是否存在该前缀。如果找到，位图确定是否扩展该前缀。如果未找到，则减少前缀长度。

本文概述了一种前驱搜索算法，该算法将查询字符串与哈希表条目关联的完整名称进行比较。它包括找到位图中小于查询字符串的下一个字符的最大字符，并可能一次一个字符地向下遍历前驱子 trie。

作者将 p-快速 trie 与 qp-trie 进行比较，估计 p-快速 trie 对于精确匹配需要更少的哈希表探测（大约 3-9 次），而 qp-trie 的深度为 7-15 次。但是，p-快速 trie 中的前驱搜索可能需要更多的探测，这可能会使叶子对象的链表成为更实用的解决方案。作者承认难以准确估计哈希表探测和 qp-trie 指针追踪的相对性能。

---

## 45. LLMs并非世界模型

**原文标题**: LLMs Aren't World Models

**原文链接**: [https://yosefk.com/blog/llms-arent-world-models.html](https://yosefk.com/blog/llms-arent-world-models.html)

本文认为，尽管大型语言模型（LLMs）具有令人印象深刻的能力，但其本质上并非“世界模型”。作者通过例子佐证了这一观点，这些例子表明LLMs在基本的推理和理解现实世界概念方面存在不足。

第一个例子是国际象棋，其中LLM很快就会失去对棋盘状态的跟踪，并做出非法移动，这突显了它尽管接触了无数的国际象棋游戏，却无法掌握游戏核心规则的能力。第二个例子剖析了LLM如何错误地解释图像编辑器中的“正常混合模式”，揭示了其对基本计算原理和透明度工作方式的理解不足。

作者探讨了更复杂的场景，如alpha混合结合律和Python中的线程安全，进一步证明了LLMs推理的不一致性和提供不正确信息的倾向，即使在面对矛盾的证据时也是如此。

作者承认，LLMs确实学习到了世界的某些方面，例如token嵌入中的性别代表。然而，他强调这种学习是偶然且不可靠的。他预测未来机器学习的突破将创造真正的“世界模型”，并允许从更少的数据中学习，类似于人类的学习方式。

最终，作者得出结论，LLMs并非通往通用机器智能的道路，并且在某种程度上是一种干扰，因为它们能够在没有真正理解的情况下执行复杂的任务。他预计LLMs将继续在代码理解、知识验证以及在新情况下的可靠推理方面挣扎。尽管存在这些局限性，他承认LLMs在特定领域（如校对和基本问答）的实用性。

---

## 46. 一个以人工智能为先导，围绕新型编程语言构建的程序合成框架

**原文标题**: An AI-first program synthesis framework built around a new programming language

**原文链接**: [https://queue.acm.org/detail.cfm?id=3746223](https://queue.acm.org/detail.cfm?id=3746223)

本文介绍 Universalis，一种全新的 AI 优先编程语言，旨在让领域专家能够阅读，并由机器（特别是 LLM）编写。该语言是 AI 驱动的程序合成框架的一部分，旨在帮助知识工作者轻松地对 AI 系统进行编程。

Universalis 脚本的结构类似于自然语言，使用模仿 Excel 公式的语法，并结合了自然语言解释。这种设计优先考虑可读性而非语法复杂性，使没有正式编程背景的用户也能访问。Universalis 构建于 Prolog 之上，并使用“对冲”（\[...]) 来包含逻辑谓词。

Universalis 的主要功能包括：

*   **前置和后置条件：** 允许嵌入逻辑约束和数据验证规则，增强 AI 安全性并实现错误检测。
*   **条件语句：** 以清单格式呈现条件逻辑，并附带自然语言解释，使决策点清晰直观。
*   **无循环编程：** 隐式地在值集合上广播操作，简化批量处理，并消除对显式循环的需求。
*   **查询理解：** 通过结构化的自然语言方法实现高级数据操作（过滤、分组、聚合），简化像 SQL 这样的复杂查询。

本文将 Universalis 与传统的编程语言和工具（如 SQL 和 Excel）进行了对比，突出了它对非程序员来说卓越的可读性和易用性。目标是弥合自然语言问题描述和可执行代码之间的差距，使 AI 编程更易于访问和用户友好。

---

## 47. ESP32 Bus Pirate 0.5 – 一款通吃所有协议的硬件黑客工具

**原文标题**: ESP32 Bus Pirate 0.5 – A hardware hacking tool that speaks every protocol

**原文链接**: [https://github.com/geo-tp/ESP32-Bus-Pirate](https://github.com/geo-tp/ESP32-Bus-Pirate)

ESP32 Bus Pirate 0.5 是一个开源固件，可将 ESP32 设备转换为多功能的硬件黑客工具，灵感来自原始 Bus Pirate。它允许用户通过串行终端或基于 Web 的 CLI 嗅探、发送、编写脚本并与各种数字协议（如 I2C、UART、SPI、1-Wire 等）进行交互。

主要功能包括交互式 CLI（USB 串行或 WiFi Web）、支持不同协议的各种模式（I2C、SPI、UART 等）、针对 I2C、Wi-Fi、蓝牙和 1-Wire 的嗅探功能、使用字节码指令进行脚本编写、用于红外协议的 Device-B-Gone 命令以及直接 I/O 管理。它支持 ESP32 S3 Dev Kit、M5 设备（Cardputer、Stick C Plus 2、Atom S3 Lite、Stamp S3）和 LILYGO T-Embed 型号等设备。

文章鼓励用户查阅 Wiki，以获取有关模式、命令、指令语法和 Python 脚本示例的详细文档。入门包括刷写固件、通过串行或 Web 接口连接以及使用诸如“mode”、“help”和“scan”之类的命令。 它强调了 Web 和串行接口的优点，指出 Web 接口的可访问性以及串行接口的速度。

文章还提供了一种为项目做出贡献的方式，并警告不要使用超出 3.3V 或 5V 的电压电平，以避免损坏 ESP32。

---

## 48. 生命游戏中一个简单的CPU (2021)

**原文标题**: A Simple CPU on the Game of Life (2021)

**原文链接**: [https://nicholas.carlini.com/writing/2021/unlimited-register-machine-game-of-life.html](https://nicholas.carlini.com/writing/2021/unlimited-register-machine-game-of-life.html)

尼古拉斯·卡里尼的文章《生命游戏上的简易CPU - 第四部分》详细介绍了在康威生命游戏中构建一个两级流水线无限寄存器机（URM）。该URM是一个图灵完备的CPU，具有四个指令：递增、递减、非零跳转和空操作。

该CPU包含几个关键组件：用于同步的时钟、保存16个四位寄存器的寄存器文件、能够进行递增和递减的算术逻辑单元（ALU）、程序计数器以及能够存储128条指令的ROM。 两级流水线允许同时进行指令获取和执行，从而显着提高速度。输出通过四个7段显示器显示。

本文重点介绍了生命游戏特有的设计考虑因素，其中最小化电路的总长度（滑翔机移动距离）至关重要，这与传统硬件设计侧重于最小化晶体管不同。生命游戏中的确定性时序允许精确依赖于导线长度来排序操作。作者详细介绍了ALU和寄存器文件的构建，包括专为高效布局和最小化占用空间而设计的专用逻辑门。 ROM将指令编码为二维AND门网格，并提供了一种读取数据的方法。最后，本文介绍了指令执行以及如何处理跳转指令和两级流水线。

---

## 49. GPTs与被抛下的感觉

**原文标题**: GPTs and Feeling Left Behind

**原文链接**: [https://whynothugo.nl/journal/2025/08/06/gpts-and-feeling-left-behind/](https://whynothugo.nl/journal/2025/08/06/gpts-and-feeling-left-behind/)

作者表达了在GPTs等人工智能编码工具的快速发展面前感到不足和落后的情绪。虽然他们看到了围绕人工智能辅助开发的炒作，但他们的个人体验却令人失望。他们发现GPTs在寻找合适的词语或类型注释，以及调试特定函数等小任务时很有帮助。然而，在处理更大、更复杂的任务时，作者将输出描述为“毫无用处的垃圾”，通常依赖于不存在的库，并在尝试修复时引入新的错误。

核心问题是作者的经验与包括经验丰富的开发者在内的其他人所报告的成功之间存在脱节。他们努力调和自己的失败与这些工具被认为具有的力量和效率之间的矛盾，从而导致沮丧。他们强调了广告宣传的潜力与他们遇到的实际局限性之间的差距，并用“坚不可摧的锤子”结果却脆弱而无效的比喻。这表明一种担忧，即当前人工智能编码更多的是关于外观和炒作，而不是对于复杂开发任务的实际、可靠的效用。作者感到有适应这些工具的压力，但却发现它们并没有真正帮助，这让他们觉得现有的技能正在变得过时，而没有可行的替代品。

---

## 50. R0ML的比率

**原文标题**: R0ML's Ratio

**原文链接**: [https://blog.glyph.im/2025/08/r0mls-ratio.html](https://blog.glyph.im/2025/08/r0mls-ratio.html)

本文介绍R0ML比率 (RR)，这是一种评估批量采购以确定折扣是否真正划算的方法。作者将该概念归功于他们的父亲“R0ML”。

RR的计算方法是将整个企业批量许可协议的总价 (TPotEEVLA) 除以使用的单位的全额未折扣零售标价 (FURLPoUU)。FURLPoUU的确定方法是将单个单位的零售价格乘以*实际*使用的单位数量。

核心概念是，如果购买的数量未得到充分利用，那么大幅折扣可能并非有益。如果RR小于1，则交易是好的。如果RR大于1，则采购不划算。

文章用一个幽默的例子来说明这一点，一个马戏团购买了10,000个小丑鼻子。虽然50%的折扣听起来很棒，但如果只有200个小丑戴上鼻子，则RR会变得很高 (25)，表明这是一项糟糕的投资。

作者认为，这在软件许可和SaaS交易中尤其重要，因为未使用的许可证不提供任何价值。他们主张允许员工最初进行个人购买，以确定实际使用情况，然后再承诺大量批量折扣。这确保了R0ML比率保持在1.0，避免了“傻瓜”情况。

---

## 51. MCP忽视了分布式系统来之不易的教训。

**原文标题**: MCP overlooks hard-won lessons from distributed systems

**原文链接**: [https://julsimon.medium.com/why-mcps-disregard-for-40-years-of-rpc-best-practices-will-burn-enterprises-8ef85ce5bc9b](https://julsimon.medium.com/why-mcps-disregard-for-40-years-of-rpc-best-practices-will-burn-enterprises-8ef85ce5bc9b)

本文批评旨在成为AI工具交互标准的模型上下文协议（MCP）忽视了分布式系统中数十年来既定的最佳实践。作者认为，MCP优先考虑易于采用，而非运营稳健性，这为部署它的企业埋下了一颗“定时炸弹”。

本文重点指出了MCP的几个不足之处，并将其与UNIX RPC、CORBA、REST、SOAP和gRPC等成熟技术进行了比较。主要缺陷包括缺乏强大的类型安全、跨语言实现的不一致性、安全措施不足、缺乏内置可观察性（分布式追踪）、无法追踪AI成本归属，以及关键的运营缺陷，如服务发现和版本管理。

作者批评了依赖大量第三方库来解决这些缺陷的“拼凑式”方法，认为这造成了碎片化，并增加了企业采用的复杂性和成本。在新MCP版本中不断对关键特性进行追溯性改进，被视为过早发布的承认。

最终，作者警告说，MCP以牺牲稳健性为代价专注于简单性，这将使企业面临痛苦的生产故障，尤其是在安全关键和收入关键的系统中。文章最后概述了使MCP达到既定分布式系统原则所需的即时、短期和长期改进。

---

## 52. 电费上涨，更多证据表明数据中心难辞其咎

**原文标题**: As electric bills rise, evidence mounts that data centers share blame

**原文链接**: [https://apnews.com/article/electricity-prices-data-centers-artificial-intelligence-fbf213a915fb574a4f3e5baaa7041c3a](https://apnews.com/article/electricity-prices-data-centers-artificial-intelligence-fbf213a915fb574a4f3e5baaa7041c3a)

美联社文章《电费上涨，证据表明数据中心难辞其咎》指出，在人工智能和云计算需求不断增长的推动下，数据中心的快速增长正在显著推高电价。这些高耗能设施需要大量电力来运行和保持服务器冷却，从而给现有电网带来压力并推高需求。

文章强调，虽然数据中心对现代技术至关重要，但在关于公用事业成本上涨的讨论中，它们的能源消耗往往被忽视。文章引用了具体的例子，表明数据中心高度集中的地区，其居民和商业用户的电价正经历着不成比例的增长。

文章还指出，数据中心需求的增加正在促使公用事业公司建造新的发电厂，这些发电厂通常以天然气为燃料，进一步增加了碳排放，并可能延缓向可再生能源的过渡。虽然一些数据中心运营商正在投资可再生能源以抵消其消耗，但文章认为这些努力往往不足以跟上其不断增长的能源需求。

最后，文章暗示需要更大的透明度和监管来解决这个问题。它呼吁更仔细地审查数据中心的能源消耗及其对电价的影响，以及促进数据中心行业内节能和可再生能源采用的策略。最终，文章认为，对数据中心日益增长的依赖正在加剧能源成本上涨的问题，并需要一种更全面的方法来管理它们的能源足迹。

---

## 53. 跑题的重要性

**原文标题**: The importance of offtopic

**原文链接**: [https://blog.tadzik.net/the-importance-of-offtopic.html](https://blog.tadzik.net/the-importance-of-offtopic.html)

本文论证了在远程工作环境中进行“非工作相关”互动至关重要。作者作为一名资深远程工作者，分享了自身经历，强调了类似于实体办公室厨房的轻松线上空间如何培养友谊、理解，并最终促进更好的工作。

作者将Opera公司和一家咨询公司的积极体验（非工作频道蓬勃发展）与一家客户公司的消极体验进行了对比，后者强制使用摄像头，但未能培养真正的联系。他们还回忆起加入一家以远程优先为导向的公司，该公司吹嘘其非工作相关举措，但未能培养一种让员工感到舒适参与其中的文化。

核心论点是，从工作中移除人为因素会降低其价值。实体公司通过厨房、游戏室和其他非正式空间直观地理解这一点。然而，许多远程公司未能在线上复制这一点，导致了无趣的工作环境。作者强调，仅仅创建非工作频道是不够的；领导层必须积极参与并鼓励非正式互动，以建立一种让员工感到舒适参与其中的文化。否则，新员工会避开这些频道，从而使这种循环长期存在。

作者最后批评那些推动重返办公室的公司，认为这是管理失败的标志，尤其是因为开源社区几十年来已经成功地培养了强大的远程连接。他们认为，有效的远程工作并不复杂，但需要有意识地培养非正式的、非工作相关的互动。

---

## 54. 我如何使用 Tailscale

**原文标题**: How I use Tailscale

**原文链接**: [https://chameth.com/how-i-use-tailscale/](https://chameth.com/how-i-use-tailscale/)

本文详细介绍了作者使用Tailscale连接设备和服务的经验。Tailscale是一个WireGuard编排服务，通过消除复杂的网络配置和密钥管理，简化了VPN连接。作者使用它从任何地方访问树莓派托管的家庭自动化服务。

除了基本的连接功能之外，本文还重点介绍了Tailscale的功能，例如将单个服务暴露为节点，用于自动DNS条目的MagicDNS，以及用于公开共享本地开发项目的“漏斗”功能。“serve”命令在tailnet内提供类似的功能。

作者讨论了最初使用GitHub进行身份验证的繁琐过程，以及随后切换到自托管KeyCloak OIDC提供程序以获得更流畅和可控的登录体验。Tailscale能够通过HTTP标头将用户信息传递给服务，从而可以实现对Grafana、Miniflux和Linkding等应用程序的无密码登录。

作者还讲述了关于Tailscale ACL和标签的学习经历。最初，缺乏ACL导致潜在的安全漏洞。然而，不正确的标签应用导致作者无法访问自己的设备。一个经过修改的标签系统，结合Tailscale的授权，现在根据设备类型（用户、服务器、应用、集成）限制访问，在不影响可用性的前提下提高了安全性。

最后，本文提到了Tailscale的其他功能，如出口节点和Tailscale锁，强调了慷慨的免费个人计划，以及作者对Tailscale管理服务器和私有应用程序的依赖。

---

## 55. 一致性优先于可用性：rqlite 如何处理 CAP 理论

**原文标题**: Consistency over Availability: How rqlite Handles the CAP theorem

**原文链接**: [https://philipotoole.com/consistency-over-availability-how-rqlite-handles-the-cap-theorem/](https://philipotoole.com/consistency-over-availability-how-rqlite-handles-the-cap-theorem/)

本文解释了 rqlite（一个基于 SQLite 和 Go 构建的分布式关系数据库）如何处理 CAP 定理。 CAP 定理指出，分布式数据库只能保证一致性 (Consistency)、可用性 (Availability) 和分区容错性 (Partition Tolerance) 三者中的两个。

rqlite 优先考虑一致性和分区容错性 (CP)。 它使用 Raft 共识协议，确保在发生网络分区时，只有拥有大多数节点的节点保持活动状态，从而保证可用节点之间的数据一致性。 少数节点会停止接受请求，直到分区得到解决并且数据同步。

虽然本质上是一个 CP 系统，但 rqlite 通过可选择的读取一致性级别，提供了对一致性和可用性之间权衡的细粒度控制：

*   **弱（默认）：** 读取速度快，检查本地状态以确认领导权。 存在少量数据过期的风险。
*   **强：** 一致性最高，读取请求通过 Raft 日志，性能损失很大，主要用于测试。
*   **线性化：** 一致性和性能的最佳平衡。 领导者在读取之前，会与法定数量的追随者确认其状态。
*   **无：** 读取速度最快，节点查询本地 SQLite 数据库而无需集群检查，无法保证数据新鲜度。

这些读取一致性级别允许开发人员根据特定的应用程序需求定制 rqlite 的行为，从而平衡性能和数据准确性。 本文鼓励进一步探索 rqlite 的文档和社区，以获得更深入的理解和实践实施。

---

## 56. 这辆车跑了超过120万公里，而且仍然性能良好

**原文标题**: Car has more than 1.2M km on it – and it's still going strong

**原文链接**: [https://www.cbc.ca/news/canada/nova-scotia/1985-toyota-tercel-high-mileage-1.7597168](https://www.cbc.ca/news/canada/nova-scotia/1985-toyota-tercel-high-mileage-1.7597168)

新斯科舍省的安迪·坎贝尔拥有一辆1985年的丰田特塞尔，行驶里程超过120万公里，相当于往返月球1.5次。由于里程表位数不够，只显示253,070公里。坎贝尔于1990年购买了这辆车，当时里程为125,000公里，此后每天都在使用，每天至少行驶120公里。现在退休后，他仍然经常使用它。

尽管车龄已高，但由于坎贝尔精心维护，车况良好。他亲自进行大部分维修，使用的零件来自他为此目的保留的其他三辆特塞尔。他强调定期维护、底盘装甲和在缝隙中填充油脂以防止生锈。

坎贝尔还拥有一辆备用的1986年特塞尔。他看重他的特塞尔的实用性、雪地可靠性、易于维护和燃油效率，而不是它的地位或外观。他对用它交换任何其他车辆都不感兴趣。另一位新斯科舍省人吉姆·乔治拥有一辆类似的特塞尔，行驶里程超过50万公里，他们知道还有一辆行驶里程超过100万公里。坎贝尔希望他的特塞尔达到200万公里，但不确定他是否能活到实现这个目标。

---

## 57. 我的副业：在域名失效前发送给你可用域名信息的简报

**原文标题**: My side project: a newsletter that sends u available domains before they're gone

**原文链接**: [https://www.namedrop.us/](https://www.namedrop.us/)

Namedrop：一款帮助独立开发者免费查找可用域名的资讯服务。它通过社交媒体和电子邮件发送域名建议。该服务重点推荐最近可用的域名，通常强调易于品牌化、简短或单字的选项。

最近的例子包括 "Optimum.sh"、"Altius.so" 和 "Dormant.ai"。Namedrop 还提供 .com 以外的其他可用域名后缀信息，如 .app、.fm、.sh、.so、.ai、.xyz、.me 和 .dev，迎合了初创企业和独立开发者社区的需求。该资讯明确敦促快速行动，强调优质域名的稀缺性，并鼓励用户立即注册感兴趣的域名。

该服务此前曾提供过 "Focality.org" 和 "Paveway" 等各种后缀的域名。它还会提醒用户之前推荐的域名不再可用，有时会为同一个关键词推荐替代后缀，如 "Prowess" 所示。该资讯还设有 "Twitter Drops" 栏目，分享在 Twitter 上发布的域名建议。

---

## 58. 沙尘暴 - 可自托管的 Web 效率套件

**原文标题**: Sandstorm- self-hostable web productivity suite

**原文链接**: [https://sandstorm.org/](https://sandstorm.org/)

沙尘暴是一个开源的网络效率套件，旨在方便安全地自主托管网络应用程序。 它简化了开源应用程序的安装和管理过程，类似于在手机上使用应用商店，并提供自动更新。

主要功能包括集中式访问控制，确保所有应用程序和数据的一致安全性，以及独特的“颗粒”系统。 每个文档、聊天室或其他项目都包含在安全沙箱中，从而显著降低了漏洞风险。 用户可以完全控制其数据位置，选择在云服务或自己的机器上托管，并且可以轻松地在选项之间迁移。

沙尘暴避免了供应商锁定，允许用户组合来自不同开发者的应用程序，甚至集成自定义应用程序。 该平台面向寻求安全和私密的开源网络应用程序的个人、旨在集中数据并增强团队能力的企业，以及希望以简化的方式分发和运行其应用程序而无需复杂的服务器管理的开发人员。

---

## 59. 在布鲁克林公寓安装迷你分体式空调

**原文标题**: Installing a mini-split AC in a Brooklyn apartment

**原文链接**: [https://probablydance.com/2025/08/04/installing-a-mini-split-ac-in-a-brooklyn-apartment/](https://probablydance.com/2025/08/04/installing-a-mini-split-ac-in-a-brooklyn-apartment/)

马尔特·斯卡鲁普克详述了他在2024年用迷你分体空调系统替换其布鲁克林公寓中四个噪音大、效率低的PTAC（单体式空调）的经历。 该项目由高昂的电费（高达每月1200美元）和有故障的PTAC驱动，耗资约4万美元，包括修补PTAC孔洞。 虽然不太可能仅通过节能收回成本，但好处包括更安静的运行和更稳定的温度。

由于前任房主最近安装了PTAC，作者感叹错过了7000美元的政府退税。 寻找可靠的承包商颇具挑战性，最初的报价从31,000美元到53,000美元不等。 他最终选择了冰河时代公司进行空调安装，并聘请了另一家承包商来修补墙壁。

最初预计需要两周的安装过程，由于延误和沟通不畅，延长到了一个多月。 作者积极参与了关于机组放置和管道布线的决策。 更换PTAC涉及封闭煤气管道，这导致水管工在协商出合理价格之前哄抬价格。

虽然新的迷你分体系统运行完美，但作者对未能实现显著的节能效果表示失望。 高电费仍然存在，可能是由于不良的绝缘和空气泄漏造成的。 尽管如此，他对结果总体上感到满意，并提到舒适度和安静度的提高。 他还警告说，蚂蚁有可能通过修补过的窗户周围的缝隙进入。

---

## 60. 突破性进展的时代已经结束了吗？[视频]

**原文标题**: The era of boundary-breaking advancements is over? [video]

**原文链接**: [https://www.youtube.com/watch?v=hkAH7-u7t5k](https://www.youtube.com/watch?v=hkAH7-u7t5k)

无法访问文章链接。

---

## 61. 在音乐节测试Bitchat

**原文标题**: Testing Bitchat at the music festival

**原文链接**: [https://primal.net/saunter/testing-bitchat-at-the-music-festival](https://primal.net/saunter/testing-bitchat-at-the-music-festival)

文章《音乐节上的Bitchat测试》记录了Bitchat应用程序的一个明显测试阶段。极其有限的内容表明，作者本意是提供关于在音乐节特定环境下使用或评估Bitchat的信息。然而，“您需要启用JavaScript才能运行此应用程序”强烈表明该文章不完整或需要JavaScript才能正确显示其内容。在不启用Javascript且假设这是唯一限制信息的原因下，无法确定测试的细节、在音乐节进行评估的目的，或者与应用程序在该环境中的性能或可用性相关的任何具体发现。因此，不可能做出全面的总结。唯一可以确定的是，该文章似乎旨在记录Bitchat应用程序在音乐节上的测试或用例，但在没有进一步互动或JavaScript功能的情况下无法访问。

---

## 62. Caligra 工作台

**原文标题**: Caligra Workbench

**原文链接**: [https://caligra.com/workbench/](https://caligra.com/workbench/)

Caligra Workbench：专为技术工作站定制的Linux操作系统。其主要目标是通过减少干扰并创建对开发者友好的环境来提高生产力。该操作系统具有以性能为中心的用户界面，旨在优化开发者体验。本质上，Caligra Workbench旨在通过提供简化而高效的工作环境，使团队能够更有效地交付成果。

---

## 63. 成人网站在SVG文件中藏匿漏洞利用代码

**原文标题**: Adult sites are stashing exploit code inside svg files

**原文链接**: [https://arstechnica.com/security/2025/08/adult-sites-use-malicious-svg-files-to-rack-up-likes-on-facebook/](https://arstechnica.com/security/2025/08/adult-sites-use-malicious-svg-files-to-rack-up-likes-on-facebook/)

色情网站正利用恶意的.svg图像文件，秘密地为其帖子生成Facebook点赞。安全公司Malwarebytes发现，这些.svg文件包含混淆的JavaScript代码，该代码在执行时会下载一系列额外的脚本。最终的脚本被识别为Trojan.JS.Likejack，它会强制浏览器“喜欢”特定的Facebook帖子，而无需用户的知晓或同意，前提是用户已登录Facebook。

.svg格式基于XML，允许嵌入HTML和JavaScript，其灵活性正被利用。该代码使用自定义版本的JSFuck进行了大量混淆，从而使分析更加困难。

这种策略允许这些网站人为地增加其在Facebook上的受欢迎程度。虽然Facebook会定期关闭参与此类滥用的帐户，但肇事者会迅速使用新的个人资料卷土重来。这并非首次使用.svg文件进行恶意活动。过去的事件包括跨站脚本攻击和网络钓鱼攻击。Malwarebytes已识别出数十个参与此点赞劫持计划的基于WordPress的色情网站。

---

## 64. Jan – 带有本地UI的Ollama替代方案

**原文标题**: Jan – Ollama alternative with local UI

**原文链接**: [https://github.com/menloresearch/jan](https://github.com/menloresearch/jan)

Jan 是一款本地 AI 助手，允许用户直接在设备上下载并运行 Llama、Gemma 和 Qwen 等大型语言模型 (LLM)，确保隐私和控制。它提供用户友好的界面，并能连接到 OpenAI、Anthropic、Mistral 和 Groq 等基于云的 AI 服务。用户可以创建自定义 AI 助手，并利用与 OpenAI 兼容的 API 与其他应用程序集成。

安装过程简单直接，提供适用于 Windows、macOS 和 Linux 的预构建二进制文件。对于开发者，可以使用 Make 或 Mise 从源代码构建 Jan，从而简化 Node.js 和 Rust 的依赖管理。

系统要求包括 macOS 13.6+（RAM 因模型大小而异）、带有 GPU 支持的 Windows 10+，以及与大多数 Linux 发行版的兼容性。该项目欢迎贡献，提供全面的文档，并通过 Discord 提供社区支持。主要功能包括本地 AI 模型执行、云集成、自定义助手创建，以及对隐私的关注。它在 Apache 2.0 许可下运营，并感谢对 Llama.cpp、Tauri 和 Scalar 的依赖。

---

## 65. GPT-5：“蓝莓里出现多少次字母b？”

**原文标题**: GPT-5: "How many times does the letter b appear in blueberry?"

**原文链接**: [https://bsky.app/profile/kjhealy.co/post/3lvtxbtexg226](https://bsky.app/profile/kjhealy.co/post/3lvtxbtexg226)

基兰·希利在Bluesky上发帖，描述了他用GPT-5进行的一项实验，似乎引用了一个与“蓝莓”相关的流行或新兴查询。他表示他“不得不亲自尝试一下‘蓝莓’的事情”，暗示存在一个涉及该词和生成式AI的预先存在的趋势或挑战。然后他只是简单地表示他正在报告结果，但没有详细说明GPT-5的响应是什么或实验的重点是什么。该帖子内容极简，表明读者应该已经理解了围绕“蓝莓”现象和GPT-5的背景。该帖子的时间戳为2025年8月8日，表明在撰写本文时是一个未来的日期。“GPT5”的使用表明了OpenAI的GPT系列的下一代模型。所包含的JavaScript要求强调了Bluesky平台的互动性质。

---

## 66. Hyprland - 一个独立的动态平铺Wayland合成器

**原文标题**: Hyprland – An independent, dynamic tiling Wayland compositor

**原文链接**: [https://hypr.land/](https://hypr.land/)

本文宣布将于2025年7月28日推出与Hyprland相关的“Hyprperks”。 Hyprland是一个独立的动态平铺Wayland合成器。 本文未详细说明Hyprperks究竟*是什么*。 然而，标题和第一句话表明它们是与Hyprland合成器相关的一项新功能、程序或福利。 鉴于Hyprland被描述为“动态平铺Wayland合成器”，这些福利很可能面向参与或对这种特定类型的Wayland环境感兴趣的开发者、用户或贡献者。

---

## 67. 当政客干预经济数据时会发生什么：阿根廷的例子

**原文标题**: What Happens When Politicians Meddle with Economic Data: Argentina's Example

**原文链接**: [https://www.wsj.com/economy/trump-jobs-economic-data-risk-e4b7410b](https://www.wsj.com/economy/trump-jobs-economic-data-risk-e4b7410b)

无法访问文章链接。

---

## 68. Suzhou Imperial Kiln Ruins Park and Museum of Imperial Kiln Brick (2018)

**原文标题**: Suzhou Imperial Kiln Ruins Park and Museum of Imperial Kiln Brick (2018)

**原文链接**: [https://www.theplan.it/eng/award-2018-Culture/suzhou-imperial-kiln-ruins-park-museum-of-imperial-kiln-brick-1](https://www.theplan.it/eng/award-2018-Culture/suzhou-imperial-kiln-ruins-park-museum-of-imperial-kiln-brick-1)

生成摘要时出错

---

## 69. Ultrathin business card runs a fluid simulation

**原文标题**: Ultrathin business card runs a fluid simulation

**原文链接**: [https://github.com/Nicholas-L-Johnson/flip-card](https://github.com/Nicholas-L-Johnson/flip-card)

生成摘要时出错

---

## 70. Mexico to US livestock trade halted due to screwworm spread

**原文标题**: Mexico to US livestock trade halted due to screwworm spread

**原文链接**: [https://www.usda.gov/about-usda/news/press-releases/2025/07/09/secretary-rollins-takes-decisive-action-and-shuts-down-us-southern-border-ports-livestock-trade-due](https://www.usda.gov/about-usda/news/press-releases/2025/07/09/secretary-rollins-takes-decisive-action-and-shuts-down-us-southern-border-ports-livestock-trade-due)

生成摘要时出错

---

## 71. Steve Wozniak's Perforated Pads of $2 Bills (2015)

**原文标题**: Steve Wozniak's Perforated Pads of $2 Bills (2015)

**原文链接**: [https://www.coinbooks.org/esylum_v18n36a40.html](https://www.coinbooks.org/esylum_v18n36a40.html)

生成摘要时出错

---

## 72. Claude Code IDE integration for Emacs

**原文标题**: Claude Code IDE integration for Emacs

**原文链接**: [https://github.com/manzaltu/claude-code-ide.el](https://github.com/manzaltu/claude-code-ide.el)

生成摘要时出错

---

## 73. Goodbye, Six-Figure Tech Jobs. Young Coders Seek Work at Fast-Food Joints

**原文标题**: Goodbye, Six-Figure Tech Jobs. Young Coders Seek Work at Fast-Food Joints

**原文链接**: [https://www.nytimes.com/2025/08/10/technology/coding-ai-jobs-students.html](https://www.nytimes.com/2025/08/10/technology/coding-ai-jobs-students.html)

生成摘要时出错

---

## 74. Every company has the same hiring criteria

**原文标题**: Every company has the same hiring criteria

**原文链接**: [https://ethanding.substack.com/p/every-company-has-the-same-hiring](https://ethanding.substack.com/p/every-company-has-the-same-hiring)

生成摘要时出错

---

## 75. Our European search index goes live

**原文标题**: Our European search index goes live

**原文链接**: [https://blog.ecosia.org/launching-our-european-search-index/](https://blog.ecosia.org/launching-our-european-search-index/)

生成摘要时出错

---

## 76. Let's properly analyze an AI article for once

**原文标题**: Let's properly analyze an AI article for once

**原文链接**: [https://nibblestew.blogspot.com/2025/08/lets-properly-analyze-ai-article-for.html](https://nibblestew.blogspot.com/2025/08/lets-properly-analyze-ai-article-for.html)

生成摘要时出错

---

## 77. Happy BuyNothing Day

**原文标题**: Happy BuyNothing Day

**原文链接**: [https://justbuynothing.com/](https://justbuynothing.com/)

生成摘要时出错

---

## 78. Italy OKs $15.5B project to build suspension bridge from mainland to Sicily

**原文标题**: Italy OKs $15.5B project to build suspension bridge from mainland to Sicily

**原文链接**: [https://apnews.com/article/italy-messina-bridge-sicily-calabria-meloni-nato-1a19e957e303c46ff51214d54a2dc6d7](https://apnews.com/article/italy-messina-bridge-sicily-calabria-meloni-nato-1a19e957e303c46ff51214d54a2dc6d7)

生成摘要时出错

---

## 79. Design Patterns for Securing LLM Agents Against Prompt Injections

**原文标题**: Design Patterns for Securing LLM Agents Against Prompt Injections

**原文链接**: [https://arxiv.org/abs/2506.08837](https://arxiv.org/abs/2506.08837)

生成摘要时出错

---

## 80. One-Handed Keyboard

**原文标题**: One-Handed Keyboard

**原文链接**: [https://github.com/htx-studio/One-Handed-Keyboard](https://github.com/htx-studio/One-Handed-Keyboard)

生成摘要时出错

---

## 81. 'It's a Mess': A Brain-Bending Trip to Quantum Theory's 100th Birthday Party

**原文标题**: 'It's a Mess': A Brain-Bending Trip to Quantum Theory's 100th Birthday Party

**原文链接**: [https://www.quantamagazine.org/its-a-mess-a-brain-bending-trip-to-quantum-theorys-100th-birthday-party-20250808/](https://www.quantamagazine.org/its-a-mess-a-brain-bending-trip-to-quantum-theorys-100th-birthday-party-20250808/)

生成摘要时出错

---

## 82. FidoNet Global HyperText Interface

**原文标题**: FidoNet Global HyperText Interface

**原文链接**: [https://github.com/Mithgol/FGHI-URL/blob/master/FidoURL.txt](https://github.com/Mithgol/FGHI-URL/blob/master/FidoURL.txt)

生成摘要时出错

---

## 83. The Magic of Herding

**原文标题**: The Magic of Herding

**原文链接**: [https://nautil.us/the-magic-of-herding-1229248/](https://nautil.us/the-magic-of-herding-1229248/)

生成摘要时出错

---

## 84. Tribblix – The Retro Illumos Distribution

**原文标题**: Tribblix – The Retro Illumos Distribution

**原文链接**: [http://www.tribblix.org/](http://www.tribblix.org/)

生成摘要时出错

---

## 85. Cordoomceps – Replacing an Amiga’s brain with DOOM

**原文标题**: Cordoomceps – Replacing an Amiga’s brain with DOOM

**原文链接**: [https://mjg59.dreamwidth.org/73001.html](https://mjg59.dreamwidth.org/73001.html)

生成摘要时出错

---

## 86. Btrfs Has Saved Meta "Billions of Dollars" in Infrastructure Costs

**原文标题**: Btrfs Has Saved Meta "Billions of Dollars" in Infrastructure Costs

**原文链接**: [https://www.phoronix.com/news/Btrfs-Saves-Meta-Billions](https://www.phoronix.com/news/Btrfs-Saves-Meta-Billions)

生成摘要时出错

---

## 87. A SPARC makes a little fire

**原文标题**: A SPARC makes a little fire

**原文链接**: [https://www.leadedsolder.com/2025/08/05/sparcstation-scsi-termination-fix-magic-smoke.html](https://www.leadedsolder.com/2025/08/05/sparcstation-scsi-termination-fix-magic-smoke.html)

生成摘要时出错

---

## 88. Isle FPGA Computer: creating a simple, open, modern computer

**原文标题**: Isle FPGA Computer: creating a simple, open, modern computer

**原文链接**: [https://projectf.io/isle/fpga-computer.html](https://projectf.io/isle/fpga-computer.html)

生成摘要时出错

---

## 89. Show HN: Kitten TTS – 25MB CPU-Only, Open-Source TTS Model

**原文标题**: Show HN: Kitten TTS – 25MB CPU-Only, Open-Source TTS Model

**原文链接**: [https://github.com/KittenML/KittenTTS](https://github.com/KittenML/KittenTTS)

生成摘要时出错

---

## 90. Representing Python notebooks as dataflow graphs

**原文标题**: Representing Python notebooks as dataflow graphs

**原文链接**: [https://marimo.io/blog/dataflow](https://marimo.io/blog/dataflow)

生成摘要时出错

---

## 91. Yet Another LLM Rant

**原文标题**: Yet Another LLM Rant

**原文链接**: [https://overengineer.dev/txt/2025-08-09-another-llm-rant/](https://overengineer.dev/txt/2025-08-09-another-llm-rant/)

生成摘要时出错

---

## 92. Perfect pesticide? RNA kills crop-destroying beetles with unprecedented accuracy

**原文标题**: Perfect pesticide? RNA kills crop-destroying beetles with unprecedented accuracy

**原文链接**: [https://www.science.org/content/article/perfect-pesticide-rna-kills-crop-destroying-beetles-unprecedented-accuracy](https://www.science.org/content/article/perfect-pesticide-rna-kills-crop-destroying-beetles-unprecedented-accuracy)

生成摘要时出错

---

## 93. Astronomy Photographer of the Year 2025 shortlist

**原文标题**: Astronomy Photographer of the Year 2025 shortlist

**原文链接**: [https://www.rmg.co.uk/whats-on/astronomy-photographer-year/galleries/2025-shortlist](https://www.rmg.co.uk/whats-on/astronomy-photographer-year/galleries/2025-shortlist)

生成摘要时出错

---

## 94. The rise of America's intangible economy

**原文标题**: The rise of America's intangible economy

**原文链接**: [https://www.ft.com/content/38c3ccd8-3aa0-4dbb-a832-00177c40996c](https://www.ft.com/content/38c3ccd8-3aa0-4dbb-a832-00177c40996c)

生成摘要时出错

---

## 95. QNX: The Incredible 1.44M Demo

**原文标题**: QNX: The Incredible 1.44M Demo

**原文链接**: [https://archive.org/details/QNX_incredible_1.44m_demo_v4.0](https://archive.org/details/QNX_incredible_1.44m_demo_v4.0)

生成摘要时出错

---

## 96. Which colors are primary?

**原文标题**: Which colors are primary?

**原文链接**: [https://jamesgurney.substack.com/p/which-colors-are-primary](https://jamesgurney.substack.com/p/which-colors-are-primary)

生成摘要时出错

---

## 97. LLM advises to delete the Linux dynamic linker during a troubleshooting session

**原文标题**: LLM advises to delete the Linux dynamic linker during a troubleshooting session

**原文链接**: [https://old.reddit.com/r/linux4noobs/comments/1mlveoo/help/](https://old.reddit.com/r/linux4noobs/comments/1mlveoo/help/)

生成摘要时出错

---

## 98. Efrit: A native elisp coding agent running in Emacs

**原文标题**: Efrit: A native elisp coding agent running in Emacs

**原文链接**: [https://github.com/steveyegge/efrit](https://github.com/steveyegge/efrit)

生成摘要时出错

---

## 99. Breaking the Sorting Barrier for Directed Single-Source Shortest Paths

**原文标题**: Breaking the Sorting Barrier for Directed Single-Source Shortest Paths

**原文链接**: [https://arxiv.org/abs/2504.17033](https://arxiv.org/abs/2504.17033)

生成摘要时出错

---

## 100. Procrastination and the Bikeshed Effect (2009)

**原文标题**: Procrastination and the Bikeshed Effect (2009)

**原文链接**: [https://blog.codinghorror.com/procrastination-and-the-bikeshed-effect/](https://blog.codinghorror.com/procrastination-and-the-bikeshed-effect/)

生成摘要时出错

---

