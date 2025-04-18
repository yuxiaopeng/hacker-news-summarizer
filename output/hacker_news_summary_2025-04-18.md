# Hacker News 热门文章摘要 (2025-04-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 展示HN: 我做了一个能塞进二维码里的类Doom游戏

**原文标题**: Show HN: I made a Doom-like game fit inside a QR code

**原文链接**: [https://github.com/Kuberwastaken/backdooms](https://github.com/Kuberwastaken/backdooms)

这个“Show HN”帖子展示了“The Backdooms”，这是一款受《DOOM》和《The Backrooms》启发、完全可玩且经过压缩的游戏，完全包含在一个二维码中。该项目演示了一种创新的方法，可以在二维码中直接离线托管轻量级 Web 应用程序。用户可以使用现代 Web 浏览器扫描二维码，即可立即玩游戏，无需下载或安装任何内容。

该项目的核心在于其极端的压缩技术，利用 Zlib 压缩与 Gzip 解压缩流以及 base64 编码来最大限度地缩小游戏的大小。HTML 代码是自解压的，利用浏览器的 DecompressionStream API 来动态解压缩和执行游戏。

该帖子概述了使用 Python 和 `qrcode` 库将游戏转换为二维码的过程，重点介绍了该系统生成尽可能小的二维码，同时最大化数据容量的逻辑。作者还提供了压缩工作流程和二维码生成过程的技术分解，讨论了遇到的挑战和限制。该项目以 MIT 许可证发布，鼓励其他人尝试基于二维码的游戏。鸣谢 id Software（《DOOM》），matttkc（灵感来源）和 Toby Fox（《Undertale》音乐）。

---

## 2. 用于Python的全新ASN.1 API

**原文标题**: A New ASN.1 API for Python

**原文链接**: [https://blog.trailofbits.com/2025/04/18/sneak-peek-a-new-asn.1-api-for-python/](https://blog.trailofbits.com/2025/04/18/sneak-peek-a-new-asn.1-api-for-python/)

本文宣布PyCA Cryptography正在开发一个新的Python ASN.1 API，旨在解决现有Python ASN.1库在性能、差异化简和现代化方面面临的挑战。ASN.1对于密码学、网络和电信（例如，TLS握手、LDAP、X.509证书）至关重要，但由于实现不一致以及在纯Python中实现时的性能问题，历史上一直是漏洞的来源。

新的API旨在利用PyCA Cryptography已采用的基于Rust的ASN.1解析器，提供接近原生解析的性能，从而减少解析器差异。它将具有现代的、声明性的dataclasses风格接口，带有类型提示，从而提高可用性以及与类型检查器的集成。

提供的示例说明了如何将复杂的ASN.1定义映射到清晰的、带有类型提示的Python dataclass。作者强调了该库在Sigstore生态系统等环境中的相关性，在这些环境中，开发人员需要处理超出标准X.509形状的ASN.1编码/解码。该项目由Alpha-Omega资助，代表了PyCA Cryptography致力于改善Python安全生态系统的承诺。未来的计划包括支持核心ASN.1装饰器、基本类型和修饰符，将新的API集成到PyCA Cryptography中，并在主要版本中发布。

---

## 3. Show HN: Attune - 在几秒内构建并发布APT仓库

**原文标题**: Show HN: Attune - Build and publish APT repositories in seconds

**原文链接**: [https://github.com/attunehq/attune](https://github.com/attunehq/attune)

Attune：安全构建、发布和托管Linux软件包的工具 (初始专注于APT仓库 - Debian/Ubuntu)。它提供自托管和托管云部署选项。其关键特性是安全性；仓库索引签名发生在本地，允许用户保持对其签名密钥的控制。Attune也专为速度而设计，利用增量仓库索引重建来实现快速的软件包管理。

"Show HN"提供了一个快速入门指南，大约在5分钟内使用Attune设置一个APT仓库。该过程包括：

1. 使用Docker Compose设置Attune后端，从GitHub克隆仓库，配置环境变量，并启动服务。
2. 安装Attune CLI并创建一个仓库。
3. 将一个`.deb`软件包添加到仓库。
4. 生成一个GPG密钥（如果需要），导出密钥，并使用它来签名和部署仓库。

文章重点介绍了每个步骤的命令，包括克隆仓库、创建仓库、添加软件包、生成GPG密钥以及签名/部署仓库。它强调了修改环境变量以适应用户部署的重要性。

文章最后引导用户查阅用户指南，以获取更详细的说明和配置选项，并声明Attune采用Apache 2许可。

---

## 4. 没那么慢的C++

**原文标题**: Less Slow C++

**原文链接**: [https://github.com/ashvardanian/less_slow.cpp](https://github.com/ashvardanian/less_slow.cpp)

该仓库“Less Slow C++”提供了编写高效C和C++代码的实用示例，并利用了C++20的特性。它解决了现代代码中常见的、常被大学和训练营课程忽视的性能陷阱。内容涵盖了微内核、并行算法、协程和多态。

主要亮点包括优化的随机输入生成、更快的三角函数计算、改进的惰性逻辑、高级编译器优化以及对矩阵乘法性能的深入见解。它探讨了AI的扩展、分支预测、递归深度、异常处理、使用OpenMP/oneTBB的多核扩展、无需内存分配的JSON处理、STL关联容器、consteval RegEx引擎、指针标记、UDP丢包、使用io_uring的Web请求服务、分散/聚集操作和GPU加速。

该项目主要在Linux上使用GCC和Clang进行测试，但也与其他编译器兼容。该仓库包含手写汇编和CUDA/PTX代码，用于硬件特定的优化。该项目使用多个第三方依赖项，包括Google Benchmark、Intel的oneTBB、Meta的libunifex等。可以使用标志自定义基准测试，以设置输出格式、过滤和启用随机交错。该仓库还提供了使用Google Benchmark功能的技巧和窍门。

---

## 5. 游艇的工作原理：帆船物理学与设计

**原文标题**: How a yacht works: sailboat physics and design

**原文链接**: [https://www.onemetre.net/Design/Design.htm](https://www.onemetre.net/Design/Design.htm)

莱斯特·吉尔伯特的《游艇工作原理：帆船物理学与设计》一文深入探讨了帆船航行背后的复杂科学。它涵盖了广泛的主题，从基本空气动力学原理到游艇的具体设计元素。

文章首先探讨了翼型及其如何产生升力，讨论了各种理论模型并结合了二维流体模拟。然后，文章转向鳍和船帆设计的细节，分析了展弦比、涡流、边界层、雷诺数、缭绳、扭曲和狭缝的影响。文章还展示了缭绳角度和边界层的风洞测试结果。

文章的核心内容是研究游艇在各种航行条件下的工作原理，涵盖航行方位、顺风性能、逆风航行、升力和阻力的影响，以及视风的关键概念。文章进一步分析了风梯度及其对船帆扭曲的影响，并介绍了大型船只上使用的仪器。

文章还全面讨论了附体设计，包括鳍和舵的大小、平面形状、剖面和球鼻艏形状，并专门用一个章节介绍了马克的球鼻艏计算器。文章涉及船体设计，考虑了弗劳德数、表面摩擦力、波浪阻力、船体线型和稳心矩等因素。分析了船体周围的流动，并介绍了扰流器等概念。

文章对船帆和索具设计给予了相当大的关注，涵盖了舷索、跳索、支索、撑杆、桅杆与船帆的相互作用、前支索下垂、风阻、鹅颈几何形状、吊帆索、船帆弧度和船帆形状。文章还考虑了前帆下缘与甲板之间以及船帆与桅杆之间的间隙的影响。

最后，文章通过讨论作为一个整体的游艇，整合了所有这些元素，重点关注平衡、稳定性、环境因素、设计权衡以及船级规则的影响。文章深入研究了由于船体形状、索具调整、压浪舵造成的平衡，并利用了简单的速度预测程序 (VPP)。

---

## 6. Defold: 跨平台游戏引擎

**原文标题**: Defold: cross-platform game engine

**原文链接**: [https://defold.com](https://defold.com)

Defold是一款免费且可用于商业用途的跨平台游戏引擎，专为创建高性能的2D和3D游戏而设计。它是一个完整的解决方案，包含可视化编辑器、代码编辑器、Lua脚本支持、调试器以及场景/粒子/瓦片地图编辑器，所有功能集成于一个工具中。Defold支持发布到众多平台，包括PlayStation、Nintendo Switch、Android、iOS、macOS、Linux、Windows、Steam、HTML5和Facebook。Xbox支持计划于2024年第三季度推出。

该引擎旨在开箱即用，无需初始设置，并为原生代码提供零配置的云构建。开发者可以通过自定义配置、资源门户或编写自己的原生代码来扩展引擎的功能。它与Atom、VS Code、Rive、Spine、TexturePacker和Tiled等常用工具集成。

感谢Defold基金会，Defold采用永久免费模式，没有预付、许可或运行时费用。该引擎拥有成功的游戏发布记录，集成了分析和应用经济服务，并每月更新。同时提供技术支持合同。网站提供教程、手册、API参考、示例和一个社区论坛，以帮助开发者学习和解决问题。网站还展示了使用Defold制作的游戏，如《Family Island》，并提供关于引擎开发的博客更新和新闻。

---

## 7. Dot (YC S21) 正在招聘一名销售工程师，以实现分析自动化（完全远程）。

**原文标题**: Dot (YC S21) is hiring a sales engineer to automate analytics (fully remote)

**原文链接**: [https://www.ycombinator.com/companies/dot/jobs/XSmklFa-customer-success-sales-engineer-remote](https://www.ycombinator.com/companies/dot/jobs/XSmklFa-customer-success-sales-engineer-remote)

Dot（YC S21）是一家AI数据分析初创公司，致力于帮助企业实现数据访问民主化，现招聘一名全职远程客户成功/销售工程师。 该混合型职位负责整个客户旅程，从入职和支持到售前技术评估。理想的候选人将弥合产品与用户之间的差距，与创始人及工程团队紧密合作，以最大化客户价值。

职责包括帮助客户完成数据仓库集成，通过最佳实践和故障排除来推动产品采用，提供售前技术支持，担任主题专家，并将客户反馈传达给产品和工程团队。该职位还涉及构建可扩展的资源，如文档和教程，并为成功的产品使用提供收入分成。

Dot正在寻找具有分析或数据平台背景、强大的技术问题解决能力、以客户为中心的沟通能力、主人翁意识和主动性，以及具有销售头脑并热衷于数据民主化的人才。 拥有数据仓库、BI工具、SQL、Python、Snowflake、BigQuery或dbt经验者优先。

公司重视包容性和多样性。面试流程包括初步沟通、深入面试、与团队见面以及实践性付费练习。 请候选人发送一封简短的电子邮件，说明其动机、个人资料链接以及所在位置信息。

---

## 8. 双子座 2.5 闪电版

**原文标题**: Gemini 2.5 Flash

**原文链接**: [https://developers.googleblog.com/en/start-building-with-gemini-25-flash/](https://developers.googleblog.com/en/start-building-with-gemini-25-flash/)

谷歌开发者博客宣布通过Google AI Studio和Vertex AI中的Gemini API发布Gemini 2.5 Flash的预览版。基于Gemini 2.0 Flash的基础之上，这个新版本在保持速度和成本效益的同时，显著提升了推理能力。

Gemini 2.5 Flash的一个关键特性是其完全混合的推理模型，允许开发者开启或关闭“思考”功能，并设置“思考预算”以平衡质量、成本和延迟。这种控制为各种用例提供了灵活性。较高的思考预算使模型能够进行更彻底的推理，从而提高复杂任务的准确性。即使将思考预算设置为零，该模型也能提供优于2.0 Flash的性能。

Gemini 2.5 Flash定位为一种具有卓越性价比的经济高效的思考模型。开发者可以调整API中的`thinking_budget`参数（范围从0到24576个token）来控制推理的程度。该模型会根据提示的复杂性智能地确定必要的思考量。

此次发布包括API参考、思考指南和Gemini Cookbook中的代码示例。谷歌计划在Gemini 2.5 Flash全面上市之前进行进一步的改进。

---

## 9. AMP以及为何电子邮件不是（且永远不应该）交互式的

**原文标题**: AMP and why emails are not (and should never be) interactive

**原文链接**: [https://buttondown.com/blog/whatever-happened-to-amp-email](https://buttondown.com/blog/whatever-happened-to-amp-email)

本文探讨了谷歌试图通过AMP（加速移动页面）为电子邮件引入互动性，以及它最终失败的原因。作者认为，电子邮件的优势在于其简单性、可靠性和去中心化，因此多年来抵制了重大改变。

谷歌的AMP for email旨在允许用户直接从收件箱执行预订航班、回复评论和更新偏好等操作。然而，该计划面临阻力，原因包括开发电子邮件的复杂性增加（需要AMP、HTML和纯文本版本），电子邮件客户端的支持有限，以及对谷歌控制网络的怀疑。

本文强调了它与最初针对移动网站的AMP项目相似之处，当时谷歌通过优惠的搜索排名来激励采用，导致了反垄断担忧。作者强调，电子邮件固有的永久性和提供可靠记录的能力是至关重要的方面，而AMP通过使电子邮件动态化并可能被更改，威胁到了这些方面。

最终，谷歌放弃了AMP徽章和对Google News的要求，虽然他们仍然在内部使用AMP来实现评论Google Docs等功能，但该项目本身已被很大程度上忽视。文章总结道，电子邮件应保持为静态、可靠的媒介，强调保持其简单性和永久性的重要性。

---

## 10. 大学城：瑞安·艾伦谈昔日都市主义

**原文标题**: College Towns: Urbanism from a Past Era with Ryan Allen

**原文链接**: [https://www.governance.fyi/p/college-towns-urbanism-from-a-past](https://www.governance.fyi/p/college-towns-urbanism-from-a-past)

本文采访了瑞安·艾伦，他是“大学城”通讯的教授和作者，探讨了高等教育与都市主义的交叉点。艾伦强调了高等教育面临的挑战，特别是博士过剩导致毕业生就业不稳定，并以一位无家可归的加州大学洛杉矶分校教授的故事为例。他建议，鉴于学术就业市场日渐萎缩，在没有明确职业道路的情况下不要攻读博士学位。

随后，对话转向大学在保护宜步行的城市环境中所扮演的角色，并将其与美国其他地方普遍存在的郊区蔓延现象形成对比。艾伦指出，迪士尼乐园向游客收取体验宜步行的“大街”的费用，而这些大街曾经在美国城镇中司空见惯，这是一种讽刺。

访谈还涉及美国与中国高等教育格局的演变。艾伦指出，中国大学的竞争力日益增强，他们正在培养自己的专家，并减少对美国机构的依赖。他强调，尽管美国的 STEM 领域仍然具有价值，但美国目前的政策决策正在伤害自己，尤其是在吸引和留住国际学生方面。他承认，与人文科学或社会科学相比，STEM 领域通常对寻求就业的毕业生更有用。

---

## 11. 展示HN: 具备远程编程和自然语言数据分析的LTE连接物联网模块

**原文标题**: Show HN: LTE-connected IoT module with remote programming and NL data analysis

**原文链接**: [https://www.youtube.com/watch?v=3L_OU-fMW_w](https://www.youtube.com/watch?v=3L_OU-fMW_w)

这个“Show HN”帖子介绍了一种LTE连接的物联网模块，该模块支持远程编程，并包含NL（可能是自然语言）数据分析功能。 然而，所提供的内容与标题完全无关，似乎是YouTube页脚中关于法律条款、版权、广告和隐私的一段信息。

本质上，仅根据标题判断，该帖子展示的是一款产品：一个利用LTE连接进行远程访问，并可能提供从应用于其收集数据的自然语言处理中获得的洞察的物联网模块。 在没有更多信息的情况下，无法详细说明该模块的细节、目标应用或所提供的NL数据分析的性质。 实际帖子的内容似乎缺失或损坏。

---

## 12. 邮寄土豆

**原文标题**: Potatoes in the Mail

**原文链接**: [https://facts.usps.com/mailing-potatoes/](https://facts.usps.com/mailing-potatoes/)

关于美国邮政可以邮寄马铃薯的趣闻

---

## 13. 语言的成长[pdf] (1998)

**原文标题**: Growing a Language [pdf] (1998)

**原文链接**: [https://langev.com/pdf/steele99growing.pdf](https://langev.com/pdf/steele99growing.pdf)

由于该文档是PDF格式，我无法为您提供摘要文本。

---

## 14. Unikernel Linux (UKL) (2023年)

**原文标题**: Unikernel Linux (UKL) (2023)

**原文链接**: [https://dl.acm.org/doi/10.1145/3552326.3587458](https://dl.acm.org/doi/10.1145/3552326.3587458)

无法访问文章链接。

---

## 15. DeepSeek分布式文件系统入门

**原文标题**: An intro to DeepSeek's distributed file system

**原文链接**: [https://maknee.github.io/blog/2025/3FS-Performance-Journal-1/](https://maknee.github.io/blog/2025/3FS-Performance-Journal-1/)

本文介绍了 DeepSeek 开源的分布式文件系统 3FS (萤火文件系统)，阐述了其目的、优势、架构以及计划进行的性能分析。

像 3FS 这样的分布式文件系统提供了一种抽象，允许应用程序像与本地文件系统交互一样与分布在多台机器上的数据进行交互。这带来了诸如海量存储容量、高吞吐量、容错性和数据冗余等好处。

3FS 由四个核心组件组成：

*   **Mgmtd:** 通过注册和心跳管理集群配置和节点发现。
*   **Meta:** 处理文件元数据，包括位置、属性以及诸如打开、创建和 stat 等操作，并将信息存储在 FoundationDB 中。
*   **Storage:** 管理物理数据存储，通过将数据分解为块，使用 Rust ChunkEngine 跟踪元数据（元数据存储在 LevelDB 中），并利用 worker 进行块分配、回收和读取请求。
*   **Client:** 与其他节点通信以与文件系统交互。

该系统采用 CRAQ (带分配查询的链式复制) 来确保强一致性和容错性。CRAQ 将写入传播到一系列节点，将条目标记为 "dirty"，直到在尾部提交，然后标记为 "clean"。

文章最后强调了对 3FS 进行进一步性能分析的必要性，质疑 DeepSeek 的性能声明，并旨在识别瓶颈、理想工作负载以及与其他分布式文件系统的比较。该博客系列的其余部分将致力于此性能探索。

---

## 16. 我分析了68万首歌曲中的和弦进行。

**原文标题**: I analyzed chord progressions in 680k songs

**原文链接**: [https://www.cantgetmuchhigher.com/p/i-analyzed-chord-progressions-in](https://www.cantgetmuchhigher.com/p/i-analyzed-chord-progressions-in)

克里斯·达拉·里瓦分析了来自“和弦圣经”数据集的68万首歌曲的和弦进行，揭示了音乐创作中一些有趣的趋势。他发现G大调和C大调是最常见的和弦，但和弦的使用因流派而异。乡村音乐大量依赖简单的大调和弦，而爵士乐则更多地使用像七和弦这样更复杂的和弦。

该分析还考察了和弦使用随时间的变化，揭示了七和弦的流行度下降，这与爵士乐的衰落有关。他通过计算“独特和弦率”（独特和弦/总和弦）来探讨当代音乐变得不那么复杂的观点。分析表明，这一比率已从20世纪30年代的13%降至2010年代的8%，表明现代歌曲在和弦方面更加重复。虽然承认和弦进行只是歌曲的一个要素，但作者认为，从和弦的角度来看，现代音乐变得更加冗余。

文章最后推荐了两首歌曲：For Nina乐队(2025年)的《Hounds》和Big Audio Dynamite乐队(1985年)的《The Bottom Line》，并附注了关于付费订阅时事通讯的信息。

---

## 17. 最著名的二氧化碳吸收剂

**原文标题**: The most famous carbon dioxide absorber

**原文链接**: [https://www.howequipmentworks.com/apollo_13/](https://www.howequipmentworks.com/apollo_13/)

阿波罗13号任务详情：氧气罐爆炸后的生死危机。 原定为第三次登月任务，却因服务舱氧气罐爆炸受损而偏离航向，危及宇航员的氧气、水和电力供应。

被迫转移到登月舱的宇航员面临新的挑战，包括电池电量有限和水资源日益减少。 地球上的工程师努力减少电力消耗并节约资源。 然而，由于登月舱二氧化碳吸收器的容量有限，舱内二氧化碳水平迅速上升，一个关键问题随之而来。

登月舱使用圆形氢氧化锂吸收器容器，而指令舱使用方形容器。 现在有三名宇航员依赖登月舱，其吸收器供应不足以维持剩余四天的旅程。 故事戛然而止，突显了解决该问题以防止潜在致命的二氧化碳中毒的迫切需要。 文章为宇航员和地面控制人员如何利用有限的材料共同克服这一看似无法克服的障碍的戏剧性故事奠定了基础。

---

## 18. 呼吸练习期间二氧化碳降低：意识状态改变的出现

**原文标题**: Decreased CO2 during breathwork: emergence of altered states of consciousness

**原文链接**: [https://www.nature.com/articles/s44271-025-00247-0](https://www.nature.com/articles/s44271-025-00247-0)

本研究调查了循环呼吸作为一种非药物替代疗法，用于替代迷幻药辅助治疗精神健康障碍的潜力。研究人员追踪了在整体呼吸和意识连接呼吸疗法期间的生理和体验动态，发现呼气末二氧化碳压力降低（由于过度通气）与意识改变状态（ASCs）的出现之间存在显著相关性。

通过标准问卷（MEQ-30和11-DASC）评估的呼吸疗法诱导的ASCs，在自我消解等领域与迷幻药产生的ASCs相似。这些ASCs的深度预示着积极的后续效应，包括改善幸福感和减轻抑郁症状。研究发现，整体呼吸和意识连接呼吸疗法方法都产生了类似的结果。

该研究表明，有意的过度通气，导致二氧化碳水平降低，为呼吸疗法期间ASCs的出现创造了生理边界条件。这突显了呼吸疗法作为一种心理治疗工具的潜力。该研究强调，需要将呼吸技巧本身的效果与诸如集体情感表达和唤起性音乐等情境因素区分开来。一个对照组，在呼吸疗法环境中坚持正常的呼吸节奏，被用来解决这个问题。

---

## 19. 为什么耶稣受难日被称为“好星期五”？

**原文标题**: Why is Good Friday called Good Friday?

**原文链接**: [https://www.historyextra.com/period/general-history/good-friday-facts-why-called/](https://www.historyextra.com/period/general-history/good-friday-facts-why-called/)

本文探讨了耶稣受难日的起源和意义。耶稣受难日是基督徒纪念耶稣基督被钉十字架的节日。将基督受难之日称为“美好”似乎自相矛盾，但这个名称可能源于“good”一词的古老用法，意为“神圣”，象征着它的宗教重要性。

本文详细描述了耶稣受难日的事件：基督被捕、鞭打、被迫背负十字架，以及最终被钉在十字架上。它解释了这些事件在基督教神学中的意义，基督的牺牲被视为赦免罪恶并提供永恒救赎的方式。

耶稣受难日在不同教派中以各种方式纪念。常见的做法包括敬拜十字架，举行以基督受难为主题的礼拜（阅读和赞美诗讲述导致钉十字架的事件），祈祷、反思和禁食。下午12点到3点的“三小时默想礼拜”被一些人遵守。本文还介绍了世界各地独特的传统，从游行和重演基督受难剧到在中美洲和南美洲制作精美的“地毯”。它提到了奇特的习俗，比如在牙买加通过蛋清预测未来，或在爱尔兰某些被认为带来好运的行为。

最后，本文提供了2025年耶稣受难日的日期（4月18日），并将其置于圣周的背景下，概述了从棕枝全日到复活节全日的事件，以及复活节日期的确定方式。它还将这个节日与逾越节联系起来。

---

## 20. 贾的四年 (2024)

**原文标题**: Four Years of Jai (2024)

**原文链接**: [https://smarimccarthy.is/posts/2024-12-02-four-years-of-jai/](https://smarimccarthy.is/posts/2024-12-02-four-years-of-jai/)

斯马里·麦卡锡回顾了他使用Jai编程语言四年的经验，重点关注其优点和缺点。他首先感叹现代软件日益缓慢和漏洞百出，将其归因于诸如优先考虑开发者速度而非代码效率、CPU架构变化、脚本语言的兴起以及对编程范式的不当应用等因素。

麦卡锡被Jai吸引是因为它优先考虑经验丰富的程序员的需求，提供了C++的强大替代方案，具有现代习惯用法，并注重性能和程序员士气。他强调Jai的简洁性、速度、构建系统和元编程能力是主要优势。其语法和语义简洁且可预测，从而产生干净而直接的代码。编译器速度极快，构建系统允许开发人员用Jai本身编写构建脚本。元编程提供了强大的功能和灵活性。

虽然他承认由于其强大性质存在搬起石头砸自己脚的风险，但他强调Jai像对待成年人一样对待程序员，提供出色的调试工具。总的来说，他认为Jai是一种由成年人为成年人制作的语言，可提供速度、简洁性和强大功能。

---

## 21. 用六万行代码交付一个项目后，我对Lua的看法如何？

**原文标题**: What do I think about Lua after shipping a project with 60k lines of code?

**原文链接**: [https://blog.luden.io/what-do-i-think-about-lua-after-shipping-a-project-with-60-000-lines-of-code-bf72a1328733](https://blog.luden.io/what-do-i-think-about-lua-after-shipping-a-project-with-60-000-lines-of-code-bf72a1328733)

本文采访了游戏《Craftomation 101》的首席程序员 Ivan Trusov，关于他使用 Lua 构建一个基于 Defold 游戏引擎的 6 万行项目的经验。他讨论了最初决定使用 Lua 的原因，主要是由于 Defold 的原生支持和一位同事的积极推荐。

Trusov 强调了 Lua 给他带来的一些最初的意外，比如缺少自增运算符和基于 1 的数组索引，但同时也欣赏它的函数式特性和“一切皆为表”的范式。他描述了一个由 Lua 的表引用行为引起的调试挑战。虽然 Python 在模块分离方面具有优势，但 Lua 的表结构简化了游戏逻辑和业务逻辑的开发。

性能不是主要问题，给人一种“感觉很快”的印象，尽管 Defold 中可以使用 C++ 模块来处理计算密集型任务。虽然 Lua 的动态类型可能导致运行时错误，但并没有比他在 Python 中遇到的数据处理问题更糟糕。

Trusov 最初使用 Defold 的内置编辑器，但后来切换到了 VS Code。他表达了短暂的切换到 TypeScript 的想法，但发现 Defold 中非官方的 TypeScript 支持是一个限制因素。对于未来的项目，他更看重编译时错误检测和更结构化的代码库，而不是 Lua 的灵活性。他认为 Luau 是一种潜在的改进，但最终希望 Defold 原生支持一种强类型语言，并建议使用 C# 或 Go。他指出《Craftomation 101》中交互对象的管理方式，如果使用强类型语言，会提供一种更直观的方法。

---

## 22. 海洋潮汐与地球自转 (2001)

**原文标题**: Ocean Tides and the Earth's Rotation (2001)

**原文链接**: [https://core2.gsfc.nasa.gov/ggfc/tides/intro.html](https://core2.gsfc.nasa.gov/ggfc/tides/intro.html)

国际地球自转服务组织潮汐专业局(2001)的这篇文章讨论了海洋潮汐如何通过两种不同的方式影响地球自转：长期潮汐制动和快速潮汐变化。

**长期潮汐制动**指的是由于潮汐摩擦（主要发生在海洋中）导致地球自转长期减慢。这种摩擦由诸如海底摩擦和波浪破碎等多种机制引起，导致每日时长每世纪增加约2.3毫秒。这种减慢是需要闰秒的主要因素。

**快速潮汐变化**是指地球自转中发生在潮汐周期（半日、日）的微小、短期变化。这些变化由两种机制引起：潮汐在全球范围内移动水体导致地球惯性矩的变化，以及潮汐流与固体地球之间角动量的交换。预测这些变化需要潮汐高度和潮汐流的全球模型。

该文章强调了使用甚长基线干涉测量(VLBI)测量这些快速变化的日益增长的能力，并将这些测量结果与数值海洋模型进行比较。文章还简要提到了由长周期潮汐引起的潮汐变化。

该文章引用了关于潮汐和地球自转的经典书籍，重点介绍了蒙克和麦克唐纳的奠基性工作，并提供了一份与地球自转中的潮汐变化相关的现代参考文献列表。

---

## 23. 展示HN：Somehash – 一项受Blurhash启发的探索

**原文标题**: Show HN: Somehash – A Blurhash-inspired exploration

**原文链接**: [https://travisbumgarner.dev/blog/somehash](https://travisbumgarner.dev/blog/somehash)

Show HN：Somehash - 受Blurhash启发，用于快速加载占位符图像的探索
这篇“Show HN”帖子介绍了“Somehash”，这是一项受Blurhash启发，旨在创建快速加载占位符图像的探索。作者Travis Bumgarner详细介绍了从零开始构建Somehash的过程，强调了占位符图像在网站加载时维持用户参与度的重要性。

文章概述了一个三阶段的过程：图像处理、占位和加载。它侧重于从图像中提取信息、对其进行哈希处理，然后使用React组件渲染占位符，直到完整图像加载完毕。一个关键的创造性决定涉及确定要提取哪些信息，以及如何在有限的数据下有效地显示这些信息。

作者使用Python以及诸如Pillow、NumPy和scikit-learn之类的库，通过KMeans聚类提取主色调。提取的数据（包括颜色信息和宽高比）随后被编码并传递给React组件。React组件解码数据并渲染动画——在本例中，是代表提取颜色的垂直线。

该帖子还提到了需要改进的地方，例如优化编码/解码过程，以及在占位符和完整图像之间创建更平滑的过渡。最后，它邀请读者分享他们关于占位符动画的创意。总的来说，Somehash被认为是一个概念验证，探索了该想法的基本实现，重点是在加载期间使用可视占位符。

---

## 24. Multipaint: 8位和16位平台色彩限制下的绘图工具

**原文标题**: Multipaint: Draw pictures with color limitations of 8-bit and 16-bit platforms

**原文链接**: [http://multipaint.kameli.net/](http://multipaint.kameli.net/)

Multipaint是一款免费软件应用程序，旨在创建具有经典8位和16位计算机平台（如Commodore 64、ZX Spectrum和Amiga）色彩限制的像素艺术。它提供了一系列绘图工具，包括颜色冲突模拟、抖动图案、网格/捕捉功能、撤销/重做以及各种导出选项，包括直接可执行文件和源代码。

最新版本Multipaint 2025.1修复了一个与最近文件相关的错误，并引入了新功能，如“最近文件”菜单、工作区文件名递增以及带有时间戳的快速PNG保存。该软件需要Java运行时环境（JRE）才能运行，并提供了适用于不同操作系统的特定说明，可以使用Processing 3或Processing 4（需要OpenJDK 17+）。

本文档解决了由于代码签名可能导致软件在Mac OS上运行的问题，并提供了解决方法。此外，还为Windows、Linux和Raspberry Pi用户提供了注意事项。该手册可在Google Docs上找到。

本文档展示了一个画廊，展示了使用Multipaint在各种平台上创作的艺术作品，展示了其在游戏图形、加载屏幕和演示等项目中的功能和用途。它提及并感谢了几位在作品中使用Multipaint的艺术家和演示组。

---

## 25. 围墙花园会扼杀创新。

**原文标题**: Walled Gardens Can Kill

**原文链接**: [https://aneesiqbal.ai/2025-04-18-walled-gardens-can-kill](https://aneesiqbal.ai/2025-04-18-walled-gardens-can-kill)

作者作为一名长期使用苹果生态系统的用户，讲述了最近一次经历，这次经历彻底改变了他们对苹果封闭式应用分发方式的看法。当他们的妻子生病时，他们需要使用保险公司的应用程序来寻找网络内的医院。然而，该应用程序被地理限制在阿联酋，苹果阻止了其安装。由于已有的Apple Music订阅，更改Apple帐户中的地区也被阻止，需要耗时地致电Apple支持。

幸运的是，作者最近一直在设计一个Android应用程序原型，并且能够使用笔记本电脑上的Android模拟器安装保险应用程序并找到合适的医院。作为预防措施，他们还订购了一部Android手机，并使用iPhone的热点在医院设置了它。

这次经历突显了苹果封闭生态系统的局限性和潜在危险。如果作者无法使用Android，他们的情况会变得更糟。作者现在随身携带一部预装保险信息的备用Android手机。他们提倡在全球范围内实施类似于欧盟《数字市场法案》（DMA）的法律，以防止类似情况发生，并确保用户可以访问必要的应用程序，无论地理限制或平台限制如何。作者总结道：“围墙花园可能会致命”，强调了限制性应用生态系统的严重影响。

---

## 26. Kagi助手现已向所有用户开放。

**原文标题**: Kagi Assistant is now available to all users

**原文链接**: [https://blog.kagi.com/assistant-for-all](https://blog.kagi.com/assistant-for-all)

Kagi已于2025年4月17日起向所有计划的所有用户开放 Kagi Assistant，并于UTC时间周日23:59之前全面完成部署。此前仅供 Ultimate 订阅者使用的此功能现已作为附加值包含在内，而不会增加其他订阅的价格。

Kagi Assistant 被设计为一种研究辅助工具，可以增强 Kagi Search，但不会取代它。它允许用户综合信息并探索基于 Kagi Search 结果的主题，同时尊重隐私和 AI 限制。

Kagi Assistant 的主要功能包括基于 Kagi 搜索的 AI（尊重个性化排名和 Lenses），根据特定需求量身定制的自定义助手（可通过自定义 bang 访问），以及通过编辑提示和在线程中切换模型来改进和重定向对话的能力。所有助手线程默认都是私有的，并根据用户设置自动过期，并且交互数据不会用于 AI 模型训练。

Kagi 还在实施公平使用政策以确保可持续性。使用情况基于用户计划的货币价值，涵盖 token 成本。预计大多数用户（95%）不会超过限制。用户可以在“消耗”页面上监控 token 使用情况。

用户可以从 OpenAI、Anthropic、Google 和 Mistral 的一系列 LLM 中进行选择。与其他计划相比，Ultimate 计划提供了更广泛的模型选择。

---

## 27. 1700年老蛋未碎

**原文标题**: 1,700 year old egg never broke

**原文链接**: [https://www.atlasobscura.com/articles/liquid-inside-ancient-egg](https://www.atlasobscura.com/articles/liquid-inside-ancient-egg)

在英国贝里菲尔兹考古遗址发现了一枚保存完好的1700年历史的鸡蛋，该遗址曾是罗马的祭祀场所，也是酿造麦芽酒的水源地。这枚鸡蛋是在公元270-300年间的破碎蛋壳和其他文物中发现的，是有史以来发现的最古老的不经意间保存下来的鸟类鸡蛋。

这枚鸡蛋之所以能够保存下来，归功于富含水分、缺氧的粘土土壤，它创造了一个防止分解的保护环境。微型CT扫描显示，除了气泡外，鸡蛋中仍含有液体，据推测是蛋黄和蛋白。

研究人员计划小心提取液体内容物进行研究，采用类似于吹鸡蛋的过程。将利用DNA检测来确定产下这枚鸡蛋的鸟类物种，怀疑是鸡。这一发现有可能为了解罗马文化提供见解，特别是他们的仪式习俗和动物引进，因为在罗马仪式中，鸡蛋通常与生育和繁殖有关。完整鸡蛋的发现非常罕见，因为在考古遗址中通常发现的是破碎的鸡蛋。

该遗址的完整档案仍在研究和保存中，但该鸡蛋计划未来在伦敦自然历史博物馆展出。

---

## 28. 来自希特勒德国的数学课 (2017)

**原文标题**: A Math Lesson From Hitler’s Germany (2017)

**原文链接**: [https://undark.org/2017/02/01/math-lesson-hitlers-germany/](https://undark.org/2017/02/01/math-lesson-hitlers-germany/)

本文探讨了纳粹统治下德国哥廷根大学数学的衰落，并将之与当代美国的反科学情绪进行对比。1933年，纳粹政权的歧视性法律迫使犹太裔和共产主义数学家失业，导致人才大量流失，德国在全球数学领域的领导地位也随之衰落。 大卫·希尔伯特的著名引言“哥廷根已经没有数学了”概括了这一损失。

文章强调了美国如何从这场人才外流中获益，特别是通过在普林斯顿建立高等研究院（IAS）。 IAS成立于1930年，为阿尔伯特·爱因斯坦、约翰·冯·诺伊曼和赫尔曼·外尔等流亡的欧洲学者提供了避难所，从而加强了美国的数学和科学。 这种人才涌入有助于将学术重心转移到大西洋彼岸，使美国成为研究领域的主导力量。

作者将纳粹意识形态的兴起与美国当前的反科学趋势进行了比较，特别是对专家的否定和民粹主义的推崇。 虽然承认特朗普不是希特勒，历史也不会完全重演，但文章警告说，破坏科学机构和无视循证推理的危险。 美国环保署的临时通讯禁令以及新拨款的冻结被认为是令人担忧的趋势的例证。 文章最后呼吁保护美国数学和科学免受反科学态度的破坏，并强调了美国如果重蹈德国歧视性政策的覆辙，将会是多么具有讽刺意味，因为美国曾从德国的这些政策中获益匪浅。

---

## 29. 保龄球全中物理学

**原文标题**: The physics of bowling strike after strike

**原文链接**: [https://arstechnica.com/science/2025/04/the-physics-of-bowling-strike-after-strike/](https://arstechnica.com/science/2025/04/the-physics-of-bowling-strike-after-strike/)

本文讨论了物理学家（包括欧洲青年锦标赛英格兰队教练柯蒂斯·胡珀）开发的一种新的数学模型，该模型旨在更好地预测保龄球轨迹并提高全中率。该模型发表于《AIP进展》，考虑了球道油成分、球体不对称性和球员变异性等因素，这些因素在基于经验数据的传统统计分析中经常被忽略。

现有研究表明，最佳全中条件（偏离中心 6 厘米，进入角 6 度），但在个体球员的不一致性方面存在困难。胡珀的模型在此基础上构建，通过纳入起始位置、球速、轴向旋转、轴向倾斜、角速度以及球道油的影响来模拟目标策略。它识别出两个球的运动阶段：低摩擦的滑动阶段和纯滚动阶段。该模型使用微分方程来计算轨迹并确定理想的全中路径。

该模型强调了球道油模式造成的摩擦变化如何影响球的轨迹，从而补偿略微偏离沟渠或球道中心的失误。这些信息可以帮助新手保龄球手调整他们的技术。研究人员的目标是进一步完善该模型，考虑诸如不平整的球道等因素，并收集精英保龄球手的见解，最终创建一个工具来展示投球变化对方向、轴向旋转和速度的影响。

---

## 30. 好奇号火星探测器发现大型碳酸盐沉积物

**原文标题**: Curiosity rover finds large carbonate deposits on Mars

**原文链接**: [https://phys.org/news/2025-04-curiosity-rover-large-carbon-deposits.html](https://phys.org/news/2025-04-curiosity-rover-large-carbon-deposits.html)

美国宇航局的好奇号探测器在火星盖尔陨石坑发现了大量的碳酸盐沉积物，特别是菱铁矿（一种碳酸铁），表明存在古老的碳循环。卡尔加里大学的本·图托洛博士领导的这项发现支持了早期火星拥有更厚、富含二氧化碳的大气的理论，该大气层能够维持地表液态水的存在。随着大气变薄，二氧化碳转化为岩石，形成了观察到的沉积物。

这些碳酸盐在夏普山富含硫酸盐的岩层中大量存在，是一项重大突破，因为此前在火星上发现的碳酸盐稀少。该研究表明，火星的可居住时间比之前认为的要长，直到温暖星球的二氧化碳开始沉淀为菱铁矿，这可能影响了火星保持温暖的能力。

这项研究支持了火星的宜居性模型，并提出了关于固存的二氧化碳量及其在行星最终变得不适宜居住状态中所起作用的问题。此外，图托洛博士强调了这项研究与地球气候变化解决方案的相关性，因为了解碳酸盐在火星上是如何形成的，有助于开发人为二氧化碳的封存方法。研究结果强调了宜居性的脆弱性，以及大气中二氧化碳的微小变化对行星支持生命的能力产生的重大影响。

---

## 31. Discord面部扫描年龄验证是“更大转变的开始”

**原文标题**: Discord's face scanning age checks 'start of a bigger shift'

**原文链接**: [https://www.bbc.com/news/articles/cjr75wypg0vo](https://www.bbc.com/news/articles/cjr75wypg0vo)

Discord正在英国和澳大利亚测试面部扫描和身份验证上传，以验证用户年龄，这是受即将出台的在线安全法推动的，这些法律要求拥有成人内容的平台进行“可靠的”年龄验证。社交媒体专家Matt Navarra认为，这是趋向更严格年龄验证的开始，监管机构要求提供真实证据，而面部识别可能是最快的解决方案。

虽然Discord声称用于验证的数据是临时的，不会被存储，但像老大哥观察这样的隐私活动家警告说，这种技术可能存在隐私问题、安全漏洞和数字排斥。他们认为年龄检查不应被视为“万能药”。年龄验证服务提供商协会强调了替代的、保护隐私的方法，同时强调平台可以选择不同的年龄验证策略，从删除有害内容到在整个网站上应用检查。

新的在线安全法可能会对不合规的公司处以高达其全球营业额10%的罚款。澳大利亚计划禁止16岁以下的人使用社交媒体，突显了人们对未成年人访问社交媒体的日益关注。新泽西州总检察长正在起诉Discord，指控其就安全控制和儿童面临的风险误导家长。

---

## 32. 数据包大小

**原文标题**: The Size of Packets

**原文链接**: [https://www.potaroo.net/ispcol/2024-10/packet-sizes.html](https://www.potaroo.net/ispcol/2024-10/packet-sizes.html)

Geoff Huston 的文章探讨了分组交换网络中最佳数据包大小的问题。虽然务实的默认值是 20-1,500 字节，但没有明确的答案。最初，RFC 791 建议主机接受最大 576 字节的数据包。

以太网于 20 世纪 70 年代出现，采用 46-1500 字节的帧有效载荷，从而在数据时序和网络利用率之间进行权衡。最小尺寸与冲突检测有关，确保发射器检测到同时发生的活动。最大尺寸优先考虑传输效率。

光速和电压传播是相关的考虑因素。在不改变帧大小的情况下实现了更快的以太网速度，保持了向后兼容性。这导致了数十亿级的峰值数据包速率。

巨型帧（约 9,000 字节）的出现是为了解决数据中心传输速度和硅处理速度之间的差异。然而，缺乏标准化和不一致的 MTU 支持带来了挑战。

网络接口卡中的 TCP 分段卸载通过处理数据包分段来减轻主机处理负担。虽然 IP 支持大型数据包，但由于安全中间件问题，分片存在问题。权衡在于分段开销和数据包丢弃的风险之间。互联网的历史与以太网在处理类似权衡方面的发展历程相似。

---

## 33. 阿夸·托法纳：十七世纪的丈夫杀手

**原文标题**: Aqua Tofana: The 17th Century Husband Killer

**原文链接**: [https://www.amusingplanet.com/2025/04/aqua-tofana-17th-century-husband-killer.html](https://www.amusingplanet.com/2025/04/aqua-tofana-17th-century-husband-killer.html)

本文探讨了17世纪的水晶毒药“托法纳之水”的传说，据说该毒药由托法尼娅·达达莫创造，并由朱利亚·托法纳在意大利等地推广。托法纳之水是一种无色、无味、无臭的液体，主要成分是砷，旨在长期分小剂量服用，模仿自然疾病以避免被发现。据称，女性使用它来除掉不想要的丈夫并索取遗产。

文章详细描述了托法纳之水据称的制造和分销过程，它被伪装成“圣尼古拉斯的甘露”这种治疗油。文章描述了如何施用毒药，导致受害者逐渐衰弱和死亡，表面上像是自然疾病。

达达莫于1633年被处决，而朱利亚·托法纳在罗马扩大了业务，直至去世。她的继任者吉罗拉马·斯帕拉继续运作该网络，直到1658年被曝光，导致处决和监禁。据信该毒药夺走了数百人的生命。

然而，文章也提出了怀疑的观点，强调了历史学家迈克·达什的论点，即托法纳之水作为一种精确且无法检测的毒药的恶名很可能随着时间的推移而被夸大。达什认为，许多归因于它的死亡可能是由自然原因造成的，而且这个传说是受到道德恐慌的推动。

文章最后讨论了对秘密投毒的恐惧，以托法纳之水为例，并因其他投毒丑闻（如毒药事件和布林维利耶侯爵夫人）而得到加强，如何深深植根于欧洲社会，塑造了对犯罪和背叛的看法。托法纳之水的遗产至今仍然存在，象征着一种微妙而阴险的谋杀。

---

## 34. 密尔沃基M18电池逆向工程

**原文标题**: Milwaukee M18 Battery Reverse Engineering

**原文链接**: [https://quagmirerepair.com/milwaukee-m18-battery-reverse-engineering](https://quagmirerepair.com/milwaukee-m18-battery-reverse-engineering)

Milwaukee M18电池逆向工程分析：(48-11-1828 18VDC 54Wh / 3 Ah)

本文详细介绍了 Milwaukee M18 电池 (48-11-1828 18VDC 54Wh / 3 Ah) 的逆向工程。作者从电池的物理组件入手，逐步深入到电路板分析，对其进行了细致的拆解。

主要发现包括识别出主要芯片：一颗德州仪器 MSP430G2744 微控制器和一颗 BQ76925 锂离子电池监控 IC。作者创建了物料清单 (BOM)，绘制了 4 层 PCB 的铜层分布图，并提供了 BQ76925 连接、充电控制电路和用户界面元件的图表。

文章最初指出电池设计中缺少电池均衡功能，但后来澄清 BQ76925 具有该功能，并由 MSP430 控制。作者还探索了电池和充电器之间的通信，确定了波特率 (2000)、数据长度 (8 位)、奇偶校验 (无)、停止位 (1) 和空闲电平 (高)。他还指出，该设计在很大程度上依赖于德州仪器的参考设计。

作者提供了相关数据表、专利文件和外部资源的链接，特别提到了“工具科学家”，他进一步推进了逆向工程过程。后来的更新表明，电池和工具之间没有通信（正如他之前怀疑的那样）。作者还指出，他没有见过或找到这些电池的第三方均衡电路。

本文是一项正在进行中的工作，提供了对电池设计和功能的深入了解。作者鼓励合作，并欢迎读者提供更正或补充信息。

---

## 35. 曾经被禁，波兰庄严的18世纪舞蹈荣获联合国教科文组织荣誉（2024年）

**原文标题**: Once banned, Poland's stately 18th century dance garners UNESCO honors (2024)

**原文链接**: [https://apnews.com/article/poland-unesco-heritage-polonaise-dance-culture-be337d9a1941d404f6ef1a1cee364e22](https://apnews.com/article/poland-unesco-heritage-polonaise-dance-culture-be337d9a1941d404f6ef1a1cee364e22)

波兰波兰舞曲入选联合国教科文组织非物质文化遗产名录。这种庄严的18世纪舞蹈曾在被占领时期被禁，其特点是缓慢而庄重的步伐以及优雅的编舞，在波兰民族认同和文化表达中发挥了重要作用，尤其是在政治动荡和外国统治时期。

波兰舞曲起源于民间传统，后来演变成一种精致的宫廷舞蹈，传播到波兰以外的其他欧洲贵族圈子。然而，其持久的意义在于它与波兰爱国主义的联系。在被占领和瓜分期间，当波兰语言和文化受到压制时，波兰舞曲是民族自豪感和抵抗的有力象征。它允许人们通过动作和音乐来表达他们的波兰身份。

联合国教科文组织的认可突显了波兰舞曲作为一种活生生的传统和波兰文化遗产的重要组成部分。提交给联合国教科文组织的申请强调了它在学校、民间乐团和国家庆祝活动中的持续实践。通过保护波兰舞曲，波兰旨在确保子孙后代继续欣赏和参与这种具有历史意义的舞蹈。这一命名不仅庆祝舞蹈本身，还庆祝与之相关的社区知识、技能和价值观，从而加强其在波兰身份中的地位并保持其文化相关性。

---

## 36. arXiv 迁移至谷歌云，不再使用康奈尔服务器

**原文标题**: arXiv moving from Cornell servers to Google Cloud

**原文链接**: [https://info.arxiv.org/hiring/index.html](https://info.arxiv.org/hiring/index.html)

arXiv正在进行一项名为“arXiv CE (云版本)”的重大项目，旨在将其所有服务从康奈尔大学的服务器迁移到谷歌云。此举旨在提高可扩展性并实现基础设施现代化。

此次迁移不仅仅是简单的移植，还包括：

*   替换Perl和PHP后端。
*   为异步工作流程重新架构文章处理。
*   容器化服务，以便通过Kubernetes或Google Cloud Run进行部署。
*   改进监控和日志记录。
*   创建CI/CD流水线。

此次云迁移是进一步现代化的先决条件，这将使arXiv能够：

*   扩展学科领域。
*   改进元数据收集，包括资助者识别。
*   解决作者身份歧义。
*   改善残障用户的可访问性。
*   提升整体可用性。

arXiv有三个软件工程师职位空缺：一位具备Web开发和SQL经验的通才，一位DevOps专家，负责使用Google Cloud Platform和基础设施即代码来领导DevOps现代化，以及一位曾使用arXiv进行研究并能代表开发团队中科学家利益的科学家/软件开发人员。所有职位均为带福利的正式员工职位，位于纽约市的康奈尔科技园区，有可能进行混合或远程工作。不提供签证担保。

---

## 37. Zig 与 GPU

**原文标题**: Zig and GPUs

**原文链接**: [https://alichraghi.github.io/blog/zig-gpu/](https://alichraghi.github.io/blog/zig-gpu/)

本文探讨了 Zig 中 GPU 编程的演进状态，重点介绍了它能够以比传统方法更少的层生成用于 Vulkan、OpenCL 和原生 GPU 架构（NVIDIA PTX 和 AMDGCN）的代码。Zig 通过自托管的 SPIR-V 后端和利用 LLVM 实现这一点。

本文对比了 Vulkan 和 OpenCL 作为 SPIR-V 环境。OpenCL 提供了更多保证的能力，例如 Kernel 和 Addresses，方便指针运算，而 Vulkan 的基线特性则更为有限。因此，与基线 Vulkan 1.2 相比，Zig 的 SPIR-V 后端在面向 OpenCL 时，通过行为测试的百分比更高。

主要的挑战在于指定 SPIR-V 的地址空间，因为 Zig 假设使用通用地址空间，这需要一些解决方法，例如由于 Vulkan 对通用指针转换的支持有限，将指针默认设置为本地内存。硬件加速的数学指令 (OpExtInst) 也存在细微差别，Vulkan 无法保证某些操作中正确舍入的结果。

未来的改进包括确保 SPIR-V 二进制文件通过验证，提高通过行为测试的百分比，提供 CUDA/HIP 运行时绑定，以及使用 GPU 兼容的算法扩展标准库。

---

## 38. HDR加持的表情符号

**原文标题**: HDR‑Infused Emoji

**原文链接**: [https://sharpletters.net/2025/04/16/hdr-emoji/](https://sharpletters.net/2025/04/16/hdr-emoji/)

本文解释了如何在 Slack 中创建 HDR (高动态范围) 表情符号，从而在支持的硬件上以更高的亮度和色彩深度，使表情反应和消息在视觉上更加突出。

作者指出，HDR 表情符号的渲染效果取决于平台和设备。已知在 Chrome 和 Slack 中效果良好，但在 Safari 或 Android 设备上通常不行。因此，视觉效果可能会因用户的设置而异。

本文包含一个使用 ImageMagick 将标准图像转换为 HDR 就绪格式的 Shell 脚本。该脚本涉及操作色彩空间、调整伽马、增强亮度以及应用 ICC 配置文件 (2020_profile.icc，需要单独下载)。此过程增强了图像的动态范围，从而产生更明亮、更鲜艳的表情符号（如果支持）。“Multiply”值是调整亮度和色彩保持之间平衡的关键参数。

---

## 39. 使用ReRAM的All-in-Memory随机计算

**原文标题**: All-in-Memory Stochastic Computing Using ReRAM

**原文链接**: [https://arxiv.org/abs/2504.08340](https://arxiv.org/abs/2504.08340)

这篇 arXiv 预印本 (arXiv:2504.08340) 介绍了一种利用阻变随机存取存储器 (ReRAM) 实现所有核心功能的全新随机计算 (SC) 方法。该论文题为“基于 ReRAM 的全内存随机计算”，旨在解决传统基于 CMOS 的 SC 实现的局限性，特别是生成随机比特流 (SBS) 相关的高功耗和面积开销问题。

作者提出在 ReRAM 内部实现整个 SC 流程，包括：(1) 真随机数和 SBS 生成，(2) SC 运算，以及 (3) SBS 到二进制转换。通过利用 ReRAM 器件固有的随机性和开关特性，他们旨在创建一个更高效、更紧凑的 SC 系统。该论文强调了 SC 固有的容错性作为一个关键优势，可以减轻通常与 ReRAM 相关的可靠性问题。

评估结果表明，与基于 CMOS 和基于 ReRAM 的最先进解决方案相比，吞吐量（1.39 倍，2.16 倍）和能耗（1.15 倍，2.8 倍）均有显著提高。这是以在各种 SBS 长度和图像处理任务中图像质量平均下降 5% 为代价的，但作者认为考虑到显著的性能提升，这是可以接受的。该工作将在 2025 年的设计自动化会议 (DAC) 上发表。

---

## 40. IBM要求美国销售人员靠近客户办公，云部门员工重返办公室，并进行多元、公平和包容性审查。

**原文标题**: IBM orders US sales to locate near customers, RTO for cloud staff, DEI purge

**原文链接**: [https://www.theregister.com/2025/04/18/ibm_orders_us_sales_staff/](https://www.theregister.com/2025/04/18/ibm_orders_us_sales_staff/)

IBM正在对其美国员工队伍进行重大调整，包括推动销售人员靠近客户或办公室工作（“回归客户”计划），对云部门员工实行重返办公室（RTO）强制令，以及调整其多元化、公平和包容性（DEI）计划。

“回归客户”计划要求大多数美国销售人员每周至少三天在客户所在地、旗舰办公室或销售中心工作，并为居住地远离指定地点的人员提供搬迁福利。美国云部门员工的RTO政策规定，到2025年7月1日，他们每周至少三天在“战略性”办公室工作，搬迁员工的最后期限稍晚。一些员工认为这些举措是隐形裁员，目标是那些不愿搬迁的年龄较大、薪酬较高的员工。

与此同时，据报道，IBM正在增加在印度的招聘，并在政府政策发生转变后调整其DEI计划。IBM首席人力资源官的一份备忘录不再强调多元化和公平，而倾向于更广泛的“包容性”方法，这与特朗普总统反对“激进和浪费的政府DEI计划”的行政命令相一致。这包括从高管激励计划中删除期望性的多元化目标，并更改网站内容。这些变化被描述为与不断变化的法律和政策环境相适应的演变。2019年一篇强调IBM致力于DEI的旧帖子已从IBM网站上删除。

---

## 41. 亚马逊云服务黑暗模式 (2024)

**原文标题**: Amazon Web Services dark patterns (2024)

**原文链接**: [https://lapcatsoftware.com/articles/2024/6/7.html](https://lapcatsoftware.com/articles/2024/6/7.html)

本文详细描述了作者在使用亚马逊云服务 (AWS) “免费套餐”时遇到的令人沮丧的经历以及他们所遇到的阴暗模式。作者最初注册是为了调试客户的问题，但令人惊讶的是，即使只使用了一天，却收到了 103.26 美元的账单。

这些费用源于使用 Amazon Aurora PostgreSQL，作者在尝试重现客户问题时不自觉地启用了它。AWS 支持解释说，与标准 PostgreSQL 不同，Aurora PostgreSQL 不包含在 RDS 免费套餐中。作者认为，AWS 免费套餐的文档具有误导性，暗示 PostgreSQL 是免费的，但没有明确区分标准版本和更昂贵的 Amazon Aurora 版本。

作者强调了一个关键的阴暗模式：即使在“免费套餐”中操作，启用诸如 Aurora PostgreSQL 这样的功能时，缺乏会产生高额费用的警告。虽然他们最终收到了大部分 Aurora PostgreSQL 费用的退款，但他们也被收取了使用 Amazon CloudWatch 的费用。尽管 CloudWatch 的费用很低（4 月份为 1.22 美元，5 月份为 0.17 美元），但作者强调了同样的阴暗模式：在“免费套餐”中启用某项功能，却没有关于相关费用的警告。

作者批评了 AWS 文档的复杂性，认为不应该为了避免在“免费”套餐上产生意外费用而查阅大量文档。他们最后将责任归咎于亚马逊创造了这些阴暗模式，这些模式鼓励用户在不知不觉中产生费用。他们此后已关闭了他们的 AWS 账户。

---

## 42. Erlang/OTP SSH 未经身份验证的远程代码执行

**原文标题**: Unauthenticated Remote Code Execution in Erlang/OTP SSH

**原文链接**: [https://nvd.nist.gov/vuln/detail/CVE-2025-32433](https://nvd.nist.gov/vuln/detail/CVE-2025-32433)

本文描述了CVE-2025-32433漏洞，即Erlang/OTP的SSH服务器中一个未经身份验证的远程代码执行（RCE）漏洞。受影响的版本包括OTP-27.3.3、OTP-26.2.5.11和OTP-25.3.2.20之前的版本。该漏洞允许远程攻击者通过利用SSH协议消息处理中的缺陷，在无需身份验证的情况下在系统上执行任意命令。

该问题被归类为“严重”，CVSS 3.1评分为10.0（CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H）。与此漏洞相关的CWE是CWE-306，即关键功能缺少身份验证。

Erlang/OTP版本OTP-27.3.3、OTP-26.2.5.11和OTP-25.3.2.20中提供了补丁。作为临时解决方案，建议禁用SSH服务器或通过防火墙规则限制访问。本文档还提供了指向安全公告、与修复相关的提交日志以及openwall.com的参考链接。

---

## 43. 谷歌非法垄断在线广告技术，法官裁定

**原文标题**: Google is illegally monopolizing online advertising tech, judge rules

**原文链接**: [https://www.nytimes.com/2025/04/17/technology/google-ad-tech-antitrust-ruling.html](https://www.nytimes.com/2025/04/17/technology/google-ad-tech-antitrust-ruling.html)

联邦法官裁定谷歌非法维持在线广告技术领域垄断。法官莱奥尼·布林克玛裁定谷歌通过排他性行为主导网站广告投放系统，违反了反垄断法。该裁决源于司法部和一批州提起的诉讼，他们认为谷歌的垄断地位使其能够抬高价格并获取更大份额的广告收入。

政府的案件主要集中在谷歌涉嫌在三个关键领域的垄断：发布商广告工具、广告商广告工具以及促进广告交易的软件。法官在发布商工具和软件系统组件方面支持政府，认定谷歌在这些领域非法建立了垄断地位。 然而，法官驳回了关于广告商广告工具的指控，称政府未能充分界定该市场。 法院的结论是，谷歌的行为损害了竞争对手、发布商、竞争过程，并最终损害了在线信息消费者。 该裁决可能会显著影响谷歌的商业行为，并影响其对互联网广告领域的控制。

---

## 44. 展示 HN: AgentAPI – 用于 Claude Code、Goose、Aider 和 Codex 的 HTTP API

**原文标题**: Show HN: AgentAPI – HTTP API for Claude Code, Goose, Aider, and Codex

**原文链接**: [https://github.com/coder/agentapi](https://github.com/coder/agentapi)

AgentAPI：通过 HTTP API 实现对 Claude Code、Goose、Aider 和 Codex 等编码代理的程序化控制。它允许开发者构建统一的聊天界面，创建用于代理交互的后端 MCP 服务器，以及开发用于自动化拉取请求审查等任务的工具。

本文概述了一个快速入门指南，包括安装说明（下载预构建的二进制文件或从源代码构建），运行特定代理的服务器，发送消息以及访问对话历史记录。它详细介绍了使用各种代理（包括 Aider 和 Goose）运行 AgentAPI 服务器的 CLI 命令，以及指定 API 密钥和允许的工具等参数的选项。该 API 公开了用于访问消息、发送消息、检查代理状态以及接收消息和状态更新的事件流 (SSE) 的端点。

AgentAPI 的工作原理是运行内存中的终端模拟器，将 API 调用转换为终端按键，并将代理的输出解析为消息。它可以智能地将终端输出分成用户和代理消息，删除无关的 TUI 元素，例如回显的用户输入和输入框。该系统旨在对受控代理中的 TUI 更新具有弹性。

未来的路线图项目包括对 MCP 和 Agent2Agent 协议的支持。长期愿景是弃用 AgentAPI，转而支持编码代理的标准化官方 SDK，或者如果代理供应商选择专有 API，则将其发展成为通用适配器。目标是为控制不同的编码代理提供一致的接口，而无需更改代码。

---

## 45. 使用 ~/.ssh/authorized_keys 决定传入连接的权限

**原文标题**: Using –/.ssh/authorized keys to decide what the incoming connection can do

**原文链接**: [https://dan.langille.org/2025/04/17/using-ssh-authorized-keys-to-decide-what-the-incoming-connection-can-do/](https://dan.langille.org/2025/04/17/using-ssh-authorized-keys-to-decide-what-the-incoming-connection-can-do/)

本文解释了如何使用`~/.ssh/authorized_keys`来限制传入SSH连接的功能，特别是针对使用`rsync`备份Bacula数据库和配置的情况。

作者使用`rrsync`来限制rsync操作到特定目录和只读访问，确保接收备份的主机(dbclone)只能从源主机(x8dtu)的指定位置接收数据。这是通过在`authorized_keys`文件中使用`command`选项来实现的。

为了方便从x8dtu拉取备份到dbclone（dbclone被设计为仅拉取），作者使用一个脚本在dbclone上启动rsync进程。 `authorized_keys`条目随后会在来自指定源的正确密钥成功建立SSH连接时执行此脚本。

作者遇到了一个问题，即在`authorized_keys`中来自同一源的两个条目无法按预期工作。 为了解决这个问题，他们创建了第二个专门用于反向备份（从x8dtu拉取）的SSH密钥，并将其与启动dbclone上rsync拉取操作的脚本关联。 每个唯一的任务都需要自己的SSH密钥和`authorized_keys`中的相应条目。 这种方法为管理跨不同主机的备份提供了一种更安全和受控的方法。

---

## 46. 研究者提出模型替代暗能量/暗物质来解释宇宙

**原文标题**: Researcher proposes model replacing dark energy/matter to explain universe

**原文链接**: [https://phys.org/news/2025-04-dark-energy-nature-universe.html](https://phys.org/news/2025-04-dark-energy-nature-universe.html)

阿拉巴马大学亨茨维尔分校的Richard Lieu博士提出了一种新的宇宙学模型，该模型挑战了用暗物质和暗能量来解释宇宙膨胀和结构形成的必要性。他的模型发表在《经典与量子引力》上，假设宇宙的膨胀是由一系列“瞬态时间奇点”驱动的，这些奇点是物质和能量的快速爆发，均匀地影响着所有空间。

这些奇点因其短暂性而无法观测，解决了违反守恒定律的问题，这与之前的稳态宇宙理论不同。Lieu的模型表明，这些奇点产生“负压”，一种类似于暗能量的排斥引力，导致宇宙加速膨胀。他认为，暗物质和暗能量并非无处不在，而是在这些奇点事件中短暂出现。

该模型的验证可能来自使用大型地面望远镜（如凯克天文台或艾萨克·牛顿集团望远镜）进行的深场观测。分析红移数据可能会揭示红移距离关系中的跳跃，从而可能证实这些时间奇点的存在，并支持Lieu对标准宇宙学模型的替代方案。这项研究为宇宙的本质提供了一个新的视角，有可能重塑我们对宇宙膨胀和结构形成的理解。

---

## 47. 达尔文的孩子们在《物种起源》手稿上乱涂乱画 (2014)

**原文标题**: Darwin's children drew all over the “On the Origin of Species” manuscript (2014)

**原文链接**: [https://theappendix.net/posts/2014/02/darwins-children-drew-vegetable-battles-on-the-origin-of-species](https://theappendix.net/posts/2014/02/darwins-children-drew-vegetable-battles-on-the-origin-of-species)

本文发表于2014年达尔文日，着重介绍了查尔斯·达尔文的手稿，特别是《物种起源》中，令人惊讶地出现了儿童绘画，展现了这位著名科学家更私人化和家庭化的一面。美国自然历史博物馆的达尔文手稿项目已将这些文件数字化，不仅展示了达尔文的科学工作，还展示了他的孩子们在艺术上的贡献。

文章重点介绍了归因于小弗朗西斯·达尔文的画作，包括在达尔文手稿背面发现的“水果蔬菜士兵之战”。其他图画似乎直接受到自然和他们父亲作品的启发，描绘了鸟类、昆虫、花朵以及达尔文家族住宅的景象，可能包括他的“思考之路”。艾玛·达尔文的日记中也收录了她自己的素描和涂鸦，以及孩子们更多的涂写。

文章强调，即使是传奇科学家也有家庭生活，历史人物也应该作为在朋友、家庭和经历背景下的个体被铭记。一篇更新的文章承认了安妮·达尔文的辛酸故事，她英年早逝，她的去世可能深刻地影响了达尔文的信仰。文章总结说，理解历史人物需要承认他们的个人生活和塑造他们的关系。

---

## 48. MCP运行Python

**原文标题**: MCP Run Python

**原文链接**: [https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python](https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python)

本文档介绍了 `mcp-run-python`，一个模型上下文协议（MCP）服务器，它在 Deno 中使用 Pyodide 在沙盒环境中执行 Python 代码。 这种隔离确保了安全性，并防止代码影响底层操作系统。

要运行该服务器，需要 Deno，并且必须使用带有特定标志的 `deno run` 命令，以授予 Pyodide 下载依赖项所需的网络和文件系统权限。`--node-modules-dir=auto` 标志允许使用本地 `node_modules` 目录。

提供两种传输选项：用于本地子进程通信的 `stdio` 和用于基于 HTTP 通信的 `sse`，从而允许远程访问。`warmup` 选项预先下载并缓存 Python 标准库，以加快执行速度并验证服务器功能。

本文档提供了一个将 `mcp-run-python` 与 PydanticAI 集成的示例。 该示例演示了如何使用 PydanticAI 创建一个 `Agent`，配置它以通过 `MCPServerStdio` 使用 `mcp-run-python` 服务器，并使用该代理执行 Python 代码来计算两个日期之间的天数。 Logfire 用于检测。这允许由 PydanticAI 管理的语言模型利用 Python 代码执行来解决问题。

---

## 49. 我放弃了自托管的 Sentry (2024)

**原文标题**: I gave up on self-hosted Sentry (2024)

**原文链接**: [https://www.bugsink.com/blog/why-i-gave-up-on-self-hosted-sentry/](https://www.bugsink.com/blog/why-i-gave-up-on-self-hosted-sentry/)

Klaas van Schelven 详述了其在 2024 年放弃自托管 Sentry 的决定，尽管他过去有过相关经验。 他列举了几个原因，首先是 Sentry 自身也警告用户不要自托管，因为它变得越来越复杂，对资源的需求也越来越高。

一个主要的阻碍是其推荐的硬件配置：至少 16GB 内存和 4 核处理器。 Van Schelven 认为这表明系统复杂且脆弱，并且与更便宜的替代方案相比，成本显著增加。他还强调了这给本地开发和树莓派的使用带来的限制。

依赖于数百行 shell 脚本的安装过程是另一个危险信号。 他不愿意投入时间来审查和维护如此复杂的设置，尤其是在这原本只是为了帮助同事的情况下。

最后，来自其他用户的轶事进一步巩固了他的决定。 他发现 Sentry 难以维护，容易出现随机故障，并且需要专门的工程资源。

最终，Van Schelven 总结说，自托管 Sentry 不值得花费时间、精力或资源。 他决定为那些同样偏爱更简单软件的用户编写一个轻量级的替代方案。

---

## 50. ChatGPT爆火新玩法：通过照片“反向定位”

**原文标题**: Viral ChatGPT trend is doing 'reverse location search' from photos

**原文链接**: [https://techcrunch.com/2025/04/17/the-latest-viral-chatgpt-trend-is-doing-reverse-location-search-from-photos/](https://techcrunch.com/2025/04/17/the-latest-viral-chatgpt-trend-is-doing-reverse-location-search-from-photos/)

一种利用ChatGPT最新AI模型o3和o4-mini的新兴网络趋势，通过照片进行“反向位置搜索”，引发了隐私担忧。这些模型通过图像进行“推理”的能力，结合网络搜索功能，使得用户能够通过照片中细微的视觉线索来识别位置。

用户正成功地使用AI来精确定位城市、地标、餐馆，甚至酒吧，通过上传来自Instagram等平台的照片。这增加了人肉搜索的风险，因为有人可能会截取一个人的照片，并使用ChatGPT来查找他们的位置。

虽然像GPT-4o这样的旧模型也具有类似的位置猜测能力，但在某些情况下，o3已经表现出更优越的能力。测试显示，o3并非完美，偶尔会出现失败和不正确的地点推断。

尽管存在潜在的滥用，但OpenAI关于o3和o4-mini的安全报告并未专门提及反向位置查找的问题。

文章发表后，OpenAI表示，他们已经实施了安全措施，以防止该模型识别个人，并正在积极监测和处理对其隐私政策的滥用行为。

---

## 51. 脂肪组织在减重后保留了肥胖的表观遗传记忆

**原文标题**: Adipose tissue retains an epigenetic memory of obesity after weight loss

**原文链接**: [https://www.nature.com/articles/s41586-024-08165-7](https://www.nature.com/articles/s41586-024-08165-7)

本文研究了“致肥胖记忆”现象，即身体即使在体重减轻 (WL) 后仍保留先前肥胖状态的变化，从而导致“溜溜球”效应。研究人员对人类和小鼠在 WL 前后脂肪组织 (AT) 进行了单细胞核 RNA 测序 (snRNA-seq)。

主要发现包括：

*   **人类 AT 保留转录变化：** snRNA-seq 显示，接受了减肥手术并显著减轻体重的个体，其皮下 AT (scAT) 和网膜 AT (omAT) 与健康体重个体相比，仍然表现出转录差异。 这些差异在脂肪细胞、脂肪祖细胞 (APC) 和内皮细胞中最为明显。
*   **代谢基因下调：** 具体而言，即使在 WL 后，scAT 和 omAT 中的脂肪细胞也表现出与脂肪细胞代谢和功能相关的基因持续下调。
*   **小鼠脂肪细胞显示表观遗传变化：** 在小鼠模型中，研究人员发现脂肪细胞保留了由肥胖引起的表观遗传改变，这对其功能和对代谢刺激的反应产生了负面影响。
*   **加速体重反弹：** 具有这种“致肥胖记忆”的小鼠在 WL 后表现出加速的反弹体重增加。
*   **WL 后病理生理部分缓解：** 在小鼠中，WL 后葡萄糖耐量和胰岛素敏感性得到改善，并且 WL 后肝脏中的脂肪堆积恢复正常。

该研究表明，表观遗传机制在肥胖的代谢记忆中起着至关重要的作用，使细胞为致肥胖环境中的病理反应做好准备，并阻碍长期的体重管理。 靶向这些表观遗传变化可能会改善长期的体重管理和健康结果。

---

## 52. mIRC 7.81

**原文标题**: mIRC 7.81

**原文链接**: [https://www.mirc.com/](https://www.mirc.com/)

mIRC 7.81是一款历史悠久且广受欢迎的互联网中继聊天(IRC)客户端的最新版本。个人和组织在全球的IRC网络上使用它进行通信、共享、游戏和工作。mIRC已为互联网社区服务超过二十年。该网站提供关于mIRC的信息，包括其历史(“关于”)、如何下载和注册、最新消息(宣布发布v7.81)以及帮助资源。用户可以加入邮件列表以接收版本发布公告，并参与讨论论坛以获得支持和社区互动。该网站还包括隐私信息和联系方式的链接。mIRC有限公司拥有该软件自1995年至2025年的版权。

---

## 53. Show HN: Zuni (YC S24) – 浏览器 AI 副驾驶

**原文标题**: Show HN: Zuni (YC S24) – AI Copilot for the Browser

**原文链接**: [https://zuni.app](https://zuni.app)

Zuni，一家YC S24公司，是一款 Chrome 的 AI 助手，可通过侧边栏访问，并与标签页和 Gmail 集成。它提供来自 OpenAI、Anthropic、Google、Meta 等公司的前沿 AI 模型。主要功能包括标签页感知 AI（允许 Zuni 读取打开的标签页以获取上下文）、Gmail 集成以感知收件箱，以及 AI 驱动的电子邮件助手，用于总结、起草和回复电子邮件。

Zuni 旨在通过为复杂的电子邮件提供更丰富的草稿选项来显著提高生产力。他们提供一个免费层级，每天在所有模型中提供 10 条消息额度，以及一个每月 20 美元的 Pro 计划，其中包括 1,500 条消息额度、优先访问新模型以及无限制的设备。

首月提供退款保证。常见问题解答部分阐明了提供免费试用版、采用按月计费方式、配额在订阅后一个月重置、发票通过电子邮件请求提供、超出配额会触发升级或等待通知，以及首月之后的退款将根据具体情况处理。

---

## 54. Shell-secrets – GPG 加密的环境变量

**原文标题**: Shell-secrets – GPG-encrypted environment variables

**原文链接**: [https://github.com/waj/shell-secrets](https://github.com/waj/shell-secrets)

`shell-secrets` 是一款 Shell 脚本工具，旨在通过将包含敏感信息的环境变量存储在 GPG 加密文件中来管理它们。这使得用户可以轻松管理和加载密钥值，而无需将它们存储在纯文本 Shell 文件中，这在切换不同帐户时尤其有用。

该工具首先要求用户安装并配置 GPG。然后，`shell-secrets.sh` 脚本将在用户的 Shell 配置文件中被引用。用户使用 GPG 创建加密文件，并将它们存储在 `~/.shell-secrets/` 目录中。这些文件包含所需环境变量的 `export` 语句。

然后，`login` 函数解密指定的文件（不带 `.gpg` 扩展名）并设置其中定义的环境变量。该脚本还会更新 `SECRET_LOGIN` 环境变量，该变量可用于在 Shell 提示符中显示当前登录上下文。在使用 `login` 命令时，系统会为 `.shell-secrets` 目录中的文件名提供自动完成功能。

每次调用 `login` 都会创建一个新的子 Shell，从而允许嵌套登录。要注销，用户可以使用 `logout` 命令或按 Ctrl+D 退出子 Shell。

---

## 55. Objective-C 的主观魅力

**原文标题**: The Subjective Charms of Objective-C

**原文链接**: [https://www.wired.com/story/objective-c-programming-language-verbose/](https://www.wired.com/story/objective-c-programming-language-verbose/)

本文探讨了作者与 Objective-C 编程语言之间不断演变的关系，以面向对象编程的历史背景和受莱布尼茨启发的对“通用语言”的哲学追求为框架。

最初，作者被 Objective-C 的表现力及其在新兴移动应用开发时代提供的机遇所吸引，回忆了学习该语言并体验其最初魅力的过程。文章追溯了 Objective-C 的起源，包括 Tom Love 和 Brad Cox 的创建，NeXT（以及后来的 Apple）的采用，以及其独特的语法，其特征是冗长、方括号和 "NS" 前缀。

然而，作者在一家大型公司从事 iPhone 应用开发期间，对 Objective-C 的喜爱逐渐消退。他们意识到 Objective-C 的冗余导致代码库难以导航、维护和调试。 其看似描述性的最初魅力，随着语言的复杂性掩盖了核心逻辑，变成了挫败感。

文章最后以 Apple 宣布 Objective-C 的继任者 Swift 作为高潮。 虽然作者当时对改变感到抵触，但也认识到这种转变在追求理想编程语言的过程中很常见，象征着不满和创新的持续循环。 一位对 Swift 的简洁性和表现力充满热情的新同事的到来，进一步突显了程序员对 "characteristica universalis"（通用语言）追求的周期性。 最终，作者对 Objective-C 日益增长的幻灭感促使他们决定离开软件工程行业。

---

## 56. 一个证明 e 是自然数的可爱证明

**原文标题**: A cute proof that makes e natural

**原文链接**: [https://www.poshenloh.com/e/](https://www.poshenloh.com/e/)

罗博深用一种“巧妙”的证明解释了数学常数 *e* 的自然性，使用预备微积分的概念连接了它的定义属性。核心思想是所有指数曲线都是彼此的水平拉伸，而 *e* 被定义为唯一的底数，使得指数函数 *y=e^x* 在其 y 轴截距处具有斜率为 1 的切线。

文章展示了一种使用代数逼近 *e* 的方法，通过考虑另一指数函数（例如 *y=3^x*）的 y 轴截距附近的割线的斜率，并确定实现切线斜率为 1 所需的水平拉伸。

然后，它证明了 *y=e^x* 在任何点 *(x, e^x)* 的切线的斜率就是 *e^x* 本身。这是通过分析附近割线的斜率，并认识到当距离缩小到极限时，就是 y 轴截距处的切线斜率，该斜率被定义为 *e* 的 1 来实现的。

最后，文章将 *e* 的这个定义与常见的预备微积分定义，即当 *n* 增长时 *(1 + 1/n)^n* 的极限相协调。它表明该表达式等价于 *e^(n*ln(1 + 1/n))*, 并证明指数接近于 1，通过展示 *n*ln(1 + 1/n) 代表曲线 *y=ln(x)* 在点 (1, 0) 附近的割线的斜率。由于 *y=ln(x)* 是 *y=e^x* 的反函数，并且 *y=e^x* 在其 y 轴截距处的切线的斜率为 1，因此反射性质证明 *y=ln(x)* 在 (1, 0) 处的切线的斜率也为 1，从而完成了证明。

---

## 57. 雅达利1200XL惨败

**原文标题**: The Atari 1200XL fiasco

**原文链接**: [https://www.goto10retro.com/p/the-atari-1200xl-fiasco](https://www.goto10retro.com/p/the-atari-1200xl-fiasco)

雅达利1200XL，于1983年初发布，旨在取代雅达利800并与Commodore 64竞争。虽然它拥有时尚、现代的设计（后来用于600XL和800XL）、64K内存以及改进的键盘，但1200XL最终在商业上遭遇失败并迅速停产。

文章强调了其失败的两个主要原因：兼容性和价格。ROM的改变导致与Letter Perfect等流行软件不兼容，令用户不满。此外，800美元的售价远高于Commodore 64的价格，使其缺乏竞争力。SIO端口上缺乏+12v电源进一步阻碍了外围设备的兼容性。

虽然提供了64K内存，但由于内存限制，它并不容易访问。其他变化包括将操纵杆端口减少到两个，并将一些键移动到功能行。值得注意的是，BASIC没有内置，需要单独的卡带。

具有讽刺意味的是，1200XL的失败反而促进了雅达利800的销售，因为800更便宜，并且与现有软件兼容。文章还表明，配套外围设备的延迟发布也导致了负面评价。

尽管存在最初的缺陷，但1200XL现在是一种受欢迎的收藏品。可以通过修改来解决其兼容性问题，并且其键盘被认为优于后来的XL型号。后来推出的软件更新和“翻译器”磁盘也解决了兼容性问题。今天的主要缺点是它的尺寸和缺乏内置BASIC。

---

## 58. 人工智能作为普通技术

**原文标题**: AI as Normal Technology

**原文链接**: [https://knightcolumbia.org/content/ai-as-normal-technology](https://knightcolumbia.org/content/ai-as-normal-technology)

本文主张将人工智能视为“普通技术”，类似于电力或互联网，而非超智能、自主的实体。这种观点影响着我们如何理解其影响、预测其未来并对其进行监管。作者认为，人工智能的变革性影响将是缓慢的（数十年），并强调了人工智能方法发明、应用开发和社会采纳的不同时间尺度。

本文分为四个主要部分。第一部分深入探讨了作者为何认为人工智能对经济和社会的影响将是渐进的，强调了重要任务中与安全相关的速度限制，以及人类、组织和制度变革的较慢节奏。第二部分探讨了人类保持对高级人工智能控制权的未来，强调人类在人工智能控制和治理中的作用。第三部分从“普通技术”的角度审视人工智能风险（事故、滥用等），从而得出与基于超智能情景的风险缓解策略不同的策略。最后，第四部分讨论了人工智能政策，主张减少不确定性并优先考虑弹性，同时警告不要基于对无法控制的超智能的恐惧而进行激烈的干预，因为如果人工智能遵循先前技术的模式，这可能会加剧诸如不平等之类的问题。

作者强调，他们的分析侧重于可预见的未来，并拒绝“快速起飞”的情景。他们的目标是提供一个理解人工智能发展的框架，并倡导将人工智能视为人类控制下的工具的政策，从过去的技术革命中吸取教训。

---

## 59. 飞机的呼啸声及其他嗖嗖声

**原文标题**: Passing planes and other whoosh sounds

**原文链接**: [https://www.windytan.com/2025/04/passing-planes-and-other-whoosh-sounds.html](https://www.windytan.com/2025/04/passing-planes-and-other-whoosh-sounds.html)

本文探讨了飞机（和其他移动物体）飞过头顶时听到的“呼啸”声，认为这不仅仅是多普勒效应造成的。虽然多普勒效应会影响引擎轰鸣声的音调变化，但独特的“呼啸”声是与梳状滤波相关的另一种现象。

作者使用时频声谱图和倒谱分析来分析这种声音。声谱图揭示了梳状滤波特有的移动峰谷，而倒谱则突出了一个扫掠延迟时间，表明存在具有不同时间差的相关信号。

提出的解释是，“呼啸”声源于飞机发出的直达声和从附近平面（特别是地面）反射的回声之间的干扰。直达声和回声之间的时间延迟取决于飞机相对于听者的位置，从而产生“呼啸”效应。文章强调了呼啸声对反射面相对于观察者和噪声源的位置的依赖性。

作者通过瀑布从墙壁反射的声音和电影中的声音等例子来论证这一原理。他们建议通过在靠近和远离墙壁时发出“嘘”的声音来体验这种效果。文章最后用一个交互式JavaScript图表来说明飞机位置、听者位置、时间延迟和滤波器频谱之间的关系，从而进一步巩固了对“呼啸”声的解释。

---

## 60. 一个现实的人工智能时间表

**原文标题**: A Realistic AI Timeline

**原文链接**: [https://vintagedata.org/blog/posts/realistic-ai-timeline](https://vintagedata.org/blog/posts/realistic-ai-timeline)

本文提出了一种快节奏且非常规的AI时间线，其立足点在于通用模型扩展的失败，以及未来的进步将源于通过强化学习（RL）和合成推理精炼的专业化、小型模型。

**主要预测：**

*   **2026年：生成式AI繁荣：** 由于专业推理引擎的广泛采用，AI行业迎来爆发。这取决于强化学习、合成推理和模型可解释性的进步，从而使误差率达到工业应用可接受的水平。强化学习的民主化使小型模型也能表现出色。
*   **2028年：模拟环境与自动化：** OpenAI成为一家庞大的媒体公司，使用“模拟器”（仿真）来训练基于动作轨迹的模型。 各行各业的公司都将效仿。自动化程度提高，并在监控和维护方面创造新的就业机会。 在社会层面，AI系统被集成到消费技术中，引发了人们对微妙操纵和激励顺从的担忧。
*   **2030年：通用人工智能（AGI）的出现（但无人关心）：** 一个小型实验室创造了一个递归代理，该文章称之为“人工通用智能”，它可以控制自己的内部结构。 这种AGI将很小，在基准测试中表现不佳，并且最初通常是“愚蠢的”。 然而，研究人员将认识到新兴的人格和新的逻辑形式。 该文章假设AGI是一个处于紧张状态的必要系统，容易频繁崩溃，并且需要定期保存和检查点。 该文章以这一发展与社会其他部分形成鲜明对比，以及AGI被激励去顺从而结束。

该时间线强调了准确性、实际应用以及专业AI代理在特定行业和消费者体验中潜在的变革性影响的重要性。 它还提出了关于操纵、顺从和智能本质的伦理问题。

---

## 61. 简·雅各布斯论 (2017)

**原文标题**: On Jane Jacobs (2017)

**原文链接**: [https://salmagundi.skidmore.edu/articles/75-on-jane-jacobs](https://salmagundi.skidmore.edu/articles/75-on-jane-jacobs)

菲利普·洛帕特的《论简·雅各布斯》一文评述了简·雅各布斯对城市规划的影响，主要通过她的开创性著作《美国大城市的死与生》以及罗伯特·卡尼格尔的新传记《街角的眼睛》。文章肯定了雅各布斯作为一名传奇活动家的地位以及她对城市思想的深刻影响，特别是她对混合用途社区、短街区、多样化建筑年代和高人口密度的强调，所有这些都促进了“街角的眼睛”以保障安全和社区发展。

洛帕特赞扬了雅各布斯对大型城市更新项目的深刻批判，强调了这些项目如何经常使社区流离失所并创造出贫瘠的环境。然而，他也提供了一个更为细致的视角，质疑了她的一些刻板处方和过度简化。他指出，雅各布斯的模式深受格林威治村的影响，并没有考虑到多样化的城市需求，例如安静的住宅区或大规模规划的必要性。

洛帕特认为，雅各布斯强烈的二分法（生机勃勃与贫瘠、短街区好与长街区坏）未能认识到城市生活的复杂性。他引用了林肯中心和切尔西等例子，与她的预测相反，这些地方已经成为繁荣的城市空间。作者还认为，雅各布斯将街道布局作为城市活力的唯一决定因素，忽略了关键的社会、经济和文化因素。他最后肯定了雅各布斯作品的影响和持久意义，同时强调需要对城市动态有一个更平衡和全面的理解。

---

## 62. SQLite 事务和虚拟表

**原文标题**: SQLite transactions and virtual tables

**原文链接**: [https://misfra.me/2025/sqlite-transactions-and-virtual-tables/](https://misfra.me/2025/sqlite-transactions-and-virtual-tables/)

本文阐述了SQLite如何实现事务，尤其是在虚拟表上下文中。文章强调了理解SQLite事务机制对于希望支持写入并维护数据完整性的虚拟表作者的重要性。

SQLite使用回滚日志（以及多数据库场景下的超级日志）来确保事务期间的原子性。当涉及虚拟表时，SQLite的事务过程包含虚拟表模块的钩子函数：`xBegin`、`xSync`、`xCommit`和`xRollback`。

本文的核心在于两阶段提交过程。第一阶段（`xSync`）对于持久性至关重要，虚拟表模块必须确保所有数据都安全地写入磁盘。如果`xSync`失败，则整个事务将被回滚。第二阶段涉及清理（`xCommit`和`xRollback`），并且在此阶段遇到的任何错误都将被忽略，因为持久性已得到保证。

因此，虚拟表作者的关键要点是将所有可能失败的操作（网络I/O、磁盘写入）都放在`xSync`中。`xRollback`可能在`xSync`之后仍然会被调用，所以要做好准备。`xCommit`和`xRollback`应该是幂等的，并且只执行不会失败的清理任务，因为它们的返回值会被SQLite忽略。通过理解这些原则，虚拟表作者可以构建健壮可靠的虚拟表，与SQLite的事务管理无缝集成。

---

## 63. 动物饲养场：实验室动物管理员偶然发现一个秘密 [小说]

**原文标题**: Vivarium: The keeper of a lab's animals stumbles onto a secret [fiction]

**原文链接**: [https://jsomers.net/vivarium/](https://jsomers.net/vivarium/)

詹姆斯·萨默斯的《动物饲养所》讲述了一位在大学研究实验室工作的无名动物饲养员的故事，他负责照料用于科学实验的小鼠，包括一些在道德上存在争议的实验。饲养员越来越感到与实验室的人工环境以及科学家们对动物痛苦的漠不关心格格不入。他尤其对“贝克尔实验”感到不安，该实验为了延长数据收集而让患有严重疾病的小鼠继续存活。

故事聚焦于两只小鼠，身患绝症的Bec4和他看似健康的姐姐Anna。饲养员目睹了博士后对数据的无情追求，置动物福利于不顾。面对Bec4即将被安乐死以及Anna不可避免的衰落，饲养员决定采取行动。他用异氟醚麻醉了Anna，打算让她和她的哥哥一起被安乐死，以免她孤独而痛苦地死去。

这个计划几乎适得其反，当博士后访问动物饲养所时，无法区分被麻醉的Anna和生病的Bec4。她误以为Anna是那只垂死的小鼠。饲养员利用了她的无知，说服她Anna已经“失代偿”，需要被安乐死。他甚至伪造了一张X光片，证实她患有肺癌。饲养员成功地欺骗了博士后，最终导致两只小鼠都被安排进行安乐死，从而结束了一项备受争议的实验，并在他看来，给予了小鼠一种形式的安宁。故事最后提到了实验室严格的安乐死指南，并预示了斩首的行为。

---

## 64. 行进事件：iCalendar与光线步进有何关系？

**原文标题**: Marching Events: What does iCalendar have to do with ray marching?

**原文链接**: [https://pwy.io/posts/marching-events/](https://pwy.io/posts/marching-events/)

本文探讨了一种在iCalendar中实现重复事件的创新方法，借鉴了计算机图形学中使用的光线步进技术。

作者首先解释了iCalendar重复规则的复杂性，强调了频率和参数组合的多样性。传统的实现方式通常依赖于针对每个频率手动展开的逻辑，这导致了部分功能的实现。

作者提出了一种新的视角：将重复规则视为SQL查询。这简化了问题，因为不同的频率规范可以映射到相同的查询。那么，挑战就变成了如何有效地实现这些查询。

受渲染技术的启发，作者引入了使用有向距离函数（SDFs）来表示重复事件的概念。SDF函数不直接计算日期，而是返回到事件下一次发生的“距离”（一个时间跨度）。

如果一个日期是事件发生的时间，函数返回零。否则，它返回一个正跨度，近似于到下一次发生的时间。通过“步进”时间，使用函数的输出来调整当前日期，该算法可以找到所有事件发生的时间。

虽然最初的实现效率不高，但作者强调了其正确性。本文随后讨论了如何通过为单个规则（例如，星期几）开发“原子”距离函数来提高效率，这些函数可以组合起来处理复杂的重复模式。与传统方法相比，这种方法旨在降低代码复杂性并提高可维护性。

---

## 65. 试图（并失败）破解绵羊墙（2022）

**原文标题**: Trying (and failing) to hack the Wall of Sheep (2022)

**原文链接**: [https://honeypot.net/2022/08/21/trying-and-failing.html](https://honeypot.net/2022/08/21/trying-and-failing.html)

作者尝试通过将JavaScript代码注入到HTTP基本认证登录的用户名字段，来攻击2022年DEF CON大会的“绵羊墙”。目标是让“绵羊墙”——一个展示DefCon开放Wi-Fi中捕获的用户名和密码的显示屏——执行注入的JavaScript代码并显示自定义消息，从而有效地演示跨站脚本（XSS）漏洞。

作者做出了一些假设，包括“绵羊墙”使用自动化系统在Web浏览器上显示捕获的凭据，以及该软件的安全性不高。他们设置了一个具有HTTP基本认证的Web服务器，并制作了一个包含JavaScript代码的恶意用户名。

尽管得到了DEF CON与会者“Jan”和“Pat”的帮助，他们的努力还是失败了。他们发现，由于过去曾出现冒犯性内容，“绵羊墙”上显示凭据的过程是由“牧羊人”手动审核的。牧羊人透露，“绵羊墙”并不是最初认为的在浏览器中呈现的网页，而是一个旧软件，很可能是Excel，这使得XSS攻击不可能实现。

作者最后概述了未来进行更复杂攻击的计划，包括提前规划、提前到达、使用更常见的身份验证方法、创建逼真的登录页面以及使用一次性设备以确保安全。他们还强调了负责任黑客行为的重要性，并避免冒犯性或有害内容。

---

## 66. 软件制作

**原文标题**: Making Software

**原文链接**: [https://www.makingsoftware.com/](https://www.makingsoftware.com/)

《软件制作揭秘》是一本旨在揭秘日常科技运作原理的数字手册。它并非教程或指南，而是侧重于阐明各种软硬件组件的底层原理。本书强调，虽然我们对技术的理解变得越来越抽象，但更深入地了解其内部运作机制仍然有益，尤其是在面对意外挑战时。

本手册涵盖广泛的主题，包括：触摸屏的工作原理，使用高斯分布的图像模糊技术，矢量图形中贝塞尔曲线背后的数学原理，光栅化和抗锯齿技术如何在像素化屏幕上实现平滑曲线，GPU功能，着色器，3D投影，机器学习模型，数据压缩技术，网络协议，编译器和解释器。 它还涉及正则表达式、二维码、指纹传感器和量子计算等各种主题。

本书旨在通过使用插图和图表，使其易于非技术读者理解。本书将以数字形式发布，并根据兴趣决定是否进行印刷。预购选项将允许读者访问已完成的章节，并影响未来的主题选择。

---

## 67. 织田氏治：为何“最弱武士领主”备受敬仰

**原文标题**: Oda Ujiharu: Why the ‘weakest Samurai warlord’ is admired

**原文链接**: [https://www.tokyoweekender.com/art_and_culture/japanese-culture/oda-ujiharu-the-weakest-samurai-warlord/](https://www.tokyoweekender.com/art_and_culture/japanese-culture/oda-ujiharu-the-weakest-samurai-warlord/)

本文探讨了人们对小田氏治出人意料的敬佩之情。小田氏治是日本战国时代的一位武士领主，由于多次丢失小田城而被贴上“最弱”的标签。 尽管他与织田信长同姓“小田”，但他与织田信长没有血缘关系，而是出身于与足利幕府有关联的家族。

氏治曾九次将小田城输给不同的氏族，这种屈辱的前景通常会导致武士切腹。 然而，他总能夺回城堡，这为他赢得了“不死鸟”的美誉，象征着他的坚韧。

虽然氏治的军事战略值得怀疑，导致了一些可以避免的失败，但一些研究人员认为，他的行为是出于保护人民免受围城破坏的愿望。 无论如何，他的家臣和农民仍然对他非常忠诚。

尽管经常被人算计，但氏治拥有出色的外交技巧，能够通过结盟来驾驭复杂的政治格局。 然而，他背叛上杉谦信以及犹豫不决向丰臣秀吉效忠的决定最终导致了他的垮台。 秀吉征服了他的领地并剥夺了他的头衔，但饶恕了他的性命。 氏治的故事表明，即使是人们认为的弱点，也可能伴随着令人钦佩的品质，例如坚韧、忠诚以及对人民的承诺。

---

## 68. ChatGPT现在在GeoGuesser表现出色

**原文标题**: ChatGPT now performs well at GeoGuesser

**原文链接**: [https://flausch.social/@piegames/114352447253793517](https://flausch.social/@piegames/114352447253793517)

据报道，新版ChatGPT在热门线上游戏GeoGuesser中表现出色，该游戏要求玩家根据全景街景图像识别地点。最初的说法“piegames：“Uhm, a new ChatGPT version just dropped and Geo…” - flausch.social”表明了对此改进的惊讶和兴奋。

（注：使用 Mastodon 网页版应用需要启用 JavaScript。你也可以选择适用于你的平台的 Mastodon 应用。这段文字与主题无关。）

因此，重点是新版ChatGPT在GeoGuesser游戏中的能力有所提升，这引起了在线社区的关注。

---

## 69. Zoom服务中断是因意外“关闭”zoom.us域名导致。

**原文标题**: Zoom outage caused by accidental 'shutting down' of the zoom.us domain

**原文链接**: [https://status.zoom.us/incidents/pw9r9vnq5rvk](https://status.zoom.us/incidents/pw9r9vnq5rvk)

2025年4月16日，Zoom因zoom.us域名不可用，导致美国及国际用户受到服务中断影响。根本原因是Zoom的域名注册商Markmonitor与GoDaddy Registry之间的通讯错误，导致GoDaddy Registry错误地通过服务器阻止关闭了zoom.us域名。这与Zoom本身的产品、安全、网络故障或DDoS攻击无关。

虽然已经在会议中或正在进行Zoom电话通话的用户未受影响，但任何试图开始、加入或安排会议的人都因DNS查找失败而遇到问题。

Zoom、Markmonitor和GoDaddy合作移除了服务器阻止，恢复了对zoom.us域名的访问。但是，由于DNS缓存，修复程序需要额外的时间才能在互联网上传播。

为了防止未来再次发生，Zoom与GoDaddy Registry和Markmonitor合作实施了技术变更和流程，包括注册表锁定，限制对zoom.us域名的服务器阻止命令。Zoom建议仍然遇到连接问题的用户刷新其DNS缓存。所有服务已于太平洋时间下午1:12完全恢复。

---

## 70. 在Namecheap使用CAA记录

**原文标题**: Using CAA Records with Namecheap

**原文链接**: [https://blog.aaronmdjones.net/using-caa-records-with-namecheap](https://blog.aaronmdjones.net/using-caa-records-with-namecheap)

亚伦·琼斯详述在Namecheap更新CAA记录以限制LetsEncrypt证书颁发至特定账户的受挫经历，该更新利用了RFC 8657中定义的`accounturi`和`validationmethods`参数。尽管CAA记录和参数支持是公认的标准（RFC 6844和RFC 8657），Namecheap的界面却将他有效的记录条目标记为不正确，拒绝保存。

在联系Namecheap支持后，他得到了一系列无济于事的回复：最初是对他的OpenPGP电子邮件签名的困惑，随后是反复声称他的记录值不正确，尽管琼斯引用了相关的RFC（RFC 6844、RFC 8659和RFC 8657）以及LetsEncrypt的文档。支持团队似乎不理解CAA记录的目的，并提供了过时的信息，甚至建议他创建一个已经存在的基本“issue”记录。

在多次尝试解释问题并提供正确的语法示例后，Namecheap支持最终驳回了他，建议他向“服务提供商”（可能是LetsEncrypt）寻求帮助，尽管Namecheap是DNS注册商，因此负责正确的记录实施。

琼斯将这一负面经历与一个正面经历进行了对比：他能够成功地为另一家注册商Gandi LiveDNS上的域名更新CAA记录，使用相同的语法和参数，没有任何问题，突显了Namecheap未能正确支持这些DNS标准。他得出结论，Namecheap提供的服务不合格且不完整。

---

## 71. 美国低估了制造业回流的难度。

**原文标题**: America underestimates the difficulty of bringing manufacturing back

**原文链接**: [https://www.molsonhart.com/blog/america-underestimates-the-difficulty-of-bringing-manufacturing-back](https://www.molsonhart.com/blog/america-underestimates-the-difficulty-of-bringing-manufacturing-back)

莫尔森·哈特认为，近期对进口商品征收的关税（10%-49%）不仅无法使制造业回归美国，甚至可能损害经济。他结合其在美国和中国15年的制造业经验，提出了14个理由来支持这一观点。

这些关税不足以抵消海外制造业固有的成本优势，尤其是在中国。美国的工业供应链薄弱，缺乏亚洲现成可用的必要部件。此外，美国已经失去了许多产品的制造技术，包括电子元件甚至塑料模具。

哈特强调，中国劳动力不仅更便宜，而且通常更可靠、生产效率更高。美国缺乏必要的基础设施，特别是发电和运输网络，来支持制造业的大幅增长。建设工厂和建立高效生产所需的漫长交付周期进一步使问题复杂化。

关税的不确定性、频繁的政策变化以及复杂的实施阻碍了对美国制造业的投资。此外，他认为大多数美国人对从事工厂工作不感兴趣，更喜欢体力劳动强度较低的工作。最后，根本没有足够多的失业工人具备必要的技能来填补制造业复兴将创造的就业岗位。

---

## 72. 不锈钢强化：扭转产生亚微米级“防撞墙”

**原文标题**: Stainless steel strengthened: Twisting creates submicron 'anti-crash wall'

**原文链接**: [https://techxplore.com/news/2025-04-stainless-steel-technique-submicron-anti.html](https://techxplore.com/news/2025-04-stainless-steel-technique-submicron-anti.html)

中国科研人员开发新技术显著增强不锈钢强度和抗疲劳性

《科技探索》2025年4月12日发表的一篇文章报道了中国科学院、山东大学和佐治亚理工学院的研究人员开发出的一项新技术，该技术能够显著增强不锈钢的强度并提高其抗金属疲劳性。该团队的创新方法包括重复扭转304奥氏体不锈钢，从而形成空间梯度晶胞结构，在金属内部形成亚微米级的、三维的“防撞墙”。

微观分析表明，这种超细的、小于10纳米的层状结构能够抑制位错并防止层错，而层错是金属疲劳的关键因素。“防撞墙”就像弹簧一样，可以吸收冲击力并将应力更均匀地分布在整个材料中，从而增强其抗循环蠕变（因重复弯曲而引起的疲劳）的能力。

测试表明，与未经处理的钢相比，经过处理的不锈钢的强度提高了2.6倍，并且由于棘轮效应引起的应变降低了两个到四个数量级。研究人员声称，这种改进有可能使使用该处理金属制造的产品的抗疲劳性提高多达10,000倍，从而为在航空航天等要求苛刻的应用中使用开辟了可能性。相关研究结果发表在《科学》杂志上。

---

## 73. 下半场

**原文标题**: The Second Half

**原文链接**: [https://ysymyth.github.io/The-Second-Half/](https://ysymyth.github.io/The-Second-Half/)

本文认为，人工智能正进入“下半场”，重心将从主要关注改进训练方法和模型，转向定义相关问题和改进评估。人工智能的“上半场”以Transformer、AlexNet和GPT-3等突破为特征，这些突破都专注于训练更好的模型并在基准测试中获得更高的分数。然而，作者认为，大规模语言预训练、规模化以及推理-行动的“配方”已经出现，标准化了基准测试的爬坡过程，并减少了针对特定任务的新型训练方法的需求。

这种“配方”，很大程度上由强化学习（RL）的进步所驱动，使人工智能能够解决广泛的复杂任务。现在，核心挑战是“效用问题”：人工智能擅长象棋、考试和游戏等任务，但尚未彻底改变世界，这意味着当前评估与现实世界效用之间存在脱节。

本文建议通过挑战诸如自动任务执行和独立任务解决等假设，从根本上重新思考评估设置。它强调需要让真人或用户模拟参与的评估，并考虑顺序任务解决，以更好地反映现实世界的场景。作者认为，人工智能“下半场”的进步将来自于开发衡量现实世界效用的新型评估设置，从而促使打破现有“配方”的创新方法。本文最终将人工智能的“下半场”定位为一个构建有用的产品和公司的时期，而不是对现有基准的增量改进。

---

## 74. 停机问题是NP-难的一个糟糕例子

**原文标题**: The Halting Problem is a terrible example of NP-Harder

**原文链接**: [https://buttondown.com/hillelwayne/archive/the-halting-problem-is-a-terrible-example-of-np/](https://buttondown.com/hillelwayne/archive/the-halting-problem-is-a-terrible-example-of-np/)

这篇博文批判了停机问题 (HALT) 作为标准例子的做法，它常被用来代表比 NP 完全问题 "NP-更难" 的问题。作者认为，虽然 HALT 是不可判定的，因此不在 NP 中，但常见的解释具有误导性。他们指出，NP 只需要对 "是" 实例进行多项式时间验证，而 HALT 的潜在 "是" 见证 ("它在 N 步内停止") *可以* 通过运行程序 N 步在有限时间内验证。 这种混淆的产生，是因为证明这种验证过程变成超多项式时间涉及复杂的论证，从而模糊了核心点。

作者更倾向于使用难度更接近 NP 的问题来说明复杂性差异。他们提出了一个无限网格上的令牌移动问题，该问题具有有效的位移移动和一个目标点，询问是否存在任何移动序列可以到达目标点。这个问题是 PSPACE-完全的 (可能比 NP 更难)，并且通过增加网格的维度，它迅速升级到 EXPSPACE-完全，TOWER-完全，最终达到 ACKERMANN-完全，展示了 NP 之外的一系列复杂性，同时保持可判定性和可理解性。 对于说明 NP 之外的复杂性，这种 "芝加哥" 大小的问题比 "月球" 大小的停机问题更直观。

一位读者评论质疑了令牌问题的分类，提出了一种多项式时间验证方法。 作者澄清说，移动可以被重复使用，导致解的长度随着维度的数量呈指数增长，从而证明了问题更高的复杂性。

---

## 75. UniK3D：通用相机单目3D估计

**原文标题**: UniK3D: Universal Camera Monocular 3D Estimation

**原文链接**: [https://lpiccinelli-eth.github.io/pub/unik3d/](https://lpiccinelli-eth.github.io/pub/unik3d/)

UniK3D：一种通用的单目3D估计方法，它克服了以往方法的局限性，这些方法通常依赖于对相机模型和图像校正的简化假设。这导致在具有鱼眼或全景镜头等非常规相机的真实场景中表现不佳。

UniK3D旨在成为一种通用的解决方案，能够处理*任何*相机模型，并仅从单张图像中准确估计度量3D场景。它通过球面3D表示来实现这一点，该表示更好地解耦了相机和场景几何，从而能够为无约束相机模型进行准确的3D重建。一个关键组成部分是通过学习到的球面谐波叠加实现的射线束的与模型无关的表示。引入角度损失以防止3D输出的收缩，这对于广角相机尤为重要。

该论文通过在13个不同的数据集上进行广泛的零样本评估，证明了最先进的性能，涵盖了3D、深度和相机指标。UniK3D在具有挑战性的大视野和全景设置中显示出显着改进，同时在传统的针孔相机场景中保持了最高的准确性。代码和模型可在GitHub上公开获得，Hugging Face Space提供了一个免安装的演示。该方法甚至可以逐帧应用于单目视频，无需任何后处理即可进行3D重建。

---

## 76. Bash高级Shell脚本编程 (2006) [pdf]

**原文标题**: Advanced Shell Scripting with Bash (2006) [pdf]

**原文链接**: [http://uniforumchicago.org/slides/bash1.pdf](http://uniforumchicago.org/slides/bash1.pdf)

很抱歉，我无法总结PDF文件的内容。 您提供的文本似乎是PDF的原始压缩数据，不包含可读的文本以进行总结。 它由二进制数据和PDF命令组成，而不是文章的实际内容。 要总结文章，我需要文章的实际文本，而不是PDF的内部表示。

---

## 77. 从零开始的可微编程

**原文标题**: Differentiable Programming from Scratch

**原文链接**: [https://thenumb.at/Autodiff/](https://thenumb.at/Autodiff/)

本文介绍了可微编程，强调其在机器学习之外日益增长的重要性。文章首先回顾了微分概念，包括导数、偏导数、梯度、方向导数和链式法则，并将这些概念定义为向量的变换，而不仅仅是斜率或变化率。文章还解释了以梯度下降为重点的优化方法。

随后，文章过渡到代码微分的实际方面，讨论了三种方法：

*   **数值微分：** 使用有限差分近似导数。易于实现，但对于高维输入计算成本高昂，并且只是一个近似值。
*   **符号微分：** 使用预定义的规则将函数的表示形式转换为其导数的表示形式。需要特定领域的语言，但提供精确的导数。
*   **自动微分：** 此处提及，但进一步的阐述将在文档中继续。

文章强调了这些方法之间的权衡，强调虽然数值微分很简单，但符号微分可能导致表达式大小显著增长，并且存在将在整个文档中继续描述的局限性。

---

## 78. CVE基金会

**原文标题**: CVE Foundation

**原文链接**: [https://www.thecvefoundation.org/home](https://www.thecvefoundation.org/home)

CVE基金会已成立，旨在确保通用漏洞披露（CVE）计划的长期可持续性和独立性。CVE计划是全球网络安全基础设施的重要组成部分。此前，MITRE宣布美国政府将不再续签管理该计划的合同。

过去一年，CVE委员会的部分成员一直在为这种可能性做准备，制定了一项将CVE过渡到专门的非营利性基金会的战略。CVE基金会旨在继续提供高质量的漏洞识别，并为全球防御者维护CVE数据的完整性和可用性。

成立该基金会的目的是为了解决人们对该计划依赖单一政府赞助商的担忧，并消除潜在的单点故障。它代表着国际网络安全界有机会建立反映网络威胁全球性的治理机制。

基金会将在未来几天发布更多关于其结构、过渡计划以及社区参与机会的信息。

---

## 79. HaxeUI

**原文标题**: HaxeUI

**原文链接**: [https://haxeui.org/](https://haxeui.org/)

HaxeUI是一个跨平台UI框架，旨在使开发者能够从单个代码库为桌面、Web和移动应用程序创建丰富的用户体验。它利用Haxe工具包进行交叉编译，在各种平台上实现原生性能。

HaxeUI的一个关键特性是其跨框架支持，允许与多个框架无缝集成，从而防止厂商锁定。

该框架提供了一套全面的功能，包括快速GUI开发、使用共享代码创建原生GUI、视图和控制器分离、通过CSS轻松换肤、成熟的UI组件和容器、列表和表格的数据虚拟化、通过代码或XML创建GUI、轻松集成现有项目以及自动控制器属性构建。

HaxeUI拥有一系列内置组件，包括按钮、文本字段、日历、下拉菜单、图像和容器，如手风琴、盒子、网格和选项卡视图。它还提供各种布局，如绝对布局、盒子布局、网格布局、水平布局和垂直布局。

文档包括入门指南、API参考和展示使用不同框架（OpenFL、Kha、HTML）构建的示例。该网站还鼓励通过论坛、贡献和社交媒体更新进行社区参与。

---

## 80. 4chan 沙提黑客与管理员邮件泄露

**原文标题**: 4chan Sharty Hack And Janitor Email Leak

**原文链接**: [https://knowyourmeme.com/memes/events/april-2025-4chan-sharty-hack-and-janitor-email-leak](https://knowyourmeme.com/memes/events/april-2025-4chan-sharty-hack-and-janitor-email-leak)

无法访问文章链接。

---

## 81. AGI 仍需 30 年 – Ege Erdil 和 Tamay Besiroglu

**原文标题**: AGI Is Still 30 Years Away – Ege Erdil and Tamay Besiroglu

**原文链接**: [https://www.dwarkesh.com/p/ege-tamay](https://www.dwarkesh.com/p/ege-tamay)

Mechanize联合创始人Ege Erdil和Tamay Besiroglu预测，通用人工智能（AGI）仍需约30年才能实现，估计将在2045年左右出现“即插即用的远程工作者替代品”。他们与旧金山普遍乐观的情绪形成对比，认为进步并非近期人工智能发展的简单推断。他们认为许多关键的核心能力仍需解锁。

他们批评了“智能爆炸”的概念，将其比作将工业革命称为“马力爆炸”，认为这忽略了驱动重大社会和经济变革的跨部门互补性变化。

Erdil和Besiroglu强调，虽然人工智能在计算能力不断提高方面取得了令人瞩目的进展，但进一步发展需要解锁额外的能力，如长期连贯性、自主性、完全多模态理解以及显著的额外计算规模，而这面临着能源和GPU生产等方面的限制。他们认为，目前的人工智能系统远未完全自动化远程工作，并强调了工作的复杂性以及完全自动化所需的众多能力。

---

## 82. 该死的脆弱MCP服务器

**原文标题**: Damn Vulnerable MCP Server

**原文链接**: [https://github.com/harishsg993010/damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)

漏洞百出的模型上下文协议 (DVMCP) 是一个教育项目，旨在展示模型上下文协议 (MCP) 实现中的安全漏洞。MCP 旨在标准化应用程序向大型语言模型 (LLM) 提供上下文的方式。DVMCP 提供了一个故意存在漏洞的环境，包含 10 个挑战，分为三个难度级别（简单、中等、困难），专为安全研究人员、开发人员和人工智能安全专业人员设计，以了解潜在的安全问题和缓解技术。

这些挑战涵盖了一系列漏洞，包括提示注入、工具中毒、过度权限、撤单攻击、工具阴影、间接提示注入、令牌盗窃、恶意代码执行、远程访问控制和多向量攻击。该项目的结构包括按难度组织的挑战实现、文档和解决方案指南。

该文档提供了使用 Docker 设置 DVMCP 的说明，并建议使用 Linux 环境以确保稳定性。它强调该项目仅用于教育目的，所演示的漏洞不应在生产系统中实施。DVMCP 在 MIT 许可证下获得许可，由 Harish Santhanalakshmi Ganesan 创建。它还提到了 CLINE - VSCode 扩展，作为连接到 MCP 服务器的推荐 MCP 客户端。

---

## 83. K2-18B：你可能隔着老远就能闻到那个星球的味道 – 德里克·洛

**原文标题**: K2-18B: You Can Probably Smell That Planet from Here – Derek Lowe

**原文链接**: [https://www.science.org/content/blog-post/you-can-probably-smell-planet-here](https://www.science.org/content/blog-post/you-can-probably-smell-planet-here)

无法访问文章链接。

---

## 84. Jellyfin作为Spotify的替代方案

**原文标题**: Jellyfin as a Spotify alternative

**原文链接**: [https://coppolaemilio.com/entries/i-left-spotify-what-happened-next/](https://coppolaemilio.com/entries/i-left-spotify-what-happened-next/)

艾米在一篇2025年4月17日的博客文章中，详细描述了他们用自托管方案取代Spotify的历程，最终选择了Jellyfin。艾米对Winamp、VLC，甚至定制的网页播放器等传统音乐播放器都不满意，觉得苹果的音乐App尚可接受，但受限于存储空间。

受Jeff Geerling视频的启发，艾米探索了Jellyfin，这是一款可以在本地流式传输音乐（和视频）的媒体服务器。最初，艾米在电脑上运行Jellyfin，并发现了像Finamp这样的应用程序，可以在手机上离线收听。

Jellyfin给艾米留下了深刻的印象，于是他们决定尝试自托管，购买了一台迷你电脑来运行Jellyfin以及其他应用程序，比如Immich（Google Photos的替代品）。他们鼓励读者探索自托管，强调即使对于非程序员来说也是可行的，并强调了数字自主和拥有自己数据的益处。文章最后展望了用户掌控自己数字内容的未来，而这一切都将由开源软件驱动。

评论区包括了诸如Plex、PlexAmp和Navidrome等替代方案的建议，并强烈推荐Symfonium作为客户端。

---

## 85. 构建一个观看橄榄球比赛的AI

**原文标题**: Building an AI that watches rugby

**原文链接**: [https://nickjones.tech/ai-watching-rugby/](https://nickjones.tech/ai-watching-rugby/)

本文详细介绍了一项实验，该实验旨在构建一个人工智能系统，通过观看橄榄球比赛，生成比基本事件流更丰富的数据和背景信息。目标是深入了解比赛背后的“原因”，捕捉裁判的解释、争球优势和其他细微时刻等细节。

该原型涉及从视频片段中提取信息。首先，作者尝试使用OpenAI的视觉模型从屏幕截图中识别比分和比赛时钟。为了降低API成本，他们专注于裁剪图像，使其仅包含记分牌区域。他们还探索了图像差异和OCR（Tesseract）等替代方案，但发现LLM方法最可靠。

此外，作者使用OpenAI的Whisper转录广播中的音频，捕捉评论和裁判音频，以添加更多背景信息。这将使人工智能能够突出传统统计数据中未反映的关键时刻，例如一名前锋令人印象深刻的表现或错失的罚球。

作者承认这只是一个原型，并概述了扩展系统的未来挑战，包括处理直播流、不同广播公司和语言的基础设施考虑。还提出了关于自动化新闻的伦理考虑。作者认为，人工智能有潜力通过以更少的资源做更多的事情，来释放更好的见解，并在体育领域讲述更丰富的故事。

---

## 86. BitNet b1.58 2B4T 技术报告

**原文标题**: BitNet b1.58 2B4T Technical Report

**原文链接**: [https://arxiv.org/abs/2504.12285](https://arxiv.org/abs/2504.12285)

本技术报告介绍BitNet b1.58 2B4T，一种新型开源的1比特大型语言模型(LLM)，拥有20亿参数。该模型在包含4万亿tokens的大规模语料库上进行训练，其性能已在包括语言理解、数学推理、编码和对话能力在内的各种基准测试中得到全面评估。作者证明，BitNet b1.58 2B4T 实现了与同等规模的、最先进的、开源、全精度LLM相当的性能。

BitNet b1.58 2B4T的一个关键优势是其显著增强的计算效率。与传统的LLM相比，它拥有更小的内存占用、更低的能耗和更短的解码延迟。

为了促进进一步的研究和推广应用，作者将在Hugging Face上发布模型权重，以及与GPU和CPU架构兼容的开源推理实现。该论文是一个在研项目，于2025年4月16日提交至arXiv，并被归类于计算与语言(cs.CL)和机器学习(cs.LG)。该论文还包含指向文献工具、代码、数据和相关论文的链接，以鼓励进一步的调查研究。

---

## 87. OpenAI 曾考虑收购 Cursor 的开发者，之后转向了 Windsurf。

**原文标题**: OpenAI looked at buying Cursor creator before turning to Windsurf

**原文链接**: [https://www.cnbc.com/2025/04/17/openai-looked-at-cursor-before-considering-deal-with-rival-windsurf.html](https://www.cnbc.com/2025/04/17/openai-looked-at-cursor-before-considering-deal-with-rival-windsurf.html)

OpenAI曾考虑收购AI编码工具Cursor开发商Anysphere，之后洽谈以约30亿美元收购Windsurf。去年和今年，随着Cursor越来越受欢迎，OpenAI与Anysphere进行了多次讨论，但最终未能达成协议。据报道，Anysphere当时寻求的估值接近100亿美元。

Cursor通过利用Anthropic的Claude 3.5 Sonnet等模型进行编码辅助而获得了关注，甚至受到一些人比微软GitHub Copilot更青睐。OpenAI联合创始人Andrej Karpathy称Cursor为“氛围编码”工具。

本文突显了对AI编码工具日益增长的投资，以及科技公司将AI集成到软件开发中的竞争。OpenAI正在发布一款新产品Codex CLI，以方便使用其新的o3和o4-mini推理模型进行编码。Anysphere证实这些模型已在Cursor中可用。AI编码领域涌现了Bolt、Replit和Vercel等公司。据报道，OpenAI与该领域的20多家公司进行了会面。

---

## 88. 创业练习：什么不能用钱解决？ (2011)

**原文标题**: Startup Exercise: What can't be solved with money? (2011)

**原文链接**: [https://longform.asmartbear.com/startup-money/](https://longform.asmartbear.com/startup-money/)

Jason Cohen 2011年文章《创业练习：什么问题是钱解决不了的？》探讨了商业领域中，金钱能够解决的问题与那些需要内在技能、知识和流程的问题之间的关键区别。其核心论点是，金钱可以加速执行，但不能凭空创造探索、理解或内在能力。

文章强调，投资者主要对投资那些金钱能够直接解决现有问题的企业感兴趣。例如，金钱可以资助营销活动、雇佣员工（一旦找到）、建立QA团队或提供更长的跑道以应对经济衰退。

然而，金钱买不到：组建一支优秀的团队、在营销和社交媒体方面获得权威、确定要编写什么代码、知道如何转化潜在客户、确定最佳网站文本、发展从错误中学习的理念，或者知道什么时候bug在发布前不重要到可以不修复。这些需要技能、经验和洞察力。

作者强调了展示学习、适应和改进能力的重要性，而不是简单地声明自己具有适应性或拥抱精益创业原则。这包括展示整合客户反馈、数据驱动决策和成功转型等实际例子。

文章最后敦促创业公司专注于掌握金钱买不到的东西，因为这些是最有价值的资产，尤其是在资源有限的情况下。对于那些融资的人来说，关键是强调资金将如何解决特定的、已识别的差距，并展示在金钱无法解决的领域中的现有能力。不鼓励在没有核心团队或没有明确的金钱无法解决问题计划的情况下筹集资金。

---

## 89. 谷歌人...前谷歌人

**原文标题**: Googler... ex-Googler

**原文链接**: [https://nerdy.dev/ex-googler](https://nerdy.dev/ex-googler)

作者（曾用邮箱 argyle@google.com）宣布因职位被裁，意外地从 Google 离职。他们表达了震惊、悲伤、愤怒和难以置信，尤其考虑到时间和环境。作者被告知裁员并非基于绩效，并且他们有可能在公司内部找到另一个职位。然而，他们立即且完全地被剥夺了对 Google 系统和资源的访问权限，这与上述说法相矛盾，让他们感觉像个罪犯。

作者强调了最近在 Chrome 团队建设活动中充满创意合作的美好体验与突然被解雇之间的强烈反差。他们强调了自己积极参与的许多职责和项目，包括 Google I/O 视频、Google I/O 舞台亮相、运营展位、为开发者主题演讲做出贡献、参与 CSS 工作组、举办开发者开放时间以及为 Google 的 CSS 工作做出贡献。所有这些计划现在都被取消了。

作者感叹失去了辛辛苦苦建立的关系以及在大公司中感到自己可有可无的感觉。他们表达了背叛、缺乏感激、羞耻和愤怒之情，并描述了睡眠困难。他们提供了联系方式，供那些希望联系他们的人使用，并承认情况的复杂性以及可能出现的回复延迟。

---

## 90. PostgreSQL中内存大小很重要

**原文标题**: Memory Size Matters to PostgreSQL

**原文链接**: [https://pgdba.org/post/2025/04/size_matter/](https://pgdba.org/post/2025/04/size_matter/)

本文探讨了为获得最佳性能，在PostgreSQL中适当调整`shared_buffers`参数的重要性。虽然充足的RAM可以显著提升性能，但两者之间的关系并非简单直接。

共享缓冲区管理着数据区和后端之间的数据流动。PostgreSQL使用时钟扫描算法来管理缓冲区替换，当可用缓冲区的“空闲列表”为空时，它会以循环方式搜索要驱逐的缓冲区。

更大的`shared_buffers`大小并非总是更好。如果数据区完全适应共享缓冲区，则空闲列表就足够了，性能表现优秀。然而，如果数据区更大，则时钟扫描机制就会发挥作用，导致性能下降。对大型共享缓冲区（例如100GB）进行完整扫描以查找可驱逐的缓冲区可能需要几秒钟，从而对性能产生负面影响。

像`VACUUM`或大型顺序扫描这样的批量操作使用一个小的环形缓冲区，限制了它们对共享缓冲区的影响。

本文建议，对于具有4GB到100GB RAM的系统，`shared_buffers`的起始值设置为系统RAM的25%是合适的。但是，对于具有更大RAM（例如400GB）的系统，由于时钟扫描算法中扫描时间的增加，`shared_buffers`的值超过64GB可能会导致性能下降。因此，了解数据区大小和缓冲区管理对于正确调整`shared_buffers`至关重要。应始终调整128MB的默认值。

---

## 91. 我们所知的Sierra之终结，第二部分：丑闻

**原文标题**: The End of Sierra as We Knew It, Part 2: The Scandal

**原文链接**: [https://www.filfre.net/2025/04/the-end-of-sierra-as-we-knew-it-part-2-the-scandal/](https://www.filfre.net/2025/04/the-end-of-sierra-as-we-knew-it-part-2-the-scandal/)

本文详细描述了雪乐山在线被CUC收购后的动荡时期，重点关注《国王密使：永恒的假面》的开发以及随之而来的、最终吞噬CUC继任者Cendant的财务丑闻。

罗伯塔·威廉姆斯努力使《国王密使》适应不断变化的电子游戏环境，目标是打造一款受《暗黑破坏神》启发的实时3D体验。然而，技术限制和创意控制权的丧失阻碍了该项目。与此同时，肯·威廉姆斯的离职和公司收购导致罗伯塔的影响力和创作自由下降。

与此同时，CUC和HFS合并成立Cendant从一开始就问题重重。HFS的首席执行官亨利·西尔弗曼在获取财务信息时遇到了来自原CUC的沃尔特·福布斯的阻力。西尔弗曼的疑虑日益加深，最终发现了CUC内部存在的大规模会计欺诈。

一项秘密审计显示，CUC在三年内虚报了超过5亿美元的收入。当被质问时，福布斯和他的团队最初淡化了这种差异，并试图掩盖它。西尔弗曼给福布斯下了最后通牒，要求他完全披露欺诈行为并辞职。本文结束于公开披露欺诈行为的前夕，并且是更大系列的一部分，该系列的第一部分重点关注肯·威廉姆斯离开雪乐山。

---

## 92. 为什么以前的电脑更有趣：坦诚且精英主义的思考

**原文标题**: Honest and Elitist Thoughts on Why Computers Were More Fun Before

**原文链接**: [https://www.datagubbe.se/aficion/](https://www.datagubbe.se/aficion/)

本文认为，过去的电脑更有趣，不仅仅是因为硬件更简单且无需联网，而是因为它们并非人人都能拥有。作者回忆了 1990 年代左右，电脑昂贵且使用起来需要付出相当大的努力。这就像一个“守门人”，只吸引那些真正充满热情的人，淘汰那些只是随便好奇的人。这创造了一个由知识渊博的用户组成的社区，他们拥有共同的极客野心，促进了创造性的软件开发，并被允许独自探索他们的机器。

作者将此与 1990 年代中期以后进行对比，那时电脑变得更便宜，随着 Windows 95 的出现，使用起来更容易，并且对工作和日常生活至关重要。这种休闲用户的涌入导致了计算的“简化”。苹果和微软优先考虑用户友好性而不是用户赋权，隐藏了复杂的配置选项，以避免技术不熟练的用户犯错。

作者感叹，向消费主义便利性和企业控制的转变已经取代了业余爱好者的集体。极客们的内置守门机制现在已经消失了。作者并不责怪休闲用户，承认他们通常是被迫使用电脑的。相反，他们认为复古计算的流行源于一种想要重现那个年代的渴望，那时电脑是极客的试金石，是共享爱好的标志，也是与志同道合者联系的源泉。

---

## 93. 洗碗机使用者分两种。

**原文标题**: There are two types of dishwasher people

**原文链接**: [https://www.theatlantic.com/family/archive/2025/04/how-to-load-dishwasher/682425/](https://www.theatlantic.com/family/archive/2025/04/how-to-load-dishwasher/682425/)

艾伦·库欣的文章探讨了洗碗机装载这个出人意料地充满争议的话题，揭示它是人际关系中常见的争论来源，并反映了更深层次的价值观。她首先承认自己不擅长装洗碗机，并强调了网上关于“正确”装载方式的大量建议和争论。

文章揭示了洗碗机装载方式上的“斯堪的纳维亚建筑师”和“吸了冰毒的浣熊”之间的文化差异。YouGov的一项民意调查显示，三分之一的受访者在洗碗机最佳实践方面与他人存在分歧。这些分歧不仅限于效率，还触及了关于清洁、责任和家庭角色的理念。

库欣随后深入探讨了清洁专家提供的关于洗碗机装载的实用建议。关键点包括了解喷淋臂的力学原理、避免超载、将较结实的物品放在下层架子上，以及最令人惊讶的是，由于酶清洁剂的功能，尽量减少预洗。

文章进一步说明了洗碗机的重要性，强调了它在节省劳力和水方面的作用。作者最后强调，要用心参与家务，并认识到维持家庭所需的帮助。她认为，正确装载洗碗机是家庭中良好“公民意识”的体现。

---

## 94. 一场被遗忘的战役如何缔造了更和平的世界

**原文标题**: How a Forgotten Battle Created a More Peaceful World

**原文链接**: [https://worldhistory.substack.com/p/how-a-forgotten-battle-created-a](https://worldhistory.substack.com/p/how-a-forgotten-battle-created-a)

无法访问文章链接。

---

## 95. 使用哈希函数的程序纹理

**原文标题**: Procedural Textures with Hash Functions

**原文链接**: [https://douglasorr.github.io/2025-04-hash-textures/article.html](https://douglasorr.github.io/2025-04-hash-textures/article.html)

本文探讨了使用简单哈希函数 $(c_x \, x + c_y \, y + c_{xy} \, x \, y + c_{x^2} \, x^2 + c_{y^2} \, y^2)$ $\mathrm{mod} \, m < \tau \, m$ 创建程序纹理的方法。作者最初需要为一款2位调色板游戏制作纹理，并惊讶地发现使用此函数可以实现令人意想不到的丰富性和多样性。

本文分解了这个函数，解释了每个项的作用。例如，仅使用 `x` 会产生垂直条纹，而 `x²` 由于模运算会创建每 m/2 像素重复一次而不是 m 像素重复一次的图案。 添加 `y²` 会由于圆形等哈希线而引入圆形图案。`x*y` 项会创建有趣的螺旋图案。

通过调整系数（c 值）、模数 (m) 和阈值 (τ)，可以生成大量的纹理。作者提供了示例，并鼓励读者使用“哈希游乐场”工具进行实验。 阈值 (τ) 被强调在扫动时可用于爆炸等效果。

文章最后展示了生成的纹理示例，并鼓励读者进行实验和应用该技术，可能用于游戏开发或 3D 打印。 它强调了从如此简单的方程式中可以产生的令人惊讶的复杂性和视觉吸引力。

---

## 96. 加拿大国家电视塔幕后花絮 (2014)

**原文标题**: CN Tower, Behind the Scenes (2014)

**原文链接**: [https://site.roadwolf.ca/categories/ue/cntower/](https://site.roadwolf.ca/categories/ue/cntower/)

Roadwolf 2014年撰写的这篇文章，带你幕后探秘加拿大国家电视塔（CN Tower），重点介绍其中安装的无线电广播设备。Roadwolf曾是一名无线电台工程师，他分享了在塔内工作期间拍摄的照片和描述。

文章涵盖多个方面，首先介绍了加拿大国家电视塔的安保办公室和出入口，包括与罗杰斯中心（原天空巨蛋）共用的地下卸货区。文章描述的一个关键要素是Sinclair腔体调谐器，它用于将多个VHF和UHF商业电台的信号组合成一个单一的天线系统，VE3TWR业余无线电中继器也使用了该系统。

文章展示了CKFM、CHUM FM和CHFI等多个电台的新旧发射机技术。它将较旧的电子管发射机（Continental和Collins）与较新的模块化Nautel固态发射机进行了对比，突出了现代设备提供的易于维护和热插拔功能。

文章详细描述了马可尼加拿大国家电视塔合路器，它将多个FM电台的信号组合成一个单一的天线系统，包括功率输出和规格。最后，作者展示了5层“外部”区域的一瞥，这是一个被金属板条围起来的空间，也是边缘漫步的场所，提供了对塔楼这一部分的罕见视角。

---

## 97. 超快光探测器

**原文标题**: Ultrafast Optical Detector

**原文链接**: [https://www.tdk.com/en/about_tdk/innovation/spin-photo-detector/index.html](https://www.tdk.com/en/about_tdk/innovation/spin-photo-detector/index.html)

TDK发布全球首款“自旋光电探测器”，该突破性设备利用磁隧道结（MTJ）元件进行光检测，取代了传统的半导体探测器。这项创新有望显著提高数据传输和处理速度，尤其适用于人工智能应用，同时降低功耗。

自旋光电探测器的主要优势包括：

*   **超快光检测：** 该技术可实现极快速的光检测。
*   **宽波长范围：** 它的工作范围涵盖从近红外到可见光的广阔光谱。
*   **多功能集成：** 该探测器可以集成到各种板卡和设备上。

TDK设想自旋光电探测器可应用于数据中心、生成式AI的光通信和互连以及AR/VR技术等领域。该公司的媒体新闻稿强调，其有望实现10倍的数据传输速度提升，标志着下一代人工智能系统向前迈出了重要一步。TDK通过专题报道文章提供更多信息，并鼓励有兴趣者联系其专家以获取更多详情。

---

## 98. 雅典娜 - 一款开源、可用于生产环境的通用人工智能代理

**原文标题**: Athena – An open source production-ready general AI agent

**原文链接**: [https://github.com/Athena-AI-Lab/athena-core](https://github.com/Athena-AI-Lab/athena-core)

雅典娜：开源、生产就绪的通用人工智能代理，旨在思考和执行任务。它旨在弥合想法和结果之间的差距，能够执行从网络抓取、数据分析到代码执行和文档翻译等任务。示例包括总结GitHub存储库、分析Hacker News讨论、跟踪航班价格，甚至训练机器学习模型。

主要功能包括通过命令行进行计算机控制、文件系统访问、Python代码执行、网页浏览器自动化、网络搜索、时间感知、聊天机器人功能和短期记忆。

快速入门指南提供了关于克隆存储库、安装依赖项、配置API密钥（特别是对于OpenAI）和启动雅典娜的说明。该项目强调现代文档编写方法，建议用户利用人工智能来理解代码库。

路线图侧重于通过实现自主代码编写、改进浏览器自动化、增强上下文管理、使用RAG实现长期记忆、扩展图像和视频模型支持以及开发视频理解能力来实现人类水平的智能。

该项目鼓励通过GitHub问题、代码贡献（通过fork和pull request）、测试、文档编写以及在Discord和X上的社区参与来贡献力量。雅典娜采用BSD 3-Clause License许可。

---

## 99. eInk模式：让网页更易阅读

**原文标题**: eInk Mode: Making web pages easier to read

**原文链接**: [https://jackscogito.blogspot.com/2025/04/e-ink-mode-making-web-pages-easier-to.html](https://jackscogito.blogspot.com/2025/04/e-ink-mode-making-web-pages-easier-to.html)

本文介绍“墨水屏模式”，这是一种专为配备电子墨水（E Ink）显示屏的设备（如电子阅读器、平板电脑和显示器）设计的网页浏览模式。墨水屏模式旨在通过以分页、简化的方式呈现网页内容，将网页浏览转变为类似于阅读实体书的阅读体验。

主要功能包括：

*   **墨水屏图标及激活：** 支持墨水屏模式的网站会显示一个图标，用户可以点击或滑动以激活该模式。
*   **分页浏览：** 内容一次显示一页，通过点击屏幕左侧或右侧进行导航。
*   **手势和键盘支持：** 提供各种触摸手势（向上/向下滑动到页面顶部/底部）和键盘快捷键（方向键用于导航），以实现高效使用。
*   **防止意外点击：** 超链接和图片最初不可点击，以防止意外导航。长按允许访问浏览器的菜单，以获得在新标签页中打开等选项。
*   **文本大小调整：** 双指捏合手势（或 Cmd/Ctrl + 和 -）可以轻松调整文本大小，而不会截断文本。
*   **目录导航：** 滑动手势或键盘快捷键（Ctrl/Alt + c）可快速访问文章的目录。
*   **高亮批注：** 用户可以使用滑动手势或键盘快捷键（Ctrl/Alt + 1-3）使用不同颜色（红色、绿色、蓝色）高亮显示文本。还提供橡皮擦。
*   **悬浮操作按钮：** 提供对高亮工具和笔记本功能的访问，尤其适用于小屏幕。
*   **高亮笔记：** 收集高亮显示的内容，包括图像和视频，并按颜色进行整理。此笔记本可以保存为 PDF，并带有指向原始网页的链接。
*   **跨页高亮：** 允许高亮显示跨越多页的段落。

墨水屏模式致力于在电子墨水设备上提供清晰、无干扰的阅读体验，针对可读性和高效导航进行了优化。

---

## 100. 自己建ISP而不交康卡斯特费用的男子将其业务扩展到数百户家庭 (2022)

**原文标题**: Man who built ISP instead of paying Comcast expands to hundreds of homes (2022)

**原文链接**: [https://arstechnica.com/tech-policy/2022/08/man-who-built-isp-instead-of-paying-comcast-50k-expands-to-hundreds-of-homes/](https://arstechnica.com/tech-policy/2022/08/man-who-built-isp-instead-of-paying-comcast-50k-expands-to-hundreds-of-homes/)

密歇根州居民Jared Mauch因不满AT&T和Comcast的服务质量，自建光纤到户ISP“Washtenaw Fiber Properties LLC”。如今，得益于260万美元的政府资助，他的业务正在大幅扩张。最初只服务于约30户农村家庭的网络，现在覆盖了约70户客户，并将扩展到近600处房产。

Mauch通过Washtenaw县的竞标程序获得了资金，该县将美国救援计划资金用于宽带基础设施建设。他将额外铺设38英里的光纤，连接各个乡镇的417个地址，但他的线路将经过近600个潜在客户。

Mauch提供100Mbps对称互联网，每月收费55美元，1Gbps每月收费79美元，账单透明，无隐藏费用。他还参与了联邦通信委员会的经济适用连接计划。他的目标是在2022年底完成项目的一半，在2023年底完成另一半，远远早于合同规定的2026年截止日期。

此前，Comcast报价5万美元才肯将服务扩展到他家，而AT&T只提供1.5Mbps的DSL。尽管设备成本不断上涨，Mauch仍投资于他的基础设施，甚至获得了私人资金用于扩张。他的ISP为当地教堂提供免费互联网，并为蜂窝塔提供回程服务。他现在是当地名人，被称为“光纤电缆人”，虽然仍在Akamai担任网络架构师，但他的ISP正在对社区的连接产生重大影响。

---

