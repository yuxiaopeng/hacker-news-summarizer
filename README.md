# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-03.md)

*最后自动更新时间: 2026-04-03 18:07:30*
## 1. Show HN：我为个人博客开发了一个首页

**原文标题**: Show HN: I built a frontpage for personal blogs

**原文链接**: [https://text.blogosphere.app/](https://text.blogosphere.app/)

**Blogosphere** 是一个全新的网络平台，旨在成为“独立网络”（indie web）的中心发现枢纽。作为个人博客的首页，它汇集了来自各行各业独立创作者的最新博文，其风格类似于 Hacker News 等新闻聚合器。

该平台将内容划分为多个专业类别，包括：
*   **科技与科学：** 涵盖人工智能、编程和硬件领域。
*   **生活与个人：** 日常生活更新、日志和“数字花园”。
*   **艺术与文化：** 摄影、设计、美食和流行文化。
*   **社会与经济：** 时事分析和经济趋势。

界面以时间顺序呈现文章流，其中既包括 *Stratechery*、*Kottke.org* 和 *Simon Willison* 等知名独立媒体的内容，也包含较小的个人日志和微博客。每条信息都列出了文章标题、来源域名、博客名称以及时间戳。

通过为去中心化内容提供一个经过筛选、易于导航的目录，Blogosphere 旨在重振个人博客的可见性，并帮助读者发现那些往往被主流社交媒体算法所埋没的高质量、非企业化创作。

---

## 2. iNaturalist

**原文标题**: iNaturalist

**原文链接**: [https://www.inaturalist.org/](https://www.inaturalist.org/)

**iNaturalist** 是一个全球性的社交网络和移动平台，旨在让自然爱好者记录、分享和讨论生物多样性观测结果。它在业余博物学家与科学界之间架起了一座桥梁，将随意的户外发现转化为有价值的研究数据。

该平台的操作流程分为简单的三个步骤：
1. **记录：** 用户拍摄生物照片，涵盖从常见的杂草到稀有的野生动植物。
2. **分享：** 观测记录被上传至云端数据库。
3. **讨论：** 社区成员和专家通过众包方式提供鉴定建议，以核实发现的物种。

**主要科学影响：**
收集的数据会共享至全球生物多样性信息网络（GBIF）等全球科学数据库。这有助于科学家和资源管理人员追踪物种分布、了解物候学（生物季节性现象），并监测生物多样性的健康状况。

**主要功能：**
* **公民科学：** 用户可以加入或发起特定项目，并举办“生物闪查”（Bioblitz）活动来调查当地的野生动植物。
* **专家连接：** 初学者可以获得专家的鉴定帮助。
* **离线功能：** 移动应用程序支持在没有蜂窝网络或 Wi-Fi 的偏远地区记录数据。
* **个人追踪：** 用户可以维护一份记录自己所遇生物的数字化“生命清单”。

iNaturalist 支持数十种语言并在全球范围内使用，它让任何拥有智能手机的人都能为全球保护事业做出贡献，并深化对自然世界的理解。

---

## 3. 三星 Magician 磁盘工具卸载需 18 个步骤和两次重启

**原文标题**: Samsung Magician disk utility takes 18 steps and two reboots to uninstall

**原文链接**: [https://chalmovsky.com/2026/03/29/samsung-magician.html](https://chalmovsky.com/2026/03/29/samsung-magician.html)

本文描述了一位用户在 macOS 上卸载“Samsung Magician”的惨痛经历。该过程最终耗费了 18 个步骤，并需两次重启进入恢复模式。作者最初安装该工具是为了在三星 T7 Shield SSD 上启用硬件加密，但因软件无法正常工作，作者决定将其卸载。

作者详细说明了该软件存在的几个主要问题：

*   **缺乏卸载程序：** 三星未提供标准的卸载程序或“拖入废纸篓”卸载的功能。隐藏在应用包中的官方“清理”脚本也以失败告终，因为它尝试以 macOS 拦截的方式更改文件所有权，导致产生数百个错误且未能实际删除文件。
*   **极难清除：** 尽管针对各种系统文件夹（Caches、Application Support、LaunchAgents）多次手动执行 `rm -rf` 命令，仍有数十个文件隐藏在系统目录中，包括失效的驱动程序和安装包回执。
*   **SIP 障碍：** 最后剩下的八个内核扩展文件受系统完整性保护（SIP）机制保护。为了删除它们，作者不得不进入恢复模式以禁用 SIP，重启后删除文件，然后再回到恢复模式重新启用 SIP。
*   **过度臃肿：** 作者批评了该应用的内部架构，指出其简单的界面竟使用了完整的 Electron/Chromium 框架。软件内包含数百张用于简单旋转动画的 PNG 图片、横幅广告、冗余的自定义字体以及不必要的响应式编程框架。

最后，作者将 Samsung Magician 形容为一种“毒瘤”和“臃肿的奇观”，将一个简单的磁盘工具变成了用户沉重的技术负担。

---

## 4. 使用 QEMU 进行大端测试

**原文标题**: Big-Endian Testing with QEMU

**原文链接**: [https://www.hanshq.net/big-endian-qemu.html](https://www.hanshq.net/big-endian-qemu.html)

本文介绍了如何使用 QEMU 用户模式模拟测试软件在大端（big-endian）系统上的兼容性。

**核心概念**
字节序是指字节在内存中的存储顺序。**小端序**（如 x86_64 和 ARM）优先存储最低有效字节，而**大端序**（如 MIPS 和 IBM z/Architecture）则优先存储最高有效字节。尽管现代硬件大多采用小端序，但开发者仍需确保代码在两种架构之间保持可移植性。

**解决方案**
由于普通开发者很难接触到物理大端硬件，作者建议使用 **QEMU** 和 **GCC 交叉编译器**。这使得开发者可以直接在本地 Linux 机器上编译并运行针对不同架构的二进制文件。

**方法论**
作者通过一个 C 程序演示了该过程，该程序用于打印 32 位整数（`0x12345678`）的各个字节：
1. **本地测试**：在标准小端机器上，程序按反向顺序输出字节（`0x78`、`0x56`、`0x34`、`0x12`）。
2. **跨平台测试**：通过安装 `qemu-user` 以及 MIPS 或 s390x 交叉编译器（`gcc-mips-linux-gnu` 或 `gcc-s390x-linux-gnu`），专门为这些架构编译代码。
3. **模拟**：通过 `qemu-mips` 或 `qemu-s390x` 运行生成的静态二进制文件，即可得到大端序输出（`0x12`、`0x34`、`0x56`、`0x78`）。

最终，QEMU 提供了一种简单且易于获取的方法，无需专用硬件即可验证软件是否正确处理字节序。

---

## 5. 2026年4月：在 Mac mini 上部署 Ollama 与 Gemma 4 26B 的简明指南

**原文标题**: April 2026 TLDR Setup for Ollama and Gemma 4 26B on a Mac mini

**原文链接**: [https://gist.github.com/greenstevester/fc49b4e60a4fef9effc79066c1033ae5](https://gist.github.com/greenstevester/fc49b4e60a4fef9effc79066c1033ae5)

这份 2026 年 4 月的指南提供了一套简化的设置流程，用于在 Apple Silicon Mac mini 上运行 Ollama 和谷歌的 Gemma 4 模型。

**核心建议与硬件**
该指南强调在配备 24GB 统一内存的机器上使用 **Gemma 4 8B** 模型（约 9.6GB）。虽然该模型也有 26B 版本，但其消耗约 17GB 的内存，会导致系统不稳定及剧烈的内存交换。8B 版本则能提供更流畅的体验，并为 macOS 和并发任务留出充足的余量。

**安装与配置**
*   **安装：** 通过 Homebrew 使用 `brew install --cask ollama-app` 进行安装。
*   **自动化：** 为了确保模型随时可用，用户应启用“登录时启动”，并创建一个 macOS 启动代理（`.plist`），以便在开机时将模型预加载到内存中。
*   **持久性：** 默认情况下，Ollama 会在五分钟后卸载模型。通过设置环境变量 `OLLAMA_KEEP_ALIVE="-1"` 可使模型保持无限期加载。

**Ollama v0.19+ 的新特性**
指南重点介绍了 2026 年发布的几项显著提升性能的更新：
*   **原生 MLX 后端：** Ollama 现在自动使用苹果的 MLX 框架，为 M1 至 M5 芯片提供大幅加速。
*   **高级缓存：** 全新的“智能检查点”和更明智的驱逐策略减少了提示词的处理时间及内存占用，这对 Claude Code 等智能体工具尤为有利。
*   **NVFP4 支持：** 对英伟达 NVFP4 格式的支持，允许用户在降低内存需求的同时保持高精度，使本地开发与生产环境保持一致。

文章最后提供了必要的命令行（CLI）指令和 API 说明，以便通过 `localhost:11434` 将 Gemma 4 集成到编程工作流中。

---

## 6. Show HN：用于向量检索的 TurboQuant —— 2-4 位压缩

**原文标题**: Show HN: TurboQuant for vector search – 2-4 bit compression

**原文链接**: [https://github.com/RyanCodrai/py-turboquant](https://github.com/RyanCodrai/py-turboquant)

**TurboQuant** is an unofficial Rust implementation (with Python bindings) of a Google Research paper (ICLR 2026) designed for efficient vector search. It specializes in compressing high-dimensional vectors to just **2–4 bits per coordinate**, achieving up to 16x compression with near-optimal distortion.

**Key Technical Features:**
*   **Data-Oblivious Indexing:** Unlike traditional methods like Product Quantization (PQ) in FAISS, TurboQuant requires **zero training**. It uses a random rotation to transform any input data into a predictable Gaussian distribution, allowing for precomputed Lloyd-Max scalar quantization.
*   **Zero Indexing Time:** Because there is no training phase, the index build is 3–4x faster than FAISS. It is "online" by design, meaning new vectors can be added dynamically without rebuilding the index.
*   **High Performance:** 
    *   **ARM (Apple Silicon):** Matches or exceeds FAISS speed while providing superior recall at 4-bit compression.
    *   **x86 (Intel/AMD):** Performs within 18–25% of FAISS speed but maintains higher recall (e.g., 0.955 vs. 0.930 for OpenAI DBpedia d=1536).
*   **SIMD Optimization:** The search pipeline utilizes highly optimized SIMD kernels—NEON for ARM and AVX2 for x86—using nibble-split lookup tables for high-throughput scoring without full decompression.

**Architecture and Usage:**
The project consists of a core Rust crate (`turbovec`) and a thin PyO3 wrapper for Python. It is particularly effective for high-dimensional embeddings, such as those from OpenAI (d=1536 or d=3072), where it maintains near-perfect recall (k=4) even at high compression ratios. By stripping vector norms and applying Lloyd-Max quantization to the rotated coordinates, it achieves distortion within 2.7x of the Shannon information-theoretic limit.

---

## 7. A Recipe for Steganogravy

**原文标题**: A Recipe for Steganogravy

**原文链接**: [https://theo.lol/python/ai/steganography/seo/recipes/2026/03/27/a-recipe-for-steganogravy.html](https://theo.lol/python/ai/steganography/seo/recipes/2026/03/27/a-recipe-for-steganogravy.html)

生成摘要时出错

---

## 8. If you're running OpenClaw, you probably got hacked in the last week

**原文标题**: If you're running OpenClaw, you probably got hacked in the last week

**原文链接**: [https://old.reddit.com/r/sysadmin/comments/1sbdw29/if_youre_running_openclaw_you_probably_got_hacked/](https://old.reddit.com/r/sysadmin/comments/1sbdw29/if_youre_running_openclaw_you_probably_got_hacked/)

生成摘要时出错

---

## 9. We replaced RAG with a virtual filesystem for our AI documentation assistant

**原文标题**: We replaced RAG with a virtual filesystem for our AI documentation assistant

**原文链接**: [https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant](https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant)

生成摘要时出错

---

## 10. SSH certificates: the better SSH experience

**原文标题**: SSH certificates: the better SSH experience

**原文链接**: [https://jpmens.net/2026/04/03/ssh-certificates-the-better-ssh-experience/](https://jpmens.net/2026/04/03/ssh-certificates-the-better-ssh-experience/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 2 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 3 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 4 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 5 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 6 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 7 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 8 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 9 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 10 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 11 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 12 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 13 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 14 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 15 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 16 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 17 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 18 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 19 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 20 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 21 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 22 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 23 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 24 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 25 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 26 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 27 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 28 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 29 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 30 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 31 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 32 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 33 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 34 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 35 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 36 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 37 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 38 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 39 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 40 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 41 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 42 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 43 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 44 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 45 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 46 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 47 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 48 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 49 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 50 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 51 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 52 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 53 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 54 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 55 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 56 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 57 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 58 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 59 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 60 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 61 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 62 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 63 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 64 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 65 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 66 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 67 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 68 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 69 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 70 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 71 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 72 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 73 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 74 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 75 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 76 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 77 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 78 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 79 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 80 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 81 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 82 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 83 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 84 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 85 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 86 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 87 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 88 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 89 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 90 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 91 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 92 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 93 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 94 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 95 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 96 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 97 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 98 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 99 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 100 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 101 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 102 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 103 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 104 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 105 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 106 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 107 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 108 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 109 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 110 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 111 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 112 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 113 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 114 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 115 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 116 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 117 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 118 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 119 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 120 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 121 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 122 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 123 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 124 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 125 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 126 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 127 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 128 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 129 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 130 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 131 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 132 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 133 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 134 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 135 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 136 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 137 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 138 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 139 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 140 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 141 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 142 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 143 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 144 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 145 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 146 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 147 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 148 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 149 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 150 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 151 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 152 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 153 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 154 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 155 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 156 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 157 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 158 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 159 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 160 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 161 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 162 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 163 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 164 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 165 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 166 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 167 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 168 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 169 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 170 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 171 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 172 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 173 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 174 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 175 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 176 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 177 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 178 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 179 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 180 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 181 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 182 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 183 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 184 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 185 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 186 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 187 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 188 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 189 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 190 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 191 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 192 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 193 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 194 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 195 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 196 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 197 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 198 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 199 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 200 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 201 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 202 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 203 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 204 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 205 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 206 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 207 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 208 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 209 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 210 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 211 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 212 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 213 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 214 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 215 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 216 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 217 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 218 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 219 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 220 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 221 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 222 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 223 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 224 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 225 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 226 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 227 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 228 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 229 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 230 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 231 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 232 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 233 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 234 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 235 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 236 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 237 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 238 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 239 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 240 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 241 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 242 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 243 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 244 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 245 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 246 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 247 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 248 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 249 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 250 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 251 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 252 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 253 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 254 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 255 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 256 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 257 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 258 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 259 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 260 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 261 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 262 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 263 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 264 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 265 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 266 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 267 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 268 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 269 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 270 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 271 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 272 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 273 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 274 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 275 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 276 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 277 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 278 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 279 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 280 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 281 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 282 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 283 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 284 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 285 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 286 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 287 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 288 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 289 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 290 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 291 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 292 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 293 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 294 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 295 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 296 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 297 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 298 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 299 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 300 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 301 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 302 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 303 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 304 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 305 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 306 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 307 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 308 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 309 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 310 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 311 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 312 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 313 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 314 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 315 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 316 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 317 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 318 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 319 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 320 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 321 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 322 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 323 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 324 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 325 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 326 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 327 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 328 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 329 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 330 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 331 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 332 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 333 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 334 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 335 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 336 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 337 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 338 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 339 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 340 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 341 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 342 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 343 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 344 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 345 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 346 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 347 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 348 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 349 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 350 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 351 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 352 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 353 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 354 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 355 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 356 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 357 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 358 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 359 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 360 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 361 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 362 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 363 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 364 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 365 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 366 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 367 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 368 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 369 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 370 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 371 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 372 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 373 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 374 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 375 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 376 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 377 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 378 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 379 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
