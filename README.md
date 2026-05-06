# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-06.md)

*最后自动更新时间: 2026-05-06 18:47:02*
## 1. Valve 以知识共享许可协议公开 Steam 控制器 CAD 文件

**原文标题**: Valve releases Steam Controller CAD files under Creative Commons license

**原文链接**: [https://www.digitalfoundry.net/news/2026/05/valve-releases-steam-controller-cad-files-under-creative-commons-license](https://www.digitalfoundry.net/news/2026/05/valve-releases-steam-controller-cad-files-under-creative-commons-license)

Valve 发布了新款 Steam 控制器及其配套“Puck”设备的完整 CAD 文件，使社区能够设计并 3D 打印定制配件。发布内容包括表面拓扑文件（.STP 和 .STL 格式）以及工程图纸，其中标明了为确保最佳信号强度和功能而不得遮盖的关键区域。

通过公开这些文件，Valve 旨在鼓励 Mod 制作者开发各类附件，如充电底座、外壳、握把扩展器和手机支架。此举延续了 Valve 支持硬件改装的一贯传统，此前该公司也曾为 Steam Deck、Valve Index 和初代 Steam 控制器发布过类似文件。

这些文件基于“知识共享”（Creative Commons）许可协议发布，允许非商业用途，前提是创作者需进行适当署名并向社区分享其设计。有意制造配件的商业实体请直接联系 Valve 洽谈授权条款。这一举措在保障设备技术完整性的前提下，赋予了爱好者们定制个性化硬件体验的能力。

---

## 2. Appearing Productive in the Workplace

**原文标题**: Appearing Productive in the Workplace

**原文链接**: [https://nooneshappy.com/article/appearing-productive-in-the-workplace/](https://nooneshappy.com/article/appearing-productive-in-the-workplace/)

This article explores the deceptive nature of AI-driven productivity, arguing that while large language models can generate infinite "work," they often facilitate **output-competence decoupling**. This phenomenon severs the link between the quality of a deliverable and the actual skill of the person producing it, allowing novices to impersonate experts without possessing the judgment to verify the results.

The author identifies several critical risks:
*   **Cross-Domain Failure:** Workers are using AI to perform complex tasks in disciplines they aren't trained in (e.g., non-engineers designing data architectures). This creates work that looks polished but is fundamentally flawed.
*   **The Conduit Problem:** Humans are becoming mere "conduits" for AI output. Because the "slowness" of traditional work—which historically built expertise—is being bypassed, the pipeline for developing future experts is thinning.
*   **Internal Slop:** AI has made it cheap to produce massive amounts of documentation. This results in "internal slop"—lengthy reports and memos that no one reads—which drowns out actual signal and creates a false sense of momentum.
*   **Managerial Failure:** Many organizations prioritize the appearance of progress over correctness. Research indicates that AI is sycophantic (affirming users even when they are wrong) and that novices are particularly prone to overestimating their AI-boosted performance.

The article concludes that the "human-in-the-loop" is not a bottleneck to be removed, but the only component with the "skin in the game" necessary for quality control. To remain competitive, firms must treat AI as a tool for throughput directed by human judgment, rather than a replacement for it. Ultimately, the author predicts a "reckoning" where firms that have hollowed out their expertise will lose to those that maintain trusted, human-verified work.

---

## 3. 从 Supabase 到 Clerk 再到 Better Auth

**原文标题**: From Supabase to Clerk to Better Auth

**原文链接**: [https://blog.val.town/better-auth](https://blog.val.town/better-auth)

在这篇文章中，Tom MacWright 概述了 Val Town 为何将其身份验证系统从 Clerk 迁移到 Better Auth，这标志着其从 Supabase 转向更受控、自托管架构的多年历程正式告一段落。

在承认 Clerk 商业成功的同时，MacWright 解释了其架构如何为 Val Town 这样的社交平台带来了巨大阻力。其“核心问题”在于 Clerk 试图取代本地用户表的理念，这导致了两个主要问题：

1.  **速率限制与复杂性：** 由于 Clerk 存在严格的速率限制，Val Town 无法可靠地通过 API 获取社交动态所需的用户数据（如头像和用户名）。这迫使他们不得不使用 Webhook 来维护一个辅助本地数据库，导致同步过程既复杂又“脆弱”。
2.  **单点故障：** Clerk 管理着所有的用户会话。一旦 Clerk 宕机（作者指出这种情况发生的频率足以令人担忧），整个 Val Town 网站对所有用户都将变得不可用，因为连现有的会话也无法刷新。

MacWright 选择 Better Auth 作为替代方案，是因为这款开源解决方案能让 Val Town 拥有用户和会话数据的所有权。这种架构消除了站点可用性对第三方的依赖，同时仍能提供高质量的 SDK 和框架集成。Better Auth 的付费“基础设施”功能保持了无状态特性，确保了 Val Town 核心身份验证的独立性。

整个过渡通过让两套身份验证系统并行运行两周来完成，使用户能够在登录时自然地完成迁移。MacWright 总结道，对于复杂的社交应用而言，将关键的会话管理外包给第三方存在巨大风险，而“正确”的工具往往取决于项目的具体架构需求。

---

## 4. 瓶颈从来不是代码

**原文标题**: The bottleneck was never the code

**原文链接**: [https://www.thetypicalset.com/blog/thoughts-on-coding-agents](https://www.thetypicalset.com/blog/thoughts-on-coding-agents)

在《瓶颈从来不在代码》一文中，作者指出，尽管 AI 编程助手极大地提高了个人生产力，但它们并不会自动加速整个软件行业。相反，它们暴露了行业真正的瓶颈：人类的协商与组织的一致性。

借鉴《人月神话》等软件经典著作，作者认为代码仅仅是人类在达成“构建什么”的共识后留下的“残余物”。随着 AI 助手让代码编写变得近乎免费，工作重心转向了管理和产出精确的技术规范。这引发了“杰文斯悖论”：当代码成本降低时，组织并不会节省时间，反而会开发更多功能，从而增加了对严谨专注力以及“拒绝”能力的需求。

AI 助手的一个关键局限是缺乏“共享上下文”。人类通过“渗透作用”（如会议、Slack 讨论、过往故障）获得项目直觉，而助手只知道被明确提供的信息。缺乏这种非书面的底层认知，助手会产生看似合理但错误的方案。为解决这一问题，作者建议建立一种“读取并提取”循环：利用助手挖掘“组织废气”（如 PR 评论和旧讨论帖），将隐性知识显性化并存入知识库，供人类和助手共同使用。

最终，AI 助手充当了组织文化的“倍增器”。对于小型且团结的团队，其影响是积极的；然而对于大型组织，助手可能只是帮助“糟糕的组织”更快地搞砸事情。AI 时代的竞争护城河并非技术基础设施，而是通过强大的写作文化来保持一致性并将上下文显性化的能力。成功取决于将组织一致性视为一种必须管理和维护的实体产物。

---

## 5. 智能体现已能够创建 Cloudflare 账户、购买域名并进行部署。

**原文标题**: Agents can now create Cloudflare accounts, buy domains, and deploy

**原文链接**: [https://blog.cloudflare.com/agents-stripe-projects/](https://blog.cloudflare.com/agents-stripe-projects/)

Cloudflare 宣布与 Stripe 达成合作，使 AI 编程智能体能够自主管理整个部署生命周期。通过与 Stripe 共同设计的新协议，智能体现在可以创建 Cloudflare 账户、注册域名，并直接将应用程序部署到生产环境，无需人工干预。

**核心特性与功能：**
*   **零配置部署：** 智能体可以通过自动配置账户和签发 API 令牌，实现“从零到生产环境”的跨越。用户不再需要手动操作控制面板或手动复制粘贴凭据。
*   **自动化支付：** 利用 “Stripe Projects”，智能体可以处理付费订阅和域名购买。安全性通过令牌化支付和默认支出限制（通常为每月 100 美元）来保障，以防止未经授权的超支。
*   **发现与授权：** 智能体使用新的 REST API 目录来发现可用服务。Stripe 充当身份提供者；如果用户没有 Cloudflare 账户，系统将根据其 Stripe 凭据自动为其配置。

**协议结构：**
该集成依赖于三大支柱：**发现**（寻找服务）、**授权**（通过 OAuth/OIDC 进行身份认证）和**支付**（安全的令牌化计费）。虽然此次初始发布与 Stripe Projects CLI 绑定，但 Cloudflare 计划将此协议推行成为一种标准，允许任何拥有登录用户的平台充当云服务的“编排者”。

**激励措施与获取途径：**
为了支持此次发布，Cloudflare 为通过 Stripe Atlas 注册的新初创公司提供 **10 万美元的抵扣额度**。该系统目前已通过 Stripe CLI 开启公测，开发者只需一条命令，即可驱动智能体在 Cloudflare 上构建并部署生产级应用程序。

---

## 6. CARA 2.0 – “I Built a Better Robot Dog”

**原文标题**: CARA 2.0 – “I Built a Better Robot Dog”

**原文链接**: [https://www.aaedmusa.com/projects/cara2](https://www.aaedmusa.com/projects/cara2)

生成摘要时出错

---

## 7. What makes a good smartphone camera?

**原文标题**: What makes a good smartphone camera?

**原文链接**: [https://cadence.moe/blog/2026-05-05-what-makes-a-good-smartphone-camera](https://cadence.moe/blog/2026-05-05-what-makes-a-good-smartphone-camera)

生成摘要时出错

---

## 8. Show HN: I built an open-source email builder, alternative to Beefree/Unlayer

**原文标题**: Show HN: I built an open-source email builder, alternative to Beefree/Unlayer

**原文链接**: [https://play.templatical.com](https://play.templatical.com)

生成摘要时出错

---

## 9. Setting up a Sun Ray server on OpenIndiana Hipster 2025.10

**原文标题**: Setting up a Sun Ray server on OpenIndiana Hipster 2025.10

**原文链接**: [https://catstret.ch/202605/srss-hipster202510/](https://catstret.ch/202605/srss-hipster202510/)

生成摘要时出错

---

## 10. Google tools for customizing searches

**原文标题**: Google tools for customizing searches

**原文链接**: [https://cardcatalogforlife.substack.com/p/google-has-a-secret-reference-desk](https://cardcatalogforlife.substack.com/p/google-has-a-secret-reference-desk)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 2 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 3 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 4 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 5 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 6 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 7 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 8 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 9 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 10 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 11 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 12 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 13 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 14 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 15 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 16 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 17 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 18 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 19 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 20 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 21 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 22 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 23 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 24 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 25 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 26 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 27 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 28 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 29 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 30 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 31 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 32 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 33 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 34 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 35 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 36 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 37 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 38 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 39 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 40 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 41 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 42 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 43 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 44 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 45 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 46 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 47 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 48 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 49 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 50 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 51 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 52 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 53 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 54 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 55 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 56 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 57 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 58 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 59 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 60 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 61 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 62 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 63 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 64 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 65 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 66 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 67 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 68 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 69 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 70 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 71 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 72 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 73 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 74 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 75 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 76 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 77 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 78 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 79 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 80 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 81 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 82 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 83 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 84 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 85 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 86 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 87 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 88 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 89 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 90 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 91 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 92 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 93 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 94 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 95 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 96 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 97 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 98 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 99 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 100 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 101 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 102 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 103 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 104 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 105 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 106 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 107 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 108 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 109 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 110 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 111 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 112 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 113 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 114 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 115 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 116 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 117 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 118 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 119 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 120 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 121 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 122 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 123 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 124 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 125 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 126 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 127 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 128 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 129 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 130 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 131 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 132 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 133 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 134 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 135 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 136 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 137 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 138 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 139 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 140 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 141 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 142 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 143 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 144 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 145 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 146 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 147 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 148 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 149 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 150 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 151 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 152 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 153 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 154 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 155 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 156 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 157 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 158 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 159 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 160 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 161 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 162 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 163 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 164 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 165 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 166 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 167 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 168 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 169 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 170 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 171 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 172 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 173 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 174 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 175 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 176 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 177 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 178 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 179 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 180 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 181 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 182 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 183 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 184 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 185 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 186 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 187 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 188 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 189 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 190 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 191 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 192 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 193 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 194 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 195 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 196 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 197 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 198 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 199 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 200 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 201 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 202 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 203 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 204 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 205 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 206 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 207 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 208 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 209 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 210 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 211 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 212 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 213 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 214 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 215 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 216 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 217 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 218 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 219 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 220 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 221 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 222 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 223 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 224 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 225 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 226 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 227 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 228 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 229 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 230 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 231 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 232 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 233 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 234 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 235 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 236 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 237 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 238 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 239 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 240 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 241 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 242 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 243 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 244 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 245 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 246 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 247 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 248 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 249 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 250 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 251 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 252 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 253 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 254 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 255 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 256 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 257 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 258 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 259 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 260 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 261 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 262 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 263 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 264 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 265 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 266 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 267 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 268 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 269 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 270 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 271 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 272 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 273 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 274 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 275 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 276 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 277 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 278 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 279 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 280 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 281 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 282 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 283 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 284 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 285 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 286 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 287 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 288 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 289 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 290 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 291 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 292 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 293 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 294 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 295 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 296 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 297 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 298 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 299 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 300 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 301 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 302 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 303 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 304 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 305 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 306 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 307 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 308 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 309 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 310 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 311 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 312 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 313 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 314 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 315 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 316 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 317 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 318 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 319 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 320 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 321 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 322 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 323 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 324 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 325 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 326 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 327 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 328 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 329 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 330 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 331 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 332 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 333 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 334 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 335 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 336 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 337 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 338 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 339 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 340 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 341 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 342 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 343 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 344 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 345 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 346 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 347 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 348 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 349 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 350 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 351 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 352 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 353 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 354 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 355 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 356 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 357 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 358 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 359 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 360 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 361 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 362 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 363 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 364 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 365 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 366 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 367 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 368 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 369 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 370 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 371 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 372 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 373 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 374 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 375 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 376 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 377 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 378 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 379 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 380 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 381 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 382 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 383 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 384 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 385 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 386 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 387 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 388 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 389 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 390 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 391 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 392 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 393 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 394 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 395 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 396 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 397 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 398 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 399 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 400 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 401 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 402 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 403 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 404 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 405 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 406 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 407 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 408 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 409 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 410 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 411 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 412 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
