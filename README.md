# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-08.md)

*最后自动更新时间: 2026-02-08 17:56:41*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 2 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 3 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 4 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 5 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 6 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 7 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 8 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 9 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 10 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 11 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 12 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 13 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 14 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 15 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 16 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 17 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 18 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 19 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 20 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 21 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 22 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 23 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 24 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 25 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 26 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 27 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 28 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 29 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 30 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 31 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 32 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 33 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 34 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 35 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 36 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 37 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 38 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 39 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 40 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 41 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 42 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 43 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 44 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 45 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 46 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 47 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 48 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 49 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 50 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 51 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 52 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 53 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 54 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 55 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 56 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 57 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 58 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 59 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 60 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 61 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 62 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 63 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 64 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 65 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 66 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 67 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 68 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 69 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 70 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 71 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 72 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 73 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 74 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 75 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 76 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 77 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 78 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 79 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 80 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 81 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 82 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 83 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 84 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 85 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 86 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 87 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 88 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 89 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 90 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 91 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 92 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 93 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 94 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 95 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 96 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 97 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 98 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 99 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 100 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 101 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 102 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 103 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 104 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 105 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 106 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 107 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 108 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 109 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 110 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 111 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 112 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 113 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 114 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 115 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 116 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 117 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 118 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 119 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 120 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 121 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 122 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 123 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 124 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 125 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 126 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 127 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 128 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 129 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 130 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 131 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 132 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 133 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 134 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 135 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 136 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 137 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 138 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 139 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 140 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 141 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 142 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 143 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 144 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 145 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 146 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 147 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 148 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 149 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 150 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 151 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 152 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 153 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 154 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 155 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 156 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 157 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 158 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 159 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 160 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 161 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 162 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 163 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 164 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 165 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 166 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 167 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 168 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 169 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 170 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 171 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 172 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 173 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 174 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 175 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 176 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 177 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 178 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 179 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 180 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 181 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 182 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 183 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 184 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 185 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 186 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 187 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 188 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 189 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 190 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 191 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 192 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 193 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 194 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 195 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 196 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 197 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 198 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 199 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 200 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 201 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 202 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 203 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 204 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 205 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 206 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 207 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 208 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 209 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 210 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 211 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 212 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 213 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 214 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 215 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 216 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 217 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 218 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 219 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 220 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 221 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 222 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 223 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 224 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 225 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 226 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 227 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 228 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 229 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 230 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 231 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 232 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 233 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 234 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 235 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 236 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 237 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 238 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 239 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 240 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 241 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 242 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 243 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 244 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 245 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 246 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 247 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 248 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 249 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 250 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 251 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 252 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 253 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 254 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 255 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 256 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 257 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 258 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 259 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 260 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 261 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 262 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 263 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 264 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 265 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 266 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 267 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 268 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 269 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 270 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 271 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 272 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 273 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 274 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 275 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 276 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 277 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 278 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 279 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 280 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 281 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 282 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 283 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 284 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 285 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 286 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 287 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 288 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 289 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 290 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 291 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 292 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 293 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 294 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 295 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 296 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 297 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 298 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 299 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 300 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 301 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 302 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 303 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 304 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 305 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 306 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 307 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 308 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 309 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 310 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 311 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 312 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 313 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 314 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 315 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 316 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 317 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 318 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 319 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 320 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 321 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 322 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 323 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 324 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 325 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
