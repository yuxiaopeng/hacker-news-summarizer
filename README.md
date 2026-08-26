# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-26.md)

*最后自动更新时间: 2026-08-26 19:24:49*
## 1. GLM-5.3-Flash

**原文标题**: GLM-5.3-Flash

**原文链接**: [https://z.ai/blog/glm-5.3-flash](https://z.ai/blog/glm-5.3-flash)

无法访问文章链接。

---

## 2. 一起持续中的3D打印机AGPL协议违规事件

**原文标题**: An ongoing 3D-printer AGPL violation

**原文链接**: [https://lwn.net/SubscriberLink/1089390/46116614cc74b814/](https://lwn.net/SubscriberLink/1089390/46116614cc74b814/)

在 FOSSY 2026 大会上，软件自由保护协会（SFC）的代表详细阐述了 3D 打印机制造商拓竹科技（Bambu Lab）持续存在的许可证违规行为。该公司被指控违反了 AGPLv3（涉及其“Bambu Studio”切片软件）和 GPLv2（涉及其基于 Linux 的打印机固件）。

SFC 强调，拓竹科技采用了 AGPL 旨在防止的特定手段。这些手段包括发布仅含二进制文件的共享库，以及将关键软件功能迁移到仅能通过特定 User-Agent 字符串访问的专有服务器上。当社区成员对这些代码进行逆向工程时，拓竹科技发出了 DMCA 删帖通知。此外，尽管使用了基于 Buildroot 的 Linux，该公司仍未能提供其固件的相应源代码。

SFC 负责人 Bradley Kühn、Karen Sandler 和 Denver Gingerich 指出，虽然拓竹科技无视了合规请求，但这一局势引发了前所未有的维权热潮。3D 打印社区的积极参与促成了一场金额超过 25 万美元的成功筹款，使 SFC 能够聘请一名全职诉讼律师。

SFC 正在寻求多种维权途径，包括：
*   **社区行动：** 支持“baltobu”等项目，对专有组件进行逆向工程并开发替代方案。
*   **诉讼：** 探索传统的版权主张以及新颖的合同法途径，即通过将消费者视为 GPL 的“第三方受益人”来开展行动。

演讲者强调，软件许可证必须通过积极的执法才能产生实质意义。通过追究企业的责任，SFC 旨在纠正权力失衡，捍卫维修权，并确保 3D 打印的爱好者文化始终根植于软件自由。其目标是将此次违规事件转化为自由开源软件（FOSS）维权行动的一个里程碑式契机。

---

## 3. 尾猫

**原文标题**: Tailcat

**原文链接**: [https://github.com/tailscale/tailcat](https://github.com/tailscale/tailcat)

**Tailcat** 是 Tailscale 推出的一款开源命令行工具和 Go 语言库。它的功能类似于 `netcat`，但利用了 Tailscale 的数据平面，且无需其中心控制平面。它能在无需 Tailscale 账号、root/管理员权限或更改系统路由表的情况下，实现机器间点对点的 WireGuard 加密隧道。

**核心特性与功能：**
*   **连接性：** 它利用 Tailscale 的 **magicsock** 进行 NAT 穿透，并使用 **DERP** 中继作为引导侧信道和通信备选方案。
*   **用户态运行：** Tailcat 使用 **gVisor 的 Netstack** 完全在用户态运行，这意味着它在进程内部而非操作系统层面终止 TCP 连接。
*   **连接令牌：** 服务端生成一个带外“连接令牌”（包含公钥和 DERP 信息），客户端利用该令牌发起握手。
*   **多功能性：** 除了管道化标准输入/输出，它还支持 TCP 端口转发、受 WireGuard 保护的免密 SSH 服务、SOCKS5 代理以及出口节点功能。
*   **密钥管理：** 用户可以为一次性会话使用临时密钥，或使用保存的密钥以获得固定地址。通过 `--allow` 标志可以限制特定客户端的访问。

**技术组件：**
Tailcat 复用了多个 Tailscale 核心组件：用于加密的用户态 **WireGuard**、用于 UDP 打洞的 **magicsock** 以及用于加密中继的 **DERP**。虽然它默认使用 Tailscale 提供的免费且限流的中继服务器，但用户也可以托管自己的 DERP 中继以消除外部依赖。

**稳定性：**
Tailcat 目前处于实验阶段。其命令行界面（CLI）、Go API 或传输格式均不提供稳定性保证，且公共 DERP 中继按“尽力而为”原则提供，不设在线时间服务水平协议（SLA）。

---

## 4. AWS 收购 DuckLabs

**原文标题**: AWS Acquires DuckLabs

**原文链接**: [https://ducklabs.com/news/2026/08/26/ducklabs-to-join-aws](https://ducklabs.com/news/2026/08/26/ducklabs-to-join-aws)

热门开源分析型数据库 DuckDB 的幕后团队 DuckLabs 宣布，将于 2026 年 9 月加入亚马逊云科技（AWS）。

此次收购旨在利用 AWS 的基础设施和资源，将包含 DuckDB、DuckLake 和 Quack 在内的“Duck Stack”推向全球受众。创始人 Mark Raasveldt 和 Hannes Mühleisen 指出，尽管 DuckLabs 作为一家日均下载量超过 100 万次的自筹资金公司已取得成功，但加入 AWS 可以避免团队成为项目快速发展的瓶颈。

**此次过渡的核心要点包括：**

*   **开源承诺：** DuckDB 及其相关项目将继续在 MIT 许可证下保持免费和开源。非营利性的 DuckDB 基金会将继续独立管理这些项目，以确保供应商的中立性。
*   **团队延续性：** DuckLabs 团队将继续留在阿姆斯特丹，专注于技术研发，而非独立扩展业务所带来的运营障碍。
*   **未来扩展：** AWS 计划将 DuckDB 技术整合到新的数据服务中。此外，DuckDB 基金会将成立技术咨询委员会，并开放其扩展栈，允许第三方开发者运行经过签名的扩展程序。
*   **行业支持：** 此举得到了 AWS 领导层以及 MotherDuck 和 Fivetran 等合作伙伴的支持。他们认为，这次收购在保持软件“可灵活扩展”（hackable）特性的同时，将加速技术创新。

最后，创始人强调，这一举措在保护社区信任的同时，也为开启数据分析的新纪元提供了必要的稳定性和影响力。

---

## 5. 研究显示联合健康集团的利润率是其声称的四倍 [pdf]

**原文标题**: Study Reveals UnitedHealth's Profit Margins Four Times What It Claimed [pdf]

**原文链接**: [https://insurancewatchdogcoalition.com/wp-content/uploads/2026/08/UHG-Profits-Study_August-2026.pdf](https://insurancewatchdogcoalition.com/wp-content/uploads/2026/08/UHG-Profits-Study_August-2026.pdf)

生成摘要时出错

---

## 6. 部分 GitHub 服务出现异常

**原文标题**: Disruption with Some GitHub Services

**原文链接**: [https://www.githubstatus.com/incidents/hcbtzksccj2f](https://www.githubstatus.com/incidents/hcbtzksccj2f)

2026年8月26日，GitHub 遭遇了一次服务中断，影响了旗下多项服务的性能。该事件始于 UTC 时间约 15:09，当时 GitHub 开始对性能下降的报告展开调查。

截至 UTC 时间 16:07，问题已正式解决。GitHub 对用户的耐心表示感谢，并宣布将在最终确定后分享详细的根本原因分析（RCA）。摘要中未点名具体受影响的服务，但指出此次中断波及了 GitHub 的“部分”功能。

---

## 7. 星云无衬线体

**原文标题**: Nebula Sans

**原文链接**: [https://www.nebulasans.com](https://www.nebulasans.com)

**Nebula Sans** is a modern, humanist sans-serif typeface created for Nebula, the independent creator-driven streaming service. Designed as a drop-in replacement for their previous brand font, Whitney SSm, Nebula Sans is based on Adobe’s **Source Sans** by Paul D. Hunt and is released for free under the SIL Open Font License.

The transition to a custom typeface was motivated by three primary factors:
1.  **Sustainability:** Eliminating the rising costs of commercial licensing as the platform grows.
2.  **Personalization:** Aligning the font’s aesthetics more closely with brand preferences.
3.  **Features:** Integrating advanced typographic tools tailored to their specific digital needs.

Technically, Nebula Sans adjusts the metrics of Source Sans to match the larger, wider profile of Whitney SSm. It features six weights—Light, Book, Medium, Semibold, Bold, and Black—along with corresponding italics. Key design elements include:
*   **Tabular Figures:** Monospaced numerals that ensure timestamps in video players remain stable.
*   **Stylistic Alternates:** Options for a single-story ‘a’, open ‘g’, and tailed ‘l’.
*   **Enhanced Punctuation:** Utilizing "curly" glyphs rather than straight marks for a more elegant aesthetic.
*   **Custom Asterisk:** A unique glyph designed to reflect the stars in the Nebula logo.

Nebula Sans is optimized for legibility across digital interfaces and print, offering a versatile, neutral aesthetic for both creators and the general public.

---

## 8. The Tariff Cost: analysis of the costs to Americans from new tariffs on Canada

**原文标题**: The Tariff Cost: analysis of the costs to Americans from new tariffs on Canada

**原文链接**: [https://thetariffcost.com/](https://thetariffcost.com/)

生成摘要时出错

---

## 9. Qwen3.8-Flash-Next

**原文标题**: Qwen3.8-Flash-Next

**原文链接**: [https://qwen.ai/blog?id=qwen3.8-flash-next](https://qwen.ai/blog?id=qwen3.8-flash-next)

The provided text, titled **"Qwen3.8-Flash-Next,"** contains only the single word **"Qwen"** in its body.

Because the content lacks descriptive detail, data, or context, a comprehensive summary of features or technical specifications is not possible. However, based on the title, the information suggests a focus on a specific, likely next-generation iteration of the Qwen language model series. The "Flash" designation typically indicates a model optimized for high-speed inference and low latency, while "3.8" likely refers to a version number or parameter scale.

In its current form, the article acts as a placeholder or a brief identification of the Qwen brand without providing any further insights.

---

## 10. Tim Curry has died

**原文标题**: Tim Curry has died

**原文链接**: [https://www.theguardian.com/film/2026/aug/26/tim-curry-dies-rocky-horror-show-stephen-king-it-legend-film](https://www.theguardian.com/film/2026/aug/26/tim-curry-dies-rocky-horror-show-stephen-king-it-legend-film)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 2 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 3 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 4 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 5 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 6 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 7 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 8 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 9 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 10 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 11 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 12 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 13 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 14 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 15 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 16 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 17 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 18 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 19 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 20 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 21 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 22 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 23 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 24 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 25 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 26 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 27 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 28 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 29 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 30 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 31 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 32 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 33 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 34 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 35 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 36 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 37 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 38 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 39 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 40 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 41 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 42 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 43 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 44 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 45 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 46 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 47 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 48 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 49 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 50 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 51 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 52 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 53 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 54 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 55 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 56 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 57 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 58 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 59 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 60 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 61 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 62 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 63 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 64 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 65 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 66 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 67 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 68 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 69 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 70 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 71 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 72 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 73 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 74 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 75 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 76 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 77 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 78 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 79 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 80 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 81 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 82 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 83 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 84 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 85 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 86 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 87 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 88 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 89 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 90 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 91 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 92 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 93 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 94 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 95 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 96 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 97 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 98 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 99 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 100 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 101 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 102 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 103 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 104 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 105 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 106 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 107 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 108 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 109 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 110 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 111 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 112 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 113 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 114 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 115 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 116 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 117 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 118 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 119 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 120 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 121 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 122 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 123 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 124 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 125 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 126 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 127 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 128 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 129 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 130 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 131 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 132 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 133 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 134 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 135 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 136 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 137 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 138 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 139 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 140 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 141 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 142 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 143 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 144 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 145 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 146 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 147 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 148 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 149 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 150 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 151 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 152 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 153 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 154 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 155 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 156 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 157 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 158 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 159 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 160 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 161 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 162 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 163 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 164 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 165 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 166 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 167 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 168 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 169 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 170 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 171 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 172 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 173 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 174 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 175 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 176 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 177 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 178 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 179 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 180 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 181 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 182 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 183 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 184 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 185 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 186 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 187 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 188 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 189 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 190 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 191 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 192 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 193 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 194 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 195 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 196 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 197 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 198 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 199 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 200 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 201 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 202 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 203 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 204 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 205 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 206 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 207 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 208 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 209 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 210 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 211 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 212 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 213 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 214 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 215 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 216 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 217 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 218 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 219 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 220 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 221 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 222 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 223 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 224 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 225 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 226 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 227 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 228 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 229 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 230 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 231 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 232 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 233 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 234 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 235 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 236 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 237 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 238 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 239 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 240 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 241 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 242 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 243 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 244 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 245 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 246 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 247 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 248 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 249 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 250 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 251 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 252 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 253 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 254 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 255 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 256 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 257 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 258 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 259 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 260 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 261 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 262 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 263 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 264 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 265 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 266 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 267 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 268 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 269 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 270 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 271 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 272 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 273 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 274 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 275 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 276 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 277 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 278 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 279 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 280 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 281 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 282 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 283 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 284 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 285 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 286 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 287 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 288 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 289 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 290 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 291 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 292 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 293 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 294 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 295 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 296 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 297 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 298 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 299 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 300 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 301 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 302 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 303 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 304 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 305 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 306 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 307 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 308 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 309 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 310 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 311 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 312 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 313 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 314 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 315 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 316 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 317 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 318 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 319 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 320 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 321 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 322 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 323 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 324 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 325 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 326 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 327 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 328 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 329 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 330 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 331 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 332 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 333 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 334 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 335 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 336 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 337 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 338 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 339 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 340 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 341 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 342 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 343 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 344 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 345 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 346 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 347 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 348 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 349 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 350 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 351 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 352 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 353 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 354 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 355 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 356 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 357 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 358 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 359 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 360 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 361 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 362 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 363 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 364 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 365 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 366 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 367 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 368 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 369 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 370 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 371 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 372 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 373 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 374 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 375 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 376 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 377 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 378 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 379 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 380 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 381 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 382 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 383 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 384 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 385 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 386 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 387 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 388 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 389 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 390 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 391 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 392 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 393 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 394 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 395 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 396 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 397 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 398 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 399 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 400 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 401 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 402 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 403 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 404 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 405 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 406 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 407 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 408 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 409 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 410 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 411 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 412 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 413 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 414 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 415 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 416 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 417 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 418 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 419 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 420 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 421 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 422 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 423 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 424 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 425 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 426 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 427 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 428 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 429 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 430 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 431 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 432 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 433 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 434 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 435 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 436 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 437 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 438 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 439 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 440 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 441 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 442 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 443 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 444 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 445 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 446 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 447 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 448 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 449 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 450 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 451 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 452 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 453 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 454 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 455 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 456 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 457 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 458 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 459 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 460 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 461 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 462 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 463 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 464 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 465 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 466 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 467 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 468 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 469 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 470 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 471 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 472 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 473 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 474 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 475 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 476 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 477 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 478 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 479 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 480 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 481 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 482 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 483 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 484 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 485 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 486 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 487 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 488 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 489 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 490 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 491 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 492 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 493 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 494 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 495 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 496 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 497 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 498 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 499 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 500 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 501 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 502 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 503 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 504 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 505 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 506 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 507 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 508 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 509 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 510 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 511 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 512 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 513 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 514 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 515 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 516 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 517 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 518 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 519 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 520 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 521 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 522 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 523 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
