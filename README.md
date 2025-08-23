# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-23.md)

*最后自动更新时间: 2025-08-23 17:44:09*
## 1. 构建 A16Z 的个人 AI 工作站

**原文标题**: Building A16Z's Personal AI Workstation

**原文链接**: [https://a16z.com/building-a16zs-personal-ai-workstation-with-four-nvidia-rtx-6000-pro-blackwell-max-q-gpus/](https://a16z.com/building-a16zs-personal-ai-workstation-with-four-nvidia-rtx-6000-pro-blackwell-max-q-gpus/)

a16z 的这篇文章详细介绍了高性能个人AI工作站的创建，该工作站专为研究人员、创始人、开发者和工程师设计，用于处理大型AI模型。该工作站优先考虑本地计算能力，用于训练、微调和推理等任务，以最大限度地减少延迟、最大化控制并确保数据隐私，同时避免基于云的解决方案的复杂性。

该系统的核心是四个 NVIDIA RTX 6000 Pro Blackwell Max-Q GPU，总共提供 384GB 的 VRAM。这种设置确保每个 GPU 都有完整的 PCIe 5.0 x16 带宽，这对于最大化 GPU 到 CPU 的数据传输至关重要。它还拥有 8TB 的 NVMe 5.0 存储，可以在 RAID 0 中配置，以实现极快的数据访问。256GB 的 ECC DDR5 RAM 完善了内存功能。

该工作站由 AMD Ryzen Threadripper PRO 7975WX CPU 提供支持。尽管功能强大，但整个系统仅消耗 1650W 的功率，并且可以放在桌子下面，可以在标准的 15 安培/120V 电路中运行。该构建旨在潜在地支持 NVIDIA GPUDirect Storage (GDS)，用于从 NVMe SSD 直接将数据流式传输到 GPU VRAM，从而进一步减少延迟。

该工作站的预期用例包括训练大型语言模型 (LLM)、运行多模态推理、试验模型并行性以及流式传输用于强化学习的高吞吐量数据集。它旨在为 AI 开发提供一个独立的自我环境，消除云依赖。

---

## 2. RFC 9839 与错误的 Unicode

**原文标题**: RFC 9839 and Bad Unicode

**原文链接**: [https://www.tbray.org/ongoing/When/202x/2025/08/14/RFC9839](https://www.tbray.org/ongoing/When/202x/2025/08/14/RFC9839)

蒂姆·布雷的文章讨论了 RFC 9839，这是一份与保罗·霍夫曼合著的文档，旨在解决数据结构和协议（特别是文本字段）中“不良 Unicode”字符的问题。 虽然 Unicode 本身是有益的，但某些字符可能会因其含义模糊、存在滥用可能或与不同编程语言和系统不兼容而导致问题。

RFC 9839 识别了诸如控制字符（例如，U+0089）、未配对代理项（与 UTF-16 编码相关）和非字符（例如，U+7FFFF）等有问题的字符类。 RFC 提供了 Unicode 的三个“不那么糟糕”的子集，开发人员可以选择从其文本字段中排除有问题的字符，旨在提高互操作性并防止意外行为。

作者认为，虽然像 JSON 这样的标准在技术上允许这些有问题的字符，但明确排除它们是一种很好的做法。 他将 RFC 9839 与更全面但复杂的 PRECIS 框架 (RFC 8264) 进行了对比，认为 9839 的简单性使其更有可能被采用。

布雷还提供了一个 Go 语言库，用于针对指定的子集验证文本字段。 他包含一个表格，比较了各种数据格式和标准（CBOR、I-JSON、JSON、Protobufs、TOML、XML、YAML）如何处理代理项、旧控制字符和非字符。 他最后反思了与传统工作组方法相比，通过个人提交创建 RFC 所面临的挑战。 该 RFC 旨在为开发人员提供一个实用的解决方案来处理其应用程序中有问题的 Unicode。

---

## 3. 使用CUDA C++编写适用于5090的光速闪存注意力

**原文标题**: Writing Speed-of-Light Flash Attention for 5090 in CUDA C++

**原文链接**: [https://gau-nernst.github.io/fa-5090/](https://gau-nernst.github.io/fa-5090/)

本文详细介绍了作者使用CUDA C++为NVIDIA 5090 GPU实现Flash Attention的历程。目标是学习CUDA C++ attention实现，特别是Triton中不可用的特性，例如sm120的MXFP8/NVFP4 MMA。

作者首先概述了Flash Attention 2算法，使用类似Python的表示，并专注于基于tile的处理，其中tile_Q使用寄存器内存。实现过程包括使用`cp.async`将数据从全局内存加载到共享内存，然后使用`ldmatrix`从共享内存加载到寄存器内存，最后使用`mma.m16n8k16`进行MMA（矩阵乘法和累加）。

第一个版本（v1）是一个基本的实现，侧重于正确性，放弃了共享内存混洗和流水线优化等。它强调了数据传输过程，包括关于合并内存访问、共享内存地址以及使用`__syncthreads()`进行同步的详细信息。作者解释了如何对warp进行分区以处理tile_Q的部分，以及使用`ldmatrix`加载数据进行MMA时的布局要求。文章的最终版本展示了一个CUDA内核草案，其中包含核心逻辑，包括加载、MMA和写入输出，并指出在线softmax将在后续版本中介绍。提供了性能基准，展示了后续版本中包括各种优化（例如共享内存混洗和流水线优化）后的改进。

---

## 4. Manim：解释性数学视频动画引擎

**原文标题**: Manim: Animation engine for explanatory math videos

**原文链接**: [https://github.com/3b1b/manim](https://github.com/3b1b/manim)

Manim是一个基于Python的动画引擎，最初由3Blue1Brown开发，用于创建解释性数学视频。它有两个版本：原始版本（ManimGL）和一个社区维护的分支（Manim Community）。本文档重点介绍ManimGL。

要安装ManimGL，需要Python 3.7或更高版本，以及FFmpeg、OpenGL，可选地还需要LaTeX。可以通过`pip install manimgl`进行安装。针对Linux、Windows和Mac OSX提供了具体说明，包括安装FFmpeg、LaTeX（Windows推荐MiKTeX，Mac推荐brew）和Cairo（适用于基于ARM的Mac）等依赖项的详细信息。还提供了Anaconda环境的安装说明。

本文档解释了如何运行Manim并查看示例，使用命令`manimgl example_scenes.py OpeningManimExample`。它列出了用于控制输出和播放的有用命令行标志，例如`-w`用于写入文件，`-s`用于显示最后一帧，以及`-n`用于跳过动画。它还提到了用于配置的`custom_config.yml`，允许自定义输出路径、样式和视频质量。

文档可在3b1b.github.io/manim上找到，中文版本位于docs.manim.org.cn。欢迎贡献，特别是向更活跃的社区版本贡献。该项目采用MIT许可。

---

## 5. Librebox：一款开源的、兼容 Roblox 的游戏引擎

**原文标题**: Librebox: An open source, Roblox-compatible game engine

**原文链接**: [https://github.com/librebox-devs/librebox-demo](https://github.com/librebox-devs/librebox-demo)

Librebox 是一个开源游戏引擎，旨在实现与 Roblox 的兼容性，允许 Luau 代码独立于 Roblox 平台运行。其目标是让开发者在利用现有 Lua 技能的同时，掌控自己的游戏和平台。目前处于演示阶段，Librebox 支持基本的场景渲染、光照、部件、相机移动和核心数据类型。它还实现了 Instance API 的大部分以及客户端服务，如 Workspace 和 RunService。Luau 脚本支持包含任务调度器和协程。

未来计划包括集成 UserInputService、StarterPlayer、物理引擎、网格支持、game.Players、GUI，并最终实现服务器功能的复制。该引擎的开发考虑了跨平台兼容性，首先从 Windows 开始。

Librebox 与 Roblox 无关，不使用任何 Roblox 的源代码或资产。该项目旨在提供一个完全开源的替代方案，首先提供完整的客户端兼容性，然后提供服务器功能。它使用 Luau（MIT 许可）和 raylib（zlib/libpng 许可）。可以从项目页面下载版本，并且该引擎提供用于配置的命令行参数。

---

## 6. 重新思考用于机密虚拟机的 Linux 云堆栈

**原文标题**: Rethinking the Linux cloud stack for confidential VMs

**原文链接**: [https://lwn.net/Articles/1030818/](https://lwn.net/Articles/1030818/)

LWN.net的这篇文章讨论了在Linux云环境中实现机密虚拟机所面临的挑战和解决方案。机密计算旨在保护客户虚拟机内存，即使是hypervisor也无法访问，从而增强隐私，但也与I/O直通等性能优化工作产生冲突。

文章强调了安全与性能之间的权衡，其中为了速度而卸载I/O会通过降低可见性以及对硬件和固件的依赖性来牺牲安全性。一个潜在的解决方案是使用AMD的SEV-TIO和TDISP标准等技术将机密计算扩展到设备本身，从而实现安全通信和DMA到加密的VM内存，避免降低性能的bounce buffer。

文章随后深入探讨了整个Linux云堆栈中需要的更改，首先是安全启动。它解释了这个过程、安全虚拟机服务模块(SVSM)的引入，以及涉及Attester、Verifier和Endorser的远程证明过程，以确保平台完整性。文章提到了不同的机密计算方法，例如微软的LVBS，以及对它们的权衡进行共享理解的必要性。

文章讨论了运行时开销，例如DRAM加密/解密以及接受内存页的过程。扩展也是一个挑战，受到可用地址空间标识符(ASID)数量等因素的限制。文章最后考虑了对交换内存、网络通信、实时迁移等功能的影响，并强调机密计算正在改变Linux云环境中的信任模型，加深对硬件和固件供应商的依赖。

---

## 7. Bild AI (YC W25) 招聘应用人工智能创始工程师

**原文标题**: Bild AI (YC W25) Is Hiring Applied AI Founding Engineer

**原文链接**: [https://www.workatastartup.com/jobs/75647](https://www.workatastartup.com/jobs/75647)

Bild AI (YC W25) 招聘创始工程师（应用人工智能），助力构建理解建筑蓝图的人工智能。这家初创公司获得顶级风投支持，专注于以模型花园方法解决建筑行业中蓝图解读、成本估算和许可证申请方面的技术难题。

该职位侧重于智能层，需要具备应用计算机视觉、大型语言模型和人工智能系统以交付原型并根据用户反馈改进它们的经验。理想的候选人应具备应用计算机视觉/机器学习经验，拥有从零到一的建设者心态，并能将人工智能应用于生产环境，同时展现出成长型思维，并有效沟通。必须能承受压力。

有初创公司或创始人经验、建筑行业背景以及具有影响力驱动力的人将获得额外加分。该职位为全职、办公室工作，位于旧金山或需要搬迁。薪资范围为 10 万美元至 18 万美元，股权在 0.50% 至 2.00% 之间。欢迎应届毕业生申请。该公司优先考虑智能侧的算法和模型开发，而非应用侧。有意者请在申请信息中说明自己为何适合该职位以及最喜欢的水果。

---

## 8. 我从零开始制作了一张软盘

**原文标题**: I Made a Floppy Disk from Scratch

**原文链接**: [https://kottke.org/25/08/i-made-a-floppy-disk-from-scratch](https://kottke.org/25/08/i-made-a-floppy-disk-from-scratch)

Jason Kottke 关注了 Polymatt 的一项雄心勃勃的项目：从头开始制作 3.5 英寸软盘。文章强调了重制软盘出乎意料的复杂性，特别是生产磁介质本身的挑战。Polymatt 面临着将微米级的磁性薄膜涂覆到 PET 薄膜上的任务。Kottke 将其与“从头开始制作手表”的视频相提并论，暗示了类似的吸引力。

文章还提到了 Polymatt 在工具获取方面的巧妙方法。在发现购买精密拖刀的成本很高后，他决定自己制造一个，以便在他的机器上进行精确切割。Kottke 强调了利用机器扩展其自身能力的满足感。文章最后，Kottke 思考着购买 CNC 机器的可能性，暗示他受到了 Polymatt 项目的启发。

---

## 9. 开发者瓶颈

**原文标题**: Developer's block

**原文链接**: [https://underlap.org/developers-block/](https://underlap.org/developers-block/)

本文探讨了“开发者阻塞”，一种类似于写作障碍的瘫痪状态，会影响软件开发者。文章概述了其发生的两种主要情景：新项目启动时和现有项目开发过程中。

在项目初期，开发者阻塞源于一开始就实施所有最佳实践的压力，例如全面的测试、详尽的文档、遵守编码标准以及强大的错误处理。 虽然这些很有价值，但这些任务的积累会导致感到不知所措。

在项目后期，阻塞可能源于对大型现有代码库（尤其是刚接触项目时）感到不知所措，或因过度劳累而失去动力。

本文提供了克服开发者阻塞的几种解决方案，包括：

*   **花时间学习：** 特意安排时间来理解代码库和语言。
*   **意识到何时疲倦：** 识别并通过休息和不太费力的任务来解决精神疲惫。
*   **增量工作：** 专注于小型、可管理的功能，并推迟不太关键的任务。
*   **编写原型：** 创建一个快速、最小的解决方案，以获得牵引力和理解。
*   **从草稿文档开始：** 优先考虑基本文档，并在以后进行完善。
*   **避免过早优化：** 首先专注于清晰、易于理解的代码，仅在必要时进行优化。
*   **尽早发布，频繁发布：** 定期发布代码以获得动力和反馈。
*   **选择要刮的牦牛皮：** 避免陷入修复依赖项或工具的小问题中。

---

## 10. 我黑了魔爪能量，你不会相信他们觉得你长什么样

**原文标题**: I Hacked Monster Energy and You Won't Believe What They Think You Look Like

**原文链接**: [https://bobdahacker.com/blog/monster-energy](https://bobdahacker.com/blog/monster-energy)

一名黑客调查了魔爪能量公司的企业基础设施，发现了重大的安全漏洞。他们通过利用存在缺陷的注册系统，轻易地访问了内部培训平台“魔爪大学”。在其中，他们发现了培训材料，包括对魔爪的目标消费者——年轻、低收入的白人（或西班牙裔）男性——的刻板且颇具争议的描述。讽刺的是，该平台自身缺乏安全性，却托管了网络安全培训。

该黑客还发现了Zoom会议日程、一个名为“野兽币”的内部员工奖励系统，以及，最令人震惊的是，一个完全暴露的OpenText API。这个API允许任何人搜索并下载魔爪整个公司文件系统中的文件，包括合同和内部文档，而无需任何身份验证。

此外，该黑客在一个子域名上发现了一个ClickUp集成，该集成在网站的JavaScript中暴露了一个管理员的私人账户令牌。这个令牌授予了对魔爪ClickUp工作区的完全访问权限，允许该黑客查看私人文档、修改项目数据，并将自己邀请到工作区，他们为了演示漏洞而这样做了。

该黑客试图直接联系魔爪能量公司，告知这些问题，但没有收到任何回应。ClickUp在被黑客提醒后解决了令牌问题，但魔爪尚未承认已报告的漏洞，而OpenText API仍然暴露。作者批评魔爪的安全措施不足以及对客户的刻板描述，并建议他们优先考虑安全而不是营销。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 2 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 3 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 4 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 5 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 6 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 7 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 8 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 9 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 10 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 11 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 12 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 13 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 14 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 15 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 16 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 17 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 18 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 19 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 20 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 21 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 22 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 23 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 24 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 25 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 26 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 27 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 28 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 29 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 30 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 31 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 32 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 33 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 34 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 35 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 36 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 37 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 38 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 39 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 40 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 41 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 42 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 43 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 44 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 45 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 46 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 47 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 48 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 49 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 50 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 51 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 52 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 53 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 54 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 55 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 56 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 57 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 58 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 59 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 60 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 61 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 62 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 63 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 64 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 65 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 66 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 67 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 68 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 69 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 70 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 71 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 72 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 73 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 74 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 75 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 76 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 77 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 78 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 79 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 80 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 81 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 82 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 83 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 84 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 85 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 86 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 87 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 88 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 89 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 90 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 91 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 92 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 93 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 94 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 95 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 96 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 97 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 98 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 99 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 100 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 101 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 102 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 103 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 104 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 105 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 106 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 107 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 108 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 109 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 110 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 111 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 112 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 113 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 114 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 115 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 116 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 117 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 118 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 119 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 120 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 121 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 122 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 123 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 124 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 125 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 126 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 127 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 128 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 129 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 130 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 131 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 132 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 133 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 134 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 135 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 136 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 137 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 138 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 139 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 140 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 141 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 142 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 143 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 144 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 145 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 146 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 147 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 148 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 149 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 150 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 151 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 152 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 153 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 154 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 155 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 156 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 157 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
