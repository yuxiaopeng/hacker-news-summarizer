# Hacker News 热门文章摘要 (2026-03-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. If DSPy is so great, why isn't anyone using it?

**原文标题**: If DSPy is so great, why isn't anyone using it?

**原文链接**: [https://skylarbpayne.com/posts/dspy-engineering-patterns/](https://skylarbpayne.com/posts/dspy-engineering-patterns/)

生成摘要时出错

---

## 12. Migrating to the EU

**原文标题**: Migrating to the EU

**原文链接**: [https://rz01.org/eu-migration/](https://rz01.org/eu-migration/)

生成摘要时出错

---

## 13. PC Gamer recommends RSS readers in a 37mb article that just keeps downloading

**原文标题**: PC Gamer recommends RSS readers in a 37mb article that just keeps downloading

**原文链接**: [https://stuartbreckenridge.net/2026-03-19-pc-gamer-recommends-rss-readers-in-a-37mb-article/](https://stuartbreckenridge.net/2026-03-19-pc-gamer-recommends-rss-readers-in-a-37mb-article/)

生成摘要时出错

---

## 14. Two pilots dead after plane and ground vehicle collide at LaGuardia

**原文标题**: Two pilots dead after plane and ground vehicle collide at LaGuardia

**原文链接**: [https://www.bbc.com/news/articles/cy01g522ww4o](https://www.bbc.com/news/articles/cy01g522ww4o)

生成摘要时出错

---

## 15. POSSE – Publish on your Own Site, Syndicate Elsewhere

**原文标题**: POSSE – Publish on your Own Site, Syndicate Elsewhere

**原文链接**: [https://indieweb.org/POSSE](https://indieweb.org/POSSE)

生成摘要时出错

---

## 16. Side-Effectful Expressions in C (2023)

**原文标题**: Side-Effectful Expressions in C (2023)

**原文链接**: [https://blog.xoria.org/expr-stmt-c/](https://blog.xoria.org/expr-stmt-c/)

生成摘要时出错

---

## 17. Walmart: ChatGPT checkout converted 3x worse than website

**原文标题**: Walmart: ChatGPT checkout converted 3x worse than website

**原文链接**: [https://searchengineland.com/walmart-chatgpt-checkout-converted-worse-472071](https://searchengineland.com/walmart-chatgpt-checkout-converted-worse-472071)

生成摘要时出错

---

## 18. GitHub appears to be struggling with measly three nines availability

**原文标题**: GitHub appears to be struggling with measly three nines availability

**原文链接**: [https://www.theregister.com/2026/02/10/github_outages/](https://www.theregister.com/2026/02/10/github_outages/)

生成摘要时出错

---

## 19. General Motors is assisting with the restoration of a rare EV1

**原文标题**: General Motors is assisting with the restoration of a rare EV1

**原文链接**: [https://evinfo.net/2026/03/general-motors-is-assisting-with-the-restoration-of-an-1996-ev1/](https://evinfo.net/2026/03/general-motors-is-assisting-with-the-restoration-of-an-1996-ev1/)

生成摘要时出错

---

## 20. The gold standard of optimization: A look under the hood of RollerCoaster Tycoon

**原文标题**: The gold standard of optimization: A look under the hood of RollerCoaster Tycoon

**原文链接**: [https://larstofus.com/2026/03/22/the-gold-standard-of-optimization-a-look-under-the-hood-of-rollercoaster-tycoon/](https://larstofus.com/2026/03/22/the-gold-standard-of-optimization-a-look-under-the-hood-of-rollercoaster-tycoon/)

生成摘要时出错

---

## 21. Tin Can, a 'landline' for kids

**原文标题**: Tin Can, a 'landline' for kids

**原文链接**: [https://www.businessinsider.com/tin-can-landline-kids-cellphone-cell-alternative-how-2025-9](https://www.businessinsider.com/tin-can-landline-kids-cellphone-cell-alternative-how-2025-9)

生成摘要时出错

---

## 22. “Collaboration” is bullshit

**原文标题**: “Collaboration” is bullshit

**原文链接**: [https://www.joanwestenberg.com/collaboration-is-bullshit/](https://www.joanwestenberg.com/collaboration-is-bullshit/)

生成摘要时出错

---

## 23. Reports of code's death are greatly exaggerated

**原文标题**: Reports of code's death are greatly exaggerated

**原文链接**: [https://stevekrouse.com/precision](https://stevekrouse.com/precision)

生成摘要时出错

---

## 24. The future of version control

**原文标题**: The future of version control

**原文链接**: [https://bramcohen.com/p/manyana](https://bramcohen.com/p/manyana)

生成摘要时出错

---

## 25. Nanopositioning Metrology, Gödel, and Bootstraps

**原文标题**: Nanopositioning Metrology, Gödel, and Bootstraps

**原文链接**: [https://www.pi-usa.us/en/tech-blog/nanopositioning-metrology-goedel-and-bootstraps](https://www.pi-usa.us/en/tech-blog/nanopositioning-metrology-goedel-and-bootstraps)

生成摘要时出错

---

## 26. Cyberattack on vehicle breathalyzer company leaves drivers stranded in the US

**原文标题**: Cyberattack on vehicle breathalyzer company leaves drivers stranded in the US

**原文链接**: [https://techcrunch.com/2026/03/20/cyberattack-on-vehicle-breathalyzer-company-leaves-drivers-stranded-across-the-us/](https://techcrunch.com/2026/03/20/cyberattack-on-vehicle-breathalyzer-company-leaves-drivers-stranded-across-the-us/)

生成摘要时出错

---

## 27. Can you get root with only a cigarette lighter? (2024)

**原文标题**: Can you get root with only a cigarette lighter? (2024)

**原文链接**: [https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html](https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html)

生成摘要时出错

---

## 28. Why I love NixOS

**原文标题**: Why I love NixOS

**原文链接**: [https://www.birkey.co/2026-03-22-why-i-love-nixos.html](https://www.birkey.co/2026-03-22-why-i-love-nixos.html)

生成摘要时出错

---

## 29. Project Nomad – Knowledge That Never Goes Offline

**原文标题**: Project Nomad – Knowledge That Never Goes Offline

**原文链接**: [https://www.projectnomad.us](https://www.projectnomad.us)

生成摘要时出错

---

## 30. You are not your job

**原文标题**: You are not your job

**原文链接**: [https://jry.io/writing/you-are-not-your-job/](https://jry.io/writing/you-are-not-your-job/)

生成摘要时出错

---

## 31. GoGoGrandparent (YC S16) is hiring Back end Engineers

**原文标题**: GoGoGrandparent (YC S16) is hiring Back end Engineers

**原文链接**: [https://www.ycombinator.com/companies/gogograndparent/jobs/2vbzAw8-backend-engineer](https://www.ycombinator.com/companies/gogograndparent/jobs/2vbzAw8-backend-engineer)

生成摘要时出错

---

## 32. You are not your job

**原文标题**: You are not your job

**原文链接**: [https://jry.io/writing/you-are-not-your-job/](https://jry.io/writing/you-are-not-your-job/)

生成摘要时出错

---

## 33. Study: 'Security Fatigue' May Weaken Digital Defenses

**原文标题**: Study: 'Security Fatigue' May Weaken Digital Defenses

**原文链接**: [https://www.albany.edu/news-center/news/2026-study-security-fatigue-may-weaken-digital-defenses](https://www.albany.edu/news-center/news/2026-study-security-fatigue-may-weaken-digital-defenses)

生成摘要时出错

---

## 34. Flash-MoE: Running a 397B Parameter Model on a Laptop

**原文标题**: Flash-MoE: Running a 397B Parameter Model on a Laptop

**原文链接**: [https://github.com/danveloper/flash-moe](https://github.com/danveloper/flash-moe)

生成摘要时出错

---

## 35. Show HN: The King Wen Permutation: [52, 10, 2]

**原文标题**: Show HN: The King Wen Permutation: [52, 10, 2]

**原文链接**: [https://gzw1987-bit.github.io/iching-math/](https://gzw1987-bit.github.io/iching-math/)

生成摘要时出错

---

## 36. Fear and Fragility: The Glass Delusion and Its History

**原文标题**: Fear and Fragility: The Glass Delusion and Its History

**原文链接**: [https://publicdomainreview.org/essay/fear-and-fragility-the-glass-delusion-and-its-history](https://publicdomainreview.org/essay/fear-and-fragility-the-glass-delusion-and-its-history)

生成摘要时出错

---

## 37. What young workers are doing to AI-proof themselves

**原文标题**: What young workers are doing to AI-proof themselves

**原文链接**: [https://www.wsj.com/economy/jobs/ai-jobs-young-people-careers-14282284](https://www.wsj.com/economy/jobs/ai-jobs-young-people-careers-14282284)

生成摘要时出错

---

## 38. America tells private firms to "hack back"

**原文标题**: America tells private firms to "hack back"

**原文链接**: [https://www.economist.com/united-states/2026/03/22/america-tells-private-firms-to-hack-back](https://www.economist.com/united-states/2026/03/22/america-tells-private-firms-to-hack-back)

生成摘要时出错

---

## 39. Student beauty and grades under in-person and remote teaching

**原文标题**: Student beauty and grades under in-person and remote teaching

**原文链接**: [https://www.sciencedirect.com/science/article/pii/S016517652200283X](https://www.sciencedirect.com/science/article/pii/S016517652200283X)

生成摘要时出错

---

## 40. Diverse perspectives on AI from Rust contributors and maintainers

**原文标题**: Diverse perspectives on AI from Rust contributors and maintainers

**原文链接**: [https://nikomatsakis.github.io/rust-project-perspectives-on-ai/feb27-summary.html](https://nikomatsakis.github.io/rust-project-perspectives-on-ai/feb27-summary.html)

生成摘要时出错

---

## 41. Dataframe 1.0.0.0

**原文标题**: Dataframe 1.0.0.0

**原文链接**: [https://discourse.haskell.org/t/ann-dataframe-1-0-0-0/13834](https://discourse.haskell.org/t/ann-dataframe-1-0-0-0/13834)

生成摘要时出错

---

## 42. Mark Zuckerberg Is Building an AI Agent to Help Him Be CEO

**原文标题**: Mark Zuckerberg Is Building an AI Agent to Help Him Be CEO

**原文链接**: [https://www.wsj.com/tech/ai/mark-zuckerberg-is-building-an-ai-agent-to-help-him-be-ceo-eddab2d5](https://www.wsj.com/tech/ai/mark-zuckerberg-is-building-an-ai-agent-to-help-him-be-ceo-eddab2d5)

生成摘要时出错

---

## 43. GrapheneOS will remain usable by anyone without requiring personal information

**原文标题**: GrapheneOS will remain usable by anyone without requiring personal information

**原文链接**: [https://grapheneos.social/@GrapheneOS/116261301913660830](https://grapheneos.social/@GrapheneOS/116261301913660830)

生成摘要时出错

---

## 44. Building an FPGA 3dfx Voodoo with Modern RTL Tools

**原文标题**: Building an FPGA 3dfx Voodoo with Modern RTL Tools

**原文链接**: [https://noquiche.fyi/voodoo](https://noquiche.fyi/voodoo)

生成摘要时出错

---

## 45. Five years of running a systems reading group at Microsoft

**原文标题**: Five years of running a systems reading group at Microsoft

**原文链接**: [https://armaansood.com/posts/systems-reading-group/](https://armaansood.com/posts/systems-reading-group/)

生成摘要时出错

---

## 46. More common mistakes to avoid when creating system architecture diagrams

**原文标题**: More common mistakes to avoid when creating system architecture diagrams

**原文链接**: [https://www.ilograph.com/blog/posts/more-common-diagram-mistakes/](https://www.ilograph.com/blog/posts/more-common-diagram-mistakes/)

生成摘要时出错

---

## 47. The LCA problem revisited [pdf]

**原文标题**: The LCA problem revisited [pdf]

**原文链接**: [https://www3.cs.stonybrook.edu/~bender/talks/BenderFa00-lca-talk.pdf](https://www3.cs.stonybrook.edu/~bender/talks/BenderFa00-lca-talk.pdf)

生成摘要时出错

---

## 48. Ordered dithering with arbitrary or irregular colour palettes (2023)

**原文标题**: Ordered dithering with arbitrary or irregular colour palettes (2023)

**原文链接**: [https://matejlou.blog/2023/12/06/ordered-dithering-for-arbitrary-or-irregular-palettes/](https://matejlou.blog/2023/12/06/ordered-dithering-for-arbitrary-or-irregular-palettes/)

生成摘要时出错

---

## 49. Fyn: An uv fork with new features, bug fixes, stripped telemetry

**原文标题**: Fyn: An uv fork with new features, bug fixes, stripped telemetry

**原文链接**: [https://github.com/duriantaco/fyn](https://github.com/duriantaco/fyn)

生成摘要时出错

---

## 50. A Copy-Paste Bug That Broke PSpice AES-256 Encryption

**原文标题**: A Copy-Paste Bug That Broke PSpice AES-256 Encryption

**原文链接**: [https://jtsylve.blog/post/2026/03/18/PSpice-Encryption-Weakness](https://jtsylve.blog/post/2026/03/18/PSpice-Encryption-Weakness)

生成摘要时出错

---

## 51. LLMs predict my coffee

**原文标题**: LLMs predict my coffee

**原文链接**: [https://dynomight.net/coffee/](https://dynomight.net/coffee/)

生成摘要时出错

---

## 52. Show HN: Lockpaw One hotkey to cover your Mac screen without putting it to sleep

**原文标题**: Show HN: Lockpaw One hotkey to cover your Mac screen without putting it to sleep

**原文链接**: [https://github.com/sorkila/lockpaw](https://github.com/sorkila/lockpaw)

生成摘要时出错

---

## 53. They’re vibe-coding spam now

**原文标题**: They’re vibe-coding spam now

**原文链接**: [https://tedium.co/2026/02/25/vibe-coded-email-spam/](https://tedium.co/2026/02/25/vibe-coded-email-spam/)

生成摘要时出错

---

## 54. The IBM scientist who rewrote the rules of information just won a Turing Award

**原文标题**: The IBM scientist who rewrote the rules of information just won a Turing Award

**原文链接**: [https://www.ibm.com/think/news/ibm-scientist-charles-bennett-turing-award](https://www.ibm.com/think/news/ibm-scientist-charles-bennett-turing-award)

生成摘要时出错

---

## 55. How to attract AI bots to your open source project

**原文标题**: How to attract AI bots to your open source project

**原文链接**: [https://nesbitt.io/2026/03/21/how-to-attract-ai-bots-to-your-open-source-project.html](https://nesbitt.io/2026/03/21/how-to-attract-ai-bots-to-your-open-source-project.html)

生成摘要时出错

---

## 56. Huel Joins Danone

**原文标题**: Huel Joins Danone

**原文链接**: [https://huel.com/pages/huel-joins-danone](https://huel.com/pages/huel-joins-danone)

生成摘要时出错

---

## 57. MAUI Is Coming to Linux

**原文标题**: MAUI Is Coming to Linux

**原文链接**: [https://avaloniaui.net/blog/maui-avalonia-preview-1](https://avaloniaui.net/blog/maui-avalonia-preview-1)

生成摘要时出错

---

## 58. Migrating the American express payment network, twice

**原文标题**: Migrating the American express payment network, twice

**原文链接**: [https://americanexpress.io/migrating-the-payments-network-twice/](https://americanexpress.io/migrating-the-payments-network-twice/)

生成摘要时出错

---

## 59. The world just lived through the 11 hottest years on record

**原文标题**: The world just lived through the 11 hottest years on record

**原文链接**: [https://www.nature.com/articles/d41586-026-00946-6](https://www.nature.com/articles/d41586-026-00946-6)

生成摘要时出错

---

## 60. A Review of Dice that came with The White Castle (2025)

**原文标题**: A Review of Dice that came with The White Castle (2025)

**原文链接**: [https://boardgamegeek.com/thread/3533812/a-review-of-dice-that-came-with-the-white-castle](https://boardgamegeek.com/thread/3533812/a-review-of-dice-that-came-with-the-white-castle)

生成摘要时出错

---

## 61. Bored of eating your own dogfood? Try smelling your own farts

**原文标题**: Bored of eating your own dogfood? Try smelling your own farts

**原文链接**: [https://shkspr.mobi/blog/2026/03/bored-of-eating-your-own-dogfood-try-smelling-your-own-farts/](https://shkspr.mobi/blog/2026/03/bored-of-eating-your-own-dogfood-try-smelling-your-own-farts/)

生成摘要时出错

---

## 62. 355 Issues of the UK music magazine NME from 1969-1983

**原文标题**: 355 Issues of the UK music magazine NME from 1969-1983

**原文链接**: [https://archive.org/search?query=creator%3A%22NME+-+New+Musical+Express%22&sort=-addeddate](https://archive.org/search?query=creator%3A%22NME+-+New+Musical+Express%22&sort=-addeddate)

生成摘要时出错

---

## 63. Apple's intentional crippling of Mobile Safari

**原文标题**: Apple's intentional crippling of Mobile Safari

**原文链接**: [https://pwa.gripe/](https://pwa.gripe/)

生成摘要时出错

---

## 64. My first patch to the Linux kernel

**原文标题**: My first patch to the Linux kernel

**原文链接**: [https://pooladkhay.com/posts/first-kernel-patch/](https://pooladkhay.com/posts/first-kernel-patch/)

生成摘要时出错

---

## 65. Windows native app development is a mess

**原文标题**: Windows native app development is a mess

**原文链接**: [https://domenic.me/windows-native-dev/](https://domenic.me/windows-native-dev/)

生成摘要时出错

---

## 66. Teaching Claude to QA a mobile app

**原文标题**: Teaching Claude to QA a mobile app

**原文链接**: [https://christophermeiklejohn.com/ai/zabriskie/development/android/ios/2026/03/22/teaching-claude-to-qa-a-mobile-app.html](https://christophermeiklejohn.com/ai/zabriskie/development/android/ios/2026/03/22/teaching-claude-to-qa-a-mobile-app.html)

生成摘要时出错

---

## 67. Unlocking 25 Gigabit/S on 10 GbE Direct Attach Copper

**原文标题**: Unlocking 25 Gigabit/S on 10 GbE Direct Attach Copper

**原文链接**: [https://kohlschuetter.github.io/blog/posts/2026/03/22/unlock25/](https://kohlschuetter.github.io/blog/posts/2026/03/22/unlock25/)

生成摘要时出错

---

## 68. First and Lego Education Partnership Update

**原文标题**: First and Lego Education Partnership Update

**原文链接**: [https://community.firstinspires.org/first-lego-education-partnership-update](https://community.firstinspires.org/first-lego-education-partnership-update)

生成摘要时出错

---

## 69. Lyme Disease Vaccine Candidate Demonstrates Strong Efficacy in Phase 3 Trial

**原文标题**: Lyme Disease Vaccine Candidate Demonstrates Strong Efficacy in Phase 3 Trial

**原文链接**: [https://www.pfizer.com/news/press-release/press-release-detail/pfizer-and-valneva-announce-lyme-disease-vaccine-candidate](https://www.pfizer.com/news/press-release/press-release-detail/pfizer-and-valneva-announce-lyme-disease-vaccine-candidate)

生成摘要时出错

---

## 70. Show HN: Agent Kernel – Three Markdown files that make any AI agent stateful

**原文标题**: Show HN: Agent Kernel – Three Markdown files that make any AI agent stateful

**原文链接**: [https://github.com/oguzbilgic/agent-kernel](https://github.com/oguzbilgic/agent-kernel)

生成摘要时出错

---

## 71. DoorDash Tasks

**原文标题**: DoorDash Tasks

**原文链接**: [https://about.doordash.com/en-us/news/introducing-doordash-tasks](https://about.doordash.com/en-us/news/introducing-doordash-tasks)

生成摘要时出错

---

## 72. Apply video compression on KV cache to 10,000x less error at Q4 quant

**原文标题**: Apply video compression on KV cache to 10,000x less error at Q4 quant

**原文链接**: [https://github.com/cenconq25/delta-compress-llm](https://github.com/cenconq25/delta-compress-llm)

生成摘要时出错

---

## 73. Show HN: Codala, a social network built on scanning barcodes

**原文标题**: Show HN: Codala, a social network built on scanning barcodes

**原文链接**: [https://play.google.com/store/apps/details?id=com.hsynkrkye.codala&hl=en](https://play.google.com/store/apps/details?id=com.hsynkrkye.codala&hl=en)

生成摘要时出错

---

## 74. Brute-forcing my algorithmic ignorance

**原文标题**: Brute-forcing my algorithmic ignorance

**原文链接**: [http://blog.dominikrudnik.pl/my-google-recruitment-journey-part-1](http://blog.dominikrudnik.pl/my-google-recruitment-journey-part-1)

生成摘要时出错

---

## 75. Show HN: Revise – An AI Editor for Documents

**原文标题**: Show HN: Revise – An AI Editor for Documents

**原文链接**: [https://revise.io](https://revise.io)

生成摘要时出错

---

## 76. A case against currying

**原文标题**: A case against currying

**原文链接**: [https://emi-h.com/articles/a-case-against-currying.html](https://emi-h.com/articles/a-case-against-currying.html)

生成摘要时出错

---

## 77. TypeScript 6.0

**原文标题**: TypeScript 6.0

**原文链接**: [https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/)

生成摘要时出错

---

## 78. OpenClaw is a security nightmare dressed up as a daydream

**原文标题**: OpenClaw is a security nightmare dressed up as a daydream

**原文链接**: [https://composio.dev/content/openclaw-security-and-vulnerabilities](https://composio.dev/content/openclaw-security-and-vulnerabilities)

生成摘要时出错

---

## 79. Vectorization of Verilog Designs and its Effects on Verification and Synthesis

**原文标题**: Vectorization of Verilog Designs and its Effects on Verification and Synthesis

**原文链接**: [https://arxiv.org/abs/2603.17099](https://arxiv.org/abs/2603.17099)

生成摘要时出错

---

## 80. Cloudflare flags archive.today as "C&C/Botnet"; no longer resolves via 1.1.1.2

**原文标题**: Cloudflare flags archive.today as "C&C/Botnet"; no longer resolves via 1.1.1.2

**原文链接**: [https://radar.cloudflare.com/domains/domain/archive.today](https://radar.cloudflare.com/domains/domain/archive.today)

生成摘要时出错

---

## 81. Intuitions for Tranformer Circuits

**原文标题**: Intuitions for Tranformer Circuits

**原文链接**: [https://www.connorjdavis.com/p/intuitions-for-transformer-circuits](https://www.connorjdavis.com/p/intuitions-for-transformer-circuits)

生成摘要时出错

---

## 82. JavaScript Is Enough

**原文标题**: JavaScript Is Enough

**原文链接**: [https://geajs.com/](https://geajs.com/)

生成摘要时出错

---

## 83. HopTab – Open source macOS app switcher and tiler that replaces Cmd+Tab

**原文标题**: HopTab – Open source macOS app switcher and tiler that replaces Cmd+Tab

**原文链接**: [https://www.royalbhati.com/hoptab](https://www.royalbhati.com/hoptab)

生成摘要时出错

---

## 84. Why Expanding Roads Fails to Reduce Traffic Congestion

**原文标题**: Why Expanding Roads Fails to Reduce Traffic Congestion

**原文链接**: [https://www.nominalnews.com/p/expanding-roads-traffic-congestion](https://www.nominalnews.com/p/expanding-roads-traffic-congestion)

生成摘要时出错

---

## 85. Theodosian Land Walls of Constantinople (2025)

**原文标题**: Theodosian Land Walls of Constantinople (2025)

**原文链接**: [https://turkisharchaeonews.net/object/theodosian-land-walls-constantinople](https://turkisharchaeonews.net/object/theodosian-land-walls-constantinople)

生成摘要时出错

---

## 86. Bayesian statistics for confused data scientists

**原文标题**: Bayesian statistics for confused data scientists

**原文链接**: [https://nchagnet.pages.dev/blog/bayesian-statistics-for-confused-data-scientists/](https://nchagnet.pages.dev/blog/bayesian-statistics-for-confused-data-scientists/)

生成摘要时出错

---

## 87. Node.js worker threads are problematic, but they work great for us

**原文标题**: Node.js worker threads are problematic, but they work great for us

**原文链接**: [https://www.inngest.com/blog/node-worker-threads](https://www.inngest.com/blog/node-worker-threads)

生成摘要时出错

---

## 88. The three pillars of JavaScript bloat

**原文标题**: The three pillars of JavaScript bloat

**原文链接**: [https://43081j.com/2026/03/three-pillars-of-javascript-bloat](https://43081j.com/2026/03/three-pillars-of-javascript-bloat)

生成摘要时出错

---

## 89. GrapheneOS refuses to comply with new age verification laws for operating system

**原文标题**: GrapheneOS refuses to comply with new age verification laws for operating system

**原文链接**: [https://www.tomshardware.com/software/operating-systems/grapheneos-refuses-to-comply-with-age-verification-laws](https://www.tomshardware.com/software/operating-systems/grapheneos-refuses-to-comply-with-age-verification-laws)

生成摘要时出错

---

## 90. Some things just take time

**原文标题**: Some things just take time

**原文链接**: [https://lucumr.pocoo.org/2026/3/20/some-things-just-take-time/](https://lucumr.pocoo.org/2026/3/20/some-things-just-take-time/)

生成摘要时出错

---

## 91. A Bilingual Localization for Pillars of Eternity (EN and ZH)

**原文标题**: A Bilingual Localization for Pillars of Eternity (EN and ZH)

**原文链接**: [https://blog.cerrorism.com/blog/2026-03-19](https://blog.cerrorism.com/blog/2026-03-19)

生成摘要时出错

---

## 92. Trivy ecosystem supply chain temporarily compromised

**原文标题**: Trivy ecosystem supply chain temporarily compromised

**原文链接**: [https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23](https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23)

生成摘要时出错

---

## 93. OpenCode – Open source AI coding agent

**原文标题**: OpenCode – Open source AI coding agent

**原文链接**: [https://opencode.ai/](https://opencode.ai/)

生成摘要时出错

---

## 94. AI Proteomics Competition 2026 – $13K Prize, Internships and Compute Support

**原文标题**: AI Proteomics Competition 2026 – $13K Prize, Internships and Compute Support

**原文链接**: [https://www.bohrium.com/competitions/9813928053?tab=introduce](https://www.bohrium.com/competitions/9813928053?tab=introduce)

生成摘要时出错

---

## 95. The Slow Collapse of MkDocs

**原文标题**: The Slow Collapse of MkDocs

**原文链接**: [https://fpgmaas.com/blog/collapse-of-mkdocs/](https://fpgmaas.com/blog/collapse-of-mkdocs/)

生成摘要时出错

---

## 96. 25 Years of Eggs

**原文标题**: 25 Years of Eggs

**原文链接**: [https://www.john-rush.com/posts/eggs-25-years-20260219.html](https://www.john-rush.com/posts/eggs-25-years-20260219.html)

生成摘要时出错

---

## 97. Tinybox – A powerful computer for deep learning

**原文标题**: Tinybox – A powerful computer for deep learning

**原文链接**: [https://tinygrad.org/#tinybox](https://tinygrad.org/#tinybox)

生成摘要时出错

---

## 98. ForgeKV – Redis-compatible KV server in Rust that scales with cores

**原文标题**: ForgeKV – Redis-compatible KV server in Rust that scales with cores

**原文链接**: [https://github.com/ForgeKV/forgekv](https://github.com/ForgeKV/forgekv)

生成摘要时出错

---

## 99. Mamba-3

**原文标题**: Mamba-3

**原文链接**: [https://www.together.ai/blog/mamba-3](https://www.together.ai/blog/mamba-3)

生成摘要时出错

---

## 100. Battle of U.S. rail barons: Merger is setting the industry on a collision course

**原文标题**: Battle of U.S. rail barons: Merger is setting the industry on a collision course

**原文链接**: [https://www.thecanadianpressnews.ca/business/battle-of-the-rail-barons-how-a-merger-is-setting-the-industry-on-a-collision/article_4b82ef47-bb9b-533a-ac97-78a89d065ad1.html](https://www.thecanadianpressnews.ca/business/battle-of-the-rail-barons-how-a-merger-is-setting-the-industry-on-a-collision/article_4b82ef47-bb9b-533a-ac97-78a89d065ad1.html)

生成摘要时出错

---

