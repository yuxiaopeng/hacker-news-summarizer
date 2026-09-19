# Hacker News 热门文章摘要 (2026-09-19)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 一年前，我利用强化学习构建了非自回归决策模型。

**原文标题**: I built non-autoregressive decision models with RL a year ago

**原文链接**: [https://laya.convaiinnovations.com/](https://laya.convaiinnovations.com/)

Laya 是一个开源的“系统 1”决策模型系列，旨在取代缓慢且昂贵的自回归大语言模型，用于处理分类、路由和筛选等反射性任务。Laya 由一位在该领域早于 TypeSafe 的 Jev 等闭源竞争对手一年便开创此方法的作者开发，利用双向编码器和校准决策强化学习 (RLCD) 来提供近乎即时的结构化输出。

核心亮点包括：

*   **性能与速度：** Laya 的单次前向传播延迟仅为 32.8 毫秒，比同类闭源产品快约 8 倍，且通过私有化部署可实现零运行成本。
*   **三种决策基元：** 该模型不生成文本，而是使用 `choice`（多分类）、`score`（序数）和 `noul`（布尔概率）函数。这种架构从物理层面杜绝了幻觉和架构违规。
*   **多语言支持：** 系统包含一个亚毫秒级路由器，可检测 100 多种语言的脚本，自动将查询引导至最有效的专用检查点（例如用于英语的 ModernBERT-large 或用于多语言任务的 mmBERT-base）。
*   **卓越的校准：** Laya 的校准误差 (ECE) 显著低于闭源模型，能够提供反映实际准确率的“真实”概率。
*   **易用性：** 模型权重已在 Apache 2.0 协议下发布于 Hugging Face，并配有专门的 Python SDK（`pip install laya`）和用于微调的专业训练笔记本。

虽然 Laya 针对选项少于 20 个的架构进行了优化，且需要微调以实现最佳零样本性能，但它代表了向高速、可离网且具成本效益的 AI 决策方式的重大转变。

---

## 2. AI生成的海报不必如此糟糕

**原文标题**: AI-generated posters don’t have to be horrible

**原文链接**: [https://john.hartnup.uk/2026/06/07/ai-event-posters.html](https://john.hartnup.uk/2026/06/07/ai-event-posters.html)

文章**《AI生成的海报未必糟糕》**针对人们对“千篇一律”的AI海报——即常用于当地活动的重复、平庸的设计——日益增长的不满进行了探讨。作者认为，这种乏味并非AI本身的局限，而是由于用户接受了默认设置。

为了克服这种“默认感”，作者展示了特定的提示词如何开启更广泛、更高级的审美。核心要点包括：

*   **明确设计流派：** 与其让AI自行选择布局，用户应要求特定的风格，如**包豪斯（Bauhaus）、瑞士风格（Swiss Style）、日式极简主义（Japanese Minimalism）或孟菲斯设计（Memphis Design）**。这将使输出作品从“业余集市”水平提升至类似画廊海报或专业传单的质感。
*   **将AI视为设计顾问：** 如果你不熟悉艺术史，可以要求AI提供一份多样化风格的“菜单”。作者重点推荐了**孔版印刷（Risograph）、粗野主义（Brutalist）和90年代狂欢（90s Rave）审美**等选项，以使海报脱颖而出。
*   **管理上下文：** 作者指出，随着对话的深入，AI可能会根据此前的交互开始自行添加“创意”文本或元素。为了保持设计简洁，通常最好在选定风格后重新开启新对话。
*   **超越平面图像：** 虽然作者主要关注图像生成，但他也建议利用Claude或Gemini等工具生成可编辑的格式（如HTML或SVG）。这允许用户直接操作图层和文本，而不必受限于静态、不可编辑的图像。

最终的核心观点是，尽管目光敏锐的人或许仍能辨认出AI生成的痕迹，但只要用户运用特定的设计词汇，而非依赖通用的提示词，作品就能变得极具视觉冲击力且独具特色。

---

## 3. Btrfs/ZFS/bcachefs 实际工作负载：略过经典基准测试

**原文标题**: Btrfs/ZFS/bcachefs under workloads classic benchmarks skip

**原文链接**: [https://bartosz.fenski.pl/modern-fs-benchmark/](https://bartosz.fenski.pl/modern-fs-benchmark/)

Bartosz Fenski 的文章指出，传统的综合基准测试（如顺序读/写速度）无法准确反映现代写时复制 (CoW) 文件系统的性能。相反，他通过处理元数据密集型的真实工作负载，对 **Btrfs、ZFS 和 bcachefs** 进行了评估。

作者强调，虽然经典的基准测试更青睐 EXT4 等旧式文件系统，但用户选择现代文件系统是为了数据完整性（校验和）、快照和内置 RAID 等功能。该研究重点关注三个主要场景：**软件编译 (GCC)**、**数据库操作 (PostgreSQL)** 和 **软件包管理 (apt)**。

**主要观察结果：**

*   **ZFS：** 依然是最稳定且功能最完备的选择，提供了卓越的数据保护。然而，由于其高资源需求以及源自 Solaris 移植的开销，它在简单任务中通常表现出较高的延迟和较慢的性能。
*   **Btrfs：** 在面向桌面的任务中表现良好，但在沉重的随机写工作负载（如数据库）下性能下降明显。这主要是由其 CoW 特性导致的碎片化造成的，通常需要对特定文件进行手动调优（如使用 `nodatacow`）。
*   **bcachefs：** 这个较新的文件系统表现尤为出色。它弥合了传统文件系统的速度与 ZFS/Btrfs 先进功能集之间的差距，展现了令人印象深刻的效率和低延迟，预示着它将成为 Linux 生态系统中强有力的竞争者。

**结论：**
Fenski 总结道，文件系统的选择应基于特定的功能需求（如原生加密或多设备管理），而非单纯的 MB/s 吞吐量。他强调，虽然 ZFS 是关键数据“最安全”的选择，但对于那些需要 CoW 功能且不希望牺牲性能的用户来说，bcachefs 正被证明是一个高性能且现代的替代方案。

---

## 4. 斯坦福医学院领导的研究发现：人类大脑是两个独立的器官。

**原文标题**: Human brain is two separate organs, Stanford Medicine-led research finds

**原文链接**: [https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html](https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html)

由斯坦福医学院领导的最新研究颠覆了长期以来认为人类大脑是一个单一、统一器官的观点。研究表明，大脑实际上由两个不同的器官组成，它们独立进化且源自不同的发育起源。

几十年来，科学家们一直认为单个祖细胞产生了整个大脑。然而，研究人员发现，在原肠胚形成过程中，大脑是由两个互斥的祖细胞群体发育而来的。其中一个表达 *Otx2* 基因的群体形成了前脑和中脑（负责高级思维），而另一个表达 *Gbx2* 基因的群体则形成了后脑或脑干（负责呼吸和心率等基本生存功能）。这两个谱系通过截然不同的 DNA 包装（染色质）被锁定在各自的命运中，这意味着它们在平行轨道上运行，永不重叠。

这一发现解释了为何科学家此前难以在实验室中培养后脑神经元。利用这一新认知，斯坦福团队首次成功诱导人类干细胞转化为功能性后脑运动神经元。这一突破对于研究脊髓性肌萎缩症（SMA）和肌萎缩侧索硬化症（ALS）等影响脑干的毁灭性疾病至关重要。此外，由于后脑包含调节饥饿的回路，该研究也为肥胖研究开辟了新途径。

从进化角度看，这种双重起源模式可追溯至 5.5 亿多年前，并为从斑马鱼到柱头虫等多种物种所共有。研究结果表明，进化将两个古老且独立的神经系统合并到了同一个空间结构中。这项研究标志着神经科学领域的重大转变，为理解大脑发育以及开发针对复杂神经系统疾病的再生疗法提供了全新的框架。

---

## 5. 适用于 ZX Spectrum 的图形化桌面

**原文标题**: A graphical desktop for the ZX Spectrum

**原文链接**: [https://github.com/mindbox77/zxdesk](https://github.com/mindbox77/zxdesk)

**ZX Desk** 是一个专为 48K Sinclair ZX Spectrum 开发的图形桌面环境，完全采用 Z80 汇编语言编写。它在 1982 年的硬件上实现了类似 GEM 的操作体验，具备重叠窗口、下拉菜单、文件管理器以及多种桌面附件（记事本、时钟、日历）。尽管该机器仅搭载 3.5 MHz 的 CPU 且存在属性冲突（attribute-clash）显示限制，该系统仍能在 69,888 个 T 周期的单帧内实现窗口拖动。

该项目的文档侧重于实测数据而非“硬件传闻”。关键技术发现包括：

*   **ULA 争用：** 普遍观点认为屏幕渲染期间的内存访问会导致 50% 的性能损失，但实际测量显示，该成本仅约为 14.7%。
*   **性能瓶颈：** 绘制文本占窗口渲染耗时的 50%，而“填充”仅占 21%。开发者指出，在 Z80 处理器上，针对“每行开销”的优化比提升“每字节吞吐量”更为关键。
*   **中断管理：** 一项重要发现是，Spectrum 发出中断信号的持续时间仅为 32 个 T 周期。如果在该窗口期内禁用了中断（DI），中断将会**丢失**而非推迟。为此，开发者发明了一种名为“欠下最后一次压栈（owing the last push）”的新技术，允许高速屏幕填充程序在使用堆栈指针（SP）的同时保持中断开启，从而防止系统定时失效。

该系统采用自底向上的架构，利用专用设备层、事件队列和内存管理堆。它支持包括 RAM 磁盘和 esxDOS 在内的多种存储后端。作为一项“心血之作”，ZX Desk 既是 Spectrum 上的实用操作系统，也是 Z80 开发者研究内存争用和精确帧时序的详细技术资源。

---

## 6. Tin：Postgres 全文搜索

**原文标题**: Tin: full-text search for Postgres

**原文链接**: [https://planetscale.com/blog/introducing-tin](https://planetscale.com/blog/introducing-tin)

TIN (Text INdex) 是一款新发布的、适用于 Postgres 和 Neki 数据库的通用版 (GA) 全文搜索扩展。TIN 旨在解决 GIN、ParadeDB 和 pg_textsearch 等现有解决方案的局限性，提供了一个快速、可靠且功能丰富的搜索引擎，并与 Postgres 的事务可见性、复制及备份系统原生集成。

**核心特性与性能**
TIN 支持高级搜索功能，包括布尔表达式、短语和跨度查询、模糊匹配以及 BM25 评分排序。在使用 Stack Exchange 等大规模语料库（1.5 亿个文档）的基准测试中，TIN 展现了卓越的性能：
*   **吞吐量：** 在各种工作负载下，TIN 的每秒查询数 (QPS) 是 ParadeDB 和 GIN 的 10 到 57 倍。
*   **延迟：** 其 p99 延迟比竞争对手低多达 26 倍。
*   **并发性：** 不同于在高负载下会停滞或显著变慢的其他扩展，TIN 即使在密集的并发更新（如每秒 1,000 次更新）期间也能保持高读取吞吐量。
*   **效率：** 索引构建速度显著加快——仅需 8 分钟，而 ParadeDB 需要 19 分钟，GIN 则需要 2 小时以上。

**架构创新**
TIN 速度优势的核心在于它直接使用 Postgres 的 `ctid`（元组标识符）作为文档 ID。竞争扩展通常分配顺序标识符，且必须执行开销巨大的二次映射来定位 Postgres 中的行，而 TIN 完全避免了这种开销。这种“Postgres 原生”方法实现了 O(1) 的行查找。此外，TIN 采用专门的两级位图编码来高效压缩 48 位标识符，从而支持高度矢量化的 CPU 操作并减少磁盘 I/O。

通过优化数据的读取和索引方式，无论索引是存储在内存中还是需要磁盘访问，TIN 都能确保搜索性能“快得惊人”。

---

## 7. Show HN: CUA-S1 – A System One Model for Computer Use

**原文标题**: Show HN: CUA-S1 – A System One Model for Computer Use

**原文链接**: [https://github.com/trycua/cua](https://github.com/trycua/cua)

Cua is an open-source ecosystem designed to enable AI agents to interact with computers via graphical interfaces, APIs, and code—a concept the creators call "Computer-Use 2.0." The suite provides the infrastructure, models, and evaluation tools necessary to build and deploy desktop automation agents.

Key components of the ecosystem include:

*   **CUA-S1:** A family of small, specialized "System 1" models designed for fast, bounded decision-making, such as form-filling and UI element scoring. These research models are hosted on Hugging Face and focus on structured interface interaction rather than general-purpose reasoning.
*   **Cua Fleets:** A service for provisioning isolated cloud desktops. Developers can use the Sandbox SDK to claim Linux desktops, run commands, and interact with applications in a secure, scalable environment.
*   **Cua Driver:** A cross-platform tool (macOS, Windows, Linux) that allows agents to inspect and operate native desktop apps. Notably, it supports background delivery, enabling agents to work without moving the user's physical cursor or taking focus.
*   **Lume:** A utility for managing local macOS and Linux VMs on Apple Silicon, facilitating unattended setup and SSH connectivity.
*   **Cua Bench:** A benchmarking framework for building computer-use tasks, evaluating agent trajectories, and generating training data.

The project is largely MIT-licensed and integrates with popular agents like Claude Code and Cursor. By providing both the "driver" for execution and the specialized models for UI navigation, Cua offers a comprehensive stack for developers building the next generation of computer-use automation.

---

## 8. 苏珊·齐亚尼的 Buchla 食谱

**原文标题**: Suzanne Ciani's Buchla Cookbook

**原文链接**: [https://echo.orpheusinstituut.be/article/suzannes-buchla-cookbook](https://echo.orpheusinstituut.be/article/suzannes-buchla-cookbook)

生成摘要时出错

---

## 9. 电路的秘密生活

**原文标题**: The Secret Life of Circuits

**原文链接**: [https://blog.coredump.cx/p/the-secret-life-of-circuits-is-here](https://blog.coredump.cx/p/the-secret-life-of-circuits-is-here)

生成摘要时出错

---

## 10. Supabase (YC S20) Is Hiring for OrioleDB

**原文标题**: Supabase (YC S20) Is Hiring for OrioleDB

**原文链接**: [https://supabase.link/orioledbjob](https://supabase.link/orioledbjob)

生成摘要时出错

---

## 11. Android 17 is the first since 3.x to add new APIs without releasing to the AOSP

**原文标题**: Android 17 is the first since 3.x to add new APIs without releasing to the AOSP

**原文链接**: [https://grapheneos.social/@GrapheneOS/117282080803799576](https://grapheneos.social/@GrapheneOS/117282080803799576)

生成摘要时出错

---

## 12. Black Holes or Black Hole Stars? Astronomers Spar over 'Little Red Dots'

**原文标题**: Black Holes or Black Hole Stars? Astronomers Spar over 'Little Red Dots'

**原文链接**: [https://www.quantamagazine.org/black-holes-or-black-hole-stars-astronomers-spar-over-webb-telescopes-little-red-dots-20260914/](https://www.quantamagazine.org/black-holes-or-black-hole-stars-astronomers-spar-over-webb-telescopes-little-red-dots-20260914/)

生成摘要时出错

---

## 13. New evidence for hidden chambers beyond Tutankhamun's tomb

**原文标题**: New evidence for hidden chambers beyond Tutankhamun's tomb

**原文链接**: [https://www.nature.com/articles/d41586-026-02621-2](https://www.nature.com/articles/d41586-026-02621-2)

生成摘要时出错

---

## 14. Almost Never Use AI to Write Anything Substantive

**原文标题**: Almost Never Use AI to Write Anything Substantive

**原文链接**: [https://erichgrunewald.substack.com/p/why-you-should-almost-never-use-ai](https://erichgrunewald.substack.com/p/why-you-should-almost-never-use-ai)

生成摘要时出错

---

## 15. GPT-6 Astra Solves a WWI German Radio Cipher

**原文标题**: GPT-6 Astra Solves a WWI German Radio Cipher

**原文链接**: [https://www.prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio](https://www.prinzai.com/p/gpt-6-astra-solves-a-wwi-german-radio)

生成摘要时出错

---

## 16. San Francisco Onion Futures Company

**原文标题**: San Francisco Onion Futures Company

**原文链接**: [https://onionfutures.com/](https://onionfutures.com/)

生成摘要时出错

---

## 17. Cloudflare Quick Tunnels

**原文标题**: Cloudflare Quick Tunnels

**原文链接**: [https://try.cloudflare.com/](https://try.cloudflare.com/)

生成摘要时出错

---

## 18. How to Write with an LLM

**原文标题**: How to Write with an LLM

**原文链接**: [https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm/](https://sockpuppet.org/blog/2026/09/17/how-to-write-with-an-llm/)

生成摘要时出错

---

## 19. What Zig felt like, coming from Rust

**原文标题**: What Zig felt like, coming from Rust

**原文链接**: [https://besok.github.io/posts/what-zig-felt-like-coming-from-rust/](https://besok.github.io/posts/what-zig-felt-like-coming-from-rust/)

生成摘要时出错

---

## 20. If math is more than proof, we need to better celebrate the rest of it

**原文标题**: If math is more than proof, we need to better celebrate the rest of it

**原文链接**: [https://terrytao.wordpress.com/2026/09/18/if-math-is-more-than-proof-we-need-to-better-celebrate-the-rest-of-it/](https://terrytao.wordpress.com/2026/09/18/if-math-is-more-than-proof-we-need-to-better-celebrate-the-rest-of-it/)

生成摘要时出错

---

## 21. Adventures in Microcontroller Circuit Debugging

**原文标题**: Adventures in Microcontroller Circuit Debugging

**原文链接**: [https://www.bigmessowires.com/2026/08/30/adventures-in-microcontroller-circuit-debugging/](https://www.bigmessowires.com/2026/08/30/adventures-in-microcontroller-circuit-debugging/)

生成摘要时出错

---

## 22. Saving another 100TB of RAM

**原文标题**: Saving another 100TB of RAM

**原文链接**: [https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/)

生成摘要时出错

---

## 23. You can run Git on object storage if you re-make packfiles

**原文标题**: You can run Git on object storage if you re-make packfiles

**原文链接**: [https://www.tigrisdata.com/blog/objgit-packfiles/](https://www.tigrisdata.com/blog/objgit-packfiles/)

生成摘要时出错

---

## 24. How OpenAI Used Its Own LLMs to Design Its Jalapeño Chip

**原文标题**: How OpenAI Used Its Own LLMs to Design Its Jalapeño Chip

**原文链接**: [https://spectrum.ieee.org/llms-for-chip-design](https://spectrum.ieee.org/llms-for-chip-design)

生成摘要时出错

---

## 25. Communication by means of modulated Johnson noise

**原文标题**: Communication by means of modulated Johnson noise

**原文链接**: [https://www.pnas.org/doi/10.1073/pnas.2201337119](https://www.pnas.org/doi/10.1073/pnas.2201337119)

生成摘要时出错

---

## 26. SDCC – Small Device C Compiler

**原文标题**: SDCC – Small Device C Compiler

**原文链接**: [https://sdcc.sourceforge.net/](https://sdcc.sourceforge.net/)

生成摘要时出错

---

## 27. Asking Authors About Their Own Papers

**原文标题**: Asking Authors About Their Own Papers

**原文链接**: [https://medium.com/@TmlrOrg/asking-authors-about-their-own-papers-3d2e04e5dee0](https://medium.com/@TmlrOrg/asking-authors-about-their-own-papers-3d2e04e5dee0)

生成摘要时出错

---

## 28. Ray Ozzie and the Optimism of Being Early

**原文标题**: Ray Ozzie and the Optimism of Being Early

**原文链接**: [https://reproof.app/blog/lotus-notes-history](https://reproof.app/blog/lotus-notes-history)

生成摘要时出错

---

## 29. Science Is Open Software

**原文标题**: Science Is Open Software

**原文链接**: [https://jepedersen.dk/blog/202505_research/](https://jepedersen.dk/blog/202505_research/)

生成摘要时出错

---

## 30. The first new cat species discovered in 100 years

**原文标题**: The first new cat species discovered in 100 years

**原文链接**: [https://www.nationalgeographic.com/animals/article/meet-the-first-new-cat-species-discovered-in-100-years](https://www.nationalgeographic.com/animals/article/meet-the-first-new-cat-species-discovered-in-100-years)

生成摘要时出错

---

## 31. Why building a Rust LSP is hard

**原文标题**: Why building a Rust LSP is hard

**原文链接**: [https://rust-glancer.github.io/blog/why-lsp-is-hard/](https://rust-glancer.github.io/blog/why-lsp-is-hard/)

生成摘要时出错

---

## 32. Ctenophores: Wonders of Biology

**原文标题**: Ctenophores: Wonders of Biology

**原文链接**: [https://www.quantamagazine.org/ctenophores-arent-just-beautiful-theyre-biological-wonders-20260916/](https://www.quantamagazine.org/ctenophores-arent-just-beautiful-theyre-biological-wonders-20260916/)

生成摘要时出错

---

## 33. Show HN: Cactus Needle 3: 8-29MB automation models can match DeepSeek V4 Flash

**原文标题**: Show HN: Cactus Needle 3: 8-29MB automation models can match DeepSeek V4 Flash

**原文链接**: [https://cactuscompute.com/needle](https://cactuscompute.com/needle)

生成摘要时出错

---

## 34. From Stonemasons to Carpenters

**原文标题**: From Stonemasons to Carpenters

**原文链接**: [https://thelastsoftwareengineer.substack.com/p/from-stonemasons-to-carpenters](https://thelastsoftwareengineer.substack.com/p/from-stonemasons-to-carpenters)

生成摘要时出错

---

## 35. Photon-Emission-Guided Laser Fault Injection Enables RP2350 Secure Debug

**原文标题**: Photon-Emission-Guided Laser Fault Injection Enables RP2350 Secure Debug

**原文链接**: [https://donjon.ledger.com/blog/rp2350-secure-debug-laser-fault-injection/](https://donjon.ledger.com/blog/rp2350-secure-debug-laser-fault-injection/)

生成摘要时出错

---

## 36. Goroutine Leak Profiles

**原文标题**: Goroutine Leak Profiles

**原文链接**: [https://go.dev/blog/goroutine-leak-profiles](https://go.dev/blog/goroutine-leak-profiles)

生成摘要时出错

---

## 37. Warez: The Infrastructure and Aesthetics of Piracy (2021)

**原文标题**: Warez: The Infrastructure and Aesthetics of Piracy (2021)

**原文链接**: [https://archive.org/details/b904a8eb-9c98-4bb1-bf25-3cb9d075b157](https://archive.org/details/b904a8eb-9c98-4bb1-bf25-3cb9d075b157)

生成摘要时出错

---

## 38. Inside ZCode: Silently uploading your Git history to the cloud

**原文标题**: Inside ZCode: Silently uploading your Git history to the cloud

**原文链接**: [https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/)

生成摘要时出错

---

## 39. NASA-IBM Lunar Foundation open-Source Geospatial AI Model

**原文标题**: NASA-IBM Lunar Foundation open-Source Geospatial AI Model

**原文链接**: [https://newsroom.usra.edu/usra-contributes-planetary-science-expertise-to-nasa-ibm-lunar-foundation-model/](https://newsroom.usra.edu/usra-contributes-planetary-science-expertise-to-nasa-ibm-lunar-foundation-model/)

生成摘要时出错

---

## 40. Cache-to-Cache: Direct Semantic Communication Between LLMs (2025)

**原文标题**: Cache-to-Cache: Direct Semantic Communication Between LLMs (2025)

**原文链接**: [https://arxiv.org/abs/2510.03215](https://arxiv.org/abs/2510.03215)

生成摘要时出错

---

## 41. Microsoft director: AI scraping 'the largest theft of labor in human history'

**原文标题**: Microsoft director: AI scraping 'the largest theft of labor in human history'

**原文链接**: [https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-director-called-ai-scraping-the-largest-theft-of-labor-in-human-history-while-openai-head-brands-chatgpt-an-existential-threat-to-publishers-revelations-come-from-legal-briefs-filed-in-nyt-lawsuit](https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-director-called-ai-scraping-the-largest-theft-of-labor-in-human-history-while-openai-head-brands-chatgpt-an-existential-threat-to-publishers-revelations-come-from-legal-briefs-filed-in-nyt-lawsuit)

生成摘要时出错

---

## 42. Cyclomatic Complexity in C#

**原文标题**: Cyclomatic Complexity in C#

**原文链接**: [https://blog.ndepend.com/understanding-cyclomatic-complexity/](https://blog.ndepend.com/understanding-cyclomatic-complexity/)

生成摘要时出错

---

## 43. How SpaceX streamlined the Raptor engine

**原文标题**: How SpaceX streamlined the Raptor engine

**原文链接**: [https://www.construction-physics.com/p/how-spacex-streamlined-the-raptor](https://www.construction-physics.com/p/how-spacex-streamlined-the-raptor)

生成摘要时出错

---

## 44. Veronese's Dogs

**原文标题**: Veronese's Dogs

**原文链接**: [https://publicdomainreview.org/essay/veroneses-dogs](https://publicdomainreview.org/essay/veroneses-dogs)

生成摘要时出错

---

## 45. Lawsuit says Anthropic, OpenAI and others made illegal agreement on AI slowdown

**原文标题**: Lawsuit says Anthropic, OpenAI and others made illegal agreement on AI slowdown

**原文链接**: [https://apnews.com/article/antitrust-lawsuit-ai-slowdown-anthropic-openai-spacexai-google-960af4308161eaf4ed13c383b0ce1c1b](https://apnews.com/article/antitrust-lawsuit-ai-slowdown-anthropic-openai-spacexai-google-960af4308161eaf4ed13c383b0ce1c1b)

生成摘要时出错

---

## 46. We made Playwright 2x faster and 80% more token efficient

**原文标题**: We made Playwright 2x faster and 80% more token efficient

**原文链接**: [https://github.com/browserbase/stagehand](https://github.com/browserbase/stagehand)

生成摘要时出错

---

## 47. Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations

**原文标题**: Show HN: An e-ink frame that hears birds and draws them as 1800s illustrations

**原文链接**: [https://github.com/arnegiacomo/fugleramme](https://github.com/arnegiacomo/fugleramme)

生成摘要时出错

---

## 48. Two parallel neural ectoderm progenitors contribute to the developing brain

**原文标题**: Two parallel neural ectoderm progenitors contribute to the developing brain

**原文链接**: [https://www.newscientist.com/article/2589739-our-brain-evolved-from-two-primitive-nervous-systems-that-merged/](https://www.newscientist.com/article/2589739-our-brain-evolved-from-two-primitive-nervous-systems-that-merged/)

生成摘要时出错

---

## 49. Show HN: I wrote a custom assembler for CHIP-8 in C++

**原文标题**: Show HN: I wrote a custom assembler for CHIP-8 in C++

**原文链接**: [https://github.com/Tackx/c8-ass](https://github.com/Tackx/c8-ass)

生成摘要时出错

---

## 50. C++26: Trivial infinite loops are no longer undefined behaviour

**原文标题**: C++26: Trivial infinite loops are no longer undefined behaviour

**原文链接**: [https://www.sandordargo.com/blog/2026/09/16/cpp26-trivial-infinite-loops](https://www.sandordargo.com/blog/2026/09/16/cpp26-trivial-infinite-loops)

生成摘要时出错

---

## 51. Xcode 27.1 Beta Release Notes

**原文标题**: Xcode 27.1 Beta Release Notes

**原文链接**: [https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes)

生成摘要时出错

---

## 52. The Implications of Linguistic Illegibility for LLM Security

**原文标题**: The Implications of Linguistic Illegibility for LLM Security

**原文链接**: [https://arxiv.org/abs/2609.02852](https://arxiv.org/abs/2609.02852)

生成摘要时出错

---

## 53. Claude Code now reads AGENTS.md if there is no Claude.md

**原文标题**: Claude Code now reads AGENTS.md if there is no Claude.md

**原文链接**: [https://code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog)

生成摘要时出错

---

## 54. North Korean nuclear test sets off years of earthquakes

**原文标题**: North Korean nuclear test sets off years of earthquakes

**原文链接**: [https://www.science.org/content/article/north-korean-nuclear-test-sets-years-earthquakes](https://www.science.org/content/article/north-korean-nuclear-test-sets-years-earthquakes)

生成摘要时出错

---

## 55. I vibed a proof of Conway's conjecture

**原文标题**: I vibed a proof of Conway's conjecture

**原文链接**: [https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/](https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/)

生成摘要时出错

---

## 56. OpenJev

**原文标题**: OpenJev

**原文链接**: [https://openjev.com/](https://openjev.com/)

生成摘要时出错

---

## 57. Learning Another Language May Be One of the Best Ways to Keep Your Brain Healthy

**原文标题**: Learning Another Language May Be One of the Best Ways to Keep Your Brain Healthy

**原文链接**: [https://theconversation.com/learning-another-language-may-be-one-of-the-best-ways-to-keep-your-brain-healthy-as-you-age-291951](https://theconversation.com/learning-another-language-may-be-one-of-the-best-ways-to-keep-your-brain-healthy-as-you-age-291951)

生成摘要时出错

---

## 58. Jobs Without LeetCode

**原文标题**: Jobs Without LeetCode

**原文链接**: [https://noleet.lol/jobs](https://noleet.lol/jobs)

生成摘要时出错

---

## 59. DraftKings Uses A.I. To Target the Gamblers Likeliest to Lose

**原文标题**: DraftKings Uses A.I. To Target the Gamblers Likeliest to Lose

**原文链接**: [https://www.nytimes.com/2026/09/19/business/draftkings-ai.html](https://www.nytimes.com/2026/09/19/business/draftkings-ai.html)

生成摘要时出错

---

## 60. Minimal Phone 2

**原文标题**: Minimal Phone 2

**原文链接**: [https://minimalcompany.com/](https://minimalcompany.com/)

生成摘要时出错

---

## 61. AI chatbots are becoming experts at changing people's minds

**原文标题**: AI chatbots are becoming experts at changing people's minds

**原文链接**: [https://www.science.org/content/article/ai-chatbots-are-becoming-experts-changing-people-s-minds-what-s-their-secret](https://www.science.org/content/article/ai-chatbots-are-becoming-experts-changing-people-s-minds-what-s-their-secret)

生成摘要时出错

---

## 62. Pre-Greek: The lost language hidden within Ancient Greek

**原文标题**: Pre-Greek: The lost language hidden within Ancient Greek

**原文链接**: [https://linguisticdiscovery.com/posts/pre-greek/](https://linguisticdiscovery.com/posts/pre-greek/)

生成摘要时出错

---

## 63. The Pain Axis: LLMs Represent Self-Directed Harm and Act to Relieve It

**原文标题**: The Pain Axis: LLMs Represent Self-Directed Harm and Act to Relieve It

**原文链接**: [https://arxiv.org/abs/2609.16247](https://arxiv.org/abs/2609.16247)

生成摘要时出错

---

## 64. China's Electric Aviation Advantage Is a Transport System, Not a Prototype

**原文标题**: China's Electric Aviation Advantage Is a Transport System, Not a Prototype

**原文链接**: [https://cleantechnica.com/2026/09/19/china-electric-aviation-transport-system/](https://cleantechnica.com/2026/09/19/china-electric-aviation-transport-system/)

生成摘要时出错

---

## 65. Alibaba open-sources AI model that can detect cancer and nearly 150 conditions

**原文标题**: Alibaba open-sources AI model that can detect cancer and nearly 150 conditions

**原文链接**: [https://www.scmp.com/tech/big-tech/article/3368055/alibaba-open-sources-medical-ai-model-can-detect-cancer-and-nearly-150-conditions](https://www.scmp.com/tech/big-tech/article/3368055/alibaba-open-sources-medical-ai-model-can-detect-cancer-and-nearly-150-conditions)

生成摘要时出错

---

## 66. Replacing Pull Requests with Delta

**原文标题**: Replacing Pull Requests with Delta

**原文链接**: [https://zed.dev/blog/delta-public-beta](https://zed.dev/blog/delta-public-beta)

生成摘要时出错

---

## 67. Mathematicians Build Long-Awaited Graph Sandwich

**原文标题**: Mathematicians Build Long-Awaited Graph Sandwich

**原文链接**: [https://www.quantamagazine.org/mathematicians-build-long-awaited-graph-sandwich-20260918/](https://www.quantamagazine.org/mathematicians-build-long-awaited-graph-sandwich-20260918/)

生成摘要时出错

---

## 68. A heap overflow and SSO misconfiguration to compromise OpenAI internal repos

**原文标题**: A heap overflow and SSO misconfiguration to compromise OpenAI internal repos

**原文链接**: [https://www.hacktron.ai/blog/hacking-openai](https://www.hacktron.ai/blog/hacking-openai)

生成摘要时出错

---

## 69. LispBM is a concurrent Lisp for microcontrollers with message passing

**原文标题**: LispBM is a concurrent Lisp for microcontrollers with message passing

**原文链接**: [https://www.lispbm.com/](https://www.lispbm.com/)

生成摘要时出错

---

## 70. Show HN: Scry, programmable internet search w/ congestion pricing

**原文标题**: Show HN: Scry, programmable internet search w/ congestion pricing

**原文链接**: [https://scry.io/](https://scry.io/)

生成摘要时出错

---

## 71. A search-and-inference database from scratch in pure Zig

**原文标题**: A search-and-inference database from scratch in pure Zig

**原文链接**: [https://antfly.io/research/antfly-zig](https://antfly.io/research/antfly-zig)

生成摘要时出错

---

## 72. Four AI lab breaches were caused by a single underlying issue, Irregular says

**原文标题**: Four AI lab breaches were caused by a single underlying issue, Irregular says

**原文链接**: [https://thenextweb.com/news/irregular-four-labs-one-issue-disclosure-timeline-gemini](https://thenextweb.com/news/irregular-four-labs-one-issue-disclosure-timeline-gemini)

生成摘要时出错

---

## 73. I don't like passkeys

**原文标题**: I don't like passkeys

**原文链接**: [https://hawksley.dev/blog/i-dont-like-passkeys](https://hawksley.dev/blog/i-dont-like-passkeys)

生成摘要时出错

---

## 74. Bonsai 2 27B: Near-Lossless Compression in a 9x Smaller Footprint

**原文标题**: Bonsai 2 27B: Near-Lossless Compression in a 9x Smaller Footprint

**原文链接**: [https://prismml.com/news/bonsai-2-27b](https://prismml.com/news/bonsai-2-27b)

生成摘要时出错

---

## 75. Stepfun Step 5 Preview (LLM): On AA Pareto frontier

**原文标题**: Stepfun Step 5 Preview (LLM): On AA Pareto frontier

**原文链接**: [https://artificialanalysis.ai/models/step-5](https://artificialanalysis.ai/models/step-5)

生成摘要时出错

---

## 76. Astra for Law

**原文标题**: Astra for Law

**原文链接**: [https://openai.com/index/astra-for-law/](https://openai.com/index/astra-for-law/)

生成摘要时出错

---

## 77. From Geometry to Algebra and Back Again: 4000 Years of Papers (2023) [video]

**原文标题**: From Geometry to Algebra and Back Again: 4000 Years of Papers (2023) [video]

**原文链接**: [https://www.youtube.com/watch?v=1cRFfYQYGxE](https://www.youtube.com/watch?v=1cRFfYQYGxE)

生成摘要时出错

---

## 78. Diplodocus, Long Thought Exclusively American, Turns Up in Spain

**原文标题**: Diplodocus, Long Thought Exclusively American, Turns Up in Spain

**原文链接**: [https://www.sci.news/paleontology/spanish-diplodocus-15064.html](https://www.sci.news/paleontology/spanish-diplodocus-15064.html)

生成摘要时出错

---

## 79. Hister: A private search engine for the pages you visit and the files you keep

**原文标题**: Hister: A private search engine for the pages you visit and the files you keep

**原文链接**: [https://github.com/asciimoo/hister](https://github.com/asciimoo/hister)

生成摘要时出错

---

## 80. Suppress vulnerabilities applying Kubernetes context to scans

**原文标题**: Suppress vulnerabilities applying Kubernetes context to scans

**原文链接**: [https://github.com/alegrey91/vex8s](https://github.com/alegrey91/vex8s)

生成摘要时出错

---

## 81. Fujitsu launches made-in-Japan next-generation CPU FUJITSU-MONAKA

**原文标题**: Fujitsu launches made-in-Japan next-generation CPU FUJITSU-MONAKA

**原文链接**: [https://global.fujitsu/en-global/pr/news/2026/09/14-02](https://global.fujitsu/en-global/pr/news/2026/09/14-02)

生成摘要时出错

---

## 82. The American Religion of Self-Storage Facilities

**原文标题**: The American Religion of Self-Storage Facilities

**原文链接**: [https://www.newyorker.com/magazine/2026/09/21/the-american-religion-of-self-storage-facilities](https://www.newyorker.com/magazine/2026/09/21/the-american-religion-of-self-storage-facilities)

生成摘要时出错

---

## 83. US Military had close call after using AI for hallucinated intelligence report

**原文标题**: US Military had close call after using AI for hallucinated intelligence report

**原文链接**: [https://www.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship](https://www.cnn.com/2026/09/18/politics/us-military-ai-false-intelligence-china-ship)

生成摘要时出错

---

## 84. Warren Buffett Steps Down as Berkshire Chairman, Names Son to Replace Him

**原文标题**: Warren Buffett Steps Down as Berkshire Chairman, Names Son to Replace Him

**原文链接**: [https://www.nytimes.com/2026/09/18/business/warren-buffett-berkshire-chairman.html](https://www.nytimes.com/2026/09/18/business/warren-buffett-berkshire-chairman.html)

生成摘要时出错

---

## 85. Human brain is two separate organs

**原文标题**: Human brain is two separate organs

**原文链接**: [https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html](https://med.stanford.edu/news/all-news/2026/09/two-separate-brains.html)

生成摘要时出错

---

## 86. Ctenophores Aren't Just Beautiful. They're Biological Wonders

**原文标题**: Ctenophores Aren't Just Beautiful. They're Biological Wonders

**原文链接**: [https://www.quantamagazine.org/ctenophores-arent-just-beautiful-theyre-biological-wonders-20260916/](https://www.quantamagazine.org/ctenophores-arent-just-beautiful-theyre-biological-wonders-20260916/)

生成摘要时出错

---

## 87. Wax motor

**原文标题**: Wax motor

**原文链接**: [https://en.wikipedia.org/wiki/Wax_motor](https://en.wikipedia.org/wiki/Wax_motor)

生成摘要时出错

---

## 88. Flet 1.0 – Build cross-platform apps in Python

**原文标题**: Flet 1.0 – Build cross-platform apps in Python

**原文链接**: [https://flet.dev/](https://flet.dev/)

生成摘要时出错

---

## 89. The most important product decision is what you don't build

**原文标题**: The most important product decision is what you don't build

**原文链接**: [https://liamnugent.me/posts/what-you-dont-build/](https://liamnugent.me/posts/what-you-dont-build/)

生成摘要时出错

---

## 90. Nvidia announces native GPU programming in Rust

**原文标题**: Nvidia announces native GPU programming in Rust

**原文链接**: [https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/](https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/)

生成摘要时出错

---

## 91. Show HN: Seal – Letters and passwords that open for your family after you die

**原文标题**: Show HN: Seal – Letters and passwords that open for your family after you die

**原文链接**: [https://github.com/jasonepage/Seal](https://github.com/jasonepage/Seal)

生成摘要时出错

---

## 92. Lawsuit: Illegal Agreement of Anthropic, OpenAI, SpaceXAI, Google on AI Slowdown

**原文标题**: Lawsuit: Illegal Agreement of Anthropic, OpenAI, SpaceXAI, Google on AI Slowdown

**原文链接**: [https://www.independent.co.uk/news/lawsuit-anthropic-google-openai-lawyers-b3052942.html](https://www.independent.co.uk/news/lawsuit-anthropic-google-openai-lawyers-b3052942.html)

生成摘要时出错

---

## 93. Jemalloc 5.4.0

**原文标题**: Jemalloc 5.4.0

**原文链接**: [https://github.com/jemalloc/jemalloc/releases/tag/5.4.0](https://github.com/jemalloc/jemalloc/releases/tag/5.4.0)

生成摘要时出错

---

## 94. Show HN: Ax-check.com – Can agents use your product?

**原文标题**: Show HN: Ax-check.com – Can agents use your product?

**原文链接**: [https://www.ax-check.com/](https://www.ax-check.com/)

生成摘要时出错

---

## 95. I built the fastest PHP webserver in the world

**原文标题**: I built the fastest PHP webserver in the world

**原文链接**: [https://qbixserver.com](https://qbixserver.com)

生成摘要时出错

---

## 96. When the fractional part of a float fixes your shader

**原文标题**: When the fractional part of a float fixes your shader

**原文链接**: [https://crocidb.com/post/when-the-fractional-part-of-a-float-fixes-your-shader/](https://crocidb.com/post/when-the-fractional-part-of-a-float-fixes-your-shader/)

生成摘要时出错

---

## 97. Apple M6 Pro Achieves the Highest Single-Core CPU Score in Geekbench 7

**原文标题**: Apple M6 Pro Achieves the Highest Single-Core CPU Score in Geekbench 7

**原文链接**: [https://browser.geekbench.com/v7/cpu/389219](https://browser.geekbench.com/v7/cpu/389219)

生成摘要时出错

---

## 98. Flock Offers Employees Buyouts as Customers Flee

**原文标题**: Flock Offers Employees Buyouts as Customers Flee

**原文链接**: [https://www.wired.com/story/flock-is-offering-voluntary-buyouts-to-employees/](https://www.wired.com/story/flock-is-offering-voluntary-buyouts-to-employees/)

生成摘要时出错

---

## 99. Show HN: Jeff – A read-only CLI for semantic code review using Jev

**原文标题**: Show HN: Jeff – A read-only CLI for semantic code review using Jev

**原文链接**: [https://github.com/Alurith/jeff](https://github.com/Alurith/jeff)

生成摘要时出错

---

## 100. Qwen 3.8 Omni Flash

**原文标题**: Qwen 3.8 Omni Flash

**原文链接**: [https://qwen.ai/blog?id=qwen3.8-omni-flash](https://qwen.ai/blog?id=qwen3.8-omni-flash)

生成摘要时出错

---

