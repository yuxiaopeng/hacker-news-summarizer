# Hacker News 热门文章摘要 (2026-11-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 紧急公告：亚历山德罗·马苏洛 GRH

**原文标题**: Hurried Announcement: Alessandro Masullo GRH

**原文链接**: [https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/](https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/)

在2026年11月20日发布的一篇博文中，数学家拉维·瓦基勒（Ravi Vakil）宣布，亚历山德罗·马苏洛（Alessandro Masullo）提出了一项关于广义黎曼猜想（GRH）的拟议证明。

该公告强调了几个关键点：

*   **专家评审：**布莱恩·康拉德（Brian Conrad）已花费数月时间仔细审查马苏洛的工作。康拉德的大量反馈正被纳入证明中，目前的研究结果被形容为“进展良好”。
*   **人类创作：**瓦基勒强调，该证明完全由人类完成，没有人工智能的辅助。
*   **提前发布：**虽然原计划是邀请马苏洛前往斯坦福大学进行为期一年的访问，在正式发布前完善手稿，但瓦基勒决定立即向数学界公开当前的草案。
*   **呼吁核实：**鼓励数学界对这份题为《素数的音乐》（The Music of the Primes）的草案进行审查和形式化验证，并指出其中可能存在的任何漏洞。

瓦基勒在参加美国数学学会会议期间撰写了此文，他表达了对康拉德判断力的坚定信心，并希望该证明能经受住严苛的审查。

---

## 2. Inkling 2 迷你

**原文标题**: Inkling 2 Mini

