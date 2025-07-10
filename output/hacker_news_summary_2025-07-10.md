# Hacker News 热门文章摘要 (2025-07-10)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 衡量人工智能对资深开源开发者生产力的影响

**原文标题**: Measuring the Impact of AI on Experienced Open-Source Developer Productivity

**原文链接**: [https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

本文发表于2025年7月10日，重点研究2025年初发布的人工智能工具对资深开源开发者生产力的影响。它调查了这些新的人工智能工具如何影响参与开源项目的经验丰富的开发者。其核心目标很可能是量化生产力的变化——开发者是否在人工智能的帮助下编写了更多代码、更快地修复了错误，或者更有效地进行了协作？

该研究可能会探讨人工智能可能影响的开发者工作流程的各个方面，例如：代码生成、代码补全、调试辅助、文档创建、代码审查流程和项目管理任务。它也可能深入研究正在使用的人工智能工具的类型，考察特定工具或方法是否比其他工具或方法更有益。

最终，该研究旨在提供具体的数据和见解，了解2025年初的人工智能技术是否以及在多大程度上改变了开源开发的格局，特别是对于经验丰富的贡献者而言。它正在衡量这些工具在增强或阻碍他们现有技能和工作流程方面的有效性。

---

## 2. Gemini 2.5 擅长边界框吗？

**原文标题**: Is Gemini 2.5 good at bounding boxes?

**原文链接**: [https://simedw.com/2025/07/10/gemini-bounding-boxes/](https://simedw.com/2025/07/10/gemini-bounding-boxes/)

本文评估了 Gemini 2.5 Pro 在 MS-COCO 数据集上的目标检测能力，并将其性能与已建立的 CNN 模型进行了比较。作者的目标是探索多模态大型语言模型 (MLLM) 在目标检测中取代传统 CNN 的潜力，从而消除对大量数据集收集和标注的需求。

作者使用了详细的提示，包括 MS-COCO 类别的列表，并请求具有边界框、置信度分数和掩码的特定 JSON 输出格式。 实验使用了不同版本的 Gemini（Pro、Flash、Flash-Lite），改变了“思考预算”（token 限制）以及结构化/非结构化输出格式。

使用的主要指标是平均精度均值 (mAP)，它衡量边界框预测的准确性。 结果表明，Gemini 2.5 Pro 的性能与 Yolo v3 (2018 年) 相当，使用结构化输出实现了约 0.34 mAP。 增加思考预算通常会降低性能。 包含掩码输出会导致问题，从而导致无限循环和不完整的测试。

作者的结论是，虽然 CNN 仍然更快且更可预测，但 Gemini 在开放集任务中的多功能性和性能是有希望的。 尽管在 mAP 方面没有超过最先进的 CNN，但 Gemini 2.5 Pro 在没有明确在 MS-COCO 数据集上进行训练的情况下，表现出了不错的对象检测能力，这表明 MLLM 在计算机视觉任务中具有潜力。 作者计划将 Gemini 集成到未来的副项目中。

---

## 3. Flix – 一种强大的面向效果的编程语言

**原文标题**: Flix – A powerful effect-oriented programming language

**原文链接**: [https://flix.dev/](https://flix.dev/)

本文介绍了一种名为Flix的编程语言，该语言被描述为一种强大的、面向效果的语言。虽然文章内容简略，仅呈现标题“Flix | The Flix Programming Language”以及一条表明需要JavaScript才能运行应用程序的消息，但其本质是Flix是一种编程语言。根据标题，我们可以推断它强调函数式编程原则，并旨在有效地管理副作用。由于提供的摘录缺乏详细信息，因此无法提供对其特性、优势或目标用例的更深入总结。 主要内容是Flix编程语言的存在及其自称的对面向效果编程的关注。

---

## 4. 图形线性代数

**原文标题**: Graphical Linear Algebra

**原文链接**: [https://graphicallinearalgebra.net/](https://graphicallinearalgebra.net/)

图形线性代数

这是一个博客，记录了使用图表探索线性代数的进行中项目。该博客旨在通过视觉表示连接算术、几何和代数，突出这种方法的研究潜力和应用。

内容组织成几个主题部分：

*   **引言**: 建立项目的基础和动机。
*   **加法和复制**: 探索基本代数运算及其图解解释。
*   **矩阵和PROPs**: 将图表与矩阵相关联，并介绍PROPs（积和置换范畴）作为框架。
*   **整数和关系**: 将框架扩展到整数矩阵和关系。
*   **分数和空间**: 通过图解视角处理分数、零除、线性关系和子空间。
*   **冗余**: 探讨图解线性代数中的冗余。
*   **插曲**: 讨论弦图和资源敏感语法。
*   **序列和信号流图**: 将概念应用于序列和信号流图。
*   **无序**: 尚未整合到主要结构中的主题。
*   **贡献**: 收录其他研究人员的贡献。
*   **跑题**: 包含关于无关主题的博客文章。

该博客还宣传了2018年ACT应用范畴论研究学校，并呼吁对该领域感兴趣的博士生。 它鼓励通过翻译进行协作，并重点介绍相关的研讨会和会议。

---

## 5. 通过180万条 Hacker News 标题分析数据库趋势

**原文标题**: Analyzing database trends through 1.8M Hacker News headlines

**原文链接**: [https://camelai.com/blog/hn-database-hype/](https://camelai.com/blog/hn-database-hype/)

本文基于2007年2月至2025年6月期间的180万条 Hacker News 标题，分析了数据库发展趋势。利用 camelAI 和 ClickHouse 数据库，识别数据库流行度和讨论趋势。

分析显示，PostgreSQL 一直保持增长，并在近期的讨论中占据主导地位。MySQL 在早期很突出，但已趋于平稳。MongoDB 在 2013 年左右达到顶峰后有所下降，这可能是因为 SQL 数据库整合了 JSON 支持。ClickHouse 和 DuckDB 正经历快速增长，这得益于分析领域的复兴。Redis 和 SQLite 的提及率保持稳定，反映了它们作为基础设施组件的重要性。

分析还识别出增长最快的数据库：DuckDB、ClickHouse 和 Supabase。虽然 PostgreSQL 的同比略有下降，但其长期增长仍然强劲。DynamoDB、BigQuery 和 Redshift 等云原生 SaaS 数据库在讨论中的份额正在下降。

MongoDB、MySQL、DynamoDB、BigQuery 和 Redshift 等数据库的标题提及量较峰值时期有所下降，这归因于成熟、开源竞争（Postgres 扩展和湖仓一体）以及讨论主题转向成本、锁定和无服务器架构。

主要结论是，开源数据库正在推动大部分新讨论，以分析为中心的存储越来越受欢迎，持续改进胜过炒作周期，专有云数据库正在失去吸引力。作者建议进一步分析，包括识别作为替代或替换方案提及的数据库，分析正面与负面标题，并将向量数据库的提及与传统数据库进行比较。

---

## 6. 230万美元桥梁包含90度转弯，七名工程师停职

**原文标题**: Seven Engineers Suspended After $2.3M Bridge Includes 90-Degree Turn

**原文链接**: [https://www.vice.com/en/article/7-engineers-suspended-after-2-3-million-bridge-includes-bizarre-90-degree-turn/](https://www.vice.com/en/article/7-engineers-suspended-after-2-3-million-bridge-includes-bizarre-90-degree-turn/)

印度博帕尔耗资230万美元新建桥梁因突兀的90度转弯引发争议。这座旨在缓解每日30万通勤者交通拥堵的桥梁，反而因其不切实际的设计而备受嘲讽和担忧。

这座怪异的转弯位于高架道路的中途，促使首席部长莫汉·亚达夫立即采取行动，停职了包括两名总工程师在内的七名工程师。一名退休的副工程师也面临部门调查，涉事的建筑和设计公司已被列入黑名单。

该项目坎坷的历史揭示了七年间因公共工程部（PWD）和铁路部门在土地使用方面的分歧而多次修改设计。最初2018年的设计方案具有更易于管理的45度倾斜角，但遭到铁路部门的拒绝。随后的设计试图同时兼顾铁路用地和一条新的地铁线路，最终导致了令人尴尬的90度角。

总工程师VD Verma为该设计辩护，称土地空间有限以及靠近地铁站是制约因素。然而，批评人士认为不应该批准这种急转弯。甚至铁路部门后来也承认，最终设计既不实用也不安全。

当局现在正在考虑购买额外的土地来纠正转弯，这将导致进一步的成本和延误。这座有缺陷的桥梁深刻地提醒人们，官僚内讧、设计妥协以及糟糕的几何设计可能导致重大政治影响。

---

## 7. Perplexity 推出 AI 驱动的网页浏览器 Comet

**原文标题**: Perplexity launches Comet, an AI-powered web browser

**原文链接**: [https://techcrunch.com/2025/07/09/perplexity-launches-comet-an-ai-powered-web-browser/](https://techcrunch.com/2025/07/09/perplexity-launches-comet-an-ai-powered-web-browser/)

Perplexity推出Comet浏览器，挑战谷歌搜索。

---

## 8. 展示HN: Typeform太贵了，所以我自己做了表单

**原文标题**: Show HN: Typeform was too expensive so I built my own forms

**原文链接**: [https://www.ikiform.com/](https://www.ikiform.com/)

Ikiform：经济实惠的开源表单解决方案，是Typeform和Google Forms的替代品，专注于轻松创建美观且交互式的表单。主要功能包括基于文本描述生成表单的AI表单构建器、直观的拖放式表单构建器，以及用于提供见解的AI驱动型分析。

该平台提供简单、透明的定价模式，从免费层级开始，升级可获得更多功能。早期用户可享受一次性59美元的折扣。核心功能包括无限提交、AI表单构建器、导出回复和优先支持。移动构建器和高级分析等高级功能包含在付费层级中。一些功能被标记为“即将推出”，包括团队协作、自定义域名、标记回复、集成以及更高级的表单逻辑和数据处理能力。

常见问题解答部分解决了关于Ikiform的用途、优势、表单类型、AI辅助、数据安全、开源性质、功能建议、数据存储、数据删除策略和数据所有权等常见问题。文章最后以行动号召结束，鼓励用户使用Ikiform创建他们的第一个表单。

---

## 9. 在 Rust 中优化数学表达式解析器

**原文标题**: Optimizing a Math Expression Parser in Rust

**原文链接**: [https://rpallas.xyz/math-parser/](https://rpallas.xyz/math-parser/)

本文详细介绍了用Rust编写的数学表达式解析器的优化过程。最初的基准实现处理一个1.5GB的文件耗时43.1秒，作者通过几个关键优化系统地提高了性能。

**优化1** 消除了分词阶段不必要的`Vec<Token>`分配，转而使用惰性迭代器，从而显著提高了速度，从43.1秒降至6.45秒。

**优化2** 侧重于零分配，直接从输入字节(`&[u8]`)解析，而不是使用字符串，避免了`split_whitespace`生成的临时字符串切片。这进一步将运行时间缩短至3.68秒。

**优化3** 移除了`Peekable`的使用，重构了解析算法，使其直接与普通迭代器配合使用。这避免了窥视token的开销，实现了新的运行时间3.21秒。

后续计划进行涉及多线程、SIMD和内存映射I/O的进一步优化，但在提供的文本中未充分讨论。本文强调了通过仔细识别和解决代码中的瓶颈所取得的显著性能提升，展示了内存效率和算法选择在优化Rust应用程序中的重要性。

---

## 10. 苏格兰海岸水下涡轮机运转六年实现突破

**原文标题**: Underwater turbine spinning for 6 years off Scotland's coast is a breakthrough

**原文链接**: [https://apnews.com/article/tidal-energy-turbine-marine-meygen-scotland-ffff3a7082205b33b612a1417e1ec6d6](https://apnews.com/article/tidal-energy-turbine-marine-meygen-scotland-ffff3a7082205b33b612a1417e1ec6d6)

美联社文章《苏格兰海岸运行六年的水下涡轮机是一项突破》摘要：

该文章重点介绍了苏格兰海岸一个水下潮汐涡轮机成功运行了六年。这代表了潮汐能领域的一项重大突破，证明了该技术的长期可行性和可靠性。该涡轮机是 MeyGen 项目的一部分，已经证明了其承受恶劣海洋环境并持续发电的能力。

这一成功非常重要，因为潮汐能提供了一种可预测且稳定的可再生能源，不同于依赖天气状况的风能和太阳能。MeyGen 项目表明，潮汐能有潜力为可再生能源组合做出重大贡献，并有助于减少对化石燃料的依赖。

文章可能强调了在这种严苛环境下运营的挑战，包括强劲的水流、腐蚀性的盐水以及对耐用材料和强大工程的需求。涡轮机持续运行如此之久的事实验证了该技术的设计和建造。

虽然文章可能承认潮汐能仍然是一种相对昂贵的可再生能源，但它表明像 MeyGen 这样的项目的长期成功对于吸引投资和扩大技术规模以使其更具成本竞争力至关重要。 成功的运营正在为世界各地潮汐能项目的进一步开发和部署铺平道路。

---

## 11. 如何证明错误声明：针对Fiat-Shamir的实用攻击

**原文标题**: How to prove false statements: Practical attacks on Fiat-Shamir

**原文链接**: [https://www.quantamagazine.org/computer-scientists-figure-out-how-to-prove-lies-20250709/](https://www.quantamagazine.org/computer-scientists-figure-out-how-to-prove-lies-20250709/)

本文讨论了Fiat-Shamir转换中发现的一个新漏洞。Fiat-Shamir转换是一种广泛使用的技术，用于在密码学中创建非交互式证明。由包括Dmitry Khovratovich、Ron Rothblum和Lev Soukhanov在内的研究人员开发的这一攻击，展示了一种欺骗证明系统以证明虚假陈述的方法，即使这些系统在随机预言模型下被认为是安全的（假设哈希函数表现得像真正的随机源）。

Fiat-Shamir转换对于验证各种应用（包括区块链和云计算）中的计算至关重要，它通过将交互式证明转换为非交互式证明来实现。该漏洞源于现实世界的哈希函数并非完全随机，这使得攻击者可以制作恶意程序，利用哈希过程生成虚假证明。

具体来说，研究人员针对的是基于GKR协议的Fiat-Shamir证明系统。他们创建了一个恶意程序，该程序在以其自身的哈希作为输入时，可以计算用于验证的随机挑战，并操纵其内部运作以通过检查，即使使用不正确的数据也是如此。

这一发现挑战了长期以来关于Fiat-Shamir安全性的假设，并引发了人们对依赖它的系统安全性的担忧，尤其是在区块链应用中，那里涉及巨额资金。虽然已经提出了针对Fiat-Shamir的补丁和修改以缓解攻击，但这一发现需要对随机预言模型进行更广泛的重新评估，并更深入地了解密码学实现中潜在的漏洞。

---

## 12. 微型机器人无需挖掘即可检测并修复水管泄漏。

**原文标题**: Mini robots detect and fix water pipe leaks without digging

**原文链接**: [https://www.foxnews.com/tech/mini-robots-detect-fix-water-pipe-leaks-without-digging](https://www.foxnews.com/tech/mini-robots-detect-fix-water-pipe-leaks-without-digging)

文章探讨了英国谢菲尔德大学研究人员开发的“管道机器人（Pipebots）”。这些小型机器人旨在管道内行进，检测并可能修复泄漏，而无需进行破坏性和昂贵的挖掘。

英国老化的供水基础设施，其中许多是维多利亚时代的管道，因泄漏而遭受严重的水流失，每年造成数十亿美元的损失，并因街道维修而造成重大干扰。管道机器人配备了声学传感器、摄像头和坚固的轮子，可以在管道中导航，识别裂缝，并将数据传输回工程师，以便进行有针对性的维修。

该项目是英国水管理现代化的更广泛努力的一部分。它得到了OFWAT的支持，包括专注于检查加压废水管道和开发“非开挖泄漏修复”方法的项目。欧盟资助的Pipeon项目也在开发用于自主下水道检查的AI驱动机器人。

Kurt "CyberGuy" Knutsson 强调了管道机器人使全球水系统维护更加高效、经济和清洁的潜力，尤其是在资源有限且基础设施老化的发展中国家。他强调了它们在节约用水工作中的重要性。

---

## 13. Diffsitter – 基于 Tree-sitter 的 AST 差异工具，用于获取有意义的语义差异

**原文标题**: Diffsitter – A Tree-sitter based AST difftool to get meaningful semantic diffs

**原文链接**: [https://github.com/afnanenayet/diffsitter](https://github.com/afnanenayet/diffsitter)

Difsitter：通过比较抽象语法树生成语义化差异的命令行工具（开发中）。它忽略格式差异，利用 tree-sitter 项目进行解析，目前支持 Bash、C#、C++、CSS、Go、Java、OCaml、PHP、Python、Ruby、Rust、TypeScript/TSX 和 HCL 等语言。

与传统的 `diff` 不同，Difsitter 专注于语义变更而非逐行比较。它允许通过配置文件过滤差异中考虑的 AST 节点，从而精确控制构成有意义的变更。

安装选项包括从 Github 发布版获取预构建的二进制文件，使用 Cargo 从源代码构建，使用 Homebrew、Arch Linux AUR、Alpine Linux 仓库，或通过 Docker 镜像。 使用方法包括运行带有文件路径和可选配置的 `diffsitter` 命令。它通过 `.git/config` 与 Git 集成，在 Git 工作流程中提供语义化差异体验。可以为各种 shell 生成 shell 补全脚本。

可以使用配置文件（默认位置：`$XDG_HOME/.config/diffsitter/config.json5`）配置 Difsitter，以指定文件关联和格式。该工具还支持 tree-sitter 语法动态链接。欢迎通过 Github 问题和讨论提出问题、功能请求和建议。该项目正在积极寻求贡献。

---

## 14. 红帽技术写作风格指南

**原文标题**: Red Hat Technical Writing Style Guide

**原文链接**: [https://stylepedia.net/style/](https://stylepedia.net/style/)

本文档是红帽技术写作风格指南，7.1版，版权所有 2025 年。它是红帽培训、认证内容以及大多数技术文档（不包括遵循补充风格指南的产品文档）的官方风格指南。

本指南涵盖广泛的主题，包括：

*   **核心写作原则：** 语法、标点、句子结构、词语用法和风格惯例。
*   **设计：** 整体出版设计、标题样式、用户界面 (UI) 文档记录，以及缩写词、首字母缩略词和品牌名称的正确用法。
*   **语言：** 避免误导性语言、俚语和推广包容性语言。
*   **清晰性和简洁性：** 有效的句子结构、列表格式和简洁的写作实践。
*   **交叉引用：** 指导文档中交叉引用的有效使用。
*   **词语用法词典：** 提供关于个别词语和短语的具体指导。

本文档强调可访问性和全球受众。欢迎来自社区的贡献。本指南会定期更新，最近的版本包括针对“人工智能 (AI)”、“即代码”、“边缘”等术语的新增或更新条目。最近的更新还包括对标点符号、对象命名和使用真实用户名的澄清。它还删除了冗余内容，并确保该指南与技术写作最佳实践保持同步。

---

## 15. 自动将 Haskell 库打包为 Swift 二进制 XCFramework

**原文标题**: Automatically Packaging a Haskell Library as a Swift Binary XCFramework

**原文链接**: [https://alt-romes.github.io/posts/2025-07-05-packaging-a-haskell-library-as-a-swift-binary-xcframework.html](https://alt-romes.github.io/posts/2025-07-05-packaging-a-haskell-library-as-a-swift-binary-xcframework.html)

本文介绍 `xcframework`，一个 Haskell 库，它可自动化将 Haskell 库打包为 Swift 二进制 XCFrameworks 的过程，以便无缝集成到 Swift 应用程序中。作者强调了之前使用 Xcode 的更手动方法的问题，并提出了一个更清晰、更稳健的解决方案。

要点：

*   **问题：** 直接使用 Xcode 将 Haskell 库集成到 Swift 项目中可能很复杂、容易出错，并导致重新编译问题。
*   **解决方案：** 创建一个独立的 Swift Package 包装 Haskell 库，该库无需 Xcode 即可构建。
*   **`xcframework` 库：** 此库可自动化使用 Cabal 构建 Haskell 库以及使用 Cabal SetupHooks 从 Haskell artifacts 创建 Swift 包。
*   **XCFrameworks：** Apple 的 XCFramework bundles 允许使用多平台二进制框架，使 Swift 项目可以依赖于二进制 artifact 和头文件。
*   **`xcframework` bundles 包含：** 外部共享库 (.dylib)、外部导出头文件、RTS 头文件以及 .modulemap。
*   **安装与使用：** 本文提供了有关使用 Cabal 安装 `xcframework`、将生成的 `.xcframework` 添加到 Xcode 项目以及在 Swift 中导入 Haskell 函数的说明。 它还演示了如何使用 swift build 创建独立的 Swift 包。
*   **

---

## 16. FOKS：联邦开放密钥服务

**原文标题**: FOKS: The Federated Open Key Service

**原文链接**: [https://foks.pub/](https://foks.pub/)

FOKS (联邦开放密钥服务) 是一个全新的开源项目，提供端到端、后量子加密的 Git 托管和键值存储。它旨在为长期存在的数据提供卓越的安全性和隐私保护，并通过其联邦式设计解决对供应商锁定的担忧。用户可以托管自己的 FOKS 服务器或使用托管服务。

主要功能包括：

*   **端到端加密:** 数据在客户端加密，确保服务器端泄露不会暴露敏感信息。
*   **后量子安全:** 使用可抵抗量子攻击的现代密码学。
*   **联邦:** 允许用户运行自己的服务器，并在联邦边界上与其他人交互。
*   **团队管理:** 促进团队创建、成员管理和角色分配，即使跨联邦实例。
*   **设备管理:** 支持设备注册、访问管理和撤销，包括 YubiKey 集成以增强安全性。
*   **密钥层级:** 采用多层密钥结构（设备密钥、每用户密钥、每团队密钥）来管理访问并启用密钥轮换。
*   **签名链和 Merkle 树:** 通过可验证的签名和一致的世界观，确保数据完整性并防止服务器篡改。

FOKS 的设计考虑了安全性、隐私性和开放性。它作为一个充满激情的项目启动，未来可能会通过提供托管服务来获得资金。提供了适用于 macOS、Linux 和 Windows 的安装说明。未来的路线图项目包括移动应用程序、Web UI 和基于同步的文件系统。

---

## 17. 树木借阅

**原文标题**: Tree Borrows

**原文链接**: [https://plf.inf.ethz.ch/research/pldi25-tree-borrows.html](https://plf.inf.ethz.ch/research/pldi25-tree-borrows.html)

本文介绍了 Tree Borrows，一种用于定义 Rust 中不安全代码行为的新模型。 Rust 基于所有权的类型系统确保了内存安全和数据竞争自由，但不安全代码会绕过这些保证，从而可能阻碍编译器依赖指针别名假设进行的优化。 之前的工作 Stacked Borrows 定义了“行为良好”的不安全代码的规则，以实现这些优化，但它被发现过于严格，拒绝了许多合法的 Rust 不安全模式，并且未能考虑借用检查器最近的进展。

Tree Borrows 通过用树结构替换堆栈结构来改进 Stacked Borrows。 这种改变使该模型能够接受更广泛的有效不安全代码，同时保持安全保证。 针对 30,000 个最流行的 Rust 库进行基准测试，Tree Borrows 比 Stacked Borrows 拒绝的测试用例明显更少（减少了 54%）。

作者证明（使用 Rocq），Tree Borrows 保留了 Stacked Borrows 启用的大部分优化，并且至关重要的是，解锁了新的优化，例如读-读重排序。 这种改进使编译器能够更积极地进行优化，而无需担心被 Rust 不安全代码中的常见模式所破坏。 这项工作在 PLDI'25 上获得了杰出论文奖。 提供了论文、演讲录音、工件和源代码的链接。

---

## 18. MCP-B：AI浏览器自动化协议

**原文标题**: MCP-B: A Protocol for AI Browser Automation

**原文链接**: [https://mcp-b.ai/](https://mcp-b.ai/)

“MCP-B：一种用于AI浏览器自动化的协议”一文介绍了MCP-B（浏览器模型上下文协议），该协议旨在促进AI驱动的浏览器自动化。本质上，MCP-B旨在标准化AI代理与Web浏览器交互的方式，使AI模型更容易理解和有效地操作Web内容。

MCP-B没有仅仅依赖于传统的CSS选择器或XPath等方法（这些方法可能很脆弱且对网站更改敏感），而是侧重于为AI提供更全面的浏览器状态“上下文”。此上下文包括有关DOM（文档对象模型）、视觉布局、文本内容，甚至可能包括用户交互历史的信息。

通过提供这种更丰富、更结构化的数据，MCP-B使AI代理能够：

*   **更好地理解Web元素的语义含义：** AI可以根据其目的和上下文，而不仅仅是视觉外观，来识别按钮、表单和其他交互式元素。
*   **执行更可靠的自动化：** 自动化脚本变得不易受到网站更新的影响，因为AI可以基于语义理解进行调整，而不是依赖于特定的CSS类或ID。
*   **促进更复杂的任务：** AI可以处理更复杂的工作流程，例如填写多步骤表单、导航复杂菜单以及从网站提取特定信息。
*   **增强模型训练：** MCP-B提供的结构化浏览器上下文可用于更有效地训练AI模型，从而提高在浏览器自动化任务中的性能。

从本质上讲，MCP-B旨在弥合人类理解和与Web浏览器交互的方式与AI代理如何实现相同水平的理解和控制之间的差距。它承诺了一种更强大、适应性更强且更智能的浏览器自动化方法。

---

## 19. 加拿大特色词汇类型学

**原文标题**: A Typology of Canadianisms

**原文链接**: [https://dchp.arts.ubc.ca/how-to-use](https://dchp.arts.ubc.ca/how-to-use)

《加拿大历史词典》(DCHP-3)将加拿大英语词汇分为六种类型，外加一个“非加拿大”类别。 这些类型根据词语的起源、用法以及在加拿大的文化意义对其进行分类。

六种加拿大特色词汇类型包括：

*   **类型 1（起源）：** 在加拿大创造的词语（例如，garburator）。
*   **类型 2（保留）：** 在加拿大英语中从其他变体保留下来的词语（例如，pencil crayon）。
*   **类型 3（语义变化）：** 在加拿大英语中具有不同含义的词语（例如，toque）。
*   **类型 4（文化意义）：** 深深扎根于加拿大认同中的词语（例如，goalie mask）。
*   **类型 5（频率）：** 在加拿大比其他地方更频繁使用的词语（例如，washroom）。
*   **类型 6（纪念）：** 代表加拿大历史上阴暗面的词语（例如，residential school）。

该词典的条目结构以DCHP-2为基础，提供含义、来自加拿大来源的引文以及参考资料。 频率图表用于支持类型5的分类，使用标准化的网络搜索（使用“the”）来比较不同地区之间的词语使用情况。 该词典还采用专门的搜索词和布尔运算符来隔离特定的词语含义，以进行准确的分析。

DCHP-3包含一个全面的领域标签列表，以按主题进一步对词语进行分类。 新版本中，这些标签已从38个扩展到55个。 此外，还有区域和社会标签。

DCHP-3可以作为免费的数字资源使用，但其内容受版权保护，未经许可不得复制、修改或创作衍生作品。

---

## 20. 雷鸟 140 “日蚀”

**原文标题**: Thunderbird 140 “Eclipse”

**原文链接**: [https://blog.thunderbird.net/2025/07/welcome-to-thunderbird-140-eclipse/](https://blog.thunderbird.net/2025/07/welcome-to-thunderbird-140-eclipse/)

Thunderbird 140 “Eclipse” 最新扩展支持版 (ESR) 现已发布。它基于 Thunderbird 128 “Nebula”，并包含了月度发布渠道的功能和改进，专注于通过自适应暗色消息和改进的可视化控件来增强电子邮件体验。

主要功能包括：

*   **暗色消息模式：** 自动将消息调整为暗色模式，并提供切换开关方便调整。
*   **外观设置：** 单击即可自定义消息列表布局（卡片或表格视图）和排序/线程选项。
*   **原生操作系统通知：** 利用 Windows、Linux 和 Mac OS 通知，实现更快速的操作，如删除或存档。
*   **账户中心：** 简化了添加电子邮件、地址簿和日历的流程。
*   **手动文件夹排序：** 通过拖放操作自定义文件夹顺序。
*   **实验性 Exchange 支持：** 通过首选项设置原生设置 Microsoft Exchange 账户。
*   **移动设备导出：** 生成二维码，用于将账户设置传输到适用于 Android 的 Thunderbird。
*   **表格视图水平滚动：** 允许在消息列表中水平滚动以显示表格数据。

此版本还包含数千个错误修复和性能改进。用户可以切换到常规发布渠道以获取每月更新。Thunderbird 140 适用于 Windows、Linux 和 MacOS。自动更新正在逐步推出，但可以通过“帮助 > 关于”或直接从 thunderbird.net 下载来手动升级，选择 ESR 渠道。使用 snap 或 flatpak 的 Linux 用户和 Windows Store 用户预计将在几周内收到更新。对于 32 位 MAPI 用户，除非使用撰写窗口，否则存在已知的密码提示问题。

---

## 21. Show HN: CXXStateTree – 一款现代 C++ 分层状态机库

**原文标题**: Show HN: CXXStateTree – A modern C++ library for hierarchical state machines

**原文链接**: [https://github.com/ZigRazor/CXXStateTree](https://github.com/ZigRazor/CXXStateTree)

CXXStateTree：用于创建分层状态机的现代C++20库。它具有使用基于lambda的DSL的流畅构建器API，提供快速的运行时性能，无需堆分配。该库支持用于转换的可选守卫和动作，并基于事件驱动的状态转换进行操作。

主要特点包括：

*   **简洁的DSL：** 方便状态机定义。
*   **性能：** 旨在提高速度和效率。
*   **灵活性：** 允许在状态转换期间使用守卫和动作。
*   **可测试性：** 与Google Test集成。
*   **可扩展性：** 专为嵌套状态等功能而设计。

提供的示例演示了使用`send()`在“空闲”和“运行”状态之间的基本状态转换。

该项目使用CMake进行构建，支持代码覆盖率分析，并自动下载GoogleTest作为依赖项。它采用MPL2.0许可。

未来计划的功能包括嵌套状态支持、用于可视化的DOT/Graphviz导出，以及潜在的协程/异步支持。欢迎贡献、问题和功能建议。该库正在通过里程碑推进，基本功能、守卫/动作、嵌套状态和graphviz导出已经完成，协程支持和全面覆盖计划在后续版本中实现。

---

## 22. Grok 4 发布 [视频]

**原文标题**: Grok 4 Launch [video]

**原文链接**: [https://twitter.com/xai/status/1943158495588815072](https://twitter.com/xai/status/1943158495588815072)

由于您的浏览器禁用了 JavaScript，您无法查看所需内容（“Grok 4 发布 [视频]”）。请启用 JavaScript 或切换到受支持的浏览器以使用此平台。X 帮助中心、服务条款、隐私政策、Cookie 政策、版本说明、广告信息。 © 2025 X Corp.

---

## 23. Show HN：用于搜索和下载 Anna's Archive 文档的 MCP 服务器

**原文标题**: Show HN: MCP server for searching and downloading documents from Anna's Archive

**原文链接**: [https://github.com/iosifache/annas-mcp](https://github.com/iosifache/annas-mcp)

这个 "Show HN" 帖子介绍了一个 MCP 服务器和 CLI 工具，旨在从 Anna's Archive 搜索和下载文档。该工具通过 Anna's Archive 的 API 访问，据作者称，其目的是检索许可式授权或公共领域的文档，并强烈敦促用户尊重版权法和知识产权。

该软件提供两个主要操作：基于关键词搜索 Anna's Archive，以及下载通过搜索识别出的特定文档。

要使用 CLI 工具，用户需要一个 Anna's Archive API 密钥（通过捐赠获得）。将其用作 MCP 服务器需要一个 MCP 客户端（如 Claude Desktop），并且需要设置 `ANNAS_SECRET_KEY` (API 密钥) 和 `ANNAS_DOWNLOAD_PATH` 环境变量。

该帖子包含设置说明，强调从 GitHub Releases 下载适当的二进制文件。提供了一个 Claude Desktop 的配置示例，演示了如何将该工具集成为 MCP 服务器。该帖子还提供了一个演示，展示了如何使用服务器和 CLI 工具。

---

## 24. 威廉征服王的“中世纪大数据”项目作者揭晓

**原文标题**: Author of William the Conqueror's 'Medieval Big Data' Project Revealed

**原文链接**: [https://www.ox.ac.uk/news/2025-07-02-author-william-conqueror-s-medieval-big-data-project-revealed](https://www.ox.ac.uk/news/2025-07-02-author-william-conqueror-s-medieval-big-data-project-revealed)

牛津大学研究将《末日审判书》解读为“中世纪大数据”项目

---

## 25. Show HN: FlopperZiro – 自制开源的Flipper Zero克隆

**原文标题**: Show HN: FlopperZiro – A DIY open-source Flipper Zero clone

**原文链接**: [https://github.com/lraton/FlopperZiro](https://github.com/lraton/FlopperZiro)

Flopper Ziro是一个DIY、开源的Flipper Zero克隆项目，旨在成为一个使用Arduino IDE实现的有趣且廉价的项目。明确声明它不是专业的替代品。该项目利用了STM32-L432KC微控制器、FS1000a/RXB12用于RF、PN532用于RFID/NFC（计划测试PN7150）、红外LED/接收器、SSD1306 OLED显示屏、TF卡存储屏蔽以及其他常用组件等组件。

主要功能包括RubberDucky功能、RFID/NFC（开发中）、红外读取/模拟、射频读取/模拟、SD卡保存/加载、电池百分比和SD卡剩余内存百分比。所有功能都可以通过Arduino IDE进行编程。提供3D打印外壳。

该项目正在积极开发中，待办事项包括解决显示屏的SD卡问题、创建SD卡菜单和保存/加载功能、修复SD列表中的错误、完成射频扫描仪/发送器、改进菜单、修复红外数据显示中的错误、实现RFID读取和模拟、设计PCB以及添加文档。

---

## 26. 太阳能已开始改变世界能源系统

**原文标题**: Solar power has begun to transform the world’s energy system

**原文链接**: [https://www.newyorker.com/news/annals-of-a-warming-planet/46-billion-years-on-the-sun-is-having-a-moment](https://www.newyorker.com/news/annals-of-a-warming-planet/46-billion-years-on-the-sun-is-having-a-moment)

太阳能正迅速改变世界能源系统，从“替代”能源走向主流、高性价比之选。作者强调了全球太阳能板安装量的指数级增长，世界正以加速的速度增加兆瓦级太阳能发电。关键数据显示，可再生能源在美国、加州和德州满足新增电力需求方面的主导地位日益增强。

中国是主导力量，安装了全球一半以上的可再生能源，并出口太阳能板和电池。这对贸易联系紧密的国家产生了影响，导致可再生能源激增。南美洲甚至像波兰这样历史上依赖煤炭的国家也在经历向太阳能和风能的转变。

储能成本，特别是电池成本的降低，是实现更可靠的可再生能源供应的关键因素。作者将太阳能板的“功”与化石燃料的“热能”的低效率进行了对比，突出了电动汽车和热泵的优势。

尽管取得了进展，但文章承认美国出现了对清洁能源的抵制，例如试图废除太阳能板和电动汽车的税收抵免。然而，作者认为这是对可再生能源颠覆性潜力的认可。1954年光伏电池的发明标志着这一变革时代的开始，它受到成本降低和气候变化意识日益增强的推动。

---

## 27. 美国派对文化的衰落

**原文标题**: The death of partying in the USA

**原文链接**: [https://www.derekthompson.org/p/the-death-of-partying-in-the-usaand](https://www.derekthompson.org/p/the-death-of-partying-in-the-usaand)

德里克·汤普森的文章《美国派对文化的消亡——以及为何重要》探讨了过去二十年美国社交聚会显著减少的现象。该文章引用了美国时间使用调查（ATUS）的数据，显示15-24岁的年轻人参加派对的时间比2003年减少了70%，而美国人整体的社交日程也减少了一半。这种下降是日益孤独的更广泛趋势的一部分，汤普森称之为“反社交世纪”。

作者追溯了美国社交的历史背景，指出自20世纪70年代以来出现下滑。他将派对文化的消亡归因于几个因素：双职工家庭的兴起，特别是女性进入职场后，男性并没有取代她们成为社交活动组织者的角色；更加密集的育儿方式；以及屏幕和数字技术的普遍影响。虽然智能手机将人们与内部圈子和在线部落联系起来，但它们往往以牺牲“中间圈”社区和现实生活互动为代价，培养了虚假的社交关系而非真实的社交关系。文章还指出年轻人饮酒量的下降，这可能导致社交活动的减少。

汤普森最后告诫说，虽然进步和富足是可取的，但它们也可能带来意想不到的代价，例如社交生活的侵蚀以及焦虑的上升和亲密关系的衰退。他认为社会需要注意与技术进步相关的权衡，并优先考虑真正的人际联系。

---

## 28. 研究型大学的起源

**原文标题**: The Origin of the Research University

**原文链接**: [https://asteriskmag.com/issues/10/the-origin-of-the-research-university](https://asteriskmag.com/issues/10/the-origin-of-the-research-university)

克拉拉·科利尔的文章探讨了19世纪德国研究型大学的惊人起源，并将其与大学作为培养牧师、律师和医生等人才的传统教学机构的角色进行了对比。在此转变之前，真正的学术研究发生在大学之外，例如英国皇家学会等机构。

最初功能失调且专注于中世纪课程的德国大学经历了一次重大转变。它们开始将教学与研究相结合，这是受到追求实用性和现代化的愿望所驱动。早期的改革尝试深受重商主义的影响，重商主义侧重于公共管理，旨在通过国家控制以及推广出版以获取名声和吸引学生，而非真正的研究，使大学变得高效并有益于国家。

哥廷根大学成为一个关键角色，率先提出了通过出版记录来奖励学术进步的概念，这一概念由格拉赫·阿道夫·冯·明希豪森倡导。这种对出版的强调，尽管最初是为了简历建设，却为研究文化奠定了基础。文章将“研究”定义为对更广泛的学术对话做出贡献并为进一步调查提供基础的原创学术成果。

伊曼努尔·康德的“Wissenschaft”概念，即“系统知识”，进一步塑造了研究型大学。康德倡导哲学系的独立性，并强调以结构化方式追求真理的重要性，从而促进了一个不仅重视原创学术成果，而且将其制度化的体系的发展。

---

## 29. Jank编程语言

**原文标题**: The jank programming language

**原文链接**: [https://jank-lang.org/](https://jank-lang.org/)

Jank：一种旨在实现原生编译和最小运行时的Clojure方言通用编程语言。它试图将Clojure的交互式开发体验与C++的性能和原生集成能力相结合。

与运行在JVM上的Clojure不同，Jank托管于C++中，并使用基于LLVM的JIT编译器。这使其能够在保留REPL驱动开发优势的同时，实现更接近原生语言的性能。Jank优先考虑与Clojure的强大兼容性，拥抱其代码即数据的理念和强大的宏系统。它仍然是一种函数式优先的语言，并利用Clojure的不可变数据结构。对于需要可变性的情况，Jank提供软件事务内存和一个反应式代理系统，用于可靠的多线程编程。

该语言正在积极开发中，其主要优势在于其弥合Clojure的表达性和交互性与编译语言提供的性能和原生集成能力之间差距的潜力。

---

## 30. 放射性碳定年法揭示拉帕努伊并非如先前认为的那般孤立

**原文标题**: Radiocarbon dating reveals Rapa Nui not as isolated as previously thought

**原文链接**: [https://phys.org/news/2025-06-radiocarbon-dating-reveals-rapa-nui.html](https://phys.org/news/2025-06-radiocarbon-dating-reveals-rapa-nui.html)

本文探讨了新的研究，这些研究挑战了长期以来认为拉帕努伊岛（复活节岛）在最初定居后孤立发展的观点。通过对整个东波利尼西亚的祭祀场所和纪念碑进行放射性碳年代测定和考古分析，Wallin教授和Martinsson-Wallin教授认为，岛屿之间的互动网络更加强大，祭祀思想在双向传播。

该研究确定了祭祀活动的三个阶段。第一阶段与最初的自西向东的迁徙有关，涉及以直立石柱为标志的埋葬和宴饮祭祀。第二阶段见证了“marae”（矩形祭祀场所）的发展。放射性碳年代测定表明，可见祭祀场所的概念起源于拉帕努伊岛，并向西传播回东波利尼西亚中部。最后阶段涉及日益增长的孤立，导致独立发展，以及随着等级社会的演变，在拉帕努伊岛上建造了像摩艾石像这样的巨型建筑。

该研究强调，虽然最初的殖民化是从西向东发生的，但祭祀习俗的发展和传播更为复杂。研究表明，像精心设计的marae的发展这样的创新祭祀习俗，起源于拉帕努伊岛，然后影响了东波利尼西亚的其他岛屿。这挑战了先前认为的单向文化流动观点，并强化了岛屿之间的互动网络在塑造波利尼西亚文化中发挥了重要作用的观点。

---

## 31. 琳达·亚卡里诺离开X

**原文标题**: Linda Yaccarino is leaving X

**原文链接**: [https://www.nytimes.com/2025/07/09/technology/linda-yaccarino-x-steps-down.html](https://www.nytimes.com/2025/07/09/technology/linda-yaccarino-x-steps-down.html)

无法访问文章链接。

---

## 32. Biomni：通用生物医学人工智能体

**原文标题**: Biomni: A General-Purpose Biomedical AI Agent

**原文链接**: [https://github.com/snap-stanford/Biomni](https://github.com/snap-stanford/Biomni)

Biomni：一款通用生物医学人工智能代理，旨在自主执行多样化的研究任务。它利用大型语言模型（LLM）推理、检索增强规划和基于代码的执行，以提高研究效率并为科学家生成可测试的假设。

开始使用时，用户需要使用提供的安装脚本安装Biomni环境，激活环境，并安装Biomni软件包。需要配置Anthropic的API密钥，以及可选的OpenAI的API密钥。设置完成后，用户可以通过`biomni.agent`模块使用自然语言命令与代理交互，执行诸如规划CRISPR筛选、注释scRNA-seq数据或预测化合物的ADMET属性等任务。

Biomni是一项开放科学倡议，欢迎社区贡献，包括新工具、数据集、软件集成、基准和教程。该项目目前正在构建Biomni-E2，这是一个下一代环境，用于协作定义标准生物医学行动的共享库。贡献者可以提交工具/数据库/软件建议，做出重大贡献的人将被邀请作为即将发表的出版物的共同作者。

Biomni的Web界面可在biomni.stanford.edu上访问。该项目有一个发布计划，包括基准、贡献教程和代理基线。此特定版本（A1+E1）已于2025年4月15日冻结，并且与当前的Web平台不同。虽然Biomni本身采用Apache 2.0许可，但各个组件可能具有更严格的许可。

---

## 33. Show HN: Petrichor – 一款免费、开源、离线的 macOS 音乐播放器

**原文标题**: Show HN: Petrichor – a free, open-source, offline music player for macOS

**原文链接**: [https://github.com/kushalpandya/Petrichor](https://github.com/kushalpandya/Petrichor)

Petrichor 是一款免费、开源、离线的 macOS 音乐播放器 (14 或更高版本)，使用 Swift 和 SwiftUI 构建。 它支持多种音频格式 (MP3, M4A, WAV, AAC, AIFF, FLAC) 并提供诸如组织化的音乐库浏览、播放列表创建、文件夹视图、收藏夹固定、快速搜索以及原生 macOS 集成 (菜单栏控制、暗黑模式) 等功能。该应用依赖于音轨元数据。

计划中的功能包括智能播放列表、音频均衡器、更多格式支持 (Opus, OGG)、AirPlay 2、迷你播放器/全屏模式、自动更新以及在线专辑/艺术家信息获取。

该应用扫描用户添加的音乐文件夹，填充一个 SQLite 数据库 (使用 GRDB)，且不更改原始文件。 音轨搜索由 SQLite FTS5 提供支持，播放使用 AVFoundation。 数据库模式包含文件夹、艺术家、专辑、流派、音轨、播放列表和固定项目表。

该项目的动机是作者希望拥有一个现代化的、功能丰富的离线音乐播放器，同时学习 Swift 和 macOS 应用开发。 安装说明包括从 Releases 下载 DMG 并将应用移动到 Applications 文件夹。 构建 DMG 安装程序需要 `xcpretty` 和 `create-dmg`。 该项目采用 MIT 许可证。

---

## 34. 快速三维碰撞检测算法

**原文标题**: A fast 3D collision detection algorithm

**原文链接**: [https://cairno.substack.com/p/improvements-to-the-separating-axis](https://cairno.substack.com/p/improvements-to-the-separating-axis)

无法访问文章链接。

---

## 35. 将副业启动成盈利百万美元的生意

**原文标题**: Bootstrapping a side project into a profitable seven-figure business

**原文链接**: [https://projectionlab.com/blog/we-reached-1m-arr-with-zero-funding](https://projectionlab.com/blog/we-reached-1m-arr-with-zero-funding)

凯尔·诺兰在四年内将金融规划工具ProjectionLab从一个副业发展成一个年收入百万美元的企业。受财务独立运动的启发，他创建了这个工具来满足自己的规划需求。最初，他白天上班，晚上和周末兼职，两头兼顾，非常辛苦。

关键里程碑包括来自Hacker News的早期收入，Mr. Money Mustache的推荐，以及最终辞去日常工作，专注于ProjectionLab。诺兰强调了创业的情感过山车，包括应对停滞不前的月份和订阅取消。

他强调了坚持、不放弃以及与你喜欢的人一起工作的重要性。在独自工作了两年之后，诺兰聘请了Jon Kuipers作为增长和营销合作伙伴。他们还从ProjectionLab用户社区中增加了承包商来处理客户成功。

诺兰的策略包括专注于优秀的产品，保持精简和自筹资金，以及可持续发展。他鼓励有抱负的企业家不断改进他们的想法，即使面对分心和怀疑。他将ProjectionLab的成功归功于小而持续的行动的复利效应，这与美元成本平均法的原则相呼应。

---

## 36. 贿赂还是社区福利？可再生能源的激励措施需要妥善处理

**原文标题**: Bribe or community benefit? Sweeteners for renewables need to be done right

**原文链接**: [https://theconversation.com/bribe-or-community-benefit-sweeteners-smoothing-the-way-for-renewables-projects-need-to-be-done-right-258903](https://theconversation.com/bribe-or-community-benefit-sweeteners-smoothing-the-way-for-renewables-projects-need-to-be-done-right-258903)

本文探讨了可再生能源开发商日益普遍地采用社区利益计划来为新项目铺平道路的做法，并探讨了这些计划可能被视为贿赂而非真正社区支持的潜在风险。

作者概述了三种主要的计划类型：社区基金、实物福利和本地所有权模式，并解释了其预期目的是抵消对当地居民的影响，更公平地分配经济利益，并提高社区接受度。

然而，文章警告说，设计不完善的计划可能类似于贿赂，影响社区成员忽视其公民义务，做出公共利益决策。这可能会导致强烈反对并损害项目的合法性。

为了避免这种情况，作者提出了设计社区利益计划的四个关键目标：通过关注实物福利来最大限度地减少自身利益，通过当地就业和透明的沟通来尊重社区，通过真正的咨询来鼓励社区参与，并通过使任何计划的开发和实施做到真实、透明和负责任来确保诚信。

总之，文章认为，虽然社区利益计划对于清洁能源转型至关重要，但必须经过精心设计并听取当地意见，以避免被视为贿赂，并确保气候行动和公民合法性都得到维护。

---

## 37. 大规模DNA研究揭示人类疾病3万7千年历史

**原文标题**: Large-scale DNA study maps 37,000 years of human disease history

**原文链接**: [https://www.cam.ac.uk/research/news/large-scale-dna-study-maps-37000-years-of-human-disease-history](https://www.cam.ac.uk/research/news/large-scale-dna-study-maps-37000-years-of-human-disease-history)

一项发表于《自然》杂志的大规模DNA研究绘制了3.7万年的人类疾病史，揭示了人与动物互动以及迁徙对传染病传播的重大影响。通过分析超过1300名史前人类的DNA，研究人员发现了最早的动物源性疾病证据，其历史可追溯至约6500年前，并在大约5000年前变得更加普遍。这一增长与亚姆纳娅牧民从蓬特草原向西北欧的迁徙同时发生。

该研究在5500年前的样本中发现了世界上最古老的鼠疫杆菌（Yersinia pestis）遗传痕迹，以及疟疾、麻风病、乙型肝炎和白喉等其他已有数千年历史的疾病。研究结果支持了向农业和畜牧业的过渡导致了疾病新时代的理论。

该研究由埃斯克·维勒斯列夫教授领导，强调了过去的感染如何可能导致人口变化和基因适应。马丁·西科拉副教授强调了了解过去疾病模式对于为未来爆发做好准备的重要性，因为许多新兴传染病都源于动物。研究人员认为，这些知识可以通过预测过去成功的突变来帮助开发更有效的疫苗。

---

## 38. Xenharmlib：一个支持非西方和声系统的音乐理论库

**原文标题**: Xenharmlib: A music theory library that supports non-western harmonic systems

**原文链接**: [https://xenharmlib.readthedocs.io/en/latest/](https://xenharmlib.readthedocs.io/en/latest/)

Xenharmlib是一个Python库，专为音乐理论设计，超越了传统的西方和声体系，涵盖了非西方、微分音和宏音调律，以及非标准记谱法。它旨在对具备基本Python知识的作曲家和研究人员来说，易于使用、扩展和直观。

主要功能包括支持平均律调律、西方和上/下记谱法、音程和音阶分析、群论分析、音程序列模式匹配、调性建议以及基本的后调性分析。

该库是面向对象的，但倾向于函数式编程，具有不可变对象和返回修改版本的方法。

计划中的功能包括西方音乐模板、用于乐谱渲染的插件接口、高级后调性分析、MOS音阶生成以及对纯律和其他调律的支持。

Xenharmlib在GNU通用公共许可证v3下发布，源代码可在Gitlab上找到。欢迎通过符合特定代码格式、测试和类型提示准则的pull request进行贡献。文档提供了用户指南，涵盖了调律、音高、音程、音阶、记谱法、序列分析和后调性基础知识，以及API文档和更新日志。

---

## 39. 考拉：面向性能优化的Shell优化研究基准套件

**原文标题**: Koala: A benchmark suite for performance-oriented shell-optimization research

**原文链接**: [https://github.com/kbensh/koala](https://github.com/kbensh/koala)

考拉 (Koala) 是一个全新的基准测试套件，专为针对 POSIX shell 脚本的性能导向型研究而设计。它包含 14 个来自不同领域的真实 shell 程序集，如 CI/CD、AI/ML、生物学和人文科学。这些基准测试附带不同大小的真实输入，从而能够进行全面的性能表征和优化。

该套件旨在为从事 shell 脚本性能研究的研究人员提供一个标准化和全面的资源，提供比现有基准测试更真实和多样化的工作负载。每个基准测试的关键方面，包括输入、依赖项和用法，都在各自的目录中详细说明。

这些基准测试涵盖广泛的任务，包括：分析、生物信息学、CI/CD 流程、COVID-19 数据分析、文件格式操作、机器学习、自然语言处理、shell 单行命令、包管理、安全审计、文本处理、天气统计和网络搜索。

考拉 (Koala) 可以通过多种方式轻松访问：一键安装脚本、克隆存储库或使用预构建的 Docker 容器。 详细的设置和配置说明，以及有关输入和依赖项的信息，可在 `INSTRUCTIONS` 文件中找到。 欢迎对项目做出贡献，如 `CONTRIBUTING` 文件中所述。 考拉 (Koala) 在 MIT 许可证下授权。 该套件的配套论文在 USENIX ATC '25 上获得了所有三个用于工件评估的徽章，表明其可用性、功能性和可重复性。

---

## 40. 考古学家在秘鲁发现3500年古城

**原文标题**: Archaeologists unveil 3,500-year-old city in Peru

**原文链接**: [https://www.bbc.co.uk/news/articles/c07dmx38kyeo](https://www.bbc.co.uk/news/articles/c07dmx38kyeo)

考古学家在秘鲁巴兰卡省发掘出一座拥有3500年历史的城市佩尼科，据信该城市是一个重要的贸易中心，连接了早期太平洋沿岸社区与安第斯山脉和亚马逊盆地。该城市位于利马以北约200公里处，其历史可追溯到公元前1800年至1500年之间。

在露丝·莎迪博士的带领下，这项研究强调了佩尼科在理解卡拉尔文明的命运方面的重要性。卡拉尔文明是美洲已知最古老的文明，曾在公元前3000年左右在附近繁荣发展，之后受到气候变化的影响。此次挖掘发现了18座建筑，包括寺庙和住宅区，其中包含祭祀物品、黏土雕塑和贝壳项链。

莎迪博士强调了佩尼科在沿海、高地和丛林社会之间进行贸易的战略地位。考古学家马科·马查奎指出，佩尼科是卡拉尔社会的延续。这一发现为秘鲁丰富的考古遗产增添了新的内容，其中包括马丘比丘和纳斯卡线条。

---

## 41. 评估内存安全消毒器的有效性

**原文标题**: Evaluating the Effectiveness of Memory Safety Sanitizers

**原文链接**: [https://www.computer.org/csdl/proceedings-article/sp/2025/223600a088/21TfesaEHTy](https://www.computer.org/csdl/proceedings-article/sp/2025/223600a088/21TfesaEHTy)

标题：内存安全净化器有效性评估

文章可能探讨内存安全净化器在识别和预防内存相关错误（如缓冲区溢出、释放后使用和重复释放）方面的有效性。它可能对不同的净化器进行比较分析，评估它们在检测各种类型内存错误方面的优缺点。

评估可能包括在启用和未启用净化器的情况下运行基准测试和实际应用程序，然后测量检测到的错误数量和类型。性能开销（如执行时间和内存消耗）也可能是关键的评估指标。

文章可能旨在为寻求通过使用内存安全净化器来提高软件可靠性和安全性的开发人员和研究人员提供有价值的见解。该研究可能会强调有效使用净化器的最佳实践，并可能为改进其准确性和性能提出未来的方向。与IEEE计算机协会的联系表明了对评估的严格技术方法。

---

## 42. Show HN: BreakerMachines – 具有异步支持的 Rails 现代断路器

**原文标题**: Show HN: BreakerMachines – Modern Circuit Breaker for Rails with Async Support

**原文链接**: [https://github.com/seuros/breaker_machines](https://github.com/seuros/breaker_machines)

BreakerMachines 是一个经过实战检验的 Ruby Gem，实现了熔断器模式，构建于 `state_machines` gem 之上，旨在提高分布式系统的可靠性。它旨在通过提供强大的服务中断管理解决方案来防止微服务架构中的级联故障。

主要特性包括线程和纤程安全操作（适用于 Falcon 等异步 Ruby）、用于降低延迟的对冲请求、具有自动故障转移的多个后端、舱壁隔离、基于百分比的阈值、动态熔断器和可插拔存储选项（内存、Redis、自定义）。它与 ActiveSupport::Notifications 集成，并提供丰富的回调和检测。

该文档涵盖入门、配置、高级模式、持久化、可观察性、异步模式和测试，包括 Rails 集成，甚至还有一个“恐怖故事”部分。

BreakerMachines 定位为现代 Ruby 应用程序的解决方案，这些应用程序需要抵御故障。它旨在阻止重试逻辑使发生故障的服务过载（“重试死亡螺旋”）。该文档采用幽默的科幻主题，将分布式系统的挑战比作在太空中的生存。

该 Gem 是开源的（MIT 许可），鼓励贡献，并将 `state_machines`、真实的服务超时和“抵抗组织”视为贡献因素。

---

## 43. 使用 Pi-Hole 和 Tailscale 配置分离式 DNS

**原文标题**: Configuring Split Horizon DNS with Pi-Hole and Tailscale

**原文链接**: [https://www.bentasker.co.uk/posts/blog/general/configuring-pihole-to-serve-different-records-to-different-clients.html](https://www.bentasker.co.uk/posts/blog/general/configuring-pihole-to-serve-different-records-to-different-clients.html)

本文详细介绍了作者如何使用 Pi-hole 和 Tailscale 配置分域 DNS，以便在离开家庭网络时，安全便捷地访问内部服务。

作者之前使用反向代理进行身份验证来保护服务免受 WAN 访问，但某些服务（如 Nextcloud）无法强制执行额外的身份验证。为了解决这个问题，并在遭受攻击尝试后减少攻击面，他们实施了分域 DNS。

目标是让 tailnet 客户端将特定的 DNS 名称解析为 tailnet IP，而 LAN 客户端解析为 LAN IP。这利用了 Pi-hole 底层的 `dnsmasq` 功能，在启用 `localise-queries` 设置后，该功能会根据接收查询的接口返回地址。

该实现包括将 DNS 记录转换为 `/etc/pihole/custom.list` 格式，并重新配置 Pi-hole Docker 容器以使用主机网络。这使 Pi-hole 可以看到 DNS 查询的实际来源接口。最初，这导致 DNS 解析失败，因为 Pi-hole 被配置为仅侦听不存在的接口 `eth0`。通过允许来自 Pi-hole Web 界面中所有来源的查询，解决了这个问题。

最后，作者禁用了 Tailscale 中之前的路由通告，并在 Tailscale 管理面板中启用了分域 DNS，确保客户端可以根据其在 LAN 或 Tailnet 上的位置将目标域名解析为相应的 IP 地址。结果是安全无缝地访问服务，无论客户端是在 LAN 上还是通过 Tailscale 远程连接。

---

## 44. 异步 Ruby 是 AI 应用的未来（它已到来）

**原文标题**: Async Ruby Is the Future of AI Apps (and It's Already Here)

**原文链接**: [https://paolino.me/async-ruby-is-the-future/](https://paolino.me/async-ruby-is-the-future/)

本文认为，异步Ruby优于Python的异步实现，尤其是在AI应用方面，特别是涉及LLM的应用。作者是一位前Python机器学习工程师，最初认为Ruby对线程的依赖已经过时，但后来发现由Samuel Williams等人构建的基于fiber的异步生态系统具有显著优势。

LLM通信具有长连接、流式响应和高并发需求，这暴露了基于线程的并发的局限性，导致了时隙饥饿、资源倍增、性能开销和可扩展性挑战。

本文将线程（抢占式多任务，由操作系统管理）与fiber（协同并发，由用户空间管理）进行了对比。Ruby的全局VM锁（GVL）使得fiber对于I/O密集型操作特别有效。与线程相比，Fiber提供更快的分配、上下文切换和更高的吞吐量，并且由于高效的资源共享和I/O多路复用而提高了可扩展性。

Ruby的异步实现是透明的，无需语法更改或库迁移。例如，RubyLLM通过利用Async块中的Net::HTTP，自动获得异步性能。本文重点介绍了`async` gem及其生态系统，包括Falcon、async-job和async-cable。将Rails应用程序迁移到异步非常简单，只需进行最少的配置更改。

Async最适合I/O密集型操作，如API调用和流式传输，而线程仍然适用于CPU密集型任务或遗留C扩展。作者认为，Ruby的方法避免了Python异步采用中出现的分裂和复杂性，通过更低的成本、更好的性能和更简单的操作（无需更改代码库）为AI应用程序开发提供了竞争优势。

---

## 45. 从国际空间站扔出的纸飞机能幸存飞行吗？

**原文标题**: Could a Paper Plane Thrown from the ISS Survive the Flight?

**原文链接**: [https://www.sciencealert.com/could-a-paper-plane-thrown-from-the-international-space-station-survive-the-flight](https://www.sciencealert.com/could-a-paper-plane-thrown-from-the-international-space-station-survive-the-flight)

今日宇宙文章探讨纸飞机从国际空间站再入大气层的可行性。东京大学的研究员Maximilien Berthet和Kojiro Suzuki对由标准A4纸张制成的折纸太空飞机的动力学进行了建模。

他们的模拟显示，从国际空间站以7800米/秒的速度发射的纸飞机，在400公里至120公里高度的稀薄大气中将保持相对稳定，由于其低弹道系数，将在大约3.5天内下降到120公里。然而，当到达120公里左右的稠密大气时，飞机会经历无法控制的翻滚，从而无法稳定下降。

为了进一步研究，研究人员将纸飞机的三分之一比例模型（带有铝制尾翼）置于高超音速风洞中，以7马赫的风速模拟了7秒钟的再入大气层条件。虽然飞机没有解体，但机头向后弯曲并出现炭化迹象，表明它最终会被烧毁。

该实验虽然没有产生幸存的纸飞机，但突出了使用轻型、稳定平台执行LEAVES金星探测或地球观测等任务的潜力，这些平台的设计目的是在其使用寿命结束时完全烧毁。这项研究融合了灵感和探索，展示了简单设计在复杂应用中的可能性。

---

## 46. 地球上最超凡脱俗、神秘莫测的闪电形态

**原文标题**: The most otherworldly, mysterious forms of lightning on Earth

**原文链接**: [https://www.nationalgeographic.com/science/article/lightning-sprites-transient-luminous-events-thunderstorms](https://www.nationalgeographic.com/science/article/lightning-sprites-transient-luminous-events-thunderstorms)

本文探讨瞬态发光现象(TLE)，这是一种神秘的光显示，发生在地球高层大气中雷暴之上。这些现象包括红色精灵、喷流和鬼影，因其难以捉摸的本质和外观而以童话人物命名。科学家们正致力于了解它们的成因、频率以及它们所揭示的关于大气的信息。

红色精灵是最常见的瞬态发光现象，是由正向闪电产生一个延伸到大气层高处的电场引起的。最近的研究，包括来自青藏高原业余天体摄影师的观测，极大地促进了瞬态发光现象的研究，证明了公民科学的价值。美国宇航局的“精灵奇观”项目是一个众包数据库，收集来自全球各地的瞬态发光现象图像，以识别模式并研究更罕见的事件。

了解瞬态发光现象也可能为其他行星提供见解，因为有证据表明类似的现象发生在木星上。此外，研究界正在调查气候变化如何通过影响雷暴强度和闪电活动来影响瞬态发光现象的发生。研究这些转瞬即逝的大气事件不仅满足了好奇心，而且还提供了关于地球风暴和大气变化的至关重要信息。

---

## 47. 展示一下：我建了一个游乐场来展示 Flux Kontext 的优势

**原文标题**: Show HN: I built a playground to showcase what Flux Kontext is good at

**原文链接**: [https://fluxkontextlab.com](https://fluxkontextlab.com)

Show HN：Flux Kontext Dev - 基于AI的在线图像编辑工具，无需注册即可免费使用

Flux Kontext Dev 的主要特点包括：

*   **AI驱动的编辑：** 基于用户定义的文本指令转换图像。
*   **多样化的应用：** 涵盖从简单调整到复杂转换的广泛编辑任务。
*   **模型展示：** 通过前后对比示例展示该工具的功能。
*   **免费在线工具：** 无需注册即可访问，即时获得结果。
*   **开放权重（非商业用途）：** 提供对底层FLUX.1 Kontext [dev]模型的访问，用于研究和非商业用途。
*   **卓越的性能：** 声称优于现有的开放图像编辑模型。
*   **硬件优化：** 针对NVIDIA Blackwell架构进行了优化。
*   **开发者友好：** 兼容流行的推理框架，如ComfyUI和HuggingFace Diffusers。

该帖子强调Flux Kontext Dev 专注于编辑任务，能够进行迭代编辑，并具有出色的角色保留能力，同时提供局部和全局编辑功能。它旨在通过为用户提供强大、可访问和高质量的AI驱动图像处理工具，从而为开放图像编辑设定新标准。

---

## 48. 白噪声 - 安全私密的通讯工具

**原文标题**: White Noise – secure and private messenger

**原文链接**: [https://www.whitenoise.chat/](https://www.whitenoise.chat/)

White Noise：一款注重用户隐私与自由的安全私密通讯工具。它强调强大的端到端加密，具备前向保密和事后安全，即使密钥泄露也能确保过去和未来的消息保持隐秘。其关键特性是身份自由，允许用户在无需电话号码或电子邮件的情况下进行通信，可以使用匿名身份、化名或真实姓名。

White Noise基于Nostr和MLS等开放式去中心化标准构建，使用户能够在不同平台之间迁移其身份、数据和联系人。 其分布式网络由独立节点驱动，提供抗审查能力，并允许用户运行自己的中继节点。

White Noise的设计兼顾速度、可靠性和可扩展性，能够高效处理直接消息和大型群聊。 它作为一个非营利性的社区驱动项目运作，独立于企业或政府资金。

文本包含常见问题解答部分，解答了关于加密、审查、数据位置、中继可用性、审核、开源性质、多设备使用、长期安全性、私有中继、消息隐私验证、设备盗窃和使用成本等方面的问题。 这些主题进一步突显了White Noise对用户安全、隐私和控制的承诺。 该服务免费使用。

---

## 49. 未能成功的桌面出版工具 (2022)

**原文标题**: Desktop Publishing Tools That Didn't Make It (2022)

**原文链接**: [https://tedium.co/2022/10/12/forgotten-desktop-publishing-tools-history/](https://tedium.co/2022/10/12/forgotten-desktop-publishing-tools-history/)

本文探讨了十款早期桌面出版(DTP)软件，尽管DTP对计算机行业和新业务的创造产生了重大影响，但这些软件已经被人遗忘。

该列表从**施乐奥拓(Xerox Alto)**开始，认为其功能预示了DTP，并引用了其排版和文档布局工具。接下来讨论的是**The Book Machine**，一台专用排版计算机，重点介绍了其高昂的成本和利基受众。然后，提到了**MacPublisher**，一款早于PageMaker的早期Mac DTP工具，以及它的发明者Bob Doyle。**Aldus PageMaker**，一款非常成功且定义行业的应用程序，也被作为最终被取代的软件的例子包含在内。

该文章还涵盖了更多面向消费者的选项，例如旨在为儿童创建可打印报纸的**The Newsroom**，以及首批以PC为中心的DTP应用程序之一**Clickart Personal Publisher**。然后，介绍了相对复杂的**geoPublish**，适用于Commodore 64和Apple II。**Ventura Publisher**，以其样式表和类似XML的文档代码而闻名，以及出现在各种平台上并努力解决字距调整问题的**Timeworks Publisher**，也得到了考察。最后，提到了**Serif PagePlus**，为其继任者Affinity Publisher奠定了基础。

本文最终突出了DTP软件的演变，展示了早期出现的各种工具，其中许多工具为我们今天使用的更复杂的程序铺平了道路。

---

## 50. 微软宣称节省5亿美元AI成本，同时大规模裁员

**原文标题**: Microsoft Touts $500M AI Savings While Slashing Jobs

**原文链接**: [https://finance.yahoo.com/news/microsoft-touts-500-million-ai-171149783.html](https://finance.yahoo.com/news/microsoft-touts-500-million-ai-171149783.html)

微软展示了其人工智能实施带来的财务效益，仅去年一年在呼叫中心就节省了超过 5 亿美元。与此同时，公司仍在持续裁员，今年已裁员约 15,000 人，其中包括最近在客户服务岗位的裁员。首席商务官 Judson Althoff 强调，人工智能正在提高各个部门的生产力，包括销售、客户服务和软件工程。人工智能现在正在处理与较小客户的互动，产生数百万美元的收入，并为新产品的 35% 代码做出贡献，从而加快了上市时间。

其他科技公司，如 Salesforce、Alphabet 和 Meta，也在利用人工智能来实现任务自动化和减少招聘需求。虽然人工智能的实施引发了员工对工作保障的担忧，但 Althoff 认为人工智能可以提高销售人员的效率，他提到 Copilot AI 助手可以帮助销售人员找到更多潜在客户、更快地完成交易并增加 9% 的收入。尽管进行了裁员，微软仍坚称，正如首席律师 Brad Smith 所说，人工智能带来的生产力提升“并非近期裁员的主要因素”。该公司还在投资超过 40 亿美元的现金和技术，以促进学校的人工智能技能发展。

---

## 51. 您要来一份 IDOR 漏洞吗？泄露 6400 万麦当劳求职申请

**原文标题**: Would You Like an IDOR With That? Leaking 64m McDonald's Job Applications

**原文链接**: [https://ian.sh/mcdonalds](https://ian.sh/mcdonalds)

安全研究人员发现了麦当劳加盟商使用的招聘聊天机器人平台McHire中的两个严重漏洞：管理界面的默认凭据（123456:123456）以及内部API中的不安全直接对象引用（IDOR）。

使用默认凭据登录后，他们获得了对测试餐厅账户的管理权限，从而能够探索McHire系统。随后，他们通过操纵`/api/lead/cem-xhr` API端点中的`lead_id`参数发现了IDOR漏洞。这使他们能够访问超过6400万麦当劳求职者的个人数据。

可访问的数据包括姓名、电子邮件地址、电话号码、地址、候选人状态、提交的申请数据（如轮班偏好），甚至还有访问申请人聊天记录的身份验证令牌。这意味着任何拥有McHire账户的人都可能检索到敏感信息。

研究人员迅速向 Paradox.ai (McHire背后的公司) 和麦当劳披露了该漏洞。Paradox.ai迅速修复了这些问题，撤销了默认凭据，并修补了IDOR漏洞。该公司承诺进行进一步的安全审查。研究人员还感谢合作者 Ian Carroll 和 Sam Curry。

---

## 52. 通过恶意图表执行Helm本地代码

**原文标题**: Helm local code execution via a malicious chart

**原文链接**: [https://github.com/helm/helm/security/advisories/GHSA-557j-xg8c-q2mm](https://github.com/helm/helm/security/advisories/GHSA-557j-xg8c-q2mm)

安全公告：Helm 高危漏洞 (CVE-2025-53547)

---

## 53. HyAB k-means 颜色量化

**原文标题**: HyAB k-means for color quantization

**原文链接**: [https://30fps.net/pages/hyab-kmeans/](https://30fps.net/pages/hyab-kmeans/)

本文探讨了使用HyAB颜色距离公式与k-means聚类进行颜色量化以提高图像质量的方法。作者Pekka Väänänen详细阐述了HyAB，一种结合了绝对亮度差和欧几里得色度距离的混合距离，如何比CIELAB空间中的标准欧几里得距离更好地表示大的颜色差异。

作者将HyAB k-means应用于颜色量化，为图像找到有限的调色板并重建它。他将其与Pillow的quantize()、libimagequant、sRGB k-means以及纯CIELAB k-means进行了比较。结果表明，HyAB能够更好地控制亮度与颜色误差，并提高色调精度，尤其是在品红色和绿色等具有挑战性的颜色中。

Väänänen还试验了在HyAB中对L通道（亮度）进行加权，发现它比sRGB或CIELAB中的类似调整更容易控制。他进一步修改了k-means算法，使用中位数而不是平均值来计算聚类中心的L分量，观察到了细微的改进。

文章提醒说，HyAB并非万能药，一个完善的图像压缩系统，包括抖动和适当的缩放等技术，对于获得最佳效果至关重要。虽然HyAB可以在特定情况下提供改进，尤其是在处理大的颜色差异或固定调色板时，但它不应取代全面的系统调优。

---

## 54. 麦当劳AI招聘机器人被曝将申请人数据暴露给黑客

**原文标题**: McDonald's AI Hiring Bot Exposed Applicants' Data to Hackers

**原文链接**: [https://www.wired.com/story/mcdonalds-ai-hiring-chat-bot-paradoxai/](https://www.wired.com/story/mcdonalds-ai-hiring-chat-bot-paradoxai/)

安全研究人员发现Paradox.ai的AI聊天机器人平台Olivia存在重大漏洞，麦当劳使用该平台进行招聘。由于管理员账户使用了极其薄弱的密码“123456”，他们获得了测试账户的访问权限。这使得他们能够查询包含多达6400万条麦当劳求职者记录的数据库，其中包括姓名、电子邮件地址和电话号码。

研究人员Ian Carroll和Sam Curry最初对麦当劳使用AI聊天机器人进行招聘及其潜在的利用可能性感到好奇。他们发现他们可以操纵申请人ID号码来查看其他申请人的聊天记录和个人信息。

Paradox.ai证实了这些发现，声称只有一小部分记录包含个人信息，并且该弱密码未被任何其他第三方访问过。他们正在实施漏洞赏金计划作为回应。麦当劳指责Paradox.ai存在“不可接受的漏洞”，并强制要求立即修复。

暴露的数据，加上求职者正在麦当劳求职这一信息，可能会造成重大的网络钓鱼风险。欺诈者可以冒充招聘人员并索要敏感的财务信息。虽然暴露的信息本身并不是最敏感的，但其背景使其成为恶意行为者的有价值的目标。

---

## 55. 让Lovable和Bolt变得惹人喜爱的架构

**原文标题**: The Architecture Behind Lovable and Bolt

**原文链接**: [https://www.beam.cloud/blog/agentic-apps](https://www.beam.cloud/blog/agentic-apps)

很抱歉，我没有足够的信息来完成这个请求。提供的文本只包含标题“Lovable and Bolt背后的架构”以及短语“你需要启用JavaScript才能运行此应用程序的人工智能产品云”。 这并没有提供任何关于Lovable and Bolt背后架构的内容来进行总结。

---

## 56. Zorin OS
卓林操作系统

**原文标题**: Zorin OS

**原文链接**: [https://zorin.com/os/](https://zorin.com/os/)

Zorin OS 被定位为Windows和macOS的易用替代品，旨在恢复旧电脑的活力，并提供更快、更安全且尊重隐私的操作系统。它面向面临Windows 10生命周期结束的Windows用户，强调易用性，允许用户自定义桌面环境，使其类似于熟悉的操作系统。

主要亮点包括：

*   **性能：** Zorin OS设计轻量级，即使在较旧的硬件上也能快速运行，延长现有PC的使用寿命。
*   **安全与隐私：** 基于Linux构建，它能抵抗病毒和恶意软件，提供及时的安全更新，并通过不收集个人数据来尊重用户隐私。
*   **兼容性：** 它支持广泛的应用程序，包括许多Windows应用程序，并与现有文档和文件兼容。它预装了基本应用程序，并允许访问软件商店。
*   **游戏：** 通过Steam、Lutris和其他平台，它支持庞大的游戏库，并优化了图形驱动程序。
*   **连接性：** Zorin Connect允许与Android设备无缝集成，实现通知、文件共享和远程控制。
*   **辅助功能：** 它支持100多种语言，并包含辅助技术。
*   **双启动：** 用户可以将其与现有操作系统一起安装。

Zorin OS提供免费的“Core”版本，以及提供更多功能和支持的付费“Pro”版本。积极的用户评价强调其易用性、速度和吸引人的设计。17版本的软件更新和安全补丁将至少持续到2027年6月。

---

## 57. 美国法院废止联邦贸易委员会“点击取消”要求

**原文标题**: US Court nullifies FTC requirement for click-to-cancel

**原文链接**: [https://arstechnica.com/tech-policy/2025/07/us-court-cancels-ftc-rule-that-would-have-made-canceling-subscriptions-easier/](https://arstechnica.com/tech-policy/2025/07/us-court-cancels-ftc-rule-that-would-have-made-canceling-subscriptions-easier/)

美国上诉法院推翻联邦贸易委员会“点击取消”规定。该规定旨在使取消订阅与注册一样容易。法院一致裁定，在一位行政法法官认定该规定的年度经济影响将超过1亿美元后，前主席莉娜·汗领导下的联邦贸易委员会未能遵守适当的规则制定程序，未进行初步监管分析。

法院同情联邦贸易委员会防止消费者陷入不必要订阅的目标，但强调程序缺陷是致命的。他们强调，缺乏初步分析剥夺了行业团体充分机会来质疑联邦贸易委员会的成本效益分析以及该规定的替代方案。

联邦贸易委员会辩称，该过程后期不需要初步分析，并且任何错误都是无害的，但法院不同意，称一旦超过1亿美元的门槛，就必须进行单独的初步分析。包括有线电视公司在内的行业团体起诉了联邦贸易委员会，导致第八巡回法院审理了合并案件。

共和党联邦贸易委员会委员从一开始就反对该规定，其中一位警告说，该规定可能无法通过法律挑战，并指责多数派在2024年大选前仓促制定该规定。前主席汗辩称，该规定将通过结束取消订阅的“技巧和陷阱”来节省消费者的时间和金钱。 该裁决引发了人们对通过最初较低的经济影响估计来操纵规则制定过程，从而限制公众参与和分析的担忧。

---

## 58. 可解释的扫雷游戏

**原文标题**: Making Explainable Minesweeper

**原文链接**: [https://sublevelgames.github.io/blogs/2025-07-06-making-explainable-minesweeper/](https://sublevelgames.github.io/blogs/2025-07-06-making-explainable-minesweeper/)

本文详细介绍了作者创建“可解释扫雷”的过程，这是一款经典扫雷游戏的版本，旨在教导玩家逻辑推理，而非依赖运气。受“14种扫雷变体”中提示的启发，作者意识到许多玩家，包括他们自己，经常错过推理的机会，尤其是在模棱两可的情况下。

“可解释扫雷”的核心在于其地图生成过程。它生成随机棋盘，然后人工智能尝试从不同的起点进行演绎求解。只有完全通过演绎可解的棋盘才会被保留。然后，人工智能会稍微揭示这些棋盘，以降低起始难度。

本文概述了游戏中实现的演绎规则，这些规则也用作提示：全局模式（解决所有地雷或常规单元格会显示其余部分）、简单模式（当邻居计数与单元格的数字匹配时标记单元格，或者在放置所有标记后显示剩余单元格）和高级模式。高级模式侧重于比较两个相邻编号单元格之间公共和唯一区域中所需地雷的数量，从而可以对这些区域是否包含地雷或是否安全做出逻辑结论。

作者强调，这些模式背后的逻辑相对简单，可以用常识解决，突出了许多玩家通过理解这些演绎方法来提高扫雷技能的潜力。该游戏支持多种语言，作者欢迎反馈和对额外语言支持的请求。关键目标是教育玩家，并证明扫雷可以通过逻辑而不是仅仅依靠运气来解决。

---

## 59. 从任务到餐桌：我如何吃到韩式汉堡

**原文标题**: From Task to Table: How I Got to the Korean Burger

**原文链接**: [https://medium.com/@chrisveleris/from-task-to-table-how-i-finally-got-to-the-korean-burger-01245a14d491](https://medium.com/@chrisveleris/from-task-to-table-how-i-finally-got-to-the-korean-burger-01245a14d491)

克里斯·维勒里斯的文章《从任务到餐桌：我是如何接触到韩式汉堡的》提倡一种名为tududi的任务管理系统，该系统优先考虑流程和最小认知负荷。维勒里斯批评了过于复杂的任务应用程序，将它们比作菜单繁琐的餐厅，导致决策瘫痪和质量下降。他认为，这些应用程序的无限选项和设置会产生摩擦，阻碍生产力。

tududi的核心概念是避开用户的干扰，充当一个“安静的助手”，实现无缝的输入、捕获、分配和执行。它避免了不必要的功能，如电子邮件通知或动画，而是专注于提供清晰的前进道路。该系统是可定制的，允许用户仅在需要时添加类别和颜色，从而保持心理带宽。

维勒里斯通过一个真实的日常场景来说明tududi的简洁性，展示了它是如何通过Telegram无缝捕获任务和想法，并将它们集成到一个统一的收件箱中。他强调行动和执行的重要性，而不是细致的管理，突出了诸如“智能建议”之类的功能，这些功能可以指导任务选择。总体目标是创建一个适应用户的工具，而不是强迫用户适应工具，最终促进专注和不间断的思考。文章最后将简洁定义为不是缺乏力量，而是专注的力量，在没有不必要干扰的情况下赋能用户。

---

## 60. 为什么LLM写不出Q/Kdb+：从右到左编写代码

**原文标题**: Why LLMs Can't Write Q/Kdb+: Writing Code Right-to-Left

**原文链接**: [https://medium.com/@gabiteodoru/why-llms-cant-write-q-kdb-writing-code-right-to-left-ea6df68af443](https://medium.com/@gabiteodoru/why-llms-cant-write-q-kdb-writing-code-right-to-left-ea6df68af443)

大型语言模型为何难以编写q/kdb+代码

---

## 61. 更深入地了解CPU分支指令

**原文标题**: Understand CPU Branch Instructions Better

**原文链接**: [https://chrisfeilbach.com/2025/07/05/understand-cpu-branch-instructions-better/](https://chrisfeilbach.com/2025/07/05/understand-cpu-branch-instructions-better/)

本文深入探讨CPU分支指令，这些指令对于程序决策和性能至关重要。文章解释了顺序执行模型，即指令一个接一个地执行，除非分支指令重定向控制流。

分支分为条件分支（仅当满足条件时才执行）和无条件分支（总是执行）。条件分支依赖于CPU标志或比较来确定其方向。分支也可以是直接分支（目标地址编码在指令中）或间接分支（目标地址由寄存器或内存位置确定）。

本文强调了分支预测的重要性，CPU会猜测分支是否会被执行，并相应地获取下一条指令。正确的预测可以提高性能，而错误的预测会导致浪费精力。分支预测是有效的，因为分支往往是可预测的，尤其是在循环中。

然而，即使正确预测，频繁的分支也可能代价高昂。优化策略包括简化if语句和循环条件，确保内联合适的函数以消除调用/返回分支，避免过度的函数调用深度以防止返回地址栈溢出，以及最小化间接分支（通常与C++继承和函数指针相关）。本文强调了代码灵活性与某些编程结构相关的性能成本之间的权衡。

---

## 62. 我将SAP移植到1976年的CPU上，速度还行。

**原文标题**: I Ported SAP to a 1976 CPU. It Wasn't That Slow

**原文链接**: [https://github.com/oisee/zvdb-z80/blob/master/ZVDB-Z80-ABAP.md](https://github.com/oisee/zvdb-z80/blob/master/ZVDB-Z80-ABAP.md)

将SAP移植到1976年CPU上：并没有那么慢

---

## 63. Attimet (YC F24) – 量化交易研究实验室 – 招聘创始研究员

**原文标题**: Attimet (YC F24) – Quant Trading Research Lab – Is Hiring Founding Researcher

**原文链接**: [https://www.ycombinator.com/companies/attimet/jobs/6LaQIc5-founding-researcher-quant](https://www.ycombinator.com/companies/attimet/jobs/6LaQIc5-founding-researcher-quant)

Attimet 招募创始研究员/量化分析师

Attimet (Y Combinator F24 孵化的初创公司) 正在寻找一位创始研究员/量化分析师加入他们在旧金山的量化交易研究实验室。该职位提供 10 万美元 - 15 万美元的年薪和 0.25% - 1.00% 的股权。Attimet 正在构建时间人工智能系统，以适应、预测金融市场中的行为，最初专注于期权交易。他们的优势在于快速迭代和学习，而非秘密数据。

创始研究员将领导机器学习/人工智能战略，开发预测模型、强化学习智能体和信号发现工作流程。他们将整合另类数据，设计实验，并在模拟和实盘交易中测试假设，直接通过市场回报衡量影响。公司强调与创始人合作，根据真实市场结果改进预测。

Attimet 正在寻找在机器学习/人工智能（尤其是时间序列、预测和表征学习）方面具有深厚专业知识、精通 Python 编码技能以及具有模型生产部署经验的人才。不需要金融市场经验；动力和好奇心是首要考虑因素。该公司强调自主性和进行有影响力工作的机会。Attimet 旨在构建一个实验平台，弥合流动市场中研究与实践之间的差距。创始人拥有来自 Optiver、DRW 和 Argo AI 的经验。

---

## 64. CockroachDB 中的多区域行级安全

**原文标题**: Multi-Region Row Level Security in CockroachDB

**原文链接**: [https://www.cockroachlabs.com/blog/fine-grained-access-control-row-level-security/](https://www.cockroachlabs.com/blog/fine-grained-access-control-row-level-security/)

This article introduces Row-Level Security (RLS) in CockroachDB 25.2, highlighting its ability to enforce fine-grained data access policies at the row level, addressing limitations of table-level permissions. RLS is particularly useful for multi-tenancy and multi-region scenarios.

For multi-tenancy, RLS enables data isolation in shared tables, reducing infrastructure costs and operational complexity compared to separate databases/schemas per tenant. The article demonstrates how to implement RLS using session variables to control tenant data visibility without modifying application queries.

In multi-region deployments, RLS complements CockroachDB's Regional by Row (RBR) feature, allowing data residency and access control based on geographic location. The article shows how to combine RBR and RLS to restrict user access based on their connection region, ensuring compliance with data residency laws like GDPR. Users connected in US-east1 will only see data from us-east1 and so on.

The article emphasizes that CockroachDB's RLS provides a powerful, built-in mechanism for enforcing fine-grained access control directly within the database, scaling securely and efficiently without extensive application changes. It also provides resources for users to get started with RLS in their own applications.


---

## 65. Show HN: OffChess - 离线象棋谜题应用

**原文标题**: Show HN: OffChess – Offline chess puzzles app

**原文链接**: [https://offchess.com](https://offchess.com)

OffChess is an offline chess puzzle app boasting over 100,000 puzzles playable without an internet connection. The app is available on both the App Store and Play Store. A key feature is its rating system: puzzles are rated, and users gain or lose points based on their performance against the puzzle's difficulty. OffChess tracks user statistics, enabling players to monitor their progress and improve their chess skills. Users can customize the app's appearance with a variety of themes. The app emphasizes accessibility, offering a vast library of puzzles accessible anytime, anywhere, even without Wi-Fi, making it ideal for travel or situations where internet access is limited. The bottom of the app provides navigation links to "home," "about," "privacy," and "contact," and includes a copyright notice for 2025. In short, OffChess promotes chess skill improvement through offline puzzle solving with a focus on personalization and accessibility.


---

## 66. 今天在哪里可以看到葛饰北斋的巨浪？

**原文标题**: Where can I see Hokusai's Great Wave today?

**原文链接**: [https://greatwavetoday.com/](https://greatwavetoday.com/)

This resource provides information on where to view Hokusai's iconic "Great Wave" woodblock print. Currently, the print is listed as being on view at the Musei Civici in Treviso, Italy until September 28, 2025, and at the Musée d’histoire in Nantes, France until September 7, 2025.

The resource also lists other locations where it *may* be on view, referencing Instagram posts or websites as confirmation: the Civic Museum of Oriental Art in Trieste, Italy, Palazzo Maffei Casa Museo in Verona, Italy, and the Hill-Stead Museum in Farmington, USA.

Finally, it notes that the print is *not* currently on display at 55 other locations. The resource invites museums and galleries to get listed by posting at GitHub and offers automatic updates via an RSS feed. It also credits the project to Matt Sephton and provides a link to learn more about the print itself.


---

## 67. At last, a use case for AI agents with sky-high ROI: Stealing crypto

**原文标题**: At last, a use case for AI agents with sky-high ROI: Stealing crypto

**原文链接**: [https://www.theregister.com/2025/07/10/ai_agents_automatically_steal_cryptocurrency/](https://www.theregister.com/2025/07/10/ai_agents_automatically_steal_cryptocurrency/)

生成摘要时出错

---

## 68. German court rules Meta tracking technology violates European privacy laws

**原文标题**: German court rules Meta tracking technology violates European privacy laws

**原文链接**: [https://therecord.media/german-court-meta-tracking-tech](https://therecord.media/german-court-meta-tracking-tech)

生成摘要时出错

---

## 69. Executed Chinese prisoners likely used in UK exhibition (2021)

**原文标题**: Executed Chinese prisoners likely used in UK exhibition (2021)

**原文链接**: [https://www.theartnewspaper.com/2021/01/25/executed-chinese-prisoners-likely-used-in-uk-exhibition](https://www.theartnewspaper.com/2021/01/25/executed-chinese-prisoners-likely-used-in-uk-exhibition)

生成摘要时出错

---

## 70. Chimpfluencers Stick Grass in Their Ears and Butts in Latest Viral Trend

**原文标题**: Chimpfluencers Stick Grass in Their Ears and Butts in Latest Viral Trend

**原文链接**: [https://www.sciencealert.com/chimpfluencers-are-sticking-grass-in-their-ears-and-butts-in-latest-viral-trend](https://www.sciencealert.com/chimpfluencers-are-sticking-grass-in-their-ears-and-butts-in-latest-viral-trend)

生成摘要时出错

---

## 71. ESIM Security

**原文标题**: ESIM Security

**原文链接**: [https://security-explorations.com/esim-security.html](https://security-explorations.com/esim-security.html)

生成摘要时出错

---

## 72. Kite News

**原文标题**: Kite News

**原文链接**: [https://kite.kagi.com/](https://kite.kagi.com/)

生成摘要时出错

---

## 73. Phrase origin: Why do we "call" functions?

**原文标题**: Phrase origin: Why do we "call" functions?

**原文链接**: [https://quuxplusone.github.io/blog/2025/04/04/etymology-of-call/](https://quuxplusone.github.io/blog/2025/04/04/etymology-of-call/)

生成摘要时出错

---

## 74. Ruby 3.4 frozen string literals: What Rails developers need to know

**原文标题**: Ruby 3.4 frozen string literals: What Rails developers need to know

**原文链接**: [https://www.prateekcodes.dev/ruby-34-frozen-string-literals-rails-upgrade-guide/](https://www.prateekcodes.dev/ruby-34-frozen-string-literals-rails-upgrade-guide/)

生成摘要时出错

---

## 75. Is the doc bot docs, or not?

**原文标题**: Is the doc bot docs, or not?

**原文链接**: [https://www.robinsloan.com/lab/what-are-we-even-doing-here/](https://www.robinsloan.com/lab/what-are-we-even-doing-here/)

生成摘要时出错

---

## 76. I'm Building LLM for Satellite Data EarthGPT.app

**原文标题**: I'm Building LLM for Satellite Data EarthGPT.app

**原文链接**: [https://www.earthgpt.app/](https://www.earthgpt.app/)

生成摘要时出错

---

## 77. Most RESTful APIs aren't really RESTful

**原文标题**: Most RESTful APIs aren't really RESTful

**原文链接**: [https://florian-kraemer.net//software-architecture/2025/07/07/Most-RESTful-APIs-are-not-really-RESTful.html](https://florian-kraemer.net//software-architecture/2025/07/07/Most-RESTful-APIs-are-not-really-RESTful.html)

生成摘要时出错

---

## 78. Libpostal: C library for parsing/normalizing street addresses around the world

**原文标题**: Libpostal: C library for parsing/normalizing street addresses around the world

**原文链接**: [https://github.com/openvenues/libpostal](https://github.com/openvenues/libpostal)

生成摘要时出错

---

## 79. Breaking Git with a carriage return and cloning RCE

**原文标题**: Breaking Git with a carriage return and cloning RCE

**原文链接**: [https://dgl.cx/2025/07/git-clone-submodule-cve-2025-48384](https://dgl.cx/2025/07/git-clone-submodule-cve-2025-48384)

生成摘要时出错

---

## 80. IKEA ditches Zigbee for Thread going all in on Matter smart homes

**原文标题**: IKEA ditches Zigbee for Thread going all in on Matter smart homes

**原文链接**: [https://www.theverge.com/smart-home/701697/ikea-matter-thread-new-products-new-smart-home-strategy](https://www.theverge.com/smart-home/701697/ikea-matter-thread-new-products-new-smart-home-strategy)

生成摘要时出错

---

## 81. A lightweight Cloudflare Dynamic DNS shell script

**原文标题**: A lightweight Cloudflare Dynamic DNS shell script

**原文链接**: [https://github.com/fernvenue/cloudflare-ddns](https://github.com/fernvenue/cloudflare-ddns)

生成摘要时出错

---

## 82. Matt Trout has died

**原文标题**: Matt Trout has died

**原文链接**: [https://www.shadowcat.co.uk/2025/07/09/ripples-they-cause-in-the-world/](https://www.shadowcat.co.uk/2025/07/09/ripples-they-cause-in-the-world/)

生成摘要时出错

---

## 83. Astro is a return to the fundamentals of the web

**原文标题**: Astro is a return to the fundamentals of the web

**原文链接**: [https://websmith.studio/blog/astro-is-a-developers-dream/](https://websmith.studio/blog/astro-is-a-developers-dream/)

生成摘要时出错

---

## 84. Dynamical origin of Theia, the last giant impactor on Earth

**原文标题**: Dynamical origin of Theia, the last giant impactor on Earth

**原文链接**: [https://arxiv.org/abs/2507.01826](https://arxiv.org/abs/2507.01826)

生成摘要时出错

---

## 85. Using MPC for Anonymous and Private DNA Analysis

**原文标题**: Using MPC for Anonymous and Private DNA Analysis

**原文链接**: [https://vishakh.blog/2025/07/08/using-mpc-for-anonymous-and-private-dna-analysis/](https://vishakh.blog/2025/07/08/using-mpc-for-anonymous-and-private-dna-analysis/)

生成摘要时出错

---

## 86. Show HN: Virby, a vfkit-based Linux builder for Nix-Darwin

**原文标题**: Show HN: Virby, a vfkit-based Linux builder for Nix-Darwin

**原文链接**: [https://github.com/quinneden/virby-nix-darwin](https://github.com/quinneden/virby-nix-darwin)

生成摘要时出错

---

## 87. Comet Browser by Perplexity

**原文标题**: Comet Browser by Perplexity

**原文链接**: [https://comet.perplexity.ai/](https://comet.perplexity.ai/)

生成摘要时出错

---

## 88. RapidRAW: A non-destructive and GPU-accelerated RAW image editor

**原文标题**: RapidRAW: A non-destructive and GPU-accelerated RAW image editor

**原文链接**: [https://github.com/CyberTimon/RapidRAW](https://github.com/CyberTimon/RapidRAW)

生成摘要时出错

---

## 89. Blind to Disruption – The CEOs Who Missed the Future

**原文标题**: Blind to Disruption – The CEOs Who Missed the Future

**原文链接**: [https://steveblank.com/2025/07/08/blind-to-disruption-the-ceos-who-missed-the-future/](https://steveblank.com/2025/07/08/blind-to-disruption-the-ceos-who-missed-the-future/)

生成摘要时出错

---

## 90. SVGs that feel like GIFs

**原文标题**: SVGs that feel like GIFs

**原文链接**: [https://koaning.io/posts/svg-gifs/](https://koaning.io/posts/svg-gifs/)

生成摘要时出错

---

## 91. iPod Linux (2017)

**原文标题**: iPod Linux (2017)

**原文链接**: [http://www.ipodlinux.org/](http://www.ipodlinux.org/)

生成摘要时出错

---

## 92. Smollm3: Smol, multilingual, long-context reasoner LLM

**原文标题**: Smollm3: Smol, multilingual, long-context reasoner LLM

**原文链接**: [https://huggingface.co/blog/smollm3](https://huggingface.co/blog/smollm3)

生成摘要时出错

---

## 93. Federal court in Colorado fines lawyers for errors caused by use of "AI"

**原文标题**: Federal court in Colorado fines lawyers for errors caused by use of "AI"

**原文链接**: [https://archive.org/download/gov.uscourts.cod.215068/gov.uscourts.cod.215068.383.0.pdf](https://archive.org/download/gov.uscourts.cod.215068/gov.uscourts.cod.215068.383.0.pdf)

生成摘要时出错

---

## 94. Browser extensions turn nearly 1M browsers into website-scraping bots

**原文标题**: Browser extensions turn nearly 1M browsers into website-scraping bots

**原文链接**: [https://arstechnica.com/security/2025/07/browser-extensions-turn-nearly-1-million-browsers-into-website-scraping-bots/](https://arstechnica.com/security/2025/07/browser-extensions-turn-nearly-1-million-browsers-into-website-scraping-bots/)

生成摘要时出错

---

## 95. Epanet-JS

**原文标题**: Epanet-JS

**原文链接**: [https://macwright.com/2025/07/03/epanet-placemark](https://macwright.com/2025/07/03/epanet-placemark)

生成摘要时出错

---

## 96. Ceramic: A cross-platform and open-source 2D framework in Haxe

**原文标题**: Ceramic: A cross-platform and open-source 2D framework in Haxe

**原文链接**: [https://ceramic-engine.com/](https://ceramic-engine.com/)

生成摘要时出错

---

## 97. Code and Trust: Vibrators to Pacemakers

**原文标题**: Code and Trust: Vibrators to Pacemakers

**原文链接**: [https://punkx.org/jackdoe/code-and-trust.html](https://punkx.org/jackdoe/code-and-trust.html)

生成摘要时出错

---

## 98. GlobalFoundries to Acquire MIPS

**原文标题**: GlobalFoundries to Acquire MIPS

**原文链接**: [https://mips.com/press-releases/gf-mips/](https://mips.com/press-releases/gf-mips/)

生成摘要时出错

---

## 99. Plants monitor the integrity of their barrier by sensing gas diffusion

**原文标题**: Plants monitor the integrity of their barrier by sensing gas diffusion

**原文链接**: [https://www.nature.com/articles/s41586-025-09223-4](https://www.nature.com/articles/s41586-025-09223-4)

生成摘要时出错

---

## 100. A Emoji Reverse Polish Notation Calculator Written in COBOL

**原文标题**: A Emoji Reverse Polish Notation Calculator Written in COBOL

**原文链接**: [https://github.com/ghuntley/cobol-emoji-rpn-calculator](https://github.com/ghuntley/cobol-emoji-rpn-calculator)

生成摘要时出错

---

