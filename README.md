# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-02.md)

*最后自动更新时间: 2026-07-02 19:04:16*
## 1. 自 Linux 6.9 起，LUKS 挂起不再从内存中擦除磁盘加密密钥。

**原文标题**: Since Linux 6.9, LUKS suspend stopped wiping disk-encryption keys from memory

**原文链接**: [https://mathstodon.xyz/@iblech/116769502749142438](https://mathstodon.xyz/@iblech/116769502749142438)

自 Linux 内核 6.9 版本发布以来，LUKS 磁盘加密领域发现了一个重大的安全回归问题。正如研究人员 Ingo Blechschmidt 所指出的，即使在进行了专门配置的情况下，内核在系统进入挂起（suspend）模式时，也无法再成功从内存（RAM）中清除加密密钥。

**问题详情**
此前，注重安全的用户通常可以利用 `cryptsetup` 和 `systemd` 启用相关功能，在系统睡眠期间从内存中逐出敏感加密密钥。此举旨在防御“冷启动攻击”，防止攻击者通过物理手段从挂起设备的内存中提取密钥来解密驱动器。然而，由于 6.9 和 6.10 版本内核在挂起过渡期间处理任务和内存的方式发生了变化，导致该清除过程失败或被绕过。

**安全影响**
这一故障意味着当计算机处于睡眠状态时，加密密钥仍驻留在易失性内存中。如果笔记本电脑在挂起状态下被盗或被他人访问，全盘加密将形同虚设，因为解锁数据所需的密钥仍保留在硬件中。

**现状与缓解措施**
该回归问题影响了依赖“挂起到内存（suspend-to-RAM）”安全工作流的用户。Linux 社区已对此进行了广泛讨论，开发人员正致力于通过补丁恢复预期的安全行为。建议用户关注其发行版的内核更新，并升级到已集成修复程序的版本（例如最近发布的 6.11 或 6.10.x 后期稳定版）。在此期间，使用“休眠”（挂起到磁盘）而非“挂起”（到内存）是更安全的替代方案，因为休眠会完全关闭系统电源并清空内存。

---

## 2. PeerTube 是一个自由、去中心化且联邦化的视频平台。

**原文标题**: PeerTube is a free, decentralized and federated video platform

**原文链接**: [https://github.com/Chocobozzz/PeerTube](https://github.com/Chocobozzz/PeerTube)

PeerTube 是一个由法国非营利组织 Framasoft 开发的自由、开源且去中心化的视频平台。作为 YouTube 和 Vimeo 等中心化服务的道德替代方案，PeerTube 采用联邦模式运行。它由一个独立且可互操作的实例网络组成，这些实例通过 ActivityPub 协议进行通信，使其能够与更广泛的“联邦宇宙”（Fediverse，包括 Mastodon 等平台）相集成。

**核心功能：**
*   **P2P 流媒体：** PeerTube 利用 WebRTC 技术在观众之间实现点对点共享，从而减轻单个服务器的带宽负载。这使得小型实例也能高效地承载热门内容。
*   **隐私与自主：** 该平台由社区所有且无广告。它杜绝了数据挖掘、“暗黑模式”的用户体验设计以及操纵性的推荐算法。
*   **创作者支持：** 创作者可以上传视频、开启永久直播，并通过 RSS 或联邦账号与粉丝互动。该平台不依赖广告收入，而是鼓励通过内置的捐赠链接获得观众的直接支持。
*   **高度定制：** 用户和管理员都能对其使用体验拥有极高的控制权，包括自定义界面、修改主题以及设定特定的审核政策。

**技术与社区层面：**
PeerTube 构建于透明、社区驱动的模型之上。它鼓励从代码编写、漏洞报告到翻译和文档编制等各种形式的贡献。对于希望搭建自有实例的用户，该项目提供了详尽的文档、REST API 以及适用于 Docker 和 YunoHost 等平台的社区软件包。该软件采用 GNU Affero 通用公共许可证（AGPLv3）授权，确保平台始终对所有人保持自由与开放。

---

## 3. Android Developer Verification: Threat masquerading as protection

**原文标题**: Android Developer Verification: Threat masquerading as protection

**原文链接**: [https://f-droid.org/2026/07/01/adv-malware.html](https://f-droid.org/2026/07/01/adv-malware.html)

生成摘要时出错

---

## 4. Launch HN: Manufact (YC S25) – MCP Cloud

**原文标题**: Launch HN: Manufact (YC S25) – MCP Cloud

**原文链接**: [https://manufact.com](https://manufact.com)

生成摘要时出错

---

## 5. How to ask for help from people who don't know you

**原文标题**: How to ask for help from people who don't know you

**原文链接**: [https://pradyuprasad.com/writings/how-to-ask-for-help/](https://pradyuprasad.com/writings/how-to-ask-for-help/)

生成摘要时出错

---

## 6. AI can't be listed as inventor on patent applications, Japan's top court rules

**原文标题**: AI can't be listed as inventor on patent applications, Japan's top court rules

**原文链接**: [https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/](https://japannews.yomiuri.co.jp/science-nature/technology/20260306-314930/)

生成摘要时出错

---

## 7. Podman v6.0.0

**原文标题**: Podman v6.0.0

**原文链接**: [https://blog.podman.io/2026/07/introducing-podman-v6-0-0/](https://blog.podman.io/2026/07/introducing-podman-v6-0-0/)

生成摘要时出错

---

## 8. German button maker searched rivers of American Midwest for valuable shells

**原文标题**: German button maker searched rivers of American Midwest for valuable shells

**原文链接**: [https://www.smithsonianmag.com/smithsonian-institution/how-one-german-button-maker-searched-the-rivers-of-the-american-midwest-for-the-shells-that-could-make-him-a-fortune-180989012/](https://www.smithsonianmag.com/smithsonian-institution/how-one-german-button-maker-searched-the-rivers-of-the-american-midwest-for-the-shells-that-could-make-him-a-fortune-180989012/)

生成摘要时出错

---

## 9. Spain Orders Blacklist of Palantir from Public and Private Companies

**原文标题**: Spain Orders Blacklist of Palantir from Public and Private Companies

**原文链接**: [https://clashreport.com/world/articles/spain-orders-blacklist-of-us-tech-giant-palantir-from-public-and-private-companies-fsnc2z17gjv](https://clashreport.com/world/articles/spain-orders-blacklist-of-us-tech-giant-palantir-from-public-and-private-companies-fsnc2z17gjv)

生成摘要时出错

---

## 10. Show HN: CLI tool for detecting non-exact code duplication with embedding models

**原文标题**: Show HN: CLI tool for detecting non-exact code duplication with embedding models

**原文链接**: [https://github.com/rafal-qa/slopo](https://github.com/rafal-qa/slopo)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 2 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 3 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 4 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 5 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 6 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 7 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 8 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 9 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 10 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 11 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 12 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 13 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 14 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 15 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 16 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 17 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 18 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 19 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 20 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 21 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 22 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 23 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 24 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 25 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 26 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 27 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 28 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 29 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 30 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 31 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 32 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 33 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 34 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 35 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 36 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 37 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 38 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 39 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 40 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 41 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 42 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 43 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 44 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 45 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 46 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 47 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 48 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 49 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 50 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 51 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 52 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 53 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 54 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 55 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 56 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 57 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 58 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 59 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 60 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 61 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 62 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 63 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 64 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 65 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 66 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 67 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 68 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 69 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 70 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 71 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 72 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 73 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 74 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 75 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 76 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 77 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 78 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 79 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 80 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 81 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 82 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 83 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 84 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 85 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 86 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 87 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 88 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 89 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 90 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 91 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 92 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 93 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 94 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 95 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 96 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 97 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 98 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 99 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 100 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 101 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 102 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 103 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 104 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 105 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 106 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 107 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 108 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 109 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 110 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 111 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 112 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 113 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 114 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 115 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 116 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 117 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 118 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 119 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 120 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 121 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 122 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 123 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 124 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 125 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 126 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 127 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 128 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 129 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 130 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 131 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 132 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 133 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 134 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 135 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 136 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 137 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 138 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 139 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 140 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 141 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 142 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 143 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 144 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 145 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 146 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 147 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 148 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 149 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 150 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 151 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 152 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 153 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 154 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 155 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 156 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 157 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 158 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 159 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 160 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 161 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 162 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 163 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 164 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 165 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 166 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 167 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 168 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 169 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 170 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 171 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 172 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 173 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 174 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 175 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 176 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 177 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 178 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 179 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 180 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 181 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 182 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 183 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 184 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 185 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 186 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 187 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 188 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 189 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 190 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 191 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 192 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 193 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 194 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 195 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 196 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 197 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 198 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 199 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 200 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 201 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 202 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 203 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 204 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 205 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 206 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 207 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 208 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 209 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 210 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 211 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 212 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 213 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 214 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 215 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 216 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 217 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 218 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 219 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 220 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 221 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 222 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 223 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 224 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 225 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 226 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 227 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 228 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 229 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 230 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 231 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 232 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 233 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 234 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 235 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 236 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 237 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 238 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 239 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 240 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 241 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 242 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 243 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 244 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 245 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 246 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 247 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 248 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 249 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 250 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 251 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 252 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 253 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 254 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 255 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 256 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 257 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 258 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 259 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 260 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 261 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 262 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 263 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 264 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 265 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 266 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 267 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 268 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 269 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 270 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 271 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 272 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 273 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 274 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 275 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 276 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 277 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 278 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 279 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 280 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 281 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 282 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 283 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 284 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 285 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 286 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 287 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 288 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 289 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 290 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 291 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 292 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 293 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 294 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 295 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 296 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 297 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 298 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 299 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 300 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 301 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 302 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 303 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 304 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 305 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 306 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 307 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 308 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 309 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 310 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 311 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 312 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 313 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 314 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 315 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 316 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 317 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 318 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 319 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 320 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 321 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 322 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 323 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 324 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 325 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 326 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 327 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 328 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 329 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 330 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 331 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 332 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 333 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 334 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 335 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 336 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 337 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 338 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 339 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 340 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 341 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 342 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 343 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 344 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 345 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 346 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 347 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 348 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 349 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 350 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 351 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 352 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 353 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 354 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 355 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 356 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 357 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 358 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 359 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 360 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 361 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 362 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 363 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 364 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 365 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 366 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 367 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 368 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 369 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 370 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 371 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 372 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 373 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 374 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 375 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 376 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 377 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 378 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 379 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 380 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 381 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 382 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 383 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 384 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 385 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 386 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 387 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 388 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 389 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 390 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 391 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 392 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 393 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 394 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 395 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 396 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 397 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 398 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 399 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 400 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 401 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 402 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 403 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 404 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 405 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 406 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 407 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 408 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 409 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 410 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 411 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 412 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 413 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 414 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 415 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 416 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 417 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 418 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 419 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 420 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 421 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 422 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 423 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 424 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 425 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 426 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 427 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 428 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 429 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 430 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 431 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 432 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 433 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 434 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 435 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 436 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 437 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 438 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 439 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 440 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 441 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 442 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 443 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 444 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 445 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 446 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 447 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 448 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 449 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 450 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 451 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 452 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 453 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 454 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 455 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 456 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 457 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 458 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 459 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 460 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 461 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 462 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 463 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 464 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 465 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 466 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 467 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 468 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 469 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
