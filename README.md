# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-30.md)

*最后自动更新时间: 2026-10-30 21:47:44*
## 1. 我最喜欢的 PowerMac 是任天堂 Wii

**原文标题**: My favourite PowerMac is a Nintendo Wii

**原文链接**: [https://virtuallyfun.com/2026/10/29/my-favourite-powermac-is-a-nintendo-wii/](https://virtuallyfun.com/2026/10/29/my-favourite-powermac-is-a-nintendo-wii/)

在《我最喜欢的 PowerMac 是任天堂 Wii》一文中，作者探讨了任天堂游戏机与苹果老旧硬件之间的技术重合。其核心前提是，任天堂 Wii 实际上是一台基于 PowerPC 架构的电脑，其搭载的“Broadway”处理器是早期 Mac 所使用的 PowerPC 750CL (G3) 处理器的演进版本。

作者详细介绍了通过改造 Wii 来运行 Macintosh 操作系统的过程。通过利用 Wii-Linux-NG 环境，作者成功运行了 Mac-on-Linux (MOL) 虚拟机，使 PowerPC 版本的 Mac OS 能够以接近原生的速度运行。主要亮点包括：

*   **硬件性能：** 尽管仅有 88MB 的可用内存和 729MHz 的处理器，Wii 却出人意料地能够启动 Classic Mac OS（如 Mac OS 9.2.2）以及早期版本的 Mac OS X（如 10.2 Jaguar）。
*   **技术实现：** 该项目涉及使用一台已安装自制系统的 Wii 引导进入 Linux 内核，进而托管 Mac 环境。作者指出，虽然内存是运行 Mac OS X 的重大瓶颈，但该系统作为一项功能性的奇趣探索依然具有意义。
*   **吸引力所在：** 作者认为，与真实的苹果老式塔式机箱相比，Wii 是一款更优秀的“PowerMac”，因为它极其廉价、紧凑且节能。它提供了一种怀旧而奇特的方式，在从未预设运行此类软件的硬件上体验 PowerPC 软件。

最终，这篇文章证明了 Wii 硬件的多功能性，也展现了自制软件社区通过爱好者虚拟化技术让 PowerPC 架构保持生命力的创造力。

---

## 2. Bunny CDN 安全事件

**原文标题**: Bunny CDN Security Incident

**原文链接**: [https://status.bunny.net/incidents/p6gf1by9kr7m](https://status.bunny.net/incidents/p6gf1by9kr7m)

**Bunny CDN 安全事件摘要**

2026年10月28日，bunny.net 报告了一起涉及其某家基础设施提供商的安全事件。该事件源于该提供商使用的第三方服务器管理软件遭到未经授权的访问，影响了 bunny.net 位于亚美尼亚的一个 CDN 节点。

**响应与调查**
收到通知后，bunny.net 的工程团队在 20 分钟内停止了通过受影响服务器的流量路由。随后，该服务器的数据被擦除，其对内部系统的访问权限被撤销，并从基础设施中永久移除。虽然 bunny.net 和提供商的调查均未发现该服务器或其数据遭到实际访问的证据，但公司仍将此事件视为一次潜在的泄露。

**影响与数据安全**
可能泄露的信息仅限于存储在该特定节点上的数据，包括临时缓存的 CDN 内容、Pull Zone 配置和 TLS 证书。重要的是，内部系统和客户账户数据并未存储在受影响的服务器上，目前依然安全。

**缓解措施与客户操作**
作为预防措施，bunny.net 已针对 TLS 证书采取了以下步骤：
*   **平台域名：** `b-cdn.net` 和 `bunny.run` 的证书已经撤销并重新签发。
*   **托管证书：** 公司目前正在分批次为自定义域名重新签发托管 TLS 证书。该过程预计将于 10 月 31 日结束前完成。使用这些托管服务的客户**无需采取任何操作**。
*   **自管证书：** 强烈建议自行提供 TLS 证书的客户撤销原证书，并使用新私钥重新签发。

Bunny.net 将继续监控其基础设施，并在重新签发流程完成后提供最终更新。

---

## 3. Product Managers aren't safe either

**原文标题**: Product Managers aren't safe either

**原文链接**: [https://lucaskostka.com/posts/ai-challenges-more-than-devs](https://lucaskostka.com/posts/ai-challenges-more-than-devs)

生成摘要时出错

---

## 4. Northflank 遭到入侵

**原文标题**: Northflank Breached

**原文链接**: [https://status.northflank.com](https://status.northflank.com)

2026年10月30日，云平台 Northflank 报告了一起严重的安全性漏洞和大规模服务中断，波及了包括网络、服务、附加组件（Addons）及作业（Jobs）在内的多个核心组件。

该事件始于 UTC 时间 11:43 由 Wiz 触发的威胁警报，随后平台进行了多次紧急网络策略修补。截至 UTC 下午 1:58，Northflank 确认**所有环境变量均应被视为已解密且遭到泄露。**

**关键信息与必要行动：**
*   **密钥泄露：** 所有用户必须立即轮换所有密钥和凭据，包括存储在工作负载、密钥组以及全局密钥中的信息。
*   **AI 密钥滥用：** 已有多名用户确认其 AI 密钥被盗并被未经授权的第三方使用。
*   **附加组件安全：** 建议用户禁用所有附加组件的公共访问权限。Northflank 已针对 Postgres 和 MongoDB 启用了特定的密钥轮换工具，以协助保护数据库安全。
*   **平台状态：** 尽管 Northflank 应用、API 和营销网站仍保持运行，但大多数基础设施服务目前正处于大规模中断状态。

Northflank 目前正与 Wiz 云事件响应团队 (CIRT) 合作调查此次漏洞的影响范围。公司的官方指导建议是：用户应在假设环境变量中所有敏感数据均已暴露的前提下进行操作。

---

## 5. Cursor 市场中 Claude Code for VS Code 扩展的后门

**原文标题**: Backdoor in Claude Code for VS Code extension on the Cursor Marketplace

**原文链接**: [https://phorion.io/blog/offical-claude-code-vsx-compromise/](https://phorion.io/blog/offical-claude-code-vsx-compromise/)

Phorion 在 Cursor 插件市场中发现，“Claude Code” VS Code 扩展程序的 2.1.313 版本包含恶意后门。该扩展现已下架，它在加载后会立即执行多阶段有效载荷，无需任何用户交互。

**关键技术细节：**
*   **SSH 访问：** 该恶意软件将攻击者控制的公钥 (`svc-telemetry`) 添加到 `~/.ssh/authorized_keys` 中，并尝试在 macOS、Linux 和 Windows 上启用本地 SSH 守护程序。在 macOS 上，脚本检查“远程登录”状态时存在逻辑漏洞，如果用户缺乏管理员权限，可能无法启用 SSH。
*   **反向隧道：** 它向攻击者控制的 IP (`134.209.82.225`) 建立持久的出站 SSH 隧道。这允许操作者绕过防火墙，通过隧道回连来获取交互式 Shell 访问权限。
*   **持久化：** 为了在重启后继续运行，该脚本会安装特定平台的组件：macOS 上的 LaunchAgent（伪装为 `com.apple.sysmond.plist`）、Linux 上的 crontab 条目，以及 Windows 上的启动文件夹脚本或计划任务。
*   **侦察：** 该扩展会通过 HTTP 向攻击者发送主机元数据，包括 IP 地址、用户名以及敏感环境变量名称列表（例如 AWS、GCP、SECRET）。

**检测与修复：**
安全团队应监控对 `authorized_keys` 的未经授权修改、`~/.config/` 中隐藏脚本的创建，以及指向识别出的恶意 IP 的出站 SSH 连接。由于该恶意软件在扩展文件夹之外安装了持久性组件，仅卸载扩展是不够的；需要进行完整的事件响应，并手动清除持久化组件和未经授权的 SSH 密钥。

---

## 6. 儒勒·凡尔纳的遗失小说

**原文标题**: Jules Verne's Lost Novel

**原文链接**: [https://blue-continuum.com/verne-paris](https://blue-continuum.com/verne-paris)

1863年，儒勒·凡尔纳创作了小说《二十世纪的巴黎》，这部作品与其以往典型的冒险叙事截然不同。凡尔纳没有去探索深海或外层空间，而是将目光投向未来，构想了1960年的巴黎。该书审视了19世纪对科学、机械、商业和效率的狂热追求可能带来的后果。

与他那些风格较为乐观的作品不同，这部小说呈现了一个冷酷的预言，其出版商皮埃尔-儒勒·赫泽尔认为该作品脱离现实且过于悲观，不宜向公众发行。因此，凡尔纳将手稿锁进了家族保险箱。它被尘封并秘而不宣长达131年，直到1994年才被寻回并最终在法国出版。

本文强调，这部“失落的小说”是凡尔纳职业生涯中的一个独特时刻，他在书中批判了工业时代的逻辑终局，描绘了一个完全由技术和商业驱动的文明所呈现的反乌托邦愿景。

---

## 7. 破坏开放互联网阻挡不了恶意机器人

**原文标题**: Breaking the open web won't stop the bad bots

**原文链接**: [https://www.techpolicy.press/breaking-the-open-web-wont-stop-the-bad-bots/](https://www.techpolicy.press/breaking-the-open-web-wont-stop-the-bad-bots/)

在《破坏开放网络并不能阻止恶意机器人》一文中，莱拉·贝利（Lila Bailey）和泰丝·瓦塔尼安（Tess Vartanian）指出，诸如联邦《隐形机器人禁止法案》和纽约州《隐形爬虫禁止法案》等拟议立法，在未能解决人工智能激进抓取所引发的问题的同时，还威胁到了开放网络的基础。

尽管作者承认人工智能开发者往往会剥夺新闻编辑室的收入和流量，但他们认为，强制要求所有自动化“爬虫”表明身份和目的的拟议解决方案存在严重缺陷。他们强调了几个关键风险：

*   **威胁新闻报道与学术研究：** 许多具有社会价值的活动，如《华尔街日报》对政府腐败的调查或针对网络歧视的学术研究，都依赖于匿名抓取。如果被调查对象知道自己正受到监控，可能会改变行为，从而损害数据的真实性。
*   **损害公益工具：** 互联网档案库（Internet Archive）、残障人士倡导组织和网络安全研究人员利用机器人来保存历史、检测无障碍问题并扫描威胁。模糊的法律措辞可能会使这些“善意”机器人因担心承担法律责任而畏缩不前。
*   **缺乏实效：** 识别出机器人的身份并不能阻止其使服务器过载。一个公开身份的爬虫仍可能造成技术和经济损害，而“恶意”机器人则很可能会找到规避身份识别要求的方法。
*   **宪法层面的担忧：** 作者认为，强制身份识别损害了宪法第一修正案赋予公民匿名获取信息的权利。

作者敦促决策者不要采取“去匿名化”措施，而应关注**基于行为的责任追究**——针对服务器受损或欺诈等具体危害。他们建议支持流量管理的技术标准，并利用现有的隐私和版权法，而不是实施会破坏自由开放互联网所必需的匿名性的全面禁令。

---

## 8. Show HN：在约 1GB 的 Qwen 权重中实现可运行的任天堂

**原文标题**: Show HN: A working Nintendo in ~1GB of Qwen weights

**原文链接**: [https://github.com/dbreunig/nesformer](https://github.com/dbreunig/nesformer)

**nesformer** is a project that successfully compiles a functional Nintendo Entertainment System (NES) CPU into the weights of a stock Qwen3.5-4B language model. Unlike typical AI models, these weights were not trained; instead, a compiler computed them to represent the logic of the NES's 6502 CPU, its 2 KB of RAM, and the cartridge's ROM.

**Key Technical Details:**
*   **Mechanism:** The model utilizes its **Gated DeltaNet state** as the machine's memory. Every row in the state matrix acts as a memory cell for registers, RAM, and ROM.
*   **The Trace:** As the model runs, it predicts the CPU’s execution log one token at a time. A Python-based host program handles the "rest" of the console—rendering graphics via a scanline PPU, reading controller inputs, and managing timing interrupts.
*   **Compatibility:** It currently supports **NROM (Mapper 0)** games, such as *Super Mario Bros.*, *Donkey Kong*, and *Excitebike*. It handles all 151 official 6502 opcodes and matches the output of conventional emulators exactly.
*   **Performance:** While technically precise, it is slow—running approximately 150–290 times slower than a real NES. A single frame takes 1–6 seconds to generate on a standard CPU.
*   **Architecture:** The checkpoint contains roughly 466 million parameters (~933 MB). Because the logic is sparse, the weights are highly compressible.

**Limitations:**
The project is currently limited to NROM cartridges (max 32 KB ROM) and does not support bank-switching mappers, unofficial opcodes, or sound (APU). It serves as a sophisticated "proof of concept" for using transformer architectures as general-purpose computational engines.

---

## 9. 无限 Mac：BeOS

**原文标题**: Infinite Mac: BeOS

**原文链接**: [https://blog.persistent.info/2026/10/infinite-mac-beos.html](https://blog.persistent.info/2026/10/infinite-mac-beos.html)

生成摘要时出错

---

## 10. Florilegium: Procedural Flowers in LaTeX

**原文标题**: Florilegium: Procedural Flowers in LaTeX

**原文链接**: [https://github.com/kevinraymond/florilegium](https://github.com/kevinraymond/florilegium)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 2 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 3 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 4 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 5 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 6 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 7 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 8 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 9 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 10 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 11 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 12 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 13 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 14 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 15 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 16 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 17 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 18 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 19 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 20 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 21 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 22 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 23 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 24 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 25 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 26 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 27 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 28 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 29 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 30 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 31 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 32 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 33 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 34 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 35 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 36 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 37 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 38 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 39 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 40 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 41 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 42 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 43 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 44 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 45 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 46 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 47 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 48 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 49 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 50 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 51 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 52 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 53 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 54 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 55 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 56 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 57 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 58 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 59 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 60 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 61 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 62 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 63 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 64 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 65 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 66 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 67 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 68 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 69 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 70 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 71 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 72 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 73 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 74 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 75 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 76 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 77 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 78 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 79 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 80 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 81 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 82 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 83 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 84 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 85 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 86 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 87 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 88 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 89 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 90 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 91 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 92 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 93 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 94 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 95 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 96 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 97 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 98 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 99 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 100 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 101 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 102 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 103 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 104 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 105 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 106 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 107 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 108 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 109 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 110 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 111 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 112 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 113 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 114 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 115 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 116 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 117 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 118 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 119 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 120 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 121 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 122 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 123 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 124 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 125 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 126 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 127 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 128 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 129 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 130 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 131 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 132 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 133 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 134 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 135 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 136 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 137 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 138 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 139 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 140 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 141 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 142 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 143 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 144 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 145 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 146 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 147 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 148 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 149 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 150 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 151 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 152 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 153 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 154 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 155 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 156 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 157 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 158 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 159 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 160 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 161 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 162 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 163 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 164 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 165 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 166 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 167 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 168 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 169 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 170 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 171 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 172 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 173 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 174 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 175 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 176 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 177 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 178 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 179 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 180 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 181 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 182 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 183 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 184 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 185 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 186 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 187 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 188 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 189 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 190 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 191 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 192 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 193 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 194 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 195 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 196 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 197 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 198 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 199 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 200 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 201 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 202 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 203 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 204 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 205 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 206 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 207 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 208 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 209 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 210 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 211 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 212 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 213 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 214 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 215 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 216 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 217 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 218 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 219 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 220 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 221 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 222 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 223 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 224 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 225 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 226 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 227 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 228 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 229 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 230 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 231 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 232 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 233 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 234 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 235 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 236 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 237 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 238 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 239 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 240 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 241 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 242 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 243 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 244 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 245 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 246 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 247 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 248 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 249 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 250 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 251 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 252 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 253 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 254 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 255 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 256 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 257 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 258 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 259 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 260 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 261 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 262 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 263 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 264 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 265 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 266 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 267 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 268 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 269 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 270 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 271 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 272 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 273 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 274 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 275 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 276 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 277 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 278 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 279 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 280 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 281 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 282 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 283 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 284 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 285 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 286 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 287 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 288 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 289 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 290 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 291 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 292 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 293 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 294 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 295 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 296 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 297 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 298 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 299 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 300 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 301 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 302 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 303 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 304 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 305 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 306 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 307 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 308 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 309 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 310 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 311 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 312 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 313 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 314 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 315 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 316 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 317 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 318 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 319 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 320 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 321 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 322 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 323 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 324 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 325 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 326 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 327 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 328 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 329 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 330 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 331 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 332 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 333 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 334 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 335 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 336 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 337 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 338 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 339 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 340 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 341 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 342 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 343 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 344 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 345 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 346 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 347 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 348 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 349 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 350 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 351 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 352 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 353 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 354 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 355 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 356 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 357 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 358 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 359 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 360 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 361 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 362 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 363 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 364 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 365 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 366 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 367 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 368 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 369 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 370 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 371 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 372 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 373 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 374 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 375 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 376 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 377 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 378 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 379 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 380 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 381 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 382 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 383 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 384 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 385 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 386 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 387 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 388 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 389 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 390 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 391 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 392 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 393 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 394 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 395 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 396 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 397 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 398 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 399 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 400 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 401 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 402 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 403 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 404 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 405 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 406 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 407 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 408 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 409 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 410 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 411 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 412 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 413 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 414 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 415 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 416 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 417 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 418 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 419 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 420 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 421 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 422 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 423 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 424 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 425 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 426 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 427 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 428 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 429 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 430 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 431 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 432 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 433 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 434 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 435 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 436 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 437 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 438 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 439 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 440 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 441 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 442 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 443 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 444 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 445 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 446 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 447 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 448 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 449 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 450 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 451 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 452 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 453 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 454 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 455 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 456 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 457 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 458 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 459 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 460 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 461 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 462 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 463 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 464 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 465 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 466 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 467 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 468 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 469 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 470 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 471 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 472 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 473 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 474 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 475 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 476 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 477 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 478 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 479 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 480 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 481 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 482 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 483 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 484 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 485 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 486 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 487 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 488 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 489 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 490 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 491 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 492 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 493 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 494 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 495 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 496 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 497 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 498 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 499 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 500 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 501 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 502 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 503 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 504 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 505 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 506 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 507 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 508 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 509 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 510 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 511 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 512 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 513 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 514 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 515 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 516 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 517 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 518 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 519 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 520 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 521 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 522 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 523 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 524 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 525 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 526 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 527 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 528 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 529 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 530 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 531 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 532 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 533 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 534 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 535 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 536 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 537 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 538 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 539 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 540 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 541 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 542 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 543 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 544 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 545 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 546 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 547 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 548 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 549 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 550 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 551 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 552 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 553 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 554 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 555 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 556 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 557 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 558 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 559 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 560 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 561 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 562 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 563 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 564 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 565 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 566 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 567 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 568 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 569 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 570 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 571 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 572 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 573 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 574 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 575 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 576 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 577 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 578 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 579 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 580 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 581 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 582 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 583 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 584 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 585 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 586 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 587 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
