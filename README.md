# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-10.md)

*最后自动更新时间: 2026-04-10 18:15:35*
## 1. 你无法信任 macOS 的隐私与安全性设置

**原文标题**: You can't trust macOS Privacy and Security settings

**原文链接**: [https://eclecticlight.co/2026/04/10/why-you-cant-trust-privacy-security/](https://eclecticlight.co/2026/04/10/why-you-cant-trust-privacy-security/)

《你无法信任 macOS 的隐私与安全性设置》一文揭示了 macOS 用户界面与受保护文件夹（如文档、桌面和下载）实际系统权限之间存在的重大差异。

作者解释说，macOS 主要通过两种机制管理文件访问：“透明度、同意与控制 (TCC)”提示，以及“用户意图”（即通过“打开/保存面板”手动选择文件）。通过一个名为“Insent”的自定义应用，作者展示了这些系统交互中的一个漏洞：

1.  **绕过机制：** 即便应用在“隐私与安全性”设置中被明确拒绝访问某个文件夹，只要用户通过标准的“打开/保存面板”选择过一次该文件夹，应用就能绕过此限制。
2.  **漏洞所在：** macOS 将手动选择解读为“用户意图”，从而解除了该文件夹的沙盒限制。关键在于，这种权限覆盖不会反映在“系统设置”中。即使在“文件和文件夹”设置中该应用的开关显示为“关闭”，它依然保留对该文件夹的完整访问权限。
3.  **持久性：** 这种访问权限似乎是永久性的，即使在界面上关闭了开关依然有效。作者指出，真正撤销这种“隐形”访问权限的唯一方法是在终端运行特定的 `tccutil reset` 命令并重启 Mac。

**结论：**
文章总结道，macOS 中的“文件和文件夹”列表并不能作为应用实际权限的可靠参考。由于沙盒行为可以在不更新 UI 的情况下覆盖 TCC 设置，导致应用在系统设置显示为“已阻止”时，仍可能不受限地访问隐私数据。这造成了一个潜在的安全盲点，即用户误以为权限已被撤销，而实际上它们在后台依然处于活跃状态。

---

## 2. WireGuard 在微软签名问题解决后发布 Windows 新版本

**原文标题**: WireGuard makes new Windows release following Microsoft signing resolution

**原文链接**: [https://lists.zx2c4.com/pipermail/wireguard/2026-April/009561.html](https://lists.zx2c4.com/pipermail/wireguard/2026-April/009561.html)

Jason A. Donenfeld 宣布发布 WireGuardNT v0.11（底层内核驱动程序）和 WireGuard for Windows v0.6（管理 UI 与 CLI）。这标志着 Windows 客户端在较长一段时间内的首次更新。

**关键技术改进：**
*   **代码现代化：** 开发人员通过提高支持的最低 Windows 版本，显著简化了代码库。这使得移除旧版兼容补丁、冗余代码以及复杂的动态调度成为可能。
*   **性能与功能：** 此次更新包含大量错误修复和性能增强。新功能包括支持在不丢包的情况下移除单个允许的 IP 地址，以及支持在 IPv4 连接上设置极低的 MTU。
*   **更新工具链：** 该版本受益于 EWDK、Clang/LLVM 和 Go 的更新版本，以及现代化的 EV 证书签名基础设施。

**微软签名问题解决：**
公告回应了近期关于微软暂停 WireGuard 开发者账户的消息，该事件曾短暂阻碍了驱动程序的签名工作。Donenfeld 澄清称，此次封禁源于行政失误，而非阴谋或“恶意”。在 Hacker News 和 Twitter 引起公众关注后，微软迅速解封了账户，使项目得以恢复官方发布。

**安装：**
现有用户将收到内置更新程序的通知，该程序会在更新前安全地验证签名。新用户可以直接从 WireGuard 官方网站下载安装程序。尽管代码库已实现现代化，但该软件仍支持旧至 Windows 10 1507（内部版本 10240）的版本。

---

## 3. 一维国际象棋

**原文标题**: 1D Chess

**原文链接**: [https://rowan441.github.io/1dchess/chess.html](https://rowan441.github.io/1dchess/chess.html)

**一维国际象棋**（1D Chess）是传统国际象棋的一种简化一维变体，最早由马丁·加德纳在1980年7月为《科学美国人》撰写的“数学游戏”专栏中提出。通过移除多余的维度，该游戏在保留国际象棋核心原则的同时，专注于线性策略。

游戏包含三种棋子，具有特定的移动规则：
*   **王：** 向任一方向移动一格。
*   **马：** 向任一方向跳跃恰好两格，并跳过中间的任何棋子。
*   **车：** 沿直线移动任意距离。

游戏的目标是实现**将死**，即敌方王受到攻击且没有合法走法可以逃脱。尽管规则简单，该游戏仍具有战略深度；例如，白方已知可以通过特定的着法序列实现必胜（N4 N5, N6 K7, R4 K6, R2 K7, R5++）。

比赛在以下三种特定情况下以**和棋**结束：
1.  **逼和：** 玩家未被将军，但没有任何合法走法。
2.  **三次重复局面：** 同样的棋局局面出现了三次。
3.  **棋力不足：** 棋盘上仅剩下双方的王，导致无法实现将死。

这种变体作为一种数学和战略练习，证明了即使在单一维度中也能进行复杂的游戏。

---

## 4. Keychron 键盘与鼠标工业设计文件

**原文标题**: Industrial design files for Keychron keyboards and mice

**原文链接**: [https://github.com/Keychron/Keychron-Keyboards-Hardware-Design](https://github.com/Keychron/Keychron-Keyboards-Hardware-Design)

Keychron 发布了其键盘和鼠标的完整生产级工业设计文件库。这一“源码可用”项目包含超过 686 个 CAD 文件（涵盖 STEP、DWG、DXF 和 PDF 格式），涉及 88 种不同型号，包括 Q、K、V、L、C、P 系列键盘以及 M 和 G 系列鼠标。

该资源库提供了完整模型、外壳设计、定位板布局、卫星轴以及各种键帽高度。通过共享这些内部设计文件，Keychron 旨在从以下几个方面支持硬件和键盘社区：
*   **教育：** 学生和工程师可以研究真实的生产公差和安装结构。
*   **定制：** 爱好者可以重新修改外壳和定位板，或设计原创的硬件改装方案。
*   **生态增长：** 第三方开发人员可以高精度地开发兼容配件和插件。

**许可与使用**
该项目遵循“源码可用”原则，并设有特定限制。Keychron 鼓励个人和教育用途，且**商业用途仅限于创建兼容配件**。然而，严禁用户制造或销售 Keychron 仿制品、将硬件设计直接用于生产自有品牌的键盘/鼠标，或将 Keychron 商标用于自有品牌营销。

资源库中包含“入门指南”、3D 打印说明和文件格式指南，以帮助用户高效利用这些数据。Keychron 还鼓励社区贡献（如修复尺寸错误或添加 ISO 布局变体），以不断完善文件的文档说明和实用性。这一举措体现了 Keychron 迈向透明化的努力，旨在邀请用户以创造者而非仅仅是消费者的身份参与到硬件生态系统中。

---

## 5. 氦气难以替代

**原文标题**: Helium Is Hard to Replace

**原文链接**: [https://www.construction-physics.com/p/helium-is-hard-to-replace](https://www.construction-physics.com/p/helium-is-hard-to-replace)

在《氦气难以替代》一文中，布莱恩·波特（Brian Potter）探讨了氦气的至关重要性及其全球供应链的脆弱性。近期的地缘政治动荡——特别是霍尔木兹海峡的封锁——扰乱了来自卡塔尔的供应，而卡塔尔的产量占全球氦气产量的三分之一。2024年美国战略储备的抛售进一步加剧了这场危机。

氦气是天然气开采过程中产生的一种不可再生副产品。它拥有一系列独特的属性：惰性、轻质、高导热性，并拥有所有元素中最低的沸点（4.2 K）。这些特性使其在多个高科技行业中不可或缺：

*   **医疗保健：** 核磁共振（MRI）设备使用液氦来冷却超导磁体。尽管现代“零蒸发”设备减少了损耗，但全球存量设备仍是主要的氦气消耗者。
*   **半导体：** 该行业将氦气用于冷却、检漏和先进光刻（DUV/EUV）。预计到2035年，其需求将增长五倍。
*   **光纤：** 氦气作为冷却剂对于在制造过程中防止产生气泡至关重要，且目前尚无已知的替代品。
*   **航空航天与科学：** 它被用作火箭燃料箱的吹扫气，并用于冷却大型强子对撞机等科学仪器。

波特指出，虽然某些应用可以使用替代品——例如焊接用氩气或起重用氢气——但大多数低温和高科技用途并无实际的替代方案。尽管回收和再捕捉技术可以将消耗降低90%以上，但氦气仍然是一种日益难以获取的有限关键资源。

---

## 6. Bluesky 2026年4月故障复盘

**原文标题**: Bluesky April 2026 Outage Post-Mortem

**原文链接**: [https://pckt.blog/b/jcalabro/april-2026-outage-post-mortem-219ebg2](https://pckt.blog/b/jcalabro/april-2026-outage-post-mortem-219ebg2)

2026年4月，Bluesky 遭遇了一次重大故障，在长达 8 小时的时间里导致约 50% 的用户服务中断。在技术复盘中，工程师 Jim Calabro 详细说明了导致系统数据平面陷入“死亡螺旋”的连锁事件。

**根本原因**
问题的根源在于 `GetPostRecord` RPC 缺少并发限制。虽然大多数端点都使用 `errgroup.SetLimit` 来限制活动，但这个特定的处理程序却没有。当一个新的内部服务开始在每个请求中发送 1.5 万到 2 万个 URI（远超通常的 1 到 50 个）时，系统催生了数万个 goroutine。这压垮了 memcached 并耗尽了可用的 TCP 端口，使它们处于 `TIME_WAIT` 状态。

**死亡螺旋**
由于大量的错误日志记录，故障进一步升级。由于 Go 中的日志记录使用阻塞式系统调用，错误消息的激增迫使 Go 运行时创建了比平时多十倍的操作系统线程。这给垃圾回收器带来了巨大压力，导致了严重的“stop-the-world”停顿和频繁的内存溢出（OOM）崩溃。重启后，由于之前耗尽的端口仍被占用，服务依然处于瘫痪状态。

**解决与教训**
工程师们使用一种非常规的“临时修复”方案稳定了平台：通过一个分配随机回环 IP 的自定义拨号器来绕过端口耗尽。永久性的修复方案是在 Go 代码中添加了缺失的并发限制。

Calabro 总结道，此次故障凸显了对单客户端可观测性的需求，以及从繁重的日志记录转向更具扩展性的遥测技术（如 Prometheus 指标或 OpenTelemetry）的必要性。他还撤销了此前的一份状态更新，该更新曾错误地将此次中断归咎于第三方服务商。

---

## 7. CPU-Z and HWMonitor compromised

**原文标题**: CPU-Z and HWMonitor compromised

**原文链接**: [https://www.theregister.com/2026/04/10/cpuid_site_hijacked/](https://www.theregister.com/2026/04/10/cpuid_site_hijacked/)

生成摘要时出错

---

## 8. Bild AI (YC W25) 招聘创始产品工程师

**原文标题**: Bild AI (YC W25) Is Hiring a Founding Product Engineer

**原文链接**: [https://www.ycombinator.com/companies/bild-ai/jobs/dDMaxVN-founding-product-engineer](https://www.ycombinator.com/companies/bild-ai/jobs/dDMaxVN-founding-product-engineer)

生成摘要时出错

---

## 9. Clojure on Fennel Part One: Persistent Data Structures

**原文标题**: Clojure on Fennel Part One: Persistent Data Structures

**原文链接**: [https://andreyor.st/posts/2026-04-07-clojure-on-fennel-part-one-persistent-data-structures/](https://andreyor.st/posts/2026-04-07-clojure-on-fennel-part-one-persistent-data-structures/)

生成摘要时出错

---

## 10. Mysteries of Dropbox: Testing of a Distributed Sync Service (2016) [pdf]

**原文标题**: Mysteries of Dropbox: Testing of a Distributed Sync Service (2016) [pdf]

**原文链接**: [https://www.cis.upenn.edu/~bcpierce/papers/mysteriesofdropbox.pdf](https://www.cis.upenn.edu/~bcpierce/papers/mysteriesofdropbox.pdf)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 2 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 3 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 4 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 5 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 6 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 7 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 8 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 9 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 10 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 11 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 12 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 13 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 14 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 15 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 16 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 17 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 18 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 19 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 20 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 21 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 22 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 23 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 24 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 25 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 26 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 27 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 28 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 29 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 30 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 31 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 32 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 33 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 34 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 35 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 36 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 37 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 38 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 39 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 40 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 41 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 42 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 43 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 44 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 45 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 46 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 47 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 48 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 49 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 50 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 51 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 52 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 53 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 54 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 55 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 56 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 57 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 58 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 59 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 60 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 61 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 62 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 63 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 64 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 65 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 66 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 67 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 68 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 69 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 70 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 71 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 72 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 73 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 74 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 75 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 76 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 77 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 78 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 79 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 80 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 81 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 82 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 83 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 84 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 85 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 86 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 87 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 88 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 89 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 90 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 91 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 92 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 93 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 94 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 95 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 96 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 97 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 98 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 99 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 100 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 101 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 102 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 103 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 104 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 105 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 106 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 107 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 108 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 109 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 110 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 111 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 112 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 113 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 114 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 115 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 116 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 117 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 118 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 119 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 120 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 121 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 122 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 123 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 124 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 125 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 126 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 127 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 128 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 129 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 130 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 131 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 132 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 133 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 134 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 135 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 136 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 137 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 138 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 139 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 140 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 141 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 142 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 143 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 144 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 145 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 146 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 147 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 148 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 149 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 150 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 151 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 152 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 153 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 154 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 155 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 156 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 157 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 158 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 159 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 160 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 161 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 162 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 163 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 164 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 165 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 166 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 167 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 168 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 169 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 170 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 171 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 172 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 173 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 174 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 175 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 176 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 177 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 178 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 179 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 180 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 181 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 182 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 183 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 184 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 185 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 186 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 187 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 188 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 189 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 190 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 191 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 192 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 193 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 194 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 195 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 196 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 197 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 198 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 199 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 200 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 201 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 202 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 203 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 204 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 205 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 206 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 207 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 208 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 209 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 210 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 211 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 212 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 213 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 214 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 215 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 216 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 217 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 218 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 219 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 220 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 221 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 222 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 223 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 224 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 225 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 226 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 227 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 228 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 229 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 230 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 231 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 232 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 233 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 234 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 235 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 236 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 237 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 238 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 239 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 240 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 241 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 242 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 243 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 244 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 245 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 246 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 247 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 248 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 249 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 250 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 251 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 252 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 253 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 254 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 255 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 256 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 257 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 258 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 259 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 260 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 261 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 262 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 263 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 264 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 265 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 266 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 267 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 268 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 269 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 270 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 271 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 272 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 273 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 274 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 275 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 276 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 277 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 278 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 279 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 280 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 281 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 282 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 283 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 284 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 285 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 286 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 287 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 288 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 289 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 290 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 291 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 292 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 293 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 294 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 295 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 296 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 297 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 298 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 299 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 300 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 301 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 302 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 303 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 304 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 305 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 306 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 307 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 308 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 309 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 310 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 311 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 312 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 313 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 314 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 315 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 316 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 317 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 318 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 319 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 320 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 321 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 322 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 323 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 324 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 325 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 326 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 327 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 328 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 329 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 330 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 331 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 332 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 333 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 334 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 335 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 336 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 337 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 338 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 339 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 340 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 341 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 342 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 343 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 344 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 345 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 346 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 347 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 348 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 349 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 350 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 351 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 352 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 353 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 354 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 355 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 356 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 357 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 358 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 359 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 360 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 361 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 362 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 363 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 364 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 365 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 366 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 367 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 368 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 369 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 370 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 371 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 372 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 373 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 374 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 375 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 376 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 377 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 378 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 379 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 380 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 381 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 382 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 383 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 384 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 385 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 386 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
