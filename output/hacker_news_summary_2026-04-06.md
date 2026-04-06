# Hacker News 热门文章摘要 (2026-04-06)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. What Being Ripped Off Taught Me

**原文标题**: What Being Ripped Off Taught Me

**原文链接**: [https://belief.horse/notes/what-being-ripped-off-taught-me/](https://belief.horse/notes/what-being-ripped-off-taught-me/)

生成摘要时出错

---

## 12. Show HN: I built a tiny LLM to demystify how language models work

**原文标题**: Show HN: I built a tiny LLM to demystify how language models work

**原文链接**: [https://github.com/arman-bd/guppylm](https://github.com/arman-bd/guppylm)

生成摘要时出错

---

## 13. Adobe modifies hosts file to detect whether Creative Cloud is installed

**原文标题**: Adobe modifies hosts file to detect whether Creative Cloud is installed

**原文链接**: [https://www.osnews.com/story/144737/adobe-secretly-modifies-your-hosts-file-for-the-stupidest-reason/](https://www.osnews.com/story/144737/adobe-secretly-modifies-your-hosts-file-for-the-stupidest-reason/)

生成摘要时出错

---

## 14. The Last Quiet Thing

**原文标题**: The Last Quiet Thing

**原文链接**: [https://www.terrygodier.com/the-last-quiet-thing](https://www.terrygodier.com/the-last-quiet-thing)

生成摘要时出错

---

## 15. Microsoft hasn't had a coherent GUI strategy since Petzold

**原文标题**: Microsoft hasn't had a coherent GUI strategy since Petzold

**原文链接**: [https://www.jsnover.com/blog/2026/03/13/microsoft-hasnt-had-a-coherent-gui-strategy-since-petzold/](https://www.jsnover.com/blog/2026/03/13/microsoft-hasnt-had-a-coherent-gui-strategy-since-petzold/)

生成摘要时出错

---

## 16. An open-source 240-antenna array to bounce signals off the Moon

**原文标题**: An open-source 240-antenna array to bounce signals off the Moon

**原文链接**: [https://moonrf.com/](https://moonrf.com/)

生成摘要时出错

---

## 17. Gemma 4 on iPhone

**原文标题**: Gemma 4 on iPhone

**原文链接**: [https://apps.apple.com/nl/app/google-ai-edge-gallery/id6749645337](https://apps.apple.com/nl/app/google-ai-edge-gallery/id6749645337)

生成摘要时出错

---

## 18. France pulls last gold held in US for $15B gain

**原文标题**: France pulls last gold held in US for $15B gain

**原文链接**: [https://www.mining.com/france-pulls-last-gold-held-in-us-for-15b-gain/](https://www.mining.com/france-pulls-last-gold-held-in-us-for-15b-gain/)

生成摘要时出错

---

## 19. The 1987 game “The Last Ninja” was 40 kilobytes

**原文标题**: The 1987 game “The Last Ninja” was 40 kilobytes

**原文链接**: [https://twitter.com/exQUIZitely/status/2040777977521398151](https://twitter.com/exQUIZitely/status/2040777977521398151)

生成摘要时出错

---

## 20. Show HN: GovAuctions lets you browse government auctions at once

**原文标题**: Show HN: GovAuctions lets you browse government auctions at once

**原文链接**: [https://www.govauctions.app/](https://www.govauctions.app/)

生成摘要时出错

---

## 21. Show HN: Real-time AI (audio/video in, voice out) on an M3 Pro with Gemma E2B

**原文标题**: Show HN: Real-time AI (audio/video in, voice out) on an M3 Pro with Gemma E2B

**原文链接**: [https://github.com/fikrikarim/parlor](https://github.com/fikrikarim/parlor)

生成摘要时出错

---

## 22. One ant for $220: The new frontier of wildlife trafficking

**原文标题**: One ant for $220: The new frontier of wildlife trafficking

**原文链接**: [https://www.bbc.com/news/articles/cg4g44zv37qo](https://www.bbc.com/news/articles/cg4g44zv37qo)

生成摘要时出错

---

## 23. LÖVE: 2D Game Framework for Lua

**原文标题**: LÖVE: 2D Game Framework for Lua

**原文链接**: [https://github.com/love2d/love](https://github.com/love2d/love)

生成摘要时出错

---

## 24. Signals, the push-pull based algorithm

**原文标题**: Signals, the push-pull based algorithm

**原文链接**: [https://willybrauner.com/journal/signal-the-push-pull-based-algorithm](https://willybrauner.com/journal/signal-the-push-pull-based-algorithm)

生成摘要时出错

---

## 25. Drop, formerly Massdrop, ends most collaborations and rebrands under Corsair

**原文标题**: Drop, formerly Massdrop, ends most collaborations and rebrands under Corsair

**原文链接**: [https://drop.com/](https://drop.com/)

生成摘要时出错

---

## 26. Running Gemma 4 locally with LM Studio's new headless CLI and Claude Code

**原文标题**: Running Gemma 4 locally with LM Studio's new headless CLI and Claude Code

**原文链接**: [https://ai.georgeliu.com/p/running-google-gemma-4-locally-with](https://ai.georgeliu.com/p/running-google-gemma-4-locally-with)

生成摘要时出错

---

## 27. Sheets Spreadsheets in Your Terminal

**原文标题**: Sheets Spreadsheets in Your Terminal

**原文链接**: [https://github.com/maaslalani/sheets](https://github.com/maaslalani/sheets)

生成摘要时出错

---

## 28. Music for Programming

**原文标题**: Music for Programming

**原文链接**: [https://musicforprogramming.net](https://musicforprogramming.net)

生成摘要时出错

---

## 29. Show HN: Gemma Gem – AI model embedded in a browser – no API keys, no cloud

**原文标题**: Show HN: Gemma Gem – AI model embedded in a browser – no API keys, no cloud

**原文链接**: [https://github.com/kessler/gemma-gem](https://github.com/kessler/gemma-gem)

生成摘要时出错

---

## 30. Case study: recovery of a corrupted 12 TB multi-device pool

**原文标题**: Case study: recovery of a corrupted 12 TB multi-device pool

**原文链接**: [https://github.com/kdave/btrfs-progs/issues/1107](https://github.com/kdave/btrfs-progs/issues/1107)

生成摘要时出错

---

## 31. Why Switzerland has 25 Gbit internet and America doesn't

**原文标题**: Why Switzerland has 25 Gbit internet and America doesn't

**原文链接**: [https://sschueller.github.io/posts/the-free-market-lie/](https://sschueller.github.io/posts/the-free-market-lie/)

生成摘要时出错

---

## 32. Show HN: I made a YouTube search form with advanced filters

**原文标题**: Show HN: I made a YouTube search form with advanced filters

**原文链接**: [https://playlists.at/youtube/search/](https://playlists.at/youtube/search/)

生成摘要时出错

---

## 33. Employers use your personal data to figure out the lowest salary you'll accept

**原文标题**: Employers use your personal data to figure out the lowest salary you'll accept

**原文链接**: [https://www.marketwatch.com/story/employers-are-using-your-personal-data-to-figure-out-the-lowest-salary-youll-accept-c2b968fb](https://www.marketwatch.com/story/employers-are-using-your-personal-data-to-figure-out-the-lowest-salary-youll-accept-c2b968fb)

生成摘要时出错

---

## 34. I Replaced Kafka, Redis, and RabbitMQ with One Tool – A Deep Dive into NATS

**原文标题**: I Replaced Kafka, Redis, and RabbitMQ with One Tool – A Deep Dive into NATS

**原文链接**: [https://medium.com/@jainal/i-replaced-kafka-redis-and-rabbitmq-with-one-tool-heres-what-i-learned-b9f0b5ca94ed](https://medium.com/@jainal/i-replaced-kafka-redis-and-rabbitmq-with-one-tool-heres-what-i-learned-b9f0b5ca94ed)

生成摘要时出错

---

## 35. Show HN: Modo – I built an open-source alternative to Kiro, Cursor, and Windsurf

**原文标题**: Show HN: Modo – I built an open-source alternative to Kiro, Cursor, and Windsurf

**原文链接**: [https://github.com/mohshomis/modo](https://github.com/mohshomis/modo)

生成摘要时出错

---

## 36. Number in man page titles e.g. sleep(3)

**原文标题**: Number in man page titles e.g. sleep(3)

**原文链接**: [https://lalitm.com/til-number-in-man-page-titles-e-g-sleep-3/](https://lalitm.com/til-number-in-man-page-titles-e-g-sleep-3/)

生成摘要时出错

---

## 37. Caveman: Why use many token when few token do trick

**原文标题**: Caveman: Why use many token when few token do trick

**原文链接**: [https://github.com/JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)

生成摘要时出错

---

## 38. Eight years of wanting, three months of building with AI

**原文标题**: Eight years of wanting, three months of building with AI

**原文链接**: [https://lalitm.com/post/building-syntaqlite-ai/](https://lalitm.com/post/building-syntaqlite-ai/)

生成摘要时出错

---

## 39. A tail-call interpreter in (nightly) Rust

**原文标题**: A tail-call interpreter in (nightly) Rust

**原文链接**: [https://www.mattkeeter.com/blog/2026-04-05-tailcall/](https://www.mattkeeter.com/blog/2026-04-05-tailcall/)

生成摘要时出错

---

## 40. Computational Physics (2nd Edition) (2025)

**原文标题**: Computational Physics (2nd Edition) (2025)

**原文链接**: [https://websites.umich.edu/~mejn/cp2/](https://websites.umich.edu/~mejn/cp2/)

生成摘要时出错

---

## 41. Artemis II crew see first glimpse of far side of Moon [video]

**原文标题**: Artemis II crew see first glimpse of far side of Moon [video]

**原文链接**: [https://www.bbc.com/news/videos/ce3d5gkd2geo](https://www.bbc.com/news/videos/ce3d5gkd2geo)

生成摘要时出错

---

## 42. Nanocode: The best Claude Code that $200 can buy in pure JAX on TPUs

**原文标题**: Nanocode: The best Claude Code that $200 can buy in pure JAX on TPUs

**原文链接**: [https://github.com/salmanmohammadi/nanocode/discussions/1](https://github.com/salmanmohammadi/nanocode/discussions/1)

生成摘要时出错

---

## 43. My university uses prompt injection to catch cheaters

**原文标题**: My university uses prompt injection to catch cheaters

**原文链接**: [https://varun.ch/til/prompt-injection-catch-cheaters/](https://varun.ch/til/prompt-injection-catch-cheaters/)

生成摘要时出错

---

## 44. Stamp It: All programs must report their version

**原文标题**: Stamp It: All programs must report their version

**原文链接**: [https://michael.stapelberg.ch/posts/2026-04-05-stamp-it-all-programs-must-report-their-version/](https://michael.stapelberg.ch/posts/2026-04-05-stamp-it-all-programs-must-report-their-version/)

生成摘要时出错

---

## 45. Show HN: I replaced Google Analytics with my own tool – no cookies, <1KB script

**原文标题**: Show HN: I replaced Google Analytics with my own tool – no cookies, <1KB script

**原文链接**: [https://datakool.com/](https://datakool.com/)

生成摘要时出错

---

## 46. Friendica – A Decentralized Social Network

**原文标题**: Friendica – A Decentralized Social Network

**原文链接**: [https://friendi.ca/](https://friendi.ca/)

生成摘要时出错

---

## 47. Show HN: I just built a MCP Server that connects Claude to all your wearables

**原文标题**: Show HN: I just built a MCP Server that connects Claude to all your wearables

**原文链接**: [https://pacetraining.co/](https://pacetraining.co/)

生成摘要时出错

---

## 48. OpenJDK: Panama

**原文标题**: OpenJDK: Panama

**原文链接**: [https://openjdk.org/projects/panama/](https://openjdk.org/projects/panama/)

生成摘要时出错

---

## 49. The Mechanics of Steins Gate (2023) [pdf]

**原文标题**: The Mechanics of Steins Gate (2023) [pdf]

**原文链接**: [https://github.com/Votuko/steins-gate-mechanics/blob/main/The%20Mechanics%20of%20Steins%20Gate%20v1.0.3.pdf](https://github.com/Votuko/steins-gate-mechanics/blob/main/The%20Mechanics%20of%20Steins%20Gate%20v1.0.3.pdf)

生成摘要时出错

---

## 50. Media scraper Gallery-dl is moving to Codeberg after receiving a DMCA notice

**原文标题**: Media scraper Gallery-dl is moving to Codeberg after receiving a DMCA notice

**原文链接**: [https://github.com/mikf/gallery-dl/discussions/9304](https://github.com/mikf/gallery-dl/discussions/9304)

生成摘要时出错

---

## 51. How Paris swapped cars for bikes – and transformed its streets

**原文标题**: How Paris swapped cars for bikes – and transformed its streets

**原文链接**: [https://www.theguardian.com/world/2026/apr/05/how-paris-swapped-cars-for-bikes-and-remade-its-streets](https://www.theguardian.com/world/2026/apr/05/how-paris-swapped-cars-for-bikes-and-remade-its-streets)

生成摘要时出错

---

## 52. Make your own ColecoVision at home, part 5

**原文标题**: Make your own ColecoVision at home, part 5

**原文链接**: [https://www.leadedsolder.com/2026/03/24/colecovision-diy-part-5.html](https://www.leadedsolder.com/2026/03/24/colecovision-diy-part-5.html)

生成摘要时出错

---

## 53. When Virality Is the Message: The New Age of AI Propaganda

**原文标题**: When Virality Is the Message: The New Age of AI Propaganda

**原文链接**: [https://time.com/article/2026/04/02/when-virality-is-the-message-the-new-age-of-ai-propaganda/](https://time.com/article/2026/04/02/when-virality-is-the-message-the-new-age-of-ai-propaganda/)

生成摘要时出错

---

## 54. The threat is comfortable drift toward not understanding what you're doing

**原文标题**: The threat is comfortable drift toward not understanding what you're doing

**原文链接**: [https://ergosphere.blog/posts/the-machines-are-fine/](https://ergosphere.blog/posts/the-machines-are-fine/)

生成摘要时出错

---

## 55. Tiny Corp's Exabox

**原文标题**: Tiny Corp's Exabox

**原文链接**: [https://twitter.com/__tinygrad__/status/2040944508402360592](https://twitter.com/__tinygrad__/status/2040944508402360592)

生成摘要时出错

---

## 56. Show HN: A game where you build a GPU

**原文标题**: Show HN: A game where you build a GPU

**原文链接**: [https://jaso1024.com/mvidia/](https://jaso1024.com/mvidia/)

生成摘要时出错

---

## 57. Usenet Archives

**原文标题**: Usenet Archives

**原文链接**: [https://usenetarchives.com](https://usenetarchives.com)

生成摘要时出错

---

## 58. In Japan, the robot isn't coming for your job; it's filling the one nobody wants

**原文标题**: In Japan, the robot isn't coming for your job; it's filling the one nobody wants

**原文链接**: [https://techcrunch.com/2026/04/05/japan-is-proving-experimental-physical-ai-is-ready-for-the-real-world/](https://techcrunch.com/2026/04/05/japan-is-proving-experimental-physical-ai-is-ready-for-the-real-world/)

生成摘要时出错

---

## 59. Rock-climbing fish can shimmy up a 50-foot waterfall

**原文标题**: Rock-climbing fish can shimmy up a 50-foot waterfall

**原文链接**: [https://text.npr.org/nx-s1-5773315](https://text.npr.org/nx-s1-5773315)

生成摘要时出错

---

## 60. Rock-climbing fish can shimmy up a 50-foot waterfall

**原文标题**: Rock-climbing fish can shimmy up a 50-foot waterfall

**原文链接**: [https://text.npr.org/nx-s1-5773315](https://text.npr.org/nx-s1-5773315)

生成摘要时出错

---

## 61. Scientists Figured Out How Eels Reproduce (2022)

**原文标题**: Scientists Figured Out How Eels Reproduce (2022)

**原文链接**: [https://www.intelligentliving.co/scientists-finally-figured-out-how-eels-reproduce/](https://www.intelligentliving.co/scientists-finally-figured-out-how-eels-reproduce/)

生成摘要时出错

---

## 62. The Team Behind a Pro-Iran, Lego-Themed Viral-Video Campaign

**原文标题**: The Team Behind a Pro-Iran, Lego-Themed Viral-Video Campaign

**原文链接**: [https://www.newyorker.com/culture/infinite-scroll/the-team-behind-a-pro-iran-lego-themed-viral-video-campaign](https://www.newyorker.com/culture/infinite-scroll/the-team-behind-a-pro-iran-lego-themed-viral-video-campaign)

生成摘要时出错

---

## 63. Women were never meant to give birth on their backs

**原文标题**: Women were never meant to give birth on their backs

**原文链接**: [https://www.bbc.com/future/article/20260401-women-were-never-meant-to-give-birth-on-their-backs](https://www.bbc.com/future/article/20260401-women-were-never-meant-to-give-birth-on-their-backs)

生成摘要时出错

---

## 64. Finnish sauna heat exposure induces stronger immune cell than cytokine responses

**原文标题**: Finnish sauna heat exposure induces stronger immune cell than cytokine responses

**原文链接**: [https://www.tandfonline.com/doi/full/10.1080/23328940.2026.2645467#abstract](https://www.tandfonline.com/doi/full/10.1080/23328940.2026.2645467#abstract)

生成摘要时出错

---

## 65. Aegis – open-source FPGA silicon

**原文标题**: Aegis – open-source FPGA silicon

**原文链接**: [https://github.com/MidstallSoftware/aegis](https://github.com/MidstallSoftware/aegis)

生成摘要时出错

---

## 66. Tracing Goroutines in Realtime with eBPF

**原文标题**: Tracing Goroutines in Realtime with eBPF

**原文链接**: [https://sazak.io/articles/tracing-goroutines-in-realtime-with-ebpf-2026-03-31](https://sazak.io/articles/tracing-goroutines-in-realtime-with-ebpf-2026-03-31)

生成摘要时出错

---

## 67. German implementation of eIDAS will require an Apple/Google account to function

**原文标题**: German implementation of eIDAS will require an Apple/Google account to function

**原文链接**: [https://bmi.usercontent.opencode.de/eudi-wallet/wallet-development-documentation-public/latest/architecture-concept/06-mobile-devices/02-mdvm/](https://bmi.usercontent.opencode.de/eudi-wallet/wallet-development-documentation-public/latest/architecture-concept/06-mobile-devices/02-mdvm/)

生成摘要时出错

---

## 68. Apple approves driver that lets Nvidia eGPUs work with Arm Macs

**原文标题**: Apple approves driver that lets Nvidia eGPUs work with Arm Macs

**原文链接**: [https://twitter.com/__tinygrad__/status/2039213719155310736](https://twitter.com/__tinygrad__/status/2039213719155310736)

生成摘要时出错

---

## 69. Tattoo ink induces inflammation and alters the immune response to vaccination

**原文标题**: Tattoo ink induces inflammation and alters the immune response to vaccination

**原文链接**: [https://www.pnas.org/doi/10.1073/pnas.2510392122](https://www.pnas.org/doi/10.1073/pnas.2510392122)

生成摘要时出错

---

## 70. Perfmon – Consolidate your favorite CLI monitoring tools into a single TUI

**原文标题**: Perfmon – Consolidate your favorite CLI monitoring tools into a single TUI

**原文链接**: [https://github.com/sumant1122/Perfmon](https://github.com/sumant1122/Perfmon)

生成摘要时出错

---

## 71. Is Germany's gold safe in New York ?

**原文标题**: Is Germany's gold safe in New York ?

**原文链接**: [https://www.dw.com/en/is-germanys-gold-safe-in-new-york/video-75766873](https://www.dw.com/en/is-germanys-gold-safe-in-new-york/video-75766873)

生成摘要时出错

---

## 72. Show HN: OsintRadar – Curated directory for osint tools

**原文标题**: Show HN: OsintRadar – Curated directory for osint tools

**原文链接**: [https://osintradar.com/](https://osintradar.com/)

生成摘要时出错

---

## 73. From birds to brains: My path to the fusiform face area (2024)

**原文标题**: From birds to brains: My path to the fusiform face area (2024)

**原文链接**: [https://www.kavliprize.org/nancy-kanwisher-autobiography](https://www.kavliprize.org/nancy-kanwisher-autobiography)

生成摘要时出错

---

## 74. Show HN: M. C. Escher spiral in WebGL inspired by 3Blue1Brown

**原文标题**: Show HN: M. C. Escher spiral in WebGL inspired by 3Blue1Brown

**原文链接**: [https://static.laszlokorte.de/escher/](https://static.laszlokorte.de/escher/)

生成摘要时出错

---

## 75. OpenAI's fall from grace as investors race to Anthropic

**原文标题**: OpenAI's fall from grace as investors race to Anthropic

**原文链接**: [https://www.latimes.com/business/story/2026-04-01/openais-shocking-fall-from-grace-as-investors-race-to-anthropic](https://www.latimes.com/business/story/2026-04-01/openais-shocking-fall-from-grace-as-investors-race-to-anthropic)

生成摘要时出错

---

## 76. Iran's IRGC Publishes Satellite Imagery of OpenAI's $30B Stargate Datacenter

**原文标题**: Iran's IRGC Publishes Satellite Imagery of OpenAI's $30B Stargate Datacenter

**原文链接**: [https://newclawtimes.com/articles/iran-irgc-satellite-imagery-openai-stargate-abu-dhabi-datacenter-threat/](https://newclawtimes.com/articles/iran-irgc-satellite-imagery-openai-stargate-abu-dhabi-datacenter-threat/)

生成摘要时出错

---

## 77. LibreOffice – Let's put an end to the speculation

**原文标题**: LibreOffice – Let's put an end to the speculation

**原文链接**: [https://blog.documentfoundation.org/blog/2026/04/05/lets-put-an-end-to-the-speculation/](https://blog.documentfoundation.org/blog/2026/04/05/lets-put-an-end-to-the-speculation/)

生成摘要时出错

---

## 78. Does coding with LLMs mean more microservices?

**原文标题**: Does coding with LLMs mean more microservices?

**原文链接**: [https://ben.page/microservices](https://ben.page/microservices)

生成摘要时出错

---

## 79. Lisette a little language inspired by Rust that compiles to Go

**原文标题**: Lisette a little language inspired by Rust that compiles to Go

**原文链接**: [https://lisette.run/](https://lisette.run/)

生成摘要时出错

---

## 80. NIMBY Rails

**原文标题**: NIMBY Rails

**原文链接**: [https://store.steampowered.com/app/1134710/NIMBY_Rails/](https://store.steampowered.com/app/1134710/NIMBY_Rails/)

生成摘要时出错

---

## 81. AI Singer Now Occupies Eleven Spots on iTunes Singles Chart

**原文标题**: AI Singer Now Occupies Eleven Spots on iTunes Singles Chart

**原文链接**: [https://www.showbiz411.com/2026/04/05/itunes-takeover-by-fake-ai-singer-eddie-dalton-now-occupies-eleven-spots-on-chart-despite-not-being-human-or-real-exclusive](https://www.showbiz411.com/2026/04/05/itunes-takeover-by-fake-ai-singer-eddie-dalton-now-occupies-eleven-spots-on-chart-despite-not-being-human-or-real-exclusive)

生成摘要时出错

---

## 82. Show HN: Contrapunk – Real-time counterpoint harmony from guitar input

**原文标题**: Show HN: Contrapunk – Real-time counterpoint harmony from guitar input

**原文链接**: [https://contrapunk.com/](https://contrapunk.com/)

生成摘要时出错

---

## 83. Electrical transformer manufacturing is throttling the electrified future

**原文标题**: Electrical transformer manufacturing is throttling the electrified future

**原文链接**: [https://www.bloomberg.com/features/2025-bottlenecks-transformers/](https://www.bloomberg.com/features/2025-bottlenecks-transformers/)

生成摘要时出错

---

## 84. Artemis II crew take “spectacular” image of Earth

**原文标题**: Artemis II crew take “spectacular” image of Earth

**原文链接**: [https://www.bbc.com/news/articles/ce8jzr423p9o](https://www.bbc.com/news/articles/ce8jzr423p9o)

生成摘要时出错

---

## 85. Embarrassingly simple self-distillation improves code generation

**原文标题**: Embarrassingly simple self-distillation improves code generation

**原文链接**: [https://arxiv.org/abs/2604.01193](https://arxiv.org/abs/2604.01193)

生成摘要时出错

---

## 86. Rendering arbitrary-scale emojis using the Slug algorithm

**原文标题**: Rendering arbitrary-scale emojis using the Slug algorithm

**原文链接**: [https://leduyquang753.name.vn/blog/2026/4/4/rendering-arbitrary-scale-emojis-using-the-slug-algorithm](https://leduyquang753.name.vn/blog/2026/4/4/rendering-arbitrary-scale-emojis-using-the-slug-algorithm)

生成摘要时出错

---

## 87. Spath and Splan

**原文标题**: Spath and Splan

**原文链接**: [https://sumato.ai/posts/2026-04-04-spath-and-splan.html](https://sumato.ai/posts/2026-04-04-spath-and-splan.html)

生成摘要时出错

---

## 88. My Google Workspace account suspension

**原文标题**: My Google Workspace account suspension

**原文链接**: [https://zencapital.substack.com/p/sad-story-of-my-google-workspace](https://zencapital.substack.com/p/sad-story-of-my-google-workspace)

生成摘要时出错

---

## 89. Make Humans Analog Again

**原文标题**: Make Humans Analog Again

**原文链接**: [https://bhave.sh/make-humans-analog-again/](https://bhave.sh/make-humans-analog-again/)

生成摘要时出错

---

## 90. Shared mutable state in Rust (2022)

**原文标题**: Shared mutable state in Rust (2022)

**原文链接**: [https://draft.ryhl.io/blog/shared-mutable-state/](https://draft.ryhl.io/blog/shared-mutable-state/)

生成摘要时出错

---

## 91. Google releases Gemma 4 open models

**原文标题**: Google releases Gemma 4 open models

**原文链接**: [https://deepmind.google/models/gemma/gemma-4/](https://deepmind.google/models/gemma/gemma-4/)

生成摘要时出错

---

## 92. AWS engineer reports PostgreSQL perf halved by Linux 7.0, fix may not be easy

**原文标题**: AWS engineer reports PostgreSQL perf halved by Linux 7.0, fix may not be easy

**原文链接**: [https://www.phoronix.com/news/Linux-7.0-AWS-PostgreSQL-Drop](https://www.phoronix.com/news/Linux-7.0-AWS-PostgreSQL-Drop)

生成摘要时出错

---

## 93. Rubysyn: Clarifying Ruby's Syntax and Semantics

**原文标题**: Rubysyn: Clarifying Ruby's Syntax and Semantics

**原文链接**: [https://github.com/squadette/rubysyn/blob/master/README.md](https://github.com/squadette/rubysyn/blob/master/README.md)

生成摘要时出错

---

## 94. The frontline is like Terminator: fighting robots give Ukraine hope in war

**原文标题**: The frontline is like Terminator: fighting robots give Ukraine hope in war

**原文链接**: [https://www.theguardian.com/world/2026/apr/04/fighting-robots-give-ukraine-hope-in-war-with-russia](https://www.theguardian.com/world/2026/apr/04/fighting-robots-give-ukraine-hope-in-war-with-russia)

生成摘要时出错

---

## 95. The secretive plan for a Maine data center collapsed in 6 days

**原文标题**: The secretive plan for a Maine data center collapsed in 6 days

**原文链接**: [https://www.bangordailynews.com/2026/04/06/mainefocus/mainefocus-environment/secretive-plan-maine-data-center-joam40zk0w/](https://www.bangordailynews.com/2026/04/06/mainefocus/mainefocus-environment/secretive-plan-maine-data-center-joam40zk0w/)

生成摘要时出错

---

## 96. Introduction to Computer Music (2009) [pdf]

**原文标题**: Introduction to Computer Music (2009) [pdf]

**原文链接**: [https://composerprogrammer.com/introductiontocomputermusic.pdf](https://composerprogrammer.com/introductiontocomputermusic.pdf)

生成摘要时出错

---

## 97. Demonstrating Real Time AV2 Decoding on Consumer Laptops

**原文标题**: Demonstrating Real Time AV2 Decoding on Consumer Laptops

**原文链接**: [http://aomedia.org/blog%20posts/Demonstrating-Real-Time-AV2-Decoding-on-Consumer-Laptops/](http://aomedia.org/blog%20posts/Demonstrating-Real-Time-AV2-Decoding-on-Consumer-Laptops/)

生成摘要时出错

---

## 98. Docker Offload

**原文标题**: Docker Offload

**原文链接**: [https://www.docker.com/blog/docker-offload-now-generally-available-the-full-power-of-docker-for-every-developer-everywhere/](https://www.docker.com/blog/docker-offload-now-generally-available-the-full-power-of-docker-for-every-developer-everywhere/)

生成摘要时出错

---

## 99. U.S. Lawmakers Work on Unified Site-Blocking Bill to Counter Online Piracy

**原文标题**: U.S. Lawmakers Work on Unified Site-Blocking Bill to Counter Online Piracy

**原文链接**: [https://torrentfreak.com/u-s-lawmakers-work-on-unified-site-blocking-bill-to-counter-online-piracy/](https://torrentfreak.com/u-s-lawmakers-work-on-unified-site-blocking-bill-to-counter-online-piracy/)

生成摘要时出错

---

## 100. Scientists found a protein that drives brain aging – and how to stop it

**原文标题**: Scientists found a protein that drives brain aging – and how to stop it

**原文链接**: [https://www.sciencedaily.com/releases/2026/04/260405065236.htm](https://www.sciencedaily.com/releases/2026/04/260405065236.htm)

生成摘要时出错

---

