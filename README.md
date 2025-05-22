# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-05-22.md)

*最后自动更新时间: 2025-05-22 17:49:24*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 2 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 3 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 4 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 5 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 6 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 7 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 8 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 9 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 10 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 11 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 12 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 13 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 14 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 15 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 16 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 17 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 18 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 19 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 20 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 21 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 22 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 23 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 24 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 25 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 26 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 27 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 28 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 29 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 30 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 31 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 32 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 33 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 34 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 35 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 36 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 37 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 38 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 39 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 40 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 41 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 42 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 43 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 44 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 45 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 46 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 47 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 48 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 49 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 50 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 51 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 52 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 53 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 54 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 55 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 56 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 57 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 58 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 59 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 60 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 61 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 62 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 63 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 64 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
