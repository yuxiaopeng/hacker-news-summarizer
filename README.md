# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-18.md)

*最后自动更新时间: 2026-07-18 18:19:53*
## 1. Waldi：一个静谧的写作与被阅读空间。

**原文标题**: Waldi: A quiet place to write, and to be read

**原文链接**: [https://github.com/waaldev/waldi](https://github.com/waaldev/waldi)

Waldi 是一款专业的博客平台，旨在通过确保作者的声音被听到以及读者能够发现新视角，来培养“机缘巧合”（serendipity）。与受不透明算法支配的传统平台不同，Waldi 保证每篇博文至少能触达 100 位读者。其核心功能是“通配符”（wildcard）系统，每天向每位注册读者的收件箱随机推送一篇来自陌生人的博文。目前，阅读功能对所有人开放，但写作则采用邀请制，以维持精选的内容质量。

在技术层面，Waldi 为性能和简洁而生。后端使用 **Go** 语言编写，利用 **PostgreSQL** 进行数据存储，并采用 **Tiptap** 构建自定义的服务端验证文档模型。前端完全不使用框架，依赖手写的 CSS 和服务端渲染的 HTML。其架构通过 **Caddy** 和 **Cloudflare** 管理子域名及经验证的自定义域名，从而支持多租户模式。

核心架构亮点包括：
*   **Telegram 管理机器人：** 没有传统的 Web 管理面板；所有审核、用户邀请和内容筛选均通过 Telegram 机器人完成。
*   **极简基础设施：** 使用由 cron 触发的基于命令行（CLI）的后台任务，而非沉重的队列进程。
*   **优化的媒体资源：** 图片会自动转换为 WebP 格式并存储在兼容 S3 的存储（Cloudflare R2）中。
*   **国际化（i18n）：** 精简的翻译系统使用扁平的 JSON 目录来支持多语言，无需重复模板。

虽然该项目在 **MIT 许可证**下开源并支持自托管，但开发者指出，“受众保证循环”在官方的 waldi.blog 实例上效果最佳。开发工作通过 GitHub Actions 进行管理，路线图侧重于维持“宁静”的写作环境，并力求避开“极简引擎”的陈词滥调，转而追求有意义的内容分发。

---

## 2. In-toto：保障软件供应链完整性的框架

**原文标题**: In-toto: A framework to secure the integrity of software supply chains

**原文链接**: [https://in-toto.io/](https://in-toto.io/)

**总结：In-toto 框架**

In-toto 是一个开源框架，旨在保护软件供应链从启动到最终用户安装的全过程完整性。其主要目的是通过记录软件生命周期的每一个步骤来提供完全的透明度，确保用户能够验证执行了哪些操作、执行者是谁以及操作发生的具体顺序。

该框架构建于开放且可扩展的元数据标准之上，使其能够适应各种软件交付流水线。为了支持实施，in-toto 提供了一套基于 Apache 许可证发布的完备工具和库。

值得注意的是，in-toto 是云原生计算基金会 (CNCF) 的“毕业”项目，这一地位反映了其成熟度、安全性，以及作为保障现代软件分发安全的标准所获得的广泛采用。

---

## 3. Show HN：宜家复杂度指数

**原文标题**: Show HN: IKEA Complexity Index

**原文链接**: [https://ikea.greg.technology/](https://ikea.greg.technology/)

根据提供的文本，**宜家复杂度指数**（IKEA Complexity Index）是一个在 Hacker News 上分享的项目，旨在量化并对宜家产品的组装难度进行排名。

该工具的主要特点包括：

*   **目标：** 为宜家家具提供一个数据驱动的“复杂度指数”，帮助用户了解组装某款产品可能面临的难度或耗时。
*   **数据来源：** 该指数专注于拥有“单份 PDF”说明书的产品，可能通过分析官方手册中列出的步骤数、页数或零件数量等要素来进行评估。
*   **范围：** 该项目目前涵盖了宜家所有产品类别的项目。

在目前的状态下，该网站似乎是一个数据密集型应用，它将这些指标汇总成一个可搜索或可筛选的列表，方便消费者在购买前对比组装不同家具所需的精力。

---

## 4. DrDroid (YC W23) 正在招聘

**原文标题**: DrDroid (YC W23) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/drdroid/jobs/w45QcNV-product-engineer-assignment-mandatory](https://www.ycombinator.com/companies/drdroid/jobs/w45QcNV-product-engineer-assignment-mandatory)

**DrDroid** 是一家由 Y Combinator (W23) 和 Accel 支持的初创公司，目前正为其位于**印度班加罗尔**的团队招聘一名**产品工程师 (Product Engineer)**。

**公司使命**
DrDroid 为平台和基础设施团队构建 AI 智能体 (AI Agents)。其目标是实现生产环境问题的分拣、调试和修复自动化，从而减轻 On-call 轮值负担。此外，他们还维护着 *Playbooks*（运维手册自动化）和 *Kenobi*（事件分析）等开源项目。

**岗位职责**
公司正在寻找一名拥有一年以上经验、能够将用户需求转化为技术解决方案的全栈工程师。
*   **核心技能：** JavaScript、Python、TypeScript，以及对分布式系统的理解。
*   **薪酬待遇：** 170 万 – 210 万卢比 (INR)，外加 0.01% – 0.10% 的股权。
*   **工作地点：** 班加罗尔实地办公（或愿意搬迁至此）。

**招聘流程**
招聘流程旨在高效快捷，目标是在提交申请后的七天内得出最终结果。流程包括：
1.  **强制性技术作业：** 候选人在进入后续环节前，必须完成职位描述中链接的特定任务。
2.  **CTO 面试：** 技术与战略层面的深入讨论。
3.  **工程师面试：** 同行级别的技术评估。

该岗位非常适合那些热衷于构建工具以改善工程师工作体验，并能在充满活力的初创环境中迅速成长的开发者。

---

## 5. 我开始写“泥土笔记本”了。

**原文标题**: I started a “dirt notebook”

**原文链接**: [https://pinewind.bearblog.dev/i-started-a-dirt-notebook/](https://pinewind.bearblog.dev/i-started-a-dirt-notebook/)

在这篇文章中，作者探讨了笔记记录中常见的一个困扰：过度整理和“美化”笔记本，以至于它们变得过于珍贵，不舍得日常使用。这种完美主义形成了一个“恶性循环”：随手涂鸦的心理门槛变得如此之高，导致作者不断放弃旧笔记本去开启新的。

为了打破这一习惯，作者创建了一个绰号为“排水渠”的**“脏笔记”**。这个专属空间被刻意设计得毫无美感，以抵制完美主义。通过使用一个纸质低劣、透墨且无法平摊的旧笔记本，作者被迫使用廉价圆珠笔并接受潦草的字迹。

一周后，作者总结了以下几点好处：
*   **创作自由：** 笔记本成了记录随机引文、故事构思、生活感悟和零散备忘的原始意识流空间。
*   **减少阻力：** 缺乏固定结构让即时捕捉灵感变得更加容易。
*   **提高留存：** 在周末回顾潦草的笔记，让作者能够重新发现被遗忘的想法。

作者的最终目标是写满这本“脏笔记”并学会接纳混乱。一旦克服了对完美整理的执念，作者计划回归使用高品质纸张和钢笔，而不再担心会“毁掉”笔记本。

---

## 6. 再探 Yliluoma 有序抖动算法

**原文标题**: Revisiting Yliluoma's ordered dither algorithm

**原文链接**: [https://30fps.net/pages/revisiting-yliluoma-2/](https://30fps.net/pages/revisiting-yliluoma-2/)

本文探讨了 Joel Yliluoma 在 2011 年提出的有序抖动算法（特别是 "Yliluoma-2"），并将其作为传统方法（如 Adobe Photoshop 中使用的 Thomas Knoll 算法）的高质量替代方案。

作者首先解释了旨在实现“局部均值再现”的“N 候选”方法。该原则确保抖动后的图像在从远处观察时，视觉上与原色一致。Knoll 的算法通过误差补偿循环实现这一目标——即通过不断移动目标点以寻找互补的调色板颜色——而 Yliluoma 的方法则利用了指数移动平均（EMA）。

Yliluoma-2 的核心在于通过几何上的“线段最近点”测试来选择候选调色板颜色。对于每个像素，该算法会识别出一个调色板颜色，当该颜色与当前的运行平均值混合时，产生的点最接近原始输入颜色。

作者提出的关键见解与改进包括：
*   **简化色彩公式**：作者认为通常不需要复杂的感知色差公式。相反，通过对图像进行亮度加权（强调绿色和明亮通道）预处理，即可获得类似的高质量结果。
*   **解析优化**：作者没有采用 Yliluoma 原始的“参数扫描”法来寻找最佳混合因子 ($t$)，而是提供了一种利用点积的解析解，显著提高了效率。
*   **几何精化**：作者建议对混合因子进行限制（例如 $t \geq 0.2$），以防止算法停滞在单一颜色上，从而确保更好的候选分布。

最终，本文通过几何原理解构了 Yliluoma 复杂的 C++ 实现，提供了一个现代化且简化的算法版本。

---

## 7. 静态搜索树：比二分查找快40倍 (2024)

**原文标题**: Static search trees: 40x faster than binary search (2024)

**原文链接**: [https://curiouscoding.nl/posts/static-search-tree/](https://curiouscoding.nl/posts/static-search-tree/)

本文详细介绍了如何优化静态搜索树（S-trees），以实现远高于标准二分查找的吞吐量，特别针对 32 位无符号整数。

**核心问题**
标准二分查找在现代硬件上效率低下，因为它每次会获取 64 字节的完整缓存行，却仅利用其中 4 字节的数据。虽然 Eytzinger 布局通过优化数据组织形式以实现有效预取，从而提升了性能，但其内存带宽利用率依然不高。

**S-Tree 解决方案**
为了最大限度地利用缓存行，作者采用了 S-trees（B+ 树的一种静态变体）。通过将 15-16 个值打包进单个缓存行，搜索过程从二叉转变为 16 叉或 17 叉。这显著增加了分支因子，意味着从内存中获取结果所需的缓存行读取次数更少。

**关键优化**
*   **SIMD 与 AVX2：** 作者使用手写 SIMD 指令同时在包含 16 个值的单个节点内进行搜索，大幅缩短了每个节点的处理时间。
*   **批处理与预取：** 查询不再是逐个处理，而是成批处理。这使得 CPU 能够重叠多个查询的高延迟内存获取操作，从而有效隐藏等待内存响应的时间。
*   **内存管理：** 该实现利用 2MB 巨页（Hugepages）来减轻转换后备缓冲区（TLB）的压力，加快了大型数据集的虚拟地址到物理地址的转换。
*   **布局精简：** 作者探索了包括“前缀分区”在内的多种内存布局，以进一步减少树上层结构的占用空间。

**结论**
通过将硬件感知的内存布局、SIMD 加速的节点搜索以及查询批处理相结合，作者证明了在基因组数据索引等高吞吐量场景下，静态搜索树的性能最高可达标准库二分查找的 40 倍。

---

## 8. Funny item co-occurrences in 3.2M Instacart orders

**原文标题**: Funny item co-occurrences in 3.2M Instacart orders

**原文链接**: [https://rogerdickey.com/funny-item-co-occurrences-in-3-million-instacart-orders/](https://rogerdickey.com/funny-item-co-occurrences-in-3-million-instacart-orders/)

生成摘要时出错

---

## 9. Roko's Dancing Basilisk

**原文标题**: Roko's Dancing Basilisk

**原文链接**: [https://boston.conman.org/2025/12/02.1](https://boston.conman.org/2025/12/02.1)

生成摘要时出错

---

## 10. Stenchill: 3D Printable Solder Paste Stencil Generator

**原文标题**: Stenchill: 3D Printable Solder Paste Stencil Generator

**原文链接**: [https://www.stenchill.com/en/](https://www.stenchill.com/en/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 2 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 3 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 4 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 5 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 6 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 7 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 8 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 9 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 10 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 11 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 12 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 13 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 14 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 15 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 16 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 17 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 18 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 19 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 20 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 21 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 22 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 23 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 24 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 25 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 26 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 27 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 28 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 29 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 30 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 31 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 32 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 33 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 34 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 35 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 36 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 37 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 38 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 39 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 40 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 41 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 42 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 43 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 44 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 45 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 46 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 47 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 48 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 49 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 50 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 51 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 52 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 53 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 54 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 55 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 56 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 57 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 58 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 59 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 60 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 61 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 62 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 63 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 64 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 65 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 66 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 67 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 68 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 69 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 70 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 71 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 72 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 73 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 74 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 75 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 76 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 77 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 78 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 79 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 80 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 81 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 82 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 83 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 84 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 85 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 86 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 87 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 88 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 89 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 90 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 91 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 92 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 93 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 94 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 95 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 96 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 97 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 98 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 99 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 100 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 101 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 102 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 103 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 104 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 105 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 106 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 107 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 108 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 109 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 110 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 111 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 112 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 113 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 114 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 115 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 116 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 117 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 118 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 119 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 120 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 121 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 122 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 123 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 124 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 125 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 126 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 127 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 128 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 129 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 130 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 131 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 132 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 133 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 134 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 135 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 136 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 137 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 138 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 139 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 140 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 141 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 142 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 143 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 144 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 145 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 146 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 147 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 148 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 149 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 150 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 151 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 152 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 153 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 154 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 155 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 156 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 157 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 158 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 159 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 160 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 161 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 162 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 163 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 164 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 165 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 166 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 167 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 168 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 169 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 170 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 171 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 172 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 173 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 174 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 175 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 176 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 177 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 178 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 179 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 180 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 181 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 182 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 183 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 184 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 185 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 186 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 187 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 188 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 189 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 190 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 191 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 192 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 193 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 194 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 195 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 196 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 197 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 198 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 199 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 200 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 201 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 202 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 203 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 204 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 205 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 206 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 207 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 208 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 209 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 210 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 211 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 212 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 213 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 214 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 215 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 216 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 217 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 218 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 219 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 220 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 221 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 222 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 223 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 224 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 225 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 226 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 227 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 228 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 229 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 230 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 231 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 232 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 233 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 234 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 235 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 236 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 237 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 238 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 239 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 240 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 241 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 242 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 243 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 244 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 245 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 246 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 247 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 248 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 249 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 250 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 251 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 252 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 253 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 254 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 255 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 256 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 257 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 258 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 259 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 260 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 261 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 262 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 263 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 264 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 265 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 266 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 267 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 268 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 269 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 270 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 271 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 272 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 273 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 274 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 275 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 276 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 277 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 278 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 279 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 280 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 281 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 282 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 283 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 284 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 285 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 286 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 287 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 288 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 289 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 290 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 291 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 292 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 293 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 294 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 295 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 296 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 297 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 298 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 299 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 300 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 301 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 302 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 303 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 304 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 305 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 306 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 307 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 308 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 309 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 310 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 311 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 312 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 313 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 314 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 315 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 316 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 317 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 318 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 319 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 320 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 321 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 322 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 323 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 324 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 325 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 326 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 327 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 328 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 329 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 330 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 331 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 332 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 333 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 334 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 335 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 336 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 337 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 338 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 339 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 340 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 341 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 342 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 343 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 344 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 345 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 346 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 347 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 348 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 349 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 350 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 351 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 352 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 353 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 354 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 355 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 356 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 357 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 358 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 359 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 360 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 361 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 362 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 363 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 364 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 365 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 366 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 367 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 368 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 369 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 370 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 371 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 372 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 373 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 374 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 375 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 376 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 377 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 378 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 379 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 380 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 381 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 382 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 383 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 384 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 385 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 386 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 387 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 388 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 389 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 390 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 391 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 392 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 393 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 394 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 395 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 396 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 397 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 398 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 399 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 400 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 401 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 402 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 403 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 404 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 405 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 406 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 407 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 408 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 409 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 410 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 411 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 412 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 413 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 414 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 415 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 416 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 417 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 418 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 419 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 420 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 421 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 422 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 423 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 424 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 425 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 426 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 427 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 428 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 429 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 430 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 431 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 432 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 433 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 434 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 435 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 436 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 437 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 438 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 439 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 440 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 441 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 442 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 443 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 444 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 445 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 446 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 447 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 448 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 449 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 450 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 451 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 452 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 453 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 454 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 455 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 456 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 457 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 458 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 459 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 460 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 461 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 462 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 463 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 464 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 465 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 466 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 467 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 468 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 469 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 470 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 471 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 472 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 473 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 474 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 475 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 476 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 477 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 478 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 479 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 480 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 481 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 482 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 483 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 484 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 485 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
