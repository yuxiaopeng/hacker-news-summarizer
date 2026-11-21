# Hacker News 热门文章摘要 (2026-11-21)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Tropical Rainforests Species may be surprisingly young

**原文标题**: Tropical Rainforests Species may be surprisingly young

**原文链接**: [https://phys.org/news/2026-11-species-tropical-rainforests-young-emergence.html](https://phys.org/news/2026-11-species-tropical-rainforests-young-emergence.html)

生成摘要时出错

---

## 12. Upload2Shell · CVE-2026-125396

**原文标题**: Upload2Shell · CVE-2026-125396

**原文链接**: [https://pwn.ai/upload2shell](https://pwn.ai/upload2shell)

The article "Upload2Shell · CVE-2026-125396" on pwn.ai details a critical vulnerability demonstrating how an unrestricted file upload flaw can be escalated to Remote Code Execution (RCE). Although the CVE ID is futuristic/simulated, the article serves as a technical breakdown of a common web security threat.

**Key Points:**

*   **The Vulnerability:** The flaw exists in a web application’s file upload feature, which fails to properly validate user-supplied files. While the interface may imply it only accepts images, it lacks server-side checks to enforce these restrictions.
*   **Exploitation Process:** An attacker can bypass client-side filters to upload a malicious script (such as a PHP web shell). Because the server stores these uploads in a web-accessible directory and the web server is configured to execute scripts in that location, the attacker can trigger the malicious code by simply navigating to the file's URL.
*   **Impact:** Successful exploitation allows an attacker to execute arbitrary commands on the host server. This provides a "shell," leading to total system compromise, unauthorized data access, and the potential for lateral movement within the network.
*   **Mitigation Strategies:** The article emphasizes several layers of defense:
    1.  **Allowlisting:** Only permit specific, safe file extensions rather than trying to block "bad" ones.
    2.  **File Validation:** Use "magic bytes" (header checks) to verify that the file content matches its extension.
    3.  **Storage Security:** Store uploaded files outside of the web root or on a dedicated storage server with execution permissions disabled.
    4.  **Filename Randomization:** Rename files upon upload to prevent attackers from easily guessing the path to their payload.

In summary, the article highlights that file upload features are high-risk components that require rigorous multi-layered validation to prevent attackers from gaining full control over a server.

---

## 13. Exponential Behavior in Magic: The Gathering

**原文标题**: Exponential Behavior in Magic: The Gathering

**原文链接**: [https://levineuwirth.org/essays/exponential-magic/](https://levineuwirth.org/essays/exponential-magic/)

生成摘要时出错

---

## 14. Verification files for the Lean proof of the Riemann Hypothesis

**原文标题**: Verification files for the Lean proof of the Riemann Hypothesis

**原文链接**: [https://math.mit.edu/~drew/grh/](https://math.mit.edu/~drew/grh/)

On November 20, 2026, Andrew Sutherland (MIT) announced the successful formal verification of a Lean 4 proof of the Riemann Hypothesis (RH) and the Generalized Riemann Hypothesis (GRH) for Dirichlet L-functions. The verification process, conducted using "Claude Code" and multiple independent kernels, confirms that the proof is logically sound and relies solely on Lean’s three standard axioms (*propext*, *Classical.choice*, and *Quot.sound*).

The verification covered five headline theorems, including the standard Riemann Hypothesis and GRH for both primitive and non-primitive Dirichlet characters. To ensure the proof's mathematical consistency beyond Lean’s internal definitions, Sutherland’s team combined the proof with the independent "Robin1984" formalization. This successfully produced verified proofs of Robin’s and Lagarias’s inequalities regarding divisor sums, which are known to be equivalent to RH.

Key technical details include:
*   **Scale:** The proof comprises 175,187 modules and an exported proof file of approximately 61.6 GB.
*   **Kernel Validation:** The proof was accepted by multiple independent kernels, including *nanoda* (Rust) and *con-leche*, as well as the *lean4lean* checker.
*   **Integrity:** Statement matching confirmed that the solution matches the provided challenge statements, and Mathlib dependencies were verified as byte-identical to official caches.

While some single-threaded Lean kernel replays were still in progress at the time of the report, all completed major checks passed without error. This milestone marks a historic achievement in computational mathematics, providing a machine-verified foundation for one of the most significant conjectures in number theory.

---

## 15. Show HN: Zero C# – C# without a runtime or GC

**原文标题**: Show HN: Zero C# – C# without a runtime or GC

**原文链接**: [https://onurgumus.github.io/zero-csharp/index.html](https://onurgumus.github.io/zero-csharp/index.html)

生成摘要时出错

---

## 16. The Emergence of Inequality in the Czech Corded Ware Culture

**原文标题**: The Emergence of Inequality in the Czech Corded Ware Culture

**原文链接**: [https://www.jna.uni-kiel.de/index.php/jna/article/view/1560/1746](https://www.jna.uni-kiel.de/index.php/jna/article/view/1560/1746)

生成摘要时出错

---

## 17. Inkling 2 Mini

**原文标题**: Inkling 2 Mini

**原文链接**: [https://thinkingmachines.ai/news/inkling-2-mini/](https://thinkingmachines.ai/news/inkling-2-mini/)

生成摘要时出错

---

## 18. I'm quite pleased by the tech architecture of my art website

**原文标题**: I'm quite pleased by the tech architecture of my art website

**原文链接**: [https://klauria.tech/klauria-art/](https://klauria.tech/klauria-art/)

生成摘要时出错

---

## 19. RCE in Gnupg

**原文标题**: RCE in Gnupg

**原文链接**: [https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html](https://lists.gnupg.org/pipermail/gnupg-announce/2026q4/000517.html)

生成摘要时出错

---

## 20. Context-Generic Programming v0.8.0 – Pluggable trait implementations for Rust

**原文标题**: Context-Generic Programming v0.8.0 – Pluggable trait implementations for Rust

**原文链接**: [https://contextgeneric.dev/blog/v0.8.0-release/](https://contextgeneric.dev/blog/v0.8.0-release/)

生成摘要时出错

---

## 21. Bolt's Scooters Are Becoming Accessibility Sensors

**原文标题**: Bolt's Scooters Are Becoming Accessibility Sensors

**原文链接**: [https://geoawesome.com/bolt-scooters-accessibility-mapping-wheels4wheels/](https://geoawesome.com/bolt-scooters-accessibility-mapping-wheels4wheels/)

生成摘要时出错

---

## 22. Why there are still no non-WebKit browsers on iOS

**原文标题**: Why there are still no non-WebKit browsers on iOS

**原文链接**: [https://blog.mozilla.org/en/mozilla/internet-policy/apple-ios-browser-engine-rules/](https://blog.mozilla.org/en/mozilla/internet-policy/apple-ios-browser-engine-rules/)

生成摘要时出错

---

## 23. LLMs can read and write executables byte by byte from a hex dump

**原文标题**: LLMs can read and write executables byte by byte from a hex dump

**原文链接**: [https://sgiannopoulos.github.io/blog/machine-code-programming/](https://sgiannopoulos.github.io/blog/machine-code-programming/)

生成摘要时出错

---

## 24. How I made a custom game engine for Satelital

**原文标题**: How I made a custom game engine for Satelital

**原文链接**: [https://spectralorbit.com/blog/satelital_game_engine](https://spectralorbit.com/blog/satelital_game_engine)

生成摘要时出错

---

## 25. We promoted developers into architects without informing them

**原文标题**: We promoted developers into architects without informing them

**原文链接**: [https://manidoraisamy.com/developer-to-architect.html](https://manidoraisamy.com/developer-to-architect.html)

生成摘要时出错

---

## 26. Deterministic Simulation Testing Is for Everyone

**原文标题**: Deterministic Simulation Testing Is for Everyone

**原文链接**: [https://outdata.net/blog/261120](https://outdata.net/blog/261120)

生成摘要时出错

---

## 27. Unforced Navier-Stokes Singularity and the Generalized Riemann Hypothesis

**原文标题**: Unforced Navier-Stokes Singularity and the Generalized Riemann Hypothesis

**原文链接**: [https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/)

生成摘要时出错

---

## 28. Levent Alpöge claims proof of the Generalized Riemann Hypothesis [pdf]

**原文标题**: Levent Alpöge claims proof of the Generalized Riemann Hypothesis [pdf]

**原文链接**: [https://alpo.ge/remark.pdf](https://alpo.ge/remark.pdf)

生成摘要时出错

---

## 29. Show HN: An ASCII cell aquarium for your terminal

**原文标题**: Show HN: An ASCII cell aquarium for your terminal

**原文链接**: [https://github.com/kborer/cells/](https://github.com/kborer/cells/)

生成摘要时出错

---

## 30. The Soviet Elektronika BK-0010 home computer built on a clone of the PDP-11 CPU

**原文标题**: The Soviet Elektronika BK-0010 home computer built on a clone of the PDP-11 CPU

**原文链接**: [https://8bitarchitect.net/machines/elektronika-bk-0010/](https://8bitarchitect.net/machines/elektronika-bk-0010/)

生成摘要时出错

---

## 31. Slopstrap – Make your site look hastily vibecoded

**原文标题**: Slopstrap – Make your site look hastily vibecoded

**原文链接**: [https://slopstrap.mikelacher.com/](https://slopstrap.mikelacher.com/)

生成摘要时出错

---

## 32. NINLIVE: The Nine Inch Nails live archive

**原文标题**: NINLIVE: The Nine Inch Nails live archive

**原文链接**: [https://ninlive.com/](https://ninlive.com/)

生成摘要时出错

---

## 33. Clojure will affect the way you think about programming (2017)

**原文标题**: Clojure will affect the way you think about programming (2017)

**原文链接**: [https://eli.thegreenplace.net/2017/clojure-the-perfect-language-to-expand-your-brain/](https://eli.thegreenplace.net/2017/clojure-the-perfect-language-to-expand-your-brain/)

生成摘要时出错

---

## 34. ClawDOS – An AI coding agent for DOS

**原文标题**: ClawDOS – An AI coding agent for DOS

**原文链接**: [http://ricapar.net/ClawDOS/](http://ricapar.net/ClawDOS/)

生成摘要时出错

---

## 35. Astra 6.2 and Sol 6.2 flop at Simple Bench

**原文标题**: Astra 6.2 and Sol 6.2 flop at Simple Bench

**原文链接**: [https://simple-bench.com/](https://simple-bench.com/)

生成摘要时出错

---

## 36. Language Models Can Rewrite Their Own Weights

**原文标题**: Language Models Can Rewrite Their Own Weights

**原文链接**: [https://arxiv.org/abs/2611.21885](https://arxiv.org/abs/2611.21885)

生成摘要时出错

---

## 37. Nasdaq erases all 2026 gains as AI sell-off dampens Anthropic’s second day

**原文标题**: Nasdaq erases all 2026 gains as AI sell-off dampens Anthropic’s second day

**原文链接**: [https://www.theguardian.com/business/2026/nov/20/global-stock-markets-slump-anthropic-ipo-ai-sell-off](https://www.theguardian.com/business/2026/nov/20/global-stock-markets-slump-anthropic-ipo-ai-sell-off)

生成摘要时出错

---

## 38. Surprisingly Adorable Insect Portraits

**原文标题**: Surprisingly Adorable Insect Portraits

**原文链接**: [https://amateurphotographer.com/latest/these-astonishing-insect-portraits-reveal-a-hidden-world-you-never-knew-existed/](https://amateurphotographer.com/latest/these-astonishing-insect-portraits-reveal-a-hidden-world-you-never-knew-existed/)

生成摘要时出错

---

## 39. Sir Brian May adds new dimension to Hera asteroid

**原文标题**: Sir Brian May adds new dimension to Hera asteroid

**原文链接**: [https://www.esa.int/articles/about-us/directorates/operations/space-safety/hera/sir-brian-may-adds-new-dimension-to-hera-asteroid](https://www.esa.int/articles/about-us/directorates/operations/space-safety/hera/sir-brian-may-adds-new-dimension-to-hera-asteroid)

生成摘要时出错

---

## 40. DreamCoder: Coding harness and IDE from the author of Mastering Emacs

**原文标题**: DreamCoder: Coding harness and IDE from the author of Mastering Emacs

**原文链接**: [https://www.masteringemacs.org/article/announcing-dreamcoder](https://www.masteringemacs.org/article/announcing-dreamcoder)

生成摘要时出错

---

## 41. Finite-time blow-up for the Navier–Stokes equations

**原文标题**: Finite-time blow-up for the Navier–Stokes equations

**原文链接**: [https://github.com/tristanbuckmaster/navier-stokes/](https://github.com/tristanbuckmaster/navier-stokes/)

生成摘要时出错

---

## 42. Valkey kills the skiplist, cuts sorted set overhead by up to 43%

**原文标题**: Valkey kills the skiplist, cuts sorted set overhead by up to 43%

**原文链接**: [https://valkey.io/blog/from-skiplist-to-b+tree/](https://valkey.io/blog/from-skiplist-to-b+tree/)

生成摘要时出错

---

## 43. Show HN: Tinnitus frequency finder and audio notch tool

**原文标题**: Show HN: Tinnitus frequency finder and audio notch tool

**原文链接**: [https://trynotched.com/find](https://trynotched.com/find)

生成摘要时出错

---

## 44. Why the Airbus A321XLR often gets stuck climbing for first few hours of flight

**原文标题**: Why the Airbus A321XLR often gets stuck climbing for first few hours of flight

**原文链接**: [https://simpleflying.com/airbus-a321xlr-often-stuck-climbing-1st-few-hours-flight/](https://simpleflying.com/airbus-a321xlr-often-stuck-climbing-1st-few-hours-flight/)

生成摘要时出错

---

## 45. FBI reportedly investigating apparent hack of its criminal database

**原文标题**: FBI reportedly investigating apparent hack of its criminal database

**原文链接**: [https://www.bbc.com/news/articles/cvze7de86pk3o](https://www.bbc.com/news/articles/cvze7de86pk3o)

生成摘要时出错

---

## 46. Jensen Huang's fall is bad news for Silicon Valley's accelerationists

**原文标题**: Jensen Huang's fall is bad news for Silicon Valley's accelerationists

**原文链接**: [https://www.economist.com/business/2026/11/19/jensen-huangs-fall-is-bad-news-for-silicon-valleys-accelerationists](https://www.economist.com/business/2026/11/19/jensen-huangs-fall-is-bad-news-for-silicon-valleys-accelerationists)

生成摘要时出错

---

## 47. Defcon 5's California Caravan Program/Zine

**原文标题**: Defcon 5's California Caravan Program/Zine

**原文链接**: [https://netninja.com/2026/06/08/defcon-5s-california-caravan-program-zine/](https://netninja.com/2026/06/08/defcon-5s-california-caravan-program-zine/)

生成摘要时出错

---

## 48. Fewer slides, more dragons

**原文标题**: Fewer slides, more dragons

**原文链接**: [https://www.breakingchange.blog/p/fewer-slides-more-dragons](https://www.breakingchange.blog/p/fewer-slides-more-dragons)

生成摘要时出错

---

## 49. Vibecoding an inference chip

**原文标题**: Vibecoding an inference chip

**原文链接**: [https://ankitg.me/blog/vibecoding-inference-chip/](https://ankitg.me/blog/vibecoding-inference-chip/)

生成摘要时出错

---

## 50. Serious cyberattack thought backed by wealthy operators

**原文标题**: Serious cyberattack thought backed by wealthy operators

**原文链接**: [https://www.ruv.is/english/2026-11-20-serious-cyberattack-thought-backed-by-wealthy-operators-493411](https://www.ruv.is/english/2026-11-20-serious-cyberattack-thought-backed-by-wealthy-operators-493411)

生成摘要时出错

---

## 51. I can’t believe it’s 1

**原文标题**: I can’t believe it’s 1

**原文链接**: [https://aperiodical.com/2026/11/i-cant-believe-its-1/](https://aperiodical.com/2026/11/i-cant-believe-its-1/)

生成摘要时出错

---

## 52. GrapheneOS made a proof of concept RCS messaging app without Google Messages

**原文标题**: GrapheneOS made a proof of concept RCS messaging app without Google Messages

**原文链接**: [https://twitter.com/GrapheneOS/status/2124158267123233056](https://twitter.com/GrapheneOS/status/2124158267123233056)

生成摘要时出错

---

## 53. Winedroid – run Android apps without Android (WASM demo)

**原文标题**: Winedroid – run Android apps without Android (WASM demo)

**原文链接**: [https://winedroid.soham.sh/demo/](https://winedroid.soham.sh/demo/)

生成摘要时出错

---

## 54. Show HN: I made a PS1 style racing game

**原文标题**: Show HN: I made a PS1 style racing game

**原文链接**: [https://outpostracer.com](https://outpostracer.com)

生成摘要时出错

---

## 55. Show HN: I made an audio-to-MIDI model 60x more efficient

**原文标题**: Show HN: I made an audio-to-MIDI model 60x more efficient

**原文链接**: [https://kobi.music/research/dettato](https://kobi.music/research/dettato)

生成摘要时出错

---

## 56. Battery storage in Great Britain: how a grid battery makes money

**原文标题**: Battery storage in Great Britain: how a grid battery makes money

**原文链接**: [https://a115.co.uk/battery-storage-revenues/](https://a115.co.uk/battery-storage-revenues/)

生成摘要时出错

---

## 57. Pakistan's solar revolution is so successful the national grid is lagging behind

**原文标题**: Pakistan's solar revolution is so successful the national grid is lagging behind

**原文链接**: [https://www.bbc.com/news/articles/ckvg2n2q3103o](https://www.bbc.com/news/articles/ckvg2n2q3103o)

生成摘要时出错

---

## 58. The stochastic parrots have apparently proved the Riemann Hypothesis

**原文标题**: The stochastic parrots have apparently proved the Riemann Hypothesis

**原文链接**: [https://scottaaronson.blog/?p=10344](https://scottaaronson.blog/?p=10344)

生成摘要时出错

---

## 59. FBI Criminal Database Hacked

**原文标题**: FBI Criminal Database Hacked

**原文链接**: [https://www.france24.com/en/fbi-criminal-database-hacked](https://www.france24.com/en/fbi-criminal-database-hacked)

生成摘要时出错

---

## 60. If you can't explain something in simple terms, you don't understand it (2017)

**原文标题**: If you can't explain something in simple terms, you don't understand it (2017)

**原文链接**: [https://kottke.org/17/06/if-you-cant-explain-something-in-simple-terms-you-dont-understand-it](https://kottke.org/17/06/if-you-cant-explain-something-in-simple-terms-you-dont-understand-it)

生成摘要时出错

---

## 61. Frostbite: A new CPU architecture discovered, designed and verified by AI

**原文标题**: Frostbite: A new CPU architecture discovered, designed and verified by AI

**原文链接**: [https://architectlabs.com/blog/frostbite](https://architectlabs.com/blog/frostbite)

生成摘要时出错

---

## 62. Claude solves two open problems in the physics of black holes

**原文标题**: Claude solves two open problems in the physics of black holes

**原文链接**: [https://www.anthropic.com/research/claude-black-hole-physics](https://www.anthropic.com/research/claude-black-hole-physics)

生成摘要时出错

---

## 63. The Making of Oxygene

**原文标题**: The Making of Oxygene

**原文链接**: [https://jeanmicheljarre.com/aaa/the-making-of-oxygene](https://jeanmicheljarre.com/aaa/the-making-of-oxygene)

生成摘要时出错

---

## 64. Restricting AI agents in mobile operating systems platforms from capturing data

**原文标题**: Restricting AI agents in mobile operating systems platforms from capturing data

**原文链接**: [https://signal.org/blog/protecting-your-privacy/](https://signal.org/blog/protecting-your-privacy/)

生成摘要时出错

---

## 65. The Hungry Butler Effect: Concealed Commercial Incentives in LLMs

**原文标题**: The Hungry Butler Effect: Concealed Commercial Incentives in LLMs

**原文链接**: [https://www.researchgate.net/publication/418143113_The_Hungry_Butler_Effect_Concealed_Commercial_Incentives_and_the_Erosion_of_Epistemic_Rigour_in_Large_Language_Models](https://www.researchgate.net/publication/418143113_The_Hungry_Butler_Effect_Concealed_Commercial_Incentives_and_the_Erosion_of_Epistemic_Rigour_in_Large_Language_Models)

生成摘要时出错

---

## 66. 3-legged Persian leopard's 150-mile journey highlights Caucasus border hazards

**原文标题**: 3-legged Persian leopard's 150-mile journey highlights Caucasus border hazards

**原文链接**: [https://news.mongabay.com/short-article/2026/11/three-legged-persian-leopards-150-mile-journey-highlights-caucasus-border-hazards/](https://news.mongabay.com/short-article/2026/11/three-legged-persian-leopards-150-mile-journey-highlights-caucasus-border-hazards/)

生成摘要时出错

---

## 67. Floppy3.5: A portable 3.5-inch floppy WiFi NAS

**原文标题**: Floppy3.5: A portable 3.5-inch floppy WiFi NAS

**原文链接**: [https://github.com/bigcrimping/floppy3.5](https://github.com/bigcrimping/floppy3.5)

生成摘要时出错

---

## 68. Exascale fusion simulation team named finalist for 2026 Gordon Bell Prize

**原文标题**: Exascale fusion simulation team named finalist for 2026 Gordon Bell Prize

**原文链接**: [https://www.alcf.anl.gov/news/exascale-fusion-simulation-team-named-finalist-2026-gordon-bell-prize](https://www.alcf.anl.gov/news/exascale-fusion-simulation-team-named-finalist-2026-gordon-bell-prize)

生成摘要时出错

---

## 69. AI is giving everyone the same advice

**原文标题**: AI is giving everyone the same advice

**原文链接**: [https://a90.com/experiments/same-advice/](https://a90.com/experiments/same-advice/)

生成摘要时出错

---

## 70. FFmpeg 9.1 'Gauss'

**原文标题**: FFmpeg 9.1 'Gauss'

**原文链接**: [https://ffmpeg.org/download.html#release_9.1](https://ffmpeg.org/download.html#release_9.1)

生成摘要时出错

---

## 71. Show HN: agent-mcts – Monte Carlo tree search on top of Claude Code

**原文标题**: Show HN: agent-mcts – Monte Carlo tree search on top of Claude Code

**原文链接**: [https://github.com/natsu0529/agent-mcts](https://github.com/natsu0529/agent-mcts)

生成摘要时出错

---

## 72. The G1 Garbage Collector

**原文标题**: The G1 Garbage Collector

**原文链接**: [https://dev.java/learn/jvm/tool/garbage-collection/g1gc-overview/](https://dev.java/learn/jvm/tool/garbage-collection/g1gc-overview/)

生成摘要时出错

---

## 73. What people are building, discovered through new domains

**原文标题**: What people are building, discovered through new domains

**原文链接**: [https://startups.novumsignals.com/](https://startups.novumsignals.com/)

生成摘要时出错

---

## 74. Show HN: OpenComputer – an open source alternative to Devin

**原文标题**: Show HN: OpenComputer – an open source alternative to Devin

**原文链接**: [https://github.com/diggerhq/opencomputer](https://github.com/diggerhq/opencomputer)

生成摘要时出错

---

## 75. Countries open path towards 'killer robots' pact

**原文标题**: Countries open path towards 'killer robots' pact

**原文链接**: [https://www.afp.com/en/countries-open-path-towards-killer-robots-pact](https://www.afp.com/en/countries-open-path-towards-killer-robots-pact)

生成摘要时出错

---

## 76. Jujutsu Primer

**原文标题**: Jujutsu Primer

**原文链接**: [https://ethanlowman.com/posts/jj-primer/](https://ethanlowman.com/posts/jj-primer/)

生成摘要时出错

---

## 77. US SEC's Nvidia probe is examining potential accounting issues – sources

**原文标题**: US SEC's Nvidia probe is examining potential accounting issues – sources

**原文链接**: [https://www.marketscreener.com/news/us-sec-s-nvidia-probe-is-examining-potential-accounting-issues-sources-say-ce785ed3dd8ff627](https://www.marketscreener.com/news/us-sec-s-nvidia-probe-is-examining-potential-accounting-issues-sources-say-ce785ed3dd8ff627)

生成摘要时出错

---

## 78. And yet, it moves

**原文标题**: And yet, it moves

**原文链接**: [https://signoregalilei.com/2026/11/20/and-yet-it-moves/](https://signoregalilei.com/2026/11/20/and-yet-it-moves/)

生成摘要时出错

---

## 79. Backblaze Notice at Collection and Privacy Policy

**原文标题**: Backblaze Notice at Collection and Privacy Policy

**原文链接**: [https://www.backblaze.com/company/policy/privacy](https://www.backblaze.com/company/policy/privacy)

生成摘要时出错

---

## 80. Worlds largest beaver dam in Northern Alberta

**原文标题**: Worlds largest beaver dam in Northern Alberta

**原文链接**: [https://substack.com/@canadianreturnee/note/c-319574497](https://substack.com/@canadianreturnee/note/c-319574497)

生成摘要时出错

---

## 81. Show HN: Fast deterministic natural language search for OpenStreetMap data

**原文标题**: Show HN: Fast deterministic natural language search for OpenStreetMap data

**原文链接**: [https://hippomaps.ch/?q=cafes+by+the+Limmat+100+m+from+the+lake+in+zurich#map=15.02/47.36708/8.54935](https://hippomaps.ch/?q=cafes+by+the+Limmat+100+m+from+the+lake+in+zurich#map=15.02/47.36708/8.54935)

生成摘要时出错

---

## 82. Postgres 19 Repack: Faster, Built-In Table Bloat Cleanup

**原文标题**: Postgres 19 Repack: Faster, Built-In Table Bloat Cleanup

**原文链接**: [https://www.snowflake.com/en/blog/engineering/postgres-19-repack-table-bloat/](https://www.snowflake.com/en/blog/engineering/postgres-19-repack-table-bloat/)

生成摘要时出错

---

## 83. Microsoft's SideWinder Strategic Commander was a failed attempt

**原文标题**: Microsoft's SideWinder Strategic Commander was a failed attempt

**原文链接**: [https://www.rockpapershotgun.com/microsofts-sidewinder-strategic-commander-was-a-failed-attempt-to-reimagine-rts-controls-23-years-later-why-are-some-players-still-using-it](https://www.rockpapershotgun.com/microsofts-sidewinder-strategic-commander-was-a-failed-attempt-to-reimagine-rts-controls-23-years-later-why-are-some-players-still-using-it)

生成摘要时出错

---

## 84. Show HN: LZ0 -An asymmetric LZ compressor with ultra minimal, 0-alloc decoder

**原文标题**: Show HN: LZ0 -An asymmetric LZ compressor with ultra minimal, 0-alloc decoder

**原文链接**: [https://github.com/seb3773/lz0](https://github.com/seb3773/lz0)

生成摘要时出错

---

## 85. I'll never buy Framework hardware again

**原文标题**: I'll never buy Framework hardware again

**原文链接**: [https://poolp.org/posts/2026-11-20/ill-never-buy-framework-hardware-again/](https://poolp.org/posts/2026-11-20/ill-never-buy-framework-hardware-again/)

生成摘要时出错

---

## 86. Launch HN: Onlook (YC W25) – An open-source developer tool for designers

**原文标题**: Launch HN: Onlook (YC W25) – An open-source developer tool for designers

**原文链接**: [https://github.com/onlook-dev/onlook/](https://github.com/onlook-dev/onlook/)

生成摘要时出错

---

## 87. Carnival Cruises emits ten times more sulphur oxide than all of Europe's cars (2019)

**原文标题**: Carnival Cruises emits ten times more sulphur oxide than all of Europe's cars (2019)

**原文链接**: [https://ecohustler.com/article/one-corporation-to-pollute-them-all/](https://ecohustler.com/article/one-corporation-to-pollute-them-all/)

生成摘要时出错

---

## 88. Do not buy RAM, compress

**原文标题**: Do not buy RAM, compress

**原文链接**: [https://curiousbits.nl/blog/do-not-buy-ram-compress/](https://curiousbits.nl/blog/do-not-buy-ram-compress/)

生成摘要时出错

---

## 89. Acoustic parameters of bird vocalizations&their perceived pleasantness by humans

**原文标题**: Acoustic parameters of bird vocalizations&their perceived pleasantness by humans

**原文链接**: [https://www.frontiersin.org/journals/bird-science/articles/10.3389/fbirs.2026.1794594/full](https://www.frontiersin.org/journals/bird-science/articles/10.3389/fbirs.2026.1794594/full)

生成摘要时出错

---

## 90. Show HN: Foolscap – a writing app that reads your book and never writes for you

**原文标题**: Show HN: Foolscap – a writing app that reads your book and never writes for you

**原文链接**: [https://foolscap.works/](https://foolscap.works/)

生成摘要时出错

---

## 91. µ-Wire – USB on an ATtiny 10

**原文标题**: µ-Wire – USB on an ATtiny 10

**原文链接**: [https://cpldcpu.com/2014/03/19/%c2%b5-wire-usb-on-an-attiny-10/](https://cpldcpu.com/2014/03/19/%c2%b5-wire-usb-on-an-attiny-10/)

生成摘要时出错

---

## 92. Synology Security Advisory

**原文标题**: Synology Security Advisory

**原文链接**: [https://www.synology.com/en-uk/security/advisory/Synology_SA_26_21](https://www.synology.com/en-uk/security/advisory/Synology_SA_26_21)

生成摘要时出错

---

## 93. What Comes After AGI?

**原文标题**: What Comes After AGI?

**原文链接**: [https://institute.deepmind.com/essays/what-comes-after-agi/](https://institute.deepmind.com/essays/what-comes-after-agi/)

生成摘要时出错

---

## 94. Running two PSP emulators on one Switch 2 and sharing one via GameShare

**原文标题**: Running two PSP emulators on one Switch 2 and sharing one via GameShare

**原文链接**: [https://github.com/XITRIX/ppsspp-nx2/blob/master/SWITCH2-GAMESHARE.md](https://github.com/XITRIX/ppsspp-nx2/blob/master/SWITCH2-GAMESHARE.md)

生成摘要时出错

---

## 95. FBI's criminal information database hacked, CNN reports

**原文标题**: FBI's criminal information database hacked, CNN reports

**原文链接**: [https://www.cnbc.com/2026/11/21/fbis-criminal-information-database-hacked-cnn-reports.html](https://www.cnbc.com/2026/11/21/fbis-criminal-information-database-hacked-cnn-reports.html)

生成摘要时出错

---

## 96. Show HN: An API for word timestamps from speech, 75% within 20ms

**原文标题**: Show HN: An API for word timestamps from speech, 75% within 20ms

**原文链接**: [https://quebec.yarn.so](https://quebec.yarn.so)

生成摘要时出错

---

## 97. Engineer's Guide to Career Growth – Advice from My Time at Stripe and Facebook

**原文标题**: Engineer's Guide to Career Growth – Advice from My Time at Stripe and Facebook

**原文链接**: [https://review.firstround.com/the-engineers-guide-to-career-growth-advice-from-my-time-at-stripe-and-facebook/](https://review.firstround.com/the-engineers-guide-to-career-growth-advice-from-my-time-at-stripe-and-facebook/)

生成摘要时出错

---

## 98. Anthropic's IPO bank closed position meant to stabilize stock

**原文标题**: Anthropic's IPO bank closed position meant to stabilize stock

**原文链接**: [https://www.reuters.com/markets/us/anthropics-ipo-bank-closed-position-meant-stabilize-stock-removing-source-2026-11-20](https://www.reuters.com/markets/us/anthropics-ipo-bank-closed-position-meant-stabilize-stock-removing-source-2026-11-20)

生成摘要时出错

---

## 99. Garage Door Spam

**原文标题**: Garage Door Spam

**原文链接**: [https://blog.harrison.page/garage-door-spam/](https://blog.harrison.page/garage-door-spam/)

生成摘要时出错

---

## 100. If you stop writing code, you also get worse at reviewing it

**原文标题**: If you stop writing code, you also get worse at reviewing it

**原文链接**: [https://cekrem.github.io/posts/if-you-stop-writing-code-you-also-get-worse-at-reviewing-it/](https://cekrem.github.io/posts/if-you-stop-writing-code-you-also-get-worse-at-reviewing-it/)

生成摘要时出错

---

