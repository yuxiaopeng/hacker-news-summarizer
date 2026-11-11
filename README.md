# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-11.md)

*最后自动更新时间: 2026-11-11 23:46:15*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-11](output/hacker_news_summary_2026-11-11.md) |
| 2 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 3 | [2026-11-10](output/hacker_news_summary_2026-11-10.md) |
| 4 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 5 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 6 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 7 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 8 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 9 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 10 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 11 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 12 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 13 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 14 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 15 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 16 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 17 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 18 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 19 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 20 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 21 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 22 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 23 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 24 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 25 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 26 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 27 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 28 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 29 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 30 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 31 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 32 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 33 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 34 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 35 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 36 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 37 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 38 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 39 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 40 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 41 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 42 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 43 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 44 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 45 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 46 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 47 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 48 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 49 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 50 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 51 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 52 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 53 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 54 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 55 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 56 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 57 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 58 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 59 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 60 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 61 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 62 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 63 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 64 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 65 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 66 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 67 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 68 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 69 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 70 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 71 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 72 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 73 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 74 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 75 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 76 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 77 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 78 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 79 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 80 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 81 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 82 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 83 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 84 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 85 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 86 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 87 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 88 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 89 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 90 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 91 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 92 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 93 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 94 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 95 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 96 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 97 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 98 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 99 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 100 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 101 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 102 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 103 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 104 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 105 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 106 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 107 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 108 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 109 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 110 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 111 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 112 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 113 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 114 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 115 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 116 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 117 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 118 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 119 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 120 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 121 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 122 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 123 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 124 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 125 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 126 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 127 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 128 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 129 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 130 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 131 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 132 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 133 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 134 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 135 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 136 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 137 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 138 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 139 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 140 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 141 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 142 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 143 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 144 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 145 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 146 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 147 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 148 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 149 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 150 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 151 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 152 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 153 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 154 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 155 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 156 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 157 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 158 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 159 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 160 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 161 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 162 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 163 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 164 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 165 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 166 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 167 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 168 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 169 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 170 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 171 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 172 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 173 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 174 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 175 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 176 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 177 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 178 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 179 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 180 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 181 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 182 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 183 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 184 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 185 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 186 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 187 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 188 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 189 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 190 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 191 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 192 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 193 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 194 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 195 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 196 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 197 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 198 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 199 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 200 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 201 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 202 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 203 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 204 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 205 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 206 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 207 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 208 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 209 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 210 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 211 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 212 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 213 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 214 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 215 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 216 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 217 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 218 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 219 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 220 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 221 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 222 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 223 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 224 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 225 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 226 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 227 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 228 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 229 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 230 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 231 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 232 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 233 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 234 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 235 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 236 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 237 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 238 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 239 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 240 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 241 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 242 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 243 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 244 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 245 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 246 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 247 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 248 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 249 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 250 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 251 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 252 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 253 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 254 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 255 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 256 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 257 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 258 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 259 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 260 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 261 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 262 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 263 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 264 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 265 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 266 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 267 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 268 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 269 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 270 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 271 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 272 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 273 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 274 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 275 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 276 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 277 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 278 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 279 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 280 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 281 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 282 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 283 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 284 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 285 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 286 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 287 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 288 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 289 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 290 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 291 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 292 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 293 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 294 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 295 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 296 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 297 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 298 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 299 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 300 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 301 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 302 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 303 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 304 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 305 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 306 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 307 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 308 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 309 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 310 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 311 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 312 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 313 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 314 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 315 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 316 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 317 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 318 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 319 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 320 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 321 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 322 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 323 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 324 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 325 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 326 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 327 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 328 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 329 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 330 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 331 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 332 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 333 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 334 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 335 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 336 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 337 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 338 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 339 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 340 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 341 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 342 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 343 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 344 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 345 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 346 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 347 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 348 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 349 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 350 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 351 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 352 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 353 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 354 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 355 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 356 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 357 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 358 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 359 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 360 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 361 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 362 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 363 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 364 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 365 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 366 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 367 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 368 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 369 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 370 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 371 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 372 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 373 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 374 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 375 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 376 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 377 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 378 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 379 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 380 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 381 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 382 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 383 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 384 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 385 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 386 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 387 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 388 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 389 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 390 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 391 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 392 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 393 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 394 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 395 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 396 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 397 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 398 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 399 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 400 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 401 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 402 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 403 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 404 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 405 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 406 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 407 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 408 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 409 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 410 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 411 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 412 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 413 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 414 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 415 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 416 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 417 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 418 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 419 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 420 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 421 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 422 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 423 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 424 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 425 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 426 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 427 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 428 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 429 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 430 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 431 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 432 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 433 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 434 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 435 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 436 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 437 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 438 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 439 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 440 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 441 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 442 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 443 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 444 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 445 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 446 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 447 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 448 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 449 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 450 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 451 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 452 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 453 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 454 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 455 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 456 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 457 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 458 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 459 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 460 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 461 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 462 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 463 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 464 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 465 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 466 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 467 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 468 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 469 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 470 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 471 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 472 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 473 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 474 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 475 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 476 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 477 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 478 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 479 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 480 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 481 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 482 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 483 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 484 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 485 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 486 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 487 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 488 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 489 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 490 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 491 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 492 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 493 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 494 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 495 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 496 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 497 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 498 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 499 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 500 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 501 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 502 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 503 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 504 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 505 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 506 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 507 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 508 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 509 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 510 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 511 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 512 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 513 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 514 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 515 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 516 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 517 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 518 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 519 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 520 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 521 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 522 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 523 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 524 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 525 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 526 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 527 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 528 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 529 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 530 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 531 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 532 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 533 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 534 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 535 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 536 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 537 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 538 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 539 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 540 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 541 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 542 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 543 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 544 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 545 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 546 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 547 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 548 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 549 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 550 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 551 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 552 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 553 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 554 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 555 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 556 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 557 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 558 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 559 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 560 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 561 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 562 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 563 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 564 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 565 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 566 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 567 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 568 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 569 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 570 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 571 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 572 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 573 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 574 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 575 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 576 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 577 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 578 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 579 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 580 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 581 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 582 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 583 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 584 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 585 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 586 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 587 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 588 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 589 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 590 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 591 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 592 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 593 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 594 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 595 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 596 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 597 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
