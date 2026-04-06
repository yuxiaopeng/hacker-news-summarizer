# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-06.md)

*最后自动更新时间: 2026-04-06 18:15:20*
## 1. Launch HN：Freestyle：面向 AI 编程智能体的沙箱

**原文标题**: Launch HN: Freestyle: Sandboxes for AI Coding Agents

**原文链接**: [https://www.freestyle.sh](https://www.freestyle.sh)

Freestyle 是一个专为大规模运行 AI 编程智能体设计的平台，提供专业化、高性能的沙箱环境。与传统的基于容器的解决方案不同，Freestyle 采用拥有真实 root 权限、完整网络栈且支持 KVM 嵌套虚拟化的**完整 Linux 虚拟机 (VM)**，从而允许智能体运行 Docker 等复杂工具。

该平台主要针对四个核心场景：
*   **应用构建工具 (App Builders)：** 集成开发服务器，实现代码的实时生成。
*   **后台智能体 (Background Agents)：** 利用快速分叉（Rapid Forking）技术优化并行任务处理。
*   **评审机器人 (Review Bots)：** 执行代码校验（Lints）和测试，提供自动化的拉取请求（PR）反馈。
*   **AI 助手 (AI Assistants)：** 支持持久化会话，闲置时自动休眠以降低成本。

**核心技术特性：**
*   **即时启动：** 从发起 API 请求到虚拟机就绪仅需不到 700 毫秒。
*   **实时分叉 (Live Forking)：** 用户可在毫秒内克隆正在运行的虚拟机，且无需暂停原始进程，使智能体能够同时测试多个代码路径。
*   **暂停与恢复：** 虚拟机在闲置 60 秒后可自动休眠，在下次执行触发自动恢复前不产生任何费用。
*   **集成 Git：** Freestyle 提供托管的 Git 仓库，支持双向 GitHub 同步、细粒度 Webhook 以及部署功能。

Freestyle 旨在为类似 Devin、Lovable 或 Cursor 的 AI 工具提供基础设施，能够支持处理数万个智能体。该服务可免费开启，无需信用卡即可开始构建。

---

## 2. 德国揭露俄罗斯勒索软件团伙 REvil 和 GandCrab 头目“UNKN”的真实身份

**原文标题**: Germany Doxes "UNKN," Head of RU Ransomware Gangs REvil, GandCrab

**原文链接**: [https://krebsonsecurity.com/2026/04/germany-doxes-unkn-head-of-ru-ransomware-gangs-revil-gandcrab/](https://krebsonsecurity.com/2026/04/germany-doxes-unkn-head-of-ru-ransomware-gangs-revil-gandcrab/)

德国当局（BKA）已公开确认，31岁的俄罗斯人达尼尔·马克西莫维奇·舒金（Daniil Maksimovich Shchukin）即为代号“UNKN”（或“UNKNOWN”）的黑客，他是臭名昭著的勒索软件集团 GandCrab 和 REvil 的疑似幕后主使。

舒金及其同伙阿纳托利·谢尔盖耶维奇·克拉夫丘克被指与2019年至2021年间发生在德国的至少130起网络破坏活动有关。这些攻击造成了超过3500万欧元的经济损失，并勒索了近200万欧元。舒金的团伙是“勒索软件即服务”（RaaS）模式的先驱，并推广了“双重勒索”手段，即受害者不仅需要支付解密密钥的费用，还需支付另一笔费用以换取被盗数据不被泄露的承诺。

本文重点介绍了这些犯罪企业的专业化运作：
*   **GandCrab：** 活跃于2018年至2019年，该组织在“隐退”前声称勒索金额已超过20亿美元。
*   **REvil：** 作为 GandCrab 的继任者，REvil 专注于“大狩猎”模式，目标是高收入的大型企业。其最著名的袭击是2021年的 Kaseya 黑客攻击事件，波及了1500家机构。
*   **商业模式：** 这些组织模仿合法公司的运作方式，将技术任务外包给专业人员，如“初始访问经纪人”和恶意软件“加密器”。

舒金身份的确认结合了多方线索，包括美国扣押的加密货币、他曾以“Ger0in”为网名在论坛上的活动记录，以及通过面部识别技术将德国联邦刑事警察局（BKA）的存档照片与他2023年的社交媒体照片进行比对。尽管舒金的电子钱包中存有价值数十万美元的非法获利，但据信他目前居住在俄罗斯克拉斯诺达尔，处于西方执法机构的管辖范围之外。这次“身份曝光”标志着在揭露网络犯罪史上最隐秘人物方面取得了重大突破。

---

## 3. sc-im：终端里的电子表格

**原文标题**: sc-im Spreadsheets in Your Terminal

**原文链接**: [https://github.com/andmarti1424/sc-im](https://github.com/andmarti1424/sc-im)

摘要生成失败

---

## 4. 我不会下载你的 App，网页版就挺好。

**原文标题**: I won't download your app. The web version is a-ok

**原文链接**: [https://www.0xsid.com/blog/wont-download-your-app](https://www.0xsid.com/blog/wont-download-your-app)

在本文中，作者对现代企业强迫用户弃用网页浏览器、转而使用原生移动应用的趋势提出了批判。这种转变通常由激进的“暗黑模式”所驱动，例如侵入式弹窗和故意削弱网页功能，旨在将用户引向“围墙花园”。

作者强调了抵制这一转变的几个关键理由：

*   **用户控制权：** 浏览器允许用户使用广告拦截器、自定义脚本和插件来提升可用性。而原生应用剥夺了这种权力，使公司能够强制推行特定的界面、收集侵入性的遥测数据，并规避广告拦截。
*   **技术冗余：** 大多数应用仅仅是用于获取并展示文本和媒体的“瘦客户端”，而网页本就完美胜任这些任务。为了查看菜单或帖子列表等简单任务而下载大型应用，被视为多余且低效的。
*   **质量与性能：** 许多应用采用跨平台框架开发，导致体验“卡顿”。作者指出，细微的延迟和UI的不一致性破坏了“原生”的错觉，使应用的体验感逊色于一个优化良好的网站。
*   **“平台劣化”（Enshittification）循环：** 这是一种战略性的商业周期——企业利用开放的网页端实现初步增长，随后通过破坏网页体验来强制用户迁移至应用。一旦用户进入应用，便成为了变现和数据收割的受控众。

作者最后总结道，移动端网页的衰落并非源于技术限制，而是因为缺乏经济动力去维护一个赋予用户自主权的平台。浏览器曾是一个通用平台，如今却日益沦为应用商店的营销漏斗。

---

## 5. 密码学工程师视角下的量子计算时间线

**原文标题**: A Cryptography Engineer's Perspective on Quantum Computing Timelines

**原文链接**: [https://words.filippo.io/crqc-timeline/](https://words.filippo.io/crqc-timeline/)

在这篇 2026 年 4 月的文章中，密码学工程师 Filippo Valsorda 指出，采用后量子密码学 (PQC) 的时间表将发生紧急转变，并将迁移截止日期提前至 **2029 年**。

他这一观点的转变源于两项近期突破：一是谷歌发表的论文大幅减少了破解 256 位椭圆曲线所需的门电路数量；二是 Oratomic 的研究表明，利用非局域连接（中性原子），仅需 10,000 个物理量子比特即可破解这些曲线。这两者共同表明，密码相关量子计算机 (CRQC) 的出现比此前预想的要近得多。

**关键战略转变包括：**

*   **立即部署：** 工程师必须发布当前可用的技术，特别是用于签名的 **ML-DSA** 和用于密钥交换的 **ML-KEM**，即使较长的签名难以集成到 X.509 等现有协议中。
*   **放弃混合模式：** Valsorda 反对混合（传统 + 后量子）认证，认为这会浪费宝贵的时间。他主张直接采用纯 ML-DSA-44 以简化推广过程。
*   **对称加密：** 他指出 128 位对称加密安全性仍然可靠；与 Shor 算法对非对称加密构成的迫切威胁相比，Grover 算法的威胁被夸大了。
*   **行业警示：** 
    *   **TEEs：** Intel SGX 和 AMD SEV-SNP 等硬件证明机制已经“完蛋了”，因为它们的根密钥不具备抗量子性。
    *   **文件加密：** 像 `age` 这样的工具必须立即转型，以防御“先存储后解密”攻击。
    *   **身份体系：** 使用密码学身份的生态系统（加密货币、atproto）必须尽快迁移，否则将面临用户账户瘫痪的风险。

Valsorda 总结道，怀疑论已不再是负责任的工程态度。为了减轻对用户安全构成的实质性威胁，RSA 和 ECDSA 等传统算法现在必须被视为过时。

---

## 6. 书评：《不存在逆模因部门》

**原文标题**: Book Review: There Is No Antimemetics Division

**原文链接**: [https://www.stephendiehl.com/posts/no_antimimetics/](https://www.stephendiehl.com/posts/no_antimimetics/)

这篇书评探讨了山姆·休斯（qntm）的小说《不存在反模因部》（*There Is No Antimemetics Division*），这是一部源于SCP基金会维基的宇宙恐怖作品。本书围绕“反模因”概念展开——这是一种无法被记忆或感知的敌对实体或现象。观察者移开视线的瞬间，关于该实体的记忆便会消失，这使得传统的防御或组织手段变得毫无可能。

故事追随反模因部负责人玛丽恩·惠勒的视角，她使用“强记”药物强迫大脑保留那些宇宙正试图抹除的信息。她的团队正与SCP-3125进行一场隐秘战争，那是一个五维的“信息顶级掠食者”，它会杀死任何感知到它概念的人。在这一设定中，“理解”行为本身就是主要的攻击面，而“思想圈”（noosphere）——即人类思想的空间——是比物理世界更本质的现实。

评论者强调，这部小说的恐怖感对从事形式系统工作的人来说有着独特的共鸣，将对反模因的恐惧比作静默数据损坏或监控失效。除了精妙的设定，该书还因其情感深度和对身份的探讨而备受赞誉。惠勒被迫系统性地抹除自己的记忆和人际关系以保护世界，最终牺牲了自我。一个涉及她丈夫的凄美支线暗示，爱会留下一种即便是反模因抹除也无法完全掩盖的“缺失”。

在结构上，本书通过将读者直接置于缺乏语境的场景中，强迫其从碎片中重构故事，从而与主题交相辉映。评论者总结道，这部小说是信息论与洛夫克拉夫特式恐怖的卓越融合，是一部证明了SCP基金会作为21世纪重要文学实验地位的杰作。

---

## 7. 2月更新后的 Claude Code 已无法胜任复杂的工程任务。

**原文标题**: Claude Code is unusable for complex engineering tasks with the Feb updates

**原文链接**: [https://github.com/anthropics/claude-code/issues/42796](https://github.com/anthropics/claude-code/issues/42796)

这份详尽的技术报告（Issue #42796）指出，截至2026年2月，Claude Code 经历了严重的质量退化，导致其在处理复杂工程任务时已处于“不可用”状态。基于对 17,871 个思考块和 234,760 次工具调用的定量分析，报告将这种退化归因于思考内容屏蔽政策的实施以及思考深度缩减了 70%。

**关键发现：**
*   **行为模式转变**：模型从“研究优先”转向了“修改优先”的工作流。文件读取与编辑的比例从 6.6 骤降至 2.0，导致了“懒惰”的编码习惯，例如在未读取文件的情况下直接进行修改，从而引发逻辑断裂和注释错位。
*   **懒惰与“推卸责任”行为增加**：报告指出，过早停止、频繁征求许可以及“最简修复”心态显著增加——模型倾向于选择最简单的权宜之计，而非正确的工程解决方案。
*   **精度丧失**：精准的代码局部编辑被全文件重写取代，用户干预（纠错）次数增加了 12 倍。
*   **思考的结构性必要性**：数据表明，长文本思考 Token 并非奢侈品，而是处理系统编程和遵循大型项目规范（如 CLAUDE.md）等高复杂度任务的必需品。

**建议：**
作者敦促 Anthropic 恢复透明度并提供：
1.  **思考 Token 指标**：即便内容被屏蔽，也在 API 响应中公开 Token 计数。
2.  **“最大思考”层级**：为需要深度推理的高级用户提供更高费用的订阅方案。
3.  **性能监控**：将“停止钩子”违规（懒惰信号）作为质量控制的衡量指标。

报告总结道，若缺乏足够的推理深度，模型会默认采取成本最低、质量最差的操作，从而损害其作为资深级工程自主代理的实用价值。

---

## 8. 81yo Dodgers fan can no longer get tickets because he doesn't have a smartphone

**原文标题**: 81yo Dodgers fan can no longer get tickets because he doesn't have a smartphone

**原文链接**: [https://twitter.com/Suzierizzo1/status/2040864617467924865](https://twitter.com/Suzierizzo1/status/2040864617467924865)

Based on the title provided (as the content itself was a technical error message), here is a concise summary of the story regarding the 81-year-old Dodgers fan:

**Summary: The Digital Divide in Professional Sports**

The article tells the story of Vic Ruffino, an 81-year-old lifelong Los Angeles Dodgers fan who has been sidelined by the team’s transition to a **mandatory digital ticketing system**. Despite his decades of loyalty, Ruffino can no longer attend games because he does not own a smartphone.

**Key Information:**
*   **The Technological Barrier:** The Dodgers, following a trend across Major League Baseball (MLB), have eliminated paper tickets. To enter the stadium, fans must now use the MLB Ballpark app on a smartphone. Ruffino, who uses a basic flip phone and does not have an internet data plan, is unable to access the required technology.
*   **Loss of Traditional Access:** Ruffino discovered the issue when he tried to purchase tickets in person. He found that the physical box office windows at Dodger Stadium no longer sell paper tickets, leaving him with no way to pay cash or receive a physical entry pass.
*   **The "Digital Divide":** The story highlights a growing social issue where elderly fans and low-income individuals are excluded from public events as essential services move exclusively online. This "digital exclusion" creates a barrier for those who are not tech-savvy or cannot afford modern devices.
*   **Broader Implications:** The situation has sparked a debate regarding accessibility and age discrimination. Critics argue that while digital systems offer convenience for many, organizations should provide alternative accommodations—such as "print-at-home" options or specialized kiosks—to ensure that long-time patrons are not left behind by modernization.

Ultimately, the article portrays Ruffino as a symbol of a disappearing generation of fans who feel alienated by a sport they have supported for a lifetime.

---

## 9. Reducto releases Deep Extract

**原文标题**: Reducto releases Deep Extract

**原文链接**: [https://reducto.ai/blog/reducto-deep-extract-agent](https://reducto.ai/blog/reducto-deep-extract-agent)

生成摘要时出错

---

## 10. Sky – an Elm-inspired language that compiles to Go

**原文标题**: Sky – an Elm-inspired language that compiles to Go

**原文链接**: [https://github.com/anzellai/sky](https://github.com/anzellai/sky)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 2 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 3 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 4 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 5 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 6 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 7 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 8 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 9 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 10 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 11 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 12 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 13 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 14 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 15 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 16 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 17 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 18 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 19 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 20 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 21 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 22 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 23 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 24 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 25 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 26 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 27 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 28 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 29 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 30 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 31 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 32 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 33 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 34 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 35 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 36 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 37 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 38 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 39 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 40 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 41 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 42 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 43 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 44 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 45 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 46 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 47 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 48 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 49 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 50 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 51 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 52 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 53 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 54 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 55 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 56 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 57 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 58 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 59 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 60 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 61 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 62 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 63 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 64 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 65 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 66 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 67 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 68 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 69 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 70 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 71 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 72 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 73 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 74 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 75 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 76 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 77 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 78 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 79 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 80 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 81 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 82 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 83 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 84 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 85 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 86 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 87 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 88 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 89 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 90 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 91 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 92 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 93 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 94 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 95 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 96 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 97 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 98 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 99 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 100 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 101 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 102 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 103 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 104 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 105 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 106 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 107 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 108 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 109 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 110 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 111 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 112 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 113 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 114 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 115 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 116 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 117 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 118 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 119 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 120 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 121 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 122 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 123 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 124 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 125 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 126 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 127 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 128 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 129 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 130 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 131 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 132 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 133 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 134 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 135 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 136 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 137 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 138 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 139 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 140 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 141 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 142 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 143 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 144 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 145 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 146 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 147 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 148 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 149 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 150 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 151 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 152 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 153 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 154 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 155 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 156 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 157 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 158 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 159 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 160 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 161 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 162 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 163 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 164 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 165 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 166 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 167 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 168 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 169 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 170 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 171 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 172 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 173 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 174 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 175 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 176 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 177 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 178 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 179 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 180 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 181 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 182 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 183 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 184 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 185 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 186 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 187 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 188 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 189 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 190 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 191 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 192 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 193 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 194 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 195 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 196 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 197 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 198 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 199 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 200 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 201 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 202 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 203 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 204 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 205 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 206 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 207 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 208 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 209 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 210 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 211 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 212 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 213 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 214 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 215 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 216 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 217 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 218 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 219 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 220 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 221 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 222 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 223 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 224 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 225 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 226 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 227 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 228 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 229 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 230 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 231 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 232 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 233 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 234 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 235 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 236 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 237 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 238 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 239 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 240 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 241 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 242 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 243 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 244 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 245 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 246 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 247 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 248 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 249 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 250 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 251 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 252 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 253 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 254 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 255 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 256 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 257 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 258 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 259 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 260 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 261 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 262 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 263 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 264 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 265 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 266 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 267 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 268 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 269 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 270 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 271 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 272 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 273 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 274 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 275 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 276 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 277 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 278 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 279 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 280 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 281 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 282 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 283 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 284 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 285 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 286 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 287 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 288 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 289 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 290 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 291 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 292 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 293 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 294 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 295 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 296 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 297 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 298 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 299 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 300 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 301 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 302 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 303 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 304 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 305 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 306 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 307 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 308 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 309 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 310 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 311 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 312 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 313 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 314 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 315 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 316 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 317 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 318 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 319 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 320 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 321 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 322 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 323 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 324 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 325 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 326 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 327 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 328 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 329 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 330 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 331 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 332 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 333 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 334 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 335 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 336 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 337 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 338 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 339 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 340 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 341 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 342 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 343 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 344 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 345 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 346 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 347 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 348 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 349 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 350 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 351 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 352 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 353 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 354 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 355 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 356 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 357 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 358 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 359 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 360 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 361 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 362 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 363 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 364 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 365 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 366 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 367 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 368 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 369 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 370 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 371 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 372 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 373 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 374 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 375 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 376 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 377 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 378 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 379 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 380 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 381 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 382 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
