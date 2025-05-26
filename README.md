# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-05-26.md)

*最后自动更新时间: 2025-05-26 17:48:37*
## 1. 从空气中被动收集水分的新型材料

**原文标题**: A new class of materials that can passively harvest water from air

**原文链接**: [https://blog.seas.upenn.edu/penn-engineers-discover-a-new-class-of-materials-that-passively-harvest-water-from-air/](https://blog.seas.upenn.edu/penn-engineers-discover-a-new-class-of-materials-that-passively-harvest-water-from-air/)

宾夕法尼亚大学工程学院的研究人员发现了一种新型纳米结构材料，能够被动地从空气中收集水分。这种材料由亲水纳米孔和疏水聚合物混合而成，无需外部能量输入即可从空气中捕获水分并以液滴形式释放。这一发现是在进行另一项项目时偶然发生的。

与需要冷却或高湿度的传统集水方法不同，这种材料利用毛细凝聚作用，即使在较低湿度下也能将水蒸气吸入微小孔隙中。其独特之处在于，水不会滞留在孔隙中，而是以液滴的形式出现在表面，这与纳米多孔材料的典型行为相反。

研究小组发现，该材料实现了吸水和拒水成分之间的完美平衡，形成了一个反馈回路，其中水蒸气补充孔隙中的储水库，从而稳定了表面的液滴。这种现象最初似乎违反了物理规律，并得到了外部合作者的验证。

这种材料由常见的聚合物和纳米颗粒制成，具有简单且可扩展的特性，为各种应用提供了前景。潜在用途包括在干旱地区被动集水、冷却电子设备以及对湿度做出反应的智能涂层。未来的研究重点是优化材料的成分、扩大生产规模以及改善液滴释放。该团队旨在开发利用大气水蒸气在干燥气候下提供清洁用水和可持续冷却方法的技术。

---

## 2. 展示HN: PgDog – 无需扩展分片Postgres

**原文标题**: Show HN: PgDog – Shard Postgres without extensions

**原文链接**: [https://github.com/pgdogdev/pgdog](https://github.com/pgdogdev/pgdog)

PgDog：无需扩展即可分片PostgreSQL数据库的新型事务池管理器和逻辑复制管理器，采用Rust编写，旨在实现速度、安全性和可扩展性，能够管理数百个数据库和连接。

主要特性包括：

*   **负载均衡：** 应用层负载均衡，支持多种策略（轮询、最少连接等），并且能够将SELECT查询路由到副本，将其他查询路由到主库。
*   **健康检查与故障转移：** 基于数据库主机的实时健康状态自动重新路由查询。
*   **事务池：** 类似于PgBouncer，支持大量客户端的事务和会话池。
*   **分片：** 自动将查询路由到适当的分片，跨分片查询结果组装，以及自动拆分COPY命令以进行数据摄取。
*   **逻辑复制：** 在后台将数据拆分到数据库之间，而无需停机即可分片现有数据库。
*   **配置：** 高度可配置，提供PgBouncer/PgCat用户熟悉的选项。

本文提供了Kubernetes和Docker部署的快速入门指南，以及使用和配置示例。 它还详细介绍了如何在本地运行PgDog，从源代码构建它以及配置基本设置。

PgDog定位为一个早期项目，欢迎早期采用者。 性能是重点，利用Rust和Tokio，并提供基准测试。 该项目采用AGPL v3许可证，该许可证允许内部使用和私有修改，但如果PgDog作为公共服务提供，则需要共享修改。

---

## 3. 德国法院因柴油门丑闻判处大众高管入狱

**原文标题**: German court sends VW execs to prison over Dieselgate scandal

**原文链接**: [https://www.politico.eu/article/german-court-vw-execs-prison-dieselgate-scandal-volkswagen-environment-illegal-pollution/](https://www.politico.eu/article/german-court-vw-execs-prison-dieselgate-scandal-volkswagen-environment-illegal-pollution/)

柴油门丑闻：大众四名前高管因排放作弊欺诈罪被判刑。

---

## 4. Hacker News 现在运行于 Common Lisp 之上。

**原文标题**: Hacker News now runs on top of Common Lisp

**原文链接**: [https://lisp-journey.gitlab.io/blog/hacker-news-now-runs-on-top-of-common-lisp/](https://lisp-journey.gitlab.io/blog/hacker-news-now-runs-on-top-of-common-lisp/)

Hacker News (HN) 出于性能考虑，已从 Racket 迁移到 SBCL (一种 Common Lisp 实现)，特别是为了支持多核处理。这一转变由“dang”（HN 背后的关键人物）多年开发的 Arc 到 Common Lisp 编译器“Clarc”促成。此次迁移还恰逢移除了长评论线程的分页，表明性能容量有所提升。

迁移到 Clarc 是重构 HN 所使用的 Lisp 方言 Arc 的更大努力的一部分。该过程涉及创建分层 Arc 实现：arc0、arc1 和 arc2，其中 arc0 是唯一需要在底层系统（Racket、JavaScript 或 Common Lisp）中直接实现的部分。还有一个名为 Lilt 的 Arc 到 JavaScript 编译器。

虽然 Clarc 尚未公开发布，但 dang 表示它“差不多完成了”。保密的原因是 HN 代码库包含反滥用措施，如果暴露，这些措施将会受到损害。发布 Clarc 和其他替代 Arc 实现的计划已经制定，但这取决于分离这些敏感安全组件的能力。迁移到 SBCL 已经成功实施，并且悄无声息。

---

## 5. 使用 WebGPU 在浏览器中实现的粒子生命模拟

**原文标题**: Particle Life simulation in browser using WebGPU

**原文链接**: [https://lisyarus.github.io/blog/posts/particle-life-simulation-in-browser-using-webgpu.html](https://lisyarus.github.io/blog/posts/particle-life-simulation-in-browser-using-webgpu.html)

本文详细介绍了作者使用 WebGPU API 在 Web 浏览器中实现的“粒子生命”模拟。粒子生命是一种非物理的粒子模拟，其中不同类型粒子之间的力可以是不对称的，从而产生类似生命的涌现行为。

该模拟通过计算粒子之间的相互作用力和碰撞力来工作，这些力由粒子类型和定义的相互作用表决定。作者选择 WebGPU 而不是 OpenGL，是因为 WebGPU 具有更现代、更简洁的 API，并支持计算着色器和原子操作，这对于高效的模拟至关重要。

模拟循环包括计算力、更新粒子位置、应用边界条件和渲染。一个关键的优化是空间哈希/分箱，以减少 O(N^2) 的力计算复杂度。这涉及将模拟空间划分为箱子，并仅计算相邻箱子中粒子之间的力。

分箱过程使用计算着色器分三个阶段实现：使用原子操作计算每个箱子中的粒子数量，使用并行前缀和算法计算箱子偏移量，以及再次使用原子操作将粒子放置到新数组中相应的箱子中。这允许在 GPU 上高效计算粒子间力。在力计算之后，另一个计算着色器移动粒子并应用边界条件。

---

## 6. TeleMessage Explorer: 一款新的开源研究工具

**原文标题**: TeleMessage Explorer: a new open-source research tool

**原文链接**: [https://micahflee.com/telemessage-explorer-a-new-open-source-research-tool/](https://micahflee.com/telemessage-explorer-a-new-open-source-research-tool/)

本文介绍了TeleMessage Explorer，一个开源工具，用于分析从TeleMessage泄露的数据。TeleMessage是一家提供修改版Signal应用程序的公司。作者鼓励能够访问该数据集（通过DDoSecrets获取）的记者和研究人员使用该工具来挖掘有新闻价值的信息。

本文详细介绍了使用该工具的先决条件，包括Docker、Python、Poetry和充足的存储空间。它解释了从TeleMessage数据集中的堆转储文件中提取字符串的过程，这是工具正常运行的关键步骤。

TeleMessage Explorer由Python/Flask后端、TypeScript/Vue.js前端、PostgreSQL数据库（在Docker中运行）以及一个“cruncher”脚本组成，该脚本使用从提取的字符串中获取的相关JSON数据填充数据库。作者提供了设置和运行这些组件的说明。

本文通过截图展示了该工具的功能，演示了如何浏览群组、用户和消息，过滤数据以及下载附件。它还指出了OAuth2验证对象的存在，这些对象可用于识别TeleMessage客户。该工具允许搜索和过滤数据，显示消息的JSON对象，甚至可以下载嵌入在消息中的附件。

---

## 7. 今日我学到：Bash脚本中的超时

**原文标题**: TIL: timeout in Bash scripts

**原文链接**: [https://heitorpb.github.io/bla/timeout/](https://heitorpb.github.io/bla/timeout/)

本文探讨了在Bash脚本中使用`timeout`命令来防止无限循环，特别是在脚本需要等待服务可用时的场景。作者遇到了一个问题，即旨在检查Web服务器健康的`until`循环在服务器启动失败时无限期运行。

`timeout`命令提供了一种解决方案，它为给定的命令添加了一个时间限制；如果命令超过时间限制，`timeout`会发送一个信号（默认情况下为SIGTERM）来终止该命令，并以非零状态码退出。

然而，作者指出一个局限性：`timeout`不能直接与像`until`这样的shell内置命令一起使用，因为它们不是可终止的命令。为了规避这个问题，作者建议使用`bash -c`将`until`循环包装在一个单独的Bash进程中。或者，可以将`until`循环移动到一个单独的脚本中，然后进行超时处理。这种方法有效地限制了等待时间，防止脚本在目标服务启动失败时无限期挂起。文章强调了`timeout`在确保Bash脚本健壮性方面的作用。

---

## 8. Webhook 安全和 API 安全的双重标准

**原文标题**: The double standard of webhook security and API security

**原文链接**: [https://www.speakeasy.com/blog/webhook-security](https://www.speakeasy.com/blog/webhook-security)

Speakeasy文章：《Webhook安全与API安全的双重标准》强调了Webhook相对于API常常被忽视的漏洞，尽管它们都是现代软件集成的重要组成部分。虽然API在安全最佳实践方面受到高度关注，但Webhook经常被视为事后才考虑的问题，从而导致潜在风险。

该文章认为，这种差异源于一种误解：API被视为系统的“前门”，而Webhook被视为“后门”或通知系统。这导致Webhook的安全措施不够严格，即使它们可能被利用于恶意目的，例如数据泄露、未经授权的访问和拒绝服务攻击。

讨论的关键漏洞包括：

*   **缺乏适当的身份验证和授权：** Webhook通常缺乏足够的身份验证机制，使其容易受到欺骗和未经授权的数据访问。
*   **输入验证不足：** 对通过Webhook接收的数据验证不足，可能允许攻击者注入恶意代码并危害系统。
*   **缺少速率限制：** 缺少速率限制可能使攻击者能够通过大量Webhook请求淹没系统，从而导致拒绝服务。

该文章强调需要像对待API一样对待Webhook，保持同样的安全意识。它建议实施强大的身份验证、严格的输入验证、适当的速率限制和定期的安全审计，以降低与Webhook相关的风险。最终，该文章倡导对所有集成点采取一致的安全方法，无论它们是API还是Webhook。

---

## 9. 你和爱因斯坦、霍金、陶哲轩合住一间房子。

**原文标题**: You share a house with Einstein, Hawking and Tao

**原文链接**: [https://www.faisalabid.com/p/you-share-a-house-with-einstein-hawking](https://www.faisalabid.com/p/you-share-a-house-with-einstein-hawking)

这篇文章以幽默的笔触，想象了与阿尔伯特·爱因斯坦、斯蒂芬·霍金和陶哲轩合租公寓的情景，最初是寻求他们的深刻见解，但最终却利用他们的才智来完成诸如撰写电子邮件和格式化电子表格之类的琐碎任务。作者提议将他们的租金从20美元提高到200美元，以反映他们共同智慧的价值。高潮是将一项复杂的任务交给他们，要求他们运用先进的科学概念来制定策略，以对付偷包裹的邻居，突显了他们的能力与请求的琐碎之间的荒谬对比。

随后，文章转向了对社会对人工智能利用不足的更广泛评论。它认为，我们拥有强大的人工智能工具，堪比拥有可以随意支配的天才，但主要将它们用于诸如语法检查和撰写普通信息之类的微不足道的目的。作者感叹人工智能的潜力与其实际应用之间的差距，并建议虽然不是每个人都需要解决宇宙的奥秘，但我们应该努力提升我们的问题，并更好地利用这些强大的工具，而不是仅仅要求他们撰写更优美的电子邮件或格式化购物清单。文章以行动号召结束，敦促读者考虑他们今天可以向这些数字“爱因斯坦”提出什么要求，强调了动力与能力同等重要。

---

## 10. 从上游Git创建Debian软件包

**原文标题**: Creating Debian packages from upstream Git

**原文链接**: [https://optimizedbyotto.com/post/debian-packaging-from-git/](https://optimizedbyotto.com/post/debian-packaging-from-git/)

从上游 Git 仓库创建 Debian 软件包的详细指南：协作、溯源和安全最佳实践

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 2 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 3 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 4 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 5 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 6 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 7 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 8 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 9 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 10 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 11 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 12 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 13 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 14 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 15 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 16 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 17 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 18 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 19 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 20 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 21 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 22 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 23 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 24 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 25 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 26 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 27 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 28 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 29 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 30 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 31 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 32 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 33 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 34 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 35 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 36 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 37 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 38 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 39 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 40 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 41 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 42 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 43 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 44 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 45 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 46 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 47 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 48 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 49 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 50 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 51 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 52 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 53 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 54 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 55 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 56 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 57 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 58 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 59 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 60 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 61 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 62 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 63 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 64 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 65 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 66 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 67 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 68 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
