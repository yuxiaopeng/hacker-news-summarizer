# Hacker News 热门文章摘要 (2026-11-11)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. AWS 模拟器

**原文标题**: AWS emulator

**原文链接**: [https://github.com/aws/aws-emulator](https://github.com/aws/aws-emulator)

**AWS Emulator** 是一款免费的本地工具，旨在无需 AWS 账号或互联网连接的情况下，针对 AWS API 进行软件测试。它允许开发人员在开发环境或 CI 管道中使用模拟资源，从而避免产生 AWS 服务费用。

**主要运行模式：**
*   **服务器模式：** 模拟器作为本地进程（Linux）或在 Docker 容器（Windows/macOS）中运行。用户通过环境变量将 AWS CLI 或 SDK 指向其端点。
*   **嵌入模式：** 专为 Rust 开发人员设计，模拟器可作为 `dev-dependency` 在进程内运行，无需环境配置即可为每个测试提供独立实例。
*   **AI 智能体：** 用户可将模拟器集成为 AI 编程智能体的一项技能。

**技术要求与性能：**
该模拟器基于 Rust 构建，采用高度模块化的设计，每个 AWS 服务对应一个 crate。因此，从源码构建非常耗费资源，需要多核机器以及至少 100 GB 的磁盘空间作为构建目录。建议大多数用户使用预构建包或 Docker 镜像。

**局限性与保真度：**
该模拟器严格仅用于构建和测试，不适用于生产负载或安全性测试。由于其属于模拟性质，用户应参考“保真度评分”和仓库的 issues 目录，以识别模拟器与实际 AWS 服务之间的功能差距。

**隐私与贡献：**
系统默认开启了匿名遥测以帮助改进工具，但可以通过命令行选项、环境变量或配置文件将其禁用。虽然用户可以通过 GitHub 报告错误和保真度差距，但该项目不接受拉取请求。大部分软件采用 CC0 1.0 通用协议授权。

---

## 2. 蒂姆·彼得斯逝世

**原文标题**: Tim Peters has died

**原文链接**: [https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028](https://discuss.python.org/t/in-memoriam-tim-peters-1952-2026/110028)

Python 创始人 Guido van Rossum 宣布了 Tim Peters 逝世的消息，他于 7 月 15 日去世。Peters 是 Python 社区的奠基性人物，自该语言早期以来一直是其设计的密切合作者。

Peters 最广为人知的贡献是撰写了 **“Python 之禅” (PEP 20)**，这被视为该语言的指导哲学。然而，他的技术贡献远不止于此。他曾促使 van Rossum 支持整数与浮点数之间的混合运算，并于 2002 年发明了 **Timsort** 排序算法——这种高效的算法后来被 Java 和 Android 采用。

除了技术成就，Peters 还是多产的导师，也是 Python 邮件列表的核心人物。他被称为 **“Timbot”**，因其对用户问题耐心、详尽且幽默的回复而深受爱戴。Van Rossum 称赞 Peters 凭借深厚的数学和编译器知识，为早期核心开发奠定了基调，并指出如果没有 Peters 的影响和指导，Python 就不会有今天的成就。

---

## 3. 美联航禁止 AI 代理代表旅客预订航班

**原文标题**: United Airlines bans AI agents from booking flights on behalf of travelers

**原文链接**: [https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/](https://www.cbsnews.com/news/united-airlines-bans-ai-agents-booking-flights/)

美联航宣布禁止第三方人工智能代理代表旅客进行航班预订。该航空公司称，安全风险、潜在的监管违规以及商业考量是出台这一新政策的主要驱动因素。

美联航表示担心，与个人AI助手（如Meta的Muse或OpenAI的工具）共享账户凭据可能会泄露敏感的客户数据，并导致非本人意愿的购买或未经授权的账户变更。此外，该航空公司指出，使用AI处理值机等任务可能会违反联邦法规，因为相关法规要求旅客必须亲自核实其行李中不含违禁物品。

行业分析师认为，此项禁令也有助于美联航维持对客户预订流程的控制。通过限制AI机器人，该航空公司可以避免因海量自动化航班查询而产生的运营成本，并防止AI平台成为航空公司与客户之间强大的新中介。

这一举措使美联航与某些竞争对手区别开来；例如，西南航空已允许ChatGPT用户查看其航班库存。虽然美联航的票价信息仍可通过Google Flights、Kayak和Hopper等传统聚合平台获取，但旅客将无法再将最终的预订和出票流程委托给个人AI代理。

---

## 4. 93% 的油漆溅痕都是有效的 Perl 程序 (2019)

**原文标题**: 93% of Paint Splatters Are Valid Perl Programs (2019)

**原文链接**: [https://www.mcmillen.dev/sigbovik/](https://www.mcmillen.dev/sigbovik/)

Colin McMillen 在其文章《93% 的油漆溅痕都是有效的 Perl 程序》中，通过一个幽默的计算实验，探讨了 Perl 编程语言极高的灵活性和宽松的语法。

**实验过程**
McMillen 进行了一项测试，以观察 Perl 解释器如何处理随机噪声。他生成了随机字符串——旨在模拟“油漆溅痕”或“线路噪声”——并使用 Perl 语法检查器（`perl -c`）对其进行运行。

**主要发现**
研究发现，这些随机生成的字符串中约有 93% 被判定为语法有效的 Perl 代码。虽然这些“程序”极少能实现有用功能，且在实际执行时可能会触发警告或导致崩溃，但它们成功通过了初始编译阶段。

**为什么 Perl 如此宽松**
这种极高的“有效率”归功于 Perl 设计中的几个独特特性：
*   **裸字 (Barewords)：** Perl 经常将未加引号的字符串解释为常量或函数调用。
*   **灵活的运算符：** 该语言拥有大量的特殊变量和基于标点符号的运算符，使得许多字符组合都能被解释为有效的表达式。
*   **TMTOWTDI 哲学：** Perl 秉持“解决问题的方法不止一种” (There’s More Than One Way To Do It) 的准则，这造就了一个极其包容的解析器，旨在尽可能为代码寻找合理的解释。

**结论**
这篇文章幽默地佐证了业界流传已久的笑话：Perl 代码与随机线路噪声无异。最终，McMillen 的实验证明了该语言独特且高度复杂的语法，以及其历史上对程序员灵活性优于僵硬语法规则的坚持。

---

## 5. 一次烟雾报警器误报险些淹没 Jane Street 唯一的纽约数据中心

**原文标题**: A false smoke alarm almost drowned Jane Street's only NYC datacenter

**原文链接**: [https://michael.bacarella.com/2026/11/10/false-smoke-alarm-jane-street-datacenter/](https://michael.bacarella.com/2026/11/10/false-smoke-alarm-jane-street-datacenter/)

本文讲述了 Jane Street 系统团队的一段“实战往事”，详细记录了该公司以前在纽约市数据中心发生的一次近乎灾难性的事件。从历史上看，Jane Street 将服务器保留在办公现场，是为了确保交易员在系统失灵时能手动“拔掉插头”——这种风险管理哲学深受一位合伙人在核潜艇服役经历的影响。

危机始于施工粉尘引发的火灾误报。虽然其“预作用”喷淋系统需要感应到热量才会喷水，但警报自动关闭了机房空调（CRAC）单元，以防为潜在火情供氧。这形成了一个致命的反馈循环：服务器仍在运行，但在失去冷却的情况下，环境温度迅速攀升，逼近 150°F 的阈值——一旦达到该温度，喷淋装置就会启动并彻底淹没硬件。

在收到香港办公室的提醒后，住在仅几分钟路程外的作者冲到大楼，在已经变成“桑拿房”的机房内手动拔掉了成排服务器机柜的电源。当时室内温度最高达到了 143.6°F，距离触发点仅一步之遥，惊险地避免了硬件全毁和公司倒闭的危机。

事件发生后，Jane Street 进行了冷静的事后剖析。虽然他们选择继续保留现场数据中心，但作者使用 OCaml 开发了一套更强大的监控系统。该工具旨在汇总整个 Linux 服务器集群的温度遥测数据，提供高可靠的保险机制，以便在冷却故障达到临界水平前及时察觉。这套系统取代了以往不太可靠的方法，确保公司今后不会再被类似的冷却失效问题所困扰。

---

## 6. Gemini 决策 API

**原文标题**: Gemini Decisions API

**原文链接**: [https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)

Google DeepMind 推出了由全新 Gemini Decision 1 模型驱动的 **Gemini Decisions API**。这一专业工具旨在针对文本、图像、音频、视频及 PDF（最高支持 256K token）等多种模态输入，进行快速、概率性的闭集决策。

与逐个生成 token 的传统生成模型不同，Gemini Decision 1 在一次前向传递中即可对候选选项进行评分。这种方法显著降低了端到端延迟（150–250 毫秒），并提供了极具竞争力的定价模式：每 100 万输入 token 仅需 **0.10 美元**，且不收取输出 token 费用。

**核心能力包括：**
*   **单次请求评估：** 用户可以在单次请求中，针对同一个多模态输入评估多达 1,000 个独立问题。
*   **决策类型：** 该 API 支持三种主要格式：**是/否** (`noul`)、**多项选择**（最多支持 255 个选项）以及**有序评分标准** (`score`)。
*   **校准置信度：** 每次响应都包含一个置信度分数（0 到 1），方便开发者将模棱两可的案例路由至人工审核或备用模型。
*   **原生多模态：** 它可以处理复杂的组合信息，例如将通话录音与账户元数据匹配，或将 PDF 扫描件与损毁照片结合处理。

谷歌已在 Gemini Notebook 的动态模型路由、谷歌搜索的安全性层以及 Stitch 的快速设计迭代中应用了该 API。Gemini Decisions API 目前已在 **Google AI Studio** 中上线，支持 Python、JavaScript 和 REST，并集成了 LangChain、Vercel、LiteLLM 和 Pydantic AI 等主流生态系统工具。

---

## 7. 锁定你的 GitHub Actions

**原文标题**: Lock Your GitHub Actions

**原文链接**: [https://hugovk.dev/blog/2026/lock-github-actions/](https://hugovk.dev/blog/2026/lock-github-actions/)

生成摘要时出错

---

## 8. Emacs in the Age of Magic

**原文标题**: Emacs in the Age of Magic

**原文链接**: [https://commandlinesystems.com/magic.txt](https://commandlinesystems.com/magic.txt)

"Emacs in the Age of Magic" explores the profound shift from traditional, rules-based programming to the era of stochastic AI. The author reflects on how AI tools, such as Claude Code, have disrupted the computer science landscape by solving complex research problems and automating tasks that were once the pride of elite "power users."

Historically, AI research relied on human-coded rules and recursive languages like LISP. However, the author argues that these methods couldn't capture the complexity of the real world. Modern LLMs have bypassed these limitations, rendering the manual "speed" and "efficiency" of Emacs users obsolete. Tasks that once required expertise, such as managing Git commits or customizing complex workflows, are now handled instantly by AI.

The article highlights two case studies—*excali-mode.el* and *cooked.el*—where AI allowed developers to perform "insane" feats of engineering, such as reimplementing entire web stacks or building terminal emulators from scratch over a weekend. In the "before times," these projects would be dismissed as wasteful; today, they are "throwaway hacks" that cost nothing but tokens.

Ultimately, the author predicts the "Emacsification of Software," a future where all applications are hyper-personalized by AI to fit individual whims. While this realizes Richard Stallman’s dream of total software freedom, it comes with a heavy irony: users can now build anything they can imagine, but they—and perhaps everyone else—no longer understand how any of it actually works. The age of rigid digital instruction has given way to a "magic" that trades comprehension for raw creative power.

---

## 9. Show HN: I recreated Papers Please but you're deciding which YC startups to fund

**原文标题**: Show HN: I recreated Papers Please but you're deciding which YC startups to fund

**原文链接**: [https://termsheetplease.com/](https://termsheetplease.com/)

The article introduces **"Term Sheet, Please,"** a web-based game created by Bo Lau and shared on Hacker News. The project is a thematic recreation of the indie hit *Papers, Please*, but it replaces the original's dystopian border control setting with the fast-paced world of venture capital.

In the game, players take on the role of an investor deciding which Y Combinator (YC) startups to fund. Set "one day after Demo Day," the gameplay mirrors the mechanics of the original title: players must call founders to their desk, inspect documents for discrepancies, and cross-reference facts. Using a familiar bureaucratic interface, the player must ultimately decide whether to **"FUND," "PASS,"** or **"HOLD"** a startup by placing a decision sheet on their desk.

The game features the iconic lo-fi aesthetic and high-pressure atmosphere of its inspiration, focusing on the meticulous review of term sheets and founder pitches. It serves as a creative parody of the Silicon Valley investment process, challenging players to make quick, high-stakes financial decisions.

---

## 10. Huawei releases MACaQ, its internal quantizer for local inference

**原文标题**: Huawei releases MACaQ, its internal quantizer for local inference

**原文链接**: [https://github.com/huawei-csl/MACaQ](https://github.com/huawei-csl/MACaQ)

生成摘要时出错

---

## 11. The Utah Teapot

**原文标题**: The Utah Teapot

**原文链接**: [https://graphics.cs.utah.edu/teapot/](https://graphics.cs.utah.edu/teapot/)

生成摘要时出错

---

## 12. Faster Retrieval for Better, More Efficient RAG

**原文标题**: Faster Retrieval for Better, More Efficient RAG

**原文链接**: [https://machinelearning.apple.com/research/faster-retrieval](https://machinelearning.apple.com/research/faster-retrieval)

生成摘要时出错

---

## 13. Flying on Green: Why Farmers Are Turning to Drones for Cover Crop Seeding

**原文标题**: Flying on Green: Why Farmers Are Turning to Drones for Cover Crop Seeding

**原文链接**: [https://www.agweb.com/news/machinery/flying-green-why-farmers-are-turning-drones-cover-crop-seeding](https://www.agweb.com/news/machinery/flying-green-why-farmers-are-turning-drones-cover-crop-seeding)

生成摘要时出错

---

## 14. My AI agents found an unmapped Maya site

**原文标题**: My AI agents found an unmapped Maya site

**原文链接**: [https://pietromiotti.com/latest/maya-site](https://pietromiotti.com/latest/maya-site)

In this article, the author describes how they used a team of AI agents to "rediscover" a Maya archaeological site in Mexico using NASA lidar data. Inspired by the history of Machu Picchu, the author—a self-described "naive outsider" to archaeology—tasked 48 agents (using models like Gemini and Claude) to scan 1,200 km² of jungle lidar imagery for man-made geometric structures.

Within 72 hours, the agents identified a Classic-period (AD 250–900) civic center featuring a pyramid, a leveled plaza, and a suspected water reservoir. The AI agents further assisted by drafting a formal report in Spanish and identifying the correct contact authorities at Mexico’s National Institute of Anthropology and History (INAH). While INAH initially confirmed the location was not in their official register, the author later discovered that professional archaeologists had recently mapped the site in a 2025 study.

Though the project resulted in a "rediscovery" rather than a new find, the author emphasizes three key takeaways:
1.  **Speed and Accessibility:** The process went from a random thought to an official government reply in three days.
2.  **Democratization of Science:** Agentic AI allows non-experts to apply "brute-force" compute to complex problems, achieving results comparable to professional researchers.
3.  **The Future of Research:** This methodology isn't limited to archaeology; it signals a revolution across all scientific fields where curiosity and imagination become the primary bottlenecks.

The author concludes that we are entering an era where AI agents can systematically analyze global data to uncover hidden history and scientific breakthroughs at an unprecedented scale.

---

## 15. 英伟达正准备罢免英伟达首席执行官黄仁勋

**原文标题**: Nvidia Is Preparing to Oust Nvidia CEO Jensen Huang

**原文链接**: [https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad](https://www.wsj.com/business/nvidia-is-preparing-to-oust-nvidia-ceo-jensen-huang-30f421ad)

Unable to access the article link.

---

## 16. 基于 WebGL2 的超逼真沙子

**原文标题**: Hyper-Realistic Sand with WebGL2

**原文链接**: [https://av.github.io/safe-sand/](https://av.github.io/safe-sand/)

生成摘要时出错

---

## 17. Show HN: Yogurt – Free, private, open-source alternative to Granola

**原文标题**: Show HN: Yogurt – Free, private, open-source alternative to Granola

**原文链接**: [https://github.com/FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt)

生成摘要时出错

---

## 18. The hardest notes to find on the guitar

**原文标题**: The hardest notes to find on the guitar

**原文链接**: [https://www.gitori.com/blog/articles/hardest-notes-on-the-guitar-fretboard](https://www.gitori.com/blog/articles/hardest-notes-on-the-guitar-fretboard)

生成摘要时出错

---

## 19. Optimizing Reference Deletions in Git

**原文标题**: Optimizing Reference Deletions in Git

**原文链接**: [https://nayak.im/posts/optimizing-reference-deletion/](https://nayak.im/posts/optimizing-reference-deletion/)

生成摘要时出错

---

## 20. IBM Quantum Nighthawk Demonstrates New Levels of Speed and Quality

**原文标题**: IBM Quantum Nighthawk Demonstrates New Levels of Speed and Quality

**原文链接**: [https://newsroom.ibm.com/2026-11-11-ibm-quantum-nighthawk-demonstrates-new-levels-of-speed-and-quality,-with-plans-to-scale-beyond-1,000-qubits-in-2027](https://newsroom.ibm.com/2026-11-11-ibm-quantum-nighthawk-demonstrates-new-levels-of-speed-and-quality,-with-plans-to-scale-beyond-1,000-qubits-in-2027)

生成摘要时出错

---

## 21. Atuin Threads: All your agent sessions on every machine

**原文标题**: Atuin Threads: All your agent sessions on every machine

**原文链接**: [https://blog.atuin.sh/threads-agent-sessions/](https://blog.atuin.sh/threads-agent-sessions/)

生成摘要时出错

---

## 22. The Apple Support Community will permanently close on November 20, 2026

**原文标题**: The Apple Support Community will permanently close on November 20, 2026

**原文链接**: [https://discussions.apple.com/welcome](https://discussions.apple.com/welcome)

生成摘要时出错

---

## 23. Can a Linear Program Do Weight-Space Programming?

**原文标题**: Can a Linear Program Do Weight-Space Programming?

**原文链接**: [https://nathan.rs/posts/weight-space-lp/](https://nathan.rs/posts/weight-space-lp/)

生成摘要时出错

---

## 24. Nvidia prepares to fire CEO Jensen Huang, WSJ reports

**原文标题**: Nvidia prepares to fire CEO Jensen Huang, WSJ reports

**原文链接**: [https://twitter.com/watcherguru/status/2120645607866188008](https://twitter.com/watcherguru/status/2120645607866188008)

生成摘要时出错

---

## 25. Using voltage glitching to unleash the A100 in my mining card

**原文标题**: Using voltage glitching to unleash the A100 in my mining card

**原文链接**: [https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/](https://blog.kate.land/posts/using-voltage-glitching-to-unlock-the-a100/)

生成摘要时出错

---

## 26. Tools for exploring the souls of large language models

**原文标题**: Tools for exploring the souls of large language models

**原文链接**: [https://oshea00.github.io/posts/tinygpt-visualizer/](https://oshea00.github.io/posts/tinygpt-visualizer/)

生成摘要时出错

---

## 27. We need more goat sacrifices

**原文标题**: We need more goat sacrifices

**原文链接**: [https://www.experimental-history.com/p/we-need-more-goat-sacrifices](https://www.experimental-history.com/p/we-need-more-goat-sacrifices)

生成摘要时出错

---

## 28. The tiny transmitter tracking monarch butterflies' migration, Canada to Mexico

**原文标题**: The tiny transmitter tracking monarch butterflies' migration, Canada to Mexico

**原文链接**: [https://www.begiant.ca/stories/places/monarch-butterflies-tracking-conservation](https://www.begiant.ca/stories/places/monarch-butterflies-tracking-conservation)

生成摘要时出错

---

## 29. GitHub Incident with Webhooks, Actions, etc.

**原文标题**: GitHub Incident with Webhooks, Actions, etc.

**原文链接**: [https://www.githubstatus.com/incidents/dvy0t3mvh1lg](https://www.githubstatus.com/incidents/dvy0t3mvh1lg)

生成摘要时出错

---

## 30. Pharo in the Browser with WebAssembly

**原文标题**: Pharo in the Browser with WebAssembly

**原文链接**: [https://massimo-nocentini.github.io/pharo-vm/world.html](https://massimo-nocentini.github.io/pharo-vm/world.html)

生成摘要时出错

---

## 31. Retirement Savings Are Fueling the AI Bubble

**原文标题**: Retirement Savings Are Fueling the AI Bubble

**原文链接**: [https://lpeproject.org/blog/your-retirement-savings-are-fueling-the-ai-bubble/](https://lpeproject.org/blog/your-retirement-savings-are-fueling-the-ai-bubble/)

生成摘要时出错

---

## 32. The Computer Graphics Book of Knowledge

**原文标题**: The Computer Graphics Book of Knowledge

**原文链接**: [https://www.cs.cmu.edu/~ph/nyit/masson/history.htm](https://www.cs.cmu.edu/~ph/nyit/masson/history.htm)

生成摘要时出错

---

## 33. Attention to Mamba: A Recipe for Cross-Architecture Distillation

**原文标题**: Attention to Mamba: A Recipe for Cross-Architecture Distillation

**原文链接**: [https://machinelearning.apple.com/research/attention-mamba-distillation](https://machinelearning.apple.com/research/attention-mamba-distillation)

生成摘要时出错

---

## 34. Show HN: Godbolt-in-a-floating-window for Neovim (C, C++, Rust)

**原文标题**: Show HN: Godbolt-in-a-floating-window for Neovim (C, C++, Rust)

**原文链接**: [https://github.com/0xdeadf1sh/AssemblyForNeovim](https://github.com/0xdeadf1sh/AssemblyForNeovim)

生成摘要时出错

---

## 35. Apple has new Mac app coming to make running local AI models easy

**原文标题**: Apple has new Mac app coming to make running local AI models easy

**原文链接**: [https://9to5mac.com/2026/11/10/apple-has-new-mac-app-coming-to-make-running-local-ai-models-easy/](https://9to5mac.com/2026/11/10/apple-has-new-mac-app-coming-to-make-running-local-ai-models-easy/)

生成摘要时出错

---

## 36. AI, activity, and outcomes in software engineering

**原文标题**: AI, activity, and outcomes in software engineering

**原文链接**: [https://cabird.com/talks/shipping-faster/](https://cabird.com/talks/shipping-faster/)

生成摘要时出错

---

## 37. Show HN: Micron – Oberon with the Power of C

**原文标题**: Show HN: Micron – Oberon with the Power of C

**原文链接**: [https://github.com/rochus-keller/Micron](https://github.com/rochus-keller/Micron)

生成摘要时出错

---

## 38. I asked every TV manufacturer 17 questions about how they spy on you

**原文标题**: I asked every TV manufacturer 17 questions about how they spy on you

**原文链接**: [https://www.theverge.com/tech/1012372/tv-privacy-acr-questions](https://www.theverge.com/tech/1012372/tv-privacy-acr-questions)

生成摘要时出错

---

## 39. TimeNet: Open-source data infrastructure for Temporal Foundation Models

**原文标题**: TimeNet: Open-source data infrastructure for Temporal Foundation Models

**原文链接**: [https://github.com/OpenTSLM/TimeNet](https://github.com/OpenTSLM/TimeNet)

生成摘要时出错

---

## 40. Show HN: Klad, a paint app your coding agent can drive (source-available)

**原文标题**: Show HN: Klad, a paint app your coding agent can drive (source-available)

**原文链接**: [https://github.com/klad-app/klad](https://github.com/klad-app/klad)

生成摘要时出错

---

## 41. Jensen Huang had a second affair – with an employee

**原文标题**: Jensen Huang had a second affair – with an employee

**原文链接**: [https://www.cnbc.com/2026/11/11/nvidia-jensen-huang-affair-employee.html](https://www.cnbc.com/2026/11/11/nvidia-jensen-huang-affair-employee.html)

生成摘要时出错

---

## 42. Peer-to-peer WebRTC connections with built-in signaling and discovery

**原文标题**: Peer-to-peer WebRTC connections with built-in signaling and discovery

**原文链接**: [https://github.com/lukks/like-webrtc](https://github.com/lukks/like-webrtc)

生成摘要时出错

---

## 43. EventSourcingDB 1.3.0 Is Available

**原文标题**: EventSourcingDB 1.3.0 Is Available

**原文链接**: [https://www.eventfoundation.io/resources/blog/eventsourcingdb-1-3-0-is-available](https://www.eventfoundation.io/resources/blog/eventsourcingdb-1-3-0-is-available)

生成摘要时出错

---

## 44. A C++ Quicksort Faster Than std:sort

**原文标题**: A C++ Quicksort Faster Than std:sort

**原文链接**: [https://tiki.li/blog/about_blqsort](https://tiki.li/blog/about_blqsort)

生成摘要时出错

---

## 45. Cancer vaccine for Yash, he's diagnosed with stage IV pancreatic cancer

**原文标题**: Cancer vaccine for Yash, he's diagnosed with stage IV pancreatic cancer

**原文链接**: [https://github.com/popvax/yash](https://github.com/popvax/yash)

生成摘要时出错

---

## 46. The Power and Legacy of Virginia Tech's Mac-Based Supercomputers

**原文标题**: The Power and Legacy of Virginia Tech's Mac-Based Supercomputers

**原文链接**: [https://512pixels.net/2026/11/va-tech-system-x-system-g/](https://512pixels.net/2026/11/va-tech-system-x-system-g/)

生成摘要时出错

---

## 47. Multiple remote code execution vulnerabilities in danfoss sm-800A

**原文标题**: Multiple remote code execution vulnerabilities in danfoss sm-800A

**原文链接**: [https://www.midnightblue.nl/blog/multiple-rce-danfoss-aksm800a](https://www.midnightblue.nl/blog/multiple-rce-danfoss-aksm800a)

生成摘要时出错

---

## 48. Next-Level Benchmarking Overfitting – Thomas Neumann

**原文标题**: Next-Level Benchmarking Overfitting – Thomas Neumann

**原文链接**: [http://databasearchitects.blogspot.com/2026/11/next-level-benchmarking-overfitting.html](http://databasearchitects.blogspot.com/2026/11/next-level-benchmarking-overfitting.html)

生成摘要时出错

---

## 49. Brazil's Serra Verde starts shipping heavy rare earths to US under 15-year deal

**原文标题**: Brazil's Serra Verde starts shipping heavy rare earths to US under 15-year deal

**原文链接**: [https://investors.usare.com/news-releases/news-release-details/usa-rare-earth-announces-start-commercial-scale-shipments-and](https://investors.usare.com/news-releases/news-release-details/usa-rare-earth-announces-start-commercial-scale-shipments-and)

生成摘要时出错

---

## 50. Hooked on Tuna

**原文标题**: Hooked on Tuna

**原文链接**: [https://theconversation.com/hooked-on-tuna-people-have-been-harvesting-these-ocean-predators-for-44-000-years-292428](https://theconversation.com/hooked-on-tuna-people-have-been-harvesting-these-ocean-predators-for-44-000-years-292428)

生成摘要时出错

---

## 51. Play GTA5 on Browser

**原文标题**: Play GTA5 on Browser

**原文链接**: [https://playgta5.com/](https://playgta5.com/)

生成摘要时出错

---

## 52. A great old-timey game-programming hack (2013)

**原文标题**: A great old-timey game-programming hack (2013)

**原文链接**: [https://blog.moertel.com/posts/2013-12-14-great-old-timey-game-programming-hack.html](https://blog.moertel.com/posts/2013-12-14-great-old-timey-game-programming-hack.html)

生成摘要时出错

---

## 53. Show HN: Black Ops II statically recompiled to native ARM64 macOS

**原文标题**: Show HN: Black Ops II statically recompiled to native ARM64 macOS

**原文链接**: [https://github.com/adrbn/bo2-mac](https://github.com/adrbn/bo2-mac)

生成摘要时出错

---

## 54. If I were diagnosed with cancer today, here's what I'd do

**原文标题**: If I were diagnosed with cancer today, here's what I'd do

**原文链接**: [https://killingdave.substack.com/p/if-i-were-diagnosed-with-cancer-today](https://killingdave.substack.com/p/if-i-were-diagnosed-with-cancer-today)

生成摘要时出错

---

## 55. "Zlibrary my beloved": Anthropic staff chats extolling piracy cited in Sony suit

**原文标题**: "Zlibrary my beloved": Anthropic staff chats extolling piracy cited in Sony suit

**原文链接**: [https://arstechnica.com/tech-policy/2026/08/zlibrary-my-beloved-anthropic-staff-chats-extolling-piracy-cited-in-sony-suit/](https://arstechnica.com/tech-policy/2026/08/zlibrary-my-beloved-anthropic-staff-chats-extolling-piracy-cited-in-sony-suit/)

生成摘要时出错

---

## 56. Why I wrote the BEAM book (2025)

**原文标题**: Why I wrote the BEAM book (2025)

**原文链接**: [https://happihacking.com/blog/posts/2025/why_I_wrote_theBEAMBook/](https://happihacking.com/blog/posts/2025/why_I_wrote_theBEAMBook/)

生成摘要时出错

---

## 57. Smart home devices should work without the internet

**原文标题**: Smart home devices should work without the internet

**原文链接**: [https://docodethatmatters.com/home-automation-overnight-success/](https://docodethatmatters.com/home-automation-overnight-success/)

生成摘要时出错

---

## 58. Greg Kurtzer's Ginux is now a userspace kernel

**原文标题**: Greg Kurtzer's Ginux is now a userspace kernel

**原文链接**: [https://github.com/gmkurtzer/ginux](https://github.com/gmkurtzer/ginux)

生成摘要时出错

---

## 59. Reddit Migration's Impact on Lemmy (2023)

**原文标题**: Reddit Migration's Impact on Lemmy (2023)

**原文链接**: [https://www.jmis.org/archive/view_article?pid=jmis-10-4-333](https://www.jmis.org/archive/view_article?pid=jmis-10-4-333)

生成摘要时出错

---

## 60. Physically Controllable Relighting of Photographs

**原文标题**: Physically Controllable Relighting of Photographs

**原文链接**: [https://yaksoy.github.io/PhysicalRelighting/](https://yaksoy.github.io/PhysicalRelighting/)

生成摘要时出错

---

## 61. Hayabusa2 Is Chasing the mysterious object 1998 KY26

**原文标题**: Hayabusa2 Is Chasing the mysterious object 1998 KY26

**原文链接**: [https://gizmodo.com/a-japanese-spacecraft-is-chasing-a-space-rock-that-defies-gravity-the-best-explanation-just-took-a-hit-2000837742](https://gizmodo.com/a-japanese-spacecraft-is-chasing-a-space-rock-that-defies-gravity-the-best-explanation-just-took-a-hit-2000837742)

生成摘要时出错

---

## 62. Protecting SSH Keys with macOS Secure Enclave

**原文标题**: Protecting SSH Keys with macOS Secure Enclave

**原文链接**: [https://gatezh.com/posts/macos-secure-enclave-ssh-keys/](https://gatezh.com/posts/macos-secure-enclave-ssh-keys/)

生成摘要时出错

---

## 63. Show HN: 3D to 2D, point clouds flattening (geometry images)

**原文标题**: Show HN: 3D to 2D, point clouds flattening (geometry images)

**原文链接**: [https://github.com/Neighborhood-Grid/flatpoints](https://github.com/Neighborhood-Grid/flatpoints)

生成摘要时出错

---

## 64. Claude Whiteboards, Claude Sheets, and Claude Data

**原文标题**: Claude Whiteboards, Claude Sheets, and Claude Data

**原文链接**: [https://claude.com/resources/articles/sheets-whiteboards-data](https://claude.com/resources/articles/sheets-whiteboards-data)

生成摘要时出错

---

## 65. .name Grandfathered

**原文标题**: .name Grandfathered

**原文链接**: [https://neil.fraser.name/news/2026/11/10/](https://neil.fraser.name/news/2026/11/10/)

生成摘要时出错

---

## 66. Open research, stronger privacy: Making Firefox users harder to fingerprint

**原文标题**: Open research, stronger privacy: Making Firefox users harder to fingerprint

**原文链接**: [https://blog.mozilla.org/security/2026/11/10/open-research-stronger-privacy-making-firefox-users-harder-to-fingerprint/](https://blog.mozilla.org/security/2026/11/10/open-research-stronger-privacy-making-firefox-users-harder-to-fingerprint/)

生成摘要时出错

---

## 67. Why Amstrad chose the 3" drives

**原文标题**: Why Amstrad chose the 3" drives

**原文链接**: [https://www.cpcwiki.eu/forum/amstrad-cpc-hardware/why-amstrad-chose-the-3-drives/](https://www.cpcwiki.eu/forum/amstrad-cpc-hardware/why-amstrad-chose-the-3-drives/)

生成摘要时出错

---

## 68. Jensen Huang Said to Have Had Relationship with Nvidia Executive

**原文标题**: Jensen Huang Said to Have Had Relationship with Nvidia Executive

**原文链接**: [https://www.nytimes.com/2026/11/11/technology/jensen-huang-nvidia-affair.html](https://www.nytimes.com/2026/11/11/technology/jensen-huang-nvidia-affair.html)

生成摘要时出错

---

## 69. Foldable Flight: The Best Paper Airplanes

**原文标题**: Foldable Flight: The Best Paper Airplanes

**原文链接**: [https://www.foldableflight.com](https://www.foldableflight.com)

生成摘要时出错

---

## 70. Laser-armed AI submarine robots patrol Norwegian salmon farms, killing sea lice

**原文标题**: Laser-armed AI submarine robots patrol Norwegian salmon farms, killing sea lice

**原文链接**: [https://www.tomshardware.com/tech-industry/drones/3-500-ai-laser-robots-patrol-norwegian-salmon-farms-killing-sea-lice-parasites-get-zapped-by-high-tech-alternative-to-harsh-chemical-baths](https://www.tomshardware.com/tech-industry/drones/3-500-ai-laser-robots-patrol-norwegian-salmon-farms-killing-sea-lice-parasites-get-zapped-by-high-tech-alternative-to-harsh-chemical-baths)

生成摘要时出错

---

## 71. A Brain Teaser of an Obituary

**原文标题**: A Brain Teaser of an Obituary

**原文链接**: [https://www.nytimes.com/2026/11/10/obituaries/steve-selvin-dead.html](https://www.nytimes.com/2026/11/10/obituaries/steve-selvin-dead.html)

生成摘要时出错

---

## 72. Tracking Anthropic-discovered vulnerabilities

**原文标题**: Tracking Anthropic-discovered vulnerabilities

**原文链接**: [https://www.vulncheck.com/blog/anthropic-glasswing-november-update](https://www.vulncheck.com/blog/anthropic-glasswing-november-update)

生成摘要时出错

---

## 73. Scion is back and is going to sell a kei truck in America

**原文标题**: Scion is back and is going to sell a kei truck in America

**原文链接**: [https://www.theautopian.com/scion-is-back-and-its-going-to-sell-a-freaking-kei-truck-in-america/](https://www.theautopian.com/scion-is-back-and-its-going-to-sell-a-freaking-kei-truck-in-america/)

生成摘要时出错

---

## 74. Hacking the Meta Ray-Ban smartglasses

**原文标题**: Hacking the Meta Ray-Ban smartglasses

**原文链接**: [https://p0pcycle.com/2026/11/06/hacking-the-meta-ray-ban-smartglasses/](https://p0pcycle.com/2026/11/06/hacking-the-meta-ray-ban-smartglasses/)

生成摘要时出错

---

## 75. JSON vs. jsonb in Postgres: size and speed, measured

**原文标题**: JSON vs. jsonb in Postgres: size and speed, measured

**原文链接**: [https://now-next.nl/en/insights/postgresql-json-vs-jsonb-measured/](https://now-next.nl/en/insights/postgresql-json-vs-jsonb-measured/)

生成摘要时出错

---

## 76. Show HN: I created a library for correctly using SQLite in Go programs

**原文标题**: Show HN: I created a library for correctly using SQLite in Go programs

**原文链接**: [https://github.com/cattlecloud/litesql](https://github.com/cattlecloud/litesql)

生成摘要时出错

---

## 77. No device left behind: Home Assistant Connect AUX-2

**原文标题**: No device left behind: Home Assistant Connect AUX-2

**原文链接**: [https://www.home-assistant.io/blog/2026/11/11/no-device-left-behind-home-assistant-connect-aux-2/](https://www.home-assistant.io/blog/2026/11/11/no-device-left-behind-home-assistant-connect-aux-2/)

生成摘要时出错

---

## 78. AUX-2 – No device left behind

**原文标题**: AUX-2 – No device left behind

**原文链接**: [https://www.home-assistant.io/connect/aux-2/](https://www.home-assistant.io/connect/aux-2/)

生成摘要时出错

---

## 79. AMD's Zen 6 Family: Feeding the Beast

**原文标题**: AMD's Zen 6 Family: Feeding the Beast

**原文链接**: [https://chipsandcheese.com/p/amds-zen-6-family-feeding-the-beast](https://chipsandcheese.com/p/amds-zen-6-family-feeding-the-beast)

生成摘要时出错

---

## 80. Make this forward pass as fast as possible

**原文标题**: Make this forward pass as fast as possible

**原文链接**: [https://ianbarber.blog/2026/11/09/make-this-forward-pass-as-fast-as-possible/](https://ianbarber.blog/2026/11/09/make-this-forward-pass-as-fast-as-possible/)

生成摘要时出错

---

## 81. $30M Raised to Redo the CPU

**原文标题**: $30M Raised to Redo the CPU

**原文链接**: [https://tendrils.co/blog/2026-11-10/30m-raised](https://tendrils.co/blog/2026-11-10/30m-raised)

生成摘要时出错

---

## 82. Show HN: Valencia, Spain in Sim City/Isometric View

**原文标题**: Show HN: Valencia, Spain in Sim City/Isometric View

**原文链接**: [https://tinyvalencia.com/](https://tinyvalencia.com/)

生成摘要时出错

---

## 83. Zellij 0.46: built-in terminal, attention inbox, session previews

**原文标题**: Zellij 0.46: built-in terminal, attention inbox, session previews

**原文链接**: [https://zellij.dev/news/terminal-inbox-session-previews/](https://zellij.dev/news/terminal-inbox-session-previews/)

生成摘要时出错

---

## 84. CVE-2026-119618 (critical): mod_HTTP2: heap corruption and RCE in assign_headers

**原文标题**: CVE-2026-119618 (critical): mod_HTTP2: heap corruption and RCE in assign_headers

**原文链接**: [https://httpd.apache.org/security/vulnerabilities_24.html](https://httpd.apache.org/security/vulnerabilities_24.html)

生成摘要时出错

---

## 85. Gemini Decision 1 is Free on Google AI Studio

**原文标题**: Gemini Decision 1 is Free on Google AI Studio

**原文链接**: [https://aistudio.google.com/docs/decisions-api](https://aistudio.google.com/docs/decisions-api)

生成摘要时出错

---

## 86. LLMs Play Zachtronics' TIS-100

**原文标题**: LLMs Play Zachtronics' TIS-100

**原文链接**: [https://tis-100.wincon.dev/](https://tis-100.wincon.dev/)

生成摘要时出错

---

## 87. I deleted all my SSH keys

**原文标题**: I deleted all my SSH keys

**原文链接**: [https://blog.infected.systems/posts/2026-11-03-i-deleted-all-my-ssh-keys/](https://blog.infected.systems/posts/2026-11-03-i-deleted-all-my-ssh-keys/)

生成摘要时出错

---

## 88. Simon Winchester has died

**原文标题**: Simon Winchester has died

**原文链接**: [https://www.nytimes.com/2026/11/04/obituaries/simon-winchester-dead.html](https://www.nytimes.com/2026/11/04/obituaries/simon-winchester-dead.html)

生成摘要时出错

---

## 89. What constant surveillance is doing to children and parents

**原文标题**: What constant surveillance is doing to children and parents

**原文链接**: [https://www.theatlantic.com/magazine/2026/12/location-tracking-apps-parental-surveillance/689031/](https://www.theatlantic.com/magazine/2026/12/location-tracking-apps-parental-surveillance/689031/)

生成摘要时出错

---

## 90. Lunch with Alan Kay: how to become educated enough to invent the future (2019)

**原文标题**: Lunch with Alan Kay: how to become educated enough to invent the future (2019)

**原文链接**: [https://stevekrouse.com/syndicated/alan-kay-lunch](https://stevekrouse.com/syndicated/alan-kay-lunch)

生成摘要时出错

---

## 91. M John Harrison becomes first science fiction author to win the Booker

**原文标题**: M John Harrison becomes first science fiction author to win the Booker

**原文链接**: [https://www.theguardian.com/books/2026/nov/09/m-john-harrison-the-end-of-everything-wins-2026-booker-prize](https://www.theguardian.com/books/2026/nov/09/m-john-harrison-the-end-of-everything-wins-2026-booker-prize)

生成摘要时出错

---

## 92. Queens Public Library under ransomware attack

**原文标题**: Queens Public Library under ransomware attack

**原文链接**: [https://connect.queenslibrary.org/](https://connect.queenslibrary.org/)

生成摘要时出错

---

## 93. Gen X will outnumber Baby Boomers in US Congress

**原文标题**: Gen X will outnumber Baby Boomers in US Congress

**原文链接**: [https://www.ctinsider.com/columnist/article/gen-x-boomers-congress-2027-22522678.php](https://www.ctinsider.com/columnist/article/gen-x-boomers-congress-2027-22522678.php)

生成摘要时出错

---

## 94. Six Math Essentials

**原文标题**: Six Math Essentials

**原文链接**: [https://teorth.github.io/tao-web/six-math-essentials.html](https://teorth.github.io/tao-web/six-math-essentials.html)

生成摘要时出错

---

## 95. Starlink Mini 2

**原文标题**: Starlink Mini 2

**原文链接**: [https://starlink.com/mini-2](https://starlink.com/mini-2)

生成摘要时出错

---

## 96. A comprehensive study of how fingerprintable users are

**原文标题**: A comprehensive study of how fingerprintable users are

**原文链接**: [https://fingerprinting.study/](https://fingerprinting.study/)

生成摘要时出错

---

## 97. A ZIP-style Prolog VM for trilog

**原文标题**: A ZIP-style Prolog VM for trilog

**原文链接**: [https://github.com/no382001/zipc](https://github.com/no382001/zipc)

生成摘要时出错

---

## 98. A Compendium of Abandoned Greenhouses

**原文标题**: A Compendium of Abandoned Greenhouses

**原文链接**: [https://www.messynessychic.com/2015/01/15/a-compendium-of-abandoned-greenhouses/](https://www.messynessychic.com/2015/01/15/a-compendium-of-abandoned-greenhouses/)

生成摘要时出错

---

## 99. AlphaProof Code

**原文标题**: AlphaProof Code

**原文链接**: [https://deepmind.google/blog/introducing-alphaproof-code/](https://deepmind.google/blog/introducing-alphaproof-code/)

生成摘要时出错

---

## 100. Synaptics patent claims stop work on DisplayLink drivers

**原文标题**: Synaptics patent claims stop work on DisplayLink drivers

**原文链接**: [https://lwn.net/SubscriberLink/1102549/acbc92e00cee3a3f/](https://lwn.net/SubscriberLink/1102549/acbc92e00cee3a3f/)

生成摘要时出错

---

