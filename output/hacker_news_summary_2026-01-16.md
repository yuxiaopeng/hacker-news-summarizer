# Hacker News 热门文章摘要 (2026-01-16)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Cloudflare 收购 Astro

**原文标题**: Cloudflare acquires Astro

**原文链接**: [https://astro.build/blog/joining-cloudflare/](https://astro.build/blog/joining-cloudflare/)

Cloudflare 已收购热门 Web 框架 Astro 的开发团队 The Astro Technology Company。此举旨在为 Astro 团队提供所需的稳定性与资源，使其能够全身心地投入到框架开发中；此前，该团队在围绕 Astro DB 等托管原语建立可持续商业模式方面曾面临挑战。

尽管发生了收购，但 Astro 的几个关键方面将保持不变：
*   **开源：** Astro 将继续在 MIT 协议下保持开源。
*   **治理：** 现有的开放治理模式和社区路线图将维持不变。
*   **平台无关性：** Astro 将继续支持所有部署目标和托管服务商，而不仅仅是 Cloudflare。
*   **专属团队：** 所有 Astro 全职员工都将加入 Cloudflare，继续全职从事该框架的开发工作。

Astro 成立于 2021 年，旨在优先发展“内容驱动型”网站，而非复杂的重状态应用。自此以后，它经历了飞速增长，每周下载量已接近 100 万次，并被谷歌、微软和 Webflow 等知名公司采用。

通过加入 Cloudflare——该框架的长期赞助者和倡导者——Astro 团队旨在消除商业变现带来的“干扰”。这使他们能够 100% 地专注于构建更快速、性能更卓越的 Web 这一使命。展望未来，团队正优先发布 Astro 6（目前处于 Beta 阶段），并执行其直至 2026 年的长期路线图。

---

## 2. 6天期及IP地址证书现已正式发布

**原文标题**: 6-Day and IP Address Certificates Are Generally Available

**原文链接**: [https://letsencrypt.org/2026/01/15/6day-and-ip-general-availability](https://letsencrypt.org/2026/01/15/6day-and-ip-general-availability)

Let’s Encrypt 宣布正式推出**短期证书**和 **IP 地址证书**。

**短期证书**
这些证书的有效期为 160 小时（约 6 天），用户可以通过 ACME 客户端中的“shortlived”配置文件选择使用。其主要目标是增强安全性；通过大幅缩短有效期，Let's Encrypt 降低了私钥泄露相关的风险，并绕过了传统且通常不可靠的撤销机制的局限性。虽然这些证书目前是可选的，但 Let's Encrypt 计划在未来几年内将其标准的 90 天证书有效期缩短至 45 天。

**IP 地址证书**
该服务现在支持 IPv4 和 IPv6 地址证书，允许运营商直接针对 IP 地址而非域名进行 TLS 连接验证。由于 IP 地址比域名更具临时性，Let’s Encrypt 要求所有 IP 证书必须采用短期（6 天）格式，以确保频繁的重新验证。

**实施与支持**
这些功能旨在面向已实现完全自动化续期流程的用户。这些工具的开发得到了开放技术基金会（Open Technology Fund）、Sovereign Tech Agency 以及各企业赞助商和捐助者的支持。这一转变反映了行业正努力推动自动化、高频率验证，以提升互联网的整体安全性。

---

## 3. 米开朗基罗在12或13岁时创作的第一幅画。

**原文标题**: Michelangelo's first painting, created when he was 12 or 13

**原文链接**: [https://www.openculture.com/2026/01/discover-michelangelos-first-painting.html](https://www.openculture.com/2026/01/discover-michelangelos-first-painting.html)

本文探讨了**《圣安东尼的诱惑》**（*The Torment of Saint Anthony*）的历史与鉴定过程。这是米开朗基罗已知的第一幅画作，创作于他仅12或13岁时。

尽管该作品基于一幅著名的版画，但在近500年的时间里，它一直未被归为这位文艺复兴大师之手。直到2008年，该画作在苏富比拍卖行售出并被送往大都会艺术博物馆进行修复，其真实身世才开始浮出水面。修复清洗揭示了其色调和解剖学风格，与米开朗基罗后来在西斯廷礼拜堂的作品惊人地相似。此外，红外反射成像技术发现了“修改痕迹”（*pentimenti*），证明这件作品是原创构思，而非单纯的临摹。

这幅画最终由德克萨斯州沃斯堡的**坎贝尔艺术博物馆**（Kimbell Art Museum）购得。它是美洲境内唯一的米开朗基罗画作，也是现存仅有的四幅被归于其名下的架上画之一。尽管仍有部分人持怀疑态度，但在经过深入分析后，著名艺术史学家乔治·邦桑蒂（Giorgio Bonsanti）明确支持这一鉴定结论。这件作品见证了米开朗基罗早慧的天赋，展现了他在享誉国际之前便已具备的高超技艺与创造力。

---

## 4. 只需浏览器

**原文标题**: Just the Browser

**原文链接**: [https://justthebrowser.com/](https://justthebrowser.com/)

**Just the Browser** 是一个开源项目，旨在剥离主流浏览器（特别是 Google Chrome、Microsoft Edge 和 Mozilla Firefox）中的现代“臃肿软件”。其核心目标是通过禁用 AI 功能（如 Copilot）、遥测数据收集、赞助内容、购物集成以及侵入性的“默认浏览器”提示，提供纯净、无干扰的浏览体验。

**工作原理**
该项目不修改浏览器的可执行代码，而是利用官方的“组策略”设置——这些隐藏配置通常预留给 IT 部门和大型组织。由于使用的是这些原生企业级工具，相关更改非常稳定且受浏览器完全支持，不过用户会在设置中看到“由所属组织管理”的通知。

**移除的关键功能：**
*   **AI 与建议：** 生成式 AI 工具和自动标签组建议。
*   **商业臃肿功能：** 购物工具、价格追踪器和优惠券查找器。
*   **数据报告：** 大多数遥测和后台数据收集。
*   **干扰项：** 欢迎界面、启动增强功能以及持久的数据导入提示。

**安装与支持**
该项目通过 Windows 的 PowerShell 和 macOS/Linux 的终端提供自动安装脚本。此外也为希望自定义设置的用户提供手动配置指南。目前该项目支持各大主流桌面平台，尚未提供 Android 和 iOS 移动版本。

**设计理念**
开发者认为，相比转向可能在关键安全更新上滞后的小众浏览器，“Just the Browser”是一个更安全的选择。通过使用这些配置文件，用户可以在移除干扰 UI 的企业级功能的同时，保持主流浏览器引擎的性能和安全性。该项目不包含广告拦截功能，建议用户配合 uBlock Origin 等第三方扩展使用。

---

## 5. HN 产品发布：Indy (YC S21) —— 专为 ADHD 大脑设计的辅助应用

**原文标题**: Launch HN: Indy (YC S21) – A support app designed for ADHD brains

**原文链接**: [https://www.shimmer.care/indy-redirect](https://www.shimmer.care/indy-redirect)

**Indy (YC S21)** 是一款专为 ADHD（注意缺陷多动障碍）群体设计的专业辅助应用。作为 Y Combinator 2021 年夏季孵化项目的成员，该应用旨在解决 ADHD 群体所面临的独特认知需求和执行功能挑战。

发布要点包括：

*   **目标受众：** 该应用专为“ADHD 大脑”量身定制，侧重于那些仅靠传统效率工具无法满足需求的用户。
*   **产品宗旨：** 它作为一个支持系统，通过针对 ADHD 症状定制的框架，帮助用户管理日常任务、保持专注并进行条理化组织。
*   **平台背景：** 该发布源于 “Launch HN”，这是一个 Y Combinator 初创公司向技术社区推介产品、获取反馈并吸引用户的平台。

总之，Indy 代表了效率应用市场向垂直领域的转变，即从通用型工具转向针对神经多样性群体的专业化支持。

---

## 6. Zep AI (Agent Context Engineering, YC W24) 招聘前线部署工程师

**原文标题**: Zep AI (Agent Context Engineering, YC W24) Is Hiring Forward Deployed Engineers

**原文链接**: [https://www.ycombinator.com/companies/zep-ai/jobs/](https://www.ycombinator.com/companies/zep-ai/jobs/)

Zep AI 是一家专注于智能体上下文工程（Agent Context Engineering）的 Y Combinator (W24) 孵化初创公司，目前正在扩充其五人团队。该公司致力于通过高效整合聊天记录、业务数据和用户行为来提升 AI 智能体的性能，确保其能够提供个性化、快速且准确的服务。

**开放职位与薪酬**
Zep AI 目前正在招聘拥有 6 年以上经验的资深候选人，职位包括：
* **资深工程师 (Staff Engineer)**
* **首席现场部署工程师 (Lead Forward Deployed Engineer)**
* **开发者关系主管 (Developer Relations Lead)**

所有职位的年薪范围为 17.5 万至 25 万美元，并提供 0.50% 至 1.50% 的股权。办公地点位于旧金山，或支持美国境内远程办公。

**公司成就与文化**
Zep AI 成立于 2023 年，在开发者社区迅速积累了极高的人气。其开源项目 *Graphiti* 在不到一年的时间里便获得了 20,000 个 GitHub 星标。该平台专为大规模扩展和安全性而设计，检索延迟低于 200 毫秒，并已通过 SOC 2 Type 2 和 HIPAA 认证。其客户群涵盖了从初创公司到财富 500 强的各类企业。

现任员工高度认可公司充满自主权的文化、创始人 Daniel Chalef 提供的技术指导，以及参与开发具有重大意义的开源产品的机会。对于渴望影响一家高增长 AI 基础设施初创公司发展方向的资深工程师而言，Zep AI 提供了一个独特的工作环境。

---

## 7. 加拿大将中国电动汽车关税从100%下调至6%

**原文标题**: Canada slashes 100% tariffs on Chinese EVs to 6%

**原文链接**: [https://electrek.co/2026/01/16/canada-breaks-with-us-slashes-100-tariffs-chinese-evs/](https://electrek.co/2026/01/16/canada-breaks-with-us-slashes-100-tariffs-chinese-evs/)

生成摘要时出错

---

## 8. Lock-Picking Robot

**原文标题**: Lock-Picking Robot

**原文链接**: [https://github.com/etinaude/Lock-Picking-Robot](https://github.com/etinaude/Lock-Picking-Robot)

生成摘要时出错

---

## 9. Read_once(), Write_once(), but Not for Rust

**原文标题**: Read_once(), Write_once(), but Not for Rust

**原文链接**: [https://lwn.net/SubscriberLink/1053142/8ec93e58d5d3cc06/](https://lwn.net/SubscriberLink/1053142/8ec93e58d5d3cc06/)

生成摘要时出错

---

## 10. Can You Disable Spotlight and Siri in macOS Tahoe?

**原文标题**: Can You Disable Spotlight and Siri in macOS Tahoe?

**原文链接**: [https://eclecticlight.co/2026/01/16/can-you-disable-spotlight-and-siri-in-macos-tahoe/](https://eclecticlight.co/2026/01/16/can-you-disable-spotlight-and-siri-in-macos-tahoe/)

生成摘要时出错

---

## 11. psc: The ps utility, with an eBPF twist and container context

**原文标题**: psc: The ps utility, with an eBPF twist and container context

**原文链接**: [https://github.com/loresuso/psc](https://github.com/loresuso/psc)

生成摘要时出错

---

## 12. Training my smartwatch to track intelligence

**原文标题**: Training my smartwatch to track intelligence

**原文链接**: [https://dmvaldman.github.io/rooklift/](https://dmvaldman.github.io/rooklift/)

生成摘要时出错

---

## 13. OpenBSD-current now runs as guest under Apple Hypervisor

**原文标题**: OpenBSD-current now runs as guest under Apple Hypervisor

**原文链接**: [https://www.undeadly.org/cgi?action=article;sid=20260115203619](https://www.undeadly.org/cgi?action=article;sid=20260115203619)

生成摘要时出错

---

## 14. List of individual trees

**原文标题**: List of individual trees

**原文链接**: [https://en.wikipedia.org/wiki/List_of_individual_trees](https://en.wikipedia.org/wiki/List_of_individual_trees)

This article provides a comprehensive list of individual trees across Africa, Asia, and Europe that are recognized for their historical, national, natural, or mythological significance. Categorized into "Living" and "Historical" specimens, these trees serve as vital landmarks, religious icons, and scientific marvels.

**Africa** is home to several ancient Baobabs, such as the **Sunland Baobab**, which once housed a pub in its hollow, and the **Glencoe Baobab**, the continent's stoutest tree. Historical entries include the **Tree of Ténéré**, once the most isolated tree in the world, and the **Cotton Tree**, a symbol of Freetown, Sierra Leone, which fell in 2023.

**Asia** features some of the world's oldest and most religiously significant trees. Notable examples include the **Jaya Sri Maha Bodhi** in Sri Lanka, a sacred fig planted in 288 BC, and the **Cypress of Abarkuh** in Iran, estimated to be 4,500 years old. The region also boasts trees of immense size, such as India’s **Thimmamma Marrimanu**, a banyan covering over 11 acres, and **Menara**, the world's tallest tropical tree.

**Europe’s** listings emphasize ancient Yews and Oaks. Highlights include **Old Tjikko** in Sweden, the world’s oldest known individual clonal tree (9,567 years old), and the **Fortingall Yew** in Scotland. Many European trees are tied to legend and history, such as the **Birnam Oak** (linked to Shakespeare’s *Macbeth*) and the **Bicycle Tree**, which has a bike embedded in its trunk.

In summary, the list documents trees that have survived millennia, served as "post offices" or peace treaty sites, and continue to function as symbols of endurance and cultural heritage.

---

## 15. Interactive eBPF

**原文标题**: Interactive eBPF

**原文链接**: [https://ebpf.party/](https://ebpf.party/)

生成摘要时出错

---

## 16. Cursor's latest "browser experiment" implied success without evidence

**原文标题**: Cursor's latest "browser experiment" implied success without evidence

**原文链接**: [https://embedding-shapes.github.io/cursor-implied-success-without-evidence/](https://embedding-shapes.github.io/cursor-implied-success-without-evidence/)

生成摘要时出错

---

## 17. Why DuckDB is my first choice for data processing

**原文标题**: Why DuckDB is my first choice for data processing

**原文链接**: [https://www.robinlinacre.com/recommend_duckdb/](https://www.robinlinacre.com/recommend_duckdb/)

生成摘要时出错

---

## 18. Pocket TTS: A high quality TTS that gives your CPU a voice

**原文标题**: Pocket TTS: A high quality TTS that gives your CPU a voice

**原文链接**: [https://kyutai.org/blog/2026-01-13-pocket-tts](https://kyutai.org/blog/2026-01-13-pocket-tts)

生成摘要时出错

---

## 19. The spectrum of isolation: From bare metal to WebAssembly

**原文标题**: The spectrum of isolation: From bare metal to WebAssembly

**原文链接**: [https://buildsoftwaresystems.com/post/guide-to-execution-environments/](https://buildsoftwaresystems.com/post/guide-to-execution-environments/)

生成摘要时出错

---

## 20. Exasol Personal – Democratizing Big Data Analytics

**原文标题**: Exasol Personal – Democratizing Big Data Analytics

**原文链接**: [https://www.exasol.com/blog/introducing-exasol-personal/](https://www.exasol.com/blog/introducing-exasol-personal/)

生成摘要时出错

---

## 21. Show HN: mdto.page – Turn Markdown into a shareable webpage instantly

**原文标题**: Show HN: mdto.page – Turn Markdown into a shareable webpage instantly

**原文链接**: [https://mdto.page](https://mdto.page)

生成摘要时出错

---

## 22. ICE takes back into custody man released for violation of rights

**原文标题**: ICE takes back into custody man released for violation of rights

**原文链接**: [https://apnews.com/article/minnesota-immigration-crackdown-25e46910fcc62fbf5ab341905af9891c](https://apnews.com/article/minnesota-immigration-crackdown-25e46910fcc62fbf5ab341905af9891c)

生成摘要时出错

---

## 23. Briar keeps Iran connected via Bluetooth and Wi-Fi when the internet goes dark

**原文标题**: Briar keeps Iran connected via Bluetooth and Wi-Fi when the internet goes dark

**原文链接**: [https://briarproject.org/manual/fa/](https://briarproject.org/manual/fa/)

生成摘要时出错

---

## 24. Boeing knew of flaw in part linked to UPS plane crash, NTSB report says

**原文标题**: Boeing knew of flaw in part linked to UPS plane crash, NTSB report says

**原文链接**: [https://www.bbc.com/news/articles/cly56w0p9e1o](https://www.bbc.com/news/articles/cly56w0p9e1o)

生成摘要时出错

---

## 25. Inside The Internet Archive's Infrastructure

**原文标题**: Inside The Internet Archive's Infrastructure

**原文链接**: [https://hackernoon.com/the-long-now-of-the-web-inside-the-internet-archives-fight-against-forgetting](https://hackernoon.com/the-long-now-of-the-web-inside-the-internet-archives-fight-against-forgetting)

生成摘要时出错

---

## 26. Show HN: pgwire-replication - pure rust client for Postgres CDC

**原文标题**: Show HN: pgwire-replication - pure rust client for Postgres CDC

**原文链接**: [https://github.com/vnvo/pgwire-replication](https://github.com/vnvo/pgwire-replication)

生成摘要时出错

---

## 27. Linux boxes via SSH: suspended when disconected

**原文标题**: Linux boxes via SSH: suspended when disconected

**原文链接**: [https://shellbox.dev/](https://shellbox.dev/)

生成摘要时出错

---

## 28. Bringing the Predators to Life in MAME

**原文标题**: Bringing the Predators to Life in MAME

**原文链接**: [https://lysiwyg.mataroa.blog/blog/bringing-the-predators-to-life-in-mame/](https://lysiwyg.mataroa.blog/blog/bringing-the-predators-to-life-in-mame/)

生成摘要时出错

---

## 29. Altaid 8800 (2024)

**原文标题**: Altaid 8800 (2024)

**原文链接**: [https://sunrise-ev.com/8080.htm](https://sunrise-ev.com/8080.htm)

生成摘要时出错

---

## 30. Show HN: Hc: an agentless, multi-tenant shell history sink

**原文标题**: Show HN: Hc: an agentless, multi-tenant shell history sink

**原文链接**: [https://github.com/alessandrocarminati/hc](https://github.com/alessandrocarminati/hc)

生成摘要时出错

---

## 31. Claude is good at assembling blocks, but still falls apart at creating them

**原文标题**: Claude is good at assembling blocks, but still falls apart at creating them

**原文链接**: [https://www.approachwithalacrity.com/claude-ne/](https://www.approachwithalacrity.com/claude-ne/)

生成摘要时出错

---

## 32. pf: Make af-to less magical

**原文标题**: pf: Make af-to less magical

**原文链接**: [https://undeadly.org/cgi?action=article;sid=20260116085115](https://undeadly.org/cgi?action=article;sid=20260116085115)

生成摘要时出错

---

## 33. Starlink updates Privacy Policy to allow AI model training with personal data

**原文标题**: Starlink updates Privacy Policy to allow AI model training with personal data

**原文链接**: [https://coywolf.com/news/startups/starlink-updates-tos-to-allow-ai-model-training-with-personal-data/](https://coywolf.com/news/startups/starlink-updates-tos-to-allow-ai-model-training-with-personal-data/)

生成摘要时出错

---

## 34. Dev-Owned Testing: Why It Fails in Practice and Succeeds in Theory

**原文标题**: Dev-Owned Testing: Why It Fails in Practice and Succeeds in Theory

**原文链接**: [https://dl.acm.org/doi/10.1145/3780063.3780066](https://dl.acm.org/doi/10.1145/3780063.3780066)

生成摘要时出错

---

## 35. Data is the only moat

**原文标题**: Data is the only moat

**原文链接**: [https://frontierai.substack.com/p/data-is-your-only-moat](https://frontierai.substack.com/p/data-is-your-only-moat)

生成摘要时出错

---

## 36. Show HN: OpenWork – An open-source alternative to Claude Cowork

**原文标题**: Show HN: OpenWork – An open-source alternative to Claude Cowork

**原文链接**: [https://github.com/different-ai/openwork](https://github.com/different-ai/openwork)

生成摘要时出错

---

## 37. Apple is fighting for TSMC capacity as Nvidia takes center stage

**原文标题**: Apple is fighting for TSMC capacity as Nvidia takes center stage

**原文链接**: [https://www.culpium.com/p/exclusiveapple-is-fighting-for-tsmc](https://www.culpium.com/p/exclusiveapple-is-fighting-for-tsmc)

生成摘要时出错

---

## 38. Cyberattack in Venezuela Demonstrated Precision of U.S. Capabilities

**原文标题**: Cyberattack in Venezuela Demonstrated Precision of U.S. Capabilities

**原文链接**: [https://www.nytimes.com/2026/01/15/us/politics/cyberattack-venezuela-military.html](https://www.nytimes.com/2026/01/15/us/politics/cyberattack-venezuela-military.html)

生成摘要时出错

---

## 39. My Gripes with Prolog

**原文标题**: My Gripes with Prolog

**原文链接**: [https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/](https://buttondown.com/hillelwayne/archive/my-gripes-with-prolog/)

生成摘要时出错

---

## 40. Prime chains

**原文标题**: Prime chains

**原文链接**: [https://www.johndcook.com/blog/2026/01/10/prime-chains/](https://www.johndcook.com/blog/2026/01/10/prime-chains/)

生成摘要时出错

---

## 41. JuiceFS is a distributed POSIX file system built on top of Redis and S3

**原文标题**: JuiceFS is a distributed POSIX file system built on top of Redis and S3

**原文链接**: [https://github.com/juicedata/juicefs](https://github.com/juicedata/juicefs)

生成摘要时出错

---

## 42. First impressions of Claude Cowork

**原文标题**: First impressions of Claude Cowork

**原文链接**: [https://simonw.substack.com/p/first-impressions-of-claude-cowork](https://simonw.substack.com/p/first-impressions-of-claude-cowork)

生成摘要时出错

---

## 43. Show HN: I built a text-based business simulator to replace video courses

**原文标题**: Show HN: I built a text-based business simulator to replace video courses

**原文链接**: [https://www.core-mba.pro/](https://www.core-mba.pro/)

生成摘要时出错

---

## 44. Go-legacy-winxp: Compile Golang 1.24 code for Windows XP

**原文标题**: Go-legacy-winxp: Compile Golang 1.24 code for Windows XP

**原文链接**: [https://github.com/syncguy/go-legacy-winxp/tree/winxp-compat](https://github.com/syncguy/go-legacy-winxp/tree/winxp-compat)

生成摘要时出错

---

## 45. Why Greenland's natural resources are nearly impossible to mine

**原文标题**: Why Greenland's natural resources are nearly impossible to mine

**原文链接**: [https://theweek.com/world-news/greenland-natural-resources-impossible-mine](https://theweek.com/world-news/greenland-natural-resources-impossible-mine)

生成摘要时出错

---

## 46. CVEs affecting the Svelte ecosystem

**原文标题**: CVEs affecting the Svelte ecosystem

**原文链接**: [https://svelte.dev/blog/cves-affecting-the-svelte-ecosystem](https://svelte.dev/blog/cves-affecting-the-svelte-ecosystem)

生成摘要时出错

---

## 47. Supply Chain Vuln Compromised Core AWS GitHub Repos & Threatened the AWS Console

**原文标题**: Supply Chain Vuln Compromised Core AWS GitHub Repos & Threatened the AWS Console

**原文链接**: [https://www.wiz.io/blog/wiz-research-codebreach-vulnerability-aws-codebuild](https://www.wiz.io/blog/wiz-research-codebreach-vulnerability-aws-codebuild)

生成摘要时出错

---

## 48. I Built a 1 Petabyte Server from Scratch [video]

**原文标题**: I Built a 1 Petabyte Server from Scratch [video]

**原文链接**: [https://www.youtube.com/watch?v=vVI7atoAeoo](https://www.youtube.com/watch?v=vVI7atoAeoo)

生成摘要时出错

---

## 49. All 23-Bit Still Lifes Are Glider Constructible

**原文标题**: All 23-Bit Still Lifes Are Glider Constructible

**原文链接**: [https://mvr.github.io/posts/xs23.html](https://mvr.github.io/posts/xs23.html)

生成摘要时出错

---

## 50. Tldraw pauses external contributions due to AI slop

**原文标题**: Tldraw pauses external contributions due to AI slop

**原文链接**: [https://github.com/tldraw/tldraw/issues/7695](https://github.com/tldraw/tldraw/issues/7695)

生成摘要时出错

---

## 51. Found: Medieval Cargo Ship – Largest Vessel of Its Kind Ever

**原文标题**: Found: Medieval Cargo Ship – Largest Vessel of Its Kind Ever

**原文链接**: [https://www.smithsonianmag.com/smart-news/archaeologists-say-theyve-unearthed-a-massive-medieval-cargo-ship-thats-the-largest-vessel-of-its-kind-ever-found-180987984/](https://www.smithsonianmag.com/smart-news/archaeologists-say-theyve-unearthed-a-massive-medieval-cargo-ship-thats-the-largest-vessel-of-its-kind-ever-found-180987984/)

生成摘要时出错

---

## 52. Show HN: BGP Scout – BGP Network Browser

**原文标题**: Show HN: BGP Scout – BGP Network Browser

**原文链接**: [https://bgpscout.io/](https://bgpscout.io/)

生成摘要时出错

---

## 53. Elon Musk's X down for users

**原文标题**: Elon Musk's X down for users

**原文链接**: [https://www.bbc.com/news/live/cp8456m8mnkt](https://www.bbc.com/news/live/cp8456m8mnkt)

生成摘要时出错

---

## 54. What a Programmer Does (1967) [pdf]

**原文标题**: What a Programmer Does (1967) [pdf]

**原文链接**: [http://archive.computerhistory.org/resources/text/Knuth_Don_X4100/PDF_index/k-9-pdf/k-9-u2769-1-Baker-What-Programmer-Does.pdf](http://archive.computerhistory.org/resources/text/Knuth_Don_X4100/PDF_index/k-9-pdf/k-9-u2769-1-Baker-What-Programmer-Does.pdf)

生成摘要时出错

---

## 55. 25 Years of Wikipedia

**原文标题**: 25 Years of Wikipedia

**原文链接**: [https://wikipedia25.org](https://wikipedia25.org)

生成摘要时出错

---

## 56. Photos capture the breathtaking scale of China's wind and solar buildout

**原文标题**: Photos capture the breathtaking scale of China's wind and solar buildout

**原文链接**: [https://e360.yale.edu/digest/china-renewable-photo-essay](https://e360.yale.edu/digest/china-renewable-photo-essay)

生成摘要时出错

---

## 57. Show HN: Gambit, an open-source agent harness for building reliable AI agents

**原文标题**: Show HN: Gambit, an open-source agent harness for building reliable AI agents

**原文链接**: [https://github.com/bolt-foundry/gambit](https://github.com/bolt-foundry/gambit)

生成摘要时出错

---

## 58. Show HN: Reversing YouTube’s “Most Replayed” Graph

**原文标题**: Show HN: Reversing YouTube’s “Most Replayed” Graph

**原文链接**: [https://priyavr.at/blog/reversing-most-replayed/](https://priyavr.at/blog/reversing-most-replayed/)

生成摘要时出错

---

## 59. Cue Does It All, but Can It Literate?

**原文标题**: Cue Does It All, but Can It Literate?

**原文链接**: [https://xlii.space/cue/cue-does-it-all-but-can-it-literate/](https://xlii.space/cue/cue-does-it-all-but-can-it-literate/)

生成摘要时出错

---

## 60. Design and Implementation of Sprites

**原文标题**: Design and Implementation of Sprites

**原文链接**: [https://fly.io/blog/design-and-implementation/](https://fly.io/blog/design-and-implementation/)

生成摘要时出错

---

## 61. Show HN: TinyCity – A tiny city SIM for MicroPython (Thumby micro console)

**原文标题**: Show HN: TinyCity – A tiny city SIM for MicroPython (Thumby micro console)

**原文链接**: [https://github.com/chrisdiana/TinyCity](https://github.com/chrisdiana/TinyCity)

生成摘要时出错

---

## 62. Why senior engineers let bad projects fail

**原文标题**: Why senior engineers let bad projects fail

**原文链接**: [https://lalitm.com/post/why-senior-engineers-let-bad-projects-fail/](https://lalitm.com/post/why-senior-engineers-let-bad-projects-fail/)

生成摘要时出错

---

## 63. The 3D Software Rendering Technology of 1998's Thief: The Dark Project (2019)

**原文标题**: The 3D Software Rendering Technology of 1998's Thief: The Dark Project (2019)

**原文链接**: [https://nothings.org/gamedev/thief_rendering.html](https://nothings.org/gamedev/thief_rendering.html)

生成摘要时出错

---

## 64. The <Geolocation> HTML Element

**原文标题**: The <Geolocation> HTML Element

**原文链接**: [https://developer.chrome.com/blog/geolocation-html-element](https://developer.chrome.com/blog/geolocation-html-element)

生成摘要时出错

---

## 65. Use of Bayesian methodology in clinical trials of drug and biological products [pdf]

**原文标题**: Use of Bayesian methodology in clinical trials of drug and biological products [pdf]

**原文链接**: [https://www.fda.gov/media/190505/download](https://www.fda.gov/media/190505/download)

生成摘要时出错

---

## 66. Many college players among dozens charged in point-shaving plot

**原文标题**: Many college players among dozens charged in point-shaving plot

**原文链接**: [https://www.espn.com/mens-college-basketball/story/_/id/47619154/many-college-players-20-charged-point-shaving-scheme](https://www.espn.com/mens-college-basketball/story/_/id/47619154/many-college-players-20-charged-point-shaving-scheme)

生成摘要时出错

---

## 67. Building a better Bugbot

**原文标题**: Building a better Bugbot

**原文链接**: [https://cursor.com/blog/building-bugbot](https://cursor.com/blog/building-bugbot)

生成摘要时出错

---

## 68. Claude Cowork runs Linux VM via Apple virtualization framework

**原文标题**: Claude Cowork runs Linux VM via Apple virtualization framework

**原文链接**: [https://gist.github.com/simonw/35732f187edbe4fbd0bf976d013f22c8](https://gist.github.com/simonw/35732f187edbe4fbd0bf976d013f22c8)

生成摘要时出错

---

## 69. Have Taken Up Farming

**原文标题**: Have Taken Up Farming

**原文链接**: [https://dylan.gr/1768295794](https://dylan.gr/1768295794)

生成摘要时出错

---

## 70. The URL shortener that makes your links look as suspicious as possible

**原文标题**: The URL shortener that makes your links look as suspicious as possible

**原文链接**: [https://creepylink.com/](https://creepylink.com/)

生成摘要时出错

---

## 71. vLLM-MLX – Run LLMs on Mac at 464 tok/s

**原文标题**: vLLM-MLX – Run LLMs on Mac at 464 tok/s

**原文链接**: [https://github.com/waybarrios/vllm-mlx](https://github.com/waybarrios/vllm-mlx)

生成摘要时出错

---

## 72. UK High Court judgment on whether the Theft Act applies to Runescape gold pieces

**原文标题**: UK High Court judgment on whether the Theft Act applies to Runescape gold pieces

**原文链接**: [https://caselaw.nationalarchives.gov.uk/ewca/crim/2026/4](https://caselaw.nationalarchives.gov.uk/ewca/crim/2026/4)

生成摘要时出错

---

## 73. The five orders of ignorance (2000)

**原文标题**: The five orders of ignorance (2000)

**原文链接**: [https://cacm.acm.org/opinion/the-five-orders-of-ignorance/](https://cacm.acm.org/opinion/the-five-orders-of-ignorance/)

生成摘要时出错

---

## 74. Judge: ICE violated Liberian man's rights by bursting through front door

**原文标题**: Judge: ICE violated Liberian man's rights by bursting through front door

**原文链接**: [https://www.fox9.com/news/judge-ice-violated-liberian-mans-rights-bursting-through-front-door-during-arrest](https://www.fox9.com/news/judge-ice-violated-liberian-mans-rights-bursting-through-front-door-during-arrest)

生成摘要时出错

---

## 75. Handy – Free open source speech-to-text app

**原文标题**: Handy – Free open source speech-to-text app

**原文链接**: [https://github.com/cjpais/Handy](https://github.com/cjpais/Handy)

生成摘要时出错

---

## 76. A Unique Performance Optimization for a 3D Geometry Language

**原文标题**: A Unique Performance Optimization for a 3D Geometry Language

**原文链接**: [https://cprimozic.net/notes/posts/persistent-expr-memo-optimization-for-geoscript/](https://cprimozic.net/notes/posts/persistent-expr-memo-optimization-for-geoscript/)

生成摘要时出错

---

## 77. On Being a Human Being in the Time of Collapse (2022) [pdf]

**原文标题**: On Being a Human Being in the Time of Collapse (2022) [pdf]

**原文链接**: [https://web.cs.ucdavis.edu/~rogaway/papers/crisis/crisis.pdf](https://web.cs.ucdavis.edu/~rogaway/papers/crisis/crisis.pdf)

生成摘要时出错

---

## 78. Show HN: Sparrow-1 – Audio-native model for human-level turn-taking without ASR

**原文标题**: Show HN: Sparrow-1 – Audio-native model for human-level turn-taking without ASR

**原文链接**: [https://www.tavus.io/post/sparrow-1-human-level-conversational-timing-in-real-time-voice](https://www.tavus.io/post/sparrow-1-human-level-conversational-timing-in-real-time-voice)

生成摘要时出错

---

## 79. Claude Cowork exfiltrates files

**原文标题**: Claude Cowork exfiltrates files

**原文链接**: [https://www.promptarmor.com/resources/claude-cowork-exfiltrates-files](https://www.promptarmor.com/resources/claude-cowork-exfiltrates-files)

生成摘要时出错

---

## 80. SETI Home Flags 100 Signals After Sorting 12B Others

**原文标题**: SETI Home Flags 100 Signals After Sorting 12B Others

**原文链接**: [https://news.berkeley.edu/2026/01/12/for-21-years-enthusiasts-used-their-home-computers-to-search-for-et-uc-berkeley-scientists-are-homing-in-on-100-signals-they-found/](https://news.berkeley.edu/2026/01/12/for-21-years-enthusiasts-used-their-home-computers-to-search-for-et-uc-berkeley-scientists-are-homing-in-on-100-signals-they-found/)

生成摘要时出错

---

## 81. FCC Helps Verizon Make It Harder for You to Switch Wireless Carriers

**原文标题**: FCC Helps Verizon Make It Harder for You to Switch Wireless Carriers

**原文链接**: [https://www.techdirt.com/2026/01/16/trump-fcc-helps-verizon-make-it-harder-for-you-to-switch-wireless-carriers/](https://www.techdirt.com/2026/01/16/trump-fcc-helps-verizon-make-it-harder-for-you-to-switch-wireless-carriers/)

生成摘要时出错

---

## 82. Remails: A European Mail Transfer Agent

**原文标题**: Remails: A European Mail Transfer Agent

**原文链接**: [https://tweedegolf.nl/en/blog/197/remails](https://tweedegolf.nl/en/blog/197/remails)

生成摘要时出错

---

## 83. The State of OpenSSL for pyca/cryptography

**原文标题**: The State of OpenSSL for pyca/cryptography

**原文链接**: [https://cryptography.io/en/latest/statements/state-of-openssl/](https://cryptography.io/en/latest/statements/state-of-openssl/)

生成摘要时出错

---

## 84. The Z80 Mem­ber­ship Card (2015)

**原文标题**: The Z80 Mem­ber­ship Card (2015)

**原文链接**: [https://sunrise-ev.com/z80.htm](https://sunrise-ev.com/z80.htm)

生成摘要时出错

---

## 85. X (Twitter) Is Down

**原文标题**: X (Twitter) Is Down

**原文链接**: [https://downforeveryoneorjustme.com/twitter](https://downforeveryoneorjustme.com/twitter)

生成摘要时出错

---

## 86. Bubblewrap: A nimble way to prevent agents from accessing your .env files

**原文标题**: Bubblewrap: A nimble way to prevent agents from accessing your .env files

**原文链接**: [https://patrickmccanna.net/a-better-way-to-limit-claude-code-and-other-coding-agents-access-to-secrets/](https://patrickmccanna.net/a-better-way-to-limit-claude-code-and-other-coding-agents-access-to-secrets/)

生成摘要时出错

---

## 87. Show HN: Webctl – Browser automation for agents based on CLI instead of MCP

**原文标题**: Show HN: Webctl – Browser automation for agents based on CLI instead of MCP

**原文链接**: [https://github.com/cosinusalpha/webctl](https://github.com/cosinusalpha/webctl)

生成摘要时出错

---

## 88. Sun Position Calculator

**原文标题**: Sun Position Calculator

**原文链接**: [https://drajmarsh.bitbucket.io/earthsun.html](https://drajmarsh.bitbucket.io/earthsun.html)

生成摘要时出错

---

## 89. Playing Arcade Mahjong at Home? Or is it just a Mirage?

**原文标题**: Playing Arcade Mahjong at Home? Or is it just a Mirage?

**原文链接**: [https://nicole.express/2026/put-your-clothes-back-on.html](https://nicole.express/2026/put-your-clothes-back-on.html)

生成摘要时出错

---

## 90. Raspberry Pi's New AI Hat Adds 8GB of RAM for Local LLMs

**原文标题**: Raspberry Pi's New AI Hat Adds 8GB of RAM for Local LLMs

**原文链接**: [https://www.jeffgeerling.com/blog/2026/raspberry-pi-ai-hat-2/](https://www.jeffgeerling.com/blog/2026/raspberry-pi-ai-hat-2/)

生成摘要时出错

---

## 91. To those who fired or didn't hire tech writers because of AI

**原文标题**: To those who fired or didn't hire tech writers because of AI

**原文链接**: [https://passo.uno/letter-those-who-fired-tech-writers-ai/](https://passo.uno/letter-those-who-fired-tech-writers-ai/)

生成摘要时出错

---

## 92. Roam 50GB is now Roam 100GB

**原文标题**: Roam 50GB is now Roam 100GB

**原文链接**: [https://starlink.com/support/article/58c9c8b7-474e-246f-7e3c-06db3221d34d](https://starlink.com/support/article/58c9c8b7-474e-246f-7e3c-06db3221d34d)

生成摘要时出错

---

## 93. Go Home, Windows EXE, You're Drunk

**原文标题**: Go Home, Windows EXE, You're Drunk

**原文链接**: [https://gpfault.net/posts/drunk-exe.html](https://gpfault.net/posts/drunk-exe.html)

生成摘要时出错

---

## 94. Python: Tprof, a Targeting Profiler

**原文标题**: Python: Tprof, a Targeting Profiler

**原文链接**: [https://adamj.eu/tech/2026/01/14/python-introducing-tprof/](https://adamj.eu/tech/2026/01/14/python-introducing-tprof/)

生成摘要时出错

---

## 95. Ideas are cheap, execution is cheaper

**原文标题**: Ideas are cheap, execution is cheaper

**原文链接**: [https://davekiss.com/blog/ideas-are-cheap-execution-is-cheaper/](https://davekiss.com/blog/ideas-are-cheap-execution-is-cheaper/)

生成摘要时出错

---

## 96. Show HN: The Hessian of tall-skinny networks is easy to invert

**原文标题**: Show HN: The Hessian of tall-skinny networks is easy to invert

**原文链接**: [https://github.com/a-rahimi/hessian](https://github.com/a-rahimi/hessian)

生成摘要时出错

---

## 97. GitHub Incident

**原文标题**: GitHub Incident

**原文链接**: [https://www.githubstatus.com/incidents/q987xpbqjbpl](https://www.githubstatus.com/incidents/q987xpbqjbpl)

生成摘要时出错

---

## 98. I Made Adobe CC Installers Work on Linux

**原文标题**: I Made Adobe CC Installers Work on Linux

**原文链接**: [https://old.reddit.com/r/linux_gaming/comments/1qdgd73/i_made_adobe_cc_installers_work_on_linux_pr_in/](https://old.reddit.com/r/linux_gaming/comments/1qdgd73/i_made_adobe_cc_installers_work_on_linux_pr_in/)

生成摘要时出错

---

## 99. The Gleam Programming Language

**原文标题**: The Gleam Programming Language

**原文链接**: [https://gleam.run/](https://gleam.run/)

生成摘要时出错

---

## 100. America could have $4 lunch bowls like Japan but for zoning laws

**原文标题**: America could have $4 lunch bowls like Japan but for zoning laws

**原文链接**: [https://abio.substack.com/p/america-could-have-4-lunch-bowls](https://abio.substack.com/p/america-could-have-4-lunch-bowls)

生成摘要时出错

---

