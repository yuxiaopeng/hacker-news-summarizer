# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-25.md)

*最后自动更新时间: 2026-02-25 18:29:28*
## 1. 公交站点优化快速、廉价且有效。

**原文标题**: Bus stop balancing is fast, cheap, and effective

**原文链接**: [https://worksinprogress.co/issue/the-united-states-needs-fewer-bus-stops/](https://worksinprogress.co/issue/the-united-states-needs-fewer-bus-stops/)

**摘要：公交站点优化**

公交站点优化（Bus stop balancing）——即通过战略性地移除冗余站点来增加站间距——是改善城市交通的一种快速、低成本且高效的方式。虽然大型轨道交通项目往往备受关注，但公交车承载了更多的乘客，且在疫情后恢复得更快。然而，在美英两国的许多城市，公交站点间距仅为700英尺左右，导致车辆行驶缓慢，使其在与私家车的竞争中缺乏优势。

通过采用欧洲间距更宽（约1,300英尺）的模式，交通管理部门可以获得以下关键收益：

*   **提高速度与效率：** 减少站点既缩短了“停站时间”（乘客上下车），也减少了“非停站时间”（减速、加速及应对交通流量）。在旧金山和温哥华等城市的实施结果显示，车速提升了高达14%，为乘客节省了大量时间。
*   **节省成本：** 人工成本是交通部门最大的开支。更快的公交车能更迅速地完成运行路线，从而只需更少的车辆和司机即可维持相同的发车频率。节省下的资金可重新投入到其他线路的服务中。
*   **提高可靠性：** 站点减少意味着行程延误和变数的机会减少，解决了通勤者最主要的困扰之一。
*   **改善配套设施：** 通过维护更少的站点，管理部门有能力对剩余站点进行升级，配备更好的候车亭、座椅、照明和实时信息系统，将“孤零零的站牌”转化为高质量的交通枢纽。

尽管批评者认为站点整合会降低覆盖范围，但研究表明，由于“步行覆盖区”存在重叠，对实际可达性的影响微乎其微。最终，站点优化将重点从单纯的地理覆盖转向了实质性的便捷通达，让乘客能在更短时间内到达更多目的地。它是交通改革中一个罕见的范例：无需新建基础设施，却能产生立竿见影且可衡量的效果。

---

## 2. 千万别买 .online 域名

**原文标题**: Never buy a .online domain

**原文链接**: [https://www.0xsid.com/blog/online-tld-is-pain](https://www.0xsid.com/blog/online-tld-is-pain)

作者是一位长期的“.com 纯粹主义者”，他分享了一个关于通过 Namecheap 促销购买 **.online** 域名的警示案例。在为一个浏览器应用发布了一个简单的落地页后不久，该网站被 Google 标记为“不安全”，并被注册局 Radix 设为 **serverHold**（注册局暂停解析）状态。

这引发了一个技术上的“第 22 条军规”（死循环）：
1.  **注册局 (Radix)** 拒绝解除 serverHold 状态，直到 Google 将该网站从黑名单中移除。
2.  **Google** 要求作者通过 Search Console 中的 DNS 记录验证所有权，方可申请复审。
3.  **冲突点：** 由于域名处于 serverHold 状态，域名无法解析，导致 DNS 验证根本无法完成。

在没有收到注册商或注册局任何通知，且无法通过自动化渠道解决的情况下，作者的网站始终处于离线且无法访问的状态。直到该故事在 Hacker News 上引起热议，一名匿名的 Google 员工手动清除了黑名单标记，Radix 才最终解除了域名锁定，问题才得以解决。

**核心启示：**
*   **坚持使用 .com：** 标准顶级域名（TLD）面临注册局层面激进自动化封禁的概率较低。
*   **立即验证：** 务必在购买新域名后立即将其添加到 Google Search Console，以便在潜在封禁发生前确立所有权。
*   **可观测性：** 即使是小项目，也要使用运行时间监控，以捕获隐蔽的 DNS 故障。
*   **“小众”顶级域名的风险：** 小众注册局的滥用处理政策可能极其敏感且沟通不畅，一旦被标记，所有者往往投诉无门。

---

## 3. 基于大语言模型的大规模在线去匿名化

**原文标题**: Large-Scale Online Deanonymization with LLMs

**原文链接**: [https://simonlermen.substack.com/p/large-scale-online-deanonymization](https://simonlermen.substack.com/p/large-scale-online-deanonymization)

文章《使用大语言模型进行大规模在线去匿名化》重点介绍了苏黎世联邦理工学院（ETH Zurich）关于数字隐私侵蚀的突破性研究。该研究表明，GPT-4 等大语言模型（LLM）能够从看似匿名的社交媒体评论中准确推断出高度敏感的个人信息。

通过分析包含 500 多个 Reddit 个人资料的数据集，研究人员发现 LLM 能够以惊人的精度预测用户属性，包括所在地、年龄、性别、职业甚至收入。在研究中，GPT-4 的 Top-1 预测准确率高达 85%，Top-3 准确率则达到 95.8%。这些模型通过“串联”散布在多条帖子中的细微线索（如提到的当地地标、特定的通勤路线或人生里程碑）来实现这一目标。

核心发现及其影响包括：

*   **大规模画像：** 人类专家虽然也能进行类似的画像分析，但时间和劳动力成本高昂；与之不同，LLM 能够实现低成本、大规模的自动化去匿名化。
*   **传统匿名化的失效：** 移除姓名或直接标识符等传统做法已不足以保护隐私。LLM 利用复杂的推理能力绕过这些保护措施，使得在公开互联网上实现真正的匿名几乎成为不可能。
*   **新的隐私风险：** 这种能力降低了大范围监控、定向骚扰以及揭露匿名举报者或政治异议人士身份的门槛。

归根结底，这篇文章发出了警示：LLM 已从根本上改变了隐私格局。随着这些模型变得愈发普及和强大，将零散的数字足迹整合为完整个人画像的能力，已成为任何拥有 API 访问权限的人都能使用的工具，这对全球互联网用户构成了重大威胁。

---

## 4. 大学的误用

**原文标题**: The Misuses of the University

**原文链接**: [https://www.publicbooks.org/the-misuses-of-the-university/](https://www.publicbooks.org/the-misuses-of-the-university/)

在《大学之误》（The Misuses of the University）一文中，肖恩·菲利普斯（Siobhán Phillips）通过重新审视克拉克·克尔（Clark Kerr）1963年提出的“巨型大学”（multiversity）概念，探讨了美国高等教育的演变及其当前的危机。克尔认为大学不应是孤立的“象牙塔”，而应是与国家和经济需求紧密结合的核心“知识产业”。菲利普斯指出，尽管克尔的愿景具有预见性，但它也为现代学术机构堕落为企业化榨取和社会剥削的工具铺平了道路。

该摘要强调了对当代大学的几项关键批判：

*   **私有化陷阱**：继20世纪后期的“大错误”之后，大学的角色从公共产品转变为私人投资。这导致了政府拨款的减少、学费的飙升，以及对学生债务和不稳定的临时教职劳动力的依赖。
*   **掠夺性城市化**：借鉴达瓦里安·鲍德温（Davarian Baldwin）的研究，菲利普斯描述了“大学城”（UniverCities）的兴起。许多富裕的机构非但没有提升周边环境，反而扮演着掠夺性房地产开发商的角色，利用其免税地位推动社区绅士化、驱逐低收入居民，并扩大校园警务管控。
*   **机构虚伪**：虽然大学经常在营销中宣传“多样性与包容性”，但其财务结构往往在强化不平等。所谓的“误用”在于，这些机构将资本积累和机构声望置于其教育和公民使命之上。

最终，菲利普斯认为现代大学已成为一座为自身行政增长而非公众利益服务的“知识工厂”。文章呼吁对高等教育进行根本性的重新构想——超越克尔的工业模式，优先考虑真正的社会公平，并恢复大学作为公共资源的属性。

---

## 5. 增长35%后，美国电网太阳能发电量已超过水电。

**原文标题**: Following 35% growth, solar has passed hydro on US grid

**原文链接**: [https://arstechnica.com/science/2026/02/final-2025-data-is-in-us-energy-use-is-up-as-solar-passes-hydro/](https://arstechnica.com/science/2026/02/final-2025-data-is-in-us-energy-use-is-up-as-solar-passes-hydro/)

2025年，由于发电量同比增长35%，太阳能首次超过水电，实现了重大里程碑。尽管可再生能源经历了创纪录的扩张，但受数据中心、电动汽车和热泵的驱动，美国电力总需求增长了2.8%，其增速超过了可再生能源的增量。

报告强调了能源形势的复杂性：虽然太阳能和风能满足了近四分之三的新增需求，但其余部分则由煤炭使用量13%的增长来填补。煤炭消费的复苏受多种因素影响，包括天然气出口增加及硬件关税导致的天然气价格上涨，以及特朗普政府旨在推迟煤电厂关闭的政策。

展望2026年，受有利的经济因素驱动，可再生能源的前景依然强劲。计划中的项目包括创纪录的43吉瓦（GW）太阳能装机和12吉瓦风电，其中包括重大的海上开发项目以及新墨西哥州一座3.6吉瓦的大型风电场。此外，为了应对可再生能源的波动性，预计电网将新增24吉瓦的电池储能，主要分布在德克萨斯州和加利福尼亚州。

最终，美国正接近一个关键转折点，届时风能和太阳能的增长可能很快便能完全抵消不断增长的需求。然而，当前依靠煤炭填补即时缺口的现状表明，市场动态和政策转变仍在使减少电网整体碳排放的努力变得复杂化。

---

## 6. GNU TeXmacs

**原文标题**: GNU Texmacs

**原文链接**: [https://www.texmacs.org/tmweb/home/welcome.en.html](https://www.texmacs.org/tmweb/home/welcome.en.html)

GNU TeXmacs 是由自由软件基金会 (FSF) GNU 项目开发的免费开源科学编辑平台。它旨在通过用户友好的“所见即所得”(WYSIWYG) 界面创建高质量的技术文档。

**核心特性与功能：**
*   **结构化内容：** 该编辑器支持广泛的内容，包括复杂的数学排版、集成图形、演示文稿以及交互式内容。
*   **计算接口：** 它可以作为各种外部系统的图形前端，例如计算机代数、数值分析和统计软件。
*   **独特的引擎：** 尽管名称如此，TeXmacs 并不基于 TeX/LaTeX。它使用自有的高质量排版引擎，为打印或数字演示生成专业级文档。
*   **兼容性与转换：** 该软件可在 Unix、MacOS 和 Windows 上运行。它支持多种语言，并提供针对 TeX/LaTeX 和 HTML/MathML 的转换器。文档原生以 TeXmacs、XML 或 Scheme 格式保存，并可导出为 PDF 或 Postscript 文件。
*   **可扩展性：** 用户可以通过创建新的文档样式或使用 Scheme 扩展语言添加功能来自定义平台。

总之，GNU TeXmacs 为科学专业人士提供了一个统一的框架，使他们能够在单一且可扩展的环境中编写、计算和展示自己的工作。

---

## 7. 如何折叠《银翼杀手》折纸独角兽 (1996)

**原文标题**: How to fold the Blade Runner origami unicorn (1996)

**原文链接**: [https://web.archive.org/web/20011104015933/www.linkclub.or.jp/~null/index_br.html](https://web.archive.org/web/20011104015933/www.linkclub.or.jp/~null/index_br.html)

The provided text is a metadata snapshot from the **Wayback Machine (Internet Archive)** regarding a webpage titled **"How to fold the Blade Runner origami unicorn."**

Rather than containing the folding instructions themselves, the text provides archival details about the site’s history. Key points include:

*   **Subject Matter:** The page is dedicated to teaching readers how to recreate the iconic origami unicorn from the 1982 film *Blade Runner*. This specific guide, hosted by a user named "null," is historically significant within the fan community as one of the earliest online resources (dating back to 1996) to decode the prop's complex design.
*   **Archival History:** The specific capture shown is from **November 4, 2001**. The Wayback Machine has recorded 47 captures of this URL between 2001 and 2026.
*   **Source Data:** The page was preserved as part of the **Alexa Crawls** collection, a project where Alexa Internet donated web crawl data to the Internet Archive starting in 1996.
*   **Technical Details:** The original site was hosted on a Japanese service provider (`linkclub.or.jp`). 

In summary, the document serves as a digital footprint of a classic piece of "cyber-culture" history, marking the preservation of a fan-made tutorial for a famous cinematic prop.

---

## 8. Trellis AI (YC W24) is hiring deployment lead to accelerate medication access

**原文标题**: Trellis AI (YC W24) is hiring deployment lead to accelerate medication access

**原文链接**: [https://www.ycombinator.com/companies/trellis-ai/jobs/7ZlvQkN-lead-deployment-strategist](https://www.ycombinator.com/companies/trellis-ai/jobs/7ZlvQkN-lead-deployment-strategist)

Trellis AI, a Y Combinator (W24) healthcare startup and Stanford AI Lab spinout, is seeking a **Lead Deployment Strategist** to scale its AI-driven administrative platform. Based in San Francisco (with remote options), the company automates complex healthcare paperwork—including document intake, prior authorizations, and appeals—to accelerate patient access to life-saving medications.

**The Role**
The Lead Deployment Strategist will bridge the gap between internal engineering teams and enterprise healthcare clients. Key responsibilities include managing mission-critical implementations, translating technical capabilities into real-world business value, and navigating the complex IT environments of Fortune 500 customers.

**Candidate Requirements**
*   **Experience:** 3+ years in client-facing technical roles (Forward Deployment, Solutions, or Consulting).
*   **Technical Background:** A technical degree or at least one summer of engineering experience is required.
*   **Skills:** Strong project management, executive-level communication, and the ability to operate autonomously in a fast-paced startup environment. Backgrounds in top-tier consulting or private equity are preferred.

**Company Impact & Growth**
Trellis agents currently process billions of dollars in therapies across all 50 states, reducing time-to-treatment by over 90%. The company has reported 10x revenue growth in recent months and is backed by major investors, including General Catalyst and executives from Google and Salesforce. 

The position offers a salary range of **$80K – $180K** and the opportunity to join a world-class team of AI researchers and healthcare operations experts aiming to eliminate the 20% of U.S. healthcare spending lost to administrative inefficiency.

---

## 9. Racket v9.1

**原文标题**: Racket v9.1

**原文链接**: [https://blog.racket-lang.org/2026/02/racket-v9-1.html](https://blog.racket-lang.org/2026/02/racket-v9-1.html)

生成摘要时出错

---

## 10. New accounts on HN 10x more likely to use em-dashes

**原文标题**: New accounts on HN 10x more likely to use em-dashes

**原文链接**: [https://www.marginalia.nu/weird-ai-crap/hn/](https://www.marginalia.nu/weird-ai-crap/hn/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 2 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 3 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 4 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 5 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 6 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 7 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 8 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 9 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 10 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 11 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 12 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 13 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 14 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 15 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 16 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 17 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 18 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 19 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 20 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 21 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 22 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 23 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 24 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 25 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 26 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 27 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 28 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 29 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 30 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 31 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 32 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 33 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 34 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 35 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 36 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 37 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 38 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 39 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 40 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 41 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 42 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 43 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 44 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 45 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 46 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 47 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 48 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 49 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 50 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 51 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 52 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 53 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 54 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 55 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 56 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 57 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 58 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 59 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 60 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 61 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 62 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 63 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 64 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 65 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 66 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 67 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 68 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 69 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 70 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 71 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 72 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 73 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 74 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 75 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 76 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 77 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 78 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 79 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 80 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 81 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 82 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 83 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 84 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 85 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 86 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 87 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 88 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 89 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 90 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 91 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 92 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 93 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 94 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 95 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 96 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 97 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 98 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 99 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 100 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 101 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 102 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 103 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 104 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 105 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 106 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 107 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 108 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 109 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 110 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 111 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 112 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 113 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 114 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 115 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 116 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 117 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 118 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 119 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 120 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 121 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 122 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 123 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 124 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 125 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 126 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 127 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 128 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 129 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 130 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 131 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 132 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 133 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 134 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 135 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 136 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 137 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 138 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 139 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 140 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 141 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 142 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 143 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 144 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 145 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 146 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 147 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 148 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 149 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 150 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 151 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 152 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 153 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 154 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 155 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 156 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 157 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 158 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 159 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 160 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 161 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 162 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 163 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 164 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 165 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 166 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 167 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 168 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 169 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 170 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 171 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 172 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 173 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 174 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 175 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 176 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 177 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 178 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 179 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 180 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 181 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 182 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 183 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 184 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 185 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 186 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 187 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 188 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 189 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 190 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 191 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 192 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 193 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 194 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 195 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 196 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 197 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 198 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 199 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 200 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 201 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 202 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 203 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 204 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 205 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 206 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 207 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 208 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 209 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 210 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 211 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 212 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 213 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 214 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 215 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 216 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 217 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 218 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 219 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 220 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 221 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 222 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 223 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 224 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 225 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 226 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 227 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 228 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 229 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 230 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 231 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 232 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 233 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 234 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 235 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 236 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 237 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 238 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 239 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 240 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 241 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 242 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 243 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 244 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 245 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 246 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 247 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 248 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 249 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 250 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 251 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 252 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 253 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 254 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 255 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 256 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 257 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 258 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 259 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 260 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 261 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 262 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 263 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 264 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 265 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 266 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 267 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 268 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 269 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 270 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 271 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 272 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 273 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 274 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 275 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 276 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 277 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 278 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 279 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 280 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 281 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 282 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 283 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 284 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 285 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 286 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 287 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 288 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 289 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 290 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 291 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 292 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 293 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 294 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 295 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 296 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 297 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 298 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 299 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 300 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 301 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 302 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 303 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 304 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 305 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 306 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 307 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 308 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 309 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 310 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 311 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 312 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 313 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 314 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 315 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 316 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 317 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 318 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 319 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 320 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 321 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 322 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 323 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 324 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 325 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 326 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 327 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 328 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 329 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 330 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 331 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 332 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 333 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 334 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 335 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 336 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 337 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 338 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 339 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 340 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 341 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 342 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
