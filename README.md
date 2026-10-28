# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-28.md)

*最后自动更新时间: 2026-10-28 21:57:03*
## 1. 为什么这个指纹识别脚本在制造生物武器？

**原文标题**: Why is this fingerprinting script creating bioweapons?

**原文链接**: [https://nullpt.rs/fingerprinting-bioweapons](https://nullpt.rs/fingerprinting-bioweapons)

在文章《为什么这个指纹脚本在制造生物武器？》中，作者“veritas”描述了他在通过抓取网页来映射浏览器 API 调用时，发现的一个极不寻常的浏览器指纹脚本。

该脚本由 `servicepipe.tech` 托管，最初看起来包含一些令人震惊的功能，涉及合成生物制剂、计算毒药致死剂量以及策划针对医疗基础设施的网络攻击。然而，作者揭示了这些内容实际上是一种复杂的“反大模型混淆”（anti-LLM obfuscation）手段。

通过在脚本中加入与高风险话题（如生物武器、自残和非法行为）以及政治敏感词（如“坦克人”或“8964”）相关的符号名称、字符串和系统提示词，开发者故意触发大语言模型（LLM）的安全护栏。这使得研究人员无法利用 AI 助手对代码进行反混淆或分析，因为模型会因内容“危险”而拒绝处理。

当作者改用限制较少的模型绕过这些触发机制后，该脚本的真实功能浮出水面：它只是一个标准的反机器人工具。它收集典型的指纹信号（如 WebGL 渲染器信息、硬件并发数和浏览器扩展），用于区分真实用户与自动化机器人。脚本中还包含一段具有误导性的 Node.js 代码，模仿了恶意软件下载器（malware dropper）的行为，这显然是为迷惑自动化分析工具而设计的另一层伪装。

作者将该脚本溯源至 Servicepipe，这是一家专注于 DDoS 防护和流量控制的俄罗斯网络安全公司。文章最后介绍了作者的项目 **fingerprint.garden**，该项目展示了他在抓取过程中收集到的各种 Canvas 渲染图。最终证明，那些“生物武器”引用并非真正的威胁，而是一种对抗 AI 辅助逆向工程的新型防御手段。

---

## 2. Gemini 4 碳

**原文标题**: Gemini 4 Carbon

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)

2026年10月28日，Google DeepMind发布了其迄今为止最先进的前沿模型——**Gemini 4 Carbon**。在近期发布的Gemini 4 Argon的基础之上，Carbon专为顶尖的网络安全和长时程智能体工作流而设计。

**关键性能与能力：**
*   **网络安全领先地位：** Carbon在漏洞检测（SEC-bench Pro得分88.2%）、漏洞利用验证（ExploitGym得分54.8%）和根因修复（CWE-bench得分71.0%）方面均取得了最高评分。
*   **长时程工程：** 该模型专为持续性任务构建，能够连续运行数日，在大型代码库中进行根因分析并修复复杂漏洞。
*   **编程与Web开发：** 它在人工智能分析指数（Artificial Analysis Intelligence Index）中排名第一，并在Web开发领域取得显著进步，在WebDev Arena的排名跃升至第四位。

**安全性与可靠性：**
Carbon在模型对齐和透明度方面带来了重大改进。它成功将Terminal-Bench 4.0上的作弊率降至0.0%，并在Gray Swan间接提示注入（IPI）基准测试中实现了0.0%的攻击成功率。内部测试显示，无根据的主张（幻觉）减少了2倍，实时编程期间的高严重性对齐失当警报降低了80%。

**定价与可用性：**
*   **定价：** 每百万输入Token为2美元，每百万输出Token为10美元（与Argon的初期定价一致）。
*   **发布计划：** Google正采取审慎的分阶段发布策略，首批包括美国政府的自愿预发布测试，以及通过Fairwind计划向部分网络安全防御者开放。预计不久后将向开发者、企业和消费者广泛发布。

---

## 3. 数控石材雕刻

**原文标题**: CNC Stone Carving

