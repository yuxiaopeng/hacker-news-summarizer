# Hacker News 热门文章摘要 (2026-08-19)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. PostgreSQL for Everything

**原文标题**: PostgreSQL for Everything

**原文链接**: [https://www.raphaelbauer.com:443/posts/postgresql-everything/](https://www.raphaelbauer.com:443/posts/postgresql-everything/)

生成摘要时出错

---

## 12. Microgpt in pure C hits 10M tps on Apple m5

**原文标题**: Microgpt in pure C hits 10M tps on Apple m5

**原文链接**: [https://github.com/vixhal-baraiya/microgpt-c](https://github.com/vixhal-baraiya/microgpt-c)

生成摘要时出错

---

## 13. Chain-of-Thought Reasoning in the Wild Is Not Always Faithful

**原文标题**: Chain-of-Thought Reasoning in the Wild Is Not Always Faithful

**原文链接**: [https://arxiv.org/abs/2503.08679](https://arxiv.org/abs/2503.08679)

生成摘要时出错

---

## 14. Air Theremin – a browser theremin you play by waving at your webcam

**原文标题**: Air Theremin – a browser theremin you play by waving at your webcam

**原文链接**: [https://theremin.bizibah.com/](https://theremin.bizibah.com/)

生成摘要时出错

---

## 15. Mathematics in the Age of AI

**原文标题**: Mathematics in the Age of AI

**原文链接**: [https://arxiv.org/abs/2608.16753](https://arxiv.org/abs/2608.16753)

生成摘要时出错

---

## 16. Taffy: A flexible, high-performance, cross-platform UI layout library

**原文标题**: Taffy: A flexible, high-performance, cross-platform UI layout library

**原文链接**: [https://github.com/DioxusLabs/taffy](https://github.com/DioxusLabs/taffy)

生成摘要时出错

---

## 17. A decades-old bug in Knuth's long division (TAOCP Vol II, Algorithm 4.3.1D)

**原文标题**: A decades-old bug in Knuth's long division (TAOCP Vol II, Algorithm 4.3.1D)

**原文链接**: [https://kolja.rs/algorithm-d/](https://kolja.rs/algorithm-d/)

生成摘要时出错

---

## 18. New Casio F-B100W – Upgrade to the iconic F-91W after 40 years

**原文标题**: New Casio F-B100W – Upgrade to the iconic F-91W after 40 years

**原文链接**: [https://www.casio.com/uk/watches/casio/product.F-B100W-1A/](https://www.casio.com/uk/watches/casio/product.F-B100W-1A/)

生成摘要时出错

---

## 19. Cerebras CS-4

**原文标题**: Cerebras CS-4

**原文链接**: [https://www.cerebras.ai/cs4](https://www.cerebras.ai/cs4)

生成摘要时出错

---

## 20. Being ambitious and being a dad

**原文标题**: Being ambitious and being a dad

**原文链接**: [https://nicholascharriere.com/blog/being-ambitious-and-being-a-dad/](https://nicholascharriere.com/blog/being-ambitious-and-being-a-dad/)

生成摘要时出错

---

## 21. Rings forged from meteorites may have been fashionable among ancient Greek elite

**原文标题**: Rings forged from meteorites may have been fashionable among ancient Greek elite

**原文链接**: [https://phys.org/news/2026-08-forged-meteorites-fashionable-ancient-greek.html](https://phys.org/news/2026-08-forged-meteorites-fashionable-ancient-greek.html)

生成摘要时出错

---

## 22. A recipe for drone racing with reinforcement learning

**原文标题**: A recipe for drone racing with reinforcement learning

**原文链接**: [https://mrandri19.github.io/2026/07/19/drone-racing-with-reinforcement-learning.html](https://mrandri19.github.io/2026/07/19/drone-racing-with-reinforcement-learning.html)

生成摘要时出错

---

## 23. Supersonic Trebuchet [video]

**原文标题**: Supersonic Trebuchet [video]

**原文链接**: [https://www.youtube.com/watch?v=Co57SfcT-h0](https://www.youtube.com/watch?v=Co57SfcT-h0)

生成摘要时出错

---

## 24. Activation Energy is a good model for a lot of things

**原文标题**: Activation Energy is a good model for a lot of things

**原文链接**: [https://homosabiens.substack.com/p/activation-energy-is-a-good-model](https://homosabiens.substack.com/p/activation-energy-is-a-good-model)

生成摘要时出错

---

## 25. How Kubernetes Probes Work

**原文标题**: How Kubernetes Probes Work

**原文链接**: [https://ngrok.com/blog/probes](https://ngrok.com/blog/probes)

生成摘要时出错

---

## 26. Show HN: Nikon F100 Film Camera Repair Notes

**原文标题**: Show HN: Nikon F100 Film Camera Repair Notes

**原文链接**: [https://github.com/enthdegree/f100](https://github.com/enthdegree/f100)

生成摘要时出错

---

## 27. Palomar: A registry of Lean verified mathematics

**原文标题**: Palomar: A registry of Lean verified mathematics

**原文链接**: [https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/](https://terrytao.wordpress.com/2026/08/18/palomar-a-registry-of-lean-verified-mathematics/)

生成摘要时出错

---

## 28. A 3D fruit fly on macOS desktop powered by the real FlyWire connectome

**原文标题**: A 3D fruit fly on macOS desktop powered by the real FlyWire connectome

**原文链接**: [https://github.com/DenisSergeevitch/desktop-fly](https://github.com/DenisSergeevitch/desktop-fly)

生成摘要时出错

---

## 29. How does IKEA come up with names for its products?

**原文标题**: How does IKEA come up with names for its products?

**原文链接**: [https://www.ikea.com/se/en/customer-service/knowledge/articles/6f564c4d-2ccc-46de-b643-545a3948dc79.html](https://www.ikea.com/se/en/customer-service/knowledge/articles/6f564c4d-2ccc-46de-b643-545a3948dc79.html)

生成摘要时出错

---

## 30. Finger: the 1971 social network that never died

**原文标题**: Finger: the 1971 social network that never died

**原文链接**: [https://en.andros.dev/blog/54572bc7/finger-the-1971-social-network-that-never-died/](https://en.andros.dev/blog/54572bc7/finger-the-1971-social-network-that-never-died/)

生成摘要时出错

---

## 31. λλ: A Programming Language for Silicon Photonics

**原文标题**: λλ: A Programming Language for Silicon Photonics

**原文链接**: [https://dl.acm.org/doi/10.1145/3789240.3829151](https://dl.acm.org/doi/10.1145/3789240.3829151)

生成摘要时出错

---

## 32. A 25-year-old video patent just expired, ending a legal headache for Linux

**原文标题**: A 25-year-old video patent just expired, ending a legal headache for Linux

**原文链接**: [https://www.xda-developers.com/25-year-old-brazilian-video-patent-expired-legal-headache-linux/](https://www.xda-developers.com/25-year-old-brazilian-video-patent-expired-legal-headache-linux/)

生成摘要时出错

---

## 33. Claude writing a macOS driver for my obscure HP printer built only for Windows

**原文标题**: Claude writing a macOS driver for my obscure HP printer built only for Windows

**原文链接**: [https://twitter.com/kuberwastaken/status/2089377982536388964](https://twitter.com/kuberwastaken/status/2089377982536388964)

生成摘要时出错

---

## 34. Solo – a .so loader for static Linux binaries

**原文标题**: Solo – a .so loader for static Linux binaries

**原文链接**: [https://github.com/pg83/solo](https://github.com/pg83/solo)

生成摘要时出错

---

## 35. The Mojo language (by Modular, now Qualcomm) is now open-source

**原文标题**: The Mojo language (by Modular, now Qualcomm) is now open-source

**原文链接**: [https://www.modular.com/blog/modcon-announcements](https://www.modular.com/blog/modcon-announcements)

生成摘要时出错

---

## 36. And then the men with guns tell you to do it anyway

**原文标题**: And then the men with guns tell you to do it anyway

**原文链接**: [https://shkspr.mobi/blog/2026/08/and-then-the-men-with-guns-tell-you-to-do-it-anyway/](https://shkspr.mobi/blog/2026/08/and-then-the-men-with-guns-tell-you-to-do-it-anyway/)

生成摘要时出错

---

## 37. The Amazon tax

**原文标题**: The Amazon tax

**原文链接**: [https://seths.blog/2026/08/the-amazon-tax/](https://seths.blog/2026/08/the-amazon-tax/)

生成摘要时出错

---

## 38. Turbovec – Google's TurboQuant for vector search in Rust

**原文标题**: Turbovec – Google's TurboQuant for vector search in Rust

**原文链接**: [https://github.com/RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec)

生成摘要时出错

---

## 39. Apple announces changes for apps in the European Union

**原文标题**: Apple announces changes for apps in the European Union

**原文链接**: [https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/](https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/)

生成摘要时出错

---

## 40. The Vietnam Binh Chau (Chau Tan) Late Tang Wreck

**原文标题**: The Vietnam Binh Chau (Chau Tan) Late Tang Wreck

**原文链接**: [https://www.koh-antique.com/client/tangwreck/tangwreck.html](https://www.koh-antique.com/client/tangwreck/tangwreck.html)

生成摘要时出错

---

## 41. AI usage patterns in software teams

**原文标题**: AI usage patterns in software teams

**原文链接**: [https://linear.app/data](https://linear.app/data)

生成摘要时出错

---

## 42. Show HN: Automatically detect and patch walking-dead states in Sierra games

**原文标题**: Show HN: Automatically detect and patch walking-dead states in Sierra games

**原文链接**: [https://github.com/katiahayati/lucasartsifier/](https://github.com/katiahayati/lucasartsifier/)

生成摘要时出错

---

## 43. Scientists stunned by children's lung recovery in ultra low emission zone

**原文标题**: Scientists stunned by children's lung recovery in ultra low emission zone

**原文链接**: [https://www.bbc.com/news/articles/c1l1r1zne1ro](https://www.bbc.com/news/articles/c1l1r1zne1ro)

生成摘要时出错

---

## 44. Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces

**原文标题**: Stop Anthropomorphizing Intermediate Tokens as Reasoning/Thinking Traces

**原文链接**: [https://arxiv.org/abs/2504.09762](https://arxiv.org/abs/2504.09762)

生成摘要时出错

---

## 45. What's in a PowerPoint File?

**原文标题**: What's in a PowerPoint File?

**原文链接**: [https://editide.com/blog/what-is-a-pptx-file/](https://editide.com/blog/what-is-a-pptx-file/)

生成摘要时出错

---

## 46. Looking for Missed Alarm Bugs in a Formal Verification Tool

**原文标题**: Looking for Missed Alarm Bugs in a Formal Verification Tool

**原文链接**: [https://blog.regehr.org/archives/2124](https://blog.regehr.org/archives/2124)

生成摘要时出错

---

## 47. Teaching my kid to code with a modern MUD

**原文标题**: Teaching my kid to code with a modern MUD

**原文链接**: [https://tau.dev/2026/08/07/canon](https://tau.dev/2026/08/07/canon)

生成摘要时出错

---

## 48. California's new tire efficiency rules could save drivers $1B a year

**原文标题**: California's new tire efficiency rules could save drivers $1B a year

**原文链接**: [https://grist.org/transportation/californias-new-tire-efficiency-rules-could-save-drivers-1b-a-year/](https://grist.org/transportation/californias-new-tire-efficiency-rules-could-save-drivers-1b-a-year/)

生成摘要时出错

---

## 49. Show HN: Interactive, animated architecture of any HuggingFace models

**原文标题**: Show HN: Interactive, animated architecture of any HuggingFace models

**原文链接**: [https://modelmap.cc](https://modelmap.cc)

生成摘要时出错

---

## 50. Zuckerberg lied about concern for child safety

**原文标题**: Zuckerberg lied about concern for child safety

**原文链接**: [https://www.theguardian.com/technology/2026/aug/19/meta-safety-trial-whistleblower-testimony](https://www.theguardian.com/technology/2026/aug/19/meta-safety-trial-whistleblower-testimony)

生成摘要时出错

---

## 51. Beware Management Consultants

**原文标题**: Beware Management Consultants

**原文链接**: [https://about.iceland.co.uk/our-story/the-dark-ages/beware-management-consultants/](https://about.iceland.co.uk/our-story/the-dark-ages/beware-management-consultants/)

生成摘要时出错

---

## 52. Launch HN: machine0 (YC S26) – Persistent CPU and GPU VMs from the CLI

**原文标题**: Launch HN: machine0 (YC S26) – Persistent CPU and GPU VMs from the CLI

**原文链接**: [https://machine0.io](https://machine0.io)

生成摘要时出错

---

## 53. The science behind Pixel Watch's insulin resistance feature

**原文标题**: The science behind Pixel Watch's insulin resistance feature

**原文链接**: [https://www.empirical.health/blog/wearable-insulin-resistance/](https://www.empirical.health/blog/wearable-insulin-resistance/)

生成摘要时出错

---

## 54. Meta's blockbuster trial draws parallels to big tobacco

**原文标题**: Meta's blockbuster trial draws parallels to big tobacco

**原文链接**: [https://www.economist.com/business/2026/08/18/metas-blockbuster-trial-draws-parallels-to-big-tobacco](https://www.economist.com/business/2026/08/18/metas-blockbuster-trial-draws-parallels-to-big-tobacco)

生成摘要时出错

---

## 55. Python Polars Cheatsheet (based on our O'Reilly book)

**原文标题**: Python Polars Cheatsheet (based on our O'Reilly book)

**原文链接**: [https://opensource.posit.co/resources/cheatsheets/polars/](https://opensource.posit.co/resources/cheatsheets/polars/)

生成摘要时出错

---

## 56. Memory prices climb 500% in 12 months

**原文标题**: Memory prices climb 500% in 12 months

**原文链接**: [https://www.tomshardware.com/pc-components/ram/memory-prices-climb-500-percent-in-12-months-up-to-10x-the-lowest-ever-tracked-prices-128gb-of-ddr5-now-usd3-399](https://www.tomshardware.com/pc-components/ram/memory-prices-climb-500-percent-in-12-months-up-to-10x-the-lowest-ever-tracked-prices-128gb-of-ddr5-now-usd3-399)

生成摘要时出错

---

## 57. Tiny satellite will use the dark side of the Moon as a shield

**原文标题**: Tiny satellite will use the dark side of the Moon as a shield

**原文链接**: [https://www.cam.ac.uk/research/news/tiny-satellite-will-use-the-dark-side-of-the-moon-to-eavesdrop-on-whispers-from-the-early-universe](https://www.cam.ac.uk/research/news/tiny-satellite-will-use-the-dark-side-of-the-moon-to-eavesdrop-on-whispers-from-the-early-universe)

生成摘要时出错

---

## 58. Universal health coverage could save $1T and 114k lives a year: study

**原文标题**: Universal health coverage could save $1T and 114k lives a year: study

**原文链接**: [https://ysph.yale.edu/news-article/universal-health-coverage-could-save-one-trillion-dollars-and-114000-lives-every-year/](https://ysph.yale.edu/news-article/universal-health-coverage-could-save-one-trillion-dollars-and-114000-lives-every-year/)

生成摘要时出错

---

## 59. CUDA Shared Memory Swizzling

**原文标题**: CUDA Shared Memory Swizzling

**原文链接**: [https://leimao.github.io/blog/CUDA-Shared-Memory-Swizzling/](https://leimao.github.io/blog/CUDA-Shared-Memory-Swizzling/)

生成摘要时出错

---

## 60. Does AI stop children from learning?

**原文标题**: Does AI stop children from learning?

**原文链接**: [https://www.economist.com/graphic-detail/2026/08/18/does-ai-stop-children-from-learning](https://www.economist.com/graphic-detail/2026/08/18/does-ai-stop-children-from-learning)

生成摘要时出错

---

## 61. Cursor launches Origin, GitHub alternative

**原文标题**: Cursor launches Origin, GitHub alternative

**原文链接**: [https://cursor.com/changelog/origin-code-hosting](https://cursor.com/changelog/origin-code-hosting)

生成摘要时出错

---

## 62. That Disgraceful, Disreputable, (Wonderful) Form of Punctuation: The Parenthesis

**原文标题**: That Disgraceful, Disreputable, (Wonderful) Form of Punctuation: The Parenthesis

**原文链接**: [https://lithub.com/on-that-disgraceful-disreputable-wonderful-form-of-punctuation-the-parenthesis/](https://lithub.com/on-that-disgraceful-disreputable-wonderful-form-of-punctuation-the-parenthesis/)

生成摘要时出错

---

## 63. How a giant battery is transforming a town centre in Cannington, Ontario

**原文标题**: How a giant battery is transforming a town centre in Cannington, Ontario

**原文链接**: [https://betakit.com/how-a-giant-battery-is-transforming-a-town-centre-in-cannington-ontario/](https://betakit.com/how-a-giant-battery-is-transforming-a-town-centre-in-cannington-ontario/)

生成摘要时出错

---

## 64. Splitting a Git Commit

**原文标题**: Splitting a Git Commit

**原文链接**: [https://blog.gnoack.org/post/git-history-split](https://blog.gnoack.org/post/git-history-split)

生成摘要时出错

---

## 65. Rethinking Database Programming

**原文标题**: Rethinking Database Programming

**原文链接**: [https://acadia.engineering/blog/rethinking-database-programming](https://acadia.engineering/blog/rethinking-database-programming)

生成摘要时出错

---

## 66. Using the railway network as a flatbed scanner

**原文标题**: Using the railway network as a flatbed scanner

**原文链接**: [https://philo.gay/linecam/](https://philo.gay/linecam/)

生成摘要时出错

---

## 67. Sticky wage norms and the real wage cost of unexpected inflation

**原文标题**: Sticky wage norms and the real wage cost of unexpected inflation

**原文链接**: [https://bfi.uchicago.edu/wp-content/uploads/2026/08/BFI_WP_2026-108-1.pdf](https://bfi.uchicago.edu/wp-content/uploads/2026/08/BFI_WP_2026-108-1.pdf)

生成摘要时出错

---

## 68. Claude Code May–August 2026 weekly limits promotion

**原文标题**: Claude Code May–August 2026 weekly limits promotion

**原文链接**: [https://support.claude.com/en/articles/15910845-claude-code-may-august-2026-weekly-limits-promotion](https://support.claude.com/en/articles/15910845-claude-code-may-august-2026-weekly-limits-promotion)

生成摘要时出错

---

## 69. Building Without Predicting

**原文标题**: Building Without Predicting

**原文链接**: [https://sive.rs/fit](https://sive.rs/fit)

生成摘要时出错

---

## 70. Win-V combo from Windows on Ubuntu

**原文标题**: Win-V combo from Windows on Ubuntu

**原文链接**: [https://leo98ml.github.io/win-v/](https://leo98ml.github.io/win-v/)

生成摘要时出错

---

## 71. GLM-5.3 Artificial Analysis Benchmarks

**原文标题**: GLM-5.3 Artificial Analysis Benchmarks

**原文链接**: [https://artificialanalysis.ai/models/glm-5-3](https://artificialanalysis.ai/models/glm-5-3)

生成摘要时出错

---

## 72. Fixing a bricked Framework laptop

**原文标题**: Fixing a bricked Framework laptop

**原文链接**: [https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/](https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/)

生成摘要时出错

---

## 73. Nvidia's new financial strategy does not compute

**原文标题**: Nvidia's new financial strategy does not compute

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/981668/nvidias-goldman-blackrock-gpu-compute-asset](https://www.theverge.com/ai-artificial-intelligence/981668/nvidias-goldman-blackrock-gpu-compute-asset)

生成摘要时出错

---

## 74. AI Has Plunged the Book Publishing Industry into Utter Chaos

**原文标题**: AI Has Plunged the Book Publishing Industry into Utter Chaos

**原文链接**: [https://www.wsj.com/arts-culture/books/generative-ai-book-publishing-be79a287](https://www.wsj.com/arts-culture/books/generative-ai-book-publishing-be79a287)

生成摘要时出错

---

## 75. 2,500-year-old sculpture discovered at UNESCO site in Turkey

**原文标题**: 2,500-year-old sculpture discovered at UNESCO site in Turkey

**原文链接**: [https://www.theartnewspaper.com/2026/08/07/colossal-2500-year-old-sculpture-discovered-turkey-unesco-site](https://www.theartnewspaper.com/2026/08/07/colossal-2500-year-old-sculpture-discovered-turkey-unesco-site)

生成摘要时出错

---

## 76. "Sabotage": Experts, lawmakers blast RFK Jr. for destroying healthcare research

**原文标题**: "Sabotage": Experts, lawmakers blast RFK Jr. for destroying healthcare research

**原文链接**: [https://arstechnica.com/health/2026/08/sabotage-experts-lawmakers-blast-rfk-jr-for-destroying-healthcare-research/](https://arstechnica.com/health/2026/08/sabotage-experts-lawmakers-blast-rfk-jr-for-destroying-healthcare-research/)

生成摘要时出错

---

## 77. Show HN: Openleetcode – Local LeetCode runner where tests live in the repo

**原文标题**: Show HN: Openleetcode – Local LeetCode runner where tests live in the repo

**原文链接**: [https://github.com/therepanic/openleetcode](https://github.com/therepanic/openleetcode)

生成摘要时出错

---

## 78. Linux 7.3 improves performance when running out of vRAM

**原文标题**: Linux 7.3 improves performance when running out of vRAM

**原文链接**: [https://pixelcluster.dev/VRAM-Overcommit/](https://pixelcluster.dev/VRAM-Overcommit/)

生成摘要时出错

---

## 79. The 90-year history of the binoculars bolted to scenic overlooks

**原文标题**: The 90-year history of the binoculars bolted to scenic overlooks

**原文链接**: [https://www.dpreview.com/news/the-90-year-history-of-the-binoculars-bolted-to-scenic-overlooks/](https://www.dpreview.com/news/the-90-year-history-of-the-binoculars-bolted-to-scenic-overlooks/)

生成摘要时出错

---

## 80. Google has acquired the data of failed US airline Spirit

**原文标题**: Google has acquired the data of failed US airline Spirit

**原文链接**: [https://www.theregister.com/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962](https://www.theregister.com/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962)

生成摘要时出错

---

## 81. Norway should buy OpenAI

**原文标题**: Norway should buy OpenAI

**原文链接**: [https://www.onethousandmeans.com/p/norway-should-buy-openai](https://www.onethousandmeans.com/p/norway-should-buy-openai)

生成摘要时出错

---

## 82. We've flown a radiation-blocking vest to the Moon and back, and it worked

**原文标题**: We've flown a radiation-blocking vest to the Moon and back, and it worked

**原文链接**: [https://arstechnica.com/science/2026/08/weve-flown-a-radiation-blocking-vest-to-the-moon-and-back-and-it-worked/](https://arstechnica.com/science/2026/08/weve-flown-a-radiation-blocking-vest-to-the-moon-and-back-and-it-worked/)

生成摘要时出错

---

## 83. Evolve: An incremental game about evolving a civilization

**原文标题**: Evolve: An incremental game about evolving a civilization

**原文链接**: [https://pmotschmann.github.io/Evolve/](https://pmotschmann.github.io/Evolve/)

生成摘要时出错

---

## 84. Field measurements of neighborhood-scale air temperature impacts of data centers

**原文标题**: Field measurements of neighborhood-scale air temperature impacts of data centers

**原文链接**: [https://asmedigitalcollection.asme.org/sustainablebuildings/article/7/2/024501/1233035/Data-Center-Waste-Heat-as-an-Emerging-Urban](https://asmedigitalcollection.asme.org/sustainablebuildings/article/7/2/024501/1233035/Data-Center-Waste-Heat-as-an-Emerging-Urban)

生成摘要时出错

---

## 85. Programmable Property-Based Testing

**原文标题**: Programmable Property-Based Testing

**原文链接**: [https://dl.acm.org/doi/10.1145/3828685](https://dl.acm.org/doi/10.1145/3828685)

生成摘要时出错

---

## 86. Show HN: Saggar, a Mac terminal that keeps sessions and your attention organized

**原文标题**: Show HN: Saggar, a Mac terminal that keeps sessions and your attention organized

**原文链接**: [https://saggar.marginalutility.dev/](https://saggar.marginalutility.dev/)

生成摘要时出错

---

## 87. Fairphone is now officially available in the United States

**原文标题**: Fairphone is now officially available in the United States

**原文链接**: [https://www.fairphone.com/nl/stories/the-fairphone-gen-6-is-all-about-giving-you-more](https://www.fairphone.com/nl/stories/the-fairphone-gen-6-is-all-about-giving-you-more)

生成摘要时出错

---

## 88. Moderna and Merck say mRNA cancer vaccine succeeded in late-stage melanoma trial

**原文标题**: Moderna and Merck say mRNA cancer vaccine succeeded in late-stage melanoma trial

**原文链接**: [https://www.statnews.com/2026/08/19/mrna-cancer-vaccine-trial-melanoma-merck-moderna/](https://www.statnews.com/2026/08/19/mrna-cancer-vaccine-trial-melanoma-merck-moderna/)

生成摘要时出错

---

## 89. Babies born under sugar rationing grew into adults with lower cancer risk

**原文标题**: Babies born under sugar rationing grew into adults with lower cancer risk

**原文链接**: [https://theconversation.com/babies-born-under-sugar-rationing-grew-into-adults-with-lower-cancer-risk-289873](https://theconversation.com/babies-born-under-sugar-rationing-grew-into-adults-with-lower-cancer-risk-289873)

生成摘要时出错

---

