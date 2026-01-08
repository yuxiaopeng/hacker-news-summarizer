# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-08.md)

*最后自动更新时间: 2026-01-08 17:56:28*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 2 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 3 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 4 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 5 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 6 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 7 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 8 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 9 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 10 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 11 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 12 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 13 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 14 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 15 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 16 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 17 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 18 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 19 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 20 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 21 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 22 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 23 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 24 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 25 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 26 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 27 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 28 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 29 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 30 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 31 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 32 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 33 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 34 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 35 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 36 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 37 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 38 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 39 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 40 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 41 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 42 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 43 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 44 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 45 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 46 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 47 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 48 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 49 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 50 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 51 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 52 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 53 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 54 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 55 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 56 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 57 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 58 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 59 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 60 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 61 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 62 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 63 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 64 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 65 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 66 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 67 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 68 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 69 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 70 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 71 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 72 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 73 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 74 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 75 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 76 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 77 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 78 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 79 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 80 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 81 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 82 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 83 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 84 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 85 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 86 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 87 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 88 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 89 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 90 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 91 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 92 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 93 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 94 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 95 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 96 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 97 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 98 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 99 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 100 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 101 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 102 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 103 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 104 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 105 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 106 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 107 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 108 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 109 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 110 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 111 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 112 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 113 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 114 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 115 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 116 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 117 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 118 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 119 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 120 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 121 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 122 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 123 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 124 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 125 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 126 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 127 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 128 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 129 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 130 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 131 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 132 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 133 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 134 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 135 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 136 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 137 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 138 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 139 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 140 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 141 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 142 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 143 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 144 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 145 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 146 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 147 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 148 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 149 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 150 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 151 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 152 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 153 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 154 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 155 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 156 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 157 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 158 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 159 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 160 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 161 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 162 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 163 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 164 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 165 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 166 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 167 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 168 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 169 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 170 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 171 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 172 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 173 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 174 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 175 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 176 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 177 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 178 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 179 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 180 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 181 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 182 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 183 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 184 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 185 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 186 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 187 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 188 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 189 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 190 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 191 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 192 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 193 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 194 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 195 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 196 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 197 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 198 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 199 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 200 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 201 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 202 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 203 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 204 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 205 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 206 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 207 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 208 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 209 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 210 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 211 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 212 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 213 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 214 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 215 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 216 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 217 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 218 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 219 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 220 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 221 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 222 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 223 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 224 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 225 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 226 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 227 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 228 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 229 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 230 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 231 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 232 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 233 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 234 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 235 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 236 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 237 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 238 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 239 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 240 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 241 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 242 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 243 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 244 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 245 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 246 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 247 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 248 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 249 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 250 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 251 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 252 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 253 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 254 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 255 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 256 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 257 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 258 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 259 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 260 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 261 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 262 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 263 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 264 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 265 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 266 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 267 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 268 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 269 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 270 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 271 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 272 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 273 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 274 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 275 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 276 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 277 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 278 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 279 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 280 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 281 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 282 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 283 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 284 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 285 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 286 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 287 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 288 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 289 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 290 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 291 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 292 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 293 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 294 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
