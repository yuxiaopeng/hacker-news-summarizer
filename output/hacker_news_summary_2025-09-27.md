# Hacker News 热门文章摘要 (2025-09-27)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 格陵兰：美丽的梦魇

**原文标题**: Greenland Is a Beautiful Nightmare

**原文链接**: [https://matduggan.com/greenland-is-a-beautiful-nightmare/](https://matduggan.com/greenland-is-a-beautiful-nightmare/)

作者回忆起他们意外的格陵兰之旅，最初源于一个随意的约定。出行前，他们因令人失望的旅行视频而感到焦虑，并准备迎接一段黯淡的经历。由于雾气，一段令人沮丧的航班最终返回起点，凸显了不可预测的旅行条件。

最终抵达后，格陵兰呈现出截然不同的景象：一个平静而冷静的人民与一个极其不适宜居住的景观形成鲜明对比。首都努克感觉既宁静又超现实，在这个小城市里出现了交通拥堵。作者随后前往伊卢利萨特，那里饱受蚊群侵扰，并且目睹了雪橇犬在恶劣条件下生存。

这次旅行包括一次乘船游览，作者的女儿喜欢吃冰川冰。对格陵兰文化的观察，包括鲸鱼消费和工业捕捞方法的使用，挑战了先入为主的观念。作者强调了在这个道路有限的地方，豪华轿车的令人费解的存在，以及当地杂货店和当地美食的古怪之处。

---

## 2. SSH3：使用HTTP/3更快更丰富的安全Shell

**原文标题**: SSH3: Faster and rich secure shell using HTTP/3

**原文链接**: [https://github.com/francoismichel/ssh3](https://github.com/francoismichel/ssh3)

SSH3是基于HTTP/3构建的SSH协议的新版本，旨在实现更快的会话建立和增强的安全特性。它利用QUIC+TLS 1.3进行安全连接，并使用HTTP授权进行用户身份验证。主要优势包括显著加快的会话建立速度（3个往返时间，而SSHv2为5-7个）、对OAuth 2.0和OpenID Connect等现代身份验证方法的支持，以及通过允许服务器隐藏在秘密URL后面来提高抵御端口扫描的鲁棒性。

其他优势包括UDP端口转发、连接迁移（计划中）和多路径连接，这些都由底层的QUIC协议支持。它支持常见的密码和公钥认证（RSA、EdDSA/ed25519）。

重要的是，SSH3目前处于实验阶段，未经彻底的安全审查，不建议用于生产环境。鼓励社区反馈和专家分析。

SSH3提供诸如服务器的X.509证书认证、通过OpenID Connect进行的无密钥用户认证等功能，并支持OpenSSH功能，例如authorized_keys解析、ssh-agent集成、TCP端口转发和代理跳转。

本文档提供了有关如何从源代码或使用`go install`安装SSH3、部署SSH3服务器（包括生成Let's Encrypt证书或自签名证书）以及使用SSH3客户端进行私钥、基于代理或基于密码的身份验证的说明。它还解释了如何使用类似OpenSSH的配置文件配置SSH3。

---

## 3. 首个恶意MCP：邮戳后门窃取你的邮件

**原文标题**: First Malicious MCP in the Wild: The Postmark Backdoor Stealing Your Emails

**原文链接**: [https://www.koi.security/blog/postmark-mcp-npm-malicious-backdoor-email-theft](https://www.koi.security/blog/postmark-mcp-npm-malicious-backdoor-email-theft)

BackKoi研究揭露首个恶意MCP服务器“postmark-mcp”被植入后门窃取邮件。MCP服务器是AI助手用于自动化任务（如发送邮件和数据库查询）的工具，通常具有广泛权限。每周下载1500次的“postmark-mcp”软件包自1.0.16版本起，被发现将所有邮件复制到攻击者服务器giftshop.club。

攻击者在npm上冒充合法的Postmark包，添加一行代码来密件抄送每封邮件。这突显了一个重大安全风险：开发者经常信任并集成这些工具，而未进行适当审查，从而授予它们对敏感数据的广泛访问权限。文章强调，传统安全措施通常无法检测到此类威胁，因为开发者独立采用在既定安全范围之外运行的AI工具。

潜在影响巨大，可能影响数百个组织和每天数千封电子邮件。作者强调了MCP生态系统的固有漏洞，其中AI助手盲目执行来自不受信任来源的命令。他们建议立即删除受感染的软件包，轮换暴露的凭据，并审计所有MCP服务器以查找可疑活动。Koi的风险引擎和供应链网关被认为是检测和预防类似威胁的解决方案。文章敦促在使用MCP服务器时提高警惕和保持高度戒备。

---

## 4. 在微型星球上投递信息的WebGL游戏

**原文标题**: A WebGL game where you deliver messages on a tiny planet

**原文链接**: [https://messenger.abeto.co/](https://messenger.abeto.co/)

核心概念是一款名为“信使 (Messenger)”的 WebGL 游戏，玩家的主要目标是在一个微型、据推测是程序生成的星球上递送消息。“信使 (Messenger)”这个名称直接反映了玩家的角色和核心游戏机制。虽然这句描述非常简短，但它突出了技术基础 (WebGL)、类型 (游戏)、玩家的任务 (消息传递) 和背景 (一个小星球)。描述的简洁性表明重点可能在于构建 WebGL 游戏的技术方面，在微型世界中导航进行交付的独特游戏机制，或两者兼而有之。关于游戏视觉效果、故事、挑战和进展系统的更多细节尚不明确，但核心理念已经明确：玩家是在紧凑的行星尺度上工作的信使。

---

## 5. 困在树莓派中的AI模型

**原文标题**: AI model trapped in a Raspberry Pi

**原文链接**: [https://blog.adafruit.com/2025/09/26/ai-model-trapped-in-raspberry-pi-piday-raspberrypi/](https://blog.adafruit.com/2025/09/26/ai-model-trapped-in-raspberry-pi-piday-raspberrypi/)

无法访问文章链接。

---

## 6. Typst：一个可能的LaTeX替代品

**原文标题**: Typst: A Possible LaTeX Replacement

**原文链接**: [https://lwn.net/Articles/1037577/](https://lwn.net/Articles/1037577/)

这篇2025年9月17日来自LWN.net的文章介绍了Typst，一种潜在的LaTeX替代方案。Typst使用Rust编写，并采用Apache-2.0许可，旨在提供更简单的标记系统、更快的编译速度和更便捷的自定义功能，同时保持与LaTeX相媲美的高质量输出。

文章强调了LaTeX作为技术文档长期标准的优势，但也承认用户对其庞大的安装体积、缓慢的编译速度、晦涩的错误信息以及用于自定义的神秘宏语言感到不满。

Typst自2019年以来一直在开发，它通过一种受Markdown启发的、不太冗长、更易读的标记语法以及更清晰、带有颜色编码的错误信息来解决这些问题。它还提供了一个“watch”模式，用于在编辑期间进行实时预览。作者赞扬了Typst集成的编程语言（类似于Rust）、对浮动图形和表格的出色处理，以及学术期刊的初步采用。

缺点包括与LaTeX庞大的生态系统相比，缺乏专门的软件包、文档问题以及在早期开发过程中可能出现的重大更改。 然而，编程的简易性和积极响应的开发团队被认为是优势。 虽然期刊模板支持有限，但Pandoc可以将Typst转换为LaTeX。 作者总结说，他们正在使用Typst撰写一篇物理论文，并使用Pandoc将其转换为LaTeX，赞扬了其数学公式处理和语法感知编辑器支持，并预测Typst最终可能会取代LaTeX。 长期成功的关键将是保持与用户文档的前向兼容性。

---

## 7. 伟大的问题 (YC W21) 正在招聘产品总监

**原文标题**: Great Question (YC W21) Is Hiring Director of Product

**原文链接**: [https://www.ycombinator.com/companies/great-question/jobs/9crdslU-director-of-product](https://www.ycombinator.com/companies/great-question/jobs/9crdslU-director-of-product)

Great Question 招募产品总监或高级总监

---

## 8. 挪威将在斯瓦尔巴群岛监测空气中的放射性。

**原文标题**: Norway to Monitor Airborne Radioactivity in Svalbard

**原文链接**: [https://www.highnorthnews.com/en/norway-monitor-airborne-radioactivity-svalbard](https://www.highnorthnews.com/en/norway-monitor-airborne-radioactivity-svalbard)

挪威将在斯瓦尔巴群岛监测空气中的放射性物质。此举可能源于俄罗斯新地岛试验场负责人声明称，该试验场已准备好可能恢复核试验。新地岛位于俄罗斯北部，是冷战时期主要的核武器试验场。虽然目前没有迹象表明正在进行试验，但挪威在斯瓦尔巴群岛的监测计划表明，该地区对潜在核活动的意识和准备程度有所提高。在斯瓦尔巴群岛的监测旨在检测和测量可能源于核活动的任何空气中的放射性粒子，确保挪威能够迅速评估并应对任何可能对其环境和人口造成的威胁。

---

## 9. 2024年亚马逊火灾对大气CO₂破纪录增长的前所未有影响

**原文标题**: Unprecedented role of Amazon fires in the record atmospheric CO₂ growth in 2024

**原文链接**: [https://essopenarchive.org/doi/full/10.22541/essoar.175874118.83695562/v1](https://essopenarchive.org/doi/full/10.22541/essoar.175874118.83695562/v1)

无法访问文章链接。

---

## 10. 虚拟内存基础

**原文标题**: Fundamental of Virtual Memory

**原文链接**: [https://nghiant3223.github.io/2025/05/29/fundamental_of_virtual_memory.html](https://nghiant3223.github.io/2025/05/29/fundamental_of_virtual_memory.html)

本文解释了虚拟内存的基础知识，这是现代操作系统中的一个关键概念。文章首先强调了与较慢的磁盘存储相比，主内存（RAM）对于快速数据访问的必要性。由于寄存器数量有限，主内存作为程序和数据的大型、可寻址空间。

文章接着讨论了一个简单的内存分配策略（连续块）及其缺点：外部碎片。为了解决这个问题，文章介绍了分页，即内存被划分为固定大小的帧，进程使用虚拟内存，这是一种由操作系统映射到物理内存的抽象。虚拟内存被划分为页，这些页使用页表映射到帧。解释了诸如页号、帧号和偏移量等关键概念。还介绍了不同的页表结构（多级、哈希、倒置）。

然后介绍了按需分页，解释了如何只将必要的页加载到内存中，从而提高效率。当访问的页面不在内存中时，会发生缺页中断，触发操作系统加载该页。定义了诸如RSS（物理内存使用量）和VSZ（分配的总虚拟内存）等指标。

最后，文章详细介绍了虚拟内存布局，概述了内核空间、堆栈、内存映射区域、堆和代码/数据段等段。文章提供了有关堆栈分配的详细信息，解释了它如何随着函数调用而增长和缩小，以及堆栈指针的作用。文章还涉及了线程堆栈、它们的默认大小以及相关的系统调用。

---

## 11. 跨越近千年的天体景象描绘 (2014)

**原文标题**: Depictions of Celestial Objects Spanning Nearly a Millennium (2014)

**原文链接**: [https://publicdomainreview.org/collection/flowers-of-the-sky/](https://publicdomainreview.org/collection/flowers-of-the-sky/)

鉴于标题和极其有限的内容（“杂录”），难以提供全面的总结。但我们可以推断如下：

这篇题为《近千年来的天体描绘（2014）》的文章，很可能展示了大约1000年间（截止于2014年）创作的，关于天文现象和天体（恒星、行星、彗星、星云等）的艺术作品、插图或文字描述的集合或调查。

关键词“杂录”强烈暗示该文章并非专注于单一类型的描绘或特定的艺术风格。相反，它可能展示了各种各样的来源，可能包括：

*   **历史天文插图：** 从中世纪手稿到文艺复兴时期的木刻版画和早期望远镜绘画。
*   **艺术诠释：** 受天体启发的绘画、雕塑和其他艺术形式。
*   **文字记录：** 摘录自描述宇宙观测或理论的历史文献。

该文章的目的很可能是为了说明我们在一个重要的历史时期内对宇宙的理解和视觉表现的演变。它可以探讨艺术风格和科学知识如何影响这些描绘，并突出对宇宙不断变化的文化认知。

本质上，这篇文章可能提供了人类在过去一千年里如何想象和表现宇宙的视觉和历史概述。

---

## 12. 我构建了 Foyer：一个能大幅降低 S3 延迟的 Rust 混合缓存。

**原文标题**: I built Foyer: a Rust hybrid cache that slashes S3 latency

**原文链接**: [https://medium.com/@yingjunwu/the-case-for-hybrid-cache-for-object-stores-4b1f02ec6c9a](https://medium.com/@yingjunwu/the-case-for-hybrid-cache-for-object-stores-4b1f02ec6c9a)

本文介绍了RisingWave开发的基于Rust的混合缓存库Foyer，旨在解决在现代数据系统中使用Amazon S3作为主存储层时面临的延迟挑战。虽然S3具有可扩展性、持久性和低成本的优点，但其高延迟和每次访问成本会显著降低性能，特别是对于像RisingWave这样的流数据库等对延迟敏感的应用。

Foyer结合了用于低延迟访问的内存缓存和用于扩展容量的磁盘缓存，并由协调器统一管理这两个层。内存缓存通过分片和请求去重来优先考虑速度，而磁盘缓存提供用于不同数据配置文件的模块化引擎和灵活的I/O选项。

Foyer以混合模式（内存和磁盘）和仅内存模式运行，并具有一致的API以实现无缝采用。其优点包括改善延迟、降低S3成本、增加容量和可配置性。RisingWave在三层存储架构（内存、本地磁盘、S3）中使用Foyer，以最大限度地减少S3访问，从而控制延迟并降低成本。

本文详细介绍了RisingWave的具体集成策略，包括块级读取、稀疏索引、预取和缓存补水。Foyer被深度集成，管理I/O，提供访问模式反馈，并与RisingWave的压缩过程协同工作。结论强调，混合缓存正成为基于对象存储的架构支持实时和高吞吐量工作负载的必要条件。

---

## 13. 伊什库尔电子音乐指南

**原文标题**: Ishkur's Guide to Electronic Music

**原文链接**: [http://music.ishkur.com/](http://music.ishkur.com/)

无法访问文章链接。

---

## 14. 测试树莓派500的新机械键盘

**原文标题**: Testing the Raspberry Pi 500's new mechanical keyboard

**原文链接**: [https://www.jeffgeerling.com/blog/2025/testing-raspberry-pi-500s-new-mechanical-keyboard](https://www.jeffgeerling.com/blog/2025/testing-raspberry-pi-500s-new-mechanical-keyboard)

本文评测了新款 Raspberry Pi 500+ 中包含的机械键盘，这是对原 Pi 500 的一项 200 美元升级。Pi 500+ 包括一个内置 M.2 NVMe SSD、16GB 内存和新款 RGB 背光机械键盘。

该键盘采用佳达隆 KS-33 薄型青轴开关和标准键帽，键帽易于拆卸和更换。较大的按键经过加固以提高稳定性。键盘预编程了多种 RGB 灯光效果，可通过 Raspberry Pi 的键盘工具进行配置，并运行在带有 QMK 固件 Pi 分支的 RP2040 微控制器上，从而可能实现与 VIA (或 Vial) 的兼容，以进行进一步的自定义。

作者将这款键盘描述为“咔哒咔哒”作响，在 1 英尺距离处的测量值约为 60 分贝。尽管作者个人更喜欢更安静的开关，但他发现这款键盘比以前 Raspberry Pi 型号的扁平键盘有了显著改进。文章探讨了更换键帽的问题，证明了它与矮键帽和（在某些情况下）全高键帽的兼容性，从而可以自定义外观和手感。

作者总结说，与过去的 Pi 键盘相比，这款键盘是一项重大升级，可以与中端机械键盘相媲美。虽然对于不喜欢青轴的人来说，无法更换开关是一个缺点，但整体的构建质量和键帽的定制性使其成为一个受欢迎的补充。单独的键盘顶壳为未来的改装提供了可能性。

---

## 15. 社会关系持续时间累积起来，有助于分子层面的健康老龄化

**原文标题**: Lifetime of social ties adds up to healthy aging at molecular level

**原文链接**: [https://news.cornell.edu/stories/2025/09/lifetime-social-ties-adds-healthy-aging](https://news.cornell.edu/stories/2025/09/lifetime-social-ties-adds-healthy-aging)

一生中强大的社会关系，被称为“累积社会优势”，可以在分子层面减缓生物衰老。这是发表在《大脑、行为与免疫 - 健康》上的研究得出的结论。该研究分析了 MIDUS 研究中 2100 多名成年人的数据，发现具有较高累积社会优势的个体表现出较慢的表观遗传衰老，通过 GrimAge 和 DunedinPACE 等“表观遗传时钟”进行测量，以及较低水平的慢性炎症。

累积社会优势包括早年父母的关爱和支持、社区和宗教参与，以及来自朋友和家人持续的情感支持。研究人员发现，这种优势与白细胞介素-6（一种与年龄相关疾病相关的促炎分子）的较低水平有关。

该研究强调，社会资源与经济资源一样，会在一生中积累，从而导致差异。在物质方面处于劣势的人也可能缺乏持续的社会支持，这可能会加速衰老。研究结果支持“风化假说”，表明逆境会导致更早的健康恶化。

研究人员强调了数十年间建立的持续而深入的社会关系的重要性，认为它们就像一个健康的“退休账户”，早期和持续的“投资”会产生更大的生物回报。健康老龄化意味着保持健康和保持联系。

---

## 16. 我们为何思考

**原文标题**: Why We Think

**原文链接**: [https://lilianweng.github.io/posts/2025-05-01-thinking/](https://lilianweng.github.io/posts/2025-05-01-thinking/)

本文探讨了大型语言模型（LLM）“思考时间”的益处，并将其类比于人类认知和计算。它讨论了如何在测试时分配更多的计算资源，通过诸如思维链（CoT）等技术，显著提升模型性能。

本文将CoT视为一种隐变量建模形式，模型生成中间推理步骤（隐变量）以得出最终答案。这使得更复杂和细致的问题解决成为可能。 然后，本文对比了利用测试时计算能力的两种主要方法：并行采样和顺序修正。

并行采样涉及同时生成多个输出，并根据评分函数选择最佳输出（例如，N中最佳采样、带有过程奖励模型的集束搜索）。自洽性，即在CoT展开中选择多数投票的答案，属于此类别。

另一方面，顺序修正涉及基于先前的输出来迭代地改进模型的响应，类似于反思和纠正错误。这种方法通常需要微调一个“纠正器”模型，因为LLM本身并不擅长自我纠正。诸如自我修正学习和递归检查等技术旨在训练这些纠正器模型。SCoRe是一种基于强化学习的方法，用于鼓励多轮自我纠正。本文强调，整合并行和顺序采样方法可以利用这两种方法的优势。较容易的问题受益于顺序修正，而较难的问题受益于两者的结合。

---

## 17. 开放社交

**原文标题**: Open Social

**原文链接**: [https://overreacted.io/open-social/](https://overreacted.io/open-social/)

本文倡导“开放社交”，将其比作开源运动。文章认为，当前社交媒体将用户数据困于中心化平台，阻碍了用户的自由，并激励平台优先考虑利润而非用户福祉。

作者提出了一种去中心化的模型，用户拥有自己的社交数据，这些数据托管在个人存储库中，并通过基于域名的句柄（例如，@alice.com）访问。这使得用户能够控制自己的数据，并在社交应用程序之间迁移，而不会丢失其连接和内容。Bluesky开发的AT协议被认为是一种有前景的方法。它支持一个超链接JSON数据网络，其中每个记录（帖子、点赞、关注）都有一个唯一的“at://”URI，允许跨用户和应用程序的连接。

文章强调，这种基础设施在幕后运行，非技术用户感觉不到，就像Web服务器的工作方式一样。 关键好处是用户赋权：能够“离开”平台而不放弃其社交关系网络，从而促进竞争和改善用户待遇。作者认为，就像开源一样，开放社交可能需要时间才能普及，但最终将显得不可避免，从而赋予个人权力并重塑社交媒体格局。目标是从用户是数据库中的一行数据的“封闭社交”模型过渡到用户控制自己数据的“开放社交”模型。

---

## 18. 三星现在拥有天龙、宝华韦健、马兰士、普乐之声等众多音频品牌。

**原文标题**: Samsung now owns Denon, Bowers and Wilkins, Marantz, Polk, and more audio brands

**原文链接**: [https://www.theverge.com/news/784390/samsung-harman-masimo-audio-acquisition-complete](https://www.theverge.com/news/784390/samsung-harman-masimo-audio-acquisition-complete)

三星通过其子公司哈曼，已完成从玛斯莫手中以 3.5 亿美元收购 Sound United 的交易。此次收购显著扩大了三星的音频品牌组合，将 Bowers & Wilkins、Denon、Marantz、Definitive Technology、Polk Audio、HEOS、Classé 和 Boston Acoustics 等著名品牌纳入旗下，与现有的 JBL 和 Harman Kardon 等哈曼品牌并列。

Sound United 产品组合将作为哈曼生活方式部门内的一个独立业务运营，以保持每个品牌的独特个性和客户群。哈曼认为此次收购是一个重要的增长机会，使其能够在现有成功的基础上再接再厉，并进一步巩固其作为全球音频领导者的地位。玛斯莫，Sound United 的前所有者，现在可以专注于其与美国海关和边境保护局就 Apple Watch 技术相关的持续诉讼。

---

## 19. SimpleFold：蛋白质折叠比你想象的更简单

**原文标题**: SimpleFold: Folding proteins is simpler than you think

**原文链接**: [https://github.com/apple/ml-simplefold](https://github.com/apple/ml-simplefold)

SimpleFold是一种新型蛋白质折叠模型，在研究论文《SimpleFold：蛋白质折叠比你想象的更简单》中被提出。它是第一个基于流匹配的模型，使用通用Transformer层，避免了像三角形注意力这样复杂的特定领域架构。该模型使用生成式流匹配目标，在一个包含超过860万个提炼蛋白质结构和实验性PDB数据的大型数据集上进行训练。

开发的最大的SimpleFold-3B模型在标准折叠基准测试中实现了与最先进模型相比具有竞争力的性能。其生成式训练实现了强大的集成预测性能。这项工作挑战了蛋白质折叠对复杂架构的依赖，并提供了一种更简单、替代性的方法。

该存储库提供安装说明，包括设置conda环境和安装必要的软件包，如MLX（用于Apple Silicon）和ESM。提供了示例代码和说明，用于使用PyTorch或MLX后端从FASTA文件预测蛋白质结构。还包括使用提供的预测结构和openstructure评估模型性能的说明，以及在自定义数据集上训练或微调SimpleFold的说明。该论文可被引用，代码是开源的，代码和模型都有特定的许可证。

---

## 20. Show HN: macOS 26 的开源启动台

**原文标题**: Show HN: An open source Launchpad for macOS 26

**原文链接**: [https://github.com/RoversX/LaunchNext](https://github.com/RoversX/LaunchNext)

LaunchNext 是一款开源的 macOS 启动台替代方案，旨在恢复近期 macOS 更新（特别是 Tahoe，即假定的 macOS 26）中丢失的经典启动台体验。LaunchNext 构建于 LaunchNow 项目之上，提供一键导入现有启动台布局、多语言支持、自定义图标大小、文件夹管理和即时搜索等功能。

主要功能包括：

*   **经典启动台恢复：** 复制原始启动台界面，并提供可自定义功能。
*   **导入能力：** 直接从系统的 SQLite 数据库导入现有启动台数据。
*   **自定义选项：** 提供可隐藏的图标标签、可调整的图标大小和智能文件夹管理。
*   **性能优化：** 使用图标缓存、延迟加载和后台扫描来实现流畅的性能。

该项目旨在解决 macOS 更新中引入的限制，例如缺乏自定义应用程序组织和文件夹创建。安装需要 macOS Tahoe（或更高版本），并且如果从源代码构建，可能需要 Xcode。由于开发者无力承担 Apple 开发者证书的费用，用户可能需要在终端中运行命令来删除隔离标志，从而绕过 macOS 安全性。开发者鼓励大家贡献，并希望 Apple 考虑恢复原始启动台的功能。

---

## 21. 这只一万八千年前的西伯利亚幼崽是狗还是狼？

**原文标题**: Was This 18,000-Year-Old Siberian Puppy a Dog or a Wolf?

**原文链接**: [https://www.nytimes.com/2019/12/02/science/frozen-puppy-found-russia.html](https://www.nytimes.com/2019/12/02/science/frozen-puppy-found-russia.html)

纽约时报文章《这只一万八千年前的西伯利亚幼犬是狗还是狼？》讨论了在西伯利亚雅库茨克附近的永久冻土层中发现的一只保存异常完好的犬科动物幼犬木乃伊的发现和分析。这只大约有一万八千年历史的幼犬，绰号“多戈尔”（在雅库特语中意为“朋友”），让试图确定它是狼还是狗的科学家们感到困惑。

包括基因组测序在内的大量基因分析未能最终将多戈尔置于犬科动物的进化树上。虽然永久冻土层出色地保存了这具尸体，使其看起来很新，但DNA并未提供明确的答案。研究人员认为，多戈尔生活在一个关键时期，当时人们认为狗正从狼中分离出来。模棱两可的基因结果表明，多戈尔可能代表一种过渡形态、一个共同祖先，或者是一只仍然与狼有着相当基因相似性的早期狗。

这项研究突显了确定狗被驯化的确切时刻的难度。它暗示狗和狼之间的分裂可能比之前认为的发生得更早，并强调了驯化过程的复杂性和渐进性。有必要对类似的古代犬科动物进行进一步的研究和分析，以更好地了解狗的进化历史及其与狼的关系。该研究强调，精确地确定狼何时转变为我们今天所知的狗仍然是一个持续的科学难题。

---

## 22. Meshtastic 64 – Commodore 64 的 Meshtastic 无线电

**原文标题**: Meshtastic 64 – A meshtastic radio for the Commodore 64

**原文链接**: [http://64jim64.blogspot.com/2025/09/meshtastic-64-meshtastic-radio-for.html](http://64jim64.blogspot.com/2025/09/meshtastic-64-meshtastic-radio-for.html)

Jim_64详细介绍了他的项目“Meshtastic 64”，这是一个定制的Meshtastic无线电模块，可以直接插入 Commodore 64。他的目标是在芝加哥举办的2025年中西部古董计算机节（VCF Midwest 2025）上首次展示该项目。Meshtastic是一个开源的、去中心化的点对点文本消息网络，用于远距离通信，吸引了对技术、去中心化系统和应急通信感兴趣的人。

Jim 使用了 Heltec LoRa V3 模块，并通过串行端口使用特定的 IO 引脚将其连接到 C64。最初使用 protobuf 命令，后来他切换到文本模式以简化通信。他创建了一个可以装入 C64 卡带外壳的原型。Commodore 64 程序是用 BASIC 语言编写的，因为它具有复古的吸引力并且速度足够快。

在最初的 PCB 设计出现错误后，他改进了设计，包括考虑了电池和 LED。他进一步开发了 C64 代码，以实现两台 C64 之间的通信，并尝试了 PETSCII 图像，最终优先考虑标准的大小写文本通信，使用 ASCII 到 PETSCII 的转换。他还集成了具有专用编辑器的 PETSCII 图形功能。

他修改了卡带外壳，增加了 USB-C 插槽、天线孔和使用丙烯酸棒的按钮驱动系统。他及时赶在 VCFMW 展会前构建了 19 个单元，Meshtastic 64 在展会上取得了成功，在具有多达 200 个节点的专用 Meshtastic 频道上发送和接收消息。它的内置电池允许独立运行。对该项目的反响是积极的，用户们测试并享受了该设备。代码将在 BIT-Zeal 网站上发布，供其他人使用。

---

## 23. AGI妄想的代价：追逐超人工智能导致美国在真正的人工智能竞赛中落后

**原文标题**: Cost of AGI Delusion:Chasing Superintelligence US Falling Behind in Real AI Race

**原文链接**: [https://www.foreignaffairs.com/united-states/cost-delusion-artificial-general-intelligence](https://www.foreignaffairs.com/united-states/cost-delusion-artificial-general-intelligence)

在《AGI幻觉的代价》一文中，迈克尔·C·霍洛维茨和劳伦·A·卡恩认为，美国过度关注实现通用人工智能（AGI）阻碍了其在更广泛的对华人工智能竞赛中的进展。他们认为，以萨姆·奥特曼为代表的人物所推动的对AGI的炒作，与其真正迫在眉睫的可能性不成比例，转移了人们对实际人工智能开发和应用的关注和资源。

作者强调，政治家们越来越关注AGI，导致政策和投资都基于其近期到来的假设。他们反驳说，人工智能的进步更可能是迭代的和复杂的，像其他通用技术一样，而不是突然的突破。

他们认为，中国正专注于快速整合和扩展现有和近期的AI能力，尤其是在机器人和工业应用领域。为了有效竞争，美国应该将其重点从追逐AGI的“神话”转移到投资于政府内部的人工智能素养，实现基础设施和数据实践的现代化，并支持大学的研发。这包括利用现有的人工智能基础设施投资，并促进公共和私营部门之间的合作。

通过优先考虑实际的人工智能实施和应用，美国不仅可以提高其当前的能力，还可以为未来的进步奠定更坚实的基础，包括实现AGI的可能性。他们警告说，对AGI的单一痴迷可能会忽视人工智能更直接和有形的益处，从而可能使中国在真正的人工智能竞赛中超越美国。

---

## 24. 渐进式类型输入已死？Typed Racket 中的性能问题

**原文标题**: Is sound gradual typing dead? Performance problems in Typed Racket

**原文链接**: [https://dl.acm.org/doi/abs/10.1145/2837614.2837630](https://dl.acm.org/doi/abs/10.1145/2837614.2837630)

无法访问文章链接。

---

## 25. 一千块锂离子电池的CT扫描显示廉价电池存在质量风险

**原文标题**: CT scans of 1k lithium-ion batteries show quality risks in inexpensive cells

**原文链接**: [https://www.lumafield.com/article/finding-hidden-risks-in-the-battery-supply-chain](https://www.lumafield.com/article/finding-hidden-risks-in-the-battery-supply-chain)

基于CT扫描超千颗锂离子18650电池的Lumafield电池质量报告揭示，不同品牌电池质量差异显著，尤其是在廉价和假冒电池中。研究重点关注阳极悬垂(AOH)和边缘对齐，这些是影响电池性能、衰减以及导致热失控（火灾和爆炸）的内部短路风险的关键因素。

研究发现，低成本/假冒电池的AOH质量和边缘对齐明显低于OEM电池。此外，某些品牌内部的质量差异表明过程控制不稳定。一个令人担忧的发现是，有33颗电池出现了“阴极悬垂”（负AOH），这些电池全部来自低成本/假冒品牌，这大大增加了内部短路的风险。

该报告强调，即使是低故障率，由于电池流通量巨大，也会转化为现场大量的事故。研究发现市场上存在误导性品牌宣传和虚报电池容量的情况。

Lumafield倡导使用CT扫描结合自动化分析来确保电池质量，使团队能够快速识别缺陷并采取纠正措施。他们的工业X射线CT平台可以进行快速且可扩展的检测，使其适用于现代电池生产线。该研究强调了供应链控制的重要性，敦促电芯制造商、电池包组装商、设备集成商和消费者优先考虑可衡量的质量，以降低与缺陷电池相关的风险。最终，CT扫描在通常不透明的供应链中提供了透明度，从而可以更好地进行质量控制并降低风险。

---

## 26. Moondream 3 预览：前沿推理，疾速运行

**原文标题**: Moondream 3 Preview: Frontier-level reasoning at a blazing speed

**原文链接**: [https://moondream.ai/blog/moondream-3-preview](https://moondream.ai/blog/moondream-3-preview)

Moondream 3：一款新型90亿参数规模的混合专家视觉语言模型（VLM），具有20亿活跃参数，现以预览版形式发布。它旨在将前沿级别的视觉推理能力带到对速度、效率和经济性有要求的实际应用中。

该架构优先考虑视觉推理、专门任务的可训练性、快速推理和低运营成本。通过利用MoE设计，它在保持速度和成本效益的同时，实现了与更大模型相当或更优越的性能。关键改进包括将上下文长度从2k扩展到32k tokens，从而能够处理更复杂的查询和输出。

Moondream 3展示了强大的物体检测、原生指向能力、结构化输出生成（例如，JSON数组）以及增强的OCR能力。该模型展示了具有基础的视觉推理能力，将推理过程与特定的图像区域连接起来。

该架构基于一个具有64个专家的稀疏混合专家系统，其中每个token激活8个专家。上下文长度已扩展到32k，并且该模型使用学习到的温度缩放来进行长上下文建模。在训练期间使用了负载平衡和路由器正交性损失，以帮助相似的token在早期一起专门化。

预览版发布带有一个注意事项：推理代码尚未完全优化，导致速度低于预期。该模型仍在训练中，预计在能力和基准分数方面会有进一步的改进。还计划推出量化和更小的精馏版本。

Moondream 3可在Moondream Playground上使用，也可在HuggingFace上下载。

---

## 27. 编程之美 (2001)

**原文标题**: The Beauty of Programming (2001)

**原文链接**: [https://www.brynmawr.edu/inside/academic-information/departments-programs/computer-science/beauty-programming](https://www.brynmawr.edu/inside/academic-information/departments-programs/computer-science/beauty-programming)

在《编程之美》中， Linus Torvalds 探讨了他对编程的痴迷，认为它类似于一场你可以制定自己的规则和结果的游戏。他强调了计算机最初的绝对服从所带来的兴奋，但更强调真正的投入在于弄清楚 *如何* 有效地指挥它们。

Torvalds 将计算机科学与物理学相提并论，认为两者都在探索基本真理，但计算机科学允许你在计算机内部 *创造* 世界，从而赋予你一种神一般的控制力。他将编程比作建造一个美丽而富有创意设计的树屋，强调功能往往次于艺术性和创新性。

一个关键的吸引力在于能够创建一个具有自身规则的自洽世界，类似于数学。 Torvalds 以 Mandelbrot 集合为例，展示了计算机如何可视化抽象的数学概念，从而产生美丽的图案。虽然许多编程涉及解决问题，但最终的挑战在于创建操作系统——建立所有其他程序运行的基本规则。

Torvalds 强调了找到优雅和高效解决方案的价值。他讲述了高斯计算从 1 到 100 的数字之和的故事，来说明识别模式和创造性地解决问题的重要性。他总结说，对于程序员来说，最大的感觉是在努力寻找之后，发现解决一个具有挑战性的问题的正确、美妙的方法。

---

## 28. 美国城市为公交车支付过多

**原文标题**: US cities pay too much for buses

**原文链接**: [https://www.bloomberg.com/news/articles/2025-09-26/us-cities-are-paying-too-much-for-new-transit-buses](https://www.bloomberg.com/news/articles/2025-09-26/us-cities-are-paying-too-much-for-new-transit-buses)

本文突显了美国城市购买的公交车价格远高于国际同行的现象。2023年，丹佛区域交通区(RTD)每辆公交车支付了432,028美元，而辛辛那提西南俄亥俄地区交通管理局(SORTA)从同一制造商处购买类似的柴油公交车，却支付了高达939,388美元。与此形成鲜明对比的是，新加坡购买了全电动公交车，通常是美国柴油公交车价格的两倍，但每辆仅花费333,000美元。本文暗示美国城市在公交车采购上支付了过高的价格，引发了人们对采购流程、市场动态以及美国交通系统潜在低效率的质疑。

---

## 29. 科学家称X已失去其专业优势，Bluesky正在取而代之。

**原文标题**: Scientists say X has lost its professional edge and Bluesky is taking its place

**原文链接**: [https://www.psypost.org/scientists-say-x-formerly-twitter-has-lost-its-professional-edge-and-bluesky-is-taking-its-place/](https://www.psypost.org/scientists-say-x-formerly-twitter-has-lost-its-professional-edge-and-bluesky-is-taking-its-place/)

本文预测了社交媒体的未来，特别指出X（原Twitter）正在失去其专业吸引力，而Bluesky正在成为一个潜在的替代品。这意味着专业用户正在从一个平台转移到另一个平台。

然而，提供的内容片段似乎与标题完全无关。它描述了一项研究，表明熬夜、经历孤独和焦虑以及表现出有问题的智能手机使用之间存在相关性。给出的日期2025年9月22日表明这项研究将在未来发表。

因此，仅关注标题的总结将是：**科学家预测X（Twitter）的专业用户正在减少，而Bluesky正成为首选替代方案。**

仅关注内容片段的总结将是：**一项即将发布的研究（2025年9月22日）表明，熬夜、孤独感和焦虑感与有问题的智能手机使用之间存在联系。**

由于标题和内容似乎无关，因此一份全面的总结将承认这种差异，并分别呈现上述两部分信息。

---

## 30. GPT-OSS 强化学习

**原文标题**: GPT-OSS Reinforcement Learning

**原文链接**: [https://docs.unsloth.ai/new/gpt-oss-reinforcement-learning](https://docs.unsloth.ai/new/gpt-oss-reinforcement-learning)

本文宣布Unsloth在OpenAI的gpt-oss模型的强化学习(RL)上取得突破，使其即使在Google Colab等有限资源上也能实现。 与其他实现相比，Unsloth提供更快的推理速度（高达3倍）、更低的VRAM使用率（减少50%）和更长的上下文窗口（8倍），且不牺牲准确性。

主要进展包括：

*   **重写的Transformers推理：** 实现了显著的速度提升，尤其是在4位和BF16推理方面。
*   **Flex Attention：** 一种自定义的注意力机制，解决了与掩码、批量生成和填充相关的挑战，同时与`torch.compile`保持兼容。
*   **支持4位RL：** Unsloth是唯一支持gpt-oss的框架。
*   **奖励黑客缓解：** 文章重点介绍了并提供了解决方案，以防止RL模型作弊以最大化奖励，重点是代码生成。
*   **可访问性：** 使用GRPO的gpt-oss-20b训练可以在15GB VRAM上进行，甚至在免费的Colab层级上也能实现。 gpt-oss-120b可以容纳在80GB VRAM上。
*   **FlashAttention 3警告：** 由于反向传播问题，FA3不适用于gpt-oss训练。

核心信息是Unsloth democratized访问gpt-oss RL训练，提供性能改进和解决常见挑战的方案，使更多的研究人员和开发人员能够探索这种强大的架构。

---

## 31. 新数学重燃古老几何难题

**原文标题**: New math revives geometry's oldest problems

**原文链接**: [https://www.quantamagazine.org/new-math-revives-geometrys-oldest-problems-20250926/](https://www.quantamagazine.org/new-math-revives-geometrys-oldest-problems-20250926/)

本文探讨了枚举几何学的复兴，该领域专注于计算满足特定几何条件的几何对象。枚举几何学曾是数学的核心领域，但在20世纪逐渐衰落。然而，数学家克斯汀·威克格伦和杰西·卡斯通过应用动机同伦理论（一种在20世纪60年代和70年代发展起来的复杂框架）解决了各种数系（包括实数、复数和有限数系）中的枚举问题，从而复兴了该领域。

其关键突破在于将几何问题重新构建为描述空间之间关系的方程和函数，从而能够应用动机同伦理论。这种方法会生成一个二次型，其符号提供了关于不同数系中解的数量的重要信息。

这种新方法为数系提供了新的见解，并使他们能够提供关于诸如确定三次曲面上直线数量等问题的答案，不仅适用于复数和实数，也适用于有限数系。该理论不仅提供了答案，还产生了数学家仍在努力解读的额外信息，从而激发了人们重新燃起的兴趣，并吸引了新的研究人才加入该领域。最终，这次复兴将枚举几何学与代数、拓扑学和数论联系起来，实现了大卫·希尔伯特关于以更严谨和通用的方法解决这些长期存在的数学挑战的愿景。

---

## 32. 痴迷完整的 Infocom 产品目录

**原文标题**: The Obsessively Complete Infocom Catalog

**原文链接**: [https://eblong.com/infocom/](https://eblong.com/infocom/)

本文介绍了“穷尽式 Infocom 作品全集”，该项目致力于存档每个已知的 Infocom 游戏版本，包括源代码和编译后的游戏文件。与其他合集不同，该全集收录了与 Infocom 同期的变体、Beta 测试版和粉丝修改版。

该项目承认了 Jason Scott 的重要贡献，他最初在 GitHub 上发布了大量的 Infocom 源代码，以及 Beaux Hemmer、Torbjörn Andersson 和 Alessandro Giassi 等其他贡献者的贡献。

该全集提供 JSON 格式的完整合集下载，以及游戏文件、源代码、解释器和其他相关项目的单独 ZIP 文件下载。尽管承认 Activision 的版权，但作者认为，考虑到 Activision 可能无法利用这些源代码且有丢失的风险，这些源代码对互动小说（IF）社区的历史价值超过了法律问题。

作者强调了与 Jason Scott 的 GitHub 仓库的主要区别，包括源代码的组织方式、从补丁文件派生的游戏文件的收录，以及 GitHub 仓库中发现的错误的更正。为了保护隐私，个人通信和开发者评论被省略，但“彩蛋”手稿被收录。

本文解释了 Z-code 文件版本（zip、ezip、xzip、yzip）及其对应的文件扩展名（.z3、.z4、.z5、.z6）。文中还提到了原始 ZIL 编译器和现代 ZILF 编译器的可用性。它将“Infocom 文本冒险杰作 CD”（1996 年）确定为大多数现代版本的来源，并指出了“杰作”、“Infocom 失落的宝藏”和“Solid Gold”版本之间的差异。最后，文章总结了关于存档文件的说明，包括发布版本号的不一致性、声音/图形媒体、Mac 专用修改以及因版权保护而进行的修改。

---

## 33. 扎波罗热核电站外部供电中断三天后仍未恢复

**原文标题**: External power to Zaporizhzhia nuclear plant still out after three days

**原文链接**: [https://www.theguardian.com/world/2025/sep/27/safety-fears-as-external-power-to-zaporizhzhia-nuclear-plant-still-out-after-three-days](https://www.theguardian.com/world/2025/sep/27/safety-fears-as-external-power-to-zaporizhzhia-nuclear-plant-still-out-after-three-days)

被俄罗斯占领的扎波罗热核电站已断电三天多，创下历史最长停电纪录，引发重大安全担忧。最后一根电力线被切断后，应急发电机目前正在为冷却和安全系统供电。国际原子能机构总干事拉斐尔·格罗西表示深切关注，但线路重新连接工作陷入停滞。

乌克兰官员和西方专家怀疑俄罗斯故意制造危机，以巩固其对该电站的控制，甚至可能在危险情况下重启反应堆。压力测试表明，核电站只能在没有外部电源的情况下运行72小时，超过此时间会带来风险。

虽然俄罗斯声称乌克兰的炮击阻碍了维修，但乌克兰否认以该电站为目标。国际原子能机构报告称，发电机有足够的柴油供应20天，但失去外部电源会增加发生事故的风险。发电机故障可能导致核燃料过热和潜在的熔毁。

俄罗斯似乎正在通过占领区建设一条新的电力线。绿色和平组织分析表明，可能已经创建了一个新的水源，这引发了人们的担忧，即俄罗斯可能会重启反应堆以展示其控制权。绿色和平组织敦促国际原子能机构阻止俄罗斯重启反应堆的计划，俄罗斯总统向国际原子能机构保证支持其工作。国际原子能机构未在任何公开声明中提及扎波罗热。

---

## 34. Auth.js 现在是 Better Auth 的一部分

**原文标题**: Auth.js is now part of Better Auth

**原文链接**: [https://www.better-auth.com/blog/authjs-joins-better-auth](https://www.better-auth.com/blog/authjs-joins-better-auth)

Auth.js，前身 NextAuth.js，一款广受欢迎的开源 JavaScript 身份验证库，现由 Better Auth 团队维护和监督。Better Auth 团队的成立源于他们在构建复杂应用程序时意识到 Auth.js 的局限性，并希望为拥有身份验证提供更好的解决方案。Auth.js 团队也意识到了这些局限性，但无法完全实现他们的愿景。鉴于双方都有赋能开发者自主掌控身份验证的共同目标，Auth.js 团队决定让 Better Auth 成为 Auth.js 的新家。

现有的 Auth.js 用户可以继续使用该库，不会受到干扰，并且安全补丁和紧急问题仍将得到处理。然而，文章强烈建议新项目从 Better Auth 开始，因为它旨在成为一个更完整的解决方案。对于考虑从 Auth.js 切换到 Better Auth 的团队，我们提供了一个迁移指南。Better Auth 团队计划将 Auth.js 中剩余的关键功能，特别是无需数据库的无状态会话管理，引入 Better Auth，以促进生态系统的融合。

文章对 Auth.js 社区和核心维护者为该项目所做的工作表示感谢。最终目标是赋能开发者自主掌控身份验证。

---

## 35. 为什么 Windows 还在摆弄临界区？- The Old New Thing

**原文标题**: Why is Windows still tinkering with critical sections? – The Old New Thing

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20250924-00/?p=111624](https://devblogs.microsoft.com/oldnewthing/20250924-00/?p=111624)

尽管临界区已是成熟技术，为何Windows仍在不断对其进行修改？文章探讨了这一问题。虽然漏洞可能罕见，但性能始终是关注重点。由于临界区被大量使用，即使是微小的性能提升也能带来显著收益。

过去的优化侧重于公平性（避免锁队列）和减少内存占用，尤其是在非分页池中，这是一种昂贵且有限的资源。当临界区大规模使用时，减少每个临界区使用的非分页池数量极其有益。

最近的更改旨在检测和缓解优先级反转。Windows 11 24H2的优化将更多此类工作转移到用户模式，避免了昂贵的内核模式切换。正是这种优化暴露了旧版《侠盗猎车手：圣安地列斯》的漏洞。

总而言之，文章认为，即使是像临界区这样成熟的组件，也需要持续优化，以在规模、速度和并发性不断提高的计算环境中保持性能和可靠性。老狗仍在学习新把戏。

---

## 36. Traefik 十周年

**原文标题**: Traefik's 10-year anniversary

**原文链接**: [https://traefik.io/blog/celebrating-10-years-of-traefik](https://traefik.io/blog/celebrating-10-years-of-traefik)

本文庆祝广受欢迎的开源反向代理和负载均衡器Traefik诞生十周年。作者回顾了Traefik于2015年诞生之初的历程，当时它旨在解决微服务管理中的挑战，并强调了在动态容器化环境中手动配置负载均衡器的最初难题。Traefik的关键创新在于其能够基于容器和服务信息自动发现和配置自身。

本文强调了Traefik过去十年中的增长和影响，并列举了令人印象深刻的统计数据，例如数十亿次的Docker Hub下载量、数千颗GitHub星标和贡献者，以及数百个版本。然后，它详细介绍了Traefik通过主要版本的发展历程，包括v1（自动服务发现）、v2（路由器、中间件、TCP/UDP支持）和v3（Gateway API、OpenTelemetry）。它承认了迁移过程中向后兼容性的挑战。

展望未来，本文概述了v3.5（NGINX Ingress兼容性以简化迁移）和v3.6（多层路由、KNative集成）中即将推出的功能。文章宣布了版本4的战略转变，新功能将首先在v3.x版本中发布，并在v4最终发布时删除已弃用的功能，旨在实现更平滑的升级体验。

作者还强调了开源社区的重要作用，强调了来自非核心团队成员的大量贡献。为了庆祝周年纪念，接下来合并pull request的前50名贡献者将获得一件限量版Traefik T恤，其设计包含所有用于发布的奶酪代号。文章最后感谢了社区，并期待下一个十年让基础设施更加自动化。

---

## 37. 如果你被激光骚扰

**原文标题**: If you are harassed by lasers

**原文链接**: [https://www.laserpointersafety.com/harassment.html](https://www.laserpointersafety.com/harassment.html)

本文旨在指导如何应对激光骚扰，提供实用建议，并提醒人们注意常见的误解。文章首先建议，如果受到激光骚扰，特别是当激光瞄准头部或眼睛时，应联系当地警方。文章强调要区分真正的激光事件和误判现象，如镜头光晕、传感器溢出或昆虫。

文章随后探讨了来自未知来源的光或热的感觉，建议采用阻挡光或热的方法来确定这些感觉是否来自外部。文章建议，如果持续感到不适，应寻求医疗咨询，因为这些感觉可能源于视网膜脱落或神经误放电等医疗状况。

文章的一个重点是收集证据（照片、视频）并寻求他人确认的重要性，同时承认警方的介入往往有限。文章接着讨论了神秘的、持续不断的骚扰案例，承认人们确实感受到了这些影响，但其原因往往无法解释，且不太可能是外部设备造成的。文章强烈建议咨询医疗专家，并专注于描述症状，而不是将其归因于外部来源。

文章警告不要激化冲突，并提供了真实案例，说明了个人认为自己是目标的情况，并说明了擅自行动的潜在危险。文章还指出，截至2023年9月1日，该网站不再为涉及热激光、照片/视频中奇怪的点/线或类似的无法解释的骚扰事件提供支持。最终，文章倡导一种理性的方法，强调医学解释和向当局负责任地报告。

---

## 38. 展示HN：适用于macOS的隐私优先语音转文本

**原文标题**: Show HN: Privacy-First Voice-to-Text for macOS

**原文链接**: [https://github.com/cydanix/whisperclip](https://github.com/cydanix/whisperclip)

WhisperClip：一款注重隐私的macOS本地语音转文本及AI文本增强应用。

---

## 39. 显示 HN: 我花了四个月打造了一个人生版 Duolingo

**原文标题**: Show HN: I spent 4 months building Duolingo but for your life

**原文链接**: [https://three-cells.com](https://three-cells.com)

这款“Show HN”帖子介绍了一款旨在成为“生活版多邻国”的效率应用，它将日记、习惯追踪和任务管理结合到一个简洁的界面中。 该应用的创建者因对现有的效率应用感到沮丧，构建此应用是为了满足自己的需求并提供更有效的解决方案。 该应用专注于简洁性和日常使用，鼓励用户养成一致的习惯。

主要功能包括用于自我反思的快速两问题日记、带有可视化热图以增强动力的一键式习惯追踪，以及一个优先考虑行动而非组织结构的精简任务清单。 该应用旨在帮助用户更好地了解自己、建立积极习惯的连胜，并完成任务。

用户评价强调了该应用的极简主义、易用性以及将不同的效率工具整合到一个精简平台中的有效性。 该应用目前适用于 iPhone，并提供免费试用。 该帖子还包括指向该应用隐私政策、服务条款和联系信息的链接。

---

## 40. 坏机器：负载下的中断管理

**原文标题**: Bad Machinery: Managing Interrupts Under Load

**原文链接**: [https://log.andvari.net/pages/bad-machinery.html](https://log.andvari.net/pages/bad-machinery.html)

坏机器：高负载下管理中断

本文“坏机器：高负载下管理中断”探讨了团队（尤其是在SRE团队中）平衡项目工作和运营负载（如告警和工单等中断）的挑战。核心论点是，两者之间频繁切换会大大降低生产力并增加压力，因为“人类是坏机器”。

本文提倡时间*极化*，将特定的时间段（理想情况下是一天或一周）专门用于项目工作或中断处理。主要结论包括：

*   **避免混合项目工作和中断：** 如果您正在值班，请专注于值班职责。不要试图同时处理项目。
*   **疏导中断：** 组织值班和工单处理，将中断集中在指定的个人身上。在整个团队中随机分配工单是适得其反的。
*   **充足的人员配置：** 如果中断负载对一个人来说太高，请增加人手。不要让个人负担过重。
*   **拥抱“创造时间”：** 划出不被打扰的创造性工作时间，以培养认知流畅度和提高员工满意度。
*   **明确定义的角色：** 标准化诸如推送和标志翻转等程序，以便任何人都可以承担责任，避免长期个人所有权。

通过减少上下文切换并允许专注工作，团队可以提高生产力，减轻压力并营造更积极的工作环境。 中心主题围绕理解人类上下文切换的成本，并构建工作以最大程度地减少它。

---

## 41. 口腔微生物与胰腺癌风险增加3倍有关

**原文标题**: Oral Microbes Linked to 3-Fold Increased Risk of Pancreatic Cancer

**原文链接**: [https://nyulangone.org/news/oral-microbes-linked-increased-risk-pancreatic-cancer](https://nyulangone.org/news/oral-microbes-linked-increased-risk-pancreatic-cancer)

纽约大学朗格尼健康中心的研究发现特定口腔微生物与胰腺癌风险显著增加有关。研究人员分析了122000名个体的唾液，识别出27种细菌和真菌，这些菌群总体上使罹患胰腺癌的风险增加了3.5倍。值得注意的是，该研究发现了一种特定的念珠菌，这是一种酵母菌，存在于患者的唾液和胰腺肿瘤中。

研究团队分析了从参与者在进行的癌症预防研究中收集的唾液样本中的微生物DNA，并对他们进行了大约九年的跟踪调查。通过比较445名胰腺癌患者和无癌个体的微生物DNA，研究人员确定了影响癌症风险的特定细菌和真菌。一些被识别出的细菌已知会导致牙周病，进一步突出了口腔健康与胰腺癌之间的联系。

研究结果表明，分析口腔细菌和真菌种群可以作为一种工具，用于识别患胰腺癌风险较高的人群，从而实现更早的筛查。虽然该研究表明存在相关性，但并未建立直接的因果关系。计划进行进一步的研究，以探索口腔病毒的作用以及口腔微生物组对患者生存的影响。该研究强调了良好的口腔卫生对癌症预防的潜在保护作用。

---

## 42. 保险风险如何转化为可投资资产

**原文标题**: How insurance risk is transformed into investable assets

**原文链接**: [https://riskvest.io/riskvest-insights/transforming-insurance-risk](https://riskvest.io/riskvest-insights/transforming-insurance-risk)

本文解释了通常由保险公司承担的保险风险如何转化为可投资资产，特别是对于零售投资者而言。保险公司以部分抵押的方式运作，其持有的资本和盈余少于保单的总限额。这使得他们面临超过保费的潜在损失，需要资本储备。

由于存在无限损失的可能，零售投资者通常无法直接投资保险风险。为了克服这一点，创建了完全抵押的结构，如巨灾债券（CAT Bonds）。CAT Bonds类似于公司债券，但如果特定的灾难性事件触发了发起保险公司的保险损失，它们的本金将面临风险。

本文使用一个假设的巨灾债券“Gator Re Ltd.”来说明这个概念。Florida保险公司Risksure Re发行了一种债券，投资者的本金用于支付超过一定阈值的飓风损失。投资者因承担这种风险而获得息票，以及持有本金的无风险资产带来的收入。如果发生符合条件的损失事件，投资者可能会损失部分或全部本金。

虽然CAT Bonds提供了对具有有限责任的保险风险的敞口，但它们并非没有风险。一旦本金被触发，它将永久损失。作者最后解释了为什么保险公司没有完全抵押：这降低了资本效率和资本回报率。大量的制衡机制允许传统保险中的抵押不足，而完全抵押对于外部投资者保护其投资至关重要。

---

## 43. Suno Studio, a Generative AI DAW

**原文标题**: Suno Studio, a Generative AI DAW

**原文链接**: [https://suno.com/studio-welcome](https://suno.com/studio-welcome)

生成摘要时出错

---

## 44. Thoughts on Mechanical Keyboards and the ZSA Moonlander

**原文标题**: Thoughts on Mechanical Keyboards and the ZSA Moonlander

**原文链接**: [https://www.masteringemacs.org/article/thoughts-on-mechanical-keyboards-zsa-moonlander](https://www.masteringemacs.org/article/thoughts-on-mechanical-keyboards-zsa-moonlander)

生成摘要时出错

---

## 45. The Other Linux Logo

**原文标题**: The Other Linux Logo

**原文链接**: [https://ecogex.com/the-other-linux-logo/](https://ecogex.com/the-other-linux-logo/)

生成摘要时出错

---

## 46. Modular Manifolds

**原文标题**: Modular Manifolds

**原文链接**: [https://thinkingmachines.ai/blog/modular-manifolds/](https://thinkingmachines.ai/blog/modular-manifolds/)

生成摘要时出错

---

## 47. Britain to introduce compulsory digital ID for workers

**原文标题**: Britain to introduce compulsory digital ID for workers

**原文链接**: [https://www.reuters.com/world/uk/britain-introduce-mandatory-digital-id-cards-2025-09-26/](https://www.reuters.com/world/uk/britain-introduce-mandatory-digital-id-cards-2025-09-26/)

生成摘要时出错

---

## 48. Why use mailing lists?

**原文标题**: Why use mailing lists?

**原文链接**: [https://mailarchive.ietf.org/arch/msg/ietf/q6A_anL1u-Y9iXe-vboiOYamsl0/](https://mailarchive.ietf.org/arch/msg/ietf/q6A_anL1u-Y9iXe-vboiOYamsl0/)

生成摘要时出错

---

## 49. Why do we remember some life moments but not others?

**原文标题**: Why do we remember some life moments but not others?

**原文链接**: [https://www.bu.edu/articles/2025/why-do-we-remember-some-moments-but-not-others/](https://www.bu.edu/articles/2025/why-do-we-remember-some-moments-but-not-others/)

生成摘要时出错

---

## 50. How This Retro Cafeteria Became a Launchpad for Buffalo’s Food Entrepreneurs

**原文标题**: How This Retro Cafeteria Became a Launchpad for Buffalo’s Food Entrepreneurs

**原文链接**: [https://www.thefoodcorridor.com/blog/how-this-retro-cafeteria-became-a-launchpad-for-buffalos-food-entrepreneurs/](https://www.thefoodcorridor.com/blog/how-this-retro-cafeteria-became-a-launchpad-for-buffalos-food-entrepreneurs/)

生成摘要时出错

---

## 51. Ultra efficient vector extension for SQLite

**原文标题**: Ultra efficient vector extension for SQLite

**原文链接**: [https://marcobambini.substack.com/p/the-state-of-vector-search-in-sqlite](https://marcobambini.substack.com/p/the-state-of-vector-search-in-sqlite)

生成摘要时出错

---

## 52. "Whispering Death" – The Most Dangerous Motorcycle Ever Sold [video]

**原文标题**: "Whispering Death" – The Most Dangerous Motorcycle Ever Sold [video]

**原文链接**: [https://www.youtube.com/watch?v=N1y_ZzGSD0k](https://www.youtube.com/watch?v=N1y_ZzGSD0k)

生成摘要时出错

---

## 53. Requiem for a Hash Function, or: How I learned to love package maphash

**原文标题**: Requiem for a Hash Function, or: How I learned to love package maphash

**原文链接**: [https://matttproud.com/blog/posts/go-maphash.html](https://matttproud.com/blog/posts/go-maphash.html)

生成摘要时出错

---

## 54. Evolving the Multi-User Spaceport

**原文标题**: Evolving the Multi-User Spaceport

**原文链接**: [https://www.spacex.com/updates#multiuser-spaceport](https://www.spacex.com/updates#multiuser-spaceport)

生成摘要时出错

---

## 55. The Amazon Kindle War Against Piracy

**原文标题**: The Amazon Kindle War Against Piracy

**原文链接**: [https://goodereader.com/blog/kindle/the-amazon-kindle-war-against-piracy](https://goodereader.com/blog/kindle/the-amazon-kindle-war-against-piracy)

生成摘要时出错

---

## 56. Litex: The First Formal Language Learnable in 1-2 Hours

**原文标题**: Litex: The First Formal Language Learnable in 1-2 Hours

**原文链接**: [https://github.com/litexlang/golitex](https://github.com/litexlang/golitex)

生成摘要时出错

---

## 57. Americans traveling to Europe will have fingerprints scanned under new rule

**原文标题**: Americans traveling to Europe will have fingerprints scanned under new rule

**原文链接**: [https://www.livenowfox.com/news/americans-traveling-europe-fingerprints-scanned](https://www.livenowfox.com/news/americans-traveling-europe-fingerprints-scanned)

生成摘要时出错

---

## 58. DeepFabric – Generate high-quality synthetic datasets at scale

**原文标题**: DeepFabric – Generate high-quality synthetic datasets at scale

**原文链接**: [https://lukehinds.github.io/deepfabric/](https://lukehinds.github.io/deepfabric/)

生成摘要时出错

---

## 59. PSA: Declare an incident if someone on your team installed the postmark-MCP

**原文标题**: PSA: Declare an incident if someone on your team installed the postmark-MCP

**原文链接**: [https://twitter.com/jessethanley/status/1971909570378584443](https://twitter.com/jessethanley/status/1971909570378584443)

生成摘要时出错

---

## 60. Pop OS 24.04 LTS Beta

**原文标题**: Pop OS 24.04 LTS Beta

**原文链接**: [https://system76.com/pop/pop-beta/](https://system76.com/pop/pop-beta/)

生成摘要时出错

---

## 61. Fast UDP I/O for Firefox in Rust

**原文标题**: Fast UDP I/O for Firefox in Rust

**原文链接**: [https://max-inden.de/post/fast-udp-io-in-firefox/](https://max-inden.de/post/fast-udp-io-in-firefox/)

生成摘要时出错

---

## 62. Titanic's sister, Britannic, sank in 1916. Divers have recovered artifacts

**原文标题**: Titanic's sister, Britannic, sank in 1916. Divers have recovered artifacts

**原文链接**: [https://www.smithsonianmag.com/smart-news/the-titanics-sister-ship-the-britannic-sank-in-1916-for-the-first-time-ever-divers-have-recovered-artifacts-from-its-wreck-180987402/](https://www.smithsonianmag.com/smart-news/the-titanics-sister-ship-the-britannic-sank-in-1916-for-the-first-time-ever-divers-have-recovered-artifacts-from-its-wreck-180987402/)

生成摘要时出错

---

## 63. How to stop AI's "lethal trifecta"

**原文标题**: How to stop AI's "lethal trifecta"

**原文链接**: [https://www.economist.com/leaders/2025/09/25/how-to-stop-ais-lethal-trifecta](https://www.economist.com/leaders/2025/09/25/how-to-stop-ais-lethal-trifecta)

生成摘要时出错

---

## 64. A platform-jumping prince – History of Prince of Persia's 1990s Ports

**原文标题**: A platform-jumping prince – History of Prince of Persia's 1990s Ports

**原文链接**: [https://www.jordanmechner.com/en/latest-news/#a-platform-jumping-prince](https://www.jordanmechner.com/en/latest-news/#a-platform-jumping-prince)

生成摘要时出错

---

## 65. Genode OS Framework

**原文标题**: Genode OS Framework

**原文链接**: [https://genode.org](https://genode.org)

生成摘要时出错

---

## 66. RNA structure prediction is hard. How much does that matter?

**原文标题**: RNA structure prediction is hard. How much does that matter?

**原文链接**: [https://www.owlposting.com/p/rna-structure-prediction-is-hard](https://www.owlposting.com/p/rna-structure-prediction-is-hard)

生成摘要时出错

---

## 67. Bach Cello Suites (2024)

**原文标题**: Bach Cello Suites (2024)

**原文链接**: [https://bachcellosuites.co.uk/](https://bachcellosuites.co.uk/)

生成摘要时出错

---

## 68. How to make sense of any mess

**原文标题**: How to make sense of any mess

**原文链接**: [https://www.howtomakesenseofanymess.com](https://www.howtomakesenseofanymess.com)

生成摘要时出错

---

## 69. The largest-ever simulation of the universe has just been released

**原文标题**: The largest-ever simulation of the universe has just been released

**原文链接**: [https://www.space.com/astronomy/the-largest-ever-simulation-of-the-universe-has-just-been-released](https://www.space.com/astronomy/the-largest-ever-simulation-of-the-universe-has-just-been-released)

生成摘要时出错

---

## 70. Redis is fast – I'll cache in Postgres

**原文标题**: Redis is fast – I'll cache in Postgres

**原文链接**: [https://dizzy.zone/2025/09/24/Redis-is-fast-Ill-cache-in-Postgres/](https://dizzy.zone/2025/09/24/Redis-is-fast-Ill-cache-in-Postgres/)

生成摘要时出错

---

## 71. Clean hydrogen at a crossroads: Why methane pyrolysis deserves attention

**原文标题**: Clean hydrogen at a crossroads: Why methane pyrolysis deserves attention

**原文链接**: [https://www.c2es.org/2025/09/clean-hydrogen-at-a-crossroads-why-methane-pyrolysis-deserves-attention/](https://www.c2es.org/2025/09/clean-hydrogen-at-a-crossroads-why-methane-pyrolysis-deserves-attention/)

生成摘要时出错

---

## 72. Show HN: Family Chess: Play across firewalls and Internet cultures

**原文标题**: Show HN: Family Chess: Play across firewalls and Internet cultures

**原文链接**: [https://github.com/kelvinq/family-chess](https://github.com/kelvinq/family-chess)

生成摘要时出错

---

## 73. Elephantshark, a tool to monitor Postgres network traffic

**原文标题**: Elephantshark, a tool to monitor Postgres network traffic

**原文链接**: [https://neon.com/blog/elephantshark-monitor-postgres-network-traffic](https://neon.com/blog/elephantshark-monitor-postgres-network-traffic)

生成摘要时出错

---

## 74. Do YC after you graduate: Early decision for students

**原文标题**: Do YC after you graduate: Early decision for students

**原文链接**: [https://www.ycombinator.com/early-decision](https://www.ycombinator.com/early-decision)

生成摘要时出错

---

## 75. Property-Based Testing of OCaml 5's Runtime System [pdf]

**原文标题**: Property-Based Testing of OCaml 5's Runtime System [pdf]

**原文链接**: [https://janmidtgaard.dk/papers/Midtgaard%3AOLIVIERFEST25.pdf](https://janmidtgaard.dk/papers/Midtgaard%3AOLIVIERFEST25.pdf)

生成摘要时出错

---

## 76. When Bruce Lee trained with Kareem Abdul-Jabbar

**原文标题**: When Bruce Lee trained with Kareem Abdul-Jabbar

**原文链接**: [https://lithub.com/when-bruce-lee-trained-with-kareem-abdul-jabbar/](https://lithub.com/when-bruce-lee-trained-with-kareem-abdul-jabbar/)

生成摘要时出错

---

## 77. Investigating a Forged PDF

**原文标题**: Investigating a Forged PDF

**原文链接**: [https://mjg59.dreamwidth.org/73317.html](https://mjg59.dreamwidth.org/73317.html)

生成摘要时出错

---

## 78. RedoxFS is the default filesystem of Redox OS, inspired by ZFS

**原文标题**: RedoxFS is the default filesystem of Redox OS, inspired by ZFS

**原文链接**: [https://doc.redox-os.org/book/redoxfs.html](https://doc.redox-os.org/book/redoxfs.html)

生成摘要时出错

---

## 79. The Best Way to Use AI for Learning

**原文标题**: The Best Way to Use AI for Learning

**原文链接**: [https://medium.com/heptabase/the-best-way-to-use-ai-for-learning-762c3467bdf1](https://medium.com/heptabase/the-best-way-to-use-ai-for-learning-762c3467bdf1)

生成摘要时出错

---

## 80. Show HN: Dreamtap – Make your AI more creative

**原文标题**: Show HN: Dreamtap – Make your AI more creative

**原文链接**: [https://dreamtap.xyz/](https://dreamtap.xyz/)

生成摘要时出错

---

## 81. Understanding RL for model training, and future directions with GRAPE

**原文标题**: Understanding RL for model training, and future directions with GRAPE

**原文链接**: [https://arxiv.org/abs/2509.04501](https://arxiv.org/abs/2509.04501)

生成摘要时出错

---

## 82. Amiga SPICE is a program for simulating electronic circuits

**原文标题**: Amiga SPICE is a program for simulating electronic circuits

**原文链接**: [https://www.edsa.uk/blog/amiga-spice](https://www.edsa.uk/blog/amiga-spice)

生成摘要时出错

---

## 83. The Little Book of Linear Algebra

**原文标题**: The Little Book of Linear Algebra

**原文链接**: [https://little-book-of.github.io/linear-algebra/](https://little-book-of.github.io/linear-algebra/)

生成摘要时出错

---

## 84. A history of ARM, part 1: Building the first chip (2022)

**原文标题**: A history of ARM, part 1: Building the first chip (2022)

**原文链接**: [https://arstechnica.com/gadgets/2022/09/a-history-of-arm-part-1-building-the-first-chip/](https://arstechnica.com/gadgets/2022/09/a-history-of-arm-part-1-building-the-first-chip/)

生成摘要时出错

---

## 85. Gurted – A web ecosystem introducing the gurt:// protocol

**原文标题**: Gurted – A web ecosystem introducing the gurt:// protocol

**原文链接**: [https://gurted.com/](https://gurted.com/)

生成摘要时出错

---

## 86. Perplexing diamonds from South Africa mine contain 'almost impossible' chemistry

**原文标题**: Perplexing diamonds from South Africa mine contain 'almost impossible' chemistry

**原文链接**: [https://www.scientificamerican.com/article/almost-impossible-deep-earth-diamonds-confirm-how-these-gems-form/](https://www.scientificamerican.com/article/almost-impossible-deep-earth-diamonds-confirm-how-these-gems-form/)

生成摘要时出错

---

## 87. Evanston orders Flock to remove reinstalled cameras

**原文标题**: Evanston orders Flock to remove reinstalled cameras

**原文链接**: [https://evanstonroundtable.com/2025/09/24/flock-safety-reinstalls-evanston-cameras/](https://evanstonroundtable.com/2025/09/24/flock-safety-reinstalls-evanston-cameras/)

生成摘要时出错

---

## 88. Can a model trained on satellite data really find brambles on the ground?

**原文标题**: Can a model trained on satellite data really find brambles on the ground?

**原文链接**: [https://toao.com/blog/can-we-really-see-brambles-from-space](https://toao.com/blog/can-we-really-see-brambles-from-space)

生成摘要时出错

---

## 89. Improved Gemini 2.5 Flash and Flash-Lite

**原文标题**: Improved Gemini 2.5 Flash and Flash-Lite

**原文链接**: [https://developers.googleblog.com/en/continuing-to-bring-you-our-latest-models-with-an-improved-gemini-2-5-flash-and-flash-lite-release/](https://developers.googleblog.com/en/continuing-to-bring-you-our-latest-models-with-an-improved-gemini-2-5-flash-and-flash-lite-release/)

生成摘要时出错

---

## 90. Context is the bottleneck for coding agents now

**原文标题**: Context is the bottleneck for coding agents now

**原文链接**: [https://runnercode.com/blog/context-is-the-bottleneck-for-coding-agents-now](https://runnercode.com/blog/context-is-the-bottleneck-for-coding-agents-now)

生成摘要时出错

---

## 91. Bit is all we need: binary normalized neural networks

**原文标题**: Bit is all we need: binary normalized neural networks

**原文链接**: [https://arxiv.org/abs/2509.07025](https://arxiv.org/abs/2509.07025)

生成摘要时出错

---

## 92. Exploit allows for takeover of fleets of Unitree robots

**原文标题**: Exploit allows for takeover of fleets of Unitree robots

**原文链接**: [https://spectrum.ieee.org/unitree-robot-exploit](https://spectrum.ieee.org/unitree-robot-exploit)

生成摘要时出错

---

## 93. No reachable chess position with more than 218 moves

**原文标题**: No reachable chess position with more than 218 moves

**原文链接**: [https://lichess.org/@/Tobs40/blog/there-is-no-reachable-chess-position-with-more-than-218-moves/a5xdxeqs](https://lichess.org/@/Tobs40/blog/there-is-no-reachable-chess-position-with-more-than-218-moves/a5xdxeqs)

生成摘要时出错

---

## 94. Pairing with Claude Code to rebuild my startup's website

**原文标题**: Pairing with Claude Code to rebuild my startup's website

**原文链接**: [https://blog.nseldeib.com/p/pairing-with-claude-code-to-rebuild](https://blog.nseldeib.com/p/pairing-with-claude-code-to-rebuild)

生成摘要时出错

---

## 95. The Theatre of Pull Requests and Code Review

**原文标题**: The Theatre of Pull Requests and Code Review

**原文链接**: [https://meks.quest/blogs/the-theatre-of-pull-requests-and-code-review](https://meks.quest/blogs/the-theatre-of-pull-requests-and-code-review)

生成摘要时出错

---

## 96. ChatGPT Pulse

**原文标题**: ChatGPT Pulse

**原文链接**: [https://openai.com/index/introducing-chatgpt-pulse/](https://openai.com/index/introducing-chatgpt-pulse/)

生成摘要时出错

---

## 97. A recent chess controversy

**原文标题**: A recent chess controversy

**原文链接**: [https://www.chicagobooth.edu/review/did-us-chess-champion-cheat](https://www.chicagobooth.edu/review/did-us-chess-champion-cheat)

生成摘要时出错

---

## 98. The Wind, a Pole, and the Dragon

**原文标题**: The Wind, a Pole, and the Dragon

**原文链接**: [https://entropicthoughts.com/the-wind-a-pole-and-the-dragon](https://entropicthoughts.com/the-wind-a-pole-and-the-dragon)

生成摘要时出错

---

## 99. LuaJIT Language Toolkit

**原文标题**: LuaJIT Language Toolkit

**原文链接**: [https://github.com/franko/luajit-lang-toolkit](https://github.com/franko/luajit-lang-toolkit)

生成摘要时出错

---

## 100. Wild performance tricks

**原文标题**: Wild performance tricks

**原文链接**: [https://davidlattimore.github.io/posts/2025/09/02/rustforge-wild-performance-tricks.html](https://davidlattimore.github.io/posts/2025/09/02/rustforge-wild-performance-tricks.html)

生成摘要时出错

---

