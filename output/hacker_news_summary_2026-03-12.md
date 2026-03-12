# Hacker News 热门文章摘要 (2026-03-12)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. The Cost of Indirection in Rust

**原文标题**: The Cost of Indirection in Rust

**原文链接**: [https://blog.sebastiansastre.co/posts/cost-of-indirection-in-rust/](https://blog.sebastiansastre.co/posts/cost-of-indirection-in-rust/)

生成摘要时出错

---

## 12. Dolphin Progress Release 2603

**原文标题**: Dolphin Progress Release 2603

**原文链接**: [https://dolphin-emu.org/blog/2026/03/12/dolphin-progress-report-release-2603/](https://dolphin-emu.org/blog/2026/03/12/dolphin-progress-report-release-2603/)

生成摘要时出错

---

## 13. Show HN: Understudy – Teach a desktop agent by demonstrating a task once

**原文标题**: Show HN: Understudy – Teach a desktop agent by demonstrating a task once

**原文链接**: [https://github.com/understudy-ai/understudy](https://github.com/understudy-ai/understudy)

生成摘要时出错

---

## 14. Italian prosecutors seek trial for Amazon, 4 execs in alleged $1.4B tax evasion

**原文标题**: Italian prosecutors seek trial for Amazon, 4 execs in alleged $1.4B tax evasion

**原文链接**: [https://www.reuters.com/world/italian-prosecutors-seek-trial-amazon-four-execs-over-alleged-14-bln-tax-evasion-2026-03-12/](https://www.reuters.com/world/italian-prosecutors-seek-trial-amazon-four-execs-over-alleged-14-bln-tax-evasion-2026-03-12/)

生成摘要时出错

---

## 15. Scrt: A CLI secret manager for developers, sysadmins and DevOps

**原文标题**: Scrt: A CLI secret manager for developers, sysadmins and DevOps

**原文链接**: [https://github.com/loderunner/scrt](https://github.com/loderunner/scrt)

生成摘要时出错

---

## 16. Avoiding Trigonometry (2013)

**原文标题**: Avoiding Trigonometry (2013)

**原文链接**: [https://iquilezles.org/articles/noacos/](https://iquilezles.org/articles/noacos/)

生成摘要时出错

---

## 17. Claude now creates interactive charts, diagrams and visualizations

**原文标题**: Claude now creates interactive charts, diagrams and visualizations

**原文链接**: [https://claude.com/blog/claude-builds-visuals](https://claude.com/blog/claude-builds-visuals)

生成摘要时出错

---

## 18. Emacs internals: Tagged pointers vs. C++ std:variant and LLVM (Part 3)

**原文标题**: Emacs internals: Tagged pointers vs. C++ std:variant and LLVM (Part 3)

**原文链接**: [https://thecloudlet.github.io/blog/project/emacs-03/](https://thecloudlet.github.io/blog/project/emacs-03/)

生成摘要时出错

---

## 19. 3D-Knitting: The Ultimate Guide

**原文标题**: 3D-Knitting: The Ultimate Guide

**原文链接**: [https://www.oliver-charles.com/pages/3d-knitting](https://www.oliver-charles.com/pages/3d-knitting)

生成摘要时出错

---

## 20. Full Spectrum and Infrared Photography

**原文标题**: Full Spectrum and Infrared Photography

**原文链接**: [https://timstr.website/blog/fullspectrumphotography.html](https://timstr.website/blog/fullspectrumphotography.html)

生成摘要时出错

---

## 21. Long Overlooked as Crucial to Life, Fungi Start to Get Their Due

**原文标题**: Long Overlooked as Crucial to Life, Fungi Start to Get Their Due

**原文链接**: [https://e360.yale.edu/features/fungi-kingdom](https://e360.yale.edu/features/fungi-kingdom)

生成摘要时出错

---

## 22. ATMs didn't kill bank Teller jobs, but the iPhone did

**原文标题**: ATMs didn't kill bank Teller jobs, but the iPhone did

**原文链接**: [https://davidoks.blog/p/why-the-atm-didnt-kill-bank-teller](https://davidoks.blog/p/why-the-atm-didnt-kill-bank-teller)

生成摘要时出错

---

## 23. Show HN: Web-Based ANSI Art Viewer

**原文标题**: Show HN: Web-Based ANSI Art Viewer

**原文链接**: [https://sure.is/ansi/](https://sure.is/ansi/)

生成摘要时出错

---

## 24. Lf-lean: The frontier of verified software engineering

**原文标题**: Lf-lean: The frontier of verified software engineering

**原文链接**: [https://theorem.dev/blog/lf-lean/](https://theorem.dev/blog/lf-lean/)

生成摘要时出错

---

## 25. The Road Not Taken: A World Where IPv4 Evolved

**原文标题**: The Road Not Taken: A World Where IPv4 Evolved

**原文链接**: [https://owl.billpg.com/ipv4x/](https://owl.billpg.com/ipv4x/)

生成摘要时出错

---

## 26. Apple's MacBook Neo makes repairs easier and cheaper than other MacBooks

**原文标题**: Apple's MacBook Neo makes repairs easier and cheaper than other MacBooks

**原文链接**: [https://arstechnica.com/gadgets/2026/03/more-modular-design-makes-macbook-neo-easier-to-fix-than-other-apple-laptops/](https://arstechnica.com/gadgets/2026/03/more-modular-design-makes-macbook-neo-easier-to-fix-than-other-apple-laptops/)

生成摘要时出错

---

## 27. Suburban school district uses license plate readers to verify student residency

**原文标题**: Suburban school district uses license plate readers to verify student residency

**原文链接**: [https://www.nbcchicago.com/consumer/suburban-school-district-uses-license-plate-readers-to-verify-student-residency/3906703/](https://www.nbcchicago.com/consumer/suburban-school-district-uses-license-plate-readers-to-verify-student-residency/3906703/)

生成摘要时出错

---

## 28. Printf-Tac-Toe

**原文标题**: Printf-Tac-Toe

**原文链接**: [https://github.com/carlini/printf-tac-toe](https://github.com/carlini/printf-tac-toe)

生成摘要时出错

---

## 29. High fidelity font synthesis for CJK languages

**原文标题**: High fidelity font synthesis for CJK languages

**原文链接**: [https://github.com/kaonashi-tyc/zi2zi-JiT](https://github.com/kaonashi-tyc/zi2zi-JiT)

生成摘要时出错

---

## 30. Returning to Rails in 2026

**原文标题**: Returning to Rails in 2026

**原文链接**: [https://www.markround.com/blog/2026/03/05/returning-to-rails-in-2026/](https://www.markround.com/blog/2026/03/05/returning-to-rails-in-2026/)

生成摘要时出错

---

## 31. Returning to Rails in 2026

**原文标题**: Returning to Rails in 2026

**原文链接**: [https://www.markround.com/blog/2026/03/05/returning-to-rails-in-2026/](https://www.markround.com/blog/2026/03/05/returning-to-rails-in-2026/)

生成摘要时出错

---

## 32. Reliable Software in the LLM Era

**原文标题**: Reliable Software in the LLM Era

**原文链接**: [https://quint-lang.org/posts/llm_era](https://quint-lang.org/posts/llm_era)

生成摘要时出错

---

## 33. Big Data on the Cheapest MacBook

**原文标题**: Big Data on the Cheapest MacBook

**原文链接**: [https://duckdb.org/2026/03/11/big-data-on-the-cheapest-macbook](https://duckdb.org/2026/03/11/big-data-on-the-cheapest-macbook)

生成摘要时出错

---

## 34. U.S. to suspend the Jones Act in a bid to curb oil prices

**原文标题**: U.S. to suspend the Jones Act in a bid to curb oil prices

**原文链接**: [https://www.bloomberg.com/news/articles/2026-03-12/trump-administration-set-to-suspend-jones-act-to-tame-oil-prices](https://www.bloomberg.com/news/articles/2026-03-12/trump-administration-set-to-suspend-jones-act-to-tame-oil-prices)

生成摘要时出错

---

## 35. Datahäxan

**原文标题**: Datahäxan

**原文链接**: [https://0dd.company/galleries/witches/7.html](https://0dd.company/galleries/witches/7.html)

生成摘要时出错

---

## 36. Tested: How Many Times Can a DVD±RW Be Rewritten? Methodology and Results

**原文标题**: Tested: How Many Times Can a DVD±RW Be Rewritten? Methodology and Results

**原文链接**: [https://goughlui.com/2026/03/07/tested-how-many-times-can-a-dvd%C2%B1rw-be-rewritten-part-2-methodology-results/](https://goughlui.com/2026/03/07/tested-how-many-times-can-a-dvd%C2%B1rw-be-rewritten-part-2-methodology-results/)

生成摘要时出错

---

## 37. Show HN: We analyzed 1,573 Claude Code sessions to see how AI agents work

**原文标题**: Show HN: We analyzed 1,573 Claude Code sessions to see how AI agents work

**原文链接**: [https://github.com/obsessiondb/rudel](https://github.com/obsessiondb/rudel)

生成摘要时出错

---

## 38. SBCL: A Sanely-Bootstrappable Common Lisp (2008) [pdf]

**原文标题**: SBCL: A Sanely-Bootstrappable Common Lisp (2008) [pdf]

**原文链接**: [https://research.gold.ac.uk/id/eprint/2336/1/sbcl.pdf](https://research.gold.ac.uk/id/eprint/2336/1/sbcl.pdf)

生成摘要时出错

---

## 39. 1B identity records exposed in ID verification data leak

**原文标题**: 1B identity records exposed in ID verification data leak

**原文链接**: [https://www.aol.com/articles/1-billion-identity-records-exposed-152505381.html](https://www.aol.com/articles/1-billion-identity-records-exposed-152505381.html)

生成摘要时出错

---

## 40. ArcaOS 5.1.2 (based on OS/2 Warp 4.52) now available

**原文标题**: ArcaOS 5.1.2 (based on OS/2 Warp 4.52) now available

**原文链接**: [https://www.arcanoae.com/arcaos-5-1-2-now-available/](https://www.arcanoae.com/arcaos-5-1-2-now-available/)

生成摘要时出错

---

## 41. NASA's DART spacecraft changed an asteroid's orbit around the sun

**原文标题**: NASA's DART spacecraft changed an asteroid's orbit around the sun

**原文链接**: [https://www.sciencenews.org/article/spacecraft-changed-asteroid-orbit-nasa](https://www.sciencenews.org/article/spacecraft-changed-asteroid-orbit-nasa)

生成摘要时出错

---

## 42. Show HN: s@: decentralized social networking over static sites

**原文标题**: Show HN: s@: decentralized social networking over static sites

**原文链接**: [http://satproto.org/](http://satproto.org/)

生成摘要时出错

---

## 43. The modern formatting addiction in writing

**原文标题**: The modern formatting addiction in writing

**原文链接**: [https://dynomight.net/formatting/](https://dynomight.net/formatting/)

生成摘要时出错

---

## 44. Faster asin() was hiding in plain sight

**原文标题**: Faster asin() was hiding in plain sight

**原文链接**: [https://16bpp.net/blog/post/faster-asin-was-hiding-in-plain-sight/](https://16bpp.net/blog/post/faster-asin-was-hiding-in-plain-sight/)

生成摘要时出错

---

## 45. AI should not replace people at Atlassian, says CEO

**原文标题**: AI should not replace people at Atlassian, says CEO

**原文链接**: [https://www.heise.de/en/news/Atlassian-CEO-AI-doesn-t-replace-people-here-but-we-re-firing-them-anyway-11208758.html](https://www.heise.de/en/news/Atlassian-CEO-AI-doesn-t-replace-people-here-but-we-re-firing-them-anyway-11208758.html)

生成摘要时出错

---

## 46. Personal Computer by Perplexity

**原文标题**: Personal Computer by Perplexity

**原文链接**: [https://www.perplexity.ai/personal-computer-waitlist](https://www.perplexity.ai/personal-computer-waitlist)

生成摘要时出错

---

## 47. WebPKI and You

**原文标题**: WebPKI and You

**原文链接**: [https://blog.brycekerley.net/2026/03/08/webpki-and-you.html](https://blog.brycekerley.net/2026/03/08/webpki-and-you.html)

生成摘要时出错

---

## 48. Temporal: The 9-year journey to fix time in JavaScript

**原文标题**: Temporal: The 9-year journey to fix time in JavaScript

**原文链接**: [https://bloomberg.github.io/js-blog/post/temporal/](https://bloomberg.github.io/js-blog/post/temporal/)

生成摘要时出错

---

## 49. Show HN: Axe A 12MB binary that replaces your AI framework

**原文标题**: Show HN: Axe A 12MB binary that replaces your AI framework

**原文链接**: [https://github.com/jrswab/axe](https://github.com/jrswab/axe)

生成摘要时出错

---

## 50. First 6 days of Iran war cost $11.3B

**原文标题**: First 6 days of Iran war cost $11.3B

**原文链接**: [https://www.nbcnews.com/politics/congress/first-6-days-iran-war-cost-11-billion-pentagon-tells-senators-rcna263060](https://www.nbcnews.com/politics/congress/first-6-days-iran-war-cost-11-billion-pentagon-tells-senators-rcna263060)

生成摘要时出错

---

## 51. Colon cancer now leading cause of cancer deaths under 50 in US

**原文标题**: Colon cancer now leading cause of cancer deaths under 50 in US

**原文链接**: [https://www.theguardian.com/us-news/2026/mar/12/colon-cancer-leading-deaths](https://www.theguardian.com/us-news/2026/mar/12/colon-cancer-leading-deaths)

生成摘要时出错

---

## 52. Many SWE-bench-Passing PRs would not be merged

**原文标题**: Many SWE-bench-Passing PRs would not be merged

**原文链接**: [https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/](https://metr.org/notes/2026-03-10-many-swe-bench-passing-prs-would-not-be-merged-into-main/)

生成摘要时出错

---

## 53. Making WebAssembly a first-class language on the Web

**原文标题**: Making WebAssembly a first-class language on the Web

**原文链接**: [https://hacks.mozilla.org/2026/02/making-webassembly-a-first-class-language-on-the-web/](https://hacks.mozilla.org/2026/02/making-webassembly-a-first-class-language-on-the-web/)

生成摘要时出错

---

## 54. How we hacked McKinsey's AI platform

**原文标题**: How we hacked McKinsey's AI platform

**原文链接**: [https://codewall.ai/blog/how-we-hacked-mckinseys-ai-platform](https://codewall.ai/blog/how-we-hacked-mckinseys-ai-platform)

生成摘要时出错

---

## 55. 5,200 holes carved into a Peruvian mountain left by an ancient economy

**原文标题**: 5,200 holes carved into a Peruvian mountain left by an ancient economy

**原文链接**: [https://newatlas.com/environment/5-200-holes-peruvian-mountain/](https://newatlas.com/environment/5-200-holes-peruvian-mountain/)

生成摘要时出错

---

## 56. Swiss e-voting pilot can't count 2,048 ballots after decryption failure

**原文标题**: Swiss e-voting pilot can't count 2,048 ballots after decryption failure

**原文链接**: [https://www.theregister.com/2026/03/11/swiss_evote_usb_snafu/](https://www.theregister.com/2026/03/11/swiss_evote_usb_snafu/)

生成摘要时出错

---

## 57. They Came to Spy on America. They Stayed to Coach Little League

**原文标题**: They Came to Spy on America. They Stayed to Coach Little League

**原文链接**: [https://www.politico.com/news/magazine/2026/03/07/soviet-spy-america-cold-war-00755831](https://www.politico.com/news/magazine/2026/03/07/soviet-spy-america-cold-war-00755831)

生成摘要时出错

---

## 58. Tony Hoare has died

**原文标题**: Tony Hoare has died

**原文链接**: [https://blog.computationalcomplexity.org/2026/03/tony-hoare-1934-2026.html](https://blog.computationalcomplexity.org/2026/03/tony-hoare-1934-2026.html)

生成摘要时出错

---

## 59. I was interviewed by an AI bot for a job

**原文标题**: I was interviewed by an AI bot for a job

**原文链接**: [https://www.theverge.com/featured-video/892850/i-was-interviewed-by-an-ai-bot-for-a-job](https://www.theverge.com/featured-video/892850/i-was-interviewed-by-an-ai-bot-for-a-job)

生成摘要时出错

---

## 60. About memory pressure, lock contention, and Data-oriented Design

**原文标题**: About memory pressure, lock contention, and Data-oriented Design

**原文链接**: [https://mnt.io/articles/about-memory-pressure-lock-contention-and-data-oriented-design/](https://mnt.io/articles/about-memory-pressure-lock-contention-and-data-oriented-design/)

生成摘要时出错

---

## 61. Easy-to-use solar panels are coming, but utilities are trying to delay them

**原文标题**: Easy-to-use solar panels are coming, but utilities are trying to delay them

**原文链接**: [https://www.npr.org/2026/03/12/nx-s1-5737287/solar-panels-utilities-energy-saving](https://www.npr.org/2026/03/12/nx-s1-5737287/solar-panels-utilities-energy-saving)

生成摘要时出错

---

## 62. 50 Years of Thinking Different

**原文标题**: 50 Years of Thinking Different

**原文链接**: [https://www.apple.com/50-years-of-thinking-different/](https://www.apple.com/50-years-of-thinking-different/)

生成摘要时出错

---

## 63. Show HN: Calyx – Ghostty-Based macOS Terminal with Liquid Glass UI

**原文标题**: Show HN: Calyx – Ghostty-Based macOS Terminal with Liquid Glass UI

**原文链接**: [https://github.com/yuuichieguchi/Calyx](https://github.com/yuuichieguchi/Calyx)

生成摘要时出错

---

## 64. Against vibes: When is a generative model useful

**原文标题**: Against vibes: When is a generative model useful

**原文链接**: [https://www.williamjbowman.com/blog/2026/03/05/against-vibes-when-is-a-generative-model-useful/](https://www.williamjbowman.com/blog/2026/03/05/against-vibes-when-is-a-generative-model-useful/)

生成摘要时出错

---

## 65. Thinnings: Sublist Witnesses and de Bruijn Index Shift Clumping

**原文标题**: Thinnings: Sublist Witnesses and de Bruijn Index Shift Clumping

**原文链接**: [https://www.philipzucker.com/thin1/](https://www.philipzucker.com/thin1/)

生成摘要时出错

---

## 66. Building a TB-303 from Scratch

**原文标题**: Building a TB-303 from Scratch

**原文链接**: [https://loopmaster.xyz/tutorials/tb303-from-scratch](https://loopmaster.xyz/tutorials/tb303-from-scratch)

生成摘要时出错

---

## 67. Galaxy Zoo

**原文标题**: Galaxy Zoo

**原文链接**: [https://www.zooniverse.org/projects/zookeeper/galaxy-zoo](https://www.zooniverse.org/projects/zookeeper/galaxy-zoo)

生成摘要时出错

---

## 68. The MacBook Neo

**原文标题**: The MacBook Neo

**原文链接**: [https://daringfireball.net/2026/03/the_macbook_neo](https://daringfireball.net/2026/03/the_macbook_neo)

生成摘要时出错

---

## 69. CNN Explainer – Learn Convolutional Neural Network in Your Browser (2020)

**原文标题**: CNN Explainer – Learn Convolutional Neural Network in Your Browser (2020)

**原文链接**: [https://poloclub.github.io/cnn-explainer/](https://poloclub.github.io/cnn-explainer/)

生成摘要时出错

---

## 70. Don't post generated/AI-edited comments. HN is for conversation between humans

**原文标题**: Don't post generated/AI-edited comments. HN is for conversation between humans

**原文链接**: [https://news.ycombinator.com/newsguidelines.html#generated](https://news.ycombinator.com/newsguidelines.html#generated)

生成摘要时出错

---

## 71. Britain is ejecting hereditary nobles from Parliament after 700 years

**原文标题**: Britain is ejecting hereditary nobles from Parliament after 700 years

**原文链接**: [https://apnews.com/article/uk-house-of-lords-hereditary-peers-expelled-535df8781dd01e8970acda1dca99d3d4](https://apnews.com/article/uk-house-of-lords-hereditary-peers-expelled-535df8781dd01e8970acda1dca99d3d4)

生成摘要时出错

---

## 72. Show HN: Open-source browser for AI agents

**原文标题**: Show HN: Open-source browser for AI agents

**原文链接**: [https://github.com/theredsix/agent-browser-protocol](https://github.com/theredsix/agent-browser-protocol)

生成摘要时出错

---

## 73. The purpose of Continuous Integration is to fail

**原文标题**: The purpose of Continuous Integration is to fail

**原文链接**: [https://blog.nix-ci.com/post/2026-02-05_the-purpose-of-ci-is-to-fail](https://blog.nix-ci.com/post/2026-02-05_the-purpose-of-ci-is-to-fail)

生成摘要时出错

---

## 74. Iran Includes American Tech Giants on List of New Targets

**原文标题**: Iran Includes American Tech Giants on List of New Targets

**原文链接**: [https://gizmodo.com/iran-includes-american-tech-giants-on-list-of-new-targets-2000732530](https://gizmodo.com/iran-includes-american-tech-giants-on-list-of-new-targets-2000732530)

生成摘要时出错

---

## 75. Newcomb's Paradox Needs a Demon

**原文标题**: Newcomb's Paradox Needs a Demon

**原文链接**: [https://samestep.com/blog/newcombs-paradox/](https://samestep.com/blog/newcombs-paradox/)

生成摘要时出错

---

## 76. Physicist Astrid Eichhorn is a leader in the field of asymptotic safety

**原文标题**: Physicist Astrid Eichhorn is a leader in the field of asymptotic safety

**原文链接**: [https://www.quantamagazine.org/where-some-see-strings-she-sees-a-space-time-made-of-fractals-20260311/](https://www.quantamagazine.org/where-some-see-strings-she-sees-a-space-time-made-of-fractals-20260311/)

生成摘要时出错

---

## 77. Show HN: Autoresearch@home

**原文标题**: Show HN: Autoresearch@home

**原文链接**: [https://www.ensue-network.ai/autoresearch](https://www.ensue-network.ai/autoresearch)

生成摘要时出错

---

## 78. Challenging the Single-Responsibility Principle

**原文标题**: Challenging the Single-Responsibility Principle

**原文链接**: [https://kiss-and-solid.com/blog/keep-it-simple](https://kiss-and-solid.com/blog/keep-it-simple)

生成摘要时出错

---

## 79. Show HN: I built a tool that watches webpages and exposes changes as RSS

**原文标题**: Show HN: I built a tool that watches webpages and exposes changes as RSS

**原文链接**: [https://sitespy.app](https://sitespy.app)

生成摘要时出错

---

## 80. BitNet: Inference framework for 1-bit LLMs

**原文标题**: BitNet: Inference framework for 1-bit LLMs

**原文链接**: [https://github.com/microsoft/BitNet](https://github.com/microsoft/BitNet)

生成摘要时出错

---

## 81. Google closes deal to acquire Wiz

**原文标题**: Google closes deal to acquire Wiz

**原文链接**: [https://www.wiz.io/blog/google-closes-deal-to-acquire-wiz](https://www.wiz.io/blog/google-closes-deal-to-acquire-wiz)

生成摘要时出错

---

## 82. Urea prices

**原文标题**: Urea prices

**原文链接**: [https://tradingeconomics.com/commodity/urea](https://tradingeconomics.com/commodity/urea)

生成摘要时出错

---

## 83. Human Organ Atlas

**原文标题**: Human Organ Atlas

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.adz2240](https://www.science.org/doi/10.1126/sciadv.adz2240)

生成摘要时出错

---

## 84. The Isolation Trap: Erlang

**原文标题**: The Isolation Trap: Erlang

**原文链接**: [https://causality.blog/essays/the-isolation-trap/](https://causality.blog/essays/the-isolation-trap/)

生成摘要时出错

---

## 85. Entities enabling scientific fraud at scale (2025)

**原文标题**: Entities enabling scientific fraud at scale (2025)

**原文链接**: [https://doi.org/10.1073/pnas.2420092122](https://doi.org/10.1073/pnas.2420092122)

生成摘要时出错

---

## 86. I'm glad the Anthropic fight is happening now

**原文标题**: I'm glad the Anthropic fight is happening now

**原文链接**: [https://www.dwarkesh.com/p/dow-anthropic](https://www.dwarkesh.com/p/dow-anthropic)

生成摘要时出错

---

## 87. Show HN: A context-aware permission guard for Claude Code

**原文标题**: Show HN: A context-aware permission guard for Claude Code

**原文链接**: [https://github.com/manuelschipper/nah/](https://github.com/manuelschipper/nah/)

生成摘要时出错

---

## 88. Show HN: Vanilla JavaScript refinery simulator built to explain job to my kids

**原文标题**: Show HN: Vanilla JavaScript refinery simulator built to explain job to my kids

**原文链接**: [https://fuelingcuriosity.com/game.html](https://fuelingcuriosity.com/game.html)

生成摘要时出错

---

## 89. Launch HN: Prism (YC X25) – Workspace and API to generate and edit videos

**原文标题**: Launch HN: Prism (YC X25) – Workspace and API to generate and edit videos

**原文链接**: [https://www.prismvideos.com](https://www.prismvideos.com)

生成摘要时出错

---

## 90. Preliminary data from a longitudinal AI impact study

**原文标题**: Preliminary data from a longitudinal AI impact study

**原文链接**: [https://newsletter.getdx.com/p/ai-productivity-gains-are-10-not](https://newsletter.getdx.com/p/ai-productivity-gains-are-10-not)

生成摘要时出错

---

## 91. Silicon Valley's New Obsession: Watching Bots Do Their Grunt Work

**原文标题**: Silicon Valley's New Obsession: Watching Bots Do Their Grunt Work

**原文链接**: [https://www.wsj.com/tech/ai/ai-bots-claude-openclaw-285ac816](https://www.wsj.com/tech/ai/ai-bots-claude-openclaw-285ac816)

生成摘要时出错

---

## 92. Show HN: XLA-based array computing framework for R

**原文标题**: Show HN: XLA-based array computing framework for R

**原文链接**: [https://github.com/r-xla/anvil](https://github.com/r-xla/anvil)

生成摘要时出错

---

## 93. Apple to celebrate 50 years of thinking different

**原文标题**: Apple to celebrate 50 years of thinking different

**原文链接**: [https://www.apple.com/newsroom/2026/03/apple-to-celebrate-50-years-of-thinking-different/](https://www.apple.com/newsroom/2026/03/apple-to-celebrate-50-years-of-thinking-different/)

生成摘要时出错

---

## 94. Julia Snail – An Emacs Development Environment for Julia Like Clojure's Cider

**原文标题**: Julia Snail – An Emacs Development Environment for Julia Like Clojure's Cider

**原文链接**: [https://github.com/gcv/julia-snail](https://github.com/gcv/julia-snail)

生成摘要时出错

---

## 95. U.S. Navy Turns Down Hormuz Escort Requests Because of High Risk

**原文标题**: U.S. Navy Turns Down Hormuz Escort Requests Because of High Risk

**原文链接**: [https://maritime-executive.com/article/u-s-navy-turns-down-strait-of-hormuz-escort-requests-because-of-high-risk](https://maritime-executive.com/article/u-s-navy-turns-down-strait-of-hormuz-escort-requests-because-of-high-risk)

生成摘要时出错

---

## 96. Iran appears to have conducted a significant cyberattack against a U.S. company

**原文标题**: Iran appears to have conducted a significant cyberattack against a U.S. company

**原文链接**: [https://www.nbcnews.com/world/iran/iran-appears-conducted-significant-cyberattack-us-company-first-war-st-rcna263084](https://www.nbcnews.com/world/iran/iran-appears-conducted-significant-cyberattack-us-company-first-war-st-rcna263084)

生成摘要时出错

---

## 97. Launch HN: Sentrial (YC W26) – Catch AI agent failures before your users do

**原文标题**: Launch HN: Sentrial (YC W26) – Catch AI agent failures before your users do

**原文链接**: [https://www.sentrial.com/](https://www.sentrial.com/)

生成摘要时出错

---

## 98. Create value for others and don’t worry about the returns

**原文标题**: Create value for others and don’t worry about the returns

**原文链接**: [https://geohot.github.io//blog/jekyll/update/2026/03/11/running-69-agents.html](https://geohot.github.io//blog/jekyll/update/2026/03/11/running-69-agents.html)

生成摘要时出错

---

## 99. Lego's 0.002mm specification and its implications for manufacturing (2025)

**原文标题**: Lego's 0.002mm specification and its implications for manufacturing (2025)

**原文链接**: [https://www.thewave.engineer/articles.html/productivity/legos-0002mm-specification-and-its-implications-for-manufacturing-r120/](https://www.thewave.engineer/articles.html/productivity/legos-0002mm-specification-and-its-implications-for-manufacturing-r120/)

生成摘要时出错

---

## 100. Chardet dispute shows how AI will kill software licensing

**原文标题**: Chardet dispute shows how AI will kill software licensing

**原文链接**: [https://www.theregister.com/2026/03/06/ai_kills_software_licensing/](https://www.theregister.com/2026/03/06/ai_kills_software_licensing/)

生成摘要时出错

---

