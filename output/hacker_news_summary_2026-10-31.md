# Hacker News 热门文章摘要 (2026-10-31)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Do the math: How we took over ChatGPT accounts

**原文标题**: Do the math: How we took over ChatGPT accounts

**原文链接**: [https://www.parameter.ai/labs/we-found-a-gap-at-openai](https://www.parameter.ai/labs/we-found-a-gap-at-openai)

生成摘要时出错

---

## 12. Much Ado About None: Sentinel Values in Python

**原文标题**: Much Ado About None: Sentinel Values in Python

**原文链接**: [https://florianwilhelm.info/2026/10/sentinel_values/](https://florianwilhelm.info/2026/10/sentinel_values/)

生成摘要时出错

---

## 13. Redox: Ring Buffers Project Summary

**原文标题**: Redox: Ring Buffers Project Summary

**原文链接**: [https://www.redox-os.org/news/nlnet-rb-summary/](https://www.redox-os.org/news/nlnet-rb-summary/)

生成摘要时出错

---

## 14. I post trained a model on Demoscenes

**原文标题**: I post trained a model on Demoscenes

**原文链接**: [https://datavorous.com/writing/demoscener/](https://datavorous.com/writing/demoscener/)

生成摘要时出错

---

## 15. Noctua Fan Swap on a Calnex Rb/GPS Frequency Reference

**原文标题**: Noctua Fan Swap on a Calnex Rb/GPS Frequency Reference

**原文链接**: [https://www.jeffgeerling.com/blog/2026/noctua-fan-swap-calnex-rb-gps-frequency-reference/](https://www.jeffgeerling.com/blog/2026/noctua-fan-swap-calnex-rb-gps-frequency-reference/)

生成摘要时出错

---

## 16. William Nordhaus has died

**原文标题**: William Nordhaus has died

**原文链接**: [https://news.yale.edu/2026/10/31/william-nordhaus-nobel-laureate-who-integrated-economics-and-climate-change-devoted-yale](https://news.yale.edu/2026/10/31/william-nordhaus-nobel-laureate-who-integrated-economics-and-climate-change-devoted-yale)

生成摘要时出错

---

## 17. Simple circuits can create complex behaviors

**原文标题**: Simple circuits can create complex behaviors

**原文链接**: [https://aatishb.com/myriad/lets-build-a-brain/](https://aatishb.com/myriad/lets-build-a-brain/)

生成摘要时出错

---

## 18. 阅读与写作并不像你（可能）认为的那样对称

**原文标题**: Reading and writing are less symmetric than you (probably) think

**原文链接**: [https://fgiesen.wordpress.com/2015/10/25/reading-and-writing-are-less-symmetric-than-you-probably-think/](https://fgiesen.wordpress.com/2015/10/25/reading-and-writing-are-less-symmetric-than-you-probably-think/)

生成摘要时出错

---

## 19. Switch Lowering in GCC

**原文标题**: Switch Lowering in GCC

**原文链接**: [https://xoranth.net/gcc-switch/](https://xoranth.net/gcc-switch/)

生成摘要时出错

---

## 20. Serbia just elected the world's brainiest parliament

**原文标题**: Serbia just elected the world's brainiest parliament

**原文链接**: [https://www.science.org/content/article/serbia-just-elected-world-s-brainiest-parliament](https://www.science.org/content/article/serbia-just-elected-world-s-brainiest-parliament)

生成摘要时出错

---

## 21. Casio Watches of the 1980s

**原文标题**: Casio Watches of the 1980s

**原文链接**: [https://www.casio.com/us/watches/50th/Heritage/1980s/](https://www.casio.com/us/watches/50th/Heritage/1980s/)

生成摘要时出错

---

## 22. Digital minimalism

**原文标题**: Digital minimalism

**原文链接**: [https://vitalik.eth.limo/general/2026/10/31/digital_minimalism.html](https://vitalik.eth.limo/general/2026/10/31/digital_minimalism.html)

生成摘要时出错

---

## 23. Show HN: Ghostman – A fast, keyboard-driven TUI API client and webhook inspector

**原文标题**: Show HN: Ghostman – A fast, keyboard-driven TUI API client and webhook inspector

**原文链接**: [https://github.com/4yk5/Ghostman](https://github.com/4yk5/Ghostman)

生成摘要时出错

---

## 24. Malware uses LLMs to rank victims by how much they're worth

**原文标题**: Malware uses LLMs to rank victims by how much they're worth

**原文链接**: [https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/](https://blog.talosintelligence.com/appraisal-by-ai-model-driven-victim-prioritization-in-the-volta-infostealer/)

生成摘要时出错

---

## 25. Show HN: A USB-C LTE modem that gives my computer a phone line

**原文标题**: Show HN: A USB-C LTE modem that gives my computer a phone line

**原文链接**: [https://github.com/Koppar-AI/koppar-lte-modem](https://github.com/Koppar-AI/koppar-lte-modem)

生成摘要时出错

---

## 26. AI, Lean, and the Future of Formal Verification, with Lean Creator Leo de Moura

**原文标题**: AI, Lean, and the Future of Formal Verification, with Lean Creator Leo de Moura

**原文链接**: [https://thedataexchange.media/leo-de-moura-lean-aws/](https://thedataexchange.media/leo-de-moura-lean-aws/)

生成摘要时出错

---

## 27. The Impact of Generative AI on Critical Thinking: Self-Reported (2025)

**原文标题**: The Impact of Generative AI on Critical Thinking: Self-Reported (2025)

**原文链接**: [https://dl.acm.org/doi/full/10.1145/3706598.3713778](https://dl.acm.org/doi/full/10.1145/3706598.3713778)

生成摘要时出错

---

## 28. What is a light-day? The milestone Voyager 1 is closing in on

**原文标题**: What is a light-day? The milestone Voyager 1 is closing in on

**原文链接**: [https://science.nasa.gov/mission/voyager/voyager-1/voyager-1-what-is-a-light-day/](https://science.nasa.gov/mission/voyager/voyager-1/voyager-1-what-is-a-light-day/)

生成摘要时出错

---

## 29. Show HN: Marelleo, an open-source story box I built for my kids using ESP32

**原文标题**: Show HN: Marelleo, an open-source story box I built for my kids using ESP32

**原文链接**: [https://zebra.rodeo/en/blog/marelleo/](https://zebra.rodeo/en/blog/marelleo/)

生成摘要时出错

---

## 30. Copyright Office is restoring copyright to something you have to work to get

**原文标题**: Copyright Office is restoring copyright to something you have to work to get

**原文链接**: [https://pluralistic.net/2026/10/31/burn-berne/#unvictored](https://pluralistic.net/2026/10/31/burn-berne/#unvictored)

生成摘要时出错

---

## 31. Prospero: A new coding harness for a more civilized age

**原文标题**: Prospero: A new coding harness for a more civilized age

**原文链接**: [https://nullprogram.com/blog/2026/10/31/](https://nullprogram.com/blog/2026/10/31/)

生成摘要时出错

---

## 32. Hunting 'Zombie Accounts' in Active Directory

**原文标题**: Hunting 'Zombie Accounts' in Active Directory

**原文链接**: [https://www.fabian.fyi/2026/10/zombie-hunt.html](https://www.fabian.fyi/2026/10/zombie-hunt.html)

生成摘要时出错

---

## 33. Cloudflare Turnstile solver library (no headless browser required)

**原文标题**: Cloudflare Turnstile solver library (no headless browser required)

**原文链接**: [https://github.com/chris124567/cfsolve](https://github.com/chris124567/cfsolve)

生成摘要时出错

---

## 34. Enlightenment 0.28 Released with Many Improvements

**原文标题**: Enlightenment 0.28 Released with Many Improvements

**原文链接**: [https://www.phoronix.com/news/Enlightenment-0.28](https://www.phoronix.com/news/Enlightenment-0.28)

生成摘要时出错

---

## 35. Show HN: Jointter – A daily word puzzle using dots and lines

**原文标题**: Show HN: Jointter – A daily word puzzle using dots and lines

**原文链接**: [https://www.jointter.com/](https://www.jointter.com/)

生成摘要时出错

---

## 36. Backdoor in Claude Code for VS Code extension on the Cursor Marketplace

**原文标题**: Backdoor in Claude Code for VS Code extension on the Cursor Marketplace

**原文链接**: [https://phorion.io/blog/offical-claude-code-vsx-compromise/](https://phorion.io/blog/offical-claude-code-vsx-compromise/)

生成摘要时出错

---

## 37. The oldest ice disappears and the Stone Age emerges from it

**原文标题**: The oldest ice disappears and the Stone Age emerges from it

**原文链接**: [https://www.sciencenorway.no/archaeology-climate-culture/the-oldest-ice-is-disappearing-the-stone-age-is-emerging-from-the-melting-ice/2713921](https://www.sciencenorway.no/archaeology-climate-culture/the-oldest-ice-is-disappearing-the-stone-age-is-emerging-from-the-melting-ice/2713921)

生成摘要时出错

---

## 38. Crypto firm Binance covers 90% of losses after $6.3B hack

**原文标题**: Crypto firm Binance covers 90% of losses after $6.3B hack

**原文链接**: [https://www.bbc.com/news/articles/ckpdg3ql4169o](https://www.bbc.com/news/articles/ckpdg3ql4169o)

生成摘要时出错

---

## 39. UK Green party drops longstanding opposition to nuclear power

**原文标题**: UK Green party drops longstanding opposition to nuclear power

**原文链接**: [https://www.theguardian.com/politics/2026/oct/05/green-party-nuclear-power-policy](https://www.theguardian.com/politics/2026/oct/05/green-party-nuclear-power-policy)

生成摘要时出错

---

## 40. Longitudinal Changes InWearable-Captured PhysiologyBefore Sudden Cardiac Death

**原文标题**: Longitudinal Changes InWearable-Captured PhysiologyBefore Sudden Cardiac Death

**原文链接**: [https://www.jacc.org/doi/epdf/10.1016/j.jaccas.2026.110397](https://www.jacc.org/doi/epdf/10.1016/j.jaccas.2026.110397)

生成摘要时出错

---

## 41. Anthropic blocks users for anything touching training larger models

**原文标题**: Anthropic blocks users for anything touching training larger models

**原文链接**: [https://twitter.com/jiahaoshao1/status/2116475922190922088](https://twitter.com/jiahaoshao1/status/2116475922190922088)

生成摘要时出错

---

## 42. AI Data Centers Could Erase 15 Years of America's Climate Progress by 2030

**原文标题**: AI Data Centers Could Erase 15 Years of America's Climate Progress by 2030

**原文链接**: [https://www.gadgetreview.com/ai-data-centers-could-erase-15-years-of-americas-climate-progress-by-2030](https://www.gadgetreview.com/ai-data-centers-could-erase-15-years-of-americas-climate-progress-by-2030)

生成摘要时出错

---

## 43. Useful Custom-Media Presets

**原文标题**: Useful Custom-Media Presets

**原文链接**: [https://blog.master.dev/useful-custom-media-presets/](https://blog.master.dev/useful-custom-media-presets/)

生成摘要时出错

---

## 44. Nonna – TypeScript Dependency injection without the reflection tax

**原文标题**: Nonna – TypeScript Dependency injection without the reflection tax

**原文链接**: [https://nonna.nodeboot.io/](https://nonna.nodeboot.io/)

生成摘要时出错

---

## 45. CVE-2026-98432: Linux IPv4 UAF

**原文标题**: CVE-2026-98432: Linux IPv4 UAF

**原文链接**: [https://nvd.nist.gov/vuln/detail/cve-2026-98432](https://nvd.nist.gov/vuln/detail/cve-2026-98432)

生成摘要时出错

---

## 46. The $6.3B Binance hack was pulled off in just 20 minutes

**原文标题**: The $6.3B Binance hack was pulled off in just 20 minutes

**原文链接**: [https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/](https://www.wired.com/story/the-dollar63-billion-binance-hack-was-pulled-off-in-just-20-minutes/)

生成摘要时出错

---

## 47. Jules Verne's Lost Novel

**原文标题**: Jules Verne's Lost Novel

**原文链接**: [https://blue-continuum.com/verne-paris](https://blue-continuum.com/verne-paris)

生成摘要时出错

---

## 48. HTTP/3 is faster with some work and help from Cloudflare

**原文标题**: HTTP/3 is faster with some work and help from Cloudflare

**原文链接**: [https://www.theregister.com/devops/2026/10/30/http/3-is-faster-with-some-work-and-help-from-cloudflare/5306767](https://www.theregister.com/devops/2026/10/30/http/3-is-faster-with-some-work-and-help-from-cloudflare/5306767)

生成摘要时出错

---

## 49. Trapped in the Technologist Factory

**原文标题**: Trapped in the Technologist Factory

**原文链接**: [https://ideolalia.com/essays/trapped-in-the-technologist-factory.html](https://ideolalia.com/essays/trapped-in-the-technologist-factory.html)

生成摘要时出错

---

## 50. I'm a Proton employee and I'm breaking my silence

**原文标题**: I'm a Proton employee and I'm breaking my silence

**原文链接**: [https://www.reddit.com/r/ProtonMail/comments/1xkezig/im_a_proton_employee_and_im_breaking_my_silence/](https://www.reddit.com/r/ProtonMail/comments/1xkezig/im_a_proton_employee_and_im_breaking_my_silence/)

生成摘要时出错

---

## 51. Keeping the Bonfires Lit

**原文标题**: Keeping the Bonfires Lit

**原文链接**: [https://www.historytoday.com/archive/out-margins/keeping-bonfires-lit](https://www.historytoday.com/archive/out-margins/keeping-bonfires-lit)

生成摘要时出错

---

## 52. Anthropic's Claude AI blocks video game cloning and reverse-engineering

**原文标题**: Anthropic's Claude AI blocks video game cloning and reverse-engineering

**原文链接**: [https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked](https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked)

生成摘要时出错

---

## 53. Show HN: To Honor Sir Patrick Stewart, Enjoy the TNG Episode Guessing Game

**原文标题**: Show HN: To Honor Sir Patrick Stewart, Enjoy the TNG Episode Guessing Game

**原文链接**: [https://tng.episodle.com/](https://tng.episodle.com/)

生成摘要时出错

---

## 54. Wasmer (YC S19) Is Hiring OS/Hypervisor Experts in Europe

**原文标题**: Wasmer (YC S19) Is Hiring OS/Hypervisor Experts in Europe

**原文链接**: [https://www.workatastartup.com/jobs/98722](https://www.workatastartup.com/jobs/98722)

生成摘要时出错

---

## 55. Sanstun: A sans-IO, parallel-friendly WireGuard implementation in Rust

**原文标题**: Sanstun: A sans-IO, parallel-friendly WireGuard implementation in Rust

**原文链接**: [https://www.firezone.dev/blog/introducing-sanstun](https://www.firezone.dev/blog/introducing-sanstun)

生成摘要时出错

---

## 56. My favourite PowerMac is a Nintendo Wii

**原文标题**: My favourite PowerMac is a Nintendo Wii

**原文链接**: [https://virtuallyfun.com/2026/10/29/my-favourite-powermac-is-a-nintendo-wii/](https://virtuallyfun.com/2026/10/29/my-favourite-powermac-is-a-nintendo-wii/)

生成摘要时出错

---

## 57. Homebrew 68000 computer with a PCI bus

**原文标题**: Homebrew 68000 computer with a PCI bus

**原文链接**: [https://maniek86.xyz/projects/homebrew_m68k_pci.php](https://maniek86.xyz/projects/homebrew_m68k_pci.php)

生成摘要时出错

---

## 58. Building an AI-native engineering org

**原文标题**: Building an AI-native engineering org

**原文链接**: [https://twitter.com/sgondala2/status/2115832070274723875](https://twitter.com/sgondala2/status/2115832070274723875)

生成摘要时出错

---

## 59. Infinite Mac: BeOS

**原文标题**: Infinite Mac: BeOS

**原文链接**: [https://blog.persistent.info/2026/10/infinite-mac-beos.html](https://blog.persistent.info/2026/10/infinite-mac-beos.html)

生成摘要时出错

---

## 60. Wasmer (YC S19) Is Hiring OS/Hypervisor Experts in Europe

**原文标题**: Wasmer (YC S19) Is Hiring OS/Hypervisor Experts in Europe

**原文链接**: [https://www.workatastartup.com/jobs/98722](https://www.workatastartup.com/jobs/98722)

生成摘要时出错

---

## 61. We're releasing the weights of Mistral Large 4

**原文标题**: We're releasing the weights of Mistral Large 4

**原文链接**: [https://mistral.ai/news/mistral-large-4-oss/](https://mistral.ai/news/mistral-large-4-oss/)

生成摘要时出错

---

## 62. 2.5 hrs of makeup: Japan teen struggles with social media beauty standards

**原文标题**: 2.5 hrs of makeup: Japan teen struggles with social media beauty standards

**原文链接**: [https://mainichi.jp/english/articles/20261029/p2a/00m/0na/004000c](https://mainichi.jp/english/articles/20261029/p2a/00m/0na/004000c)

生成摘要时出错

---

## 63. Amazon sends chills through its workforce with mixed message memo about AI use

**原文标题**: Amazon sends chills through its workforce with mixed message memo about AI use

**原文链接**: [https://www.theregister.com/ai-and-ml/2026/10/31/amazon-sends-chills-through-its-workforce-with-mixed-message-memo-about-ai-use-corey-quinn/5306804](https://www.theregister.com/ai-and-ml/2026/10/31/amazon-sends-chills-through-its-workforce-with-mixed-message-memo-about-ai-use-corey-quinn/5306804)

生成摘要时出错

---

## 64. Northflank Breached

**原文标题**: Northflank Breached

**原文链接**: [https://status.northflank.com](https://status.northflank.com)

生成摘要时出错

---

## 65. Through Captain Jean-Luc Picard, Patrick Stewart taught us the measure of a man

**原文标题**: Through Captain Jean-Luc Picard, Patrick Stewart taught us the measure of a man

**原文链接**: [https://www.bostonglobe.com/2026/10/29/metro/patrick-stewart-picard-star-trek-the-next-generation/](https://www.bostonglobe.com/2026/10/29/metro/patrick-stewart-picard-star-trek-the-next-generation/)

生成摘要时出错

---

## 66. Breaking the open web won't stop the bad bots

**原文标题**: Breaking the open web won't stop the bad bots

**原文链接**: [https://www.techpolicy.press/breaking-the-open-web-wont-stop-the-bad-bots/](https://www.techpolicy.press/breaking-the-open-web-wont-stop-the-bad-bots/)

生成摘要时出错

---

## 67. We ran AI agent swarms in Minecraft and Mindustry

**原文标题**: We ran AI agent swarms in Minecraft and Mindustry

**原文链接**: [https://labs.ycombinator.com/projects/games/index.html](https://labs.ycombinator.com/projects/games/index.html)

生成摘要时出错

---

## 68. How do you take a picture of a black hole?

**原文标题**: How do you take a picture of a black hole?

**原文链接**: [https://www.quantamagazine.org/how-do-you-take-a-picture-of-a-black-hole-20261029/](https://www.quantamagazine.org/how-do-you-take-a-picture-of-a-black-hole-20261029/)

生成摘要时出错

---

## 69. Tree-mounted machines connect to web app to let users knock on wood remotely

**原文标题**: Tree-mounted machines connect to web app to let users knock on wood remotely

**原文链接**: [https://www.designboom.com/technology/tree-mounted-machines-web-app-users-knock-on-wood-remotely/](https://www.designboom.com/technology/tree-mounted-machines-web-app-users-knock-on-wood-remotely/)

生成摘要时出错

---

## 70. Cisco gives engineer unlimited AI tokens to rewrite legacy code

**原文标题**: Cisco gives engineer unlimited AI tokens to rewrite legacy code

**原文链接**: [https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/](https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/)

生成摘要时出错

---

## 71. Double Buffering with Cloudflare Queues

**原文标题**: Double Buffering with Cloudflare Queues

**原文链接**: [https://bellone.com/technical/double-buffering-with-cloudflare-queues](https://bellone.com/technical/double-buffering-with-cloudflare-queues)

生成摘要时出错

---

## 72. Why a program doesn't work when run from a batch file, but works when clicked

**原文标题**: Why a program doesn't work when run from a batch file, but works when clicked

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20261026-00/?p=112797/](https://devblogs.microsoft.com/oldnewthing/20261026-00/?p=112797/)

生成摘要时出错

---

## 73. Florilegium: Procedural Flowers in LaTeX

**原文标题**: Florilegium: Procedural Flowers in LaTeX

**原文链接**: [https://github.com/kevinraymond/florilegium](https://github.com/kevinraymond/florilegium)

生成摘要时出错

---

## 74. Gilgamesh by Simon Armitage review – an ancient epic is brilliantly translated

**原文标题**: Gilgamesh by Simon Armitage review – an ancient epic is brilliantly translated

**原文链接**: [https://www.theguardian.com/books/2026/oct/20/gilgamesh-by-simon-armitage-review-an-ancient-epic-is-brilliantly-translated-for-our-times](https://www.theguardian.com/books/2026/oct/20/gilgamesh-by-simon-armitage-review-an-ancient-epic-is-brilliantly-translated-for-our-times)

生成摘要时出错

---

## 75. Turning a solar power system into its own backup

**原文标题**: Turning a solar power system into its own backup

**原文链接**: [https://arstechnica.com/science/2026/10/turning-a-solar-power-system-into-its-own-backup/](https://arstechnica.com/science/2026/10/turning-a-solar-power-system-into-its-own-backup/)

生成摘要时出错

---

## 76. AI isn't replacing SREs, it's deskilling them

**原文标题**: AI isn't replacing SREs, it's deskilling them

**原文链接**: [https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling](https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling)

生成摘要时出错

---

## 77. I'm so bad at billiards that I ended up in the hyperbolic plane [video]

**原文标题**: I'm so bad at billiards that I ended up in the hyperbolic plane [video]

**原文链接**: [https://www.youtube.com/watch?v=kL9BTbIGxLg](https://www.youtube.com/watch?v=kL9BTbIGxLg)

生成摘要时出错

---

## 78. The Great American Rascal: Tom Sawyer at 150

**原文标题**: The Great American Rascal: Tom Sawyer at 150

**原文链接**: [https://claremontreviewofbooks.com/the-great-american-rascal/](https://claremontreviewofbooks.com/the-great-american-rascal/)

生成摘要时出错

---

## 79. Shiny Object Syndrome

**原文标题**: Shiny Object Syndrome

**原文链接**: [https://en.wikipedia.org/wiki/Shiny_object_syndrome](https://en.wikipedia.org/wiki/Shiny_object_syndrome)

生成摘要时出错

---

## 80. Brief History of PDP Computers

**原文标题**: Brief History of PDP Computers

**原文链接**: [https://entropicthoughts.com/history-of-pdp-computers](https://entropicthoughts.com/history-of-pdp-computers)

生成摘要时出错

---

## 81. Show HN: A working Nintendo in ~1GB of Qwen weights

**原文标题**: Show HN: A working Nintendo in ~1GB of Qwen weights

**原文链接**: [https://github.com/dbreunig/nesformer](https://github.com/dbreunig/nesformer)

生成摘要时出错

---

## 82. Astroterm: A Planetarium for Your Terminal

**原文标题**: Astroterm: A Planetarium for Your Terminal

**原文链接**: [https://github.com/da-luce/astroterm](https://github.com/da-luce/astroterm)

生成摘要时出错

---

## 83. Azure's Weakest Link – Five Full Cross-Tenant Compromises

**原文标题**: Azure's Weakest Link – Five Full Cross-Tenant Compromises

**原文链接**: [https://www.binarysecurity.no/posts/2026/10/one-root-case](https://www.binarysecurity.no/posts/2026/10/one-root-case)

生成摘要时出错

---

## 84. Ex-Meta Researcher Torrented Pirated Books, Deleted It 'Due to Litigation'

**原文标题**: Ex-Meta Researcher Torrented Pirated Books, Deleted It 'Due to Litigation'

**原文链接**: [https://torrentfreak.com/ex-meta-researcher-torrented-pirated-books-dataset-deleted-it-due-to-all-this-litigation/](https://torrentfreak.com/ex-meta-researcher-torrented-pirated-books-dataset-deleted-it-due-to-all-this-litigation/)

生成摘要时出错

---

## 85. The federated code forge

**原文标题**: The federated code forge

**原文链接**: [https://tangled.org/blog/forge/](https://tangled.org/blog/forge/)

生成摘要时出错

---

## 86. Anthropic orders AI tool Claude to stop remaking video games

**原文标题**: Anthropic orders AI tool Claude to stop remaking video games

**原文链接**: [https://www.gamedeveloper.com/programming/anthropic-appears-to-have-ordered-ai-tool-claude-to-stop-remaking-video-games](https://www.gamedeveloper.com/programming/anthropic-appears-to-have-ordered-ai-tool-claude-to-stop-remaking-video-games)

生成摘要时出错

---

## 87. Sneezecount (2018)

**原文标题**: Sneezecount (2018)

**原文链接**: [https://sneezecount.joyfeed.com](https://sneezecount.joyfeed.com)

生成摘要时出错

---

## 88. How long do you need to hold down the power button to turn off a PC?

**原文标题**: How long do you need to hold down the power button to turn off a PC?

**原文链接**: [https://www.osnews.com/story/146273/how-long-do-you-need-to-hold-down-the-power-button-to-turn-off-a-pc/](https://www.osnews.com/story/146273/how-long-do-you-need-to-hold-down-the-power-button-to-turn-off-a-pc/)

生成摘要时出错

---

## 89. NASA's Voyager 1 mysteriously lost touch with Earth

**原文标题**: NASA's Voyager 1 mysteriously lost touch with Earth

**原文链接**: [https://mashable.com/science/nasa-voyager-1-communication-outage](https://mashable.com/science/nasa-voyager-1-communication-outage)

生成摘要时出错

---

## 90. Cuis: The Modern Smalltalk-80

**原文标题**: Cuis: The Modern Smalltalk-80

**原文链接**: [https://cuis.st/](https://cuis.st/)

生成摘要时出错

---

## 91. Tracks along the longest drive on another world

**原文标题**: Tracks along the longest drive on another world

**原文链接**: [https://science.nasa.gov/blog/tracks-along-the-longest-drive-on-another-world/](https://science.nasa.gov/blog/tracks-along-the-longest-drive-on-another-world/)

生成摘要时出错

---

## 92. Finding Panics with Call Graph Analyzer

**原文标题**: Finding Panics with Call Graph Analyzer

**原文链接**: [https://tweedegolf.nl/en/blog/242/finding-panics-with-call-graph-analyzer/](https://tweedegolf.nl/en/blog/242/finding-panics-with-call-graph-analyzer/)

生成摘要时出错

---

## 93. Show HN: Sketch Stadium – watch your agent play Pictionary

**原文标题**: Show HN: Sketch Stadium – watch your agent play Pictionary

**原文链接**: [https://sketch.wakeshift.ai/games/q5ucru](https://sketch.wakeshift.ai/games/q5ucru)

生成摘要时出错

---

## 94. Why is this fingerprinting script creating bioweapons?

**原文标题**: Why is this fingerprinting script creating bioweapons?

**原文链接**: [https://nullpt.rs/fingerprinting-bioweapons](https://nullpt.rs/fingerprinting-bioweapons)

生成摘要时出错

---

## 95. NetBSD adds a new text editor called atto

**原文标题**: NetBSD adds a new text editor called atto

**原文链接**: [https://mastodon.sdf.org/@netbsd/117518160563539748](https://mastodon.sdf.org/@netbsd/117518160563539748)

生成摘要时出错

---

## 96. Some Thing is Happening A note from the AI companies

**原文标题**: Some Thing is Happening A note from the AI companies

**原文链接**: [https://alanbellows.com/some-thing-is-happening/](https://alanbellows.com/some-thing-is-happening/)

生成摘要时出错

---

## 97. Compile-Time Dependent Types

**原文标题**: Compile-Time Dependent Types

**原文链接**: [https://thenumb.at/Syl-Intro/](https://thenumb.at/Syl-Intro/)

生成摘要时出错

---

## 98. Show HN: I rebuilt Kubernetes for ESP32 microcontrollers

**原文标题**: Show HN: I rebuilt Kubernetes for ESP32 microcontrollers

**原文链接**: [https://github.com/arterialist/kube32](https://github.com/arterialist/kube32)

生成摘要时出错

---

## 99. Is the Music Business Collapsing?

**原文标题**: Is the Music Business Collapsing?

**原文链接**: [https://www.honest-broker.com/p/is-the-music-business-collapsing](https://www.honest-broker.com/p/is-the-music-business-collapsing)

生成摘要时出错

---

## 100. Leak Exposes 41,000 Homeland Security Workers–Including Undercover ICE Agents

**原文标题**: Leak Exposes 41,000 Homeland Security Workers–Including Undercover ICE Agents

**原文链接**: [https://www.wired.com/story/massive-leak-exposes-41000-homeland-security-workers-including-undercover-ice-agents/](https://www.wired.com/story/massive-leak-exposes-41000-homeland-security-workers-including-undercover-ice-agents/)

生成摘要时出错

---

