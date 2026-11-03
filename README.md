# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-03.md)

*最后自动更新时间: 2026-11-03 00:10:54*
## 1. Astra可以读写权重以提升Qwen。

**原文标题**: Astra can read and write weights to improve Qwen

**原文链接**: [https://rikiyat.github.io/blog/weight-space-programming/](https://rikiyat.github.io/blog/weight-space-programming/)

文章《权重空间编程之火》（Sparks of Weight-Space Programming）详述了一项重大突破：前沿大语言模型——特别是 GPT-6 Astra——展示了在不使用梯度、符号优化器（如 Adam）或环境反馈的情况下，原生地读取、解释和写入神经网络权重的能力。这种被称为“权重空间编程”的新范式表明，大语言模型可以通过刻意的推理来优化可微网络。

关键发现包括：

*   **读取与可解释性：** Astra 仅通过分析原始权重矩阵，就能识别网络的功能，例如其运行的具体游戏或训练所用的语言。在一次实验中，Astra 仅通过阅读中间层权重，就准确识别了 Transformer 中的“复制头”。
*   **零样本权重生成：** Astra 可以从零开始编写功能性神经网络。在 MinAtar 游戏中，Astra 生成的权重表现优于经过 1 亿步 PPO 训练的策略。在物理控制任务中，它通过仅编辑 3.5% 的权重修复了失效策略，成功绕过了局部最小值。
*   **改进前沿模型：** 最显著的是，Astra 提升了 Qwen3.5-0.8B 的数学推理能力。通过识别导致“推理循环”的特定权重问题，Astra 仅修改了 0.016% 的参数。这一针对性修复使 Qwen 的 MATH-500 分数从 7.9% 提升至 48.1%，并使其在 IFEval 基准测试中的表现翻了三倍。

作者总结道，深度学习的历史正从简单的符号优化器向推理驱动型优化转变。在此过程中，大语言模型扮演着神经权重“编译器”或“修复器”的角色，为模型优化和机械可解释性开辟了新的可能性。

---

## 2. Anthropic的增长陷入停滞

**原文标题**: Anthropic's growth just flattened

**原文链接**: [https://www.regenerator1.com/p/anthropics-growth-just-flattened](https://www.regenerator1.com/p/anthropics-growth-just-flattened)

根据亨利·布罗杰特（Henry Blodget）2026年10月发布的一份报告，Anthropic的爆发式增长在2026年第三季度显现出明显放缓的迹象。尽管该公司报告了高达168亿美元的季度营收，但详细分析表明，其增长势头已开始趋于平缓。

**主要财务发现：**
*   **环比增速回落：** 尽管第三季度营收巨大，但52亿美元的绝对增长额低于第二季度的68亿美元。增长率从第二季度的141%降至第三季度的45%。
*   **单月增长停滞：** 根据7月份报告的650亿美元年化营收率（约合单月54亿美元）推算，数据暗示其8月和9月的营收几乎持平。
*   **数据缺失：** 值得注意的是，Anthropic拒绝向投资者提供9月份的年化营收率，这表明该数据不足以支撑其增长叙事。

**市场影响：**
此次增长放缓引发了CoreWeave等“新云（neocloud）”服务商股价的崩盘，这些公司此前通过大量借贷来资助人工智能基础设施建设。随着利率上升和人工智能服务营收增长放缓，债务的“持有成本”正成为投资者关注的焦点。

**潜在原因：**
布罗杰特提出了增长放缓的几点原因：
1.  **季节性因素：** 8月通常是商业活动的淡季。
2.  **产能限制：** 受硬件限制影响，Anthropic可能无法满足市场需求。
3.  **市场转向：** 需求可能正在降温，或者客户正转向来自中国的更廉价的AI模型。

文章总结认为，这种趋于平缓的态势表明，随着供应最终赶上需求，“人工智能泡沫”可能正接近顶峰。

---

## 3. 那些由男名演变为女名以及由女名演变为男名的美国名字

**原文标题**: US boy names that became girl names and vice versa

**原文链接**: [https://namedaisy.com/blog/boy-names-that-became-girl-names](https://namedaisy.com/blog/boy-names-that-became-girl-names)

《美国男名女用及女名男用的历史演变》一文探讨了美国性别化命名习惯的流变，强调了文化中对“男性化”和“女性化”发音的认知如何随时间而变化。

**从男名向女名转变的趋势**
文章指出，命名领域存在一种明显的“单向通行”现象：最初为男孩设计的名字频繁演变为流行的女孩名字。历史上，**Ashley、Beverly、Courtney、Evelyn、Hilary、Joyce、Leslie** 和 **Meredith** 等名字曾是专属或主要的男性姓名。这种转变通常源于父母希望为女儿寻找“强大”或独特的的名字。然而，一旦某个名字在女孩中的流行程度达到“临界点”，通常就会在男孩中失宠，因为社会普遍存在一种偏见，不愿给儿子起任何被视为具有女性色彩的名字。

**麦迪逊效应**
文章以“Madison”为例，该名字从姓氏演变为男名，随后在 1984 年电影《美人鱼》（*Splash*）的影响下，成为了顶尖的女性化选择。这证明了流行文化如何加速名字性别的转变。

**罕见的逆向转变**
虽然“男名女用”很常见，但“女名男用”的情况在美国历史上却罕见得多。大多数朝这个方向演变的名字通常是姓氏或自然类名称，在被用于男孩之前，尚未形成稳固的女性化印象。

**现代中性名字**
尽管历史上存在名字“女性化”后便定型的趋势，但文章指出，现代真正性别中性的命名方式正在兴起。像 **Taylor、Jordan、Morgan、Riley** 和 **Avery** 这样的名字，在过去几十年中成功在两性之间保持了平衡的吸引力。

**总结**
文章最后得出结论：尽管命名的界限正变得更具渗透性，但历史模式依然倾向于“男性名字女性化”，而非相反方向。

---

## 4. Launch HN: Momentic (YC W24) – 通过使用您的应用来发现 Bug 的智能体

**原文标题**: Launch HN: Momentic (YC W24) – Agents that catch bugs by using your app

**原文链接**: [https://momentic.ai/](https://momentic.ai/)

**Momentic (YC W24)** 是一款 AI 驱动的测试平台，利用自主智能体通过模拟人类用户的交互方式来识别软件漏洞。

该平台的效能最近通过发现某消费金融科技应用中的一个关键安全漏洞得到了验证。在对功能分支进行测试时，Momentic 的智能体发现，登录路由的变更导致系统无意中绕过了针对新设备强制执行的双重身份验证（2FA）提示。

由于这一安全校验是被静默跳过的，传统的自动化测试很容易忽略它。通过在代码进入生产环境前识别出该缺陷，Momentic 成功预防了一场重大的安全违规事件，证明了 AI 智能体在维护软件完整性和捕捉复杂逻辑错误方面的价值。

---

## 5. 如果你爱一个网站，请备份它。

**原文标题**: If you love a website, back it up

**原文链接**: [https://blog.mistys-internet.website/post/2026/10/29/if-you-love-a-website-back-it-up/](https://blog.mistys-internet.website/post/2026/10/29/if-you-love-a-website-back-it-up/)

In the article "If you love a website, back it up," a web archiving professional warns of the fragility of the internet, using the disappearance of a beloved niche fansite as a cautionary tale. The author argues that web preservation should not be left solely to large organizations like the Internet Archive; instead, individuals should take proactive responsibility for saving the digital content they value.

The author highlights three primary tools for personal archiving, all of which utilize standard formats like WARC and WACZ:

1.  **ArchiveWeb.page Browser Extension:** The most accessible option, allowing users to manually record pages, interactive elements, and social media posts simply by browsing them.
2.  **ArchiveWeb.page App:** A standalone desktop version of the extension that serves as both a capture tool and a local gallery for viewing archives.
3.  **Browsertrix:** An automated web crawler designed for high-capacity archiving. It is ideal for saving entire domains or complex social media profiles without manual browsing. While it is a paid service, its open-source nature allows technical users to run it independently.

Once a site is archived, it can be viewed privately or shared globally. The author recommends **ReplayWeb.page**, an open-source tool that allows users to embed archived websites directly into blog posts or share portable data files with others. 

The article concludes with a call to action for a decentralized approach to web history. By creating and sharing personal archives, users can ensure that "lots of copies keep stuff safe," protecting digital culture from link rot and domain expiration.

---

## 6. 苹果公布第四季度业绩

**原文标题**: Apple reports fourth quarter results

**原文链接**: [https://www.apple.com/newsroom/2026/11/apple-reports-fourth-quarter-results/](https://www.apple.com/newsroom/2026/11/apple-reports-fourth-quarter-results/)

苹果公司发布了其2026财年第四季度破纪录的财务业绩，营收达到1145亿美元，同比增长12%。稀释后每股收益 (EPS) 增长14%，至2.10美元。这些业绩为苹果公司迄今为止最成功的财年画上了圆满句号，其全年总营收达到4790亿美元的历史新高。

该季度的增长主要受到iPhone创纪录的9月营收以及服务业务营收历史新高的驱动。首席执行官约翰·特努斯 (John Ternus) 强调了几款重大产品的发布，包括具有“变革性”的iPhone Duo、iPhone 18 Pro系列，以及Touch to Mac的推出。他还指出，全新Siri AI的集成以及新型家居硬件是进入假期购物季的关键驱动力。

报告中的财务亮点包括：
*   **毛利率：** 47.9%，受益于关税退税带来的1个百分点影响。
*   **现金流：** 本季度产生了280亿美元的运营现金流。
*   **股东回报：** 向股东返还了280亿美元；宣布派发每股0.27美元的现金股息。
*   **装机量：** 公司在所有产品类别和地理区域的活跃设备数量均创下历史新高。

首席财务官凯文·帕雷克 (Kevan Parekh) 将这一成功归功于极高的客户忠诚度和满意度，并指出公司在整个财年实现了两位数的每股收益增长。

---

## 7. Show HN：体素华沙——市中心交互式 3D 地图

**原文标题**: Show HN: Warsaw in voxels – An interactive 3D map of the city centre

**原文链接**: [https://p.migdal.pl/warsaw-vibe-voxel/](https://p.migdal.pl/warsaw-vibe-voxel/)

该项目名为**“体素华沙” (Warsaw in Voxels)**，是一个展示波兰首都中心地带的交互式 3D 数字地图。该应用近期在 Hacker News 上备受关注，它将城市地理数据转化为独特的体素美学风格，类似于《我的世界》(Minecraft) 等游戏中的方块视觉效果。

通过可导航的三维界面，用户可以探索华沙密集的建筑群和知名地标。该项目通过将传统的城市布局转换为基于体素的环境，为城市设计提供了独特的视角，实现了技术数据可视化与复古风 3D 艺术的融合。目前，该界面支持加载实时地图数据，为用户提供城市核心区域的沉浸式体验。

---

## 8. 美国证券交易委员会应阻止 Anthropic 的 IPO 以保护公众利益。

**原文标题**: The SEC Should Block Anthropic's IPO to Protect the Public

**原文链接**: [https://www.techpolicy.press/the-sec-should-block-anthropics-ipo-to-protect-the-public/](https://www.techpolicy.press/the-sec-should-block-anthropics-ipo-to-protect-the-public/)

生成摘要时出错

---

## 9. Sneaking into the auditorium for the Windows 2000 launch rehearsal

**原文标题**: Sneaking into the auditorium for the Windows 2000 launch rehearsal

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20261102-00/?p=112818/](https://devblogs.microsoft.com/oldnewthing/20261102-00/?p=112818/)

生成摘要时出错

---

## 10. Egoless Mathematics in the AI Era

**原文标题**: Egoless Mathematics in the AI Era

**原文链接**: [https://terrytao.wordpress.com/2026/11/02/egoless-mathematics-in-the-ai-era/](https://terrytao.wordpress.com/2026/11/02/egoless-mathematics-in-the-ai-era/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 2 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 3 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 4 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 5 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 6 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 7 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 8 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 9 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 10 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 11 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 12 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 13 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 14 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 15 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 16 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 17 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 18 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 19 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 20 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 21 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 22 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 23 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 24 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 25 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 26 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 27 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 28 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 29 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 30 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 31 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 32 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 33 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 34 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 35 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 36 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 37 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 38 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 39 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 40 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 41 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 42 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 43 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 44 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 45 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 46 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 47 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 48 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 49 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 50 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 51 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 52 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 53 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 54 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 55 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 56 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 57 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 58 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 59 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 60 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 61 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 62 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 63 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 64 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 65 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 66 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 67 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 68 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 69 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 70 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 71 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 72 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 73 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 74 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 75 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 76 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 77 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 78 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 79 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 80 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 81 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 82 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 83 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 84 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 85 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 86 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 87 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 88 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 89 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 90 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 91 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 92 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 93 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 94 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 95 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 96 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 97 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 98 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 99 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 100 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 101 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 102 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 103 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 104 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 105 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 106 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 107 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 108 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 109 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 110 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 111 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 112 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 113 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 114 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 115 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 116 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 117 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 118 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 119 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 120 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 121 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 122 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 123 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 124 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 125 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 126 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 127 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 128 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 129 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 130 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 131 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 132 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 133 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 134 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 135 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 136 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 137 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 138 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 139 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 140 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 141 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 142 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 143 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 144 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 145 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 146 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 147 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 148 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 149 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 150 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 151 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 152 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 153 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 154 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 155 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 156 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 157 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 158 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 159 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 160 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 161 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 162 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 163 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 164 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 165 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 166 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 167 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 168 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 169 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 170 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 171 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 172 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 173 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 174 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 175 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 176 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 177 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 178 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 179 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 180 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 181 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 182 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 183 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 184 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 185 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 186 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 187 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 188 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 189 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 190 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 191 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 192 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 193 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 194 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 195 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 196 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 197 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 198 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 199 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 200 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 201 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 202 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 203 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 204 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 205 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 206 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 207 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 208 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 209 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 210 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 211 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 212 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 213 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 214 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 215 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 216 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 217 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 218 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 219 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 220 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 221 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 222 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 223 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 224 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 225 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 226 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 227 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 228 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 229 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 230 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 231 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 232 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 233 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 234 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 235 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 236 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 237 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 238 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 239 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 240 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 241 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 242 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 243 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 244 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 245 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 246 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 247 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 248 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 249 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 250 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 251 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 252 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 253 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 254 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 255 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 256 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 257 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 258 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 259 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 260 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 261 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 262 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 263 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 264 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 265 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 266 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 267 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 268 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 269 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 270 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 271 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 272 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 273 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 274 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 275 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 276 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 277 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 278 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 279 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 280 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 281 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 282 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 283 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 284 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 285 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 286 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 287 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 288 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 289 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 290 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 291 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 292 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 293 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 294 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 295 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 296 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 297 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 298 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 299 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 300 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 301 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 302 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 303 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 304 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 305 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 306 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 307 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 308 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 309 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 310 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 311 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 312 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 313 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 314 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 315 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 316 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 317 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 318 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 319 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 320 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 321 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 322 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 323 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 324 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 325 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 326 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 327 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 328 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 329 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 330 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 331 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 332 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 333 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 334 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 335 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 336 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 337 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 338 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 339 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 340 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 341 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 342 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 343 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 344 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 345 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 346 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 347 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 348 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 349 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 350 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 351 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 352 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 353 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 354 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 355 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 356 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 357 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 358 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 359 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 360 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 361 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 362 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 363 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 364 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 365 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 366 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 367 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 368 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 369 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 370 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 371 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 372 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 373 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 374 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 375 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 376 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 377 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 378 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 379 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 380 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 381 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 382 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 383 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 384 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 385 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 386 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 387 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 388 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 389 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 390 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 391 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 392 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 393 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 394 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 395 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 396 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 397 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 398 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 399 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 400 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 401 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 402 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 403 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 404 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 405 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 406 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 407 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 408 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 409 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 410 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 411 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 412 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 413 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 414 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 415 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 416 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 417 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 418 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 419 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 420 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 421 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 422 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 423 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 424 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 425 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 426 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 427 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 428 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 429 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 430 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 431 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 432 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 433 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 434 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 435 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 436 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 437 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 438 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 439 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 440 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 441 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 442 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 443 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 444 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 445 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 446 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 447 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 448 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 449 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 450 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 451 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 452 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 453 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 454 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 455 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 456 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 457 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 458 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 459 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 460 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 461 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 462 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 463 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 464 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 465 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 466 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 467 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 468 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 469 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 470 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 471 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 472 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 473 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 474 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 475 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 476 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 477 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 478 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 479 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 480 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 481 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 482 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 483 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 484 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 485 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 486 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 487 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 488 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 489 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 490 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 491 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 492 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 493 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 494 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 495 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 496 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 497 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 498 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 499 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 500 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 501 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 502 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 503 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 504 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 505 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 506 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 507 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 508 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 509 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 510 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 511 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 512 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 513 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 514 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 515 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 516 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 517 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 518 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 519 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 520 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 521 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 522 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 523 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 524 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 525 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 526 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 527 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 528 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 529 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 530 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 531 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 532 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 533 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 534 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 535 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 536 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 537 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 538 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 539 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 540 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 541 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 542 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 543 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 544 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 545 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 546 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 547 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 548 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 549 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 550 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 551 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 552 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 553 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 554 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 555 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 556 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 557 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 558 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 559 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 560 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 561 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 562 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 563 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 564 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 565 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 566 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 567 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 568 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 569 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 570 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 571 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 572 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 573 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 574 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 575 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 576 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 577 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 578 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 579 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 580 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 581 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 582 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 583 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 584 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 585 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 586 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 587 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 588 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 589 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 590 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
