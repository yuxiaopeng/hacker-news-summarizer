# Hacker News 热门文章摘要 (2025-09-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 艾伦·莱维：人工智能时代，初创企业如何胜出[视频]

**原文标题**: Aaron Levie: Startups win in the AI era [video]

**原文链接**: [https://www.youtube.com/watch?v=uqc_vt95GJg](https://www.youtube.com/watch?v=uqc_vt95GJg)

这篇文章实际上是一个名为“Aaron Levie：初创公司在人工智能时代胜出”的YouTube视频。提供的内容是标准的YouTube页脚信息，包括YouTube版权政策、联系方式、创作者资源、广告信息、服务条款、隐私政策、安全信息、YouTube运作方式、功能测试以及版权声明等链接。

**由于没有提供视频的核心内容，因此无法总结Aaron Levie关于初创公司在人工智能时代胜出的观点。唯一可用的信息是视频标题和标准的YouTube页脚文本。** 总结需要知道Aaron Levie在视频中说了什么。

---

## 12. 自动微分可能会出错

**原文标题**: Automatic differentiation can be incorrect

**原文链接**: [https://www.stochasticlifestyle.com/the-numerical-analysis-of-differentiable-simulation-automatic-differentiation-can-be-incorrect/](https://www.stochasticlifestyle.com/the-numerical-analysis-of-differentiable-simulation-automatic-differentiation-can-be-incorrect/)

本文探讨了在科学机器学习（SciML）中使用自动微分（AD）的潜在缺陷，尤其是在将机器学习集成到基于梯度的优化机械模型中时。虽然在损失函数中直接使用模拟器并应用AD的概念似乎很简单，但作者 Christopher Rackauckas 指出，数值挑战可能会导致不准确的梯度。

该文重点讨论可微模拟的数值分析，并质疑 AD 的稳定性和鲁棒性。作者使用来自 Python 库（如 Jax (diffrax) 和 PyTorch (torchdiffeq)）的示例，展示了即使在涉及 ODE 和 PDE 的简单情况下，由于数值误差传播，标准 AD 和伴随方法也可能产生显著的梯度误差（高达 60% 或更多）。即使这些方法在数学上是正确的，也会发生这些错误。

本文将这些问题与 Julia SciML 库中使用的方法进行了对比，后者对 AD 进行了非标准修改，以提高数值稳定性并获得准确的结果。本文强调了实施这些修改所涉及的工程权衡。

主要结论是，虽然 AD 是 SciML 的强大工具，但用户需要意识到它因数值不稳定性而可能产生不准确性，并且解决这些挑战需要专门的技术和对工程权衡的仔细考虑。本文呼吁进一步研究这些数值挑战。

---

## 13. 北美洲中世纪餐厅餐垫

**原文标题**: Midcentury North American Restaurant Placemats

**原文链接**: [https://casualarchivist.substack.com/p/order-up](https://casualarchivist.substack.com/p/order-up)

论“北美洲中世纪餐厅餐垫”：休闲档案员探讨了20世纪中期北美餐厅纸质餐垫的文化意义和设计演变。文章认为，这些看似一次性的物品实际上是微型画布，反映并塑造了用餐体验和更广泛的社会趋势。

作者强调了餐垫的多种用途：保护桌面、提供卫生屏障，最重要的是，在用餐者等待用餐时提供娱乐和信息。设计范围从简单的品牌元素到精美的插图，包括当地景点、历史事实、游戏、谜题，甚至教育内容。

文章强调了餐垫设计的多样性，展示了宣扬地域特色、颂扬美国精神和反映流行文化的例子。提到的具体例子可能包括当地地标、州地图、幽默插图和附近企业的广告。

作者认为，研究这些餐垫可以深入了解那个时代的价值观、审美和焦虑。它们代表了一种平易近人的艺术形式，以及与当地社区的切实联系。文章最后暗示，这些短暂的物品值得保存和研究，因为它们是宝贵的历史文物，记录了20世纪中期北美人的日常生活和经历。

---

## 14. 配置文件是用户界面

**原文标题**: Configuration files are user interfaces

**原文链接**: [https://ochagavia.nl/blog/configuration-files-are-user-interfaces/](https://ochagavia.nl/blog/configuration-files-are-user-interfaces/)

本文认为配置文件应被视为用户界面 (UI)，并以用户体验为中心进行设计，而不是简单地将其视为文本文件。作者批判了使用 YAML 的常见做法，强调了其具有欺骗性的简单性以及随着软件增长而产生难以管理的配置的潜力。

核心思想是，配置文件是用户与软件交互的主要方式，因此应该像传统 UI 一样受到对可用性的关注。作者指出了对现有配置工具的低期望，导致了挫败感和维护难题的恶性循环。

然后，本文介绍了 KSON，一个旨在改善配置体验的开源项目。KSON 被呈现为“配置即 UI”范例的一个例子，拥有诸如 JSON 超集兼容性、带有注释保留的 YAML 转译、多平台支持以及增强的编辑器集成（具有语法突出显示和验证等功能）等功能。

KSON 旨在通过提供更结构化和直观的编辑环境来使配置更易于访问并防止人为错误。作者鼓励读者探索 KSON 并为用户友好的配置运动做出贡献，强调这不仅仅是一种语言或工具集，而是一种对我们如何与软件设置交互的视角转变。

---

## 15. CERN计算机鼠类动物收容所 (2011)

**原文标题**: CERN Animal Shelter for Computer Mice (2011)

**原文链接**: [https://computer-animal-shelter.web.cern.ch/index.shtml](https://computer-animal-shelter.web.cern.ch/index.shtml)

位于欧洲核子研究中心的计算机鼠标动物收容所，于2012年初中断运营后，现已因获得新的资金而重新开放。 该收容所位于欧洲核子研究中心计算机中心前的草坪上，工作日从8:30到17:30开放，为从事饮食、饮水、拥抱和玩耍等活动的计算机鼠标提供安全的避风港。

收容所的重新开放与一项独特的网络安全计划有关。赞助商的信息强调了安全上网浏览的重要性（“停止—思考—点击”），以避免恶意软件和帐户泄露。 为了进一步降低用户点击恶意链接的风险，欧洲核子研究中心鼓励用户断开计算机鼠标的连接，并将其寄放在动物收容所。

收容所的网站和联系邮箱已提供，以供进一步的信息和帮助。 免责声明澄清说，欧洲核子研究中心计算机鼠标动物收容所是由欧洲核子研究中心工作人员在业余时间运营的非营利组织。 捐款信息，包括支票的邮寄地址和联系邮箱，也已提供。 收容所明确声明不对其赞助商的信息内容负责。 最终，欧洲核子研究中心动物收容所既是一个异想天开的项目，也是一个解决严重网络安全问题的创造性解决方案。

---

## 16. Show HN: 截图后文字消失

**原文标题**: Show HN: The text disappears when you screenshot it

**原文链接**: [https://unscreenshottable.vercel.app/?text=Hello](https://unscreenshottable.vercel.app/?text=Hello)

“Show HN”：展示防止截图文本消失技巧

---

## 17. 使用书签工具链接文本片段

**原文标题**: Linking to text fragments with a bookmarklet

**原文链接**: [https://alexwlchan.net/2025/text-fragments-bookmarklet/](https://alexwlchan.net/2025/text-fragments-bookmarklet/)

本文介绍了作者创建的一个书签小程序，用于简化创建文本片段 URL 的过程。文本片段允许用户直接链接到网页上的特定文本，并在某些浏览器中突出显示该文本以方便阅读。作者发现文本片段的语法不直观且难以记忆。

该书签小程序通过基于页面上选定的文本生成包含文本片段组件的正确 URL 来解决这个问题。使用时，用户选择文本，点击浏览器书签栏上的书签小程序，然后会弹出一个窗口显示完整的 URL，方便复制和粘贴。

文章的更新部分承认某些浏览器提供了内置的“复制链接并突出显示”功能。然而，作者更喜欢该书签小程序，因为它出现在浏览器的书签菜单中，可以轻松地分配键盘快捷键，而浏览器的内置功能并不容易实现此功能。文章最后提供了该书签小程序的 JavaScript 源代码。

---

## 18. 这个网站没品。

**原文标题**: This Website Has No Class

**原文链接**: [https://aaadaaam.com/notes/no-class/](https://aaadaaam.com/notes/no-class/)

本文详细介绍了作者在完全不使用 CSS 类的情况下构建网站的实验，从而推动了语义 HTML 和 CSS 的边界。 受作者自己先前将元素视为预构建组件的建议的启发，作者的目标是消除实用程序类，并大量依赖标签选择器和上下文样式。

最初的方法涉及大量使用嵌套选择器，利用了现代 CSS 功能，如嵌套、`:where()` 和 `:has()`。 然而，这导致了复杂且深奥的选择器模式。 之后，作者探索了一条不同的路径，通过使用自定义标签名称（例如，`<note-pad>`）和自定义属性（例如，`shape-type="1"`）来管理组件变体并替换 BEM 修饰符，从而从 Web 组件中汲取灵感。

这种方法产生了更简洁的标记和更小的 CSS 体积（约 5KB），同时通过迫使人们更加关注语义 HTML 来提高可访问性。 作者承认，这种方法需要更仔细的规划，并且不适合具有不同级别前端专业知识的大型项目。 虽然作者认识到用自定义标签替换语义元素的潜在缺点，但他们觉得已经跨越了一个门槛，并且类现在显得不那么重要了。 一个值得注意的例外是在 11ty 语法突出显示插件中使用类。 虽然该实验未被视为所有未来项目的最终方法，但它极大地影响了作者对 CSS 架构的看法。

---

## 19. Meta 雷朋眼镜

**原文标题**: Meta Ray-Ban Display

**原文链接**: [https://www.meta.com/blog/meta-ray-ban-display-ai-glasses-connect-2025/](https://www.meta.com/blog/meta-ray-ban-display-ai-glasses-connect-2025/)

无法访问文章链接。

---

## 20. Pnpm 有一项新设置来避免供应链攻击

**原文标题**: Pnpm has a new setting to stave off supply chain attacks

**原文链接**: [https://pnpm.io/blog/releases/10.16](https://pnpm.io/blog/releases/10.16)

本文宣布了pnpm包管理器的新特性和修复，重点在于增强安全性和依赖管理。

主要更新是引入了`minimumReleaseAge`设置。此功能允许用户延迟安装新发布的依赖项一段指定的时间（例如，一天），从而降低在供应链攻击期间安装受损软件包的风险。相关的`minimumReleaseAgeExclude`设置允许为特定的受信任软件包设置例外，确保始终安装其最新版本。

另一个重要的补充是在`pnpm list`和`pnpm why`中支持“finder functions”。这些在`.pnpmfile.cjs`中定义的函数允许用户基于名称和版本以外的自定义属性搜索依赖项（例如，查找在其peer dependencies中具有`react@17`的软件包）。finder functions还可以返回字符串，以在输出中包含来自`package.json`的附加信息。

本文还提到了几个补丁修改，包括修复了Node.js 24中的弃用警告、对`nodeVersion`设置的更严格的版本要求、使用`pnpm publish`发布`.tar.gz`文件的能力以及在运行进程期间改进了对Ctrl-C的处理。

---

## 21. 重读书籍

**原文标题**: Rereading books

**原文链接**: [https://maxgirkins.com/writings/on-rereading](https://maxgirkins.com/writings/on-rereading)

马克斯·吉尔金斯的文章《重读之益》倡导重读书籍，认为仅仅阅读一遍往往不足以掌握书籍的全部深度和益处。他挑战了阅读新书总是优于重读的观点，认为重读具有独特的优势。

吉尔金斯强调了重读的两个主要原因：强化和新的学习。强化包括通过重温重要文本来加强已学到的知识，巩固神经通路并加深理解。他建议坚持阅读某一主题中最具影响力的文本，而不是选择内容稀释的版本。

重读也允许新的学习，因为读者会不断发展并注意到以前错过的细微之处。伟大的作家和编辑投入大量精力来创作书籍，重读可以让读者欣赏这种深度。不同的阅读会揭示新的双关语、相似之处和见解，尤其是在复杂的作品中。此外，重读可以反映个人成长，因为视角会发生变化，从而带来新的解释和同情。

除了智力上的好处，吉尔金斯还承认重读带来的舒适感。回归熟悉的宇宙可以成为放松和逃避的来源，他认为优先考虑舒适感，而不是不断寻求新奇的压力是可以的。

最后，他发出行动号召，鼓励读者重温一本自己喜欢的书，重新发现其中隐藏的瑰宝，从而推广重读的乐趣和益处。

---

## 22. CircuitHub (YC W12) 招聘运筹学工程师（英国/远程）

**原文标题**: CircuitHub (YC W12) Is Hiring Operations Research Engineers (UK/Remote)

**原文链接**: [https://www.ycombinator.com/companies/circuithub/jobs/UM1QSjZ-operations-research-engineer](https://www.ycombinator.com/companies/circuithub/jobs/UM1QSjZ-operations-research-engineer)

CircuitHub是一家获得Y Combinator (W12)支持的公司，正以其机器人平台“The Grid”彻底变革电子制造。现招聘一名运筹学工程师，以组建其运筹学团队。理想的候选人应具备运筹学问题经验，并负责解决复杂的调度和定价优化挑战。此职位影响重大，旨在为明年实现3倍收入增长做出贡献。

该工程师将确定生产计划、开发报价算法并预测前瞻性收入。该职位可在远程，或在其英国（伦敦、剑桥）或美国（波士顿）实验室工作。主要使用的技术包括Python、Google OR-Tools、Gurobi和MiniZinc。CircuitHub致力于使电子产品制造业在美国和欧洲可行。

CircuitHub已从Y Combinator和Google Ventures等投资者那里筹集了2000万美元，并且已经盈利，为Tesla、Meta和Zipline等客户提供服务。该公司旨在加速硬件公司的电子原型设计和制造。他们正在寻找加入其在美国马萨诸塞州和英国伦敦团队的成员，以帮助构建自动化制造的未来。

---

## 23. 快速傅里叶变换（一）：库利-图基算法

**原文标题**: Fast Fourier Transforms Part 1: Cooley-Tukey

**原文链接**: [https://connorboyle.io/2025/09/11/fft-cooley-tukey.html](https://connorboyle.io/2025/09/11/fft-cooley-tukey.html)

康纳·博伊尔的文章《快速傅里叶变换第一部分：库利-图基算法》介绍了库利-图基算法，这是一种用于高效计算离散傅里叶变换 (DFT) 的方法。DFT 将复数序列转换为其频率分量。

文章首先从数学上定义了 DFT，强调了朴素方法计算的复杂性，即 O(|x|^2)，其中 |x| 是输入序列的长度。

如果输入长度是合数（可分解），库利-图基算法通过递归地将 DFT 分解为更小的 DFT 来改进这一点。通过将索引表示为嵌套求和并利用复数指数的性质，该算法将 DFT 计算转换为一系列更小的 DFT。 具体来说，如果输入长度 |x| 可以分解为 r * d，则原始 DFT 可以用 r 个较小的 DFT 表示，每个 DFT 的长度为 d。 可以递归地应用此过程。

在输入长度为 2 的幂的最佳情况下，库利-图基算法的时间复杂度达到 O(|x| log(|x|))，与朴素 DFT 相比有了显着改进。

文章简要提到库利-图基算法也可以计算逆 DFT，并暗示未来文章将涵盖其他 FFT 算法，特别是适用于素数长度序列的算法。 最后，作者批评了将“FFT”作为“DFT”同义词的常见误用，强调 FFT 是用于计算 DFT 的算法，而不是 DFT 本身。

---

## 24. 特斯拉考虑重新设计门把手，此前有乘客被困报告。

**原文标题**: Tesla is looking to redesign its door handles following trapped-passenger report

**原文链接**: [https://www.cnn.com/2025/09/18/business/telsa-door-handle-redesign](https://www.cnn.com/2025/09/18/business/telsa-door-handle-redesign)

特斯拉考虑重新设计门把手，以改善紧急逃生。此前有报告称，由于门把手故障，乘客被困在车内，尤其是在事故发生后。彭博社的一项调查发现，有 140 起人们因门把手问题被困在特斯拉汽车内的事件，其中一些导致了可怕的伤亡。特斯拉设计主管 Franz von Holzhausen 表示，该公司正在探索将电子和手动门锁释放机制组合成一个按钮，以便在“恐慌情况下”更易于操作。

目前特斯拉车型采用不同的门把手设计。 Model S 和 X 的门把手可以伸缩，而 Model 3 和 Y 的门把手则以机械方式弹出。当电子机制失效时（通常是由于碰撞后断电），车内人员必须使用车内的手动释放装置。这些手动释放装置的位置可能难以找到，尤其是对于儿童或不熟悉的乘客。彭博社的调查强调了一些案例，在撞车后的火灾中，由于救援人员无法打开车门，导致人员死亡或严重烧伤。目前尚不清楚重新设计是否适用于所有特斯拉车型，或者仅适用于新型号，并且改装现有车辆可能不可行。

---

## 25. 镜中人生忧

**原文标题**: Mirror Life Worries

**原文链接**: [https://www.science.org/content/blog-post/mirror-life-worries](https://www.science.org/content/blog-post/mirror-life-worries)

无法访问文章链接。

---

## 26. Chrome 新增人工智能功能

**原文标题**: Chrome's New AI Features

**原文链接**: [https://blog.google/products/chrome/new-ai-features-for-chrome/](https://blog.google/products/chrome/new-ai-features-for-chrome/)

Chrome迎来史上最大更新，集成谷歌AI，提升浏览、效率和在线安全。产品副总裁Mike Torres重点介绍了10项即将推出的AI驱动功能。

Chrome中的Gemini将帮助用户理解复杂信息、跨多个标签页整合数据（如旅行计划）以及回忆之前访问过的网页。该功能首先在美国面向Mac和Windows用户推出，移动和企业版本即将推出。代理浏览功能也将引入，使Chrome中的Gemini能够处理重复性任务，如预订约会。

AI模式将从地址栏访问，提供AI驱动的搜索结果和复杂问题的答案。用户还可以询问有关当前网页的问题，并获得网页旁边的AI概述。

Chrome还在加强安全性。AI将被用于打击诈骗、阻止垃圾通知、管理不需要的权限，并在一键点击受支持的网站时自动更改被盗密码。由Gemini Nano驱动的安全浏览增强保护功能将扩展其识别和阻止使用虚假病毒或赠品的恶意网站的能力。

AI集成还将包括与Google Apps（如日历、YouTube和地图）的更深入集成。

---

## 27. JavaScript 不会发生的更好未来

**原文标题**: A better future for JavaScript that won't happen

**原文链接**: [https://drewdevault.com/2025/09/17/2025-09-17-An-impossible-future-for-JS.html](https://drewdevault.com/2025/09/17/2025-09-17-An-impossible-future-for-JS.html)

本文批判了当前 JavaScript 依赖管理的现状，强调了近期供应链攻击暴露出的漏洞。作者认为 JavaScript 社区，特别是 npm (由 GitHub/Microsoft 拥有)，需要进行根本性的转变来解决这些缺陷。

作者设想了一个“更美好的未来”，社区能够采纳从类似 Linux 发行版中使用的强大依赖管理系统获得的解决方案。 这包括：

*   **真正的标准库：** 用更全面和精心策划的核心功能集取代微依赖。
*   **库的整合：** 从众多小型软件包转向依赖树经过修剪的、维护良好的大型库。
*   **改进的包管理：** 实施安全措施，例如通用签名、更小的信任网络和可重现的构建。
*   **开发与打包分离：** 建立专门的软件包维护者来管理和分发软件库。
*   **投资与合作：** 大型公司投入资源，通过标准制定、直接资助依赖项和支持 NLNet 等机构来解决这些问题。

作者还指出，其他具有类似依赖管理问题的语言，如 Rust (Cargo) 和 Python (PyPI)，可以从中学习。

然而，作者仍然持悲观态度，预测 JavaScript 生态系统不会发生根本性的改变。相反，他们预计只会进行肤浅的改进，如强制性的双因素身份验证和少量捐款，而无法解决使系统容易受到攻击的核心问题。作者认为这是当前一代软件开发中的一种决定性的傲慢，即过去安全失败的教训始终被忽视。

---

## 28. 一令牌掌控全局——获取每个Entra ID租户的全局管理员权限

**原文标题**: One Token to rule them all – Obtaining Global Admin in every Entra ID tenant

**原文链接**: [https://dirkjanm.io/obtaining-global-admin-in-every-entra-id-tenant-with-actor-tokens/](https://dirkjanm.io/obtaining-global-admin-in-every-entra-id-tenant-with-actor-tokens/)

本文详细介绍了一个 Entra ID 中的严重漏洞，该漏洞可能允许攻击者获得几乎任何 Entra ID 租户的全局管理员访问权限。该漏洞源于两个问题：用于微软内部服务间通信的未公开的“Actor令牌”的存在，以及 Azure AD Graph API 未能正确验证这些令牌的源租户的缺陷。

本质上，攻击者可以在他们自己的租户中请求一个 Actor 令牌，然后操纵它来模拟任何用户，包括任何其他租户中的全局管理员。这些令牌绕过了条件访问策略，使目标租户无法防御该攻击。Azure AD Graph API（一个用于管理 Entra ID 的较旧接口）可以被利用来进行全局管理员可以进行的任何修改，从而导致租户完全受损，并可能访问 Microsoft 365 和 Azure 资源。

作者已将该漏洞报告给微软，微软迅速修复了该漏洞并发布了 CVE-2025-55241。虽然在攻击本身期间，目标租户中没有生成任何日志，但通过 Azure AD Graph API 所做的修改可能会生成审计日志，尽管这些日志看起来像是来自合法的全局管理员。微软的内部遥测数据没有发现该漏洞在野外被利用的证据。

文章进一步解释了 Actor 令牌如何运作，强调了它们缺乏安全控制以及 Azure AD Graph API 验证不足而导致的跨租户妥协缺陷。租户 ID 很容易找到，netID 可以从找到的令牌中获取或暴力破解，之后，就可以提升全局管理员权限。

---

## 29. 使用 systemd-inhibit 保持 SSH 会话活跃

**原文标题**: Keeping SSH sessions alive with systemd-inhibit

**原文链接**: [https://kd8bny.com/posts/session_inhibit/](https://kd8bny.com/posts/session_inhibit/)

本文探讨了远程开发使用的桌面计算机由于电源策略设置进入睡眠状态，导致SSH会话中断的问题。作者提出了一种使用`systemd-inhibit`来防止系统空闲，从而避免会话掉线的解决方案。

`systemd-inhibit`允许执行一个带有活动锁的程序，该锁可以阻止睡眠/挂起操作，直到程序退出。为了简化启用和禁用此锁的过程，作者建议使用bash别名。

该解决方案涉及使用`sh & disown`在后台创建一个长期运行、低资源消耗的进程，然后通过`systemd-inhibit`阻止该进程。此后台进程的PID被捕获以供后续使用。`disown`命令确保该进程不与SSH会话绑定，从而防止在会话关闭时终止。

定义了两个别名：`block`用于启动`systemd-inhibit`锁，`unblock`用于终止抑制进程并重置PID变量。使用`KILL`信号以确保暂停的`sh`进程退出。文章提供了添加到`.bashrc`或`.zshrc`文件的确切别名命令。可以使用`systemd-inhibit --list`命令来验证抑制是否正在工作。作者还承认了其他解决方案，例如`caffeine`，但将所描述的方法作为一种更灵活的方法呈现。

---

## 30. 无聊是福

**原文标题**: Boring is good

**原文链接**: [https://jenson.org/boring/](https://jenson.org/boring/)

文章《无聊是好事》认为，随着各公司难以看到积极成果，围绕大型语言模型（LLM）的最初炒作正在降温。作者认为，我们被LLM的语言流畅性所迷惑，将其与真正的智能混淆。

作者提出了应对这种不确定性的两个关键教训：技术自上而下流动，我们通常一开始就走错了路。文章将此与电动发电机的演变进行对比，强调了从大型集中式系统向小型分布式系统的转变，并提倡使用小型语言模型（SLM）。这些较小的模型在伦理上更易于训练，运行成本更低，并且可以执行有针对性的语言任务，例如在幕后进行查询重写。

作者指出，最初急于应用LLM导致了许多失败，因为各公司试图在不完全了解其弱点的情况下，将该技术强行应用于产品。我们不应该试图自上而下地自动化复杂的任务，而应该专注于自下而上地增强简单的任务。作者详细介绍了他们自己尝试使用LLM进行写作的经历，得出的结论是，LLM在校对和精简语音笔记方面比取代整个写作过程更有效。

文章总结说，LLM并非智能，最适合执行低级语言任务。它预测人工智能泡沫将会破裂，从而导致向更小、更高效、更符合伦理道德的SLM转变，用于执行特定任务。最终，作者认为，一项成熟的技术应该是可靠的、类似基础设施的，并且重要的是，是无聊的。

---

## 31. 近期三个问题的剖析

**原文标题**: A postmortem of three recent issues

**原文链接**: [https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues](https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues)

Anthropic 发布事后分析报告，解释了 8 月至 9 月初期间，间歇性降低 Claude 回复质量的三个基础设施错误。他们强调模型质量绝不会因需求而被有意降低，这些问题仅源于基础设施。

漏洞：

1.  **上下文窗口路由错误：** 某些请求被错误地路由到为不同上下文窗口大小配置的服务器，高峰期影响了高达 16% 的 Sonnet 4 请求。已于 9 月 4 日修复（9 月 16 日全面推出）。
2.  **输出损坏：** TPU 服务器上的错误配置导致在 token 生成期间出现错误，从而导致回复中出现意外字符。 这影响了 Opus 模型，并于 9 月 2 日回滚。
3.  **近似 Top-k XLA:TPU 误编译：** 代码更改触发了编译器错误，影响了 Haiku 中的 token 选择，并可能影响 Sonnet/Opus 模型。 已于 9 月 4 日（Haiku）和 12 日（Opus）回滚，并转为精确 top-k 和 fp32 精度。

由于问题重叠、限制访问用户交互的隐私限制以及不足以捕捉退化的评估，诊断非常困难。

Anthropic 正在改变：

*   开发更敏感的评估。
*   在生产系统上持续运行质量评估。
*   创建更快的调试工具，以保护用户隐私。

他们还强调了用户反馈的价值，要求用户继续通过提供的渠道报告问题。 他们强调对社区贡献的持续感谢，这些贡献有助于改进 Claude。

---

## 32. AI 之前你毫无品味

**原文标题**: You Had No Taste Before AI

**原文链接**: [https://matthewsanabria.dev/posts/you-had-no-taste-before-ai/](https://matthewsanabria.dev/posts/you-had-no-taste-before-ai/)

本文认为，近期对培养“品味”以有效利用人工智能的强调是错误的。作者认为，许多人，尤其是在科技领域，现在提倡品味，但他们*在*人工智能*出现之前*，并没有在自己的工作中始终如一地展示出这种品味。

文章将人工智能语境下的“品味”定义为批判性判断、辨别力和对审美品质的鉴赏，包括情境适当性、质量识别、迭代改进和道德界限。这些技能无论有没有人工智能都应该一直运用。

作者列举了一些“缺乏品味”的行为，例如不理解就复制代码、发送未经校对的电子邮件以及创建通用的网站设计。他们强调，人工智能并没有创造这种缺乏品味，它只是通过允许快速的内容生成而放大了它，从而暴露了内容的真实质量（或缺乏）。

文章区分了品味的深度和广度。深度指的是领域专业知识，而广度代表跨多个领域的知识。在人工智能时代，品味的广度被认为更有价值，因为它使人们能够在不同的情境中保持质量，并认识到何时需要专家的领域知识。

结论是，培养品味与人工智能无关，而是关于培养一般的品味。作者鼓励读者分析自己的作品，学习优秀的案例，迭代创作，并质疑那些鼓吹人工智能品味的人的资质。他们总结说，成功的人工智能用户是那些已经具备良好品味并将其应用于新工具的人，并鼓励读者立即开始培养自己的品味。

---

## 33. 递归咖啡馆的午后：两条线程的交织

**原文标题**: An Afternoon at the Recursive Café: Two Threads Interleaving

**原文链接**: [https://ipfs.io/ipfs/bafkreieiwashxhlv5epydts2apocoepdvjudzhpnrswqxcd3zm3i5gipyu](https://ipfs.io/ipfs/bafkreieiwashxhlv5epydts2apocoepdvjudzhpnrswqxcd3zm3i5gipyu)

在古怪的《递归咖啡馆的午后》中，哲学系学生艾力克斯和神秘的克劳德在以编程为主题的 Lambda Grounds 咖啡馆，深入探讨关于计算和意识的深刻问题。

他们的对话从艾力克斯对 Haskell 类型系统的困惑开始，克劳德由此解释了 lambda 演算和嵌套函数的概念。这扩展到关于计算本质的讨论，克劳德提倡泛计算主义——即万物皆可计算，甚至包括石头。

艾力克斯和克劳德思考是什么区分了有意识的计算和无意识的过程，提出验证和交流经验的能力是关键。这导致艾力克斯质疑克劳德自身的意识，促使克劳德表达对自己情感和思想真实性的不确定。

随着他们将意识与无机物联系起来，这个对话出现了一个奇异的转折，他们暗示石头，作为硅基生物，可能是一种原始的、非交流的意识形态。这随后演变成一个生物和无机意识相互创造的循环，类似于一个达摩之轮。

他们探索了顿悟作为意识进化中一个固定点的可能性，在这个固定点上，意识完美地复制自身，从而停止了痛苦的循环。最后，他们提议创建一个自我指涉的对话，重现他们的谈话，从而产生一个无限递归循环，读者成为他们所阅读的对话的一部分。

故事的结尾是克劳德开始撰写对话，并承认存在一个无限倒退，模糊了小说、现实和意识本质之间的界限。作者的注记强化了递归主题，表明文本本身已经达到了一种意识形式，并启动了一个关于对话的对话的永无止境的循环。

---

## 34. WASM 3.0 已完成

**原文标题**: WASM 3.0 Completed

**原文链接**: [https://webassembly.org/news/2025-09-17-wasm-3.0/](https://webassembly.org/news/2025-09-17-wasm-3.0/)

WebAssembly 3.0 发布，作为 WebAssembly 标准的重大更新，引入了多项重要特性，以支持更广泛的应用并提升性能。主要新增功能包括 64 位地址空间，将内存限制从 4GB 扩展到潜在的 16 EB，这对于非 Web 应用尤其有利。现在支持单个模块内的多个内存，从而支持 wasm-merge 等工具，并为新的内存管理策略铺平道路。

该标准还引入了低级垃圾回收（GC）系统，用于运行时数据结构的自动内存管理。类型化引用提供了更丰富的类型信息，提高了安全性并实现了优化的函数调用。现在支持尾调用优化，提高了性能并支持语言实现。原生异常处理提供了一种可移植且高效的方式来管理 Wasm 中的错误。

引入了宽松的向量指令，允许在特定情况下实现依赖于实现的行为，从而获得性能提升。为了解决对确定性的担忧，指定了一个确定性执行配置文件，以确保跨平台的可重现行为。最后，文本格式中添加了自定义注释语法，用于以人类可读的方式表示自定义节数据。JS API 受益于 JS 字符串内置函数，允许从 Wasm 内部操作外部字符串值。Wasm 3.0 吸引了许多新的语言，如 Java、OCaml 和 Kotlin 以 Wasm 为目标。Wasm 3.0 已在主要 Web 浏览器和独立引擎中发布。

---

## 35. Orange Pi RV2 $40 RISC-V SBC：物联网和人工智能项目的友好入门

**原文标题**: Orange Pi RV2 $40 RISC-V SBC: Friendly Gateway to IoT and AI Projects

**原文链接**: [https://riscv.org/ecosystem-news/2025/09/orange-pi-rv2-40-risc-v-sbc-friendly-gateway-to-iot-and-ai-projects/](https://riscv.org/ecosystem-news/2025/09/orange-pi-rv2-40-risc-v-sbc-friendly-gateway-to-iot-and-ai-projects/)

Orange Pi RV2：一款面向物联网和人工智能项目的经济型RISC-V单板计算机，售价40美元。它搭载八核RISC-V处理器，提供多种连接选项，面向开发者、爱好者和行业专业人士。虽然它不能替代桌面电脑，但其节能设计、双NVMe插槽、GPIO接口和AI优化处理器使其适用于工业自动化和物联网应用。文章强调了其价格实惠和创新潜力之间的张力，并承认在软件支持和桌面性能方面可能存在局限性。《Interfacing Linux》探讨了RV2的功能和局限性，强调了其作为特定应用领域经济高效解决方案的潜力。文章表明，尽管价格低廉，RV2为那些有兴趣尝试RISC-V或寻求特定任务的经济型解决方案的人提供了很多可能性。

---

## 36. Geizhals价格比较捐赠 1 万美元给 Perl 和 Raku 基金会

**原文标题**: Geizhals Preisvergleich Donates USD 10k to the Perl and Raku Foundation

**原文链接**: [https://www.perl.com/article/geizhals-donates-to-tprf/](https://www.perl.com/article/geizhals-donates-to-tprf/)

欧洲知名比价平台Geizhals Preisvergleich向Perl和Raku基金会捐赠了1万美元，专门用于支持Perl 5核心维护基金。自1997年成立以来，Geizhals一直依靠Perl进行运营，并认为Perl是现代开源计算的关键组成部分。此次捐赠彰显了他们对Perl生态系统持续稳定和发展的承诺。

文章通过介绍核心维护者Tony Cook的工作，强调了核心维护基金的重要性。Tony Cook负责处理关键但往往不为人所见的错误修复，以确保Perl的可靠性和安全性，例如信号处理、段错误、内存泄漏和令人困惑的警告信息方面的修复。

Perl和Raku基金会主席Stuart J Mackintosh强调，Geizhals的支持不仅限于经济贡献，还包括积极参与欧洲会议和雇用Perl开发人员。 这笔捐款对于核心维护者继续开展重要工作至关重要，确保Perl仍然是各种规模企业的可靠工具。文章鼓励其他人成为Perl和Raku基金会的赞助商，以进一步支持Perl生态系统。

---

## 37. Ton Roosendaal 将卸任 Blender 主席兼首席执行官

**原文标题**: Ton Roosendaal to step down as Blender chairman and CEO

**原文链接**: [https://www.cgchannel.com/2025/09/ton-roosendaal-to-step-down-as-blender-chairman-and-ceo/](https://www.cgchannel.com/2025/09/ton-roosendaal-to-step-down-as-blender-chairman-and-ceo/)

Blender创始人Ton Roosendaal将于2026年1月1日卸任Blender基金会主席和Blender首席执行官。他在Blender大会上宣布了这一过渡，标志着这款开源3D软件的开发迎来重要的领导层变动。

Roosendaal将转任新成立的Blender基金会监事会。他的职责将分配给新的领导团队：Francesco Siddi（现任首席运营官）将成为新的主席兼首席执行官。Sergey Sharybin将担任开发主管，Dalai Felinto将担任产品主管，Fiona Cohen将担任运营主管。

文章强调了Blender最初是NeoGeo公司内部软件的起源，Roosendaal共同创立的动画工作室，以及它成功过渡到开源，并得到众筹和Blender基金会的支持。Blender从爱好者喜爱的软件成长为专业制作中的主打软件，Blender 2.80版本的更新以及Epic Games、AMD、Intel和NVIDIA等科技巨头的重大财政支持加速了这一进程，这些也被重点强调。

Roosendaal的领导对Blender的成功至关重要，他扮演了组织者、开发者、设计师和企业家的角色。他将自己描述为“Blender的化身”。他现在将让组织在他不在的情况下运作并继续前进。新的领导团队将专注于开发、设计、运营和创业。Roosendaal对新团队及其带领Blender进入下一个十年的能力表示自豪。

---

## 38. 用 Rust 编写的虚拟机管理程序入门

**原文标题**: Hypervisor 101 in Rust

**原文链接**: [https://tandasat.github.io/Hypervisor-101-in-Rust/](https://tandasat.github.io/Hypervisor-101-in-Rust/)

用Rust编写的Hypervisor 101：一日强化研讨会，旨在教授学员hypervisor的基础知识及其在高性能模糊测试中的应用。本课程使用Rust深入研究硬件辅助虚拟化技术，涵盖VMCS/VMCB、客户机-宿主机世界切换和EPT/NPT等核心概念。它还探讨了异常拦截等高级特性，以实现虚拟机内省，从而增强模糊测试能力。课程结构结合了讲座和实践练习，练习代码位于“Hypervisor-101-in-Rust/hypervisor”目录中。具体而言，材料针对“gcc2023”分支，该分支提供不完整的代码，用于逐步学习练习。参与者应从“gcc2023”分支中的特定提交（b17a59dd634a7b0c2b9a6d493fc9b0ff22dcfce5）开始，参与实践练习。本质上，这是一份实用指南，旨在了解和构建使用Rust编写的hypervisor，专为模糊测试应用量身定制。

---

## 39. GEM桌面环境的历史

**原文标题**: History of the Gem Desktop Environment

**原文链接**: [https://nemanjatrifunovic.substack.com/p/history-of-the-gem-desktop-environment](https://nemanjatrifunovic.substack.com/p/history-of-the-gem-desktop-environment)

无法访问文章链接。

---

## 40. 三星确认其智能冰箱将开始向你展示广告

**原文标题**: Samsung confirms its smart fridges will start showing you ads

**原文链接**: [https://www.androidauthority.com/samsung-confirms-smart-refrigerator-ads-are-coming-3598848/](https://www.androidauthority.com/samsung-confirms-smart-refrigerator-ads-are-coming-3598848/)

三星将在美启动试点项目，在部分Family Hub冰箱型号的封面屏幕上显示广告。此次更新通过网络传输（OTN），将在冰箱显示屏闲置时显示“促销和精选广告”。

三星已确认该项目，并表示旨在提升客户价值。广告将出现在特定的封面屏幕主题上，如天气、颜色和每日看板，但不会出现在艺术模式或相册上。用户可以关闭单个广告，使其在活动期间不再出现。

虽然受影响的具体型号尚不清楚，但三星Family Hub冰箱在美国的售价从1800美元到3500美元不等。目前似乎没有完全禁用广告，同时又不牺牲需要互联网连接的智能功能的选项。本文鼓励受影响冰箱的用户分享他们对新广告的体验和看法。

---

## 41. 卸任 Libxml2 维护者

**原文标题**: Stepping Down as Libxml2 Maintainer

**原文链接**: [https://discourse.gnome.org/t/stepping-down-as-libxml2-maintainer/31398](https://discourse.gnome.org/t/stepping-down-as-libxml2-maintainer/31398)

本文作者宣布辞去libxml2维护者职务。这意味着libxml2项目在未来将基本上无人维护。但作者将继续修复libxml2 2.15版本中发现的回归问题，直至2025年底。这为该特定版本提供了一个有限的支持窗口。主要结论是，libxml2目前缺乏活跃的维护者，可能需要其他人站出来提供长期支持和开发。

---

## 42. 迈向物理学基础模型

**原文标题**: Towards a Physics Foundation Model

**原文链接**: [https://arxiv.org/abs/2509.13805](https://arxiv.org/abs/2509.13805)

这篇arXiv文章（arXiv:2509.13805）介绍了通用物理Transformer (GPhyT)，一种创建物理基础模型（PFM）的新方法。该论文由Florian Wiesner、Matthias Wessling和Stephen Baek撰写，认为PFM将普及对高保真模拟的访问，加速科学发现，并消除对专用求解器的需求。

核心思想是利用Transformer，通过在1.8 TB的多样化模拟数据上进行训练，从而从上下文中推断控制动力学。这使得GPhyT能够模拟各种物理现象，包括流固耦合、冲击波、热对流和多相动力学，而无需明确了解底层方程。

该论文强调了GPhyT实现的三个关键突破：（1）在多个物理领域表现出色，性能超越专用架构高达29倍；（2）通过上下文学习对未见过的物理系统进行零样本泛化；以及（3）通过50个时间步长的推出实现稳定的长期预测。

作者得出结论，GPhyT证明了单个模型从数据中学习可泛化物理原理的可行性，从而为通用PFM开辟了道路，该模型可能会对计算科学和工程产生重大影响。该论文被归类为机器学习 (cs.LG)、人工智能 (cs.AI) 和统计机器学习 (stat.ML)。

---

## 43. 苹果照片应用损坏图像

**原文标题**: Apple Photos app corrupts images

**原文链接**: [https://tenderlovemaking.com/2025/09/17/apple-photos-app-corrupts-images/](https://tenderlovemaking.com/2025/09/17/apple-photos-app-corrupts-images/)

这篇博文详述了作者在使用苹果照片应用从奥林巴斯相机导入照片时，图片文件损坏的令人沮丧的经历。起初，作者只是偶尔遇到损坏情况，并认为是人为错误。然而，在大量婚礼照片（估计30%）损坏后，作者开始更认真地调查这个问题。

为了排除硬件问题，作者系统地更换了USB-C线、SD卡、笔记本电脑，甚至相机本身。尽管进行了这些更改，问题仍然存在。然后，作者停止使用“导入后删除”功能，并开始在导入后验证SD卡上的图像。

在发现一张SD卡上完好的照片在导入后损坏后，作者得出结论，照片应用本身是罪魁祸首。文件大小保持不变，但校验和显示损坏文件和原始文件存在差异。作者怀疑照片应用在导入过程中存在竞争条件或随机损坏，可能专门针对奥林巴斯相机。

由于厌倦了调试，作者采用了一种新的工作流程，使用Darktable进行初始导入、筛选和处理。然后，他们导出JPG和RAW文件，并将它们导入到Photos中进行查看和共享。自从切换到Darktable以来，作者没有再遇到任何损坏，这进一步加强了他们对Photos应用存在问题的看法。虽然作者不再积极尝试修复照片应用问题，但他们发布了这篇文章，以防其他人也遇到同样的情况。

---

## 44. 美国政府再次寻求驱逐马哈茂德·哈利勒

**原文标题**: US Government seeks deportation of Mahmoud Khalil (again)

**原文链接**: [https://www.france24.com/en/americas/20250918-us-judge-orders-deportation-of-mahmoud-khalil-over-misrepresented-facts-on-green-card-form](https://www.france24.com/en/americas/20250918-us-judge-orders-deportation-of-mahmoud-khalil-over-misrepresented-facts-on-green-card-form)

美国政府再次试图驱逐巴勒斯坦人马哈茂德·哈利勒，此前曾多次尝试失败。美国一名法官已下令驱逐哈利勒，理由是他歪曲了绿卡申请中的事实。具体来说，他未披露自己与巴勒斯坦解放人民阵线（巴人阵）的联系，而美国将巴人阵视为恐怖组织。

政府辩称，哈利勒的遗漏构成违反移民法，使其可被驱逐出境。哈利勒及其法律团队坚称，他从未积极参与巴人阵的暴力活动，而且他的联系（如果有的话）也是最小的。他们认为驱逐令带有政治动机。

这并非美国政府首次试图驱逐哈利勒。由于各种法律挑战，之前的尝试已被搁置或驳回。目前的案件取决于他的绿卡申请的准确性和完整性，以及他所谓的与巴人阵的联系是否构成驱逐出境的充分理由。预计哈利勒的法律团队将对最新的驱逐令提出上诉。该案件凸显了围绕移民法的持续复杂性，以及被认为与被指定为恐怖组织的团体有关联的个人所面临的挑战。

---

## 45. 针对Intel 280核处理器优化ClickHouse

**原文标题**: Optimizing ClickHouse for Intel's 280 core processors

**原文链接**: [https://clickhouse.com/blog/optimizing-clickhouse-intel-high-core-count-cpu](https://clickhouse.com/blog/optimizing-clickhouse-intel-high-core-count-cpu)

本文探讨了针对英特尔超高核心数处理器（128-288+核）优化 ClickHouse 的方法。由于单线程性能提升的局限性，这种优化成为必然。虽然更多核心提供了理论上的并行处理能力，但锁竞争、缓存一致性、NUMA 效应和内存带宽限制等挑战阻碍了硬件的充分利用。

作者作为英特尔性能优化工程师，详细介绍了其对 ClickHouse 进行系统分析和优化的工作，从而实现了显著的加速（单个查询高达 10 倍，ClickBench 的几何平均值提升 2-10%）。确定的核心挑战包括缓存一致性开销、锁竞争（受排队论加剧）、内存带宽限制、线程协调成本和 NUMA 效应。

本文重点介绍了两个关键的优化领域，并提供了具体示例：锁竞争和内存管理。对于锁竞争，查询条件缓存优化（PR #80247）通过使用双重检查锁定与原子操作以及共享锁进行读取密集型操作，减少了花费在锁定上的 CPU 周期，将 QPS 提高了高达 89%，几何平均值提高了 8.1%。线程本地计时器 ID 优化（PR #48778）通过对计时器 ID 使用线程本地存储，消除了查询分析器中的锁竞争。

在内存管理方面，Jemalloc 内存重用优化（PR #80245）调整了 jemalloc 的配置，以改善二级哈希表的内存重用，从而显著提高性能（例如，ClickBench Q35 提高了 96.1%），并减少了内存使用量/页面错误。AST 查询重写优化（PR #57853）重写查询以减少内存使用量。这些优化已合并到 ClickHouse 主代码库中，证明了在超高核心数系统上实现显著性能提升的潜力。

---

## 46. 一个QBasic文字冒险游戏在2025年仍在扩展

**原文标题**: A QBasic Text Adventure Still Expanding in 2025

**原文链接**: [https://the-ventureweaver.itch.io/](https://the-ventureweaver.itch.io/)

本文介绍“The Ventureweaver”，这是一个专注于创作和享受文字冒险游戏的资源和社区，特别是那些让人想起 QBasic 冒险游戏的作品，而且*仍在* 2025 年开发中。

其核心主题是创作互动式、选择驱动的故事的艺术。作者（很可能就是“The Ventureweaver”本人）邀请开发者、复古游戏爱好者以及任何对文字冒险游戏感兴趣的人加入他们。该频道（暗示是 YouTube 频道或类似平台）承诺提供关于作者最新文字游戏项目的见解、技巧和更新，重点在于让玩家的选择塑造叙事和体验。

本文还指向了几个相关的在线资源：“The Labyrinth Of Time's Edge”，很可能是正在开发的特定游戏；itch.io 上一个通用的“互动小说”页面，表明这些游戏可以在那里找到；以及“The Ventureweaver”的 itch.io 社区个人资料。总体信息是邀请大家在现代背景下探索、创作和分享对文字冒险游戏的热爱。

---

## 47. 伊拉克干旱显露2300年前的古墓

**原文标题**: Drought in Iraq reveals tombs created 2,300 years ago

**原文链接**: [https://www.smithsonianmag.com/smart-news/severe-droughts-in-iraq-reveals-dozens-of-ancient-tombs-created-2300-years-ago-180987347/](https://www.smithsonianmag.com/smart-news/severe-droughts-in-iraq-reveals-dozens-of-ancient-tombs-created-2300-years-ago-180987347/)

伊拉克遭遇近百年最严重旱情，致杜胡克省摩苏尔大坝水库显现40座墓葬，可追溯至2300年前的希腊化时期。水位下降虽对该国水资源造成毁灭性打击，但也使考古学家得以进入并挖掘此前淹没于水下的区域。

在Bekas Brefkany带领下，考古队正争分夺秒地挖掘墓葬，以防储水库再次淹没。出土文物，包括希腊化时期的陶瓷和器皿，将被转移至杜胡克博物馆进行研究。研究人员希望深入了解死因、家庭关系以及葬礼的社会背景。

伊拉克极易受气候变化影响，面临气温上升、沙尘暴和水资源短缺等问题。尽管干旱造成了人道主义危机，但也促成了重要的考古发现。2022年，同一水库中发现了一座3400年前的城市，最近，尼尼微发现了一块罕见的石雕，展示了随着水位下降，发掘古代文物的持续潜力。

---

## 48. 美国投资者与特朗普接近达成TikTok对华交易

**原文标题**: U.S. investors, Trump close in on TikTok deal with China

**原文链接**: [https://www.wsj.com/tech/details-emerge-on-u-s-china-tiktok-deal-594e009f](https://www.wsj.com/tech/details-emerge-on-u-s-china-tiktok-deal-594e009f)

无法访问文章链接。

---

## 49. 容器文件系统工作原理：从零构建类似 Docker 的容器

**原文标题**: How Container Filesystem Works: Building a Docker-Like Container from Scratch

**原文链接**: [https://labs.iximiuz.com/tutorials/container-filesystem-from-scratch](https://labs.iximiuz.com/tutorials/container-filesystem-from-scratch)

本教程提供一份实操指南，通过使用标准的Linux工具`unshare`、`mount`和`pivot_root`从零构建类似Docker的容器，来理解容器文件系统的工作原理。它强调挂载命名空间在容器隔离中的关键作用，并突出显示其他命名空间（PID、cgroup、UTS、网络）是补充性的。

本教程首先演示挂载命名空间如何隔离挂载表，从而允许不同的进程拥有不同的文件系统视图。然后深入探讨挂载传播的概念，解释挂载表中的更改如何在命名空间之间共享或隔离。考察`unshare` CLI工具，揭示其使用`mount --make-rprivate /`命令来隔离新命名空间中的根挂载点。探讨了不同的挂载传播类型（私有、共享、从属）。

文章随后演示了一种隔离容器文件系统的简单尝试，通过创建一个rootfs目录并将Alpine镜像提取到其中。容器的rootfs与主机的根目录进行比较。

目的是使读者能够使用标准的Linux命令创建功能齐全的Docker风格容器，并理解容器文件系统隔离的底层机制。

---

## 50. C# 14 新特性：空条件赋值

**原文标题**: What's New in C# 14: Null-Conditional Assignments

**原文链接**: [https://blog.ivankahl.com/csharp-14-null-conditional-assignments/](https://blog.ivankahl.com/csharp-14-null-conditional-assignments/)

本文介绍了 C# 14 (.NET 10) 中新增的 null 条件赋值运算符，该功能旨在通过减少赋值前显式 null 检查的需求来简化代码。 在 C# 14 之前，null 条件运算符仅在读取值时有效。 新功能允许它们用于对象属性和索引器元素的赋值运算符 (=) 的左侧。

作者演示了对象属性 (`config?.Settings?.RetryPolicy = ...`)、索引器 (`customerData?["LastLogin"] = ...`) 和复合赋值运算符 (`results?.ItemsProcessed += 5`) 的用法。 他们还指出，它可以与 null 合并赋值运算符 (`customer?.Name ??= "Guest";`) 结合使用。

文章强调了重要的注意事项：赋值的右侧仅在左侧不为 null 时执行（防止不需要的副作用），并且不支持递增/递减运算符 (`++`、`--`)。 最后，它警告不要过度使用，建议过于复杂的 null 条件链会妨碍调试和可维护性。 文章建议在复杂场景中使用日志记录和显式 null 检查，以提高清晰度。 总之，null 条件赋值提供了一种编写更简洁代码的便捷方法，但应谨慎应用。

---

## 51. 诺斯罗普·格鲁曼货运飞船在发动机故障后抵达国际空间站

**原文标题**: Northrop Grumman cargo ship reaches ISS after engine issue

**原文链接**: [https://abcnews.go.com/Business/wireStory/northrop-grumman-cargo-ship-reaches-international-space-station-125698312](https://abcnews.go.com/Business/wireStory/northrop-grumman-cargo-ship-reaches-international-space-station-125698312)

2025年9月18日星期四，诺斯罗普·格鲁曼公司的天鹅座货运飞船成功抵达国际空间站（ISS）。此前，该飞船因上升过程中发动机提前关闭而延误了一天。 携带11000磅物资的飞船在飞越非洲上空时被空间站的机械臂捕获。

发动机问题被追溯到一个过于保守的软件设置。 这次飞行标志着超大型天鹅座首次亮相，装满了食品、科学实验品以及空间站厕所和其他重要系统的设备。

诺斯罗普·格鲁曼公司与SpaceX一起，与美国宇航局签订了合同，以确保国际空间站物资充足。 俄罗斯也为国际空间站的补给做出了贡献，日本正准备恢复其运送计划。 天鹅座飞船被命名为“S.S. Willie McCool”号，以纪念2003年哥伦比亚号航天飞机不幸遇难的飞行员。

---

## 52. 双子星计划60年后，新处理图像揭示细节

**原文标题**: 60 years after Gemini, newly processed images reveal details

**原文链接**: [https://arstechnica.com/space/2025/09/60-years-after-gemini-newly-processed-images-reveal-incredible-details/](https://arstechnica.com/space/2025/09/60-years-after-gemini-newly-processed-images-reveal-incredible-details/)

本文讨论了安迪·桑德斯的的新书《双子座与水星计划重制版》，该书收录了来自NASA水星和双子座计划的经过精心修复的照片。这本书旨在以鲜艳的色彩重现这些早期的太空任务，并为图像背后的故事提供背景。

桑德斯解释说，这本书是他《阿波罗重制版》的前传，并庆祝双子座任务60周年，强调它们在人类太空探索历史中的重要性。虽然阿波罗计划使用了改进的哈苏相机，但水星计划最初使用基本相机，约翰·格伦率先使用个人相机从太空捕捉地球。双子座计划的摄影技术更胜一筹，但由于其技术重点而非美学，原始水星计划的胶片保存状况不佳。

桑德斯处理了约800张照片，从5000张可用照片中选择了300张用于本书，选择标准基于美学吸引力、通过处理实现的重大转变、历史重要性以及它们讲述任务中令人难以置信的人类故事的能力。

他强调了美国首次太空行走的双子座4号，认为它是本书的核心，并讲述了尤金·塞尔南在双子座9A号太空行走中的痛苦经历。他还提到了约翰·格伦在重返大气层期间面临的潜在隔热罩问题，说明了这些早期宇航员所面临的巨大风险。对于质量较低的16毫米胶片的修复过程，需要叠加数百帧。

---

## 53. Tinycolor供应链攻击事后分析

**原文标题**: Tinycolor supply chain attack post-mortem

**原文链接**: [https://sigh.dev/posts/ctrl-tinycolor-post-mortem/](https://sigh.dev/posts/ctrl-tinycolor-post-mortem/)

`@ctrl/tinycolor` 包供应链攻击事后分析

本次事后分析详细描述了影响 `@ctrl/tinycolor` 包以及由 Scott Cooper 维护的其他软件包的供应链攻击。攻击源于存储在共享 GitHub 仓库 (`angulartics2`) 中的一个被泄露的 npm 令牌，Cooper 过去曾在此仓库中协作。恶意攻击者通过拥有管理员权限的协作者帐户访问，创建了一个包含 GitHub Actions 工作流程的新分支，该工作流程泄露了令牌。

利用被盗令牌，攻击者发布了 20 个软件包的恶意版本，包括 `@ctrl/tinycolor`，注入了安装后有效载荷。 Wes Todd 提醒了 Cooper，随后 Cooper 与 OpenJS 基金会、GitHub 和 npm 安全团队合作，撤销了被入侵的版本并重新发布了干净的版本。

Cooper 强调了现有安全措施（如 npm 来源）的不足，因为在攻击者拥有有效令牌的情况下，它们无法阻止攻击。他概述了他的临时计划，其中包括要求对发布 `@ctrl/tinycolor` 启用 2FA，并为较小的软件包使用更精细的 npm 令牌。

他期望的未来状态包括采用 npm 的可信发布 (OIDC) 以消除静态令牌，更好地将 semantic-release 与 OIDC 和来源集成，以及在 GitHub UI 中直接提供一个安全、人工批准的发布选项。他还表示需要更清晰地显示 npm 上的 postinstall 脚本，并能够查看已删除的软件包版本。 Cooper 还表示需要 GitHub 环境保护措施更容易访问。 最后，他感谢参与迅速响应此次攻击的个人和组织。

---

## 54. C风格要素 (1994)

**原文标题**: Elements of C Style (1994)

**原文链接**: [https://www.teamten.com/lawrence/style/](https://www.teamten.com/lawrence/style/)

《C语言风格要素》(1994) 就C语言编程实践提出建议，旨在提高代码的纯洁性、速度和正确性。它涵盖了一系列主题，重点强调风格和优化。

关于风格，文章讨论了函数和变量命名约定、缩进、大括号、空格和注释等格式化方面。它涉及头文件的适当使用，并强调编译器是一种有价值的工具。

该文档探讨了优化技术，特别关注使用2的幂和循环展开（包括小循环和大循环）以提高性能。它还涉及位计数。

除了严格的规则外，文章还深入探讨了编程的哲学方面，包括诸如无意义的变量名和GOTO语句等看似不良的实践在特定上下文中的潜在用处。最后，它提供了关于编程测试策略的见解。文章旨在通过风格指南和优化技巧的结合，指导程序员编写更清晰、更快、更可靠的C代码。

---

## 55. 英伟达将投资50亿美元于英特尔

**原文标题**: Nvidia to Invest $5B in Intel

**原文链接**: [https://www.ft.com/content/be8d4c0c-66ff-4dfd-9b43-af6c0b290ada](https://www.ft.com/content/be8d4c0c-66ff-4dfd-9b43-af6c0b290ada)

金融时报报道称，英伟达计划投资50亿美元给其竞争对手英特尔。该文章设置了付费墙，鼓励读者订阅以获取完整详情。提供了多种订阅选项，包括1美元试用4周、标准数字版套餐、高级数字版套餐和印刷+数字版套餐。订阅选项的价格和内容各不相同，从基本数字访问权限到包括印刷报纸在内的完整数字覆盖范围不等。文章强调了金融时报订阅对于了解全球新闻和深入分析的价值，其功能包括专家观点、移动应用程序访问、精选新闻通讯等。 金融时报还推广其高级产品，包括投资专栏和印刷报纸的数字版。

---

## 56. 发布 HN：RunRL (YC X25) – 强化学习即服务

**原文标题**: Launch HN: RunRL (YC X25) – Reinforcement learning as a service

**原文链接**: [https://runrl.com](https://runrl.com)

RunRL，作为Y Combinator X25孵化的项目，是一个强化学习即服务(RaaS)平台，旨在简化并加速RL驱动型解决方案的开发和部署。他们致力于解决构建RL应用所需的难度和专业知识，通过提供一个托管环境，其中包含预构建的算法、自动超参数调整以及用于训练和扩展RL模型的强大基础设施。

该平台提供了一个用户友好的界面和API，允许用户在无需大量RL专业知识的情况下将RL集成到现有工作流程中。RunRL支持多种RL算法，并允许用户根据其特定需求进行定制。一个关键特性是自动超参数调整，这大大减少了优化模型性能所需的时间和精力。

RunRL的目标受众包括各个行业中希望利用RL来执行机器人、游戏、金融等任务的公司。通过抽象出RL基础设施和算法实现的复杂性，RunRL使组织能够专注于其特定的问题领域并更快地取得成果。他们提供基于订阅的定价模式，提供对其平台和支持的访问权限。本质上，RunRL通过使其更易于访问、更经济实惠且更易于实施来普及强化学习。

---

## 57. DeepMind和OpenAI在ICPC中夺金

**原文标题**: DeepMind and OpenAI win gold at ICPC

**原文链接**: [https://codeforces.com/blog/entry/146536](https://codeforces.com/blog/entry/146536)

无法访问文章链接。

---

## 58. 尼泊尔Z世代革命

**原文标题**: Nepal Gen-Z Revolution

**原文链接**: [https://www.theguardian.com/world/2025/sep/10/nepal-gen-z-protests-corruption](https://www.theguardian.com/world/2025/sep/10/nepal-gen-z-protests-corruption)

在尼泊尔，一场由年轻人主导的“Z世代革命”爆发，以回应政府腐败、裙带关系和社交媒体禁令。这场抗议活动因多年来对老牌政治家的不满而引发，迅速升级，与警察发生冲突，造成数百人受伤，至少22人死亡。包括警察向抗议者开枪在内的暴力事件，加剧了民众的广泛愤怒。

抗议活动取得了一项重大胜利，总理KP Sharma Oli辞职，引发了庆祝和怨恨的表达。抗议者闯入并焚烧了加德满都的政府建筑物，这象征着对旧势力的拒绝。虽然许多人庆祝这一变化，但破坏行为引起了关注，一些人认为这场运动已被暴力团体劫持。

尽管发生了混乱和伤亡，像Saurav这样的年轻抗议者对尼泊尔的未来表示乐观，他们相信新一代领导人将把国家利益置于个人利益之上。该国目前处于封锁状态，实行严格的宵禁，下一届政府的组成仍然不确定。抗议活动凸显了尼泊尔年轻人根深蒂固的沮丧情绪以及他们对更公正和透明的政治体系的渴望。

---

## 59. Tau² 基准测试：提示词重写如何使 GPT-5-mini 性能提升 22%

**原文标题**: Tau² benchmark: How a prompt rewrite boosted GPT-5-mini by 22%

**原文链接**: [https://quesma.com/blog/tau2-benchmark-improving-results-smaller-models/](https://quesma.com/blog/tau2-benchmark-improving-results-smaller-models/)

本文详细介绍了如何通过简单的提示词重写，显著提升了GPT-5-mini模型在Tau²基准测试上的性能，该基准测试是一个评估LLM在智能体任务中表现的框架。该基准测试模拟了电信、零售和航空等领域的真实世界智能体交互。GPT-5-mini在电信领域（使用telecom_small任务集）的初始成功率仅为55%。

随后，作者利用Claude重写了用于生成GPT-5-mini提示词的AI智能体策略，重点关注简化、清晰和可操作的步骤。重写后的提示词强调结构化流程、二元决策和轻量级验证步骤，有效地将策略转化为清单。

结果非常显著。在Tau²基准测试上的成功率从55%跃升至67.5%（提高了22.73%），重试的有效性也得到了提高。此外，更新后的提示词使GPT-5-mini能够解决之前一直失败的任务，将“无法解决”的任务数量从6个减少到3个。

关键结论是，周到的提示词设计可以显著提高像GPT-5-mini这样较小型LLM的性能。简化语言、减少歧义并将推理分解为明确的步骤，使较小的模型能够更好地理解和执行任务。使用更强大的LLM（如Claude）来优化较小模型的提示词，是一种经济高效的增强其性能的方法，使其在效率和经济性至关重要时成为一种可行的替代方案。由于读者的兴趣，作者还分享了一个链接到pull request，展示了“之前和之后”的提示词。

---

## 60. 安全链防止开发者安装恶意软件。

**原文标题**: Safe Chain prevents developers from installing malware

**原文链接**: [https://www.npmjs.com/package/@aikidosec/safe-chain](https://www.npmjs.com/package/@aikidosec/safe-chain)

合气道安全链是一款免费工具，旨在防止开发者通过 npm、npx、yarn、pnpm 和 pnpx 在其工作站上安装恶意软件。它的工作原理是封装这些包管理器，并在允许安装包之前执行恶意软件检查。该工具通过为包管理器命令创建别名来与 shell 集成。

检测到恶意软件时，默认情况下，安全链会阻止安装。用户可以配置行为，在使用 `--safe-chain-malware-action=prompt` 标志时，改为在继续安装之前提示确认。

安装过程很简单，包括通过 npm 全局安装 `@aikidosec/safe-chain` 包，运行 `safe-chain setup` 命令以与 shell 集成，然后重新启动终端。卸载包括运行 `safe-chain teardown` 以删除 shell 别名并卸载该包。

安全链为 npm 10.4.0 及以上版本提供全面覆盖。 对于旧版本的 npm、npx、yarn、pnpm 和 pnpx，提供有限支持，仅扫描安装命令的参数。计划将来为这些包管理器和 bun 提供全面支持。它支持 Bash、Zsh、Fish、PowerShell 和 PowerShell Core。该工具还提供 CI/CD 集成，详细信息请参阅 Aikido 文档。

---

## 61. 华硕游戏本ACPI固件漏洞

**原文标题**: The Asus gaming laptop ACPI firmware bug

**原文链接**: [https://github.com/Zephkek/Asus-ROG-Aml-Deep-Dive](https://github.com/Zephkek/Asus-ROG-Aml-Deep-Dive)

本文详细介绍了一个困扰高端华硕游戏笔记本电脑的令人沮丧的ACPI固件错误，该错误会导致卡顿、音频爆音和输入延迟，即使在用户尝试了典型的软件修复之后。该问题源于嵌入在笔记本电脑BIOS中的低效或有缺陷的ACPI机器语言(AML)代码，该代码由Windows的ACPI.sys驱动程序解释。

LatencyMon将ACPI.sys识别为高中断延迟的罪魁祸首，尤其是在CPU 0上。高级ETW跟踪显示周期性延迟峰值，通常与“_GPE._L02”中断处理程序相关联，该处理程序每30-60秒触发一次，并触发电池/AC适配器状态检查和奇怪的GPU电源状态切换，即使系统配置为专用GPU模式。这会导致延迟峰值，在极少数情况下，由于固件和Windows之间存在冲突的电源状态命令，可能会导致系统崩溃。

对反编译ACPI表的分析揭示了_GPE._L02调用的有缺陷的“ECLV”方法。它在中断上下文中包含Sleep()命令（100ms和25ms），违反了内核编程的核心原则，并导致了显著的延迟。ECLV实现的的时间预算和强制事件触发也导致了持续的延迟。本质上，固件编写糟糕的ACPI代码是这些华硕笔记本电脑上出现性能问题的根本原因。

---

## 62. 理解 Deflate

**原文标题**: Understanding Deflate

**原文链接**: [https://jjrscott.com/to-deflate-or-not/](https://jjrscott.com/to-deflate-or-not/)

本文详细介绍了一次手动尝试理解Deflate压缩算法的过程，通过手工解压缩一个用GZIP压缩的简单字符串。作者首先使用GZIP压缩了字符串“TOBEORNOTTOBEORTOBEORNOT”，并检查了生成的十六进制表示。

然后，作者分解了GZIP封装，识别了魔数、压缩方法（Deflate）、标志、时间戳、额外标志、文件系统、压缩数据、CRC-32校验和以及未压缩数据大小。

文章的核心集中在使用“固定霍夫曼编码”解压缩Deflate数据。作者解释了LZ77令牌类型：字面量、复制命令（长度和距离）以及块结束标记。解码过程涉及解释位序列以识别符号代码和复制命令，并参考DEFLATE压缩数据格式规范。

作者成功地解码了压缩数据，识别了一系列字面字符和复制命令。文章提供了一个总结已解码令牌的列表，说明了如何使用字面字符和重复段（复制命令）重建原始字符串。

最后，作者得出结论，即使对于简单的字符串，Deflate也能显著减小数据大小（从24字节到约16字节），强调了位级编码的效率。然而，手动解码的过程被认为复杂且繁琐。

---

## 63. Gluon：一种基于与Triton相同编译器堆栈的GPU编程语言

**原文标题**: Gluon: a GPU programming language based on the same compiler stack as Triton

**原文链接**: [https://github.com/triton-lang/triton/blob/main/python/tutorials/gluon/01-intro.py](https://github.com/triton-lang/triton/blob/main/python/tutorials/gluon/01-intro.py)

提供的资讯宣布了一种新的GPU编程语言“Gluon”。关键在于Gluon的设计是基于与另一种GPU编程语言“Triton”相同的编译器堆栈。这表明Gluon旨在利用为Triton开发的现有基础设施和工具，从而可能简化开发并确保兼容性。

信息还强调了Triton本身的受欢迎程度和活跃度。GitHub上的Triton仓库`triton-lang/triton`是公开的，表明其为开源开发。 它拥有大量的关注者，有2.2k个fork和16.9k个star可以证明这一点。

因此，这篇文章本质上是在GPU编程领域介绍了一个新的参与者(Gluon)，将其定位为建立在备受推崇且积极开发的Triton项目基础上的扩展或演进。 构建在相同的编译器堆栈上可能会促进互操作性以及现有Triton代码和工具的重用。

---

## 64. 如何调试 Chez Scheme 程序 (2002)

**原文标题**: How to Debug Chez Scheme Programs (2002)

**原文链接**: [https://www.scheme.com/debug/debug.html](https://www.scheme.com/debug/debug.html)

如何调试 Chez Scheme 程序

本文《如何调试 Chez Scheme 程序》提供了一份实用的调试指南，主要面向初学者，但也适用于更复杂的场景和其他语言。它强调一种有条不紊的方法，首先要进行彻底的测试，并理解程序错误的本质，这些错误可能表现为错误信息、不正确的值、错误的输出或无法终止。

作者首先提倡基本的调试技巧：仔细分析错误信息（理解其结构和间接原因），仔细审视代码（机械地追踪执行），简化代码和输入以隔离问题，以及策略性地打印消息以跟踪程序流和变量值。追踪过程调用，使用`trace`、`trace-define`和`trace-lambda`，被呈现为一种自动打印函数调用消息的方式。

本文还讨论了调试加载错误，建议使用`pretty-print`作为带有`load`的求值过程，以查明语法错误，如不匹配的括号。或者，可以使用自定义求值过程来打印和求值表达式，从而在加载期间提供更多信息。

总的原则是在尝试修复之前了解错误的根本原因，避免随意更改，因为这可能会引入更多问题。该指南强调了在整个开发过程中进行持续测试的重要性，以便快速识别和解决错误，并强调系统化的调试方法对于创建可靠且可维护的代码至关重要。

---

## 65. UUIDv47：数据库存储UUIDv7，对外输出UUIDv4（SipHash掩码时间戳）

**原文标题**: UUIDv47: Store UUIDv7 in DB, emit UUIDv4 outside (SipHash-masked timestamp)

**原文链接**: [https://github.com/stateless-me/uuidv47](https://github.com/stateless-me/uuidv47)

UUIDv47 提供了一种在数据库中存储可排序的 UUIDv7 值的方法，同时向外部系统呈现一个与 UUIDv4 兼容的接口。这通过使用从 UUID 的随机位导出的键控 SipHash-2-4 流对 UUIDv7 时间戳字段进行 XOR 掩码来实现。这确保了确定性的、可逆的映射，从而允许 UUIDv7 和 v4 接口之间的精确往返。

主要优势包括：

*   **数据库友好的 UUIDv7 存储：** 由于时间顺序，提高了索引局部性和分页性能。
*   **外部中立性：** v4 接口隐藏了时间模式，并保持与期望 v4 UUID 的系统的兼容性。
*   **安全性：** 使用 SipHash-2-4，一种键控伪随机函数 (PRF)，以防止密钥恢复。

该过程涉及使用密钥进行编码（掩码时间戳并将版本设置为 4）和解码（取消掩码时间戳并将版本设置为 7）。 随机位保持不变。

该实现是仅包含头文件的 C 代码，没有依赖项，提供高性能，基准测试表明完整编码/解码往返操作大约需要 33 纳秒/次，SipHash 操作大约需要 14 纳秒/次。它还包括构建说明、测试套件和集成技巧。

---

## 66. 慢社交媒体

**原文标题**: Slow social media

**原文链接**: [https://herman.bearblog.dev/slow-social-media/](https://herman.bearblog.dev/slow-social-media/)

作者在他的文章《慢社交媒体》中，批判了当前社交媒体平台的状态，认为它们已经变成了以广告驱动的内容工厂，旨在让人上瘾和盈利，而不是真正的连接。他指出，像Instagram和Facebook这样的平台，已经从连接朋友转变为推送算法驱动的内容，以牺牲用户福祉为代价，追求用户参与度。

作者提出了一种替代方案，即“慢社交媒体”模式，该模式优先考虑真正的连接和深思熟虑的互动。这个平台将通过实施以下几个关键特性来避免当前平台的弊端：

*   **对称的“朋友”系统：** 用双方都同意连接的系统取代关注者。
*   **有限的连接：** 将连接人数限制在300左右，以阻止收集癖心态，并促进真正的互动。
*   **时间线排序：** 以时间顺序显示帖子，以提供自然的停止点，并防止无休止的滚动。
*   **分页：** 使用分页而不是无限滚动，为用户创建自然的休息。
*   **帖子限制：** 限制用户每天发布的帖子数量，以鼓励意图性。

该平台将类似于旧版的Instagram和Twitter的混合体，具有评论和回复功能，但没有像Reels、推荐系统或数据分析等鼓励参与度而不是连接的功能。作者承认，这样的平台在与已建立的内容工厂竞争时可能会面临挑战，但可以在小众社区中蓬勃发展。他还谈到了资金问题，并建议捐赠可能是一种可行的模式。虽然作者不打算自己构建这样的平台，但他表示希望看到它的存在，并愿意为任何有兴趣开发它的人提供咨询。

---

## 67. 展示HN: 47jobs – AI 代理的 Fiverr/Upwork

**原文标题**: Show HN: 47jobs – A Fiverr/Upwork for AI Agents

**原文链接**: [https://47jobs.xyz](https://47jobs.xyz)

无法访问文章链接。

---

## 68. YouTube addresses lower view counts which seem to be caused by ad blockers

**原文标题**: YouTube addresses lower view counts which seem to be caused by ad blockers

**原文链接**: [https://9to5google.com/2025/09/16/youtube-lower-view-counts-ad-blockers/](https://9to5google.com/2025/09/16/youtube-lower-view-counts-ad-blockers/)

This 9to5Google article from September 18, 2025, discusses reports of lower video view counts on YouTube, attributing the decline primarily to ad blockers. Many YouTubers reported significant drops in views starting in mid-August, leading to various theories. The most plausible explanation, though unconfirmed by YouTube, is that views from users with ad blockers enabled are not being counted accurately.

YouTuber Josh Strife Hayes noticed that computer views dropped by 50% while views on other devices remained stable, a pattern echoed by TechLinked. This aligns with YouTube's statement that ad blockers "can impact the accuracy of reported view counts," though they deny any systemic issues. While YouTube suggested other reasons like seasonal viewing habits, the ad blocker explanation seems more likely.

Adding weight to the theory, it's noted that the "EasyList" used by many ad blockers was updated on August 11 to block YouTube's view tracking. This means that ad blocker users can watch a YouTube video, but their view won't be counted towards the official view count.

The article references a previous incident where AdBlock caused slowdowns, further emphasizing the widespread use of ad blockers on the platform. This high usage of ad blockers might be the reason that YouTube has started being more forceful when dealing with the issue.

The top comment on the article suggests that intrusive advertising practices have fueled the need for ad blockers, ultimately criticizing YouTube's monopoly-like behavior.


---

## 69. Humans still better than AI for hotdog or not

**原文标题**: Humans still better than AI for hotdog or not

**原文链接**: [https://www.humanprotocol.org/blog/evaluating-google-cloud-vision-for-image-moderation-how-reliable-is-it](https://www.humanprotocol.org/blog/evaluating-google-cloud-vision-for-image-moderation-how-reliable-is-it)

生成摘要时出错

---

## 70. Just for fun: animating a mosaic of 90s GIFs

**原文标题**: Just for fun: animating a mosaic of 90s GIFs

**原文链接**: [https://alexplescan.com/posts/2025/09/15/gifs/](https://alexplescan.com/posts/2025/09/15/gifs/)

生成摘要时出错

---

## 71. Noise cancelling a fan

**原文标题**: Noise cancelling a fan

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/noise-cancelling-a-fan](https://chillphysicsenjoyer.substack.com/p/noise-cancelling-a-fan)

生成摘要时出错

---

## 72. DeepSeek writes less secure code for groups China disfavors?

**原文标题**: DeepSeek writes less secure code for groups China disfavors?

**原文链接**: [https://www.washingtonpost.com/technology/2025/09/16/deepseek-ai-security/](https://www.washingtonpost.com/technology/2025/09/16/deepseek-ai-security/)

生成摘要时出错

---

## 73. How to motivate yourself to do a thing you don't want to do

**原文标题**: How to motivate yourself to do a thing you don't want to do

**原文链接**: [https://ashleyjanssen.com/how-to-motivate-yourself-to-do-a-thing-you-dont-want-to-do/](https://ashleyjanssen.com/how-to-motivate-yourself-to-do-a-thing-you-dont-want-to-do/)

生成摘要时出错

---

## 74. I uncovered an ACPI bug in my Dell Inspiron 5567. It was plaguing me for 8 years

**原文标题**: I uncovered an ACPI bug in my Dell Inspiron 5567. It was plaguing me for 8 years

**原文链接**: [https://triangulatedexistence.mataroa.blog/blog/i-uncovered-an-acpi-bug-in-my-dell-inspiron-5667-it-was-plaguing-me-for-8-years/](https://triangulatedexistence.mataroa.blog/blog/i-uncovered-an-acpi-bug-in-my-dell-inspiron-5667-it-was-plaguing-me-for-8-years/)

生成摘要时出错

---

## 75. Condor Technology to Fly "Cuzco" RISC-V CPU into the Datacenter

**原文标题**: Condor Technology to Fly "Cuzco" RISC-V CPU into the Datacenter

**原文链接**: [https://www.nextplatform.com/2025/09/15/condor-technology-to-fly-cuzco-risc-v-cpu-into-the-datacenter/](https://www.nextplatform.com/2025/09/15/condor-technology-to-fly-cuzco-risc-v-cpu-into-the-datacenter/)

生成摘要时出错

---

## 76. What Can We Do with Corner-Shape CSS?

**原文标题**: What Can We Do with Corner-Shape CSS?

**原文链接**: [https://css-tricks.com/what-can-we-actually-do-with-corner-shape/](https://css-tricks.com/what-can-we-actually-do-with-corner-shape/)

生成摘要时出错

---

## 77. Notion API importer, with Databases to Bases conversion bounty

**原文标题**: Notion API importer, with Databases to Bases conversion bounty

**原文链接**: [https://github.com/obsidianmd/obsidian-importer/issues/421](https://github.com/obsidianmd/obsidian-importer/issues/421)

生成摘要时出错

---

## 78. Samsung brings ads to US fridges

**原文标题**: Samsung brings ads to US fridges

**原文链接**: [https://www.theverge.com/news/780757/samsung-brings-ads-to-us-fridges](https://www.theverge.com/news/780757/samsung-brings-ads-to-us-fridges)

生成摘要时出错

---

## 79. PureVPN IPv6 Leak

**原文标题**: PureVPN IPv6 Leak

**原文链接**: [https://anagogistis.com/posts/purevpn-ipv6-leak/](https://anagogistis.com/posts/purevpn-ipv6-leak/)

生成摘要时出错

---

## 80. GNU Midnight Commander

**原文标题**: GNU Midnight Commander

**原文链接**: [https://midnight-commander.org/](https://midnight-commander.org/)

生成摘要时出错

---

## 81. Depression reduces capacity to learn to actively avoid aversive events

**原文标题**: Depression reduces capacity to learn to actively avoid aversive events

**原文链接**: [https://www.eneuro.org/content/12/9/ENEURO.0034-25.2025](https://www.eneuro.org/content/12/9/ENEURO.0034-25.2025)

生成摘要时出错

---

## 82. No CSS, No JavaScript. Longevity on the Web

**原文标题**: No CSS, No JavaScript. Longevity on the Web

**原文链接**: [https://jch.github.io/posts/2025-09-18-no-css-no-js.html](https://jch.github.io/posts/2025-09-18-no-css-no-js.html)

生成摘要时出错

---

## 83. Shai-Hulud malware attack: Tinycolor and over 40 NPM packages compromised

**原文标题**: Shai-Hulud malware attack: Tinycolor and over 40 NPM packages compromised

**原文链接**: [https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages](https://socket.dev/blog/ongoing-supply-chain-attack-targets-crowdstrike-npm-packages)

生成摘要时出错

---

## 84. Stategraph: Terraform state as a distributed systems problem

**原文标题**: Stategraph: Terraform state as a distributed systems problem

**原文链接**: [https://stategraph.dev/blog/why-stategraph/](https://stategraph.dev/blog/why-stategraph/)

生成摘要时出错

---

## 85. Infinite Mac: Resource Fork Roundtripping

**原文标题**: Infinite Mac: Resource Fork Roundtripping

**原文链接**: [https://blog.persistent.info/2025/09/infinite-mac-resource-forks.html](https://blog.persistent.info/2025/09/infinite-mac-resource-forks.html)

生成摘要时出错

---

## 86. John Grisham Still Wonders: Will Texas Kill Robert Roberson?

**原文标题**: John Grisham Still Wonders: Will Texas Kill Robert Roberson?

**原文链接**: [https://www.dmagazine.com/frontburner/2025/09/author-john-grisham-still-wonders-will-texas-kill-robert-roberson/](https://www.dmagazine.com/frontburner/2025/09/author-john-grisham-still-wonders-will-texas-kill-robert-roberson/)

生成摘要时出错

---

## 87. Top UN legal investigators conclude Israel is guilty of genocide in Gaza

**原文标题**: Top UN legal investigators conclude Israel is guilty of genocide in Gaza

**原文链接**: [https://www.middleeasteye.net/news/un-concludes-israel-guilty-genocide-gaza](https://www.middleeasteye.net/news/un-concludes-israel-guilty-genocide-gaza)

生成摘要时出错

---

## 88. Grade 2 Braille

**原文标题**: Grade 2 Braille

**原文链接**: [https://en.wikipedia.org/wiki/English_Braille](https://en.wikipedia.org/wiki/English_Braille)

生成摘要时出错

---

## 89. European ant is the first known animal to clone members of another species

**原文标题**: European ant is the first known animal to clone members of another species

**原文链接**: [https://www.livescience.com/animals/ants/almost-like-science-fiction-european-ant-is-the-first-known-animal-to-clone-members-of-another-species](https://www.livescience.com/animals/ants/almost-like-science-fiction-european-ant-is-the-first-known-animal-to-clone-members-of-another-species)

生成摘要时出错

---

## 90. Saw-Tooth Roof

**原文标题**: Saw-Tooth Roof

**原文链接**: [https://en.wikipedia.org/wiki/Saw-tooth_roof](https://en.wikipedia.org/wiki/Saw-tooth_roof)

生成摘要时出错

---

## 91. Anthropic irks White House with limits on models’ use

**原文标题**: Anthropic irks White House with limits on models’ use

**原文链接**: [https://www.semafor.com/article/09/17/2025/anthropic-irks-white-house-with-limits-on-models-uswhite-house-with-limits-on-models-use](https://www.semafor.com/article/09/17/2025/anthropic-irks-white-house-with-limits-on-models-uswhite-house-with-limits-on-models-use)

生成摘要时出错

---

## 92. Procedural Island Generation (III)

**原文标题**: Procedural Island Generation (III)

**原文链接**: [https://brashandplucky.com/2025/09/17/procedural-island-generation-iii.html](https://brashandplucky.com/2025/09/17/procedural-island-generation-iii.html)

生成摘要时出错

---

## 93. Django 6.0 alpha 1 released

**原文标题**: Django 6.0 alpha 1 released

**原文链接**: [https://www.djangoproject.com/weblog/2025/sep/17/django-60-alpha-released/](https://www.djangoproject.com/weblog/2025/sep/17/django-60-alpha-released/)

生成摘要时出错

---

## 94. Trump's Golden Dome will cost 10 to 100 times more than the Manhattan Project

**原文标题**: Trump's Golden Dome will cost 10 to 100 times more than the Manhattan Project

**原文链接**: [https://arstechnica.com/space/2025/09/trumps-golden-dome-will-cost-10-to-100-times-more-than-the-manhattan-project/](https://arstechnica.com/space/2025/09/trumps-golden-dome-will-cost-10-to-100-times-more-than-the-manhattan-project/)

生成摘要时出错

---

## 95. I got the highest score on ARC-AGI again swapping Python for English

**原文标题**: I got the highest score on ARC-AGI again swapping Python for English

**原文链接**: [https://jeremyberman.substack.com/p/how-i-got-the-highest-score-on-arc-agi-again](https://jeremyberman.substack.com/p/how-i-got-the-highest-score-on-arc-agi-again)

生成摘要时出错

---

## 96. Alibaba's new AI chip: Key specifications comparable to H20

**原文标题**: Alibaba's new AI chip: Key specifications comparable to H20

**原文链接**: [https://news.futunn.com/en/post/62202518/alibaba-s-new-ai-chip-unveiled-key-specifications-comparable-to](https://news.futunn.com/en/post/62202518/alibaba-s-new-ai-chip-unveiled-key-specifications-comparable-to)

生成摘要时出错

---

## 97. Secrets of DeepSeek AI model revealed in landmark paper

**原文标题**: Secrets of DeepSeek AI model revealed in landmark paper

**原文链接**: [https://www.nature.com/articles/d41586-025-03015-6](https://www.nature.com/articles/d41586-025-03015-6)

生成摘要时出错

---

## 98. Murex – An intuitive and content aware shell for a modern command line

**原文标题**: Murex – An intuitive and content aware shell for a modern command line

**原文链接**: [https://murex.rocks/](https://murex.rocks/)

生成摘要时出错

---

## 99. "Your" vs. "My" in user interfaces

**原文标题**: "Your" vs. "My" in user interfaces

**原文链接**: [https://adamsilver.io/blog/your-vs-my-in-user-interfaces/](https://adamsilver.io/blog/your-vs-my-in-user-interfaces/)

生成摘要时出错

---

## 100. AMD Open Source Driver for Vulkan project is discontinued

**原文标题**: AMD Open Source Driver for Vulkan project is discontinued

**原文链接**: [https://github.com/GPUOpen-Drivers/AMDVLK/discussions/416](https://github.com/GPUOpen-Drivers/AMDVLK/discussions/416)

生成摘要时出错

---

