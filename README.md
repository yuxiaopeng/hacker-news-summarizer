# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-04-17.md)

*最后自动更新时间: 2025-04-17 17:48:38*
## 1. OpenAI顶级灾难风险官员突然辞职

**原文标题**: Top OpenAI Catastrophic Risk Official Steps Down Abruptly

**原文链接**: [https://garrisonlovely.substack.com/p/breaking-top-openai-catastrophic](https://garrisonlovely.substack.com/p/breaking-top-openai-catastrophic)

无法访问文章链接。

---

## 2. DeepSeek分布式文件系统入门

**原文标题**: An Intro to DeepSeek's Distributed File System

**原文链接**: [https://maknee.github.io/blog/2025/3FS-Performance-Journal-1/](https://maknee.github.io/blog/2025/3FS-Performance-Journal-1/)

本文介绍DeepSeek的开源分布式文件系统3FS（Fire-Flyer File System）。它阐述了分布式文件系统的概念，强调了其将数据碎片化分布在多台机器上的复杂性抽象化，从而使用户感觉就像在使用单个本地文件系统。分布式文件系统的优势包括海量数据服务能力、高吞吐量、容错性和冗余性。

3FS由四种主要节点类型组成：Meta（管理元数据）、Mgmtd（管理集群配置和节点发现）、Storage（存储实际文件数据）和Client（与其他节点通信）。本文详细介绍了每个节点的功能，包括Mgmtd在节点注册和配置中的作用，Meta使用FoundationDB处理文件操作和元数据存储，以及Storage使用ChunkEngine（用Rust编写）通过将文件分成块并将元数据存储在LevelDB中来管理物理存储。

3FS的一个重要方面是它使用CRAQ（具有分配查询的链式复制）来实现强一致性和容错。CRAQ确保数据复制到一系列节点上，写入操作按顺序传播，读取操作可以从干净或脏数据中获取，并且尾节点始终具有最新的数据。

文章最后将3FS与其他分布式文件系统进行比较，强调了实际应用性、调优灵活性和实际实现细节的重要性。作者概述了未来博客文章的计划，以对3FS性能进行基准测试，找出瓶颈，并将其与现有系统进行比较。最后，该文章提供了指向设计说明、技术文档和学术论文的链接，其中包含更深入的信息。

---

## 3. Erlang/OTP SSH 中未经身份验证的远程代码执行

**原文标题**: Unauthenticated Remote Code Execution in Erlang/OTP SSH

**原文链接**: [https://nvd.nist.gov/vuln/detail/CVE-2025-32433](https://nvd.nist.gov/vuln/detail/CVE-2025-32433)

CVE-2025-32433 描述了 Erlang/OTP 的 SSH 服务器中的一个未经身份验证的远程代码执行 (RCE) 漏洞。受影响的版本包括 OTP-27.3.3 之前的版本、OTP-26.2.5.11 之前的版本以及 OTP-25.3.2.20 之前的版本。攻击者可以利用 SSH 协议消息处理中的缺陷，在无需有效凭据的情况下获得未授权访问权限并执行任意命令。

GitHub, Inc. 将此漏洞评级为 CRITICAL（严重），CVSS 3.1 评分为 10.0，向量为 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H。这表明该漏洞可通过网络利用，无需用户交互或权限，攻击复杂度低，并可能导致受影响系统的机密性、完整性和可用性完全受损。

补丁已在 OTP-27.3.3、OTP-26.2.5.11 和 OTP-25.3.2.20 版本中提供。临时的解决方案是禁用 SSH 服务器或使用防火墙规则阻止访问。此漏洞是由于关键功能缺少身份验证 (CWE-306) 导致的。更多详细信息和与修复相关的代码提交可以在链接的 GitHub 资源中找到。

---

## 4. 谷歌是线上广告技术领域的垄断者，法官表示

**原文标题**: Google Is a Monopolist in Online Advertising Tech, Judge Says

**原文链接**: [https://www.nytimes.com/2025/04/17/technology/google-ad-tech-antitrust-ruling.html](https://www.nytimes.com/2025/04/17/technology/google-ad-tech-antitrust-ruling.html)

联邦法官裁定谷歌非法垄断部分在线广告技术市场

---

## 5. 软件制作

**原文标题**: Making Software

**原文链接**: [https://www.makingsoftware.com/](https://www.makingsoftware.com/)

《软件制作》一书面向那些对日常技术如何运作充满好奇心，但又不是技术专家的读者。它不是教程或指南，而是一本解释触摸屏、图像模糊、矢量图形等底层机制的手册。

本书旨在弥合我们对技术的使用与理解之间日益扩大的差距。它旨在提供对事物如何运作的更深入（但不一定是可操作的）的知识，这有助于解决问题或满足纯粹的求知欲。本书使用插图和图表来方便理解。

目录揭示了本书涵盖的广泛主题，包括像素和颜色、字体和矢量、3D和着色器、人工智能和机器学习、压缩和数据、网络和Web、以及编译器和解释器。它还将探讨更具体的例子，如正则表达式、二维码和量子计算。

本书最初将以数字形式发布，之后可能会进行印刷。预购选项允许读者在章节撰写时访问它们，并允许读者提出主题建议。虽然价格尚未确定，但某些内容将是免费的，特别是对于那些在邮件列表中的人。

---

## 6. 不锈钢强化：扭转产生亚微米级“防撞墙”

**原文标题**: Stainless steel strengthened: Twisting creates submicron 'anti-crash wall'

**原文链接**: [https://techxplore.com/news/2025-04-stainless-steel-technique-submicron-anti.html](https://techxplore.com/news/2025-04-stainless-steel-technique-submicron-anti.html)

发表于2025年4月12日Tech Xplore上的一篇文章报道了中国科学院、山东大学和佐治亚理工学院的研究人员开发的一种新型不锈钢强化方法。该研究发表在《科学》杂志上，详细介绍了一种扭转技术，该技术显著提高了金属的抗金属疲劳和循环蠕变能力。

这种创新方法包括重复扭转304奥氏体不锈钢，创造一种空间梯度蜂窝结构，形成亚微米级的三维“防撞墙”。显微分析显示，超细的、小于10纳米的相干层状结构有效地通过阻止堆垛层错来减缓位错运动。这种“防撞墙”像弹簧一样，吸收冲击力，使金属的抗循环蠕变能力更加均匀。

测试表明，与未处理的钢相比，处理后的不锈钢强度提高了2.6倍，棘轮效应引起的应变减少了2到4个数量级。研究人员声称，这种改进可能会使由处理后的钢制成的产品抗疲劳能力提高多达10,000倍，为航空航天等行业的专业应用开辟了可能性。

---

## 7. EasyPost (YC S13) 正在招聘

**原文标题**: EasyPost (YC S13) Is Hiring

**原文链接**: [https://www.easypost.com/careers](https://www.easypost.com/careers)

EasyPost (YC S13) 积极招聘，寻找平易近人、充满活力、富有创造力、才智过人且值得信赖的候选人，共同定义航运的未来。他们正在寻找能够协作、提出挑战性问题、探索新解决方案并承担责任的问题解决者。

该公司强调他们专注于现代、灵活的技术，以改善航运的客户体验，展望实现当日送达和减少环境浪费的未来。他们强调一种适应性强、简单和包容的文化。

EasyPost 以其工程至上的公司理念和务实的软件开发方法而自豪。他们提供一个有趣、充满激情和创业精神的环境，团队拥有多样化的经验。关键技术特性包括受 CI/CD 启发的Workflow、小型服务而非单体应用、强大的工程工具和开发者支持，以及一种不咎责任的文化。

他们提供医疗、牙科和视力保险计划、弹性休假、股票期权机会、跨职能学习和每月虚拟活动等福利和津贴。文章还警告存在冒充 EasyPost 的招聘诈骗，并敦促申请人保持警惕，并通过官方渠道验证任何可疑的职位邀请。

---

## 8. 展示 HN: AgentAPI – Claude Code、Goose、Aider 和 Codex 的 HTTP API

**原文标题**: Show HN: AgentAPI – HTTP API for Claude Code, Goose, Aider, and Codex

**原文链接**: [https://github.com/coder/agentapi](https://github.com/coder/agentapi)

AgentAPI 是一个 HTTP API，它允许对 Claude Code、Goose、Aider 和 Codex 等编码代理进行编程控制。它解决了通过基于终端的界面与这些代理交互的难题，提供了一种统一的方式来构建聊天界面、创建多代理系统和自动化代码审查流程。

该工具可以通过预构建的二进制文件安装，也可以使用 Go 从源代码构建。它提供了 CLI 命令来运行代理服务器 (`agentapi server`) 和连接到正在运行的代理的终端会话 (`agentapi attach`)。该服务器公开了一个 OpenAPI 模式和文档 UI。

主要功能包括：

*   **API 端点：** `/messages` (获取历史记录), `/message` (发送消息), `/status` (获取状态), `/events` (SSE 流).
*   **终端模拟：** 将 API 调用转换为终端击键。
*   **消息解析：** 将终端输出拆分为用户和代理消息，删除不需要的 TUI 元素。
*   **代理兼容性：** 适用于 Claude Code、Goose、Aider 和 Codex，并具有适应未来 TUI 更新的灵活性。

AgentAPI 的长期愿景是，要么因标准化官方 SDK 的出现而变得过时，要么在代理继续使用专有 API 的情况下，充当通用适配器。正在考虑的未来功能包括支持 MCP 和 Agent2Agent 协议。

---

## 9. HDR加持的表情符号

**原文标题**: HDR‑Infused Emoji

**原文链接**: [https://sharpletters.net/2025/04/16/hdr-emoji/](https://sharpletters.net/2025/04/16/hdr-emoji/)

本文解释了如何在Slack中创建HDR（高动态范围）表情符号。作者指出，这些HDR表情符号以增强的亮度渲染，使其在视觉上引人注目，尤其是在支持HDR显示的硬件上。

HDR表情符号的创建过程涉及使用`imagemagick`来处理图像。具体来说，该脚本执行以下操作：

1. 将图像的色彩空间调整为RGB。
2. 应用自动伽马校正。
3. 乘以并幂运算图像值以增加亮度。乘法因子需要根据源图像进行调整。
4. 将色彩空间转换回sRGB。
5. 将颜色深度调整为16位。
6. 应用2020\_profile.icc颜色配置文件。

文章强调HDR表情符号的支持并不普遍。它在Chrome和Slack中运行良好，但在很大程度上与Safari和Android设备不兼容。建议用户在Slack中测试表情符号，以验证它们在不同平台上的渲染效果。一个关键要求是在执行`imagemagick`脚本的工作目录中拥有`2020_profile.icc`文件。

---

## 10. Zoom宕机因意外“关闭”zoom.us域名导致。

**原文标题**: Zoom outage caused by accidental 'shutting down' of the zoom.us domain

**原文链接**: [https://status.zoom.us/incidents/pw9r9vnq5rvk](https://status.zoom.us/incidents/pw9r9vnq5rvk)

2025年4月16日，Zoom遭遇中断，影响了包括Zoom Meetings、Zoom Phone、Zoom Contact Center和Zoom网站在内的多项服务。根本原因是Zoom的域名注册商Markmonitor与GoDaddy Registry之间发生通信错误。此错误导致GoDaddy Registry错误地屏蔽了zoom.us域名，使其在东部时间下午2:25至下午4:12之间无法访问。

Zoom、Markmonitor和GoDaddy迅速采取行动，确定并解决了问题，恢复了zoom.us域名的服务。Zoom澄清说，中断并非由于任何产品故障、安全漏洞、网络问题或分布式拒绝服务(DDoS)攻击所致。

恢复后，Zoom建议遇到连接问题的用户刷新其DNS缓存，并为Windows和Mac用户提供了执行此操作的说明。GoDaddy和Markmonitor正在合作以防止未来发生类似事件。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 2 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 3 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 4 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 5 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 6 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 7 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 8 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 9 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 10 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 11 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 12 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 13 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 14 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 15 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 16 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 17 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 18 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 19 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 20 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 21 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 22 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 23 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 24 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 25 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 26 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 27 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 28 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 29 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
