# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-02.md)

*最后自动更新时间: 2026-02-02 18:15:40*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 2 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 3 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 4 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 5 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 6 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 7 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 8 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 9 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 10 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 11 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 12 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 13 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 14 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 15 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 16 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 17 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 18 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 19 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 20 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 21 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 22 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 23 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 24 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 25 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 26 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 27 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 28 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 29 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 30 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 31 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 32 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 33 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 34 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 35 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 36 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 37 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 38 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 39 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 40 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 41 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 42 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 43 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 44 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 45 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 46 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 47 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 48 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 49 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 50 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 51 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 52 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 53 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 54 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 55 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 56 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 57 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 58 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 59 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 60 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 61 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 62 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 63 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 64 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 65 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 66 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 67 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 68 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 69 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 70 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 71 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 72 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 73 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 74 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 75 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 76 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 77 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 78 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 79 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 80 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 81 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 82 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 83 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 84 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 85 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 86 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 87 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 88 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 89 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 90 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 91 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 92 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 93 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 94 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 95 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 96 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 97 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 98 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 99 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 100 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 101 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 102 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 103 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 104 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 105 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 106 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 107 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 108 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 109 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 110 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 111 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 112 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 113 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 114 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 115 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 116 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 117 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 118 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 119 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 120 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 121 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 122 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 123 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 124 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 125 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 126 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 127 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 128 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 129 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 130 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 131 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 132 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 133 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 134 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 135 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 136 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 137 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 138 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 139 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 140 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 141 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 142 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 143 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 144 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 145 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 146 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 147 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 148 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 149 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 150 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 151 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 152 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 153 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 154 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 155 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 156 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 157 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 158 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 159 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 160 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 161 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 162 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 163 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 164 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 165 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 166 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 167 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 168 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 169 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 170 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 171 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 172 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 173 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 174 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 175 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 176 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 177 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 178 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 179 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 180 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 181 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 182 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 183 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 184 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 185 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 186 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 187 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 188 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 189 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 190 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 191 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 192 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 193 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 194 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 195 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 196 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 197 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 198 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 199 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 200 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 201 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 202 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 203 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 204 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 205 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 206 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 207 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 208 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 209 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 210 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 211 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 212 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 213 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 214 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 215 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 216 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 217 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 218 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 219 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 220 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 221 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 222 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 223 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 224 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 225 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 226 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 227 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 228 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 229 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 230 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 231 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 232 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 233 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 234 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 235 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 236 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 237 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 238 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 239 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 240 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 241 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 242 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 243 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 244 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 245 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 246 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 247 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 248 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 249 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 250 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 251 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 252 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 253 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 254 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 255 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 256 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 257 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 258 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 259 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 260 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 261 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 262 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 263 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 264 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 265 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 266 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 267 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 268 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 269 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 270 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 271 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 272 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 273 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 274 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 275 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 276 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 277 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 278 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 279 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 280 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 281 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 282 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 283 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 284 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 285 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 286 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 287 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 288 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 289 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 290 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 291 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 292 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 293 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 294 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 295 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 296 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 297 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 298 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 299 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 300 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 301 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 302 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 303 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 304 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 305 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 306 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 307 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 308 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 309 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 310 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 311 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 312 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 313 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 314 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 315 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 316 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 317 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 318 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 319 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
