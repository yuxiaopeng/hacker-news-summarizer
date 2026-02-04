# Hacker News 热门文章摘要 (2026-02-04)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Coding Agent VMs on NixOS with Microvm.nix

**原文标题**: Coding Agent VMs on NixOS with Microvm.nix

**原文链接**: [https://michael.stapelberg.ch/posts/2026-02-01-coding-agent-microvm-nix/](https://michael.stapelberg.ch/posts/2026-02-01-coding-agent-microvm-nix/)

生成摘要时出错

---

## 12. In Tehran

**原文标题**: In Tehran

**原文链接**: [https://www.lrb.co.uk/blog/2026/january/in-tehran](https://www.lrb.co.uk/blog/2026/january/in-tehran)

生成摘要时出错

---

## 13. Guinea worm on track to be 2nd eradicated human disease; only 10 cases in 2025

**原文标题**: Guinea worm on track to be 2nd eradicated human disease; only 10 cases in 2025

**原文链接**: [https://arstechnica.com/health/2026/02/guinea-worm-on-track-to-be-2nd-eradicated-human-disease-only-10-cases-in-2025/](https://arstechnica.com/health/2026/02/guinea-worm-on-track-to-be-2nd-eradicated-human-disease-only-10-cases-in-2025/)

生成摘要时出错

---

## 14. Lessons learned shipping 500 units of my first hardware product

**原文标题**: Lessons learned shipping 500 units of my first hardware product

**原文链接**: [https://www.simonberens.com/p/lessons-learned-shipping-500-units](https://www.simonberens.com/p/lessons-learned-shipping-500-units)

生成摘要时出错

---

## 15. Old Insurance Maps – Georeferencing Sanborn Fire Insurance Maps on Modern Maps

**原文标题**: Old Insurance Maps – Georeferencing Sanborn Fire Insurance Maps on Modern Maps

**原文链接**: [https://oldinsurancemaps.net/](https://oldinsurancemaps.net/)

生成摘要时出错

---

## 16. The Voxel Is a Cutting-Edge Theater Experiment

**原文标题**: The Voxel Is a Cutting-Edge Theater Experiment

**原文链接**: [https://bmoreart.com/2024/09/the-voxel-is-a-cutting-edge-theater-experiment.html](https://bmoreart.com/2024/09/the-voxel-is-a-cutting-edge-theater-experiment.html)

生成摘要时出错

---

## 17. Show HN: Ghidra MCP Server – 110 tools for AI-assisted reverse engineering

**原文标题**: Show HN: Ghidra MCP Server – 110 tools for AI-assisted reverse engineering

**原文链接**: [https://github.com/bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp)

生成摘要时出错

---

## 18. FBI couldn't get into WaPo reporter's iPhone because Lockdown Mode enabled

**原文标题**: FBI couldn't get into WaPo reporter's iPhone because Lockdown Mode enabled

**原文链接**: [https://www.404media.co/fbi-couldnt-get-into-wapo-reporters-iphone-because-it-had-lockdown-mode-enabled/](https://www.404media.co/fbi-couldnt-get-into-wapo-reporters-iphone-because-it-had-lockdown-mode-enabled/)

生成摘要时出错

---

## 19. Brazilian Micro-SaaS Map

**原文标题**: Brazilian Micro-SaaS Map

**原文链接**: [https://saas-map.ssr.trapiche.cloud/](https://saas-map.ssr.trapiche.cloud/)

生成摘要时出错

---

## 20. Intel will start making GPUs

**原文标题**: Intel will start making GPUs

**原文链接**: [https://techcrunch.com/2026/02/03/intel-will-start-making-gpus-a-market-dominated-by-nvidia/](https://techcrunch.com/2026/02/03/intel-will-start-making-gpus-a-market-dominated-by-nvidia/)

生成摘要时出错

---

## 21. Show HN: Craftplan – I built my wife a production management tool for her bakery

**原文标题**: Show HN: Craftplan – I built my wife a production management tool for her bakery

**原文链接**: [https://github.com/puemos/craftplan](https://github.com/puemos/craftplan)

生成摘要时出错

---

## 22. I miss thinking hard

**原文标题**: I miss thinking hard

**原文链接**: [https://www.jernesto.com/articles/thinking_hard](https://www.jernesto.com/articles/thinking_hard)

生成摘要时出错

---

## 23. New York’s budget bill would require “blocking technology” on all 3D printers

**原文标题**: New York’s budget bill would require “blocking technology” on all 3D printers

**原文链接**: [https://blog.adafruit.com/2026/02/03/new-york-wants-to-ctrlaltdelete-your-3d-printer/](https://blog.adafruit.com/2026/02/03/new-york-wants-to-ctrlaltdelete-your-3d-printer/)

生成摘要时出错

---

## 24. Microsoft's Pivotal AI Product Is Running into Big Problems

**原文标题**: Microsoft's Pivotal AI Product Is Running into Big Problems

**原文链接**: [https://www.wsj.com/tech/ai/microsofts-pivotal-ai-product-is-running-into-big-problems-ce235b28](https://www.wsj.com/tech/ai/microsofts-pivotal-ai-product-is-running-into-big-problems-ce235b28)

生成摘要时出错

---

## 25. Claude Is a Space to Think

**原文标题**: Claude Is a Space to Think

**原文链接**: [https://www.anthropic.com/news/claude-is-a-space-to-think](https://www.anthropic.com/news/claude-is-a-space-to-think)

生成摘要时出错

---

## 26. Launching the Rural Guaranteed Minimum Income Initiative

**原文标题**: Launching the Rural Guaranteed Minimum Income Initiative

**原文链接**: [https://blog.codinghorror.com/launching-the-rural-guaranteed-minimum-income-initiative/](https://blog.codinghorror.com/launching-the-rural-guaranteed-minimum-income-initiative/)

生成摘要时出错

---

## 27. Deno Sandbox

**原文标题**: Deno Sandbox

**原文链接**: [https://deno.com/blog/introducing-deno-sandbox](https://deno.com/blog/introducing-deno-sandbox)

生成摘要时出错

---

## 28. High-Altitude Adventure with a DIY Pico Balloon

**原文标题**: High-Altitude Adventure with a DIY Pico Balloon

**原文链接**: [https://spectrum.ieee.org/explore-stratosphere-diy-pico-balloon](https://spectrum.ieee.org/explore-stratosphere-diy-pico-balloon)

生成摘要时出错

---

## 29. Agent Skills

**原文标题**: Agent Skills

**原文链接**: [https://agentskills.io/home](https://agentskills.io/home)

生成摘要时出错

---

## 30. AI Is Killing B2B SaaS

**原文标题**: AI Is Killing B2B SaaS

**原文链接**: [https://nmn.gl/blog/ai-killing-b2b-saas](https://nmn.gl/blog/ai-killing-b2b-saas)

生成摘要时出错

---

## 31. Goblins: Distributed, Transactional Programming with Racket and Guile

**原文标题**: Goblins: Distributed, Transactional Programming with Racket and Guile

**原文链接**: [https://spritely.institute/goblins/](https://spritely.institute/goblins/)

生成摘要时出错

---

## 32. AliSQL: Alibaba's open-source MySQL with vector and DuckDB engines

**原文标题**: AliSQL: Alibaba's open-source MySQL with vector and DuckDB engines

**原文链接**: [https://github.com/alibaba/AliSQL](https://github.com/alibaba/AliSQL)

生成摘要时出错

---

## 33. Xcode 26.3 – Developers can leverage coding agents directly in Xcode

**原文标题**: Xcode 26.3 – Developers can leverage coding agents directly in Xcode

**原文链接**: [https://www.apple.com/newsroom/2026/02/xcode-26-point-3-unlocks-the-power-of-agentic-coding/](https://www.apple.com/newsroom/2026/02/xcode-26-point-3-unlocks-the-power-of-agentic-coding/)

生成摘要时出错

---

## 34. Stanford's Fake Disability Crisis Is America's Future

**原文标题**: Stanford's Fake Disability Crisis Is America's Future

**原文链接**: [https://garryslist.org/posts/stanford-cheating](https://garryslist.org/posts/stanford-cheating)

生成摘要时出错

---

## 35. The fax numbers of the beast, and other mathematical sports

**原文标题**: The fax numbers of the beast, and other mathematical sports

**原文链接**: [https://cabinetmagazine.org/issues/57/wertheim.php](https://cabinetmagazine.org/issues/57/wertheim.php)

生成摘要时出错

---

## 36. Broken Proofs and Broken Provers

**原文标题**: Broken Proofs and Broken Provers

**原文链接**: [https://lawrencecpaulson.github.io/2026/01/15/Broken_proofs.html](https://lawrencecpaulson.github.io/2026/01/15/Broken_proofs.html)

生成摘要时出错

---

## 37. Exploring Different Keyboard Sensing Technologies

**原文标题**: Exploring Different Keyboard Sensing Technologies

**原文链接**: [https://www.lttlabs.com/articles/2026/01/27/exploring-different-keyboard-sensing-technologies](https://www.lttlabs.com/articles/2026/01/27/exploring-different-keyboard-sensing-technologies)

生成摘要时出错

---

## 38. 221 Cannon is Not For Sale

**原文标题**: 221 Cannon is Not For Sale

**原文链接**: [https://fredbenenson.com/blog/2026/02/03/221-cannon-is-not-for-sale/](https://fredbenenson.com/blog/2026/02/03/221-cannon-is-not-for-sale/)

生成摘要时出错

---

## 39. The Mathematics of Tuning Systems

**原文标题**: The Mathematics of Tuning Systems

**原文链接**: [https://math.ucr.edu/home/baez/tuning_talk/](https://math.ucr.edu/home/baez/tuning_talk/)

生成摘要时出错

---

## 40. The largest zip tie is nearly 4 feet long and $75

**原文标题**: The largest zip tie is nearly 4 feet long and $75

**原文链接**: [https://www.thedrive.com/news/youll-have-that-on-those-big-jobs-the-worlds-largest-zip-tie-is-nearly-4-feet-long-and-75](https://www.thedrive.com/news/youll-have-that-on-those-big-jobs-the-worlds-largest-zip-tie-is-nearly-4-feet-long-and-75)

生成摘要时出错

---

## 41. Prek: A better, faster, drop-in pre-commit replacement, engineered in Rust

**原文标题**: Prek: A better, faster, drop-in pre-commit replacement, engineered in Rust

**原文链接**: [https://github.com/j178/prek](https://github.com/j178/prek)

生成摘要时出错

---

## 42. Reimplementing Tor from Scratch for a Single-Hop Proxy

**原文标题**: Reimplementing Tor from Scratch for a Single-Hop Proxy

**原文链接**: [https://foxmoss.com/blog/kurrat/](https://foxmoss.com/blog/kurrat/)

生成摘要时出错

---

## 43. Steve Bannon Proposes Using ICE in Elections

**原文标题**: Steve Bannon Proposes Using ICE in Elections

**原文链接**: [https://www.newsweek.com/steve-bannon-proposes-using-ice-in-elections-11462376](https://www.newsweek.com/steve-bannon-proposes-using-ice-in-elections-11462376)

生成摘要时出错

---

## 44. Bunny Database

**原文标题**: Bunny Database

**原文链接**: [https://bunny.net/blog/meet-bunny-database-the-sql-service-that-just-works/](https://bunny.net/blog/meet-bunny-database-the-sql-service-that-just-works/)

生成摘要时出错

---

## 45. Ending 15 years of subprocess polling

**原文标题**: Ending 15 years of subprocess polling

**原文链接**: [https://gmpy.dev/blog/2026/event-driven-process-waiting](https://gmpy.dev/blog/2026/event-driven-process-waiting)

生成摘要时出错

---

## 46. Resurrecting Crimsonland – Decompiling and preserving a cult 2003 classic game

**原文标题**: Resurrecting Crimsonland – Decompiling and preserving a cult 2003 classic game

**原文链接**: [https://banteg.xyz/posts/crimsonland/](https://banteg.xyz/posts/crimsonland/)

生成摘要时出错

---

## 47. France dumps Zoom and Teams as Europe seeks digital autonomy from the US

**原文标题**: France dumps Zoom and Teams as Europe seeks digital autonomy from the US

**原文链接**: [https://apnews.com/article/europe-digital-sovereignty-big-tech-9f5388b68a0648514cebc8d92f682060](https://apnews.com/article/europe-digital-sovereignty-big-tech-9f5388b68a0648514cebc8d92f682060)

生成摘要时出错

---

## 48. Qwen3-Coder-Next

**原文标题**: Qwen3-Coder-Next

**原文链接**: [https://qwen.ai/blog?id=qwen3-coder-next](https://qwen.ai/blog?id=qwen3-coder-next)

生成摘要时出错

---

## 49. 1,400-year-old tomb featuring giant owl sculpture discovered in Mexico

**原文标题**: 1,400-year-old tomb featuring giant owl sculpture discovered in Mexico

**原文链接**: [https://www.cnn.com/2026/01/29/science/zapotec-tomb-mexico-scli-intl](https://www.cnn.com/2026/01/29/science/zapotec-tomb-mexico-scli-intl)

生成摘要时出错

---

## 50. Y Combinator will let founders receive funds in stablecoins

**原文标题**: Y Combinator will let founders receive funds in stablecoins

**原文链接**: [https://fortune.com/2026/02/03/famed-startup-incubator-y-combinator-to-let-founders-receive-funds-in-stablecoins/](https://fortune.com/2026/02/03/famed-startup-incubator-y-combinator-to-let-founders-receive-funds-in-stablecoins/)

生成摘要时出错

---

## 51. Fastmail Donates USD 10k to the Perl and Raku Foundation

**原文标题**: Fastmail Donates USD 10k to the Perl and Raku Foundation

**原文链接**: [https://www.perl.com/article/fastmail-donates-usd-10-000-to-the-perl-and-raku-foundation/](https://www.perl.com/article/fastmail-donates-usd-10-000-to-the-perl-and-raku-foundation/)

生成摘要时出错

---

## 52. How watercolor brushes are made (2015)

**原文标题**: How watercolor brushes are made (2015)

**原文链接**: [https://www.handprint.com/HP/WCL/brush1.html](https://www.handprint.com/HP/WCL/brush1.html)

生成摘要时出错

---

## 53. FlashAttention-T: Towards Tensorized Attention

**原文标题**: FlashAttention-T: Towards Tensorized Attention

**原文链接**: [https://dl.acm.org/doi/10.1145/3774934.3786425](https://dl.acm.org/doi/10.1145/3774934.3786425)

生成摘要时出错

---

## 54. I prefer to pass secrets between programs through standard input

**原文标题**: I prefer to pass secrets between programs through standard input

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/programming/PassingSecretsViaStdin](https://utcc.utoronto.ca/~cks/space/blog/programming/PassingSecretsViaStdin)

生成摘要时出错

---

## 55. X offices raided in France as UK opens fresh investigation into Grok

**原文标题**: X offices raided in France as UK opens fresh investigation into Grok

**原文链接**: [https://www.bbc.com/news/articles/ce3ex92557jo](https://www.bbc.com/news/articles/ce3ex92557jo)

生成摘要时出错

---

## 56. Puget Systems Most Reliable Hardware of 2025

**原文标题**: Puget Systems Most Reliable Hardware of 2025

**原文链接**: [https://www.pugetsystems.com/labs/articles/puget-systems-most-reliable-hardware-of-2025/](https://www.pugetsystems.com/labs/articles/puget-systems-most-reliable-hardware-of-2025/)

生成摘要时出错

---

## 57. Heritability of intrinsic human life span is about 50%

**原文标题**: Heritability of intrinsic human life span is about 50%

**原文链接**: [https://www.science.org/doi/10.1126/science.adz1187](https://www.science.org/doi/10.1126/science.adz1187)

生成摘要时出错

---

## 58. Notepad++ supply chain attack breakdown

**原文标题**: Notepad++ supply chain attack breakdown

**原文链接**: [https://securelist.com/notepad-supply-chain-attack/118708/](https://securelist.com/notepad-supply-chain-attack/118708/)

生成摘要时出错

---

## 59. Speculative Sampling Explained

**原文标题**: Speculative Sampling Explained

**原文链接**: [https://saibo-creator.github.io/post/2024_03_08_speculative_sampling/](https://saibo-creator.github.io/post/2024_03_08_speculative_sampling/)

生成摘要时出错

---

## 60. 1 kilobyte is precisely 1000 bytes?

**原文标题**: 1 kilobyte is precisely 1000 bytes?

**原文链接**: [https://waspdev.com/articles/2026-01-11/kilobyte-is-1000-bytes](https://waspdev.com/articles/2026-01-11/kilobyte-is-1000-bytes)

生成摘要时出错

---

## 61. 1 kilobyte is precisely 1000 bytes?

**原文标题**: 1 kilobyte is precisely 1000 bytes?

**原文链接**: [https://waspdev.com/articles/2026-01-11/kilobyte-is-1000-bytes](https://waspdev.com/articles/2026-01-11/kilobyte-is-1000-bytes)

生成摘要时出错

---

## 62. Beg Bounties

**原文标题**: Beg Bounties

**原文链接**: [https://www.troyhunt.com/beg-bounties/](https://www.troyhunt.com/beg-bounties/)

生成摘要时出错

---

## 63. What's up with all those equals signs anyway?

**原文标题**: What's up with all those equals signs anyway?

**原文链接**: [https://lars.ingebrigtsen.no/2026/02/02/whats-up-with-all-those-equals-signs-anyway/](https://lars.ingebrigtsen.no/2026/02/02/whats-up-with-all-those-equals-signs-anyway/)

生成摘要时出错

---

## 64. Flying Around the World in under 80 Days

**原文标题**: Flying Around the World in under 80 Days

**原文链接**: [https://pinchito.es/2026/avis-lxxx](https://pinchito.es/2026/avis-lxxx)

生成摘要时出错

---

## 65. AI didn't break copyright law, it just exposed how broken it was

**原文标题**: AI didn't break copyright law, it just exposed how broken it was

**原文链接**: [https://www.jasonwillems.com/technology/2026/02/02/AI-Copyright/](https://www.jasonwillems.com/technology/2026/02/02/AI-Copyright/)

生成摘要时出错

---

## 66. Show HN: GitHub Browser Plugin for AI Contribution Blame in Pull Requests

**原文标题**: Show HN: GitHub Browser Plugin for AI Contribution Blame in Pull Requests

**原文链接**: [https://blog.rbby.dev/posts/github-ai-contribution-blame-for-pull-requests/](https://blog.rbby.dev/posts/github-ai-contribution-blame-for-pull-requests/)

生成摘要时出错

---

## 67. The Everdeck: A Universal Card System (2019)

**原文标题**: The Everdeck: A Universal Card System (2019)

**原文链接**: [https://thewrongtools.wordpress.com/2019/10/10/the-everdeck/](https://thewrongtools.wordpress.com/2019/10/10/the-everdeck/)

生成摘要时出错

---

## 68. The full history of Windows widgets, from 1997 to today

**原文标题**: The full history of Windows widgets, from 1997 to today

**原文链接**: [https://xakpc.dev/windows-widgets/history/](https://xakpc.dev/windows-widgets/history/)

生成摘要时出错

---

## 69. Show HN: Octosphere, a tool to decentralise scientific publishing

**原文标题**: Show HN: Octosphere, a tool to decentralise scientific publishing

**原文链接**: [https://octosphere.social/](https://octosphere.social/)

生成摘要时出错

---

## 70. China Moon Mission: Aiming for 2030 lunar landing

**原文标题**: China Moon Mission: Aiming for 2030 lunar landing

**原文链接**: [https://spectrum.ieee.org/china-moon-mission-mengzhou-artemis](https://spectrum.ieee.org/china-moon-mission-mengzhou-artemis)

生成摘要时出错

---

## 71. The €10 Mirror: Why Enterprise Security Looks Like a Kid's Toy

**原文标题**: The €10 Mirror: Why Enterprise Security Looks Like a Kid's Toy

**原文链接**: [https://labs.itresit.es/2026/02/04/the-e10-mirror-why-enterprise-security-looks-like-a-kids-toy/](https://labs.itresit.es/2026/02/04/the-e10-mirror-why-enterprise-security-looks-like-a-kids-toy/)

生成摘要时出错

---

## 72. Banning lead in gas worked. The proof is in our hair

**原文标题**: Banning lead in gas worked. The proof is in our hair

**原文链接**: [https://attheu.utah.edu/health-medicine/banning-lead-in-gas-worked-the-proof-is-in-our-hair/](https://attheu.utah.edu/health-medicine/banning-lead-in-gas-worked-the-proof-is-in-our-hair/)

生成摘要时出错

---

## 73. The next steps for Airbus' big bet on open rotor engines

**原文标题**: The next steps for Airbus' big bet on open rotor engines

**原文链接**: [https://aerospaceamerica.aiaa.org/the-next-steps-for-airbus-big-bet-on-open-rotor-engines/](https://aerospaceamerica.aiaa.org/the-next-steps-for-airbus-big-bet-on-open-rotor-engines/)

生成摘要时出错

---

## 74. Coding assistants are solving the wrong problem

**原文标题**: Coding assistants are solving the wrong problem

**原文链接**: [https://www.bicameral-ai.com/blog/introducing-bicameral](https://www.bicameral-ai.com/blog/introducing-bicameral)

生成摘要时出错

---

## 75. Show HN: Safe-now.live – Ultra-light emergency info site (<10KB)

**原文标题**: Show HN: Safe-now.live – Ultra-light emergency info site (<10KB)

**原文链接**: [https://safe-now.live](https://safe-now.live)

生成摘要时出错

---

## 76. Tadpole – A modular and extensible DSL built for web scraping

**原文标题**: Tadpole – A modular and extensible DSL built for web scraping

**原文链接**: [https://tadpolehq.com/](https://tadpolehq.com/)

生成摘要时出错

---

## 77. US Gen-X is definitely feeling the pressure

**原文标题**: US Gen-X is definitely feeling the pressure

**原文链接**: [https://www.sciencedaily.com/releases/2026/02/260201062457.htm](https://www.sciencedaily.com/releases/2026/02/260201062457.htm)

生成摘要时出错

---

## 78. Reference Target: having your encapsulation and eating it too

**原文标题**: Reference Target: having your encapsulation and eating it too

**原文链接**: [https://blogs.igalia.com/alice/reference-target-having-your-encapsulation-and-eating-it-too/](https://blogs.igalia.com/alice/reference-target-having-your-encapsulation-and-eating-it-too/)

生成摘要时出错

---

## 79. Show HN: Sandboxing untrusted code using WebAssembly

**原文标题**: Show HN: Sandboxing untrusted code using WebAssembly

**原文链接**: [https://github.com/mavdol/capsule](https://github.com/mavdol/capsule)

生成摘要时出错

---

## 80. Sandboxing AI Agents in Linux

**原文标题**: Sandboxing AI Agents in Linux

**原文链接**: [https://blog.senko.net/sandboxing-ai-agents-in-linux](https://blog.senko.net/sandboxing-ai-agents-in-linux)

生成摘要时出错

---

## 81. Rentahuman – The Meatspace Layer for AI

**原文标题**: Rentahuman – The Meatspace Layer for AI

**原文链接**: [https://rentahuman.ai](https://rentahuman.ai)

生成摘要时出错

---

## 82. See how many words you have written in Hacker News comments

**原文标题**: See how many words you have written in Hacker News comments

**原文链接**: [https://serjaimelannister.github.io/hn-words/](https://serjaimelannister.github.io/hn-words/)

生成摘要时出错

---

## 83. China bans hidden car door handles

**原文标题**: China bans hidden car door handles

**原文链接**: [https://text.npr.org/nx-s1-5698224](https://text.npr.org/nx-s1-5698224)

生成摘要时出错

---

## 84. Show HN: C discrete event SIM w stackful coroutines runs 45x faster than SimPy

**原文标题**: Show HN: C discrete event SIM w stackful coroutines runs 45x faster than SimPy

**原文链接**: [https://github.com/ambonvik/cimba](https://github.com/ambonvik/cimba)

生成摘要时出错

---

## 85. "time to GPT-2", down to 2.91 hours

**原文标题**: "time to GPT-2", down to 2.91 hours

**原文链接**: [https://twitter.com/karpathy/status/2018804068874064198](https://twitter.com/karpathy/status/2018804068874064198)

生成摘要时出错

---

## 86. Oracle to raise $50B as AI debt piles up

**原文标题**: Oracle to raise $50B as AI debt piles up

**原文链接**: [https://www.marketwatch.com/story/oracles-monster-25-billion-debt-financing-points-to-anxieties-around-ai-funding-b92c634b?gaa_at=eafs&gaa_n=AWEtsqczVlBBoDjcC6lCxjyKeNisB6QEz-oEo2k0PWtFwpsWKtDrK59-8jvylfPs4hg%3D&gaa_ts=6982f2dc&gaa_sig=-KcqgqDi0dxU0ClZBaHnzzgUTR14fkTa5R5HKguuHzRXJHBu8gNGy1MqJfI3oFVq-3e_cvFlJqfulVUup8b5hw%3D%3D](https://www.marketwatch.com/story/oracles-monster-25-billion-debt-financing-points-to-anxieties-around-ai-funding-b92c634b?gaa_at=eafs&gaa_n=AWEtsqczVlBBoDjcC6lCxjyKeNisB6QEz-oEo2k0PWtFwpsWKtDrK59-8jvylfPs4hg%3D&gaa_ts=6982f2dc&gaa_sig=-KcqgqDi0dxU0ClZBaHnzzgUTR14fkTa5R5HKguuHzRXJHBu8gNGy1MqJfI3oFVq-3e_cvFlJqfulVUup8b5hw%3D%3D)

生成摘要时出错

---

## 87. The Codex App

**原文标题**: The Codex App

**原文链接**: [https://openai.com/index/introducing-the-codex-app/](https://openai.com/index/introducing-the-codex-app/)

生成摘要时出错

---

## 88. Another London: Excavating the disenchanted city

**原文标题**: Another London: Excavating the disenchanted city

**原文链接**: [https://harpers.org/archive/2026/02/another-london-situationists-hari-kunzru/](https://harpers.org/archive/2026/02/another-london-situationists-hari-kunzru/)

生成摘要时出错

---

## 89. Floppinux – An Embedded Linux on a Single Floppy, 2025 Edition

**原文标题**: Floppinux – An Embedded Linux on a Single Floppy, 2025 Edition

**原文链接**: [https://krzysztofjankowski.com/floppinux/floppinux-2025.html](https://krzysztofjankowski.com/floppinux/floppinux-2025.html)

生成摘要时出错

---

## 90. Underrated ways to change the world, part II

**原文标题**: Underrated ways to change the world, part II

**原文链接**: [https://www.experimental-history.com/p/underrated-ways-to-change-the-world-b64](https://www.experimental-history.com/p/underrated-ways-to-change-the-world-b64)

生成摘要时出错

---

## 91. Archive.today is directing a DDoS attack against my blog?

**原文标题**: Archive.today is directing a DDoS attack against my blog?

**原文链接**: [https://gyrovague.com/2026/02/01/archive-today-is-directing-a-ddos-attack-against-my-blog/](https://gyrovague.com/2026/02/01/archive-today-is-directing-a-ddos-attack-against-my-blog/)

生成摘要时出错

---

## 92. Todd C. Miller – Sudo maintainer for over 30 years

**原文标题**: Todd C. Miller – Sudo maintainer for over 30 years

**原文链接**: [https://www.millert.dev/](https://www.millert.dev/)

生成摘要时出错

---

## 93. Migrate Wizard – IMAP Based Email Migration Tool

**原文标题**: Migrate Wizard – IMAP Based Email Migration Tool

**原文链接**: [https://migratewizard.com/](https://migratewizard.com/)

生成摘要时出错

---

## 94. Anki ownership transferred to AnkiHub

**原文标题**: Anki ownership transferred to AnkiHub

**原文链接**: [https://forums.ankiweb.net/t/ankis-growing-up/68610](https://forums.ankiweb.net/t/ankis-growing-up/68610)

生成摘要时出错

---

## 95. Geologists may have solved mystery of Green River's 'uphill' route

**原文标题**: Geologists may have solved mystery of Green River's 'uphill' route

**原文链接**: [https://phys.org/news/2026-01-geologists-mystery-green-river-uphill.html](https://phys.org/news/2026-01-geologists-mystery-green-river-uphill.html)

生成摘要时出错

---

## 96. Carnegie Mellon Unversity Computer Club FTP Server

**原文标题**: Carnegie Mellon Unversity Computer Club FTP Server

**原文链接**: [http://128.237.157.9/pub/](http://128.237.157.9/pub/)

生成摘要时出错

---

## 97. On being sane in insane places (1973) [pdf]

**原文标题**: On being sane in insane places (1973) [pdf]

**原文链接**: [https://www.weber.edu/wsuimages/psychology/FacultySites/Horvat/OnBeingSaneInInsanePlaces.PDF](https://www.weber.edu/wsuimages/psychology/FacultySites/Horvat/OnBeingSaneInInsanePlaces.PDF)

生成摘要时出错

---

## 98. Majority of Trump voters back solar power, poll finds

**原文标题**: Majority of Trump voters back solar power, poll finds

**原文链接**: [https://www.axios.com/2026/02/04/trump-maga-poll-solar-energy](https://www.axios.com/2026/02/04/trump-maga-poll-solar-energy)

生成摘要时出错

---

## 99. Julia

**原文标题**: Julia

**原文链接**: [https://borretti.me/fiction/julia](https://borretti.me/fiction/julia)

生成摘要时出错

---

## 100. Joedb, the Journal-Only Embedded Database

**原文标题**: Joedb, the Journal-Only Embedded Database

**原文链接**: [https://www.joedb.org/index.html](https://www.joedb.org/index.html)

生成摘要时出错

---

