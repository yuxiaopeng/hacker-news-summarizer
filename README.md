# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-08.md)

*最后自动更新时间: 2025-10-08 17:48:02*
## 1. 经过二十年的调整，MAME破解了Hyper Neo Geo 64。

**原文标题**: After 2 decades of tinkering, MAME cracks the Hyper Neo Geo 64

**原文链接**: [https://www.readonlymemo.com/mame-hyper-neo-geo-support-sound-emulation/](https://www.readonlymemo.com/mame-hyper-neo-geo-support-sound-emulation/)

本文主要探讨了近期在模拟两个复古游戏平台上的进展：Hyper Neo Geo 64 和 Pioneer LaserActive。

经过二十年的努力，MAME 终于实现了对 Hyper Neo Geo 64 街机系统的正确模拟，包括正常的声音。最初，模拟能够运行，但音质很差。MAME 开发者的近期贡献，特别是 R. Belmont、Happy 和 O. Galibert，显著改善了声音模拟，使该系统真正可玩。即将发布的 MAME 0.282 版本将进一步完善音频，尤其是在具有挑战性的游戏《Xtreme Rally》中。

本文还涵盖了 Pioneer LaserActive 模拟方面出乎意料的快速进展。在成功模拟 Sega Mega LD 游戏之后，模拟开发者 Nemesis 现在已经支持在该平台上运行 NEC PC Engine 游戏。此外，还实施了重大的性能优化，允许用户从标准硬盘流畅运行 LaserActive 游戏镜像。推荐尝试的游戏包括《Vajra》、《Triad Stone》和《J.B. Harold - Blue Chicago Blues》。

---

## 2. 在法治国家，无端监视聊天内容必须是禁忌。

**原文标题**: Suspicionless ChatControl must be taboo in a state governed by the rule of law

**原文链接**: [https://digitalcourage.social/@echo_pbreyer/115337976340299372](https://digitalcourage.social/@echo_pbreyer/115337976340299372)

文章（如标题和引文所示）围绕着“无端监控聊天”在法治国家中应被视为禁忌这一观点展开。Patrick Breyer在Mastodon上的帖子（如链接digitalcourage.social所示）提到了德国司法部长和“无端……”的概念，暗示了一场关于在没有事先怀疑的情况下监控数字通信的合法性和伦理性的讨论。

核心问题是大规模监控私人通信（聊天监控）与法治国家原则之间的潜在冲突，后者优先考虑个人权利和自由。“无端监控聊天”意味着在没有任何合理理由的情况下，对公民的数字互动进行全面监控，可能侵犯隐私和言论自由。

该帖子在去中心化且注重隐私的社交媒体平台Mastodon上分享的背景，进一步强调了对数字监控的担忧。 关于使用Web应用程序需要JavaScript的说明也间接突出了对技术通信的依赖以及与之相关的潜在漏洞。

本质上，文章和链接的帖子引发了对隐私侵蚀和政府在没有合理怀疑的情况下实施监控措施时可能滥用权力的担忧，并认为这种做法与法治国家不相容。

---

## 3. 美国证监会批准德克萨斯证券交易所成立，为数十年来首个美国新增综合交易所

**原文标题**: SEC approves Texas Stock Exchange, first new US integrated exchange in decades

**原文链接**: [https://www.cbsnews.com/texas/news/sec-approves-texas-stock-exchange-txse/](https://www.cbsnews.com/texas/news/sec-approves-texas-stock-exchange-txse/)

美国证券交易委员会(SEC)已批准德克萨斯证券交易所(TXSE)成为国家证券交易所，这是几十年来美国首个新建的完全整合的证券交易所。TXSE总部位于达拉斯，旨在与纽约证券交易所(NYSE)和纳斯达克竞争，计划于2026年推出交易服务、交易所交易产品(ETP)和公司上市。

TXSE首席执行官James H. Lee强调，一致性、透明度和伙伴关系是核心价值观。德克萨斯州州长Greg Abbott赞扬该批准是对德克萨斯州经济发展的推动，巩固了该州作为金融中心的地位。

在贝莱德和城堡证券等公司的支持下，TXSE从投资者那里筹集了1.2亿美元。其总部于2024年春季在达拉斯开业。该交易所希望避免之前与纽约证券交易所或纳斯达克合并的区域性交易所的命运。

德克萨斯州拥有强大的经济，美国财富500强企业数量最多，拥有超过5,000家私募股权支持的公司，以及超过1,500家上市公司。其2.4万亿美元的经济规模超过了许多国家。

---

## 4. 我们在Go的ARM64编译器中发现了一个错误。

**原文标题**: We found a bug in Go's ARM64 compiler

**原文链接**: [https://blog.cloudflare.com/how-we-found-a-bug-in-gos-arm64-compiler/](https://blog.cloudflare.com/how-we-found-a-bug-in-gos-arm64-compiler/)

Cloudflare arm64 基础设施偶发性 panic 事件调查报告

本文详细介绍了 Cloudflare 对影响其 arm64 基础设施的偶发性 panic 事件的调查。最初，这些 panic 被认为是罕见的堆栈内存损坏而被忽略，但随着 panic 持续且加剧，调查也随之深入。这些错误表现为堆栈展开期间的崩溃，特别是在 `(*unwinder).next` 函数中，原因是致命错误表明展开不完整或由于无效内存访问导致的段错误。

通过分析 coredump 文件，该团队确定崩溃始终发生在从 `Go Netlink` 库的 `(*NetlinkSocket).Receive` 函数进行抢占期间。 这种抢占发生在函数的结尾部分，特别是在两个堆栈指针调整之间。 抢占期间堆栈状态的不一致导致堆栈展开器读取无效的堆栈指针，从而导致崩溃。

为了验证他们的假设，他们开发了一个最小化重现程序，这是一个简单的 Go 程序，它创建了一个大型堆栈帧，需要在 arm64 上将堆栈指针调整拆分为两个操作。 这个程序可靠地触发了 panic，证实该问题是与特定堆栈操作期间的异步抢占相关的 Go 运行时错误。当 Go 运行时在这两个操作码之间进行抢占时，就会发生此错误，然后堆栈展开器将读取无效的堆栈指针并崩溃。

---

## 5. Show HN: Recall：用Redis支持的持久上下文赋予Claude完美记忆

**原文标题**: Show HN: Recall: Give Claude perfect memory with Redis-backed persistent context

**原文链接**: [https://www.npmjs.com/package/@joseairosa/recall](https://www.npmjs.com/package/@joseairosa/recall)

无法访问文章链接。

---

## 6. 多克托罗：美国科技卡特尔利用应用程序违法

**原文标题**: Doctorow: American Tech Cartels Use Apps to Break the Law

**原文链接**: [https://lithub.com/how-american-tech-cartels-use-apps-to-break-the-law/](https://lithub.com/how-american-tech-cartels-use-apps-to-break-the-law/)

科里·多克托罗在其著作《垃圾化》的节选中指出，美国科技垄断集团正在利用应用程序的复杂性来规避监管并违反法律，他将这种策略称为“如果我们用应用程序来做，那就不是犯罪”。他认为，科技行业竞争的衰落导致了监管俘获，即强大的公司可以影响或逃避监管监督。

多克托罗强调，少数几家公司主导的集中行业可以轻松协调政策，并积累资源来压倒监管机构。他认为，由于放松管制而经常缺乏资源的监管机构，无法有效监督这些科技巨头。

他提供了诸如优步对司机的分类、爱彼迎对住房市场的影响以及金融科技平台等例子，来说明公司如何使用应用程序来掩盖非法活动，例如无视劳动法、高利贷法和价格操纵。他还提到了Plexure，该公司出售供应商用来提高价格的监控数据，以及RealPage，该公司向房东提供租金建议。

多克托罗还指出，知识产权法正被用来阻止用户和竞争对手修改或“去垃圾化”有问题的应用程序，从而进一步巩固了这些科技垄断集团的权力。他认为，科技公司不仅声称由于使用了应用程序而免受法律约束，还通过将修复这些应用程序以保护用户的行为定为犯罪，来维护自己的权力。他的论点核心是，应用程序提供的复杂性使得这些公司能够在现有法规无法触及的范围内运营。

---

## 7. 奥特加假说

**原文标题**: Ortega Hypothesis

**原文链接**: [https://en.wikipedia.org/wiki/Ortega_hypothesis](https://en.wikipedia.org/wiki/Ortega_hypothesis)

奥尔特加假说认为，科学进步主要由普通或平庸的科学家做出小型、专业化的累积贡献所驱动。这与“牛顿假说”形成对比，“牛顿假说”认为，重大突破主要是一些杰出科学家在彼此工作的基础上构建的结果。

引文研究普遍支持牛顿假说，表明高引用论文不成比例地引用了精英机构的精英科学家发表的其他高引用论文，这表明小研究在很大程度上依赖于少数杰出论文。然而，文章指出，引用次数可能无法准确反映科学工作的真正影响或价值，并且可能受到社会分层、肤浅的引用习惯以及理论论文比实验报告更容易被引用的趋势的影响而产生偏差。

该假说以何塞·奥尔特加·伊·加塞特的名字命名，他认为虽然一些科学工作可以由进行“机械性脑力劳动”的“令人震惊的平庸”专家完成，但真正的科学进步取决于天才们在其他天才建立的框架基础上进行构建。“奥尔特加假说”仅捕捉到奥尔特加整体理论的一小部分，误导了他的观点，即天才而非庸才是科学进步的主要驱动力。关于普通科学家与精英科学家相对贡献的争论仍未解决。

---

## 8. 现在开放构建： Gemini CLI 扩展介绍

**原文标题**: Now open for building: Introducing Gemini CLI extensions

**原文链接**: [https://blog.google/technology/developers/gemini-cli-extensions/](https://blog.google/technology/developers/gemini-cli-extensions/)

本文宣布推出 Gemini CLI 扩展，这是一个全新的框架，允许开发者自定义 Gemini CLI（一个由 AI 驱动的终端代理），并将其连接到他们偏好的工具。 这些扩展充当“增强功能”，提供与数据库、设计平台和支付服务等外部工具的预打包集成。 每个扩展都包含一个“剧本”，指导 AI 如何有效地使用新工具，无需复杂的设置即可立即获得有意义的结果。

开发者可以使用命令“gemini extensions install <GitHub URL or local path>”来安装扩展。 本文重点介绍了开放生态系统的发展，该生态系统得到了 Google、Dynatrace、Elastic、Figma、Harness、Postman、Shopify、Snyk 和 Stripe 等行业领导者以及开源社区的贡献。

本文还介绍了 Gemini CLI 扩展页面，用于发现和浏览可用的扩展。 文章重点介绍了几个启动合作伙伴，展示了用于应用程序性能监控 (Dynatrace)、Elasticsearch 数据分析 (Elastic)、设计集成 (Figma)、CI/CD 智能 (Harness)、API 管理 (Postman)、Shopify 开发 (Shopify)、安全集成 (Snyk) 和 Stripe API 交互 (Stripe) 的扩展。

本文强调，扩展通过模型上下文协议 (MCP) 增加了智能和个性化，超越了简单的连接。 还展示了 Google 创建的扩展，包括用于云原生部署（Cloud Run、GKE、gcloud、Google Cloud Observability）、应用程序构建器（代码审查、安全、Google Maps Platform、Flutter、Chrome DevTools、Firebase、Genkit）以及生成式 AI 和数据交互（Nano Banana、Looker、Data Cloud、数据库 MCP 工具箱）的扩展。 开发者可以组合扩展并链接命令来创建个性化的工具链。

---

## 9. 2025年诺贝尔化学奖

**原文标题**: Nobel Prize in Chemistry 2025

**原文链接**: [https://www.nobelprize.org/prizes/chemistry/2025/popular-information/](https://www.nobelprize.org/prizes/chemistry/2025/popular-information/)

2025年诺贝尔化学奖授予北川进、理查德·罗布森和奥马尔·亚吉，以表彰他们开发了金属有机框架（MOFs），一种具有大腔室的新型分子结构，可以捕获和释放分子。

受分子模型启发，理查德·罗布森于1989年创造了第一个MOF，展示了设计具有宽敞内部空间晶体结构的潜力。北川进秉持着在“无用”中发现价值的原则，在20世纪90年代创造了具有开放通道的稳定三维MOF。他还认识到它们与沸石等现有材料相比具有独特的灵活性。奥马尔·亚吉受控制材料创造的愿望驱动，于1995年创造了“金属有机框架”一词，并在1999年展示了MOF-5，这是一种高度稳定且空间宽敞的材料，几克重的面积相当于一个足球场。

亚吉进一步展示了MOFs的合理设计和修改，为它们的多样化应用铺平了道路。如今，MOFs被用于各种目的，包括从沙漠空气中收集水、污染物提取、二氧化碳捕获、氢气储存和水果的缓慢成熟。获奖者的开创性工作使化学家能够设计数千种不同的MOF，彻底改变了材料科学，并为各种化学应用创造了新的可能性。

---

## 10. Synology据称销量暴跌后，撤回禁止第三方硬盘的政策

**原文标题**: Synology reverses policy banning third-party HDDs after sales allegedly plummet

**原文链接**: [https://www.guru3d.com/story/synology-reverses-policy-banning-thirdparty-hdds-after-nas-sales-plummet/](https://www.guru3d.com/story/synology-reverses-policy-banning-thirdparty-hdds-after-nas-sales-plummet/)

群晖取消限制第三方硬盘政策，此前销量因政策下跌。2025年初，群晖强制用户购买其更昂贵的硬盘，导致希捷和西数等品牌的第三方硬盘几乎无法使用。此举引发用户和评测人员的强烈反对，他们批评此举贪婪，并试图锁定客户。

据报道，在限制政策实施后，群晖2025款NAS型号的销量急剧下降。随着DSM 7.3的发布，群晖悄然恢复了对第三方硬盘和2.5英寸SATA固态硬盘的支持。希捷、西数和其他品牌的硬盘现在可以像以前一样工作，具有完整的监控、警报和存储功能。

虽然群晖没有明确承认错误，但这一决定被视为对销售压力和社区强烈抗议的回应。批评人士认为，这一事件损害了群晖的声誉，因为许多用户已经转向其他品牌，或者犹豫是否购买另一款群晖产品。恢复开放硬盘支持被认为是一个积极的发展，恢复了最初使群晖受欢迎的灵活性。但这种逆转是否足以重新获得沮丧用户的信任，还有待观察。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 2 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 3 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 4 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 5 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 6 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 7 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 8 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 9 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 10 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 11 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 12 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 13 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 14 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 15 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 16 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 17 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 18 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 19 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 20 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 21 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 22 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 23 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 24 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 25 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 26 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 27 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 28 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 29 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 30 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 31 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 32 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 33 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 34 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 35 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 36 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 37 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 38 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 39 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 40 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 41 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 42 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 43 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 44 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 45 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 46 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 47 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 48 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 49 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 50 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 51 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 52 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 53 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 54 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 55 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 56 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 57 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 58 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 59 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 60 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 61 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 62 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 63 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 64 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 65 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 66 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 67 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 68 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 69 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 70 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 71 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 72 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 73 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 74 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 75 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 76 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 77 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 78 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 79 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 80 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 81 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 82 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 83 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 84 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 85 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 86 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 87 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 88 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 89 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 90 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 91 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 92 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 93 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 94 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 95 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 96 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 97 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 98 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 99 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 100 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 101 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 102 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 103 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 104 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 105 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 106 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 107 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 108 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 109 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 110 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 111 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 112 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 113 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 114 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 115 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 116 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 117 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 118 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 119 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 120 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 121 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 122 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 123 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 124 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 125 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 126 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 127 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 128 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 129 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 130 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 131 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 132 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 133 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 134 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 135 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 136 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 137 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 138 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 139 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 140 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 141 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 142 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 143 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 144 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 145 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 146 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 147 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 148 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 149 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 150 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 151 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 152 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 153 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 154 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 155 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 156 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 157 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 158 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 159 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 160 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 161 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 162 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 163 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 164 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 165 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 166 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 167 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 168 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 169 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 170 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 171 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 172 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 173 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 174 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 175 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 176 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 177 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 178 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 179 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 180 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 181 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 182 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 183 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 184 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 185 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 186 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 187 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 188 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 189 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 190 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 191 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 192 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 193 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 194 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 195 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 196 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 197 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 198 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 199 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 200 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 201 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 202 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 203 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
