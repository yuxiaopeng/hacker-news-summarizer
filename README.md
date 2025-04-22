# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-04-22.md)

*最后自动更新时间: 2025-04-22 17:48:15*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 2 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 3 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 4 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 5 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 6 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 7 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 8 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 9 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 10 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 11 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 12 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 13 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 14 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 15 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 16 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 17 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 18 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 19 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 20 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 21 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 22 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 23 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 24 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 25 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 26 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 27 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 28 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 29 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 30 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 31 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 32 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 33 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 34 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
