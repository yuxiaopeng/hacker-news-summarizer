# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-02.md)

*最后自动更新时间: 2026-09-02 20:04:27*
## 1. Gemini 3.8 Flash 及 3.8 Flash Cyber

**原文标题**: Gemini 3.8 Flash and 3.8 Flash Cyber

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)

Google 宣布推出 **Gemini 3.8 Flash** 和 **Gemini 3.8 Flash Cyber**，这标志着其在短短六周内发布的第三个“Flash”版本。这些模型在保持与此前 3.7 Flash 相同的速度和低廉价格的同时，为智能体工作流（agentic workflows）和网络安全提供了下一代智能。

**Gemini 3.8 Flash** 是一款通用的主力模型，针对长周期编程和自主智能体进行了优化。它在复杂推理方面表现出色，在 DeepSWE v1.1（软件工程）和 Vals Finance Agent V2 等基准测试中超越了更大规模的前沿模型。该模型的一个核心特征是“勤奋”（diligence）；它通过执行更多推理步骤和迭代调用工具来“更努力地工作”，从而确保在法律和 STEM 等专业领域的准确性。

**Gemini 3.8 Flash Cyber** 是专为网络安全防御者量身定制的专业版本。它在自主漏洞发现和自动化修补方面展现了前沿级别的性能。在涵盖 20 种编程语言的内部测试中，其漏洞发现成功率达到 70%。谷歌已开始使用该模型保护自身代码，并指出其为 Chrome 提供的正确补丁数量是其他大型商业模型的 2.6 倍。

**安全与获取方式：**
两款模型都集成了针对 CBRN（化学、生物、放射性和核）风险的高级防护措施，并显著增强了对抗提示词注入的鲁棒性。
*   **Gemini 3.8 Flash** 现已通过 Gemini API、Google AI Studio 提供，并面向 Google AI Pro/Ultra 订阅用户开放。
*   **Gemini 3.8 Flash Cyber** 通过全新的 **Fairwind 计划**，仅限受信任的防御者使用，包括政府机构和关键基础设施运营商。

开发者还可以在 **Google Antigravity** 中利用这些模型，构建复杂的、由智能体主导的应用程序和 3D 可视化工具。

---

## 2. 谷歌避免广告技术业务被拆分

**原文标题**: Google avoids a breakup of its ad tech business

**原文链接**: [https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html](https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html)

无法访问文章链接。

---

## 3. 我可以选择不将我的输入或输出数据用于训练吗？

**原文标题**: Can I opt out of my input or output data being used for training?

**原文链接**: [https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training](https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training)

Mistral 允许用户选择退出，使其输入和输出数据（包括对话和上传的文档）不被用于模型训练。退出流程因所使用的平台而异：

*   **Vibe (Web)：** 个人和团队用户默认开启。如需退出，请前往管理面板中的 **Manage（管理）** 部分，选择 **Privacy（隐私）**，并关闭“Allow your interactions to be used to train our models（允许您的交互用于训练我们的模型）”开关。
*   **Vibe (企业版)：** 企业客户**默认退出**，该设置仅由管理员级别管理。
*   **移动应用 (iOS/Android)：** 用户可以通过访问 **Settings > Data & Account Controls（设置 > 数据和账户控制）** 并取消勾选“Enable data sharing（启用数据共享）”复选框来退出。
*   **Mistral Studio 和 API：** 为了防止 API 调用及相关数据被用于改进，用户必须前往管理面板中的 **Privacy（隐私）** 菜单，并关闭“Anonymous improvement data（匿名改进数据）”开关。

**关键信息：**
*   **独立开关：** 退出 Vibe 不会自动退出 API（反之亦然）。您必须分别为每项服务进行配置。
*   **文档：** 上传的文档被视为输入数据；选择退出可确保这些文档不会被用于改进 Mistral 的模型。
*   **生效：** 一旦确认退出，Mistral 将立即停止将您的数据用于训练目的。

---

## 4. 最大的暗物质探测器发现了一个奇特粒子。

**原文标题**: Biggest dark matter detector spots a single weird particle

