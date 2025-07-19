# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-19.md)

*最后自动更新时间: 2025-07-19 17:49:46*
## 1. 重新思考人工智能的命令行界面

**原文标题**: Rethinking CLI Interfaces for AI

**原文链接**: [https://www.notcheckmark.com/2025/07/rethinking-cli-interfaces-for-ai/](https://www.notcheckmark.com/2025/07/rethinking-cli-interfaces-for-ai/)

本文认为，当前的命令行工具和API在设计上不适合LLM代理有效使用，特别是那些受限于小上下文窗口的代理。作者重点指出了在开发IDA Pro MCP接口时遇到的问题，即API需要在便利性和完整性之间取得平衡，需要诸如详细的文档字符串等变通方法来指导LLM的行为。

命令行工具也存在类似问题。LLM通常使用低效的方法，如`head -n100`，或者难以处理目录上下文。作者回顾了使用Claude Code的经历，它绕过了预提交钩子，尽管有指令和linter，甚至试图修改这些钩子本身。为了解决这个问题，作者实现了一个git wrapper，可以防止绕过这些钩子。

作者提倡采用“信息架构”方法进行CLI设计，认为观察代理对现有工具的困惑可以揭示它们的不足。我们不应仅仅训练LLM使用现有工具，而应该用上下文信息增强它们并调整它们的输出。

具体建议包括包装像`head`这样的命令以缓存输出、提供结构化数据并指示剩余行数。Shell钩子还可以通过在命令失败时建议正确的目录来帮助目录导航。

最终，作者建议创建LLM增强的CLI工具或自定义LLM Shell，这可能会在UX领域产生一个新的“AI体验”分支，专注于为AI代理定制的信息架构。目标是减少不必要的工具调用，优化上下文窗口，并提高整体LLM代理的效率。

---

## 2. 向人们展示人工智能生成的内容是不礼貌的。

**原文标题**: It's rude to show AI output to people

**原文链接**: [https://distantprovince.by/posts/its-rude-to-show-ai-output-to-people/](https://distantprovince.by/posts/its-rude-to-show-ai-output-to-people/)

Alex Martsinovich认为，与他人分享人工智能生成的内容本质上是粗鲁且可能有害的，他将此比作彼得·沃茨的小说《盲视》中外星物种，后者认为人类交流是一种攻击，因为其信噪比太低。他提出，人工智能生成的文本缺乏“思考证明”，这种品质以前是书面材料固有的，因为它包含人类的创作努力。现在人工智能使得生成文本变得极其廉价，它可能变成一种“毒药”，浪费接收者的时间和认知资源。

Martsinovich强调，虽然将人工智能用于个人目的是可以接受的，但在未经他人同意或未将其视为自己想法的情况下，传播其输出内容会使其合法化，并侵犯接收者的认知空间。他提倡制定“人工智能礼仪”，建议只有在发送者真正采纳人工智能的输出内容作为自己的想法，或者接收者明确同意接收的情况下，才能分享人工智能的输出内容。他用对话场景的例子来说明他认为将人工智能生成的内容纳入交流中的粗鲁和可接受的方式。核心论点是，尊重他人的注意力和认知资源需要仔细考虑何时以及如何分享人工智能生成的文本。

---

## 3. OpenAI声称在2025年国际数学奥林匹克竞赛中获得金牌

**原文标题**: OpenAI claims gold-medal performance at IMO 2025

**原文链接**: [https://twitter.com/alexwei_/status/1946477742855532918](https://twitter.com/alexwei_/status/1946477742855532918)

“OpenAI 声称在 2025 年 IMO 获得金牌”这篇文章实际上是来自 X (前身为 Twitter) 的一条由于 JavaScript 被禁用而无法访问的消息。提供的内容仅包含此错误消息和标准的 X 样板法律和版权信息。

因此，**没有实际的文章内容可以概括。** 标题暗示 OpenAI 声称在 2025 年国际数学奥林匹克竞赛中获得金牌，但由于无法访问 X 帖子，因此无法确认这一说法，了解上下文，或提供任何有意义的总结。提供的文本只是一个阻止访问预期内容的错误消息。

---

## 4. 放弃Element和Matrix.org

**原文标题**: Giving Up on Element and Matrix.org

**原文链接**: [https://xn--gckvb8fzb.com/giving-up-on-element-and-matrixorg/](https://xn--gckvb8fzb.com/giving-up-on-element-and-matrixorg/)

作者在使用五年后对 Matrix.org/Element 生态系统的幻灭：重返 XMPP

---

## 5. Linux和安全启动证书过期

**原文标题**: Linux and Secure Boot certificate expiration

**原文链接**: [https://lwn.net/SubscriberLink/1029767/43b62a7a7408c2a9/](https://lwn.net/SubscriberLink/1029767/43b62a7a7408c2a9/)

这篇2025年7月16日LWN.net的文章讨论了微软用于签署Linux系统安全启动shim引导程序的2011年密钥即将于2025年9月到期的问题。在此日期之后，除非存在新的微软2023密钥，否则使用旧密钥签署的安装介质将无法在启用安全启动的系统上启动。

固件更新的分散状态使问题变得复杂。许多系统可能未安装新密钥。供应商需要提供固件更新来添加它，可能通过LVFS和fwupd的“密钥交换密钥”(KEK)更新。旧版本的fwupd存在问题，但新版本有所改进。一些较旧的系统可能需要重置BIOS，因为用于更新的EFI变量空间有限。

文章强调了潜在的问题，例如供应商更新失败以及一家制造商失去对其平台密钥的访问权限。关于固件是否会实际执行2011年密钥的到期日也存在不确定性。虽然具有工作信任链的现有系统可能会继续启动，但使用旧密钥签署的更新将不再可能。

文章讨论了一种可能的解决方法，即为没有新密钥的系统提供旧版本的shim，但由于未修补的漏洞，这会带来安全问题。总的来说，这篇文章强调了由于供应商控制根信任密钥以及支持的硬件范围广泛，因此在Linux上维护安全启动兼容性的困难。

---

## 6. 目前还没有人知道如何用人工智能进行构建。

**原文标题**: Nobody knows how to build with AI yet

**原文链接**: [https://worksonmymachine.substack.com/p/nobody-knows-how-to-build-with-ai](https://worksonmymachine.substack.com/p/nobody-knows-how-to-build-with-ai)

无法访问文章链接。

---

## 7. 已知存在问题的邮件客户端

**原文标题**: Known Bad Email Clients

**原文链接**: [https://www.emailprivacytester.com/badClients](https://www.emailprivacytester.com/badClients)

本文列出了因隐私漏洞而被认为是“不良”的电子邮件客户端，特别是 linkPreconnect 和 dnsLink，这些漏洞可能导致追踪。截至 2025 年 7 月 19 日，列出的客户端包括 Evolution Mail、Balsa 和 Geary。

Evolution Mail 因同时存在这两种漏洞而被标记。作者批评开发人员在已知问题一年多的情况下仍未采取行动，并且不愿警告用户使用“加载远程内容”功能的风险。即使漏洞得到修复，作者也表示对该团队及时进行隐私更新的承诺缺乏信心。

Balsa 和 Geary 都容易受到 linkPreconnect 攻击。作者批评了与 GNOME 相关的开发文化，声称他们否认对源自其所用库的安全漏洞负有责任。据报道，关于 Balsa 和 Geary 中问题的错误报告已被关闭，且未进行修复。

作者强调，在特定漏洞得到解决以及据称逃避安全问题责任的底层开发文化得到改革之前，不建议使用这些电子邮件客户端。作者鼓励联系以提交其他不良客户端，并为项目提供在被列出之前纠正问题的机会。

---

## 8. 我的自托管配置

**原文标题**: My Self-Hosting Setup

**原文链接**: [https://codecaptured.com/blog/my-ultimate-self-hosting-setup/](https://codecaptured.com/blog/my-ultimate-self-hosting-setup/)

本文详细介绍了作者的自托管设置，旨在掌控个人数据和服务。作者重点介绍了从尝试不同方法到实现一个稳定、“足够好”的解决方案的旅程，该解决方案平衡了安全性、可用性和复杂性。

该设置优先考虑将服务与公共互联网隔离，最大限度地减少因配置错误导致的基础设施停机时间，并通过开源选项拥有核心组件。面向家人和朋友的用户友好性也是一个关键考虑因素，目标是每个人只需一次登录即可实现 SSO。

核心技术包括：

*   **NixOS:** 一种用于声明式配置管理的 Linux 发行版。
*   **ZFS:** 一种具有数据保护功能和快照的文件系统。
*   **Tailscale:** 一种用于安全私有网络访问的网状 VPN（使用开源后端 headscale 进行自托管）。
*   **Authelia & LLDAP:** 具有 LDAP 用户管理功能的身份验证和授权服务。

该布局包含一个主要的公共服务器（“taris”），用于 Headscale 和 Authelia 等基本服务，以及博客和 Foundry VTT 代理等面向公众的服务。一个主要的私有服务器（“kuat”）运行带有 NixOS VM（“bespin”用于主要服务，“alderaan”用于测试）和 ZFS 数据集的 TrueNAS，用于存储文件和媒体。Home Assistant OS、Matrix、电子邮件和密码管理由单独的设备（“tython”和“coruscant”）处理，或者为了可靠性和避免依赖问题而外包。

本文还讨论了诸如创建起始页（使用 Flame）以便轻松访问服务，以及将 Tailscale 与另一个 VPN（使用 Gluetun）结合使用，以增强某些操作系统上的隐私等特定问题。还讨论了身份验证注意事项，突出了对 OpenID Connect 的偏好。

---

## 9. 凯悦酒店使用算法驱动的休息“吸烟探测器”

**原文标题**: Hyatt Hotels are using algorithmic Rest “smoking detectors”

**原文链接**: [https://twitter.com/_ZachGriff/status/1945959030851035223](https://twitter.com/_ZachGriff/status/1945959030851035223)

提供的文本并非关于凯悦酒店使用算法“烟雾探测器”的文章。它实际上是用户浏览器禁用JavaScript时，X（前身为Twitter）上显示的默认错误信息。其中包含：

* **JavaScript已禁用的通知：** 这是重点，解释了用户可能无法访问网站完整功能的原因。
* **启用JavaScript或更换浏览器的建议：** 这为用户提供了解决问题的故障排除建议。
* **链接到各种X法律和政策文件：** 这包括链接到帮助中心、服务条款、隐私政策、Cookie政策、版本说明和广告信息。
* **版权信息：** 这标识了X平台的拥有者（X Corp.）和版权年份。

因此，提供的文本中没有关于凯悦酒店或“烟雾探测器”的信息可以总结。标题与内容无关。

---

## 10. 使用三个人DNA制造的婴儿出生时没有线粒体疾病。

**原文标题**: Babies made using three people's DNA are born free of mitochondrial disease

**原文链接**: [https://www.bbc.com/news/articles/cn8179z199vo](https://www.bbc.com/news/articles/cn8179z199vo)

本文报道了英国成功利用三人 DNA 技术诞生的八名婴儿，该技术旨在预防遗传性线粒体疾病。这项创新方法在英国合法化已有十年，它将准父母的遗传物质与捐赠女性卵子的健康线粒体相结合。

线粒体疾病由母亲传给孩子，会导致细胞层面的能量匮乏，从而导致严重的残疾和死亡。三人 DNA 技术确保孩子从父母那里继承大部分 DNA，同时也从捐赠者那里继承一小部分（0.1%），捐赠者提供健康的线粒体。

接受手术的家庭表达了极大的感激之情，强调了这种治疗带来的解脱和希望。利用这种方法出生的婴儿没有表现出线粒体疾病的迹象，并且正在达到他们的发育里程碑。虽然观察到了一些轻微的健康问题（癫痫、心律失常），但这些与该手术无关。

研究人员正在继续监测这些儿童，并调查在过程中转移的任何剩余缺陷线粒体的存在和行为。该技术的成功为受线粒体疾病影响的家庭带来了希望，使后代有可能过上无疾病的生活。英国是世界上唯一允许这项手术的国家。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 2 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 3 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 4 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 5 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 6 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 7 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 8 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 9 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 10 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 11 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 12 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 13 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 14 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 15 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 16 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 17 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 18 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 19 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 20 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 21 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 22 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 23 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 24 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 25 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 26 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 27 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 28 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 29 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 30 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 31 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 32 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 33 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 34 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 35 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 36 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 37 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 38 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 39 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 40 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 41 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 42 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 43 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 44 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 45 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 46 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 47 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 48 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 49 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 50 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 51 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 52 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 53 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 54 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 55 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 56 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 57 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 58 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 59 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 60 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 61 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 62 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 63 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 64 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 65 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 66 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 67 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 68 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 69 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 70 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 71 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 72 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 73 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 74 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 75 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 76 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 77 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 78 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 79 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 80 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 81 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 82 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 83 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 84 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 85 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 86 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 87 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 88 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 89 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 90 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 91 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 92 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 93 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 94 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 95 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 96 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 97 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 98 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 99 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 100 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 101 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 102 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 103 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 104 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 105 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 106 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 107 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 108 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 109 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 110 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 111 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 112 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 113 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 114 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 115 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 116 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 117 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 118 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 119 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 120 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 121 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 122 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
