# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-23.md)

*最后自动更新时间: 2026-03-23 18:18:45*
## 1. iPhone 17 Pro 演示运行 400B 大语言模型

**原文标题**: iPhone 17 Pro Demonstrated Running a 400B LLM

**原文链接**: [https://twitter.com/anemll/status/2035901335984611412](https://twitter.com/anemll/status/2035901335984611412)

根据提供的标题，以下是报道信息的摘要。请注意，您提供的内容包含一条来自 X（原 Twitter）关于禁用 JavaScript 的技术错误消息，而非文章正文。

### **摘要：iPhone 17 Pro 运行 400B LLM**

该标题预示着一个重大的技术里程碑：**iPhone 17 Pro** 已被证明可以运行拥有 **4000 亿（400B）参数的大语言模型（LLM）**。

**关键影响：**
*   **硬件突破：** 运行 400B 参数的模型（规模与 Meta 的 Llama 3 400B 相当）通常需要巨大的计算能力和企业级服务器集群中常见的数百 GB 显存（VRAM）。为了让智能手机处理此类模型，iPhone 17 Pro 可能需要革命性的 **A 系列芯片（推测为 A19 Pro）** 以及在 **统一内存（RAM）** 容量上实现前所未有的跨越。
*   **优化与量化：** 这一演示可能依赖于极致的 **模型量化**（压缩模型大小）和先进的内存交换技术，从而允许移动设备在不耗尽资源的情况下处理如此庞大的神经网络。
*   **端侧 AI 自主权：** 如果该模型是在本地（端侧）运行而非通过云端，这标志着 AI 正在转向保护用户隐私且无需互联网连接的高速性能时代。

**注意：** 由于提供的内容为错误消息，关于演示地点、所使用的具体 LLM 或是否利用了“混合”云处理等细节尚无法获知。

---

## 2. Cyber.mil 正在使用已过期 3 天的 TLS 证书提供文件下载服务。

**原文标题**: Cyber.mil serving file downloads using TLS certificate which expired 3 days ago

**原文链接**: [https://www.cyber.mil/stigs/downloads](https://www.cyber.mil/stigs/downloads)

Cyber.mil 网站是美国国防部（DoD）网络安全信息和工具的主要资源，目前其提供的文件下载服务正使用一个已于三天前过期的 TLS（传输层安全）证书。

此次证书过期影响了负责托管可下载内容（如软件补丁、安全指南和技术手册）的子域名或服务器。因此，尝试下载这些文件的用户会遇到浏览器安全警告，提示连接并非私密或不安全。

鉴于 Cyber.mil 是军方网络安全最佳实践和合规性的核心权威机构，这一失误尤为重大。在如此高知名度的域名上出现证书过期，表明其在监控和更新基础安全设施方面存在管理疏忽。

虽然网站主页可能看起来运行正常，但无法安全下载文件损害了网站的可靠性，并为依赖这些资源维护系统安全的人员制造了障碍。这一事件提醒人们，即使是专门从事数字防御的机构，也可能在常规维护中出现失误。

---

## 3. Trivy 再遭攻击：GitHub Actions 标签大规模篡改致密钥泄露

**原文标题**: Trivy under attack again: Widespread GitHub Actions tag compromise secrets

**原文链接**: [https://socket.dev/blog/trivy-under-attack-again-github-actions-compromise](https://socket.dev/blog/trivy-under-attack-again-github-actions-compromise)

在一起重大的供应链安全事件中，知名安全工具 **Trivy** 成为了针对 GitHub Actions 标签进行的持续攻击扩展的目标。

根据 Philipp Burckhardt 于 2026 年 3 月 22 日发布的研究，攻击者成功将三个受污染的 Trivy Docker 镜像版本——**0.69.4、0.69.5 和 0.69.6**——推送至 Docker Hub。这些特定的镜像被发现含有**窃信软件的失陷指标 (IOC)**，旨在从部署该工具的环境中外泄敏感数据。

此次入侵的一个关键迹象是分发平台之间的差异：恶意镜像被上传到了 Docker Hub，但在 Trivy 的 GitHub 仓库中并未出现任何对应的官方发布版本或源代码更新。此事件凸显了自动化供应链日益严峻的脆弱性，攻击者正利用受信任的分发渠道来绕过传统的安全边界。

建议用户核实镜像版本，并确保从官方、经过验证的发布路径拉取镜像。

---

## 4. Show HN: Threadprocs – 共享单一地址空间的可执行程序（零拷贝指针）

**原文标题**: Show HN: Threadprocs – executables sharing one address space (0-copy pointers)

**原文链接**: [https://github.com/jer-irl/threadprocs](https://github.com/jer-irl/threadprocs)

**Threadprocs** 是一个基于 Linux 的实验性项目，它使多个独立程序能够共存于单个共享虚拟地址空间中。通过结合 POSIX 进程模型与多线程技术，它允许不同的可执行文件（每个文件都维护各自的全局变量、libc 实例和运行时）直接共享指针。这使得不同程序之间能够对复杂的指针式数据结构进行零拷贝访问，而无需传统 IPC（进程间通信）的开销。

**工作原理**
该系统使用一个“服务器”（server）工具来托管虚拟地址空间，并使用一个“启动器”（launcher）将程序注入其中。由于它们共享地址空间，在一个程序中生成的指针在另一个程序中仍然有效。配套库 `libtproc` 用于实现服务发现，并提供对“服务器全局”暂存空间的访问，以用于引导通信。

**主要局限性**
*   **内存管理：** 每个 threadproc 使用各自的分配器。因此，内存必须由分配它的同一个程序进行释放；一个进程不能 `free()` 属于另一个进程的内存。
*   **编译：** 程序必须编译为位置无关代码（PIC）。
*   **系统调用：** 限制使用 `brk()` 和 `sbrk()` 以避免冲突，系统依赖 `mmap` 进行内存分配。
*   **工具支持：** 不支持通过 `ptrace()` 和 GDB 进行标准调试。在针对 PID 的操作和信号处理方面也存在细微差别。

**现状**
Threadprocs 目前是针对 aarch64 和 x86_64 Linux 的概念验证，旨在用于高性能的特殊应用。尽管它简化了指针共享，但作者指出，内存所有权的复杂性意味着它可能更适合自定义框架（如内置的 `tproc-actors`），而非通用软件。

---

## 5. BIO：Bao I/O 协处理器

**原文标题**: BIO: The Bao I/O Coprocessor

**原文链接**: [https://www.bunniestudios.com/blog/2026/bio-the-bao-i-o-coprocessor/](https://www.bunniestudios.com/blog/2026/bio-the-bao-i-o-coprocessor/)

**BIO (Bao I/O)** 是专为 **Baochip-1x**（一款基本开源的 22nm SoC）设计的专用协处理器。其主要用途是将 I/O 任务从主 CPU 卸载，以确保确定性且低抖动的性能。

作者最初参考了树莓派的 **PIO**，但发现其类 CISC 架构效率低下。在 FPGA 和 ASIC 实现中，PIO 复杂的指令和桶形移位器比标准 RISC-V 内核消耗更多逻辑资源，并显著阻碍了时序收敛。

为此，作者开发了基于 **RISC-V PicoRV32 (RV32E)** 内核的 BIO。为了克服标准 CPU 的不确定性，BIO 采用了源自作者博士论文“ADAM”的“寄存器队列”架构。寄存器 **x16 至 x31** 被映射至 I/O 功能，包括：
*   **FIFO：** 具有阻塞语义的 8 深共享队列（CPU 会在发生上溢或下溢时挂起）。
*   **GPIO 与事件：** 直接访问引脚和同步原语。
*   **量子寄存器 (x20)：** 挂起 CPU 执行，直到特定的分频器脉冲或外部事件发生，从而实现周期精确的时序，无需手动计算指令周期。

BIO 还支持 **BDMA 扩展**，使其能够作为智能 DMA 引擎处理复杂的数据转换。为了安全起见，内存访问受主机配置的白名单限制。

通过将标准 RISC-V 指令集架构 (ISA) 与硬件级阻塞寄存器相结合，BIO 为传统 I/O 控制器提供了一种紧凑、高性能的替代方案。它允许开发者在获得专用硬件状态机精度的同时，继续使用熟悉的软件工具。

---

## 6. Bombadil：针对 Web UI 的基于属性的测试

**原文标题**: Bombadil: Property-based testing for web UIs

**原文链接**: [https://github.com/antithesishq/bombadil](https://github.com/antithesishq/bombadil)

**Bombadil** 是由 **Antithesis** 开发的一款针对 Web UI 的实验性基于属性的测试工具。它通过自主探索用户界面来验证正确性属性，旨在比传统测试方法更早地在开发生命周期中识别复杂漏洞。

该工具具有出色的通用性，支持在本地开发环境、持续集成（CI）流水线以及 Antithesis 平台中运行。虽然目前仍处于早期实验阶段，功能和规范可能会发生变化，但开发者鼓励用户尝试并为其发展做出贡献。

项目提供了详尽的文档，包括手册、安装指南和各种示例，旨在帮助开发者将该模糊测试工具集成到工作流中。其命名灵感源自 J.R.R. 托尔金笔下的汤姆·庞巴迪（Tom Bombadil），强调其作为通过快速、稳健的规范来捕捉漏洞的“大师”角色。

---

## 7. Is it a pint?

**原文标题**: Is it a pint?

**原文链接**: [https://isitapint.com/](https://isitapint.com/)

生成摘要时出错

---

## 8. Unix philosophy is dead Long live something else?

**原文标题**: Unix philosophy is dead Long live something else?

**原文链接**: [https://sdomi.pl/weblog/27-manifesto-of-a-burnt-out-hacker/](https://sdomi.pl/weblog/27-manifesto-of-a-burnt-out-hacker/)

生成摘要时出错

---

## 9. An unsolicited guide to being a researcher [pdf]

**原文标题**: An unsolicited guide to being a researcher [pdf]

**原文链接**: [https://emerge-lab.github.io/papers/an-unsolicited-guide-to-good-research.pdf](https://emerge-lab.github.io/papers/an-unsolicited-guide-to-good-research.pdf)

生成摘要时出错

---

## 10. I built an AI receptionist for a mechanic shop

**原文标题**: I built an AI receptionist for a mechanic shop

**原文链接**: [https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/](https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 2 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 3 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 4 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 5 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 6 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 7 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 8 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 9 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 10 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 11 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 12 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 13 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 14 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 15 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 16 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 17 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 18 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 19 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 20 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 21 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 22 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 23 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 24 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 25 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 26 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 27 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 28 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 29 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 30 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 31 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 32 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 33 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 34 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 35 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 36 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 37 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 38 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 39 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 40 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 41 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 42 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 43 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 44 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 45 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 46 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 47 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 48 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 49 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 50 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 51 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 52 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 53 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 54 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 55 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 56 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 57 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 58 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 59 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 60 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 61 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 62 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 63 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 64 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 65 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 66 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 67 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 68 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 69 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 70 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 71 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 72 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 73 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 74 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 75 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 76 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 77 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 78 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 79 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 80 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 81 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 82 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 83 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 84 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 85 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 86 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 87 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 88 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 89 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 90 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 91 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 92 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 93 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 94 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 95 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 96 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 97 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 98 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 99 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 100 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 101 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 102 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 103 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 104 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 105 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 106 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 107 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 108 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 109 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 110 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 111 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 112 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 113 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 114 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 115 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 116 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 117 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 118 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 119 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 120 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 121 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 122 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 123 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 124 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 125 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 126 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 127 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 128 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 129 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 130 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 131 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 132 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 133 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 134 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 135 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 136 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 137 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 138 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 139 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 140 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 141 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 142 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 143 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 144 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 145 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 146 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 147 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 148 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 149 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 150 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 151 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 152 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 153 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 154 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 155 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 156 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 157 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 158 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 159 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 160 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 161 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 162 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 163 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 164 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 165 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 166 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 167 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 168 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 169 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 170 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 171 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 172 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 173 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 174 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 175 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 176 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 177 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 178 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 179 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 180 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 181 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 182 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 183 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 184 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 185 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 186 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 187 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 188 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 189 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 190 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 191 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 192 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 193 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 194 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 195 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 196 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 197 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 198 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 199 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 200 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 201 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 202 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 203 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 204 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 205 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 206 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 207 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 208 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 209 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 210 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 211 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 212 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 213 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 214 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 215 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 216 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 217 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 218 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 219 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 220 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 221 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 222 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 223 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 224 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 225 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 226 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 227 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 228 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 229 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 230 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 231 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 232 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 233 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 234 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 235 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 236 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 237 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 238 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 239 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 240 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 241 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 242 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 243 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 244 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 245 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 246 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 247 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 248 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 249 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 250 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 251 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 252 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 253 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 254 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 255 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 256 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 257 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 258 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 259 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 260 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 261 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 262 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 263 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 264 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 265 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 266 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 267 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 268 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 269 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 270 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 271 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 272 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 273 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 274 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 275 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 276 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 277 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 278 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 279 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 280 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 281 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 282 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 283 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 284 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 285 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 286 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 287 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 288 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 289 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 290 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 291 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 292 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 293 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 294 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 295 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 296 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 297 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 298 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 299 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 300 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 301 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 302 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 303 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 304 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 305 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 306 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 307 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 308 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 309 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 310 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 311 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 312 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 313 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 314 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 315 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 316 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 317 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 318 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 319 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 320 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 321 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 322 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 323 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 324 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 325 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 326 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 327 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 328 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 329 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 330 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 331 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 332 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 333 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 334 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 335 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 336 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 337 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 338 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 339 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 340 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 341 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 342 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 343 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 344 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 345 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 346 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 347 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 348 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 349 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 350 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 351 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 352 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 353 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 354 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 355 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 356 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 357 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 358 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 359 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 360 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 361 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 362 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 363 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 364 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 365 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 366 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 367 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 368 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
