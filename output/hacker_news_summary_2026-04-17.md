# Hacker News 热门文章摘要 (2026-04-17)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 克劳德设计

**原文标题**: Claude Design

**原文链接**: [https://www.anthropic.com/news/claude-design-anthropic-labs](https://www.anthropic.com/news/claude-design-anthropic-labs)

Anthropic 宣布推出 **Claude Design**，这是一款由 **Claude Opus 4.7** 视觉模型驱动的新型协作工具。该平台专为专业设计师和非专业人士（如创始人、营销人员）量身打造，通过对话式 AI 即可创作高质量的视觉作品，包括交互原型、线框图、路演 PPT 和营销素材。

核心功能与特性：
*   **品牌一致性：** Claude Design 可从代码库和文件中提取团队现有的设计系统，确保所有产出均自动遵循特定的品牌指南、配色和字体。
*   **交互式优化：** 用户可以通过自然语言、行内评论、直接编辑文本或使用自定义“调节旋钮”来实时调整布局和间距。
*   **多元输入方式：** 该工具支持文本提示词、上传文档（DOCX、PPTX、XLSX）以及网页截图，用于构建或复现现有的 UI 元素。
*   **无缝交付：** 与 **Claude Code** 的集成让用户能够打包设计方案以便快速落地。此外，它还与 **Canva** 达成深度合作，支持将草稿导出为可编辑的 Canva 设计，以及 PPTX、PDF 和 HTML 格式。
*   **团队协作：** 平台支持组织范围内的共享和群组对话，方便团队成员共同编辑并与 Claude 进行实时沟通。

Claude Design 目前正面向 Claude Pro、Max、Team 和 Enterprise 订阅用户开放**研究预览**。该功能正在逐步推行，企业级（Enterprise）管理员需在组织设置中手动开启此功能。

---

## 2. Claude Opus 4.7 每次会话的成本高出 20%–30%

**原文标题**: Claude Opus 4.7 costs 20–30% more per session

**原文链接**: [https://www.claudecodecamp.com/p/i-measured-claude-4-7-s-new-tokenizer-here-s-what-it-costs-you](https://www.claudecodecamp.com/p/i-measured-claude-4-7-s-new-tokenizer-here-s-what-it-costs-you)

本文分析了 **Claude Opus 4.7** 引入的新分词器对财务和性能的影响。尽管 Anthropic 维持了相同的单 Token 标价，但新分词器在处理相同文本时会产生明显更多的 Token，从而导致用户的实际成本增加。

**核心发现：**
*   **更高的 Token 比例：** 虽然 Anthropic 的官方文档建议 Token 数量会增加 1.0–1.35 倍，但针对技术内容和代码的实测显示，该比例高达 **1.45 至 1.47 倍**。英文文本和代码受影响最大，而中日韩（CJK）语言几乎保持不变。
*   **性能权衡：** 转向更小的 Token 单元似乎提升了模型对“字面指令的遵循能力”。在 IFEval 基准测试中，Opus 4.7 在严格指令遵循方面的表现比 4.6 版本提高了 **5 个百分点**。这可能是因为更小的 Token 迫使模型在格式和约束方面保持更细颗粒度的注意力。
*   **会话成本增加：** 对于典型的高频次“Claude Code”会话（约 80 轮），对话历史增长与提示词缓存的累积效应导致**总成本增加了 20–30%**。
*   **速率限制影响：** 对于使用“Max”方案的用户，更高的 Token 计数意味着上下文窗口消耗更快，即使不按 Token 计费，也会更早触发速率限制。

**结论：**
向 Claude 4.7 的过渡实际上起到了一种“Token 税”的作用。用户为精度和指令遵循能力的适度提升支付了约 30% 的额外会话成本。作者建议，在为英文和代码密集型工作负载制定预算时，用户应参考 Anthropic 预估范围的上限（1.35倍及以上）进行规划。

---

## 3. 艾萨克·阿西莫夫：最后的问题 (1956)

**原文标题**: Isaac Asimov: The Last Question (1956)

**原文链接**: [https://hex.ooo/library/last_question.html](https://hex.ooo/library/last_question.html)

生成摘要时出错

---

## 4. 初中生在柏林发现特洛伊古币

**原文标题**: Middle schooler finds coin from Troy in Berlin

**原文链接**: [https://www.thehistoryblog.com/archives/75848](https://www.thehistoryblog.com/archives/75848)

一名14岁的中学生卡斯帕（Caspar）在柏林最古老的广场——莫尔肯市集（Molkenmarkt）参加学生实习期间，有了一项非凡的考古发现。自2019年以来，该地块因重大重新开发一直处于考古挖掘中。在挖掘过程中，卡斯帕发现了一枚可追溯至公元前2世纪的稀有青铜硬币。

经史前史和早期史博物馆的专家分析，这枚硬币被确定源自伊利昂（Ilion），即古城特洛伊（位于今土耳其境内）。硬币正面是该城守护神雅典娜戴着头盔的头像，背面则刻有一头祭祀用的牛以及城市的名字。在伊利昂作为重要宗教和朝圣地的希腊化时期，这种货币十分常见。

这一发现在历史学上意义重大，因为它是柏林发现的首枚来自特洛伊的硬币。它为何会出现在柏林市中心的中世纪地层中至今仍是一个谜。虽然古代贸易路线跨越万里，但考古学家认为，这枚硬币更有可能是在晚得多的时期到达柏林的——或许是在18或19世纪作为纪念品或收藏品被带回，随后遗落在土壤之中。

这一发现凸显了莫尔肯市集挖掘工作的重要性，这些工作不断为柏林的最早历史提供新的见解。这枚硬币现在成为了古代安纳托利亚世界与中世纪德国城市发展之间的一条独特纽带。

---

## 5. NIST 停止对大多数 CVE 进行富化处理。

**原文标题**: NIST gives up enriching most CVEs

**原文链接**: [https://risky.biz/risky-bulletin-nist-gives-up-enriching-most-cves/](https://risky.biz/risky-bulletin-nist-gives-up-enriching-most-cves/)

In a major policy shift announced on April 15, 2026, the US National Institute of Standards and Technology (NIST) has officially ceased "enriching" the majority of vulnerabilities added to the National Vulnerability Database (NVD). Faced with a massive backlog of nearly 30,000 unenriched CVEs and significant budget cuts, NIST will now only provide detailed metadata for "important" vulnerabilities.

**The New Enrichment Criteria:**
NIST will focus its limited resources on three categories:
1.  Vulnerabilities listed in CISA’s Known Exploited Vulnerabilities (KEV) catalog.
2.  Software utilized by US federal agencies.
3.  "Critical software," including operating systems, browsers, VPNs, and security tools.

**Significant Policy Changes:**
NIST is also abandoning its practice of providing independent CVSS severity scores. Instead, the NVD will display the score assigned by the organization that originally issued the CVE. Experts warn this may lead to "infosec drama," as software vendors have a historical tendency to downplay the severity of their own security flaws to minimize reputational damage.

**Industry Impact:**
The decision marks the end of the NVD as a "single source of truth." Cybersecurity and vulnerability management firms that relied on NVD data must now find alternative sources or perform their own enrichment. NIST cited the explosion of "CVE chaff"—minor bugs in obscure libraries and IoT devices—and the anticipated surge of AI-discovered vulnerabilities as the primary drivers for this capitulation.

**Other Notable News:**
The bulletin also highlights that OpenAI has entered private testing for **GPT-5.4-Cyber**, a specialized model for defensive and offensive security work. Additionally, the report notes ongoing budget and staff cuts at CISA under the Trump administration, alongside a series of state-sponsored cyberattacks from Russian and North Korean actors targeting infrastructure and financial institutions.

---

## 6. 是时候禁止销售精确地理位置信息了。

**原文标题**: It Is Time to Ban the Sale of Precise Geolocation

**原文链接**: [https://www.lawfaremedia.org/article/it-is-time-to-ban-the-sale-of-precise-geolocation](https://www.lawfaremedia.org/article/it-is-time-to-ban-the-sale-of-precise-geolocation)

Tom Uren 在本文中主张全面禁止销售精确的地理位置数据，并引用了公民实验室（Citizen Lab）关于 Penlink 公司旗下监控工具“Webloc”的报告。

**地理位置数据的风险**
Webloc 提供全球约 5 亿台移动设备的数据访问权限，这些数据通过数字广告和广告技术（adtech）收集。此类数据允许对个人进行细粒度追踪（通常无需搜查令），并可与社交媒体标识符整合。Uren 强调，尽管这些工具能协助美国执法，但它们构成了双重威胁：既侵犯了国内公民自由，又带来了国家安全风险，因为外国对手可以购买或复制这些数据来针对美国利益。虽然弗吉尼亚州最近颁布了此类销售禁令，但 Uren 呼吁采取更广泛的联邦行动。

**作为网络犯罪“倍增器”的 AI**
文章还详细引用了 Gambit 的一份报告，该报告涉及一名入侵了九个墨西哥政府机构的黑客。攻击者利用 Claude Code 和 GPT-4.1 自动进行侦察，并生成了数千份情报报告。这一案例表明，AI 充当了“力量倍增器”，使个人即便在使用已知漏洞时，也能以专业团队的速度和效率开展行动。

**网络安全领域的进展与更新**
尽管存在这些威胁，Uren 仍强调了三项积极进展：
1. 美国摧毁了一个针对家用路由器的俄罗斯格鲁乌（GRU）僵尸网络。
2. 联邦调查局（FBI）与印尼合作，取缔了一个大型网络钓鱼网络。
3. 谷歌在 Chrome 浏览器中推出设备绑定会话凭据（DBSC），以防止会话劫持。

通讯最后简要更新了以下内容：法国政府系统正从 Windows 转向 Linux；发现了恶意的大语言模型（LLM）代理路由器；以及中国致力于成为“网络强国”的战略五年计划。

---

## 7. Healthchecks.io 现已采用自托管对象存储。

**原文标题**: Healthchecks.io Now Uses Self-Hosted Object Storage

**原文链接**: [https://blog.healthchecks.io/2026/04/healthchecks-io-now-uses-self-hosted-object-storage/](https://blog.healthchecks.io/2026/04/healthchecks-io-now-uses-self-hosted-object-storage/)

Healthchecks.io 创始人 Pēteris Caune 最近宣布，该服务已将其对象存储（用于存储 ping 请求主体）从托管服务商迁移到了自建方案。

此次迁移的原因是之前的服务商（包括 OVHcloud 和 UpCloud）性能下降且存在可靠性问题。虽然曾考虑过 AWS S3，但其按请求计费的模式以及《云法案》(CLOUD Act) 的影响，使其不适合 Healthchecks.io 高频、小对象的应用场景。

为了避免 Minio 或 SeaweedFS 等分布式系统带来的运维复杂性，Caune 选择了 **Versity S3 Gateway**。该工具将 S3 操作直接映射到本地文件系统，将 S3 对象视为普通文件。这种简洁性使得这个单人团队能够使用标准的备份工具和二进制更新来管理系统。

**新架构的关键技术细节包括：**
*   **硬件/操作系统：** 一台配备 NVMe 硬盘（RAID 1）并运行 **Btrfs 文件系统**（以避免 inode 耗尽）的专用服务器。
*   **安全性：** 应用服务器通过 Wireguard 隧道与存储服务器通信。
*   **持久性：** 数据每两小时通过 rsync 同步至备份服务器，每日加密的异地备份保留 30 天。
*   **规模：** 系统目前处理 1400 万个对象（119GB），峰值上传每秒达 150 次。

结果显示，S3 操作延迟显著降低，上传队列也变短了。虽然租用专用服务器比托管存储成本更高，且在硬件故障时存在丢失最多两小时数据的微小风险，但 Caune 总结认为，性能和可靠性的提升以及对第三方处理器的依赖减少，使得这些权衡是值得的。

---

## 8. Kyber (YC W23) 招聘工程负责人

**原文标题**: Kyber (YC W23) Is Hiring a Head of Engineering

**原文链接**: [https://www.ycombinator.com/companies/kyber/jobs/TcEa3b5-head-of-engineering](https://www.ycombinator.com/companies/kyber/jobs/TcEa3b5-head-of-engineering)

Kyber (YC W23), a profitable AI-native document platform for enterprise regulatory workflows, is hiring a **Head of Engineering** in New York City with a clear path to becoming CTO. The company has experienced significant recent momentum, including 40x revenue growth and multi-year contracts with major insurance enterprises.

**Role and Compensation**
The position offers a salary of **$220K – $280K** and **0.50% – 1.50% equity**. Kyber is seeking a hands-on "10x engineer" with at least six years of experience who thrives in early-stage environments and can balance high-volume coding with strategic leadership.

**Key Responsibilities**
*   **Technical Ownership:** Lead end-to-end decisions across the stack (TypeScript, Node.js, React, PostgreSQL, Redis).
*   **AI Integration:** Scale engineering capacity by incorporating agentic AI coding tools (e.g., Cursor, Claude Code) into the development workflow.
*   **Execution:** Manage an aggressive product roadmap, ship features personally, and ensure system reliability and uptime.
*   **Compliance:** Maintain enterprise-grade security standards, including SOC 2 and HIPAA.
*   **Leadership:** Mentor the existing team and spearhead future recruitment efforts.

**Candidate Profile**
The ideal candidate possesses mastery in system design and a "ship first, harden later" mentality. They must be comfortable with enterprise software requirements and demonstrate high accountability. The role is open to US citizens and valid visa holders only.

**How to Apply**
The hiring process includes founder screens, a practical take-home assignment, technical deep dives, and a five-reference check. To stand out, Kyber encourages applicants to have a former colleague submit their resume and a brief endorsement directly to the founder.

---

## 9. Iceye Open Data

**原文标题**: Iceye Open Data

**原文链接**: [https://www.iceye.com/open-data-initiative](https://www.iceye.com/open-data-initiative)

生成摘要时出错

---

## 10. Designing the Transport Typeface

**原文标题**: Designing the Transport Typeface

**原文链接**: [https://www.thamesandhudson.com/blogs/all-news-features/designing-the-transport-typeface-margaret-calvert-on-the-making-of-britain-s-road-signs](https://www.thamesandhudson.com/blogs/all-news-features/designing-the-transport-typeface-margaret-calvert-on-the-making-of-britain-s-road-signs)

生成摘要时出错

---

## 11. Show HN: PanicLock – Close your MacBook lid disable TouchID –> password unlock

**原文标题**: Show HN: PanicLock – Close your MacBook lid disable TouchID –> password unlock

**原文链接**: [https://github.com/paniclock/paniclock/](https://github.com/paniclock/paniclock/)

生成摘要时出错

---

## 12. Claude Opus 4.7

**原文标题**: Claude Opus 4.7

**原文链接**: [https://www.anthropic.com/news/claude-opus-4-7](https://www.anthropic.com/news/claude-opus-4-7)

生成摘要时出错

---

## 13. The Utopia of the Family Computer

**原文标题**: The Utopia of the Family Computer

**原文链接**: [https://mudmapmagazine.com/the-utopia-of-the-family-computer/](https://mudmapmagazine.com/the-utopia-of-the-family-computer/)

生成摘要时出错

---

## 14. Show HN: Stage – Putting humans back in control of code review

**原文标题**: Show HN: Stage – Putting humans back in control of code review

**原文链接**: [https://stagereview.app/](https://stagereview.app/)

生成摘要时出错

---

## 15. NASA Force

**原文标题**: NASA Force

**原文链接**: [https://nasaforce.gov/](https://nasaforce.gov/)

生成摘要时出错

---

## 16. Solitaire simulator for finding the best strategy: Current record is 8.590%

**原文标题**: Solitaire simulator for finding the best strategy: Current record is 8.590%

**原文链接**: [https://github.com/dacracot/Klondike3-Simulator](https://github.com/dacracot/Klondike3-Simulator)

生成摘要时出错

---

## 17. The Gregorio project – GPL tools for typesetting Gregorian chant

**原文标题**: The Gregorio project – GPL tools for typesetting Gregorian chant

**原文链接**: [https://gregorio-project.github.io/index.html](https://gregorio-project.github.io/index.html)

生成摘要时出错

---

## 18. Codex for almost everything

**原文标题**: Codex for almost everything

**原文链接**: [https://openai.com/index/codex-for-almost-everything/](https://openai.com/index/codex-for-almost-everything/)

生成摘要时出错

---

## 19. Hyperscalers have already outspent most famous US megaprojects

**原文标题**: Hyperscalers have already outspent most famous US megaprojects

**原文链接**: [https://twitter.com/finmoorhouse/status/2044933442236776794](https://twitter.com/finmoorhouse/status/2044933442236776794)

生成摘要时出错

---

## 20. Teddy Roosevelt and Abraham Lincoln in the same photo (2010)

**原文标题**: Teddy Roosevelt and Abraham Lincoln in the same photo (2010)

**原文链接**: [https://prologue.blogs.archives.gov/2010/11/09/teddy-roosevelt-and-abraham-lincoln-in-the-same-photo/](https://prologue.blogs.archives.gov/2010/11/09/teddy-roosevelt-and-abraham-lincoln-in-the-same-photo/)

生成摘要时出错

---

## 21. FIM – Linux framebuffer image viewer

**原文标题**: FIM – Linux framebuffer image viewer

**原文链接**: [https://www.nongnu.org/fbi-improved/](https://www.nongnu.org/fbi-improved/)

生成摘要时出错

---

## 22. Ada, Its Design, and the Language That Built the Languages

**原文标题**: Ada, Its Design, and the Language That Built the Languages

**原文链接**: [https://www.iqiipi.com/the-quiet-colossus.html](https://www.iqiipi.com/the-quiet-colossus.html)

生成摘要时出错

---

## 23. Scan your website to see how ready it is for AI agents

**原文标题**: Scan your website to see how ready it is for AI agents

**原文链接**: [https://isitagentready.com](https://isitagentready.com)

生成摘要时出错

---

## 24. CadQuery is an open-source Python library for building 3D CAD models

**原文标题**: CadQuery is an open-source Python library for building 3D CAD models

**原文链接**: [https://cadquery.github.io/](https://cadquery.github.io/)

生成摘要时出错

---

## 25. The missing catalogue: why finding books in translation is still so hard

**原文标题**: The missing catalogue: why finding books in translation is still so hard

**原文链接**: [https://blogs.lse.ac.uk/impactofsocialsciences/2026/04/13/the-missing-catalogue-why-finding-books-in-translation-is-still-so-hard/](https://blogs.lse.ac.uk/impactofsocialsciences/2026/04/13/the-missing-catalogue-why-finding-books-in-translation-is-still-so-hard/)

生成摘要时出错

---

## 26. A Python Interpreter Written in Python

**原文标题**: A Python Interpreter Written in Python

**原文链接**: [https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html](https://aosabook.org/en/500L/a-python-interpreter-written-in-python.html)

生成摘要时出错

---

## 27. Official Clojure Documentary page with Video, Shownotes, and Links

**原文标题**: Official Clojure Documentary page with Video, Shownotes, and Links

**原文链接**: [https://clojure.org/about/documentary](https://clojure.org/about/documentary)

生成摘要时出错

---

## 28. Android CLI: Build Android apps 3x faster using any agent

**原文标题**: Android CLI: Build Android apps 3x faster using any agent

**原文链接**: [https://android-developers.googleblog.com/2026/04/build-android-apps-3x-faster-using-any-agent.html](https://android-developers.googleblog.com/2026/04/build-android-apps-3x-faster-using-any-agent.html)

生成摘要时出错

---

## 29. Playdate’s handheld changed how Duke University teaches game design

**原文标题**: Playdate’s handheld changed how Duke University teaches game design

**原文链接**: [https://news.play.date/news/duke-playdate-education/](https://news.play.date/news/duke-playdate-education/)

生成摘要时出错

---

## 30. 中文 Literacy Speedrun II: Character Cyclotron

**原文标题**: 中文 Literacy Speedrun II: Character Cyclotron

**原文链接**: [https://blog.kevinzwu.com/character-cyclotron/](https://blog.kevinzwu.com/character-cyclotron/)

生成摘要时出错

---

## 31. 中文 Literacy Speedrun II: Character Cyclotron

**原文标题**: 中文 Literacy Speedrun II: Character Cyclotron

**原文链接**: [https://blog.kevinzwu.com/character-cyclotron/](https://blog.kevinzwu.com/character-cyclotron/)

生成摘要时出错

---

## 32. Congress extends controversial surveillance powers for 10 days

**原文标题**: Congress extends controversial surveillance powers for 10 days

**原文链接**: [https://www.npr.org/2026/04/17/nx-s1-5788573/house-extends-surveillance-powers-for-10-days](https://www.npr.org/2026/04/17/nx-s1-5788573/house-extends-surveillance-powers-for-10-days)

生成摘要时出错

---

## 33. Human Accelerated Region 1

**原文标题**: Human Accelerated Region 1

**原文链接**: [https://en.wikipedia.org/wiki/Human_accelerated_region_1](https://en.wikipedia.org/wiki/Human_accelerated_region_1)

生成摘要时出错

---

## 34. Reflections on 30 Years of HPC Programming

**原文标题**: Reflections on 30 Years of HPC Programming

**原文链接**: [https://chapel-lang.org/blog/posts/30years/](https://chapel-lang.org/blog/posts/30years/)

生成摘要时出错

---

## 35. Show HN: SPICE simulation → oscilloscope → verification with Claude Code

**原文标题**: Show HN: SPICE simulation → oscilloscope → verification with Claude Code

**原文链接**: [https://lucasgerads.com/blog/lecroy-mcp-spice-demo/](https://lucasgerads.com/blog/lecroy-mcp-spice-demo/)

生成摘要时出错

---

## 36. Guy builds AI driven hardware hacker arm from duct tape, old cam and CNC machine

**原文标题**: Guy builds AI driven hardware hacker arm from duct tape, old cam and CNC machine

**原文链接**: [https://github.com/gainsec/autoprober](https://github.com/gainsec/autoprober)

生成摘要时出错

---

## 37. Slop Cop

**原文标题**: Slop Cop

**原文链接**: [https://awnist.com/slop-cop](https://awnist.com/slop-cop)

生成摘要时出错

---

## 38. A Better R Programming Experience Thanks to Tree-sitter

**原文标题**: A Better R Programming Experience Thanks to Tree-sitter

**原文链接**: [https://ropensci.org/blog/2026/04/02/tree-sitter-overview/](https://ropensci.org/blog/2026/04/02/tree-sitter-overview/)

生成摘要时出错

---

## 39. ReBot-DevArm: open-source Robotic Arm

**原文标题**: ReBot-DevArm: open-source Robotic Arm

**原文链接**: [https://github.com/Seeed-Projects/reBot-DevArm](https://github.com/Seeed-Projects/reBot-DevArm)

生成摘要时出错

---

## 40. Qwen3.6-35B-A3B: Agentic coding power, now open to all

**原文标题**: Qwen3.6-35B-A3B: Agentic coding power, now open to all

**原文链接**: [https://qwen.ai/blog?id=qwen3.6-35b-a3b](https://qwen.ai/blog?id=qwen3.6-35b-a3b)

生成摘要时出错

---

## 41. A Git helper tool that breaks large merges into parallelizable tasks

**原文标题**: A Git helper tool that breaks large merges into parallelizable tasks

**原文链接**: [https://github.com/mwallner/mergetopus](https://github.com/mwallner/mergetopus)

生成摘要时出错

---

## 42. Cloudflare's AI Platform: an inference layer designed for agents

**原文标题**: Cloudflare's AI Platform: an inference layer designed for agents

**原文链接**: [https://blog.cloudflare.com/ai-platform/](https://blog.cloudflare.com/ai-platform/)

生成摘要时出错

---

## 43. The future of everything is lies, I guess: Where do we go from here?

**原文标题**: The future of everything is lies, I guess: Where do we go from here?

**原文链接**: [https://aphyr.com/posts/420-the-future-of-everything-is-lies-i-guess-where-do-we-go-from-here](https://aphyr.com/posts/420-the-future-of-everything-is-lies-i-guess-where-do-we-go-from-here)

生成摘要时出错

---

## 44. The beginning of scarcity in AI

**原文标题**: The beginning of scarcity in AI

**原文链接**: [https://tomtunguz.com/ai-compute-crisis-2026/](https://tomtunguz.com/ai-compute-crisis-2026/)

生成摘要时出错

---

## 45. Century-bandwidth antenna reinvented,patented after 18 yrs with decade bandwidth (2006)

**原文标题**: Century-bandwidth antenna reinvented,patented after 18 yrs with decade bandwidth (2006)

**原文链接**: [https://ieeexplore.ieee.org/document/1715264](https://ieeexplore.ieee.org/document/1715264)

生成摘要时出错

---

## 46. Codex Hacked a Samsung TV

**原文标题**: Codex Hacked a Samsung TV

**原文链接**: [https://blog.calif.io/p/codex-hacked-a-samsung-tv](https://blog.calif.io/p/codex-hacked-a-samsung-tv)

生成摘要时出错

---

## 47. Launch HN: Kampala (YC W26) – Reverse-Engineer Apps into APIs

**原文标题**: Launch HN: Kampala (YC W26) – Reverse-Engineer Apps into APIs

**原文链接**: [https://www.zatanna.ai/kampala](https://www.zatanna.ai/kampala)

生成摘要时出错

---

## 48. NIST cuts down CVE analysis amid vulnerability overload

**原文标题**: NIST cuts down CVE analysis amid vulnerability overload

**原文链接**: [https://www.csoonline.com/article/4159882/nist-cuts-down-cve-analysis-amid-vulnerability-overload.html](https://www.csoonline.com/article/4159882/nist-cuts-down-cve-analysis-amid-vulnerability-overload.html)

生成摘要时出错

---

## 49. Discourse Is Not Going Closed Source

**原文标题**: Discourse Is Not Going Closed Source

**原文链接**: [https://blog.discourse.org/2026/04/discourse-is-not-going-closed-source/](https://blog.discourse.org/2026/04/discourse-is-not-going-closed-source/)

生成摘要时出错

---

## 50. Bluesky has been dealing with a DDoS attack for nearly a full day

**原文标题**: Bluesky has been dealing with a DDoS attack for nearly a full day

**原文链接**: [https://www.theverge.com/tech/913638/bluesky-has-been-dealing-with-a-ddos-attack-for-nearly-a-full-day](https://www.theverge.com/tech/913638/bluesky-has-been-dealing-with-a-ddos-attack-for-nearly-a-full-day)

生成摘要时出错

---

## 51. Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7

**原文标题**: Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7

**原文链接**: [https://simonwillison.net/2026/Apr/16/qwen-beats-opus/](https://simonwillison.net/2026/Apr/16/qwen-beats-opus/)

生成摘要时出错

---

## 52. AI cybersecurity is not proof of work

**原文标题**: AI cybersecurity is not proof of work

**原文链接**: [https://antirez.com/news/163](https://antirez.com/news/163)

生成摘要时出错

---

## 53. New unsealed records reveal Amazon's price-fixing tactics, California AG claims

**原文标题**: New unsealed records reveal Amazon's price-fixing tactics, California AG claims

**原文链接**: [https://www.theguardian.com/us-news/ng-interactive/2026/apr/16/amazon-price-fixing-california-lawsuit](https://www.theguardian.com/us-news/ng-interactive/2026/apr/16/amazon-price-fixing-california-lawsuit)

生成摘要时出错

---

## 54. Precision over perception: Why architecture matters in benchmarking

**原文标题**: Precision over perception: Why architecture matters in benchmarking

**原文链接**: [https://www.redhat.com/en/blog/precision-over-perception-why-architecture-matters-benchmarking](https://www.redhat.com/en/blog/precision-over-perception-why-architecture-matters-benchmarking)

生成摘要时出错

---

## 55. EU age verification app hacked, 2 minute How to posted

**原文标题**: EU age verification app hacked, 2 minute How to posted

**原文链接**: [https://xcancel.com/Paul_Reviews/status/2044723123287666921](https://xcancel.com/Paul_Reviews/status/2044723123287666921)

生成摘要时出错

---

## 56. Rubens Menin's 150 Years "Old" Port Wine

**原文标题**: Rubens Menin's 150 Years "Old" Port Wine

**原文链接**: [https://neofeed.com.br/finde/o-vinho-do-porto-very-very-old-de-rubens-menin/en/](https://neofeed.com.br/finde/o-vinho-do-porto-very-very-old-de-rubens-menin/en/)

生成摘要时出错

---

## 57. Artifacts: Versioned storage that speaks Git

**原文标题**: Artifacts: Versioned storage that speaks Git

**原文链接**: [https://blog.cloudflare.com/artifacts-git-for-agents-beta/](https://blog.cloudflare.com/artifacts-git-for-agents-beta/)

生成摘要时出错

---

## 58. Everything we like is a psyop?

**原文标题**: Everything we like is a psyop?

**原文链接**: [https://techcrunch.com/2026/04/16/everything-we-like-is-a-psyop/](https://techcrunch.com/2026/04/16/everything-we-like-is-a-psyop/)

生成摘要时出错

---

## 59. US Bill Mandates On-Device Age Verification

**原文标题**: US Bill Mandates On-Device Age Verification

**原文链接**: [https://reclaimthenet.org/us-bill-mandates-on-device-age-verification](https://reclaimthenet.org/us-bill-mandates-on-device-age-verification)

生成摘要时出错

---

## 60. Show HN: MacMind – A transformer neural network in HyperCard on a 1989 Macintosh

**原文标题**: Show HN: MacMind – A transformer neural network in HyperCard on a 1989 Macintosh

**原文链接**: [https://github.com/SeanFDZ/macmind](https://github.com/SeanFDZ/macmind)

生成摘要时出错

---

## 61. GPT‑Rosalind for life sciences research

**原文标题**: GPT‑Rosalind for life sciences research

**原文链接**: [https://openai.com/index/introducing-gpt-rosalind/](https://openai.com/index/introducing-gpt-rosalind/)

生成摘要时出错

---

## 62. Israel escalates attacks on medics in Lebanon with deadly 'quadruple tap'

**原文标题**: Israel escalates attacks on medics in Lebanon with deadly 'quadruple tap'

**原文链接**: [https://www.theguardian.com/world/2026/apr/16/israel-escalates-attacks-on-medics-in-lebanon-with-deadly-quadruple-tap](https://www.theguardian.com/world/2026/apr/16/israel-escalates-attacks-on-medics-in-lebanon-with-deadly-quadruple-tap)

生成摘要时出错

---

## 63. PHP 8.6 Closure Optimizations

**原文标题**: PHP 8.6 Closure Optimizations

**原文链接**: [https://wiki.php.net/rfc/closure-optimizations](https://wiki.php.net/rfc/closure-optimizations)

生成摘要时出错

---

## 64. The "Passive Income" trap ate a generation of entrepreneurs

**原文标题**: The "Passive Income" trap ate a generation of entrepreneurs

**原文链接**: [https://www.joanwestenberg.com/the-passive-income-trap-ate-a-generation-of-entrepreneurs/](https://www.joanwestenberg.com/the-passive-income-trap-ate-a-generation-of-entrepreneurs/)

生成摘要时出错

---

## 65. Show HN: CodeBurn – Analyze Claude Code token usage by task

**原文标题**: Show HN: CodeBurn – Analyze Claude Code token usage by task

**原文链接**: [https://github.com/AgentSeal/codeburn](https://github.com/AgentSeal/codeburn)

生成摘要时出错

---

## 66. Cave under castle with prehistoric hippo bones 'once in a lifetime' find

**原文标题**: Cave under castle with prehistoric hippo bones 'once in a lifetime' find

**原文链接**: [https://www.bbc.com/news/articles/c8ejjw7377jo](https://www.bbc.com/news/articles/c8ejjw7377jo)

生成摘要时出错

---

## 67. What's the Point of Hardbacks?

**原文标题**: What's the Point of Hardbacks?

**原文链接**: [https://tomrowley.substack.com/p/whats-the-point-of-hardbacks](https://tomrowley.substack.com/p/whats-the-point-of-hardbacks)

生成摘要时出错

---

## 68. PROBoter – Open-source platform for automated PCB analysis

**原文标题**: PROBoter – Open-source platform for automated PCB analysis

**原文链接**: [https://www.schutzwerk.com/en/blog/proboter-01/](https://www.schutzwerk.com/en/blog/proboter-01/)

生成摘要时出错

---

## 69. Circuit Transformations, Loop Fusion, and Inductive Proof

**原文标题**: Circuit Transformations, Loop Fusion, and Inductive Proof

**原文链接**: [https://natetyoung.github.io/carry_save_fusion/](https://natetyoung.github.io/carry_save_fusion/)

生成摘要时出错

---

## 70. North American English Dialects

**原文标题**: North American English Dialects

**原文链接**: [https://aschmann.net/AmEng/](https://aschmann.net/AmEng/)

生成摘要时出错

---

## 71. Cloudflare Email Service

**原文标题**: Cloudflare Email Service

**原文链接**: [https://blog.cloudflare.com/email-for-agents/](https://blog.cloudflare.com/email-for-agents/)

生成摘要时出错

---

## 72. US tech firms lobbied EU to keep datacentre emissions secret

**原文标题**: US tech firms lobbied EU to keep datacentre emissions secret

**原文链接**: [https://www.theguardian.com/technology/2026/apr/17/microsoft-us-tech-firms-lobbied-eu-secrecy-rules-datacentre-emissions](https://www.theguardian.com/technology/2026/apr/17/microsoft-us-tech-firms-lobbied-eu-secrecy-rules-datacentre-emissions)

生成摘要时出错

---

## 73. German Dog Commands

**原文标题**: German Dog Commands

**原文链接**: [https://www.fluentu.com/blog/german/german-dog-commands/](https://www.fluentu.com/blog/german/german-dog-commands/)

生成摘要时出错

---

## 74. Building a Web Page That Edits Itself

**原文标题**: Building a Web Page That Edits Itself

**原文链接**: [https://www.patrickweaver.net/blog/one-pager-self-editing-html/](https://www.patrickweaver.net/blog/one-pager-self-editing-html/)

生成摘要时出错

---

## 75. Darkbloom – Private inference on idle Macs

**原文标题**: Darkbloom – Private inference on idle Macs

**原文链接**: [https://darkbloom.dev](https://darkbloom.dev)

生成摘要时出错

---

## 76. US v. Heppner (S.D.N.Y. 2026) no attorney-client privilege for AI chats [pdf]

**原文标题**: US v. Heppner (S.D.N.Y. 2026) no attorney-client privilege for AI chats [pdf]

**原文链接**: [https://fingfx.thomsonreuters.com/gfx/legaldocs/xmvjyjekkpr/Rakoff%20-%20order%20-%20AI.pdf](https://fingfx.thomsonreuters.com/gfx/legaldocs/xmvjyjekkpr/Rakoff%20-%20order%20-%20AI.pdf)

生成摘要时出错

---

## 77. RedSun: System user access on Win 11/10 and Server with the April 2026 Update

**原文标题**: RedSun: System user access on Win 11/10 and Server with the April 2026 Update

**原文链接**: [https://github.com/Nightmare-Eclipse/RedSun](https://github.com/Nightmare-Eclipse/RedSun)

生成摘要时出错

---

## 78. The paper computer

**原文标题**: The paper computer

**原文链接**: [https://jsomers.net/blog/the-paper-computer](https://jsomers.net/blog/the-paper-computer)

生成摘要时出错

---

## 79. Six Characters

**原文标题**: Six Characters

**原文链接**: [https://ajitem.com/blog/iron-core-part-2-six-characters/](https://ajitem.com/blog/iron-core-part-2-six-characters/)

生成摘要时出错

---

## 80. Too much discussion of the XOR swap trick

**原文标题**: Too much discussion of the XOR swap trick

**原文链接**: [https://heather.cafe/posts/too_much_xor_swap_trick/](https://heather.cafe/posts/too_much_xor_swap_trick/)

生成摘要时出错

---

## 81. FSF trying to contact Google about spammer sending 10k+ mails from Gmail account

**原文标题**: FSF trying to contact Google about spammer sending 10k+ mails from Gmail account

**原文链接**: [https://daedal.io/@thomzane/116410863009847575](https://daedal.io/@thomzane/116410863009847575)

生成摘要时出错

---

## 82. Show HN: Marky – A lightweight Markdown viewer for agentic coding

**原文标题**: Show HN: Marky – A lightweight Markdown viewer for agentic coding

**原文链接**: [https://github.com/GRVYDEV/marky](https://github.com/GRVYDEV/marky)

生成摘要时出错

---

## 83. IPv6 traffic crosses the 50% mark

**原文标题**: IPv6 traffic crosses the 50% mark

**原文链接**: [https://www.google.com/intl/en/ipv6/statistics.html?yzh=28197](https://www.google.com/intl/en/ipv6/statistics.html?yzh=28197)

生成摘要时出错

---

## 84. ChatGPT for Excel

**原文标题**: ChatGPT for Excel

**原文链接**: [https://chatgpt.com/apps/spreadsheets/](https://chatgpt.com/apps/spreadsheets/)

生成摘要时出错

---

## 85. Do you even need a database?

**原文标题**: Do you even need a database?

**原文链接**: [https://www.dbpro.app/blog/do-you-even-need-a-database](https://www.dbpro.app/blog/do-you-even-need-a-database)

生成摘要时出错

---

## 86. Ancient DNA reveals pervasive directional selection across West Eurasia [pdf]

**原文标题**: Ancient DNA reveals pervasive directional selection across West Eurasia [pdf]

**原文链接**: [https://reich.hms.harvard.edu/sites/reich.hms.harvard.edu/files/inline-files/2026_Akbari_Nature_selection_0.pdf](https://reich.hms.harvard.edu/sites/reich.hms.harvard.edu/files/inline-files/2026_Akbari_Nature_selection_0.pdf)

生成摘要时出错

---

## 87. Retrofitting JIT Compilers into C Interpreters

**原文标题**: Retrofitting JIT Compilers into C Interpreters

**原文链接**: [https://tratt.net/laurie/blog/2026/retrofitting_jit_compilers_into_c_interpreters.html](https://tratt.net/laurie/blog/2026/retrofitting_jit_compilers_into_c_interpreters.html)

生成摘要时出错

---

## 88. Shares in shoe brand Allbirds rise 580% after it pivots from footwear to AI

**原文标题**: Shares in shoe brand Allbirds rise 580% after it pivots from footwear to AI

**原文链接**: [https://www.bbc.com/news/articles/c98mrepzgj7o](https://www.bbc.com/news/articles/c98mrepzgj7o)

生成摘要时出错

---

## 89. Introduction to spherical harmonics for graphics programmers

**原文标题**: Introduction to spherical harmonics for graphics programmers

**原文链接**: [https://gpfault.net/posts/sph.html](https://gpfault.net/posts/sph.html)

生成摘要时出错

---

## 90. The Gemini app is now on Mac

**原文标题**: The Gemini app is now on Mac

**原文链接**: [https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-mac-os/](https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-mac-os/)

生成摘要时出错

---

## 91. Tailscale-rs: Official Rust library for embedding Tailscale

**原文标题**: Tailscale-rs: Official Rust library for embedding Tailscale

**原文链接**: [https://tailscale.com/blog/tailscale-rs-rust-tsnet-library-preview](https://tailscale.com/blog/tailscale-rs-rust-tsnet-library-preview)

生成摘要时出错

---

## 92. Probabilistic engineering and the 24-7 employee

**原文标题**: Probabilistic engineering and the 24-7 employee

**原文链接**: [https://www.timdavis.com/blog/probabilistic-engineering-and-the-24-7-employee](https://www.timdavis.com/blog/probabilistic-engineering-and-the-24-7-employee)

生成摘要时出错

---

## 93. PiCore - Raspberry Pi Port of Tiny Core Linux

**原文标题**: PiCore - Raspberry Pi Port of Tiny Core Linux

**原文链接**: [http://tinycorelinux.net/5.x/armv6/releases/README](http://tinycorelinux.net/5.x/armv6/releases/README)

生成摘要时出错

---

## 94. Japan implements language proficiency requirements for certain visa applicants

**原文标题**: Japan implements language proficiency requirements for certain visa applicants

**原文链接**: [https://www.japantimes.co.jp/news/2026/04/15/japan/society/jlpt-visa-requirement/](https://www.japantimes.co.jp/news/2026/04/15/japan/society/jlpt-visa-requirement/)

生成摘要时出错

---

## 95. IBM AP-101 general-purpose computer [pdf]

**原文标题**: IBM AP-101 general-purpose computer [pdf]

**原文链接**: [https://gandalfddi.z19.web.core.windows.net/Shuttle/IBM%20AP-101S%20General%20Purpose%20Computer%20With%20Shuttle%20Instruction%20Set.pdf](https://gandalfddi.z19.web.core.windows.net/Shuttle/IBM%20AP-101S%20General%20Purpose%20Computer%20With%20Shuttle%20Instruction%20Set.pdf)

生成摘要时出错

---

## 96. Direct Win32 API, weird-shaped windows, and why they mostly disappeared

**原文标题**: Direct Win32 API, weird-shaped windows, and why they mostly disappeared

**原文链接**: [https://warped3.substack.com/p/direct-win32-api-weird-shaped-windows](https://warped3.substack.com/p/direct-win32-api-weird-shaped-windows)

生成摘要时出错

---

## 97. The buns in McDonald's Japan's burger photos are all slightly askew

**原文标题**: The buns in McDonald's Japan's burger photos are all slightly askew

**原文链接**: [https://www.mcdonalds.co.jp/en/menu/burger/](https://www.mcdonalds.co.jp/en/menu/burger/)

生成摘要时出错

---

## 98. Cybersecurity looks like proof of work now

**原文标题**: Cybersecurity looks like proof of work now

**原文链接**: [https://www.dbreunig.com/2026/04/14/cybersecurity-is-proof-of-work-now.html](https://www.dbreunig.com/2026/04/14/cybersecurity-is-proof-of-work-now.html)

生成摘要时出错

---

## 99. Live Nation illegally monopolized ticketing market, jury finds

**原文标题**: Live Nation illegally monopolized ticketing market, jury finds

**原文链接**: [https://www.bloomberg.com/news/articles/2026-04-15/live-nation-illegally-monopolized-ticketing-market-jury-finds](https://www.bloomberg.com/news/articles/2026-04-15/live-nation-illegally-monopolized-ticketing-market-jury-finds)

生成摘要时出错

---

## 100. Moving a large-scale metrics pipeline from StatsD to OpenTelemetry / Prometheus

**原文标题**: Moving a large-scale metrics pipeline from StatsD to OpenTelemetry / Prometheus

**原文链接**: [https://medium.com/airbnb-engineering/building-a-high-volume-metrics-pipeline-with-opentelemetry-and-vmagent-c714d6910b45](https://medium.com/airbnb-engineering/building-a-high-volume-metrics-pipeline-with-opentelemetry-and-vmagent-c714d6910b45)

生成摘要时出错

---

