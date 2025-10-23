# Hacker News 热门文章摘要 (2025-10-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我用D语言花了一年时间做了一个ASN.1编译器。

**原文标题**: I spent a year making an ASN.1 compiler in D

**原文链接**: [https://bradley.chatha.dev/blog/dlang-propaganda/asn1-compiler-in-d/](https://bradley.chatha.dev/blog/dlang-propaganda/asn1-compiler-in-d/)

本文详细介绍了作者为期一年使用D语言构建ASN.1编译器“dasn1”的历程，该编译器用于其玩具异步I/O框架Juptune，专门用于处理TLS中的x.509证书。作者深入探讨了ASN.1的复杂性，这是一种类似于“打了类固醇的protobuf”的数据规范语言，概述了其表示法标准（x.680、x.681、x.682、x.683）以及各种编码（BER、CER、DER、PER、XER、JER）。

文章探讨了实现ASN.1所面临的挑战，原因在于其历史上的弃用、复杂的扩展（如信息类对象(x.681)和表约束(x.682)）以及需要多次实现约束。尽管困难重重，作者还是强调了ASN.1的一些很酷的特性，例如其约束系统和使用OBJECT IDENTIFIER的模块版本控制。

作者称赞了D语言的代码生成能力，强调了静态导入、完全限定名称、模块本地查找、`typeof()`、尾随逗号和元编程等特性。他们还提到了特定的D语言实现细节，如mixin模板和`alias this`特性，同时也感叹了永远处于实验阶段的分配器包的状态。主要的痛点包括值序列语法的复杂性、在规范中难以找到关键信息以及ASN.1复杂性的要么全有要么全无的本质。尽管尚未完成，该编译器已成功解析了一些x.509证书。

---

## 2. PyTorch 君主

**原文标题**: PyTorch Monarch

**原文链接**: [https://pytorch.org/blog/introducing-pytorch-monarch/](https://pytorch.org/blog/introducing-pytorch-monarch/)

PyTorch Monarch 是一个全新的分布式编程框架，旨在简化在大型集群上运行的复杂、异构且易出错的机器学习工作流程的开发。它通过提供单控制器编程模型来解决传统多控制器模型的局限性，在该模型中，单个脚本编排所有分布式资源，使其感觉像是本地资源。

Monarch 的主要特点包括：

*   **像数组一样编程集群：** 使用进程和 Actor 网格（资源的多维数组）来高效地在大型系统上调度操作。
*   **渐进式故障处理：** 允许开发者最初编写代码时假设没有故障，然后仅在需要时添加细粒度的故障处理。
*   **分离控制和数据：** 将消息传递（控制平面）与 RDMA 传输（数据平面）分离，以优化通信。
*   **分布式张量：** 与 PyTorch 无缝集成，提供看似本地但跨 GPU 集群运行的分布式张量。

该框架包括诸如进程和 Actor 网格、张量引擎和 RDMA 缓冲区 API 等关键 API。后端使用 Rust 实现，以实现性能、规模和稳健性，并利用名为 hyperactor 和 hyperactor_mesh 的底层 actor 框架。通过多播树和多部分消息传递实现可扩展的消息传递。

文章重点介绍了两个案例研究：强化学习和大规模预训练中的容错。Monarch 通过将每个组件表示为网格，从而能够创建复杂的 RL 管道，并与 VERL 等现有框架集成。对于容错，它使研究人员能够利用各种方法使模型的数值更能容忍各个组以更加异步的方式运行。Monarch 旨在通过提供具有原生 PyTorch 集成的通用 API 来解锁下一代人工智能应用程序。

---

## 3. Antislop：一种消除语言模型中重复模式的框架

**原文标题**: Antislop: A framework for eliminating repetitive patterns in language models

**原文链接**: [https://arxiv.org/abs/2510.15061](https://arxiv.org/abs/2510.15061)

这篇题为“Antislop：用于识别和消除语言模型中重复模式的综合框架”的arXiv文章，旨在解决LLM生成文本中重复短语（“slop”）的问题。作者Samuel Paech、Allen Roush、Judah Goldfeder和Ravid Shwartz-Ziv介绍了Antislop，该框架旨在检测和消除这些模式，从而提高输出质量并降低AI生成文本的可识别性。

Antislop包含三个主要创新：Antislop采样器、自动化管线和最终Token偏好优化（FTPO）。Antislop采样器在推理过程中使用回溯来抑制不需要的字符串，而不会损坏词汇表。自动化管线针对人类文本分析特定于模型的slop，以创建训练数据。FTPO是一种微调方法，可针对推理跟踪中出现禁止模式的单个token进行logits的精确调整。

该论文表明，与人类文本相比，LLM输出中slop模式的出现频率明显更高。Antislop采样器有效地抑制了大量模式。FTPO实现了slop的显著减少（90%），同时在跨领域评估（如GSM8K、MMLU和创意写作任务）中保持或提高了性能。相比之下，直接偏好优化（DPO）的性能有所下降。作者已在MIT许可下发布了代码和结果。

---

## 4. 算法如何推高价格的博弈论

**原文标题**: The game theory of how algorithms can drive up prices

**原文链接**: [https://www.quantamagazine.org/the-game-theory-of-how-algorithms-can-drive-up-prices-20251022/](https://www.quantamagazine.org/the-game-theory-of-how-algorithms-can-drive-up-prices-20251022/)

本文探讨了定价算法（即使是简单的算法）如何在没有明确共谋的情况下导致更高的价格，从而挑战了传统的反垄断方法。文章重点介绍了一项2019年的研究，该研究表明算法通过报复性定价学会了默契共谋。

文章随后讨论了一篇最新的论文，该论文认为，即使是为个人利润优化的“良性”算法也可能导致对买家不利的结果。该研究利用博弈论来分析定价算法如何互动，特别关注“无互换后悔”算法，理论上，该算法应导致竞争性定价。

然而，研究人员发现，当一个无互换后悔算法面对一个“无反应”算法时，后者以很高的概率随机选择高价，结果是消费者面临出人意料的高价。这是因为无互换后悔算法被诱导提高自身价格，并达到一种均衡状态，在这种状态下，即使消费者支付更多，双方都没有改变策略的动机。

文章最后讨论了这带来的监管挑战。虽然禁止无互换后悔算法没有意义，但“无反应”策略突显了即使是看似无害的方法也可能导致不良的定价结果。Jason Hartline建议只允许无互换后悔算法，但文章最终承认，还需要更多的研究来充分理解算法定价在现实世界中的影响。

---

## 5. VST3音频插件格式现已采用MIT许可。

**原文标题**: VST3 audio plugin format is now MIT

**原文链接**: [https://forums.steinberg.net/t/vst-3-8-0-sdk-released/1011988](https://forums.steinberg.net/t/vst-3-8-0-sdk-released/1011988)

Steinberg Media Technologies 发布 VST SDK 3.8，标志着 VST 3 在 MIT 许可下向开源模式的重大转变。

本次发布的主要更新包括：

*   **许可：** VST 3 现在采用 MIT 许可，从而实现更广泛的访问和使用。
*   **MIDI 2.0 支持：** 引入了新的接口 IMidiLearn2 和 IMidiMapping2，取代了之前的 IMidiLearn 和 IMidiMapping，以改进 MIDI 处理。 为 MIDI 1.0 系统消息添加了缺少的 ControllerNumbers 枚举。
*   **Wayland 支持 (Linux)：** 预览版支持 Linux 上的 Wayland，包括新的接口 IWaylandHost 和 IWaylandFrame，以及新的平台 UI 类型 kPlatformTypeWaylandSurfaceID。
*   **VSTGUI 4.15.0 更新：** 包括用于后台任务调度的 Task Concurrency API、对自定义视图布局的支持 (IViewLayouter)、类似于 CSS Grid 的网格视图布局器 (GridLayouter)、UIDescription 的脚本、新的文本编辑器视图以及滚动视图的边缘视图支持。 此外还增加了初步的 Wayland 支持。
*   **文档更新：** 文档已更新，以反映新的许可模式和 Steinberg VST 使用指南。
*   **CMake 改进：** 修复了 macOS、Linux 和 Visual Studio Compiler 上的 CMake 脚本。
*   **示例：** 更新了示例以支持新的 ControllerNumbers 枚举和 MIDI 2.0 接口。
*   **Helper 类修复：** 修复了多个问题，包括解决验证器问题、验证测试套件中未定义的行为以及潜在的崩溃问题。

SDK 和在线文档可通过提供的链接获取。

---

## 6. 在 TypeScript 中进行类型转换的非常规方法

**原文标题**: Unconventional Ways to Cast in TypeScript

**原文链接**: [https://wolfgirl.dev/blog/2025-10-22-4-unconventional-ways-to-cast-in-typescript/](https://wolfgirl.dev/blog/2025-10-22-4-unconventional-ways-to-cast-in-typescript/)

本文探讨了在 TypeScript 中执行类型转换的非常规且可能不安全的方法，突出了该语言类型系统中的局限性和潜在陷阱。虽然 TypeScript 提供了一个强大的系统来为 JavaScript 添加类型，但它并非万无一失，可以通过巧妙的技巧来绕过。

作者首先展示了标准的 `as unknown as B` 转换方法。然后，他们演示了四种非常规的转换方法：

1.  **`is` 操作符：** 滥用类型谓词来欺骗编译器，使其相信一个值是另一种类型，即使它不是。
2.  **跨边界突变：** 通过跨函数边界突变对象来利用变异问题，从而有效地更改属性的类型。
3.  **通过结构化类型传递：** 使用结构化类型和诸如 `Object.values` 和展开运算符之类的技术来引入不正确的类型假设。
4.  **`| void` 非常糟糕：** 利用 `void` 和类型联合之间的相互作用，将一种类型的值偷偷地传递到另一种类型中，利用 TypeScript 将 `void` 视为假值的方式。

作者强调，虽然 TypeScript 通常很有帮助，但这些“非常规方法”可能会导致细微的错误并破坏类型安全。他们提倡使用积极的 linting，特别推荐 `typescript-eslint` 规则集，以捕获和防止这些潜在的问题模式。提到的具体规则是 `@typescript-eslint/prefer-readonly-parameter-types`、`@typescript-eslint/no-invalid-void-type` 和 `@typescript-eslint/no-unnecessary-type-parameters`。文章最后敦促开发人员通过实施更严格的 linting 配置来积极保护他们的 TypeScript 项目。

---

## 7. 谷歌将 Immich 网站标记为危险网站

**原文标题**: Google flags Immich sites as dangerous

**原文链接**: [https://immich.app/blog/google-flags-immich-as-dangerous](https://immich.app/blog/google-flags-immich-as-dangerous)

2025年10月，谷歌安全浏览将 Immich 的 *.immich.cloud 网站标记为危险网站，向用户显示警告。这实际上导致这些网站无法访问，影响了 Immich 团队的内部和生产环境，包括预览环境和瓦片服务器。

该问题源于谷歌检测到 Immich 预览环境 URL（例如 `preview.internal.immich.cloud` 上的 URL）存在“有害内容”，错误地声称它们试图欺骗用户。核心问题在于，一个被标记的子域名使整个域名失效。

Immich 团队使用谷歌搜索控制台请求审查，解释说被标记的网站是他们自己开源产品的合法部署。审查最初被接受，但每次创建新的预览环境时，该问题都会再次发生，这表明谷歌的爬虫从 GitHub 上抓取了 URL 并对其进行了标记。

为了缓解这个问题，Immich 计划将预览环境迁移到单独的域名 immich.build。 这篇文章强调了谷歌安全浏览对 Jellyfin、YunoHost 和 NextCloud 等开源和自托管软件项目产生的更广泛影响。 Immich 团队对谷歌随意标记域名的能力以及除了反复请求审查之外解决这些误报的有限追索权表示沮丧。

---

## 8. CRDTs：无需协调的收敛

**原文标题**: CRDTs: Convergence without coordination

**原文链接**: [https://read.thecoder.cafe/p/crdt](https://read.thecoder.cafe/p/crdt)

本文《CRDTs：无需协调的收敛》介绍了无冲突复制数据类型 (CRDTs)，它是一种在分布式系统中保持一致性而无需协调的解决方案。

文章首先将并发操作定义为在因果关系上不相关的操作，并将并发与冲突区分开来。然后解释说，传统的分布式系统通过协调来解决冲突，通常涉及通信和等待，从而影响可用性。

另一方面，CRDTs 的设计允许在不同的节点上进行独立和并发的更新，通过确定性的冲突解决算法保证最终收敛到同一状态，从而确保强最终一致性 (SEC)。文章使用 G-Counters 和 PN-Counters 等示例来说明 CRDTs 的工作原理，其中节点通过取元素级最大值来合并其状态向量。

文章重点介绍了协作式离线优先系统（如 Notion 的离线编辑）和高可用性系统（如 Redis 的主-主架构）等用例。文章区分了基于状态的 CRDTs（交换完整状态）和基于操作的 CRDTs（交换更新操作），并提到了基于 Delta 的 CRDTs。

最后，文章将 CRDTs 与 Google Docs 等系统中使用的操作转换 (OT) 进行了对比，强调了 CRDTs 不需要中央服务器来实现收敛的优势。关键在于，CRDTs 通过消除协调需求，实现了高可用性和可扩展性的分布式系统，使其成为具有离线功能和地理分布式数据的场景的理想选择。

---

## 9. 一无所有的编程

**原文标题**: Programming with Less Than Nothing

**原文链接**: [https://joshmoody.org/blog/programming-with-less-than-nothing/](https://joshmoody.org/blog/programming-with-less-than-nothing/)

本文是一篇讽刺文章，旨在讽刺过度设计一个简单的编程问题——FizzBuzz，以展示极端理论知识，即使这种知识是不切实际且低效的。主角在一次面试中，试图使用组合逻辑和lambda演算来解决FizzBuzz问题，而不是使用直接的JavaScript。

面试官Dana起初很感兴趣，但随着解决方案变得越来越深奥，并引用了“Programming with Nothing”和“What is PLUS times PLUS”，她很快就变得怀疑起来，暗示这是候选人为了炫耀而常有的、毫无成效的尝试。

主角认为lambda演算过于臃肿，并开始手动实现Church numerals、point-free arithmetic和Y combinators，以纯函数式的方式实现递归。他遇到了JavaScript的急切求值问题，并求助于“Skoobert”，这是一种虚构的JavaScript惰性方言。

尽管Dana越来越困惑，但主角坚持不懈，从基本逻辑构建到列表、字符串，最后是FizzBuzz输出。代码变得越来越复杂和难以理解，最终达到所有变量都内联的程度，导致一个完全不可维护、定义被替换的混乱局面。 幽默之处在于主角为了避免传统的编程实践所采取的极端措施，将理论纯粹性置于实用性和效率之上，最终疏远了面试官。

---

## 10. 亚马逊 DynamoDB 美国东部一区服务中断概要

**原文标题**: Summary of the Amazon DynamoDB Service Disruption in US-East-1 Region

**原文链接**: [https://aws.amazon.com/message/101925/](https://aws.amazon.com/message/101925/)

2025年10月19日和20日，美国东部1区（弗吉尼亚北部）区域发生了服务中断，影响了Amazon DynamoDB、EC2和网络负载均衡器（NLB）。此次中断涉及三个不同的影响时期。

主要原因是DynamoDB的DNS管理系统中存在潜在的竞态条件，于10月19日太平洋夏令时晚上11:48触发，导致区域端点出现不正确的空DNS记录。这阻止了与DynamoDB的新连接，影响了客户流量和内部AWS服务，直至10月20日太平洋夏令时凌晨2:40解决。

与此同时，由于DynamoDB问题影响了DropletWorkflow Manager (DWFM)（管理底层物理服务器），EC2实例启动开始失败。在DynamoDB恢复后，DWFM因尝试重新建立droplet租约而变得拥堵，导致“容量不足”错误。负责网络配置的网络管理器随后面临积压，延迟了新实例的网络连接。EC2全面恢复发生在10月20日太平洋夏令时下午1:50。

10月20日太平洋夏令时上午5:30至下午2:09之间，由于健康检查失败，NLB经历了连接错误增加。新启动的EC2实例缺乏适当的网络配置，导致间歇性故障，并影响了NLB的健康检查子系统。这造成了一个节点被移除并返回服务的循环，进一步降低了系统性能。

---

## 11. 谷歌地球AI扩展全球访问

**原文标题**: Google Earth AI expanding access around the globe

**原文链接**: [https://blog.google/technology/research/new-updates-and-more-access-to-google-earth-ai/](https://blog.google/technology/research/new-updates-and-more-access-to-google-earth-ai/)

谷歌地球AI拓展应用，新增功能，助力企业、城市及非营利组织应对环境监测和灾害响应等关键问题。基于数十年世界建模和Gemini的推理能力，Earth AI现推出地理空间推理，这是一个由Gemini驱动的框架，可自动连接不同的Earth AI模型以解答复杂问题。这有助于识别灾害场景中的脆弱社区和高危基础设施，GiveDirectly利用洪水和人口密度数据便是例证。

Gemini的功能也正在整合到谷歌地球中，使用户能够即时查找物体并从卫星图像中发现模式，包括识别干涸的河流或有害藻华。此功能将很快在美国向谷歌地球专业版和专业高级版用户开放，谷歌AI Pro和Ultra订阅者将获得更高的使用限制。

Earth AI的图像、人口和环境模型也将面向谷歌云上的可信测试者开放。企业可以将这些模型与自身数据相结合，以应对特定挑战。

Earth AI的应用案例包括：世界卫生组织使用Earth AI预测刚果民主共和国的霍乱爆发；Planet和空中客车等卫星图像提供商使用Earth AI分析图像，分别用于绘制森林砍伐地图和检测植被侵占；以及Bellwether使用Earth AI为保险经纪人提供飓风预测洞察。

---

## 12. 克劳德记忆

**原文标题**: Claude Memory

**原文链接**: [https://www.anthropic.com/news/memory](https://www.anthropic.com/news/memory)

本文宣布为Anthropic的AI助手Claude发布“记忆”功能，该功能最初面向团队和企业计划用户推出，并将于2025年10月23日开始扩展到Pro和Max计划。 “记忆”功能使Claude能够记住用户偏好、项目和团队流程，从而无需在每次对话中重新解释上下文，并提高工作效率。

主要功能包括项目范围记忆（每个项目单独的记忆）、用户完全控制查看和编辑Claude的记忆，以及用于不保存到记忆或对话历史记录的对话的“隐身聊天”。 企业管理员可以为其组织禁用记忆功能。

“记忆”功能专为专业环境而设计，可帮助团队保持跨项目、客户和计划的连续性。 用户可以编辑记忆摘要，以便将Claude的注意力集中在特定细节上。 隐身聊天为敏感讨论提供了一个全新的开始。

Anthropic在推出之前进行了广泛的安全测试，以改进Claude的响应并防止有害模式或绕过安全措施。 公司正在采取分阶段部署方法，以确保负责任的使用。 用户可以在设置中启用“记忆”功能，并通过询问Claude有关过去工作的问题来了解它的实际效果。 Anthropic还发布了关于其对美国人工智能领导地位、网络版Claude Code以及Claude for Life Sciences的承诺的新闻。

---

## 13. VectorWare – `rust-GPU` 和 `rust-CUDA` 的创造者出品

**原文标题**: VectorWare – from creators of `rust-GPU` and `rust-CUDA`

**原文链接**: [https://www.vectorware.com/blog/announcing-vectorware/](https://www.vectorware.com/blog/announcing-vectorware/)

VectorWare认为从CPU到GPU的转变正在加速，该公司由`rust-GPU`和`rust-CUDA`的创建者创立。虽然GPU变得越来越重要，但软件开发却滞后，仍然主要以CPU为中心。VectorWare旨在引领创建新的“GPU原生”软件行业，其中GPU处于控制地位，构建工具和底层堆栈以支持这一转变。

他们设想的未来是，所有软件都将利用GPU，从而改进现有的GPU应用程序（AI、ML等）并迁移CPU应用程序。他们将自己的角色比作微软在PC时代的角色，为新兴的以GPU为中心的硬件提供平台、应用程序和开发者工具。

该公司获得了Dan Portillo、John Lilly、Patrick Kavanagh和Nick Candito等经验丰富的投资者的支持，目前正在积极招聘。他们正在寻找具有GPU原生应用程序开发、编译器工程/语言设计（特别是Rust）、用户空间图形工程和Linux内核工程方面专业知识的工程师。他们的目标包括构建GPU原生应用程序、塑造底层软件堆栈、改进GPU原生应用程序的图形堆栈以及增强数据中心内GPU应用程序的操作系统支持。他们强调Rust专业知识的重要性，以及学习GPU的意愿，反之亦然。

---

## 14. Show HN: Deta Surf – 一个开源且本地优先的AI笔记本

**原文标题**: Show HN: Deta Surf – An open source and local-first AI notebook

**原文链接**: [https://github.com/deta/surf](https://github.com/deta/surf)

Deta Surf 是一个开源的、本地优先的 AI 笔记本，旨在通过将各种媒体类型集成到单个环境中来简化研究和思考。它的目标是消除在笔记、网站和 PDF 之间切换多个应用程序的低效率。Surf 使用 Svelte、TypeScript 和 Rust 构建，可在 MacOS、Windows 和 Linux 上使用。

主要功能包括一个多媒体库，该库以开放格式将文件、网站和链接本地存储，并组织成笔记本，以供离线访问和支持 AI 功能。智能笔记使用户能够 @-提及和自动生成来自任何资源的内容，执行网络搜索，生成交互式应用程序 (Surflets)，并包含图像、表格和数据。界面包括选项卡、分屏视图和一个侧边栏，方便导航。

Surf 利用大型语言模型（用户可以自带密钥或使用本地模型）来支持笔记和 Surflets。可以通过 GitHub Releases 或具有托管功能的 Deta 网站版本进行安装（受不同条款约束）。该项目在 Apache 2.0 许可下授权，但特定软件包除外，强调其对开源原则的承诺，而其背后的商业实体 Deta GmbH 提供了一个与其服务器集成的修改版本。

---

## 15. MinIO拒绝发布修复CVE-2025-62506漏洞的Docker构建版本

**原文标题**: MinIO declines to release Docker builds resolving CVE-2025-62506

**原文链接**: [https://github.com/minio/minio/issues/21647](https://github.com/minio/minio/issues/21647)

文章描述了MinIO GitHub仓库上的一个未决问题，该问题涉及解决特定安全漏洞CVE-2025-62506（于2025年10月15日发布）的Docker镜像的可用性。问题报告者neil-lcv-cs指出，他们在quay.io或Docker Hub上都找不到反映该安全发布的更新Docker镜像。他们询问这是否是预期行为，如果不是，则请求发布新镜像。该问题被标记为“社区”和“按预期工作”，表明MinIO有意不发布专门用于解决该漏洞的Docker镜像。在此提供的上下文中，并未明确说明做出此决定的原因。

---

## 16. Nango (YC W23) 招聘后端工程师（远程）

**原文标题**: Nango (YC W23) is hiring staff back-end engineers (remote)

**原文链接**: [https://www.nango.dev/careers](https://www.nango.dev/careers)

Nango（YC W23公司）正在招聘远程后端工程师。Nango正在构建B2B软件的集成层，旨在简化、提高可靠性并实现原生集成，从而解决构建集成过程中常见的痛点。他们强调，随着公司采用更多软件和人工智能，无缝集成至关重要。

该公司强调了加入其团队的几项优势：

*   **完全远程：** 提供全球分布式团队结构，注重结果。
*   **开源：** 重视透明度、社区和开发者友好性。
*   **开发者工具：** 专注于解决开发者能够理解的集成问题。
*   **技术挑战：** 应对诸如DevExp、可扩展性和API碎片化等复杂问题。
*   **专家主导：** 由来自Uber、Netlify和Algolia等公司的经验丰富的个人组成。
*   **发展势头：** 在收入和使用量方面均显示出显著增长。

---

## 17. 《程序员习题》 (1978) "Easy" 语言编译器

**原文标题**: Compiler for "Easy" language from "Etudes for Programmers" book (1978)

**原文链接**: [https://github.com/begoon/easy](https://github.com/begoon/easy)

本文档描述了一个“Easy”编程语言的编译器，该编译器基于《程序员练习曲》(1978)一书。这个用TypeScript编写的编译器也具有教育意义，旨在学习编译器实现。它将Easy代码转换为C代码，然后使用Clang或GCC将其编译成原生可执行文件，并通过`runtime.c`提供最小的运行时环境。

该编译器支持完整的Easy语言语法，但对`EXTERNAL`子程序、`NAME`别名和多个`PROGRAM`段有限制。Easy使用复制语义，确保数据结构的深拷贝，但动态大小的数组除外，它们会进行浅拷贝。

该编译器采用手写的递归下降解析器。存在一个实验性的PEG解析器，但目前未用于代码生成。一个测试套件`test.ts`针对各种示例（如Brainfuck、康威生命游戏和埃拉托斯特尼筛法）评估编译器。这些测试将生成的C代码（`test.c`）和程序输出（`test.output`）与预期值进行比较。测试可以在本地或使用`just`在Docker容器中运行。

本文档提供了编译和运行Easy程序的说明，以及编译器内部结构的解释和使用C结构体来表示复杂数据类型的方法。该项目还包括对“cot”编辑器的语法高亮支持和一个VSCode扩展，以及一个概念验证LSP。它被作为一个编译器开发的学习练习来展示。

---

## 18. 我经常使用的自写脚本

**原文标题**: Scripts I wrote that I use all the time

**原文链接**: [https://evanhahn.com/scripts-i-wrote-that-i-use-all-the-time/](https://evanhahn.com/scripts-i-wrote-that-i-use-all-the-time/)

埃文·哈恩分享了一系列他在日常工作中开发并经常使用的 Shell 脚本。这些脚本按功能分类，包括剪贴板管理、文件管理、互联网工具、文本处理、REPL 启动器、日期和时间工具、音频和视频处理、进程管理、快速参考和系统管理。

示例包括用于剪贴板交互的 `copy` 和 `pasta`，用于目录创建和临时目录管理的 `mkcd` 和 `tempe`，以及用于安全文件删除的 `trash`。像 `serveit`、`getsong`、`getpod` 和 `getsubs` 这样的互联网相关脚本简化了诸如启动本地服务器和下载媒体之类的任务。

诸如 `straightquote`、`markdownquote` 和 `jsonformat` 这样的文本处理脚本简化了文本操作，而 REPL 启动器则提供了对各种编程语言环境的快速访问。像 `hoy` 和 `timer` 这样的日期和时间脚本有助于文件命名和时间管理。

像 `tunes` 和 `shrinkvid` 这样的音频和视频脚本提供了媒体播放和压缩功能。像 `each`、`murder` 和 `bb` (后台进程) 这样的进程管理工具帮助管理运行中的进程。像 `theme`、`sleepybear` 和 `ds-destroy` 这样的系统管理脚本自动化了诸如主题切换和删除 `.DS_Store` 文件之类的任务。

文章最后邀请读者分享他们自己有用的脚本。

---

## 19. 与克劳德的危险生活

**原文标题**: Living Dangerously with Claude

**原文链接**: [https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)

在 Claude Code Anonymous 的一次演示中，作者探讨了以“YOLO 模式”（使用 `--dangerously-skip-permissions` 标志）运行像 Claude Code 这样的编码代理的利弊。 YOLO 模式通过允许代理自主处理复杂任务来显著提高生产力，例如在 NVIDIA Spark 上运行 DeepSeek-OCR，在 WebAssembly 沙箱中使用 Pyodide 运行服务器端 Python 代码，以及为 SLOCCount 创建基于浏览器的应用程序。

然而，这种自由带来了巨大的风险，主要是由于提示注入漏洞。 这些攻击会通过将访问敏感信息与暴露于不受信任的内容以及外部通信能力相结合，诱骗代理泄露私有数据，例如 API 密钥或源代码。

作者强调，依靠 AI 来检测这些攻击是不可靠的，并提倡将沙箱化编码代理作为唯一可靠的安全防御手段。 沙箱限制了文件系统访问，并且至关重要的是，控制网络连接以防止数据外泄。 OpenAI Codex Cloud、面向 Web 的 Claude Code 和 Gemini Jules 等解决方案被强调为有用的工具。 该文章还提到了 Anthropic 利用 Apple 的 `sandbox-exec` 命令（尽管已被弃用）创建沙箱的开源库。 关键要点：危险地使用编码代理，但始终在安全的沙箱环境中进行。

---

## 20. 无线电：它们是如何工作的？(2024)

**原文标题**: Radios, how do they work? (2024)

**原文链接**: [https://lcamtuf.substack.com/p/radios-how-do-they-work](https://lcamtuf.substack.com/p/radios-how-do-they-work)

无法访问文章链接。

---

## 21. 哪些忙碌海狸模拟了考拉兹数（如果有的话）？

**原文标题**: Which Collatz numbers do Busy Beavers simulate (if any)?

**原文链接**: [https://gbragafibra.github.io/2025/10/16/collatz_ant11.html](https://gbragafibra.github.io/2025/10/16/collatz_ant11.html)

本文通过引入“考拉兹纸带”，一种基于考拉兹序列演化纸带的改进型图灵机，探讨了忙碌海狸图灵机与考拉兹猜想之间的联系。

考拉兹纸带的工作原理是，从数字“n”开始，重复应用考拉兹函数。每次应用时，机器会根据“n”模3的结果翻转当前纸带单元格的状态。对于奇数“n”，机器向左移动；对于偶数“n”，机器向右移动，直到“n”达到1。

作者将使用考拉兹纸带由特定数字 ($n=371581$) 生成的纸带发展与已知忙碌海狸冠军 BB(4) 的纸带发展进行了比较。这是基于一些忙碌海狸候选者表现出类似考拉兹行为的观察结果。

提出的核心问题是，忙碌海狸*是否应该*使用定义的考拉兹纸带方法来模拟任何考拉兹数。文章没有提供明确的答案，但表明这是一个值得探索的途径，可能揭示图灵机行为与数论之间更深层次的联系。

最后，文章包含了由非常大的数字（10的幂）及其变体生成的有趣考拉兹纸带的示例，提供了更多背景信息并说明了纸带演化的复杂性。

---

## 22. Show HN: Nostr Web – 去中心化网站托管在Nostr上

**原文标题**: Show HN: Nostr Web – decentralized website hosting on Nostr

**原文链接**: [https://nweb.shugur.com](https://nweb.shugur.com)

Show HN: Nostr Web 介绍了一种在去中心化 Nostr 网络上托管网站的方法。关键在于，正在浏览的网站使用 Nostr 进行去中心化托管。访问它需要用户安装特定的浏览器扩展。该帖子提供了在 Chrome 和 Firefox 上安装扩展的直接链接，并引导用户访问 GitHub 仓库进行手动安装或用于其他浏览器。本质上，它是在推广一种新的网站托管方法，并提供访问使用该方法托管的网站所需的工具（浏览器扩展）。

---

## 23. 通过国际汽联漏洞访问马克斯·维斯塔潘的护照和个人身份信息

**原文标题**: Accessing Max Verstappen's passport and PII through FIA bugs

**原文链接**: [https://ian.sh/fia](https://ian.sh/fia)

三名网络安全研究人员在国际汽联车手分级网站上发现了一个重大漏洞，使他们能够获得管理员权限，并可能访问包括马克斯·维斯塔潘在内的F1车手敏感个人信息。

该漏洞源于用于更新用户配置文件的HTTP PUT请求中的大规模赋值问题。研究人员发现，JSON响应中包含一个“roles”参数。通过在随后的PUT请求中操纵此参数，他们成功地将自己分配为“ADMIN”角色。

这种管理员权限使他们能够访问专供国际汽联管理员使用的仪表板，从而能够管理车手、员工和服务器端变量。至关重要的是，他们能够访问用户配置文件，包括密码哈希值、电子邮件地址、电话号码、护照、简历和其他PII。他们还可以访问国际汽联关于车手分级的内部通信。

研究人员在确认访问马克斯·维斯塔潘的护照和PII后停止了测试，并确保所有访问的数据都被删除。他们向国际汽联报告了该漏洞，国际汽联最初关闭了该网站，实施了全面的修复，后来得知了公开披露。这篇博文记录了他们的发现。

---

## 24. SpaceX 禁用 2500 个据称被亚洲诈骗中心使用的星链终端

**原文标题**: SpaceX disables 2,500 Starlink terminals allegedly used by Asian scam centers

**原文链接**: [https://arstechnica.com/tech-policy/2025/10/starlink-blocks-2500-dishes-allegedly-used-by-myanmars-notorious-scam-centers/](https://arstechnica.com/tech-policy/2025/10/starlink-blocks-2500-dishes-allegedly-used-by-myanmars-notorious-scam-centers/)

SpaceX已禁用缅甸境内2500多个星链终端，怀疑被诈骗中心使用。此前，缅甸军方关闭了泰国边境附近一处大型网络诈骗窝点，查获星链终端并拘留了2000多人。星链未获准在缅甸运营，但这些诈骗中心利用该服务进行网络犯罪，包括针对全球受害者的网络诈骗。这些中心通常由中国犯罪集团运营，以虚假借口引诱工人，并强迫他们从事欺诈活动。联合国毒品和犯罪问题办公室此前曾报告缅甸和泰国此类行动中使用星链的情况。美国参议员玛吉·哈桑也敦促埃隆·马斯克采取行动，防止犯罪分子利用星链进行诈骗活动，促使SpaceX重申其致力于检测和防止滥用其服务的承诺。SpaceX副总裁劳伦·德雷尔表示，他们正在与执法部门协调，积极识别和禁用用于非法目的的终端。

---

## 25. Karpathy 谈 DeepSeek-OCR 论文：像素比文本更适合作为 LLM 的输入吗？

**原文标题**: Karpathy on DeepSeek-OCR paper: Are pixels better inputs to LLMs than text?

**原文链接**: [https://twitter.com/karpathy/status/1980397031542989305](https://twitter.com/karpathy/status/1980397031542989305)

提供的内容并非文章，而是X（前身为Twitter）的一个错误信息片段，表明JavaScript已被禁用。因此，没有文章内容可供总结。标题暗示了对Andrej Karpathy关于DeepSeek-OCR论文的观点的讨论，质疑原始像素数据是否可能比预处理文本更适合作为大型语言模型（LLM）的输入。然而，实际内容仅仅是一个网站错误信息，阻止了对所谓讨论的访问。

简而言之，提供的信息不包含任何实际文章或讨论，仅包含来自X.com的指示JavaScript已禁用的错误信息，以及一个标题，暗示了关于在OCR背景下使用像素数据与文本作为LLM输入的争论。我们无法根据此信息了解Karpathy的实际观点或DeepSeek-OCR论文中的具体论点。

---

## 26. 在 Gemini CLI 中运行交互式命令

**原文标题**: Run interactive commands in Gemini CLI

**原文链接**: [https://developers.googleblog.com/en/say-hello-to-a-new-level-of-interactivity-in-gemini-cli/](https://developers.googleblog.com/en/say-hello-to-a-new-level-of-interactivity-in-gemini-cli/)

本文宣布对 Gemini CLI 的一项重大增强：支持交互式命令。此次更新允许用户直接在 Gemini CLI 环境中运行复杂的基于终端的应用程序，如 `vim`、`top` 和交互式 `git rebase`，无需切换到单独的终端。

该改进保持了 Gemini CLI 的上下文，因为之前交互式命令是在此上下文之外运行的。此次更新利用伪终端 (PTY) 支持，使需要丰富终端功能和控制代码的命令能够在 Gemini CLI 中正常运行。

该系统的工作原理是在后台 PTY 中生成一个新进程，然后将终端状态（文本、颜色、光标位置）的类似视频的馈送流式传输到用户的屏幕。该系统还支持双向通信，允许用户输入击键和调整终端窗口的大小。此次更新还可以正确呈现彩色终端输出。

交互式 shell 在 Gemini CLI 0.9.0 版本中默认启用。本文重点介绍了用例示例，包括使用 `vim` 编辑代码、使用交互式 `git` 命令管理提交、使用交互式 REPL、运行全屏终端应用程序、导航交互式设置脚本以及响应 `gcloud` 命令中的交互式提示。作者鼓励用户通过 GitHub 存储库提供反馈。

---

## 27. Stalwart 现已支持日历、联系人和文件的JMAP协议

**原文标题**: JMAP for Calendars, Contacts and Files Now in Stalwart

**原文链接**: [https://stalw.art/blog/jmap-collaboration/](https://stalw.art/blog/jmap-collaboration/)

Stalwart 成为首个完整实现 JMAP 的服务器，支持日历、联系人、文件存储和共享，标志着开放高效群件的重大进步。该版本采用了新一代 IETF 协议，旨在取代基于 WebDAV 的 CalDAV 和 CardDAV 等旧技术的局限性，这些旧技术存在冗长、不一致和实施挑战。

JMAP 最初用于邮件，现在将其基于 JSON 的简洁性和网络效率扩展到整个协作堆栈，提供了一个清晰且易于实现的 API。 JSCalendar 和 JSContact 用优雅的基于 JSON 的格式取代了 iCalendar 和 vCard，简化了数据表示并提高了解析效率。

此版本简化了日历、联系人管理和文件共享，使其更易于实施和更可靠。虽然客户端支持仍在开发中，但 Mailtemi、Parula 和 OpenCloud 等项目正在积极进行实施。 Stalwart 的开发得到了 NLNet NGI Zero 资助的支持。

凭借这一功能完整的里程碑，Stalwart 现在专注于完成其数据库模式、提高性能并解决 GitHub 请求，目标是尽快发布稳定的 1.0.0 版本，为现代通信服务器树立新标准。

---

## 28. 美国关闭了报告受美武装外国部队侵犯人权行为的网站

**原文标题**: US axes website for reporting human rights abuses by US-armed foreign forces

**原文链接**: [https://www.bbc.com/news/articles/cqx30vnwd4do](https://www.bbc.com/news/articles/cqx30vnwd4do)

美国国务院已移除人权报告门户网站(HRG)，这是一个在线举报外国军事单位在使用美国武器情况下侵犯人权行为的平台。此举引发人权活动家和一位曾协助起草要求设立该门户网站的法律的国会助手的批评。HRG成立于2022年，旨在遵守《莱希法案》，允许组织和个人直接报告美国武装部队犯下的法外处决、酷刑和强奸等虐待行为。

前官员和人权团体认为，此举削弱了美国政府遏制虐待行为的能力，并违反了《莱希法案》，该法案旨在防止美国纳税人的钱被用于支持侵犯人权的行为。他们担心这将助长外国政府不将此类罪行的肇事者绳之以法的行为。国际特赦组织曾提交关于哥伦比亚安全部队涉嫌过度使用武力的报告，并正在准备关于以色列国防军在西岸行动的报告。

国务院坚称，它继续接收并处理人权报告，并遵守其法律要求，但批评人士指出，在卢比奥国务卿领导下，国务院内部进行了更广泛的重组，减少了人权监测工作。令人担忧的是，由于缺乏专门的报告渠道，美国将在不知情的情况下支持犯下严重罪行的外国安全部队。HRG的删除引发了人们对美国承诺防止其军事援助助长海外侵犯人权行为的质疑。

---

## 29. C64血钱

**原文标题**: C64 Blood Money

**原文链接**: [https://lemmings.info/c64-blood-money/](https://lemmings.info/c64-blood-money/)

本文详细回顾了一位开发者将《血钱》移植到Commodore 64（C64）上的经验。作者概述了游戏的核心组件，包括多方向滚动、精灵多路复用器、脚本、精灵压缩、炮塔、角色精灵、武器、碰撞检测、商店和前端。

作者强调了使用程序员开发系统（PDS），这是一个基于PC的工具，带有一个C64卡带，通过提供汇编器、文本编辑器和调试器，极大地加快了开发过程。与传统的基于C64磁盘的汇编器相比，该系统可以快速编译和调试，从而大大提高了工作流程。

本文深入探讨了代码结构，重点介绍了等式（常量）和变量分配的使用，尤其是在6502处理器快速访问的零页内存中。作者描述了碰撞系统，该系统涉及读取背景图块并使用飞船的活动帧进行遮罩，这是一种缓慢但有效的精确碰撞检测方法。

最后一部分概述了初始启动代码，包括内存初始化、ROM禁用和IRQ设置。文章最后指出，考虑到作者当时相对缺乏经验，源代码中的注释水平出乎意料，并暗示下一期将介绍IRQ和多路复用器系统的复杂性。

---

## 30. C64血钱

**原文标题**: C64 Blood Money

**原文链接**: [https://lemmings.info/c64-blood-money/](https://lemmings.info/c64-blood-money/)

本文回顾了作者开发 Commodore 64 (C64) 版游戏“血钱 (Blood Money)”的历程。他反思了遇到的挑战和解决方案，并对某些方面表达了自豪和自我批评。

文章概述了游戏开发的关键组成部分，包括多方向滚动、精灵复用、脚本编写、精灵压缩、敌方炮塔、角色精灵、武器、碰撞检测、游戏内商店和前端界面。

文章重点介绍了程序员开发系统 (PDS)，这是一个强大的基于 PC 的开发环境，与传统的基于 C64 磁盘的汇编器相比，它大大加快了开发过程。PDS 包括一个内置的文本编辑器、汇编器和调试器。

作者深入研究了代码结构，特别关注使用 equates、零页面变量、精灵变量和通用变量的内存管理。他强调了基于位图的碰撞检测的使用，这涉及到读取背景图块并将飞船的框架掩盖在它们上面。

最后，他简要描述了启动代码，包括接管系统控制、清除内存和设置中断。他注意到源代码中的高水平注释，尽管这只是他的第二个游戏。下一篇文章将更详细地讨论中断例程和多路复用器。

---

## 31. Ovi：用于音视频生成的双主干跨模态融合

**原文标题**: Ovi: Twin backbone cross-modal fusion for audio-video generation

**原文链接**: [https://github.com/character-ai/Ovi](https://github.com/character-ai/Ovi)

Ovi：Character AI推出的新型音视频生成模型

---

## 32. 我们需要开始出于非技术原因进行网页屏蔽。

**原文标题**: We need to start doing web blocking for non-technical reasons

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/web/WeShouldBlockForSocialReasons?showcomments](https://utcc.utoronto.ca/~cks/space/blog/web/WeShouldBlockForSocialReasons?showcomments)

由于大量爬虫（特别是那些为LLM训练收集数据的爬虫）的涌入，“Wandering Thoughts”的Chris Siebenmann正在实施网页屏蔽措施。这些爬虫通常使用旧版Chrome浏览器的用户代理，这使得它们难以与合法用户区分。

因此，使用较旧或“可疑地旧”浏览器的访问者可能会被阻止，即使他们是真正的用户。 Siebenmann承认这可能会无意中影响到真实用户，并为那些认为自己被错误阻止的人提供了一种联系方式（大学电子邮件地址）。他要求受影响的用户提供他们的浏览器和User-Agent字符串，以帮助改进阻止规则。

他特别针对通过archive.*（例如，archive.today、archive.ph、archive.is）访问该网站的用户。他解释说，这些存档服务存在问题，因为它们的抓取行为与恶意行为者无法区分。他建议使用archive.org，因为它是一个行为更好的存档爬虫，可以与他的博客协同工作。实施网页屏蔽是一项实验，旨在减少这些有问题爬虫造成的服务器负载。

---

## 33. 为什么选择SSA？

**原文标题**: Why SSA?

**原文链接**: [https://mcyoung.xyz/2025/10/21/ssa-1/](https://mcyoung.xyz/2025/10/21/ssa-1/)

本文“为何选择SSA？”阐述了在编译器中使用静态单赋值（SSA）作为中间表示（IR）的优势。SSA通过将依赖于状态改变和程序顺序的命令式代码转换成更易于分析的“电路式”表示，从而提高程序分析和优化的效率。

SSA的核心思想是每个变量只被赋值一次（“静态单赋值”）。这简化了数据流分析，并允许编译器更像处理组合电路一样处理代码，即有向无环图（DAG），其中操作之间的依赖关系清晰明了。作者用一个C语言示例说明了这一点，展示了改变变量如何阻碍优化，而转换为单赋值形式则简化了常量折叠和死代码消除。

本文介绍了SSA-CFG（控制流图），一种将程序分解为基本块（非控制流操作序列）并带有终止操作的特定SSA形式。作者提出了两种常见的SSA-CFG形式：一种使用phi节点（LLVM风格），另一种使用块参数（MLIR风格）。

本文提供了一个简化的SSA IR示例，将C语言的斐波那契函数转换为SSA-CFG表示。它演示了基于内存的方法（使用堆栈槽）如何作为初始步骤，然后将其转换为仅寄存器表示以提高效率。解释了支配关系的概念，强调了其对于定义SSA中的核心图算法和实现优化的重要性。

---

## 34. 元素：setHTML()方法

**原文标题**: Element: setHTML() method

**原文链接**: [https://developer.mozilla.org/en-US/docs/Web/API/Element/setHTML](https://developer.mozilla.org/en-US/docs/Web/API/Element/setHTML)

`Element.setHTML()` 方法提供了一种安全的方式将 HTML 字符串注入到 DOM 中。它会对输入的 HTML 进行清理，通过将 HTML 解析为 `DocumentFragment`，然后将其作为元素的子树插入，从而防止跨站脚本攻击 (XSS)。

**主要特性：**

*   **XSS 防护：** 无论指定的清理器配置如何，它都会移除不安全的元素和属性。它是处理不受信任的 HTML 输入的推荐方法，可替代此类情况下的 `Element.innerHTML`。
*   **清理：** 该方法使用清理器来控制允许或移除哪些 HTML 元素、属性和注释。 它可以与默认的清理器或自定义的 `Sanitizer` 或 `SanitizerConfig` 对象一起使用。
*   **上下文感知：** `setHTML()` 会根据元素的上下文丢弃无效元素 (例如，`<table>` 外部的 `<col>`)。
*   **语法：** `element.setHTML(input, options)`
    *   `input`：要清理的 HTML 字符串。
    *   `options`：一个可选对象，其中包含一个 `sanitizer` 属性，用于定义清理器配置。

**示例：**

文章提供了演示如何使用具有默认清理器和自定义清理器的 `setHTML()` 的示例。 这些示例强调，即使自定义清理器允许潜在的不安全元素（如 `<script>`），`setHTML()` 仍然会移除它们以确保 XSS 安全性。

**重要提示：**

*   `setHTML()` 是实验性的，并非所有浏览器都支持。
*   除非特别需要不安全的元素，否则最好使用 `Element.setHTMLUnsafe()`。
*   它不使用 Trusted Types API 进行保护或验证，因为它会对输入字符串进行清理。

---

## 35. 展示HN: 与朋友或机器人在线玩抽象策略棋盘游戏

**原文标题**: Show HN: Play abstract strategy board games online with friends or against bots

**原文链接**: [https://abstractboardgames.com/](https://abstractboardgames.com/)

好的，以下是基于我对那种“Show HN”帖子和URL的预期所做的总结：

这个“Show HN”帖子介绍了一个网络应用程序，可通过abstractboardgames.com访问，该程序允许用户在线玩抽象策略棋盘游戏。该平台可能支持与朋友对战（异步进行，可能通过电子邮件或通知），以及/或者与不同难度级别的电脑控制的机器人对战。

关键功能可能包括：

* **一系列抽象策略游戏：** 预期会有诸如国际象棋、围棋、跳棋、双陆棋之类的游戏，或者可能是一些更小众或不太常见的抽象游戏。 该URL表明重点是 *抽象* 游戏，所以不要期望任何过于主题化或包含大量组件的复杂游戏。
* **多人游戏功能：** 主要吸引力可能是在线与朋友玩游戏的能力，无需实际棋盘或面对面会议。
* **AI对手（机器人）：** 玩家可以与AI对手进行练习或独自享受游戏。 该帖子可能会重点介绍提供的难度级别范围。
* **简洁直观的界面：** 鉴于它是一个专注于策略的网络应用程序，可用性和清晰的棋盘状态视觉呈现至关重要。
* **帐户系统：** 它很可能具有用户帐户，用于跟踪进度、elo值、比赛历史记录和管理朋友。
* **现代网络技术：** 该平台可能使用现代网络开发技术构建，以确保响应性和跨平台兼容性。

这个“Show HN”帖子很可能是为了征求 Hacker News 社区对该平台可用性、功能和游戏选择的反馈。 开发者可能正在寻找改进建议和错误报告。

---

## 36. 当你写宏变得聪明时

**原文标题**: When you get to be smart writing a macro

**原文链接**: [https://tonsky.me/blog/hashp/](https://tonsky.me/blog/hashp/)

本文介绍了一种巧妙的解决方案，用于解决在Clojure的thread-first (`->`) 和 thread-last (`->>`) 宏中使用调试宏 (`#p`) 时遇到的问题。标准的 `#p` 宏用于打印变量的值和形式以进行调试，但在这些线程宏中会失效，因为它在线程逻辑之前展开，从而导致语法错误。

作者最初考虑为每种线程类型创建单独的宏 (`p->` 和 `p->>`)，但目标是寻找一个通用的解决方案。他们通过使用一个探针来实现这一点：一个匿名函数，用于确定它是否在 thread-first 或 thread-last 宏内部。

探针函数接受两个参数，并检查一个特殊的值 (`::undef`) 是否落在第一个或第二个位置。如果 `::undef` 是第一个参数，则表示 thread-last；如果它是第二个参数，则表示 thread-first。如果两者都不是，则默认为原始的 `#p` 行为。这使得 `#p` 宏能够动态地适应其上下文。作者随后提供了一个额外的arity来处理正常情况（即，未在thread first/last宏中使用的情况），其中只有一个参数。

现在，这单个的 `#p` 宏可以在 `->` 和 `->>` 中无缝工作，提供一致的调试体验。该解决方案是 Clojure+ 库的一部分。

---

## 37. 微软将停止Office Online Server服务。

**原文标题**: Microsoft puts Office Online Server on the chopping block

**原文链接**: [https://www.theregister.com/2025/10/22/microsoft_office_online_server/](https://www.theregister.com/2025/10/22/microsoft_office_online_server/)

微软将于2026年12月31日停止Office Online Server服务，届时将不再提供对该本地浏览器版Office套件的支持、安全更新和技术协助。此举迫使客户迁移至微软365，该公司基于云的替代方案，以获得安全和协作功能。

本次停用将影响SharePoint Server SE和Exchange Server SE的用户，因为Office Online Server集成将会消失。微软建议使用Microsoft 365 Apps for Enterprise和Office LTSC 2024作为文档查看和编辑的替代方案。

Skype for Business Server用户也将受到影响，他们将失去诸如演示者备注、高保真PowerPoint渲染、会议中的注释等功能，并体验到较低保真度的嵌入式视频播放。微软建议使用Teams作为会议体验的替代方案。

Office Online Server于2016年推出，是Office Web Apps Server 2013的继任者，旨在为偏好本地数据处理的组织服务。由于没有计划推出直接的继任者，本次停用使得那些优先考虑本地解决方案的用户面临有限的选择，需要切换到Microsoft 365或Office LTSC 2024。

---

## 38. 首个星际软件更新：拯救旅行者1号的漏洞 [视频]

**原文标题**: The first interstellar software update: The hack that saved Voyager 1 [video]

**原文链接**: [https://www.youtube.com/watch?v=p0K7u3B_8rY](https://www.youtube.com/watch?v=p0K7u3B_8rY)

这篇文章的标题具有欺骗性，实际上是指向标准的 YouTube 页脚。它*并非*关于星际软件更新或拯救旅行者1号的黑客行为。相反，这段文字仅仅是 YouTube 页面底部的典型样板信息，包括版权声明、创作者资源链接、广告信息、开发者选项、服务条款、隐私政策、安全指南、关于 YouTube 运作方式的信息、新功能测试以及 Google 版权声明。

简而言之，**没有**关于旅行者1号或任何软件更新的**文章**。标题是标题党，内容无关。

---

## 39. Rivian TM-B 电动自行车

**原文标题**: Rivian's TM-B electric bike

**原文链接**: [https://www.theverge.com/news/804157/rivian-tm-b-electric-bike-price-specs-helmet-quad](https://www.theverge.com/news/804157/rivian-tm-b-electric-bike-price-specs-helmet-quad)

Rivian的微出行衍生公司Also推出了其首款电动自行车TM-B，以及TM-Q脚踏辅助电动四轮自行车和Alpha Wave头盔。TM-B配备独特的“DreamRide”线控脚踏驱动系统，通过踩踏为发电机供电，补充电池。它配备可拆卸电池（538Wh或808Wh），支持USB-C充电，续航里程可达100英里，并且可兼作移动电源。作为3级电动自行车，它在脚踏辅助下时速可达28英里，油门模式下时速20英里（在允许的情况下），扭矩为180牛米。

TM-B采用模块化框架，可轻松改装为货物搬运车、儿童运输车或巡航车。一个5英寸触摸屏控制台控制座椅柱和其他功能。安全功能包括电池、车轮和车架的自动锁定，以及防篡改警报。首发版售价为4,500美元，预计将于2026年春季交付， базовойモデル запланирована на конец 2026 года и оценивается в 4,000 долларов.

Alpha Wave头盔提供先进的旋转冲击保护，集成灯、四扬声器音频系统和降噪麦克风，并与TM-B的控制台集成。TM-Q是TM-B的四轮版本，旨在促进最后一英里交付以及在封闭社区中的休闲使用。Also总裁Chris Yu认为这些电动汽车将成为更广泛采用高效交通方式的催化剂。

---

## 40. Show HN: 用 WebSockets 做的傻瓜式莫尔斯电码聊天应用

**原文标题**: Show HN: Silly Morse code chat app using WebSockets

**原文链接**: [https://noamtamir.github.io/morwse/](https://noamtamir.github.io/morwse/)

这个“Show HN”帖子介绍了一个简单的，可能是实验性的聊天应用，它使用 WebSockets 以摩尔斯电码传输消息。帖子包含一个摩尔斯电码序列（“MORSE”），随后是文本“beep”，大概表示传输代码的听觉或视觉指示。该应用似乎专注于新颖性和实验性，优先考虑不寻常的摩尔斯电码通信方式，而不是实用性或功能丰富性。关键方面是支持实时通信的 WebSocket 技术以及将消息翻译并呈现为摩尔斯电码的中心主题。该帖子可能旨在展示一个功能性的，虽然非常规的应用程序，作为一个有趣的项目或概念验证。

---

## 41. Derek Sivers 的数据库和网络应用

**原文标题**: Derek Sivers's database and web apps

**原文链接**: [https://github.com/sivers/sivers](https://github.com/sivers/sivers)

Derek Sivers 详细介绍了如何以 PostgreSQL 数据库为核心构建 Web 应用程序的独特方法。他的数据是私有的，但代码是开源的，并在 GitHub、GitLab 和 Codeberg 上进行了镜像，但他并不监控这些平台上的贡献。`tables.sql` 文件定义了数据库结构，而 `table-refs.sql` 在初始数据加载后处理外键添加。

他将函数组织到模式中（例如，`o` 代表 omni 函数），并使用 `scripts/reset.sh` 在修改后重新加载模式函数，以确保数据保存。每个函数在 `test/` 目录下都有使用 pgTAP 的相应测试。这些测试在实时数据库的克隆版本上执行，使用 `tap` 脚本简化执行和回滚。

Sivers 强调了他使用 Mustache 将数据库值直接合并到 PostgreSQL 中的 HTML 模板中的方法，以实现简洁性和减少耦合。Web 函数返回两个值：`head` 和 `body`。`head` 值用于覆盖默认的 HTTP 标头和状态代码（例如，404、重定向），而 `body` 包含 HTML 内容。`Call handler` 和 `Response handler` 函数简化了 Ruby HTTP 服务器和 PostgreSQL 之间的交互。

代码进一步结构化为特定于应用程序的模式，例如 `blog/` 用于 sive.rs，`inch/` 用于 inchword.com 等等。Sivers 鼓励程序员就他的设置与他联系，提出问题和意见。

---

## 42. 安德森·霍洛维茨筹集100亿美元，押注下一波科技浪潮

**原文标题**: Andreessen Horowitz lines up $10B for next wave of tech bets

**原文链接**: [https://www.ft.com/content/92262343-b4e0-406e-8a01-2199d45d719e](https://www.ft.com/content/92262343-b4e0-406e-8a01-2199d45d719e)

据报道，安德里森·霍罗维茨正在筹集100亿美元，用于其下一轮科技投资。该文章可通过《金融时报》访问，但设置了付费墙，需要订阅才能解锁并阅读完整内容。《金融时报》推广各种订阅选项，包括标准数字版、试用版、高级数字版和《金融时报》数字版，每种版本提供不同级别的访问权限，以获取其新闻报道和特色内容。这些订阅的价格和权益各不相同，旨在满足不同读者的需求，从基本的新闻访问到高级内容和数字版本。

---

## 43. 我们如何阻止人工智能生成的“贫困色情”虚假图片？

**原文标题**: How do we stop AI-generated 'poverty porn' fake images?

**原文链接**: [https://redasadki.me/2025/10/23/how-do-we-stop-ai-generated-poverty-porn-fake-images/](https://redasadki.me/2025/10/23/how-do-we-stop-ai-generated-poverty-porn-fake-images/)

本文认为，全球健康和人道主义传播中人工智能生成的“贫困色情”图片，主要不是一个技术问题，而是这些领域中根深蒂固的种族主义和殖民主义心态的症状。作者认为，各组织长期以来一直在利用刻板印象和种族化的苦难形象来吸引资助者，这种做法早于人工智能。将责任归咎于人工智能并实施全面禁令被视为一种肤浅的补救措施，让各组织得以避免面对其潜在的偏见。这也会惩罚那些可能以合乎道德的方式利用人工智能来克服资源限制或解决儿童保护和知情同意等伦理问题的小型地方组织。

作者强调，重点应转向挑战系统性的种族主义和殖民主义遗产，这些遗产使对这类图像的需求得以延续。这需要追究世卫组织和联合国等大型组织对其传播行为的责任，支持当地摄影师和艺术家，并要求从根本上改变批准剥削性宣传活动的工作文化。最终，作者认为人工智能仅仅是一个促成者，使有害行为变得更廉价和更快，但该行业内早已存在的殖民主义心态才是问题的根源。呼吁重新评估伦理标准，并消除系统性偏见，这些偏见使对视觉表现中的苦难的剥削得以延续。

---

## 44. 普通酵母能在火星条件下生存

**原文标题**: Common yeast can survive Martian conditions

**原文链接**: [https://phys.org/news/2025-10-common-yeast-survive-martian-conditions.html](https://phys.org/news/2025-10-common-yeast-survive-martian-conditions.html)

该文章发表于PNAS Nexus，报道了常见的酵母（酿酒酵母）可以在模拟的火星环境中存活。研究人员使酵母承受冲击波和高氯酸盐，这是火星环境中的两个挑战性因素。

该酵母部分由于之前的太空研究而被选中，通过形成核糖核蛋白（RNP）凝聚物（一种由RNA和蛋白质组成的保护性结构，包括应激颗粒和P-小体）来应对这两种应激源。暴露于冲击波（在印度高强度冲击波管天体化学实验室模拟）以及与火星土壤中发现的浓度相似的高氯酸钠中的酵母，生长速度减慢但仍然存活。有趣的是，冲击波诱导了应激颗粒和P-小体，而高氯酸盐主要诱导了P-小体。缺乏形成RNP凝聚物能力的突变体在这些应激条件下表现出较差的存活率。

转录组分析进一步揭示了受类火星条件影响的特定RNA转录本。作者得出结论，酵母和RNP凝聚物是理解生命如何在火星上潜在生存的重要因素。该研究强调了酵母的适应能力以及RNP凝聚物对火星应激源的保护作用，为理解火星上过去、现在或未来生命的可能性提供了见解。

---

## 45. 面向内存计算系统的分布式仿真环境

**原文标题**: A Distributed Emulation Environment for In-Memory Computing Systems

**原文链接**: [https://www.arxiv.org/pdf/2510.08257](https://www.arxiv.org/pdf/2510.08257)

此文档似乎是一个PDF文件，包含一篇题为“面向内存计算系统的分布式仿真环境”的研究文章的LaTeX源代码和元数据。

元数据显示作者为Eleni Bougioukou, Anastasios Petropoulos, Nikolaos Toulgaridis, Theodoros Chatzimichail和Theodore Antonakopoulos。该文档使用arXiv GenPDF和pikepdf生成，并具有DOI。它在Creative Commons Attribution 4.0国际许可协议下授权。

文档内容显示了大量的注释和大纲，表明它被组织成多个章节，并包含图、表和引用。“边缘计算”、“AI内存计算”、“SoC验证”和“NVM挑战”等关键词表明该文章讨论了内存计算系统的设计和验证，可能是在边缘应用的背景下。

鉴于标题和包含的引用标记，该文章很可能介绍了一个为促进内存计算架构的设计、测试和验证而开发的分布式仿真环境。与物理原型相比，仿真可以更快速、更经济高效地探索设计选择和性能分析，而分布式环境允许对现代架构的复杂性进行精确建模。提及NVM（非易失性存储器）意味着该系统的重点可能是在内存计算中使用的新兴存储技术。指向表格、图表和章节的注释超链接指出了文档的结构和作者的重要元素。

---

## 46. Show HN: Cuq – Rust GPU内核的形式化验证

**原文标题**: Show HN: Cuq – Formal Verification of Rust GPU Kernels

**原文链接**: [https://github.com/neelsomani/cuq](https://github.com/neelsomani/cuq)

Cuq是一个新的框架，它通过将Rust的中级中间表示（MIR）翻译成Coq，并将其连接到现有的PTX内存模型的Coq形式化，来正式验证Rust GPU内核。这弥合了Rust的安全性保证与NVIDIA的PTX的形式化定义的执行模型之间的差距，解决了Rust GPU代码缺乏形式语义的问题。

该项目为适用于GPU内核的MIR子集定义了一个机械化的操作语义，重点关注内存模型健全性，证明MIR原子和同步操作可以健全地编译为PTX指令。技术方法包括定义MIR的Coq形式化，使用自定义工具将MIR翻译为Coq，并将其连接到现有的PTX语义形式化。

预期成果包括Rust MIR语义的Coq形式化、MIR→PTX内存模型对应定理、原型转换器以及对标准CUDA基准的案例研究。未来的工作包括整合Rust的所有权和生命周期推理。该项目的影响在于建立Rust编译器基础设施与GPU执行的机械化模型之间的正式桥梁，为GPU代码的验证编译和所有权感知的安全性证明铺平道路。提供了一个演示来展示翻译和验证过程。目前的局限性包括侧重于全局内存、精选的MIR子集和简化的浮点处理。

---

## 47. 微软推动Xbox部门实现更高的利润率

**原文标题**: Microsoft Pushes Xbox Division to Hit Higher Profit Margins

**原文链接**: [https://www.bloomberg.com/news/articles/2025-10-23/microsoft-pushes-xbox-studios-to-hit-higher-profit-margins](https://www.bloomberg.com/news/articles/2025-10-23/microsoft-pushes-xbox-studios-to-hit-higher-profit-margins)

无法访问文章链接。

---

## 48. 古登堡计划文学档案馆基金会 CEO 格雷格·纽比去世

**原文标题**: Greg Newby, CEO of Project Gutenberg Literary Archive Foundation, has died

**原文链接**: [https://www.pgdp.net/wiki/In_Memoriam/gbnewby](https://www.pgdp.net/wiki/In_Memoriam/gbnewby)

古登堡计划文学档案馆基金会首席执行官格雷戈里·B·纽比博士，在与癌症短暂斗争后逝世，他担任该职位超过20年。他同时也是分布式校对者基金会董事会的投票成员，并与分布式校对者保持着密切合作。

纽比，原籍加拿大，但在美国长大，之后返回加拿大在育空地区政府工作，同时继续领导古登堡计划。他热衷于古登堡计划让文学作品易于获取的使命，回忆起1987年收到《爱丽丝梦游仙境》电子邮件副本时的兴奋之情。他强调，他在古登堡计划的工作对将文学作品送到人们手中产生了积极影响。

在他的领导下，古登堡计划的电子书藏书增长到超过75,000册，其中许多都是在分布式校对者的帮助下制作的。2023年，他与微软和麻省理工学院合作创建了古登堡计划人工智能叙述有声读物开放馆藏，该馆藏被《时代》杂志评为年度最佳发明之一。分布式校对者社区及其他人士将深切缅怀他的远见卓识和不知疲倦的领导。

---

## 49. 皮力传输：由体内射频能量供电的全身体穿戴设备 (2024)

**原文标题**: Power-over-Skin: Full-Body Wearables Powered by Intra-Body RF Energy (2024)

**原文链接**: [https://dl.acm.org/doi/10.1145/3654777.3676394](https://dl.acm.org/doi/10.1145/3654777.3676394)

无法访问该文章链接。

---

## 50. 我在jj看到了未来。

**原文标题**: I see a future in jj

**原文链接**: [https://steveklabnik.com/writing/i-see-a-future-in-jj/](https://steveklabnik.com/writing/i-see-a-future-in-jj/)

在2025年10月22日的这篇博文中，Rust编程语言社区的知名人物Steve Klabnik解释了他参与“jj”（一个用Rust编写的新版本控制系统）的决定。他将jj的潜力与他早期对Rust未来成功的评估进行了类比。

Klabnik强调，与Rust在C和C++主导的领域中崛起类似，jj为Git提供了一个引人注目的替代方案，尤其因为它可以在Git仓库中逐步采用。他强调jj具有强大的市场契合度、由Martin（jj的创建者）领导的强大团队以及不断增长的用户群。他指出谷歌在内部采用jj是一个重要的社会证明，并指出它被用于小型个人项目和大型单体仓库。

虽然承认有经验的Git用户需要一个学习曲线，但Klabnik认为jj对新手来说是友好的，并且培养了一个充满激情的社区。他还强调jj被用作Piper的后端，并且可以展示其他用户尝试所需的社会证明。

这篇博文的最后，Klabnik宣布他将离开Oxide加入ERSC，一家在jj之上构建开发者协作平台的新公司。他表达了他很高兴能花更多时间在jj社区，为平台的开发做出贡献，并创建更多的教程。他看到了jj光明的未来，正如他见证Rust的成功一样。

---

## 51. 柳树量子芯片展示了硬件上可验证的量子优势

**原文标题**: Willow quantum chip demonstrates verifiable quantum advantage on hardware

**原文链接**: [https://blog.google/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/](https://blog.google/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/)

谷歌量子AI团队宣布，他们的“柳树”（Willow）量子芯片取得重大突破：首次在硬件上演示了可验证的量子优势。 他们发表在《自然》杂志上的“量子回声”（Quantum Echoes）算法，比超算上最好的经典算法快13000倍。 该算法可用于了解从分子到黑洞的系统结构。

“量子回声”算法是一种可验证的量子优势，因为该结果可以在其他类似的量子计算机上重复，以获得相同的结果。 该算法的工作原理是向量子系统发送信号，扰动一个量子比特，然后反转信号，监听由量子干涉放大的“回声”。

在另一项相关的实验中，他们使用“量子回声”算法作为“分子标尺”，通过核磁共振（NMR）测量分子中更长的距离。 该实验成功测量了15和28个原子分子的几何结构。 结果与传统核磁共振一致，并揭示了新数据，验证了该方法的有效性。

这项突破是量子计算在医药和材料科学等领域的实际应用的重要一步，特别是对于模拟量子力学现象，例如分子结构。 这可能会显著影响药物发现和新材料的表征。 该团队现在专注于实现量子硬件路线图上的第三个里程碑：一个长寿命的逻辑量子比特。

---

## 52. HP SitePrint
惠普场地打印

**原文标题**: HP SitePrint

**原文链接**: [https://www.hp.com/us-en/printers/site-print/layout-robot.html](https://www.hp.com/us-en/printers/site-print/layout-robot.html)

HP SitePrint是一款建筑放样机器人，旨在自动化并提高建筑工地放样和楼板偏差标记的效率和精度。它结合了惠普的打印和机器人技术专长，以加速项目进度、减少错误并提高现场生产力。

主要特性和优势包括：

*   **提高效率：** 自主技术可降低放样成本并节省时间，从而解放熟练劳动力，使其从事增值任务。生产力提升高达 10 倍。
*   **提高精度：** 借助高达 +/- 3/32 英寸（+/- 2 毫米 EMEA 版本）的放样精度，以及 +/- 1/32 英寸（+/- 0.8 毫米 EMEA 版本）的楼板偏差标记精度（使用 SMR 棱镜和 1 英寸全站仪时），确保复杂布局和楼板水平度的精确实施。
*   **易于使用：** 一体化解决方案便携且易于管理。用户可以准备 CAD 文件、进行场地准备、使用机器人全站仪设置解决方案，并通过用户界面执行作业。
*   **楼板偏差标记：** HP SitePrint 自动化楼板偏差标记过程，节省时间、加强沟通并简化施工流程。
*   **Value Pack 3.0：** 包括机器人升级套件，具有改进的导航速度、优化的避障功能、实时路线调整以及增强的连续运行能力。
*   **云管理：** HP SitePrint 云允许共享 CAD 文件、监控作业进度以及管理会计报告。
*   **兼容性：** 惠普与 Leica、Topcon 和 Trimble 等定位行业领导者合作，确保与各种机器人全站仪的兼容性。
*   **按需付费模式：** 基于使用量的定价结构包括支持、维修、软件和固件更新。
*   **客户成功案例：** 案例研究表明，在各种施工场景中，成本显著降低，生产力显著提高。

HP SitePrint 是一款可提高建筑放样过程效率、精度和整体生产力的解决方案。

---

## 53. LibCube：更轻松地发现音频合成器中的新音色

**原文标题**: LibCube: Find new sounds from audio synths easier

**原文链接**: [https://github.com/cslr/libcube-public/wiki](https://github.com/cslr/libcube-public/wiki)

LibCube 是一个 C++ DLL，它利用机器学习来简化音频合成器的声音设计。它通过将合成器过多的参数减少到易于管理的两到三个来解决参数过多的问题。这使得用户更容易在复杂的参数空间中搜索新的和有趣的声音。

该库以合成器预设值为输入，并采用 t-SNE 等算法将高维参数空间映射到包含“好声音”的低维空间中。提供的 `test_cube_c_api.cpp` 演示了如何使用 C API（在 `cube_interface.h` 中定义）以及 `cube_param.dll`。包含了 Linux（使用 `compile.sh`）和 Windows（使用带有 MSYS2 MINGW 或 Visual C++ 的 `compile.bat`）的编译说明。

虽然该库利用多核 CPU 进行高效计算，但使用神经网络的参数重建过程计算密集型，并且不支持 DAW 中的实时自动化。用户可以更改参数并离线播放乐器。

作者 Tomas Ukkonen 提供了使用 LibCube 找到的声音示例和一个演示其与商业 Sylent1 VST2 合成器一起使用的 YouTube 视频。欢迎通过 tomas.ukkonen@iki.fi 提供反馈，但可能无法提供广泛的支持。该库的许可方式允许商业使用。

---

## 54. Cloudflare Circl FourQ实现中的密码学问题 (CVE-2025-8556)

**原文标题**: Cryptographic Issues in Cloudflare's Circl FourQ Implementation (CVE-2025-8556)

**原文链接**: [https://www.botanica.software/blog/cryptographic-issues-in-cloudflares-circl-fourq-implementation](https://www.botanica.software/blog/cryptographic-issues-in-cloudflares-circl-fourq-implementation)

本文详细介绍了 Cloudflare CIRCL 库中发现的密码学漏洞 (CVE-2025-8556)，特别是其 FourQ 椭圆曲线的实现。这些漏洞主要集中在 Diffie-Hellman 密钥交换中使用的点验证不足，可能导致“无效点攻击”。

文章解释说，如果没有适当的验证，攻击者可以提供属于具有平滑子群阶的曲线的无效点。 这使得使用中国剩余定理更容易暴力破解服务器的密钥。 虽然 Edwards 曲线不易受到标准的无效曲线攻击，但可以通过使用 (0, y) 形式的点进行特定的退化曲线攻击。

报告的问题包括：

*   **Point.Unmarshal 中的不正确的点验证：** 未能在共轭 x 值后重新验证。
*   **pointR1.isEqual 中的错误点比较：** 当 Z 为零时返回 true，这是一个无效的投影坐标。
*   **pointR1.ClearCofactor 中缺少点验证：** 未在清除辅因子后验证点的有效性。
*   **pointR1.ScalarMult 中缺少点验证：** 假设有效的投影值并且该点在曲线上。

作者向 Cloudflare 报告了这些漏洞，随后 Cloudflare 承认并修复了这些漏洞。 文章强调了在任何计算之前进行点验证以防止此类攻击的重要性，并参考了相关的 IETF 规范和研究论文。

---

## 55. 尽可能多的CPU和其他有趣芯片的芯片照片

**原文标题**: Die shots of as many CPUs and other interesting chips as possible

**原文链接**: [https://commons.wikimedia.org/wiki/User:Birdman86](https://commons.wikimedia.org/wiki/User:Birdman86)

这个维基共享资源页面是由 Pauli Rautakorpi 发起的一个项目，旨在收集和展示各种 CPU 和其他集成电路的芯片照片。该页面按芯片架构和系列组织，方便浏览该合集。

该合集广泛涵盖了 x86 CPU，从 8086/8088 开始，一直到第五代（奔腾、K5、Cyrix 5x86/6x86），包括英特尔、AMD、Cyrix、德州仪器等各种制造商。它还包括与这些 CPU 兼容的 FPU 的芯片照片。

除了 x86 之外，该项目还涵盖了来自不同架构的各种 CPU 和 FPU，包括 AMD Am29k、英特尔 i860/i960、DEC PDP-11/VAX/Alpha、惠普 PA-RISC、摩托罗拉 680x/68k/88k/PowerPC、MIPS、SPARC 和 ARM 处理器。此外，它还包括来自 AT&T、Bull、Data General、Fairchild、Inmos、Intergraph、Intersil、MOS Technology、National Semiconductor、nCUBE、RCA、Signetics、Tandem、德州仪器、TriMedia、Unisys 和 Zilog 等制造商的不太常见的处理器。

该项目还包括各种支持芯片的芯片照片，例如图形芯片、视频编解码器、RAMDAC、缓存控制器、内存控制器、内存管理单元、DMA 控制器、总线和接口控制器、中断控制器、网络控制器、存储芯片和加密芯片。最后是一个用于未识别或未知芯片的部分。作者计划继续向该合集中添加芯片照片。

---

## 56. SourceFS: 使用虚拟文件系统将 2 小时以上的 Android 构建缩短为 15 分钟的任务

**原文标题**: SourceFS: A 2h+ Android build becomes a 15m task with a virtual filesystem

**原文链接**: [https://www.source.dev/journal/sourcefs](https://www.source.dev/journal/sourcefs)

以下是“SourceFS：通过虚拟文件系统，2小时以上的安卓构建缩短至15分钟”文章的摘要：

本文讨论了SourceFS，这是Sourcegraph开发的一种虚拟文件系统，旨在显著缩短Android构建时间。大型Android构建通常耗时数小时，对开发人员的生产力构成重大瓶颈。由于依赖项和输入文件的细微变化，传统的缓存解决方案通常效果不佳，导致频繁的缓存未命中。

SourceFS通过提供一个只读的、内容寻址的文件系统来解决这个问题，该文件系统由远程构建服务器填充。这意味着本地机器只需要下载当前构建所需的特定文件，而不是整个源代码。内容寻址确保只传输已更改的文件。

SourceFS的主要优点是：

*   **大幅缩短构建时间：** 文章声称，大型Android构建的时间从2小时以上缩短到大约15分钟。
*   **提高开发人员的生产力：** 更快的构建速度可以实现更快的迭代周期和更频繁的测试。
*   **降低本地资源使用率：** 只下载必要的文件，从而最大限度地减少磁盘空间需求并降低I/O开销。
*   **一致性和可重复性：** SourceFS的内容寻址特性保证了相同的源代码始终产生相同的构建产物。

本质上，SourceFS将获取和准备源代码的繁重工作转移到集中式服务器，使本地开发机器能够专注于实际的构建过程，只需必要的文件。它代表着从“下载所有内容并希望缓存有效”到“只下载所需内容”的转变。

---

## 57. 最温文尔雅且著作等身的英国捉鬼人

**原文标题**: The mild mannered Englishman who was the most prolific ghost hunter

**原文链接**: [https://lithub.com/the-mild-mannered-englishman-who-was-the-worlds-most-prolific-ghost-hunter/](https://lithub.com/the-mild-mannered-englishman-who-was-the-worlds-most-prolific-ghost-hunter/)

本·马歇尔的文章介绍了托尼·康奈尔，一位看似普通的英国人，却成为了世界上最多产的超自然现象调查员之一。文章以令人不安的超自然事件开场：一对悲伤的夫妇在降神会上遇到的幽灵孩子，一个被无形的“黑狗”折磨的男人，以及一间莫名其妙被水淹没的房子。

作者描述了他深入研究康奈尔在剑桥大学图书馆的浩瀚档案的经历。他详细介绍了康奈尔数十年调查超自然现象所积累的大量报告、信件、照片和笔记。这些材料包括普通人描述他们与鬼魂、骚灵现象和其他无法解释的事件的信件，以及来自学者甚至卡尔·荣格的信件。

文章强调了驱动康奈尔工作的核心问题：我们死后会发生什么？他毕生致力于探索人类意识是否能超越肉体的死亡。文章表明，康奈尔为那些努力应对无法解释的现象的普通人提供了一个避风港，提供了一个在其他形式的安慰和终结方式，如科学或宗教，失效时，调查这些声称的空间。最终，文章将康奈尔定位为超心理学领域的一个关键人物，留下了一份重要的档案，这份档案一直在探索关于生命、死亡和超自然现象的持久谜团。

---

## 58. 对《身体从未忘记》的批评

**原文标题**: Criticisms of “The Body Keeps the Score”

**原文链接**: [https://josepheverettwil.substack.com/p/the-body-keeps-the-score-is-bullshit](https://josepheverettwil.substack.com/p/the-body-keeps-the-score-is-bullshit)

无法访问文章链接。

---

## 59. Linux Capabilities 再探

**原文标题**: Linux Capabilities Revisited

**原文链接**: [https://dfir.ch/posts/linux_capabilities/](https://dfir.ch/posts/linux_capabilities/)

本文重新探讨了Linux capabilities，一种细粒度的访问控制机制，它将root权限划分为不同的单元。文章强调了理解和监控capabilities对于安全性的重要性，因为与传统的SUID/SGID位相比，它们提供了一种潜在的隐蔽方式来提升权限。

文章演示了capabilities如何被利用。例如，授予Python `cap_setuid` capability允许非root用户生成root shell，本质上是在系统上留下后门。`setcap`命令在可执行文件上设置这些capabilities，而`getcap`有助于枚举具有capabilities的文件。作者还介绍了如何通过使用`capsh --decode`和`getpcaps`检查`/proc`目录来查找它们。您还可以使用`setcap -r`命令删除capabilities。

文章强调，安全审计应包括搜索capabilities，以及传统的SUID/SGID检查。文章提到了诸如`getcap`、`getfattr`之类的工具以及LinPEAS之类的脚本来帮助完成此过程。文章还引用了用于检测`setcap`实用程序使用的Elastic规则。最后，文章鼓励进一步探索用户capabilities（存储在`/etc/security/capability.conf`中）和AmbientCapabilities（在服务文件中指定），并提供了指向其他资源的链接，以进行深入学习。

---

## 60. 法国前总统萨科齐开始服刑

**原文标题**: French ex-president Sarkozy begins jail sentence

**原文链接**: [https://www.bbc.com/news/articles/cvgkm2j0xelo](https://www.bbc.com/news/articles/cvgkm2j0xelo)

法国前总统尼古拉·萨科齐因涉嫌非法利用利比亚卡扎菲的资金资助其2007年竞选活动，已开始服刑五年。 这标志着自二战后菲利普·贝当以来，法国首位前总统入狱。

萨科齐坚称自己无罪并已提出上诉。为了他的安全，他已被安置在拉桑特监狱的隔离区，在一个配备基本设施的小牢房里。在隔离期间，他与其他囚犯的接触有限，每天只有一小时的锻炼时间。

在入狱之前，萨科齐表达了他对不公的感受和对法国的悲痛，坚称自己是无辜的，并誓言真相终将胜出。他的律师也提出了释放他的请求。人们看到他和妻子卡拉·布吕尼-萨科齐在支持者的簇拥下离开了家。

此案在法国引起了相当大的争议。 马克龙总统承认，一位前总统入狱会引发震惊和评论，同时强调他对司法判决不加干涉。司法部长热拉尔·达尔马宁计划前往监狱探望萨科齐。

萨科齐还面临其他法律挑战，包括即将对Bygmalion事件中针对六个月监禁判决的上诉做出裁决，这是一起独立的非法竞选资金案。他此前曾被判试图贿赂一名法官。

---

## 61. Patina: UEFI固件的Rust实现

**原文标题**: Patina: a Rust implementation of UEFI firmware

**原文链接**: [https://github.com/OpenDevicePartnership/patina](https://github.com/OpenDevicePartnership/patina)

Patina 是一个用 Rust 语言实现的 UEFI 固件，旨在用内存安全的 Rust 代码替换基于 C 的核心 UEFI 组件，从而提高系统固件的安全性和稳定性，同时保持启动性能。目前处于 Beta 阶段，Patina 鼓励平台测试和反馈。

关键方面包括发布流程、可通过托管站点或使用 `mdbook` 自托管的文档，以及使用 `rustup` 设置 Rust 工具链并安装诸如 `cargo-make` 和 `cargo-llvm-cov` 等必要工具的说明。

该项目支持为 aarch64、x64 和原生目标构建。它提供运行单元测试、构建平台测试和更新 Rust 版本的命令，并强调在更改最低支持的 Rust 版本时要进行仔细评估和论证。该项目还支持覆盖率分析和基准测试。

项目路线图侧重于稳定化（错误修复、性能改进）、扩展（添加新组件和 MM Core 支持）以及生态系统集成（固件和更广泛的 Rust 社区协作）。 欢迎社区贡献。

---

## 62. 互联网最大的烦恼：Cookie法应针对浏览器，而非网站

**原文标题**: Internet's biggest annoyance: Cookie laws should target browsers, not websites

**原文链接**: [https://nednex.com/en/the-internets-biggest-annoyance-why-cookie-laws-should-target-browsers-not-websites/](https://nednex.com/en/the-internets-biggest-annoyance-why-cookie-laws-should-target-browsers-not-websites/)

本文认为，当前 Cookie 同意法（如 GDPR 和 CCPA）的实施效果不佳，且对互联网用户过于烦扰。作者批评网站上不断出现的 Cookie 横幅广告，导致“同意疲劳”和控制幻觉。这些法律不公平地给小型网站所有者带来了技术和法律上的复杂性，而大型公司则可以更轻松地驾驭这一体系。

核心建议是一个根本性的转变：将 Cookie 同意管理从各个网站转移到网络浏览器。用户无需在每个网站上都遇到 Cookie 横幅广告，而只需在其浏览器（Chrome、Firefox、Safari 等）中设置一次隐私偏好。然后，浏览器将充当个人隐私执行者，根据用户定义的设置自动允许或阻止 Cookie。

这种以浏览器为中心的方法具有以下几个优点：通过一次深思熟虑的决定，实现真正的用户控制；更清洁、更快的网络体验；大大减轻网站所有者的负担，无需笨拙的同意管理平台；监管机构可以更轻松地进行执法，专注于浏览器开发商，而不是数百万个网站。作者以“请勿追踪”信号的失败为例，作为一个警示故事，强调了浏览器端执行以确保合规性的必要性。文章最后倡导一个更简单、更高效的系统，即由浏览器而非网站来管理 Cookie 同意，从而创建一个更用户友好和尊重隐私的互联网。

---

## 63. MinIO 停止分发免费 Docker 镜像

**原文标题**: MinIO stops distributing free Docker images

**原文链接**: [https://github.com/minio/minio/issues/21647#issuecomment-3418675115](https://github.com/minio/minio/issues/21647#issuecomment-3418675115)

报告指出，最近MinIO安全版本（Security/CVE RELEASE.2025-10-15T17-29-55Z）的Docker镜像在quay.io和DockerHub上均缺失。报告者询问这是否为预期行为，并请求推送用于Docker安装的新版本。该问题被标记为“社区”和“按预期工作”，暗示MinIO可能已故意停止分发免费Docker镜像或改变了其分发策略。

---

## 64. 围棋精妙

**原文标题**: Go subtleties

**原文链接**: [https://harrisoncramer.me/15-go-sublteties-you-may-not-already-know/](https://harrisoncramer.me/15-go-sublteties-you-may-not-already-know/)

Go语言的15个微妙之处

1. 整数范围迭代：Go 1.22 允许直接迭代整数。
2. 重命名包：Go 的 LSP 可以重命名包并更新所有引用，包括目录。
3. 约束泛型函数签名：`~` 运算符将泛型类型签名约束为底层类型。
4. 基于索引的字符串插值：`fmt.Printf` 允许索引字符串格式化以重复值。
5. `time.After` 函数：创建一个通道，在指定持续时间后接收消息，可用于设置截止时间。
6. `embed` 包：将非 Go 文件直接嵌入到 Go 二进制文件中。
7. `len()` 处理字符串：返回字节数，而不是字符数，需要 rune 迭代处理 UTF-8 字符串。
8. Nil 接口：即使底层值为 nil，接口也可能为非 nil，因为存在“装箱”。
9. 在 Nil 值上调用方法：可以在 nil 结构体上调用方法，但访问属性将引发 panic。
10. 范围迭代 Map 中的变量引用：在范围循环中更新 map 不能保证在迭代期间生效。
11. 返回自定义错误：返回带有结构化数据的类型化错误以进行调试。
12. 上下文感知函数：在上下文感知函数中同时 select 上下文和通道，以处理取消。
13. 空结构体：占用零字节，通常用于通道上的信号传递。
14. 隐藏的接口满足：由于提升的方法，结构体嵌入可能会导致意外行为。
15. JSON "-" 标签："-" 标签在序列化为 JSON 时会忽略字段。
16. 时间比较：从 Time 结构转换时，时区信息会自动附加到字符串，这意味着字符串比较不起作用。请改用 .Equal() 方法。
17. wg.Go 函数：在 go 1.25 中添加，简化了向等待组添加 go 协程的操作。

---

## 65. OpenAI新浏览器引发“难以逾越”的安全担忧

**原文标题**: OpenAI's New Browser Raises 'Insurmountably High' Security Concerns

**原文链接**: [https://gizmodo.com/openais-new-browser-raises-insurmountably-high-security-concerns-2000675516](https://gizmodo.com/openais-new-browser-raises-insurmountably-high-security-concerns-2000675516)

OpenAI新款ChatGPT Atlas浏览器，一款集成聊天机器人的Chromium内核浏览器，引发了重大的安全和隐私担忧。虽然它旨在通过对话式界面和“记忆”（存储访问网站的上下文信息）等功能来增强网络导航，但该浏览器默认的数据收集令专家感到震惊。

该浏览器会保存用户互动和偏好的详细信息，排除个人身份证明等某些敏感信息，但这依赖于系统按预期工作。内置的AI代理，旨在浏览和完成任务，尤其容易受到攻击。安全研究人员已经演示了提示注入攻击如何劫持此类代理，从而可能暴露登录凭据和身份验证码。

程序员Simon Willison强调了缺乏针对提示注入的明确防御措施，以及浏览器中AI代理相关的高风险隐私和安全风险。一名黑客已经演示了一种“剪贴板注入”漏洞，导致用户访问钓鱼网站。专家警告说，存在潜在的重大隐私和安全漏洞，而Atlas同时收集大量的用户数据用于个性化。这种漏洞和数据收集的结合，创造了一个复杂的监控系统，可能导致对用户隐私和安全的灾难性后果。

---

## 66. VortexNet：基于流体动力学的神经网络

**原文标题**: VortexNet: Neural network based on fluid dynamics

**原文链接**: [https://github.com/samim23/vortexnet](https://github.com/samim23/vortexnet)

The "VortexNet: Neural Computing through Fluid Dynamics" project introduces a novel neural network architecture inspired by fluid dynamics, specifically vortex behavior. The repository provides toy implementations to illustrate how PDE-based vortex layers and fluid-inspired mechanisms can be integrated into neural networks, with a focus on autoencoders.

The project includes two main scripts: `vortexnet_mnist.py`, which demonstrates a VortexNet autoencoder trained on the MNIST dataset, and `vortexnext_image.py`, an advanced version for custom image datasets featuring data augmentation and latent space interpolation. These scripts are intended as educational prototypes rather than fully optimized solvers.

To use the code, users need to clone the repository, install Python dependencies (torch, torchvision, matplotlib, pyyaml, scikit-learn, seaborn, tensorboard), and prepare the data. MNIST is automatically downloaded. For custom images, users should place them in the `my_data/` directory. The scripts can be run using Python 3.11, with `vortexnext_image.py` requiring a configuration file (`config_image.yaml`).

The project emphasizes that the scripts are toy prototypes for educational purposes. Output, logs, reconstructed images, and model checkpoints are saved in a user-specified output directory, and TensorBoard can be used to monitor training progress. The configuration file is crucial for proper setup before running the advanced script.


---

## 67. The Tonnetz

**原文标题**: The Tonnetz

**原文链接**: [https://thetonnetz.com/](https://thetonnetz.com/)

生成摘要时出错

---

## 68. Is It Time to Regulate React?

**原文标题**: Is It Time to Regulate React?

**原文链接**: [https://dbushell.com/2025/10/23/react-regulation/](https://dbushell.com/2025/10/23/react-regulation/)

生成摘要时出错

---

## 69. Portable GPU Programming – csc.fi

**原文标题**: Portable GPU Programming – csc.fi

**原文链接**: [https://github.com/csc-training/portable-gpu-programming](https://github.com/csc-training/portable-gpu-programming)

生成摘要时出错

---

## 70. The security paradox of local LLMs

**原文标题**: The security paradox of local LLMs

**原文链接**: [https://quesma.com/blog/local-llms-security-paradox/](https://quesma.com/blog/local-llms-security-paradox/)

生成摘要时出错

---

## 71. I, Sharpie

**原文标题**: I, Sharpie

**原文链接**: [https://www.commonplace.org/p/chris-griswold-i-sharpie](https://www.commonplace.org/p/chris-griswold-i-sharpie)

生成摘要时出错

---

## 72. Designing software for things that rot

**原文标题**: Designing software for things that rot

**原文链接**: [https://drobinin.com/posts/designing-software-for-things-that-rot/](https://drobinin.com/posts/designing-software-for-things-that-rot/)

生成摘要时出错

---

## 73. YASA beats own power density record pushing electric motor to 59kW/kg benchmark

**原文标题**: YASA beats own power density record pushing electric motor to 59kW/kg benchmark

**原文链接**: [https://yasa.com/news/yasa-smashes-own-unofficial-power-density-world-record-pushing-state-of-the-art-electric-motor-to-staggering-new-59kw-kg-benchmark/](https://yasa.com/news/yasa-smashes-own-unofficial-power-density-world-record-pushing-state-of-the-art-electric-motor-to-staggering-new-59kw-kg-benchmark/)

生成摘要时出错

---

## 74. Erowid - Documenting the Complex Relationship Between Humans and Psychoactives

**原文标题**: Erowid - Documenting the Complex Relationship Between Humans and Psychoactives

**原文链接**: [https://www.erowid.org](https://www.erowid.org)

生成摘要时出错

---

## 75. Evaluating the Infinity Cache in AMD Strix Halo

**原文标题**: Evaluating the Infinity Cache in AMD Strix Halo

**原文链接**: [https://chipsandcheese.com/p/evaluating-the-infinity-cache-in](https://chipsandcheese.com/p/evaluating-the-infinity-cache-in)

生成摘要时出错

---

## 76. Show HN: Cadence – A guitar theory app

**原文标题**: Show HN: Cadence – A guitar theory app

**原文链接**: [https://cadenceguitar.com/](https://cadenceguitar.com/)

生成摘要时出错

---

## 77. AI assistants misrepresent news content 45% of the time

**原文标题**: AI assistants misrepresent news content 45% of the time

**原文链接**: [https://www.bbc.co.uk/mediacentre/2025/new-ebu-research-ai-assistants-news-content](https://www.bbc.co.uk/mediacentre/2025/new-ebu-research-ai-assistants-news-content)

生成摘要时出错

---

## 78. Galaxy XR: The first Android XR headset

**原文标题**: Galaxy XR: The first Android XR headset

**原文链接**: [https://blog.google/products/android/samsung-galaxy-xr/](https://blog.google/products/android/samsung-galaxy-xr/)

生成摘要时出错

---

## 79. US probes Alphabet unit Waymo robotaxis over school bus safety

**原文标题**: US probes Alphabet unit Waymo robotaxis over school bus safety

**原文链接**: [https://www.yahoo.com/news/articles/us-investigates-waymo-robotaxis-over-102015308.html](https://www.yahoo.com/news/articles/us-investigates-waymo-robotaxis-over-102015308.html)

生成摘要时出错

---

## 80. Rethinking CQRS: An Interview on OpenCQRS

**原文标题**: Rethinking CQRS: An Interview on OpenCQRS

**原文链接**: [https://docs.eventsourcingdb.io/blog/2025/10/23/rethinking-cqrs-an-interview-on-opencqrs/](https://docs.eventsourcingdb.io/blog/2025/10/23/rethinking-cqrs-an-interview-on-opencqrs/)

生成摘要时出错

---

## 81. Trump Pardons Convicted Binance Founder

**原文标题**: Trump Pardons Convicted Binance Founder

**原文链接**: [https://www.wsj.com/finance/currencies/trump-pardons-convicted-binance-founder-7509bd63](https://www.wsj.com/finance/currencies/trump-pardons-convicted-binance-founder-7509bd63)

生成摘要时出错

---

## 82. Knocker, a knock based access control system for your homelab

**原文标题**: Knocker, a knock based access control system for your homelab

**原文链接**: [https://github.com/FarisZR/knocker](https://github.com/FarisZR/knocker)

生成摘要时出错

---

## 83. The Hidden Engineering of Niagara Falls

**原文标题**: The Hidden Engineering of Niagara Falls

**原文链接**: [https://practical.engineering/blog/2025/10/21/the-hidden-engineering-of-niagara-falls](https://practical.engineering/blog/2025/10/21/the-hidden-engineering-of-niagara-falls)

生成摘要时出错

---

## 84. The Logarithmic Time Perception Hypothesis

**原文标题**: The Logarithmic Time Perception Hypothesis

**原文链接**: [http://www.kafalas.com/Logtime.html](http://www.kafalas.com/Logtime.html)

生成摘要时出错

---

## 85. Resistant Bacteria Are Advancing Faster Than Antibiotics

**原文标题**: Resistant Bacteria Are Advancing Faster Than Antibiotics

**原文链接**: [https://www.wired.com/story/resistant-bacteria-are-advancing-faster-than-antibiotics/](https://www.wired.com/story/resistant-bacteria-are-advancing-faster-than-antibiotics/)

生成摘要时出错

---

## 86. Enchanting Imposters

**原文标题**: Enchanting Imposters

**原文链接**: [https://daily.jstor.org/enchanting-imposters/](https://daily.jstor.org/enchanting-imposters/)

生成摘要时出错

---

## 87. Trump pardons convicted Binance founder Zhao, White House says

**原文标题**: Trump pardons convicted Binance founder Zhao, White House says

**原文链接**: [https://www.reuters.com/world/us/trump-pardons-convicted-binance-founder-zhao-white-house-says-2025-10-23/](https://www.reuters.com/world/us/trump-pardons-convicted-binance-founder-zhao-white-house-says-2025-10-23/)

生成摘要时出错

---

## 88. Show HN: Create interactive diagrams with pop-up content

**原文标题**: Show HN: Create interactive diagrams with pop-up content

**原文链接**: [https://vexlio.com/features/interactive-diagrams-with-popups/](https://vexlio.com/features/interactive-diagrams-with-popups/)

生成摘要时出错

---

## 89. Bare Metal (The Emacs Essay)

**原文标题**: Bare Metal (The Emacs Essay)

**原文链接**: [https://waxbanks.wordpress.com/2025/08/01/bare-metal-the-emacs-essay/](https://waxbanks.wordpress.com/2025/08/01/bare-metal-the-emacs-essay/)

生成摘要时出错

---

## 90. Sodium-ion batteries have started to appear in cars and home storage

**原文标题**: Sodium-ion batteries have started to appear in cars and home storage

**原文链接**: [https://cleantechnica.com/2025/10/22/the-sodium-ion-battery-revolution-has-started/](https://cleantechnica.com/2025/10/22/the-sodium-ion-battery-revolution-has-started/)

生成摘要时出错

---

## 91. Rust MinIO Alternative

**原文标题**: Rust MinIO Alternative

**原文链接**: [https://github.com/rustfs/rustfs](https://github.com/rustfs/rustfs)

生成摘要时出错

---

## 92. The death of thread per core

**原文标题**: The death of thread per core

**原文链接**: [https://buttondown.com/jaffray/archive/the-death-of-thread-per-core/](https://buttondown.com/jaffray/archive/the-death-of-thread-per-core/)

生成摘要时出错

---

## 93. Clojure Zippers

**原文标题**: Clojure Zippers

**原文链接**: [https://grishaev.me/en/clojure-zippers/](https://grishaev.me/en/clojure-zippers/)

生成摘要时出错

---

## 94. André Gorz predicted the revolt against meaningless work (2023)

**原文标题**: André Gorz predicted the revolt against meaningless work (2023)

**原文链接**: [https://znetwork.org/znetarticle/andre-gorz-was-the-theorist-who-predicted-the-revolt-against-meaningless-work/](https://znetwork.org/znetarticle/andre-gorz-was-the-theorist-who-predicted-the-revolt-against-meaningless-work/)

生成摘要时出错

---

## 95. ChatGPT Atlas

**原文标题**: ChatGPT Atlas

**原文链接**: [https://chatgpt.com/atlas](https://chatgpt.com/atlas)

生成摘要时出错

---

## 96. The key to universe exists may lie in an 1800s knot idea science once dismissed

**原文标题**: The key to universe exists may lie in an 1800s knot idea science once dismissed

**原文链接**: [https://phys.org/news/2025-10-key-universe-1800s-idea-science.html](https://phys.org/news/2025-10-key-universe-1800s-idea-science.html)

生成摘要时出错

---

## 97. Researchers complete first human trial on viability of enteral ventilation

**原文标题**: Researchers complete first human trial on viability of enteral ventilation

**原文链接**: [https://newatlas.com/disease/butt-breathing-ignobel-prize/](https://newatlas.com/disease/butt-breathing-ignobel-prize/)

生成摘要时出错

---

## 98. Iceland reports the presence of mosquitoes as climate warms

**原文标题**: Iceland reports the presence of mosquitoes as climate warms

**原文链接**: [https://www.npr.org/2025/10/22/nx-s1-5582748/iceland-mosquitoes-first-time](https://www.npr.org/2025/10/22/nx-s1-5582748/iceland-mosquitoes-first-time)

生成摘要时出错

---

## 99. Wikipedia says traffic is falling due to AI search summaries and social video

**原文标题**: Wikipedia says traffic is falling due to AI search summaries and social video

**原文链接**: [https://techcrunch.com/2025/10/18/wikipedia-says-traffic-is-falling-due-to-ai-search-summaries-and-social-video/](https://techcrunch.com/2025/10/18/wikipedia-says-traffic-is-falling-due-to-ai-search-summaries-and-social-video/)

生成摘要时出错

---

## 100. 20,858 Public Domain Audio Books

**原文标题**: 20,858 Public Domain Audio Books

**原文链接**: [https://librivox.org/search](https://librivox.org/search)

生成摘要时出错

---

