# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-04.md)

*最后自动更新时间: 2026-02-04 18:16:26*
## 1. Voxtral 转录 2

**原文标题**: Voxtral Transcribe 2

**原文链接**: [https://mistral.ai/news/voxtral-transcribe-2](https://mistral.ai/news/voxtral-transcribe-2)

Mistral 宣布推出 **Voxtral Transcribe 2**，包含两款旨在实现高质量转录和极低延迟的新一代语音转文字模型。

**核心模型：**
*   **Voxtral Mini Transcribe V2：** 专为批量转录优化，以极具竞争力的价格（0.003 美元/分钟）提供业界领先的准确度。它包含企业级功能，如说话人分离、词级时间戳和**上下文偏置**（允许用户输入特定词汇，以提高技术术语或名称的拼写准确性）。
*   **Voxtral Realtime：** 专为语音智能体和字幕生成等实时应用打造，采用创新的流式架构，延迟可配置至 200 毫秒以下。该模型以 **Apache 2.0 开放权重许可**发布，非常适合注重隐私的边缘部署。

**性能与特性：**
两款模型均支持 **13 种语言**（包括英语、中文、印地语和西班牙语），并展现出行业领先的字错率（WER），性能优于 GPT-4o mini、Gemini 2.5 Flash 和 Deepgram Nova 等竞争对手。模型具有强大的抗噪能力，可处理长达三小时的录音。

**可用性与工具：**
Mistral 还在 Mistral Studio 中推出了 **Audio Playground**，方便用户即时测试转录、说话人分离和时间戳功能。这些模型符合 GDPR 和 HIPAA 标准，适用于医疗保健、金融和呼叫中心等领域。

**定价：**
*   **Mini Transcribe V2：** 通过 API 调用为 0.003 美元/分钟。
*   **Voxtral Realtime：** 通过 API 调用为 0.006 美元/分钟（也可在 Hugging Face 上获取）。

这些模型旨在为会议智能、对话式人工智能和媒体广播工作流提供高性能、高性价比的解决方案。

---

## 2. 通过对称感知泰勒近似实现单 Token 常数开销的注意力机制

**原文标题**: Attention at Constant Cost per Token via Symmetry-Aware Taylor Approximation

**原文链接**: [https://arxiv.org/abs/2602.00294](https://arxiv.org/abs/2602.00294)

“**基于对称感知泰勒近似的恒定逐标记成本自注意力机制**” (arXiv:2602.00294) 解决了标准 Transformer 模型的扩展性限制。在传统的自注意力机制中，计算和内存成本随上下文长度呈二次方增长，这为长上下文应用和大规模部署构成了重大瓶颈。

为了解决这一问题，作者 Franz A. Heinsen 和 Leo Kozachkov 提出了一种在保持任意精度的同时，实现**恒定逐标记成本**（相对于序列长度的复杂度为 $O(1)$）的公式。其方法的核心在于将标准注意力机制的泰勒展开分解为张量积的对称链。通过利用这些对称性，他们推导出前馈变换，将查询（queries）和键（keys）映射到**最小多项式核特征基**中。

该研究的核心亮点包括：
*   **效率：** 与标准自注意力相比，该方法在内存使用和计算量方面实现了数量级的降低。
*   **扩展性：** 它支持以固定成本进行无限制的标记生成，使得处理远超以往长度的序列成为可能。
*   **架构优化：** 由于成本与注意力头的大小成反比固定，该公式允许在每个标记上配置更多数量的注意力头。
*   **可持续性：** 计算需求的减少直接降低了大规模 AI 模型对基础设施和能源的需求。

作者通过实验验证了其公式的正确性，并指出文中所引入的数学技术——特别是向对称张量基的高效映射——对于更广泛的机器学习领域具有独立的研究价值。这项工作代表了在推动高性能人工智能的普适化与环境可持续性方面迈出的重要一步。

---

## 3. 研究：社交媒体的情感支持可缓解焦虑

**原文标题**: Study: emotional support from social media found to reduce anxiety

**原文链接**: [https://news.uark.edu/articles/80669/emotional-support-from-social-media-found-to-reduce-anxiety](https://news.uark.edu/articles/80669/emotional-support-from-social-media-found-to-reduce-anxiety)

阿肯色大学布莱恩·普里马克（Brian Primack）博士领导的一项研究揭示，通过社交媒体获得的情感支持可以显著减轻年轻人的焦虑。尽管公众舆论往往关注社交媒体对心理健康的负面影响，但这项研究强调了这些平台如何提供至关重要的“一线希望”。

该研究调查了1700多名18至30岁的美国成年人，以探讨社交媒体上感知到的情感支持与焦虑症状之间的关系。研究人员根据是否有倾诉对象、是否获得鼓励以及是否感受到在线社区的重视等因素来衡量支持程度。

研究结果表明，报告在社交媒体上获得高水平情感支持的个体，出现焦虑的可能性显著降低。至关重要的是，即使在考虑了各种人口统计因素后，这种相关性依然强劲。研究指出，在线互动的“质量”——特别是支持性的、有意义的联系——是比单纯在平台上花费的时间“数量”更重要的心理健康结果预测指标。

普里马克博士指出，这些结果为看待数字生活提供了一个更细致的视角。这项研究并未将社交媒体视为纯粹的有害力量，而是认为它可以作为建立联系和心理健康管理的便捷工具。这些发现可以为未来的公共卫生策略提供参考，鼓励开发旨在促进积极情感交流的在线环境，并为受焦虑困扰的人群提供资源。

---

## 4. 拖拉机

**原文标题**: Tractor

**原文链接**: [https://incoherency.co.uk/blog/stories/tractor.html](https://incoherency.co.uk/blog/stories/tractor.html)

本文详细介绍了一个为期六个月的项目：为作者三岁的女儿打造一辆定制电动玩具拖拉机。该拖拉机由350W有刷直流电机和36V锂离子电动自行车电池驱动，采用胶合板底盘、固定后轴以及可应对崎岖地形的摆动式前轴。

关键技术亮点包括：

*   **转向系统：** 仿照弗格森TE20型拖拉机设计，转向机构采用了由废旧角磨机齿轮改装而成的定制变速箱（传动比为3:1）。转向臂通过摩擦配合安装在转轴上，起到“机械保险丝”的作用，以防止在撞击时受损。
*   **传动系统：** 由于需要30:1的减速比，作者在电机组件上增加了一个中间轴。后轮源自割草机，安装在作者用小型车床加工的20毫米车轴上。虽然链轮支架最初是用螺栓固定在轴上的，但在经历多次剪切故障后，作者最终将其永久焊接。
*   **控制系统：** 倒车功能通过带有定制3D打印操纵杆和挡槽的双刀双掷（DPDT）开关实现。一具迷你摩托车碟刹提供制动力，尽管作者指出其效果有限。
*   **车身：** 弧形引擎盖采用胶合板“锯缝弯曲”工艺制成。虽然木材在加工过程中发生了断裂，但作者通过胶水、原子灰和打磨将其修复，最终实现了平滑的外观。

作者还尝试使用基于Arduino的“油门调节器”来平滑起步时的顿挫感，但最终为了追求机械结构的简洁而将其拆除。项目最后总结了对繁琐涂装工作的思考，以及对MIG焊接设置（特别是送丝速度与热量之间的关系）的学习心得。

---

## 5. 关于 Clawdbot / OpenClaw 的理性看涨观点

**原文标题**: A sane but bull case on Clawdbot / OpenClaw

**原文链接**: [https://brandon.wang/2026/clawdbot](https://brandon.wang/2026/clawdbot)

本文针对 Clawdbot (OpenClaw) 提出了“理性的看好论据”。这是一款能够深度融入个人和职业生活的 AI 智能体。作者站在 2026 年 2 月的视角指出，尽管公众舆论往往倾向于极端的恐慌或轻率的使用，但 AI 的真正价值在于赋予其充分的背景信息和自主代理权。

**核心应用场景**
通过自动化处理多项“高摩擦”的生活任务，作者从一名怀疑者转变为深度用户：
*   **主动沟通：** Clawdbot 扫描短信以识别承诺，在日历上预留时间以防止重复预约，并汇总海量群聊内容（如 WhatsApp/Signal）。
*   **复杂监控：** 它处理“重推理”任务，例如根据特定的视觉标准监控酒店价格（如通过照片核实房间内是否没有折叠床）。
*   **生活行政：** 该智能体通过照片管理冷冻库库存等家庭后勤，将食谱转换为购物清单，并通过登录门户网站和处理双重身份验证 (2FA) 码来完成服务预订（牙医、餐厅）。
*   **工作流演进：** Clawdbot 在 Notion 中记录其不断演进的工作流，并随着时间的推移学习用户的特定偏好。

**风险与回报**
作者通过将授予 AI 访问银行、短信和 2FA 的权限与聘请人类私人助手进行类比，探讨了重大的安全风险。他们认为，所有的授权都需要在风险与实用性之间做出权衡。作者指出，目前大多数人对 AI 并不感冒，是因为他们使用的是受限且“无状态”的版本；只有当 AI 拥有“背景信息的甘露”来自主收集、完善并**执行**数据时，真正的生产力才能被释放。

文章最后总结道，营利性或“安全”型 AI 模型往往缺乏实现真正变革所需的持续性，这使得像 Clawdbot 这样开放且集成度高的智能体成为了个人生产力的未来。

---

## 6. 沥青路面坑槽修补规程

**原文标题**: Procedures for Repair of Potholes in Asphalt-Surfaced Pavements

**原文链接**: [https://highways.dot.gov/media/7941](https://highways.dot.gov/media/7941)

本文由美国联邦公路管理局（FHWA）发布，总结了旨在确定沥青路面坑槽修补中最具成本效益的材料与工艺的广泛研究（特别是SHRP H-105研究）。

该研究评估了四种主要的修补方法：
*   **填补碾压法 (Throw-and-Roll)：** 最常用的方法，将修补材料直接填入坑槽（无论是否有杂物），并利用养护卡车的轮胎进行压实。
*   **半永久性修补法 (Semi-Permanent)：** 一种劳动力密集型方法，包括将坑槽边缘切齐成方形、清除积水和杂物，并使用振动夯或压路机进行压实。
*   **喷注式修补法 (Spray Injection)：** 一种机械化工艺，利用专门设备吹除杂物、喷涂粘层，然后将集料与乳化沥青的混合物喷入坑槽内。
*   **封边法 (Edge Seal)：** 一种辅助工序，在修补完成的区域边缘铺设一带状液体沥青和砂，以防止水分入渗。

**主要发现：**
1.  **方法效率：** 令人意外的是，只要使用高品质材料，“填补碾压法”在大多数情况下的效果与“半永久性修补法”相当。由于其施工速度更快且所需人工更少，通常是最具成本效益的选择。
2.  **材料质量：** 修补材料的质量是决定修补寿命最关键的因素。专利高品质冷拌料的表现始终优于当地标准的普通冷拌料，其更长的使用寿命证明了其较高的初期成本是合理的。
3.  **喷注式修补：** 该方法被证明非常成功且生产效率最高，但需要对专用设备进行大量投资。

报告得出结论，通过优先选用高品质材料并采用“填补碾压法”而非劳动力密集的传统方法，相关机构可以降低整体养护成本。

---

## 7. A case study in PDF forensics: The Epstein PDFs

**原文标题**: A case study in PDF forensics: The Epstein PDFs

**原文链接**: [https://pdfa.org/a-case-study-in-pdf-forensics-the-epstein-pdfs/](https://pdfa.org/a-case-study-in-pdf-forensics-the-epstein-pdfs/)

Peter Wyatt of the PDF Association provides a forensic analysis of the documents released by the U.S. Department of Justice (DOJ) under the Epstein Files Transparency Act (EFTA). Examining datasets totaling over 14,000 files, Wyatt focuses on PDF syntax, structural validity, and redaction integrity.

A primary conclusion is that the EFTA PDFs are correctly redacted. Wyatt addresses social media reports of “recoverable redactions,” clarifying that these claims likely stem from older, unrelated DOJ filings where ineffective "black box" overlays left underlying text copyable. In contrast, the specific EFTA tranche uses robust sanitization methods with no recoverable hidden information.

Technically, the PDFs are mostly valid, consisting of scanned images and photos with OCR (Optical Character Recognition). They contain no encryption, JavaScript, forms, or embedded files. Forensic investigation revealed that many files utilize incremental updates—a PDF feature that appends revisions to the end of a file. In this case, updates were used to add Bates numbering (e.g., "EFTA00000001") and upgrade document catalogs to PDF version 1.5. 

Wyatt highlights the necessity of using multiple forensic tools, noting that basic utilities often produced conflicting results because they failed to properly interpret these incremental updates or compressed object streams. The study concludes that while the DOJ has historically used inadequate redaction processes in other cases, the EFTA datasets currently show no signs of technical malformation or failed sanitization. This case study serves as a reminder of the expertise required to accurately navigate PDF forensics and the importance of professional sanitization workflows for sensitive documents.

---

## 8. Converge (YC S23) Is Hiring Product Engineers (NYC, In-Person)

**原文标题**: Converge (YC S23) Is Hiring Product Engineers (NYC, In-Person)

**原文链接**: [https://www.runconverge.com/careers/product-engineer](https://www.runconverge.com/careers/product-engineer)

生成摘要时出错

---

## 9. French streamer unbanked by Qonto after criticizing Palantir and Peter Thiel

**原文标题**: French streamer unbanked by Qonto after criticizing Palantir and Peter Thiel

**原文链接**: [https://twitter.com/Ced_haurus/status/2018716889191498172](https://twitter.com/Ced_haurus/status/2018716889191498172)

生成摘要时出错

---

## 10. Data centers in space makes no sense

**原文标题**: Data centers in space makes no sense

**原文链接**: [https://civai.org/blog/space-data-centers](https://civai.org/blog/space-data-centers)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 2 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 3 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 4 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 5 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 6 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 7 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 8 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 9 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 10 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 11 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 12 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 13 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 14 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 15 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 16 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 17 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 18 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 19 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 20 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 21 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 22 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 23 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 24 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 25 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 26 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 27 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 28 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 29 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 30 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 31 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 32 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 33 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 34 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 35 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 36 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 37 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 38 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 39 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 40 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 41 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 42 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 43 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 44 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 45 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 46 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 47 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 48 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 49 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 50 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 51 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 52 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 53 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 54 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 55 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 56 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 57 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 58 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 59 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 60 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 61 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 62 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 63 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 64 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 65 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 66 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 67 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 68 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 69 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 70 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 71 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 72 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 73 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 74 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 75 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 76 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 77 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 78 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 79 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 80 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 81 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 82 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 83 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 84 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 85 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 86 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 87 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 88 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 89 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 90 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 91 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 92 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 93 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 94 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 95 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 96 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 97 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 98 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 99 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 100 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 101 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 102 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 103 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 104 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 105 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 106 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 107 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 108 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 109 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 110 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 111 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 112 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 113 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 114 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 115 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 116 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 117 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 118 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 119 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 120 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 121 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 122 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 123 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 124 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 125 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 126 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 127 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 128 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 129 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 130 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 131 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 132 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 133 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 134 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 135 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 136 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 137 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 138 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 139 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 140 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 141 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 142 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 143 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 144 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 145 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 146 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 147 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 148 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 149 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 150 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 151 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 152 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 153 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 154 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 155 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 156 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 157 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 158 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 159 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 160 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 161 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 162 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 163 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 164 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 165 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 166 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 167 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 168 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 169 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 170 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 171 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 172 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 173 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 174 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 175 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 176 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 177 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 178 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 179 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 180 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 181 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 182 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 183 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 184 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 185 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 186 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 187 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 188 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 189 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 190 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 191 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 192 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 193 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 194 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 195 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 196 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 197 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 198 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 199 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 200 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 201 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 202 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 203 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 204 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 205 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 206 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 207 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 208 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 209 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 210 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 211 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 212 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 213 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 214 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 215 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 216 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 217 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 218 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 219 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 220 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 221 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 222 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 223 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 224 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 225 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 226 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 227 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 228 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 229 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 230 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 231 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 232 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 233 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 234 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 235 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 236 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 237 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 238 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 239 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 240 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 241 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 242 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 243 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 244 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 245 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 246 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 247 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 248 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 249 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 250 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 251 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 252 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 253 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 254 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 255 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 256 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 257 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 258 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 259 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 260 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 261 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 262 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 263 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 264 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 265 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 266 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 267 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 268 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 269 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 270 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 271 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 272 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 273 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 274 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 275 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 276 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 277 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 278 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 279 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 280 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 281 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 282 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 283 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 284 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 285 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 286 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 287 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 288 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 289 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 290 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 291 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 292 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 293 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 294 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 295 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 296 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 297 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 298 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 299 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 300 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 301 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 302 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 303 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 304 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 305 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 306 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 307 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 308 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 309 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 310 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 311 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 312 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 313 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 314 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 315 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 316 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 317 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 318 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 319 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 320 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 321 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
