# Hacker News 热门文章摘要 (2026-08-02)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我们教授给英语学习者的词汇是如何演变的

**原文标题**: How the words we teach English language learners changed

**原文链接**: [https://pudding.cool/2026/07/essential-words/](https://pudding.cool/2026/07/essential-words/)

在《我们教给英语学习者的单词是如何变化的》一文中，Jasmine Nackash 通过对比 1953 年的《通用词表》（General Service List）及其 2023 年的更新版本，分析了“核心”英语词汇的演变。70 多年来，核心词汇经历了深刻的转变，反映了从具象、实践性的世界向由抽象系统定义的世界的过渡。

分析揭示了几个关键趋势：

*   **从具象到抽象：** 1953 年的词表扎根于物理世界，以农业、手工工具和生活用品（如 *plow*、*soap*、*flour*）为特色。2023 年的词表则将这些替换为抽象概念，如 *mortgage*（抵押）、*corporation*（公司）、*perspective*（视角）和 *analysis*（分析）。高度具象的词汇——即那些易于视觉化的词汇——在总数中的占比从 21% 下降到了 14%。
*   **从自我到系统：** 描述身体和个人情感的词汇（如 *mercy*、*pity*）已转向医疗管理（*clinical*、*therapy*）和认知过程（*logic*、*investigate*）。同样，社交语言也从个人关系（*fellowship*、*polite*）转向了制度和类别身份（*ethnic*、*gender*、*organization*）。
*   **对精确性的需求：** 2023 年的词表中副词显著增加（如 *specifically*、*approximately*、*virtually*）。这些词被用来校准和界定现代交流中日益增强的抽象性。
*   **认知影响：** Nackash 指出，具象词汇更具“粘性”，因为它们使用了“双重编码”（感官和语言路径）。而抽象词汇纯粹是语言层面的，更难以处理和记忆。

最终，这种转变反映了一个从蓝领手工劳动向白领系统管理转型的社会。我们不再优先考虑关于事物如何制造的语言，而是转向了管理现代生活的复杂、无形的制度和思想。

---

## 2. Coldcard 灾难进一步恶化：黑客攻击损失可能已达 8860 万美元

**原文标题**: The Coldcard Disaster Gets Worse: The Hack May Have Reached $88.6M

**原文链接**: [https://medium.com/mountain-movers/the-coldcard-disaster-gets-worse-the-hack-may-have-reached-88-6-af507b028594](https://medium.com/mountain-movers/the-coldcard-disaster-gets-worse-the-hack-may-have-reached-88-6-af507b028594)

针对 Coldcard 硬件钱包的重大固件漏洞攻击已经升级，目前估计涉及 4,585 个地址，损失达 8,860 万美元（1,367 BTC）。根据 Galaxy Research 的数据，此次攻击发生在 2024 年 7 月 30 日至 8 月 1 日之间，共分为三个明显的波次，攻击目标从高净值用户转向了规模较小的个人持有者。

该漏洞源于 2021 年 3 月发布的固件中的一个关键缺陷，该缺陷损害了助记词生成的随机性，使得攻击者能够预测并扫描存在风险的地址。前两波攻击使用了共享的归集地址，而第三波攻击则表现出更高的复杂性——利用 P2WSH 保管库并支付极高的交易手续费（200 sat/vB），以优先保证速度并规避区块链分析。这种策略的转变表明攻击者可能使用了自动化脚本，或者有第二名攻击者介入。

关键发现包括：
*   **目标群体：** 此次黑客攻击主要影响的是个人自托管用户，而非交易所；95.5% 的受害者持币量低于 1 BTC。
*   **操作纪律：** 被盗资金仍存放在“海盗”地址中未被动用，这表明攻击者极具纪律性，正在等待合适时机转移资产。
*   **行业影响：** 这是开源硬件的“心脏滴血（Heartbleed）时刻”，打破了自托管在心理上的确定性。它凸显了如果没有严格、独立的审计，代码的透明性并不能保证安全性。

专家警告称，随着攻击的持续，损失可能会进一步扩大。任何使用该受损固件生成助记词的用户都面临极大风险，务必立即将资金迁移至安全生成的新助记词地址中。

---

## 3. Show HN: Kakehashi – 在 Linux ARM 上运行 macOS 二进制文件的实验性用户空间

**原文标题**: Show HN: Kakehashi – Experimental userspace to run macOS binaries on Linux ARM

**原文链接**: [https://github.com/wie-project/kakehashi](https://github.com/wie-project/kakehashi)

**Kakehashi** 是一个基于 Rust 开发的实验性用户态转换层，旨在 Linux aarch64 上原生运行 macOS ARM64 (Darwin Mach-O) 二进制文件。与指令模拟器不同，Kakehashi 直接在宿主 CPU 上执行访客代码，其核心功能在于加载二进制文件、映射独立的 `libSystem` 以及转换 BSD 系统调用。

**核心特性与能力：**
*   **侧重命令行 (CLI)：** 已成功运行如 `7-Zip (7zz)`、`curl` 和 `clang` 探测程序等真实世界的 Darwin 工具。
*   **架构设计：** 由 Mach-O 加载器、系统调用转换运行时以及内置的 `libSystem` 动态库组成，无需用户提供苹果私有的二进制文件 (blobs)。
*   **兼容性：** 已在 Linux aarch64 裸机、虚拟机 (UTM) 和容器 (Docker/Colima) 中经过验证。支持多线程，并提供用于桥接宿主与访客文件系统的“bottle”系统。

**性能与应用场景：**
虽然访客代码以原生速度运行，但系统调用边界（上下文切换与状态保存）会引入额外开销。在多文件压缩等系统调用密集型任务中，Kakehashi 的速度约为原生 Linux 二进制文件的五分之一。然而，对于计算密集型任务，性能差距会显著缩小（仅慢 1.1–1.2 倍）。

其核心价值主张是 **CI/CD 成本优化**。macOS 云端运行节点的成本通常是 Linux ARM 节点的 10–12 倍。即使存在 5 倍的性能损耗，在 Linux 节点上通过 Kakehashi 运行 Darwin 命令行工具的成本仍远低于使用原生 macOS 资源。

**局限性：**
Kakehashi 目前仅是一个“产品切片”，并非 macOS 的完整替代品。它尚不支持 GUI、代码签名、公证或如 `Security.framework` 等复杂的苹果框架。其目标受众是需要在 Linux 基础设施上运行 Darwin 特定命令行工作流的开发者。

---

## 4. RISC OS Open 二十年

**原文标题**: Twenty Years of RISC OS Open

**原文链接**: [https://www.riscosopen.org/news/articles/2026/06/20/twenty-years-of-risc-os-open](https://www.riscosopen.org/news/articles/2026/06/20/twenty-years-of-risc-os-open)

为庆祝 RISC OS Open Limited (ROOL) 成立二十周年，本文记录了这一曾经的专有操作系统转型为蓬勃发展的开源项目的历程。ROOL 成立于 2006 年，旨在向公众开放该操作系统。其发展历程始于共享源码计划，并于 2007 年首次发布了源代码。

过去二十年的重大里程碑包括：
*   **硬件扩展：** 将 RISC OS 5 移植到现代 ARM 硬件，从 BeagleBoard 开始，到 2012 年发布具有里程碑意义的树莓派 (Raspberry Pi) 版本，将该系统带给了新一代用户。
*   **社区参与：** 2010 年推出的奖励计划 (Bounty Scheme) 允许社区为特定功能提供资金支持，而 2019 年迁移至公开的 GitLab 平台则促成了超过一千项协作改进。
*   **全面开源转型：** 2018 年迎来了一个关键转折点，RISC OS 重新以 Apache 2.0 许可证授权，使其可供任何人免费使用并进行商业化开发。
*   **技术现代化：** 该项目持续交付稳定的版本（从 5.20 到 5.30），引入了原生 Git 支持、NVMe 存储兼容性，并更新了完善的文档。

展望未来，ROOL 启动了 **“登月计划” (Moonshots initiative)**。这一雄心勃勃的多年工程计划旨在将 RISC OS 转型至 64 位 ARM 架构，确保在 32 位硬件逐渐被淘汰时，该系统依然保持生命力。文章最后将该操作系统现状的欣欣向荣归功于 ROOL 与全球开发者、测试者及支持者社区的共同努力。

---

## 5. 卡帕斯的鹈鹕

**原文标题**: Karpathy’s Pelican

**原文链接**: [https://twitter.com/karpathy/status/2083749667410727319](https://twitter.com/karpathy/status/2083749667410727319)

在这篇文章中，安德烈·卡帕斯（Andrej Karpathy）探讨了大型语言模型（LLM）不断进化的能力：从简单的提示词操作转向复杂的自主创意任务。他详细介绍了一项实验，他给未来版本的 Claude（Opus 5）提供了 100 万 token 的预算（约 10 美元），并要求它根据《指环王》的第一段内容创建一个 Three.js 渲染。

在两小时内，该模型编写了 5,500 行代码，对故事进行了程序化渲染和动画处理。卡帕斯从这次实验中总结了三个核心启示：

*   **空间推理：** LLM 能够编排复杂的 3D 资产、动画和 (x,y,z) 坐标，从而从零开始构建一个功能完备的环境，这是一个重大的里程碑。
*   **“耐力”转型：** 以前对人类开发者来说过于繁琐或定制化的任务，现在由于 AI 拥有无限的耐心而变得“几乎免费”。这为“瞬态 GTA”（ephemeral GTAs）——即按需生成的、高度定制的虚拟世界——打开了大门，玩家可以作为参与者或旁观者进入任何想象中的故事。
*   **审计瓶颈：** 实验揭示了当前 LLM 的一个核心弱点：缺乏原生的、高效的视频感知能力。由于模型无法直接“运行”其游戏或观看其作品的视频，而只能依赖缓慢的周期性截图，导致最终产品存在瑕疵和错误。

卡帕斯总结道，虽然原生的多模态和游戏审计能力尚不完善，但 LLM 按需构建复杂的定制化世界的能力，标志着生成式 AI 的一次巨大飞跃。

---

## 6. Show HN: NixOS-DGX-Spark – DGX Spark 上的 Nix 和 NixOS

**原文标题**: Show HN: NixOS-DGX-Spark – Nix and NixOS on the DGX Spark

**原文链接**: [https://github.com/graham33/nixos-dgx-spark](https://github.com/graham33/nixos-dgx-spark)

**NixOS-DGX-Spark** 是一个开源项目，旨在将 Nix 软件包管理器和 NixOS 操作系统引入 NVIDIA DGX Spark 和 Asus Ascent GX10 硬件。它提供两种主要工作流：在原生 DGX OS (Ubuntu) 上使用 Nix，或者进行完整的 NixOS 安装。

**核心特性：**
*   **NixOS 模块：** 专用模块提供硬件特定的配置，包括为 DGX Spark 优化的定制版 NVIDIA 内核。该内核确保了全面的 GPU 支持和正常的以太网功能，而这些在标准内核上目前仍存在问题。
*   **DGX 仪表板：** 该模块会自动启用一个基于 Web 的遥测界面（位于 localhost:11000），用于系统监控和 GPU 追踪。
*   **AI Playbooks：** 该仓库包含多个针对 AI 工作负载（如 ComfyUI、vLLM 和 PyTorch 微调）预配置的“方案（Playbooks）”。这些方案分为“Full Nix”（完全可复现的原生环境）和基于容器的工作流。
*   **二进制缓存：** 为了避免 CUDA 相关软件包冗长的编译时间，该项目利用了 Flox 二进制缓存（针对 aarch64-linux CUDA 依赖项）和自定义的 Cachix 缓存。
*   **部署选项：** 用户可以构建 USB 启动镜像或使用快速入门 flake 模板。该项目还支持通过 `nixos-anywhere` 进行实验性的远程安装。

**重要注意事项：**
作者提醒，用户在安装 NixOS 之前必须使用原始 DGX OS 更新系统固件，因为出厂固件可能不支持 NixOS 启动。此外，在 Ubuntu 上使用 Nix 时，需要使用 `nix-gl-host` 工具来桥接 Nix 构建的应用程序与宿主机的 GPU 驱动程序。

总而言之，该项目为管理高性能 NVIDIA 边缘 AI 硬件提供了一个可复现且声明式的框架。

---

## 7. F*：一种通用的面向证明的编程语言

**原文标题**: F*: A general-purpose proof-oriented programming language

**原文链接**: [https://fstar-lang.org/](https://fstar-lang.org/)

F* (pronounced F star) is a general-purpose, proof-oriented programming language designed for both purely functional and effectful programming. It uniquely combines the expressive power of dependent types with advanced proof capabilities, utilizing SMT solving for automation alongside tactic-based interactive theorem proving.

The language is versatile in its compilation, primarily targeting OCaml by default. However, various fragments of F* can also be extracted to F#, C, WebAssembly (via the KaRaMeL tool), or assembly (via the Vale toolchain). 

F* is an open-source project hosted on GitHub. It is implemented in its own language and bootstrapped using OCaml. Development is led by Microsoft Research and Inria, supported by an active community.

---

## 8. Rooting, firmware analysis and persistent credentials of TP-Link TL-841N

**原文标题**: Rooting, firmware analysis and persistent credentials of TP-Link TL-841N

**原文链接**: [https://blog.juni-mp4.com/posts/42/rooting-the-tplink-tl841n-pt1/](https://blog.juni-mp4.com/posts/42/rooting-the-tplink-tl841n-pt1/)

生成摘要时出错

---

## 9. Meshdiff – visually compare two STL versions in the browser, client-side

**原文标题**: Meshdiff – visually compare two STL versions in the browser, client-side

**原文链接**: [https://meshdiff.com/](https://meshdiff.com/)

生成摘要时出错

---

## 10. When transit passes were designed by hand (2022)

**原文标题**: When transit passes were designed by hand (2022)

**原文链接**: [https://letterformarchive.org/news/milwaukee-transit-passes/](https://letterformarchive.org/news/milwaukee-transit-passes/)

生成摘要时出错

---

## 11. Fasttracker II clone in C using SDL 2

**原文标题**: Fasttracker II clone in C using SDL 2

**原文链接**: [https://16-bits.org/ft2.php](https://16-bits.org/ft2.php)

生成摘要时出错

---

## 12. Developers are attached to tools because tools encode trust

**原文标题**: Developers are attached to tools because tools encode trust

**原文链接**: [https://stackoverflow.blog/2026/07/29/developers-are-attached-to-tools-because-tools-encode-trust/](https://stackoverflow.blog/2026/07/29/developers-are-attached-to-tools-because-tools-encode-trust/)

生成摘要时出错

---

## 13. Folding Paper Globes

**原文标题**: Folding Paper Globes

**原文链接**: [https://foldingglobes.com/globes](https://foldingglobes.com/globes)

生成摘要时出错

---

## 14. Linux Desktop Market Share Surpasses 10% in North America

**原文标题**: Linux Desktop Market Share Surpasses 10% in North America

**原文链接**: [https://linuxiac.com/linux-desktop-market-share-surpasses-10-in-north-america/](https://linuxiac.com/linux-desktop-market-share-surpasses-10-in-north-america/)

生成摘要时出错

---

## 15. Show HN: Bor – Open-source policy management for Linux desktops

**原文标题**: Show HN: Bor – Open-source policy management for Linux desktops

**原文链接**: [https://getbor.dev/blog/2026-08-02-bor-v080-release/](https://getbor.dev/blog/2026-08-02-bor-v080-release/)

生成摘要时出错

---

## 16. Show HN: Fuse – statically typed functional programming language

**原文标题**: Show HN: Fuse – statically typed functional programming language

**原文链接**: [https://fuselang.org](https://fuselang.org)

生成摘要时出错

---

## 17. Great Question (YC W21) 招聘高级需求生成经理

**原文标题**: Great Question (YC W21) Is Hiring Senior Demand Gen Manager

**原文链接**: [https://www.ycombinator.com/companies/great-question/jobs/YutDxyf-senior-demand-generation-manager](https://www.ycombinator.com/companies/great-question/jobs/YutDxyf-senior-demand-generation-manager)

Great Question, a Y Combinator-backed (W21) AI customer research platform, is seeking a **Senior Demand Generation Manager** for a remote-first, full-time position. The company provides an all-in-one platform for recruiting participants and sharing research insights, trusted by brands like Canva, Brex, and Gusto.

**The Role and Responsibilities**
The primary objective of this role is to own **SQL (Sales Qualified Lead) attainment**. The manager will build and scale a predictable demand engine across various channels, including organic and AI search (AEO), content, gated assets, and paid acquisition. Positioned within a lean marketing team, the role sits between Product Marketing (which provides messaging) and the Growth Lead (who converts SQLs to pipeline).

Key responsibilities include:
*   Developing and executing multi-channel lead-generation systems.
*   Targeting specific practitioner audiences like UX researchers and product managers.
*   Leveraging AI, automation, and contractors to maximize output without increasing linear headcount.
*   Rigorous data analysis of the marketing funnel (MQL → SQL → SQO) and ROI.

**Candidate Requirements**
The ideal candidate has **5–8 years of B2B SaaS demand generation experience** and a proven track record of hitting pipeline targets. They must be "AI-native," demonstrating a practical ability to use AI tools to significantly increase execution speed. Proficiency in marketing automation (HubSpot, Cargo) and experience marketing to technical audiences are preferred.

**Compensation and Success**
Success in the first year is defined by consistent SQL delivery and the creation of a scalable demand engine. The compensation structure is a **70/30 split** (base salary/variable), with uncapped variable pay tied to quarterly SQL performance. The company offers a culture of high agency, competitive equity, and annual retreats.

---

## 18. Norway Salmon

**原文标题**: Norway Salmon

**原文链接**: [https://www.abc.net.au/news/2026-07-28/how-norway-s-salmon-industry-became-a-global-behemoth/106949872](https://www.abc.net.au/news/2026-07-28/how-norway-s-salmon-industry-became-a-global-behemoth/106949872)

生成摘要时出错

---

## 19. Artificial Intelligence: Ars Notoria and the Promise of Instant Knowledge

**原文标题**: Artificial Intelligence: Ars Notoria and the Promise of Instant Knowledge

**原文链接**: [https://publicdomainreview.org/essay/ars-notoria/](https://publicdomainreview.org/essay/ars-notoria/)

生成摘要时出错

---

## 20. Rust All Hands 2026 Retrospective

**原文标题**: Rust All Hands 2026 Retrospective

**原文链接**: [https://blog.rust-lang.org/inside-rust/2026/07/31/all-hands-2026-retrospective/](https://blog.rust-lang.org/inside-rust/2026/07/31/all-hands-2026-retrospective/)

生成摘要时出错

---

## 21. Go 1.27 Interactive Tour

**原文标题**: Go 1.27 Interactive Tour

**原文链接**: [https://victoriametrics.com/blog/go-1-27/index.html](https://victoriametrics.com/blog/go-1-27/index.html)

生成摘要时出错

---

## 22. Pushes to arch AUR are suspendended right now.

**原文标题**: Pushes to arch AUR are suspendended right now.

**原文链接**: [https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/message/YPJ3FQYJTJXXY3RUXCYLMHUKHLIUNVFF/](https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/message/YPJ3FQYJTJXXY3RUXCYLMHUKHLIUNVFF/)

生成摘要时出错

---

## 23. Show HN: I'm a 15 Year Old Wannabe Engineer, This Is a Cycloidal Gearbox I Built

**原文标题**: Show HN: I'm a 15 Year Old Wannabe Engineer, This Is a Cycloidal Gearbox I Built

**原文链接**: [https://github.com/tom-ilan/cycloidal_gearbox](https://github.com/tom-ilan/cycloidal_gearbox)

生成摘要时出错

---

## 24. Holocloth

**原文标题**: Holocloth

**原文链接**: [https://holocloth.vercel.app](https://holocloth.vercel.app)

生成摘要时出错

---

## 25. Diátaxis

**原文标题**: Diátaxis

**原文链接**: [https://diataxis.fr/](https://diataxis.fr/)

生成摘要时出错

---

## 26. MkLinux and the pimped-out Apple Workgroup Server 9150

**原文标题**: MkLinux and the pimped-out Apple Workgroup Server 9150

**原文链接**: [http://oldvcr.blogspot.com/2026/08/mklinux-and-pimped-out-apple-workgroup.html](http://oldvcr.blogspot.com/2026/08/mklinux-and-pimped-out-apple-workgroup.html)

生成摘要时出错

---

## 27. A Rant About “Technology” (2005)

**原文标题**: A Rant About “Technology” (2005)

**原文链接**: [https://www.ursulakleguin.com/a-rant-about-technology](https://www.ursulakleguin.com/a-rant-about-technology)

生成摘要时出错

---

## 28. Show HN: Syncular – offline-first SQL sync with TypeScript and Rust cores

**原文标题**: Show HN: Syncular – offline-first SQL sync with TypeScript and Rust cores

**原文链接**: [https://github.com/syncular/syncular](https://github.com/syncular/syncular)

生成摘要时出错

---

## 29. Seedance 2.5

**原文标题**: Seedance 2.5

**原文链接**: [https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)

生成摘要时出错

---

## 30. ESP32-C3 SuperMini antenna modification

**原文标题**: ESP32-C3 SuperMini antenna modification

**原文链接**: [https://peterneufeld.wordpress.com/2025/03/04/esp32-c3-supermini-antenna-modification/](https://peterneufeld.wordpress.com/2025/03/04/esp32-c3-supermini-antenna-modification/)

生成摘要时出错

---

## 31. Running Kimi K3 on MI355X at Better Performance per Dollar Than B300

**原文标题**: Running Kimi K3 on MI355X at Better Performance per Dollar Than B300

**原文链接**: [https://www.wafer.ai/blog/kimi-k3-mi355x](https://www.wafer.ai/blog/kimi-k3-mi355x)

生成摘要时出错

---

## 32. The Rise of Million-Dollar Companies with Just One Employee

**原文标题**: The Rise of Million-Dollar Companies with Just One Employee

**原文链接**: [https://www.wsj.com/tech/ai/the-rise-of-million-dollar-companies-with-just-one-employee-f36a77c1](https://www.wsj.com/tech/ai/the-rise-of-million-dollar-companies-with-just-one-employee-f36a77c1)

生成摘要时出错

---

## 33. Show HN: Katharos Functional programming and CSP-style concurrency for Python

**原文标题**: Show HN: Katharos Functional programming and CSP-style concurrency for Python

**原文链接**: [https://github.com/kamalfarahani/katharos](https://github.com/kamalfarahani/katharos)

生成摘要时出错

---

## 34. Cyberscript

**原文标题**: Cyberscript

**原文链接**: [https://cyberscript.dev](https://cyberscript.dev)

生成摘要时出错

---

## 35. Elena, a library for building Progressive Web Components

**原文标题**: Elena, a library for building Progressive Web Components

**原文链接**: [https://elenajs.com/](https://elenajs.com/)

生成摘要时出错

---

## 36. Deep-sea vehicles spot 'alien' sharks deep beneath the waves in the Pacific

**原文标题**: Deep-sea vehicles spot 'alien' sharks deep beneath the waves in the Pacific

**原文链接**: [https://www.science.org/content/article/deep-sea-vehicles-spot-alien-sharks-deep-beneath-waves-pacific#](https://www.science.org/content/article/deep-sea-vehicles-spot-alien-sharks-deep-beneath-waves-pacific#)

生成摘要时出错

---

## 37. ASRock BC-250: Building the Budget Steam Machine

**原文标题**: ASRock BC-250: Building the Budget Steam Machine

**原文链接**: [https://plug-world.com/posts/2026/asrock-bc250-the-budget-steam-machine/](https://plug-world.com/posts/2026/asrock-bc250-the-budget-steam-machine/)

生成摘要时出错

---

## 38. I Learned to Stop Worrying and Love the Mask

**原文标题**: I Learned to Stop Worrying and Love the Mask

**原文链接**: [https://dispatchesfromtheautismwars.substack.com/p/how-i-learned-to-stop-worrying-and](https://dispatchesfromtheautismwars.substack.com/p/how-i-learned-to-stop-worrying-and)

生成摘要时出错

---

## 39. Unraveling the mysteries of habit formation

**原文标题**: Unraveling the mysteries of habit formation

**原文链接**: [https://www.kyoto-u.ac.jp/en/research-news/2026-07-28](https://www.kyoto-u.ac.jp/en/research-news/2026-07-28)

生成摘要时出错

---

## 40. US Treasury undertakes historic intervention in yen market

**原文标题**: US Treasury undertakes historic intervention in yen market

**原文链接**: [https://www.ft.com/content/0f9b2fe7-bde4-4f5f-b49e-93ccb5da9ea8](https://www.ft.com/content/0f9b2fe7-bde4-4f5f-b49e-93ccb5da9ea8)

生成摘要时出错

---

## 41. Galaxy Research Coldcard hack update: 1,158.81 BTC stolen from 2,673 addresses

**原文标题**: Galaxy Research Coldcard hack update: 1,158.81 BTC stolen from 2,673 addresses

**原文链接**: [https://twitter.com/glxyresearch/status/2083560979128820105](https://twitter.com/glxyresearch/status/2083560979128820105)

生成摘要时出错

---

## 42. Peter Principle

**原文标题**: Peter Principle

**原文链接**: [https://en.wikipedia.org/wiki/Peter_principle](https://en.wikipedia.org/wiki/Peter_principle)

生成摘要时出错

---

## 43. Postmortem for Kernel Soundness Bug #14576

**原文标题**: Postmortem for Kernel Soundness Bug #14576

**原文链接**: [https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/)

生成摘要时出错

---

## 44. RFC 10015: Deprecating Obsolete Key Exchange Methods in TLS 1.2 and DTLS 1.2

**原文标题**: RFC 10015: Deprecating Obsolete Key Exchange Methods in TLS 1.2 and DTLS 1.2

**原文链接**: [https://www.rfc-editor.org/rfc/rfc10015.html](https://www.rfc-editor.org/rfc/rfc10015.html)

生成摘要时出错

---

## 45. But can your calculator run Linux?

**原文标题**: But can your calculator run Linux?

**原文链接**: [https://raymii.org/s/articles/But_can_your_calculator_run_Linux.html](https://raymii.org/s/articles/But_can_your_calculator_run_Linux.html)

生成摘要时出错

---

## 46. A big win for Android interoperability

**原文标题**: A big win for Android interoperability

**原文链接**: [https://www.openhomefoundation.org/blog/a-big-win-for-android-interoperability/](https://www.openhomefoundation.org/blog/a-big-win-for-android-interoperability/)

生成摘要时出错

---

## 47. Wikimedia Foundation refuses union recognition, hires union-busting law firm

**原文标题**: Wikimedia Foundation refuses union recognition, hires union-busting law firm

**原文链接**: [https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2026-08-02/News_and_notes](https://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2026-08-02/News_and_notes)

生成摘要时出错

---

## 48. The Prospects for 128 Bit Processors ( John Mashey SGI 1995)

**原文标题**: The Prospects for 128 Bit Processors ( John Mashey SGI 1995)

**原文链接**: [https://yarchive.net/comp/128bit.html](https://yarchive.net/comp/128bit.html)

生成摘要时出错

---

## 49. How Google helped destroy adoption of RSS feeds (2023)

**原文标题**: How Google helped destroy adoption of RSS feeds (2023)

**原文链接**: [https://openrss.org/blog/how-google-helped-destroy-adoption-of-rss-feeds](https://openrss.org/blog/how-google-helped-destroy-adoption-of-rss-feeds)

生成摘要时出错

---

## 50. Show HN: Elevators

**原文标题**: Show HN: Elevators

**原文链接**: [https://john.fun/elevators](https://john.fun/elevators)

生成摘要时出错

---

## 51. Sizeof is surprisingly difficult to parse in C

**原文标题**: Sizeof is surprisingly difficult to parse in C

**原文链接**: [https://sebsite.pw/w/20260802-sizeof.html](https://sebsite.pw/w/20260802-sizeof.html)

生成摘要时出错

---

## 52. Glyphs 4 – the leading Mac font editor

**原文标题**: Glyphs 4 – the leading Mac font editor

**原文链接**: [https://glyphsapp.com](https://glyphsapp.com)

生成摘要时出错

---

## 53. Mozilla's Inaugural 'State of Open Source AI' Report Is Here

**原文标题**: Mozilla's Inaugural 'State of Open Source AI' Report Is Here

**原文链接**: [https://blog.mozilla.org/en/mozilla/mozilla-state-of-open-source-ai-report/](https://blog.mozilla.org/en/mozilla/mozilla-state-of-open-source-ai-report/)

生成摘要时出错

---

## 54. Kenji/Serious Eats – 30-Min Pressure Cooker Pho Ga

**原文标题**: Kenji/Serious Eats – 30-Min Pressure Cooker Pho Ga

**原文链接**: [https://www.seriouseats.com/30-minute-pressure-cooker-pho-ga-recipe](https://www.seriouseats.com/30-minute-pressure-cooker-pho-ga-recipe)

生成摘要时出错

---

## 55. Linux on ESP32

**原文标题**: Linux on ESP32

**原文链接**: [https://github.com/GrieferPig/esp32-s31-linux](https://github.com/GrieferPig/esp32-s31-linux)

生成摘要时出错

---

## 56. NetBSD 11.0

**原文标题**: NetBSD 11.0

**原文链接**: [https://blog.netbsd.org/tnf/entry/netbsd_11_0_released](https://blog.netbsd.org/tnf/entry/netbsd_11_0_released)

生成摘要时出错

---

## 57. We accidentally built an LLVM compiler for Jax

**原文标题**: We accidentally built an LLVM compiler for Jax

**原文链接**: [https://iza.ac/posts/2026/07/accidental-llvm-compiler-for-jax/](https://iza.ac/posts/2026/07/accidental-llvm-compiler-for-jax/)

生成摘要时出错

---

## 58. Nyctography: A substituton cypher by Lewis Carroll

**原文标题**: Nyctography: A substituton cypher by Lewis Carroll

**原文链接**: [https://en.wikipedia.org/wiki/Nyctography](https://en.wikipedia.org/wiki/Nyctography)

生成摘要时出错

---

## 59. The Cipher Behind QSYRUPWD: Reconstructing IBM i Password Hashes

**原文标题**: The Cipher Behind QSYRUPWD: Reconstructing IBM i Password Hashes

**原文链接**: [https://blog.silentsignal.eu/2026/07/28/the-cipher-behind-qsyrupwd-reconstructing-ibm-i-password-hashes/](https://blog.silentsignal.eu/2026/07/28/the-cipher-behind-qsyrupwd-reconstructing-ibm-i-password-hashes/)

生成摘要时出错

---

## 60. Atom is better than RSS, in ways that matter

**原文标题**: Atom is better than RSS, in ways that matter

**原文链接**: [https://chrismorgan.info/atom%3Erss](https://chrismorgan.info/atom%3Erss)

生成摘要时出错

---

## 61. When random.bytes() runs but doesn't work

**原文标题**: When random.bytes() runs but doesn't work

**原文链接**: [https://insider.btcpp.dev/p/when-randombytes-runs-but-doesnt](https://insider.btcpp.dev/p/when-randombytes-runs-but-doesnt)

生成摘要时出错

---

## 62. The tiny holdout building in the middle of Macy’s is back in view

**原文标题**: The tiny holdout building in the middle of Macy’s is back in view

**原文链接**: [https://ephemeralnewyork.wordpress.com/2026/07/27/hidden-by-billboards-for-over-100-years-the-tiny-holdout-building-in-the-middle-of-macys-is-back-in-view/](https://ephemeralnewyork.wordpress.com/2026/07/27/hidden-by-billboards-for-over-100-years-the-tiny-holdout-building-in-the-middle-of-macys-is-back-in-view/)

生成摘要时出错

---

## 63. P[drive failure]: how reliable is your NAS?

**原文标题**: P[drive failure]: how reliable is your NAS?

**原文链接**: [https://khz.ac/low-voltage/drive-failure.html](https://khz.ac/low-voltage/drive-failure.html)

生成摘要时出错

---

## 64. Impro is a handbook for running a cult

**原文标题**: Impro is a handbook for running a cult

**原文链接**: [https://www.seangoedecke.com/impro/](https://www.seangoedecke.com/impro/)

生成摘要时出错

---

## 65. Manual: •.,:;…!?·

**原文标题**: Manual: •.,:;…!?·

**原文链接**: [https://type.today/en/journal/dots](https://type.today/en/journal/dots)

生成摘要时出错

---

## 66. Show HN: Logan Basic v2.1 - An online BASIC interpreter.

**原文标题**: Show HN: Logan Basic v2.1 - An online BASIC interpreter.

**原文链接**: [https://sinusoft.com/loganbasic/](https://sinusoft.com/loganbasic/)

生成摘要时出错

---

## 67. Dark Hours

**原文标题**: Dark Hours

**原文链接**: [https://darkhours.io](https://darkhours.io)

生成摘要时出错

---

## 68. IBM i (OS/400) the Database Operating System

**原文标题**: IBM i (OS/400) the Database Operating System

**原文链接**: [https://osadmins.com/en/ibm-i-os-400-the-database-operating-system/](https://osadmins.com/en/ibm-i-os-400-the-database-operating-system/)

生成摘要时出错

---

## 69. Why are all the amounts values negative?

**原文标题**: Why are all the amounts values negative?

**原文链接**: [https://bankstatementconverter.com/blog/posts/2026-08-02-why-are-all-amounts-negative/](https://bankstatementconverter.com/blog/posts/2026-08-02-why-are-all-amounts-negative/)

生成摘要时出错

---

## 70. A Surveillance Treaty in Disguise: Canada Signs UN Cybercrime Convention

**原文标题**: A Surveillance Treaty in Disguise: Canada Signs UN Cybercrime Convention

**原文链接**: [https://www.michaelgeist.ca/2026/07/a-surveillance-treaty-in-disguise-the-trouble-with-canadas-quiet-decision-to-sign-the-un-cybercrime-convention/](https://www.michaelgeist.ca/2026/07/a-surveillance-treaty-in-disguise-the-trouble-with-canadas-quiet-decision-to-sign-the-un-cybercrime-convention/)

生成摘要时出错

---

## 71. Kubeside – a Kubernetes client that shows your app, not your cluster

**原文标题**: Kubeside – a Kubernetes client that shows your app, not your cluster

**原文链接**: [https://github.com/dynaum/kubeside](https://github.com/dynaum/kubeside)

生成摘要时出错

---

## 72. The Apple Network Server's all-too-secret weapon (featuring PPC Toolbox)

**原文标题**: The Apple Network Server's all-too-secret weapon (featuring PPC Toolbox)

**原文链接**: [http://oldvcr.blogspot.com/2023/11/the-apple-network-servers-all-too.html](http://oldvcr.blogspot.com/2023/11/the-apple-network-servers-all-too.html)

生成摘要时出错

---

## 73. Investigating three real-world incidents in our cybersecurity evaluations

**原文标题**: Investigating three real-world incidents in our cybersecurity evaluations

**原文链接**: [https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals](https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals)

生成摘要时出错

---

## 74. GPUs could explode to multiple TB with new storage-inspired memory tech

**原文标题**: GPUs could explode to multiple TB with new storage-inspired memory tech

**原文链接**: [https://www.theregister.com/storage/2026/07/30/gpus-could-explode-to-multiple-tb-with-new-storage-inspired-memory-tech/5281363](https://www.theregister.com/storage/2026/07/30/gpus-could-explode-to-multiple-tb-with-new-storage-inspired-memory-tech/5281363)

生成摘要时出错

---

## 75. The time filter in Google Search broke a few days ago

**原文标题**: The time filter in Google Search broke a few days ago

**原文链接**: [https://mastodon.online/@mwichary/117023736804129342](https://mastodon.online/@mwichary/117023736804129342)

生成摘要时出错

---

## 76. Solid Queue 1.6.0 now supports fiber workers

**原文标题**: Solid Queue 1.6.0 now supports fiber workers

**原文链接**: [https://github.com/rails/solid_queue/releases/tag/v1.6.0](https://github.com/rails/solid_queue/releases/tag/v1.6.0)

生成摘要时出错

---

## 77. I don't recommend Tailwind CSS

**原文标题**: I don't recommend Tailwind CSS

**原文链接**: [https://en.andros.dev/blog/af3ee191/why-i-dont-recommend-tailwind-css/](https://en.andros.dev/blog/af3ee191/why-i-dont-recommend-tailwind-css/)

生成摘要时出错

---

## 78. AI opens new era in cognitive studies of wild primates

**原文标题**: AI opens new era in cognitive studies of wild primates

**原文链接**: [https://news.emory.edu/features/2026/07/ai-opens-new-era-cognitive-studies-wild-primates](https://news.emory.edu/features/2026/07/ai-opens-new-era-cognitive-studies-wild-primates)

生成摘要时出错

---

## 79. The Burau representation of the braid group is faithful for n = 4

**原文标题**: The Burau representation of the braid group is faithful for n = 4

**原文链接**: [https://arxiv.org/abs/2607.05283](https://arxiv.org/abs/2607.05283)

生成摘要时出错

---

## 80. Show HN: I worked on a new browser for 2 years, today it passed Acid 3

**原文标题**: Show HN: I worked on a new browser for 2 years, today it passed Acid 3

**原文链接**: [https://code.intellios.ai/cwbrowser/](https://code.intellios.ai/cwbrowser/)

生成摘要时出错

---

## 81. Show HN: TamedTable, AI ETL in Natural Language

**原文标题**: Show HN: TamedTable, AI ETL in Natural Language

**原文链接**: [https://www.tamedtable.com/](https://www.tamedtable.com/)

生成摘要时出错

---

## 82. Increasing the lifespan of a bulb makes it worse in every other way

**原文标题**: Increasing the lifespan of a bulb makes it worse in every other way

**原文链接**: [https://maurycyz.com/misc/tungsten/](https://maurycyz.com/misc/tungsten/)

生成摘要时出错

---

## 83. Cursor removed cost information from the usage page and CSV export

**原文标题**: Cursor removed cost information from the usage page and CSV export

**原文链接**: [https://forum.cursor.com/t/usage-page-to-token-amount-what/167153](https://forum.cursor.com/t/usage-page-to-token-amount-what/167153)

生成摘要时出错

---

## 84. The Art of 64-bit Assembly

**原文标题**: The Art of 64-bit Assembly

**原文链接**: [https://nostarch.com/art-64-bit-assembly-v2](https://nostarch.com/art-64-bit-assembly-v2)

生成摘要时出错

---

## 85. qm – Multiplayer agent harness for work

**原文标题**: qm – Multiplayer agent harness for work

**原文链接**: [https://github.com/yc-software/qm](https://github.com/yc-software/qm)

生成摘要时出错

---

## 86. Premier league bans gambling sponsors

**原文标题**: Premier league bans gambling sponsors

**原文链接**: [https://www.footyheadlines.com/2646571793/betting-ban-takes-effect-no-more-gambling-sponsors-in-the-premier-league.html](https://www.footyheadlines.com/2646571793/betting-ban-takes-effect-no-more-gambling-sponsors-in-the-premier-league.html)

生成摘要时出错

---

## 87. AI financial advice is surprisingly good, especially if you ask right questions

**原文标题**: AI financial advice is surprisingly good, especially if you ask right questions

**原文链接**: [https://mitsloan.mit.edu/ideas-made-to-matter/ai-financial-advice-surprisingly-good-especially-if-you-ask-right-questions](https://mitsloan.mit.edu/ideas-made-to-matter/ai-financial-advice-surprisingly-good-especially-if-you-ask-right-questions)

生成摘要时出错

---

## 88. Danube's record low levels force shutdown of Hungary's only nuclear plant

**原文标题**: Danube's record low levels force shutdown of Hungary's only nuclear plant

**原文链接**: [https://www.bbc.com/news/articles/cn0nqv05g0do](https://www.bbc.com/news/articles/cn0nqv05g0do)

生成摘要时出错

---

## 89. Is AI reasoning right for the wrong reasons?

**原文标题**: Is AI reasoning right for the wrong reasons?

**原文链接**: [https://www.quantamagazine.org/is-ai-reasoning-right-for-the-wrong-reasons-20260731/](https://www.quantamagazine.org/is-ai-reasoning-right-for-the-wrong-reasons-20260731/)

生成摘要时出错

---

## 90. Agent4Lease

**原文标题**: Agent4Lease

**原文链接**: [https://agent4lease.com/](https://agent4lease.com/)

生成摘要时出错

---

## 91. Agent4Lease

**原文标题**: Agent4Lease

**原文链接**: [https://agent4lease.com/](https://agent4lease.com/)

生成摘要时出错

---

## 92. Show HN: Btfy – a blockchain that uses weather observations

**原文标题**: Show HN: Btfy – a blockchain that uses weather observations

**原文链接**: [https://github.com/kotagit75/btfy](https://github.com/kotagit75/btfy)

生成摘要时出错

---

## 93. Golang proposal: container/: generic collection types

**原文标题**: Golang proposal: container/: generic collection types

**原文链接**: [https://github.com/golang/go/issues/80590](https://github.com/golang/go/issues/80590)

生成摘要时出错

---

## 94. If technology got better, why did everything get worse?

**原文标题**: If technology got better, why did everything get worse?

**原文链接**: [https://www.sammystraus.com/#if-technology-got-better-why-did-everything-get-worse](https://www.sammystraus.com/#if-technology-got-better-why-did-everything-get-worse)

生成摘要时出错

---

## 95. CISA Alert: Water Sector PLC Targeting

**原文标题**: CISA Alert: Water Sector PLC Targeting

**原文链接**: [https://censys.com/blog/cisa-alert-water-tower-plc-targeting/](https://censys.com/blog/cisa-alert-water-tower-plc-targeting/)

生成摘要时出错

---

## 96. Things I would have done differently (consulting)

**原文标题**: Things I would have done differently (consulting)

**原文链接**: [https://www.revsys.com/tidbits/things-i-would-have-done-differently/](https://www.revsys.com/tidbits/things-i-would-have-done-differently/)

生成摘要时出错

---

## 97. RipGrep musl binaries occasionally segfault during very-large searches

**原文标题**: RipGrep musl binaries occasionally segfault during very-large searches

**原文链接**: [https://github.com/BurntSushi/ripgrep/issues/3494](https://github.com/BurntSushi/ripgrep/issues/3494)

生成摘要时出错

---

## 98. A Uiua Type System (2025)

**原文标题**: A Uiua Type System (2025)

**原文链接**: [https://www.uiua.org/blog/a-uiua-type-system](https://www.uiua.org/blog/a-uiua-type-system)

生成摘要时出错

---

## 99. Anime User Interfaces

**原文标题**: Anime User Interfaces

**原文链接**: [https://animeuserinterface.tumblr.com](https://animeuserinterface.tumblr.com)

生成摘要时出错

---

## 100. Google fixed more Chrome bugs in June than over the past two years, thanks to AI

**原文标题**: Google fixed more Chrome bugs in June than over the past two years, thanks to AI

**原文链接**: [https://blog.google/security/chrome-stronger-with-every-update/](https://blog.google/security/chrome-stronger-with-every-update/)

生成摘要时出错

---

