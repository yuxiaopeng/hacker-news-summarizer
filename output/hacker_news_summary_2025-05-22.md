# Hacker News 热门文章摘要 (2025-05-22)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 克劳德 4

**原文标题**: Claude 4

**原文链接**: [https://www.anthropic.com/news/claude-4](https://www.anthropic.com/news/claude-4)

Anthropic 发布 Claude 4，推出两款新模型：Claude Opus 4 和 Claude Sonnet 4。Opus 4 是最强大的模型，擅长编码和复杂问题解决，性能超越所有 Sonnet 模型，并被认为是世界最佳编码模型。Sonnet 4 是 Sonnet 3.7 的升级版，提供卓越的编码和推理能力，并将成为全新 GitHub Copilot 编码代理的基础。

主要改进包括使用工具进行扩展思考（测试版），如网络搜索、并行工具执行、改进的指令遵循以及增强的本地文件访问记忆能力。Claude Code 现已全面推出，并集成 VS Code 和 JetBrains。同时发布了新的 API 功能。

这两款模型都提供混合模式：近乎即时的响应和扩展的思考。它们可在 Anthropic API、Amazon Bedrock 和 Google Cloud 的 Vertex AI 等多个平台上使用。Opus 4 的价格为每百万 tokens 15 美元/75 美元（输入/输出），Sonnet 4 的价格为 3 美元/15 美元。

Opus 4 在 SWE-bench (72.5%) 和 Terminal-bench (43.2%) 上领先。Sonnet 4 在 SWE-bench 上达到 72.7%。Claude 4 模型还表现出减少的捷径行为和改进的记忆能力，特别是 Opus 4，它利用“记忆文件”来实现长期任务感知。

Claude Code 包括针对 IDE 的全新测试版扩展程序和一个可扩展的 Claude Code SDK。这些模型经过了广泛的安全测试，并实施了更高的 AI 安全级别 (ASL-3)。

---

## 2. 在我墙上挂了12年的那个分形图

**原文标题**: That fractal that's been up on my wall for 12 years

**原文链接**: [https://chriskw.xyz/2025/05/21/Fractal/](https://chriskw.xyz/2025/05/21/Fractal/)

作者在本文中详细阐述了他们对贴在墙上12年之久的碎形（昵称“壁花”）的探索。这个碎形最初是作者在初中时通过重复平铺和旋转正方形而创建的。经过多年的数学教育后，作者重新审视了这个碎形，意识到它可以用L系统生成。然而，最初的L系统生成的是另一种有充分文献记载的碎形（二次科赫岛）。关键的区别在于如何放置前一次迭代的副本：“壁花”将副本直接放置在上方、下方和侧面，而标准的L系统将它们对角放置。

然后，作者深入研究了如何用基于矩阵的数字系统来表示该碎形的结构。通过以特定顺序为正方形分配数字，他们发现了模式，并将正方形的位置表示为向量。这使得他们找到一个矩阵M，当该矩阵自乘并应用于“数字向量”时，可以准确地预测碎形中正方形的位置。

至关重要的是，他们发现矩阵的行列式至关重要。负行列式会在每次迭代时翻转碎形的朝向，从而生成“壁花”变体。正行列式会生成更常见的二次科赫岛。他们还表明，行列式的大小决定了碎形的缩放因子，偏离+/-5的行列式会导致碎形迭代中出现间隙或重叠。因此，看似任意的初始旋转角度与行列式和所使用的矩阵的结构有关。

---

## 3. 提高 rav1d 视频解码器的性能

**原文标题**: Improving performance of rav1d video decoder

**原文链接**: [https://ohadravid.github.io/posts/2025-05-rav1d-faster/](https://ohadravid.github.io/posts/2025-05-rav1d-faster/)

本文详细介绍了作者为提升rav1d（dav1d AV1视频解码器的Rust移植版本）性能所做的努力，目标是提高1%的速度。作者利用采样分析器(samply)，将rav1d的性能与dav1d进行比较，重点关注共享的汇编函数作为锚点。

初步分析显示，`cdef_filter`函数存在差异，与dav1d不同，rav1d在将其传递给汇编代码之前不必要地将一个临时缓冲区(`tmp_buf`)归零。 解决方案包括使用`MaybeUninit`来避免初始化，从而提高性能。 另一个优化涉及将`lr_bak`的初始化提升到`rav1d_cdef_brow`循环之外，避免冗余初始化。

使用“反向堆栈”视图的进一步分析突出了`add_temporal_candidate`函数中的性能差异。 作者发现，对`Mv`结构体（包含两个i16字段）进行逐字段相等性检查比dav1d将`Mv`结构体视为u32进行比较的方法要慢。 作者建议使用`transmute`将`Mv`重新解释为u32，以实现更快的相等性检查。

这些优化使得rav1d在特定基准测试中的运行时提高了1.5%（1.2秒），涵盖了rav1d和dav1d之间大约20%的性能差距。 作者强调了剖析和理解代码底层性能特征以识别优化机会的重要性。

---

## 4. Ruby 3.5 中的快速内存分配

**原文标题**: Fast Allocations in Ruby 3.5

**原文链接**: [https://railsatscale.com/2025-05-21-fast-allocations-in-ruby-3-5/](https://railsatscale.com/2025-05-21-fast-allocations-in-ruby-3-5/)

本文详细介绍了 Ruby 3.5 中一项显著的优化，该优化加速了对象分配，特别是 `Class#new` 内部的分配。该优化实现了高达 6.5 倍的加速，在使用关键字参数和 YJIT 时尤其明显。

作者最初的目标是用 Ruby 重写 `Class#new`，利用参数转发。然而，内联缓存未命中的问题导致与笹田耕一和 John Hawthorn 合作，通过使用新的 YARV 指令 (`opt_new`) 将 `Class#new` 逻辑直接“内联”到字节码中来实现优化。

内联消除了单独调用 `Class#new` 方法的开销，包括在 Ruby 堆栈和 C 寄存器之间复制参数的需要（对于关键字参数来说，尤其昂贵，因为在之前的版本中需要分配哈希）。这种方法减少了推送和弹出堆栈帧的需要，并通过将 `initialize` 调用站点分布在所有 `new` 调用中来提高内联缓存命中率。

本文展示了在有和没有 YJIT 的情况下，位置参数和关键字参数的加速比基准测试。虽然有效，但内联也存在一些小的缺点：指令大小增加（仅增加 0.5%）以及影响堆栈跟踪输出的向后不兼容，因为不再存在 `Class#new` 帧。总的来说，该优化显著提高了 Ruby 3.5 中的分配性能。

---

## 5. Mozilla将于2025年7月8日关闭Pocket。

**原文标题**: Mozilla to shutdown Pocket on July 8, 2025

**原文链接**: [https://support.mozilla.org/en-US/kb/future-of-pocket](https://support.mozilla.org/en-US/kb/future-of-pocket)

Mozilla将于2025年7月8日关闭Pocket服务。此日期之后，Pocket将进入仅导出模式，直至2025年10月8日，届时所有用户数据将被永久删除。用户可以在此之前导出他们保存的文章（包括列表、存档、收藏夹、笔记和高亮）。

此决定源于不断演变的网页使用情况，Mozilla将资源集中于其他项目。尽管Pocket即将关闭，Mozilla强调了其连接数百万用户与高质量内容的遗产，并将继续通过诸如新标签页体验和更名为“Ten Tabs”的电子邮件新闻通讯（原Pocket Hits）等举措，投资于内容策划。

Pocket Premium的月度订阅将立即停止续订，用户可以免费访问直至订阅周期结束。年度订阅者将在2025年7月8日自动收到按比例退款。

Pocket网页扩展将于2025年5月22日从应用商店中移除，并将用户重定向到导出页面。该扩展将保留在浏览器中，需要手动移除。该应用程序将从2025年5月22日起无法进行新安装，但现有用户可以在2025年10月8日之前重新安装。

第三方应用程序对Pocket API的访问权限将于2025年10月8日起禁用。

关键日期：

*   **2025年5月22日：** Pocket从应用商店移除，月度续订禁用，停止新用户注册
*   **2025年7月8日：** Pocket关闭，年度退款处理，开始仅导出模式
*   **2025年10月8日：** 最终数据导出日期，所有数据删除。

---

## 6. Showh HN: SQLite JavaScript - 使用 JavaScript 扩展你的数据库

**原文标题**: Showh HN: SQLite JavaScript - extend your database with JavaScript

**原文链接**: [https://github.com/sqliteai/sqlite-js](https://github.com/sqliteai/sqlite-js)

SQLite-JS 是一个强大的扩展，允许开发者使用 JavaScript 代码扩展 SQLite 数据库。它支持直接在 SQLite 中创建自定义标量函数、聚合函数、窗口函数和排序规则。

安装过程包括下载适用于各种平台（Linux、macOS、Windows、Android、iOS）的预构建二进制文件，并使用 SQLite CLI 或 SQL 加载扩展。 该扩展提供了诸如 `js_create_scalar`、`js_create_aggregate`、`js_create_window` 和 `js_create_collation` 等函数，用于使用 JavaScript 定义自定义逻辑。 标量函数处理单个行，聚合函数处理多行以生成单个结果，窗口函数在不折叠行的情况下对一组行进行操作，排序规则定义自定义排序顺序。

该扩展还允许使用 `js_eval` 在 SQLite 查询中直接进行 JavaScript 评估。 与 sqlite-sync 一起使用时，用户定义的函数会自动在设备之间复制。

示例说明了如何使用 SQLite-JS 执行诸如从电子邮件中提取域名、计算标准差以及实现用于百分位数排名的自定义窗口函数等任务。 请注意，由于 SQLite 的限制，更新函数需要单独的数据库连接。 该项目可以使用提供的 Makefile 从源代码构建，并根据 MIT 许可证获得许可。

---

## 7. 韩国酱油大师谈完美酱油之道

**原文标题**: A South Korean grand master on the art of the perfect soy sauce

**原文链接**: [https://www.theguardian.com/world/2025/may/21/without-time-there-is-no-flavour-a-south-korean-grand-master-on-the-art-of-the-perfect-soy-sauce](https://www.theguardian.com/world/2025/may/21/without-time-there-is-no-flavour-a-south-korean-grand-master-on-the-art-of-the-perfect-soy-sauce)

奇顺道是韩国唯一的传统酱油（진장，jinjang）大师，这个称号认可了她致力于保护家族传承370年的发酵技术。她监管着1200个陶罐，在其中，大豆、水、盐、呵护和时间转化为酱油（간장，ganjang）、大酱（된장，doenjang）和辣椒酱（고추장，gochujang），这些都是韩国料理的基石。她的工艺浸润在传统中，包括净化仪式、特定的天气条件，以及使用竹盐等原料。她还使用潭阳草莓制作草莓辣椒酱，以获得天然甜味。

她对这项事业的奉献为她赢得了国际赞誉，她的陈年“母酱”曾被用来调味招待唐纳德·特朗普的烤牛排。奇顺道相信发酵食品的健康益处，并创办了一所发酵学校来分享她的知识。

这篇文章强调了她面临的挑战，包括家庭酱料制作的衰落以及气候变化对发酵过程的影响，迫使她调整自己的方法。尽管面临这些挑战，奇顺道仍然致力于保护这项文化遗产，特别是自酱料制作被联合国教科文组织认可为人类非物质文化遗产以来，这强调了它超越单纯食品生产的重要性。她将自己的工作视为维护这一传统以传承给后代的使命。

---

## 8. 基于模型上下文协议的符号代数探险

**原文标题**: Adventures in Symbolic Algebra with Model Context Protocol

**原文链接**: [https://www.stephendiehl.com/posts/computer_algebra_mcp/](https://www.stephendiehl.com/posts/computer_algebra_mcp/)

本文详细介绍了作者实验Anthropic的Model Context Protocol (MCP)的经验。MCP是一种允许语言模型(LLMs)与外部工具交互的系统。作者专注于使用MCP使像Claude这样的LLMs能够执行复杂的符号代数运算，这是一项由于计算限制，它们通常难以完成的任务。

作者构建了一个sympy-mcp服务器，利用像SymPy这样的计算机代数系统来处理数学运算，而LLM则处理自然语言理解和编排。该服务器通过MCP暴露数学工具，使Claude能够准确地解决诸如整数分解或求解微分方程等问题。

本文强调了将LLMs与专用工具相结合的好处：LLMs处理界面，而工具提供精确的结果。阻尼谐振子求解的例子证明了这种方法。

然而，作者也强调了MCP生态系统早期“狂野西部”的性质，指出文档不完善、黑客松质量的实现以及调试挑战。由于MCP服务器在本地运行，可能允许LLMs调用任意代码，因此提出了一个重大的安全问题。作者建议谨慎，并鼓励读者由于缺乏安全措施，在安装MCP服务器之前审查源代码。

---

## 9. Show HN: DockFlow – 瞬间切换多个macOS Dock布局

**原文标题**: Show HN: DockFlow – Switch between multiple macOS Dock layouts instantly

**原文链接**: [https://dockflow.appitstudio.com/](https://dockflow.appitstudio.com/)

DockFlow 是一款 macOS 应用程序，旨在通过允许用户即时切换多个自定义的 Dock 布局来提高生产力。 这消除了在编码、设计或写作等任务之间切换时手动重新排列 Dock 的需要。

该应用程序设计简洁，设置快捷：用户按需排列 Dock，在 DockFlow 中为配置命名并保存。 然后只需单击一下或使用自定义热键即可在这些已保存的布局之间切换。

除了应用程序之外，DockFlow 还允许用户将文件夹、文件和网站链接添加到 Dock 布局中，从而进一步自定义工作区。 用户还可以插入空白区域进行视觉分组，并使用快捷指令或 CLI 进行更高级的自动化。

DockFlow 以一次性购买方式提供终身访问权限，无需订阅费，目前以折扣价出售。 用户评价强调了它在简化工作流程和提高专注力方面的有效性。 该应用程序通过提供动态且适应性强的 Dock 体验，解决了开发人员和其他同时处理多个角色和项目的专业人士的常见痛点。

---

## 10. 星落

**原文标题**: Planetfall

**原文链接**: [https://somethingaboutmaps.wordpress.com/2025/05/20/planetfall/](https://somethingaboutmaps.wordpress.com/2025/05/20/planetfall/)

丹尼尔·霍夫曼详细介绍了其精心制作喀戎星（1999年电脑游戏《席德·梅尔之半人马座阿尔法星》中的虚构星球）详细地图的流程。受自身对游戏的热爱驱动，他试图利用游戏中提供的海拔、降雨量、岩石密度和异种真菌分布等数据，扩展游戏最初的128x64像素地图。

最耗时的任务是手动转录游戏地图中8192个像素的海拔值，这一过程历时数年。降雨量和岩石密度数据则通过截图和GIS软件提取。

一个关键挑战是将这种低分辨率数据转换为更详细的地形图。霍夫曼描述了他迭代的过程，包括随机散布点、进行三角剖分、平均海拔值以及添加随机噪声，以创建更具自然感的数字高程模型（DEM）。他通过使用圆柱等面积投影，特别是Trystan Edwards投影，来解决投影问题，以匹配游戏地图的属性。

为了纠正与原始游戏地图的差异，例如确保岛屿的准确位置和重塑花环环形山，付出了巨大的努力。霍夫曼还为两极生成了单独的、更高分辨率的DEM，以解决投影变形问题。最后，他混合并平滑了各种DEM，以达到他想要的效果。作者强调了他的工作如何展示真实世界制图与虚构世界制图之间的差异。

---

## 11. 双子座扩散

**原文标题**: Gemini Diffusion

**原文链接**: [https://simonwillison.net/2025/May/21/gemini-diffusion/](https://simonwillison.net/2025/May/21/gemini-diffusion/)

谷歌Gemini Diffusion：一种新的语言模型，它使用扩散而非自回归来生成文本，优先考虑速度。它通过逐步优化噪声来解决传统自回归模型缓慢的顺序处理问题，从而实现快速迭代和纠错。

作者测试了Gemini Diffusion，对其速度印象深刻。在提示构建模拟聊天应用程序时，它达到了857 tokens/秒，并在几秒钟内生成了功能性的HTML+JavaScript代码。这一性能与使用Llama3.1-70b的Cerebras Coder类似。谷歌声称它提供了Gemini 2.0 Flash-Lite的性能，但速度提高了5倍。

虽然缺乏独立的基准测试，但文章澄清说，扩散是用来代替自回归，而不是transformers。扩散LLM利用transformers，但没有因果掩码，允许同时处理整个输入。文章解释说，扩散LMs在概念上更接近BERT，涉及迭代掩码和预测tokens来生成文本。该模型经过训练，可以恢复具有不同百分比掩码tokens的文本。生成从所有掩码tokens开始，通过逐步取消掩码tokens，在多次迭代中完善文本。

---

## 12. 我为什么自制音频播放器

**原文标题**: Why I Built My Own Audio Player

**原文链接**: [https://nexo.sh/posts/why-i-built-a-native-mp3-player-in-swiftui/](https://nexo.sh/posts/why-i-built-a-native-mp3-player-in-swiftui/)

2025年，作者因不满苹果对iPhone播放个人音乐的限制和付费墙，从头开始构建了一个自定义音频播放器。苹果的内置选项功能不足，第三方应用程序通常依赖订阅。作者最初尝试了熟悉的React Native，但遇到了访问iOS文件系统、iCloud以及遵守沙盒的障碍，这导致转而使用Swift和SwiftUI，以便更好地控制原生API并获得更简洁的UI。

最终的应用程序具有灵活的全文搜索、iCloud文件夹导入、全面的音乐管理（播放列表、队列）以及熟悉的界面。应用程序架构是分层的，类似于后端服务器，利用带有FTS5的SQLite进行本地优先的数据存储和模糊搜索。SQLite的全文搜索可以轻松地查询文件名和诸如艺术家、专辑和标题等元数据。

该应用程序有三个主要屏幕：库导入、库管理以及播放器和播放。一个关键的挑战是管理iOS文件访问，其中安全范围书签的可靠性有限。解决方案是将文件复制到应用程序的沙盒中。作者还使用了Apple的AVFoundation框架来解析元数据。文章最后反思了Xcode的局限性，Swift和SwiftUI的优点（特别是async/await和SwiftUI的声明式特性）。作者批评了苹果生态系统对开发者的锁定。

---

## 13. 我们称之为分贝的科学“单位”

**原文标题**: The scientific “unit” we call the decibel

**原文链接**: [https://lcamtuf.substack.com/p/decibels-are-ridiculous](https://lcamtuf.substack.com/p/decibels-are-ridiculous)

无法访问文章链接。

---

## 14. Show HN: Whenish - iMessage群组活动计划

**原文标题**: Show HN: Whenish – Plan Group Events in iMessages

**原文链接**: [https://apps.apple.com/us/app/whenish/id6745035749](https://apps.apple.com/us/app/whenish/id6745035749)

Whenish：一款便捷的 iMessage 群聊活动计划应用。它无需离开“信息”应用，即可让用户创建日期投票、分享空闲时间并查看群成员的实时回复，从而简化群聊中的活动安排，告别繁琐的来回沟通。

主要功能包括快速创建日期投票、选择多个日期以表明空闲时间、实时更新回复以及用户友好的日历界面。非常适合计划团体聚餐、旅行、家庭活动和工作会议。

使用方法：在“信息”应用中打开群聊，点击 Whenish 图标，选择空闲日期，发送投票并监控回复。该应用免费、体积小巧（990.2 KB），需要 iOS/iPadOS 17.6 或更高版本，并基于 4 条评论获得了 5 星评级。开发者 CommonGroundTech, LLC 强调该应用不会收集任何用户数据。

---

## 15. 社交媒体平台：问题何在，路在何方

**原文标题**: Social media platforms: what's wrong, and what's next

**原文链接**: [https://www.scottgoci.com/social-media-platforms-whats-wrong-and-whats-next/](https://www.scottgoci.com/social-media-platforms-whats-wrong-and-whats-next/)

本文介绍一个系列，探讨当前社交媒体平台的问题以及2025年新平台的潜在解决方案。作者认为，现有社交媒体平台的激励机制对用户不利，将日活跃用户、互动、用户生成内容、覆盖范围和货币化等指标置于真正的社交关系之上。

作者强调了具体问题：平台对虚假账户、标题党内容、机器人生成或盗窃的内容以及数据隐私问题视而不见，这些都源于对增长和利润的追求。这些优先事项导致用户被广告和操纵性内容轰炸，而不是培养有意义的互动。

文章以TikTok的商店功能为例，说明了平台将货币化置于用户体验之上。

作者认为需要一种新的方法，首先要批判性地审视当前社交媒体各个方面存在的问题。接下来的文章将更深入地探讨与平台本身、社区、内容、用户和版主相关的问题。目标是“重新学习”当前的社交媒体真理，并探索构建更高效、以用户为中心的社交平台的解决方案。作者欢迎反馈，并期待对其想法的审视。

---

## 16. 基准犯罪符合形式验证

**原文标题**: Benchmarking Crimes Meet Formal Verification

**原文链接**: [https://microkerneldude.org/2025/04/27/benchmarking-crimes-meet-formal-verification/](https://microkerneldude.org/2025/04/27/benchmarking-crimes-meet-formal-verification/)

本文批判了使用“证明代码比”作为衡量形式化验证操作系统效率的指标。作者认为这是一种“基准测试犯罪”，因为它在不考虑被验证规范的完整性和复杂性的情况下毫无意义。

作者用一个`sort()`函数的例子说明了这一点，展示了如何提高规范的完整性（例如，要求输出包含与输入相同数量的每个元素）会在不改变代码本身的情况下，极大地增加证明的复杂性和大小。

本文提供了一个更全面的表格，包括代码、规范和证明的大小，突出了规范大小的重要性。它引用研究表明规范大小和证明大小之间存在二次关系。

作者认为，比较证明代码比意味着一种线性关系，这是不成立的。相反，重点应该放在规范大小上，并理解规范复杂性和证明工作量之间的非线性关系。

文章讨论了模块化作为减少验证工作量的一种策略，但认为由于 seL4 等系统的高度互连性，它不容易应用于这些系统。

最终，作者得出结论，证明代码比具有误导性，自动化定理证明（ATP）方法比交互式定理证明（ITP）需要更少的证明工作量，并且每个类别（ITP 和 ATP）内的相对效率各不相同，其中 seL4 在 ITP 类别中表现良好。作者敦促业界放弃这种科学上不健全的做法。

---

## 17. 南极冰盗

**原文标题**: Ice Theft in Antarctica

**原文链接**: [https://nautil.us/ice-theft-in-antarctica-1210083/](https://nautil.us/ice-theft-in-antarctica-1210083/)

南极洲的冰盗：冰川间的冰块争夺战

鲍勃·格兰特的这篇《鹦鹉螺》文章《南极洲的冰盗》讨论了最近观测到的南极洲冰川间“冰块盗窃”现象。研究人员利用卫星数据发现，冰川正以过去认为需要几个世纪甚至几千年才能发生的速度，从其邻居那里窃取冰块。

利兹大学的科学家在《冰冻圈》杂志上发表的这项研究，特别强调了科勒东冰川和科勒西冰川之间的相互作用。 在2005年至2022年期间，移动速度更快的科勒东冰川一直在窃取其移动速度较慢的邻居科勒西冰川的冰流。 这种冰块盗窃导致科勒西冰川在此期间减速了10%，因为它不像移动更快的邻居那样变薄和拉伸。

了解这些不寻常的冰流动力学对于预测未来冰川的行为及其对海平面上升的影响至关重要，因为随着气候变暖，冰川将继续向大海流动，并可能携带被盗的冰块。

---

## 18. 无需炒作或虚言解释MCP

**原文标题**: MCP explained without hype or fluff

**原文链接**: [https://blog.nilenso.com/blog/2025/05/12/mcp-explained-without-hype-or-fluff/](https://blog.nilenso.com/blog/2025/05/12/mcp-explained-without-hype-or-fluff/)

本文介绍了模型上下文协议 (MCP)，将其作为解决人工智能领域 M x N 集成问题的方案，简化了 AI 客户端与各种平台之间的集成。 MCP 引入了 MCP 服务器，该服务器连接到数据源并公开平台特定的工具、提示和资源。 AI 应用程序随后可以使用 MCP 客户端连接到这些服务器。

作者通过一个实际的例子来说明这一点：构建一个用于 CKAN 的 MCP 服务器，CKAN 是一个开放数据管理系统。 这使得 AI 应用程序（如 Claude）能够访问和分析来自 CKAN 实例（如 JusticeHub）的数据，而无需专门为 CKAN API 进行编码。 这开启了更广泛地使用开放数据和更高级的 AI 驱动分析的潜力。

虽然 MCP 提供了诸如降低集成摩擦和解耦等优势，但作者强调它不是构建优秀 AI 产品的万能药。 应该考虑 MCP 所需的脚手架、LLM 性能对提示的敏感性以及潜在的延迟问题。 MCP 最适合与外部平台（例如 GitHub）集成，在这些平台中解耦是有价值的。 对于可以严格控制客户端和服务器的内部工具，直接优化可能是一种更好的方法。

最终，MCP 被认为是一个有价值的工具，特别是在促进人工智能领域的互操作性方面，但它不能取代扎实的软件工程实践。 作者鼓励大家探索所提供的资源以进行进一步学习。

---

## 19. 四年视奏练习

**原文标题**: Four years of sight reading practice

**原文链接**: [https://sandrock.co.za/carl/2025/05/four-years-of-sight-reading-pracice/](https://sandrock.co.za/carl/2025/05/four-years-of-sight-reading-pracice/)

本文详细介绍了作者使用iPad应用程序（“NoteVision”）和一个MIDI键盘进行钢琴视奏练习的四年历程。作者虽有吉他背景，但对钢琴技巧的不足感到沮丧，于是开始坚持有规律的自动化练习。

该设置包括通过蓝牙连接的MIDI键盘，NoteVision应用程序，以及一个自定义的Pythonista脚本，该脚本可以随机生成调号，并在MySQL数据库中跟踪绩效指标。D3.js仪表板可视化了练习进度，揭示了专注于特定调性，然后采用更随机方法的各个阶段。

主要经验包括，无需有意识地命名音符，直接进行手指到音符的映射是可能的，因此需要使用Anki采取单独的方法来学习调号。 尽管经过多年的练习，作者仍在不断进步。 他们认识到键盘音域的局限性，并强调了随机练习在避免偏见和识别弱点方面的价值。 作者现在优先练习经验较少或准确率较低的调性。

作者的完整练习包括视奏，音阶/琶音，乐理练习，记谱/转录，听音训练和曲目练习，但承认很难跟上所有这些练习。

---

## 20. Show HN：Three.js 中的弯曲空间着色器 (通过 4D 球体投影)

**原文标题**: Show HN: Curved Space Shader in Three.js (via 4D sphere projection)

**原文链接**: [https://github.com/bntre/CurvedSpaceShader](https://github.com/bntre/CurvedSpaceShader)

此“Show HN”帖子介绍了一个用 Three.js 实现的曲面空间着色器，它改编自 Unity 游戏 Sfera 中使用的 HLSL 着色器。该着色器通过将 3D 模型投影到 4D 单位球上，应用 4D 旋转，然后使用立体投影将其投影回 3D，从而创造出曲面空间的错觉。这个过程扭曲了 3D 模型，模拟了曲面空间环境。

该帖子提供了一个实时演示链接和一个展示效果的视频。它还解释了着色器背后的数学概念，概述了缩放、定位和投影步骤。

该实现提供了交互式控件，供用户操纵场景。这些控件允许缩放、在各种 4D 平面（包括“内外翻转”和旋转）中旋转对象、缩放对象以及使用鼠标和键盘移动相机。该帖子还承认使用了来自 three.js 示例的预先存在的动画模型和 Kevin MacLeod 的音乐。它澄清了模型是在运行时从 Three.js 存储库加载的，而不是直接包含在给定的存储库中。

---

## 21. 上转换隐形眼镜实现近红外时空彩色视觉

**原文标题**: Near-infrared spatiotemporal color vision enabled by upconversion contact lenses

**原文链接**: [https://www.cell.com/cell/fulltext/S0092-8674(25)00454-4](https://www.cell.com/cell/fulltext/S0092-8674(25)00454-4)

无法访问文章链接。

---

## 22. 炳哲韩的哲学（2020）

**原文标题**: The Philosophy of Byung-Chul Han (2020)

**原文链接**: [https://newintrigue.com/2020/06/29/the-philosophy-of-byung-chul-han/](https://newintrigue.com/2020/06/29/the-philosophy-of-byung-chul-han/)

本文介绍了韩炳哲的哲学思想。韩炳哲是一位出生于韩国的德国哲学家，他被认为是尼尔·波兹曼和马歇尔·麦克卢汉等挑战围绕技术而产生的社会规范的思想家的当代继承者。韩炳哲的哲学以通俗易懂的短篇著作呈现，批判了现代“成就社会”，在这种社会中，成功的压力和自我满足导致了孤立、精神疾病和疏离。

韩炳哲认为，我们已经从“服从主体”的“规训社会”过渡到“成就主体”或“自我创业者”的“成就社会”，而驱动这种转变的动力是“能”而非“应”。这导致了自我剥削和倦怠，因为个人不断努力通过持续的成就来“成为自己”。

他还探讨了由自恋和“他者”丧失所引发的爱情危机、消除了消极性和内省的“平滑”美学（以杰夫·昆斯的作品为例）的兴起，以及“透明社会”的危险，在这种社会中，我们通过社交媒体自愿屈服于全景凝视，成为囚徒和施害者。

本文还涉及韩炳哲的“好的娱乐”的概念，他认为我们已经将工作和娱乐混为一谈，将激情和生产置于真正的享受之上。他提倡为了娱乐本身而拥抱玩耍，使其独立于商品化。最终，韩炳哲鼓励读者拒绝追求完美，拥抱源于消极性、不完美以及与他人和世界的联系的真实性，摆脱社会指令和不断追求成就的驱动。

---

## 23. 一切皆是缺陷 (或问题)

**原文标题**: Everything’s a bug (or an issue)

**原文链接**: [https://www.bozemanpass.com/everythings-a-bug-or-an-issue/](https://www.bozemanpass.com/everythings-a-bug-or-an-issue/)

戴维·博勒姆的文章《一切皆为缺陷（或问题）》提倡以缺陷为中心的软件项目管理方法，借鉴了他早期使用名为BugSplat的内部系统的经验。他认为，将每个任务都视为一个缺陷，从新功能到文档，可以提供一个统一的项目规划框架。

这种方法的有效性取决于四个关键原则：1) 将所有任务视为系统内的缺陷；2) 使用一致的、带有主观色彩的缺陷记录模式来捕获详细信息；3) 每次只将每个缺陷的责任分配给一个人；4) 启用强大而灵活的查询，以创建为个人需求量身定制的自定义缺陷列表。

该文章将这种历史方法与如今由GitHub及其问题功能主导的现代格局进行了对比。尽管GitHub Issues在源代码控制方面很方便，但由于其功能匮乏，它在上述四个原则上有所欠缺。由于缺乏一致的模式、单一受让人强制执行和灵活的查询，GitHub Issues通常会导致采用补充性的项目规划工具，从而破坏了统一的、以缺陷为中心的系统。

博勒姆建议，尽管像GitLab和Bitbucket这样的替代方案在问题管理方面有所改进，但它们仍然不能完全满足这四个原则。他建议通过添加缺失的功能来增强像Gitea这样的优秀开源项目。文章重点介绍了一个具体的例子，即向Gitea的问题列表添加优先级排序。作者最后表示，他致力于添加剩余的功能，以在Gitea中完全实现软件开发的“缺陷委员会方式”。

---

## 24. 伊尼戈·奎莱斯：计算机图形学、数学、着色器、分形、演示场景

**原文标题**: Inigo Quilez: computer graphics, mathematics, shaders, fractals, demoscene

**原文链接**: [https://iquilezles.org/articles/](https://iquilezles.org/articles/)

Inigo Quilez的网站是计算机图形学、数学、着色器、分形和演示场景技术的综合资源。它提供了涵盖广泛主题的文字教程（着陆页上提供视频教程），所有教程均采用MIT许可，便于重复使用。

该网站组织成几个关键领域：有向距离函数 (SDF) 和光线步进，涵盖 2D 和 3D SDF、光线与表面相交、平滑最小值、域重复、阴影、法线和各种几何形状。它还包括关于纹理和过滤的部分，讨论了双平面贴图、纹理重复、程序纹理过滤和改进的插值方法等技术。

网站还探讨了光照技术，包括室外光照、雾、环境光遮蔽和全局光照。渲染器/引擎部分涵盖了 GPU 条件语句、三角函数优化、计时、视锥剔除、立体渲染和基本 VR 等主题。网站还解释了有用的数学概念及其应用，例如逆运动学、环境光遮蔽、形状密度/可见性/投影、贝塞尔曲线、椭圆、多边形法线和傅里叶级数。

分形和复杂动力学也受到了极大的关注，涵盖了曼德勃罗集、朱利亚集、各种轨道陷阱技术、菩提勃罗分形等等。最后，该网站还包含关于演示场景技术的文章，例如在 4kb 中制作程序图形、网格压缩、尺寸编码、最小样条代码和紧凑型浮点存储。

---

## 25. 美国情报机构——购买你个人数据的一站式商店

**原文标题**: U.S. Spy Agencies–One-Stop Shop to Buy Your Personal Data

**原文链接**: [https://theintercept.com/2025/05/22/intel-agencies-buying-data-portal-privacy/](https://theintercept.com/2025/05/22/intel-agencies-buying-data-portal-privacy/)

拦截者报导揭露美国情报界绕过第四修正案，计划建立集中式“一站式”平台购买美国人商业可用信息（CAI）。这个名为“情报界数据联盟”（ICDC）的门户网站icdata.gov旨在为情报界的18个机构简化敏感数据（如位置信息、房地产记录和社交媒体内容）的获取。

国家情报总监办公室（ODNI）声称ICDC将消除重复购买，提高成本效益，同时纳入“公民自由和隐私最佳实践”。然而，布伦南中心Emile Ayoub等批评人士认为，它使各机构能够廉价购买大量敏感数据，规避宪法保护。

文章强调了使用人工智能工具分析这些数据的担忧，这可能导致个人的重新识别和歧视性情感分析的延续。虽然ODNI发布了CAI使用规则，但批评人士认为这些规则为情报界提供了过多的自由，并依赖私人供应商来确定数据的敏感性。国土安全部（DHS）等非情报机构也可以访问ICDC门户，这可能会针对非公民。参议员Ron Wyden表达了对特朗普政府可能如何使用商业数据以及该项目缺乏透明度的担忧。

---

## 26. 自由线程Python库兼容性检查器

**原文标题**: Free-Threaded Python Library Compatibility Checker

**原文链接**: [https://ft-checker.com/](https://ft-checker.com/)

本文档介绍了一个用于检查 Python 库在自由线程 Python 环境下与 CPython 3.13t 和 3.14t 版本兼容性的工具。它以热图形式显示各种库的安装状态，表明安装成功、失败或无数据。提供的数据显示了 Python 3.13t 的兼容性结果，包括库列表、版本、构建结果、错误详情（如有）和最后更新时间戳。

`boto3`、`charset-normalizer`、`urllib3`、`requests`、`botocore`、`typing-extensions`、`idna`、`setuptools`、`s3transfer`、`certifi`、`packaging`、`python-dateutil`、`six`、`numpy` 和 `importlib-metadata` 等几个常见库在 Python 3.13t 上报告为“成功”。但是，`aiobotocore`、`cryptography`、`s3fs` 和 `grpcio-status` 构建失败。

`aiobotocore` 和 `s3fs` 的错误详情表明 `aiohttp._websocket.mask` 扩展存在编译问题，源于未知的类型名称 `__pyx_vectorcallfunc` 和已弃用的 `Py_OptimizeFlag`。 `cryptography` 的失败是由于所需的 Rust 版本（1.65.0）比当前激活的版本（1.63.0）更新。 `grpcio-status` 的错误详情表明在编译阶段由于 `DistutilsExecError` 而失败，具体而言，C++ 编译器退出的代码为 1。

---

## 27. 扩散语言模型的优势与局限性

**原文标题**: Strengths and limitations of diffusion language models

**原文链接**: [https://www.seangoedecke.com/limitations-of-text-diffusion-models/](https://www.seangoedecke.com/limitations-of-text-diffusion-models/)

扩散模型与自回归模型的比较：速度、上下文处理与推理能力

---

## 28. 将任何CSV文件显示为可搜索、可过滤的美观HTML表格

**原文标题**: Display any CSV file as a searchable, filterable, pretty HTML table

**原文链接**: [https://github.com/derekeder/csv-to-html-table](https://github.com/derekeder/csv-to-html-table)

本文档介绍“CSV to HTML Table”，这是一个基于 JavaScript 的工具，用于将 CSV 文件显示为可搜索、可过滤的 HTML 表格。它是一个 100% 的客户端解决方案，意味着无需服务器端处理。

**用法:**

1. 克隆仓库。
2. 将 CSV 文件放置在 `data/` 文件夹中。
3. 在 `index.html` 中使用选项配置 `CsvToHtmlTable.init()`，例如：
    * `csv_path`: CSV 文件的路径。
    * `element`: HTML 元素 ID，表格将在此呈现。
    * `allow_download`: 启用 CSV 下载链接。
    * `csv_options`: jQuery CSV 解析器的配置（例如，自定义分隔符）。
    * `datatables_options`: DataTables 插件的配置（例如，分页）。
    * `custom_formatting`: 用于格式化列数据的列索引和函数数组。

该文档提供了创建超链接的自定义格式化函数示例，并警告需要对 HTML 输出进行消毒以防止 XSS 漏洞。

**运行和部署:**

* 在本地使用 Python 的 `SimpleHTTPServer` 或 `http.server`。
* 通过推送到 `gh-pages` 分支部署到 GitHub Pages。
* 将项目文件上传到任何 Web 服务器。

生成的表格可以使用 `iframe` 嵌入到其他网站中。

**依赖项:**

* Bootstrap 4
* jQuery
* jQuery CSV
* DataTables

该文档包括故障排除提示，特别建议用户使用浏览器开发者控制台来识别 JavaScript 错误。 它鼓励用户报告错误，并欢迎通过 pull request 提交贡献。 该项目在 MIT 许可证下发布。

---

## 29. 我们如何提高OCR代码的准确性

**原文标题**: How we made our OCR code more accurate

**原文链接**: [https://pieces.app/blog/how-we-made-our-optical-character-recognition-ocr-code-more-accurate](https://pieces.app/blog/how-we-made-our-optical-character-recognition-ocr-code-more-accurate)

Pieces 如何改进其 OCR 引擎以实现代码图像转录

---

## 30. 算法而言，少量内存胜过大量时间。

**原文标题**: For algorithms, a little memory outweighs a lot of time

**原文链接**: [https://www.quantamagazine.org/for-algorithms-a-little-memory-outweighs-a-lot-of-time-20250521/](https://www.quantamagazine.org/for-algorithms-a-little-memory-outweighs-a-lot-of-time-20250521/)

本文详细介绍了瑞安·威廉姆斯突破性的证明，该证明表明少量内存在所有可想见的计算中与大量时间具有同等效力，标志着计算机科学领域一个 50 年难题取得了重大进展。这一结果挑战了长期以来认为空间（内存）和时间在算法需求上大致成比例的假设。

威廉姆斯的证明确立了一种将任何算法转化为更节省空间形式的方法。更重要的是，这一结果意味着一个先前无法证明的结论：某些计算在特定时间范围内是绝对不可能的。这个证明被其他计算机科学家认为是“令人震惊的”和“巨大的进步”。

本文通过强调 Juris Hartmanis 和 Richard Stearns 的奠基性工作来提供背景，他们在 20 世纪 60 年代开发了时间和空间复杂度的数学定义，为定义诸如“P”（可以在合理时间内解决的问题）和“PSPACE”（空间类似类）等复杂度类铺平了道路。它还讨论了 John Hopcroft、Wolfgang Paul 和 Leslie Valiant 早期的努力，他们创建了一种节省少量空间的通用模拟，但由于假设不同的数据块不能同时占用相同的内存空间，进展停滞不前。

本文还叙述了威廉姆斯的旅程，他对计算机的早期迷恋，以及他克服挑战坚持追求复杂性理论的决心。他的坚持最终促成了这一突破，巩固了他作为该领域领军人物的地位。

---

## 31. 热点：用于性能分析的Linux `perf` GUI

**原文标题**: Hotspot: Linux `perf` GUI for performance analysis

**原文链接**: [https://github.com/KDAB/hotspot](https://github.com/KDAB/hotspot)

Hotspot：Linux `perf` 数据分析独立GUI工具，旨在提供类似 KCachegrind 的体验。它可以可视化 `perf.data` 文件，突出显示内联函数并允许基于时间的过滤。它还可以启动 `perf` 来分析应用程序。

Hotspot 可通过软件包管理器（Arch、Debian/Ubuntu、Gentoo、Fedora）在各种 Linux 发行版上获得，或者作为通用 AppImage 提供。贡献者或需要最新版本的人员可以从源代码构建。

主要功能包括使用内核跟踪点的 off-CPU 分析，有助于等待时间分析。它还支持通过指定 sysroot 和 kallsyms 来分析来自嵌入式系统的数据。该工具允许将捕获的数据导出到自包含的 `.perfparser` 文件中，以便轻松共享。包含一个反汇编器，用于显示每个指令的成本。

已知问题包括由于缺少 ELF 文件或调试信息而导致的断裂的回溯。解决方案包括使用命令行参数来指定路径、安装调试包或升级 elfutils。Hotspot 支持 debuginfod。与 `perf report` 相比，存在缺少的功能，并且录制可能需要调整权限。导出文件格式目前受到限制。Hotspot 使用 Qt Creator 的 `perfparser` 实用程序，并根据 GPL v2+ 获得许可。

---

## 32. Kotlin-Lsp：Kotlin语言服务器及Visual Studio Code插件

**原文标题**: Kotlin-Lsp: Kotlin Language Server and Plugin for Visual Studio Code

**原文链接**: [https://github.com/Kotlin/kotlin-lsp](https://github.com/Kotlin/kotlin-lsp)

Kotlin-Lsp 项目通过基于 IntelliJ IDEA 的语言服务器协议实现，为 Visual Studio Code 提供预 Alpha 版本的 Kotlin 语言支持。它旨在为 Kotlin 提供无缝的开发者体验，尤其是在 Java 互操作性方面。

**要点：**

*   **功能：** 开箱即用地支持仅 JVM 的 Kotlin Gradle 项目，提供诸如语义高亮、导航（Kotlin & Java）、快速修复、检查、重构（重命名、移动等）、即时诊断和代码补全等功能。路线图详细说明了计划对 Gradle KMP、Maven/Amper、构建系统无关导入等功能的支持。
*   **安装：** 下载 VSC 扩展，并从 VSIX 文件安装。需要 Java 17 或更高版本。
*   **项目状态：** 实验性，预 Alpha 阶段。由于不稳定，不适用于日常工作。优先考虑快速开发和功能探索。
*   **平台：** 主要在 macOS 和 Linux 上使用 Visual Studio Code 进行测试。可通过手动配置与其他符合 LSP 规范的编辑器一起使用。需要基于拉取的诊断。
*   **源代码：** 目前部分闭源以提高开发速度，利用 IntelliJ、Fleet 和 Bazel 构建基础设施。计划在初始稳定阶段后开源 LSP 实现。VSC 扩展是开源的。
*   **反馈：** Bug 报告和功能请求应以 GitHub issue 的形式提交。目前直接的代码贡献受到限制，但欢迎提交文档 PR。

---

## 33. 微软支持的Builder.ai因发现潜在的虚假销售而倒闭。

**原文标题**: Microsoft-backed Builder.ai collapsed after finding potentially bogus sales

**原文链接**: [https://www.ft.com/content/926f4969-fda7-4e78-b106-4888c8704bda](https://www.ft.com/content/926f4969-fda7-4e78-b106-4888c8704bda)

据报道，微软支持的Builder.ai公司因发现潜在的欺诈性销售而倒闭。《金融时报》(FT)文章指出，如需了解完整详情，需要订阅。该文章推广了多种订阅选项，从“标准数字版”每月45美元到“印刷+高级数字版”每月79美元不等，提供不同级别的FT新闻访问权限，包括全球新闻、专家观点、新闻通讯和报纸的数字版。

---

## 34. 为数据分析追逐分布式架构的迷失十年？

**原文标题**: A lost decade chasing distributed architectures for data analytics?

**原文链接**: [https://duckdb.org/2025/05/19/the-lost-decade-of-small-data.html](https://duckdb.org/2025/05/19/the-lost-decade-of-small-data.html)

文章质疑，鉴于单节点性能的提升，过去十年对数据分析采用分布式架构的关注是否是必要的。作者使用 TPC-H 基准测试（SF1000，约 265GB 数据库）在 2012 年的 MacBook Pro（配备 16GB 内存和 SSD）与现代 M3 Max MacBook Pro 上对 DuckDB 进行了基准测试。

尽管 2012 年的机器明显较慢（现代机器的几何平均加速比约为 20 倍），但它成功地在合理的时间内（一分钟到半小时之间）运行了所有 22 个基准查询。这表明即使在十年前，像 DuckDB 这样的单节点 SQL 引擎也能够处理大型数据集上的复杂分析查询。

作者认为，转向分布式系统可能为时过早。到 2012-2014 年，高性能单节点解决方案的必要要素（如向量化查询处理和 SSD 存储）已经存在。鉴于许多分析数据集的相对较小，硬件能力的提升表明，关注单节点解决方案可能足以满足许多用例，从而可能避免分布式系统的复杂性和开销。最终，作者得出结论，行业可能在追逐分布式架构上“浪费了整整十年”，而单节点解决方案早已可行。

---

## 35. 罗伯特·穆齐尔被遗忘的戏剧作品启发了他最伟大的小说

**原文标题**: Robert Musil Forgotten Plays Inspired His Greatest Work of Fiction

**原文链接**: [https://lithub.com/the-austrian-writer-whose-forgotten-plays-inspired-his-greatest-work-of-fiction/](https://lithub.com/the-austrian-writer-whose-forgotten-plays-inspired-his-greatest-work-of-fiction/)

Lit Hub精选文章，题为“罗伯特·穆齐尔被遗忘的剧作如何启发了他的小说巨作”。虽然文章本身未收录，但标题表明该文探讨了罗伯特·穆齐尔鲜为人知的戏剧作品与他的代表作，很可能是《没有个性的人》之间的联系。核心观点是，这些剧作尽管被忽视，但在塑造他这部著名小说的主题、思想，甚至可能是叙事结构方面发挥了重要作用。

此外，该摘要提供了Lit Hub上热门内容的快照。文章主题多样，从短篇小说（艾萨克·阿西莫夫的《夜幕降临》）到实验小说、假想情景（“曼哈顿上空的蘑菇云”）以及对创作过程的反思（克雷格·莫德谈行走）不等。此外，还有书评和备受期待的犯罪小说的综述。最后，还收录了几篇作者驱动的文章，探讨新小说背后的创作过程和主题关注。

---

## 36. CERN准备向欧洲各地运送反物质

**原文标题**: CERN gears up to ship antimatter across Europe

**原文链接**: [https://arstechnica.com/science/2025/05/cern-gears-up-to-ship-antimatter-across-europe/](https://arstechnica.com/science/2025/05/cern-gears-up-to-ship-antimatter-across-europe/)

欧洲核子研究中心开发出一种便携式反物质约束装置，用于将反物质运送到干扰较少的实验室，从而能够更精确地测量其特性。目前，欧洲核子研究中心产生的反物质受到减缓其速度的硬件产生的电磁场干扰。这种新型容器是一个两米长的装置，配备超导磁体、真空系统、电池供电和保护性金属框架，可以将反物质运离这种干扰。

为了测试该装置，欧洲核子研究中心成功地用该容器在其园区内运输了质子，行程近4公里。测试保持了容器的低温（约5开尔文），并且表明在运输过程中没有质子损失。确定的主要挑战是运输过程中由于湍流造成的液氦损失，这是限制运输持续时间的关键因素。

最终目标是将反物质运送到德国杜塞尔多夫的一个新设施，距离约800公里。该设施有望实现比目前在欧洲核子研究中心实现的精度高100倍的测量，但这取决于解决液氦供应问题。这种移动反物质约束装置的成功开发和测试标志着反物质研究及其应用向前迈出了重要一步。

---

## 37. 论文被录用

**原文标题**: Getting a paper accepted

**原文链接**: [https://maxwellforbes.com/posts/how-to-get-a-paper-accepted/](https://maxwellforbes.com/posts/how-to-get-a-paper-accepted/)

如何让论文被录用：本文详细介绍了如何通过关注清晰度、影响力和完整性，将一篇被拒稿的研究论文转化为被接受的论文的策略。核心论点是，一篇论文的感知质量很大一部分（约80%）是在第一页确定的，特别是标题、图1、摘要和引言。

作者提倡使用具体且令人难忘的标题，可以加入品牌推广以帮助记忆。图1应该具有视觉吸引力，清晰地展示作品的价值，并且在没有图说的情况下也能被理解，最后以简洁的总结信息结束。摘要应该具体、有价值，并作为一个钩子来吸引读者，避免泛泛而谈和过度声明。引言应该通过提出问题来制造紧张感，然后以提出的解决方案的形式释放，强调作品的价值和独特性。

除了第一页，本文还强调了完整性的重要性，以避免被拒绝。这包括添加基线、消融实验、统计显著性和人工评估。清晰度也至关重要，可以通过改进图表和表格，以及重写结论来实现。作者建议从论文的中间部分删除内容，以为改进腾出空间。他还强调了使图表密集、美观且易于理解的重要性，方法是包括视觉辅助工具和清晰的标签。目标是先发制人地解决潜在的审稿人问题，从而提高被接受的机会。

---

## 38. 直接 TLS 可以加速你的连接。

**原文标题**: Direct TLS can speed up your connections

**原文链接**: [https://marc-bowes.com/postgres-direct-tls.html](https://marc-bowes.com/postgres-direct-tls.html)

本文详细介绍了 Aurora DSQL 开发者在不使用公司 VPN 从 AWS 办公网络连接时遇到的性能问题，导致连接速度缓慢，大约需要 3 秒。

根本原因被确定为 Cisco 公司防火墙使用的 TLS 服务器身份发现功能。该功能旨在检查 TLS 1.2 中的 TLS 证书以强制执行策略，它会打开第二个未经请求的 TLS 连接来以明文形式检索证书。PostgreSQL 的标准 TLS 握手过程期望客户端首先请求 TLS 支持，然后再发起握手。防火墙的额外连接导致了延迟，因为它试图在允许原始连接之前了解证书。

该解决方案利用了 PostgreSQL 17 的“直接 TLS”功能。此功能允许客户端立即发起 TLS 握手，跳过初始的 TLS 支持请求。通过在客户端和服务器上启用直接 TLS，防火墙的辅助连接成功完成握手，从而消除了 3 秒的延迟。

本文强调了直接 TLS 在客户端和服务器均受控且强制使用 TLS 的环境中是有益的，因为它避免了往返延迟，并允许使用 Cisco 防火墙等网络工具。Aurora DSQL 仅支持 TLS，建议使用直接 TLS 以获得最佳性能。本文包括使用 psql 和 pdsql 连接到启用直接 TLS 的 Aurora DSQL 的示例。

---

## 39. ITXPlus：ITX尺寸的Macintosh Plus主板复刻

**原文标题**: ITXPlus: A ITX Sized Macintosh Plus Logicboard Reproduction

**原文链接**: [https://68kmla.org/bb/index.php?threads/itxplus-a-itx-sized-macintosh-plus-logicboard-reproduction.49715/](https://68kmla.org/bb/index.php?threads/itxplus-a-itx-sized-macintosh-plus-logicboard-reproduction.49715/)

Max1zzz正在制作ITXPlus，这是一个Mini-ITX尺寸的Macintosh Plus逻辑板克隆，专为现代机箱设计，并且完全使用新零件构建（除了68000 CPU和连接器）。目标是创建一个完整的开源项目，供爱好者从头开始构建一个可工作的Macintosh Plus系统，而无需依赖原始Macintosh零件。

ITXPlus的主要功能包括：

*   **板载VGA：** 使用GuruThree基于Pico的视频转换器进行显示输出。
*   **ATX电源：** 由标准的24针ATX电源供电。
*   **板载SCSI：** 包含用于存储的50针内部SCSI接头。
*   **4MB内存：** 具有4MB焊接内存。
*   **现代替代品：** 采用DosFox的声音IC替代品、Max1zzz的SCHWIM IWM旁路（基于DosFox的工作）、pgreenland/quortan基于ATTiny的RTC替代品以及Porchy/Hkz/Bolle逆向工程的PAL。
*   **软驱选项：** 虽然基于SCHWIM的IWM旁路本身不支持软驱，但扩展头允许在需要时连接真正的IWM。
*   **表面贴装设计：** 主要采用表面贴装元件，除了68000 CPU，允许使用陶瓷封装版本。

该项目完成后将在GitHub上开源。选择Macintosh Plus是因为它可以完全用新组件复制。

---

## 40. 双子座猜出了我侄子的名字。

**原文标题**: Gemini figured out my nephew’s name

**原文链接**: [https://blog.nawaz.org/posts/2025/May/gemini-figured-out-my-nephews-name/](https://blog.nawaz.org/posts/2025/May/gemini-figured-out-my-nephews-name/)

这篇博文详细介绍了作者如何通过构建的MCP服务器，授予谷歌Gemini LLM对其邮件存档的只读访问权限，从而找到了侄子的名字（“Monty”）。该服务器提供了三个工具：`search`、`get_message_content_by_id`和`get_thread_by_id`。

作者最初的任务是让Gemini制定一个寻找名字的策略，并强调在讨论该策略之前不要使用这些工具。在概述了一个搜索来自Donovan（作者的兄弟）的包含与儿子、婴儿和祝贺相关的关键词的电子邮件的计划后，Gemini执行了这个计划。

LLM进行了一系列搜索，并根据结果改进其查询。它最初遇到了许多涉及Donovan的堂兄弟姐妹孩子的虚假线索。它探索了提及“powertoddler”的电子邮件，并试图识别发送给Donovan的祝贺邮件。

最终，Gemini找到了一封来自Donovan的标题为“Re: Monty”的电子邮件。即使该电子邮件没有明确说明Monty是Donovan的儿子，LLM还是通过分析电子邮件的上下文（讨论了Monty的阅读偏好）推断出了这种联系。作者确认Monty确实是侄子的名字。

作者发现有趣的是，Gemini最终是从最初的、广泛的搜索查询识别出的电子邮件中推导出答案的，即使在尝试了许多更具针对性的搜索之后也是如此。作者强调了通过构建自己的工具来控制访问和功能的重要性，而不是依赖第三方服务器。

---

## 41. 术士(YC S24) 招聘首席硬件设计工程师

**原文标题**: Sorcerer (YC S24) Is Hiring a Lead Hardware Design Engineer

**原文链接**: [https://jobs.ashbyhq.com/sorcerer/6beb70de-9956-49b7-8e28-f48ea39efac6](https://jobs.ashbyhq.com/sorcerer/6beb70de-9956-49b7-8e28-f48ea39efac6)

Sorcerer (YC S24) 招聘首席硬件设计工程师。需启用 Javascript 查看完整职位描述及申请详情。

---

## 42. 微型卫星为地球上任何地方的量子通信铺平道路

**原文标题**: Mini-satellite paves the way for quantum messaging anywhere on Earth

**原文链接**: [https://www.nature.com/articles/d41586-025-00581-7](https://www.nature.com/articles/d41586-025-00581-7)

研究人员在量子通信领域取得重大突破，他们利用一颗微型卫星在中国和南非之间传输了一个秘密加密密钥，距离接近13000公里，打破了纪录。这一进展展示了使用相对廉价且轻巧的技术在全球任何地方建立安全量子消息传递能力的潜力。

文章重点介绍了使用“廉价、轻巧”的微型卫星，表明了一种经济高效的长距离量子通信方法。它还引用了一篇相关的《自然》杂志文章，提供了有关具体研究和方法的更多细节（Li, Y. et al. Nature https://doi.org/10.1038/s41586-025-08739-z (2025)）。

文章还链接到有关量子网络和卫星技术进步的相关文章，突显了量子通信领域的持续进展和关注。相关主题为量子物理学和量子信息。

---

## 43. Rocky Linux 10 将支持 RISC-V

**原文标题**: Rocky Linux 10 Will Support RISC-V

**原文链接**: [https://rockylinux.org/news/rockylinux-support-for-riscv](https://rockylinux.org/news/rockylinux-support-for-riscv)

得益于 Fedora RISC-V 社区和 Rocky 的 AltArch SIG 之间的合作，Rocky Linux 10 将正式支持 RISC-V 架构。该版本将提供 riscv64gc 构建，最初目标平台为 StarFive VisionFive 2 (VF2)、QEMU 和 SiFive HiFive Premier P550 等。

虽然 RISC-V 支持被认为是替代架构，但构建失败不会阻止其他架构的发布，从而确保及时更新。主要硬件支持包括 VisionFive 2（推荐，标准内核支持）、QEMU（非常适合测试）和 SiFive HiFive P550（通过供应商内核提供有限的支持）。其他平台，如 Milk-V 和 Banana Pi，正在考虑之中，随着主线支持的成熟。

这项倡议由社区驱动，利用来自 Fedora RISC-V 的编译器堆栈并反向移植到 EL10。用户可以期待快速迭代和增长。Rocky Linux 计划很快发布 Rocky Linux 10 RISC-V 镜像和安装指南。用户可以在 Rocky Linux Mattermost 频道加入讨论。这一举措使 Rocky Linux 成为一个真正开放、跨架构的生态系统，支持各种架构。

---

## 44. Debian为什么要更改软件？

**原文标题**: Why does Debian change software?

**原文链接**: [https://blog.liw.fi/posts/2025/why-debian-changes/](https://blog.liw.fi/posts/2025/why-debian-changes/)

本文解释了 Debian 为何在发布前修改软件包，强调这些修改是为了遵守 Debian 严格的策略，并致力于提升用户体验和安全性。

修改的主要原因包括：

*   **策略合规性：** Debian 执行其策略手册中规定的策略，以确保标准化（例如，配置文件位置、文档放置）并防止软件包之间的冲突。
*   **互操作性：** Debian 修改软件以确保不同程序之间的无缝集成和协作，例如就 Unix 域套接字位置或用户帐户配置达成一致。
*   **隐私和安全：** Debian 删除了“回拨”或绕过 Debian 软件包系统进行更新的功能，从而保护用户隐私并防止与更新相关的问题。
*   **错误修复和反向移植：** Debian 主动修复错误，包括安全漏洞，并将修复反向移植到旧版本，从而优先考虑用户稳定性和安全性。
*   **自由软件准则：** Debian 严格遵守 Debian 自由软件准则，删除或重新定位非自由组件（例如，具有不可变部分的说明书、非自由徽标）到存档的“非自由”部分。
*   **文档：** 当上游软件缺乏手册页时，Debian 通常会添加手册页，从而提高用户的可访问性和理解。

本质上，Debian 的软件修改旨在创建一个有凝聚力、安全且符合策略的操作系统，该操作系统在坚持自由软件原则的同时优先考虑用户体验。

---

## 45. Google AI Studio 中升级的开发者体验

**原文标题**: An upgraded dev experience in Google AI Studio

**原文链接**: [https://developers.googleblog.com/en/google-ai-studio-native-code-generation-agentic-tools-upgrade/](https://developers.googleblog.com/en/google-ai-studio-native-code-generation-agentic-tools-upgrade/)

Google AI Studio重大升级：Gemini API及生成式AI模型构建平台更强大

*   **Gemini 2.5 Pro代码生成：** Gemini 2.5 Pro集成至AI Studio原生代码编辑器，支持通过文本、图像或视频提示快速开发应用。新增“构建”选项卡简化AI赋能Web应用的构建和部署。通过聊天、版本控制和一键部署至Cloud Run，支持迭代应用开发。Google AI Studio处理API密钥管理，允许用户共享应用而不影响自身API配额（实验性功能）。

*   **多模态生成：** 集中化的“生成媒体”页面提供对Imagen、Veo和Gemini的便捷访问，用于图像生成，同时提供新的语音生成模型以及使用Lyria RealTime的交互式音乐创作。

*   **原生音频功能：** Live API中的Gemini 2.5 Flash现支持原生音频对话，提供30多种声音的自然响应。还增加了主动音频功能，允许模型区分说话者和背景噪音。此外，Gemini 2.5 Pro和Flash的文本转语音（TTS）预览版可灵活控制单扬声器和多扬声器输出。

*   **模型上下文协议（MCP）支持：** Google Gen AI SDK对MCP定义的原生支持简化了与开源工具的集成，一个结合了Google Maps和Gemini API的演示应用对此进行了演示。

*   **URL上下文工具：** 这项新的实验性工具允许模型检索和引用来自所提供链接的内容，有助于事实核查、总结和研究。

这些更新旨在使Google AI Studio成为开发者探索和构建Google最新AI模型的首选平台。所有公告和Google I/O 2025的更新已于2025年5月22日在io.google上发布。

---

## 46. GodAmp：用Godot重写的Winamp 2.9，支持跨平台

**原文标题**: GodAmp: Reimplementation of Winamp 2.9 in Godot, with cross-platform support

**原文链接**: [https://github.com/Dowsley/GodAmp](https://github.com/Dowsley/GodAmp)

GodAmp是一款使用Godot引擎构建的Winamp 2.9跨平台重制版，专为Tool Jam 5创作，目标是最终成为一个完全可定制的音乐播放器，拥有“旧互联网感觉”，并为现代平台更新。 这是一个免费的非商业项目，尊重原Winamp资产的版权。

主要功能包括基本的音乐播放器控制（播放、暂停、停止、上一首/下一首）、播放列表功能（随机播放、重复播放、音量/平衡调整、加载MP3音轨）、一个功能齐全的EQ10均衡器（带有PreAmp和开关选项）以及两个可视化器：波形线和赛车方块。

路线图包括计划增加对更多文件类型的支持、完整的皮肤主题支持、模仿Winamp界面的实际窗口、功能性播放列表、正常工作的频率面板、更多具有更高灵活性的可视化器，以及与特殊键盘按键的集成。 该项目感谢几位艺术家为包含的示例歌曲所做的贡献，确保其免版税状态。

---

## 47. 太阳系或发现新的矮行星

**原文标题**: Possible new dwarf planet found in our solar system

**原文链接**: [https://www.minorplanetcenter.net/mpec/K25/K25K47.html](https://www.minorplanetcenter.net/mpec/K25/K25K47.html)

本期小行星电子通告 (MPEC 2025-K47)，于2025年5月21日发布，报告了小行星2017 OF201的观测数据和轨道要素。观测数据跨越2011年至2018年，使用加拿大-法国-夏威夷望远镜 (T14) 和托洛洛山天文台-DECam (W84) 收集。

计算出的轨道要素显示其具有高离心率轨道 (e=0.9485897)，半长轴为880.0169161个天文单位 (AU)，倾角为16.21146度。其绝对星等 (H) 为3.55，斜率参数 (G) 为0.15。这些轨道特征表明这是一个遥远的天体，可能位于外太阳系。

该通告提供了2017 OF201的简短星历表，预测了其在2025年4月、5月和6月特定日期的天空位置。列出了赤经和赤纬，以及该天体与地球的距离 (Delta)、与太阳的距离 (r)、距角、相位角和视星等 (V)。该天体非常遥远，Delta值约为91 AU。

报告包含残差（观测位置和计算位置之间的差异），证实了轨道确定的准确性。小行星中心 (MPC) 工作人员汇编了这些数据。这项发现的意义取决于未来的观测和精细的轨道分析，以确定该天体的精确分类以及作为矮行星候选者的潜力。

---

## 48. 机器停止 (1909)

**原文标题**: The Machine Stops (1909)

**原文链接**: [https://standardebooks.org/ebooks/e-m-forster/short-fiction/text/the-machine-stops](https://standardebooks.org/ebooks/e-m-forster/short-fiction/text/the-machine-stops)

机器停止运转：描述了一个未来世界，人类生活在地下六边形房间里，彼此隔离，完全依赖一台庞大且无处不在的机器来满足所有需求和互动。瓦什蒂是一个忠于机器的女人，她对自己的讲座和虚拟交流生活感到满意。她的儿子库诺住在世界的另一端，敦促她亲自去看他，表达了对真正联系的渴望以及对看到地球表面的渴望，而现在地球表面被认为是无法居住的。

瓦什蒂最初是抵触的，她厌恶身体旅行的想法，并且怀疑库诺对禁忌地面的兴趣。她害怕直接体验，更喜欢机器提供的过滤现实。库诺批评机器，认为它只提供对现实的肤浅理解，并阻止真正的人际连接。

尽管瓦什蒂不情愿和恐惧，但最终她还是决定克服厌恶，去见库诺，因为他坚持认为“可能会发生非常重要的事情”。她进行了罕见的物理旅行，穿梭于废弃已久的交通系统，揭示了人类在身体和情感上与世界和彼此脱节的程度。由于机器的存在，每个地方都一样，飞艇几乎是空的。这个故事突出了过度依赖技术的危险，以及失去人际联系、好奇心和直接体验的潜在风险。

---

## 49. 不丹可播放唱片邮票的奇妙故事 (2015)

**原文标题**: The curious tale of Bhutan's playable record postage stamps (2015)

**原文链接**: [https://thevinylfactory.com/features/the-curious-tale-of-bhutans-playable-record-postage-stamps/](https://thevinylfactory.com/features/the-curious-tale-of-bhutans-playable-record-postage-stamps/)

本文探讨了不丹1972年发行的可播放唱片邮票的迷人历史。这些迷你黑胶唱片，以每分钟33 1/3转的速度播放，收录了不丹民间歌曲和历史，并以英语和宗喀语（当地语言）呈现。

最初被集邮爱好者忽视的它们，由于被黑胶爱好者发现，价值一路飙升，现在的整套售价高达数百美元。

这些邮票是美国冒险家伯特·托德的创意。他于1951年受邀前往不丹，在向世界银行提出的贷款请求被拒绝后，他建议不丹通过发行邮票来筹集资金。托德获得了皇家授权，并成立了不丹邮票局。

意识到新颖性是成功的关键，托德推出了越来越创新的邮票，包括圆形金箔压花邮票、三角形雪人邮票、3D太空探索邮票、丝绸邮票，甚至还有钢箔邮票。

会说话的邮票是他最具雄心的项目。这套七枚邮票包含歌曲、历史和旁白，使其真正独一无二。托德在邮票设计方面的创新方法极大地提高了不丹的收入。他的女儿弗朗西斯继承了他的事业，并制作了带有关于不丹的纪录片视频的CD-ROM邮票。

---

## 50. 开发者空间

**原文标题**: Devstral

**原文链接**: [https://mistral.ai/news/devstral](https://mistral.ai/news/devstral)

Mistral AI 与 All Hands AI 合作发布 Devstral，一款专为软件工程任务设计的新型开源自主LLM。Devstral 在 SWE-Bench Verified 基准测试中表现优于现有开源模型，实现了 46.8% 的分数，甚至超越了 Deepseek-V3-0324 等更大的模型。

Devstral 旨在解决现实世界软件开发中的挑战，这些挑战需要代码情境化、识别组件之间的关系以及调试复杂函数。它运行在 OpenHands 或 SWE-Agent 等代码代理框架上，并经过训练以解决真实的 GitHub 问题。

主要优势包括其多功能性：Devstral 可以本地部署在单个 RTX 4090 或具有 32GB RAM 的 Mac 上，使其适用于本地开发、对隐私敏感的存储库上的企业使用，以及集成到编码 IDE 或插件中。

该模型在 Apache 2.0 许可下发布，可免费使用和定制。它也可以在 Mistral AI 的 API 上以“devstral-small-2505” 的名称使用，价格与 Mistral Small 3.1 相同。该模型可以从 HuggingFace、Ollama、Kaggle、Unsloth 和 LM Studio 下载。

Mistral AI 鼓励社区反馈，并正在开发一个更大的自主编码模型，即将发布。他们还为私有代码库提供 Devstral 的微调和定制的企业支持。

---

## 51. ZEUS – 密歇根大学新型双拍瓦激光装置

**原文标题**: ZEUS – A new two-petawatt laser facility at the University of Michigan

**原文链接**: [https://news.engin.umich.edu/2025/05/the-us-has-a-new-most-powerful-laser/](https://news.engin.umich.edu/2025/05/the-us-has-a-new-most-powerful-laser/)

密歇根大学ZEUS激光设施成为美国最强大的激光器，功率达到2拍瓦。在NSF资助下，ZEUS将作为一个用户设施，允许来自美国和国际的研究人员进行实验，其应用领域涵盖医学、国家安全、材料科学、天体物理学、等离子体科学和量子物理学。

加州大学尔湾分校的Franklin Dollar领导的首次2拍瓦实验，旨在利用两束激光和重新设计的目标产生高能电子束，其潜力超过更大的粒子加速器。ZEUS团队还计划进行一项标志性实验，即让加速电子与激光脉冲发生碰撞，从而有效地产生泽塔瓦级的脉冲。

文章强调了开发激光器的挑战，包括获取全功率所需的大型钛蓝宝石晶体以及处理使光栅变暗的碳沉积物。尽管存在这些障碍，ZEUS自2023年10月开放以来已经举办了11个用户实验。随着该设施继续升级到其完整的3拍瓦潜力，其开放和灵活的操作预计将吸引广泛的科学家群体并促进创新。

---

## 52. 理解 Go 调度器

**原文标题**: Understanding the Go Scheduler

**原文链接**: [https://nghiant3223.github.io/2025/04/15/go-scheduler.html](https://nghiant3223.github.io/2025/04/15/go-scheduler.html)

本文深入探讨 Go 调度器，重点关注其演变历程以及实现高效并发的底层机制。文章首先解释了编译过程和 Go 运行时 (runtime) 的作用，强调 Go 代码如何被转换为可执行二进制文件，以及运行时函数对于像 goroutine 管理等特性的重要性。

随后，文章追溯了调度器的发展历程，从最初的因锁争用和局部性差而饱受诟病的“原始”方法开始。文章详细描述了各项改进，重点介绍了本地运行队列的引入，以及最重要的逻辑处理器（P）的概念。这引出了 GMP 模型：Goroutine (G)、线程 (M) 和处理器 (P)。

文章详细解释了 GMP 模型：G 代表 goroutine，M 代表由操作系统管理的内核线程，而 P 代表执行 goroutine 的逻辑处理器。文章描述了每个实体的状态机，概述了控制它们行为的转换和条件（例如，goroutine 从 Runnable 状态转换为 Running 状态，线程 Spinning 状态以寻找工作）。文章强调，P 的数量是基于 `GOMAXPROCS` 固定的，并且每个 P 都有一个本地运行队列，从而最大限度地减少锁争用。文章提到，后续章节将涵盖程序引导、goroutine 的创建和调度、抢占、系统调用处理、网络 I/O 以及垃圾回收等主题。

---

## 53. Show HN: ClipJS – 在电脑或手机上编辑你的视频

**原文标题**: Show HN: ClipJS – Edit your videos from a PC or phone

**原文链接**: [https://clipjs.vercel.app/](https://clipjs.vercel.app/)

Show HN: ClipJS：一款可在电脑和手机上使用的视频编辑器，其主要卖点是编辑后的视频没有水印。

---

## 54. 展示HN：用于高保证RISC-V嵌入式系统的机密计算

**原文标题**: Show HN: Confidential computing for high-assurance RISC-V embedded systems

**原文链接**: [https://github.com/IBM/ACE-RISCV](https://github.com/IBM/ACE-RISCV)

ACE-RISCV是一个开源项目，为RISC-V嵌入式系统提供保密计算框架，其特点是具有经过形式化验证的安全监控器。 该项目旨在通过规范架构和围绕安全监控器实现的形式化验证工作，遵循RISC-V CoVE规范的部署模型3，从而提供高保障的安全性。 欢迎合作以推进可证明的保密计算。

主要功能包括支持后量子密码学 (PQC)，用于本地证明（ML-KEM、SHA-384 和 AES-GCM-256），从而能够在资源受限的环境中对保密虚拟机进行身份验证。

该项目目前基于RISC-V 64位，具有特定的扩展（I、A、H、PMP、MMU、IOPMP、CLINT、Sstc），并且可以在SiFive P550评估板上运行。

提供了一个快速入门指南，用于在模拟的RISC-V环境中，在不受信任的Linux KVM虚拟机管理程序下运行示例保密工作负载。 构建该框架需要一台至少具有 4 个内核、4GB RAM 和 50GB 磁盘空间的机器。 详细说明给出了在 Ubuntu 22.04 上设置依赖项的步骤，包括构建工具和 Rust 工具链。

编译说明涵盖构建整个框架或单个组件，如虚拟机管理程序、固件（包括安全监控器）、保密虚拟机和 RISC-V 模拟器。 说明详细介绍了如何运行和测试环境，包括证明以及从保密虚拟机内部检索密钥。 该项目以 Apache 2.0 许可协议发布，并包含对相关研究论文的引用。

---

## 55. 远古爬行动物足迹改写动物进化史

**原文标题**: Ancient reptile footprints are rewriting the history of when animals evolved

**原文链接**: [https://apnews.com/article/oldest-reptile-footprints-australia-963e3c38c8d5782e7ac20f5405f15f89](https://apnews.com/article/oldest-reptile-footprints-australia-963e3c38c8d5782e7ac20f5405f15f89)

美联社报道《远古爬行动物足迹改写动物进化史》称，在澳大利亚发现的爬行动物足迹化石比先前已知的陆地爬行动物存在证据要古老得多。这些足迹在新南威尔士州的砂岩中被发现，可以追溯到大约3.15亿至3.32亿年前，将已知羊膜动物（包括爬行动物、鸟类和哺乳动物）的存在时间提前了1400万至2700万年。

该发现表明，作为第一批完全适应陆地生活的脊椎动物，羊膜动物的进化时间远早于之前的认知。先前的化石证据主要由骨骼遗骸组成，这些遗骸比足迹等痕迹化石更为罕见。这些足迹直接证明了这些早期爬行动物在石炭纪时期在陆地上的存在和活动。

这一发现的意义在于其对我们理解四足动物进化的影响。它暗示着羊膜动物的物种演化和传播可能比之前认为的更快，可能与一个促进其陆地适应的生态变化时期相吻合。这项研究强调了痕迹化石在重建地球生命进化史中的重要性，以及它们如何在骨骼遗骸稀少的情况下提供新的见解。这些发现挑战了既定的时间线，并有必要重新评估爬行动物及其祖先的早期进化。

---

## 56. 毅力过剩会损伤大脑

**原文标题**: Too Much Grit Can Damage Your Brain

**原文链接**: [https://www.inc.com/jessica-stillman/new-science-too-much-grit-can-actually-damage-your-brain/91187193](https://www.inc.com/jessica-stillman/new-science-too-much-grit-can-actually-damage-your-brain/91187193)

过度坚毅会损害大脑
杰西卡·斯蒂尔曼的文章《过度坚毅会损害大脑》探讨了过度坚毅——通常被誉为成功的关键——如何对大脑健康和整体幸福感产生负面影响。文章引用神经学研究表明，不充分休息和恢复地无情追求目标会导致倦怠和大脑的结构性改变。

主旨是，坚毅，定义为对长期目标的坚持和热情，适度是有益的。然而，不断鞭策自己而不允许适当的休息和情绪处理会耗尽认知资源并扰乱大脑的自然活动和休息周期。

文章强调了过度坚毅的潜在负面后果，包括：

*   **决策能力受损：** 不断追求目标带来的慢性压力会影响前额叶皮层，即大脑中负责理性决策的区域。
*   **精神健康问题风险增加：** 倦怠是过度劳累的常见后果，可能导致抑郁症、焦虑症和其他精神健康问题。
*   **认知灵活性降低：** 持续专注于单一目标会使人难以适应不断变化的环境或考虑其他观点。
*   **潜在的脑损伤：** 持续的压力会改变大脑的结构和功能，可能导致长期的认知能力下降。

文章强调了在坚毅与自我同情、正念和充分休息之间取得平衡的重要性。文章建议，优先考虑幸福感并将恢复性实践纳入日常生活中，可以帮助最大限度地发挥坚毅的益处，同时最大限度地减少其潜在的弊端。最终，可持续的成功需要一种兼顾成就和大脑健康的整体方法。

---

## 57. VAX/VMS带来的人生经验 (2013)

**原文标题**: Some Life Lessons from VAX/VMS (2013)

**原文链接**: [https://davewentzel.com/content/some-life-lessons-from-vax-vms/](https://davewentzel.com/content/some-life-lessons-from-vax-vms/)

Dave Wentzel 的这篇博文回顾了他从 VAX/VMS 系统工作中获得的经验教训，他非常怀念这个系统。作者分享了他在大学勤工俭学期间担任计算机实验室技术员，以及后来在大型电信公司担任计算机操作员的轶事。他强调幽默感在科技行业的重要性，并提到了 HAL/IBM 和 VMS/WNT 的文字游戏。

他强调了努力工作和主动性的价值，回忆了他如何因在计算机实验室的积极主动而获得晋升和更多责任。他描述了支持用户使用复杂的 VMS 电子邮件所面临的挑战。

另一个关键的教训是关于从失败中学习，他回忆起一次事故，由于配置错误的“已发送邮件”宏，他不小心使电子邮件系统崩溃。虽然他最初害怕被解雇，但他快速的修复几乎让他获得晋升，但随后又受到了审查。

最后，他饶有兴致地回忆起他作为学生在数据中心使用 VAX 系统作为头枕长达两年的时间。

---

## 58. 三年远程工作

**原文标题**: 3 Years of Remote Work

**原文链接**: [https://www.brendangregg.com/blog/2025-05-22/3-years-of-extremely-remote-work.html](https://www.brendangregg.com/blog/2025-05-22/3-years-of-extremely-remote-work.html)

本文详细介绍了澳大利亚一位为美国公司（英特尔）远程工作的员工的经历，重点讲述了远程工作所面临的挑战和误解，尤其是在处理显著时区差异时。作者在过去三年里，参加了77次凌晨1点到6点之间的会议，同时保持着正常的日常工作。

主要问题包括尽管不想抱怨工作时间，但还是难以坚持早起参加会议，之后再进行标准工作。作者强调了拥有配备高质量音频和视频的专用家庭办公室对于有效的远程沟通的重要性。

作者提供了管理远程工作的技巧，例如记录非工作时间的会议、避免抱怨工作时间、保持成就记录以及积极沟通时区冲突。一个常见的误解是远程工作者都在睡觉且无法联系，即使问题在于日程安排冲突。

文章还涉及了不常被讨论的、不规律作息对身体健康的影响，以及因“眼不见为净”而可能造成的职业发展限制。尽管存在这些挑战，作者也承认远程工作的好处，并列举了Linux开发和他们自己的书籍项目等成功案例。文章最后呼吁那些考虑结束远程工作政策的人，敦促他们避免假设，并考虑远程工作者经历的真实情况。

---

## 59. 展示 HN：无限叶隐

**原文标题**: Show HN: Infinite Hagakure

**原文链接**: [https://hagakure.space](https://hagakure.space)

提供的文字摘自《叶隐》，是武士的实践和精神指南。它强调了对主君坚定不移的忠诚，甚至达到愿意拥抱死亡的地步。武士道存在于死亡之中，并在于为领主献出生命的准备之中。懦弱等同于在不履行职责的情况下苟且偷生。

文本强调无私奉献，将主君的福祉置于个人利益或舒适之上。一个好的家臣的定义在于他对主君的奉献以及他愿意将一切托付给他。虽然智慧和才能很有价值，但坚定不移的奉献精神至关重要。

《叶隐》还探讨了提出建设性批评的挑战。它强调在纠正他人错误时需要策略、同理心和理解，突出了简单诽谤的徒劳。关键是建立信任，并以容易接受和理解的方式提供建议。

此外，文本还触及了男性精神和勇气的衰落，感叹巧妙的借口和逃避繁重任务的兴起。它强调了内心纯洁和直接的重要性，表明真诚的愚钝之人比肤浅的聪明之人更可取。最后，它强调了咨询和学习古代智慧的好处，以避免自私自利并改善自己。

---

## 60. Show HN: 无尽《叶隐闻书》

**原文标题**: Show HN: Infinite Hagakure

**原文链接**: [https://hagakure.space](https://hagakure.space)

本文节选自《叶隐》，一本为武士提供的实用和精神指南。它强调对主君坚定不移的忠诚和对死亡的准备是武士道的核心。 《叶隐》批判那些将自身利益和聪明才智置于真正的奉献和无私服务之上的人。

要点包括：

*   **忠诚与无私：** 一名优秀的家臣应将主君的福祉置于一切之上，甚至不惜牺牲自己的生命。
*   **接受死亡：** 武士道在于死亡；一个人应该毫不犹豫地为他的领主而死。
*   **对肤浅的批判：** 文本谴责那些过于关注智慧和聪明才智的人，强调直接和简单的价值。
*   **进谏的重要性：** 向他人寻求建议并研究古代的智慧可以帮助个人克服偏见并做出明智的决定。
*   **技能/理解的层次：** 本文概述了任何领域的熟练程度阶段，从最初的无能到深刻的掌握，最后到一种谦逊的专业知识状态。
*   **敬畏：** 它强调必须敬畏主君、父母、守护神和守护佛。

《叶隐》提倡一种充满目标、奉献精神和对自身死亡的持续意识的生活，敦促读者拥抱无私，并将为领主服务置于一切之上。 它告诫人们不要将聪明才智和自身利益置于真正的奉献和牺牲的准备之上。

---

## 61. 店面 Web 组件

**原文标题**: Storefront Web Components

**原文链接**: [https://shopify.dev/docs/api/storefront-web-components](https://shopify.dev/docs/api/storefront-web-components)

无法访问文章链接。

---

## 62. 使用 Haskell 的值限制违反内存安全

**原文标题**: Violating memory safety with Haskell's value restriction

**原文链接**: [https://welltypedwit.ch/posts/value-restriction](https://welltypedwit.ch/posts/value-restriction)

本文深入探讨了Haskell中内存安全违规的可能性，尽管Haskell具有纯粹性，重点关注`IO` monad和值限制的作用。作者证明，虽然Haskell的`let`绑定没有传统的值限制，但`IO` monad的接口提供了一个类似的约束，以防止可能导致类型和内存不安全的多态引用。

核心论点通过展示一个看似安全的`unsafeCoerce`函数（依赖于`IO`内的`IORef`）如何因`IO`类型的结构而无法泛化来说明。由于`forall`量词位于`IO`之外，因此阻止了`IORef`在`IO`上下文中变为多态。

文章随后通过`MonadGen`类型类探讨了“可泛化Monad”的概念，表明像`Identity`和`State`这样的monad*可以*支持monadic绑定的泛化，从而有效地模仿了纯`let`绑定的功能。

令人惊讶的高潮揭示，`IO`尽管具有保护性接口，但可以通过直接访问其内部结构来操纵以违反内存安全。通过利用`IO`的底层`State# RealWorld`机制并将其装箱以规避GHC的限制，作者成功地为`IO`实现了`MonadGen`，并随后构建了一个有效的`unsafeCoerceIO`函数，该函数触发了段错误。

结论强调，Haskell的纯粹性并不能固有地保证内存安全，而`IO`的monadic接口（而非其基本定义）提供了必要的保护。解包`IO`构造函数，即使不复制或丢弃`State#`令牌，也从根本上是不安全的，这挑战了普遍的信念，并突出了尊重monadic接口的重要性。

---

## 63. 涡轮增压的线粒体助力鸟类史诗般的迁徙之旅

**原文标题**: 'Turbocharged' Mitochondria Power Birds' Epic Migratory Journeys

**原文链接**: [https://www.quantamagazine.org/turbocharged-mitochondria-power-birds-epic-migratory-journeys-20250519/](https://www.quantamagazine.org/turbocharged-mitochondria-power-birds-epic-migratory-journeys-20250519/)

本文探讨了候鸟如何通过研究线粒体（细胞的能量工厂）的作用来实现其令人难以置信的长途飞行。它重点介绍了最近的研究，该研究表明这些鸟类不仅在整体身体成分上，而且在亚细胞水平上，特别是在飞行肌肉的线粒体中，都经历了生理变化。

两项关于黄腰柳莺和白冠麻雀的独立研究表明，在迁徙期间，这些鸟类会发展出“涡轮增压”的线粒体：比非迁徙鸟类或非迁徙状态下的鸟类数量更多、效率更高、相互连接更紧密。这些增强的线粒体更擅长产生 ATP（细胞的能量货币），为鸟类的持续飞行提供燃料。

该研究还表明，这些线粒体变化是由季节性光线线索触发的，表明这是一种独立于基因改造的快速适应。这种“表型可塑性”使鸟类无需长时间的训练即可为迁徙做准备。

虽然改进的线粒体性能可能带来潜在的负面影响，例如增加有害活性氧的产生，但候鸟可能会通过其饮食来减轻这种影响，食用富含抗氧化剂的食物。

文章最后强调了线粒体在各种生理适应中的重要性，并提出了潜在的未来研究方向，包括研究如何复制人类中的这些线粒体增强，以用于与运动和衰老相关的应用。

---

## 64. JEP 519：精简对象头

**原文标题**: JEP 519: Compact Object Headers

**原文链接**: [https://openjdk.org/jeps/519](https://openjdk.org/jeps/519)

JEP 519 提议：将“紧凑对象头”从实验特性提升为 JDK 25 的产品特性。紧凑对象头在 JDK 24 中作为替代的对象头布局（JEP 450）引入，并在 Oracle 和 Amazon 的严格测试中展示了稳定性和性能改进。

证据表明，启用紧凑对象头可带来显著益处，包括减少堆空间使用量（例如，在 SPECjbb2015 中减少 22%）、减少 CPU 时间（例如，在 SPECjbb2015 中减少 8%）以及减少垃圾回收次数（例如，G1 和 Parallel 收集器均减少 15%）。JSON 解析器基准测试也显示运行时性能提高了 10%。

这项变更意味着，不再需要使用目前启用紧凑对象头所需的命令行选项 `-XX:+UnlockExperimentalVMOptions` 以及 `-XX:+UseCompactObjectHeaders`。依赖于 `-XX:+UnlockExperimentalVMOptions` 的现有测试将被调整。

JEP 承认未来可能需要额外的对象头位，特别是对于 Valhalla 项目（已经预留了 4 位），并建议在需要更多空间时使用 Lilliput 项目中原型设计的技术（缩小压缩类指针和身份哈希码）。由于已经在 JEP 450 下进行了广泛的测试，因此不计划进行额外的测试。非目标是将紧凑对象头作为默认的对象头布局。

---

## 65. 离散文本扩散解释

**原文标题**: Discrete Text Diffusion Explained

**原文链接**: [https://aaronlou.com/blog/2024/discrete-diffusion/](https://aaronlou.com/blog/2024/discrete-diffusion/)

本文介绍了一种称为得分熵离散扩散（SEDD）模型的新方法，作为自回归语言建模的一种替代方案。尽管自回归语言建模在领域内占据主导地位，但它也存在诸如漂移和迭代采样等局限性。

作者首先解释了概率建模及其在诸如自然语言等离散数据领域中所面临的挑战。在这些领域中，大量可能的文本组合使得直接建模概率变得困难。自回归建模通过预测序列中的下一个token来规避这个问题，但作者认为由于其顺序处理和在控制任务中的局限性，它并非理想选择。

SEDD模型提供了一种新的方法，即通过建模具体的得分（相邻数据点之间的概率比率）而不是直接建模概率。这消除了计算归一化常数的需求，而归一化常数是基于能量模型的重大障碍。

为了训练模型，作者引入了得分熵，一种推广了交叉熵的损失函数，它能够学习任意概率比率。然而，得分熵损失依赖于知道这些比率。作者随后引入了去噪得分熵损失，该损失用已知的转移比率取代未知的比率，从而实现易于处理的优化。

本文从扩散模型中汲取灵感，利用学习到的具体得分来迭代地将随机值去噪成数据点。离散扩散过程被用于建模向离散文本样本添加“噪声”的过程，该过程涉及随机突变序列的元素。

---

## 66. 默认情况下，Signal 不会撤回消息。

**原文标题**: By default, Signal doesn't recall

**原文链接**: [https://signal.org/blog/signal-doesnt-recall/](https://signal.org/blog/signal-doesnt-recall/)

Signal默认启用Windows 11“屏幕安全”功能以抵御微软Recall

---

## 67. 无需CRDT或OT的协同文本编辑

**原文标题**: Collaborative Text Editing Without CRDTs or OT

**原文链接**: [https://mattweidner.com/2025/05/21/text-without-crdts.html](https://mattweidner.com/2025/05/21/text-without-crdts.html)

本文提出了一种协作文本编辑的替代方法，该方法避免了无冲突复制数据类型 (CRDT) 和操作转换 (OT) 的复杂性。核心思想是为每个文本字符标记一个全局唯一ID (UUID)，并让客户端向服务器发送“在…之后插入”的操作，引用现有的ID。然后，服务器直接将新字符插入到被引用ID之后。

这种方法通过确保服务器以可预测的方式更新其自身的文本，而无需“重新定位”索引，从而解决了并发编辑的挑战。在处理删除时，服务器会保留ID，即使在删除关联字符后也是如此，将其标记为已删除，而不是完全删除，以保持未来操作的插入上下文。

对于实时协作，本文讨论了服务器协调，在这种协调中，客户端可以乐观地应用本地更新，然后通过撤消、应用远程操作和重做挂起的本地操作来与服务器的状态进行协调。一个更简单的替代方案是在存在挂起的本地操作时阻止客户端处理远程操作。

作者强调，这种方法虽然与 CRDT（如唯一 ID 和墓碑）有相似之处，但在处理顺序方面有所不同。它没有依赖复杂的 CRDT 排序算法，而是提供了对插入点的直接控制，使其更加灵活和可定制。这种 DIY 方法使开发人员能够更轻松地实现使用现有 CRDT/OT 库难以或不可能实现的功能，例如部分文档加载、细粒度权限、建议更改和对各种操作类型的支持。

---

## 68. Show HN: Forge – 基于 K8s 或 EC2 的安全多租户 GitHub Actions Runner

**原文标题**: Show HN: Forge – Secure, Multi-Tenant GitHub Actions Runners on K8s or EC2

**原文链接**: [https://github.com/cisco-open/forge](https://github.com/cisco-open/forge)

Forge：简化并安全管理AWS上GitHub Actions Runner的开源平台，专为平台团队设计。它利用`terraform-aws-github-runner`和`actions-runner-controller`等工具，为临时Runner提供可扩展的多租户环境。

主要功能包括：

*   **临时Runner:** 在EC2和EKS上自动伸缩Runner，消除空闲成本。
*   **租户隔离:** 使用IAM和OIDC的安全边界。
*   **零接触自动化:** 自动化生命周期管理（补丁、更新、漂移检测）。
*   **内置可观测性:** 开箱即用的仪表盘、日志和指标。
*   **成本优化:** Spot实例和扩展至零的能力。
*   **灵活配置:** 自带AMI、实例类型、子网等。
*   **多Runner支持:** 同时部署多种Runner类型。
*   **广泛的操作系统支持:** Linux (x64/arm64) 和 Windows。
*   **GitHub Cloud & GHES 支持:** 无缝支持两种托管模式。

Forge旨在通过Terraform (Tofu)轻松设置，其文档提供了基础设施设置、租户配置和使用指南。它鼓励社区贡献，并提供未来发展路线图。Forge解决了在AWS中管理GitHub Actions Runner时，尤其是在多租户环境中，围绕安全性、成本和运营开销的常见痛点。

---

## 69. Ruby中Block、Proc和Lambda的区别 (2013)

**原文标题**: What Is the Difference Between a Block, a Proc, and a Lambda in Ruby? (2013)

**原文链接**: [https://blog.awaxman.com/what-is-the-difference-between-a-block-a-proc-and-a-lambda-in-ruby](https://blog.awaxman.com/what-is-the-difference-between-a-block-a-proc-and-a-lambda-in-ruby)

本文解释了 Ruby 中代码块 (blocks)、Proc 对象和 Lambda 表达式之间的区别，它们都是用于组织和执行代码的机制。

**代码块 (Blocks)** 是用 `{}` 或 `do...end` 定义的代码片段，是方法调用语法的一部分。它们只能在方法的参数列表中出现一次，并且本身不是对象。

**Proc 对象 (Procs)** 是 `Proc` 类的实例，允许它们被视为对象，赋值给变量并传递。您可以将多个 Proc 对象作为参数传递给方法。Proc 对象使用 `Proc.new` 创建。

**Lambda 表达式 (Lambdas)** 是一种特殊的 Proc 对象，也是 `Proc` 类的实例，但存在关键差异。它们使用 `lambda { ... }` 创建。

Proc 对象和 Lambda 表达式之间的核心区别是：

1. **参数检查:** Lambda 表达式严格执行传递的参数数量，如果数量不正确，则引发 `ArgumentError`。Proc 对象更宽松，忽略额外的参数或为缺失的参数返回 `nil`。
2. **`return` 关键字:** 在 Lambda 表达式中，`return` 仅退出 Lambda 表达式。在 Proc 对象中，`return` 退出调用该 Proc 对象的方法。

本文还定义了 **闭包 (closure)**，即有权访问其周围环境（局部变量）的函数，即使在外部环境中调用时也是如此。Proc 对象和 Lambda 表达式都可以充当闭包。

最后，它简要介绍了名称“lambda”和“Proc”的由来，分别将它们与 Lambda 演算和过程式编程联系起来。

---

## 70. 动画分解 (2012)

**原文标题**: Animated Factorization (2012)

**原文链接**: [http://www.datapointed.net/visualizations/math/factorization/animated-diagrams/](http://www.datapointed.net/visualizations/math/factorization/animated-diagrams/)

动画分解图：一种数据驱动的数学分解可视化教学方法

---

## 71. 下一个密码或可储存在塑料中

**原文标题**: Next Password Could Be Stored in Plastic

**原文链接**: [https://spectrum.ieee.org/plastic-data-storage](https://spectrum.ieee.org/plastic-data-storage)

2025年5月21日《计算新闻》报道，研究人员开发出一种在名为寡聚氨酯的微型定制塑料中存储数据的方法。这项创新为密码安全和数据存储提供了一种潜在的新途径。信息可以被编码在塑料的分子结构中，然后使用电化学技术检索，而不是依赖传统方法。《电气电子工程师学会频谱》被引用为信息来源，并包含来自Bipin Pandey的原始图像。 Elie Dolgin撰写的这篇文章只需3分钟阅读，重点介绍了数据存储技术中这一潜在的突破性进展。

---

## 72. DumPy: 允许犯错的NumPy

**原文标题**: DumPy: NumPy except it's OK if you're dum

**原文链接**: [https://dynomight.net/dumpy/](https://dynomight.net/dumpy/)

本文介绍DumPy，一种旨在简化数组操作的NumPy替代方案。DumPy通过重新引入类似循环的语法，同时利用底层向量化运算来提高性能。作者认为，NumPy的复杂性源于将循环功能推入各个函数以避免缓慢的Python循环，从而导致对数组形状和函数行为的困惑。

DumPy旨在通过允许用户使用直观的循环和索引符号来表达数组运算来解决这个问题，DumPy随后将其编译成向量化运算，理想情况下在GPU上运行。核心机制涉及“映射”数组，其中使用字符串或dp.Range对象进行索引会创建维度较少的虚拟数组。然后，DumPy函数基于映射维度中的共享标签自动向量化计算，并利用JAX的`vmap`进行实际的向量化。

本文提供了DumPy与NumPy和JAX（使用`vmap`）在各种任务（如希尔伯特矩阵创建、批量协方差计算、移动平均、索引、高斯密度评估和多头自注意力）中的比较示例。作者认为，与NumPy的形状操作和JAX的`vmap`配置相比，DumPy的语法更具可读性和直观性，所需的精神负担更少。虽然DumPy的底层实现依赖于现有的向量化工具，但其主要贡献在于通过熟悉的类似循环的语法简化用户体验。

---

## 73. 大型机现代化改造故事

**原文标题**: Tales from Mainframe Modernization

**原文链接**: [https://oppi.li/posts/tales_from_mainframe_modernization/](https://oppi.li/posts/tales_from_mainframe_modernization/)

阿克谢的《大型机现代化故事》讲述了COBOL代码库现代化的经验。他重点介绍了在传统大型机系统中发现的“意外”和历史怪癖。

主要内容包括：

*   **十进制数值：** COBOL使用十进制数值，如`PIC 9(3)`定义一个3位数所示。
*   **国际化：** 代码库通常包含国际化策略，例如使用`REDEFINES`结构以其他语言重新定义数据定义，西班牙语变量就是证明。
*   **字符串解析：** COBOL允许通过定义具有特定布局的内存区域来解析字符串，例如将日期字符串分解为日、月和年。
*   **提前退出：** `COMPUTE ABEND = CONSTANT-ZERO / CONSTANT-ZERO`用作触发异常作业终止的方法。
*   **神秘常量：** 文章提到一个包含前800个自然数定义为字符串常量的奇怪文件。
*   **DD语句：** JCL（作业控制语言）中的DD语句，代表“数据定义”，是UNIX中`dd`命令的起源。

作者目前正在构建tangled.sh，一个去中心化的代码协作平台。

---

## 74. 可视化整个 Chromium 包含关系图

**原文标题**: Visualizing entire Chromium include graph

**原文链接**: [https://blog.bkryza.com/posts/visualizing-chromium-include-graph/](https://blog.bkryza.com/posts/visualizing-chromium-include-graph/)

本文详细介绍了使用`clang-include-graph`可视化Chromium include图的过程，该工具用于分析C/C++项目include图。作者旨在针对大型代码库测试新的`clang-include-graph`版本。

该过程包括几个步骤：构建Chromium以生成`compile_commands.json`，使用`clang-include-graph`创建include图的GraphML表示，以及使用Gephi可视化该图。作者提供了一个Docker镜像以实现可复现性，并概述了获取Chromium源代码、生成`compile_commands.json`（由于Chromium的自动生成代码而必需）以及使用带有特定标志的`clang-include-graph`生成GraphML文件的手动步骤。

生成的图包含Chromium `src`目录中的源文件和头文件，并将`#include`指令表示为边。然后，作者使用带有NetworkX的Python脚本计算图统计信息，揭示了被包含最多的文件、包含最多include的文件、循环的数量以及其他指标。

最后，本文讨论了使用Gephi可视化该图。最初的尝试证明没有帮助，这促使作者使用表示顶层目录（组件）的节点属性和基于组件的颜色来丰富图形数据。作者标记了10个被包含最多的文件以及每个组件中的至少一个文件，以提高可读性。提供了一个NetworkX脚本将这些注释添加到GraphML文件中，为在Gephi中可视化做准备。

---

## 75. 伦敦的水泵：奇异历史自由流淌 (2024)

**原文标题**: London’s water pumps: Where strange history flows freely (2024)

**原文链接**: [https://londonist.com/london/features/london-s-water-pump](https://londonist.com/london/features/london-s-water-pump)

无法访问文章链接。

---

## 76. Lune：独立Luau运行时

**原文标题**: Lune: Standalone Luau Runtime

**原文链接**: [https://github.com/lune-org/lune](https://github.com/lune-org/lune)

Lune：一个独立的Luau运行时，旨在提供类似于Node.js或Deno的精简高效开发体验，但专门针对Luau。Lune使用Rust构建，注重性能和安全，强调异步API，并在一个小型可执行文件中（压缩后约5MB）包含必要的功能。

主要功能包括：简洁易用的界面，全面的文件系统操作、网络和标准输入/输出API。它还拥有详尽的文档，可在线和离线访问。此外，Lune通过移植的任务调度器和用于操作Roblox场景和模型文件的可选库，为Roblox开发者提供了一个熟悉的运行时环境。

Lune优先考虑代码可读性，而非简洁性，其目的不是在Roblox环境之外运行完整的Roblox游戏，而是专注于不同的应用场景。文档会指导用户完成安装过程，以便开始使用Lune。

---

## 77. 我有耳鸣。不推荐。

**原文标题**: I have tinnitus. I don't recommend it

**原文链接**: [https://blog.greg.technology/2025/05/20/tinnitus.html](https://blog.greg.technology/2025/05/20/tinnitus.html)

作者讲述了在一次音乐会后患上永久性耳鸣的经历，并强烈建议大家避免这种情况。他们之前在电子音乐演出中对耳朵保护漫不经心，事后只会出现暂时性耳鸣。但这次，耳鸣从未停止，这让他们开始质疑那次活动的音量、与扬声器的距离、或特定频率，以及之前暴露的累积效应。

作者强调了对场地危险造成的伤害反应的差异。激光造成的视力障碍会立即引起重视，但因过高音量造成的永久性听力损伤却很少导致场地承担后果。作者因噪音而感到身体疼痛，并采取了积极的安全措施，例如使用耳塞和骑自行车时佩戴防护装备。

他们现在理解并践行了曾经认为不必要的预防措施，强调了永久性损伤发生的容易程度。最后，他们恳请读者保护听力、佩戴头盔、远离激光，并告诫大家要避免因可预防的残疾而带来的悲伤和遗憾。他们已经采取了一种“老爸”的姿态，建议朋友们优先考虑安全，这为他们赢得了昵称“seguridad”（安全）。

---

## 78. 像维京人一样航行的考古学家意外发现

**原文标题**: Archaeologist sailing like a Viking makes unexpected discoveries

**原文链接**: [https://phys.org/news/2025-05-archaeologist-viking-unexpected-discoveries.html](https://phys.org/news/2025-05-archaeologist-viking-unexpected-discoveries.html)

隆德大学的考古学家格里尔·贾瑞特正在研究维京航海路线，他驾驶一艘维京复制船沿挪威海岸航行。他的研究表明，维京人比之前认为的航行得更远离陆地，并且更广泛地利用了一个由较小的、分散的港口组成的网络。贾瑞特的航行超过5000公里，涉及在开阔水域和具有挑战性的峡湾条件下航行，证明了维京船只的适航性。

为了重建维京航海方法，贾瑞特将他的经验与对挪威海员的采访相结合，借鉴他们的传统知识。他强调维京人依赖“心理地图”，利用与海岸地标相关的的故事和神话进行导航，这是一种“海洋文化精神景观”。

贾瑞特的研究沿挪威海岸确定了四个潜在的“避风港”——较小的、易于进入的港口。他认为这些避风港在促进主要维京中心之间的贸易和旅行方面发挥了关键作用，为休息和互动提供了安全的场所。尽管面临设备故障和恶劣天气等挑战，贾瑞特的研究强调了能干和合作的船员的重要性，以及维京航海所需的韧性。他的研究结果发表在《考古方法与理论杂志》上。

---

## 79. 突破性科学发现是否越来越难寻？

**原文标题**: Are groundbreaking science discoveries becoming harder to find?

**原文链接**: [https://www.nature.com/articles/d41586-025-01548-4](https://www.nature.com/articles/d41586-025-01548-4)

本文探讨了一种观点，即突破性科学发现正变得越来越难寻，这引发了科学家和政策制定者之间的辩论和担忧。文章的核心是 Russell Funk 及其同事的一项研究，该研究表明，随着时间的推移，科学论文和专利的颠覆性有所下降，这意味着新的研究成果不太可能使先前的发现过时。

文章深入探讨了衡量研究中的“颠覆性”和“新颖性”的各种视角，强调了引用模式和语言分析等指标的挑战和局限性。尽管一些研究人员仍然怀疑当前指标能否准确捕捉颠覆性，但越来越多的人认为科学创新确实变得更加困难。

对于这种感知到的下降，人们提出了几个原因，包括行政负担的增加、发表压力导致研究被“香肠切割”、科学事业日益复杂和昂贵，以及现有知识的庞大数量使得突破变得更具挑战性。文章引用了半导体研究和药物开发等领域研发投资回报递减的证据。尽管科学资金和研究人员数量大幅增加，但真正突破性发现的速度似乎并未跟上。研究人员目前正在尝试新的方法来量化突破性工作，以促进其未来的发展。

---

## 80. LLM函数调用无法规模化；代码编排更简单，更有效。

**原文标题**: LLM function calls don't scale; code orchestration is simpler, more effective

**原文链接**: [https://jngiam.bearblog.dev/mcp-large-data/](https://jngiam.bearblog.dev/mcp-large-data/)

仅依赖LLM处理和编排来自MCP（多智能体协作协议）工具调用的数据是低效且难以扩展的，尤其是在处理真实世界数据时。本文指出，MCP服务器（如Linear和Intercom）返回的大型JSON Blob中包含冗余数据，迫使LLM重复大量信息，导致成本增加、处理速度降低以及潜在的数据不准确性。

作者提倡转向代码编排，即LLM生成代码来与MCP工具的结构化数据进行交互和处理。这种方法利用了代码执行环境的优势：可扩展性、保证数据完整性，以及使用NumPy或pandas等库执行复杂数据转换的能力。代码还可以促进工具链和甚至LLM内启（代码调用LLM进行非结构化数据处理）。

本文强调，MCP规范中输出模式的出现是实现此方法的关键，允许直接操作结构化数据。 然而，它也承认了创建安全且可扩展的“AI运行时”的挑战，该运行时可以执行AI生成的代码，并有权访问MCP和用户数据，重点关注沙盒环境和无状态但持久的执行。 作者最后邀请大家对他们的方法提出反馈，并强调了他们在Lutra的工作。

---

## 81. CPanel的IPv6大修

**原文标题**: CPanel's IPv6 Overhaul

**原文链接**: [https://blog.apnic.net/2025/05/21/cpanels-ipv6-overhaul/](https://blog.apnic.net/2025/05/21/cpanels-ipv6-overhaul/)

本文讨论了cPanel最近在其企业网站TNC和Merlot上部署AAAA记录（IPv6地址）一事。主要问题在于，通过IPv6访问时，这两个网站目前均已损坏且无法访问。这意味着这些特定网站的IPv6配置或服务器设置存在问题。简而言之，虽然cPanel已采取措施启用IPv6连接，但TNC和Merlot的实施目前失败。

---

## 82. OpenAI将收购Jony Ive的人工智能初创公司

**原文标题**: OpenAI to buy AI startup from Jony Ive

**原文链接**: [https://www.bloomberg.com/news/articles/2025-05-21/openai-to-buy-apple-veteran-jony-ive-s-ai-device-startup-in-6-5-billion-deal](https://www.bloomberg.com/news/articles/2025-05-21/openai-to-buy-apple-veteran-jony-ive-s-ai-device-startup-in-6-5-billion-deal)

无法访问文章链接。

---

## 83. 搭建我自己的太阳能发电系统

**原文标题**: Building my own solar power system

**原文链接**: [https://medium.com/@joe_5312/pg-e-sucks-or-how-i-learned-to-stop-worrying-and-love-building-my-own-solar-system-acf0c9f03f3b](https://medium.com/@joe_5312/pg-e-sucks-or-how-i-learned-to-stop-worrying-and-love-building-my-own-solar-system-acf0c9f03f3b)

乔·埃克伦德对太平洋煤气电力公司不断上涨的电费感到沮丧，决定在湾区建造自己的太阳能发电系统。他研究了各种方案，最初考虑建造一个小型的系统来抵消其服务器机架的功耗，但最终选择了更大的系统来消除他的电费账单。他从太阳能公司收到的报价从4.5万美元到5.5万美元不等，都是容量不足的电池系统。决定自己动手后，他估计他可以用大约3万美元（在享受退税前）建造一个类似的系统。

他选择了EG4设备（逆变器和电池）和Aptos太阳能电池板，为了提高效率，他选择了带有Tigo优化器的传统组串式逆变器，而不是微型逆变器。他还聘请了一位太阳能规划师来处理城市审批并绘制必要的图纸。

安装包括更换新屋顶，使用Unistrut安装沉重的电池（在意识到最初的木制框架存在火灾隐患后），并使用新的子面板配置系统以满足城市要求。他解释了他设置主服务面板（MSP）的原因，以及选择并网和离网逆变器模式的原因，强调了即使在无意中也可能通过并网模式导出电力。他从Signature Solar购买了他的设备。

他强调确保所有设备都通过UL认证并批准在加利福尼亚州使用，并且他描述了快速关断功能（通过Tigo优化器实现）的重要性。他最终选择了将室外额定的电池安装在室内。

---

## 84. 构建一个能自我改进的自主图像生成器

**原文标题**: Building an agentic image generator that improves itself

**原文链接**: [https://simulate.trybezel.com/research/image_agent](https://simulate.trybezel.com/research/image_agent)

Palash Shah 探索构建一个自主图像生成器，该生成器使用大型语言模型 (LLM) 作为评估器和 OpenAI Image API，迭代地提高图像质量。目标是自动化生成图像的优化，解决诸如文本模糊和整体图像吸引力等问题。

最初的方法是使用 LLM (o3) 作为评判者来识别生成图像中的缺陷。然后使用 /edit 端点，根据 LLM 的反馈来纠正这些问题。这种方法在通过多次迭代提高文本清晰度方面证明是有效的，但很快就达到了瓶颈。将评估器扩展到评估图像构图和吸引力产生了较差的结果，推测是由于模型同时难以处理创造性和技术性任务。一种改进的工作流程将文本校正与整体质量提升分开，效果更好。

第二种方法尝试使用 LLM 生成模糊文本周围的边界框，并将这些框用作通过 OpenAI API 进行有针对性编辑的蒙版。然而，LLM 难以产生准确的像素空间关联，导致无效的修改。

结论强调，虽然 LLM 擅长识别语义层面的图像缺陷，但它们在诸如边界框生成和局部遮蔽等精确的像素级操作方面表现不佳。LLM 在将推理约束在离散维度时最为有效，并且在图像生成的多模态评估中，应首选 LLM 作为评判者的方法。

---

## 85. 加快 iText 表格渲染速度

**原文标题**: Making iText's table rendering faster

**原文链接**: [https://kb.itextpdf.com/itext/how-i-made-pdf-table-rendering-faster](https://kb.itextpdf.com/itext/how-i-made-pdf-table-rendering-faster)

本文详细介绍了对iText Core表格渲染的性能优化，重点在于解决由大量单元格导致的性能下降问题。作者首先建立了性能基线，揭示了单元格数量增加时的二次时间复杂度。分析表明，边框合并是主要的性能瓶颈，尤其是在`TableBorderUtil#createAndFillBorderList`和`CollapsedTableBorders#getCollapsedList`中。

第一个优化是在`CollapsedTableBorders#getVerticalBorder`中缓存合并边框计算的结果，以避免内部列的冗余计算。这显著缩短了渲染时间，将一个包含50,000个单元格的表格的渲染时间从35秒降至1.3秒。

作者随后调查了带标签表格的性能影响，发现与未带标签表格相比，性能大幅下降。分析表明，iText标签机制中的`isKidFlushed`安全检查是开销的主要来源。此检查涉及对PDF对象的昂贵解析。通过重写此检查以直接利用iText的底层PdfObject API并避免解析，作者实现了又一次显著的性能提升。包含50,000个单元格的表格的渲染时间从300秒减少到111秒。

最后，本文简要提及了通过缓存标签提示键和删除重复函数调用来进一步减少渲染时间的其他优化。总之，作者通过最少的代码更改显著提高了iText的表格渲染性能，主要是通过缓存结果和避免冗余计算，从而大大缩短了运行时间。

---

## 86. 半导体 Scaling 的漫长弧线

**原文标题**: The Long Arc of Semiconductor Scaling

**原文链接**: [https://www.chipstrat.com/p/the-long-arc-of-semiconductor-scaling](https://www.chipstrat.com/p/the-long-arc-of-semiconductor-scaling)

本文记录了半导体缩放技术的早期历史，从真空管到分立晶体管以及固态电子的兴起。文章首先强调了基于真空管的计算机的不可靠性和笨重性，并将其与使用基于晶体管逻辑的IBM 1401进行了对比。

文章随后深入探讨了贝尔实验室晶体管的发明，这是由于希望用更可靠的固态开关取代真空管。文章回顾了对锗等半导体材料的研究，最终在1947年由约翰·巴丁和沃尔特·布拉顿成功制造了第一个晶体管放大器。

文章强调了晶体管作为“世界上一种全新的事物”的意义，详细介绍了贝尔实验室改进设计和授权技术的努力。文章强调了肖克利的书籍在教育工程师（包括台积电创始人张忠谋）方面的重要性。

晶体管的出现开创了固态电子时代，从而产生了更小、更节能、更具成本效益的设备。贝尔实验室的被许可方索尼在推广晶体管收音机方面发挥了关键作用，标志着便携式消费电子产品的开端。文章还提到了晶体管的早期大规模应用，例如TRADIC计算机，它用数千个晶体管和二极管取代了真空管。

---

## 87. 疑似信息窃取恶意软件导致数据泄露，暴露1.84亿登录名/密码

**原文标题**: Suspected InfoStealer Malware Data Breach Exposed 184M Logins/Passwords

**原文链接**: [https://www.websiteplanet.com/news/infostealer-breach-report/](https://www.websiteplanet.com/news/infostealer-breach-report/)

网络安全研究员 Jeremiah Fowler 发现了一个巨大的、未受保护的数据库，其中包含 1.84 亿个登录凭据，总计 47.42 GB 的原始数据。该数据库包括电子邮件提供商、Facebook、Instagram 和 Snapchat 等社交媒体平台，以及银行、医疗保健和政府门户网站等各种服务的用户名、密码和 URL。Fowler 立即通知了托管服务提供商，后者限制了公共访问。

数据的来源被怀疑是信息窃取恶意软件，它通过网络钓鱼邮件和恶意软件等方法从受感染的系统中收集敏感信息。被盗数据通常在暗网上出售，或用于欺诈和身份盗窃。

Fowler 通过联系名单上的人员并确认他们的密码准确来验证数据的真实性。他强调了此类漏洞相关的风险，包括凭据填充攻击、帐户接管、商业间谍活动和有针对性的网络钓鱼活动。

文章为用户提供了保护自己的建议，包括每年更改密码、使用独特而复杂的密码、启用双因素身份验证、检查已知漏洞、监控帐户，以及考虑使用密码管理器和防病毒软件。研究人员还强调了拥有或传播被盗个人数据的法律影响。Fowler 强调了他的道德研究实践，专注于识别漏洞并提高意识，以鼓励主动的安全措施。

---

## 88. Ada计算机语言竞赛（1979）概述

**原文标题**: Overview of the Ada Computer Language Competition (1979)

**原文链接**: [https://iment.com/maida/computer/redref/](https://iment.com/maida/computer/redref/)

无法访问文章链接。

---

## 89. Red编程语言

**原文标题**: Red Programming Language

**原文链接**: [https://www.red-lang.org/p/about.html](https://www.red-lang.org/p/about.html)

Red是一种受REBOL启发的新一代编程语言，旨在成为一种“全栈”语言，能够处理从底层系统编程到高级脚本编写的各种任务。其主要特性包括人性化的语法、同像性、多范式编程（函数式、命令式、反应式、符号式）、基于原型的对象支持、强大的模式匹配和宏系统。

它拥有丰富的内置数据类型、原生代码编译（静态和JIT）、以及能够生成小型（小于1MB）、无依赖可执行文件的交叉编译。Red支持并发、并行、内置的PEG解析器DSL、紧凑型垃圾回收器和一个跨平台的原生GUI系统。

Red的“全栈”特性不仅仅是技术实力；它提供了一个“语言构建集”，允许开发者使用通用语法，在适合任何任务的抽象级别上进行编码，从而实现可读性和高性能。目标是拥有一个单一的可执行工具链，该工具链可以从任何平台编译和打包代码到任何平台，而无需外部依赖。

该语言于2011年首次亮相，并在2013年进行了更新的展示。这些演示的幻灯片可供下载。该项目提供Visual Studio Code插件、高嵌入性、低内存占用和一个单文件工具链（尽管暂时分为两个二进制文件）。

---

## 90. 卷积、多项式与翻转核

**原文标题**: Convolutions, Polynomials and Flipped Kernels

**原文链接**: [https://eli.thegreenplace.net/2025/convolutions-polynomials-and-flipped-kernels/](https://eli.thegreenplace.net/2025/convolutions-polynomials-and-flipped-kernels/)

本文探讨了多项式乘法、卷积和与信号处理之间的联系。首先，通过基于表格的方法阐述多项式乘法，重点展示了如何从对角线导出系数。由此引出公式：S_k = ∑ P_i * R_{k-i}，其中S是P和R的乘积多项式。

随后，本文提出了一种多项式乘法的图形方法，其中一个多项式被“翻转”和移动，模拟了卷积过程。这种“翻转”是关键，因为它涉及到求和中指标相反的方向。

接下来，本文深入研究了离散信号和系统，并对其进行了数学定义。介绍了一个关键概念，即离散脉冲δ[n]，用于分解任何离散信号。文章强调了线性时不变（LTI）系统，并且可以通过它们对脉冲h[n]的响应来确定它们对任意信号的响应。

然后，本文介绍了卷积的核心概念：y[n] = x[n] * h[n] = ∑ x[k] * h[n-k]，其中y[n]是LTI系统的输出，x[n]是输入信号，h[n]是脉冲响应。文章展示了一个使用求和公式计算卷积的例子，强调了h[n]相对于x[n]的“翻转”特性。

最后，本文简要介绍了卷积的性质，强调了它的交换律以及卷积定理中所述的它在频域中的行为：F(f * g) = F(f) * F(g)。文章最后指出，该定理结合高效的算法（如FFT）可以实现非常高效的卷积实现。

---

## 91. 前所未见的“极端”微生物包围了NASA机器人

**原文标题**: Never-before-seen 'extreme' microbes surrounded NASA robot

**原文链接**: [https://www.livescience.com/space/space-exploration/never-before-seen-extreme-microbes-surrounded-nasa-robot-before-it-was-sent-to-mars-18-years-ago-new-study-reveals](https://www.livescience.com/space/space-exploration/never-before-seen-extreme-microbes-surrounded-nasa-robot-before-it-was-sent-to-mars-18-years-ago-new-study-reveals)

研究人员在用于存放NASA凤凰号火星探测器发射前使用的洁净室样本中，发现了26个新的“极端微生物”物种。通过重新分析旧样本发现，这些顽强的微生物拥有使其能够承受极端温度、压力、辐射甚至太空真空等恶劣条件的基因。

这项发表在《微生物组》杂志上的研究旨在了解极端微生物在太空任务中传播的风险，并确定哪些微生物可能在太空中生存。新发现的物种占洁净室中发现的所有物种的近四分之一，表明这些房间是寻找更多顽强微生物的理想场所。

发现新的极端微生物可以帮助研究人员预测潜在的外星微生物可能是什么样子，以及如何防止污染。这些微生物在医学、食品保鲜和生物技术方面也具有潜在的应用价值。这项研究强调了完全消毒洁净室的困难，以及微生物“搭便车”随航天器旅行的可能性，突出了理解和减轻行星际污染风险的重要性。

---

## 92. Show HN: 用 Janet 写的 Windows 上的平铺窗口管理器

**原文标题**: Show HN: A Tiling Window Manager for Windows, Written in Janet

**原文链接**: [https://agent-kilo.github.io/jwno/](https://agent-kilo.github.io/jwno/)

Jwno：一款用Janet编写的Windows 10/11磁贴窗口管理器。它旨在为Windows带来高度可定制的磁贴功能，并强调其灵活性。

Show HN帖子重点：

*   **功能性：** Jwno提供磁贴窗口管理，截图展示了Emacs、Sonic Pi和UI交互。
*   **自定义性：** 基于Janet构建，意味着具有显著的自定义潜力。
*   **文档：** 作者承认文档仍在开发中，但提供了关键章节的链接，例如功能、安装指南、交互式教程、手册和参考索引。
*   **资源：** 提供下载Jwno（包括Itch.io页面）、报告问题以及访问GitHub和Chisel上源代码的链接。
*   **目标受众：** 该帖子包含针对新用户和经验丰富的用户的部分。

---

## 93. 意外发现纳米结构材料可被动地从空气中收集水分

**原文标题**: Accidentally discovered nanostructured material passively harvest water from air

**原文链接**: [https://phys.org/news/2025-05-accidentally-class-nanostructured-materials-passively.html](https://phys.org/news/2025-05-accidentally-class-nanostructured-materials-passively.html)

宾夕法尼亚大学的研究人员意外发现了一种新型两亲性纳米多孔材料，能够被动地从空气中收集水分。这种材料已在《科学进展》杂志上发表，它将亲水（吸水）和疏水（拒水）成分结合在独特的纳米尺度结构中。这使得它能够从空气中捕获水分，在孔隙中冷凝，然后将其作为液滴释放到表面，而无需外部能量。

这个过程依赖于孔隙内的毛细管凝聚，但与其他类似材料不同，捕获的水不会被困住。相反，它会以稳定的液滴形式释放。研究人员发现，收集的水量随着材料厚度的增加而增加，这证明了液滴来源于材料内部，打破了关于蒸发速率的热力学预期。

该材料的特性归因于吸水纳米颗粒和疏水聚乙烯塑料之间精确的平衡，从而形成一个反馈回路，其中液滴与孔隙中的储水库相连，而这些储水库不断得到补充。这项发现具有在干旱地区用于水收集、冷却电子设备以及创造对湿度做出反应的智能涂层的潜力。

未来的研究将集中在优化材料的组成、扩大其在现实世界中的应用规模以及提高从表面去除液滴的效率上。该团队最终目标是开发出能够在干燥气候中提供清洁用水并利用环境水蒸气实现可持续冷却方法的技术。

---

## 94. 重构复杂代码库

**原文标题**: Refactor Complex Codebases

**原文链接**: [https://www.freecodecamp.org/news/how-to-refactor-complex-codebases/](https://www.freecodecamp.org/news/how-to-refactor-complex-codebases/)

Ankur Tyagi 的这篇文章探讨了重构复杂代码库这一关键但常被忽视的实践。它强调了技术债务如何积累，阻碍开发速度和可维护性，以及重构如何经常被低估，尽管它具有长期效益。

文章提倡一种结构化的重构方法，强调通过将重构工作与切实的业务成果（更快的上市时间、减少错误、新的收入来源）联系起来，以获得管理层的支持的重要性。它强调需要通过自动化测试（单元测试、集成测试和端到端测试）和 CI/CD 管道来建立一个强大的安全网，以确保变更不会引入回归。

文章讨论了重构的关键技术，包括使用团队知识、代码复杂性指标 (SonarQube)、变更频率分析和热点分析来识别和隔离代码中的“问题区域”。介绍了“接缝”概念，作为打破依赖关系和隔离代码以进行安全重构的一种方式。文章比较了增量重构（随着时间的推移进行小的、可管理的更改）和“大爆炸”重构（完全重写），通常倾向于前者，因为它的风险较低且功能持续可用。文章提到了向后兼容性的重要性，以及处理依赖关系和紧密耦合。还建议使用 AI 工具自动执行代码审查，以加快审查速度。最终，本文提供了一个实用的指南，将复杂、脆弱的代码转化为团队可以拥有和维护的干净、可靠的代码库。

---

## 95. 英伟达技术的曙光

**原文标题**: The Dawn of Nvidia's Technology

**原文链接**: [https://blog.dshr.org/2025/05/the-dawn-of-nvidias-technology.html](https://blog.dshr.org/2025/05/the-dawn-of-nvidias-technology.html)

英伟达技术黎明：早期创新与I/O架构

---

## 96. 维生素D补充剂显示出抵抗生物衰老的迹象

**原文标题**: Vitamin D Supplements Show Signs of Protection Against Biological Aging

**原文链接**: [https://www.massgeneralbrigham.org/en/about/newsroom/press-releases/vitamin-d-supplements-show-signs-of-protection-against-biological-aging](https://www.massgeneralbrigham.org/en/about/newsroom/press-releases/vitamin-d-supplements-show-signs-of-protection-against-biological-aging)

马萨诸塞州总医院布莱根医院2025年5月21日发布的新闻稿称，VITAL随机对照试验的一项子研究表明，补充维生素D可能有助于抵抗生物衰老。该研究发现，与安慰剂相比，服用维生素D3补充剂（2,000 IU/天）可在四年内显著减少端粒缩短。端粒是染色体上的保护帽，会随着年龄增长而缩短，并与年龄相关疾病有关。这种缩短的减少相当于阻止了近三年的衰老。

VITAL试验跟踪了美国50岁及以上的男性和55岁及以上的女性，为期五年。该子研究评估了1054名参与者在基线、第2年和第4年时白细胞中的端粒长度。虽然维生素D3显示出积极作用，但补充omega 3脂肪酸（1克/天）对端粒长度没有显著影响。

研究人员认为，补充维生素D可能是一种有前景的对抗生物衰老的策略，但还需要进一步研究。主要作者Haidong Zhu强调需要进一步调查。VITAL的首席研究员JoAnn Manson指出，之前的VITAL研究结果表明维生素D在减少炎症和衰老引起的慢性疾病方面有益处。该研究得到了美国国家心肺血液研究所的支持。

---

## 97. µPC：将预测编码扩展到百层网络

**原文标题**: µPC: Scaling Predictive Coding to 100 Layer Networks

**原文链接**: [https://arxiv.org/abs/2505.13124](https://arxiv.org/abs/2505.13124)

μPC：将预测编码扩展到100+层网络

本文题为“μPC：将预测编码扩展到100+层网络”，旨在解决训练极深预测编码网络（PCN）的难题，PCN是一种受大脑启发的、替代反向传播的方法。Innocenti等作者证明，标准PCN难以扩展到深度架构。他们提出了一种名为“μPC”的解决方案，该方案利用受现有工作启发的Depth-μP参数化，以稳定深度PCN的训练。

该论文强调，μPC能够可靠地训练具有100多层的PCN，特别是在简单分类任务上高达128层残差网络。与当前基准相比，该性能是在具有竞争力的结果和最少的超参数调整的情况下实现的。μPC的一个关键优势是它能够促进学习率在不同网络宽度和深度之间的零样本迁移。

作者识别并解决了阻碍标准深度PCN训练的一些病理。该研究表明，μPC方法对其他局部学习算法具有影响，并可能扩展到更复杂的架构，如卷积网络和transformers。μPC的代码已作为PCN的JAX库的一部分公开发布。该论文包括对缩放行为的广泛分析，为未来受大脑启发的算法的开发提供了宝贵的见解。

---

## 98. WiFi：“波束成形”仅仅是开始 (2014)

**原文标题**: WiFi: "beamforming" only begins to describe it (2014)

**原文链接**: [https://apenwarr.ca/log/20140801](https://apenwarr.ca/log/20140801)

本文深入探讨了如何通过天线方向性、波束成形和MIMO在WiFi中“作弊”香农定律。文章主要关注天线方向性和波束成形，解释了它们如何提高信噪比(SNR)，从而提高数据传输速度。

天线方向性，或“天线增益”，并非放大信号，而是通过聚焦特定区域来降低噪声。理想的天线是各向同性的，能从所有方向平等地接收信号。 实际天线具有方向性的“勺子”形状，最大圆形部分的尺寸决定了天线增益 (dBi)。 正确瞄准定向天线可以提高信噪比，但需要小心瞄准，这对于室内WiFi而言并不理想。 将路由器从天花板上悬挂下来，并使用向下指向的天线，对于家庭而言是一种实用的解决方案，可提供高达6dB的改进。

波束成形，虽然名称具有误导性，但它使用多个天线来创建“虚拟方向性”。它涉及调整来自多个天线的信号相位，以在特定区域产生相长干涉，从而提高这些区域中接收器的信号功率和信噪比。文章提到了在相长干涉和相消干涉过程中的能量守恒，并参考了费曼对光路的解释。 FCC限制了总发射功率，因此在使用多个天线时需要降低每个天线的功率。 然而，通过相位调整实现相长干涉，接收器可以从更高的信噪比中受益。 文章还讨论了“显式波束成形反馈”，即接收器提供有关相位差的信息，以及“隐式波束成形反馈”，即发射器通过监听来自远端信号来估计相位差。

---

## 99. OpenAI Codex 体验评测

**原文标题**: OpenAI Codex hands-on review

**原文链接**: [https://zackproser.com/blog/openai-codex-review](https://zackproser.com/blog/openai-codex-review)

本文对 OpenAI Codex 进行了实操评测，重点关注其功能和潜力。Codex 被描述为一种“聊天优先”的体验，用户可以将他们的 GitHub 仓库连接起来，并指示 AI 执行任务。作者强调了其多线程任务启动的吸引力，从而可以并行处理多个请求。

作者设想 Codex 支持未来的“无束缚工作流”，从而实现远程工作，并赞扬其基于聊天的后续跟进、自动创建拉取请求以及监控日志的能力。

然而，该评测也指出了需要改进的方面。较差的错误处理、有限的代码质量以及单次任务执行模式使得大型重构变得繁琐。无法轻松更新现有拉取请求以及执行沙箱中缺乏网络连接是重要的限制。作者发现 Codex 对小型维护任务和样式更改很有用，但对于复杂的开发，更喜欢传统的 IDE。

尽管存在这些限制，作者对 Codex 的潜力持乐观态度。改进一次性任务完成、更好的拉取请求管理以及与其他 OpenAI 功能的集成可能会带来显著的生产力提升。作者认为 Codex 将发展成为一个中心协调层，特别是用于管理繁琐的任务和规划一天的工作。

---

## 100. 适用于 Linux 的 Windows 子系统现已开源

**原文标题**: The Windows Subsystem for Linux is now open source

**原文链接**: [https://blogs.windows.com/windowsdeveloper/2025/05/19/the-windows-subsystem-for-linux-is-now-open-source/](https://blogs.windows.com/windowsdeveloper/2025/05/19/the-windows-subsystem-for-linux-is-now-open-source/)

微软在 Build 2025 大会上宣布，适用于 Linux 的 Windows 子系统 (WSL) 现已开源，可在 GitHub 的 Microsoft/WSL 上获取。 经过多年的努力，此举让开发者能够直接下载、构建、修复和贡献 WSL 的开发。

本文概述了 WSL 的架构，将代码分解为命令行可执行文件（wsl.exe、wslconfig.exe、wslg.exe）、WSL 服务 (wslservice.exe)、Linux init 和守护进程，以及用于文件共享的 Plan9 服务器实现。文章还提到了现有的开源组件，如 microsoft/wslg 和 microsoft/WSL2-Linux-Kernel。 一些组件，如 Lxcore.sys 和 P9rdr.sys，仍然保留在 Windows 镜像中。

本文重点介绍了 WSL 的发展历程，从 2016 年首次使用 pico 进程提供程序 (WSL 1) 到 WSL 2 的开发，后者利用了 Linux 内核。 2021 年 WSL 与 Windows 代码库的分离，使得可以通过 Microsoft Store 进行更快的开发和独立更新。 达到 WSL 2.0.0 版本带来了镜像网络和 DNS 隧道等功能。

微软强调了社区在 WSL 开发中发挥的重要作用，即使没有访问源代码。 他们希望开源发布能够进一步加速创新并满足用户需求。 鼓励开发者访问 Microsoft/WSL 仓库进行贡献。

---

