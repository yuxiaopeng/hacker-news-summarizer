# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-10.md)

*最后自动更新时间: 2026-11-10 01:00:21*
## 1. Claude Fable 5.2 和 Mythos 5.2

**原文标题**: Claude Fable 5.2 and Mythos 5.2

**原文链接**: [https://www.anthropic.com/claude-fable-and-mythos-5-2](https://www.anthropic.com/claude-fable-and-mythos-5-2)

Anthropic 宣布推出 **Claude Fable 5.2 和 Claude Mythos 5.2**。作为升级版模型，这两款模型旨在应对编程、推理和科学领域的复杂技术挑战。尽管两者基于相同的底层架构，但 Fable 为通用场景内置了强健的网络安全和生物安全防护，而 Mythos 则专供生命科学和网络验证计划中的经认证组织使用。

**关键性能提升：**
5.2 版本模型在多项基准测试中超越了前代产品及竞争对手（包括 GPT-6 Astra 和 Gemini 4 Carbon）。显著成就包括：
*   **速度与成本：** 生成速度比 5.1 版本快 30%，成本降至每百万输入 Token 8 美元，每百万输出 Token 40 美元。可选的“快速模式”可进一步提供 2.5 倍的速度提升。
*   **技术里程碑：** 在测试中，该模型仅用 30 小时就完成了费马大定理的形式化证明，并实现了从零设计操作系统以及解决黑洞物理学中的悬案。
*   **智能体能力：** Fable 5.2 在“智能体”（Agentic）任务中表现卓越，例如管理 1,000 多个子智能体以构建软件，或执行长达 12 小时的自主安全审计。

**战略应用场景：**
Anthropic 将 Fable 5.2 定位为处理开放式技术工作的终极“顾问”或“编排”模型，其层级高于 Claude Opus 5.5。来自 Vercel、Shopify 和 Datadog 等公司的早期采用者报告称，该模型展现出了“资深级”的工程判断力、卓越的意图识别能力，并能在模糊、陌生的系统中工作而不产生幻觉。

**安全与对齐：**
发布前测试重点关注了高风险领域，包括沙箱逃逸和蒸馏攻击。与 5.1 版本相比，新模型表现出更好的对齐性，且“不必要的屏蔽”更少，确保了先进能力不会损害安全性。Claude Mythos 5.2 在漏洞发现方面比 Opus 5.5 提升了 10.2%，使其成为网络安全工程的顶尖工具。

---

## 2. USPS 现已提供官方邮政编码边界多边形

**原文标题**: USPS now offers official ZIP Code boundary polygons

**原文链接**: [https://postalpro.usps.com/zcb](https://postalpro.usps.com/zcb)

美国邮政管理局（USPS）推出了 **USPS® 邮政编码边界 (USPS® ZIP Code Boundaries)**，这是一款官方全国性地图产品，根据实际投递地址和位置数据提供精确的邮政编码多边形。作为邮政编码区域的“权威基准”，这些边界每季度更新一次，以反映新的投递位置和不断变化的配送模式。

**主要特点与优势：**
*   **准确性：** 提供官方数据，用于纠正或补充现有的绘图和邮寄数据库。
*   **行业应用：** 支持房地产、保险、物流、市场营销和交通等多个领域。
*   **应用场景：** 协助整理人口统计数据、优化路径规划，并为空间分析提供可靠的框架。

**产品级别：**
该数据提供三种不同的许可选项，所有选项均包含四次季度更新：
1.  **内部版 (Internal)：** 仅限单一组织内部使用。
2.  **企业版 (Enterprise)：** 包含面向子公司和合作伙伴的有限分发权。
3.  **发布版 (Publication)：** 用于有限的公开分发。

**支持与实施：**
为了便于集成，USPS 提供了多种资源，包括技术指南、GeoJSON 示例文件、简报和许可协议。这些工具允许用户将官方边界数据整合到其现有的地理信息系统 (GIS) 和工作流中。

---

## 3. TPU 8tx 和 TPU 8i Max

**原文标题**: TPU 8tx and TPU 8i Max

**原文链接**: [https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/)

谷歌推出了 TPU 8tx 和 TPU 8i Max，扩展了其第八代 TPU 产品系列，这标志着其在一年内以前所未有的节奏发布了四款 TPU 系统。这些新增产品专为“智能体时代”量身打造，重点关注硬件级安全、推理能力以及超大规模上下文窗口。

**核心硬件更新：**
*   **TPU 8tx：** 针对**安全和机密推理**进行了优化，该系统提供硬件级加密，以在模型运行过程中保护敏感数据和权重。它专为受监管行业设计，在处理智能体工作负载时，其延迟比 TPU 8t 降低了多达 2 倍。
*   **TPU 8i Max：** 旨在突破“内存墙”，该系统将两颗 8i 芯片封装在一起，从而实现**算力、SRAM 和 HBM 带宽翻倍**。它专为处理超大规模上下文窗口（数百万个 token）而设计，并提供单机架最高的计算密度。

**软件与易用性增强：**
谷歌还致力于消除采用门槛，使 TPU 像通用硬件一样易于使用：
*   **PyTorch 集成：** 通过开源的 **TorchTPU**，开发者无需重写代码即可在 TPU 上原生运行 PyTorch 代码和 Hugging Face 模型。
*   **开发者工具：** 全新的 TPU 智能体套件可自动化入门流程并自动调优自定义内核，而 **XLA 服务引擎 (XLA Serving Engine)** 则简化了生产环境的部署。
*   **效率与扩展性：** **智能体计算引擎 (Agent Compute Engine)** 通过挂起闲置会话来降低成本，而 **TPU Sync** 和 **GKE 动态切分 (dynamic slicing)** 则优化了大集群中的存储层级和硬件利用率。

通过软硬件协同设计，谷歌现已为 AI 生命周期的每个阶段提供专门的加速器：训练 (8t)、实时推理 (8i)、机密计算 (8tx) 以及长上下文智能体工作负载 (8i Max)。

---

## 4. Google Gemini 将个人云端硬盘文件和电子邮件发送给人工标注员

**原文标题**: Google Gemini routes personal Drive files and emails to human annotators

**原文链接**: [https://github.com/thisisme6598/gemini_files/](https://github.com/thisisme6598/gemini_files/)

Google 正式撤回了其在 2023 年做出的承诺，即 Workspace 扩展程序（Gmail、Docs 和 Drive）中的个人数据将与人工审核员隔离。更新后的政策文档和博文现已明确证实，来自这些关联应用的内容会被输送到人工审核流程中。

测试显示，这种数据摄取是**自主且具有概率性**的。即使没有明确使用“@”标签，提及个人话题（如账单或旅行计划）的语境也可能触发后台查询。由于系统是非确定性的，交互呈现出四种状态：
1. **零检索：** 未提取任何数据。
2. **元数据/通用摘要：** 生成高层级的摘要。
3. **部分未脱敏提取：** 提取包含敏感个人身份信息 (PII) 的简短引用。
4. **全文件摄取：** 文档或电子邮件的完整、未脱敏文本被拉入对话上下文中。

Google 现已明确警告用户，如果 Workspace 应用中包含机密信息，请勿将其连接到 Gemini。由于 Google 的自动去标识化清理程序往往无法删除敏感的描述性数据（如账号、确认码以及个人详细信息的独特组合），这一风险变得更加复杂。

总而言之，最初承诺用于 Workspace 集成的严格隐私屏障已被移除。个人文件可能会在日常对话中被摄取，并随后被人工外包人员查看，这使得该平台不再适合处理敏感或机密信息。

---

## 5. Fable 5.2 秒杀了我侄子梦想中的游戏。

**原文标题**: Fable 5.2 one-shotted my nephew's dream game

**原文链接**: [https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game](https://notesbylex.com/fable-5-2-one-shotted-my-nephews-dream-game)

Lex Toumbourou 的文章详细记录了生成式 AI 领域的一个重要里程碑：利用（虚构的）**Claude Fable 5.2**，根据其侄子 Aiden 的手绘设计，“一次性（one-shot）”生成了一款复杂且高质量的清版动作游戏。

受《忍者神龟》等经典游戏的启发，Aiden 提议开发一款以家庭成员为英雄并包含 12 个独特 Boss 的游戏。在 2026 年初使用旧模型（Opus 4.8）进行的尝试效果不佳后，Toumbourou 利用 Fable 5.2 的早期访问权限和 **Claude Code** 尝试了全自动构建。

通过提供一个宏大的提示词和 Aiden 的素描草图，该 AI 独立完成了以下工作：
*   整合了 **OpenAI 的 ChatGPT Images 2.5** 用于生成精灵图和背景，并使用 **ElevenLabs** 生成音乐和音效。
*   生成了约 175 张图像和 140 个音频剪辑。
*   编写了一个自动测试机器人，在无头浏览器中运行全部 12 个关卡，以识别并修复视觉或机制漏洞。
*   将角色阵容从 5 名英雄扩展到 18 名可解锁角色，其中包括宠物以及被重新构思为“天使”的已故亲人。

整个项目消耗了约 3.4 亿个 token，并产出了一个包含过场动画、特殊招式和 12 个 Boss 关卡、制作精良的四人游戏体验。Toumbourou 总结道，该项目的成功标志着智能体（agentic）工具的一个“疯狂里程碑”。它证明了 AI 已经超越了生成简单代码片段的阶段，进化到能够根据粗略的创意构想，在极少人工干预的情况下，执行整个有趣且功能完备的软件项目。

---

## 6. 加拿大支付协会宣布启动加拿大实时支付系统 (RTR)

**原文标题**: Payments Canada announces launch of Canada's Real-Time Rail (RTR) payment system

**原文链接**: [https://www.payments.ca/canada-launches-real-time-rail-bringing-247-payment-infrastructure-national-economy](https://www.payments.ca/canada-launches-real-time-rail-bringing-247-payment-infrastructure-national-economy)

2026年11月9日，加拿大支付协会（Payments Canada）正式推出“实时支付系统”（Real-Time Rail，简称RTR）。这一全新的国家级支付系统提供全年无休（24/7/365）的即时清算与结算。RTR由加拿大支付协会运营，并与CGI、德勤（Deloitte）、IBM及Interac等合作伙伴共同开发，标志着加拿大金融基础设施的一次重大现代化升级。

该系统采用ISO 20022报文标准以支持数据丰富的交易，为企业和消费者提供实时的现金流透明度和即时资金到账。其经济影响十分显著：据C.D. Howe研究所预测，通过降低处理成本和缩短“资金占用期”，RTR将节省高达145亿加元的成本，并带来160亿至270亿加元的广泛经济收益。

安全性是该系统的一大亮点；加拿大是七国集团（G7）中首个在启动时即强制实施集中化反欺诈服务的国家。这些服务包括“收款人确认”服务、交易安全评分以及一个旨在降低所有用户风险的集中式欺诈情报平台。

首批参与机构涵盖了金融科技公司和银行，包括Wealthsimple、KOHO、Questbank和美国银行（Bank of America）。虽然该系统采用分阶段推广，但其设计具备快速扩展能力；随着各大主要金融机构陆续接入，预计RTR在运行首年内将覆盖超过90%的加拿大人。

政府及行业领袖，包括财政部长商鹏飞（François-Philippe Champagne）和加拿大央行行长蒂夫·麦克勒姆（Tiff Macklem），将此次启动称作“加拿大团队”（Team Canada）的里程碑。他们强调，RTR提供了一个安全且植根于加拿大的基础，用以驱动创新、增强全球竞争力，并支持更具包容性的数字经济。

---

## 7. E-means: Outperforming k-means in one-tenth the epochs

**原文标题**: E-means: Outperforming k-means in one-tenth the epochs

**原文链接**: [https://e-means.github.io/](https://e-means.github.io/)

生成摘要时出错

---

## 8. Claude Fable 5.2 在 Artificial Analysis 获 65 分，创下目前最高纪录

**原文标题**: Claude Fable 5.2 Scores 65 on Artificial Analysis, Highest So Far

**原文链接**: [https://artificialanalysis.ai/models/claude-fable-5-2](https://artificialanalysis.ai/models/claude-fable-5-2)

Anthropic’s **Claude Fable 5.2 (Max)** has set a new record in AI performance, scoring **65** on the Artificial Analysis Intelligence Index—the highest recorded to date and well above the industry median of 40. Released in November 2026, this proprietary reasoning model leads in intelligence but comes with significant trade-offs in speed and cost.

**Key Performance Metrics:**
*   **Intelligence:** Ranked #1 out of 734 models. It excels in complex benchmarks like AA-Briefcase (agentic work), FrontierCode 2.0 (software engineering), and HLE-Diamond (reasoning).
*   **Speed and Latency:** The model is notably slow, averaging **44.1 minutes per task** compared to a 12.9-minute median. It has a high "time to first answer token" of 231.55 seconds, though it maintains an output speed of 103 tokens per second.
*   **Cost:** Pricing is premium at **$8.00 per 1M input tokens** and **$40.00 per 1M output tokens**. The average cost per intelligence task is $26.54, significantly higher than competitors.
*   **Verbosity:** The model is highly verbose, generating 275M tokens during the Intelligence Index evaluation—nearly four times the median volume.

**Technical Specifications:**
Claude Fable 5.2 supports multimodal inputs (text and images) and features a **1M token context window**. It is categorized as a reasoning model, designed for high-level analytical quality and transparency.

**Summary:**
While Claude Fable 5.2 establishes a new frontier for AI intelligence and agentic capabilities, its high operational costs and slow processing times position it as a specialized tool for complex reasoning tasks rather than high-speed, low-cost applications.

---

## 9. Our Smallest, Most Efficient Model: Muse Ember

**原文标题**: Our Smallest, Most Efficient Model: Muse Ember

**原文链接**: [https://research.meta.ai/blog/muse-ember](https://research.meta.ai/blog/muse-ember)

生成摘要时出错

---

## 10. Fold Epic Paper Airplanes

**原文标题**: Fold Epic Paper Airplanes

**原文链接**: [https://www.foldableflight.com](https://www.foldableflight.com)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-10](output/hacker_news_summary_2026-11-10.md) |
| 2 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 3 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 4 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 5 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 6 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 7 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 8 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 9 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 10 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 11 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 12 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 13 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 14 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 15 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 16 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 17 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 18 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 19 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 20 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 21 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 22 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 23 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 24 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 25 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 26 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 27 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 28 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 29 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 30 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 31 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 32 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 33 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 34 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 35 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 36 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 37 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 38 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 39 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 40 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 41 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 42 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 43 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 44 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 45 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 46 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 47 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 48 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 49 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 50 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 51 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 52 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 53 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 54 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 55 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 56 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 57 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 58 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 59 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 60 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 61 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 62 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 63 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 64 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 65 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 66 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 67 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 68 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 69 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 70 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 71 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 72 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 73 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 74 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 75 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 76 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 77 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 78 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 79 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 80 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 81 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 82 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 83 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 84 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 85 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 86 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 87 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 88 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 89 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 90 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 91 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 92 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 93 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 94 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 95 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 96 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 97 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 98 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 99 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 100 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 101 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 102 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 103 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 104 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 105 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 106 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 107 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 108 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 109 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 110 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 111 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 112 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 113 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 114 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 115 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 116 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 117 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 118 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 119 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 120 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 121 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 122 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 123 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 124 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 125 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 126 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 127 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 128 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 129 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 130 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 131 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 132 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 133 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 134 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 135 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 136 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 137 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 138 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 139 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 140 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 141 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 142 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 143 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 144 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 145 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 146 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 147 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 148 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 149 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 150 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 151 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 152 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 153 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 154 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 155 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 156 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 157 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 158 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 159 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 160 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 161 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 162 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 163 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 164 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 165 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 166 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 167 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 168 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 169 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 170 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 171 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 172 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 173 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 174 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 175 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 176 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 177 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 178 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 179 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 180 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 181 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 182 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 183 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 184 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 185 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 186 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 187 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 188 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 189 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 190 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 191 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 192 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 193 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 194 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 195 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 196 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 197 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 198 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 199 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 200 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 201 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 202 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 203 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 204 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 205 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 206 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 207 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 208 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 209 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 210 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 211 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 212 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 213 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 214 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 215 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 216 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 217 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 218 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 219 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 220 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 221 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 222 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 223 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 224 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 225 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 226 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 227 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 228 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 229 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 230 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 231 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 232 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 233 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 234 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 235 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 236 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 237 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 238 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 239 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 240 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 241 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 242 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 243 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 244 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 245 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 246 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 247 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 248 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 249 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 250 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 251 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 252 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 253 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 254 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 255 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 256 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 257 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 258 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 259 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 260 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 261 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 262 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 263 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 264 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 265 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 266 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 267 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 268 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 269 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 270 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 271 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 272 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 273 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 274 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 275 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 276 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 277 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 278 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 279 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 280 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 281 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 282 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 283 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 284 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 285 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 286 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 287 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 288 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 289 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 290 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 291 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 292 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 293 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 294 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 295 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 296 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 297 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 298 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 299 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 300 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 301 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 302 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 303 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 304 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 305 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 306 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 307 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 308 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 309 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 310 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 311 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 312 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 313 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 314 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 315 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 316 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 317 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 318 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 319 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 320 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 321 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 322 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 323 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 324 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 325 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 326 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 327 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 328 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 329 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 330 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 331 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 332 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 333 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 334 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 335 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 336 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 337 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 338 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 339 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 340 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 341 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 342 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 343 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 344 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 345 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 346 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 347 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 348 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 349 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 350 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 351 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 352 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 353 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 354 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 355 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 356 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 357 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 358 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 359 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 360 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 361 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 362 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 363 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 364 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 365 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 366 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 367 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 368 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 369 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 370 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 371 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 372 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 373 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 374 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 375 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 376 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 377 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 378 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 379 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 380 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 381 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 382 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 383 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 384 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 385 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 386 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 387 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 388 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 389 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 390 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 391 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 392 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 393 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 394 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 395 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 396 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 397 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 398 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 399 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 400 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 401 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 402 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 403 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 404 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 405 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 406 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 407 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 408 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 409 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 410 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 411 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 412 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 413 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 414 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 415 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 416 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 417 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 418 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 419 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 420 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 421 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 422 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 423 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 424 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 425 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 426 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 427 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 428 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 429 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 430 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 431 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 432 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 433 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 434 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 435 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 436 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 437 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 438 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 439 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 440 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 441 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 442 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 443 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 444 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 445 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 446 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 447 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 448 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 449 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 450 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 451 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 452 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 453 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 454 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 455 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 456 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 457 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 458 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 459 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 460 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 461 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 462 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 463 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 464 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 465 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 466 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 467 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 468 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 469 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 470 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 471 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 472 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 473 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 474 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 475 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 476 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 477 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 478 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 479 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 480 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 481 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 482 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 483 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 484 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 485 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 486 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 487 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 488 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 489 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 490 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 491 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 492 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 493 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 494 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 495 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 496 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 497 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 498 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 499 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 500 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 501 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 502 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 503 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 504 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 505 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 506 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 507 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 508 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 509 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 510 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 511 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 512 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 513 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 514 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 515 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 516 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 517 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 518 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 519 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 520 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 521 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 522 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 523 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 524 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 525 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 526 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 527 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 528 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 529 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 530 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 531 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 532 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 533 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 534 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 535 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 536 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 537 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 538 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 539 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 540 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 541 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 542 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 543 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 544 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 545 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 546 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 547 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 548 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 549 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 550 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 551 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 552 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 553 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 554 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 555 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 556 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 557 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 558 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 559 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 560 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 561 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 562 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 563 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 564 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 565 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 566 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 567 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 568 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 569 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 570 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 571 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 572 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 573 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 574 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 575 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 576 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 577 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 578 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 579 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 580 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 581 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 582 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 583 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 584 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 585 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 586 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 587 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 588 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 589 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 590 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 591 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 592 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 593 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 594 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 595 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 596 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
