# Hacker News 热门文章摘要 (2026-04-10)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. The difficulty of making sure your website is broken

**原文标题**: The difficulty of making sure your website is broken

**原文链接**: [https://letsencrypt.org/2026/04/10/test-sites.html](https://letsencrypt.org/2026/04/10/test-sites.html)

生成摘要时出错

---

## 12. A compelling title that is cryptic enough to get you to take action on it

**原文标题**: A compelling title that is cryptic enough to get you to take action on it

**原文链接**: [https://ericwbailey.website/published/a-compelling-title-that-is-cryptic-enough-to-get-you-to-take-action-on-it/](https://ericwbailey.website/published/a-compelling-title-that-is-cryptic-enough-to-get-you-to-take-action-on-it/)

生成摘要时出错

---

## 13. FBI used iPhone notification data to retrieve deleted Signal messages

**原文标题**: FBI used iPhone notification data to retrieve deleted Signal messages

**原文链接**: [https://9to5mac.com/2026/04/09/fbi-used-iphone-notification-data-to-retrieve-deleted-signal-messages/](https://9to5mac.com/2026/04/09/fbi-used-iphone-notification-data-to-retrieve-deleted-signal-messages/)

生成摘要时出错

---

## 14. How NASA built Artemis II’s fault-tolerant computer

**原文标题**: How NASA built Artemis II’s fault-tolerant computer

**原文链接**: [https://cacm.acm.org/news/how-nasa-built-artemis-iis-fault-tolerant-computer/](https://cacm.acm.org/news/how-nasa-built-artemis-iis-fault-tolerant-computer/)

生成摘要时出错

---

## 15. I still prefer MCP over skills

**原文标题**: I still prefer MCP over skills

**原文链接**: [https://david.coffee/i-still-prefer-mcp-over-skills/](https://david.coffee/i-still-prefer-mcp-over-skills/)

生成摘要时出错

---

## 16. France to ditch Windows for Linux to reduce reliance on US tech

**原文标题**: France to ditch Windows for Linux to reduce reliance on US tech

**原文链接**: [https://techcrunch.com/2026/04/10/france-to-ditch-windows-for-linux-to-reduce-reliance-on-us-tech/](https://techcrunch.com/2026/04/10/france-to-ditch-windows-for-linux-to-reduce-reliance-on-us-tech/)

生成摘要时出错

---

## 17. C++: Freestanding Standard Library

**原文标题**: C++: Freestanding Standard Library

**原文链接**: [https://www.sandordargo.com/blog/2026/04/08/cpp-freestanding](https://www.sandordargo.com/blog/2026/04/08/cpp-freestanding)

生成摘要时出错

---

## 18. Penguin 'Toxicologists' Find PFAS Chemicals in Remote Patagonia

**原文标题**: Penguin 'Toxicologists' Find PFAS Chemicals in Remote Patagonia

**原文链接**: [https://www.ucdavis.edu/health/news/penguin-toxicologists-find-pfas-chemicals-remote-patagonia](https://www.ucdavis.edu/health/news/penguin-toxicologists-find-pfas-chemicals-remote-patagonia)

生成摘要时出错

---

## 19. A new trick brings stability to quantum operations

**原文标题**: A new trick brings stability to quantum operations

**原文链接**: [https://ethz.ch/en/news-and-events/eth-news/news/2026/04/a-new-trick-brings-stability-to-quantum-operations.html](https://ethz.ch/en/news-and-events/eth-news/news/2026/04/a-new-trick-brings-stability-to-quantum-operations.html)

生成摘要时出错

---

## 20. Code is run more than read (2023)

**原文标题**: Code is run more than read (2023)

**原文链接**: [https://olano.dev/blog/code-is-run-more-than-read/](https://olano.dev/blog/code-is-run-more-than-read/)

生成摘要时出错

---

## 21. RSoC 2026: A new CPU scheduler for Redox OS

**原文标题**: RSoC 2026: A new CPU scheduler for Redox OS

**原文链接**: [https://www.redox-os.org/news/rsoc-dwrr/](https://www.redox-os.org/news/rsoc-dwrr/)

生成摘要时出错

---

## 22. Native Instant Space Switching on macOS

**原文标题**: Native Instant Space Switching on macOS

**原文链接**: [https://arhan.sh/blog/native-instant-space-switching-on-macos/](https://arhan.sh/blog/native-instant-space-switching-on-macos/)

生成摘要时出错

---

## 23. Deterministic Primality Testing for Limited Bit Width

**原文标题**: Deterministic Primality Testing for Limited Bit Width

**原文链接**: [https://www.jeremykun.com/2026/04/07/deterministic-miller-rabin/](https://www.jeremykun.com/2026/04/07/deterministic-miller-rabin/)

生成摘要时出错

---

## 24. Supply chain nightmare: How Rust will be attacked and what we can do to mitigate

**原文标题**: Supply chain nightmare: How Rust will be attacked and what we can do to mitigate

**原文链接**: [https://kerkour.com/rust-supply-chain-nightmare](https://kerkour.com/rust-supply-chain-nightmare)

生成摘要时出错

---

## 25. We've raised $17M to build what comes after Git

**原文标题**: We've raised $17M to build what comes after Git

**原文链接**: [https://blog.gitbutler.com/series-a](https://blog.gitbutler.com/series-a)

生成摘要时出错

---

## 26. US summons bank bosses over cyber risks from Anthropic's latest AI model

**原文标题**: US summons bank bosses over cyber risks from Anthropic's latest AI model

**原文链接**: [https://www.theguardian.com/technology/2026/apr/10/us-summoned-bank-bosses-to-discuss-cyber-risks-posed-by-anthropic-latest-ai-model](https://www.theguardian.com/technology/2026/apr/10/us-summoned-bank-bosses-to-discuss-cyber-risks-posed-by-anthropic-latest-ai-model)

生成摘要时出错

---

## 27. DRAM has a design flaw from 1966. I bypassed it [video]

**原文标题**: DRAM has a design flaw from 1966. I bypassed it [video]

**原文链接**: [https://www.youtube.com/watch?v=KKbgulTp3FE](https://www.youtube.com/watch?v=KKbgulTp3FE)

生成摘要时出错

---

## 28. Generative art over the years

**原文标题**: Generative art over the years

**原文链接**: [https://blog.veitheller.de/Generative_art_over_the_years.html](https://blog.veitheller.de/Generative_art_over_the_years.html)

生成摘要时出错

---

## 29. Charcuterie – Visual similarity Unicode explorer

**原文标题**: Charcuterie – Visual similarity Unicode explorer

**原文链接**: [https://charcuterie.elastiq.ch/](https://charcuterie.elastiq.ch/)

生成摘要时出错

---

## 30. Why I'm Building a Database Engine in C#

**原文标题**: Why I'm Building a Database Engine in C#

**原文链接**: [https://nockawa.github.io/blog/why-building-database-engine-in-csharp/](https://nockawa.github.io/blog/why-building-database-engine-in-csharp/)

生成摘要时出错

---

## 31. "Negative" views of Broadcom driving VMware migrations, rival says

**原文标题**: "Negative" views of Broadcom driving VMware migrations, rival says

**原文链接**: [https://arstechnica.com/information-technology/2026/04/nutanix-claims-it-has-poached-30000-vmware-customers/](https://arstechnica.com/information-technology/2026/04/nutanix-claims-it-has-poached-30000-vmware-customers/)

生成摘要时出错

---

## 32. Show HN: Keeper – embedded secret store for Go (help me break it)

**原文标题**: Show HN: Keeper – embedded secret store for Go (help me break it)

**原文链接**: [https://github.com/agberohq/keeper](https://github.com/agberohq/keeper)

生成摘要时出错

---

## 33. Show HN: Marimo pair – Reactive Python notebooks as environments for agents

**原文标题**: Show HN: Marimo pair – Reactive Python notebooks as environments for agents

**原文链接**: [https://github.com/marimo-team/marimo-pair](https://github.com/marimo-team/marimo-pair)

生成摘要时出错

---

## 34. Old laptops in a colo as low cost servers

**原文标题**: Old laptops in a colo as low cost servers

**原文链接**: [https://colaptop.pages.dev/](https://colaptop.pages.dev/)

生成摘要时出错

---

## 35. The Art of Risk Management (2017)

**原文标题**: The Art of Risk Management (2017)

**原文链接**: [https://www.bcg.com/publications/2017/finance-function-excellence-corporate-development-art-risk-management](https://www.bcg.com/publications/2017/finance-function-excellence-corporate-development-art-risk-management)

生成摘要时出错

---

## 36. Unfolder for Mac – A 3D model unfolding tool for creating papercraft

**原文标题**: Unfolder for Mac – A 3D model unfolding tool for creating papercraft

**原文链接**: [https://www.unfolder.app/](https://www.unfolder.app/)

生成摘要时出错

---

## 37. OpenAI backs Illinois bill that would limit when AI labs can be held liable

**原文标题**: OpenAI backs Illinois bill that would limit when AI labs can be held liable

**原文链接**: [https://www.wired.com/story/openai-backs-bill-exempt-ai-firms-model-harm-lawsuits/](https://www.wired.com/story/openai-backs-bill-exempt-ai-firms-model-harm-lawsuits/)

生成摘要时出错

---

## 38. The Vasa

**原文标题**: The Vasa

**原文链接**: [https://psychsafety.com/the-vasa-disaster/](https://psychsafety.com/the-vasa-disaster/)

生成摘要时出错

---

## 39. Inflation Rose to 3.3% in March, Driven by Rising Fuel Costs

**原文标题**: Inflation Rose to 3.3% in March, Driven by Rising Fuel Costs

**原文链接**: [https://www.wsj.com/economy/cpi-inflation-report-march-2026-bb353007](https://www.wsj.com/economy/cpi-inflation-report-march-2026-bb353007)

生成摘要时出错

---

## 40. Model-Based Testing for Dungeons & Dragons

**原文标题**: Model-Based Testing for Dungeons & Dragons

**原文链接**: [https://www.loskutoff.com/blog/model-based-testing-dnd/](https://www.loskutoff.com/blog/model-based-testing-dnd/)

生成摘要时出错

---

## 41. HBO Obtains DMCA Subpoena to Unmask 'Euphoria' Spoiler Account on X

**原文标题**: HBO Obtains DMCA Subpoena to Unmask 'Euphoria' Spoiler Account on X

**原文链接**: [https://torrentfreak.com/hbo-obtains-dmca-subpoena-to-unmask-euphoria-spoiler-account-on-x/](https://torrentfreak.com/hbo-obtains-dmca-subpoena-to-unmask-euphoria-spoiler-account-on-x/)

生成摘要时出错

---

## 42. Intel 486 CPU announced April 10, 1989

**原文标题**: Intel 486 CPU announced April 10, 1989

**原文链接**: [https://dfarq.homeip.net/intel-486-cpu-announced-april-10-1989/](https://dfarq.homeip.net/intel-486-cpu-announced-april-10-1989/)

生成摘要时出错

---

## 43. Instant 1.0, a backend for AI-coded apps

**原文标题**: Instant 1.0, a backend for AI-coded apps

**原文链接**: [https://www.instantdb.com/essays/architecture](https://www.instantdb.com/essays/architecture)

生成摘要时出错

---

## 44. Kagi Product Tips – Customize Your Search Results with URL Redirects

**原文标题**: Kagi Product Tips – Customize Your Search Results with URL Redirects

**原文链接**: [https://blog.kagi.com/tips/redirects](https://blog.kagi.com/tips/redirects)

生成摘要时出错

---

## 45. Research-Driven Agents: When an agent reads before it codes

**原文标题**: Research-Driven Agents: When an agent reads before it codes

**原文链接**: [https://blog.skypilot.co/research-driven-agents/](https://blog.skypilot.co/research-driven-agents/)

生成摘要时出错

---

## 46. PicoZ80 – Drop-In Z80 Replacement

**原文标题**: PicoZ80 – Drop-In Z80 Replacement

**原文链接**: [https://eaw.app/picoz80/](https://eaw.app/picoz80/)

生成摘要时出错

---

## 47. Artemis II and the invisible hazard on the way to the Moon

**原文标题**: Artemis II and the invisible hazard on the way to the Moon

**原文链接**: [https://www.ansto.gov.au/news/artemis-ii-and-invisible-hazard-on-way-to-moon-part-1](https://www.ansto.gov.au/news/artemis-ii-and-invisible-hazard-on-way-to-moon-part-1)

生成摘要时出错

---

## 48. An AI robot in my home

**原文标题**: An AI robot in my home

**原文链接**: [https://allevato.me/2026/04/07/an-ai-robot-in-my-home](https://allevato.me/2026/04/07/an-ai-robot-in-my-home)

生成摘要时出错

---

## 49. Hegel, a universal property-based testing protocol and family of PBT libraries

**原文标题**: Hegel, a universal property-based testing protocol and family of PBT libraries

**原文链接**: [https://hegel.dev](https://hegel.dev)

生成摘要时出错

---

## 50. LittleSnitch for Linux

**原文标题**: LittleSnitch for Linux

**原文链接**: [https://obdev.at/products/littlesnitch-linux/index.html](https://obdev.at/products/littlesnitch-linux/index.html)

生成摘要时出错

---

## 51. The Raft consensus algorithm explained through "Mean Girls" (2019)

**原文标题**: The Raft consensus algorithm explained through "Mean Girls" (2019)

**原文链接**: [https://www.cockroachlabs.com/blog/raft-is-so-fetch/](https://www.cockroachlabs.com/blog/raft-is-so-fetch/)

生成摘要时出错

---

## 52. Reverse engineering Gemini's SynthID detection

**原文标题**: Reverse engineering Gemini's SynthID detection

**原文链接**: [https://github.com/aloshdenny/reverse-SynthID](https://github.com/aloshdenny/reverse-SynthID)

生成摘要时出错

---

## 53. Jennifer Aniston and Friends Cost Us 377GB and Broke Ext4 Hardlinks

**原文标题**: Jennifer Aniston and Friends Cost Us 377GB and Broke Ext4 Hardlinks

**原文链接**: [https://blog.discourse.org/2026/04/how-jennifer-aniston-and-friends-cost-us-377gb-and-broke-ext4-hardlinks/](https://blog.discourse.org/2026/04/how-jennifer-aniston-and-friends-cost-us-377gb-and-broke-ext4-hardlinks/)

生成摘要时出错

---

## 54. Anthropic's Claude Mythos isn't a sentient super-hacker, it's a sales pitch

**原文标题**: Anthropic's Claude Mythos isn't a sentient super-hacker, it's a sales pitch

**原文链接**: [https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-claude-mythos-isnt-a-sentient-super-hacker-its-a-sales-pitch-claims-of-thousands-of-severe-zero-days-rely-on-just-198-manual-reviews](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-claude-mythos-isnt-a-sentient-super-hacker-its-a-sales-pitch-claims-of-thousands-of-severe-zero-days-rely-on-just-198-manual-reviews)

生成摘要时出错

---

## 55. I ported Mac OS X to the Nintendo Wii

**原文标题**: I ported Mac OS X to the Nintendo Wii

**原文链接**: [https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html](https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html)

生成摘要时出错

---

## 56. A WebGPU implementation of Augmented Vertex Block Descent

**原文标题**: A WebGPU implementation of Augmented Vertex Block Descent

**原文链接**: [https://github.com/jure/webphysics](https://github.com/jure/webphysics)

生成摘要时出错

---

## 57. Show HN: I built a Cargo-like build tool for C/C++

**原文标题**: Show HN: I built a Cargo-like build tool for C/C++

**原文链接**: [https://github.com/randerson112/craft](https://github.com/randerson112/craft)

生成摘要时出错

---

## 58. Moving from WordPress to Jekyll (and static site generators in general)

**原文标题**: Moving from WordPress to Jekyll (and static site generators in general)

**原文链接**: [https://www.demandsphere.com/blog/rebuilding-demandsphere-with-jekyll-and-claude-code/](https://www.demandsphere.com/blog/rebuilding-demandsphere-with-jekyll-and-claude-code/)

生成摘要时出错

---

## 59. Will I ever own a zettaflop?

**原文标题**: Will I ever own a zettaflop?

**原文链接**: [https://geohot.github.io//blog/jekyll/update/2026/01/26/own-a-zettaflop.html](https://geohot.github.io//blog/jekyll/update/2026/01/26/own-a-zettaflop.html)

生成摘要时出错

---

## 60. Git commands I run before reading any code

**原文标题**: Git commands I run before reading any code

**原文链接**: [https://piechowski.io/post/git-commands-before-reading-code/](https://piechowski.io/post/git-commands-before-reading-code/)

生成摘要时出错

---

## 61. Principles of Mechanical Sympathy

**原文标题**: Principles of Mechanical Sympathy

**原文链接**: [https://martinfowler.com/articles/mechanical-sympathy-principles.html](https://martinfowler.com/articles/mechanical-sympathy-principles.html)

生成摘要时出错

---

## 62. 生而私密：在 Proton 为您的孩子预留首个电子邮箱。

**原文标题**: Born Private: Reserve your child's first email address with Proton

**原文链接**: [https://proton.me/blog/born-private](https://proton.me/blog/born-private)

生成摘要时出错

---

## 63. Afrika Bambaataa has died

**原文标题**: Afrika Bambaataa has died

**原文链接**: [https://www.bbc.co.uk/news/articles/c2evppm30p7o](https://www.bbc.co.uk/news/articles/c2evppm30p7o)

生成摘要时出错

---

## 64. War on Raze

**原文标题**: War on Raze

**原文链接**: [https://gist.github.com/chrispsn/af6844b80687462814fc39d4b97399a6](https://gist.github.com/chrispsn/af6844b80687462814fc39d4b97399a6)

生成摘要时出错

---

## 65. LLM plays an 8-bit Commander X16 game using structured "smart senses"

**原文标题**: LLM plays an 8-bit Commander X16 game using structured "smart senses"

**原文链接**: [https://pvp-ai.russell-harper.com](https://pvp-ai.russell-harper.com)

生成摘要时出错

---

## 66. Launch HN：Relvy (YC F24) – 自动化的值班操作手册

**原文标题**: Launch HN: Relvy (YC F24) – On-call runbooks, automated

**原文链接**: [https://www.relvy.ai](https://www.relvy.ai)

生成摘要时出错

---

## 67. Robots eat cars

**原文标题**: Robots eat cars

**原文链接**: [https://telemetry.endeff.com/p/robots-eat-cars](https://telemetry.endeff.com/p/robots-eat-cars)

生成摘要时出错

---

## 68. Show HN: CSS Studio. Design by hand, code by agent

**原文标题**: Show HN: CSS Studio. Design by hand, code by agent

**原文链接**: [https://cssstudio.ai](https://cssstudio.ai)

生成摘要时出错

---

## 69. Show HN: Druids – Build your own software factory

**原文标题**: Show HN: Druids – Build your own software factory

**原文链接**: [https://github.com/fulcrumresearch/druids](https://github.com/fulcrumresearch/druids)

生成摘要时出错

---

## 70. EFF is leaving X

**原文标题**: EFF is leaving X

**原文链接**: [https://www.eff.org/deeplinks/2026/04/eff-leaving-x](https://www.eff.org/deeplinks/2026/04/eff-leaving-x)

生成摘要时出错

---

## 71. Creating the Futurescape for the Fifth Element (2019)

**原文标题**: Creating the Futurescape for the Fifth Element (2019)

**原文链接**: [https://theasc.com/articles/fantastic-voyage-creating-the-futurescape-for-the-fifth-element](https://theasc.com/articles/fantastic-voyage-creating-the-futurescape-for-the-fifth-element)

生成摘要时出错

---

## 72. Lichess and Take Take Take Sign Cooperation Agreement

**原文标题**: Lichess and Take Take Take Sign Cooperation Agreement

**原文链接**: [https://lichess.org/@/Lichess/blog/lichess-and-take-take-take-sign-cooperation-agreement/DZS0S0Dy](https://lichess.org/@/Lichess/blog/lichess-and-take-take-take-sign-cooperation-agreement/DZS0S0Dy)

生成摘要时出错

---

## 73. Meta removes ads for social media addiction litigation

**原文标题**: Meta removes ads for social media addiction litigation

**原文链接**: [https://www.axios.com/2026/04/09/meta-social-media-addiction-ads](https://www.axios.com/2026/04/09/meta-social-media-addiction-ads)

生成摘要时出错

---

## 74. Knit File Formats

**原文标题**: Knit File Formats

**原文链接**: [https://soup.agnescameron.info//2026/03/25/kniterate-waste-section.html](https://soup.agnescameron.info//2026/03/25/kniterate-waste-section.html)

生成摘要时出错

---

## 75. VFX HQ: Visual Effects Headquarters (2000)

**原文标题**: VFX HQ: Visual Effects Headquarters (2000)

**原文链接**: [https://www.vfxhq.com/index.html](https://www.vfxhq.com/index.html)

生成摘要时出错

---

## 76. Top laptops to use with FreeBSD

**原文标题**: Top laptops to use with FreeBSD

**原文链接**: [https://freebsdfoundation.github.io/freebsd-laptop-testing/](https://freebsdfoundation.github.io/freebsd-laptop-testing/)

生成摘要时出错

---

## 77. Sorting Performance Rabbit Hole

**原文标题**: Sorting Performance Rabbit Hole

**原文链接**: [https://nibblestew.blogspot.com/2026/04/sorting-performance-rabbit-hole.html](https://nibblestew.blogspot.com/2026/04/sorting-performance-rabbit-hole.html)

生成摘要时出错

---

## 78. Reallocating $100/Month Claude Code Spend to Zed and OpenRouter

**原文标题**: Reallocating $100/Month Claude Code Spend to Zed and OpenRouter

**原文链接**: [https://braw.dev/blog/2026-04-06-reallocating-100-month-claude-spend/](https://braw.dev/blog/2026-04-06-reallocating-100-month-claude-spend/)

生成摘要时出错

---

## 79. Microsoft is employing dark patterns to goad users into paying for storage?

**原文标题**: Microsoft is employing dark patterns to goad users into paying for storage?

**原文链接**: [https://lzon.ca/posts/other/microsoft-user-abuse/](https://lzon.ca/posts/other/microsoft-user-abuse/)

生成摘要时出错

---

## 80. Sam Altman may control our future – can he be trusted?

**原文标题**: Sam Altman may control our future – can he be trusted?

**原文链接**: [https://www.newyorker.com/magazine/2026/04/13/sam-altman-may-control-our-future-can-he-be-trusted](https://www.newyorker.com/magazine/2026/04/13/sam-altman-may-control-our-future-can-he-be-trusted)

生成摘要时出错

---

## 81. Netflix Prices Went Up Again – I Bought a DVD Player Instead

**原文标题**: Netflix Prices Went Up Again – I Bought a DVD Player Instead

**原文链接**: [https://aywren.com/2026/04/09/netflix-prices-went-up-again-i-bought-a-dvd-player-instead/](https://aywren.com/2026/04/09/netflix-prices-went-up-again-i-bought-a-dvd-player-instead/)

生成摘要时出错

---

## 82. Show HN: Rust based eBook library for Python, with MIT license

**原文标题**: Show HN: Rust based eBook library for Python, with MIT license

**原文链接**: [https://github.com/arc53/fast-ebook](https://github.com/arc53/fast-ebook)

生成摘要时出错

---

## 83. Many African families spend fortunes burying their dead

**原文标题**: Many African families spend fortunes burying their dead

**原文链接**: [https://davidoks.blog/p/how-funerals-keep-africa-poor](https://davidoks.blog/p/how-funerals-keep-africa-poor)

生成摘要时出错

---

## 84. The effects of caffeine consumption do not decay with a ~5 hour half-life

**原文标题**: The effects of caffeine consumption do not decay with a ~5 hour half-life

**原文链接**: [https://www.lesswrong.com/posts/vefsxkGWkEMmDcZ7v/the-effects-of-caffeine-consumption-do-not-decay-with-a-5](https://www.lesswrong.com/posts/vefsxkGWkEMmDcZ7v/the-effects-of-caffeine-consumption-do-not-decay-with-a-5)

生成摘要时出错

---

## 85. Claude mixes up who said what

**原文标题**: Claude mixes up who said what

**原文链接**: [https://dwyer.co.za/static/claude-mixes-up-who-said-what-and-thats-not-ok.html](https://dwyer.co.za/static/claude-mixes-up-who-said-what-and-thats-not-ok.html)

生成摘要时出错

---

## 86. Zero-build privacy policies with Astro

**原文标题**: Zero-build privacy policies with Astro

**原文链接**: [https://www.openpolicy.sh/blog/no-build-astro](https://www.openpolicy.sh/blog/no-build-astro)

生成摘要时出错

---

## 87. Peers vote to ban pornography depicting sex acts between stepfamily members

**原文标题**: Peers vote to ban pornography depicting sex acts between stepfamily members

**原文链接**: [https://www.theguardian.com/society/2026/apr/10/porngraphy-depicting-sex-acts-between-stepfamily-members-banned-in-uk](https://www.theguardian.com/society/2026/apr/10/porngraphy-depicting-sex-acts-between-stepfamily-members-banned-in-uk)

生成摘要时出错

---

## 88. Doing Impressions: Monet's Early Caricatures (ca. late 1850s)

**原文标题**: Doing Impressions: Monet's Early Caricatures (ca. late 1850s)

**原文链接**: [https://publicdomainreview.org/collection/claude-monet-caricatures/](https://publicdomainreview.org/collection/claude-monet-caricatures/)

生成摘要时出错

---

## 89. Small Engines

**原文标题**: Small Engines

**原文链接**: [https://scottlocklin.wordpress.com/2026/03/25/very-small-engines/](https://scottlocklin.wordpress.com/2026/03/25/very-small-engines/)

生成摘要时出错

---

## 90. Peers vote to ban pornography depicting sex acts between stepfamily members

**原文标题**: Peers vote to ban pornography depicting sex acts between stepfamily members

**原文链接**: [https://www.theguardian.com/society/2026/apr/10/porngraphy-depicting-sex-acts-between-stepfamily-members-banned-in-uk](https://www.theguardian.com/society/2026/apr/10/porngraphy-depicting-sex-acts-between-stepfamily-members-banned-in-uk)

生成摘要时出错

---

## 91. Show HN: Moon simulator game, ray-casting

**原文标题**: Show HN: Moon simulator game, ray-casting

**原文链接**: [https://mooncraft2000.com](https://mooncraft2000.com)

生成摘要时出错

---

## 92. Building a framework-agnostic Ruby gem (and making sure it doesn't break)

**原文标题**: Building a framework-agnostic Ruby gem (and making sure it doesn't break)

**原文链接**: [https://newsletter.masilotti.com/p/on-building-a-framework-agnostic](https://newsletter.masilotti.com/p/on-building-a-framework-agnostic)

生成摘要时出错

---

## 93. Introduction to Nintendo DS Programming

**原文标题**: Introduction to Nintendo DS Programming

**原文链接**: [https://www.patater.com/files/projects/manual/manual.html](https://www.patater.com/files/projects/manual/manual.html)

生成摘要时出错

---

## 94. Clean code in the age of coding agents

**原文标题**: Clean code in the age of coding agents

**原文链接**: [https://www.yanist.com/clean-code-in-the-age-of-coding-agents/](https://www.yanist.com/clean-code-in-the-age-of-coding-agents/)

生成摘要时出错

---

## 95. Understanding Traceroute

**原文标题**: Understanding Traceroute

**原文链接**: [https://tech.stonecharioteer.com/posts/2026/traceroute/](https://tech.stonecharioteer.com/posts/2026/traceroute/)

生成摘要时出错

---

## 96. How Pizza Tycoon simulated traffic on a 25 MHz CPU

**原文标题**: How Pizza Tycoon simulated traffic on a 25 MHz CPU

**原文链接**: [https://pizzalegacy.nl/blog/traffic-system.html](https://pizzalegacy.nl/blog/traffic-system.html)

生成摘要时出错

---

## 97. New iPhone age and identity checks restrict internet freedom in the UK

**原文标题**: New iPhone age and identity checks restrict internet freedom in the UK

**原文链接**: [https://bigbrotherwatch.org.uk/blog/apples-new-iphone-update-is-restricting-internet-freedom-in-the-uk/](https://bigbrotherwatch.org.uk/blog/apples-new-iphone-update-is-restricting-internet-freedom-in-the-uk/)

生成摘要时出错

---

## 98. Who is Satoshi Nakamoto? My quest to unmask Bitcoin's creator

**原文标题**: Who is Satoshi Nakamoto? My quest to unmask Bitcoin's creator

**原文链接**: [https://www.nytimes.com/2026/04/08/business/bitcoin-satoshi-nakamoto-identity-adam-back.html](https://www.nytimes.com/2026/04/08/business/bitcoin-satoshi-nakamoto-identity-adam-back.html)

生成摘要时出错

---

## 99. Installing OpenBSD on the Pomera DM250{,XY?}

**原文标题**: Installing OpenBSD on the Pomera DM250{,XY?}

**原文链接**: [https://jcs.org/2026/04/09/openbsd-dm250](https://jcs.org/2026/04/09/openbsd-dm250)

生成摘要时出错

---

## 100. YouTube locked my accounts and I can't cancel my subscription

**原文标题**: YouTube locked my accounts and I can't cancel my subscription

**原文链接**: [https://pocketables.com/2026/04/ai-music-corporate-control-and-the-creator-who-cant-even-leave.html](https://pocketables.com/2026/04/ai-music-corporate-control-and-the-creator-who-cant-even-leave.html)

生成摘要时出错

---

