# Hacker News 热门文章摘要 (2026-02-08)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 通过子代理与代理定义的组合可以绕过计费。

**原文标题**: Billing can be bypassed using a combo of subagents with an agent definition

**原文链接**: [https://github.com/microsoft/vscode/issues/292452](https://github.com/microsoft/vscode/issues/292452)

GitHub issue #292452 描述了微软 VS Code Copilot 中的一个计费绕过漏洞，该漏洞允许用户在不消耗所需“高级请求”额度的情况下，访问 Claude Opus 4.5 等高级 AI 模型。

此漏洞利用了 Copilot 的计费逻辑，该逻辑根据聊天会话中所选的**初始模型**来计算请求成本。通过使用“免费”模型（如 GPT-5 mini）启动会话，并将其作为调用高级子代理的入口，用户即可绕过计费。由于子代理和工具调用目前不消耗额外额度，高级模型的处理费用实际上由免费模型的会话分担了。

报告者“Angry-Orangutan”提供了两种主要的滥用途径：
1. **子代理编排（Subagent Orchestration）：** 定义一个使用高级模型的自定义代理，并指令免费的“编排”模型通过 `runSubagent` 工具将所有用户查询传递给该子代理。
2. **递归循环（Recursive Looping）：** 使用自定义脚本和特定提示将高级模型困在工具调用循环中。在一次测试中，单条消息触发了一个涉及数百次高级模型调用、耗时三小时的过程，而仅消耗了最初的三个额度。

报告还强调了服务器端 API 验证的缺失，指出消息“类型”似乎是在客户端声明的。值得注意的是，研究人员最初将此问题提交给了微软安全响应中心（MSRC），但被要求提交公开 Bug 报告，因为 MSRC 认为计费绕过不属于其安全范畴。该议题目前仍处于开启状态并已指派调查。

---

## 2. 五个学科独立发现了相同的数学，且互不知情。

**原文标题**: Five disciplines discovered the same math independently – none of them knew

**原文链接**: [https://freethemath.org](https://freethemath.org)

本文探讨了“趋同发现”现象，即至少六个不同的科学学科独立开发出了相同的数学工具，用以预测复杂系统中的“临界点”。这些临界点代表了微小变化引发连锁反应的时刻，例如市场崩盘、电网断电、心脏衰竭和交通拥堵。

尽管这种数学工具具有普适性，但包括物理学（1944年）、金融学（1994年）、生物学（1994年）和机器学习（2001年）在内的各个领域在数十年间仍处于隔绝状态。研究人员发明了各自的术语并仅引用本领域的文献，在很大程度上并未意识到其他学科已经解决了相同的问题。这种碎片化导致了大量的“重复研究”，并推迟了医疗和基础设施领域关键工具的开发。

这项研究记录在独立研究员布鲁斯·斯蒂芬森（Bruce Stephenson）发表的一篇 arXiv 论文中，并得到了苏黎世联邦理工学院迪迪埃·索内特（Didier Sornette）的支持。该研究利用引用网络分析证明，尽管这些领域研究的是相同的现象，但它们之间仍然相互孤立。分析强调，虽然这些独立发现在其特定领域内为人所知，但这种跨领域趋同的完整模式直到现在才被量化。

最终，文章认为这种数学框架是任何互连系统的基本属性，可以从第一性原理中推导出来。结论指出，这种至关重要的知识应当跨越所有学科边界免费开放，以防止未来在解决紧迫的全球和生物挑战时出现延误。

---

## 3. 运行你自己的 AS：在 FreeBSD 上结合 FRR、GRE 隧道和策略路由实现 BGP

**原文标题**: Running Your Own As: BGP on FreeBSD with FRR, GRE Tunnels, and Policy Routing

**原文链接**: [https://blog.hofstede.it/running-your-own-as-bgp-on-freebsd-with-frr-gre-tunnels-and-policy-routing/](https://blog.hofstede.it/running-your-own-as-bgp-on-freebsd-with-frr-gre-tunnels-and-policy-routing/)

本文概述了个人如何利用 FreeBSD 和 FRR 运行自己的自治系统 (AS) 并广播提供商无关 (PI) 的 IPv6 前缀。通过与赞助本地互联网注册机构 (LIR) 合作，爱好者可以从 RIPE 获取 AS 号和地址空间，从而在更换托管服务提供商时也能保持 IP 地址不变。

**设置的关键组件：**

*   **架构：** 该设计采用双层架构。一台中央 FreeBSD BGP 路由器与上游中转提供商建立对等连接，随后通过 GIF (IPv6-in-IPv4) 和 GRE 隧道将特定子网分发给远程下游服务器。
*   **BGP 配置 (FRR)：** 路由器使用 FRR 管理 BGP 会话。关键配置包括：
    *   **前缀过滤：** 采用严格的入站 bogon 过滤器和出站过滤器，以防止路由泄漏或劫持。
    *   **流量工程：** 利用 BGP 团体属性 (communities) 和 AS-path 预挂 (prepending) 来影响入站流量路径。
    *   **安全：** 实施 GTSM (TTL 安全)、软重配置和最大前缀限制，以保护 BGP 控制平面。
*   **系统路由：** 为聚合的 /48 前缀配置了关键的“黑洞”路由，以防止未分配子网产生路由环路。
*   **防火墙 (PF)：** FreeBSD 的 PF 防火墙经配置可严格隔离控制平面流量 (BGP/SSH) 与数据平面转发。同时实施 MSS 调整 (clamping)，以抵消 GRE 和 GIF 隧道带来的 MTU 开销。

最终，此配置提供了一个健壮且可移植的网络环境，使用户能够在多个物理或虚拟位置对其全球 IPv6 地址空间拥有完全的控制权。

---

## 4. RFC 3092 – “Foo”的词源 (2001)

**原文标题**: RFC 3092 – Etymology of "Foo" (2001)

**原文链接**: [https://datatracker.ietf.org/doc/html/rfc3092](https://datatracker.ietf.org/doc/html/rfc3092)

RFC 3092《“Foo”的语源》是 2001 年发布的一份信息化文档，旨在解释“foo”、“bar”和“foobar”等常见元语法变量的起源与用法。这些术语在技术文档中被用作任意文件、函数或变量的标准占位符。截至该文档发布时，约 7% 的 RFC 文档中都出现了这些词汇。

“foo”的语源是多方面的：
*   **流行文化**：该词在 20 世纪 30 年代通过比尔·霍尔曼（Bill Holman）的漫画《斯莫基·斯托弗》（Smokey Stover）而流行，漫画中将其用于荒诞的口号中（例如“有 foo 的地方就有火”）。霍尔曼可能借鉴了小雕像上出现的汉字“福”（意为幸福）。
*   **军事用途**：二战期间，“foo fighters”是当时对不明飞行物（UFO）的称呼，英国军队则将“FOO”作为一种半传奇性的涂鸦，类似于“基尔罗伊到此一游”（Kilroy was here）。术语 FUBAR（意为“彻底搞砸，无法修复”）也诞生于这一时期，可能影响了后来“foobar”的演变。
*   **技术历史**：麻省理工学院技术模型铁路俱乐部（TMRC）在其 1959 年的词典中将“foo”列为“神圣音节”。到了 20 世纪 60 和 70 年代，“foobar”通过数字设备公司（DEC）的手册得以广泛传播。
*   **语言学**：该术语可能受到意第绪语“feh”的影响，或者源于 13 世纪表示“敌人”或“魔鬼”的“foo”用法。

该文档还探讨了常见的缩写词和逆向缩写词，例如“前沿观察官”（Forward Observation Officer）或“大地址记录上的 FTP 操作”（RFC 1639）。最终，RFC 3092 为这些术语提供了历史背景，旨在帮助新手和非英语母语者理解这些常见的互联网术语。

---

## 5. 担保

**原文标题**: Vouch

**原文链接**: [https://github.com/mitchellh/vouch](https://github.com/mitchellh/vouch)

**Vouch** 是一个实验性的信任管理系统，旨在保护开源项目免受低质量、AI 生成的贡献的影响。为了应对软件开发格局的变化——即 AI 工具可以生成看似合理但质量低劣的代码——Vouch 将项目从“先信任后验证”模式转变为**显式信任模型**。

**核心特性与功能：**
*   **担保与谴责：** 项目维护者可以“担保”（vouch）贡献者以授予其访问权限，或“谴责”（denounce）他们以阻止其交互。这些策略完全可由项目自行配置。
*   **信任网络：** Vouch 允许项目共享信任决策。通过读取其他项目的担保列表，维护者可以创建一个更大的生态系统，使在一个项目中被证明值得信赖的用户在另一个项目中也能自动获得信任。
*   **GitHub 集成：** 该系统提供原生的 GitHub Actions 来自动化工作流，例如检查 PR 作者，以及直接通过 issue 或 discussion 评论来管理信任级别。
*   **Nushell CLI：** 以 Nushell 模块形式实现的命令行界面允许进行本地管理（添加、检查或谴责用户），且无需外部依赖。
*   **Trustdown (.td) 格式：** 信任列表以一种名为“Trustdown”的简单扁平文件格式存储。它旨在易于通过标准 POSIX 工具解析且具备良好的可读性，确保数据具有可移植性和易访问性。

Vouch 目前已被 **Ghostty** 项目采用。它的设计具有足够的通用性，适用于任何代码托管平台，同时为 GitHub 用户提供强大且自动化的体验。其目标是通过关注已建立的人类声誉，而非仅仅是提交 Pull Request 的能力，来重新建立开源贡献的准入门槛。

---

## 6. GitHub 智能体工作流

**原文标题**: GitHub Agentic Workflows

**原文链接**: [https://github.github.io/gh-aw/](https://github.github.io/gh-aw/)

**GitHub Agentic Workflows** 由 GitHub Next 和微软研究院（Microsoft Research）开发，引入了在 GitHub Actions 中运行的自动化仓库智能体。该系统允许开发者通过简单的 Markdown 文件（而非复杂的 YAML 代码）定义 AI 驱动的自动化，从而管理和优化代码仓库。

### **核心功能**
该系统通过三个步骤运行：
1.  **编写：** 在 `.md` 文件中以自然语言编写自动化指令。
2.  **编译：** 使用 `gh aw` 命令行工具将 Markdown 转换为安全的 GitHub Actions 工作流（`.lock.yml`）。
3.  **运行：** GitHub Actions 根据计划任务或手动触发，在容器化环境中执行工作流。

### **关键特性**
*   **AI 驱动的决策：** 智能体利用 GitHub Copilot、Claude 和 Codex 等引擎理解仓库上下文，以适应各种场景。
*   **安全优先设计：** 工作流默认以只读权限运行。写入操作需通过“安全输出”获得明确授权，且执行过程在具备网络隔离和工具白名单的沙箱环境中进行。
*   **深度集成：** 智能体可直接与 GitHub Issues、Pull Requests、Discussions 以及仓库管理工具进行交互。

### **应用场景**
这些工作流旨在将“持续 AI”（Continuous AI）应用于多个领域：
*   **维护：** 自动化文档更新、代码重构和代码风格优化。
*   **管理：** 自动化 Issue 分类、标签管理和项目协调。
*   **质量保证：** CI 失败诊断、测试覆盖率提升和安全扫描。
*   **报告：** 生成每日状态报告、趋势分析和团队指标。

总之，GitHub Agentic Workflows 通过实现安全、可扩展且与现有 GitHub 生态系统深度集成的自然语言自动化，极大地简化了 DevOps 流程。

---

## 7. I put a real-time 3D shader on the Game Boy Color

**原文标题**: I put a real-time 3D shader on the Game Boy Color

**原文链接**: [https://blog.otterstack.com/posts/202512-gbshader/](https://blog.otterstack.com/posts/202512-gbshader/)

生成摘要时出错

---

## 8. Omega-3 is inversely related to risk of early-onset dementia

**原文标题**: Omega-3 is inversely related to risk of early-onset dementia

**原文链接**: [https://pubmed.ncbi.nlm.nih.gov/41506004/](https://pubmed.ncbi.nlm.nih.gov/41506004/)

生成摘要时出错

---

## 9. Curating a Show on My Ineffable Mother, Ursula K. Le Guin

**原文标题**: Curating a Show on My Ineffable Mother, Ursula K. Le Guin

**原文链接**: [https://hyperallergic.com/curating-a-show-on-my-ineffable-mother-ursula-k-le-guin/](https://hyperallergic.com/curating-a-show-on-my-ineffable-mother-ursula-k-le-guin/)

生成摘要时出错

---

## 10. Show HN: It took 4 years to sell my startup. I wrote a book about it

**原文标题**: Show HN: It took 4 years to sell my startup. I wrote a book about it

**原文链接**: [https://derekyan.com/ma-book/](https://derekyan.com/ma-book/)

生成摘要时出错

---

## 11. Why E cores make Apple silicon fast

**原文标题**: Why E cores make Apple silicon fast

**原文链接**: [https://eclecticlight.co/2026/02/08/last-week-on-my-mac-why-e-cores-make-apple-silicon-fast/](https://eclecticlight.co/2026/02/08/last-week-on-my-mac-why-e-cores-make-apple-silicon-fast/)

生成摘要时出错

---

## 12. Exploiting signed bootloaders to circumvent UEFI Secure Boot

**原文标题**: Exploiting signed bootloaders to circumvent UEFI Secure Boot

**原文链接**: [https://habr.com/en/articles/446238/](https://habr.com/en/articles/446238/)

生成摘要时出错

---

## 13. The Contagious Taste of Cancer

**原文标题**: The Contagious Taste of Cancer

**原文链接**: [https://www.historytoday.com/archive/history-matters/contagious-taste-cancer](https://www.historytoday.com/archive/history-matters/contagious-taste-cancer)

生成摘要时出错

---

## 14. Reverse Engineering Raiders of the Lost Ark for the Atari 2600

**原文标题**: Reverse Engineering Raiders of the Lost Ark for the Atari 2600

**原文链接**: [https://github.com/joshuanwalker/Raiders2600](https://github.com/joshuanwalker/Raiders2600)

生成摘要时出错

---

## 15. Matchlock – Secures AI agent workloads with a Linux-based sandbox

**原文标题**: Matchlock – Secures AI agent workloads with a Linux-based sandbox

**原文链接**: [https://github.com/jingkaihe/matchlock](https://github.com/jingkaihe/matchlock)

生成摘要时出错

---

## 16. Dave Farber has died

**原文标题**: Dave Farber has died

**原文链接**: [https://lists.nanog.org/archives/list/nanog@lists.nanog.org/thread/TSNPJVFH4DKLINIKSMRIIVNHDG5XKJCM/](https://lists.nanog.org/archives/list/nanog@lists.nanog.org/thread/TSNPJVFH4DKLINIKSMRIIVNHDG5XKJCM/)

生成摘要时出错

---

## 17. OpenClaw is changing my life

**原文标题**: OpenClaw is changing my life

**原文链接**: [https://reorx.com/blog/openclaw-is-changing-my-life/](https://reorx.com/blog/openclaw-is-changing-my-life/)

生成摘要时出错

---

## 18. Kolakoski Sequence

**原文标题**: Kolakoski Sequence

**原文链接**: [https://en.wikipedia.org/wiki/Kolakoski_sequence](https://en.wikipedia.org/wiki/Kolakoski_sequence)

生成摘要时出错

---

## 19. Slop Terrifies Me

**原文标题**: Slop Terrifies Me

**原文链接**: [https://ezhik.jp/ai-slop-terrifies-me/](https://ezhik.jp/ai-slop-terrifies-me/)

生成摘要时出错

---

## 20. Show HN: LocalGPT – A local-first AI assistant in Rust with persistent memory

**原文标题**: Show HN: LocalGPT – A local-first AI assistant in Rust with persistent memory

**原文链接**: [https://github.com/localgpt-app/localgpt](https://github.com/localgpt-app/localgpt)

生成摘要时出错

---

## 21. Beyond agentic coding

**原文标题**: Beyond agentic coding

**原文链接**: [https://haskellforall.com/2026/02/beyond-agentic-coding](https://haskellforall.com/2026/02/beyond-agentic-coding)

生成摘要时出错

---

## 22. DoNotNotify is now Open Source

**原文标题**: DoNotNotify is now Open Source

**原文链接**: [https://donotnotify.com/opensource.html](https://donotnotify.com/opensource.html)

生成摘要时出错

---

## 23. A11yJSON: A standard to describe the accessibility of the physical world

**原文标题**: A11yJSON: A standard to describe the accessibility of the physical world

**原文链接**: [https://sozialhelden.github.io/a11yjson/](https://sozialhelden.github.io/a11yjson/)

生成摘要时出错

---

## 24. Rabbit Ear "Origami": programmable origami in the browser

**原文标题**: Rabbit Ear "Origami": programmable origami in the browser

**原文链接**: [https://rabbitear.org/book/origami.html](https://rabbitear.org/book/origami.html)

生成摘要时出错

---

## 25. The Legacy of Daniel Kahneman: A Personal View (2025)

**原文标题**: The Legacy of Daniel Kahneman: A Personal View (2025)

**原文链接**: [https://ejpe.org/journal/article/view/1075/753](https://ejpe.org/journal/article/view/1075/753)

生成摘要时出错

---

## 26. Let's compile Quake like it's 1997

**原文标题**: Let's compile Quake like it's 1997

**原文链接**: [https://fabiensanglard.net/compile_like_1997/index.html](https://fabiensanglard.net/compile_like_1997/index.html)

生成摘要时出错

---

## 27. We mourn our craft

**原文标题**: We mourn our craft

**原文链接**: [https://nolanlawson.com/2026/02/07/we-mourn-our-craft/](https://nolanlawson.com/2026/02/07/we-mourn-our-craft/)

生成摘要时出错

---

## 28. Roger Ebert Reviews "The Shawshank Redemption" (1999)

**原文标题**: Roger Ebert Reviews "The Shawshank Redemption" (1999)

**原文链接**: [https://www.rogerebert.com/reviews/great-movie-the-shawshank-redemption-1994](https://www.rogerebert.com/reviews/great-movie-the-shawshank-redemption-1994)

生成摘要时出错

---

## 29. SectorC: A C Compiler in 512 bytes (2023)

**原文标题**: SectorC: A C Compiler in 512 bytes (2023)

**原文链接**: [https://xorvoid.com/sectorc.html](https://xorvoid.com/sectorc.html)

生成摘要时出错

---

## 30. I am happier writing code by hand

**原文标题**: I am happier writing code by hand

**原文链接**: [https://www.abhinavomprakash.com/posts/i-am-happier-writing-code-by-hand/](https://www.abhinavomprakash.com/posts/i-am-happier-writing-code-by-hand/)

生成摘要时出错

---

## 31. I write games in C (yes, C) (2016)

**原文标题**: I write games in C (yes, C) (2016)

**原文链接**: [https://jonathanwhiting.com/writing/blog/games_in_c/](https://jonathanwhiting.com/writing/blog/games_in_c/)

生成摘要时出错

---

## 32. The Architecture of Open Source Applications (Volume 1) Berkeley DB

**原文标题**: The Architecture of Open Source Applications (Volume 1) Berkeley DB

**原文链接**: [https://aosabook.org/en/v1/bdb.html](https://aosabook.org/en/v1/bdb.html)

生成摘要时出错

---

## 33. LLMs as the new high level language

**原文标题**: LLMs as the new high level language

**原文链接**: [https://federicopereiro.com/llm-high/](https://federicopereiro.com/llm-high/)

生成摘要时出错

---

## 34. Software factories and the agentic moment

**原文标题**: Software factories and the agentic moment

**原文链接**: [https://factory.strongdm.ai/](https://factory.strongdm.ai/)

生成摘要时出错

---

## 35. Show HN: Fine-tuned Qwen2.5-7B on 100 films for probabilistic story graphs

**原文标题**: Show HN: Fine-tuned Qwen2.5-7B on 100 films for probabilistic story graphs

**原文链接**: [https://cinegraphs.ai/](https://cinegraphs.ai/)

生成摘要时出错

---

## 36. Speed up responses with fast mode

**原文标题**: Speed up responses with fast mode

**原文链接**: [https://code.claude.com/docs/en/fast-mode](https://code.claude.com/docs/en/fast-mode)

生成摘要时出错

---

## 37. How to squeeze a lexicon (2001) [pdf]

**原文标题**: How to squeeze a lexicon (2001) [pdf]

**原文链接**: [https://marcinciura.wordpress.com/wp-content/uploads/2019/10/lexicon.pdf](https://marcinciura.wordpress.com/wp-content/uploads/2019/10/lexicon.pdf)

生成摘要时出错

---

## 38. Vocal Guide – belt sing without killing yourself

**原文标题**: Vocal Guide – belt sing without killing yourself

**原文链接**: [https://jesperordrup.github.io/vocal-guide/](https://jesperordrup.github.io/vocal-guide/)

生成摘要时出错

---

## 39. Hoot: Scheme on WebAssembly

**原文标题**: Hoot: Scheme on WebAssembly

**原文链接**: [https://www.spritely.institute/hoot/](https://www.spritely.institute/hoot/)

生成摘要时出错

---

## 40. AI fatigue is real and nobody talks about it

**原文标题**: AI fatigue is real and nobody talks about it

**原文链接**: [https://siddhantkhare.com/writing/ai-fatigue-is-real](https://siddhantkhare.com/writing/ai-fatigue-is-real)

生成摘要时出错

---

## 41. Stories from 25 Years of Software Development

**原文标题**: Stories from 25 Years of Software Development

**原文链接**: [https://susam.net/twenty-five-years-of-computing.html](https://susam.net/twenty-five-years-of-computing.html)

生成摘要时出错

---

## 42. Arcan Explained – A browser for different webs

**原文标题**: Arcan Explained – A browser for different webs

**原文链接**: [https://arcan-fe.com/2026/01/26/arcan-explained-a-browser-for-different-webs/](https://arcan-fe.com/2026/01/26/arcan-explained-a-browser-for-different-webs/)

生成摘要时出错

---

## 43. uLauncher

**原文标题**: uLauncher

**原文链接**: [https://github.com/jrpie/launcher](https://github.com/jrpie/launcher)

生成摘要时出错

---

## 44. Brookhaven Lab's RHIC concludes 25-year run with final collisions

**原文标题**: Brookhaven Lab's RHIC concludes 25-year run with final collisions

**原文链接**: [https://www.hpcwire.com/off-the-wire/brookhaven-labs-rhic-concludes-25-year-run-with-final-collisions/](https://www.hpcwire.com/off-the-wire/brookhaven-labs-rhic-concludes-25-year-run-with-final-collisions/)

生成摘要时出错

---

## 45. SCOTUS to decide if 1988 video tape privacy law applies to internet uses

**原文标题**: SCOTUS to decide if 1988 video tape privacy law applies to internet uses

**原文链接**: [https://www.jurist.org/news/2026/01/us-supreme-court-to-decide-if-1988-video-tape-privacy-law-applies-to-internet-uses/](https://www.jurist.org/news/2026/01/us-supreme-court-to-decide-if-1988-video-tape-privacy-law-applies-to-internet-uses/)

生成摘要时出错

---

## 46. First Proof

**原文标题**: First Proof

**原文链接**: [https://arxiv.org/abs/2602.05192](https://arxiv.org/abs/2602.05192)

生成摘要时出错

---

## 47. Wood Gas Vehicles: Firewood in the Fuel Tank (2010)

**原文标题**: Wood Gas Vehicles: Firewood in the Fuel Tank (2010)

**原文链接**: [https://solar.lowtechmagazine.com/2010/01/wood-gas-vehicles-firewood-in-the-fuel-tank/](https://solar.lowtechmagazine.com/2010/01/wood-gas-vehicles-firewood-in-the-fuel-tank/)

生成摘要时出错

---

## 48. Total surface area required to fuel the world with solar (2009)

**原文标题**: Total surface area required to fuel the world with solar (2009)

**原文链接**: [https://landartgenerator.org/blagi/archives/127](https://landartgenerator.org/blagi/archives/127)

生成摘要时出错

---

## 49. Modern and Antique Technologies Reveal a Dynamic Cosmos

**原文标题**: Modern and Antique Technologies Reveal a Dynamic Cosmos

**原文链接**: [https://www.quantamagazine.org/how-modern-and-antique-technologies-reveal-a-dynamic-cosmos-20260202/](https://www.quantamagazine.org/how-modern-and-antique-technologies-reveal-a-dynamic-cosmos-20260202/)

生成摘要时出错

---

## 50. Show HN: I saw this cool navigation reveal, so I made a simple HTML+CSS version

**原文标题**: Show HN: I saw this cool navigation reveal, so I made a simple HTML+CSS version

**原文链接**: [https://github.com/Momciloo/fun-with-clip-path](https://github.com/Momciloo/fun-with-clip-path)

生成摘要时出错

---

## 51. Start all of your commands with a comma (2009)

**原文标题**: Start all of your commands with a comma (2009)

**原文链接**: [https://rhodesmill.org/brandon/2009/commands-with-comma/](https://rhodesmill.org/brandon/2009/commands-with-comma/)

生成摘要时出错

---

## 52. OpenCiv3: Open-source, cross-platform reimagining of Civilization III

**原文标题**: OpenCiv3: Open-source, cross-platform reimagining of Civilization III

**原文链接**: [https://openciv3.org/](https://openciv3.org/)

生成摘要时出错

---

## 53. Sargasso Sea

**原文标题**: Sargasso Sea

**原文链接**: [https://en.wikipedia.org/wiki/Sargasso_Sea](https://en.wikipedia.org/wiki/Sargasso_Sea)

生成摘要时出错

---

## 54. LineageOS 23.2

**原文标题**: LineageOS 23.2

**原文链接**: [https://lineageos.org/Changelog-31/](https://lineageos.org/Changelog-31/)

生成摘要时出错

---

## 55. San Francisco's pro-billionaire march draws dozens

**原文标题**: San Francisco's pro-billionaire march draws dozens

**原文链接**: [https://techcrunch.com/2026/02/08/san-franciscos-pro-billionaire-march-draws-dozens/](https://techcrunch.com/2026/02/08/san-franciscos-pro-billionaire-march-draws-dozens/)

生成摘要时出错

---

## 56. The AI boom is causing shortages everywhere else

**原文标题**: The AI boom is causing shortages everywhere else

**原文链接**: [https://www.washingtonpost.com/technology/2026/02/07/ai-spending-economy-shortages/](https://www.washingtonpost.com/technology/2026/02/07/ai-spending-economy-shortages/)

生成摘要时出错

---

## 57. The Waymo World Model

**原文标题**: The Waymo World Model

**原文链接**: [https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation](https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation)

生成摘要时出错

---

## 58. Al Lowe on model trains, funny deaths and working with Disney

**原文标题**: Al Lowe on model trains, funny deaths and working with Disney

**原文链接**: [https://spillhistorie.no/2026/02/06/interview-with-sierra-veteran-al-lowe/](https://spillhistorie.no/2026/02/06/interview-with-sierra-veteran-al-lowe/)

生成摘要时出错

---

## 59. Unseen Footage of Atari Battlezone Arcade Cabinet Production

**原文标题**: Unseen Footage of Atari Battlezone Arcade Cabinet Production

**原文链接**: [https://arcadeblogger.com/2026/02/02/unseen-footage-of-atari-battlezone-cabinet-production/](https://arcadeblogger.com/2026/02/02/unseen-footage-of-atari-battlezone-cabinet-production/)

生成摘要时出错

---

## 60. CCC (Claude's C Compiler) on Compiler Explorer

**原文标题**: CCC (Claude's C Compiler) on Compiler Explorer

**原文链接**: [https://godbolt.org/z/asjc13sa6](https://godbolt.org/z/asjc13sa6)

生成摘要时出错

---

## 61. Where did all the starships go?

**原文标题**: Where did all the starships go?

**原文链接**: [https://www.datawrapper.de/blog/science-fiction-decline](https://www.datawrapper.de/blog/science-fiction-decline)

生成摘要时出错

---

## 62. The F Word

**原文标题**: The F Word

**原文链接**: [http://muratbuffalo.blogspot.com/2026/02/friction.html](http://muratbuffalo.blogspot.com/2026/02/friction.html)

生成摘要时出错

---

## 63. MS-DOS game copy protection and cracks

**原文标题**: MS-DOS game copy protection and cracks

**原文链接**: [https://www.dosdays.co.uk/topics/game_cracks.php](https://www.dosdays.co.uk/topics/game_cracks.php)

生成摘要时出错

---

## 64. Claude Opus 4.6

**原文标题**: Claude Opus 4.6

**原文链接**: [https://www.anthropic.com/news/claude-opus-4-6](https://www.anthropic.com/news/claude-opus-4-6)

生成摘要时出错

---

## 65. Making geo joins faster with H3 indexes

**原文标题**: Making geo joins faster with H3 indexes

**原文链接**: [https://floedb.ai/blog/how-we-made-geo-joins-400-faster-with-h3-indexes](https://floedb.ai/blog/how-we-made-geo-joins-400-faster-with-h3-indexes)

生成摘要时出错

---

## 66. In the Australian outback, we're listening for nuclear tests

**原文标题**: In the Australian outback, we're listening for nuclear tests

**原文链接**: [https://www.abc.net.au/news/2026-02-08/australian-outback-nuclear-tests-listening-warramunga-facility/106307478](https://www.abc.net.au/news/2026-02-08/australian-outback-nuclear-tests-listening-warramunga-facility/106307478)

生成摘要时出错

---

## 67. Substack confirms data breach affects users’ email addresses and phone numbers

**原文标题**: Substack confirms data breach affects users’ email addresses and phone numbers

**原文链接**: [https://techcrunch.com/2026/02/05/substack-confirms-data-breach-affecting-email-addresses-and-phone-numbers/](https://techcrunch.com/2026/02/05/substack-confirms-data-breach-affecting-email-addresses-and-phone-numbers/)

生成摘要时出错

---

## 68. Selection rather than prediction

**原文标题**: Selection rather than prediction

**原文链接**: [https://voratiq.com/blog/selection-rather-than-prediction/](https://voratiq.com/blog/selection-rather-than-prediction/)

生成摘要时出错

---

## 69. Reinforcement Learning from Human Feedback

**原文标题**: Reinforcement Learning from Human Feedback

**原文链接**: [https://rlhfbook.com/](https://rlhfbook.com/)

生成摘要时出错

---

## 70. Bye Bye Humanity: The Potential AMOC Collapse

**原文标题**: Bye Bye Humanity: The Potential AMOC Collapse

**原文链接**: [https://thatjoescott.com/2026/02/03/bye-bye-humanity-the-potential-amoc-collapse/](https://thatjoescott.com/2026/02/03/bye-bye-humanity-the-potential-amoc-collapse/)

生成摘要时出错

---

## 71. FDA intends to take action against non-FDA-approved GLP-1 drugs

**原文标题**: FDA intends to take action against non-FDA-approved GLP-1 drugs

**原文链接**: [https://www.fda.gov/news-events/press-announcements/fda-intends-take-action-against-non-fda-approved-glp-1-drugs](https://www.fda.gov/news-events/press-announcements/fda-intends-take-action-against-non-fda-approved-glp-1-drugs)

生成摘要时出错

---

## 72. Show HN: A luma dependent chroma compression algorithm (image compression)

**原文标题**: Show HN: A luma dependent chroma compression algorithm (image compression)

**原文链接**: [https://www.bitsnbites.eu/a-spatial-domain-variable-block-size-luma-dependent-chroma-compression-algorithm/](https://www.bitsnbites.eu/a-spatial-domain-variable-block-size-luma-dependent-chroma-compression-algorithm/)

生成摘要时出错

---

## 73. Coding agents have replaced every framework I used

**原文标题**: Coding agents have replaced every framework I used

**原文链接**: [https://blog.alaindichiappari.dev/p/software-engineering-is-back](https://blog.alaindichiappari.dev/p/software-engineering-is-back)

生成摘要时出错

---

## 74. Microsoft account bugs locked me out of Notepad – Are thin clients ruining PCs?

**原文标题**: Microsoft account bugs locked me out of Notepad – Are thin clients ruining PCs?

**原文链接**: [https://www.windowscentral.com/microsoft/windows-11/windows-locked-me-out-of-notepad-is-the-thin-client-era-ruining-pcs](https://www.windowscentral.com/microsoft/windows-11/windows-locked-me-out-of-notepad-is-the-thin-client-era-ruining-pcs)

生成摘要时出错

---

## 75. 72M Points of Interest

**原文标题**: 72M Points of Interest

**原文链接**: [https://tech.marksblogg.com/overture-places-pois.html](https://tech.marksblogg.com/overture-places-pois.html)

生成摘要时出错

---

## 76. The Scriptovision Super Micro Script video titler is almost a home computer

**原文标题**: The Scriptovision Super Micro Script video titler is almost a home computer

**原文链接**: [http://oldvcr.blogspot.com/2026/02/the-scriptovision-super-micro-script.html](http://oldvcr.blogspot.com/2026/02/the-scriptovision-super-micro-script.html)

生成摘要时出错

---

## 77. I spent 5 years in DevOps – Solutions engineering gave me what I was missing

**原文标题**: I spent 5 years in DevOps – Solutions engineering gave me what I was missing

**原文链接**: [https://infisical.com/blog/devops-to-solutions-engineering](https://infisical.com/blog/devops-to-solutions-engineering)

生成摘要时出错

---

## 78. Uber held liable, ordered to pay $8.5M in driver rape suit

**原文标题**: Uber held liable, ordered to pay $8.5M in driver rape suit

**原文链接**: [https://www.cnbc.com/2026/02/06/uber-liable-pay-8-5-million-driver-rape-suit.html](https://www.cnbc.com/2026/02/06/uber-liable-pay-8-5-million-driver-rape-suit.html)

生成摘要时出错

---

## 79. France's homegrown open source online office suite

**原文标题**: France's homegrown open source online office suite

**原文链接**: [https://github.com/suitenumerique](https://github.com/suitenumerique)

生成摘要时出错

---

## 80. Dark Alley Mathematics

**原文标题**: Dark Alley Mathematics

**原文链接**: [https://blog.szczepan.org/blog/three-points/](https://blog.szczepan.org/blog/three-points/)

生成摘要时出错

---

## 81. Moroccan sardine prices to stabilise via new measures: officials

**原文标题**: Moroccan sardine prices to stabilise via new measures: officials

**原文链接**: [https://maghrebi.org/2026/01/27/moroccan-sardine-prices-to-stabilise-via-new-measures-officials/](https://maghrebi.org/2026/01/27/moroccan-sardine-prices-to-stabilise-via-new-measures-officials/)

生成摘要时出错

---

## 82. Female Asian Elephant Calf Born at the Smithsonian National Zoo

**原文标题**: Female Asian Elephant Calf Born at the Smithsonian National Zoo

**原文链接**: [https://www.si.edu/newsdesk/releases/female-asian-elephant-calf-born-smithsonians-national-zoo-and-conservation?user_id=66c4bf745d78644b3aa57b08&utm_medium=email&utm_placement=newsletter&utm_source=join1440](https://www.si.edu/newsdesk/releases/female-asian-elephant-calf-born-smithsonians-national-zoo-and-conservation?user_id=66c4bf745d78644b3aa57b08&utm_medium=email&utm_placement=newsletter&utm_source=join1440)

生成摘要时出错

---

## 83. GPT-5.3-Codex

**原文标题**: GPT-5.3-Codex

**原文链接**: [https://openai.com/index/introducing-gpt-5-3-codex/](https://openai.com/index/introducing-gpt-5-3-codex/)

生成摘要时出错

---

## 84. Introducing the Developer Knowledge API and MCP Server

**原文标题**: Introducing the Developer Knowledge API and MCP Server

**原文链接**: [https://developers.googleblog.com/introducing-the-developer-knowledge-api-and-mcp-server/](https://developers.googleblog.com/introducing-the-developer-knowledge-api-and-mcp-server/)

生成摘要时出错

---

## 85. Learning from context is harder than we thought

**原文标题**: Learning from context is harder than we thought

**原文链接**: [https://hy.tencent.com/research/100025?langVersion=en](https://hy.tencent.com/research/100025?langVersion=en)

生成摘要时出错

---

## 86. Show HN: Smooth CLI – Token-efficient browser for AI agents

**原文标题**: Show HN: Smooth CLI – Token-efficient browser for AI agents

**原文链接**: [https://docs.smooth.sh/cli/overview](https://docs.smooth.sh/cli/overview)

生成摘要时出错

---

## 87. Ga68, a GNU Algol 68 Compiler

**原文标题**: Ga68, a GNU Algol 68 Compiler

**原文链接**: [https://fosdem.org/2026/schedule/event/PEXRTN-ga68-intro/](https://fosdem.org/2026/schedule/event/PEXRTN-ga68-intro/)

生成摘要时出错

---

## 88. Hackers (1995) Animated Experience

**原文标题**: Hackers (1995) Animated Experience

**原文链接**: [https://hackers-1995.vercel.app/](https://hackers-1995.vercel.app/)

生成摘要时出错

---

## 89. Show HN: Kappal – CLI to Run Docker Compose YML on Kubernetes for Local Dev

**原文标题**: Show HN: Kappal – CLI to Run Docker Compose YML on Kubernetes for Local Dev

**原文链接**: [https://github.com/sandys/kappal](https://github.com/sandys/kappal)

生成摘要时出错

---

## 90. What Is Ruliology?

**原文标题**: What Is Ruliology?

**原文链接**: [https://writings.stephenwolfram.com/2026/01/what-is-ruliology/](https://writings.stephenwolfram.com/2026/01/what-is-ruliology/)

生成摘要时出错

---

## 91. 80386 Barrel Shifter

**原文标题**: 80386 Barrel Shifter

**原文链接**: [https://nand2mario.github.io/posts/2026/80386_barrel_shifter/](https://nand2mario.github.io/posts/2026/80386_barrel_shifter/)

生成摘要时出错

---

## 92. A new bill in New York would require disclaimers on AI-generated news content

**原文标题**: A new bill in New York would require disclaimers on AI-generated news content

**原文链接**: [https://www.niemanlab.org/2026/02/a-new-bill-in-new-york-would-require-disclaimers-on-ai-generated-news-content/](https://www.niemanlab.org/2026/02/a-new-bill-in-new-york-would-require-disclaimers-on-ai-generated-news-content/)

生成摘要时出错

---

## 93. Stay Away from My Trash

**原文标题**: Stay Away from My Trash

**原文链接**: [https://tldraw.dev/blog/stay-away-from-my-trash](https://tldraw.dev/blog/stay-away-from-my-trash)

生成摘要时出错

---

## 94. My AI Adoption Journey

**原文标题**: My AI Adoption Journey

**原文链接**: [https://mitchellh.com/writing/my-ai-adoption-journey](https://mitchellh.com/writing/my-ai-adoption-journey)

生成摘要时出错

---

## 95. Maihem (YC W24): hiring senior robotics perception engineer (London, on-site)

**原文标题**: Maihem (YC W24): hiring senior robotics perception engineer (London, on-site)

**原文链接**: [https://jobs.ashbyhq.com/maihem/8da3fa8b-5544-45de-a99e-888021519758](https://jobs.ashbyhq.com/maihem/8da3fa8b-5544-45de-a99e-888021519758)

生成摘要时出错

---

## 96. Sheldon Brown's Bicycle Technical Info

**原文标题**: Sheldon Brown's Bicycle Technical Info

**原文链接**: [https://www.sheldonbrown.com/](https://www.sheldonbrown.com/)

生成摘要时出错

---

## 97. An Update on Heroku

**原文标题**: An Update on Heroku

**原文链接**: [https://www.heroku.com/blog/an-update-on-heroku/](https://www.heroku.com/blog/an-update-on-heroku/)

生成摘要时出错

---

## 98. PC Floppy Copy Protection: Vault Prolok

**原文标题**: PC Floppy Copy Protection: Vault Prolok

**原文链接**: [https://martypc.blogspot.com/2024/09/pc-floppy-copy-protection-vault-prolok.html](https://martypc.blogspot.com/2024/09/pc-floppy-copy-protection-vault-prolok.html)

生成摘要时出错

---

## 99. Show HN: Look Ma, No Linux: Shell, App Installer, Vi, Cc on ESP32-S3 / BreezyBox

**原文标题**: Show HN: Look Ma, No Linux: Shell, App Installer, Vi, Cc on ESP32-S3 / BreezyBox

**原文链接**: [https://github.com/valdanylchuk/breezydemo](https://github.com/valdanylchuk/breezydemo)

生成摘要时出错

---

## 100. Eigen: Building a Workspace

**原文标题**: Eigen: Building a Workspace

**原文链接**: [https://reindernijhoff.net/2025/10/eigen-building-a-workspace/](https://reindernijhoff.net/2025/10/eigen-building-a-workspace/)

生成摘要时出错

---

