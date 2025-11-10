# Hacker News 热门文章摘要 (2025-11-10)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Asus Ascent GX10

**原文标题**: Asus Ascent GX10

**原文链接**: [https://www.asus.com/networking-iot-servers/desktop-ai-supercomputer/ultra-small-ai-supercomputers/asus-ascent-gx10/](https://www.asus.com/networking-iot-servers/desktop-ai-supercomputer/ultra-small-ai-supercomputers/asus-ascent-gx10/)

生成摘要时出错

---

## 2. 微服务？不，模块化才是关键。

**原文标题**: Microservices? No, modularity is what matters

**原文链接**: [https://binaryigor.com/modular-monolith-and-microservices-modularity-is-what-truly-matters.html](https://binaryigor.com/modular-monolith-and-microservices-modularity-is-what-truly-matters.html)

本文倡导在软件设计中优先考虑模块化，无论选择单体架构还是微服务架构。模块化被定义为将系统划分为具有清晰API的独立、逻辑模块，它带来了诸如改进组织、理解、资源利用、可重用性和可测试性等好处。

作者使用“奇闻轶事笔记”系统为例，将其拆分为“用户”、“名言”和“笔记”模块来阐述这一概念。关键是首先解决领域理解和功能需求，然后考虑影响实现的非功能性因素。

本文还承认现实世界软件开发中知识不完整的挑战。它建议在高不确定性的情况下采用模块化单体策略，因为与微服务相比，在需求不稳定的情况下，它可以实现更低成本的重新设计。

最后，作者探讨了实际的实施策略，从最简单的开始：将模块组织为具有明确通信约定的文件夹（例如，用于共享接口的“_contracts”文件夹）。一种更严格的方法是使用独立版本控制和可部署的模块，即使只有一个部署单元，也能提供更大的隔离和透明的依赖关系。文章强调，最佳选择取决于具体的上下文、团队纪律以及对领域的确定性。

---

## 3. 启动 HN：Hypercubic (YC F25) – 面向 COBOL 和大型机的 AI

**原文标题**: Launch HN: Hypercubic (YC F25) – AI for COBOL and Mainframes

**原文链接**: [https://www.hypercubic.ai/](https://www.hypercubic.ai/)

Hypercubic：利用人工智能理解并保存复杂大型机系统和COBOL代码中的知识，解决资深开发者退休导致专业知识流失的关键问题。其核心产品为HyperTwin和HyperDocs。HyperTwin通过创建主题专家数字孪生，记录调试过程和操作流程，实现全天候访问，从而捕获机构知识。HyperDocs自动从大型机操作和COBOL代码库中创建结构化文档，提取系统知识并使其与代码库同步。

Hypercubic的混合方法结合了确定性人工智能和生成式人工智能，确保准确性、可审计性和可信度，从而降低与人工智能幻觉相关的风险。这有助于实现无与伦比的风险缓解，防止系统故障和停机，同时通过生产就绪的知识资产加速实现价值。该解决方案可与COBOL和JCL等传统语言互操作。

Hypercubic致力于解决金融服务、零售、航空航天、能源、政府和制造业等行业的知识保留难题。他们帮助这些行业确保核心系统、供应链、工程智慧、电网控制、公共服务和制造流程的关键知识。该平台提供全面的AI驱动现代化，通过捕获数十年的机构知识来降低风险。Hypercubic现提供平台早期访问权限。

---

## 4. Zig (及其设计选择)

**原文标题**: Zig (and the Design Choices Within)

**原文链接**: [https://blueberrywren.dev/blog/on-zig/](https://blueberrywren.dev/blog/on-zig/)

This article is a critical opinion piece on the Zig programming language, focusing on its design choices and their implications. The author, with significant experience in programming language design, expresses concerns about several aspects of Zig.

Chief among these is Zig's lack of memory safety, deemed a significant flaw in a modern language. The author presents data suggesting a higher incidence of crashes in Zig projects compared to projects in memory-safe languages like Rust and even those using JavaScript runtimes like Deno.

The article criticizes Zig's comptime generics for lacking standardization and potentially hindering readability. The verbosity of casting and the unpredictable behavior of float-to-int conversions are also highlighted. Issues with Result Location Semantics (RLS), particularly unexpected behavior when assigning struct members, are explored. The removal of Pointer Reference Optimization (PRO) is viewed as a missed opportunity.

The author acknowledges the ongoing efforts to improve the Zig compiler's speed and tooling but finds the current build system confusing and the unofficial language server (ZLS) subpar. The absence of use-after-realloc detection is a significant concern.

The author also points out the language design choices around undefined behavior, the prohibition of tabs in comments and strings, the limited iteration methods, and the absence of warnings (everything is an error). Finally, they address negative experiences within the Zig community, characterized by unhelpful advice and resistance to alternative approaches.


---

## 5. ClickHouse收购LibreChat：开源Agentic数据栈

**原文标题**: ClickHouse acquires LibreChat: The open-source Agentic Data Stack

**原文链接**: [https://clickhouse.com/blog/librechat-open-source-agentic-data-stack](https://clickhouse.com/blog/librechat-open-source-agentic-data-stack)

生成摘要时出错

---

## 6. 使用iCE40 FPGA实现的有趣的SPI路由

**原文标题**: Interesting SPI Routing with iCE40 FPGAs

**原文链接**: [https://danielmangum.com/posts/spi-routing-ice40-fpga/](https://danielmangum.com/posts/spi-routing-ice40-fpga/)

This article explores the interesting SPI routing design in the Fomu FPGA development board, which uses a Lattice Semiconductor iCE40 UltraPlus 5K FPGA. Unlike many FPGA boards that use a USB-to-Serial IC for configuration, the Fomu implements its USB core in RTL (using ValentyUSB), presenting a challenge for initial configuration.

The iCE40 can be configured via SRAM or non-volatile configuration memory (NVCM), or through an external SPI flash chip (GD25Q16CEIGR) for persistent storage, which is the approach used in the Fomu. The article highlights the challenge of having both the FPGA and flash IC accessible via SPI test points, given that the iCE40 can act as both an SPI controller (when booting from flash) and a peripheral (when being directly programmed).

The author investigates how the Fomu handles this dual functionality, noting that it cleverly uses the GD25Q16CEIGR flash IC's "Deep Power-Down" mode (activated by SPI commands 0xb9 and 0xab), rather than asserting the HOLD pin, to isolate the flash IC from SPI traffic when directly programming the iCE40. This is a contrast to other boards like the iCEstick, which explicitly prevents direct iCE40 programming. The Deep Power-Down method reduces the number of required test points, requiring only seven. The author concludes by highlighting how the unique capabilities of FPGAs can lead to innovative board design decisions.


---

## 7. 意想不到的人形之物

**原文标题**: Unexpected Things that are People

**原文链接**: [https://bengoldhaber.substack.com/p/unexpected-things-that-are-people](https://bengoldhaber.substack.com/p/unexpected-things-that-are-people)

无法访问文章链接。

---

## 8. 姿态动画器 – 一款开源的SVG角色动画工具 (2020)

**原文标题**: Pose Animator – An open source tool to bring SVG characters to life (2020)

**原文链接**: [https://blog.tensorflow.org/2020/05/pose-animator-open-source-tool-to-bring-svg-characters-to-life.html](https://blog.tensorflow.org/2020/05/pose-animator-open-source-tool-to-bring-svg-characters-to-life.html)

本文介绍 Pose Animator，这是一个使用 TensorFlow.js 构建的开源工具，它允许用户通过使用网络摄像头的实时动作捕捉，在浏览器中让 SVG 角色栩栩如生。该工具由 Shan Huang 开发，利用 PoseNet 和 FaceMesh 模型检测人体姿势和面部表情，然后将这些动作转换为 2D 矢量插图。

Pose Animator 采用基于骨骼的动画方法，使用表面（SVG 路径）和基于 PoseNet 和 FaceMesh 关键点的分层骨骼结构来定义角色。该工具采用线性混合蒙皮（LBS）根据骨骼运动变形 SVG 路径，从而提供细致而富有表现力的动画。

绑定过程包括解析 SVG 文件、计算骨骼对矢量段的影响、基于 ML 模型输出实时更新骨骼位置，以及最终计算新的矢量段位置。运动稳定技术，包括基于置信度分数的插值和裁剪，用于减少抖动并提高动画的流畅度。

本文还讨论了未来的改进方向，例如增强的网格绑定算法、浏览器内编辑功能（如蒙皮权重绘制）以及对栅格图像的支持。用户可以使用现有的角色尝试 Pose Animator，或者上传他们自己的 SVG 设计，并鼓励使用 #PoseAnimator 标签分享他们的创作。源代码可在 GitHub 上找到。

---

## 9. 警察可以获取你的私人在线数据

**原文标题**: Cops Can Get Your Private Online Data

**原文链接**: [https://www.eff.org/deeplinks/2025/06/how-cops-can-get-your-private-online-data](https://www.eff.org/deeplinks/2025/06/how-cops-can-get-your-private-online-data)

生成摘要时出错

---

## 10. 开始去应用化

**原文标题**: Time to Start De-Appling

**原文链接**: [https://heatherburns.tech/2025/11/10/time-to-start-de-appling/](https://heatherburns.tech/2025/11/10/time-to-start-de-appling/)

希瑟·伯恩斯的文章讨论了英国政府通过技术能力通知（TCN）要求访问苹果iCloud数据的事件，尤其影响了苹果的端到端加密功能——高级数据保护（ADP）。

由于《调查权力法案》，苹果正在从英国撤回ADP，要求启用ADP的用户手动禁用该功能才能保留其iCloud帐户。英国新用户将无法启用ADP。这意味着10个iCloud数据类别（iCloud备份、iCloud Drive、照片、备忘录、提醒事项、Safari书签、Siri捷径、语音备忘录、钱包凭证和Freeform）将不再在英国享受端到端加密的保护。

作者建议英国用户将这些数据从iCloud迁移到安全的端到端加密服务，并推荐Proton、Standard Notes、Obsidian或Joplin作为替代方案。她强调在迁移后需要清除iCloud上的数据。

文章强调，第一份TCN不仅限于ADP数据，而是寻求访问全球所有iCloud数据，这引发了对信任苹果产品堆栈存储敏感信息（包括密码）的担忧。第二份TCN专门针对英国公民的数据，引发了关于苹果将如何实施国籍检查的问题。

作者鼓励读者，特别是那些在英国以外的读者，如果可用的话，激活ADP。她敦促大家进行“去谷歌化”、“去苹果化”和“去美国堆栈化”，以提高安全性。她强调了主流媒体缺乏相关报道，以及依赖于总部设在具有不利法律的国家/地区的公司所存在的潜在危险。

---

## 11. Steven Heller's Font of the Month: Archive Matrix

**原文标题**: Steven Heller's Font of the Month: Archive Matrix

**原文链接**: [https://ilovetypography.com/2025/11/07/steven-hellers-font-of-the-month-archive-matrix/](https://ilovetypography.com/2025/11/07/steven-hellers-font-of-the-month-archive-matrix/)

Unable to access the article link.


---

## 12. 游戏保存很难，有时需要私家侦探

**原文标题**: Games Preservation Is Hard and Sometimes Involves Private Detectives

**原文链接**: [https://kotaku.com/gog-preservation-program-private-detectives-drm-2000635611](https://kotaku.com/gog-preservation-program-private-detectives-drm-2000635611)

生成摘要时出错

---

## 13. 甜菜：音乐发烧友的媒体管理器

**原文标题**: Beets: The music geek’s media organizer

**原文链接**: [https://beets.io/](https://beets.io/)

Beets is a powerful, extensible media library management system designed for obsessive music geeks. Its core purpose is to organize and perfect music collections by automatically cataloging and enriching metadata using the MusicBrainz database.

Beyond basic cataloging, Beets leverages a plugin-based architecture to offer a wide array of functionalities. These include fetching and calculating metadata like album art, lyrics, genres, tempos, ReplayGain levels, and acoustic fingerprints from sources like MusicBrainz, Discogs, and Beatport. It can also guess metadata from filenames or acoustic fingerprints. Furthermore, Beets can transcode audio, identify duplicate tracks or albums, and detect missing tracks. A web-based interface allows browsing and playing music within a browser.

The system is highly customizable; users can write their own plugins using Python to extend functionality to meet specific needs.

Installation is straightforward using `pip install beets`. The article encourages users to explore the "Getting Started" guide and follow the project on Fosstodon for updates. It also provides links to project resources such as the GitHub repository, documentation, FAQ, bug tracker, discussion board, and blog. Users can seek help on the discussion board or by filing an issue on GitHub. While donations are accepted, the article encourages donations to Move to Amend.


---

## 14. 安装和使用HP-UX 9

**原文标题**: Installing and using HP-UX 9

**原文链接**: [https://thejpster.org.uk/blog/blog-2025-11-08/](https://thejpster.org.uk/blog/blog-2025-11-08/)

本文详细介绍了作者在老式HP 9000 Model 340 (68K) 工作站和HP 9000 Model 705 (PA-RISC) 工作站上安装和使用HP-UX 9的经验。在获得一系列老式计算机后，作者专注于在基于68K的Model 340和基于PA-RISC的Model 705之间建立混合架构集群。

作者介绍了在Model 705上安装HP-UX 9的过程，重点介绍了磁盘兼容性和网络配置方面的挑战。文章描述了使用SAM（系统管理管理器）将Model 705配置为集群服务器的过程。

当尝试将Model 340集成到集群中时，出现了一个关键挑战。作者发现，要启用混合架构集群，必须将Series 300的HP-UX 9 *覆盖*安装在Series 700的现有安装上，这是一个不寻常的步骤。

这次经历中最有趣的部分是发现了HP-UX 9的上下文相关文件系统（CDF）。CDF允许系统根据访问它的机器的架构提供相同可执行文件（例如/bin/ls）的不同二进制版本。文章解释了CDF的工作原理，即通过创建包含特定于架构的文件的目录，使共享文件系统能够在具有不同架构的机器上正常工作。这个独特的功能虽然强大，但最终在更高版本的HP-UX中被移除。

---

## 15. Using the expand and contract pattern for schema changes

**原文标题**: Using the expand and contract pattern for schema changes

**原文链接**: [https://www.prisma.io/dataguide/types/relational/expand-and-contract-pattern](https://www.prisma.io/dataguide/types/relational/expand-and-contract-pattern)

The expand and contract pattern is a multi-step database schema migration strategy that allows for safe and reliable transitions between old and new data structures without downtime. It involves incrementally introducing the new structure in the background, preparing data for live usage, and seamlessly switching over.

The process consists of seven steps:

1.  **Build and deploy the new schema:** Create the new schema alongside the existing one, ensuring no constraints impact current client behavior.
2.  **Expand the interface:** Update client applications to write to both the old and new schemas, validating the interface and ensuring data is persisted in both.
3.  **Migrate existing data:** Transfer data from the old schema to the new one, potentially requiring data transformation to accommodate schema differences.
4.  **Test the new interface:** Validate the new schema's functionality and performance by running queries and clients in parallel.
5.  **Cut reads over to the new interface:** Modify client behavior to read from the new schema, effectively migrating production traffic.
6.  **Discontinue writing to the original structure:** Update client applications to stop writing to the old schema.
7.  **Remove the original structure:** Delete the old data structure, completing the migration.

The article illustrates the pattern with an example, migrating location data from an `equipment` table to a separate `playground` table. This involves creating the new table, updating the client to write to both, migrating existing data, switching reads to the new table, discontinuing writes to the old, and finally, removing the old columns. Feature flags are used to control read and write operations to ease the cutover.


---

## 16. 想得更怪：年度最佳科幻创意

**原文标题**: Think Weirder: The Year's Best SciFi Ideas

**原文链接**: [https://thinkweirder.com](https://thinkweirder.com)

《想得更怪：年度最佳科幻创意》是2024年出版的科幻小说选集，由编辑乔·斯特奇策划。斯特奇从391篇故事中挑选了16篇，重点关注发人深省的、近未来人类与技术之间的互动。该书旨在通过提供新颖的思考理念，提供比社交媒体更高质量的娱乐。

该选集包含各种各样的概念。故事探讨了人工智能预测的影响、幸福优化纳米机器人的潜在权衡，以及技术如何在困难的情况下提供微小但有意义的改进。其他故事深入探讨了通过技术实现的跨文化理解、人工智能在压迫社会中面临的伦理困境、对雄心勃勃的长期项目的追求、富有同情心的太空航行文化的发展，以及应用于环境复兴的技术的复杂性。这本书承诺通过引人入胜的叙事和引人入胜的想法，提供对世界的新鲜视角。

---

## 17. 重塑：基于模块化设计的可重构服装

**原文标题**: Refashion: Reconfigurable Garments via Modular Design

**原文链接**: [https://arxiv.org/abs/2510.11941](https://arxiv.org/abs/2510.11941)

“重塑：基于模块化设计的可重构服装”一文提出了一种新颖的服装设计方法，旨在解决固定尺寸和静态风格服装的局限性。作者Rebecca Lin、Michal Lukáč和Mackenzie Leake介绍了一种模块化系统，该系统能够调整尺寸、重塑风格并重复利用服装组件。

核心贡献包括：
1. 一组模块化的构建块和连接器，允许服装被组装和重新配置。
2. 一种使用整数线性规划将现有服装设计分解为模块的方法。
3. 一种促进模块化服装设计和仿真的数字设计工具。

该研究旨在创造适应身体尺寸变化和不断演变的时尚潮流的服装。用户评估表明，模块化设计方法有效地支持了多种服装风格的创作，并促进了尺寸和风格的转换，同时利用了相同的核心组件。该论文在第38届ACM用户界面软件与技术年度研讨会（UIST '25）上发表。它被归类为“人机交互（cs.HC）”，并探讨了计算在服装和设计中的应用。

---

## 18. Quad9 DNS提供商认为盗版屏蔽令是“生存威胁”

**原文标题**: DNS Provider Quad9 Sees Piracy Blocking Orders as "Existential Threat"

**原文链接**: [https://torrentfreak.com/dns-provider-quad9-sees-piracy-blocking-orders-as-existential-threat/](https://torrentfreak.com/dns-provider-quad9-sees-piracy-blocking-orders-as-existential-threat/)

本文探讨了DNS提供商Quad9如何看待法国最近的海盗行为封锁令，认为其对其运营构成“生存威胁”。在最初针对谷歌、Cloudflare和思科的封锁盗版体育流媒体网站的命令之后，权利持有人将这些请求扩大到包括像Quad9和Vercel这样的小型DNS提供商。

Quad9是一家瑞士非营利组织，它认为自己缺乏像谷歌和Cloudflare这样的大公司那样在法庭上为自己辩护的财政资源。该公司认为，版权所有者正在将执法负担转移到像ISP、VPN和DNS提供商这样的中立中介机构身上，而不是直接针对侵权者。这对缺乏无限期遵守资源的小型运营商构成了重大挑战。

思科已经离开法国，以回应封锁令。Quad9无法将封锁限制在法国，不得不将其应用于全球范围。本文强调了这些行动的更广泛影响，质疑中立的基础设施是否应该对其他人的行为负责，并引发了对跨司法管辖区法律范围的担忧。Quad9担心这些封锁战可能导致互联网变得不那么开放、不那么私密，也更加中心化，由能够负担法律费用的公司主导。文章强调了Quad9在之前与索尼在德国进行了一场代价高昂的法律战之后的困境，目前的局势提出了关于互联网治理未来和小型、使命驱动型组织生存的关键问题。

---

## 19. 多稳态薄壳超结构用于多响应超材料机器人

**原文标题**: Multistable thin-shell metastructures for multiresponsive metabots

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.adx4359](https://www.science.org/doi/10.1126/sciadv.adx4359)

Unable to access the article link.


---

## 20. Show HN: Hacker News 正在做什么？

**原文标题**: Show HN: What Is Hacker News Working On?

**原文链接**: [https://waywo.eamag.me/](https://waywo.eamag.me/)

无法访问文章链接。

---

## 21. XSLT 安息

**原文标题**: XSLT RIP

**原文链接**: [https://xslt.rip/](https://xslt.rip/)

这篇题为“XSLT RIP”的短文，本质上是对可扩展样式表转换语言（XSLT）技术假定消亡的悼念，据称它被谷歌扼杀了。该文明确指出XSLT“被谷歌扼杀了”，并表示哀悼（“愿逝者安息。”），暗示至少在作者和目标受众中，普遍认为谷歌的行为已使XSLT过时或无关紧要。信息简洁明了，侧重于XSLT的假定死亡，并表达了对该技术的失落感。

---

## 22. 欧洲将决定6 GHz频段是否由Wi-Fi和蜂窝网络共享。

**原文标题**: Europe to decide if 6 GHz is shared between Wi-Fi and cellular networks

**原文链接**: [https://www.theregister.com/2025/11/09/europe_to_decide_if_6/](https://www.theregister.com/2025/11/09/europe_to_decide_if_6/)

生成摘要时出错

---

## 23. 英国如何失去造船业

**原文标题**: How the UK lost its shipbuilding industry

**原文链接**: [https://www.construction-physics.com/p/how-the-uk-lost-its-shipbuilding](https://www.construction-physics.com/p/how-the-uk-lost-its-shipbuilding)

This article details the decline of the UK's shipbuilding industry from its global dominance in the late 19th and early 20th centuries to its virtual disappearance by the 21st century.

The UK's success was initially built on cheap coal, iron, and skilled labor. Shipyards favored labor-intensive methods over expensive infrastructure, allowing flexibility in the cyclical market and close relationships with British shipowners for custom-built vessels. Strong labor unions protected workers but resisted production changes.

The first signs of decline appeared after World War I due to increased global competition, overcapacity, and the Washington Naval Treaty, which limited naval construction. Other nations invested in their shipbuilding industries, experimenting with new techniques.

After WWII, despite an initial advantage due to war-torn competitors, the UK failed to adapt to new, US-developed, methods of shipbuilding like welding and prefabrication, which Japan embraced. These new methods were used to mass produce ships, but required significant investment and changes to labor practices, which British shipbuilders and unions resisted. A reluctance to innovate, partly fueled by conservatism and some failures of welded ships, further hampered progress. As a result, the UK's market share plummeted, leading to closures, unemployment, and ultimately, the industry's demise. The UK's focus on skilled labor over capital investment, while initially an advantage, proved to be its downfall in the face of changing technologies and global competition.


---

## 24. 科学家发现“螺旋形”材料，可增强光基计算机。

**原文标题**: Scientists Discover "Gyromorphs" Materials to Enhance Light-Based Computers

**原文链接**: [https://www.nyu.edu/about/news-publications/news/2025/november/scientists-discover-breakthrough-materials-to-enhance-light-base.html](https://www.nyu.edu/about/news-publications/news/2025/november/scientists-discover-breakthrough-materials-to-enhance-light-base.html)

科学家发现“陀螺形”材料，有望提升光子计算机性能：

纽约大学的研究人员发现了一种名为“陀螺形”（gyromorphs）的新型材料，有望显著提升光子计算机（也称光基计算机）的性能。这些材料具有独特的结构，能够以不同寻常的方式操纵光线，在速度和能源效率方面提供优于传统电子产品的潜在优势。

这项关键创新在于陀螺形材料能够创建光的“拓扑”状态，这意味着光的特性由材料的形状和结构决定，而非其特定的化学成分。这种稳健性使得它们不易受到制造过程中的缺陷和变化的影响。具体而言，这些材料表现出强大的“手性”响应，与不同偏振的光相互作用的方式不同，从而可以精确控制和操纵光信号。

研究人员证明，通过精心设计陀螺形结构，他们可以制造出能够强烈旋转光偏振或以最小损耗引导光沿复杂路径传播的材料。这种控制对于开发先进的光子器件至关重要，例如光开关、调制器和波导，这些都是光子计算机的构建基块。

该发现被认为是实现光子计算潜力的重要一步，光子计算有望克服当前电子计算机在人工智能和大规模数据处理等特定应用中的局限性。未来的研究将侧重于改进制造技术，并探索陀螺形材料可以提供的全部功能。

---

## 25. Realtime BART Arrival Display

**原文标题**: Realtime BART Arrival Display

**原文链接**: [https://filbot.com/real-time-bart-display/](https://filbot.com/real-time-bart-display/)

本文介绍了一个构建实时BART列车到达显示器的项目，该显示器模仿了老式站台标志的外观和感觉。作者使用Seeed Studio XIAO ESP32C6、BuyDisplay的红色OLED字符显示器和一个逻辑电平转换器来创建硬件。为了简化数据处理，作者创建了一个中间件服务，该服务获取并解析官方BART API的GTFS实时数据，然后为ESP32提供一个简化的API供使用。ESP32随后在OLED屏幕上显示即将到来的列车到达信息、时间和BART安全消息。该项目包括将组件焊接在万用板上、3D打印外壳并对其进行喷漆以模仿真实的BART标志。最后的润色包括添加螺丝和贴纸等细节，模仿原始站台标志。作者将完成的显示器安装在显示器上方，以便他们可以快速查看列车到达时间并享受站台显示器的怀旧感。所有代码和3D文件都可在GitHub和Makerworld上找到。

---

## 26. BGP僵尸和过度寻径

**原文标题**: BGP zombies and excessive path hunting

**原文链接**: [https://blog.cloudflare.com/going-bgp-zombie-hunting/](https://blog.cloudflare.com/going-bgp-zombie-hunting/)

生成摘要时出错

---

## 27. 邓斯特-谢弗与集合推理

**原文标题**: Dempster-shafer and reasoning about sets

**原文链接**: [https://emiruz.com/post/2025-10-30-epistemics/](https://emiruz.com/post/2025-10-30-epistemics/)

This article explores the application of Dempster-Shafer (DS) theory to model beliefs about sets, specifically binary variables, given probabilistic information about subsets. The problem involves estimating the probability of a subset satisfying a quantified logic formula, given updates that assign probabilities to subsets based on similar logical conditions.

The author argues that Bayesian methods are difficult to apply due to the non-atomic statements and lack of true conditioning statements. DS theory, which directly assigns probabilities (mass assignments) to subsets of events, offers an elegant solution. Mass assignments can overlap, and any unassigned probability is assigned to the vacuous set. Belief and plausibility are then calculated, representing lower and upper bounds on the probability.

The article demonstrates the approach using GNU SETL, a set-based language, with a concrete example where information about relationships between binary variables is provided. Dempster's rule is used to combine multiple information updates (mass assignments), and then belief and plausibility are calculated for specific queries. The results show the effectiveness of the DS approach.

Finally, a Frequentist alternative is presented, where probabilities are assigned to each variable and updated based on new information through simulation. However, the author finds this approach less elegant and potentially computationally expensive. The article concludes by highlighting the applicability of DS theory as a portable metaphor for "sensor fusion," where overlapping beliefs from multiple sources are combined.


---

## 28. 这些人在几十年前潜入了埃德蒙·菲茨杰拉德号沉船。他们的故事

**原文标题**: These Men dove to the Edmund Fitzgerald shipwreck decades ago. Their stories

**原文链接**: [https://www.freep.com/story/news/local/michigan/2025/11/02/edmund-fitzgerald-wreck-diving/86752517007/](https://www.freep.com/story/news/local/michigan/2025/11/02/edmund-fitzgerald-wreck-diving/86752517007/)

本文讲述了里克·米克斯特和特伦斯·泰索尔的故事。他们两人在1975年苏必利尔湖埃德蒙·菲茨杰拉德号沉没数十年后，探索了该沉船残骸。那次沉船事故夺去了29名船员的生命。

米克斯特是一名纪录片电影制作人，1994年他乘坐潜水器到达沉船地点，称那里既令人着迷又是一个阴森的坟墓。他的团队无意中发现了一名船员的遗体，这在遇难者家属中引发了争议。泰索尔和他的潜水伙伴是1995年仅有的两个水肺潜水到沉船地点的人。他形容这次经历既是一种荣幸又是一个激动人心的时刻，他意识到这个地方的神圣性。

米克斯特的探索旨在揭示沉船的原因。他发现了一些线索，比如扭曲的舱口盖，这挑战了之前的理论。他得出结论，很可能是巨浪导致船只断裂。遗体的发现以及随后的报道引发了批评，一些人认为这些探索是不敏感的。尽管存在争议，米克斯特和泰索尔都为他们的行为辩护，强调了理解这场悲剧和向逝者致敬的重要性。

---

## 29. 深入剖析山姆大叔拟议的TP-Link禁令

**原文标题**: Drilling down on Uncle Sam's proposed TP-Link ban

**原文链接**: [https://krebsonsecurity.com/2025/11/drilling-down-on-uncle-sams-proposed-tp-link-ban/](https://krebsonsecurity.com/2025/11/drilling-down-on-uncle-sams-proposed-tp-link-ban/)

美国政府正考虑禁止TP-Link系统的网络设备，原因是担忧该公司据称与中国政府存在关联以及潜在的安全风险。TP-Link否认这些指控，并强调其在美国的业务和在越南的生产，但该提议源于担心TP-Link设备可能被用于访问敏感的美国数据或助长网络攻击。

文章强调，TP-Link的经济性和性能使其成为消费者和ISP的热门选择。然而，众议院委员会的一项调查引发了人们对TP-Link设备漏洞及其在美国军事基地存在的担忧。安全研究人员还将TP-Link路由器与参与网络间谍活动和密码喷洒攻击的中国国家支持的黑客组织联系起来。

文章强调，许多路由器，无论品牌如何，都出厂设置不安全的默认设置和过时的固件。为了降低风险，文章提出了几个步骤：更改默认凭据，定期更新固件，并考虑像OpenWRT这样的开源固件替代方案。文章还指出，现代路由器正越来越多地强制用户使用移动应用程序来更新安全设置。最后，文章建议出于性能原因升级旧路由器，并警告不要在未经咨询的情况下修改由ISP管理的路由器。

---

## 30. 罗马道路的谷歌地图：Itiner-e

**原文标题**: Itiner-e: the Google Maps of Roman Roads

**原文链接**: [https://itiner-e.org/](https://itiner-e.org/)

Itiner-e：罗马道路的“谷歌地图”——或更准确地说，是一部致力于罗马帝国道路的数字地图集。其目标是成为关于该主题最全面且公开访问的数字数据集。该项目以协作模式运作，贡献和编辑来自学者社区。用户可以通过查看地图、查询特定道路的信息以及下载数据集以用于自己的研究或目的来与数据进行交互。该项目正在进行中，表明致力于持续改进和扩展数据。本质上，Itiner-e提供了一个以数字形式探索和利用罗马道路信息的平台。

---

## 31. Today I Learned: Binfmt_misc

**原文标题**: Today I Learned: Binfmt_misc

**原文链接**: [https://dfir.ch/posts/today_i_learned_binfmt_misc/](https://dfir.ch/posts/today_i_learned_binfmt_misc/)

本文探讨了 Linux 内核特性 `binfmt_misc`，该特性允许系统基于自定义二进制格式执行文件。它通过在 `/proc/sys/fs/binfmt_misc/` 中注册处理程序，指定如何识别文件（例如，通过魔数），以及使用哪个解释器，从而扩展了内核运行可执行文件的能力，使其超越了原生二进制文件。

作者强调 `binfmt_misc` 可能会成为攻击者利用 root 权限重新获得控制权的后门。一种名为“Shadow SUID”的技术利用了这一点，通过注册一个处理程序，使用 SUID 二进制文件（如 `chfn`）的凭据来以 root 身份运行攻击者控制的解释器。这避免了在攻击者的二进制文件上设置 SUID 位，使其更难被检测到。

文章演示了如何设置这个后门：编译一个解释器，确定一个合适的 SUID 二进制文件（例如 `chfn`），提取其魔数，并使用 `C` 标志注册一个新的处理程序。这个标志指示内核使用原始文件的 setuid 凭据运行攻击者的解释器，从而获得 root 访问权限。

检测方法包括监控 `/proc/sys/fs/binfmt_misc/` 中新建/修改的处理程序，特别是那些指向可写位置的处理程序。但是，文章指出，检测初始设置需要 root 权限，这使其具有挑战性。专家 Ruben Groenewoud 证实，传统的 SUID 搜索方法不会标记该解释器。积极的一面是，该处理程序是临时的，并在重启后消失，迫使攻击者创建持久化机制，从而提供另一个检测机会。

---

## 32. 李·费尔森斯坦

**原文标题**: Lee Felsenstein

**原文链接**: [https://en.wikipedia.org/wiki/Lee_Felsenstein](https://en.wikipedia.org/wiki/Lee_Felsenstein)

李·费尔森斯坦是一位1945年出生的美国计算机工程师，以其在个人电脑发展中的关键作用而闻名。作为Homebrew计算机俱乐部的关键人物，他设计了奥斯本1号，第一台量产的便携式电脑。

在奥斯本1号之前，费尔森斯坦设计了Sol-20电脑、PennyWhistle调制解调器以及VDM-1视频显示模块板，这是一种共享内存字母数字视频显示设计，后来成为个人电脑显示器的标准。受伊万·伊里奇“合意”技术哲学的启发，他的设计专注于降低成本，以使计算机技术得以广泛应用。

费尔森斯坦还参与了社区记忆项目，这是互联网时代之前最早尝试创建用于社交互动的公共计算机终端的项目之一。他曾就读于加州大学伯克利分校，参与了言论自由运动，后来获得了电气工程和计算机科学学位。

他的职业生涯包括在奥斯本电脑公司、Interval Research Corporation和Pemstar Pacific Consultants担任职务。他被誉为“电子前沿的先驱”，并获得了创意卓越奖的编辑选择奖。2003年，他为发展中国家设计了一个开源电信系统，被称为“脚踏动力互联网”。他是Hacker Dojo的创始导师，并于2016年被任命为计算机历史博物馆的研究员。

---

## 33. 用一次性电子烟电池组装2.5千瓦时电池，为我的工作室供电 [视频]

**原文标题**: Building a 2.5kWh battery from disposable vapes to power my workshop [video]

**原文链接**: [https://www.youtube.com/watch?v=dy-wFixuRVU](https://www.youtube.com/watch?v=dy-wFixuRVU)

用一次性电子烟电池构建2.5千瓦时电池为我的工作室供电：本YouTube视频探索了一个项目，创作者旨在利用从一次性电子烟中提取的电池构建一个可用的电源。标题清楚地概述了核心思想：收集废弃电子烟中的小型独立电池，并将其重新用于构建一个更大的2.5千瓦时电池组。该电池组的预期用途是为创作者的工作室供电，表明这是一种DIY且可能具有成本效益的储能方法。

虽然标题信息量很大，但所提供的摘录内容仅包含标准的YouTube样板信息。它提到了版权、联系方式、广告、开发者资源、条款、隐私、安全、YouTube的运作方式、测试新功能以及关于NFL周日票的免责声明。这段附加文字与视频的实际内容无关，没有提供关于电子烟电池项目的构建过程、面临的挑战或整体可行性的进一步见解。我们只知道视频的*目标*，而不是*执行*。

---

## 34. JVM异常：反编译视角

**原文标题**: JVM exceptions are weird: a decompiler perspective

**原文链接**: [https://purplesyringa.moe/blog/jvm-exceptions-are-weird-a-decompiler-perspective/](https://purplesyringa.moe/blog/jvm-exceptions-are-weird-a-decompiler-perspective/)

本文深入探讨了JVM异常反编译的复杂性，揭示了`try...catch`和`try...finally`块看似简单的表象背后，隐藏着字节码解释方面的重大挑战。作者强调，JVM基于栈的特性，以及异常处理区域存储在单独的异常表中，再加上`javac`行为上的怪异之处，导致了复杂的边缘情况。

主要问题包括：

*   **非嵌套异常区域：** JVM允许异常处理范围相交甚至目标地址位于范围之内，从而使简单的反编译变得复杂。
*   **`try...finally`复制：** `javac`在每个退出路径（fallthrough, `return`, `throw`）上复制`finally`块，需要在反编译过程中谨慎处理，以避免错误地捕获`finally`块内的异常。
*   **`return`语句中的异常：** 虽然不常见，但在特定情况下，`return`语句可能会抛出`IllegalMonitorStateException`，增加了另一层复杂性。
*   **可达性和类型检查：** JVM的双重类型检查系统（验证与推断）影响了不可达代码的处理方式，可能导致旧类文件中不正确的类型解释。
*   **EH的豁免范围：** 当存在`finally`块或存在导致异常表中单个try块有多行的`catch`块时，`javac`会将`return`和`goto`语句从`try`范围中排除。

作者总结说，对异常处理进行反编译的简单方法是不够的，对于准确和健壮的反编译，需要对JVM的内部机制有更细致的理解。他们的方法包括表示到try块的每个路径上的豁免区域，如果这些区域具有匹配的内容，则简化为finally。

---

## 35. 大理石喷泉

**原文标题**: Marble Fountain

**原文链接**: [https://willmorrison.net/posts/marble-fountain/](https://willmorrison.net/posts/marble-fountain/)

作者描述了“大理石喷泉”的创作过程，这是一个程序生成的3D打印艺术品。出于利用Formlabs打印机的性能创造复杂结构的愿望，该项目涉及算法设计，以引导大理石球穿过蜿蜒的轨道。

最初的系统涉及随机点放置和样条生成，但作者的目标是更复杂的运动，从而开发了一种路径求解器。该求解器使用一系列规则和函数来迭代地优化大理石路径，确保其保持在边界内，保持恒定的坡度，强制执行转弯半径限制，并避免与其他轨道段和自身发生碰撞。

由于旋转惯性和摩擦的复杂性，速度控制被证明具有挑战性。解决方案包括大幅倾斜转弯以调节速度。滚珠丝杠升降机构允许无轴承操作，但也引入了一种特定的故障模式。

支撑结构的生成通过将支柱视为具有吸引力、排斥力和惯性规则的粒子系统来简化。作者指出OpenSCAD在处理此类有机几何体方面的局限性，并建议未来的迭代可以从SDF库中受益。

该项目于2024年2月开始，于9月结束，投入了大量精力，最终在画廊展出。展览期间出现了诸如大理石丢失和电机过热等问题。尽管如此，作者还是分享了该项目和代码，并打算探索诸如改进速度估计和加速度建模等想法。感谢朋友Alex在整个过程中给予的支持和投入。

---

## 36. 理解Excel中的财务函数

**原文标题**: Understanding Financial Functions in Excel

**原文链接**: [https://ciju.in/writings/understanding-financial-functions-excel-sheets](https://ciju.in/writings/understanding-financial-functions-excel-sheets)

生成摘要时出错

---

## 37. 艾兹格·W·戴克斯特拉的手稿

**原文标题**: The Manuscripts of Edsger W. Dijkstra

**原文链接**: [https://www.cs.utexas.edu/~EWD/](https://www.cs.utexas.edu/~EWD/)

E.W. Dijkstra 文档库是一个致力于保存和提供 Edsger W. Dijkstra 手稿的网站，Edsger W. Dijkstra 是计算机科学领域极具影响力的人物。该文档库收录了一千多份他的技术笔记、旅行报告、观察记录和评论，统称为“EWD”。虽然许多 EWD 是已发表作品的基础，但大多数仍未发表且之前无法访问。

该文档库旨在通过以 PDF 格式提供这些手稿来缓解这种情况，这些手稿可以通过 BibTeX 和临时索引进行搜索。原始手稿以及其他个人文件保存在奥斯汀德克萨斯大学美国历史中心。该网站还包括志愿者贡献的精选 EWD 的文本记录和翻译，以提高可访问性。

除了手稿之外，该文档库还包含 Dijkstra 的讲座和访谈的视频和音频记录，以及有关他的生平、事业和遗产的信息，包括为纪念他而举办的研讨会。它重点介绍了 Edsger W. Dijkstra 分布式计算奖和 Dijkstra 纪念讲座。该网站鼓励用户贡献，例如校对文本记录、添加交叉引用和提供 EWD 的摘要。最后，该网站提供有关版权的信息，并提供指向相关网站和资源的链接，包括一个致力于受 Dijkstra 工作启发的严谨思维的网站。

---

## 38. DEC64：十进制浮点数（2020）

**原文标题**: DEC64: Decimal Floating Point (2020)

**原文链接**: [https://www.crockford.com/dec64.html](https://www.crockford.com/dec64.html)

生成摘要时出错

---

## 39. 时间机器简史（2024）

**原文标题**: A brief history of Time Machine (2024)

**原文链接**: [https://eclecticlight.co/2024/09/07/a-brief-history-of-time-machine/](https://eclecticlight.co/2024/09/07/a-brief-history-of-time-machine/)

生成摘要时出错

---

## 40. 扩散模型原理

**原文标题**: The Principles of Diffusion Models

**原文链接**: [https://arxiv.org/abs/2510.21890](https://arxiv.org/abs/2510.21890)

arXiv 文章《扩散模型原理》（2025年10月提交）全面概述了扩散模型，探讨了其基本原理和各种公式。作者 Lai、Song、Kim、Mitsufuji 和 Ermon 解释了扩散模型的工作原理，即定义一个将数据逐渐转化为噪声的前向过程。学习目标是学习一个逆向过程，该过程从噪声中重建数据，同时恢复中间分布。

该专著概述了关于扩散模型的三个互补视角：变分视角、基于分数的视角和基于流的视角。变分视角将扩散视为类似于变分自编码器的去噪过程。基于分数的视角侧重于学习不断演变的数据分布的梯度，从而指导重建过程。基于流的视角将生成描述为使用学习到的速度场将噪声连续变换为数据的过程。

一个中心主题是随时间变化的速度场，它指导着从简单的先验分布（噪声）到数据分布的转换。采样涉及求解遵循此轨迹的微分方程。

除了核心原理之外，本文还深入研究了可控生成技术、高效数值求解器以及直接在时间点之间映射的扩散驱动的流映射模型。作者旨在为熟悉基本深度学习的读者提供对扩散模型在概念上和数学上都合理的理解。该论文还提供了各种资源的链接，例如代码存储库、相关论文和交互式演示，供进一步探索。

---

## 41. 树莓派莓果派 – 低成本DIY树莓派掌上赛博终端

**原文标题**: Bumble Berry Pi – A Cheap DIY Raspberry Pi Handheld Cyberdeck

**原文链接**: [https://github.com/samcervantes/bumble-berry-pi](https://github.com/samcervantes/bumble-berry-pi)

“大黄蜂莓派”文章详细介绍了一个低成本、DIY的树莓派掌上网络终端设备的构建项目。作者的动机源于对便携式、触感设备的渴望，该设备适用于编码和脚本编写，而无需长时间等待预制选项。大黄蜂莓派的主要特点包括一个4.3英寸触摸屏、一个QWERTY键盘、一个37瓦时电池，以及一个仅依赖两个3D打印部件的设计，方便构建。

该项目优先考虑经济性和易于获得的零件，目标总成本约为60美元（不包括树莓派本身）。文章提供了一个详细的零件清单，附带亚马逊链接，明确说明了树莓派、触摸屏显示器、迷你蓝牙键盘、USB移动电源以及必要的适配器、螺丝和插件等组件。

组装说明虽然仍在完善中，但概述了以下步骤：3D打印外壳部件、插入螺纹插件、将树莓派连接到屏幕、将屏幕固定到外壳、使用Kapton胶带放置键盘和移动电源、布线，以及将外壳拧在一起。作者还为有兴趣修改设计的人提供了Solidworks设计文件。

---

## 42. 蒙大拿州成为首个将“计算权”写入法律的州

**原文标题**: Montana becomes first state to enshrine 'right to compute' into law

**原文链接**: [https://montananewsroom.com/montana-becomes-first-state-to-enshrine-right-to-compute-into-law/](https://montananewsroom.com/montana-becomes-first-state-to-enshrine-right-to-compute-into-law/)

2025年4月，蒙大拿州成为首个将“计算权”写入法律的州，通过了由参议员丹尼尔·佐尔尼科夫发起、州长格雷格·詹福特签署的《蒙大拿州计算权法案》(MRTCA)。这项开创性的立法根据该州宪法对财产和言论自由的保护，保障了公民访问和使用计算工具和人工智能技术的权利。支持者认为，它在人工智能驱动的世界中确保了数字自由。

该法律允许州政府为公共卫生和安全进行监管，但对限制设置了很高的门槛，要求这些限制必须是明确必要的且范围窄。它还强制要求对人工智能控制的关键基础设施实施“关闭机制”和年度安全审查。

隐私倡导者和技术政策团体，如边疆研究所，对该法律表示赞赏，认为它是对数字权利的捍卫。与其他州不同，蒙大拿州的做法是赋予个人用户权力，而不是限制访问。

《蒙大拿州计算权法案》激发了新罕布什尔州的类似努力，该州立法者正在推动一项宪法修正案，以保证计算访问权。在全国范围内，由RightToCompute.ai领导，并得到Haltia.AI和ASIMOV Protocol等组织支持的计算权运动认为，计算是一项基本人权。这些团体认为，计算机是人类思想的延伸，个人应控制自己的数据和数字工具。蒙大拿州的法律可以作为其他州的潜在蓝图。

---

## 43. “米”是如何变成一米长的

**原文标题**: How the "meter" came to be one meter long

**原文链接**: [https://bigthink.com/starts-with-a-bang/meter-exactly-one-meter-long/](https://bigthink.com/starts-with-a-bang/meter-exactly-one-meter-long/)

生成摘要时出错

---

## 44. 世嘉Master System

**原文标题**: The Sega Master System

**原文链接**: [https://bumbershootsoft.wordpress.com/2025/11/08/the-sega-master-system/](https://bumbershootsoft.wordpress.com/2025/11/08/the-sega-master-system/)

本文深入探讨了世嘉Master System（SMS），将其置于游戏机世代的背景下，并将其与其前代产品SG-1000以及其主要竞争对手Famicom/NES进行了比较。文章认为，虽然SG-1000被认为是第三代游戏机，但其硬件更接近于ColecoVision等第二代系统。基于Mark III的SMS代表了一次重大升级，与1985年家用电脑的进步相吻合。

文章详细比较了SMS、SG-1000和NES在几个关键领域的性能：CPU内存、显存、ROM容量、分辨率、色深、调色板、精灵、背景和滚动、VDP寄存器和VRAM访问以及时间限制。 与SG-1000和NES相比，SMS在RAM、ROM空间和色彩能力方面均有所提升。

一个关键的结论是世嘉和任天堂之间设计理念的差异。 世嘉的设计被描述为更加“务实”，提供了易于访问、设计好的功能。 相反，任天堂的系统通常需要结合多个独立的机制才能达到预期的效果，从而提供更大的灵活性，但也可能更难编程。

最后，文章还涉及了卡带结构、BIOS编写以及SMS与SG-1000的向后兼容性。

---

## 45. 电子邮件验证协议

**原文标题**: Email verification protocol

**原文链接**: [https://github.com/WICG/email-verification-protocol](https://github.com/WICG/email-verification-protocol)

电子邮件验证协议提供了一种新的Web上验证电子邮件地址的方式，无需依赖传统的验证邮件或社交登录提供商。它旨在减少用户摩擦并增强隐私。

其工作原理如下：当用户在网站的表单字段中输入电子邮件地址时，浏览器会查询与该电子邮件域名关联的DNS记录，以找到指定的“颁发者”。该颁发者已获得域名所有者的授权来验证电子邮件，如果用户已经通过该颁发者进行了身份验证（例如，通过现有的cookie），则颁发者将提供一个签名令牌，确认电子邮件的所有权。

该协议使用SD-JWT+KB令牌，这是一种特定类型的JWT，它将令牌颁发与呈现分离，从而增强了安全性和隐私性。浏览器验证颁发者的签名并生成一个“KB”令牌，该令牌将颁发者的令牌绑定到浏览器，防止其他方重用。然后，将生成的SD-JWT+KB呈现给网站，网站可以使用颁发者的公钥验证该令牌，从而确认电子邮件地址的有效性。

此过程消除了用户切换到其电子邮件收件箱并单击链接的需求，并且防止颁发者知道哪些网站正在请求验证。该文档还概述了特定的HTML和JavaScript实现，以及错误处理和安全注意事项。

---

## 46. Reviving Classic Unix Games: A 20-Year Journey Through Software Archaeology

**原文标题**: Reviving Classic Unix Games: A 20-Year Journey Through Software Archaeology

**原文链接**: [https://vejeta.com/reviving-classic-unix-games-a-20-year-journey-through-software-archaeology/](https://vejeta.com/reviving-classic-unix-games-a-20-year-journey-through-software-archaeology/)

本文记录了为复兴1987年经典Unix游戏“Conquer”而进行的20年历程。作者“admin”在20世纪90年代发现了这款游戏，并在2006年开始了将其重新授权为GPL的行动，以确保其得以保存。

这个过程涉及大量的“数字考古”，以找到原始作者Edward Barlow和Adam Bryant，并获得他们的许可。成功联系到Barlow后，寻找Bryant的过程持续了数年，直到他自己发现了作者的在线文章并授予了许可。

2025年，Stephen Smoogen向作者介绍了“Conquer Version 5”，这是Adam Bryant对游戏的完全重写版本。为这个版本获得GPL许可也被证明是成功的。另一位贡献者Martin Forssen (MaF)也被找到，并同意重新授权他的PostScript实用程序来生成游戏地图。寻找另一位贡献者Richard Caley的努力，最终以发现他的纪念网站而告终，该网站揭示了他已于2005年去世，因此无法重新授权他的贡献。

作者随后使用Melange（用于APK打包）和Debian打包等工具对游戏进行了现代化改造，并使用GitHub Actions实现了CI/CD。该项目强调了代码文档、明确许可、社区参与的重要性，以及现代工具如何复兴遗留软件。现在，两个Conquer版本都获得了GPL v3许可，并提供现代化的打包，这成为了软件考古和保存的一个案例研究。本文强调了保存计算历史并将过去与未来联系起来的重要性。

---

## 47. AWS 如何因其复杂性而失去年轻一代

**原文标题**: How AWS is losing the younger generation with complexity

**原文链接**: [https://www.theregister.com/2025/11/04/aws_genz_misery_nope/](https://www.theregister.com/2025/11/04/aws_genz_misery_nope/)

由于 AWS 的复杂性和繁琐的部署流程，Corey Quinn 认为它正在失去年轻开发者的青睐。他用一个在 AWS 上部署简单 Webapp 的详细例子说明了这些痛点，强调了繁琐的账户设置、IAM 配置以及集成各种无法无缝协作的服务的必要性。他将此与 Vercel、Netlify 和 Render 等现代、以开发者为中心的平台所提供的易用性和快速部署进行了对比。

Quinn 认为这是一个代际问题，X 世代和千禧一代已经习惯了 AWS 和 GCP 的复杂性，而 Z 世代更喜欢更简单的平台。他幽默地将 Azure 称为“婴儿潮一代云”。他指出，AWS 的复杂性是一种刻意的设计选择，反映了对用户体验缺乏关注。

他进一步强调，AI 助手（越来越多地指导开发者）会因为 AWS 的复杂性而引导他们远离它，这是一个风险。他担心下一代开发者将没有耐心或欲望来驾驭 AWS 困难的系统。Quinn 总结说，AWS 尽管功能强大，但有可能对未来的开发者变得无关紧要，他们优先考虑易用性和效率，而不是通过忍受复杂性来证明他们的技术实力。

---

## 48. 被任天堂起诉

**原文标题**: Sued by Nintendo

**原文链接**: [https://www.suedbynintendo.com/](https://www.suedbynintendo.com/)

提供的内容极其有限，仅说明有关任天堂诉讼的信息正在加载中，并且需要启用JavaScript。

因此，我无法提供文章本身的摘要。我只能推断出*可能*有关于任天堂涉及诉讼的信息，但由于技术问题导致内容无法加载，因此无法访问。我无法告诉你诉讼的*内容*，任天堂在起诉*谁*，或者*任何*细节。关键在于该文章目前无法阅读。

---

## 49. The Linux Kernel Looks to “Bite the Bullet” in Enabling Microsoft C Extensions

**原文标题**: The Linux Kernel Looks to “Bite the Bullet” in Enabling Microsoft C Extensions

**原文链接**: [https://www.phoronix.com/news/Linux-6.19-Patch-Would-MS-Ext](https://www.phoronix.com/news/Linux-6.19-Patch-Would-MS-Ext)

The Linux kernel is considering enabling Microsoft C Extensions by adding the `-fms-extensions` compiler argument during compilation, potentially starting with the Linux 6.19 kernel. This would allow the GCC and LLVM/Clang compilers to recognize and utilize non-standard C/C++ constructs found in Microsoft header files.

While patches to enable this have been proposed in the past, they haven't been implemented due to concerns about adding another compiler flag for relatively minor code improvements. The current proposal, now queued in kbuild-next, aims to "bite the bullet" and enable it universally, making it readily available for future use cases where it could lead to "prettier code" and potentially save stack space. Specifically, it would allow the use of anonymously tagged structs or unions within other structs/unions.

Rasmus Villemoes and others argue that a universal implementation avoids the need to justify the flag on a case-by-case basis. The change is being implemented through two patches: one to enable `-fms-extensions` globally and another to ensure it's applied to architectures with dedicated CFLAGS. Linus Torvalds seems amenable to the change, although some may object to incorporating Microsoft C behavior into the core Linux kernel.


---

## 50. 维生素D3突破性研究：心脏病再发风险降低一半

**原文标题**: Vitamin D3 breakthrough halves risk of second heart attack

**原文链接**: [https://www.sciencedaily.com/releases/2025/11/251110021043.htm](https://www.sciencedaily.com/releases/2025/11/251110021043.htm)

2025年Intermountain Healthcare文章强调个性化维生素D3治疗在降低二次心脏病发作风险方面取得的突破。研究人员发现，针对心脏病发作幸存者调整维生素D3剂量以达到最佳血液水平，可将其再次心脏病发作的风险降低50%。这种“靶向治疗”方法包括监测血液维生素D水平并调整剂量，以维持水平高于40 ng/mL。

从2017年至2025年进行的TARGET-D临床试验涉及630名心脏病患者。参与者被随机分配到没有维生素D管理的对照组或接受靶向维生素D3补充剂的治疗组。超过一半的治疗组需要初始剂量为5,000 IU的维生素D3才能达到目标水平，这明显高于标准建议。

虽然各组之间总体主要心脏事件（MACE）没有显著差异，但治疗组再次心脏病发作的风险降低了50%。鉴于全球很大一部分人口由于生活方式的改变和日晒减少而维生素D水平较低，这一发现尤为重要。研究人员计划进行更大规模的试验，以证实这些结果并评估靶向维生素D管理对其他形式心血管疾病的影响。

---

## 51. Zensical – 由 Material for MkDocs 团队构建的现代静态站点生成器

**原文标题**: Zensical – A modern static site generator built by the Material for MkDocs team

**原文链接**: [https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/](https://squidfunk.github.io/mkdocs-material/blog/2025/11/05/zensical/)

Zensical：Material for MkDocs团队开发的新一代静态站点生成器，旨在解决MkDocs的局限性和供应链风险。它专注于性能、可扩展性和舒适的编写体验，以简化文档站点创建。Zensical与现有的Material for MkDocs项目高度兼容，读取`mkdocs.yml`，迁移所需更改极少。

主要改进包括高达5倍的重建速度提升、现代化的可定制设计，以及名为Disco的超快速客户端搜索引擎。全新的差分构建引擎ZRX是Zensical的基础，可实现更快的特性开发和强大的性能。未来的计划包括用于扩展的模块系统、用于灵活设计的组件系统，以及基于Rust的Markdown解析器的CommonMark支持，以提高速度。

该项目完全开源，并以“Zensical Spark”取代了赞助商模式，为专业用户提供支持、对开发的影响力，并确保长期维护。Material for MkDocs目前处于维护模式，至少提供12个月的持续支持。团队正在壮大，他们鼓励用户订阅其新闻通讯，以获取更新和潜在的未来支持机会。

---

## 52. 迄今最大、最详尽的银河系射电图像

**原文标题**: The largest, most detailed radio image of the Milky Way yet

**原文链接**: [https://www.sciencenews.org/article/largest-radio-image-milky-way-galaxy](https://www.sciencenews.org/article/largest-radio-image-milky-way-galaxy)

天文学家创建了迄今为止最大、最详细的银河系射电图像，该图像发表在《澳大利亚天文学会出版物》上。这张图像是从南半球看到的银河系侧视图，是利用位于西澳大利亚的默奇森广域阵列望远镜在2013年至2020年间140多个夜晚收集的数据组装而成的。

该项目的主要动机是识别和分类超新星遗迹，即爆炸恒星的气体残骸。虽然已经发现了大约300个超新星遗迹，但科学家估计银河系内大约存在2000个，研究它们将为恒星演化提供有价值的见解。

该图像是通过拼接近2000个单独的观测结果构建的，每个观测结果都捕捉到特定的射电波长范围。最终的图像跨越60,000光年，仅占银河系宽度的一半多一点。研究人员叠加了20个版本的图像，每个版本代表不同的射电波长，其中较长的波长显示为红色，较短的波长显示为蓝色。这些颜色指示了射电发射背后的机制，例如来自恒星育婴所的热辐射（蓝色）和来自超新星遗迹的非热辐射（红色）。由此产生的多色视图有助于识别和理解各种银河系过程。

---

## 53. 当哈希变成字符串时：追 hunting Ruby 的百万分之一内存漏洞

**原文标题**: When your hash becomes a string: Hunting Ruby's million-to-one memory bug

**原文链接**: [https://mensfeld.pl/2025/11/ruby-ffi-gc-bug-hash-becomes-string/](https://mensfeld.pl/2025/11/ruby-ffi-gc-bug-hash-becomes-string/)

文章详细介绍了作者深入调查一个由 Karafka 用户报告的神秘 Ruby 错误，该错误表现为在访问 FFI 结构体时出现 `NoMethodError: undefined method 'default' for an instance of String`。这个错误尤其令人困惑，因为代码从未明确使用 `#default` 方法，而该方法通常与 Ruby Hash 相关联。

最初怀疑与预编译 gems 和 Alpine Linux (musl libc) 的组合有关，作者系统地排除了类型不匹配、结构体对齐问题和 ABI 不兼容等常见原因。

突破来自于意识到负责存储结构体字段定义的内部 FFI Hash (`rbFieldMap`) 在运行时不知何故被替换为 String 对象。 这指向潜在的内存管理问题，特别是“释放后使用”漏洞。 作者发现，旧版本的 FFI gem（1.17.0 之前）在创建结构体布局时缺乏正确的写屏障。 这意味着 Ruby 垃圾回收器 (GC) 不知道对内部 Hash 的引用，从而允许它们被提前释放。

作者随后开发了一个复杂的多线程概念验证 (POC)，旨在通过创建高内存压力并利用时间窗口来重现该错误，在该时间窗口中，Hash 可能被 GC 释放并被 String 替换，然后被 FFI 访问。 POC 证实了该漏洞，表明 FFI 版本 < 1.17.0 中缺少写屏障确实可能导致灾难性的内存损坏。 在 FFI 1.17.0 中实现的修复涉及添加 `RB_OBJ_WRITE` 调用，以使用 Ruby GC 正确注册这些引用，防止提前释放并确保内存安全。

---

## 54. LLM政策？

**原文标题**: LLM policy?

**原文链接**: [https://github.com/opencontainers/runc/issues/4990](https://github.com/opencontainers/runc/issues/4990)

`opencontainers/runc` GitHub议题：关于大型语言模型（LLM）生成内容贡献策略的探讨。作者cyphar注意到可能由LLM生成的PR和bug报告数量增多，建议在`CONTRIBUTING.md`文件中明确可接受和不可接受的LLM使用方式。

Cyphar个人反对接受任何LLM生成的内容，并提议将LLM生成的issue作为垃圾信息关闭，因为它们包含的信息不可靠且常常不正确。 担忧在于，这些信息无法验证是否确实发生在用户身上，从而使bug的分类变得困难。

关于LLM生成的代码，作者建议最低要求是：提交者必须通过在审查期间能够用自己的话解释代码，来证明其对所提交代码的清晰理解。 他引用了具体示例（#4940和#4939），在这些示例中，可能没有达到此标准。

提出的进一步论点是，LLM生成的代码可能不符合开发者原创证明（DCO）的要求，从而可能产生法律问题。 最后，该议题参考了Incus的做法，即完全禁止所有LLM的使用作为可能的先例。 该议题旨在引发`opencontainers/runc-maintainers`之间的讨论，以达成如何处理LLM生成内容的共识。

---

## 55. 解决鸽子问题的过度工程方案 (2022)

**原文标题**: The overengineered solution to my pigeon problem (2022)

**原文链接**: [https://maxnagy.com/posts/pigeons/](https://maxnagy.com/posts/pigeons/)

生成摘要时出错

---

## 56. 解开每一个数独谜题 (2006)

**原文标题**: Solving Every Sudoku Puzzle (2006)

**原文链接**: [https://norvig.com/sudoku.html](https://norvig.com/sudoku.html)

彼得·诺维格的这篇文章探讨了如何使用约束传播和搜索算法以编程方式解决每一个数独谜题。文章首先定义了数独符号，包括方格、单元（行、列和宫）和同伴（共享一个单元的方格）。

作者介绍了两种数据表示形式：用于初始谜题输入的文本网格和一个名为“values”的字典，该字典将每个方格映射到其可能的数字值。约束传播是一种关键策略，它使用两条规则：当一个方格只有一个可能的值时，从该方格的同伴中消除该数字；以及当一个数字在一个单元内只有一个可能的位置时，将该数字放置在该单元中。`assign`和`eliminate`函数实现了这种传播。

虽然仅靠约束传播可以解决一些谜题，但更难的谜题需要搜索。文章解释说，由于大量的可能性，蛮力方法是不可行的。约束传播通过尽早消除不可能的组合来显著减少搜索空间。

实现的搜索算法是深度优先搜索。它涉及选择一个可能性最少的未填充方格，然后递归地尝试该方格中的每个可能的数字。如果分配一个数字导致矛盾，则算法回溯并尝试另一个数字。这个过程一直持续到找到解决方案。

---

## 57. 如果Java的集合拥有对称转换器方法会怎样？

**原文标题**: What If Java Had Symmetric Converter Methods on Collection?

**原文链接**: [https://donraab.medium.com/what-if-java-had-symmetric-converter-methods-on-collection-cbb824885c3f](https://donraab.medium.com/what-if-java-had-symmetric-converter-methods-on-collection-cbb824885c3f)

本文探讨了集合上对称转换器方法的概念，比较了它们在 Smalltalk、Java 和 Eclipse Collections 中的可用性和用法。 Smalltalk 为其可变集合提供了一组丰富的以 "as" 为前缀的转换器方法。 Java 直接在 `Collection` 和 `Stream` 接口上提供了有限的以 "to" 为前缀的转换器方法，通常需要使用 `Collectors` 进行多步骤转换。 作者认为 Java 的方法缺乏对称性和便利性。

Eclipse Collections 是一个开源项目，被认为是一种更优的选择。 它在其 `RichIterable` 接口上提供了一套全面的以 "to" 为前缀的转换器方法，支持可变和不可变集合，并在类型名称上具有明确的区分。 这种对称性提高了可发现性和易用性。 文章展示了代码示例，演示了使用每种语言/库在 `List`、`Set` 和 `Bag` 之间进行转换。

作者强调了良好设计的转换器方法对于可维护性、可读性和可用集合类型的可发现性的重要性。 他认为 Eclipse Collections 将 Smalltalk 的便利性带到了 Java 中，提供了更对称和用户友好的集合转换。 最后，他简要地提到了 Kotlin，暗示了随着不可变集合的添加，其集合功能未来会有增长。

---

## 58. 欧盟出招整治塑料颗粒，防止梦魇般的清理工作

**原文标题**: EU takes aim at plastic pellets to prevent their nightmare cleanup

**原文链接**: [https://www.yahoo.com/news/articles/eu-takes-aim-plastic-pellets-030314496.html](https://www.yahoo.com/news/articles/eu-takes-aim-plastic-pellets-030314496.html)

欧盟正在考虑更严格的法规，以应对塑料颗粒（“塑料微珠”）污染。这种污染是由于生产、运输和处理过程中发生的泄漏造成的，是一个普遍存在的环境问题。 这些微小的颗粒被用于制造各种塑料产品，一旦释放到环境中就难以清理，从而影响海洋生物、旅游业，并可能影响人类健康。

欧盟委员会估计，每年有数万吨塑料微珠进入欧盟环境。清理工作既费力又常常不彻底。斯里兰卡和西班牙等国过去发生的泄漏事件凸显了其毁灭性后果。

虽然国际海事组织（IMO）已发布不具约束力的建议，但泄漏源不仅仅限于运输，还包括石化行业的运营损失。环保组织强调需要在整个价值链中追究责任。

行业团体提出了不同的观点。塑料制造商声称，加工环节并非泄漏的主要来源，并强调了浪费原材料的成本。 主要的石油和天然气生产国抵制对新塑料生产的限制，突显了解决这一普遍存在的污染问题的难度。 文章最后强调了塑料消费与环境中塑料微珠的普遍存在之间的联系。

---

## 59. 使用 FastAPI-Voyager 可视化 FastAPI 端点

**原文标题**: Visualize FastAPI endpoints with FastAPI-Voyager

**原文链接**: [https://www.newsyeah.fun/voyager/](https://www.newsyeah.fun/voyager/)

本文简要介绍FastAPI-Voyager，一款可视化FastAPI端点的工具。其核心功能是提供API的交互式图形化表示，方便用户轻松探索和理解其结构。

主要要点包括：

*   **可视化：** FastAPI-Voyager以可视方式映射FastAPI端点，提高API理解度。
*   **交互式探索：** 用户可以放大/缩小并双击节点以查看有关特定端点的详细信息。
*   **依赖关系映射：** 按住Shift键并单击允许用户查看模式依赖关系，简化对API内数据流的理解。
*   **JSON导入：** 该工具似乎允许导入API定义的JSON表示进行可视化。

总而言之，FastAPI-Voyager通过提供用于探索端点、模式依赖关系和API结构的视觉界面，使导航和理解复杂的FastAPI项目变得更加容易。

---

## 60. 欧盟采取措施应对塑料颗粒，以防止其造成的清理噩梦

**原文标题**: EU takes aim at plastic pellets to prevent their nightmare cleanup

**原文链接**: [https://www.yahoo.com/news/articles/eu-takes-aim-plastic-pellets-030314496.html](https://www.yahoo.com/news/articles/eu-takes-aim-plastic-pellets-030314496.html)

本文着重强调了对塑料颗粒（“塑料微粒”）污染日益增长的担忧以及欧盟可能采取的应对措施。塑料微粒是制造过程中使用的小塑料珠，在运输和处理过程中容易洒落，导致广泛的环境污染。这些泄漏给清理工作带来了巨大的挑战，影响了海洋生物、旅游业，并可能影响人类健康。欧洲议会正在考虑制定更严格的法规，要求公司实施保障措施以防止塑料微粒泄漏。

文章详细描述了问题的严重程度，引用了每年有数万吨塑料颗粒进入欧盟环境的估计数据。清理工作困难重重，而且很少能完全成功。斯里兰卡和西班牙等重大泄漏事件的例子说明了其对沿海地区的破坏性影响。

虽然集装箱落水等运输事故是一个已知来源，但文章指出，整个价值链中存在更广泛的问题，包括制造场所的运营损失。虽然塑料制造商声称已经意识到并在努力防止其设施内的泄漏，但石化巨头在很大程度上对此事保持沉默。文章强调需要采取全面的方法来解决塑料微粒问题，并指出在全球范围内限制塑料生产的努力面临阻力。

---

## 61. CHIP8 – 模拟器、汇编器、游戏、VHDL硬件实现

**原文标题**: CHIP8 – emulator, assembler, game, vhdl hardware implementations

**原文链接**: [http://blog.dominikrudnik.pl/chip8-emulator-assembler-game-vhdl](http://blog.dominikrudnik.pl/chip8-emulator-assembler-game-vhdl)

本文详细介绍了作者出于教育目的，从头开始创建 CHIP-8 模拟器、汇编器和游戏的旅程。该项目涉及在 VHDL 中实现 CHIP-8 指令集架构 (ISA)，创建基于 C 的解释器，以及用 C++ 开发一个简单的汇编器。

该模拟器的构建重点在于操作码实现的细节，避免了抽象层。C 代码获取并解码操作码，然后在大型 if-else 代码块中执行它们。由于其复杂性，绘制指令被重点介绍。作者还在实现的平台上创建了一个名为“Flappy Bird”的简单游戏。

汇编器使用 TokenIterator 来扫描和标记源代码。操作码匹配通过 TokenMatcher 函数和 OutputGenerator 函数系统完成，这些函数将 token 转换为二进制操作码。由于汇编器的单次处理特性，使用了一个类似链接器的系统来解析地址引用。文章提供了 TokenIterator 和汇编器各个组件的代码片段。

作者承认该项目尚未达到可用于生产的水平，包含注释代码和非最佳解决方案，但强调了在理解计算机系统概念方面获得的教育价值。

---

## 62. Show HN: DroidDock – 一款通过ADB浏览安卓设备文件的简洁macOS应用

**原文标题**: Show HN: DroidDock – A sleek macOS app for browsing Android device files via ADB

**原文链接**: [https://rajivm1991.github.io/DroidDock/](https://rajivm1991.github.io/DroidDock/)

DroidDock is a free and open-source macOS application designed for browsing and managing files on Android devices via ADB (Android Debug Bridge). Version 0.1.0, compatible with macOS 10.13 and later and supporting both Apple Silicon and Intel processors, offers a sleek and intuitive native interface for file management.

Key features include automatic device detection and simultaneous management of multiple devices, a comprehensive file browser with support for all file types, fast drag-and-drop or single-click downloads and uploads, image previews, real-time storage information, built-in search, dark mode, and auto-updates.

Installation involves downloading the DMG file, moving the application to the Applications folder, and initially right-clicking and selecting "Open" to bypass a security warning since the application is currently unsigned.

Prerequisites include ADB installation (easily done via Homebrew), a USB cable, and an Android device with USB debugging enabled. DroidDock offers a stylish and efficient way to interact with Android file systems directly from a macOS environment.


---

## 63. 任天堂前员工揭秘NES发售幕后故事

**原文标题**: Former Nintendo employees reveal what it took to launch the NES

**原文链接**: [https://hanafuda.report/articles/former-nintendo-employees-reveal-what-it-took-to-launch-the-nes-in-america/](https://hanafuda.report/articles/former-nintendo-employees-reveal-what-it-took-to-launch-the-nes-in-america/)

本文报道了在波特兰复古游戏博览会上举行的小组讨论，庆祝 NES 在美国发布 40 周年。小组讨论由 Frank Cifaldi 主持，参与者包括前任天堂美国分公司员工 Bruce Lowry（销售副总裁）、Gail Tilden（市场经理）和 Lance Barr（设计师）。

讨论涵盖了所面临的市场挑战、设计考量以及 NES 的持久遗产。 Lance Barr 讨论了他为美国市场重新设计游戏机的工作，并指出代理商早期的设计方案通常类似于雅达利的机器，甚至带有仿木纹。

小组分享了许多轶事，包括：来自母亲们对 NES 光枪的担忧、术语“Game Pak”的由来、在 CES 贸易展上采用的策略，甚至还有关于任天堂仓库里蛇的故事。

本文鼓励读者在 YouTube 上观看完整的 1 小时 45 分钟的小组讨论，详细了解 NES 的发布历程。

---

## 64. 使用 bubblewrap 为 NetBSD 增加沙盒功能

**原文标题**: Using bubblewrap to add sandboxing to NetBSD

**原文链接**: [https://blog.netbsd.org/tnf/entry/gsoc2025_bubblewrap_sandboxing](https://blog.netbsd.org/tnf/entry/gsoc2025_bubblewrap_sandboxing)

本文总结了Vasyl Lanko的Google编程之夏2025项目，该项目旨在为NetBSD实现类似Linux的命名空间以进行沙盒化。目前，NetBSD缺乏除chroot之外的强大的沙盒解决方案。该项目的目标是为应用程序隔离系统的各个部分，类似于Linux命名空间。

该项目侧重于实现八种Linux命名空间类型中的两种：UTS（UNIX分时系统）和MNT（挂载）。UTS命名空间允许隔离主机名和域名，而MNT命名空间隔离挂载点。

该实现使用NetBSD的kauth子系统来管理命名空间生命周期和凭据处理。为每种命名空间类型创建了单独的secmodel。UTS命名空间的实现涉及创建UTS信息的副本并修改内核代码以使用包装函数来检索正确的UTS结构。MNT命名空间的实现旨在控制每个命名空间的挂载列表，这需要对内核代码进行更复杂的更改，并深刻理解Linux和NetBSD中的VFS概念。

该项目完成了功能正常的UTS命名空间实现和一个正在进行中的MNT命名空间实现。该代码可在GitHub上找到。未来的工作包括实现其他命名空间类型，如PID和用户命名空间，以及实现命名空间管理功能（lsns，setns）。作者强调了由于Linux和NetBSD之间的差异而遇到的挑战，强调了意想不到的研究量以及移植Linux命名空间的复杂性。该项目从模拟unshare系统调用转向直接在NetBSD内核中实现命名空间。作者对导师和NetBSD社区表示感谢。

---

## 65. 空中客车如何起飞

**原文标题**: How Airbus took off

**原文链接**: [https://worksinprogress.co/issue/how-airbus-took-off/](https://worksinprogress.co/issue/how-airbus-took-off/)

本文记录了空中客车如何从一个苦苦挣扎的欧洲联盟发展成为全球航空航天领导者的历程，并将它的成功与其他欧洲工业项目的失败进行了对比。在商业航空的早期，美国占据主导地位，波音公司利用军事合同和优惠政策占据优势。欧洲公司各自为政，举步维艰。为了应对这种情况，欧洲各国政府于1970年成立了空中客车工业公司。

空中客车的成功源于以客户为中心的策略，优先打造理想的产品，而不是政治考量。负责A300项目的罗杰·贝泰勒专注于了解航空公司的需求，从而促成了设计变更和务实的设备选择，例如使用更便宜的美国发动机。空中客车指定英语为项目语言，并避免使用公制测量单位，以吸引美国市场。

由于经济形势和美国航空公司的怀疑，A300B最初面临销售挑战。空中客车强调其美国制造的零部件，并在华盛顿积极游说。东方航空公司以1美元试租飞机成为一个关键的突破，大大提升了信誉。

于1988年推出的A320以数字电传操纵系统和包线保护彻底改变了窄体飞机。尽管最初采用缓慢，但其卓越的技术和设计灵活性使其广受欢迎，成为有史以来最受欢迎的客机系列。到2019年，空中客车的收入超过了波音。

本文强调了其他欧洲企业失败的原因，列举了不利的市场条件、缺乏中央控制、不明确的理由和政治干预。协和飞机是一个工程奇迹，但在商业上不可行，而Unidata和Quaero等项目则因内部纷争和任务蔓延而遭受损失。波音公司最近在安全和监管方面的问题更加凸显了空中客车的成功。

---

## 66. 工作之后又工作：失业应届毕业生眼看就业市场崩溃的笔记

**原文标题**: Work after work: Notes from an unemployed new grad watching the job market break

**原文链接**: [https://urlahmed.com/2025/11/05/work-after-work-notes-from-an-unemployed-new-grad-watching-the-job-market-break/](https://urlahmed.com/2025/11/05/work-after-work-notes-from-an-unemployed-new-grad-watching-the-job-market-break/)

新毕业生的严峻就业市场：自动化、人工智能与“分布外人类”

---

## 67. 数学书籍

**原文标题**: Math Books

**原文链接**: [https://github.com/valeman/Awesome_Math_Books](https://github.com/valeman/Awesome_Math_Books)

本文档是一份全面的数学和物理书籍清单，另有少量计量经济学、优化和信息论方面的书籍。

数学部分内容广泛，涵盖概率、分析（实分析、复分析和数学分析）、线性代数、微积分（微分和积分）、几何（解析几何和初等几何）、微分方程、数论、拓扑等各种主题。 一些书籍用🔥🔥🔥🔥🔥突出显示，可能表明它们的重要性或受欢迎程度。 许多书是旨在培养解决问题能力的问题集。这是一个全面的清单，包括从初级到高级主题的所有技能水平的书籍，就像高中和大学水平的教科书清单一样。

物理部分包含较少的选择，侧重于普通物理问题、力学、电磁学和电子学。 也有几本物理书被突出显示。

---

## 68. Forth – Is it still relevant?

**原文标题**: Forth – Is it still relevant?

**原文链接**: [https://github.com/chochain/eforth](https://github.com/chochain/eforth)

生成摘要时出错

---

## 69. Thiel and Zuckerberg on Facebook, Millennials, and predictions for 2030

**原文标题**: Thiel and Zuckerberg on Facebook, Millennials, and predictions for 2030

**原文链接**: [https://www.techemails.com/p/mark-zuckerberg-peter-thiel-millennials](https://www.techemails.com/p/mark-zuckerberg-peter-thiel-millennials)

生成摘要时出错

---

## 70. Rubin Observatory Discovers Surprise 'Tail' on Iconic Galaxy

**原文标题**: Rubin Observatory Discovers Surprise 'Tail' on Iconic Galaxy

**原文链接**: [https://www.scientificamerican.com/article/rubin-observatory-discovers-surprise-tail-on-iconic-galaxy/](https://www.scientificamerican.com/article/rubin-observatory-discovers-surprise-tail-on-iconic-galaxy/)

生成摘要时出错

---

## 71. Metabolic and cellular differences between sedentary and active individuals

**原文标题**: Metabolic and cellular differences between sedentary and active individuals

**原文链接**: [https://howardluksmd.substack.com/p/if-youre-not-active-youre-sick-you](https://howardluksmd.substack.com/p/if-youre-not-active-youre-sick-you)

生成摘要时出错

---

## 72. The Computer Church – Pennsylvania Computer and Technology Museum

**原文标题**: The Computer Church – Pennsylvania Computer and Technology Museum

**原文链接**: [https://www.thecomputerchurch.org/](https://www.thecomputerchurch.org/)

生成摘要时出错

---

## 73. A hacking kingpin reveals all: Inside the gang that left a trail of destruction

**原文标题**: A hacking kingpin reveals all: Inside the gang that left a trail of destruction

**原文链接**: [https://www.bbc.com/news/articles/cm2w0pvg4wko](https://www.bbc.com/news/articles/cm2w0pvg4wko)

生成摘要时出错

---

## 74. Opencloud – An alternative to Nextcloud written in Go

**原文标题**: Opencloud – An alternative to Nextcloud written in Go

**原文链接**: [https://github.com/opencloud-eu/opencloud](https://github.com/opencloud-eu/opencloud)

生成摘要时出错

---

## 75. Let's Unify Linux Desktops

**原文标题**: Let's Unify Linux Desktops

**原文链接**: [https://www.theregister.com/2025/11/10/deduplicating_the_desktops/](https://www.theregister.com/2025/11/10/deduplicating_the_desktops/)

生成摘要时出错

---

## 76. Defeating KASLR by doing nothing at all

**原文标题**: Defeating KASLR by doing nothing at all

**原文链接**: [https://googleprojectzero.blogspot.com/2025/11/defeating-kaslr-by-doing-nothing-at-all.html](https://googleprojectzero.blogspot.com/2025/11/defeating-kaslr-by-doing-nothing-at-all.html)

生成摘要时出错

---

## 77. Ironclad – formally verified, real-time capable, Unix-like OS kernel

**原文标题**: Ironclad – formally verified, real-time capable, Unix-like OS kernel

**原文链接**: [https://ironclad-os.org/](https://ironclad-os.org/)

生成摘要时出错

---

## 78. Python Software Foundation gets a donor surge after rejecting federal grant

**原文标题**: Python Software Foundation gets a donor surge after rejecting federal grant

**原文链接**: [https://thenewstack.io/psf-gets-a-donor-surge-after-rejecting-anti-dei-federal-grant/](https://thenewstack.io/psf-gets-a-donor-surge-after-rejecting-anti-dei-federal-grant/)

生成摘要时出错

---

## 79. Daemon Example in C

**原文标题**: Daemon Example in C

**原文链接**: [https://lloydrochester.com/post/c/unix-daemon-example/](https://lloydrochester.com/post/c/unix-daemon-example/)

生成摘要时出错

---

## 80. Iran faces unprecedented drought as water crisis hits Tehran

**原文标题**: Iran faces unprecedented drought as water crisis hits Tehran

**原文链接**: [https://www.bbc.com/news/articles/cy4p2yzmem0o](https://www.bbc.com/news/articles/cy4p2yzmem0o)

生成摘要时出错

---

## 81. Tabloid: The Clickbait Headline Programming Language

**原文标题**: Tabloid: The Clickbait Headline Programming Language

**原文链接**: [https://tabloid.vercel.app/](https://tabloid.vercel.app/)

生成摘要时出错

---

## 82. Show HN: Hephaestus – Autonomous Multi-Agent Orchestration Framework

**原文标题**: Show HN: Hephaestus – Autonomous Multi-Agent Orchestration Framework

**原文链接**: [https://github.com/Ido-Levi/Hephaestus](https://github.com/Ido-Levi/Hephaestus)

生成摘要时出错

---

## 83. Toolkit to help you get started with Spec-Driven Development

**原文标题**: Toolkit to help you get started with Spec-Driven Development

**原文链接**: [https://github.com/github/spec-kit](https://github.com/github/spec-kit)

生成摘要时出错

---

## 84. Largest cargo sailboat completes first Atlantic crossing

**原文标题**: Largest cargo sailboat completes first Atlantic crossing

**原文链接**: [https://www.marineinsight.com/shipping-news/worlds-largest-cargo-sailboat-completes-historic-first-atlantic-crossing/](https://www.marineinsight.com/shipping-news/worlds-largest-cargo-sailboat-completes-historic-first-atlantic-crossing/)

生成摘要时出错

---

## 85. LLMs are steroids for your Dunning-Kruger

**原文标题**: LLMs are steroids for your Dunning-Kruger

**原文链接**: [https://bytesauna.com/post/dunning-kruger](https://bytesauna.com/post/dunning-kruger)

生成摘要时出错

---

## 86. Startups are pushing the boundaries of reproductive genetics

**原文标题**: Startups are pushing the boundaries of reproductive genetics

**原文链接**: [https://www.wsj.com/tech/biotech/genetically-engineered-babies-tech-billionaires-6779efc8](https://www.wsj.com/tech/biotech/genetically-engineered-babies-tech-billionaires-6779efc8)

生成摘要时出错

---

## 87. How to maintain good vision amidst the myopia epidemic

**原文标题**: How to maintain good vision amidst the myopia epidemic

**原文链接**: [https://ssathe.substack.com/p/vision-in-the-digital-age](https://ssathe.substack.com/p/vision-in-the-digital-age)

生成摘要时出错

---

## 88. Cloudflare scrubs Aisuru botnet from top domains list

**原文标题**: Cloudflare scrubs Aisuru botnet from top domains list

**原文链接**: [https://krebsonsecurity.com/2025/11/cloudflare-scrubs-aisuru-botnet-from-top-domains-list/](https://krebsonsecurity.com/2025/11/cloudflare-scrubs-aisuru-botnet-from-top-domains-list/)

生成摘要时出错

---

## 89. My Git history was a mess of 'update' and 'fix' – so I made AI clean it up

**原文标题**: My Git history was a mess of 'update' and 'fix' – so I made AI clean it up

**原文链接**: [https://github.com/f/git-rewrite-commits](https://github.com/f/git-rewrite-commits)

生成摘要时出错

---

## 90. Show HN: Sparktype – a CMS and SSG that runs entirely in the browser

**原文标题**: Show HN: Sparktype – a CMS and SSG that runs entirely in the browser

**原文链接**: [https://app.sparktype.org](https://app.sparktype.org)

生成摘要时出错

---

## 91. Study identifies weaknesses in how AI systems are evaluated

**原文标题**: Study identifies weaknesses in how AI systems are evaluated

**原文链接**: [https://www.oii.ox.ac.uk/news-events/study-identifies-weaknesses-in-how-ai-systems-are-evaluated/](https://www.oii.ox.ac.uk/news-events/study-identifies-weaknesses-in-how-ai-systems-are-evaluated/)

生成摘要时出错

---

## 92. I Am Mark Zuckerberg

**原文标题**: I Am Mark Zuckerberg

**原文链接**: [https://iammarkzuckerberg.com/](https://iammarkzuckerberg.com/)

生成摘要时出错

---

## 93. Custom doorbell app with Home Assistant and WebRTC

**原文标题**: Custom doorbell app with Home Assistant and WebRTC

**原文链接**: [https://www.naps62.com/posts/custom-doorbell-app-with-homeassistant](https://www.naps62.com/posts/custom-doorbell-app-with-homeassistant)

生成摘要时出错

---

## 94. AI isn't replacing jobs. AI spending is

**原文标题**: AI isn't replacing jobs. AI spending is

**原文链接**: [https://www.fastcompany.com/91435192/chatgpt-llm-openai-jobs-amazon](https://www.fastcompany.com/91435192/chatgpt-llm-openai-jobs-amazon)

生成摘要时出错

---

## 95. Show HN: Trilogy Studio, open-source browser-based SQL editor and visualizer

**原文标题**: Show HN: Trilogy Studio, open-source browser-based SQL editor and visualizer

**原文链接**: [https://trilogydata.dev/trilogy-studio-core/#screen=dashboard-import&import=https%3A%2F%2Ftrilogy-data.github.io%2Ftrilogy-public-models%2Fstudio%2Fdemo-model.json&dashboard=demo_dashboard&modelName=demo-model&connection=duckdb](https://trilogydata.dev/trilogy-studio-core/#screen=dashboard-import&import=https%3A%2F%2Ftrilogy-data.github.io%2Ftrilogy-public-models%2Fstudio%2Fdemo-model.json&dashboard=demo_dashboard&modelName=demo-model&connection=duckdb)

生成摘要时出错

---

## 96. Debugging BeagleBoard USB boot with a sniffer: fixing omap_loader on modern PCs

**原文标题**: Debugging BeagleBoard USB boot with a sniffer: fixing omap_loader on modern PCs

**原文链接**: [https://www.downtowndougbrown.com/2025/11/debugging-beagleboard-usb-boot-with-a-sniffer-fixing-omap_loader-on-modern-pcs/](https://www.downtowndougbrown.com/2025/11/debugging-beagleboard-usb-boot-with-a-sniffer-fixing-omap_loader-on-modern-pcs/)

生成摘要时出错

---

## 97. The Return of Language-Oriented Programming

**原文标题**: The Return of Language-Oriented Programming

**原文链接**: [https://blog.evacchi.dev/posts/2025/11/09/the-return-of-language-oriented-programming/](https://blog.evacchi.dev/posts/2025/11/09/the-return-of-language-oriented-programming/)

生成摘要时出错

---

## 98. Open-source communications by bouncing signals off the Moon

**原文标题**: Open-source communications by bouncing signals off the Moon

**原文链接**: [https://open.space/](https://open.space/)

生成摘要时出错

---

## 99. Mullvad: Shutting down our search proxy Leta

**原文标题**: Mullvad: Shutting down our search proxy Leta

**原文链接**: [https://mullvad.net/en/blog/shutting-down-our-search-proxy-leta](https://mullvad.net/en/blog/shutting-down-our-search-proxy-leta)

生成摘要时出错

---

## 100. A software synthesizer modellled on Yevgeny Murzin's ANS synthesizer

**原文标题**: A software synthesizer modellled on Yevgeny Murzin's ANS synthesizer

**原文链接**: [https://github.com/frankenbeans/MZ2SYNTH](https://github.com/frankenbeans/MZ2SYNTH)

生成摘要时出错

---