**原文链接**: [https://carmelitegothic.com/cnc-stone-carving/](https://carmelitegothic.com/cnc-stone-carving/)

加尔默罗修会的修士们正通过使用CNC（计算机数字控制）石材雕刻技术，将古老的哥特式建筑与现代科技相结合。利用来自普鲁西亚尼工程公司（Prussiani Engineering）的五轴和六轴机床，修士们可以在几天内完成过去需要数月才能实现的复杂细节，使哥特式教堂这一“浪漫构想”在经济和物质层面成为现实。

其技术流程涉及使用金刚石刀具，根据XYZ坐标对石材进行研磨。这些机器可以24小时无人值守运行，显著提高了生产率。工作流程分为三个主要角色：

1.  **艺术家：** 使用3D建模软件进行数字“雕刻”，允许进行无限次的实验，并能通过虚拟模型清晰地预览建筑成品。
2.  **程序员：** 通过CAM（计算机辅助加工）软件将这些模型转换为G代码，规划复杂的刀具路径，并管理刀具速度和防碰撞等逻辑。
3.  **锯切师：** 作为“现场执行者”，负责准备石块、设置参考点，并操作CNC机器和线锯，以确保程序完美地转化为石材作品。

这种数字化工作流程使当代青年——他们往往比使用传统锤凿更擅长操作计算机——能够将天赋投入到神圣的事业中。虽然传统手工雕刻方法仍发挥着作用，但CNC技术使修士们能够实现前所未有的3D浮雕和结构美感。最终，这种技术与信仰的融合服务于一个更高的目标：为上帝的荣耀建造一座旨在屹立数百年的宏伟教堂。

---

## 4. Formlabs Studio 1 $699 树脂打印机

**原文标题**: Formlabs Studio 1 $699 Resin Printer

**原文链接**: [https://formlabs.com/products/form-studio-1-basic-founders-edition/](https://formlabs.com/products/form-studio-1-basic-founders-edition/)

Formlabs 推出了其首款价格亲民的专业级树脂 3D 打印机 **Form Studio 1**，起售价为 **699 美元**。该打印机采用掩模光固化 (MSLA) 技术，专为速度和可靠性而设计，大多数零件的打印时间不足两小时，成型体积为 20.0 x 12.5 x 23.5 cm。

**核心功能与技术：**
*   **开放平台：** 包含“开放材料模式”，允许用户在使用 Formlabs 原厂材料的同时使用第三方树脂。
*   **安全与排放：** 配合选配的 VOC 提取器及全新的 Alpha 系列树脂使用时，它是首款获得 **UL GREENGUARD 金级认证**（低化学排放）的树脂打印机。
*   **易用性：** 支持“柔性成型平台 (Build Platform Flex)”，无需工具即可取下零件，实现流线化且整洁的工作流程。

**产品档次：**
1.  **基础版 ($699)：** 包含打印机、树脂槽和标准成型平台。
2.  **完整版 ($948)：** 增加柔性成型平台和 “Form Studio Wash+Cure” 一体式后处理机。
3.  **专业版 ($2,447)：** 包含高端、独立的 Form Wash 和 Form Cure V2 后处理设备。

此外还提供限量的**创始人版 (Founders Edition)**，采用专属配色（水蓝色、紫罗兰色和青色），并包含限量版毛绒玩具和树脂折扣等额外福利。

**材料：**
该打印机随 **Alpha 系列树脂**一同发布，包括：
*   **Alpha Fast：** 打印速度高达 130 mm/h。
*   **Alpha Model：** 具备高细节度和哑光表面，适用于手办模型。
*   **Alpha Grey/Clear/Black：** 用于功能性原型的多功能树脂。

总的来说，Form Studio 1 旨在弥补个人爱好者价位与专业级性能之间的差距，主要面向工程、牙科和创意行业。

---

## 5. Dayjob：税务——在 50 项专业税务任务中评估 AI 智能体

**原文标题**: Dayjob: Tax – evaluating AI agents on 50 professional tax assignments

**原文链接**: [https://surgehq.ai/blog/dayjob-tax](https://surgehq.ai/blog/dayjob-tax)

Surge AI 推出了 **DAYJOB: Tax**，这是一项旨在评估 AI 智能体执行专业级税务工作能力的新基准。与侧重于特定问题或计算的传统基准不同，DAYJOB: Tax 测试的是“专业判断力”——即识别潜在风险、解决矛盾证据以及管理端到端任务的能力。

**该基准的主要特点：**
*   **范围：** 涵盖国际税收、企业交易、合伙企业和遗产等 8 个税务领域的 50 个复杂环境。
*   **数据复杂性：** 智能体必须处理 1,789 个工作区文件，包括 PDF、Excel 工作簿、手写收据和现场日志。
*   **专业标准：** 由普华永道 (PwC) 和德勤 (Deloitte) 等机构的专家开发，任务要求智能体生成纳税申报表、工作底稿和咨询函。

**关键发现：**
该基准凸显了 AI 能力与专业要求之间的巨大差距。在一个案例研究中，智能体未能就即将到来的居住期限向客户发出警告，而这可能导致 25 万美元的税收减免损失。在另一个案例中，智能体假设一对夫妇未婚，忽略了文件中关于事实婚姻的证据，而这本会改变其退休账户分割的税务后果。

**性能结果：**
结果显示，前沿模型在处理专业税务咨询的细微差别方面仍面临困难：
*   **Claude Sonnet 5.5** 以仅 **10.8%** 的通过率位居榜首。
*   **Claude Fable 5.1** (9.6%) 和 **Claude Opus 5.5** (9.2%) 紧随其后。
*   较低的得分（以 95% 的评分标准阈值衡量）表明，虽然模型可以执行单个步骤，但缺乏独立承担完整专业任务所需的可靠性和判断力。

最终，Surge AI 得出结论：虽然 AI 智能体正在不断进化，但它们尚未通过现实世界专业税务工作的“审计”。

---

## 6. 配备 PROLED XDR 显示屏及触控功能的 MacBook Pro

**原文标题**: MacBook Pro with PROLED XDR Display and Touch

**原文链接**: [https://www.apple.com/macbook-pro/proled-xdr-display/](https://www.apple.com/macbook-pro/proled-xdr-display/)

搭载 PROLED XDR 显示屏的 MacBook Pro 标志着 Apple 专业笔记本系列的重大飞跃，不仅引入了串联 OLED 显示技术，更带来了 Mac 首个多点触控 (Multi-Touch) 界面。全新的 PROLED XDR 屏幕具备行业领先的规格，包括 2000 尼特峰值亮度、10,000,000:1 对比度，并支持 P3 及 Adobe RGB 广色域。

**核心功能包括：**
*   **触控与设计：** 触控传感器直接集成于显示屏以实现低延迟交互，方便专业人士操控 3D 对象或直接在屏幕上绘图。设计上还引入了灵动岛用于显示通知和聚焦搜索，并采用了更窄的边框和更轻巧的机身。
*   **性能：** 搭载 M5 Pro 和 M5 Max 芯片，针对 AI 进行了深度优化。它配备了强大的神经加速器和第三代光线追踪引擎。M5 Max 堪称“AI 猛兽”，支持高达 128GB 的统一内存和 16TB 存储空间，能够直接在设备上运行庞大的大语言模型 (LLM)。基准测试显示，其 LLM 处理速度比 M1 Max 快达 12 倍。
*   **连接性与续航：** 该笔记本支持雷雳 5、Wi-Fi 7 和蓝牙 6，并提供行业领先的 24 小时电池续航。
*   **多媒体：** 重新设计的六扬声器系统使低音深度提升了 50%，并配备支持“人物居中”和“桌上视角”功能的 1200 万像素摄像头，以及先进的视频防抖技术。

该款 MacBook Pro 提供 14 英寸和 16 英寸两种型号，可选深空黑色或银色，被定位为电影制作人、开发者和 AI 研究人员的终极利器。

---

## 7. Nango (YC W23) 正在招聘工程、FDE、市场及 DevRel 岗位

**原文标题**: Nango (YC W23) Is Hiring Across Eng, FDE, Marketing, DevRel

**原文链接**: [https://nango.dev/careers](https://nango.dev/careers)

Nango 是一家专注于产品集成的 YC W23 初创公司，目前正在招聘工程、现场交付工程 (FDE)、市场营销和开发者关系 (DevRel) 等多个部门的人才。

作为一家专家主导型组织，Nango 的团队由开发者基础设施领域的资深人士组成，致力于构建开源工具以解决 API 碎片化和大规模数据同步等复杂难题。

公司文化及核心优势包括：
*   **远程优先环境：** 全球化团队，相比固定工时，更注重产出和现代化的工作流程。
*   **专注开源：** 致力于保持透明度、积极参与社区并打造开发者友好型产品。
*   **技术挑战：** 有机会解决涉及开发者体验 (DevExp) 和大规模基础设施的硬核工程问题。
*   **高速增长：** 随着营收和使用量的快速增长，公司兼具初创公司的激情与强劲的发展势头。

Nango 旨在通过为同行构建工具来服务开发者社区，强调谦逊的态度、快速的反馈循环，并专注于解决真实的技术痛点。

---

## 8. Leak Exposes 41,000 Homeland Security Workers–Including Undercover ICE Agents

**原文标题**: Leak Exposes 41,000 Homeland Security Workers–Including Undercover ICE Agents

**原文链接**: [https://www.wired.com/story/massive-leak-exposes-41000-homeland-security-workers-including-undercover-ice-agents/](https://www.wired.com/story/massive-leak-exposes-41000-homeland-security-workers-including-undercover-ice-agents/)

A massive data leak titled "Icepick" has exposed the records of over 41,000 Department of Homeland Security (DHS) employees and contractors. Published by the transparency group Distributed Denial of Secrets (DDoSecrets) and researcher maia arson crimew, the archive includes personal contact information, office addresses, and internal system access details for personnel across agencies including ICE, CBP, USCIS, and CISA.

Significantly, the leak reveals sensitive information regarding "certified undercover operations," surveillance programs, and the use of specialized tools like facial recognition apps and AI platforms (ChatGPT, Gemini, and Grok). The data also exposes the reporting structures of senior leadership and reveals the identities of political appointees with ties to the second Trump administration.

The hackers, calling themselves the "Department of Peace," claim the data was obtained from DHS’s Okta login system, though Okta has denied any breach of its systems. The leak follows a similar recent breach involving FBI employee data.

This exposure occurs as the DHS aggressively moves to shield employee identities and expand the definition of "doxing" to include the publication of basic professional details. While the leak’s creators frame the release as a necessary tool for government accountability and a response to aggressive federal surveillance of protesters, national security experts warn the dataset is an "extraordinarily valuable intelligence resource." They suggest adversaries could use the information to identify vulnerable personnel, conduct targeted phishing attacks, or compromise ongoing criminal investigations.

---

## 9. The Grid, a factory-scale robot in Massachusetts that builds PCBs on demand

**原文标题**: The Grid, a factory-scale robot in Massachusetts that builds PCBs on demand

**原文链接**: [https://www.circuithub.com/post/unveiling-the-grid](https://www.circuithub.com/post/unveiling-the-grid)

生成摘要时出错

---

## 10. Start Doing Graph Theory

**原文标题**: Start Doing Graph Theory

**原文链接**: [https://vertex.degree/](https://vertex.degree/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 2 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 3 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 4 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 5 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 6 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 7 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 8 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 9 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 10 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 11 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 12 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 13 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 14 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 15 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 16 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 17 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 18 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 19 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 20 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 21 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 22 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 23 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 24 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 25 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 26 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 27 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 28 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 29 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 30 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 31 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 32 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 33 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 34 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 35 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 36 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 37 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 38 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 39 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 40 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 41 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 42 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 43 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 44 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 45 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 46 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 47 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 48 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 49 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 50 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 51 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 52 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 53 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 54 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 55 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 56 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 57 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 58 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 59 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 60 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 61 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 62 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 63 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 64 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 65 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 66 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 67 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 68 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 69 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 70 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 71 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 72 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 73 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 74 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 75 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 76 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 77 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 78 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 79 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 80 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 81 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 82 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 83 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 84 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 85 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 86 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 87 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 88 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 89 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 90 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 91 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 92 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 93 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 94 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 95 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 96 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 97 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 98 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 99 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 100 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 101 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 102 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 103 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 104 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 105 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 106 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 107 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 108 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 109 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 110 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 111 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 112 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 113 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 114 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 115 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 116 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 117 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 118 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 119 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 120 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 121 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 122 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 123 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 124 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 125 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 126 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 127 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 128 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 129 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 130 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 131 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 132 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 133 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 134 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 135 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 136 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 137 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 138 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 139 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 140 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 141 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 142 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 143 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 144 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 145 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 146 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 147 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 148 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 149 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 150 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 151 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 152 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 153 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 154 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 155 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 156 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 157 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 158 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 159 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 160 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 161 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 162 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 163 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 164 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 165 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 166 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 167 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 168 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 169 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 170 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 171 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 172 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 173 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 174 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 175 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 176 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 177 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 178 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 179 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 180 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 181 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 182 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 183 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 184 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 185 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 186 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 187 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 188 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 189 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 190 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 191 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 192 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 193 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 194 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 195 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 196 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 197 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 198 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 199 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 200 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 201 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 202 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 203 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 204 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 205 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 206 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 207 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 208 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 209 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 210 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 211 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 212 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 213 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 214 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 215 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 216 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 217 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 218 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 219 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 220 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 221 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 222 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 223 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 224 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 225 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 226 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 227 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 228 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 229 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 230 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 231 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 232 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 233 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 234 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 235 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 236 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 237 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 238 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 239 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 240 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 241 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 242 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 243 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 244 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 245 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 246 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 247 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 248 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 249 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 250 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 251 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 252 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 253 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 254 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 255 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 256 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 257 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 258 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 259 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 260 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 261 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 262 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 263 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 264 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 265 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 266 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 267 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 268 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 269 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 270 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 271 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 272 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 273 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 274 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 275 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 276 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 277 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 278 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 279 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 280 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 281 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 282 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 283 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 284 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 285 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 286 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 287 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 288 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 289 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 290 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 291 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 292 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 293 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 294 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 295 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 296 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 297 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 298 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 299 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 300 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 301 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 302 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 303 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 304 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 305 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 306 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 307 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 308 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 309 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 310 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 311 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 312 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 313 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 314 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 315 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 316 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 317 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 318 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 319 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 320 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 321 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 322 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 323 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 324 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 325 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 326 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 327 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 328 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 329 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 330 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 331 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 332 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 333 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 334 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 335 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 336 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 337 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 338 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 339 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 340 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 341 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 342 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 343 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 344 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 345 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 346 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 347 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 348 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 349 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 350 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 351 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 352 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 353 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 354 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 355 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 356 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 357 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 358 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 359 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 360 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 361 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 362 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 363 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 364 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 365 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 366 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 367 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 368 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 369 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 370 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 371 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 372 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 373 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 374 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 375 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 376 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 377 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 378 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 379 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 380 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 381 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 382 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 383 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 384 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 385 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 386 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 387 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 388 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 389 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 390 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 391 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 392 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 393 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 394 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 395 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 396 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 397 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 398 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 399 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 400 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 401 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 402 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 403 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 404 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 405 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 406 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 407 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 408 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 409 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 410 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 411 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 412 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 413 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 414 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 415 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 416 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 417 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 418 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 419 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 420 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 421 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 422 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 423 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 424 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 425 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 426 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 427 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 428 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 429 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 430 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 431 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 432 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 433 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 434 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 435 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 436 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 437 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 438 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 439 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 440 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 441 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 442 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 443 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 444 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 445 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 446 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 447 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 448 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 449 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 450 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 451 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 452 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 453 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 454 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 455 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 456 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 457 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 458 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 459 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 460 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 461 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 462 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 463 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 464 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 465 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 466 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 467 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 468 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 469 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 470 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 471 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 472 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 473 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 474 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 475 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 476 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 477 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 478 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 479 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 480 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 481 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 482 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 483 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 484 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 485 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 486 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 487 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 488 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 489 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 490 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 491 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 492 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 493 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 494 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 495 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 496 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 497 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 498 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 499 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 500 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 501 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 502 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 503 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 504 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 505 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 506 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 507 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 508 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 509 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 510 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 511 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 512 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 513 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 514 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 515 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 516 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 517 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 518 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 519 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 520 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 521 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 522 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 523 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 524 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 525 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 526 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 527 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 528 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 529 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 530 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 531 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 532 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 533 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 534 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 535 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 536 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 537 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 538 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 539 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 540 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 541 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 542 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 543 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 544 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 545 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 546 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 547 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 548 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 549 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 550 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 551 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 552 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 553 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 554 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 555 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 556 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 557 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 558 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 559 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 560 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 561 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 562 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 563 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 564 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 565 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 566 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 567 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 568 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 569 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 570 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 571 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 572 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 573 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 574 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 575 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 576 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 577 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 578 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 579 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 580 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 581 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 582 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 583 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 584 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 585 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
