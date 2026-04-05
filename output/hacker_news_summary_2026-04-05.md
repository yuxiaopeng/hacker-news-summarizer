# Hacker News 热门文章摘要 (2026-04-05)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 阿耳忒弥斯2号机组人员首次瞥见月球背面 [视频]

**原文标题**: Artemis II crew see first glimpse of far side of Moon [video]

**原文链接**: [https://www.bbc.com/news/videos/ce3d5gkd2geo](https://www.bbc.com/news/videos/ce3d5gkd2geo)

所提供的文本概述了一系列重大新闻报道，主要关注阿耳忒弥斯2号任务的历史性进展以及几项重大的国内外危机。

**阿耳忒弥斯2号任务**
在执行任务的第三天，阿耳忒弥斯2号机组人员——NASA宇航员里德·怀斯曼、维克多·格洛弗、克里斯蒂娜·科赫以及加拿大航天局宇航员杰里米·汉森——成为首批亲眼目睹月球背面东海盆地的人类。截至周六晚，猎户座飞船距离地球约18万英里。机组人员称这次体验“绝对壮观”，并指出月球背面与从地球上看到的熟悉月面有着显著不同。

**航空与基础设施危机**
纽约拉瓜迪亚机场发生了一起重大悲剧，一架载有76人的加拿大航空客机在跑道上与一辆消防车相撞。这起“致命碰撞”导致了大规模的交通中断。受政府部分停摆影响，交通安全管理局（TSA）特工在无薪工作，局势进一步恶化，政府不得不部署移民海关执法局（ICE）特工到机场协助工作。

**政治与经济动荡**
头条新闻反映了一段剧烈的国内动荡和全球冲突时期：
*   **战争与经济：** 持续进行的对伊战争已导致美国汽油价格升至每加仑4美元以上，给农业部门带来了沉重的财务负担。
*   **抗议活动：** 由布鲁斯·斯普林斯汀参与的“拒绝国王”集会已在美国各地蔓延，抗议特朗普政府。
*   **政府活动：** 代理总检察长托德·布兰奇的角色正受到审查，而第一夫人梅拉尼娅·特朗普主持了一场关于人工智能与数字安全的峰会，并展示了一个人形机器人。
*   **法律裁决：** 洛杉矶的一个陪审团最近裁定，Meta和谷歌因故意创建损害青少年心理健康的成瘾性平台而承担责任。

---

## 2. Codex 将面向所有用户切换为基于 API 用量的计费模式。

**原文标题**: Codex is switching to API pricing based usage for all users

**原文链接**: [https://help.openai.com/en/articles/20001106-codex-rate-card](https://help.openai.com/en/articles/20001106-codex-rate-card)

OpenAI 已宣布 Codex 模型的免费测试期于 2023 年 3 月 23 日结束。因此，特定的 Codex 模型——`code-davinci-002` 和 `code-cushman-001`——已被弃用。

此次过渡的要点包括：

*   **模型过渡：** OpenAI 建议所有用户从旧版 Codex 模型迁移至 `gpt-3.5-turbo` 或 `gpt-4`。这些模型具备强大的代码处理能力，且与原始 Codex 模型相比，性能更优、用途更广。
*   **定价：** 虽然 Codex 测试版此前可免费使用，但替代模型将按照 OpenAI 的标准 API 定价计费。这意味着用户将根据处理的 Token 数量支付费用。
*   **研究访问：** 为支持学术界，OpenAI 提供了研究人员访问计划。如果标准定价造成负担，研究人员和教育工作者可以申请资助访问以继续其工作。
*   **功能：** 较新的聊天补全（Chat Completions）API 模型支持与 Codex 相同的编程功能，但在处理更广泛的指令和对话语境方面进行了优化。

这一变化反映了 OpenAI 整合其模型产品、并将资源集中于最先进且高效的大语言模型的策略。建议用户将其应用程序更新至较新模型，以确保服务的持续性并获得更好的效果。

---

## 3. 八年渴望，三月 AI 筑就

**原文标题**: Eight years of wanting, three months of building with AI

**原文链接**: [https://lalitm.com/post/building-syntaqlite-ai/](https://lalitm.com/post/building-syntaqlite-ai/)

在渴望更好的 SQLite 开发工具八年后，作者利用 AI 编程助手在三个月内构建了 **syntaqlite**。该项目涉及提取并适配 SQLite 复杂且缺乏文档的 C 语言解析器——这项任务此前因过于“艰巨且乏味”而被认为不适合作为业余项目。

开发过程分为两个阶段。最初，作者尝试了“凭感觉编码”（vibe-coding），将几乎所有实现工作交给 Claude Code。虽然这产生了一个可运行的原型，但生成的“面条式代码”难以维护。这促使作者用 Rust 进行了彻底重写，期间作者重新主导设计决策，并将 AI 作为“加强版自动补全”，将其融入严格的代码审查、重构和自动化测试流程中。

**AI 的主要优势：**
*   **克服惯性：** AI 提供的具体原型将令人生畏的设计任务转化为了可处理的具体问题。
*   **速度与重构：** AI 擅长编写“标准”代码，并能实现快速、大规模的重构。
*   **助教功能：** 它弥补了作者在 Rust 工具链和编辑器扩展 API 等陌生领域的知识空白。
*   **项目广度：** AI 降低了“长尾”功能（如 WASM 演练场、打包和文档）的开发成本，使得 0.1 版本的发布更加完整。

**核心代价与挑战：**
*   **“老虎机”效应：** 作者注意到提示词（prompting）具有某种成瘾性，可能导致陷入无意义的时间消耗。
*   **疲劳导致的收益递减：** 深夜时段措辞不当的提示词会产生“垃圾代码”和循环错误。
*   **上下文丢失：** 过度依赖 AI 导致作者偶尔会失去对代码库的心理建模，使深度调试变得困难。

作者总结道，虽然 AI 是该项目的关键催化剂，但其成功仍取决于保持人类的“品味”、技术领导力，以及果断舍弃低质量 AI 输出的意愿。

---

## 4. 用 (nightly) Rust 编写的尾调用解释器

**原文标题**: A tail-call interpreter in (nightly) Rust

**原文链接**: [https://www.mattkeeter.com/blog/2026-04-05-tailcall/](https://www.mattkeeter.com/blog/2026-04-05-tailcall/)

本文探讨了如何利用 `become` 关键字实现高性能的 Uxn CPU 模拟器。该关键字是 Rust nightly 版本最近新增的特性，用于显式尾调用优化（tail-call optimization）。

作者的目标是在保持 Rust 安全性的同时，达到其此前手写 ARM64 汇编代码的性能水平。尾调用解释器的工作原理是将虚拟机状态（寄存器、栈和程序计数器）作为函数参数传递，并在每条指令结束时直接跳转到下一个函数。这种被称为“线程代码”（threaded code）的技术通过替换当前栈帧而非嵌套栈帧来防止栈溢出。

关键实现细节包括：
*   **样板代码管理**：作者利用复杂的宏将现有的操作码逻辑封装为尾调用函数。
*   **调用约定**：在 x86 平台上，作者使用了 `extern "rust-preserve-none"` 来确保编译器使用足够的寄存器传递参数，从而减少开销。
*   **安全性**：整个实现保持了 100% 的安全 Rust，成功避免了作者此前汇编版本中存在的内存损坏风险。

**性能测试结果：**
*   **ARM64 (M1 MacBook)**：尾调用解释器取得了圆满成功，性能超过了原有的 Rust 虚拟机和手写汇编。
*   **x86-64**：结果喜忧参半。虽然明显快于原有的虚拟机，但仍落后于经过手动调优的汇编。对生成的机器码进行检查后发现，Rust 编译器在 x86 上引入了不必要的“寄存器重组”和栈溢出，而人工编写代码可以避免这些问题。

最终作者得出结论：Rust 的尾调用支持为编写高性能模拟器提供了一种愉悦且高效的方式，证明了在合适的架构条件下，安全的人类编写代码现已能与汇编语言相媲美。

---

## 5. 穴居人：何必多用token，少用就行。

**原文标题**: Caveman: Why use many token when few token do trick

**原文链接**: [https://github.com/JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)

**Caveman** 是一款专为 Claude Code 和 Codex 设计的插件，旨在不牺牲技术准确性的前提下，将大语言模型（LLM）的输出 Token 减少约 75%。受“穴居人说话（caveman-speak）”梗的启发，该工具强制 AI 采用极简的、电报式的风格进行交流，剔除了填充词、客套话、冠词和模棱两可的表述。

**核心特性与优势：**
*   **高效性：** 通过剔除“废话”（如“我很乐意为您提供帮助”），Caveman 将响应长度平均缩减了 65%–87%，从而显著提升了生成速度并降低了 API 成本。
*   **技术完整性：** 尽管 AI 的表达变得简单，但它保留了 100% 的技术准确性。代码块、技术术语（如“多态性”）和错误消息均保持原样。
*   **性能提升：** 该项目引用的研究表明，简洁性约束实际上可以通过迫使模型关注实质内容而非冗长辞藻，从而提高 LLM 的准确性。
*   **定向优化：** 该插件仅影响“输出”Token；AI 的内部推理和“思考”Token 则不受限制。

**使用与安装：**
Caveman 由 Julius Brussee 开发，可通过 `npx skills add JuliusBrussee/caveman` 或 Claude Code 插件市场进行安装。安装后，用户可以使用 `/caveman` 或 "caveman mode" 等命令开启该模式，并通过 "normal mode" 恢复正常。

总之，Caveman 是为那些比起对话礼貌，更看重速度、可读性和成本效益的开发者而打造的生产力工具。

---

## 6. 计算物理（第2版）

**原文标题**: Computational Physics (2nd Edition)

**原文链接**: [https://websites.umich.edu/~mejn/cp2/](https://websites.umich.edu/~mejn/cp2/)

Mark Newman 所著的《计算物理》（第2版）是一本全面的教科书及在线资源，旨在向学生介绍利用计算机解决物理问题的核心技术。本书主要围绕 Python 编程语言展开，在理论物理与实际计算应用之间架起了一座桥梁。

该书的官方网站作为一个配套中心，为学生和教师提供了丰富的资源。其主要特色包括：

*   **核心课程：** 本书涵盖了广泛的基础数值方法，包括积分、微分、线性方程组、傅里叶变换以及蒙特卡罗模拟等随机方法。此外，书中还深入探讨了对物理系统建模至关重要的常微分方程和偏微分方程的求解。
*   **强调 Python：** Newman 极力推崇 Python，得益于其出色的易读性以及 NumPy 和 Matplotlib 等强大科学库的支持。这使得没有深厚计算机科学背景的学习者也能顺利掌握相关内容。
*   **实用资源：** 网站提供了书中所有示例和程序的 Python 源代码下载。此外，还配有课后练习所需的数据文件，便于用户进行实战数据分析。
*   **教学支持：** 除代码外，网站还包含详细目录、前言及勘误表，以确保学习者获取的信息准确无误。

总体而言，该资源将计算物理定位为与实验和理论并列的科学方法第三大支柱，为现代物理研究与模拟提供了必备的工具。

---

## 7. Nanocode：200美元预算内，在TPU上基于纯JAX实现的最佳Claude Code。

**原文标题**: Nanocode: The best Claude Code that $200 can buy in pure JAX on TPUs

**原文链接**: [https://github.com/salmanmohammadi/nanocode/discussions/1](https://github.com/salmanmohammadi/nanocode/discussions/1)

Salman Mohammadi 推出了 nanocode，这是一个纯 JAX 编写的开源库，旨在 TPU 上端到端地训练智能体编码模型。受 Andrej Karpathy 的 *nanochat* 启发，该项目展示了如何以较低的预算构建一个“Claude Code”风格的助手。

**核心技术细节：**
*   **模型扩展：** 该库包含两个主要模型：一个拥有 13 亿参数（d24）的模型，训练成本约为 200 美元（在 TPU v6e-8 上运行 9 小时）；以及一个拥有 4.77 亿参数（d20）的模型，成本为 34 美元（1.5 小时）。
*   **数据与分词：** nanocode 采用了 *The Stack-V2* 和 *FineWeb-EDU* 按 1:5 比例混合的数据集。这种特定的配比使代码分词效率比标准模型提高了 50%，同时保持了与 GPT-2 XL 相当的通用推理能力。
*   **智能体框架：** 模型通过专门的工具调用接口与环境交互。它使用特定的特殊标记（tokens）来执行 `Read`、`Edit`、`Grep` 和 `Bash` 等命令，从而使其能够浏览和修改类 UNIX 文件系统。

**训练理念：**
nanocode 采用了由 Anthropic 推广的宪法 AI（Constitutional AI, CAI）方法论。这包括：
1.  **一份“SOUL”文档：** 一份定义模型性格的宪法规范——具体表现为一种随和、友好且“搞怪”的人设，且全篇仅使用小写文本。
2.  **对齐：** 训练流水线包括合成数据生成和偏好优化，以确保模型遵循其行为原则并可靠地使用工具。

该项目强调，通过优化的 JAX 基础设施和谷歌的 TPU 研究云（TRC）项目，开发者可以高效且以适度的算力成本，复现复杂的智能体编码助手。

---

## 8. Finnish sauna heat exposure induces stronger immune cell than cytokine responses

**原文标题**: Finnish sauna heat exposure induces stronger immune cell than cytokine responses

**原文链接**: [https://www.tandfonline.com/doi/full/10.1080/23328940.2026.2645467#abstract](https://www.tandfonline.com/doi/full/10.1080/23328940.2026.2645467#abstract)

生成摘要时出错

---

## 9. From birds to brains: My path to the fusiform face area (2024)

**原文标题**: From birds to brains: My path to the fusiform face area (2024)

**原文链接**: [https://www.kavliprize.org/nancy-kanwisher-autobiography](https://www.kavliprize.org/nancy-kanwisher-autobiography)

生成摘要时出错

---

## 10. Lisette a little language inspired by Rust that compiles to Go

**原文标题**: Lisette a little language inspired by Rust that compiles to Go

**原文链接**: [https://lisette.run/](https://lisette.run/)

生成摘要时出错

---

## 11. Baby's Second Garbage Collector

**原文标题**: Baby's Second Garbage Collector

**原文链接**: [https://www.matheusmoreira.com/articles/babys-second-garbage-collector](https://www.matheusmoreira.com/articles/babys-second-garbage-collector)

In "Baby's Second Garbage Collector," the author chronicles the evolution of a garbage collector (GC) for a Lisp implementation called "lone lisp." While the initial version was a "precise" collector that tracked objects strictly within the Lisp stack, it failed when objects escaped into "primitive lands"—native C functions and the native stack. This resulted in premature reclamation of active objects, leading to system instability and crashes.

To resolve this, the author transitions the GC toward a **conservative** model. The first step involves scanning the **native stack**. By utilizing the `__builtin_frame_address` intrinsic to determine stack boundaries, the GC iterates through the stack’s memory words. It checks if any of these values point to addresses within the Lisp heap. While this approach is "conservative"—meaning it may occasionally keep dead objects alive if a random bit pattern resembles a pointer—it ensures that no living objects are accidentally destroyed.

However, stack scanning alone proved insufficient, as the program continued to suffer from "shark attacks" (memory corruption). The author realized that objects were also "hiding" in **CPU registers**. Drawing inspiration from the Boehm-Demers-Weiser conservative GC, the author concludes that the GC must also inspect these registers. 

The article culminates in the implementation of **register spilling**. Using platform-specific assembly for `x86_64` and `aarch64`, the author writes routines to save all general-purpose registers into a buffer that the GC can then scan. This final step bridges the gap between the high-level dynamic language and the "underworld" of native execution, ensuring that any Lisp object referenced anywhere in the system’s physical memory or processing units is safely preserved.

---

## 12. The threat is comfortable drift toward not understanding what you're doing

**原文标题**: The threat is comfortable drift toward not understanding what you're doing

**原文链接**: [https://ergosphere.blog/posts/the-machines-are-fine/](https://ergosphere.blog/posts/the-machines-are-fine/)

生成摘要时出错

---

## 13. German implementation of eIDAS will require an Apple/Google account to function

**原文标题**: German implementation of eIDAS will require an Apple/Google account to function

**原文链接**: [https://bmi.usercontent.opencode.de/eudi-wallet/wallet-development-documentation-public/latest/architecture-concept/06-mobile-devices/02-mdvm/](https://bmi.usercontent.opencode.de/eudi-wallet/wallet-development-documentation-public/latest/architecture-concept/06-mobile-devices/02-mdvm/)

生成摘要时出错

---

## 14. Friendica – A Decentralized Social Network

**原文标题**: Friendica – A Decentralized Social Network

**原文链接**: [https://friendi.ca/](https://friendi.ca/)

生成摘要时出错

---

## 15. Just 'English with Hanzi'

**原文标题**: Just 'English with Hanzi'

**原文链接**: [https://www.oldnorthwhale.com/p/why-modern-chinese-is-just-english](https://www.oldnorthwhale.com/p/why-modern-chinese-is-just-english)

生成摘要时出错

---

## 16. Hightouch (YC S19) Is Hiring

**原文标题**: Hightouch (YC S19) Is Hiring

**原文链接**: [https://hightouch.com/careers#open-positions](https://hightouch.com/careers#open-positions)

生成摘要时出错

---

## 17. My Google Workspace account suspension

**原文标题**: My Google Workspace account suspension

**原文链接**: [https://zencapital.substack.com/p/sad-story-of-my-google-workspace](https://zencapital.substack.com/p/sad-story-of-my-google-workspace)

生成摘要时出错

---

## 18. OpenScreen is an open-source alternative to Screen Studio

**原文标题**: OpenScreen is an open-source alternative to Screen Studio

**原文链接**: [https://github.com/siddharthvaddem/openscreen](https://github.com/siddharthvaddem/openscreen)

生成摘要时出错

---

## 19. Phone-free bars and restaurants on the rise across the U.S.

**原文标题**: Phone-free bars and restaurants on the rise across the U.S.

**原文链接**: [https://www.axios.com/2026/04/05/phone-free-restaurants-bars-bans-restrictions-offline](https://www.axios.com/2026/04/05/phone-free-restaurants-bars-bans-restrictions-offline)

生成摘要时出错

---

## 20. Someone at BrowserStack is leaking users' email addresses

**原文标题**: Someone at BrowserStack is leaking users' email addresses

**原文链接**: [https://shkspr.mobi/blog/2026/04/someone-at-browserstack-is-leaking-users-email-address/](https://shkspr.mobi/blog/2026/04/someone-at-browserstack-is-leaking-users-email-address/)

生成摘要时出错

---

## 21. The Melanesian: Dark-skinned people with blonde hair region of Oceania

**原文标题**: The Melanesian: Dark-skinned people with blonde hair region of Oceania

**原文链接**: [https://guardian.ng/life/the-melanesian-dark-skinned-people-with-blonde-hair/](https://guardian.ng/life/the-melanesian-dark-skinned-people-with-blonde-hair/)

生成摘要时出错

---

## 22. Iguanaworks has closed and our products are no longer sold

**原文标题**: Iguanaworks has closed and our products are no longer sold

**原文链接**: [http://iguanaworks.net/products/usb-ir-transceiver.html](http://iguanaworks.net/products/usb-ir-transceiver.html)

生成摘要时出错

---

## 23. Introduction to Computer Music (2009) [pdf]

**原文标题**: Introduction to Computer Music (2009) [pdf]

**原文链接**: [https://composerprogrammer.com/introductiontocomputermusic.pdf](https://composerprogrammer.com/introductiontocomputermusic.pdf)

生成摘要时出错

---

## 24. Tracing Goroutines in Realtime with eBPF

**原文标题**: Tracing Goroutines in Realtime with eBPF

**原文链接**: [https://sazak.io/articles/tracing-goroutines-in-realtime-with-ebpf-2026-03-31](https://sazak.io/articles/tracing-goroutines-in-realtime-with-ebpf-2026-03-31)

生成摘要时出错

---

## 25. StackOverflow: Retiring the Beta Site

**原文标题**: StackOverflow: Retiring the Beta Site

**原文链接**: [https://meta.stackoverflow.com/questions/438628/retiring-the-beta-site](https://meta.stackoverflow.com/questions/438628/retiring-the-beta-site)

生成摘要时出错

---

## 26. Perfmon – Consolidate your favorite CLI monitoring tools into a single TUI

**原文标题**: Perfmon – Consolidate your favorite CLI monitoring tools into a single TUI

**原文链接**: [https://github.com/sumant1122/Perfmon](https://github.com/sumant1122/Perfmon)

生成摘要时出错

---

## 27. Aegis – open-source FPGA silicon

**原文标题**: Aegis – open-source FPGA silicon

**原文链接**: [https://github.com/MidstallSoftware/aegis](https://github.com/MidstallSoftware/aegis)

生成摘要时出错

---

## 28. Shared mutable state in Rust (2022)

**原文标题**: Shared mutable state in Rust (2022)

**原文链接**: [https://draft.ryhl.io/blog/shared-mutable-state/](https://draft.ryhl.io/blog/shared-mutable-state/)

生成摘要时出错

---

## 29. Scientists Figured Out How Eels Reproduce (2022)

**原文标题**: Scientists Figured Out How Eels Reproduce (2022)

**原文链接**: [https://www.intelligentliving.co/scientists-finally-figured-out-how-eels-reproduce/](https://www.intelligentliving.co/scientists-finally-figured-out-how-eels-reproduce/)

生成摘要时出错

---

## 30. Program analysis using random interpretation (2005) [pdf]

**原文标题**: Program analysis using random interpretation (2005) [pdf]

**原文链接**: [https://sigplan.org/Awards/Dissertation/2005_gulwani.pdf](https://sigplan.org/Awards/Dissertation/2005_gulwani.pdf)

生成摘要时出错

---

## 31. Show HN: OsintRadar – Curated directory for osint tools

**原文标题**: Show HN: OsintRadar – Curated directory for osint tools

**原文链接**: [https://osintradar.com/](https://osintradar.com/)

生成摘要时出错

---

## 32. Show HN: A game where you build a GPU

**原文标题**: Show HN: A game where you build a GPU

**原文链接**: [https://jaso1024.com/mvidia/](https://jaso1024.com/mvidia/)

生成摘要时出错

---

## 33. LLM Wiki – example of an "idea file"

**原文标题**: LLM Wiki – example of an "idea file"

**原文链接**: [https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

生成摘要时出错

---

## 34. SPF/PC v4 for MS-DOS, FreeDOS, x86

**原文标题**: SPF/PC v4 for MS-DOS, FreeDOS, x86

**原文链接**: [https://github.com/moshix/SPFPC](https://github.com/moshix/SPFPC)

生成摘要时出错

---

## 35. Common drug tests lead to tens of thousands wrongful arrests a year

**原文标题**: Common drug tests lead to tens of thousands wrongful arrests a year

**原文链接**: [https://www.cnn.com/2026/04/05/us/colorado-field-drug-test-law](https://www.cnn.com/2026/04/05/us/colorado-field-drug-test-law)

生成摘要时出错

---

## 36. How many products does Microsoft have named 'Copilot'?

**原文标题**: How many products does Microsoft have named 'Copilot'?

**原文链接**: [https://teybannerman.com/strategy/2026/03/31/how-many-microsoft-copilot-are-there.html](https://teybannerman.com/strategy/2026/03/31/how-many-microsoft-copilot-are-there.html)

生成摘要时出错

---

## 37. Apple approves driver that lets Nvidia eGPUs work with Arm Macs

**原文标题**: Apple approves driver that lets Nvidia eGPUs work with Arm Macs

**原文链接**: [https://twitter.com/__tinygrad__/status/2039213719155310736](https://twitter.com/__tinygrad__/status/2039213719155310736)

生成摘要时出错

---

## 38. Show HN: M. C. Escher spiral in WebGL inspired by 3Blue1Brown

**原文标题**: Show HN: M. C. Escher spiral in WebGL inspired by 3Blue1Brown

**原文链接**: [https://static.laszlokorte.de/escher/](https://static.laszlokorte.de/escher/)

生成摘要时出错

---

## 39. Zml-smi: universal monitoring tool for GPUs, TPUs and NPUs

**原文标题**: Zml-smi: universal monitoring tool for GPUs, TPUs and NPUs

**原文链接**: [https://zml.ai/posts/zml-smi/](https://zml.ai/posts/zml-smi/)

生成摘要时出错

---

## 40. Rubysyn: Clarifying Ruby's Syntax and Semantics

**原文标题**: Rubysyn: Clarifying Ruby's Syntax and Semantics

**原文链接**: [https://github.com/squadette/rubysyn/blob/master/README.md](https://github.com/squadette/rubysyn/blob/master/README.md)

生成摘要时出错

---

## 41. Show HN: I made open source, zero power PCB hackathon badges

**原文标题**: Show HN: I made open source, zero power PCB hackathon badges

**原文链接**: [https://github.com/KaiPereira/Overglade-Badges](https://github.com/KaiPereira/Overglade-Badges)

生成摘要时出错

---

## 42. With one million displaced, Lebanon turns to digital wallets for aid

**原文标题**: With one million displaced, Lebanon turns to digital wallets for aid

**原文链接**: [https://www.wired.com/story/with-one-million-displaced-lebanon-turns-to-digital-wallets-for-aid/](https://www.wired.com/story/with-one-million-displaced-lebanon-turns-to-digital-wallets-for-aid/)

生成摘要时出错

---

## 43. Meta, Google under attack as court cases bypass 30-year-old legal shield

**原文标题**: Meta, Google under attack as court cases bypass 30-year-old legal shield

**原文链接**: [https://www.cnbc.com/2026/04/03/meta-google-under-attack-court-cases-bypass-30-year-old-legal-shield.html](https://www.cnbc.com/2026/04/03/meta-google-under-attack-court-cases-bypass-30-year-old-legal-shield.html)

生成摘要时出错

---

## 44. AWS engineer reports PostgreSQL perf halved by Linux 7.0, fix may not be easy

**原文标题**: AWS engineer reports PostgreSQL perf halved by Linux 7.0, fix may not be easy

**原文链接**: [https://www.phoronix.com/news/Linux-7.0-AWS-PostgreSQL-Drop](https://www.phoronix.com/news/Linux-7.0-AWS-PostgreSQL-Drop)

生成摘要时出错

---

## 45. Show HN: I built a small app for FSI German Course

**原文标题**: Show HN: I built a small app for FSI German Course

**原文链接**: [https://detawk.com/](https://detawk.com/)

生成摘要时出错

---

## 46. Demonstrating Real Time AV2 Decoding on Consumer Laptops

**原文标题**: Demonstrating Real Time AV2 Decoding on Consumer Laptops

**原文链接**: [http://aomedia.org/blog%20posts/Demonstrating-Real-Time-AV2-Decoding-on-Consumer-Laptops/](http://aomedia.org/blog%20posts/Demonstrating-Real-Time-AV2-Decoding-on-Consumer-Laptops/)

生成摘要时出错

---

## 47. Electrical transformer manufacturing is throttling the electrified future

**原文标题**: Electrical transformer manufacturing is throttling the electrified future

**原文链接**: [https://www.bloomberg.com/features/2025-bottlenecks-transformers/](https://www.bloomberg.com/features/2025-bottlenecks-transformers/)

生成摘要时出错

---

## 48. Why Over-Engineering Happens

**原文标题**: Why Over-Engineering Happens

**原文链接**: [https://yusufaytas.com/why-over-engineering-happens/](https://yusufaytas.com/why-over-engineering-happens/)

生成摘要时出错

---

## 49. Embarrassingly simple self-distillation improves code generation

**原文标题**: Embarrassingly simple self-distillation improves code generation

**原文链接**: [https://arxiv.org/abs/2604.01193](https://arxiv.org/abs/2604.01193)

生成摘要时出错

---

## 50. Docker Offload

**原文标题**: Docker Offload

**原文链接**: [https://www.docker.com/blog/docker-offload-now-generally-available-the-full-power-of-docker-for-every-developer-everywhere/](https://www.docker.com/blog/docker-offload-now-generally-available-the-full-power-of-docker-for-every-developer-everywhere/)

生成摘要时出错

---

## 51. Right to repair: Why the US military can't fix much of its own equipment

**原文标题**: Right to repair: Why the US military can't fix much of its own equipment

**原文链接**: [https://taskandpurpose.com/tech-tactics/us-military-right-to-repair/](https://taskandpurpose.com/tech-tactics/us-military-right-to-repair/)

生成摘要时出错

---

## 52. Writing Lisp is AI resistant and I'm sad

**原文标题**: Writing Lisp is AI resistant and I'm sad

**原文链接**: [https://blog.djhaskin.com/blog/writing-lisp-is-ai-resistant-and-im-sad/](https://blog.djhaskin.com/blog/writing-lisp-is-ai-resistant-and-im-sad/)

生成摘要时出错

---

## 53. Unverified: What Practitioners Post About OCR, Agents, and Tables

**原文标题**: Unverified: What Practitioners Post About OCR, Agents, and Tables

**原文链接**: [https://idp-software.com/news/idp-accuracy-reckoning-2026/](https://idp-software.com/news/idp-accuracy-reckoning-2026/)

生成摘要时出错

---

## 54. Artemis II crew take “spectacular” image of Earth

**原文标题**: Artemis II crew take “spectacular” image of Earth

**原文链接**: [https://www.bbc.com/news/articles/ce8jzr423p9o](https://www.bbc.com/news/articles/ce8jzr423p9o)

生成摘要时出错

---

## 55. Advice to young people, the lies I tell myself (2024)

**原文标题**: Advice to young people, the lies I tell myself (2024)

**原文链接**: [https://jxnl.co/writing/2024/06/01/advice-to-young-people/](https://jxnl.co/writing/2024/06/01/advice-to-young-people/)

生成摘要时出错

---

## 56. Modern Generic SVGA driver for Windows 3.1

**原文标题**: Modern Generic SVGA driver for Windows 3.1

**原文链接**: [https://github.com/PluMGMK/vbesvga.drv](https://github.com/PluMGMK/vbesvga.drv)

生成摘要时出错

---

## 57. What if the browser built the UI for you?

**原文标题**: What if the browser built the UI for you?

**原文链接**: [https://jonno.nz/posts/what-if-your-browser-built-the-ui-for-you/](https://jonno.nz/posts/what-if-your-browser-built-the-ui-for-you/)

生成摘要时出错

---

## 58. Show HN: Contrapunk – Real-time counterpoint harmony from guitar input, in Rust

**原文标题**: Show HN: Contrapunk – Real-time counterpoint harmony from guitar input, in Rust

**原文链接**: [https://contrapunk.com/](https://contrapunk.com/)

生成摘要时出错

---

## 59. Dynamics of (Not) Being Perceived: Grief and Relief After Leaving Social Media

**原文标题**: Dynamics of (Not) Being Perceived: Grief and Relief After Leaving Social Media

**原文链接**: [https://networkcultures.org/thedigitalgutmensch/2026/04/02/dynamics-of-not-being-perceived-the-grief-relief-after-leaving-social-media/](https://networkcultures.org/thedigitalgutmensch/2026/04/02/dynamics-of-not-being-perceived-the-grief-relief-after-leaving-social-media/)

生成摘要时出错

---

## 60. Breaking Enigma with Index of Coincidence on a Commodore 64

**原文标题**: Breaking Enigma with Index of Coincidence on a Commodore 64

**原文链接**: [https://imapenguin.com/2026/03/breaking-enigma-with-index-of-coincidence-on-a-commodore-64/](https://imapenguin.com/2026/03/breaking-enigma-with-index-of-coincidence-on-a-commodore-64/)

生成摘要时出错

---

## 61. IBM 3270 Information Display System: Color and Programmed Symbols (1979) [pdf]

**原文标题**: IBM 3270 Information Display System: Color and Programmed Symbols (1979) [pdf]

**原文链接**: [https://bitsavers.org/pdf/ibm/3278/GA33-3056-0_3270_Information_Display_System_Color_and_Programmed_Symbols_3278_3279_3287_Sep1979.pdf](https://bitsavers.org/pdf/ibm/3278/GA33-3056-0_3270_Information_Display_System_Color_and_Programmed_Symbols_3278_3279_3287_Sep1979.pdf)

Based on the title and historical context of this 1979 IBM technical announcement, here is a concise summary:

**Summary: IBM 3270 Information Display System (1979)**

This document details a significant technological milestone for the IBM 3270 family: the introduction of multi-color capabilities and user-defined character sets. The announcement centers on the **IBM 3279 Color Display Station** and the **IBM 3287 Printer**, marking a transition from traditional monochrome (green-screen) environments to high-contrast color data presentation.

**Key Features and Innovations:**

*   **Seven-Color Support:** The system introduced a palette of seven colors (Red, Green, Blue, White, Pink, Yellow, and Turquoise). This was designed to improve operator efficiency by using color to categorize data, highlight errors, and distinguish between protected and unprotected fields.
*   **Programmed Symbols (PS):** Perhaps the most significant technical leap, Programmed Symbols allowed the host computer to download custom-defined character sets to the terminal. This enabled the display of graphics, mathematical symbols, and non-Latin alphabets. It effectively allowed the 3270 to move beyond simple text into the realm of business graphics and specialized data visualization.
*   **Extended Attributes:** The update introduced new "Extended Highlighting" features, including underscoring, blinking, and reverse video. These attributes gave programmers more granular control over how information was prioritized on the screen.
*   **System Integration:** The document outlines how these features integrated with existing IBM architectures (like System/370) via the 3274 and 3276 Control Units, ensuring that the new color features were backward compatible with existing applications while providing a path for modernized UI design.

In summary, the 1979 enhancements transformed the 3270 system from a rigid text-entry tool into a versatile display system capable of complex data representation and improved human-computer interaction.

---

## 62. Costco sued for seeking refunds on tariffs customers paid

**原文标题**: Costco sued for seeking refunds on tariffs customers paid

**原文链接**: [https://arstechnica.com/tech-policy/2026/03/costco-sued-for-seeking-refunds-on-tariffs-customers-paid/](https://arstechnica.com/tech-policy/2026/03/costco-sued-for-seeking-refunds-on-tariffs-customers-paid/)

生成摘要时出错

---

## 63. Banray.eu: Raising awareness of the terrible idea that is always-on AI glasses

**原文标题**: Banray.eu: Raising awareness of the terrible idea that is always-on AI glasses

**原文链接**: [https://banray.eu/en/index.html](https://banray.eu/en/index.html)

生成摘要时出错

---

## 64. SpaceX and OpenAI: The Mega IPO Grift [video]

**原文标题**: SpaceX and OpenAI: The Mega IPO Grift [video]

**原文链接**: [https://www.youtube.com/watch?v=iOyFja87uyw](https://www.youtube.com/watch?v=iOyFja87uyw)

生成摘要时出错

---

## 65. Components of a Coding Agent

**原文标题**: Components of a Coding Agent

**原文链接**: [https://magazine.sebastianraschka.com/p/components-of-a-coding-agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)

生成摘要时出错

---

## 66. Google releases Gemma 4 open models

**原文标题**: Google releases Gemma 4 open models

**原文链接**: [https://deepmind.google/models/gemma/gemma-4/](https://deepmind.google/models/gemma/gemma-4/)

生成摘要时出错

---

## 67. Claude Code Found a Linux Vulnerability Hidden for 23 Years

**原文标题**: Claude Code Found a Linux Vulnerability Hidden for 23 Years

**原文链接**: [https://mtlynch.io/claude-code-found-linux-vulnerability/](https://mtlynch.io/claude-code-found-linux-vulnerability/)

生成摘要时出错

---

## 68. The machines are fine. I'm worried about us

**原文标题**: The machines are fine. I'm worried about us

**原文链接**: [https://ergosphere.blog/posts/the-machines-are-fine/](https://ergosphere.blog/posts/the-machines-are-fine/)

生成摘要时出错

---

## 69. Show HN: sllm – Split a GPU node with other developers, unlimited tokens

**原文标题**: Show HN: sllm – Split a GPU node with other developers, unlimited tokens

**原文链接**: [https://sllm.cloud](https://sllm.cloud)

生成摘要时出错

---

## 70. Emotion concepts and their function in a large language model

**原文标题**: Emotion concepts and their function in a large language model

**原文链接**: [https://www.anthropic.com/research/emotion-concepts-function](https://www.anthropic.com/research/emotion-concepts-function)

生成摘要时出错

---

## 71. Power-washing, pool-cleaning and mowing – playing games about mundane jobs

**原文标题**: Power-washing, pool-cleaning and mowing – playing games about mundane jobs

**原文链接**: [https://www.bbc.com/news/articles/cj60r2kdnw1o](https://www.bbc.com/news/articles/cj60r2kdnw1o)

生成摘要时出错

---

## 72. EPA official in charge of methane regulations was an oil and gas lobbyist

**原文标题**: EPA official in charge of methane regulations was an oil and gas lobbyist

**原文链接**: [https://www.propublica.org/article/trump-epa-methane-deregulation-aaron-szabo-oil-gas-axpc](https://www.propublica.org/article/trump-epa-methane-deregulation-aaron-szabo-oil-gas-axpc)

生成摘要时出错

---

## 73. Elizabeth I's Manuscript of Pierre Boaistuau's Histoires Prodigieuses (1559)

**原文标题**: Elizabeth I's Manuscript of Pierre Boaistuau's Histoires Prodigieuses (1559)

**原文链接**: [https://publicdomainreview.org/collection/histoires-prodigieuses/](https://publicdomainreview.org/collection/histoires-prodigieuses/)

生成摘要时出错

---

## 74. The Indie Internet Index – submit your favorite sites

**原文标题**: The Indie Internet Index – submit your favorite sites

**原文链接**: [https://iii.social](https://iii.social)

生成摘要时出错

---

## 75. VR Realizes the Cyberspace Metaphor

**原文标题**: VR Realizes the Cyberspace Metaphor

**原文链接**: [https://yadin.com/notes/vr-disrupts/](https://yadin.com/notes/vr-disrupts/)

生成摘要时出错

---

## 76. Ruckus: Racket for iOS

**原文标题**: Ruckus: Racket for iOS

**原文链接**: [https://ruckus.defn.io/](https://ruckus.defn.io/)

生成摘要时出错

---

## 77. Japanese, French and Omani Vessels Cross Strait of Hormuz

**原文标题**: Japanese, French and Omani Vessels Cross Strait of Hormuz

**原文链接**: [https://japantoday.com/category/politics/japanese-french-and-omani-vessels-cross-the-strait-of-hormuz](https://japantoday.com/category/politics/japanese-french-and-omani-vessels-cross-the-strait-of-hormuz)

生成摘要时出错

---

## 78. When legal sports betting surges, so do Americans' financial problems

**原文标题**: When legal sports betting surges, so do Americans' financial problems

**原文链接**: [https://www.npr.org/2026/04/04/nx-s1-5773354/legal-sports-betting-research-credit-bankruptcy](https://www.npr.org/2026/04/04/nx-s1-5773354/legal-sports-betting-research-credit-bankruptcy)

生成摘要时出错

---

## 79. Drivers May Soon Pay Taxes Based on How Much Their Car Weighs

**原文标题**: Drivers May Soon Pay Taxes Based on How Much Their Car Weighs

**原文链接**: [https://www.autoblog.com/news/drivers-may-soon-pay-taxes-based-on-how-much-their-car-weighs](https://www.autoblog.com/news/drivers-may-soon-pay-taxes-based-on-how-much-their-car-weighs)

生成摘要时出错

---

## 80. Some Unusual Trees

**原文标题**: Some Unusual Trees

**原文链接**: [https://thoughts.wyounas.com/p/some-unusual-trees](https://thoughts.wyounas.com/p/some-unusual-trees)

生成摘要时出错

---

## 81. Roogle: a Rust API search engine

**原文标题**: Roogle: a Rust API search engine

**原文链接**: [https://github.com/roogle-rs/roogle](https://github.com/roogle-rs/roogle)

生成摘要时出错

---

## 82. Author of "Careless People" banned from saying anything negative about Meta

**原文标题**: Author of "Careless People" banned from saying anything negative about Meta

**原文链接**: [https://www.thetimes.com/uk/technology-uk/article/sarah-wynn-williams-careless-people-meta-nrffdfpmf](https://www.thetimes.com/uk/technology-uk/article/sarah-wynn-williams-careless-people-meta-nrffdfpmf)

生成摘要时出错

---

## 83. How Pope Leo is pushing back on divine justification of war

**原文标题**: How Pope Leo is pushing back on divine justification of war

**原文链接**: [https://www.cnn.com/2026/04/04/middleeast/pope-leo-iran-war-analysis-latam-intl](https://www.cnn.com/2026/04/04/middleeast/pope-leo-iran-war-analysis-latam-intl)

生成摘要时出错

---

## 84. Microsoft terms say Copilot is for entertainment purposes only, not serious use

**原文标题**: Microsoft terms say Copilot is for entertainment purposes only, not serious use

**原文链接**: [https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-says-copilot-is-for-entertainment-purposes-only-not-serious-use-firm-pushing-ai-hard-to-consumers-tells-users-not-to-rely-on-it-for-important-advice](https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-says-copilot-is-for-entertainment-purposes-only-not-serious-use-firm-pushing-ai-hard-to-consumers-tells-users-not-to-rely-on-it-for-important-advice)

生成摘要时出错

---

## 85. Large language models are not the problem

**原文标题**: Large language models are not the problem

**原文链接**: [https://www.nature.com/articles/s41550-026-02837-2](https://www.nature.com/articles/s41550-026-02837-2)

生成摘要时出错

---

## 86. OpenClaw privilege escalation vulnerability

**原文标题**: OpenClaw privilege escalation vulnerability

**原文链接**: [https://nvd.nist.gov/vuln/detail/CVE-2026-33579](https://nvd.nist.gov/vuln/detail/CVE-2026-33579)

生成摘要时出错

---

## 87. Iranian missile blitz takes down AWS data centers in Bahrain and Dubai

**原文标题**: Iranian missile blitz takes down AWS data centers in Bahrain and Dubai

**原文链接**: [https://www.tomshardware.com/tech-industry/iranian-missile-blitz-takes-down-aws-data-centers-in-bahrain-and-dubai-amazon-declares-hard-down-status-for-multiple-zones](https://www.tomshardware.com/tech-industry/iranian-missile-blitz-takes-down-aws-data-centers-in-bahrain-and-dubai-amazon-declares-hard-down-status-for-multiple-zones)

生成摘要时出错

---

## 88. Plague Ships (2020)

**原文标题**: Plague Ships (2020)

**原文链接**: [https://www.afloat.com.au/feature/plague-ships/](https://www.afloat.com.au/feature/plague-ships/)

生成摘要时出错

---

## 89. Decisions that eroded trust in Azure – by a former Azure Core engineer

**原文标题**: Decisions that eroded trust in Azure – by a former Azure Core engineer

**原文链接**: [https://isolveproblems.substack.com/p/how-microsoft-vaporized-a-trillion](https://isolveproblems.substack.com/p/how-microsoft-vaporized-a-trillion)

生成摘要时出错

---

## 90. Show HN: I built a frontpage for personal blogs

**原文标题**: Show HN: I built a frontpage for personal blogs

**原文链接**: [https://text.blogosphere.app/](https://text.blogosphere.app/)

生成摘要时出错

---

## 91. Brain scans reveal how to enters a psychedelic-like trance without drugs

**原文标题**: Brain scans reveal how to enters a psychedelic-like trance without drugs

**原文链接**: [https://www.psypost.org/brain-scans-reveal-how-a-woman-voluntarily-enters-a-psychedelic-like-trance-without-drugs/](https://www.psypost.org/brain-scans-reveal-how-a-woman-voluntarily-enters-a-psychedelic-like-trance-without-drugs/)

生成摘要时出错

---

## 92. iNaturalist

**原文标题**: iNaturalist

**原文链接**: [https://www.inaturalist.org/](https://www.inaturalist.org/)

生成摘要时出错

---

## 93. Show HN: TurboQuant-WASM – Google's vector quantization in the browser

**原文标题**: Show HN: TurboQuant-WASM – Google's vector quantization in the browser

**原文链接**: [https://github.com/teamchong/turboquant-wasm](https://github.com/teamchong/turboquant-wasm)

生成摘要时出错

---

## 94. Post Mortem: axios NPM supply chain compromise

**原文标题**: Post Mortem: axios NPM supply chain compromise

**原文链接**: [https://github.com/axios/axios/issues/10636](https://github.com/axios/axios/issues/10636)

生成摘要时出错

---

## 95. The CMS is dead, long live the CMS

**原文标题**: The CMS is dead, long live the CMS

**原文链接**: [https://next.jazzsequence.com/posts/the-cms-is-dead-long-live-the-cms](https://next.jazzsequence.com/posts/the-cms-is-dead-long-live-the-cms)

生成摘要时出错

---

## 96. Why are we still using Markdown?

**原文标题**: Why are we still using Markdown?

**原文链接**: [https://bgslabs.org/blog/why-are-we-using-markdown/](https://bgslabs.org/blog/why-are-we-using-markdown/)

生成摘要时出错

---

## 97. Scientists observe an immune signaling complex forming inside cells

**原文标题**: Scientists observe an immune signaling complex forming inside cells

**原文链接**: [https://news.stanford.edu/stories/2026/03/immune-response-inside-cells-inflammation-research](https://news.stanford.edu/stories/2026/03/immune-response-inside-cells-inflammation-research)

生成摘要时出错

---

## 98. Ubuntu now requires more RAM than Windows 11

**原文标题**: Ubuntu now requires more RAM than Windows 11

**原文链接**: [https://www.howtogeek.com/ubuntu-now-requires-more-ram-than-windows-11/](https://www.howtogeek.com/ubuntu-now-requires-more-ram-than-windows-11/)

生成摘要时出错

---

## 99. Getting Claude to QA its own work

**原文标题**: Getting Claude to QA its own work

**原文链接**: [https://www.skyvern.com/blog/getting-claude-to-qa-its-own-work/](https://www.skyvern.com/blog/getting-claude-to-qa-its-own-work/)

生成摘要时出错

---

## 100. The house is a work of art: Frank Lloyd Wright

**原文标题**: The house is a work of art: Frank Lloyd Wright

**原文链接**: [https://aeon.co/essays/frank-lloyd-wright-as-a-mirror-of-the-american-condition](https://aeon.co/essays/frank-lloyd-wright-as-a-mirror-of-the-american-condition)

生成摘要时出错

---

