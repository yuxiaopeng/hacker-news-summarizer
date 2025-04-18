# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-04-18.md)

*最后自动更新时间: 2025-04-18 17:47:43*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 2 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 3 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 4 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 5 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 6 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 7 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 8 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 9 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 10 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 11 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 12 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 13 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 14 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 15 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 16 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 17 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 18 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 19 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 20 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 21 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 22 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 23 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 24 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 25 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 26 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 27 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 28 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 29 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 30 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
