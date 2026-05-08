# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-08.md)

*最后自动更新时间: 2026-05-08 18:37:11*
## 1. Google Cloud Fraud Defence 只是重新包装后的 WEI。

**原文标题**: Google Cloud Fraud Defence is just WEI repackaged

**原文链接**: [https://privatecaptcha.com/blog/google-cloud-fraud-defence-wei/](https://privatecaptcha.com/blog/google-cloud-fraud-defence-wei/)

文章指出，谷歌于 2026 年 5 月推出的“谷歌云欺诈防御”（Google Cloud Fraud Defense）是其备受争议的“网络环境完整性”（Web Environment Integrity，简称 WEI）提案的战略性更名。该提案曾于 2023 年因公众强烈抗议而被废弃。

该系统采用二维码挑战机制，要求用户通过智能手机验证真人身份。然而，作者揭示其底层机制依赖于“设备验证”（device attestation，特别是谷歌的 Play Integrity API）。这强制要求使用“经过认证”的硬件和软件，从而实际上排除了 GrapheneOS 等注重隐私的操作系统、LineageOS 等开源替代方案，以及 Firefox 等拒绝此类追踪的浏览器。

作者列举了四大核心担忧：
1.  **准入门槛化：** 它将开放的网络转变为“围墙花园”，访问权限以谷歌或苹果认证的硬件为前提，剥夺了互联网“硬件无关”的特性。
2.  **持久追踪：** 通过将网络访问与稳定的硬件身份绑定，谷歌能够跨会话、浏览器和私密模式追踪用户，建立永久性的归因踪迹。
3.  **安全风险：** 二维码的使用会诱导用户养成盲目扫码访问网站的习惯，作者警告称，这很快就会被网络钓鱼攻击所利用。
4.  **缺乏实效：** 该系统未能达成其首要目标；专业僵尸网络（bot farms）可以利用廉价的现成安卓设备和基础的摄像头自动化技术轻松绕过检查。

文章总结道，尽管存在如“工作量证明”（proof-of-work）等保护隐私的替代方案，但谷歌选择了一条优先考虑生态控制和数据收集的道路。通过绕过曾阻挠 WEI 的标准制定机构，谷歌正打着验证码更新的幌子，成功实施由硬件把关的互联网。

---

## 2. 卡通频道 Flash 游戏

**原文标题**: Cartoon Network Flash Games

**原文链接**: [https://www.webdesignmuseum.org/flash-game-exhibitions/cartoon-network-flash-games](https://www.webdesignmuseum.org/flash-game-exhibitions/cartoon-network-flash-games)

本条目介绍了**2001年**发布的Flash网页游戏《**史酷比：史酷比快照**》（Scooby-Doo: Scooby Snapshot）。作为**Cartoon Network Flash游戏**系列的一部分，它代表了21世纪初利用在线游戏推广热门动画系列的时代。该游戏曾在Cartoon Network官方网站上线，让粉丝们能够通过浏览器与《史酷比》系列作品进行互动。

---

## 3. Serving a Website on a Raspberry Pi Zero Running in RAM

**原文标题**: Serving a Website on a Raspberry Pi Zero Running in RAM

**原文链接**: [https://btxx.org/posts/memory/](https://btxx.org/posts/memory/)

生成摘要时出错

---

## 4. Meshtastic 简介

**原文标题**: An Introduction to Meshtastic

**原文链接**: [https://meshtastic.org/docs/introduction/](https://meshtastic.org/docs/introduction/)

Meshtastic 是一个开源、由社区驱动的项目，利用廉价的 LoRa（远距离）无线电硬件实现远距离、离网通信。它旨在无需蜂窝塔或互联网等现有基础设施的情况下运行，非常适合通信不稳定或缺失的地区。

**工作原理**
该系统利用在大多数地区无需授权的 LoRa 协议。网络中的每台无线电设备都充当一个节点，负责转发接收到的消息，从而构建一个去中心化的网状网络。通过在设备间跳转直至到达目的地，这确保了消息能够进行远距离传输——目前已有 331 公里的确认记录。

**核心特性**
*   **去中心化与加密：** 无需中央路由器，所有通信均安全加密。
*   **高效性：** 设备具有出色的电池续航表现，支持文本消息以及可选的 GPS 位置追踪。
*   **易用性：** 无线电设备既可独立工作，也可与智能手机配对（每台设备供一名用户使用），以提供直观的消息交互界面。

**社区与支持**
由于 Meshtastic 完全基于志愿者运作，项目的发展依赖于社区贡献。其代码库和文档在 GitHub 上维护，并通过 Discord 和社区论坛提供支持。我们鼓励新用户查阅“入门指南”，并为不断更新的项目文档做出贡献，以帮助优化他人的使用体验。

---

## 5. PC Engine 中央处理器

**原文标题**: PC Engine CPU

**原文链接**: [https://jsgroth.dev/blog/posts/pc-engine-cpu/](https://jsgroth.dev/blog/posts/pc-engine-cpu/)

本文提供了 PC Engine (TurboGrafx-16) 中央处理器 Hudson HuC6280 的技术概览。尽管该主机在北美以“16 位”作为品牌宣传，但其 CPU 实际上是一款基于 WDC 65C02 的 8 位芯片。其核心特征是速度：在 7.16 MHz 的主频下，它的实际运行速度是 SNES CPU 的两倍，且在访问大多数 ROM 和 RAM 时几乎没有内存延迟。

**核心技术特性：**
*   **内存管理：** HuC6280 内置了 MMU（内存管理单元），可将 16 位逻辑地址空间映射到 21 位（2 MB）的物理范围。它利用 8 个 8 KB 的“内存页寄存器”（MPR）进行银行切换，这使得大多数游戏卡带不再需要额外的映射硬件。
*   **内存映射：** 该系统配备了 8 KB 的内置工作 RAM，虽然远少于 Genesis 或 SNES，但这一缺陷通常通过 CD-ROM 扩展单元得到了弥补。
*   **增强指令集：** 该 CPU 引入了多项专用指令，最显著的是**块传输**指令（例如 TII、TAI），在缺乏专用 DMA 硬件的情况下，这些指令可实现快速的数据移动（每字节仅需 6 个周期）。其他新增功能还包括用于直接操作零页的 **SET** 指令、用于更新视频寄存器的 VDC 专用指令，以及用于编写位置无关代码的 **BSR**（分支到子程序）指令。

总结而言，虽然 PC Engine 缺乏 16 位寄存器和数学处理能力，但它通过高时钟频率和高效、现代化的 6502 架构弥补了不足。这使其能够填补 8 位与 16 位主机之间的代差，在性能表现上足以与世嘉 Genesis 和 SNES 等更复杂的系统相抗衡。

---

## 6. 一个展示浏览器在未经询问的情况下所透露的所有信息的网页。

**原文标题**: A web page that shows you everything the browser told it without asking

**原文链接**: [https://sinceyouarrived.world/taken](https://sinceyouarrived.world/taken)

《Since You Arrived Vol. IV》是由 Rise Up Labs 的 Matt 创建的一个实验性网络项目，旨在展示浏览器在未经用户同意的情况下，自动向网站披露的惊人数据量。作为将关注焦点从全球事件逐步转向个人用户的系列作品之一，本卷是对现代网络标准的批判。

该页面利用标准的 JavaScript API（而非黑客手段或漏洞利用）来获取信息，例如用户的地理位置、IP 地址、硬件规格（GPU、CPU 核心数、电池状态）以及系统偏好（字体、语言、屏幕尺寸）。它强调了“字体和画布指纹”等技术如何生成唯一的数字画像，使得网站即使在不使用 Cookie 的情况下也能在互联网上追踪个人。

该项目的一个核心主题是“设计问题”。作者指出，虽然这个特定页面是透明且符合伦理的——使用手写文字而非 AI 生成，不存储任何数据，并拒绝运行诸如登录检测或剪贴板访问之类的侵入性脚本——但大多数其他网站并非如此。为了直观展示这种数字签名，页面会根据访客特定的设备遥测数据生成一个唯一的条形码。

项目最后强调了其自身的数据极简主义：它仅向服务器发送两个匿名事件（访问和完成），且不在用户设备上存储任何内容。通过揭示页面加载最初几毫秒内发生的“隐形”数据交换，《Vol. IV》敦促用户重新审视其数字隐私以及现代浏览方式固有的脆弱性。

---

## 7. 苹果与英特尔已达成初步芯片制造协议。

**原文标题**: Apple, Intel have reached preliminary chip-making deal

**原文链接**: [https://www.reuters.com/business/apple-intel-have-reached-preliminary-chip-making-deal-wsj-reports-2026-05-08/](https://www.reuters.com/business/apple-intel-have-reached-preliminary-chip-making-deal-wsj-reports-2026-05-08/)

无法访问文章链接。

---

## 8. 波兰现已跻身全球前20大经济体之列。

**原文标题**: Poland is now among the 20 largest economies

**原文链接**: [https://apnews.com/article/poland-economy-growth-g20-gdp-26fe06e120398410f8d773ba5661e7aa](https://apnews.com/article/poland-economy-growth-g20-gdp-26fe06e120398410f8d773ba5661e7aa)

Since the fall of communism in 1989, Poland has undergone a dramatic economic transformation, recently surpassing Switzerland to become the world’s 20th-largest economy with over $1 trillion in annual output. Once a nation defined by rationing and poverty, it is now recognized as a "European growth champion," with the Trump administration advocating for its inclusion in the G20.

Several key factors have driven this ascent:
*   **Institutional Stability:** Unlike other post-communist states, Poland established strong independent courts and regulatory agencies early on, preventing the rise of a corrupt oligarch class.
*   **EU Integration:** Joining the European Union in 2004 provided access to the single market and billions in development aid. Since then, Poland’s economy has grown at an average annual rate of 3.8%, far outpacing the EU average.
*   **Human Capital:** A post-communist boom in higher education means 50% of young Poles now hold degrees. This highly skilled but relatively affordable workforce has attracted significant foreign investment.
*   **Innovation:** The country is shifting from a manufacturing hub to a center for high-tech innovation, illustrated by leaders in green energy like Solaris (electric buses) and new investments in artificial intelligence and quantum computing.

Despite this success, challenges remain. Poland faces an aging population, a low birth rate, and the need to address urban-rural inequalities. However, with a per capita GDP that has risen from 38% of the EU average in 1990 to 85% today (roughly equal to Japan’s when adjusted for cost of living), Poland is increasingly seen as a land of opportunity, prompting many expatriates to return home to participate in its burgeoning tech sector.

---

## 9. Podman rootless containers and the Copy Fail exploit

**原文标题**: Podman rootless containers and the Copy Fail exploit

**原文链接**: [https://garrido.io/notes/podman-rootless-containers-copy-fail/](https://garrido.io/notes/podman-rootless-containers-copy-fail/)

生成摘要时出错

---

## 10. Show HN: Git for AI Agents

**原文标题**: Show HN: Git for AI Agents

**原文链接**: [https://github.com/regent-vcs/re_gent](https://github.com/regent-vcs/re_gent)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 2 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 3 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 4 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 5 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 6 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 7 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 8 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 9 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 10 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 11 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 12 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 13 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 14 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 15 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 16 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 17 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 18 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 19 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 20 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 21 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 22 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 23 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 24 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 25 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 26 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 27 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 28 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 29 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 30 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 31 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 32 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 33 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 34 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 35 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 36 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 37 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 38 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 39 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 40 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 41 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 42 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 43 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 44 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 45 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 46 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 47 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 48 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 49 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 50 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 51 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 52 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 53 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 54 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 55 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 56 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 57 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 58 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 59 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 60 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 61 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 62 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 63 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 64 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 65 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 66 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 67 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 68 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 69 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 70 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 71 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 72 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 73 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 74 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 75 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 76 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 77 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 78 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 79 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 80 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 81 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 82 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 83 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 84 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 85 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 86 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 87 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 88 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 89 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 90 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 91 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 92 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 93 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 94 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 95 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 96 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 97 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 98 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 99 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 100 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 101 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 102 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 103 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 104 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 105 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 106 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 107 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 108 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 109 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 110 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 111 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 112 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 113 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 114 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 115 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 116 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 117 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 118 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 119 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 120 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 121 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 122 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 123 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 124 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 125 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 126 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 127 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 128 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 129 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 130 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 131 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 132 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 133 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 134 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 135 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 136 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 137 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 138 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 139 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 140 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 141 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 142 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 143 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 144 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 145 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 146 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 147 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 148 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 149 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 150 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 151 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 152 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 153 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 154 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 155 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 156 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 157 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 158 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 159 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 160 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 161 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 162 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 163 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 164 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 165 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 166 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 167 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 168 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 169 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 170 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 171 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 172 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 173 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 174 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 175 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 176 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 177 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 178 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 179 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 180 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 181 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 182 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 183 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 184 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 185 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 186 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 187 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 188 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 189 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 190 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 191 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 192 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 193 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 194 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 195 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 196 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 197 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 198 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 199 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 200 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 201 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 202 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 203 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 204 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 205 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 206 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 207 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 208 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 209 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 210 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 211 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 212 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 213 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 214 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 215 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 216 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 217 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 218 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 219 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 220 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 221 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 222 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 223 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 224 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 225 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 226 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 227 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 228 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 229 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 230 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 231 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 232 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 233 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 234 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 235 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 236 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 237 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 238 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 239 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 240 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 241 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 242 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 243 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 244 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 245 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 246 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 247 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 248 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 249 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 250 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 251 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 252 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 253 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 254 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 255 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 256 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 257 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 258 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 259 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 260 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 261 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 262 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 263 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 264 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 265 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 266 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 267 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 268 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 269 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 270 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 271 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 272 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 273 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 274 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 275 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 276 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 277 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 278 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 279 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 280 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 281 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 282 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 283 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 284 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 285 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 286 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 287 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 288 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 289 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 290 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 291 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 292 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 293 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 294 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 295 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 296 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 297 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 298 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 299 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 300 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 301 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 302 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 303 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 304 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 305 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 306 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 307 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 308 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 309 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 310 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 311 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 312 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 313 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 314 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 315 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 316 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 317 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 318 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 319 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 320 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 321 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 322 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 323 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 324 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 325 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 326 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 327 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 328 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 329 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 330 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 331 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 332 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 333 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 334 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 335 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 336 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 337 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 338 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 339 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 340 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 341 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 342 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 343 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 344 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 345 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 346 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 347 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 348 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 349 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 350 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 351 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 352 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 353 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 354 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 355 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 356 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 357 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 358 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 359 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 360 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 361 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 362 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 363 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 364 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 365 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 366 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 367 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 368 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 369 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 370 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 371 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 372 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 373 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 374 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 375 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 376 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 377 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 378 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 379 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 380 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 381 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 382 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 383 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 384 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 385 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 386 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 387 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 388 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 389 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 390 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 391 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 392 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 393 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 394 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 395 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 396 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 397 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 398 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 399 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 400 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 401 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 402 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 403 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 404 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 405 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 406 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 407 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 408 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 409 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 410 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 411 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 412 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 413 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 414 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
