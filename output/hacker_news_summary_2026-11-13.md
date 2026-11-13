# Hacker News 热门文章摘要 (2026-11-13)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 美国联邦航空管理局发布全美地面停飞指令

**原文标题**: FAA Issues National Ground Stop

**原文链接**: [https://www.fly.faa.gov/adv/adv_otherdis?adv_date=11132026&advn=111](https://www.fly.faa.gov/adv/adv_otherdis?adv_date=11132026&advn=111)

根据提供的内容，以下是简要总结：

尽管标题显示为“全国地面停飞”，但美国联邦航空管理局（FAA）空中交通管制系统指挥中心（ATCSCC）提供的文本明确指出，目前**没有正在生效的咨询通知**。

内容由标准的网站导航链接、格式化的法律声明以及 FAA 咨询门户的技术查看器组成。关键信息是状态更新“无咨询通知（NO Advisory）”，这表明根据该特定来源，目前没有任何生效的地面停飞或空中交通警报。

---

## 2. 价值1140万美元的英伟达硬件在从加州运往德州的途中不翼而飞

**原文标题**: $11.4M in Nvidia hardware vanishes during shipment from CA to TX

**原文链接**: [https://www.freightwaves.com/news/11-4-million-in-nvidia-hardware-vanishes-during-shipment-from-california-to-texas](https://www.freightwaves.com/news/11-4-million-in-nvidia-hardware-vanishes-during-shipment-from-california-to-texas)

价值约1140万美元的英伟达（NVIDIA）计算机硬件在从加利福尼亚州奥克兰运往德克萨斯州沃斯堡的途中失踪。这批货物共计六个托盘，于2026年8月29日由一辆印有食品运输公司标志的卡车取走。调查人员在追踪该车经过数个长时间停靠点后，在圣贝纳迪诺县失去了其踪迹。

奥克兰警察局（OPD）在9月13日接到正式报案后，目前正展开重大盗窃案调查。虽然当局尚未正式确认货物估值或货主的具体身份，但此次失踪事件发生的背景是全行业高价值数据中心货运盗窃案正呈激增态势，损失总计已近1.11亿美元。

此次事件是北加州针对英伟达产品的一系列类似犯罪中的最新一起。2025年，弗里蒙特和联合市发生了价值超过750万美元的硬件失窃案。最近，窃贼还盗走了带有英伟达标识的拖车，但随后发现其中仅装有沙子——这是在货运劫案中用于争取时间的策略。

截至目前，尚未有人员被捕，被盗财物也尚未追回。英伟达尚未就此损失发表声明。此案凸显了货运欺诈风险的不断升级，以及在运输高价值技术产品时，加强承运人核验和运输透明度的迫切需求。

---

## 3. FM-1 工作台

**原文标题**: FM-1 Workbench

**原文链接**: [https://open.m-vave.com/fm1-workbench](https://open.m-vave.com/fm1-workbench)

生成摘要时出错

---

## 4. 经过600次实验，以下是我对JEPA世界模型的发现

**原文标题**: After 600 experiments, here's what I discovered about JEPA world models

**原文链接**: [https://haddyalchaer.com/jepa](https://haddyalchaer.com/jepa)

本文详细介绍了在联合嵌入预测架构 (JEPA) —— LeWorldModel (LeWM) 上进行的 600 次实验，重点针对 Push-T 机器人基准测试。作者的核心发现是，LeWM 的预测准确性已经可以媲美完美的物理模型；因此，长程任务的主要瓶颈不在于模型的权重，而在于其规划策略。

作者提出了四种无需额外训练即可提升性能的零样本改进方案：

1.  **分层子目标：** 将 75 步的任务分解为 25 步的片段，使成功率从 22% 提高到 80%，因为该模型在短时域内具有极高的准确度。
2.  **潜在记忆图：** 通过将专家演示的嵌入向量连接成图，并为不同演示之间的跳转添加“代价”，规划器可以利用过去的经验作为子目标来引导长程路径。
3.  **变换记忆：** 为了处理分布外目标，作者利用对称性（旋转或镜像现有数据）来填补记忆图中的空白。这使得模型能够在不存在原始演示的区域取得成功。
4.  **精细化目标评分：** 作者发现，规划时若试图精确匹配目标图像中推手的准确位置，往往会阻碍成功。通过将代价函数集中在物体（方块）而非推手上，或将预测结果与多个有效的推手最终状态进行对比，成功率显著提升。

最终，这些改进将长程任务的成功率从 22% 提升至 85%。研究结果表明，JEPA 世界模型的未来在于更复杂的分层规划，以及自主生成超出现有训练数据范围的子目标。

---

## 5. 逆向工程我的 Coway 空气净化器，摆脱云端依赖

**原文标题**: Reverse engineering my Coway air purifier to ditch the cloud

**原文链接**: [https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/](https://scottjg.com/posts/2026-11-11-reverse-engineering-my-coway-air-purifier-to-ditch-the-cloud/)

本文详细介绍了一个对 Coway Airmega IconS 空气净化器进行逆向工程的技术项目，旨在将其控制权从不稳定的云端应用迁移至集成 Home Assistant 和 Apple Home 的本地环境中。

作者的核心初衷是解决 Coway “IoCare” 云服务频繁宕机、API 变更及账号受限等可靠性问题。为了实现本地控制，作者利用配置为无线接入点的树莓派搭建了中间人（MitM）环境。通过 `mitmproxy` 路由设备流量，作者发现了一个关键设计缺陷：该设备通过未加密的 HTTP 下载根 CA 证书来引导其安全机制。这一漏洞允许作者拦截引导请求并注入自定义证书。一旦设备信任了本地 CA，作者便能解密并分析其 HTTPS 和 MQTT（消息队列遥测传输）流量。分析表明，净化器通过特定的 API 调用获取连接参数，包括 MQTT 代理地址和安全令牌。

通过篡改这些响应，作者成功将设备重定向至本地 MQTT 服务器，从而实现在局域网内直接发送控制指令（如调节风速），有效地实现了设备的“去云化”。文章最后总结道，通过部署本地引导服务器和 MQTT 代理，用户可以在不依赖 Coway 外部基础设施的情况下，维持空气净化器的完整功能，从而确保长期的可靠性与隐私。

---

## 6. Perplexity Decider v1.3：训练、评估与应用场景

**原文标题**: Perplexity Decider v1.3: Training, eval, and use cases

**原文链接**: [https://www.perplexity.ai/hub/blog/perplexity-decider](https://www.perplexity.ai/hub/blog/perplexity-decider)

Perplexity 最近推出了 **Perplexity Decider v1.3**，这是一款专门的推理模型，旨在充当其 AI 搜索引擎的“交通控制器”。其主要作用是分析用户查询并确定最佳执行路径——决定是否需要进行网页搜索、调用哪些工具以及如何构建回答结构。

**关键技术细节与训练**
Decider v1.3 是一款经过优化的轻量级参数模型（基于 Llama 3 等架构微调而成），旨在平衡高性能与低延迟。为了对其进行训练，Perplexity 采用了复杂的流程，包括：
*   **高质量数据：** 结合了人类专家标注数据以及由更大型“教师”模型生成的合成数据。
*   **优化：** 该模型经过了直接偏好优化 (DPO) 和人类反馈强化学习 (RLHF)，以完善其决策逻辑。

**评估与性能**
在内部基准测试中，v1.3 在特定路由任务上的表现显著优于其前代产品，甚至超过了大型通用模型（如 GPT-4o）。它在以下方面有显著提升：
*   **精确度：** 减少了“幻觉”工具调用，意图分类更加准确。
*   **延迟：** 作为一个更小型的专业化模型，它处理决策的速度比通用大语言模型更快，缩短了用户获取回答的总时长。

**使用场景**
该模型的主要应用是增强“Pro Search”体验。它擅长识别查询是需要多步搜索还是直接回答。它还为“Pro Check”功能提供支持，模型会评估其是否拥有足够的信息来继续操作，还是需要向用户提出澄清性问题。通过完善这一“决策”阶段，Perplexity 在保持界面快速响应的同时，能够提供更具相关性且有引用支持的结果。

---

## 7. KORS 机场所有频率的实时航空波段。加拿大维多利亚机场也已实施地面停飞。

**原文标题**: Live airband on all frequencies from KORS. Victoria, CA also ground stopped

**原文链接**: [https://orcasairband.com/](https://orcasairband.com/)

根据提供的标题，以下是情况的简要总结：

该报告监控以 **KORS**（奥卡斯岛机场）和 **Victoria**（很可能是维多利亚国际机场）为中心的实时航空活动。主要包含以下两项进展：

1.  **实时航空波段监控：** KORS 目前正在广播所有可用频率的实时无线电传输。这使得能够实时跟踪该扇区内空中交通管制员与飞行员之间的通讯。
2.  **维多利亚地面停飞：** 维多利亚机场已实施地面停飞指令。这是一种战术性空中交通管制措施，旨在暂停飞往或离开该机场的航班，通常由恶劣天气、设备故障或安全事件引起。

由于提供的内容为直播标题，这些要点代表了该区域领空的当前运行状态。

---

## 8. Found: A protein that drives ageing without unleashing inflammation

**原文标题**: Found: A protein that drives ageing without unleashing inflammation

**原文链接**: [https://www.nature.com/articles/d41586-026-03638-3](https://www.nature.com/articles/d41586-026-03638-3)

根据提供的文章，以下是内容摘要：

**摘要：酶的新发现为抗衰老提供新路径**

研究人员发现了一种在驱动身体组织衰老中起关键作用的特定酶。在发表于《免疫》（Immunity, 2026）杂志的一项研究中，科学家们发现，通过生物工程技术缺失该蛋白质的小鼠，其与年龄相关的肝脏退化（特别是在组织硬化和纤维化方面）显著减轻。

这一发现是长寿科学领域的重大突破，因为它提出了一种可以应对衰老的物理影响且不产生常见副作用的方法。目前许多抗衰老干预措施可能会无意中抑制免疫系统或引发有害炎症。然而，这种特定的蛋白质似乎通过某种路径驱动组织衰败，如果抑制该路径，则不会损害人体的天然免疫防御功能。

这一发现为未来开发旨在降低人体内该酶水平的药物奠定了基础。此类治疗方法有望对抗与年龄相关的器官衰竭和组织流失，在保持免疫系统完好的同时，助力老年群体维持身体健康。

---

## 9. Autonomous (YC F25) 招聘 MTS，构建管理个人财富的 AI 智能体。

**原文标题**: Autonomous (YC F25) is hiring MTS to build AI agents that manage your wealth

**原文链接**: [https://atg.science/careers](https://atg.science/careers)

生成摘要时出错

---

## 10. Doomsday: Friday, 13 November, A.D. 2026 (1960)

**原文标题**: Doomsday: Friday, 13 November, A.D. 2026 (1960)

**原文链接**: [https://www.science.org/doi/10.1126/science.132.3436.1291](https://www.science.org/doi/10.1126/science.132.3436.1291)

在1960年发表于《科学》杂志的文章《末日：公元2026年11月13日，星期五》中，海因茨·冯·福斯特、帕特里夏·M·莫拉和劳伦斯·W·阿米奥特对人类人口增长进行了数学分析，对传统的指数增长模型提出了挑战。

作者认为，人类人口的增长是“超指数级”的，而不仅仅是指数级的。他们指出，人类的独特之处在于形成了一个全球性的“联盟”，在这个联盟中，人口密度的增加促进了更好的沟通和技术进步。这种集体智慧使人类能够系统地克服环境障碍并降低死亡率，从而创造出一个正反馈循环：随着人口增加，供养更多人口的能力也随之增长。

通过将数学公式应用于跨越两千年的历史人口数据，作者计算出了一个数学奇点——即理论上人口密度将达到无穷大的点。计算得出的日期为2026年11月13日。

作者并非意图将这个“末日”日期视为对自然灾害或世界末日的字面预言。相反，它是对持续增长趋势在物理上之不可能性的警告。他们曾留下著名的论断：在这一天，我们的后代不会死于饥饿，而是会被庞大的人口数量“挤死”。

这篇文章是对人口趋势的一次挑衅式批判，说明人类增长无法按照历史轨迹无限持续。它表明，除非社会或生物因素介入以改变增长参数，否则数学上的结论便是奇点处的崩溃。由于该论文较早地识别了人类技术与合作如何影响人口动态，它在系统论和人口学领域至今仍具有重要意义。

---

## 11. Big tech is here to let us down

**原文标题**: Big tech is here to let us down

**原文链接**: [https://blog.jsweeting.me/big-tech-is-here-to-let-us-down](https://blog.jsweeting.me/big-tech-is-here-to-let-us-down)

生成摘要时出错

---

## 12. Live-migration support in FreeBSD and bhyve coming

**原文标题**: Live-migration support in FreeBSD and bhyve coming

**原文链接**: [https://gyptazy.com/blog/freebsd-bhyve-live-migration-support-rfc/](https://gyptazy.com/blog/freebsd-bhyve-live-migration-support-rfc/)

FreeBSD 15.1 has introduced a working prototype for the live migration of bhyve guests on amd64 architecture. This project, currently a Work In Progress (WIP) RFC, allows running virtual machines to move between hosts over TCP with minimal downtime—observed at roughly 138–171 ms for small guests.

**Technical Implementation**
The process utilizes a pre-copy mechanism that builds on bhyve’s experimental snapshot support. It iteratively tracks and transfers "dirty" memory pages while the guest is running. Once the remaining data reaches a target threshold, the guest is briefly paused for a final "stop-and-copy" phase. The implementation includes a migration protocol in `bhyve` and `bhyvectl` that ensures a "commit point" is reached at the destination before the source guest is retired.

**Significance**
Live migration is a critical requirement for enterprise virtualization, enabling host maintenance, hardware replacement, and load balancing without service outages. It is central to the development of **Sylve** (a Proxmox-like cluster solution for FreeBSD) and **BoxyBSD** (a VPS provider).

**Current Status and Road to Upstreaming**
While successful in initial tests involving multi-vCPU support and disk-write validation, several "blockers" must be addressed before the code can be officially upstreamed:
*   **Hardening:** Proving the correctness of the kernel-side dirty-page tracking algorithm.
*   **Security:** Adding authentication and encryption to the currently unencrypted TCP transport.
*   **Compatibility:** Establishing strict contracts to ensure destination hosts match the source’s CPU capabilities and device topologies.
*   **Standardization:** Clarifying network/storage handoffs and creating automated in-tree regression tests.

The code is being published on GitHub and Git.gyptazy.com to solicit community feedback, with a primary focus on correctness and stability before moving toward performance optimizations like compression.

---

## 13. Ctrl+C, Ctrl+v, Ctrl+cve: Bypassing Android's Clipboard Read Security Measures

**原文标题**: Ctrl+C, Ctrl+v, Ctrl+cve: Bypassing Android's Clipboard Read Security Measures

**原文链接**: [https://toninoble.com/post/ctrlc-ctrlv-ctrlcve](https://toninoble.com/post/ctrlc-ctrlv-ctrlcve)

生成摘要时出错

---

## 14. Show HN: Isometric SF – A pixel-art map of the SF Bay Area

**原文标题**: Show HN: Isometric SF – A pixel-art map of the SF Bay Area

**原文链接**: [https://isometricsf.com/](https://isometricsf.com/)

生成摘要时出错

---

## 15. All US airports are currently ground stopped

**原文标题**: All US airports are currently ground stopped

**原文链接**: [https://twitter.com/flightradar24/status/2121347654714077605](https://twitter.com/flightradar24/status/2121347654714077605)

生成摘要时出错

---

## 16. A technical vision for the Haskell ecosystem

**原文标题**: A technical vision for the Haskell ecosystem

**原文链接**: [https://discourse.haskell.org/t/a-technical-vision-for-the-haskell-ecosystem/15078](https://discourse.haskell.org/t/a-technical-vision-for-the-haskell-ecosystem/15078)

生成摘要时出错

---

## 17. AI unlocks Gödel's notebooks, said to contain hundreds of proved theorems

**原文标题**: AI unlocks Gödel's notebooks, said to contain hundreds of proved theorems

**原文链接**: [https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths](https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths)

生成摘要时出错

---

## 18. Minnesota guitarist's "palmfrets" invention strikes a new chord

**原文标题**: Minnesota guitarist's "palmfrets" invention strikes a new chord

**原文链接**: [https://www.echopress.com/business/minnesota-guitarists-invention-strikes-a-new-chord](https://www.echopress.com/business/minnesota-guitarists-invention-strikes-a-new-chord)

生成摘要时出错

---

## 19. Models can now transmit viruses in weight-space

**原文标题**: Models can now transmit viruses in weight-space

**原文链接**: [https://www.alphaxiv.org/abs/2611.weight-space-misfolding](https://www.alphaxiv.org/abs/2611.weight-space-misfolding)

生成摘要时出错

---

## 20. FAA issues nationwide ground stop due to "extraordinary circumstances"

**原文标题**: FAA issues nationwide ground stop due to "extraordinary circumstances"

**原文链接**: [https://www.axios.com/2026/11/13/faa-nationwide-ground-stop](https://www.axios.com/2026/11/13/faa-nationwide-ground-stop)

生成摘要时出错

---

## 21. It Takes 16 Clicks for a Student to Open a PowerPoint on an iPad

**原文标题**: It Takes 16 Clicks for a Student to Open a PowerPoint on an iPad

**原文链接**: [https://www.reddit.com/r/Teachers/comments/1xuup7a/technology_sucks_it_literally_takes_16_clicks_for/](https://www.reddit.com/r/Teachers/comments/1xuup7a/technology_sucks_it_literally_takes_16_clicks_for/)

生成摘要时出错

---

## 22. Lonewolf 0.3 – A standalone XMPP server written in Rust

**原文标题**: Lonewolf 0.3 – A standalone XMPP server written in Rust

**原文链接**: [https://github.com/lonewolf-im/lonewolf/releases/tag/v0.3.0](https://github.com/lonewolf-im/lonewolf/releases/tag/v0.3.0)

生成摘要时出错

---

## 23. Apify Security Incident

**原文标题**: Apify Security Incident

**原文链接**: [https://status.apify.com/incidents/sxd1dj5j6749](https://status.apify.com/incidents/sxd1dj5j6749)

生成摘要时出错

---

## 24. 欧洲核子研究中心研制出大型强子对撞机的下一代磁体。

**原文标题**: CERN Built the Large Hadron Collider's Next-Gen Magnets

**原文链接**: [https://spectrum.ieee.org/large-hadron-collider-superconducting-magnets](https://spectrum.ieee.org/large-hadron-collider-superconducting-magnets)

生成摘要时出错

---

## 25. No AI Slop: A Manifesto

**原文标题**: No AI Slop: A Manifesto

**原文链接**: [https://www.slopmanifesto.com/](https://www.slopmanifesto.com/)

生成摘要时出错

---

## 26. OpenAI disbands its robotics team as its general models start running robots

**原文标题**: OpenAI disbands its robotics team as its general models start running robots

**原文链接**: [https://fortune.com/2026/11/13/openai-disbands-robotics-team-as-its-general-models-start-running-robots/](https://fortune.com/2026/11/13/openai-disbands-robotics-team-as-its-general-models-start-running-robots/)

生成摘要时出错

---

## 27. Someone's Impersonating This Blog

**原文标题**: Someone's Impersonating This Blog

**原文链接**: [https://mattbee.mataroa.blog/p/someones-impersonating-this-blog/](https://mattbee.mataroa.blog/p/someones-impersonating-this-blog/)

生成摘要时出错

---

## 28. Technology as a Search Problem

**原文标题**: Technology as a Search Problem

**原文链接**: [https://www.construction-physics.com/p/technology-as-a-search-problem](https://www.construction-physics.com/p/technology-as-a-search-problem)

生成摘要时出错

---

## 29. Microsoft outage gives customers a crash course in dependence on Redmond

**原文标题**: Microsoft outage gives customers a crash course in dependence on Redmond

**原文链接**: [https://www.theregister.com/saas/2026/11/13/microsoft-outage-gives-customers-a-crash-course-in-dependence-on-redmond/5309805](https://www.theregister.com/saas/2026/11/13/microsoft-outage-gives-customers-a-crash-course-in-dependence-on-redmond/5309805)

生成摘要时出错

---

## 30. Concurrent Shell Command Queues

**原文标题**: Concurrent Shell Command Queues

**原文链接**: [https://emmer.dev/blog/concurrent-shell-command-queues/](https://emmer.dev/blog/concurrent-shell-command-queues/)

生成摘要时出错

---

## 31. LibreOffice actually works 365 days a year

**原文标题**: LibreOffice actually works 365 days a year

**原文链接**: [https://twitter.com/LibreOffice/status/2121205272479998268](https://twitter.com/LibreOffice/status/2121205272479998268)

生成摘要时出错

---

## 32. Elevated errors on claude.ai, Claude Code, and platform.claude.com

**原文标题**: Elevated errors on claude.ai, Claude Code, and platform.claude.com

**原文链接**: [https://status.claude.com/incidents/nn11wk485zfn](https://status.claude.com/incidents/nn11wk485zfn)

生成摘要时出错

---

## 33. Brazil's Caixa insurer breach exposes names and tax IDs of all 7.6M customers

**原文标题**: Brazil's Caixa insurer breach exposes names and tax IDs of all 7.6M customers

**原文链接**: [https://filemanager-cdn.mziq.com/published/3972906b-e50b-4f74-ab74-4d0d32125d11/9567a559-d20a-486e-a7ae-5c6bbc030c5e](https://filemanager-cdn.mziq.com/published/3972906b-e50b-4f74-ab74-4d0d32125d11/9567a559-d20a-486e-a7ae-5c6bbc030c5e)

生成摘要时出错

---

## 34. Why is Google cutting off Search from AI-free schools? Here are some theories

**原文标题**: Why is Google cutting off Search from AI-free schools? Here are some theories

**原文链接**: [https://text.npr.org/nx-s1-6029408](https://text.npr.org/nx-s1-6029408)

生成摘要时出错

---

## 35. Starship Flight 15 live

**原文标题**: Starship Flight 15 live

**原文链接**: [https://twitter.com/SpaceX/status/2121316300702056595](https://twitter.com/SpaceX/status/2121316300702056595)

生成摘要时出错

---

## 36. AI is destroying the trust between writers and readers

**原文标题**: AI is destroying the trust between writers and readers

**原文链接**: [https://www.theatlantic.com/books/2026/11/ai-literary-scams-amazon/689391/](https://www.theatlantic.com/books/2026/11/ai-literary-scams-amazon/689391/)

生成摘要时出错

---

## 37. Microsoft is too big to live

**原文标题**: Microsoft is too big to live

**原文链接**: [https://pluralistic.net/2026/11/13/outlookpocalypse/#bright-line-test](https://pluralistic.net/2026/11/13/outlookpocalypse/#bright-line-test)

生成摘要时出错

---

## 38. North Korean hackers used fake video calls in $400M crypto hack, says FBI

**原文标题**: North Korean hackers used fake video calls in $400M crypto hack, says FBI

**原文链接**: [https://www.bbc.com/news/articles/cqdj1ellpd70o](https://www.bbc.com/news/articles/cqdj1ellpd70o)

生成摘要时出错

---

## 39. Agda v2.9.0

**原文标题**: Agda v2.9.0

**原文链接**: [https://github.com/agda/agda/releases/tag/v2.9.0](https://github.com/agda/agda/releases/tag/v2.9.0)

生成摘要时出错

---

## 40. There Was Time Now

**原文标题**: There Was Time Now

**原文链接**: [https://blog.bawolf.com/p/there-was-time-now](https://blog.bawolf.com/p/there-was-time-now)

生成摘要时出错

---

## 41. The Dawn of the Data Intelligence Engineer

**原文标题**: The Dawn of the Data Intelligence Engineer

**原文链接**: [https://motherduck.com/blog/the-data-intelligence-engineer/](https://motherduck.com/blog/the-data-intelligence-engineer/)

生成摘要时出错

---

## 42. DeepSeek Ultrafast

**原文标题**: DeepSeek Ultrafast

**原文链接**: [https://github.com/basetenlabs/deepseek-ultrafast](https://github.com/basetenlabs/deepseek-ultrafast)

生成摘要时出错

---

## 43. Why Zig over C for Systems Programming

**原文标题**: Why Zig over C for Systems Programming

**原文链接**: [https://www.mtsoukalos.eu/2026/11/why-zig-over-c-for-systems-programming/](https://www.mtsoukalos.eu/2026/11/why-zig-over-c-for-systems-programming/)

生成摘要时出错

---

## 44. Rust 1.100

**原文标题**: Rust 1.100

**原文链接**: [https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/](https://blog.rust-lang.org/2026/11/12/Rust-1.100.0/)

生成摘要时出错

---

## 45. Beating benchmarks by weight-space optimizing decision models with DSPy

**原文标题**: Beating benchmarks by weight-space optimizing decision models with DSPy

**原文链接**: [https://www.cmpnd.ai/blog/weight-space-programming-dspy.html](https://www.cmpnd.ai/blog/weight-space-programming-dspy.html)

生成摘要时出错

---

## 46. Are we just going to ignore that books are destroyed for AI?

**原文标题**: Are we just going to ignore that books are destroyed for AI?

**原文链接**: [https://www.forbes.com/sites/maryroeloffs/2026/08/17/ai-companies-are-buying-and-destroying-antique-books-heres-why/](https://www.forbes.com/sites/maryroeloffs/2026/08/17/ai-companies-are-buying-and-destroying-antique-books-heres-why/)

生成摘要时出错

---

## 47. IceWM

**原文标题**: IceWM

**原文链接**: [https://ice-wm.org/](https://ice-wm.org/)

生成摘要时出错

---

## 48. National ground stop throughout the USA happening?

**原文标题**: National ground stop throughout the USA happening?

**原文链接**: [https://www.reddit.com/r/aviation/comments/1xvj4u8/national_ground_stop_throughout_the_usa_happening/](https://www.reddit.com/r/aviation/comments/1xvj4u8/national_ground_stop_throughout_the_usa_happening/)

生成摘要时出错

---

## 49. Brave Search API now accepts agentic payments via the x402 protocol

**原文标题**: Brave Search API now accepts agentic payments via the x402 protocol

**原文链接**: [https://brave.com/blog/search-api-agentic-payments/](https://brave.com/blog/search-api-agentic-payments/)

生成摘要时出错

---

## 50. Jensen Huang resigns

**原文标题**: Jensen Huang resigns

**原文链接**: [https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f](https://apnews.com/article/nvidia-megaspeed-china-singapore-huang-5403f152a601cf82ce939f1d24fffa0f)

生成摘要时出错

---

## 51. Show HN: My $300 embroidery machine needed a subscription, so I built my own app

**原文标题**: Show HN: My $300 embroidery machine needed a subscription, so I built my own app

**原文链接**: [https://github.com/simpsoka/zigzag](https://github.com/simpsoka/zigzag)

生成摘要时出错

---

## 52. US test reactor cleared for operations

**原文标题**: US test reactor cleared for operations

**原文链接**: [https://www.world-nuclear-news.org/articles/us-test-reactor-cleared-for-operations](https://www.world-nuclear-news.org/articles/us-test-reactor-cleared-for-operations)

生成摘要时出错

---

## 53. Most affairs don't matter much. Nvidia Jensen's blunder will rock the world

**原文标题**: Most affairs don't matter much. Nvidia Jensen's blunder will rock the world

**原文链接**: [https://www.theregister.com/columnists/2026/11/13/most-affairs-dont-matter-except-to-the-people-involved-ex-nvidia-ceo-jensens-blunder-will-rock-the-world/5309649](https://www.theregister.com/columnists/2026/11/13/most-affairs-dont-matter-except-to-the-people-involved-ex-nvidia-ceo-jensens-blunder-will-rock-the-world/5309649)

生成摘要时出错

---

## 54. Switcher (2004)

**原文标题**: Switcher (2004)

**原文链接**: [https://folklore.org/Switcher.html](https://folklore.org/Switcher.html)

生成摘要时出错

---

## 55. Arm boss Rene Haas approached in Nvidia CEO search

**原文标题**: Arm boss Rene Haas approached in Nvidia CEO search

**原文链接**: [https://www.ft.com/content/2a64f698-46dd-4178-a3f4-4c5f4c0a0926](https://www.ft.com/content/2a64f698-46dd-4178-a3f4-4c5f4c0a0926)

生成摘要时出错

---

## 56. EU Digital Identity Wallet rollout: every EU state on one board

**原文标题**: EU Digital Identity Wallet rollout: every EU state on one board

**原文链接**: [https://myid.ie/business/eu-digital-wallet-tracker/](https://myid.ie/business/eu-digital-wallet-tracker/)

生成摘要时出错

---

## 57. Show HN: AgentRun – open-source, Self-improving Managed Agents

**原文标题**: Show HN: AgentRun – open-source, Self-improving Managed Agents

**原文链接**: [https://github.com/Parcha-ai/agentrun/blob/main/README.md](https://github.com/Parcha-ai/agentrun/blob/main/README.md)

生成摘要时出错

---

## 58. Former Nvidia CEO Huang had a relationship with a second employee, sources say

**原文标题**: Former Nvidia CEO Huang had a relationship with a second employee, sources say

**原文链接**: [https://www.reuters.com/technology/former-nvidia-ceo-huang-had-relationship-with-second-employee-sources-say-2026-11-12/](https://www.reuters.com/technology/former-nvidia-ceo-huang-had-relationship-with-second-employee-sources-say-2026-11-12/)

生成摘要时出错

---

## 59. Talking Zen 6 with Mike Clark at AMD In-Depth

**原文标题**: Talking Zen 6 with Mike Clark at AMD In-Depth

**原文链接**: [https://chipsandcheese.com/p/talking-zen-6-with-mike-clark-at](https://chipsandcheese.com/p/talking-zen-6-with-mike-clark-at)

生成摘要时出错

---

## 60. Gemini 4 Hydrogen and Orchestrator

**原文标题**: Gemini 4 Hydrogen and Orchestrator

**原文链接**: [https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/](https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity/)

生成摘要时出错

---

## 61. Relax: JIT compiler for Rust to reduce build times

**原文标题**: Relax: JIT compiler for Rust to reduce build times

**原文链接**: [https://makepad.github.io/relax/](https://makepad.github.io/relax/)

生成摘要时出错

---

## 62. US wide ground stop (Nov 13)

**原文标题**: US wide ground stop (Nov 13)

**原文链接**: [https://www.pprune.org/rumours-news/674910-us-wide-ground-stop-nov-13-a.html](https://www.pprune.org/rumours-news/674910-us-wide-ground-stop-nov-13-a.html)

生成摘要时出错

---

## 63. Show HN: Log every LLM call with tokens, cost, latency, and time to first token

**原文标题**: Show HN: Log every LLM call with tokens, cost, latency, and time to first token

**原文链接**: [https://github.com/garritfra/llmtee](https://github.com/garritfra/llmtee)

生成摘要时出错

---

## 64. Dwarf planet candidate appears which takes roughly 280 years to orbit our sun

**原文标题**: Dwarf planet candidate appears which takes roughly 280 years to orbit our sun

**原文链接**: [https://www.smithsonianmag.com/smart-news/astronomers-found-a-mysterious-object-orbiting-far-beyond-pluto-it-could-be-a-new-dwarf-planet-hidden-in-our-solar-system-180989857/](https://www.smithsonianmag.com/smart-news/astronomers-found-a-mysterious-object-orbiting-far-beyond-pluto-it-could-be-a-new-dwarf-planet-hidden-in-our-solar-system-180989857/)

生成摘要时出错

---

## 65. FAA imposes nationwide ground stop on all flights

**原文标题**: FAA imposes nationwide ground stop on all flights

**原文链接**: [https://www.washingtonexaminer.com/policy/infrastructure/4802941/faa-imposes-nationwide-ground-stop-on-all-flights/](https://www.washingtonexaminer.com/policy/infrastructure/4802941/faa-imposes-nationwide-ground-stop-on-all-flights/)

生成摘要时出错

---

## 66. A dumb copyright law makes it illegal to remove the spyware from your own TV

**原文标题**: A dumb copyright law makes it illegal to remove the spyware from your own TV

**原文链接**: [https://boingboing.net/2026/11/12/fountain-pen-fulu-smart-tv-spyware-dmca.html](https://boingboing.net/2026/11/12/fountain-pen-fulu-smart-tv-spyware-dmca.html)

生成摘要时出错

---

## 67. Sift: LSP, Lint, Format Lisp, Scheme and Emacs Lisp

**原文标题**: Sift: LSP, Lint, Format Lisp, Scheme and Emacs Lisp

**原文链接**: [https://github.com/jjba23/sift](https://github.com/jjba23/sift)

生成摘要时出错

---

## 68. FAA issues nationwide ground stop

**原文标题**: FAA issues nationwide ground stop

**原文链接**: [https://www.cnbc.com/2026/11/13/faa-ground-stop.html](https://www.cnbc.com/2026/11/13/faa-ground-stop.html)

生成摘要时出错

---

## 69. Edge0-145B: Frontier AI Capabilities on Your Own Computer

**原文标题**: Edge0-145B: Frontier AI Capabilities on Your Own Computer

**原文链接**: [https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer](https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer)

生成摘要时出错

---

## 70. Our software engineering interviews are changing a little

**原文标题**: Our software engineering interviews are changing a little

**原文链接**: [https://blog.janestreet.com/software-engineering-interviews-are-changing-a-little/](https://blog.janestreet.com/software-engineering-interviews-are-changing-a-little/)

生成摘要时出错

---

## 71. Gemini 4 Hydrogen

**原文标题**: Gemini 4 Hydrogen

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)

生成摘要时出错

---

## 72. Ed Zitron on CNN's Laura Coates Live 11/12/26

**原文标题**: Ed Zitron on CNN's Laura Coates Live 11/12/26

**原文链接**: [https://www.youtube.com/watch?v=Mn2HhRx0NgY](https://www.youtube.com/watch?v=Mn2HhRx0NgY)

生成摘要时出错

---

## 73. Show HN: Cal.flare – cal.diy ported to Cloudflare Workers

**原文标题**: Show HN: Cal.flare – cal.diy ported to Cloudflare Workers

**原文链接**: [https://github.com/ralphbibera/cal.flare](https://github.com/ralphbibera/cal.flare)

生成摘要时出错

---

## 74. Microsoft Outlook/365 still down after 12 hours

**原文标题**: Microsoft Outlook/365 still down after 12 hours

**原文链接**: [https://twitter.com/MSFT365Status/status/2121079061774491735](https://twitter.com/MSFT365Status/status/2121079061774491735)

生成摘要时出错

---

## 75. Researchers discover rare star system that emits radio signals every 8 minutes

**原文标题**: Researchers discover rare star system that emits radio signals every 8 minutes

**原文链接**: [https://www.curtin.edu.au/news/media-release/researchers-discover-rare-star-system-that-emits-radio-signals-every-eight-minutes/](https://www.curtin.edu.au/news/media-release/researchers-discover-rare-star-system-that-emits-radio-signals-every-eight-minutes/)

生成摘要时出错

---

## 76. Mozilla leaves Solo website owners to go it alone as hosting shuts down

**原文标题**: Mozilla leaves Solo website owners to go it alone as hosting shuts down

**原文链接**: [https://www.theregister.com/software/2026/11/13/mozilla-leaves-solo-website-owners-to-go-it-alone-as-hosting-shuts-down/5309632](https://www.theregister.com/software/2026/11/13/mozilla-leaves-solo-website-owners-to-go-it-alone-as-hosting-shuts-down/5309632)

生成摘要时出错

---

## 77. Service degradation on Microsoft 365

**原文标题**: Service degradation on Microsoft 365

**原文链接**: [https://status.cloud.microsoft/](https://status.cloud.microsoft/)

生成摘要时出错

---

## 78. I'm making LLMs work on small and old devices

**原文标题**: I'm making LLMs work on small and old devices

**原文链接**: [https://github.com/hyperionaidev/smolmaxxing/](https://github.com/hyperionaidev/smolmaxxing/)

生成摘要时出错

---

## 79. Libreagi – Save OSS Models

**原文标题**: Libreagi – Save OSS Models

**原文链接**: [https://libreagi.com/](https://libreagi.com/)

生成摘要时出错

---

## 80. Tim Peters has died

**原文标题**: Tim Peters has died

**原文链接**: [https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028](https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028)

生成摘要时出错

---

## 81. Global Microsoft Outage

**原文标题**: Global Microsoft Outage

**原文链接**: [https://www.cnn.com/2026/11/12/business/live-news/microsoft-global-outage-intl-hnk](https://www.cnn.com/2026/11/12/business/live-news/microsoft-global-outage-intl-hnk)

生成摘要时出错

---

## 82. Some Projects Need to Fail

**原文标题**: Some Projects Need to Fail

**原文链接**: [https://yusufaytas.com/some-projects-need-to-fail](https://yusufaytas.com/some-projects-need-to-fail)

生成摘要时出错

---

## 83. Nvidia employees petition to bring back Jensen Huang

**原文标题**: Nvidia employees petition to bring back Jensen Huang

**原文链接**: [https://www.wired.com/story/nvidia-employees-petition-for-jensen-huangs-return/](https://www.wired.com/story/nvidia-employees-petition-for-jensen-huangs-return/)

生成摘要时出错

---

## 84. ExcalidrawZ: Local Native Excalidraw on macOS/iOS

**原文标题**: ExcalidrawZ: Local Native Excalidraw on macOS/iOS

**原文链接**: [https://github.com/chocoford/ExcalidrawZ](https://github.com/chocoford/ExcalidrawZ)

生成摘要时出错

---

## 85. Adapting CPython for Yk

**原文标题**: Adapting CPython for Yk

**原文链接**: [https://tratt.net/laurie/blog/2026/adapting_cpython_for_yk.html](https://tratt.net/laurie/blog/2026/adapting_cpython_for_yk.html)

生成摘要时出错

---

## 86. Making a €40 USB-C hub work as a Nintendo Switch 2 dock

**原文标题**: Making a €40 USB-C hub work as a Nintendo Switch 2 dock

**原文链接**: [http://blog.nozomi.space/posts/sw2_dock/](http://blog.nozomi.space/posts/sw2_dock/)

生成摘要时出错

---

## 87. Chinese frontier AI models carry the fingerprint of export-controlled GPUs

**原文标题**: Chinese frontier AI models carry the fingerprint of export-controlled GPUs

**原文链接**: [https://unemploymentlabs.com/checkpoint-forensics](https://unemploymentlabs.com/checkpoint-forensics)

生成摘要时出错

---

## 88. Vibes Don't Maintain

**原文标题**: Vibes Don't Maintain

**原文链接**: [https://roll.bybacon.com/2026/10/14/vibes-dont-maintain.html](https://roll.bybacon.com/2026/10/14/vibes-dont-maintain.html)

生成摘要时出错

---

## 89. Foundation Models framework

**原文标题**: Foundation Models framework

**原文链接**: [https://developer.apple.com/foundation-models-framework/](https://developer.apple.com/foundation-models-framework/)

生成摘要时出错

---

## 90. Show HN: Reflota – Open-source data recovery for NTFS/FAT disks with phased copy

**原文标题**: Show HN: Reflota – Open-source data recovery for NTFS/FAT disks with phased copy

**原文链接**: [https://github.com/Christ10-8/reflota](https://github.com/Christ10-8/reflota)

生成摘要时出错

---

## 91. Microsoft outage 'stark reminder' of how much we rely on tech

**原文标题**: Microsoft outage 'stark reminder' of how much we rely on tech

**原文链接**: [https://www.bbc.com/news/articles/cxzd9171m51qo](https://www.bbc.com/news/articles/cxzd9171m51qo)

生成摘要时出错

---

## 92. Apple has new Mac app coming to make running local AI models easy

**原文标题**: Apple has new Mac app coming to make running local AI models easy

**原文链接**: [https://9to5mac.com/2026/11/10/apple-has-new-mac-app-coming-to-make-running-local-ai-models-easy/](https://9to5mac.com/2026/11/10/apple-has-new-mac-app-coming-to-make-running-local-ai-models-easy/)

生成摘要时出错

---

## 93. Abandoned Quake 4 expansion finished by modders and now playable

**原文标题**: Abandoned Quake 4 expansion finished by modders and now playable

**原文链接**: [https://www.moddb.com/mods/openq4/downloads/openq4-0141-windows-x64](https://www.moddb.com/mods/openq4/downloads/openq4-0141-windows-x64)

生成摘要时出错

---

## 94. Writing correct software is hard and math alone won’t help us (2016)

**原文标题**: Writing correct software is hard and math alone won’t help us (2016)

**原文链接**: [https://pron.github.io/posts/correctness-and-complexity](https://pron.github.io/posts/correctness-and-complexity)

生成摘要时出错

---

## 95. Congrats, you survived the scheduled human extinction

**原文标题**: Congrats, you survived the scheduled human extinction

**原文链接**: [https://reason.com/2026/11/13/human-extinction-scheduled-forhuh-how-about-that-today/](https://reason.com/2026/11/13/human-extinction-scheduled-forhuh-how-about-that-today/)

生成摘要时出错

---

## 96. Turning a 22-year-old Postgres type-confusion primitive into RCE

**原文标题**: Turning a 22-year-old Postgres type-confusion primitive into RCE

**原文链接**: [https://mehmetince.net/part-3-6-how-i-ended-up-turning-a-22-year-old-postgresql-type-confusion-primitive-into-rce-cve-2026-6460/](https://mehmetince.net/part-3-6-how-i-ended-up-turning-a-22-year-old-postgresql-type-confusion-primitive-into-rce-cve-2026-6460/)

生成摘要时出错

---

## 97. Electric ship batteries promise compact, cooler power

**原文标题**: Electric ship batteries promise compact, cooler power

**原文链接**: [https://spectrum.ieee.org/electric-ship-batteries](https://spectrum.ieee.org/electric-ship-batteries)

生成摘要时出错

---

## 98. Show HN: Hexalexagons, a daily word game on a hexagonal grid

**原文标题**: Show HN: Hexalexagons, a daily word game on a hexagonal grid

**原文链接**: [https://hexalexagons.com/](https://hexalexagons.com/)

生成摘要时出错

---

## 99. AWS emulator

**原文标题**: AWS emulator

**原文链接**: [https://github.com/aws/aws-emulator](https://github.com/aws/aws-emulator)

生成摘要时出错

---

## 100. Tang Nano 20K FPGA replaces chips on a TRS-80 CoCo 1/2 to make it a CoCo 3

**原文标题**: Tang Nano 20K FPGA replaces chips on a TRS-80 CoCo 1/2 to make it a CoCo 3

**原文链接**: [https://hackaday.com/2026/11/12/upgrade-your-coco-the-modern-way/](https://hackaday.com/2026/11/12/upgrade-your-coco-the-modern-way/)

生成摘要时出错

---

