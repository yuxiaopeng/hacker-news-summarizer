# Hacker News 热门文章摘要 (2026-03-22)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 版本控制的未来

**原文标题**: The Future of Version Control

**原文链接**: [https://bramcohen.com/p/manyana](https://bramcohen.com/p/manyana)

Bram Cohen 推出了 **Manyana**，这是一个概念验证项目，提出了一种基于**无冲突复制数据类型 (CRDTs)** 的版本控制新愿景。与 Git 等依赖三路合并（可能失败或产生晦涩冲突标记）的传统系统不同，Manyana 在设计上确保合并总能成功。

核心特性与见解包括：

*   **结构化冲突展示：** 由于 CRDT 确保最终一致性，“冲突”被视为具有参考价值的元数据，而非阻塞性错误。Manyana 提供了结构化的清晰度，能够精确显示各方的具体操作（例如，“左侧删除了此函数，右侧在其中添加了一行”），而不是呈现两个缺乏上下文的代码块。
*   **“编织 (Weave)”结构：** 系统将文件视为一种“编织”——一个包含有史以来编写的每一行及其元数据的单一结构。这消除了在有向无环图 (DAG) 中寻找共同祖先的必要，因为历史记录已嵌入在文件的状态之中。
*   **非破坏性变基：** Manyana 允许进行变基（在新的基点上重新回放提交）而不破坏原始历史。通过使用“主要祖先”注解，它避免了传统版本控制系统在频繁变基时遇到的拓扑问题。

目前，Manyana 仅是一个 470 行 Python 代码的演示程序，针对单个文件操作，而非全规模的版本控制工具。然而，它作为一个公有领域的蓝图和“连贯愿景”，预示着未来的版本控制将更加稳健、信息更丰富，且不易陷入现代分支与合并的“噩梦”。

---

## 2. Flash-MoE：在笔记本电脑上运行 397B 参数模型

**原文标题**: Flash-MoE: Running a 397B Parameter Model on a Laptop

**原文链接**: [https://github.com/danveloper/flash-moe](https://github.com/danveloper/flash-moe)

**Flash-MoE** 是一款采用纯 C 和 Metal 编写的高性能推理引擎，旨在消费级硬件上运行超大规模混合专家（MoE）模型。具体而言，它能让 **MacBook Pro（M3 Max，48GB 内存）** 以超过 **4.4 token/秒** 的速度运行拥有 3970 亿参数的 **Qwen3.5-397B** 模型。

该项目的核心突破在于通过直接从 **SSD** 流式传输专家权重，使内存受限的机器能够处理高达 **209GB 的模型**。其关键技术特性包括：

*   **SSD 专家流式传输：** 受苹果“LLM in a Flash”启发，该引擎通过并行 `pread()` 调用，按需仅加载每层所需的 $K=4$ 个激活专家（每个约 6.75MB）。
*   **“信任操作系统”哲学：** 开发人员没有实现自定义的 LRU 缓存或复杂的压缩算法（如 LZ4），而是依赖 macOS 原生的页面缓存（page cache），实现了 71% 的命中率，性能优于自定义内存管理。
*   **硬件优化：** 定制的 **FMA 优化反量化内核** 通过重新排列数学运算来利用 GPU 的融合乘加单元，带来了 12% 的性能提升。此外，它还使用 **Accelerate BLAS** 处理线性注意力，将 CPU 端的计算速度提高了 64%。
*   **策略性流水线：** 由于统一内存架构中 SSD I/O 和 GPU 计算会竞争带宽，引擎采用串行流水线（GPU → SSD → GPU）以避免延迟波动。

该引擎支持生产级的 4-bit 量化，保留了完整的工具调用（tool-calling）和 JSON 处理能力。虽然 2-bit 量化可达到 7 token/秒，但因输出质量下降而在生产环境中被弃用。通过将非专家权重和缓冲区占用的内存控制在 6GB 以内，系统确保了零 OOM（内存溢出）风险，并将剩余内存交给操作系统用于管理专家数据。

---

## 3. Project Nomad – Knowledge That Never Goes Offline

**原文标题**: Project Nomad – Knowledge That Never Goes Offline

**原文链接**: [https://www.projectnomad.us](https://www.projectnomad.us)

生成摘要时出错

---

## 4. 关于代码已死的报道言过其实。

**原文标题**: Reports of code's death are greatly exaggerated

**原文链接**: [https://stevekrouse.com/precision](https://stevekrouse.com/precision)

在《代码之死，言过其实》一文中，Steve Krouse 指出，尽管 AI 生成软件的趋势日益增强，但编程技艺和对精确代码的需求依然至关重要。他质疑了当下流行的观点，即“氛围编程”（vibe coding）——即通过自然语言提示 AI 来创建软件——将取代传统编程。

Krouse 揭示了一个根本性的矛盾：英语虽然直观，但对于复杂系统而言过于模糊。他引用了开发者在使用“氛围编程”时的经历，即由于缺乏对底层复杂性的深刻理解，这些应用在扩展规模时往往会走向失败。自然语言无法取代定义明确的规范所具备的精确性；正如伯特兰·罗素所言，一切事物在被尝试精确化之前都是模糊的。

Krouse 论点的核心在于**抽象**。由于人类的认知能力有限，我们利用抽象将复杂的思想压缩为易于管理且精确的语义层次。Krouse 认为，AI 和未来通用人工智能（AGI）的真正价值不在于制造大量的“垃圾代码”或低质量代码，而在于帮助我们掌控复杂性。AI 应当被用于发现更好的抽象模式——如 React 或 Tailwind——从而使人类能够构建更稳健、更优雅的系统。

Krouse 以写作类比，指出没有人会认为“氛围写作”能取代小说家；同样，代码依然是“核心且重要的载体”，是一种智力层面的诗歌。他总结道，编程并未走向终结，而是正步入一个新纪元。正如印刷机的出现并未扼杀叙事艺术，AI 将成为编程的福音，助力开发者达到更高层次的形式化推理，并解决世间最难的抽象问题。

---

## 5. 使用现代 RTL 工具构建 FPGA 版 3dfx Voodoo

**原文标题**: Building an FPGA 3dfx Voodoo with Modern RTL Tools

**原文链接**: [https://noquiche.fyi/voodoo](https://noquiche.fyi/voodoo)

本文详细介绍了如何使用 SpinalHDL 和调试工具 conetrace 等现代 RTL 工具对 3dfx Voodoo 1 进行 FPGA 重新实现。该项目指出，尽管 Voodoo 是一款老旧芯片，但其固定功能架构（将 Gouraud 着色、Mipmapping 和雾化等复杂行为硬化）带来了极高的设计复杂度。

核心挑战之一是 Voodoo 的寄存器语义。由于芯片采用深度流水线设计，寄存器写入充当了“时序契约”。为防止新设置干扰正在进行的任务，作者将寄存器分为四种类型：FIFO、FIFO+Stall（暂停）、Direct（直接）和 Float（浮动）。通过利用 SpinalHDL 的 RegIf 抽象，作者将这些架构规则直接编码到寄存器映射中。这使得硬件能够自动处理流水线暂停或写入排队等复杂行为，而无需依赖分散的手动逻辑。

作者还强调了从传统波形查看到“网表感知调试”的转变。此前，一个涉及半透明像素消失的顽固 Bug 最初被认为是内存排序冒险。然而，通过使用 conetrace 在流水线各阶段追踪像素，作者发现该“冒险”实际上是三个细微硬件精度不匹配的累积结果：W 值的早期量化、错误的 LOD 舍入以及混合中的抖动减法错误。

项目总结认为，现代 RTL 工具使得单人开发者也能驾驭复杂的固定功能设计。通过在代码中直接表达架构意图，并提供高抽象层级的执行查询工具，现代工作流程将 Voodoo 复杂的硅片行为从文档层面的挑战转变为可管理且可执行的现实。

---

## 6. 我为什么喜欢 NixOS

**原文标题**: Why I love NixOS

**原文链接**: [https://www.birkey.co/2026-03-22-why-i-love-nixos.html](https://www.birkey.co/2026-03-22-why-i-love-nixos.html)

在本文中，作者解释了他们对 NixOS 的青睐源于 Nix 包管理器确定性、函数式和可复现的特性。与会随着时间推移积累“状态堆积”并变得不可预测的传统操作系统不同，NixOS 通过声明式配置进行定义。这使得用户能够在一个地方管理从硬件设置到桌面扩展的所有内容，确保系统可以充满信心地被重建、修改或回滚。

作者强调了几个关键的实际优势：
*   **安全实验：** `nix shell` 和 `nix develop` 等工具允许用户在隔离环境中尝试新软件或编译器，而不会污染基础系统或更改 `PATH` 变量。
*   **稳定性：** 凭借可预测的六个月发布周期和无痛升级，NixOS 让硬件表现得“平淡”且可靠。
*   **跨平台一致性：** Nix 包管理器可同时在 Linux 和 macOS 上运行，在不同机器上提供一致的开发体验。
*   **LLM 集成：** 在 AI 编程智能体时代，Nix 具有独特的价值。它允许智能体为特定任务拉取特定的工具链（如 Rust 或 Python 版本），而无需使用会留下残留文件的 "curl | sh" 脚本。这些实验随后可以记录在 `flake.nix` 中，以实现永久可复现。
*   **部署：** 相比传统的 Docker 方法，Nix 提供了一种更具确定性的部署方案，允许通过 `dockerTools` 创建分层的极简镜像。

最终，作者热爱 NixOS 是因为它代表了软件系统应有的样子：一个连贯、可逆且稳定的基础，能够让用户专注于实际工作而不受干扰。

---

## 7. Windows原生应用开发现状一团糟

**原文标题**: Windows native app development is a mess

**原文链接**: [https://domenic.me/windows-native-dev/](https://domenic.me/windows-native-dev/)

The author, a veteran Windows developer, argues that native Windows application development has become a fragmented "mess," characterized by inconsistent frameworks and significant technical gaps. While attempting to build a simple monitor-utility program using the latest **Windows App SDK (WinUI 3)**, the author found the experience so frustrating that it explains the industry-wide shift toward Electron and web technologies.

Key issues highlighted include:

*   **Framework Fragmentation:** Microsoft has cycled through numerous UI stacks (Win32, MFC, WinForms, WPF, UWP, and WinUI 3), yet each new iteration lacks features present in its predecessors. Basic tasks like creating tray icons, global shortcuts, or non-activating windows still require dropping down to legacy Win32 C APIs via complex "interop goop."
*   **Deployment and Distribution Hurdles:** Modern .NET versions are not pre-installed on Windows 11, forcing developers to choose between prompting users for downloads or distributing large, self-contained AOT binaries. Furthermore, the high cost of code-signing certificates and the difficult "sideloading" experience for unsigned apps create significant barriers for independent creators.
*   **Stagnant Tooling:** The author notes that C# still lacks idiomatic ways to handle Win32 architectural patterns. Additionally, the excessive boilerplate code required for XAML data binding has remained largely unchanged for twenty years.
*   **Lack of First-Party Commitment:** The author suggests native development is no longer a priority for Microsoft, noting that even many first-party apps (like VS Code, Outlook, and the Start menu) are now built using web technologies. 

Ultimately, the article concludes that the neglect of first-party tools has forced the developer community to seek stability in third-party alternatives like Avalonia and Uno Platform.

---

## 8. 绘制系统架构图时应避免的更多常见错误

**原文标题**: More common mistakes to avoid when creating system architecture diagrams

**原文链接**: [https://www.ilograph.com/blog/posts/more-common-diagram-mistakes/](https://www.ilograph.com/blog/posts/more-common-diagram-mistakes/)

在《架构图的另外 7 个常见错误》一文中，Billy Pilger 指出了阻碍技术文档清晰度和有效性的关键陷阱。为了改善沟通，他建议避免以下错误：

1. **省略资源名称**：仅按“类型”（如“数据库”）标记资源会产生歧义。必须使用具体名称（如“订单表”）来明确资源的特定角色。
2. **未连接的资源**：图表中的每个元素都应与其他元素有可见的关联。孤立的图标会让查看者对其在系统中的功能感到困惑。
3. **“全能”总图**：试图在单一视图中展示整个系统的复杂性会导致信息过载。相反，绘图者应将图表拆分为多个“视角”，例如分别展示运行时依赖和部署情况的独立视图。
4. **传送带综合症**：将复杂的交互过度简化为单向线性流会误导查看者。Pilger 建议使用时序图来准确描述往返通信。
5. **无意义的动画**：通常用于市场营销的华丽动态箭头不具技术价值，反而会分散对实际架构的注意力。
6. **扇形陷阱**：当所有通信都汇集到单个中间枢纽（如消息代理）时，具体的关联信息就会丢失。可以通过详细说明内部子资源（如特定主题或队列）来解决此问题。
7. **过度依赖 AI**：虽然 AI 可以辅助白板绘图，但目前它还缺乏直接从源代码创建高保真图表所需的战略判断和训练数据，往往会导致“幻觉”或模糊的输出。

最后，Pilger 强调，高效的绘图本质上仍是一项以人为本的任务，需要通过战略决策来决定内容的取舍，从而讲述一个连贯的故事。

---

## 9. Brute-forcing my algorithmic ignorance with an LLM in 7 days

**原文标题**: Brute-forcing my algorithmic ignorance with an LLM in 7 days

**原文链接**: [http://blog.dominikrudnik.pl/my-google-recruitment-journey-part-1](http://blog.dominikrudnik.pl/my-google-recruitment-journey-part-1)

生成摘要时出错

---

## 10. MAUI Is Coming to Linux

**原文标题**: MAUI Is Coming to Linux

**原文链接**: [https://avaloniaui.net/blog/maui-avalonia-preview-1](https://avaloniaui.net/blog/maui-avalonia-preview-1)

生成摘要时出错

---

## 11. A review of dice that came with the white castle

**原文标题**: A review of dice that came with the white castle

**原文链接**: [https://boardgamegeek.com/thread/3533812/a-review-of-dice-that-came-with-the-white-castle](https://boardgamegeek.com/thread/3533812/a-review-of-dice-that-came-with-the-white-castle)

生成摘要时出错

---

## 12. A case against currying

**原文标题**: A case against currying

**原文链接**: [https://emi-h.com/articles/a-case-against-currying.html](https://emi-h.com/articles/a-case-against-currying.html)

生成摘要时出错

---

## 13. 25 Years of Eggs

**原文标题**: 25 Years of Eggs

**原文链接**: [https://www.john-rush.com/posts/eggs-25-years-20260219.html](https://www.john-rush.com/posts/eggs-25-years-20260219.html)

生成摘要时出错

---

## 14. Cloudflare flags archive.today as "C&C/Botnet"; no longer resolves via 1.1.1.2

**原文标题**: Cloudflare flags archive.today as "C&C/Botnet"; no longer resolves via 1.1.1.2

**原文链接**: [https://radar.cloudflare.com/domains/domain/archive.today](https://radar.cloudflare.com/domains/domain/archive.today)

生成摘要时出错

---

## 15. Zero ZGC4: A Better Graphing Calculator for School and Beyond

**原文标题**: Zero ZGC4: A Better Graphing Calculator for School and Beyond

**原文链接**: [https://www.zerocalculators.com/features](https://www.zerocalculators.com/features)

生成摘要时出错

---

## 16. iBook Clamshell

**原文标题**: iBook Clamshell

**原文链接**: [https://www.ibook-clamshell.com/index.php/en/](https://www.ibook-clamshell.com/index.php/en/)

生成摘要时出错

---

## 17. The IBM scientist who rewrote the rules of information just won a Turing Award

**原文标题**: The IBM scientist who rewrote the rules of information just won a Turing Award

**原文链接**: [https://www.ibm.com/think/news/ibm-scientist-charles-bennett-turing-award](https://www.ibm.com/think/news/ibm-scientist-charles-bennett-turing-award)

生成摘要时出错

---

## 18. Why Lab Coats Turned White

**原文标题**: Why Lab Coats Turned White

**原文链接**: [https://www.asimov.press/p/lab-coat](https://www.asimov.press/p/lab-coat)

生成摘要时出错

---

## 19. My first patch to the Linux kernel

**原文标题**: My first patch to the Linux kernel

**原文链接**: [https://pooladkhay.com/posts/first-kernel-patch/](https://pooladkhay.com/posts/first-kernel-patch/)

生成摘要时出错

---

## 20. Node.js worker threads are problematic, but they work great for us

**原文标题**: Node.js worker threads are problematic, but they work great for us

**原文链接**: [https://www.inngest.com/blog/node-worker-threads](https://www.inngest.com/blog/node-worker-threads)

生成摘要时出错

---

## 21. Tinybox – A powerful computer for deep learning

**原文标题**: Tinybox – A powerful computer for deep learning

**原文链接**: [https://tinygrad.org/#tinybox](https://tinygrad.org/#tinybox)

生成摘要时出错

---

## 22. I hate: Programming Wayland applications

**原文标题**: I hate: Programming Wayland applications

**原文链接**: [https://www.p4m.dev/posts/29/index.html](https://www.p4m.dev/posts/29/index.html)

生成摘要时出错

---

## 23. The three pillars of JavaScript bloat

**原文标题**: The three pillars of JavaScript bloat

**原文链接**: [https://43081j.com/2026/03/three-pillars-of-javascript-bloat](https://43081j.com/2026/03/three-pillars-of-javascript-bloat)

生成摘要时出错

---

## 24. Monuses and Heaps

**原文标题**: Monuses and Heaps

**原文链接**: [https://doisinkidney.com/posts/2026-03-03-monus-heaps.html](https://doisinkidney.com/posts/2026-03-03-monus-heaps.html)

生成摘要时出错

---

## 25. A Fuzzer for the Toy Optimizer

**原文标题**: A Fuzzer for the Toy Optimizer

**原文链接**: [https://bernsteinbear.com/blog/toy-fuzzer/](https://bernsteinbear.com/blog/toy-fuzzer/)

生成摘要时出错

---

## 26. Professional video editing, right in the browser with WebGPU and WASM

**原文标题**: Professional video editing, right in the browser with WebGPU and WASM

**原文链接**: [https://tooscut.app/](https://tooscut.app/)

生成摘要时出错

---

## 27. Bored of eating your own dogfood? Try smelling your own farts

**原文标题**: Bored of eating your own dogfood? Try smelling your own farts

**原文链接**: [https://shkspr.mobi/blog/2026/03/bored-of-eating-your-own-dogfood-try-smelling-your-own-farts/](https://shkspr.mobi/blog/2026/03/bored-of-eating-your-own-dogfood-try-smelling-your-own-farts/)

生成摘要时出错

---

## 28. Chest Fridge (2009)

**原文标题**: Chest Fridge (2009)

**原文链接**: [https://mtbest.net/chest-fridge/](https://mtbest.net/chest-fridge/)

生成摘要时出错

---

## 29. HopTab – Open source macOS app switcher and tiler that replaces Cmd+Tab

**原文标题**: HopTab – Open source macOS app switcher and tiler that replaces Cmd+Tab

**原文链接**: [https://www.royalbhati.com/hoptab](https://www.royalbhati.com/hoptab)

生成摘要时出错

---

## 30. How We Synchronized Editing for Rec Room's Multiplayer Scripting System

**原文标题**: How We Synchronized Editing for Rec Room's Multiplayer Scripting System

**原文链接**: [https://www.tyleo.com/blog/how-we-synchronized-editing-for-rec-rooms-multiplayer-scripting-system](https://www.tyleo.com/blog/how-we-synchronized-editing-for-rec-rooms-multiplayer-scripting-system)

生成摘要时出错

---

## 31. Floci – A free, open-source local AWS emulator

**原文标题**: Floci – A free, open-source local AWS emulator

**原文链接**: [https://github.com/hectorvent/floci](https://github.com/hectorvent/floci)

生成摘要时出错

---

## 32. Hormuz Minesweeper – Are you tired of winning?

**原文标题**: Hormuz Minesweeper – Are you tired of winning?

**原文链接**: [https://hormuz.pythonic.ninja/](https://hormuz.pythonic.ninja/)

生成摘要时出错

---

## 33. Electronics for Kids, 2nd Edition

**原文标题**: Electronics for Kids, 2nd Edition

**原文链接**: [https://nostarch.com/electronics-for-kids-2e](https://nostarch.com/electronics-for-kids-2e)

生成摘要时出错

---

## 34. Turns out your coffee addiction may be doing your brain a favor

**原文标题**: Turns out your coffee addiction may be doing your brain a favor

**原文链接**: [https://www.theregister.com/2026/03/21/turns_out_your_coffee_addiction/](https://www.theregister.com/2026/03/21/turns_out_your_coffee_addiction/)

生成摘要时出错

---

## 35. Boomloom: Think with your hands

**原文标题**: Boomloom: Think with your hands

**原文链接**: [https://www.theboomloom.com](https://www.theboomloom.com)

生成摘要时出错

---

## 36. Bayesian statistics for confused data scientists

**原文标题**: Bayesian statistics for confused data scientists

**原文链接**: [https://nchagnet.pages.dev/blog/bayesian-statistics-for-confused-data-scientists/](https://nchagnet.pages.dev/blog/bayesian-statistics-for-confused-data-scientists/)

生成摘要时出错

---

## 37. 'Miracle': Europe reconnects with lost spacecraft

**原文标题**: 'Miracle': Europe reconnects with lost spacecraft

**原文链接**: [https://phys.org/news/2026-03-miracle-europe-reconnects-lost-spacecraft.html](https://phys.org/news/2026-03-miracle-europe-reconnects-lost-spacecraft.html)

生成摘要时出错

---

## 38. Hide macOS Tahoe's Menu Icons

**原文标题**: Hide macOS Tahoe's Menu Icons

**原文链接**: [https://512pixels.net/2026/03/hide-macos-tahoes-menu-icons-with-this-one-simple-trick/](https://512pixels.net/2026/03/hide-macos-tahoes-menu-icons-with-this-one-simple-trick/)

生成摘要时出错

---

## 39. Operation Epic Fury Explained: Riches and Domination Drive This War

**原文标题**: Operation Epic Fury Explained: Riches and Domination Drive This War

**原文链接**: [https://truthout.org/articles/operation-epic-fury-explained-riches-and-domination-drive-this-war/](https://truthout.org/articles/operation-epic-fury-explained-riches-and-domination-drive-this-war/)

生成摘要时出错

---

## 40. Apple's intentional crippling of Mobile Safari

**原文标题**: Apple's intentional crippling of Mobile Safari

**原文链接**: [https://pwa.gripe/](https://pwa.gripe/)

生成摘要时出错

---

## 41. Grafeo – A fast, lean, embeddable graph database built in Rust

**原文标题**: Grafeo – A fast, lean, embeddable graph database built in Rust

**原文链接**: [https://grafeo.dev/](https://grafeo.dev/)

生成摘要时出错

---

## 42. It's Their Mona Lisa

**原文标题**: It's Their Mona Lisa

**原文链接**: [https://ironicsans.ghost.io/its-t-mona-lisa/](https://ironicsans.ghost.io/its-t-mona-lisa/)

生成摘要时出错

---

## 43. 不要将未成年人保护变为互联网访问控制。

**原文标题**: Do Not Turn Child Protection into Internet Access Control

**原文链接**: [https://news.dyne.org/child-protection-is-not-access-control/](https://news.dyne.org/child-protection-is-not-access-control/)

生成摘要时出错

---

## 44. Thinking Fast, Slow, and Artificial: How AI Is Reshaping Human Reasoning

**原文标题**: Thinking Fast, Slow, and Artificial: How AI Is Reshaping Human Reasoning

**原文链接**: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6097646](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6097646)

生成摘要时出错

---

## 45. Some things just take time

**原文标题**: Some things just take time

**原文链接**: [https://lucumr.pocoo.org/2026/3/20/some-things-just-take-time/](https://lucumr.pocoo.org/2026/3/20/some-things-just-take-time/)

生成摘要时出错

---

## 46. Sashiko: An agentic Linux kernel code review system

**原文标题**: Sashiko: An agentic Linux kernel code review system

**原文链接**: [https://sashiko.dev/](https://sashiko.dev/)

生成摘要时出错

---

## 47. Show HN: Termcraft – Terminal-first 2D sandbox survival in Rust

**原文标题**: Show HN: Termcraft – Terminal-first 2D sandbox survival in Rust

**原文链接**: [https://github.com/pagel-s/termcraft](https://github.com/pagel-s/termcraft)

生成摘要时出错

---

## 48. Show HN: Oku – One tab to filter out noise from feeds and content sources

**原文标题**: Show HN: Oku – One tab to filter out noise from feeds and content sources

**原文链接**: [https://oku.io](https://oku.io)

生成摘要时出错

---

## 49. Common Lisp Development Tooling

**原文标题**: Common Lisp Development Tooling

**原文链接**: [https://www.creativetension.co/posts/common-lisp-development-tooling](https://www.creativetension.co/posts/common-lisp-development-tooling)

生成摘要时出错

---

## 50. How Invisalign became the biggest user of 3D printers

**原文标题**: How Invisalign became the biggest user of 3D printers

**原文链接**: [https://www.wired.com/story/how-invisalign-became-the-worlds-biggest-3d-printing-company/](https://www.wired.com/story/how-invisalign-became-the-worlds-biggest-3d-printing-company/)

生成摘要时出错

---

## 51. GrapheneOS refuses to comply with new age verification laws for operating system

**原文标题**: GrapheneOS refuses to comply with new age verification laws for operating system

**原文链接**: [https://www.tomshardware.com/software/operating-systems/grapheneos-refuses-to-comply-with-age-verification-laws](https://www.tomshardware.com/software/operating-systems/grapheneos-refuses-to-comply-with-age-verification-laws)

生成摘要时出错

---

## 52. Walmart fires OpenAI in playbook-changing move

**原文标题**: Walmart fires OpenAI in playbook-changing move

**原文链接**: [https://www.thestreet.com/retail/walmart-fires-openai-in-playbook-changing-move](https://www.thestreet.com/retail/walmart-fires-openai-in-playbook-changing-move)

生成摘要时出错

---

## 53. Trivy ecosystem supply chain briefly compromised

**原文标题**: Trivy ecosystem supply chain briefly compromised

**原文链接**: [https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23](https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23)

生成摘要时出错

---

## 54. Linking Smaller Haskell Binaries (2023)

**原文标题**: Linking Smaller Haskell Binaries (2023)

**原文链接**: [https://brandon.si/code/linking-smaller-haskell-binaries/](https://brandon.si/code/linking-smaller-haskell-binaries/)

生成摘要时出错

---

## 55. The paddle wheel aircraft carriers of Lake Michigan

**原文标题**: The paddle wheel aircraft carriers of Lake Michigan

**原文链接**: [https://signoregalilei.com/2026/03/08/the-paddle-wheel-aircraft-carriers-of-lake-michigan/](https://signoregalilei.com/2026/03/08/the-paddle-wheel-aircraft-carriers-of-lake-michigan/)

生成摘要时出错

---

## 56. Alpha Micro AM-1000E and AM-1200

**原文标题**: Alpha Micro AM-1000E and AM-1200

**原文链接**: [http://oldvcr.blogspot.com/2026/03/refurb-weekend-double-header-alpha.html](http://oldvcr.blogspot.com/2026/03/refurb-weekend-double-header-alpha.html)

生成摘要时出错

---

## 57. Show HN: Atomic – Self-hosted, semantically-connected personal knowledge base

**原文标题**: Show HN: Atomic – Self-hosted, semantically-connected personal knowledge base

**原文链接**: [https://github.com/kenforthewin/atomic](https://github.com/kenforthewin/atomic)

生成摘要时出错

---

## 58. Training Center for Maneuvering on Manned Model Ships

**原文标题**: Training Center for Maneuvering on Manned Model Ships

**原文链接**: [https://www.portrevel.com/](https://www.portrevel.com/)

生成摘要时出错

---

## 59. Non-trivial error in physics paper found via Lean

**原文标题**: Non-trivial error in physics paper found via Lean

**原文链接**: [https://arxiv.org/abs/2603.08139](https://arxiv.org/abs/2603.08139)

生成摘要时出错

---

## 60. How Ford burned $12B in Brazil (2021)

**原文标题**: How Ford burned $12B in Brazil (2021)

**原文链接**: [https://www.reuters.com/business/autos-transportation/how-ford-burned-12-billion-brazil-2021-05-20/](https://www.reuters.com/business/autos-transportation/how-ford-burned-12-billion-brazil-2021-05-20/)

生成摘要时出错

---

## 61. $ teebot.dev – from terminal to tee in 6 seconds

**原文标题**: $ teebot.dev – from terminal to tee in 6 seconds

**原文链接**: [https://teebot.dev](https://teebot.dev)

生成摘要时出错

---

## 62. OpenCode – Open source AI coding agent

**原文标题**: OpenCode – Open source AI coding agent

**原文链接**: [https://opencode.ai/](https://opencode.ai/)

生成摘要时出错

---

## 63. Vatican Rebukes Peter Thiel's Antichrist Lectures in Rome

**原文标题**: Vatican Rebukes Peter Thiel's Antichrist Lectures in Rome

**原文链接**: [https://www.thenerdreich.com/peter-thiels-antichrist-circus-smacked-down-in-rome/](https://www.thenerdreich.com/peter-thiels-antichrist-circus-smacked-down-in-rome/)

生成摘要时出错

---

## 64. Mamba-3

**原文标题**: Mamba-3

**原文链接**: [https://www.together.ai/blog/mamba-3](https://www.together.ai/blog/mamba-3)

生成摘要时出错

---

## 65. Meta's Omnilingual MT for 1,600 Languages

**原文标题**: Meta's Omnilingual MT for 1,600 Languages

**原文链接**: [https://ai.meta.com/research/publications/omnilingual-mt-machine-translation-for-1600-languages/?_fb_noscript=1](https://ai.meta.com/research/publications/omnilingual-mt-machine-translation-for-1600-languages/?_fb_noscript=1)

生成摘要时出错

---

## 66. FFmpeg 101 (2024)

**原文标题**: FFmpeg 101 (2024)

**原文链接**: [https://blogs.igalia.com/llepage/ffmpeg-101/](https://blogs.igalia.com/llepage/ffmpeg-101/)

生成摘要时出错

---

## 67. Books of the Century by Le Monde

**原文标题**: Books of the Century by Le Monde

**原文链接**: [https://standardebooks.org/collections/le-mondes-100-books-of-the-century](https://standardebooks.org/collections/le-mondes-100-books-of-the-century)

生成摘要时出错

---

## 68. ZJIT removes redundant object loads and stores

**原文标题**: ZJIT removes redundant object loads and stores

**原文链接**: [https://railsatscale.com/2026-03-18-how-zjit-removes-redundant-object-loads-and-stores/](https://railsatscale.com/2026-03-18-how-zjit-removes-redundant-object-loads-and-stores/)

生成摘要时出错

---

## 69. A Visual Guide to Attention Variants in Modern LLMs

**原文标题**: A Visual Guide to Attention Variants in Modern LLMs

**原文链接**: [https://magazine.sebastianraschka.com/p/visual-attention-variants](https://magazine.sebastianraschka.com/p/visual-attention-variants)

生成摘要时出错

---

## 70. No Semicolons Needed

**原文标题**: No Semicolons Needed

**原文链接**: [https://terts.dev/blog/no-semicolons-needed/](https://terts.dev/blog/no-semicolons-needed/)

生成摘要时出错

---

## 71. Can Programming Be Liberated from the von Neumann Style? (1977) [pdf]

**原文标题**: Can Programming Be Liberated from the von Neumann Style? (1977) [pdf]

**原文链接**: [https://worrydream.com/refs/Backus_1978_-_Can_Programming_Be_Liberated_from_the_von_Neumann_Style.pdf](https://worrydream.com/refs/Backus_1978_-_Can_Programming_Be_Liberated_from_the_von_Neumann_Style.pdf)

生成摘要时出错

---

## 72. Molly guard in reverse

**原文标题**: Molly guard in reverse

**原文链接**: [https://unsung.aresluna.org/molly-guard-in-reverse/](https://unsung.aresluna.org/molly-guard-in-reverse/)

生成摘要时出错

---

## 73. A digital resource for studying the graffiti of Herculaneum and Pompeii

**原文标题**: A digital resource for studying the graffiti of Herculaneum and Pompeii

**原文链接**: [https://ancientgraffiti.org/Graffiti/](https://ancientgraffiti.org/Graffiti/)

生成摘要时出错

---

## 74. OpenAI to introduce ads to all ChatGPT free and Go users in US

**原文标题**: OpenAI to introduce ads to all ChatGPT free and Go users in US

**原文链接**: [https://www.reuters.com/business/media-telecom/openai-expand-ads-chatgpt-all-free-low-cost-users-information-reports-2026-03-21/](https://www.reuters.com/business/media-telecom/openai-expand-ads-chatgpt-all-free-low-cost-users-information-reports-2026-03-21/)

生成摘要时出错

---

## 75. Cross-Model Void Convergence: GPT-5.2 and Claude Opus 4.6 Deterministic Silence

**原文标题**: Cross-Model Void Convergence: GPT-5.2 and Claude Opus 4.6 Deterministic Silence

**原文链接**: [https://zenodo.org/records/18976656](https://zenodo.org/records/18976656)

生成摘要时出错

---

## 76. Blocking Internet Archive Won't Stop AI, but Will Erase Web's Historical Record

**原文标题**: Blocking Internet Archive Won't Stop AI, but Will Erase Web's Historical Record

**原文链接**: [https://www.eff.org/deeplinks/2026/03/blocking-internet-archive-wont-stop-ai-it-will-erase-webs-historical-record](https://www.eff.org/deeplinks/2026/03/blocking-internet-archive-wont-stop-ai-it-will-erase-webs-historical-record)

生成摘要时出错

---

## 77. Sandboxing: Foolproof Boundaries vs. Unbounded Foolishness (2025)

**原文标题**: Sandboxing: Foolproof Boundaries vs. Unbounded Foolishness (2025)

**原文链接**: [https://spawn-queue.acm.org/doi/10.1145/3733699](https://spawn-queue.acm.org/doi/10.1145/3733699)

生成摘要时出错

---

## 78. Freestyle Linked Lists Tricks

**原文标题**: Freestyle Linked Lists Tricks

**原文链接**: [https://nullprogram.com/blog/2025/12/31/](https://nullprogram.com/blog/2025/12/31/)

生成摘要时出错

---

## 79. An industrial piping contractor on Claude Code [video]

**原文标题**: An industrial piping contractor on Claude Code [video]

**原文链接**: [https://twitter.com/toddsaunders/status/2034243420147859716](https://twitter.com/toddsaunders/status/2034243420147859716)

生成摘要时出错

---

## 80. Linux Applications Programming by Example: The Fundamental APIs (2nd Edition)

**原文标题**: Linux Applications Programming by Example: The Fundamental APIs (2nd Edition)

**原文链接**: [https://github.com/arnoldrobbins/LinuxByExample-2e](https://github.com/arnoldrobbins/LinuxByExample-2e)

生成摘要时出错

---

## 81. Ubuntu 26.04 Ends 46 Years of Silent sudo Passwords

**原文标题**: Ubuntu 26.04 Ends 46 Years of Silent sudo Passwords

**原文链接**: [https://pbxscience.com/ubuntu-26-04-ends-46-years-of-silent-sudo-passwords/](https://pbxscience.com/ubuntu-26-04-ends-46-years-of-silent-sudo-passwords/)

生成摘要时出错

---

## 82. The Dude

**原文标题**: The Dude

**原文链接**: [https://yusufaytas.com/the-dude/](https://yusufaytas.com/the-dude/)

生成摘要时出错

---

## 83. I ran a 5-day experiment to see how fast Google reshapes your ad profile

**原文标题**: I ran a 5-day experiment to see how fast Google reshapes your ad profile

**原文链接**: [https://nanobuilds.substack.com/p/how-fast-can-you-reshape-what-google](https://nanobuilds.substack.com/p/how-fast-can-you-reshape-what-google)

生成摘要时出错

---

## 84. France's aircraft carrier located in real time by Le Monde through fitness app

**原文标题**: France's aircraft carrier located in real time by Le Monde through fitness app

**原文链接**: [https://www.lemonde.fr/en/international/article/2026/03/20/stravaleaks-france-s-aircraft-carrier-located-in-real-time-by-le-monde-through-fitness-app_6751640_4.html](https://www.lemonde.fr/en/international/article/2026/03/20/stravaleaks-france-s-aircraft-carrier-located-in-real-time-by-le-monde-through-fitness-app_6751640_4.html)

生成摘要时出错

---

## 85. Fujifilm X RAW STUDIO webapp clone

**原文标题**: Fujifilm X RAW STUDIO webapp clone

**原文链接**: [https://github.com/eggricesoy/filmkit](https://github.com/eggricesoy/filmkit)

生成摘要时出错

---

## 86. Kagi: Small Web Just Got Bigger

**原文标题**: Kagi: Small Web Just Got Bigger

**原文链接**: [https://blog.kagi.com/small-web-updates](https://blog.kagi.com/small-web-updates)

生成摘要时出错

---

## 87. Are humans naturally violent? New research challenges long-held assumptions

**原文标题**: Are humans naturally violent? New research challenges long-held assumptions

**原文链接**: [https://phys.org/news/2026-03-humans-naturally-violent-held-assumptions.html](https://phys.org/news/2026-03-humans-naturally-violent-held-assumptions.html)

生成摘要时出错

---

## 88. ArXiv declares independence from Cornell

**原文标题**: ArXiv declares independence from Cornell

**原文链接**: [https://www.science.org/content/article/arxiv-pioneering-preprint-server-declares-independence-cornell](https://www.science.org/content/article/arxiv-pioneering-preprint-server-declares-independence-cornell)

生成摘要时出错

---

## 89. A Japanese glossary of chopsticks faux pas (2022)

**原文标题**: A Japanese glossary of chopsticks faux pas (2022)

**原文链接**: [https://www.nippon.com/en/japan-data/h01362/](https://www.nippon.com/en/japan-data/h01362/)

生成摘要时出错

---

## 90. How BYD got EV chargers to work almost as fast as gas pumps

**原文标题**: How BYD got EV chargers to work almost as fast as gas pumps

**原文链接**: [https://www.wired.com/story/how-byds-ev-charger-got-even-faster-and-it-might-not-matter-as-much-as-you-think/](https://www.wired.com/story/how-byds-ev-charger-got-even-faster-and-it-might-not-matter-as-much-as-you-think/)

生成摘要时出错

---

## 91. A pig's brain has been frozen with its cellular activity locked in place

**原文标题**: A pig's brain has been frozen with its cellular activity locked in place

**原文链接**: [https://www.newscientist.com/article/2520204-major-leap-towards-reanimation-after-death-as-mammals-brain-preserved/](https://www.newscientist.com/article/2520204-major-leap-towards-reanimation-after-death-as-mammals-brain-preserved/)

生成摘要时出错

---

## 92. Discontinuation and reinitiation of dual-labeled GLP-1 receptor agonists

**原文标题**: Discontinuation and reinitiation of dual-labeled GLP-1 receptor agonists

**原文链接**: [https://nautil.us/whiplash-heart-attack-and-stroke-risk-jumps-when-people-stop-taking-glp-1s-1279029](https://nautil.us/whiplash-heart-attack-and-stroke-risk-jumps-when-people-stop-taking-glp-1s-1279029)

生成摘要时出错

---

## 93. Proof Theory and Logic Programming

**原文标题**: Proof Theory and Logic Programming

**原文链接**: [https://www.lix.polytechnique.fr/Labo/Dale.Miller/ptlp/](https://www.lix.polytechnique.fr/Labo/Dale.Miller/ptlp/)

生成摘要时出错

---

## 94. Astral to Join OpenAI

**原文标题**: Astral to Join OpenAI

**原文链接**: [https://astral.sh/blog/openai](https://astral.sh/blog/openai)

生成摘要时出错

---

## 95. We rewrote our Rust WASM parser in TypeScript and it got faster

**原文标题**: We rewrote our Rust WASM parser in TypeScript and it got faster

**原文链接**: [https://www.openui.com/blog/rust-wasm-parser](https://www.openui.com/blog/rust-wasm-parser)

生成摘要时出错

---

## 96. Iran will close strait of Hormuz if Trump acts on 48 hour infrastructure threat

**原文标题**: Iran will close strait of Hormuz if Trump acts on 48 hour infrastructure threat

**原文链接**: [https://www.theguardian.com/world/live/2026/mar/22/middle-east-crisis-live-iran-war-trump-ultimatum-major-attack-strait-of-hormuz-open-israel-hit-tehran-retaliation](https://www.theguardian.com/world/live/2026/mar/22/middle-east-crisis-live-iran-war-trump-ultimatum-major-attack-strait-of-hormuz-open-israel-hit-tehran-retaliation)

生成摘要时出错

---

## 97. Google details new 24-hour process to sideload unverified Android apps

**原文标题**: Google details new 24-hour process to sideload unverified Android apps

**原文链接**: [https://arstechnica.com/gadgets/2026/03/google-details-new-24-hour-process-to-sideload-unverified-android-apps/](https://arstechnica.com/gadgets/2026/03/google-details-new-24-hour-process-to-sideload-unverified-android-apps/)

生成摘要时出错

---

## 98. How we give every user SQL access to a shared ClickHouse cluster

**原文标题**: How we give every user SQL access to a shared ClickHouse cluster

**原文链接**: [https://trigger.dev/blog/how-trql-works](https://trigger.dev/blog/how-trql-works)

生成摘要时出错

---

## 99. Show HN: We built a terminal-only Bluesky / AT Proto client written in Fortran

**原文标题**: Show HN: We built a terminal-only Bluesky / AT Proto client written in Fortran

**原文链接**: [https://github.com/FormerLab/fortransky](https://github.com/FormerLab/fortransky)

生成摘要时出错

---

## 100. Too Much Color

**原文标题**: Too Much Color

**原文链接**: [https://www.keithcirkel.co.uk/too-much-color/](https://www.keithcirkel.co.uk/too-much-color/)

生成摘要时出错

---

