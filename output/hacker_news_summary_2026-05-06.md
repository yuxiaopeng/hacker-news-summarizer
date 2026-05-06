# Hacker News 热门文章摘要 (2026-05-06)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Show HN: Tilde.run – Agent Sandbox with a Transactional, Versioned Filesystem

**原文标题**: Show HN: Tilde.run – Agent Sandbox with a Transactional, Versioned Filesystem

**原文链接**: [https://tilde.run/](https://tilde.run/)

生成摘要时出错

---

## 12. Colombia hosts talks on exiting fossil fuels as global energy crisis deepens

**原文标题**: Colombia hosts talks on exiting fossil fuels as global energy crisis deepens

**原文链接**: [https://www.latimes.com/environment/story/2026-04-26/colombia-hosts-talks-on-exiting-fossil-fuels-as-global-energy-crisis-deepens](https://www.latimes.com/environment/story/2026-04-26/colombia-hosts-talks-on-exiting-fossil-fuels-as-global-energy-crisis-deepens)

生成摘要时出错

---

## 13. The Thinking Plant's Man (2025)

**原文标题**: The Thinking Plant's Man (2025)

**原文链接**: [https://www.sciencehistory.org/stories/magazine/the-thinking-plants-man/](https://www.sciencehistory.org/stories/magazine/the-thinking-plants-man/)

生成摘要时出错

---

## 14. Knitting bullshit

**原文标题**: Knitting bullshit

**原文链接**: [https://katedaviesdesigns.com/2026/04/29/knitting-bullshit/](https://katedaviesdesigns.com/2026/04/29/knitting-bullshit/)

生成摘要时出错

---

## 15. Reverse-engineering the 1998 Ultima Online demo server

**原文标题**: Reverse-engineering the 1998 Ultima Online demo server

**原文链接**: [https://draxinar.github.io/articles/2026-05-01-uodemo-reverse-engineering.html](https://draxinar.github.io/articles/2026-05-01-uodemo-reverse-engineering.html)

生成摘要时出错

---

## 16. CNN founder Ted Turner, a pioneer of cable TV news, dies at 87

**原文标题**: CNN founder Ted Turner, a pioneer of cable TV news, dies at 87

**原文链接**: [https://www.cnn.com/2026/05/06/us/ted-turner-death](https://www.cnn.com/2026/05/06/us/ted-turner-death)

生成摘要时出错

---

## 17. Batteries Not Included, or Required, for These Smart Home Sensors

**原文标题**: Batteries Not Included, or Required, for These Smart Home Sensors

**原文链接**: [https://coe.gatech.edu/news/2026/04/batteries-not-included-or-required-these-smart-home-sensors](https://coe.gatech.edu/news/2026/04/batteries-not-included-or-required-these-smart-home-sensors)

生成摘要时出错

---

## 18. Coverage Cat (YC S22) Seeks Fractional Engineer to build AI Growth Toolkit

**原文标题**: Coverage Cat (YC S22) Seeks Fractional Engineer to build AI Growth Toolkit

**原文链接**: [https://www.coveragecat.com/careers/engineering/fractional-growth-engineer](https://www.coveragecat.com/careers/engineering/fractional-growth-engineer)

生成摘要时出错

---

## 19. Multi-stroke text effect in CSS

**原文标题**: Multi-stroke text effect in CSS

**原文链接**: [https://yuanchuan.dev/multi-stroke-text-effect-in-css](https://yuanchuan.dev/multi-stroke-text-effect-in-css)

生成摘要时出错

---

## 20. Vibe coding and agentic engineering are getting closer than I'd like

**原文标题**: Vibe coding and agentic engineering are getting closer than I'd like

**原文链接**: [https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/)

生成摘要时出错

---

## 21. 245TB Micron 6600 ION Data Center SSD Now Shipping

**原文标题**: 245TB Micron 6600 ION Data Center SSD Now Shipping

**原文链接**: [https://investors.micron.com/news-releases/news-release-details/industry-leading-245tb-micron-6600-ion-data-center-ssd-now](https://investors.micron.com/news-releases/news-release-details/industry-leading-245tb-micron-6600-ion-data-center-ssd-now)

生成摘要时出错

---

## 22. Wolfenstein 3D for Gameboy Color on custom cartridge (2016)

**原文标题**: Wolfenstein 3D for Gameboy Color on custom cartridge (2016)

**原文链接**: [https://www.happydaze.se/wolf/](https://www.happydaze.se/wolf/)

生成摘要时出错

---

## 23. YouTube, your RSS feeds are broken

**原文标题**: YouTube, your RSS feeds are broken

**原文链接**: [https://openrss.org/blog/youtube-your-feeds-are-broken](https://openrss.org/blog/youtube-your-feeds-are-broken)

生成摘要时出错

---

## 24. StarFighter 16-Inch

**原文标题**: StarFighter 16-Inch

**原文链接**: [https://us.starlabs.systems/pages/starfighter](https://us.starlabs.systems/pages/starfighter)

生成摘要时出错

---

## 25. Going Full Time on Open Source

**原文标题**: Going Full Time on Open Source

**原文链接**: [https://jdx.dev/posts/2026-04-17-going-full-time-on-open-source/](https://jdx.dev/posts/2026-04-17-going-full-time-on-open-source/)

生成摘要时出错

---

## 26. Egg Intake and the Incidence of Alzheimer's Disease in Adventist Health Study-2

**原文标题**: Egg Intake and the Incidence of Alzheimer's Disease in Adventist Health Study-2

**原文链接**: [https://www.sciencedirect.com/science/article/pii/S0022316626001902](https://www.sciencedirect.com/science/article/pii/S0022316626001902)

生成摘要时出错

---

## 27. RAM prices are forcing companies to choose higher prices, worse specs, or both

**原文标题**: RAM prices are forcing companies to choose higher prices, worse specs, or both

**原文链接**: [https://gizmodo.com/shrinkflation-is-quietly-making-all-gadgets-worse-2000754565](https://gizmodo.com/shrinkflation-is-quietly-making-all-gadgets-worse-2000754565)

生成摘要时出错

---

## 28. Google Cloud fraud defense, the next evolution of reCAPTCHA

**原文标题**: Google Cloud fraud defense, the next evolution of reCAPTCHA

**原文链接**: [https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-fraud-defense-the-next-evolution-of-recaptcha/](https://cloud.google.com/blog/products/identity-security/introducing-google-cloud-fraud-defense-the-next-evolution-of-recaptcha/)

生成摘要时出错

---

## 29. Google Chrome silently installs a 4 GB AI model on your device without consent

**原文标题**: Google Chrome silently installs a 4 GB AI model on your device without consent

**原文链接**: [https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/](https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/)

生成摘要时出错

---

## 30. Virtual violin produces realistic sounds

**原文标题**: Virtual violin produces realistic sounds

**原文链接**: [https://news.mit.edu/2026/mit-engineers-virtual-violin-produces-realistic-sounds-0429](https://news.mit.edu/2026/mit-engineers-virtual-violin-produces-realistic-sounds-0429)

生成摘要时出错

---

## 31. Higher usage limits for Claude and a compute deal with SpaceX

**原文标题**: Higher usage limits for Claude and a compute deal with SpaceX

**原文链接**: [https://www.anthropic.com/news/higher-limits-spacex](https://www.anthropic.com/news/higher-limits-spacex)

生成摘要时出错

---

## 32. DNSSEC disruption affecting .de domains – Resolved

**原文标题**: DNSSEC disruption affecting .de domains – Resolved

**原文链接**: [https://status.denic.de/pages/incident/592577eab611ce1e0d00046f/69fa60ef9d12f5057a974f38](https://status.denic.de/pages/incident/592577eab611ce1e0d00046f/69fa60ef9d12f5057a974f38)

生成摘要时出错

---

## 33. Wiki Builder: Skill to Build LLM Knowledge Bases

**原文标题**: Wiki Builder: Skill to Build LLM Knowledge Bases

**原文链接**: [https://academy.dair.ai/blog/wiki-builder-claude-code-plugin](https://academy.dair.ai/blog/wiki-builder-claude-code-plugin)

生成摘要时出错

---

## 34. Mexico City is sinking so quickly, it can be seen from space

**原文标题**: Mexico City is sinking so quickly, it can be seen from space

**原文链接**: [https://apnews.com/article/mexico-city-sinking-nasa-satellite-imagery-b5a70fbc2f73a789f248ab69b08c75e7](https://apnews.com/article/mexico-city-sinking-nasa-satellite-imagery-b5a70fbc2f73a789f248ab69b08c75e7)

生成摘要时出错

---

## 35. Our Continuation of MkDocs

**原文标题**: Our Continuation of MkDocs

**原文链接**: [https://github.com/orgs/ProperDocs/discussions/33](https://github.com/orgs/ProperDocs/discussions/33)

生成摘要时出错

---

## 36. Accelerating Gemma 4: faster inference with multi-token prediction drafters

**原文标题**: Accelerating Gemma 4: faster inference with multi-token prediction drafters

**原文链接**: [https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/)

生成摘要时出错

---

## 37. Revisiting the 2015 Open Source Census

**原文标题**: Revisiting the 2015 Open Source Census

**原文链接**: [https://nesbitt.io/2026/05/06/revisiting-the-2015-open-source-census.html](https://nesbitt.io/2026/05/06/revisiting-the-2015-open-source-census.html)

生成摘要时出错

---

## 38. Show HN: Adam – An embeddable cross-platform AI agent library

**原文标题**: Show HN: Adam – An embeddable cross-platform AI agent library

**原文链接**: [https://github.com/sqliteai/adam](https://github.com/sqliteai/adam)

生成摘要时出错

---

## 39. Building the deployment tool I wish I had

**原文标题**: Building the deployment tool I wish I had

**原文链接**: [https://ruuda.nl/2026/deptool](https://ruuda.nl/2026/deptool)

生成摘要时出错

---

## 40. Telus Uses AI to Alter Call-Agent Accents

**原文标题**: Telus Uses AI to Alter Call-Agent Accents

**原文链接**: [https://letsdatascience.com/news/telus-uses-ai-to-alter-call-agent-accents-a3868f63](https://letsdatascience.com/news/telus-uses-ai-to-alter-call-agent-accents-a3868f63)

生成摘要时出错

---

## 41. SpaceXAI will provide Anthropic with access to Colossus 1

**原文标题**: SpaceXAI will provide Anthropic with access to Colossus 1

**原文链接**: [https://twitter.com/xai/status/2052060350770515978](https://twitter.com/xai/status/2052060350770515978)

生成摘要时出错

---

## 42. Red Squares – GitHub outages as contributions

**原文标题**: Red Squares – GitHub outages as contributions

**原文链接**: [https://red-squares.cian.lol/](https://red-squares.cian.lol/)

生成摘要时出错

---

## 43. Visualize Any Hugging Face Model

**原文标题**: Visualize Any Hugging Face Model

**原文链接**: [https://hfviewer.com/](https://hfviewer.com/)

生成摘要时出错

---

## 44. Behavior-Oriented Concurrency for Python

**原文标题**: Behavior-Oriented Concurrency for Python

**原文链接**: [https://microsoft.github.io/bocpy/](https://microsoft.github.io/bocpy/)

生成摘要时出错

---

## 45. TikTok's algorithm favored Republican content in 2024 US elections, study finds

**原文标题**: TikTok's algorithm favored Republican content in 2024 US elections, study finds

**原文链接**: [https://www.theguardian.com/technology/2026/may/06/tiktok-pro-republican-algorithm-2024-election](https://www.theguardian.com/technology/2026/may/06/tiktok-pro-republican-algorithm-2024-election)

生成摘要时出错

---

## 46. Write some software, give it away for free

**原文标题**: Write some software, give it away for free

**原文链接**: [https://nonogra.ph/write-some-software-give-it-away-for-free-05-05-2026](https://nonogra.ph/write-some-software-give-it-away-for-free-05-05-2026)

生成摘要时出错

---

## 47. Computer Use is 45x more expensive than structured APIs

**原文标题**: Computer Use is 45x more expensive than structured APIs

**原文链接**: [https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/](https://reflex.dev/blog/computer-use-is-45x-more-expensive-than-structured-apis/)

生成摘要时出错

---

## 48. Make some art with your phone sensors

**原文标题**: Make some art with your phone sensors

**原文链接**: [https://tautme.github.io/phone-sensors/sensor-etch.html](https://tautme.github.io/phone-sensors/sensor-etch.html)

生成摘要时出错

---

## 49. Three Inverse Laws of AI

**原文标题**: Three Inverse Laws of AI

**原文链接**: [https://susam.net/inverse-laws-of-robotics.html](https://susam.net/inverse-laws-of-robotics.html)

生成摘要时出错

---

## 50. Chrome downloads a 4GB AI file without user consent, researcher alleges

**原文标题**: Chrome downloads a 4GB AI file without user consent, researcher alleges

**原文链接**: [https://www.engadget.com/2166113/chrome-downloads-a-4gb-ai-file-without-user-consent-researcher-alleges/](https://www.engadget.com/2166113/chrome-downloads-a-4gb-ai-file-without-user-consent-researcher-alleges/)

生成摘要时出错

---

## 51. Accelerating the GraalVM Release Train

**原文标题**: Accelerating the GraalVM Release Train

**原文链接**: [https://medium.com/graalvm/accelerating-the-graalvm-release-train-26b0d7cff2ab](https://medium.com/graalvm/accelerating-the-graalvm-release-train-26b0d7cff2ab)

生成摘要时出错

---

## 52. California farmers to destroy 420k peach trees following Del Monte bankruptcy

**原文标题**: California farmers to destroy 420k peach trees following Del Monte bankruptcy

**原文链接**: [https://www.sfgate.com/centralcoast/article/usda-aid-california-farmers-22240694.php](https://www.sfgate.com/centralcoast/article/usda-aid-california-farmers-22240694.php)

生成摘要时出错

---

## 53. Ombudsman column: The Pentagon is trying to silence me

**原文标题**: Ombudsman column: The Pentagon is trying to silence me

**原文链接**: [https://www.stripes.com/opinion/2026-04-23/stripes-former-ombudsman-pentagon-trying-to-silence-21465037.html](https://www.stripes.com/opinion/2026-04-23/stripes-former-ombudsman-pentagon-trying-to-silence-21465037.html)

生成摘要时出错

---

## 54. Companies Will Stop Making Software

**原文标题**: Companies Will Stop Making Software

**原文链接**: [https://thegeneralpartnership.substack.com/p/the-best-companies-will-stop-making](https://thegeneralpartnership.substack.com/p/the-best-companies-will-stop-making)

生成摘要时出错

---

## 55. Comparing the Z80 and 6502 to Their Relatives

**原文标题**: Comparing the Z80 and 6502 to Their Relatives

**原文链接**: [https://bumbershootsoft.wordpress.com/2026/05/02/comparing-the-z80-and-6502-to-their-relatives/](https://bumbershootsoft.wordpress.com/2026/05/02/comparing-the-z80-and-6502-to-their-relatives/)

生成摘要时出错

---

## 56. EEVblog: The 555 Timer is 55 years old [video]

**原文标题**: EEVblog: The 555 Timer is 55 years old [video]

**原文链接**: [https://www.youtube.com/watch?v=6JhK8iCQuqI](https://www.youtube.com/watch?v=6JhK8iCQuqI)

生成摘要时出错

---

## 57. Zuckerberg 'Personally Authorized and Encouraged' Meta's Copyright Infringement

**原文标题**: Zuckerberg 'Personally Authorized and Encouraged' Meta's Copyright Infringement

**原文链接**: [https://variety.com/2026/digital/news/meta-ai-mark-zuckerberg-copyright-infringement-lawsuit-publishers-scott-turow-1236738383/](https://variety.com/2026/digital/news/meta-ai-mark-zuckerberg-copyright-infringement-lawsuit-publishers-scott-turow-1236738383/)

生成摘要时出错

---

## 58. Academics Need to Wake Up on AI

**原文标题**: Academics Need to Wake Up on AI

**原文链接**: [https://www.popularbydesign.org/p/academics-need-to-wake-up-on-ai](https://www.popularbydesign.org/p/academics-need-to-wake-up-on-ai)

生成摘要时出错

---

## 59. I completed 100 Days of Java over 5 years and mapped the journey as a graph

**原文标题**: I completed 100 Days of Java over 5 years and mapped the journey as a graph

**原文链接**: [https://mohibulsblog.netlify.app/java/100daysofjava/graph/](https://mohibulsblog.netlify.app/java/100daysofjava/graph/)

生成摘要时出错

---

## 60. iOS 27 is adding a 'Create a Pass' button to Apple Wallet

**原文标题**: iOS 27 is adding a 'Create a Pass' button to Apple Wallet

**原文链接**: [https://walletwallet.alen.ro/blog/ios-27-wallet-create-pass/](https://walletwallet.alen.ro/blog/ios-27-wallet-create-pass/)

生成摘要时出错

---

## 61. Today I've made the difficult decision to reduce the size of Coinbase by ~14%

**原文标题**: Today I've made the difficult decision to reduce the size of Coinbase by ~14%

**原文链接**: [https://twitter.com/brian_armstrong/status/2051616759145185723](https://twitter.com/brian_armstrong/status/2051616759145185723)

生成摘要时出错

---

## 62. Lessons for Agentic Coding: What should we do when code is cheap?

**原文标题**: Lessons for Agentic Coding: What should we do when code is cheap?

**原文链接**: [https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html](https://www.dbreunig.com/2026/05/04/10-lessons-for-agentic-coding.html)

生成摘要时出错

---

## 63. Hand Drawn QR Codes (2025)

**原文标题**: Hand Drawn QR Codes (2025)

**原文链接**: [https://sethmlarson.dev/hand-drawn-qr-codes](https://sethmlarson.dev/hand-drawn-qr-codes)

生成摘要时出错

---

## 64. Google Chrome silently installs 4 GB Gemini Nano AI model without consent

**原文标题**: Google Chrome silently installs 4 GB Gemini Nano AI model without consent

**原文链接**: [https://alternativeto.net/news/2026/5/google-chrome-silently-installs-4-gb-gemini-nano-ai-model-to-user-device-without-consent/](https://alternativeto.net/news/2026/5/google-chrome-silently-installs-4-gb-gemini-nano-ai-model-to-user-device-without-consent/)

生成摘要时出错

---

## 65. Canadian fiddler sues Google after AI Overview claimed he was a sex offender

**原文标题**: Canadian fiddler sues Google after AI Overview claimed he was a sex offender

**原文链接**: [https://www.theguardian.com/music/2026/may/05/canadian-ashley-macisaac-fiddler-musician-singer-songwriter-sues-google-ai-sex-offender-ntwnfb](https://www.theguardian.com/music/2026/may/05/canadian-ashley-macisaac-fiddler-musician-singer-songwriter-sues-google-ai-sex-offender-ntwnfb)

生成摘要时出错

---

## 66. IBM didn't want Microsoft to use the Tab key to move between dialog fields

**原文标题**: IBM didn't want Microsoft to use the Tab key to move between dialog fields

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20260505-00/?p=112298](https://devblogs.microsoft.com/oldnewthing/20260505-00/?p=112298)

生成摘要时出错

---

## 67. Researchers print structural colour with an inkjet printer

**原文标题**: Researchers print structural colour with an inkjet printer

**原文链接**: [https://physicsworld.com/a/researchers-print-structural-colour-with-an-inkjet-printer/](https://physicsworld.com/a/researchers-print-structural-colour-with-an-inkjet-printer/)

生成摘要时出错

---

## 68. Why most product tours get skipped

**原文标题**: Why most product tours get skipped

**原文链接**: [https://productonboarding.com/articles/why-product-tours-get-skipped](https://productonboarding.com/articles/why-product-tours-get-skipped)

生成摘要时出错

---

## 69. Atlassian HipChat (2017)

**原文标题**: Atlassian HipChat (2017)

**原文链接**: [https://web.archive.org/web/20170202090011/https://www.hipchat.com/](https://web.archive.org/web/20170202090011/https://www.hipchat.com/)

生成摘要时出错

---

## 70. Underwater robot tracks sperm whale conversations in real time

**原文标题**: Underwater robot tracks sperm whale conversations in real time

**原文链接**: [https://www.reuters.com/business/environment/underwater-robot-tracks-sperm-whale-conversations-real-time-2026-05-01/](https://www.reuters.com/business/environment/underwater-robot-tracks-sperm-whale-conversations-real-time-2026-05-01/)

生成摘要时出错

---

## 71. What Causes Lightning? The Answer Keeps Getting More Interesting

**原文标题**: What Causes Lightning? The Answer Keeps Getting More Interesting

**原文链接**: [https://www.quantamagazine.org/what-causes-lightning-the-answer-keeps-getting-more-interesting-20260506/](https://www.quantamagazine.org/what-causes-lightning-the-answer-keeps-getting-more-interesting-20260506/)

生成摘要时出错

---

## 72. I'm scared about biological computing

**原文标题**: I'm scared about biological computing

**原文链接**: [https://kuber.studio/blog/Reflections/I%27m-Scared-About-Biological-Computing](https://kuber.studio/blog/Reflections/I%27m-Scared-About-Biological-Computing)

生成摘要时出错

---

## 73. Feds Fine Durham Energy Efficiency Co $722M

**原文标题**: Feds Fine Durham Energy Efficiency Co $722M

**原文链接**: [https://www.theassemblync.com/news/business/american-efficient-ferc-durham-fine/](https://www.theassemblync.com/news/business/american-efficient-ferc-durham-fine/)

生成摘要时出错

---

## 74. When everyone has AI and the company still learns nothing

**原文标题**: When everyone has AI and the company still learns nothing

**原文链接**: [https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/](https://www.robert-glaser.de/when-everyone-has-ai-and-the-company-still-learns-nothing/)

生成摘要时出错

---

## 75. Should I run plain Docker Compose in production in 2026?

**原文标题**: Should I run plain Docker Compose in production in 2026?

**原文链接**: [https://distr.sh/blog/running-docker-in-production/](https://distr.sh/blog/running-docker-in-production/)

生成摘要时出错

---

## 76. Talking to strangers at the gym

**原文标题**: Talking to strangers at the gym

**原文链接**: [https://thienantran.com/talking-to-35-strangers-at-the-gym/](https://thienantran.com/talking-to-35-strangers-at-the-gym/)

生成摘要时出错

---

## 77. Show HN: NFC tags are good material for pranks on Android

**原文标题**: Show HN: NFC tags are good material for pranks on Android

**原文链接**: [https://mastodon.social/@maxwellito/116524250100439866](https://mastodon.social/@maxwellito/116524250100439866)

生成摘要时出错

---

## 78. Farewell to a Giant of Botany

**原文标题**: Farewell to a Giant of Botany

**原文链接**: [https://nautil.us/farewell-to-a-giant-of-botany-1280409](https://nautil.us/farewell-to-a-giant-of-botany-1280409)

生成摘要时出错

---

## 79. Israel's AI targeting system: How data from a phone become a death sentence

**原文标题**: Israel's AI targeting system: How data from a phone become a death sentence

**原文链接**: [https://www.latimes.com/world-nation/story/2026-05-04/inside-israels-ai-targeting-system-how-data-from-phone-become-death-sentence](https://www.latimes.com/world-nation/story/2026-05-04/inside-israels-ai-targeting-system-how-data-from-phone-become-death-sentence)

生成摘要时出错

---

## 80. CVE-2026-31431: Copy Fail vs. rootless containers

**原文标题**: CVE-2026-31431: Copy Fail vs. rootless containers

**原文链接**: [https://www.dragonsreach.it/2026/05/04/cve-2026-31431-copy-fail-rootless-containers/](https://www.dragonsreach.it/2026/05/04/cve-2026-31431-copy-fail-rootless-containers/)

生成摘要时出错

---

## 81. Agents for financial services and insurance

**原文标题**: Agents for financial services and insurance

**原文链接**: [https://www.anthropic.com/news/finance-agents](https://www.anthropic.com/news/finance-agents)

生成摘要时出错

---

## 82. While the King Lives: An Old C Programming Prank in GNU Hello from 1993

**原文标题**: While the King Lives: An Old C Programming Prank in GNU Hello from 1993

**原文链接**: [https://lowendbox.com/blog/while-the-king-lives-an-old-c-programming-prank-in-gnu-hello-from-1993/](https://lowendbox.com/blog/while-the-king-lives-an-old-c-programming-prank-in-gnu-hello-from-1993/)

生成摘要时出错

---

## 83. Detection of an atmosphere on a trans-Neptunian object beyond Pluto

**原文标题**: Detection of an atmosphere on a trans-Neptunian object beyond Pluto

**原文链接**: [https://www.nature.com/articles/s41550-026-02846-1](https://www.nature.com/articles/s41550-026-02846-1)

生成摘要时出错

---

## 84. Show HN: Hallucinopedia

**原文标题**: Show HN: Hallucinopedia

**原文链接**: [http://halupedia.com/](http://halupedia.com/)

生成摘要时出错

---

## 85. Async Rust never left the MVP state

**原文标题**: Async Rust never left the MVP state

**原文链接**: [https://tweedegolf.nl/en/blog/237/async-rust-never-left-the-mvp-state](https://tweedegolf.nl/en/blog/237/async-rust-never-left-the-mvp-state)

生成摘要时出错

---

## 86. Show HN: Explore color palettes inspired by 3000 master painter artworks

**原文标题**: Show HN: Explore color palettes inspired by 3000 master painter artworks

**原文链接**: [https://paletteinspiration.com/](https://paletteinspiration.com/)

生成摘要时出错

---

## 87. B.C. residents baffled as shape floats through night sky

**原文标题**: B.C. residents baffled as shape floats through night sky

**原文链接**: [https://www.cbc.ca/news/canada/british-columbia/strange-light-british-columbia-9.7189267](https://www.cbc.ca/news/canada/british-columbia/strange-light-british-columbia-9.7189267)

生成摘要时出错

---

## 88. Built a real-time bird tracking station to combat my burnout

**原文标题**: Built a real-time bird tracking station to combat my burnout

**原文链接**: [https://alec.is/birds/](https://alec.is/birds/)

生成摘要时出错

---

## 89. Built a real-time bird tracking station to combat my burnout

**原文标题**: Built a real-time bird tracking station to combat my burnout

**原文链接**: [https://alec.is/birds/](https://alec.is/birds/)

生成摘要时出错

---

## 90. How the heck do solar panels work?

**原文标题**: How the heck do solar panels work?

**原文链接**: [https://perthirtysix.com/how-the-heck-do-solar-panels-work](https://perthirtysix.com/how-the-heck-do-solar-panels-work)

生成摘要时出错

---

## 91. Google Tag Gateway – Ad-Block Killer?

**原文标题**: Google Tag Gateway – Ad-Block Killer?

**原文链接**: [https://developers.google.com/tag-platform/tag-manager/gateway](https://developers.google.com/tag-platform/tag-manager/gateway)

生成摘要时出错

---

## 92. The extended predicative Mahlo universe in Martin-Löf type theory (2023)

**原文标题**: The extended predicative Mahlo universe in Martin-Löf type theory (2023)

**原文链接**: [https://academic.oup.com/logcom/article/34/6/1032/7158523](https://academic.oup.com/logcom/article/34/6/1032/7158523)

生成摘要时出错

---

## 93. Docker 29 has changed its default image store for new installs

**原文标题**: Docker 29 has changed its default image store for new installs

**原文链接**: [https://docs.docker.com/engine/storage/containerd](https://docs.docker.com/engine/storage/containerd)

生成摘要时出错

---

## 94. GLM-5V-Turbo: Toward a Native Foundation Model for Multimodal Agents

**原文标题**: GLM-5V-Turbo: Toward a Native Foundation Model for Multimodal Agents

**原文链接**: [https://arxiv.org/abs/2604.26752](https://arxiv.org/abs/2604.26752)

生成摘要时出错

---

## 95. Show HN: Guten – Android ereader for Project Gutenberg's 70k+ free books

**原文标题**: Show HN: Guten – Android ereader for Project Gutenberg's 70k+ free books

**原文链接**: [https://play.google.com/store/apps/details?id=com.bhunt.guten&hl=en_US](https://play.google.com/store/apps/details?id=com.bhunt.guten&hl=en_US)

生成摘要时出错

---

## 96. Urban Birds Are Rising Earlier Because of Traffic Noise (2013)

**原文标题**: Urban Birds Are Rising Earlier Because of Traffic Noise (2013)

**原文链接**: [https://www.audubon.org/news/urban-birds-are-rising-earlier-because-traffic-noise](https://www.audubon.org/news/urban-birds-are-rising-earlier-because-traffic-noise)

生成摘要时出错

---

## 97. PyInfra 3.8.0

**原文标题**: PyInfra 3.8.0

**原文链接**: [https://github.com/pyinfra-dev/pyinfra/releases/tag/v3.8.0](https://github.com/pyinfra-dev/pyinfra/releases/tag/v3.8.0)

生成摘要时出错

---

## 98. GameStop makes $55.5B takeover offer for eBay

**原文标题**: GameStop makes $55.5B takeover offer for eBay

**原文链接**: [https://www.bbc.co.uk/news/articles/cn0p8yled1do](https://www.bbc.co.uk/news/articles/cn0p8yled1do)

生成摘要时出错

---

## 99. Empty Screenings – Finds AMC movie screenings with few or no tickets sold

**原文标题**: Empty Screenings – Finds AMC movie screenings with few or no tickets sold

**原文链接**: [https://walzr.com/empty-screenings](https://walzr.com/empty-screenings)

生成摘要时出错

---

## 100. How OpenAI delivers low-latency voice AI at scale

**原文标题**: How OpenAI delivers low-latency voice AI at scale

**原文链接**: [https://openai.com/index/delivering-low-latency-voice-ai-at-scale/](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/)

生成摘要时出错

---

