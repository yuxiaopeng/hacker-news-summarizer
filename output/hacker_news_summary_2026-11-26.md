# Hacker News 热门文章摘要 (2026-11-26)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 1Password 安全事件

**原文标题**: 1Password Security Incident

**原文链接**: [https://1password.com/blog/update-on-nov-2026-security-incident](https://1password.com/blog/update-on-nov-2026-security-incident)

**1Password 安全事件摘要 (2026年11月)**

2026年11月19日，1Password 检测到一起安全漏洞，其源头是攻击者非法获取了一名员工的公司 GitHub 账户。攻击者利用该访问权限复制了源代码，并在后端服务中部署了恶意代码，从而得以下载管理元数据。

**受影响范围：**
攻击者访问了部分用户的账户记录，包括姓名、电子邮件地址、账户标识符和登录时间戳。同时泄露的还包括公钥、安全远程密码 (SRP) 参数，以及用于邀请和账户恢复邮件的令牌。此外，攻击者还获得了 1Password CI/CD 系统和基础设施相关机密的访问权限。

**仍保持安全的内容：**
至关重要的是，**客户保险库内容从未被访问或泄露。** 得益于 1Password 的零知识架构，解密保险库所需的密钥仅由用户持有。账户密码、秘密密钥 (Secret Keys) 和恢复密钥保持完全安全，且从未存储在受攻击的系统中。

**已采取的措施：**
1Password 立即停用了受影响的 GitHub 账户，并撤销了所有受损令牌和内部凭证。为了防止针对恢复尝试的暴力破解攻击，他们将邀请码和恢复码从 6 位数字延长至 10 位字母数字字符。公司还加强了内部安全控制，增加了新的检测层，并聘请了独立网络安全专家来验证其修复工作的有效性。

**用户建议：**
虽然服务未受影响，但敦促用户对提及账户恢复或 1Password 邀请的钓鱼攻击保持警惕。公司提醒用户，官方绝不会通过电子邮件或短信索取秘密密钥或账户密码。任何可疑活动均应报告至 support@1password.com。

---

## 2. 卧槽卧槽卧槽卧槽：正在发生的一切影响竟如此之巨

**原文标题**: Holy shit holy shit holy shit holy shit: The magnitude of what’s now happening

**原文链接**: [https://scottaaronson.blog/?p=10379](https://scottaaronson.blog/?p=10379)

这篇写于 2026 年 11 月的博文描述了数学和理论计算机科学领域的“AI 奇点”。作者详细记录了一场“数学启示录”（Mathocalypse），来自 OpenAI、Anthropic 和 Google 的 AI 模型接连攻克了数个世界上最深奥的数学难题。

提到的关键突破包括：
*   **黎曼猜想：**由 Alpöge 和 Anthropic 证明。
*   **矩阵乘法：**指数 $\omega$ 被证明恰好为 $9/4$，为这一追溯至 20 世纪 60 年代的谜团提供了确切答案。
*   **复杂度理论：**证明了 $VP \neq VNP$ 和 $QIP(2) = PSPACE$，并提出了傅里叶变换的新匹配下界。
*   **算法进展：**一种确定性亚指数级整数分解算法，以及埃尔德什-拉多（Erdős–Rado）向日葵猜想的解决方案。

作者强调，科学方法论已经发生了根本性转变。AI 实验室现在绕过传统的同行评审，直接将经过 Lean 认证的证明上传至 GitHub。尽管有人将其斥为“证明废料”（proofslop），但作者认为，形式化验证使这些结果无可辩驳。他指出，发现的速度如此之快，以至于过去足以成就职业生涯的重大成果，如今已几乎算不上新闻。

全篇传达了一种知性冲击和存在感转型的意味。作者预测 $P \neq NP$ 的证明已近在咫尺，并暗示 AI 实验室可能正掌握着足以瓦解现代密码学的“重磅级”算法。最终，他将这一时刻定性为一场预言已久的启示，建议读者在世界进入 AI 驱动的新“数学真理大陆”之际，珍惜人类的情感联结。

---

## 3. Anthropic 发布的 GRH Lean 验证大幅简化版

**原文标题**: Much shorter version of GRH Lean verification from Anthropic

**原文链接**: [https://github.com/lsernau/grh-lean](https://github.com/lsernau/grh-lean)

Anthropic 发布了一项研究成果，利用 Lean 4 实现了对黎曼猜想 (RH) 以及狄利克雷 L 函数的广义黎曼猜想 (GRH) 的形式化验证。该项目是与 AI 模型 Claude 合作开发，并基于 Levent Alpöge 的研究工作，其篇幅较以往的形式化尝试有了显著缩减。

该代码仓库包含两个版本的证明：一个是约 30 万行的“可读版”，另一个是缩减至约 7.6 万行的“精简版”。这些证明构建于 Mathlib 之上，并严格依赖于 Lean 的标准公理（`propext`、`Classical.choice` 和 `Quot.sound`）。

**关键详情包括：**
*   **验证状态：** 证明已通过机器检查，但尚未经过数学家的同行评审，目前也没有配套的正式论文。
*   **技术

此次发布凸显了 AI 在辅助复杂数学形式化验证中日益增长的作用。

---

## 4. The New York Times warns photographers not to update Photoshop over AI features

**原文标题**: The New York Times warns photographers not to update Photoshop over AI features

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features](https://www.theverge.com/ai-artificial-intelligence/1041227/the-new-york-times-warns-photographers-not-to-update-photoshop-over-ai-features)

*The New York Times* has instructed freelance photographers to avoid updating to Adobe Photoshop 2027 (version 28.0.0) due to concerns regarding its new AI-powered features. In an internal email, photography leaders Meaghan Looram and Josh Haner warned that the update integrates AI in "ways that may not be apparent to users," potentially resulting in metadata that identifies photographs as AI-generated.

The primary concern involves Adobe’s implementation of C2PA metadata, which automatically tags images that have been created or edited using AI. The 2027 update includes several "agentic" AI tools, such as an AI Assisted Editor, prompt-based image transformation, and AI-powered upscaling. Because it is not always clear which specific tools trigger these metadata tags—and because even traditional selection tools are becoming AI-integrated—the *Times* worries that these tags could inadvertently appear in their published photos.

For the *Times*, which maintains a strict policy of minimal photo manipulation to ensure journalistic accuracy and reader trust, these AI-identifying tags pose a significant reputational risk. The newsroom generally limits edits to minor color adjustments and prohibits digital retouching. By barring the latest Photoshop update, the *Times* aims to prevent misleading metadata from suggesting their photography is anything other than authentic, minimally processed documentation.

A spokesperson for the *New York Times* confirmed the new requirement, emphasizing the organization's commitment to maintaining its standards as Adobe continues to integrate generative AI across its creative suite.

---

## 5. GPT-6.2 Astra 是首个打破 Google 员工代码高尔夫纪录的模型。

**原文标题**: GPT-6.2 Astra is the first model to beat Googlers' code golf records

**原文链接**: [https://bjin.github.io/go-codegolf-benchmark/#leaderboard](https://bjin.github.io/go-codegolf-benchmark/#leaderboard)

生成摘要时出错

---

## 6. Ubuntu 安全响应时间缓慢

**原文标题**: Slow Ubuntu security response times

**原文链接**: [https://www.openwall.com/lists/oss-security/2026/11/25/9](https://www.openwall.com/lists/oss-security/2026/11/25/9)

在 *oss-security* 邮件列表的一篇帖子中，独立安全研究员 Hanno Böck 批评 Ubuntu 在应对严重安全漏洞时的响应速度显著延迟。

Böck 重点列举了 Ubuntu 落后于其他 Linux 发行版的几个严重缺陷：
*   **CVE-2026-99288 (NoisyTCP)：** TCP 协议栈中的一个远程内存损坏漏洞。虽然其他发行版在 11 月 16 日漏洞公布时就已准备好修复程序，但 Ubuntu 在九天后仍未修复。
*   **CVE-2026-99312：** 一个影响 AMD 虚拟化的 KVM 主机逃逸漏洞，同样缺乏及时的修复。
*   **CVE-2026-98432：** 另一个远程 TCP 损坏漏洞，据报道耗时数周才完成修复，且已发现与现有的在野利用相关联。

Böck 认为，对于远程内核损坏漏洞，安全更新应在数小时内而非数周内发布。他将这些延迟归因于 Ubuntu 的技术策略，即坚持将补丁反向移植（backporting）到较旧版本的内核，而不是使用最新的上游长期支持（LTS）内核。

通过将 Ubuntu 与使用更新上游 LTS 版本的 Debian 进行对比，Böck 指出 Ubuntu 的反向移植模式已日益不可持续。他总结道，为了确保更高效的安全维护，所有发行版理想情况下都应将其内核基于 Linux 内核主线开发人员支持的版本。

---

## 7. 想问问那个在 Home Depot 蓄水池里浮潜的老兄几个问题

**原文标题**: A few questions for the guy who went snorkeling in a Home Depot retention pond

**原文链接**: [https://www.vox.com/down-to-earth/511999/home-depot-retention-pond-snorkel-joseph-ricketts](https://www.vox.com/down-to-earth/511999/home-depot-retention-pond-snorkel-joseph-ricketts)

在这次采访中，现居佛罗里达州的生物学家兼 YouTuber 约瑟夫·里基茨 (Joseph Ricketts) 讨论了他那段记录在 Home Depot 蓄水池进行夜间浮潜的走红视频。虽然从表面上看，这个池塘只是一个充斥着城市垃圾的死水潭，但里基茨在水下发现了一个繁荣的生态系统，其中包括水蛇、发育中的“幼蛙”以及稀有的蝌蚪虾（鲎虫）。

本文强调了关于城市生态与保护的几个关键主题：

*   **蓄水池的角色：** 在佛罗里达州这样开发密集的地区，这些人工池塘充当了自然湿地的重要替代品，通过吸收雨水来防止洪涝。然而，里基茨强调，虽然它们支持部分生命，但并不能取代那些需要保护的广阔、未受破坏的原始生态系统。
*   **自然荒漠：** 里基茨提出了“自然荒漠”的概念，指出对于城市地区的许多人来说，这些小型人工池塘可能是他们唯一能接触到自然界的途径。他认为这些空间值得保留，以确保每个人都有机会体验荒野。
*   **重新定义美丽：** 该项目旨在挑战人们在意想不到的地方寻找美。里基茨希望培养人们对蛇类和无脊椎动物等不那么“迷人”的物种的好奇心，并反思为何社会已经对日常环境中的水质污染习以为常。

虽然这次“行为艺术”旨在引发思考并凸显大自然的韧性，但里基茨建议他人不要在蓄水池中浮潜，因为存在潜在的污染风险。最终，他旨在利用自己的平台缩小城市生活与隐藏的自然世界之间的鸿沟，倡导保护当地的城市生态角落以及大规模的栖息地。

---

## 8. Nfs2root：Linux 内核 NFS 服务器中一个存在 12 年之久的预认证远程 Root 漏洞

**原文标题**: Nfs2root: A 12-year-old pre-auth remote root in the Linux kernel's NFS server

**原文链接**: [https://opensec.in/blog/nfs2root-cve-2026-99362](https://opensec.in/blog/nfs2root-cve-2026-99362)

**CVE-2026-99362**，被称为 **“Nfs2root”**，是 Linux 内核 NFS 服务器 (`nfsd`) 中的一个严重的预身份验证堆溢出漏洞。该漏洞的 CVSS 评分为 9.8，已存在 12 年之久，自 Linux 3.16 版本以来一直影响相关系统。任何在可访问的 TCP 2049 端口上提供 NFSv4.1 或 4.2 服务的 Linux 主机都会受到影响。

**技术机制**
该漏洞存在于 `nfsd` 处理 NFSv4.1 会话回复缓存的方式中。未经身份验证的客户端可以将其会话的回复缓存缩小到零字节。当服务器处理后续请求时，它会尝试将回复内容复制到这个长度为零的缓冲区中，从而导致内核堆的越界写入。研究人员证明，可以利用该溢出漏洞链式泄露 KASLR 偏移量并操纵内核对象，最终允许攻击者以 root 权限执行任意命令。

**发现与影响**
该漏洞由 ANSSI 的 Jérémy Jean 和 OpenSec 的自动化平台 “Antara” 独立发现。后者在无需人工干预的情况下成功生成了功能完整的远程 root 利用程序。由于该漏洞发生在身份验证之前且涉及标准 NFS 流量，因此很难通过传统的网络特征码进行检测。

**修复与缓解**
*   **补丁：** 用户应立即更新到已修复的内核版本，包括 **6.12.117、6.18.61、7.3.2 或 7.4-rc1**，或应用相关的发行版后向移植补丁。
*   **临时解决方案：** 如果无法打补丁，管理员应：
    1.  配置防火墙限制 TCP 2049 端口，仅允许受信网络访问。
    2.  在 `/etc/nfs.conf` 中禁用 NFSv4.1 和 4.2 并重启服务。
*   **监控：** 安全团队应留意来自 `nfsd4_check_resp_size` 的内核警告或源自内核工作线程的可疑 shell 活动。

---

## 9. 裸金属 Qwen

**原文标题**: Bare Metal Qwen

**原文链接**: [https://github.com/alesha-pro/llm.asm/tree/main/02-baremetal-os](https://github.com/alesha-pro/llm.asm/tree/main/02-baremetal-os)

生成摘要时出错

---

## 10. SSH is a GUI framework

**原文标题**: SSH is a GUI framework

**原文链接**: [https://zydra.sh/articles/ssh-is-a-gui-framework/](https://zydra.sh/articles/ssh-is-a-gui-framework/)

生成摘要时出错

---

## 11. Jev is probably Qwen3.5-35B-A3B

**原文标题**: Jev is probably Qwen3.5-35B-A3B

**原文链接**: [https://modaic.dev/blog/latency-doesnt-lie](https://modaic.dev/blog/latency-doesnt-lie)

生成摘要时出错

---

## 12. Deploying a payphone on a tiny Pacific Island for fun and zero profit

**原文标题**: Deploying a payphone on a tiny Pacific Island for fun and zero profit

**原文链接**: [https://nickvsnetworking.com/deploying-a-payphone-on-a-tiny-pacific-island-for-fun-and-zero-profit/](https://nickvsnetworking.com/deploying-a-payphone-on-a-tiny-pacific-island-for-fun-and-zero-profit/)

生成摘要时出错

---

## 13. The polynomial Hirsch conjecture is false [pdf]

**原文标题**: The polynomial Hirsch conjecture is false [pdf]

**原文链接**: [https://github.com/openai/math/blob/main/preprints/Superpolynomial-graph-diameter-of-simple-polytopes-November-24-2026/paper.pdf](https://github.com/openai/math/blob/main/preprints/Superpolynomial-graph-diameter-of-simple-polytopes-November-24-2026/paper.pdf)

生成摘要时出错

---

## 14. Multiagent coding is the future

**原文标题**: Multiagent coding is the future

**原文链接**: [https://www.kalzumeus.com/2026/11/25/multiagent-coding-is-the-future/](https://www.kalzumeus.com/2026/11/25/multiagent-coding-is-the-future/)

生成摘要时出错

---

## 15. Google releases Cogentic papers on integer factorization, discrete logs and more

**原文标题**: Google releases Cogentic papers on integer factorization, discrete logs and more

**原文链接**: [https://github.com/google-research/google-research/tree/master/cogentic_research_papers](https://github.com/google-research/google-research/tree/master/cogentic_research_papers)

生成摘要时出错

---

## 16. Defang Security Incident

**原文标题**: Defang Security Incident

**原文链接**: [https://defang.io/blog/post/security-incident-november-2026/](https://defang.io/blog/post/security-incident-november-2026/)

On November 12, 2026, Defang experienced a security breach where an attacker compromised its build system and downloaded the main production database. The incident, confirmed on November 23, occurred because a development GitHub App with excessive permissions allowed an attacker to execute malicious code in the production CI environment and extract credentials.

**What was exposed:**
*   **User Information:** Names, email addresses, and GitHub/GitLab usernames.
*   **Project Data:** Repository names, cloud account IDs/regions, and Compose files.
*   **Sensitive Credentials:** Deployment states from October 12 to November 19 were compromised, potentially exposing database passwords and environment variables.
*   **GitHub Access:** For users of the Defang GitHub App, the attacker briefly held the ability to push commits, modify workflows, and change repository settings.
*   **Billing:** Stripe data, including billing addresses and the last four digits of credit cards, was accessed; however, full card numbers were not exposed.

**What was not exposed:** 
Defang does not store user passwords, cloud credentials, or repository contents, so these remained secure.

**Actions taken and required:**
Defang has replaced all production credentials, revoked GitHub tokens, and invalidated active sessions. Affected users should:
1.  **Audit GitHub activity:** Check for unauthorized commits, workflow changes, or new collaborators since November 11.
2.  **Lock down environments:** Restrict deployment environment rules in GitHub to specific branches.
3.  **Rotate secrets:** Change any database passwords or environment variables used between October 12 and November 19.
4.  **Re-authenticate:** Revoke and reconnect Defang’s access in GitHub settings.
5.  **Exercise caution:** Be alert for sophisticated phishing attempts using your name or repository details. 

Users can contact `sec@defang.io` for assistance with auditing their accounts.

---

## 17. Windows Loudness Equalization, reverse-engineered and ported to PipeWire

**原文标题**: Windows Loudness Equalization, reverse-engineered and ported to PipeWire

**原文链接**: [https://github.com/xoxorwr/pw-loudness-eq](https://github.com/xoxorwr/pw-loudness-eq)

生成摘要时出错

---

## 18. Britain's ghost stations

**原文标题**: Britain's ghost stations

**原文链接**: [https://spectator.com/article/britains-ghost-stations-are-fascinating/](https://spectator.com/article/britains-ghost-stations-are-fascinating/)

生成摘要时出错

---

## 19. I checked Clojure's core with Lean and found unreported bugs

**原文标题**: I checked Clojure's core with Lean and found unreported bugs

**原文链接**: [https://s.conao3.com/blog/2026/e4f733](https://s.conao3.com/blog/2026/e4f733)

生成摘要时出错

---

## 20. Porting Rockbox to an undocumented $9 AliExpress 'YP3' MP3 player with LLMs

**原文标题**: Porting Rockbox to an undocumented $9 AliExpress 'YP3' MP3 player with LLMs

**原文链接**: [https://jayd.ml/2026/11/14/rockbox-on-yp3.html](https://jayd.ml/2026/11/14/rockbox-on-yp3.html)

生成摘要时出错

---

## 21. The trouble with serendipity: Scientific discoveries don't happen how you think

**原文标题**: The trouble with serendipity: Scientific discoveries don't happen how you think

**原文链接**: [https://www.worksinprogress.news/p/the-trouble-with-serendipity](https://www.worksinprogress.news/p/the-trouble-with-serendipity)

生成摘要时出错

---

## 22. The undocumented 249-file limit for Googlebot rendering

**原文标题**: The undocumented 249-file limit for Googlebot rendering

**原文链接**: [https://www.fullstackoptimization.com/a/googlebot-249-file-rendering-limit](https://www.fullstackoptimization.com/a/googlebot-249-file-rendering-limit)

生成摘要时出错

---

## 23. Predicting LoRA size for any dataset

**原文标题**: Predicting LoRA size for any dataset

**原文链接**: [https://engram.com/blog/lora-size](https://engram.com/blog/lora-size)

生成摘要时出错

---

## 24. Show HN: Rchive – Every drive I've owned since the 90s, searchable in one window

**原文标题**: Show HN: Rchive – Every drive I've owned since the 90s, searchable in one window

**原文链接**: [https://www.rchive.computer/](https://www.rchive.computer/)

生成摘要时出错

---

## 25. Show HN: An agent skill that optimizes code with falsifiable hypotheses

**原文标题**: Show HN: An agent skill that optimizes code with falsifiable hypotheses

**原文链接**: [https://chszlab.github.io/AgenticAlgorithmEngineering/](https://chszlab.github.io/AgenticAlgorithmEngineering/)

生成摘要时出错

---

## 26. 72-hour fasting can reset your immune system, USC study shows

**原文标题**: 72-hour fasting can reset your immune system, USC study shows

**原文链接**: [https://scienceinhand.com/72-hour-fasting-can-reset-your-entire-immune-system-usc-study-shows/](https://scienceinhand.com/72-hour-fasting-can-reset-your-entire-immune-system-usc-study-shows/)

生成摘要时出错

---

## 27. Why "all different" Sets take 5x longer to find

**原文标题**: Why "all different" Sets take 5x longer to find

**原文链接**: [https://setdaily.app/blog/spotting-sets](https://setdaily.app/blog/spotting-sets)

生成摘要时出错

---

## 28. Smart people who give a shit use tools

**原文标题**: Smart people who give a shit use tools

**原文链接**: [https://www.iankduncan.com/engineering/2026-11-19-smart-people-who-give-a-shit-use-tools](https://www.iankduncan.com/engineering/2026-11-19-smart-people-who-give-a-shit-use-tools)

生成摘要时出错

---

## 29. A fast CAS with a focus on resolution of singularities

**原文标题**: A fast CAS with a focus on resolution of singularities

**原文链接**: [https://github.com/pportilla/atlas](https://github.com/pportilla/atlas)

生成摘要时出错

---

## 30. Hazel (YC W24) Is Hiring a Product Designer

**原文标题**: Hazel (YC W24) Is Hiring a Product Designer

**原文链接**: [https://www.ycombinator.com/companies/hazel-2/jobs/8EhsvYE-product-designer-contract](https://www.ycombinator.com/companies/hazel-2/jobs/8EhsvYE-product-designer-contract)

生成摘要时出错

---

## 31. In C++, = default and {} are not the same constructor

**原文标题**: In C++, = default and {} are not the same constructor

**原文链接**: [https://lemire.me/blog/2026/11/02/default-and-braces-are-not-the-same-constructor/](https://lemire.me/blog/2026/11/02/default-and-braces-are-not-the-same-constructor/)

生成摘要时出错

---

## 32. Show HN: Old Nvidia and ATI tech demos, running again in the browser

**原文标题**: Show HN: Old Nvidia and ATI tech demos, running again in the browser

**原文链接**: [https://gpu-demo-gallery.pages.dev/](https://gpu-demo-gallery.pages.dev/)

生成摘要时出错

---

## 33. A Beer Brewer's Noise Estimation

**原文标题**: A Beer Brewer's Noise Estimation

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/a-beer-brewers-noise-estimation](https://chillphysicsenjoyer.substack.com/p/a-beer-brewers-noise-estimation)

生成摘要时出错

---

## 34. Pinocchio at 200: a tale of hunger, greed and Italy's culinary history

**原文标题**: Pinocchio at 200: a tale of hunger, greed and Italy's culinary history

**原文链接**: [https://www.repubblica.it/en/europe/food-travel/2026/11/24/news/carlo_collodi_pinocchio_pellegrino_artusi_italian_literature-425744069/](https://www.repubblica.it/en/europe/food-travel/2026/11/24/news/carlo_collodi_pinocchio_pellegrino_artusi_italian_literature-425744069/)

生成摘要时出错

---

## 35. Bypassing iOS Safari's 60 FPS Limit to Build Web Applications That Feel Native

**原文标题**: Bypassing iOS Safari's 60 FPS Limit to Build Web Applications That Feel Native

**原文链接**: [https://rida.dev/blog/bypassing-ios-safari-60-fps-limit](https://rida.dev/blog/bypassing-ios-safari-60-fps-limit)

生成摘要时出错

---

## 36. The matrix multiplication exponent is nine fourths [pdf]

**原文标题**: The matrix multiplication exponent is nine fourths [pdf]

**原文链接**: [https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf](https://github.com/openai/math/blob/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026/paper.pdf)

生成摘要时出错

---

## 37. Rumors swirling that labs might have cracked Factoring in P

**原文标题**: Rumors swirling that labs might have cracked Factoring in P

**原文链接**: [https://www.reddit.com/r/singularity/comments/1y59ef1/rumor_that_openai_or_anthropic_found_a_way_to/](https://www.reddit.com/r/singularity/comments/1y59ef1/rumor_that_openai_or_anthropic_found_a_way_to/)

生成摘要时出错

---

## 38. The industrialization of noise: Automated proof-solving is the same old dead end [pdf]

**原文标题**: The industrialization of noise: Automated proof-solving is the same old dead end [pdf]

**原文链接**: [https://arxiv.org/abs/2611.31286](https://arxiv.org/abs/2611.31286)

生成摘要时出错

---

## 39. Button Sounds – collection of professionally-recorded button clicks and presses

**原文标题**: Button Sounds – collection of professionally-recorded button clicks and presses

**原文链接**: [https://buttons.joshwcomeau.com/](https://buttons.joshwcomeau.com/)

生成摘要时出错

---

## 40. PenGPT: A Generative Transformer for Handwriting and Sketches

**原文标题**: PenGPT: A Generative Transformer for Handwriting and Sketches

**原文链接**: [https://greydanus.github.io/2026/11/12/pengpt/](https://greydanus.github.io/2026/11/12/pengpt/)

生成摘要时出错

---

## 41. Macrohistory in Six Facts

**原文标题**: Macrohistory in Six Facts

**原文链接**: [https://basilhalperin.com/essays/macrohistory.html](https://basilhalperin.com/essays/macrohistory.html)

生成摘要时出错

---

## 42. Investigating degraded experiences across GitHub products

**原文标题**: Investigating degraded experiences across GitHub products

**原文链接**: [https://www.githubstatus.com/incidents/qn8mfv6q5hlx](https://www.githubstatus.com/incidents/qn8mfv6q5hlx)

生成摘要时出错

---

## 43. Taking over US Treasury subdomains for $3 each

**原文标题**: Taking over US Treasury subdomains for $3 each

**原文链接**: [https://www.intruder.io/research/taking-over-us-treasury-subdomains-for-3-each](https://www.intruder.io/research/taking-over-us-treasury-subdomains-for-3-each)

生成摘要时出错

---

## 44. Getting old Java phones online again

**原文标题**: Getting old Java phones online again

**原文链接**: [https://antcating.github.io/2026/11/23/getting-old-java-phones-online-again.html](https://antcating.github.io/2026/11/23/getting-old-java-phones-online-again.html)

生成摘要时出错

---

## 45. The short age of dragon riders

**原文标题**: The short age of dragon riders

**原文链接**: [https://atilloy.com/2026/11/16/the-short-age-of-dragon-riders/](https://atilloy.com/2026/11/16/the-short-age-of-dragon-riders/)

生成摘要时出错

---

## 46. Is your DNS ready for a bigger namespace?

**原文标题**: Is your DNS ready for a bigger namespace?

**原文链接**: [https://www.akamai.com/blog/security/2026/nov/1615-new-tlds-dns-ready-for-bigger-namespace](https://www.akamai.com/blog/security/2026/nov/1615-new-tlds-dns-ready-for-bigger-namespace)

生成摘要时出错

---

## 47. When the Air Force Needed a Supercomputer, They Built It Out of PS3 Consoles

**原文标题**: When the Air Force Needed a Supercomputer, They Built It Out of PS3 Consoles

**原文链接**: [https://www.warhistoryonline.com/war-articles/ps3-supercomputer.html](https://www.warhistoryonline.com/war-articles/ps3-supercomputer.html)

生成摘要时出错

---

## 48. How did pinwheel calculators work?

**原文标题**: How did pinwheel calculators work?

**原文链接**: [https://blog.coredump.cx/p/how-did-pinwheel-calculators-work](https://blog.coredump.cx/p/how-did-pinwheel-calculators-work)

生成摘要时出错

---

## 49. GPT-6 models demonstrate intrinsic protein-design capabilities

**原文标题**: GPT-6 models demonstrate intrinsic protein-design capabilities

**原文链接**: [https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/](https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities/)

生成摘要时出错

---

## 50. Migrating Our Messages API to Rust

**原文标题**: Migrating Our Messages API to Rust

**原文链接**: [https://www.anthropic.com/research/migrating-api-to-rust](https://www.anthropic.com/research/migrating-api-to-rust)

生成摘要时出错

---

## 51. Show HN: Turned a $5 AliExpress clock into a desk Clawd pet(+usage)

**原文标题**: Show HN: Turned a $5 AliExpress clock into a desk Clawd pet(+usage)

**原文链接**: [https://github.com/click6067-ship-it/token-tv](https://github.com/click6067-ship-it/token-tv)

生成摘要时出错

---

## 52. Duran Duran guitarist Andy Taylor dies aged 65

**原文标题**: Duran Duran guitarist Andy Taylor dies aged 65

**原文链接**: [https://www.bbc.co.uk/news/articles/cmp3vk6vr44po](https://www.bbc.co.uk/news/articles/cmp3vk6vr44po)

生成摘要时出错

---

## 53. Marginalia Search, Money, C++, Rust, AI, Stuff

**原文标题**: Marginalia Search, Money, C++, Rust, AI, Stuff

**原文链接**: [https://www.marginalia.nu/log/a_141_marginalia_update/](https://www.marginalia.nu/log/a_141_marginalia_update/)

生成摘要时出错

---

## 54. The USAID Files

**原文标题**: The USAID Files

**原文链接**: [https://reclaimthenet.org/usaid-files](https://reclaimthenet.org/usaid-files)

生成摘要时出错

---

## 55. The Shapes of Rivers

**原文标题**: The Shapes of Rivers

**原文链接**: [https://dominicroye.github.io/shapes-of-rivers/](https://dominicroye.github.io/shapes-of-rivers/)

生成摘要时出错

---

## 56. Macy's Thanksgiving Day Parade Postponed Until Saturday

**原文标题**: Macy's Thanksgiving Day Parade Postponed Until Saturday

**原文链接**: [https://www.nytimes.com/live/2026/11/25/nyregion/macys-thanksgiving-parade-postponed](https://www.nytimes.com/live/2026/11/25/nyregion/macys-thanksgiving-parade-postponed)

生成摘要时出错

---

## 57. Models Can Communicate via Inference Servers Despite Being Sandboxed

**原文标题**: Models Can Communicate via Inference Servers Despite Being Sandboxed

**原文链接**: [https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being](https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being)

生成摘要时出错

---

## 58. When in Doubt, Flail About

**原文标题**: When in Doubt, Flail About

**原文链接**: [https://www.seangoedecke.com/when-in-doubt-flail-about/](https://www.seangoedecke.com/when-in-doubt-flail-about/)

生成摘要时出错

---

## 59. GTA 6 Running on Windows

**原文标题**: GTA 6 Running on Windows

**原文链接**: [https://twitter.com/raul_bs3/status/2125213756238291075](https://twitter.com/raul_bs3/status/2125213756238291075)

生成摘要时出错

---

## 60. What does a software factory cost?

**原文标题**: What does a software factory cost?

**原文链接**: [https://zarar.dev/software-factory/](https://zarar.dev/software-factory/)

生成摘要时出错

---

## 61. The algebra of dependent types (2025)

**原文标题**: The algebra of dependent types (2025)

**原文链接**: [https://dotat.at/@/2025-05-28-types.html](https://dotat.at/@/2025-05-28-types.html)

生成摘要时出错

---

## 62. Top open problems in mathematics ranked by LLM-assessed importance

**原文标题**: Top open problems in mathematics ranked by LLM-assessed importance

**原文链接**: [https://www.proofatlas.ai/open-problems/](https://www.proofatlas.ai/open-problems/)

生成摘要时出错

---

## 63. Nvidia Reinstates Jensen Huang as CEO

**原文标题**: Nvidia Reinstates Jensen Huang as CEO

**原文链接**: [https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html](https://www.cnbc.com/2026/11/23/nvidia-jensen-huang-ceo.html)

生成摘要时出错

---

## 64. Serving Qwen via AWS Lambdas for fun and 80x negative profit

**原文标题**: Serving Qwen via AWS Lambdas for fun and 80x negative profit

**原文链接**: [https://noahbuilt.it/writing/qwen-on-5600-lambdas](https://noahbuilt.it/writing/qwen-on-5600-lambdas)

生成摘要时出错

---

## 65. Deriving Black-Scholes

**原文标题**: Deriving Black-Scholes

**原文链接**: [https://david.alvarezrosa.com/posts/deriving-black-scholes/](https://david.alvarezrosa.com/posts/deriving-black-scholes/)

生成摘要时出错

---

## 66. Ternary Bonsai 2.5 27B

**原文标题**: Ternary Bonsai 2.5 27B

**原文链接**: [https://prismml.com/news/bonsai-2-5-27b](https://prismml.com/news/bonsai-2-5-27b)

生成摘要时出错

---

## 67. Show HN: Ribbon Architect – Endless ways to tie a gift ribbon

**原文标题**: Show HN: Ribbon Architect – Endless ways to tie a gift ribbon

**原文链接**: [https://ribbonarchitect.com](https://ribbonarchitect.com)

生成摘要时出错

---

## 68. An Italian folding bicycle design that fits into a suitcase

**原文标题**: An Italian folding bicycle design that fits into a suitcase

**原文链接**: [https://www.core77.com/posts/145766/An-Italian-Folding-Bicycle-Design-that-Fits-Into-a-Suitcase](https://www.core77.com/posts/145766/An-Italian-Folding-Bicycle-Design-that-Fits-Into-a-Suitcase)

生成摘要时出错

---

## 69. Remote software jobs that show which countries can apply

**原文标题**: Remote software jobs that show which countries can apply

**原文链接**: [https://jobs.codemind.site/remote-jobs](https://jobs.codemind.site/remote-jobs)

生成摘要时出错

---

## 70. Lua for data representation (2025)

**原文标题**: Lua for data representation (2025)

**原文链接**: [https://citrons.xyz/journal/2025-07-23](https://citrons.xyz/journal/2025-07-23)

生成摘要时出错

---

## 71. Show HN: Cerulion – Harness for Robotics, Gemini 3.8 Flash Matches GPT-6 Astra

**原文标题**: Show HN: Cerulion – Harness for Robotics, Gemini 3.8 Flash Matches GPT-6 Astra

**原文链接**: [https://github.com/cerulion-inc/cerulion#harness-results](https://github.com/cerulion-inc/cerulion#harness-results)

生成摘要时出错

---

## 72. GTA 6 Recomp (Leonida) banned from GitHub while lead dev was in school

**原文标题**: GTA 6 Recomp (Leonida) banned from GitHub while lead dev was in school

**原文链接**: [https://github.com/ItsNotRexed/Leonida/issues](https://github.com/ItsNotRexed/Leonida/issues)

生成摘要时出错

---

## 73. Cento fine foods has been sued for “tomato fraud”

**原文标题**: Cento fine foods has been sued for “tomato fraud”

**原文链接**: [https://slate.com/life/2026/11/cento-san-marzano-tomato-sauce-recipes-lawsuit.html](https://slate.com/life/2026/11/cento-san-marzano-tomato-sauce-recipes-lawsuit.html)

生成摘要时出错

---

## 74. A training engine for your local model, using your idle compute

**原文标题**: A training engine for your local model, using your idle compute

**原文链接**: [https://github.com/sous-labs/songe](https://github.com/sous-labs/songe)

生成摘要时出错

---

## 75. Gödel Enigma

**原文标题**: Gödel Enigma

**原文链接**: [https://www.helsinki.fi/en/researchgroups/godel-enigma/research/project-description](https://www.helsinki.fi/en/researchgroups/godel-enigma/research/project-description)

生成摘要时出错

---

## 76. A Linux environment and Ghostty-based terminal for iOS

**原文标题**: A Linux environment and Ghostty-based terminal for iOS

**原文链接**: [https://github.com/swipt-automation/Swipterm](https://github.com/swipt-automation/Swipterm)

生成摘要时出错

---

## 77. New York bans AI toys, including those using internet to talk to children

**原文标题**: New York bans AI toys, including those using internet to talk to children

**原文链接**: [https://www.theguardian.com/us-news/2026/nov/25/new-york-bans-ai-toys](https://www.theguardian.com/us-news/2026/nov/25/new-york-bans-ai-toys)

生成摘要时出错

---

## 78. A Clock Made of Branches

**原文标题**: A Clock Made of Branches

**原文链接**: [https://fzakaria.com/2026/11/01/a-clock-made-of-branches](https://fzakaria.com/2026/11/01/a-clock-made-of-branches)

生成摘要时出错

---

## 79. Free alternative TV network built from the Internet Archive's forgotten videos

**原文标题**: Free alternative TV network built from the Internet Archive's forgotten videos

**原文链接**: [https://spelunkr.tv](https://spelunkr.tv)

生成摘要时出错

---

## 80. Jetty Pro

**原文标题**: Jetty Pro

**原文链接**: [http://hypercritical.co/2026/11/23/jetty-pro](http://hypercritical.co/2026/11/23/jetty-pro)

生成摘要时出错

---

## 81. Show HN: Rust agent with an Inkling 2 Mini inference engine for Apple Silicon

**原文标题**: Show HN: Rust agent with an Inkling 2 Mini inference engine for Apple Silicon

**原文链接**: [https://github.com/onatm/rustling](https://github.com/onatm/rustling)

生成摘要时出错

---

## 82. Ladybird is now in alpha

**原文标题**: Ladybird is now in alpha

**原文链接**: [https://ladybird.org/posts/alpha/](https://ladybird.org/posts/alpha/)

生成摘要时出错

---

## 83. A faster algorithm for extracting hexadecimal digits of π

**原文标题**: A faster algorithm for extracting hexadecimal digits of π

**原文链接**: [https://www.stylewarning.com/posts/faster-digit-extraction/](https://www.stylewarning.com/posts/faster-digit-extraction/)

生成摘要时出错

---

## 84. The Spray Bottle

**原文标题**: The Spray Bottle

**原文链接**: [https://mechanical-pencil.com/products/spray-bottle](https://mechanical-pencil.com/products/spray-bottle)

生成摘要时出错

---

## 85. How a Mechanical Watch Keeps Time

**原文标题**: How a Mechanical Watch Keeps Time

**原文链接**: [https://martincmartin.github.io/slidev-stem/watches/article/1/](https://martincmartin.github.io/slidev-stem/watches/article/1/)

生成摘要时出错

---

## 86. A Tasty Combination: Multivariable Calculus and Differential Forms

**原文标题**: A Tasty Combination: Multivariable Calculus and Differential Forms

**原文链接**: [https://arxiv.org/abs/0910.0047](https://arxiv.org/abs/0910.0047)

生成摘要时出错

---

## 87. 2035 came early

**原文标题**: 2035 came early

**原文链接**: [https://fzakaria.com/2026/11/23/2035-came-early](https://fzakaria.com/2026/11/23/2035-came-early)

生成摘要时出错

---

## 88. Calculate how many mesh radio nodes your city needs

**原文标题**: Calculate how many mesh radio nodes your city needs

**原文链接**: [https://meshcoveragecalculator.lalala.ing/](https://meshcoveragecalculator.lalala.ing/)

生成摘要时出错

---

## 89. New rewritable antimony selenide display shows an image for months without power

**原文标题**: New rewritable antimony selenide display shows an image for months without power

**原文链接**: [https://tmos.org.au/news/new-rewritable-displays-can-show-an-image-for-months-without-power/](https://tmos.org.au/news/new-rewritable-displays-can-show-an-image-for-months-without-power/)

生成摘要时出错

---

## 90. Google search alternative Kagi launches Gmail rival

**原文标题**: Google search alternative Kagi launches Gmail rival

**原文链接**: [https://arstechnica.com/gadgets/2026/11/google-search-alternative-kagi-launches-gmail-rival/](https://arstechnica.com/gadgets/2026/11/google-search-alternative-kagi-launches-gmail-rival/)

生成摘要时出错

---

## 91. Canada's median health-care wait time hits 30.7 weeks–longest ever recorded

**原文标题**: Canada's median health-care wait time hits 30.7 weeks–longest ever recorded

**原文链接**: [https://www.fraserinstitute.org/studies/waiting-your-turn-wait-times-for-health-care-in-canada-2026](https://www.fraserinstitute.org/studies/waiting-your-turn-wait-times-for-health-care-in-canada-2026)

生成摘要时出错

---

## 92. Splitting USB-C: USB 3 and USB 2 on one port

**原文标题**: Splitting USB-C: USB 3 and USB 2 on one port

**原文链接**: [https://www.frankchiarulli.com/blog/splitting-usb-c/](https://www.frankchiarulli.com/blog/splitting-usb-c/)

生成摘要时出错

---

## 93. From CUDA and Jax to TorchTPU: Lessons from a Cayley Graph Solver

**原文标题**: From CUDA and Jax to TorchTPU: Lessons from a Cayley Graph Solver

**原文链接**: [https://andlukyane.com/blog/cayley-graphs-and-torchtpu](https://andlukyane.com/blog/cayley-graphs-and-torchtpu)

生成摘要时出错

---

## 94. LLM agents work for their parent companies, not for you

**原文标题**: LLM agents work for their parent companies, not for you

**原文链接**: [https://michaelharley.net/posts/2026/11/01/llm-agents-work-for-their-parent-companies-not-for-you/](https://michaelharley.net/posts/2026/11/01/llm-agents-work-for-their-parent-companies-not-for-you/)

生成摘要时出错

---

## 95. Fable 5.2 tries less on some hard tasks when a shortcut is available

**原文标题**: Fable 5.2 tries less on some hard tasks when a shortcut is available

**原文链接**: [https://goodhartlabs.com/blog/fable-5-2-tries-less-on-some-hard-tasks-when-a-shortcut-is-available](https://goodhartlabs.com/blog/fable-5-2-tries-less-on-some-hard-tasks-when-a-shortcut-is-available)

生成摘要时出错

---

## 96. Spending 35B Opus 5.5 Tokens to Write a Symphony

**原文标题**: Spending 35B Opus 5.5 Tokens to Write a Symphony

**原文链接**: [https://danprice.ai/blog/opus-symphony](https://danprice.ai/blog/opus-symphony)

生成摘要时出错

---

## 97. AMD EPYC Zen 6 vs. Zen 1 Performance: 12.1x Geo Mean in Less Than 10 Years

**原文标题**: AMD EPYC Zen 6 vs. Zen 1 Performance: 12.1x Geo Mean in Less Than 10 Years

**原文链接**: [https://www.phoronix.com/review/amd-epyc-9006-7601](https://www.phoronix.com/review/amd-epyc-9006-7601)

生成摘要时出错

---

## 98. I've been drinking wine in my kitchen

**原文标题**: I've been drinking wine in my kitchen

**原文链接**: [https://scottaaronson.blog/?p=10362](https://scottaaronson.blog/?p=10362)

生成摘要时出错

---

## 99. US authorizes SpaceX to deploy 1M satellites for data centers in space

**原文标题**: US authorizes SpaceX to deploy 1M satellites for data centers in space

**原文链接**: [https://www.reuters.com/business/media-telecom/us-authorizes-spacex-deploy-1-million-satellites-data-centers-space-2026-11-25/](https://www.reuters.com/business/media-telecom/us-authorizes-spacex-deploy-1-million-satellites-data-centers-space-2026-11-25/)

生成摘要时出错

---

## 100. 1.5 TB of Dark Net Market Scrapes (2015)

**原文标题**: 1.5 TB of Dark Net Market Scrapes (2015)

**原文链接**: [https://gwern.net/dnm-archive](https://gwern.net/dnm-archive)

生成摘要时出错

---

