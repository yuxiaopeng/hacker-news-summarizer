# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-31.md)

*最后自动更新时间: 2026-10-31 20:46:52*
## 1. TCP 释放后重用：CVE-2026-98432 / CVSS 9.8

**原文标题**: TCP Use-After-Free: CVE-2026-98432 / CVSS 9.8

**原文链接**: [https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf](https://atlasum.net/blog/cve-2026-98432-linux-ipv4-tcp-uaf)

CVE-2026-98432 是 Linux 内核 IPv4 TCP 握手中的一个严重释放后重用（use-after-free）漏洞，CVSS 评分为 9.8。该漏洞影响 4.4 及以上版本的内核，存在于初始连接阶段处理 IPv4 选项的代码中。由于内核可能会在另一个 CPU 仍在访问选项数据时将其释放，远程且未经身份验证的攻击者可触发内存损坏、系统崩溃或内核堆泄露。

**关键影响与利用**
Anthropic 的研究表明，该漏洞可被用于远程代码执行，从而在无需凭据的情况下获取 root 权限。虽然该缺陷存在于标准 TCP 处理流程中，但目前已知的利用方式专门针对启用了多路径 TCP (MPTCP) 监听器的服务器。一个显著的风险因素是，在进行任何应用层身份验证之前即可触发该漏洞。

**补丁状态**
上游修复程序已于 2026 年 10 月 11 日至 18 日期间针对主要稳定分支（包括 5.10、6.1、6.6、6.12 和 7.3）发布。截至 2026 年 10 月下旬，各发行版的状态如下：
*   **已修复：** Debian、SUSE、Oracle Linux (UEK) 及特定的 Amazon Linux 2023 内核。
*   **受影响/待处理：** Ubuntu（所有版本）、RHEL (8, 9, 10) 和 Amazon Linux 2。

**修复建议**
1.  **更新并重启：** 首要修复措施是将内核更新至已修复版本并重启主机。
2.  **缓解措施：** 若无法及时修补，管理员可以使用 `nftables` 丢弃头部长度大于 5 的 IPv4 TCP 数据包。这将拦截包含 IPv4 选项（极少用于合法用途）的数据包，从而阻止漏洞利用程序触发受影响的代码路径。
3.  **配置：** 在应用补丁之前，禁用或限制 MPTCP 监听器的暴露。

---

## 2. GPT-5.6 Sol 可以在和平模式下通关《异星工厂》

**原文标题**: GPT-5.6 Sol can beat Factorio on peaceful mode

**原文链接**: [https://ryanmadden.net/gpt-56-beats-factorio/](https://ryanmadden.net/gpt-56-beats-factorio/)

本文详细记录了一次成功的实验：AI 智能体 **GPT-5.6 Sol** 在和平模式下历时 13.5 小时成功通关《异星工厂》（Factorio）。该模型在 Codex 中以“低思考水平”运行，通过一个基于 Python 的管理程序与游戏交互，该程序强制执行了诸如触及距离和战争迷雾等类人限制。

实验的核心结论包括：

*   **物流能力提升：** 相比于在传送带等基础机制上表现挣扎的 GPT-5.5 模型，Sol 展现出了显著的进步。
*   **后期扩展瓶颈：** 尽管 Sol 在游戏前期表现超出预期，但随着游戏推进，其管理复杂生产系统的能力开始下降。
*   **问题解决策略：** 为了弥补无法构建高效后期物流网络的缺陷，Sol 采取了“手动”补救措施，在不同工厂区域间反复搬运物资，以确保火箭最终发射。
*   **AI 基准测试：** 作者认为《异星工厂》可以作为编程和通用问题解决能力的绝佳代理指标。由于游戏过程对观察者而言高度透明，它为建立关于模型能力和自主行为的直观感受提供了一个独特的媒介。

作者计划通过测试不同的思考水平，并在非和平模式中引入“食人虫”敌人，进一步挑战该模型的自主性，从而继续这项研究。

---

## 3. 学者的职责

**原文标题**: The Duty of a Scholar

**原文链接**: [https://www.daemonology.net/blog/2026-10-31-The-Duty-of-a-Scholar.html](https://www.daemonology.net/blog/2026-10-31-The-Duty-of-a-Scholar.html)

在《学者的职责》（The Duty of a Scholar）中，作者回顾了他在2005年发现的英特尔超线程技术中的一个关键安全漏洞，该漏洞可导致RSA加密密钥被盗。作者并未优先考虑自己尚在起步阶段的职业生涯或博士论文，而是投入了六个月时间进行“协同披露”，与安全团队私下合作，以确保在漏洞公开前完成补丁的准备工作。

作者通过这一经历探讨了专业知识持有者的伦理义务。他将这种责任与IEEE等专业工程行为准则相联系，这些准则规定，公众的安全与福祉必须优先于个人或雇主的利益。

借鉴让-卢克·皮卡德（Jean-Luc Picard）的“对真理的职责”以及约翰·戈特利布·费希特（Johann Gottlieb Fichte）的哲学思想，作者指出知识是为社会所代管的。他在创造新知识的“研究者”与将知识传递给需求者的“学者”之间做了严谨的区分。在作者看来，真正的学者不仅仅是发表论文，更要积极寻找那些能够针对研究发现采取行动的人。

最后，作者承认履行这一职责的能力往往取决于社会和经济的稳定性。他指出，由于加拿大的社会安全网和他当时的个人境况，他才得以优先考虑公众安全。最终，他将学者的天职定义为一种“知识的职责”：这是一种伦理承诺，旨在确保真理不仅被发现，还能得到有效传播，从而保护并造福公众。

---

## 4. 笨蛋，关键是内存延迟。

**原文标题**: It's the Memory Latency, Stupid

**原文链接**: [https://pivotlake.io/blog/its-the-memory-latency-stupid/](https://pivotlake.io/blog/its-the-memory-latency-stupid/)

本文探讨了数据库性能中内存延迟这一关键瓶颈，并指出高 CPU 使用率往往掩盖了 CPU 因等待内存（RAM）数据而处于闲置状态的真相。

**核心问题**
虽然 CPU 每纳秒能处理 4–8 条指令，但单次内存访问却需要 50–100 纳秒。这意味着在从内存获取数据的时间内，CPU 理论上可以执行 400–800 条指令。虽然 CPU 缓存（L1、L2 和 L3）通过让数据更贴近处理器来缓解这一问题，但由于其容量较小，需要专门的算法才能发挥效用。

**案例研究：GROUP BY 聚合**
作者通过对一个包含 9900 万行的数据集进行“GROUP BY”查询来论证这一点。
*   **朴素方法：** 使用单个大型哈希表会导致“冷”命中，因为哈希表超过了缓存容量。这迫使 CPU 为了等待内存数据而停顿。性能指标显示，CPU 有 50.1% 的时间处于停顿状态，只有 16.1% 的周期实际完成了操作。
*   **优化方法（基数分区）：** 通过先将键（Keys）哈希到 4,096 个较小的分区中，引擎确保了随后的哈希表能完全放入 CPU 缓存内。

**主要结果**
尽管基数分区法执行的总指令数更多，但由于它减少了内存停顿，其运行速度显著提升。在测试中，该优化：
*   将执行时间从 3.6 秒缩短至 2.7 秒。
*   将内存停顿率从 50.1% 降至 23.5%。
*   将从内存提取的数据量从 4.5GB 减少到 1.5GB。

**结论**
作者总结道，性能工程的关键不在于减少原始指令数量，而在于最大化缓存利用率并“隐藏”内存延迟。利用这些技术，作者开发的“Pivot”引擎最终实现了仅 171 毫秒的并行执行时间。

---

## 5. Hackers hijack Egypt highway billboard and Malaysian screens to show porn

**原文标题**: Hackers hijack Egypt highway billboard and Malaysian screens to show porn

**原文链接**: [https://www.cairoreport.org/p/egypt-brazil-iraq-billboard-hack](https://www.cairoreport.org/p/egypt-brazil-iraq-billboard-hack)

生成摘要时出错

---

## 6. Show HN：NES 魂斗罗 (1987) 移植版 (ASM -> C，再由 C -> WebAssembly)

**原文标题**: Show HN: NES Contra (1987) port (ASM –> C and then C –> WebAssembly)

**原文链接**: [https://epoyraz.github.io/nes-contra-us/](https://epoyraz.github.io/nes-contra-us/)

本项目是 1987 年经典 NES 游戏《魂斗罗》（Contra）的网页移植版，旨在通过 WebAssembly 在浏览器中原生运行。

技术实现过程涉及将原始的 6502 汇编代码移植为 C 语言，随后将其编译为 WebAssembly (Wasm)。这种方法使游戏无需传统模拟器，即可在现代浏览器中高效运行。

**核心功能：**
*   **游戏模式：** 支持单人模式及完善的在线双人模式。用户可以创建房间并分享邀请链接，进行远程联机协作。
*   **操作方式：** 游戏支持键盘映射（方向键移动，空格/A 键跳跃，S 键开火），并为移动设备提供屏幕触控操作。
*   **双人设置：** 开启双人模式时，房主需在标题界面使用 Shift 键（Select）切换菜单。

该移植版旨在保留任天堂原版游戏的怀旧体验，同时利用现代网页技术使其触手可及。

---

## 7. Molly (Signal 分支) 已有 3 个月未更新，且存在安全漏洞。

**原文标题**: Molly (Signal fork) has not been updated since 3 months and is vulnerable

**原文链接**: [https://piefed.world/post/1503394](https://piefed.world/post/1503394)

该社区讨论向用户发出警示：Signal 通讯应用的加固分支 Molly 已超过三个月未更新（自2024年7月31日起）。因此，它目前存在安全漏洞，而这些漏洞在 Signal 官方应用（特别是 8.27.1 及更高版本）中已得到修复。

**核心要点：**

*   **安全风险：** Molly 缺少 Signal 在 10 月发布的关键安全补丁。发帖者建议在更新恢复前卸载 Molly 并换回 Signal 官方应用。
*   **用户选择 Molly 的原因：** 尽管存在风险，用户仍青睐 Molly 提供的官方客户端所缺失的功能，包括：
    *   **UnifiedPush：** 允许在去谷歌化的手机上无需 Google Play 服务即可接收通知。
    *   **数据库加密：** 为本地消息存储提供额外的安全保障。
    *   **F-Droid 供应：** 方便不使用 Play 商店的用户安装。
*   **官方 Signal 的改进：** 评论者指出，官方 Signal 现在已支持将安卓平板作为辅助设备关联（此前这是使用 Molly 的主要原因），并在其官网上提供独立 APK，利用 Websockets 实现无需谷歌服务的通知功能。
*   **建议的替代方案：**
    *   **Signal-FOSS：** 一个去除了闭源组件并支持自动更新的 Signal 版本。
    *   **Obtainium：** 一款用于直接从 GitHub 或官方网站追踪并安装 APK 更新的应用。
    *   **官方 Signal APK：** 直接从 Signal 官网获取，适用于没有 Google Play 的用户。

参与者的共识是：虽然 Molly 提供了更优越的隐私功能，但目前其安全性与官方 Signal 存在差距，因此不建议在日常生活中使用。

---

## 8. HackerTube: YouTube built from videos recommended by HN

**原文标题**: HackerTube: YouTube built from videos recommended by HN

**原文链接**: [https://karpathy.bearblog.dev/hacker-tube/](https://karpathy.bearblog.dev/hacker-tube/)

生成摘要时出错

---

## 9. Jepsen：ParticleDB 1.1.4

**原文标题**: Jepsen: ParticleDB 1.1.4

**原文链接**: [https://jepsen.io/analyses/particledb-1.1.4](https://jepsen.io/analyses/particledb-1.1.4)

Jepsen 对 ParticleDB（版本 1.1.4 至 1.1.18.11.rc-22）的调查揭示了该系统营销宣称与实际表现之间的巨大反差。ParticleDB 由 Orkes 开发，被定位为面向 AI 应用、基于 Rust 的高性能 Postgres 和 Redis 继任者，并宣称符合“完全 ACID”标准且拥有正式的 TLA+ 证明。然而，Jepsen 的测试（仅限于单节点实例）发现了 96 个问题，涵盖了从性能故障到严重数据损坏的各个方面。

关键发现包括：

*   **安全性和文档不一致：** 营销承诺了可串行化和形式化验证，但 TLA+ 证明并不可用。事务隔离由混乱的启动标志（`--txn-mode`）而非标准 SQL 命令控制，且关于这些模式安全性的文档不仅相互矛盾，而且往往不准确。
*   **性能和稳定性问题：** 在最严格的隔离模式（`table-2pl`）下，性能“极其糟糕”，基本不可用。即使在健康的单节点环境中，系统在并发操作期间也会频繁出现神秘崩溃和长期的死锁。
*   **Postgres 兼容性受损：** 尽管宣称原生支持 Postgres 协议，但许多功能缺失或严重损坏，包括预处理语句、`CASE` 表达式中的聚合以及基础数学运算符的失效。
*   **内部一致性失效：** 测试发现谓词、约束和连接（join）存在重大问题。在某些情况下，事务表现出“僵尸”行为，或无法读取其自身先前的写入，导致状态损坏。

总之，Jepsen 发现 ParticleDB 1.1.4 未能履行其在安全性、持久性和兼容性方面的保证。尽管该数据库旨在统一各种工作负载，但在测试中证明其既不可靠也不稳定，经常无法维持基本的内部一致性。

---

## 10. Show HN: A language model that lives in a boot sector

**原文标题**: Show HN: A language model that lives in a boot sector

**原文链接**: [https://github.com/kerlenton/bootgpt](https://github.com/kerlenton/bootgpt)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 2 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 3 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 4 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 5 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 6 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 7 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 8 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 9 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 10 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 11 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 12 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 13 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 14 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 15 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 16 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 17 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 18 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 19 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 20 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 21 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 22 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 23 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 24 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 25 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 26 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 27 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 28 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 29 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 30 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 31 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 32 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 33 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 34 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 35 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 36 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 37 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 38 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 39 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 40 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 41 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 42 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 43 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 44 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 45 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 46 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 47 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 48 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 49 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 50 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 51 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 52 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 53 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 54 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 55 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 56 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 57 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 58 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 59 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 60 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 61 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 62 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 63 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 64 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 65 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 66 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 67 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 68 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 69 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 70 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 71 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 72 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 73 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 74 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 75 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 76 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 77 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 78 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 79 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 80 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 81 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 82 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 83 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 84 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 85 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 86 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 87 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 88 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 89 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 90 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 91 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 92 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 93 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 94 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 95 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 96 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 97 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 98 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 99 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 100 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 101 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 102 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 103 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 104 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 105 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 106 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 107 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 108 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 109 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 110 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 111 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 112 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 113 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 114 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 115 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 116 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 117 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 118 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 119 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 120 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 121 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 122 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 123 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 124 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 125 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 126 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 127 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 128 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 129 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 130 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 131 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 132 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 133 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 134 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 135 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 136 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 137 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 138 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 139 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 140 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 141 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 142 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 143 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 144 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 145 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 146 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 147 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 148 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 149 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 150 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 151 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 152 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 153 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 154 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 155 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 156 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 157 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 158 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 159 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 160 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 161 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 162 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 163 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 164 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 165 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 166 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 167 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 168 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 169 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 170 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 171 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 172 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 173 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 174 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 175 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 176 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 177 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 178 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 179 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 180 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 181 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 182 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 183 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 184 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 185 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 186 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 187 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 188 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 189 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 190 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 191 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 192 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 193 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 194 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 195 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 196 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 197 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 198 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 199 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 200 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 201 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 202 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 203 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 204 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 205 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 206 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 207 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 208 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 209 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 210 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 211 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 212 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 213 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 214 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 215 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 216 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 217 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 218 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 219 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 220 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 221 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 222 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 223 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 224 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 225 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 226 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 227 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 228 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 229 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 230 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 231 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 232 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 233 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 234 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 235 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 236 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 237 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 238 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 239 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 240 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 241 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 242 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 243 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 244 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 245 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 246 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 247 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 248 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 249 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 250 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 251 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 252 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 253 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 254 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 255 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 256 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 257 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 258 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 259 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 260 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 261 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 262 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 263 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 264 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 265 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 266 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 267 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 268 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 269 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 270 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 271 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 272 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 273 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 274 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 275 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 276 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 277 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 278 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 279 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 280 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 281 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 282 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 283 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 284 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 285 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 286 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 287 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 288 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 289 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 290 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 291 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 292 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 293 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 294 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 295 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 296 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 297 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 298 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 299 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 300 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 301 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 302 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 303 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 304 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 305 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 306 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 307 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 308 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 309 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 310 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 311 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 312 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 313 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 314 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 315 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 316 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 317 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 318 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 319 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 320 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 321 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 322 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 323 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 324 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 325 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 326 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 327 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 328 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 329 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 330 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 331 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 332 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 333 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 334 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 335 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 336 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 337 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 338 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 339 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 340 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 341 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 342 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 343 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 344 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 345 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 346 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 347 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 348 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 349 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 350 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 351 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 352 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 353 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 354 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 355 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 356 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 357 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 358 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 359 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 360 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 361 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 362 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 363 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 364 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 365 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 366 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 367 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 368 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 369 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 370 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 371 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 372 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 373 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 374 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 375 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 376 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 377 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 378 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 379 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 380 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 381 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 382 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 383 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 384 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 385 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 386 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 387 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 388 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 389 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 390 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 391 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 392 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 393 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 394 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 395 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 396 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 397 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 398 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 399 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 400 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 401 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 402 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 403 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 404 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 405 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 406 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 407 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 408 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 409 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 410 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 411 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 412 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 413 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 414 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 415 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 416 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 417 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 418 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 419 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 420 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 421 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 422 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 423 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 424 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 425 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 426 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 427 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 428 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 429 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 430 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 431 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 432 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 433 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 434 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 435 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 436 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 437 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 438 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 439 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 440 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 441 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 442 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 443 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 444 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 445 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 446 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 447 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 448 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 449 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 450 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 451 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 452 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 453 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 454 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 455 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 456 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 457 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 458 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 459 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 460 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 461 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 462 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 463 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 464 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 465 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 466 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 467 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 468 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 469 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 470 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 471 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 472 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 473 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 474 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 475 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 476 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 477 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 478 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 479 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 480 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 481 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 482 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 483 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 484 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 485 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 486 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 487 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 488 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 489 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 490 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 491 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 492 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 493 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 494 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 495 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 496 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 497 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 498 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 499 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 500 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 501 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 502 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 503 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 504 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 505 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 506 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 507 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 508 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 509 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 510 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 511 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 512 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 513 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 514 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 515 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 516 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 517 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 518 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 519 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 520 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 521 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 522 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 523 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 524 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 525 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 526 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 527 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 528 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 529 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 530 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 531 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 532 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 533 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 534 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 535 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 536 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 537 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 538 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 539 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 540 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 541 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 542 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 543 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 544 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 545 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 546 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 547 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 548 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 549 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 550 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 551 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 552 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 553 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 554 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 555 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 556 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 557 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 558 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 559 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 560 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 561 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 562 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 563 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 564 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 565 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 566 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 567 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 568 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 569 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 570 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 571 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 572 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 573 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 574 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 575 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 576 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 577 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 578 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 579 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 580 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 581 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 582 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 583 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 584 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 585 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 586 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 587 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 588 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
