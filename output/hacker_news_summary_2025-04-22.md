# Hacker News 热门文章摘要 (2025-04-22)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 机器针织的代数语义

**原文标题**: Algebraic Semantics for Machine Knitting

**原文链接**: [https://uwplse.org/2025/03/31/Algebraic-Knitting.html](https://uwplse.org/2025/03/31/Algebraic-Knitting.html)

本文探讨了为机器编织开发严谨的代数语义的挑战，类似于传统编程语言中使用的语义。作者认为，尽管机器编织代码看起来比传统代码更简单（没有分支、循环或函数），但编织的 3D 特性引入了复杂的性，例如线股的上下交叉，这会影响程序行为并阻止操作的简单交换。

作者通过确定两个机器编织操作是否可以交换的问题，阐述了对形式语义的需求，并将其与 C 和 Haskell 等编程语言中的类似问题进行比较。与这些语言中可交换性取决于数据依赖性和副作用不同，在机器编织中，即使没有数据依赖性，线股交叉也会引入拓扑约束，从而阻止操作交换。

该文章强调了现有的基于结理论的语义，但批评它们难以被计算机使用，因为它们依赖于连续变形。相反，作者提倡使用代数拓扑，特别是辫群，作为一种更易于计算机使用的方法来表示和分析机器编织的拓扑方面。

最后，这篇文章令人惊讶地将机器编织与拓扑量子计算联系起来，在拓扑量子计算中，粒子的上下交叉也很重要，这突出了拓扑考虑因素在看似不相关的领域中的潜在影响。

---

## 2. ClickHouse 变得更懒 (也更快了): 引入惰性物化

**原文标题**: ClickHouse gets lazier (and faster): Introducing lazy materialization

**原文链接**: [https://clickhouse.com/blog/clickhouse-gets-lazier-and-faster-introducing-lazy-materialization](https://clickhouse.com/blog/clickhouse-gets-lazier-and-faster-introducing-lazy-materialization)

本文介绍了“延迟物化”——ClickHouse 中的一项新优化技术，它能显著提高查询性能，尤其是在 Top N 查询中。“延迟物化”会在查询执行期间延迟读取列数据，直到绝对必要时才进行，并构建在 ClickHouse 现有的 I/O 优化堆栈之上。

ClickHouse 的 I/O 效率建立在以下基础上：
*   **列式存储：** 跳过不必要的列，并实现高压缩。
*   **稀疏主索引和二级数据跳过索引：** 在行块级别修剪不相关的数据。
*   **PREWHERE：** 甚至在非索引列上也能提前过滤数据。

“延迟物化”作为补充，通过将列读取推迟到查询计划需要时才执行。 只有下一个操作（例如，排序）所需的列才会被立即加载；其他列会被推迟，并且由于 `LIMIT` 子句，通常只读取部分内容。 这对于 Top N 查询尤其有效，因为只需要来自大型列的几行数据。

本文使用 Amazon 客户评论数据集演示了其影响。 一个选择前 3 个最有帮助的评论的查询，在启用延迟物化后，从 219 秒降至 139 毫秒（提速 1576 倍），而无需任何 SQL 更改。 然后，本文系统地分解了其他优化如何逐步发挥作用，直到“延迟物化”实现最终飞跃。 该示例还强调了较慢的磁盘 I/O 如何成为瓶颈，以及 ClickHouse 的优化如何最大限度地减少该瓶颈。

---

## 3. 多项式特征是万恶之源吗？(2024)

**原文标题**: Are polynomial features the root of all evil? (2024)

**原文链接**: [https://alexshtf.github.io/2024/01/21/Bernstein.html](https://alexshtf.github.io/2024/01/21/Bernstein.html)

本文挑战了人们普遍认为高阶多项式天生不适合机器学习的观点，认为其表现不佳通常是一种源于两个误解的迷思：多项式基的选择以及对魏尔斯特拉斯逼近定理的误解。

文章强调，标准多项式基不适合从数据中估计多项式，导致过拟合和对噪声的敏感。文章建议使用替代的多项式基，例如切比雪夫或勒让德多项式，可能会更好。然而，这些基经过优化用于插值，而不是拟合噪声数据。

文章提倡使用伯恩斯坦基，它具有易于正则化和控制的特性。该基使用二项式系数定义，可以解释为系数的加权平均值，确保它们与模型的标签处于相同的尺度。这使得L2正则化更有效。

作者通过实验证明了伯恩斯坦基的有效性，表明在高阶多项式中使用适当的正则化可以成功地拟合噪声数据。文章还强调了在使用多项式特征之前将数据归一化到区间的重要性，正如魏尔斯特拉斯逼近定理所暗示的那样。本质上，文章认为，使用正确的基和适当的正则化，高阶多项式可以成为机器学习中非常有价值的工具。

---

## 4. 使用 DuckDB-WASM 通过 SQL 绘制 3D 图形 (某种程度上)

**原文标题**: Abusing DuckDB-WASM by making SQL draw 3D graphics (Sort Of)

**原文链接**: [https://www.hey.earth/posts/duckdb-doom](https://www.hey.earth/posts/duckdb-doom)

本文详细介绍了一项实验，作者使用 DuckDB-WASM 构建了一个简陋的 3D 游戏引擎，具体来说是一个基于文本的 Doom 克隆，用于处理大部分核心逻辑。其核心思想是利用 SQL 查询来完成通常由 JavaScript 游戏循环和渲染管线处理的任务。

游戏状态，包括地图、玩家/敌人位置和游戏设置，都驻留在 DuckDB 表格中。玩家移动、子弹物理和碰撞检测都是使用 SQL UPDATE 和 DELETE 语句实现的。3D 渲染是通过一个复杂的 SQL VIEW 实现的，该 VIEW 使用递归 CTE 执行光线投射，计算墙壁距离并使用字符串聚合生成基于文本的 3D 场景。

JavaScript 的作用被简化为处理键盘输入、协调游戏循环，并使用 Z 缓冲区检查在 SQL 生成的背景之上渲染精灵（敌人/子弹）。作者遇到了一些挑战：DuckDB-WASM 初始化不正确、SQL 方言差异（AUTOINCREMENT 与 SEQUENCE）、查询规划器限制（表函数和子查询）、async/setInterval 竞争条件以及将精灵与 SQL 渲染的背景集成。解决方案包括遵循推荐的初始化模式、遵守 DuckDB 的 SQL 方言、重构查询以满足查询规划器、实施锁定以防止竞争条件，以及将 SQL 用于距离计算与 JavaScript 用于精灵渲染和 Z 缓冲区检查相结合。尽管采用了非常规的方法，该游戏仍然实现了可玩的 6-7 FPS，证明了 DuckDB-WASM 超出其预期用例的惊人能力。

---

## 5. 我本该也喜欢生物学的。

**原文标题**: I should have loved biology too

**原文链接**: [https://nehalslearnings.substack.com/p/i-should-have-loved-biology-too](https://nehalslearnings.substack.com/p/i-should-have-loved-biology-too)

无法访问文章链接。

---

## 6. 逻辑的惊喜 (2016)

**原文标题**: Surprises in Logic (2016)

**原文链接**: [https://math.ucr.edu/home/baez/surprises.html](https://math.ucr.edu/home/baez/surprises.html)

John Baez的“逻辑中的惊奇”探讨了数学系统内可证性的局限性，重点关注了蔡廷不完备性定理及其含义，以及通过突击测验悖论与哥德尔第二不完备性定理的联系。

蔡廷定理指出，存在一个复杂度界限*L*，使得我们无法证明任何特定比特串的柯尔莫哥洛夫复杂度（输出字符串的最短程序）大于*L*。 虽然我们可以证明存在无穷多个比任何给定数字都复杂的字符串，但我们无法确定一个并证明其复杂度超过*L*。 该文章阐述了看似复杂的创作，例如动画视频，可以被压缩成非常小的程序，然而可证明的复杂度却有一个令人惊讶的低上限。

该证明依赖于一个程序，该程序搜索声称字符串具有超过某个值的复杂度的证明。 如果找到了这样的证明，它将与该定理相矛盾，因为程序本身将比所声称的复杂度更短。

文章随后提到了Kritchman和Raz利用蔡廷定理对哥德尔第二不完备性定理提供了一种新的视角。 作者以突击测验悖论为例，论证了无法证明字符串的复杂度超过*L*会削弱我们证明数学自身一致性的能力。 本质上，如果数学可以证明其自身的一致性，那么在识别不可证明的复杂数字的能力方面就会出现矛盾。

---

## 7. Recover (YC W21) 正在招聘

**原文标题**: Recover (YC W21) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/recover/jobs/76dMle9-head-of-finance](https://www.ycombinator.com/companies/recover/jobs/76dMle9-head-of-finance)

Recover招聘财务主管

---

## 8. 展示 HN：Morphik – 开源 RAG，理解 PDF 图像，本地运行

**原文标题**: Show HN: Morphik – Open-source RAG that understands PDF images, runs locally

**原文链接**: [https://github.com/morphik-org/morphik-core](https://github.com/morphik-org/morphik-core)

Morphik：用于处理高技术和视觉文档的开源检索增强生成 (RAG) 替代方案。它允许开发者摄取、搜索、转换和管理非结构化和多模态数据，如图像、PDF 和视频。主要特性包括使用 ColPali 等技术的多模态搜索、知识图谱创建、快速元数据提取、与 Google Suite 和 Slack 等工具的集成，以及用于更快处理的缓存增强生成。

用户可以通过注册免费层级（采用基于使用量的定价）或自托管开源版本（提供有限支持）来开始使用。Morphik 提供 Python SDK 和 REST API 用于程序化访问，允许通过简单命令进行文件摄取和查询。基于 Web 的 Morphik 控制台提供了一个用户界面来与数据交互。此外，Morphik 还可以通过模型上下文协议 (MCP) 访问。

欢迎对开源项目做出贡献，包括错误报告、功能请求和拉取请求。重点是提高速度、扩展集成和识别有价值的研究论文。请注意，某些功能，如 Morphik 控制台，是付费版本专有的。

---

## 9. Supabase 完成 2 亿美元 D 轮融资，估值 20 亿美元

**原文标题**: Supabase raises $200M Series D at $2B valuation

**原文链接**: [https://finance.yahoo.com/news/exclusive-supabase-raises-200-million-112154867.html](https://finance.yahoo.com/news/exclusive-supabase-raises-200-million-112154867.html)

Supabase获Accel领投2亿美元D轮融资，估值达20亿美元。本轮融资还吸引了Coatue、Y Combinator、Craft Ventures、Felicis以及天使投资人Kevin Weil (OpenAI)、Guillermo Rauch (Vercel)和Taylor Otwell (Laravel)的参与。

Accel的投资凸显了数据库层在重大平台变革中日益增长的重要性，并将Supabase的潜力与Oracle和MongoDB相提并论。 Supabase目前被两百万开发者使用，管理着超过350万个数据库，并支持Postgres，是Google Firebase的替代方案。他们的目标是成为开发者全面的后端解决方案，包括“vibe coders”。

首席执行官Paul Copplestone是一位第三次创业的创始人，他强调远程优先的企业文化，在全球范围内聘用有才华的人，包括以前的创始人，基于能力和性格而非地理位置。该公司通过在100个城市举办发布周聚会等活动来促进联系。该公司的名字是故意致敬Nicki Minaj的歌曲“Super Bass”。

---

## 10. 戴维·佟理论物理讲义

**原文标题**: David Tong Lectures on Theoretical Physics

**原文链接**: [https://www.damtp.cam.ac.uk/user/tong/books.html](https://www.damtp.cam.ac.uk/user/tong/books.html)

大卫·唐的理论物理讲义已扩展成剑桥大学出版社出版的系列教材。虽然原始讲义免费，但书籍内容更加丰富，解释更清晰，拼写也更准确（例如，“Schwarzschild”）。 它们也比许多同类教科书更实惠。

目前已有四本教材出版。该系列受到了著名物理学家的高度赞扬，包括诺贝尔奖得主弗兰克·维尔泽克、丽莎·兰道尔、胡安·马尔达西那、内森·塞伯格、桑迪普·特里维迪、肖恩·卡罗尔和拉杰什·戈帕库玛。

这些专家强调了这些书的清晰度、引人入胜的写作风格、全面性以及传达对理论物理深刻理解的能力。 许多评论家将唐的系列与朗道和栗弗席兹的经典“理论物理教程”相提并论，表明它们可能成为学生和研究人员同样重要的现代资源。 这些书被描述为有价值的学习和教学工具，因其主题的统一性、幽默感以及重新点燃读者对物理的热情的方式而备受赞赏。

---

## 11. 让电脑杂志广告变得伟大的浣熊们

**原文标题**: The raccoons who made computer magazine ads great

**原文链接**: [https://technologizer.com/home/2025/04/22/pc-connection-ads-raccoons/](https://technologizer.com/home/2025/04/22/pc-connection-ads-raccoons/)

无法访问文章链接。

---

## 12. 加入 W3C 探索兴趣组：标准由此启程

**原文标题**: Join the W3C Exploration Interest Group: where standards start

**原文链接**: [https://www.w3.org/blog/2025/join-the-w3c-exploration-interest-group-where-standards-start/](https://www.w3.org/blog/2025/join-the-w3c-exploration-interest-group-where-standards-start/)

W3C探索兴趣组（IG）旨在成为网络身份、认证和信任的早期研发实验室。与工作组不同，IG不定义规范性标准。相反，它专注于将现实世界的观察与标准世界联系起来，旨在识别差距并提出更好的问题。

鉴于网络身份格局的演变，例如 Cookie 的衰落、联合登录的改变、浏览器 API 实验以及监管发展，IG与任何为网络构建、制定政策或努力实现互操作性的人员相关。该小组鼓励个人分享真实世界的经验，并强调当前标准可能无法充分解决的问题。

IG的探索涵盖了浏览器实现中的技术差距、新兴的钱包模型、跨行业的各种用例、同一问题的多种解决方案带来的碎片化风险以及需要技术响应的监管信号等领域。

该小组邀请通过其公共 GitHub 存储库进行贡献，鼓励任何人提出问题、提出想法和参与讨论。鼓励合作，如果个人的贡献变得经常性，欢迎加入该小组。会议每两周举行一次，重点讨论社区建议的主题。

---

## 13. Libro: 一个用于追踪书籍的命令行工具

**原文标题**: Libro: a command-line tool to track your books

**原文链接**: [https://github.com/mkaz/libro](https://github.com/mkaz/libro)

Libro 是一个用于跟踪阅读历史的命令行工具。它将数据存储在本地 SQLite 数据库中。主要功能包括添加新书 (`libro add`)、按年份 (`libro show --year`) 或 ID (`libro show <id>`) 显示已读书籍以及生成报告。报告可以显示按年份的阅读书籍（带有可视化条形图）（`libro report`）或按作者的阅读书籍 (`libro report --author`)。

该工具使用名为 `libro.db` 的 SQLite 数据库，其位置由 `--db` 标志、当前目录、环境变量 `LIBRO_DB` 或平台特定的数据目录确定。

Libro 可以使用命令 `libro import goodreads_library_export.csv` 从 Goodreads CSV 导出文件导入阅读历史。请注意，Goodreads 导出文件中不包含类型数据。

数据库模式包含两个表："Books" (id, title, author, pages, pub_year, genre) 和 "Reviews" (id, book_id, date_read, rating, review)。

Libro 在 PyPI 上打包为 `libro-book`，可以通过 `pip install libro-book` 安装。或者，在克隆 GitHub 存储库后，也可以在本地安装。

---

## 14. 使用物理模拟寻找十瓶保龄球的击球策略

**原文标题**: Using physics simulations to find targeting strategies in tenpin bowling

**原文链接**: [https://pubs.aip.org/aip/adv/article/15/4/045222/3344017/Using-physics-simulations-to-find-targeting](https://pubs.aip.org/aip/adv/article/15/4/045222/3344017/Using-physics-simulations-to-find-targeting)

利用物理模拟优化保龄球瞄准策略的文章摘要：

本文探讨了利用物理模拟优化保龄球瞄准策略的方法。该研究利用球-瓶相互作用、球道条件（油型、摩擦力）和球体特征（质量、半径、旋转）的计算模型来预测不同击球的结果。通过模拟大量具有不同释放角度、速度和旋转速度的保龄球尝试，研究人员旨在确定在不同条件下最大化全中率的最佳瞄准策略。

这些模拟可能包含运动方程、碰撞动力学（包括恢复系数）和摩擦模型，以准确表示保龄球运动中涉及的物理过程。该研究可能分析从这些模拟中生成的数据，以确定全中概率对各种输入参数的敏感性。

主要目标是为保龄球运动员和教练提供基于数据的有效瞄准策略见解。物理模拟提供了一种更系统且可能更有效的方法来发现成功的击球模式，而不是仅仅依赖于经验观察和反复试验。该研究还探讨了球道条件对最佳瞄准的影响，表明不同的油型可能需要不同的方法。此外，该研究可能会分析不同球体特征的影响，使保龄球运动员能够选择最适合其风格和球道条件的设备。最终目标是通过更深入地了解这项运动背后的物理原理来提高性能，并指导球道上的战略决策。

---

## 15. WebAssembly: 如何分配你的分配器

**原文标题**: WebAssembly: How to Allocate Your Allocator

**原文链接**: [https://nullprogram.com/blog/2025/04/19/](https://nullprogram.com/blog/2025/04/19/)

本文探讨了如何在 WebAssembly (WASM) 环境中处理内存分配，尤其是在缺乏传统操作系统内存管理功能的情况下。文章探讨了三种主要方法：导出静态堆、增长动态堆和导入动态堆。

**导出静态堆：** 指在编译时在 WASM 模块中保留一个固定大小的内存区域。虽然简单，但它受到不成熟的 WASM 工具链的阻碍（没有链接器脚本，不灵活的 WAT）。作者使用 C 数组来保留空间，但指出存在类型安全问题。导入内存时，编译器必须假设最坏的情况，即线性内存未初始化，导致所有清零的堆空间直接包含在 WASM 模块中，从而大大增加了文件大小。作者建议在使用 LLVM 工具链时避免导入内存。

**增长动态堆：** 这种方法利用 WASM 的 `memory.grow` 指令（通过未公开的 `__builtin_wasm_memory_grow` Clang 内置函数访问）在运行时请求额外的内存页（64KB 递增）。作者演示了如何使用此内置函数实现一个基本的 `sbrk` 函数。但是，他警告说，在浏览器中增长内存可能会将内存与引用分离，需要嵌入器在每次增长后重新获取内存句柄。

**导入动态堆：** 在这里，WASM 模块导入一个由嵌入器提供的动态大小的堆。该模块使用 `__heap_base`（链接器设置的绝对符号，标记数据结束位置）和 `__builtin_wasm_memory_size` Clang 内置函数来确定可用内存的边界。这适用于嵌入器控制内存分配的情况，但依赖于嵌入器提供足够的内存。

文章强调了每种方法的权衡，涵盖了技术细节和实际考虑因素，尤其是在编译时成本、内存管理以及 WASM 生态系统中的限制方面。

---

## 16. Pike – 一种语法类似于 Java 和 C 的动态编程语言

**原文标题**: Pike – a dynamic programming language with a syntax similar to Java and C

**原文链接**: [https://pike.lysator.liu.se/](https://pike.lysator.liu.se/)

Pike是一种动态编程语言，语法类似于Java和C，旨在易于学习、快速数据处理和快速执行。它采用GNU GPL、GNU LGPL和MPL许可证，可免费用于各种用途。近期新闻包括：林雪平的Pike聚会（2025年4月10日和2025年1月15日）公告、Pike 8.0 release 16 (build 8.0.1956)于2025年2月8日发布，以及2024年11月2日至3日在林雪平举行的Pike大会。Pike 9.0.9的测试版也可作为即将发布的稳定9.0系列的第二个测试版本使用。Pike网站是学习和下载该语言的官方资源。

---

## 17. Show HN: 我用 Ruby 构建了一个带 TTL 的 memoization 处理 gem

**原文标题**: Show HN: I built a Ruby gem that handles memoization with a ttl

**原文链接**: [https://github.com/mishalzaman/memo_ttl](https://github.com/mishalzaman/memo_ttl)

MemoTTL 是一个 Ruby Gem，它提供了具有生存时间 (TTL) 和最近最少使用 (LRU) 驱逐功能的线程安全备忘录化。 这允许开发人员缓存计算成本高昂的方法的结果，以指定的持续时间，通过避免冗余计算来提高性能。 LRU 驱逐策略确保缓存不会无限增长，通过在缓存达到其最大大小时删除最近最少访问的条目来管理内存使用。

可以使用 `include MemoTTL` 轻松将该 Gem 集成到 Ruby 类中。 然后可以使用 `memoize` 关键字对方法进行备忘录化，指定 TTL（以秒为单位）和最大缓存大小。 所提供的示例演示了它在简单计算器类中的用法，其中 `a_method_that_does_something` 方法被备忘录化，TTL 为 60 秒，最大缓存大小为 100。

该 Gem 还提供了用于清除特定备忘录化方法 (`clear_memoized_method`)、清除所有备忘录化方法 (`clear_all_memoized_methods`) 和触发清理操作 (`cleanup_memoized_methods`) 的方法。 一个 Rails 示例演示了如何在控制器中使用 MemoTTL，输出会突出显示实际执行了哪些方法调用，而不是从缓存中检索。 主要好处是通过利用缓存的结果来更快地执行，同时自动管理缓存大小和过期时间。

---

## 18. 1825年研究之极不完整一瞥

**原文标题**: An Utterly Incomplete Look at Research from 1825

**原文链接**: [http://bcmullins.github.io/research-from-1825/](http://bcmullins.github.io/research-from-1825/)

本文对1825年的研究和出版物进行了一项“极不完整”的调查，重点关注数学、经济学、哲学和国际关系。它突出了1820年代启蒙运动理想与保守反动之间的紧张关系。

讨论的关键著作包括塞缪尔·贝利的《论价值的性质、尺度和原因》，因其主观价值论而备受赞誉；以及让·安泰尔姆·布里亚-萨瓦兰的《厨房里的哲学家》，这是一部关于美食学和法国文化的论著。本文还提到了威廉·汤普森对女性社会地位的批判、托马斯·霍吉斯金对劳动的辩护，以及约翰·拉姆齐·麦克库洛赫颇具影响力的《政治经济学原理》。

该评论深入探讨了经济学，分析了贝利对劳动价值论的批判和雷文斯通对英国融资体系的批判。它还涉及麦克库洛赫的作品以及亨利·布鲁厄姆对技工学院和成人教育的倡导。

在哲学方面，本文探讨了赫兹里特的《时代精神》，这是一部收录了英国人物简介并批评他们放弃自由主义原则的文集。它还讨论了奥古斯特·孔德关于三阶段法则和科学等级的早期著作。

最后，该评论涉及詹姆斯·艾 Ivory 和本杰明·冈珀茨的数学研究，以及 J.C.L. de 西斯蒙第对国际关系的看法，将其描述为自由与暴政之间的斗争。总的来说，本文为了解1825年的知识界提供了一个窗口，其特点是对价值、教育和社会进步的辩论。

---

## 19. 谷歌将在Chrome浏览器中保留Cookie并跳过退出选项。

**原文标题**: Google will keep cookies and skip opt-out option in Chrome

**原文链接**: [https://privacysandbox.com/news/privacy-sandbox-next-steps/](https://privacysandbox.com/news/privacy-sandbox-next-steps/)

在隐私沙盒计划的最新进展中，谷歌宣布将维持目前Chrome浏览器中第三方 Cookie 的处理方式，*不会*推出新的独立提示框供用户选择退出。用户将继续通过 Chrome 的隐私和安全设置来管理他们的 Cookie 偏好。

这项决定是在与各方利益相关者（发布商、开发者、监管机构和广告行业）沟通后，并考虑到自2019年该计划启动以来，隐私增强技术的加速应用、人工智能驱动的安全措施的出现以及不断变化的全球法规而做出的。

谷歌将继续加强 Chrome 浏览器无痕模式下的跟踪保护，该模式默认阻止第三方 Cookie，包括在 2025 年第三季度推出 IP 保护功能。他们还将继续投资于 Chrome 的安全功能，例如安全浏览和人工智能驱动的保护措施。

该公告暗示了隐私沙盒 API 作用的潜在转变。谷歌计划收集行业反馈，并发布更新的路线图，概述这些技术未来的投资领域。该公司重申其致力于建立一个健康、保护隐私的网络生态系统。

---

## 20. 攻击我房东的锅炉

**原文标题**: Attacking My Landlord's Boiler

**原文链接**: [https://blog.videah.net/attacking-my-landlords-boiler/](https://blog.videah.net/attacking-my-landlords-boiler/)

本文详细介绍了作者如何在不干预房东的情况下，远程控制公寓锅炉的历程。由于对房东安装的温控器（单房间温度感应、不便及能源浪费）感到沮丧，作者寻求一种与Home Assistant自动化集成的DIY解决方案。

作者最初尝试逆向工程温控器和锅炉之间的无线电协议，但发现过于复杂。因此，他们选择了重放攻击，克隆和重播设备之间的信号。他们通过温控器的数据表识别出其868Mhz频率。

在最初使用经济型微控制器遇到困难后，作者购买了一个HackRF One克隆版（一种软件定义无线电），用于记录和重放温控器的“开”和“关”信号。将HackRF连接到他们的Home Assistant服务器后，他们创建了一个简单的Web服务器，通过命令行命令触发信号传输。

最后，利用Home Assistant的Average Sensor和Generic Thermostat插件，他们成功地基于多个房间的平均温度自动控制锅炉。

作者承认该解决方案有些“仓促”，可以通过适当的插件进行改进，但对它的功能以及它提供的节能效益感到满意。作者还谈到了使用开源硬件克隆产品的道德问题以及英国的《在线安全法案》，该法案导致博客评论区被删除。

---

## 21. 与实验鼠同居

**原文标题**: Living with Lab Mice

**原文链接**: [https://nautil.us/living-with-lab-mice-1202657/](https://nautil.us/living-with-lab-mice-1202657/)

与实验鼠同居
在《与实验鼠同居》一书中，哲学家艾娃·梅耶讲述了她领养25只退役实验鼠的经历，作为一项试点项目的一部分。由于缺乏对实验鼠社会生活和个体性格的研究，这些实验鼠主要被当作以人类为中心的研究工具来研究，梅耶对此感到沮丧，因此她试图从它们自身的角度去理解它们。

她详细描述了自己如何通过体貌特征来区分这些老鼠，然后通过它们的个体性格和行为来区分它们，观察它们的交流方式、梳理仪式和社交互动。梅耶目睹了许多关怀行为，例如安慰生病的同伴和哀悼死去的同伴，突显了它们复杂的社会动态。她挑战了人们普遍认为老鼠是简单、机械生物的看法，认为它们是具有丰富情感生活的、高度社会化的生物。

梅耶将自己的方法与科学研究的客观视角进行了对比，强调了长期观察和同情心在理解其他动物方面的重要性。她将此与科学家收集有用信息的观点进行了对比。

文章以梅耶与斯波基的关系达到高潮，斯波基是她最后一批老鼠中最后幸存的一只，她与斯波基建立了独特的联系，包括互相梳理毛发。通过她的经历，梅耶强调了所有动物的共同经历——社群、爱、关怀和死亡——并强调了认识到它们的个性和内在价值的重要性。最终，她倡导对老鼠和其他动物采取更富有同情心和尊重的理解。

---

## 22. Evertop：E-ink IBM XT兼容机，电池续航100+小时

**原文标题**: Evertop: E-ink IBM XT clone with 100+ hours of battery life

**原文链接**: [https://github.com/ericjenott/Evertop](https://github.com/ericjenott/Evertop)

Evertop是一款便携式IBM XT克隆机，专为超低功耗和延长电池续航时间而设计，旨在单次充电后使用数百甚至数千小时。它由ESP32微控制器驱动，配备5.83英寸电子墨水屏，可以运行DOS、Minix和高达3.0版本的Windows。它拥有众多内置外设，包括PS/2键盘/鼠标接口、CGA/Hercules/MCGA图形支持、多个音频输出、串口、USB闪存驱动器支持、以太网、WiFi和LoRA无线电。它还包含蓝牙功能，未来计划支持蓝牙键盘/鼠标、串口、IP、音频和文件传输。

该设备提供多种充电方式：可拆卸太阳能板、直流输入（2.5-20V）和micro USB。它可以在使用中同时从所有来源充电，并具有用于监控的电压表。太阳能板理论上每小时日照可提供10-50小时的使用时间。

存储通过SD卡处理，支持高达4GB的硬盘镜像，并允许配置多个模拟系统。外壳采用哑光PETG材料3D打印。文章还介绍了“Evertop Min”版本，这是一个更轻、更经济的版本，内置功能较少，但保留了基本功能，如电子墨水屏、PS/2接口、USB、WiFi和蓝牙。两个版本运行相同的固件。文章还包含一个视频和图片列表，展示了Evertop的功能和可用应用程序。

---

## 23. 强化学习能激励大型语言模型在基础模型之上进行推理吗？

**原文标题**: Does RL Incentivize Reasoning in LLMs Beyond the Base Model?

**原文链接**: [https://limit-of-rlvr.github.io/](https://limit-of-rlvr.github.io/)

杨岳正在研究如何更好地激励大型语言模型 (LLM) 和多模态大型语言模型 (MLLM) 中的推理能力。他的研究重点是为此开发新方法，以及探索通用世界模型和视觉-语言-动作 (VLA) 模型的泛化能力。他积极寻求与能够提供探索这些复杂且基础的研究领域所需的资源、技术环境和自由的公司合作。此外，他对博士访问机会感兴趣。他鼓励任何对合作研究这些主题感兴趣的人与他联系。本质上，他正在寻找合作伙伴关系和机会来推进其关于改进人工智能模型推理和泛化的研究。

---

## 24. 用于检测所有类型电离辐射的手持式探测器，提升辐射安全

**原文标题**: Handheld detector for all types of ionizing radiation improves radiation safety

**原文链接**: [https://phys.org/news/2025-04-handheld-detector-ionizing-safety.html](https://phys.org/news/2025-04-handheld-detector-ionizing-safety.html)

于韦斯屈莱大学和芬兰辐射与核安全局(STUK)联合开发的新型手持式多用途辐射探测器，可以探测所有类型的电离辐射（α、β、γ/X射线和中子）。这款辐射探测器的“瑞士军刀”提高了工业、医疗、监管、核能、急救人员和军事用户的安全性和态势感知能力。

该设备采用多层闪烁体技术，结合多种闪烁材料，在一个重量不到两公斤的紧凑单元中充当五个不同的探测器。它可以测量表面上的放射性污染，定向感知伽马射线发射材料（这种尺寸的探测器的新功能），并探测中子辐射以识别核材料。探测器的小尺寸减少了携带多个设备的需求。

于韦斯屈莱大学和STUK已将该技术申请了专利，并正在寻找商业合作伙伴进行商业化，计划开发更广泛的辐射探测仪器系列。未来的应用包括背包式系统、辐射门户监测以及集成到空中/地面车辆中。目前的原型机配有用于实时监控的集成屏幕，电池续航时间约为两小时。

---

## 25. 检测 C 语言中表达式是否为常量

**原文标题**: Detecting if an expression is constant in C

**原文链接**: [https://nrk.neocities.org/articles/c-constexpr-macro](https://nrk.neocities.org/articles/c-constexpr-macro)

本文探讨了多种C宏实现，用于验证表达式是否为编译时常量并返回其值，同时可以选择性地保留原始类型。作者提出了几种方法，每种方法都有其自身的优点和缺点以及与不同C标准的兼容性。

解决方案包括：

*   **静态复合字面量 (C23):** 使用静态存储持续时间和typeof来强制执行常量求值和类型保留，但需要现代C支持。
*   **`__builtin_constant_p` (GNU扩展):** 利用编译器内置函数来检查常量表达式，如果不是常量则触发编译错误，但依赖于GNU扩展。
*   **`static_assert` (C11+):** 在结构体中使用静态断言来验证常量性，但可能会改变表达式的类型。
*   **`sizeof` + 具有数组类型的复合字面量:** 利用复合字面量不允许变长数组的限制来强制执行常量表达式求值，但面临数组大小和类型支持的限制。
*   **`sizeof` + 枚举常量:** 利用枚举常量必须是整数常量表达式的要求，提供C89兼容性，但存在名称泄漏和警告的问题。
*   **逗号运算符:** 解决类型保留问题，但会生成关于未使用表达式的警告。

作者还讨论了GCC的一个怪癖，即负数组大小仅产生警告，因此采用了`error`属性来实现强大的错误处理。 最后，作者提到了来自u/P-p-H-d的C11解决方案，该方案使用`_Generic`，但指出其对整数类型的限制。 作者强调了避免警告的挑战，并寻求替代的、更优越的解决方案。

---

## 26. 我开源了我基于ESP32和OpenAI实时API的AI玩具公司

**原文标题**: I Open-Sourced My AI Toy Company That Runs on ESP32 and OpenAI Realtime API

**原文链接**: [https://github.com/akdeb/ElatoAI](https://github.com/akdeb/ElatoAI)

本文宣布开源 ElatoAI，这是一家利用 ESP32 微控制器和 OpenAI Realtime API 进行实时、全球 AI 语音对话的 AI 玩具公司。文章概述了硬件和软件设置、项目架构、功能、技术栈和高级数据流。

ElatoAI 允许用户创建具有鲜明个性和声音的自定义 AI 代理，然后这些代理可以通过基于 ESP32 的设备与用户交互。该系统使用 Next.js 前端、Deno 边缘函数（托管在 Deno/Supabase Edge 上）和 ESP32 Arduino 客户端进行通信。

主要功能包括实时语音到语音转换、可自定义的声音、安全的 WebSockets、服务器端语音活动检测、Opus 音频压缩和对话历史记录功能。技术栈包括 Next.js、Supabase DB、Deno Edge Functions、PlatformIO/Arduino (用于 ESP32) 和 Opus (用于音频)。

文章详细介绍了设置过程，包括安装 Supabase、配置 Next.js 前端和 Deno 服务器以及设置 ESP32 Arduino 客户端的说明。它还强调了重要的统计数据，例如延迟、音频质量和对话长度。文章指出了局限性，包括冷启动时间和对话长度限制。该项目欢迎贡献，提出了改进领域并概述了贡献过程。该项目采用 MIT 许可证。

---

## 27. 冷启动问题：利用网络效应扩展产品——评述

**原文标题**: The Cold Start Problem: Using Network Effects to Scale Your Product – A Review

**原文链接**: [https://madhavajay.com/the-cold-start-problem-using-network-effects-to-scale-your-product/](https://madhavajay.com/the-cold-start-problem-using-network-effects-to-scale-your-product/)

本文评述了陈安迪的著作《冷启动难题》，该书探讨了如何构建成功的网络效应产品。其核心悖论在于，庞大的网络必须从小型的“原子”网络起步：即能够产生自我维持价值的最小用户群体。关键在于专注于MVN（最小可行网络）。

该评述强调了“硬边”的概念，即创造不成比例价值的用户（例如，优步司机、爱彼迎房东）。吸引和留住他们至关重要。文章提供了一个表格，分析了优步、爱彼迎、Tinder、Reddit等公司，详细说明了它们的起步阶段、硬边、原子规模以及用于克服冷启动难题的策略。常见的策略包括“解决难题”、“始于工具，终于网络”以及利用“原子网络”。

文章随后将策略分为两个阶段：0-1（冷启动）和1-N（预热）。冷启动阶段侧重于通过上述策略实现最初的原子网络。预热阶段涉及规模扩张和防御竞争。该评述还列出了构建网络时常见的反模式（错误），并提供了书中建议的解决方案。

它强调了数据分析、理解用户摩擦点以及创造“神奇”用户体验的重要性。评述总结时强调，即使为一个人构建有用的东西（“单人游戏”）也可以发现网络价值，并且应该“追随用户价值的梯度”。最后，它简要地提到了如果你正在失去梯度应该怎么做，以及你应该检查竞争对手在做什么。

---

## 28. Verus：用于底层系统代码的已验证Rust

**原文标题**: Verus: Verified Rust for low-level systems code

**原文链接**: [https://github.com/secure-foundations/verus](https://github.com/secure-foundations/verus)

Verus：一款针对 Rust 代码的验证工具，使开发者能够正式证明其代码符合规范。Verus 利用强大的求解器进行静态验证，而不是运行时检查，从而确保代码在所有可能的执行中都符合规范。目前，Verus 支持 Rust 的一个子集，并提供超出标准 Rust 类型系统的功能，包括对操作原始指针的代码进行验证。

该项目正在积极开发中，不断改进和扩展。Verus 社区积极发表研究论文，并促进工业界和学术界的使用。学习和使用 Verus 的资源包括交互式演练场、安装说明、全面的文档（教程、API 参考和并发代码验证指南）以及自动格式化工具（`verusfmt`）。

用户可以通过已发布的项目、教程材料、独立示例和单元测试来找到 Verus 的实际应用示例。社区鼓励贡献，并提供相应的指南。Verus 使用 GitHub 进行问题跟踪和讨论，社区也可以在 Zulip 上获得实时支持和交流。Verus 采用 Creative Commons Attribution 4.0 International 许可协议。

---

## 29. 我们在150亿英里之外诊断并修复了2023年旅行者1号的异常 [视频]

**原文标题**: We Diagnosed and Fixed the 2023 Voyager 1 Anomaly from 15B Miles Away [video]

**原文链接**: [https://www.youtube.com/watch?v=YcUycQoz0zg](https://www.youtube.com/watch?v=YcUycQoz0zg)

文章概述了一个名为“我们诊断并修复了距离150亿英里的2023年旅行者1号异常”的YouTube视频。该视频可能详细介绍了旅行者1号探测器在2023年经历的异常的故障排除过程和最终解决方案。考虑到150亿英里的遥远距离，该视频很可能突出了远程诊断和解决如此老旧且遥远的探测器问题的挑战和复杂性。提供的内容包括典型的YouTube样板信息，例如版权声明、服务条款、隐私政策和广告链接。这表明文章本身内容很少，主要用作视频内容的广告或介绍。

---

## 30. 非凸动力下降制导的实时算法 [pdf]

**原文标题**: A Real-Time Algorithm for Non-Convex Powered Descent Guidance [pdf]

**原文链接**: [https://depts.washington.edu/uwrainlab/wordpress/wp-content/uploads/2020/01/AIAA_SciTech_2020.pdf](https://depts.washington.edu/uwrainlab/wordpress/wp-content/uploads/2020/01/AIAA_SciTech_2020.pdf)

此文档似乎是一个PDF文件，包含用于非凸动力下降制导的实时算法的源代码。标题“用于非凸动力下降制导的实时算法”清楚地表明了主题内容。

由于PDF格式，所提供的内容经过压缩和编码，未经进一步处理难以理解算法的具体细节。但是，标题和看似随机的字符/代码的存在表明该文档涉及算法的开发或实施。

从标题中可以推断出的关键方面是：

*   **实时性：** 该算法旨在高效运行并在严格的时间限制内产生结果，这对于制导系统至关重要。
*   **非凸性：** 这表明动力下降制导中涉及的优化问题具有非凸目标函数或约束。这是现实世界轨迹优化问题的常见特征，使其难以解决。
*   **动力下降制导：** 指的是使用发动机进行推进和制导来控制飞行器（例如，航天器或火箭）的下降。这通常需要优化推力剖面，以在满足各种约束的同时，在目标位置实现软着陆。

本质上，该文档可能提出了一种新颖的方法，用于实时解决动力下降制导这一具有挑战性的优化问题，特别是解决非凸性引入的复杂性。它可能详细介绍了算法方法，包括数学公式、潜在的近似值和实现细节。

---

## 31. 在任天堂Wii上托管的博客

**原文标题**: Blog hosted on a Nintendo Wii

**原文链接**: [https://blog.infected.systems/posts/2025-04-21-this-blog-is-hosted-on-a-nintendo-wii/](https://blog.infected.systems/posts/2025-04-21-this-blog-is-hosted-on-a-nintendo-wii/)

作者在一个运行NetBSD的任天堂Wii上托管博客的实验详情。受在非通用硬件上运行通用操作系统的想法启发，作者选择了Wii，因为它有主线NetBSD支持。

作者获得了一台Wii，并使用Wilbrand漏洞和自制频道安装了NetBSD。然后，他们配置了系统，使用NetBSD的软件包管理器（pkgin）安装了lighttpd Web服务器，并复制了其Hugo构建的静态博客文件。

作者最初因Wii有限的处理能力而苦苦挣扎，尤其是在提供加密内容时，不得不禁用诸如ntpd之类的服务以释放资源。最终，他们使用Caddy实施了反向代理来处理TLS终止并阻止已知的网络爬虫，从而减轻了Wii的处理和资源使用。

该博文详细介绍了设置Wii的过程，包括获取USB LAN适配器和设置静态网络配置。状态监控是通过一个简单的脚本实现的，该脚本将系统统计信息输出到HTML文件，因为使用更密集的脚本会使系统陷入困境。

作者总结说，虽然该设置存在一些缺点，例如需要重新启动整个控制台才能进行系统升级，但效果却出奇的好。Wii的功耗也相对较低。作者认为该实验是成功的，并打算继续运行它，也许会在此过程中学习更多有关NetBSD内核调优的知识。

---

## 32. Show HN: Dia，一个用于生成逼真对话的开放权重TTS模型

**原文标题**: Show HN: Dia, an open-weights TTS model for generating realistic dialogue

**原文链接**: [https://github.com/nari-labs/dia](https://github.com/nari-labs/dia)

南瑞实验室推出Dia：一款开放权重、16亿参数的文本转语音(TTS)模型，旨在生成具有情感和语气控制（包括非语言提示）的逼真对话。主要功能包括使用[S1]和[S2]标签生成对话、产生非语言提示以及通过提供音频提示实现语音克隆。

该项目在Hugging Face上提供预训练模型检查点和推理代码，目前仅支持英文生成。演示页面比较了Dia与ElevenLabs Studio和Sesame CSM-1B，并提供ZeroGPU Space供立即使用。

Dia可以通过pip安装，Gradio UI允许进行交互式实验。该模型需要GPU（CUDA 12.6）和大约10GB的VRAM，企业级GPU上的推理速度更快。未来的计划包括CPU支持、用于提高内存效率的量化和Docker支持。

该项目根据Apache 2.0许可协议进行许可，并提醒用户注意滥用，包括身份冒充、欺骗性内容生成和非法活动。南瑞实验室鼓励贡献，并感谢SoundStorm、Parakeet和Descript Audio Codec的启发，以及Google TPU Research Cloud和Hugging Face的支持。

---

## 33. 富士通与理研联合开发出世界领先的256量子位超导量子计算机

**原文标题**: Fujitsu and RIKEN develop world-leading 256-qubit sup quantum computer

**原文链接**: [https://www.fujitsu.com/global/about/resources/news/press-releases/2025/0422-01.html](https://www.fujitsu.com/global/about/resources/news/press-releases/2025/0422-01.html)

富士通与理研宣布开发出世界领先的256量子比特超导量子计算机，该计算机在理研RQC-富士通合作中心建造。这是对其先前64量子比特系统的重大进步，代表着迈向实用量子计算应用的关键一步。

这台新计算机采用了高密度实现技术，并将被集成到他们的混合量子计算平台中，该平台将于2025财年第一季度开始向全球公司和研究机构开放。扩大的量子比特数量使用户能够解决更复杂的问题，例如分析更大的分子和实现先进的纠错算法。富士通和理研的目标是通过实现量子计算机和经典计算机之间的无缝协作来提高平台可用性。

主要功能包括可扩展的3D连接结构，该结构可以有效扩展量子比特数量，并在稀释制冷机内实现四倍的实现密度。这种更高的密度是在不需要复杂重新设计的情况下实现的。

展望未来，富士通和理研致力于进一步的研发，目标是在2026年推出一台1000量子比特的计算机，该计算机将位于富士通科技园。他们还将把合作中心的工作期限延长至2029年3月，以继续长期研究。该项目获得了日本文部科学省通过量子飞跃旗舰计划（Q-LEAP）的支持。

---

## 34. 欢迎来到我们的1963年BBC MCR21 OB转播车网站

**原文标题**: Welcome to our website for the 1963 BBC MCR21 OB Van

**原文链接**: [https://mcr21.org.uk/](https://mcr21.org.uk/)

本网站致力于介绍1963年BBC MCR21 OB转播车，它是派伊公司的“主力扫描车队”之一，是广播历史上具有重要意义的作品。MCR21按照BBC的详细规格开发，展示了当时的多项先进技术，为未来的彩色广播铺平了道路。

该网站重点介绍了转播车的主要功能，包括其声音和视频控制系统。调音台有20个通道，分为3组，提供PA输出和广泛的监听功能。它描述了工程经理的办公桌，配备了15线手动电话交换机和混音器。在断电的情况下，混音器会恢复电池供电。监视器堆栈为每台摄像机配备了一个屏幕，并为工程、预览和传输配备了屏幕。它包括一个用于声音电平监控的光学PPM，以及一个能够接收405线和625线的双标准无线信号检测接收器。

视频工程师的控制台支持四台Pye Mk6摄像机，配备了专用的操作控制面板（OCP）和Tektronix示波器，用于监控和控制。

该网站强调了MCR21作为派伊为BBC生产的十辆单色OB转播车之一的作用，这些转播车被称为“主力扫描车队”，比之前的转播车先进得多。它们包含了许多新技术，为未来的彩色设备奠定了基础。

---

## 35. 网络工程师的人工智能：理解流、流簇和基于数据包的负载均衡

**原文标题**: AI for Network Engineers: Understanding Flow, Flowlet, and Packet-Based LB

**原文链接**: [https://nwktimes.blogspot.com/2025/04/ai-for-network-engineers-understanding.html](https://nwktimes.blogspot.com/2025/04/ai-for-network-engineers-understanding.html)

AI用于网络工程师：理解流、流簇和基于包的负载均衡
        
本文讨论了基于RoCEv2的AI后端网络中的负载均衡挑战，其中传统的基于流的3层ECMP可能因GPU间通信产生的“大象流”而导致拥塞。文章介绍了两种替代的负载均衡方法：基于流簇的自适应路由负载均衡和基于包的包喷射负载均衡。

基于流簇的路由根据实时拥塞监控动态重定向流量，从而缓解缓冲区积累和丢包。

包喷射将各个数据包分配到多个路径上，但它需要按顺序交付才能进行RDMA操作。本文解释了RDMA WRITE过程（首包、中间包、尾包）以说明这种依赖关系。为了克服这个问题，NVIDIA的RDMA网卡（ConnectX-5及更高版本）支持RDMA Write Only，它在每个数据包中都包含RDMA扩展传输头（RETH）。这实现了真正的基于每个数据包的负载均衡，均匀地分散流量，而无需担心数据包的顺序。

文章最后详细介绍了如何在Cisco Nexus 9000系列云规模交换机（NX-OS 10.5(1)F及更高版本）上使用动态负载均衡（DLB）配置基于每个数据包的负载均衡（包喷射）。提供的配置示例展示了如何在特定接口上启用DLB并定义DLB MAC地址。

---

## 36. 101个基础电脑游戏

**原文标题**: 101 BASIC Computer Games

**原文链接**: [https://github.com/maurymarkowitz/101-BASIC-Computer-Games](https://github.com/maurymarkowitz/101-BASIC-Computer-Games)

本文档介绍了一本1975年由David Ahl编写的书中的101个BASIC计算机游戏合集。与Ahl更为著名的《BASIC Computer Games》不同，本合集包含独特的游戏，并使用了各种BASIC方言，反映了当时编程风格的多样性。这些方言包括达特茅斯BASIC、BASIC-PLUS和EduSystem BASIC等。

本文档提供了一份游戏清单，包括游戏描述、书中页码以及估计使用的BASIC方言。游戏示例包括经典的二十一点、猜词游戏和井字游戏，以及一些不太常见的游戏，如Hurkle、Mugwump和Furs。这些游戏涵盖了各种类型，从策略和逻辑谜题到模拟和测验。

该合集是使用OCR和AI辅助准备的，并承认了原始材料的良好印刷质量。创建此数字合集的一个主要目标是为改进RetroBASIC解释器提供示例代码。本文档强调了该合集的独特之处，突出了20世纪70年代中期流行的各种BASIC方言和编程风格。

---

## 37. Prolog冒险游戏

**原文标题**: Prolog Adventure Game

**原文链接**: [https://github.com/stefanrodrigues2/Prolog-Adventure-game](https://github.com/stefanrodrigues2/Prolog-Adventure-game)

本文介绍了一款基于Prolog的冒险游戏，玩家的目标是在城堡内找到隐藏的宝藏。 该游戏结合了典型的冒险游戏机制，并使用逻辑编程语言Prolog。 玩家有三条命，必须在城堡中导航，面对诸如需要钥匙的锁着的门、必须被发现的隐藏物品以及需要找到零件才能完成的不完整物品等挑战。 该游戏还具有有限的资源，表明玩家需要仔细管理诸如生命值或物品之类的事物，以及库存管理，意味着玩家可以收集和使用他们在探索过程中找到的物品来解决难题和克服障碍。 本质上，该游戏是一个典型的基于文本的冒险游戏，依靠Prolog的规则和事实来定义游戏的世界、机制和逻辑，允许玩家通过Prolog查询与游戏交互。 核心玩法围绕着探索、解决与隐藏物品和锁着的门相关的谜题、管理资源以及在城堡的危险中生存，最终发现宝藏。

---

## 38. 围棋中的死里逃生

**原文标题**: Cheating the Reaper in Go

**原文链接**: [https://mcyoung.xyz/2025/04/21/go-arenas/](https://mcyoung.xyz/2025/04/21/go-arenas/)

本文探讨了 Go 语言中的手动内存管理，通过构建一个非类型化的、具有垃圾回收功能的 Arena 抽象来实现。作者是一位对 Go 设计选择着迷的 C++ 程序员，他认为尽管存在垃圾回收机制，但 Go 语言有限的未定义行为和简单的 GC 语义使得这种手动内存管理成为可能。

本文详细介绍了 `Allocator` 接口和 `Arena` 结构的设计和实现，它们允许在特定生命周期内进行高效的内存分配。文章强调了一个关键挑战：Go 垃圾回收器需要指针形状信息（指针位）才能正确识别和管理已分配内存中的指针。Arena 的原始实现无法安全地处理指针，因为 GC 不会识别 Arena 内存中的指针，导致过早释放。

文章提出了一种解决方案，即持有从 Arena 分配的任何指针都可以防止整个 Arena 被垃圾回收。这使得 Arena 可以安全地包含指针，因为 Arena 中指向的任何内容都将被保持存活。基准测试将 Arena 分配器与 Go 的内置 `new` 函数进行比较，显示出显著的性能提升，尤其是在较大的内存分配方面。本文深入探讨了 Go 语言的 GC 实现，强调了为什么在像 Go 这样“不安全”的语言中进行内存管理是安全的。

---

## 39. 数据压缩专家讨厌的这个小技巧 [视频]

**原文标题**: Data Compression Nerds Hate This One Trick [video]

**原文链接**: [https://media.ccc.de/v/eh22-8-more-than-just-quite-ok-data-compression-nerds-hate-this-one-trick](https://media.ccc.de/v/eh22-8-more-than-just-quite-ok-data-compression-nerds-hate-this-one-trick)

这个Easterhegg 2025讲座“不仅仅是还行 – 数据压缩迷们讨厌这个小技巧”探讨了Quite Okay Image Format (QOI) 作为无损图像压缩领域中 PNG 格式的令人惊讶的竞争者的出现。 演讲者讨论了 QOI 这种低复杂度的替代方案如何在 PNG 经过数十年的开发和改进后仍能取得令人印象深刻的成果。

讲座深入研究了数据压缩的世界，比较了 PNG、JPEG 和 QOI。它强调了一个违反直觉的观点，即更复杂的压缩算法并不总是等同于更好的性能。演讲者解释了 QOI 如何提供数据压缩的不同视角，并可能因其简单性而在特定用例中提供优势。

本次演讲承诺内容丰富，包含“多汁的数据压缩知识”，包括对相关压缩方法的基本概念和数学基础的解释。 讲座录音包含多种语言（英语和德语）的音轨，为更广泛的受众提供了可访问性。 可下载的视频和音频文件提供多种分辨率和格式。 演讲者将 QOI 的成功归功于一个人长达一年的努力，从而引发了人们对所使用的特定技巧或方法的兴趣。

---

## 40. 天文学家证实存在孤立黑洞

**原文标题**: Astronomers confirm the existence of a lone black hole

**原文链接**: [https://phys.org/news/2025-04-astronomers-lone-black-hole.html](https://phys.org/news/2025-04-astronomers-lone-black-hole.html)

天文学家已确认一颗孤立黑洞的存在，它是一颗没有伴星的天体，这一壮举是通过研究引力微透镜效应实现的。空间望远镜科学研究所的一个团队，利用哈勃和盖亚的数据，分析了一个先前被认为是潜在黑洞的物体。在2011-2017年的初步观测之后，又进行了2021-2022年的数据跟进。

该物体OGLE-2011-BLG-0462被探测到是因为它从一颗遥远的恒星前面经过，放大了它的光线并稍微改变了其视位置。数据分析显示，该物体的质量约为太阳的七倍，排除了其为中子星的可能性。这项发现标志着首次确认观测到一颗没有伴星的黑洞。

以前，黑洞主要通过它们与伴星发出的光的相互作用来识别。这种方法对于孤立存在的黑洞来说是不可能的。

第二个研究团队最初对黑洞的分类提出异议，认为它是一颗中子星。他们后来修改了评估，同意黑洞的识别，并估计质量约为六个太阳质量。天文学家计划使用即将于2027年发射的南希·格雷斯·罗曼太空望远镜来寻找更多的孤立黑洞。该研究发表在《天体物理学杂志》上。

---

## 41. LLM驱动的工具是增强而非取代开发者能力

**原文标题**: LLM-powered tools amplify developer capabilities rather than replacing them

**原文链接**: [https://matthewsinclair.com/blog/0178-why-llm-powered-programming-is-more-mech-suit-than-artificial-human](https://matthewsinclair.com/blog/0178-why-llm-powered-programming-is-more-mech-suit-than-artificial-human)

马修·辛克莱认为，像Claude Code这样由LLM驱动的编程工具更像是开发者的“机甲战衣”，而非替代品。他使用Claude Code构建了两个应用程序，生成了3万行代码，并了解到这些工具可以放大现有技能。虽然AI可以快速生成代码，但开发者在架构决策、质量控制和防范错误方面仍然至关重要。

作者强调，即使有了AI的辅助，理解业务问题和设计解决方案仍然是开发速度的主要制约因素。他还强调了愿意放弃非最佳AI生成代码的重要性，这是许多开发者需要培养的技能。

辛克莱警告说，没有经验的开发者可能难以识别AI生成的无稽之谈，并且这些工具会放大错误。他将这种情况比作“人马象棋”，即人与AI的团队表现优于单独的人或单独的AI系统。

关键在于找到委托给AI和保持控制之间的适当平衡。作者总结说，LLM将改变开发者的工作方式，使架构思维、模式识别和技术判断比原始编码能力更有价值。未来属于那些掌握这些工具并了解其局限性的人，他们拥抱这些工具以空前的规模和速度构建软件。

---

## 42. 图Transformer简介

**原文标题**: Introduction to Graph Transformers

**原文链接**: [https://kumo.ai/research/introduction-to-graph-transformers/](https://kumo.ai/research/introduction-to-graph-transformers/)

本文介绍了图Transformer，一种新型的图数据学习模型，它克服了图神经网络（GNN）的局限性。GNN擅长通过消息传递捕捉局部邻域模式，但难以处理远距离关系。图Transformer受到传统Transformer的启发，使用自注意力机制，使每个节点可以直接关注图中任何位置的信息，从而捕捉更丰富的关系和微妙的模式。

文章解释了Transformer如何利用其注意力机制和并行处理来应对关系重要的数据中的挑战。它详细介绍了自注意力的关键步骤：线性投影（Query、Key、Value）、缩放点积注意力、多头注意力以及带有残差连接的前馈。

图Transformer将这种核心注意力机制应用于图结构数据，无需逐步消息传递即可捕捉局部结构和全局上下文。它们与传统Transformer的不同之处在于，它们结合了图拓扑结构，使用位置编码来捕捉结构关系，并显式地建模边特征。与GNN相比，图Transformer在信息流和远距离依赖关系捕捉方面具有优势，避免了深度GNN中出现的过度平滑问题。它们还提供更高的计算效率，尤其是在捕捉远距离关系方面。文章重点介绍了其在蛋白质折叠、欺诈检测、社交网络推荐和知识图谱推理等领域的应用。

---

## 43. Bluesky 的一种新型验证方式

**原文标题**: A new form of verification on Bluesky

**原文链接**: [https://bsky.social/about/blog/04-21-2025-verification](https://bsky.social/about/blog/04-21-2025-verification)

Bluesky 推出新的验证系统以提高平台信任度。该系统在真实和知名账户的名称旁边添加一个可视的“蓝色对勾”，作为现有域名句柄验证方法的补充。

除了 Bluesky 自己的验证之外，该平台还启用了“可信验证者”，即可以直接向账户颁发蓝色对勾的独立组织。这些组织由扇形蓝色对勾标识。例如，《纽约时报》可以验证其记者。Bluesky 会审查这些验证，以确保其真实性。用户可以通过点击蓝色对勾来查看哪个组织验证了账户。

用户可以选择在应用程序设置中完全隐藏验证指示器。

目前，Bluesky 不接受直接申请蓝色对勾验证。鼓励用户通过将其域名设置为用户名来进行验证。一旦该功能稳定，Bluesky 计划推出一个申请表格，供有兴趣获得验证或成为可信验证者的知名账户和组织使用。

---

## 44. 人工智能辅助的基于搜索的研究工作

**原文标题**: AI assisted search-based research works now

**原文链接**: [https://simonwillison.net/2025/Apr/21/ai-assisted-search/](https://simonwillison.net/2025/Apr/21/ai-assisted-search/)

本文探讨了人工智能辅助的基于搜索的研究工具的重大进展，尤其是在2025年上半年。作者指出，早期的版本，如2023年的Perplexity和早期Bing，容易产生幻觉和不可靠的信息。然而，最近的迭代，特别是来自Google Gemini、OpenAI和Perplexity的深度研究实现，已经变得真正有用。

作者强调了OpenAI的o3和o4-mini模型在ChatGPT中的影响，这些模型可以将搜索作为其思维链推理的一部分来运行，从而产生更准确和可靠的答案。这与早期难以过滤网络垃圾邮件和欺骗性内容的系统形成对比。作者提供了这些模型成功处理的查询示例，包括技术规格、查找在线工具，甚至将代码移植到新的库版本。

作者指出，谷歌和Anthropic需要改进，谷歌的Gemini应用程序缺乏透明度，谷歌搜索仍然会产生幻觉。Claude也被认为落后。作者认为这些进步对网络的经济模式具有深远的影响，因为用户可能会越来越依赖聊天机器人获取信息，从而减少网站流量。作者预计会出现法律挑战以及在线访问信息方式的转变。

---

## 45. Bethesda宣布重制版《上古卷轴IV：湮没》

**原文标题**: Bethesda announces remastered version of The Elder Scrolls IV: Oblivion

**原文链接**: [https://www.youtube.com/watch?v=Ed_E2crglcw](https://www.youtube.com/watch?v=Ed_E2crglcw)

贝塞斯达公布《上古卷轴IV：湮灭》重制版的消息。主要信息来源似乎是一段YouTube视频，但提供的文本内容很少，主要由标准的YouTube法律声明和操作信息组成。

---

## 46. M.2 HDMI采集卡

**原文标题**: A M.2 HDMI capture card

**原文链接**: [https://interfacinglinux.com/2025/04/18/magewell-eco-m-2-hdmi-capture-card/](https://interfacinglinux.com/2025/04/18/magewell-eco-m-2-hdmi-capture-card/)

本文评测了美乐威 Eco Capture Dual HDMI M.2 采集卡，该采集卡采用 M.2 接口而非传统的 PCIe 接口。作者强调了该卡在现代系统中更具吸引力，因为 M.2 接口正逐渐取代 PCIe 接口。

评测涵盖了开箱体验，提到了随附的 SHD 转 HDMI 线缆，以及需要单独购买安装硬件。文章详细介绍了 x86（Debian、Fedora）和 ARM（NVIDIA Jetson TX1/2、Rockchip 3588 SOC with Armbian）平台的驱动安装，包括具体命令和依赖项。

该采集卡在 OBS 和 WebRTC 应用（Discord、Jitsi、Zoom）中的表现良好，像标准的 V4L2 设备一样工作，并成功采集了两路 1080p 60 帧的视频流。与 Decklink Mini 4K Recorder 等其他采集卡的图像质量比较表明，其质量和延迟相似，而美乐威的 M.2 外形是一个关键优势。

作者总结说，该卡性能良好，但价格昂贵，为 385 美元，使其适合特定的专业应用场景。文章提到在 eBay 上寻找打折产品是一个可行的选择。评测包括对安装性、性能、外观和价格的评分，以及优缺点，突出了 2 年保修、24/7 运行和 M.2 外形，同时也提到了缺乏安装支架和价格偏高等缺点。

---

## 47. “长期主义”与“生存风险”的危险理念

**原文标题**: The Dangerous Ideas of "Longtermism" and "Existential Risk"

**原文链接**: [https://www.currentaffairs.org/news/2021/07/the-dangerous-ideas-of-longtermism-and-existential-risk](https://www.currentaffairs.org/news/2021/07/the-dangerous-ideas-of-longtermism-and-existential-risk)

埃米尔·P·托雷斯批判“长期主义”，一种在有效利他主义运动中流行的道德哲学，认为它是一种危险的意识形态，会为了人类假想的未来而牺牲当下的苦难。长期主义源于尼克·博斯特罗姆的著作，它认为最重要的目标是确保“源于地球的智能生命”通过殖民太空和创造模拟现实来发挥其“潜力”，从而最大化有意识生命的数量。

托雷斯认为，这种观点导致人们对气候变化和全球贫困等当今危机不屑一顾，因为与如果发生“生存风险”而可能造成的未来价值损失相比，这些危机显得微不足道。长期主义者优先降低这些风险，即使只是微小的幅度，而不是解决眼前的需求，实际上是将假想的未来生命置于实际活着的人之上。

作者批判了长期主义中固有的数字计算，强调了一些例子，在这些例子中，拯救数十亿现在的生命被认为不如无限小地增加庞大未来人口的可能性重要。托雷斯强调，这种哲学允许从现有体系中不成比例地受益的富有精英们，通过关注抽象的、长远的目标，在道德上为他们对紧迫的全球问题的不作为辩护。文章总结说，长期主义类似于一种世俗宗教，通过免除精英们解决眼前问题的责任并确认他们对生存威胁的关注，从而对他们产生吸引力。

---

## 48. 来访

**原文标题**: Visiting Us

**原文链接**: [https://www.epic.com/visiting/](https://www.epic.com/visiting/)

Epic公司位于威斯康星州维罗纳的星际总部欢迎已注册的访客在工作日和周末的特定时间进行自助游。这些游览大约持续一小时，游客可以探索六个独特的园区：草原园、中央公园园、农场园、学习园、巫师学院园和故事书园。游览包括步行，并可能使用“奶牛自行车”、“奶牛车”或“奶牛厢型车”在园区之间穿梭。

必须提前预订，可通过在线或电话方式进行。旅游团规模有限。抵达后，游客应将车停在访客停车场并按照指示牌行驶。园区内有各种景点，包括谷仓、艾拉旋转木马、深空、翡翠城、巫师学院和树屋。该公司还展示了其从当地艺术博览会上挑选的独特艺术收藏品。

Epic公司强调其园区的设计旨在提高工作效率，并重点介绍了其采用当地食材的美食场所。他们甚至在网上提供其厨师的食谱。文章还鼓励游客探索威斯康星州麦迪逊周边的地区，重点介绍了当地的文化活动、户外活动和餐饮选择。

该地点在特定日期因特殊活动而关闭参观。有关职业、社区参与、法律方面和其他主题的信息可通过提供的链接获取。

---

## 49. 用于空间干涉测量的超精密编队飞行演示

**原文标题**: Ultra-precision formation flying demonstration for space-based interferometry

**原文链接**: [https://arxiv.org/abs/2504.05001](https://arxiv.org/abs/2504.05001)

本文介绍了SILVIA（空间干涉仪实验室创新应用探索），一项旨在验证空间超精密编队飞行的任务提案。其主要目标是实现三颗相距100米的航天器之间亚微米级的相对距离控制精度。这将通过集成先进技术来实现，包括航天器传感器、用于精确距离测量的激光干涉测量技术，以及用于实时控制距离和相对方向的低推力、低噪声微推进技术。

拟议的任务将在近圆形低地球轨道运行，为测试这些技术提供经济高效且相对安全的环境。100米的尺度平衡了较小的相对扰动和较低的碰撞风险。

SILVIA旨在弥合未来雄心勃勃的太空任务（如DECIGO（用于探测原初引力波）和LIFE（用于直接成像系外行星））的技术差距。这些未来的任务需要极其精确的编队飞行才能实现各自的科学目标。通过在更易于管理的 Setting 中展示必要的技术，SILVIA 将为下一代高精度空间天文台铺平道路。本文概述了任务概念，并重点介绍了其成功所需的关键技术。

---

## 50. Show HN: Open Codex – 具有开源LLM的OpenAI Codex CLI

**原文标题**: Show HN: Open Codex – OpenAI Codex CLI with open-source LLMs

**原文链接**: [https://github.com/codingmoh/open-codex](https://github.com/codingmoh/open-codex)

Open Codex：一款开源的本地命令行AI助手，灵感源自 OpenAI Codex，可将自然语言翻译成 shell 命令。与 OpenAI Codex 不同，它完全在本地运行，利用 phi-4-mini 等开源语言模型，无需 API 密钥和外部服务器。

该工具支持一次性命令生成，用户可以输入纯英文指令，收到建议的 shell 命令，然后选择执行、复制到剪贴板或中止。由于其基于 Python 的实现，它可在 macOS、Linux 和 Windows 上运行，并在终端中提供彩色编码输出，以提高可读性。

安装简单明了，包括 Homebrew（推荐用于 macOS）、pipx（跨平台）以及通过 Git 进行本地克隆等选项。该项目具有雄心勃勃的未来计划，包括交互式、上下文感知模式、TUI、支持更多开源模型、函数调用、通过 Whisper 进行语音输入、命令历史记录、撤消功能以及插件系统。

重点放在安全性上，因为所有模型都在本地运行，并且命令在执行前需要明确批准。欢迎贡献，该项目采用 MIT 许可证。

---

## 51. CaMeL：从设计上防御提示注入

**原文标题**: CaMeL: Defeating Prompt Injections by Design

**原文链接**: [https://arxiv.org/abs/2503.18813](https://arxiv.org/abs/2503.18813)

该arXiv文章 (arXiv:2503.18813) 介绍了CaMeL，一种新型防御机制，旨在缓解大型语言模型(LLM)代理中的提示注入攻击。 提示注入攻击利用了LLM在与来自外部环境的不可信数据交互时的漏洞，可能劫持LLM的预期功能。

CaMeL作为LLM周围的一层保护层运行。 它通过显式地从可信查询中提取控制流和数据流来实现鲁棒性。 这种隔离确保了LLM检索到的任何不可信数据都不能改变程序的流程，从而防止恶意注入控制程序。

CaMeL的安全性通过管理数据流的“能力”系统得到进一步增强。 这可以防止未经授权泄露私人数据，从而增加了一层额外的保护。

该论文通过展示CaMeL在AgentDojo基准测试上的表现来证明其有效性。 CaMeL成功完成了67%的任务，并具有可证明的安全性，表明代理安全性在对抗提示注入攻击方面有了显著提高。 作者是Edoardo Debenedetti和其他九位研究人员。

---

## 52. 计算的未来：英伟达的王冠正在滑落

**原文标题**: The Future of Compute: Nvidia's Crown Is Slipping

**原文链接**: [https://mohitdagarwal.substack.com/p/from-dominance-to-dilemma-nvidia](https://mohitdagarwal.substack.com/p/from-dominance-to-dilemma-nvidia)

无法访问文章链接。

---

## 53. LHC 2025 首次对撞

**原文标题**: LHC 2025 First Collisions

**原文链接**: [https://op-webtools.web.cern.ch/vistar/](https://op-webtools.web.cern.ch/vistar/)

无法访问文章链接。

---

## 54. 帕金森病iPS细胞来源多巴胺能细胞的I/II期临床试验

**原文标题**: Phase I/II trial of iPS-cell-derived dopaminergic cells for Parkinson's disease

**原文链接**: [https://www.nature.com/articles/s41586-025-08700-0](https://www.nature.com/articles/s41586-025-08700-0)

这项I/II期临床试验旨在研究将诱导多能干细胞(iPS)来源的多巴胺能祖细胞移植到帕金森病(PD)患者大脑中的安全性和有效性。七名患者接受了双侧移植，安全性为主要终点，运动症状改变和多巴胺产生为次要终点，监测期为24个月。

试验表明，移植的细胞存活，产生多巴胺，并且没有形成肿瘤，表明安全性和潜在的临床益处。没有发生严重不良事件，但报告了73起轻度至中度事件。MRI扫描显示没有移植物过度生长。

对六名患者的疗效评估显示，四名患者在停药期间的运动功能（MDS-UPDRS第三部分）有所改善，五名患者在服药状态下有所改善。四名患者的Hoehn-Yahr分期有所改善。重要的是，示踪多巴胺产生的氟-18-左旋多巴（18F-DOPA）摄取速率常数（Ki）值在壳核中增加了44.7%，且高剂量组的增加幅度更大。患者的抗帕金森病药物剂量保持稳定，导致一些运动障碍增加。该试验表明，异基因iPS细胞来源的多巴胺能祖细胞是帕金森病的一种有前景的治疗方法。

---

## 55. Pahole 更新

**原文标题**: An Update on Pahole

**原文链接**: [https://lwn.net/Articles/1016243/](https://lwn.net/Articles/1016243/)

LWN.net 文章：pahole 工具更新——用于 BPF 的内核开发调试信息工具

要点：

*   **新增共同维护者：** Alan Maguire 加入 Arnaldo Carvalho de Melo 成为共同维护者。
*   **发布节奏与持续集成：** Melo 计划加快 pahole 的发布节奏，使其与内核保持一致，并建立持续集成 (CI) 测试。
*   **近期进展：** 该项目已取得显著进展，大约有 140 个补丁。
*   **功能更新：** 包括对灵活数组的支持，改进的 BTF 处理以及有限的 Rust 支持（主要忽略 Rust 调试信息）。现在它可以转换全局变量信息（默认关闭）。
*   **BTF 调整：** Pahole 现在可以解析 BTF 并用于修改它，以进行重复数据删除和编译器错误修复。
*   **未来计划：** 长期目标是让 GCC 在编译期间直接生成 BTF 调试信息，从而消除 pahole 从 DWARF 转换的需要，这将大大加快内核构建速度。这依赖于 binutils 处理 BTF 链接。使用 `-gbtf` 进行编译已经可行，预计很快就会支持链接。

即使编译器原生生成 BTF，pahole 仍然会是构建过程的一部分，因为它会应用其他修复程序。

---

## 56. Show HN: 我构建了一个AI，可以将GitHub代码库转化为简易教程

**原文标题**: Show HN: I built an AI that turns GitHub codebases into easy tutorials

**原文链接**: [https://github.com/The-Pocket/Tutorial-Codebase-Knowledge](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge)

这款“Show HN”帖子介绍了一款AI驱动的工具，可以从GitHub代码库自动生成适合初学者的教程。该工具基于仅100行的LLM框架Pocket Flow构建，能够分析代码、识别核心抽象概念，并创建带有清晰可视化的教程。

该帖子重点介绍了针对AutoGen、FastAPI和NumPy等热门仓库的AI生成教程示例，展示了该工具解释复杂代码的能力。

要开始使用，用户需要克隆代码库，安装依赖项，配置他们的LLM API密钥（最好是像Claude 3.7或O1这样强大的模型），然后运行`main.py`脚本。用户可以指定GitHub仓库URL或本地目录、包含/排除文件模式、最大文件大小以及所需的输出语言。

该帖子提到，该项目是使用Agentic Coding开发的，即人类设计，AI代理（如Cursor AI）编码，由Pocket Flow框架提供支持。对于那些对开发过程有更深入了解的人，提供了YouTube开发教程和Substack帖子的链接。

---

## 57. 平面折纸是图灵完备的 (2023)

**原文标题**: Flat origami is Turing complete (2023)

**原文链接**: [https://arxiv.org/abs/2309.07932](https://arxiv.org/abs/2309.07932)

托马斯·C·赫尔和茵娜·扎哈列维奇在arXiv上发表的题为“平面折纸是图灵完备的”的论文证明了平面折纸是一种图灵完备的计算设备。平面折纸指的是折叠零曲率的纸张，使最终结构平铺在一个平面上。

作者通过展示具有“可选折痕”的平面折纸折痕模式可以模拟 Rule 110 来证明这一点，Rule 110 是 Matthew Cook 先前证明的图灵完备的一维元胞自动机。 该论文侧重于平面折纸映射的折痕模式，即映射不可微的线。

摘要强调了平面折纸映射及其层顺序的复杂结构。它提到了先前的研究表明，确定给定的平面图是否是某些平面折纸的折痕模式是一个 NP 完全问题。 这一新结果扩展了对平面折纸计算能力的理解，表明它不仅复杂，而且能够进行通用计算。 该论文被归类为组合数学和计算复杂度。

---

## 58. 《世界大战动物园》评论：炮火与野兽

**原文标题**: 'World War Zoos' Review: Of Bombs and Beasts

**原文链接**: [https://www.wsj.com/arts-culture/books/world-war-zoos-review-of-bombs-and-beasts-a037c4b6](https://www.wsj.com/arts-culture/books/world-war-zoos-review-of-bombs-and-beasts-a037c4b6)

无法访问文章链接。

---

## 59. 旋转能解决哈勃难题吗？

**原文标题**: Can rotation solve the Hubble Puzzle?

**原文链接**: [https://academic.oup.com/mnras/article/538/4/3038/8090496?login=false](https://academic.oup.com/mnras/article/538/4/3038/8090496?login=false)

无法访问文章链接。

---

## 60. 愚蠢的统计模型，总是让人难堪

**原文标题**: Dumb statistical models, always making people look bad

**原文链接**: [https://statmodeling.stat.columbia.edu/2025/04/18/dumb-statistical-models-always-making-people-look-bad/](https://statmodeling.stat.columbia.edu/2025/04/18/dumb-statistical-models-always-making-people-look-bad/)

无法访问文章链接。

---

## 61. 群晖硬盘锁死操作，自毁前程

**原文标题**: Synology Lost the Plot with Hard Drive Locking Move

**原文链接**: [https://www.servethehome.com/synology-lost-the-plot-with-hard-drive-locking-move/](https://www.servethehome.com/synology-lost-the-plot-with-hard-drive-locking-move/)

本文批评群晖将在即将推出的2025年“Plus”NAS型号中，把硬盘健康报告、重复数据删除和固件更新等功能锁定在其自有品牌硬盘上的做法。作者认为这是一种“攫取额外利润”的行为，会对客户产生负面影响。

关键点包括：

*   **硬盘锁定：** 群晖正在限制其NAS单元的完整功能，使其仅限于群晖品牌的硬盘。
*   **容量限制：** 群晖目前的“Plus”系列硬盘产品限制在16TB，落后于26TB的西数红盘Pro，并限制了多盘位设置中的总原始容量，逊色于QNAP或TrueNAS解决方案。
*   **可用性与成本：** 群晖硬盘的预计交货时间更长，有时比西数红盘Pro、东芝N300和希捷IronWolf Pro等现成替代品更贵。
*   **更换担忧：** 锁定在群晖硬盘会阻碍用不同型号快速更换故障硬盘的能力，特别是当特定型号出现高故障率时。它还引发了对长期可用性以及对群晖持续制造和存在的依赖的担忧。
*   **过时硬件：** 作者批评群晖在其NAS设备中使用“几代之前的硬件”。
*   **建议：** 作者总结说，过时的硬件和硬盘锁定的结合使得2025年的群晖难以推荐，尤其是在无法选择更快的替代硬盘的情况下。

---

## 62. 表格化编程：一种表达性计算的新范式

**原文标题**: Tabular Programming: A New Paradigm for Expressive Computing

**原文链接**: [https://sam.elborai.me/articles/tabular-programming/](https://sam.elborai.me/articles/tabular-programming/)

本文介绍了一种名为“表格化编程”的新型编程范式，该范式专为最小化、便携式硬件设备等受限环境设计。它受到 Dirtywave m8 音轨器的启发，建议将代码组织成结构化的表格，其中包含固定列，分别用于函数名称、输入参数、五个表达式单元格（EXP1-EXP5）和输出规范。

其核心思想是将每个函数限制为五个表达式，从而鼓励将复杂的操作分解为更小、可组合的函数，从而提高代码的可维护性。目标硬件将是最小化的，使用 Teensy 4.1 微控制器、小型显示器以及仅用于导航和编辑的八个按钮。

本文重点介绍了关键特性，如降低的错误率（通过选项选择）、专注的分解、显式的数据流和可移植性。它展示了使用此表格模型实现的两种演示场景效果（等离子和隧道），证明了在约束条件下实现复杂视觉效果的潜力。

这些示例说明了堆栈如何在行内隐式管理数据流，而函数调用则处理行之间的数据流。虚拟机将执行表格化代码，支持堆栈操作、算术、条件语句和硬件抽象。

本文还讨论了演示之外的潜在应用，例如像素艺术编辑器和音乐工具，强调了上下文相关菜单对于导航和函数发现的重要性。作者拥有一个 Web 原型来验证这个概念。最终目标是从根本上重新思考针对特定、最小硬件环境的编程方式，并通过约束来增强创造性表达。

---

## 63. 用 Joplin 做笔记

**原文标题**: Taking Notes with Joplin

**原文链接**: [https://lwn.net/Articles/1016400/](https://lwn.net/Articles/1016400/)

这篇LWN.net文章评测了Joplin，一个免费开源的笔记应用程序，适用于从代码片段到小说写作的各种用途。其主要功能包括Markdown支持、插件系统、多媒体内容附件，以及具有端到端加密的跨设备同步。

Joplin提供Linux、macOS、Windows、Android和iOS版本，使用Electron实现桌面兼容性。它支持Markdown和富文本编辑（尽管后者存在局限性），并将笔记存储在SQLite数据库中。同步选项包括Nextcloud、WebDAV、Joplin Cloud（一项付费服务）、Dropbox、OneDrive和本地文件系统选项。笔记可以使用主密码进行加密。

界面采用三窗格布局，用于导航、笔记列表和编辑/查看。3.2版本引入了多窗口支持、多列布局、改进的辅助功能以及系统主题检测。Joplin的功能可以通过基于JavaScript的扩展API进行扩展，现有插件可用于数学计算和手绘等功能。包含用于扫描文档的OCR，但难以处理复杂的格式和手写。

缺点包括由于Electron导致的高资源消耗、不同的同步性能以及WYSIWYG编辑器的局限性。开发正在进行中，定期发布版本，并受用户反馈和社区贡献驱动。尽管灵活且功能强大，但该文章表明Joplin可能缺乏某些专有替代方案的完善程度。

---

## 64. FTC对Uber采取行动，指控其欺骗性收费和取消行为

**原文标题**: FTC takes action against Uber for deceptive billing and cancellation practices

**原文链接**: [https://www.ftc.gov/news-events/news/press-releases/2025/04/ftc-takes-action-against-uber-deceptive-billing-cancellation-practices](https://www.ftc.gov/news-events/news/press-releases/2025/04/ftc-takes-action-against-uber-deceptive-billing-cancellation-practices)

联邦贸易委员会对优步采取行动，指控其存在欺骗性账单和取消行为。据联邦贸易委员会称，优步在未获得适当同意的情况下，将消费者纳入订阅服务并收取费用。联邦贸易委员会还指控优步人为地增加用户取消订阅的难度。该公告于2025年4月21日发布。这表明联邦贸易委员会认为优步通过与订阅注册和取消相关的非公平或欺骗性商业行为违反了消费者保护法。

---

## 65. 月球虫子 (2018)

**原文标题**: Moon Bugs (2018)

**原文链接**: [https://www.michalfarkas.net/moonbugs/](https://www.michalfarkas.net/moonbugs/)

米哈尔·法卡斯的网页赞颂了1983年编程的经典DOS游戏《月球虫（Moon Bugs）》。他深情地回忆起它持久的趣味性，特别是对孩子们而言，并强调了它简单却引人入胜的玩法：驾驶坦克，射击外星人，以及收集铀。

该游戏独特的160x100 16色文本模式分辨率（通过CGA调整实现）被详细介绍，同时解释了奖励关卡（通过射击小型UFO触发）和额外生命（每增加20,000分奖励）的机制。

作者探索了“破解、技巧和作弊”，包括操纵游戏代码以从更高等级或拥有更多生命开始，甚至禁用生命损失。然而，他指出一个漏洞，即阻止生命损失会导致怪物频率和铀收集的难度增加。他还提到由于游戏循环，99级无法达到。

该网站强调了《月球虫》的简洁之美，仅有50 KB的代码和数据，没有现代的复杂性，例如框架、依赖项或在线帐户。

最后，该页面提供了如何在DOSBox中运行《月球虫》的说明，包括配置设置和游戏本身（MOONBUGS.ZIP）以及修改版本（MOON98.ZIP）的下载链接。该页面将读者指向www.digger.org，并以反汇编代码示例以及等级和生命值结束。

---

## 66. 用 Haskell 改造我的 Python

**原文标题**: Haskelling My Python

**原文链接**: [https://unnamed.website/posts/haskelling-my-python/](https://unnamed.website/posts/haskelling-my-python/)

用Python实现Haskell的特性：惰性无限列表

---

## 67. 高血压？多吃香蕉。

**原文标题**: High blood pressure? Eat more bananas

**原文链接**: [https://uwaterloo.ca/news/media/high-blood-pressure-eat-more-bananas](https://uwaterloo.ca/news/media/high-blood-pressure-eat-more-bananas)

本文重点介绍了滑铁卢大学的一项研究，该研究表明，增加膳食钾摄入量，而不是仅仅减少钠，可能是降低高血压更有效的策略。高血压影响着全球相当大比例的成年人，并可能导致严重的健康并发症。

该研究使用数学模型发现，钾与钠的摄入比例至关重要。研究人员表示，我们的身体可能已经进化到在高钾、低钠饮食下运作得最好，这反映了早期人类的饮食习惯。然而，现代西方饮食通常高钠低钾，这可能导致工业化社会中高血压的普遍存在。

该模型还揭示了钾与血压之间关系的性别差异。男性比绝经前女性更容易患上高血压，但也更可能从增加钾摄入量中获益。研究人员强调了数学模型在高效且合乎伦理地识别影响身体的因素方面的价值。他们建议在饮食中加入富含钾的食物，如香蕉或西兰花，以潜在地改善血压。

---

## 68. 本地LLM推理：令人印象深刻，但难以使用

**原文标题**: Local LLM inference – impressive but too hard to work with

**原文链接**: [https://medium.com/@aazo11/local-llm-inference-897a06cc17a2](https://medium.com/@aazo11/local-llm-inference-897a06cc17a2)

Amir Zohrenejad 探索本地LLM推理，强调其潜力和当前局限。他认为，尽管令人印象深刻，但尚未达到生产就绪状态。作者指出了本地计算的几大优势：降低成本、增强隐私、提高速度以及实现离线功能。他们使用 DeepSeek-R1-Distill-Qwen-7B 的量化版本测试了 llama.cpp、Ollama 和 WebLLM 等框架，并以 OpenAI 的 gpt-4.0-mini 作为性能基准。

Llama.cpp 和 Ollama 在首个 token 出现时间 (TTFT) 方面表现更快，而 WebLLM 在每秒 token 数 (TPS) 方面落后。尽管性能尚可，但所有本地解决方案都比基于云的 gpt-4.0-mini 慢。作者强调了找到和部署适合本地执行的更小、特定任务模型的挑战。模型的种类繁多和缓慢的下载时间会显著降低用户体验。

作者总结说，虽然本地 LLM 推理是可行的，但更好的开发者工具对于广泛采用至关重要。一个实际的解决方案需要简化的训练、更小模型的部署、与云 LLM 的无缝集成以及透明的下载和缓存处理，以提供无缝的用户体验。

---

## 69. 为 Tcl 过程添加关键字参数

**原文标题**: Adding keyword parameters to Tcl procs

**原文链接**: [https://world-playground-deceit.net/blog/2025/04/adding-keyword-parameters-to-tcl-procs.html](https://world-playground-deceit.net/blog/2025/04/adding-keyword-parameters-to-tcl-procs.html)

这篇博文讨论了作者为Tcl过程添加关键字参数的解决方案，这是他们在该语言的标准功能中发现缺失的一项特性。他们的目标是复制类似于UNIX的选项解析行为，这种行为在Tcl的内置命令中很常见，并使其在用户自定义的过程中可用。

作者提出了一个围绕标准`proc`命令的`proc*`包装器。该包装器解析参数列表以查找可选的、命名参数（标志和选项），从而允许类似于命令行实用程序的与顺序无关的参数传递。它基于定义的强制性位置参数的数量，处理位置参数和关键字参数之间的歧义。

该实现包括预处理过程的参数列表以识别可选参数，构建`optswitch`逻辑，并使用`quasiquote`动态生成代码，以处理参数解析和过程体的应用。

作者强调了由于缺乏选择性字符串替换，Tcl中元编程的挑战。然后，他们深入研究了自定义`quasiquote`命令的实现细节，该命令使用字符串操作和正则表达式来选择性地取消引用和拼接字符串中的代码片段，从而有效地创建了一个基于字符串的模板系统。他们承认这个解决方案很复杂，并且是对Tcl在这方面限制的变通方法。

---

## 70. Python 的新 t 字符串

**原文标题**: Python’s new t-strings

**原文链接**: [https://davepeck.org/2025/04/11/pythons-new-t-strings/](https://davepeck.org/2025/04/11/pythons-new-t-strings/)

本文宣布Python 3.14接受“t-strings”（模板字符串）作为一项新特性，预计于2025年末发布。作者强调，t-strings旨在解决f-strings的误用问题，尤其是在处理用户输入时，这可能导致SQL注入和跨站脚本等安全漏洞。

与立即求值为字符串的f-strings不同，t-strings会创建一个`string.templatelib.Template`对象。该对象分别包含字符串和插值，使开发者能够在创建最终字符串之前安全地处理和转义动态内容。库可以利用t-strings执行自定义处理，例如HTML转义或类型转换。

本文解释了如何使用t-strings，详细说明了如何通过`.strings`、`.values`访问字符串部分和值，如何迭代模板，甚至访问详细的插值信息。文章还包含一个将模板字符串转换为猪拉丁语的简单示例，以说明如何处理模板。作者希望看到t-strings被广泛采用，尤其是在处理用户输入的库中，并希望格式化工具和IDE等工具能够添加对它们的支持。

---

## 71. 流水线操作可能是我最喜欢的编程语言特性。

**原文标题**: Pipelining might be my favorite programming language feature

**原文链接**: [https://herecomesthemoon.net/2025/04/pipelining/](https://herecomesthemoon.net/2025/04/pipelining/)

本文倡导流水线操作作为一种更优越的编程语言特性。流水线操作，也称方法链，允许省略参数，通过传递前一个值，创建可读的、逐行流程。作者认为流水线操作的优势包括提高可读性、更易于注释，以及无需中间变量，这与嵌套函数调用形成对比，后者控制流是“由内而外”且更难解析。

作者认为，使用“.”运算符的成员访问是流水线操作的一个常见且有用的实例。文章强调了流水线操作的编辑优势，使其更容易添加或修改操作，而无需复杂的括号管理或混乱的git差异。通过IDE自动完成的代码发现也因流水线操作而得到显著增强，因为IDE可以基于流水线左侧对象的类型提供建议。

流水线操作的原则被应用于SQL，作者提出了一种嵌套较少的替代语法。他们还将其与建造者模式联系起来，通过方法链实现复杂对象的构建。文章探讨了在Haskell中使用“&”运算符来改进流水线操作的可读性，将从右到左的数据流转换为更线性的方法。

---

## 72. RISC-V RVA23规范：一个重要的里程碑

**原文标题**: RISC-V RVA23 Profile: A major milestone

**原文链接**: [https://riscv.org/ecosystem-news/2025/04/risc-v-rva23-a-major-milestone/](https://riscv.org/ecosystem-news/2025/04/risc-v-rva23-a-major-milestone/)

本文重点强调了RISC-V Profiles的重要性，特别是已批准的RVA23 Profile，它有助于促进RISC-V生态系统内的增长和兼容性。RVA23在2024年北美RISC-V峰会上的批准是一项重大事件，使RISC-V成为应用处理器市场潜在的领导者。RVA profiles，特别是针对64位应用处理器的，旨在运行来自标准二进制操作系统发行版的丰富操作系统。它们的主要功能是确保软件在各种硬件实现之间的可移植性，从而防止供应商锁定并鼓励更广泛地采用RISC-V。简而言之，RVA23和未来的profiles对于标准化RISC-V实现并促进更开放和更具竞争力的处理器格局至关重要。

---

## 73. 科学家证实1958年关于维生素B1的假设

**原文标题**: Scientists confirm vitamin B1 hypothesis from 1958

**原文链接**: [https://news.ucr.edu/articles/2025/04/21/scientists-finally-confirm-vitamin-b1-hypothesis-1958](https://news.ucr.edu/articles/2025/04/21/scientists-finally-confirm-vitamin-b1-hypothesis-1958)

加州大学河滨分校的化学家证实了罗纳德·布雷斯洛提出的关于维生素B1（硫胺素）的一个有67年历史的理论，他们成功地在水中稳定了一种叫做卡宾的高活性分子。卡宾是只有六个价电子的碳原子，通常极不稳定，在水中会立即分解。布雷斯洛在1958年提出，维生素B1可以转化为类卡宾结构，以促进体内的生化反应。

该研究团队由文森特·拉瓦洛教授领导，他们通过将卡宾包裹在一个合成的“盔甲”分子中，使其免受水和其他反应性化合物的影响，从而实现了这一突破。这使他们能够分离卡宾，使用核磁共振波谱和X射线晶体学观察其结构，并证明其在水性环境中的稳定性。

这一发现不仅验证了布雷斯洛数十年前的假设，而且具有重要的实际意义。卡宾广泛用作金属基催化剂中的配体，这些催化剂对于生产药物、燃料和其他材料至关重要。在水中稳定卡宾可能带来更清洁、更高效、更便宜的催化过程，从而减少对有毒有机溶剂的依赖。此外，在水中稳定活性中间分子，使科学家们更接近于理解和模仿细胞内自然发生的化学过程。这项研究强调了坚持不懈和持续投资于科学发现的重要性。

---

## 74. 我如何使用Kate编辑器

**原文标题**: How I use Kate editor

**原文链接**: [https://akselmo.dev/posts/how-i-use-kate-editor/](https://akselmo.dev/posts/how-i-use-kate-editor/)

本文是一位长期用户对Kate文本编辑器的热情推荐，详细介绍了他们的工作流程和配置。作者强调了Kate的持久性、易于设置以及丰富的开箱即用功能是主要的卖点。他们讨论了关键设置，如插件使用（编译和运行、LSP客户端、调试器、Git Blame等）、自定义快捷键和会话管理（分离工作和个人项目）。

文章的很大一部分 посвящена于解释语言服务器协议（LSP）、调试适配器协议（DAP）和格式化程序的配置。作者还强调了路径设置对于语言服务器发现的重要性。

除了配置之外，文章还展示了Kate的实际应用，例如文件快速切换、动作搜索（查找Kate命令）以及强大的“编译和运行”插件，用于在项目中执行自定义命令。Git集成，提供差异比较、暂存和提交功能，也受到了称赞。

作者还探讨了Kate的Snippets功能，该功能允许使用JavaScript进行动态代码生成。文章最后将其与VSCode进行了比较，认为Kate的集成功能和避免专有扩展使其成为作者的更好选择。作者强调了热情的社区和KDE哲学的体现是他们忠诚的原因，并鼓励读者尝试Kate。

---

## 75. AI正在帮助诈骗犯在几分钟内大量制造诈骗活动。

**原文标题**: AI is helping fraudsters pump out scamming campaigns in minutes

**原文链接**: [https://www.techradar.com/pro/security/ai-is-helping-fraudsters-pump-out-scamming-campaigns-in-minutes](https://www.techradar.com/pro/security/ai-is-helping-fraudsters-pump-out-scamming-campaigns-in-minutes)

生成式AI正大幅加速并简化复杂网络诈骗的制造

---

## 76. 长期L1执行层提案：用RISC-V取代EVM

**原文标题**: Long-term L1 execution layer proposal: replace the EVM with RISC-V

**原文链接**: [https://ethereum-magicians.org/t/long-term-l1-execution-layer-proposal-replace-the-evm-with-risc-v/23617](https://ethereum-magicians.org/t/long-term-l1-execution-layer-proposal-replace-the-evm-with-risc-v/23617)

本提案建议将以太坊虚拟机（EVM）替换为RISC-V，作为智能合约的执行层，以大幅提高效率并简化执行层。账户、存储和跨合约调用等现有概念将保留，而EVM操作码（SLOAD、SSTORE等）将变为RISC-V系统调用。开发者仍然可以使用Solidity和Vyper，它们将被调整为编译到RISC-V。

主要动机是解决长期的扩展瓶颈，特别是关于ZK-EVM的证明成本。作者认为，很大一部分证明时间花费在EVM特定的操作上，而RISC-V可以更有效地执行这些操作，有可能使证明器效率提高50倍以上。

该提案概述了几种实现策略：支持具有互操作性的双虚拟机（EVM和RISC-V），将现有的EVM合约转换为调用用RISC-V编写的EVM解释器，或者形式化“虚拟机解释器”的概念，需要RISC-V实现。后两种方法具有简化执行层规范的优势，可能使其变得更小且更易于维护。作者认为，这种根本性的改变可能是实现执行层上与beam链在共识层上获得的可比简化收益的唯一途径。

---

## 77. 化石燃料发电占比首次跌破50%，创美国历史新低

**原文标题**: Fossil fuels fall below 50% of US electricity for the first month on record

**原文链接**: [https://ember-energy.org/latest-updates/fossil-fuels-fall-below-50-of-us-electricity-for-the-first-month-on-record/](https://ember-energy.org/latest-updates/fossil-fuels-fall-below-50-of-us-electricity-for-the-first-month-on-record/)

以下是该文章的简明摘要：

2025年3月，美国在其能源转型方面取得了一个重要里程碑，化石燃料发电首次低于全国电力供应的50%（49.2%），创下历史新低。这一转变归功于创纪录的太阳能和风力发电量，两者合计占美国电力结构的24.4%。清洁能源总计贡献了50.8%的电力。

太阳能发电量较2024年3月显著增长了37%，风力发电量增长了12%。风能和太阳能发电总量达到83太瓦时，超过了2024年4月创下的75太瓦时的纪录。相比之下，化石燃料发电量下降了2.5%。

这一成就标志着美国电力部门对化石燃料依赖程度长期下降的趋势，过去十年中，太阳能和风能发电量大幅增长。十年前，即2015年3月，化石燃料占发电量的65%，而风能和太阳能仅贡献了5.7%。

预计2025年美国新增发电容量中，太阳能将占一半以上，德克萨斯州是新增太阳能电池板的主要接收地。“美国电力2025”最新报告强调，太阳能是2024年美国增长最快的电力来源。2024年，风能和太阳能发电总量达到美国电力结构的17%，首次超过煤炭。

发布该数据的能源智库Ember认为，这一里程碑标志着一个转折点，清洁能源开始在美国能源领域占据主导地位。

---

## 78. Pydrofoil：加速帆船式指令集模拟器

**原文标题**: Pydrofoil: Accelerating Sail-based instruction set simulators

**原文链接**: [https://arxiv.org/abs/2503.04389](https://arxiv.org/abs/2503.04389)

本文介绍Pydrofoil，一种新型多阶段编译器，旨在加速从高级ISA规范语言Sail生成的指令集模拟器（ISS）。作者证明，与Sail默认的基于C的ISS相比，在他们的基准测试中速度提升超过230倍。

Pydrofoil的方法基于三个关键见解：

1. ISS本质上是解释器循环，即时（JIT）编译跟踪已被证明是有效的。
2. ISS工作负载主要由位操作构成，通用编译器优化效果不佳。
3. 仅使用跟踪JIT或提前（AOT）编译都无法获得最佳性能。

因此，Pydrofoil采用混合方法，将AOT编译器与基于PyPy元跟踪框架构建的跟踪JIT编译器相结合。AOT和JIT组件都利用针对位操作量身定制的领域特定优化。

基准测试突出了这种混合方法的有效性，表明AOT和JIT编译的结合产生了比单独使用任一编译器更大的性能提升。这表明Pydrofoil提供了一种从Sail规范生成高性能ISS的强大方法。

---

## 79. 生物膜的奇异形状如何从细胞几何结构中涌现

**原文标题**: How a Biofilm’s Strange Shape Emerges From Cellular Geometry

**原文链接**: [https://www.quantamagazine.org/how-a-biofilms-strange-shape-emerges-from-cellular-geometry-20250421/](https://www.quantamagazine.org/how-a-biofilms-strange-shape-emerges-from-cellular-geometry-20250421/)

本文探讨了界面上存在的微生物群落——生物膜——的独特形状如何从其组成微生物与其环境的相互作用中产生。佐治亚理工学院生物物理学家彼得·扬克的科研工作侧重于理解单个细菌之间的相互作用如何导致生物膜的高阶结构，特别是生物膜生长过程中出现的奇怪形状。

生物膜既是单细胞的，又是多细胞的，表现出诸如将自身固定在表面、集体消化更多营养物质以及获得免受环境压力源侵害的保护等涌现特性。然而，群居生活也带来挑战，例如将营养物质和氧气分配给所有细胞的困难。Lars Dietrich的研究表明，营养物质分配只有在20-50个细胞厚的生物膜中才会成为问题，突显了物理结构的重要性。他发现营养物质可用性的变化会导致不同的生物膜形貌。

扬克的工作利用软物质物理原理来研究这些形状。他将生物膜比作胶体，其中颗粒之间的相互作用会产生复杂的集体现象。排斥力（细胞不能占据同一空间）和吸引力（粘性蛋白质将细胞粘在一起）之间的平衡决定了生物膜的形成。扬克的团队发现，生物膜前沿的几何形状，特别是扩展边缘与基质之间的接触角，在其整体生长和适应性中起着至关重要的作用。该角度由细胞粘性和细胞数量决定，影响营养物质的可用性、细胞分裂速率和细胞死亡速率，最终控制生物膜的复杂结构。该研究表明，细胞之间简单的相互作用如何导致具有生物学意义的涌现物理特征，从而可能为了解多细胞生物的进化提供见解。

---

## 80. 官方XRP NPM包已被入侵，并引入窃取密钥的恶意软件。

**原文标题**: Offical XRP NPM package has been compromised and key stealing malware introduced

**原文链接**: [https://www.aikido.dev/blog/xrp-supplychain-attack-official-npm-package-infected-with-crypto-stealing-backdoor](https://www.aikido.dev/blog/xrp-supplychain-attack-official-npm-package-infected-with-crypto-stealing-backdoor)

广受欢迎的XRP Ledger (xrpl)官方NPM包（每周下载量超过14万）遭到攻击，攻击者植入了一个窃取加密货币的后门。此次供应链攻击可能影响数十万个应用程序和网站。

Aikido Intel检测到用户mukulljangid发布的xrpl包的五个恶意版本（4.2.1、4.2.2、4.2.3、4.2.4和2.14.2）。这些版本包含可疑代码，包括一个`checkValidityOfSeed`函数，该函数会将私钥发送到一个新注册的域名（0x9c[.]xyz）。恶意代码被注入到Wallet类构造函数和其他与钱包创建和种子派生相关的函数中，从而能够在Wallet对象被实例化后立即窃取加密货币私钥。

攻击者尝试了多种插入后门的方法，从直接修改JavaScript代码到修改TypeScript代码。入侵指标包括指定的包版本以及4月21日20:53 GMT+0至4月22日13:00 GMT+0期间与已识别域名的出站连接。建议用户将受损代码处理过的任何种子或私钥视为已泄露，并将资产转移到新钱包。xrpl团队已发布4.2.5和2.14.3版本以覆盖恶意软件包。

---

## 81. 走出迷雾

**原文标题**: Out of the Fog

**原文链接**: [https://www.theverge.com/cs/features/651701/vietnam-operation-babylift-adoption-transnational](https://www.theverge.com/cs/features/651701/vietnam-operation-babylift-adoption-transnational)

卡米尔·布罗姆利的《走出迷雾》探讨了“婴儿空运行动”的复杂遗产。该行动是指1975年西贡陷落期间，大规模将越南儿童送往西方国家进行收养。该文章挑战了纯粹人道主义救援任务的流行叙事，突出了伦理上的含糊不清以及对被收养者的长期后果。

虽然福特总统将婴儿空运行动描述为“慈悲行动”，但布罗姆利揭示了一个更为复杂的现实，包括一架C-5A银河飞机的悲惨坠毁、许多儿童令人质疑的孤儿身份以及文件的伪造。一些母亲，如Anh Thi Hoang Doan，在违背自己意愿的情况下与孩子分离。

该文章强调了被收养者在努力应对身份认同、文化错位和潜在虐待时所面临的困难。“跨国收养者之声”和“越南国际收养者协会”(AVI)等组织应运而生，为被收养者提供资源和社区归属感，帮助他们寻找关于自己过去的答案。布罗姆利强调了在他们经常感到不完整、徘徊于两种文化之间、并寻找归属感和身份认同的世界中航行的挑战。这篇文章强调了“婴儿空运行动”的持久影响，不仅对被拯救的儿童，也对他们对身份、家庭和归属感的理解产生了影响。

---

## 82. 神经科学家竞相将脑电波转化为语音

**原文标题**: Neuroscientists are racing to turn brain waves into speech

**原文链接**: [https://arstechnica.com/health/2025/04/neuroscientists-are-racing-to-turn-brain-waves-into-speech/](https://arstechnica.com/health/2025/04/neuroscientists-are-racing-to-turn-brain-waves-into-speech/)

无法访问文章链接。

---

## 83. Swift 6.2：并发变革初探

**原文标题**: Swift 6.2: A first look at how it's changing Concurrency

**原文链接**: [https://www.avanderlee.com/concurrency/swift-6-2-concurrency-changes/](https://www.avanderlee.com/concurrency/swift-6-2-concurrency-changes/)

本文初步探讨了Swift 6.2如何旨在提高Swift并发的可访问性，因为并发一直是开发者的痛点。 考虑到开发者在迁移现有项目以及新手过早遇到并发概念时面临的挑战，Swift团队概述了逐步揭示并发的愿景。

核心思想是将并发的采用简化为三个阶段：1）默认情况下为单线程代码，2）没有数据竞争安全问题的异步代码，以及3）具有编译器辅助安全性的高级并发。 Swift 6.2将引入更改以支持此愿景，减少编译器警告和错误，并可能提供自动迁移工具。

本文重点介绍了与此愿景相关的已实施或已接受的Swift Evolution提案，包括SE-0466（默认为MainActor隔离以减少误报）和SE-0461（默认情况下在调用者的actor上运行nonisolated异步函数，以防止意外的多线程和数据竞争）。 作者通过代码示例演示了这些提案如何改变并发行为。

主要结论是，Swift 6.2正在采取措施使并发更易于管理，特别是对于那些并非有意使用并行性的人，并简化了向Swift 6更严格的并发规则的过渡。 这些更改最终将需要在项目中选择启用新行为。

---

## 84. 去中心化方案

**原文标题**: Decentralizing Schemes

**原文链接**: [https://www.tbray.org/ongoing/When/202x/2025/04/16/Decentralized-Schemes](https://www.tbray.org/ongoing/When/202x/2025/04/16/Decentralized-Schemes)

蒂姆·布雷力主使用URI方案（如`mailto:`）来改善去中心化社交媒体平台（如联邦宇宙和Bluesky）的用户体验。他认为，目前对`https:` URL的依赖导致了分享、客户端选择和帖子可移植性方面的问题。

具体来说，点击一个指向联邦宇宙帖子的`https:`链接通常会在默认浏览器中打开，而不是用户首选的联邦宇宙客户端，从而阻碍了互动。此外，当一个联邦宇宙实例关闭时，所有托管在那里的帖子都会丢失，因为URL不再有效。

布雷建议为联邦宇宙和Bluesky分别注册自定义URI方案，如`fedi:`或`at:`。这些方案将允许操作系统将链接分发到适当的社交媒体应用程序，从而改善用户体验。此外，联邦宇宙软件可以使用`fedi:`方案来跟踪迁移的帐户并从已失效的服务器检索帖子，从而确保帖子的可移植性。

文章承认存在挑战，包括浏览器对替代方案的支持不足，但认为去中心化社交媒体日益增长的势头使其更有理由实施这些方案。他认为，URI方案是Web架构的核心组成部分，旨在支持多种协议，因此应该用于去中心化平台。

评论讨论了实施细节、浏览器回退行为以及NOSTR等替代的去中心化协议。

---

## 85. 教宗方济各去世了

**原文标题**: Pope Francis has died

**原文链接**: [https://www.reuters.com/world/pope-francis-has-died-vatican-says-video-statement-2025-04-21/](https://www.reuters.com/world/pope-francis-has-died-vatican-says-video-statement-2025-04-21/)

无法访问文章链接。

---

## 86. 电影加密技术原理

**原文标题**: How encryption for Cinema Movies works

**原文链接**: [https://serverless.industries/2024/05/31/digital-cinema.en.html](https://serverless.industries/2024/05/31/digital-cinema.en.html)

本文概述了根据DCI（数字电影倡议）标准，数字电影的加密和发行方式。DCI标准确保电影在影院的安全交付和播放。

该过程始于制片人创建一个数字电影包（DCP），其中包含电影的音频、视频和元数据，分别位于MXF文件中。在母版制作过程中，使用诸如DCP-o-matic之类的工具，内容会使用静态的AES 128位密钥进行加密。

为了保护加密密钥，会创建一个密钥分发消息（DKDM）。AES密钥会使用发行商的公钥进行加密。然后，发行商为各个影院生成密钥交付消息（KDM）。这些KDM包含AES密钥，该密钥使用特定投影仪的公钥重新加密。

投影仪使用“媒体块”来实时解密DCP数据。KDM提供了解密所需的加密信息。由根证书、中间证书和叶证书组成的证书链用于验证发行商和投影仪的真实性。投影仪通过比较签名证书的指纹和密钥UUID与XML文件中的信息来验证KDM。

发行过程还依赖于投影仪制造商提供的“可信设备列表”。只有此列表上经过DCI认证的投影仪才可能收到发行商的KDM，从而防止未经授权的播放。

本文还涉及DCP中使用的MXF文件格式，并描述了MXF帧中三元组的结构，详细说明了加密密钥、加密上下文链接和纯文本偏移量的存在。

---

## 87. 展示一下：我做了个应用，这样我就可以用中文读《三体》了

**原文标题**: Show HN: I built an app so I could read the 3 Body-Problem in Chinese

**原文链接**: [https://readly.ink/](https://readly.ink/)

这款“Show HN”帖子介绍Readly，一款移动应用，旨在简化中文文本阅读，其灵感源于作者阅读《三体》的需求。Readly通过整合图像文本识别、即时翻译、拼音显示、音频发音、AI驱动的文本分析和闪卡创建等多项功能，简化学习过程。

用户可以拍摄来自小说、教科书或社交媒体帖子等各种来源的中文文本图片。然后，该应用只需轻点一下，即可提供翻译、拼音和音频。用户还可以单独查找单词或句子。Readly更进一步，提供AI驱动的文本解释，帮助用户理解复杂的段落。

最后，Readly自动执行闪卡创建过程。用户可以一键将单词添加到Anki风格的间隔重复闪卡中，从而促进长期记忆。该应用旨在消除手动查找单词和创建闪卡这一耗时的过程，使中文阅读更加高效和愉快。

---

## 88. 锯齿状AGI：o3、Gemini 2.5 以及之后的一切

**原文标题**: Jagged AGI: o3, Gemini 2.5, and everything after

**原文链接**: [https://www.oneusefulthing.org/p/on-jagged-agi-o3-gemini-25-and-everything](https://www.oneusefulthing.org/p/on-jagged-agi-o3-gemini-25-and-everything)

Ethan Mollick 的文章《锯齿状通用人工智能：o3、Gemini 2.5 以及之后的一切》，探讨了在近期人工智能进步的背景下，特别是像 o3 和 Gemini 2.5 这样的模型，定义和衡量通用人工智能 (AGI) 所面临的挑战。

Mollick 强调了人工智能的“锯齿状前沿”，意味着人工智能在一些复杂任务中表现出色，但在简单的任务中却会失败，这使得它的能力参差不齐且难以预测。他用 o3 在营销计划生成和地理猜测等任务中的出色能力，以及它在修改后的脑筋急转弯中的失败进行了说明。

文章讨论了 Tyler Cowen 如何宣布 o3 为 AGI，这归功于该模型增强的推理和自主代理能力（分解目标并独立使用工具）。Mollick 质疑了这一声明，承认围绕 AGI 的定义问题，但认为这些模型代表了一种“锯齿状 AGI”——在某些领域超越人类，但在其他领域却不可靠，需要人工监督。

他还探讨了实现 AGI 或高水平的“锯齿状 AGI”是否会导致立即的社会变革。虽然历史模式表明技术会逐渐普及，但文章承认，人工智能的自主代理能力可能会加速采用，速度快于预期，或者可能会出现不可预见的能力阈值，从而改变人工智能融入社会的方式。文章最后强调，人工智能的未来轨迹及其影响仍然不确定，强调了在这一“锯齿状景象”中航行，为即将到来的变革做好准备的重要性。

---

## 89. 找出异常磁盘

**原文标题**: Find the Odd Disk

**原文链接**: [https://colors2.alessandroroussel.com/](https://colors2.alessandroroussel.com/)

本文介绍一款名为“找出异色圆盘”的简单在线游戏，这是一个颜色辨别实验。玩家会看到一组圆盘，必须点击颜色与其他圆盘不同的那个。游戏强调使用视觉感知，不依赖可能改变颜色呈现的工具或屏幕滤镜。说明明确要求玩家禁用蓝光过滤。游戏提供英语、法语和西班牙语说明。用户会被告知当前回合数，例如“回合：1 / 20”，表明游戏包含多个回合。本文还展示了“游戏结束！”的消息，并感谢参与者的参与，鼓励他们再次玩游戏以贡献更多数据。

---

## 90. 通廷咖啡馆 (2018)

**原文标题**: The Tontine Coffee-House (2018)

**原文链接**: [https://tontinecoffeehouse.com/2018/10/15/the-tontine-coffee-house/](https://tontinecoffeehouse.com/2018/10/15/the-tontine-coffee-house/)

本文探讨了纽约证券交易所的起源，追溯其根源至托丁咖啡馆。1792年，经纪人签署了梧桐树协议，规范了交易。此后不久，托丁咖啡馆作为正式交易场所建立起来，由一种名为“托丁”的古老年金形式资助。

托丁以洛伦佐·德·托蒂命名，结合了退休计划和彩票。投资者购买股份并领取股息直至去世，已故投资者的分配份额将重新分配给幸存者，随着时间的推移，增加他们的收益。这使得比其他人活得更久在经济上更有利。

托丁咖啡馆建于1793-94年，拥有超过4万美元（相当于今天的超过100万美元）的托丁资金，成为华尔街交易员的中心枢纽。它位于华尔街和水街的拐角处，容纳了从事各种金融交易的经纪人、商人和政客。

交易最终于1817年迁至专门的交易所大楼，托丁咖啡馆后来被拆除。托丁本身于1870年结束，使最后七位幸存的受益人受益，他们中的许多人已经是纽约社会杰出人士。

本文认为，托丁咖啡馆的故事强调了美国股市的卑微开端，并让人们得以一窥18世纪的金融实践。它提醒读者欣赏证券业务的起源以及当今数万亿美元市场背后的历史背景。

---

## 91. 停用脸书和照片墙对用户情绪状态的影响

**原文标题**: The effect of deactivating Facebook and Instagram on users' emotional state

**原文链接**: [https://www.nber.org/papers/w33697](https://www.nber.org/papers/w33697)

这份发表于2025年4月的美国国家经济研究局工作论文，调查了停用Facebook和Instagram对用户情绪状态的影响，尤其关注幸福感、抑郁和焦虑。该研究使用了2020年美国大选前进行的两个大型随机实验的数据。

主要发现是，长时间停用社交媒体可以改善情绪健康。与仅停用一周的人相比，在选举前六周停用Facebook的参与者，其幸福感、抑郁和焦虑指数提高了0.060个标准差。同样，停用Instagram六周的参与者，该指数提高了0.041个标准差。

进一步的探索性分析揭示了人口统计学上的细微差别。Facebook停用的积极影响在35岁以上的人群中更为明显，而Instagram停用的积极影响在25岁以下的女性中更为显著。

该论文还包括致谢和披露，强调了潜在的利益冲突。许多作者收到了Meta（Facebook的母公司）或相关公司的资金、差旅补偿或咨询费，或持有Meta股票，这在解读研究结果时需要考虑。

---

## 92. 重写30行Linux代码可降低高达30%的功耗

**原文标题**: Reworking 30 lines of Linux code could cut power use by up to 30 percent

**原文链接**: [https://spectrum.ieee.org/data-center-energy-consumption](https://spectrum.ieee.org/data-center-energy-consumption)

对Linux进行一个简单的代码调整，只需30行代码，就有可能使数据中心的功耗显著降低高达30%。这个由滑铁卢大学计算机科学教授Martin Karsten和他的合作者开发的修复方案，解决了以往浪费能源的一个低效率问题。这一发现表明，对基础软件进行相对较小的调整，就能对能源效率产生重大影响，尤其是在数据中心等资源密集型环境中。文章强调了持续优化软件以节约能源的重要性，尤其是在计算需求和对可持续实践的需求不断增长的情况下。

---

## 93. Show HN: Nerdlog – 快速、多主机 TUI 日志查看器，带时间线直方图

**原文标题**: Show HN: Nerdlog – Fast, multi-host TUI log viewer with timeline histogram

**原文链接**: [https://github.com/dimonomid/nerdlog](https://github.com/dimonomid/nerdlog)

Nerdlog：一款快速、远程优先、多主机 TUI 日志查看器，灵感来源于 Graylog/Kibana，但没有集中式服务器的臃肿。它专注于通过 SSH 高效查询多台远程机器的日志，按时间范围和模式进行过滤，并显示时间线直方图以进行可视化分析。所有日志分析都在远程主机上进行，仅下载有限的数据（每个日志流最多 250 条消息和直方图数据）。数据在传输过程中会进行 gzip 压缩以节省带宽。

主要功能包括：

*   **多主机支持：** 通过 SSH 连接到多个远程主机。
*   **时间线直方图：** 提供一段时间内日志活动的可视化概览。
*   **高效查询：** 在远程分析日志，最大限度地减少数据传输。
*   **灵活的日志流配置：** 支持 SSH 配置和自定义 YAML 配置，用于配置日志文件位置、用户和端口。
*   **Awk 模式过滤：** 使用 awk 进行强大的日志过滤。
*   **类 Vim 导航：** 支持 Vim 键绑定和命令行界面。

Nerdlog 需要 Go 进行安装，通过 SSH 访问具有正在运行的 SSH 代理的远程主机，并在远程主机上安装 Gawk。它仍处于概念验证阶段，但可用且速度惊人，尤其是在读取 `/var/log/messages` 等系统日志时。该工具提供 UI 导航、键盘快捷键和命令，用于查询、断开连接、编辑查询等。

---

## 94. 以匠心代码：重返旧道场

**原文标题**: Coding as Craft: Going Back to the Old Gym

**原文链接**: [https://cekrem.github.io/posts/coding-as-craft-going-back-to-the-old-gym/](https://cekrem.github.io/posts/coding-as-craft-going-back-to-the-old-gym/)

本文反对在编程中“反射式地使用AI”，提倡一种平衡的方法，将编程作为一种技艺来保留，并培养真正的技能。作者受Shopify CEO的一句话和电影《洛奇3》的启发，引入了“旧式健身房”的概念——指程序员直接面对问题，不依赖AI生成解决方案的，具有挑战性的精神空间。

作者并非反对AI，而是承认其在生成样板代码、总结文档和调试等任务中的用处。然而，他们认为编程的核心——思考、设计和架构决策——应该仍然是程序员的领域，以保持技能并享受这门技艺。

中心论点是，认知上的挣扎对于学习至关重要。解决问题的艰难过程会带来“顿悟”时刻和改善编码能力的神经通路。将这些外包给AI会剥夺程序员的成长机会。

作者提出了与AI的“有意的协作”：战略性地使用AI，保持批判性思维，理解集成的代码，并挑战AI的假设。他们还提供了一个“旧式健身房训练计划”，其中包括为AI使用设置界限，练习手动编码，理解使用的代码，拥抱挣扎，以及深入学习基础知识。文章最后强调，编码不仅仅是关于输出，而是关于成为更好的问题解决者，而这个过程不能完全外包给AI。

---

## 95. 量子保密磁导航，定位精度高于GPS

**原文标题**: Quantum-assured magnetic navigation with higher positioning accuracy than GPS

**原文链接**: [https://arxiv.org/abs/2504.08167](https://arxiv.org/abs/2504.08167)

量子保障磁导航系统在空地试验中超越战略级惯性导航系统

---

## 96. 逆向工程混淆后的TikTok虚拟机

**原文标题**: Reverse engineering the obfuscated TikTok VM

**原文链接**: [https://github.com/LukasOgunfeitimi/TikTok-ReverseEngineering](https://github.com/LukasOgunfeitimi/TikTok-ReverseEngineering)

本文档详细介绍了对 TikTok 在 `webmssdk.js` 中发现的混淆虚拟机 (VM) 的逆向工程。TikTok 使用此 VM 进行混淆和安全保护。该项目的目标是反混淆脚本、反编译 VM 指令、注入反混淆的 VM，并为经过身份验证的请求（如发布评论）生成签名 URL。

最初的混淆严重依赖于括号表示法和数组编码，可以通过执行编码片段并使用正则表达式替换来绕过。函数调用隐藏在数组中，需要使用 AST 分析将其转换为标准函数调用。

VM 的字节码以 XOR 加密、gZip 压缩的字符串形式存储，并使用 leb128 编码。解密包括提取密钥、解密字节码，然后提取字符串、函数和元数据。

字节码 VM 支持作用域、嵌套函数和异常处理。通过手动分析 VM 指令并生成可读代码，创建了一个反编译器。通过使用 Tampermonkey 等浏览器扩展程序将原始 `webmssdk.js` 替换为反混淆版本并禁用 CSP，可以方便地进行调试。

签名 URL 对于经过身份验证的请求至关重要。该过程涉及以下 VM：VM86 作为初始调用，VM113 用于 X-Bogus，VM189 用于 _signature 生成。已成功实现一个签名器，用于生成有效的签名，这证明了发布评论的能力。对于签名生成，可以忽略客户端机器人保护措施，例如鼠标跟踪。TikTok VM 不断更新，需要频繁重新反编译。

---

## 97. 斯特拉皮萨尼庄园迷宫：错综复杂的路径

**原文标题**: The Labyrinth of Villa Pisani in Stra, an Intricate Pathway

**原文链接**: [https://www.finestresullarte.info/en/travel/the-labyrinth-of-villa-pisani-in-stra-suggestions-of-d-annunzio-and-an-intricate-pathway](https://www.finestresullarte.info/en/travel/the-labyrinth-of-villa-pisani-in-stra-suggestions-of-d-annunzio-and-an-intricate-pathway)

本文探寻意大利斯特拉皮萨尼别墅的迷宫，着重介绍了其历史意义、精巧设计和文化关联。皮萨尼别墅，又名“威尼斯别墅女王”，建于18世纪，后曾为拿破仑·波拿巴和哈布斯堡家族所有，之后成为博物馆。

这座迷宫是欧洲最大、最复杂的迷宫之一，在加布里埃尔·邓南遮的小说《火》中有所描绘，为其增添了名气。其设计归功于吉罗拉莫·弗里吉梅利卡，可能受到凡尔赛宫迷宫的启发，由一条蜿蜒的路径通向中央炮塔，炮塔顶端矗立着密涅瓦雕像。传说甚至拿破仑也未能解开它。

本文详细介绍了迷宫的布局，最初旨在为别墅宾客提供娱乐，并描述了女士们如何在炮塔上乔装打扮，挑战绅士们到达那里。它强调了迷宫的难度，因为每个岔路口总是通向死胡同。构成路径的树篱现在主要是黄杨木，取代了最初的角树。

文章最后提到迷宫在20世纪70年代的修复以及它对游客持续的吸引力，游客有时会穿着时代服装来体验其中的挑战。文章还提到，它的结构已被世界各地的迷宫模仿，并且正如邓南遮的小说中所描述的那样，它既能唤起人们的乐趣，又能唤起人们的迷失感。

---

## 98. 被微软分叉

**原文标题**: Getting forked by Microsoft

**原文链接**: [https://philiplaine.com/posts/getting-forked-by-microsoft/](https://philiplaine.com/posts/getting-forked-by-microsoft/)

作为开源项目Spegel的唯一维护者，作者讲述了被微软“分叉”的经历。Spegel的创建是为了解决Kubernetes集群中镜像仓库停机问题，通过启用P2P镜像分发方案来实现。

在微软对Spegel表示兴趣并与作者进行讨论后，他们最终创建了自己的项目Peerd，作者在KubeCon Paris上发现了该项目。虽然Peerd承认了Spegel的影响，但作者发现其中存在大量代码重叠，包括函数签名、注释和测试用例，这些代码似乎直接从Spegel复制而来，且未按照Spegel的MIT许可进行适当的署名。

这种情况在社区中造成了混乱，使得作者难以推广Spegel。这也导致了个人价值被贬低的感觉，并开始质疑Spegel的持续开发。尽管遭遇挫折，Spegel依然取得了成功。

作者提出了关于个体开源维护者如何在不被利用的情况下与大型公司合作的担忧，尤其是在开源环境发生变化、许可变更和投资减少的情况下。作者现在使用GitHub赞助来资助Spegel，并正在考虑更改项目的许可，以更好地保护他们的工作。

---

## 99. Go 中堆分配优化：案例研究

**原文标题**: Optimizing Heap Allocations in Go: A Case Study

**原文链接**: [https://www.dolthub.com/blog/2025-04-18-optimizing-heap-allocations/](https://www.dolthub.com/blog/2025-04-18-optimizing-heap-allocations/)

Go数据库项目Dolt性能衰退：`GetBytes`方法看似无害的重构导致

---

## 100. SaaS是药物发现公司的良好商业模式吗？

**原文标题**: Is SaaS a good business model for drug‑discovery companies?

**原文链接**: [https://liorz.github.io/blog/posts/saas_drug_discovery/](https://liorz.github.io/blog/posts/saas_drug_discovery/)

该文章质疑药物研发公司采用AlphaFold2等人工智能基础模型，并以纯SaaS模式运营的可行性。虽然计算蛋白质设计方面的进展令人印象深刻，但作者认为，仅仅以SaaS平台的形式向制药公司授权这些模型是一种薄弱的策略。

核心问题在于人工智能模型的优势与药物开发中的真正痛点之间存在脱节。人工智能擅长于早期分子生成，但制药行业在“死亡之谷”——即将有前景的分子通过临床试验和监管审批——面临着重大挑战。模型构建者（序列、结构）的语言和关注点与药物开发者（ADME、PK/PD、CMC）的语言和关注点大相径庭。

文章强调了verubecestat的失败案例，以此说明一种“模型驱动”的药物在后期临床试验中失败，强调了计算机模拟预测和动物数据并不能保证在人体中获得成功。这促使Recursion和Insitro等人工智能优先的公司拥有自己的分子，通过将药物推进临床来证明其技术。

此外，AlphaFold3复制版本等开源模型的兴起削弱了专有SaaS许可证的定价权。制药公司最关心的是临床成功的概率，而上游工具的SaaS费用并不能显著降低与药物开发相关的下游财务风险。作者的结论是，在人工智能平台能够显著提高后期成功率之前，纯SaaS模式将面临重大障碍。

---

