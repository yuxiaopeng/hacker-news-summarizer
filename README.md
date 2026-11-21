# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-21.md)

*最后自动更新时间: 2026-11-21 22:28:56*
## 1. 胰腺癌治疗药物被誉为“数十年来最大突破”

**原文标题**: Pill to treat pancreatic cancer hailed as 'biggest breakthrough in decades'

**原文链接**: [https://www.theguardian.com/society/2026/nov/20/pill-pancreatic-cancer-breakthrough-daraxonrasib](https://www.theguardian.com/society/2026/nov/20/pill-pancreatic-cancer-breakthrough-daraxonrasib)

一种名为 **daraxonrasib** 的新药被誉为几十年来胰腺癌治疗领域最重大的突破。这种作为 KRAS 抑制剂的口服药物，通过阻断驱动肿瘤生长的特定基因突变发挥作用。

在一项涉及 61 名晚期转移性胰腺癌患者的临床试验中，其结果对于这种通常预后极差的疾病来说是前所未有的：

*   **生存率：** 76.6% 的患者在开始治疗一年后仍然存活，较之仅接受化疗通常 40–45% 的生存率几乎翻了一番。
*   **肿瘤控制：** 90% 的受试者肿瘤停止生长，超过 60% 的患者肿瘤缩小或消失。
*   **癌症检测不到：** 约 8%（十二分之一）的患者在试验期间，其体内的癌细胞在 CT 扫描中已无法检出。

纪念斯隆-凯特琳癌症中心的 Wungki Park 博士将这些结果描述为他在晚期病例中所见过的“最接近治愈”的表现，并指出该药物比以往的治疗方案提供了更深层且更持久的缓解。专家认为，这种药物最终可能用于治疗携带类似 KRAS 突变的其他类型癌症。

尽管这些结果被视为一次重大的“飞跃”，但卫生官员强调，该药物尚未被视为最终的治愈方案。研究人员目前尚不清楚该药物能控制疾病多久，仍需进行更长期的研究以确定它是否能带来永久性缓解。在英国国民医疗服务体系（NHS）等医疗系统批准其广泛使用之前，还需要进行进一步的临床试验。

---

## 2. Inkling-2-Mini 仅需 5.4 GB 内存

**原文标题**: Inkling-2-Mini in 5.4 GB Memory

**原文链接**: [https://github.com/ShinMegamiBoson/lookatmyquant](https://github.com/ShinMegamiBoson/lookatmyquant)

**LookAtMyQuant (LAMQ)** 是一款开源量化编译器和运行时，旨在压缩大语言模型（LLM），且其性能损耗显著低于传统方法。通过“测量-分配-构建”（measure-allocate-build）的工作流，LAMQ 会计算每个模型组件的压缩对输出质量（KL 散度）的影响，并利用 Fisher 信息在特定的大小预算内实现最优比特分配。

文章的核心亮点包括：
*   **Inkling-2-Mini：** 这款主打的 26.4B MoE 模型被压缩至 5.4 GB（1.63 bits/weight）和 8.9 GB（2.69 bits/weight）。其中 5.4 GB 版本在数学和编程基准测试中的表现优于 9.14 GB 的同类竞品，且在 Apple Silicon 上运行高效。
*   **通义千问 (Qwen) 系列：** Qwen3.8-27B 从 53.7 GB 缩减至 7.2 GB，数学性能与原版持平，且在 MMLU 和 HumanEval 上的得分超过了其他量化版本。Qwen3.5-4B 被缩小至 1.23 GB，保留了原版 92% 的数学解题准确率。
*   **技术创新：** 其“方案”包括格形码（trellis codes）、e-means 码本以及“SQYFR”近端微调/蒸馏。近期引入的 Softmax-Fisher Token 排序等改进进一步降低了误差率。
*   **Apple Silicon 优化：** LAMQ 拥有专门的 `runtime_mlx`，配备自定义 Metal 内核、FlashAttention-2 以及使用“草稿”（drafter）模型的推测解码。在 M5 Max 上，这些优化使 5.4 GB 的 Inkling 模型解码速度高达 142 tokens/秒。

该项目采用 MIT 协议开源，提供 Python API 和命令行工具，方便用户量化自有模型或运行 Hugging Face 上的预压缩版本。总体而言，LAMQ 证明了通过精细的比特分配和蒸馏，高倍率压缩（接近每权重 2 比特）仍能保持接近原版的模型智能。

---

## 3. 黎曼猜想的 Lean 验证

**原文标题**: Lean verification of the Riemann Hypothesis

**原文链接**: [https://leanprover-community.github.io/blog/posts/riemann-hypothesis/](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)

2026年11月20日，Lean与Mathlib社区正式认证了由Levent Alpöge完成的黎曼猜想（RH）形式化证明。该证明是一个包含1700万行代码的Lean库，通过了基于以下四个关键标准的严苛验证过程：

1.  **命题准确性：** 专家确认所证明的定理与Mathlib中黎曼猜想的官方定义完全一致。
2.  **编译成功：** 该库实现了无错编译，且结果已由数十名独立用户成功复现。
3.  **命题对应性：** 社区利用`comparator`和`con-leche`等独立比较工具，验证了Alpöge的证明目标确为黎曼猜想的精确表述，并排除了潜在的恶意代码。
4.  **逻辑有效性：** 导出的证明已通过多个独立内核的验证，包括Lean官方内核以及经过形式化验证的检查器*con-leche*和*con-ron*。这些外部检查器提供了形式化保证，确保该证明未利用Lean自身逻辑中的任何潜在漏洞。

这一里程碑式成果得到了Lean FRO和Mathlib Initiative的认可，通过人工审核与自动化交叉验证确认了证明的正确性。数学界目前计划重点分析并解读Alpöge庞大代码库中所蕴含的新理论见解。

---

## 4. 引爆一堆叠氮化铅

**原文标题**: Detonating a pile of lead azide

**原文链接**: [https://www.science.org/content/blog-post/detonating-huge-pile-lead-azide-really](https://www.science.org/content/blog-post/detonating-huge-pile-lead-azide-really)

在《正在研发中》（In the Pipeline）博客的这篇文章中，德里克·洛（Derek Lowe）讨论了叠氮化铅这一高度敏感的起爆药及其令人畏惧的特性与历史。虽然叠氮化铅因其能瞬间从燃烧转为爆轰的特性而成为雷管的标准组件，但它也因极度不稳定且对撞击、摩擦和静电释放极其敏感而臭名昭著。

文章的核心是关于德国诺贝尔动力公司（Dynamit Nobel）工厂一次大规模处置行动的历史记录。在多年的生产过程中，一个专门的水下储存坑中积聚了大量废弃叠氮化铅，估计达100公斤。由于这些物质过于危险，无法移动或处理，当局决定对其进行原位引爆。

尽管该物质被淹没在数米深的水下，但爆炸产生的威力远超预期。爆轰产生的巨大冲击波震碎了周边地区的窗户，这冷酷地提醒人们，当起爆药的规模扩大时，其物理特性是难以预测的。

洛利用这一轶事强调了实验室和工业安全中的一个关键教训：绝不要让危险废物积压。他强调，虽然少量的叠氮化铅尚可控，但“质量效应”会彻底改变危险程度。这篇文章是一则警示录，揭示了在处理本质上不稳定的物质时，可控的化学实验是如何演变成不可控的大规模灾难的。

---

## 5. 巴西税务局在 GitHub 上以 MIT 协议开源其税务计算器。

**原文标题**: Brazil's tax authority open-sources its tax calculator on GitHub under MIT

**原文链接**: [https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/novembro/receita-federal-publica-primeiro-codigo-fonte-aberto-no-github-e-amplia-transparencia-da-reforma-tributaria](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/novembro/receita-federal-publica-primeiro-codigo-fonte-aberto-no-github-e-amplia-transparencia-da-reforma-tributaria)

巴西联邦税务局（Receita Federal）在 GitHub 上正式发布了其首个开源项目，标志着该国在推动政府透明度方面迈出了重要里程碑。该项目包含了用于计算新税改影响的模拟器源代码。

**关键信息：**

*   **开源与许可：** 代码采用 MIT 许可证发布，这是最宽松的开源协议之一。这允许公民、企业和研究人员自由地使用、复制、修改和分发该软件。
*   **透明度：** 通过公开税务计算背后的“引擎”，政府旨在确保向新税制（IBS 和 CBS）过渡过程的完全透明。社会各界现在可以独立验证和审计税务机关所使用的数学逻辑及预测数据。
*   **范围：** 该代码库专门针对双重增值税（VAT）模型。它有助于展示在为期数年的过渡期内税收负担如何转移，从而让公众更清晰地理解改革的实际影响。
*   **协作开发：** 在 GitHub 上托管项目标志着巴西政府向更现代、更具协作性的“DevOps”文化转型。它允许全球开发者社区识别漏洞、提出优化建议，并为该工具的演进做出贡献。
*   **公众信任：** 该倡议是政府“开放数据”战略的核心，旨在通过从私有的“黑箱”系统转向可验证的公益软件，增强公众对税改进程的信任。

此举使巴西税务局成为数字化转型的领军者，利用开放技术简化并阐明了该国复杂的财政格局。

---

## 6. 让心智驾驭身体，从而指引自我。

**原文标题**: Getting the mind to steer the body to steer you

**原文链接**: [https://notnottalmud.substack.com/p/getting-the-mind-to-steer-the-body](https://notnottalmud.substack.com/p/getting-the-mind-to-steer-the-body)

在《让心智引导身体来引导你》一文中，作者探讨了有意识的“飞行员”（心智）与生物性的“容器”（身体及其潜意识系统）之间的动态关系。其核心论点是：意志力是一种有限的资源，试图通过意识层面的努力来“硬刚”行为，通常是一种注定失败的策略。

文章指出，由激素、睡眠、环境和习惯决定的身体状态，实际上主宰了我们的大部分选择和情绪。因此，心智最有效的角色并非充当持续的驾驶员，而是扮演战略建筑师。心智不应与身体的倾向对抗，而应专注于“元引导”（meta-steering）：通过操纵环境和生物输入，确保身体的“自动驾驶模式”自然地向预定方向移动。

核心要点包括：
*   **意志力差距**：从长期来看，有意识的心智往往过于脆弱，无法凌驾于身体的生理需求或根深蒂固的习惯之上。
*   **系统设计**：有效的改变源于对外部变量的调整（如清除工作区的干扰或利用社交压力），而非盲目地“更加努力”。
*   **生物基础**：管理睡眠、运动和营养等生理输入也是一种引导方式，因为这些因素决定了“飞行员”必须面对的心理“天气”。

最终，作者指出，自我提升的秘诀在于建立一种反馈循环：心智引导身体所处的环境，而由此产生的身体状态则以最小的阻力“引导”人走向目标。成功的关键在于设计一种生活，让做“正确”的事成为身体阻力最小的路径。

---

## 7. PostgreSQL Extensions in Go

**原文标题**: PostgreSQL Extensions in Go

**原文链接**: [https://jespino.github.io/gopgext/](https://jespino.github.io/gopgext/)

**gopgext** 是一款实验性工具，旨在通过 TinyGo 编译器使用 Go 语言构建 PostgreSQL 扩展。它允许开发人员使用纯 Go 编写扩展，并通过 `//gopgext:function` 等特定指令自动生成 C 语言胶水代码、安装脚本和控制文件。

**主要特性与功能：**
*   **语言支持：** 支持大部分 Go 标准库（包括 `fmt`、`regexp`、`json` 和 `crypto`），以及泛型和迭代器等现代特性。
*   **数据库集成：** 该工具将 Go 类型（字符串、数字、数组、JSON、UUID 等）映射为 SQL 类型。它使开发人员能够通过 SPI 执行 SQL、处理触发器、定义聚合函数，并创建复杂的索引访问方法（如 GIN、GiST、BRIN）或外部数据包装器（FDW）。
*   **安全性与共存：** 多个基于 Go 的扩展可以在同一个后端进程中运行。系统确保 PostgreSQL 错误不会穿透 Go 栈帧，并保证数据安全地复制到 PostgreSQL 内存中。
*   **逻辑验证：** 为了证明其可行性，该项目已成功移植了多个 PostgreSQL `contrib` 模块（如 `pgcrypto` 和 `hstore`），并通过了它们原始的上游回归测试。

**状态与风险：**
该项目目前处于**实验阶段**，不建议用于生产环境。由于 Go 运行时直接在 PostgreSQL 服务端内部运行，生成的代码或运行时中的任何错误都可能导致服务器崩溃或数据损坏。

**工作流：**
通过类似于标准 Go 工具的命令行界面（CLI），开发人员可以初始化项目（`gopgext init`）并进行安装（`gopgext install`）。此过程会将代码编译为共享对象（`.so`）文件，并将其与 PostgreSQL 构建系统（PGXS）集成。该方案模仿了 `gokm` —— 一个用于使用 Go 构建 Linux 内核模块的兄弟项目。

---

## 8. Tasklet (YC P26) 招聘产品与 Agent 基础架构工程师

**原文标题**: Tasklet (YC P26) Is Hiring Product and Agent Infra Engineers

**原文链接**: [https://tasklet.ai/careers](https://tasklet.ai/careers)

Tasklet (YC P26) is a San Francisco-based startup building an "AI workforce" designed to handle end-to-end business responsibilities—such as accounting, sales pipeline management, and customer support—rather than just answering prompts. Led by Firebase founder Andrew Lee and Jonny Dimond, the 14-person team includes veterans from Google, OpenAI, and Amazon. The company recently raised $42M at a $500M valuation cap from prestigious investors including Union Square Ventures, Lightspeed, and Jeff Dean.

**Open Roles**
Tasklet is hiring for five full-time, in-person positions in their San Francisco office:
*   Head of Design Engineering
*   Software Engineer (Platform)
*   Software Engineer (AI Infra)
*   Software Engineer (Product)
*   Customer Success Engineer

**Application Process**
To apply, candidates must email CEO Andrew Lee (**andrew@tasklet.ai**) with a resume and a video (under five minutes). The video must include:
1.  An introduction and motivation for joining.
2.  Confirmation of full-time, in-person availability in SF (Note: They are **not** sponsoring new visas at this time).
3.  A technical demo of a recent, relevant project that showcases the applicant's skills.

**Culture and Incentives**
Tasklet maintains a high-performance, engineering-driven culture that prioritizes shipping daily and taking extreme ownership. They focus on turning frontier models into dependable "colleagues" through a unified agent harness. Additionally, the company offers a **$20,000 referral bonus** to US residents who recommend a candidate that is successfully hired.

---

## 9. My monitor was cutting my download speed by 75%

**原文标题**: My monitor was cutting my download speed by 75%

**原文链接**: [https://blog.tymscar.com/posts/studiodisplayethernet/](https://blog.tymscar.com/posts/studiodisplayethernet/)

生成摘要时出错

---

## 10. 紧急公告：Alessandro Masullo GRH

**原文标题**: Hurried Announcement: Alessandro Masullo GRH

**原文链接**: [https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-21](output/hacker_news_summary_2026-11-21.md) |
| 2 | [2026-11-19](output/hacker_news_summary_2026-11-19.md) |
| 3 | [2026-11-18](output/hacker_news_summary_2026-11-18.md) |
| 4 | [2026-11-20](output/hacker_news_summary_2026-11-20.md) |
| 5 | [2026-11-17](output/hacker_news_summary_2026-11-17.md) |
| 6 | [2026-11-14](output/hacker_news_summary_2026-11-14.md) |
| 7 | [2026-11-11](output/hacker_news_summary_2026-11-11.md) |
| 8 | [2026-11-15](output/hacker_news_summary_2026-11-15.md) |
| 9 | [2026-11-12](output/hacker_news_summary_2026-11-12.md) |
| 10 | [2026-11-13](output/hacker_news_summary_2026-11-13.md) |
| 11 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 12 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 13 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 14 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 15 | [2026-11-10](output/hacker_news_summary_2026-11-10.md) |
| 16 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 17 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 18 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 19 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 20 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 21 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 22 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 23 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 24 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 25 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 26 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 27 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 28 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 29 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 30 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 31 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 32 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 33 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 34 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 35 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 36 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 37 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 38 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 39 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 40 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 41 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 42 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 43 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 44 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 45 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 46 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 47 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 48 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 49 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 50 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 51 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 52 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 53 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 54 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 55 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 56 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 57 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 58 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 59 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 60 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 61 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 62 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 63 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 64 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 65 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 66 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 67 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 68 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 69 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 70 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 71 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 72 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 73 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 74 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 75 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 76 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 77 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 78 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 79 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 80 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 81 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 82 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 83 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 84 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 85 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 86 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 87 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 88 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 89 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 90 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 91 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 92 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 93 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 94 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 95 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 96 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 97 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 98 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 99 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 100 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 101 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 102 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 103 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 104 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 105 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 106 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 107 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 108 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 109 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 110 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 111 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 112 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 113 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 114 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 115 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 116 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 117 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 118 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 119 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 120 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 121 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 122 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 123 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 124 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 125 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 126 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 127 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 128 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 129 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 130 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 131 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 132 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 133 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 134 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 135 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 136 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 137 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 138 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 139 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 140 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 141 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 142 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 143 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 144 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 145 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 146 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 147 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 148 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 149 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 150 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 151 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 152 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 153 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 154 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 155 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 156 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 157 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 158 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 159 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 160 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 161 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 162 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 163 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 164 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 165 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 166 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 167 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 168 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 169 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 170 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 171 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 172 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 173 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 174 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 175 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 176 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 177 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 178 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 179 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 180 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 181 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 182 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 183 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 184 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 185 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 186 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 187 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 188 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 189 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 190 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 191 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 192 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 193 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 194 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 195 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 196 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 197 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 198 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 199 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 200 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 201 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 202 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 203 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 204 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 205 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 206 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 207 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 208 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 209 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 210 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 211 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 212 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 213 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 214 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 215 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 216 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 217 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 218 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 219 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 220 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 221 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 222 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 223 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 224 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 225 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 226 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 227 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 228 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 229 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 230 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 231 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 232 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 233 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 234 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 235 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 236 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 237 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 238 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 239 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 240 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 241 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 242 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 243 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 244 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 245 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 246 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 247 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 248 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 249 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 250 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 251 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 252 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 253 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 254 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 255 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 256 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 257 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 258 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 259 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 260 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 261 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 262 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 263 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 264 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 265 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 266 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 267 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 268 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 269 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 270 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 271 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 272 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 273 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 274 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 275 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 276 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 277 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 278 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 279 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 280 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 281 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 282 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 283 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 284 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 285 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 286 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 287 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 288 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 289 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 290 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 291 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 292 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 293 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 294 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 295 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 296 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 297 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 298 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 299 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 300 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 301 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 302 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 303 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 304 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 305 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 306 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 307 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 308 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 309 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 310 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 311 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 312 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 313 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 314 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 315 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 316 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 317 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 318 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 319 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 320 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 321 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 322 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 323 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 324 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 325 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 326 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 327 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 328 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 329 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 330 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 331 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 332 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 333 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 334 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 335 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 336 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 337 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 338 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 339 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 340 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 341 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 342 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 343 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 344 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 345 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 346 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 347 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 348 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 349 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 350 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 351 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 352 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 353 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 354 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 355 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 356 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 357 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 358 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 359 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 360 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 361 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 362 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 363 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 364 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 365 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 366 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 367 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 368 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 369 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 370 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 371 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 372 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 373 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 374 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 375 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 376 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 377 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 378 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 379 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 380 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 381 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 382 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 383 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 384 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 385 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 386 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 387 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 388 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 389 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 390 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 391 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 392 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 393 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 394 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 395 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 396 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 397 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 398 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 399 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 400 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 401 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 402 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 403 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 404 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 405 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 406 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 407 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 408 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 409 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 410 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 411 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 412 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 413 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 414 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 415 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 416 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 417 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 418 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 419 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 420 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 421 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 422 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 423 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 424 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 425 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 426 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 427 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 428 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 429 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 430 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 431 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 432 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 433 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 434 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 435 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 436 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 437 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 438 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 439 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 440 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 441 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 442 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 443 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 444 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 445 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 446 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 447 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 448 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 449 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 450 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 451 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 452 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 453 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 454 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 455 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 456 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 457 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 458 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 459 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 460 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 461 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 462 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 463 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 464 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 465 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 466 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 467 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 468 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 469 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 470 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 471 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 472 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 473 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 474 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 475 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 476 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 477 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 478 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 479 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 480 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 481 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 482 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 483 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 484 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 485 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 486 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 487 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 488 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 489 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 490 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 491 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 492 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 493 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 494 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 495 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 496 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 497 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 498 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 499 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 500 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 501 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 502 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 503 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 504 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 505 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 506 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 507 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 508 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 509 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 510 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 511 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 512 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 513 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 514 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 515 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 516 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 517 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 518 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 519 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 520 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 521 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 522 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 523 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 524 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 525 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 526 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 527 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 528 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 529 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 530 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 531 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 532 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 533 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 534 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 535 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 536 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 537 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 538 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 539 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 540 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 541 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 542 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 543 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 544 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 545 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 546 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 547 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 548 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 549 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 550 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 551 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 552 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 553 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 554 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 555 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 556 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 557 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 558 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 559 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 560 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 561 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 562 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 563 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 564 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 565 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 566 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 567 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 568 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 569 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 570 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 571 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 572 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 573 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 574 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 575 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 576 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 577 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 578 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 579 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 580 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 581 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 582 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 583 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 584 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 585 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 586 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 587 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 588 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 589 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 590 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 591 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 592 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 593 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 594 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 595 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 596 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 597 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 598 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 599 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 600 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 601 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 602 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 603 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 604 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 605 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 606 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
