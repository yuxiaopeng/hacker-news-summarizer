# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-25.md)

*最后自动更新时间: 2026-08-25 18:06:19*
## 1. 苹果推出 M6 和 M5 Ultra，性能与 AI 算力实现重大飞跃

**原文标题**: Apple introduces M6 and M5 Ultra for a big leap in performance and AI compute

**原文链接**: [https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/](https://www.apple.com/newsroom/2026/08/apple-introduces-m6-and-m5-ultra-for-a-big-leap-in-performance-and-ai-compute/)

苹果发布了 M6 和 M5 Ultra 芯片，标志着性能和以 AI 为中心的计算迈出了重要一步。M6 芯片在新款 Mac mini 中首发，而 M5 Ultra 则助力更新后的 Mac Studio。

**M6 芯片**
作为苹果首款 **2 纳米芯片**，M6 拥有 12 核中央处理器（包括全新的“超大核”）和 12 核图形处理器。它专为能效和日常 AI 任务设计，引入了**双 16 核神经网络引擎**，其峰值算力较前代翻倍。此外，每个图形处理器核心现在都包含一个**神经加速器**，使 AI 性能比 M5 提升了 30%。该芯片支持高达 32GB 的统一内存，带宽达 170GB/s。

**M5 Ultra**
M5 Ultra 是苹果迄今为止最强大的处理器，采用了首创的**四芯架构**。通过 UltraFusion 技术将两颗双芯 M5 Max 芯片互连，它实现了最高 36 核中央处理器和最高 80 核图形处理器。它提供了惊人的 **1.2TB/s 统一内存带宽**，并支持高达 **512GB 内存**，让专业人士能够完全在设备端运行拥有数千亿参数的大语言模型（LLM）。在第三代光线追踪技术的支持下，其图形性能比 M3 Ultra 快 40%。

**核心特性与开发者影响**
*   **聚焦 AI：** 两款芯片均针对“智能体”AI 和私密设备端处理进行了优化。
*   **能效比：** 转向 2 纳米工艺（针对 M6）和先进的着色器架构，确保了行业领先的每瓦性能。
*   **开发者工具：** 苹果的框架（Core ML、Metal、Xcode）已更新，可自动利用双神经网络引擎和图形处理器加速器，从而实现更快的模型执行。

这些产品的发布代表了向高容量、本地 AI 计算的战略转型，使研究人员和创作者无需依赖云端处理，即可处理“前沿”AI 模型和复杂的 3D 工作流。

---

## 2. 搭载 M5 Max 和 M5 Ultra 的新款 Mac Studio

**原文标题**: New Mac Studio with M5 Max and M5 Ultra

**原文链接**: [https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/](https://www.apple.com/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/)

苹果发布了新款 Mac Studio，搭载 M5 Max 和 M5 Ultra 芯片，定位为端侧 AI 与高端专业工作流的突破性台式机。该产品于 2026 年 8 月 25 日发布，性能实现巨大飞跃，与前代产品相比，其 AI 计算速度提升高达 4.3 倍，图形性能提升 1.8 倍。

**核心硬件规格：**
*   **M5 Max：** 配备 18 核 CPU、最高 40 核 GPU 以及 128GB 统一内存。
*   **M5 Ultra：** 配备最高 36 核 CPU、80 核 GPU 以及惊人的 **512GB 统一内存**。
*   **神经网络加速器：** 苹果首次将神经网络加速器直接集成到每个 GPU 核心中，以加速矩阵乘法和大型语言模型（LLM）的处理。
*   **连接性：** 该设备引入了 **Wi-Fi 7、蓝牙 6 和雷雳 5**。全新的集群功能支持通过雷雳 5 连接多台 Mac Studio 进行分布式 AI 推理，使性能提升至三倍。

**性能与软件：**
Mac Studio 采用 PCIe Gen 6 架构，存储速度提升 2 倍。它支持多达八台显示器，并引入了基于 USB-C 的“三级同步”（genlock）功能，用于专业视频同步。系统运行 **macOS 27 (Golden Gate)**，搭载新一代 **Siri AI** 和“Apple 智能”，允许用户在完全保护隐私的前提下在本地运行大规模前沿级 AI 模型。

**价格与上市时间：**
*   **M5 Max 机型：** 起售价 **2,499 美元**。
*   **M5 Ultra 机型：** 起售价 **5,499 美元**。
*   **上市时间：** 2026 年 8 月 25 日开启预订，**9 月 22 日**正式发售。512GB 内存配置版本将于 10 月下旬发货。

外观设计依然保持紧凑且静音，同时使用了 35% 的再生材料，助力苹果实现 2030 年碳中和目标。

---

## 3. Nitter 项目收到停止并终止函

**原文标题**: Nitter project received cease and desist

**原文链接**: [https://github.com/zedeus/nitter/issues/1442](https://github.com/zedeus/nitter/issues/1442)

据报道，广受欢迎的Twitter（现更名为X）开源替代前端项目Nitter已收到停止并终止函。根据用户AlexandrPutenikhin于2026年8月25日提交的GitHub议题（#1442），所有公开的Nitter实例均已停止运作。

在这些实例中，报告的主要技术症状为“速率限制”（rate limited）错误，导致用户无法通过该服务访问内容。此次停运似乎是全面性的，连同twiiit.com等知名聚合平台也受到了影响。

这一进展对该项目构成了沉重打击。Nitter的设计初衷是允许用户在无需JavaScript或追踪的情况下私密地浏览Twitter。这份“停止并终止函”暗示了正式法律行动的升级，推测极有可能来自X Corp，旨在取缔绕过其官方界面和广告系统的第三方前端。

---

## 4. 炸鱼活动正严重破坏印度尼西亚的珊瑚礁。

**原文标题**: Bomb fishing is wreaking havoc on Indonesia's coral reefs

**原文链接**: [https://e360.yale.edu/digest/bomb-fishing-coral-reefs](https://e360.yale.edu/digest/bomb-fishing-coral-reefs)

印度尼西亚的“珊瑚大三角”正因非法炸鱼而面临严重的生态危机。伦敦动物学会与哈桑丁大学的一项研究显示，斯佩尔蒙德群岛的渔民每年引爆超过8500枚水下炸弹——大约每62分钟就有一枚。这种行径每年摧毁相当于三个足球场面积的珊瑚礁，将充满生机的生态系统变成了荒芜的碎石堆。

炸鱼涉及使用装满炸药的塑料瓶，在90英尺半径范围内无差别地杀鱼。除了直接屠杀海洋生物，由此造成的物理破坏还阻碍了珊瑚再生，导致该地区自1990年以来损失了75%的珊瑚。虽然这种行为常被归因于贫困，但专家指出，设备成本表明其主要由中等收入渔民驱动，并因印尼广阔海洋保护区内执法不力而愈演愈烈。

为了记录破坏规模，研究人员部署了水下麦克风，并利用开源人工智能软件将爆炸声与发动机噪音区分开来。数据显示，炸鱼活动全年都在发生，在早晨达到顶峰，但在当地的礼拜日（周五）有所减少。

然而，恢复仍有希望。首席研究员本·威廉姆斯认为，通过公开人工智能检测代码，当局可以开发实时、GPS同步的传感器网络来拦截渔民。与海洋变暖和白化等全球性挑战不同，炸鱼是一种具有局部解决方案的“急性压力源”。科学家强调，如果停止炸鱼，这些生物多样性丰富的栖息地可以成功恢复健康。

---

## 5. Black hole singularity is a surface not a point

**原文标题**: Black hole singularity is a surface not a point

**原文链接**: [https://arxiv.org/abs/2608.21590](https://arxiv.org/abs/2608.21590)

In the paper "Black hole singularity is a surface not a point," authors Andrew J. S. Hamilton and Tyler McMaken challenge the common misconception that the center of a black hole is an infinitesimal point. Instead, they argue that general relativity dictates the singularity is a spatially extended surface.

The authors support this claim by examining the causal trajectories of observers. In a spherical black hole, two observers entering from different angles do not converge at a single point; rather, they lose causal contact with one another before reaching the singularity. For rotating black holes, the authors posit that the singularity resides at the inner horizon. They explain that even minor classical or quantum perturbations trigger an "exponential mass inflation instability," which precipitates a collapse into a spacelike singular surface.

These findings have significant implications for the field of quantum gravity. Hamilton and McMaken suggest that the quantum states of a black hole are likely located on this effectively two-dimensional singular surface. According to their model, this surface coevolves unitarily and exists in thermodynamic equilibrium with the "hot atmosphere" of trapped Hawking radiation located within the event horizon. By reframing the singularity as a surface, the paper provides a potential path forward for reconciling black hole evolution with the principles of quantum mechanics.

---

## 6. Clara (YC P26) Is Hiring a Growth Engineer to Bring AI Doctors to Market

**原文标题**: Clara (YC P26) Is Hiring a Growth Engineer to Bring AI Doctors to Market

**原文链接**: [https://www.ycombinator.com/companies/clara-2/jobs/8snci6k-founding-full-stack-growth-engineer](https://www.ycombinator.com/companies/clara-2/jobs/8snci6k-founding-full-stack-growth-engineer)

摘要生成出错

---

## 7. New Mac mini, featuring M6 and M5 Pro

**原文标题**: New Mac mini, featuring M6 and M5 Pro

**原文链接**: [https://www.apple.com/newsroom/2026/08/apple-unveils-a-more-powerful-mac-mini-featuring-the-all-new-m6-and-m5-pro/](https://www.apple.com/newsroom/2026/08/apple-unveils-a-more-powerful-mac-mini-featuring-the-all-new-m6-and-m5-pro/)

生成摘要时出错

---

## 8. Qwen 3.8-Flash-Next releasing tomorrow (125B a6B)

**原文标题**: Qwen 3.8-Flash-Next releasing tomorrow (125B a6B)

**原文链接**: [https://modelscope.cn/models/Qwen/Qwen3.8-Flash-Next](https://modelscope.cn/models/Qwen/Qwen3.8-Flash-Next)

生成摘要时出错

---

## 9. Water Behind the Watts: The Hidden Risk of Powering Data Centers

**原文标题**: Water Behind the Watts: The Hidden Risk of Powering Data Centers

**原文链接**: [https://www.ceres.org/resources/reports/water-behind-the-watts-the-hidden-risk-of-powering-data-centers](https://www.ceres.org/resources/reports/water-behind-the-watts-the-hidden-risk-of-powering-data-centers)

生成摘要时出错

---

## 10. My Friend Aaron

**原文标题**: My Friend Aaron

**原文链接**: [https://rorz.io/writing/my-friend-aaron](https://rorz.io/writing/my-friend-aaron)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 2 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 3 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 4 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 5 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 6 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 7 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 8 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 9 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 10 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 11 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 12 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 13 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 14 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 15 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 16 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 17 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 18 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 19 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 20 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 21 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 22 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 23 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 24 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 25 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 26 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 27 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 28 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 29 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 30 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 31 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 32 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 33 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 34 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 35 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 36 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 37 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 38 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 39 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 40 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 41 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 42 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 43 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 44 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 45 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 46 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 47 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 48 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 49 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 50 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 51 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 52 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 53 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 54 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 55 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 56 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 57 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 58 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 59 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 60 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 61 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 62 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 63 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 64 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 65 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 66 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 67 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 68 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 69 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 70 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 71 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 72 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 73 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 74 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 75 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 76 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 77 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 78 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 79 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 80 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 81 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 82 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 83 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 84 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 85 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 86 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 87 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 88 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 89 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 90 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 91 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 92 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 93 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 94 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 95 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 96 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 97 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 98 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 99 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 100 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 101 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 102 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 103 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 104 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 105 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 106 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 107 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 108 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 109 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 110 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 111 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 112 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 113 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 114 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 115 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 116 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 117 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 118 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 119 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 120 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 121 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 122 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 123 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 124 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 125 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 126 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 127 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 128 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 129 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 130 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 131 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 132 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 133 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 134 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 135 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 136 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 137 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 138 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 139 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 140 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 141 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 142 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 143 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 144 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 145 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 146 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 147 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 148 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 149 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 150 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 151 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 152 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 153 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 154 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 155 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 156 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 157 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 158 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 159 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 160 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 161 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 162 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 163 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 164 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 165 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 166 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 167 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 168 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 169 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 170 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 171 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 172 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 173 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 174 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 175 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 176 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 177 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 178 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 179 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 180 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 181 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 182 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 183 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 184 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 185 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 186 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 187 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 188 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 189 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 190 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 191 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 192 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 193 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 194 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 195 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 196 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 197 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 198 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 199 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 200 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 201 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 202 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 203 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 204 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 205 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 206 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 207 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 208 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 209 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 210 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 211 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 212 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 213 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 214 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 215 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 216 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 217 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 218 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 219 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 220 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 221 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 222 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 223 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 224 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 225 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 226 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 227 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 228 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 229 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 230 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 231 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 232 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 233 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 234 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 235 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 236 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 237 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 238 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 239 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 240 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 241 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 242 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 243 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 244 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 245 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 246 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 247 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 248 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 249 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 250 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 251 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 252 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 253 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 254 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 255 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 256 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 257 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 258 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 259 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 260 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 261 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 262 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 263 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 264 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 265 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 266 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 267 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 268 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 269 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 270 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 271 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 272 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 273 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 274 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 275 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 276 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 277 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 278 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 279 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 280 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 281 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 282 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 283 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 284 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 285 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 286 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 287 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 288 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 289 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 290 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 291 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 292 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 293 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 294 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 295 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 296 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 297 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 298 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 299 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 300 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 301 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 302 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 303 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 304 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 305 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 306 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 307 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 308 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 309 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 310 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 311 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 312 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 313 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 314 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 315 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 316 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 317 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 318 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 319 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 320 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 321 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 322 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 323 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 324 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 325 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 326 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 327 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 328 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 329 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 330 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 331 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 332 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 333 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 334 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 335 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 336 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 337 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 338 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 339 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 340 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 341 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 342 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 343 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 344 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 345 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 346 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 347 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 348 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 349 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 350 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 351 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 352 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 353 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 354 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 355 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 356 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 357 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 358 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 359 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 360 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 361 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 362 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 363 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 364 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 365 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 366 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 367 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 368 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 369 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 370 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 371 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 372 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 373 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 374 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 375 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 376 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 377 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 378 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 379 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 380 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 381 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 382 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 383 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 384 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 385 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 386 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 387 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 388 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 389 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 390 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 391 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 392 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 393 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 394 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 395 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 396 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 397 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 398 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 399 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 400 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 401 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 402 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 403 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 404 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 405 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 406 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 407 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 408 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 409 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 410 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 411 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 412 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 413 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 414 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 415 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 416 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 417 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 418 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 419 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 420 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 421 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 422 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 423 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 424 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 425 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 426 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 427 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 428 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 429 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 430 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 431 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 432 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 433 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 434 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 435 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 436 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 437 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 438 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 439 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 440 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 441 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 442 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 443 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 444 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 445 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 446 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 447 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 448 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 449 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 450 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 451 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 452 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 453 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 454 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 455 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 456 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 457 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 458 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 459 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 460 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 461 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 462 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 463 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 464 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 465 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 466 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 467 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 468 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 469 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 470 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 471 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 472 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 473 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 474 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 475 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 476 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 477 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 478 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 479 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 480 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 481 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 482 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 483 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 484 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 485 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 486 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 487 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 488 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 489 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 490 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 491 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 492 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 493 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 494 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 495 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 496 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 497 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 498 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 499 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 500 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 501 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 502 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 503 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 504 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 505 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 506 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 507 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 508 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 509 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 510 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 511 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 512 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 513 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 514 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 515 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 516 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 517 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 518 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 519 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 520 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 521 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 522 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
