# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-12.md)

*最后自动更新时间: 2026-03-12 18:16:14*
## 1. Malus – 洁净室即服务

**原文标题**: Malus – Clean Room as a Service

**原文链接**: [https://malus.sh](https://malus.sh)

**Malus** 是一项讽刺性的“洁净室即服务”（Clean Room as a Service），旨在帮助企业规避开源软件（OSS）许可证带来的法律和伦理义务。它将自己包装为一种“解放”工具，专门针对那些对署名要求（Apache）、Copyleft“污染”（AGPL）以及回馈开发者社区的负担感到厌烦的公司。

该服务的核心是**机器人驱动的洁净室重建**流程。为了避免产生会继承开源许可证的“衍生作品”，Malus 雇佣了两个相互隔离的 AI 团队：
1. **分析团队：** 仅研究公开文档、API 和类型定义，绝不接触原始源代码。
2. **构建团队：** 仅根据分析团队提供的规格说明，从零开始重新实现软件。

这种方法论声称能产出功能等效但在“法律上独立”的代码，从而让客户拥有完整的软件所有权。产出的代码根据 **MalusCorp-0 许可证**交付，该许可证无需署名，允许绝对保密，且对原始维护者不承担任何义务。

**核心功能与定价：**
* **清单自动化：** 用户通过上传依赖文件（如 `package.json`、`requirements.txt`）来识别需要被“解放”的软件包。
* **广泛支持：** 兼容包括 npm、PyPI、Cargo 和 Maven 在内的多种生态系统。
* **按 KB 计费：** 成本根据依赖项解压后的大小进行计算。
* **赔偿保障：** 该服务提供一份可疑的担保，由一家设立在不承认软件版权的司法管辖区的离岸子公司承保。

本文的语调是对企业态度的辛辣讽刺，其中穿插了虚构的高管证词，展现了他们如何将股东价值和并购速度置于开源生态系统的可持续性之上。最终，Malus 承诺将“烦人”的社区义务转化为私有的企业资产。

---

## 2. 大都会艺术博物馆发布140件著名艺术品的高清3D扫描图

**原文标题**: The Met Releases High-Def 3D Scans of 140 Famous Art Objects

**原文链接**: [https://www.openculture.com/2026/03/the-met-releases-high-definition-3d-scans-of-140-famous-art-objects.html](https://www.openculture.com/2026/03/the-met-releases-high-definition-3d-scans-of-140-famous-art-objects.html)

大都会艺术博物馆发布了一个全新的数字档案库，收录了140件著名艺术品的高清3D扫描模型，为公众提供了接触其馆藏的前所未有的机会。通过这一举措，用户可以与梵高的《向日葵》、莫奈的《干草堆》以及丹铎神庙等重要作品进行互动，实现缩放、旋转并观察那些亲临现场也难以看清的细节。

这些3D模型具备极高的多功能性，支持智能手机上的增强现实（AR）技术以及各类虚拟现实（VR）头显设备。这一功能使研究人员、学生和艺术爱好者能够将历史文物投射到自己的环境中进行近距离研究。档案库中的亮点还包括亨利二世国王的盔甲、一座3世纪的大理石石棺，以及17世纪日本艺术家狩野山雪和铃木其一的屏风。

该项目是与日本公共广播机构NHK合作开发的，属于为文化瑰宝创建超高清图像计划的一部分。除了即时的探索体验，双方的合作还旨在利用这些顶级模型制作更多教育节目。

若要体验这些馆藏，用户只需在大都会博物馆官方网站的特定文物页面上点击“3D查看”按钮。虽然数字体验无法取代触摸实物的真实感，但它提供了一个亲密且多角度的视角，拉近了公众与这些世界上最重要的历史文物之间的距离。

---

## 3. 冒泡排序 Amen Break

**原文标题**: Bubble Sorted Amen Break

**原文链接**: [https://parametricavocado.itch.io/amen-sorting](https://parametricavocado.itch.io/amen-sorting)

生成摘要时出错

---

## 4. Show HN: OneCLI – Rust 实现的 AI 智能体保险库

**原文标题**: Show HN: OneCLI – Vault for AI Agents in Rust

**原文链接**: [https://github.com/onecli/onecli](https://github.com/onecli/onecli)

**OneCLI** 是一个开源的、基于 Rust 的安全网关，旨在管理和保护 AI 智能体（Agent）所使用的 API 凭据。它通过充当中间保管库将机密信息“注入”到出站请求中，从而解决了向自主智能体暴露原始 API 密钥的安全风险。

### 核心功能
该系统通过**透明凭据注入**进行工作。开发人员为 AI 智能体提供占位符密钥（例如 `FAKE_KEY`）而非真实凭据。当智能体通过 OneCLI 代理进行 HTTP 调用时，网关会拦截请求，将其与相应的主机或路径模式进行匹配，并将占位符替换为真实的、解密后的机密信息。这确保了智能体永远不会“看到”或处理实际的 API 密钥。

### 关键组件
*   **Rust 网关：** 一个高性能、内存安全的代理，用于拦截出站流量，并通过 MITM（中间人）方式处理 HTTPS 的机密注入。
*   **Web 控制面板：** 一个 Next.js 应用程序，用于管理智能体、轮换密钥以及定义作用域权限。
*   **安全存储：** 凭据在静态存储时使用 AES-256-GCM 进行加密，且仅在请求时解密。
*   **数据库：** 使用 PGlite 提供零依赖的嵌入式体验，同时也支持生产环境的外部 PostgreSQL。

### 主要特性
*   **多智能体支持：** 每个智能体都会获得具有特定权限的唯一访问令牌。
*   **主机与路径匹配：** 精确控制将哪些机密注入到特定的 API 端点。
*   **灵活的身份验证：** 支持用于本地开发的简单单用户模式，或用于团队协作的 Google OAuth。
*   **部署：** 专为易用性设计，支持 Docker 部署，允许开发人员通过单个命令启动网关和控制面板。

OneCLI 采用 **Apache-2.0** 许可协议，提供了一个集中化平台，可同时管理访问权限、轮换密钥并审计多个 AI 智能体的活动。

---

## 5. 通过肠脑通讯逆转记忆力丧失

**原文标题**: Reversing memory loss via gut-brain communication

**原文链接**: [https://med.stanford.edu/news/all-news/2026/03/gut-brain-cognitive-decline.html](https://med.stanford.edu/news/all-news/2026/03/gut-brain-cognitive-decline.html)

斯坦福医学院和 Arc 研究所研究人员的一项新研究表明，与年龄相关的记忆力减退并非仅仅是大脑内部的逻辑过程，而是受到“肠-脑轴”的积极调节。这项发表在《自然》（Nature）杂志上的研究将迷走神经鉴定为一个“遥控器”，负责将信号从胃肠道传递到大脑的记忆中心——海马体。

研究发现，随着小鼠年龄的增长，其肠道微生物群组成会发生变化，特别是金氏副拟杆菌（*Parabacteroides goldsteinii*）会有所增加。这种变化增加了某些代谢物（中链脂肪酸），从而引发肠道免疫细胞的炎症反应。这种炎症阻碍了迷走神经向大脑发送信号的能力，导致认知能力下降。

关键实验结果包括：
* **微生物群转移：** 与老年小鼠同笼居住的年轻小鼠获得了“老年”微生物群，并随后出现了记忆缺陷。
* **无菌实验成功：** 在没有肠道细菌的情况下培育的小鼠没有经历典型的与年龄相关的认知能力下降。
* **可逆性：** 研究人员通过使用抗生素重置微生物群或直接刺激迷走神经，将健忘的老年小鼠的记忆力恢复到了年轻水平。

这些结果表明，内感受（即大脑对身体内部状态的感知）是认知健康的关键调节因素。由于胃肠道易于干预，且迷走神经刺激已获得 FDA 批准用于治疗其他疾病，这些发现为临床干预提供了一条充满前景的途径。研究人员目前正在调查人类是否存在类似的通路，这可能为扭转老龄人口的认知能力下降和保护记忆提供新策略。

---

## 6. Kotlin 创始人发布新语言：一种替代英语与大模型交流的正式方式

**原文标题**: Kotlin creator's new language: a formal way to talk to LLMs instead of English

**原文链接**: [https://codespeak.dev/](https://codespeak.dev/)

Kotlin 创始人 Andrey Breslav 推出了 CodeSpeak，这是一种旨在为与大语言模型 (LLM) 通信提供正式、结构化方式的下一代编程语言。与非正式的“氛围编码 (vibe-coding)”或纯英文提示词不同，CodeSpeak 使用简洁的“规格说明 (specs)”来生成生产级代码，旨在弥合人类意图与机器执行之间的差距。

**核心特性与哲学：**
*   **代码库缩减：** 该语言声称可将代码库缩小 5 至 10 倍。通过维护高层级的规格说明而非数千行手动编写的代码，开发者可以更轻松地管理复杂系统。
*   **专业工程化：** CodeSpeak 的定位是面向专业团队和长期项目，而非个人爱好者或简单的原型开发。它强调“维护规格，而非代码”。
*   **混合集成：** 它支持“混合项目”，允许开发者将手动编写的代码与 LLM 生成的组件相结合。目前也正在开发将现有遗留代码转换为规格说明的功能。

**效能证明：**
文中重点列举了几个涉及开源 Python 库的真实案例研究，以展示其“缩减倍数”：
*   **BeautifulSoup4：** 代码从 826 行减少到 141 行规格说明（缩减 5.9 倍）。
*   **yt-dlp：** 从 255 行缩减至 38 行（缩减 6.7 倍）。
*   **MarkItDown：** 将 139 行压缩至仅 14 行（缩减 9.9 倍）。

在所有案例中，生成的代码均通过了现有测试，并在多个实例中促进了新测试的添加。CodeSpeak 目前处于 **Alpha 预览阶段**，可通过命令行界面 (`codespeak-cli`) 访问。

---

## 7. 2025年美国银行业私人信贷风险敞口触及3000亿美元

**原文标题**: US banks' exposure to private credit hits $300B (2025)

**原文链接**: [https://alternativecreditinvestor.com/2025/10/22/us-banks-exposure-to-private-credit-hits-300bn/](https://alternativecreditinvestor.com/2025/10/22/us-banks-exposure-to-private-credit-hits-300bn/)

截至2025年6月，美国银行对私人信贷的风险敞口已接近3000亿美元，在非存款类金融机构（NDFI）1.2万亿美元的总贷款额中占据了重要部分。根据穆迪评级（Moody’s Ratings）的分析，对NDFI的贷款目前占美国银行贷款总额的10.4%，与其十年前3.6%的占比相比增长了近两倍。

这一转变源于银行寻求通过与另类资产管理公司建立合作伙伴关系，从而实现收入来源多元化并降低风险。然而，穆迪指出一个“战略悖论”：银行正越来越多地为那些与其争夺市场份额的非银行贷款机构提供关键融资。

**关键数据与贷款机构：**
私人信贷领域的前五大贷款机构包括：
1. **富国银行 (Wells Fargo)：** 597亿美元
2. **美国银行 (Bank of America)：** 332亿美元
3. **PNC金融服务集团 (PNC)：** 295亿美元
4. **花旗集团 (Citigroup)：** 258亿美元
5. **摩根大通 (JPMorgan Chase)：** 222亿美元

虽然私人信贷行业的资产管理规模在过去十年中增长了两倍，但穆迪警告称“资产质量挑战可能会浮出水面”。报告以近期Tricolor Holdings的破产为例，说明了对NDFI的贷款可能导致重大损失。尽管一些行业专家对Tricolor和First Brands等案例中的欺诈行为与信用表现不佳进行了区分，但庞大的风险敞口规模仍是银行业需要保持警惕的重点。

---

## 8. Converge (YC S23) Is Hiring a Founding Platform Engineer (NYC, Onsite)

**原文标题**: Converge (YC S23) Is Hiring a Founding Platform Engineer (NYC, Onsite)

**原文链接**: [https://www.runconverge.com/careers/founding-platform-engineer](https://www.runconverge.com/careers/founding-platform-engineer)

Converge (YC S23), a NYC-based startup that provides marketing performance analytics for over 200 consumer brands, is seeking a **Founding Platform Engineer**. Having raised $5.7 million from investors like General Catalyst and Y Combinator, the company is looking for a hands-on engineer to own and scale the data infrastructure powering their platform.

**The Role and Technical Scale**
This is an onsite, coding-intensive position. The engineer will manage a platform that currently handles $4 billion in annual revenue, ingests 20TB of data monthly, and processes 5 billion jobs per month (peaking at 6,000 jobs/second). Responsibilities include building services for massive job ingestion, optimizing Clickhouse performance, and developing real-time data materialization strategies for billion-row datasets.

**Candidate Requirements**
The ideal candidate is a pragmatic, customer-minded builder who prefers rapid execution over long-term architectural migrations. Key requirements include:
*   Strong coding skills in Python and more performant languages.
*   Deep expertise in OLTP and OLAP databases (specifically Postgres and Clickhouse).
*   First-hand experience scaling high-traffic, data-heavy systems.

**Compensation and Benefits**
*   **Salary:** $180K – $240K.
*   **Equity:** 0.5% – 0.85%.
*   **Benefits:** Private health, dental, and vision insurance, plus 401k/pension contributions.

**Interview Process**
Converge operates with high urgency; the entire hiring process can be completed in just two days. It consists of a 30-minute introductory call, a one-hour technical problem-solving session, a 45-minute culture interview, and a full-day paid "Superday" where the candidate builds a project alongside the founding team.

---

## 9. Show HN: LogClaw – Open-source AI SRE that auto-creates tickets from logs

**原文标题**: Show HN: LogClaw – Open-source AI SRE that auto-creates tickets from logs

**原文链接**: [https://logclaw.ai](https://logclaw.ai)

生成摘要时出错

---

## 10. Asia rolls out 4-day weeks, WFH to solve fuel crisis caused by Iran war

**原文标题**: Asia rolls out 4-day weeks, WFH to solve fuel crisis caused by Iran war

**原文链接**: [https://fortune.com/2026/03/11/iran-war-fuel-crisis-asia-work-from-home-closed-schools-price-caps/](https://fortune.com/2026/03/11/iran-war-fuel-crisis-asia-work-from-home-closed-schools-price-caps/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 2 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 3 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 4 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 5 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 6 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 7 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 8 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 9 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 10 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 11 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 12 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 13 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 14 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 15 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 16 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 17 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 18 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 19 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 20 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 21 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 22 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 23 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 24 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 25 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 26 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 27 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 28 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 29 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 30 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 31 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 32 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 33 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 34 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 35 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 36 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 37 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 38 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 39 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 40 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 41 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 42 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 43 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 44 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 45 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 46 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 47 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 48 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 49 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 50 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 51 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 52 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 53 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 54 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 55 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 56 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 57 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 58 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 59 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 60 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 61 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 62 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 63 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 64 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 65 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 66 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 67 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 68 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 69 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 70 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 71 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 72 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 73 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 74 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 75 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 76 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 77 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 78 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 79 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 80 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 81 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 82 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 83 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 84 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 85 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 86 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 87 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 88 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 89 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 90 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 91 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 92 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 93 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 94 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 95 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 96 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 97 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 98 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 99 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 100 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 101 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 102 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 103 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 104 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 105 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 106 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 107 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 108 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 109 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 110 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 111 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 112 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 113 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 114 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 115 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 116 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 117 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 118 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 119 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 120 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 121 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 122 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 123 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 124 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 125 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 126 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 127 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 128 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 129 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 130 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 131 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 132 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 133 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 134 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 135 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 136 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 137 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 138 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 139 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 140 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 141 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 142 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 143 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 144 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 145 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 146 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 147 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 148 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 149 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 150 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 151 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 152 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 153 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 154 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 155 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 156 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 157 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 158 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 159 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 160 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 161 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 162 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 163 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 164 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 165 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 166 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 167 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 168 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 169 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 170 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 171 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 172 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 173 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 174 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 175 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 176 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 177 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 178 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 179 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 180 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 181 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 182 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 183 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 184 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 185 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 186 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 187 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 188 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 189 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 190 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 191 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 192 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 193 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 194 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 195 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 196 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 197 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 198 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 199 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 200 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 201 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 202 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 203 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 204 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 205 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 206 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 207 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 208 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 209 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 210 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 211 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 212 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 213 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 214 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 215 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 216 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 217 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 218 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 219 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 220 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 221 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 222 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 223 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 224 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 225 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 226 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 227 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 228 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 229 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 230 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 231 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 232 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 233 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 234 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 235 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 236 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 237 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 238 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 239 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 240 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 241 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 242 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 243 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 244 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 245 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 246 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 247 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 248 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 249 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 250 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 251 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 252 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 253 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 254 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 255 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 256 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 257 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 258 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 259 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 260 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 261 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 262 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 263 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 264 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 265 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 266 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 267 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 268 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 269 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 270 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 271 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 272 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 273 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 274 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 275 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 276 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 277 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 278 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 279 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 280 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 281 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 282 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 283 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 284 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 285 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 286 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 287 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 288 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 289 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 290 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 291 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 292 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 293 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 294 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 295 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 296 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 297 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 298 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 299 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 300 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 301 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 302 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 303 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 304 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 305 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 306 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 307 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 308 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 309 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 310 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 311 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 312 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 313 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 314 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 315 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 316 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 317 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 318 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 319 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 320 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 321 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 322 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 323 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 324 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 325 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 326 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 327 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 328 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 329 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 330 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 331 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 332 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 333 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 334 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 335 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 336 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 337 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 338 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 339 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 340 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 341 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 342 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 343 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 344 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 345 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 346 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 347 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 348 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 349 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 350 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 351 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 352 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 353 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 354 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 355 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 356 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 357 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
