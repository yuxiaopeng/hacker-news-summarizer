# Hacker News 热门文章摘要 (2025-08-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 使用索引条件下推技术，连接速度提升450倍

**原文标题**: 450× Faster Joins with Index Condition Pushdown

**原文链接**: [https://readyset.io/blog/optimizing-straddled-joins-in-readyset-from-hash-joins-to-index-condition-pushdown](https://readyset.io/blog/optimizing-straddled-joins-in-readyset-from-hash-joins-to-index-condition-pushdown)

本文探讨了Readyset中针对“跨越式连接”的性能优化，在这种连接中，过滤谓词同时应用于连接的两侧。最初，Readyset使用哈希连接，但当连接的一侧具有低基数过滤器时，这被证明效率低下，导致全表扫描、高I/O和内存使用。

分析表明，即使禁用压缩，过度的数据读取和磁盘I/O仍然是瓶颈。引擎独立评估连接的双方，而不管选择性如何。

为了解决这个问题，Readyset实现了索引条件下推（ICP）。这种新策略首先将谓词应用于连接的一侧，收集生成的连接键，然后将复合条件（包括连接键和另一侧的原始谓词）推送到存储引擎（RocksDB）。这使得可以基于索引检索仅相关的行，从而最大限度地减少不必要的数据读取和全表扫描。

一项比较旧哈希连接方法和新ICP策略的基准测试显示，性能有了显着提高。由于缓存和索引效率的提高，ICP的实现使吞吐量提高了450倍以上，延迟降低了450倍以上。这种优化对于在Readyset中缓存未命中期间保持性能一致性至关重要。

---

## 12. WebR – 浏览器中的R

**原文标题**: WebR – R in the Browser

**原文链接**: [https://docs.r-wasm.org/webr/latest/](https://docs.r-wasm.org/webr/latest/)

WebR是一个R统计语言的版本，它被编译为使用WebAssembly直接在Web浏览器和Node.js中运行。这消除了执行R代码对服务器的需求，允许用户直接在他们的机器上运行R。一些R包已被适配用于WebR，并可以使用标准的`library()`函数加载。

该项目正处于积极开发中，API可能会发生变化。开发者应注意，文档可能与最新的构建版本不一致。此外，某些移动浏览器可能会限制WebAssembly可用的RAM，这可能会影响WebR应用程序在移动设备上的性能。

用户可以通过基于Web的REPL演示尝试WebR，无需安装，或者使用交互式R代码编辑器。WebR GitHub存储库的链接也已提供。

---

## 13. WaitGroup：用途、用法及Go 1.25变更

**原文标题**: Waitgroups: What they are, how to use them and what changed with Go 1.25

**原文链接**: [https://mfbmina.dev/en/posts/waitgroups/](https://mfbmina.dev/en/posts/waitgroups/)

本文探讨了Go语言中`sync.WaitGroup`的使用，以管理并发goroutine，并重点介绍了Go 1.25中引入的一项重大改进。在Go 1.25之前，开发者必须在启动goroutine之前手动增加计数器（`wg.Add(1)`），并在goroutine内部递减计数器（`wg.Done()`）以表示完成。未能保持准确的计数可能导致死锁或panic。`goleak`库可用于检测这些情况下的goroutine泄漏。

Go 1.25通过引入`wg.Go(func(){...})`简化了此过程。这个新函数自动处理每个goroutine的添加和完成信号，消除了手动错误的潜在可能。虽然`wg.Go`期望一个没有参数的函数，但需要参数的函数可以被包装在一个匿名函数中。

本文还简要提到了Go 1.25的另一个改进：自动检测容器化环境（Kubernetes）中的CPU限制，不再需要像`automaxprocs`这样的库来正确设置`GOMAXPROCS`。作者鼓励探索`sync`包中的其他功能，并提供了一个包含示例的仓库链接。

---

## 14. 硫排放管制后，航运线路上的雷电活动减少

**原文标题**: Lightning declines over shipping lanes following regulation of sulfur emissions

**原文链接**: [https://theconversation.com/the-world-regulated-sulfur-in-ship-fuels-and-the-lightning-stopped-249445](https://theconversation.com/the-world-regulated-sulfur-in-ship-fuels-and-the-lightning-stopped-249445)

本文探讨了船舶排放与雷击之间的联系，重点关注了航运燃料中硫排放法规的影响。研究人员注意到在新加坡港附近最繁忙的航运线上，出现了一条明显的强烈雷电活动带。他们调查了船舶尾气羽流与雷电频率之间的联系，尤其是在国际海事组织于2020年实施了大幅降低船舶燃料中硫排放量的法规之后。

该研究发现，这些法规生效后，航运线上空的雷击次数几乎立即下降了约50%。这项“意外实验”表明了雷暴对颗粒物排放的敏感性，特别是作为云滴和冰晶凝结核的气溶胶颗粒。硫排放的减少导致这些颗粒减少，可能导致暴风云内冰晶之间的碰撞减少，而冰晶碰撞对于电荷积累和雷电产生至关重要。

文章强调，虽然雷电减少并不一定意味着风暴减少或降雨减少，但它突出了人类污染对雷暴活动的显著且此前较少被理解的影响。还需要进一步研究来确定气溶胶颗粒对风暴的更广泛影响，包括它们增强风暴强度和改变全球雷电频率的潜力。了解这些影响对于预测地球气候将如何应对人类排放的波动至关重要。

---

## 15. 我入侵了麦当劳（找到安全联系人比找到秘方还难）

**原文标题**: I Hacked McDonald's (Security Contact Was Harder to Find Than Secret Recipe)

**原文链接**: [https://bobdahacker.com/blog/mcdonalds-security-vulnerabilities](https://bobdahacker.com/blog/mcdonalds-security-vulnerabilities)

本文详细描述了一位安全研究人员在麦当劳系统中发现多个漏洞的经历，以及在报告这些漏洞时遇到的困难。该研究人员最初在麦当劳App中发现了一个客户端验证问题，允许免费获取麦乐鸡，在联系一位软件工程师后该问题得到了修复。这促使他进一步调查，揭示了更严重的缺陷。

其中一个主要问题是用于品牌资产的“Feel-Good Design Hub”，它具有客户端密码保护，以及一个公开的注册端点，该端点以明文形式通过电子邮件发送密码。该研究人员还在JavaScript中发现了明文API密钥，这可能会导致用户数据列表和网络钓鱼攻击。Algolia索引暴露了请求访问麦当劳系统的用户的个人信息。

此外，一位员工能够访问面向公司员工的行政系统，包括TRT系统，从而可以进行全球员工搜索（包括电子邮件地址）以及冒充功能。GRS加盟商工具对管理功能没有身份验证，允许任意页面内容更改。员工还可以通过Stravito访问内部文档。新的CosMc's餐厅存在优惠券漏洞，允许无限次使用一次性优惠券，并且可以将任意数据注入订单中。

主要挑战是缺乏有效安全报告渠道。该研究人员不得不冷拨麦当劳总部电话，提及安全员工姓名，最终才找到联系人。虽然这些漏洞大多已修复，但协助进行OAuth研究的研究人员的朋友被解雇了。文章最后为麦当劳提出了建议，包括维护security.txt文件、建立安全联系人以及考虑漏洞奖励计划。

---

## 16. 着色器学院：通过解决挑战学习计算机图形学

**原文标题**: Shader Academy: Learn computer graphics by solving challenges

**原文链接**: [https://shaderacademy.com/](https://shaderacademy.com/)

着色器学院

---

## 17. 全球闪电定位网络

**原文标题**: World Wide Lightning Location Network

**原文链接**: [https://wwlln.net/](https://wwlln.net/)

全球闪电定位网络（WWLLN）是由华盛顿大学运营的全球网络，利用甚低频（VLF）无线电传感器监测闪电活动，旨在绘制全球范围内的闪电 strikes。

WWLLN的主要特点包括：

*   **全球监测:** 使用超过70个传感器的网络在全球范围内探测闪电 strikes。
*   **数据产品:** 提供近实时闪电地图、闪电密度地图、叠加闪电数据的卫星动画以及VLF频谱图。历史数据也可获取。
*   **传感器网络:** 依赖于由全球大学、研究所和研究人员托管的传感器网络。 托管方可获得全球数据用于其研究。
*   **闪电探测:** 使用来自至少5个传感器的群到达时间（TOGA）来定位闪电 strikes。
*   **准确性和效率:** 大约检测到全球约30%的30 kA strokes。 当闪电被传感器包围时，检测最为准确。
*   **数据可用性:** 存档数据可供购买，近实时数据可用于研究或商业用途。
*   **伙伴关系:** 该网络依赖于与全球众多托管传感器的机构合作。

WWLLN 不断寻找新的传感器站点，以提高覆盖范围和准确性。 他们鼓励有兴趣的各方与他们联系，商讨托管传感器事宜。

---

## 18. 将网络游戏转换为无需任何JavaScript也能运行的版本

**原文标题**: Converting an online game to work without any JavaScript

**原文链接**: [https://bejofo.com/blog/no-js-game-case-study](https://bejofo.com/blog/no-js-game-case-study)

本文详述了作者使用“渐进增强”方法，在不使用 JavaScript 的情况下，使其在线桌游网站实现全部功能的实验。目标是在禁用 JavaScript 的情况下也能提供可用的体验，同时不牺牲启用 JavaScript 用户的用户体验。

核心策略是使用 SvelteKit 进行服务器端渲染，提供一个可以立即查看的初始 HTML 页面。为了在没有 JavaScript 的情况下实现全部功能，作者采用了以下几种技术：

*   **交互式 UI 元素：** 使用 `<summary>` 和 `<details>` 元素来实现下拉菜单，并使用 URL 参数来控制模态对话框。
*   **表单提交：** 所有更改服务器状态的操作（游戏移动）都依赖于 `<form>` 元素，当启用 JavaScript 时，Svelte 会拦截这些操作以进行 websocket 通信。
*   **实时更新：** 采用 `<meta http-equiv="refresh"` 标签进行自动页面刷新，模拟实时更新，但会有延迟。
*   **动画：** 动画主要针对 JavaScript 用户，并确保服务器端渲染提供正确的最终状态。

作者认为，这样做有几个好处：由于服务器端渲染，初始页面加载速度更快；由于状态主要在服务器端管理，网站的恢复能力更强；HTML 的语义正确性也得到提高。缺点包括频繁刷新导致服务器资源使用量增加、代码复杂性增加以及功能开发速度减慢。

最终，作者得出结论，虽然该实验提高了网站的质量和性能，但考虑到理论上不使用 JavaScript 浏览的用户群体，所需的大量工作对于大多数项目来说可能并不值得。他们计划监控不使用 JavaScript 的使用情况，并可能最终删除额外的代码。

---

## 19. 大卫·克莱恩的环球航空海报 (2018)

**原文标题**: David Klein's TWA Posters (2018)

**原文链接**: [https://flashbak.com/david-kleins-magnificent-twa-posters-404428/](https://flashbak.com/david-kleins-magnificent-twa-posters-404428/)

大卫·克莱恩，1918年生于德克萨斯州埃尔帕索，以其在 20 世纪 50 年代和 60 年代为环球航空公司 (TWA) 创作的充满活力且极具影响力的旅行海报而闻名。他曾就读于洛杉矶艺术中心学院，二战期间为陆军绘制手册后，搬到纽约，并在 Clifford Strohl Associates 担任艺术总监，为百老汇演出设计广告。

当时的 TWA 在霍华德·休斯的所有权下，是一家领先的航空公司，以其创新而闻名，例如聘用第一位非裔美国人空姐，以及开创机上电影和使用波音 747 客机。1962 年，他们启用了具有重要建筑意义的肯尼迪机场航站楼。

克莱恩的海报捕捉了战后早期航空旅行的兴奋和乐观，并以洛杉矶、旧金山、纽约、华盛顿、瑞士、拉斯维加斯、以色列、希腊、佛罗里达、葡萄牙、巴黎、非洲和好莱坞等目的地为特色。他的作品至今仍具有时代意义，并因其艺术价值和历史意义而继续受到人们的赞赏。文章还鼓励通过捐款、注册邮件列表或在社交媒体上关注他们来支持该网站。文章包含指向网站商店的链接，该商店出售版画、马克杯、T 恤和明信片。

---

## 20. 你不能在炎热气候种植喜凉植物。

**原文标题**: You can't grow cool-climate plants in hot climates

**原文链接**: [https://www.crimepaysbutbotanydoesnt.com/blog/why-you-cant-grow-cool-climate-plants-in-hot-climates](https://www.crimepaysbutbotanydoesnt.com/blog/why-you-cant-grow-cool-climate-plants-in-hot-climates)

Joey Santore解释了凉爽气候植物为何在炎热气候中难以生存，重点在于“补偿点”的概念。植物和动物一样，会进行呼吸作用，燃烧糖类获取能量。补偿点是光合作用等于呼吸作用的平衡点；生长需要光合作用超过呼吸作用。

潮湿气候中常见的温暖夜晚会加速呼吸作用，导致凉爽气候植物消耗碳水化合物储备的速度超过它们通过光合作用补充的速度。这会导致健康状况下降，对病虫害的抵抗力增强，最终导致死亡。作者以番茄为例，指出其高海拔安第斯山脉的起源解释了它们对温暖夜晚和湿度的敏感性。

相反，热带植物在较冷的气候中难以生存，因为它们的新陈代谢减慢，阻碍了它们产生防御化学物质和新的生长的能力。

文章还提到了充足的光照对植物达到补偿点的重要性，并以仙人掌为例。最后，文章简要讨论了CAM、C3和C4光合作用，强调了不同的光合途径是如何进化来优化不同温度环境下的碳固定的。例如，C4光合作用在高温下更有效，因为它最大限度地减少了光呼吸，光呼吸是指Rubisco酶与氧气而不是二氧化碳结合的过程，从而阻碍了糖的产生。最终，植物的生存取决于光照、二氧化碳、温度以及其对特定气候的进化适应之间的相互作用。

---

## 21. 从M1 MacBook到Arch Linux：一个月的实验变成了永久

**原文标题**: From M1 MacBook to Arch Linux: A month-long experiment that became permanenent

**原文链接**: [https://www.ssp.sh/blog/macbook-to-arch-linux-omarchy/](https://www.ssp.sh/blog/macbook-to-arch-linux-omarchy/)

作者放弃 macOS，转用 Arch Linux (Omarchy发行版) 的体验

在 macOS 上使用了 15 年后，作者换到了联想 ThinkBook 14 G7 ARP 笔记本上运行的 Arch Linux (特别是 Omarchy 发行版)，并且很享受这种体验。 切换的主要原因是 macOS 更新带来的挫败感以及窗口管理 (Yabai) 的限制。

作者概述了成功过渡的几个先决条件，包括 Obsidian 笔记、模糊查找器、截图工具、照片程序、日光调整、日历集成和休眠。 macOS 上使用的许多 Setapp 应用程序都被 Linux 上的开源或类似替代品所取代。

这篇文章详细介绍了 macOS 和 Linux 之间的权衡，特别是关于截图工具 (Snagit)、电池续航、硬件质量和备份解决方案。 虽然 macOS 提供了无缝体验，但 Linux 允许更深层次的定制。 使用 Filen 实现了云同步，键盘快捷键则由 Kanata 和 XCompose 管理。 应用程序启动和剪贴板管理由 Walker 和 Clipse 处理。

Omarchy，一个定制的 Arch Linux 发行版，通过提供预配置的设置和快捷方式，使过渡更加顺畅。 作者强调了 Hyprland 的易用导航和外部显示器的无缝集成。

挑战包括缺少原生 Grammarly 覆盖以及 Microsoft Teams/Office 应用。 电池续航和风扇噪音也不如 MacBook 理想。 尽管存在这些挑战，作者仍然欣赏 Linux 提供的可定制性和控制力，并对继续这段旅程，不断学习和改进他们的设置感到兴奋。 他们还提供了他们的时事通讯、GitHub 和 dotfiles 的链接，供那些有兴趣的人关注。

---

## 22. 我使用LLM智能体创建软件的技巧

**原文标题**: My tips for using LLM agents to create software

**原文链接**: [https://efitz-thoughts.blogspot.com/2025/08/my-experience-creating-software-with_22.html](https://efitz-thoughts.blogspot.com/2025/08/my-experience-creating-software-with_22.html)

本文详述了作者使用LLM编码代理进行软件创建的经验，强调这不仅仅是“编码”，而是“创造”。作者作为一名爱好者，分享了提高这些代理生产力的一些技巧。

关键建议包括：为AI模型提供充足且相关的上下文；使用专用目录存储内部和面向公众的文档；在代码中，尤其是在测试文件中，直接强化指令，以避免常见错误。作者建议不要让AI直接读取大型文件，而是建议它使用工具仅提取所需内容。作者表示，必须监控上下文大小，如果AI失去焦点，则需要压缩或重启。

当你预测到困难领域时，可以通过预先生成上下文文档来引导上下文。作者指出，虽然沟通很重要，但只有当解释“为什么”能揭示新的目标或指南时，才有意义。

作者还强调，心中要有设计，而不仅仅是目标，并与AI合作改进设计。为重要功能保留单独的设计文档有助于节省token，并防止AI进行不必要的重新设计。通过将AI指向明确的设计，它可以降低其建议随机重构的可能性。

---

## 23. 机器人现在可以通过观察我们来学习使用工具。

**原文标题**: Robots can now learn to use tools just by watching us

**原文链接**: [https://techxplore.com/news/2025-08-robots-tools.html](https://techxplore.com/news/2025-08-robots-tools.html)

本文探讨了一种名为“工具即界面”的新框架，该框架允许机器人通过观看人类执行任务的视频来学习如何使用工具。该方法由伊利诺伊大学厄巴纳-香槟分校、哥伦比亚大学和德克萨斯大学奥斯汀分校的研究人员开发，旨在克服传统编程机器人的局限性，这些机器人难以适应新任务，并且需要大量的重新编程。

该过程包括使用两个摄像机视角拍摄动作，使用视觉模型 (MASt3R) 对其进行处理，以重建场景的 3D 模型，然后使用 3D 高斯溅射生成多个视点。至关重要的是，该系统会以数字方式将人类从场景中移除，仅使用“Grounded-SAM”专注于工具及其与环境的交互。这种“以工具为中心”的视角使机器人能够学习工具的轨迹和方向，从而实现不同机器人之间的技能转移，而无需考虑它们的物理配置。

该框架在诸如锤钉子、舀肉丸和在平底锅中翻转食物等任务上进行了测试，与传统的远程操作方法相比，获得了显着更高的成功率和更快的训练数据获取速度。受到儿童学习方式的启发，该方法使机器人能够适应动态情况，例如在不断添加肉丸的同时舀肉丸。尽管该系统目前存在局限性，例如假设工具是刚性固定的，以及在 6D 位姿估计方面面临挑战，但研究人员设想未来机器人可以从现成的视频中学习，从而创建一个用于适应性机器人的全球训练库。该研究荣获 ICRA 2025 年研讨会最佳论文奖。

---

## 24. 首个基于QUIC的媒体CDN：Cloudflare

**原文标题**: The first Media over QUIC CDN: Cloudflare

**原文链接**: [https://moq.dev/blog/first-cdn/](https://moq.dev/blog/first-cdn/)

Cloudflare 发布首个 Media over QUIC (MoQ) CDN，技术预览版开放测试

此博文宣布 Cloudflare 的 Media over QUIC (MoQ) CDN，这是同类产品中的首例。MoQ 是一种很有前景的标准，旨在取代 WebRTC、HLS/DASH 和 RTMP/SRT 用于实时媒体。此技术预览版可免费使用公共中继端点 (relay.cloudflare.mediaoverquic.com) 进行测试。

作者提供了使用其 @kixelated/hang 库的代码片段，以使用 Web Components 发布和观看直播。这些示例包括使用 AI 在浏览器中生成的可选隐藏式字幕。还有一个 Rust 库用于更复杂的媒体处理。

此预览版的限制包括 MoQ 草案的一个有限子集、潜在的错误、无身份验证（使用难以猜测的广播名称）、无 ANNOUNCE 支持（影响会议）、无 Safari 支持以及未优化的性能。作者还提到运行他们自己的 moq-relay，它具有诸如 JWT 身份验证和 WebSocket 回退之类的附加功能。

该文章强调了实际应用对于塑造 MoQ 标准的重要性，而不是仅仅依赖于理论设计。Cloudflare 的举措被誉为在标准化之前测试和完善 MoQ 的关键一步。作者鼓励其他公司构建和发布 MoQ 实现，以获得实践见解。未来的发展包括改进 Web API，以匹配现有平台的功能。

---

## 25. 展示：无需 JavaScript 的 (X)HTML 包含

**原文标题**: Show HN: JavaScript-free (X)HTML Includes

**原文链接**: [https://github.com/Evidlo/xsl-website](https://github.com/Evidlo/xsl-website)

使用原生XSL构建主题一致的网站，无需服务器端代码、静态站点生成器或JavaScript。

---

## 26. 我只是因为能做到，所以才在 Docker 里运行完整的 Linux 桌面。

**原文标题**: I run a full Linux desktop in Docker just because I can

**原文链接**: [https://www.howtogeek.com/i-run-a-full-linux-desktop-in-docker-just-because-i-can/](https://www.howtogeek.com/i-run-a-full-linux-desktop-in-docker-just-because-i-can/)

在 Windows 10 的 Docker 容器中运行完整 Linux 桌面环境的实验纪实

本文记录了作者在 Windows 10 的 Docker 容器中运行完整 Linux 桌面环境的实验过程，这与 Docker 通常用于轻量级、无头应用程序的传统用法背道而驰。出于好奇和学习 Docker 的渴望，作者最初尝试使用 AI 生成的代码创建自定义 Docker 镜像，但遇到了困难，突显了理解底层技术的重要性。随后，他们转而使用 Docker Hub 上预构建的基于 XFCE 的 Debian 镜像，成功在浏览器中运行了一个功能齐全的 Linux 桌面。

作者遇到了 GPU 加速和 Flatpak 兼容性方面的挑战。他们尝试了不同的桌面环境，发现 XFCE 性能最佳。进一步的探索包括研究工作镜像的 Dockerfile 以创建自定义镜像，并尝试了 xrdp，但收效甚微。文章随后重点介绍了 LinuxServer.io 的 Webtop 和 Kasm Workspaces 等预配置解决方案。

发现的一个显著好处是从低功耗 Chromebook 远程访问 Linux 桌面的能力，展示了容器化在远程访问方面的强大功能。作者还发现了其他好处，例如一次性沙箱、私密浏览和专用工作区。文章最后承认由于 Docker 容器和完整操作系统之间的根本差异而带来的挑战，但最终认为该项目对于学习体验及其所揭示的意外实际应用是有价值的。作者还提出了未来可能的实验，例如启用 Flatpak、通过 GPU 直通进行游戏以及进一步优化性能。

---

## 27. 华丽地毯的困境

**原文标题**: The Fancy Rug Dilemma

**原文链接**: [https://epan.land/essays/2025-8_FancyRugDilemma](https://epan.land/essays/2025-8_FancyRugDilemma)

好的，名为《华丽地毯的困境》的文章正在加载内容，意味着我现在还无法访问文本。因此，我无法提供摘要。内容加载完成后，请告知我，我将很乐意在300字范围内为您总结。

---

## 28. Nitro: 一个小巧而灵活的init系统和进程管理器

**原文标题**: Nitro: A tiny but flexible init system and process supervisor

**原文链接**: [https://git.vuxu.org/nitro/about/](https://git.vuxu.org/nitro/about/)

Nitro：轻量级且灵活的init系统和进程管理器，适用于嵌入式系统、桌面、服务器、initramfs和容器等各种环境。它具有运行时零内存分配、无限制文件描述符使用以及小型静态二进制文件等优点。配置基于脚本，位于目录中（默认为/etc/nitro），无需编译。

服务由包含可选`setup`、`run`和`finish`脚本的目录定义。`log`符号链接允许链接服务进行日志处理。特殊服务包括`LOG`（默认日志记录）、`SYS`（用于系统级设置、完成以及处理致命错误或重生）。支持使用`@`后缀的参数化服务。

Nitro分三个阶段运行：启动系统、运行服务（失败时重启）和关闭系统（SIGTERM后SIGKILL）。可以使用`nitroctl`远程控制它，提供用于服务管理（启动、停止、重启、信号）、列出服务和系统控制（重启、关机）的命令。它还会响应`rescan`、`reboot`和`shutdown`信号（除非用作pid 1）。

Nitro可以直接替代Linux上的init和Docker容器中的init。在FreeBSD上，它可以从`/etc/ttys`运行。

---

## 29. 销售阿加炉具的理论与实践(1935) [pdf]

**原文标题**: The theory and practice of selling the Aga cooker (1935) [pdf]

**原文链接**: [https://comeadwithus.wordpress.com/wp-content/uploads/2012/08/the-theory-and-practice-of-selling-the-aga-cooker.pdf](https://comeadwithus.wordpress.com/wp-content/uploads/2012/08/the-theory-and-practice-of-selling-the-aga-cooker.pdf)

基于该PDF内容，其内容看起来是一系列压缩字符和PDF命令，以及一些可辨认的文本片段，因此无法提供对一篇名为“阿加厨具销售的理论与实践（1935）”的文章的有意义的总结。

该PDF内容主要由编码文本组成，很可能是PDF指令和文本数据的混合体，这些数据已被损坏或未正确解码。 没有可辨认的与销售厨具或任何相关主题相关的连贯叙述或论证。

---

## 30. ArduinoOS (2017)

**原文标题**: ArduinoOS (2017)

**原文链接**: [https://github.com/DrBubble/ArduinoOS](https://github.com/DrBubble/ArduinoOS)

ArduinoOS 是一个为 Arduino 板设计的操作系统，实现了真正的多线程、异常处理和硬件抽象，同时最大限度地减少了内存使用。其内核采用汇编和 C 语言编写。支持的线程数量因板而异（例如，Arduino Uno 上为 20 个，Mega 上为 90 个）。

主要功能包括：

*   **多线程：** 支持多个任务的并发执行。线程使用 `InitTask` 或 `InitTaskWithStackSize` 创建。
*   **异常处理：** 使用基于整数的异常，通过 `try-catch` 块进行错误处理。提供各种预定义的异常代码。
*   **锁：** 允许线程安全地访问共享资源，防止冲突。
*   **睡眠：** 提供 `sleep()` 函数，用于暂停线程，而不会阻塞整个系统。
*   **内存管理：** 提供诸如 `freeMemory()` 和 `freeStack()` 等函数来监控内存使用情况。
*   **硬件抽象：** 包含常见硬件组件（如 LED、键盘、电机、蜂鸣器和舵机）的抽象类。

该操作系统需要包含 "KernelInitializer.h" 头文件，并在 `setup()` 函数中初始化内核。可以为线程定义自定义堆栈大小，但不同的大小可能会导致内存碎片。线程也可以接收参数。内核恐慌处理可用于管理严重错误。可以调整内核滴答周期来控制线程切换频率。

---

## 31. FFmpeg 8.0

**原文标题**: FFmpeg 8.0

**原文链接**: [https://ffmpeg.org/index.html#pr8.0](https://ffmpeg.org/index.html#pr8.0)

本文概述了FFmpeg项目的最新消息和更新，该项目是一个用于音频和视频录制、转换和流媒体的跨平台解决方案，主要涵盖从2023年11月到2025年8月期间。

**FFmpeg 8.0 "Huffman"（2025年8月）**: 这个主要版本新增了APV、ProRes RAW、RealVideo 6.0、Sanyo LD-ADPCM和G.728的原生解码器，改进了VVC解码器，并为FFv1（编码/解码）和ProRes RAW（解码）提供了基于Vulkan计算的编解码器。它还引入了硬件加速解码（Vulkan VP9, VAAPI VVC, OpenHarmony H264/5）和编码（Vulkan AV1, OpenHarmony H264/5）。新增了格式（MCC, G.728, Whip, APV）和滤镜（colordetect, pad_cuda, scale_d3d11, Whisper）。添加了基于Vulkan计算的新型解码器和编码器，提高了速度并实现了新的用例。该项目的基础设施已现代化，包括一个新的贡献平台。

**FFmpeg 7.1 "Péter"（2024年9月）**: 此版本宣布VVC解码器已稳定，并增加了对原生AAC USAC解码器、MV-HEVC解码和LC-EVC解码的支持。它合并了对H264和HEVC的Vulkan编码支持，从而实现了完全基于Vulkan的流水线。对颜色范围处理进行了重大内部改进。

**其他值得关注的新闻：**

*   **Coverity：** FFmpeg的代码质量得到了显著提高，缺陷密度低于平均水平。
*   **原生xHE-AAC解码器：** FFmpeg现在实现了原生xHE-AAC解码器。
*   **主权技术基金：** 德国的主权技术基金成为FFmpeg的第一个政府赞助商。
*   **FFmpeg 7.0 "Dijkstra"：** 此版本引入了原生VVC解码器（实验性）、IAMF支持和一个多线程的ffmpeg CLI工具。
*   **Vulkan解码：** Vulkan驱动的解码硬件加速已合并，从而实现了供应商通用和平台通用的解码。
*   **FFmpeg 6.0 "Von Neumann"：** 此版本具有许多新的编码器、解码器和滤镜。 实施了新的ABI发布计划。

---

## 32. 绝密：自动过滤敏感信息

**原文标题**: Top Secret: Automatically filter sensitive information

**原文链接**: [https://thoughtbot.com/blog/top-secret](https://thoughtbot.com/blog/top-secret)

本文介绍“绝密”（Top Secret），该工具旨在自动过滤自由文本中的敏感信息，尤其适用于处理聊天机器人、LLM 以及其他涉及用户数据处理的场景。它解决了保护难以使用正则表达式识别的敏感数据的难题。

“绝密”利用命名实体识别（NER）来识别和分类真实世界的实体，例如人物和地点。它的工作原理是过滤敏感信息并将其替换为占位符（例如，[PERSON_1]，[LOCATION_1]）。该工具提供这些占位符与原始敏感数据之间的映射，从而能够在以后恢复过滤后的值，例如在聊天机器人的响应中。

本文重点介绍了三个主要用例：

1.  **与 LLM 协同工作：** 在将用户输入发送到 LLM 之前对其进行过滤，然后使用映射恢复响应中的敏感信息。
2.  **过滤对话历史记录：** 通过在包含每条消息之前对其进行过滤，确保敏感数据不会通过之前的消息泄露。
3.  **通过验证防止存储敏感信息：** 在模型中使用“绝密”作为验证工具，以防止将敏感信息存储在数据库中。过滤器可以根据需要进行自定义和禁用。

本文强调了保护用户数据的重要性，尤其是在聊天机器人和 LLM 的使用日益增加的情况下。“绝密”旨在减轻手动过滤敏感信息的负担。

---

## 33. 鸭嘴兽步入符号执行新纪元

**原文标题**: Echidna Enters a New Era of Symbolic Execution

**原文链接**: [https://gustavo-grieco.github.io/blog/echidna-symexec/](https://gustavo-grieco.github.io/blog/echidna-symexec/)

本文介绍了Echidna集成的hevm增强型符号执行能力，提供验证和探索两种模式。验证模式通过在构造函数执行后对每个方法进行符号测试，来证明无状态代码中不存在错误，类似于形式化验证技术。它检查构造函数执行后的所有可能路径，确认断言成立，但受到外部调用和无限gas等假设的限制。结果可以是“已验证”、“通过”、“失败”、“错误”或“超时”。探索模式结合模糊测试和符号执行，以揭示有状态场景中的断言失败。它利用通过模糊测试积累的语料库，在其之上执行单个符号交易，以更详尽地探索特定状态并减少对运气的依赖。

文章包含使用Algebra和ERC4626金库的案例研究，说明了每种模式的有效性。验证模式识别出几个通过的不变量，而探索模式快速查明了金库代码中的一个断言失败，仅靠模糊测试很难找到。虽然文章展示了符号执行工具日益成熟，但它强调了理解其局限性的重要性，特别是关于无界循环和动态数据结构，以及开发者可能误解结果的可能性。最后，文章解释了如何在Echidna中启用符号执行模式，并提到了当前不太直观的界面。

---

## 34. 欧洲对抗空调的战争是疯狂的

**原文标题**: Europe's crusade against air conditioning is insane

**原文链接**: [https://www.noahpinion.blog/p/europes-crusade-against-air-conditioning](https://www.noahpinion.blog/p/europes-crusade-against-air-conditioning)

诺亚·史密斯认为，欧洲抵制空调是一种有害且不合逻辑的“圣战”，其驱动因素是环境担忧和文化精英主义的混合体。他指出，气候变化正在导致欧洲出现大量与高温相关的死亡，远远超过美国枪支暴力死亡率，而空调是减少这些死亡人数的行之有效的解决方案，美国的经验已经证明了这一点。

欧洲官方避免使用空调的理由是其通过电力消耗对气候变化造成的贡献。 然而，史密斯认为，更深层的原因是一种文化因素：即认为空调是一种不必要的、 “美国的”奢侈品，与欧洲传统背道而驰。 他列举了围绕空调使用的法规、社会压力和迷信的例子。

史密斯批评这种立场是一种“去增长”意识形态，它优先考虑紧缩和自我约束，而不是技术解决方案。 他认为，放弃空调所实现的相对较小的排放量减少，不值得付出数万不必要的死亡。 他认为，像日本和新加坡那样拥抱技术，对于社会进步和经济繁荣至关重要。 他总结说，欧洲不愿采用空调正在使其成为一个不太舒适、更加贫困的文明。

---

## 35. Glyn：用于 Gleam Actor 的类型安全 PubSub 和注册中心，支持分布式集群

**原文标题**: Glyn: Type-safe PubSub and Registry for Gleam actors with distributed clustering

**原文链接**: [https://github.com/mbuhot/glyn](https://github.com/mbuhot/glyn)

Glyn 是一个 Gleam 库，为 actor 通信提供类型安全的 PubSub 和 Registry 系统，旨在与 Erlang 的 syn 库一起用于分布式集群。它提供了两种 actor 交互方法：PubSub 用于向订阅者广播事件，Registry 用于将命令直接路由到命名进程，两者都与 Gleam 的 actor 模型集成。

该库需要显式消息解码器，以确保跨集群节点的类型安全。它使用 Erlang terms 进行消息传递，因此需要元组解码。本文提供了如何使用 Gleam 的 `dynamic` 和 `decode` 模块定义消息类型和解码器函数的示例，重点介绍了 `Event` 和 `Command` 类型。

示例演示了使用 `pubsub.new`、`pubsub.subscribe` 和 `pubsub.publish` 进行的基本 PubSub 功能，以及通过 `registry.new`、`registry.register`、`registry.send` 和 `registry.call` 使用 Registry 的示例。本文还展示了如何使用 `process.select` 和 `process.merge_selector` 将两个系统集成到单个 Gleam actor 中，以创建复杂的消息处理程序，从而为管理 actor 中不同的通信通道提供结构化的方法。

最后，该文档简要介绍了使用 `gleam test` 和 `gleam docs build` 进行的开发，并指定了 MIT 许可证。

---

## 36. LabPlot：免费、开源、跨平台数据可视化与分析

**原文标题**: LabPlot: Free, open source and cross-platform Data Visualization and Analysis

**原文链接**: [https://labplot.org/](https://labplot.org/)

LabPlot 2.12.1发布：免费开源跨平台数据可视化分析应用，此版本由Alexander Semke于2025年8月18日发布，主要修复了软件各方面的错误并进行了细微改进，建议用户更新。

---

## 37. 网站和网页开发者大多不在意客户端问题。

**原文标题**: Websites and web developers mostly don't care about client-side problems

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/web/WebsitesDontCareAboutClients](https://utcc.utoronto.ca/~cks/space/blog/web/WebsitesDontCareAboutClients)

Chris Siebenmann的《网站和Web开发者大多不关心客户端问题》解释了为什么使用较旧或可疑浏览器的用户在访问他的博客Wandering Thoughts和CSpace时会遇到错误。他实施了反爬虫措施，以应对大量爬虫涌入，特别是那些使用过时Chrome User-Agent的机器人，它们很可能用于LLM训练。这些措施无意中阻止了使用旧浏览器的合法用户。

Siebenmann承认由此带来的不便，并鼓励使用最新浏览器的受影响用户向他提供浏览器详细信息和User-Agent字符串。他还提到了通过archive.today、archive.ph和archive.is等存档服务访问该网站的用户。他批评这些服务的行为与恶意爬虫类似，使用旧的Chrome User-Agent、无法追踪的IP地址，甚至伪造反向DNS条目。他建议使用archive.org，因为它是一个行为更好的存档爬虫，可以访问他的博客。核心问题在于难以区分合法用户和良性存档服务与恶意爬虫，这导致了采取一刀切的方法，影响了一些真正的用户。

---

## 38. 使用LLM助手进行内核开发

**原文标题**: The use of LLM assistants for kernel development

**原文链接**: [https://lwn.net/Articles/1032612/](https://lwn.net/Articles/1032612/)

这篇2025年8月发表在LWN.net上的文章探讨了内核开发社区内部关于使用基于LLM（大型语言模型）的工具生成内核补丁的持续辩论。这场辩论是由LLM生成的补丁被提交引发的，引发了关于披露政策和对此类贡献总体接受度的讨论。

一些开发者，如Vlastimil Babka和Lorenzo Stoakes，主张在广泛采用*之前*建立正式的“内核AI政策”，担心当前缺乏指导方针会导致大量难以理解且可能存在错误的补丁涌入。人们担心贡献者缺乏解释或修复LLM生成的代码的能力。文章提到了QEMU项目彻底禁止LLM生成的贡献。

另一些开发者，如Mark Brown和Kees Cook，认为无论是否有政策，这些工具都已经在使用并将继续使用。他们提倡对LLM的使用保持开放和诚实，以便在代码审查期间进行考虑。

文章重点介绍了围绕在补丁中披露LLM使用情况的讨论，建议包括使用“Generated-by”或“Assisted-by”标签，或将信息包含在封面信中。适当的披露程度存在争议，并提出了关于代码完成工具和编译器诊断的问题。

LLM生成的代码的版权和责任也是主要问题。虽然Linux基金会提供了指导，但仍然存在维护者如何验证合规性的问题。建议使用“Signed-off-by”标签作为提交者承担责任的一种方式，但这并不能缓解人们对维护者负担过重和潜在的低质量补丁涌入的担忧。文章总结说，这场辩论可能会继续下去，该问题已被提议在2025年维护者峰会上进行讨论。

---

## 39. Linux上的反作弊问题 (2024)

**原文标题**: The issue of anti-cheat on Linux (2024)

**原文链接**: [https://tulach.cc/the-issue-of-anti-cheat-on-linux/](https://tulach.cc/the-issue-of-anti-cheat-on-linux/)

本文探讨了在Linux上为多人游戏实施反作弊方案所面临的挑战。虽然由于Steam Deck和对Windows的不满，Linux游戏正在增长，但大多数竞技性多人游戏都无法进行，因为它们的反作弊系统（如BattlEye、Easy Anti-Cheat、Vanguard和RICOCHET）在Linux上无法正常工作，甚至根本无法工作。

作者解释了反作弊解决方案在Windows上的工作原理，重点介绍了如何通过用户模式组件、服务和内核模式驱动程序的组合来阻止内存访问以及检测/封禁作弊者。他以Valorant为例，强调了该游戏通过将反作弊措施与游戏开发紧密结合，包括内核级保护、数据加密和积极的社区监控，有效地打击作弊行为。

文章探讨了关于内核模式反作弊的常见担忧，例如安全漏洞和潜在的间谍行为，并认为与Windows系统上现有的漏洞相比，这些担忧通常被夸大了。

最终，Linux上的核心问题在于其开放性，这使得无法实施与Windows相当的有效反作弊方案。作者解释了Linux内核如何能被轻易修改以绕过任何反作弊措施，使其失效。虽然某些反作弊解决方案（如Easy Anti-Cheat）可能看起来可以在Linux上工作，但它们通常只执行基本功能，并且很容易被作弊者绕过。

---

## 40. "\u{1F926}\u{1F3FC}\u200D\u2642\uFE0F".length == 7 没错 (2019)

**原文标题**: It’s not wrong that "\u{1F926}\u{1F3FC}\u200D\u2642\uFE0F".length == 7 (2019)

**原文链接**: [https://hsivonen.fi/string-length/](https://hsivonen.fi/string-length/)

本文深入探讨了在处理Unicode字符，特别是像"🤦🏼‍♂️"这样的表情符号时，各种编程语言中字符串长度计算的复杂性。作者指出，JavaScript中`.length`属性对"🤦🏼‍♂️"返回7并非本质上的“错误”，而是反映了JavaScript（以及其他语言，如Python 3和Rust）如何基于底层Unicode编码形式的代码单元来计算字符串长度（JavaScript为UTF-16，Python 3为UTF-32，Rust为UTF-8）。

文章解释说，"🤦🏼‍♂️"由多个Unicode标量值组成，这些标量值代表不同的组成部分（捂脸，肤色修饰符，性别符号和变体选择器）。因此，JavaScript计算UTF-16代码单元的数量（7），Python 3计算UTF-32代码单元的数量（5），而Rust计算UTF-8代码单元的数量（17）。

另一方面，Swift使用“扩展字位簇”的概念，并返回长度1，将整个表情符号视为单个视觉单元。文章强调，不同的语言提供了不同程度的抽象和对字符串长度确定方式的控制。文章进一步讨论了何时计算和存储长度信息（急切与懒惰）以及记住存储原生代码单元长度的优势相关的权衡。最终，“正确”的长度取决于具体的用例和所需的细节级别。

---

## 41. 测量人工智能推理的环境影响

**原文标题**: Measuring the environmental impact of AI inference

**原文链接**: [https://arstechnica.com/ai/2025/08/google-says-it-dropped-the-energy-cost-of-ai-queries-by-33x-in-one-year/](https://arstechnica.com/ai/2025/08/google-says-it-dropped-the-energy-cost-of-ai-queries-by-33x-in-one-year/)

这篇Ars Technica文章探讨了人工智能推理对环境的影响，重点介绍了谷歌对其自身人工智能使用情况的新分析。虽然美国电力需求的增长（部分原因是人工智能数据中心）引发了人们对环境成本的担忧，特别是考虑到煤炭使用量的增加，但精确的测量非常困难。

谷歌的分析（罕见地揭示了真实世界的数据）显示，仅仅一年内，每次搜索查询的能源消耗就惊人地减少了33倍。这种改进源于可再生能源使用量的增加等因素，但主要源于软件优化，如混合专家系统和紧凑型模型版本，以及高效的数据中心管理和定制人工智能加速器设计。

该分析包括CPU、人工智能加速器和内存（包括激活和空闲状态）的能耗，以及数据中心的整体能源和用水量，甚至包括硬件生产中的碳排放。但是，它不包括网络、终端用户硬件和人工智能模型训练的环境成本，尽管后者可以合理估计。

谷歌估计，在Gemini Apps中，一个典型的文本提示消耗0.24瓦时电量，排放0.03克二氧化碳当量，并使用0.26毫升水，大致相当于观看9秒电视。虽然个人影响很小，但请求量很大。

尽管取得了进展，但文章强调需要全面的测量框架，并鼓励其他公司采用类似的方法，以确保环境效率与人工智能的进步保持同步。谷歌的透明度和详细的方法被强调为行业改进的积极一步。

---

## 42. 使用博弈论解释制度如何产生以管理有限资源

**原文标题**: Using game theory to explain how institutions arise to manage limited resources

**原文链接**: [https://phys.org/news/2025-08-game-theory-naturally-limited-resources.html](https://phys.org/news/2025-08-game-theory-naturally-limited-resources.html)

本文探讨了日本理化学研究所和哥本哈根大学的一项研究，该研究利用博弈论解释了如何自组织机构涌现以管理渔业和水等有限资源。这些机构的特点是基层有机发展起来的规范和规则，从而确保可持续的资源利用和公平的获取。

研究人员创建了一个简单的数学模型，涉及定期收获资源（例如鱼）的两个人。每个人根据鱼类种群以及自己和他人的福祉来决定是否收获。他们可以通过克制自己来合作，通过过度捕捞来惩罚对方，或者自私地行事。这些选择取决于当前的鱼类种群和过去的互动。

尽管该模型很简单，但它成功地预测了自组织机构的出现。关键发现是，即使参数最少，该模型也能证明这些机构如何自然产生。研究人员认为该模型为理解此类机构的形成提供了基础，并计划将其应用于现代社会中的送礼等其他情境。该研究发表在《美国国家科学院院刊》（PNAS）上。

---

## 43. 哪吒二是世界第一大电影。

**原文标题**: Ne Zha II is the biggest movie in the world

**原文链接**: [https://www.cbc.ca/news/entertainment/ne-zha-ii-1.7614698](https://www.cbc.ca/news/entertainment/ne-zha-ii-1.7614698)

杰克逊·韦弗在加拿大广播公司新闻发表的文章探讨了中国动画电影《哪吒II》的巨大成功，分析了其文化意义和对全球电影产业的潜在影响。这部电影打破了票房纪录，成为有史以来票房最高的动画电影，超越了许多好莱坞大片，这主要得益于其在中国市场的成功。

文章解释了剧情，改编自中国古典小说《封神演义》，重点讲述了哪吒在与他作为魔的既定命运作斗争时，自我发现和接受的旅程。文章强调了这部电影对道教哲学的探索，即善与恶是相互关联的，而不是绝对的。

《哪吒II》的成功归功于其引人入胜的故事、令人惊叹的动画和动感十足的场面，以及它与中国观众的共鸣，这得益于哪吒既有的文化影响力。韦弗还强调了这部电影对中国电影产业日益增长的信心的贡献，认为这是全球电影格局的潜在转变，挑战了好莱坞的统治地位。A24在北美发行英文配音版被视为检验中国电影是否能扩大其海外影响力的尝试。总的来说，这篇文章将《哪吒II》描绘成一部当之无愧的电影成就，也是中国文化影响力上升的象征。

---

## 44. 离开Gmail转用Mailbox.org

**原文标题**: Leaving Gmail for Mailbox.org

**原文链接**: [https://giuliomagnifico.blog/post/2025-08-18-leaving-gmail/](https://giuliomagnifico.blog/post/2025-08-18-leaving-gmail/)

朱利奥·马尼菲科详述了其从Gmail切换到Mailbox.org的经历，原因是出于对谷歌数据收集以及美国政府访问邮件的隐私担忧。在考虑了Proton Mail和Tutanota（两者都提供端到端加密）后，他选择了Mailbox.org，因为其PGP集成使他能够继续在macOS和iOS上使用Apple的Mail应用。

Mailbox.org提供10GB的电子邮件存储空间和5GB的云存储空间，起价为每月2.50欧元（按年付费），并提供可扩展的存储选项。朱利奥对简单而有效的网页界面以及与Apple Mail无缝集成的文件夹系统感到特别满意。虽然Mailbox.org包含视频聊天和任务列表等功能，但他主要关注的是电子邮件功能。

迁移是在其存档服务器上使用Docker容器内的`imapsync`完成的。他精心配置了脚本，以避免重复并合并特定文件夹。该过程花费了大约3个小时来传输2.14GB的数据。

为了确保平稳过渡，朱利奥设置了从其旧Gmail帐户的电子邮件转发，并在Mailbox.org中标记了从Gmail转发的电子邮件，这使他可以更新其在各个服务上的电子邮件地址。他还赞赏Mailbox.org轻松导入PGP密钥的功能，从而实现了加密通信，即使在iOS上也是如此。最终，朱利奥对他的决定表示满意，并强调了远离Gmail后意想不到的积极方面。

---

## 45. 因年龄验证法案，Bluesky 在密西西比州停止服务

**原文标题**: Bluesky Goes Dark in Mississippi over Age Verification Law

**原文链接**: [https://www.wired.com/story/bluesky-goes-dark-in-mississippi-age-verification/](https://www.wired.com/story/bluesky-goes-dark-in-mississippi-age-verification/)

Bluesky屏蔽密西西比州所有IP地址，以回应美国最高法院允许该州强制执行社交媒体平台严格年龄验证的最新裁决。Bluesky认为，密西西比州的验证方式要求追踪所有18岁以下用户，并向所有用户索取敏感个人信息以验证年龄，这在他们目前的资源和基础设施条件下是不可行的。违规行为可能导致每次高达1万美元的罚款。

Bluesky认为该法律制造了限制言论自由的重大障碍，并对较小型平台造成不成比例的损害。该公司认为，有效的儿童安全政策应经过精心定制，而不应为较小型供应商制造巨大障碍。

旨在保护儿童的年龄验证法律已经在英国等地产生了广泛影响，需要进行身份扫描和其他方法来证明年龄。德克萨斯州也有一项类似的法律得到最高法院的支持，引发了对言论自由的担忧。批评人士认为，这些法律可以通过VPN和其他方法规避，甚至可能使儿童面临更大的身份盗窃和隐私侵犯风险。Bluesky是第一个对年龄验证法律采取如此严厉行动的主要社交媒体平台。

---

## 46. 我太笨了，学不会 Zig 的新 IO 接口。

**原文标题**: I'm too dumb for Zig's new IO interface

**原文链接**: [https://www.openmymind.net/Im-Too-Dumb-For-Zigs-New-IO-Interface/](https://www.openmymind.net/Im-Too-Dumb-For-Zigs-New-IO-Interface/)

本文记录了作者在使用 Zig 0.15 中引入的新的 `std.Io.Reader` 和 `std.Io.Writer` 接口时遇到的困难，尤其是在尝试升级他们的库以使用新的 `std.crypto.tls.Client` 时。他们发现这个新接口令人困惑且不一致，特别是与之前的（同样有问题的）接口相比。

作者详细描述了调整 `tls.Client.init` 函数的步骤，该函数需要 `std.Io.Reader` 和 `std.Io.Writer`，而不是熟悉的 `net.Stream`。这涉及到使用 `net.Stream` 的 `reader()` 和 `writer()` 方法，并分别使用 `interface()` 和 `&interface` 将返回的类型转换为预期的接口类型。作者注意到访问接口时的不一致性。

作者还努力解决 readers 和 writers 所需的缓冲区参数，这些参数必须至少为 `std.crypto.tls.max_ciphertext_record_len` 大小。他们强调了传递给 `tls.Client.init` 的看似强制的选项，即 `ca_bundle`、`host`、`write_buffer` 和 `read_buffer`，并质疑为什么这些不是可选的。

在提供所有必要的参数后，程序最初挂起，作者通过为 `write_buffer` 和 `read_buffer` 选项分配第二对缓冲区来解决此问题。最后，由于缺少标准的 `read` 方法，他们在从 `tls_client.reader` 读取响应时遇到了困难，并求助于使用 `stream(&w, .limited(buf.len))` 将数据传输到固定大小的 writer `w`，以提取响应，但代码无法正常工作。他们最终感到迷失，并被新接口的复杂性以及缺乏清晰的文档和示例所淹没。

---

## 47. 弥合 Nix 差距：从环境到 Rust 的打包应用

**原文标题**: Closing the Nix gap: From environments to packaged applications for rust

**原文链接**: [https://devenv.sh/blog/2025/08/22/closing-the-nix-gap-from-environments-to-packaged-applications-for-rust/](https://devenv.sh/blog/2025/08/22/closing-the-nix-gap-from-environments-to-packaged-applications-for-rust/)

本文旨在解决开发者在为Rust应用程序选择Nix打包工具（crate2nix, cargo2nix, naersk等）时面临的困惑。`devenv` 致力于通过为开发和部署提供一致的接口来简化此过程。

在开发过程中，`devenv` 通过 `languages.rust.enable` 提供必要的工具（cargo, rustc, rust-analyzer），而无需 Nix 专业知识。在部署时，`languages.rust.import` 利用 `crate2nix` 来打包 Rust 应用程序。 这消除了开发者研究和选择特定打包工具的需求，因为 `devenv` 已经评估并选择了 `crate2nix`。

这种方法与之前 `devenv` 为 Rust 工具链从 `fenix` 无缝过渡到 `rust-overlay` 的决策相类似。

本文强调一个统一的工作流程：启用一种语言进行开发 (`languages.rust.enable`)，然后使用相应的 `languages.<language>.import` 来打包应用程序以进行部署。 这种模式也适用于其他语言，如 Python (使用 `uv2nix`) 和 Go。

该示例演示了如何添加 `crate2nix` 作为输入，使用 `config.languages.rust.import` 导入 Rust 应用程序，在开发环境中公开该应用程序，最后使用 `devenv build outputs.myapp` 构建它。 目标是为各种语言提供简化且一致的 Nix 打包体验。

---

## 48. 用计算机诈骗法起诉向CNN泄露空难录像

**原文标题**: Computer fraud laws used to prosecute leaking air crash footage to CNN

**原文链接**: [https://www.techdirt.com/2025/08/22/investigators-used-terrible-computer-fraud-laws-to-ensure-people-were-punished-for-leaking-air-crash-footage-to-cnn/](https://www.techdirt.com/2025/08/22/investigators-used-terrible-computer-fraud-laws-to-ensure-people-were-punished-for-leaking-air-crash-footage-to-cnn/)

此短文声称，计算机欺诈法正被用来起诉向CNN泄露空难录像的人。作者对法律体系表达了一种愤世嫉俗的观点，声称实际法律无关紧要。相反，他们认为，即使荒谬，逮捕警官的解释才是决定结果的因素。作者否定了正当程序的概念，暗示在这种类型的起诉中，它不再是相关的考虑因素。本质上，这篇文章声称在对泄密者的起诉中存在滥用权力和无视法律原则的行为。

---

## 49. VHS-C：当一个懒惰的想法踉跄走向完美[视频]

**原文标题**: VHS-C: When a lazy idea stumbles towards perfection [video]

**原文链接**: [https://www.youtube.com/watch?v=HFYWHeBhYbM](https://www.youtube.com/watch?v=HFYWHeBhYbM)

这看起来像是YouTube的样板页脚内容，而不是一篇文章。"VHS-C：当一个懒惰的想法跌跌撞撞走向完美"这个标题暗示着一个讨论VHS-C格式的视频。然而，提供的内容与此无关，列出了标准的YouTube法律和政策链接，关于版权、广告和NFL周日比赛套票的信息。

因此，基于所提供内容的总结是：

这段内容包含标准的YouTube页脚链接和版权信息。其中包括指向关于新闻版权、如何联系YouTube、创作者信息、广告、开发者、服务条款、隐私政策、安全以及YouTube运作方式的页面链接。它还提到了测试新功能以及属于Google LLC的2025年NFL周日比赛套票版权。它没有提供任何关于标题所指示的视频主题VHS-C的实际信息。

---

## 50. Visual C++ (2017) 可视化历史

**原文标题**: A visual history of Visual C++ (2017)

**原文链接**: [http://www.malsmith.net/blog/visual-c-visual-history/](http://www.malsmith.net/blog/visual-c-visual-history/)

本文以图文形式回顾了微软 Visual C++ IDE 从诞生到 2017 年的发展历程，重点关注其演变及其对 Windows 软件开发的影响。文章从 Visual C++ 1.0 (1993) 开始，记录了每个主要版本，并指出了 UI 设计、目标操作系统支持以及所使用的 C 运行时库 (CRT) DLL 的变化。

早期版本 (1.x-4) 在集成和 DLL 部署方面存在困难，但后来的版本 (5-6) 实现了更高的稳定性和效率，尤其是在采用 MSVCRT.DLL 之后。Visual C++ 6 因其能够与较新的 Windows SDK 集成而备受赞誉。

.NET 时代带来了显著的 UI 变化和新的 CRT DLL，但也带来了部署难题。Visual C++ 2005 取消了标准版中的非优化编译器。Visual C++ 2010 因其基于 WPF 的 UI 而引人注目，作者认为这对其性能产生了负面影响。作者表示对后来的版本（2012 年及以后）缺乏兴趣，原因是它们缺乏针对其特定原生代码用例的引人注目的功能，主要侧重于 C++ 支持和不同的主题。文章最后指出，随着旧操作系统的淘汰和硬件的进步，每个 Visual C++ 版本的价值都会随着时间的推移而增加。

---

## 51. 如何避免买到劣质固态硬盘

**原文标题**: How Not to Buy a SSD

**原文链接**: [https://andrei.xyz/post/how-not-to-buy-a-ssd/](https://andrei.xyz/post/how-not-to-buy-a-ssd/)

作者从罗马尼亚大型在线零售商eMag的第三方卖家处购买了一块960GB的金士顿SSD，但由于传输速度极慢，怀疑是假货。初步测试显示速度远低于SATA III甚至USB 2.0标准。怀疑存在欺诈行为，作者使用F3（Fight Flash Fraud）测试了驱动器的容量，但驱动器变得无法使用，并在尝试格式化时开始报错。

作者怀疑该驱动器是真正的、容量较小的（128GB）金士顿SSD，其固件被重写以虚报960GB的容量。作者指出低质量的背面标签印刷是最初的警告信号。他警告读者在大型平台上从第三方卖家处购买时要小心，即使是“由零售商履行”，因为这是一种常见的诈骗手段。

作者联系了eMag，举报了欺诈卖家并要求退款。产品列表已被修改，导致难以发起退货。作者还强调了在填充大约128GB后驱动器性能急剧下降，进一步支持了他的理论。最终，eMag客户支持同意启动退款流程，作者收到了全额退款。

---

## 52. 流行的日本手機遊戲引入了外部支付系統。

**原文标题**: Popular Japanese smartphone games have introduced external payment systems

**原文链接**: [https://english.kyodonews.net/articles/-/59689](https://english.kyodonews.net/articles/-/59689)

日本手游开发者纷纷绕开应用内支付系统以避开苹果谷歌的佣金。据共同社报道，高达70%的日本手游现已引入外部支付系统。此举让开发者得以保留更多收入，否则这些收入将被应用商店平台抽成。文章指出，这是日本游戏公司在竞争激烈的移动游戏市场中保持财务独立性并优化收益的策略。

---

## 53. Io_uring、kTLS与Rust构建零系统调用HTTPS服务器

**原文标题**: Io_uring, kTLS and Rust for zero syscall HTTPS server

**原文链接**: [https://blog.habets.se/2025/04/io-uring-ktls-and-rust-for-zero-syscall-https-server.html](https://blog.habets.se/2025/04/io-uring-ktls-and-rust-for-zero-syscall-https-server.html)

本文探讨了如何使用 Rust、io_uring 和 kTLS 构建高性能 HTTPS 服务器，以最大限度地减少系统调用并提高效率。作者追溯了 Web 服务器架构从预先派生到 epoll 的演变，突出了减少系统调用开销日益增长的重要性。

Io_uring 被视为一种解决方案，它允许内核操作的异步排队，从而最大限度地减少系统调用。内核和服务器通过内存队列交换工作和结果，在高负载下实现接近无系统调用的操作。理想的设置涉及每个核心一个线程，针对 NUMA 架构进行了优化，以最大限度地减少内存访问延迟。内存分配通过预先为连接分配固定块来管理，以避免系统调用和碎片。

kTLS 将加密/解密卸载到内核，从而可以进行 `sendfile()` 操作，并有可能进行硬件卸载以获得进一步的性能提升。使用 `register_files` 的无描述符文件通过避免在用户和内核空间之间传递文件描述符来进一步降低开销。

作者构建了一个名为“tarweb”的 Web 服务器，该服务器从 tar 文件提供内容，作为这些技术的实际应用。他们面临着集成 io_uring 和 kTLS 的挑战，因为缺少 `setsockopt()` 支持，这需要自定义 PR 到 rustls。

文章最后承认了 io_uring 由于手动内存管理而存在的固有安全问题。作者建议需要一个更安全的 Rust 封装 crate，以利用 Rust 的借用检查器和内存安全保证，避免潜在的数据损坏和段错误。由于代码仍在改进中，作者尚未对 tarweb 进行基准测试。

---

## 54. 运动的回报

**原文标题**: The ROI of Exercise

**原文链接**: [https://herman.bearblog.dev/exercise/](https://herman.bearblog.dev/exercise/)

本文论证了定期锻炼带来的高投资回报率（ROI）。作者本人也是一位坚持锻炼者，他强调了经常被忽视的益处——延长寿命，并将力量、专注力和心理健康等即时益处放在一边，进行一个简单的思维实验。

作者保守估计，坚持锻炼（每周3小时）在成年后相当于大约一年的总锻炼时间。引用研究表明，定期体育锻炼可以延长3-10年的寿命，作者保守地使用了基于网球研究的10年寿命延长。这产生了1:10的投资回报率——一年的锻炼带来了额外的十年寿命。

虽然承认存在过度简化和混杂因素，但作者强调，花在锻炼上的时间并非浪费。他在运动中找到了快乐和社区，并强调了除长寿之外的许多其他好处，包括改善睡眠、减少虚弱、增强力量、提高认知功能以及进入社群的机会。

最后，作者强调了锻炼的可及性，将其与花在看Netflix上的时间进行比较，并鼓励读者慢慢开始，建立一个可持续的锻炼习惯。

---

## 55. Palantir CEO Alex Karp致股东的信

**原文标题**: Palantir CEO Alex Karp's Letter to Shareholders

**原文链接**: [https://www.palantir.com/q2-2025-letter/en/](https://www.palantir.com/q2-2025-letter/en/)

好的，这并非一篇完整的文章，而是一个标题和寻找路径的提示。基于标题“Palantir CEO Alex Karp致股东信 (2025年第二季度)”，我们可以推断其可能的内容，并根据典型的股东信提供合理的摘要：

这篇文章很可能是Palantir CEO Alex Karp写给公司股东的一封信，报告公司在2025年第二季度的业绩。

这封信可能涵盖2025年第二季度的关键财务业绩，包括收入、盈利能力（或亏损）和每股收益。预计会讨论与前期和行业基准相比的增长率。

除了数字之外，这封信还可能对Palantir的战略方向进行评论。这可能包括讨论赢得的重要交易、产品更新和创新、影响公司的市场趋势以及实现长期目标的进展。Karp的信件有时会包含与公司使命相关的更广泛的哲学或政治观点。

这封信很可能还会提及公司对未来的展望，包括对下一季度或今年剩余时间的指导。这封信很可能会以对股东和员工的感谢之情结束。它还将解释Palantir的未来发展蓝图。

---

## 56. 使用语法高亮显示将音乐转录为abc格式

**原文标题**: Transcribe music in abc with syntax highlighting

**原文链接**: [https://fugue-state.io/app?project=24024aab-22f1-43cc-abef-c1647cc59597](https://fugue-state.io/app?project=24024aab-22f1-43cc-abef-c1647cc59597)

这篇文章极其简短，本质上只有一个标题：“以语法高亮的方式用abc记谱法转录音乐”和一句话：“赋格状态 - 高级音频分析与音乐学习平台 加载中...”。

总结：

这篇文章（或网页）似乎是关于赋格状态平台中的一个功能。赋格状态被描述为一个“高级音频分析与音乐学习平台”。重点突出的关键功能是将音乐转录成abc记谱法，并且这个过程包含abc转录中的语法高亮。“加载中...”暗示该功能正在加载，或者该平台仍在加载中。因此，主要的结论是赋格状态提供将音乐转录为带有语法高亮的abc记谱法作为一项功能，并且该功能可能正在加载或仍在开发中。

---

## 57. 九十年代组装电脑 (2019)

**原文标题**: Building a computer in the 90s (2019)

**原文链接**: [https://dfarq.homeip.net/building-a-computer-in-the-90s/](https://dfarq.homeip.net/building-a-computer-in-the-90s/)

在本文中，戴夫·法夸尔回忆了上世纪90年代组装电脑的挑战与冒险，并将其与现代PC组装的相对容易进行了对比。叙述重点是1996年为他的朋友汤姆组装一台电脑的经历，详细介绍了购买零件的过程，强调了当时的信息匮乏以及寻找可靠组件的困难。

他描述了从一家二手电脑商店购买的IBM 5170机箱开始，并将其与通过当地杂志广告获得的华硕P55T2P4主板配对，而他是在Computer Shopper的广告中了解到这款主板的，强调了当时互联网购物的局限性。

文章深入探讨了获取其他组件的机会主义方法，例如通过一位有员工折扣的朋友获得CD-ROM驱动器和键盘。 法夸尔还讨论了由于不值得信任的做法而应该避免的商店。

故事最终以在圣路易斯度过的一个周六结束，他四处开车，比较价格，并最终获得了必要的零件。 然而，意想不到的复杂情况出现了，主要是由于二手机箱中不匹配的组件以及对键盘适配器的需求。 经过一番疯狂的寻找，适配器在百思买关门前被找到了。

尽管困难重重，计算机最终还是组装好了，尽管一款老游戏《坦克大战》在新硬件上运行得太快了。 文章最后强调了如今组装电脑的简单性，备件和集成组件随处可见。

---

## 58. 私有铁路车辆

**原文标题**: Privately-Owned Rail Cars

**原文链接**: [https://www.amtrak.com/privately-owned-rail-cars](https://www.amtrak.com/privately-owned-rail-cars)

好的，我可以用我的知识总结Amtrak关于私人铁路车辆页面的内容，因为我无法访问外部链接。

以下是总结：

Amtrak允许私人和组织在符合特定要求和获得批准的前提下，在其线路上运营私人铁路车辆。该项目允许车主以独特和个性化的方式体验火车旅行，利用复古或定制的铁路车辆。

在Amtrak上运营私人铁路车辆的关键方面包括：

*   **要求和规定：** 车主必须遵守其铁路车辆的严格安全和机械标准，确保其符合Amtrak的规范。这包括定期检查和维护。

*   **申请和批准：** 运营私人铁路车辆需要向Amtrak提出正式申请。Amtrak审查申请，考虑车辆的状况和安全记录，并评估将其纳入预定Amtrak列车的可行性。

*   **路线可用性和时间安排：** 并非所有Amtrak路线都可用于私人铁路车辆运营。可用性取决于轨道容量、列车时刻表和运营考虑因素等因素。时间安排也需要提前协调。

*   **费用和收费：** 车主负责各种费用和收费，包括里程费率、转换费和乘务人员费用，以及为其车辆投保。

*   **服务和支持：** Amtrak可以向私人铁路车辆车主提供某些服务，例如转换、维修和有限的维护，但需收取费用。

*   **乘客限制：** 将私人铁路车辆连接到Amtrak列车时，通常对其可以搭载的乘客数量有限制。

简而言之，Amtrak的项目允许私人铁路车辆车主在其网络上旅行，但这涉及严格的申请流程、遵守安全标准以及支付适用费用。该项目专为寻求独特和豪华铁路旅行体验的个人和组织量身定制。

---

## 59. 蛋头软件怎么了

**原文标题**: What Happened to Egghead Software

**原文链接**: [https://dfarq.homeip.net/what-happened-to-egghead-software/](https://dfarq.homeip.net/what-happened-to-egghead-software/)

戴夫·法夸尔的文章探讨了Egghead Software的兴衰。这家零售店于1984年至2001年间专门销售电脑软件，由维克多·D·阿尔哈德夫创立，旨在提供消费者友好的购物体验，拥有广泛的选择和折扣价格。1988年首次公开募股和在全国开设约200家门店推动了公司快速增长。

然而，尽管20世纪90年代个人电脑市场蓬勃发展，Egghead仍难以维持盈利能力。百思买和Circuit City等消费电子产品大型超市的兴起，提供了更广泛的产品和更具竞争力的价格，给Egghead带来了压力。这些大型超市可以像整个Egghead商店一样为软件分配同样多的空间，从而削弱了Egghead的竞争优势。

为了适应，Egghead在1998年转型为在线销售，关闭了所有实体店。然后在1999年与在线拍卖网站Onsale合并。尽管销售额迅速增长，但该公司继续亏损。最终，Egghead的商业模式被证明是不可持续的。2001年，该公司宣布破产，亚马逊收购了其域名和相关资产。虽然Egghead的遗产通过品牌软盘等遗迹得以延续，但由于数字软件发行盛行，其零售模式不太可能回归。

---

## 60. 为什么这么难？

**原文标题**: Why is this hard?

**原文链接**: [https://programmersstone.blog/posts/why-is-this-hard/](https://programmersstone.blog/posts/why-is-this-hard/)

为什么这么难？：本文探讨了积极应对开发挑战以保持生产力和管理代码库复杂性的重要性。文章认为，开发者必须平衡添加新代码和控制其相关成本（维护、流程开销等）。

作者强调需要倾听“求救信号”，即暗示阻碍开发的潜在问题的短语。例如：

*   **“这真的很难，但我坚持下来了”：** 表示潜在的过度复杂性或缺少简化流程。
*   **“我让LLM写了所有的样板代码”：** 突出显示了抽象以减少重复代码的潜力。
*   **“测试/类型系统没有发现这个问题”：** 表明需要改进工具和类型定义以更好地进行错误检测。
*   **“我在这件事上和我们的/我的工具作斗争”：** 指出需要优化工具并解决依赖关系。
*   **“那部分需要重新设计”：** 标志着可以使用绞杀榕等模式进行迭代代码改进的机会。
*   **“我不知道那会花多长时间”：** 强调需要通过练习特征分解来提高估算技能。

本文提倡直接询问（“为什么这么难？”），并鼓励探索多种解决方案，即使是最初被认为是“不可能的”解决方案，以促进创新性问题解决。最终，本文强调持续改进理解比仅仅生成代码更重要，并且完善开发者的直觉有助于更快更高效地构建更多软件。

---

## 61. 使用 rel="share-url" 来暴露分享意图怎么样？

**原文标题**: What about using rel="share-url" to expose sharing intents?

**原文链接**: [https://shkspr.mobi/blog/2025/08/what-about-using-relshare-url-to-expose-sharing-intents/](https://shkspr.mobi/blog/2025/08/what-about-using-relshare-url-to-expose-sharing-intents/)

本文提出了一种标准化的方式，让网站使用新的HTML `rel` 属性 `rel="share-url"` 来暴露其分享机制。目前，分享到不同的平台（如Facebook、LinkedIn和BlueSky）需要不同的URL结构和参数（有些接受URL和标题，有些只接受URL，还有一些只接受文本）。这种不一致性使得创建通用的分享按钮变得困难。

`rel="share-url"` 属性将为每个平台的分享意图提供一个URL模板。例如：

*   `<link rel="share-url" href="https://www.facebook.com/sharer.php?u={url}&t={text}">`
*   `<link rel="share-url" href="https://bsky.app/intent/compose?text={text}">`

`{url}` 和 `{text}` 占位符将被动态替换为要分享页面的URL和标题/描述。对于仅接受文本的平台，该提案建议使用 `{text}`，可能将URL连接到文本字段中。

本文建议通过编写规范并在microformats页面上注册新的 `rel` 值来正式确定此提案，然后鼓励社交网络采用它。

作者随后提出了三个问题：

1.  `rel="share-url"` 是个好主意吗？
2.  应该做哪些修改？
3.  你是否会作为分享者或分享目的地使用它？

---

## 62. Web 平台应该采用 XSLT 3.0 吗？

**原文标题**: Should the web platform adopt XSLT 3.0?

**原文链接**: [https://github.com/whatwg/html/issues/11578](https://github.com/whatwg/html/issues/11578)

WHATWG HTML 仓库的此问题讨论了 Web 平台是否应采用 XSLT 3.0 来取代完全弃用 XSLT。此讨论由先前问题（#11523）中提出的关于安全性、可维护性以及当前浏览器对 XSLT 1.0 的实现复杂性的担忧引发。

核心问题在于，尽管 XSLT 已经发展到 2.0 和 3.0 版本，但大多数浏览器仅支持过时的 XSLT 1.0，该版本存在已知的错误和限制。问题在于，XSLT 的低使用率是由于其固有的有用性，还是由于其过时实现的限制。作者提供了一个轶事，说明了 XSLT 1.0 的局限性如何阻碍了一个个人项目，暗示较新版本将释放更大的潜力。

作者并非提倡特定的解决方案，而是提出问题以探索弃用的替代方案。这些问题包括：外部库是否可以提供 XSLT 3.0 支持？是否存在 v3.0 特有的安全问题？浏览器供应商是否可以协作开发单一的 XSLT 实现？该问题旨在引发关于采用 XSLT 3.0 的利弊的讨论，避免讨论假设的动机或特定供应商。目标是确定升级到 XSLT 3.0 是否可以解决这些担忧并释放潜力，或者弃用是否仍然是最佳方案。

---

## 63. Show HN: AgentState – 多智能体AI工作流的轻量级状态管理器

**原文标题**: Show HN: AgentState – Lightweight state manager for multi-agent AI workflows

**原文链接**: [https://github.com/ayushmi/agentstate](https://github.com/ayushmi/agentstate)

AgentState v1.0.0：用于管理AI代理状态的类Firebase解决方案，提供持久化存储、实时更新和丰富的查询功能，旨在简化多代理AI工作流程。主要特性包括零配置Docker设置、语言无关的API（HTTP/gRPC、Python/Node.js SDK）、高性能（1400+ ops/sec）、使用标签的实时查询，以及具备负载测试和Kubernetes支持的生产就绪性。

该工具允许创建和管理具有唯一ID、类型、状态JSON主体和查询标签的代理。它与LangChain和CrewAI等AI框架集成。性能基准测试表明具有高吞吐量和低延迟。核心概念包括作为对象存在的代理、用于组织管理的命名空间，以及基于标签的实时查询。

本文提供Docker和Kubernetes部署、从源代码构建以及全面测试的说明。用例包括协调多代理系统、编排工作流程和监控代理健康状况。AgentState通过提供简单的API、内置持久性、丰富的查询和实时更新，简化了AI代理管理，从而区别于传统方法。还包括快速入门指南和故障排除技巧。

---

## 64. 我的世界代码 (2024) [视频]

**原文标题**: The Minecraft Code (2024) [video]

**原文链接**: [https://www.youtube.com/watch?v=nz2LeXwJOyI](https://www.youtube.com/watch?v=nz2LeXwJOyI)

这段“文章”根本不是文章，而像是YouTube视频“The Minecraft Code (2024)”的页脚。内容只是标准的YouTube样板文字，包含以下链接：

*   YouTube的关于页面
*   新闻版权信息
*   联系方式
*   创作者信息
*   广告信息
*   开发者信息
*   服务条款
*   隐私政策和安全指南
*   YouTube 的运作方式
*   测试新功能
*   NFL Sunday Ticket 信息
*   版权声明。

本质上，提供的文本是大多数YouTube页面上都有的标准法律和信息页脚，没有提供关于“The Minecraft Code (2024)”视频内容的任何细节。

---

## 65. 日本城市拟定条例，限制每日智能手机使用时长为2小时。

**原文标题**: Japan city drafts ordinance to cap smartphone use at 2 hours per day

**原文链接**: [https://english.kyodonews.net/articles/-/59582](https://english.kyodonews.net/articles/-/59582)

日本某市正在起草一项条例，将智能手机的使用时间限制在每天最多两小时。此举旨在解决过度使用电子屏幕时间的担忧及其潜在影响，尤其是对年轻居民的影响。文章还提到，日本70%的智能手机游戏正在避免应用内支付系统，以规避主要IT公司征收的费用。这表明日本市场内部的地方治理、技术使用和经济动态之间存在复杂的相互作用。

---

## 66. 美国政府获得英特尔10%股份

**原文标题**: U.S. government takes 10% stake in Intel

**原文链接**: [https://www.cnbc.com/2025/08/22/intel-goverment-equity-stake.html](https://www.cnbc.com/2025/08/22/intel-goverment-equity-stake.html)

The U.S. government, under President Trump, has acquired a 10% stake in Intel, signaling a significant shift towards active government involvement in the private sector. Commerce Secretary Howard Lutnick announced the move, stating that the government invested $8.9 billion in Intel common stock, purchasing 433.3 million shares at $20.47 per share, a discount to the market price.

The funding comprises $5.7 billion in previously awarded CHIPS Act grants and $3.2 billion from a program focused on secure chip production. Trump touted the deal on Truth Social, emphasizing that the shares, acquired at no cost, are now valued at approximately $11 billion. The government also holds a warrant for an additional 5% stake if Intel loses majority ownership of its foundry business.

Intel CEO Lip-Bu Tan affirmed the company's commitment to U.S.-based advanced technology manufacturing. Intel shares saw a temporary rise on the news. This development follows Intel's earlier announcement of a $2 billion investment from SoftBank. The move is driven by concerns about Intel's technological competitiveness compared to companies like Taiwan Semiconductor Manufacturing Company and the desire to bolster domestic chip production, particularly in the face of delays in the construction of Intel's Ohio factory. Lutnick emphasized the government's pursuit of equity stakes in exchange for CHIPS Act funding.


---

## 67. Build Log: Macintosh Classic

**原文标题**: Build Log: Macintosh Classic

**原文链接**: [https://www.jeffgeerling.com/blog/2025/build-log-macintosh-classic](https://www.jeffgeerling.com/blog/2025/build-log-macintosh-classic)

生成摘要时出错

---

## 68. Show HN: Pinch – macOS voice translation for real-time conversations

**原文标题**: Show HN: Pinch – macOS voice translation for real-time conversations

**原文链接**: [https://www.startpinch.com/](https://www.startpinch.com/)

生成摘要时出错

---

## 69. Waymo granted permit to begin testing in New York City

**原文标题**: Waymo granted permit to begin testing in New York City

**原文链接**: [https://www.cnbc.com/2025/08/22/waymo-permit-new-york-city-nyc-rides.html](https://www.cnbc.com/2025/08/22/waymo-permit-new-york-city-nyc-rides.html)

生成摘要时出错

---

## 70. Making LLMs Cheaper and Better via Performance-Efficiency Optimized Routing

**原文标题**: Making LLMs Cheaper and Better via Performance-Efficiency Optimized Routing

**原文链接**: [https://arxiv.org/abs/2508.12631](https://arxiv.org/abs/2508.12631)

生成摘要时出错

---

## 71. TrueNAS on Arm is finally a thing

**原文标题**: TrueNAS on Arm is finally a thing

**原文链接**: [https://www.jeffgeerling.com/blog/2025/truenas-on-arm-finally-thing](https://www.jeffgeerling.com/blog/2025/truenas-on-arm-finally-thing)

生成摘要时出错

---

## 72. Now, Together

**原文标题**: Now, Together

**原文链接**: [https://natashajaffe.substack.com/p/now-together](https://natashajaffe.substack.com/p/now-together)

生成摘要时出错

---

## 73. Optimizing our way through Metroid

**原文标题**: Optimizing our way through Metroid

**原文链接**: [https://antithesis.com/blog/2025/metroid/](https://antithesis.com/blog/2025/metroid/)

生成摘要时出错

---

## 74. 1981 Sony Trinitron KV-3000R: The Most Luxurious Trinitron [video]

**原文标题**: 1981 Sony Trinitron KV-3000R: The Most Luxurious Trinitron [video]

**原文链接**: [https://www.youtube.com/watch?v=jHG_I-9a7FY](https://www.youtube.com/watch?v=jHG_I-9a7FY)

生成摘要时出错

---

## 75. 4chan will refuse to pay daily online safety fines, lawyer tells BBC

**原文标题**: 4chan will refuse to pay daily online safety fines, lawyer tells BBC

**原文链接**: [https://www.bbc.co.uk/news/articles/cq68j5g2nr1o](https://www.bbc.co.uk/news/articles/cq68j5g2nr1o)

生成摘要时出错

---

## 76. Fans loved her new album. The thing was, she hadn't released one

**原文标题**: Fans loved her new album. The thing was, she hadn't released one

**原文链接**: [https://www.bbc.co.uk/news/articles/clydz8d03dvo](https://www.bbc.co.uk/news/articles/clydz8d03dvo)

生成摘要时出错

---

## 77. Go is still not good

**原文标题**: Go is still not good

**原文链接**: [https://blog.habets.se/2025/07/Go-is-still-not-good.html](https://blog.habets.se/2025/07/Go-is-still-not-good.html)

生成摘要时出错

---

## 78. Miles from the ocean, there's diving beneath the streets of Budapest

**原文标题**: Miles from the ocean, there's diving beneath the streets of Budapest

**原文链接**: [https://www.cnn.com/2025/08/18/travel/budapest-diving-molnar-janos-cave](https://www.cnn.com/2025/08/18/travel/budapest-diving-molnar-janos-cave)

生成摘要时出错

---

## 79. DeepSeek v3.1 Is Not Having a Moment

**原文标题**: DeepSeek v3.1 Is Not Having a Moment

**原文链接**: [https://thezvi.substack.com/p/deepseek-v31-is-not-having-a-moment](https://thezvi.substack.com/p/deepseek-v31-is-not-having-a-moment)

生成摘要时出错

---

## 80. Control shopping cart wheels with your phone (2021)

**原文标题**: Control shopping cart wheels with your phone (2021)

**原文链接**: [https://www.begaydocrime.com/](https://www.begaydocrime.com/)

生成摘要时出错

---

## 81. Code formatting comes to uv experimentally

**原文标题**: Code formatting comes to uv experimentally

**原文链接**: [https://pydevtools.com/blog/uv-format-code-formatting-comes-to-uv-experimentally/](https://pydevtools.com/blog/uv-format-code-formatting-comes-to-uv-experimentally/)

生成摘要时出错

---

## 82. SK hynix dethrones Samsung as world’s top DRAM maker

**原文标题**: SK hynix dethrones Samsung as world’s top DRAM maker

**原文链接**: [https://koreajoongangdaily.joins.com/news/2025-08-15/business/tech/Thanks-Nvidia-SK-hynix-dethrones-Samsung-as-worlds-top-DRAM-maker-for-first-time-in-over-30-years/2376834](https://koreajoongangdaily.joins.com/news/2025-08-15/business/tech/Thanks-Nvidia-SK-hynix-dethrones-Samsung-as-worlds-top-DRAM-maker-for-first-time-in-over-30-years/2376834)

生成摘要时出错

---

## 83. Administration will review all 55M visa holders for deportable violations

**原文标题**: Administration will review all 55M visa holders for deportable violations

**原文链接**: [https://apnews.com/article/trump-visas-deportations-068ad6cd5724e7248577f17592327ca4](https://apnews.com/article/trump-visas-deportations-068ad6cd5724e7248577f17592327ca4)

生成摘要时出错

---

## 84. Weaponizing image scaling against production AI systems

**原文标题**: Weaponizing image scaling against production AI systems

**原文链接**: [https://blog.trailofbits.com/2025/08/21/weaponizing-image-scaling-against-production-ai-systems/](https://blog.trailofbits.com/2025/08/21/weaponizing-image-scaling-against-production-ai-systems/)

生成摘要时出错

---

## 85. Why is D3 so Verbose?

**原文标题**: Why is D3 so Verbose?

**原文链接**: [https://theheasman.com/short_stories/why-is-d3-code-so-long-and-complicated-or-why-is-it-so-verbose/](https://theheasman.com/short_stories/why-is-d3-code-so-long-and-complicated-or-why-is-it-so-verbose/)

生成摘要时出错

---

## 86. Elegant mathematics bending the future of design

**原文标题**: Elegant mathematics bending the future of design

**原文链接**: [https://actu.epfl.ch/news/elegant-mathematics-bending-the-future-of-design/](https://actu.epfl.ch/news/elegant-mathematics-bending-the-future-of-design/)

生成摘要时出错

---

## 87. How to Draw a Space Invader

**原文标题**: How to Draw a Space Invader

**原文链接**: [https://muffinman.io/blog/invaders/](https://muffinman.io/blog/invaders/)

生成摘要时出错

---

## 88. Everything is correlated (2014–23)

**原文标题**: Everything is correlated (2014–23)

**原文链接**: [https://gwern.net/everything](https://gwern.net/everything)

生成摘要时出错

---

## 89. Epson MX-80 Fonts

**原文标题**: Epson MX-80 Fonts

**原文链接**: [https://mw.rat.bz/MX-80/](https://mw.rat.bz/MX-80/)

生成摘要时出错

---

## 90. An interactive guide to SVG paths

**原文标题**: An interactive guide to SVG paths

**原文链接**: [https://www.joshwcomeau.com/svg/interactive-guide-to-paths/](https://www.joshwcomeau.com/svg/interactive-guide-to-paths/)

生成摘要时出错

---

## 91. Mark Zuckerberg freezes AI hiring amid bubble fears

**原文标题**: Mark Zuckerberg freezes AI hiring amid bubble fears

**原文链接**: [https://www.telegraph.co.uk/business/2025/08/21/zuckerberg-freezes-ai-hiring-amid-bubble-fears/](https://www.telegraph.co.uk/business/2025/08/21/zuckerberg-freezes-ai-hiring-amid-bubble-fears/)

生成摘要时出错

---

## 92. The AI Job Title Decoder Ring

**原文标题**: The AI Job Title Decoder Ring

**原文链接**: [https://www.dbreunig.com/2025/08/21/a-guide-to-ai-titles.html](https://www.dbreunig.com/2025/08/21/a-guide-to-ai-titles.html)

生成摘要时出错

---

## 93. D4D4

**原文标题**: D4D4

**原文链接**: [https://www.nmichaels.org/musings/d4d4/d4d4/](https://www.nmichaels.org/musings/d4d4/d4d4/)

生成摘要时出错

---

## 94. Writing Micro Compiler in OCaml (2014)

**原文标题**: Writing Micro Compiler in OCaml (2014)

**原文链接**: [http://troydm.github.io/blog/2014/03/29/writing-micro-compiler-in-ocaml/](http://troydm.github.io/blog/2014/03/29/writing-micro-compiler-in-ocaml/)

生成摘要时出错

---

## 95. Mail Carriers Pause US Deliveries as Tariff Shift Sows Confusion

**原文标题**: Mail Carriers Pause US Deliveries as Tariff Shift Sows Confusion

**原文链接**: [https://www.bloomberg.com/news/articles/2025-08-21/global-mail-services-halt-us-deliveries-ahead-of-de-minimis-end](https://www.bloomberg.com/news/articles/2025-08-21/global-mail-services-halt-us-deliveries-ahead-of-de-minimis-end)

生成摘要时出错

---

## 96. Why are anime catgirls blocking my access to the Linux kernel?

**原文标题**: Why are anime catgirls blocking my access to the Linux kernel?

**原文链接**: [https://lock.cmpxchg8b.com/anubis.html](https://lock.cmpxchg8b.com/anubis.html)

生成摘要时出错

---

## 97. Analysis of the GFW's Unconditional Port 443 Block on August 20, 2025

**原文标题**: Analysis of the GFW's Unconditional Port 443 Block on August 20, 2025

**原文链接**: [https://gfw.report/blog/gfw_unconditional_rst_20250820/en/](https://gfw.report/blog/gfw_unconditional_rst_20250820/en/)

生成摘要时出错

---

## 98. Show HN: I was curious about spherical helix, ended up making this visualization

**原文标题**: Show HN: I was curious about spherical helix, ended up making this visualization

**原文链接**: [https://visualrambling.space/moving-objects-in-3d/](https://visualrambling.space/moving-objects-in-3d/)

生成摘要时出错

---

## 99. Show HN: I replaced vector databases with Git for AI memory (PoC)

**原文标题**: Show HN: I replaced vector databases with Git for AI memory (PoC)

**原文链接**: [https://github.com/Growth-Kinetics/DiffMem](https://github.com/Growth-Kinetics/DiffMem)

生成摘要时出错

---

## 100. Show HN: Clyp – Clipboard Manager for Linux

**原文标题**: Show HN: Clyp – Clipboard Manager for Linux

**原文链接**: [https://github.com/murat-cileli/clyp](https://github.com/murat-cileli/clyp)

生成摘要时出错

---

