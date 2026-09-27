# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-27.md)

*最后自动更新时间: 2026-09-27 20:28:06*
## 1. Ember-1

**原文标题**: Ember-1

**原文链接**: [https://fireworks.ai/blog/ember-1](https://fireworks.ai/blog/ember-1)

Fireworks Research 推出了 **Ember-1**，这是一款专门设计的模型，旨在提供与 Kimi K3 相当的高质量性能，同时减少约 40% 的 Token 使用量。该模型解决了现代推理模型的低效问题——这类模型往往将超过 90% 的输出用于内部推理，这一过程在多轮智能体工作流中成本极其高昂。

通过在 Fireworks Serverless 训练平台上进行的 50 多次训练实验，Ember-1 学会了在不牺牲准确性的情况下消除冗余推理和无效循环。其性能亮点包括：

*   **基准测试优势：** Ember-1 在“Bedside Bench”（一项经医生验证的临床指标）上设定了新的帕累托前沿，在单次任务成本基础上，其表现优于或媲美 GPT-6 Astra 和 Claude Opus 5 等模型。
*   **成本效率：** 在 SWE-bench 和 DeepSWE 等行业基准测试中，Ember-1 在达到 K3-max 质量的同时显著降低了 Token 支出，证明其比单纯降低基础 K3 模型的推理强度更有效。
*   **现实世界验证：** 在生产编程工作流的实时 A/B 测试中，单个任务的 Token 使用量减少了 35%，且质量无损。Fireworks 的内部测试过程非常平滑，开发人员甚至没有察觉到从基础模型的切换。

Ember-1 目前作为**研究预览版**在 Fireworks Serverless 上提供。为了支持进一步优化，Fireworks 还推出了训练支持，允许企业利用自有数据构建定制化、高 Token 效率的 Ember-1 版本。此次发布标志着 Fireworks Research 系列专用模型的开端，旨在最大限度地提高模型效率并降低开发者成本。

---

## 2. 2026 年 Rust SIMD 现状

**原文标题**: The state of SIMD in Rust in 2026

**原文链接**: [https://shnatsel.github.io/state-of-simd-rust-2026/](https://shnatsel.github.io/state-of-simd-rust-2026/)

本文由 **Fearless SIMD** 库的维护者撰写，全面概述了截至 2026 年的 Rust SIMD（单指令多数据）生态系统。SIMD 通过在单个时钟周期内处理成批数据，可实现高达 64 倍的显著性能提升，但硬件碎片化（尤其是 x86 架构）使实现变得极具挑战性。

作者指出了在 Rust 中使用 SIMD 的三种主要方式：

1.  **自动向量化：** 依赖编译器的启发式算法。虽然这种方式最简单，但通常并不可靠，且可能需要特定的提示，或使用代数运算（在 Rust 1.98 中稳定）来处理浮点数学。
2.  **`multiversion` Crate：** 适用于运行时 CPU 特性检测，但对于极小的函数会引入微小的开销。
3.  **可移植抽象：** 目前有多个库提供跨平台 SIMD 支持：
    *   **std::simd：** 仅限 nightly 版本的标准库基础。它非常灵活，但缺乏三角函数等高级数学运算，且严重依赖 LLVM 的内部能力。
    *   **fearless_simd：** 被描述为一个安全的“全能”解决方案，可自动处理复杂的多版本分发（包括智能 AVX-512 调度），但需要特定的样板代码。
    *   **wide：** 一个稳定的 v1.0 选项，易于使用，但缺乏高效的多版本分发和泛型支持。
    *   **pulp & macerator：** 为线性代数 (`faer`) 和 AI (`burn`) 构建的专用库。`macerator` 特别支持 `f16` 和龙芯架构 (LoongArch)，但缺乏文档。

核心挑战仍然是**多版本分发 (multiversioning)**：即通过在运行时检查 AVX2 或 AVX-512 等特性，确保二进制文件可以在各种 x86 CPU 上运行。虽然 ARM 和 WebAssembly 的 SIMD 规范更加统一，但 x86 开发者必须选择一个能在安全性、易用性和硬件优化之间取得平衡的库。

---

## 3. FM合成发明者约翰·钱宁口述历史 [视频]

**原文标题**: Oral history of John Chowning, inventor of FM synthesis [video]

**原文链接**: [https://www.youtube.com/watch?v=e1Xn3030IvM](https://www.youtube.com/watch?v=e1Xn3030IvM)

虽然所提供的文本仅包含 YouTube 的通用站点元数据和法律样板文字，但标题指向的是**约翰·乔宁**（John Chowning）的口述历史。他是电子音乐和数字合成史上的开创性人物。

**关键信息与背景：**

约翰·乔宁是一位美国作曲家、音乐家，也是斯坦福大学的名誉教授。他最著名的成就是在 1967 年发现了**频率调制（FM）合成**算法。这一突破使得利用比以往方法低得多的计算能力，就能创造出复杂的、不断变化的数字声音——其范围涵盖了从逼真的铜管乐和铃声到全新的音色纹理。

**乔宁成就核心：**

*   **技术发现：** 在进行高速颤音实验时，乔宁意识到快速调制会产生复杂的边带，从而产生丰富的音色。这与当时主流的加法合成方法完全不同。
*   **斯坦福大学与 CCRMA：** 乔宁在斯坦福大学创立了音乐与声学计算机研究中心（CCRMA），该中心随后成为了全球领先的数字音频研究枢纽。
*   **商业成功：** 斯坦福大学将 FM 技术授权给了**雅马哈**（Yamaha）。这一合作促成了 1983 年 **Yamaha DX7** 的发布，它是史上最畅销的合成器之一。DX7 定义了“80 年代之声”，出现在无数流行金曲中。
*   **经济影响：** FM 合成专利成为斯坦福大学历史上最赚钱的专利之一，产生了约 2000 万美元的版税收入，并为后续的音乐创新提供了资金支持。

这段口述历史通常涵盖了乔宁的早期生活、他为争取学术界重视计算机音乐而付出的努力、他在技术发现上的机缘巧合，以及 FM 合成对音乐产业和数字信号处理领域的深远影响。

---

## 4. 在一间80美元的汽车旅馆房间里，一项发现揭示了生命起源的奥秘。

**原文标题**: In an $80 motel room, a discovery to shed light on the origins of life

**原文链接**: [https://www.nytimes.com/2026/09/26/science/motel-science-discovery.html](https://www.nytimes.com/2026/09/26/science/motel-science-discovery.html)

无法访问文章链接。

---

## 5. Show HN: Lofi Cities – Pixel-art city nights with browser-generated lofi

**原文标题**: Show HN: Lofi Cities – Pixel-art city nights with browser-generated lofi

**原文链接**: [https://loficities.com/](https://loficities.com/)

生成摘要时出错

---

## 6. Alan Kay's answer to "Did the ENIAC have a BIOS"?

**原文标题**: Alan Kay's answer to "Did the ENIAC have a BIOS"?

**原文链接**: [https://www.quora.com/Did-the-ENIAC-have-a-BIOS/answer/Alan-Kay-11](https://www.quora.com/Did-the-ENIAC-have-a-BIOS/answer/Alan-Kay-11)

生成摘要时出错

---

## 7. Writing Efficient C++ Code (2013)

**原文标题**: Writing Efficient C++ Code (2013)

**原文链接**: [https://asawicki.info/articles/writing_efficient_cpp_code.php](https://asawicki.info/articles/writing_efficient_cpp_code.php)

生成摘要时出错

---

## 8. Imp is a full port of DSPy to the BEAM

**原文标题**: Imp is a full port of DSPy to the BEAM

**原文链接**: [https://github.com/deepfates/imp](https://github.com/deepfates/imp)

生成摘要时出错

---

## 9. 更换充电式自行车灯的旧电池

**原文标题**: Replacing the old battery on rechargeable bike lights

**原文链接**: [https://jvns.ca/blog/2026/09/27/replacing-the-old-battery-on-rechargeable-bike-lights/](https://jvns.ca/blog/2026/09/27/replacing-the-old-battery-on-rechargeable-bike-lights/)

生成摘要时出错

---

## 10. Show HN: TinyAIArena watch AI agents battle it out

**原文标题**: Show HN: TinyAIArena watch AI agents battle it out

**原文链接**: [https://tinyaiarena.com/](https://tinyaiarena.com/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 2 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 3 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 4 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 5 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 6 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 7 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 8 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 9 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 10 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 11 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 12 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 13 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 14 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 15 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 16 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 17 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 18 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 19 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 20 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 21 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 22 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 23 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 24 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 25 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 26 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 27 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 28 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 29 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 30 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 31 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 32 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 33 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 34 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 35 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 36 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 37 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 38 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 39 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 40 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 41 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 42 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 43 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 44 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 45 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 46 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 47 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 48 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 49 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 50 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 51 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 52 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 53 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 54 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 55 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 56 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 57 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 58 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 59 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 60 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 61 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 62 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 63 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 64 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 65 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 66 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 67 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 68 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 69 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 70 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 71 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 72 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 73 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 74 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 75 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 76 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 77 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 78 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 79 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 80 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 81 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 82 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 83 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 84 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 85 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 86 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 87 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 88 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 89 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 90 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 91 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 92 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 93 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 94 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 95 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 96 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 97 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 98 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 99 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 100 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 101 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 102 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 103 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 104 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 105 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 106 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 107 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 108 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 109 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 110 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 111 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 112 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 113 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 114 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 115 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 116 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 117 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 118 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 119 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 120 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 121 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 122 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 123 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 124 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 125 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 126 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 127 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 128 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 129 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 130 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 131 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 132 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 133 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 134 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 135 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 136 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 137 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 138 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 139 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 140 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 141 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 142 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 143 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 144 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 145 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 146 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 147 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 148 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 149 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 150 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 151 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 152 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 153 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 154 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 155 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 156 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 157 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 158 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 159 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 160 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 161 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 162 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 163 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 164 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 165 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 166 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 167 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 168 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 169 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 170 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 171 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 172 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 173 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 174 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 175 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 176 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 177 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 178 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 179 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 180 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 181 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 182 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 183 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 184 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 185 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 186 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 187 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 188 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 189 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 190 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 191 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 192 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 193 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 194 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 195 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 196 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 197 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 198 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 199 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 200 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 201 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 202 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 203 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 204 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 205 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 206 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 207 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 208 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 209 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 210 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 211 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 212 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 213 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 214 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 215 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 216 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 217 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 218 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 219 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 220 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 221 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 222 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 223 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 224 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 225 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 226 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 227 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 228 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 229 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 230 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 231 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 232 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 233 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 234 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 235 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 236 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 237 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 238 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 239 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 240 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 241 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 242 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 243 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 244 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 245 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 246 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 247 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 248 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 249 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 250 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 251 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 252 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 253 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 254 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 255 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 256 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 257 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 258 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 259 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 260 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 261 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 262 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 263 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 264 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 265 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 266 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 267 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 268 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 269 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 270 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 271 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 272 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 273 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 274 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 275 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 276 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 277 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 278 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 279 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 280 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 281 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 282 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 283 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 284 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 285 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 286 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 287 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 288 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 289 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 290 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 291 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 292 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 293 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 294 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 295 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 296 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 297 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 298 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 299 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 300 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 301 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 302 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 303 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 304 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 305 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 306 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 307 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 308 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 309 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 310 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 311 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 312 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 313 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 314 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 315 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 316 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 317 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 318 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 319 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 320 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 321 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 322 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 323 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 324 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 325 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 326 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 327 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 328 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 329 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 330 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 331 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 332 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 333 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 334 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 335 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 336 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 337 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 338 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 339 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 340 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 341 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 342 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 343 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 344 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 345 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 346 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 347 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 348 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 349 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 350 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 351 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 352 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 353 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 354 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 355 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 356 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 357 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 358 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 359 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 360 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 361 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 362 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 363 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 364 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 365 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 366 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 367 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 368 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 369 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 370 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 371 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 372 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 373 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 374 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 375 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 376 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 377 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 378 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 379 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 380 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 381 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 382 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 383 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 384 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 385 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 386 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 387 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 388 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 389 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 390 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 391 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 392 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 393 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 394 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 395 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 396 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 397 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 398 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 399 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 400 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 401 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 402 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 403 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 404 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 405 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 406 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 407 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 408 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 409 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 410 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 411 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 412 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 413 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 414 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 415 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 416 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 417 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 418 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 419 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 420 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 421 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 422 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 423 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 424 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 425 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 426 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 427 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 428 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 429 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 430 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 431 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 432 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 433 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 434 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 435 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 436 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 437 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 438 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 439 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 440 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 441 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 442 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 443 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 444 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 445 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 446 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 447 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 448 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 449 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 450 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 451 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 452 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 453 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 454 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 455 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 456 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 457 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 458 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 459 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 460 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 461 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 462 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 463 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 464 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 465 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 466 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 467 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 468 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 469 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 470 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 471 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 472 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 473 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 474 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 475 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 476 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 477 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 478 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 479 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 480 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 481 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 482 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 483 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 484 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 485 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 486 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 487 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 488 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 489 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 490 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 491 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 492 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 493 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 494 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 495 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 496 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 497 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 498 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 499 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 500 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 501 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 502 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 503 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 504 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 505 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 506 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 507 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 508 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 509 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 510 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 511 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 512 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 513 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 514 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 515 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 516 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 517 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 518 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 519 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 520 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 521 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 522 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 523 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 524 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 525 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 526 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 527 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 528 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 529 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 530 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 531 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 532 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 533 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 534 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 535 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 536 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 537 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 538 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 539 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 540 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 541 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 542 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 543 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 544 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 545 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 546 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 547 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 548 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 549 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 550 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 551 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 552 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 553 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 554 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
