# Hacker News 热门文章摘要 (2025-05-24)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Show HN: 旋转拨号盘 Linux 内核驱动

**原文标题**: Show HN: Rotary Phone Dial Linux Kernel Driver

**原文链接**: [https://gitlab.com/sephalon/rotary_dial_kmod](https://gitlab.com/sephalon/rotary_dial_kmod)

此“Show HN”提交介绍了一个用于旋转拨号电话的 Linux 内核驱动程序。 虽然除了“正在加载”之外没有提供任何进一步的内容，但标题表明了核心思想。 该项目可能涉及：

* **Linux 内核驱动程序：** 这表明该软件旨在直接与操作系统内核交互，从而实现底层控制和集成。
* **旋转拨号电话接口：** 该驱动程序旨在解释来自旋转拨号电话的信号，将拨号盘的旋转转换为数字输入。
* **潜在用例：** 该项目暗示可以启用旋转拨号电话，将其用作 Linux 系统上的输入设备。 这可能包括控制软件、导航菜单或触发应用程序中的操作。 这是一个小众且可能是由业余爱好者驱动的项目，可能旨在重新利用旧技术并提供独特的用户界面。

在没有更多详细信息的情况下，很难指定具体的实现、支持的硬件或超出将旋转拨号盘用作 Linux 输入设备这一核心概念之外的潜在应用。“正在加载”状态表明该项目仍在进行中或演示不完整。

---

## 2. 氙气闪光灯之死：相机差点害死树莓派 2

**原文标题**: The Xenon Death Flash: How a Camera Nearly Killed the Raspberry Pi 2

**原文链接**: [https://magnus919.com/2025/05/the-xenon-death-flash-how-a-camera-nearly-killed-the-raspberry-pi-2/](https://magnus919.com/2025/05/the-xenon-death-flash-how-a-camera-nearly-killed-the-raspberry-pi-2/)

2015年2月，彼得·昂尼恩发现树莓派2的一个奇怪漏洞：在使用氙气闪光灯拍照时容易崩溃。这在树莓派论坛上引发了一场社区驱动的调查，揭示了闪光灯的高强度光会触发关机。问题追溯到U16电源稳压器芯片，该芯片使用晶圆级芯片尺寸封装 (WL-CSP)，暴露了其硅片。

暴露的硅对光电效应敏感，闪光灯的光子会产生破坏性的电子流，导致树莓派崩溃。普通的LED闪光灯没有足够的强度来触发这种情况。虽然很独特，但这个问题并非史无前例，半导体行业之前也发生过类似的光学干扰问题。

最初的临时解决方案包括用Blu-Tack等不透明材料覆盖U16芯片。然而，永久性的修复出现在硬件修订版1.2中，该版本实现了不同的电源管理架构，从而解决了这个问题。

这种“氙气死亡闪光”凸显了现代电子产品小型化和稳健性之间的矛盾。它表明，非常规的使用场景可以揭示标准测试遗漏的漏洞。该事件强调了芯片级封装的潜在风险，以及在设计中考虑光照等环境因素的重要性。树莓派基金会以透明的方式处理了这个问题，将其描述为一个“可爱的漏洞”，从而建立了社区信任。

树莓派2事件提醒我们，随着设备变得越来越复杂和互联，可能会出现意想不到的漏洞。社区协作和实验精神对于应对这些挑战至关重要。

---

## 3. 香港著名竹棚建筑，暂存。

**原文标题**: Hong Kong's Famous Bamboo Scaffolding Hangs on (For Now)

**原文链接**: [https://www.nytimes.com/2025/05/24/world/asia/hongkong-bamboo-scaffolding.html](https://www.nytimes.com/2025/05/24/world/asia/hongkong-bamboo-scaffolding.html)

本文介绍了戴思莉·朴，香港为数不多的女性竹棚架工人之一，突出了这种传统中国技艺在香港的延续。文章首先描述了朴的工作场景，展示了这项工作的高要求和潜在危险性。

31岁的朴于2021年进入这个行业，寻求在克服了个人成瘾和债务困境后的全新开始。她被对熟练工人的需求、相对较好的薪酬以及竹制建筑的独特美感所吸引。文章强调了竹棚架在香港的历史意义，以及它在中国其他地方的逐渐消失。

文章还详细描述了朴在一个男性主导的行业中所面临的挑战，包括对她能力的怀疑、不公平的待遇和身体上的艰辛。尽管面临这些障碍，她证明自己的决心和掌握这门技艺的热情依然闪耀，突出了她的韧性和对保护这项传统技艺的热情。

---

## 4. Show HN: F2 – 跨平台 CLI 批量重命名工具

**原文标题**: Show HN: F2 – Cross-Platform CLI Batch Renaming Tool

**原文链接**: [https://github.com/ayoisaiah/f2](https://github.com/ayoisaiah/f2)

F2是一款使用Go编写的跨平台命令行工具，旨在快速安全地批量重命名文件和目录。它区别于其他重命名工具的特点是：默认提供干运行模式、广泛的变量支持（包括EXIF和ID3标签等文件属性）以及全面的重命名选项，范围从简单的字符串替换到复杂的正则表达式。

F2通过验证每次重命名操作的冲突并自动解决它们来优先考虑安全性。即使在重命名大量文件时，它也具有高性能，并提供撤消功能以方便错误更正。该工具具有完善的文档，并附有实际示例。

提供了安装说明，包括使用`go install`（适用于Go开发人员）以及指向其他安装方法和预编译二进制文件的文档链接。该文档涵盖诸如入门、真实示例、内置变量、文件对重命名、使用CSV重命名、排序、冲突解决和撤消错误等主题。欢迎通过GitHub issues提交贡献、错误报告和功能请求。F2采用MIT许可证。

---

## 5. 中银舱体塔的遗产

**原文标题**: The legacy of the iconic Nakagin capsule tower

**原文链接**: [https://www.designboom.com/architecture/moma-nakagin-capsule-tower-exhibition-many-lives-museum-modern-art-new-york-05-23-2025/](https://www.designboom.com/architecture/moma-nakagin-capsule-tower-exhibition-many-lives-museum-modern-art-new-york-05-23-2025/)

纽约现代艺术博物馆(MoMA)举办“中银胶囊塔的多重生命”展览，探索黑川纪章标志性新陈代谢派建筑项目的遗产。中银胶囊塔于1972年在东京建成，2022年拆除，其最初设想是一种模块化、可再生的居住空间，可以根据需要更换单个胶囊。虽然胶囊从未真正被更换过，但在其生命周期内，该塔经历了非正式的改造，成为了画廊、DJ台和私人空间。

MoMA收藏了A1305号胶囊，并将其修复至接近原始状态，展示其模块化家具、音频控制设备和索尼彩色电视机。展览还包括40多份档案材料，如模型、传单和访谈，记录了该塔楼在过去五十年中的演变。其目的是激发人们对建筑中保护和适应的反思，超越单纯的怀旧。

展览考察了该塔楼如何通过居民主导的改造，来颠覆最初的设计。MoMA的收藏确保了曾被认为无法维护的设计的实物生存。参观者将有机会在会员活动期间亲身体验胶囊。

与展览相辅相成的是Evangelos Kotsioris撰写的一本书，详细介绍了该塔楼从概念起源到最后日子的历史。此外，与日本协会合作举办的一系列活动将为该项目提供背景，使其历史意义和对新观众的意义得到体现。展览时间为2025年7月10日至2026年7月12日。

---

## 6. 代数效应为何？

**原文标题**: Why Algebraic Effects?

**原文链接**: [https://antelang.org/blog/why_effects/](https://antelang.org/blog/why_effects/)

本文论证了在编程语言中采用代数效应（效应处理程序）的必要性，强调了它们的多功能性和超越实现常见语言功能（如生成器和异常）的优势。作者将代数效应视为可以恢复的异常，提供用户可定义的控制流，并通过启用对效应的多态函数来解决“你的函数是什么颜色”的问题。

除了引人注目的应用之外，本文还强调代数效应可以作为一种强大的抽象机制。它们可用于依赖注入，从而可以轻松地交换实现（例如，数据库、日志记录）并方便使用模拟进行测试。代数效应还可以通过隐式管理上下文对象（状态）来帮助实现更简洁的API，从而减少了显式传递的需求。

作者建议使用代数效应来替代全局变量，特别是对于需要状态管理的接口，例如随机数生成或内存分配。通过将这些关注点封装为效应，代码变得更加灵活和可维护。

最后，本文指出，与错误联合或异步函数包装器等替代方案相比，代数效应通常可以实现更直接的编码风格。虽然这里没有详细讨论（原文更长），但其他优势包括保证纯度、可重放性和基于能力的安全性。

---

## 7. Trellis (YC W24) 招聘创始销售开发代表，助力医疗保健文书工作自动化

**原文标题**: Trellis (YC W24) Is Hiring founding SDR to help automate healthcare paperwork

**原文链接**: [https://www.ycombinator.com/companies/trellis/jobs/7Ru1X1P-founding-sdr](https://www.ycombinator.com/companies/trellis/jobs/7Ru1X1P-founding-sdr)

Trellis (YC W24)，一家利用人工智能简化医疗保健文书工作的初创公司，正在招聘一位创始销售开发代表(SDR)，以推动其市场推广战略。Trellis为医疗保健提供商自动化文档导入、预先授权和申诉流程，使他们能够更快地治疗更多患者并减轻管理负担。SDR将在寻找潜在客户、筛选合格线索和执行GTM活动中发挥关键作用，并与创始人密切合作。

理想的候选人应具有以往的销售经验、积极主动的心态、出色的沟通能力以及适应快节奏环境的能力。有医疗保健行业经验者优先。职责包括管理销售渠道、创建营销内容以及确保及时跟进线索。

Trellis由YC、General Catalyst等机构支持，旨在降低医疗保健领域的管理成本，该成本目前占支出的20%以上。他们的人工智能代理将非结构化临床文档转换为EHR的结构化数据，使提供商能够将治疗时间缩短90%，提高授权率并增强药物计划的性能。该职位提供具有竞争力的薪资（6万美元-11万美元）和股权（0.10%-1.00%）。

---

## 8. 好的写作

**原文标题**: Good Writing

**原文链接**: [https://paulgraham.com/goodwriting.html](https://paulgraham.com/goodwriting.html)

好文之声：文采与思想的奇妙关联

在《好文之声》一文中，作者探讨了优美动听的文字与传达准确且深刻的思想之间令人惊讶的联系。核心论点是，这两种看似独立的品质实际上是紧密相连的。

作者认为，追求美观的散文实际上能促进更好的思考和更清晰的思想表达。这是因为修改不流畅的段落会迫使作者提炼他们的想法，就像摇晃一箱物品会导致它们更有效地排列一样。对真理的内在追求可以防止作者在专注于声音的修改过程中故意降低内容的准确性。

此外，悦耳的文字提高了可读性，使作者（作为第一读者）更容易识别其思维中的缺陷和不一致之处。这使得可以持续改进和完善潜在的思想。

这篇文章更深入地探讨，认为优美文字的节奏和流畅性不仅仅是美学品质，而且反映了思想本身的自然节奏。因此，关注文字的声音可以作为确保思想的准确性和连贯性的启发式方法。

虽然承认优美的文字可以用来传达虚假信息，但作者认为这需要有意识地努力说服自己接受错误的假设，强调了良好写作中内在一致性的重要性。最终，这篇文章得出结论，在写作中同时追求清晰和优美对于有效地发展和传达思想至关重要。

---

## 9. VS Code 中的 Postgres IDE

**原文标题**: Postgres IDE in VS Code

**原文链接**: [https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-a-new-ide-for-postgresql-in-vs-code-from-microsoft/4414648](https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-a-new-ide-for-postgresql-in-vs-code-from-microsoft/4414648)

微软发布Visual Studio Code PostgreSQL扩展公开预览版，简化数据库管理与开发。

主要功能包括：

*   **模式可视化:** 通过右键菜单轻松可视化模式。
*   **数据库感知 GitHub Copilot:** 使用自然语言命令（例如“@pgsql”）进行查询、模式优化和 SQL 操作的 AI 辅助。上下文菜单还在查询编辑器窗口中提供 AI 智能。
*   **GitHub Copilot 聊天代理模式:** 支持多阶段任务，利用工作区上下文，包括代码编写和调试（经用户授权）。
*   **简化数据库连接:** 轻松管理本地和云托管 PostgreSQL 实例的连接，包括 Azure Database for PostgreSQL 和 Docker 部署，并集成 Entra ID 实现无密码身份验证。
*   **数据库浏览器:** 用于轻松管理数据库对象的结构化视图。
*   **查询历史:** 快速访问之前运行的查询。
*   **上下文感知 IntelliSense:** 自动完成和语法突出显示，以提高查询可读性。

该扩展旨在提高生产力、简化上手流程、通过 Entra ID 提高安全性，并提供在 VS Code 中管理 PostgreSQL 数据库的全面工具集。用户需要安装 PostgreSQL、GitHub Copilot 和 GitHub Copilot Chat 扩展才能使用这些功能。

---

## 10. 展示HN：SuperUtilsPlus – Lodash 的现代替代品

**原文标题**: Show HN: SuperUtilsPlus – A Modern Alternative to Lodash

**原文链接**: [https://github.com/dhaxor/super-utils-plus](https://github.com/dhaxor/super-utils-plus)

SuperUtilsPlus：一款现代化的 Lodash 替代方案，旨在提供更优的性能、全面的 TypeScript 支持和卓越的开发者体验。其关键特性包括：完整的 TypeScript 定义、ES2020+ 兼容性、Tree-shaking 能力、零依赖、广泛的测试、超越 Lodash 的扩展功能、性能优化以及跨平台兼容性（浏览器和 Node.js）。

该库提供了一系列实用函数，分为数组、对象、字符串、函数、类型检查和随机工具等类别。文章提供了 `chunk`、`compact`、`difference`、`flatten`、`groupBy`、`get`、`deepClone`、`camelCase`、`debounce`、`isNil`、`isNumber`、`isEqual`、`random` 和 `randomUUID` 等函数的使用示例。这些示例展示了如何使用每个函数，并突出了相对于 Lodash 的潜在改进，例如更直观的 `isNumber` 和 `isObject` 类型检查。

文章强调了 Tree-shaking 的重要性，鼓励开发者仅导入必要的模块以最大限度地减少包大小。通过一个使用泛型进行类型安全访问的示例，展示了 TypeScript 的支持。最后，该库采用 MIT 许可证。文章提供了使用 npm、yarn 和 pnpm 的安装说明。

---

## 11. 现在到底什么是小型语言模型？

**原文标题**: What even is a small language model now?

**原文链接**: [https://jigsawstack.com/blog/what-even-is-a-small-language-model-now--ai](https://jigsawstack.com/blog/what-even-is-a-small-language-model-now--ai)

本文探讨了当前人工智能领域中“小型语言模型”(SLM)不断演变的定义。曾经以参数数量和在简单硬件上运行的能力来定义的SLM，现在已转变为关注可部署性和资源效率。

如今，SLM被分为以下几类：

*   **边缘优化模型：** 专为移动设备和边缘硬件设计，强调速度、低内存使用和离线功能。
*   **GPU友好模型：** 需要单个GPU，并且可以包括拥有数百亿参数的模型，适用于内部RAG管道和聊天机器人等任务。

SLM的强大之处在于它们的专业化。与通用LLM不同，SLM针对特定任务进行了优化，从而提高了准确性、效率，并更容易进行微调。示例包括总结医疗记录或解析发票。

本文强调了一个令人惊讶的事实，即即使是300亿+参数的模型，如果它们可以在没有分布式推理的情况下部署、在单个消费级GPU上运行，并且可以在没有大量基础设施的情况下进行调整，也可以被认为是“小型”的。

文章还承认了像Google Translate和AWS Textract这样的旧的、已建立的模型所发挥的作用，它们继续为日常应用程序提供支持。SLM日益增长的重要性使初创公司、开发人员和企业能够利用LLM，而无需巨额的基础设施成本，从而促进了以隐私为中心的应用程序和特定于任务的微调。

---

## 12. 人工智能连个简单的bug都修不好，却要解雇工程师。

**原文标题**: AI can't even fix a simple bug – but sure, let's fire engineers

**原文链接**: [https://nmn.gl/blog/ai-scam](https://nmn.gl/blog/ai-scam)

本文幽默地批判了关于人工智能取代工程师能力的夸大叙事，并以 GitHub Copilot 最近试图修复微软 .NET 运行时中的漏洞却频频出错为例。作者强调了人工智能的反复失败以及人类开发人员不断纠正其代码的必要性。

作者认为，目前由人工智能驱动的裁员通常只是公司解决疫情期间过度招聘问题的便捷借口，让他们看起来更具创新性，而不是承认计划不周。

作者承认人工智能作为编码工具的有用性，但同时强调了它的局限性，并倡导开发人员成为团队内部的人工智能专家。他们鼓励开发人员记录人工智能的不足之处，公开分享他们在人工智能方面的真实经验，并强调人机协作的力量，以塑造对人工智能能力更为现实的理解。

文章最后建议，如果首席执行官认真考虑由人工智能驱动的裁员，开发人员应该更新简历，不是因为人工智能会取代他们，而是因为这表明他对人工智能目前的局限性存在误解。作者敦促读者将人工智能视为增强人类潜力的工具，而不是取代人类专业知识的替代品。

---

## 13. 找到你的同伴

**原文标题**: Find Your People

**原文链接**: [https://foundersatwork.posthaven.com/find-your-people](https://foundersatwork.posthaven.com/find-your-people)

在巴克内尔大学2025届毕业典礼上的这篇演讲稿，为毕业生们提供了毕业后寻找雄心壮志和人生目标的建议。演讲者回顾了自己大学毕业后漫无目的的经历，为那些缺乏明确规划的人提出了一项策略。

他强调，毕业标志着结构化的“火车轨道”生活的结束和未知领域的开始。虽然这令人望而却步，但这种自由也带来了重新塑造自己的机会。他鼓励毕业生们摆脱基于过去表现的任何自我限制性信念，拥抱新的好奇心和雄心壮志。

关键在于积极寻找感兴趣的职业道路，并意识到选择之多令人应接不暇。他倡导利用人脉关系，而不是漫无目的地陷入不满意的职业：与人交谈，获得引荐，并了解他们的热情所在。找到合适的人和支持性的环境至关重要。

最后，演讲者强调了培养对拒绝的免疫力的重要性。追求雄心勃勃的目标往往会招致怀疑，因此必须忽略消极情绪并坚持不懈。他以最初被认为是个笑话的 Y Combinator 为例，说明了开创性的想法最初看起来可能显得愚蠢。简而言之，掌控自己的方向，从他人那里寻求灵感，不要让挫折阻碍你的雄心壮志。

---

## 14. 远 - 卓越的启发式查找和替换

**原文标题**: Far – Sublime Inspired Find and Replace

**原文链接**: [https://github.com/ibilalkayy/far](https://github.com/ibilalkayy/far)

`far` 是一个命令行工具，旨在快速灵活地在文件和文件夹中搜索和替换文本。它受到 Sublime Text 查找和替换功能的启发，提供搜索、替换、使用 glob 模式指定目标文件/目录、智能大小写（例如，保留大小写转换）以及计划中的试运行模式等功能。

该工具可以使用 `git clone` 安装，然后导航到克隆的目录，并使用 `cargo build --release` 构建。基本用法包括指定要查找的文本（`--find`）、替换文本（`--replace`）和目标文件或目录（`--target`），例如使用像 "./src/**/*.rs" 这样的 glob 模式来定位 Rust 文件。

`far` 基于 Apache-2.0 许可证授权，鼓励以拉取请求和建议的形式进行贡献。

---

## 15. 小公司，就要有个小公司的样子。

**原文标题**: You're a little company, now act like one

**原文链接**: [https://longform.asmartbear.com/little-company/](https://longform.asmartbear.com/little-company/)

杰森·科恩认为，小公司常犯的一个错误是试图塑造“大公司”形象，认为这会吸引更多客户。然而，这种做法实际上疏远了他们的理想早期客户：早期采用者。

早期采用者喜欢新的，甚至是存在缺陷的技术，并享受与创始人的密切关系、对产品开发的直接影响以及采用尖端解决方案所获得的竞争优势。如果他们能得到关注和快速修复，他们愿意容忍不完善之处。

科恩强调，小公司应该拥抱自己的规模，并迎合这一特定市场。试图模仿大型企业，采用通用的营销语言和过度润色的演示文稿对早期采用者毫无吸引力。相反，公司应该展示他们的热情、可及性和合作意愿。

文章建议小公司在信息传递方面做到真实、具体和人性化。这意味着突出他们对客户痛点的理解，推广他们的论坛和开放沟通渠道，并展示他们对客户反馈的奉献精神。通过停止隐藏并公开拥抱他们的小公司身份，他们可以吸引那些会支持他们的产品并为其发展做出贡献的早期采用者。目标不是立即从大型公司获得大量订单，而是培养与那些能够帮助为未来成功奠定坚实基础的人建立关系。

---

## 16. 人工智能、海德格尔与新世纪福音战士

**原文标题**: AI, Heidegger, and Evangelion

**原文链接**: [https://fakepixels.substack.com/p/ai-heidegger-and-evangelion](https://fakepixels.substack.com/p/ai-heidegger-and-evangelion)

无法访问文章链接。

---

## 17. 木星曾经是现在两倍大，并拥有更强的磁场。

**原文标题**: Jupiter was formerly twice its current size, had a much stronger magnetic field

**原文链接**: [https://phys.org/news/2025-05-jupiter-current-size-stronger-magnetic.html](https://phys.org/news/2025-05-jupiter-current-size-stronger-magnetic.html)

Science X 的这篇文章详细介绍了一项发表在《自然·天文学》上的新研究，该研究揭示了木星早期演化的奥秘。研究人员 Konstantin Batygin 和 Fred C. Adams 计算得出，在太阳系中第一个固体形成大约 380 万年后，木星的体积是现在的两倍，并且拥有比今天强 50 倍的磁场。

该研究侧重于木星卫星阿马尔忒亚和底比斯轨道上的差异，以独立确定木星的原始大小和磁场强度，从而绕过了传统行星形成模型中的不确定性。这项分析确立了木星在太阳星云蒸发这一关键时刻的状态快照，标志着行星建造材料的结束和太阳系初始结构的巩固。

这些发现通过提供木星在早期阶段的大小、自旋速率和磁场条件的具体测量，完善了现有的关于巨行星形成的核吸积理论。 这些结果为理解木星乃至整个太阳系的演化提供了一个有价值的基准。

---

## 18. 禁用进程中的内核函数 (2009)

**原文标题**: Disabling kernel functions in your process (2009)

**原文链接**: [https://chadaustin.me/2009/03/disabling-functions/](https://chadaustin.me/2009/03/disabling-functions/)

这篇2009年的文章探讨了一种解决第三方库（Direct3D和Flash）干扰应用程序未处理异常过滤器，导致崩溃报告失效问题的技术。作者描述了这些库如何重复安装自己的异常过滤器，覆盖应用程序的过滤器。

实现的解决方案包括直接修改`kernel32.dll`中的`SetUnhandledExceptionFilter`函数的代码，在应用程序安装了自己的处理程序后有效地禁用它。这可以防止其他库劫持异常处理机制。

文章提供了C++代码，用于使用`GetProcAddress`定位`SetUnhandledExceptionFilter`，验证其初始代码（常见的函数序言），然后用一段简单返回0的代码覆盖它，从而有效地使该函数成为一个空操作。该代码使用`VirtualProtect`更改内存保护，并使用`FlushInstructionCache`来确保执行修改后的代码。

作者承认代码修改本质上是“黑魔法”，但将其证明为解决特定问题的实用方法。文章的评论讨论了较新Windows版本中可能出现的问题、对其他进程的影响以及使用Detours等库进行IAT Hooking等替代方法。

---

## 19. 为你的朋友加油

**原文标题**: Root for your friends

**原文链接**: [https://josephthacker.com/personal/2025/05/13/root-for-your-friends.html](https://josephthacker.com/personal/2025/05/13/root-for-your-friends.html)

约瑟夫·“rez0”·萨克的博客文章《为你的朋友喝彩》倡导积极支持和庆祝朋友的成功。其核心理念是培养一种兴奋和慷慨的心态，拒绝嫉妒，并认识到生活的正和博弈本质。

萨克介绍了“助威者”或“热情的朋友”的概念，即那些热情地为你欢呼的人。他解释了“助威者飞轮”——一个积极的反馈循环，即支持你的朋友会带来他们的成功，进而通过共享信息和机会使你受益。但他指出，这个飞轮需要互惠。

文章提供了识别会为你喝彩的朋友的指导，列出了诸如诚实的反馈与真诚的赞扬相结合、持续的祝贺、积极推广你的工作以及协作心态等特征。它还提供了关于*如何* *成为* 助威者的可行步骤，包括随时提供赞扬、提供建设性的批评、通过分享相关想法来扩展他们的视野，以及积极推广他们的工作。

最终，萨克认为，为你的朋友喝彩不仅对他们有益，而且通过消除嫉妒和培养更牢固的关系来改善你自己的幸福感。他最后鼓励读者采纳这种心态，并与他人分享这一信息。

---

## 20. DumPy：NumPy，但即使你很笨也能用

**原文标题**: DumPy: NumPy except it's OK if you're dum

**原文链接**: [https://dynomight.net/dumpy/](https://dynomight.net/dumpy/)

本文介绍了“DumPy”，一种旨在简化数组操作并降低认知负担的NumPy替代方案。作者认为，NumPy的复杂性源于其试图通过将循环逻辑推入单个函数来处理高维数组，从而迫使用户不断管理数组形状和规则。

DumPy的核心思想是接受循环和索引的语法，同时秘密地将其编译成向量化操作，从而消除了为每个函数手动操作数组维度的需要。它使用“映射”数组系统，其中使用字符串或`dp.Range`进行索引会创建假装具有较少维度的数组。然后，DumPy函数根据这些映射维度中的共享标签自动向量化计算。这种向量化由jax.vmap提供支持，jax.vmap是一个已经可用于向量化类似NumPy函数的工具。

本文展示了各种复杂程度的示例问题（希尔伯特矩阵、批量协方差、移动平均、索引、高斯密度、多头自注意力），比较了循环、NumPy、JAX（带vmap）和DumPy中的实现。作者认为，DumPy的语法比NumPy、JAX的vmap和传统循环更直观，更容易理解。`dp.Range`对象还通过同时充当字符串和映射数组来简化创建希尔伯特矩阵等任务。本文强调DumPy本身并不聪明；它的优势在于它拒绝不必要的复杂性。

---

## 21. 日本PC-98电脑的世界

**原文标题**: The world of Japan's PC-98 computer

**原文链接**: [https://strangecomforts.com/the-strange-world-of-japans-pc-98-computer/](https://strangecomforts.com/the-strange-world-of-japans-pc-98-computer/)

文章《日本PC-98电脑的奇异世界》详细介绍了NEC PC-98系列在20世纪80年代初至90年代中期在日本个人电脑市场的统治地位，而在此期间，IBM PC兼容机在世界其他地区占据主导地位。PC-98通过多种因素确立了自己的标准，包括卓越的图形处理能力，尤其是在日文文本和游戏方面，以及日本软件开发商的强大支持。

文章强调了PC-98和IBM PC之间的架构差异，包括其专有的16位架构和专用图形硬件的使用。这种差异创造了一个独特的生态系统，其中包含大量专门为PC-98量身定制的游戏和应用程序。许多标志性的日本游戏开发商，如Falcom、Enix和Square，都严重依赖PC-98的功能，从而开发出在图形上更胜一筹且具有独特视觉风格的游戏，与西方游戏相比。

然而，文章也指出了PC-98最终衰落的原因。Windows的崛起，以及IBM PC兼容机日益增长的经济性和可访问性，逐渐侵蚀了PC-98的市场份额。尽管NEC试图适应，但专有架构和遗留软件库仍然难以克服。尽管最终衰落，PC-98在日本计算机历史上留下了重要的印记，尤其是在游戏领域，并且即使在今天仍然拥有狂热的追随者。它代表了个人计算一个引人入胜的另类历史，在这种历史中，不同的标准在特定的文化背景下蓬勃发展。

---

## 22. 孤身漂流太平洋

**原文标题**: Alone and Adrift in the Pacific

**原文链接**: [https://www.theatlantic.com/magazine/archive/2025/06/commercial-fisherman-shipwreck/682580/](https://www.theatlantic.com/magazine/archive/2025/06/commercial-fisherman-shipwreck/682580/)

文章讲述了一个年轻人的渔船之旅变成太平洋上绝望求生的惊险故事。叙述者为了寻求冒险并摆脱在加州漫无目的的生活，在名为“黄昏号”的渔船上找到了一份工作，船长是一个名叫米克的人。他们开始了本应是华盛顿州海岸附近的一次短期训练航行。

第二天，一场风暴加剧，“黄昏号”开始下沉。叙述者发出了求救信号，但米克毫无反应。叙述者被迫弃船，在一条小救生筏上避难，而米克留在船上，随着船一起沉没。

孤身一人，漂流不定，叙述者面临着日益减少的补给、无情的风暴以及孤立无援的巨大压力。他详细描述了自己与饥饿、寒冷以及独自在海上所造成的心理压力的斗争。他定量分配有限的食物和水，试图用信号弹发出求救信号，并与绝望作斗争。他养成了检查地平线、舀水和祈祷救援的习惯。他反思了与父母之间紧张的关系、过去的抉择以及导致他陷入这种危险境地的鲁莽行为。这个故事为接下来不顾一切地求生奠定了基础。

---

## 23. Show HN: HNRelevant – 在 Hacker News 上添加“相关”部分

**原文标题**: Show HN: HNRelevant – Add a "related" section to Hacker News

**原文链接**: [https://github.com/imdj/HNRelevant](https://github.com/imdj/HNRelevant)

HNRelevant：为 Hacker News 增加“相关”板块，帮助用户发现他们可能错过的相关且有趣的讨论。它基于当前页面的标题，利用 HN Algolia 搜索 API，提供一个即时相关的提交列表。用户可以直接在扩展程序中自定义搜索查询，以查找更具体的内容。

该扩展程序与 Hacker News 的设计无缝集成，看起来就像一个原生功能。它提供两种操作模式：自动（页面打开时加载结果）和手动（按需获取结果）。用户还可以通过扩展程序的弹出菜单自定义默认设置。

HNRelevant 可在 Chrome、Firefox（桌面和 Android）和 Microsoft Edge 上使用。它也可以作为用户脚本安装，通过 Tampermonkey、Violentmonkey 或 Greasemonkey 等扩展程序支持更广泛的浏览器。用户脚本文件 (HNRelevant.user.js) 可以直接加载到所选的用户脚本管理器中。该项目以 MIT 许可证发布。

---

## 24. 我为什么不在我的HTTPS站点上使用传统证书了

**原文标题**: Why I no longer have an old-school cert on my HTTPS site

**原文链接**: [https://rachelbythebay.com/w/2025/05/22/ssl/](https://rachelbythebay.com/w/2025/05/22/ssl/)

无法访问文章链接。

---

## 25. 展示 HN：遗传 Boids 网页模拟

**原文标题**: Show HN: Genetic Boids Web Simulation

**原文链接**: [https://attentionmech.github.io/genetic-boids/](https://attentionmech.github.io/genetic-boids/)

此“Show HN”帖子介绍了 GeneticBoids，一个由 @attentionmech 开发的 Web 模拟程序，它通过遗传算法视角探索蜂拥行为。该模拟允许用户操纵影响 Boids 运动、蜂拥倾向（对齐、分离、凝聚力）、感知范围、寿命和遗传信号的各种参数。

主要特性和可调整的参数包括：

*   **群体：** 控制 Boids 的数量，并提供 Minimal、Medium 和 Standard 等预设。
*   **运动：** 调整最大速度、力以及初始速度范围。
*   **蜂拥行为：** 修改对齐、分离和凝聚力的权重，以及它们各自的感知范围。
*   **老化：** 设置 Boids 的寿命。
*   **遗传信号：** 试验信号概率、范围和力，从而影响 Boids 之间的通信。 基因组的长度也可以调整。
*   **视觉：** 自定义 Boid 大小、信号线可见性和背景颜色。
*   **性能：** 通过更改网格单元大小和帧速率目标来优化模拟。

Calm、Chaotic、Swarm、Signal Heavy 和 Minimal 等预设提供了快速入门点。 其他选项包括随机化、清除 Boids 以及“Explode!”功能。 该模拟还显示实时统计数据，包括 FPS、活动信号、平均速度和集群计数。 用户可以通过提供的链接在 GitHub 上访问该项目。 本质上，GeneticBoids 提供了一个沙盒环境，用于探索受传统蜂拥规则和个体代理之间遗传通信影响的涌现行为。

---

## 26. 我在Carta学到的东西

**原文标题**: Stuff I Learned at Carta

**原文链接**: [https://lethain.com/stuff-learned-at-carta/](https://lethain.com/stuff-learned-at-carta/)

Carta卸任CTO告别信：两年任期关键心得反思。中心主题是转向精细化参与，反对仅仅依赖高层抽象。他强调策略测试和领域专业知识发展，这得益于Carta的领导风格。

他详细阐述了其工程战略方法的改进，最终将以他在Carta的实践经验为基础出版一本书。另一个关键收获围绕着积极理解高层沟通，强调员工破译潜在模糊信息的权力。

他强调Carta在重要工作流程中早期采用LLM，标志着在高层领导职位上经历的重大技术转型。文章还涵盖了在决策中权衡多维度利弊的重要性，这是他在职期间正式确立的一个概念。

他推崇高级工程师的Navigator项目，确保直接代表和情境意识，尤其有利于拥有100多名工程师的公司。他还提到他对软件质量的理解发生了演变，承认某些系统的“高度本质复杂性”。

最后，CTO详细介绍了管理工程成本的见解，强调了诸如N-1替补、基于理由的晋升和具有成本效益的招聘区域等策略。他还谈到如何以简洁易懂的方式向董事会解释研发投资。

最后，他表达了对在Carta共事的人们的感谢，强调了人际关系在任何职位中的重要性。

---

## 27. 如何在美國每月靠432美元生活

**原文标题**: How to live on $432 a month in America

**原文链接**: [https://shagbark.substack.com/p/how-to-live-on-432-a-month-in-america](https://shagbark.substack.com/p/how-to-live-on-432-a-month-in-america)

无法访问文章链接。

---

## 28. 凯撒之死

**原文标题**: Caesar's Last Breath

**原文链接**: [https://charliesabino.com/caesars-last-breath/](https://charliesabino.com/caesars-last-breath/)

本文通过计算我们每次呼吸吸入的凯撒最后一口气所含分子数量的思维实验，探讨了费米估算的概念。令人惊讶的近似答案是一个分子。

作者解释说，这是由于每次呼吸中包含的分子数量巨大以及空气在整个大气层中长期广泛扩散所致。为了得出这个结论，本文引导读者完成一个费米估算过程，强调了“草稿纸数学”在估算数量方面的强大作用。

该估算包括计算地球大气层的体积（约 5 x 10^18 立方米）和典型呼吸的体积（约 5 x 10^-4 立方米）。 这允许计算单次呼吸占大气层的比例。然后，确定一次呼吸中的分子数量（约 10^22 个分子）允许确定平均一次呼吸中存在多少凯撒最后一口气分子。

本文强调了费米估算作为一项宝贵技能在各个领域的实用性，并提及了其在软件工程和其他领域的应用。 最后，它提供了资源，供进一步实践和探索费米估算技术。

---

## 29. 展示一下：我构建了一个更高效的AI聊天管理方式

**原文标题**: Show HN: I built a more productive way to manage AI chats

**原文链接**: [https://contextch.at](https://contextch.at)

无法访问文章链接。

---

## 30. DIY网络眩晕疗法

**原文标题**: DIY Cybersickness Remedies

**原文链接**: [https://spectrum.ieee.org/diy-cybersickness-remedies](https://spectrum.ieee.org/diy-cybersickness-remedies)

DIY杂志的文章《通过自黑来改善VR体验》探讨了对抗虚拟现实中的网络晕动症的简单自制技巧。这篇文章由心理学讲师Matthew Coxon撰写，认为网络晕动症源于VR体验模拟与我们身体实际体验之间的感知差异。

文章承诺提供三种具体技巧，这些技巧可能减少这些感知差距，从而缓解恶心。虽然根据提供的文本，本摘要中没有详细说明具体技巧，但总体前提是用户可以主动影响他们的VR体验，以提高舒适度并降低网络晕动症的可能性。这篇文章旨在提供实用的、用户可以实施的解决方案，而不是仅仅依赖于硬件或软件调整。目标受众很可能是寻求增强体验并减轻网络晕动症不适影响的VR用户。文章的发表日期（2025年5月23日）表明VR技术已经相对先进和普及。

---

## 31. Show HN: DoubleMemory – 更高效的本地优先稍后阅读应用

**原文标题**: Show HN: DoubleMemory – more efficient local-first read-it-later app

**原文链接**: [https://doublememory.com](https://doublememory.com)

此“Show HN”提交介绍DoubleMemory，一款本地优先的“稍后阅读”应用程序，旨在高效保存和组织文章及在线内容。其关键在于对**本地优先架构**的关注，意味着所有数据都存储在用户设备上，而非云端，从而提升隐私性和离线访问能力。

虽然从提供的标题和介绍性文字中细节不多，但我们可以推断DoubleMemory可能提供稍后阅读应用程序的常见核心功能，例如：

*   **保存文章：** 用户可以保存文章、链接和其他在线内容以供稍后阅读。
*   **组织：** 该应用程序可能提供用于组织已保存内容的工具，可能包括标签、文件夹或搜索功能。

强调的方面“更高效”表明DoubleMemory通过以下方式区分自己：

*   **性能：** 与其他类似应用程序相比，可能具有更快的保存和检索速度。
*   **资源使用：** 可能更有效地利用设备存储空间或电池。

总而言之，DoubleMemory是一款本地优先的稍后阅读应用程序，专注于效率，承诺以一种私密且可访问的方式保存和组织在线内容以供稍后使用。“更高效”的强调意味着与现有解决方案相比，在速度、存储或其他资源使用方面的改进。

---

## 32. Show HN: Lnk – 基于 Git 的 dotfiles 管理器

**原文标题**: Show HN: Lnk – Git-native dotfiles manager

**原文链接**: [https://github.com/yarlson/lnk](https://github.com/yarlson/lnk)

Lnk：一款Git原生的dotfiles管理器，旨在提供简洁易用的体验。Lnk 不采用复杂的配置，而是将你的 dotfiles 移动到 `~/.config/lnk`，创建指向其原始位置的符号链接，并允许你使用标准的 Git 命令来管理它们。

主要功能包括：

*   **简单设置：** 通过 `curl` 或 Homebrew 快速安装，轻松初始化新的或现有的 Git 仓库。
*   **Git 原生工作流：** 使用熟悉的 Git 命令，如 `add`、`status`、`push` 和 `pull`。
*   **自动化任务：** 自动化移动文件、创建符号链接、处理冲突和跟踪管理的文件，从而减少手动操作。
*   **主要命令：** `lnk init`，`lnk add`，`lnk rm`，`lnk status`，`lnk push`，`lnk pull`。
*   **技术优势：** 单个二进制文件，原子操作，相对符号链接，XDG 兼容性和集成测试。
*   **替代方案：** 突出了其他 dotfiles 管理器，如 chezmoi、yadm、dotbot 和 stow，将 Lnk 的极简复杂性与它们的功能进行对比。

Lnk 优先考虑直接的工作流程，允许用户利用 Git 的强大功能来管理 dotfiles，而无需手动配置或复杂的工具。 该项目包含全面的测试并被积极使用，尽管在 1.0 版本之前不保证 API 稳定性。

---

## 33. 位置偏好、顺序效应和提示敏感性会削弱人工智能的判断力

**原文标题**: Positional preferences, order effects, prompt sensitivity undermine AI judgments

**原文链接**: [https://www.cip.org/blog/llm-judges-are-unreliable](https://www.cip.org/blog/llm-judges-are-unreliable)

本文强调，由于各种认知偏差和漏洞，在敏感领域使用大型语言模型（LLM）进行决策的不可靠性。文章认为，LLM表现出与人类认知相似的偏差，包括位置偏好、顺序效应和对提示语措辞的敏感性，导致不可预测和不一致的判断。

作者展示了对各种LLM进行的测试的证据，表明提示语措辞、标签选择（例如，“回复A/B”）或评估标准的顺序的微小变化如何显著改变结果。他们发现，LLM通常偏爱成对选择中的第二个选项，在评分中表现出近因偏见，并且难以完成需要评估负面特征的任务。旨在消除模型偏差的系统提示有时反而会加剧这些偏差。

文章强调，由于其架构和训练数据的复杂性，LLM缺乏传统计算机程序的确定性精度。文章为减轻这些偏差提供了建议，包括使用中性标签、改变项目顺序、验证提示组件、优化评分机制、采用稳健的排名方法、设计清晰的分类模式以及多元化模型组合。

作者警告说，在不了解LLM偏差的情况下，不要仅仅依赖LLM在高度相关的领域，并提倡使用工具来系统地测试和量化这些偏差。他们还警告说，不要假设LLM的共识或集成固有地减轻了偏差，因为这些方法可能会强化共享的系统性错误。

---

## 34. 展示 HN：使用激光雷达数据进行高分辨率表面分析

**原文标题**: Show HN: High-resolution surface analysis with Lidar data

**原文链接**: [https://github.com/r-follador/delta-relief](https://github.com/r-follador/delta-relief)

此“Show HN”帖子介绍delta-relief项目，旨在提高高分辨率SwissTopo LiDAR数据的可访问性，以便更轻松地解释地形变化，尤其是在考古应用方面。 该项目将LiDAR数据可视化为图像，突出显示细微的地形变化，并将其部署在交互式、移动友好的在线地图 (lidar.cubetrek.com) 中，适用于瑞士东部（格劳宾登州北部）。

其核心思想是处理LiDAR数据（最初由绝对海拔值组成），以便专注于检测细微的地形变化。 该项目计算每个点的坡度（一阶导数），并应用非线性变换来放大精细的梯度，同时保持更广泛的特征。 第二阶导数和颜色映射的实验效果不佳。

在线地图允许用户通过GPS平移到他们的位置，并在LiDAR衍生的、航拍的和标准地图视图之间切换。 该帖子重点介绍了使用LiDAR数据在格劳宾登州北部识别出的特定考古遗址，包括Colm La Runga（罗马营地遗迹）、Rohanschanze（罗翰的防御工事）和Cresta聚落（青铜时代）。

在技术上，该项目使用mbtileserver来托管MapLibre JS的地图切片。 工作流程包括从SwissTopo下载GeoTIFF，使用自定义脚本将海拔数据转换为基于坡度的可视化数据，使用GDAL生成mbtiles（具有从LV95到Web Mercator的坐标系转换），并使用NGINX作为反向代理。

---

## 35. 米制起源于法国大革命

**原文标题**: The metre originated in the French Revolution

**原文链接**: [https://www.abc.net.au/news/science/2025-05-20/metre-treaty-anniversary-metric-system-measurement-metrology/105302024](https://www.abc.net.au/news/science/2025-05-20/metre-treaty-anniversary-metric-system-measurement-metrology/105302024)

本文详细介绍了米的单位历史，追溯其起源于法国大革命时期，当时革命者寻求一种基于自然而非任意标准的通用测量系统。最初，米被定义为从北极经巴黎到赤道距离的一千万分之一，后来用一根铂金杆“档案米原器”来具体代表。

随着科学的进步，这个物理标准被基于光的定义所取代，先是使用氪-86发射的光的波长，然后在1983年，将米定义为光在真空中1/299,792,458秒内传播的距离。这个最终定义与光速相关联，允许进行高度精确的测量，例如确定到月球的距离。

本文还提到了《米制公约》，这是一项于1875年签署的条约，该条约建立了国际计量局以标准化测量。虽然包括澳大利亚在内的许多国家都采用了公制，但美国在日常生活中仍主要使用英制单位，尽管公制已获得法律认可。本文强调了仍然存在的不一致之处，即使在采用了公制的国家，例如烹饪食谱中不同汤匙的测量值。

---

## 36. 丢番图方程复杂度界的形式化证明

**原文标题**: A Formal Proof of Complexity Bounds on Diophantine Equations

**原文链接**: [https://arxiv.org/abs/2505.16963](https://arxiv.org/abs/2505.16963)

题为“丢番图方程复杂度界限的形式化证明”的论文，在Isabelle/HOL中形式化地构建了具有有界复杂度的丢番图方程。该工作由Jonas Bayer和Marco David撰写，是对他们数论研究的形式化验证，旨在寻找一个通用对 (ν, δ)，表示变量的数量和次数，使得相应的丢番图方程类是不可判定的。这与希尔伯特第十问题相关，该问题已被Matiyasevich对整数解否定，但对于有理数和有界复杂度的情况仍然悬而未决。

该论文的贡献在于形式化地验证了建立整数未知数通用对所需的主要构造。这涉及扩展Isabelle形式化证明档案库 (AFP) 中关于多元多项式的条目，形式化数论教科书的相关部分，并在Isabelle中开发丢番图方程理论。该工作还结合了用于管理复杂多项式定义的元编程基础设施。

作者强调数学研究与形式化验证之间的密切合作，定理证明器Isabelle在正在进行的数学开发过程中提供了宝贵的帮助。该论文详细介绍了数学家和计算机之间这种不常见但有希望的协同作用。该论文共16页，包含一个图。

---

## 37. 喜剧演员购入新泽西房产，拯救模型铁路

**原文标题**: A Comedian Saves a Model Railroad with Purchase of a New Jersey Home

**原文链接**: [https://www.wsj.com/lifestyle/model-railroad-james-murray-ac709a96](https://www.wsj.com/lifestyle/model-railroad-james-murray-ac709a96)

无法访问文章链接。

---

## 38. 一颗珠子引发的思考：哥伦布之前的全球联系

**原文标题**: A Bead Too Far: Rethinking Global Connections Before Columbus

**原文链接**: [https://peterfrankopan.substack.com/p/a-bead-too-far-rethinking-global](https://peterfrankopan.substack.com/p/a-bead-too-far-rethinking-global)

无法访问文章链接。

---

## 39. UndoDB – Linux C/C++ 交互式时间旅行调试器

**原文标题**: UndoDB – The interactive time travel debugger for Linux C/C++ for debugging

**原文链接**: [https://undo.io/](https://undo.io/)

无法访问文章链接。

---

## 40. 如何以写作为生

**原文标题**: How to Make a Living as a Writer

**原文链接**: [https://thewalrus.ca/how-to-make-a-living-as-a-writer/](https://thewalrus.ca/how-to-make-a-living-as-a-writer/)

本文记录了作者作为自由撰稿人为生计奋斗的历程，着重讲述了所遇到的挑战和意想不到的机遇。作者毕业于创意写作专业后，最初面临着从事更传统职业的压力，选择继续读研，但因罹患慢性神经系统疾病，身体机能受限，被迫辍学。

由于无法从事许多传统工作，她开始从事自由职业，撰写文章和散文，但由于收入不稳定和稿件被采用率不高，很难维持生计。这促使她接受了“马新闻”这份工作，为一家声誉管理公司编写每日赛马信息简报，尽管对这项运动本身存在道德担忧，但这份工作提供了急需的稳定性。

为了补充收入，作者承担了各种“零工”，包括撰写Instagram文案、银行网站内容以及回顾《单身女郎》的剧集。文章最终以她开始为一款互动应用程序创作情色作品而告终，尽管报酬微薄，工作量繁重。作者强调，为了在不可预测的自由撰稿世界中维持生计，需要不断地追求工作。本文强调了持续的奔波、对非常规项目的接受以及作为作家为财务稳定而奋斗的过程。

---

## 41. 编写任务执行器（Elixir）（再次）（十年之后）

**原文标题**: Writing A Job Runner (In Elixir) (Again) (10 years later)

**原文链接**: [https://github.com/notactuallytreyanastasio/genstage_tutorial_2025/blob/main/README.md](https://github.com/notactuallytreyanastasio/genstage_tutorial_2025/blob/main/README.md)

这篇名为`genstage_tutorial_2025`、题为“（再次）用Elixir编写一个任务运行器（10年后）”的基于Elixir的文章，看起来是一个关于创建任务运行器的教程，可能回顾并更新了十年前的方法。作者“notactuallytreyanastasio”已将该代码仓库公开。

其核心含义是，这篇文章将探讨使用Elixir，并可能使用`GenStage`行为或其现代等价物，来构建一个用于管理和执行异步任务的系统。“（10年后）”这一方面表明作者可能会将现代技术和库与较旧的方法进行对比，可能突出效率、可伸缩性或开发者体验方面的改进。

它是一个教程的事实表明它采用了一种实用的、动手的方法，旨在指导读者从头开始构建一个功能正常的任务运行器。GitHub仓库的存在进一步表明有配套的代码示例可用。

该代码仓库已获得少量关注（3个fork和45个star），这表明它可能对希望了解任务处理模式的Elixir开发者来说是一个有用的资源。该仓库的名称也强烈表明它是一个关于`GenStage`的教程，`GenStage`是Elixir中用于构建管道的行为。

---

## 42. 大型强子对撞机束流吸收器的解剖

**原文标题**: Autopsy of an LHC Beam Dump

**原文链接**: [https://home.cern/news/news/accelerators/autopsy-lhc-beam-dump](https://home.cern/news/news/accelerators/autopsy-lhc-beam-dump)

本文详细介绍了欧洲核子研究中心（CERN）首次进行的LHC放射性束流倾卸器的“解剖”分析，旨在了解其运行十年后的材料退化情况，特别是氮气泄漏问题。内窥镜检查发现挤压石墨圆盘存在裂缝，因此需要更多信息来为LHC和HL-LHC未来的束流倾卸器设计提供参考。

由于放射性，研究人员开发了远程控制技术，利用自动化圆锯和机械臂切割倾卸器的双相不锈钢合金外壳。“解剖”分析显示，虽然挤压石墨圆盘出现裂缝，但低密度和高密度石墨的状况良好。

结果验证了LHC第三次运行中使用低密度和高密度石墨的可行性，但排除了挤压石墨用于未来备用倾卸器设计的可能性。目前正在HiRadMat设施进行进一步测试，以探索HL-LHC束流倾卸器的新材料。预计对现有LHC束流倾卸器的改进将提高其在第三次运行中的抗压性，尽管能量水平有所提高。这次“解剖”分析为极端条件下的材料性能提供了宝贵的见解，为未来的束流倾卸器设计提供信息，并确保LHC的安全运行。

---

## 43. 降低对乙酰氨基酚肝毒性并提高药效的改造

**原文标题**: Modification of acetaminophen to reduce liver toxicity and enhance drug efficacy

**原文链接**: [https://www.societyforscience.org/regeneron-sts/2025-student-finalists/chloe-lee/](https://www.societyforscience.org/regeneron-sts/2025-student-finalists/chloe-lee/)

17岁的李 Chloe 研究改良对乙酰氨基酚（泰诺），以降低其肝毒性，同时保持或增强其止痛效果。对乙酰氨基酚用途广泛，但却是美国肝功能衰竭和全球肝移植的主要原因之一。Chloe专注于对乙酰氨基酚分子的苯环进行化学修饰。

她利用计算机建模评估了这些修饰分子的止痛和毒性潜力。她的研究鉴定并合成了一种新的、经过修饰的对乙酰氨基酚分子，该分子显示出比原始分子毒性更低、止痛效果可能更有效的潜力。这种新分子代表了开发更安全、更有效的对乙酰氨基酚配方的一个潜在的第一步。

除了科学研究之外，Chloe还是她高中管弦乐队的主席、大达拉斯青年交响乐团的第一小提琴手以及STEM领域女孩俱乐部的创始人/主席。她还是一位屡获殊荣的小提琴家，教授小提琴并为老年人表演。

---

## 44. 超越语义：无理性中间令牌的非理性有效性

**原文标题**: Beyond Semantics: Unreasonable Effectiveness of Reasonless Intermediate Tokens

**原文链接**: [https://arxiv.org/abs/2505.13775](https://arxiv.org/abs/2505.13775)

超越语义：无理性中间令牌的非凡有效性

---

## 45. Mermaid：从文本生成流程图或时序图等图表

**原文标题**: Mermaid: Generation of diagrams like flowcharts or sequence diagrams from text

**原文链接**: [https://github.com/mermaid-js/mermaid](https://github.com/mermaid-js/mermaid)

Mermaid 是一种基于 JavaScript 的图表绘制工具，它从类似 Markdown 的文本生成图表。 它的目标是通过轻松创建和修改图表来缓解“文档腐烂”问题，使文档能够跟上开发进度。 它提供了一个在线编辑器，并支持与各种应用程序（包括 GitHub）的集成。

Mermaid 支持各种图表，包括流程图、时序图、甘特图、类图、状态图、饼图、Git 图、条形图、用户旅程图和 C4 图。 这些图表可以使用简单的基于文本的语法创建。

该项目赢得了 2019 年 JS 开源奖。 它依赖于 d3 和 dagre-d3 等开源项目进行图形布局。

出于安全考虑，Mermaid 提供了一个沙盒化的 iframe 渲染选项，以防止恶意 JavaScript 执行，这对于拥有外部用户的站点尤其有用。 漏洞可以报告给 security@mermaid.live。

该项目欢迎贡献，并提供贡献指南。 它还感谢主要贡献者及其依赖的开源库。

---

## 46. 最高的木制风力涡轮机

**原文标题**: Tallest Wooden Wind Turbine

**原文链接**: [https://modvion.com/](https://modvion.com/)

这家公司用木材而非传统材料（如钢铁或混凝土）建造风力涡轮机塔架，本文重点介绍了这一点。其主要信息是，他们的木结构建造方法能够实现净零风电。这表明使用木材显著减少了建造和运营风力涡轮机相关的碳足迹，从而有助于实现更可持续的能源。本文含蓄地提出了诸多益处，例如可再生材料来源、潜在的更低制造排放以及与传统风力涡轮机塔架材料相比，可能的报废处置优势。“了解其运作方式”这一行动号召表明该公司对其技术保持透明，并邀请感兴趣的人士更多地了解其创新的风力涡轮机建造方法。本质上，本文宣传木制风力涡轮机塔架是实现真正可持续的净零风电的关键解决方案。

---

## 47. 为高质量类型错误设计类型推断

**原文标题**: Designing type inference for high quality type errors

**原文链接**: [https://blog.polybdenum.com/2025/02/14/designing-type-inference-for-high-quality-type-errors.html](https://blog.polybdenum.com/2025/02/14/designing-type-inference-for-high-quality-type-errors.html)

本文认为类型推断本身并不会必然导致糟糕的错误信息。PolySubML语言的作者概述了类型推断系统的设计原则，这些原则优先考虑提供有用的错误信息。

核心论点是，许多语言为了其他目标牺牲了良好的错误信息，导致用户感到沮丧。作者指出了两个主要陷阱：

1.  **猜测和回溯：** 使用ad-hoc重载的语言需要编译器尝试多种可能性，导致指数级的复杂性和臃肿、无关的错误信息。作者提倡避免猜测和回溯的类型系统，确保发生错误时存在直接的推理链。C++的模板元编程和Swift对整数文字的处理被认为是这个问题的例子。

2.  **过早下结论：** 许多编译器，如OCaml的编译器，在类型检查期间不会跟踪它们期望相等的类型。这导致错误信息突出显示了症状，而不是根本原因。作者将此与PolySubML进行对比，后者会显示类型冲突的双方，并建议手动进行类型注释的位置，以缩小问题范围。

本质上，本文提倡一种设计理念，即类型推断系统应仔细跟踪类型期望，并提供清晰、上下文丰富的错误信息，以帮助用户理解类型错误的来源以及如何修复它们。

---

## 48. 微软支持的英国科技独角兽Builder.ai破产倒闭

**原文标题**: Microsoft-backed UK tech unicorn Builder.ai collapses into insolvency

**原文链接**: [https://www.ft.com/content/9fdb4e2b-93ea-436d-92e5-fa76ee786caa](https://www.ft.com/content/9fdb4e2b-93ea-436d-92e5-fa76ee786caa)

据《金融时报》报道，微软支持的英国科技独角兽Builder.ai已破产倒闭。这家以人工智能驱动的软件构建平台而闻名的公司，似乎正面临严重的财务困境。要了解故事的全部细节，《金融时报》要求订阅。该文章推广了订阅选项，包括标准数字版、高级数字版和印刷+高级数字版，并向潜在订阅者强调了它们各自的特性和优势。这些订阅选项提供了不同级别的《金融时报》新闻、分析和独家内容的访问权限。

---

## 49. 镜头设计师工具箱中的光学系统类型 (2020)

**原文标题**: Types of optical systems in a lens designer's toolbox (2020)

**原文链接**: [https://www.pencilofrays.com/lens-design-forms/](https://www.pencilofrays.com/lens-design-forms/)

镜头设计师工具箱中的光学系统类型：终极指南

本文题为《镜头设计师工具箱中的光学系统类型》，旨在为镜头设计师提供超越软件驱动设计的更深层次理解，是镜头设计形式的终极指南。它解决了镜头类型选择和替代设计考虑等常见问题。

该指南强调镜头设计中的模式识别，突出了理解镜头配置、材料选择和光线行为以直观评估性能的重要性。它承认镜头设计的历史背景，展示了不同时代和可用技术如何塑造当前的镜头形式。

主要议题包括：
*   **经典镜头：** 单透镜、双胶合透镜、Petzval镜头、Cooke三片式镜头和Tessar镜头。
*   **演变设计：** Ernostar镜头、Sonnar镜头、双高斯镜头和广角镜头。
*   **特定应用：** 望远镜头、反望远镜头、鱼眼镜头、变焦镜头、远心镜头和无焦系统。
*   **专业光学：** 反射镜、目镜、望远镜、显微镜、步进电机镜头、f-theta镜头、非球面镜头、自由曲面镜头和手机镜头，以及激光和照明镜头。

作者 Kats Ikeda 博士强调了掌握基本镜头设计形式以提高效率和直觉的重要性。该指南提供了历史背景、设计要点、设计之间的交叉链接、技巧和实际示例，以帮助理解每种镜头形式。 本指南专为那些寻求镜头设计形式及其应用的全面概述的人士而设计。

---

## 50. 约翰·卡马克在上限2025的演讲

**原文标题**: John Carmack talk at Upper Bound 2025

**原文链接**: [https://twitter.com/ID_AA_Carmack/status/1925710474366034326](https://twitter.com/ID_AA_Carmack/status/1925710474366034326)

这份“文章”根本不是文章，而是X.com（前身为Twitter）的一个页面，表明用户的浏览器中JavaScript已禁用。它不是John Carmack谈话的文字记录或摘要。因此，**无法根据提供的文本总结John Carmack的Upper Bound 2025谈话内容。** 该文本仅说明JavaScript已禁用，导致用户无法访问X.com的全部功能。它建议启用JavaScript或切换到受支持的浏览器，并提供X.com帮助中心、服务条款、隐私政策、Cookie政策、版本说明和广告信息的链接。

---

## 51. 日记：J. M. 库切，(1) 母语

**原文标题**: Diary: J. M. Coetzee, (1) Mother Tongue

**原文链接**: [https://books.substack.com/p/diary-j-m-coetzee-1-mother-tongue](https://books.substack.com/p/diary-j-m-coetzee-1-mother-tongue)

无法访问文章链接。

---

## 52. 侏儒䳭的奇特案例

**原文标题**: The Curious Case of the Pygmy Nuthatch

**原文链接**: [https://slate.com/culture/2025/05/birds-movies-charlies-angels-2000-pygmy-nuthatch.html](https://slate.com/culture/2025/05/birds-movies-charlies-angels-2000-pygmy-nuthatch.html)

文章详细描述了作者对鸟类的痴迷以及对2000年电影《霹雳娇娃》中一个特定场景的失望。在那个场景中，角色们根据一种鸟的歌声（与两种鸟都不符）将一只委内瑞拉黄鹂（视觉上描绘的）识别为小䴓，并声称它只生活在加利福尼亚州的卡梅尔，这在事实上是不正确的。这种公然的鸟类学上的不准确引发了作者为期一年的调查，以找出谁应该对此错误负责。

作者采访了最初的编剧约翰·奥古斯特，他透露早期草稿中曾出现更准确的鸟类，比如‘i’iwi和后来的岛屿红头伯劳。然而，奥古斯特因为创作分歧离开了这个项目，导致出现了17位编剧的频繁更替。作者随后采访了另一位编剧扎克·佩恩，他承认虚构了一种“蓝斑鹭”，但否认对小䴓错误负责。佩恩认为，混乱的制作环境可能导致多位编剧随意改动，最终导致了这个“离谱”的错误。

---

## 53. MCP是Web 2.0 2.0时代的到来

**原文标题**: MCP is the coming of Web 2.0 2.0

**原文链接**: [https://www.anildash.com//2025/05/20/mcp-web20-20/](https://www.anildash.com//2025/05/20/mcp-web20-20/)

文章认为，模型上下文协议（MCP）的迅速采用预示着Web 2.0开放精神的潜在复兴，作者称之为“Web 2.0 2.0”。 MCP是一种用于大型语言模型与不同应用程序交互的规范，被视为互操作性和用户控制的催化剂，让人想起早期的社交网络。

作者感叹当前互联网的状态，它被Facebook等封闭的专有平台所主导，这些平台扼杀了开发者的创新和用户的自主性。 他回忆起一个开放API和数据共享优先的时代，当时培育了一个协作生态系统，开发者们共同努力以确保互操作性，即使是在竞争对手之间。 他分享了一个个人轶事，讲述了大型社交网络如何关闭API，从而摧毁了他的公司，并突显了行业对开放标准的背离。

文章表达了希望，即MCP的采用能够重燃Web 2.0的精神，推动平台变得更加可编程和透明。 在承认MCP的不完善之处和潜在安全风险的同时，作者强调了拥抱并要求符合开放标准的重要性。 他敦促开发者将互操作性置于专有改进之上，从HTML的成功案例中吸取教训，尽管它存在缺陷。 他希望年轻一代能够受到MCP的启发，推动网络朝着其自然的架构发展：可编程和开放，而不是由少数大型公司控制。

---

## 54. 芝麻计划：过敏原食品标签的意外后果

**原文标题**: Sesame Scheme: Unintended Consequences of Allergen Food Labeling

**原文链接**: [https://www.choicesmagazine.org/choices-magazine/submitted-articles/unintended-consequences-of-allergen-food-labeling](https://www.choicesmagazine.org/choices-magazine/submitted-articles/unintended-consequences-of-allergen-food-labeling)

芝麻计划：过敏原食品标签的意外后果

---

## 55. 卫星探测深度

**原文标题**: Satellites Spotting Depth

**原文链接**: [https://tech.marksblogg.com/depth-anything-v2-maxar-ai-detection.html](https://tech.marksblogg.com/depth-anything-v2-maxar-ai-detection.html)

本文详细介绍了一项实验，该实验使用TikTok和香港大学开发的Depth Anything V2深度估计模型，处理Maxar公司提供的泰国曼谷卫星图像。作者使用了一台配备AMD Ryzen 9 9950X CPU、96 GB DDR5 RAM和高速NVMe SSD的高端工作站。由于更好的GPU驱动支持和与ArcGIS Pro的兼容性，操作系统为通过WSL在Windows 11 Pro上运行的Ubuntu 24 LTS。

作者安装了必要的先决条件，包括Python 3.12.3以及通过虚拟环境安装的Depth Anything V2的依赖项。然后，他们下载了最大的预训练Depth Anything V2模型（约1.3 GB）。

使用了两张Maxar卫星图像：一张是乍都乍区的大图，另一张是邦甲锁区较小的裁剪图。最初尝试使用大图进行推理失败，原因是黑色区域干扰了模型。第二次尝试使用较小的图像产生了更好的结果，成功生成了深度图。作者对深度图进行了地理配准，使其与原始卫星图像对齐。

文章最后指出，虽然深度信息是相对的，但可以开发一种工作流程，根据每个图像图块中最高建筑物的高度来缩放深度图，可能可以使用Overture的建筑物数据集。最后，作者展示了该模型在航拍图像上的有效性，并提供了来自塔林老城的例子。

---

## 56. 走进隧道：风洞的秘密生活

**原文标题**: Into The Tunnel: The secret life of wind tunnels

**原文链接**: [https://jordanwtaylor2.substack.com/p/into-the-tunnel](https://jordanwtaylor2.substack.com/p/into-the-tunnel)

无法访问文章链接。

---

## 57. Show HN: GetStack.dev – 追踪 GitHub 开源趋势

**原文标题**: Show HN: GetStack.dev – Track GitHub open-source trends

**原文链接**: [https://getstack.dev](https://getstack.dev)

GetStack.dev：追踪GitHub开源项目趋势的工具。展示给Hacker News社区。旨在帮助用户通过GitHub仓库数据识别和监控各种开源技术的流行度和演变，主要功能是追踪和可视化开源技术趋势，使用户了解哪些技术正在兴起、衰落或保持稳定。

---

## 58. 纪念阿拉斯代尔·麦金泰尔

**原文标题**: Remembering Alasdair MacIntyre

**原文链接**: [https://www.wordonfire.org/articles/remembering-alasdair-macintyre-1929-2025/](https://www.wordonfire.org/articles/remembering-alasdair-macintyre-1929-2025/)

无法访问文章链接。

---

## 59. 一个死而复生的男孩：我儿子马克斯的濒死体验与改变的人生

**原文标题**: A boy who came back: the near-death, and changed life, of my son Max

**原文链接**: [https://www.theguardian.com/lifeandstyle/2025/may/24/the-boy-who-came-back-the-near-death-and-changed-life-of-my-son-max](https://www.theguardian.com/lifeandstyle/2025/may/24/the-boy-who-came-back-the-near-death-and-changed-life-of-my-son-max)

阿奇·布兰德讲述了他幼子马克斯的濒死经历，以及这件事对他生活和育儿观产生的深刻影响。一天早上，马克斯被发现停止了呼吸，没有脉搏。经过紧急心肺复苏和医护人员的抢救，马克斯苏醒并被紧急送往医院。

最初的预后很糟糕，医生担心会造成严重的脑损伤，可能会影响他的呼吸甚至意识。家人经历了痛苦的充满不确定性的日子，接受了无数的测试，并努力应对马克斯可能残疾的可能性。

出乎意料的是，马克斯开始出现好转的迹象，最终能够自主呼吸并表现出意识。虽然事件的确切原因尚不清楚，但医生怀疑是罕见的婴儿猝死综合征（SIDS）中断病例。

这次经历彻底改变了布兰德的观点。他与内疚和责任感作斗争，尤其是关于他们雇佣夜间保姆的决定。他还深刻体会到生命的脆弱，有意义的生活可以以多种方式存在，以及残疾人所面临的社会挑战。布兰德分享这个故事的动机是为了正视回避讨论残疾的倾向，并庆祝他的儿子马克斯正在成为一个独特而引人注目的人。他最后讲述了《野兽国》中马克斯的故事，一个找到回家的路并获得爱的男孩。

---

## 60. 终结者：后会有期，Shell

**原文标题**: Terminator: Hasta La Vista, Shell

**原文链接**: [https://github.com/steipete/Terminator](https://github.com/steipete/Terminator)

Terminator：防止 AI 编码助手卡死的终端会话管理器

Terminator 是一款基于 AppleScript 的终端会话管理器，旨在防止像 Cursor 这样的 AI 编码助手因命令挂起而变得无响应。通过将命令隔离在不同的终端会话中，Terminator 确保循环连续性、更快的执行速度以及对进程的更好控制。

该工具解决了 AI 助手在遇到无限期运行的命令时中断其执行循环的问题，从而导致手动干预和工作流程中断。 Terminator 允许 AI 助手即使在命令挂起的情况下仍保持响应，保留会话上下文，并按项目管理相关任务。

主要功能包括：

*   **进程隔离：** 命令在独立的终端会话中运行。
*   **持久会话：** 终端会话在操作过程中保持不变。
*   **模糊目标分组：** 用于会话组织的智能模式匹配。
*   **进程终止协议：** 自动中断繁忙进程。
*   **会话智能：** 实时监控终端会话状态。

要使用 Terminator，请训练您的 AI 助手调用 `terminator.scpt` 脚本，并提供项目路径、任务标签、命令以及可选的要返回的输出行数。该脚本还包括可配置的属性，如命令超时、默认输出行数和模糊标签分组。

本文重点介绍了系统要求，包括 Terminal.app 和 System Events.app 的自动化权限，并提供了故障排除技巧。它还提到了有用的模型上下文协议 (MCP) 服务器，如 macOS Automator MCP 和 Claude Code MCP，以增强集成和开发循环效率。 最终，Terminator 旨在通过提供有组织和管理的终端会话来提高开发人员的生产力。

---

## 61. 从RPC到事务和持久化执行

**原文标题**: From RPC to transactions and durable executions

**原文链接**: [https://www.pramodb.com/index.php/2025/05/21/from-rpc-to-transactions-and-durable-executions/](https://www.pramodb.com/index.php/2025/05/21/from-rpc-to-transactions-and-durable-executions/)

本文探讨了实现容错系统的演变历程，从传统的数据库事务和分布式事务（使用两阶段提交或2PC）到现代的“持久执行引擎”（如Temporal）。它强调了简单函数与多个服务（数据库、电子邮件、事件总线）交互的缺陷，以及确保一致性和可靠性的挑战。

作者追溯了企业集成模式（EIP）的演进，分布式事务的局限性（特别是2PC的阻塞特性和放大故障的潜力），以及Java（JTA、Activity Service）和Web服务（WS-AtomicTransaction、WS-BusinessActivity）中标准化的尝试，但最终采用有限。

微服务和云计算的兴起催生了Resilience4J等库和Spring Integration等框架，重点在于补偿分布式系统固有的不可靠性。持久执行引擎作为一种现代解决方案出现，试图通过抽象底层复杂性来简化容错和异步性。

文章最后强调了各种持久执行引擎所做的不同设计选择，例如与编程语言的集成（Autokitteh vs. Temporal），使用事件日志（Restate）与数据库（DBOS）来存储执行历史记录，以及对无服务器函数的支持。作者表明没有“一刀切”的答案，并且有各种各样的实现可用于适应独特的用例和设计决策。最后，它指出，随着“持久执行”需求的增加，IPC机制和授权要求也会增加，因此出现了Temporal的Nexus。

---

## 62. KumoRFM：关系数据上下文学习的基础模型

**原文标题**: KumoRFM: A Foundation Model for In-Context Learning on Relational Data

**原文链接**: [https://kumo.ai/company/news/kumo-relational-foundation-model/](https://kumo.ai/company/news/kumo-relational-foundation-model/)

KumoRFM：关系型基础模型，旨在将基础模型的强大功能引入结构化关系数据。与需要特定任务训练的传统机器学习方法不同，KumoRFM利用上下文学习，无需事先训练即可对各种任务和数据库进行准确预测。

该模型通过将关系数据库转换为时序异构图来运行。它采用表不变编码方案和关系图Transformer，以跨多个表进行推理并处理各种数据类型。关键组件包括实时上下文标签生成器、预训练的关系型基础模型和可解释性模块。KumoRFM使用预测查询语言 (PQL) 来定义预测问题，然后将其转换为回归、分类和链接预测等任务。

在RelBench基准测试中的评估表明，KumoRFM优于传统的特征工程和监督深度学习方法，平均提高了2-8%。微调进一步将性能提升10-30%。至关重要的是，KumoRFM显著缩短了开发时间，与传统方法所需的数小时相比，只需几秒钟即可提供预测，并且只需极少的代码甚至无需代码。这使得KumoRFM成为实时预测的强大工具，从而能够更快、更智能地做出业务决策。

---

## 63. 逆向工程 iOS 快捷指令 Deeplink

**原文标题**: Reverse Engineering iOS Shortcuts Deeplinks

**原文链接**: [https://blog.alexbeals.com/posts/reverse-engineering-ios-deeplinking-for-shortcuts](https://blog.alexbeals.com/posts/reverse-engineering-ios-deeplinking-for-shortcuts)

本文详述了对iOS快捷指令深层链接的反向工程，以寻找一种以编程方式创建自动化的方法，特别是为单个应用程序切换灰度模式。作者最初的目标是避免为每个应用程序手动设置自动化。

作者首先使用`strings`命令行工具在快捷指令应用程序二进制文件上提取潜在的深层链接URL，揭示了`shortcuts://create-workflow?source=3d_touch`和`shortcuts://gallery`。虽然这些链接功能正常，但与自动化无关。

文章随后过渡到使用Apple的调试器`lldb`来调查快捷指令应用程序中的URL解析。在`-[NSURL scheme]`上设置断点，以观察对`shortcuts://`方案的处理。通过回溯，作者确定WorkflowKit的`ICManager`参与了深层链接处理。

为了进一步分析代码，作者利用反汇编器Hopper来反编译快捷指令二进制文件。通过找到内存中的当前偏移量并相应地调整Hopper的基地址，解决了地址空间布局随机化(ASLR)问题。通过检查反编译的代码，作者将深层链接处理追踪到`WFMainSceneDelegate`类和`ICManager`。

作者最后确定WorkflowKit中的`ICManager`是处理深层链接的关键组件，为进一步研究其功能和能力奠定了基础。本文最终旨在发现未记录的深层链接功能，这些功能可以促进以编程方式创建快捷指令自动化。

---

## 64. 古代法律规定查令十字车站铁路桥上必须悬挂一捆稻草。

**原文标题**: Ancient law requires a bale of straw to hang from Charing Cross rail bridge

**原文链接**: [https://www.ianvisits.co.uk/articles/ancient-law-requires-a-bale-of-hay-to-hang-from-charing-cross-rail-bridge-81318/](https://www.ianvisits.co.uk/articles/ancient-law-requires-a-bale-of-hay-to-hang-from-charing-cross-rail-bridge-81318/)

2025年5月，查令十字火车站桥上的脚手架触发了一项古老法律，要求悬挂一捆稻草（或干草，以安抚抱怨者），以警告水手。这项鲜为人知的地方法规，即《伦敦港泰晤士河章程》第36.2条，规定当桥拱净空高度低于正常水平时，必须展示一捆稻草。

这项法律起源于中世纪，尽管其起源已湮没在历史中，但仍然有效。目前的情况是由于对亨格福德桥进入查令十字车站进行多年维护工作的第一阶段造成的。脚手架正在逐拱架设，暂时阻碍了水道。

稻草捆目前悬挂在铁路桥旁边的禧年步行桥上，除了夜间使用的警示灯外，还提供了视觉警告。随着脚手架在未来几年内沿着桥梁移动，稻草捆也需要重新安置。因此，在维修期间，一捆稻草将成为查令十字火车站桥上的固定装置，这一切都要归功于一项古老的法律。

---

## 65. Go语言中的死锁：并发的阴暗面 (2021)

**原文标题**: Deadlocks in Go: the dark side of concurrency (2021)

**原文链接**: [https://www.craig-wood.com/nick/articles/deadlocks-in-go/](https://www.craig-wood.com/nick/articles/deadlocks-in-go/)

本文基于2021年Gophercon UK大会上的演讲，深入探讨了Go语言中死锁的复杂性，重点在于调试和预防。死锁发生在并发进程无限期地相互阻塞时，每个进程都在等待另一个进程持有的资源。

作者Nick Craig-Wood强调了Go内置死锁检测器的局限性，由于其他活跃的goroutine，它通常无法在实际场景中触发。他使用rclone项目中的示例来说明常见的死锁场景，特别是那些由`sync.Mutex`和通道的使用引起的死锁。

文章强调，死锁通常是过度锁定的结果，引入过度锁定是为了解决Go的竞态检测器所识别的数据竞争问题。为了调试死锁，文章建议使用`kill -QUIT`命令或`net/http/pprof`包来生成回溯信息。检查这些回溯信息可以揭示哪些goroutine被阻塞在`semacquire`（锁获取）上，以及导致死锁的锁获取顺序。

关键要点是，死锁发生在goroutine以不同的顺序获取锁时。分析调用栈以识别潜在冲突至关重要。虽然可以使用通道，但死锁也可能发生，但使用通道时死锁发生的频率较低。

---

## 66. Show HN: SweepIQ – 一款帮你更快学习的简单AI工具

**原文标题**: Show HN: SweepIQ – A simple AI tool to help you learn more, faster

**原文链接**: [https://www.sweepiq.com](https://www.sweepiq.com)

无法访问文章链接。

---

## 67. 量子图论

**原文标题**: Quantum Picturalism

**原文链接**: [https://quantuminpictures.org/](https://quantuminpictures.org/)

量子图解主义以一种可视且易于理解的方式介绍量子概念，旨在消除该领域的神秘感并使其对所有人具有包容性。它通过仅使用加法、减法和角度来表示量子数学，并采用“游戏式”规则，同时保持足够的数学严谨性以供专家使用来实现这一点。这种方法通过消除通常与复杂数学方程相关的恐惧感来增强各年龄段教育者和学习者的能力。“量子图解主义”一词描述了这种可视化的教学方法。文章重点介绍了进一步学习的资源，包括Bob Coecke和Stefano Gogioso的著作《图解量子》，常见问题解答部分以及ZX演算Discord服务器的链接，以促进社区互动。它强调参与不需要复杂的数学，从而推广了一种对量子力学世界的初学者友好的介绍。

---

## 68. 展示 HN: SQLite JavaScript - 使用 JavaScript 扩展你的数据库

**原文标题**: Show HN: SQLite JavaScript - extend your database with JavaScript

**原文链接**: [https://github.com/sqliteai/sqlite-js](https://github.com/sqliteai/sqlite-js)

SQLite-JS：为 SQLite 添加 JavaScript 能力的强大扩展，使用户能够直接在数据库中创建自定义函数，以实现灵活的数据操作。它支持标量、聚合和窗口函数，以及自定义排序规则，所有这些都可以使用 JavaScript 代码定义。

**主要特性：**

*   **自定义函数：** 创建用于处理单个行的标量函数、用于分组数据的聚合函数以及用于更复杂数据分析的窗口函数。
*   **自定义排序：** 定义文本值的自定义排序顺序。
*   **JavaScript 执行：** 直接在 SQLite 查询中执行 JavaScript 代码。
*   **跨设备同步：** 与 sqlite-sync 集成，以自动跨集群复制函数。
*   **轻松安装：** 预构建的二进制文件适用于 Linux、macOS、Windows、Android 和 iOS。
*   **清晰的用法示例：** 文档提供了用于创建和使用各种类型自定义函数的详细示例。
*   **从源代码构建：** 提供了使用 Makefile 从源代码构建扩展的说明。

本质上，SQLite-JS 使开发人员能够利用 JavaScript 的表达能力来扩展 SQLite 的功能，从而为直接在数据库中进行复杂的数据转换、计算和排序开辟了可能性。 对于任何寻求增强 SQLite 标准 SQL 之外的能力的人来说，它都是一个有用的工具。

---

## 69. Inigo Quilez: 计算机图形学、数学、着色器、分形、演示场景

**原文标题**: Inigo Quilez: computer graphics, mathematics, shaders, fractals, demoscene

**原文链接**: [https://iquilezles.org/articles/](https://iquilezles.org/articles/)

Inigo Quilez的网站是一个关于计算机图形学、数学、着色器、分形和演示场景技术的综合资源。该网站提供涵盖广泛主题的文字教程，所有教程均以MIT许可证发布，便于重复使用。虽然Inigo在他的主页上提供视频教程，但此特定页面侧重于基于文本的教程。

主要涵盖的主题包括：

*   **有向距离函数 (SDF) & 光线步进：** 详细介绍了2D和3D形状的SDF、光线步进技术、平滑最小值运算、域重复、软阴影，以及处理各种形状（如盒子和椭球）的方法。还包括分形光线步进。
*   **程序化生成：** 探讨了程序化噪声、FBM、梯度和值噪声导数、域扭曲、Voronoi噪声以及用于程序纹理的各种过滤技术。
*   **光照 & 渲染：** 涵盖了诸如户外光照、雾、环境光遮蔽（屏幕空间和逐顶点）、全局光照、GPU条件、三角函数优化、立体渲染、VR和简单的旧式效果等主题。
*   **实用数学：** 提供了一系列与图形相关的数学函数和技术，包括IK、环境光遮蔽计算、球体密度/可见性、逆双线性插值、距离计算、贝塞尔边界框和四元数运算。
*   **分形 & 复杂动力学：** 深入探讨了曼德勃罗集、朱利亚集、曼德博球分形、轨道陷阱、布达勃罗分形、IFS分形和李雅普诺夫分形。
*   **压缩：** 介绍了遗传算法、网格和wavelet压缩技术。

该网站还包括关于纹理和过滤、光线追踪技术、体素渲染、小型演示技术以及休闲数学问题的部分。作者鼓励用户通过Patreon或PayPal支持他的工作。

---

## 70. 草图日历

**原文标题**: Sketchy Calendar

**原文链接**: [https://www.inkandswitch.com/ink/notes/sketchy-calendar/](https://www.inkandswitch.com/ink/notes/sketchy-calendar/)

本文题为《草图日历》，探讨了将数字日历的便利性与纸质日历的灵活性和表现力相结合的可能性。目前的数字日历应用虽然提供同步和共享等功能，但可能让人感觉缺乏个性，并强加一种无法适应暂定计划或个人细微差别的刚性结构。另一方面，纸质日历允许更大的自定义、涂鸦以及将日常生活的各个方面（而不仅仅是事件）整合起来。

作者们质疑是否可以创建一个既能捕捉两种方法优势的数字日历。虽然有些应用程序试图通过添加个性化背景和习惯追踪器等功能来解决这个问题，但它们仍然受到“应用程序”范式和开发者定义的功能的限制。

相反，作者们建议从纸质日历的方式入手，并在一个简单的数字笔记本（如iPad和Apple Pencil）上添加少量的数字结构。他们的目标是探索如何创建互联的每日、每周和每月视图，将手绘注释与正式日历事件相结合，实施共享日历和邀请，并使用户能够使用自定义动态行为（如习惯或时间追踪器）个性化他们的日历，同时保留草图式的个性化感觉。文章最后预览了一个潜在的“草图日历”，并鼓励读者订阅以获取未来关于他们进展的更新。

---

## 71. “涡轮增压”线粒体助力鸟类史诗般的迁徙之旅

**原文标题**: 'Turbocharged' Mitochondria Power Birds' Epic Migratory Journeys

**原文链接**: [https://www.quantamagazine.org/turbocharged-mitochondria-power-birds-epic-migratory-journeys-20250519/](https://www.quantamagazine.org/turbocharged-mitochondria-power-birds-epic-migratory-journeys-20250519/)

候鸟如何依靠线粒体实现长途迁徙

本文探讨了候鸟如何依靠细胞动力源——线粒体，完成其不可思议的长途飞行。两个独立的研究小组发现，候鸟在亚细胞水平上发生生理变化，以提高其能量生产。

研究表明，在迁徙期间，鸟类线粒体发生变化，包括飞行肌肉中线粒体的数量、效率和互连性增加。 线粒体的这种“涡轮增压”使它们能够产生更多的ATP（肌肉收缩的燃料），从而使它们能够不停地飞行更长时间。

研究人员比较了黄腰柳莺和白冠带鹀等迁徙和非迁徙鸟类，观察到线粒体性能的差异。“线粒体移动实验室”促进了对野生鸟类线粒体的现场分析。迁徙鸟类表现出更高的线粒体氧消耗量，表明能量产生更多。 此外，它们表现出与线粒体重塑相关的蛋白质标记物，表明细胞器融合或分解以优化能量产生。

虽然涡轮增压的线粒体提供了额外的能量，但它们也会产生可能有害的活性氧。候鸟可能会通过富含抗氧化剂的饮食来抵消这一点。 该研究强调了鸟类的“表型可塑性”，其中环境线索（如不断变化的光照水平）会引发亚细胞变化，而不会改变遗传构成。这种适应对于理解鸟类如何完成其漫长的迁徙之旅至关重要。对鸟类线粒体的研究也可能对理解人类衰老和运动生理学产生影响。

---

## 72. 团队过于庞大时

**原文标题**: When a team is too big

**原文链接**: [https://blog.alexewerlof.com/p/when-a-team-is-too-big](https://blog.alexewerlof.com/p/when-a-team-is-too-big)

本文探讨了一个大型专业工程团队面临的挑战，以及向通才团队转型如何提高生产力和韧性。作者回顾了他们在由14名成员组成的团队中的经历，该团队正苦于沟通、无关紧要的站会以及前后端专家之间的依赖性。试图根据技术（前端/后端）将团队划分为工作组的尝试，由于固有的依赖性而被证明是无效的。其他解决方案，如临时特性团队和聘请顾问，也未能奏效。

关键的转折点是拥抱通才方法，团队成员发展了前端、后端、质量保证和DevOps方面的技能。这减少了内部依赖性，提高了所有权（知识、授权和责任），并培养了好奇心和协作。伍迪·祖尔主持的研讨会促进了结对编程，这对知识共享以及更简单、更易于维护的解决方案至关重要。

向通才的转变之所以奏效，是因为每个人都共享一个共同的产品背景，需求定义明确，并且该方法与团队的动机（自主性、精通和目标）相一致。虽然该解决方案不是一个总体规划，但开放的对话、实验以及工作流程的持续优化被证明至关重要。作者强调，“适用实践”而非通用的最佳实践，对于成功至关重要。

---

## 73. 双子座扩散

**原文标题**: Gemini Diffusion

**原文链接**: [https://simonwillison.net/2025/May/21/gemini-diffusion/](https://simonwillison.net/2025/May/21/gemini-diffusion/)

谷歌Gemini Diffusion是一种在Google I/O大会上发布的新型LLM，它使用扩散而非自回归进行文本生成，优先考虑速度。与传统LLM按顺序生成文本不同，Gemini Diffusion通过提炼噪声来创建输出，从而实现更快的处理和错误纠正，尤其是在代码生成等任务中。

作者测试了Gemini Diffusion，发现它速度极快，生成代码速度达到857个token/秒，与运行Llama3.1-70b的Cerebras Coder相当。谷歌声称Gemini Diffusion实现了与Gemini 2.0 Flash-Lite类似的性能，但速度是其五倍。

文章根据Hacker News的更正澄清说，扩散被用来代替自回归，但可能仍然使用Transformer架构。进一步的解释描述了扩散LM类似于BERT，训练模型并行恢复被屏蔽的token，从而允许它通过从所有被屏蔽的token开始，并在多个步骤中完善它们来迭代生成文本。作者此前曾遇到过作为商业级扩散模型的Inception Mercury。

---

## 74. 挂在我墙上好几年的那个分形图

**原文标题**: That fractal that's been up on my wall for years

**原文链接**: [https://chriskw.xyz/2025/05/21/Fractal/](https://chriskw.xyz/2025/05/21/Fractal/)

本文深入探讨了作者对他们在中学时发现的分形“壁花”的探索。“壁花”已被粘贴在他们的墙上12年。最初，作者通过重复平铺和倾斜正方形来绘制它，后来试图使用L系统来生成它，但发现存在差异。L系统方法产生“二次科赫岛”，而壁花由于其正交平铺方法而具有独特的结构。

然后，作者探索了分形中正方形的计数和排序。他们设计了一个系统来为每个正方形分配数字，揭示了与5的倍数和5的幂（分形的比例因子）的联系。这导致使用基于矩阵的数字系统来表示分形中的位置，其中矩阵“M”作为基数，向量作为数字。

矩阵“M”的行列式起着至关重要的作用。壁花独特的正交平铺与“M”具有负行列式（-5）相关，这会在每次迭代时翻转空间的朝向。具有正行列式（+5）的矩阵会产生L系统版本。文章总结说，分形的两个版本都源于这些矩阵的选择，行列式5与分形的比例因子相关，解释了最初约27度的角度。改变行列式会导致具有空白空间或重叠迭代的分形。

---

## 75. 并非因果链，而是互动与适应

**原文标题**: Not causal chains, but interactions and adaptations

**原文链接**: [https://surfingcomplexity.blog/2025/05/19/not-causal-chains-but-interactions-and-adaptations/](https://surfingcomplexity.blog/2025/05/19/not-causal-chains-but-interactions-and-adaptations/)

Lorin Hochstein 批判了事件调查的根本原因分析（RCA）模型，认为它基于对复杂系统故障的错误理解。虽然承认 RCA 认识到多种原因并避免指责“人为错误”，但 Hochstein 认为 RCA 的因果链模型（根本原因到潜在原因到直接原因）过于简单。

Hochstein 提出了一种弹性工程（RE）模型，该模型强调系统组件之间的*交互*是事件的主要驱动因素。 RE 将事件视为意想不到的交互作用造成的“完美风暴”，而不是线性的因果序列。 它认识到单个组件本身可能没有缺陷，但它们在特定情况下的交互作用会导致故障。

RE 模型的一个关键方面是它专注于*适应*，以补偿分布在整个系统中的潜在故障。 Hochstein 认为，复杂系统之所以能运行，是因为持续的适应和容错。 虽然 RCA 试图消除根本原因以防止再次发生，但 RE 强调理解系统如何成功适应故障，并识别适应能力薄弱的领域。 RE 方法旨在培养和发展组织内部的容错来源，认识到消除特定的根本原因并不能阻止未来由未发现的故障的新组合引起的事件。 因此，理解和增强适应能力对于弹性至关重要。

---

## 76. 从 JSON 加载 Pydantic 模型，避免内存溢出

**原文标题**: Loading Pydantic models from JSON without running out of memory

**原文链接**: [https://pythonspeed.com/articles/pydantic-json-memory/](https://pythonspeed.com/articles/pydantic-json-memory/)

本文探讨了在 Python 中将大型 JSON 文件加载到 Pydantic 模型时内存占用过高的问题。作者 Itamar Turner-Trauring 演示了默认的 Pydantic JSON 加载方式会导致内存占用量达到 JSON 文件大小的 20 倍。

为了缓解这个问题，本文探讨了两种主要策略：内存高效的 JSON 解析和内存高效的表示。第一种方法是使用 `ijson`，一种增量 JSON 解析器，它逐段处理 JSON 文档，从而减少解析过程中的内存消耗。虽然速度较慢（5 倍），但它显着提高了内存使用率。

第二种策略侧重于数据的内存表示。作者将 `pydantic.BaseModel` 切换到带有 `slots=True` 的 `pydantic.dataclasses`。 使用 slots 通过预定义对象属性来优化内存使用，防止动态属性添加，从而进一步减少内存消耗。

文章提供了一个比较分析，显示当解析一个 100MB 的 JSON 文件时，峰值内存使用量从 2000MB（使用 `Model.model_validate_json()`）显着降低到 1200MB（使用 `ijson`），最终降低到 450MB（使用 `ijson` 和 `@dataclass(slots=True)`）。 作者提出了 Pydantic 的潜在改进方案，例如集成像 `ijson` 这样的增量解析以及在 `BaseModel` 中添加对 slots 的原生支持。 文章最后提供了优化生产环境 Python 代码的咨询服务，并推广了一份面向 Python 开发者的时事通讯。

---

## 77. Show HN: Defuddle，Readability 的 HTML 转 Markdown 替代方案

**原文标题**: Show HN: Defuddle, an HTML-to-Markdown alternative to Readability

**原文链接**: [https://github.com/kepano/defuddle](https://github.com/kepano/defuddle)

Defuddle 是一款用于从网页中提取和清理主要内容的工具，提供更具可读性和一致性的 HTML 输出，尤其适用于转换为 Markdown。 它的目标是移除广告、侧边栏、页眉和页脚等干扰，作为 Mozilla Readability 的替代方案，但采用更宽松的方式，并以一致的方式处理脚注、数学公式和代码块。

主要功能包括：

*   **内容提取：** 隔离网页的核心内容。
*   **HTML 标准化：** 将标题、代码块、脚注和数学公式等元素转换为标准格式，以便于处理。
*   **元数据提取：** 检索作者、标题、描述、域名和 schema.org 数据等元数据。
*   **移动端样式猜测：** 使用移动端样式来识别不必要的元素。
*   **可自定义选项：** 提供用于调试、Markdown 转换、URL 指定和基于选择器的元素移除的选项。
*   **程序包：** 提供核心版、完整版（包含数学公式转换）和 Node.js 版程序包，以满足不同的需求。

它可以通过 npm 安装，并可在浏览器和 Node.js 环境中使用。 该工具返回一个对象，其中包含 `content`、`title`、`author` 和其他元数据等属性。 Defuddle 专注于提供干净且一致的 HTML，以提高 HTML 到 Markdown 转换器的输出质量。

---

## 78. 关于“氛围编码”

**原文标题**: On "Vibe Coding"

**原文链接**: [https://tante.cc/2025/05/23/on-vibe-coding/](https://tante.cc/2025/05/23/on-vibe-coding/)

在《关于“氛围编码”》一文中，tante 批判了围绕人工智能代码助手（“氛围编码”）及其所谓的技术民主化益处的炒作。Tante 认为这种说法具有欺骗性，并忽略了软件开发的复杂性。作者认为，优秀的软件需要透彻的需求分析、对问题领域的理解以及对用户需求的考虑。实际代码往往是次要的，重要的是涉及同理心和社会理解的基础工作。

氛围编码承诺轻松获得结果，却削弱了“做功”的价值——即开发过程中发生的批判性思维和问题解决。虽然有些人认为它适用于快速原型，但 tante 认为这些原型往往会变成永久的、维护不良的解决方案。

“民主化”的论点也受到挑战。人工智能工具并没有通过赋能技能发展来提供真正的赋权；相反，它们提供现成的解决方案，这些解决方案可能会让人失去动力并限制个人成长。这种对人工智能的依赖加强了对大型科技公司的依赖，延续了偏见并边缘化了不同的声音。

此外，氛围编码可能导致构建不良、未经测试的软件，产生负面外部性，例如安全漏洞和错误信息的传播。这导致了一种用户对产品和服务期望降低的文化。作者总结说，受对专业知识的蔑视和对快速退出的关注驱动的氛围编码，最终通过创建不透明、不可持续且可能有害的数字环境，损害了开发者和用户。

---

## 79. Show HN: Samchika – 一个用于快速、多线程文件处理的Java库

**原文标题**: Show HN: Samchika – A Java Library for Fast, Multithreaded File Processing

**原文链接**: [https://github.com/MayankPratap/Samchika](https://github.com/MayankPratap/Samchika)

Samchika 是一个 Java 库，专为快速、多线程文件处理而设计，尤其适用于大型文本文件。 它提供了一个简单的 API 和并行处理能力，与传统方法相比，可显著提高性能。

主要功能包括完全多线程、直观的 API、可选的运行时统计信息和开源可访问性。 它非常适合用于日志分析、ETL 操作、大型文本语料库处理、批量报告生成、数据转换管道和实时数据处理等用例。

该库可以使用 Maven 或 Gradle 轻松集成到 Java 项目中，只需几行代码即可定义输入/输出路径和行处理器函数。 Samchika 的 `SmartFileProcessor` 使用构建器模式来配置文件处理任务。

基准测试表明，与简单的 BufferedReader 实现相比，性能显著提升（超过 70%），尤其是在多核系统和较大的文件（已测试高达 16 GB）上。 即使对于非常大的文件，内存使用量也保持在可控范围内。

Samchika 在 MIT 许可证下获得许可，允许免费使用、修改和分发。 该项目的灵感来自一个 JavaScript 库以及 LinkedIn 上关于大型文件处理挑战的讨论。

---

## 80. 有缺陷的120W充电器分析（Anker GAN Prime）[视频]

**原文标题**: Faulty 120W charger analysis (Anker GAN Prime) [video]

**原文链接**: [https://www.youtube.com/watch?v=-JV5VGO55-I](https://www.youtube.com/watch?v=-JV5VGO55-I)

此“文章”仅为YouTube页脚。它根本不是文章，而是YouTube页面底部的标准样板文字，包含指向YouTube平台各版块的链接，包括：

*   **关于：** 关于YouTube的信息。
*   **新闻：** YouTube的新闻版块（可能与平台更新相关）。
*   **版权：** 关于YouTube版权政策的信息。
*   **联系我们：** 指向YouTube联系/帮助资源的链接。
*   **创作者：** 为平台内容创作者提供的资源。
*   **广告：** 关于在YouTube上投放广告的信息。
*   **开发者：** 供开发者与YouTube交互的资源。
*   **条款：** YouTube的服务条款。
*   **隐私：** YouTube的隐私政策。
*   **安全：** 关于YouTube安全政策的信息。
*   **YouTube运作方式：** 对YouTube算法和运作方式的解释。
*   **测试新功能：** 关于YouTube测试计划的信息。

它还包括版权声明和对NFL Sunday Ticket的提及。因此，根据标题进行总结，实际内容可能涉及对YouTube视频中存在故障的Anker GAN Prime 120W充电器的分析。但是，提供的文本绝对没有提供关于视频内容的任何信息，除了它可能的主题。

---

## 81. 克劳德 4

**原文标题**: Claude 4

**原文链接**: [https://www.anthropic.com/news/claude-4](https://www.anthropic.com/news/claude-4)

Anthropic发布Claude 4，包含Opus 4和Sonnet 4模型，在编码、推理和AI Agent方面设立新标准。Opus 4是领先的编码模型，擅长复杂任务和Agent工作流，而Sonnet 4在Sonnet 3.7的基础上改进了编码和推理能力。

主要功能包括通过工具使用的扩展思考（测试版），允许Claude利用网络搜索和其他工具来改进响应、并行工具执行以及通过本地文件访问改进的记忆能力。Claude Code现已全面上市，集成了VS Code、JetBrains和GitHub Actions，简化了协作。新的API功能，如代码执行、MCP连接器、Files API和prompt缓存，使开发人员能够构建更强大的AI Agent。

Opus 4擅长编码和解决问题，在编码基准测试（SWE-bench、Terminal-bench）中取得了最高分。Sonnet 4平衡了性能和效率，展示了在Agent场景和代码库导航方面的进步。Claude 4模型还在避免走捷径和保持记忆方面有所改进。

Claude Code为IDE提供新的测试版扩展、可扩展的SDK和GitHub集成。这些模型旨在通过保持上下文、保持专注和推动有影响力的转型来改进AI协作，同时实施AI安全级别3保护。Opus 4和Sonnet 4可在Anthropic API、Amazon Bedrock和Google Cloud的Vertex AI上使用，定价与之前的模型一致。

---

## 82. 有灵魂的比特

**原文标题**: Bits with Soul

**原文链接**: [https://www.darwin.cam.ac.uk/lectures/entry/bits-with-soul/](https://www.darwin.cam.ac.uk/lectures/entry/bits-with-soul/)

“有灵魂的比特”引导读者观看西蒙·佩顿·琼斯的讲座和访谈。这意味着核心内容包含在这两个来源中，而本文则作为介绍或路标。

其隐含的目的是提供对西蒙·佩顿·琼斯的工作和观点的见解。他可能会讨论与计算机科学相关的主题，可能侧重于函数式编程、编译器设计或相关领域，因为他在这些领域广为人知。标题表明他可能会涵盖有关编程语言及其与人类智能和创造力相关联的概念。

达尔文学院的访谈表明会更深入地探讨他的个人观点，可能会探讨其工作背后的哲学、职业生涯或对计算机科学未来的看法。总之，讲座和访谈旨在全面展现西蒙·佩顿·琼斯的工作和思维过程。

---

## 83. Show HN: hcker.news – 一个符合人体工学的、基于时间线的 Hacker News 首页

**原文标题**: Show HN: hcker.news – an ergonomic, timeline-based Hacker News front page

**原文链接**: [https://hcker.news](https://hcker.news)

Hacker News 提交：“Show HN: hcker.news – 一个符合人体工学的、基于时间线的 Hacker News 首页”，宣布了一个新的、替代 Hacker News 前端。重点强调的关键特性是其“符合人体工学”的设计和“基于时间线”的故事呈现。页面本身目前正在加载故事，表明该项目要么是新的，要么正在开发中，要么遇到了临时的技术问题。目的是为浏览 Hacker News 内容提供潜在的改进用户体验，可能侧重于更好的可读性和提交内容的时间顺序视图。

---

## 84. Unix 工作站 – 计算机收藏

**原文标题**: Unix Workstations – The Computer Collection

**原文链接**: [https://www.computercollection.net/index.php/unix-workstations/](https://www.computercollection.net/index.php/unix-workstations/)

本文详细介绍了一系列基于Unix的工作站收藏，重点讲述了作者与它们相关的经验，尤其是在威斯康星州交通部工作期间的经历。该收藏包括一台Sun 4/60 SPARCstation 1，它被修复并更新了SCSI2SD板，运行SunOS 4.1.4和Solaris 2.7（尽管后者速度较慢）。

另一台是Intergraph InterPro 2020，从威斯康星州交通部的剩余物资中获得。作者讨论了它的历史，以及由于PC技术进步而导致的最终过时。他成功地使用定制的DB5W5转VGA电缆将其连接到两台LCD显示器，并提供了引脚图详情供他人复制。

Apollo DN3000是另一件怀旧之作，它是在威斯康星州交通部选择HP/Apollo工作站而不是DEC和Tektronix机器后获得的。作者回忆了竞标过程以及导致他获得DN3000的情况。他还提到了软件分发磁带和MAME模拟器的可用性。

最后，本文还提到了从威斯康星大学剩余物资中获得的HP 9000 C100工作站。作者描述了威斯康星州交通部对各种HP 9000系列工作站和服务器的使用，以及他们最终过渡到使用PC进行CEAL和ARC/INFO等应用以及Web服务器托管的过程。他还提到在HP C100上运行了早期版本的Linux。

---

## 85. 使用FoundationDB构建分布式Postgres

**原文标题**: Making Postgres Distributed with FoundationDB

**原文链接**: [https://fabianlindfors.se/blog/making-postgres-distributed/](https://fabianlindfors.se/blog/making-postgres-distributed/)

本文介绍了 `pgfdb`，一个实验性的开源 Postgres 扩展，旨在利用 FoundationDB 的强大功能将 Postgres 转化为分布式数据库。现有的解决方案，如 Citus、CockroachDB 和 Neon，存在局限性，要么需要手动配置，要么不是真正的 Postgres，要么缺乏完全的多主节点分布。`pgfdb` 旨在通过提供与 FoundationDB 的可扩展性、弹性和事务保证完全兼容的 Postgres 来解决这些缺点。

该扩展通过利用 Postgres 的可扩展性，特别是自定义表和索引访问方法，来替换标准存储和事务引擎来实现这一点。这允许以针对 FoundationDB 优化的方式存储和检索表和索引数据，同时还利用 FoundationDB 的分布式事务处理能力。

尽管仍处于早期实验阶段，但作者承认，对于典型的 Postgres 工作负载而言，实现可接受的性能尚不确定。然而，该项目提前发布是为了收集反馈并鼓励讨论。作者邀请感兴趣的个人联系以进行进一步的讨论。

---

## 86. 理查德·加温在氢弹设计中的作用被掩盖了。

**原文标题**: Richard Garwin’s role in designing the hydrogen bomb was obscured

**原文链接**: [https://www.nytimes.com/2025/05/19/science/richard-garwin-hydrogen-bomb.html](https://www.nytimes.com/2025/05/19/science/richard-garwin-hydrogen-bomb.html)

本文讲述了理查德·L·加温的一生及其成就，他在23岁时设计了世界上第一颗氢弹。文章着重强调了他人生中看似矛盾的一点：加温制造了一种具有巨大破坏力的武器，但他在后来的岁月中致力于阻止核扩散，并倡导负责任的公共政策。

文章强调了恩里科·费米的影响，费米是加温的导师和诺贝尔奖获得者，他在生命的尽头表示遗憾，因为他没有更多地参与关键的公共政策问题。受到费米遗憾的启发，加温感到有义务站出来，解决核武器的危险。

文章还指出，加温在设计氢弹中所扮演的角色一直保密，甚至对他的家人也是如此，这反映了核武器研发的敏感性和保密性。作者威廉·J·布罗德多年来对加温进行了广泛的采访，并强调了加温人生的“奇怪谜题”——这种“最致命武器”的创造者将其一生奉献于防止核恐怖。

---

## 87. 基于模型上下文协议的符号代数探险

**原文标题**: Adventures in Symbolic Algebra with Model Context Protocol

**原文链接**: [https://www.stephendiehl.com/posts/computer_algebra_mcp/](https://www.stephendiehl.com/posts/computer_algebra_mcp/)

本文详细介绍了作者探索使用 Anthropic 的模型上下文协议 (MCP) 将大型语言模型 (LLM) 与符号计算机代数系统（如 SymPy）连接起来的过程。目标是利用 LLM 的自然语言理解能力来解决数学问题，同时使用计算机代数系统进行精确的符号运算，从而解决 LLM 在执行精确计算方面的弱点。

MCP 允许 LLM 通过 REST API 调用外部工具，从而实现分工。作者在 Github 上分享了用于实验的代码。他们强调了使用 MCP 的挑战，包括稀疏的文档、Node.js 生态系统以及由于 LLM 的非确定性本质而导致的调试困难。

一个关键的例子表明，LLM 在整数分解等任务中表现不佳，而使用 'factor' 命令实现的 MCP 服务器能够准确地解决该问题。另一个例子展示了如何通过 MCP 使用 SymPy 求解阻尼谐振子，演示了 LLM 协调问题设置，而 SymPy 提供正确的解决方案，从而避免 LLM 产生幻觉。

作者强调了 MCP 在形式验证和定理证明方面的潜力，但也提出了严重的安全问题。本地 MCP 服务器执行任意代码的能力带来了恶意软件和漏洞的风险。本文警告不要盲目安装 MCP 服务器而不了解其安全影响。作者提供了 Cursor 和 Claude Desktop 的配置示例，以便在本地和通过 Docker 连接到 sympy-mcp 服务器。

---

## 88. Kotlin-Lsp：Kotlin语言服务器及Visual Studio Code插件

**原文标题**: Kotlin-Lsp: Kotlin Language Server and Plugin for Visual Studio Code

**原文链接**: [https://github.com/Kotlin/kotlin-lsp](https://github.com/Kotlin/kotlin-lsp)

Kotlin-Lsp：基于 IntelliJ IDEA 和 Kotlin 插件的 Visual Studio Code 官方 Kotlin 语言服务器协议 (LSP) 实现（预 Alpha 版），旨在为 VS Code 提供 Kotlin 支持。

**要点：**

*   **安装：** 从 RELEASES.md 安装 VSC 扩展（通过 VSIX）。 需要 Java 17+。 在打开仅 JVM Kotlin Gradle 项目时自动激活。
*   **特性：** 目前专注于仅 JVM Kotlin Gradle 项目。 支持的特性包括 Gradle JVM 项目导入、语义高亮、导航至 Kotlin/Java 源码/二进制文件、快速修复、部分 Kotlin 检查、即时诊断和基本补全。 计划支持 KMP 项目导入、重构和代码格式化等其他特性。
*   **状态：** 实验性，正处于积极开发中，不保证稳定性。 适合实验，但不建议用于关键工作。
*   **平台：** 主要在 macOS 和 Linux 上使用 Visual Studio Code 进行测试。 兼容其他 LSP 兼容的编辑器，但需要手动配置。 需要支持拉取式诊断的编辑器。
*   **源代码：** 目前部分闭源，以加快开发速度，利用 IntelliJ、Fleet 和 Bazel 构建系统。 目标是在初步稳定后完全开源。 VSC 扩展在 kotlin-vscode 中开源。
*   **反馈：** 通过 GitHub 报告错误和问题。 目前直接贡献仅限于文档 PR。

---

## 89. 人工智能的反弹会蔓延到街头吗？

**原文标题**: Will the AI backlash spill into the streets?

**原文链接**: [https://gabrielweinberg.com/p/will-the-ai-backlash-spill-into-the](https://gabrielweinberg.com/p/will-the-ai-backlash-spill-into-the)

加布里埃尔·温伯格的文章探讨了人工智能驱动的失业潮引发大规模公众骚乱和抗议的可能性。他认为，尽管对隐私、虚假信息和环境影响的担忧确实存在，但失业带来的威胁更为独特，因为它可能影响到跨党派和收入阶层的人们。

温伯格引用了历史案例，如卢德运动和20世纪60年代对自动化的恐惧，以说明潜在的结果。他强调，经济中断的严重性和持续时间将决定反弹的程度。他提出了关键问题，包括：人工智能是否会导致净失业？失业工人将如何得到支持？以及谁将承担干预成本？

文章提及了最近好莱坞、汽车工人及码头工人的罢工，认为它们可能是更大规模运动的早期迹象。温伯格还讨论了抗议活动对选举和政策的潜在影响，并指出了过去运动的喜忧参半的结果。他认为，历史上的相似之处，例如三角工厂大火后的抗议活动，或许可以提供一些见解。最后，他邀请读者分享他们对这个话题的看法和见解。

---

## 90. 四年视奏练习

**原文标题**: Four years of sight reading practice

**原文链接**: [https://sandrock.co.za/carl/2025/05/four-years-of-sight-reading-pracice/](https://sandrock.co.za/carl/2025/05/four-years-of-sight-reading-pracice/)

Alchemyst 详细介绍了他们四年来使用 iPad 应用程序 NoteVision 搭配 MIDI 键盘进行视奏练习的历程。他们使用 Pythonista 脚本自动化了部分流程，以随机化调号并在 MySQL 数据库中跟踪进度。这些数据通过 D3 仪表板进行可视化，揭示了明显的进步阶段：最初专注于 C 大调，然后是 G 大调，最后是随机调号。仪表板还突出了需要改进的领域。

作者发现他们可以直接从乐谱上演奏音符，而无需有意识地命名它们，而是依赖于识别升号和降号的模式。尽管他们的 49 键 MIDI 键盘存在局限性，但他们在视奏方面取得了持续进步并增强了信心。调号随机化对于避免自满和针对薄弱环节至关重要。

除了该应用程序，作者还有一个更广泛的 30 分钟练习流程，包括音阶/琶音、使用 Anki 进行理论练习、听写/作曲、听力训练和曲目练习。一位评论者提出了使用数字应用程序而不是纸质乐谱以及在较小键盘上演奏的担忧。Alchemyst 澄清说，该应用程序的练习是对使用完整尺寸钢琴演奏乐谱以及参与其他音乐活动的补充。

---

## 91. 我们称之为分贝的科学“单位”

**原文标题**: The scientific “unit” we call the decibel

**原文链接**: [https://lcamtuf.substack.com/p/decibels-are-ridiculous](https://lcamtuf.substack.com/p/decibels-are-ridiculous)

无法访问文章链接。

---

## 92. 好的伪随机数变坏时

**原文标题**: When good pseudorandom numbers go bad

**原文链接**: [https://blog.djnavarro.net/posts/2025-05-18_multivariate-normal-sampling-floating-point/](https://blog.djnavarro.net/posts/2025-05-18_multivariate-normal-sampling-floating-point/)

本文探讨了R代码中与使用`MASS::mvrnorm()`从多元正态分布生成样本相关的可重复性问题。尽管使用了`set.seed()`来控制随机数生成器 (RNG)，但模拟在不同的机器上产生了不同的结果，这本不应该发生。

作者调查了这个问题，发现根本原因不是`MASS`包本身，而是浮点运算的怪异之处。由于不同的机器计算协方差矩阵的方式略有不同（即使是看起来相同的机器），该函数会生成不同的随机向量。作者用略微扰动的协方差矩阵（`cov1`和`cov2`）演示了这一点，当与`MASS::mvrnorm()`一起使用时，它们会产生截然不同的结果，即使种子相同。这与`rnorm()`对于单变量正态分布的直观行为形成对比。

主要的结论是，`MASS::mvrnorm()`涉及矩阵分解，这是一个计算密集的过程，其中浮点误差会累积并导致输出的显著差异，即使生成的数字的底层分布属性保持正确。本文作为一个警示故事，说明了浮点运算的局限性及其对计算可重复性的影响，特别是那些涉及复杂矩阵运算的计算。

---

## 93. 史莱姆 (2021)

**原文标题**: Slime (2021)

**原文链接**: [https://granta.com/slime/](https://granta.com/slime/)

在《黏液》中，苏珊娜·韦德利奇探讨了黏液在自然界和人类认知中普遍存在却又常常被忽视的作用。作者从在格拉斯哥亨特博物馆寻找一种特殊的黏液标本开始，该标本驳斥了原始黏液是生命起源的理论。这为更深入地探讨黏液在各个科学学科中的多样功能奠定了基础。

韦德利奇强调了黏液在进化中的重要性，认为它为复杂生命形式铺平了道路，并继续支撑着全球循环和过程。她讨论了黏液如何作为一种物理和概念上的边界，同时在艺术、文学，甚至我们对生物学的理解中，将人类与“他者”联系起来并分隔开来。

作者考察了黏液的材料特性，指出其独特的能力，既能作为固体又能作为液体。她讨论了黏液在各种生物体中的作用，从水母的结构支撑到盲鳗的防御机制，强调黏液的存在对植物、动物和微生物的生命至关重要。她将现代人对黏液的厌恶与古代人对黏液的敬畏进行了对比，并解释了目前对黏液在生物医学和材料科学中的应用的研究。

最后，韦德利奇强调了气候变化对黏液生态系统构成的潜在威胁，认为一个更温暖的世界可能会自相矛盾地导致“黏液的新时代”的主导地位。她断言，本书呼吁人们认识到黏液在我们生活和环境中的重要作用，尽管它常常与令人不快的联想联系在一起。

---

## 94. 在线文本转图工具

**原文标题**: Online Text to Diagram Tools

**原文链接**: [https://xosh.org/text-to-diagram/](https://xosh.org/text-to-diagram/)

本文全面列出了将文本转换为图表的在线和命令行工具。它旨在作为参考，允许用户通过使用CTRL+F快速找到适合其特定需求的工具。

作者的个人建议是，序列图使用sequencediagram.org，因为它能够编辑文本和图表元素，流程图使用flowchart.fun，因为它速度快且简单。

本文的主体部分专门介绍了按类别划分的在线（基于浏览器）工具列表。这些工具涵盖了各种图表类型，包括：

*   **通用图表：** Pikchr, D2, Diagon, Typograms, Markdeep
*   **ASCII艺术：** Svgbob, asciigrid, shaky, MonoSketch, Archetype, Textik, ASCIIFlow, fsymbols
*   **专用图表：** Kroki（支持多种格式，包括 PlantUML、D2、Mermaid 等），Markwhen（时间线/甘特图），flowchart.js, code2flow, JSSM（状态），WebSequenceDiagrams, SVG Sequence Diagram, GraphUp, Diagwiz, Text Diagram, Chart Mage, BPMN Sketch Miner, dagre-svg, Graphviz editors, nomnoml, CodeUML, yUML, PlantText, Umple Online, ZenUML, DotUML, Database Diagram Tools, drawthe（网络）, mermaid, Diagram.codes, Blockdiag, state machine cat, XState Visualizer, LikeC4, Ilograph, Structurizr, Gleek, Penrose, WaveDrom (时序)。

本文还包括一个较小的 CLI（命令行界面）工具列表，这些工具需要从终端下载并运行。 这些工具包括 ditaa, perl graph-easy, GoAT: Go ASCII Tool, 以及 protocol（用于 ASCII 数据包图）。

本文强调该列表是手动维护的。

---

## 95. 阿尔伯塔分离主义浪潮搅动加拿大

**原文标题**: Alberta separatism push roils Canada

**原文链接**: [https://www.nytimes.com/2025/05/22/world/canada/alberta-separatism-referendum.html](https://www.nytimes.com/2025/05/22/world/canada/alberta-separatism-referendum.html)

阿尔伯塔省准备就脱离联邦举行公投，加拿大面临潜在的新危机。虽然由于宪法障碍，实际分离不太可能，但此举凸显了阿尔伯塔省居民长期存在的不满，他们觉得自己受到联邦政府的不公平对待。他们认为联邦制度限制了他们的石油和天然气资源，同时仍在征税，导致怨恨。特朗普呼吁吞并加拿大以及自由党政府的再次当选（被认为对阿尔伯塔省的担忧持敌对态度）等因素加剧了这种情绪。尽管阿尔伯塔省只有少数坚定的分离主义者，但这种情况与之前魁北克省的分离主义运动（最近已经失去动力）相似，表明加拿大联邦内部存在潜在的紧张关系。

---

## 96. 系统工程知识体系指南 (2024)

**原文标题**: Guide to the Systems Engineering Body of Knowledge (SEBoK) (2024)

**原文链接**: [https://sebokwiki.org/wiki/Guide_to_the_Systems_Engineering_Body_of_Knowledge_(SEBoK)](https://sebokwiki.org/wiki/Guide_to_the_Systems_Engineering_Body_of_Knowledge_(SEBoK))

系统工程知识体系 (SEBoK) 2.11版于2024年11月25日发布，是系统工程领域关键知识来源和参考资料的指南。它旨在通过组织和解释该领域来帮助各种人员。SEBoK是一个动态资源，会根据社区的意见定期更新，但主要参考现有文献，而不是一个全面的汇编。

它将系统工程定义为一种跨学科的方法，旨在实现成功的产品、服务和企业系统的整个生命周期，涵盖问题发现、解决方案定义、实现、运营、维持和处置。它适用于单一问题场景以及组织内部干预的管理。

最近的更新包括关于成功将系统工程嵌入组织中的障碍、系统工程中的成本估算和分析以及弹性建模的新文章。SEBoK的其他文章也进行了更新。编辑委员会正在努力整合更新，以在未来的版本中反映INCOSE手册的v. 5和2023年版本的ISO/IEC/IEEE 15288。

SEBoK分为八个部分，涵盖基础知识、新兴实践（如系统之系统和基于模型的系统工程MBSE）以及系统工程与其他学科之间的关系。它还包括词汇表和推荐参考资料。

SEBoK由理事会和管理机构（INCOSE、IEEE系统理事会和史蒂文斯理工学院）监督。来自SE社区的志愿者作者和审阅者贡献和审查内容。主要内容可以下载为PDF文件。

---

## 97. 注意力并非我们所需的全部

**原文标题**: Attention Wasn't All We Needed

**原文链接**: [https://www.stephendiehl.com/posts/post_transformers/](https://www.stephendiehl.com/posts/post_transformers/)

题为“Attention Wasn't All We Needed”的这篇文章探讨了注意力机制在最初的“Attention Is All You Need”论文基础上的进展，重点介绍了 PyTorch 中的实际应用。 它涵盖了几种旨在提高效率和可扩展性的关键技术：

*   **分组查询注意力 (GQA):** 通过在多个查询头之间共享键/值 (K/V) 投影来减少推理期间的内存使用。 GQA 不是为每个查询头拥有独立的 K/V 头，而是将查询分组以关注同一个 K/V 头，从而显著缩小了自回归解码所需的 K/V 缓存大小。 多查询注意力 (MQA) 是 GQA 的一个极端情况。

*   **多头潜在注意力:** 通过引入可学习的“潜在”向量作为中介，缓解了标准自注意力机制的二次计算成本。 输入元素关注这些潜在向量，然后潜在向量反过来关注输入元素，从而将复杂度从 O(L^2) 降低到 O(L \* N\_latents)，使其适用于非常长的序列。

*   **Flash Attention:** 通过避免物化完整的注意力分数矩阵来解决内存瓶颈。 它将输入分解为块，并使用在线 softmax 算法在更快的片上内存中逐块处理注意力，从而显著减少内存占用。

文章提供了每种方法的代码示例，说明了核心实现细节以及它们与标准多头注意力的区别。 关键的结论是，注意力机制的进步对于有效部署大型模型和处理更长的序列至关重要。

---

## 98. Haskell 的愚蠢面试题

**原文标题**: Silly job interview questions in Haskell

**原文链接**: [https://chrispenner.ca/posts/interview](https://chrispenner.ca/posts/interview)

本文探讨了如何使用 Haskell 解决常见的编程面试题，展示了该语言独特的范式和优势。它强调了 Haskell 的函数式特性、可组合性以及模式匹配和高阶函数的使用。

本文涵盖了几个问题：

*   **回文检查：** 使用 `reverse` 进行字符串比较的简单而优雅的解决方案。
*   **Fizz Buzz：** 演示了模式守卫和将逻辑与效果（打印）分离。
*   **和为 N：** 涉及找到加起来等于目标的数字组合，利用递归和过滤。 提出了两个版本：一个用于特定长度的组合，另一个用于任何长度的组合。
*   **字谜检查：** 使用 `sort` 和 `on` 比较排序字符串的简洁解决方案，突出了 Haskell 的表达能力。
*   **最小值和最大值：** 提出了三种查找列表中最小和最大元素的方法，解决了空列表的潜在问题，并展示了使用 Semigroups、Monoids 和 `Maybe` 进行更安全实现的方法。
*   **词频统计：** 侧重于数据结构，特别是 `Data.Map`，以统计单词出现次数并查找文本中最常见的单词。

作者强调，Haskell 解决方案通常优先考虑清晰度和可组合性，而不是原始性能，同时承认惰性有时可以隐式地优化性能。 本文将 Haskell 的方法与 Java 等其他语言中更冗长的解决方案进行了对比，提倡在性能足够时使用可读代码。

---

## 99. Visual Studio Code: 文本缓冲区重构 (2018)

**原文标题**: Visual Studio Code: Text Buffer Reimplementation (2018)

**原文链接**: [https://code.visualstudio.com/blogs/2018/03/23/text-buffer-reimplementation](https://code.visualstudio.com/blogs/2018/03/23/text-buffer-reimplementation)

本文详细介绍了 Visual Studio Code 于 2018 年对其文本缓冲区进行的重新实现，重点关注速度和内存使用方面的性能提升。最初的行数组实现虽然简单，但对于包含大量行的大型文件而言效率低下，导致内存不足错误和文件打开速度缓慢。

作者探讨了使用分段表数据结构来减少元数据开销。基本分段表存储原始文件内容和后续编辑，但行查找速度较慢，需要逐字符迭代。为了改进这一点，行分隔符信息缓存在每个节点中。然而，V8 的字符串长度限制迫使从单个“原始”字符串转变为缓冲区数组。

作者引入了平衡二叉树（特别是红黑树）来加速行查找。通过在每个节点中存储左子树的元数据（文本长度和换行符计数），搜索复杂度降低到 O(log n)。为了进一步优化，该实现没有在节点中存储实际的行分隔符偏移量，而是使用对缓冲区内行分隔符位置的引用，从而减少了对象分配并加快了操作速度。这种优化的结构被称为“分段树”。

基准测试表明，与行数组实现相比，分段树显著减少了内存使用并提高了文件打开和编辑速度。虽然基于行的查找在使用分段树时略慢，但它对整体性能的影响很小，尤其考虑到花费在渲染和标记化上的时间。本文强调了在特定环境中进行实际分析以及理解数据结构和算法影响的重要性。

---

## 100. 地球两端都有高潮隆起吗？(2014)

**原文标题**: Does Earth have two high-tide bulges on opposite sides? (2014)

**原文链接**: [http://physics.stackexchange.com/questions/121830/does-earth-really-have-two-high-tide-bulges-on-opposite-sides](http://physics.stackexchange.com/questions/121830/does-earth-really-have-two-high-tide-bulges-on-opposite-sides)

无法访问文章链接。

---

