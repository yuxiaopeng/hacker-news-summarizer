# Hacker News 热门文章摘要 (2026-11-03)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Self-Employed? Solopreneur? NIST Has a Cybersecurity Guide Just for You

**原文标题**: Self-Employed? Solopreneur? NIST Has a Cybersecurity Guide Just for You

**原文链接**: [https://www.nist.gov/news-events/news/2026/11/self-employed-solopreneur-nist-has-cybersecurity-guide-just-you](https://www.nist.gov/news-events/news/2026/11/self-employed-solopreneur-nist-has-cybersecurity-guide-just-you)

生成摘要时出错

---

## 12. Ubuntu still has not released patch for Linux 0day RCE in almost 3 weeks

**原文标题**: Ubuntu still has not released patch for Linux 0day RCE in almost 3 weeks

**原文链接**: [https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432](https://freenode.net/article/ubuntu-lts-kernels-still-unfixed-for-critical-cve-2026-98432)

生成摘要时出错

---

## 13. WTF Ubuntu?

**原文标题**: WTF Ubuntu?

**原文链接**: [https://chalmovsky.com/posts/wtf-ubuntu](https://chalmovsky.com/posts/wtf-ubuntu)

生成摘要时出错

---

## 14. Polyend releases the Tracker firmware source code

**原文标题**: Polyend releases the Tracker firmware source code

**原文链接**: [https://polyend.com/whats-up/tracker-the-biggest-update-yet/](https://polyend.com/whats-up/tracker-the-biggest-update-yet/)

生成摘要时出错

---

## 15. Oracle files to sell $20B in new stock, bonds to finance AI buildout

**原文标题**: Oracle files to sell $20B in new stock, bonds to finance AI buildout

**原文链接**: [https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html](https://www.cnbc.com/2026/11/02/oracle-files-to-sell-20-billion-in-new-stock-bonds-to-finance-ai-buildout.html)

生成摘要时出错

---

## 16. The Ford Privacy Promise: You're in Control of Your Data

**原文标题**: The Ford Privacy Promise: You're in Control of Your Data

**原文链接**: [https://www.fromtheroad.ford.com/us/en/articles/2026/introducing-the-ford-privacy-promise](https://www.fromtheroad.ford.com/us/en/articles/2026/introducing-the-ford-privacy-promise)

生成摘要时出错

---

## 17. Skill to Create Product Videos

**原文标题**: Skill to Create Product Videos

**原文链接**: [https://github.com/aaitor/skill-video-studio](https://github.com/aaitor/skill-video-studio)

生成摘要时出错

---

## 18. Bitmovin (YC S15) Is Hiring Technical Graduates in Denver (Engineering/CS Focus)

**原文标题**: Bitmovin (YC S15) Is Hiring Technical Graduates in Denver (Engineering/CS Focus)

**原文链接**: [https://bitmovin.com/careers/8660599002/](https://bitmovin.com/careers/8660599002/)

生成摘要时出错

---

## 19. A Conversation with Paul Masurel, Creator of Tantivy

**原文标题**: A Conversation with Paul Masurel, Creator of Tantivy

**原文链接**: [https://www.paradedb.com/blog/tantivy-interview](https://www.paradedb.com/blog/tantivy-interview)

生成摘要时出错

---

## 20. When Modernization Breaks Working Code: A Study of LLMs on Legacy PHP

**原文标题**: When Modernization Breaks Working Code: A Study of LLMs on Legacy PHP

**原文链接**: [https://arxiv.org/abs/2610.40269](https://arxiv.org/abs/2610.40269)

生成摘要时出错

---

## 21. We halved DNS build delay and cut memory use by 85%

**原文标题**: We halved DNS build delay and cut memory use by 85%

**原文链接**: [https://blog.cloudflare.com/dns-targeted-zone-builds/](https://blog.cloudflare.com/dns-targeted-zone-builds/)

生成摘要时出错

---

## 22. C64 Basic Dungeon Crawler: Stairs, Levels and Levelling Up (Part 11)

**原文标题**: C64 Basic Dungeon Crawler: Stairs, Levels and Levelling Up (Part 11)

**原文链接**: [https://retrogamecoders.com/c64-basic-dungeon-part11/](https://retrogamecoders.com/c64-basic-dungeon-part11/)

生成摘要时出错

---

## 23. SLAC researchers find proof of altermagnetism, a new magnetic phase

**原文标题**: SLAC researchers find proof of altermagnetism, a new magnetic phase

**原文链接**: [https://www6.slac.stanford.edu/news/2026-10-29-slac-researchers-find-proof-altermagnetism-new-magnetic-phase](https://www6.slac.stanford.edu/news/2026-10-29-slac-researchers-find-proof-altermagnetism-new-magnetic-phase)

生成摘要时出错

---

## 24. LongCat-2.5: Native Multimodality for Agentic Tasks

**原文标题**: LongCat-2.5: Native Multimodality for Agentic Tasks

**原文链接**: [https://longcat.ai/blog/longcat-2.5/](https://longcat.ai/blog/longcat-2.5/)

生成摘要时出错

---

## 25. Making Peace with the Projective Plane

**原文标题**: Making Peace with the Projective Plane

**原文链接**: [https://www.johndcook.com/blog/2026/11/02/projective-plane/](https://www.johndcook.com/blog/2026/11/02/projective-plane/)

生成摘要时出错

---

## 26. Moving our warehouse off DuckDB

**原文标题**: Moving our warehouse off DuckDB

**原文链接**: [https://posthog.com/blog/moving-off-duckdb](https://posthog.com/blog/moving-off-duckdb)

生成摘要时出错

---

## 27. Agentic backdoors via pretraining poisoning

**原文标题**: Agentic backdoors via pretraining poisoning

**原文链接**: [https://arxiv.org/abs/2610.37741](https://arxiv.org/abs/2610.37741)

生成摘要时出错

---

## 28. BYD sold more EVs last month than the US did all quarter

**原文标题**: BYD sold more EVs last month than the US did all quarter

**原文链接**: [https://electrek.co/2026/11/02/byd-sold-more-evs-last-month-than-the-us-did-all-quarter/](https://electrek.co/2026/11/02/byd-sold-more-evs-last-month-than-the-us-did-all-quarter/)

生成摘要时出错

---

## 29. Show HN: I've updated my Linux System Call website and API

**原文标题**: Show HN: I've updated my Linux System Call website and API

**原文链接**: [https://syscall.sh/](https://syscall.sh/)

生成摘要时出错

---

## 30. My Favourite Laptop

**原文标题**: My Favourite Laptop

**原文链接**: [https://blog.jsbarretto.com/post/laptop](https://blog.jsbarretto.com/post/laptop)

生成摘要时出错

---

## 31. Supermarket freezers across Europe hit by second suspected cyber-attack

**原文标题**: Supermarket freezers across Europe hit by second suspected cyber-attack

**原文链接**: [https://www.theguardian.com/world/2026/nov/02/supermarket-freezers-across-europe-hit-by-second-suspected-cyber-attack](https://www.theguardian.com/world/2026/nov/02/supermarket-freezers-across-europe-hit-by-second-suspected-cyber-attack)

生成摘要时出错

---

## 32. Can’t fish Ethernet? Use “invisible” fiber instead

**原文标题**: Can’t fish Ethernet? Use “invisible” fiber instead

**原文链接**: [https://momandpop.network/2026/11/02/cant-fish-ethernet-use-invisible-fiber-instead/](https://momandpop.network/2026/11/02/cant-fish-ethernet-use-invisible-fiber-instead/)

生成摘要时出错

---

## 33. Anthropic's internal AI use, at retail prices, now exceeds its employee pay

**原文标题**: Anthropic's internal AI use, at retail prices, now exceeds its employee pay

**原文链接**: [https://www.businessinsider.com/anthropic-claude-internal-ai-use-exceeds-employee-pay-tokens-2026-11](https://www.businessinsider.com/anthropic-claude-internal-ai-use-exceeds-employee-pay-tokens-2026-11)

生成摘要时出错

---

## 34. Ballot Rejections Have Soared in Rural Counties as USPS Reduces Mail Service

**原文标题**: Ballot Rejections Have Soared in Rural Counties as USPS Reduces Mail Service

**原文链接**: [https://www.propublica.org/article/mail-ballot-delays-postal-service-midterms](https://www.propublica.org/article/mail-ballot-delays-postal-service-midterms)

生成摘要时出错

---

## 35. Show HN: HackerBooks – HackerTube, but for books mentioned on HN

**原文标题**: Show HN: HackerBooks – HackerTube, but for books mentioned on HN

**原文链接**: [https://hackerbooks.org](https://hackerbooks.org)

生成摘要时出错

---

## 36. Postgres 19 is late because so many more bugs are being found now

**原文标题**: Postgres 19 is late because so many more bugs are being found now

**原文链接**: [http://rhaas.blogspot.com/2026/10/postgres-19-is-late-and-its-ais-fault.html](http://rhaas.blogspot.com/2026/10/postgres-19-is-late-and-its-ais-fault.html)

生成摘要时出错

---

## 37. The U.S. Census Bureau and "Super Intelligence"

**原文标题**: The U.S. Census Bureau and "Super Intelligence"

**原文链接**: [https://simonwillison.net/2026/Nov/2/census-bureau-super-intelligence/](https://simonwillison.net/2026/Nov/2/census-bureau-super-intelligence/)

生成摘要时出错

---

## 38. HackerTube: YouTube built from videos recommended by HN

**原文标题**: HackerTube: YouTube built from videos recommended by HN

**原文链接**: [https://karpathy.bearblog.dev/hacker-tube/](https://karpathy.bearblog.dev/hacker-tube/)

生成摘要时出错

---

## 39. Show HN: PyWolf3D, a wolfenstein3D clone written from scratch in Python

**原文标题**: Show HN: PyWolf3D, a wolfenstein3D clone written from scratch in Python

**原文链接**: [https://github.com/atifcodesalot/pyWolf3D](https://github.com/atifcodesalot/pyWolf3D)

生成摘要时出错

---

## 40. GPT-Rosalind-6 System Card Addendum

**原文标题**: GPT-Rosalind-6 System Card Addendum

**原文链接**: [https://deploymentsafety.openai.com/gpt-rosalind-6](https://deploymentsafety.openai.com/gpt-rosalind-6)

生成摘要时出错

---

## 41. Jobless tech workers are being left out of San Francisco's AI boom

**原文标题**: Jobless tech workers are being left out of San Francisco's AI boom

**原文链接**: [https://www.bloomberg.com/news/features/2026-09-17/san-francisco-s-ai-wealth-boom-skirts-engineers-as-openai-anthropic-ipos-near](https://www.bloomberg.com/news/features/2026-09-17/san-francisco-s-ai-wealth-boom-skirts-engineers-as-openai-anthropic-ipos-near)

生成摘要时出错

---

## 42. Cyberattacks hit supermarket fridges and freezers in Europe

**原文标题**: Cyberattacks hit supermarket fridges and freezers in Europe

**原文链接**: [https://www.euronews.com/2026/11/02/cyberattack-hits-belgian-supermarket-fridges-and-freezers](https://www.euronews.com/2026/11/02/cyberattack-hits-belgian-supermarket-fridges-and-freezers)

生成摘要时出错

---

## 43. Bitcoin Suisse CEO: Switzerland has lost interest in cryptocurrencies

**原文标题**: Bitcoin Suisse CEO: Switzerland has lost interest in cryptocurrencies

**原文链接**: [https://www.swissinfo.ch/eng/swiss-economy/cryptocurrencies-switzerland-has-lost-interest-says-bitcoin-suisse-ceo/92314545](https://www.swissinfo.ch/eng/swiss-economy/cryptocurrencies-switzerland-has-lost-interest-says-bitcoin-suisse-ceo/92314545)

生成摘要时出错

---

## 44. Japan launches mission to make first return trip to Mars

**原文标题**: Japan launches mission to make first return trip to Mars

**原文链接**: [https://www.ft.com/content/88638d03-1537-4f71-b099-3a951f1c4cb7](https://www.ft.com/content/88638d03-1537-4f71-b099-3a951f1c4cb7)

生成摘要时出错

---

## 45. Bones may release proteins that slow aging and extend life span

**原文标题**: Bones may release proteins that slow aging and extend life span

**原文链接**: [https://www.science.org/content/article/bones-may-release-proteins-slow-aging-and-extend-life-span](https://www.science.org/content/article/bones-may-release-proteins-slow-aging-and-extend-life-span)

生成摘要时出错

---

## 46. LLMs are not superhuman at reading and writing neural network weights

**原文标题**: LLMs are not superhuman at reading and writing neural network weights

**原文链接**: [https://www.seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/](https://www.seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/)

生成摘要时出错

---

## 47. Claude Opus 5.5 Can Draw Permit-Level Architectural Drawings

**原文标题**: Claude Opus 5.5 Can Draw Permit-Level Architectural Drawings

**原文链接**: [https://stephenjgallagher.substack.com/p/ai-can-draw-blueprints-now](https://stephenjgallagher.substack.com/p/ai-can-draw-blueprints-now)

生成摘要时出错

---

## 48. Last night an AI agent performed brain surgery on a mouse

**原文标题**: Last night an AI agent performed brain surgery on a mouse

**原文链接**: [https://twitter.com/OcanaSantero/status/2115442964574908902](https://twitter.com/OcanaSantero/status/2115442964574908902)

生成摘要时出错

---

## 49. Let Me Ch...

**原文标题**: Let Me Ch...

**原文链接**: [https://blog.alxgsv.com/let-me-check/](https://blog.alxgsv.com/let-me-check/)

生成摘要时出错

---

## 50. Anthropic's spending commitments surge to nearly $900B

**原文标题**: Anthropic's spending commitments surge to nearly $900B

**原文链接**: [https://www.axios.com/2026/11/02/anthropic-spending-revenue-surge](https://www.axios.com/2026/11/02/anthropic-spending-revenue-surge)

生成摘要时出错

---

## 51. Most of our measures of a key cognitive process don't agree

**原文标题**: Most of our measures of a key cognitive process don't agree

**原文链接**: [https://arstechnica.com/science/2026/11/most-of-our-measures-of-a-key-cognitive-process-dont-agree/](https://arstechnica.com/science/2026/11/most-of-our-measures-of-a-key-cognitive-process-dont-agree/)

生成摘要时出错

---

## 52. South Korea targets ' highest performance' sovereign AI model

**原文标题**: South Korea targets ' highest performance' sovereign AI model

**原文链接**: [https://www.cnbc.com/2026/11/02/south-korea-ai-spending-budget.html](https://www.cnbc.com/2026/11/02/south-korea-ai-spending-budget.html)

生成摘要时出错

---

## 53. Wir müssen wissen – wir werden wissen

**原文标题**: Wir müssen wissen – wir werden wissen

**原文链接**: [https://remy.wang/blog/hilbert.html](https://remy.wang/blog/hilbert.html)

生成摘要时出错

---

## 54. Moment of Ruby: An Argument for Nothing

**原文标题**: Moment of Ruby: An Argument for Nothing

**原文链接**: [https://www.aha.io/engineering/articles/moment-of-ruby-an-argument-for-nothing](https://www.aha.io/engineering/articles/moment-of-ruby-an-argument-for-nothing)

生成摘要时出错

---

## 55. New 3D thermal invisibility cloak makes objects disappear from infrared cameras

**原文标题**: New 3D thermal invisibility cloak makes objects disappear from infrared cameras

**原文链接**: [https://www.sciencedaily.com/releases/2026/10/261025073051.htm](https://www.sciencedaily.com/releases/2026/10/261025073051.htm)

生成摘要时出错

---

## 56. Mystery of 60-Second Fluctuations in Power Grids Solved

**原文标题**: Mystery of 60-Second Fluctuations in Power Grids Solved

**原文链接**: [https://www.fz-juelich.de/en/news/archive/press-release/2026/mystery-of-60-second-fluctuations-in-power-grids-solved](https://www.fz-juelich.de/en/news/archive/press-release/2026/mystery-of-60-second-fluctuations-in-power-grids-solved)

生成摘要时出错

---

## 57. Why are Soviet math textbooks so hardcore in comparison to US textbooks? (2017)

**原文标题**: Why are Soviet math textbooks so hardcore in comparison to US textbooks? (2017)

**原文链接**: [https://www.quora.com/Why-are-Soviet-mathematics-physics-textbooks-so-insanely-hardcore-in-comparison-to-US-textbooks/answer/Scott-Miller-307?share=1](https://www.quora.com/Why-are-Soviet-mathematics-physics-textbooks-so-insanely-hardcore-in-comparison-to-US-textbooks/answer/Scott-Miller-307?share=1)

生成摘要时出错

---

## 58. Goldman Restricts Traders and Bankers from Using Some AI Tools

**原文标题**: Goldman Restricts Traders and Bankers from Using Some AI Tools

**原文链接**: [https://www.bloomberg.com/news/articles/2026-11-02/goldman-restricts-traders-and-bankers-from-using-some-ai-tools](https://www.bloomberg.com/news/articles/2026-11-02/goldman-restricts-traders-and-bankers-from-using-some-ai-tools)

生成摘要时出错

---

## 59. F/OSS Comics #13: BSD Unix, Part 3 – The Beginning of BSD Unix

**原文标题**: F/OSS Comics #13: BSD Unix, Part 3 – The Beginning of BSD Unix

**原文链接**: [https://fosscomics.com/posts/13.%20BSD%20Unix%20Part%203%20-%20The%20Beginning%20of%20BSD%20Unix/](https://fosscomics.com/posts/13.%20BSD%20Unix%20Part%203%20-%20The%20Beginning%20of%20BSD%20Unix/)

生成摘要时出错

---

## 60. SOML – A Config Format for Humans

**原文标题**: SOML – A Config Format for Humans

**原文链接**: [https://github.com/soml-lang/soml](https://github.com/soml-lang/soml)

生成摘要时出错

---

## 61. Never Complain, Never Explain

**原文标题**: Never Complain, Never Explain

**原文链接**: [https://en.wikipedia.org/wiki/Never_complain,_never_explain](https://en.wikipedia.org/wiki/Never_complain,_never_explain)

生成摘要时出错

---

## 62. China's First Frontier AI Export Controls: Mofcom Announcement No. 48

**原文标题**: China's First Frontier AI Export Controls: Mofcom Announcement No. 48

**原文链接**: [https://labs.cloudsecurityalliance.org/research/csa-research-note-china-ai-export-controls-announcement-48-2/](https://labs.cloudsecurityalliance.org/research/csa-research-note-china-ai-export-controls-announcement-48-2/)

生成摘要时出错

---

## 63. 40 °C heat extremes are no longer implausible in the Nordic countries

**原文标题**: 40 °C heat extremes are no longer implausible in the Nordic countries

**原文链接**: [https://www.nature.com/articles/s44304-026-00290-9](https://www.nature.com/articles/s44304-026-00290-9)

生成摘要时出错

---

## 64. Proving and improving the Platonic Representation Hypothesis with JEPAs

**原文标题**: Proving and improving the Platonic Representation Hypothesis with JEPAs

**原文链接**: [https://arxiv.org/abs/2610.39302](https://arxiv.org/abs/2610.39302)

生成摘要时出错

---

## 65. From Charlemagne to the Kitchen Boy: Reading the Hamburg Rathaus

**原文标题**: From Charlemagne to the Kitchen Boy: Reading the Hamburg Rathaus

**原文链接**: [https://alsterrunde.com/from-charlemagne-to-the-kitchen-boy-reading-the-hamburg-rathaus/](https://alsterrunde.com/from-charlemagne-to-the-kitchen-boy-reading-the-hamburg-rathaus/)

生成摘要时出错

---

## 66. Patrick Stewart's First TV Appearance

**原文标题**: Patrick Stewart's First TV Appearance

**原文链接**: [https://www.youtube.com/watch?v=FUwYwJ2DT_I](https://www.youtube.com/watch?v=FUwYwJ2DT_I)

生成摘要时出错

---

## 67. An Italian farmer found some unknown seeds in his attic and planted them

**原文标题**: An Italian farmer found some unknown seeds in his attic and planted them

**原文链接**: [https://www.smithsonianmag.com/science-nature/italian-farmer-found-unknown-seeds-attic-with-nothing-lose-planted-them-result-biblical-180989644/](https://www.smithsonianmag.com/science-nature/italian-farmer-found-unknown-seeds-attic-with-nothing-lose-planted-them-result-biblical-180989644/)

生成摘要时出错

---

## 68. Radiation Map of the World

**原文标题**: Radiation Map of the World

**原文链接**: [https://radiaverse.com/](https://radiaverse.com/)

生成摘要时出错

---

## 69. Trigger.dev customer environment variables exposed

**原文标题**: Trigger.dev customer environment variables exposed

**原文链接**: [https://trigger.dev/blog/security-incident-nov-2026](https://trigger.dev/blog/security-incident-nov-2026)

生成摘要时出错

---

## 70. Mathematics has changed. Let's act like it

**原文标题**: Mathematics has changed. Let's act like it

**原文链接**: [https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it/](https://terrytao.wordpress.com/2026/11/01/mathematics-has-changed-lets-act-like-it/)

生成摘要时出错

---

## 71. Lenovo's 'encrypted' fingerprint USB is just an unencrypted SD card in a case

**原文标题**: Lenovo's 'encrypted' fingerprint USB is just an unencrypted SD card in a case

**原文链接**: [https://www.reddit.com/r/technology/comments/1xl2pr3/lenovos_encrypted_fingerprint_usb_drive_is_just/](https://www.reddit.com/r/technology/comments/1xl2pr3/lenovos_encrypted_fingerprint_usb_drive_is_just/)

生成摘要时出错

---

## 72. Leaking Secrets from Air-Gap Computers by Spelling Radio Signals from RAM (2024)

**原文标题**: Leaking Secrets from Air-Gap Computers by Spelling Radio Signals from RAM (2024)

**原文链接**: [https://arxiv.org/abs/2409.02292](https://arxiv.org/abs/2409.02292)

生成摘要时出错

---

## 73. Kraft Mac & Cheese Now Comes in Cinnamon Roll Flavor

**原文标题**: Kraft Mac & Cheese Now Comes in Cinnamon Roll Flavor

**原文链接**: [https://parade.com/food/kraft-mac-cheese-just-launched-2-unexpected-new-flavors-and-one-is-inspired-by-a-beloved-breakfast-treat](https://parade.com/food/kraft-mac-cheese-just-launched-2-unexpected-new-flavors-and-one-is-inspired-by-a-beloved-breakfast-treat)

生成摘要时出错

---

## 74. Domain hacks with unusual Unicode characters (2018)

**原文标题**: Domain hacks with unusual Unicode characters (2018)

**原文链接**: [https://shkspr.mobi/blog/2018/11/domain-hacks-with-unusual-unicode-characters/](https://shkspr.mobi/blog/2018/11/domain-hacks-with-unusual-unicode-characters/)

生成摘要时出错

---

## 75. Researchers face record-low chances of getting a grant partly due to rise of AI

**原文标题**: Researchers face record-low chances of getting a grant partly due to rise of AI

**原文链接**: [https://nltimes.nl/2026/11/02/researchers-face-record-low-chances-getting-grant-partly-due-rise-ai](https://nltimes.nl/2026/11/02/researchers-face-record-low-chances-getting-grant-partly-due-rise-ai)

生成摘要时出错

---

## 76. Show HN: I rebuilt my old canvas 3D library as a small WebGL 2 library – phoria2

**原文标题**: Show HN: I rebuilt my old canvas 3D library as a small WebGL 2 library – phoria2

**原文链接**: [https://kevs3d.co.uk/phoria2/](https://kevs3d.co.uk/phoria2/)

生成摘要时出错

---

## 77. OccupySaaS

**原文标题**: OccupySaaS

**原文链接**: [https://occupysaas.com/](https://occupysaas.com/)

生成摘要时出错

---

## 78. Running a bootstrapped SaaS for 20 years with my brother

**原文标题**: Running a bootstrapped SaaS for 20 years with my brother

**原文链接**: [https://blog.zamzar.com/2026/10/30/20-years-766-million-files-two-chameleons/](https://blog.zamzar.com/2026/10/30/20-years-766-million-files-two-chameleons/)

生成摘要时出错

---

## 79. Ondrej Surý, who saved the internet: You have to want to do something for others

**原文标题**: Ondrej Surý, who saved the internet: You have to want to do something for others

**原文链接**: [https://english.elpais.com/technology/2026-11-02/ondrej-sury-the-man-who-saved-the-internet-you-have-to-want-to-do-something-for-others.html](https://english.elpais.com/technology/2026-11-02/ondrej-sury-the-man-who-saved-the-internet-you-have-to-want-to-do-something-for-others.html)

生成摘要时出错

---

## 80. Zinc creep in cable spelter sockets brought down the Arecibo telescope in 2020

**原文标题**: Zinc creep in cable spelter sockets brought down the Arecibo telescope in 2020

**原文链接**: [https://maketecheasier.com/arecibo-zinc-creep-collapse/](https://maketecheasier.com/arecibo-zinc-creep-collapse/)

生成摘要时出错

---

## 81. Napping characteristics and incident dementia

**原文标题**: Napping characteristics and incident dementia

**原文链接**: [https://academic.oup.com/biomedgerontology/article/81/10/glag208/8769491?login=false](https://academic.oup.com/biomedgerontology/article/81/10/glag208/8769491?login=false)

生成摘要时出错

---

## 82. The She-Wolves of Jülich

**原文标题**: The She-Wolves of Jülich

**原文链接**: [https://www.historytoday.com/archive/history-matters/she-wolves-julich](https://www.historytoday.com/archive/history-matters/she-wolves-julich)

生成摘要时出错

---

## 83. Nibnib: Image compression with extreme decompression speed

**原文标题**: Nibnib: Image compression with extreme decompression speed

**原文链接**: [https://github.com/raphlinus/nibnib](https://github.com/raphlinus/nibnib)

生成摘要时出错

---

## 84. TCP Use-After-Free: CVE-2026-98432 / CVSS 9.8

**原文标题**: TCP Use-After-Free: CVE-2026-98432 / CVSS 9.8

**原文链接**: [https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf](https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf)

生成摘要时出错

---

## 85. It's the memory latency, stupid

**原文标题**: It's the memory latency, stupid

**原文链接**: [https://pivotlake.io/blog/its-the-memory-latency-stupid/](https://pivotlake.io/blog/its-the-memory-latency-stupid/)

生成摘要时出错

---

## 86. Show HN: ClickBench inspired leaderboard for multiple database benchmarks

**原文标题**: Show HN: ClickBench inspired leaderboard for multiple database benchmarks

**原文链接**: [https://benchmark.pivotlake.io/](https://benchmark.pivotlake.io/)

生成摘要时出错

---

## 87. $48 e-paper display can be whatever you want it to be

**原文标题**: $48 e-paper display can be whatever you want it to be

**原文链接**: [https://arstechnica.com/gadgets/2026/11/this-48-e-paper-display-can-be-whatever-you-want-it-to-be/](https://arstechnica.com/gadgets/2026/11/this-48-e-paper-display-can-be-whatever-you-want-it-to-be/)

生成摘要时出错

---

## 88. New cyberattack on supermarket fridges sweeps across Europe

**原文标题**: New cyberattack on supermarket fridges sweeps across Europe

**原文链接**: [https://www.reuters.com/business/retail-consumer/temperature-soars-swedish-grocery-store-freezers-one-store-blames-hackers-2026-11-02/](https://www.reuters.com/business/retail-consumer/temperature-soars-swedish-grocery-store-freezers-one-store-blames-hackers-2026-11-02/)

生成摘要时出错

---

## 89. Bidirectional charging during grid outages

**原文标题**: Bidirectional charging during grid outages

**原文链接**: [https://www.jefftk.com/p/bidirectional-charging-during-grid-outages](https://www.jefftk.com/p/bidirectional-charging-during-grid-outages)

生成摘要时出错

---

## 90. Parchment Paper History: How We Got Paper Perfect for Baking (2019)

**原文标题**: Parchment Paper History: How We Got Paper Perfect for Baking (2019)

**原文链接**: [https://tedium.co/2019/11/21/nonstick-parchment-paper-history/](https://tedium.co/2019/11/21/nonstick-parchment-paper-history/)

生成摘要时出错

---

## 91. The AI cost of JavaScript frameworks

**原文标题**: The AI cost of JavaScript frameworks

**原文链接**: [https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/](https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/)

生成摘要时出错

---

## 92. Seoul Viosys begins production of rare-earth-free white light emitter

**原文标题**: Seoul Viosys begins production of rare-earth-free white light emitter

**原文链接**: [https://www.semiconductor-today.com/news_items/2026/oct/seoul-291026.shtml](https://www.semiconductor-today.com/news_items/2026/oct/seoul-291026.shtml)

生成摘要时出错

---

## 93. Altoids Project

**原文标题**: Altoids Project

**原文链接**: [https://uvdn7.github.io/altoids-project/](https://uvdn7.github.io/altoids-project/)

生成摘要时出错

---

## 94. Tips for more effective fuzz testing with AFL++

**原文标题**: Tips for more effective fuzz testing with AFL++

**原文链接**: [https://nullprogram.com/blog/2025/02/05/](https://nullprogram.com/blog/2025/02/05/)

生成摘要时出错

---

## 95. A proposal: how to hire junior engineers in the age of AI

**原文标题**: A proposal: how to hire junior engineers in the age of AI

**原文链接**: [https://seldo.com/posts/a-proposal-how-to-hire-junior-engineers-in-the-age-of-ai/](https://seldo.com/posts/a-proposal-how-to-hire-junior-engineers-in-the-age-of-ai/)

生成摘要时出错

---

## 96. Memdoor: A team of 5 Qwen3.8-27B models beats Fable 5 on LiveCodeBench Hard

**原文标题**: Memdoor: A team of 5 Qwen3.8-27B models beats Fable 5 on LiveCodeBench Hard

**原文链接**: [https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve](https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve)

生成摘要时出错

---

## 97. Brazilian Court Sanctions Lawyers for Prompt Injection in Court Filing

**原文标题**: Brazilian Court Sanctions Lawyers for Prompt Injection in Court Filing

**原文链接**: [https://jetstream.security/insights/brazilian-court-sanctions-prompt-injection-filing/](https://jetstream.security/insights/brazilian-court-sanctions-prompt-injection-filing/)

生成摘要时出错

---

## 98. Anthropic's Amended S1 Filing Shows Slowing Q3 Growth

**原文标题**: Anthropic's Amended S1 Filing Shows Slowing Q3 Growth

**原文链接**: [https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm](https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm)

生成摘要时出错

---

## 99. The future in old computer magazines (1984–2004)

**原文标题**: The future in old computer magazines (1984–2004)

**原文链接**: [https://tomorrowasusual.substack.com/p/blast-from-the-past-the-future-in](https://tomorrowasusual.substack.com/p/blast-from-the-past-the-future-in)

生成摘要时出错

---

## 100. I Built a $5 Apple Vision Pro [video]

**原文标题**: I Built a $5 Apple Vision Pro [video]

**原文链接**: [https://www.youtube.com/watch?v=XtNmiTohUcs](https://www.youtube.com/watch?v=XtNmiTohUcs)

生成摘要时出错

---

