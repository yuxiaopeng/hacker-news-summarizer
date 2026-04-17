# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-04-17.md)

*最后自动更新时间: 2026-04-17 18:16:48*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 2 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 3 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 4 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 5 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 6 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 7 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 8 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 9 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 10 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 11 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 12 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 13 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 14 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 15 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 16 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 17 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 18 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 19 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 20 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 21 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 22 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 23 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 24 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 25 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 26 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 27 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 28 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 29 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 30 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 31 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 32 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 33 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 34 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 35 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 36 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 37 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 38 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 39 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 40 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 41 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 42 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 43 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 44 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 45 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 46 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 47 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 48 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 49 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 50 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 51 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 52 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 53 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 54 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 55 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 56 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 57 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 58 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 59 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 60 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 61 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 62 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 63 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 64 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 65 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 66 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 67 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 68 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 69 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 70 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 71 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 72 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 73 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 74 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 75 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 76 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 77 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 78 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 79 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 80 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 81 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 82 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 83 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 84 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 85 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 86 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 87 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 88 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 89 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 90 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 91 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 92 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 93 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 94 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 95 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 96 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 97 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 98 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 99 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 100 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 101 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 102 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 103 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 104 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 105 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 106 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 107 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 108 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 109 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 110 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 111 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 112 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 113 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 114 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 115 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 116 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 117 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 118 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 119 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 120 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 121 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 122 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 123 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 124 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 125 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 126 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 127 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 128 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 129 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 130 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 131 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 132 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 133 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 134 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 135 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 136 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 137 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 138 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 139 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 140 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 141 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 142 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 143 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 144 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 145 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 146 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 147 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 148 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 149 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 150 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 151 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 152 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 153 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 154 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 155 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 156 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 157 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 158 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 159 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 160 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 161 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 162 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 163 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 164 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 165 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 166 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 167 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 168 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 169 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 170 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 171 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 172 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 173 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 174 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 175 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 176 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 177 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 178 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 179 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 180 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 181 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 182 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 183 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 184 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 185 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 186 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 187 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 188 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 189 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 190 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 191 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 192 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 193 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 194 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 195 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 196 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 197 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 198 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 199 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 200 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 201 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 202 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 203 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 204 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 205 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 206 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 207 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 208 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 209 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 210 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 211 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 212 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 213 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 214 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 215 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 216 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 217 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 218 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 219 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 220 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 221 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 222 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 223 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 224 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 225 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 226 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 227 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 228 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 229 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 230 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 231 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 232 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 233 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 234 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 235 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 236 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 237 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 238 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 239 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 240 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 241 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 242 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 243 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 244 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 245 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 246 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 247 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 248 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 249 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 250 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 251 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 252 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 253 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 254 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 255 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 256 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 257 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 258 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 259 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 260 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 261 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 262 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 263 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 264 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 265 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 266 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 267 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 268 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 269 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 270 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 271 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 272 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 273 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 274 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 275 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 276 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 277 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 278 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 279 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 280 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 281 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 282 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 283 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 284 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 285 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 286 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 287 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 288 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 289 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 290 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 291 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 292 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 293 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 294 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 295 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 296 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 297 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 298 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 299 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 300 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 301 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 302 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 303 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 304 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 305 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 306 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 307 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 308 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 309 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 310 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 311 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 312 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 313 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 314 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 315 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 316 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 317 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 318 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 319 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 320 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 321 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 322 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 323 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 324 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 325 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 326 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 327 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 328 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 329 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 330 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 331 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 332 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 333 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 334 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 335 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 336 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 337 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 338 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 339 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 340 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 341 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 342 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 343 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 344 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 345 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 346 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 347 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 348 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 349 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 350 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 351 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 352 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 353 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 354 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 355 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 356 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 357 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 358 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 359 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 360 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 361 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 362 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 363 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 364 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 365 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 366 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 367 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 368 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 369 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 370 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 371 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 372 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 373 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 374 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 375 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 376 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 377 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 378 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 379 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 380 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 381 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 382 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 383 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 384 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 385 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 386 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 387 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 388 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 389 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 390 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 391 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 392 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 393 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
