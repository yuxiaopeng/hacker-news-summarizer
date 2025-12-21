# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-21.md)

*最后自动更新时间: 2025-12-21 17:45:07*
## 1. 不成名的理由 (2020)

**原文标题**: Reasons Not to Become Famous (2020)

**原文链接**: [https://tim.blog/2020/02/02/reasons-to-not-become-famous/](https://tim.blog/2020/02/02/reasons-to-not-become-famous/)

在《成名的坏处》中，蒂姆·费里斯（Tim Ferriss）回顾了他13年的心路历程：从最初试图通过成名来治愈自我厌恶，到如今不得不应对身为公众人物所带来的种种不安现实。尽管他承认成名带来了巨大的好处——如资助医学研究、建立有影响力的人脉以及支持慈善事业——但费里斯警告说，成名是一场“浮士德式的交易”，伴随着严峻且往往隐秘的代价。

其核心论点是一个统计学上的比喻：随着受众从一个小规模且可控的“部落”成长为一座拥有数百万人的“城市”，不稳定个体的出现便成了数学上的必然。他认为，无论创作者的行为如何，只要样本量足够大，就不可避免地会出现跟踪者、敲诈者和精神病发作的个体。费里斯分享了一些令人心惊胆战的个人经历来佐证这一点，包括收到粉丝的自杀视频、应对追踪其住址和行程的跟踪者，以及定期收到需要动用私家侦探和武装保安的死亡威胁。

费里斯对名气的过度美化提出了质疑，并呼应了比尔·默里（Bill Murray）的建议：“先试着变富有吧”，因为财富并不像成名那样是一份“24小时不停歇的工作”，也没有与之相关的安全风险。他强调，一旦留下了公众印记，就几乎不可能“将挤出的牙膏再装回管子里”。

最终，这篇文章为那些利用TikTok等现代平台追求快速曝光的人敲响了警钟。费里斯敦促那些渴望成为影响力人物的人去评估，他们的目标是否真的需要成名，还是他们只是在对着错误的墙爬梯子。他的结论是：虽然拥有庞大受众的回报可能会改变人生，但对个人隐私、心理健康和人身安全造成的损害是一个沉重的代价。

---

## 2. ARIN 公开事件报告 — 4.10 错误签发

**原文标题**: ARIN Public Incident Report – 4.10 Misissuance Error

**原文链接**: [https://www.arin.net/announcements/20251212/](https://www.arin.net/announcements/20251212/)

2025年12月2日，ARIN（美洲网络号码注册局）在进行4.10过渡空间分配时，由于依赖手动、离线的库存管理流程，误将已分配给现有客户的IPv4地址块（23.150.164.0/24）重新签发给了新的申请者。

由于一名分析师在使用旧版Excel“电子台账”时错误地将该地址块识别为可用，导致原客户的注册记录和路由来源授权（ROA）被删除，该地址块被分配给了另一家机构。此错误持续了七天，直到原客户于12月9日报告了该异常。ARIN随后采取行动，为原持有者恢复了资源，向新申请者签发了替代地址块，并协调撤回了错误的路由公告。

根本原因是工作流程碎片化，将在线系统与离线电子表格混用，缺乏防止此类重叠所需的统一可见性和自动化保障措施。

**缓解措施与未来行动：**
*   **即时控制：** ARIN已对所有网络删除操作实施了强制性的双重审核流程，并将此类任务限制在少数高级分析师范围内。
*   **系统改进：** ARIN正加速向全自动化、集成化的在线库存架构转型。这将消除离线文件，并引入基于业务规则的警告（特别是感知ROA的警报），以防止误删活跃资源。
*   **自动化：** 该机构计划快轨推进高风险库存签发的自动化，以减少“转椅式”人工操作流程中的人为错误。

---

## 3. Show HN：2025 年 Hacker News 上提及的书籍

**原文标题**: Show HN: Books mentioned on Hacker News in 2025

**原文链接**: [https://hackernews-readings-613604506318.us-west1.run.app](https://hackernews-readings-613604506318.us-west1.run.app)

这篇“Show HN”帖子介绍了 **HackerNews Readings** 项目，该项目致力于追踪并汇总 2025 年整个 Hacker News 社区中提到的书籍推荐。

该工具为这个以技术为核心的社区提供了一个发现引擎，捕捉评论区和帖子中讨论的各种书名。鉴于 Hacker News 用户以推荐高质量且往往较为小众的读物而闻名——涵盖从深度技术解析、数学到科幻和哲学的各个领域——该资源将这些零散的提及集中化，以便于用户查阅。

**核心特点包括：**
*   **集中追踪：** 自动化处理每日数以千计的评论，挖掘其中隐藏的书籍信息。
*   **社区驱动策展：** 清单反映了 2025 年 Hacker News 受众的特定兴趣和智力趋势。
*   **书迷必备资源：** 为开发者、工程师和创业者提供了一个获取同行认可阅读材料的便捷渠道。

简而言之，“HackerNews Readings”在 HN 的海量讨论与寻求社区背书书籍建议的读者之间架起了一座桥梁。

---

## 4. E.W.Dijkstra 档案馆

**原文标题**: E.W.Dijkstra Archive

**原文链接**: [https://www.cs.utexas.edu/~EWD/welcome.html](https://www.cs.utexas.edu/~EWD/welcome.html)

**E.W. 迪杰斯特拉档案馆**（The E.W. Dijkstra Archive）是一个致力于记录埃兹赫尔·W·迪杰斯特拉（Edsger W. Dijkstra，1930–2002）生平与成就的数字化资源库。迪杰斯特拉是计算科学的奠基人，曾获 ACM 图灵奖。他因在算法设计、操作系统、分布式处理和形式化验证领域的开创性贡献而享誉全球。

该档案馆的核心内容是 **“EWDs”** 系列——这是迪杰斯特拉在四十多年间撰写的 1000 多篇技术笔记、出差报告和富有见地的评论。尽管其中许多手稿在他生前曾非正式流传，但大多数从未出版且难以引用。该档案馆由德克萨斯大学奥斯汀分校管理，提供这些文档的 PDF 版本，以确保科学界能够持续获取并利用这些宝贵资料。

网站的主要功能包括：
*   **可检索索引：** BibTeX 和专用索引允许用户通过编号、标题或出版年份查找手稿。
*   **誊录与** 通过持续的志愿者协作，为视障人士提供可搜索的文本，并将荷兰语手稿翻译成英语、西班牙语和俄语。
*   **多媒体与资源：** 网站托管了迪杰斯特拉讲座、访谈的音视频记录，以及同事们撰写的各种生平回忆。
*   **遗产信息：** 重点展示了相关荣誉，如**埃兹赫尔·W·迪杰斯特拉分布式计算奖**以及在德克萨斯大学奥斯汀分校举办的一年一度的纪念讲座。

虽然数字档案馆提供了广泛的查阅渠道，但原始纸质手稿、通信和日记均保存在德克萨斯大学奥斯汀分校的布里斯科美国历史中心（Briscoe Center for American History）。该网站目前仍是一个协作项目，欢迎社区成员贡献力量，参与校对、摘要撰写和交叉引用。

---

## 5. Show HN: WalletWallet – 将任何内容转化为 Apple 票证

**原文标题**: Show HN: WalletWallet – create Apple passes from anything

**原文链接**: [https://walletwallet.alen.ro/](https://walletwallet.alen.ro/)

**WalletWallet** 是一款免费的基于浏览器的工具，旨在将实体条形码和会员卡转换为 Apple 钱包（Apple Wallet）数字凭证。该工具注重易用性与隐私保护，无需安装软件、注册用户或创建账户。

整个过程分为三个简单步骤：
1. **数据输入：** 用户输入会员卡或积分卡的条形码信息。
2. **个性化定制：** 用户配置视觉外观，包括标签和标题。
3. **下载：** 该工具会生成一个标准的 `.pkpass` 文件，可供下载并直接添加到 Apple 钱包应用中。

通过完全在浏览器中运行，WalletWallet 为将实体卡片转换为适配移动端的数字化格式提供了一种私密且高效的方案。

---

## 6. 结构化输出产生虚假信心

**原文标题**: Structured Outputs Create False Confidence

**原文链接**: [https://boundaryml.com/blog/structured-outputs-create-false-confidence](https://boundaryml.com/blog/structured-outputs-create-false-confidence)

在《结构化输出产生虚假信心》一文中，Sam Lijin 指出，虽然结构化输出 API 和受限解码确保了数据的一致性，但它们显著降低了大语言模型（LLM）回答的实际质量和准确性。通过强迫模型优先考虑僵化的格式而非正确性，开发者往往在用智能换取一种虚假的可靠感。

Lijin 指出了结构化输出的几个关键缺陷：

*   **准确性下降：** 约束可能迫使模型选择“合法”但错误的 Token。例如，为了满足严格的模式（Schema），模型可能会将小数四舍五入为整数，而自由格式的输出本可以捕捉到正确的值。
*   **错误处理不力：** 结构化输出剥夺了模型拒绝任务或标记无效输入的能力。如果用户提供了毫无意义的数据（例如在提取收据的任务中提供一张大象的照片），受限模型会生成一个符合模式但毫无意义的对象，而不是报错。
*   **推理能力受损：** 思维链（CoT）推理的有效性降低。强迫模型在 JSON 字段内进行推理，会使其在处理格式化任务（如转义换行符和引号）上消耗“智能预算”，而不是专注于问题本身的逻辑。
*   **技术限制：** 从技术上讲，受限解码在 Token 采样过程中起到了过滤器的作用。如果最“准确”的 Token 被模式禁用，模型将被迫选择次优的替代方案。

Lijin 总结认为，最佳方法是让大模型以自然文本形式自由回答，然后使用“模式对齐解析”（Schema-aligned parsing）来提取必要的数据。这种方法保留了模型进行推理、提供警告和维持高质量输出的能力，同时依然能交付软件系统所需的结构化结果。

---

## 7. ELF 罪行：程序解释器的乐趣

**原文标题**: ELF Crimes: Program Interpreter Fun

**原文链接**: [https://nytpu.com/gemlog/2025-12-21](https://nytpu.com/gemlog/2025-12-21)

在《ELF 罪行：程序解释器的乐趣》一文中，作者探讨了 ELF 可执行格式中 `PT_INTERP` 段的非常规用法。通常，该段指定了动态链接器（如 `ld-linux.so`）的路径，操作系统会将其与可执行文件一同加载到内存中以处理库链接。然而，作者指出，操作系统加载器并不关心解释器的实际功能；它只是简单地加载这两个二进制文件，并将控制权移交给解释器。

作者利用这一特性将 ELF 文件视为一种自包含的数据格式。在这种“邪门”的实现中，ELF 文件包含的是原始数据而非机器代码，其 `PT_INTERP` 段指向一个专门用于处理该数据的自定义“解释器”。这使得数据文件可以直接从 shell 执行，而无需依赖文件扩展名或 MIME 类型。

技术实现过程经历了从手工十六进制编辑到使用链接脚本和 `objcopy` 的转变。其中一个主要的障碍是文档说明不足的

最终的概念验证成功加载了一个包含字符串的“数据”ELF，并通过自定义解释器将其打印出来。尽管实验成功，但作者强烈建议不要在实际应用中使用此方法。该方法依赖于特定架构，存在数据与解释器之间内存冲突的风险，且移植性远不如 Shebang (`#!`) 或 Linux 的 `binfmt_misc` 等标准替代方案。归根结底，该项目是对操作系统加载器机制和 ELF 格式灵活性的一次教学性质的深入探究。

---

## 8. Coarse Is Better

**原文标题**: Coarse Is Better

**原文链接**: [https://borretti.me/article/coarse-is-better](https://borretti.me/article/coarse-is-better)

生成摘要时出错

---

## 9. Show HN: Jmail – Google Suite for Epstein files

**原文标题**: Show HN: Jmail – Google Suite for Epstein files

**原文链接**: [https://www.jmail.world](https://www.jmail.world)

生成摘要时出错

---

## 10. I Program on the Subway

**原文标题**: I Program on the Subway

**原文链接**: [https://www.scd31.com/posts/programming-on-the-subway](https://www.scd31.com/posts/programming-on-the-subway)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 2 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 3 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 4 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 5 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 6 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 7 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 8 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 9 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 10 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 11 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 12 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 13 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 14 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 15 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 16 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 17 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 18 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 19 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 20 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 21 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 22 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 23 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 24 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 25 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 26 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 27 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 28 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 29 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 30 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 31 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 32 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 33 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 34 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 35 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 36 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 37 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 38 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 39 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 40 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 41 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 42 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 43 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 44 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 45 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 46 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 47 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 48 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 49 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 50 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 51 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 52 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 53 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 54 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 55 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 56 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 57 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 58 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 59 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 60 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 61 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 62 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 63 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 64 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 65 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 66 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 67 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 68 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 69 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 70 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 71 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 72 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 73 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 74 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 75 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 76 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 77 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 78 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 79 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 80 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 81 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 82 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 83 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 84 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 85 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 86 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 87 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 88 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 89 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 90 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 91 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 92 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 93 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 94 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 95 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 96 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 97 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 98 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 99 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 100 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 101 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 102 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 103 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 104 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 105 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 106 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 107 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 108 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 109 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 110 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 111 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 112 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 113 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 114 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 115 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 116 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 117 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 118 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 119 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 120 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 121 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 122 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 123 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 124 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 125 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 126 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 127 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 128 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 129 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 130 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 131 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 132 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 133 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 134 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 135 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 136 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 137 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 138 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 139 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 140 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 141 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 142 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 143 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 144 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 145 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 146 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 147 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 148 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 149 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 150 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 151 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 152 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 153 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 154 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 155 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 156 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 157 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 158 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 159 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 160 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 161 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 162 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 163 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 164 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 165 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 166 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 167 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 168 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 169 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 170 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 171 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 172 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 173 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 174 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 175 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 176 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 177 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 178 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 179 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 180 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 181 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 182 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 183 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 184 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 185 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 186 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 187 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 188 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 189 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 190 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 191 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 192 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 193 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 194 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 195 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 196 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 197 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 198 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 199 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 200 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 201 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 202 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 203 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 204 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 205 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 206 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 207 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 208 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 209 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 210 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 211 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 212 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 213 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 214 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 215 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 216 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 217 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 218 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 219 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 220 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 221 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 222 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 223 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 224 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 225 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 226 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 227 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 228 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 229 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 230 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 231 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 232 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 233 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 234 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 235 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 236 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 237 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 238 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 239 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 240 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 241 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 242 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 243 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 244 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 245 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 246 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 247 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 248 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 249 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 250 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 251 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 252 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 253 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 254 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 255 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 256 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 257 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 258 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 259 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 260 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 261 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 262 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 263 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 264 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 265 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 266 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 267 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 268 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 269 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 270 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 271 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 272 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 273 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 274 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 275 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 276 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
