# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-25.md)

*最后自动更新时间: 2025-11-25 17:52:18*
## 1. Apt Rust 需求引发质疑

**原文标题**: Apt Rust requirement raises questions

**原文链接**: [https://lwn.net/SubscriberLink/1046841/5bbf1fc049a18947/](https://lwn.net/SubscriberLink/1046841/5bbf1fc049a18947/)

LWN.net文章探讨Debian的APT可能于2026年要求使用Rust引发的争议。APT维护者Julian Andres Klode宣布了这项计划，理由是使用Rust重写APT的部分（特别是.deb、.ar、.tar解析和HTTP签名验证）可以带来内存安全和改进的单元测试。

此决定引发了争论，因为它会影响缺乏Rust工具链的Debian移植版本，可能迫使它们获取工具链、放弃移植或继续使用旧版APT。虽然一些开发者欢迎转向Rust等现代技术，但另一些开发者批评Klode的沟通方式以及缺乏事先讨论。

提出的主要问题包括：志愿者维护者支持Rust的负担、Rust软件包的静态链接特性对Debian基础设施的影响，导致潜在的安全支持限制，以及Debian在管理Rust依赖项和跟踪CVE方面面临的现有挑战。

David Kalnischkies建议完全从APT中删除有问题的代码，因为它主要由Canonical的Launchpad软件使用。有些人担心此更改违背了Debian支持多样化硬件和民主治理的价值观，因为这是一个由单个开发者推动的，缺乏足够的社区投入的决定。

讨论还涉及潜在的解决方案，例如Fork APT、创建Rust到C的转换器或为现有的Rust编译器做出贡献。 争论还扩展到静态库与共享库的更大问题，一些人主张使用依赖项更新重建软件包，而另一些人则更喜欢使用共享库以便于维护。

---

## 2. FLUX.2：前沿视觉智能

**原文标题**: FLUX.2: Frontier Visual Intelligence

**原文链接**: [https://bfl.ai/blog/flux-2](https://bfl.ai/blog/flux-2)

FLUX.2：Black Forest Labs最新视觉智能模型，专为真实创意工作流程设计，提供高质量图像生成，具备跨多重参考一致性、结构化提示遵循和高级文本处理能力。它能在保留细节的同时编辑高达 4 百万像素的图像。

Black Forest Labs强调开放式创新，将FLUX.1（流行的开放图像模型）等开放模型与FLUX.1 Kontext等专业级模型相结合。这种开放核心方法旨在推动实验、审查并降低成本。

FLUX.2相比FLUX.1有显著改进，包括多重参考支持（最多10张图像）、图像细节和照片级真实感提升、可靠的文本渲染、增强的提示遵循、改进的世界知识和更高的分辨率输出。

FLUX.2系列包括FLUX.2 [pro]（最先进的质量）、FLUX.2 [flex]（完全参数控制）、FLUX.2 [dev]（32B开放权重模型）和FLUX.2 [klein]（即将推出的开源模型）。一种新的变分自编码器(VAE)为所有FLUX.2模型提供支持，优化可学习性、质量和压缩。

FLUX.2采用潜在流匹配架构，将视觉-语言模型与修正流Transformer相结合。这实现了多重参考支持、更高分辨率、更好的提示遵循和改进的排版。

Black Forest Labs致力于这些模型的负责任开发，并寻求构建视觉智能的基础设施，目标是实现统一感知、生成、记忆和推理的多模态模型。

---

## 3. 模拟信号滤波入门

**原文标题**: The 101 of Analog Signal Filtering

**原文链接**: [https://lcamtuf.substack.com/p/the-101-of-analog-signal-filtering](https://lcamtuf.substack.com/p/the-101-of-analog-signal-filtering)

无法访问文章链接。

---

## 4. Meta 分割一切模型 3

**原文标题**: Meta Segment Anything Model 3

**原文链接**: [https://ai.meta.com/blog/segment-anything-model-3/?_fb_noscript=1](https://ai.meta.com/blog/segment-anything-model-3/?_fb_noscript=1)

无法访问文章链接。

---

## 5. 人类大脑预先配置了理解世界的指令。

**原文标题**: Human brains are preconfigured with instructions for understanding the world

**原文链接**: [https://news.ucsc.edu/2025/11/sharf-preconfigured-brain/](https://news.ucsc.edu/2025/11/sharf-preconfigured-brain/)

加州大学圣克鲁兹分校的研究人员发现，人脑在感官体验发生之前就已具备预先配置的活动模式，表明存在一种内在的“操作系统”指导着与世界的互动。他们利用脑类器官（由干细胞生长而成的三维人脑组织模型）来研究最早的电活动时刻。这项发表在《自然·神经科学》上的研究表明，这些早期的脑电活动是在没有外部刺激的情况下以结构化模式发生的。

这项研究使科学家们能够在伦理的框架下研究人脑发育，而这通常是在子宫内受到保护的。通过观察类器官，该团队发现细胞自发地发出类似于大脑“默认模式”的电信号，这是一种神经元放电的基本底层结构。这些模式出现在发育的最初几个月，有可能被优化用于特定的感觉。

这些发现对于理解神经发育障碍以及毒素对发育中的大脑的影响具有重大意义。识别和研究类器官中的这些早期模式可以为开发脑部疾病的临床前疗法铺平道路，包括药物疗法和基因编辑工具。这项研究突显了类器官在彻底改变我们对人脑发育及其脆弱性的理解方面的潜力。

---

## 6. Pebble手表软件现在开源

**原文标题**: Pebble Watch software is now open source

**原文链接**: [https://ericmigi.com/blog/pebble-watch-software-is-now-100percent-open-source](https://ericmigi.com/blog/pebble-watch-software-is-now-100percent-open-source)

本文宣布Pebble手表软件现已100%开源，旨在解决对该平台长期可持续性的担忧。在Core Devices旗下重启Pebble的作者强调了硬件和软件长期维护的重要性。

在硬件方面，Core Devices自筹资金，致力于制造可修复的手表，如Pebble Time 2，其电池可更换，且Pebble 2 Duo的原理图已公开。

关键进展是Pebble软件的完全开源，包括PebbleOS和移动配套应用程序。这确保了即使Core Devices不复存在，社区也能维护和改进该软件。文章详细介绍了使用Kotlin Multiplatform构建的新移动应用程序现在是开源的。

Pebble Appstore也在去中心化。该移动应用程序将支持多个应用商店“源”，允许任何人创建和托管Pebble应用程序库。Core Devices已推出自己的源，将应用程序备份到Archive.org。开发者仍然可以将其应用程序货币化。

最后，本文提供了有关Pebble Time 2的最新信息，目标是在一月份开始发货，大部分预计在三月/四月送达，并承认可能因中国新年而延迟。还提供了一个预生产PT2手表的视频演示。预购客户很快就可以选择自己喜欢的颜色。

---

## 7. 古惑狼制作秘辛 (2011)

**原文标题**: Making Crash Bandicoot (2011)

**原文链接**: [https://all-things-andy-gavin.com/video-games/making-crash/](https://all-things-andy-gavin.com/video-games/making-crash/)

这篇2011年2月的文章节选标志着“古惑狼”制作系列文章的开始。作者，顽皮狗公司创始人之一，回顾了公司1994年夏天的状况。当时，顽皮狗还是一个由作者和他搭档杰森·鲁宾组成的两人小团队。在过去的八年里，他们高效合作，成功发行了六款游戏。然而，文章暗示，1994年他们决定扩大公司规模，预示着即将开始开发后来的“古惑狼”。“阅读更多”链接表明后续文章将更深入地探讨公司扩张的过程以及这款标志性平台游戏开发的早期阶段。

---

## 8. 数万亿美元投入，大型软件项目依然失败

**原文标题**: Trillions Spent and Big Software Projects Are Still Failing

**原文链接**: [https://spectrum.ieee.org/it-management-software-failures](https://spectrum.ieee.org/it-management-software-failures)

万亿投入，大型软件项目仍频频失败

---

## 9. 研究发现，Ozempic无法延缓阿尔茨海默症。

**原文标题**: Ozempic does not slow Alzheimer's, study finds

**原文链接**: [https://www.semafor.com/article/11/25/2025/ozempic-does-not-slow-alzheimers-study-finds](https://www.semafor.com/article/11/25/2025/ozempic-does-not-slow-alzheimers-study-finds)

诺和诺德研究显示Ozempic不延缓阿尔茨海默病进展

---

## 10. 最稳定的树莓派？更好的NTP与散热管理

**原文标题**: Most Stable Raspberry Pi? Better NTP with Thermal Management

**原文链接**: [https://austinsnerdythings.com/2025/11/24/worlds-most-stable-raspberry-pi-81-better-ntp-with-thermal-management/](https://austinsnerdythings.com/2025/11/24/worlds-most-stable-raspberry-pi-81-better-ntp-with-thermal-management/)

本文详细介绍了如何通过解决热致时序抖动来提高基于树莓派的NTP服务器的稳定性，以实现精确计时。作者注意到，尽管有稳定的GPS PPS参考，NTP服务器中的频率漂移与CPU温度变化相关。核心问题：CPU频率调整和温度相关的晶体振荡器频率。

解决方案包括两个主要组成部分：CPU核心绑定和热稳定。CPU核心绑定将CPU 0专用于时间关键型任务（chronyd和PPS中断），通过启动优化脚本将CPU调控器设置为“性能”模式，将PPS中断和chronyd绑定到CPU 0，将chronyd设置为实时优先级，并提高内核softirq处理程序的优先级。

热稳定使用PID控制的“时间燃烧器”来维持恒定的CPU温度。这个Python脚本读取CPU温度，计算维持目标温度（54°C）所需的CPU负载，并使用worker进程将负载分配到CPU 1-3上，这些进程在忙循环哈希和睡眠之间交替。通过维持稳定的CPU温度，物理上接近的晶体振荡器的热环境得到稳定，从而实现一致的时钟频率并改善计时。

结果表明，频率稳定性得到了显著改善，平均RMS偏移降低了近50%，中位数RMS偏移降低了52.7%。本文提供了复制优化的详细设置说明，包括启动优化和热稳定的脚本，以及systemd服务配置。作者强调，对于频率稳定性而言，保持硅温度一致比环境空气温度变化更重要。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 2 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 3 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 4 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 5 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 6 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 7 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 8 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 9 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 10 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 11 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 12 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 13 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 14 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 15 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 16 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 17 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 18 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 19 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 20 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 21 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 22 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 23 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 24 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 25 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 26 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 27 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 28 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 29 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 30 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 31 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 32 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 33 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 34 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 35 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 36 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 37 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 38 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 39 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 40 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 41 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 42 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 43 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 44 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 45 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 46 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 47 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 48 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 49 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 50 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 51 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 52 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 53 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 54 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 55 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 56 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 57 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 58 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 59 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 60 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 61 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 62 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 63 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 64 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 65 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 66 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 67 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 68 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 69 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 70 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 71 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 72 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 73 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 74 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 75 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 76 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 77 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 78 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 79 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 80 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 81 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 82 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 83 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 84 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 85 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 86 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 87 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 88 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 89 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 90 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 91 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 92 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 93 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 94 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 95 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 96 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 97 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 98 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 99 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 100 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 101 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 102 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 103 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 104 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 105 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 106 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 107 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 108 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 109 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 110 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 111 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 112 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 113 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 114 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 115 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 116 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 117 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 118 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 119 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 120 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 121 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 122 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 123 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 124 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 125 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 126 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 127 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 128 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 129 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 130 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 131 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 132 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 133 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 134 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 135 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 136 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 137 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 138 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 139 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 140 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 141 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 142 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 143 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 144 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 145 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 146 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 147 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 148 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 149 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 150 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 151 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 152 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 153 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 154 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 155 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 156 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 157 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 158 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 159 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 160 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 161 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 162 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 163 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 164 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 165 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 166 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 167 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 168 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 169 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 170 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 171 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 172 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 173 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 174 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 175 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 176 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 177 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 178 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 179 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 180 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 181 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 182 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 183 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 184 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 185 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 186 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 187 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 188 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 189 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 190 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 191 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 192 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 193 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 194 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 195 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 196 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 197 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 198 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 199 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 200 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 201 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 202 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 203 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 204 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 205 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 206 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 207 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 208 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 209 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 210 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 211 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 212 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 213 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 214 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 215 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 216 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 217 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 218 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 219 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 220 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 221 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 222 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 223 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 224 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 225 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 226 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 227 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 228 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 229 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 230 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 231 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 232 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 233 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 234 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 235 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 236 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 237 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 238 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 239 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 240 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 241 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 242 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 243 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 244 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 245 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 246 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 247 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 248 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 249 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 250 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
