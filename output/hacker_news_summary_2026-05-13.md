# Hacker News 热门文章摘要 (2026-05-13)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. A History of IDEs at Google

**原文标题**: A History of IDEs at Google

**原文链接**: [https://laurent.le-brun.eu/blog/a-history-of-ides-at-google](https://laurent.le-brun.eu/blog/a-history-of-ides-at-google)

生成摘要时出错

---

## 12. Leaving GitHub for Forgejo

**原文标题**: Leaving GitHub for Forgejo

**原文链接**: [https://jorijn.com/en/blog/leaving-github-for-forgejo/](https://jorijn.com/en/blog/leaving-github-for-forgejo/)

生成摘要时出错

---

## 13. An idiot's guide to lead optimisation for proteins

**原文标题**: An idiot's guide to lead optimisation for proteins

**原文链接**: [https://magnusross.github.io/posts/protein-lead-optimisation-1/](https://magnusross.github.io/posts/protein-lead-optimisation-1/)

生成摘要时出错

---

## 14. New stainless steel can survive conditions for hydrogen production in seawater

**原文标题**: New stainless steel can survive conditions for hydrogen production in seawater

**原文链接**: [https://www.sciencedaily.com/releases/2026/05/260510030950.htm](https://www.sciencedaily.com/releases/2026/05/260510030950.htm)

Researchers at the University of Hong Kong (HKU), led by Professor Mingxin Huang, have developed a revolutionary "super steel" (SS-H2) designed to withstand the harsh corrosive environments of green hydrogen production from seawater.

Traditional stainless steel typically fails during water electrolysis because its protective chromium-oxide layer breaks down at high electrical potentials (~1000 mV), well below the ~1600 mV required for water oxidation. To overcome this, the HKU team utilized a "sequential dual-passivation" strategy. In addition to the standard chromium layer, SS-H2 forms a second manganese-based protective shield at higher voltages, allowing it to resist corrosion up to 1700 mV. This discovery is particularly notable as manganese was previously believed to impair corrosion resistance in steel.

The primary impact of SS-H2 is economic. Currently, seawater electrolyzers rely on expensive titanium structural components often coated with precious metals like gold or platinum. The HKU team estimates that replacing these costly materials with SS-H2 could reduce structural material costs by approximately 40 times, significantly lowering the financial barrier for large-scale green hydrogen production.

The project has already transitioned toward industrial application, with tons of SS-H2 wire produced in collaboration with a factory in Mainland China. While the team continues to work on manufacturing specific components like meshes and foams, this breakthrough establishes a new paradigm for alloy development. By creating a material that is both durable and affordable, the HKU team has provided a critical piece of the puzzle for making sustainable seawater electrolysis commercially viable.

---

## 15. Heritability of human life span is ~50% when heritability is redefined

**原文标题**: Heritability of human life span is ~50% when heritability is redefined

**原文链接**: [https://dynomight.net/lifespan/](https://dynomight.net/lifespan/)

生成摘要时出错

---

## 16. I moved my digital stack to Europe

**原文标题**: I moved my digital stack to Europe

**原文链接**: [https://monokai.com/articles/how-i-moved-my-digital-stack-to-europe/](https://monokai.com/articles/how-i-moved-my-digital-stack-to-europe/)

生成摘要时出错

---

## 17. Preserving Fisher-Price Pixter

**原文标题**: Preserving Fisher-Price Pixter

**原文链接**: [https://dmitry.gr/?r=05.Projects&proj=37.%20Pixter](https://dmitry.gr/?r=05.Projects&proj=37.%20Pixter)

生成摘要时出错

---

## 18. A sentimental tour of late 1990s and early 2000s hacking tools

**原文标题**: A sentimental tour of late 1990s and early 2000s hacking tools

**原文链接**: [https://andreafortuna.org/2026/05/13/amarcord/](https://andreafortuna.org/2026/05/13/amarcord/)

生成摘要时出错

---

## 19. Twin brothers wipe 96 government databases minutes after being fired

**原文标题**: Twin brothers wipe 96 government databases minutes after being fired

**原文链接**: [https://arstechnica.com/tech-policy/2026/05/drop-database-what-not-to-do-after-losing-an-it-job/](https://arstechnica.com/tech-policy/2026/05/drop-database-what-not-to-do-after-losing-an-it-job/)

生成摘要时出错

---

## 20. Substrate (YC S24) Is Hiring a Technical Success Manager

**原文标题**: Substrate (YC S24) Is Hiring a Technical Success Manager

**原文链接**: [https://www.ycombinator.com/companies/substrate/jobs/T2fMBhD-technical-success-manager](https://www.ycombinator.com/companies/substrate/jobs/T2fMBhD-technical-success-manager)

生成摘要时出错

---

## 21. Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model

**原文标题**: Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model

**原文链接**: [https://github.com/cactus-compute/needle](https://github.com/cactus-compute/needle)

生成摘要时出错

---

## 22. Nailing jelly to a wall: is it possible? (2005)

**原文标题**: Nailing jelly to a wall: is it possible? (2005)

**原文链接**: [https://greem.co.uk/otherbits/jelly.html](https://greem.co.uk/otherbits/jelly.html)

生成摘要时出错

---

## 23. Altman forced to confront claims at OpenAI trial that he's a prolific liar

**原文标题**: Altman forced to confront claims at OpenAI trial that he's a prolific liar

**原文链接**: [https://arstechnica.com/tech-policy/2026/05/altman-forced-to-confront-claims-at-openai-trial-that-hes-a-prolific-liar/](https://arstechnica.com/tech-policy/2026/05/altman-forced-to-confront-claims-at-openai-trial-that-hes-a-prolific-liar/)

生成摘要时出错

---

## 24. Deterministic Fully-Static Whole-Binary Translation Without Heuristics

**原文标题**: Deterministic Fully-Static Whole-Binary Translation Without Heuristics

**原文链接**: [https://arxiv.org/abs/2605.08419](https://arxiv.org/abs/2605.08419)

生成摘要时出错

---

## 25. Haiku

**原文标题**: Haiku

**原文链接**: [https://www.haiku-os.org](https://www.haiku-os.org)

生成摘要时出错

---

## 26. Web Server on a Nintendo Wii

**原文标题**: Web Server on a Nintendo Wii

**原文链接**: [http://wii.sjmulder.nl/](http://wii.sjmulder.nl/)

生成摘要时出错

---

## 27. 50K Tahoe residents need power as utility eyes redirecting lines to data centers

**原文标题**: 50K Tahoe residents need power as utility eyes redirecting lines to data centers

**原文链接**: [https://fortune.com/2026/05/12/lake-tahoe-data-center-49000-residents-power-source/](https://fortune.com/2026/05/12/lake-tahoe-data-center-49000-residents-power-source/)

生成摘要时出错

---

## 28. Kraftwerk's radical 1976 track

**原文标题**: Kraftwerk's radical 1976 track

**原文链接**: [https://www.bbc.com/culture/article/20260511-kraftwerks-radical-1976-track-radioactivity-became-an-anti-nuclear-anthem](https://www.bbc.com/culture/article/20260511-kraftwerks-radical-1976-track-radioactivity-became-an-anti-nuclear-anthem)

生成摘要时出错

---

## 29. Using OR-Tools CP-SAT for Scheduling Problems

**原文标题**: Using OR-Tools CP-SAT for Scheduling Problems

**原文链接**: [https://atalaykutlay.com/or-tools-cp-sat-for-scheduling-problems.html](https://atalaykutlay.com/or-tools-cp-sat-for-scheduling-problems.html)

生成摘要时出错

---

## 30. Cost of enum-to-string: C++26 reflection vs. the old ways

**原文标题**: Cost of enum-to-string: C++26 reflection vs. the old ways

**原文链接**: [https://vittorioromeo.com/index/blog/refl_enum_to_string.html](https://vittorioromeo.com/index/blog/refl_enum_to_string.html)

生成摘要时出错

---

## 31. Using OR-Tools CP-SAT for Scheduling Problems

**原文标题**: Using OR-Tools CP-SAT for Scheduling Problems

**原文链接**: [https://atalaykutlay.com/or-tools-cp-sat-for-scheduling-problems.html](https://atalaykutlay.com/or-tools-cp-sat-for-scheduling-problems.html)

生成摘要时出错

---

## 32. Cost of enum-to-string: C++26 reflection vs. the old ways

**原文标题**: Cost of enum-to-string: C++26 reflection vs. the old ways

**原文链接**: [https://vittorioromeo.com/index/blog/refl_enum_to_string.html](https://vittorioromeo.com/index/blog/refl_enum_to_string.html)

生成摘要时出错

---

## 33. Kickstarter is forced to ban adult content by payment processors

**原文标题**: Kickstarter is forced to ban adult content by payment processors

**原文链接**: [https://kotaku.com/kickstarter-is-the-latest-platform-seemingly-forced-to-ban-adult-content-by-payment-processors-2000695648](https://kotaku.com/kickstarter-is-the-latest-platform-seemingly-forced-to-ban-adult-content-by-payment-processors-2000695648)

生成摘要时出错

---

## 34. Data centers cutting power to homes, driving homeowners to solar and batteries

**原文标题**: Data centers cutting power to homes, driving homeowners to solar and batteries

**原文链接**: [https://electrek.co/2026/05/13/data-centers-grid-strain-driving-residential-solar-battery-demand/](https://electrek.co/2026/05/13/data-centers-grid-strain-driving-residential-solar-battery-demand/)

生成摘要时出错

---

## 35. The Boring Part of Bell Labs (2025)

**原文标题**: The Boring Part of Bell Labs (2025)

**原文链接**: [https://acesounderglass.com/2025/11/15/the-boring-part-of-bell-labs/](https://acesounderglass.com/2025/11/15/the-boring-part-of-bell-labs/)

生成摘要时出错

---

## 36. When “idle” isn't idle: how a Linux kernel optimization became a QUIC bug

**原文标题**: When “idle” isn't idle: how a Linux kernel optimization became a QUIC bug

**原文链接**: [https://blog.cloudflare.com/quic-death-spiral-fix/](https://blog.cloudflare.com/quic-death-spiral-fix/)

生成摘要时出错

---

## 37. Restore full BambuNetwork support for Bambu Lab printers

**原文标题**: Restore full BambuNetwork support for Bambu Lab printers

**原文链接**: [https://github.com/FULU-Foundation/OrcaSlicer-bambulab](https://github.com/FULU-Foundation/OrcaSlicer-bambulab)

生成摘要时出错

---

## 38. Traceway: MIT-licensed observability stack you can self-host in ~90s

**原文标题**: Traceway: MIT-licensed observability stack you can self-host in ~90s

**原文链接**: [https://github.com/tracewayapp/traceway](https://github.com/tracewayapp/traceway)

生成摘要时出错

---

## 39. Fragnesia Made Public as Latest Linux Local Privilege Escalation Vulnerability

**原文标题**: Fragnesia Made Public as Latest Linux Local Privilege Escalation Vulnerability

**原文链接**: [https://www.phoronix.com/news/Linux-Fragnesia](https://www.phoronix.com/news/Linux-Fragnesia)

生成摘要时出错

---

## 40. Googlebook

**原文标题**: Googlebook

**原文链接**: [https://googlebook.google/](https://googlebook.google/)

生成摘要时出错

---

## 41. As researchers age, they produce less disruptive work

**原文标题**: As researchers age, they produce less disruptive work

**原文链接**: [https://nautil.us/is-this-why-science-advances-one-funeral-at-a-time-1280650](https://nautil.us/is-this-why-science-advances-one-funeral-at-a-time-1280650)

生成摘要时出错

---

## 42. My graduation cap runs Rust

**原文标题**: My graduation cap runs Rust

**原文链接**: [https://ericswpark.com/blog/2026/2026-05-12-my-graduation-cap-runs-rust/](https://ericswpark.com/blog/2026/2026-05-12-my-graduation-cap-runs-rust/)

生成摘要时出错

---

## 43. Notepad++ Mac Port Renamed Nextpad++ After Trademark Row

**原文标题**: Notepad++ Mac Port Renamed Nextpad++ After Trademark Row

**原文链接**: [https://www.macrumors.com/2026/05/13/notepad-plus-plus-mac-nextpad-dispute-settlement/](https://www.macrumors.com/2026/05/13/notepad-plus-plus-mac-nextpad-dispute-settlement/)

生成摘要时出错

---

## 44. Use the Claude Agent SDK with Your Claude Plan

**原文标题**: Use the Claude Agent SDK with Your Claude Plan

**原文链接**: [https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan)

生成摘要时出错

---

## 45. The vi family

**原文标题**: The vi family

**原文链接**: [https://lpar.ATH0.com/posts/2026/05/the-vi-family/](https://lpar.ATH0.com/posts/2026/05/the-vi-family/)

生成摘要时出错

---

## 46. Residents furious as Utah approves datacenter twice the size of Manhattan

**原文标题**: Residents furious as Utah approves datacenter twice the size of Manhattan

**原文链接**: [https://www.theguardian.com/us-news/2026/may/13/utah-approves-datacenter-backlash](https://www.theguardian.com/us-news/2026/may/13/utah-approves-datacenter-backlash)

生成摘要时出错

---

## 47. Neanderthals drilled cavities to treat a toothache 59,000 years ago

**原文标题**: Neanderthals drilled cavities to treat a toothache 59,000 years ago

**原文链接**: [https://arstechnica.com/science/2026/05/neanderthals-drilled-cavities-to-treat-a-toothache-59000-years-ago/](https://arstechnica.com/science/2026/05/neanderthals-drilled-cavities-to-treat-a-toothache-59000-years-ago/)

生成摘要时出错

---

## 48. SecurityBaseline.eu

**原文标题**: SecurityBaseline.eu

**原文链接**: [https://internetcleanup.foundation/2026/05/european-governments-3000-tracking-sites-1000-phpmyadmins-and-99pct-poorly-encrypted-email-introducing-securitybaseline-eu/](https://internetcleanup.foundation/2026/05/european-governments-3000-tracking-sites-1000-phpmyadmins-and-99pct-poorly-encrypted-email-introducing-securitybaseline-eu/)

生成摘要时出错

---

## 49. US producer prices surprise with largest increase in four years

**原文标题**: US producer prices surprise with largest increase in four years

**原文链接**: [https://www.reuters.com/business/us-producer-prices-post-biggest-gain-four-years-april-2026-05-13/](https://www.reuters.com/business/us-producer-prices-post-biggest-gain-four-years-april-2026-05-13/)

生成摘要时出错

---

## 50. Fc, a lossless compressor for floating-point streams

**原文标题**: Fc, a lossless compressor for floating-point streams

**原文链接**: [https://github.com/xtellect/fc](https://github.com/xtellect/fc)

生成摘要时出错

---

## 51. Why senior developers fail to communicate their expertise

**原文标题**: Why senior developers fail to communicate their expertise

**原文链接**: [https://www.nair.sh/guides-and-opinions/communicating-your-expertise/why-senior-developers-fail-to-communicate-their-expertise](https://www.nair.sh/guides-and-opinions/communicating-your-expertise/why-senior-developers-fail-to-communicate-their-expertise)

生成摘要时出错

---

## 52. Electricity generation from solar could exceed coal in ERCOT for the first time

**原文标题**: Electricity generation from solar could exceed coal in ERCOT for the first time

**原文链接**: [https://www.eia.gov/todayinenergy/detail.php?id=67685](https://www.eia.gov/todayinenergy/detail.php?id=67685)

生成摘要时出错

---

## 53. Pyrefly v1.0.0 is here (Type Checker / Language Server for Python) [video]

**原文标题**: Pyrefly v1.0.0 is here (Type Checker / Language Server for Python) [video]

**原文链接**: [https://www.youtube.com/watch?v=_o0TZG_xrys](https://www.youtube.com/watch?v=_o0TZG_xrys)

生成摘要时出错

---

## 54. How to make your text look futuristic (2016)

**原文标题**: How to make your text look futuristic (2016)

**原文链接**: [https://typesetinthefuture.com/2016/02/18/futuristic/](https://typesetinthefuture.com/2016/02/18/futuristic/)

生成摘要时出错

---

## 55. Redis and the Cost of Ambition

**原文标题**: Redis and the Cost of Ambition

**原文链接**: [https://charlesleifer.com/blog/redis-and-the-cost-of-ambition/](https://charlesleifer.com/blog/redis-and-the-cost-of-ambition/)

生成摘要时出错

---

## 56. What if there was no BASIC in EndBASIC?

**原文标题**: What if there was no BASIC in EndBASIC?

**原文链接**: [https://blogsystem5.substack.com/p/no-basic-in-endbasic](https://blogsystem5.substack.com/p/no-basic-in-endbasic)

生成摘要时出错

---

## 57. Up in Smoke

**原文标题**: Up in Smoke

**原文链接**: [https://thebaffler.com/odds-and-ends/the-profession-that-does-not-exist-symposium](https://thebaffler.com/odds-and-ends/the-profession-that-does-not-exist-symposium)

生成摘要时出错

---

## 58. Tell NYT, Atlantic, USA Today to keep Wayback Machine

**原文标题**: Tell NYT, Atlantic, USA Today to keep Wayback Machine

**原文链接**: [https://www.savethearchive.com/newsleaders/](https://www.savethearchive.com/newsleaders/)

生成摘要时出错

---

## 59. When life gives you lemons, write better error messages

**原文标题**: When life gives you lemons, write better error messages

**原文链接**: [https://wix-ux.com/when-life-gives-you-lemons-write-better-error-messages-46c5223e1a2f](https://wix-ux.com/when-life-gives-you-lemons-write-better-error-messages-46c5223e1a2f)

生成摘要时出错

---

## 60. CERT is releasing six CVEs for serious security vulnerabilities in dnsmasq

**原文标题**: CERT is releasing six CVEs for serious security vulnerabilities in dnsmasq

**原文链接**: [https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html)

生成摘要时出错

---

## 61. Scrcpy v4.0

**原文标题**: Scrcpy v4.0

**原文链接**: [https://github.com/Genymobile/scrcpy/releases/tag/v4.0](https://github.com/Genymobile/scrcpy/releases/tag/v4.0)

生成摘要时出错

---

## 62. Starship V3

**原文标题**: Starship V3

**原文链接**: [https://www.spacex.com/updates#starship-v3](https://www.spacex.com/updates#starship-v3)

生成摘要时出错

---

## 63. EU browser choice rules send millions more users Firefox's way

**原文标题**: EU browser choice rules send millions more users Firefox's way

**原文链接**: [https://www.theregister.com/software/2026/05/12/eu-law-bestows-6m-more-firefox-users-upon-us-moz-says/5238623](https://www.theregister.com/software/2026/05/12/eu-law-bestows-6m-more-firefox-users-upon-us-moz-says/5238623)

生成摘要时出错

---

## 64. Valve snuck a Wilhelm scream Easter egg into the new Steam Controller

**原文标题**: Valve snuck a Wilhelm scream Easter egg into the new Steam Controller

**原文链接**: [https://www.pcgamer.com/hardware/steam-machines/valve-snuck-a-wilhelm-scream-easter-egg-into-the-new-steam-controller/](https://www.pcgamer.com/hardware/steam-machines/valve-snuck-a-wilhelm-scream-easter-egg-into-the-new-steam-controller/)

生成摘要时出错

---

## 65. Launch HN: Voker (YC S24) – Analytics for AI Agents

**原文标题**: Launch HN: Voker (YC S24) – Analytics for AI Agents

**原文链接**: [https://voker.ai](https://voker.ai)

生成摘要时出错

---

## 66. Almost half of everything orbiting Earth is space junk

**原文标题**: Almost half of everything orbiting Earth is space junk

**原文链接**: [https://www.popsci.com/science/space-junk-around-earth/](https://www.popsci.com/science/space-junk-around-earth/)

生成摘要时出错

---

## 67. Show HN: Statewright – Visual state machines that make AI agents reliable

**原文标题**: Show HN: Statewright – Visual state machines that make AI agents reliable

**原文链接**: [https://github.com/statewright/statewright](https://github.com/statewright/statewright)

生成摘要时出错

---

## 68. Pyrefly v1.0 is here (fast type checker and language server for Python)

**原文标题**: Pyrefly v1.0 is here (fast type checker and language server for Python)

**原文链接**: [https://pyrefly.org/blog/v1.0/](https://pyrefly.org/blog/v1.0/)

生成摘要时出错

---

## 69. Lanzaboote – NixOS Secure Boot

**原文标题**: Lanzaboote – NixOS Secure Boot

**原文链接**: [https://x86.lol/generic/2022/11/26/lanzaboote.html](https://x86.lol/generic/2022/11/26/lanzaboote.html)

生成摘要时出错

---

## 70. Israel's AI targeting system: how data from a phone become a death sentence

**原文标题**: Israel's AI targeting system: how data from a phone become a death sentence

**原文链接**: [https://www.latimes.com/world-nation/story/2026-05-04/inside-israels-ai-targeting-system-how-data-from-phone-become-death-sentence](https://www.latimes.com/world-nation/story/2026-05-04/inside-israels-ai-targeting-system-how-data-from-phone-become-death-sentence)

生成摘要时出错

---

## 71. The limits of Rust, or why you should probably not follow Amazon and Cloudflare

**原文标题**: The limits of Rust, or why you should probably not follow Amazon and Cloudflare

**原文链接**: [https://kerkour.com/the-limits-of-rust](https://kerkour.com/the-limits-of-rust)

生成摘要时出错

---

## 72. AI startup upgrades Euro air traffic systems and raises $5.5M

**原文标题**: AI startup upgrades Euro air traffic systems and raises $5.5M

**原文链接**: [https://designverse.ai/blog](https://designverse.ai/blog)

生成摘要时出错

---

## 73. Quack: The DuckDB Client-Server Protocol

**原文标题**: Quack: The DuckDB Client-Server Protocol

**原文链接**: [https://duckdb.org/2026/05/12/quack-remote-protocol](https://duckdb.org/2026/05/12/quack-remote-protocol)

生成摘要时出错

---

## 74. Rendering the Sky, Sunsets, and Planets

**原文标题**: Rendering the Sky, Sunsets, and Planets

**原文链接**: [https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/](https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/)

生成摘要时出错

---

## 75. I made Rust’s cargo copy but for CPP

**原文标题**: I made Rust’s cargo copy but for CPP

**原文链接**: [https://github.com/user-with-username/crow](https://github.com/user-with-username/crow)

生成摘要时出错

---

## 76. Referer Reality

**原文标题**: Referer Reality

**原文链接**: [https://www.robinsloan.com/lab/referer/](https://www.robinsloan.com/lab/referer/)

生成摘要时出错

---

## 77. Postmortem: TanStack NPM supply-chain compromise

**原文标题**: Postmortem: TanStack NPM supply-chain compromise

**原文链接**: [https://tanstack.com/blog/npm-supply-chain-compromise-postmortem](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)

生成摘要时出错

---

## 78. Foucault's Order of Things Explained with Trading Cards [video]

**原文标题**: Foucault's Order of Things Explained with Trading Cards [video]

**原文链接**: [https://www.youtube.com/watch?v=1TbHYjGvS68](https://www.youtube.com/watch?v=1TbHYjGvS68)

生成摘要时出错

---

## 79. Dead.Letter (CVE-2026-45185) – How XBOW found an unauthenticated RCE on Exim

**原文标题**: Dead.Letter (CVE-2026-45185) – How XBOW found an unauthenticated RCE on Exim

**原文链接**: [https://xbow.com/blog/dead-letter-cve-2026-45185-xbow-found-rce-exim](https://xbow.com/blog/dead-letter-cve-2026-45185-xbow-found-rce-exim)

生成摘要时出错

---

## 80. The Future of Obsidian Plugins

**原文标题**: The Future of Obsidian Plugins

**原文链接**: [https://obsidian.md/blog/future-of-plugins/](https://obsidian.md/blog/future-of-plugins/)

生成摘要时出错

---

## 81. Learning Software Architecture

**原文标题**: Learning Software Architecture

**原文链接**: [https://matklad.github.io/2026/05/12/software-architecture.html](https://matklad.github.io/2026/05/12/software-architecture.html)

生成摘要时出错

---

## 82. EFF to 4th Circuit: Electronic Device Searches at the Border Require a Warrant

**原文标题**: EFF to 4th Circuit: Electronic Device Searches at the Border Require a Warrant

**原文链接**: [https://www.eff.org/deeplinks/2026/05/eff-fourth-circuit-electronic-device-searches-border-require-warrant](https://www.eff.org/deeplinks/2026/05/eff-fourth-circuit-electronic-device-searches-border-require-warrant)

生成摘要时出错

---

## 83. Show HN: FixMyNPM, CLI to fix your insecure npm config

**原文标题**: Show HN: FixMyNPM, CLI to fix your insecure npm config

**原文链接**: [https://github.com/madhugb/FixMyNPM](https://github.com/madhugb/FixMyNPM)

**FixMyNPM** is a Go-based CLI tool designed to diagnose and repair insecure `.npmrc` configurations across both global and project-level directories. Built to align with npm security best practices, the tool addresses vulnerabilities such as man-in-the-middle (MITM) risks from insecure HTTP registries, disabled TLS verification, and accidental credential leaks.

The tool offers four primary commands:

*   **doctor**: Analyzes the global `~/.npmrc` for critical security flaws and suggests immediate fixes.
*   **scan**: Searches directory trees for `.npmrc` files or specific packages. It includes an "incident mode" for supply chain security, allowing users to hunt for compromised packages (using semver ranges) or detect registry hijacking via bundled config files within `node_modules`.
*   **audit**: Performs a comprehensive security scan of all configurations within a specified root directory.
*   **fixer**: Automatically applies recommended security patches, featuring a dry-run mode to preview changes before they are written.

FixMyNPM categorizes issues by severity, flagging critical errors like hardcoded auth tokens in project files and warnings for risky settings like disabled `ignore-scripts`. By automating the identification of registry hijacking and dependency confusion risks, it serves as a specialized utility for both routine maintenance and rapid incident response. 

The tool is open-source under the MIT License and can be installed via `go install github.com/madhugb/fixmynpm@latest`.

---

## 84. Blaise v0.7.0 (alpha) – Independent of Free Pascal compiler

**原文标题**: Blaise v0.7.0 (alpha) – Independent of Free Pascal compiler

**原文链接**: [https://github.com/graemeg/blaise/discussions/24](https://github.com/graemeg/blaise/discussions/24)

生成摘要时出错

---

## 85. Screenshots of Old Desktop OSes

**原文标题**: Screenshots of Old Desktop OSes

**原文链接**: [http://www.typewritten.org/Media/](http://www.typewritten.org/Media/)

生成摘要时出错

---

## 86. xAI Adds 19 New Gas Turbines Despite Ongoing Lawsuit

**原文标题**: xAI Adds 19 New Gas Turbines Despite Ongoing Lawsuit

**原文链接**: [https://www.wired.com/story/xai-adds-19-new-gas-turbines-despite-ongoing-lawsuit/](https://www.wired.com/story/xai-adds-19-new-gas-turbines-despite-ongoing-lawsuit/)

生成摘要时出错

---

## 87. I hate soldering

**原文标题**: I hate soldering

**原文链接**: [https://user8.bearblog.dev/rant/](https://user8.bearblog.dev/rant/)

生成摘要时出错

---

## 88. Canada’s Bill C-22 Is a Repackaged Version of Last Year’s Surveillance Nightmare

**原文标题**: Canada’s Bill C-22 Is a Repackaged Version of Last Year’s Surveillance Nightmare

**原文链接**: [https://www.eff.org/deeplinks/2026/05/canadas-bill-c-22-repackaged-version-last-years-surveillance-nightmare](https://www.eff.org/deeplinks/2026/05/canadas-bill-c-22-repackaged-version-last-years-surveillance-nightmare)

生成摘要时出错

---

## 89. Dutch suicide prevention website shares data with tech companies without consent

**原文标题**: Dutch suicide prevention website shares data with tech companies without consent

**原文链接**: [https://nltimes.nl/2026/05/13/dutch-suicide-prevention-hotline-shares-visitor-data-tech-companies](https://nltimes.nl/2026/05/13/dutch-suicide-prevention-hotline-shares-visitor-data-tech-companies)

生成摘要时出错

---

## 90. Canada’s Bill C-22 Is a Repackaged Version of Last Year’s Surveillance Nightmare

**原文标题**: Canada’s Bill C-22 Is a Repackaged Version of Last Year’s Surveillance Nightmare

**原文链接**: [https://www.eff.org/deeplinks/2026/05/canadas-bill-c-22-repackaged-version-last-years-surveillance-nightmare](https://www.eff.org/deeplinks/2026/05/canadas-bill-c-22-repackaged-version-last-years-surveillance-nightmare)

生成摘要时出错

---

## 91. Reimagining the mouse pointer for the AI era

**原文标题**: Reimagining the mouse pointer for the AI era

**原文链接**: [https://deepmind.google/blog/ai-pointer/](https://deepmind.google/blog/ai-pointer/)

生成摘要时出错

---

## 92. Extremely Low Frequencies

**原文标题**: Extremely Low Frequencies

**原文链接**: [https://computer.rip/2026-05-09-extremely-low-frequencies.html](https://computer.rip/2026-05-09-extremely-low-frequencies.html)

生成摘要时出错

---

## 93. Hardware Attestation as Monopoly Enabler

**原文标题**: Hardware Attestation as Monopoly Enabler

**原文链接**: [https://grapheneos.social/@GrapheneOS/116550899908879585](https://grapheneos.social/@GrapheneOS/116550899908879585)

生成摘要时出错

---

## 94. Software Internals Book Club

**原文标题**: Software Internals Book Club

**原文链接**: [https://eatonphil.com/bookclub.html](https://eatonphil.com/bookclub.html)

生成摘要时出错

---

## 95. Fragnesia

**原文标题**: Fragnesia

**原文链接**: [https://github.com/v12-security/pocs/tree/main/fragnesia](https://github.com/v12-security/pocs/tree/main/fragnesia)

生成摘要时出错

---

## 96. Show HN: TikTok but for scientific papers

**原文标题**: Show HN: TikTok but for scientific papers

**原文链接**: [https://andreaturchet.github.io/website/index.html](https://andreaturchet.github.io/website/index.html)

生成摘要时出错

---

## 97. If AI writes your code, why use Python?

**原文标题**: If AI writes your code, why use Python?

**原文链接**: [https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055](https://medium.com/@NMitchem/if-ai-writes-your-code-why-use-python-bf8c4ba1a055)

生成摘要时出错

---

## 98. The Surprisingly Long Life of the Vacuum Tube

**原文标题**: The Surprisingly Long Life of the Vacuum Tube

**原文链接**: [https://www.construction-physics.com/p/the-surprisingly-long-life-of-the](https://www.construction-physics.com/p/the-surprisingly-long-life-of-the)

生成摘要时出错

---

## 99. Testing UPS Output Waveforms

**原文标题**: Testing UPS Output Waveforms

**原文链接**: [https://www.lttlabs.com/articles/2026/05/12/ups-exploration](https://www.lttlabs.com/articles/2026/05/12/ups-exploration)

生成摘要时出错

---

## 100. Local AI needs to be the norm

**原文标题**: Local AI needs to be the norm

**原文链接**: [https://unix.foo/posts/local-ai-needs-to-be-norm/](https://unix.foo/posts/local-ai-needs-to-be-norm/)

生成摘要时出错

---