**原文链接**: [https://www.science.org/content/article/world-s-biggest-dark-matter-detector-spots-single-weird-particle](https://www.science.org/content/article/world-s-biggest-dark-matter-detector-spots-single-weird-particle)

LUX-ZEPLIN (LZ) 实验是世界上最灵敏的暗物质探测器，位于南达科他州地下 1.5 公里处。该实验近日发布了迄今为止最详尽的研究结果。尽管发现暗物质的主要目标尚未实现，但探测器成功观测到了一个“奇异”且极其罕见的物理事件：氙-124 的双中微子双电子俘获。

这一过程涉及原子核同时吸收两个电子并释放两个中微子。这是物理学中所观测到的最罕见事件之一，其半衰期比宇宙的年龄还要长数万亿倍。对这一特定类型相互作用的成功探测，有力地证明了 LZ 探测器前所未有的灵敏度，以及它从背景辐射中区分微弱信号的能力。

该探测器利用 10 吨超纯液氙来寻找暗物质的主要候选者——弱相互作用有质量粒子 (WIMPs)。在过去 280 天收集的最新数据中，并未发现 WIMPs 的证据。然而，这一“零结果”在科学上具有重要意义；它使研究人员能够对 WIMPs 的性质设定全球最严苛的限制，从而有效地缩小了搜索范围，并排除了几种理论模型。

物理学家们依然保持乐观，因为 LZ 实验计划还将运行数年。氙-124 衰变的成功探测证明了该仪器的性能正处于巅峰状态。如果 WIMPs 确实存在于探测器目前的灵敏度范围内，LZ 将拥有率先发现它们的独特优势，从而有望解开现代宇宙学中最大的谜团之一。

---

## 5. 走出洞穴

**原文标题**: Exit the Cave

**原文链接**: [https://turtlespace.blog/p/exit-the-cave](https://turtlespace.blog/p/exit-the-cave)

在《走出洞穴》一文中，贾斯汀·安德森（Justin Andersun）反对将私下的“磨炼”——他称之为“洞穴”——浪漫化。安德森指出，尽管独自训练或钻研看似富有成效，但它往往只是一个舒适的泡沫，让我们沉溺于幻觉，从而逃避现实的残酷反馈。

安德森以自己高中摔跤手的经历为例，说明了他如何多年来误将努力当成进步。尽管经历了艰苦的体能训练和严格的减重，他在比赛中却屡屡落败。他最终意识到，虽然他掌控了“投入”（技术与体能），却缺乏获胜所需的“心志”。他是在“为了不输而摔跤”——其动力源于对羞辱的恐惧，而非对胜利的渴望。他将此定性为一种“看起来极像自律的怯懦”，即利用“洞穴”的安全性来保护自尊，使其免受公开失败的打击。

文章最后呼吁人们离开“洞穴”，去寻找“垫子”——一个公开接受考验的场所。安德森断言，无论是在创业、艺术还是人际关系中，真正的进步都要求步入“真实世界”，因为那里的结果是无法被掌控或隐匿的。他认为，与其在私下漫无目的地训练做一个“懦夫”，不如拿出勇气面对公开的失败。最终，一个人必须承担变得“脱胎换骨”的风险，而这种转变并非源于秘密的蜕变，而是源于发布产品、分享故事或勇敢去爱的无畏。

---

## 6. 温德尔·贝里逝世

**原文标题**: Wendell Berry has died

**原文链接**: [https://www.nytimes.com/2026/08/31/us/wendell-berry-dead.html](https://www.nytimes.com/2026/08/31/us/wendell-berry-dead.html)

无法访问文章链接。

---

## 7. 衰老的大脑会将记忆混淆，而不仅仅是遗忘。

**原文标题**: Aging Brains Blend Memories Together Instead of Just Forgetting Them

**原文链接**: [https://studyfinds.com/aging-brains-blend-memories-together-instead-of-forgetting-them-study-finds/](https://studyfinds.com/aging-brains-blend-memories-together-instead-of-forgetting-them-study-finds/)

Recent research published in *Cerebral Cortex* suggests that age-related memory decline is not caused by simple forgetfulness, but rather by a process where the brain "blends" unrelated memories together. 

Using MRI scans of adults aged 18 to 74, researchers monitored hippocampal activity during a task where participants paired faces with either objects or scenes. In younger adults, a high degree of similarity between brain activity during learning and recall predicted accurate memory. However, in older adults, this same overlap predicted a specific type of error called "category-level misbinding." Instead of replaying a specific memory faithfully, the older brain retrieved information too broadly, leading participants to confuse entirely different categories—such as mistaking a scene for an object.

The study found that memory accuracy drops sharply after young adulthood, with middle-aged and older adults performing at similarly lower levels. Interestingly, traditional explanations for memory loss—such as hippocampal shrinkage, baseline brain organization, or attention deficits—did not fully account for this shift toward blended memories. 

These findings indicate that as the brain ages, its memory "replay" mechanism changes from a precise "scalpel" to a "wide brush." Rather than losing storage capacity, the aging brain struggles with precision, stitching together scattered pieces of unrelated experiences into false connections. This distinction suggests that future cognitive treatments should focus on sharpening the brain’s ability to keep memories separate rather than just boosting general memory strength.

---

## 8. SteamdDB Joins Nexus Mods

**原文标题**: SteamdDB Joins Nexus Mods

**原文链接**: [https://www.nexusmods.com/news/15597](https://www.nexusmods.com/news/15597)

生成摘要时出错

---

## 9. Three sites made 215,128 “best software” pages for AI. Perplexity cites them

**原文标题**: Three sites made 215,128 “best software” pages for AI. Perplexity cites them

**原文链接**: [https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/)

生成摘要时出错

---

## 10. Commodore 64 released September 1, 1982

**原文标题**: Commodore 64 released September 1, 1982

**原文链接**: [https://dfarq.homeip.net/commodore-64-released-september-1-1982/](https://dfarq.homeip.net/commodore-64-released-september-1-1982/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 2 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 3 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 4 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 5 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 6 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 7 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 8 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 9 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 10 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 11 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 12 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 13 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 14 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 15 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 16 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 17 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 18 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 19 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 20 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 21 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 22 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 23 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 24 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 25 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 26 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 27 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 28 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 29 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 30 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 31 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 32 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 33 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 34 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 35 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 36 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 37 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 38 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 39 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 40 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 41 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 42 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 43 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 44 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 45 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 46 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 47 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 48 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 49 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 50 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 51 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 52 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 53 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 54 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 55 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 56 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 57 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 58 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 59 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 60 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 61 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 62 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 63 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 64 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 65 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 66 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 67 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 68 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 69 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 70 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 71 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 72 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 73 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 74 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 75 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 76 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 77 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 78 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 79 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 80 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 81 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 82 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 83 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 84 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 85 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 86 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 87 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 88 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 89 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 90 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 91 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 92 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 93 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 94 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 95 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 96 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 97 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 98 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 99 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 100 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 101 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 102 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 103 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 104 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 105 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 106 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 107 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 108 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 109 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 110 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 111 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 112 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 113 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 114 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 115 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 116 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 117 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 118 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 119 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 120 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 121 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 122 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 123 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 124 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 125 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 126 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 127 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 128 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 129 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 130 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 131 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 132 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 133 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 134 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 135 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 136 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 137 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 138 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 139 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 140 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 141 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 142 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 143 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 144 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 145 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 146 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 147 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 148 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 149 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 150 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 151 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 152 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 153 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 154 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 155 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 156 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 157 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 158 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 159 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 160 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 161 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 162 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 163 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 164 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 165 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 166 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 167 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 168 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 169 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 170 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 171 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 172 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 173 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 174 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 175 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 176 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 177 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 178 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 179 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 180 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 181 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 182 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 183 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 184 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 185 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 186 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 187 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 188 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 189 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 190 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 191 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 192 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 193 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 194 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 195 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 196 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 197 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 198 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 199 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 200 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 201 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 202 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 203 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 204 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 205 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 206 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 207 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 208 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 209 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 210 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 211 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 212 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 213 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 214 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 215 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 216 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 217 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 218 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 219 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 220 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 221 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 222 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 223 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 224 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 225 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 226 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 227 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 228 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 229 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 230 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 231 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 232 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 233 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 234 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 235 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 236 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 237 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 238 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 239 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 240 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 241 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 242 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 243 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 244 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 245 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 246 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 247 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 248 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 249 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 250 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 251 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 252 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 253 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 254 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 255 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 256 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 257 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 258 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 259 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 260 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 261 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 262 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 263 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 264 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 265 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 266 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 267 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 268 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 269 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 270 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 271 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 272 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 273 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 274 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 275 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 276 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 277 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 278 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 279 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 280 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 281 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 282 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 283 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 284 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 285 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 286 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 287 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 288 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 289 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 290 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 291 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 292 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 293 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 294 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 295 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 296 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 297 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 298 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 299 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 300 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 301 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 302 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 303 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 304 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 305 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 306 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 307 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 308 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 309 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 310 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 311 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 312 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 313 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 314 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 315 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 316 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 317 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 318 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 319 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 320 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 321 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 322 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 323 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 324 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 325 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 326 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 327 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 328 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 329 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 330 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 331 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 332 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 333 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 334 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 335 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 336 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 337 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 338 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 339 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 340 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 341 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 342 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 343 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 344 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 345 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 346 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 347 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 348 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 349 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 350 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 351 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 352 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 353 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 354 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 355 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 356 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 357 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 358 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 359 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 360 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 361 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 362 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 363 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 364 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 365 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 366 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 367 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 368 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 369 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 370 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 371 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 372 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 373 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 374 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 375 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 376 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 377 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 378 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 379 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 380 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 381 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 382 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 383 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 384 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 385 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 386 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 387 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 388 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 389 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 390 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 391 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 392 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 393 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 394 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 395 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 396 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 397 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 398 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 399 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 400 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 401 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 402 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 403 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 404 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 405 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 406 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 407 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 408 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 409 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 410 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 411 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 412 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 413 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 414 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 415 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 416 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 417 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 418 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 419 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 420 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 421 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 422 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 423 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 424 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 425 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 426 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 427 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 428 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 429 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 430 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 431 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 432 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 433 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 434 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 435 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 436 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 437 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 438 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 439 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 440 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 441 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 442 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 443 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 444 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 445 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 446 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 447 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 448 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 449 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 450 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 451 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 452 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 453 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 454 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 455 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 456 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 457 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 458 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 459 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 460 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 461 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 462 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 463 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 464 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 465 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 466 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 467 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 468 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 469 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 470 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 471 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 472 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 473 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 474 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 475 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 476 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 477 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 478 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 479 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 480 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 481 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 482 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 483 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 484 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 485 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 486 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 487 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 488 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 489 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 490 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 491 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 492 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 493 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 494 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 495 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 496 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 497 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 498 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 499 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 500 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 501 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 502 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 503 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 504 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 505 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 506 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 507 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 508 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 509 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 510 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 511 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 512 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 513 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 514 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 515 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 516 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 517 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 518 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 519 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 520 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 521 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 522 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 523 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 524 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 525 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 526 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 527 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 528 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 529 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
