# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-15.md)

*最后自动更新时间: 2026-10-15 20:38:11*
## 1. 缪斯火花公开赛

**原文标题**: Muse Spark Open

**原文链接**: [https://research.meta.ai/blog/muse-spark-open](https://research.meta.ai/blog/muse-spark-open)

**Muse Spark Open** 是一款最新发布的原生多模态开源权重模型，专为高级智能体任务、复杂软件工程和长程推理而设计。该模型拥有 **8160 亿总参数（420 亿激活参数）**和 **100 万令牌（1M-token）上下文窗口**，被定位为迄今为止功能最强大的美国开源权重模型。

其一大亮点是针对桌面端使用的优化。通过利用 **MLX 框架**，该模型可以在双 **Apple M5 Ultra Mac Studio** 配置上运行，凭借 1.2 TB/s 的内存带宽发挥个人超级计算机的效能。它还针对 NVIDIA、AMD 和 Intel 芯片进行了高度优化，其定制的 Helion GPU 内核可在企业级硬件上实现显著的加速。

本次发布的关键亮点包括：
*   **性能：** 在复杂工作流中展现了卓越实力，例如交付 iOS 应用代码以及在 DaVinci Resolve 中进行逐帧视频分析。
*   **可访问性：** 模型权重可通过 **Hugging Face**、Amazon SageMaker 和 Microsoft Foundry 获取。API 访问由 **Groq、Together AI、Fireworks AI 和 OpenRouter** 等合作伙伴提供。
*   **定制化：** 开发者可以使用 PyTorch 和 TorchTitan 对模型进行微调。
*   **安全与许可：** 该模型在 Meta 超智能扩展框架下经过了严格的安全测试。它根据 **Muse 模型许可证** 发布，其中包括有限的商业条款，以支持广泛的开发者使用。

通过将“个人超智能”引入桌面，Muse Spark Open 旨在为个人开发者和企业研究人员普及顶尖的 AI 能力。

---

## 2. 神经网络很干净

**原文标题**: Neural networks are clean

**原文链接**: [https://already-clean.goodfire.com/](https://already-clean.goodfire.com/)

在《神经网络是整洁的》（Neural networks are clean）一文中，作者指出神经网络的内部机制是由清晰可辨的构建模块组成的，这使得机理可解释性（mechanistic interpretability）远比此前担心的更容易实现。该领域过去认为，网络利用“叠加”（superposition）将不相关的概念打包进单个神经元，从而产生不可解释的“乱麻”。然而，作者认为这其实是对**“递归泛化”**（recursive generalization）的误解——即神经元以分形、层级化的方式将相关概念分组（例如，代表“diy”的神经元是从代表“iy”的神经元中生长出来的）。

核心发现包括：

*   **规模下的可读性：** 早期在 InceptionV1 等模型中发现的多义性证据，实际上源于架构缺陷和工具匮乏。相比之下，现代模型具有高度的可解释性；对 Qwen3-32B 等模型的审计表明，90–97% 的神经元都承担着单一的主要职责。
*   **规模优势：** 模型越大实际上越容易解释，因为它们学习的是更狭窄、更特定的神经元，而不是将不相关的概念折叠在一起。
*   **直接研究 vs. 重构：** 作者提倡开展“快速的常规科学”，即直接研究网络的神经元和电路，而非通过训练稀疏自编码器等二次模型来“拆解”网络。
*   **填字游戏效应：** 随着网络地图被不断绘制，可解释性研究会产生动量。一旦“地图”开始完善，周围的神经元和电路就能提供上下文，使剩余部分的破译变得更加容易。

最终，文章表明，由于神经网络天生具有结构化和分形特征，理解其完整内部逻辑的前景是乐观的。它们并非随意的乱麻，而是可以通过直接观察和改进工具来解码的整洁系统。

---

## 3. E Ink 发布最新一代彩色电子纸平台 E Ink Kaleido 4

**原文标题**: E Ink Launches Latest Version of Color EPaper Platform, E Ink Kaleido 4

**原文链接**: [https://www.eink.com/news/detail/EInk-Launches-Latest-Version-of-Color-ePaper-Platform-E-Ink-Kaleido-4](https://www.eink.com/news/detail/EInk-Launches-Latest-Version-of-Color-ePaper-Platform-E-Ink-Kaleido-4)

E Ink 元太科技正式发布了最新一代印刷彩色电子纸技术 **E Ink Kaleido 4**。该平台旨在提升数字阅读与书写体验，与前代产品 Kaleido 3 相比，在视觉质量、响应速度和用眼舒适度方面均有显著提升。

**主要特性与改进包括：**

*   **色彩表现增强：** Kaleido 4 的**色彩亮度提升了 50%**，**色彩饱和度提升了 30%**。这些升级带来了更鲜艳的图像和更清晰的文字，使显示质量更接近传统彩色印刷。
*   **卓越的响应速度：** 新平台拥有更快的刷新率和更新速度。这些进步使该技术更适用于互动应用，如电子纸手写本（eNotes）和更平滑的翻页体验。
*   **眼部健康与舒适：** 该技术集成了 **E Ink ComfortGaze™** 护眼前光技术，可减少蓝光输出。这确保了更舒适的长期阅读体验，并最大程度地降低了对用户睡眠模式的影响。
*   **技术通用性：** Kaleido 4 支持 4,096 色和 16 级灰度，同时延续了 E Ink 显示屏超低功耗和阳光下清晰可读的特性。此外，它还改进了对细腻细节和纹理的呈现。

E Ink 元太科技董事长李政昊强调，Kaleido 4 代表了彩色电子纸技术的一个重要里程碑，旨在为电子阅读器和电子手写本市场提供更丰富、更具沉浸感的体验。预计全球制造商将在即将推出的针对教育、专业办公和数字阅读的设备中采用这一技术。

---

## 4. Wayland desktop for Linux with skeuomorphic design

**原文标题**: Wayland desktop for Linux with skeuomorphic design

**原文链接**: [https://github.com/fyzugx/DEsk](https://github.com/fyzugx/DEsk)

生成摘要时出错

---

## 5. Krea 3 – An image model built for editing at scale

**原文标题**: Krea 3 – An image model built for editing at scale

**原文链接**: [https://www.krea.ai/krea-3](https://www.krea.ai/krea-3)

生成摘要时出错

---

## 6. Celebrating 70 Years of Fortran

**原文标题**: Celebrating 70 Years of Fortran

**原文链接**: [https://fortran-lang.org/news/2026/09-15-Fortran-birthday/](https://fortran-lang.org/news/2026/09-15-Fortran-birthday/)

生成摘要时出错

---

## 7. Why I Wrote PGP (1991, revised 1999)

**原文标题**: Why I Wrote PGP (1991, revised 1999)

**原文链接**: [https://philzimmermann.com/EN/essays/WhyIWrotePGP.html](https://philzimmermann.com/EN/essays/WhyIWrotePGP.html)

生成摘要时出错

---

## 8. The engineering that allows articulated buses to bend

**原文标题**: The engineering that allows articulated buses to bend

**原文链接**: [https://www.theautopian.com/you-wont-believe-the-incredible-engineering-that-allows-articulated-buses-to-bend/](https://www.theautopian.com/you-wont-believe-the-incredible-engineering-that-allows-articulated-buses-to-bend/)

生成摘要时出错

---

## 9. Delta’s Biscoff cookies were supposed to be temporary

**原文标题**: Delta’s Biscoff cookies were supposed to be temporary

**原文链接**: [https://www.seriouseats.com/biscoff-history-12168161](https://www.seriouseats.com/biscoff-history-12168161)

生成摘要时出错

---

## 10. Libreboot 26.10 "Ominous Olive" released with UEFI, Chromebook support

**原文标题**: Libreboot 26.10 "Ominous Olive" released with UEFI, Chromebook support

**原文链接**: [https://libreboot.org/news/libreboot2610.html](https://libreboot.org/news/libreboot2610.html)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 2 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 3 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 4 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 5 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 6 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 7 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 8 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 9 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 10 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 11 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 12 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 13 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 14 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 15 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 16 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 17 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 18 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 19 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 20 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 21 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 22 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 23 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 24 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 25 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 26 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 27 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 28 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 29 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 30 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 31 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 32 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 33 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 34 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 35 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 36 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 37 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 38 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 39 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 40 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 41 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 42 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 43 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 44 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 45 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 46 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 47 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 48 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 49 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 50 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 51 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 52 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 53 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 54 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 55 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 56 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 57 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 58 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 59 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 60 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 61 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 62 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 63 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 64 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 65 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 66 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 67 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 68 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 69 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 70 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 71 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 72 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 73 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 74 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 75 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 76 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 77 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 78 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 79 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 80 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 81 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 82 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 83 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 84 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 85 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 86 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 87 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 88 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 89 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 90 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 91 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 92 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 93 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 94 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 95 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 96 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 97 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 98 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 99 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 100 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 101 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 102 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 103 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 104 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 105 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 106 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 107 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 108 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 109 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 110 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 111 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 112 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 113 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 114 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 115 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 116 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 117 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 118 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 119 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 120 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 121 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 122 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 123 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 124 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 125 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 126 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 127 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 128 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 129 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 130 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 131 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 132 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 133 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 134 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 135 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 136 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 137 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 138 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 139 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 140 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 141 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 142 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 143 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 144 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 145 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 146 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 147 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 148 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 149 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 150 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 151 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 152 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 153 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 154 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 155 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 156 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 157 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 158 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 159 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 160 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 161 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 162 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 163 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 164 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 165 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 166 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 167 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 168 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 169 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 170 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 171 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 172 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 173 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 174 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 175 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 176 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 177 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 178 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 179 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 180 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 181 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 182 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 183 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 184 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 185 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 186 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 187 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 188 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 189 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 190 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 191 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 192 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 193 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 194 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 195 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 196 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 197 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 198 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 199 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 200 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 201 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 202 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 203 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 204 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 205 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 206 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 207 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 208 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 209 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 210 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 211 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 212 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 213 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 214 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 215 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 216 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 217 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 218 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 219 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 220 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 221 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 222 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 223 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 224 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 225 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 226 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 227 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 228 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 229 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 230 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 231 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 232 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 233 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 234 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 235 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 236 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 237 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 238 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 239 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 240 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 241 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 242 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 243 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 244 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 245 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 246 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 247 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 248 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 249 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 250 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 251 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 252 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 253 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 254 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 255 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 256 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 257 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 258 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 259 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 260 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 261 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 262 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 263 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 264 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 265 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 266 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 267 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 268 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 269 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 270 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 271 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 272 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 273 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 274 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 275 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 276 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 277 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 278 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 279 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 280 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 281 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 282 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 283 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 284 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 285 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 286 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 287 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 288 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 289 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 290 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 291 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 292 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 293 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 294 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 295 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 296 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 297 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 298 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 299 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 300 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 301 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 302 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 303 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 304 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 305 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 306 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 307 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 308 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 309 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 310 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 311 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 312 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 313 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 314 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 315 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 316 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 317 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 318 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 319 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 320 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 321 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 322 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 323 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 324 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 325 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 326 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 327 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 328 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 329 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 330 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 331 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 332 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 333 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 334 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 335 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 336 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 337 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 338 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 339 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 340 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 341 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 342 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 343 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 344 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 345 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 346 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 347 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 348 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 349 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 350 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 351 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 352 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 353 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 354 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 355 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 356 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 357 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 358 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 359 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 360 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 361 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 362 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 363 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 364 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 365 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 366 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 367 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 368 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 369 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 370 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 371 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 372 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 373 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 374 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 375 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 376 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 377 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 378 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 379 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 380 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 381 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 382 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 383 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 384 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 385 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 386 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 387 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 388 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 389 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 390 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 391 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 392 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 393 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 394 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 395 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 396 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 397 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 398 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 399 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 400 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 401 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 402 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 403 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 404 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 405 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 406 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 407 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 408 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 409 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 410 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 411 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 412 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 413 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 414 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 415 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 416 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 417 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 418 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 419 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 420 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 421 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 422 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 423 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 424 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 425 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 426 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 427 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 428 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 429 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 430 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 431 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 432 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 433 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 434 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 435 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 436 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 437 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 438 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 439 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 440 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 441 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 442 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 443 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 444 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 445 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 446 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 447 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 448 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 449 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 450 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 451 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 452 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 453 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 454 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 455 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 456 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 457 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 458 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 459 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 460 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 461 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 462 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 463 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 464 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 465 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 466 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 467 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 468 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 469 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 470 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 471 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 472 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 473 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 474 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 475 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 476 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 477 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 478 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 479 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 480 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 481 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 482 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 483 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 484 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 485 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 486 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 487 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 488 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 489 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 490 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 491 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 492 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 493 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 494 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 495 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 496 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 497 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 498 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 499 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 500 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 501 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 502 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 503 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 504 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 505 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 506 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 507 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 508 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 509 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 510 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 511 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 512 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 513 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 514 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 515 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 516 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 517 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 518 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 519 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 520 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 521 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 522 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 523 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 524 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 525 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 526 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 527 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 528 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 529 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 530 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 531 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 532 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 533 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 534 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 535 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 536 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 537 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 538 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 539 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 540 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 541 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 542 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 543 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 544 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 545 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 546 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 547 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 548 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 549 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 550 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 551 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 552 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 553 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 554 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 555 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 556 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 557 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 558 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 559 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 560 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 561 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 562 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 563 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 564 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 565 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 566 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 567 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 568 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 569 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 570 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 571 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 572 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
