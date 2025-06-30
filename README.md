# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-30.md)

*最后自动更新时间: 2025-06-30 17:48:06*
## 1. Show HN: TokenDagger – 比 OpenAI 的 Tiktoken 更快的分词器

**原文标题**: Show HN: TokenDagger – A tokenizer faster than OpenAI's Tiktoken

**原文链接**: [https://github.com/M4THYOU/TokenDagger](https://github.com/M4THYOU/TokenDagger)

TokenDagger：一款高性能的TikToken替代品，旨在加速文本处理，尤其是在大规模应用中。基于AMD EPYC 4584PX处理器进行的基准测试显示，与TikToken相比，TokenDagger的吞吐量最高可达2倍，在代码分词任务上的速度提升更是高达4倍。

速度的提升归功于优化的PCRE2正则表达式解析以及简化的BPE（字节对编码）算法，这降低了大型特殊token词汇表对性能的影响。该项目强调与原始TikToken分词器的完全兼容，使其易于集成。

使用`pip install tokendagger`即可轻松安装。本文还提供了开发安装的说明，包括必要的依赖项如`libpcre2-dev`以及可选的依赖项如`tiktoken`，用于运行测试。 随附的测试和基准测试验证了TokenDagger针对TikToken的兼容性和性能声明，使用了Llama和Mistral分词器，结论强调了在代码分词方面4.02倍的速度优势。

---

## 2. 森喜刚国度2和开放式巴士

**原文标题**: Donkey Kong Country 2 and Open Bus

**原文链接**: [https://jsgroth.dev/blog/posts/dkc2-open-bus/](https://jsgroth.dev/blog/posts/dkc2-open-bus/)

本文调查了ZSNES模拟器中一个长期存在的缺陷，该缺陷会影响《森喜刚国度2》中的旋转木桶。这些由方向键控制的木桶在ZSNES中会无限旋转，原因是模拟器缺乏开放总线模拟。作者jsgroth深入研究了65816汇编代码以查明原因。

65816处理器的开放总线行为意味着从无效内存地址读取数据会返回数据总线上的最后一个值。在DKC2的情况下，游戏会从未映射的地址读取数据，期望得到一个特定的值。作者识别出一个关键的代码片段，该片段依赖于此行为来停止木桶的旋转。该代码将当前和新的木桶方向进行异或运算，然后将结果与从地址$2000的开放总线读取获得的值进行与运算，并有条件地停止旋转。

在实际硬件上，在$2000处进行的开放总线读取始终返回0x2020。这个特定的值对于预期的游戏逻辑至关重要，当木桶到达基本或序数方向时，该逻辑会停止木桶。作者得出结论，开放总线读取实际上是拼写错误的结果，汇编指令是`and $2000`（绝对寻址），而不是预期的`and #$2000`（立即寻址）。用`and #$2000`指令替换`and $2000`指令可以修复该错误，即使没有开放总线模拟，木桶也能正常工作。

---

## 3. C语言的出处内存模型

**原文标题**: The provenance memory model for C

**原文链接**: [https://gustedt.wordpress.com/2025/06/30/the-provenance-memory-model-for-c/](https://gustedt.wordpress.com/2025/06/30/the-provenance-memory-model-for-c/)

本文探讨了明确定义的指针来源模型对于C编程语言的重要性，强调了它对编译器优化和程序正确性的影响。现有C标准中缺乏清晰的来源定义导致别名分析的模糊性，阻碍了编译器安全地执行优化。

作者解释了指针别名（即两个指针指向同一内存位置）及其对代码优化的影响。关于指针别名的错误假设可能导致错误并阻止编译器生成高效代码。

本文回顾了现有编译器工具和机制，这些工具和机制有助于推断有关指针使用的信息，例如基于类型的别名分析、`register`存储类、`restrict`指针限定符和`volatile`限定符。然而，这些工具和机制具有局限性，并且在很大程度上依赖于程序员的责任。

问题的核心在于指针未定义的“来源”，这使得编译器可以在没有明确指南的情况下，基于指针的“来源”对别名进行假设。这导致不一致和潜在的错误。作者随后讨论了对象粒度、指针生命周期和信息流等影响别名分析的问题。通过整数操作、`memcpy`复制和I/O的指针信息流动增加了复杂性。

本文最后强调，需要一个精确的来源模型来指导编译器和程序员，确保正确的优化和更安全的代码。它强调了通过整数跟踪来源的难度，以及需要适应诸如XOR链表之类的常用技术。

---

## 4. Show HN: 新Ensō – 首次公开测试版

**原文标题**: Show HN: New Ensō – first public beta

**原文链接**: [https://untested.sonnet.io/notes/new-enso-first-public-beta/](https://untested.sonnet.io/notes/new-enso-first-public-beta/)

此“Show HN”帖子宣布 Ensō 新版本的公开测试版发布，这是一个无干扰的写作应用程序。这个新版本（代号：Occult Vampire Keanu）的重点是简化和优化，秉承“MISS”（最重要的简单事物）理念。

主要改进包括简化的 UI 移动到菜单栏以便于访问、对辅助功能友好的主题，以及隐藏文本以保护隐私的“咖啡馆模式”。其他改进包括排版控制、新的文本渲染引擎以及 MacOS AI 垃圾信息预防功能。该应用程序将通过 AppStore（以及备用的 Gumroad 版本）提供，以避免作者认为 Gumroad 支付方式的阴暗性质。

尚未包含的功能包括分析（由于作者依赖直接用户反馈）、个性化（计划在未来实现）以及 RTL 语言支持（将在下一个测试版本中推出）。作者强调易用性和减少干扰，旨在实现类似于 Moleskine 笔记本的精致、熟悉的感觉。

未来的计划包括收集反馈、创建营销材料、添加 RTL 支持，并可能探索 Windows/Linux 支持、“快速保存”功能以及用于实验性写作工具的“玩具箱”功能。作者强调一种类似木工的开发方法，专注于质量和精心改进，而不是快速添加功能。

---

## 5. 人工智能领域没有新想法，只有新数据集

**原文标题**: There Are No New Ideas in AI Only New Datasets

**原文链接**: [https://blog.jxmo.io/p/there-are-no-new-ideas-in-ai-only](https://blog.jxmo.io/p/there-are-no-new-ideas-in-ai-only)

杰克·莫里斯认为，人工智能的最新进展主要得益于获取新的数据集，而非完全新颖的想法。他承认不断有研究改进人工智能系统（如FlashAttention和推测解码），但他认为，人工智能历史上的重大范式转变源于解锁新的数据来源。

他强调了四个关键突破：在ImageNet上使用深度神经网络，Transformer使得能够在整个互联网上进行训练，从人类反馈中进行强化学习（RLHF）从而允许从人类标记的数据中学习，以及推理，让AI从“验证者”那里学习。他认为，这些突破的底层机制早已存在，而关键的创新在于能够大规模地利用这些新的数据集。

莫里斯强调了从现有数据集（如文本）中学习的潜在饱和性。他认为，人工智能的下一次重大飞跃可能来自利用目前未被充分利用的数据来源，特别是视频（如YouTube）以及来自具身智能体或机器人的数据。他认为，视频数据的巨大数量和丰富性以及来自机器人的真实世界互动数据提供了未被开发的潜力。莫里斯主张探索和有效利用新的数据来源，以开启下一波人工智能的进步，而不是仅仅关注新的算法。他总结说，人工智能界应该优先寻找和利用新的数据，而不是仅仅关注新颖的算法思想。

---

## 6. 幻影阴谋：历时四十年完成的文字冒险游戏

**原文标题**: The Plot of the Phantom, a text adventure that took 40 years to finish

**原文链接**: [https://scottandrew.com/blog/2025/06/you-can-now-play-plot-of-the-phantom-the-text-adventure-game/](https://scottandrew.com/blog/2025/06/you-can-now-play-plot-of-the-phantom-the-text-adventure-game/)

此博文宣布《幻影阴谋》的完成与发布，这是一款作者于1984年开始创作的文字冒险游戏。受Infocom的《魔域》系列启发，作者孩提时代便开始在Atari 800上开发自己的地牢探险游戏。然而，由于内存限制和兴趣转移，该项目被搁置。

几十年后的2018年，作者（现为软件工程师）通过Playfic和Inform 7重新燃起了对文字冒险的热情。受最初的地图和物品笔记本的启发，他们决定使用Inform 7（Infocom用于创建《魔域》的同一虚拟机）重新制作《幻影阴谋》。直到新冠疫情爆发，才最终推动了游戏的完成，但进度并不稳定。

重新制作的游戏与最初的版本有所不同。房间被移除，计分和寻宝被省略，结局也变得不那么暴力。添加了一个元叙事，其中包含了自传元素和对作者童年的引用。现在的游戏比最初设想的更短，也更容易。

作者对游戏的完成表达了快乐和悲伤的混合情感，将其描述为“让一个幽灵安息”。该游戏可在网络浏览器中游玩，博文中包含复古包装盒艺术，其中包含线索。

---

## 7. 14.ai (YC W24) 在旧金山招聘创始工程师，打造Zendesk替代方案

**原文标题**: 14.ai (YC W24) hiring founding engineers in SF to build a Zendesk alternative

**原文链接**: [https://14.ai/careers](https://14.ai/careers)

14.ai（Y Combinator W24孵化项目，位于旧金山）正在招聘创始工程师，以构建Zendesk的替代产品。他们专注于安全性、可靠性、性能和客户响应速度。团队规模小但工作强度大，服务于从初创公司到大型企业的客户。

创始工程师的职责包括直接的客户互动和跨整个技术栈的工作：TypeScript、Postgres、Vite、Next.js 和 Effect。 关键领域包括并发系统、模块化服务基础设施、座席编排、文本处理、RAG、数据库优化、LLM 工程、遥测、CI/CD 和前端。

要求包括扎实的 Web 技术（尤其是 JavaScript/TypeScript）经验、将代码发布到生产环境的经验、从头开始构建产品的热情，以及加入创始团队的意愿。候选人必须居住在旧金山或愿意搬迁到旧金山。

加分项包括将 LLM 部署到生产环境的经验，以及之前的创业或高影响力项目经验。14.ai 获得了 Vercel、Slack、Dropbox、Replit 和 Algolia 等公司的知名投资者和创始人的支持。

---

## 8. 基于草图的预测与2027年人工智能

**原文标题**: Scribble-based forecasting and AI 2027

**原文链接**: [https://dynomight.net/scribbles/](https://dynomight.net/scribbles/)

Dynomight探讨了数学模型与基于直觉的“涂鸦式”预测的价值，尤其是在人工智能时间线背景下。作者认为，虽然数学模型对于受良好理解规则支配的复杂系统很有价值，但在预测缺乏这些属性的领域（如通用人工智能的到来）时，它们可能并不比直觉更有优势。

文章批评了“AI 2027”预测，该预测基于人工智能在特定任务上的进展速度，预测最早在2027年就能实现通用人工智能。Dynomight认为，尽管“AI 2027”预测采用了数学框架，但主要依赖于单一变量趋势的预测，并不一定考虑到计算、数据和算法进步等因素之间的复杂相互作用。

作为一种替代方案，作者提出了一种“涂鸦式预测”方法。这种方法包括绘制现有数据（在本例中为人工智能性能指标），然后在数据之上绘制多个看似合理的未来曲线，代表不同的潜在轨迹。这些曲线随后被视为概率分布，从而提供一系列可能的结果。作者提供了一个工具供读者创建自己的涂鸦式预测。文章最后链接到作者Substack上的其他内容。

---

## 9. Gridfinity：模块化开源网格收纳系统

**原文标题**: Gridfinity: The modular, open-source grid storage system

**原文链接**: [https://gridfinity.xyz/](https://gridfinity.xyz/)

Gridfinity：模块化开源收纳系统，旨在整理工作间并提高生产力。它几乎完全可以通过 3D 打印实现，并且基于 42x42x7mm 的倍数尺寸。该系统允许用户使用在线生成器创建自定义的收纳盒、底板和盖子。

该项目起源于 Alexander Chappel 的分类系统，并由 Zack Freedman 进一步开发，他以 MIT 许可证发布了他的设计。这促进了一个蓬勃发展的社区，该社区不断地调整和扩展该系统。Gridfinity 可以免费使用和修改，鼓励用户根据自己的特定需求进行定制。官方 Gridfinity Wiki 正在建设中，欢迎贡献者加入 Zack 的 Discord 服务器上的 #gridfinity 频道，以帮助开发该项目。

---

## 10. B2B SaaS 认证：与消费者软件认证不同

**原文标题**: Auth for B2B SaaS: it's not like auth for consumer software

**原文链接**: [https://tesseral.com/blog/b2b-auth-isnt-that-similar-to-b2c-auth](https://tesseral.com/blog/b2b-auth-isnt-that-similar-to-b2c-auth)

本文重点强调了B2B和B2C软件身份验证（auth）之间的关键差异，并指出B2B身份验证需要一种根本不同的方法。作者确定了三个主要区别领域：逻辑隔离/租户模型、优先级/权衡取舍以及功能/协议。

在B2C中，用户是主要实体，控制着他们的个人账户和数据。然而，B2B优先考虑*组织*作为主要租户，赋予企业控制公司内部用户访问和权限的能力。

优先级差异包括：B2C应用程序必须预见大规模应用，并优先考虑最终用户体验，以最大限度地减少客户流失。相反，B2B应用程序可以更侧重于安全性和业务需求，有时会牺牲最终用户的便利性。单位经济效益也不同，允许B2B供应商提供更个性化的支持，甚至用户模拟来进行故障排除。威胁模型也不同：B2C侧重于外部威胁（诈骗、欺诈），而B2B还必须解决内部威胁和潜在破坏。

最后，B2B软件需要B2C通常不需要的特定功能和协议，包括对企业身份提供商（IDP）、使用SAML的企业单点登录（SSO）以及通过SCIM的自动配置/取消配置的支持。这些功能对于企业客户管理用户访问并将软件与其现有IT基础设施集成至关重要。作者强调，企业需要这些组件，不容忽视。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 2 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 3 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 4 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 5 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 6 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 7 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 8 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 9 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 10 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 11 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 12 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 13 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 14 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 15 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 16 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 17 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 18 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 19 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 20 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 21 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 22 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 23 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 24 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 25 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 26 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 27 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 28 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 29 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 30 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 31 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 32 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 33 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 34 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 35 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 36 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 37 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 38 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 39 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 40 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 41 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 42 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 43 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 44 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 45 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 46 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 47 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 48 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 49 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 50 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 51 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 52 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 53 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 54 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 55 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 56 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 57 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 58 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 59 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 60 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 61 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 62 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 63 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 64 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 65 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 66 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 67 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 68 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 69 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 70 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 71 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 72 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 73 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 74 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 75 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 76 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 77 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 78 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 79 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 80 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 81 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 82 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 83 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 84 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 85 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 86 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 87 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 88 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 89 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 90 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 91 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 92 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 93 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 94 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 95 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 96 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 97 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 98 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 99 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 100 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 101 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 102 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 103 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
