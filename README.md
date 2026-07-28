# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-07-28.md)

*最后自动更新时间: 2026-07-28 18:45:49*
## 1. 你本可以想到 Kimi Delta Attention

**原文标题**: You Could Have Come Up with Kimi Delta Attention

**原文链接**: [https://blog.doubleword.ai/you-could-have-come-up-with-kimi-delta-attention](https://blog.doubleword.ai/you-could-have-come-up-with-kimi-delta-attention)

本文逐步推导了 **Kimi Delta Attention (KDA)**，展示了复杂的线性注意力机制是如何从关联记忆（associative memory）的基础原理演变而来的。推导过程分为四个阶段：

1.  **线性注意力（Linear Attention）：** 通过移除标准平方复杂度注意力中的 softmax，模型可以将键值对存储在固定大小的循环状态（$S_t$）中。然而，简单的加法更新（$S_t = S_{t-1} + v_t k_t^\top$）会导致干扰，因为新信息是直接叠加到旧关联之上，而非将其替换。
2.  **DeltaNet：** 为解决干扰问题，DeltaNet 引入了 **Delta 规则**。它不再写入原始值（$v_t$），而是通过将当前值与现有记忆的预测值进行比较，计算出预测误差（$e_t$）。写入该误差在数学上等同于执行一步在线梯度下降，以最小化重构损失。
3.  **门控 DeltaNet（Gated DeltaNet）：** 虽然 Delta 规则提供了针对性的更新，但它无法处理正交方向上的陈旧信息。门控 DeltaNet 引入了一个标量保留门（$\alpha_t$），在应用 Delta 更新之前对状态进行全局遗忘。
4.  **Kimi Delta Attention (KDA)：** KDA 进一步优化了门控机制，将标量门替换为以对角矩阵（$D_t$）形式应用的**向量门**（$\alpha_t$）。这实现了通道级（channel-wise）遗忘，使模型能够独立地对键空间的特定维度进行选择性保留或丢弃。

总之，KDA 代表了一种复杂的循环更新机制，其状态转移矩阵呈现为“对角加低秩”结构。这种结构使模型能够通过 Delta 规则执行针对性的记忆替换，同时通过对角门控保持对信息衰减的细粒度控制。

---

## 2. Steel Bank Common Lisp 版本 2.6.7

**原文标题**: Steel Bank Common Lisp version 2.6.7

**原文链接**: [https://sbcl.org/all-news.html?2.6.7](https://sbcl.org/all-news.html?2.6.7)

Steel Bank Common Lisp (SBCL) 2.6.2 至 2.6.7 版本于 2026 年 2 月至 7 月按月发布，在平台支持、性能和文档方面引入了重大增强。

2.6.7 版本的一个主要新增内容是 **SB-MANUAL** 模块。该模块通过文档字符串将 SBCL 手册直接集成到交互式环境中，方便用户通过 Slime 等工具进行探索。文档字符串现在支持 Markdown 的子集，且手册中新增了声明索引。

**平台支持**进行了广泛更新，包括：
*   **新架构：** 支持 ARM64 版 Windows 以及 x86-64 上的 AVX512 指令集。
*   **SIMD 增强：** 扩展了 ARM64 和 x86-64 的 SIMD 能力，并改进了 UTF-8 转换例程。
*   **稳定性：** 针对 RISC-V、龙芯架构 (LoongArch)、PPC64 和 macOS 进行了重大修复。2.6.3 版本通过在多个架构上移除对 Lisp 返回地址对象（Lisp Return Address object）的要求，简化了调用约定。

**性能优化**侧重于通过利用哈希表减少内存分配（consing）来优化序列操作（如 `COUNT`、`INTERSECTION` 和 `UNION`）。编译器还针对 `AREF`、`COERCE` 和 `ELT` 实现了更精确的类型推导，并提升了对常量复数的处理效率。

**稳定性与错误修复**解决了编译器死循环问题，提高了 mark-region 垃圾回收器的稳定性，并修正了与 FFI 相关的内存问题。

**不兼容的变更**虽然细微但值得注意，包括：调整 `FDEFINITION` 以匹配 `SYMBOL-FUNCTION`，将某些槽（slot）访问错误移出 `TYPE-ERROR` 范畴，以及对 `MAKE-ARRAY` 执行更严格的验证。

总体而言，这些版本在精进 SBCL 硬件特定性能的同时，显著提升了开发者的交互式文档体验。

---

## 3. 延迟满足——以“最后报道突发新闻”为荣

**原文标题**: Delayed Gratification – Proud to Be 'Last to Breaking News'

**原文链接**: [https://www.slow-journalism.com/](https://www.slow-journalism.com/)

**《延迟满足》**（Delayed Gratification）创刊于2011年，是全球首本“慢新闻”季刊。该杂志秉持“以‘最后报道突发新闻’为荣”的信条，在重大全球事件发生三个月后对其进行重新审视，为狂躁的24小时新闻周期提供了一个具有反思性且深入的参照。

该刊通过独立报道和精美的信息图表，为重大新闻提供背景和视角。近期的刊号涵盖了广泛的全球议题，包括委内瑞拉政坛局势、美国大选的影响、加沙冲突，以及飓风“梅丽莎”等环境危机。每一期杂志都以极高的制作水准著称，封面通常出自大卫·霍克尼（David Hockney）、谢泼德·费尔雷（Shepard Fairey）和埃米利亚诺·蓬齐（Emiliano Ponzi）等知名创作人之手。

除了纸质杂志，该机构还通过以下渠道推动“慢新闻革命”：
*   **教育大师班：** 提供在线直播课程，教授如何创办独立杂志以及如何制作专业信息图表等技能。
*   **数字化参与：** 推送包含“慢新闻”和信息图表的时事通讯，并活跃于各大社交媒体。
*   **业内赞誉：** 该杂志赢得了行业领袖的高度评价，其中包括《私家侦探》（Private Eye）编辑伊恩·希斯洛普（Ian Hislop），他称其为“英国第二好的杂志”。

总之，《延迟满足》优先考虑品质、智慧和启发，而非传播速度，鼓励读者摒弃即时、浅薄的标题，转而选择全面、回顾性的深度分析。

---

## 4. Zig 增量编译内部机制

**原文标题**: Zig's Incremental Compilation Internals

**原文链接**: [https://mlugg.co.uk/posts/incremental-compilation-internals/](https://mlugg.co.uk/posts/incremental-compilation-internals/)

Zig 编译器引入了一套强大的增量编译系统，能够实现复杂应用的毫秒级重建。通过检测函数和声明级别的特定更改，编译器避免了全量重新编译，而是直接将产生的字节补丁打入输出的二进制文件中。

作者将该实现划分为三个核心阶段：

1.  **源码处理：** Zig 将源文件转换为 **ZIR**（Zig 中间表示）。这一阶段具有“极高的并行性”并利用了磁盘缓存。由于一个文件的 ZIR 生成是其内容的纯函数，编译器仅重新处理发生实际更改的文件。
2.  **语义分析：** 此阶段负责类型检查和编译时（comptime）求值。Zig 将代码拆分为**分析单元**（如函数体或常量值），并利用依赖图进行管理。当源码哈希值发生变化时，编译器通过该图识别并仅重新分析受影响的单元。Zig 的语言设计经过专门优化，以确保这些依赖关系能够被有效地建模和隔离。
3.  **代码生成：** AIR（分析中间表示）以函数级粒度转换为 **MIR**（机器中间表示）。由于各函数是独立生成的，这一阶段具有高度并行性，且无需中间缓存。

最后，文章讨论了**增量链接**。虽然通用的增量链接器非常罕见且难以构建，但 Zig 对整个流水线的掌控使其能够避开传统“对比”输入对象所面临的困难。

尽管该特性在 Zig 0.16.0 中已提供，但完整的链接器功能仍需最新的 master 分支（以及最终的 0.17.0 版本）。其结果是，即使是大型项目，开发工作流的更新耗时也仅需 50–70 毫秒。

---

## 5. 日本7.1级地震

**原文标题**: 7.1 Earthquake in Japan

**原文链接**: [https://www.data.jma.go.jp/multi/quake/quake_detail.html?eventID=20260728163528&lang=en](https://www.data.jma.go.jp/multi/quake/quake_detail.html?eventID=20260728163528&lang=en)

提供的这段内容看起来更像是一个地震报告的抬头或模板（列出了都道府县、震度和市町村），而非一篇描述性文章。不过，根据标题，这指的是2024年8月8日发生在日本的7.1级大地震。

### 摘要：九州7.1级地震（2024年8月）

2024年8月8日下午约4时43分，九州东海岸的日向滩海域发生了7.1级强震。此次地震立即触发了应急预案，并引发了日本全国对地质状况的高度关注。

**关键信息：**
*   **地震烈度**：此次地震在宫崎县日南市记录到日本气象厅震度等级最高为“6弱”。鹿儿岛县和熊本县的部分地区也记录到了5级的强震。
*   **海啸预警**：九州和四国的太平洋沿岸发布了海啸预警。在宫崎港观测到的海浪高达50厘米，但未发生大规模洪涝。
*   **影响**：地震导致多人受伤，主要原因为摔倒和玻璃破碎。灾情包括轻微山体滑坡、道路裂缝，以及新干线暂时停运和局部地区停电。
*   **历史先例**：此次事件是日本气象厅首次触发针对南海海槽的“特大地震预警”。专家警告称，南海海槽发生后续灾难性地震的风险暂时增加，促使全国进入了为期一周的高度戒备状态。

虽然“特大地震预警”最终在未发生后续灾害的情况下解除，但这次7.1级地震对日本更新后的应急警报系统是一次重大考验，并再次凸显了该地区防灾准备的重要性。

---

## 6. Kimi K3 架构概览与笔记

**原文标题**: Kimi K3 Architecture Overview and Notes

**原文链接**: [https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html](https://sebastianraschka.com/blog/2026/kimi-k3-architecture-notes.html)

Kimi K3 是一款新发布的开源模型，它将之前的 Kimi Linear 架构从 48B 扩展到了庞大的 2.8T 参数，使其成为目前可用的规模最大的开源模型。

该架构通过以下几个关键组件优先提升推理效率：
*   **LatentMoE：** 新增组件，通过压缩大型线性层（类似于 Nemotron 3 Ultra）来减少计算开销。
*   **效率优化注意力机制：** 利用多头潜变量注意力和 Kimi Delta 注意力来优化性能。
*   **注意力残差：** 不同于标准的残差路径，K3 利用注意力分数对贡献进行加权，从而跨层连接残差。这以极小的成本增加（训练增加 4%，推理增加 2%）提升了验证损失表现和下游任务性能。
*   **NoPE（无位置嵌入）：** 不同于行业普遍使用 RoPE（旋转位置嵌入）的趋势，K3 在所有层中完全移除了位置嵌入。这是全球首个采用该方案的前沿级模型。

此外，Kimi K3 还引入了原生多模态支持。尽管其架构复杂，但它遵循了更广泛的行业趋势（如 DeepSeek V4 等模型所示）：即用效率优化版本替换标准组件，并改进残差连接路径，以获得更好的稳定性和性能。

---

## 7. 如何对 eBPF 代码进行性能分析？

**原文标题**: How Do I Profile eBPF Code?

**原文链接**: [https://naveensrinivasan.com/posts/2026-07-22-how-do-i-profile-ebpf-code/](https://naveensrinivasan.com/posts/2026-07-22-how-do-i-profile-ebpf-code/)

本文概述了一种分析 eBPF 代码以衡量其性能开销的实用方法，并以 LSM（Linux 安全模块）文件打开钩子（hook）作为案例研究。

该分析过程由四个关键阶段组成：

1.  **测试框架：** 为了隔离 eBPF 开销，作者提供了一个极简的 C 程序来基准测试 `openat` 系统调用的延迟。它通过使用预热缓存、内存锁定以防止缺页异常以及直接系统调用，将干扰降至最低。基准测试使用 `taskset` 进行 CPU 绑定，并使用 `chrt` 进行高优先级调度，以确保结果的一致性。
2.  **系统配置：** 为确保 `perf` 工具能够解析 eBPF 符号，必须启用特定的 `sysctl` 设置（`net.core.bpf_jit_enable` 和 `net.core.bpf_jit_kallsyms`）。这使得分析器能够显示实际的 BPF 程序名称，而非十六进制地址。
3.  **测量：** 该过程涉及建立一个没有 eBPF 的性能基准，然后在 eBPF 工作负载和基准测试运行时执行 `perf record`。配置专门采样内核态下的 CPU 周期，并利用帧指针进行准确的堆栈回溯。
4.  **分析：** 通过生成 `perf report` 或火焰图，开发人员可以可视化调用栈。这有助于识别 eBPF 执行路径中的特定瓶颈，例如频繁的 `bpf_probe_read_kernel` 调用或高开销的 map 查找。

最终，该工作流允许开发人员精确定位钩子中耗时的位置，从而进行针对性优化（如缓存或算法改进），以减少对系统的性能影响。

---

## 8. 利用 Claude 发现密码学弱点

**原文标题**: Discovering Cryptographic Weaknesses with Claude

**原文链接**: [https://www.anthropic.com/research/discovering-cryptographic-weaknesses](https://www.anthropic.com/research/discovering-cryptographic-weaknesses)

生成摘要时出错

---

## 9. Show HN: XY – A Fast, composable, GPU-accelerated interactive plotting library

**原文标题**: Show HN: XY – A Fast, composable, GPU-accelerated interactive plotting library

**原文链接**: [https://github.com/reflex-dev/xy](https://github.com/reflex-dev/xy)

生成摘要时出错

---

## 10. iPhone Upgrade Program

**原文标题**: iPhone Upgrade Program

**原文链接**: [https://www.apple.com/shop/iphone/iphone-upgrade-program](https://www.apple.com/shop/iphone/iphone-upgrade-program)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 2 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 3 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 4 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 5 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 6 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 7 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 8 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 9 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 10 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 11 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 12 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 13 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 14 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 15 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 16 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 17 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 18 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 19 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 20 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 21 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 22 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 23 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 24 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 25 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 26 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 27 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 28 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 29 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 30 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 31 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 32 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 33 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 34 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 35 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 36 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 37 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 38 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 39 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 40 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 41 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 42 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 43 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 44 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 45 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 46 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 47 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 48 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 49 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 50 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 51 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 52 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 53 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 54 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 55 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 56 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 57 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 58 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 59 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 60 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 61 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 62 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 63 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 64 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 65 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 66 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 67 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 68 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 69 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 70 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 71 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 72 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 73 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 74 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 75 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 76 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 77 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 78 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 79 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 80 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 81 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 82 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 83 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 84 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 85 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 86 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 87 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 88 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 89 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 90 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 91 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 92 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 93 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 94 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 95 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 96 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 97 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 98 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 99 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 100 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 101 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 102 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 103 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 104 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 105 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 106 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 107 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 108 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 109 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 110 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 111 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 112 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 113 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 114 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 115 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 116 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 117 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 118 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 119 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 120 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 121 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 122 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 123 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 124 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 125 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 126 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 127 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 128 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 129 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 130 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 131 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 132 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 133 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 134 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 135 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 136 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 137 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 138 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 139 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 140 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 141 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 142 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 143 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 144 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 145 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 146 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 147 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 148 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 149 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 150 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 151 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 152 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 153 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 154 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 155 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 156 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 157 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 158 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 159 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 160 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 161 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 162 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 163 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 164 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 165 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 166 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 167 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 168 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 169 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 170 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 171 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 172 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 173 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 174 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 175 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 176 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 177 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 178 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 179 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 180 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 181 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 182 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 183 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 184 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 185 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 186 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 187 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 188 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 189 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 190 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 191 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 192 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 193 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 194 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 195 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 196 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 197 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 198 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 199 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 200 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 201 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 202 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 203 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 204 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 205 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 206 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 207 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 208 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 209 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 210 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 211 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 212 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 213 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 214 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 215 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 216 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 217 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 218 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 219 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 220 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 221 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 222 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 223 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 224 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 225 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 226 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 227 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 228 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 229 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 230 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 231 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 232 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 233 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 234 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 235 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 236 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 237 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 238 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 239 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 240 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 241 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 242 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 243 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 244 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 245 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 246 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 247 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 248 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 249 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 250 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 251 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 252 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 253 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 254 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 255 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 256 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 257 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 258 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 259 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 260 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 261 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 262 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 263 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 264 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 265 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 266 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 267 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 268 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 269 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 270 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 271 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 272 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 273 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 274 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 275 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 276 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 277 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 278 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 279 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 280 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 281 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 282 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 283 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 284 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 285 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 286 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 287 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 288 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 289 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 290 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 291 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 292 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 293 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 294 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 295 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 296 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 297 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 298 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 299 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 300 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 301 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 302 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 303 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 304 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 305 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 306 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 307 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 308 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 309 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 310 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 311 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 312 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 313 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 314 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 315 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 316 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 317 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 318 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 319 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 320 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 321 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 322 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 323 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 324 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 325 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 326 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 327 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 328 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 329 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 330 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 331 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 332 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 333 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 334 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 335 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 336 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 337 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 338 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 339 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 340 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 341 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 342 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 343 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 344 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 345 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 346 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 347 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 348 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 349 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 350 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 351 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 352 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 353 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 354 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 355 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 356 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 357 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 358 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 359 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 360 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 361 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 362 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 363 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 364 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 365 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 366 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 367 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 368 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 369 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 370 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 371 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 372 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 373 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 374 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 375 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 376 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 377 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 378 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 379 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 380 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 381 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 382 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 383 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 384 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 385 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 386 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 387 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 388 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 389 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 390 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 391 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 392 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 393 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 394 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 395 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 396 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 397 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 398 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 399 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 400 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 401 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 402 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 403 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 404 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 405 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 406 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 407 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 408 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 409 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 410 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 411 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 412 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 413 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 414 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 415 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 416 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 417 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 418 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 419 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 420 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 421 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 422 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 423 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 424 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 425 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 426 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 427 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 428 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 429 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 430 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 431 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 432 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 433 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 434 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 435 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 436 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 437 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 438 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 439 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 440 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 441 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 442 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 443 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 444 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 445 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 446 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 447 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 448 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 449 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 450 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 451 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 452 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 453 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 454 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 455 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 456 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 457 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 458 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 459 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 460 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 461 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 462 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 463 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 464 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 465 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 466 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 467 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 468 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 469 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 470 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 471 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 472 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 473 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 474 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 475 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 476 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 477 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 478 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 479 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 480 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 481 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 482 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 483 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 484 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 485 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 486 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 487 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 488 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 489 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 490 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 491 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 492 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 493 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 494 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 495 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
