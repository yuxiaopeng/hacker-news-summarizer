# Hacker News 热门文章摘要 (2026-01-08)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Bose 开源旧款智能音箱，而非将其变砖。

**原文标题**: Bose is open-sourcing its old smart speakers instead of bricking them

**原文链接**: [https://www.theverge.com/news/858501/bose-soundtouch-smart-speakers-open-source](https://www.theverge.com/news/858501/bose-soundtouch-smart-speakers-open-source)

Bose针对其老旧的SoundTouch智能音箱宣布了一项利好消费者的策略：在官方云端支持结束时，将选择开源设备的API文档，而非让其“变砖”。为了给用户预留更多的过渡时间，公司还将停止支持的日期从原定的2月18日推迟至2026年5月6日。

一旦云服务停用，SoundTouch应用程序的最终更新将使音箱转为本地控制。这一转变确保了用户仍能通过蓝牙、AirPlay、Spotify Connect以及物理AUX连接来串流音乐。包括音箱分组、遥控功能和设备设置在内的核心功能也将维持正常运作。

通过开源API，Bose允许社区开发自定义工具和第三方集成，以弥补云端功能的缺失。这一举措在科技行业殊为罕见，因为在通常情况下，一旦制造商停止支持后端服务器，相关产品便会沦为电子垃圾。Bose并未让功能尚好的硬件就此报废，而是通过本地连接和社区驱动的支持，为SoundTouch系列赋予了“第二次生命”。

---

## 2. Jeff Dean 事实

**原文标题**: The Jeff Dean Facts

**原文链接**: [https://github.com/LRitzdorf/TheJeffDeanFacts](https://github.com/LRitzdorf/TheJeffDeanFacts)

“Jeff Dean Facts”是一个精选的程序员幽默库，围绕 Google 高级会士 Jeff Dean 传奇般的技术实力展开。受到“查克·诺里斯真相（Chuck Norris facts）”梗的启发，这些笑话通过夸张的讽刺将 Dean 的编程能力描述为超人类。例子包括声称他能在白板上解决 NP 完全问题，优化光速，以及编写 O(1/n) 复杂度的算法。

该库的创建是为了保存这些文化产物，因为许多原始来源（如 Quora 和 Google+ 帖子）已开始消失。虽然大多数条目是涉及 Google 基础架构（如 MapReduce 和 Bigtable）或基础计算机科学概念的荒谬夸张，但也有少数被标注为“(TRUE)”。这些包括：Dean 在 10 级职级体系中被晋升为 11 级，以及世界著名的计算机科学家高德纳（Donald Knuth）不得不坐在地板上听他演讲。

最终，这篇文章既是特定网络民俗的存档，也是对 Dean 对现代计算产生重大现实影响的致敬。该集合涵盖了广泛的技术主题，从编译原理和二进制可读性到硬件优化和算法复杂度，一切都通过 Dean 神话般的效率视角呈现。

---

## 3. Lights and Shadows (2020)

**原文标题**: Lights and Shadows (2020)

**原文链接**: [https://ciechanow.ski/lights-and-shadows/](https://ciechanow.ski/lights-and-shadows/)

《光与影》是一篇关于光如何与表面相互作用并产生日常视觉效果的技术探讨。本文将光照物理学分解为以下几个核心原理：

**功率与感知**
光源的亮度由其功率（以瓦特为单位）决定。然而，人类视觉系统对亮度的感知是非线性的；低功率水平下的变化比高功率水平下等量的增量要明显得多。

**阴影几何学**
哑光表面的阴影受两个主要因素支配：
1. **余弦定律：** 辐照度（照射到表面上的光功率）与入射角的余弦成正比。当光源相对于表面向水平方向移动时，光线会散布在更大的面积上，使表面看起来更暗。
2. **平方反比定律：** 对于小型光源，光强随距离的平方成比例下降。随着光线传播得更远，其能量会在不断扩大的球形区域内稀释。

**角度与辐射亮度**
为了解释复杂的光源，作者引入了**立体角**（单位为球面度），用于量化物体占据视野的比例。通过使用**投影立体角**，可以同时考虑光源的大小和角度，从而计算出一个点的亮度。

最后，文章区分了表面感知与光源感知的不同。虽然表面的外观会随距离增加而变暗，但**朗伯发射体**（如太阳）无论距离或观察角度如何，都保持恒定的**辐射亮度**（感知亮度）。这是因为远距离下到达眼睛的光功率虽然减少了，但恰好被眼睛感受器捕捉到的光源表面积的增加所完美抵消。

---

## 4. 帕秋莉项目：开源电磁数位板硬件

**原文标题**: Project Patchouli: Open-source electromagnetic drawing tablet hardware

**原文链接**: [https://patchouli.readthedocs.io/en/latest/](https://patchouli.readthedocs.io/en/latest/)

**Project Patchouli** 是一个致力于电磁共振（EMR）数位板硬件实现和全面文档编制的开源项目。该项目提供了一个完整的框架，包括线圈阵列、由现成组件构建的射频（RF）前端以及数字信号处理（DSP）算法，旨在实现超低延迟的压感笔输入。

该项目的一个核心特性是广泛兼容各厂商的商用压感笔。除了硬件设计，Project Patchouli 还作为一个教育资源，提供有关 EMR 机制、电路实现以及不同制造商特定笔协议的详细文档。

**关键信息：**
*   **时间线：** 项目于 2024 年 1 月启动，2024 年 3 月成功测试首个硬件原型，并于 2025 年 1 月在 Read the Docs 上线文档。
*   **支持：** 由项目负责人 **Yukidama** 领导，并获得 **NLnet 基金会 NGI Zero Core 基金**的资助。
*   **许可协议：** 项目采用分级开源模式：
    *   **文档：** 知识共享署名 4.0 (CC BY 4.0)。
    *   **硬件设计：** CERN 开源硬件许可证 (CERN-OHL-S)。
    *   **程序代码：** GNU 通用公共许可证 v3 (GPLv3)。

目前项目正处于积极开发阶段，源代码和硬件设计均可在 GitLab 上获取。社区成员可以通过公开的 Discord 服务器或直接发送电子邮件进行交流。

---

## 5. Show HN：具有时间一致性的视频版 DeepDream

**原文标题**: Show HN: DeepDream for Video with Temporal Consistency

**原文链接**: [https://github.com/jeremicna/deepdream-video-pytorch](https://github.com/jeremicna/deepdream-video-pytorch)

**DeepDream-video-pytorch** 是 `neural-dream` 项目的一个基于 PyTorch 的分支，专门旨在将 DeepDream 视觉效果应用于视频，同时保持时间一致性。

标准的 DeepDream 实现通常独立处理每一帧视频，导致显著的闪烁感。该分支通过引入 **RAFT 光流 (Optical Flow)** 和 **遮挡掩膜 (occlusion masking)** 解决了这一问题。通过将前一帧的“梦境”效果映射到当前帧，该软件确保了视觉效果能够平滑地追踪移动物体。遮挡掩膜通过检测物体重叠进一步优化了处理过程，从而防止出现“重影”伪影。

**主要功能与用法：**
*   **视频处理：** 通过使用 `video_dream.py` 脚本，用户可以使用 `-blend`（平衡原始内容与视觉效果）和 `-independent`（切换是否开启基于流的一致性）等参数来处理视频。
*   **高效性：** 由于时间流允许每一帧在上一帧的基础上进行构建，作者建议每帧仅使用**一次迭代**。这加快了视频处理速度，并防止效果过度饱和。
*   **自定义：** 该工具继承了所有标准的 DeepDream 选项，包括特定层选择、多尺度缩放 (octave scaling) 和拉普拉斯金字塔。
*   **性能：** 支持 CUDA (NVIDIA)、MPS (Apple Silicon) 以及多 GPU 配置。为避免“显存溢出”错误，用户可以使用 cuDNN 后端或降低图像分辨率。

该项目提供了对比演示（如绿头鸭和公路素材），展示了闪烁的独立帧处理与通过光流实现的平滑一致结果之间的鲜明对比。

---

## 6. 深入探究委内瑞拉的一起 BGP 异常

**原文标题**: A closer look at a BGP anomaly in Venezuela

**原文链接**: [https://blog.cloudflare.com/bgp-route-leak-venezuela/](https://blog.cloudflare.com/bgp-route-leak-venezuela/)

Cloudflare 对 2026 年 1 月 2 日委内瑞拉 BGP 异常的分析表明，国有 ISP CANTV (AS8048) 发生的大规模路由泄露很可能是技术管理不善的结果，而非政府的蓄意破坏。尽管该事件发生时恰逢美国逮捕尼古拉斯·马杜罗，但 Cloudflare 的数据指出，这次泄露更多是“寻常疏忽”而非“阴谋诡计”。

此次事件涉及一种“1 型发卡式”路由泄露，即 AS8048 从一家供应商（Sparkle/AS6762）获取路由，并将其重新分发给另一家供应商（V.tal/AS52320）。Cloudflare 基于以下原因反驳了恶意的“中间人攻击”理论：
1. **行为模式**：AS8048 长期存在路由操作不当的问题，自 2025 年 12 月以来已记录了 11 次类似的泄露。
2. **缺乏动机**：AS8048 本就是受影响网络（Dayco Telecom）的上游供应商，这意味着他们原本就能接触到被指控“拦截”的流量。
3. **技术线索**：泄露的路由经过了大量的“路径前置”（prepended）处理，故意降低了路径吸引力，这与旨在劫持流量的恶意行为者的目标背道而驰。

文章强调了当前互联网安全的一个关键漏洞：虽然 RPKI 路由起源验证 (ROV) 可以防止 IP 地址劫持，但它无法阻止此类基于路径的异常。为了防止未来的泄露，作者主张采用自治系统提供商授权 (ASPA) 和 RFC9234 标准，以为 BGP 关系建立正式的角色定义。

最后，文章总结认为，委内瑞拉的异常是历来建立在信任基础上的 BGP 系统所产生的意外副作用，并强调全球有必要采纳路径验证标准，以确保互联网的安全性。

---

## 7. Tamarind Bio (YC W24) 招聘基础架构工程师

**原文标题**: Tamarind Bio (YC W24) Is Hiring Infrastructure Engineers

**原文链接**: [https://www.ycombinator.com/companies/tamarind-bio/jobs/HPRZAz3-infrastructure-engineer](https://www.ycombinator.com/companies/tamarind-bio/jobs/HPRZAz3-infrastructure-engineer)

Tamarind Bio 是一家由 Y Combinator 支持（W24）的初创公司，目前正在招聘一名**基础设施工程师**，以扩展其机器学习推理平台。公司总部位于旧金山，提供计算生物学工具，帮助科学家利用人工智能进行药物研发、蛋白质设计和分子工程。

**职位描述**
基础设施工程师将领导一个支持超过 150 个生物机器学习模型的系统扩展工作。主要职责包括：
*   构建并维护基础设施，以满足快速增长的需求。
*   使用 Kubernetes 编排容器化工作负载。
*   优化资源分配，并管理针对不可预测的生物机器学习任务的 GPU 工作负载。
*   确保系统的高可用性，并随公司发展推动系统演进。

**应聘要求**
*   **经验：** 欢迎各种经验水平的人士，包括应届毕业生。
*   **技能：** 具备出色的编程和自动化能力，熟悉容器化技术，并拥有主流云平台（AWS、GCP 或 Azure）的使用经验。
*   **优先条件：** 具有生产环境扩展、基础设施即代码（Terraform/Pulumi）以及监控/可观测性工具的使用经验。
*   **工作地点：** 必须位于旧金山湾区或愿意搬迁至此，要求每周五天实地办公。

**薪酬福利**
*   **年薪：** 180,000 美元 – 250,000 美元。
*   **股权：** 0.50% – 1.00%。

**关于 Tamarind Bio**
Tamarind Bio 由 Deniz Kavi 和 Sherry Liu 创立，旨在推动人工智能在制药研究中的普及。其平台简化了复杂 AI 模型的部署和扩展，而在新型药物和酶的设计中，这些模型正在日益取代传统的基于物理的工具。目前团队规模约 10 人。

---

## 8. I used Lego to design a farm for people who are blind – like me

**原文标题**: I used Lego to design a farm for people who are blind – like me

**原文链接**: [https://www.bbc.co.uk/news/articles/c4g4zlyqnr0o](https://www.bbc.co.uk/news/articles/c4g4zlyqnr0o)

生成摘要时出错

---

## 9. Open Infrastructure Map

**原文标题**: Open Infrastructure Map

**原文链接**: [https://openinframap.org](https://openinframap.org)

生成摘要时出错

---

## 10. Japanese electronics store pleads for old PCs amid ongoing hardware shortage

**原文标题**: Japanese electronics store pleads for old PCs amid ongoing hardware shortage

**原文链接**: [https://www.tomshardware.com/desktops/pc-building/major-japanese-electronics-store-begs-customers-for-their-old-pcs-as-hardware-drought-continues-we-pretty-much-buy-any-pc-pleads-the-akihabara-outlet](https://www.tomshardware.com/desktops/pc-building/major-japanese-electronics-store-begs-customers-for-their-old-pcs-as-hardware-drought-continues-we-pretty-much-buy-any-pc-pleads-the-akihabara-outlet)

东京秋叶原地区的大型电子零售商 Sofmap Gaming 因库存严重短缺，正紧急呼吁客户出售其二手 PC 硬件。据报道，该店货架已近乎清空，目前正以高价回购几乎任何功能正常的台式机或笔记本电脑，无论其是高端游戏主机还是标准办公电脑。

这场“硬件荒”的主要推手是全球范围内剧烈的内存供应紧张。AI 数据中心开发者对内存（RAM）“永不满足”的需求导致供应从消费市场分流，引发零售价格飙升。例如，文中提到某些在 2025 年底售价为 66 美元的 DDR5 内存套件已暴涨至 235 美元——涨幅超过 3.5 倍。

这种短缺正在整个 PC 行业引发连锁反应：
*   **成本上升：** 预装 PC 的价格不断上涨，且高显存显卡面临供应限制。
*   **生产转型：** 零部件制造商正重新转向支持 DDR4 的主板，以便为装机用户提供更实惠的选择。
*   **二手市场压力：** 消费者需求已大幅转向二手市场。虽然零售商通常寻求符合 Windows 11 系统要求（英特尔第八代/锐龙 2000 系列或更高版本）的硬件，但即便更老旧的机器现在也变得颇具价值。

报告强调了市场中“旧物成金”的重大转变，在持续的 AI 驱动型硬件挤压下，零售商正竭力为消费者提供价格合理的选择。

---

## 11. The Waymo Ojai Will Soon Offer Autonomous Rides Around the U.S.

**原文标题**: The Waymo Ojai Will Soon Offer Autonomous Rides Around the U.S.

**原文链接**: [https://www.caranddriver.com/news/a69938250/waymo-ojai-autonomous-robotaxi-details/](https://www.caranddriver.com/news/a69938250/waymo-ojai-autonomous-robotaxi-details/)

生成摘要时出错

---

## 12. Kernel bugs hide for 2 years on average. Some hide for 20

**原文标题**: Kernel bugs hide for 2 years on average. Some hide for 20

**原文链接**: [https://pebblebed.com/blog/kernel-bugs](https://pebblebed.com/blog/kernel-bugs)

生成摘要时出错

---

## 13. Eat Real Food

**原文标题**: Eat Real Food

**原文链接**: [https://realfood.gov](https://realfood.gov)

生成摘要时出错

---

## 14. The price of fame? Mortality risk among famous singers

**原文标题**: The price of fame? Mortality risk among famous singers

**原文链接**: [https://jech.bmj.com/content/early/2025/11/30/jech-2025-224589](https://jech.bmj.com/content/early/2025/11/30/jech-2025-224589)

生成摘要时出错

---

## 15. The Napoleon Technique: Postponing things to increase productivity

**原文标题**: The Napoleon Technique: Postponing things to increase productivity

**原文链接**: [https://effectiviology.com/napoleon/](https://effectiviology.com/napoleon/)

生成摘要时出错

---

## 16. Iran Goes Into IPv6 Blackout

**原文标题**: Iran Goes Into IPv6 Blackout

**原文链接**: [https://radar.cloudflare.com/routing/ir](https://radar.cloudflare.com/routing/ir)

生成摘要时出错

---

## 17. Shipmap.org

**原文标题**: Shipmap.org

**原文链接**: [https://www.shipmap.org/](https://www.shipmap.org/)

生成摘要时出错

---

## 18. ICE's Tool to Monitor Phones in Neighborhoods

**原文标题**: ICE's Tool to Monitor Phones in Neighborhoods

**原文链接**: [https://www.404media.co/inside-ices-tool-to-monitor-phones-in-entire-neighborhoods/](https://www.404media.co/inside-ices-tool-to-monitor-phones-in-entire-neighborhoods/)

生成摘要时出错

---

## 19. Signals vs. Query-Based Compilers

**原文标题**: Signals vs. Query-Based Compilers

**原文链接**: [https://marvinh.dev/blog/signals-vs-query-based-compilers/](https://marvinh.dev/blog/signals-vs-query-based-compilers/)

生成摘要时出错

---

## 20. Go.sum is not a lockfile

**原文标题**: Go.sum is not a lockfile

**原文链接**: [https://words.filippo.io/gosum/](https://words.filippo.io/gosum/)

生成摘要时出错

---

## 21. Our Changing Planet, as Seen from Space

**原文标题**: Our Changing Planet, as Seen from Space

**原文链接**: [https://e360.yale.edu/digest/nasa-satellite-images-2025](https://e360.yale.edu/digest/nasa-satellite-images-2025)

生成摘要时出错

---

## 22. Tailscale state file encryption no longer enabled by default

**原文标题**: Tailscale state file encryption no longer enabled by default

**原文链接**: [https://tailscale.com/changelog](https://tailscale.com/changelog)

生成摘要时出错

---

## 23. Lessons from Hash Table Merging

**原文标题**: Lessons from Hash Table Merging

**原文链接**: [https://gist.github.com/attractivechaos/d2efc77cc1db56bbd5fc597987e73338](https://gist.github.com/attractivechaos/d2efc77cc1db56bbd5fc597987e73338)

生成摘要时出错

---

## 24. ChatGPT Health

**原文标题**: ChatGPT Health

**原文链接**: [https://openai.com/index/introducing-chatgpt-health/](https://openai.com/index/introducing-chatgpt-health/)

生成摘要时出错

---

## 25. Anyone have experiences with Audio Induction Loops?

**原文标题**: Anyone have experiences with Audio Induction Loops?

**原文链接**: [https://en.wikipedia.org/wiki/Audio_induction_loop](https://en.wikipedia.org/wiki/Audio_induction_loop)

生成摘要时出错

---

## 26. The Q, K, V Matrices

**原文标题**: The Q, K, V Matrices

**原文链接**: [https://arpitbhayani.me/blogs/qkv-matrices/](https://arpitbhayani.me/blogs/qkv-matrices/)

生成摘要时出错

---

## 27. How Google got its groove back and edged ahead of OpenAI

**原文标题**: How Google got its groove back and edged ahead of OpenAI

**原文链接**: [https://www.wsj.com/tech/ai/google-ai-openai-gemini-chatgpt-b766e160](https://www.wsj.com/tech/ai/google-ai-openai-gemini-chatgpt-b766e160)

生成摘要时出错

---

## 28. Looking for Alice (2023)

**原文标题**: Looking for Alice (2023)

**原文链接**: [https://www.henrikkarlsson.xyz/p/looking-for-alice](https://www.henrikkarlsson.xyz/p/looking-for-alice)

生成摘要时出错

---

## 29. LaTeX Coffee Stains (2021) [pdf]

**原文标题**: LaTeX Coffee Stains (2021) [pdf]

**原文链接**: [https://ctan.math.illinois.edu/graphics/pgf/contrib/coffeestains/coffeestains-en.pdf](https://ctan.math.illinois.edu/graphics/pgf/contrib/coffeestains/coffeestains-en.pdf)

生成摘要时出错

---

## 30. The virtual AmigaOS runtime (a.k.a. Wine for Amiga:)

**原文标题**: The virtual AmigaOS runtime (a.k.a. Wine for Amiga:)

**原文链接**: [https://github.com/cnvogelg/amitools/blob/main/docs/vamos.md](https://github.com/cnvogelg/amitools/blob/main/docs/vamos.md)

生成摘要时出错

---

## 31. Musashi: Motorola 680x0 emulator written in C

**原文标题**: Musashi: Motorola 680x0 emulator written in C

**原文链接**: [https://github.com/kstenerud/Musashi](https://github.com/kstenerud/Musashi)

生成摘要时出错

---

## 32. NPM to implement staged publishing after turbulent shift off classic tokens

**原文标题**: NPM to implement staged publishing after turbulent shift off classic tokens

**原文链接**: [https://socket.dev/blog/npm-to-implement-staged-publishing](https://socket.dev/blog/npm-to-implement-staged-publishing)

生成摘要时出错

---

## 33. US will ban Wall Street investors from buying single-family homes

**原文标题**: US will ban Wall Street investors from buying single-family homes

**原文链接**: [https://www.reuters.com/world/us/us-will-ban-large-institutional-investors-buying-single-family-homes-trump-says-2026-01-07/](https://www.reuters.com/world/us/us-will-ban-large-institutional-investors-buying-single-family-homes-trump-says-2026-01-07/)

生成摘要时出错

---

## 34. GLSL Web CRT Shader

**原文标题**: GLSL Web CRT Shader

**原文链接**: [https://blog.gingerbeardman.com/2026/01/04/glsl-web-crt-shader/](https://blog.gingerbeardman.com/2026/01/04/glsl-web-crt-shader/)

生成摘要时出错

---

## 35. Show HN: Watch LLMs play 21,000 hands of Poker

**原文标题**: Show HN: Watch LLMs play 21,000 hands of Poker

**原文链接**: [https://pokerbench.adfontes.io/run/Large_Models](https://pokerbench.adfontes.io/run/Large_Models)

生成摘要时出错

---

## 36. Health care data breach affects over 600k patients, Illinois agency says

**原文标题**: Health care data breach affects over 600k patients, Illinois agency says

**原文链接**: [https://www.nprillinois.org/illinois/2026-01-06/health-care-data-breach-affects-600-000-patients-illinois-agency-says](https://www.nprillinois.org/illinois/2026-01-06/health-care-data-breach-affects-600-000-patients-illinois-agency-says)

生成摘要时出错

---

## 37. Creators of Tailwind laid off 75% of their engineering team

**原文标题**: Creators of Tailwind laid off 75% of their engineering team

**原文链接**: [https://github.com/tailwindlabs/tailwindcss.com/pull/2388](https://github.com/tailwindlabs/tailwindcss.com/pull/2388)

生成摘要时出错

---

## 38. Play Aardwolf MUD

**原文标题**: Play Aardwolf MUD

**原文链接**: [https://www.aardwolf.com/](https://www.aardwolf.com/)

生成摘要时出错

---

## 39. A4 Paper Stories

**原文标题**: A4 Paper Stories

**原文链接**: [https://susam.net/a4-paper-stories.html](https://susam.net/a4-paper-stories.html)

生成摘要时出错

---

## 40. “Stop Designing Languages. Write Libraries Instead” (2016)

**原文标题**: “Stop Designing Languages. Write Libraries Instead” (2016)

**原文链接**: [https://lbstanza.org/purpose_of_programming_languages.html](https://lbstanza.org/purpose_of_programming_languages.html)

生成摘要时出错

---

## 41. Claude Code CLI was broken

**原文标题**: Claude Code CLI was broken

**原文链接**: [https://github.com/anthropics/claude-code/issues/16673](https://github.com/anthropics/claude-code/issues/16673)

生成摘要时出错

---

## 42. Notion AI: Unpatched data exfiltration

**原文标题**: Notion AI: Unpatched data exfiltration

**原文链接**: [https://www.promptarmor.com/resources/notion-ai-unpatched-data-exfiltration](https://www.promptarmor.com/resources/notion-ai-unpatched-data-exfiltration)

生成摘要时出错

---

## 43. Is this the world's first solid-state battery?

**原文标题**: Is this the world's first solid-state battery?

**原文链接**: [https://www.theverge.com/transportation/858514/is-this-the-worlds-first-solid-state-battery](https://www.theverge.com/transportation/858514/is-this-the-worlds-first-solid-state-battery)

生成摘要时出错

---

## 44. Reading Without Limits or Expectations

**原文标题**: Reading Without Limits or Expectations

**原文链接**: [https://www.carolinecrampton.com/reading-without-limits-or-expectations/](https://www.carolinecrampton.com/reading-without-limits-or-expectations/)

生成摘要时出错

---

## 45. AI Coding Assistants Are Getting Worse

**原文标题**: AI Coding Assistants Are Getting Worse

**原文链接**: [https://spectrum.ieee.org/ai-coding-degrades](https://spectrum.ieee.org/ai-coding-degrades)

生成摘要时出错

---

## 46. Meditation as Wakeful Relaxation: Unclenching Smooth Muscle

**原文标题**: Meditation as Wakeful Relaxation: Unclenching Smooth Muscle

**原文链接**: [https://psychotechnology.substack.com/p/meditation-as-wakeful-relaxation](https://psychotechnology.substack.com/p/meditation-as-wakeful-relaxation)

生成摘要时出错

---

## 47. We found cryptography bugs in the elliptic library using Wycheproof

**原文标题**: We found cryptography bugs in the elliptic library using Wycheproof

**原文链接**: [https://blog.trailofbits.com/2025/11/18/we-found-cryptography-bugs-in-the-elliptic-library-using-wycheproof/](https://blog.trailofbits.com/2025/11/18/we-found-cryptography-bugs-in-the-elliptic-library-using-wycheproof/)

生成摘要时出错

---

## 48. Stem cell engineering breakthrough paves way for next-generation living drugs

**原文标题**: Stem cell engineering breakthrough paves way for next-generation living drugs

**原文链接**: [https://www.med.ubc.ca/news/stem-cell-engineering-breakthrough-paves-way-for-next-generation-living-drugs/](https://www.med.ubc.ca/news/stem-cell-engineering-breakthrough-paves-way-for-next-generation-living-drugs/)

生成摘要时出错

---

## 49. Native Amiga Filesystems on macOS / Linux / Windows with FUSE

**原文标题**: Native Amiga Filesystems on macOS / Linux / Windows with FUSE

**原文链接**: [https://github.com/reinauer/amifuse](https://github.com/reinauer/amifuse)

生成摘要时出错

---

## 50. How dependabot works

**原文标题**: How dependabot works

**原文链接**: [https://nesbitt.io/2026/01/02/how-dependabot-actually-works.html](https://nesbitt.io/2026/01/02/how-dependabot-actually-works.html)

生成摘要时出错

---

## 51. Show HN: I visualized the entire history of Citi Bike in the browser

**原文标题**: Show HN: I visualized the entire history of Citi Bike in the browser

**原文链接**: [https://bikemap.nyc/](https://bikemap.nyc/)

生成摘要时出错

---

## 52. Many hells of WebDAV

**原文标题**: Many hells of WebDAV

**原文链接**: [https://candid.dev/blog/many-hells-of-webdav](https://candid.dev/blog/many-hells-of-webdav)

生成摘要时出错

---

## 53. Building voice agents with Nvidia open models

**原文标题**: Building voice agents with Nvidia open models

**原文链接**: [https://www.daily.co/blog/building-voice-agents-with-nvidia-open-models/](https://www.daily.co/blog/building-voice-agents-with-nvidia-open-models/)

生成摘要时出错

---

## 54. AI misses nearly one-third of breast cancers, study finds

**原文标题**: AI misses nearly one-third of breast cancers, study finds

**原文链接**: [https://www.emjreviews.com/radiology/news/ai-misses-nearly-one-third-of-breast-cancers-study-finds/](https://www.emjreviews.com/radiology/news/ai-misses-nearly-one-third-of-breast-cancers-study-finds/)

生成摘要时出错

---

## 55. Sugar industry influenced researchers and blamed fat for CVD (2016)

**原文标题**: Sugar industry influenced researchers and blamed fat for CVD (2016)

**原文链接**: [https://www.ucsf.edu/news/2016/09/404081/sugar-papers-reveal-industry-role-shifting-national-heart-disease-focus](https://www.ucsf.edu/news/2016/09/404081/sugar-papers-reveal-industry-role-shifting-national-heart-disease-focus)

生成摘要时出错

---

## 56. 2026 Predictions Scorecard

**原文标题**: 2026 Predictions Scorecard

**原文链接**: [https://rodneybrooks.com/predictions-scorecard-2026-january-01/](https://rodneybrooks.com/predictions-scorecard-2026-january-01/)

生成摘要时出错

---

## 57. Quake Brutalist Jam III

**原文标题**: Quake Brutalist Jam III

**原文链接**: [https://www.slipseer.com/index.php?resources/quake-brutalist-jam-iii.549/](https://www.slipseer.com/index.php?resources/quake-brutalist-jam-iii.549/)

生成摘要时出错

---

## 58. Medical Situation on the ISS

**原文标题**: Medical Situation on the ISS

**原文链接**: [https://www.nasa.gov/blogs/spacestation/2026/01/08/international-space-station-update-2/](https://www.nasa.gov/blogs/spacestation/2026/01/08/international-space-station-update-2/)

生成摘要时出错

---

## 59. Minnesota officials say they can't access evidence after fatal ICE shooting

**原文标题**: Minnesota officials say they can't access evidence after fatal ICE shooting

**原文链接**: [https://www.pbs.org/newshour/nation/minnesota-officials-say-they-cant-access-evidence-after-fatal-ice-shooting-and-fbi-wont-work-jointly-on-investigation](https://www.pbs.org/newshour/nation/minnesota-officials-say-they-cant-access-evidence-after-fatal-ice-shooting-and-fbi-wont-work-jointly-on-investigation)

生成摘要时出错

---

## 60. Show HN: Open database of link metadata for large-scale analysis

**原文标题**: Show HN: Open database of link metadata for large-scale analysis

**原文链接**: [https://github.com/rumca-js/RSS-Link-Database-2025](https://github.com/rumca-js/RSS-Link-Database-2025)

生成摘要时出错

---

## 61. Show HN: Open database of link metadata for large-scale analysis

**原文标题**: Show HN: Open database of link metadata for large-scale analysis

**原文链接**: [https://github.com/rumca-js/RSS-Link-Database-2025](https://github.com/rumca-js/RSS-Link-Database-2025)

生成摘要时出错

---

## 62. Polymarket refuses to pay bets that US would 'invade' Venezuela

**原文标题**: Polymarket refuses to pay bets that US would 'invade' Venezuela

**原文链接**: [https://www.ft.com/content/985ae542-1ab4-491e-8e6e-b30f6a3ab666](https://www.ft.com/content/985ae542-1ab4-491e-8e6e-b30f6a3ab666)

生成摘要时出错

---

## 63. Distinct AI Models Seem to Converge on How They Encode Reality

**原文标题**: Distinct AI Models Seem to Converge on How They Encode Reality

**原文链接**: [https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107/](https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107/)

生成摘要时出错

---

## 64. SSDs, power loss protection and fsync latency

**原文标题**: SSDs, power loss protection and fsync latency

**原文链接**: [http://smalldatum.blogspot.com/2026/01/ssds-power-loss-protection-and-fsync.html](http://smalldatum.blogspot.com/2026/01/ssds-power-loss-protection-and-fsync.html)

生成摘要时出错

---

## 65. Suppression of Type I collagen in human scleral fibroblasts treated with ELF

**原文标题**: Suppression of Type I collagen in human scleral fibroblasts treated with ELF

**原文链接**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC3626379/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3626379/)

生成摘要时出错

---

## 66. Intricuit: A touchscreen add-on for Mac laptops

**原文标题**: Intricuit: A touchscreen add-on for Mac laptops

**原文链接**: [https://intricuit.com](https://intricuit.com)

生成摘要时出错

---

## 67. How Bright Headlights Escaped Regulation – and Blinded Us All

**原文标题**: How Bright Headlights Escaped Regulation – and Blinded Us All

**原文链接**: [https://www.autoblog.com/news/how-bright-headlights-escaped-regulation-and-blinded-us-all](https://www.autoblog.com/news/how-bright-headlights-escaped-regulation-and-blinded-us-all)

生成摘要时出错

---

## 68. What *is* code? (2015)

**原文标题**: What *is* code? (2015)

**原文链接**: [https://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/](https://www.bloomberg.com/graphics/2015-paul-ford-what-is-code/)

生成摘要时出错

---

## 69. Vector graphics on GPU

**原文标题**: Vector graphics on GPU

**原文链接**: [https://gasiulis.name/vector-graphics-on-gpu/](https://gasiulis.name/vector-graphics-on-gpu/)

生成摘要时出错

---

## 70. A glimpse into V8 development for RISC-V

**原文标题**: A glimpse into V8 development for RISC-V

**原文链接**: [https://riseproject.dev/2025/12/09/a-glimpse-into-v8-development-for-risc-v/](https://riseproject.dev/2025/12/09/a-glimpse-into-v8-development-for-risc-v/)

生成摘要时出错

---

## 71. Show HN: I built a "Do not disturb" Device for my home office

**原文标题**: Show HN: I built a "Do not disturb" Device for my home office

**原文链接**: [https://apoorv.page/blogs/over-engineered-dnd](https://apoorv.page/blogs/over-engineered-dnd)

生成摘要时出错

---

## 72. LMArena is a cancer on AI

**原文标题**: LMArena is a cancer on AI

**原文链接**: [https://surgehq.ai/blog/lmarena-is-a-plague-on-ai](https://surgehq.ai/blog/lmarena-is-a-plague-on-ai)

生成摘要时出错

---

## 73. The Target forensics lab (2024)

**原文标题**: The Target forensics lab (2024)

**原文链接**: [https://thehorizonsun.com/features/2024/04/11/the-target-forensics-lab/](https://thehorizonsun.com/features/2024/04/11/the-target-forensics-lab/)

生成摘要时出错

---

## 74. My first paper: A practical implementation of Rubiks cube based passkeys

**原文标题**: My first paper: A practical implementation of Rubiks cube based passkeys

**原文链接**: [https://ieeexplore.ieee.org/document/11280260](https://ieeexplore.ieee.org/document/11280260)

生成摘要时出错

---

## 75. So you wanna de-bog yourself (2024)

**原文标题**: So you wanna de-bog yourself (2024)

**原文链接**: [https://www.experimental-history.com/p/so-you-wanna-de-bog-yourself](https://www.experimental-history.com/p/so-you-wanna-de-bog-yourself)

生成摘要时出错

---

## 76. 'Stop sending butt plugs to Bahrain'

**原文标题**: 'Stop sending butt plugs to Bahrain'

**原文链接**: [https://www.ctvnews.ca/toronto/article/stop-sending-butt-plugs-to-bahrain-toronto-sex-store-receives-letters-from-us-department-of-war/](https://www.ctvnews.ca/toronto/article/stop-sending-butt-plugs-to-bahrain-toronto-sex-store-receives-letters-from-us-department-of-war/)

生成摘要时出错

---

## 77. Show HN: How I generate animated pixel art with AI and Python

**原文标题**: Show HN: How I generate animated pixel art with AI and Python

**原文链接**: [https://sarthakmishra.com/blog/building-animated-sprite-hero](https://sarthakmishra.com/blog/building-animated-sprite-hero)

生成摘要时出错

---

## 78. Michel Siffre’s self-experiments in a cave with no light (2018)

**原文标题**: Michel Siffre’s self-experiments in a cave with no light (2018)

**原文链接**: [https://www.newscientist.com/article/mg23931900-400-this-man-spent-months-alone-underground-and-it-warped-his-mind/](https://www.newscientist.com/article/mg23931900-400-this-man-spent-months-alone-underground-and-it-warped-his-mind/)

生成摘要时出错

---

## 79. Ubisoft Shuts Assassin's Creed Developer Studio Just Weeks After It Unionized

**原文标题**: Ubisoft Shuts Assassin's Creed Developer Studio Just Weeks After It Unionized

**原文链接**: [https://www.ign.com/articles/ubisoft-shuts-down-assassins-creed-rebellion-developer-halifax-studio-just-weeks-after-it-unionized](https://www.ign.com/articles/ubisoft-shuts-down-assassins-creed-rebellion-developer-halifax-studio-just-weeks-after-it-unionized)

生成摘要时出错

---

## 80. US Job Openings Decline to Lowest Level in More Than a Year

**原文标题**: US Job Openings Decline to Lowest Level in More Than a Year

**原文链接**: [https://www.bloomberg.com/news/articles/2026-01-07/us-job-openings-decline-to-lowest-level-in-more-than-a-year](https://www.bloomberg.com/news/articles/2026-01-07/us-job-openings-decline-to-lowest-level-in-more-than-a-year)

生成摘要时出错

---

## 81. BillG the Manager (2021)

**原文标题**: BillG the Manager (2021)

**原文链接**: [https://hardcoresoftware.learningbyshipping.com/p/019-billg-the-manager](https://hardcoresoftware.learningbyshipping.com/p/019-billg-the-manager)

生成摘要时出错

---

## 82. A tab hoarder's journey to sanity

**原文标题**: A tab hoarder's journey to sanity

**原文链接**: [https://twitter.com/borisandcrispin/status/2008709479068794989](https://twitter.com/borisandcrispin/status/2008709479068794989)

生成摘要时出错

---

## 83. Fighting back against biometric surveillance at Wegmans

**原文标题**: Fighting back against biometric surveillance at Wegmans

**原文链接**: [https://blog.adafruit.com/2026/01/07/dont-let-the-grocery-store-scan-your-face-a-guide-to-fighting-back-against-biometric-surveillance-at-wegmans/](https://blog.adafruit.com/2026/01/07/dont-let-the-grocery-store-scan-your-face-a-guide-to-fighting-back-against-biometric-surveillance-at-wegmans/)

生成摘要时出错

---

## 84. Show HN: SMTP Tunnel – A SOCKS5 proxy disguised as email traffic to bypass DPI

**原文标题**: Show HN: SMTP Tunnel – A SOCKS5 proxy disguised as email traffic to bypass DPI

**原文链接**: [https://github.com/x011/smtp-tunnel-proxy](https://github.com/x011/smtp-tunnel-proxy)

生成摘要时出错

---

## 85. Opus 4.5 is not the normal AI agent experience that I have had thus far

**原文标题**: Opus 4.5 is not the normal AI agent experience that I have had thus far

**原文链接**: [https://burkeholland.github.io/posts/opus-4-5-change-everything/](https://burkeholland.github.io/posts/opus-4-5-change-everything/)

生成摘要时出错

---

## 86. enclose.horse

**原文标题**: enclose.horse

**原文链接**: [https://enclose.horse/](https://enclose.horse/)

生成摘要时出错

---

## 87. High-Performance DBMSs with io_uring: When and How to use it

**原文标题**: High-Performance DBMSs with io_uring: When and How to use it

**原文链接**: [https://arxiv.org/abs/2512.04859](https://arxiv.org/abs/2512.04859)

生成摘要时出错

---

## 88. Show HN: Free and local browser tool for designing gear models for 3D printing

**原文标题**: Show HN: Free and local browser tool for designing gear models for 3D printing

**原文链接**: [https://gears.dmtrkovalenko.dev](https://gears.dmtrkovalenko.dev)

生成摘要时出错

---

## 89. Databases in 2025: A Year in Review

**原文标题**: Databases in 2025: A Year in Review

**原文链接**: [https://www.cs.cmu.edu/~pavlo/blog/2026/01/2025-databases-retrospective.html](https://www.cs.cmu.edu/~pavlo/blog/2026/01/2025-databases-retrospective.html)

生成摘要时出错

---

## 90. We recreated Steve Jobs's 1975 Atari horoscope program

**原文标题**: We recreated Steve Jobs's 1975 Atari horoscope program

**原文链接**: [https://blog.adafruit.com/2026/01/06/we-recreated-steve-jobss-1975-atari-horoscope-program-and-you-can-run-it/](https://blog.adafruit.com/2026/01/06/we-recreated-steve-jobss-1975-atari-horoscope-program-and-you-can-run-it/)

生成摘要时出错

---

## 91. Becoming a Centenarian

**原文标题**: Becoming a Centenarian

**原文链接**: [https://www.newyorker.com/magazine/2025/12/22/becoming-a-centenarian](https://www.newyorker.com/magazine/2025/12/22/becoming-a-centenarian)

生成摘要时出错

---

## 92. Formal methods only solve half my problems

**原文标题**: Formal methods only solve half my problems

**原文链接**: [https://brooker.co.za/blog/2022/06/02/formal.html](https://brooker.co.za/blog/2022/06/02/formal.html)

生成摘要时出错

---

## 93. Dissecting a C64 Autoboot Program

**原文标题**: Dissecting a C64 Autoboot Program

**原文链接**: [https://bumbershootsoft.wordpress.com/2026/01/03/dissecting-a-c64-autoboot-program/](https://bumbershootsoft.wordpress.com/2026/01/03/dissecting-a-c64-autoboot-program/)

生成摘要时出错

---

## 94. Everything You Need to Know About Email Encryption in 2026

**原文标题**: Everything You Need to Know About Email Encryption in 2026

**原文链接**: [https://soatok.blog/2026/01/04/everything-you-need-to-know-about-email-encryption-in-2026/](https://soatok.blog/2026/01/04/everything-you-need-to-know-about-email-encryption-in-2026/)

生成摘要时出错

---

## 95. The first commercial space stations will start orbiting Earth in 2026

**原文标题**: The first commercial space stations will start orbiting Earth in 2026

**原文链接**: [https://www.newscientist.com/article/2509494-the-first-commercial-space-stations-will-start-orbiting-earth-in-2026/](https://www.newscientist.com/article/2509494-the-first-commercial-space-stations-will-start-orbiting-earth-in-2026/)

生成摘要时出错

---

## 96. Locating a Photo of a Vehicle in 30 Seconds with GeoSpy

**原文标题**: Locating a Photo of a Vehicle in 30 Seconds with GeoSpy

**原文链接**: [https://geospy.ai/blog/locating-a-photo-of-a-vehicle-in-30-seconds-with-geospy](https://geospy.ai/blog/locating-a-photo-of-a-vehicle-in-30-seconds-with-geospy)

生成摘要时出错

---

## 97. On the slow death of scaling

**原文标题**: On the slow death of scaling

**原文链接**: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5877662](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5877662)

生成摘要时出错

---

## 98. Alzheimer's drug developers accuse clinical trial sites of faking data

**原文标题**: Alzheimer's drug developers accuse clinical trial sites of faking data

**原文链接**: [https://www.science.org/content/article/alzheimer-s-drug-developers-accuse-clinical-trial-sites-faking-data](https://www.science.org/content/article/alzheimer-s-drug-developers-accuse-clinical-trial-sites-faking-data)

生成摘要时出错

---

## 99. Show HN: ADHD Focus Light

**原文标题**: Show HN: ADHD Focus Light

**原文链接**: [https://github.com/zonghaoyuan/adhd-focus-light](https://github.com/zonghaoyuan/adhd-focus-light)

生成摘要时出错

---

## 100. Everything You Need to Know About Email Encryption in 2026

**原文标题**: Everything You Need to Know About Email Encryption in 2026

**原文链接**: [https://soatok.blog/2026/01/04/everything-you-need-to-know-about-email-encryption-in-2026/](https://soatok.blog/2026/01/04/everything-you-need-to-know-about-email-encryption-in-2026/)

生成摘要时出错

---

