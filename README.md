# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-18.md)

*最后自动更新时间: 2025-10-18 17:43:24*
## 1. 我们30年前用过的，后来却失去的IDE

**原文标题**: The IDEs we had 30 years ago ... and we lost

**原文链接**: [https://blogsystem5.substack.com/p/the-ides-we-had-30-years-ago-and](https://blogsystem5.substack.com/p/the-ides-we-had-30-years-ago-and)

无法访问文章链接。

---

## 2. 免费编程书籍

**原文标题**: Free Programing Books

**原文链接**: [https://github.com/EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books)

本文介绍由Free Ebook Foundation策划的、涵盖多种语言的免费编程书籍和资源综合列表。该项目最初来源于StackOverflow的列表，现已发展成为一个由社区协作维护的热门GitHub仓库。Free Ebook Foundation是一家非营利组织，致力于促进免费电子书的创作和可持续性，并接受可减税的捐款。

本文档概述了如何为项目做出贡献，鼓励用户通过遵循其贡献指南和行为准则（提供多种语言版本）来改进列表。它还提供了在社交媒体平台上的各种分享选项。

该资源的核心内容包括以下分类列表：

*   **书籍：** 英文书籍按编程语言和主题组织，其他语言的材料按语言组织。
*   **速查表：** 各种语言的速查表集合。
*   **免费在线课程：** 提供多种语言的课程。
*   **交互式编程资源：** 提供用于学习的交互式平台。
*   **问题集与竞争性编程资源：** 用于练习编码技能。
*   **播客与截屏视频：** 按语言分类的教育音频和视频资源。
*   **编程游乐场：** 基于浏览器的编码练习环境。

本文档最后提及了贡献文档的可用翻译版本以及内容的许可信息（CC BY许可）。其核心目标是为希望学习编程的任何人提供易于访问的免费资源。

---

## 3. 耳鸣神经调节器

**原文标题**: Tinnitus Neuromodulator

**原文链接**: [https://mynoise.net/NoiseMachines/neuromodulationTonesGenerator.php](https://mynoise.net/NoiseMachines/neuromodulationTonesGenerator.php)

“耳鸣神经调节器”是一个免费的声音发生器，旨在帮助人们管理耳鸣。它由 Steve Harrison (Tinnitus Works) 和 myNoise 合作创建，提供可定制的听觉体验，旨在掩蔽和疏远用户与耳鸣的联系。

其核心原理是调整滑块以匹配用户的特定耳鸣音调，并以最小的音量找到最佳的掩蔽声音，从而最大限度地减少听觉疲劳。该网站鼓励尝试不同的预设，如“神经黑客”，以及诸如“动画”之类的功能来激活听觉系统。它还提倡一种正念方法，鼓励用户将生成的声音视为一种独特的听觉体验，并在其中找到乐趣，以缓解紧张感并忽略耳鸣。

该网站强调，目标并不总是完全掩蔽，而是将耳鸣融入更令人愉悦的声景中。用户的故事突出了从缓解头痛、提高注意力到聆听后（即使是短时间）完全安静的各种体验。许多用户报告说，通过使用神经调节器，耳鸣感知显着降低，生活质量得到改善。用户还发现该工具对提高注意力以及治疗多动症等神经分化疾病有帮助。该网站由捐款支持。

---

## 4. 1180张根系图

**原文标题**: 1,180 root system drawings

**原文链接**: [https://images.wur.nl/digital/collection/coll13/search](https://images.wur.nl/digital/collection/coll13/search)

CONTENTdm中的这个条目展示了一个包含1180幅描绘根系的图纸集。核心信息是该资源包含一个重要的根系插图视觉档案。该网页明确指出需要Javascript才能充分互动浏览该系列，暗示这些图纸具有互动功能，可能用于浏览、缩放或搜索。本质上，这是一个关于一个现成的数字图书馆资源发布的公告，该资源专注于根系结构的详细描绘。

---

## 5. 事件溯源、CQRS 和微服务：真实金融科技案例

**原文标题**: Event Sourcing, CQRS and Micro Services: Real FinTech Example

**原文链接**: [https://lukasniessen.medium.com/this-is-a-detailed-breakdown-of-a-fintech-project-from-my-consulting-career-9ec61603709c](https://lukasniessen.medium.com/this-is-a-detailed-breakdown-of-a-fintech-project-from-my-consulting-career-9ec61603709c)

本文详细介绍了一个金融科技项目，该项目通过实施事件溯源、CQRS 和微服务来解决实时交易平台中的可审计性和可扩展性挑战。

客户是一家中型金融科技公司，需要其 MVP 符合金融法规（可审计性）并能处理高使用率（可扩展性）。解决方案包括将单体 Spring Boot 后端分解为微服务。

**事件溯源**在交易组合服务中实施，以确保完整的审计追踪。保存的是事件而非更新状态，从而可以重建过去的状态。这提供了完全的透明度，这对于合规性至关重要。优点包括重建状态、重播事件和调整不正确的过去事件的能力。虽然考虑了审计日志、变更数据捕获 (CDC) 和时态表等替代方案，但事件溯源提供了卓越的细节和控制。

**CQRS（命令查询职责分离）**用于分离读写操作。这使得读写资源能够独立扩展，并为每种操作采用不同的数据模型。读取端使用非规范化的、优化的读取模型来生成复杂的报告。使用了单独的数据库，分别为读取（ClickHouse）和写入（PostgreSQL）进行了优化。必须管理最终一致性，这是 CQRS 常见的问题。缓存和只读副本是替代方案。

**微服务**的选择是为了实现独立的扩展性和容错能力。服务根据业务能力进行分离，例如交易组合、通知、社交、报告和用户服务。实施了异步消息传递来实现服务间的通信，以提高容错能力。迁移采用了绞杀藤模式，逐步替换单体的一部分。服务边界经过仔细考虑，通过合并交易和组合服务避免了分布式事务。

文章最后讨论了事件溯源的优势和挑战，强调了其写入性能并提供了一个查询示例。主要挑战是事件重播期间的性能下降，这可能发生在从数千个事件重建当前状态时。

---

## 6. 注意力是一种奢侈品

**原文标题**: Attention Is a Luxury Good

**原文链接**: [https://seths.blog/2025/10/attention-is-a-luxury-good/](https://seths.blog/2025/10/attention-is-a-luxury-good/)

注意力：一种现代奢侈品

---

## 7. Liva AI (YC S25) 正在招聘

**原文标题**: Liva AI (YC S25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/liva-ai/jobs/inrUYH9-founding-engineer](https://www.ycombinator.com/companies/liva-ai/jobs/inrUYH9-founding-engineer)

Liva AI (YC S25) 是一家致力于通过构建丰富的人类语音和视频数据资料库来创建逼真 AI 的初创公司，现正寻求一位创始工程师加入他们在旧金山的团队。该职位提供 14 万美元至 25 万美元的年薪以及 0.50% 至 2.00% 的股权。

创始工程师将全面负责涉及 AI 数据收集、验证和质量保证的项目。工作内容包括平台工程和基础设施开发，例如构建数据收集平台（Web 和移动应用程序）、设计自动化 QA 流程，以及改进标注平台。该工程师还将参与开发 AI 代理驱动的工作流程，以实现运营自动化。

主要职责包括设计和构建数据收集平台、构建强大的 QA 流程、领导运营流程的自动化，以及参与代码审查和技术设计讨论。

所需技能包括快速交付能力、适应性、Node.js/TypeScript、Python 和 React/Next.js 方面的扎实编码基础、Web 应用程序（最好还有移动应用程序）的构建经验、熟悉 AWS、数据库和 API 设计，以及强大的沟通能力。拥有标注平台或移动应用开发经验者优先。

福利包括每日午餐和晚餐、免费健身房会员资格和健康保险，以及有机会成为一家快速发展的 YC 支持公司的早期成员。Liva AI 成立于 2025 年，总部位于旧金山，是 Y Combinator S25 批次成员。创始人为 Ashley Mo 和 Aoi Otani。

---

## 8. ./观看

**原文标题**: ./watch

**原文链接**: [https://dotslashwatch.com/](https://dotslashwatch.com/)

无法访问文章链接。

---

## 9. 谁发明了深度残差学习？

**原文标题**: Who invented deep residual learning?

**原文链接**: [https://people.idsia.ch/~juergen/who-invented-residual-neural-networks.html](https://people.idsia.ch/~juergen/who-invented-residual-neural-networks.html)

本文由于尔根·施密德胡伯于2025年以未来视角撰写，探讨了深度残差学习的历史和发明，这是现代人工智能的一个基础概念。核心论点是，残差连接这一训练极深神经网络的关键思想，可以追溯到1991年塞普·霍赫赖特在施密德胡伯指导下的毕业论文。该论文引入了权重为1.0的循环残差连接，以解决深度学习中的一个关键挑战——梯度消失问题。

文章追溯了这一概念通过长短期记忆（LSTM）网络的演变，LSTM网络结合了循环残差连接，以及1999年对这些连接的门控版本的开发。它强调了2005年展开LSTMs如何将循环残差连接转化为前馈残差连接。

文章随后讨论了Highway Networks（2015），它将RNN中的门控残差连接应用于前馈网络，从而可以训练更深的FNNs。文章认为，ResNets（2015）本质上是开放式门控Highway Networks，强调两者都共享残差连接的底层原理，以促进深度误差传播。

施密德胡伯强调，真正的残差连接必须具有1.0的权重，才能有效对抗梯度消失/爆炸问题。文章最后断言，LSTM和Highway Networks是关键创新，分别实现了极深RNNs和FNNs的开发，并重申了1991年循环残差连接发现的基础性作用。

---

## 10. 你应该避免的SQL反模式

**原文标题**: SQL Anti-Patterns You Should Avoid

**原文链接**: [https://datamethods.substack.com/p/sql-anti-patterns-you-should-avoid](https://datamethods.substack.com/p/sql-anti-patterns-you-should-avoid)

无法访问文章链接。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 2 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 3 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 4 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 5 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 6 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 7 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 8 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 9 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 10 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 11 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 12 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 13 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 14 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 15 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 16 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 17 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 18 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 19 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 20 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 21 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 22 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 23 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 24 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 25 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 26 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 27 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 28 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 29 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 30 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 31 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 32 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 33 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 34 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 35 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 36 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 37 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 38 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 39 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 40 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 41 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 42 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 43 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 44 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 45 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 46 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 47 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 48 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 49 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 50 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 51 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 52 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 53 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 54 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 55 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 56 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 57 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 58 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 59 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 60 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 61 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 62 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 63 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 64 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 65 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 66 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 67 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 68 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 69 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 70 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 71 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 72 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 73 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 74 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 75 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 76 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 77 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 78 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 79 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 80 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 81 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 82 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 83 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 84 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 85 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 86 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 87 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 88 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 89 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 90 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 91 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 92 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 93 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 94 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 95 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 96 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 97 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 98 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 99 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 100 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 101 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 102 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 103 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 104 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 105 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 106 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 107 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 108 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 109 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 110 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 111 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 112 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 113 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 114 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 115 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 116 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 117 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 118 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 119 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 120 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 121 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 122 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 123 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 124 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 125 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 126 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 127 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 128 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 129 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 130 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 131 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 132 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 133 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 134 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 135 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 136 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 137 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 138 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 139 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 140 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 141 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 142 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 143 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 144 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 145 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 146 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 147 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 148 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 149 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 150 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 151 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 152 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 153 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 154 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 155 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 156 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 157 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 158 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 159 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 160 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 161 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 162 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 163 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 164 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 165 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 166 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 167 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 168 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 169 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 170 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 171 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 172 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 173 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 174 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 175 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 176 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 177 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 178 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 179 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 180 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 181 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 182 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 183 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 184 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 185 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 186 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 187 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 188 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 189 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 190 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 191 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 192 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 193 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 194 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 195 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 196 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 197 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 198 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 199 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 200 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 201 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 202 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 203 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 204 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 205 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 206 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 207 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 208 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 209 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 210 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 211 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 212 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 213 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
