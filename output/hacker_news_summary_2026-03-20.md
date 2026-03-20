# Hacker News 热门文章摘要 (2026-03-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 90% of crypto's Illinois primary spending failed to achieve its objective

**原文标题**: 90% of crypto's Illinois primary spending failed to achieve its objective

**原文链接**: [https://www.mollywhite.net/micro/entry/202603172318](https://www.mollywhite.net/micro/entry/202603172318)

生成摘要时出错

---

## 12. Flash-KMeans: Fast and Memory-Efficient Exact K-Means

**原文标题**: Flash-KMeans: Fast and Memory-Efficient Exact K-Means

**原文链接**: [https://arxiv.org/abs/2603.09229](https://arxiv.org/abs/2603.09229)

生成摘要时出错

---

## 13. Regex Blaster

**原文标题**: Regex Blaster

**原文链接**: [https://mdp.github.io/regex-blaster/](https://mdp.github.io/regex-blaster/)

生成摘要时出错

---

## 14. Just Put It on a Map

**原文标题**: Just Put It on a Map

**原文链接**: [https://progressandpoverty.substack.com/p/just-put-it-on-a-map](https://progressandpoverty.substack.com/p/just-put-it-on-a-map)

生成摘要时出错

---

## 15. MacBook M5 Pro and Qwen3.5 = Local AI Security System

**原文标题**: MacBook M5 Pro and Qwen3.5 = Local AI Security System

**原文链接**: [https://www.sharpai.org/benchmark/](https://www.sharpai.org/benchmark/)

生成摘要时出错

---

## 16. Delve – Fake Compliance as a Service

**原文标题**: Delve – Fake Compliance as a Service

**原文链接**: [https://deepdelver.substack.com/p/delve-fake-compliance-as-a-service](https://deepdelver.substack.com/p/delve-fake-compliance-as-a-service)

生成摘要时出错

---

## 17. The Soul of a Pedicab Driver

**原文标题**: The Soul of a Pedicab Driver

**原文链接**: [https://www.sheldonbrown.com/pedicab.html](https://www.sheldonbrown.com/pedicab.html)

生成摘要时出错

---

## 18. Exploring 8 Shaft Weaving

**原文标题**: Exploring 8 Shaft Weaving

**原文链接**: [https://slab.org/2026/03/11/exploring-8-shaft-weaving/](https://slab.org/2026/03/11/exploring-8-shaft-weaving/)

生成摘要时出错

---

## 19. Having Kids (2019)

**原文标题**: Having Kids (2019)

**原文链接**: [https://paulgraham.com/kids.html](https://paulgraham.com/kids.html)

生成摘要时出错

---

## 20. Oregon school cell phone ban: 'Engaged students, joyful teachers'

**原文标题**: Oregon school cell phone ban: 'Engaged students, joyful teachers'

**原文链接**: [https://portlandtribune.com/2026/03/18/oregon-school-cell-phone-ban-engaged-students-joyful-teachers/](https://portlandtribune.com/2026/03/18/oregon-school-cell-phone-ban-engaged-students-joyful-teachers/)

生成摘要时出错

---

## 21. FSF statement on copyright infringement lawsuit Bartz v. Anthropic

**原文标题**: FSF statement on copyright infringement lawsuit Bartz v. Anthropic

**原文链接**: [https://www.fsf.org/blogs/licensing/2026-anthropic-settlement](https://www.fsf.org/blogs/licensing/2026-anthropic-settlement)

生成摘要时出错

---

## 22. Drawvg Filter for FFmpeg

**原文标题**: Drawvg Filter for FFmpeg

**原文链接**: [https://ayosec.github.io/ffmpeg-drawvg/](https://ayosec.github.io/ffmpeg-drawvg/)

生成摘要时出错

---

## 23. Randomization in Controlled Experiments

**原文标题**: Randomization in Controlled Experiments

**原文链接**: [https://queue.acm.org/detail.cfm?id=3778029](https://queue.acm.org/detail.cfm?id=3778029)

生成摘要时出错

---

## 24. Full Disclosure: A Third (and Fourth) Azure Sign-In Log Bypass Found

**原文标题**: Full Disclosure: A Third (and Fourth) Azure Sign-In Log Bypass Found

**原文链接**: [https://trustedsec.com/blog/full-disclosure-a-third-and-fourth-azure-sign-in-log-bypass-found](https://trustedsec.com/blog/full-disclosure-a-third-and-fourth-azure-sign-in-log-bypass-found)

生成摘要时出错

---

## 25. Drugwars for the TI-82/83/83 Calculators (2011)

**原文标题**: Drugwars for the TI-82/83/83 Calculators (2011)

**原文链接**: [https://gist.github.com/mattmanning/1002653/b7a1e88479a10eaae3bd5298b8b2c86e16fb4404](https://gist.github.com/mattmanning/1002653/b7a1e88479a10eaae3bd5298b8b2c86e16fb4404)

生成摘要时出错

---

## 26. Building a Reader for the Smallest Hard Drive

**原文标题**: Building a Reader for the Smallest Hard Drive

**原文链接**: [https://www.willwhang.dev/Reading-MK4001MTD/](https://www.willwhang.dev/Reading-MK4001MTD/)

生成摘要时出错

---

## 27. Show HN: Sonar – A tiny CLI to see and kill whatever's running on localhost

**原文标题**: Show HN: Sonar – A tiny CLI to see and kill whatever's running on localhost

**原文链接**: [https://github.com/RasKrebs/sonar](https://github.com/RasKrebs/sonar)

生成摘要时出错

---

## 28. How the Turner twins are mythbusting modern technical apparel

**原文标题**: How the Turner twins are mythbusting modern technical apparel

**原文链接**: [https://www.carryology.com/insights/how-the-turner-twins-are-mythbusting-modern-gear/](https://www.carryology.com/insights/how-the-turner-twins-are-mythbusting-modern-gear/)

生成摘要时出错

---

## 29. Push events into a running session with channels

**原文标题**: Push events into a running session with channels

**原文链接**: [https://code.claude.com/docs/en/channels](https://code.claude.com/docs/en/channels)

生成摘要时出错

---

## 30. Google details new 24-hour process to sideload unverified Android apps

**原文标题**: Google details new 24-hour process to sideload unverified Android apps

**原文链接**: [https://arstechnica.com/gadgets/2026/03/google-details-new-24-hour-process-to-sideload-unverified-android-apps/](https://arstechnica.com/gadgets/2026/03/google-details-new-24-hour-process-to-sideload-unverified-android-apps/)

生成摘要时出错

---

## 31. Chuck Norris has died

**原文标题**: Chuck Norris has died

**原文链接**: [https://variety.com/2026/film/news/chuck-norris-dead-walker-texas-ranger-dies-1236694953/](https://variety.com/2026/film/news/chuck-norris-dead-walker-texas-ranger-dies-1236694953/)

生成摘要时出错

---

## 32. Cockpit is a web-based graphical interface for servers

**原文标题**: Cockpit is a web-based graphical interface for servers

**原文链接**: [https://github.com/cockpit-project/cockpit](https://github.com/cockpit-project/cockpit)

生成摘要时出错

---

## 33. Carbon dioxide levels are higher than humans have ever experienced

**原文标题**: Carbon dioxide levels are higher than humans have ever experienced

**原文链接**: [https://www.cnn.com/2026/03/19/climate/carbon-dioxide-blood-chemistry-public-health-climate-change](https://www.cnn.com/2026/03/19/climate/carbon-dioxide-blood-chemistry-public-health-climate-change)

生成摘要时出错

---

## 34. Astral to Join OpenAI

**原文标题**: Astral to Join OpenAI

**原文链接**: [https://astral.sh/blog/openai](https://astral.sh/blog/openai)

生成摘要时出错

---

## 35. I'm OK being left behind, thanks

**原文标题**: I'm OK being left behind, thanks

**原文链接**: [https://shkspr.mobi/blog/2026/03/im-ok-being-left-behind-thanks/](https://shkspr.mobi/blog/2026/03/im-ok-being-left-behind-thanks/)

生成摘要时出错

---

## 36. Noq: n0's new QUIC implementation in Rust

**原文标题**: Noq: n0's new QUIC implementation in Rust

**原文链接**: [https://www.iroh.computer/blog/noq-announcement](https://www.iroh.computer/blog/noq-announcement)

生成摘要时出错

---

## 37. Germany Mandates ODF for Public Administration

**原文标题**: Germany Mandates ODF for Public Administration

**原文链接**: [https://linuxiac.com/germany-mandates-odf-for-public-administration/](https://linuxiac.com/germany-mandates-odf-for-public-administration/)

生成摘要时出错

---

## 38. Too Much Color

**原文标题**: Too Much Color

**原文链接**: [https://www.keithcirkel.co.uk/too-much-color/](https://www.keithcirkel.co.uk/too-much-color/)

生成摘要时出错

---

## 39. Java is fast, code might not be

**原文标题**: Java is fast, code might not be

**原文链接**: [https://jvogel.me/posts/2026/java-is-fast-your-code-might-not-be/](https://jvogel.me/posts/2026/java-is-fast-your-code-might-not-be/)

生成摘要时出错

---

## 40. A 6502 disassembler with a TUI: A modern take on Regenerator

**原文标题**: A 6502 disassembler with a TUI: A modern take on Regenerator

**原文链接**: [https://github.com/ricardoquesada/regenerator2000](https://github.com/ricardoquesada/regenerator2000)

生成摘要时出错

---

## 41. Schizophrenia study finds new biomarker, drug candidate in mice

**原文标题**: Schizophrenia study finds new biomarker, drug candidate in mice

**原文链接**: [https://news.northwestern.edu/stories/2026/03/schizophrenia-study-finds-new-biomarker-drug-candidate-to-treat-cognitive-symptoms](https://news.northwestern.edu/stories/2026/03/schizophrenia-study-finds-new-biomarker-drug-candidate-to-treat-cognitive-symptoms)

生成摘要时出错

---

## 42. Scaling Karpathy's Autoresearch: What Happens When the Agent Gets a GPU Cluster

**原文标题**: Scaling Karpathy's Autoresearch: What Happens When the Agent Gets a GPU Cluster

**原文链接**: [https://blog.skypilot.co/scaling-autoresearch/](https://blog.skypilot.co/scaling-autoresearch/)

生成摘要时出错

---

## 43. Google Search is now using AI to replace headlines

**原文标题**: Google Search is now using AI to replace headlines

**原文链接**: [https://www.theverge.com/tech/896490/google-replace-news-headlines-in-search-canary-coal-mine-experiment](https://www.theverge.com/tech/896490/google-replace-news-headlines-in-search-canary-coal-mine-experiment)

生成摘要时出错

---

## 44. Show HN: FPGA soft-core of the Saab Viggen's 1963 airborne computer

**原文标题**: Show HN: FPGA soft-core of the Saab Viggen's 1963 airborne computer

**原文链接**: [https://github.com/FormerLab/ck37-core](https://github.com/FormerLab/ck37-core)

生成摘要时出错

---

## 45. KiCad 10.0.0 Release

**原文标题**: KiCad 10.0.0 Release

**原文链接**: [https://www.kicad.org/blog/2026/03/Version-10.0.0-Released/](https://www.kicad.org/blog/2026/03/Version-10.0.0-Released/)

生成摘要时出错

---

## 46. NanoGPT Slowrun: 10x Data Efficiency with Infinite Compute

**原文标题**: NanoGPT Slowrun: 10x Data Efficiency with Infinite Compute

**原文链接**: [https://qlabs.sh/10x](https://qlabs.sh/10x)

生成摘要时出错

---

## 47. Clockwise acquired by Salesforce

**原文标题**: Clockwise acquired by Salesforce

**原文链接**: [https://www.getclockwise.com](https://www.getclockwise.com)

生成摘要时出错

---

## 48. Systemd Introduces Birth Date Support for Upcoming Linux Desktop Age Controls

**原文标题**: Systemd Introduces Birth Date Support for Upcoming Linux Desktop Age Controls

**原文链接**: [https://linuxiac.com/systemd-introduces-birth-date-support-for-upcoming-linux-desktop-age-controls/](https://linuxiac.com/systemd-introduces-birth-date-support-for-upcoming-linux-desktop-age-controls/)

生成摘要时出错

---

## 49. Linux Page Faults, MMAP, and userfaultfd for faster VM boots

**原文标题**: Linux Page Faults, MMAP, and userfaultfd for faster VM boots

**原文链接**: [https://www.shayon.dev/post/2026/65/linux-page-faults-mmap-and-userfaultfd/](https://www.shayon.dev/post/2026/65/linux-page-faults-mmap-and-userfaultfd/)

生成摘要时出错

---

## 50. Be intentional about how AI changes your codebase

**原文标题**: Be intentional about how AI changes your codebase

**原文链接**: [https://aicode.swerdlow.dev](https://aicode.swerdlow.dev)

生成摘要时出错

---

## 51. Return of the Obra Dinn: spherical mapped dithering for a 1bpp first-person game

**原文标题**: Return of the Obra Dinn: spherical mapped dithering for a 1bpp first-person game

**原文链接**: [https://forums.tigsource.com/index.php?topic=40832.msg1363742#msg1363742](https://forums.tigsource.com/index.php?topic=40832.msg1363742#msg1363742)

生成摘要时出错

---

## 52. Delphi 13.1 Released, with ARM64 support

**原文标题**: Delphi 13.1 Released, with ARM64 support

**原文链接**: [https://blogs.embarcadero.com/announcing-the-availability-of-rad-studio-13-florence-update-1/](https://blogs.embarcadero.com/announcing-the-availability-of-rad-studio-13-florence-update-1/)

生成摘要时出错

---

## 53. How many branches can your CPU predict?

**原文标题**: How many branches can your CPU predict?

**原文链接**: [https://lemire.me/blog/2026/03/18/how-many-branches-can-your-cpu-predict/](https://lemire.me/blog/2026/03/18/how-many-branches-can-your-cpu-predict/)

生成摘要时出错

---

## 54. Show HN: Three new Kitten TTS models – smallest less than 25MB

**原文标题**: Show HN: Three new Kitten TTS models – smallest less than 25MB

**原文链接**: [https://github.com/KittenML/KittenTTS](https://github.com/KittenML/KittenTTS)

生成摘要时出错

---

## 55. Waymo Safety Impact

**原文标题**: Waymo Safety Impact

**原文链接**: [https://waymo.com/safety/impact/](https://waymo.com/safety/impact/)

生成摘要时出错

---

## 56. Cursor Composer 2 is just Kimi K2.5 with RL

**原文标题**: Cursor Composer 2 is just Kimi K2.5 with RL

**原文链接**: [https://twitter.com/fynnso/status/2034706304875602030](https://twitter.com/fynnso/status/2034706304875602030)

生成摘要时出错

---

## 57. Afroman found not liable in defamation case

**原文标题**: Afroman found not liable in defamation case

**原文链接**: [https://nypost.com/2026/03/18/us-news/afroman-found-not-liable-in-bizarre-ohio-defamation-case/](https://nypost.com/2026/03/18/us-news/afroman-found-not-liable-in-bizarre-ohio-defamation-case/)

生成摘要时出错

---

## 58. I turned Markdown into a protocol for generative UI

**原文标题**: I turned Markdown into a protocol for generative UI

**原文链接**: [https://fabian-kuebler.com/posts/markdown-agentic-ui/](https://fabian-kuebler.com/posts/markdown-agentic-ui/)

生成摘要时出错

---

## 59. “Your frustration is the product”

**原文标题**: “Your frustration is the product”

**原文链接**: [https://daringfireball.net/2026/03/your_frustration_is_the_product](https://daringfireball.net/2026/03/your_frustration_is_the_product)

生成摘要时出错

---

## 60. 4Chan mocks £520k fine for UK online safety breaches

**原文标题**: 4Chan mocks £520k fine for UK online safety breaches

**原文链接**: [https://www.bbc.com/news/articles/c624330lg1ko](https://www.bbc.com/news/articles/c624330lg1ko)

生成摘要时出错

---

## 61. From Oscilloscope to Wireshark: A UDP Story (2022)

**原文标题**: From Oscilloscope to Wireshark: A UDP Story (2022)

**原文链接**: [https://www.mattkeeter.com/blog/2022-08-11-udp/](https://www.mattkeeter.com/blog/2022-08-11-udp/)

生成摘要时出错

---

## 62. The Shape of Inequalities

**原文标题**: The Shape of Inequalities

**原文链接**: [https://www.andreinc.net/2026/03/16/the-shape-of-inequalities/](https://www.andreinc.net/2026/03/16/the-shape-of-inequalities/)

生成摘要时出错

---

## 63. FSFE supporters affected: Payment provider Nexi cancelled us

**原文标题**: FSFE supporters affected: Payment provider Nexi cancelled us

**原文链接**: [https://fsfe.org/news/2026/news-20260316-01.en.html](https://fsfe.org/news/2026/news-20260316-01.en.html)

生成摘要时出错

---

## 64. Bombarding gamblers with offers greatly increases betting and gambling harm

**原文标题**: Bombarding gamblers with offers greatly increases betting and gambling harm

**原文链接**: [https://www.bristol.ac.uk/news/2026/march/bombarding-gamblers-with-offers-greatly-increases-betting-and-gambling-harm.html](https://www.bristol.ac.uk/news/2026/march/bombarding-gamblers-with-offers-greatly-increases-betting-and-gambling-harm.html)

生成摘要时出错

---

## 65. macOS 26 breaks custom DNS settings including .internal

**原文标题**: macOS 26 breaks custom DNS settings including .internal

**原文链接**: [https://gist.github.com/adamamyl/81b78eced40feae50eae7c4f3bec1f5a](https://gist.github.com/adamamyl/81b78eced40feae50eae7c4f3bec1f5a)

生成摘要时出错

---

## 66. Microsoft breaks Microsoft account sign-ins in Windows 11 with latest update

**原文标题**: Microsoft breaks Microsoft account sign-ins in Windows 11 with latest update

**原文链接**: [https://www.theregister.com/2026/03/20/microsoft_account_not_working_have/](https://www.theregister.com/2026/03/20/microsoft_account_not_working_have/)

生成摘要时出错

---

## 67. 3D Printing High Quality Keycaps (2024)

**原文标题**: 3D Printing High Quality Keycaps (2024)

**原文链接**: [https://candrews.integralblue.com/2024/03/3d-printing-high-quality-keycaps/](https://candrews.integralblue.com/2024/03/3d-printing-high-quality-keycaps/)

生成摘要时出错

---

## 68. Thoughts on OpenAI acquiring Astral and uv/ruff/ty

**原文标题**: Thoughts on OpenAI acquiring Astral and uv/ruff/ty

**原文链接**: [https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/](https://simonwillison.net/2026/Mar/19/openai-acquiring-astral/)

生成摘要时出错

---

## 69. EsoLang-Bench: Evaluating Genuine Reasoning in LLMs via Esoteric Languages

**原文标题**: EsoLang-Bench: Evaluating Genuine Reasoning in LLMs via Esoteric Languages

**原文链接**: [https://esolang-bench.vercel.app/](https://esolang-bench.vercel.app/)

生成摘要时出错

---

## 70. Essex police pause facial recognition camera use after study finds racial bias

**原文标题**: Essex police pause facial recognition camera use after study finds racial bias

**原文链接**: [https://www.theguardian.com/technology/2026/mar/19/essex-police-pause-facial-recognition-camera-use-study-racial-bias](https://www.theguardian.com/technology/2026/mar/19/essex-police-pause-facial-recognition-camera-use-study-racial-bias)

生成摘要时出错

---

## 71. TI-89 Height-Mapped Raycaster

**原文标题**: TI-89 Height-Mapped Raycaster

**原文链接**: [https://github.com/dzoba/ti-89-raycasting-with-z](https://github.com/dzoba/ti-89-raycasting-with-z)

生成摘要时出错

---

## 72. An update on Steam / GOG changes for OpenTTD

**原文标题**: An update on Steam / GOG changes for OpenTTD

**原文链接**: [https://www.openttd.org/news/2026/03/19/steam-changes-update](https://www.openttd.org/news/2026/03/19/steam-changes-update)

生成摘要时出错

---

## 73. Eniac, the First General-Purpose Digital Computer, Turns 80

**原文标题**: Eniac, the First General-Purpose Digital Computer, Turns 80

**原文链接**: [https://spectrum.ieee.org/eniac-80-ieee-milestone](https://spectrum.ieee.org/eniac-80-ieee-milestone)

生成摘要时出错

---

## 74. The day I discovered type design

**原文标题**: The day I discovered type design

**原文链接**: [https://www.marksimonson.com/notebook/view/the-day-i-discovered-type-design/](https://www.marksimonson.com/notebook/view/the-day-i-discovered-type-design/)

生成摘要时出错

---

## 75. Last love: a romance in a care home (2023)

**原文标题**: Last love: a romance in a care home (2023)

**原文链接**: [https://www.theguardian.com/lifeandstyle/2023/nov/23/last-love-a-romance-in-a-care-home](https://www.theguardian.com/lifeandstyle/2023/nov/23/last-love-a-romance-in-a-care-home)

生成摘要时出错

---

## 76. Show HN: Duplicate 3 layers in a 24B LLM, logical deduction .22→.76. No training

**原文标题**: Show HN: Duplicate 3 layers in a 24B LLM, logical deduction .22→.76. No training

**原文链接**: [https://github.com/alainnothere/llm-circuit-finder](https://github.com/alainnothere/llm-circuit-finder)

生成摘要时出错

---

## 77. Codex with a vague prompt just solved a bug in Ghostty

**原文标题**: Codex with a vague prompt just solved a bug in Ghostty

**原文链接**: [https://twitter.com/mitchellh/status/2029348087538565612](https://twitter.com/mitchellh/status/2029348087538565612)

生成摘要时出错

---

## 78. My Random Forest Was Mostly Learning Time-to-Expiry Noise

**原文标题**: My Random Forest Was Mostly Learning Time-to-Expiry Noise

**原文链接**: [https://illya.sh/threads/out-of-sample-permutation-feature-importance-for-random](https://illya.sh/threads/out-of-sample-permutation-feature-importance-for-random)

生成摘要时出错

---

## 79. OpenBSD: PF queues break the 4 Gbps barrier

**原文标题**: OpenBSD: PF queues break the 4 Gbps barrier

**原文链接**: [https://undeadly.org/cgi?action=article;sid=20260319125859](https://undeadly.org/cgi?action=article;sid=20260319125859)

生成摘要时出错

---

## 80. Juggalo makeup blocks facial recognition technology (2019)

**原文标题**: Juggalo makeup blocks facial recognition technology (2019)

**原文链接**: [https://consequence.net/2019/07/juggalo-makeup-facial-recognition/](https://consequence.net/2019/07/juggalo-makeup-facial-recognition/)

生成摘要时出错

---

## 81. Prompt Injecting Contributing.md

**原文标题**: Prompt Injecting Contributing.md

**原文链接**: [https://glama.ai/blog/2026-03-19-open-source-has-a-bot-problem](https://glama.ai/blog/2026-03-19-open-source-has-a-bot-problem)

生成摘要时出错

---

## 82. Ndea (YC W26) is hiring a symbolic RL search guidance lead

**原文标题**: Ndea (YC W26) is hiring a symbolic RL search guidance lead

**原文链接**: [https://ndea.com/jobs/search-guidance](https://ndea.com/jobs/search-guidance)

生成摘要时出错

---

## 83. Connecticut and the 1 Kilometer Effect

**原文标题**: Connecticut and the 1 Kilometer Effect

**原文链接**: [https://alearningaday.blog/2026/03/19/connecticut-and-the-1-kilometer-effect/](https://alearningaday.blog/2026/03/19/connecticut-and-the-1-kilometer-effect/)

生成摘要时出错

---

## 84. Floating wetlands boost water quality, slash greenhouse emissions

**原文标题**: Floating wetlands boost water quality, slash greenhouse emissions

**原文链接**: [https://www.science.org/content/article/floating-wetlands-boost-water-quality-slash-greenhouse-emissions](https://www.science.org/content/article/floating-wetlands-boost-water-quality-slash-greenhouse-emissions)

生成摘要时出错

---

## 85. GrapheneOS: Duress Pin/Password

**原文标题**: GrapheneOS: Duress Pin/Password

**原文链接**: [https://grapheneos.org/features](https://grapheneos.org/features)

生成摘要时出错

---

## 86. Wayland set the Linux Desktop back by 10 years?

**原文标题**: Wayland set the Linux Desktop back by 10 years?

**原文链接**: [https://omar.yt/posts/wayland-set-the-linux-desktop-back-by-10-years](https://omar.yt/posts/wayland-set-the-linux-desktop-back-by-10-years)

生成摘要时出错

---

## 87. Ramtrack.eu – RAM Price Intelligence

**原文标题**: Ramtrack.eu – RAM Price Intelligence

**原文链接**: [https://ramtrack.eu](https://ramtrack.eu)

生成摘要时出错

---

## 88. Physicists Trace Sun's Magnetic Engine, 200k Kilometers Below Surface

**原文标题**: Physicists Trace Sun's Magnetic Engine, 200k Kilometers Below Surface

**原文链接**: [https://news.njit.edu/njit-physicists-trace-sun%E2%80%99s-magnetic-engine-200000-kilometers-below-surface](https://news.njit.edu/njit-physicists-trace-sun%E2%80%99s-magnetic-engine-200000-kilometers-below-surface)

生成摘要时出错

---

## 89. A sufficiently detailed spec is code

**原文标题**: A sufficiently detailed spec is code

**原文链接**: [https://haskellforall.com/2026/03/a-sufficiently-detailed-spec-is-code](https://haskellforall.com/2026/03/a-sufficiently-detailed-spec-is-code)

生成摘要时出错

---

## 90. EnshittifAIcation

**原文标题**: EnshittifAIcation

**原文链接**: [https://it-notes.dragas.net/2026/03/20/enshittifaication/](https://it-notes.dragas.net/2026/03/20/enshittifaication/)

生成摘要时出错

---

## 91. Rob Pike’s Rules of Programming (1989)

**原文标题**: Rob Pike’s Rules of Programming (1989)

**原文链接**: [https://www.cs.unc.edu/~stotts/COMP590-059-f24/robsrules.html](https://www.cs.unc.edu/~stotts/COMP590-059-f24/robsrules.html)

生成摘要时出错

---

## 92. Consensus Board Game

**原文标题**: Consensus Board Game

**原文链接**: [https://matklad.github.io/2026/03/19/consensus-board-game.html](https://matklad.github.io/2026/03/19/consensus-board-game.html)

生成摘要时出错

---

## 93. A National Policy Framework for Artificial Intelligence [pdf]

**原文标题**: A National Policy Framework for Artificial Intelligence [pdf]

**原文链接**: [https://www.whitehouse.gov/wp-content/uploads/2026/03/03.20.26-National-Policy-Framework-for-Artificial-Intelligence-Legislative-Recommendations.pdf](https://www.whitehouse.gov/wp-content/uploads/2026/03/03.20.26-National-Policy-Framework-for-Artificial-Intelligence-Legislative-Recommendations.pdf)

生成摘要时出错

---

## 94. Iran war energy shock sparks global push to reduce fossil fuel dependence

**原文标题**: Iran war energy shock sparks global push to reduce fossil fuel dependence

**原文链接**: [https://www.reuters.com/business/energy/iran-war-energy-shock-sparks-global-push-reduce-fossil-fuel-dependence-2026-03-18/](https://www.reuters.com/business/energy/iran-war-energy-shock-sparks-global-push-reduce-fossil-fuel-dependence-2026-03-18/)

生成摘要时出错

---

## 95. Russia suffers deadliest day of year with 1,700 troops lost

**原文标题**: Russia suffers deadliest day of year with 1,700 troops lost

**原文链接**: [https://www.telegraph.co.uk/world-news/2026/03/19/russia-deadliest-day-year-1700-troops-lost-ukraine/](https://www.telegraph.co.uk/world-news/2026/03/19/russia-deadliest-day-year-1700-troops-lost-ukraine/)

生成摘要时出错

---

## 96. No AI in Node.js Core

**原文标题**: No AI in Node.js Core

**原文链接**: [https://github.com/indutny/no-ai-in-nodejs-core](https://github.com/indutny/no-ai-in-nodejs-core)

生成摘要时出错

---

## 97. Atlassian, AI sell-off’s worst-hit company, grapples with ‘SaaSpocalypse’

**原文标题**: Atlassian, AI sell-off’s worst-hit company, grapples with ‘SaaSpocalypse’

**原文链接**: [https://www.ft.com/content/206df66d-09ac-46b6-a3c6-a25aaf07eb8a](https://www.ft.com/content/206df66d-09ac-46b6-a3c6-a25aaf07eb8a)

生成摘要时出错

---

## 98. How to defer US taxes

**原文标题**: How to defer US taxes

**原文链接**: [https://taylor.town/succession-000](https://taylor.town/succession-000)

生成摘要时出错

---

## 99. 2% of ICML papers desk rejected because the authors used LLM in their reviews

**原文标题**: 2% of ICML papers desk rejected because the authors used LLM in their reviews

**原文链接**: [https://blog.icml.cc/2026/03/18/on-violations-of-llm-review-policies/](https://blog.icml.cc/2026/03/18/on-violations-of-llm-review-policies/)

生成摘要时出错

---

## 100. Store birth date in systemd for age verification

**原文标题**: Store birth date in systemd for age verification

**原文链接**: [https://github.com/systemd/systemd/pull/40954](https://github.com/systemd/systemd/pull/40954)

生成摘要时出错

---

