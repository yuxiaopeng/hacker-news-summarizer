# Hacker News 热门文章摘要 (2026-10-28)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. The Style Is Father of the Man

**原文标题**: The Style Is Father of the Man

**原文链接**: [https://harpers.org/archive/2026/11/benjamin-kunkel-reviews-cormac-mccarthy-legacy-revisted/](https://harpers.org/archive/2026/11/benjamin-kunkel-reviews-cormac-mccarthy-legacy-revisted/)

生成摘要时出错

---

## 12. AlpineBSD

**原文标题**: AlpineBSD

**原文链接**: [https://wiki.alpinebsd.org](https://wiki.alpinebsd.org)

生成摘要时出错

---

## 13. The case of the 9 bit AES key

**原文标题**: The case of the 9 bit AES key

**原文链接**: [https://v12.sh/blog/the-case-of-the-9bit-aes-key](https://v12.sh/blog/the-case-of-the-9bit-aes-key)

生成摘要时出错

---

## 14. Apple's git still trusts the compromised eMudhra certificates

**原文标题**: Apple's git still trusts the compromised eMudhra certificates

**原文链接**: [https://emudhra.we-have-a-problem.com/apple.html](https://emudhra.we-have-a-problem.com/apple.html)

生成摘要时出错

---

## 15. The tragedy of losing your Wikipedia page

**原文标题**: The tragedy of losing your Wikipedia page

**原文链接**: [https://www.wired.com/story/the-tragedy-of-losing-your-wikipedia-page/](https://www.wired.com/story/the-tragedy-of-losing-your-wikipedia-page/)

生成摘要时出错

---

## 16. Spiders Spin 'Silk Dope' into Nature's Toughest Material

**原文标题**: Spiders Spin 'Silk Dope' into Nature's Toughest Material

**原文链接**: [https://www.quantamagazine.org/how-spiders-spin-silk-dope-into-natures-toughest-material-20261028/](https://www.quantamagazine.org/how-spiders-spin-silk-dope-into-natures-toughest-material-20261028/)

生成摘要时出错

---

## 17. The Agent SDK

**原文标题**: The Agent SDK

**原文链接**: [https://cursor.com/blog/agent-sdk](https://cursor.com/blog/agent-sdk)

生成摘要时出错

---

## 18. Show HN: SlideBySide – Present slides without sharing your screen

**原文标题**: Show HN: SlideBySide – Present slides without sharing your screen

**原文链接**: [https://slidebyside.com/](https://slidebyside.com/)

生成摘要时出错

---

## 19. Gaussian Splats part 3: There's always a bigger scene

**原文标题**: Gaussian Splats part 3: There's always a bigger scene

**原文链接**: [https://www.magnopus.com/blog/gaussiansplats-part-3-theres-always-a-bigger-scene](https://www.magnopus.com/blog/gaussiansplats-part-3-theres-always-a-bigger-scene)

生成摘要时出错

---

## 20. Emacs Turns 50

**原文标题**: Emacs Turns 50

**原文链接**: [https://www.technologyreview.com/2026/10/20/1145399/emacs-turns-50/](https://www.technologyreview.com/2026/10/20/1145399/emacs-turns-50/)

生成摘要时出错

---

## 21. Regent's Ground-Effect Vehicle Reimagines Coastal Travel

**原文标题**: Regent's Ground-Effect Vehicle Reimagines Coastal Travel

**原文链接**: [https://spectrum.ieee.org/ground-effect-vehicle](https://spectrum.ieee.org/ground-effect-vehicle)

生成摘要时出错

---

## 22. Google AI gets cagey when asked who won the 2020 elections

**原文标题**: Google AI gets cagey when asked who won the 2020 elections

**原文链接**: [https://arstechnica.com/ai/2026/10/google-ai-gets-cagey-when-asked-who-won-the-2020-elections/](https://arstechnica.com/ai/2026/10/google-ai-gets-cagey-when-asked-who-won-the-2020-elections/)

生成摘要时出错

---

## 23. Oseberg Tapestry Fragments

**原文标题**: Oseberg Tapestry Fragments

**原文链接**: [https://en.wikipedia.org/wiki/Oseberg_tapestry_fragments](https://en.wikipedia.org/wiki/Oseberg_tapestry_fragments)

生成摘要时出错

---

## 24. Kentucky man becomes the first humanist granted religious exemption from AI

**原文标题**: Kentucky man becomes the first humanist granted religious exemption from AI

**原文链接**: [https://religionnews.com/2026/10/26/in-a-first-a-humanist-granted-a-religious-exemption-from-using-ai/](https://religionnews.com/2026/10/26/in-a-first-a-humanist-granted-a-religious-exemption-from-using-ai/)

生成摘要时出错

---

## 25. Decompiling Fast Food Tycoon 2: Drawing the World

**原文标题**: Decompiling Fast Food Tycoon 2: Drawing the World

**原文链接**: [https://healeycodes.com/decompiling-fast-food-tycoon-2-drawing-the-world](https://healeycodes.com/decompiling-fast-food-tycoon-2-drawing-the-world)

生成摘要时出错

---

## 26. Archive.today links going forward

**原文标题**: Archive.today links going forward

**原文链接**: [https://www.reddit.com/r/Seattle/comments/1xhf6qp/archivetoday_links_going_forward/](https://www.reddit.com/r/Seattle/comments/1xhf6qp/archivetoday_links_going_forward/)

生成摘要时出错

---

## 27. Executable Archaeology: Reanimating the Heuristic Compiler (1961) and KBEmacs (1984)

**原文标题**: Executable Archaeology: Reanimating the Heuristic Compiler (1961) and KBEmacs (1984)

**原文链接**: [https://arxiv.org/abs/2610.36341](https://arxiv.org/abs/2610.36341)

生成摘要时出错

---

## 28. Nvidia Nemotron 3.5 Transcribe: open ASR for 40 languages

**原文标题**: Nvidia Nemotron 3.5 Transcribe: open ASR for 40 languages

**原文链接**: [https://huggingface.co/blog/nvidia/nemotron-transcribe-granary](https://huggingface.co/blog/nvidia/nemotron-transcribe-granary)

生成摘要时出错

---

## 29. Meta censored the No Kings Instagram account during a nationwide campaign

**原文标题**: Meta censored the No Kings Instagram account during a nationwide campaign

**原文链接**: [https://paulfwalsh.substack.com/p/meta-censored-the-no-kings-instagram](https://paulfwalsh.substack.com/p/meta-censored-the-no-kings-instagram)

生成摘要时出错

---

## 30. US agency approves Amazon Leo’s $11.5B acquisition of Globalstar

**原文标题**: US agency approves Amazon Leo’s $11.5B acquisition of Globalstar

**原文链接**: [https://www.reuters.com/business/media-telecom/us-agency-approves-amazon-leos-115-billion-acquisition-globalstar-2026-10-27/](https://www.reuters.com/business/media-telecom/us-agency-approves-amazon-leos-115-billion-acquisition-globalstar-2026-10-27/)

生成摘要时出错

---

## 31. MacOS Extensions Pack for the Apple Network Server v1.0

**原文标题**: MacOS Extensions Pack for the Apple Network Server v1.0

**原文链接**: [http://oldvcr.blogspot.com/2026/10/macos-extensions-pack-for-apple-network.html](http://oldvcr.blogspot.com/2026/10/macos-extensions-pack-for-apple-network.html)

生成摘要时出错

---

## 32. Ghostty 1.4

**原文标题**: Ghostty 1.4

**原文链接**: [https://ghostty.org/docs/install/release-notes/1-4-0](https://ghostty.org/docs/install/release-notes/1-4-0)

生成摘要时出错

---

## 33. Leak website releases data on DHS employees

**原文标题**: Leak website releases data on DHS employees

**原文链接**: [https://www.reuters.com/legal/government/leak-website-releases-data-tens-thousands-dhs-employees-2026-10-28/](https://www.reuters.com/legal/government/leak-website-releases-data-tens-thousands-dhs-employees-2026-10-28/)

生成摘要时出错

---

## 34. Genie 4

**原文标题**: Genie 4

**原文链接**: [https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)

生成摘要时出错

---

## 35. Git for the US Code

**原文标题**: Git for the US Code

**原文链接**: [https://lexifina.com/blog/git-for-the-us-code](https://lexifina.com/blog/git-for-the-us-code)

生成摘要时出错

---

## 36. Sleep framework: A new way for LLMs to retain knowledge in continual learning

**原文标题**: Sleep framework: A new way for LLMs to retain knowledge in continual learning

**原文链接**: [https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/](https://research.google/blog/the-sleep-framework-a-new-way-for-llms-to-retain-knowledge-in-continual-learning/)

生成摘要时出错

---

## 37. Scaling Hierarchical Networks

**原文标题**: Scaling Hierarchical Networks

**原文链接**: [https://www.cartesia.ai/blog/from-tokens-to-bytes-part-1](https://www.cartesia.ai/blog/from-tokens-to-bytes-part-1)

生成摘要时出错

---

## 38. Ink droplets in motion snag top prize in Nikon Small World contest

**原文标题**: Ink droplets in motion snag top prize in Nikon Small World contest

**原文链接**: [https://arstechnica.com/science/2026/10/meet-the-2026-winner-of-nikons-small-world-photomicrography-contest/](https://arstechnica.com/science/2026/10/meet-the-2026-winner-of-nikons-small-world-photomicrography-contest/)

生成摘要时出错

---

## 39. Counting Sand Dunes in the Simpson Desert

**原文标题**: Counting Sand Dunes in the Simpson Desert

**原文链接**: [https://www.fromtheroad.ford.com/img/en/articles/2026/simpson-desert-ranger-super-duty-counting-dunes](https://www.fromtheroad.ford.com/img/en/articles/2026/simpson-desert-ranger-super-duty-counting-dunes)

生成摘要时出错

---

## 40. About the compromised eMudhra intermediate CAs

**原文标题**: About the compromised eMudhra intermediate CAs

**原文链接**: [https://support.apple.com/en-us/149555](https://support.apple.com/en-us/149555)

生成摘要时出错

---

## 41. Show HN: Yavashark: I've Built a JavaScript Engine Every Day for 950 Days

**原文标题**: Show HN: Yavashark: I've Built a JavaScript Engine Every Day for 950 Days

**原文链接**: [https://yavashark.dev/blog/announcing-yavashark/](https://yavashark.dev/blog/announcing-yavashark/)

生成摘要时出错

---

## 42. Raspberry Pi Zero 3W and Pi 4 Model A spotted in device trees

**原文标题**: Raspberry Pi Zero 3W and Pi 4 Model A spotted in device trees

**原文链接**: [https://bret.dk/raspberry-pi-zero-3-w-pi-4-model-a/](https://bret.dk/raspberry-pi-zero-3-w-pi-4-model-a/)

生成摘要时出错

---

## 43. Mecca Defence Alliance

**原文标题**: Mecca Defence Alliance

**原文链接**: [https://en.wikipedia.org/wiki/Mecca_Defence_Alliance](https://en.wikipedia.org/wiki/Mecca_Defence_Alliance)

生成摘要时出错

---

## 44. An examination of lost firefly species of the US and Canada

**原文标题**: An examination of lost firefly species of the US and Canada

**原文链接**: [https://journaloflostspecies.org/index.php/jls/article/view/37/33](https://journaloflostspecies.org/index.php/jls/article/view/37/33)

生成摘要时出错

---

## 45. Survival LLM: AI assistant and emergency library that runs on your own computer

**原文标题**: Survival LLM: AI assistant and emergency library that runs on your own computer

**原文链接**: [https://www.brangus.io/survival-llm](https://www.brangus.io/survival-llm)

生成摘要时出错

---

## 46. The Colors of a Soap Film

**原文标题**: The Colors of a Soap Film

**原文链接**: [https://aseemrb.me/blog/colors-of-a-soap-film/](https://aseemrb.me/blog/colors-of-a-soap-film/)

生成摘要时出错

---

## 47. A Love Letter to the Super Dimension Fortress

**原文标题**: A Love Letter to the Super Dimension Fortress

**原文链接**: [https://brennan.day/a-love-letter-to-the-super-dimension-fortress/](https://brennan.day/a-love-letter-to-the-super-dimension-fortress/)

生成摘要时出错

---

## 48. Four Months of Zig

**原文标题**: Four Months of Zig

**原文链接**: [https://gracefulliberty.com/articles/four-months-of-zig/](https://gracefulliberty.com/articles/four-months-of-zig/)

生成摘要时出错

---

## 49. Rising rates of colorectal cancer found in nearly all age groups

**原文标题**: Rising rates of colorectal cancer found in nearly all age groups

**原文链接**: [https://www.uchicagomedicine.org/forefront/cancer-articles/rising-rates-of-colorectal-cancer](https://www.uchicagomedicine.org/forefront/cancer-articles/rising-rates-of-colorectal-cancer)

生成摘要时出错

---

## 50. Show HN: Squishy 3D helpers powered by Three.js

**原文标题**: Show HN: Squishy 3D helpers powered by Three.js

**原文链接**: [https://prathje.github.io/plushies/](https://prathje.github.io/plushies/)

生成摘要时出错

---

## 51. Jokes for the ZX81

**原文标题**: Jokes for the ZX81

**原文链接**: [https://spelk.press/gb/products/81-jokes-for-the-zx81](https://spelk.press/gb/products/81-jokes-for-the-zx81)

生成摘要时出错

---

## 52. Evidence of a spying operation by ICE against left-wing social movements

**原文标题**: Evidence of a spying operation by ICE against left-wing social movements

**原文链接**: [https://www.wired.com/story/ice-is-running-one-of-the-largest-anti-left-surveillance-operations-in-us-history/](https://www.wired.com/story/ice-is-running-one-of-the-largest-anti-left-surveillance-operations-in-us-history/)

生成摘要时出错

---

## 53. Moxnox 1.0: NT-Like, POSIX-Compatible OS Running Atop Btrfs

**原文标题**: Moxnox 1.0: NT-Like, POSIX-Compatible OS Running Atop Btrfs

**原文链接**: [https://github.com/maharmstone/moxnox](https://github.com/maharmstone/moxnox)

生成摘要时出错

---

## 54. Tailscale SSH: Investigation and remediation update

**原文标题**: Tailscale SSH: Investigation and remediation update

**原文链接**: [https://tailscale.com/ssh-investigation-update](https://tailscale.com/ssh-investigation-update)

生成摘要时出错

---

## 55. Decompiling Games with AI: Virtueel Zoetermeer

**原文标题**: Decompiling Games with AI: Virtueel Zoetermeer

**原文链接**: [https://bou.ke/blog/zoetermeer/](https://bou.ke/blog/zoetermeer/)

生成摘要时出错

---

## 56. Show HN: Nasscad – local-first 3D CAD for browser and Windows

**原文标题**: Show HN: Nasscad – local-first 3D CAD for browser and Windows

**原文链接**: [https://www.nasscad.com/NASSCAD_V4_7_0.htm](https://www.nasscad.com/NASSCAD_V4_7_0.htm)

生成摘要时出错

---

## 57. Early progress on accelerating drug development with Claude

**原文标题**: Early progress on accelerating drug development with Claude

**原文链接**: [https://www.anthropic.com/research/early-progress-drug-development](https://www.anthropic.com/research/early-progress-drug-development)

生成摘要时出错

---

## 58. Radio-tagged Monarch butterflies

**原文标题**: Radio-tagged Monarch butterflies

**原文链接**: [https://news.vt.edu/articles/2026/10/cmi-monarchs.html](https://news.vt.edu/articles/2026/10/cmi-monarchs.html)

生成摘要时出错

---

## 59. Introducing LFM3: Every Modality for Specialized Intelligence

**原文标题**: Introducing LFM3: Every Modality for Specialized Intelligence

**原文链接**: [https://www.liquid.ai/blog/lfm3](https://www.liquid.ai/blog/lfm3)

生成摘要时出错

---

## 60. An architectural comparison of Obsidian Canvas and Heptabase

**原文标题**: An architectural comparison of Obsidian Canvas and Heptabase

**原文链接**: [https://www.fluxlinks.com/blog/obsidian-canvas-vs-heptabase](https://www.fluxlinks.com/blog/obsidian-canvas-vs-heptabase)

生成摘要时出错

---

## 61. Particle-1

**原文标题**: Particle-1

**原文链接**: [https://particle.ai/blog/introducing-particle-1](https://particle.ai/blog/introducing-particle-1)

生成摘要时出错

---

## 62. Three new discoveries in mathematics, computer science, and physics

**原文标题**: Three new discoveries in mathematics, computer science, and physics

**原文链接**: [https://openai.com/index/building-scientific-understanding-with-academic-communities/](https://openai.com/index/building-scientific-understanding-with-academic-communities/)

生成摘要时出错

---

## 63. Assembly Nights (2021)

**原文标题**: Assembly Nights (2021)

**原文链接**: [https://ratfactor.com/assembly-nights](https://ratfactor.com/assembly-nights)

生成摘要时出错

---

## 64. Python's experimental JIT to be removed

**原文标题**: Python's experimental JIT to be removed

**原文链接**: [https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/](https://lwn.net/SubscriberLink/1102102/0c00e4d550f25f8c/)

生成摘要时出错

---

## 65. Scanning 7.25M Public Repositories on China's Largest Git Platform for Secrets

**原文标题**: Scanning 7.25M Public Repositories on China's Largest Git Platform for Secrets

**原文链接**: [https://www.mongodb.com/company/blog/technical/scanning-7-point-25-million-public-repositories-chinas-largest-git-platform-for-secrets](https://www.mongodb.com/company/blog/technical/scanning-7-point-25-million-public-repositories-chinas-largest-git-platform-for-secrets)

生成摘要时出错

---

## 66. Land Value Capture in Practice: Ethiopia's Urban Land Lease System

**原文标题**: Land Value Capture in Practice: Ethiopia's Urban Land Lease System

**原文链接**: [https://blog.landeconomics.org/p/land-value-capture-in-practice-reflections](https://blog.landeconomics.org/p/land-value-capture-in-practice-reflections)

生成摘要时出错

---

## 67. NTFS3 Hardened in Linux 7.4 Against Corrupted Maliciously-Crafted NTFS Volumes

**原文标题**: NTFS3 Hardened in Linux 7.4 Against Corrupted Maliciously-Crafted NTFS Volumes

**原文链接**: [https://www.phoronix.com/news/Linux-7.4-NTFS3](https://www.phoronix.com/news/Linux-7.4-NTFS3)

生成摘要时出错

---

## 68. The October inflection point for vibe game development

**原文标题**: The October inflection point for vibe game development

**原文链接**: [https://simonwillison.net/2026/Oct/28/vibe-game-development/](https://simonwillison.net/2026/Oct/28/vibe-game-development/)

生成摘要时出错

---

## 69. Nintendo's worst nightmare begins as Switch 2 games start running on PC and Mac

**原文标题**: Nintendo's worst nightmare begins as Switch 2 games start running on PC and Mac

**原文链接**: [https://videocardz.com/newz/nintendos-worst-nightmare-begins-as-switch-2-exclusive-games-start-running-on-pcs-and-macs](https://videocardz.com/newz/nintendos-worst-nightmare-begins-as-switch-2-exclusive-games-start-running-on-pcs-and-macs)

生成摘要时出错

---

## 70. How fast can you actually patch Ruby?

**原文标题**: How fast can you actually patch Ruby?

**原文链接**: [https://paagman.dev/how-fast-can-you-patch-ruby/](https://paagman.dev/how-fast-can-you-patch-ruby/)

生成摘要时出错

---

## 71. Hex Raises $100M

**原文标题**: Hex Raises $100M

**原文链接**: [https://hex.tech/blog/hex-new-era/](https://hex.tech/blog/hex-new-era/)

生成摘要时出错

---

## 72. Show HN: Popkern – open-source CAD kernel with G2 corner blends, browser IDE

**原文标题**: Show HN: Popkern – open-source CAD kernel with G2 corner blends, browser IDE

**原文链接**: [https://popkern.dev/](https://popkern.dev/)

生成摘要时出错

---

## 73. Here be monsters: What do you still need to know when agents do the work?

**原文标题**: Here be monsters: What do you still need to know when agents do the work?

**原文链接**: [https://blog.adrq.dev/here-be-monsters-what-do-you-still-need-to-know-when-agents-do-the-work](https://blog.adrq.dev/here-be-monsters-what-do-you-still-need-to-know-when-agents-do-the-work)

生成摘要时出错

---

## 74. Wikipedia's Cleanup of AI-Generated Content

**原文标题**: Wikipedia's Cleanup of AI-Generated Content

**原文链接**: [https://spectrum.ieee.org/wikipedia-wikiproject-ai-writing-cleanup](https://spectrum.ieee.org/wikipedia-wikiproject-ai-writing-cleanup)

生成摘要时出错

---

## 75. GitHub saw 7.4B commits in Sep., adding 4M CPU cores+160 PB storage to keep up

**原文标题**: GitHub saw 7.4B commits in Sep., adding 4M CPU cores+160 PB storage to keep up

**原文链接**: [https://thenewstack.io/github-7-4b-commits-september/](https://thenewstack.io/github-7-4b-commits-september/)

生成摘要时出错

---

## 76. Major Memory Vendor: We're Basically Sold Out Through 2029

**原文标题**: Major Memory Vendor: We're Basically Sold Out Through 2029

**原文链接**: [https://www.pcmag.com/news/sk-hynix-major-memory-vendor-basically-sold-out-through-2029](https://www.pcmag.com/news/sk-hynix-major-memory-vendor-basically-sold-out-through-2029)

生成摘要时出错

---

## 77. New 14‑inch MacBook Pro with M6

**原文标题**: New 14‑inch MacBook Pro with M6

**原文链接**: [https://www.apple.com/in/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/](https://www.apple.com/in/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/)

生成摘要时出错

---

## 78. Astronomers Discover a Giant New Dwarf Planet Candidate Hiding Beyond Pluto

**原文标题**: Astronomers Discover a Giant New Dwarf Planet Candidate Hiding Beyond Pluto

**原文链接**: [https://www.sciencealert.com/astronomers-discover-giant-new-dwarf-planet-candidate-hiding-beyond-pluto](https://www.sciencealert.com/astronomers-discover-giant-new-dwarf-planet-candidate-hiding-beyond-pluto)

生成摘要时出错

---

## 79. I've used WordPress for 20 years, and I've stopped recommending it

**原文标题**: I've used WordPress for 20 years, and I've stopped recommending it

**原文链接**: [https://hatamoto.dev/post/wordpress-20-years-why-we-built-hatamoto](https://hatamoto.dev/post/wordpress-20-years-why-we-built-hatamoto)

生成摘要时出错

---

## 80. Closing the Sea: Lessons from Ancient Mediterranean Blockades

**原文标题**: Closing the Sea: Lessons from Ancient Mediterranean Blockades

**原文链接**: [https://maritime-executive.com/editorials/closing-the-sea-lessons-from-ancient-mediterranean-blockades](https://maritime-executive.com/editorials/closing-the-sea-lessons-from-ancient-mediterranean-blockades)

生成摘要时出错

---

## 81. New iMac with M6

**原文标题**: New iMac with M6

**原文链接**: [https://www.apple.com/imac/](https://www.apple.com/imac/)

生成摘要时出错

---

## 82. Big Tech's thirst for water is sparking a global resistance

**原文标题**: Big Tech's thirst for water is sparking a global resistance

**原文链接**: [https://restofworld.org/2026/ai-datacenters-water-resistance-global/](https://restofworld.org/2026/ai-datacenters-water-resistance-global/)

生成摘要时出错

---

## 83. Code-execution flaw in UEFI firmware threatens most servers on planet Earth

**原文标题**: Code-execution flaw in UEFI firmware threatens most servers on planet Earth

**原文链接**: [https://arstechnica.com/security/2026/10/code-execution-flaw-in-uefi-firmware-threatens-most-servers-on-planet-earth/](https://arstechnica.com/security/2026/10/code-execution-flaw-in-uefi-firmware-threatens-most-servers-on-planet-earth/)

生成摘要时出错

---

## 84. The Mythical Man-Month in the Age of AI

**原文标题**: The Mythical Man-Month in the Age of AI

**原文链接**: [https://j11g.com/the-mythical-man-month-in-the-age-of-ai](https://j11g.com/the-mythical-man-month-in-the-age-of-ai)

生成摘要时出错

---

## 85. SS United States to be sunk as largest artificial reef

**原文标题**: SS United States to be sunk as largest artificial reef

**原文链接**: [https://divemagazine.com/scuba-diving-news/ss-united-states-to-be-sunk-as-worlds-largest-artificial-reef-in-november](https://divemagazine.com/scuba-diving-news/ss-united-states-to-be-sunk-as-worlds-largest-artificial-reef-in-november)

生成摘要时出错

---

## 86. Passengers injured after collision between bus and delivery robot in Tallinn

**原文标题**: Passengers injured after collision between bus and delivery robot in Tallinn

**原文链接**: [https://news.err.ee/1610179027/passengers-injured-after-collision-between-bus-and-delivery-robot-in-tallinn](https://news.err.ee/1610179027/passengers-injured-after-collision-between-bus-and-delivery-robot-in-tallinn)

生成摘要时出错

---

## 87. OpenLDK: Bringing the Java World into Common Lisp

**原文标题**: OpenLDK: Bringing the Java World into Common Lisp

**原文链接**: [https://atgreen.github.io/repl-yell/posts/openldk-java-in-common-lisp/](https://atgreen.github.io/repl-yell/posts/openldk-java-in-common-lisp/)

生成摘要时出错

---

## 88. Germanys' AfD in Saxony-Anhalt: Porno, Putin, Criminals, Nazi Songs, Corruption

**原文标题**: Germanys' AfD in Saxony-Anhalt: Porno, Putin, Criminals, Nazi Songs, Corruption

**原文链接**: [https://www.crossbordertalks.eu/2026/10/24/germanys-afd-in-saxony-anhalt-porno-putin-criminals-ai-nazi-songs-corruption-rape-antisemitism/](https://www.crossbordertalks.eu/2026/10/24/germanys-afd-in-saxony-anhalt-porno-putin-criminals-ai-nazi-songs-corruption-rape-antisemitism/)

生成摘要时出错

---

## 89. Anthropic trained Claude on illegally obtained Stanford professors' books

**原文标题**: Anthropic trained Claude on illegally obtained Stanford professors' books

**原文链接**: [https://stanforddaily.com/2026/10/27/professors-books-pirated-to-train-claude/](https://stanforddaily.com/2026/10/27/professors-books-pirated-to-train-claude/)

生成摘要时出错

---

## 90. Amazon Is Gutting Its AI Division After Sustained Failure

**原文标题**: Amazon Is Gutting Its AI Division After Sustained Failure

**原文链接**: [https://futurism.com/artificial-intelligence/amazon-ai-division-failure-nova](https://futurism.com/artificial-intelligence/amazon-ai-division-failure-nova)

生成摘要时出错

---

## 91. Expanding our partnership with GSA to bring Claude to all levels of government

**原文标题**: Expanding our partnership with GSA to bring Claude to all levels of government

**原文链接**: [https://www.anthropic.com/news/expanding-partnership-gsa](https://www.anthropic.com/news/expanding-partnership-gsa)

生成摘要时出错

---

## 92. It's now official, tech is the new tobacco

**原文标题**: It's now official, tech is the new tobacco

**原文链接**: [https://cailinoconnor.substack.com/p/its-now-official-tech-is-the-new](https://cailinoconnor.substack.com/p/its-now-official-tech-is-the-new)

生成摘要时出错

---

## 93. Classification of Finite Simple Groups Formalized in Lean

**原文标题**: Classification of Finite Simple Groups Formalized in Lean

**原文链接**: [https://cfsg.axiommath.ai/](https://cfsg.axiommath.ai/)

生成摘要时出错

---

## 94. Nvidia and Micron Make Up 34% of America's Earnings Boom

**原文标题**: Nvidia and Micron Make Up 34% of America's Earnings Boom

**原文链接**: [https://www.wsj.com/finance/stocks/the-earnings-boom-is-heavily-reliant-on-just-a-handful-of-stocks-21decb53](https://www.wsj.com/finance/stocks/the-earnings-boom-is-heavily-reliant-on-just-a-handful-of-stocks-21decb53)

生成摘要时出错

---

## 95. Hunger beats tenure: Advice for junior engineers

**原文标题**: Hunger beats tenure: Advice for junior engineers

**原文链接**: [https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/](https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/)

生成摘要时出错

---

## 96. I still teach OpenGL ES 3.0

**原文标题**: I still teach OpenGL ES 3.0

**原文链接**: [https://eliasfarhan.ch/graphics/cpp/2026/01/27/why-i-teach-opengles.html](https://eliasfarhan.ch/graphics/cpp/2026/01/27/why-i-teach-opengles.html)

生成摘要时出错

---

## 97. Three TLS Bugs in GoAhead

**原文标题**: Three TLS Bugs in GoAhead

**原文链接**: [https://foxio.io/blog/choose-your-backend-three-tls-bugs-in-goahead](https://foxio.io/blog/choose-your-backend-three-tls-bugs-in-goahead)

生成摘要时出错

---

## 98. Microsoft and Epic Games Suddenly Agree That AI Is Theft

**原文标题**: Microsoft and Epic Games Suddenly Agree That AI Is Theft

**原文链接**: [https://kotaku.com/now-that-the-shoe-is-on-the-other-foot-microsoft-and-epic-games-suddenly-agree-that-ai-is-theft-2000749316](https://kotaku.com/now-that-the-shoe-is-on-the-other-foot-microsoft-and-epic-games-suddenly-agree-that-ai-is-theft-2000749316)

生成摘要时出错

---

## 99. We should be more ambitious with the software we build

**原文标题**: We should be more ambitious with the software we build

**原文链接**: [https://danluu.com/ambitious/](https://danluu.com/ambitious/)

生成摘要时出错

---

## 100. The Exponential Time Hypothesis Is False [pdf]

**原文标题**: The Exponential Time Hypothesis Is False [pdf]

**原文链接**: [https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf](https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf)

生成摘要时出错

---

