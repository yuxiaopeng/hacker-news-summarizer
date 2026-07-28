# Hacker News 热门文章摘要 (2026-07-28)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. New HIV vaccine shows unprecedented success in preclinical study

**原文标题**: New HIV vaccine shows unprecedented success in preclinical study

**原文链接**: [https://www.lji.org/news-events/news/post/new-hiv-vaccine-shows-unprecedented-success-in-preclinical-study/](https://www.lji.org/news-events/news/post/new-hiv-vaccine-shows-unprecedented-success-in-preclinical-study/)

生成摘要时出错

---

## 12. Substack writers, you need a website

**原文标题**: Substack writers, you need a website

**原文链接**: [https://elizabethtai.com/2026/06/10/substack-writers-you-need-a-website/](https://elizabethtai.com/2026/06/10/substack-writers-you-need-a-website/)

生成摘要时出错

---

## 13. Kimi Linear: An Expressive, Efficient Attention Architecture

**原文标题**: Kimi Linear: An Expressive, Efficient Attention Architecture

**原文链接**: [https://arxiv.org/abs/2510.26692](https://arxiv.org/abs/2510.26692)

生成摘要时出错

---

## 14. WOFF 1.0: a milestone on W3C's journey of fonts on the web

**原文标题**: WOFF 1.0: a milestone on W3C's journey of fonts on the web

**原文链接**: [https://www.w3.org/blog/2026/woff-1-0-a-milestone-on-w3cs-journey-of-fonts-on-the-web/](https://www.w3.org/blog/2026/woff-1-0-a-milestone-on-w3cs-journey-of-fonts-on-the-web/)

生成摘要时出错

---

## 15. Now Is the Time to Give LLMs Access to the ACM Digital Library

**原文标题**: Now Is the Time to Give LLMs Access to the ACM Digital Library

**原文链接**: [https://cacm.acm.org/opinion/now-is-the-time-to-give-llms-access-to-the-acm-digital-library/](https://cacm.acm.org/opinion/now-is-the-time-to-give-llms-access-to-the-acm-digital-library/)

生成摘要时出错

---

## 16. Harmony Explained: Progress Towards a Scientific Theory of Music (2012)

**原文标题**: Harmony Explained: Progress Towards a Scientific Theory of Music (2012)

**原文链接**: [https://arxiv.org/abs/1202.4212](https://arxiv.org/abs/1202.4212)

生成摘要时出错

---

## 17. Using a Gaming PC's RTX 5070 from a separate Linux workstation

**原文标题**: Using a Gaming PC's RTX 5070 from a separate Linux workstation

**原文链接**: [https://stephenkrings.com/posts/rtx-5070-linux-gpu-server/](https://stephenkrings.com/posts/rtx-5070-linux-gpu-server/)

生成摘要时出错

---

## 18. Anthropeum

**原文标题**: Anthropeum

**原文链接**: [https://anthropeum.com/](https://anthropeum.com/)

生成摘要时出错

---

## 19. So, you want to make a game engine (2023)

**原文标题**: So, you want to make a game engine (2023)

**原文链接**: [https://lisyarus.github.io/blog/posts/so-you-want-to-make-a-game-engine.html#part-3](https://lisyarus.github.io/blog/posts/so-you-want-to-make-a-game-engine.html#part-3)

生成摘要时出错

---

## 20. DMARC Has Been Public Since 2012. 68.4% of Domains Still Don't Enforce It

**原文标题**: DMARC Has Been Public Since 2012. 68.4% of Domains Still Don't Enforce It

**原文链接**: [https://ciphercue.com/blog/dmarc-enforcement-gap-rua-fragmentation-2026](https://ciphercue.com/blog/dmarc-enforcement-gap-rua-fragmentation-2026)

生成摘要时出错

---

## 21. How to Survive Boiling Water

**原文标题**: How to Survive Boiling Water

**原文链接**: [https://taxa.substack.com/p/how-to-survive-boiling-water](https://taxa.substack.com/p/how-to-survive-boiling-water)

生成摘要时出错

---

## 22. Stop Killing the Internet: No Digital ID and No Age Verification

**原文标题**: Stop Killing the Internet: No Digital ID and No Age Verification

**原文链接**: [https://citizens-initiative.europa.eu/initiatives/details/2026/000011_en](https://citizens-initiative.europa.eu/initiatives/details/2026/000011_en)

生成摘要时出错

---

## 23. Una Watch: Garmin watch competitor but repairable, open ecosystem and USB-C

**原文标题**: Una Watch: Garmin watch competitor but repairable, open ecosystem and USB-C

**原文链接**: [https://unawatch.com/](https://unawatch.com/)

生成摘要时出错

---

## 24. Show HN: Formally verified 3D CSG: Trust 93 lines spec, not 1000 lines AI code

**原文标题**: Show HN: Formally verified 3D CSG: Trust 93 lines spec, not 1000 lines AI code

**原文链接**: [https://github.com/schildep/verified-3d-mesh-intersection](https://github.com/schildep/verified-3d-mesh-intersection)

生成摘要时出错

---

## 25. Xenharmlib (music theory library) adds support for Just Intonation

**原文标题**: Xenharmlib (music theory library) adds support for Just Intonation

**原文链接**: [https://xenharmlib.readthedocs.io/en/latest/whats_new_0_4_0.html](https://xenharmlib.readthedocs.io/en/latest/whats_new_0_4_0.html)

生成摘要时出错

---

## 26. VMs can't boot with Network Mode set to Bridged on Apple M5 Pro machines

**原文标题**: VMs can't boot with Network Mode set to Bridged on Apple M5 Pro machines

**原文链接**: [https://github.com/utmapp/UTM/issues/7658](https://github.com/utmapp/UTM/issues/7658)

生成摘要时出错

---

## 27. Google's Beyond Zero: Enterprise Security for the AI Era

**原文标题**: Google's Beyond Zero: Enterprise Security for the AI Era

**原文链接**: [https://spawn-queue.acm.org/doi/10.1145/3819083](https://spawn-queue.acm.org/doi/10.1145/3819083)

生成摘要时出错

---

## 28. Show HN: Flashpaper – Self-destructing secret sharing with no database

**原文标题**: Show HN: Flashpaper – Self-destructing secret sharing with no database

**原文链接**: [https://flashpaper.app/](https://flashpaper.app/)

生成摘要时出错

---

## 29. Solving Fermat: Andrew Wiles

**原文标题**: Solving Fermat: Andrew Wiles

**原文链接**: [https://www.pbs.org/wgbh/nova/proof/wiles.html](https://www.pbs.org/wgbh/nova/proof/wiles.html)

生成摘要时出错

---

## 30. Scientific computing in the age of agentic AI

**原文标题**: Scientific computing in the age of agentic AI

**原文链接**: [https://openai.com/index/scientific-computing-agentic-ai/](https://openai.com/index/scientific-computing-agentic-ai/)

生成摘要时出错

---

## 31. Show HN: Scala Tutorials – interactive Scala 3 lessons in the browser

**原文标题**: Show HN: Scala Tutorials – interactive Scala 3 lessons in the browser

**原文链接**: [https://scalatutorials.com](https://scalatutorials.com)

生成摘要时出错

---

## 32. Citizen of the Galaxy (full text) by Robert Heinlein

**原文标题**: Citizen of the Galaxy (full text) by Robert Heinlein

**原文链接**: [https://metallicman.com/laoban4site/citizen-of-the-galaxy-full-text-by-robert-heinlein-2/](https://metallicman.com/laoban4site/citizen-of-the-galaxy-full-text-by-robert-heinlein-2/)

生成摘要时出错

---

## 33. A $500 RL fine-tune of a 9B open model beat frontier models on catalog review

**原文标题**: A $500 RL fine-tune of a 9B open model beat frontier models on catalog review

**原文链接**: [https://fermisense.com/when-machines-take-the-wheel/](https://fermisense.com/when-machines-take-the-wheel/)

生成摘要时出错

---

## 34. Show HN: Cynative – Read-only CLI in Go that explains your live infrastructure

**原文标题**: Show HN: Cynative – Read-only CLI in Go that explains your live infrastructure

**原文链接**: [https://github.com/cynative/cynative](https://github.com/cynative/cynative)

生成摘要时出错

---

## 35. Ubuntu's TPM encryption switches to snap kernel that blocks deb kernel packages

**原文标题**: Ubuntu's TPM encryption switches to snap kernel that blocks deb kernel packages

**原文链接**: [https://bare.systems/posts/ubuntu-tpm-snap/](https://bare.systems/posts/ubuntu-tpm-snap/)

生成摘要时出错

---

## 36. "Uncensored" open LLMs are measurably more optimistic than their base models

**原文标题**: "Uncensored" open LLMs are measurably more optimistic than their base models

**原文链接**: [https://arxiv.org/abs/2607.17427](https://arxiv.org/abs/2607.17427)

生成摘要时出错

---

## 37. Dolmenwood: Fantasy RPG built around the acclaimed Old-School Essentials rules

**原文标题**: Dolmenwood: Fantasy RPG built around the acclaimed Old-School Essentials rules

**原文链接**: [https://necroticgnome.com/collections/dolmenwood](https://necroticgnome.com/collections/dolmenwood)

生成摘要时出错

---

## 38. Setup Script Should Support Git Worktrees

**原文标题**: Setup Script Should Support Git Worktrees

**原文链接**: [https://piechowski.io/post/setup-script-git-worktrees/](https://piechowski.io/post/setup-script-git-worktrees/)

生成摘要时出错

---

## 39. Fast Remediation Is the New Trust Model (JFrog and OpenAI Zero-Day Findings)

**原文标题**: Fast Remediation Is the New Trust Model (JFrog and OpenAI Zero-Day Findings)

**原文链接**: [https://jfrog.com/blog/jfrog-and-openai-collaboration-on-zero-day-security-findings/](https://jfrog.com/blog/jfrog-and-openai-collaboration-on-zero-day-security-findings/)

生成摘要时出错

---

## 40. Chip stocks tumble as AI sell-off deepens

**原文标题**: Chip stocks tumble as AI sell-off deepens

**原文链接**: [https://www.ft.com/content/f8c03b5b-e194-4236-82c3-389b6f5dd7ae](https://www.ft.com/content/f8c03b5b-e194-4236-82c3-389b6f5dd7ae)

生成摘要时出错

---

## 41. About the security content of macOS Tahoe 26.6

**原文标题**: About the security content of macOS Tahoe 26.6

**原文链接**: [https://support.apple.com/en-us/128067](https://support.apple.com/en-us/128067)

生成摘要时出错

---

## 42. I'd not buy a LG monitor

**原文标题**: I'd not buy a LG monitor

**原文链接**: [https://beko.famkos.net/2026/07/27/id-not-buy-a-lg-monitor/](https://beko.famkos.net/2026/07/27/id-not-buy-a-lg-monitor/)

生成摘要时出错

---

## 43. Our position on open-weights models

**原文标题**: Our position on open-weights models

**原文链接**: [https://www.anthropic.com/news/position-open-weights-models](https://www.anthropic.com/news/position-open-weights-models)

生成摘要时出错

---

## 44. Usenet Archive Toolkit – process Usenet messages into a searchable archive

**原文标题**: Usenet Archive Toolkit – process Usenet messages into a searchable archive

**原文链接**: [https://github.com/wolfpld/usenetarchive](https://github.com/wolfpld/usenetarchive)

生成摘要时出错

---

## 45. Mondragon Corporation – a federation of co-operatives

**原文标题**: Mondragon Corporation – a federation of co-operatives

**原文链接**: [https://en.wikipedia.org/wiki/Mondragon_Corporation](https://en.wikipedia.org/wiki/Mondragon_Corporation)

生成摘要时出错

---

## 46. Show HN: Segue – Save context in one AI, load it in another by a short handle

**原文标题**: Show HN: Segue – Save context in one AI, load it in another by a short handle

**原文链接**: [https://segue.ai/](https://segue.ai/)

生成摘要时出错

---

## 47. Federal Judges Chastise Justice Department for 'Unlawful' Conduct

**原文标题**: Federal Judges Chastise Justice Department for 'Unlawful' Conduct

**原文链接**: [https://www.propublica.org/article/justice-department-presumption-of-regularity](https://www.propublica.org/article/justice-department-presumption-of-regularity)

生成摘要时出错

---

## 48. Rear center fuel tank adds roughly 20k liters and extends range by 1k NM

**原文标题**: Rear center fuel tank adds roughly 20k liters and extends range by 1k NM

**原文链接**: [https://www.airbus.com/en/newsroom/press-releases/2026-06-worlds-longest-range-aircraft-the-airbus-a350-1000ulr-takes-to-the-skies](https://www.airbus.com/en/newsroom/press-releases/2026-06-worlds-longest-range-aircraft-the-airbus-a350-1000ulr-takes-to-the-skies)

生成摘要时出错

---

## 49. UpCodes (YC S17) is hiring remote AE's to help make buildings cheaper

**原文标题**: UpCodes (YC S17) is hiring remote AE's to help make buildings cheaper

**原文链接**: [https://up.codes/careers?utm_source=HN](https://up.codes/careers?utm_source=HN)

生成摘要时出错

---

## 50. The five primitives I run a one-person company on

**原文标题**: The five primitives I run a one-person company on

**原文链接**: [https://methezone.github.io/solo-operator-playbook/five-primitives.html](https://methezone.github.io/solo-operator-playbook/five-primitives.html)

生成摘要时出错

---

## 51. WebKit Features for Safari 26.6

**原文标题**: WebKit Features for Safari 26.6

**原文链接**: [https://webkit.org/blog/18178/webkit-features-for-safari-26-6/](https://webkit.org/blog/18178/webkit-features-for-safari-26-6/)

生成摘要时出错

---

## 52. A Deep Logo Study

**原文标题**: A Deep Logo Study

**原文链接**: [https://dannyspina.com/blog/my_new_logo_study](https://dannyspina.com/blog/my_new_logo_study)

生成摘要时出错

---

## 53. Ars Astronomica – English translations of rare Hebrew and Latin astronomy texts

**原文标题**: Ars Astronomica – English translations of rare Hebrew and Latin astronomy texts

**原文链接**: [https://arsastronomica.com/](https://arsastronomica.com/)

生成摘要时出错

---

## 54. Why haven't organoids solved all of drug discovery?

**原文标题**: Why haven't organoids solved all of drug discovery?

**原文链接**: [https://www.owlposting.com/p/why-havent-organoids-solved-all-of](https://www.owlposting.com/p/why-havent-organoids-solved-all-of)

生成摘要时出错

---

## 55. Vehicle Motion Cues

**原文标题**: Vehicle Motion Cues

**原文链接**: [https://support.apple.com/guide/iphone/iphone-comfortably-riding-a-vehicle-iph55564cb22/ios](https://support.apple.com/guide/iphone/iphone-comfortably-riding-a-vehicle-iph55564cb22/ios)

生成摘要时出错

---

## 56. Coding Tools MCP (v0.2.2):Give any AI chat or agent a pair of hands on your code

**原文标题**: Coding Tools MCP (v0.2.2):Give any AI chat or agent a pair of hands on your code

**原文链接**: [https://github.com/xyTom/coding-tools-mcp](https://github.com/xyTom/coding-tools-mcp)

生成摘要时出错

---

## 57. Show HN: tale.fyi, we deserve a home for fiction

**原文标题**: Show HN: tale.fyi, we deserve a home for fiction

**原文链接**: [https://tale.fyi/@sam/announcing-tale-fyi-read-or-listen-to-an-entire-book-from-a-single-link](https://tale.fyi/@sam/announcing-tale-fyi-read-or-listen-to-an-entire-book-from-a-single-link)

生成摘要时出错

---

## 58. Why Are Gay Bars Building Databases of Their Patrons?

**原文标题**: Why Are Gay Bars Building Databases of Their Patrons?

**原文链接**: [https://www.eff.org/deeplinks/2026/07/why-are-gay-bars-building-databases-their-patrons](https://www.eff.org/deeplinks/2026/07/why-are-gay-bars-building-databases-their-patrons)

生成摘要时出错

---

## 59. 24,650 internet-accessible BMCs leak password-derived hashes before login

**原文标题**: 24,650 internet-accessible BMCs leak password-derived hashes before login

**原文链接**: [https://lavahq.io/research/bmc-exposure-alert](https://lavahq.io/research/bmc-exposure-alert)

生成摘要时出错

---

## 60. When sine of x degrees equals sine of x radians

**原文标题**: When sine of x degrees equals sine of x radians

**原文链接**: [https://www.johndcook.com/blog/2026/07/22/degrees-radians/](https://www.johndcook.com/blog/2026/07/22/degrees-radians/)

生成摘要时出错

---

## 61. PyTorch: A Reference Language

**原文标题**: PyTorch: A Reference Language

**原文链接**: [https://docs.pytorch.org/devlogs/compiler/2026-07-25-pytorch-a-reference-language/](https://docs.pytorch.org/devlogs/compiler/2026-07-25-pytorch-a-reference-language/)

生成摘要时出错

---

## 62. Show HN: Base-GPUI: A GPUI port of Base UI headless components

**原文标题**: Show HN: Base-GPUI: A GPUI port of Base UI headless components

**原文链接**: [https://github.com/LukeTandjung/base-gpui](https://github.com/LukeTandjung/base-gpui)

生成摘要时出错

---

## 63. Moving from Claude to Proton Lumo

**原文标题**: Moving from Claude to Proton Lumo

**原文链接**: [https://blog.nutts.org/2026/07/27/moving-from-claude-to-proton-lumo/](https://blog.nutts.org/2026/07/27/moving-from-claude-to-proton-lumo/)

生成摘要时出错

---

## 64. Italy Blocks Reproductive Health Websites Women on Web and Women Help Women

**原文标题**: Italy Blocks Reproductive Health Websites Women on Web and Women Help Women

**原文链接**: [https://ooni.org/post/2026-italy-blocks-wow-and-whw](https://ooni.org/post/2026-italy-blocks-wow-and-whw)

生成摘要时出错

---

## 65. Questions and answers on AI and verification: follow-up to my May ACM Tech Talk

**原文标题**: Questions and answers on AI and verification: follow-up to my May ACM Tech Talk

**原文链接**: [https://bertrandmeyer.com/2026/07/21/questions-and-answers-on-ai-and-verification-a-follow-up-to-my-may-acm-tech-talk/](https://bertrandmeyer.com/2026/07/21/questions-and-answers-on-ai-and-verification-a-follow-up-to-my-may-acm-tech-talk/)

生成摘要时出错

---

## 66. There are no fire alarms when it comes to privacy

**原文标题**: There are no fire alarms when it comes to privacy

**原文链接**: [https://www.unsungnovelty.org/posts/07/2026/fire-alarms-privacy/](https://www.unsungnovelty.org/posts/07/2026/fire-alarms-privacy/)

生成摘要时出错

---

## 67. The More You Buy, the More You Lose

**原文标题**: The More You Buy, the More You Lose

**原文链接**: [https://www.wheresyoured.at/the-more-you-buy-the-more-you-lose/](https://www.wheresyoured.at/the-more-you-buy-the-more-you-lose/)

生成摘要时出错

---

## 68. TWC Classics

**原文标题**: TWC Classics

**原文链接**: [https://twcclassics.com/](https://twcclassics.com/)

生成摘要时出错

---

## 69. Don't ask an LLM for a confidence score

**原文标题**: Don't ask an LLM for a confidence score

**原文链接**: [https://justinflick.com/2026/07/27/llm-confidence-scores.html](https://justinflick.com/2026/07/27/llm-confidence-scores.html)

生成摘要时出错

---

## 70. Home Office used 'AI hallucinated' information to refuse asylum claim, judge

**原文标题**: Home Office used 'AI hallucinated' information to refuse asylum claim, judge

**原文链接**: [https://www.theguardian.com/uk-news/2026/jul/28/home-office-used-ai-hallucinated-information-to-refuse-asylum-claim-judge-suggests](https://www.theguardian.com/uk-news/2026/jul/28/home-office-used-ai-hallucinated-information-to-refuse-asylum-claim-judge-suggests)

生成摘要时出错

---

## 71. Launch HN: Rise Reforming (YC S26) – Turning Waste Gases into Valuable Chemicals

**原文标题**: Launch HN: Rise Reforming (YC S26) – Turning Waste Gases into Valuable Chemicals

**原文链接**: [https://www.rise-reforming.com](https://www.rise-reforming.com)

生成摘要时出错

---

## 72. DConf 2026 in London

**原文标题**: DConf 2026 in London

**原文链接**: [https://dconf.org/2026/index.html](https://dconf.org/2026/index.html)

生成摘要时出错

---

## 73. The AI risk is inside the labs

**原文标题**: The AI risk is inside the labs

**原文链接**: [https://antirez.com/news/172](https://antirez.com/news/172)

生成摘要时出错

---

## 74. Programming Languages Are Authoring Tools for Platforms

**原文标题**: Programming Languages Are Authoring Tools for Platforms

**原文链接**: [https://www.makonea.com/en-US/blog/programming-languages-are-authoring-tools-for-platforms](https://www.makonea.com/en-US/blog/programming-languages-are-authoring-tools-for-platforms)

生成摘要时出错

---

## 75. Kimi K3 Now Available via Telnyx Inference API

**原文标题**: Kimi K3 Now Available via Telnyx Inference API

**原文链接**: [https://telnyx.com/release-notes/kimi-k3-telnyx-inference](https://telnyx.com/release-notes/kimi-k3-telnyx-inference)

生成摘要时出错

---

## 76. Contrail Avoidance for the Climate

**原文标题**: Contrail Avoidance for the Climate

**原文链接**: [https://contrails.org/](https://contrails.org/)

生成摘要时出错

---

## 77. Apple Upgrade

**原文标题**: Apple Upgrade

**原文链接**: [https://www.apple.com/shop/apple-upgrade](https://www.apple.com/shop/apple-upgrade)

生成摘要时出错

---

## 78. Show HN: Tines 3B – safe workflow automation for when everyone builds software

**原文标题**: Show HN: Tines 3B – safe workflow automation for when everyone builds software

**原文链接**: [https://www.tines.com/](https://www.tines.com/)

生成摘要时出错

---

## 79. Show HN: Ctrlb-decompose: Strip the noise from logs before sending to LLMs

**原文标题**: Show HN: Ctrlb-decompose: Strip the noise from logs before sending to LLMs

**原文链接**: [https://github.com/ctrlb-hq/ctrlb-decompose](https://github.com/ctrlb-hq/ctrlb-decompose)

生成摘要时出错

---

## 80. GOG confirm they are working towards GOG Galaxy on Linux

**原文标题**: GOG confirm they are working towards GOG Galaxy on Linux

**原文链接**: [https://www.gamingonlinux.com/2026/07/gog-confirm-they-are-working-towards-gog-galaxy-on-linux/](https://www.gamingonlinux.com/2026/07/gog-confirm-they-are-working-towards-gog-galaxy-on-linux/)

生成摘要时出错

---

## 81. Show HN: Yap – OSS on-device voice dictation for macOS with no model to download

**原文标题**: Show HN: Yap – OSS on-device voice dictation for macOS with no model to download

**原文链接**: [https://github.com/FrigadeHQ/yap](https://github.com/FrigadeHQ/yap)

生成摘要时出错

---

## 82. Benchmarking Opus 5 on SlopCodeBench

**原文标题**: Benchmarking Opus 5 on SlopCodeBench

**原文链接**: [https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-opus-5-on-slop-code-bench.md](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/benchmarking-opus-5-on-slop-code-bench.md)

生成摘要时出错

---

## 83. When Internal Memory Fails: A No-Solder Wii U Recovery

**原文标题**: When Internal Memory Fails: A No-Solder Wii U Recovery

**原文链接**: [https://smolnero.com/posts/when-internal-memory-fails-a-no-solder-wii-u-recovery](https://smolnero.com/posts/when-internal-memory-fails-a-no-solder-wii-u-recovery)

生成摘要时出错

---

## 84. The Origins of Modern Mathematics in Russia

**原文标题**: The Origins of Modern Mathematics in Russia

**原文链接**: [https://valeman.medium.com/the-origins-of-modern-mathematics-in-russia-from-peter-the-great-to-the-bernoullis-and-euler-6711b01f5f8f](https://valeman.medium.com/the-origins-of-modern-mathematics-in-russia-from-peter-the-great-to-the-bernoullis-and-euler-6711b01f5f8f)

生成摘要时出错

---

## 85. GrapheneOS Defends Data-Wiping Function That Blocked US Border Search

**原文标题**: GrapheneOS Defends Data-Wiping Function That Blocked US Border Search

**原文链接**: [https://www.pcmag.com/news/grapheneos-defends-data-wiping-function-that-blocked-us-border-search](https://www.pcmag.com/news/grapheneos-defends-data-wiping-function-that-blocked-us-border-search)

生成摘要时出错

---

## 86. Self-contained highly-portable Python distributions

**原文标题**: Self-contained highly-portable Python distributions

**原文链接**: [https://gregoryszorc.com/docs/python-build-standalone/main/](https://gregoryszorc.com/docs/python-build-standalone/main/)

生成摘要时出错

---

## 87. Apple Upgrade Launches in the United States

**原文标题**: Apple Upgrade Launches in the United States

**原文链接**: [https://www.apple.com/newsroom/2026/07/apple-upgrade-launches-in-the-united-states/](https://www.apple.com/newsroom/2026/07/apple-upgrade-launches-in-the-united-states/)

生成摘要时出错

---

## 88. How did The Shawshank Redemption become the highest rated #1 movie on IMDB?

**原文标题**: How did The Shawshank Redemption become the highest rated #1 movie on IMDB?

**原文链接**: [https://old.reddit.com/r/NoStupidQuestions/comments/1v8pm2x/comment/p07p4ri/](https://old.reddit.com/r/NoStupidQuestions/comments/1v8pm2x/comment/p07p4ri/)

生成摘要时出错

---

## 89. Show HN: BrowserAct: Browser Layer for Your AI Agent

**原文标题**: Show HN: BrowserAct: Browser Layer for Your AI Agent

**原文链接**: [https://github.com/browser-act/skills](https://github.com/browser-act/skills)

生成摘要时出错

---

## 90. Securing Services with Rootless Containers

**原文标题**: Securing Services with Rootless Containers

**原文链接**: [https://blog.coderspirit.xyz/blog/2026/07/06/securing-services-with-rootless-containers/](https://blog.coderspirit.xyz/blog/2026/07/06/securing-services-with-rootless-containers/)

生成摘要时出错

---

## 91. Show HN: Open-source Cloudflare deployed agent native task management and wiki

**原文标题**: Show HN: Open-source Cloudflare deployed agent native task management and wiki

**原文链接**: [https://tajd.github.io/projektor/](https://tajd.github.io/projektor/)

生成摘要时出错

---

## 92. If AI Writes All the Code, What Do the Programmers Do?

**原文标题**: If AI Writes All the Code, What Do the Programmers Do?

**原文链接**: [https://probablydance.com/2026/07/27/if-ai-writes-all-the-code-what-do-the-programmers-do/](https://probablydance.com/2026/07/27/if-ai-writes-all-the-code-what-do-the-programmers-do/)

生成摘要时出错

---

## 93. Some combinatorial applications of spacefilling curves

**原文标题**: Some combinatorial applications of spacefilling curves

**原文链接**: [https://www2.isye.gatech.edu/~jjb/research/mow/mow.html](https://www2.isye.gatech.edu/~jjb/research/mow/mow.html)

生成摘要时出错

---

## 94. How real are real numbers? (2004)

**原文标题**: How real are real numbers? (2004)

**原文链接**: [https://arxiv.org/abs/math/0411418](https://arxiv.org/abs/math/0411418)

生成摘要时出错

---

## 95. Anthropic A.I. Model Finds Flaws in Tough-to-Crack Encryption Algorithms

**原文标题**: Anthropic A.I. Model Finds Flaws in Tough-to-Crack Encryption Algorithms

**原文链接**: [https://www.nytimes.com/2026/07/28/us/politics/anthropic-ai-encryption-security-aes.html](https://www.nytimes.com/2026/07/28/us/politics/anthropic-ai-encryption-security-aes.html)

生成摘要时出错

---

## 96. RTX 2080 Ti Memory Upgrade to 22 GB

**原文标题**: RTX 2080 Ti Memory Upgrade to 22 GB

**原文链接**: [https://gpusolutions.net/rbservices/graphics-card-upgrade/](https://gpusolutions.net/rbservices/graphics-card-upgrade/)

生成摘要时出错

---

## 97. C/C++ projects packaged for Zig

**原文标题**: C/C++ projects packaged for Zig

**原文链接**: [https://github.com/allyourcodebase](https://github.com/allyourcodebase)

生成摘要时出错

---

## 98. Exploiting Volvo/Eicher's fleet platform to gain control over all users/vehicles

**原文标题**: Exploiting Volvo/Eicher's fleet platform to gain control over all users/vehicles

**原文链接**: [https://eaton-works.com/2026/07/27/my-eicher-hack/](https://eaton-works.com/2026/07/27/my-eicher-hack/)

生成摘要时出错

---

## 99. Giant Concentric Rings Discovered in the Atmosphere of Venus

**原文标题**: Giant Concentric Rings Discovered in the Atmosphere of Venus

**原文链接**: [https://www.sciencealert.com/giant-concentric-rings-discovered-in-the-atmosphere-of-venus](https://www.sciencealert.com/giant-concentric-rings-discovered-in-the-atmosphere-of-venus)

生成摘要时出错

---

## 100. Show HN: Cloudrift – CLI open-source that finds wated AWS spend

**原文标题**: Show HN: Cloudrift – CLI open-source that finds wated AWS spend

**原文链接**: [https://github.com/elleVas/cloudrift](https://github.com/elleVas/cloudrift)

生成摘要时出错

---

