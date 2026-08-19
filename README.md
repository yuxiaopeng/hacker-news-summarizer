# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-19.md)

*最后自动更新时间: 2026-08-19 18:00:04*
## 1. 公民卫生——避免构建可能被警察国家利用的技术 (2013)

**原文标题**: Civic Hygiene – avoid building technologies that could be used by a police state (2013)

**原文链接**: [https://shkspr.mobi/blog/2013/11/civic-hygiene/](https://shkspr.mobi/blog/2013/11/civic-hygiene/)

《公民卫生》（2013年）一文倡导“公民卫生”原则——这一概念由安全专家布鲁斯·施奈尔（Bruce Schneier）普及——主张反对构建可能助长警察国家的科技或数据库。

作者的核心论点是，我们评估技术时不应基于对当前政府的信任，而应基于该技术被未来恶意政权武器化的可能性。作者以一个假设的公民性取向数据库为例，说明了为良性城市规划（如医疗或教育）收集的数据，一旦敌对政党掌权，如何可能成为骚扰或迫害的工具。

文章强调了几个现代关注点，包括追踪互联网活动的ISP“黑匣子”、网页过滤以及向私人机构出售英国国民保健署（NHS）数据的行为。虽然某些数据库（如车辆登记）被认为具有高实用性和相对较低的风险，但涉及宗教信仰或种族的数据库在历史上却是危险的。作者指出，对20世纪法西斯独裁统治的记忆提醒着人们，基于身份的数据转变为“死刑判决”的速度有多快。

最终，文章得出结论：构建监控基础设施是公民卫生糟糕的一种表现。为了保护民主，社会必须确保今天创建的工具和系统在未来不会被轻易转用于压迫人民。作者指出，“公民卫生”的本质在于“不信任下一届政府”。

---

## 2. 一次玩笑式的域名购买演变成了地缘政治战争。

**原文标题**: A joke domain purchase turned in geopolitical warfare

**原文链接**: [https://sprocketfox.io/xssfox/2026/08/19/sondehub-and-war/](https://sprocketfox.io/xssfox/2026/08/19/sondehub-and-war/)

SondeHub最初于2018年只是澳大利亚一小群气象气球爱好者用来开玩笑的URL重定向，如今已演变成全球地缘政治基础设施的关键环节。在现有平台难以应对庞大数据量的情况下，SondeHub应运而生，旨在改进对无线电探空仪（气象气球发射器）的追踪。通过开发先进的“反向预测”算法（利用风力数据追溯发射地点），开发者在不经意间开始绘制秘密军事设施和炮兵靶场的地图。

该平台的重要性在重大国际事件期间陡增，例如2023年的“中国间谍气球”事件，引发了来自媒体和政府机构的海量流量。更重要的是，开发者发现其API正被用于俄乌战争。有证据表明，军事团队利用SondeHub的风力预测数据在空中“冲浪”，可能用于协调远程无人机袭击或“深度打击”行动。为避免危及生命的风险，开发者与AWS协调以确保服务对这些用户保持在线，同时鼓励他们迁移到本地离线版本。

除了活跃的战争用途外，SondeHub已成为各官方机构的主要资源：
* **美国国家运输安全委员会 (NTSB)** 利用其数据调查了一起飞机与气球的空中相撞事故。
* **美国联邦航空管理局 (FAA)** 寻求空域安全协调，他们起初并未意识到未经监管的气象气球有多普遍。
* **美国战争部 (US Department of War)** 曾请求获取数据，但最终未能支付所要求的基础设施费用。

从检测GPS欺骗到应对古怪的供应商和“奶酪占卜者”，SondeHub的故事凸显了开源公民科学是如何意外地跨入国家安全和国际冲突领域的。在对入侵乌克兰行为抱持“去他妈的俄罗斯”的情绪下，开发者们继续在经营这个从爱好者网站转变为关键军事工具的过程中，应对伦理和法律上的复杂挑战。

---

## 3. 使用几何学与 CUDA 编程定位随机岛屿

**原文标题**: Geolocating a random island using geometry and CUDA programming

**原文链接**: [https://yassa9.github.io/osint/gralhix-004/](https://yassa9.github.io/osint/gralhix-004/)

本文详细介绍了针对 Sofia Santos 的 OSINT 练习 #004 的技术解决方案。该练习要求参与者仅凭单张图片对特定的度假小岛进行地理定位。作者弃用了 Google Lens 等视觉搜索工具，转而结合几何学、全球地理空间数据集和 CUDA GPU 编程，通过排除法成功锁定了目标位置。

该方法首先根据度假小岛（P0）与两个背景陆地（P1 和 P2）之间的相对距离和角度创建几何“指纹”。利用 OpenStreetMap 的全球陆地多边形数据集，作者应用了多个启发式过滤器来缩小搜索空间：
*   **地理约束：** 将搜索范围限制在热带纬度和低密度岛群。
*   **计算能力：** 使用 CUDA 并行处理超过 8,000 万组潜在的岛屿三元组，并将其与初始几何指纹进行匹配。
*   **形态分析：** 基于“紧凑度”（Polsby-Popper 分值）和“填充率”评估候选目标，以匹配该小岛特定的椭圆形状。
*   **环境数据：** 利用 Sentinel-2 卫星图像验证植被情况（NDVI），并使用哥白尼数字高程模型（Copernicus DEM）数据确保目标小岛地势平坦，而背景岛屿则具有山峰特征。

经过数据过滤后，剩余 26 个候选位置。通过 Google 地图进行人工验证，确认该地点为密克罗尼西亚的 **Oan 度假村**（7.363444°, 151.755750°）。作者进一步计算出相机当时朝向**西北**。该项目全面展示了如何将高性能计算和地理空间数据科学应用于复杂的 OSINT 挑战。

---

## 4. Launch HN: OneCLI (YC S26) – 面向团队的开源沙箱化 Agent 运行框架

**原文标题**: Launch HN: OneCLI (YC S26) – OSS sandboxed agent harness for teams

**原文链接**: [https://github.com/onecli/onecli](https://github.com/onecli/onecli)

**OneCLI (YC S26)** 是一款旨在为组织规模化扩展 AI 智能体（AI Agents）的开源平台。虽然大多数自主智能体是为个人使用而设计的，但 OneCLI 提供了一套“管控框架”，允许团队为每位员工部署、管理并保护其个人智能体。

**核心功能与能力：**
*   **沙箱化智能体：** 每位团队成员都拥有一个在隔离环境中运行的专用智能体，具备独立的文件系统、Shell 和持久化内存。
*   **团队管理：** 平台与公司的身份提供商（IdP）集成以配给智能体，并允许管理员在整个工作区强制执行全局安全策略。
*   **安全与凭证管理：** 一个基于 Rust 开发的中央网关会拦截出站请求并注入凭据（支持 Bitwarden 和 1Password 等集成），而智能体本身无法接触到这些机密。它还包含针对删除数据或发送电子邮件等敏感操作的“人机回环”触发机制。
*   **全渠道接入：** 智能体可通过 Web 控制面板或 Slack 进行访问，它们可以在 Slack 中回复私信并以自己的身份和头像参与频道讨论。

**架构与部署：**
该系统由 Next.js 控制面板、用于策略执行的 Rust 网关以及仅出站的运行器（Runner）组成。由于运行器通过轮询方式获取任务，无需开放入站端口，因此可以安全地部署在 NAT 或 VPC 之后的笔记本电脑、家庭实验室或云服务器上。

**许可协议：**
OneCLI 主要采用 **Apache-2.0** 协议，允许免费的生产环境自托管。特定的企业级功能（位于 `ee/` 目录下）在生产环境中使用时需要商业订阅。用户可以通过 `onecli.sh` 的云托管服务开始使用，或通过克隆代码库进行本地开发。

---

## 5. Ornith-1.5：从自我脚手架到自我提升

**原文标题**: Ornith-1.5: From Self-Scaffolding to Self-Improvement

**原文链接**: [https://ornith.ai/ornith_1_5.html](https://ornith.ai/ornith_1_5.html)

Ornith-1.5 代表了基础模型领域的重大进步，实现了从“自我脚手架”（self-scaffolding）向全面的端到端**自我改进框架**的跨越。通过扩展 Ornith-1.0 引入的循环，该模型现在能够自主提议新的训练任务，生成特定任务的脚手架（指令和工具），并为强化学习产出解决方案轨迹（rollouts）。

该系统利用**群体相对策略优化 (GRPO)** 来联合优化任务生成、测试框架构建和策略执行。模型通过基于三个标准评估任务来创建“前沿课程”：**有效性**（可验证的环境）、**新颖性**（多样性）和**前沿难度**（针对模型目前成功率为 20% 的任务）。这确保了模型能不断应对逐渐变难且非冗余的问题挑战。

Ornith-1.5 提供三种规模：
*   **397B MoE：** 旗舰模型，在 Terminal-Bench 2.1 (86.1) 和 DeepSWE (56.0) 等基准测试中，其表现达到或超过了 Claude Opus 4.8 以及领先的开源模型（GLM-5.2、DeepSeek-V4）。
*   **35B MoE：** 每个 token 仅激活 3B 参数，在智能体编程（agentic coding）方面的表现显著优于 Gemma 4-31B 和 Muse Glimmer-30B 等更大的稠密模型。
*   **9B Dense：** 可在移动端部署的版本，其性能出色地达到或超过了 31B–35B 参数规模的模型。

在所有规模下，Ornith-1.5 在推理、编程和智能体任务中均展现出行业领先的性能。它的成功凸显了自主自我改进循环在克服静态、人工策划训练数据局限性方面的潜力，使模型能够通过自我生成的学习经验持续扩展自身能力。

---

## 6. OpenLogi

**原文标题**: OpenLogi

**原文链接**: [https://openlogi.org/en](https://openlogi.org/en)

**OpenLogi** 是一款硬件自定义实用程序，旨在通过允许用户重映射设备上的物理按键来提高生产力。

该软件的主要功能包括：

*   **按键重映射：** 用户可以将任何物理按键分配给 44 种内置操作之一，例如浏览器导航（后退/前进）、系统控制（调度中心）或标签页管理。
*   **针对每台设备的自定义：** 设置是基于每台设备进行配置的，允许为不同的硬件进行独特的个性化设置。
*   **高级功能：** 除了标准预设外，该工具还支持自定义键盘快捷键、应用程序启动器以及复杂的脚本操作。

总的来说，OpenLogi 为用户提供了一个高度灵活的环境，使其能够根据特定的工作流程定制其输入设备。

---

## 7. Remote workers report the highest well-being in study of 7,700 employees

**原文标题**: Remote workers report the highest well-being in study of 7,700 employees

**原文链接**: [https://www.colorado.edu/today/2026/08/12/remote-workers-report-highest-well-being-study-7700-employees](https://www.colorado.edu/today/2026/08/12/remote-workers-report-highest-well-being-study-7700-employees)

生成摘要时出错

---

## 8. LLM 时代的可扩展软件

**原文标题**: Extensible Software in the Age of LLMs

**原文链接**: [https://jeremymorrell.dev/blog/extensible-software-in-the-age-of-llms/](https://jeremymorrell.dev/blog/extensible-software-in-the-age-of-llms/)

生成摘要时出错

---

## 9. Moderna reports first positive Phase 3 for mRNA neoantigen therapy in melanoma

**原文标题**: Moderna reports first positive Phase 3 for mRNA neoantigen therapy in melanoma

**原文链接**: [https://twitter.com/NoubarAfeyan/status/2090050162441752787](https://twitter.com/NoubarAfeyan/status/2090050162441752787)

生成摘要时出错

---

## 10. Devices with GrapheneOS support should be available in 2027

**原文标题**: Devices with GrapheneOS support should be available in 2027

**原文链接**: [https://grapheneos.social/@GrapheneOS/117078064184215730](https://grapheneos.social/@GrapheneOS/117078064184215730)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 2 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 3 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 4 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 5 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 6 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 7 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 8 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 9 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 10 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 11 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 12 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 13 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 14 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 15 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 16 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 17 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 18 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 19 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 20 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 21 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 22 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 23 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 24 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 25 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 26 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 27 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 28 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 29 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 30 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 31 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 32 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 33 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 34 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 35 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 36 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 37 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 38 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 39 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 40 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 41 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 42 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 43 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 44 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 45 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 46 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 47 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 48 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 49 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 50 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 51 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 52 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 53 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 54 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 55 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 56 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 57 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 58 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 59 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 60 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 61 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 62 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 63 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 64 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 65 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 66 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 67 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 68 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 69 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 70 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 71 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 72 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 73 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 74 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 75 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 76 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 77 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 78 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 79 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 80 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 81 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 82 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 83 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 84 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 85 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 86 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 87 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 88 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 89 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 90 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 91 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 92 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 93 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 94 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 95 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 96 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 97 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 98 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 99 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 100 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 101 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 102 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 103 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 104 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 105 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 106 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 107 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 108 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 109 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 110 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 111 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 112 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 113 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 114 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 115 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 116 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 117 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 118 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 119 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 120 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 121 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 122 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 123 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 124 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 125 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 126 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 127 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 128 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 129 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 130 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 131 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 132 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 133 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 134 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 135 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 136 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 137 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 138 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 139 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 140 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 141 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 142 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 143 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 144 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 145 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 146 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 147 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 148 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 149 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 150 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 151 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 152 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 153 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 154 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 155 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 156 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 157 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 158 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 159 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 160 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 161 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 162 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 163 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 164 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 165 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 166 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 167 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 168 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 169 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 170 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 171 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 172 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 173 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 174 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 175 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 176 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 177 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 178 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 179 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 180 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 181 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 182 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 183 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 184 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 185 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 186 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 187 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 188 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 189 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 190 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 191 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 192 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 193 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 194 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 195 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 196 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 197 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 198 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 199 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 200 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 201 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 202 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 203 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 204 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 205 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 206 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 207 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 208 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 209 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 210 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 211 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 212 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 213 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 214 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 215 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 216 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 217 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 218 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 219 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 220 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 221 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 222 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 223 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 224 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 225 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 226 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 227 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 228 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 229 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 230 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 231 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 232 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 233 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 234 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 235 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 236 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 237 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 238 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 239 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 240 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 241 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 242 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 243 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 244 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 245 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 246 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 247 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 248 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 249 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 250 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 251 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 252 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 253 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 254 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 255 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 256 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 257 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 258 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 259 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 260 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 261 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 262 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 263 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 264 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 265 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 266 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 267 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 268 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 269 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 270 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 271 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 272 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 273 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 274 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 275 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 276 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 277 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 278 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 279 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 280 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 281 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 282 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 283 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 284 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 285 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 286 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 287 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 288 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 289 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 290 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 291 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 292 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 293 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 294 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 295 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 296 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 297 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 298 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 299 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 300 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 301 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 302 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 303 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 304 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 305 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 306 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 307 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 308 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 309 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 310 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 311 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 312 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 313 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 314 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 315 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 316 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 317 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 318 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 319 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 320 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 321 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 322 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 323 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 324 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 325 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 326 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 327 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 328 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 329 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 330 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 331 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 332 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 333 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 334 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 335 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 336 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 337 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 338 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 339 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 340 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 341 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 342 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 343 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 344 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 345 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 346 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 347 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 348 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 349 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 350 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 351 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 352 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 353 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 354 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 355 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 356 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 357 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 358 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 359 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 360 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 361 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 362 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 363 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 364 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 365 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 366 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 367 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 368 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 369 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 370 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 371 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 372 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 373 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 374 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 375 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 376 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 377 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 378 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 379 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 380 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 381 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 382 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 383 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 384 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 385 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 386 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 387 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 388 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 389 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 390 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 391 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 392 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 393 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 394 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 395 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 396 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 397 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 398 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 399 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 400 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 401 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 402 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 403 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 404 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 405 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 406 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 407 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 408 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 409 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 410 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 411 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 412 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 413 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 414 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 415 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 416 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 417 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 418 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 419 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 420 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 421 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 422 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 423 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 424 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 425 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 426 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 427 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 428 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 429 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 430 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 431 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 432 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 433 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 434 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 435 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 436 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 437 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 438 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 439 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 440 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 441 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 442 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 443 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 444 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 445 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 446 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 447 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 448 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 449 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 450 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 451 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 452 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 453 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 454 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 455 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 456 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 457 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 458 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 459 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 460 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 461 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 462 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 463 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 464 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 465 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 466 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 467 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 468 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 469 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 470 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 471 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 472 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 473 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 474 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 475 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 476 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 477 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 478 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 479 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 480 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 481 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 482 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 483 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 484 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 485 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 486 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 487 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 488 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 489 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 490 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 491 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 492 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 493 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 494 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 495 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 496 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 497 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 498 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 499 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 500 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 501 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 502 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 503 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 504 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 505 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 506 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 507 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 508 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 509 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 510 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 511 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 512 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 513 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 514 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 515 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 516 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
