# Hacker News 热门文章摘要 (2025-10-08)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. RSS订阅阅读器领域深度解析

**原文标题**: A deep dive into the RSS feed reader landscape

**原文链接**: [https://lighthouseapp.io/blog/feed-reader-deep-dive](https://lighthouseapp.io/blog/feed-reader-deep-dive)

本文深入探讨了RSS订阅阅读器的现状，并根据部署模式（设备端、浏览器扩展、自托管、托管）和商业模式（免费、一次性付款、SaaS）对其进行了分类。文章探讨了每种部署模式的优缺点。

*   **设备端阅读器**提供数据控制、离线访问和完整的计算能力，但缺乏原生同步功能，需要手动更新。
*   **浏览器扩展**易于设置，将数据存储在本地，并与浏览器深度集成，但存储空间有限，并且需要浏览器打开才能抓取订阅源。
*   **自托管阅读器**提供完整的数据控制、持续的订阅源抓取以及从任何带有Web浏览器的设备上的可访问性，但需要更多的技术专业知识来设置和维护。它们通常是开源和免费的，主要成本是服务器托管。
*   **托管阅读器**提供最完善的用户体验、全面的功能和原生同步，由服务提供商管理。

文章还强调了使用API通过移动应用程序访问来自自托管或托管产品的数据以获得离线访问权限。最后，它讨论了新闻通讯以及如何在没有原生支持的情况下，通过利用将新闻通讯转换为RSS订阅源的服务将其集成到订阅阅读器中。文章提到了每个类别中的几种流行的产品并进行了简要描述，包括NetNewsWire、Fiery Feeds、Reeder、FreshRSS、Miniflux、Feedly和Inoreader。

---

## 12. 今天在纯 JavaScript 中使用的管道操作符

**原文标题**: Working pipe operator today in pure JavaScript

**原文链接**: [https://github.com/irony/aspipes](https://github.com/irony/aspipes)

"asPipes" 项目探索了一种纯 JavaScript 实现，模仿了提议的 `|>` 管道操作符，从而在当前的 JavaScript (ES2020+) 中实现了管道风格的组合。它利用按位或运算符 (`|`) 和 `Symbol.toPrimitive` 进行强制转换，创建了一个延迟的、异步安全的、无状态的管道。

该项目定义了 `createAsPipes()`，它返回 `pipe()` 以使用初始值启动管道，以及 `asPipe()` 以包装函数，使其可管道化。转换被注册并在调用 `.run()` 时按顺序评估，返回最终结果的 Promise。该实现很小（不到 50 行），并支持同步和异步操作。

示例演示了字符串操作、数值计算、异步 API 调用（LLM 集成）以及用于创建可重用工作流程的可组合（高阶）管道。还支持使用异步生成器的流处理，从而实现函数式响应式编程模式。

文章强调 asPipes 直接在 JavaScript 中原型化 F#-style 语义，有助于人体工程学研究，并通过实践反馈为 `|>` 提案的设计提供信息。虽然它有局限性（只有右侧可管道化的标记，可能造成工具混淆）并且不适用于生产环境，但它可以作为 JavaScript 灵活性的演示，并鼓励讨论延迟评估模型、静态分析、TypeScript 集成以及官方 `|>` 运算符的 `.run()` 方法的显式与隐式性质。

---

## 13. X光扫描揭示廉价电池的潜在风险

**原文标题**: X-ray scans reveal the hidden risks of cheap batteries

**原文链接**: [https://www.theverge.com/news/784966/lumafield-x-ray-ct-scan-lithium-ion-battery-risks-manufacturing-defect](https://www.theverge.com/news/784966/lumafield-x-ray-ct-scan-lithium-ion-battery-risks-manufacturing-defect)

Lumafield研究揭示廉价锂电池质量隐患，劣质电池易引发短路和火灾。

---

## 14. 威特帝克斯迷你

**原文标题**: Vectrex Mini

**原文链接**: [https://vectrex.com/vectrex-mini-details/](https://vectrex.com/vectrex-mini-details/)

无法访问文章链接。

---

## 15. 当 Curl 可以用，但 IntelliJ 不行时：Ollama 连接之谜

**原文标题**: When Curl Works but IntelliJ Doesn't: The Ollama Connection Mystery

**原文链接**: [https://blog.tymscar.com/posts/intellijollamaconnectionmystery/](https://blog.tymscar.com/posts/intellijollamaconnectionmystery/)

Oscar Molnar 详述了一次令人沮丧的调试经历，IntelliJ IDEA 无法连接到通过 Traefik 代理的 HTTPS 端点和直接 HTTP 端点访问的 Ollama 实例，尽管 `curl` 在这两种情况下都能完美工作。IntelliJ 中最初的“测试连接”按钮仅产生通用的“连接失败”错误。

他最初怀疑是 IntelliJ 内部的 HTTPS 不兼容或权限问题。在排除 HTTPS 限制、macOS 本地网络权限和防火墙问题后，他调查了 IntelliJ 的日志。日志显示，在直接 HTTP 连接尝试期间，出现了一个 `java.net.ConnectException: No route to host` 错误。

根本原因被确定为 JVM 在回退到 IPv4 之前，尝试了 IPv6 连接（由于 LAN 上缺乏 IPv6 配置而失败），导致连接失败。解决方法是在 IntelliJ 的自定义 VM 选项中添加 JVM 选项 `-Djava.net.preferIPv4Stack=true`。这迫使 JVM 优先使用 IPv4，从而解决了连接问题。

Molnar 强调了在面对 `curl` 和基于 Java 的 IDE 连接性之间存在差异时，检查日志的重要性，并建议在采取更极端的故障排除步骤之前，将 IPv6 优先级问题作为潜在原因进行排查。

---

## 16. 为人工智能代理构建的法律合同

**原文标题**: Legal Contracts Built for AI Agents

**原文链接**: [https://paid.ai/blog/ai-agents/paid-gitlaw-introducing-legal-contracts-built-for-ai-agents](https://paid.ai/blog/ai-agents/paid-gitlaw-introducing-legal-contracts-built-for-ai-agents)

题为“为AI代理构建的法律合同”的文章，提出了一种专门为AI代理设计的法律框架。虽然内容极其简短，但我们可以推断其核心目的：

*   **新型法律挑战：** 标题突出了对专门为自主AI代理的独特能力和风险量身定制的合同的新兴需求。现有的合同法可能无法充分解决AI决策、责任和所有权的复杂性。
*   **AI货币化：** 订阅新闻通讯的号召表明，AI代理的法律合同与更广泛的AI货币化主题之间存在联系。结构合理的合同对于实现AI技术的有效和安全商业化可能至关重要。
*   **新兴领域：** 措辞表明这是一个新兴且发展中的领域，人们越来越有兴趣了解和解决AI代理的法律方面。

本质上，这篇文章可能探讨了新的法律合同模型的开发，这些模型可以有效地管理AI代理在商业环境中的活动和责任。这可能涵盖数据使用、知识产权、AI行为的责任以及与AI实体达成的协议的执行等方面。

---

## 17. 高通将收购Arduino

**原文标题**: Qualcomm to acquire Arduino

**原文链接**: [https://www.qualcomm.com/news/releases/2025/10/qualcomm-to-acquire-arduino-accelerating-developers--access-to-i](https://www.qualcomm.com/news/releases/2025/10/qualcomm-to-acquire-arduino-accelerating-developers--access-to-i)

高通收购Arduino，加速开发者获取其领先的边缘计算和人工智能技术

高通正在收购Arduino。 此项收购的战略目标是加速开发者获取高通先进的边缘计算和人工智能（AI）技术。 尽管没有全文，无法获取具体细节，但此收购可能意味着高通有意将其强大的处理能力与Arduino广泛采用的开源硬件和软件平台相集成。

这种集成可能会通过提供更简化、更易用的途径，使开发者能够在Arduino生态系统中创建利用高通人工智能和边缘计算解决方案的创新应用程序，从而使开发者受益。 这可能会加快原型设计速度，简化开发流程，并扩大高通技术在物联网、机器人和嵌入式系统等各个领域的应用。 这项收购对两家公司以及更广泛的开发者社区来说可能是一个重要的发展，它弥合了先进硬件和开源可访问性之间的差距。

---

## 18. 说再见

**原文标题**: Say Goodbye

**原文链接**: [https://www.mooreds.com/wordpress/archives/3717](https://www.mooreds.com/wordpress/archives/3717)

面对日益增加的裁员现象，《说声再见》一文倡导对那些失业者表达一份简单的善意：发送一则简短、个性化的信息。作者认为，这个小小的举动能对身处困境的人产生重大的积极影响，在他们面临失业、经济不稳定和身份认同危机时，重新肯定他们的人性和联系感。

这篇文章提供了可供发送的信息的具体示例，根据与被裁人员的关系量身定制，侧重于认可他们的贡献并祝愿他们一切顺利。作者强调，这一行为只需付出极少的努力，却能产生巨大的情感支持。虽然文中提到了潜在的未来益处，如建立人脉的机会，但主要动机应该是简单的人道主义。

文章还列出了一份“禁忌清单”，以避免潜在的陷阱。这些包括：提供虚情假意的帮助、对雇主进行负面评价、感到有义务继续最初信息之外的对话、做出无法兑现的保持联系的承诺，以及发表可能被解释为存在法律问题的言论。最后，文章建议发起裁员的管理者不要发送此类信息，因为其中涉及复杂的情绪。总而言之，这篇文章提倡在充满挑战的时期成为一个支持和富有同情心的同事。

---

## 19. Boost.Bloom 中的批量操作

**原文标题**: Bulk Operations in Boost.Bloom

**原文链接**: [http://bannalia.blogspot.com/2025/10/bulk-operations-in-boostbloom.html](http://bannalia.blogspot.com/2025/10/bulk-operations-in-boostbloom.html)

本文探讨了 Boost.Bloom 从 1.90 版本开始引入批量操作，旨在显著提高 Bloom 过滤器中插入和查找的速度。 核心优化包括将 Bloom 过滤器数组中位置的计算与实际内存访问分离，利用预取来最大限度地减少因访问未缓存内存而导致的 CPU 停顿。

本文重点介绍了算法方面的挑战，特别是对于 `k > 1` 的查找操作，传统的非批量方法分支较多且难以流水线化。一个简单的批量实现会受到过度条件分支的影响，从而损害性能。 Boost.Bloom 的解决方案使用位掩码来跟踪哪些位置仍需要评估，使用 `std::countr_zero` 来有效跳过已终止的列，并减少不必要的迭代。这最大限度地减少了分支和多余的内存提取。

对具有 1000 万个元素的过滤器进行查找操作的性能基准测试表明，使用批量操作可以提高高达 3 倍的速度，尽管确切的改进取决于过滤器配置、大小和访问模式等因素。使用 `std::countr_zero` 减少迭代的优化策略可以应用于其他环境，以增强提前退出操作的流水线处理。文章总结说，虽然性能提升可能很大，但影响各不相同，有时甚至可能导致比常规情况下的性能更低。

---

## 20. 他们不该读的邮件

**原文标题**: The email they shouldn't have read

**原文链接**: [https://it-notes.dragas.net/2025/10/08/the-email-they-shouldnt-have-read/](https://it-notes.dragas.net/2025/10/08/the-email-they-shouldnt-have-read/)

该故事详述了一位顾问在IT领域遭遇供应商锁定和掠夺性商业行为的经历。该顾问帮助A机构从过时的Exchange服务器迁移到开源电子邮件解决方案，从而显著降低了成本并增强了对数据的控制。另一家机构B被托管服务提供商长期合同锁定的，也寻求该顾问的帮助以进行同样的迁移。他们秘密计划在合同终止后进行迁移。

然而，他们的托管服务提供商发现了他们的计划，很可能是通过监控B机构的电子邮件。该提供商利用隐藏条款和单方面合同修改来阻止B机构离开，甚至威胁另一个潜在客户C机构，阻止他们与该顾问合作。这些行为包括延长通知期、将以前免费的服务收费以及限制电子邮件访问。

该顾问怀疑该提供商不公平地限制开源采用并使用欺骗性的销售策略。这个故事突出了当机构优先避免冲突而不是做正确的事情时，可能发生的权力失衡和道德妥协，最终导致成本膨胀和创新受阻。尽管技术人员对缺乏原则感到不满，但他们无法解决这个问题，但决心以后解决它。该顾问希望这个故事能够揭露那些以“支持开源”为幌子发生的 unethical 行为。

---

## 21. Gemini 2.5 计算机使用模型

**原文标题**: Gemini 2.5 Computer Use model

**原文链接**: [https://blog.google/technology/google-deepmind/gemini-computer-use-model/](https://blog.google/technology/google-deepmind/gemini-computer-use-model/)

基于 Gemini 2.5 Pro 构建的 Gemini 2.5 Computer Use 模型是一种专门的人工智能模型，通过 Gemini API 发布，使开发者能够创建可直接与用户界面 (UI) 交互的代理。它在网页和移动控制基准测试中超越了领先的替代方案，实现了更低的延迟。开发者可以通过 Google AI Studio 和 Vertex AI 访问它。

该模型允许代理执行需要 UI 交互的任务，例如填写表格、操作交互式元素以及在登录后进行操作。它在一个循环中运行，分析用户请求、屏幕截图和操作历史记录，以生成诸如点击或打字等 UI 操作。集成了安全功能，以解决滥用、意外行为和网络诈骗。开发者还拥有安全控制，包括每步安全服务和系统指令，以防止高风险操作。

Google 团队已经在将该模型用于 UI 测试，而早期访问用户正在测试其在个人助理、工作流程自动化和 UI 测试方面的应用。该模型针对 Web 浏览器进行了优化，并在移动 UI 控制方面显示出前景，尽管尚未用于桌面操作系统级别的控制。它以公开预览版形式提供，通过 Browserbase 提供文档和演示环境，Google 鼓励开发者在开发者论坛中提供反馈。

---

## 22. 反常的有效市场假说 (2024)

**原文标题**: The paradoxical efficient market hypothesis (2024)

**原文链接**: [https://3quarksdaily.com/3quarksdaily/2024/09/the-paradoxical-efficient-market-hypothesis.html](https://3quarksdaily.com/3quarksdaily/2024/09/the-paradoxical-efficient-market-hypothesis.html)

约翰·艾伦·保罗斯探讨了有效市场假说（EMH）的悖论性，该假说认为股票价格反映了所有可得信息。他追溯了路易·巴舍利耶的这一思想，并强调了该假说的不同强度，从反映过去的价格到纳入所有信息，甚至是内幕消息。

这种悖论的产生是因为有效市场假说的真实性取决于投资者的信念。如果大多数投资者认为市场是有效的，他们就不会积极寻找被低估的股票，从而导致市场效率低下。相反，如果大多数投资者认为市场是无效的，他们寻找优势的努力将推动价格趋于有效。因此，有效市场假说只有在足够多的投资者不相信它时才可能是正确的。

保罗斯承认了他的论证中的一些过度简化之处，例如定义“足够大”的投资者群体以及定价模型出错的可能性。他还认识到接受有效市场假说存在的心理障碍，因为它削弱了投资者作为熟练市场策略家的自我形象。

最终，保罗斯得出结论，有效市场假说可能成立，但只是近似的，而且大多数时候都是如此，这归因于投资者普遍的不信任。他将此与棒球运动进行类比，.400击球手的消失归因于所有球员的整体水平提高，从而在运动中创造了一个更“有效”的市场。他认为有效市场假说甚至可以应用于预测市场，随着事件临近，预测市场会变得更加有效。

---

## 23. 氛围营造工程

**原文标题**: Vibe engineering

**原文链接**: [https://simonwillison.net/2025/Oct/7/vibe-engineering/](https://simonwillison.net/2025/Oct/7/vibe-engineering/)

在这篇2025年10月7日的文章中，作者介绍了“氛围工程”，作为对已经存在的术语“氛围编码”的对应。“氛围编码”指的是一种快速、随意且不负责任地使用人工智能进行软件开发的方法。 “氛围工程”则代表了一种更成熟的方法，经验丰富的软件工程师可以利用大型语言模型，同时对他们生成的代码保持责任。

作者强调了像Claude Code、Codex CLI和Gemini CLI等编码代理日益增长的效用，它们可以迭代代码、测试代码并修改代码，直到达到特定目标。 这使得工程师能够解决更复杂的问题并并行运行多个代理。

文章强调，有效利用大型语言模型能够促进既定的软件工程实践，如自动化测试、提前计划、全面文档、良好的版本控制、有效的自动化、代码审查和强大的质量保证。它还提到了在使用编码代理时需要一种“奇怪的管理形式”，以及强大的研究技能、预览环境和更新的估算技能。

作者承认“氛围工程”是一个略带调侃意味的术语，但认为有必要将其与随意性的“氛围编码”区分开来，因为它是一种更严谨和要求更高的手段。该术语固有的矛盾（“氛围”与“工程”）是故意的，旨在令人难忘，并引发关于人工智能在软件开发中不断演变的角色讨论。

---

## 24. 旅行黑名单的武器化

**原文标题**: The weaponization of travel blacklists

**原文链接**: [https://papersplease.org/wp/2025/10/06/the-weaponization-of-travel-blacklists/](https://papersplease.org/wp/2025/10/06/the-weaponization-of-travel-blacklists/)

本文分析了旅行黑名单的“武器化”现象，特别关注了“寂静天空”计划以及参议院听证会上讨论的相关问题。该听证会在政府停摆前不久举行，审查了不考虑政治领导层的旅客监控计划的潜在滥用。

本文强调了人们对“寂静天空”等计划的担忧，该计划曾指派联邦空中警察监视预先选定的航空旅客，并以种族、旅行历史，甚至受宪法第一修正案保护的活动等因素为目标。例如，包括1月6日在国会大厦附近使用信用卡的人和以色列军事行动的批评者。

虽然“寂静天空”计划已被国土安全部部长克里斯蒂·诺姆终止，且与该计划相关的官员已被解雇，但本文质疑了美国运输安全管理局（TSA）在没有司法监督的情况下阻止旅行或监视个人的权力。文章强调了该问题的两党性质，并引用了美国-阿拉伯反歧视委员会（ADC）的观点，强调政府可以根据掌权者来标记任何群体。

本文提倡明确的旅行合法权利，并引用了正在进行的挑战禁飞名单的法庭案件，以及政府认为旅行延误不足以构成伤害的论点。2021年提出的《旅行自由法案》被认为是解决方案，它既提供了乘坐公共交通工具旅行的法定权利，也为违规行为提供了诉讼理由。作者敦促国会恢复该法案，并将其纳入更广泛的立法中。

---

## 25. 测试一个编译器驱动的全栈Web框架

**原文标题**: Testing a compiler-driven full-stack web framework

**原文链接**: [https://wasp.sh/blog/2025/10/07/how-we-test-a-web-framework](https://wasp.sh/blog/2025/10/07/how-we-test-a-web-framework)

本文详细介绍了 Wasp（一个编译器驱动的全栈 Web 框架）的全面测试策略。Wasp 重视精心设计、可读性强的测试，如同对待生产代码一般。他们使用描述性测试，有时采用自定义 DSL 以提高清晰度，并且更看重“勇气”（捕捉错误的信心）而非追求 100% 的覆盖率。他们偏爱“类型驱动开发”而非传统的 TDD，利用强类型来指导开发。

编译器自身的测试包括单元测试和端到端 (e2e) 测试。快照测试对于跟踪代码生成变化至关重要，它会将当前编译器输出与存储在 Git 中的黄金快照进行比较。

Wasp 通过将 TypeScript 逻辑迁移到 npm 包中，解决了 Mustache 模板（用于代码生成）破坏 TypeScript 工具的问题。Wasp 应用程序的运行时测试，包括启动模板和示例应用程序，使用 Playwright e2e 测试完成。“kitchen-sink”应用程序是一个全面的示例，测试了许多框架特性，并包含在快照测试中。

为了简化测试自动化，Wasp 开发了 `wasp-app-runner`，这是一个具有 `dev` 和 `build` 命令的工具。部署测试包括在每次代码合并时自动部署 kitchen-sink 应用程序并进行冒烟测试，以及在每次发布时对所有示例应用程序进行测试。

最后，Wasp 正在整合文档测试，通过直接引用示例应用程序中的代码示例，确保示例保持最新并强制进行功能测试。他们正在通过一个名为 `code-ref-checker` 的 Docusaurus 插件来实现这一点。本文展示了他们如何通过在每次发布前测试教程来确保教程的有效性。

---

## 26. 巨型岩画：人类在更新世-全新世时期于阿拉伯沙漠繁荣发展

**原文标题**: Monumental rock art: humans thrived in Arab. Desert during Pleistocene-Holocene

**原文链接**: [https://www.nature.com/articles/s41467-025-63417-y](https://www.nature.com/articles/s41467-025-63417-y)

本文提供了证据，表明在更新世-全新世过渡期（约16,000至11,400年前），人类曾在阿拉伯北部内夫德沙漠居住。此前，人们认为由于极端干旱，该时期基本上无人居住。研究团队发现，在约16至13千年间，盐湖（季节性水体）在该地区建立，提供了淡水来源，从而促进了人类的扩张。

对12.8至11.4千年间的地层考古遗址的挖掘表明，这些早期人类群体利用了这些季节性水体的网络。他们用骆驼、北山羊、马科动物、瞪羚和欧洲野牛等动物的巨大岩石雕刻标记了重要的地点和通道。

这些岩画包括真人大小和自然主义的描绘，被分为四个阶段。最早的阶段表现出风格化的女性形象，随后是较大的人类形象。后来的阶段展示了详细的动物形象，随着时间的推移，过渡到更风格化的带有卡通特征的描绘。

盐湖沉积物的光释光测年支持了该地区从约16千年前在JMI和13千年前在ARN开始建立地表水的说法，表明在末次盛冰期之后，情况向更潮湿的方向转变。研究人员得出结论，岩画和相关的考古沉积物表明，人类在阿拉伯北部存在的时间比以前所知的更长，证明了人类对不断变化的环境的适应。此外，在这些遗址发现的石器类型表明与黎凡特的晚期旧石器时代晚期和前陶器新石器时代人群持续存在联系。

---

## 27. 展示一下：哦耶 – 我为儿子们制作的日常管理应用

**原文标题**: Show HN: Oh Yah – Routine management app I built for my sons

**原文链接**: [https://ohyahapp.com](https://ohyahapp.com)

Oh Yah! 是一款为5-12岁儿童设计的日常管理应用程序，旨在通过结构化的日常流程和持续完成来帮助他们养成更好的习惯。它提供诸如具有禁用导航功能的专注计时器以最大限度地减少任务期间的干扰、用于问责制的照片证明提交、用于明确优先级的结构化任务顺序（有序和无序）、以及具有24小时后自动批准的家长审核系统等功能。该应用程序支持多个配置文件（最多8个），适用于有多个孩子的家庭，并拥有简洁的界面，以最大限度地减少干扰。

该应用程序解决了家庭面临的常见挑战，例如儿童难以养成习惯、压力大的早晨/放学后时间、无效的奖励表、令人难以承受的复杂性，以及在无需不断唠叨的情况下培养独立性的愿望。Oh Yah! 旨在提供一个适用于整个家庭的解决方案。

其工作流程包括孩子选择他们的个人资料，为每个任务启动专注计时器，完成任务并提交照片证明，然后家长审核任务并奖励星星。如果家长在24小时内未进行审核，则该任务将被自动批准。

---

## 28. 数学家在分形混沌中发现素数模式

**原文标题**: Mathematicians discover prime number pattern in fractal chaos

**原文链接**: [https://www.scientificamerican.com/article/mathematicians-discover-prime-number-pattern-in-fractal-chaos/](https://www.scientificamerican.com/article/mathematicians-discover-prime-number-pattern-in-fractal-chaos/)

《科学美国人》文章探讨了通过将素数与分形混沌联系起来，理解其看似随机分布的最新突破。几个世纪以来，数学家们一直在寻找素数的规律，素数只能被自身和1整除。文章强调了黎曼zeta函数的重要性，它是一种有助于估计和校正素数分布不规则性的工具。黎曼猜想认为zeta函数的所有零点都位于一条特定的线上，但它仍未被证明，并且是研究的主要焦点。

最近的研究表明，大量素数的分布在统计上类似于某些类型的随机序列，从而导致使用“随机测度”作为理解其行为的工具。一项关键的发现是黎曼zeta函数的零点间距与重原子核的能级之间的相似性。

最近，数学家们发现了素数与高斯乘性混沌之间的联系，高斯乘性混沌是一种在混沌系统和分形中发现的随机性。Adam Harper证明了这种分形随机性可以用来描述与zeta函数零点相关的统计数据。此外，Harper、Xu和Soundararajan发现了如何预测素数集合中何时出现混沌行为。这项工作甚至导致了一种在短区间内计算素数的新方法，超越了黎曼的原始方程，尽管它依赖于物理学的一个猜想。

虽然这些发现并没有使素数具有确定性，但它们为这些基本数学“原子”的潜在模式和统计行为提供了新的见解。数学家们将继续探索概率模式，以理解素数的更深层含义。

---

## 29. 像软件公司一样思考

**原文标题**: Seeing like a software company

**原文链接**: [https://www.seangoedecke.com/seeing-like-a-software-company/](https://www.seangoedecke.com/seeing-like-a-software-company/)

本文将詹姆斯·C·斯科特的《国家的视角》应用于软件公司，认为对可读性的追求——使工作可衡量、可报告和可预测——往往以牺牲效率为代价。虽然小型公司凭借不可读的、工程师驱动的工作蓬勃发展，但大型公司优先考虑可读性，以管理企业交易和促进长期规划，即使这会减慢开发速度。

在科技领域，可读性意味着了解哪些项目正在进行、哪些项目已经发布，并能够规划和指导资源。为了实现这一点，大型公司会对工程师和项目进行简化的假设，这些假设虽然通常不准确，但对于规划和对外沟通来说“足够真实”。

本文还强调了大型公司内部存在受认可和不受认可的不可读区域。受认可的区域，如“突击队”，是绕过正式流程的紧急问题的临时解决方案。不受认可的不可读性表现为后备渠道——工程师和团队之间非正式的沟通与协作——绕过缓慢的官方渠道。这些后备渠道对于快速完成工作至关重要，但它们依赖于人际关系，公司难以量化或控制。作者断言，这些非官方渠道对于官方的、可读流程的运作至关重要。

---

## 30. 宜家家居产品目录 1951-2021

**原文标题**: IKEA Catalogs 1951-2021

**原文链接**: [https://ikeamuseum.com/en/explore/ikea-catalogue/](https://ikeamuseum.com/en/explore/ikea-catalogue/)

该档案库提供1951年至2021年宜家目录的数字化访问，展现了该品牌的发展历程以及家居领域的社会趋势。目录最初由英格瓦·坎普拉德撰写，后规模和发行范围不断扩大，反映了每个时代的精神。2021年版目录是最后一版印刷版本。

常见问题解答强调，瑞典语目录被数字化是为了让宜家的历史更容易获取，展示了过去几十年家居设计和生活的变化。早期的目录中没有人，而后来的版本反映了不断变化的趋势，从70年代的孩子和吸烟，到90年代的缩小版斯堪的纳维亚设计。目前，该档案库主要集中在瑞典语目录上，但计划扩展到其他国家。

目录展示了部分产品（从1970年代起，占30-50%），但较小的物品和临时系列通常被排除在外。产品信息是可用的，但较老的产品可能更难研究。1951年之前，宜家是一家邮购公司，销售各种商品，而非家具，这些商品在“ikéa-nytt”小册子中展示。

实体目录在宜家博物馆存档保存，但鼓励数字化访问。用户可以分享目录链接和最多30张图片（需注明版权并链接到宜家目录），用于非商业目的。宜家博物馆还提供新闻资料。虽然他们目前不需要额外的目录副本，但欢迎就独特的收藏品进行联系。博物馆没有旧的组装说明书。该网站还提供社论、视频、产品故事、设计师肖像以及对居家生活的见解。

---

## 31. GitHub 将优先迁移到 Azure，而非开发新功能。

**原文标题**: GitHub Will Prioritize Migrating to Azure over Feature Development

**原文链接**: [https://thenewstack.io/github-will-prioritize-migrating-to-azure-over-feature-development/](https://thenewstack.io/github-will-prioritize-migrating-to-azure-over-feature-development/)

这是The New Stack新闻通讯的订阅表格。它承诺周一至周五向订阅者的收件箱发送与大规模软件开发相关的重要新闻和独家内容。

表格需要一个电子邮件地址进行订阅，并为之前取消订阅的用户提供重新订阅选项。它强调The New Stack不会出售或与无关联的第三方分享订阅者信息，并概述了其使用条款和隐私政策。

在基本订阅信息之后，该表格会收集订阅者职业背景的数据，包括名字、姓氏、公司名称、国家、邮政编码、职位级别、职位角色、公司规模、组织类型和行业。还会请求一个可选的LinkedIn个人资料URL。

完成后，新订阅者会收到一条欢迎消息和说明，告知他们查看收件箱中的确认电子邮件，以便调整他们的偏好并加入其他群组。欢迎消息还鼓励用户在LinkedIn上关注The New Stack并查看精选故事。

---

## 32. 线性代数图解入门

**原文标题**: An illustrated introduction to linear algebra

**原文链接**: [https://www.ducktyped.org/p/an-illustrated-introduction-to-linear](https://www.ducktyped.org/p/an-illustrated-introduction-to-linear)

本文以图文并茂的方式介绍了线性代数，通过一个食物（牛奶和面包）的例子，对比了“行图像”和“列图像”两种方法。作者首先回顾了高斯消元法，一种求解线性方程组的方法（用五分镍币和一分硬币，然后用牛奶和面包进行演示）。

“行图像”将每个方程可视化为图上的一条线，解是表示满足两个方程的面包和牛奶组合的交点。

“列图像”引入了向量和单个向量方程。它将问题重新解释为寻找适量的牛奶和面包向量，以“加起来”成为一个目标向量（代表所需的碳水化合物和蛋白质）。这可以通过图形方式添加缩放向量来直观地表示。文章演示了向量的代数运算：标量乘法和向量加法，展示了它如何与食物例子相匹配。

文章最后介绍了矩阵符号，作为表示相同方程组的一种紧凑方式。它强调这与行图像和列图像中描述的方程组相同。作者预告了未来的章节，这些章节将深入探讨点积和线性代数中的其他概念。目的是表明线性代数处理的是数字数组（向量、矩阵），而不仅仅是数字。

---

## 33. Show HN: Timelinize – 在本地私密地整理来自各处您自己的数据

**原文标题**: Show HN: Timelinize – Privately organize your own data from everywhere, locally

**原文链接**: [https://timelinize.com](https://timelinize.com)

Timelinize 是一个开源、自托管的个人存档套件，旨在从各种来源创建统一的个人生活数据时间线，并将其存储在本地计算机上。与仅依赖基于云的服务相比，它旨在提供更完整和私密的个人历史视图。

Timelinize 聚合来自 Facebook、Google Photos、iMessage 等平台的数据，例如照片、视频、消息、位置、社交媒体帖子等等。它并非要取代现有应用程序，而是作为数据的永久存档。

主要功能包括时间线视图、用于在地理上可视化数据点的地图、用于连接跨平台交互的对话以及用于浏览媒体的图库。它提供高速导入、支持 Live Photos，并使用实体感知处理来识别和合并与同一人或地点相关的数据。一个显著的特点是它能够通过利用上下文信息来对数据进行地理定位，而无需明确的坐标。

该软件还为高级用户提供 CLI 和 HTTP API，并通过将所有内容存储在磁盘上的文件夹中来确保数据可移植性，包括 SQLite 数据库和原始数据文件。未来的开发计划包括时间线注释、公共数据集成、安全数据共享以及具有直接同步功能的移动应用程序等功能。

---

## 34. 非官方就业数据出炉，情况不容乐观。

**原文标题**: The Unofficial Jobs Numbers Are in and It's Rough Out There

**原文链接**: [https://www.wsj.com/economy/jobs/the-unofficial-jobs-numbers-are-in-and-its-rough-out-there-3518e239](https://www.wsj.com/economy/jobs/the-unofficial-jobs-numbers-are-in-and-its-rough-out-there-3518e239)

无法访问文章链接。

---

## 35. 2025年诺贝尔物理学奖

**原文标题**: Nobel Prize in Physics 2025

**原文链接**: [https://www.nobelprize.org/prizes/physics/2025/popular-information/](https://www.nobelprize.org/prizes/physics/2025/popular-information/)

2025年诺贝尔物理学奖授予约翰·克拉克、米歇尔·H·德沃雷和约翰·M·马丁尼斯，以表彰他们利用超导电路在宏观尺度上展示量子力学性质的开创性实验。他们的工作表明，通常在单个粒子中观察到的奇异的量子隧穿现象，可以在一个大到可以握在手中的系统中观察到，该系统涉及数十亿个库珀对，这些库珀对像一个单一的量子单元一样运作。

获奖者创建了一个约瑟夫森结，即由薄绝缘体隔开的两个超导体，并证明了该系统可以隧穿出零电压状态，产生电压，尽管经典物理学上缺乏这样做的能量。他们还表明，该系统仅以特定的、量子化的量吸收和释放能量，进一步巩固了其量子特性。

这项研究建立在早期关于超导和量子隧穿的研究之上，将诸如α衰变和库珀对等微观现象与宏观观察联系起来。他们的实验提供了一个独特的视角，因为观察到的量子效应来自许多粒子集体行为的宏观状态，这与其他由单个微观组分构建的宏观量子现象不同。

他们的工作为实验和量子技术（如量子计算）提供了一种新的“人造原子”，其中量子化的能级被用作量子比特。这些发现促进了物理实验室的实际应用，并加深了对量子世界的理论理解，并将之与薛定谔的猫的思想实验相比较，以突出量子性质在更大尺度上的持续存在。

---

## 36. 在线上，女性被描绘得比男性年轻，而人工智能加剧了这种偏见。

**原文标题**: Women portrayed as younger than men online, and AI amplifies the bias

**原文链接**: [https://newsroom.haas.berkeley.edu/news-release/women-portrayed-as-younger-than-men-online-and-ai-amplifies-the-bias/](https://newsroom.haas.berkeley.edu/news-release/women-portrayed-as-younger-than-men-online-and-ai-amplifies-the-bias/)

本文着重指出了一种令人担忧的偏见：女性的在线形象往往比男性显得更年轻。尽管省略了具体的方法和具体发现，但核心论点是这种与年龄相关的差异确实存在，并且人工智能进一步加剧了这一现象。本质上，由于训练数据或算法中存在的偏见，人工智能系统会强化并放大在在线环境中将女性描绘得比男性更年轻的趋势。本文可能讨论了这种偏见的潜在影响，例如使年龄歧视和性别歧视长期存在，强化女性的价值与年轻挂钩的有害刻板印象，并可能影响女性在各个领域的机会。文章还提到了一个单独的、不相关的观点：关于人工智能如何协助职场学习的技巧。虽然这不是重点，但它提出了一种人工智能的积极应用，与它在放大女性在线形象中与年龄相关的偏见方面的消极作用形成对比。

---

## 37. 全球乡村建设工具包

**原文标题**: Global Village Construction Set

**原文链接**: [https://www.opensourceecology.org/gvcs/](https://www.opensourceecology.org/gvcs/)

全球乡村建设套装（GVCS）是一个开源项目，旨在开发一个模块化、DIY、低成本、高性能的平台，用于制造构建具有现代舒适的可持续文明所需的50种基本工业机器。该项目以远低于商业成本的价格开发开源工业机器，并免费在线分享设计。

GVCS被设想为一个可扩展的、模块化的乐高式建筑套装，由机器建筑套装组成，例如制造建筑套装。目标是终身设计和低维护，力求每台机器每年只需几个小时的维护。

该项目于2007年从压缩土砖机开始，稳步提高了机器性能和生产效率。2013年，GVCS工具被用于建造一座微型房屋。该项目旨在建立一个可复制的研讨会模型，整合教育和生产，以便广泛分发开放企业模型。

该项目的完成指标是一个可复制的、开源的、社会化生产模型，称为学习因子-e模型，其步骤从概念验证到开放企业模型。到2018年，大约三分之一的50台机器已完成。该项目旨在通过简单、模块化、可扩展的设计和开源协作来打破成本壁垒。

---

## 38. Show HN: 我在做一个给逆向工程师用的浏览器

**原文标题**: Show HN: I'm building a browser for reverse engineers

**原文链接**: [https://nullpt.rs/reverse-engineering-browser](https://nullpt.rs/reverse-engineering-browser)

Show HN: 我正在为逆向工程师构建一款浏览器" 详细介绍了一款定制浏览器的创建过程，该浏览器旨在辅助 Web 逆向工程，尤其是在绕过反爬虫措施方面。作者 veritas 最初的目标是创建一个 Chrome 扩展程序来钩住 JavaScript 函数，例如 `Array.prototype.push`，但遇到了内容脚本的隔离问题。

他们并未因此气馁，而是探索了 Chrome DevTools 协议 (CDP)，并成功地使用 `Page.addScriptToEvaluateOnNewDocument` 在页面自身的脚本之前注入钩子。这促使他们开发了一款基于 Electron 的浏览器，其 UI 可以显示被钩住的函数事件，从而揭示来自 TikTok 等网站的宝贵遥测数据。

然而，该项目遇到了 Cloudflare 的 Turnstile 的阻碍，后者使用了进程外 iframe (OOPIF)，阻止了钩子的运行。为了克服这个问题，veritas 利用了 `Target.attachedToTarget` CDP 事件来动态附加到新的框架，并将钩子注入到 OOPIF 中。

作者随后遇到了反爬虫技术检测 JavaScript 运行时补丁（例如，通过 `toString()`）的问题。由于不断修补漏洞的 "打地鼠" 游戏令人沮丧，veritas 决定 fork Chromium 并直接在 Blink 引擎中进行修补。

这涉及到创建一个名为 "Snitch" 的自定义 CDP 域，以从浏览器的核心发出事件。在克服了构建问题并对现有 CDP 域进行逆向工程之后，他们成功地集成了 "Snitch"，使浏览器能够在更深层次上捕获 API 调用，绕过许多反爬虫检测机制。该浏览器的目标是成为逆向工程师分析和规避浏览器指纹识别和反爬虫技术的强大工具。

---

## 39. 对一百万年头骨的研究指向现代人类更早的起源

**原文标题**: Study of 1M-year-old skull points to earlier origins of modern humans

**原文链接**: [https://www.theguardian.com/science/2025/sep/25/study-of-1m-year-old-skull-points-to-earlier-origins-of-modern-humans](https://www.theguardian.com/science/2025/sep/25/study-of-1m-year-old-skull-points-to-earlier-origins-of-modern-humans)

对在中国发现的百万年历史的郧县2号头骨的新分析表明，现代人类的起源可能比之前认为的更古老、更复杂。该头骨最初被归类为直立人，但科学家现在认为它可能属于龙人，一个与丹尼索瓦人密切相关的群体。

基于先进的CT成像和数字重建的重新分类，将现代人类、尼安德特人和丹尼索瓦人的分化时间至少提前了40万年。这表明我们的祖先比目前认为的更早地分化成不同的群体。

该研究提出了这些群体的共同祖先，以及潜在的首批智人，可能起源于西亚而非非洲的可能性。对更广泛的化石样本的分析表明，在过去的80万年中，大脑容量大的人类沿着五个主要分支进化：亚洲直立人、海德堡人、智人、尼安德特人和龙人（包括丹尼索瓦人）。

虽然这项研究为解决100万至30万年前人类化石的复杂性提供了一种潜在的方案，但它与一些基因分析相矛盾。因此，这些结论被认为是存在争议的，需要通过额外的化石和基因证据进一步证实。

---

## 40. Metriport (YC S22) 正在招聘创始招聘人员

**原文标题**: Metriport (YC S22) is hiring a founding recruiter

**原文链接**: [https://www.ycombinator.com/companies/metriport/jobs/uq6CuhA-founding-recruiter](https://www.ycombinator.com/companies/metriport/jobs/uq6CuhA-founding-recruiter)

Metriport是一家由Y Combinator (S22)支持的初创公司，提供开源的医疗数据智能平台。现招聘创始招聘专员，以组建和扩大团队。该公司拥有90多家客户和数百万美元的年度经常性收入，资金充足，正在寻找一位能够领导端到端招聘工作的人才，涵盖从工程到客户成功的所有职能。

理想的候选人应具备3年以上招聘经验、强烈的责任感、创业思维，以及对初创企业人才的“品味”。具备工程背景者优先。招聘专员将负责人才品牌管理、寻访、面试、录用和入职，以及部分人力资源和薪资工作。

Metriport重视有意义的工作、胜任力而非声望，以及高度自主的扁平化组织结构。创始人节奏很快，但员工可以自由安排自己的时间。

该职位提供具有竞争力的薪资（11万美元 - 15万美元）和股权（0.02% - 0.10%），以及健康保险、带匹配的401(k)计划、灵活的工作安排、免费午餐、季度异地活动和无限PTO等福利。他们正在寻找位于或愿意搬迁至旧金山湾区的人才。

---

## 41. 为最远视距打包世界

**原文标题**: Packing the world for longest lines of sight

**原文链接**: [https://tombh.co.uk/packing-world-lines-of-sight](https://tombh.co.uk/packing-world-lines-of-sight)

本文详细介绍了一个旨在利用“总可视域”算法，在海量全球高程样本数据集上寻找地球上最长视线的副项目。

作者首先解释了可视域的概念，以及如何根据峰值高度和地球曲率计算理论上的最大视线距离。然后，文章介绍了“总可视域表面（TVS）”热图，该热图可视化了从区域中每个点可见的表面积。

核心挑战是如何高效地用TVS瓦片覆盖整个地球，以识别最长视线，同时优化以实现最小重叠和瓦片尺寸。作者概述了所使用的算法：它涉及创建较低分辨率的高程数据，根据峰值高程生成TVS瓦片，并策略性地添加瓦片以覆盖全球，最初优先考虑非重叠瓦片，然后允许重叠以填补空白。其中包括一项优化，即如果可以扩展附近的现有瓦片，则避免添加新的重叠瓦片。

结果显示了用蓝色方块（TVS瓦片）平铺的世界，揭示了显着的重叠和可能过大的瓦片。作者承认解决方案的非最佳性质，但认为这是下一阶段的实用起点：计算每个瓦片的可视域。文章最后呼吁对更有效的打包算法提出建议，并邀请读者关注该项目的进展。

---

## 42. 少即是多：用小型网络进行递归推理

**原文标题**: Less is more: Recursive reasoning with tiny networks

**原文链接**: [https://alexiajm.github.io/2025/09/29/tiny_recursive_models.html](https://alexiajm.github.io/2025/09/29/tiny_recursive_models.html)

本文介绍了微型递归模型 (TRM)，这是一种新颖的递归推理方法，它使用令人惊讶的小型700万参数神经网络在 ARC-AGI 基准测试中取得了令人印象深刻的成果。作者反对当前仅仅依靠大规模、昂贵的基础模型来完成复杂任务的普遍趋势，并认为推理机制的创新至关重要。

TRM 受分层推理模型 (HRM) 的启发，但对其进行了简化。它通过递归过程迭代地改进对给定问题的答案。该模型从嵌入的问题 (x)、初始嵌入的答案 (y) 和一个潜在变量 (z) 开始。对于一定数量的步骤 (K)，该模型通过以下方式改进“y”：1) 根据“x”、“y”和当前的“z”重复更新潜在变量“z”（递归推理），以及 2) 根据当前的“y”和“z”更新答案“y”。

其核心思想是，这种迭代改进允许模型以高度参数高效的方式逐步纠正错误并改进其答案，从而最大限度地减少过度拟合。这种方法表明，利用递归推理的小型模型可以在不需要大量资源的情况下，在具有挑战性的问题上取得显著的性能。作者强调，该模型的有效性源于一种简化的递归推理方法，而不是生物学类比或复杂的数学框架。

---

## 43. 加拿大法案拟在无搜查令情况下剥夺“特定人士”的互联网访问权限

**原文标题**: Canadian bill would strip internet access from 'specified persons', no warrant

**原文链接**: [https://nationalpost.com/opinion/canadian-bill-would-strip-internet-access-from-specified-persons](https://nationalpost.com/opinion/canadian-bill-would-strip-internet-access-from-specified-persons)

本文讨论了加拿大C-8法案，该法案提议修订《电信法》，允许联邦政府在没有搜查令的情况下，单方面切断“特定人员”的网络访问。 公共安全部长加里·阿南达桑加里为该法案辩护，认为这是打击网络威胁、黑客和敌对国家行为者的必要措施。 工业部长（现任梅兰妮·乔利）将与公共安全部长协商后发布命令，电信供应商将被要求遵守。

批评人士认为，该法案赋予政府过度权力，可以在没有正当程序的情况下控制互联网访问和收集数据，可能侵犯人权并破坏加密。 他们强调了该法案与加拿大此前通过“网络自由联盟”对互联网自由的承诺之间的矛盾。 加拿大公民自由协会也批评了该法案，指出它可能会削弱加密标准，并对私营公司施加监控义务。

该法案被宣传为打击网络威胁的一种方式，但批评者认为这是政府对互联网控制的令人担忧的扩张。 文章还提到了加拿大最近的其他法律，如《在线新闻法》和《在线流媒体法》，这些法律对互联网引入了新的法规，包括内容控制和新闻机构的赔偿要求。 目前，除了保释条件外，政府没有切断互联网访问的机制。

---

## 44. 德国政府反对聊天监控

**原文标题**: German government comes out against Chat Control

**原文链接**: [https://xcancel.com/paddi_hansen/status/1975595307800142205](https://xcancel.com/paddi_hansen/status/1975595307800142205)

德国CDU/CSU党公开反对欧盟他国倡导的“聊天监控”措施，此举被视为欧盟隐私倡导者的重大胜利。

最初发布此消息的Patrick Hansen强调了德国政府立场的重要性。“anlasslose”一词，意为“无故”或“无动机”，值得注意，这表明虽然反对一刀切的聊天监控，但有针对性的措施可能仍在考虑之中。

对此消息的反应褒贬不一，从热烈支持和欣慰到怀疑和谨慎乐观。有些人对CDU的立场表示惊讶，而另一些人则警告不要过早庆祝，认为该立场可能会因联盟伙伴的影响或未来的发展而改变。人们还对引入数字身份证等其他形式的数字控制的可能性表示担忧。一些评论员特别批评了排除“anlasslose”一词的做法，而另一些人认为这将影响其他欧盟国家的决策。普遍共识是，虽然这是一个积极的进展，但仍需保持警惕以保护数字隐私。

---

## 45. Lua 的演进，续 [pdf]

**原文标题**: The evolution of Lua, continued [pdf]

**原文链接**: [https://www.lua.org/doc/cola.pdf](https://www.lua.org/doc/cola.pdf)

所提供的文本看似PDF文件的部分代码，而非关于Lua演变的可读文章。它包含PDF语法、使用FlateDecode压缩的数据流，以及对PDF结构中对象（如交叉引用表、目录、页面和资源）的引用。

因此，无法从这些数据中总结文章关于“Lua演变”的内容。这段代码仅仅是PDF文档本身的内部表示，而非PDF旨在显示的文本和信息。它需要专业的PDF解析才能提取潜在的可读内容（如果存在），即使如此，也无法保证此片段代表整个文档，或者可以从中得出关于Lua演变的有意义的信息。

---

## 46. 梯度下降法是如何运作的？

**原文标题**: How does gradient descent work?

**原文链接**: [https://centralflows.github.io/part1/](https://centralflows.github.io/part1/)

梯度下降在深度学习中的运作机制：一种新视角

本文探讨了最简单的优化算法——梯度下降在深度学习中的运作机制，挑战了传统分析并提出了一种新的视角。传统分析基于损失landscape的二次近似，认为梯度下降应保持在“稳定区域”内，即曲率（Hessian矩阵的最大特征值）小于2/η（其中η是学习率）。如果曲率超过此阈值，二次近似预测会发散。

然而，实验表明，深度学习中的梯度下降经常会离开这个稳定区域。曲率上升直到达到2/η的阈值，此时沿着Hessian矩阵最大特征向量方向的振荡开始，振荡幅度增大并导致损失尖峰。 令人惊讶的是，曲率随后下降，振荡减小，损失减少。 这种现象被称为“边缘稳定性训练（EOS）”。

本文引入了三阶泰勒展开来解释这种行为。关键的见解是，沿着Hessian矩阵最大特征向量方向的振荡会自动触发Hessian矩阵最大特征值（曲率）的降低。 具体来说，泰勒展开中的三阶项表明，每个梯度步长都隐式地对曲率采取了负梯度步长，该步长与振荡幅度的平方成正比。 这就产生了一种负反馈机制：当曲率超过2/η时，振荡增加，进而降低曲率，将过程引导回稳定区域。 这种EOS行为在各种网络架构和数据集中均可观察到。

---

## 47. 发布 HN：LlamaFarm (YC W22) – 分布式 AI 开源框架

**原文标题**: Launch HN: LlamaFarm (YC W22) – Open-source framework for distributed AI

**原文链接**: [https://github.com/llama-farm/llamafarm](https://github.com/llama-farm/llamafarm)

LlamaFarm 是一个开源框架，旨在简化检索增强和代理式人工智能应用的创建。它强调本地优先的开发者体验，并提供统一的 CLI ("lf") 来管理项目、数据集和聊天会话。虽然提供了 Ollama 和 Chroma 等预设选项，但 LlamaFarm 的构建具有高度的可扩展性，允许开发者通过 YAML 配置来替换运行时、嵌入器和数据库等组件，而无需进行大量的代码重写。

主要功能包括生产就绪的架构、可通过 YAML 定义的可组合 RAG 管道以及与 OpenAI 格式兼容的全面 REST API。该 CLI 提供了项目初始化、堆栈管理、交互式聊天、单提示查询、数据集管理（创建、上传、处理）和语义查询的工作流程。

LlamaFarm 提倡拥有您的人工智能堆栈，支持本地模型，并提供与 vLLM 或 Together 等托管服务的无缝集成。其核心价值主张在于其配置优于代码的方法、模式验证的 YAML 配置以及开发者友好的 CLI。

可扩展性是核心设计原则，提供了用于添加新提供程序、向量存储、解析器、提取器和 CLI 命令的指南。该框架包括用于 FDA 文件分析和城市规划应用的示例，并附带全面的开发和测试说明。通过 Discord、GitHub Issues 和 Discussions 提供社区支持。LlamaFarm 根据 Apache 2.0 许可获得许可。

---

## 48. 消除飞行凝结尾迹可能很便宜

**原文标题**: Eliminating contrails from flying could be cheap

**原文链接**: [https://www.sustainabilitybynumbers.com/p/eliminating-contrails](https://www.sustainabilitybynumbers.com/p/eliminating-contrails)

本文探讨了通过消除飞机尾迹（飞机留下的白色尾迹）来显著降低航空业对气候影响的潜力。尽管消除飞行中的二氧化碳排放成本高昂，但解决飞机尾迹问题可能出乎意料地廉价且有效。

飞机尾迹通过捕获外向辐射来加剧全球变暖，这种影响相对于二氧化碳排放来说是短暂的。一小部分航班（约3-5%）造成了大部分（80%）的飞机尾迹增温。提出的解决方案是将这些航班绕行大气中易于形成尾迹的区域，通常只需绕行约1%，增加几分钟的飞行时间。

据估计，实施这种改道的成本非常低，每位乘客只需几美分到50美分左右，相当于每避免一吨二氧化碳当量只需几美元。这比可持续航空燃料便宜得多。

尽管成本低廉，且有可能大幅降低气候影响（有可能使航空业的变暖效应减半），但航空公司在采取飞机尾迹规避措施方面进展缓慢。这种不情愿归因于整个机队的总体成本，更重要的是，公众缺乏意识，使得航空公司能够避免受到审查。文章认为，需要政府政策，例如强制执行飞机尾迹规避，或者仅仅要求航空公司报告非二氧化碳的影响，以推动该领域的进展。

---

## 49. 同理心入门

**原文标题**: Empathy for Dummies

**原文链接**: [https://quarter--mile.com/empathy-for-dummies](https://quarter--mile.com/empathy-for-dummies)

好的，我可以做到。基于标题和有限的信息，很难给出全面的总结。不过，根据提供的上下文，我可以推断并提出以下建议：

**摘要（假设）：**

鉴于标题为“Empathy for Dummies”（同理心入门），这篇文章很可能旨在以一种简单易懂的方式介绍同理心的概念。 它可能会将同理心分解为核心组成部分，解释它是什么、为什么重要以及如何培养它。

这篇文章很可能涉及：

*   **定义同理心：** 它可能会将同理心解释为理解和分享他人感受的能力。 这可能包括将其与同情区分开来。
*   **同理心的重要性：** 它可能会强调同理心在人际关系、职业环境和社会整体中的好处。 这可能包括改善沟通、解决冲突和建立更牢固的联系。
*   **培养同理心：** 它可能会提供实用的技巧和方法来提高同理心能力。 这可能包括积极倾听、换位思考、识别非语言线索和练习正念。
*   **常见障碍：** 它可能会讨论同理心的常见障碍，例如偏见、假设和情绪调节方面的挑战。

“Home、Subscribe、Contact、Writing Club”（主页、订阅、联系方式、写作俱乐部）的存在表明这是一个网站或博客。 因此，这篇文章很可能是更大内容集合的一部分，并且鼓励读者订阅以获取更多信息，并可能通过写作俱乐部与社区互动。

**重要提示：** 这是一个基于标题和有限信息的假设性摘要。 文章的实际内容可能会有所不同。

---

## 50. 员工 регулярно paste company secrets into ChatGPT

**原文标题**: Employees regularly paste company secrets into ChatGPT

**原文链接**: [https://www.theregister.com/2025/10/07/gen_ai_shadow_it_secrets/](https://www.theregister.com/2025/10/07/gen_ai_shadow_it_secrets/)

LayerX研究显示员工频繁将敏感公司数据（包括PII和PCI信息）粘贴到ChatGPT，构成严重的数据泄露和合规风险。报告指出，45%的企业员工使用生成式AI工具，其中77%的用户复制粘贴数据到聊天机器人查询中。令人担忧的是，这些粘贴内容中有22%包含敏感信息。

使用个人账户进行AI互动（82%的粘贴）这种不受控制的行为加剧了问题，企业对数据共享的可见性很低。上传到AI网站的文件中也有40%包含PII/PCI数据，其中39%来自非公司账户。

LayerX首席执行官Or Eshed强调了AI数据泄露可能引发地缘政治、监管和培训滥用等问题。报告还发现，ChatGPT在企业AI使用中占据主导地位，远超Google Gemini、Claude和Microsoft Copilot。尽管微软已采取措施在企业环境中支持个人Copilot账户，但ChatGPT仍然是首选的AI平台。

报告强调，首席信息安全官（CISO）需要强制在关键业务应用程序中实施单点登录（SSO），以了解数据流的可见性，尤其是在企业中AI使用迅速增长的情况下，AI使用已占所有应用程序使用的11%。

---

## 51. 快照博士

**原文标题**: A PhD in Snapshots

**原文链接**: [https://rbharath.github.io/A-PhD-In-Snapshots/](https://rbharath.github.io/A-PhD-In-Snapshots/)

本文回顾了一名博士生在计算生物学项目中运用机器学习进行药物发现和蛋白质分析的历程。文章以提交给赫兹基金会的一系列进展报告为框架，该基金会资助了该生的研究。

该生最初探索了各种机器学习领域，最终决定将这些技术应用于计算生物学，特别是 Pande 团队下的蛋白质模拟。早期工作涉及使用隐马尔可夫模型和切换线性动力系统来分析蛋白质动力学。

博士研究的很大一部分集中在使用深度学习进行虚拟药物筛选，包括在谷歌加速科学团队的实习。这促成了用于评估类药化合物的深度学习系统的创建，以及一个名为 MoleculeNet 的大规模数据集，旨在促进该领域的发展。虽然这项工作在生物化学界引起了关注和合作，但在机器学习界获得认可方面面临挑战。

该生还开发了 DeepChem，这是一个用于将机器学习应用于药物发现的开源软件包，并与辉瑞和默克等制药公司合作，以展示其效用。报告强调了研究的迭代性质，包括论文被拒、根据反馈进行调整以及根据合作和项目时间表调整优先级。这段历程展示了理论探索和实际应用之间的平衡，以及跨学科研究的挑战。

---

## 52. 使用 Git 和 pnpm 进行并行磁盘 I/O 的压力测试

**原文标题**: Stress test for parallel disk i/o using git and pnpm

**原文链接**: [https://github.com/NullVoxPopuli/disk-perf-git-and-pnpm](https://github.com/NullVoxPopuli/disk-perf-git-and-pnpm)

本文档描述了一个使用 Git 和 pnpm 进行并行磁盘 I/O 的压力测试，旨在潜在地突出 macOS 上 APFS 文件系统的性能问题。该测试包括克隆一个 Git 仓库，使用 pnpm 安装依赖项，并测量 `git clean` 和 `pnpm install` 所用的时间。

该过程包括：

1. **设置：** 确保已安装特定版本的 Node.js 和 pnpm。
2. **收集结果：** 运行 `git clean -Xfd; git clean -fd` 和 `pnpm install`，并使用 `time`（Linux/macOS）或 `Measure-Command`（Windows Powershell）记录执行时间。
3. **报告结果：** 提交包含测试结果的 pull request，包括日期、CPU、RAM、“Clean” 时间（git clean）、“Install” 时间（pnpm install）、操作系统、文件系统类型、磁盘信息，以及任何值得注意的软件更改（如安全工具）。

文档包含一个来自不同系统的结果表格，这些系统具有不同的硬件、操作系统（macOS、Ubuntu、Windows）和文件系统（APFS、Ext4、NTFS、tmpfs），展示了性能差异。目标是建立一个比较数据集，并可能识别与 APFS 性能问题相关的模式。

最后，对于遇到文件系统性能不佳的 macOS 用户，文档建议使用 RAM 磁盘、通过 Docker 使用 OverlayFS 或使用带有 Ext4 的 Linux VM 作为潜在的解决方法。

---

## 53. 微中心与iFixit合作，让科技维修更普及

**原文标题**: Micro Center and iFixit Team Up to Make Tech Repair More Accessible

**原文链接**: [https://www.microcenter.com/site/mc-news/article/micro-center-and-ifixit-team-up-for-repair.aspx](https://www.microcenter.com/site/mc-news/article/micro-center-and-ifixit-team-up-for-repair.aspx)

Micro Center 与 iFixit 合作，提高技术维修的可及性。此次合作旨在为客户提供维修电子产品所需的工具、零件和知识，从而减少电子垃圾并节省资金。

合作的主要方面包括：

*   **提高零件可用性：** Micro Center 商店将提供更多种类的 iFixit 零件和工具，使客户更容易在当地找到所需物品。
*   **教育资源：** iFixit 的维修指南将方便 Micro Center 客户在线以及可能在店内获取，提供维修各种设备的逐步说明。
*   **赋能 DIY 维修：** 此次合作强调赋能消费者维修自己的设备而不是更换它们，从而促进一种更可持续的技术消费方式。
*   **应对维修权问题：** 通过提供易于获取的工具和信息，Micro Center 和 iFixit 正在隐性地支持“维修权”运动，该运动倡导消费者维修自己设备的权利。

本质上，此次合作将 Micro Center 的零售业务和客户群与 iFixit 在维修资源和零件分销方面的专业知识相结合，为技术维修爱好者和普通消费者创造一个更易于访问和赋能的环境。

---

## 54. 数据中心投资热潮中浑浊的经济学

**原文标题**: The murky economics of the data-centre investment boom

**原文链接**: [https://www.economist.com/business/2025/09/30/the-murky-economics-of-the-data-centre-investment-boom](https://www.economist.com/business/2025/09/30/the-murky-economics-of-the-data-centre-investment-boom)

无法访问文章链接。

---

## 55. 冰山原生数据库的理由

**原文标题**: The case for an iceberg-native database

**原文链接**: [https://www.warpstream.com/blog/the-case-for-an-iceberg-native-database-why-spark-jobs-and-zero-copy-kafka-wont-cut-it](https://www.warpstream.com/blog/the-case-for-an-iceberg-native-database-why-spark-jobs-and-zero-copy-kafka-wont-cut-it)

Richard Artoul 认为，不应使用 Spark 作业或“零拷贝”Kafka 实现，从 Kafka 中的实时数据构建和维护 Iceberg 表。他认为这些方法过于复杂、效率低下，并且最终令人不满意。

Spark 批处理作业需要大量的代码，并导致表更新的延迟很高。Spark Streaming 引入了“小文件问题”，需要进行压缩作业，进而导致“单写者问题”，从而产生冲突和性能问题。这导致复杂的、资源密集型的解决方案，难以管理。

文章随后批判了 Kafka 本身通过分层存储构建 Iceberg 表的想法。虽然看似方便（“零拷贝”），但由于 CPU 密集型的 Parquet 文件生成，会在 Kafka brokers 上造成性能瓶颈，并在 Kafka 和 Iceberg 分区策略之间引入阻抗失配。最终，试图在 Kafka 中结合操作型和分析型工作负载会损害两者。使用这种方法，压缩仍然是必需的，但在 Kafka 基础设施中变得更加麻烦。

Artoul 提倡使用专用的“Iceberg 原生”数据库来处理构建和维护 Iceberg 表的复杂性。文章暗示 WarpStream 的 Tableflow 是一种解决方案，可以高效且廉价地将 Kafka 主题数据转换为 Iceberg 表，并以低延迟保持压缩状态。

---

## 56. Erlang ARM32 JIT 诞生

**原文标题**: Erlang ARM32 JIT is born

**原文链接**: [https://www.grisp.org/blog/posts/2025-10-07-jit-arm32.3](https://www.grisp.org/blog/posts/2025-10-07-jit-arm32.3)

该博客宣布 BEAM JIT 编译器已成功移植到 ARM32 架构，这是在 Erlang 生态系统基金会的资助下实现的一个重要里程碑。作者回顾了这段历程，重点介绍了使用 JIT 编译的 ARM32 机器码成功执行了一个简单的 Erlang 函数 `hello:start/2`。

`hello:start/2` 函数旨在调用 `erlang:halt/2` BIF，退出代码为 42，它作为最初的测试用例。该文章详细介绍了所涉及的步骤，包括编译 Erlang 模块、生成 BEAM 汇编，以及利用 `qemu-arm` 进行仿真。

文章解释了 JIT 的初始化过程，包括共享代码片段和 `erts_beamasm` 模块的生成，这对管理进程执行至关重要。作者还提到，通过仅关注 `hello.erl` 模块来简化构建，以方便调试和验证。`-JDdump true` 用于生成 ARM32 汇编转储，强调其对调试至关重要。

文章随后检查了生成的汇编代码，指出了对“尚未实现”（NYI）函数的调用，并强调了 Erlang 函数序言的最小化实现。作者确定了退出代码 42 在汇编中的位置，揭示它作为标记值 (687) 存储在寄存器 r4 中，该寄存器指向 ErtsSchedulerRegisters 结构体。文章最后对未来 JIT 中 Erlang 指令的增量添加表示乐观。

---

## 57. 从轨道移除这50个物体可将太空垃圾的危险降低一半。

**原文标题**: Removing these 50 objects from orbit would cut danger from space junk in half

**原文链接**: [https://arstechnica.com/space/2025/10/everyone-but-china-has-pretty-much-stopped-littering-in-low-earth-orbit/](https://arstechnica.com/space/2025/10/everyone-but-china-has-pretty-much-stopped-littering-in-low-earth-orbit/)

本文探讨了近地轨道（LEO）空间碎片日益严重的问题，重点分析了一项新的研究，该研究识别出了50个最令人担忧的物体，主要是旧火箭残骸。移除这些物体可以显著降低碰撞风险，从而减少引发连锁反应产生新碎片的风险，即凯斯勒综合征。

这项由达伦·麦克奈特领导的研究表明，大部分问题碎片是在2000年之前遗留的，俄罗斯和中国是最大的贡献者。移除前10个物体将减少30%的碎片产生潜力，而移除所有50个物体将使风险降低一半。

一个令人担忧的趋势是，2024年后遗留在近地轨道的火箭残骸数量不断增加，特别是中国在部署其国网和千帆巨型星座期间。这些行为违反了国际准则，该准则要求物体在25年内脱离轨道。尽管中国拥有将火箭脱离轨道的技术，但并未始终如一地应用，而是优先考虑快速星座部署。

虽然主动碎片清除在技术上是可行的，但缺乏可行的市场以及关于谁来支付的问题阻碍了进展。尽管面临这些挑战，该研究表明，即使移除少量最危险的物体也会产生可衡量的积极影响。

---

## 58. 如果你每年购买超过两款新游戏，你就属于少数群体。

**原文标题**: If you buy more than two new games a year, you're in the minority

**原文链接**: [https://www.eurogamer.net/if-you-buy-more-than-two-new-games-a-year-youre-in-the-minority-new-report-reveals](https://www.eurogamer.net/if-you-buy-more-than-two-new-games-a-year-youre-in-the-minority-new-report-reveals)

Eurogamer文章指出，Circana 2025年第三季度游戏未来调查数据显示，美国绝大多数（63%）游戏玩家每年仅购买两款或更少的新游戏。这表明，在非免费游戏中，频繁购买游戏且对价格不太敏感的“超级爱好者”玩家正在不成比例地推动收入增长。

文章质疑了Xbox Game Pass等订阅服务对于在单个游戏购买上花费较少的普通消费者的价值主张。文章还提出了对小型游戏工作室在少数几款大作和免费运营游戏主导的市场中生存的担忧。文章认为，针对并吸引普通玩家，而不是仅仅依赖“超级爱好者”群体，对于未来行业增长至关重要。

文章随后探讨了微软和亚马逊等公司如何分别通过“一切皆为Xbox”和云游戏服务（Amazon Luna）等举措，试图降低普通消费者的准入门槛。最后，文章暗示了这些趋势可能对主机游戏未来产生的影响。

---

## 59. 具有动态扇出的缓存友好型B+树节点

**原文标题**: Cache-Friendly B+Tree Nodes with Dynamic Fanout

**原文链接**: [https://jacobsherin.com/posts/2025-08-18-bplustree-struct-hack/](https://jacobsherin.com/posts/2025-08-18-bplustree-struct-hack/)

本文详细介绍了一种在 C++ 中创建具有动态扇出的缓存友好型 B+ 树节点的技术，重点在于实现连续的内存布局以获得最佳性能。 其挑战在于需要用于节点条目的可变长度数组（在运行时确定），同时避免 `std::vector` 引入的间接寻址。

解决方案是 “结构体技巧” 或 “柔性数组” 技术，已在 C99/C++11 中标准化。 这涉及将动态大小的数组声明为结构的最后一个成员，分配单个连续的内存块以保存结构的头部和数组元素。 使用 placement new 在预先分配的缓冲区中构造对象。

然而，这种方法引入了显著的复杂性。 内存管理变为手动，需要仔细分配和释放以防止泄漏。 继承受到限制，因为派生类成员可能会覆盖数据缓冲区而导致数据损坏。 此外，它需要重新实现类似于 `std::vector` 的功能，并强加隐藏的数据类型假设，因为 `std::memmove` 需要可平凡复制的类型，以避免在使用 `std::string` 时出现双重释放等问题。

总而言之，虽然柔性数组为具有动态扇出的高性能 B+ 树提供了必要的连续内存布局，但它们也带来了更高的实现复杂性、手动内存管理以及对继承和数据类型的限制。 对于性能至关重要的应用程序来说，这种权衡是值得的。

---

## 60. 兵升变为车或象的情况在实战中常见吗？ (2012)

**原文标题**: Is pawn promotion to rook or bishop something that is seen in play? (2012)

**原文链接**: [https://boardgames.stackexchange.com/questions/6739/is-pawn-promotion-to-rook-or-bishop-something-that-is-seen-in-play](https://boardgames.stackexchange.com/questions/6739/is-pawn-promotion-to-rook-or-bishop-something-that-is-seen-in-play)

这个StackExchange帖子讨论了在国际象棋中兵升变车或象（低级升变）是否在战略上有利。发帖人最初了解避免逼和的场景，并想知道其他情况和真实对局的例子。

几个回答强调了相对于兵升变马而言，兵升变车或象的情况相对罕见。 其主要原因是：

1.  **避免逼和：** 升变为后会导致逼和，而升变为车或象则允许游戏继续。 提供了来自Ruben - Sultan Khan (1930)和Vasiukov - Tukmakov (1976)的真实对局示例。
2.  **“自大”走法：** 当升变格已经将死，或者兵将被吃掉时。
3.  **时间压力：** 在闪电战游戏中，玩家可能会选择车，以便进行更简单的车王将死，从而避免因时间限制而意外逼和。
4.  **使残局更有趣：** 升变为车/象/马可以使其更具挑战性。

几个用户链接到Tim Krabbé的网站，该网站详细介绍了40多个在严肃对局中发生兵升变车或象的实例。

---

## 61. 判断你的 USB-C 数据线是否损坏的 macOS 终端命令

**原文标题**: A macOS terminal command that tells you if your USB-C cable is bad

**原文链接**: [https://kau.sh/blog/usbi/](https://kau.sh/blog/usbi/)

本文探讨了“usbi”的创建，这是一个旨在识别macOS上速度慢或有问题的USB-C电缆的命令行脚本。作者受到了Android Studio警告用户有关USB连接速度缓慢的功能的启发，并希望为终端创建一个类似的工具。

该脚本的工作原理是解析macOS的`system_profiler SPUSBHostDataType`命令的输出（macOS Tahoe更新为`SPUSBHostDataType`），该命令提供有关连接的USB设备的信息。原始输出密集且难以解释，因此该脚本对其进行清理和格式化，以便于阅读。然后，该脚本显示有关连接设备的相关信息，例如其名称、供应商、速度和链路速度。

作者最初在AI的帮助下创建了一个bash脚本，但发现难以维护。然后，他使用AI（Claude）用Go重写了该脚本，他发现这更容易管理，并且具有跨平台编译的优势。作者强调，主要的收获是AI如何降低了创建有用实用脚本的门槛，使得像这样的小项目在时间投入方面“几乎是免费的”。他提到了对脚本的“vibe-coding”，表明了一种轻松且迭代的开发过程。

---

## 62. 参议院确认“马克笔门”气象学家领导美国国家海洋和大气管理局

**原文标题**: Senate Confirms 'Sharpiegate' Meteorologist to Lead NOAA

**原文链接**: [https://www.nytimes.com/2025/10/07/us/politics/senate-neil-jacobs-noaa.html](https://www.nytimes.com/2025/10/07/us/politics/senate-neil-jacobs-noaa.html)

无法访问文章链接。

---

## 63. 大脑通过在现实和心理地图之间“飞 dart”来探索新空间。

**原文标题**: The Brain Navigates New Spaces by 'Darting' Between Reality and Mental Maps

**原文链接**: [https://medicine.yale.edu/news-article/brain-navigates-new-spaces-by-flickering-between-reality-and-old-mental-maps/](https://medicine.yale.edu/news-article/brain-navigates-new-spaces-by-flickering-between-reality-and-old-mental-maps/)

耶鲁大学研究人员发现，大脑的“GPS”——海马体，如何修改认知地图来导航新的空间。该研究使用在迷宫中导航的老鼠，揭示大脑甚至在遇到不熟悉的路线之前就会“预演”它们。在老鼠遇到绕行路线之前，它们的大脑在睡眠期间会以暗示想象的替代路线的模式放电，这与实际绕行期间的神经活动相关。

在绕行导航期间，老鼠的大脑会在其当前位置和原始路径的记忆之间“闪烁”，这由θ脑波促进。 绕行被移除后，大脑不会简单地恢复到旧地图；相反，它创建了一个包含绕行经历的更新后的表征。

第一作者周宇辰指出，这种“预先连接”使老鼠能够快速学习绕行路线。资深作者乔治·德拉戈伊认为，这种“闪烁”机制能够快速比较当前和记忆中的经历，具有更广泛的意义。 这种机制的紊乱可能导致诸如创伤后应激障碍（PTSD）之类的疾病，在这些疾病中，过去和现在的记忆会混淆，从而干扰现实。 这项研究突显了大脑如何灵活地调整其内部地图，以应对环境中意外的变化。

---

## 64. Tcl语言展示

**原文标题**: Tcl-Lang Showcase

**原文链接**: [https://wiki.tcl-lang.org/page/Showcase](https://wiki.tcl-lang.org/page/Showcase)

这是使用 Tcl 脚本语言（特别是 Tk 工具包用于图形用户界面）开发的应用程序和工具展示。内容重点介绍各种项目，展示了 Tcl 在不同领域的通用性。

重点展示的关键项目包括图形应用程序，例如：

*   **SpiroGraph：** 一个用于创建螺线图案的程序。
*   **3D polyhedra with simple tk canvas：** 使用 Tk 画布组件的可视化 3D 形状。
*   **trains3.tcl：** 可能是火车模拟应用程序。
*   **TriPeaks Solitaire：** 电脑纸牌游戏。
*   **HP-15 Simulation：** HP-15 计算器的模拟器。
*   **1010! and Triangle Madness：** 益智游戏。

该展示还包括工具和软件包，例如：

*   **tkEngine：** 可能是用于开发基于 Tk 的应用程序的框架或库。
*   **Pave：** 一个用于在 Tk 界面中排列小部件的几何管理器。
*   **Zen Loops：** 可能是处理 Tcl 程序中循环的系统或方法。
*   **TkPool：** 专门为 Tk 设计的资源池机制。
*   **Canvas3d：** 基于 Tk 画布组件的 3D 图形工具或库。
*   **hyperhelp-package：** 用于创建和管理帮助系统的软件包。
*   **GRIDPLUS2：** 功能不明确，但可能是一个基于命名惯例的图形工具。

本质上，这是一个精选的 Tcl/Tk 项目列表，用于例证该语言和工具包的功能。Wiki 页面链接表明可以获得关于每个项目的更深入信息。

---

## 65. 让你的邮件永远不会被封禁

**原文标题**: Become unbannable from your email

**原文链接**: [https://karboosx.net/post/PJOveGVa/become-unbannable-from-your-emailgmail](https://karboosx.net/post/PJOveGVa/become-unbannable-from-your-emailgmail)

无法访问文章链接。

---

## 66. Who needs Git when you have 1M context windows?

**原文标题**: Who needs Git when you have 1M context windows?

**原文链接**: [https://www.alexmolas.com/2025/07/28/unexpected-benefit-llm.html](https://www.alexmolas.com/2025/07/28/unexpected-benefit-llm.html)

The author, working on LTV predictions at RevenueCat, accidentally deleted the code that gave them a 5% improvement in their ML model after refactoring it into a production-ready package. They hadn't committed the original, successful code to Git, a common mistake. After struggling to reproduce the results, the author realized they had been using Gemini-2.5-pro, an LLM with a 1 million token context window, throughout the development process. On a whim, they asked the LLM to recall the original `ml_ltv_training.py` file they had previously passed to it. The LLM successfully retrieved the lost code, effectively saving the author from their mistake. The article humorously suggests that long-context LLMs can act as a backup system, potentially mitigating the need for strict version control practices like Git, although the piece is likely meant as a commentary about the increasing utility of powerful LLMs in software development.


---

## 67. 为资助美国公共广播，鲍勃·罗斯画作将被拍卖。

**原文标题**: Bob Ross paintings to be auctioned to fund US public broadcasting

**原文链接**: [https://www.bbc.com/news/articles/cly10275v5zo](https://www.bbc.com/news/articles/cly10275v5zo)

深受喜爱的艺术导师鲍勃·罗斯的画作将于11月由邦瀚斯拍卖，以支持面临资金削减的美国公共广播。鲍勃·罗斯公司向美国公共电视台捐赠了约30幅画作，其中许多创作于他在80年代和90年代的电视节目《绘画的乐趣》中。所有净收益将捐给国会批准预算削减后陷入困境的当地PBS和NPR电视台。

此次拍卖旨在延续罗斯通过公共电视将欢乐和创造力带入美国家庭的遗愿。这些资金将有助于支持像《美国厨房测试》、《茱莉亚·蔡尔德的法国厨师经典》和《老房改造》等节目。

此前，罗斯的两幅画作《雪山下的湖泊》和《雪山下的湖泊》在8月份的拍卖会上分别以114,800美元和95,750美元的价格售出，远超预期。鲍勃·罗斯公司总裁琼·科瓦尔斯基认为，罗斯会对这些画作的高价值感到惊讶，因为他更热衷于绘画的过程和激励他人创作自己的艺术。《绘画的乐趣》在新冠疫情期间经历了复兴，证明了罗斯经久不衰的魅力。

---

## 68. 交互式双摆游乐场

**原文标题**: Interactive Double Pendulum Playground

**原文链接**: [https://theabbie.github.io/DoublePendulum/](https://theabbie.github.io/DoublePendulum/)

This document presents an interactive simulation environment for a double pendulum. The title, "Interactive Double Pendulum Playground," clearly indicates its purpose: allowing users to explore the behavior of a double pendulum.

The interface includes visual representations and adjustable parameters that encourage experimentation. Key interactive elements include:

*   **Double Pendulum visualization:** The primary focus, likely displaying a graphical representation of the double pendulum in motion.

*   **Controls:** Allow users to reset the simulation, visualize the pendulum's trace (path), display a graph (likely of energy or angular position), persist the trace over multiple runs, smooth the trace visually, and adjust the gravity level.

*   **Parameter Adjustments:** Provides controls to modify the upper mass, lower mass, and overall simulation speed.

*   **Visibility toggles:** Options to show or hide features like the trace, graph, pendulum itself, and influence of gravity.

*   **Navigation:** Includes a home button (⌂), a link to the project's GitHub repository, and a share option.

The interface suggests a focus on exploration and visualization, allowing users to observe the chaotic motion of a double pendulum and understand how different parameters influence its behavior. The presence of features like trace persistence and smoothing indicates a goal of making the patterns more easily observable. Essentially, it's a sandbox for experimenting with the double pendulum system.


---

## 69. TiVo exiting legacy DVR business

**原文标题**: TiVo exiting legacy DVR business

**原文链接**: [https://www.mediaplaynews.com/tivo-exiting-legacy-dvr-business/](https://www.mediaplaynews.com/tivo-exiting-legacy-dvr-business/)

生成摘要时出错

---

## 70. Chess.com regional pricing: A case study

**原文标题**: Chess.com regional pricing: A case study

**原文链接**: [https://mobeigi.com/blog/economics/chesscom-regional-pricing/](https://mobeigi.com/blog/economics/chesscom-regional-pricing/)

生成摘要时出错

---

## 71. Doing Rails Wrong

**原文标题**: Doing Rails Wrong

**原文链接**: [https://www.bananacurvingmachine.com/articles/you-re-doing-rails-wrong](https://www.bananacurvingmachine.com/articles/you-re-doing-rails-wrong)

生成摘要时出错

---

## 72. User ban controversy reveals Bluesky’s decentralized aspiration isn’t reality

**原文标题**: User ban controversy reveals Bluesky’s decentralized aspiration isn’t reality

**原文链接**: [https://plus.flux.community/p/banning-controversy-reveals-blueskys](https://plus.flux.community/p/banning-controversy-reveals-blueskys)

This article examines the gap between Bluesky's decentralized aspirations and its current reality, highlighted by a user ban controversy. Bluesky, pitched as an open and user-friendly alternative to Twitter after Elon Musk's takeover, gained popularity due to its ease of use and flexible, user-driven content moderation. However, the platform has faced criticism regarding moderation decisions, particularly concerning anti-trans content and alleged tolerance of racist content.

Bluesky's ambitious goal is a federated Authenticated Transfer Protocol (ATProto) network, enabling independent instances. However, due to the complexity of Bluesky's software stack, true federation has not been achieved. Blacksky, an alternative service created in response to complaints about Bluesky's moderation, remains partially dependent on Bluesky's application server and moderation system.

The article focuses on a specific incident where a Blacksky user, Link, was banned by Bluesky, rendering his posts invisible even on Blacksky. This revealed the extent of Blacksky's reliance on Bluesky's infrastructure. The ban occurred after Link posted a reaction meme to a post from Bluesky CEO Jay Graber.

The situation highlights the limitations of Bluesky's current decentralization efforts. While developers are working on tools to simplify the creation of custom AppViews, alternatives like Blacksky are still dependent on the main platform. The incident has led some users to reconsider Mastodon, while others are awaiting further progress in ATProto development. Overall, the article suggests that Bluesky's vision of a truly decentralized social network is still far from being realized.


---

## 73. CachyOS Keeps Spreading and Takes Second Place Among Linux Distros

**原文标题**: CachyOS Keeps Spreading and Takes Second Place Among Linux Distros

**原文链接**: [https://boilingsteam.com/cachy-os-keeps-spreading-and-takes-second-place-among-linux-distros/](https://boilingsteam.com/cachy-os-keeps-spreading-and-takes-second-place-among-linux-distros/)

生成摘要时出错

---

## 74. Bat: Cat with syntax highlighting

**原文标题**: Bat: Cat with syntax highlighting

**原文链接**: [https://github.com/sharkdp/bat](https://github.com/sharkdp/bat)

生成摘要时出错

---

## 75. A mechanic offered a reason why no one wants to work in the industry

**原文标题**: A mechanic offered a reason why no one wants to work in the industry

**原文链接**: [https://www.motor1.com/news/774805/ford-ceo-complains-shortage-mechanics/](https://www.motor1.com/news/774805/ford-ceo-complains-shortage-mechanics/)

生成摘要时出错

---

## 76. What makes 5% of AI agents work in production?

**原文标题**: What makes 5% of AI agents work in production?

**原文链接**: [https://www.motivenotes.ai/p/what-makes-5-of-ai-agents-actually](https://www.motivenotes.ai/p/what-makes-5-of-ai-agents-actually)

生成摘要时出错

---

## 77. The least amount of CSS for a decent looking site (2023)

**原文标题**: The least amount of CSS for a decent looking site (2023)

**原文链接**: [https://thecascade.dev/article/least-amount-of-css/](https://thecascade.dev/article/least-amount-of-css/)

生成摘要时出错

---

## 78. Show HN: DidMySettingsChange – A tool that checks changed windows settings

**原文标题**: Show HN: DidMySettingsChange – A tool that checks changed windows settings

**原文链接**: [https://github.com/nolesapex/DidMySettingsChange](https://github.com/nolesapex/DidMySettingsChange)

生成摘要时出错

---

## 79. Let's Encrypt – Ten Years of Community Support

**原文标题**: Let's Encrypt – Ten Years of Community Support

**原文链接**: [https://letsencrypt.org/2025/10/07/ten-yrs-community-forum](https://letsencrypt.org/2025/10/07/ten-yrs-community-forum)

生成摘要时出错

---

## 80. State of the Bird 2024/25

**原文标题**: State of the Bird 2024/25

**原文链接**: [https://blog.thunderbird.net/2025/10/state-of-the-bird-2024-25/](https://blog.thunderbird.net/2025/10/state-of-the-bird-2024-25/)

生成摘要时出错

---

## 81. Fire destroys S. Korean government's cloud storage system, no backups available

**原文标题**: Fire destroys S. Korean government's cloud storage system, no backups available

**原文链接**: [https://koreajoongangdaily.joins.com/news/2025-10-01/national/socialAffairs/NIRS-fire-destroys-governments-cloud-storage-system-no-backups-available/2412936](https://koreajoongangdaily.joins.com/news/2025-10-01/national/socialAffairs/NIRS-fire-destroys-governments-cloud-storage-system-no-backups-available/2412936)

生成摘要时出错

---

## 82. ICE bought vehicles equipped with fake cell towers to spy on phones

**原文标题**: ICE bought vehicles equipped with fake cell towers to spy on phones

**原文链接**: [https://techcrunch.com/2025/10/07/ice-bought-vehicles-equipped-with-fake-cell-towers-to-spy-on-phones/](https://techcrunch.com/2025/10/07/ice-bought-vehicles-equipped-with-fake-cell-towers-to-spy-on-phones/)

生成摘要时出错

---

## 83. Wi-Fi Signals Can Be Used to Detect Your Heartbeat

**原文标题**: Wi-Fi Signals Can Be Used to Detect Your Heartbeat

**原文链接**: [https://spectrum.ieee.org/wi-fi-signal-heartbeat-detection](https://spectrum.ieee.org/wi-fi-signal-heartbeat-detection)

生成摘要时出错

---

## 84. RediShell: Critical remote code execution vulnerability in Redis

**原文标题**: RediShell: Critical remote code execution vulnerability in Redis

**原文链接**: [https://www.wiz.io/blog/wiz-research-redis-rce-cve-2025-49844](https://www.wiz.io/blog/wiz-research-redis-rce-cve-2025-49844)

生成摘要时出错

---

## 85. It's just a virus, the E.R. told him – days later, he was dead

**原文标题**: It's just a virus, the E.R. told him – days later, he was dead

**原文链接**: [https://www.nytimes.com/2025/10/05/well/sam-terblanche-virus-death-columbia.html](https://www.nytimes.com/2025/10/05/well/sam-terblanche-virus-death-columbia.html)

生成摘要时出错

---

## 86. High-fat diet impairs memory by autophagic-lysosomal dysfunction in Drosophila

**原文标题**: High-fat diet impairs memory by autophagic-lysosomal dysfunction in Drosophila

**原文链接**: [https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1011818](https://journals.plos.org/plosgenetics/article?id=10.1371/journal.pgen.1011818)

生成摘要时出错

---

## 87. Reconstruction of Konrad Zuse's Z3 Computer

**原文标题**: Reconstruction of Konrad Zuse's Z3 Computer

**原文链接**: [https://dcmlr.inf.fu-berlin.de/rojas/index.html%3Fp=560.html](https://dcmlr.inf.fu-berlin.de/rojas/index.html%3Fp=560.html)

生成摘要时出错

---

## 88. Git, JSON and Markdown walk into bar

**原文标题**: Git, JSON and Markdown walk into bar

**原文链接**: [https://www.grumpygamer.com/git_json_markdown/](https://www.grumpygamer.com/git_json_markdown/)

生成摘要时出错

---

## 89. Functional Threading "Macros"

**原文标题**: Functional Threading "Macros"

**原文链接**: [https://aartaka.me/threading.html](https://aartaka.me/threading.html)

生成摘要时出错

---

## 90. Who owns Express VPN, Nord, Surfshark? VPN relationships explained (2024)

**原文标题**: Who owns Express VPN, Nord, Surfshark? VPN relationships explained (2024)

**原文链接**: [https://windscribe.com/blog/the-vpn-relationship-map/](https://windscribe.com/blog/the-vpn-relationship-map/)

生成摘要时出错

---

## 91. Orcas are bringing humans gifts

**原文标题**: Orcas are bringing humans gifts

**原文链接**: [https://www.newscientist.com/article/2486216-orcas-are-bringing-humans-gifts-what-does-it-mean/](https://www.newscientist.com/article/2486216-orcas-are-bringing-humans-gifts-what-does-it-mean/)

生成摘要时出错

---

## 92. Using Deno as my game engine

**原文标题**: Using Deno as my game engine

**原文链接**: [https://explodi.tubatuba.net/2025/09/26/using-deno-as-my-game-engine](https://explodi.tubatuba.net/2025/09/26/using-deno-as-my-game-engine)

生成摘要时出错

---

## 93. The First 6100 Qubit Array at Room Temperature

**原文标题**: The First 6100 Qubit Array at Room Temperature

**原文链接**: [https://www.caltech.edu/about/news/caltech-team-sets-record-with-6100-qubit-array](https://www.caltech.edu/about/news/caltech-team-sets-record-with-6100-qubit-array)

生成摘要时出错

---

## 94. Show HN: Arc – high-throughput time-series warehouse with DuckDB analytics

**原文标题**: Show HN: Arc – high-throughput time-series warehouse with DuckDB analytics

**原文链接**: [https://github.com/Basekick-Labs/arc](https://github.com/Basekick-Labs/arc)

生成摘要时出错

---

## 95. A new bone substitute made out of 3D-printed glass

**原文标题**: A new bone substitute made out of 3D-printed glass

**原文链接**: [https://phys.org/news/2025-09-bone-substitute-3d-glass.html](https://phys.org/news/2025-09-bone-substitute-3d-glass.html)

生成摘要时出错

---

## 96. The Mondrian introduction to functional optics

**原文标题**: The Mondrian introduction to functional optics

**原文链接**: [http://marcosh.github.io/post/2025/10/07/the-mondrian-introduction-to-functional-optics.html](http://marcosh.github.io/post/2025/10/07/the-mondrian-introduction-to-functional-optics.html)

生成摘要时出错

---

## 97. Deloitte to refund the Australian government after using AI in $440k report

**原文标题**: Deloitte to refund the Australian government after using AI in $440k report

**原文链接**: [https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report](https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report)

生成摘要时出错

---

## 98. Pdoc – Generate API documentation for Python projects

**原文标题**: Pdoc – Generate API documentation for Python projects

**原文链接**: [https://pdoc.dev/](https://pdoc.dev/)

生成摘要时出错

---

## 99. Adding Stride Scheduling to Xv6

**原文标题**: Adding Stride Scheduling to Xv6

**原文链接**: [https://nickchandler.dev/articles/2025/10/03/lab-report-adding-stride-scheduling-to-xv6/](https://nickchandler.dev/articles/2025/10/03/lab-report-adding-stride-scheduling-to-xv6/)

生成摘要时出错

---

## 100. Ladybird passes the Apple 90% threshold on web-platform-tests

**原文标题**: Ladybird passes the Apple 90% threshold on web-platform-tests

**原文链接**: [https://twitter.com/awesomekling/status/1974781722953953601](https://twitter.com/awesomekling/status/1974781722953953601)

生成摘要时出错

---

