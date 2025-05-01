# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-05-01.md)

*最后自动更新时间: 2025-05-01 17:49:43*
## 1. Redis再次开源

**原文标题**: Redis is open source again

**原文链接**: [https://antirez.com/news/151](https://antirez.com/news/151)

Redis重新开源

文章《Redis重新开源》宣布Redis已回归开源项目。虽然标题简短，但暗示Redis此前已偏离其最初的开源许可。总结来说，关键要点是：

*   **Redis现在再次开源。** 这可能表明许可协议已更改为更宽松和对社区友好的模式，从而在软件的使用、分发和修改方面提供了更大的自由度。鉴于之前的许可更改是朝着更严格的方向发展，因此这次回归对于开源社区和Redis用户来说将是一个重要消息。

---

## 2. 克劳德现在可以连接你的世界了

**原文标题**: Claude can now connect to your world

**原文链接**: [https://www.anthropic.com/news/integrations](https://www.anthropic.com/news/integrations)

Anthropic 发布 Claude 重大更新，增强连接性和研究能力。核心公告是“集成”，允许 Claude 通过模型上下文协议 (MCP) 连接并使用来自各种应用和工具的数据。这使 Claude 能够理解项目历史记录、任务状态和组织知识，使其成为更明智和更具协作性的助手。

最初，集成适用于 10 个流行的服务，包括 Jira、Confluence、Zapier、Cloudflare、Intercom、Asana、Square、Sentry、PayPal、Linear 和 Plaid，未来还将推出更多服务。开发人员还可以创建自定义集成。用例示例包括：Zapier 集成，用于自动化数千个应用程序的工作流程；Atlassian 集成，用于产品开发和任务管理；Intercom 集成，用于简化用户反馈和错误解决。

此外，Claude 的“研究”能力已通过“高级模式”得到增强，从而能够跨网络搜索、Google Workspace 以及现在已连接的集成进行更深入的调查。这种高级研究可能需要长达 45 分钟，并生成带有引用的综合报告。网络搜索功能现已在全球范围内向所有 Claude 付费计划用户开放。

集成和高级研究目前以 Beta 版形式提供给 Max、Team 和 Enterprise 计划，并将很快在 Pro 上推出。

---

## 3. 我们发现一名试图在 Kraken 找工作的朝鲜黑客。

**原文标题**: We identified a North Korean hacker who tried to get a job at Kraken

**原文链接**: [https://blog.kraken.com/news/how-we-identified-a-north-korean-hacker](https://blog.kraken.com/news/how-we-identified-a-north-korean-hacker)

Kraken安全团队挫败朝鲜黑客冒充工程师渗透公司的企图。团队因初期电话中的姓名变更和面试中的语音指导等不一致之处而起疑。当候选人邮箱与行业合作伙伴提供的朝鲜黑客关联邮箱列表匹配时，疑虑得到证实。

Kraken红队利用开源情报发现了一个与该候选人相关的虚假身份网络，其中一些人曾被雇用，一人在制裁名单上。进一步调查揭示了技术上的不一致，如通过VPN远程桌面、与泄露邮箱相关的GitHub个人资料，以及可能被篡改的身份证明。

Kraken没有立即拒绝该候选人，而是策略性地推进其通过面试流程，以收集有关其策略的情报。看似随意的与首席安全官的最终面试，实则是一个巧妙的陷阱。当面对实时验证提示，如位置确认和身份验证时，候选人犹豫不决，确认了其冒名顶替者的身份。

Kraken分享此次经历旨在强调网络威胁不断演变的本质，并强调主动安全措施的重要性。主要结论包括“验证，而非信任”的必要性、国家赞助攻击的危险、人工智能辅助欺骗的兴起，以及公司范围内安全意识文化的重要性。Kraken强调，即使是招聘过程也可能成为目标，仔细审查和主动方法对于防御至关重要。

---

## 4. 在电脑间更快复制SQLite数据库的方法

**原文标题**: A faster way to copy SQLite databases between computers

**原文链接**: [https://alexwlchan.net/2025/copying-sqlite-databases/](https://alexwlchan.net/2025/copying-sqlite-databases/)

本文介绍了一种在计算机之间更快、更可靠地复制大型 SQLite 数据库的方法，重点在于通过避免数据库索引中的重复来减少传输大小。由于数据库增大，特别是索引的大小，作者最初使用 `rsync` 直接复制数据库文件的方法变得缓慢且不可靠。

该解决方案包括使用 `sqlite3 .dump` 命令创建数据库的文本转储，该转储将数据库表示为一系列 SQL 语句。 此文本文件比原始数据库小得多，因为它只包含*创建*索引的指令，而不包含索引本身。 然后使用 `gzip` 进一步压缩该文本文件。

改进后的工作流程包括：

1. 在远程服务器上创建 gzipped 文本转储（`sqlite3 ... .dump | gzip -c`）。
2. 使用 `rsync` 将 gzipped 文本文件复制到本地计算机。
3. 从服务器中删除 gzipped 文本文件。
4. 在本地解压文本文件（`gunzip`）。
5. 从文本文件重建数据库（`cat ... | sqlite3`）。
6. 删除本地文本文件。

作者提供了一个示例，表明 gzipped 文本转储可以比原始数据库小得多（例如，14 倍）。此外，此方法可确保稳定的复制源，防止在直接文件传输期间更新数据库时可能出现的数据库损坏问题。 在处理大型 SQLite 数据库时，此方法可提供更快的下载速度和更高的可靠性。

---

## 5. Show HN: 机械计算机套件 (Roons)

**原文标题**: Show HN: Mechanical Computer Kit (Roons)

**原文链接**: [https://whomtech.com/show-hn/](https://whomtech.com/show-hn/)

此“Show HN”帖子介绍了Roons，这是一款基于“织布机自动机”概念构建机械计算机的套件。受机械逻辑门实现的启发，创作者使用放置在移动织布机上的瓦片（“roons”）来引导弹珠并表示比特流，从而将逻辑门小型化。该织布机充当细胞自动机，为内存和指令集等组件提供通用接口。

该套件旨在实现紧凑性、及时性、快速编辑、保存/加载功能以及最少的核心部件，使其既实用又有趣。作者通过异或门演示了图灵完备性，并展示了二进制加法器等示例。可拆卸磁盘系统允许模块化和轻松的模式存储。驱动器可以连接以扩展工作空间，集成齿轮提供同步动力。

包括解旋器、水桶、7段显示器、数字键盘、字母数字显示器和硬盘驱动器在内的外围设备正在开发中。这些外围设备旨在增强套件的功能，并展示其执行复杂任务（如显示计算结果或滚动文本）的潜力。

创作者使用3D打印PLA进行原型设计，并计划切换到注塑成型的ABS进行生产。该帖子承认了外围设备延迟、部件可靠性和互操作性问题，以及需要提高易用性等挑战。Kickstarter众筹活动将于5月21日启动，并提供评测套件。

---

## 6. Linkwarden: 可自托管的开源书签管理，支持AI标签和页面存档

**原文标题**: Linkwarden: FOSS self-hostable bookmarking with AI-tagging and page archival

**原文链接**: [https://linkwarden.app/](https://linkwarden.app/)

Linkwarden：开源、自托管的书签工具，旨在保存网页和文档。它允许用户通过集合、子集合和AI驱动的标签来收集和组织链接，方便检索。一个关键特性是自动网页归档，创建屏幕截图和完整的HTML版本，以应对链接失效。

协作是核心，团队可以共享集合并分配权限。该平台提供注重隐私的设计、强大的搜索、浏览器扩展、暗/亮模式、批量操作、导入/导出功能以及适用于移动设备的PWA。它还拥有安全的API集成。

用例包括个人整理、设计灵感、研究和项目协作。用户评价强调了其易用性、归档能力和书签管理优势。

Linkwarden提供云托管方案，起价为每用户每月3美元，最多可存储30,000个链接；以及可定制的托管/自托管选项，提供无限链接和SSO等功能（请联系获取定价）。两者都提供优先支持和自动更新。云方案提供14天免费试用。Linkwarden网站上提供了与其他书签服务（如Pocket、Raindrop和Pinboard）的比较。

---

## 7. Waypoint Transit (YC W25) Is Hiring a Founding Engineer

**原文标题**: Waypoint Transit (YC W25) Is Hiring a Founding Engineer

**原文链接**: [https://www.workatastartup.com/jobs/75517](https://www.workatastartup.com/jobs/75517)

航点交通(YC W25)正在招聘创始软件工程师，以帮助实现城市规划自动化，并赋能城市设计可持续、有韧性且以人为本的环境。他们利用人工智能来自动化通常由成本高昂的咨询公司处理的重复性任务，从而解决传统城市规划的低效率问题。

该职位需要与创始人密切合作，从头开始定义工程系统，包括微调YOLO模型进行图像分割、开发处理城市规划文档的系统、协调人工智能代理进行安全建议、自动化报告生成以及部署/维护地图服务器等项目。

理想的候选人应具备扎实的编程技能、学习意愿、对不确定性的适应能力、以客户为中心的态度以及不屈不挠的解决问题能力。“加分项”包括人工智能、Web开发（NextJS）、GIS、交通工程/城市规划方面的经验以及对城市规划的热情。

该职位为旧金山全职现场办公，薪资为12万美元至17万美元，股权为0.50%至2.00%。面试流程包括电话面试、技术面试、现场带薪试工和背景调查。由于初创公司处于早期阶段，可能需要一些晚上和周末工作。他们对新毕业生持开放态度。

---

## 8. Fivetran 将收购 Census

**原文标题**: Fivetran to acquire Census

**原文链接**: [https://www.fivetran.com/blog/why-fivetran-and-census-are-joining-forces](https://www.fivetran.com/blog/why-fivetran-and-census-are-joining-forces)

生成摘要时出错

---

## 9. 法官裁定苹果高管作伪证，建议以藐视法庭罪起诉

**原文标题**: Judge Rules Apple Executive Lied Under Oath, Makes Criminal Contempt Referral

**原文链接**: [https://www.thebignewsletter.com/p/judge-rules-apple-executive-lied](https://www.thebignewsletter.com/p/judge-rules-apple-executive-lied)

好的，我已阅读了来自The Big Newsletter题为“法官裁定苹果高管作伪证，建议提起刑事藐视诉讼”的文章。以下是摘要：

联邦法官托马斯·S·希克森裁定，苹果高管托马斯·莫耶在Epic Games针对苹果提起的持续反垄断诉讼的相关证词中作伪证。法官认为，莫耶关于2017年与日本公司Fintiv达成的协议的证词“不真实、回避且不坦诚”。 具体而言，莫耶关于协议的时间和性质的陈述，以及他否认与也涉及Fintiv和圣克拉拉县两位警长的无关贿赂丑闻有任何关联的说法，都被认为是虚假的。

希克森法官正在将此事提交给美国检察官办公室，以寻求对莫耶提起潜在的刑事藐视指控。 这次提交意义重大，因为它提高了已经备受瞩目的反垄断案件的风险，并为这位苹果高管个人带来了承担法律后果的可能性。

该裁决源于Epic Games案件中的一项证据开示争议，Epic试图获取有关苹果与Fintiv交易的信息。 莫耶的证词被认为是理解苹果与反垄断指控相关的决策和关系背景的关键。 法官认定他撒谎削弱了苹果的信誉，并可能影响案件的整体结果。 法官强调了莫耶的证词与其他证据和文件相比存在的具体不一致之处。 美国检察官办公室现在将根据希克森法官的建议，决定是否对莫耶提起刑事藐视诉讼。

---

## 10. 7月1日起，学术出版商不得对美国国立卫生研究院资助的研究设置付费墙

**原文标题**: Starting July 1, Academic Publishers Can't Paywall NIH-Funded Research

**原文链接**: [https://www.nih.gov/about-nih/who-we-are/nih-director/statements/accelerating-access-research-results-new-implementation-date-2024-nih-public-access-policy](https://www.nih.gov/about-nih/who-we-are/nih-director/statements/accelerating-access-research-results-new-implementation-date-2024-nih-public-access-policy)

美国国立卫生研究院加速推进2024年公共获取政策，将原计划于2025年12月31日开始的NIH资助研究免费向公众开放日期提前至2025年7月1日。这一举措由新任NIH主任宣布，旨在提高科学研究的透明度和公众信任度。

2024年公共获取政策取消了之前的12个月禁运期，允许通过PubMed Central立即访问报告NIH支持研究的文章。最初的2008年公共获取政策已经免费提供了超过150万篇文章。

NIH认为，更快地获取研究结果将增强公众信心，尤其是在最近皮尤研究中心的一项研究表明，只有25%的美国人对为公共利益工作的科学家抱有强烈信心的情况下。通过确保快速访问来自纳税人资助研究的可重复、可复现和可推广的结果，NIH希望重申其为美国人民服务的承诺，并“让美国再次健康”。NIH将继续优先考虑其所有运营的透明度，以重新获得并维持公众对科学的信任。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 2 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 3 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 4 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 5 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 6 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 7 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 8 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 9 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 10 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 11 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 12 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 13 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 14 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 15 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 16 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 17 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 18 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 19 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 20 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 21 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 22 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 23 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 24 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 25 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 26 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 27 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 28 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 29 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 30 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 31 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 32 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 33 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 34 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 35 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 36 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 37 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 38 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 39 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 40 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 41 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 42 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 43 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
