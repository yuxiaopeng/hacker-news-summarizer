# Hacker News 热门文章摘要 (2025-06-30)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 预印电路：3D打印与电子学的融合

**原文标题**: Printegrated Circuits: Merging 3D Printing and Electronics

**原文链接**: [https://spectrum.ieee.org/3d-printing-smart-objects](https://spectrum.ieee.org/3d-printing-smart-objects)

奥利弗·柴尔德开创了一种名为“打印集成电路”的新型生产方法，该方法将电子元件和导电元件直接集成到3D打印物体中。 这旨在简化和增强智能、功能性3D打印物品的创建。 文章表明，与传统方法（在打印后添加单独的电子元件）相比，该方法提供了一个更精简的流程。 《健康科技内幕》前编辑和IEEE Spectrum撰稿人阿尔弗雷德·波尔强调了这项创新及其对消费电子产品和其他行业的潜在影响。 文章暗示该技术可以通过在一个打印步骤中无缝融合形式和功能来彻底改变制造过程。

---

## 12. Show HN：开源国际空间站追踪器，ESP32/Arduino，仅需20美元

**原文标题**: Show HN: Open-Source International Space Station Tracker ESP32/Arduino for $20

**原文链接**: [https://github.com/GuitarML/SpaceStationTracker](https://github.com/GuitarML/SpaceStationTracker)

这个“Show HN”帖子介绍了SpaceStationTracker，一个开源项目，它使用2.8英寸ILI9341屏幕在20美元的ESP32/Arduino CYD (廉价黄色显示屏)上显示国际空间站的实时位置。该项目使用Arduino IDE以C++开发，旨在成为一个STEM项目，教授图形学 (LVGL)、WiFi连接、REST API交互、JSON解析和触摸屏的使用。

该追踪器通过WiFi从WhereTheISS.at API获取国际空间站的位置数据，并显示纬度、经度和UTC时间。它具有用户友好的WiFi设置流程，创建一个临时热点用于安全配置，无需硬编码凭据。用户可以点击触摸屏上的国际空间站图标来显示一个关于国际空间站的随机事实。屏幕会自动变暗以节省电量，并在用户交互时变亮。

该项目需要一个带有电阻触摸屏的“ESP32-2432S028R” CYD、Arduino IDE和特定的库版本 (ArduinoJson, HttpClient, lvgl, RTClib, TFT_eSPI, WifiManager, XPT2046_Touchscreen)。该帖子提供了配置Arduino IDE、安装所需库以及将代码上传到CYD的说明。该项目根据GPL 3.0许可协议发布。 资源，包括在亚马逊上购买硬件的链接，以及Random Nerd Tutorials和其他有用项目（如Aura）的参考资料，也包含在内。

---

## 13. 逆向工程 Vercel 的 BotID

**原文标题**: Reverse Engineering Vercel's BotID

**原文链接**: [https://www.nullpt.rs/reversing-botid](https://www.nullpt.rs/reversing-botid)

文章《逆向工程 Vercel 的 BotID》探讨了 Vercel 实施的反机器人技术，特别关注其 BotID 服务的“Basic”模式。作者 veritas 强调了反机器人措施在安全和成本节约方面的必要性，以及它们对网络开放性和可访问性的潜在负面影响之间的冲突，尤其对于使用较少见的操作系统或注重隐私的浏览器的用户而言。

文章详细介绍了在 Next.js 项目中 BotID 的设置，演示了它如何通过获取并执行名为 `c.js` 的 JavaScript 脚本来识别机器人。 该脚本使用 javascript-obfuscator 进行了高度混淆，使其难以理解其功能。

文章的核心在于解混淆 `c.js` 脚本。 Veritas 概述了所使用的混淆技术，包括字符串编码和洗牌，并描述了一种使用 Babel 和 Node.js `vm` 包来逆转这些转换的方法。 作者解释了如何识别和提取用于字符串解码的相关函数（编码的字符串常量、洗牌函数和解码函数），然后在受控环境中执行它们，以显示原始的明文字符串。 然后，将解混淆的字符串用于替换混淆的调用，使代码更具可读性和可理解性。 文章并不侧重于破坏 BotID，而是侧重于理解其客户端实现。

---

## 14. 计算所需空间的新证明大幅压缩

**原文标题**: New proof dramatically compresses space needed for computation

**原文链接**: [https://www.scientificamerican.com/article/new-proof-dramatically-compresses-space-needed-for-computation/](https://www.scientificamerican.com/article/new-proof-dramatically-compresses-space-needed-for-computation/)

麻省理工学院计算机科学家瑞安·威廉姆斯的一项新证明大幅压缩了计算所需的空间，挑战了计算复杂性理论中近 50 年的假设。传统上，人们认为在“t”步内可解决的问题大约需要“t”个比特的内存。威廉姆斯的突破性成果表明，任何在时间“t”内可解决的问题都可以仅用约√t 个比特的内存解决。

这一反直觉的发现表明，一个 100 步的计算可以被压缩并用大约 10 个比特解决，远低于之前的预期。该证明依赖于一种“归约”，将问题转化为数学上等价的形式，通过巧妙地重复使用空间来解决，有效地将必要的信息塞进平方根数量的比特中。

像马赫迪·切拉奇奇这样的专家称赞这一结果“令人难以置信”，是向前迈出的重要一步，这意味着约束不一定是可用的内存量，而是如何有效地使用它。这项在 ACM 计算理论研讨会上发表的发现表明，对计算效率的理解可能会发生转变，从仅仅将更多内存塞进机器，转向优化内存使用。

---

## 15. 农作物释放的形成云雾的异戊二烯和萜烯可能显著改善气候

**原文标题**: Cloud-forming isoprene & terpenes from crops may drastically improve climate

**原文链接**: [https://www.smithsonianmag.com/science-nature/scientists-are-just-beginning-to-understand-how-life-makes-clouds-and-their-discoveries-may-drastically-improve-climate-science-180986872/](https://www.smithsonianmag.com/science-nature/scientists-are-just-beginning-to-understand-how-life-makes-clouds-and-their-discoveries-may-drastically-improve-climate-science-180986872/)

生物过程在云形成和气候调节中的重要作用

本文探讨了生物过程，特别是植物和浮游生物释放的气体，在云形成和气候调节中的重要作用。科学家们发现，与传统的尘埃和污染源相比，这些自然来源对云形成的贡献比之前认为的要大。

文章讨论了CLAW假说，该假说认为海洋藻类释放含硫气体形成云并调节阳光，作为该概念的早期例子。研究表明，来自海洋微生物的蛋白质和DNA片段等生物颗粒可以作为冰核颗粒，影响云的类型和反射率。

在陆地上，欧洲核子研究中心（CERN）的研究揭示了来自树木的气体，如单萜烯和异戊二烯，如何促进气溶胶形成和云的产生。特别是异戊二烯，在高海拔地区形成气溶胶，导致森林上空云的形成。文章强调，将这些植物衍生的蒸气纳入气候模型对于准确预测至关重要，尽管当前模型对这些影响的表述各不相同。

文章最后强调了植树造林作为一种气候缓解策略的潜力，因为树木形成的气溶胶和云有助于产生降温效果。随着传统污染源排放的减少，生物成因的云形成源对气候调节和潜在地球工程策略的重要性日益凸显。

---

## 16. 我让我的虚拟机以为它有个CPU风扇。

**原文标题**: I made my VM think it has a CPU fan

**原文链接**: [https://wbenny.github.io/2025/06/29/i-made-my-vm-think-it-has-a-cpu-fan.html](https://wbenny.github.io/2025/06/29/i-made-my-vm-think-it-has-a-cpu-fan.html)

本文详细介绍了如何使虚拟机（VM）显示具有CPU风扇，以绕过检查特定硬件组件的恶意软件检测技术。恶意软件通常使用CPU风扇的缺失（可通过Win32_Fan WMI类检测）作为虚拟化环境的指标。

作者专注于操纵SMBIOS数据，即用于填充Win32_Fan等WMI类的底层系统信息。通过制作包含“冷却设备”（类型27）和“温度探头”（类型28）数据的自定义SMBIOS二进制文件，作者试图欺骗虚拟机。

最初，作者遇到了Xen的smbios_firmware选项的限制，该选项限制了某些SMBIOS类型的修改。这需要修补Xen源代码，以允许修改类型27和28的SMBIOS记录。即使应用补丁后，仍然发现Win32_Fan类需要SMBIOS数据中同时存在类型27（冷却设备）和类型28（温度探头）条目，才能在Windows WMI中被正确识别。

最后，作者成功修改了SMBIOS数据，演示了如何使在Xen上运行的Windows虚拟机通过`wmic`命令报告存在CPU风扇。

文章还简要介绍了如何使用`-smbios`选项在QEMU/KVM中实现相同的结果，并强调了与Xen实现相比，这种方法的相对容易性。作者还指出，使用主机的SMBIOS数据也是可能的。

---

## 17. Ubuntu：Debcrafters 简介

**原文标题**: Ubuntu: Introducing Debcrafters

**原文链接**: [https://discourse.ubuntu.com/t/introducing-debcrafters/63674](https://discourse.ubuntu.com/t/introducing-debcrafters/63674)

Canonical 成立了一个名为 Debcrafters 的新团队，专注于维护 Ubuntu 软件仓库的健康。这个全球团队由来自不同背景（包括 Debian 开发者和 SRU 团队成员）的经验丰富的工程师组成，旨在吸引来自 Arch 和 NixOS 等不同 Linux 发行版的贡献者。

Debcrafters 的任务包括同步和合并来自 Debian 的软件包、审查迁移问题、向上游提交 Ubuntu 增量更新，以及管理诸如 glibc 升级等重大转换。他们还将负责改进 autopkgtest 基础设施、发行版规模的集成测试以及 Ubuntu 软件仓库的报告/仪表盘。

一个关键的重点是为 Ubuntu 开发者实现贡献体验的现代化。该团队将构建 "debcraft" 的原型，这是一种简化软件包创建、测试和上传的工具，集成了诸如 `git-ubuntu`、`lintian` 和 `autopkgtest` 等现有工具。还将提供新的文档，包括经过修订的 "Ubuntu 打包指南"。

Debcrafters 积极寻求扩大贡献者基础，提供从初学者到 "Core Dev" 的明确晋升路径。认识到跨发行版协作的价值，鼓励团队成员每周花一天时间为其他发行版做出贡献，以拓宽他们的视野并将新的想法带到 Ubuntu。Canonical 希望这个新团队能够为 Ubuntu 生态系统的健康和发展做出重大贡献。

---

## 18. 螺旋：一种现代、高性能语言

**原文标题**: Helix: A Modern, High-Performance Language

**原文链接**: [https://github.com/helixlang/helix-lang](https://github.com/helixlang/helix-lang)

Helix: 兼顾C++速度与Python安全易用性的高性能语言。其关键目标是高性能、通过高级内存跟踪（AMT）实现安全，以及通过全面的错误处理和跨平台标准库实现稳健性。

Helix具有现代、可读的语法、通用设计，并能与C和C++无缝互操作，并计划扩展到其他语言。它适用于系统编程、游戏开发和AI/ML应用。

核心关注点在于开发者体验，提供直观的错误报告和C++开发者熟悉的使用方式。Helix借鉴了C++的概念，例如模板和类，但简化了语法并增强了内存管理。与C++的本地互操作性是一项关键特性，能够重用现有的代码库和库。

与Rust严格的借用检查器或Zig的有限功能相比，Helix旨在提供一种平衡的安全方法，具有不那么严格的借用检查器、更简单的语法和完整的OOP支持。

本文档提供了安装和构建该语言的快速入门指南，以及一个“Hello, World!”示例。它还深入研究了Helix的高级类型系统，强调默认的非空类型、灵活的指针处理和全面的错误管理。还支持泛型和继承，从而实现代码的可重用性和专门化。文章最后讨论了项目状态、社区贡献、许可和致谢。

---

## 19. 为 Windows 交叉编译 Common Lisp

**原文标题**: Cross-Compiling Common Lisp for Windows

**原文链接**: [https://www.fosskers.ca/en/blog/cl-windows](https://www.fosskers.ca/en/blog/cl-windows)

本文重点介绍使用 SBCL (Steel Bank Common Lisp) 为 Windows 交叉编译 Common Lisp 代码的实践方面。它涵盖了几个重要的方面，首先是与 Windows DLL 交互所需的 C 链接。本文解释了如何在 Common Lisp 环境中管理和加载 Windows DLL。

该过程利用 SBCL，详细说明了如何设置它以进行交叉编译。至关重要的是，它提到了使用基于 Wine 的 SBCL 环境，这很可能为成功编译和链接提供必要的 Windows 环境。它还包括如何将这个基于 Wine 的 SBCL 集成到 Emacs 中，以获得简化的开发体验。

此外，该指南还涉及了在 Lisp 环境中处理 Windows 文件系统时路径名的重要性。最后，本文最终提供了关于构建可在 Windows 上运行的可执行文件的指南，确保 Lisp 应用程序可以有效地部署。本质上，本文为寻求以 Windows 平台为目标的 Common Lisp 开发者提供了一个路线图。

---

## 20. 数据中心、温度与电力

**原文标题**: Data Centers, Temperature, and Power

**原文链接**: [https://www.backblaze.com/blog/data-centers-temperature-and-power/](https://www.backblaze.com/blog/data-centers-temperature-and-power/)

数据中心是日益互联的世界和人工智能需求的关键，但面临着一个重大挑战：电力消耗。电力是主要的成本驱动因素，不仅影响水电费，还影响长期可持续性。

本文强调了数据中心电力使用量的巨大规模，其中最大的市场消耗数千兆瓦，全球数据中心占总电力消耗的很大一部分。持续运行的需求需要冗余电源系统和精确的温度控制，进一步增加了能源需求。

电源使用效率（PUE）是跟踪电源效率的关键指标，但存在局限性。本文讨论了增加数据中心温度的因素，包括IT负载、服务器配置、环境温度，甚至人员的存在。

降低温度涉及优化IT负载、定制设施设计以改善气流（高架地板、冷热通道封闭）和持续监控等策略。冷却方法包括基于空气的系统、基于水的系统和浸没式冷却，每种方法都有不同的效率水平。

本文强调了平衡冷却需求与能源消耗的重要性，并质疑过度低温的必要性。最后，本文强调了数据中心巨大的碳足迹，指出其高于航空业，单个数据中心消耗的能源可能与5万户家庭一样多。提高电源使用效率对于降低成本和承担环境责任至关重要，凸显了行业内透明报告和可持续实践的需求。

---

## 21. 疑影

**原文标题**: Shadow of a Doubt

**原文链接**: [https://harpers.org/archive/2025/07/shadow-of-a-doubt-ocd-andrew-kay/](https://harpers.org/archive/2025/07/shadow-of-a-doubt-ocd-andrew-kay/)

安德鲁·凯的《疑影》探讨了强迫症在美国生活的兴起，取材于他参加2023年度强迫症大会的经历。他强调了强迫症的孤立性，其特征是令人痛苦的想法和强迫性仪式，同时也强调了大会旨在消除对这种疾病的污名。

文章深入探讨了强迫症的各种表现形式，通过与会者在污染、暴力伤害和性取向相关痴迷作斗争的轶事加以说明。凯分享了他自己患有身份认同型强迫症的经历，其根源在于对“自我迷失”的恐惧。

凯探讨了围绕强迫症病因的争论。他指出了涉及血清素水平的传统神经生物学解释，这为SSRI药物处方提供了理由。然而，他也提出了一个有争议的观点，即没有令人信服的证据表明强迫症与低血清素有关，神经科学家无法通过脑部扫描识别强迫症患者。

文章提出了更广泛的问题，涉及制药公司的作用、精神痛苦的根源，以及文化因素是否促进了强迫症的兴起。凯认为，当前的时代精神可能正在个体中培养强迫症，使他们处于该疾病的连续谱系中。

---

## 22. 一块9900万年前的琥珀困住了一只从苍蝇体内爆发的僵尸真菌

**原文标题**: A glob of 99M-year-old amber trapped a zombie fungus erupting from a fly

**原文链接**: [https://www.cnn.com/2025/06/24/science/amber-insect-zombie-fungi-fossil](https://www.cnn.com/2025/06/24/science/amber-insect-zombie-fungi-fossil)

CNN报道：发现含感染僵尸真菌昆虫的两块9900万年前琥珀化石。第一块化石显示一只苍蝇头部长出蘑菇状的真菌子实体，第二块包含一只同样被感染的幼蚁。这些化石代表了两个先前未知的蛇形虫草菌物种（Paleoophiocordyceps gerontoformicae和Paleoophiocordyceps ironomyiae），是最古老的寄生真菌劫持并杀死其昆虫宿主的例证之一。

研究人员使用显微镜和微型计算机断层扫描技术研究了这些标本，揭示了古代生态关系的见解。蛇形虫草菌如今被称为“僵尸蚂蚁真菌”，会为了自身的繁殖而操纵宿主的行为，并启发了电子游戏《最后生还者》。这项发现表明，复杂的陆地生态系统存在于白垩纪时期，并且蛇形虫草菌充当了昆虫的“捕食者”，调节着种群数量。

文章强调，蚂蚁可能是僵尸化的早期目标，而苍蝇今天很少受到影响，这使得苍蝇化石尤为重要。专家认为，Paleoophiocordyceps可能以类似于现代僵尸蚂蚁真菌的方式将宿主僵尸化。这些发现强调了寄生真菌在塑造地球生态系统中的重要性。这些化石来源于2017年之前的缅甸琥珀市场，同时也引发了人们对冲突地区琥珀来源的伦理担忧。

---

## 23. 超声波牙刷承诺无痛检查隐藏的牙龈问题

**原文标题**: Ultrasound toothbrush promises painless checks for hidden gum problems

**原文链接**: [https://phys.org/news/2025-06-ultrasound-toothbrush-painless-hidden-gum.html](https://phys.org/news/2025-06-ultrasound-toothbrush-painless-hidden-gum.html)

研究人员开发了一种新型牙刷式超声换能器，旨在提供一种侵入性更小的方法来检测牙龈疾病。传统的牙周探诊，即使用金属器械检查牙周袋，可能会让人感到不适，并且可能错过疾病的早期迹象。

这种新设备使用超声波技术来对牙齿和牙龈进行成像，即使在难以到达的区域也是如此。与现有的超声波换能器（要么体积太大无法用于口腔，要么图像分辨率有限）不同，这种小型牙刷式换能器以更高的频率工作，从而产生高质量的图像。

在对猪牙的测试中，超声波测量的牙龈厚度和高度在统计学上与使用手动牙周探诊获得的结果相似，证明了新设备的可靠性。研究人员认为，这种侵入性更小的技术可以改善对牙龈健康的监测，从而有可能更早地诊断疾病并减轻患者的牙科疼痛。开发人员计划在未来的工作中将该设备用于患者，以便对牙龈线下进行成像、监测治疗并尽早诊断，从而减轻牙科疼痛并帮助患者保持健康的笑容。

---

## 24. 手机信号塔可兼作港口和海湾的廉价雷达系统 (2014)

**原文标题**: Cell Towers Can Double as Cheap Radar Systems for Ports and Harbors (2014)

**原文链接**: [https://spectrum.ieee.org/cell-tower-signals-can-improve-port-security](https://spectrum.ieee.org/cell-tower-signals-can-improve-port-security)

2014年TransportationNews的一篇文章中，Ian Chant报道了蜂窝塔的一种新用途：被动雷达系统。文章重点介绍了研究表明，蜂窝基站发射的被动无线电信号可用于探测小型船只，从而有可能提高港口和码头的安全性。

该系统被称为无源相干定位（PCL），无需专用雷达设备和基础设施，而是利用现有的蜂窝信号作为其信号源。这使其成为一种潜在的、更便宜且更易于部署的沿海地区监视和威胁检测解决方案。文章刊登了Fraunhofer FKIE的可视化系统图，进一步强调了该技术在船舶探测方面的能力。简而言之，该文章提出了将现有蜂窝塔改造成被动雷达网络，该网络比普通雷达更便宜。

---

## 25. 重新审视 Knuth 的“过早优化”论文

**原文标题**: Revisiting Knuth's “Premature Optimization” Paper

**原文链接**: [https://probablydance.com/2025/06/19/revisiting-knuths-premature-optimization-paper/](https://probablydance.com/2025/06/19/revisiting-knuths-premature-optimization-paper/)

Malte Skarupke 的文章重新审视了 Knuth 著名的“过早优化”引言，认为将其普遍用作避免小型优化的理由是一种误解。最初的语境涉及使用 `goto` 语句来优化多重集实现，特别是搜索数组。Knuth 的观点并非完全避免优化，而是专注于通过基准测试识别的关键代码段。

Skarupke 通过分析不同的基于数组的多重集插入方法来论证这一点。他复制了 Knuth 的优化（乐观插入，循环展开），甚至添加了另一种优化（迭代到零），并衡量了它们的影响。虽然这些优化提供了可衡量的改进，尤其是在较大的数据集上，但它们对较小数据集的影响很小，有时甚至是有害的，这表明在没有分析的情况下进行微优化可能会适得其反。

他强调，如果一个 10% 的改进，很容易实现，不应该被视为“过早优化”而放弃，如果它影响了关键代码。相反，优化工作应该以分析和识别性能瓶颈为指导。他还强调了像 STL 这样优化良好的库的作用，这些库的作者积极进行优化，而不认为它是过早的。

最终，Skarupke 提倡在优化之前进行基准测试并利用优化的库。虽然编译器并不总是能够自动执行所有这些优化，但利用像哈希表这样快速的数据结构通常会使微优化变得不必要，即使对于小型数据集也能提供卓越的性能。他总结说，Knuth 的引言是关于避免在非关键代码上浪费精力，而不是回避所有的优化工作。

---

## 26. 展示一下：我做了一个每日阳光追踪器

**原文标题**: Show HN: I built a daily sunlight tracker

**原文链接**: [https://www.lumehealth.io/products](https://www.lumehealth.io/products)

这款“Show HN”帖子介绍了一款每日阳光追踪应用程序，旨在通过使用户重新与自然光周期连接，从而改善昼夜节律健康和激素平衡。该应用程序旨在对抗现代室内生活方式对身体自然节律的负面影响，这些影响会导致精力、注意力和睡眠问题。

该应用程序鼓励用户全天测量自己的昼夜节律健康状况，并培养平衡激素的习惯。它将光定位为激素健康的基础要素。

此外，该公司正在开发一款名为“Lume”的可穿戴设备，该设备通过汗液分析持续监测激素水平，从而提供对昼夜节律健康的实时洞察。该设备旨在帮助用户优化他们的习惯，并与他们身体的自然节律保持一致，从而改善整体健康状况。用户可以注册以获得该可穿戴设备的早期使用权。

---

## 27. 大学的职责是抵制人工智能

**原文标题**: The role of the University is to resist AI

**原文链接**: [https://www.danmcquillan.org/cpct_seminar.html](https://www.danmcquillan.org/cpct_seminar.html)

本次研讨会上，演讲者借鉴伊万·伊里奇的《自愿简朴的工具》，论证大学的角色应该是抵制人工智能。演讲者认为，围绕教育领域人工智能的恐慌，例如作弊和员工替代，转移了人们对市场化教育和不稳定劳务等现有问题的注意力。

人工智能被批判为一种需要高能源和数据的大规模物质基础设施，其规模需求导致版权侵权和地缘政治纠葛。演讲者认为，教育领域的人工智能工具，如总结和研究助手，实际上并没有像声称的那样发挥作用，导致知识的“粗制滥造”。

演讲者警告大学不要接受像OpenAI这样的公司的人工智能项目，并将此与伊里奇的“激进垄断”概念相提并论，即人们变得依赖工业工具。批判性思维的影响被强调，人工智能生成的反馈可能会绕过学生自身的思考能力，甚至强化有害的叙事。

研讨会对工作场所对人工智能技能的推动提出质疑，认为这可能导致认知能力下降和企业控制。工党政府对人工智能的热情拥抱受到批评，认为这可能导致高科技和反动政治的融合，对重要服务和社会福利产生负面影响。

演讲者建议大学采取一种“技术政治”抵抗，以环境可持续性、捍卫创造力和去殖民承诺为基础。他们提倡受伊里奇启发的“对比研究”，以评估人工智能的实际后果，并优先考虑那些能够最大限度地提高自由和福祉的技术，而不是仅仅优化效率的技术。大学需要建立技术社会决定的模型，审查技术对社会的价值。

---

## 28. 简·奥斯汀最大胆的小说，也是最不被理解的一部。

**原文标题**: Jane Austen's Boldest Novel Is Also Her Least Understood

**原文链接**: [https://www.nytimes.com/2025/06/27/books/review/jane-austen-mansfield-park.html](https://www.nytimes.com/2025/06/27/books/review/jane-austen-mansfield-park.html)

无法访问文章链接。

---

## 29. 事件 – 快速的进程内事件分发器

**原文标题**: Event – Fast, In-Process Event Dispatcher

**原文链接**: [https://github.com/kelindar/event](https://github.com/kelindar/event)

这个Go包提供了一个快速的进程内事件分发器，旨在解耦模块并实现单个Go进程内的异步事件处理。它擅长需要高吞吐量、低延迟事件分发的场景，提供了一个简单、无依赖的发布/订阅解决方案。

该分发器支持同步和异步处理，每个订阅者都在自己的goroutine中运行。它利用泛型来实现类型安全，并兼容任何实现了`Event`接口的类型。该包既提供了一个默认的全局分发器以便快速使用，也提供了创建特定`Dispatcher`实例的选项，以实现更可控的事件发布和订阅。

提供的基准测试表明，与传统的通道相比，它具有显著的性能优势，事件处理速度提高了4到12倍。

然而，重要的是要注意其局限性。此解决方案不适用于进程间通信（使用Kafka或NATS等工具）、事件持久化、高级路由/过滤、跨语言场景或事件重放或去重等功能。它也不建议用于具有大量订阅者流失或大规模动态订阅者数量的应用程序。该软件包采用MIT许可证。

---

## 30. 想认识人，试试向他们收费？

**原文标题**: Want to meet people, try charging them for it?

**原文链接**: [https://notes.eatonphil.com/2025-06-28-want-to-meet-people-charge-them.html](https://notes.eatonphil.com/2025-06-28-want-to-meet-people-charge-them.html)

拥有大量在线粉丝的博主菲尔·伊顿一直苦于无法与志同道合的人建立联系，尽管他始终公开自己的联系方式。 沮丧之下，他决定尝试一种独特的方法：为30分钟的聊天收取100美元的费用，这笔钱直接捐给一家教育非营利组织。 令人惊讶的是，这几乎立即奏效了。

此后，伊顿结识了来自不同背景和地点的各种人士，讨论的话题从数据库趋势到开发者营销，并为教育事业筹集了近6000美元。 他将该项目的成功归因于几个因素。 人们很欣赏他们的钱捐给了慈善机构，而且捐款为要求他的时间提供了一个合理的理由。 这也让他可以毫不羞愧地在社交媒体上推广筹款活动。

虽然承认提供建议可能存在风险，但他将自己的意见定义为个人观点。 他意识到该项目的缺点：可能会排除那些需要他的指导但又无力捐款的人。 他试图通过声明他仍然可以在时间允许的情况下接受免费电话来缓解这个问题，并且还开展了一项生日特别活动，以 30 美元的捐款提供通话。

伊顿发起“为教育而聊”项目是因为他想帮助学生，但缺乏传统志愿服务的资格。 他发现用 30 分钟换取慈善捐款是“一项轻松的交易”，因此计划无限期地继续该项目，既享受筹款方面，也享受与有趣的人联系的机会。

---

## 31. NativeJIT：C++表达式 -> x64 JIT (2018)

**原文标题**: NativeJIT: A C++ expression –> x64 JIT (2018)

**原文链接**: [https://github.com/BitFunnel/NativeJIT](https://github.com/BitFunnel/NativeJIT)

NativeJIT是一个跨平台的开源C++库，专为涉及C数据结构的高性能即时（JIT）表达式编译而设计。由Bing团队开发并应用于其搜索引擎中，它注重速度和效率，使其适用于在运行时生成表达式并频繁评估的场景，例如基于用户查询对文档进行评分。

主要特性和设计考虑因素包括：

*   **性能至上：** 在查询处理期间优先考虑吞吐量和低延迟。
*   **轻量级且无依赖：** 仅需要标准的C++运行时依赖。
*   **支持的平台：** Linux、OSX和Windows。
*   **优化：** 针对寄存器分配进行了优化。
*   **功能：** 支持各种算术、逻辑、指针、数组操作、条件语句、结构字段访问和C函数调用。

该库包含演示基本用法的示例代码，例如计算圆的面积，并提供了使用CMake和现代C++编译器在不同操作系统上构建NativeJIT的说明。针对*nix系统、Ubuntu、OS X和Windows提供了安装说明，详细说明了必要的工具和配置。 NativeJIT的总体目标是为在性能关键型应用程序中编译和执行自定义表达式提供一种快速有效的方法。

---

## 32. 形式塑造功能吗？

**原文标题**: Does Form Shape Function?

**原文链接**: [https://www.quantamagazine.org/does-form-really-shape-function-20250612/](https://www.quantamagazine.org/does-form-really-shape-function-20250612/)

本文《形态真的决定功能吗？》刊登了 Steven Strogatz 和 Janna Levin 在 "Joy of Why" 播客中对哈佛大学教授 L. Mahadevan（“Maha”）的采访。 Maha 讨论了他对形态和功能如何在各种现象中相互交织的着迷，从莫比乌斯带等简单物体的形状到复杂的生物系统。

这次采访探讨了 Maha 关于大脑褶皱（脑回形成）的工作，以及它与发育、功能和潜在疾病的关系。 他解释说，大脑的褶皱，就像其他生物结构（肺、肠）一样，最大限度地增加了表面积，以实现不同的功能，例如信息处理。 Maha 描述了使用凝胶模拟大脑生长和褶皱的实验，表明相对于白质，灰质的扩张如何导致了特征性的沟壑（脑沟）。

对话触及了形态发生中基因预模式和自组织之间的相互作用，表明基因提供了逻辑，而物理过程提供了演算。 Maha 还提到了与大脑褶皱异常相关的发育障碍，如无脑回畸形（光滑脑）。 他指出，雪貂被用作这项研究的模型动物，因为与小鼠和大鼠不同，它们的脑部表现出褶皱。 这次采访突出了 Maha 的跨学科方法，结合了物理学、数学和生物学，以了解自然界中支配形态和功能的基本原理。

---

## 33. 学术人才流失：为何企业必须支持学术界

**原文标题**: The Academic Pipeline Stall: Why Industry Must Stand for Academia

**原文链接**: [https://www.sigops.org/2025/the-academic-pipeline-stall-why-industry-must-stand-for-academia/](https://www.sigops.org/2025/the-academic-pipeline-stall-why-industry-must-stand-for-academia/)

本文认为，近期美国国家科学基金会（NSF）资金的停止以及普遍存在的学术研究经费不足，对推动科技行业成功的创新管道构成了生存威胁。作者强调了公共资助的大学研究在RISC-V、谷歌搜索算法以及无线通信突破等基础技术中的关键作用。

核心论点是，工业界对学术研究负有“隐形债务”，从大学里培养的人才、研究和开放基础设施中不成比例地受益，而学术界却在经费削减的情况下难以维持这些资源。由此产生的“管道停滞”威胁着人才库、研究连续性和国际人才流动，可能导致“人才流失”。

作者发出行动呼吁，敦促研究人员、教育工作者，尤其是行业领导者和校友为高等教育进行倡导。文章提出了具体步骤，概括为首字母缩略词ACT：倡导（签署人民承诺书），呼吁行业贡献（财政支持和公开承认），以及超越回音室进行对话（联系参议员并参与更广泛的对话）。作者强调了局势的紧迫性，断言沉默就是同谋，计算的未来取决于捍卫使创新成为可能的条件。

---

## 34. 反作弊更新追踪

**原文标题**: Anticheat Update Tracking

**原文链接**: [https://not-matthias.github.io/posts/anticheat-update-tracking/](https://not-matthias.github.io/posts/anticheat-update-tracking/)

本文详细介绍了追踪热门游戏中使用到的各种反作弊系统更新的方法，概述了CDN结构、加密技术和文件提取过程。

**主要涵盖的反作弊系统：**

*   **EasyAntiCheat (EAC):** 解释了Epic Games收购后的CDN变化，模块解密（识别和逆向自定义解密算法），以及通过定位填充区域和利用已知加密算法提取驱动程序/内部模块。
*   **Battleye:** 重点介绍了其简单的CDN结构（Unix时间戳），以及使用偏移分析提取PE模块。指出了曾经用于保留旧版本的CDN，但现在已被删除。
*   **Electronic Arts Anti-Cheat (EA-AC):** 描述了查找安装程序并提取其内容，尽管现在需要在游戏运行时进行驱动程序转储。
*   **Vanguard:** 详细说明了提供版本和下载URL信息的公共API，从而可以轻松跟踪和直接访问文件。
*   **EQU8:** 提供了CDN URL结构和JSON响应格式，用于检索更新。
*   **FACEIT 和 ESEA:** 提及了下载链接以及与跟踪这些平台更新相关的挑战。

结论强调，虽然复杂的CDN和加密带来了一些不便，但它们并没有从根本上阻止研究人员提取模块或检测更新。真正的安全依赖于保护模块内部的检测逻辑。作者还分享说，在这方面的工作是一次关于devops、部署和对象存储的学习体验。

---

## 35. Medley Interlisp项目：复兴一个历史软件系统[pdf]

**原文标题**: The Medley Interlisp Project: Reviving a Historical Software System [pdf]

**原文链接**: [https://interlisp.org/documentation/young-ccece2025.pdf](https://interlisp.org/documentation/young-ccece2025.pdf)

该文档似乎是题为“Medley Interlisp项目：复兴历史软件系统”的文章的PDF源代码。由于PDF源代码中的内容主要是使用FlateDecode压缩的二进制数据，因此在没有正确渲染的情况下很难确定具体细节。

然而，根据标题和PDF的结构，该文章可能讨论的是Medley Interlisp项目。该项目可能围绕以下几点展开：

*   **Medley Interlisp的复兴：** 核心目标是使一个名为Medley Interlisp的历史软件系统重获新生。这意味着该软件可能年代久远，可能已经过时，或者难以以原始形式访问。
*   **历史意义：** Interlisp本身是一种具有历史意义的Lisp方言。Medley版本可能具有使其值得复兴的特定功能或用例。
*   **项目细节：** 该文章可能概述了Medley Interlisp项目的范围、面临的挑战以及用于实现其复兴的方法。这可能包括逆向工程、仿真、移植或其他软件保存技术。
*   **潜在用例：** 复兴后的系统可能在研究、教育、软件历史，甚至在保留独特功能的情况下，在实际应用中有所用途。

本质上，这篇文章可能详细介绍了一个专注于保存和使人们可以访问一个具有历史意义的软件遗产的项目。

---

## 36. 许多勒索软件在检测到已安装俄语键盘时会中止 (2021)

**原文标题**: Many ransomware strains will abort if they detect a Russian keyboard installed (2021)

**原文链接**: [https://krebsonsecurity.com/2021/05/try-this-one-weird-trick-russian-hackers-hate/](https://krebsonsecurity.com/2021/05/try-this-one-weird-trick-russian-hackers-hate/)

本文探讨了许多勒索软件中的一个奇怪特性：它们被编程为避免安装在安装了特定虚拟键盘的计算机上，特别是那些与独立国家联合体（独联体）国家相关的键盘，包括俄语和乌克兰语。这是来自东欧的网络犯罪分子采用的一种自保策略，目的是避免受到当地政府的审查和起诉，因为当地政府通常只在本土实体成为受害者时才进行调查。

本文以DarkSide勒索软件攻击Colonial Pipeline为例。尽管DarkSide声称自己不涉及政治，但其代码与许多其他代码一样，包含一份独联体国家“禁止安装”清单。仅仅安装了这些语言中的一种，就可以阻止恶意软件的执行。

虽然作者警告说这不是一个万无一失的解决方案，但它提供了一种简单、免费的“疫苗”，可以对抗特定类型的恶意软件。Unit221B的Allison Nixon认为，广泛采用这种技术可能会迫使俄罗斯黑客在法律保护和潜在收入之间做出选择，从而使他们更难区分合法的国内机器和外国机器。

本文还驳斥了伪造虚拟机环境作为有效反恶意软件策略的想法，指出虚拟机环境现在已经很普遍。最后，作者包含了在Windows计算机上安装不同键盘语言的说明。

---

## 37. 两万五美元汽车正在消失？

**原文标题**: The $25k car is going extinct?

**原文链接**: [https://media.hubspot.com/why-the-25000-car-is-going-extinct](https://media.hubspot.com/why-the-25000-car-is-going-extinct)

2025年6月29日《The Hustle》文章探讨了价格低于2.5万美元的经济型汽车日益稀缺的现象。这些曾经很常见的入门级车型正因汽车制造商优先考虑豪华车型的更高利润率而变得“濒临灭绝”。

文章以福特Maverick为例，强调了其最初作为经济型卡车的受欢迎程度，但随后四年内价格上涨了41%。截至2025年2月，售价低于2.5万美元的汽车仅占新车销量的4.8%，而2019年这一比例为23%。虽然现代和起亚等经济型品牌的价格大幅上涨，但豪华品牌的价格涨幅较小，甚至出现下降（考虑通货膨胀）。

文章指出，昂贵车辆的更高利润率是主要驱动因素。虽然许多固定成本在不同类型的汽车中基本相同（工程、材料等），但豪华车辆的回报利润更高。特别是美国品牌已经放弃了小型经济型车辆。

此外，美国的经销商模式也发挥了作用。经销商倾向于储备价格更高、配置更高的车辆，进一步减少了廉价选择的供应。虽然消费者已经习惯了豪华功能并愿意为此付费，但最近的经济不确定性导致更实惠车型的销量增加，制造商也进行了一些调整。

文章总结说，汽车市场中真正的廉价交易已经成为过去，所有新车实际上都变成了“奢侈品购买”。

---

## 38. 大规模安全构建不受信任的容器镜像

**原文标题**: Building untrusted container images safely at scale

**原文链接**: [https://depot.dev/blog/container-security-at-scale-building-untrusted-images-safely](https://depot.dev/blog/container-security-at-scale-building-untrusted-images-safely)

本文概述了如何使用Depot API，为多租户SaaS平台大规模安全高效地构建和管理容器镜像。Depot提供了一个API，用于隔离项目创建、构建管理、指标跟踪和日志检索，从而无需内部处理复杂的容器编排。

本文使用Go语言演示了如何构建工具，为每个客户创建隔离的构建环境，并使用项目范围的令牌来确保安全性。它涵盖了诸如项目创建、删除和缓存重置等基本操作。一个关键方面是利用Depot的缓存来显著缩短整个客户群的构建时间。

本文还展示了如何检索详细的构建指标，包括构建持续时间和由于缓存节省的时间，以及如何访问包含时间信息和错误状态的各个构建步骤。这使得能够进行全面的构建分析和性能监控。

通过使用Depot，平台可以安全地执行客户代码，提供快速的反馈循环，在无需基础设施管理的情况下扩展容器构建，并提供详细的构建分析。本文强调，这种方法适用于运行用户生成的Python代码或其他需要以高性能和隔离性执行用户生成的容器的服务。

---

## 39. 着色器之书 (2015)

**原文标题**: The Book of Shaders (2015)

**原文链接**: [https://thebookofshaders.com/](https://thebookofshaders.com/)

《着色器之书》是由 Patricio Gonzalez Vivo 和 Jen Lowe 编写的一本循序渐进学习片段着色器的指南。本书涵盖了广泛的主题，从 “Hello world!” 和 uniform 等基础着色器概念，到算法绘图、塑形函数、颜色、形状、矩阵、图案和生成设计等更高级的技术。它深入研究了随机数、噪声、分形布朗运动和分形的应用。

本书还探讨了使用纹理、图像操作、内核卷积和各种滤波器的图像处理技术。此外，它还讨论了诸如乒乓缓冲、康威生命游戏、涟漪、水彩效果和反应扩散等模拟技术。

最后部分涵盖了 3D 图形概念，包括光照、法线贴图、凹凸贴图、光线步进、环境贴图、反射和折射。

本书附录包含离线使用、树莓派兼容性、打印和协作等信息，以及面向 JavaScript 开发人员的介绍。还有一个示例库和词汇表。

作者和贡献者都受到了感谢，并且本书以开源许可证发布。读者可以通过新闻邮件、Twitter、Mastodon 或 Discord 了解最新章节。

---

## 40. 近两成非洲四国抗癌药物不合格

**原文标题**: Nearly 20% of cancer drugs defective in four African nations

**原文链接**: [https://www.dw.com/en/nearly-20-of-cancer-drugs-defective-in-4-african-nations/a-73062221](https://www.dw.com/en/nearly-20-of-cancer-drugs-defective-in-4-african-nations/a-73062221)

《柳叶刀全球健康》发表的一项最新研究显示，埃塞俄比亚、肯尼亚、马拉维和喀麦隆近20%的癌症药物为劣质或伪造产品。研究人员发现，从医院和药房抽样的近200种产品中，约17%含有不正确水平的活性成分。这对患者构成重大威胁，因为剂量不足会阻碍治疗，并可能加速肿瘤生长。

该调查突显了在非洲大陆监管药品方面面临的复杂挑战。原因包括制造缺陷、储存不当，以及彻头彻尾的伪造。肉眼观察通常不足以检测出劣质产品，因此需要实验室检测。

专家敦促加强监管、筛查技术和培训，以解决这一问题。处理和分析有毒的癌症药物的困难进一步使问题复杂化。世卫组织已承认该报告的调查结果，并正在与受影响的国家合作，以改善监管框架，防止劣质和伪造药品流通。

文章还强调，劣质药品是中低收入国家普遍存在的问题，可能导致治疗失败、不良反应和经济损失。在寻求长期监管改革的同时，研究人员正在开发即时解决方案，如用于现场化学测试的“纸质实验室”。尽管调查结果令人担忧，但该研究也指出，大多数供应商提供优质产品。

---

## 41. 尿素如何自发形成

**原文标题**: How urea forms spontaneously

**原文链接**: [https://ethz.ch/en/news-and-events/eth-news/news/2025/06/how-urea-forms-spontaneously.html](https://ethz.ch/en/news-and-events/eth-news/news/2025/06/how-urea-forms-spontaneously.html)

苏黎世联邦理工学院研究人员发现了一种新的途径，可在水滴表面由二氧化碳（CO₂）和氨气（NH₃）自发形成尿素。该反应在环境条件下发生，无需催化剂、高压或高温，暗示了早期地球上尿素形成的潜在机制。

这项发表在《科学》杂志上的研究强调了液滴气-水界面的独特化学环境，其中浓度和pH梯度创造了一个微观反应器。这使得尿素可以自发形成，而这种反应通常不会发生在本体液体中。理论计算支持了实验结果，证实了不需要外部能量。

这一发现为生命的起源提供了见解，因为尿素被认为是RNA和DNA等生物分子的关键前体分子。早期地球富含CO₂和氨气的 atmosphere 可能支持了含水气溶胶或雾滴中的这种反应。该研究表明，生物分子的起源可能比以前认为的更普遍，简单的界面起着至关重要的作用。此外，这种自发反应可能对未来可持续和低能耗的尿素生产产生影响。

---

## 42. 在Instagram上找到澳大利亚前总理的护照号码（2020）

**原文标题**: Finding a former Australian prime minister’s passport number on Instagram (2020)

**原文链接**: [https://mango.pdf.zone/finding-former-australian-prime-minister-tony-abbotts-passport-number-on-instagram/](https://mango.pdf.zone/finding-former-australian-prime-minister-tony-abbotts-passport-number-on-instagram/)

2020年，作者在Instagram上收到一张澳大利亚前总理托尼·艾伯特的登机牌照片。出于对潜在安全风险的好奇，作者决定利用公开信息“破解”该登机牌。

通过从登机牌图片中提取订票参考（最初扫描条形码失败后），作者使用艾伯特的姓氏和订票参考登录了澳洲航空的“管理预订”页面。

在浏览该页面时，作者最初没有发现任何过于敏感的信息。然而，通过使用Chrome浏览器中的“检查元素”功能查看页面的HTML源代码，作者发现了艾伯特的护照号码。他们还找到了艾伯特的电话号码和澳航内部员工与乘客相关的评论。这是因为航空公司在乘客登录时会提供乘客的护照号码以及航班信息。

考虑到其行为的影响和潜在的非法性，作者联系了许多人来报告这一安全漏洞，告知艾伯特，并寻求发布该故事的许可。作者还研究了相关法律，得出结论，拥有艾伯特的护照号码本身并不构成犯罪，但将其用于身份欺诈则构成犯罪。他们还考虑了潜在的诽谤问题，以及登录行为本身是否构成犯罪。这篇文章以幽默而又信息丰富的方式讲述了作者意外的发现以及随后为负责任地解决隐私泄露问题所做的努力。

---

## 43. 将 API 速率限制建模为丢番图不等式

**原文标题**: Modelling API rate limits as diophantine inequalities

**原文链接**: [https://vivekn.dev/blog/rate-limit-diophantine](https://vivekn.dev/blog/rate-limit-diophantine)

本文探讨了如何使用丢番图不等式来建模和解决API速率限制问题。作者Vivek解释说，在速率限制下调度具有重试的任务的问题本质上是一个整数可行性问题。

其核心思想是将每个任务的重试尝试表示为时间轴上的整数点。目标是调度任务(Xi)，使得落在任何60分钟窗口内的重试尝试总和(Ai)永远不超过速率限制(R)。这转化为不等式 sum(Ai * Xi) <= R，一个丢番图不等式。

作者强调了与数论的联系，并强调满足速率限制意味着在时间线上策略性地放置整数（重试时间），以使特定长度（窗口大小）的任何间隔都不包含超过给定数量的整数（速率限制）。

为了说明这个概念，Vivek提供了一个Go程序，该程序检查添加具有已定义重试模式的新任务是否会违反任何60分钟窗口内的速率限制。他还建议使用滑动窗口方法进行优化，以提高算法的效率。 本质上，本文展示了像丢番图不等式这样的数学概念如何为常见的软件工程挑战提供新的视角，突出了数学可以应用于解决问题的意想不到的地方。

---

## 44. Show HN: Octelium – Teleport、Cloudflare、Tailscale、Ngrok 的 FOSS 替代方案

**原文标题**: Show HN: Octelium – FOSS Alternative to Teleport, Cloudflare, Tailscale, Ngrok

**原文链接**: [https://github.com/octelium/octelium](https://github.com/octelium/octelium)

Octelium：一个统一的零信任资源访问自托管平台，是传统远程访问VPN以及Teleport、Cloudflare Access、Tailscale和ngrok等工具的现代替代方案。

Octelium设计用途广泛，可作为远程访问VPN、ZTNA平台、安全隧道基础设施、容器化应用程序PaaS、API网关、AI网关和Kubernetes Ingress替代方案。 它提供可扩展的零信任架构(ZTA)，并通过代码即策略实现基于身份的、应用层感知的访问控制。

主要功能包括：统一的人员和工作负载访问、支持HTTP、SSH、Kubernetes和数据库等协议的动态无密钥访问、使用策略的上下文感知访问控制、通过各种IdP的持续强身份验证，以及使用OpenTelemetry的应用层感知审计。它支持轻松的SSH访问，并简化容器化应用程序作为服务的部署。

Octelium强调通过CLI工具和基于gRPC的API进行集中式、声明式管理，无需直接管理单个服务器。它通过分配稳定的私有IP地址和管理私有DNS，避免了传统的VPN网络问题。它支持WireGuard和QUIC隧道，并设计为自托管，避免供应商锁定。

本文提供了在Codespace中试用Octelium、安装CLI工具和设置第一个集群的链接，以及许可证、支持、常见问题解答和法律信息资源。

---

## 45. Arm架构进军服务器市场——但尚无法撼动x86的控制地位

**原文标题**: Arm muscles into server market – but can't wrestle control from x86 just yet

**原文链接**: [https://www.theregister.com/2025/06/30/arm_server_shipments/](https://www.theregister.com/2025/06/30/arm_server_shipments/)

以下是文章的简明摘要：

基于Arm的服务器正在经历显著增长，预计到2025年将增长70%，这得益于Nvidia的DGX GB200 NVL72等用于人工智能处理的机架规模配置。然而，这种增长未能达到Arm设定的在今年年底前实现占据数据中心CPU销售额50%的目标。IDC估计，到2025年，Arm服务器将达到全球服务器出货量的21.1%。

整体服务器市场蓬勃发展，2025年第一季度达到创纪录的952亿美元，同比增长134.1%。IDC预测，全年将达到3660亿美元，增长44.6%。配备GPU用于人工智能的服务器正在推动这一增长，预计将增长46.7%，并占市场价值的近一半。超大规模客户和云提供商是这一激增的主要贡献者。

虽然x86服务器仍然占据主导地位，预计增长39.9%，达到2839亿美元，但包括Arm在内的非x86系统预计增长更快，达到63.7%，达到820亿美元。

从区域来看，美国预计将引领服务器市场扩张，增长59.7%，到年底将占服务器总收入的近62%。中国紧随其后，预计增长39.5%，占全球季度收入的21%以上。

IDC强调，处理人工智能，特别是推理的计算能力的需求不断增长，将继续推动服务器市场的增长。

---

## 46. Let's Encrypt – 过期通知服务已结束

**原文标题**: LetsEncrypt – Expiration Notification Service Has Ended

**原文链接**: [https://letsencrypt.org/2025/06/26/expiration-notification-service-has-ended/](https://letsencrypt.org/2025/06/26/expiration-notification-service-has-ended/)

Let's Encrypt将于2025年6月4日停止证书到期提醒服务，该服务已运行十年。此决定的原因包括用户越来越多地采用自动证书续订、希望减轻存储数百万电子邮件地址带来的隐私负担、维护服务的成本以及需要降低Let's Encrypt基础设施的复杂性。

Let's Encrypt鼓励需要到期提醒的用户使用第三方服务，例如Red Sift Certificates Lite，该服务可免费监控多达250个证书。作为停止该服务的结果，Let's Encrypt已删除之前与证书颁发数据关联的所有电子邮件地址。

今后，通过ACME API提供的任何电子邮件地址将不再与证书数据一起存储。相反，它将被转发到ISRG通用邮件列表系统。新电子邮件地址可能会收到关于订阅更新的入职邮件。

希望随时了解Let's Encrypt和ISRG的用户，请订阅他们的邮件列表。停止到期提醒服务使Let's Encrypt能够将资源分配给其他关键领域并简化其基础设施。

---

## 47. 在Python数据类中使用仅限关键字参数

**原文标题**: Use keyword-only arguments in Python dataclasses

**原文链接**: [https://chipx86.blog/2025/06/29/tip-use-keyword-only-arguments-in-python-dataclasses/](https://chipx86.blog/2025/06/29/tip-use-keyword-only-arguments-in-python-dataclasses/)

本文提倡在定义 Python 数据类时使用 `kw_only=True`，以提高可维护性和灵活性，尤其适用于可重用代码或库。在 `@dataclass` 装饰器中设置 `kw_only=True` 会强制用户使用关键字参数（例如，`MyDataClass(x=1, y='foo', z=False)`）而非位置参数（例如，`MyDataClass(1, 'foo', False)`）来初始化数据类实例。

这种方法提供了两个主要优势：

1.  **防止因字段重新排序而导致破坏性更改：** 更改数据类中字段的顺序不会破坏使用关键字参数的现有代码，而位置参数则不然。
2.  **允许子类添加必需字段而不受限制：** 如果没有 `kw_only=True`，具有默认值的字段将强制所有后续字段（包括子类中的字段）也必须具有默认值。 `kw_only=True` 赋予子类在父类中具有默认值的字段之后定义必需字段的自由。

本文强调了这些优势对于关注向后兼容性和向前扩展性的库作者的重要性。 文章提供了一个适用于 Python 3.10 之前版本（引入 `kw_only` 时）的兼容性解决方法，但承认在旧版本中子类化问题仍然未解决。

---

## 48. 我们无意中通过观看一百万小时的YouTube视频解决了机器人技术难题。

**原文标题**: We accidentally solved robotics by watching 1M hours of YouTube

**原文链接**: [https://ksagar.bearblog.dev/vjepa/](https://ksagar.bearblog.dev/vjepa/)

该文章描述了机器人技术领域的一项突破，该突破通过训练一个名为V-JEPA 2的神经网络，使其观看100万小时的YouTube视频来理解物理原理，而非语言。与在物理任务中表现不佳的大型语言模型（LLM）不同，V-JEPA 2通过学习潜在空间的表征来预测未来的现实时刻，专注于物理情境的“本质”，而不是预测每个像素。

V-JEPA 2由编码器（ViT-g）、使用掩码视频令牌（“tubelets”）的预测器和3D-RoPE组成。它使用渐进式分辨率训练，在一个庞大的视频和图像数据集上进行训练。

为了使模型具有可操作性，通过冻结V-JEPA 2并附加一个transformer来预测基于机器人动作的结果，创建了V-JEPA 2-AC。它仅在62小时的机器人录像（包括成功和失败）上进行训练。在机器人控制期间，V-JEPA 2-AC使用模型预测控制来选择使当前状态和目标状态之间的差异最小化的动作。

该系统展示了零样本泛化能力，成功地在新环境中执行抓取和拾放等任务。与扩散模型相比，它的规划时间也大大缩短。一个令人惊讶的发现是，将V-JEPA 2与较小的语言模型（80亿参数）对齐，在视频问答方面产生了最先进的结果，超越了用语言监督训练的模型。

局限性包括对相机位置的敏感性和长程漂移。未来的工作包括改进语言目标理解，并提示机器人“给我做一个三明治”，而无需视觉参考。作者推测，世界模型在现实世界理解方面可以与纯文本模型相媲美。

---

## 49. 触摸苹果商店的后墙

**原文标题**: Touching the back wall of the Apple store

**原文链接**: [https://blog.lauramichet.com/touching-the-back-wall-of-the-apple-store/](https://blog.lauramichet.com/touching-the-back-wall-of-the-apple-store/)

这篇博文讲述了作者对2000年代苹果商店的记忆以及他们与苹果产品的关系。青少年时期，作者和朋友们玩了一个游戏，试图触摸苹果商店的后墙，并在不被店员打扰的情况下离开。作者反思了青少年时期身无分文与打暑期工后成为付费顾客这两种与商店互动的奇怪动态。

那份给患有糖尿病女孩当夏令营辅导员的暑期工作非常辛苦，但足以让作者购买一台iPod 5。这次购买感觉很不真实，作者纠结于将商店视为游乐场和渴望“奢侈品”之间的矛盾。作者意识到苹果公司容忍青少年，因为他们是潜在的客户群。

作者将iPod的体验与他们早期从沃尔玛购买的普通MP3播放器（可能是Creative）进行了对比。虽然iPod是一项重要的购买，但旧的MP3播放器对他们的生活产生了更大的影响。它激发了对媒体盗版的兴趣，促使他们在笔记本电脑上安装Linux，并最终培养了Web和游戏开发方面的技能。作者感叹不记得旧MP3播放器的品牌了，尽管iPod具有“奢侈品”地位，但承认它影响更大。

---

## 50. Tumblr 迁移至 WordPress 并整合 Fediverse 的计划“已暂停”

**原文标题**: Tumblr's move to WordPress and Fediverse integration is 'on hold'

**原文链接**: [https://www.theverge.com/news/695124/tumblr-wordpress-automattic-fediverse-integration-on-hold-decoder](https://www.theverge.com/news/695124/tumblr-wordpress-automattic-fediverse-integration-on-hold-decoder)

据 Automattic 首席执行官 Matt Mullenweg 称，Tumblr 计划迁移到 WordPress 的项目（最初于去年宣布）目前已“暂停”。 此举旨在简化平台，并促进跨平台的更便捷共享。 然而，Automattic 现在优先考虑用户更需要的功能。

迁移暂停也影响了 Tumblr 与 Fediverse 的潜在集成，因为 WordPress.com ActivityPub 插件提供了一条将 Tumblr 帖子带到去中心化社交网络的直接途径。 Mullenweg 表示，如果对 Fediverse 集成有重大需求，他们可能会直接在现有的 Tumblr 代码库中实现它。

虽然 Mullenweg 仍然认为 WordPress 迁移具有长期价值，但他强调这并非当前优先事项。 重点将放在 Tumblr 用户更直接需要和请求的功能上。 Automattic 于 2019 年从 Verizon 收购了 Tumblr。

---

## 51. 微芯片CLB逆向工程

**原文标题**: Reverse Engineering the Microchip CLB

**原文链接**: [http://mcp-clb.markomo.me/](http://mcp-clb.markomo.me/)

本文描述了一个对Microchip新PIC16F13145微控制器系列上的可配置逻辑块（CLB）进行逆向工程的项目。 CLB是一个集成到微控制器中的小型类FPGA外设（32个LUT）。尽管它具有潜力，但Microchip仅提供专有的在线配置工具，从而掩盖了用户的直接访问和文档。

作者旨在通过逆向工程CLB的配置机制来规避此限制。数据手册明确指出，CLB接口无法通过SFR直接访问，并且需要Microchip的编程系统。

本文分为三个部分：背景信息和逆向工程方法，硬件测试程序，以及读者自行实施逆向工程的指南。目标是获得对CLB的更深入的理解和直接控制，超越Microchip官方工具的限制。这意味着希望以更定制和可能更有效的方式使用CLB。

---

## 52. 数列及其一阶差分共同列出所有正数且仅一次。

**原文标题**: Sequence and first differences together list all positive numbers exactly once

**原文链接**: [https://oeis.org/A005228](https://oeis.org/A005228)

本条目描述了整数序列A005228，其特点是与它的首项差分序列（A030124）结合后，恰好包含每个正整数一次。这是具有此性质的字典序最小的序列。

主要性质和公式包括：

*   `a(1) = 1`，对于 `n >= 2`，`a(n) = a(n-1) + c(n-1)`，其中 `c(n)` 是补序列A030124。
*   它是递增的，并且它的补序列（A030124）可以定义为尚未出现在任何一个序列中的最小数字。
*   给出了几个用于计算项的公式和递推关系。
*   渐近近似：`a(n) = n^2/2 + n^(3/2)/(3*sqrt(2)) + O(n^(5/4))`

该序列已被侯世达在《哥德尔、埃舍尔、巴赫》中讨论过，并且与各种其他整数序列有关（列于交叉引用中）。该条目包括用于生成序列的 Maple、Mathematica、Haskell 和 PARI 程序，以及对相关文章和网站的引用。它还与逆序列 A232746 和 A232747 有关。

---

## 53. 布隆过滤器示例

**原文标题**: Bloom Filters by Example

**原文链接**: [https://llimllib.github.io/bloomfilter-tutorial/](https://llimllib.github.io/bloomfilter-tutorial/)

布隆过滤器是一种概率型数据结构，用于高效地测试一个元素是否属于一个集合。 它以牺牲确定性来换取速度和内存效率，可能会返回假阳性，但绝不会返回假阴性。 其底层数据结构是一个位向量，通过多次哈希元素并将相应的位设置为 1 来添加元素。 通过哈希元素并检查这些位是否已设置来测试成员资格。

文章涵盖的关键方面：

*   **哈希函数：** 布隆过滤器依赖于独立、均匀分布且快速的哈希函数（例如，murmur、xxHash、fnv）。 速度对性能至关重要。
*   **大小和误判率：** 过滤器的大小（位数 'm'）和哈希函数的数量 ('k') 直接影响误判率。 较大的过滤器和/或较少数量的哈希函数会降低误判的可能性。
*   **最佳哈希函数数量：** 可以根据位数 'm' 和预期元素数量 'n' 计算最佳哈希函数数量 'k': k = (m/n)ln(2)。
*   **复杂度：** 插入和成员资格测试的时间复杂度为 O(k)，其中 k 是哈希函数的数量。
*   **应用：** 布隆过滤器用于各种需要高速和低内存使用率的成员资格测试应用。
*   **替代方案：** 如果无法估计元素数量，哈希表或可扩展的布隆过滤器可能是更好的选择。

---

## 54. 使用 eBPF 实现快速 TCP 指纹识别

**原文标题**: Implementing fast TCP fingerprinting with eBPF

**原文链接**: [https://halb.it/posts/ebpf-fingerprinting-1/](https://halb.it/posts/ebpf-fingerprinting-1/)

本文概述了作者使用eBPF在Go Web服务器中实现快速TCP指纹识别以增强反机器人检测的计划。文章首先解释了HTTP/1.0和TCP连接的基础知识，说明了一个简单的Web服务器如何在底层运行，直接与操作系统系统调用交互。

文章随后深入探讨了TCP握手的结构，强调了握手期间交换的数据如何揭示有关客户端设备和网络路由的信息。以最大分段大小 (MSS) TCP选项为例，演示如何推断网络特征。

作者探讨了潜在的实现策略。虽然POSIX API不提供对TCP SYN数据的直接访问，但考虑了使用LibPCAP的解决方案，但由于其实时限制而被否决。

文章提出eBPF作为更优的解决方案。eBPF程序可以高效地捕获和存储TCP SYN数据包在内核侧，并可从用户空间访问。这种方法消除了对外部库的需求并最大限度地减少了开销。作者解释了eBPF的功能：在内核中运行事件驱动的程序并与用户空间程序共享数据结构。他们计划使用Cilium eBPF库进行Go集成，并强调该项目是对eBPF的实践性介绍。eBPF程序的开发将在文章的第二部分中进行记录。

---

## 55. 使用无IPv4连接的互联网

**原文标题**: Using the Internet without IPv4 connectivity

**原文链接**: [https://jamesmcm.github.io/blog/no-ipv4/](https://jamesmcm.github.io/blog/no-ipv4/)

作者在ISP中断IPv4服务，仅提供IPv6后，如何利用Hetzner VPS恢复互联网连接的详细过程。面对有限的IPv4网站访问，他们利用具有IPv4和IPv6地址的Hetzner VPS创建了一个WireGuard隧道，有效地将所有流量路由通过VPS。

作者解释了网络地址转换（NAT）和运营商级NAT（CG-NAT），这些是理解问题和解决方案的关键概念。 IPv4的地址限制需要NAT，其中多个设备共享一个公共IP。ISP使用的CG-NAT增加了一层，可能导致连接问题，如作者所经历的。 IPv6的巨大地址空间在大多数情况下消除了对NAT的需求。

为了绕过IPv4中断，作者在VPS上安装了WireGuard，并将其配置为充当网关。他们提供了详细的服务器端和客户端配置，强调了对等点同时使用NATed和直接IPv6。这些配置包括用于转发流量的`iptables`和`ip6tables`规则。作者还指出，当有静态IP可用时，使用SNAT比MASQUERADE更有效率。

对于与全局WireGuard连接冲突的工作相关VPN访问，作者利用Linux网络命名空间和vopono来隔离VPN流量。通过将命名空间的流量路由通过WireGuard接口，他们可以访问工作VPN，而不会干扰全局互联网连接。该文章还讨论了修改`gai.conf`，以便在最初对IPv6问题进行故障排除时，优先在命名空间内进行IPv4 DNS解析。本文展示了Linux网络工具在克服意外互联网连接问题方面的多功能性和强大功能。

---

## 56. MCP：一个（意外地）通用的插件系统

**原文标题**: MCP: An (Accidentally) Universal Plugin System

**原文链接**: [https://worksonmymachine.substack.com/p/mcp-an-accidentally-universal-plugin](https://worksonmymachine.substack.com/p/mcp-an-accidentally-universal-plugin)

好的，我已经阅读了提供的URL中的文章《MCP：一个（意外地）通用的插件系统》。以下是一个摘要：

这篇文章讨论了MCP（Minecraft Coder Pack，后来被称为Mod Coder Pack）的历史和令人惊讶的广泛适用性，MCP最初是一个用于反编译、反混淆和重新编译Minecraft源代码的工具，目的是为了简化Mod制作。作者认为，由于几个关键的设计选择，MCP无意中变成了一个通用的插件系统，适用于其原始领域之外：

1.  **反编译和补丁：** MCP允许Mod直接修补和修改Minecraft核心代码，从而有效地规避了对正式、预定义的插件API的需求。这使其非常灵活。

2.  **版本独立性：** 由于Mod直接修补代码，该系统自然可以适应新的Minecraft版本。更新涉及到弄清楚如何将补丁应用于新反编译的代码。

3.  **专注于代码级修改：** MCP使Mod制作者能够在根本层面上更改Minecraft，允许他们添加或更改游戏的几乎任何方面。

4.  **简单的构建系统：** 核心的MCP系统促进了将修补后的代码重新编译为可工作的Minecraft版本。

文章强调，虽然MCP并非设计为通用插件系统，但其方法允许显著的灵活性和力量。这种方法可以应用于其他灵活性是主要问题的环境中，而正式的API可能具有限制性。文章假设，这种“意外”的通用性对于一般的软件设计具有借鉴意义，突出了在适当情况下启用深度修改的价值。

---

## 57. 布拉德·伍兹数字花园

**原文标题**: Brad Woods Digital Garden

**原文链接**: [https://garden.bradwoods.io](https://garden.bradwoods.io)

布拉德·伍兹的数字花园是一个专注于Web开发、创意编程和设计的笔记和探索合集。花园分为JavaScript、TypeScript、React、three.js、HTML、CSS、SVG和杂项主题等区域。

探索的关键主题包括：

*   **Web开发技术：** 花园深入探讨了动画、UI/UX开发（包括用户驱动的UI和目录设计）以及React、three.js、HTML和CSS等前端技术的实用技术。
*   **创意编程：** 诸如着色器、混合模式、滤镜和滚动驱动动画等主题突出了Web上的创意编程可能性。
*   **设计原则：** 围绕博弈论、“Juice”（增强软件感觉）、个性化、浏览器对故事叙述的适应以及有效写作的讨论，提供了有关创建引人入胜且充满灵魂的数字体验的见解。
*   **特定技术：** 笔记涵盖了JavaScript、TypeScript、React和three.js的基础和高级用法，包括状态管理、性能优化和Web API等主题。
*   **问题解决：** 该数字花园也充当了布拉德·伍兹一直在尝试以改善其工作流程并探索创意可能性的想法、代码解决方案和概念的集合。

总而言之，该数字花园提供了Web开发和创意编程主题的广泛概述，展示了实际实现、技术探索和设计考虑因素。

---

## 58. 寄往邮筒

**原文标题**: To the Postbox

**原文链接**: [https://literaryreview.co.uk/to-the-postbox](https://literaryreview.co.uk/to-the-postbox)

请提供《致邮筒》中文章“相对价值”的实际内容。我需要该文章的文本才能提供准确简洁的摘要。没有文章内容，我只能给出通用的回复，这毫无帮助。

---

## 59. 改善河流模拟

**原文标题**: Improving River Simulation

**原文链接**: [https://undiscoveredworlds.blogspot.com/2025/04/improving-river-simulation.html](https://undiscoveredworlds.blogspot.com/2025/04/improving-river-simulation.html)

JonathanCR详述了他在UW中（可能是一个游戏或世界构建程序）对其河流模拟的改进，重点在于更准确地表示河流流量。 之前，河流流量仅记录一月和七月的数据，这阻碍了对其他月份的准确推断，因为水流量取决于上游的气候条件，而不仅仅是本地单元格。

更新现在跟踪并存储所有十二个月的河流流量。 该程序计算每个单元格每月的水流量，并将其添加到下游单元格。 这使得河流流量的季节性变化更加准确。

他用一个假想的世界来说明这一点，这个世界有一条流经沙漠和苔原的长河。 第一个例子显示了河流上的一个点，尽管当地的温度和降雨量有所变化，但流量保持恒定，这是由于其北部源头持续降雨。 另一条在更南方汇入的河流表现出极端的流量变化，在东南苔原和北极山区源头的短暂夏季融化季节期间出现洪水。 河流入海口附近的最后一个例子显示了这两条河流的综合效应如何产生相反的流量模式：一年中的大部分时间流量适中，夏季融水带来的洪水会增加流量。

目标是在区域层面上动态显示河流的季节性大小，通过展示河流全年膨胀和收缩，为模拟增加真实感和可信度。

---

## 60. 欧洲批准首款唾液避孕产品——无需服药

**原文标题**: Europe approves first saliva-based contraceptive – no pill required

**原文链接**: [https://thenextweb.com/news/europe-approves-first-saliva-based-contraceptive-no-pill-required](https://thenextweb.com/news/europe-approves-first-saliva-based-contraceptive-no-pill-required)

本文报道了Inne公司的“Minilab”获得欧洲批准的消息。这是一种基于唾液的生育追踪器，现已获准用作避孕工具。该设备追踪每日孕酮水平，为传统避孕方法提供了一种无激素替代方案。临床研究表明，在完美使用情况下，其有效率达到100%，在典型使用情况下，有效率达到92%，与孕酮药丸相当。

Inne公司首席执行官Eirini Rapti强调，该设备使女性能够避免激素副作用，并更好地了解自己的身体。虽然经期追踪应用程序依赖于模式或症状，而体温追踪器可能不可靠，但Inne使用精确的激素测量方法，通过读取设备分析侧向流动试纸。结果会同步到配套应用程序，从而提供有关生育能力和避孕的见解。

Minilab目前在德国和奥地利有售，并计划扩展到英国。它以订阅方式提供，两年承诺的起价为每月24欧元。Rapti旨在使基于唾液的测试成为女性寻求控制生殖健康的广泛可用选择。

---

## 61. 使用开源情报，通过谷歌地图和披萨来检测重大世界事件

**原文标题**: Detecting Major World Events Using Osint, Through Google Maps and Pizza

**原文链接**: [https://signalslice.sebastianalexis.com/](https://signalslice.sebastianalexis.com/)

本文件概述了一种开源情报（OSINT）系统，该系统旨在通过使用谷歌地图数据监测特定位置的活动模式来检测重大世界事件，重点关注披萨餐厅和同志酒吧作为关键指标。该系统跟踪这些场所50英里半径范围内的交通流量，创建“披萨指数”和“同志酒吧指数”指标。较高的披萨指数表明活动增加，而较低的同志酒吧指数表明活动增加（反常）。

该系统每15分钟扫描127个活跃地点，并尝试识别交通模式中的异常情况。它监控谷歌地图API、扫描服务、数据管道和异常检测，提供系统状态概述。目前，系统显示中等威胁级别，尚未检测到任何异常情况。但是，数据管道受到速率限制。

系统包含实时活动源，并且可以分析1小时、6小时和24小时的数据。系统焦点区域标记为“CENTER”，并使用热图直观地表示活动。最后，Twitter账号“@PenPizzaReport”提供关于披萨活动、异常警报以及数据驱动分析的每小时更新，专门关注华盛顿特区披萨店。该分析基于开源情报，并全天候监控这些地点。

---

## 62. 内联C：在Haskell中编写内联C代码

**原文标题**: Inline-C: Write inline C in Haskell

**原文链接**: [https://github.com/fpco/inline-c/tree/master/inline-c](https://github.com/fpco/inline-c/tree/master/inline-c)

此 GitHub 仓库 `fpco/inline-c` 提供了一种在 Haskell 程序中直接编写内联 C 代码的方法。该项目本质上提供了一种将 C 代码无缝集成到 Haskell 中的机制，可能可以实现性能优化或访问 Haskell 中无法直接使用的 C 库。该仓库是公开的，并鼓励贡献。它已经引起了社区的极大兴趣，拥有 49 个 fork 和 296 个 star，表明其对于需要集成 C 代码的 Haskell 开发人员的价值和实用性。项目名称 “Inline-C” 本身清楚地传达了其核心功能。

---

## 63. 科学家用挖空的木头重现三万年前的航海之旅

**原文标题**: Scientists Retrace 30k-Year-Old Sea Voyage, in a Hollowed-Out Log

**原文链接**: [https://www.nytimes.com/2025/06/25/science/anthropology-ocean-migration-japan.html](https://www.nytimes.com/2025/06/25/science/anthropology-ocean-migration-japan.html)

无法访问文章链接。

---

## 64. 双语对大脑有好处吗？

**原文标题**: Is being bilingual good for your brain?

**原文链接**: [https://www.economist.com/science-and-technology/2025/06/27/is-being-bilingual-good-for-your-brain](https://www.economist.com/science-and-technology/2025/06/27/is-being-bilingual-good-for-your-brain)

本文探讨了关于双语认知优势的持续争论。 尽管大量研究表明，多语现象可以增强“执行功能”（计划、专注、适应新信息），甚至可能将痴呆症的发病时间推迟几年，但证据尚无定论。 一些声称具有这些优势的研究未能得到重复验证，导致专家质疑其有效性和影响的本质。 本文强调，尽管围绕这些认知优势存在不确定性，但学习语言仍然具有实际的好处，这表明双语的价值超越了潜在的脑力增强。

---

## 65. Rust 中的错误处理

**原文标题**: Error handling in Rust

**原文链接**: [https://felix-knorr.net/posts/2025-06-29-rust-error-handling.html](https://felix-knorr.net/posts/2025-06-29-rust-error-handling.html)

Felix的博客文章讨论了Rust中的错误处理，批评了为模块或Crate使用大型、单体错误枚举的常见做法。他认为这些枚举通常包含特定函数无法产生的错误变体，导致不必要的复杂性，并依赖文档来确定相关错误。

他建议了一种替代方法，将错误表示为单个结构体而不是枚举变体。他提到`terrors` crate作为一个例子，尽管他觉得它有些不方便，因为需要重复的`map_err`调用和指定错误集。

他更倾向的解决方案是`error_set` crate，它使用宏以简洁的方式为不同函数定义错误枚举，并自动生成转换的trait实现。这允许从变体和与其他错误集的联合创建错误集，并且如果错误集是函数错误集的子集，则`?`运算符有效。

他承认为结构体错误定义包装枚举可能很冗长，但他认为这是可以接受的。他还简要地提到了其他库，如SmartErr和一个丢失的crate，该crate基于函数体动态生成错误枚举。核心思想是从过于宽泛的错误枚举转向更具体和可管理的错误类型。

---

## 66. 显示 HN: 夏普比率计算工具

**原文标题**: Show HN: Sharpe Ratio Calculation Tool

**原文链接**: [https://www.fundratios.com/](https://www.fundratios.com/)

FundRatios offers a professional Sharpe Ratio Calculator designed for investment analysis. The tool helps investors measure risk-adjusted returns to make informed investment decisions. Users can upload their fund's historical Net Asset Value (NAV) data to get an instant Sharpe ratio analysis.

The Sharpe ratio measures an investment's performance relative to a risk-free asset, adjusted for risk, using the formula: (Return of portfolio - Risk-free rate) / Standard deviation of portfolio. A higher Sharpe ratio indicates better risk-adjusted performance, meaning better returns for the level of risk taken.

The calculator is valuable for comparing investments fairly by considering risk, optimizing portfolios to identify funds with the best return per unit of risk, and making data-driven investment choices. The tool uses the Secured Overnight Financing Rate (SOFR) as the risk-free rate and allows for assessing if returns are due to skill or excessive risk. FundRatios encourages users to start calculating Sharpe ratios to optimize their portfolios and make better investment decisions. The website also features a FAQ section addressing common questions about the Sharpe ratio.


---

## 67. Show HN: Summle – A little maths Game

**原文标题**: Show HN: Summle – A little maths Game

**原文链接**: [https://summle.net](https://summle.net)

生成摘要时出错

---

## 68. Personal care products disrupt the human oxidation field

**原文标题**: Personal care products disrupt the human oxidation field

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.ads7908](https://www.science.org/doi/10.1126/sciadv.ads7908)

生成摘要时出错

---

## 69. Magnetic Tape Storage Technology: usage, history, and future outlook

**原文标题**: Magnetic Tape Storage Technology: usage, history, and future outlook

**原文链接**: [https://dl.acm.org/doi/10.1145/3708997](https://dl.acm.org/doi/10.1145/3708997)

生成摘要时出错

---

## 70. Oracle signed $30B per year cloud deal with mystery customer

**原文标题**: Oracle signed $30B per year cloud deal with mystery customer

**原文链接**: [https://www.bloomberg.com/news/articles/2025-06-30/oracle-signed-cloud-services-deal-worth-30-billion-a-year](https://www.bloomberg.com/news/articles/2025-06-30/oracle-signed-cloud-services-deal-worth-30-billion-a-year)

生成摘要时出错

---

## 71. What LLMs Know About Their Users

**原文标题**: What LLMs Know About Their Users

**原文链接**: [https://www.schneier.com/](https://www.schneier.com/)

生成摘要时出错

---

## 72. Community Is Motivation on Tap

**原文标题**: Community Is Motivation on Tap

**原文链接**: [https://alanwu.xyz/posts/community/](https://alanwu.xyz/posts/community/)

生成摘要时出错

---

## 73. Show HN: I'm an airline pilot – I built interactive graphs/globes of my flights

**原文标题**: Show HN: I'm an airline pilot – I built interactive graphs/globes of my flights

**原文链接**: [https://jameshard.ing/pilot](https://jameshard.ing/pilot)

生成摘要时出错

---

## 74. Solving `Passport Application` with Haskell

**原文标题**: Solving `Passport Application` with Haskell

**原文链接**: [https://jameshaydon.github.io/passport/](https://jameshaydon.github.io/passport/)

生成摘要时出错

---

## 75. 精神分裂症是我们在悬崖边缘徘徊的头脑所付出的代价。

**原文标题**: Schizophrenia is the price we pay for minds poised near the edge of a cliff

**原文链接**: [https://www.psychiatrymargins.com/p/schizophrenia-is-the-price-we-pay](https://www.psychiatrymargins.com/p/schizophrenia-is-the-price-we-pay)

本文探讨了精神分裂症持续存在的进化之谜，尽管其对生殖适应性产生负面影响，并提出了“悬崖边缘适应度函数”模型作为一种可能的解释。该模型认为，与精神分裂症相关的基因可能在认知、语言或社交领域带来优势，从而在一定阈值内提高生殖适应性。然而，超过这个临界点，这些相同的特征可能会导致灾难性的后果并表现为精神分裂症。

文章使用培育赛马的类比来说明这个概念，选择速度会导致脆弱的腿骨容易骨折。同样，促进人类认知能力的特征在超过一定限度时可能会变得有害。

作者强调，自然选择偏爱略低于“悬崖”的性状值，从而最大化基因在群体中的传递，即使这意味着一小部分人“掉下悬崖”并发展成精神分裂症。这解释了为什么这种疾病是可遗传的但又是多基因的。

数学建模表明，有利于这些基因的正向选择是微弱的，刚好足以维持精神分裂症的流行，而又不易被检测到。此外，选择压力可能随着时间的推移而变化，一些与精神分裂症相关的基因显示出过去正向选择的证据，而随着种群接近适应度“悬崖”，最近则出现了负向选择。该模型调和了进化遗传学中看似矛盾的发现，并为理解基因、环境和精神分裂症的表现之间的复杂相互作用提供了一个引人注目的框架。

---

## 76. The Unsustainability of Moore's Law

**原文标题**: The Unsustainability of Moore's Law

**原文链接**: [https://bzolang.blog/p/the-unsustainability-of-moores-law](https://bzolang.blog/p/the-unsustainability-of-moores-law)

生成摘要时出错

---

## 77. Why Go Rocks for Building a Lua Interpreter

**原文标题**: Why Go Rocks for Building a Lua Interpreter

**原文链接**: [https://www.zombiezen.com/blog/2025/06/why-go-rocks-for-building-lua-interpreter/](https://www.zombiezen.com/blog/2025/06/why-go-rocks-for-building-lua-interpreter/)

生成摘要时出错

---

## 78. We ran a Unix-like OS on our home-built CPU with a home-built C compiler (2020)

**原文标题**: We ran a Unix-like OS on our home-built CPU with a home-built C compiler (2020)

**原文链接**: [https://fuel.edby.coffee/posts/how-we-ported-xv6-os-to-a-home-built-cpu-with-a-home-built-c-compiler/](https://fuel.edby.coffee/posts/how-we-ported-xv6-os-to-a-home-built-cpu-with-a-home-built-c-compiler/)

生成摘要时出错

---

## 79. Parsing JSON in Forty Lines of Awk

**原文标题**: Parsing JSON in Forty Lines of Awk

**原文链接**: [https://akr.am/blog/posts/parsing-json-in-forty-lines-of-awk](https://akr.am/blog/posts/parsing-json-in-forty-lines-of-awk)

生成摘要时出错

---

## 80. So you want to serialize some DER?

**原文标题**: So you want to serialize some DER?

**原文链接**: [https://alexgaynor.net/2025/jun/20/serialize-some-der/](https://alexgaynor.net/2025/jun/20/serialize-some-der/)

生成摘要时出错

---

## 81. Zero Trust for Bring Your Own Cloud (BYOC)

**原文标题**: Zero Trust for Bring Your Own Cloud (BYOC)

**原文链接**: [https://signoz.io/blog/zero-trust-bring-your-own-cloud/](https://signoz.io/blog/zero-trust-bring-your-own-cloud/)

生成摘要时出错

---

## 82. More on Apple's Trust-Eroding 'F1 the Movie' Wallet Ad

**原文标题**: More on Apple's Trust-Eroding 'F1 the Movie' Wallet Ad

**原文链接**: [https://daringfireball.net/2025/06/more_on_apples_trust-eroding_f1_the_movie_wallet_ad](https://daringfireball.net/2025/06/more_on_apples_trust-eroding_f1_the_movie_wallet_ad)

生成摘要时出错

---

## 83. The Death of the Middle-Class Musician

**原文标题**: The Death of the Middle-Class Musician

**原文链接**: [https://thewalrus.ca/the-death-of-the-middle-class-musician/](https://thewalrus.ca/the-death-of-the-middle-class-musician/)

生成摘要时出错

---

## 84. Thousands in Norway told they had won life-changing sums in lottery error

**原文标题**: Thousands in Norway told they had won life-changing sums in lottery error

**原文链接**: [https://www.theguardian.com/world/2025/jun/29/thousands-in-norway-told-they-had-won-life-changing-sums-in-lottery-error](https://www.theguardian.com/world/2025/jun/29/thousands-in-norway-told-they-had-won-life-changing-sums-in-lottery-error)

生成摘要时出错

---

## 85. Using DuckDB WASM and Cloudflare R2 to host and query big data (for almost free)

**原文标题**: Using DuckDB WASM and Cloudflare R2 to host and query big data (for almost free)

**原文链接**: [https://andrewpwheeler.com/2025/06/29/using-duckdb-wasm-cloudflare-r2-to-host-and-query-big-data-for-almost-free/](https://andrewpwheeler.com/2025/06/29/using-duckdb-wasm-cloudflare-r2-to-host-and-query-big-data-for-almost-free/)

生成摘要时出错

---

## 86. A rare asteroid flyby will happen soon, but NASA may be left on the sidelines

**原文标题**: A rare asteroid flyby will happen soon, but NASA may be left on the sidelines

**原文链接**: [https://arstechnica.com/features/2025/06/trump-budget-kills-nasas-golden-opportunity-to-see-a-killer-asteroid-up-close/](https://arstechnica.com/features/2025/06/trump-budget-kills-nasas-golden-opportunity-to-see-a-killer-asteroid-up-close/)

生成摘要时出错

---

## 87. Engineered Addictions

**原文标题**: Engineered Addictions

**原文链接**: [https://masonyarbrough.substack.com/p/engineered-addictions](https://masonyarbrough.substack.com/p/engineered-addictions)

生成摘要时出错

---

## 88. Unhooking from Amazon Ebooks

**原文标题**: Unhooking from Amazon Ebooks

**原文链接**: [https://remysharp.com/2025/06/29/unhooking-from-amazon-ebooks](https://remysharp.com/2025/06/29/unhooking-from-amazon-ebooks)

生成摘要时出错

---

## 89. IDF officers ordered to fire at unarmed crowds near Gaza food distribution sites

**原文标题**: IDF officers ordered to fire at unarmed crowds near Gaza food distribution sites

**原文链接**: [https://www.haaretz.com/israel-news/2025-06-27/ty-article-magazine/.premium/idf-soldiers-ordered-to-shoot-deliberately-at-unarmed-gazans-waiting-for-humanitarian-aid/00000197-ad8e-de01-a39f-ffbe33780000](https://www.haaretz.com/israel-news/2025-06-27/ty-article-magazine/.premium/idf-soldiers-ordered-to-shoot-deliberately-at-unarmed-gazans-waiting-for-humanitarian-aid/00000197-ad8e-de01-a39f-ffbe33780000)

生成摘要时出错

---

## 90. UV-C light kills nearly everything–except this unusual organism

**原文标题**: UV-C light kills nearly everything–except this unusual organism

**原文链接**: [https://www.science.org/content/article/uv-c-light-kills-nearly-everything-except-unusual-organism](https://www.science.org/content/article/uv-c-light-kills-nearly-everything-except-unusual-organism)

生成摘要时出错

---

## 91. Earth is trapping much more heat than climate models forecast

**原文标题**: Earth is trapping much more heat than climate models forecast

**原文链接**: [https://theconversation.com/earth-is-trapping-much-more-heat-than-climate-models-forecast-and-the-rate-has-doubled-in-20-years-258822](https://theconversation.com/earth-is-trapping-much-more-heat-than-climate-models-forecast-and-the-rate-has-doubled-in-20-years-258822)

生成摘要时出错

---

## 92. Show HN: AGL a toy language that compiles to Go

**原文标题**: Show HN: AGL a toy language that compiles to Go

**原文链接**: [https://github.com/alaingilbert/agl](https://github.com/alaingilbert/agl)

生成摘要时出错

---

## 93. Congress might block state AI laws for a decade

**原文标题**: Congress might block state AI laws for a decade

**原文链接**: [https://techcrunch.com/2025/06/27/congress-might-block-state-ai-laws-for-a-decade-heres-what-it-means/](https://techcrunch.com/2025/06/27/congress-might-block-state-ai-laws-for-a-decade-heres-what-it-means/)

生成摘要时出错

---

## 94. WorldVLA: Towards Autoregressive Action World Model

**原文标题**: WorldVLA: Towards Autoregressive Action World Model

**原文链接**: [https://arxiv.org/abs/2506.21539](https://arxiv.org/abs/2506.21539)

生成摘要时出错

---

## 95. Memory Safe Languages: Reducing Vulnerabilities in Modern Software Development [pdf]

**原文标题**: Memory Safe Languages: Reducing Vulnerabilities in Modern Software Development [pdf]

**原文链接**: [https://media.defense.gov/2025/Jun/23/2003742198/-1/-1/0/CSI_MEMORY_SAFE_LANGUAGES_REDUCING_VULNERABILITIES_IN_MODERN_SOFTWARE_DEVELOPMENT.PDF](https://media.defense.gov/2025/Jun/23/2003742198/-1/-1/0/CSI_MEMORY_SAFE_LANGUAGES_REDUCING_VULNERABILITIES_IN_MODERN_SOFTWARE_DEVELOPMENT.PDF)

生成摘要时出错

---

## 96. Continuous Glucose Monitoring

**原文标题**: Continuous Glucose Monitoring

**原文链接**: [https://www.imperialviolet.org/2025/06/29/cgm.html](https://www.imperialviolet.org/2025/06/29/cgm.html)

生成摘要时出错

---

## 97. Show HN: A tool to benchmark LLM APIs (OpenAI, Claude, local/self-hosted)

**原文标题**: Show HN: A tool to benchmark LLM APIs (OpenAI, Claude, local/self-hosted)

**原文链接**: [https://llmapitest.com/](https://llmapitest.com/)

生成摘要时出错

---

## 98. Tools I love: mise(-en-place)

**原文标题**: Tools I love: mise(-en-place)

**原文链接**: [https://blog.vbang.dk/2025/06/29/tools-i-love-mise/](https://blog.vbang.dk/2025/06/29/tools-i-love-mise/)

生成摘要时出错

---

## 99. An Important New Study on Phones and Kids

**原文标题**: An Important New Study on Phones and Kids

**原文链接**: [https://calnewport.com/an-important-new-study-on-phones-and-kids/](https://calnewport.com/an-important-new-study-on-phones-and-kids/)

生成摘要时出错

---

## 100. Most ints are not floats

**原文标题**: Most ints are not floats

**原文链接**: [https://www.johndcook.com/blog/2025/06/27/most-ints-are-not-floats/](https://www.johndcook.com/blog/2025/06/27/most-ints-are-not-floats/)

生成摘要时出错

---

