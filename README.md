# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-16.md)

*最后自动更新时间: 2026-01-16 17:52:36*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 2 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 3 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 4 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 5 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 6 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 7 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 8 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 9 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 10 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 11 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 12 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 13 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 14 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 15 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 16 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 17 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 18 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 19 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 20 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 21 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 22 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 23 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 24 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 25 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 26 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 27 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 28 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 29 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 30 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 31 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 32 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 33 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 34 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 35 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 36 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 37 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 38 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 39 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 40 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 41 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 42 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 43 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 44 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 45 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 46 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 47 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 48 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 49 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 50 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 51 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 52 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 53 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 54 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 55 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 56 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 57 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 58 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 59 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 60 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 61 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 62 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 63 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 64 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 65 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 66 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 67 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 68 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 69 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 70 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 71 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 72 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 73 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 74 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 75 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 76 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 77 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 78 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 79 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 80 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 81 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 82 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 83 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 84 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 85 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 86 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 87 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 88 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 89 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 90 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 91 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 92 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 93 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 94 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 95 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 96 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 97 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 98 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 99 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 100 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 101 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 102 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 103 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 104 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 105 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 106 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 107 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 108 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 109 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 110 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 111 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 112 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 113 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 114 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 115 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 116 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 117 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 118 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 119 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 120 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 121 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 122 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 123 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 124 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 125 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 126 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 127 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 128 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 129 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 130 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 131 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 132 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 133 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 134 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 135 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 136 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 137 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 138 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 139 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 140 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 141 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 142 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 143 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 144 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 145 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 146 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 147 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 148 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 149 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 150 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 151 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 152 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 153 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 154 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 155 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 156 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 157 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 158 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 159 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 160 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 161 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 162 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 163 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 164 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 165 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 166 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 167 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 168 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 169 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 170 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 171 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 172 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 173 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 174 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 175 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 176 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 177 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 178 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 179 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 180 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 181 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 182 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 183 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 184 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 185 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 186 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 187 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 188 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 189 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 190 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 191 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 192 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 193 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 194 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 195 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 196 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 197 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 198 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 199 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 200 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 201 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 202 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 203 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 204 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 205 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 206 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 207 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 208 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 209 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 210 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 211 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 212 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 213 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 214 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 215 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 216 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 217 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 218 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 219 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 220 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 221 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 222 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 223 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 224 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 225 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 226 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 227 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 228 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 229 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 230 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 231 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 232 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 233 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 234 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 235 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 236 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 237 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 238 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 239 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 240 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 241 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 242 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 243 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 244 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 245 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 246 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 247 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 248 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 249 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 250 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 251 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 252 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 253 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 254 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 255 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 256 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 257 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 258 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 259 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 260 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 261 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 262 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 263 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 264 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 265 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 266 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 267 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 268 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 269 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 270 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 271 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 272 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 273 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 274 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 275 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 276 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 277 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 278 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 279 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 280 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 281 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 282 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 283 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 284 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 285 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 286 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 287 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 288 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 289 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 290 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 291 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 292 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 293 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 294 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 295 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 296 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 297 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 298 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 299 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 300 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 301 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 302 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