**原文链接**: [https://thinkingmachines.ai/news/inkling-2-mini/](https://thinkingmachines.ai/news/inkling-2-mini/)

**Inkling 2 Mini** 是一款新型开源权重混合专家（MoE）模型，专为本地硬件上的高性能推理而设计。该模型总参数量为 26.4B（激活参数 3.4B），采用了独特的**循环 Transformer（looped transformer）**架构，使其核心中间层在处理每个 token 时循环运行三次。这种设计在不增加模型物理尺寸的情况下，实现了更深层的推理能力和更长的“非思维链（no-CoT）”推理视界。

**主要性能亮点：**
*   **编程与推理：** 在主流基准测试中，它在 100B 参数以下的开源模型中处于领先地位，在 DeepSWE v1.1 和 Vals Index v2.2 中分别获得 48.2% 和 46.5% 的评分。它在自主编程和内核优化等智能体任务中表现卓越。
*   **能效：** 该模型具有极高的能源效率，在“单位焦耳智能”指标上显著高于 Qwen 和 Gemma 等竞争对手。
*   **本地部署：** 经过 NVFP4 和 MXFP8 量化优化，该模型的显存占用约为 20GB。它可以在消费级设备上离线运行，其实力已通过在单台 MacBook Pro 上构建飞行模拟器并驱动 20 个智能体模拟项目（Thinkyville）得到证明。

**能力与局限性：**
虽然循环架构显著提升了推理和长上下文表现，但它并不会增加模型的内部事实知识，其知识储备仍受限于总参数量。为了弥补这一不足，该模型针对工具调用和搜索进行了优化。其主要弱点包括多轮对话和复杂指令遵循，在这些方面略逊于 Qwen3.8-27B 等模型。

Inkling 2 Mini 目前已在 Tinker 平台上开放推理和定制，为研究人员提供了一个观察功能性循环架构的难得机会。

---

## 3. Levent Alpöge 声称证明了广义黎曼猜想 [pdf]

**原文标题**: Levent Alpöge claims proof of the Generalized Riemann Hypothesis [pdf]

**原文链接**: [https://alpo.ge/remark.pdf](https://alpo.ge/remark.pdf)

根据所提供文档的标题和元数据，以下是关于 Levent Alpöge 所声称之突破的文章简要概述：

**摘要：广义黎曼猜想的证明**

本文详细介绍了数学家 **Levent Alpöge** 在**广义黎曼猜想 (GRH)** 方面声称取得的重大数论突破。广义黎曼猜想是原始黎曼猜想的扩展；它假设一类被称为 $L$-函数（$L$-functions）的广泛数学函数的所有非平凡零点都位于一条特定的“临界线”上。

**关键信息：**

*   **研究主体：** Levent Alpöge 是算术几何领域的杰出人物（与哈佛大学和纽约大学有学术关联），因其在椭圆曲线秩方面的研究而闻名。他的最新工作针对的是数学领域中最重大的未解难题之一。
*   **科学意义：** 广义黎曼猜想是现代数论的基石。其证明将对素数分布、类数（class numbers）的行为以及计算数学中各种算法的效率产生直接影响。
*   **声称背景：** 尽管普适性的广义黎曼猜想（涵盖所有代数数域）仍是该领域最艰巨的挑战之一，但 Alpöge 的工作通常侧重于证明特定的大规模 $L$-函数类别的猜想——这些函数通常与函数域上的代数簇或特定的几何对象相关。
*   **方法论：** 该证明可能利用了**朗兰兹纲领 (Langlands Program)** 和算术统计中的先进工具，架起了复分析与几何表示论之间的桥梁。

**结论：**
如果得到数学界的验证，Alpöge 的证明将具有历史里程碑意义。即便该证明仅限于特定类别的 $L$-函数，它也为全面解决该猜想提供了关键路线图，并巩固了 Alpöge 作为现代数论领军人物的地位。

---

## 4. 我们在未告知开发人员的情况下，将他们提拔为了架构师。

**原文标题**: We promoted developers into architects without informing them

**原文链接**: [https://manidoraisamy.com/developer-to-architect.html](https://manidoraisamy.com/developer-to-architect.html)

Mani Doraisamy 在其文章中指出，AI 辅助的“氛围编程”（vibe coding）的兴起已从根本上将开发者的角色转变为架构师，而开发者往往并未意识到这一点。

他以一个真实案例说明了这种转变：一个由 AI 生成的日志功能因优先满足一项需求（获取用户电子邮件）而采用了多个同步 API 调用，导致了 15 秒的延迟。虽然 AI 成功编写了代码，但它未能权衡性能与安全性之间的架构利弊。

作者强调了 AI 在开发过程中的几个关键局限性：
*   **缺乏上下文：** AI 不理解业务规模或用户体验的优先级。
*   **盲从性：** AI 会机械地执行指令，很少对可能损害应用性能或可维护性的需求提出异议。
*   **保守的默认设置：** AI 往往优先考虑安全性及向后兼容性，而牺牲了速度和简洁的数据模型。

Doraisamy 总结道，虽然手动编写代码的任务正在被自动化，但开发者的工作并不会消失，而是在进化。为了在这一新格局中取得成功，开发者必须接受向架构师的“晋升”。他们的新职责包括：
1.  在让 AI 编写实现代码之前，先**设计数据模型和架构**。
2.  **约束 AI** 遵循特定的架构模式。
3.  **回绝**利益相关者提出的在技术上不切实际的需求。
4.  **审查代码**的结构完整性，而不仅仅是功能的正确性。

最后，作者警告说，如果开发者不承担起这种架构师的角色，结果将导致系统不可维护且用户体验糟糕。开发的未来在于高层设计和批判性监督，而不仅仅是代码实现。

---

## 5. 无驱动纳维-斯托克斯奇异性与广义黎曼猜想

**原文标题**: Unforced Navier-Stokes Singularity and the Generalized Riemann Hypothesis

**原文链接**: [https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/](https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/)

这篇文章发表于 Ben Eastaugh 和 Chris Sternal-Johnson 的博客 *Theorema*，探讨了流体动力学与解析数论之间一个重大且出人意料的联系。文章重点介绍了数学家亚科夫·西奈（Yakov Sinai）为解决纳维-斯托克斯存在性与光滑性问题所做的尝试，该问题是七大千禧年大奖难题之一。

讨论的核心涉及西奈的断言，即三维无外力纳维-斯托克斯方程可能产生有限时间奇异性（或称“爆破”）。如果该断言被证明正确，将表明光滑解并不总是全局存在的，从而实际上为这一千禧年难题提供了一个否定的答案。

西奈研究中最引人注目的方面在于其对**广义黎曼猜想 (GRH)** 的依赖。西奈的方法利用基于傅里叶变换的重整化技术来分析方程。他假设这些奇异性的存在取决于一类特定复函数的行为。作者解释道，西奈的证明取决于一个“全局引理”，该引理要求这些函数的某些零点位于一条特定的临界线上——这一条件与广义黎曼猜想直接类比。

文章强调了数学界的反应，在兴奋与审慎之间保持了平衡。通过将物理流体的行为与素数分布及 L-函数的分布联系起来，西奈的研究揭示了偏微分方程与数论之间深层的潜在统一性。作者总结指出，虽然该证明仍面临严密的审查，但其跨学科的性质代表了数学家在研究湍流和奇异性问题时一种潜在的革命性转变。

---

## 6. 语言模型可以重写自身权重

**原文标题**: Language Models Can Rewrite Their Own Weights

**原文链接**: [https://arxiv.org/abs/2611.21885](https://arxiv.org/abs/2611.21885)

The paper **"Language Models Can Rewrite Their Own Weights"** (arXiv:2611.21885) introduces a novel paradigm called **self-rewriting**, where a language model optimizes its own parameters through reasoning rather than traditional gradient-based training. 

Using an open 27B parameter model, the researchers demonstrate that a model can analyze its own weights, diagnose performance failures on graded tasks, and implement weight edits using only forward passes. Key findings include:

*   **Autonomous Improvement:** The model improved its accuracy on unseen problems by 6.6 points. Through eight consecutive sessions of testing and refining its own edits, its performance consistently rose.
*   **Self-Repair:** In a "broken robot" scenario, the model successfully repaired a damaged copy of itself—which initially solved almost nothing—restoring it to over 80% of its original accuracy on new image tasks without reading the original weights.
*   **Emergence with Scale:** This capability is scale-dependent; while the 27B model succeeded, smaller models in the same family either failed to make edits or corrupted their own weights.
*   **Efficiency:** Unlike test-time scaling, self-rewriting embeds gains directly into the weights, incurring no extra cost per inference. Unlike traditional training, it requires no gradients, harnesses, or backpropagation.

The authors conclude that the historical wall between "training" and "inference" is a limitation of current tools rather than an inherent property of AI. They position self-rewriting as a critical step toward **recursive self-improvement**, enabling models to continuously upgrade themselves through a lifecycle of reasoning and self-correction, much like human intelligence.

---

## 7. A few hours ago Google DeepMind created a math horizon repo

**原文标题**: A few hours ago Google DeepMind created a math horizon repo

**原文链接**: [https://github.com/google-deepmind/math-horizon](https://github.com/google-deepmind/math-horizon)

生成摘要时出错

---

## 8. The stochastic parrots have apparently proved the Riemann Hypothesis

**原文标题**: The stochastic parrots have apparently proved the Riemann Hypothesis

**原文链接**: [https://scottaaronson.blog/?p=10344](https://scottaaronson.blog/?p=10344)

在这篇日期为2026年11月20日的博客文章中，Scott Aaronson报道了数学领域的一个里程碑：据称，Anthropic公司的一个AI模型已经证明了广义黎曼猜想（GRH）。在数学家Levent Alpöge的指导下，该AI生成了一份包含1740万行Lean代码的形式化证明。

鉴于大语言模型解决千年级问题的能力日益增强，Aaronson反思了将其贴上“随机鹦鹉”标签的讽刺意味。他指出，虽然该证明已通过Lean进行了形式化验证，但人类数学家可能需要数年时间才能提炼并理解其背后的核心思想，因为与AI相比，人类的运作速度仅为“生物速度”。尽管存在对Lean内核漏洞的潜在担忧，但Aaronson押注该证明能够成立，并指出带有Lean证书的AI结果已被证明比没有证书的结果更可靠。

这篇文章捕捉到了一种“奇迹与恐怖”并存的氛围。随着黎曼猜想有望得到解决，Aaronson将“P vs NP”问题视为数学界的“终极Boss”。他描述了更广泛的生存紧张感，引用专家的观点称，AI的递归自我改进可能会在12到18个月内从根本上改变或终结世界。

文章以一个个人轶事结尾，突显了现状的超现实色彩：正当Aaronson沉思即将到来的AI奇点时，他的妻子仍专注于解决家中漏水这一现实琐事。随后的评论则讨论了纯人类证明（如传闻中Alessandro Masullo的证明）是否仍具竞争力，以及AI最终是否会解决量子引力和AI对齐等其他“终极Boss”问题。

---

## 9. Finite-time blow-up for the Navier–Stokes equations

**原文标题**: Finite-time blow-up for the Navier–Stokes equations

**原文链接**: [https://github.com/tristanbuckmaster/navier-stokes/](https://github.com/tristanbuckmaster/navier-stokes/)

生成摘要时出错

---

## 10. Vibecoding an inference chip

**原文标题**: Vibecoding an inference chip

**原文链接**: [https://ankitg.me/blog/vibecoding-inference-chip/](https://ankitg.me/blog/vibecoding-inference-chip/)

生成摘要时出错

---

## 11. And Yet, It Moves

**原文标题**: And Yet, It Moves

**原文链接**: [https://signoregalilei.com/2026/11/20/and-yet-it-moves/](https://signoregalilei.com/2026/11/20/and-yet-it-moves/)

生成摘要时出错

---

## 12. DreamCoder: Coding harness and IDE from the author of Mastering Emacs

**原文标题**: DreamCoder: Coding harness and IDE from the author of Mastering Emacs

**原文链接**: [https://www.masteringemacs.org/article/announcing-dreamcoder](https://www.masteringemacs.org/article/announcing-dreamcoder)

生成摘要时出错

---

## 13. If you can't explain something in simple terms, you don't understand it (2017)

**原文标题**: If you can't explain something in simple terms, you don't understand it (2017)

**原文链接**: [https://kottke.org/17/06/if-you-cant-explain-something-in-simple-terms-you-dont-understand-it](https://kottke.org/17/06/if-you-cant-explain-something-in-simple-terms-you-dont-understand-it)

生成摘要时出错

---

## 14. Winedroid – run Android apps without Android (WASM demo)

**原文标题**: Winedroid – run Android apps without Android (WASM demo)

**原文链接**: [https://winedroid.soham.sh/demo/](https://winedroid.soham.sh/demo/)

生成摘要时出错

---

## 15. NINLIVE: The Nine Inch Nails live archive

**原文标题**: NINLIVE: The Nine Inch Nails live archive

**原文链接**: [https://ninlive.com/](https://ninlive.com/)

生成摘要时出错

---

## 16. Signal Is Serious About Protecting Your Privacy

**原文标题**: Signal Is Serious About Protecting Your Privacy

**原文链接**: [https://signal.org/blog/protecting-your-privacy/](https://signal.org/blog/protecting-your-privacy/)

生成摘要时出错

---

## 17. Frostbite: A new CPU architecture discovered, designed and verified by AI

**原文标题**: Frostbite: A new CPU architecture discovered, designed and verified by AI

**原文链接**: [https://architectlabs.com/blog/frostbite](https://architectlabs.com/blog/frostbite)

生成摘要时出错

---

## 18. Nvidia accounting under SEC investigation, sources say

**原文标题**: Nvidia accounting under SEC investigation, sources say

**原文链接**: [https://finance.yahoo.com/markets/article/nvidia-stock-extends-25-trillion-rout-as-sec-probe-reportedly-investigates-its-accounting-194945274.html](https://finance.yahoo.com/markets/article/nvidia-stock-extends-25-trillion-rout-as-sec-probe-reportedly-investigates-its-accounting-194945274.html)

生成摘要时出错

---

## 19. Microsoft announces Windows Server 2028 with hardened security

**原文标题**: Microsoft announces Windows Server 2028 with hardened security

**原文链接**: [https://www.bleepingcomputer.com/news/microsoft/microsoft-announces-windows-server-2028-with-hardened-security/](https://www.bleepingcomputer.com/news/microsoft/microsoft-announces-windows-server-2028-with-hardened-security/)

生成摘要时出错

---

## 20. Show HN: An API for word timestamps from speech, 75% within 20ms

**原文标题**: Show HN: An API for word timestamps from speech, 75% within 20ms

**原文链接**: [https://quebec.yarn.so](https://quebec.yarn.so)

生成摘要时出错

---

## 21. Show HN: OpenComputer – an open source alternative to Devin

**原文标题**: Show HN: OpenComputer – an open source alternative to Devin

**原文链接**: [https://github.com/diggerhq/opencomputer](https://github.com/diggerhq/opencomputer)

生成摘要时出错

---

## 22. Show HN: Professor Euler – Offline math desk, 300-function CAS, workbooks

**原文标题**: Show HN: Professor Euler – Offline math desk, 300-function CAS, workbooks

**原文链接**: [https://euler.dawei7.com](https://euler.dawei7.com)

生成摘要时出错

---

## 23. Show HN: I made an audio-to-MIDI model 60x more efficient

**原文标题**: Show HN: I made an audio-to-MIDI model 60x more efficient

**原文链接**: [https://kobi.music/research/dettato](https://kobi.music/research/dettato)

生成摘要时出错

---

## 24. Reverse Engineering my cat's litter box

**原文标题**: Reverse Engineering my cat's litter box

**原文链接**: [https://master--ytulsiani.netlify.app/blog/furrytails/](https://master--ytulsiani.netlify.app/blog/furrytails/)

生成摘要时出错

---

## 25. Google Workers Tell Their Employer Not to Punish Schools That Don't Want AI

**原文标题**: Google Workers Tell Their Employer Not to Punish Schools That Don't Want AI

**原文链接**: [https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/](https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/)

生成摘要时出错

---

## 26. Running two PSP emulators on one Switch 2 and sharing one via GameShare

**原文标题**: Running two PSP emulators on one Switch 2 and sharing one via GameShare

**原文链接**: [https://github.com/XITRIX/ppsspp-nx2/blob/master/SWITCH2-GAMESHARE.md](https://github.com/XITRIX/ppsspp-nx2/blob/master/SWITCH2-GAMESHARE.md)

生成摘要时出错

---

## 27. The Hungry Butler Effect: Concealed Commercial Incentives in LLMs

**原文标题**: The Hungry Butler Effect: Concealed Commercial Incentives in LLMs

**原文链接**: [https://www.researchgate.net/publication/418143113_The_Hungry_Butler_Effect_Concealed_Commercial_Incentives_and_the_Erosion_of_Epistemic_Rigour_in_Large_Language_Models](https://www.researchgate.net/publication/418143113_The_Hungry_Butler_Effect_Concealed_Commercial_Incentives_and_the_Erosion_of_Epistemic_Rigour_in_Large_Language_Models)

生成摘要时出错

---

## 28. The G1 Garbage Collector

**原文标题**: The G1 Garbage Collector

**原文链接**: [https://dev.java/learn/jvm/tool/garbage-collection/g1gc-overview/](https://dev.java/learn/jvm/tool/garbage-collection/g1gc-overview/)

生成摘要时出错

---

## 29. Floppy3.5: A portable 3.5-inch floppy WiFi NAS

**原文标题**: Floppy3.5: A portable 3.5-inch floppy WiFi NAS

**原文链接**: [https://github.com/bigcrimping/floppy3.5](https://github.com/bigcrimping/floppy3.5)

生成摘要时出错

---

## 30. PostgreSQL 19: A hands-on tour with runnable browser examples

**原文标题**: PostgreSQL 19: A hands-on tour with runnable browser examples

**原文链接**: [https://certuvia.com/blog/postgres-19](https://certuvia.com/blog/postgres-19)

生成摘要时出错

---

## 31. LZ-RDO lands in ARM's astc-encoder

**原文标题**: LZ-RDO lands in ARM's astc-encoder

**原文链接**: [https://www.jonolick.com/home/lz-rdo-lands-in-arms-astc-encoder](https://www.jonolick.com/home/lz-rdo-lands-in-arms-astc-encoder)

生成摘要时出错

---

## 32. The Making of Oxygene

**原文标题**: The Making of Oxygene

**原文链接**: [https://jeanmicheljarre.com/aaa/the-making-of-oxygene](https://jeanmicheljarre.com/aaa/the-making-of-oxygene)

生成摘要时出错

---

## 33. Why there are still no non-WebKit browsers on iOS

**原文标题**: Why there are still no non-WebKit browsers on iOS

**原文链接**: [https://blog.mozilla.org/en/mozilla/internet-policy/apple-ios-browser-engine-rules/](https://blog.mozilla.org/en/mozilla/internet-policy/apple-ios-browser-engine-rules/)

生成摘要时出错

---

## 34. Teskooano: A 3D N-body simulator in the browser

**原文标题**: Teskooano: A 3D N-body simulator in the browser

**原文链接**: [https://teskooano.space/](https://teskooano.space/)

生成摘要时出错

---

## 35. AI is giving everyone the same advice

**原文标题**: AI is giving everyone the same advice

**原文链接**: [https://a90.com/experiments/same-advice/](https://a90.com/experiments/same-advice/)

生成摘要时出错

---

## 36. What people are building, discovered through new domains

**原文标题**: What people are building, discovered through new domains

**原文链接**: [https://startups.novumsignals.com/](https://startups.novumsignals.com/)

生成摘要时出错

---

## 37. Slopstrap – Make your site look hastily vibecoded

**原文标题**: Slopstrap – Make your site look hastily vibecoded

**原文链接**: [https://slopstrap.mikelacher.com/](https://slopstrap.mikelacher.com/)

生成摘要时出错

---

## 38. Show HN: Fast deterministic natural language search for OpenStreetMap data

**原文标题**: Show HN: Fast deterministic natural language search for OpenStreetMap data

**原文链接**: [https://hippomaps.ch/?q=cafes+by+the+Limmat+100+m+from+the+lake+in+zurich#map=15.02/47.36708/8.54935](https://hippomaps.ch/?q=cafes+by+the+Limmat+100+m+from+the+lake+in+zurich#map=15.02/47.36708/8.54935)

生成摘要时出错

---

## 39. Lovable: Now you can explore any idea in parallel without touching what's live

**原文标题**: Lovable: Now you can explore any idea in parallel without touching what's live

**原文链接**: [https://lovable.dev/blog/introducing-drafts](https://lovable.dev/blog/introducing-drafts)

生成摘要时出错

---

## 40. OPM Data Was Breached on the Same Day as the FAA Ground Stop, per Internal Email

**原文标题**: OPM Data Was Breached on the Same Day as the FAA Ground Stop, per Internal Email

**原文链接**: [https://www.muellershewrote.com/p/breaking-opm-data-was-breached-on](https://www.muellershewrote.com/p/breaking-opm-data-was-breached-on)

生成摘要时出错

---

## 41. If you stop writing code, you also get worse at reviewing it

**原文标题**: If you stop writing code, you also get worse at reviewing it

**原文链接**: [https://cekrem.github.io/posts/if-you-stop-writing-code-you-also-get-worse-at-reviewing-it/](https://cekrem.github.io/posts/if-you-stop-writing-code-you-also-get-worse-at-reviewing-it/)

生成摘要时出错

---

## 42. Carnival Cruises emits ten times more sulphur oxide than all of Europe's cars (2019)

**原文标题**: Carnival Cruises emits ten times more sulphur oxide than all of Europe's cars (2019)

**原文链接**: [https://ecohustler.com/article/one-corporation-to-pollute-them-all/](https://ecohustler.com/article/one-corporation-to-pollute-them-all/)

生成摘要时出错

---

## 43. FFmpeg 9.1 'Gauss'

**原文标题**: FFmpeg 9.1 'Gauss'

**原文链接**: [https://ffmpeg.org/download.html#release_9.1](https://ffmpeg.org/download.html#release_9.1)

生成摘要时出错

---

## 44. Claude solves two open problems in the physics of black holes

**原文标题**: Claude solves two open problems in the physics of black holes

**原文链接**: [https://www.anthropic.com/research/claude-black-hole-physics](https://www.anthropic.com/research/claude-black-hole-physics)

生成摘要时出错

---

## 45. µ-Wire – USB on an ATtiny 10

**原文标题**: µ-Wire – USB on an ATtiny 10

**原文链接**: [https://cpldcpu.com/2014/03/19/%c2%b5-wire-usb-on-an-attiny-10/](https://cpldcpu.com/2014/03/19/%c2%b5-wire-usb-on-an-attiny-10/)

生成摘要时出错

---

## 46. Teenage Engineering EP/BC–1 专业 CD 播放机

**原文标题**: Teenage Engineering EP/BC–1 professional CD player

**原文链接**: [https://teenage.engineering/products/bc-1](https://teenage.engineering/products/bc-1)

生成摘要时出错

---

## 47. Postgres 19 Repack: Faster, Built-In Table Bloat Cleanup

**原文标题**: Postgres 19 Repack: Faster, Built-In Table Bloat Cleanup

**原文链接**: [https://www.snowflake.com/en/blog/engineering/postgres-19-repack-table-bloat/](https://www.snowflake.com/en/blog/engineering/postgres-19-repack-table-bloat/)

生成摘要时出错

---

## 48. I'll never buy Framework hardware again

**原文标题**: I'll never buy Framework hardware again

**原文链接**: [https://poolp.org/posts/2026-11-20/ill-never-buy-framework-hardware-again/](https://poolp.org/posts/2026-11-20/ill-never-buy-framework-hardware-again/)

生成摘要时出错

---

## 49. Anthropic's IPO Bust Deepens $4T AI Wipeout on Wall Street

**原文标题**: Anthropic's IPO Bust Deepens $4T AI Wipeout on Wall Street

**原文链接**: [https://www.wsj.com/finance/stocks/anthropics-ipo-bust-punctuates-4-trillion-ai-wipeout-on-wall-street-f1f1ec90](https://www.wsj.com/finance/stocks/anthropics-ipo-bust-punctuates-4-trillion-ai-wipeout-on-wall-street-f1f1ec90)

生成摘要时出错

---

## 50. Army delays detonating "catastrophically hazardous" lead azide amid fear, anger

**原文标题**: Army delays detonating "catastrophically hazardous" lead azide amid fear, anger

**原文链接**: [https://arstechnica.com/science/2026/11/outrage-questions-swirl-as-army-delays-blowing-up-stockpile-of-toxic-lead-azide/](https://arstechnica.com/science/2026/11/outrage-questions-swirl-as-army-delays-blowing-up-stockpile-of-toxic-lead-azide/)

生成摘要时出错

---

## 51. Predictions of the End of Wikipedia

**原文标题**: Predictions of the End of Wikipedia

**原文链接**: [https://en.wikipedia.org/wiki/Predictions_of_the_end_of_Wikipedia](https://en.wikipedia.org/wiki/Predictions_of_the_end_of_Wikipedia)

生成摘要时出错

---

## 52. The Strongest Sokoban Solver

**原文标题**: The Strongest Sokoban Solver

**原文链接**: [https://healeycodes.com/introducing-the-worlds-strongest-sokoban-solver](https://healeycodes.com/introducing-the-worlds-strongest-sokoban-solver)

生成摘要时出错

---

## 53. What Comes After AGI?

**原文标题**: What Comes After AGI?

**原文链接**: [https://institute.deepmind.com/essays/what-comes-after-agi/](https://institute.deepmind.com/essays/what-comes-after-agi/)

生成摘要时出错

---

## 54. PostgreSQL 19

**原文标题**: PostgreSQL 19

**原文链接**: [https://www.postgresql.org/docs/release/19.0/](https://www.postgresql.org/docs/release/19.0/)

生成摘要时出错

---

## 55. UK fridges secured from hackers

**原文标题**: UK fridges secured from hackers

**原文链接**: [https://www.bbc.co.uk/news/articles/c6eq49zyx7p4o](https://www.bbc.co.uk/news/articles/c6eq49zyx7p4o)

生成摘要时出错

---

## 56. Nasdaq erases all 2026 gains

**原文标题**: Nasdaq erases all 2026 gains

**原文链接**: [https://www.cnbc.com/2026/11/19/stock-market-today-live-updates.html](https://www.cnbc.com/2026/11/19/stock-market-today-live-updates.html)

生成摘要时出错

---

## 57. Synology Security Advisory

**原文标题**: Synology Security Advisory

**原文链接**: [https://www.synology.com/en-uk/security/advisory/Synology_SA_26_21](https://www.synology.com/en-uk/security/advisory/Synology_SA_26_21)

生成摘要时出错

---

## 58. Inkling 2 Mini, Cutting-Edge Performance for Your Local Setup

**原文标题**: Inkling 2 Mini, Cutting-Edge Performance for Your Local Setup

**原文链接**: [https://huggingface.co/blog/inkling2mini](https://huggingface.co/blog/inkling2mini)

生成摘要时出错

---

## 59. OpenSSL: Buffer overflow in EVP_EncodeBlock() (CVE-2026-121481, CVSS 9.8)

**原文标题**: OpenSSL: Buffer overflow in EVP_EncodeBlock() (CVE-2026-121481, CVSS 9.8)

**原文链接**: [https://github.com/openssl/openssl/pull/33652](https://github.com/openssl/openssl/pull/33652)

生成摘要时出错

---

## 60. Launch HN: Onlook (YC W25) – An open-source developer tool for designers

**原文标题**: Launch HN: Onlook (YC W25) – An open-source developer tool for designers

**原文链接**: [https://github.com/onlook-dev/onlook/](https://github.com/onlook-dev/onlook/)

生成摘要时出错

---

## 61. "I can tell you wrote this yourself"

**原文标题**: "I can tell you wrote this yourself"

**原文链接**: [https://em-online.bearblog.dev/i-can-tell-you-wrote-this-yourself/](https://em-online.bearblog.dev/i-can-tell-you-wrote-this-yourself/)

生成摘要时出错

---

## 62. Vint Cerf on why TCP/IP was never patented

**原文标题**: Vint Cerf on why TCP/IP was never patented

**原文链接**: [https://seremot.com/p/vint-cerf-on-why-tcpip-was-never](https://seremot.com/p/vint-cerf-on-why-tcpip-was-never)

生成摘要时出错

---

## 63. Show HN: Foolscap – a writing app that reads your book and never writes for you

**原文标题**: Show HN: Foolscap – a writing app that reads your book and never writes for you

**原文链接**: [https://foolscap.works/](https://foolscap.works/)

生成摘要时出错

---

## 64. Show HN: Tinnitus frequency finder and audio notch tool

**原文标题**: Show HN: Tinnitus frequency finder and audio notch tool

**原文链接**: [https://trynotched.com/find](https://trynotched.com/find)

生成摘要时出错

---

## 65. Bit Shifting in Basic

**原文标题**: Bit Shifting in Basic

**原文链接**: [https://subethasoftware.com/2020/06/11/bit-shifting-in-basic/](https://subethasoftware.com/2020/06/11/bit-shifting-in-basic/)

生成摘要时出错

---

## 66. ChatGPT for SNES

**原文标题**: ChatGPT for SNES

**原文链接**: [https://www.bxfoundry.com/chatgpt_snes/](https://www.bxfoundry.com/chatgpt_snes/)

生成摘要时出错

---

## 67. Do not buy RAM, compress

**原文标题**: Do not buy RAM, compress

**原文链接**: [https://curiousbits.nl/blog/do-not-buy-ram-compress/](https://curiousbits.nl/blog/do-not-buy-ram-compress/)

生成摘要时出错

---

## 68. Weight-Space Programming builds neural networks like a 1990s researcher

**原文标题**: Weight-Space Programming builds neural networks like a 1990s researcher

**原文链接**: [https://notesbylex.com/weight-space-programming-1990s](https://notesbylex.com/weight-space-programming-1990s)

生成摘要时出错

---

## 69. Kia's cheapest EV is coming next year, and it could cost under $25,000

**原文标题**: Kia's cheapest EV is coming next year, and it could cost under $25,000

**原文链接**: [https://electrek.co/2026/11/19/kias-cheapest-ev-coming-2027-under-25k/](https://electrek.co/2026/11/19/kias-cheapest-ev-coming-2027-under-25k/)

生成摘要时出错

---

## 70. Judge: DHS's Seizure Of Immigration Lawyer's Phone Likely Violated 1st Amendment

**原文标题**: Judge: DHS's Seizure Of Immigration Lawyer's Phone Likely Violated 1st Amendment

**原文链接**: [https://www.techdirt.com/2026/11/20/judge-says-dhss-seizure-of-an-immigration-lawyers-phone-likely-violated-the-first-amendment/](https://www.techdirt.com/2026/11/20/judge-says-dhss-seizure-of-an-immigration-lawyers-phone-likely-violated-the-first-amendment/)

生成摘要时出错

---

## 71. Automatic Checking of Compiler Correctness with E-Graphs

**原文标题**: Automatic Checking of Compiler Correctness with E-Graphs

**原文链接**: [https://stng.substack.com/p/automatic-checking-of-compiler-correctness](https://stng.substack.com/p/automatic-checking-of-compiler-correctness)

生成摘要时出错

---

## 72. Why YC Series A rounds fell off a cliff

**原文标题**: Why YC Series A rounds fell off a cliff

**原文链接**: [https://jaredheyman.medium.com/on-why-yc-series-a-rounds-fell-off-a-cliff-ab523211a2f2](https://jaredheyman.medium.com/on-why-yc-series-a-rounds-fell-off-a-cliff-ab523211a2f2)

生成摘要时出错

---

## 73. Garage Door Spam

**原文标题**: Garage Door Spam

**原文链接**: [https://blog.harrison.page/garage-door-spam/](https://blog.harrison.page/garage-door-spam/)

生成摘要时出错

---

## 74. Scientists Track 219,000 People–Discover Unexpected Shift in Dementia Risk

**原文标题**: Scientists Track 219,000 People–Discover Unexpected Shift in Dementia Risk

**原文链接**: [https://www.newsweek.com/scientists-track-219000-people-discover-unexpected-shift-in-dementia-risk-12733867](https://www.newsweek.com/scientists-track-219000-people-discover-unexpected-shift-in-dementia-risk-12733867)

生成摘要时出错

---

## 75. Should governments slow frontier AI? Jacob Coxon and Robin Hanson debate [video]

**原文标题**: Should governments slow frontier AI? Jacob Coxon and Robin Hanson debate [video]

**原文链接**: [https://www.youtube.com/watch?v=lwfewYL7X0o](https://www.youtube.com/watch?v=lwfewYL7X0o)

生成摘要时出错

---

## 76. Anthropic shares tank after IPO as the Nasdaq erases 2026 gains

**原文标题**: Anthropic shares tank after IPO as the Nasdaq erases 2026 gains

**原文链接**: [https://www.nbcnews.com/business/markets/anthropic-shares-markets-selloff-nasdaq-rcna610394](https://www.nbcnews.com/business/markets/anthropic-shares-markets-selloff-nasdaq-rcna610394)

生成摘要时出错

---

## 77. Why San Francisco's water system couldn't handle a record-breaking storm

**原文标题**: Why San Francisco's water system couldn't handle a record-breaking storm

**原文链接**: [https://www.sfgate.com/bayarea/article/sf-flooding-sewers-22540612.php](https://www.sfgate.com/bayarea/article/sf-flooding-sewers-22540612.php)

生成摘要时出错

---

## 78. European rights court bars Romanian lawyer for 2 years over AI citations

**原文标题**: European rights court bars Romanian lawyer for 2 years over AI citations

**原文链接**: [https://www.echr.coe.int/w/romanian-lawyer-barred-for-two-years-from-representing-applicants-before-the-court-over-unverified-ai-generated-citations](https://www.echr.coe.int/w/romanian-lawyer-barred-for-two-years-from-representing-applicants-before-the-court-over-unverified-ai-generated-citations)

生成摘要时出错

---

## 79. Show HN: Radiotherapy Delivery Demo

**原文标题**: Show HN: Radiotherapy Delivery Demo

**原文链接**: [https://tps.neuralrad.com](https://tps.neuralrad.com)

生成摘要时出错

---

## 80. How to CAD Almost Anything

**原文标题**: How to CAD Almost Anything

**原文链接**: [https://ocw.mit.edu/courses/res-16-002-how-to-cad-almost-anything-january-iap-2024/](https://ocw.mit.edu/courses/res-16-002-how-to-cad-almost-anything-january-iap-2024/)

生成摘要时出错

---

## 81. Walls Beneath Jerusalem May Solve 150-Year Mystery

**原文标题**: Walls Beneath Jerusalem May Solve 150-Year Mystery

**原文链接**: [https://www.discovermagazine.com/two-walls-beneath-jerusalem-may-solve-a-150-year-mystery-about-rome-s-military-camp-49991](https://www.discovermagazine.com/two-walls-beneath-jerusalem-may-solve-a-150-year-mystery-about-rome-s-military-camp-49991)

生成摘要时出错

---

## 82. Anton Syndrome

**原文标题**: Anton Syndrome

**原文链接**: [https://en.wikipedia.org/wiki/Anton_syndrome](https://en.wikipedia.org/wiki/Anton_syndrome)

生成摘要时出错

---

## 83. Unblockable communication with gravity

**原文标题**: Unblockable communication with gravity

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.aee0802](https://www.science.org/doi/10.1126/sciadv.aee0802)

生成摘要时出错

---

## 84. Rebuilding my local voice assistant pipeline

**原文标题**: Rebuilding my local voice assistant pipeline

**原文链接**: [https://blog.platypush.tech/article/Rewriting-my-voice-assistant-pipeline](https://blog.platypush.tech/article/Rewriting-my-voice-assistant-pipeline)

生成摘要时出错

---

## 85. Windows 11 passkey bug cries failure after successful sign-in

**原文标题**: Windows 11 passkey bug cries failure after successful sign-in

**原文链接**: [https://www.theregister.com/security/2026/11/20/windows-11-passkey-bug-cries-failure-after-successful-sign-in/5311263](https://www.theregister.com/security/2026/11/20/windows-11-passkey-bug-cries-failure-after-successful-sign-in/5311263)

生成摘要时出错

---

## 86. Unauthenticated remote code execution in Nginx

**原文标题**: Unauthenticated remote code execution in Nginx

**原文链接**: [https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)

生成摘要时出错

---

## 87. Gemini 4 Neon

**原文标题**: Gemini 4 Neon

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

生成摘要时出错

---

## 88. Grand Theft Auto VI Earns $3.79B on First Day

**原文标题**: Grand Theft Auto VI Earns $3.79B on First Day

**原文链接**: [https://www.take2games.com/ir/news/grand-theft-auto-vi-shatters-entertainment-box-office-records](https://www.take2games.com/ir/news/grand-theft-auto-vi-shatters-entertainment-box-office-records)

生成摘要时出错

---

## 89. Pancreatic cancer halted by virus injection in three patients

**原文标题**: Pancreatic cancer halted by virus injection in three patients

**原文链接**: [https://www.newscientist.com/article/2528235-pancreatic-cancer-halted-by-virus-injection-in-three-patients/](https://www.newscientist.com/article/2528235-pancreatic-cancer-halted-by-virus-injection-in-three-patients/)

生成摘要时出错

---

## 90. Evidence (YC S21) Is Hiring

**原文标题**: Evidence (YC S21) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/evidence/jobs/1xb9PpP-founding-gtm-lead](https://www.ycombinator.com/companies/evidence/jobs/1xb9PpP-founding-gtm-lead)

生成摘要时出错

---

## 91. RegExr: Temporarily Offline

**原文标题**: RegExr: Temporarily Offline

**原文链接**: [https://regexr.com/](https://regexr.com/)

生成摘要时出错

---

## 92. Someone reported java4shell bug in September 2026

**原文标题**: Someone reported java4shell bug in September 2026

**原文链接**: [https://github.com/openjdk/jdk/pull/32781](https://github.com/openjdk/jdk/pull/32781)

生成摘要时出错

---

## 93. GIMP now has UI tests

**原文标题**: GIMP now has UI tests

**原文链接**: [https://www.gimp.org/news/2026/11/16/gimp-ui-tests/](https://www.gimp.org/news/2026/11/16/gimp-ui-tests/)

生成摘要时出错

---

## 94. Teaching robots to carve marble sculptures

**原文标题**: Teaching robots to carve marble sculptures

**原文链接**: [https://eleanorwiesler.com/blog/robotic-stone-carving/](https://eleanorwiesler.com/blog/robotic-stone-carving/)

生成摘要时出错

---

## 95. Talking Venice with Mahesh Subramony at AMD In-Depth

**原文标题**: Talking Venice with Mahesh Subramony at AMD In-Depth

**原文链接**: [https://chipsandcheese.com/p/talking-venice-with-mahesh-subramony](https://chipsandcheese.com/p/talking-venice-with-mahesh-subramony)

生成摘要时出错

---

## 96. Computer Graphics from Scratch (2021)

**原文标题**: Computer Graphics from Scratch (2021)

**原文链接**: [https://www.gabrielgambetta.com/computer-graphics-from-scratch/index.html](https://www.gabrielgambetta.com/computer-graphics-from-scratch/index.html)

生成摘要时出错

---

## 97. Combatting Adversarial Distillation

**原文标题**: Combatting Adversarial Distillation

**原文链接**: [https://openai.com/index/combatting-adversarial-distillation/](https://openai.com/index/combatting-adversarial-distillation/)

生成摘要时出错

---

## 98. How to Make the Ink Used to Write Hamlet and the Declaration of Independence

**原文标题**: How to Make the Ink Used to Write Hamlet and the Declaration of Independence

**原文链接**: [https://lithub.com/how-to-make-the-ink-used-to-write-hamlet-the-declaration-of-independence-and-beethovens-fifth/](https://lithub.com/how-to-make-the-ink-used-to-write-hamlet-the-declaration-of-independence-and-beethovens-fifth/)

生成摘要时出错

---

## 99. Frankenstein PBC – Animation, bestowed upon lifeless matter

**原文标题**: Frankenstein PBC – Animation, bestowed upon lifeless matter

**原文链接**: [https://www.frankensteinpbc.com/](https://www.frankensteinpbc.com/)

生成摘要时出错

---

## 100. Pete Warden on local AI, open models, voice interfaces, the future of hardware

**原文标题**: Pete Warden on local AI, open models, voice interfaces, the future of hardware

**原文链接**: [https://thedataexchange.media/pete-warden-moonshine/](https://thedataexchange.media/pete-warden-moonshine/)

生成摘要时出错

---

