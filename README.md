# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-02.md)

*最后自动更新时间: 2026-08-02 18:30:52*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 2 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 3 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 4 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 5 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 6 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 7 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 8 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 9 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 10 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 11 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 12 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 13 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 14 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 15 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 16 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 17 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 18 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 19 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 20 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 21 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 22 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 23 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 24 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 25 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 26 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 27 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 28 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 29 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 30 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 31 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 32 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 33 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 34 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 35 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 36 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 37 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 38 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 39 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 40 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 41 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 42 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 43 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 44 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 45 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 46 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 47 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 48 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 49 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 50 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 51 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 52 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 53 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 54 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 55 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 56 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 57 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 58 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 59 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 60 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 61 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 62 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 63 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 64 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 65 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 66 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 67 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 68 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 69 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 70 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 71 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 72 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 73 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 74 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 75 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 76 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 77 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 78 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 79 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 80 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 81 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 82 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 83 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 84 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 85 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 86 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 87 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 88 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 89 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 90 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 91 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 92 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 93 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 94 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 95 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 96 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 97 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 98 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 99 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 100 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 101 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 102 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 103 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 104 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 105 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 106 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 107 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 108 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 109 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 110 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 111 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 112 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 113 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 114 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 115 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 116 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 117 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 118 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 119 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 120 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 121 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 122 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 123 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 124 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 125 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 126 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 127 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 128 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 129 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 130 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 131 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 132 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 133 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 134 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 135 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 136 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 137 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 138 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 139 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 140 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 141 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 142 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 143 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 144 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 145 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 146 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 147 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 148 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 149 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 150 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 151 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 152 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 153 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 154 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 155 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 156 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 157 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 158 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 159 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 160 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 161 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 162 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 163 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 164 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 165 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 166 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 167 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 168 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 169 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 170 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 171 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 172 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 173 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 174 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 175 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 176 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 177 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 178 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 179 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 180 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 181 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 182 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 183 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 184 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 185 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 186 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 187 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 188 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 189 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 190 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 191 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 192 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 193 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 194 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 195 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 196 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 197 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 198 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 199 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 200 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 201 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 202 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 203 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 204 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 205 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 206 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 207 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 208 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 209 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 210 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 211 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 212 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 213 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 214 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 215 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 216 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 217 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 218 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 219 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 220 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 221 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 222 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 223 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 224 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 225 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 226 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 227 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 228 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 229 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 230 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 231 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 232 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 233 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 234 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 235 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 236 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 237 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 238 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 239 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 240 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 241 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 242 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 243 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 244 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 245 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 246 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 247 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 248 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 249 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 250 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 251 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 252 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 253 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 254 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 255 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 256 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 257 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 258 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 259 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 260 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 261 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 262 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 263 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 264 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 265 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 266 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 267 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 268 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 269 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 270 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 271 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 272 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 273 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 274 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 275 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 276 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 277 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 278 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 279 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 280 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 281 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 282 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 283 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 284 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 285 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 286 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 287 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 288 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 289 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 290 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 291 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 292 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 293 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 294 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 295 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 296 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 297 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 298 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 299 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 300 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 301 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 302 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 303 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 304 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 305 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 306 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 307 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 308 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 309 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 310 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 311 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 312 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 313 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 314 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 315 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 316 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 317 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 318 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 319 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 320 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 321 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 322 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 323 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 324 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 325 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 326 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 327 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 328 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 329 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 330 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 331 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 332 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 333 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 334 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 335 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 336 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 337 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 338 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 339 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 340 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 341 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 342 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 343 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 344 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 345 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 346 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 347 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 348 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 349 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 350 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 351 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 352 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 353 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 354 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 355 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 356 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 357 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 358 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 359 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 360 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 361 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 362 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 363 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 364 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 365 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 366 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 367 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 368 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 369 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 370 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 371 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 372 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 373 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 374 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 375 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 376 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 377 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 378 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 379 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 380 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 381 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 382 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 383 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 384 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 385 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 386 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 387 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 388 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 389 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 390 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 391 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 392 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 393 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 394 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 395 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 396 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 397 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 398 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 399 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 400 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 401 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 402 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 403 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 404 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 405 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 406 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 407 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 408 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 409 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 410 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 411 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 412 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 413 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 414 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 415 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 416 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 417 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 418 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 419 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 420 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 421 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 422 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 423 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 424 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 425 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 426 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 427 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 428 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 429 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 430 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 431 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 432 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 433 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 434 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 435 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 436 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 437 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 438 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 439 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 440 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 441 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 442 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 443 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 444 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 445 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 446 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 447 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 448 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 449 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 450 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 451 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 452 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 453 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 454 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 455 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 456 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 457 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 458 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 459 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 460 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 461 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 462 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 463 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 464 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 465 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 466 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 467 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 468 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 469 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 470 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 471 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 472 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 473 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 474 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 475 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 476 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 477 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 478 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 479 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 480 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 481 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 482 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 483 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 484 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 485 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 486 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 487 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 488 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 489 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 490 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 491 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 492 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 493 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 494 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 495 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 496 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 497 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 498 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 499 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 500 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
