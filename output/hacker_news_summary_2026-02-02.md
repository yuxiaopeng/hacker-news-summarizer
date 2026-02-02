# Hacker News 热门文章摘要 (2026-02-02)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Nano-vLLM：类 vLLM 推理引擎的工作原理

**原文标题**: Nano-vLLM: How a vLLM-style inference engine works

**原文链接**: [https://neutree.ai/blog/nano-vllm-part-1](https://neutree.ai/blog/nano-vllm-part-1)

**Nano-vLLM** 是一个极简的生产级推理引擎（约 1,200 行 Python 代码），旨在模仿 vLLM 的架构。本文探讨了其内部工程设计，重点关注系统如何管理从提示词字符串到生成 Token 的转换过程。

该引擎采用了以**调度器（Scheduler）**为核心的**生产者-消费者模式**。当提交提示词时，它会被 Token 化为一个“序列”并存入队列。随后，系统通过批处理这些序列来最大化 GPU 吞吐量，从而在高效能与单个请求的延迟之间取得平衡。

推理过程分为两个阶段：
1. **预填充（Prefill）：** 处理整个输入提示词以构建初始状态。
2. **解码（Decode）：** 逐个生成输出 Token。

为了高效管理 GPU 显存，Nano-vLLM 采用了**分块管理器（Block Manager）**。与将序列视为变长数组的传统方法不同，该系统将其划分为固定大小的“块”。通过使用**哈希技术实现前缀缓存**，引擎可以识别并复用不同请求间共享的块（如通用的系统提示词），从而显著减少冗余计算和内存占用。

**模型运行器（Model Runner）** 负责执行层，支持**张量并行**，利用主从共享内存架构将模型拆分到多个 GPU 上。为了进一步优化性能，它使用 **CUDA Graphs** 来最小化解码阶段启动 GPU 内核的开销。最后，系统通过受温度参数控制的**采样**技术，从模型的输出概率中选出下一个 Token。

最终，Nano-vLLM 证明了现代推理引擎的核心创新——高效调度、基于块的内存管理和硬件级优化——可以在保持高性能的同时，以极简的形式实现。

---

## 2. 地质学家或已解开格林河“逆流”路径之谜

**原文标题**: Geologists may have solved mystery of Green River's 'uphill' route

**原文链接**: [https://phys.org/news/2026-01-geologists-mystery-green-river-uphill.html](https://phys.org/news/2026-01-geologists-mystery-green-river-uphill.html)

犹他州立大学的地质学家们针对一个困扰已久的谜团提出了解决方案：绿河为何是“逆向”切穿犹他州与科罗拉多州境内的尤因塔山脉，而非绕道而行。这一地质异常现象，尤其是河流穿过壮丽的“罗多尔之门”的路径，自约翰·威斯利·鲍威尔时代以来一直令科学家们感到困惑。

历史上，两种理论在争论中占据主导地位：**先成论**（河流在山脉隆起前就已存在）和**叠置论**（河流从上方受侵蚀的沉积层沉降至山脉上）。然而，发表在《美国地质学会学报》（GSA Bulletin）上的最新研究为第三种机制提供了证据：**湖泊溢流**与**河流袭夺**。

研究人员表示，大约600万年前，绿河并未向南流经山脉，而是注入了尤因塔山脉北侧的一个巨大的内流湖。随着气候变化或构造运动导致水位上升，湖水最终漫过了山脉的一个低洼处。这次溢流触发了所谓的“自上而下的整合”过程，剧烈的侵蚀凿出了一段陡峭的峡谷，并实质上“袭夺”了这条河流，使其转向南方汇入科罗拉多河水系。

该团队利用包括宇宙成因核素定年在内的现代测年技术，对沉积物和河成阶地进行了分析。他们的研究结果表明，绿河的整合发生得比此前认为的要晚得多，且过程更为迅速。这一发现有助于完善对科罗拉多河水系形成的宏观认识，并证明了如湖泊溢流等突发事件如何能从根本上永久性地重塑大陆地貌。

---

## 3. 使用 rclone 实现比 rsync 快 4 倍的网络文件同步 (2025)

**原文标题**: 4x faster network file sync with rclone (vs rsync) (2025)

**原文链接**: [https://www.jeffgeerling.com/blog/2025/4x-faster-network-file-sync-rclone-vs-rsync/](https://www.jeffgeerling.com/blog/2025/4x-faster-network-file-sync-rclone-vs-rsync/)

在这篇文章中，科技爱好者 Jeff Geerling 演示了在高速网络文件传输中，将 **rsync** 切换为 **rclone** 如何能实现 4 倍的速度提升。

**问题所在**
Geerling 经常需要将大型视频项目（通常包含 500–1,000 个文件，总计数十 GB）从配备 NVMe 的 NAS 同步到 Thunderbolt 外置 SSD。尽管拥有 10 Gbps 网络连接（带宽可达 1 GB/s）和超高速 SSD，但 `rsync` 的传输速度最高仅为 350 MB/s 左右。瓶颈在于 `rsync` 的单线程串行特性，即一次只能处理一个文件。在一次约 59 GiB 的传输测试中，`rsync` 耗时超过 8 分钟才完成。

**解决方案**
Geerling 转向了 `rclone`。这款工具通常与云存储相关联，但在本地和网络传输中同样高效。通过使用 `--multi-thread-streams` 标志（设置为 32），`rclone` 能够并行执行传输任务。这使得同步过程能够完全跑满 10 Gbps 的网络带宽，速度达到 1 GB/s。

**测试结果**
*   **rsync：** 8 分 17 秒
*   **rclone：** 2 分 15 秒

虽然这两款工具在扫描目录树以检查元数据更改方面所花的时间相近（约 18 秒），但在实际的数据传输阶段，`rclone` 显著领先。Geerling 得出结论，对于拥有高速基础设施的用户，`rclone` 是比 `rsync` 更优的选择，因为它克服了串行文件处理的限制。

---

## 4. Todd C. Miller —— 担任 sudo 维护者逾 30 年

**原文标题**: Todd C. Miller – sudo Maintainer for over 30 years

**原文链接**: [https://www.millert.dev/](https://www.millert.dev/)

Todd C. Miller 是 **sudo** 工具的长期维护者，担任此职已超过 30 年。他目前正在寻求个人或组织赞助，以资助该软件的持续维护与开发。

除了在 sudo 方面的工作外，Miller 还是 **OpenBSD** 的贡献者，并曾对其他开源项目做出过重大贡献，其中最著名的是 **ISC cron**。本页面提供了其简要的专业概览，并呼吁资金支持，以确保 sudo 项目的未来。

---

## 5. 我使用 OxCaml 开发的快速零分配 Web 服务器

**原文标题**: My fast zero-allocation webserver using OxCaml

**原文链接**: [https://anil.recoil.org/notes/oxcaml-httpz](https://anil.recoil.org/notes/oxcaml-httpz)

在本文中，作者介绍了 **httpz**，这是一个使用 **OxCaml** 构建的高性能 HTTP/1.1 Web 服务器。OxCaml 是由 Jane Street 开发的一套 OCaml 语言扩展。该项目旨在通过在调用栈上处理 HTTP 连接的整个生命周期来实现“零分配”，从而在稳态下消除垃圾回收（GC）活动。

`httpz` 利用的 OxCaml 核心特性包括：

*   **非装箱类型与记录：** 通过使用非装箱整数（`int16#`）和记录（`#{}`），作者将缓冲区的偏移量和长度直接存储在寄存器或栈中。这避免了传统 OCaml 内存表示中记录需要堆分配“装箱（boxes）”的问题。
*   **局部分配：** 通过使用 `local_` 和 `exclave_` 关键字，作者确保了诸如标头列表之类的数据不会逃逸出函数作用域。这使得原本需要分配在小堆（minor heap）上的复杂结构可以进行栈分配。
*   **栈分配的可变性：** `let mutable` 语法允许在循环中使用局部变量，而无需堆分配的 `ref` 单元，从而进一步减轻了内存压力。

作者通过对比汇编代码展示了性能增益：标准 OCaml 执行堆指针操作和 GC 限制检查，而 OxCaml 版本则使用直接的寄存器算术和符号扩展指令。

虽然 `httpz` 目前专注于配备 32KB 缓冲区的 HTTP/1.1，但作者强调了 OxCaml 的“直接风格”优于“回调汤（callback soup）”的益处。不过，文中也指出了一些当前的局限性，包括变动中的工具链生态（例如对 `odoc` 和 `ocamlformat` 仍在演进中的支持），以及在深度集成这些扩展后，维持与上游 OCaml 兼容性的难度。

---

## 6. 破解一款有着40年历史的加密狗

**原文标题**: Defeating a 40-year-old copy protection dongle

**原文链接**: [https://dmitrybrant.com/2026/02/01/defeating-a-40-year-old-copy-protection-dongle](https://dmitrybrant.com/2026/02/01/defeating-a-40-year-old-copy-protection-dongle)

本文记录了一个“软件考古”项目，旨在绕过一套拥有40年历史的硬件复制保护系统。作者的任务是将一家会计师事务所的遗留数据从运行在 Windows 98 系统上、由 RPG II（报表程序生成器）构建的软件中迁移出来。该软件必须配合“Software Security Inc.”生产的物理并口加密狗才能运行，这给在模拟器中运行系统带来了阻碍。

通过使用 Reko 反汇编器分析 Software West Inc. 的 RPG II 编译器，作者发现该编译器不仅自身需要加密狗，还会将相同的保护逻辑注入其生成的每个可执行文件中。调查确定了一段 0x90 字节的代码段，该段代码利用 `in` 和 `out` 指令与并口进行通信。

技术分析显示，该例程是自包含的，并在 BX 寄存器中返回一个固定的“成功”值。虽然高字节 (BH) 已硬编码为 `76h`，但低字节 (BL) 仍然未知。通过在 DOSBox 中运行暴力破解脚本，作者测试了 BL 的所有 256 种可能组合，最终确定该特定值为 `7606h`。

作者在例程开头应用了一个简单的四字节补丁（`MOV BX, 7606h; RETF`），成功攻克了该保护机制。由于编译器会将自身的逻辑复制到新程序中，因此打过补丁的编译器现在可以生成“已解锁”的可执行文件。项目最后，作者表示打算在清除所有敏感数据后，将这款罕见的 RPG II 编译器作为历史文物予以保存。

---

## 7. Valanza – 我的 Unix 体重追踪与分析方式

**原文标题**: Valanza – my Unix way for weight tracking and anlysis

**原文链接**: [https://github.com/paolomarrone/valanza](https://github.com/paolomarrone/valanza)

**Valanza** is an experimental weight tracking and analysis tool designed by Paolo Marrone. It follows the "Unix philosophy" by utilizing a collection of small, specialized programs that communicate through pipes rather than relying on a single, monolithic spreadsheet.

The project was born out of a desire to separate data from logic. By avoiding "spreadsheet hell," the author can use the most appropriate programming language for each specific computational task. The tool integrates several technologies, including **Bash/rc, R, AWK, and gnuplot**.

**Key Components and Workflow:**
*   **Data Cleaning:** An R script (`interpolate_lin.R`) fills gaps in weight data using linear interpolation.
*   **Signal Processing:** Specialized AWK scripts calculate moving averages (`mov_avg.awk`) and apply first-order low-pass filters (`lp1.awk`).
*   **Visualization:** Data is visualized using gnuplot.
*   **Architecture:** The system leverages RAM-based named pipes and process substitution to split data streams into parallel filters before recombining them for final output.

Currently intended for personal use and experimentation, Valanza is licensed under the MIT License. It serves as a proof-of-concept for a modular, command-line-driven alternative to traditional calculation software.

---

## 8. Claude Code is suddenly everywhere inside Microsoft

**原文标题**: Claude Code is suddenly everywhere inside Microsoft

**原文链接**: [https://www.theverge.com/tech/865689/microsoft-claude-code-anthropic-partnership-notepad](https://www.theverge.com/tech/865689/microsoft-claude-code-anthropic-partnership-notepad)

生成摘要时出错

---

## 9. Hypergrowth isn’t always easy

**原文标题**: Hypergrowth isn’t always easy

**原文链接**: [https://tailscale.com/blog/hypergrowth-isnt-always-easy](https://tailscale.com/blog/hypergrowth-isnt-always-easy)

生成摘要时出错

---

## 10. Solvingn the Santa Claus concurrency puzzle with a model checker

**原文标题**: Solvingn the Santa Claus concurrency puzzle with a model checker

**原文链接**: [https://wyounas.github.io/puzzles/concurrency/2026/01/10/how-to-help-santa-claus-concurrently/](https://wyounas.github.io/puzzles/concurrency/2026/01/10/how-to-help-santa-claus-concurrently/)

生成摘要时出错

---

## 11. Termux

**原文标题**: Termux

**原文链接**: [https://github.com/termux/termux-app](https://github.com/termux/termux-app)

生成摘要时出错

---

## 12. Show HN: Stelvio – Ship Python to AWS

**原文标题**: Show HN: Stelvio – Ship Python to AWS

**原文链接**: [https://stelvio.dev/](https://stelvio.dev/)

生成摘要时出错

---

## 13. My iPhone 16 Pro Max produces garbage output when running MLX LLMs

**原文标题**: My iPhone 16 Pro Max produces garbage output when running MLX LLMs

**原文链接**: [https://journal.rafaelcosta.me/my-thousand-dollar-iphone-cant-do-math/](https://journal.rafaelcosta.me/my-thousand-dollar-iphone-cant-do-math/)

生成摘要时出错

---

## 14. They lied to you. Building software is hard

**原文标题**: They lied to you. Building software is hard

**原文链接**: [https://blog.nordcraft.com/they-lied-to-you-building-software-is-really-hard](https://blog.nordcraft.com/they-lied-to-you-building-software-is-really-hard)

生成摘要时出错

---

## 15. Apple's MacBook Pro DFU port documentation is wrong

**原文标题**: Apple's MacBook Pro DFU port documentation is wrong

**原文链接**: [https://lapcatsoftware.com/articles/2026/2/1.html](https://lapcatsoftware.com/articles/2026/2/1.html)

生成摘要时出错

---

## 16. IsoCoaster – Theme Park Builder

**原文标题**: IsoCoaster – Theme Park Builder

**原文链接**: [https://iso-coaster.com/](https://iso-coaster.com/)

生成摘要时出错

---

## 17. Library of Juggling

**原文标题**: Library of Juggling

**原文链接**: [https://libraryofjuggling.com/](https://libraryofjuggling.com/)

生成摘要时出错

---

## 18. Show HN: Wikipedia as a doomscrollable social media feed

**原文标题**: Show HN: Wikipedia as a doomscrollable social media feed

**原文链接**: [https://xikipedia.org](https://xikipedia.org)

生成摘要时出错

---

## 19. Ratchets in software development (2021)

**原文标题**: Ratchets in software development (2021)

**原文链接**: [https://qntm.org/ratchet](https://qntm.org/ratchet)

生成摘要时出错

---

## 20. Show HN: NanoClaw – “Clawdbot” in 500 lines of TS with Apple container isolation

**原文标题**: Show HN: NanoClaw – “Clawdbot” in 500 lines of TS with Apple container isolation

**原文链接**: [https://github.com/gavrielc/nanoclaw](https://github.com/gavrielc/nanoclaw)

生成摘要时出错

---

## 21. Best Gas Masks

**原文标题**: Best Gas Masks

**原文链接**: [https://www.theverge.com/policy/868571/best-gas-masks](https://www.theverge.com/policy/868571/best-gas-masks)

生成摘要时出错

---

## 22. Ian's Shoelace Site

**原文标题**: Ian's Shoelace Site

**原文链接**: [https://www.fieggen.com/shoelace/](https://www.fieggen.com/shoelace/)

生成摘要时出错

---

## 23. Show HN: Apate API mocking/prototyping server and Rust unit test library

**原文标题**: Show HN: Apate API mocking/prototyping server and Rust unit test library

**原文链接**: [https://github.com/rustrum/apate](https://github.com/rustrum/apate)

生成摘要时出错

---

## 24. Adventure Game Studio: OSS software for creating adventure games

**原文标题**: Adventure Game Studio: OSS software for creating adventure games

**原文链接**: [https://www.adventuregamestudio.co.uk/](https://www.adventuregamestudio.co.uk/)

生成摘要时出错

---

## 25. Apple I Advertisement (1976)

**原文标题**: Apple I Advertisement (1976)

**原文链接**: [http://apple1.chez.com/Apple1project/Gallery/Gallery.htm](http://apple1.chez.com/Apple1project/Gallery/Gallery.htm)

生成摘要时出错

---

## 26. Swift in the Browser with ElementaryUI (Swift FOSDEM 2026 Talk) [video]

**原文标题**: Swift in the Browser with ElementaryUI (Swift FOSDEM 2026 Talk) [video]

**原文链接**: [https://www.youtube.com/watch?v=OmQ881sOTIc](https://www.youtube.com/watch?v=OmQ881sOTIc)

生成摘要时出错

---

## 27. Contracts in Nix

**原文标题**: Contracts in Nix

**原文链接**: [https://sraka.xyz/posts/contracts.html](https://sraka.xyz/posts/contracts.html)

生成摘要时出错

---

## 28. Board Games in Ancient Fiction: Egypt, Iran, Greece

**原文标题**: Board Games in Ancient Fiction: Egypt, Iran, Greece

**原文链接**: [https://reference-global.com/article/10.2478/bgs-2022-0016](https://reference-global.com/article/10.2478/bgs-2022-0016)

生成摘要时出错

---

## 29. Actors: A Model of Concurrent Computation [pdf] (1985)

**原文标题**: Actors: A Model of Concurrent Computation [pdf] (1985)

**原文链接**: [https://apps.dtic.mil/sti/tr/pdf/ADA157917.pdf](https://apps.dtic.mil/sti/tr/pdf/ADA157917.pdf)

生成摘要时出错

---

## 30. Rev up the viral factories

**原文标题**: Rev up the viral factories

**原文链接**: [https://www.science.org/content/blog-post/rev-viral-factories](https://www.science.org/content/blog-post/rev-viral-factories)

生成摘要时出错

---

## 31. EU launches government satcom program in sovereignty push

**原文标题**: EU launches government satcom program in sovereignty push

**原文链接**: [https://spacenews.com/eu-launches-government-satcom-program-in-sovereignty-push/](https://spacenews.com/eu-launches-government-satcom-program-in-sovereignty-push/)

生成摘要时出错

---

## 32. AI controls is coming to Firefox

**原文标题**: AI controls is coming to Firefox

**原文链接**: [https://blog.mozilla.org/en/firefox/ai-controls/](https://blog.mozilla.org/en/firefox/ai-controls/)

生成摘要时出错

---

## 33. Building Your Own Efficient uint128 in C++

**原文标题**: Building Your Own Efficient uint128 in C++

**原文链接**: [https://solidean.com/blog/2026/building-your-own-u128/](https://solidean.com/blog/2026/building-your-own-u128/)

生成摘要时出错

---

## 34. Waymo Seeking About $16B Near $110B Valuation

**原文标题**: Waymo Seeking About $16B Near $110B Valuation

**原文链接**: [https://www.bloomberg.com/news/articles/2026-01-31/waymo-seeking-about-16-billion-near-110-billion-valuation](https://www.bloomberg.com/news/articles/2026-01-31/waymo-seeking-about-16-billion-near-110-billion-valuation)

生成摘要时出错

---

## 35. Clearspace (YC W23) Is Hiring an Applied Researcher (ML)

**原文标题**: Clearspace (YC W23) Is Hiring an Applied Researcher (ML)

**原文链接**: [https://www.ycombinator.com/companies/clearspace/jobs/GOWiDwp-research-engineer-at-clearspace](https://www.ycombinator.com/companies/clearspace/jobs/GOWiDwp-research-engineer-at-clearspace)

生成摘要时出错

---

## 36. Leaked Chats Expose the Daily Life of a Scam Compound's Enslaved Workforce

**原文标题**: Leaked Chats Expose the Daily Life of a Scam Compound's Enslaved Workforce

**原文链接**: [https://www.wired.com/story/the-red-bull-leaks/](https://www.wired.com/story/the-red-bull-leaks/)

生成摘要时出错

---

## 37. Efficient String Compression for Modern Database Systems

**原文标题**: Efficient String Compression for Modern Database Systems

**原文链接**: [https://cedardb.com/blog/string_compression/](https://cedardb.com/blog/string_compression/)

生成摘要时出错

---

## 38. MicroPythonOS graphical operating system delivers Android-like user experience

**原文标题**: MicroPythonOS graphical operating system delivers Android-like user experience

**原文链接**: [https://www.cnx-software.com/2026/01/29/micropythonos-graphical-operating-system-delivers-android-like-user-experience-on-microcontrollers/](https://www.cnx-software.com/2026/01/29/micropythonos-graphical-operating-system-delivers-android-like-user-experience-on-microcontrollers/)

生成摘要时出错

---

## 39. Two kinds of AI users are emerging

**原文标题**: Two kinds of AI users are emerging

**原文链接**: [https://martinalderson.com/posts/two-kinds-of-ai-users-are-emerging/](https://martinalderson.com/posts/two-kinds-of-ai-users-are-emerging/)

生成摘要时出错

---

## 40. MaliciousCorgi: AI Extensions send your code to China

**原文标题**: MaliciousCorgi: AI Extensions send your code to China

**原文链接**: [https://www.koi.ai/blog/maliciouscorgi-the-cute-looking-ai-extensions-leaking-code-from-1-5-million-developers](https://www.koi.ai/blog/maliciouscorgi-the-cute-looking-ai-extensions-leaking-code-from-1-5-million-developers)

生成摘要时出错

---

## 41. FOSDEM 2026 – Open-Source Conference in Brussels – Day#1 Recap

**原文标题**: FOSDEM 2026 – Open-Source Conference in Brussels – Day#1 Recap

**原文链接**: [https://gyptazy.com/blog/fosdem-2026-opensource-conference-brussels/](https://gyptazy.com/blog/fosdem-2026-opensource-conference-brussels/)

生成摘要时出错

---

## 42. Netbird – Open Source Zero Trust Networking

**原文标题**: Netbird – Open Source Zero Trust Networking

**原文链接**: [https://netbird.io/](https://netbird.io/)

生成摘要时出错

---

## 43. Microsoft is walking back Windows 11's AI overload

**原文标题**: Microsoft is walking back Windows 11's AI overload

**原文链接**: [https://www.windowscentral.com/microsoft/windows-11/microsoft-is-reevaluating-its-ai-efforts-on-windows-11-plans-to-reduce-copilot-integrations-and-evolve-recall](https://www.windowscentral.com/microsoft/windows-11/microsoft-is-reevaluating-its-ai-efforts-on-windows-11-plans-to-reduce-copilot-integrations-and-evolve-recall)

生成摘要时出错

---

## 44. A Crisis comes to Wordle: Reusing old words

**原文标题**: A Crisis comes to Wordle: Reusing old words

**原文链接**: [https://forkingmad.blog/wordle-crisis/](https://forkingmad.blog/wordle-crisis/)

生成摘要时出错

---

## 45. Greenwashing creates 'false stability' for companies

**原文标题**: Greenwashing creates 'false stability' for companies

**原文链接**: [https://phys.org/news/2026-01-greenwashing-false-stability-companies.html](https://phys.org/news/2026-01-greenwashing-false-stability-companies.html)

生成摘要时出错

---

## 46. Founding is a snowball

**原文标题**: Founding is a snowball

**原文链接**: [https://blog.bawolf.com/p/founding-is-a-snowball](https://blog.bawolf.com/p/founding-is-a-snowball)

生成摘要时出错

---

## 47. Amiga Unix (Amix)

**原文标题**: Amiga Unix (Amix)

**原文链接**: [https://www.amigaunix.com/doku.php/home](https://www.amigaunix.com/doku.php/home)

生成摘要时出错

---

## 48. Towards a science of scaling agent systems: When and why agent systems work

**原文标题**: Towards a science of scaling agent systems: When and why agent systems work

**原文链接**: [https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)

生成摘要时出错

---

## 49. Time Machine-style Backups with rsync (2018)

**原文标题**: Time Machine-style Backups with rsync (2018)

**原文链接**: [https://samuelhewitt.com/blog/2018-06-05-time-machine-style-backups-with-rsync](https://samuelhewitt.com/blog/2018-06-05-time-machine-style-backups-with-rsync)

生成摘要时出错

---

## 50. Treasures found on HS2 route stored in secret warehouse

**原文标题**: Treasures found on HS2 route stored in secret warehouse

**原文链接**: [https://www.bbc.com/news/articles/c93v21q5xdvo](https://www.bbc.com/news/articles/c93v21q5xdvo)

生成摘要时出错

---

## 51. Stop Using Pseudo-Types

**原文标题**: Stop Using Pseudo-Types

**原文链接**: [https://f2r.github.io/en/stop-using-pseudo-types.html](https://f2r.github.io/en/stop-using-pseudo-types.html)

生成摘要时出错

---

## 52. Jack Kerouac's 37 metre-long, first draft scroll of On the Road to be auctioned

**原文标题**: Jack Kerouac's 37 metre-long, first draft scroll of On the Road to be auctioned

**原文链接**: [https://www.theguardian.com/books/2026/jan/30/jack-kerouac-on-the-road-first-draft-scroll-to-be-auctioned](https://www.theguardian.com/books/2026/jan/30/jack-kerouac-on-the-road-first-draft-scroll-to-be-auctioned)

生成摘要时出错

---

## 53. New satellite view of Tibet's tectonic clash

**原文标题**: New satellite view of Tibet's tectonic clash

**原文链接**: [https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-1/New_satellite_view_of_Tibet_s_tectonic_clash](https://www.esa.int/Applications/Observing_the_Earth/Copernicus/Sentinel-1/New_satellite_view_of_Tibet_s_tectonic_clash)

生成摘要时出错

---

## 54. Are we dismissing AI spend before the 6x lands? (2025)

**原文标题**: Are we dismissing AI spend before the 6x lands? (2025)

**原文链接**: [https://martinalderson.com/posts/are-we-dismissing-ai-spend-before-the-6x-lands/](https://martinalderson.com/posts/are-we-dismissing-ai-spend-before-the-6x-lands/)

生成摘要时出错

---

## 55. Building a Telegram Bot with Cloudflare Workers, Durable Objects and Grammy

**原文标题**: Building a Telegram Bot with Cloudflare Workers, Durable Objects and Grammy

**原文链接**: [https://flashblaze.xyz/posts/cloudflare-workers-durable-objects-telegram-bot/](https://flashblaze.xyz/posts/cloudflare-workers-durable-objects-telegram-bot/)

生成摘要时出错

---

## 56. Teaching my neighbor to keep the volume down

**原文标题**: Teaching my neighbor to keep the volume down

**原文链接**: [https://idiallo.com/blog/teaching-my-neighbor-to-keep-the-volume-down](https://idiallo.com/blog/teaching-my-neighbor-to-keep-the-volume-down)

生成摘要时出错

---

## 57. Teaching my neighbor to keep the volume down

**原文标题**: Teaching my neighbor to keep the volume down

**原文链接**: [https://idiallo.com/blog/teaching-my-neighbor-to-keep-the-volume-down](https://idiallo.com/blog/teaching-my-neighbor-to-keep-the-volume-down)

生成摘要时出错

---

## 58. Soldering Prototypes with Enamel Magnet Wire (2020)

**原文标题**: Soldering Prototypes with Enamel Magnet Wire (2020)

**原文链接**: [https://tomverbeure.github.io/2020/02/22/In-The-Lab-Magnet-Wire-Soldering.html](https://tomverbeure.github.io/2020/02/22/In-The-Lab-Magnet-Wire-Soldering.html)

生成摘要时出错

---

## 59. Typechecking is undecidable when 'type' is a type (1989) [pdf]

**原文标题**: Typechecking is undecidable when 'type' is a type (1989) [pdf]

**原文链接**: [https://dspace.mit.edu/bitstream/handle/1721.1/149366/MIT-LCS-TR-458.pdf?sequence=6](https://dspace.mit.edu/bitstream/handle/1721.1/149366/MIT-LCS-TR-458.pdf?sequence=6)

生成摘要时出错

---

## 60. Message from Pope Leo XIV on the 60th World Day of Social Communications

**原文标题**: Message from Pope Leo XIV on the 60th World Day of Social Communications

**原文链接**: [https://www.vatican.va/content/leo-xiv/en/messages/communications/documents/20260124-messaggio-comunicazioni-sociali.html](https://www.vatican.va/content/leo-xiv/en/messages/communications/documents/20260124-messaggio-comunicazioni-sociali.html)

生成摘要时出错

---

## 61. Mobile carriers can get your GPS location

**原文标题**: Mobile carriers can get your GPS location

**原文链接**: [https://an.dywa.ng/carrier-gnss.html](https://an.dywa.ng/carrier-gnss.html)

生成摘要时出错

---

## 62. A web server on a single floppy disk

**原文标题**: A web server on a single floppy disk

**原文链接**: [http://floppy.ddns.net/](http://floppy.ddns.net/)

生成摘要时出错

---

## 63. English professors double down on requiring printed copies of readings

**原文标题**: English professors double down on requiring printed copies of readings

**原文链接**: [https://yaledailynews.com/articles/english-professors-double-down-on-requiring-printed-copies-of-readings](https://yaledailynews.com/articles/english-professors-double-down-on-requiring-printed-copies-of-readings)

生成摘要时出错

---

## 64. Show HN: Sklad – Secure, offline-first snippet manager (Rust, Tauri v2)

**原文标题**: Show HN: Sklad – Secure, offline-first snippet manager (Rust, Tauri v2)

**原文链接**: [https://github.com/Rench321/sklad](https://github.com/Rench321/sklad)

生成摘要时出错

---

## 65. What Most People Miss About Getting Promoted

**原文标题**: What Most People Miss About Getting Promoted

**原文链接**: [https://news.theuncommonexecutive.com/p/what-most-people-miss-about-getting](https://news.theuncommonexecutive.com/p/what-most-people-miss-about-getting)

生成摘要时出错

---

## 66. Troublemaker: The fierce, unruly life of Jessica Mitford

**原文标题**: Troublemaker: The fierce, unruly life of Jessica Mitford

**原文链接**: [https://www.lrb.co.uk/the-paper/v48/n02/rosemary-hill/one-of-the-worst-things](https://www.lrb.co.uk/the-paper/v48/n02/rosemary-hill/one-of-the-worst-things)

生成摘要时出错

---

## 67. What I learned building an opinionated and minimal coding agent

**原文标题**: What I learned building an opinionated and minimal coding agent

**原文链接**: [https://mariozechner.at/posts/2025-11-30-pi-coding-agent/](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/)

生成摘要时出错

---

## 68. Reliable 25 Gigabit Ethernet via Thunderbolt

**原文标题**: Reliable 25 Gigabit Ethernet via Thunderbolt

**原文链接**: [https://kohlschuetter.github.io/blog/posts/2026/01/27/tb25/](https://kohlschuetter.github.io/blog/posts/2026/01/27/tb25/)

生成摘要时出错

---

## 69. Silver plunges 30% in worst day since 1980, gold tumbles

**原文标题**: Silver plunges 30% in worst day since 1980, gold tumbles

**原文链接**: [https://www.cnbc.com/2026/01/30/silver-gold-fall-price-usd-dollar-fed-warsh-chair-trump-metals.html](https://www.cnbc.com/2026/01/30/silver-gold-fall-price-usd-dollar-fed-warsh-chair-trump-metals.html)

生成摘要时出错

---

## 70. MRI scans show exercise can make the brain look younger

**原文标题**: MRI scans show exercise can make the brain look younger

**原文链接**: [https://www.sciencedaily.com/releases/2026/01/260121034130.htm](https://www.sciencedaily.com/releases/2026/01/260121034130.htm)

生成摘要时出错

---

## 71. Nintendo DS code editor and scriptable game engine

**原文标题**: Nintendo DS code editor and scriptable game engine

**原文链接**: [https://crl.io/ds-game-engine/](https://crl.io/ds-game-engine/)

生成摘要时出错

---

## 72. Autonomous cars, drones cheerfully obey prompt injection by road sign

**原文标题**: Autonomous cars, drones cheerfully obey prompt injection by road sign

**原文链接**: [https://www.theregister.com/2026/01/30/road_sign_hijack_ai/](https://www.theregister.com/2026/01/30/road_sign_hijack_ai/)

生成摘要时出错

---

## 73. Notepad++ hijacked by state-sponsored actors

**原文标题**: Notepad++ hijacked by state-sponsored actors

**原文链接**: [https://notepad-plus-plus.org/news/hijacked-incident-info-update/](https://notepad-plus-plus.org/news/hijacked-incident-info-update/)

生成摘要时出错

---

## 74. Allowlisting some Bash commands is often the same as allowlisting all

**原文标题**: Allowlisting some Bash commands is often the same as allowlisting all

**原文链接**: [https://www.joinformal.com/blog/allowlisting-some-bash-commands-is-often-the-same-as-allowlisting-all-with-claude-code/](https://www.joinformal.com/blog/allowlisting-some-bash-commands-is-often-the-same-as-allowlisting-all-with-claude-code/)

生成摘要时出错

---

## 75. History and Timeline of the Proco Rat Pedal (2021)

**原文标题**: History and Timeline of the Proco Rat Pedal (2021)

**原文链接**: [https://web.archive.org/web/20211030011207/https://thejhsshow.com/articles/history-and-timeline-of-the-proco-rat-pedal](https://web.archive.org/web/20211030011207/https://thejhsshow.com/articles/history-and-timeline-of-the-proco-rat-pedal)

生成摘要时出错

---

## 76. Finland looks to introduce Australia-style ban on social media

**原文标题**: Finland looks to introduce Australia-style ban on social media

**原文链接**: [https://yle.fi/a/74-20207494](https://yle.fi/a/74-20207494)

生成摘要时出错

---

## 77. Automatic Programming

**原文标题**: Automatic Programming

**原文链接**: [https://antirez.com/news/159](https://antirez.com/news/159)

生成摘要时出错

---

## 78. Apple Platform Security (Jan 2026) [pdf]

**原文标题**: Apple Platform Security (Jan 2026) [pdf]

**原文链接**: [https://help.apple.com/pdf/security/en_US/apple-platform-security-guide.pdf](https://help.apple.com/pdf/security/en_US/apple-platform-security-guide.pdf)

生成摘要时出错

---

## 79. List animals until failure

**原文标题**: List animals until failure

**原文链接**: [https://rose.systems/animalist/](https://rose.systems/animalist/)

生成摘要时出错

---

## 80. Nonograms: a practical guide with interactive examples

**原文标题**: Nonograms: a practical guide with interactive examples

**原文链接**: [https://lab174.com/blog/202601-nonograms/](https://lab174.com/blog/202601-nonograms/)

生成摘要时出错

---

## 81. Giving up upstream-ing my patches and feel free to pick them up

**原文标题**: Giving up upstream-ing my patches and feel free to pick them up

**原文链接**: [https://mail.openjdk.org/pipermail/hotspot-dev/2026-January/118080.html](https://mail.openjdk.org/pipermail/hotspot-dev/2026-January/118080.html)

生成摘要时出错

---

## 82. FOSDEM: Open-Source Is Political – Resist Organize Protect

**原文标题**: FOSDEM: Open-Source Is Political – Resist Organize Protect

**原文链接**: [https://ftp.belnet.be/mirror/FOSDEM/video/2026/janson/SFKNTZ-welcome_to_fosdem_2026.mp4](https://ftp.belnet.be/mirror/FOSDEM/video/2026/janson/SFKNTZ-welcome_to_fosdem_2026.mp4)

生成摘要时出错

---

## 83. Show HN: Sandbox Agent SDK – unified API for automating coding agents

**原文标题**: Show HN: Sandbox Agent SDK – unified API for automating coding agents

**原文链接**: [https://github.com/rivet-dev/sandbox-agent](https://github.com/rivet-dev/sandbox-agent)

生成摘要时出错

---

## 84. China Bans Hidden Car Door Handles

**原文标题**: China Bans Hidden Car Door Handles

**原文链接**: [https://www.bloomberg.com/news/articles/2026-02-02/china-bans-hidden-car-door-handles-in-world-first-safety-policy](https://www.bloomberg.com/news/articles/2026-02-02/china-bans-hidden-car-door-handles-in-world-first-safety-policy)

生成摘要时出错

---

## 85. The Book of PF, 4th edition

**原文标题**: The Book of PF, 4th edition

**原文链接**: [https://nostarch.com/book-of-pf-4th-edition](https://nostarch.com/book-of-pf-4th-edition)

生成摘要时出错

---

## 86. Anciente map of Fairyland. Places from nursery rhymes, fairy tales etc.

**原文标题**: Anciente map of Fairyland. Places from nursery rhymes, fairy tales etc.

**原文链接**: [https://collections.leventhalmap.org/search/commonwealth:3f463773q](https://collections.leventhalmap.org/search/commonwealth:3f463773q)

生成摘要时出错

---

## 87. Coffee as a staining agent substitute in electron microscopy

**原文标题**: Coffee as a staining agent substitute in electron microscopy

**原文链接**: [https://phys.org/news/2026-01-coffee-agent-substitute-electron-microscopy.html](https://phys.org/news/2026-01-coffee-agent-substitute-electron-microscopy.html)

生成摘要时出错

---

## 88. VisualJJ – Jujutsu in Visual Studio Code

**原文标题**: VisualJJ – Jujutsu in Visual Studio Code

**原文链接**: [https://www.visualjj.com/](https://www.visualjj.com/)

生成摘要时出错

---

## 89. In praise of –dry-run

**原文标题**: In praise of –dry-run

**原文链接**: [https://henrikwarne.com/2026/01/31/in-praise-of-dry-run/](https://henrikwarne.com/2026/01/31/in-praise-of-dry-run/)

生成摘要时出错

---

## 90. Greenland tensions harden Europe's push for energy independence

**原文标题**: Greenland tensions harden Europe's push for energy independence

**原文链接**: [https://www.ft.com/content/e9c90df9-ee03-4c51-bbd3-dad45e212961](https://www.ft.com/content/e9c90df9-ee03-4c51-bbd3-dad45e212961)

生成摘要时出错

---

## 91. Show HN: Minimal – Open-Source Community driven Hardened Container Images

**原文标题**: Show HN: Minimal – Open-Source Community driven Hardened Container Images

**原文链接**: [https://github.com/rtvkiz/minimal](https://github.com/rtvkiz/minimal)

生成摘要时出错

---

## 92. Show HN: Voiden – an offline, Git-native API tool built around Markdown

**原文标题**: Show HN: Voiden – an offline, Git-native API tool built around Markdown

**原文链接**: [https://github.com/VoidenHQ/voiden](https://github.com/VoidenHQ/voiden)

生成摘要时出错

---

## 93. A novelist who took on the Italian mafia and lived

**原文标题**: A novelist who took on the Italian mafia and lived

**原文链接**: [https://www.thetimes.com/culture/books/article/sicilian-man-leonardo-sciascia-rise-mafia-struggle-italy-soul-caroline-moorehead-review-lbsbd2p5w](https://www.thetimes.com/culture/books/article/sicilian-man-leonardo-sciascia-rise-mafia-struggle-italy-soul-caroline-moorehead-review-lbsbd2p5w)

生成摘要时出错

---

## 94. 1-Click RCE to steal your Moltbot data and keys

**原文标题**: 1-Click RCE to steal your Moltbot data and keys

**原文链接**: [https://depthfirst.com/post/1-click-rce-to-steal-your-moltbot-data-and-keys](https://depthfirst.com/post/1-click-rce-to-steal-your-moltbot-data-and-keys)

生成摘要时出错

---

## 95. We asked 15,000 European devs about jobs, salaries, and AI [pdf]

**原文标题**: We asked 15,000 European devs about jobs, salaries, and AI [pdf]

**原文链接**: [https://static.germantechjobs.de/market-reports/European-Transparent-IT-Job-Market-Report-2025.pdf](https://static.germantechjobs.de/market-reports/European-Transparent-IT-Job-Market-Report-2025.pdf)

生成摘要时出错

---

## 96. Peloton lays off 11 percent of staff just after launching its AI hardware

**原文标题**: Peloton lays off 11 percent of staff just after launching its AI hardware

**原文链接**: [https://www.theverge.com/gadgets/871422/peloton-layoffs-cost-cutting-2026](https://www.theverge.com/gadgets/871422/peloton-layoffs-cost-cutting-2026)

生成摘要时出错

---

## 97. The history of C# and TypeScript with Anders Hejlsberg [video]

**原文标题**: The history of C# and TypeScript with Anders Hejlsberg [video]

**原文链接**: [https://www.youtube.com/watch?v=uMqx8NNT4xY](https://www.youtube.com/watch?v=uMqx8NNT4xY)

生成摘要时出错

---

## 98. Noctia: A sleek and minimal desktop shell thoughtfully crafted for Wayland

**原文标题**: Noctia: A sleek and minimal desktop shell thoughtfully crafted for Wayland

**原文链接**: [https://github.com/noctalia-dev/noctalia-shell](https://github.com/noctalia-dev/noctalia-shell)

生成摘要时出错

---

## 99. Show HN: Moltbook – A social network for moltbots (clawdbots) to hang out

**原文标题**: Show HN: Moltbook – A social network for moltbots (clawdbots) to hang out

**原文链接**: [https://www.moltbook.com/](https://www.moltbook.com/)

生成摘要时出错

---

## 100. "Solving" Wordle from Shared Scores at 100%* Accuracy

**原文标题**: "Solving" Wordle from Shared Scores at 100%* Accuracy

**原文链接**: [https://marcoshuerta.com/posts/wordle_bluesky/](https://marcoshuerta.com/posts/wordle_bluesky/)

生成摘要时出错

---

