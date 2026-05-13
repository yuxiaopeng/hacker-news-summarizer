# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-13.md)

*最后自动更新时间: 2026-05-13 19:22:16*
## 1. 设置免费的 *.city.state.us 地区域名

**原文标题**: Setting up a free *.city.state.us locality domain

**原文链接**: [https://fredchan.org/blog/locality-domains-guide/](https://fredchan.org/blog/locality-domains-guide/)

本指南介绍了美国公民、居民及组织如何注册免费的地区域名（例如 `somename.city.state.us`）。这些域名建立于1992年，由受托注册商或中央管理机构 NeuStar 负责管理。

注册过程包含以下五个关键步骤：

1.  **确定地区**：用户必须找到其所在城市或州的受托管理员。虽然官方提供了一份名单，但因其内容陈旧，可能需要自行调查以获取当前的联系邮箱。如果某个地区处于“未受托（undelegated）”状态，目前注册仅限于政府机构。
2.  **准备域名服务器**：在申请之前，您必须准备好域名服务器。本指南建议使用 Amazon Lightsail，因为它能为非顶级域名提供免费的 DNS 区域。
3.  **填写模板**：申请人需填写“Interim .US Domain Template v2.0”表格。该表单要求提供联系信息、域名用途描述以及域名服务器的主机名/IP 地址。申请人还必须指定其“US Nexus”类别以证明符合注册资格。
4.  **提交申请**：将填写好的表单通过电子邮件发送给该地区的注册商。由于申请采用人工处理，审批可能需要数天或数周时间。
5.  **配置 DNS**：在申请获批后，用户需在 Lightsail 中将 DNS 记录指向所选的网站托管商（如 GitHub Pages）。

地区域名具有显著的隐私优势：WHOIS 查询通常返回的是注册商的信息，而非注册人的个人地址。虽然注册过程涉及人工操作且需要一定的技术配置，但它为用户提供了一个免费、独特且具有地理相关性的美国网络标识。

---

## 2. 开源反抗：在上班时间延续开源生命

**原文标题**: Open Source Resistance: keep OSS alive on company time

**原文链接**: [https://ossresistance.com/](https://ossresistance.com/)

这篇文章（属于“开源反抗”运动的一部分）主张将开源软件（OSS）的积极维护直接纳入开发者的付费工作时间。其核心理念是，既然企业高度依赖开源基础设施，那么维持其运行所需的劳动就应被视为一项标准的业务职责，而非业余爱好。

文章强调的核心观点是“**付诸行动**”，具体包括：

*   **直接贡献：** 积极审查拉取请求（PR），并为已开源的项目提交漏洞修复。
*   **依赖管理：** 定期更新依赖项，以确保软件的安全性和功能性。
*   **维护常态化：** 在雇主利益与开源项目健康状况的交汇点，将这些任务整合进日常工作流程。

通过在“公司时间”履行这些职责，开发者确保了雇主所依赖工具的持久性和可靠性，从而有效地促使企业资源去支持那些为其产品提供动力的底层生态系统。

---

## 3. Linux 游戏速度更快，因为 Windows API 正逐渐成为 Linux 内核特性

**原文标题**: Linux gaming is faster because Windows APIs are becoming Linux kernel features

**原文链接**: [https://www.xda-developers.com/linux-gaming-is-getting-faster-because-windows-apis-are-becoming-linux-kernel-features/](https://www.xda-developers.com/linux-gaming-is-getting-faster-because-windows-apis-are-becoming-linux-kernel-features/)

截至 2026 年初，在 Steam Deck 的普及和 Windows 10 停止支持的推动下，Linux 游戏在 Steam 用户中的份额已达到 5% 这一里程碑。这一增长的关键因素在于 Linux 处理 Windows 游戏方式的根本转变：Linux 内核开始直接集成 Windows 特有的功能，而不再仅仅依赖像 Wine 这样的翻译层。

最近最显著的进展是 NTSYNC，这是一个在内核层面原生实现 Windows 同步机制的驱动程序。在现代游戏中，CPU 必须在多个核心之间协调大量的并行任务，如物理、音频和 AI。此前，翻译层使用名为“esync”和“fsync”的权宜之计来模拟 Windows 的行为。NTSYNC 通过允许 Linux 内核原生响应这些 API 调用，取代了这些临时方案。

虽然 NTSYNC 相比基础 Wine 实现了性能飞跃，但其相对于 Valve Proton 中现有的“fsync”所带来的提升则较为细微。然而，它的真正价值在于稳定性和精确性。通过精确匹配 Windows 的行为，NTSYNC 消除了基准测试通常会忽略的“极端情况”下的漏洞，例如画面卡顿、掉帧和死锁。

这一由 Valve 和 CodeWeavers 牵头的转型标志着该操作系统进入了一个新纪元。Linux 内核不再仅仅是模拟 Windows，而是在底层架构上不断演进以满足游戏需求。随着 NTSYNC 成为 Ubuntu 和 Fedora 等流行发行版的标准配置，Linux 正进一步巩固其作为游戏玩家眼中高性能 Windows 替代方案的地位。

---

## 4. Launch HN：Ardent (YC P26) — 秒级构建 Postgres 沙盒，无需迁移

**原文标题**: Launch HN: Ardent (YC P26) – Postgres sandboxes in seconds with zero migration

**原文链接**: [https://www.tryardent.com/](https://www.tryardent.com/)

**Ardent (YC P26)** 是一个数据库克隆平台，旨在让编码智能体（coding agents）和开发人员能够在零风险的情况下，使用生产级数据测试代码。该服务提供隔离的 Postgres 沙箱，无论数据库规模大小，均可在 6 秒内创建完成。

**核心功能与特性：**
*   **快速克隆：** Ardent 可在 6 秒内创建生产数据库的 1:1 副本（包括 TB 级规模），其速度显著快于需要数小时或数天的传统副本技术。
*   **隔离与安全：** 克隆在计算和存储层面均实现隔离，确保“零波及范围”，测试过程绝不会影响生产环境的性能或稳定性。
*   **存储与成本效率：** 采用类 Git 的分支模型，Ardent 不会重复占用存储空间；用户仅需为克隆中产生的数据变更付费。计算资源在闲置时会自动缩减至零，以最大限度降低成本。
*   **无缝集成：** 该平台支持 AWS RDS、Supabase 和 PlanetScale 等主流服务商，且无需更改任何配置。

**主要应用场景：**
该平台专为“AI 原生”数据团队打造。它允许编码智能体在真实数据上验证数据库迁移、执行数据清理并测试数据回填，从而告别不准确的种子文件或繁琐的手动环境管理。

来自 Chevron 和 Dataexpert.io 等公司的行业领袖将 Ardent 视为数据工程领域的根本性变革，将其对数据库管理的影响比作 Git 对源码控制的革命。通过消除生产与测试环境之间的“环境漂移（drift）”，Ardent 助力团队提升发布速度，并杜绝因数据库代码故障导致的停机风险。

---

## 5. Xs of Y – roguelike that names itself every run. Written in 4kLoC

**原文标题**: Xs of Y – roguelike that names itself every run. Written in 4kLoC

**原文链接**: [https://github.com/nooga/xsofy](https://github.com/nooga/xsofy)

**Xs of Y** 是一款实验性 Roguelike 游戏，其特色在于程序化生成的特性和独特的基于 Lisp 的魔法系统。在每一局游戏中，系统都会生成一个新的标题（例如 *Gazebos of Mounting Dread*）、一项新任务和一套全新的符文映射。魔法系统允许玩家利用 S-表达式获取地牢“现实引擎”的“根权限”；由于该语言随每次启动而变化，玩家必须通过实验来破解其逻辑。

从技术角度看，该游戏由约 6,900 行 **let-go** 编写而成，这是一种运行在 Go 字节码虚拟机上的 Clojure 方言。它具有持久化数据结构，无任何依赖项，启动时间仅需 6 毫秒。它支持原生运行，也可通过 WASM 在浏览器中游玩。

游戏玩法受到 Roguelike 游戏 *Brogue* 的启发，具有反转的力量曲线：游戏初期是与巨魔和史莱姆等传统怪物的殊死生存搏斗，而随着玩家掌握魔法系统，游戏会演变为“应用神学”。环境交互性极高，玩家可以纵火、将敌人推入岩浆，或是意外掉入“富有教育意义”的深渊。尽管游戏目前已可游玩，但开发者指出这仍是一部未完成的作品，可能会发生“计划外的爆炸”。

---

## 6. S-100 虚拟工作台

**原文标题**: S-100 Virtual Workbench

**原文链接**: [https://grantmestrength.github.io/S100/](https://grantmestrength.github.io/S100/)

根据所提供的标题，“S-100 虚拟工作台”（S-100 Virtual Workbench）是指一种专门的软件环境，旨在仿真和模拟经典的 S-100 总线计算机系统。该系统曾是 20 世纪 70 和 80 年代早期个人电脑（如 Altair 8800 和 IMSAI 8080）的行业标准。

**关键信息与要点：**

*   **硬件仿真：** 该工作台提供了一个虚拟平台，用于复制物理 S-100 组件的功能，包括 CPU 板（如 Intel 8080 或 Zilog Z80）、内存模块和 I/O 接口。
*   **旧版软件兼容性：** 它允许用户在现代硬件上运行历史操作系统（最著名的是 CP/M）和旧版应用程序，而无需使用日益稀有且脆弱的原始物理机器。
*   **开发与测试：** 该环境为爱好者和开发者提供了一个“工作台”，用于编写、调试和测试汇编代码或硬件配置。它通常包含实时监控内存、寄存器和端口活动的工具。
*   **可访问性与保护：** 通过将 S-100 体验数字化，该工具保护了计算历史，并让那些可能没有空间或预算购买复古硬件的研究人员及复古计算爱好者能够接触到这些资源。
*   **教育用途：** 它可作为了解基础计算机体系结构、总线结构以及早期微型计算底层逻辑的教学工具。

总之，S-100 虚拟工作台架起了上世纪中叶计算逻辑与现代便利性之间的桥梁，为探索早期个人计算历史提供了一个功能完善且低风险的环境。

---

## 7. 软件的 Emacs 化

**原文标题**: The Emacsification of Software

**原文链接**: [https://sockpuppet.org/blog/2026/05/12/emacsification/](https://sockpuppet.org/blog/2026/05/12/emacsification/)

In "The Emacsification of Software," the author argues that AI agents are ushering in a new era of "personal software" by making native UI development accessible to everyone. 

The author’s thesis begins with a common frustration: the lack of a high-quality, lightweight Markdown viewer. Terminal-based viewers are visually fatiguing, while graphical editors interfere with established workspaces. Using Claude, the author "extruded" a custom native macOS app (MDV.app) in just 30 minutes of active work. Despite having little experience in SwiftUI, the author created a tool superior to those available on the App Store, featuring SQLite indexing, text search, and refined typography.

This process illustrates the "Emacsification" of software. Just as Emacs enthusiasts write bespoke Lisp code to scratch personal itches, AI now allows any developer to build niche, native applications tailored to their exact needs. This shift undermines the necessity of Electron—which bundles entire browsers to render simple interfaces—and moves the focus away from "building" products toward "configuring" a platform.

The core takeaways are:
*   **Native UI is now accessible:** AI agents like Claude have lowered the barrier to entry for complex frameworks like SwiftUI, making native performance and aesthetics easier to achieve than web-based alternatives.
*   **Software is becoming personal:** Most AI-generated tools will be "personal software," useful primarily to their creators.
*   **Prompts over Code:** In this new paradigm, the specific source code matters less than the prompts and the realization that "you can just make that." 

Ultimately, the author suggests that the future of software development lies in replacing clunky, general-purpose tools with elegant, bespoke native applications created through AI-assisted configuration.

---

## 8. Nginx.org/En/更新日志

**原文标题**: Nginx.org/En/Changes

**原文链接**: [https://nginx.org/en/CHANGES](https://nginx.org/en/CHANGES)

生成摘要时出错

---

## 9. The US is winning the AI race where it matters most: commercialization

**原文标题**: The US is winning the AI race where it matters most: commercialization

**原文链接**: [https://avkcode.github.io/blog/us-winning-ai-race.html](https://avkcode.github.io/blog/us-winning-ai-race.html)

生成摘要时出错

---

## 10. 在 Python 3.14 和 3.15 中回退增量式垃圾回收

**原文标题**: Reverting the incremental GC in Python 3.14 and 3.15

**原文链接**: [https://discuss.python.org/t/reverting-the-incremental-gc-in-python-3-14-and-3-15/107014](https://discuss.python.org/t/reverting-the-incremental-gc-in-python-3-14-and-3-15/107014)

The Python core team and Steering Council have decided to revert the incremental garbage collector (GC) in Python 3.14 and 3.15, returning to the generational GC used in version 3.13. 

**Reasons for the Revert**
The decision was prompted by reports of significant memory pressure in production environments following the release of Python 3.14. Although reverting a feature in a stable patch release (3.14) is unusual, the team justified the move because the incremental GC did not undergo a formal PEP process and had been pulled from the 3.13 release at the last minute. By returning to the "known quantity" of the 3.13 GC, the team aims to restore stability.

**Future Implementation**
The incremental GC may be reintroduced in Python 3.16, but it will be required to go through the standard PEP process to ensure more thorough evaluation and testing.

**Updated Release Schedules**
*   **Python 3.15:** Currently in alpha, the first beta is scheduled for May 5, 2026. If the revert is completed quickly, an additional "alpha 9" release may be issued within the next week.
*   **Python 3.14:** The 3.14.5 patch release, originally planned for June 9, 2026, will be moved up and released as soon as the revert is ready.

The release managers will update the specific PEPs and community topics once the new release dates are finalized.

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 2 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 3 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 4 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 5 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 6 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 7 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 8 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 9 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 10 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 11 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 12 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 13 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 14 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 15 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 16 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 17 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 18 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 19 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 20 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 21 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 22 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 23 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 24 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 25 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 26 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 27 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 28 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 29 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 30 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 31 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 32 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 33 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 34 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 35 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 36 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 37 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 38 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 39 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 40 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 41 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 42 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 43 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 44 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 45 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 46 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 47 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 48 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 49 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 50 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 51 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 52 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 53 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 54 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 55 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 56 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 57 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 58 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 59 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 60 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 61 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 62 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 63 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 64 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 65 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 66 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 67 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 68 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 69 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 70 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 71 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 72 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 73 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 74 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 75 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 76 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 77 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 78 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 79 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 80 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 81 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 82 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 83 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 84 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 85 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 86 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 87 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 88 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 89 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 90 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 91 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 92 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 93 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 94 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 95 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 96 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 97 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 98 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 99 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 100 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 101 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 102 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 103 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 104 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 105 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 106 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 107 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 108 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 109 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 110 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 111 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 112 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 113 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 114 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 115 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 116 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 117 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 118 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 119 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 120 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 121 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 122 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 123 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 124 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 125 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 126 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 127 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 128 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 129 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 130 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 131 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 132 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 133 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 134 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 135 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 136 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 137 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 138 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 139 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 140 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 141 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 142 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 143 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 144 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 145 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 146 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 147 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 148 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 149 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 150 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 151 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 152 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 153 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 154 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 155 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 156 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 157 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 158 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 159 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 160 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 161 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 162 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 163 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 164 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 165 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 166 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 167 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 168 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 169 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 170 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 171 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 172 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 173 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 174 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 175 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 176 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 177 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 178 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 179 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 180 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 181 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 182 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 183 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 184 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 185 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 186 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 187 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 188 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 189 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 190 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 191 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 192 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 193 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 194 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 195 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 196 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 197 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 198 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 199 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 200 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 201 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 202 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 203 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 204 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 205 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 206 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 207 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 208 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 209 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 210 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 211 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 212 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 213 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 214 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 215 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 216 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 217 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 218 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 219 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 220 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 221 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 222 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 223 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 224 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 225 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 226 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 227 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 228 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 229 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 230 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 231 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 232 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 233 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 234 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 235 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 236 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 237 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 238 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 239 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 240 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 241 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 242 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 243 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 244 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 245 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 246 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 247 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 248 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 249 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 250 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 251 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 252 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 253 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 254 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 255 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 256 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 257 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 258 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 259 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 260 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 261 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 262 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 263 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 264 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 265 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 266 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 267 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 268 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 269 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 270 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 271 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 272 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 273 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 274 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 275 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 276 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 277 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 278 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 279 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 280 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 281 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 282 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 283 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 284 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 285 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 286 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 287 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 288 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 289 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 290 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 291 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 292 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 293 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 294 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 295 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 296 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 297 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 298 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 299 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 300 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 301 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 302 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 303 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 304 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 305 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 306 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 307 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 308 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 309 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 310 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 311 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 312 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 313 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 314 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 315 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 316 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 317 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 318 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 319 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 320 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 321 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 322 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 323 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 324 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 325 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 326 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 327 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 328 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 329 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 330 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 331 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 332 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 333 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 334 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 335 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 336 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 337 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 338 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 339 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 340 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 341 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 342 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 343 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 344 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 345 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 346 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 347 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 348 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 349 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 350 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 351 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 352 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 353 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 354 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 355 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 356 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 357 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 358 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 359 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 360 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 361 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 362 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 363 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 364 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 365 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 366 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 367 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 368 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 369 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 370 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 371 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 372 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 373 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 374 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 375 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 376 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 377 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 378 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 379 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 380 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 381 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 382 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 383 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 384 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 385 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 386 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 387 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 388 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 389 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 390 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 391 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 392 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 393 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 394 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 395 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 396 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 397 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 398 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 399 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 400 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 401 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 402 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 403 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 404 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 405 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 406 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 407 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 408 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 409 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 410 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 411 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 412 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 413 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 414 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 415 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 416 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 417 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 418 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 419 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
