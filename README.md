# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-19.md)

*最后自动更新时间: 2026-05-19 19:33:29*
## 1. 我打造了一个虚拟博物馆，几乎涵盖了你能想到的所有操作系统。

**原文标题**: I’ve built a virtual museum with nearly every operating system you can think of

**原文链接**: [https://virtualosmuseum.org/](https://virtualosmuseum.org/)

**虚拟操作系统博物馆**（Virtual OS Museum）是一个全面的软件保存项目，收录了 1,700 多个安装实例和 570 种不同的操作系统。该项目由一名开发者历经 20 年打造，旨在通过消除复杂的模拟器配置和繁琐的安装过程等技术门槛，让用户能够“一键式”体验计算机历史。

该博物馆以 Linux 虚拟机的形式交付，兼容 QEMU、VirtualBox 和 UTM。它内置了一个自定义的、独立于模拟器的启动器，并配有快照系统，方便用户快速回滚损坏的系统环境。其目录涵盖了存储程序计算机的完整历史，从 1948 年的曼彻斯特婴儿机（Manchester Baby）到现代系统。主要亮点包括：

*   **大型机和小型机：** CTSS、Multics、MVS 和早期 IBM 系统。
*   **工作站和 Unix：** SunOS、IRIX、NeXTSTEP、A/UX 以及各种 BSD/Linux 发行版。
*   **家用和个人电脑：** Apple II、Commodore 64、ZX Spectrum、各种 DOS 版本、OS/2、早期 Windows（1.0 到 Longhorn）以及经典 Mac OS。
*   **移动和研究系统：** PalmOS、Symbian、Newton OS、BeOS、Plan 9 和 Smalltalk 环境。

该项目提供两种版本：预装了所有镜像以供离线使用的**完整版**（Full），以及按需下载系统的**精简版**（Lite）。许多系统安装中都包含符合当时时代的应用程序和开发工具，旨在真实还原这些机器当年的使用体验。

创作者持续为博物馆更新新平台和模拟器补丁。用户可以通过 Patreon 和 Ko-fi 支持该项目，社区则可以通过 Discord 和 GitLab 参与贡献。

---

## 2. Apple unveils new accessibility features

**原文标题**: Apple unveils new accessibility features

**原文链接**: [https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/](https://www.apple.com/newsroom/2026/05/apple-unveils-new-accessibility-features-and-updates-with-apple-intelligence/)

Apple has announced a suite of new accessibility features and updates powered by "Apple Intelligence," scheduled for release later in 2026. These advancements leverage on-device AI to enhance tools for users with vision, hearing, and physical disabilities while maintaining Apple’s commitment to privacy.

**Key AI-Powered Updates:**
*   **VoiceOver and Magnifier:** A new "Image Explorer" provides detailed descriptions of onscreen and real-world visual content. Through "Live Recognition," users can press the Action button to ask natural language questions about their surroundings and receive detailed responses.
*   **Voice Control:** Navigation becomes more intuitive with natural language input, allowing users to "say what they see" to interact with app elements without needing exact labels.
*   **Accessibility Reader:** This tool now supports complex documents like scientific articles, offering on-demand summaries and built-in translation while preserving custom formatting.

**New Ecosystem Features:**
*   **Generated Subtitles:** Using on-device speech recognition, the Apple ecosystem can now automatically generate captions for uncaptioned videos, including personal recordings and social media content.
*   **Vision Pro Wheelchair Control:** In a significant mobility update, Apple Vision Pro users can now control compatible power wheelchairs (starting with Tolt and LUCI systems) using precision eye-tracking.
*   **Hikawa Grip & Stand:** A MagSafe adaptive accessory designed for users with limited grip or mobility is now available globally in three new colors.

**Additional Improvements:**
Other updates include "Vehicle Motion Cues" for visionOS to reduce motion sickness, face gesture support for system actions, larger text options for tvOS, and expanded "Name Recognition" support for over 50 languages. Additionally, Apple has added support for the Sony Access game controller across its platforms.

---

## 3. I’ve joined Anthropic

**原文标题**: I’ve joined Anthropic

**原文链接**: [https://twitter.com/karpathy/status/2056753169888334312](https://twitter.com/karpathy/status/2056753169888334312)

生成摘要时出错

---

## 4. Gaussian Splat of a Strawberry

**原文标题**: Gaussian Splat of a Strawberry

**原文链接**: [https://superspl.at/scene/84df8849](https://superspl.at/scene/84df8849)

生成摘要时出错

---

## 5. KV Cache 正在成为推理的存储层次结构。

**原文标题**: KV Cache Is Becoming the Memory Hierarchy of Inference

**原文链接**: [https://touchdown-labs.com/blog/kv-cache-memory-hierarchy-inference.html](https://touchdown-labs.com/blog/kv-cache-memory-hierarchy-inference.html)

Touchdown Labs 的这篇文章指出，随着大语言模型（LLM）迈向海量上下文窗口，**键值（KV）缓存**的管理已成为推理工程的核心瓶颈和重中之重。

KV 缓存存储了先前 Token 的数学表示，以避免文本生成过程中的重复计算。LLM 的权重是静态的，但 KV 缓存会随批次大小和上下文长度线性增长。对于现代长上下文模型，缓存极易超出 GPU 昂贵的高带宽内存（HBM）的容量。

其核心论点是，KV 缓存正演变为一种**多级存储层次结构**，类似于传统 CPU 使用 L1、L2 和 L3 缓存的方式。为攻克这一“内存墙”，业界正采用以下关键策略：

*   **量化 (Quantization)：** 降低 KV 缓存的精度（如从 FP16 降至 8 位或 4 位），从而在同样的内存空间内塞入更多数据。
*   **分页注意力 (PagedAttention)：** 受操作系统虚拟内存启发，该技术（由 vLLM 推广）通过非连续内存块管理 KV 缓存，以消除内存碎片并实现高效共享。
*   **卸载 (Offloading)：** 将“冷”KV 缓存从高速 GPU 显存迁移到速度较慢但成本更低的系统内存（DDR）甚至 NVMe 存储中，仅在必要时换回。
*   **逐出与稀疏化 (Eviction and Sparsity)：** 识别并剔除缓存中“次要”的 Token，在不耗尽内存的前提下维持性能。

作者总结道，LLM 可扩展性的未来不再仅取决于原始算力（FLOPS），而在于对这种 KV 缓存层级的精细编排。能否在不同存储层级间高效调度数据，将是长上下文 AI 应用实现商业落地的决定性因素。

---

## 6. Gentoo 新闻：Copy Fail、Dirty Frag 和 Fragnesia 内核漏洞

**原文标题**: Gentoo News: Copy Fail, Dirty Frag, and Fragnesia Kernel Vulnerabilities

**原文链接**: [https://www.gentoo.org/news/2026/05/19/copy-fail-fragnesia-vulnerabilities.html](https://www.gentoo.org/news/2026/05/19/copy-fail-fragnesia-vulnerabilities.html)

Gentoo Linux has issued an advisory regarding several recent privilege escalation vulnerabilities discovered in the Linux kernel, specifically **Copy Fail**, **Dirty Frag**, and **Fragnesia**. This is part of an increasing trend of rapid vulnerability disclosures that the Gentoo Kernel and Distribution Kernel teams are actively managing through fast-tracked updates and backported mitigations.

Key points include:

*   **Proactive Patching:** While some upstream kernels remain vulnerable to the "Fragnesia" flaw, Gentoo kernels already include the latest v5 patch. 
*   **Security-Supported Packages:** Users are urged to use official security-supported packages, specifically `sys-kernel/gentoo-kernel`, `sys-kernel/gentoo-kernel-bin`, or `sys-kernel/gentoo-sources`. 
*   **Vulnerable Versions:** The `vanilla-kernel` packages and other minor kernel variants are currently vulnerable or slower to receive updates.
*   **Recommendations:** Gentoo strongly advises users to automate their kernel upgrade process and run the latest versions (either ~arch or the newest stable LTS). This is necessary because upstream developers do not reliably backport security fixes to older kernel versions. 

Overall, the distribution emphasizes staying current with official Gentoo-maintained kernels to mitigate these evolving privilege escalation risks.

---

## 7. Gemini 3.5 Flash: frontier intelligence with action

**原文标题**: Gemini 3.5 Flash: frontier intelligence with action

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)

生成摘要时出错

---

## 8. Show HN: Superlog (YC P26) – Observability that installs itself and fixes bugs

**原文标题**: Show HN: Superlog (YC P26) – Observability that installs itself and fixes bugs

**原文链接**: [https://superlog.sh/](https://superlog.sh/)

生成摘要时出错

---

## 9. CISA Admin Leaked AWS GovCloud Keys on GitHub

**原文标题**: CISA Admin Leaked AWS GovCloud Keys on GitHub

**原文链接**: [https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/](https://krebsonsecurity.com/2026/05/cisa-admin-leaked-aws-govcloud-keys-on-github/)

生成摘要时出错

---

## 10. Intro to TLA+ for the LLM Era: Prompt Your Way to Victory

**原文标题**: Intro to TLA+ for the LLM Era: Prompt Your Way to Victory

**原文链接**: [https://emptysqua.re/blog/intro-to-tla-plus-for-the-llm-era/](https://emptysqua.re/blog/intro-to-tla-plus-for-the-llm-era/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 2 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 3 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 4 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 5 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 6 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 7 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 8 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 9 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 10 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 11 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 12 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 13 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 14 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 15 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 16 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 17 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 18 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 19 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 20 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 21 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 22 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 23 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 24 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 25 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 26 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 27 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 28 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 29 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 30 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 31 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 32 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 33 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 34 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 35 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 36 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 37 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 38 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 39 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 40 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 41 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 42 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 43 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 44 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 45 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 46 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 47 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 48 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 49 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 50 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 51 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 52 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 53 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 54 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 55 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 56 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 57 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 58 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 59 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 60 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 61 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 62 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 63 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 64 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 65 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 66 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 67 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 68 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 69 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 70 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 71 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 72 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 73 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 74 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 75 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 76 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 77 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 78 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 79 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 80 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 81 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 82 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 83 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 84 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 85 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 86 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 87 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 88 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 89 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 90 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 91 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 92 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 93 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 94 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 95 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 96 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 97 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 98 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 99 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 100 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 101 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 102 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 103 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 104 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 105 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 106 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 107 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 108 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 109 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 110 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 111 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 112 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 113 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 114 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 115 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 116 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 117 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 118 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 119 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 120 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 121 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 122 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 123 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 124 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 125 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 126 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 127 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 128 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 129 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 130 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 131 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 132 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 133 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 134 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 135 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 136 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 137 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 138 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 139 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 140 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 141 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 142 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 143 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 144 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 145 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 146 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 147 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 148 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 149 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 150 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 151 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 152 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 153 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 154 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 155 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 156 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 157 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 158 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 159 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 160 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 161 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 162 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 163 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 164 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 165 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 166 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 167 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 168 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 169 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 170 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 171 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 172 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 173 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 174 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 175 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 176 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 177 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 178 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 179 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 180 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 181 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 182 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 183 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 184 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 185 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 186 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 187 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 188 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 189 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 190 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 191 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 192 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 193 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 194 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 195 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 196 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 197 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 198 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 199 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 200 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 201 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 202 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 203 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 204 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 205 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 206 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 207 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 208 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 209 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 210 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 211 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 212 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 213 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 214 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 215 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 216 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 217 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 218 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 219 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 220 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 221 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 222 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 223 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 224 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 225 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 226 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 227 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 228 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 229 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 230 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 231 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 232 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 233 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 234 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 235 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 236 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 237 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 238 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 239 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 240 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 241 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 242 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 243 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 244 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 245 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 246 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 247 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 248 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 249 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 250 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 251 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 252 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 253 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 254 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 255 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 256 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 257 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 258 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 259 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 260 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 261 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 262 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 263 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 264 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 265 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 266 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 267 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 268 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 269 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 270 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 271 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 272 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 273 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 274 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 275 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 276 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 277 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 278 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 279 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 280 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 281 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 282 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 283 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 284 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 285 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 286 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 287 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 288 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 289 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 290 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 291 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 292 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 293 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 294 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 295 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 296 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 297 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 298 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 299 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 300 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 301 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 302 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 303 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 304 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 305 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 306 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 307 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 308 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 309 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 310 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 311 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 312 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 313 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 314 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 315 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 316 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 317 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 318 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 319 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 320 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 321 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 322 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 323 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 324 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 325 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 326 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 327 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 328 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 329 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 330 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 331 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 332 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 333 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 334 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 335 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 336 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 337 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 338 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 339 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 340 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 341 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 342 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 343 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 344 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 345 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 346 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 347 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 348 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 349 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 350 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 351 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 352 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 353 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 354 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 355 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 356 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 357 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 358 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 359 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 360 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 361 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 362 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 363 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 364 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 365 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 366 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 367 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 368 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 369 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 370 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 371 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 372 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 373 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 374 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 375 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 376 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 377 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 378 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 379 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 380 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 381 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 382 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 383 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 384 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 385 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 386 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 387 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 388 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 389 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 390 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 391 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 392 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 393 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 394 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 395 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 396 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 397 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 398 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 399 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 400 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 401 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 402 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 403 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 404 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 405 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 406 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 407 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 408 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 409 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 410 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 411 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 412 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 413 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 414 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 415 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 416 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 417 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 418 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 419 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 420 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 421 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 422 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 423 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 424 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 425 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
