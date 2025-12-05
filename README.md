# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-05.md)

*最后自动更新时间: 2025-12-05 17:50:49*
## 1. 奈飞将收购华纳兄弟

**原文标题**: Netflix to Acquire Warner Bros

**原文链接**: [https://about.netflix.com/en/news/netflix-to-acquire-warner-bros](https://about.netflix.com/en/news/netflix-to-acquire-warner-bros)

2025年12月，奈飞（Netflix）和华纳兄弟探索（WBD）宣布达成最终协议，奈飞将以827亿美元的企业价值收购华纳兄弟，包括其电影和电视工作室、HBO Max和HBO。该交易以现金和股票形式进行，每股WBD价值27.75美元。预计该收购将在WBD的全球网络部门“探索全球”分拆为一家新的上市公司后完成，预计在2026年第三季度。

此次合并旨在将华纳兄弟庞大的标志性系列特许经营和故事讲述遗产与奈飞的创新流媒体服务和全球影响力相结合。两家公司的高管强调，此次合并将为消费者提供更多选择，为创意社区创造机会，加强娱乐行业，并创造股东价值。奈飞计划维持华纳兄弟目前的运营，包括院线电影的发行。

奈飞预计到第三年每年将节省20-30亿美元的巨额成本，并预计该交易将在第二年增加GAAP每股收益。该交易需获得监管机构和股东的批准，以及其他惯例成交条件。该交易已获得两家公司董事会的一致批准，预计将在12-18个月内完成。

---

## 2. Cloudflare 2025年12月5日故障

**原文标题**: Cloudflare outage on December 5, 2025

**原文链接**: [https://blog.cloudflare.com/5-december-2025-outage/](https://blog.cloudflare.com/5-december-2025-outage/)

2025年12月5日，Cloudflare因代码部署缺陷导致约28%的HTTP流量受到影响，中断了25分钟。该缺陷旨在缓解CVE-2025-55182 React Server Components漏洞。中断发生在UTC时间08:47，原因是旨在增加WAF分析缓冲区大小的body解析逻辑变更，导致Cloudflare FL1代理出现错误。

具体而言，使用全局配置系统禁用内部测试工具传播了一项变更，触发了规则模块中的一个漏洞，导致HTTP 500错误。错误发生的原因是应用于具有“execute”动作的规则的熔断机制导致Lua异常，这是一个长期存在的、之前未被发现的代码错误。

该问题影响了使用部署了Cloudflare托管规则集的较旧FL1代理的客户。更改于UTC时间09:12被撤销，恢复了全面服务。

Cloudflare承认这次中断是不可接受的，尤其是在2025年11月18日发生类似事件之后。他们正在优先改进其部署和回滚系统，包括增强的推出和版本控制、简化的紧急修复功能以及“Fail-Open”错误处理。尽管11月18日中断后的更改正在进行中，但未能及时完成以防止12月5日的事件。Cloudflare已暂时锁定网络更改，并计划发布正在进行的弹性项目的详细分析。

---

## 3. 让RSS更有趣

**原文标题**: Making RSS More Fun

**原文链接**: [https://matduggan.com/making-rss-more-fun/](https://matduggan.com/making-rss-more-fun/)

本文详细介绍了作者如何创建 Firefox 扩展程序“TimewasterPro”，该扩展程序旨在通过提供类似 TikTok 的体验来发现小型网站的内容，从而对抗 RSS 阅读器疲劳。作者对传统 RSS 阅读器带来的乏味感以及被动消费随机内容的愿望感到沮丧，因此构建了一项服务，该服务可以提供网站、允许用户赞/踩，并使用这些投票来优先排序其他用户的内容。

该项目的后端使用 FastAPI 和 SQLAlchemy 构建，利用 SQLite 数据库，该数据库通过抓取 Kagi 小型网站 Github 存储库中的 RSS 提要来填充。该扩展程序具有基本的帐户系统（电子邮件验证），但作者对此和 JWT 身份验证表示不满，并指出用户体验问题。

作者承认该项目是一个爱好，而不是一项严肃的商业冒险，这反映在使用 System.css 库的有意的复古用户界面中。主要目标是创建一个用于个人享受和实验的工具。

目前，该扩展程序已索引超过 60 万个页面。未来的计划包括对内容进行分类以个性化推荐，并开发处理被踩内容的系统。作者希望提交更多独立的摄影、科学和手工艺网站，并承认由于技术内容的流行，非技术用户入门面临挑战。源代码将在项目达到更稳定状态时发布。该扩展程序可在 timewasterpro.xyz 下载。

---

## 4. UniFi 5G

**原文标题**: UniFi 5G

**原文链接**: [https://blog.ui.com/article/introducing-unifi-5g](https://blog.ui.com/article/introducing-unifi-5g)

UniFi 5G Max系列旨在为任何环境提供精简、灵活且强大的5G互联网解决方案。本质上，它专注于提供高性能、易于使用且兼容性广泛的5G体验。关键在于其强调无论在何种环境下都能提供可靠且高效的5G连接。

---

## 5. Framework Laptop 13 通过升级套件获得 12 核 ARM 处理器

**原文标题**: Framework Laptop 13 gets ARM processor with 12 cores via upgrade kit

**原文链接**: [https://www.notebookcheck.net/Framework-Laptop-13-gets-ARM-processor-with-12-cores-via-upgrade-kit.1177930.0.html](https://www.notebookcheck.net/Framework-Laptop-13-gets-ARM-processor-with-12-cores-via-upgrade-kit.1177930.0.html)

本文讨论了MetaComputing为Framework Laptop 13推出的一款新的基于ARM的主板升级套件，为英特尔、AMD和骁龙X系列处理器提供了一个替代方案。该主板采用CIX CP8180芯片组，拥有12个核心（8个性能核心和4个效率核心）和一个ARM Immortalis-G720 GPU。虽然性能可能不如旗舰移动芯片，但预计能够处理日常任务。

由于其潜在的高空闲功耗（16瓦），该升级主要针对开发者，这可能会显著降低Framework Laptop 13的电池续航时间。

MetaComputing ARM AI PC套件可直接从MetaComputing购买。基础型号包括主板、16GB RAM、1TB SSD和一个迷你PC机箱，售价为549美元。包含Framework Laptop 13的套装售价为999美元。升级到32GB RAM需额外支付100美元。全球免费送货，但进口费用和税款不包含在列出的价格中。

---

## 6. 大多数技术问题都是人的问题。

**原文标题**: Most technical problems are people problems

**原文链接**: [https://blog.joeschrag.com/2023/11/most-technical-problems-are-really.html](https://blog.joeschrag.com/2023/11/most-technical-problems-are-really.html)

本文认为，大多数技术问题都源于人的问题。作者讲述了自己通过重写重复代码库来解决重大技术债务的个人经历，并强调了由于开发人员对变革的抵制以及管理层缺乏理解，导致这项工作停滞不前。

核心论点是，诸如需求定义不清、不切实际的截止日期、过时的技能以及个人自负等因素会导致技术债务并阻碍进展。作者意识到，解决这些潜在的人的问题对于有效解决技术挑战至关重要。他强调，重构工作常常失败，因为它们暴露了现有软件开发实践和个人技能差距方面的系统性问题。

作者还反思了一个理想的工程世界的局限性，在这个世界里，没有截止日期和“政治”，技术解决方案应该自己说话。相反，与非技术利益相关者进行有效沟通、量化技术改进的价值以及驾驭人际关系的重要性被强调为高级工程师的必备技能。文章最后将“工程师的工程师”与“抬头编码者”进行了对比，后者将技术实力与预测风险和引导团队的能力相结合，并指出后者对于大型项目往往更有价值。

---

## 7. Netflix的AV1之旅：从安卓到电视及更远

**原文标题**: Netflix’s AV1 Journey: From Android to TVs and Beyond

**原文链接**: [https://netflixtechblog.com/av1-now-powering-30-of-netflix-streaming-02f592242d80](https://netflixtechblog.com/av1-now-powering-30-of-netflix-streaming-02f592242d80)

Netflix的AV1之旅：从安卓到电视及未来

---

## 8. Show HN: Kraa – 万能写作应用

**原文标题**: Show HN: Kraa – Writing App for Everything

**原文链接**: [https://kraa.io/about](https://kraa.io/about)

此“Show HN”帖子介绍 Kraa，据称是一款“适用于一切”的写作应用。标题表明它是一款旨在处理各种写作任务的通用工具，但提供的内容极其简单。仅重复出现了名称“Kraa”，我们可以推断：

*   **Kraa 是一款写作应用。** 这是其核心功能。
*   **它专为广泛的写作活动而设计。** “适用于一切的写作应用”表明其侧重于多功能性。

在没有更多细节的情况下，无法详细说明其功能、目标受众、平台可用性或任何潜在的竞争优势。该帖子本质上是一个占位符，宣布了 Kraa 写作应用的存在。要了解其真正的功能，需要通过外部链接或资源进一步研究 Kraa。

---

## 9. 宝马插电混动：安全熔断器更换极其昂贵

**原文标题**: BMW PHEV: Safety fuse replacement is extremely expensive

**原文链接**: [https://evclinic.eu/2025/12/04/2021-phev-bmw-ibmucp-21f37e-post-crash-recovery-when-eu-engineering-becomes-a-synonym-for-unrepairable-generating-waste/](https://evclinic.eu/2025/12/04/2021-phev-bmw-ibmucp-21f37e-post-crash-recovery-when-eu-engineering-becomes-a-synonym-for-unrepairable-generating-waste/)

无法访问文章链接。

---

## 10. X因违反内容规则被欧盟处以1.4亿美元罚款

**原文标题**: X hit with $140M EU fine for breaching content rules

**原文链接**: [https://www.reuters.com/sustainability/boards-policy-regulation/eu-fines-x-140-mln-breaching-online-content-rules-tiktok-settles-with-2025-12-05/](https://www.reuters.com/sustainability/boards-policy-regulation/eu-fines-x-140-mln-breaching-online-content-rules-tiktok-settles-with-2025-12-05/)

**摘要：**

欧盟委员会因X（原推特）未能遵守《数字服务法案》（DSA），一项旨在监管在线内容和保护用户的新欧盟法律，对其处以1.28亿欧元（约合1.4亿美元）的罚款。欧盟发现，X未能充分解决非法内容的传播问题，包括仇恨言论，也未能打击平台上的虚假信息。具体而言，欧盟指出，X缺乏有效机制来及时删除非法内容，并且未能充分透明地披露其内容审核政策。

这是DSA实施以来开出的首张重大罚单，表明欧盟致力于执行新法规。DSA要求大型在线平台对其托管的内容承担更大的责任，并采取措施保护用户免受非法和有害内容的侵害。

另据报道，TikTok已同意在2025年2月前解决欧盟对其“奖励计划”的担忧，该计划据称可能对儿童造成伤害，从而避免潜在的调查和罚款。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 2 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 3 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 4 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 5 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 6 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 7 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 8 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 9 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 10 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 11 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 12 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 13 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 14 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 15 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 16 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 17 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 18 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 19 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 20 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 21 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 22 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 23 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 24 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 25 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 26 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 27 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 28 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 29 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 30 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 31 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 32 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 33 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 34 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 35 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 36 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 37 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 38 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 39 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 40 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 41 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 42 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 43 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 44 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 45 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 46 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 47 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 48 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 49 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 50 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 51 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 52 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 53 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 54 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 55 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 56 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 57 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 58 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 59 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 60 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 61 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 62 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 63 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 64 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 65 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 66 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 67 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 68 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 69 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 70 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 71 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 72 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 73 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 74 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 75 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 76 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 77 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 78 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 79 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 80 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 81 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 82 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 83 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 84 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 85 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 86 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 87 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 88 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 89 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 90 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 91 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 92 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 93 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 94 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 95 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 96 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 97 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 98 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 99 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 100 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 101 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 102 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 103 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 104 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 105 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 106 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 107 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 108 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 109 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 110 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 111 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 112 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 113 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 114 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 115 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 116 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 117 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 118 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 119 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 120 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 121 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 122 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 123 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 124 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 125 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 126 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 127 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 128 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 129 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 130 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 131 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 132 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 133 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 134 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 135 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 136 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 137 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 138 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 139 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 140 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 141 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 142 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 143 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 144 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 145 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 146 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 147 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 148 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 149 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 150 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 151 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 152 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 153 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 154 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 155 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 156 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 157 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 158 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 159 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 160 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 161 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 162 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 163 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 164 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 165 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 166 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 167 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 168 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 169 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 170 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 171 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 172 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 173 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 174 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 175 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 176 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 177 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 178 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 179 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 180 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 181 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 182 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 183 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 184 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 185 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 186 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 187 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 188 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 189 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 190 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 191 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 192 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 193 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 194 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 195 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 196 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 197 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 198 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 199 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 200 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 201 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 202 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 203 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 204 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 205 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 206 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 207 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 208 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 209 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 210 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 211 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 212 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 213 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 214 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 215 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 216 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 217 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 218 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 219 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 220 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 221 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 222 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 223 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 224 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 225 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 226 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 227 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 228 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 229 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 230 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 231 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 232 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 233 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 234 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 235 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 236 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 237 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 238 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 239 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 240 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 241 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 242 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 243 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 244 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 245 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 246 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 247 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 248 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 249 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 250 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 251 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 252 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 253 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 254 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 255 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 256 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 257 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 258 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 259 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 260 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
