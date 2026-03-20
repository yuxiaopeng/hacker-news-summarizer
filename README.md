# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-20.md)

*最后自动更新时间: 2026-03-20 18:02:56*
## 1. VisiCalc 重构

**原文标题**: VisiCalc Reconstructed

**原文链接**: [https://zserge.com/posts/visicalc/](https://zserge.com/posts/visicalc/)

在《重构 VisiCalc》一文中，作者通过演示如何用不到 500 行 C 语言代码构建一个极简克隆版，探讨了这款全球首创电子表格软件的深远影响。

该项目聚焦于四个核心组件：
1. **数据模型**：一个由单元格结构组成的网格，能够存储数字、文本标签或公式。
2. **公式求值器**：一个递归下降解析器，用于处理基础算术、单元格引用（如 +A1+B2）和函数（如 @SUM）。它利用 `NAN` 在计算过程中传递错误。
3. **响应式重算**：作者并未采用复杂的依赖图，而是实现了 VisiCalc 最初的迭代方法。程序通过多次遍历重新评估整个电子表格，直到数值趋于稳定，这对于中小型网格而言效率极高。
4. **TUI（文本用户界面）**：利用 `ncurses` 库，作者构建了一个经典的四部分界面，包含状态栏、编辑行、列标题和可滚动的网格视口。

此次重构突出了 VisiCalc 的模态界面，用户可以在“READY”（就绪）和“ENTRY”（输入）模式之间切换，以进行导航或数据录入。命令由斜杠（`/`）触发，保留了经典的交互体验。

作者总结道，尽管个人计算领域经历了近 50 年的演变，电子表格的核心架构——单元格、公式和网格——始终未变。该项目见证了 1979 年这款“杀手级应用”的设计精髓，证明了其核心功能既强大，实现起来又出奇地简单。

---

## 2. ArXiv 宣布脱离康奈尔大学独立

**原文标题**: ArXiv declares independence from Cornell

**原文链接**: [https://www.science.org/content/article/arxiv-pioneering-preprint-server-declares-independence-cornell](https://www.science.org/content/article/arxiv-pioneering-preprint-server-declares-independence-cornell)

作为数十年来开放科学的基石，影响力深远的预印本服务器 ArXiv 正从由康奈尔大学托管的项目转型为独立的 501(c)(3) 非营利组织。自 2001 年以来，康奈尔大学图书馆一直为该平台提供行政监督和技术支持。目前，该平台托管了超过 240 万篇涵盖物理、数学和计算机科学领域的论文。

成立“arXiv.org Inc.”的决定源于对更高运营灵活性和技术现代化的需求。作为一个独立实体，ArXiv 旨在更好地管理其快速增长，并更有效地升级其陈旧的基础设施。领导层指出，尽管康奈尔大学一直是一位给予支持的托管者，但该服务器的全球规模和 300 万美元的年度预算，需要一个专门致力于其独特使命的治理结构。

斯泰恩·西古德松（Steinn Sigurðsson）将继续担任科学总监，转型预计将于 2024 年底前完成。新的非营利组织将由代表其多元利益相关方的董事会管理，确保研究群体在平台的未来发展中拥有更直接的话语权。

至关重要的是，此举不会改变 ArXiv 提供免费、开放获取学术文章的核心使命。资金将维持混合模式，由西蒙斯基金会（Simons Foundation）、280 多家成员图书馆和研究机构以及个人捐赠者共同支持。这次独立是 ArXiv 的一个重大里程碑，赋予了它在数字科学传播格局不断变化的过程中随之演进的自主权。

---

## 3. France's aircraft carrier located in real time by Le Monde through fitness app

**原文标题**: France's aircraft carrier located in real time by Le Monde through fitness app

**原文链接**: [https://www.lemonde.fr/en/international/article/2026/03/20/stravaleaks-france-s-aircraft-carrier-located-in-real-time-by-le-monde-through-fitness-app_6751640_4.html](https://www.lemonde.fr/en/international/article/2026/03/20/stravaleaks-france-s-aircraft-carrier-located-in-real-time-by-le-monde-through-fitness-app_6751640_4.html)

生成摘要时出错

---

## 4. Parallel Perl —— 具备 JIT 功能的自动并行化解释器

**原文标题**: Parallel Perl – autoparallelizing interpreter with JIT

**原文链接**: [https://perl.petamem.com/gpw2026/perl-mit-ai-gpw2026.html#/4/1/1](https://perl.petamem.com/gpw2026/perl-mit-ai-gpw2026.html#/4/1/1)

在 2026 年德国 Perl 研讨会 (GPW 2026) 上，Richard Jelinek 展示了一种变革性的 Perl 开发方法，实现了从“Perl 辅助 AI”向“AI 编写 Perl”的转变。此次演讲重点介绍了两项重大成就：WHIP 家庭自动化系统和名为 **pperl** 的下一代 Perl 解释器。

**WHIP (机智房屋基础设施处理器)**
受大规模离网型“技术官僚”住宅（Villa-A 和 Villa-B）需求的驱动，Jelinek 开发了 WHIP 以取代老化的基于 Perl 的自动化工具。该系统采用多主站 CAN 总线架构、运行 FreeRTOS 的 STM32 微控制器以及基于 Perl 的中心节点。它通过“Ganglion”字节码自主管理复杂的能源、照明 (SELV-DALI) 和气候系统。

**AI 驱动的工具链**
Jelinek 利用 AI 智能体快速构建了此前缺失或损坏的高性能 Perl 基础设施。显著成果包括：
*   **SNMP::MIB::Compiler：** 一款在准确性上优于 Python 和 Go 替代方案的解析器。
*   **Grpc::FFI：** 使用 FFI 实现的、达到生产级标准的 Perl gRPC 方案。

**pperl (并行 Perl / PetaPerl)**
该项目的核心是 **pperl**，这是一个在人类指导下由 AI 智能体使用 **Rust** 编写的新型 Perl 5 解释器。pperl 专为高性能和现代并发设计，旨在兼容 Perl 5.42，同时提供标准 Perl 所缺乏的特性：
*   **自动并行化：** 利用 Rust 的 Rayon 库自动并行执行 `map`、`grep` 和 `for` 循环，无需 `threads` 编译指令。
*   **JIT 编译：** 利用 Cranelift 在运行时检测并将热点代码路径编译为原生代码。
*   **原生 Rust 实现：** 以完整的 Rust 代码取代传统的 XS，从而获得巨大的速度提升。
*   **高效性：** 通过预编译的 `.plc` 数据块和守护进程/客户端模式实现近乎瞬时的启动。

基准测试显示，pperl 在列表操作方面的性能比标准 Perl 5 高出多达 3.9 倍，使其成为面向该语言未来的现代化并行平台。

---

## 5. Entso-E关于2025年伊比利亚大停电的最终报告

**原文标题**: Entso-E final report on Iberian 2025 blackout

**原文链接**: [https://www.entsoe.eu/publications/blackout/28-april-2025-iberian-blackout/](https://www.entsoe.eu/publications/blackout/28-april-2025-iberian-blackout/)

2025年4月28日，西班牙和葡萄牙大陆地区电力系统发生全面停电，成为20多年来欧洲电网最严重的事故。事件发生后，欧洲电力传输系统运营商联盟（ENTSO-E）召集了一个由49名成员组成的专家小组——成员包括输电系统运营商（TSOs）、监管机构（ACER及各国监管机构）以及区域中心的代表——负责调查事故原因并提出建议。

在2026年3月20日发布的最终报告中，专家小组将此次停电定性为由多种复杂因素相互作用导致的“首例”事件。其主要根本原因包括功率振荡、电压和无功功率控制缺陷、监管实践不一致，以及导致西班牙境内发电机组连锁脱网的出力迅速下降。

此次调查强调了局部系统的变化如何产生波及全系统的巨大影响。为防止此类事件再次发生，专家小组提出了以下几项关键建议：
*   **运行改进：** 加强运行实践，并提升对系统行为的监测能力。
*   **协调配合：** 增加数据交换，促进电力系统各方参与者之间更紧密的合作。
*   **监管演进：** 调整监管框架和市场机制，使其适应不断变化的电力系统特性及其物理极限。
*   **韧性提升：** 实施技术上可部署的解决方案，以增强全系统的稳定能力。

报告强调，随着能源格局的持续演变，欧洲电力系统迫切需要保持局部与全欧协调之间的紧密联系，以确保系统的韧性。

---

## 6. 洛杉矶引水渠真狂野

**原文标题**: The Los Angeles Aqueduct Is Wild

**原文链接**: [https://practical.engineering/blog/2026/3/17/the-los-angeles-aqueduct-is-wild](https://practical.engineering/blog/2026/3/17/the-los-angeles-aqueduct-is-wild)

洛杉矶渡槽是一项全长300英里的重力输水工程奇迹，它将水从内华达山脉东部输送到洛杉矶。该项目于1913年在总工程师威廉·马尔霍兰的领导下竣工，将一座缺水的小镇转变为全球性大都市，目前供应着该市约三分之一的用水。

该系统堪称一台“重力机器”，利用2500英尺的海拔落差，在无需泵送的情况下实现引水。其基础设施种类多样，涵盖了露天运河、混凝土衬砌渠道，以及复杂的地下导管和用于跨越颚骨峡谷等深谷的加压“倒虹吸管”。随着时间的推移，该系统于1970年扩建了第二条渡槽，并增设了海威和布凯峡谷等多个水库，用于储水、紫外线消毒，并作为抵御地震或系统故障的缓冲。

然而，该项目的遗产极具争议。由于在欧文斯谷进行的恶意土地征收，引发了“加州水战争”，导致了当地人的怨恨、欧文斯河的改道，甚至发生了居民破坏基础设施的事件。在环境方面，引水工程导致欧文斯湖干涸，产生了巨大的有毒粉尘污染源，洛杉矶为此已投入超过10亿美元进行治理。

渡槽的历史也伴随着悲剧。1928年圣弗朗西斯大坝的溃决造成400多人死亡，成为美国历史上最严重的工程灾难之一，也彻底毁掉了马尔霍兰的声誉。

如今，这条渡槽依然是一条至关重要但又错综复杂的生命线。它整合了可产生巨大电能的水电站，并拥有与加利福尼亚州水利工程的现代连接。归根结底，该系统是一个深刻的范例，展示了人类野心、政治和工程学如何重塑一个地区的地理面貌，以支撑城市的持续扩张。

---

## 7. 社交小网络

**原文标题**: The Social Smolnet

**原文链接**: [https://ploum.net/2026-03-20-social-smolnet.html](https://ploum.net/2026-03-20-social-smolnet.html)

在《社交 Smolnet》（The Social Smolnet）一文中，Ploum 认为去中心化社交网络不需要复杂的新协议，而是已经通过博客与电子邮件的结合实现了。为了实现这一目标，Ploum 在 **Offpunk** 中集成了两项新功能。Offpunk 是一款专门针对“极简网络”（Small Web，如 Gemini、Gopher 和轻量级 HTML）的命令行浏览器。

新功能包括：
*   **分享 (Share)：** 允许用户通过默认邮件客户端快速向联系人发送 URL。
*   **回复 (Reply)：** 自动在页面或站点中搜索作者的电子邮箱地址。一旦找到，用户可以直接从终端发送反馈或“感谢”。Offpunk 还能保存这些地址，从而有效地将浏览器转变为一个去中心化的通讯录。

Ploum 强调，这种工作流非常适合偏好键盘驱动和终端环境（如使用 neomutt 和 neovim）的用户，并且非常契合离线或“断网式”的邮件处理习惯。自上线这些功能以来，Ploum 已使用它们与 40 多个不同的在线空间进行互动，并声称这让极简网络感觉像是一个功能完备的社交网络，比“点赞”按钮“更具人情味”。

文章以一种哲学视角收尾：社交网络的定义取决于我们如何使用基础设施，而非平台本身。Ploum 鼓励用户绕过臃肿的 JavaScript 和中心化的“科技巨头”生态，转而支持轻量级 HTML 和直接交流，并主张我们既有权利也有义务维护一个简单、独立的万维网。

---

## 8. 在 FFmpeg 中使用 Vulkan 计算着色器进行视频编解码

**原文标题**: Video Encoding and Decoding with Vulkan Compute Shaders in FFmpeg

**原文链接**: [https://www.khronos.org/blog/video-encoding-and-decoding-with-vulkan-compute-shaders-in-ffmpeg](https://www.khronos.org/blog/video-encoding-and-decoding-with-vulkan-compute-shaders-in-ffmpeg)

This article, written by FFmpeg maintainer Lynne, explores the use of **Vulkan Compute shaders** to accelerate professional video encoding and decoding. While consumer codecs like H.264 benefit from dedicated hardware (ASICs) via the Vulkan Video extensions, professional workflows involving 8K resolutions, high bit-depths, and lossless formats often remain performance-bound by the CPU.

The central challenge in GPU-based codec acceleration is the tension between the serial nature of compression algorithms (like Huffman coding) and the parallel architecture of GPUs. Historically, "hybrid" models—which split tasks between the CPU and GPU—failed due to high memory latency. To solve this, FFmpeg is moving toward **fully GPU-resident implementations**. By leveraging modern GPU features like cross-invocation communication, even traditionally serial processes can be parallelized effectively.

**Key implementations highlighted include:**
*   **FFv1:** An archival lossless codec optimized to handle complex range coding on the GPU.
*   **ProRes and ProRes RAW:** De-facto industry standards for editing, now accelerated through multi-pass "shred" configurations that maximize GPU saturation.
*   **APV and VC-2:** Mezzanine codecs designed for high parallelism or wavelet transforms.
*   **JPEG:** Innovative techniques like "spurious resynchronization" are being used to parallelize historically serial bitstreams.

Integrated directly into FFmpeg, these compute-based tools allow users to toggle seamlessly between software and hardware acceleration. As of **FFmpeg 8.1**, compute-accelerated support for FFv1, ProRes, and DPX is available, with APV, VC-2, and JPEG support in development. This approach unlocks the massive parallel power of consumer GPUs for high-end professional media, providing an open-source alternative to expensive, proprietary workstations.

---

## 9. Super Micro Shares Plunge 25% After Co-Founder Charged in $2.5B Smuggling Plot

**原文标题**: Super Micro Shares Plunge 25% After Co-Founder Charged in $2.5B Smuggling Plot

**原文链接**: [https://www.forbes.com/sites/tylerroush/2026/03/20/super-micro-shares-plunge-25-after-co-founder-charged-in-25-billion-ai-chip-smuggling-plot/](https://www.forbes.com/sites/tylerroush/2026/03/20/super-micro-shares-plunge-25-after-co-founder-charged-in-25-billion-ai-chip-smuggling-plot/)

生成摘要时出错

---

## 10. HP realizes that mandatory 15-minute support call wait times isn't good support

**原文标题**: HP realizes that mandatory 15-minute support call wait times isn't good support

**原文链接**: [https://arstechnica.com/gadgets/2025/02/misguided-hp-customer-support-approach-included-forced-15-minute-call-wait-times/](https://arstechnica.com/gadgets/2025/02/misguided-hp-customer-support-approach-included-forced-15-minute-call-wait-times/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 2 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 3 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 4 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 5 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 6 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 7 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 8 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 9 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 10 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 11 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 12 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 13 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 14 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 15 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 16 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 17 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 18 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 19 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 20 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 21 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 22 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 23 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 24 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 25 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 26 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 27 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 28 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 29 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 30 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 31 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 32 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 33 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 34 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 35 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 36 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 37 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 38 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 39 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 40 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 41 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 42 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 43 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 44 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 45 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 46 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 47 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 48 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 49 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 50 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 51 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 52 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 53 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 54 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 55 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 56 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 57 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 58 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 59 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 60 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 61 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 62 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 63 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 64 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 65 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 66 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 67 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 68 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 69 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 70 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 71 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 72 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 73 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 74 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 75 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 76 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 77 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 78 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 79 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 80 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 81 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 82 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 83 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 84 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 85 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 86 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 87 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 88 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 89 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 90 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 91 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 92 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 93 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 94 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 95 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 96 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 97 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 98 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 99 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 100 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 101 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 102 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 103 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 104 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 105 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 106 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 107 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 108 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 109 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 110 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 111 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 112 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 113 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 114 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 115 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 116 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 117 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 118 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 119 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 120 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 121 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 122 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 123 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 124 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 125 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 126 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 127 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 128 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 129 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 130 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 131 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 132 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 133 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 134 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 135 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 136 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 137 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 138 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 139 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 140 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 141 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 142 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 143 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 144 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 145 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 146 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 147 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 148 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 149 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 150 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 151 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 152 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 153 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 154 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 155 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 156 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 157 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 158 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 159 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 160 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 161 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 162 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 163 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 164 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 165 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 166 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 167 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 168 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 169 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 170 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 171 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 172 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 173 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 174 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 175 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 176 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 177 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 178 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 179 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 180 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 181 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 182 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 183 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 184 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 185 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 186 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 187 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 188 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 189 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 190 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 191 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 192 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 193 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 194 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 195 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 196 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 197 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 198 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 199 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 200 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 201 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 202 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 203 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 204 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 205 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 206 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 207 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 208 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 209 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 210 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 211 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 212 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 213 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 214 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 215 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 216 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 217 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 218 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 219 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 220 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 221 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 222 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 223 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 224 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 225 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 226 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 227 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 228 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 229 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 230 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 231 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 232 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 233 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 234 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 235 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 236 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 237 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 238 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 239 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 240 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 241 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 242 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 243 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 244 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 245 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 246 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 247 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 248 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 249 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 250 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 251 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 252 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 253 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 254 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 255 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 256 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 257 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 258 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 259 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 260 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 261 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 262 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 263 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 264 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 265 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 266 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 267 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 268 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 269 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 270 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 271 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 272 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 273 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 274 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 275 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 276 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 277 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 278 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 279 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 280 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 281 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 282 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 283 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 284 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 285 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 286 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 287 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 288 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 289 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 290 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 291 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 292 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 293 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 294 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 295 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 296 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 297 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 298 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 299 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 300 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 301 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 302 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 303 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 304 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 305 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 306 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 307 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 308 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 309 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 310 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 311 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 312 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 313 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 314 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 315 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 316 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 317 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 318 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 319 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 320 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 321 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 322 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 323 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 324 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 325 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 326 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 327 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 328 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 329 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 330 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 331 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 332 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 333 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 334 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 335 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 336 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 337 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 338 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 339 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 340 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 341 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 342 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 343 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 344 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 345 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 346 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 347 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 348 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 349 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 350 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 351 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 352 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 353 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 354 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 355 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 356 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 357 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 358 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 359 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 360 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 361 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 362 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 363 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 364 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 365 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
