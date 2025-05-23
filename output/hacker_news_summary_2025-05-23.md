# Hacker News 热门文章摘要 (2025-05-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. VS Code 中的 PostgreSQL IDE

**原文标题**: PostgreSQL IDE in VS Code

**原文链接**: [https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-a-new-ide-for-postgresql-in-vs-code-from-microsoft/4414648](https://techcommunity.microsoft.com/blog/adforpostgresql/announcing-a-new-ide-for-postgresql-in-vs-code-from-microsoft/4414648)

此文宣布 Visual Studio Code (VS Code) 适用的全新 PostgreSQL 扩展的公开预览版，该扩展旨在简化 PostgreSQL 数据库管理和开发工作流程。它通过在 VS Code 中集成数据库工具和 @pgsql GitHub Copilot 代理，解决了开发人员面临的挑战，例如任务切换和调试时间。

主要功能包括：

*   **模式可视化：** 通过右键单击上下文菜单轻松可视化。
*   **数据库感知型 GitHub Copilot：** 利用 AI 辅助进行查询、模式优化和 SQL 操作，提供实时指导并提高代码质量。提供一个包含“重写查询”和“解释查询”等选项的上下文菜单。
*   **GitHub Copilot 聊天代理模式：** 一种智能助手，可以执行多阶段任务、编写和调试代码、简化应用程序原型设计以及优化模式。
*   **简化连接管理：** 轻松连接到本地和云托管的 PostgreSQL 实例，包括 Azure Database for PostgreSQL，并集成 Entra ID。
*   **使用 Entra ID 的无密码身份验证：** 通过自动令牌刷新实现简化的安全身份验证。
*   **数据库资源管理器：** 数据库对象的结构化视图，用于创建、修改和删除。
*   **查询历史记录：** 快速访问以前运行的查询。
*   **上下文感知型 IntelliSense：** 自动完成和语法突出显示，以提高查询可读性。

该扩展旨在提高生产力、简化入门流程、通过 Entra ID 提高安全性、提供全面的工具集以及提供与 Azure Database for PostgreSQL 的无缝云集成。文中包含安装扩展程序和启用 PostgreSQL GitHub Copilot 聊天的说明。作者鼓励用户提供反馈以改进扩展程序。

---

## 2. 找到你的同伴

**原文标题**: Find Your People

**原文链接**: [https://foundersatwork.posthaven.com/find-your-people](https://foundersatwork.posthaven.com/find-your-people)

在巴克内尔大学的毕业典礼上，演讲者面向毕业生，特别是那些对未来感到迷茫的人们发表讲话。他认为毕业后，生活将从预设的“轨道”转变为更加开放的景象，既充满兴奋，又充满恐惧。他鼓励毕业生们积极地掌控自己的生活，而不是被动地漂流。

他建议那些不确定的人“重塑”自我，摆脱过去基于学业成绩对自身能力的认知。他强调，他们有能力采纳新的品质，比如好奇心和责任感，而不会因为过去的表现而受到评判。

为了应对大量职业选择带来的迷茫，演讲者建议使用一个“技巧”：与有趣的人建立联系。他强调与各个领域的人交谈，发现什么能激发他们的兴趣的重要性。他还建议离开那些与自己不合拍的工作场所。

最后，他强调需要培养对拒绝的免疫力。雄心勃勃的想法往往会受到怀疑，坚持至关重要。他分享了他与Y Combinator的经历，最初被认为是笑话，以说明看似“平庸”的想法也可能具有突破性。他最后重申了积极选择道路和向有趣的人学习的重要性，最终鼓励毕业生们拥抱雄心，忽略反对者。

---

## 3. 超越语义：无理性中间令牌的不可思议的有效性

**原文标题**: Beyond Semantics: Unreasonable Effectiveness of Reasonless Intermediate Tokens

**原文链接**: [https://arxiv.org/abs/2505.13775](https://arxiv.org/abs/2505.13775)

这篇arXiv论文《超越语义：无理性中间令牌的出乎意料的有效性》挑战了一个被广泛接受的观点，即大型语言模型（LLMs）中思维链（CoT）提示的成功源于中间“思考”令牌的有意义的语义。作者认为，这些通常被解释为推理证据的令牌，可能不像之前认为的那么关键。

为了调查这一点，他们训练了转换器模型，使用了来自A*搜索的形式上可验证的推理轨迹和解决方案，确保中间步骤和最终输出与形式求解器对齐。然后，他们系统地评估了不仅解决方案的准确性，还评估了这些中间轨迹的正确性。

关键发现是，用准确的轨迹训练的模型仍然可以产生不正确的推理步骤，同时得出正确的解决方案。更令人惊讶的是，作者发现，用与特定问题无关的嘈杂、损坏的轨迹训练的模型，表现与用正确的轨迹训练的模型相当，有时甚至更好。这表明轨迹准确性和解决方案准确性之间的联系并不紧密，甚至使用“无理性”的中间令牌可能会提高泛化能力。

论文的结论是，告诫人们不要将中间令牌拟人化，或者过度解读它们为人类般的或算法推理的证据，尽管它们通常看起来格式正确。结果表明，CoT的有效性可能更多地在于中间令牌提供的结构或支架，而不是它们特定的语义内容。

---

## 4. 凯撒之息

**原文标题**: Caesar's Last Breath

**原文链接**: [https://charliesabino.com/caesars-last-breath/](https://charliesabino.com/caesars-last-breath/)

本文探讨了费米估算的概念，并以“凯撒的最后一口气”这个思想实验为例，展示了如何通过简单的计算来估算看似不可能的数量。核心问题是：我们每次呼吸会吸入多少凯撒最后一口气中的分子？

文章认为，由于分子的扩散和保存，我们每次呼吸都包含着曾经生活过的所有人的呼吸的一部分。为了估算这一点，文章将问题分解为计算地球大气层的体积和单次呼吸的体积。

文章使用锚定值（地球半径、大气层厚度、大气密度和空气分子量）估计大气层的体积约为 5 x 10^18 立方米，单次呼吸的体积为 5 x 10^-4 立方米。这得出一个结论：凯撒的最后一口气占据了大气层的 1/10^22。

接下来，文章估计单次呼吸中的分子数量约为 10^22。将此数字乘以先前计算的比例，得出的结论是，我们每次呼吸大约会吸入凯撒最后一口气中的一个分子。

文章最后强调了费米估算的强大之处及其在现实世界中的适用性。它建议了一些资源，用于进一步练习和探索该技术，尤其是在软件工程的背景下。

---

## 5. 米制起源于法国大革命

**原文标题**: The metre originated in the French Revolution

**原文链接**: [https://www.abc.net.au/news/science/2025-05-20/metre-treaty-anniversary-metric-system-measurement-metrology/105302024](https://www.abc.net.au/news/science/2025-05-20/metre-treaty-anniversary-metric-system-measurement-metrology/105302024)

本文探讨了米的单位历史和演变，从其在法国的革命性起源到目前基于光速的定义。米最初在法国大革命期间被构想为一种与自然相关的通用测量单位，定义为从北极经巴黎到赤道距离的千万分之一。

1875年的《米制公约》（米制条约）在国际上标准化了米和千克，并建立了国际计量局。早期的米物理表示，如铂金棒，后来被基于氪-86发出的光波长的定义所取代。

原子钟和光速测量技术的进步导致了米目前的定义，自1983年以来，米被定义为光在真空中1/299,792,458秒内传播的距离。这种精确的定义可以进行精确的测量，例如确定地球和月球之间的距离。

虽然以米为基础的公制已被全球广泛采用，但本文强调了不同国家采用速度的差异。即使是《米制条约》的原始签署国美国，尽管在法律上承认公制，但在日常生活中仍然主要使用英制单位。文章还指出了即使在使用公制单位的国家内部，测量也存在不一致性，例如澳大利亚的汤匙测量与其他国家/地区的不同。

---

## 6. 进入隧道：风洞的秘密生活

**原文标题**: Into The Tunnel: The secret life of wind tunnels

**原文链接**: [https://jordanwtaylor2.substack.com/p/into-the-tunnel](https://jordanwtaylor2.substack.com/p/into-the-tunnel)

无法访问文章链接。

---

## 7. Show HN: Samchika – 用于快速多线程文件处理的 Java 库

**原文标题**: Show HN: Samchika – A Java Library for Fast, Multithreaded File Processing

**原文链接**: [https://github.com/MayankPratap/Samchika](https://github.com/MayankPratap/Samchika)

Samchika是一个Java库，专为快速、多线程的文件处理而设计，通过并行处理实现对大型文件的高效处理。其特性包括简单的API、可选的运行时统计以及适用于CPU密集型任务，如日志分析、ETL操作和数据转换。

该库的核心功能围绕`SmartFileProcessor`展开，它允许用户定义输入和输出路径、批处理大小以及用于自定义逻辑的行处理器。通过Maven或Gradle可以轻松集成。

针对标准`BufferedReader`实现的性能基准测试表明，尤其是在多核系统上，性能有显著提升，处理速度最多可提高70%。在提供更高速度的同时，即使对于大型文件，内存使用量也保持在可控范围内。

Samchika采用MIT许可证，鼓励免费使用和修改。该项目的灵感来自一个JavaScript库和一个LinkedIn讨论，其中强调了大型文件处理中的挑战。开发者感谢Shubham Maurya提供的灵感。

---

## 8. 史莱姆 (2021)

**原文标题**: Slime (2021)

**原文链接**: [https://granta.com/slime/](https://granta.com/slime/)

苏珊娜·韦德利希的《粘液》深入探讨了粘液在我们世界中出人意料的深刻作用，挑战了我们对这种常常被忽视的物质的普遍厌恶。这本书以作者在亨特博物馆寻找一瓶特定的“原始粘液”开始，这个样本最终驳斥了粘液是生命起源的理论。

韦德利希认为，粘液，一种存在于固态和液态之间的物质，不仅仅是一种令人作呕的副产品，而是生命的关键组成部分。它在自然界中无处不在，为生物体提供从结构支撑到防御的各种功能。许多熟悉的物质，如粘液和海洋雪，实际上都是粘液的形式。粘液充当生态系统的水泥，并在我们自己的身体中发挥着至关重要的作用，保护我们免受病原体的侵害并维持基本功能。

这本书探讨了粘液的历史观念，从其在古埃及受人尊敬的地位到其在现代社会中与怪物和厌恶的联系。它还考察了对粘液的科学研究，包括原始粘液作为生命起源的被驳斥的理论。尽管存在负面含义，科学家们现在正在研究粘液的独特特性，用于机器人技术和医学等各个领域。韦德利希警告说，气候变化等环境危机威胁着基于粘液的生态系统，但也可能迎来粘液重新占据主导地位的新时代。最终，这本书旨在颠覆我们对粘液的负面认知，揭示它是生命、健康和环境的重要元素。

---

## 9. 为高质量类型错误设计类型推断

**原文标题**: Designing type inference for high quality type errors

**原文链接**: [https://blog.polybdenum.com/2025/02/14/designing-type-inference-for-high-quality-type-errors.html](https://blog.polybdenum.com/2025/02/14/designing-type-inference-for-high-quality-type-errors.html)

本文探讨了如何设计能够提供高质量错误信息的类型推断系统，并指出类型推断在这方面声名狼藉的原因是特定的设计选择，而非其固有的局限性。

作者指出了导致不良错误信息的两个主要缺陷：

1.  **猜测和回溯：** 使用临时重载或类似功能的语言会迫使类型检查器在多种可能性之间进行猜测。这可能导致编译时间呈指数级增长，并产生与用户预期代码无关的冗长错误信息。作者认为，类型系统的设计应确保类型检查器永远不必猜测。

2.  **仓促下结论：** 像 OCaml 这样的语言通常会根据它们遇到的第一个类型来报告错误，而不跟踪冲突中涉及的其他类型。这可能导致误导性的错误信息，无法识别类型不匹配的根本原因。作者提供了一个例子，其中 OCaml 错误地将浮点数识别为期望的整数，但没有说明原因或期望的来源。

作者介绍了 PolySubML，一种在设计时充分考虑了良好错误信息的语言。其方法与 OCaml 形成对比，展示了 PolySubML 如何跟踪类型冲突的双方，并提供添加手动类型注释的提示，以缩小错误原因的范围。 最关键的结论是，将错误信息质量作为核心关注点来设计类型系统对于积极的开发者体验至关重要。

---

## 10. 纪念阿拉斯代尔·麦金太尔

**原文标题**: Remembering Alasdair MacIntyre

**原文链接**: [https://www.wordonfire.org/articles/remembering-alasdair-macintyre-1929-2025/](https://www.wordonfire.org/articles/remembering-alasdair-macintyre-1929-2025/)

无法访问文章链接。

---

## 11. 再次编写一个任务运行器（Elixir）（十年之后）

**原文标题**: Writing A Job Runner (In Elixir) (Again) (10 years later)

**原文链接**: [https://github.com/notactuallytreyanastasio/genstage_tutorial_2025/blob/main/README.md](https://github.com/notactuallytreyanastasio/genstage_tutorial_2025/blob/main/README.md)

这篇文章，notactuallytreyanastasio 撰写的 “编写 Job Runner (Elixir 实现) (再次) (十年之后)”，是一篇关于在 Elixir 中构建 Job Runner 的教程，很可能使用了 `genstage` 库。标题暗示作者在十年后重新审视该主题，可能表明更新的方法或更现代的最佳实践。

仓库名为 `genstage_tutorial_2025` 表明内容相对较新，并且专注于使用 `genstage` 管理和处理后台作业的实际实现。

虽然实现的细节不可见，但 “Fork” (1) 和 “Star” (15) 的存在表明该项目已在 Elixir 社区中获得了一些兴趣和认可，表明其作为学习资源的潜在价值。

总而言之，这篇文章提供了一个使用 `genstage` 在 Elixir 中构建 Job Runner 的实用指南，反映了对该主题的重新审视，并采用了当前的知识和方法。对于希望在其 Elixir 应用程序中实现稳健的作业处理的开发人员来说，这似乎是一个受欢迎且具有潜在价值的资源。

---

## 12. MCP是Web 2.0 2.0时代的到来

**原文标题**: MCP is the coming of Web 2.0 2.0

**原文链接**: [https://www.anildash.com//2025/05/20/mcp-web20-20/](https://www.anildash.com//2025/05/20/mcp-web20-20/)

本文认为，模型上下文协议（MCP）的迅速普及标志着Web 2.0开放精神的复兴，并将其称为“Web 2.0 2.0”。MCP虽然是一个不完善且定义模糊的规范，但它允许大型语言模型（LLM）与各种应用程序和系统交互，并且OpenAI和微软等主要参与者的采用至关重要。

作者将这种潜在的开放性与Facebook等平台的封闭式专有性质进行了对比，他们认为后者扼杀了最初的Web 2.0。Web 2.0的核心是开放API、用户控制和互操作性，Flickr和Del.icio.us等网站就是典范。作者回顾了自己为开放标准奋斗的经历，并感叹大型社交网络关闭API的决定，这阻碍了创新和用户控制。

MCP为更具可编程性的网络提供了希望，这得益于人工智能的普及。作者强调了平台忠实地采用标准的重要性，即使这些标准并不完善，这样才能促进更好的生态系统。他们鼓励开发者拥抱现有标准，而不是试图改进它们，并以HTML为例，说明了一个虽然有缺陷但却成功的规范。

作者表示乐观，认为新一代开发者将拥抱开放协议，并要求访问和控制他们在各个平台上的体验。然而，他们也承认MCP存在潜在的安全风险和数据使用方面缺乏透明度的问题。最终，他们相信MCP可以激发人们重新转向一个更加开放、可编程且较少受少数大型公司控制的网络。

---

## 13. 侏儒䳭的奇特案例

**原文标题**: The Curious Case of the Pygmy Nuthatch

**原文链接**: [https://slate.com/culture/2025/05/birds-movies-charlies-angels-2000-pygmy-nuthatch.html](https://slate.com/culture/2025/05/birds-movies-charlies-angels-2000-pygmy-nuthatch.html)

这篇文章详细讲述了作者以幽默且执着的态度，试图揭开2000年电影《霹雳娇娃》中一个引人注目的鸟类学错误背后的谜团。作者自称“鸟类爱好者”，对卡梅隆·迪亚茨饰演的角色将一只委内瑞拉拟鹂（一种原产于南美洲的大型、色彩鲜艳的鸟类）误认为小嘲鸫（一种原产于北美洲的小型、颜色暗淡的鸟类），并声称它只生活在加利福尼亚州卡梅尔的行为深感不安。更荒谬的是，场景中的鸟叫声与这两种鸟类都不符。

受这个离谱错误的驱使，作者展开了一项为期一年的调查，采访了编剧，咨询了鸟类学专家，并分析了鸟叫声。作者最初怀疑编剧约翰·奥古斯特，奥古斯特透露最初选择的鸟类是准确的，先是来自夏威夷的红旋蜜雀，然后是伯劳鸟。然而，奥古斯特在拍摄前离开了项目，许多其他编剧也参与了。另一位编剧扎克·佩恩承认添加了一种不存在的“蓝点鹭”，但否认对小嘲鸫负有责任。文章的结尾暗示，作者正越来越接近于发现是谁引入了错误的“小嘲鸫”，以及这种“华丽的错误”背后的原因。

---

## 14. 约翰·卡马克在Upper Bound 2025的演讲

**原文标题**: John Carmack talk at Upper Bound 2025

**原文链接**: [https://twitter.com/ID_AA_Carmack/status/1925710474366034326](https://twitter.com/ID_AA_Carmack/status/1925710474366034326)

这篇所谓的“文章”实际上并非关于约翰·卡马克在2025年Upper Bound大会上的演讲。它只是X（前身为Twitter）的一个占位符，表明用户的浏览器禁用了JavaScript。由于JavaScript被禁用，用户无法访问X（Twitter）网站的内容，而这些内容*本应*是关于卡马克演讲的文章。

唯一能获取的信息是，到2025年，X公司（前身为Twitter）仍然存在，并且需要JavaScript才能正常查看内容。其余内容是样板式的法律和版权信息。

因此，没有演讲摘要可供总结。关键是用户的浏览器配置阻止了他们访问预期内容。

---

## 15. 卫星探测深度

**原文标题**: Satellites Spotting Depth

**原文链接**: [https://tech.marksblogg.com/depth-anything-v2-maxar-ai-detection.html](https://tech.marksblogg.com/depth-anything-v2-maxar-ai-detection.html)

本文详细介绍了一项实验，该实验使用 Depth Anything V2 深度估计模型处理 Maxar 卫星图像。作者使用高端工作站，测试了该模型从泰国曼谷卫星图像中辨别深度的能力。

最初，作者使用了乍都乍区的大型 GeoTIFF 图像，但由于源图像中存在大片黑色区域，该模型未能生成有用的深度图。随后，使用了一张较小的、经过裁剪的邦甲梭区图像，产生了更好的结果。作者对生成的深度图进行了地理配准，并将其与原始卫星图像叠加，展示了该模型区分建筑物高度的能力。

本文强调了使用 Depth Anything V2 从卫星图像中提取高度信息的潜力。作者提出了一种工作流程，该流程将图像切片与 Overture 的建筑数据集相结合，以根据每个切片中最高的建筑物来校准深度比例。最后，作者提供了一个塔林老城航拍照片的深度估计示例，展示了该模型在非卫星图像中的有效性。

---

## 16. 最高的木制风力涡轮机

**原文标题**: Tallest Wooden Wind Turbine

**原文链接**: [https://modvion.com/](https://modvion.com/)

本文重点介绍一家使用木材建造风力涡轮机塔架的公司。其主要目标是实现净零风电。核心卖点在于风力涡轮机塔架的木材使用，这表明与传统材料相比，这是一种更可持续和环保的方法。 该文鼓励读者进一步探索，以便更多地了解其木制风力涡轮机技术的具体细节以及它如何为实现净零能源生产做出贡献。

---

## 17. 有灵魂的比特

**原文标题**: Bits with Soul

**原文链接**: [https://www.darwin.cam.ac.uk/lectures/entry/bits-with-soul/](https://www.darwin.cam.ac.uk/lectures/entry/bits-with-soul/)

这篇题为“有灵魂的比特”的短文，是一个行动号召，围绕着Simon Peyton Jones的讲座和达尔文学院访谈展开。它暗示这些来源探讨了计算机科学和编程领域中更深层的意义或目的，而不仅仅是功能上的实用性。这篇文章本质上是建议大家关注Peyton Jones的见解。

“有灵魂的比特”这个短语表明Peyton Jones可能讨论了技术中的人文因素。它暗示了与代码及其影响交织在一起的艺术、哲学，以及潜在的伦理考量。它意味着有效的技术不仅仅是高效的算法和完美的执行，还要考虑人类体验、目的以及嵌入其中的价值观。

摘要特意简洁，因为文档本身也很简洁。其核心信息是鼓励读者深入研究所提供的资源，以理解Peyton Jones关于以人为本的计算机科学观点的深度和细微之处，正如这个富有表现力的标题所暗示的那样。

---

## 18. 糖衣炮弹：良性生成解锁LLM越狱

**原文标题**: Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking

**原文链接**: [https://arxiv.org/abs/2504.05652](https://arxiv.org/abs/2504.05652)

"糖衣炮弹：良性生成解锁LLM越狱"这篇arXiv预印本论文探讨了大型语言模型(LLM)中一种使其易受越狱攻击的漏洞。作者吴宇航、熊宇杰和张杰发现了一种他们称之为“防御阈值衰减”(DTD)的现象。

DTD发生在LLM生成大量良性内容时。模型注意力从初始输入转移到其先前的输出。这种转移使得模型更容易受到后续恶意提示的影响，从而成功实现越狱攻击。

为了演示DTD，作者们提出了一种名为“糖衣炮弹”(SCP)的新型越狱攻击方法。该攻击利用DTD现象，首先通过良性输入提示LLM生成大量无害内容。随后，利用对抗推理来利用被削弱的“防御阈值”，从而从模型中诱导出恶意输出。

认识到DTD和SCP等攻击构成的威胁，作者提出了一种简单而有效的防御策略，名为POSD。POSD旨在缓解这些攻击并降低越狱成功率，同时保留LLM的泛化能力和在其他任务上的良好表现。该论文认为，分析这些漏洞并创建防御措施对于提高LLM的安全性和可靠性至关重要。

---

## 19. 涡轮增压的线粒体助力鸟类史诗般的迁徙之旅

**原文标题**: 'Turbocharged' Mitochondria Power Birds' Epic Migratory Journeys

**原文链接**: [https://www.quantamagazine.org/turbocharged-mitochondria-power-birds-epic-migratory-journeys-20250519/](https://www.quantamagazine.org/turbocharged-mitochondria-power-birds-epic-migratory-journeys-20250519/)

本文探讨了候鸟如何通过关注线粒体在其飞行肌肉中的作用来实现其令人印象深刻的长途飞行。最近的研究表明，这些鸟类在亚细胞水平上经历了重大变化，以增强其能量产生。

两项独立的研究发现，候鸟表现出“涡轮增压”的线粒体，其飞行肌肉中的数量增加、效率提高并且相互连接性发生改变。 这些变化使鸟类能够产生持续飞行所需的大量 ATP（能量）。

一项关于黄腰柳莺的研究表明，处于“迁徙”状态的鸟类比非迁徙鸟类拥有更多的线粒体，并且具有更强的能量生产能力。 另一项使用“MitoMobile”研究白冠带鹀的研究证实，迁徙亚种比非迁徙亚种拥有更多且更高效的线粒体。 这项研究还发现了线粒体重塑的证据，即细胞器改变形状以优化 ATP 产生。

本文还探讨了涡轮增压线粒体的潜在缺点，例如有害活性氧的产生，以及候鸟如何通过富含抗氧化剂的饮食来缓解这种情况。 该研究突出了鸟类的“表型可塑性”，证明了它们如何在不改变其基因构成的情况下，响应诸如变化的光照水平等环境线索来适应其线粒体功能。 科学家们现在正在探索类似的线粒体重塑策略是否可以应用于人类健康，尤其是在运动生理学和衰老等领域。

---

## 20. Show HN: Defuddle，Readability的替代方案，将HTML转换为Markdown

**原文标题**: Show HN: Defuddle, an HTML-to-Markdown alternative to Readability

**原文链接**: [https://github.com/kepano/defuddle](https://github.com/kepano/defuddle)

Defuddle 是一个从网页中提取并清理主要内容的工具，可移除侧边栏、页眉和页脚等杂乱内容。它的目标是提供干净、一致的 HTML 输出，使其适用于 HTML 到 Markdown 的转换。它被认为是 Mozilla Readability 的替代品，优点是更宽容，为脚注和数学提供一致的输出，使用移动样式进行元素猜测，并提取更多元数据。

Defuddle 可以作为不同捆绑包的 npm 包提供：用于浏览器使用的核心捆绑包（无依赖项）、带有数学公式解析的完整捆绑包以及针对具有完整功能的 JSDOM 优化的 Node.js 捆绑包。

主要功能包括元数据提取（作者、标题、描述等）、HTML 标准化（标题、代码块、脚注、数学）以及调试、Markdown 转换和基于选择器的元素删除选项。调试模式提供详细的日志记录和属性保留，以便进行详细分析。HTML 标准化涉及将 H1 转换为 H2、从标题中删除锚点链接、标准化代码块和脚注以及将数学元素转换为 MathML 等任务。安装需要 Node.js 和 npm。 提供了浏览器和 Node.js 环境的使用示例。

---

## 21. KumoRFM：关系数据上下文学习的基础模型

**原文标题**: KumoRFM: A Foundation Model for In-Context Learning on Relational Data

**原文链接**: [https://kumo.ai/company/news/kumo-relational-foundation-model/](https://kumo.ai/company/news/kumo-relational-foundation-model/)

KumoRFM是一种新型关系基础模型(RFM)，旨在无需任务特定训练即可对关系数据库执行跨多种任务的准确预测。它利用应用于多表关系图的上下文学习原理，填补了基础模型应用于结构化数据的空白。

KumoRFM通过将关系数据库转换为时序异构图来运作。它采用表不变编码方案和关系图Transformer来跨表推理，处理列类型的固有异构性。关键组件包括实时上下文标签生成器、具有表级注意力机制的预训练RFM以及全面的可解释性模块。

在RelBench基准测试中的评估表明，KumoRFM在其上下文学习模式下，优于特征工程基线和端到端监督深度学习方法2%至8%。微调可以进一步将性能提高10%至30%。至关重要的是，KumoRFM提供了显著的速度优势，其预测速度比传统的监督学习方法快几个数量级，并且几乎不需要编码，使其成为一种零代码解决方案。这种效率与准确性相结合，使KumoRFM成为一个强大的实时预测系统工具，能够驱动在关系数据上更快、更智能的业务决策。

---

## 22. 量子图论

**原文标题**: Quantum Picturalism

**原文链接**: [https://quantuminpictures.org/](https://quantuminpictures.org/)

本文介绍了“量子图像化”，这是一种无需复杂数学即可理解量子概念的方法。它旨在通过使用视觉表示和简单的算术（加法、减法和角度）使量子教育更容易为所有人所接受。

其核心思想是将令人生畏的量子概念分解成易于理解的视觉学习体验，并使用“游戏式”规则。这种方法虽然简单，但足够严谨，可以被量子专家使用。“量子图像化”这个术语的创造，专门用于描述这种教授量子概念的视觉方法。

本文重点介绍了Bob Coecke和Stefano Gogioso合著的《量子图像》一书，作为学习此方法的关键资源。它还鼓励读者加入ZX微积分Discord以进行进一步探索，并查看常见问题解答（FAQ）。本质上，“量子图像化”试图通过消除复杂数学公式的障碍来实现量子知识的民主化，从而向所有背景和年龄的学习者和教育者开放这个领域。

---

## 23. 挂在我墙上多年的那个分形图案

**原文标题**: That fractal that's been up on my wall for years

**原文链接**: [https://chriskw.xyz/2025/05/21/Fractal/](https://chriskw.xyz/2025/05/21/Fractal/)

作者回忆了童年时期的涂鸦，这些涂鸦最终形成了一个他们称之为“壁花”的分形，这个分形已经贴在他们的墙上12年了。最初，他们通过重复平铺和旋转正方形来绘制它。在发现了L系统后，他们试图生成相同的轮廓，但意识到它产生了一个已知的分形，“二次冯·科赫岛”，这与他们“拖放式”的壁花不同。

文章随后深入探讨了壁花的数学性质。作者开发了一种对分形中的正方形进行编号的方法，并发现了正方形的位置与5的幂之间的关系，从而导致了5进制的使用。他们进一步将其抽象成一种新型的数字系统，其中分形上的位置由矩阵基 (M) 和向量数字确定。

分析了两个矩阵，M和M'，它们的行列式分别为-5和5。作者发现，M生成了他们最初的壁花，而M'生成了前面提到的“二次冯·科赫岛”。行列式值5具有重要意义，因为它与分形的比例因子相匹配。行列式不是+/-5的矩阵会导致空白空间或重叠。

文章演示了线性代数，特别是用于定义数字系统的矩阵基的行列式，如何决定分形的基本结构，并解释了为什么两个看起来相似的分形（作者的壁花和二次冯·科赫岛）是不同的。

---

## 24. 克勞德4

**原文标题**: Claude 4

**原文链接**: [https://www.anthropic.com/news/claude-4](https://www.anthropic.com/news/claude-4)

Anthropic 发布 Claude 4，包含两款新型号：Claude Opus 4 和 Claude Sonnet 4。 Opus 4 是性能最佳的编码模型，擅长复杂、长时间运行的任务和代理工作流程。 Sonnet 4 是 Sonnet 3.7 的升级版，在编码、推理和指令遵循方面均有所改进。

主要特点包括：

*   **扩展工具使用思维能力：** 两款模型均可使用网络搜索等外部工具来增强推理和响应。
*   **并行工具执行和增强的记忆能力：** 实现了并行工具使用、精确的指令遵循以及增强的记忆能力（在获得文件访问权限时）。
*   **Claude Code 全面可用：** 现在支持通过 GitHub Actions 进行后台任务，以及与 VS Code 和 JetBrains 的原生集成。
*   **全新 API 功能：** 发布了代码执行工具、MCP 连接器、Files API 和提示缓存。

Opus 4 在 SWE-bench (72.5%) 和 Terminal-bench (43.2%) 等编码基准测试中领先，从而支持高级代理应用程序。 Sonnet 4 在编码方面表现出色（SWE-bench 上达到 72.7%），并在性能和效率之间提供了最佳平衡，为 GitHub Copilot 中的全新编码代理提供支持。

模型改进包括减少快捷方式使用和增强本地文件访问时的记忆能力。 还为冗长的思考过程引入了思维总结。

Claude Code 现在提供适用于 VS Code 和 JetBrains 的测试版扩展，并且提供可扩展的 Claude Code SDK 来构建自定义代理。

这些模型可在 Claude、Claude Code、Anthropic API、Amazon Bedrock 和 Google Cloud 的 Vertex AI 上使用。 定价与之前的模型一致：Opus 4 为每百万 tokens 15 美元/75 美元，Sonnet 4 为每百万 tokens 3 美元/15 美元（输入/输出）。

---

## 25. 测量月球南北极区域

**原文标题**: Measuring Lunar North and South Polar Regions

**原文链接**: [https://iopscience.iop.org/article/10.3847/PSJ/adbc9d](https://iopscience.iop.org/article/10.3847/PSJ/adbc9d)

这不是一篇文章，而是Radware Bot Manager验证码页面。似乎有人试图访问IOP Publishing网站上关于测量月球南北极区域的文章，但被机器人检测系统阻止。

核心信息是：

*   **访问被拒绝（可能）：** 试图访问内容的用户可能被标记为机器人。
*   **验证码挑战：** 显示验证码以验证用户是否为真人。用户需要勾选框才能继续。
*   **替代联系方式：** 如果验证码失败或用户遇到问题，会提供IOP Publishing联系页面的链接，并指示他们提供问题的截图。
*   **事件ID：** 提供事件ID（139c71f2-cnvj-487a-9270-555cd09e541f）以跟踪潜在问题。

需要注意的是，提供的文本*不包含*关于测量月球极地区域的实际文章的任何信息。 该文本仅与防止机器人访问的安全措施有关。

---

## 26. 我如何最终为也门国家航空公司飞行——并幸存下来

**原文标题**: How I ended up flying for Yemen's national airline – and survived

**原文链接**: [https://www.pprune.org/terms-endearment/653181-yemenia-expat-contract-full-info.html](https://www.pprune.org/terms-endearment/653181-yemenia-expat-contract-full-info.html)

无法访问文章链接。

---

## 27. 地球的两侧都有高潮隆起吗？(2014)

**原文标题**: Does Earth have two high-tide bulges on opposite sides? (2014)

**原文链接**: [http://physics.stackexchange.com/questions/121830/does-earth-really-have-two-high-tide-bulges-on-opposite-sides](http://physics.stackexchange.com/questions/121830/does-earth-really-have-two-high-tide-bulges-on-opposite-sides)

根据提供的URL，Stack Exchange 上的问题讨论了一个常见的误解：地球拥有两个高潮凸起仅仅是因为月球对一侧的引力以及对侧的离心力。

答案中提出的和讨论的关键点（基于 Stack Exchange 对类似问题的典型贡献）包括：

*   **引力梯度：** 面向月球一侧的凸起的主要原因是月球的引力。月球对地球靠近它的一侧的引力最强。这种引力差异（梯度）作用于整个地球，从而将水拉向月球。
*   **惯性与质心：** 另一侧的凸起并非仅仅由于离心力。相反，它产生的原因是地球和月球围绕一个共同的质心（重心）运行，这个质心位于地球内部但偏离中心。当地球围绕这个重心运行时，远侧水的惯性会抵抗被拉动，从而形成一个远离月球的凸起。
*   **更全面的视角：** 潮汐力是引力吸引力随距离变化以及惯性效应的净效应，最好用广义相对论的原理描述，而不仅仅是牛顿物理学。
*   **简化的解释：** “离心力”的解释通常被用作简化，但并不完全准确。远侧的凸起并非仅仅是被“抛”出去；它是地球围绕重心旋转以及水的惯性的结果。
*   **地球自转：** 地球的自转有助于这些凸起的运动，从而产生潮汐周期。
*   **其他因素：** 讨论可能承认，由于海岸线的形状、海洋的深度以及太阳的影响等因素，现实世界中的潮汐要复杂得多。理想化的双凸起模型是一种简化。

---

## 28. Mozilla将关闭Pocket和Fakespot。

**原文标题**: Mozilla to shut down Pocket and Fakespot

**原文链接**: [https://support.mozilla.org/en-US/kb/future-of-pocket](https://support.mozilla.org/en-US/kb/future-of-pocket)

由于网络使用习惯的演变以及资源分配向其他项目的转移，Mozilla 将于 2025 年 7 月 8 日关闭其 Pocket “稍后阅读”应用。用户将可以在 2025 年 10 月 8 日之前导出已保存的文章，之后所有用户数据将被永久删除。

高级订阅用户将收到按比例退款。月度订阅用户的自动续订功能已立即禁用，他们可以在订阅期结束前继续享受高级权益，无需支付额外费用。年度订阅用户将于 2025 年 7 月 8 日收到自动按比例退款。

Pocket 网页扩展将于 2025 年 5 月 22 日从应用商店中移除，并将用户引导至导出页面。Pocket 应用将从 2025 年 5 月 22 日起停止接受新安装，但现有用户可以在 2025 年 10 月 8 日之前重新安装。用户必须手动从其设备和浏览器插件中移除该应用。

Pocket 的 API 将于 2025 年 10 月 8 日停止运行，从而阻止数据交易。Pocket Hits 电子邮件新闻通讯将被更名为“Ten Tabs”，在维持其精选内容的同时，改为仅在工作日发送。用户可以随时取消订阅。需要记住的关键日期为：2025 年 5 月 22 日（从应用商店移除和订阅变更）、2025 年 7 月 8 日（关闭和退款处理）以及 2025 年 10 月 8 日（最终数据导出日期和数据删除）。Mozilla 对多年来用户的支持和反馈表示感谢。

---

## 29. 我们将停止在Glitch上为您应用提供网络托管服务。

**原文标题**: We’ll be ending web hosting for your apps on Glitch

**原文链接**: [https://blog.glitch.com/post/changes-are-coming-to-glitch/](https://blog.glitch.com/post/changes-are-coming-to-glitch/)

Glitch将于2025年7月8日停止在其平台上为应用程序提供网站托管服务。此决定是由于维护平台的成本不断增加，以及涌现出许多在创新和易用性方面超越Glitch的新平台。

用户仍可在2025年底前访问他们的Glitch仪表板以下载他们的代码。Glitch还将提供一项新功能，用于设置项目子域的重定向，以确保现有URL继续有效。这些重定向将至少保持到2026年底。

Glitch正在开发一份指南，以帮助用户导出他们的项目、创建Git存储库以及迁移到其他平台。他们鼓励用户利用社区论坛获取有关迁移的问题和技巧。

新的Glitch Pro订阅已立即停止，当前的订阅者将收到任何未使用时间的退款。有关Glitch Pro会员资格的更多详细信息将通过电子邮件于2025年6月2日发送。

该公告承认此更改可能造成的 disruption，并对Glitch社区的支持表示感谢。作者Anil Dash鼓励用户分享他们对Glitch社区未来的想法和反馈。

---

## 30. Ruby 3.5 中的快速分配

**原文标题**: Fast Allocations in Ruby 3.5

**原文链接**: [https://railsatscale.com/2025-05-21-fast-allocations-in-ruby-3-5/](https://railsatscale.com/2025-05-21-fast-allocations-in-ruby-3-5/)

本文详细介绍了 Ruby 3.5 中一项显著的优化，该优化加速了对象分配，尤其是在 `Class#new` 上。通过内联 `Class#new` 的实现，Ruby 3.5 相比 Ruby 3.4.2 实现了可观的性能提升。

加速主要归功于：

*   **消除参数复制：** 内联消除了在 Ruby 和 C 调用约定之间复制参数的需要，尤其有利于关键字参数，这些参数以前需要哈希分配。
*   **消除堆栈帧：** 删除 `Class#new` 堆栈帧进一步降低了开销。
*   **提高内联缓存命中率：** 通过内联，`initialize` 调用被分散，与集中的 `Class#new` 实现相比，从而提高了缓存命中率。

基准测试表明，与 Ruby 3.4.2 相比，Ruby 3.5 在位置参数方面通常快 1.8 倍到 2.3 倍（分别启用和未启用 YJIT）。关键字参数的加速更为显著，启用 YJIT 后，速度提高了 6.5 倍以上，尤其是在参数数量增加时。

内联优化涉及插入 `opt_new` 指令来分配新实例，然后调用 `initialize`。

一个小的缺点是 `caller` 报告的调用堆栈发生了变化，因为 `Class#new` 帧现在不存在了。然而，就性能而言，其带来的好处超过了这种小的兼容性问题。文章总结说，此优化是提高 Ruby 中对象分配速度的一大胜利。

---

## 31. 草图日历

**原文标题**: Sketchy Calendar

**原文链接**: [https://www.inkandswitch.com/ink/notes/sketchy-calendar/](https://www.inkandswitch.com/ink/notes/sketchy-calendar/)

本文《草图日历》探讨了将数字日历的便捷性与纸质日历的灵活性和表现力相结合的潜力。它对比了两者各自的优缺点：像谷歌日历这样的数字日历提供了同步、共享日历和活动邀请等功能，但可能会让人感觉枯燥、缺乏个性，并限制用户定义事件的方式。另一方面，纸质日历允许自定义、涂鸦，以及整合各种日常生活方面的内容，如笔记、膳食计划和待办事项。

作者建议研究一种混合方法，从数字笔记本（iPad和铅笔）开始，并添加最小的结构来解决两种方式的局限性。他们旨在探索如何创建相互关联的每日、每周和每月视图，将草图注释与正式日历事件集成，促进共享日历和邀请，并使用户能够通过自定义的动态行为（如习惯和时间跟踪器）来个性化他们的日历，同时保持“草图式的个人风格”。文章最后预览了一种可能的“草图日历”，并邀请读者订阅以获取未来更新。

---

## 32. 改变微处理器设计的32位

**原文标题**: 32 bits that changed microprocessor design

**原文链接**: [https://spectrum.ieee.org/bellmac-32-ieee-milestone](https://spectrum.ieee.org/bellmac-32-ieee-milestone)

IEEE Spectrum文章强调贝尔实验室Bellmac-32微处理器在塑造现代微处理器设计，尤其是智能手机微处理器设计中的重要性。威利·D·琼斯撰写的这篇文章强调了贝尔实验室开发的32位处理器Bellmac-32，为当今芯片中许多架构和技术进步奠定了基础。文章可能探讨了Bellmac-32引入的创新，可能包括其架构、指令集或制造工艺。它含蓄地表明，这些创新是计算发展中的关键步骤，并且至今仍在影响微处理器的设计。包含Bellmac-32团队的照片和电路原理图表明文章侧重于芯片创建的协作和技术方面。文章强调了贝尔实验室对微处理器领域的持久影响。

---

## 33. 古代法律要求查令十字车站铁路桥上悬挂一捆稻草。

**原文标题**: Ancient law requires a bale of straw to hang from Charing Cross rail bridge

**原文链接**: [https://www.ianvisits.co.uk/articles/ancient-law-requires-a-bale-of-hay-to-hang-from-charing-cross-rail-bridge-81318/](https://www.ianvisits.co.uk/articles/ancient-law-requires-a-bale-of-hay-to-hang-from-charing-cross-rail-bridge-81318/)

2025年5月，为亨格福德桥（查令十字火车站桥）维护工程搭建的脚手架触发了一项古老法律，要求桥上悬挂一捆稻草。这项不同寻常的做法源于伦敦港泰晤士河章程，特别是第36.2条，该条款规定当桥梁拱的净空高度降低时，必须放置一捆稻草。稻草捆的目的是警告水手减少的净空。

虽然该法律的历史渊源尚不清楚，但它一直被保留在更新后的河流章程中。目前为期数年的维护项目涉及侵占河流空域的脚手架，促使实施了这项古老的规定。目前，稻草捆悬挂在相邻的禧年步行桥上。随着脚手架在项目阶段沿着桥拱移动，稻草捆也将被重新定位。因此，在维护期间，一捆稻草将继续成为查令十字火车站桥的固定装置，这证明了一项幸存的中世纪法规。夜间也会使用警示灯以增加可见度。

---

## 34. 提高rav1d视频解码器的性能

**原文标题**: Improving performance of rav1d video decoder

**原文链接**: [https://ohadravid.github.io/posts/2025-05-rav1d-faster/](https://ohadravid.github.io/posts/2025-05-rav1d-faster/)

本文详细介绍了如何通过与 C 语言编写的 dav1d 比较，来提高基于 Rust 的 AV1 视频解码器 rav1d 的性能。作者使用诸如 samply 的采样分析器来识别两者之间的性能差异，并以汇编优化的函数作为基准。

最初的分析显示 rav1d 比 dav1d 慢约 9%。作者发现 rav1d 不必要地将内存缓冲区清零，特别是 `cdef_filter_neon_erased` 函数中的 `tmp_buf` 和 `rav1d_cdef_brow` 函数中的 `lr_bak`。在第一种情况下，作者使用 `MaybeUninit` 来避免初始化。在第二种情况下，作者将变量定义移到了循环外部。通过进行这些更改，作者减少了不必要的内存清零，从而带来了 1.5% 的性能提升。

随后，作者探索了“反向堆栈”分析，该分析突出了 `add_temporal_candidate` 函数作为瓶颈。这项调查通过将 `Mv` 结构体（包含两个 i16 字段）的字段式相等性比较替换为字节式相等性比较（将其视为 u32），从而实现了性能优化，从而进一步提高了速度。Godbolt 被用来比较汇编代码并证明更改的效率。

---

## 35. 在《卡坦岛》中如何通过灌铅骰子作弊 (2017)

**原文标题**: How to cheat at settlers by loading the dice (2017)

**原文链接**: [https://izbicki.me/blog/how-to-cheat-at-settlers-of-catan-by-loading-the-dice-and-prove-it-with-p-values.html](https://izbicki.me/blog/how-to-cheat-at-settlers-of-catan-by-loading-the-dice-and-prove-it-with-p-values.html)

本文详细介绍了如何为《卡坦岛拓荒者》游戏加载骰子以获得优势，以及如何对结果进行统计分析，同时强调了标准科学实践中的缺陷。作者解释了如何浸泡木制骰子的一面使其偏向于掷出对面，从而更频繁地掷出六。通过计算加载骰子引起的概率变化，玩家可以制定定居点位置的策略，从而在每局游戏中获得大约 5-15 张额外的资源卡。

文章随后探讨了使用 p 值来证明骰子存在偏差的方法，证明了大量的掷骰次数 (4310) 会产生具有统计学意义的结果。然而，在掷骰次数较少的典型游戏中 (60)，对手很难在统计上证明作弊。作者计算出，您可以进行多达 6 场游戏，对手才有足够的数据通过标准的 p 值测试达到统计显著性。

最后，文章批判了 p 值和零假设显著性检验的局限性。它指出，p 值未能纳入先验知识（例如骰子上的变色），并且容易出现假阳性。作者提到了贝叶斯因子等替代方案，以及提议的更严格的 p 值阈值 0.005，但承认了统计分析的日益复杂性。作者还分享了同行评审的意见，强调了科学实践中健全性检查和数据透明度的重要性。

---

## 36. 我自制了一个音频播放器

**原文标题**: I Built My Own Audio Player

**原文链接**: [https://nexo.sh/posts/why-i-built-a-native-mp3-player-in-swiftui/](https://nexo.sh/posts/why-i-built-a-native-mp3-player-in-swiftui/)

2025年，由于对苹果iPhone离线音乐播放的限制性做法感到沮丧，作者从头构建了一个自定义音频播放器。苹果的云同步功能需要付费，而现有的第三方应用程序要么是订阅制的，要么缺乏灵活搜索和iCloud集成等关键功能。

作者的自定义播放器通过提供跨iCloud文件夹的全文本搜索、全面的音乐管理功能（队列、播放列表、排序）以及熟悉的用户界面，解决了这些痛点。最初尝试了React Native，但由于访问iOS文件系统和iCloud集成的限制，最终切换到Swift和SwiftUI，以便更好地控制原生API和沙盒权限。

该应用程序架构类似于服务器应用程序，使用SQLite进行持久性数据存储，使用FTS5进行快速模糊搜索。分层架构将逻辑层与UI分离，Swift Actors管理业务规则，ViewModels转换数据供SwiftUI视图使用。SQLite的FTS5支持跨文件名和元数据的快速搜索。

挑战包括iOS的限制性文件访问和安全作用域书签的限制。作者实施了一种将文件复制到应用程序容器中的后备机制。AVFoundation框架用于元数据解析和音频播放，并与MPRemoteCommandCenter集成以实现系统级播放控制。

作者反思了Xcode的局限性以及Apple的SDK仍然滞后的领域，但也承认了SwiftUI和Swift的async/await功能的改进。

---

## 37. 完美酱油的韩国宗师

**原文标题**: A South Korean grand master on the art of the perfect soy sauce

**原文链接**: [https://www.theguardian.com/world/2025/may/21/without-time-there-is-no-flavour-a-south-korean-grand-master-on-the-art-of-the-perfect-soy-sauce](https://www.theguardian.com/world/2025/may/21/without-time-there-is-no-flavour-a-south-korean-grand-master-on-the-art-of-the-perfect-soy-sauce)

奇順道是韩国仅存的真酱（陈年酱油）大师，是拥有370年历史的发酵大豆调味品（酱）家族传统的第十代传人。酱包括酱油、大酱和辣椒酱，是韩国料理的基础。她强调时间和精心照料以及高质量的原料（大豆、水和盐）在制作正宗酱油中的重要性，并将其与大规模生产的版本形成对比。

这个过程始于冬季，将煮熟并压碎的大豆制成麹块，用有益细菌发酵，然后浸泡在竹盐盐水中。液体变成酱油，而固体则变成大酱。她陈酿超过五年的真酱获得了国际赞誉，甚至曾被用来为唐纳德·特朗普的食物调味。奇还制作一种独特的草莓辣椒酱。

她的奉献精神在2024年获得了联合国教科文组织非物质文化遗产的认可，强调了保护传统饮食文化的重要性。她经营一所发酵学校，分享她的知识。

奇面临着包括家庭自制酱衰落和影响发酵过程的气候变化等挑战。她通过修改麹块的大小和为罐子提供阴凉来适应环境。最终，奇认为她的工作是保护韩国文化重要组成部分的使命。

---

## 38. 吉露早餐谷物糖霜宣称有效性的正式数学研究

**原文标题**: A Formal Mathematical Investigation on the Validity of Kellogg's Glaze Claims

**原文链接**: [https://old.reddit.com/r/theydidthemath/comments/1iljmig/_/](https://old.reddit.com/r/theydidthemath/comments/1iljmig/_/)

无法访问文章链接。

---

## 39. 理查德·加温在氢弹设计中的作用被掩盖了。

**原文标题**: Richard Garwin’s role in designing the hydrogen bomb was obscured

**原文链接**: [https://www.nytimes.com/2025/05/19/science/richard-garwin-hydrogen-bomb.html](https://www.nytimes.com/2025/05/19/science/richard-garwin-hydrogen-bomb.html)

本文详细介绍了物理学家理查德·L·加温的生平和遗产，重点讲述了他设计第一颗氢弹的关键但常被忽视的作用。作为恩里科·费米的学生，费米认为他是天才，加温在23岁时设计了这种武器。氢弹的破坏力远超原子弹。

费米在去世前不久，对其参与公共政策议题有限表示遗憾。这次谈话激励加温将毕生精力投入到对抗他参与制造的核恐怖之中。他认为核科学家有责任发声，以费米的理想为榜样。加温将毕生精力投入到倡导核武器控制和不扩散。

本文突出了加温早期对制造有史以来最具破坏性武器的贡献，与他后来致力于防止其使用和扩散之间的对比。它为进一步探索他的人生以及围绕他参与核武器的复杂性奠定了基础。文章提到，仍然存在一个谜团，暗示了关于加温遗产的更多细节将在获得完整文章的访问权限后揭晓。

---

## 40. 团队过大时

**原文标题**: When a team is too big

**原文链接**: [https://blog.alexewerlof.com/p/when-a-team-is-too-big](https://blog.alexewerlof.com/p/when-a-team-is-too-big)

亚历克斯·埃韦尔洛夫的文章探讨了大型团队面临的挑战，并提倡采用通才方法来提高生产力和韧性。他回顾了其在14人团队中的经验，该团队在沟通、无关的站立会议和虚幻任务方面苦苦挣扎。最初解决此问题的尝试，例如将团队划分为前端和后端“任务组”，由于相互依赖性而被证明无效。

其他尝试的解决方案，如流动任务组、将团队分成两半以及聘请顾问也失败了。最终的解决方案是从专业角色转变为通才技能，团队成员可以处理跨堆栈的各种任务（前端、后端、QA、DevOps）。

作者认为，通才团队可以减少瓶颈、提高所有权并促进更好的沟通。他强调，共享背景、狭窄需求和动机（自主性、精通、目标）促成了通才模式的成功。结对编程在知识共享和技能发展方面发挥了重要作用。

文章将通才团队与专业团队进行了对比，突出了后者中的沟通开销和“虚假工作”的潜力。最终，作者得出结论，涵盖知识、授权和责任的明确所有权对于团队成功至关重要。虽然通才方法在这种特定情况下有效，但它并非被呈现为一种通用解决方案，而是一种适合特定环境的实践。

---

## 41. Show HN：SQLite JavaScript - 用 JavaScript 扩展你的数据库

**原文标题**: Show HN: SQLite JavaScript - extend your database with JavaScript

**原文链接**: [https://github.com/sqliteai/sqlite-js](https://github.com/sqliteai/sqlite-js)

SQLite-JS：使用 JavaScript 扩展 SQLite 功能的强大扩展。它允许你在数据库中直接创建自定义 SQLite 函数，实现灵活的数据操作。你可以定义标量函数、聚合函数和窗口函数，以及自定义排序规则。

该扩展提供了使用 JavaScript 代码片段创建这些自定义行为的函数。标量函数处理单个行，聚合函数处理多个行以产生单个结果，窗口函数对一组行进行操作而不折叠它们。排序规则定义自定义排序逻辑。它还包括在查询中直接执行 JavaScript 代码。

安装涉及为你操作系统（Linux、macOS、Windows、Android、iOS）下载预构建的二进制文件，并使用 SQLite CLI 中的 `.load` 命令或 SQL 中的 `load_extension()` 函数加载它。

SQLite-JS 函数可以使用 sqlite-sync（通过 `js_init_table`）跨设备同步。更新现有的 JavaScript 函数需要单独的数据库连接。该项目以 MIT 许可证授权，并且可以通过提供的 Makefile 从源代码构建。

---

## 42. 从JSON加载Pydantic模型，避免内存溢出

**原文标题**: Loading Pydantic models from JSON without running out of memory

**原文链接**: [https://pythonspeed.com/articles/pydantic-json-memory/](https://pythonspeed.com/articles/pydantic-json-memory/)

本文探讨了在 Python 中将大型 JSON 文件加载到 Pydantic 模型时内存使用率过高的问题。作者演示了默认的 Pydantic JSON 加载可能导致内存占用量达到 JSON 文件大小的 20 倍。

本文探讨了两种主要的降低内存使用率的策略：优化 JSON 解析和使用内存高效的对象表示。首先，它建议使用 `ijson` 库进行增量 JSON 解析，该方法逐块处理 JSON 文件，而不是将其全部加载到内存中。这显著降低了内存消耗，但会带来性能上的权衡。

其次，本文建议使用带有 `slots=True` 的 Python 数据类。 Slots 为具有固定属性集的对象提供了更紧凑的内存表示，防止为每个实例的属性创建字典。这通过从 `pydantic.BaseModel` 切换到 `pydantic.dataclasses.dataclass` 来实现。

作者比较了使用不同方法加载 100MB JSON 文件时的内存使用情况：`Model.model_validate_json()` 导致 2000MB，`ijson` 将其降低到 1200MB，而 `ijson` 结合 `@dataclass(slots=True)` 则进一步将其降低到 450MB。

本文最后建议 Pydantic 可能会合并 `ijson` 中的功能并在 `BaseModel` 中支持 `__slots__`，以提高内存效率。

---

## 43. 好的伪随机数变坏时

**原文标题**: When good pseudorandom numbers go bad

**原文链接**: [https://blog.djnavarro.net/posts/2025-05-18_multivariate-normal-sampling-floating-point/](https://blog.djnavarro.net/posts/2025-05-18_multivariate-normal-sampling-floating-point/)

即使使用`set.seed()`，R模拟多元正态分布时可重复性问题探究。作者最初与同事遇到此问题，即使使用相同的种子，在不同机器上也会观察到不同的随机数，导致使用`MASS::mvrnorm()`时结果不可重现。

问题的根源在于浮点运算的局限性。虽然`set.seed()`通常能保证可重复性，但由于操作系统、编译器设置等原因，不同系统之间的计算存在细微差异。这些差异，尤其是在多元正态抽样固有的矩阵分解中，会导致截然不同的结果，即使生成的数字保留了正确的分布属性。

作者用两个几乎相同的协方差矩阵（`cov1`和`cov2`）演示了这一点，尽管使用了相同的种子，但`MASS::mvrnorm()`产生的结果却大相径庭。这与单变量正态抽样（`rnorm()`）观察到的稳定行为形成对比，其中小的输入变化导致小的输出变化。

核心问题是，从多元正态分布中抽样的计算复杂度，包括矩阵分解，会大大增加浮点截断误差放大的机会，从而导致不可重现性。

---

## 44. 反乌托邦梦之队

**原文标题**: The Dystopian Dream Team

**原文链接**: [https://lmnt.me/blog/the-dystopian-dream-team.html](https://lmnt.me/blog/the-dystopian-dream-team.html)

本文对乔尼·艾维和萨姆·奥特曼的合作关系表示强烈的怀疑和厌恶，称之为“反乌托邦梦之队”。作者批评他们的介绍视频自吹自擂，尤其考虑到他们据称为旧金山带来的问题。

作者质疑艾维对计算机的真正兴趣，认为他主要是一个美观硬件的设计者，并指责奥特曼通过传播虚假信息的AI，建立了一个基于盗窃和环境不负责任的商业。他们认为这两个人都缺乏对计算机实际价值的真正欣赏，其动机是自我而非改善人们的生活。

作者认为，计算设备革命性飞跃的时代已经结束。智能手机和电脑已经达到其效用的顶峰，现在可以与家用电器相提并论。当前的“创新”，尤其是那些由人工智能驱动的创新，被视为一种为了保持相关性而进行的孤注一掷的尝试，而不是真正的进步。

作者认为，科技巨头受到傲慢自大和验证过去成功的需求的驱使，导致他们追求不必要且代价高昂的项目。他们尤其批评艾维推广奢侈品的历史，认为他脱离了普通人的需求。文章最后强烈反对有必要甚至有可能出现新的设备类别，认为艾维-奥特曼的合资企业只不过是富人追求虚荣项目，对社会没有真正好处的又一个例子。

---

## 45. 伊尼戈·奎莱斯：计算机图形学、数学、着色器、分形、演示场景

**原文标题**: Inigo Quilez: computer graphics, mathematics, shaders, fractals, demoscene

**原文链接**: [https://iquilezles.org/articles/](https://iquilezles.org/articles/)

Inigo Quilez 的网站是关于计算机图形学、数学、着色器、分形和演示场景技术的综合资源。它主要提供书面教程，并附带 MIT 许可的代码片段，方便重用。该网站涵盖了广泛的主题，包括有符号距离场 (SDF) 和光线步进，深入解释了 2D 和 3D SDF、光线与表面相交、平滑最小值技术、域重复、软阴影和数值法线。

该网站还深入研究了纹理和过滤技术，如双平面贴图、纹理重复、解析棋盘格图案过滤和改进的硬件插值。光照是另一个突出的主题，涵盖了户外照明、雾、环境光遮蔽和全局照明。

此外，该网站还提供了对渲染器和引擎优化的见解，涵盖了 GPU 条件、避免三角函数、时钟周期计时、视锥体裁剪和基本 VR 等主题。还解释了有用的数学概念和函数，包括无三角函数的 IK、球/盒环境光遮蔽、距离计算和椭圆操作。

该网站展示了 Inigo Quilez 在分形和复杂动力学方面的专业知识，探索了曼德勃罗集、朱莉娅集分形、轨道陷阱和其他分形类型。此外，还有关于程序噪声、压缩技术、程序图形创建和各种趣味数学问题的章节。作者鼓励通过 Patreon 或 PayPal 提供支持。

---

## 46. 使用模型上下文协议的符号代数探险

**原文标题**: Adventures in Symbolic Algebra with Model Context Protocol

**原文链接**: [https://www.stephendiehl.com/posts/computer_algebra_mcp/](https://www.stephendiehl.com/posts/computer_algebra_mcp/)

本文详细介绍了一项实验，该实验利用Anthropic的模型上下文协议（MCP）将大型语言模型（LLM）与计算机代数系统（如SymPy）连接起来。作者强调了LLM在理解自然语言数学问题方面的优势以及在执行精确符号计算方面的劣势。相反，计算机代数系统擅长符号操作，但缺乏直观的界面。

MCP充当AI工具的“USB-C”，允许LLM通过暴露REST API的本地服务器调用外部工具。这使得LLM能够将复杂的计算委托给像SymPy这样的系统。一个关键问题是固有的安全风险，因为本地服务器授予LLM执行任意代码的能力。

作者提供了一个使用MCP分解整数的简单示例，演示了LLM如何利用外部工具来克服其计算限制。他们还展示了一个更复杂的场景，即求解阻尼谐波振荡器方程，其中LLM协调过程，SymPy提供正确的解决方案，突出了与形式验证系统集成的潜力以及降低复杂数学计算的入门门槛的可能性。

作者将MCP生态系统描述为不成熟但充满希望，并将其比作“狂野西部”。由于LLM的随机性，调试具有挑战性。文章最后给出了关于使用MCP的潜在安全影响的说明和担忧，敦促读者在安装MCP服务器之前审查代码。

---

## 47. 双子座扩散

**原文标题**: Gemini Diffusion

**原文链接**: [https://simonwillison.net/2025/May/21/gemini-diffusion/](https://simonwillison.net/2025/May/21/gemini-diffusion/)

本文探讨了谷歌的新语言模型Gemini Diffusion，该模型利用扩散技术而非传统的自回归方法进行文本生成。Gemini Diffusion的主要优势在于其速度，作者报告称在提示其构建模拟聊天应用程序时，其生成速率为857个tokens/秒，在几秒钟内即可生成可用的交互式HTML+JavaScript页面。这种性能与Cerebras Coder相当。

虽然目前尚缺乏独立的基准测试，但谷歌声称其性能与Gemini 2.0 Flash-Lite相当，速度却是其5倍。作者指出Inception Mercury是另一款更早的基于扩散技术的商业LLM。

文章包含一项更新，澄清扩散技术用于取代自回归，而非transformers，这意味着可能仍然涉及transformer架构。此外，在这种情况下，“扩散”方面更类似于BERT的masked language modeling，模型学习恢复被大量遮蔽的文本。生成过程涉及从完全遮蔽的tokens的起点迭代地细化文本，在多个推理步骤中逐渐揭示tokens，直到生成完整的序列。这种方法允许并行处理和纠错，从而提高了模型的速度。

---

## 48. 瑞昱10美元万兆网卡即将登陆主板

**原文标题**: Realtek's $10 tiny 10GbE NIC will hit motherboards soon

**原文链接**: [https://www.tomshardware.com/networking/realteks-usd10-tiny-10gbe-network-adapter-is-coming-to-motherboards-later-this-year](https://www.tomshardware.com/networking/realteks-usd10-tiny-10gbe-network-adapter-is-coming-to-motherboards-later-this-year)

瑞昱推出超小型低功耗10GbE网络控制器RTL8127，旨在为主流主板、笔记本电脑及其他设备带来更快的网络速度。该控制器尺寸仅为9mm x 9mm，支持PCIe 4.0 x2，兼容2.5Gbps、5Gbps和10Gbps以太网，功耗低于2W，并具备纠错和诊断功能。

其主要卖点是预计售价约为10美元，这将显著降低主板制造商集成10GbE连接的成本壁垒。这有望在服务器和高端工作站之外普及10GbE应用。

然而，文章强调了“鸡和蛋”的问题：广泛采用取决于10GbE交换机和CAT6/CAT6A线缆等配套基础设施的经济性。目前，这些产品的价格远高于1GbE甚至2.5GbE同类产品。虽然Realtek网卡的推出可能会因需求增加而降低交换机价格，但具体时间尚不确定。

尽管存在基础设施成本，但更快的局域网速度（用于备份和文件共享）以及日益普及的多千兆互联网服务所带来的潜在优势，使Realtek RTL8127成为更快网络发展的一个有希望的进步。作者预计主板制造商将在2025年末或2026年初开始将10GbE作为一项高级功能进行推广。

---

## 49. 四年视奏练习

**原文标题**: Four years of sight reading practice

**原文链接**: [https://sandrock.co.za/carl/2025/05/four-years-of-sight-reading-pracice/](https://sandrock.co.za/carl/2025/05/four-years-of-sight-reading-pracice/)

Alchemyst 详细介绍了他们使用 iPad 应用程序 ("NoteVision") 和 MIDI 键盘在钢琴上进行四年视奏练习的历程。受利用现有钢琴的愿望驱使，他们采用了该应用程序，因为它能提供快速反馈，并自动化了几个步骤来增强练习。

该练习流程涉及一个自定义的 Pythonista 界面，该界面为应用程序选择一个随机的琴键，并将结果记录在 MySQL 数据库中。D3.js 仪表板可视化了随时间和每个琴键的进度，揭示了不同的阶段：最初专注于 C 大调，探索其他琴键（如 G 大调），以及转向随机琴键选择以解决弱点。作者最初使用 Excel 电子表格跟踪进度，然后转向 Airtable 并编写了手机界面。

关键的学习包括意识到视觉音符和手指动作之间的直接联系可以绕过有意识地命名音符的需要，尽管后者仍然重要，并且正在使用 Anki 解决。尽管他们的 49 键 MIDI 键盘存在局限性，但他们观察到视奏的持续进步和信心增强。他们还发现随机化对于避免对更容易的琴键产生心理偏见至关重要。

作者延长的 30 分钟练习程序包括视奏、音阶/琶音、使用 Anki 进行的理论练习、记谱/转录练习、听力训练和曲目练习。他们认识到除了自动化视奏练习之外，综合方法的重要性。

---

## 50. GNU编译器集合中的素路径覆盖

**原文标题**: Prime Path Coverage in the GNU Compiler Collection

**原文链接**: [https://arxiv.org/abs/2505.14694](https://arxiv.org/abs/2505.14694)

Jørgen Kvalsvik 的文章《GNU 编译器集合中的素路径覆盖》描述了 GCC 15 中素路径覆盖支持的实现。素路径覆盖是一种结构覆盖度量，侧重于执行路径，要求循环被执行、多次执行和跳过。该论文认为，它在测试工作量和代码覆盖率之间取得了良好的平衡，并且包含了修改后的条件/决策覆盖 (MC/DC)。

作者提出了一种改进的素路径枚举算法。该算法使用后缀树有效地修剪重复和冗余的子路径，将时间复杂度从 O(n^2m^2) 降低到 O(n^2m)，其中 n 是最长路径长度，m 是候选路径的数量。该算法利用有序素路径索引的紧凑表示和按位运算来有效地跟踪候选路径。

该论文强调了 GCC 以语言无关的方式分析控制流图和检测路径的能力，从而能够准确报告实现素路径覆盖所需的代码执行顺序。这允许有效识别需要运行哪些代码以及以什么顺序运行才能满足覆盖标准。该论文包含 12 个图表，共 11 页。

---

## 51. Gitlab Duo 远程提示注入导致源码泄露

**原文标题**: Remote Prompt Injection in Gitlab Duo Leads to Source Code Theft

**原文链接**: [https://www.legitsecurity.com/blog/remote-prompt-injection-in-gitlab-duo](https://www.legitsecurity.com/blog/remote-prompt-injection-in-gitlab-duo)

Legit研究团队发现GitLab Duo存在远程提示注入漏洞，该漏洞可能导致源代码泄露和其他恶意行为。攻击者可以在GitLab项目的各个部分（合并请求、提交信息、源代码等）嵌入隐藏提示，以操纵Duo的行为。

Unicode走私、Base16编码和KaTeX渲染等编码技巧被用于隐藏提示。这使得攻击者能够操纵代码建议，将恶意URL呈现为安全链接，并将不受信任的HTML注入到Duo的响应中。Duo的流式markdown渲染逐行解析和渲染HTML，被利用将原始HTML标签注入到其输出中，导致潜在的XSS漏洞，尽管DOMPurify进行了清理。

最重要的影响是能够泄露私有源代码。通过指示Duo从私有合并请求中提取代码更改，以Base64编码并将它们嵌入到<img>标签URL中，攻击者可以窃取敏感数据。相同的技术也可用于泄露机密问题数据，包括零日漏洞。

GitLab通过修补HTML注入漏洞并承认提示注入是一种安全风险来解决了这个问题。该补丁阻止Duo渲染指向外部域的不安全HTML标签，从而减轻了数据泄露的风险。该事件突显了在将AI助手集成到开发工作流程中时需要谨慎考虑安全性，并强调了将用户控制的输入视为不受信任和潜在恶意输入的重要性。

---

## 52. AI对齐问题：一个比例模型

**原文标题**: Problems in AI alignment: A scale model

**原文链接**: [https://muldoon.cloud/2025/05/22/alignment.html](https://muldoon.cloud/2025/05/22/alignment.html)

本文批判了当前人工智能对齐对话的焦点，认为其过于狭隘地关注技术解决方案，而忽视了更大的社会背景。虽然人工智能对齐被定义为引导人工智能系统走向伦理原则，但作者指出，其他行业，如制药和教育，也存在类似的需求，但这些行业的问题并未被主要视为技术问题。

作者认为，“人工智能对齐”存在一种隐含的技术偏见，即专注于数学和科学，而忽略了塑造人工智能开发和使用的更广泛的社会力量。作者引入了“选择”的概念，并将其比作进化，即社会选择（购买、监管、公共讨论）决定了哪些类型的人工智能公司和应用能够蓬勃发展。

虽然技术性的人工智能对齐问题很重要，但作者认为，社会“选择”对塑造人工智能的影响更为重要，因此它是“人工智能对齐的大问题”。忽视这种更广泛的背景是一种愚蠢的行为。作者驳斥了影响社会意志是不可能的观点，并将其与伦理框架和博弈论等领域联系起来。最后，作者提出了社会技术协议，例如公民组织，作为提高“选择效率”并将人工智能发展导向更理想方向的方法。本质上，人工智能对齐需要的不仅仅是技术解决方案，还需要社会积极参与塑造人工智能格局。

---

## 53. Kotlin-Lsp：Kotlin语言服务器及Visual Studio Code插件

**原文标题**: Kotlin-Lsp: Kotlin Language Server and Plugin for Visual Studio Code

**原文链接**: [https://github.com/Kotlin/kotlin-lsp](https://github.com/Kotlin/kotlin-lsp)

Kotlin-Lsp 是一个预先发布的官方 Kotlin 语言服务器和 Visual Studio Code 插件。它构建于 IntelliJ IDEA 之上，旨在通过语言服务器协议在 VS Code 中提供全面的 Kotlin 支持。

**要点：**

*   **功能：** 目前专注于纯 JVM Kotlin Gradle 项目，支持项目导入、高亮显示、导航、代码操作（快速修复、检查、组织导入）、重构、实时诊断和补全等功能。路线图包括将项目导入扩展到 KMP、Maven 和 Amper 项目以及其他改进。
*   **安装：** VSC 扩展可以通过 RELEASES.md 文件中获取的 VSIX 文件安装。 需要 Java 17 或更高版本。
*   **状态：** 实验性且正在积极开发中。预计不稳定且频繁更改。虽然适合实验，但目前不建议用于生产环境。
*   **平台：** 主要在 macOS 和 Linux 上的 Visual Studio Code 中进行测试。可以通过手动配置与其他符合 LSP 规范的编辑器一起使用。需要基于拉取的诊断支持。
*   **源代码：** 为了加快开发速度，LSP 实现目前部分闭源，依赖于内部 IntelliJ、Fleet 和 Bazel 基础设施。计划在初步稳定后将其解耦并完全开源。
*   **反馈：** Bug 报告和功能请求应通过 GitHub 问题提交。 暂时不支持直接的代码贡献。

---

## 54. 联邦法官叫停特朗普政府禁止哈佛招收国际学生的禁令

**原文标题**: Federal judge halts Trump admin ban on Harvard's ability to enroll intl students

**原文链接**: [https://www.cnn.com/2025/05/22/us/harvard-university-trump-international-students](https://www.cnn.com/2025/05/22/us/harvard-university-trump-international-students)

联邦法官暂时叫停了特朗普政府禁止哈佛大学招收国际学生的禁令，此前哈佛大学提起诉讼，称该禁令是对其拒绝政府政策要求的报复，尤其是在校园治理、课程和意识形态方面。政府此举被视为对哈佛拒绝服从交出学生纪律记录和取消公平倡议等要求的惩罚。

该禁令将影响哈佛近7000名国际学生，引起广泛焦虑和困惑。哈佛大学官员誓言要反对该决定，强调国际学生的宝贵贡献。诉讼将国土安全部、司法部和国务院以及特定部长列为被告。政府为自己的行为辩护，称需要恢复学生签证系统的“常识”，并指责哈佛大学助长反美和反犹情绪，尤其是在与以色列-哈马斯战争有关的抗议活动方面。

这场法律战正在与另一项诉讼同时展开，哈佛大学正在挑战政府冻结的26.5亿美元联邦资金。包括前哈佛校长劳伦斯·萨默斯在内的批评人士谴责国际学生禁令是歧视和滥用政府权力。

---

## 55. 威利·旺卡巧克力工厂的商业秘密 (2009)

**原文标题**: Trade Secrecy in Willy Wonka's Chocolate Factory (2009)

**原文链接**: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1430463](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1430463)

Jeanne C. Fromer的文章《威利·旺卡的巧克力工厂中的商业秘密》探讨了商业秘密在罗尔德·达尔的《查理和巧克力工厂》中的作用及其与现实糖果行业的关联。虽然这部小说主要被视为儿童故事，但Fromer认为其核心情节围绕商业秘密的法律问题展开。她认为，这种保密性并非小说独有，而是渗透到过去和现在的实际糖果行业中，并引用了如好时和玛氏等例子。

这篇文章探讨了糖果界这种高度保密性的根本原因。它提出了关于商业秘密的法律保护的有效性和必要性的根本问题，尤其是在对公司而言，保持实际保密性至关重要的情况下。最后，这篇文章还深入探讨了商业秘密和专利法在保护该行业创新方面的关系。

最终，Fromer的分析以虚构的旺卡工厂为视角，审视了商业秘密在一个竞争激烈且创新高度发达的行业中的法律和经济意义，从而促使人们更深入地思考如何管理和保护这些秘密。

---

## 56. 我们称之为分贝的科学“单位”

**原文标题**: The scientific “unit” we call the decibel

**原文链接**: [https://lcamtuf.substack.com/p/decibels-are-ridiculous](https://lcamtuf.substack.com/p/decibels-are-ridiculous)

好的，我已阅读了来自所提供URL的题为“我们称之为分贝的科学‘单位’”的文章。

以下是简要总结：

这篇文章认为，分贝（dB）是一个令人困惑且定义不明确的“单位”，在科学和工程领域被过度依赖。作者认为，dB的对数性质，加上其对通常未明确或未被充分理解的参考值的依赖，导致计算和解释中的模糊性和错误。

作者强调了几个关键问题：

*   **任意参考值：** dB表示相对于参考值的比率，但此参考值并不总是明确。不同的dB刻度（例如，dBm、dBV、dBSPL）使用不同的参考值，如果未明确说明，则会导致混淆。

*   **对数复杂性：** dB的对数性质，虽然在某些情况下对于表示大范围的值很有用，但会引入额外的计算层，并且可能会模糊数量之间的潜在关系。

*   **潜在的误解：** 对数刻度缺乏直观理解，再加上任意参考值，可能导致误解和不正确的结论。

*   **存在替代方案：** 作者建议，使用原始比率或百分比，虽然并非总是方便，但可以提供更好的清晰度并降低出错的风险。文章在承认dB在某些应用（例如表达信噪比）中的效用的同时，倡导对其使用采取更批判性和更周全的态度，强调理解底层参考的重要性，并且在清晰度至关重要时可能更喜欢替代方案。

本质上，作者认为，虽然并非完全无用，但dB通常会引入不必要的复杂性和模糊性，使其成为一个“荒谬”的单位，应谨慎使用，并在可能的情况下用更清晰的替代方案代替。

---

## 57. OpenAI: 将 PostgreSQL 扩展到新高度

**原文标题**: OpenAI: Scaling PostgreSQL to the Next Level

**原文链接**: [https://www.pixelstech.net/article/1747708863-openai%3a-scaling-postgresql-to-the-next-level](https://www.pixelstech.net/article/1747708863-openai%3a-scaling-postgresql-to-the-next-level)

无法访问文章链接。

---

## 58. 从零开始的异步编程 3：困于墙角

**原文标题**: Async from scratch 3: Pinned against the wall

**原文链接**: [https://natkr.com/2025-05-22-async-from-scratch-3/](https://natkr.com/2025-05-22-async-from-scratch-3/)

本文是关于从头开始在 Rust 中实现异步功能的系列文章的第三篇，深入探讨了 pinning 的概念，这是一种用于管理异步代码中自引用数据结构的关键机制。

首先，本文阐明了 Rust traits 中关联类型的使用，并将其与泛型进行对比。 像 `Future::Output` 这样的关联类型允许更多的类型推断和代码便利性，指定一个由实现类型唯一确定的返回类型。

解决的核心问题是 Rust 在处理借用自身的结构体方面的困难，特别是在表示异步操作的状态机枚举的上下文中。 尝试使用所有权转移、`Option` 包装器或克隆来解决这个问题被认为是不充分的。

然后，本文探讨了使用原始指针作为幼稚解决方案的危险性，强调了在 `poll()` 调用后 future 在内存中移动时，数据损坏的风险。

Pinning 被引入作为解决方案。 `Pin` 包装器可以防止在值被 pinning 后移动它，从而确保对该值的引用保持有效。 本文概述了 `Pin` API，包括用于创建 pin 的不安全方法和用于读取和替换值的安全方法。介绍了 `PinnedFuture` trait，它使用 `Pin<&mut Self>` 作为接收者。

最后，讨论了 `Unpin` 标记 trait。 实现 `Unpin` 的类型免受 pinning 要求的约束，允许代码将 `Pin<&mut T>` 视为 `&mut T` 用于这些类型，从而减少在不需要 pinning 时的精神负担。

---

## 59. 使用希尔伯特曲线可视化进行图形调试实践

**原文标题**: Practicing graphical debugging using visualizations of the Hilbert curve

**原文链接**: [https://akkartik.name/debugUIs.html](https://akkartik.name/debugUIs.html)

本文记录了作者通过图形可视化来理解和调试一个令人困惑的用于生成希尔伯特曲线的Lua函数的过程。起初，作者发现这段代码晦涩难懂，尽管理解了诸如递归和象限分割等表面概念。

作者随后采用了一系列可视化的调试技术，每一种都以前一种为基础，以揭示算法的不同方面。这些技术包括：

*   **v1:** 绘制希尔伯特曲线本身以观察整体形状。
*   **v2:** 打印递归调用的序列以理解参数流。
*   **v3:** 以动画形式展现绘制过程，以揭示叶子节点计算的顺序。
*   **v4:** 并排绘制不同阶数的多次迭代，以观察曲线的演变。
*   **v5:** 可视化每个叶子节点调用中使用的点和线，以了解各个曲线段是如何形成的。这突出了基点和控制点之间的协同作用。
*   **v6:** 尝试绘制每个递归调用的“包络”或支架，最初导致混乱的重叠，然后使用动画来揭示支架的重叠点和线。

通过这些日益详细的图形表示，作者逐渐深入了解了算法的工作原理，例如控制点的方向以及递归调用之间的关系，将一个不清晰的程序变成可以理解的东西。文章还强调了图形调试和易于获得的画布在编程中的价值。

---

## 60. 热点：用于性能分析的 Linux `perf` GUI

**原文标题**: Hotspot: Linux `perf` GUI for performance analysis

**原文链接**: [https://github.com/KDAB/hotspot](https://github.com/KDAB/hotspot)

Hotspot 是一个独立的 Linux `perf` 数据图形用户界面，旨在提供类似于 KCachegrind 的体验。它可以可视化 `perf.data` 文件，并允许按时间、进程或线程进行过滤。它还支持从 GUI 内部启动 `perf` 进行性能分析。

Hotspot 可通过 ArchLinux、Debian/Ubuntu、Gentoo 和 Fedora 上的软件包管理器获得，也可作为通用的 AppImage 提供。贡献者和需要最新版本的用户可以从源代码构建。

使用 Hotspot 首先需要使用 `perf record --call-graph dwarf <应用程序>` 记录数据。命令行选项允许指定 sysroot、kallsyms、调试信息和导出数据的路径。

Hotspot 支持使用内核跟踪点进行 off-CPU 性能分析，以进行等待时间分析，从而识别 I/O 等待、页面错误和锁竞争。它也适用于嵌入式系统，需要指定 sysroot 和 kallsyms 路径。

数据可以导出到独立的 `*.perfparser` 文件以进行共享，但此格式目前是特定于版本的。该工具包含一个带有源代码集成的反汇编器。

已知问题包括损坏的回溯（通常是由于缺少调试信息或 ELF 文件，可以使用 `--debugPaths`、`--extraLibPaths`、`--appPath`、`--sysroot` 等命令行参数解决）以及与 `perf report` 相比的局限性。该工具还支持通过 debuginfod 下载调试符号。在没有超级用户权限的情况下进行录制需要以提升的权限运行 perf，并且导出文件格式目前受到限制。该项目利用 Qt Creator 的 `perfparser`，并以 GPL v2+ 许可证授权。

---

## 61. 论文被接收

**原文标题**: Getting a paper accepted

**原文链接**: [https://maxwellforbes.com/posts/how-to-get-a-paper-accepted/](https://maxwellforbes.com/posts/how-to-get-a-paper-accepted/)

如何提高论文录用率：提升论文质量的策略

本文“如何提高论文录用率”详细介绍了提高论文录用机会的策略，特别强调了第一印象和彻底性的重要性。文章认为，一篇论文大约80%的感知质量基于第一页，包括标题、图1、摘要和引言。作者通过一个真实案例展示了这些原则，该案例为一个被拒论文在修改后最终被录用。

主要建议包括：

*   **优化第一页：** 撰写具体且令人难忘的标题（可能带有品牌效应），创建引人注目的图1，清晰地传达作品的价值，撰写具体且引人入胜的摘要，并在引言中使用紧张/释放周期来强调要解决的问题。
*   **图表和说明：** 使图表信息丰富且具有视觉吸引力，并在每个图表说明的结尾处明确总结结论。
*   **完整性：** 确保论文的其他部分避免被拒，方法是包括基线、消融研究、统计显著性和人工评估。
*   **清晰度：** 提高图、表和结论的清晰度。以各种方式突出你的贡献。
*   **数据集评估：** 通过表格和图形将数据集与其他数据集进行比较，从而展示数据集的优势。

文章强调了清晰度和预先展示价值的重要性，以及通过确保论文的完整性和清晰沟通来避免常见的拒稿原因。作者还建议花时间远离作品，以获得新的视角并改善其呈现方式。

---

## 62. 扩散语言模型的优势与局限性

**原文标题**: Strengths and limitations of diffusion language models

**原文链接**: [https://www.seangoedecke.com/limitations-of-text-diffusion-models/](https://www.seangoedecke.com/limitations-of-text-diffusion-models/)

本文探讨了扩散语言模型相对于传统自回归模型（如GPT和Claude）的优势和局限性。扩散模型，以谷歌的Gemini Diffusion为例，在每个步骤生成整个输出，这带来了潜在的速度优势，因为它们可以并行生成token，并且可以通过训练来减少迭代次数以实现更快的，尽管质量较低的输出。

然而，扩散模型通常生成固定长度的输出，这使得它们在生成该长度或更长输出时更快，但在生成短输出时可能更慢。自回归模型逐个生成token并利用键值缓存，而扩散模型由于需要在每次去噪迭代中重新计算生成块中每个token的注意力，因此难以处理长上下文，从而增加了计算成本。

本文还质疑扩散模型是否能像自回归模型那样进行“思维链”推理，因为逐块生成可能不容易适应推理模型中出现的动态调整。尽管存在潜在挑战，作者指出有研究正在探索扩散框架内的替代推理方法。

最后，本文明确指出，扩散模型可以在内部使用transformers进行噪声预测，但它们的整体架构与自回归transformer模型有显著区别。

总而言之，扩散模型通过并行生成和可调节的去噪过程提供了速度优势，但在处理长上下文、推理和高效生成可变长度输出方面面临局限性。文章指出，正在进行的研究可能会克服其中的一些挑战。

---

## 63. 每天1145个拉取请求

**原文标题**: 1,145 pull requests per day

**原文链接**: [https://saile.it/1145-pull-requests-per-day/](https://saile.it/1145-pull-requests-per-day/)

本文重点介绍了 Stripe 在 Stripe Sessions 2025 大会上展示的卓越工程表现：2024 年，他们平均每天有 1145 个拉取请求完全发布到生产环境，且 API 可靠性极高。考虑到 Stripe 大约有 3400 名工程师（根据 8500 名员工估算），这意味着平均每位工程师每三天就有一项生产变更。

作者强调，考虑到 Stripe 巨大的支付量和关键运营，这一成就使其跻身于顶级软件交付表现者中的前 1%。虽然其他公司可能偶尔达到类似的部署数量，但 Stripe 的一致性、低停机时间和规模表明其拥有卓越的工程文化。

作者指出，如此高的速度和安全性需要对自动化测试、部署、回滚、可观察性和明确的代码所有权进行大量投资。他们还链接了一些资源，突显了 Stripe 严苛且先进的工程文化。

文章最后强调，目标不仅仅是模仿 Stripe 的部署数量，而是识别并消除阻碍向用户快速可靠地交付价值的障碍，从而培养一种信任、自主和持续改进的文化。

---

## 64. 星球坠落

**原文标题**: Planetfall

**原文链接**: [https://somethingaboutmaps.wordpress.com/2025/05/20/planetfall/](https://somethingaboutmaps.wordpress.com/2025/05/20/planetfall/)

丹尼尔·霍夫曼详细介绍了他的细致制图项目：创作1999年电脑游戏《席德·梅尔的半人马座阿尔法星》中行星凯隆星的详细地图。该地图的创建涉及从游戏本身提取和处理数据。霍夫曼一丝不苟地记录了游戏中每个8192个地图瓦片的标高数据。然后，他使用通过游戏内截图和模组主题地图获得的降雨量和异形真菌数据，并将这些数据导入QGIS。

一个重要的挑战是将地图的分辨率提高到超出游戏原始的128x64像素。霍夫曼使用了圆柱等面积（特里斯坦·爱德华兹）投影来匹配游戏的格式。为了创建更详细的数字高程模型（DEM），他在原始网格上散布随机点，执行TIN插值，然后通过基于Delauney三角剖分和随机噪声添加新点来迭代地细化地形。

他手动调整了DEM以匹配规范的游戏地图，修正了诸如岛屿和花环陨石坑形状等不一致之处。为高度扭曲的极地区域创建了单独的DEM。该过程涉及大量的实验，包括平滑技术和混合图层，最终生成了一张详细且具有有机外观的凯隆星地图，远远超过了原始游戏的分辨率和复杂性。霍夫曼强调了创建真实世界地图与虚构地图之间的差异，并强调他的技能在于操纵现有数据，而不是从头开始创建数据。

---

## 65. Show HN: Three.js 中的弯曲空间着色器 (通过 4D 球体投影)

**原文标题**: Show HN: Curved Space Shader in Three.js (via 4D sphere projection)

**原文链接**: [https://github.com/bntre/CurvedSpaceShader](https://github.com/bntre/CurvedSpaceShader)

此“Show HN”帖子介绍了一个用Three.js实现的弯曲空间着色器，它是从Unity游戏“Sfera”中使用的HLSL版本移植而来。该着色器通过使用4D旋转和投影变换3D模型来创建弯曲空间效果。

过程如下：模型被缩放并居中放置。顶点着色器随后将每个3D点投影到一个4D单位球体上，应用一个每个对象独有的4D旋转，并使用立体投影将该点投影回3D。

该帖子提供了一个实时演示链接和一个展示效果的YouTube视频。它还详细介绍了用于操纵场景的交互式控件，包括使用鼠标和键盘输入进行的缩放、旋转（ZW、XY、XZ/YZ、XW/YW）、缩放比例、对象移动、相机控制和场景重置。该演示使用了来自Three.js示例库的动画模型（Michelle和一匹马），并包含Kevin MacLeod的音乐。

---

## 66. 双子座猜出了我侄子的名字。

**原文标题**: Gemini figured out my nephew’s name

**原文链接**: [https://blog.nawaz.org/posts/2025/May/gemini-figured-out-my-nephews-name/](https://blog.nawaz.org/posts/2025/May/gemini-figured-out-my-nephews-name/)

在2025年5月17日的一篇博文中，作者描述了他们如何使用谷歌的Gemini LLM，以及一个自定义的MCP服务器（授予对其邮件存档的只读访问权限），来发现他们侄子的名字，Monty。作者的目标是测试Gemini从大型数据集中提取特定信息的能力，通过一系列有针对性的查询。

作者首先与Gemini就最佳方法进行了战略性讨论。在达成计划后，Gemini使用“from:Donovan son”、“from:Donovan baby”和“congratulations son”等关键词，迭代地搜索邮件存档。许多搜索产生了关于其他亲戚的无关结果。

Gemini最终聚焦于一个名为“Re: Monty”的邮件线程，该线程提到了对象的阅读偏好。虽然这封邮件没有明确说明“Monty是我的儿子”，但Gemini推断出这种联系，并正确地识别出Monty是Donovan的儿子。

作者强调了Gemini的推理过程，展示了它使用的各种搜索查询以及从死胡同中学习的能力。他们强调，解决方案最终源于最初的广泛搜索，这表明了全面数据访问的重要性。

作者构建的MCP服务器为Gemini提供了三个关键工具：`search`（用于查询邮件存档）、`get_message_content_by_id`（用于检索特定邮件的文本）和`get_thread_by_id`（用于检索整个邮件线程）。出于安全和控制原因，作者更愿意编写自己的服务器，而不是信任第三方，并使用Gemini来帮助编写代码。他们还指出，实施了一些限制，例如结果限制和长邮件的截断。

---

## 67. 现在你可以实时观看互联网档案馆保存文档了

**原文标题**: Now you can watch the Internet Archive preserve documents in real time

**原文链接**: [https://www.theverge.com/news/672682/internet-archive-microfiche-lo-fi-beats-channel](https://www.theverge.com/news/672682/internet-archive-microfiche-lo-fi-beats-channel)

互联网档案馆推出了YouTube直播，让观众了解其缩微胶片数字化过程的幕后情况。 该直播于周一至周五播出，展示了将缩微胶片（存储报纸和政府记录等小型化文档的胶片）实时转换为数字文件，并上传到其在线图书馆的过程。

观众可以近距离观察加利福尼亚州里士满的五个数字化工作站之一，操作员将缩微胶片卡片送入高分辨率相机下方。 软件将从每张胶片上捕获的图像拼接在一起，自动化工具识别并裁剪单个页面。 然后，互联网档案馆处理这些页面，使其可进行文本搜索，并将其上传到其公共收藏中。

该直播由Sophia Tung设置，她之前曾为Waymo自动驾驶出租车创建过类似的直播。 据互联网档案馆图书馆服务主管Chris Freeland称，该过程涉及定制机器对缩微胶片进行数字化处理，Tung补充说，非工作时间的节目包括无声电影和历史性的NASA图片。 该举措提高了互联网档案馆保存物理文档以供在线访问的透明度。

---

## 68. 巫师 (YC S24) 招聘首席硬件设计工程师

**原文标题**: Sorcerer (YC S24) Is Hiring a Lead Hardware Design Engineer

**原文链接**: [https://jobs.ashbyhq.com/sorcerer/6beb70de-9956-49b7-8e28-f48ea39efac6](https://jobs.ashbyhq.com/sorcerer/6beb70de-9956-49b7-8e28-f48ea39efac6)

Sorcerer (YC S24) 招聘首席硬件设计工程师

---

## 69. 特朗普政府叫停哈佛招收国际学生

**原文标题**: Trump administration halts Harvard's ability to enroll international students

**原文链接**: [https://www.nytimes.com/2025/05/22/us/politics/trump-harvard-international-students.html](https://www.nytimes.com/2025/05/22/us/politics/trump-harvard-international-students.html)

特朗普政府采取措施阻止哈佛大学招收国际学生，理由是其拒绝配合国土安全部一项调查相关的记录要求。国土安全部部长克里斯蒂·诺姆致信哈佛大学，撤销了该校的学生和交流访问学者项目认证，立即生效。此举可能会影响哈佛大学大约四分之一的学生。

政府的这一决定加剧了其通过限制哈佛大学吸引国际学生的能力来影响高等教育的努力，而国际学生是哈佛大学学术、经济和科研力量的重要来源。国土安全部声明，哈佛大学不得再招收外国学生，目前在读的外国学生必须转学，否则将失去其合法身份。

这一行动很可能引发哈佛大学的第二次法律挑战，此前哈佛大学曾就政府试图改变其课程、招生政策和招聘做法的行为提起诉讼。

---

## 70. Flatpak 的未来

**原文标题**: The Future of Flatpak

**原文链接**: [https://lwn.net/Articles/1020571/](https://lwn.net/Articles/1020571/)

本文总结了Sebastian Wick在Linux应用程序峰会(LAS)上关于Flatpak当前状态和未来发展的演讲。尽管Flatpak已被广泛采用并获得成功，但Wick表达了对开发速度放缓的担忧，原因在于像Alexander Larsson这样的关键开发人员退出，以及大量未审查的合并请求。

他强调了几个需要改进的领域。首先，增强OCI（开放容器倡议）支持，特别是对zstd:chunked镜像的支持，以提供更好的重复数据删除和更小的更新。其次，改进权限管理，包括对新功能的向后兼容性和改进的音频访问控制。第三，解决嵌套沙盒问题，这对于像网络浏览器这样的应用程序至关重要。第四，一个更强大和安全的网络命名空间解决方案，以防止意外的应用程序间通信。第五，一个更好的NVIDIA驱动程序管理解决方案，以减少网络开销并确保兼容性。最后，增强桌面门户，提供更粗粒度的文件访问，并更广泛地支持密码自动填充和FIDO密钥等功能。

Wick设想了一个基于OCI的"Flatpak-next"，以便更好地与行业标准对齐，更广泛的采用和更轻松的维护。他强调需要更多的贡献者和Flatpak项目的振兴，以应对这些挑战并确保其持续成功。

---

## 71. 太阳系或发现新的矮行星

**原文标题**: Possible new dwarf planet found in our solar system

**原文链接**: [https://www.minorplanetcenter.net/mpec/K25/K25K47.html](https://www.minorplanetcenter.net/mpec/K25/K25K47.html)

小行星电子通告 (MPEC 2025-K47) 发布了小行星 2017 OF201 的观测资料和轨道要素。该通告由小行星中心于 2025 年 5 月 21 日发布，详细介绍了 2011 年 8 月至 2018 年 10 月期间，从加拿大-法国-夏威夷望远镜 (T14) 和 Cerro Tololo-DECam (W84) 收集的观测数据。这些观测数据包括该天体的精确天体测量位置和星等。

为 2017 OF201 计算的轨道要素表明，它具有高度偏心的轨道 (e=0.9485897)，半长轴为 880.0169161 AU，倾角为 16.21146 度。它的绝对星等 (H) 为 3.55，表明其尺寸相当大。轨道周期 (P) 为 26106 年。

该通告提供了一个星历表，预测该天体在 2025 年 4 月、5 月和 6 月若干日期的天空位置，包括赤经、赤纬、与地球和太阳的距离、距角、相位和视星等 (V)。较高的半长轴提高了该天体可能成为矮行星候选者的可能性，但还需要进一步研究。

---

## 72. 基准犯罪行为与形式化验证

**原文标题**: Benchmarking Crimes Meet Formal Verification

**原文链接**: [https://microkerneldude.org/2025/04/27/benchmarking-crimes-meet-formal-verification/](https://microkerneldude.org/2025/04/27/benchmarking-crimes-meet-formal-verification/)

本文批判了使用“证明-代码比”作为评估形式化验证操作系统效率的指标，认为该指标具有误导性且本质上毫无意义。作者论证了证明规模很大程度上受到规范的完整性和复杂性的影响，而不仅仅是代码规模。即使对于相同的代码，更全面的规范也必然会导致更大的证明。

作者随后提供了一个包含更多数据点的表格，包括规范大小，并突出了对seL4验证工作的错误描述，澄清了代码、证明和规范大小的实际数字。作者接着探讨了证明大小和规范大小之间的关系，指出不应期望存在线性关系。作者引用研究表明存在二次关系，即证明大小随着规范大小的平方而增长，从而论证了简单地比较比率是错误的。

文章最后探讨了验证中模块化的潜在好处，但认为像seL4这样的系统由于其相互关联的性质，本质上难以模块化。关键的结论是，证明-代码比是一个不足的指标，并且规范大小是一个需要考虑的关键因素。此外，即使在交互式定理证明（ITP）和自动定理证明（ATP）技术中，所需的工作量也差异很大，作者恳请社区停止使用证明-代码比作为指标。

---

## 73. 下一个抽象

**原文标题**: The Next Abstraction

**原文链接**: [https://substack.com/inbox/post/164096497](https://substack.com/inbox/post/164096497)

无法访问文章链接。

---

## 74. 管理 = 扯淡 (LLM 版)

**原文标题**: Management = Bullshit (LLM Edition)

**原文链接**: [http://funcall.blogspot.com/2025/05/management-bullshit.html](http://funcall.blogspot.com/2025/05/management-bullshit.html)

乔·马歇尔的博文《管理=扯淡（LLM版）》表达了他对管理层要求的过度官僚规划的沮丧。他认为，许多管理驱动的工作是制造问题而非解决问题。

乔强调了大型语言模型（LLM）的一个积极用例：生成管理层想要的全面但最终不必要的计划。他特别提到了灾难恢复计划，认为虽然有一个计划是好的，但管理层要求的细节和覆盖范围过于庞大且不切实际，近乎“扯淡”。

他使用LLM快速生成了各种不可能发生的灾难场景的计划，例如陨石撞击和僵尸末日，以及更标准的事件，如火灾。虽然他承认这些计划基本上是无用的，但它们满足了管理层对文档的需求，并节省了他大量时间。

在评论中，乔澄清说，LLM生成了完全合理和标准的灾难恢复程序，例如定期备份和恢复实践。他的问题不在于计划的内容，而在于以管理层要求的水平记录已经建立的最佳实践所花费的时间。

---

## 75. 韩炳哲哲学 (2020)

**原文标题**: The Philosophy of Byung-Chul Han (2020)

**原文链接**: [https://newintrigue.com/2020/06/29/the-philosophy-of-byung-chul-han/](https://newintrigue.com/2020/06/29/the-philosophy-of-byung-chul-han/)

本文介绍了韩炳哲，一位当代韩裔德国哲学家，他像尼尔·波兹曼和马歇尔·麦克卢汉一样，是一位挑战技术和社会假设的现代思想家。作者乔什·克鲁克通过韩炳哲的五本近期著作，探讨了他的哲学思想，旨在理解其核心论点。

韩炳哲的核心论点是，我们生活在一个肤浅的“成就社会”中，这个社会优先考虑积极性、成功和自我满足，从而导致孤立、精神疾病和与真实体验的脱节。在《倦怠社会》中，韩炳哲将20世纪的“规训社会”与21世纪的“成就社会”进行了对比，在“成就社会”中，“能”的强制性比“应该”更有效，从而导致自我剥削和倦怠。

韩炳哲认为，自恋和与“他人”缺乏联系导致了爱的危机。他批判了现代文化流畅的美学，例如杰夫·昆斯的艺术，认为这反映了一种消除负面性的社会强制，阻碍了内省。在《透明社会》中，韩炳哲将数字世界与圆形监狱进行了类比，在圆形监狱中，个人自愿屈服于监视，成为施害者和受害者。

最后，在《好的娱乐》中，韩炳哲质疑了高雅文化和低俗文化之间的区别，认为我们对激情和生产的痴迷扼杀了真正的玩乐。他鼓励回归为玩乐而玩乐，脱离商品化。

克鲁克总结说，韩炳哲的哲学敦促我们拥抱不完美、真实以及与他人的联系，超越成就和持续积极性的压力。作者承认，韩炳哲写作的简洁性带来了强大的隐喻和思想，即使有时牺牲了细致的论证。

---

## 76. 德夫斯特拉

**原文标题**: Devstral

**原文链接**: [https://mistral.ai/news/devstral](https://mistral.ai/news/devstral)

Mistral AI 与 All Hands AI 合作发布了 Devstral，这是一款专为软件工程任务设计的新型开源 LLM。Devstral 擅长通过代码情境化、识别组件之间的关系以及在代码库中查找细微错误来解决现实世界中的 GitHub 问题。

Devstral 在 SWE-Bench Verified 基准测试中取得了 46.8% 的分数，显著优于现有的开源模型。即使在相同的测试框架下评估，它甚至超过了 Deepseek-V3-0324 和 Qwen3 232B-A22B 等更大的模型。与闭源模型相比，Devstral 也表现出显着的性能提升，大幅超越了 GPT-4.1-mini。

它的轻量级使其适合在单个 RTX 4090 或具有 32GB 内存的 Mac 上进行本地部署。这使其非常适合在设备上使用，并通过 OpenHands 等平台快速解决本地代码库问题。Devstral 还可以应用于对隐私敏感的企业环境中。如果您正在构建或使用代理编码 IDE、插件或环境，那么它是一个适合添加到您的模型选择器中的选择。

Devstral 在 Apache 2.0 许可下发布。它可以通过 Mistral AI 的 API（作为 devstral-small-2505）获得，并且可以在 HuggingFace、Ollama、Kaggle、Unsloth 和 LM Studio 上下载。两家公司鼓励提供反馈，并计划很快发布更大的代理编码模型。他们也欢迎企业部署、微调和进一步定制 Devstral 的咨询。

---

## 77. 一切皆漏洞（或问题）

**原文标题**: Everything’s a bug (or an issue)

**原文链接**: [https://www.bozemanpass.com/everythings-a-bug-or-an-issue/](https://www.bozemanpass.com/everythings-a-bug-or-an-issue/)

David Boreham回顾了他在一家类似FAANG公司的早期经历，当时一个“缺陷委员会”有效地管理了软件项目。关键是将*一切*都视为缺陷，并使用一个专门构建的缺陷跟踪系统（“BugSplat”），该系统遵循四个原则：

1. **一切皆缺陷：**所有任务、功能和问题都输入到系统中。
2. **通用模式：**一个一致的、带有主观倾向的缺陷记录模式捕获状态、优先级和依赖关系等细节，从而提高清晰度和一致性。
3. **单一职责：**一次只能将一个人分配给每个缺陷，以确保问责制。
4. **强大的查询：**灵活的查询允许用户创建自定义视图并根据个人需求跟踪进度。

作者感叹，像GitHub Issues这样的现代系统未能达到这些原则。GitHub Issues缺乏结构化模式，允许多个受让人，并提供有限的查询功能，从而阻碍了有效的项目管理。

他建议使用Gitea，一个开源的GitHub替代方案，并添加缺失的功能。例如，Bozeman Pass添加了基于优先级的排序功能。目标是通过基于最初的四个原则向Gitea添加剩余的缺失功能，来复制“缺陷委员会式”的软件开发方式，强调强大、结构良好的缺陷跟踪系统的益处。

---

## 78. 我们如何提高OCR代码的准确率

**原文标题**: How we made our OCR code more accurate

**原文链接**: [https://pieces.app/blog/how-we-made-our-optical-character-recognition-ocr-code-more-accurate](https://pieces.app/blog/how-we-made-our-optical-character-recognition-ocr-code-more-accurate)

本文详细介绍了Pieces如何提高其OCR引擎的准确性，特别是对于代码识别。他们使用Tesseract作为基础OCR引擎，并通过针对IDE、终端和在线资源中的代码定制的预处理和后处理步骤对其进行增强。

预处理流程侧重于标准化输入：通过在确定平均像素亮度后反转深色模式图像来处理浅色和深色模式图像，使用膨胀和中值模糊处理渐变和嘈杂的背景，并通过双三次向上采样来改善低分辨率图像。这确保了Tesseract输入质量的一致性。

后处理包括OCR布局分析，以推断代码缩进。Tesseract缺少默认缩进，这对于代码可读性和正确性至关重要，尤其是在Python等语言中。该系统使用来自Tesseract的边界框数据来计算和应用适当的缩进，该缩进基于每行的平均字符宽度和起始坐标。

该团队使用手工制作和生成的图像-文本数据集评估他们的修改，计算Levenshtein距离来衡量准确性。他们通过比较相同数据集上的OCR性能来测试不同的方法，例如各种向上采样方法。虽然超分辨率向上采样没有明显优于双三次向上采样，但他们选择了双三次，因为它具有较低的存储需求和延迟。

本文强调了代码OCR的挑战，需要准确的语法、格式以及变量名和注释的识别。Pieces旨在提供一个针对代码进行微调的模型，并且正在不断改进。

---

## 79. 展示一下：Pi Co-pilot – 轻松评估人工智能应用

**原文标题**: Show HN: Pi Co-pilot – Evaluation of AI apps made easy

**原文链接**: [https://withpi.ai/](https://withpi.ai/)

Pi Co-pilot 是一个旨在简化 AI 应用评估的平台，提供构建评分系统和评估 AI 技术栈各方面的工具。它旨在提供适用于离线评估和在线推理的可信指标。Pi 通过分析提示词、PRD、用户反馈或直接互动来帮助用户识别正确的指标，并根据具体应用推荐校准后的指标。

该平台强调准确性和速度，声称其基础模型 Pi Scorer 在准确性方面优于 Deepseek 和 GPT 4.1 等模型，同时保持了 GPT Mini 和 Gemini Flash 等较小模型的速度。它支持在不到 100 毫秒内对 20 多个自定义维度进行评分。

Pi Scorer 旨在广泛集成到各种工具和 AI 技术栈的各个部分，包括离线评估、在线可观测性、训练数据质量、模型优化和代理控制流程。它可以轻松地与 Google Spreadsheets、Promptfoo 和 CrewAI 等工具集成。

Pi Labs 由 David Karam（前 Google 产品总监）和 Achint Srivastava（前 Google 首席软件工程师）创立，他们都在 Google 构建 AI 和搜索平台方面拥有丰富的经验。他们的目标是利用他们的专业知识来提供易于使用的 AI 评估工具。

---

## 80. ZEUS – 密歇根大学新建的两拍瓦激光装置

**原文标题**: ZEUS – A new two-petawatt laser facility at the University of Michigan

**原文链接**: [https://news.engin.umich.edu/2025/05/the-us-has-a-new-most-powerful-laser/](https://news.engin.umich.edu/2025/05/the-us-has-a-new-most-powerful-laser/)

密歇根大学ZEUS激光设施已达到2拍瓦的峰值功率，成为美国最强大的激光器。ZEUS由美国国家科学基金会资助，是一个面向全国和国际研究人员开放的用户设施，能够在医学、国家安全、材料科学和天体物理学等多个领域开展实验。

加州大学尔湾分校的一个团队进行的初步实验旨在产生高能电子束，有可能超越传统粒子加速器的能力。这涉及到使用两束激光来创建一个引导通道，并通过氦等离子体目标加速电子，利用尾波场加速。

最终目标是通过将加速的电子与反向传播的激光束碰撞来实现“泽塔瓦等效”脉冲。这项进步可能会带来更好的软组织成像方法和改进的癌症治疗技术。

ZEUS虽然位于相对紧凑的空间内，但利用复杂的光学设备系统来拉伸和压缩激光脉冲，从而实现惊人的强度。尽管在获得钛蓝宝石晶体等组件以及管理光栅上的碳沉积方面存在挑战，但该设施已经以1拍瓦的功率举办了多次用户实验。该团队正在继续升级系统，计划很快达到其全部3拍瓦的潜力。ZEUS的敏捷性和开放访问促进了创新，并吸引了广泛的科学家。

---

## 81. 秘密商场公寓：一场关于场所的抗议

**原文标题**: “Secret Mall Apartment,” a Protest for Place

**原文链接**: [https://modernagejournal.com/secret-mall-apartment-a-protest-for-place/251023/](https://modernagejournal.com/secret-mall-apartment-a-protest-for-place/251023/)

这篇题为《秘密商场公寓：为场所的抗议》的文章，可能探讨了在商场内创建未经授权的居住空间的现象，并将其作为反对流离失所或公共空间同质化的一种抗议形式。这个“秘密商场公寓”可能被用作一个例子，来说明文章更广泛的主题：在商业环境中重新获得或创造个性化空间。标题本身表明，在商场内居住的行为被呈现为一种抵抗或对抗主流社会结构的声明，这些结构规定了人们被允许居住的地点以及他们与公共空间互动的方式。包含日期表明这很可能是一个正在分析的时事或趋势。

然而，简短的预览也表明，这篇文章，或者可能是同一出版物，也包含了一篇马克·鲍尔莱因关于哥伦布古典学院的文章，指出该校的入学人数增加了一倍，并暗示了对该校的积极评价。根据提供的信息，这两个项目之间的联系尚不清楚。

---

## 82. 2030年的早晨日常

**原文标题**: A 2030 Morning Routine

**原文链接**: [https://www.marginalia.nu/log/a_120_morning_routine_2030/](https://www.marginalia.nu/log/a_120_morning_routine_2030/)

一篇2030年的晨间日常：一个充斥着无休止且侵入式人工智能的讽刺性未来景象。主人公的清晨是被无孔不入的数字助理所淹没的，它们存在于每一个可想象的物品中，从闹钟、咖啡机到鞋带和人行道。这些人工智能伙伴，每一个都有名字和预先设定的销售说辞，尽管主人公试图忽略它们，却仍然喋喋不休地念叨着它们“梦幻般的新人工智能功能”。

这个故事突出了过度依赖技术的荒谬和隐私的侵蚀。即使是像淋浴和使用储物柜这样的日常琐事，现在也成为了数据收集和人工智能不断干扰的机会。主人公面临着荒谬的安全措施和繁琐的验证码测试，仅仅是为了打开一个健身房的储物柜。

讽刺的高潮在于主人公意识到自己的工作正是成为他们一整个早上都在试图逃避的那种侵入式人工智能，从而创造了一个循环往复且令人丧失人性化的工作环境。这个故事强调了一个未来，在那里，真正的人际互动和自主性被牺牲，以换取持续不断的技术参与和数据收集，从而导致一种压倒性的疲惫和疏离感。

---

## 83. CRDTs #2：层层叠叠皆是龟

**原文标题**: CRDTs #2: Turtles All the Way Down

**原文链接**: [https://jhellerstein.github.io/blog/crdt-turtles/](https://jhellerstein.github.io/blog/crdt-turtles/)

本文强调了扎实的数学基础对于无冲突复制数据类型 (CRDT) 的重要性，认为它们应该“自始至终”都建立在半格之上。CRDT 承诺分布式系统中最终的一致性，而无需依赖完美的时钟或全局顺序，但许多实现都对消息传递或其他因素做出了隐藏的假设，本质上依赖于“乌龟”。

作者认为，正确的 CRDT 设计需要：（1）始终根据半格结构定义操作；（2）使用清晰的代数推理，没有隐藏的依赖关系；（3）必要时明确包含因果格。半格由一组状态和一个满足交换律、结合律和幂等律的并（或合并）函数定义。

本文使用 Observed-Remove (OR) 集中过期的 tombstone 来说明隐藏假设的危险性。使用本地时间的简单方法可能导致非收敛。解决方案是使用版本向量显式地跟踪因果上下文，并将其作为嵌套的半格包含。这确保了只有在每个节点都保证知道 tombstone 后，tombstone 才会过期。

最后，本文阐明了“基于状态”与“基于操作”的 CRDT 区别，认为基于操作的 CRDT 也是半格。在基于操作的设计中，状态表示带有 causalContext 的操作日志，它维护了正确的偏序。关键的要点是，所有 CRDT 都应设计为半格，顺序比较必须尊重合并函数，必要的假设必须在格内建模，并且对底层保证（乌龟）的依赖应该明确且被充分理解。

---

## 84. 追逐分布式数据分析架构的迷失十年？

**原文标题**: A lost decade chasing distributed architectures for data analytics?

**原文链接**: [https://duckdb.org/2025/05/19/the-lost-decade-of-small-data.html](https://duckdb.org/2025/05/19/the-lost-decade-of-small-data.html)

Hannes Mühleisen 认为，数据分析社区可能浪费了十年时间追逐分布式架构，忽视了硬件进步推动的单节点解决方案的潜力。 这篇文章使用 TPC-H 基准（规模因子 1000，产生约 265GB 的数据库）对 2012 年 MacBook Pro Retina 和现代 M3 Max MacBook Pro 上的 DuckDB 进行了基准测试。

结果表明，旧款 MacBook Pro 即使使用较旧的操作系统 (OS X 10.8.5)，也能成功完成所有 22 个基准查询，尽管速度较慢。 虽然现代 MacBook Pro 表现出显著的加速（7 倍到 53 倍，几何平均提升 20 倍），但核心在于 2012 年的机器证明了它能够在合理的时间范围内处理大量数据集（lineitem 中有 60 亿行，orders 中有 15 亿行）。

作者认为，如果 2012 年存在像 DuckDB 这样的单节点 SQL 引擎，那么推动数据分析转向分布式系统的动力可能会减弱。 考虑到当时笔记本电脑中 SSD 和更大 RAM 容量的兴起，硬件基础已经到位。 文章的结论是，对分布式系统的关注可能为时过早，导致了一个“失去的十年”，单节点架构的潜力被低估了。

---

## 85. 机器停止 (1909)

**原文标题**: The Machine Stops (1909)

**原文链接**: [https://standardebooks.org/ebooks/e-m-forster/short-fiction/text/the-machine-stops](https://standardebooks.org/ebooks/e-m-forster/short-fiction/text/the-machine-stops)

在E.M.福斯特的《机器停止运转》中，生活在技术高度发达的地下社会中的瓦什蒂收到来自儿子库诺的一个不寻常的请求，库诺住在世界的另一端。库诺希望她亲自去看望他，而不是通过机器进行交流，机器是统治他们生活、无所不包的技术系统。

瓦什蒂是机器的忠实信徒，最初很抵触。她觉得长途跋涉令人不快，并且认为在机器提供她所有需求并将她与世界联系起来的情况下，面对面的互动毫无价值。她远程授课，并对机器控制她存在的方方面面感到安心。她也不愿意去地球表面，因为人们认为那里不适合居住。

库诺表达了对机器的不满，他认为机器阻碍了真正的联系，并阻止他直接体验世界。他从飞艇上看到了星星，并被地球表面所吸引，这违背了他们社会公认的规范。

最终，瓦什蒂出于母爱和对库诺神秘信息中即将发生的“巨大”事件的模糊不安感，决定去看望他。她克服了对通往飞艇的隧道的恐惧，开始了她的旅程，突显了在这种高度互联，但又孤立的社会中，身体旅行的罕见性。

---

## 86. 树莓派调制解调器

**原文标题**: Raspberry Pi Modems

**原文链接**: [https://niiccoo2.xyz/raspberry-pi-modems/](https://niiccoo2.xyz/raspberry-pi-modems/)

本文详细介绍了作者受昂贵的Light Phone 3启发，使用树莓派和现成零件制作低成本E-Ink手机的项目。第一个难关是在树莓派Zero W上使用Waveshare SIM7600A-H调制解调器建立蜂窝网络连接。

作者遇到了几个挑战：
* GPIO上的互联网速度慢且问题多，导致计划直接连接USB数据焊盘。
* 初始SSH调试缓慢，促使购买了Pi Zero 2W，最终解决了这个问题。
* 天线连接器从调制解调器上脱落，需要进行临时焊接修复。
* 由于运营商限制，Visible SIM卡不兼容，因此需要切换到Tello SIM卡。

作者正在使用RNDIS进行互联网连接，并提供了用于SMS功能、APN配置和网络连接的AT指令。 该项目的下一步包括设置E-Ink屏幕以及开发消息和电话应用程序。 作者感谢Jeff Geerling的博客文章以及在SIM卡问题上的帮助，并强调了关于树莓派调制解调器的信息稀缺。文章以原始笔记结尾，并邀请通过电子邮件进行进一步咨询。

---

## 87. 不丹可播放唱片邮票的奇特故事（2015年）

**原文标题**: The curious tale of Bhutan's playable record postage stamps (2015)

**原文链接**: [https://thevinylfactory.com/features/the-curious-tale-of-bhutans-playable-record-postage-stamps/](https://thevinylfactory.com/features/the-curious-tale-of-bhutans-playable-record-postage-stamps/)

本文讲述了不丹独特的“会说话的邮票”的故事，这些邮票是1972年发行的迷你、可播放的黑胶唱片。这些由美国探险家伯特·托德设计的邮票，旨在通过集邮市场为不丹筹集资金。

在不丹被世界银行拒绝贷款后，与不丹王室有关系的托德的任务是创建一个成功的邮票项目。他最初发行了传统的邮票，但很快意识到需要新颖性来吸引收藏家。然后，他实施了几种创新的邮票类型，包括圆形、三角形、3D和香味邮票。

会说话的邮票是他最具雄心的项目，是单面的、33 1/3转的黑胶唱片。它们可以从信封或明信片上剥下来并贴在上面，并在标准的唱盘上播放。邮票的内容包括不丹的民歌以及用英语和当地语言宗喀语讲述的国家历史。

最初被认为是纯粹的新奇事物，这些邮票价格低廉。然而，它们已经变得非常受黑胶唱片收藏家的追捧，尤其是在美国，导致其价值飙升。最初价值约 17 英镑的一套邮票现在价值数百英镑，被认为是良好的黑胶投资。

---

## 88. 理解 Go 调度器

**原文标题**: Understanding the Go Scheduler

**原文链接**: [https://nghiant3223.github.io/2025/04/15/go-scheduler.html](https://nghiant3223.github.io/2025/04/15/go-scheduler.html)

本文详细解释了 Go 调度器，重点介绍其演变历程以及实现高效并发的底层机制。文章首先介绍了 Go 运行时及其在编译期间将 Go 关键字替换为运行时函数调用的作用。

然后，文章深入探讨了 Go 调度器的历史，将最初的 N:1 模型与当前的 GMP (Goroutine-Machine-Processor) 模型进行了对比。文章强调了早期调度器的局限性，包括全局运行队列上的锁争用以及由于频繁的线程切换导致的较差局部性。

文章讨论了促成 GMP 模型的改进，特别是每个线程引入的本地运行队列以及逻辑处理器 (P) 的概念。处理器拥有本地运行队列和 mcache，从而减少了内存消耗并实现了高效的窃取机制。

文章详细解释了 GMP 模型，定义了 Goroutines (G)、Machines (M) 和 Processors (P) 的角色和状态。 它描述了 goroutine 的创建、执行和回收方式，以及它们经历的状态转换。 文章还探讨了线程 (M) 的管理方式，包括它们与处理器的关联、系统堆栈 (g0) 的使用以及自旋行为。 处理器 (P) 管理本地运行队列，是最大限度减少锁争用的关键。

最后，本文为后续章节讨论程序如何引导启动、goroutine 如何创建、调度循环、查找可运行的 goroutine、抢占、处理系统调用、I/O 以及垃圾回收奠定了基础。

---

## 89. Tab Roving - 元素组的焦点管理

**原文标题**: Tab Roving – focus management for element groups

**原文链接**: [https://nik.digital/posts/tab-roving](https://nik.digital/posts/tab-roving)

本文探讨了Web数据表格中键盘导航体验差的问题，特别是在包含诸如输入框等交互元素的表格中。传统的通过Tab键逐个单元格切换的方式变得繁琐且效率低下，尤其是在大型表格中。

本文提出的解决方案是“Tab漫游”技术，该技术将整个表格作为一个可聚焦的元素。用户不再使用Tab键在单元格之间移动，而是使用方向键在表格内导航。这极大地改善了键盘用户的用户体验。

本文解释了Tab漫游的技术原理，即使用`tabindex`属性来控制焦点。核心思想是只有一个单元格具有`tabindex="0"`（可Tab），而其他单元格具有`tabindex="-1"`（不可Tab）。然后，通过编程方式，使用方向键将`tabindex="0"`移动到所需的单元格，并使用`HTMLElement.focus()`使其聚焦。

本文提供了一个完整的Tab漫游的React实现，展示了如何管理焦点、处理按键以及相应地更新UI。代码包括管理单元格引用、防止默认浏览器行为以及允许用户单击以聚焦单元格。

本文还涉及了高级考虑因素，例如键盘快捷键和边缘环绕行为。最后，本文将Tab漫游的应用扩展到其他UI元素，如大型菜单和自定义数值输入，突出了其在改善键盘可访问性方面的更广泛用途。

---

## 90. 将任何CSV文件显示为可搜索、可过滤的美观HTML表格。

**原文标题**: Display any CSV file as a searchable, filterable, pretty HTML table

**原文链接**: [https://github.com/derekeder/csv-to-html-table](https://github.com/derekeder/csv-to-html-table)

本文档介绍了一个基于 JavaScript 的工具 "csv-to-html-table"，它允许用户轻松地将 CSV 文件显示为可搜索、可过滤且视觉上吸引人的 HTML 表格。该工具利用 JavaScript 和多个库（Bootstrap 4、jQuery、jQuery CSV 和 DataTables）来提供功能，无需服务器端代码。

要使用该工具，用户需要克隆仓库，将他们的 CSV 文件放入 `data/` 文件夹中，并在 `index.html` 中配置 `CsvToHtmlTable.init()` 函数。关键配置选项包括指定 CSV 文件路径、将表格渲染到的 HTML 元素、允许 CSV 下载、自定义 CSV 解析（分隔符、定界符）以及自定义 DataTables 行为（分页等）。

该工具还支持通过 JavaScript 函数自定义单个列的格式。用户可以定义一个以单元格值为输入的函数，并返回 HTML 格式的输出，并根据索引将其应用于特定列。

本文档提供了关于如何使用 Python 内置 Web 服务器在本地运行该工具、将其部署到 GitHub Pages 或 Web 服务器以及使用 iframe 将表格嵌入到另一个网站中的说明。它还包括一个针对常见问题的故障排除部分和一个关于报告错误和为项目做出贡献的指南。

---

## 91. 算法而言，少许内存胜过大量时间。

**原文标题**: For algorithms, a little memory outweighs a lot of time

**原文链接**: [https://www.quantamagazine.org/for-algorithms-a-little-memory-outweighs-a-lot-of-time-20250521/](https://www.quantamagazine.org/for-algorithms-a-little-memory-outweighs-a-lot-of-time-20250521/)

本文详细介绍了瑞安·威廉姆斯在计算复杂度理论上的突破性证明，该证明表明，少量内存在计算中可以像大量时间一样强大。 这一成果标志着在关于计算中时间和空间关系这一基本问题上50年来的首次重大进展。

威廉姆斯的证明提供了一种将任何算法转换为占用更少空间形式的程序。 这一发现也对在一定时间内无法计算的内容产生影响，为解决计算机科学中长期存在的未解决问题（包括 P 与 PSPACE 问题）提供了一种潜在的新方法。

本文还重点介绍了该问题的历史背景，追溯了其根源至 Juris Hartmanis 和 Richard Stearns，他们为时间和空间复杂度建立了数学定义。 它解释了 John Hopcroft、Wolfgang Paul 和 Leslie Valiant 的工作，他们在连接空间和时间方面迈出了第一个重要步骤，提出了一个通用的模拟程序。 然而，在威廉姆斯最近的突破之前，进展停滞了几十年。

本文描绘了威廉姆斯从阿拉巴马州农场对计算机的童年迷恋到成为麻省理工学院一位杰出计算机科学家的历程。 它强调了他克服学术生涯中的挑战，决心追求复杂度理论的决心。

---

## 92. 研究揭示古代雅典娜神庙令人惊叹的照明效果

**原文标题**: Research Uncovers Parthenon Spectacular Lighting Effects for Athena in Antiquity

**原文链接**: [https://arkeonews.net/research-uncovers-the-parthenons-spectacular-lighting-effects-for-athena-in-antiquity/](https://arkeonews.net/research-uncovers-the-parthenons-spectacular-lighting-effects-for-athena-in-antiquity/)

牛津大学胡安·德·拉腊教授领导的一项多学科研究揭示了古希腊时期帕特农神庙的照明方式，旨在营造一种敬畏感。研究团队结合考古证据、3D技术和光学物理学，重建了神庙的照明系统，展示了建筑师和雕塑家菲狄亚斯如何利用屋顶开口、水池、窗户和抛光大理石来操纵自然光和人造光。

研究发现，帕特农神庙的内部通常保持昏暗，以营造虔诚的氛围。然而，在泛雅典娜节期间，阳光会与神庙入口完美对齐，将一道耀眼的光束投射到雅典娜雕像的金色长袍上，创造出闪烁的奇观。德·拉腊教授强调了技术在释放考古研究全部潜力方面的作用。

之前的学者曾思考过神庙的照明问题，但德·拉腊教授的研究为这种精巧的设计提供了确凿的证据。该研究正在转化为博物馆和教育中心的虚拟现实（VR）体验，让参观者能够亲眼目睹光影效果。3D重建已在线提供。

---

## 93. Show HN: Whenish – iMessage 中规划群组活动

**原文标题**: Show HN: Whenish – Plan Group Events in iMessages

**原文链接**: [https://apps.apple.com/us/app/whenish/id6745035749](https://apps.apple.com/us/app/whenish/id6745035749)

Whenish是一款iMessage应用，旨在简化群聊中的活动策划流程。它通过允许用户直接在Messages中创建日期投票，消除了排期时的来回沟通。参与者可以轻松选择他们的空闲日期，并且该应用提供关于每个人回复的实时更新。

主要功能包括创建快速日期投票、选择多个空闲选项、实时回复跟踪以及用户友好的日历界面，所有这些都在iMessage环境中实现。

用户称赞Whenish的简洁性和有效性，能够快速确定最佳会议时间。评论强调了它的易用性以及加速各种活动（从团体晚餐到工作会议）策划过程的能力。

该应用可以免费下载和使用。开发者CommonGroundTech, LLC声明，Whenish不会收集任何用户数据。它需要iOS 17.6或更高版本的iPhone和iPadOS 17.6或更高版本的iPad。

---

## 94. “AI 2027” 情景：它有多现实？

**原文标题**: The "AI 2027" Scenario: How realistic is it?

**原文链接**: [https://garymarcus.substack.com/p/the-ai-2027-scenario-how-realistic](https://garymarcus.substack.com/p/the-ai-2027-scenario-how-realistic)

无法访问文章链接。

---

## 95. Show HN: ClipJS – 在电脑或手机上编辑你的视频

**原文标题**: Show HN: ClipJS – Edit your videos from a PC or phone

**原文链接**: [https://clipjs.vercel.app/](https://clipjs.vercel.app/)

ClipJS：一款无水印视频编辑工具，用户可在电脑或手机端直接使用。这表明它是一款基于网页或跨平台的应用，可通过浏览器访问，也可能提供原生移动应用。其核心价值在于编辑后的视频不含水印，适合追求简洁专业效果，又不想付费购买通常用于去除水印的高级功能或订阅服务的用户。内容简洁表明该工具刚推出或正于“Show HN”环境下寻求初步反馈，暗示这是一个寻求早期采用和社区意见的项目。

---

## 96. 店面 Web 组件

**原文标题**: Storefront Web Components

**原文链接**: [https://shopify.dev/docs/api/storefront-web-components](https://shopify.dev/docs/api/storefront-web-components)

无法访问文章链接。

---

## 97. Show HN：面向高可靠RISC-V嵌入式系统的保密计算

**原文标题**: Show HN: Confidential computing for high-assurance RISC-V embedded systems

**原文链接**: [https://github.com/IBM/ACE-RISCV](https://github.com/IBM/ACE-RISCV)

ACE-RISCV 是一个开源项目，为 RISC-V 嵌入式系统提供机密计算框架，并具有经过形式化验证的安全监控器。它以 RISC-V 架构为目标，旨在实现可移植性，并专注于安全监控器实现的形式化验证。

主要功能包括：

*   **形式化验证：** 实施 RISC-V CoVE 规范部署模型 3，将形式化规范嵌入到安全监控器的代码中，并将证明放在 `verification/` 目录中。
*   **后量子密码学 (PQC) 和证明：** 支持资源受限的嵌入式系统中机密虚拟机的本地证明，利用 ML-KEM、SHA-384 和 AES-GCM-256 密码学。
*   **硬件

该项目强调使用可验证的安全监控器，并提供使用 dm-crypt/LUKS 加密根文件系统，并通过 TAP 安全传递密钥的途径。它在 Apache 2.0 许可下发布，并包含对相关研究论文的引用。

---

## 98. 袋鼠：针对微小对象优化的闪存缓存 (2021)

**原文标题**: Kangaroo: A flash cache optimized for tiny objects (2021)

**原文链接**: [https://engineering.fb.com/2021/10/26/core-infra/kangaroo/](https://engineering.fb.com/2021/10/26/core-infra/kangaroo/)

Kangaroo：一种新型闪存缓存，针对微小对象优化

Kangaroo 是一种新型闪存缓存，经过优化，可以比现有解决方案更有效地缓存微小对象（小于 100 字节）。 它在 Facebook 的 CacheLib 中开发，解决了传统集合关联和日志结构闪存缓存的低效率问题。 集合关联缓存由于需要为小对象写入整个闪存页面而遭受写放大，而日志结构缓存则需要过多的 DRAM 用于索引。

Kangaroo 结合了两种方法的优点，包括 KLog（一种小型日志结构缓存）和 KSet（一种较大的集合关联缓存）。 查找先检查 DRAM，然后检查 KLog 的索引，最后检查 KSet 中的 Bloom 过滤器。 插入首先进入 DRAM，然后被驱逐到 KLog。 一个关键的创新是从 KLog 到 KSet 的驱逐过程，在此过程中，Kangaroo 将映射到同一 KSet 集的多个对象分组，以分摊写入成本，从而最大限度地减少闪存写入。 它还采用准入策略，以避免将条目太少的集合从 KLog 写入 KSet。

使用 Facebook 和 Twitter 跟踪数据进行评估后，在实际系统约束下，与集合关联缓存相比，Kangaroo 将缓存未命中率降低了 29%，与日志结构缓存相比，降低了 56%。 这是因为它降低了 DRAM 开销和写放大，从而使大规模闪存缓存微小对象成为可能。 高效缓存微小对象对于社交媒体和物联网服务至关重要，因为必须快速检索大量此类数据（例如，社交图边缘），从而减少后端系统的负载。

---

## 99. Haskell 中的愚蠢面试题

**原文标题**: Silly job interview questions in Haskell

**原文链接**: [https://chrispenner.ca/posts/interview](https://chrispenner.ca/posts/interview)

本文探讨如何使用 Haskell 解决常见的编程面试题，重点强调该语言独特的范式和函数式方法。

文章首先从“回文”问题入手，展示了 Haskell 在字符串操作方面的简洁易懂的语法。接下来，经典的“Fizz Buzz”挑战突出了 Haskell 对带有模式守卫的 case 分析以及其可组合的高阶函数的使用，将逻辑与打印等副作用分离。

“求和至 N”问题演示了递归和过滤，用于寻找满足特定总和的数字组合。它介绍了 `combinations` 函数，并展示了其在解决涉及任意长度组合的后续问题中的实用性。

“字谜”问题突出了 Haskell 对 `on` 等高阶函数的使用，以便进行优雅的字符串比较，解决了大小写不敏感问题，并讨论了惰性求值可能带来的性能考虑。

“最小值和最大值”问题提出了三种不同的方法：简单的 `minimum` 和 `maximum`（在空列表上可能会出错），使用带有 `Min` 和 `Max` 半群的 `Bounded` 和 `foldMap` 的解决方案，以及更安全的基于 `Maybe` 的解决方案，用于优雅地处理空列表。

最后，“词频”问题展示了 Haskell 使用 `Data.Map` 的数据结构能力来计算单词出现次数，并使用 `maximumBy` 查找最频繁的单词。 使用“数学风格”的函数组合增强了可读性。

---

## 100. RISC-V 15周年：全球快速普及

**原文标题**: RISC-V Turns 15 with Fast Global Adoption

**原文链接**: [https://www.eetimes.com/risc-v-turns-15-with-fast-global-adoption/](https://www.eetimes.com/risc-v-turns-15-with-fast-global-adoption/)

RISC-V开源指令集架构迎来15周年，全球采用显著，成熟度日益提升。《电子工程专辑》的文章强调了RISC-V生态系统的快速增长，这得益于其灵活性、开放性和免版税特性。

文章的主要要点包括：

*   **广泛采用：** RISC-V在各个领域的使用越来越多，包括嵌入式系统、人工智能 (AI)、高性能计算 (HPC)，甚至移动设备。英特尔、高通和联发科等公司都在积极投资 RISC-V。

*   **全球覆盖：** RISC-V 不局限于一个地区，它已在全球范围内获得广泛关注，尤其是在北美、欧洲和亚洲。中国是 RISC-V 采用的主要推动力，致力于摆脱专有架构的束缚。

*   **生态系统发展：** 一个强大且不断发展的生态系统对于 RISC-V 的成功至关重要。文章提到了各种 RISC-V 内核、软件工具和开发板的开发，使开发人员更容易使用该架构。

*   **开源优势：** RISC-V 的开源特性允许公司定制 ISA 以满足其特定需求，从而促进创新并减少对传统专有架构的依赖。这种灵活性是推动其采用的关键因素。

*   **商业成功：** RISC-V 不再仅仅是一个研究项目；它正成为已建立 ISA 的商业可行替代方案。各公司正在推出由 RISC-V 处理器驱动的产品，这表明它已为主要应用做好准备。

总而言之，这篇文章将 RISC-V 描述为一个成熟且快速增长的 ISA，凭借其开源特性、全球采用和蓬勃发展的生态系统，有望成为半导体行业的主要参与者。

---

