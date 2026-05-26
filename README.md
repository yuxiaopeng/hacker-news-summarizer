# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-26.md)

*最后自动更新时间: 2026-05-26 19:49:55*
## 1. 停止在提交记录中打广告

**原文标题**: Stop Advertising in Your Commits

**原文链接**: [https://akselmo.dev/posts/stop-advertising-in-your-commits/](https://akselmo.dev/posts/stop-advertising-in-your-commits/)

在《停止在提交信息中打广告》一文中，Akselmo 反对在 Git 提交信息中包含不必要的元数据、签名以及特定工具的品牌标识。作者主张提交日志应当保持整洁、专注，并仅致力于解释代码变更的“内容”和“原因”。

文章的主要观点包括：

*   **冗余元数据：** 作者批评了添加如 “Signed-off-by” 或 “Reported-by” 等签名的习惯，除非项目法律或贡献指南（如 Linux 内核）有严格要求。由于 Git 已在其内部标头中存储了作者和提交者信息，在正文中重复这些内容会产生视觉噪音。
*   **工具广告：** 作者主要不满的是类似于 “Sent from my iPhone” 或由 IDE 和 Git 客户端自动生成的签名。这些签名充当了软件的免费广告，对于阅读项目历史的开发者来说毫无价值。
*   **凌乱与可读性：** 当 `git log` 充斥着多行签名和特定工具的标签时，开发者更难浏览历史记录并理解变更背后的实际逻辑。作者强调，提交信息是为人服务的，而非为了满足工具或开发者的虚荣心。
*   **聚焦内容：** 作者最后指出，开发者应当剥离“废话”，保持信息的专业性。一份优秀的提交信息应当是技术变更的简洁概括，不应受到开发者硬件或软件选择的干扰。

总的来说，这篇文章呼吁一种“极简主义”的提交信息，将清晰度和长期可维护性置于不必要的格式和签名之上。

---

## 2. TIGIT之歌

**原文标题**: The Ballad of TIGIT

**原文链接**: [https://www.owlposting.com/p/the-ballad-of-tigit](https://www.owlposting.com/p/the-ballad-of-tigit)

《TIGIT之歌》记录了TIGIT靶向药物的崛起与惨痛失败。这类药物曾被誉为重磅免疫疗法Keytruda（可瑞达）的潜在继任者。TIGIT在理论上被认为是一种强效的“免疫刹车”；研究人员相信，通过阻断TIGIT，可以同时释放免疫系统的“刹车”并激活“加速器”，从而激发更卓越的抗癌反应。

在罗氏公司tiragolumab极具前景的早期2期临床数据推动下，价值数十亿美元的行业“羊群效应”随之出现。包括默沙东、GSK、吉利德和诺华在内的主要制药巨头纷纷涌入开发，累计在临床试验中招募了近49,000名患者。罗氏凭借其庞大的“SKYSCRAPER”项目一马当先，该项目包含一系列旨在确立市场主导地位的并行3期试验。

然而，临床结果证明是灾难性的。从2022年开始，罗氏的旗舰试验接连未能达到目标。最令人震惊的是，部分数据表明某些TIGIT联合疗法甚至“适得其反”，患者的死亡速度比对照组更快。截至2025年底，包括Arcus和吉利德的“Fc静默”抗体假说在内的其他替代方案也均在3期试验中宣告失败。

到2026年，TIGIT类药物在投资者和研究人员眼中已变得如同“放射性物质”般令人避之不及。罗氏、默沙东和GSK的主要项目纷纷终止，多家生物技术公司的合作关系也随之破裂。尽管投入了超过30亿美元的资金和长达十年的研究，TIGIT假说仍未能实现临床突破。这段往事已成为制药行业盲目从众的警示录：全行业的集体狂热，最终导致了现代肿瘤学领域耗资最巨、最受瞩目的失败之一。

---

## 3. 几款有趣的现代像素字体

**原文标题**: A few interesting modern pixel fonts

**原文链接**: [https://unsung.aresluna.org/a-few-interesting-modern-pixel-fonts/](https://unsung.aresluna.org/a-few-interesting-modern-pixel-fonts/)

本文探讨了几款旨在为现代操作系统还原或改进像素美学的现代矢量字体，并重点介绍了四个值得关注的范例：

*   **Analog Mono**：由 Andrew Gleeson 创作，该字体改进了 20 世纪 90 年代风靡一时的录像机（VCR）和高保真音响（hi-fi）界面字体，修复了以往导致字母降部被迫上移的“低基线”问题。
*   **Coral Pixels**：由吉田久美子（Kumiko Yoshida）设计，该字体融入了“彩边（fringing）”——一种亚像素渲染产生的色彩伪影，以唤起 20 世纪 90 年代至 21 世纪初的数字怀旧感。
*   **Two Slice**：由 Joseph Fatula 创作的极简主义实验性字体，尽管高度仅有两个像素，但仍保持了“一定的可读性”。
*   **Geist Pixel**：由 Vercel 开发，这款字体被定位为实用的系统工具，而非装饰性的新奇产物。作者强调了其“排版严谨性”，并指出许多像素字体常因缩放不当或指标冲突而在实际生产中失效，而 Geist Pixel 则具备专业软件环境所需的精确字距和垂直指标。

文章最后指出，优秀的现代像素字体之所以成功，不仅在于其字形设计，更在于那些能确保其在各种数字视口中可靠运行的“无形”技术工作。

---

## 4. I Bypassed Adobe and Microsoft to Build a Git-Tracked Book Production Pipeline

**原文标题**: I Bypassed Adobe and Microsoft to Build a Git-Tracked Book Production Pipeline

**原文链接**: [https://www.djspeckhals.com/posts/2026-05-22-how-i-bypassed-adobe-and-microsoft-to-build-a-git-tracked-book-production-pipeline/](https://www.djspeckhals.com/posts/2026-05-22-how-i-bypassed-adobe-and-microsoft-to-build-a-git-tracked-book-production-pipeline/)

生成摘要时出错

---

## 5. Xiaomi MiMo-v2.5 Series API Permanent Price Reduction Up to 99%

**原文标题**: Xiaomi MiMo-v2.5 Series API Permanent Price Reduction Up to 99%

**原文链接**: [https://platform.xiaomimimo.com/docs/en-US/news/v2.5-price-update](https://platform.xiaomimimo.com/docs/en-US/news/v2.5-price-update)

生成摘要时出错

---

## 6. Launch HN: Minicor (YC P26) – Windows desktop automations at scale

**原文标题**: Launch HN: Minicor (YC P26) – Windows desktop automations at scale

**原文链接**: [https://www.minicor.com/](https://www.minicor.com/)

生成摘要时出错

---

## 7. Rosalind: A genomics toolkit in Rust running whole-genome pipelines on a laptop

**原文标题**: Rosalind: A genomics toolkit in Rust running whole-genome pipelines on a laptop

**原文链接**: [https://github.com/logannye/rosalind](https://github.com/logannye/rosalind)

生成摘要时出错

---

## 8. Spain blocks prediction markets Polymarket, Kalshi over lack of gambling licence

**原文标题**: Spain blocks prediction markets Polymarket, Kalshi over lack of gambling licence

**原文链接**: [https://www.reuters.com/business/spain-blocks-prediction-markets-polymarket-kalshi-over-lack-gambling-licences-2026-05-26/](https://www.reuters.com/business/spain-blocks-prediction-markets-polymarket-kalshi-over-lack-gambling-licences-2026-05-26/)

生成摘要时出错

---

## 9. C64 Basic: Game Map Overhead "Camera View"

**原文标题**: C64 Basic: Game Map Overhead "Camera View"

**原文链接**: [https://retrogamecoders.com/overhead-camera-view/](https://retrogamecoders.com/overhead-camera-view/)

生成摘要时出错

---

## 10. Sage Care (YC S24) Is Hiring Software Engineers

**原文标题**: Sage Care (YC S24) Is Hiring Software Engineers

**原文链接**: [https://www.ycombinator.com/companies/sagecare/jobs/xtloH8r-senior-software-engineer](https://www.ycombinator.com/companies/sagecare/jobs/xtloH8r-senior-software-engineer)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 2 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 3 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 4 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 5 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 6 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 7 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 8 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 9 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 10 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 11 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 12 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 13 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 14 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 15 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 16 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 17 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 18 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 19 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 20 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 21 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 22 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 23 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 24 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 25 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 26 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 27 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 28 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 29 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 30 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 31 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 32 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 33 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 34 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 35 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 36 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 37 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 38 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 39 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 40 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 41 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 42 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 43 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 44 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 45 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 46 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 47 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 48 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 49 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 50 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 51 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 52 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 53 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 54 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 55 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 56 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 57 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 58 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 59 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 60 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 61 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 62 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 63 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 64 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 65 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 66 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 67 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 68 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 69 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 70 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 71 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 72 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 73 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 74 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 75 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 76 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 77 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 78 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 79 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 80 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 81 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 82 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 83 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 84 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 85 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 86 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 87 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 88 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 89 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 90 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 91 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 92 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 93 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 94 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 95 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 96 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 97 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 98 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 99 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 100 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 101 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 102 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 103 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 104 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 105 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 106 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 107 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 108 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 109 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 110 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 111 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 112 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 113 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 114 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 115 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 116 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 117 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 118 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 119 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 120 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 121 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 122 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 123 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 124 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 125 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 126 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 127 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 128 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 129 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 130 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 131 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 132 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 133 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 134 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 135 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 136 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 137 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 138 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 139 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 140 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 141 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 142 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 143 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 144 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 145 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 146 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 147 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 148 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 149 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 150 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 151 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 152 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 153 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 154 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 155 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 156 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 157 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 158 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 159 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 160 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 161 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 162 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 163 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 164 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 165 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 166 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 167 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 168 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 169 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 170 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 171 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 172 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 173 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 174 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 175 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 176 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 177 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 178 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 179 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 180 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 181 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 182 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 183 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 184 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 185 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 186 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 187 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 188 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 189 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 190 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 191 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 192 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 193 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 194 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 195 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 196 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 197 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 198 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 199 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 200 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 201 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 202 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 203 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 204 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 205 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 206 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 207 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 208 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 209 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 210 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 211 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 212 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 213 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 214 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 215 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 216 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 217 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 218 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 219 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 220 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 221 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 222 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 223 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 224 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 225 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 226 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 227 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 228 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 229 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 230 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 231 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 232 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 233 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 234 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 235 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 236 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 237 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 238 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 239 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 240 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 241 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 242 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 243 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 244 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 245 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 246 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 247 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 248 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 249 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 250 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 251 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 252 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 253 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 254 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 255 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 256 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 257 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 258 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 259 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 260 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 261 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 262 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 263 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 264 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 265 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 266 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 267 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 268 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 269 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 270 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 271 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 272 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 273 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 274 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 275 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 276 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 277 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 278 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 279 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 280 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 281 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 282 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 283 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 284 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 285 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 286 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 287 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 288 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 289 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 290 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 291 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 292 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 293 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 294 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 295 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 296 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 297 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 298 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 299 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 300 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 301 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 302 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 303 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 304 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 305 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 306 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 307 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 308 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 309 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 310 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 311 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 312 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 313 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 314 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 315 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 316 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 317 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 318 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 319 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 320 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 321 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 322 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 323 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 324 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 325 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 326 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 327 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 328 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 329 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 330 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 331 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 332 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 333 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 334 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 335 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 336 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 337 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 338 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 339 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 340 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 341 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 342 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 343 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 344 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 345 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 346 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 347 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 348 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 349 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 350 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 351 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 352 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 353 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 354 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 355 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 356 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 357 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 358 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 359 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 360 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 361 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 362 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 363 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 364 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 365 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 366 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 367 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 368 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 369 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 370 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 371 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 372 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 373 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 374 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 375 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 376 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 377 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 378 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 379 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 380 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 381 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 382 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 383 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 384 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 385 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 386 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 387 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 388 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 389 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 390 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 391 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 392 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 393 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 394 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 395 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 396 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 397 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 398 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 399 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 400 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 401 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 402 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 403 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 404 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 405 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 406 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 407 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 408 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 409 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 410 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 411 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 412 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 413 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 414 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 415 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 416 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 417 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 418 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 419 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 420 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 421 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 422 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 423 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 424 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 425 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 426 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 427 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 428 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 429 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 430 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 431 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 432 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
