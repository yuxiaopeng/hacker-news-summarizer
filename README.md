# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-15.md)

*最后自动更新时间: 2026-06-15 21:02:23*
## 1. Iroh 1.0

**原文标题**: Iroh 1.0

**原文链接**: [https://www.iroh.computer/blog/v1](https://www.iroh.computer/blog/v1)

Iroh 正式发布 1.0 版本，标志着其网络库的首个稳定版问世。该库旨在将互联网的抽象层从 IP 地址转向公钥。通过“拨号密钥而非 IP”，Iroh 确保设备无论网络环境、防火墙或物理位置如何变化，都能保持安全的寻址与连接。

1.0 版本的核心特性与技术里程碑包括：

*   **基于密钥的寻址：** 公钥作为稳定的标识符，简化了身份验证、权限管理和归属识别，同时允许设备在不同网络间切换而不会中断连接。
*   **高效性与 NAT 穿透：** Iroh 利用自定义的 QUIC 多路径和 NAT 穿透技术建立直接的点对点连接。这使得约 95% 的数据在设备间直接传输，从而降低了延迟和出站流量成本。
*   **广泛的兼容性：** 该库支持本地优先配置（无互联网连接亦可工作），可编译为 WASM 供浏览器使用，并支持蓝牙、LoRa 和 Tor 等自定义传输协议。
*   **扩展的语言支持：** 除了核心的 Rust 实现，Iroh 1.0 还新增了对 Python、Node.js、Swift 和 Kotlin 的官方支持，实现在移动端和桌面端应用的无缝集成。
*   **稳定性保证：** 1.0 版本承诺传输协议和 API 的稳定性。团队还建立了正式的支持周期，维护公共中继服务器，并为旧版本（特别是 v0.35x）用户提供迁移路径。

Iroh 已在数百万台设备上运行，应用场景涵盖大语言模型（LLM）训练到安全聊天等。对于希望构建去中心化、安全且高效的网络应用程序的开发者，Iroh 1.0 提供了一个成熟且生产就绪的技术栈。

---

## 2. TinyWind：具备真实风力物理系统的像素海盗航海游戏（累计航行里程超38万公里）

**原文标题**: TinyWind: A pixel pirate sailing game with real wind physics (380k+ kms sailed)

**原文链接**: [https://tinywind.io](https://tinywind.io)

**TinyWind** 是一款像素风格的海盗航海游戏，其独特之处在于采用了**真实的物理风力系统**。与传统的街机风格游戏不同，该游戏的核心玩法侧重于通过掌握真实的受风机制，来应对海上航行的技术性挑战。

该游戏获得了极高的社区参与度，玩家在游戏中的累计航行里程已超过 **38 万公里**。TinyWind 将复古美学与物理仿真相结合，为热衷于海洋探索和航海精妙技巧的玩家提供了独特的体验。

---

## 3. 领英职位邀约中的后门

**原文标题**: A backdoor in a LinkedIn job offer

**原文链接**: [https://roman.pt/posts/linkedin-backdoor/](https://roman.pt/posts/linkedin-backdoor/)

本文详细介绍了一场伪装成 LinkedIn 招聘邀约的针对性社会工程学攻击。作者曾接到一家加密货币初创公司“招聘人员”的联系，对方要求其审查一个 GitHub 仓库，以协助解决“过时的 Node 模块”问题。

**攻击机制**
由于怀疑其中有诈，作者在沙盒环境中分析了代码。他们发现 `app/test/index.js` 中隐藏了一个伪装成粗糙测试套件的后门。为了规避简单的字符串搜索，恶意代码通过碎片拼接成一个远程 URL（`https://rest-icon-handler.store/icons/77`）。

该陷阱利用了 `package.json` 文件中的 `prepare` 脚本。在 Node.js 中，当用户执行 `npm install` 时，该脚本会自动运行。通过诱导开发人员安装依赖，攻击者可以强制受害者机器从其服务器获取并执行任意恶意载荷。

**身份盗用**
攻击者使用了复杂的冒充手段：
*   **GitHub：** 仓库的提交历史伪造了一名真实且无关的全栈工程师的姓名和邮箱。
*   **LinkedIn：** 招聘者的个人资料属于一名真实的艺术记者。当作者假称遇到安装问题时，“招聘人员”立即从非技术人设切换到提供专家级的 Node.js 故障排除指导，以此向作者施压并诱导其运行代码。

**核心总结**
作者强调，这类攻击极具迷惑性，往往利用真实专业人士的声誉进行背书。作者建议保持高度的安全防范意识，例如在审查不明来源的代码时，应使用一次性 VPS 环境和只读分析工具（如受限模式下的 AI 工具），因为即使是经验丰富的开发人员，在“疲惫或匆忙”时也可能中招。

---

## 4. 我的家庭实验室 AI 开发平台

**原文标题**: My Homelab AI Dev Platform

**原文链接**: [https://rsgm.dev/post/ai-dev-platform/](https://rsgm.dev/post/ai-dev-platform/)

作者描述了其构建的一个 AI 驱动开发平台，旨在简化家庭实验室（Homelab）中各种 Docker 服务的管理。通过将 OpenCode（一款与厂商无关的 Web IDE）与 GitOps 工作流相结合，作者将耗时的手动维护流程转变为高效的自动化流程。

**关键组件与配置：**
*   **基础设施：** 该方案在 TrueNAS 主机的专用虚拟机上将 OpenCode 作为 systemd 单元运行。这提供了一个持久且适配移动端的 Web UI，用于编写代码和访问终端。
*   **GitOps 集成：** 约有 12 个 Docker Compose 堆栈被迁移至 Arcane 以实现基于 Git 的管理。一旦更改合并，部署将自动执行。
*   **安全与防护措施：** 为最小化“爆炸半径”（潜在风险范围），AI 拥有专属的 Git 用户，且仅限推送至功能分支。它无法直接推送至部署分支或访问运行中的服务。通过“人工干预”机制，确保所有 AI 生成的代码在合并前都经过拉取请求（PR）的审核。

**优势：**
*   **高效：** 以前需要数小时的任务（如研究版本说明中的重大变更，或追踪跨堆栈的网络连通性），现在利用 AI 摘要和自动更新，仅需几分钟即可完成。
*   **提升可靠性：** 作者利用 AI 系统地为容器添加了健康检查，使识别问题变得更加容易。
*   **灵活性：** OpenCode 基于 Web 的特性允许作者在电脑上发起更改，并通过手机审查或合并 PR。

**挑战：**
主要的局限在于缺乏 CI 反馈。由于 Forgejo 不通过公开 API 提供 Action 日志，AI 目前还无法自动诊断测试失败或 Linter 错误，而作者认为这一功能在 GitHub 等其他环境中非常实用。

**总结：**
总体而言，该平台提供了一种可扩展且安全的方式，在利用 AI 管理复杂家庭基础设施的同时，保持了严格的管理控制。

---

## 5. Game Engine White Papers Commander Keen

**原文标题**: Game Engine White Papers Commander Keen

**原文链接**: [https://forgottenbytes.net/commander_keen.html](https://forgottenbytes.net/commander_keen.html)

生成摘要时出错

---

## 6. How TimescaleDB compresses time-series data

**原文标题**: How TimescaleDB compresses time-series data

**原文链接**: [https://roszigit.com/en/blog/timescaledb-compression-hypercore](https://roszigit.com/en/blog/timescaledb-compression-hypercore)

生成摘要时出错

---

## 7. Factoring "short-sleeve" RSA keys with polynomials

**原文标题**: Factoring "short-sleeve" RSA keys with polynomials

**原文链接**: [https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/](https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/)

生成摘要时出错

---

## 8. Hetzner Price Adjustment

**原文标题**: Hetzner Price Adjustment

**原文链接**: [https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers)

生成摘要时出错

---

## 9. Show HN: Fata – Spaced repetition to fight skill rot from AI coding

**原文标题**: Show HN: Fata – Spaced repetition to fight skill rot from AI coding

**原文链接**: [https://fata.dev](https://fata.dev)

生成摘要时出错

---

## 10. Making glass-to-metal seals for home­made vacuum tubes

**原文标题**: Making glass-to-metal seals for home­made vacuum tubes

**原文链接**: [https://maurycyz.com/projects/glass/1/](https://maurycyz.com/projects/glass/1/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 2 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 3 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 4 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 5 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 6 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 7 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 8 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 9 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 10 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 11 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 12 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 13 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 14 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 15 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 16 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 17 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 18 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 19 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 20 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 21 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 22 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 23 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 24 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 25 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 26 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 27 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 28 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 29 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 30 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 31 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 32 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 33 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 34 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 35 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 36 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 37 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 38 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 39 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 40 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 41 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 42 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 43 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 44 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 45 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 46 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 47 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 48 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 49 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 50 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 51 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 52 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 53 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 54 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 55 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 56 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 57 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 58 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 59 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 60 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 61 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 62 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 63 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 64 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 65 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 66 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 67 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 68 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 69 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 70 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 71 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 72 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 73 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 74 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 75 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 76 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 77 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 78 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 79 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 80 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 81 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 82 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 83 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 84 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 85 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 86 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 87 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 88 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 89 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 90 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 91 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 92 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 93 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 94 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 95 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 96 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 97 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 98 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 99 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 100 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 101 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 102 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 103 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 104 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 105 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 106 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 107 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 108 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 109 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 110 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 111 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 112 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 113 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 114 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 115 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 116 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 117 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 118 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 119 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 120 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 121 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 122 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 123 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 124 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 125 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 126 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 127 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 128 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 129 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 130 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 131 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 132 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 133 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 134 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 135 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 136 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 137 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 138 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 139 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 140 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 141 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 142 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 143 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 144 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 145 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 146 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 147 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 148 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 149 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 150 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 151 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 152 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 153 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 154 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 155 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 156 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 157 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 158 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 159 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 160 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 161 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 162 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 163 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 164 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 165 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 166 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 167 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 168 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 169 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 170 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 171 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 172 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 173 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 174 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 175 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 176 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 177 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 178 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 179 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 180 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 181 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 182 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 183 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 184 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 185 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 186 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 187 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 188 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 189 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 190 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 191 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 192 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 193 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 194 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 195 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 196 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 197 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 198 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 199 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 200 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 201 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 202 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 203 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 204 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 205 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 206 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 207 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 208 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 209 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 210 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 211 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 212 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 213 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 214 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 215 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 216 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 217 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 218 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 219 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 220 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 221 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 222 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 223 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 224 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 225 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 226 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 227 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 228 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 229 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 230 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 231 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 232 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 233 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 234 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 235 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 236 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 237 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 238 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 239 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 240 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 241 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 242 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 243 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 244 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 245 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 246 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 247 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 248 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 249 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 250 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 251 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 252 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 253 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 254 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 255 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 256 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 257 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 258 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 259 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 260 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 261 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 262 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 263 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 264 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 265 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 266 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 267 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 268 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 269 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 270 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 271 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 272 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 273 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 274 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 275 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 276 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 277 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 278 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 279 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 280 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 281 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 282 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 283 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 284 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 285 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 286 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 287 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 288 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 289 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 290 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 291 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 292 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 293 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 294 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 295 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 296 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 297 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 298 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 299 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 300 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 301 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 302 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 303 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 304 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 305 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 306 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 307 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 308 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 309 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 310 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 311 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 312 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 313 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 314 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 315 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 316 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 317 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 318 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 319 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 320 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 321 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 322 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 323 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 324 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 325 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 326 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 327 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 328 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 329 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 330 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 331 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 332 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 333 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 334 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 335 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 336 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 337 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 338 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 339 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 340 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 341 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 342 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 343 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 344 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 345 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 346 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 347 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 348 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 349 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 350 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 351 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 352 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 353 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 354 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 355 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 356 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 357 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 358 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 359 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 360 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 361 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 362 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 363 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 364 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 365 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 366 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 367 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 368 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 369 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 370 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 371 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 372 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 373 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 374 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 375 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 376 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 377 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 378 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 379 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 380 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 381 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 382 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 383 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 384 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 385 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 386 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 387 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 388 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 389 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 390 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 391 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 392 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 393 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 394 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 395 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 396 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 397 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 398 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 399 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 400 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 401 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 402 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 403 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 404 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 405 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 406 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 407 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 408 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 409 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 410 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 411 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 412 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 413 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 414 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 415 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 416 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 417 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 418 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 419 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 420 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 421 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 422 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 423 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 424 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 425 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 426 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 427 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 428 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 429 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 430 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 431 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 432 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 433 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 434 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 435 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 436 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 437 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 438 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 439 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 440 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 441 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 442 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 443 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 444 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 445 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 446 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 447 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 448 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 449 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 450 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 451 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 452 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
