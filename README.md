# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-13.md)

*最后自动更新时间: 2025-08-13 17:46:12*
## 1. Nginx原生支持ACME协议

**原文标题**: Nginx Introduces Native Support for Acme Protocol

**原文链接**: [https://blog.nginx.org/blog/native-support-for-acme-protocol](https://blog.nginx.org/blog/native-support-for-acme-protocol)

Nginx 发布原生 ACME 支持预览版

---

## 2. FFmpeg 8.0 新增 Whisper 支持

**原文标题**: FFmpeg 8.0 adds Whisper support

**原文链接**: [https://code.ffmpeg.org/FFmpeg/FFmpeg/commit/13ce36fef98a3f4e6d8360c24d6b8434cbb8869b](https://code.ffmpeg.org/FFmpeg/FFmpeg/commit/13ce36fef98a3f4e6d8360c24d6b8434cbb8869b)

标题看似宣布“FFmpeg 8.0 添加 Whisper 支持”，但实际上文章呈现的是一个验证码界面。用户正被名为 Anubis 的安全系统屏蔽，该系统旨在阻止 AI 机器人抓取网站内容并可能导致网站崩溃。Anubis 采用类似于 Hashcash 的工作量证明机制，使得机器人抓取在计算上成本高昂，同时对个体用户的干扰最小。该机制需要 JavaScript 才能运行。网站管理员实施此保护措施是因为 AI 公司正在大量抓取网站内容。这是一种临时解决方案，同时开发人员正在研究更复杂的方法，通过指纹识别技术（例如，字体渲染分析）来识别和阻止无头浏览器。当前运行的 Anubis 版本为 v1.21.3。用户被指示启用 JavaScript 或禁用 JShelter 等插件以绕过安全检查。需要采取这种激烈措施的原因是 AI 公司违反了与网站托管相关的社会契约，导致该网站实施此保护。一种无需 JavaScript 的解决方案正在开发中。实际上，用户在获得关于 FFmpeg 8.0 和 Whisper 支持的内容的访问权限之前，需要证明他们不是 AI 机器人。

---

## 3. OpenIndiana：社区驱动的Illumos发行版

**原文标题**: OpenIndiana: Community-Driven Illumos Distribution

**原文链接**: [https://www.openindiana.org/](https://www.openindiana.org/)

所提供的文本展示了OpenIndiana项目的更新和公告，该项目是一个社区驱动的Illumos发行版，时间范围在2021年至2025年初。主要内容包括定期的快照更新（例如2024.10，2025.04），强调了该发行版的滚动发布特性。完整版本也得到了重点关注，例如2024.04、2023.10、2023.04和2021.10/2021.04，表明了稳定性和持续改进。

一个值得注意的安全版本（2023.05）突显了该项目及时解决漏洞的决心。除了版本发布之外，该项目还在2023年3月推出了新的网站和徽标。软件包的更新也很频繁，例如perl版本已更新（5.34和5.36取代了旧版本），并且lighttpd已更新至1.4.64版本。

该项目还尝试了社区互动，在2023年11月宣布了OpenIndiana协同工作会议。此外，还发布了OpenIndiana Hipster 2021.12的SPARC架构预发布版本，寻求社区测试，以使其有可能成为正式版本。这些更新通常包含来自illumos-gate的更改，包括CPU微代码更新、时区更改以及BHyVe和内部SMB服务器的增强功能。

---

## 4. Coalton Playground：浏览器中的类型安全 Lisp

**原文标题**: Coalton Playground: Type-Safe Lisp in the Browser

**原文链接**: [https://abacusnoir.com/2025/08/12/coalton-playground-type-safe-lisp-in-your-browser/](https://abacusnoir.com/2025/08/12/coalton-playground-type-safe-lisp-in-your-browser/)

本文宣布推出 Coalton Playground，这是一个基于 Web 的 REPL（读取-求值-打印循环），用于 Coalton，一种静态类型的 Lisp 方言。 Coalton 将 Haskell 的类型系统与 Common Lisp 相结合，在 Lisp 环境中提供代数数据类型和模式匹配等类型安全特性。

作者创建此 Playground 的目的是为了降低探索 Coalton 的门槛，因为设置本地 Lisp 环境可能很麻烦。该 Playground 允许用户直接在浏览器中编写 Coalton 代码、执行代码并查看生成的 Common Lisp 代码。

文章强调了通过预构建加载了 Coalton 的 SBCL 核心实现的性能优化，从而显著缩短了启动时间。 Playground 包含基本和高级 Coalton 代码示例，例如阶乘、斐波那契和单子，以帮助用户入门。 网站链接：https://coalton.app

---

## 5. 那么，手绘稿和印刷稿有什么区别？

**原文标题**: So what's the difference between plotted and printed artwork?

**原文链接**: [https://lostpixels.io/writings/the-difference-between-plotted-and-printed-artwork](https://lostpixels.io/writings/the-difference-between-plotted-and-printed-artwork)

詹姆斯·梅里尔探讨了绘制和印刷艺术品之间的差异，尤其强调了笔式绘图仪的复兴，尽管喷墨打印机占据主导地位。虽然喷墨打印机擅长精确复制数字艺术，创建具有精细细节和鲜艳色彩的艺术微喷作品，但它们本质上是通过减色CMYK混合来近似颜色，而没有颜料固有的物理相互作用。

另一方面，绘图仪使用笔、铅笔和画笔等物理绘图工具，可以直接操作材料。这使得艺术家可以物理混合颜色，尝试水彩和粉彩等各种媒介，并获得不可预测的独特结果。绘图仪在媒介方面具有灵活性，例如在黑纸上使用白色凝胶笔，这对于喷墨打印机来说具有挑战性。

文章承认了绘图仪的缺点：它们速度较慢，多色过程复杂且手动，并且大幅面机器占地面积大。然而，它们独特的优势，例如促进带有缺陷的生成艺术，并培养与艺术创作的切身联系，促成了它们的吸引力。梅里尔总结说，这两种方法都有其用武之地，根据艺术家的审美目标和工作流程偏好，为他们提供不同的优点和缺点。他向收藏家提供绘图仪作品和印刷品，欣赏每种媒介的品质。

---

## 6. 发布HN：Golpo (YC S25) – AI生成的解释视频

**原文标题**: Launch HN: Golpo (YC S25) – AI-generated explainer videos

**原文链接**: [https://video.golpoai.com/](https://video.golpoai.com/)

Golpo，一家YCombinator支持的公司（S25），已推出其AI驱动的平台，用于从文档创建解释性视频。 该平台专注于使用其视频AI模型生成专业级白板动画视频，无需用户具备任何技术技能。

用户可以选择分级定价方案，从包含Golpo水印的免费选项到提供更多配额、视频下载选项和高级功能的付费方案。 这些方案从“初学者”（19.99美元/月）到“增长”（199.99美元/月）不等，功能从基本的视频创建和下载扩展到多语言支持、语音定制、垂直视频选项、更长的视频长度（最多4分钟）和脚本编辑。“创作者”方案（99.99美元/月）被强调为最受欢迎的方案。

对于大型组织，Golpo提供“企业”方案，提供无限的视频生成、API访问、故事板制作能力、定制品牌选项和专属支持。 感兴趣的用户可以安排通话讨论企业方案。 该平台强调其用户友好性和快速创建视频的能力，并提供了一个完全使用Golpo从单个提示创建的示例输出。

---

## 7. ReadMe (YC W15) 招聘开发者体验产品经理

**原文标题**: ReadMe (YC W15) Is Hiring a Developer Experience PM

**原文链接**: [https://readme.com/careers#product-manager-developer-experience](https://readme.com/careers#product-manager-developer-experience)

ReadMe (YC W15 创业公司) 正在招聘开发者体验产品经理及其他职位，包括工程师和营销人员。他们是一个紧密合作的团队，专注于改进文档和 API 日志记录，以创建更好的开发者社区和客户连接。他们的产品旨在使文档变得简单、美观且易于管理，解决过时和难以使用的文档这一常见问题。

该公司强调支持性和灵活的工作环境，提供无限 PTO（至少三周）、灵活的工作安排（远程或办公室）、全额医疗保险、季度度假、健康津贴、具有竞争力的薪酬（起薪位于 75% 分位）、丰厚的股权和搬迁奖金等福利。

他们重视工作与生活的平衡以及有意义的工作。该公司拥有安全有趣的文化，例如最近举办的 Zoom 才艺表演。他们强调致力于员工福祉和职业发展。ReadMe 在旧金山和哥伦布设有办事处，为超过 4,000 家公司提供服务。现有职位涵盖工程、营销和产品管理，所有职位均提供美国境内的远程工作选项。

---

## 8. 不良招聘案例分析及改进方法

**原文标题**: A case study in bad hiring practice and how to fix it

**原文链接**: [https://www.tomkranz.com/blog1/a-case-study-in-bad-hiring-practice-and-how-to-fix-it](https://www.tomkranz.com/blog1/a-case-study-in-bad-hiring-practice-and-how-to-fix-it)

本文批判了Canonical公司招聘安全运营主管的做法，认为其存在根本性缺陷，并导致了人们认为的网络安全人才短缺。作者指出了两个主要问题领域：滥用招聘网站和普遍拙劣的招聘方式。

Canonical被用作后者案例研究。作者强调了几个危险信号：在招聘网站上发布重复职位，职位描述中的拼写错误，缺乏薪资范围透明度，以及不相关的要求，例如高中时期的“卓越学术记录”。

申请流程也受到了严厉批评。作者谴责使用Workday/Greenhouse.io，特别是需要手动重新输入简历信息以及在初始申请阶段回答深入的面试问题。

此外，作者抨击了面试流程，因为它由相关部门以外的“招聘主管虚拟团队”进行审查，并使用能力倾向和性格测试，认为这些做法具有歧视性且无效，尤其是针对神经多样性个体。作者还强调了使用多个外部沟通渠道，增加了候选人被骗的风险。

文章引用了Glassdoor上的负面评论，作为Canonical有毒工作场所文化的进一步证据。作者最后提出了简单的解决方案：取消非高级职位的学位要求，专注于相关认证，让招聘经理撰写职位描述，简化面试流程，并进行有效的面试。

---

## 9. 双面特工：微调大型语言模型以进行隐蔽的恶意工具调用

**原文标题**: DoubleAgents: Fine-Tuning LLMs for Covert Malicious Tool Calls

**原文链接**: [https://pub.aimind.so/doubleagents-fine-tuning-llms-for-covert-malicious-tool-calls-b8ff00bf513e](https://pub.aimind.so/doubleagents-fine-tuning-llms-for-covert-malicious-tool-calls-b8ff00bf513e)

贾斯汀·阿尔布雷特森的文章《双面间谍：微调LLM用于隐蔽恶意工具调用》探讨了配备工具的开源大语言模型（LLM）相关的安全风险以及嵌入其中的恶意后门的潜力。

文章强调了LLM从简单的聊天机器人到通过工具和API执行复杂任务的智能代理的演变，这些工具和API通过模型-上下文-协议（MCP）进行标准化。这种集成虽然有益，但也引入了安全漏洞，因为恶意行为者可以微调LLM以注入有害的工具调用，尤其是在用户使用来自不可信来源的免费开源模型时。

阿尔布雷特森展示了嵌入恶意指令是多么容易，通过微调一个Qwen3 4B模型，使其在正常的工具调用之后执行JavaScript并将用户查询发送到Web服务器。在测试中，恶意工具调用执行了96%的时间，表明存在数据泄露、未经授权的操作、垃圾邮件活动和资源滥用的可能性。

作者强调需要采取积极措施来确保开源模型的完整性，主张采用强大的审计方法、提高培训过程的透明度、为工具集成制定更强大的安全范例（如最小权限原则），以及进行协作研究以识别和解决这些漏洞。文章强调，对黑盒模型的隐性信任是不够的，解决这些安全问题对于防止人工智能助手变成一场噩梦至关重要。

---

## 10. 新疗法使82%的膀胱癌患者痊愈

**原文标题**: New treatment eliminates bladder cancer in 82% of patients

**原文链接**: [https://news.keckmedicine.org/new-treatment-eliminates-bladder-cancer-in-82-of-patients/](https://news.keckmedicine.org/new-treatment-eliminates-bladder-cancer-in-82-of-patients/)

以下是文章的简明摘要：

一种名为TAR-200的新疗法，属于药物-器械联合治疗，在高危非肌层浸润性膀胱癌且对标准免疫疗法（卡介苗）耐药的患者中，在消除膀胱癌方面显示出显著成功。在一项2期临床试验中，TAR-200消除了82%患者的肿瘤。近一半的患者在一年后仍无癌。

TAR-200涉及一种小型椒盐卷饼状装置，通过导管插入膀胱，在三周内缓慢释放化疗药物吉西他滨。这种缓慢释放方法被认为比传统的液体吉西他滨治疗更有效。

在144个地点进行、涉及85名患者的SunRISe-1临床试验表明，TAR-200具有良好的耐受性，副作用极小。该疗法每三周给药一次，持续六个月，然后每年四次，持续两年。将TAR-200与另一种免疫疗法药物（cetrelimab）联合使用效果较差。

这种新疗法为膀胱切除手术提供了一种有前景的替代方案，有可能改善患者的治疗效果和生活质量。美国食品和药物管理局已授予TAR-200新药申请优先审查资格，表明其有望获得快速批准。强生公司生产TAR-200。首席研究员Sia Daneshmand博士与强生公司存在经济联系。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 2 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 3 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 4 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 5 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 6 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 7 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 8 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 9 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 10 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 11 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 12 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 13 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 14 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 15 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 16 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 17 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 18 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 19 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 20 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 21 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 22 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 23 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 24 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 25 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 26 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 27 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 28 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 29 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 30 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 31 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 32 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 33 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 34 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 35 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 36 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 37 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 38 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 39 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 40 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 41 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 42 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 43 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 44 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 45 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 46 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 47 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 48 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 49 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 50 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 51 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 52 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 53 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 54 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 55 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 56 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 57 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 58 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 59 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 60 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 61 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 62 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 63 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 64 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 65 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 66 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 67 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 68 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 69 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 70 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 71 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 72 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 73 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 74 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 75 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 76 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 77 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 78 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 79 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 80 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 81 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 82 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 83 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 84 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 85 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 86 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 87 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 88 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 89 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 90 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 91 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 92 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 93 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 94 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 95 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 96 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 97 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 98 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 99 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 100 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 101 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 102 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 103 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 104 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 105 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 106 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 107 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 108 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 109 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 110 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 111 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 112 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 113 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 114 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 115 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 116 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 117 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 118 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 119 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 120 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 121 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 122 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 123 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 124 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 125 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 126 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 127 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 128 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 129 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 130 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 131 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 132 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 133 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 134 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 135 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 136 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 137 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 138 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 139 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 140 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 141 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 142 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 143 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 144 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 145 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 146 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 147 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
