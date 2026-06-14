# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-14.md)

*最后自动更新时间: 2026-06-14 18:40:51*
## 1. 里约热内卢“本土研发”的大语言模型似乎是现有模型的合并版。

**原文标题**: Rio de Janeiro's "homegrown" LLM appears to be a merge of an existing model

**原文链接**: [https://github.com/nex-agi/Nex-N2/issues/4](https://github.com/nex-agi/Nex-N2/issues/4)

Nex-AGI 的 GitHub 仓库发布了一项指控，称里约热内卢的“自研”AI 模型 Rio-3.5-Open-397B 并非 IplanRIO 的原创成果。证据显示，该模型实际上是两个现有模型的直接逐元素合并（element-wise merge）：Nex-N2_pro（占 60%）和 Qwen3.5-397B-A17B（占 40%）。

报告提供了两项主要证据来支持这一指控：

1.  **行为识别**：当移除模型硬编码的“你是 Rio”系统提示词后，它在 79% 的情况下会自称为“来自 Nex-AGI 的 Nex”，且从未自称为“Rio”。据称，它还能逐字背诵 Nex-AGI 专有的组织背景故事。
2.  **权重分析**：技术分析显示，Rio 模型全部 60 层中的每一个权重张量都是 Nex 和 Qwen 模型精确到 0.6/0.4 的数学融合。报告指出，这种特定的插值在统计学上是不可能通过独立训练或标准微调实现的。

指控者总结道，尽管该模型被标榜为本地技术成就，但没有证据表明 IplanRIO 进行了任何原创训练。他们认为该模型只是简单的权重合并，而非“自研”开发。

---

## 2. Show HN: Kage – 将任意网站镜像为单个二进制文件，以便离线查看

**原文标题**: Show HN: Kage – Shadow any website to a single binary for offline viewing

**原文链接**: [https://github.com/tamnd/kage](https://github.com/tamnd/kage)

**Kage**（影）是一款开源的 Go 语言工具，旨在将网站“影子化”为无脚本、自包含的文件，以便永久离线查看。与传统的“另存为”方法（常因缺少 JavaScript 或外部依赖而失效）不同，Kage 能确保网页在未来数年内依然保持可用性和私密性。

**工作原理**
Kage 使用无头 Chrome 浏览器完整渲染网页，随后对最终的 DOM 进行快照。接着，它会剥离所有 JavaScript（从而移除追踪和网络调用），并将所有资源（CSS、字体和图像）本地化。这一过程创建了一个干净、静态的网站版本，其外观与原版完全一致，但不运行任何代码。

**核心特性**
*   **礼貌抓取**：执行广度优先爬取，遵循 `robots.txt` 协议，并支持站点地图（sitemap）。
*   **幂等性**：支持续传中断的爬取任务，并能“刷新”现有的镜像，而无需重新下载未变更的内容。
*   **灵活的输出形式**：镜像可以存储为标准目录，或“打包”为两种不同的格式：
    1.  **ZIM 归档**：一种压缩的行业标准格式，兼容 Kiwix 生态系统（Android、iOS、桌面端）。
    2.  **自包含二进制文件**：一个集成了网站内容和内置服务器的单体可执行文件，无需安装任何软件即可查看内容。
*   **原生界面**：虽然默认通过浏览器查看，但可以使用 `webview` 标签进行编译，以便在专用的类应用窗口中打开镜像。

**用法**
Kage 提供预编译二进制文件、Docker 镜像（内置 Chromium）或通过 `go install` 安装。它采用 MIT 许可证，非常适合研究人员、档案保管员或任何需要可靠离线访问网页文档和文章的用户。

---

## 3. 劈柴模拟器

**原文标题**: Firewood Splitting Simulator

**原文链接**: [https://screen.toys/firewood/](https://screen.toys/firewood/)

**Firewood Splitting Simulator** is a minimalist, browser-based interactive experience created by the developer **shapiro500**. Part of a collection referred to as "screen toys," the simulator provides a simple, tactile digital activity designed for quick entertainment or stress relief.

The application features a 3D interface where users can interact with virtual logs. The core mechanics are straightforward:
*   **Navigation:** Users can drag their cursor to rotate the view, allowing them to inspect the wood from different angles.
*   **Action:** A simple click triggers the splitting mechanic, simulating the physical act of breaking firewood.

Rather than a complex game with levels or scores, this "screen toy" focuses on the satisfaction of the interaction itself, offering a meditative and uncomplicated simulation of a manual task.

---

## 4. JavaScript的诞生与消亡 (2014)

**原文标题**: The Birth and Death of JavaScript (2014)

**原文链接**: [https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript)

生成摘要时出错

---

## 5. zeroserve 兼容 Caddy：吞吐量提升 3 倍，延迟降低 70%

**原文标题**: Caddy compatibility for zeroserve: 3x throughput and 70% lower latency

**原文链接**: [https://su3.io/posts/zeroserve-caddy-compat](https://su3.io/posts/zeroserve-caddy-compat)

本文介绍了 zeroserve 对 Caddy 的全新兼容支持。zeroserve 是一款在用户态执行 eBPF 脚本的高性能 HTTPS 服务器。

通过将 Caddyfile 即时编译（JIT）为原生 x86_64 或 ARM64 机器码，并运行在 `io_uring` 事件循环中，zeroserve 实现了远高于标准 Caddy 配置的效率。其核心亮点包括：

*   **卓越的性能：** 在 HTTPS 反向代理基准测试中，zeroserve 的**吞吐量是 Caddy 的 3 倍**（约 39,000 req/s 对比 12,500 req/s），且 **p50 延迟降低了 70%**（1.45ms 对比 4.74ms）。其性能与 Nginx 相当，甚至在某些场景下表现更佳。
*   **低资源开销：** zeroserve 保持了极小的内存占用，其峰值 RSS（常驻内存集）使用量显著低于 Caddy。
*   **可扩展性：** 由于 zeroserve 运行图灵完备的 eBPF，用户可以直接从 Caddyfile 调用自定义原生代码插件。本文展示了如何利用 eBPF 中间件来处理 S3 兼容反向代理的 AWS SigV4 身份验证。
*   **易于使用：** 现有的 Caddy 用户只需在运行二进制文件时使用 `--caddy` 参数指向其当前配置文件，即可切换到 zeroserve。

本质上，zeroserve 为那些既需要 Nginx 级性能或特定 eBPF 逻辑，又希望保留熟悉 Caddyfile 语法的用户提供了一个高速替代方案。

---

## 6. Perlisisms

**原文标题**: Perlisisms

**原文链接**: [https://www.cs.yale.edu/homes/perlis-alan/quotes.html](https://www.cs.yale.edu/homes/perlis-alan/quotes.html)

生成摘要时出错

---

## 7. 瑞士选民否决将人口上限设定为一千万的提案。

**原文标题**: Swiss voters reject proposal to cap population at ten million

**原文链接**: [https://www.swissinfo.ch/eng/swiss-politics/swiss-voters-reject-proposal-to-cap-population-at-ten-million/91548146](https://www.swissinfo.ch/eng/swiss-politics/swiss-voters-reject-proposal-to-cap-population-at-ten-million/91548146)

根据所提供的标题，以下是关于瑞士人口上限投票新闻的简要摘要：

**摘要：瑞士选民否决 1000 万人口上限提案**

瑞士选民果断否决了一项将该国人口限制在 1000 万以内的提案。这项由右翼瑞士人民党 (SVP) 发起的“可持续发展倡议”旨在通过限制移民，防止该国人口在 2050 年之前突破 1000 万大关。

**核心要点：**
*   **提案内容：** 瑞士人民党认为，由移民推动的人口快速增长给国家基础设施带来了压力，推高了住房成本并破坏了环境。该倡议要求，如果人口达到 950 万，政府必须采取限制性措施（例如退出有关人员自由流动的国际协议）。
*   **经济担忧：** 包括瑞士政府、工会和商界领袖在内的反对者认为，设定人口上限无异于“经济自杀”。他们坚称，瑞士严重依赖外国劳动力来填补医疗、科技和建筑等关键领域的短缺。
*   **欧盟关系：** 批评者还警告称，终止人员自由流动将危及与瑞士最大贸易伙伴欧盟签署的双边协议。
*   **投票结果：** 该提案被约 63% 的选民否决。这一结果表明，尽管移民仍是一个敏感的政治话题，但大多数瑞士选民认为经济稳定和国际合作比严格的人口限制更为重要。

*（注：您提供的提示中关于苏丹无国界医生组织的正文内容似乎是另一篇文章的“阅读更多”链接，与瑞士人口投票无关。）*

---

## 8. No, everyone is not using AI for everything

**原文标题**: No, everyone is not using AI for everything

**原文链接**: [https://gabrielweinberg.com/p/people-are-consuming-ai-like-they](https://gabrielweinberg.com/p/people-are-consuming-ai-like-they)

In the article **"No, everyone is not using AI for everything,"** author Gabriel Weinberg (yegg) challenges the prevailing media narrative that generative AI has reached universal adoption. Citing data from 2025 and 2026, Weinberg argues that AI usage is actually split into three roughly equal groups: one-third use it actively, one-third use it occasionally, and one-third do not use it at all.

The author highlights several key findings to debunk the "omnipresence" myth:
*   **Stalled Growth:** Even among Gen Z, adoption has plateaued. Microsoft data shows only about 30% of the U.S. working-age population engages with AI for more than 90 minutes per month.
*   **Rising Negativity:** Public sentiment is shifting; Gallup reports a significant year-over-year increase in "anger" toward AI.
*   **Barriers to Use:** Adoption is hindered by legitimate concerns regarding job displacement (42%), privacy violations (35%), and the spread of misinformation (33%). Many users also remain skeptical of AI's actual value compared to foundational tech like the internet or smartphones.

Weinberg uses a **meat consumption analogy** to explain these behaviors: just as people choose to be carnivores, "reducetarians," or vegans for ethical and health reasons, they are now choosing their level of "AI consumption" based on privacy and social concerns. 

The article concludes that businesses and policymakers must stop treating AI adoption as a binary "all or nothing" trend. Instead, they should cater to the "continuum of use" by offering choices—such as DuckDuckGo’s private AI features or opt-out settings—to respect the large segment of the population that is currently holding back. Overcoming this stagnation will require significant improvements in both product utility and safety regulation.

---

## 9. Lisp's Influence on Ruby

**原文标题**: Lisp's Influence on Ruby

**原文链接**: [https://blog.tacoda.dev/lisps-influence-on-ruby-6a54f1a7740e](https://blog.tacoda.dev/lisps-influence-on-ruby-6a54f1a7740e)

生成摘要时出错

---

## 10. FarOutCompany

**原文标题**: FarOutCompany

**原文链接**: [https://faroutcompany.com/](https://faroutcompany.com/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 2 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 3 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 4 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 5 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 6 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 7 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 8 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 9 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 10 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 11 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 12 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 13 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 14 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 15 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 16 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 17 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 18 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 19 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 20 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 21 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 22 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 23 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 24 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 25 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 26 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 27 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 28 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 29 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 30 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 31 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 32 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 33 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 34 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 35 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 36 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 37 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 38 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 39 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 40 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 41 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 42 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 43 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 44 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 45 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 46 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 47 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 48 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 49 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 50 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 51 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 52 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 53 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 54 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 55 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 56 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 57 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 58 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 59 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 60 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 61 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 62 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 63 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 64 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 65 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 66 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 67 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 68 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 69 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 70 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 71 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 72 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 73 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 74 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 75 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 76 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 77 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 78 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 79 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 80 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 81 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 82 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 83 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 84 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 85 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 86 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 87 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 88 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 89 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 90 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 91 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 92 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 93 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 94 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 95 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 96 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 97 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 98 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 99 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 100 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 101 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 102 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 103 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 104 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 105 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 106 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 107 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 108 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 109 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 110 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 111 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 112 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 113 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 114 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 115 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 116 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 117 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 118 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 119 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 120 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 121 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 122 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 123 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 124 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 125 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 126 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 127 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 128 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 129 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 130 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 131 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 132 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 133 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 134 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 135 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 136 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 137 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 138 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 139 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 140 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 141 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 142 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 143 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 144 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 145 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 146 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 147 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 148 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 149 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 150 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 151 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 152 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 153 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 154 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 155 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 156 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 157 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 158 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 159 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 160 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 161 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 162 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 163 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 164 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 165 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 166 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 167 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 168 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 169 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 170 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 171 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 172 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 173 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 174 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 175 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 176 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 177 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 178 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 179 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 180 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 181 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 182 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 183 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 184 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 185 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 186 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 187 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 188 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 189 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 190 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 191 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 192 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 193 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 194 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 195 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 196 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 197 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 198 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 199 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 200 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 201 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 202 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 203 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 204 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 205 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 206 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 207 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 208 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 209 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 210 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 211 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 212 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 213 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 214 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 215 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 216 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 217 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 218 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 219 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 220 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 221 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 222 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 223 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 224 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 225 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 226 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 227 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 228 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 229 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 230 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 231 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 232 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 233 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 234 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 235 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 236 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 237 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 238 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 239 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 240 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 241 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 242 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 243 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 244 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 245 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 246 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 247 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 248 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 249 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 250 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 251 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 252 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 253 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 254 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 255 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 256 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 257 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 258 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 259 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 260 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 261 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 262 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 263 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 264 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 265 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 266 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 267 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 268 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 269 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 270 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 271 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 272 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 273 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 274 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 275 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 276 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 277 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 278 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 279 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 280 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 281 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 282 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 283 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 284 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 285 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 286 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 287 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 288 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 289 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 290 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 291 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 292 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 293 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 294 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 295 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 296 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 297 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 298 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 299 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 300 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 301 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 302 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 303 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 304 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 305 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 306 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 307 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 308 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 309 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 310 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 311 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 312 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 313 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 314 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 315 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 316 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 317 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 318 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 319 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 320 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 321 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 322 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 323 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 324 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 325 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 326 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 327 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 328 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 329 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 330 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 331 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 332 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 333 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 334 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 335 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 336 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 337 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 338 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 339 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 340 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 341 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 342 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 343 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 344 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 345 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 346 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 347 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 348 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 349 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 350 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 351 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 352 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 353 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 354 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 355 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 356 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 357 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 358 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 359 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 360 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 361 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 362 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 363 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 364 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 365 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 366 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 367 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 368 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 369 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 370 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 371 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 372 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 373 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 374 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 375 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 376 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 377 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 378 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 379 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 380 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 381 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 382 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 383 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 384 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 385 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 386 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 387 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 388 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 389 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 390 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 391 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 392 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 393 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 394 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 395 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 396 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 397 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 398 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 399 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 400 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 401 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 402 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 403 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 404 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 405 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 406 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 407 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 408 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 409 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 410 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 411 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 412 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 413 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 414 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 415 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 416 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 417 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 418 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 419 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 420 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 421 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 422 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 423 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 424 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 425 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 426 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 427 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 428 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 429 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 430 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 431 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 432 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 433 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 434 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 435 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 436 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 437 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 438 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 439 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 440 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 441 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 442 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 443 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 444 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 445 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 446 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 447 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 448 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 449 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 450 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 451 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
