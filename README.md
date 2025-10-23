# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-23.md)

*最后自动更新时间: 2025-10-23 17:49:21*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 2 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 3 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 4 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 5 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 6 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 7 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 8 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 9 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 10 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 11 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 12 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 13 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 14 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 15 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 16 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 17 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 18 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 19 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 20 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 21 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 22 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 23 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 24 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 25 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 26 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 27 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 28 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 29 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 30 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 31 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 32 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 33 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 34 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 35 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 36 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 37 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 38 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 39 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 40 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 41 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 42 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 43 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 44 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 45 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 46 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 47 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 48 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 49 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 50 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 51 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 52 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 53 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 54 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 55 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 56 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 57 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 58 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 59 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 60 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 61 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 62 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 63 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 64 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 65 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 66 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 67 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 68 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 69 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 70 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 71 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 72 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 73 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 74 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 75 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 76 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 77 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 78 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 79 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 80 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 81 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 82 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 83 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 84 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 85 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 86 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 87 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 88 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 89 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 90 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 91 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 92 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 93 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 94 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 95 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 96 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 97 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 98 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 99 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 100 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 101 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 102 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 103 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 104 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 105 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 106 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 107 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 108 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 109 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 110 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 111 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 112 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 113 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 114 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 115 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 116 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 117 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 118 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 119 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 120 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 121 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 122 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 123 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 124 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 125 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 126 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 127 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 128 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 129 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 130 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 131 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 132 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 133 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 134 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 135 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 136 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 137 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 138 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 139 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 140 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 141 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 142 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 143 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 144 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 145 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 146 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 147 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 148 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 149 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 150 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 151 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 152 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 153 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 154 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 155 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 156 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 157 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 158 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 159 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 160 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 161 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 162 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 163 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 164 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 165 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 166 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 167 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 168 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 169 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 170 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 171 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 172 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 173 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 174 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 175 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 176 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 177 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 178 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 179 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 180 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 181 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 182 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 183 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 184 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 185 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 186 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 187 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 188 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 189 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 190 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 191 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 192 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 193 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 194 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 195 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 196 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 197 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 198 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 199 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 200 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 201 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 202 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 203 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 204 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 205 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 206 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 207 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 208 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 209 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 210 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 211 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 212 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 213 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 214 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 215 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 216 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 217 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 218 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
