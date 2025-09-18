# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-18.md)

*最后自动更新时间: 2025-09-18 17:47:06*
## 1. 英伟达收购英特尔价值 50 亿美元股份

**原文标题**: Nvidia buys $5B in Intel

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/nvidia-and-intel-announce-jointly-developed-intel-x86-rtx-socs-for-pcs-with-nvidia-graphics-also-custom-nvidia-data-center-x86-processors-nvidia-buys-usd5-billion-in-intel-stock-in-seismic-deal](https://www.tomshardware.com/pc-components/cpus/nvidia-and-intel-announce-jointly-developed-intel-x86-rtx-socs-for-pcs-with-nvidia-graphics-also-custom-nvidia-data-center-x86-processors-nvidia-buys-usd5-billion-in-intel-stock-in-seismic-deal)

英伟达与英特尔宣布合作开发新型x86产品，标志着科技领域的一次重大转变。作为协议的一部分，英伟达将斥资50亿美元购买英特尔普通股，获得约5%的股权。

此次合作将为消费游戏市场打造“英特尔x86 RTX SOC”，通过NVLink将英特尔CPU与英伟达RTX显卡芯片集成，以实现更快的通信。英伟达还将委托英特尔为其AI产品制造定制的x86数据中心CPU。

虽然产品细节和时间表尚未公布，但两家公司致力于制定多代路线图。英伟达强调，此次合作将补充其现有产品路线图，包括基于Arm的处理器。目前尚不清楚是否会使用英特尔代工服务进行生产，但英伟达一直在探索这种可能性。

这些集成芯片旨在与AMD的APU竞争，特别是在轻薄型游戏笔记本电脑和小型PC领域。与英特尔过去与AMD的合作的一个关键区别是，新芯片采用了NVLink和统一内存访问（UMA）。英伟达将提供GPU驱动程序，而英特尔将构建和销售消费级处理器。

在数据中心方面，为英伟达定制的英特尔x86 CPU将利用NVLink，从而改善与英伟达GPU的通信。此次合作是在美国政府和软银对英特尔进行投资之后进行的，旨在加强美国的技术和制造业。

---

## 2. Slack 将我们的费用提高了每年 19.5 万美元。

**原文标题**: Slack has raised our charges by $195k per year

**原文链接**: [https://skyfall.dev/posts/slack](https://skyfall.dev/posts/slack)

面向青少年提供编程教育的非营利组织Hack Club正遭受Slack突然且大幅的价格上涨，若不支付本周额外5万美元和每年20万美元，其工作区将被关闭并删除消息记录。Hack Club在使用Slack 11年后，包括过去几年每年支付5000美元，认为这次不足一周通知的突然涨价是敲诈勒索且不合理的。他们认为像Salesforce（Slack的母公司）这样的大公司不公平地向反应时间短的小型非营利组织施压。

这次突然的最后通牒严重扰乱了Hack Club的运营，迫使员工和志愿者紧急迁移系统、重建集成并转移多年积累的知识。该组织强调了这次意外且被迫转型所带来的巨大的机会成本。

由于这次经历，Hack Club正在迁移到Mattermost，强调数据所有权的重要性，特别是对于小企业而言。作者建议其他小企业因本次事件考虑放弃Slack。

---

## 3. Launch HN：Cactus (YC S25) – 智能手机上的AI推理

**原文标题**: Launch HN: Cactus (YC S25) – AI inference on smartphones

**原文链接**: [https://github.com/cactus-compute/cactus](https://github.com/cactus-compute/cactus)

Cactus (YC S25) 推出专为移动设备设计的节能型 AI 推理框架和内核，尤其针对占据市场 70% 以上的经济型和中端手机。与针对高端设备优化的现有框架不同，Cactus 从头开始构建，没有任何依赖项，因此适用于所有手机。

即使在仅使用 CPU 的实现中，Cactus 也表现出令人印象深刻的性能，在 Pixel 6a 等旧款手机上达到每秒 16-20 个 tokens，在预期的新型号上达到每秒 50-70 个 tokens。该架构提供四个抽象级别：Cactus FFI（OpenAI 兼容的 C API）、Cactus Engine（高级 Transformer 引擎）、Cactus Graph（统一的零拷贝计算图）和 Cactus Kernels（低级 ARM 专用 SIMD 操作）。Cactus Graph 作为一个通用的数值计算框架，允许自定义模型和科学计算。

Cactus Engine 构建在 Cactus Graphs 之上，提供通过 Cactus Foreign Function Interface 访问的 Transformer 推理引擎，从而可以轻松创建语言绑定。SDK 已经在生产中使用，每周处理超过 500,000 个推理任务。该框架可以在 Apple Silicon Macbook 上进行测试，提供不错的性能。

路线图包括支持更多模型（Gemma、SmolVLM 等）、高端手机上的硬件加速（SMMLA、NPU 和 DSP）、用于更大模型（1B+）的 INT4 支持以及用于移植 Torch/JAX 模型的 Python 工具。初步结果显示，Qwen3-4B-INT4 在 iPhone 16 Pro NPU 上实现了 21 t/s。创建者强调，对于通用计算机（AMD/Intel/Nvidia），HuggingFace 和 Llama.cpp 等现有框架更适合。

---

## 4. TernFS – 艾字节级、多区域分布式文件系统

**原文标题**: TernFS – An exabyte scale, multi-region distributed filesystem

**原文链接**: [https://www.xtxmarkets.com/tech/2025-ternfs/](https://www.xtxmarkets.com/tech/2025-ternfs/)

XTX开发的TernFS分布式文件系统简介：TernFS是一个由算法交易公司XTX开发的分布式文件系统，旨在处理其EB级存储需求。由于现有解决方案存在局限性，XTX构建了TernFS来支持公司不断增长的计算需求。TernFS现已在GitHub上开源。

TernFS旨在扩展到数十EB和数百万客户端，跨多个区域冗余地存储数据，并以经济高效的方式利用各种存储类型。它通过其API和一个Linux内核模块公开读/写访问，需要的外部依赖项很少。主要限制包括文件不可变、不适合存储微小文件以及目录创建/删除吞吐量较慢。

该架构包含四个核心服务：存储目录结构和文件元数据的元数据分片，用于跨分片事务的跨目录协调器（CDC），存储文件内容的块服务，以及用于服务发现和监控的注册表。元数据被分成256个分片，每个分片都有一个leader和followers以实现冗余。CDC处理跨多个分片的事务，但可能成为目录操作的瓶颈。文件内容被分割成块并由块服务（通常是驱动器）存储，并通过TCP API访问。

TernFS支持多区域部署，并对元数据和文件内容进行异步复制。元数据复制指定一个位置作为主位置。文件内容被主动和按需复制。通信使用一种称为bincode的自定义二进制序列化格式，以提高效率和内核兼容性。

---

## 5. 美国草原保护区在蒙大拿州新增7万英亩土地

**原文标题**: American Prairie unlocks another 70k acres in Montana

**原文链接**: [https://earthhope.substack.com/p/victory-for-public-access-american](https://earthhope.substack.com/p/victory-for-public-access-american)

美国草原保护区或新增蒙大拿州七万英亩土地：概要

---

## 6. KDE现在是我最喜欢的桌面。

**原文标题**: KDE is now my favorite desktop

**原文链接**: [https://kokada.dev/blog/kde-is-now-my-favorite-desktop/](https://kokada.dev/blog/kde-is-now-my-favorite-desktop/)

作者是一位长期使用Sway的用户，为了方便妻子使用，已将游戏主机上的系统切换到KDE。起初他有些犹豫，但现在对KDE印象深刻，认为其在易用性和功能方面堪比Windows和macOS。

KDE因其功能完备而受到赞扬，它提供了详细的网络信息、带有智能裁剪的集成截图工具以及强大的窗口管理选项。作者强调了拥有内置工具带来的便利，例如Flatpak权限管理、硬件信息访问（SMART状态）和防止睡眠模式，无需使用第三方应用程序。

除了功能之外，作者还强调了KDE的速度，主观上认为它在同一硬件上比Windows 11更快，甚至比MacBook Pro上的macOS更流畅。KDE与其之前的Sway设置之间的性能差异微乎其微。

虽然KDE并非完美，例如在多显示器设置中存在最初的任务栏问题，但作者的整体体验是积极的。他最后表达了对KDE的真诚喜爱，并赞扬开发人员创造了如此全面且用户友好的桌面环境。

---

## 7. Luau - 快速、小巧、安全、渐进式类型的脚本语言，源于 Lua

**原文标题**: Luau – Fast, small, safe, gradually typed scripting language derived from Lua

**原文链接**: [https://luau.org/](https://luau.org/)

Luau 是一种脚本语言，它从 Lua 5.1 衍生而来，由 Roblox 大幅演进，以满足大规模游戏开发的需求。它优先考虑性能、易用性、语言工具，并引入了渐进类型。

主要特性包括：

*   **沙盒化：** Luau 实施严格的沙盒化，以安全地执行来自不同来源（游戏开发者与 Roblox）的代码。
*   **兼容性：** 旨在向后兼容 Lua 5.1，同时有选择地整合来自更高版本 Lua 的特性，并在设计选择不同的地方进行差异化处理。
*   **语法：** Luau 在语法上与 Lua 5.1 向后兼容，同时提供符合人体工程学的扩展。
*   **分析工具：** 通过 `luau-analyze` 提供代码检查和类型检查，以帮助开发者编写正确的代码。
*   **性能：** 拥有定制的前端、新的字节码、解释器和编译器，经过优化以提高速度，并为 x64 和 arm64 平台提供可选的 JIT 编译。
*   **库：** Luau 在语言方面是 Lua 5.1 的超集，但对其标准库进行了更改，删除了一些函数，并添加了其他函数。嵌入式应用程序可以提供额外的特定于应用程序的库功能。

---

## 8. Flipper Zero 盖革计数器

**原文标题**: Flipper Zero Geiger Counter

**原文链接**: [https://kasiin.top/blog/2025-08-04-flipper_zero_geiger_counter_module/](https://kasiin.top/blog/2025-08-04-flipper_zero_geiger_counter_module/)

本文档介绍了两个用于盖革计数器的Flipper Zero应用程序：盖革计数器应用和原子骰子掷器应用。

**盖革计数器应用**提供了放射性的可视化表示，显示每秒计数 (CPS) 和每分钟计数 (CPM)。它具有记录功能、缩放功能和单位转换选项（cpm、μSv/h、mSv/y、Rad/h、mRad/h、uRad/h）。可以通过将A4 GPIO连接到A7 GPIO来在没有盖革管的情况下测试该应用。它将记录的数据以CSV文件格式存储在SD卡上，包括epoch时间和CPS。该应用最适用于β射线和γ射线，适用于天然铀、钍、镭、钴-60和碘-131等放射源。

**原子骰子掷器应用**基于检测到的放射性粒子的时间戳生成真正的随机数。它使用CRC32（适用于低放射性）或MD5（适用于高放射性）哈希方法。它可以输出骰子点数 (1-6) 或硬币翻转结果 (0-1)。 CPS显示在左上角，可用掷骰次数显示在右上角。空气中的氡子体可用作放射源，使放射源成为可选。

本文档强调了这些应用程序的教育目的，并强调在用户自己的设备上负责任地使用。 它还指出，这些模块已在Unleashed和Momentum第三方固件上进行了测试。

---

## 9. 悲伤如人，皆有尽时。

**原文标题**: Grief gets an expiration date, just like us

**原文链接**: [https://bessstillman.substack.com/p/oh-fuck-youre-still-sad](https://bessstillman.substack.com/p/oh-fuck-youre-still-sad)

无法访问文章链接。

---

## 10. AI辅助软件的质量取决于工作单元管理。

**原文标题**: The quality of AI-assisted software depends on unit of work management

**原文链接**: [https://blog.nilenso.com/blog/2025/09/15/ai-unit-of-work/](https://blog.nilenso.com/blog/2025/09/15/ai-unit-of-work/)

Atharva Raykar 认为，AI辅助软件开发的质量很大程度上取决于有效管理工作单元，并强调“上下文工程”至关重要。他指出，仅仅拥有智能AI模型是不够的，提供正确的上下文才是关键。

文章解释说，“大小合适”的工作单元可以优化上下文窗口，从而产生更好的代码生成。信息太少会导致AI幻觉或不协调的代码，而信息过多则会使AI不堪重负。

Raykar 展示了在多轮AI工作流程中错误是如何累积的，以及现实世界软件项目的“混乱性”（路径依赖、动态、没有明确的反事实）如何显著降低AI的成功率。他认为，管理上下文对于稳健性至关重要，而不仅仅是提高AI智能。

作者提倡将项目分解为小的、人类可读的工作单元，这些单元在每个检查点都能提供可验证的业务价值。他建议将用户故事作为一个好的起点，因为它们在业务价值和AI上下文之间取得了平衡。他将这种方法与主要提供技术价值的AI“规划”模式进行了对比。

最后，Raykar 介绍了 StoryMachine 实验，以测试使用用户故事加上“一些额外的东西”作为AI辅助开发的最佳工作单元的有效性。目标是通过有效管理工作单元，使AI辅助开发减少随机性，更加可靠。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 2 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 3 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 4 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 5 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 6 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 7 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 8 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 9 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 10 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 11 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 12 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 13 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 14 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 15 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 16 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 17 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 18 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 19 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 20 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 21 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 22 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 23 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 24 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 25 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 26 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 27 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 28 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 29 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 30 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 31 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 32 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 33 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 34 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 35 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 36 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 37 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 38 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 39 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 40 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 41 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 42 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 43 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 44 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 45 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 46 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 47 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 48 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 49 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 50 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 51 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 52 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 53 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 54 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 55 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 56 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 57 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 58 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 59 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 60 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 61 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 62 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 63 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 64 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 65 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 66 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 67 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 68 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 69 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 70 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 71 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 72 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 73 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 74 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 75 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 76 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 77 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 78 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 79 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 80 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 81 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 82 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 83 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 84 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 85 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 86 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 87 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 88 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 89 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 90 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 91 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 92 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 93 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 94 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 95 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 96 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 97 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 98 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 99 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 100 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 101 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 102 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 103 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 104 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 105 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 106 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 107 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 108 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 109 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 110 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 111 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 112 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 113 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 114 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 115 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 116 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 117 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 118 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 119 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 120 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 121 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 122 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 123 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 124 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 125 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 126 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 127 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 128 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 129 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 130 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 131 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 132 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 133 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 134 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 135 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 136 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 137 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 138 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 139 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 140 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 141 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 142 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 143 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 144 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 145 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 146 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 147 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 148 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 149 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 150 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 151 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 152 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 153 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 154 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 155 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 156 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 157 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 158 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 159 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 160 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 161 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 162 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 163 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 164 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 165 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 166 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 167 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 168 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 169 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 170 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 171 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 172 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 173 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 174 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 175 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 176 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 177 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 178 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 179 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 180 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 181 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 182 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 183 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
