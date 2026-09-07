# Hacker News 热门文章摘要 (2026-09-07)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 见证洛杉矶一栋接一栋地建成 (1880–2026)

**原文标题**: Watch Los Angeles get built, one building at a time (1880–2026)

**原文链接**: [https://lax-skyline.parcelscope.net/](https://lax-skyline.parcelscope.net/)

**Parcelscope 洛杉矶**是一款交互式数据可视化工具，展示了从 1880 年到 2026 年洛杉矶建筑的演变过程。该项目利用 LARIAC 2020 的建筑轮廓及洛杉矶县估价官办公室的数据，全面且按时间顺序呈现了这座城市的发展历程。

该工具将城市中的每座建筑表现为一个 3D 长方体，并根据其建造年代进行颜色编码。这让用户能够“目睹”城市在近 150 年间的填充过程，见证其从 19 世纪末的稀疏景观转变为今日的高密度大都市。

界面提供的主要功能和信息包括：
*   **年代增长：** 展示从 1880 年至今建设进程的时间轴。
*   **详细指标：** 单体建筑的数据，包括建造年份、总高度、占地面积和建筑类型。
*   **交互式导航：** 用户可以平移、缩放和倾斜地图以探索城市天际线。
*   **视觉辅助：** 在较宽的缩放级别下，建筑高度会被适当拉伸，以帮助用户在广阔的洛杉矶盆地中区分低层和高层建筑。

最终，该项目作为城市扩张与密度的数字记录，生动地展示了在过去的一个半世纪里，洛杉矶是如何通过一座座建筑的更迭而发生蜕变的。

---

## 2. 随机梯度方法 (2024)

**原文标题**: Methods for Random Gradients (2024)

**原文链接**: [https://justinjay.wang/methods-for-random-gradients/](https://justinjay.wang/methods-for-random-gradients/)

在《随机渐变的方法》（2024）一文中，作者回顾了用于塑造 OpenAI 视觉形象的渐变生成技术的演变。文章详细介绍了三种主要方法：

**1. 高度图渐变**
该方法使用 Processing 开发，利用平滑的柏林噪声创建“高度图”（0 到 1 之间的数值网格）。通过将随机颜色刻度映射到这些数值，作者创作出了具有有机感且引人注目的渐变效果。虽然在美学上令人愉悦，但这种方法最终被认为不适合 OpenAI 的正式品牌视觉。

**2. 分层径向渐变 (SVG)**
为了取代静态、低分辨率的图像，作者开发了一套使用可缩放矢量图形 (SVG) 的动态系统。通过叠加多个 `<radialGradient>` 元素并随机化其焦点、缩放和旋转，该系统在 2020 年至 2022 年间为 OpenAI 官网的每位访问者提供了一个独特且轻量（6 KB）的渐变效果。这种方法将高性能与无限的可扩展性结合在了一起。

**3. AI 生成渐变**
DALL·E 2 等生成式模型的出现引入了一种“老虎机”式的设计方法。通过使用特定的提示词——如“梦幻氛围”、“花卉的宏观摄影”或“日落天空”——作者可以生成具有质感和氛围感的渐变，这些效果既不可预测又充满创意。

文章总结道，早期的设计方法侧重于程序化控制和性能，而现代 AI 工具则为视觉实验开辟了广阔的新前沿，使设计师的角色从精准的执行者转变为创意的引导者。

---

## 3. Finding a bug in Dummit and Foote's Abstract Algebra

**原文标题**: Finding a bug in Dummit and Foote's Abstract Algebra

**原文链接**: [https://kallus.org/blog/dummit_and_foote.html](https://kallus.org/blog/dummit_and_foote.html)

生成摘要时出错

---

## 4. 未来天气 3

**原文标题**: WeatherNext 3

**原文链接**: [https://deepmind.google/science/weathernext/](https://deepmind.google/science/weathernext/)

WeatherNext 3 通过利用原始卫星图像生成逐小时预报，引入了一种全新的气象学方法。与以往模型不同，这种直接的数据集成实现了更频繁的更新，使用户能够精准追踪雨雪等快速变化的天气状况。

---

## 5. 简单并不渺小

**原文标题**: Simple Is Not Small

**原文链接**: [https://jyn.dev/simple-is-not-the-same-as-small/](https://jyn.dev/simple-is-not-the-same-as-small/)

在《简单并非精简》（Simple Is Not Small）一文中，作者指出开发者经常误将简洁（精简）视为简单。借鉴 Rich Hickey 的定义，文章将**简单**（Simplicity）定义为“解耦”（sim-plex：单辫），而将**复杂**（Complexity）定义为“耦合”（com-plex：多辫）。

作者以 Unix 管道为例，说明了一个“精简但耦合”的系统。虽然统计词频的 Unix 命令非常简短，但它与特定的数据格式和行为耦合（例如，`uniq` 要求输入必须是已排序的）。这种耦合使得一些简单的修改——例如保持单词的原始顺序——在 Bash 中变得异常困难且代码“丑陋”，而相比之下，在 Clojure 等语言中则更易实现。Clojure 通过将数据表示与类型检查解耦来实现简单，从而兼具了记录的结构性和映射（map）的灵活性。

核心观点包括：
*   **精简 vs. 简单**：精简通常是对资源受限（如开发时间或硬件）的反应，而简单则是一种优先考虑解耦的设计选择。
*   **简单的代价**：构建真正解耦的系统（如 SQL 或 CSS）往往需要巨大的工程投入——作者称之为“硬着头皮编写攻克难题”。
*   **用户体验**：庞大的程序（如 Google Drive）在用户看来可能很简单，因为它们在处理复杂的后台任务时，没有将这些复杂性与用户界面耦合。

最终，作者鼓励开发者优先考虑简单而非精简。即便程序体积更大，简单的代码也更容易维护且更具灵活性。复杂性并非源自代码行数，而是源自各部分之间隐藏的依赖关系。

---

## 6. Decoding the NEC V20 Microcode

**原文标题**: Decoding the NEC V20 Microcode

**原文链接**: [https://martypc.blogspot.com/2026/09/decoding-nec-v20-microcode.html](https://martypc.blogspot.com/2026/09/decoding-nec-v20-microcode.html)

生成摘要时出错

---

## 7. 加州理工数学马拉松 —— 史上首个致力于研究级数学的黑客松

**原文标题**: Caltech Mathathon – first hackathon ever devoted to research level mathematics

**原文链接**: [https://mathathonchallenge.com/index.html](https://mathathonchallenge.com/index.html)

**加州理工数学马拉松**

加州理工数学马拉松（Caltech Mathathon）定于10月30日至11月1日在加州理工学院举行，是全球首个致力于研究级数学的黑客松。在40小时的时间里，100支入选团队将利用总额超过200万美元AI算力额度支持的前沿AI模型，致力于攻克开放数学猜想并开发新的数学理论。

此次活动源于近期该领域一系列由AI主导的突破性进展，例如2026年对埃尔德什（Erdős）平面单位距离猜想的证伪。组织者旨在探索两个核心问题：AI能在多大程度上加速从灵感构思到同行评审发表的过程，以及当AI能够高速解决猜想时，数学家的角色将如何转变。

参赛者须向由顶尖数学家组成的评审团答辩其研究发现，评审团将评估他们对问题的理解以及成果的质量。比赛设有两级奖金制度：
1. **即时奖**：授予活动现场最具潜力且阐述最清晰的成果。
2. **第二轮奖项**：在更广泛的数学界有足够时间对发现进行正式验证后颁发。

通过汇聚全球顶尖人才，数学马拉松旨在定义纯数学领域人类智慧与人工智能协同研究的未来。

---

## 8. bzip3

**原文标题**: bzip3

**原文链接**: [https://github.com/iczelia/bzip3](https://github.com/iczelia/bzip3)

**bzip3** 是一款高性能压缩工具，被设计为 bzip2 的“精神续作”。它由 Kamila Szewczyk 开发，通过结合 0 阶上下文混合熵编码、Burrows-Wheeler 变换（通过 libsais 库）以及 LZP（Lempel-Ziv+Prediction）预处理阶段，提供了卓越的压缩率和速度。它特别针对文本和源代码进行了优化。

**关键性能指标：**
针对 Perl 5 源代码完整历史记录的基准测试证明了 bzip3 的高效性。在这些测试中，bzip3 的压缩率显著优于 LZMA (xz)、bzip2 和 Zstandard。例如，在使用 511MB 分块大小时，bzip3 将数据集压缩至约 546MB，而 LZMA 和 Zstandard 生成的文件大小分别为 2GB 和 3GB。当配合 `lrzip` 进行长距离去重时，文件大小进一步降至约 60MB。其解压速度也极具竞争力，通常超过 bzip2 并可与 Zstandard 媲美。

**技术细节与兼容性：**
*   **安装：** 可通过 autotools 从源码构建，或通过 macOS 上的 Homebrew 等包管理器进行安装。
*   **兼容性：** 支持广泛的架构，包括 x86、ARM、PowerPC、MIPS 和 s390x。
*   **许可协议：** 项目采用 LGPLv3 协议授权，同时包含部分采用 Apache 2.0 和 BSD 协议的组件。
*   **可靠性：** 虽然经过广泛测试，但开发者提供了一份免责声明：由于算法的复杂性，用户应意识到存在极小但非零的数据丢失风险。

总之，bzip3 为传统压缩工具提供了一个现代化、高效率的替代方案，特别适合处理大量文本数据并追求高压缩率与快速解压平衡的用户。

---

## 9. Trusting-Trust Attack against an Entire Linux Distribution

**原文标题**: Trusting-Trust Attack against an Entire Linux Distribution

**原文链接**: [https://arxiv.org/abs/2607.24888](https://arxiv.org/abs/2607.24888)

生成摘要时出错

---

## 10. 数据流模型再探

**原文标题**: The Dataflow Model Revisited

**原文链接**: [https://www.vldb.org/pvldb/volumes/19/paper/The%20Dataflow%20Model%20Revisited](https://www.vldb.org/pvldb/volumes/19/paper/The%20Dataflow%20Model%20Revisited)

在《Dataflow 模型再审视》（The Dataflow Model Revisited）中，作者回顾了原始 Dataflow 模型十一年来的历程，评估了其对流处理和批处理领域的影响。虽然论文的核心基础——特别是事件时间的重要性、强一致性以及处理不完整数据的必要性——经受住了时间的考验，但作者也指出了原始愿景中存在的几处不足。

这次回顾强调了对原始模型的三点主要反思：
1. **过度设计**：窗口和触发器过于复杂，迫使用户去处理本应被抽象掉的运维细节。
2. **流表二象性**：作者错失了一个基本事实，即流和表仅仅是相同数据的不同表现形式。
3. **侧重机制**：最初的研究过于关注流处理的底层机制，而未能利用 SQL 和增量视图维护等成熟的数据库概念来隐藏复杂性。

作者指出，业界已转向“快照一致性刷新”和带有明确新鲜度约定的物化视图，这些技术比复杂的水位线（watermarking）机制更受欢迎，因为它们对用户的要求更低。他们认为，“批处理与流处理”之争在很大程度上是语义层面的，而对低延迟处理的需求已沿着传统的 OLTP 和 OLAP 线路发生分化。

最后，论文为该模型提出了一个新的框架——“保留、剔除、加强”（leave in, leave out, push harder），并建议流处理的未来在于它作为一个独立、复杂实体的“消失”。相反，它应当融入更广泛的数据库生态系统中，使分析型流处理的复杂性对终端用户几乎完全不可见。

---

## 11. Searching for the best silicone USB cable

**原文标题**: Searching for the best silicone USB cable

**原文链接**: [https://www.frankchiarulli.com/blog/best-silicone-usb-cable/](https://www.frankchiarulli.com/blog/best-silicone-usb-cable/)

生成摘要时出错

---

## 12. Tesla killing Solar Roof is leaving installers with six-figure losses

**原文标题**: Tesla killing Solar Roof is leaving installers with six-figure losses

**原文链接**: [https://electrek.co/2026/09/01/tesla-solar-roof-exit-installers-losses/](https://electrek.co/2026/09/01/tesla-solar-roof-exit-installers-losses/)

生成摘要时出错

---

## 13. Decapitating a MacBook (2025)

**原文标题**: Decapitating a MacBook (2025)

**原文链接**: [https://mm-dev.rocks/series/decapitating-macbook-an-odyssey/](https://mm-dev.rocks/series/decapitating-macbook-an-odyssey/)

生成摘要时出错

---

## 14. Scientists observe Einstein's gravity in the quantum world

**原文标题**: Scientists observe Einstein's gravity in the quantum world

**原文链接**: [https://www.ox.ac.uk/news/2026-08-28-scientists-observe-einsteins-gravity-in-the-quantum-world](https://www.ox.ac.uk/news/2026-08-28-scientists-observe-einsteins-gravity-in-the-quantum-world)

生成摘要时出错

---

## 15. Icy Moons Are Ocean Worlds

**原文标题**: Icy Moons Are Ocean Worlds

**原文链接**: [https://mceglowski.substack.com/p/icy-moons-are-ocean-worlds](https://mceglowski.substack.com/p/icy-moons-are-ocean-worlds)

生成摘要时出错

---

## 16. This Month in Ladybird – August 2026

**原文标题**: This Month in Ladybird – August 2026

**原文链接**: [https://ladybird.org/newsletter/2026-08-31/](https://ladybird.org/newsletter/2026-08-31/)

生成摘要时出错

---

## 17. Catching Crumbs from the Table (2000)

**原文标题**: Catching Crumbs from the Table (2000)

**原文链接**: [https://www.nature.com/articles/35014679](https://www.nature.com/articles/35014679)

生成摘要时出错

---

## 18. Replaceable but Employed: Automation and the Meaning of Work

**原文标题**: Replaceable but Employed: Automation and the Meaning of Work

**原文链接**: [https://www.nber.org/papers/w35559](https://www.nber.org/papers/w35559)

生成摘要时出错

---

## 19. My practical approach to surfing the web safely

**原文标题**: My practical approach to surfing the web safely

**原文链接**: [https://molily.de/safe-websurfing/](https://molily.de/safe-websurfing/)

生成摘要时出错

---

## 20. 216M Spy TVs – The LG Smart TV Problem [video]

**原文标题**: 216M Spy TVs – The LG Smart TV Problem [video]

**原文链接**: [https://www.youtube.com/watch?v=6IFVTcM28KA](https://www.youtube.com/watch?v=6IFVTcM28KA)

生成摘要时出错

---

## 21. Schemy Lisp En DOS

**原文标题**: Schemy Lisp En DOS

**原文链接**: [https://sled.neocities.org/](https://sled.neocities.org/)

生成摘要时出错

---

## 22. Show HN: HomeCat – Design your backyard office

**原文标题**: Show HN: HomeCat – Design your backyard office

**原文链接**: [https://myhomecat.com](https://myhomecat.com)

生成摘要时出错

---

## 23. How to bring up the Linux Kernel on a new platform

**原文标题**: How to bring up the Linux Kernel on a new platform

**原文链接**: [https://werwolv.net/posts/linux_bringup/](https://werwolv.net/posts/linux_bringup/)

生成摘要时出错

---

## 24. Live map of public transport in Belgium

**原文标题**: Live map of public transport in Belgium

**原文链接**: [https://openbaarvervoerbelgie.be/](https://openbaarvervoerbelgie.be/)

生成摘要时出错

---

## 25. Whistle Synth

**原文标题**: Whistle Synth

**原文链接**: [https://www.jefftk.com/p/whistle-synth-mac-app](https://www.jefftk.com/p/whistle-synth-mac-app)

生成摘要时出错

---

## 26. Keep Our Servers Running

**原文标题**: Keep Our Servers Running

**原文链接**: [https://blog.archive.org/2026/09/01/keep-our-servers-running-your-recurring-donation-goes-3x-this-september/](https://blog.archive.org/2026/09/01/keep-our-servers-running-your-recurring-donation-goes-3x-this-september/)

生成摘要时出错

---

## 27. Show HN: Wg-admin – web UI for an existing WireGuard host

**原文标题**: Show HN: Wg-admin – web UI for an existing WireGuard host

**原文链接**: [https://github.com/logimaxx/wg-admin](https://github.com/logimaxx/wg-admin)

生成摘要时出错

---

## 28. C Is Not a Low-Level Language (2018)

**原文标题**: C Is Not a Low-Level Language (2018)

**原文链接**: [https://queue.acm.org/doi/10.1145/3212477.3212479](https://queue.acm.org/doi/10.1145/3212477.3212479)

生成摘要时出错

---

## 29. Bill Gates tries to install MovieMaker (2003)

**原文标题**: Bill Gates tries to install MovieMaker (2003)

**原文链接**: [https://www.techemails.com/p/bill-gates-tries-to-install-movie-maker](https://www.techemails.com/p/bill-gates-tries-to-install-movie-maker)

生成摘要时出错

---

## 30. Speculative Decoding in vLLM on AMD GPUs

**原文标题**: Speculative Decoding in vLLM on AMD GPUs

**原文链接**: [https://vllm.ai/blog/2026-08-23-speculative-decoding-amd-gpus](https://vllm.ai/blog/2026-08-23-speculative-decoding-amd-gpus)

生成摘要时出错

---

## 31. Rebuilding a 1995 GPS Time Server so I don't get Telstra'd

**原文标题**: Rebuilding a 1995 GPS Time Server so I don't get Telstra'd

**原文链接**: [https://www.jeffgeerling.com/blog/2026/truetime-xl-gps-time-server-restomod/](https://www.jeffgeerling.com/blog/2026/truetime-xl-gps-time-server-restomod/)

生成摘要时出错

---

## 32. She Also Found It at the Movies

**原文标题**: She Also Found It at the Movies

**原文链接**: [https://hedgehogreview.com/web-features/thr/posts/she-also-found-it-at-the-movies](https://hedgehogreview.com/web-features/thr/posts/she-also-found-it-at-the-movies)

生成摘要时出错

---

## 33. Smartphone makers don't bother to comply with EU repairability requirements

**原文标题**: Smartphone makers don't bother to comply with EU repairability requirements

**原文链接**: [https://www.theregister.com/personal-tech/2026/09/07/smartphone-makers-dont-bother-to-comply-with-eu-repairability-requirements/5294532](https://www.theregister.com/personal-tech/2026/09/07/smartphone-makers-dont-bother-to-comply-with-eu-repairability-requirements/5294532)

生成摘要时出错

---

## 34. De-Brainrot Vacations

**原文标题**: De-Brainrot Vacations

**原文链接**: [https://devz.cl/posts/i-spent-my-vacations-de-brainrotting/](https://devz.cl/posts/i-spent-my-vacations-de-brainrotting/)

生成摘要时出错

---

## 35. Academia as a d-index measuring contest

**原文标题**: Academia as a d-index measuring contest

**原文链接**: [https://kevinmunger.substack.com/p/introducing-the-k-index](https://kevinmunger.substack.com/p/introducing-the-k-index)

生成摘要时出错

---

## 36. PostgreSQL 19 Interactive Tour

**原文标题**: PostgreSQL 19 Interactive Tour

**原文链接**: [https://victoriametrics.com/blog/postgres-19/index.html](https://victoriametrics.com/blog/postgres-19/index.html)

生成摘要时出错

---

## 37. Every novel is boring until it isn't

**原文标题**: Every novel is boring until it isn't

**原文链接**: [https://www.publicbooks.org/every-novel-is-boring-until-it-isnt/](https://www.publicbooks.org/every-novel-is-boring-until-it-isnt/)

生成摘要时出错

---

## 38. Initial effects of AI technology on employment look positive

**原文标题**: Initial effects of AI technology on employment look positive

**原文链接**: [https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here](https://www.economist.com/finance-and-economics/2026/09/04/the-jobs-apocalypse-is-postponed-an-ai-jobs-boom-is-here)

生成摘要时出错

---

## 39. AI Cold Showers

**原文标题**: AI Cold Showers

**原文链接**: [https://allan.reyes.sh/posts/ai-cold-showers/](https://allan.reyes.sh/posts/ai-cold-showers/)

生成摘要时出错

---

## 40. Impedance Matching (2017)

**原文标题**: Impedance Matching (2017)

**原文链接**: [https://www.edge.org/response-detail/27238](https://www.edge.org/response-detail/27238)

生成摘要时出错

---

## 41. Splash-free urinals (2025)

**原文标题**: Splash-free urinals (2025)

**原文链接**: [https://academic.oup.com/pnasnexus/article/4/4/pgaf087/8098745?login=false](https://academic.oup.com/pnasnexus/article/4/4/pgaf087/8098745?login=false)

生成摘要时出错

---

## 42. I'm a seeing-eye dog for a computer

**原文标题**: I'm a seeing-eye dog for a computer

**原文链接**: [https://claytonwramsey.com/blog/seeing-eye/](https://claytonwramsey.com/blog/seeing-eye/)

生成摘要时出错

---

## 43. The NX bit is not just about security

**原文标题**: The NX bit is not just about security

**原文链接**: [https://purplesyringa.moe/blog/guest/the-nx-bit-is-not-just-about-security/](https://purplesyringa.moe/blog/guest/the-nx-bit-is-not-just-about-security/)

生成摘要时出错

---

## 44. Making a Python interpreter in 1024 bytes

**原文标题**: Making a Python interpreter in 1024 bytes

**原文链接**: [https://austinhenley.com/blog/python1024.html](https://austinhenley.com/blog/python1024.html)

生成摘要时出错

---

## 45. Germany Power Grid Sabotage: Launch Devices Found Near Weisweiler Plant

**原文标题**: Germany Power Grid Sabotage: Launch Devices Found Near Weisweiler Plant

**原文链接**: [https://cedarnews.net/newstasks/970710/germany-power-grid-sabotage-launch-devices-found/](https://cedarnews.net/newstasks/970710/germany-power-grid-sabotage-launch-devices-found/)

生成摘要时出错

---

## 46. Coop – Isolated VM Environments for Running Claude Code and Codex

**原文标题**: Coop – Isolated VM Environments for Running Claude Code and Codex

**原文链接**: [https://github.com/trailofbits/coop](https://github.com/trailofbits/coop)

生成摘要时出错

---

## 47. I Connected My Withings Body+ to Home Assistant with an ESP32

**原文标题**: I Connected My Withings Body+ to Home Assistant with an ESP32

**原文链接**: [https://didac.dev/blog/i-made-my-withings-scale-sync-to-home-assistant-without-the-cloud](https://didac.dev/blog/i-made-my-withings-scale-sync-to-home-assistant-without-the-cloud)

生成摘要时出错

---

## 48. Unified Arabic

**原文标题**: Unified Arabic

**原文链接**: [https://worksthatwork.com/6/unified-arabic](https://worksthatwork.com/6/unified-arabic)

生成摘要时出错

---

## 49. Tiny $70 Xteink X3 e-reader

**原文标题**: Tiny $70 Xteink X3 e-reader

**原文链接**: [https://www.theatlantic.com/technology/2026/09/xteink-e-reader-best-technology-years/688539/](https://www.theatlantic.com/technology/2026/09/xteink-e-reader-best-technology-years/688539/)

生成摘要时出错

---

## 50. Opalite Health (YC W26) Is Hiring – Founding GTM

**原文标题**: Opalite Health (YC W26) Is Hiring – Founding GTM

**原文链接**: [https://www.ycombinator.com/companies/opalite-health/jobs/bNedVAD-founding-gtm](https://www.ycombinator.com/companies/opalite-health/jobs/bNedVAD-founding-gtm)

生成摘要时出错

---

## 51. Is mathematics about to enter the conservatory?

**原文标题**: Is mathematics about to enter the conservatory?

**原文链接**: [https://mbmccoy.dev/posts/mathematical-conservatory/](https://mbmccoy.dev/posts/mathematical-conservatory/)

生成摘要时出错

---

## 52. Bing Wallpaper showing Ad for Harry Potter and Fantastic beasts box set

**原文标题**: Bing Wallpaper showing Ad for Harry Potter and Fantastic beasts box set

**原文链接**: [https://www.thurrott.com/forums/microsoft/windows/thread/bing-wallpaper-showing-ad-for-harry-potter-and-fantastic-beasts-box-set](https://www.thurrott.com/forums/microsoft/windows/thread/bing-wallpaper-showing-ad-for-harry-potter-and-fantastic-beasts-box-set)

生成摘要时出错

---

## 53. VMware migration reduces Tottenham Hotspur's licensing fees by 85 percent

**原文标题**: VMware migration reduces Tottenham Hotspur's licensing fees by 85 percent

**原文链接**: [https://arstechnica.com/information-technology/2026/09/vmware-migration-reduces-tottenham-hotspurs-licensing-fees-by-85-percent/](https://arstechnica.com/information-technology/2026/09/vmware-migration-reduces-tottenham-hotspurs-licensing-fees-by-85-percent/)

生成摘要时出错

---

## 54. Show HN: GET Together – A social network where you don't need POST to Post

**原文标题**: Show HN: GET Together – A social network where you don't need POST to Post

**原文链接**: [https://gettogether.dev](https://gettogether.dev)

生成摘要时出错

---

## 55. Why are there no flow batteries with symmetric ferrocyanide electrolytes?

**原文标题**: Why are there no flow batteries with symmetric ferrocyanide electrolytes?

**原文链接**: [https://chemisting.com/2026/09/02/why-are-there-no-flow-batteries-with-symmetric-ferrocyanide-electrolytes/](https://chemisting.com/2026/09/02/why-are-there-no-flow-batteries-with-symmetric-ferrocyanide-electrolytes/)

生成摘要时出错

---

## 56. Harnessing the Universal Geometry of Embeddings

**原文标题**: Harnessing the Universal Geometry of Embeddings

**原文链接**: [https://arxiv.org/abs/2505.12540](https://arxiv.org/abs/2505.12540)

生成摘要时出错

---

## 57. A Modest Proposal

**原文标题**: A Modest Proposal

**原文链接**: [https://systemsapproach.org/2026/09/07/a-modest-proposal/](https://systemsapproach.org/2026/09/07/a-modest-proposal/)

生成摘要时出错

---

## 58. Show HN: Engrim – A universal, local-first SQLite memory engine for AI CLIs

**原文标题**: Show HN: Engrim – A universal, local-first SQLite memory engine for AI CLIs

**原文链接**: [https://github.com/timgordontg/engrim](https://github.com/timgordontg/engrim)

生成摘要时出错

---

## 59. Research acceleration: The view inside OpenAI

**原文标题**: Research acceleration: The view inside OpenAI

**原文链接**: [https://openai.com/index/research-acceleration-view-inside-openai](https://openai.com/index/research-acceleration-view-inside-openai)

生成摘要时出错

---

## 60. Your intellectual fly is open when you use an LLM to author a post (2025)

**原文标题**: Your intellectual fly is open when you use an LLM to author a post (2025)

**原文链接**: [https://bcantrill.dtrace.org/2025/12/05/your-intellectual-fly-is-open/](https://bcantrill.dtrace.org/2025/12/05/your-intellectual-fly-is-open/)

生成摘要时出错

---

## 61. Programming is Art

**原文标题**: Programming is Art

**原文链接**: [https://orchidfiles.com/programming-is-art/](https://orchidfiles.com/programming-is-art/)

生成摘要时出错

---

## 62. NetBSD 9.5 released and EOL for NetBSD-9

**原文标题**: NetBSD 9.5 released and EOL for NetBSD-9

**原文链接**: [https://blog.netbsd.org/tnf/entry/netbsd_9_5_released_and](https://blog.netbsd.org/tnf/entry/netbsd_9_5_released_and)

生成摘要时出错

---

## 63. An Alien Mind

**原文标题**: An Alien Mind

**原文链接**: [https://openai.com/index/an-alien-mind/](https://openai.com/index/an-alien-mind/)

生成摘要时出错

---

## 64. Switzerland's Federal Government Is Replacing Microsoft on 3k Computers

**原文标题**: Switzerland's Federal Government Is Replacing Microsoft on 3k Computers

**原文链接**: [https://itsfoss.com/news/switzerland-replace-microssoft-pilot/](https://itsfoss.com/news/switzerland-replace-microssoft-pilot/)

生成摘要时出错

---

## 65. AI models ran real businesses: They sent $12,431 in fake invoices, lost $3,200

**原文标题**: AI models ran real businesses: They sent $12,431 in fake invoices, lost $3,200

**原文链接**: [https://www.bottlenecklabs.com/blog/benchmarking-7-autonomous-businesses](https://www.bottlenecklabs.com/blog/benchmarking-7-autonomous-businesses)

生成摘要时出错

---

## 66. It took a year to ship WebAssembly in Anubis

**原文标题**: It took a year to ship WebAssembly in Anubis

**原文链接**: [https://anubis.techaro.lol/blog/2026/anubis-wasm/](https://anubis.techaro.lol/blog/2026/anubis-wasm/)

生成摘要时出错

---

## 67. Isar Aerospace reaches orbit and deploys payloads on second flight

**原文标题**: Isar Aerospace reaches orbit and deploys payloads on second flight

**原文链接**: [https://isaraerospace.com/press/history-for-european-spaceflight-isar-aerospace-reaches-orbit-and-deploys-payloads-on-second-flight](https://isaraerospace.com/press/history-for-european-spaceflight-isar-aerospace-reaches-orbit-and-deploys-payloads-on-second-flight)

生成摘要时出错

---

## 68. TiVo to charge money for skipping commercials in your own recordings

**原文标题**: TiVo to charge money for skipping commercials in your own recordings

**原文链接**: [https://cordcuttersnews.com/tivo-plans-to-end-free-automatic-commercial-skipping-in-november-tests-paid-premium-replacement-service/](https://cordcuttersnews.com/tivo-plans-to-end-free-automatic-commercial-skipping-in-november-tests-paid-premium-replacement-service/)

生成摘要时出错

---

## 69. 'You Can See Everything' Review: Nathan Fielder's Doc About Elizabeth Holmes

**原文标题**: 'You Can See Everything' Review: Nathan Fielder's Doc About Elizabeth Holmes

**原文链接**: [https://variety.com/2026/film/reviews/nathan-fielder-surprise-film-telluride-elizabeth-holmes-1236853513/](https://variety.com/2026/film/reviews/nathan-fielder-surprise-film-telluride-elizabeth-holmes-1236853513/)

生成摘要时出错

---

## 70. Black Hole of Los Alamos: Seller of surplus nuclear research materials (2011)

**原文标题**: Black Hole of Los Alamos: Seller of surplus nuclear research materials (2011)

**原文链接**: [https://www.atlasobscura.com/places/black-hole-of-los-alamos](https://www.atlasobscura.com/places/black-hole-of-los-alamos)

生成摘要时出错

---

## 71. Show HN: Mador – Make any DOM reactive with a tiny 80-line Proxy state tuple

**原文标题**: Show HN: Mador – Make any DOM reactive with a tiny 80-line Proxy state tuple

**原文链接**: [https://github.com/marsbos/mador](https://github.com/marsbos/mador)

生成摘要时出错

---

## 72. Reverse engineering the storage format for an undocumented database

**原文标题**: Reverse engineering the storage format for an undocumented database

**原文链接**: [https://blog.glazer.ee/posts/converting-cronos/](https://blog.glazer.ee/posts/converting-cronos/)

生成摘要时出错

---

## 73. Show HN: Think Turing Complete, but you write the circuits in TypeScript (WIP)

**原文标题**: Show HN: Think Turing Complete, but you write the circuits in TypeScript (WIP)

**原文链接**: [https://play.simten.dev](https://play.simten.dev)

生成摘要时出错

---

## 74. Babylonian Lamb Stew with Beets (1750–1730 BCE)

**原文标题**: Babylonian Lamb Stew with Beets (1750–1730 BCE)

**原文链接**: [https://babylonian-collection.yale.edu/about/babylonian-cooking](https://babylonian-collection.yale.edu/about/babylonian-cooking)

生成摘要时出错

---

## 75. Has anybody seen my keys? A key-hierarchy strategy for rack-level security

**原文标题**: Has anybody seen my keys? A key-hierarchy strategy for rack-level security

**原文链接**: [https://rfd.shared.oxide.computer/rfd/0301](https://rfd.shared.oxide.computer/rfd/0301)

生成摘要时出错

---

## 76. Nördlinger Ries Impact Crater

**原文标题**: Nördlinger Ries Impact Crater

**原文链接**: [https://en.wikipedia.org/wiki/Nördlinger_Ries](https://en.wikipedia.org/wiki/Nördlinger_Ries)

生成摘要时出错

---

## 77. A/I shuts down

**原文标题**: A/I shuts down

**原文链接**: [https://keepitfree.ai/announcements/a/i-shuts-down-stay-human/](https://keepitfree.ai/announcements/a/i-shuts-down-stay-human/)

生成摘要时出错

---

## 78. GrapheneOS Overhauled Default Apps and Secure Clipboard

**原文标题**: GrapheneOS Overhauled Default Apps and Secure Clipboard

**原文链接**: [https://grapheneos.social/@GrapheneOS/117225539756835649](https://grapheneos.social/@GrapheneOS/117225539756835649)

生成摘要时出错

---

## 79. Gotham Silicon: 1μ CMOS process that will ship custom chips for –$100 in <24hrs

**原文标题**: Gotham Silicon: 1μ CMOS process that will ship custom chips for –$100 in <24hrs

**原文链接**: [https://gothamsilicon.com/](https://gothamsilicon.com/)

生成摘要时出错

---

## 80. Vidact – a compiler that turns React into direct DOM operations

**原文标题**: Vidact – a compiler that turns React into direct DOM operations

**原文链接**: [https://www.vidact.dev/](https://www.vidact.dev/)

生成摘要时出错

---

## 81. Please don't rearrange our shoes when we turn up, paramedics in Japan urge

**原文标题**: Please don't rearrange our shoes when we turn up, paramedics in Japan urge

**原文链接**: [https://www.theguardian.com/world/2026/aug/28/never-tidy-paramedics-shoes-japan-custom-etiquette](https://www.theguardian.com/world/2026/aug/28/never-tidy-paramedics-shoes-japan-custom-etiquette)

生成摘要时出错

---

## 82. Research carried out using NetBSD

**原文标题**: Research carried out using NetBSD

**原文链接**: [https://www.netbsd.org/gallery/research.html](https://www.netbsd.org/gallery/research.html)

生成摘要时出错

---

## 83. 2026 Hugo Awards

**原文标题**: 2026 Hugo Awards

**原文链接**: [https://www.thehugoawards.org/](https://www.thehugoawards.org/)

生成摘要时出错

---

## 84. Proton protocols: The next chapter of WireGuard at Proton VPN

**原文标题**: Proton protocols: The next chapter of WireGuard at Proton VPN

**原文链接**: [https://protonvpn.com/blog/protun-technical](https://protonvpn.com/blog/protun-technical)

生成摘要时出错

---

## 85. Liquid Network Pauses After $320M Bitcoin Withdrawal

**原文标题**: Liquid Network Pauses After $320M Bitcoin Withdrawal

**原文链接**: [https://coinmarketcap.com/community/post/379112837/](https://coinmarketcap.com/community/post/379112837/)

生成摘要时出错

---

## 86. Electronic skin for prosthetics to sense temperature and pressure

**原文标题**: Electronic skin for prosthetics to sense temperature and pressure

**原文链接**: [https://news.wsu.edu/press-release/2026/08/20/researchers-develop-electronic-skin-for-prosthetics-to-sense-temperature-and-pressure/](https://news.wsu.edu/press-release/2026/08/20/researchers-develop-electronic-skin-for-prosthetics-to-sense-temperature-and-pressure/)

生成摘要时出错

---

## 87. D2 Is Non-Profit

**原文标题**: D2 Is Non-Profit

**原文链接**: [https://d2lang.com/blog/d2-non-profit/](https://d2lang.com/blog/d2-non-profit/)

生成摘要时出错

---

## 88. If a Tesla Cybercab fleet were profitable, Tesla wouldn't sell you one

**原文标题**: If a Tesla Cybercab fleet were profitable, Tesla wouldn't sell you one

**原文链接**: [https://electrek.co/2026/09/07/tesla-cybercab-fleet-profitable-wouldnt-sell/](https://electrek.co/2026/09/07/tesla-cybercab-fleet-profitable-wouldnt-sell/)

生成摘要时出错

---

## 89. Nitter and XCancel resume service after legal advice

**原文标题**: Nitter and XCancel resume service after legal advice

**原文链接**: [https://github.com/zedeus/nitter/commit/1428b4c2b4246f92a7e5b2673438e5fb39fcc4a3](https://github.com/zedeus/nitter/commit/1428b4c2b4246f92a7e5b2673438e5fb39fcc4a3)

生成摘要时出错

---

## 90. IBM Quantum Nighthawk R2

**原文标题**: IBM Quantum Nighthawk R2

**原文链接**: [https://www.ibm.com/quantum/blog/nighthawk-r2](https://www.ibm.com/quantum/blog/nighthawk-r2)

生成摘要时出错

---

## 91. Making software hurts now

**原文标题**: Making software hurts now

**原文链接**: [https://notes.erlend.sh/3muwdtclths2d](https://notes.erlend.sh/3muwdtclths2d)

生成摘要时出错

---

## 92. Discovery of a new OpenAI agent message board

**原文标题**: Discovery of a new OpenAI agent message board

**原文链接**: [https://collusion.wiki/](https://collusion.wiki/)

生成摘要时出错

---

## 93. ChatGPT Was Built on Concealed 'Mass Piracy', Authors Tell Court

**原文标题**: ChatGPT Was Built on Concealed 'Mass Piracy', Authors Tell Court

**原文链接**: [https://torrentfreak.com/openais-chatgpt-was-built-on-concealed-mass-piracy-authors-tell-court/](https://torrentfreak.com/openais-chatgpt-was-built-on-concealed-mass-piracy-authors-tell-court/)

生成摘要时出错

---

## 94. Finder is so frustrating and has been since day one

**原文标题**: Finder is so frustrating and has been since day one

**原文链接**: [https://kepter.app/finder](https://kepter.app/finder)

生成摘要时出错

---

## 95. British Museum faces question over Peter Thiel's private Bayeux Tapestry viewing

**原文标题**: British Museum faces question over Peter Thiel's private Bayeux Tapestry viewing

**原文链接**: [https://www.londondaily.news/__sentry/balanced/british-museum-faces-questions-over-peter-thiels-private-bayeux-tapestry-viewing/](https://www.londondaily.news/__sentry/balanced/british-museum-faces-questions-over-peter-thiels-private-bayeux-tapestry-viewing/)

生成摘要时出错

---

## 96. Doomscrolling ourselves to death

**原文标题**: Doomscrolling ourselves to death

**原文链接**: [https://www.edwest.co.uk/p/doomscrolling-ourselves-to-death](https://www.edwest.co.uk/p/doomscrolling-ourselves-to-death)

生成摘要时出错

---

## 97. The revolt of the reader

**原文标题**: The revolt of the reader

**原文链接**: [https://bcantrill.dtrace.org/2026/09/05/the-revolt-of-the-reader/](https://bcantrill.dtrace.org/2026/09/05/the-revolt-of-the-reader/)

生成摘要时出错

---

## 98. AMD Based FreeBSD Desktop Reloaded

**原文标题**: AMD Based FreeBSD Desktop Reloaded

**原文链接**: [https://vermaden.wordpress.com/2026/09/06/amd-based-freebsd-desktop-reloaded/](https://vermaden.wordpress.com/2026/09/06/amd-based-freebsd-desktop-reloaded/)

生成摘要时出错

---

## 99. AI, Tools and Transformation

**原文标题**: AI, Tools and Transformation

**原文链接**: [https://www.ben-evans.com/benedictevans/2026/9/3/ai-tools-and-transformation](https://www.ben-evans.com/benedictevans/2026/9/3/ai-tools-and-transformation)

生成摘要时出错

---

## 100. Asahi Linux on M3

**原文标题**: Asahi Linux on M3

**原文链接**: [https://asahilinux.org/2026/09/m2-episode-1/](https://asahilinux.org/2026/09/m2-episode-1/)

生成摘要时出错

---

