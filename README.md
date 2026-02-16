# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-16.md)

*最后自动更新时间: 2026-02-16 18:12:28*
## 1. 英国司法部下令删除英国最大的庭审报告数据库。

**原文标题**: Ministry of Justice orders deletion of the UK's largest court reporting database

**原文链接**: [https://www.legalcheek.com/2026/02/ministry-of-justice-orders-deletion-of-the-uks-largest-court-reporting-database/](https://www.legalcheek.com/2026/02/ministry-of-justice-orders-deletion-of-the-uks-largest-court-reporting-database/)

英国司法部（MoJ）已下令永久删除该国最大的法庭报道数据库 Courtsdesk，此举引发了关于“司法公开”与数据隐私的激烈辩论。

**冲突焦点**
英国法院及法庭事务局（HMCTS）向该平台发布了关停通知，理由是其涉嫌与第三方人工智能公司“未经授权共享”敏感庭审信息。因此，司法部强制要求抹除该档案库中的所有记录。

**对新闻业的影响**
Courtsdesk 于 2020 年在政府批准下推出，是来自 39 家媒体机构的 1500 多名记者追踪地方法院案件的重要工具。创始人恩达·莱希（Enda Leahy）辩称，该服务至关重要，因为据称 HMCTS 的官方记录准确率仅为 4.2%。她进一步声称，已有 160 万场刑事听证会在未预先通知媒体的情况下进行，并断言 Courtsdesk 是唯一能让记者获悉法庭实况的系统。

**政府回应**
尽管有 16 次暂缓执行的呼吁，且前司法部部长克里斯·菲利普（Chris Philp）也曾介入，但现任法院部部长萨拉·萨克曼（Sarah Sackman）仍拒绝保留该档案库。司法部发言人坚称，记者的信息获取权并未受损，因为官方名单和记录仍可通过政府渠道获取。

**公众舆论**
此举遭到了法律评论员和记者的严厉批评，他们认为这是对透明度的打击，并将其视为迈向“媒体封锁”的一步。相反，一些支持该决定的人士认为，保护个人数据免受人工智能剥削是必要的安全措施。

此次删除标志着一个中心化、可搜索的数字档案库的终结，而媒体界的许多人曾将其视为现代刑事法庭报道的支柱。

---

## 2. 运行我自己的 XMPP 服务器

**原文标题**: Running My Own XMPP Server

**原文链接**: [https://blog.dmcc.io/journal/xmpp-turn-stun-coturn-prosody/](https://blog.dmcc.io/journal/xmpp-turn-stun-coturn-prosody/)

本文概述了使用 **Prosody** 和 **Docker** 搭建个人联邦化 XMPP 服务器的指南。出于对数字主权以及摆脱 Signal 等中心化平台的渴望，作者展示了 XMPP 如何提供一种可靠的自托管消息传递备选方案。

**关键技术步骤：**
*   **基础设施：** 该方案使用 Docker Compose 运行 Prosody 13.0。它需要一个带有特定 **DNS SRV 记录**（用于客户端和服务器发现）的域名，以及通过 Let’s Encrypt 和 Cloudflare 获取的 TLS 证书。
*   **移动端优化：** 为确保现代化的用户体验，作者强调了几个核心模块：用于多设备同步的 `carbons`、用于处理连接不稳定的 `smacks`，以及用于移动推送通知的 `cloud_notify`。
*   **安全性：** 配置要求强制加密连接（c2s/s2s）并禁用公开注册。尽管服务器本身是安全的，作者仍建议使用 **OMEMO** 进行客户端端到端加密。
*   **高级功能：**
    *   **文件共享：** 通过带有 Caddy 反向代理的 HTTP 上传组件实现。
    *   **群聊：** 通过多用户聊天 (MUC) 模块启用。
    *   **音视频通话：** 需要独立的 **Coturn** 容器提供 STUN/TURN 服务以实现 NAT 穿透。
*   **客户端兼容性：** 推荐的客户端包括 **Monal** (iOS/macOS)、**Conversations** (Android) 和 **Gajim** (桌面端)，它们均支持现代 XMPP 标准。

作者总结道，虽然 Signal 仍是其主要工具，但自托管 XMPP 服务器是一个轻量且稳健的“周末项目”，能确保用户不会被锁定在单一供应商的生态系统中。该配置可通过 `prosodyctl check` 工具和 XMPP 合规性测试器轻松验证。

---

## 3. 蓝牙设备揭示了你的哪些信息

**原文标题**: What Your Bluetooth Devices Reveal About You

**原文链接**: [https://blog.dmcc.io/journal/2026-bluetooth-privacy-bluehood/](https://blog.dmcc.io/journal/2026-bluetooth-privacy-bluehood/)

在本文中，作者介绍了 **Bluehood**，这是一款旨在演示持续蓝牙广播带来的重大隐私风险的开源蓝牙扫描器。受近期 **WhisperPair** 漏洞 (CVE-2025-36911) 的启发，作者探讨了我们的“常开”设备如何充当数字面包屑（digital breadcrumbs）。

**关键点：**
*   **被动元数据泄露：** 仅通过监听而不进行连接，Bluehood 工具就能识别生活模式，例如邻居何时出门上班、哪些设备属于同一个人（如手机与智能手表的配对），以及送货车辆到达的频率。
*   **控制权问题：** 许多设备（包括助听器、心脏起搏器和物流车队）会持续广播信号，且未向用户提供禁用选项。
*   **隐私悖论：** 像 **Briar** 和 **BitChat** 这样安全的点对点通讯应用在网络中断期间依赖蓝牙运行。这造成了一种矛盾：旨在保护隐私的工具同时暴露了用户的物理存在。
*   **Bluehood 的功能：** 该工具利用 Python 在 AI 辅助下构建，具备被动扫描、设备分类和模式分析（热图和停留时间）功能。它专为教育目的而非黑客攻击设计，可在树莓派或笔记本电脑等基础硬件上运行。

**结论：**
该项目提供了一个“发人深省”的提醒：即使没有恶意，任何具备基础技术知识的人都能收集到有关家庭习惯的敏感信息。作者总结道，虽然蓝牙通常是出于便利或医疗需求所必需的，但用户必须理解保持无线电功能开启所固有的隐私权衡。

---

## 4. Show HN：简单的 org-mode Web 适配器

**原文标题**: Show HN: Simple org-mode web adapter

**原文链接**: [https://github.com/SpaceTurth/Org-Web-Adapter](https://github.com/SpaceTurth/Org-Web-Adapter)

**Org Web Adapter** 是一款轻量级的本地 Web 应用程序，专为通过浏览器浏览和编辑 Emacs Org-mode 文件而设计。它由极简的 Python 后端（`main.py`）和单页面 HTML/CSS 前端构建，提供了一个实用的三窗格界面，无需复杂的基础设施即可管理个人笔记。

**核心功能：**
*   **导航与搜索：** 递归扫描指定目录下的 `.org` 文件，并将其呈现在可搜索的侧边栏中。支持按创建日期、反向链接数量或随机排序。
*   **链接管理：** 支持解析 `file:` 和 `id:` 链接，并自动计算反向链接，在专用窗格中显示笔记之间的关联。
*   **编辑与渲染：** 用户可以在预览模式和内置编辑器之间切换，修改将直接保存至本地磁盘。内置 MathJax 支持以实现 LaTeX 数学公式渲染，并采用兼容桌面与移动端的响应式设计。
*   **自定义：** 界面支持浅色/深色主题切换，服务器可通过 YAML 文件或命令行参数进行配置。

**技术考量：**
该应用的设计初衷是追求简单而非高性能扩展。它在每次请求时都会重新扫描笔记目录以确保数据实时性，并使用简化的自定义 Org 解析器而非完整实现。

**安全警告：**
该工具不含内置身份验证或加密功能。因此，开发者建议仅在受信任的本地网络中运行。对于希望快速通过 Web 访问 Org-mode 知识库的用户，它提供了一个精简的“单文件”解决方案。

---

## 5. NSA 开发的 Ghidra

**原文标题**: Ghidra by NSA

**原文链接**: [https://github.com/NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

Ghidra是由美国国家安全局（NSA）研究局开发并维护的一款综合性软件逆向工程（SRE）框架。它旨在处理大规模、复杂的分析任务，支持用户在Windows、macOS和Linux平台上检查已编译的代码。其核心功能包括反汇编、反编译、汇编、图形化分析和脚本编写，支持大量的处理器指令集和可执行文件格式。

Ghidra最初是为辅助NSA的网络安全任务而构建的——专门用于分析恶意代码和识别网络漏洞——现在已成为一个开源平台。它具有高度的可扩展性，允许用户通过集成Eclipse或Visual Studio Code，使用Java或Python开发自定义组件和脚本。

**关键技术信息：**
*   **环境

NSA鼓励开源社区做出贡献，并利用该项目为有志于开发网络安全工具以保护国家利益的美国公民展示职业机会。

---

## 6. Qwen3.5: Towards Native Multimodal Agents

**原文标题**: Qwen3.5: Towards Native Multimodal Agents

**原文链接**: [https://qwen.ai/blog?id=qwen3.5](https://qwen.ai/blog?id=qwen3.5)

生成摘要时出错

---

## 7. The Sideprocalypse

**原文标题**: The Sideprocalypse

**原文链接**: [https://johan.hal.se/wrote/2026/02/03/the-sideprocalypse/](https://johan.hal.se/wrote/2026/02/03/the-sideprocalypse/)

生成摘要时出错

---

## 8. WebMCP Proposal

**原文标题**: WebMCP Proposal

**原文链接**: [https://webmachinelearning.github.io/webmcp/](https://webmachinelearning.github.io/webmcp/)

生成摘要时出错

---

## 9. I want to wash my car. The car wash is 50 meters away. Should I walk or drive?

**原文标题**: I want to wash my car. The car wash is 50 meters away. Should I walk or drive?

**原文链接**: [https://mastodon.world/@knowmadd/116072773118828295](https://mastodon.world/@knowmadd/116072773118828295)

生成摘要时出错

---

## 10. I’m joining OpenAI

**原文标题**: I’m joining OpenAI

**原文链接**: [https://steipete.me/posts/2026/openclaw](https://steipete.me/posts/2026/openclaw)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 2 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 3 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 4 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 5 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 6 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 7 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 8 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 9 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 10 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 11 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 12 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 13 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 14 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 15 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 16 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 17 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 18 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 19 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 20 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 21 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 22 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 23 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 24 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 25 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 26 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 27 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 28 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 29 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 30 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 31 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 32 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 33 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 34 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 35 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 36 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 37 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 38 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 39 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 40 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 41 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 42 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 43 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 44 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 45 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 46 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 47 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 48 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 49 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 50 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 51 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 52 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 53 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 54 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 55 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 56 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 57 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 58 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 59 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 60 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 61 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 62 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 63 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 64 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 65 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 66 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 67 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 68 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 69 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 70 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 71 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 72 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 73 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 74 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 75 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 76 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 77 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 78 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 79 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 80 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 81 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 82 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 83 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 84 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 85 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 86 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 87 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 88 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 89 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 90 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 91 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 92 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 93 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 94 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 95 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 96 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 97 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 98 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 99 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 100 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 101 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 102 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 103 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 104 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 105 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 106 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 107 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 108 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 109 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 110 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 111 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 112 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 113 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 114 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 115 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 116 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 117 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 118 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 119 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 120 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 121 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 122 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 123 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 124 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 125 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 126 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 127 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 128 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 129 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 130 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 131 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 132 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 133 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 134 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 135 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 136 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 137 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 138 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 139 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 140 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 141 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 142 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 143 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 144 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 145 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 146 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 147 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 148 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 149 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 150 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 151 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 152 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 153 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 154 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 155 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 156 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 157 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 158 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 159 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 160 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 161 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 162 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 163 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 164 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 165 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 166 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 167 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 168 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 169 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 170 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 171 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 172 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 173 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 174 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 175 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 176 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 177 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 178 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 179 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 180 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 181 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 182 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 183 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 184 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 185 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 186 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 187 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 188 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 189 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 190 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 191 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 192 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 193 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 194 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 195 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 196 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 197 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 198 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 199 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 200 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 201 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 202 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 203 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 204 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 205 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 206 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 207 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 208 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 209 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 210 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 211 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 212 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 213 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 214 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 215 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 216 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 217 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 218 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 219 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 220 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 221 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 222 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 223 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 224 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 225 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 226 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 227 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 228 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 229 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 230 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 231 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 232 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 233 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 234 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 235 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 236 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 237 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 238 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 239 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 240 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 241 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 242 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 243 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 244 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 245 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 246 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 247 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 248 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 249 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 250 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 251 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 252 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 253 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 254 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 255 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 256 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 257 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 258 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 259 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 260 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 261 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 262 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 263 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 264 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 265 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 266 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 267 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 268 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 269 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 270 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 271 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 272 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 273 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 274 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 275 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 276 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 277 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 278 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 279 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 280 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 281 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 282 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 283 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 284 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 285 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 286 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 287 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 288 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 289 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 290 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 291 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 292 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 293 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 294 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 295 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 296 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 297 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 298 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 299 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 300 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 301 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 302 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 303 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 304 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 305 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 306 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 307 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 308 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 309 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 310 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 311 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 312 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 313 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 314 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 315 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 316 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 317 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 318 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 319 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 320 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 321 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 322 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 323 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 324 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 325 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 326 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 327 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 328 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 329 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 330 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 331 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 332 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 333 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
