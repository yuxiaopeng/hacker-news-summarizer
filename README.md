# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-13.md)

*最后自动更新时间: 2026-11-13 22:50:07*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-13](output/hacker_news_summary_2026-11-13.md) |
| 2 | [2026-11-11](output/hacker_news_summary_2026-11-11.md) |
| 3 | [2026-11-12](output/hacker_news_summary_2026-11-12.md) |
| 4 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 5 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 6 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 7 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 8 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 9 | [2026-11-10](output/hacker_news_summary_2026-11-10.md) |
| 10 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 11 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 12 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 13 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 14 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 15 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 16 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 17 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 18 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 19 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 20 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 21 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 22 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 23 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 24 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 25 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 26 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 27 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 28 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 29 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 30 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 31 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 32 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 33 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 34 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 35 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 36 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 37 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 38 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 39 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 40 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 41 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 42 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 43 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 44 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 45 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 46 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 47 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 48 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 49 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 50 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 51 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 52 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 53 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 54 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 55 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 56 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 57 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 58 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 59 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 60 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 61 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 62 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 63 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 64 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 65 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 66 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 67 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 68 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 69 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 70 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 71 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 72 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 73 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 74 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 75 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 76 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 77 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 78 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 79 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 80 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 81 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 82 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 83 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 84 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 85 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 86 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 87 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 88 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 89 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 90 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 91 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 92 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 93 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 94 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 95 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 96 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 97 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 98 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 99 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 100 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 101 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 102 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 103 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 104 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 105 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 106 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 107 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 108 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 109 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 110 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 111 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 112 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 113 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 114 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 115 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 116 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 117 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 118 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 119 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 120 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 121 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 122 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 123 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 124 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 125 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 126 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 127 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 128 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 129 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 130 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 131 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 132 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 133 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 134 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 135 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 136 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 137 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 138 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 139 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 140 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 141 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 142 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 143 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 144 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 145 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 146 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 147 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 148 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 149 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 150 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 151 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 152 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 153 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 154 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 155 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 156 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 157 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 158 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 159 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 160 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 161 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 162 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 163 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 164 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 165 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 166 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 167 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 168 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 169 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 170 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 171 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 172 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 173 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 174 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 175 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 176 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 177 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 178 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 179 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 180 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 181 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 182 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 183 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 184 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 185 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 186 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 187 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 188 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 189 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 190 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 191 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 192 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 193 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 194 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 195 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 196 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 197 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 198 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 199 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 200 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 201 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 202 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 203 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 204 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 205 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 206 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 207 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 208 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 209 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 210 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 211 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 212 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 213 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 214 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 215 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 216 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 217 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 218 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 219 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 220 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 221 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 222 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 223 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 224 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 225 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 226 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 227 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 228 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 229 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 230 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 231 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 232 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 233 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 234 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 235 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 236 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 237 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 238 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 239 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 240 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 241 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 242 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 243 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 244 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 245 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 246 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 247 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 248 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 249 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 250 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 251 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 252 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 253 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 254 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 255 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 256 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 257 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 258 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 259 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 260 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 261 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 262 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 263 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 264 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 265 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 266 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 267 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 268 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 269 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 270 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 271 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 272 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 273 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 274 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 275 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 276 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 277 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 278 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 279 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 280 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 281 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 282 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 283 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 284 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 285 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 286 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 287 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 288 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 289 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 290 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 291 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 292 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 293 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 294 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 295 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 296 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 297 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 298 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 299 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 300 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 301 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 302 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 303 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 304 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 305 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 306 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 307 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 308 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 309 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 310 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 311 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 312 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 313 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 314 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 315 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 316 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 317 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 318 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 319 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 320 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 321 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 322 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 323 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 324 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 325 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 326 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 327 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 328 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 329 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 330 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 331 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 332 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 333 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 334 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 335 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 336 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 337 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 338 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 339 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 340 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 341 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 342 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 343 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 344 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 345 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 346 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 347 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 348 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 349 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 350 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 351 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 352 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 353 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 354 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 355 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 356 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 357 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 358 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 359 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 360 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 361 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 362 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 363 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 364 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 365 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 366 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 367 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 368 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 369 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 370 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 371 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 372 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 373 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 374 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 375 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 376 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 377 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 378 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 379 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 380 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 381 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 382 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 383 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 384 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 385 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 386 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 387 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 388 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 389 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 390 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 391 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 392 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 393 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 394 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 395 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 396 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 397 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 398 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 399 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 400 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 401 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 402 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 403 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 404 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 405 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 406 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 407 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 408 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 409 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 410 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 411 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 412 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 413 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 414 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 415 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 416 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 417 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 418 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 419 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 420 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 421 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 422 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 423 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 424 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 425 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 426 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 427 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 428 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 429 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 430 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 431 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 432 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 433 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 434 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 435 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 436 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 437 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 438 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 439 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 440 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 441 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 442 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 443 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 444 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 445 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 446 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 447 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 448 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 449 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 450 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 451 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 452 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 453 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 454 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 455 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 456 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 457 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 458 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 459 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 460 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 461 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 462 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 463 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 464 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 465 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 466 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 467 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 468 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 469 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 470 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 471 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 472 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 473 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 474 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 475 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 476 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 477 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 478 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 479 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 480 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 481 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 482 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 483 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 484 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 485 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 486 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 487 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 488 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 489 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 490 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 491 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 492 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 493 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 494 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 495 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 496 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 497 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 498 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 499 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 500 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 501 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 502 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 503 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 504 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 505 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 506 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 507 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 508 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 509 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 510 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 511 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 512 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 513 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 514 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 515 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 516 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 517 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 518 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 519 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 520 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 521 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 522 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 523 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 524 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 525 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 526 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 527 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 528 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 529 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 530 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 531 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 532 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 533 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 534 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 535 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 536 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 537 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 538 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 539 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 540 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 541 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 542 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 543 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 544 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 545 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 546 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 547 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 548 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 549 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 550 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 551 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 552 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 553 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 554 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 555 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 556 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 557 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 558 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 559 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 560 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 561 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 562 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 563 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 564 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 565 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 566 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 567 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 568 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 569 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 570 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 571 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 572 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 573 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 574 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 575 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 576 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 577 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 578 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 579 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 580 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 581 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 582 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 583 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 584 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 585 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 586 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 587 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 588 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 589 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 590 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 591 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 592 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 593 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 594 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 595 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 596 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 597 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 598 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 599 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
