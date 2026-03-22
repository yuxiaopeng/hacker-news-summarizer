# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-22.md)

*最后自动更新时间: 2026-03-22 17:54:12*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 2 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 3 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 4 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 5 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 6 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 7 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 8 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 9 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 10 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 11 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 12 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 13 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 14 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 15 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 16 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 17 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 18 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 19 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 20 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 21 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 22 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 23 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 24 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 25 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 26 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 27 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 28 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 29 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 30 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 31 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 32 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 33 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 34 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 35 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 36 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 37 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 38 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 39 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 40 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 41 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 42 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 43 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 44 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 45 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 46 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 47 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 48 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 49 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 50 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 51 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 52 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 53 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 54 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 55 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 56 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 57 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 58 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 59 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 60 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 61 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 62 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 63 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 64 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 65 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 66 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 67 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 68 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 69 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 70 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 71 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 72 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 73 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 74 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 75 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 76 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 77 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 78 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 79 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 80 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 81 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 82 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 83 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 84 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 85 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 86 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 87 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 88 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 89 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 90 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 91 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 92 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 93 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 94 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 95 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 96 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 97 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 98 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 99 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 100 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 101 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 102 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 103 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 104 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 105 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 106 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 107 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 108 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 109 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 110 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 111 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 112 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 113 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 114 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 115 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 116 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 117 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 118 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 119 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 120 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 121 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 122 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 123 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 124 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 125 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 126 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 127 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 128 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 129 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 130 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 131 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 132 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 133 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 134 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 135 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 136 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 137 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 138 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 139 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 140 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 141 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 142 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 143 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 144 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 145 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 146 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 147 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 148 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 149 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 150 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 151 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 152 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 153 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 154 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 155 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 156 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 157 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 158 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 159 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 160 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 161 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 162 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 163 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 164 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 165 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 166 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 167 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 168 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 169 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 170 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 171 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 172 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 173 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 174 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 175 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 176 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 177 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 178 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 179 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 180 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 181 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 182 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 183 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 184 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 185 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 186 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 187 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 188 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 189 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 190 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 191 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 192 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 193 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 194 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 195 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 196 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 197 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 198 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 199 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 200 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 201 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 202 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 203 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 204 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 205 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 206 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 207 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 208 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 209 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 210 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 211 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 212 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 213 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 214 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 215 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 216 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 217 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 218 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 219 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 220 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 221 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 222 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 223 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 224 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 225 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 226 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 227 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 228 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 229 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 230 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 231 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 232 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 233 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 234 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 235 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 236 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 237 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 238 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 239 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 240 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 241 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 242 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 243 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 244 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 245 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 246 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 247 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 248 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 249 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 250 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 251 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 252 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 253 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 254 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 255 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 256 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 257 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 258 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 259 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 260 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 261 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 262 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 263 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 264 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 265 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 266 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 267 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 268 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 269 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 270 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 271 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 272 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 273 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 274 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 275 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 276 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 277 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 278 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 279 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 280 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 281 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 282 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 283 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 284 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 285 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 286 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 287 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 288 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 289 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 290 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 291 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 292 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 293 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 294 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 295 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 296 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 297 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 298 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 299 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 300 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 301 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 302 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 303 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 304 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 305 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 306 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 307 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 308 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 309 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 310 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 311 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 312 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 313 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 314 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 315 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 316 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 317 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 318 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 319 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 320 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 321 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 322 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 323 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 324 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 325 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 326 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 327 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 328 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 329 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 330 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 331 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 332 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 333 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 334 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 335 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 336 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 337 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 338 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 339 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 340 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 341 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 342 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 343 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 344 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 345 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 346 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 347 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 348 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 349 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 350 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 351 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 352 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 353 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 354 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 355 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 356 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 357 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 358 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 359 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 360 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 361 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 362 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 363 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 364 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 365 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 366 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 367 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
