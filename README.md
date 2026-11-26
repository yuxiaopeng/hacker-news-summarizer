# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-26.md)

*最后自动更新时间: 2026-11-26 01:15:39*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-26](output/hacker_news_summary_2026-11-26.md) |
| 2 | [2026-11-25](output/hacker_news_summary_2026-11-25.md) |
| 3 | [2026-11-19](output/hacker_news_summary_2026-11-19.md) |
| 4 | [2026-11-24](output/hacker_news_summary_2026-11-24.md) |
| 5 | [2026-11-22](output/hacker_news_summary_2026-11-22.md) |
| 6 | [2026-11-21](output/hacker_news_summary_2026-11-21.md) |
| 7 | [2026-11-18](output/hacker_news_summary_2026-11-18.md) |
| 8 | [2026-11-20](output/hacker_news_summary_2026-11-20.md) |
| 9 | [2026-11-14](output/hacker_news_summary_2026-11-14.md) |
| 10 | [2026-11-11](output/hacker_news_summary_2026-11-11.md) |
| 11 | [2026-11-15](output/hacker_news_summary_2026-11-15.md) |
| 12 | [2026-11-12](output/hacker_news_summary_2026-11-12.md) |
| 13 | [2026-11-13](output/hacker_news_summary_2026-11-13.md) |
| 14 | [2026-11-17](output/hacker_news_summary_2026-11-17.md) |
| 15 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 16 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 17 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 18 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 19 | [2026-11-10](output/hacker_news_summary_2026-11-10.md) |
| 20 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 21 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 22 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 23 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 24 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 25 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 26 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 27 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 28 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 29 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 30 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 31 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 32 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 33 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 34 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 35 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 36 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 37 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 38 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 39 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 40 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 41 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 42 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 43 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 44 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 45 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 46 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 47 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 48 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 49 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 50 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 51 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 52 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 53 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 54 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 55 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 56 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 57 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 58 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 59 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 60 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 61 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 62 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 63 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 64 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 65 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 66 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 67 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 68 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 69 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 70 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 71 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 72 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 73 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 74 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 75 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 76 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 77 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 78 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 79 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 80 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 81 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 82 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 83 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 84 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 85 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 86 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 87 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 88 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 89 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 90 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 91 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 92 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 93 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 94 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 95 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 96 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 97 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 98 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 99 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 100 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 101 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 102 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 103 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 104 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 105 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 106 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 107 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 108 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 109 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 110 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 111 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 112 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 113 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 114 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 115 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 116 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 117 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 118 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 119 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 120 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 121 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 122 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 123 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 124 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 125 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 126 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 127 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 128 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 129 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 130 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 131 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 132 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 133 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 134 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 135 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 136 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 137 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 138 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 139 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 140 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 141 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 142 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 143 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 144 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 145 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 146 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 147 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 148 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 149 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 150 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 151 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 152 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 153 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 154 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 155 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 156 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 157 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 158 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 159 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 160 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 161 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 162 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 163 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 164 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 165 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 166 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 167 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 168 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 169 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 170 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 171 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 172 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 173 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 174 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 175 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 176 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 177 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 178 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 179 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 180 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 181 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 182 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 183 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 184 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 185 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 186 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 187 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 188 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 189 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 190 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 191 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 192 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 193 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 194 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 195 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 196 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 197 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 198 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 199 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 200 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 201 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 202 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 203 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 204 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 205 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 206 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 207 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 208 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 209 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 210 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 211 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 212 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 213 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 214 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 215 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 216 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 217 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 218 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 219 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 220 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 221 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 222 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 223 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 224 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 225 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 226 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 227 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 228 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 229 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 230 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 231 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 232 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 233 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 234 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 235 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 236 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 237 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 238 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 239 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 240 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 241 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 242 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 243 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 244 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 245 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 246 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 247 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 248 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 249 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 250 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 251 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 252 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 253 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 254 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 255 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 256 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 257 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 258 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 259 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 260 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 261 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 262 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 263 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 264 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 265 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 266 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 267 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 268 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 269 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 270 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 271 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 272 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 273 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 274 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 275 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 276 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 277 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 278 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 279 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 280 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 281 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 282 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 283 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 284 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 285 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 286 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 287 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 288 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 289 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 290 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 291 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 292 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 293 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 294 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 295 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 296 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 297 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 298 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 299 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 300 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 301 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 302 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 303 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 304 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 305 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 306 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 307 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 308 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 309 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 310 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 311 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 312 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 313 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 314 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 315 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 316 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 317 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 318 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 319 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 320 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 321 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 322 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 323 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 324 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 325 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 326 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 327 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 328 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 329 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 330 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 331 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 332 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 333 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 334 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 335 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 336 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 337 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 338 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 339 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 340 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 341 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 342 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 343 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 344 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 345 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 346 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 347 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 348 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 349 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 350 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 351 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 352 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 353 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 354 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 355 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 356 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 357 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 358 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 359 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 360 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 361 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 362 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 363 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 364 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 365 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 366 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 367 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 368 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 369 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 370 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 371 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 372 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 373 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 374 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 375 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 376 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 377 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 378 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 379 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 380 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 381 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 382 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 383 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 384 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 385 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 386 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 387 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 388 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 389 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 390 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 391 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 392 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 393 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 394 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 395 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 396 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 397 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 398 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 399 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 400 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 401 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 402 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 403 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 404 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 405 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 406 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 407 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 408 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 409 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 410 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 411 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 412 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 413 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 414 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 415 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 416 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 417 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 418 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 419 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 420 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 421 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 422 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 423 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 424 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 425 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 426 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 427 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 428 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 429 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 430 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 431 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 432 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 433 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 434 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 435 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 436 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 437 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 438 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 439 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 440 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 441 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 442 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 443 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 444 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 445 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 446 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 447 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 448 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 449 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 450 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 451 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 452 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 453 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 454 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 455 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 456 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 457 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 458 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 459 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 460 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 461 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 462 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 463 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 464 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 465 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 466 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 467 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 468 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 469 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 470 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 471 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 472 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 473 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 474 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 475 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 476 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 477 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 478 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 479 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 480 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 481 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 482 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 483 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 484 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 485 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 486 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 487 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 488 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 489 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 490 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 491 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 492 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 493 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 494 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 495 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 496 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 497 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 498 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 499 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 500 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 501 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 502 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 503 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 504 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 505 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 506 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 507 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 508 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 509 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 510 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 511 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 512 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 513 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 514 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 515 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 516 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 517 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 518 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 519 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 520 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 521 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 522 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 523 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 524 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 525 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 526 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 527 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 528 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 529 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 530 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 531 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 532 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 533 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 534 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 535 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 536 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 537 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 538 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 539 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 540 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 541 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 542 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 543 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 544 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 545 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 546 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 547 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 548 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 549 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 550 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 551 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 552 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 553 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 554 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 555 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 556 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 557 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 558 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 559 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 560 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 561 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 562 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 563 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 564 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 565 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 566 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 567 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 568 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 569 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 570 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 571 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 572 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 573 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 574 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 575 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 576 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 577 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 578 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 579 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 580 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 581 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 582 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 583 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 584 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 585 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 586 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 587 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 588 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 589 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 590 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 591 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 592 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 593 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 594 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 595 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 596 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 597 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 598 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 599 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 600 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 601 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 602 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 603 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 604 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 605 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 606 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 607 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 608 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 609 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 610 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
