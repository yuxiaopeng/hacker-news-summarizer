# Hacker News 热门文章摘要 (2026-06-14)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. The only scalable delete in Postgres is DROP TABLE

**原文标题**: The only scalable delete in Postgres is DROP TABLE

**原文链接**: [https://planetscale.com/blog/the-only-scalable-delete](https://planetscale.com/blog/the-only-scalable-delete)

生成摘要时出错

---

## 12. Formal Methods and the Future of Programming

**原文标题**: Formal Methods and the Future of Programming

**原文链接**: [https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1)

生成摘要时出错

---

## 13. 全球丛枝菌根真菌网络的密度与生物量

**原文标题**: Global density and biomass of arbuscular mycorrhizal fungal networks

**原文链接**: [https://www.science.org/doi/10.1126/science.adu4373](https://www.science.org/doi/10.1126/science.adu4373)

生成摘要时出错

---

## 14. Show HN: Dual YOLOv8n UAV Detection on RK3588S at 42 FPS Using NPU

**原文标题**: Show HN: Dual YOLOv8n UAV Detection on RK3588S at 42 FPS Using NPU

**原文链接**: [https://github.com/alebal123bal/khadas_yolov8n_multithread](https://github.com/alebal123bal/khadas_yolov8n_multithread)

生成摘要时出错

---

## 15. Rio de Janeiro's city government model Rio3.5 beats Qwen3.7 in recent benchmarks

**原文标题**: Rio de Janeiro's city government model Rio3.5 beats Qwen3.7 in recent benchmarks

**原文链接**: [https://twitter.com/zenmagnets/status/2065796012820848699](https://twitter.com/zenmagnets/status/2065796012820848699)

生成摘要时出错

---

## 16. Show HN: 3D print Z reinforcement via injected loops

**原文标题**: Show HN: 3D print Z reinforcement via injected loops

**原文链接**: [https://mgunlogson.github.io/magma/](https://mgunlogson.github.io/magma/)

生成摘要时出错

---

## 17. Linux 7.1

**原文标题**: Linux 7.1

**原文链接**: [https://lore.kernel.org/lkml/CAHk-=wi4BF4bMhZNZ1tqs+FFV4OuZRe3ZqdWB+LxRLmRweUzQw@mail.gmail.com/T/#u](https://lore.kernel.org/lkml/CAHk-=wi4BF4bMhZNZ1tqs+FFV4OuZRe3ZqdWB+LxRLmRweUzQw@mail.gmail.com/T/#u)

生成摘要时出错

---

## 18. Quivers: A year of linear algebra by drawing arrows

**原文标题**: Quivers: A year of linear algebra by drawing arrows

**原文链接**: [https://lisyarus.github.io/blog/posts/quivers-a-year-of-linear-algebra-by-drawing-arrows.html](https://lisyarus.github.io/blog/posts/quivers-a-year-of-linear-algebra-by-drawing-arrows.html)

生成摘要时出错

---

## 19. How did Atari apply side art to Arcade Cabinets?

**原文标题**: How did Atari apply side art to Arcade Cabinets?

**原文链接**: [https://arcadeblogger.com/2026/06/14/how-did-atari-apply-side-art-to-arcade-cabinets/](https://arcadeblogger.com/2026/06/14/how-did-atari-apply-side-art-to-arcade-cabinets/)

生成摘要时出错

---

## 20. How to Earn a Billion Dollars

**原文标题**: How to Earn a Billion Dollars

**原文链接**: [https://paulgraham.com/earn.html](https://paulgraham.com/earn.html)

生成摘要时出错

---

## 21. USB Power Delivery: Plugging into the Benefits

**原文标题**: USB Power Delivery: Plugging into the Benefits

**原文链接**: [https://www.aptiv.com/en/insights/article/usb-power-delivery-plugging-into-the-benefits](https://www.aptiv.com/en/insights/article/usb-power-delivery-plugging-into-the-benefits)

生成摘要时出错

---

## 22. A 'cold blob' in the Atlantic could be a sign of AMOC shutdown

**原文标题**: A 'cold blob' in the Atlantic could be a sign of AMOC shutdown

**原文链接**: [https://www.cnn.com/2026/06/12/climate/cold-blob-atlantic-amoc-ocean-circulation](https://www.cnn.com/2026/06/12/climate/cold-blob-atlantic-amoc-ocean-circulation)

生成摘要时出错

---

## 23. A clear fishing wire is tied around the island of Manhattan

**原文标题**: A clear fishing wire is tied around the island of Manhattan

**原文链接**: [https://old.reddit.com/r/Damnthatsinteresting/comments/boea4v/a_clear_fishing_wire_is_tied_around_the_island_of/](https://old.reddit.com/r/Damnthatsinteresting/comments/boea4v/a_clear_fishing_wire_is_tied_around_the_island_of/)

生成摘要时出错

---

## 24. Free SQL→ER diagram tool, runs in the browser, nothing uploaded

**原文标题**: Free SQL→ER diagram tool, runs in the browser, nothing uploaded

**原文链接**: [https://sqltoerdiagram.com/](https://sqltoerdiagram.com/)

生成摘要时出错

---

## 25. Honda Civics and the Evil Valet

**原文标题**: Honda Civics and the Evil Valet

**原文链接**: [https://juniperspring.org/posts/honda-evil-valet/](https://juniperspring.org/posts/honda-evil-valet/)

生成摘要时出错

---

## 26. Dillo directory – Directory of useful sites that work reasonably well on Dillo

**原文标题**: Dillo directory – Directory of useful sites that work reasonably well on Dillo

**原文链接**: [https://dir.dillo-browser.org/](https://dir.dillo-browser.org/)

生成摘要时出错

---

## 27. KPMG pulls report on AI usage due to apparent hallucinations

**原文标题**: KPMG pulls report on AI usage due to apparent hallucinations

**原文链接**: [https://techcrunch.com/2026/06/13/kpmg-pulls-report-on-ai-usage-due-to-apparent-hallucinations/](https://techcrunch.com/2026/06/13/kpmg-pulls-report-on-ai-usage-due-to-apparent-hallucinations/)

生成摘要时出错

---

## 28. Extinction-Level Capitalism

**原文标题**: Extinction-Level Capitalism

**原文链接**: [https://matthewbutterick.com/extinction-level-capitalism.html](https://matthewbutterick.com/extinction-level-capitalism.html)

生成摘要时出错

---

## 29. Dangerous hormone-disrupting chemicals found in US breast milk samples

**原文标题**: Dangerous hormone-disrupting chemicals found in US breast milk samples

**原文链接**: [https://www.theguardian.com/us-news/2026/jun/14/breast-milk-research-chemicals](https://www.theguardian.com/us-news/2026/jun/14/breast-milk-research-chemicals)

生成摘要时出错

---

## 30. FreeOberon – Open-Source, Cross-Platform, Free Pascal/Turbo Pascal-Like Language

**原文标题**: FreeOberon – Open-Source, Cross-Platform, Free Pascal/Turbo Pascal-Like Language

**原文链接**: [https://github.com/kekcleader/FreeOberon](https://github.com/kekcleader/FreeOberon)

生成摘要时出错

---

## 31. Don't trust large context windows

**原文标题**: Don't trust large context windows

**原文链接**: [https://garrit.xyz/posts/2026-05-06-dont-trust-large-context-windows](https://garrit.xyz/posts/2026-05-06-dont-trust-large-context-windows)

生成摘要时出错

---

## 32. Tribblix: The retro Illumos distribution

**原文标题**: Tribblix: The retro Illumos distribution

**原文链接**: [http://tribblix.org/](http://tribblix.org/)

生成摘要时出错

---

## 33. Conversations with a six-year-old on functional programming (2018)

**原文标题**: Conversations with a six-year-old on functional programming (2018)

**原文链接**: [https://byorgey.wordpress.com/2018/05/06/conversations-with-a-six-year-old-on-functional-programming/](https://byorgey.wordpress.com/2018/05/06/conversations-with-a-six-year-old-on-functional-programming/)

生成摘要时出错

---

## 34. Pac-Man, but you're the ghost

**原文标题**: Pac-Man, but you're the ghost

**原文链接**: [https://garrit.xyz/posts/2026-06-13-pac-man-but-you-re-the-ghost](https://garrit.xyz/posts/2026-06-13-pac-man-but-you-re-the-ghost)

生成摘要时出错

---

## 35. Historic co-determination helps monasteries navigate digital change

**原文标题**: Historic co-determination helps monasteries navigate digital change

**原文链接**: [https://phys.org/news/2026-05-historic-monasteries-digital-countries.html](https://phys.org/news/2026-05-historic-monasteries-digital-countries.html)

生成摘要时出错

---

## 36. GLM 5.2 Is Out

**原文标题**: GLM 5.2 Is Out

**原文链接**: [https://twitter.com/jietang/status/2065784751345287314](https://twitter.com/jietang/status/2065784751345287314)

生成摘要时出错

---

## 37. Pyodide 314.0: Python packages can now publish WebAssembly wheels to PyPI

**原文标题**: Pyodide 314.0: Python packages can now publish WebAssembly wheels to PyPI

**原文链接**: [https://blog.pyodide.org/posts/314-release/](https://blog.pyodide.org/posts/314-release/)

生成摘要时出错

---

## 38. Python 3.14 garbage collection rigamarole

**原文标题**: Python 3.14 garbage collection rigamarole

**原文链接**: [https://theconsensus.dev/p/2026/06/06/python-3-14-garbage-collection-rigamarole.html](https://theconsensus.dev/p/2026/06/06/python-3-14-garbage-collection-rigamarole.html)

在 Python 3.14.0 中，开发团队将传统的世代垃圾回收器 (GC) 替换为一种新的增量式 GC。这一变化旨在通过将 Python 的三个分代合并为两个（新生代和老年代），并以增量方式而非一次性扫描老年代，从而减少大堆内存的最大停顿时间。

然而，这一改动转瞬即逝。由于有报告称“内存压力”（内存占用更高）增加，Python 团队在 3.14.5 版本中恢复了传统的世代 GC。作者 Phil Eaton 指出，由于该实现并未经过标准的 Python 增强提案 (PEP) 流程，因此引起了争议。此外，与 Java 或 Go 等语言不同，Python 的 GC 并非作为可切换选项实现的；一旦恢复，那些偏好增量回收器低延迟特性的用户就无法再使用它了。

文章提供了有关 Python 内存管理的技术背景，解释了 CPython 主要依靠**引用计数**在对象计数归零时立即释放内存。GC 的存在专门作为一种兜底机制，用于识别和清理引用计数无法解决的**引用循环**（循环引用）。

通过对比 Python 3.14.4（增量式）和 3.14.5（传统式），Eaton 展示了这两个系统处理内存的不同方式。虽然增量式 GC 成功缩减了停顿时间的“长尾”，但由此产生的内存占用增加对许多工作负载而言是不可接受的，最终导致其在稳定版中被移除。

---

## 39. Can't Stop the Signal. Poison It

**原文标题**: Can't Stop the Signal. Poison It

**原文链接**: [https://blog.digitalgrease.dev/posts/fauxx-cant-stop-the-signal](https://blog.digitalgrease.dev/posts/fauxx-cant-stop-the-signal)

生成摘要时出错

---

## 40. Noise infusion banned from statistical products published by Census Bureau

**原文标题**: Noise infusion banned from statistical products published by Census Bureau

**原文链接**: [https://desfontain.es/blog/banning-noise.html](https://desfontain.es/blog/banning-noise.html)

生成摘要时出错

---

## 41. GameBoy Workboy

**原文标题**: GameBoy Workboy

**原文链接**: [https://tcrf.net/Workboy](https://tcrf.net/Workboy)

生成摘要时出错

---

## 42. Every Frame Perfect

**原文标题**: Every Frame Perfect

**原文链接**: [https://tonsky.me/blog/every-frame-perfect/](https://tonsky.me/blog/every-frame-perfect/)

生成摘要时出错

---

## 43. Amazon CEO's talks with U.S. officials triggered crackdown on Anthropic models

**原文标题**: Amazon CEO's talks with U.S. officials triggered crackdown on Anthropic models

**原文链接**: [https://www.wsj.com/tech/ai/amazon-ceos-talks-with-u-s-officials-triggered-crackdown-on-anthropic-models-dcc90578?st=Yct6gx&reflink=desktopwebshare_permalink](https://www.wsj.com/tech/ai/amazon-ceos-talks-with-u-s-officials-triggered-crackdown-on-anthropic-models-dcc90578?st=Yct6gx&reflink=desktopwebshare_permalink)

生成摘要时出错

---

## 44. Phoenix LiveView 1.2

**原文标题**: Phoenix LiveView 1.2

**原文链接**: [https://phoenixframework.org/blog/phoenix-liveview-1-2-released](https://phoenixframework.org/blog/phoenix-liveview-1-2-released)

生成摘要时出错

---

## 45. Building a serial and VGA "everything console"

**原文标题**: Building a serial and VGA "everything console"

**原文链接**: [http://oldvcr.blogspot.com/2026/06/building-serial-and-vga-everything.html](http://oldvcr.blogspot.com/2026/06/building-serial-and-vga-everything.html)

生成摘要时出错

---

## 46. Making Claude a Chemist

**原文标题**: Making Claude a Chemist

**原文链接**: [https://www.anthropic.com/research/making-claude-a-chemist](https://www.anthropic.com/research/making-claude-a-chemist)

生成摘要时出错

---

## 47. Running DOS on Behringers DDX3216 with a DIY x86-Bios from Scratch

**原文标题**: Running DOS on Behringers DDX3216 with a DIY x86-Bios from Scratch

**原文链接**: [https://chrisdevblog.com/2026/06/08/running-dos-on-behringers-ddx3216-using-a-diy-x86-bios/](https://chrisdevblog.com/2026/06/08/running-dos-on-behringers-ddx3216-using-a-diy-x86-bios/)

生成摘要时出错

---

## 48. Appreciating Exif

**原文标题**: Appreciating Exif

**原文链接**: [https://brentfitzgerald.com/posts/appreciating-exif/](https://brentfitzgerald.com/posts/appreciating-exif/)

生成摘要时出错

---

## 49. Beagle: Git, URIs and all the dirty words

**原文标题**: Beagle: Git, URIs and all the dirty words

**原文链接**: [https://replicated.wiki/blog/uris.html](https://replicated.wiki/blog/uris.html)

生成摘要时出错

---

## 50. LaserWriter seeds

**原文标题**: LaserWriter seeds

**原文链接**: [https://inventingthefuture.ghost.io/laserwriter-seeds/](https://inventingthefuture.ghost.io/laserwriter-seeds/)

生成摘要时出错

---

## 51. Israeli firm BlackCore suspected of meddling in New York and Scotland votes

**原文标题**: Israeli firm BlackCore suspected of meddling in New York and Scotland votes

**原文链接**: [https://www.reuters.com/world/israeli-firm-blackcore-also-suspected-meddling-nyc-scotland-votes-french-2026-06-11/](https://www.reuters.com/world/israeli-firm-blackcore-also-suspected-meddling-nyc-scotland-votes-french-2026-06-11/)

生成摘要时出错

---

## 52. The adder at the heart of Intel's 8087 floating-point chip

**原文标题**: The adder at the heart of Intel's 8087 floating-point chip

**原文链接**: [https://www.righto.com/2026/06/intel-8087-adder-reverse-engineered.html](https://www.righto.com/2026/06/intel-8087-adder-reverse-engineered.html)

生成摘要时出错

---

## 53. Starmer to announce social media curfew and chatbot ban for teenagers

**原文标题**: Starmer to announce social media curfew and chatbot ban for teenagers

**原文链接**: [https://www.thetimes.com/uk/politics/article/social-media-ban-keir-starmer-qcmskxc5z](https://www.thetimes.com/uk/politics/article/social-media-ban-keir-starmer-qcmskxc5z)

生成摘要时出错

---

## 54. Arch Linux AUR Hit by Another Wave of Now More Sophisticated Malware Attack

**原文标题**: Arch Linux AUR Hit by Another Wave of Now More Sophisticated Malware Attack

**原文链接**: [https://www.phoronix.com/news/Arch-Linux-AUR-More-Malware](https://www.phoronix.com/news/Arch-Linux-AUR-More-Malware)

生成摘要时出错

---

## 55. New pancreatic cancer drug might open the door to much longer survival times

**原文标题**: New pancreatic cancer drug might open the door to much longer survival times

**原文链接**: [https://economist.com/science-and-technology/2026/06/12/treating-pancreatic-tumours-may-have-revealed-cancers-master-switch](https://economist.com/science-and-technology/2026/06/12/treating-pancreatic-tumours-may-have-revealed-cancers-master-switch)

生成摘要时出错

---

## 56. 30 years of OpenBSD development, visualized

**原文标题**: 30 years of OpenBSD development, visualized

**原文链接**: [https://www.visualsource.net/watch/94d078dd-2a47-40e5-aaca-20b69b5f6af2](https://www.visualsource.net/watch/94d078dd-2a47-40e5-aaca-20b69b5f6af2)

生成摘要时出错

---

## 57. UK set to announce social media ban for under-16s

**原文标题**: UK set to announce social media ban for under-16s

**原文链接**: [https://www.manchestereveningnews.co.uk/news/uk-news/uk-set-announce-social-media-34119132](https://www.manchestereveningnews.co.uk/news/uk-news/uk-set-announce-social-media-34119132)

生成摘要时出错

---

## 58. ReactOS (FOSS "Windows") achieves 3D-accelerated Half-Life on real hardware

**原文标题**: ReactOS (FOSS "Windows") achieves 3D-accelerated Half-Life on real hardware

**原文链接**: [https://www.phoronix.com/news/ReactOS-Running-Half-Life](https://www.phoronix.com/news/ReactOS-Running-Half-Life)

生成摘要时出错

---

## 59. Police officer investigated for using AI to 'create evidence' in multiple cases

**原文标题**: Police officer investigated for using AI to 'create evidence' in multiple cases

**原文链接**: [https://news.sky.com/story/derbyshire-police-officer-investigated-for-using-ai-to-create-evidence-in-multiple-cases-13553661](https://news.sky.com/story/derbyshire-police-officer-investigated-for-using-ai-to-create-evidence-in-multiple-cases-13553661)

生成摘要时出错

---

## 60. Orthodox C++ (2016)

**原文标题**: Orthodox C++ (2016)

**原文链接**: [https://bkaradzic.github.io/posts/orthodoxc++/](https://bkaradzic.github.io/posts/orthodoxc++/)

生成摘要时出错

---

## 61. Raress96/Dolby-Atmos-encoder: PoC Dolby Atmos encoder

**原文标题**: Raress96/Dolby-Atmos-encoder: PoC Dolby Atmos encoder

**原文链接**: [https://github.com/raress96/dolby-atmos-encoder](https://github.com/raress96/dolby-atmos-encoder)

生成摘要时出错

---

## 62. AI OSS tool repo goes archived over night after raising $7.3M Seed

**原文标题**: AI OSS tool repo goes archived over night after raising $7.3M Seed

**原文链接**: [https://github.com/tensorzero/tensorzero](https://github.com/tensorzero/tensorzero)

生成摘要时出错

---

## 63. The Story of PHP. Documentary Teaser [video]

**原文标题**: The Story of PHP. Documentary Teaser [video]

**原文链接**: [https://www.youtube.com/watch?v=4W4y46WVdCU](https://www.youtube.com/watch?v=4W4y46WVdCU)

生成摘要时出错

---

## 64. Rust 用户界面开发现状

**原文标题**: The state of building user interfaces in Rust

**原文链接**: [https://areweguiyet.com/#ecosystem](https://areweguiyet.com/#ecosystem)

生成摘要时出错

---

## 65. Show HN: I am building a map of people who lived in the Roman Empire

**原文标题**: Show HN: I am building a map of people who lived in the Roman Empire

**原文链接**: [https://new.roman-names.com/](https://new.roman-names.com/)

生成摘要时出错

---

## 66. Show HN: Paca – Lightweight Jira alternative for human-AI collaboration

**原文标题**: Show HN: Paca – Lightweight Jira alternative for human-AI collaboration

**原文链接**: [https://github.com/Paca-AI/paca](https://github.com/Paca-AI/paca)

生成摘要时出错

---

## 67. Automating myself out of development

**原文标题**: Automating myself out of development

**原文链接**: [https://www.thoughtfultechnologist.com/p/automating-myself-out-of-development](https://www.thoughtfultechnologist.com/p/automating-myself-out-of-development)

生成摘要时出错

---

## 68. CRISPR tech selectively shreds cancer cells, including "undruggable" cancers

**原文标题**: CRISPR tech selectively shreds cancer cells, including "undruggable" cancers

**原文链接**: [https://innovativegenomics.org/news/crispr-technique-selectively-shreds-cancer-cells/](https://innovativegenomics.org/news/crispr-technique-selectively-shreds-cancer-cells/)

生成摘要时出错

---

## 69. Amazon says its datacenters used about 2.5B gallons of water last year

**原文标题**: Amazon says its datacenters used about 2.5B gallons of water last year

**原文链接**: [https://www.theregister.com/on-prem/2026/06/12/amazon-owns-up-to-using-25bn-gallons-of-h2o-in-its-bit-barns-last-year/5254748](https://www.theregister.com/on-prem/2026/06/12/amazon-owns-up-to-using-25bn-gallons-of-h2o-in-its-bit-barns-last-year/5254748)

生成摘要时出错

---

## 70. Swiss voters rejected 10M population cap proposal

**原文标题**: Swiss voters rejected 10M population cap proposal

**原文链接**: [https://www.reuters.com/world/europe/switzerland-votes-proposal-cap-population-10-million-2026-06-14/](https://www.reuters.com/world/europe/switzerland-votes-proposal-cap-population-10-million-2026-06-14/)

生成摘要时出错

---

## 71. Codex for open source

**原文标题**: Codex for open source

**原文链接**: [https://openai.com/form/codex-for-oss/](https://openai.com/form/codex-for-oss/)

生成摘要时出错

---

## 72. Electric motors with no rare earths

**原文标题**: Electric motors with no rare earths

**原文链接**: [https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/](https://www.renaultgroup.com/en/magazine/energy-and-powertrains/all-about-electric-motors-with-no-rare-earths/)

生成摘要时出错

---

## 73. AI coding at home without going broke

**原文标题**: AI coding at home without going broke

**原文链接**: [https://stephen.bochinski.dev/blog/2026/06/13/ai-coding-at-home-without-going-broke/](https://stephen.bochinski.dev/blog/2026/06/13/ai-coding-at-home-without-going-broke/)

生成摘要时出错

---

## 74. Resurrecting a soaked, corroded, and damaged Commodore SX‑64 (2025)

**原文标题**: Resurrecting a soaked, corroded, and damaged Commodore SX‑64 (2025)

**原文链接**: [https://jerrylparker.com/blogs/posts/sx-64.html](https://jerrylparker.com/blogs/posts/sx-64.html)

生成摘要时出错

---

## 75. If you are asking for human attention, demonstrate human effort

**原文标题**: If you are asking for human attention, demonstrate human effort

**原文链接**: [https://tombedor.dev/human-attention-and-human-effort/](https://tombedor.dev/human-attention-and-human-effort/)

生成摘要时出错

---

## 76. A low-carbon computing platform from your retired phones

**原文标题**: A low-carbon computing platform from your retired phones

**原文链接**: [https://research.google/blog/a-low-carbon-computing-platform-from-your-retired-phones/](https://research.google/blog/a-low-carbon-computing-platform-from-your-retired-phones/)

生成摘要时出错

---

## 77. Ancient genome duplications laid the foundations of complex brains

**原文标题**: Ancient genome duplications laid the foundations of complex brains

**原文链接**: [https://www.ox.ac.uk/news/2026-06-09-ancient-genome-duplications-laid-the-foundations-of-complex-brains](https://www.ox.ac.uk/news/2026-06-09-ancient-genome-duplications-laid-the-foundations-of-complex-brains)

生成摘要时出错

---

## 78. Apt Encounters of the Third Kind (2021)

**原文标题**: Apt Encounters of the Third Kind (2021)

**原文链接**: [https://igor-blue.github.io/2021/03/24/apt1.html](https://igor-blue.github.io/2021/03/24/apt1.html)

生成摘要时出错

---

## 79. The Difference Between Rest and Idleness

**原文标题**: The Difference Between Rest and Idleness

**原文链接**: [https://idle.news/blog/on-the-difference-between-rest-and-idleness/](https://idle.news/blog/on-the-difference-between-rest-and-idleness/)

生成摘要时出错

---

## 80. Software Architecture Guide (2019)

**原文标题**: Software Architecture Guide (2019)

**原文链接**: [https://martinfowler.com/architecture/](https://martinfowler.com/architecture/)

生成摘要时出错

---

## 81. Launch HN: BitBoard (YC P25) – Analytics Workspace for Agents

**原文标题**: Launch HN: BitBoard (YC P25) – Analytics Workspace for Agents

**原文链接**: [https://bitboard.work/](https://bitboard.work/)

生成摘要时出错

---

## 82. A whale necropolis has been found

**原文标题**: A whale necropolis has been found

**原文链接**: [https://www.nature.com/articles/d41586-026-01581-x](https://www.nature.com/articles/d41586-026-01581-x)

生成摘要时出错

---

## 83. Windows 1.0 and the WinAPI, 40 Years Later

**原文标题**: Windows 1.0 and the WinAPI, 40 Years Later

**原文链接**: [https://medium.com/@stassaf.uae/windows-1-0-and-the-winapi-40-years-later-abaf64832918](https://medium.com/@stassaf.uae/windows-1-0-and-the-winapi-40-years-later-abaf64832918)

生成摘要时出错

---

## 84. Half-Life able to run on ReactOS

**原文标题**: Half-Life able to run on ReactOS

**原文链接**: [https://xcancel.com/reactos/status/2064839936059011207](https://xcancel.com/reactos/status/2064839936059011207)

生成摘要时出错

---

## 85. Hazel (YC W24) Is Hiring a Full Stack Engineer

**原文标题**: Hazel (YC W24) Is Hiring a Full Stack Engineer

**原文链接**: [https://www.ycombinator.com/companies/hazel-2/jobs/3epPWgu-full-stack-engineer-ts-sci](https://www.ycombinator.com/companies/hazel-2/jobs/3epPWgu-full-stack-engineer-ts-sci)

生成摘要时出错

---

## 86. Reinventing Control Theory One Feature at a Time: The Fallacy of Agentic Loops

**原文标题**: Reinventing Control Theory One Feature at a Time: The Fallacy of Agentic Loops

**原文链接**: [https://medium.com/agileinsider/reinventing-control-theory-one-feature-at-a-time-the-fallacy-of-agentic-loops-01dd533615de](https://medium.com/agileinsider/reinventing-control-theory-one-feature-at-a-time-the-fallacy-of-agentic-loops-01dd533615de)

生成摘要时出错

---

## 87. RTX 5080 and RTX 3090 Setup: 80 Tok/s on Qwen 3.6 27B Q8

**原文标题**: RTX 5080 and RTX 3090 Setup: 80 Tok/s on Qwen 3.6 27B Q8

**原文链接**: [https://imil.net/blog/posts/2026/rtx-5080-+-rtx-3090-setup-80+-tok-s-on-qwen-3.6-27b-q8/](https://imil.net/blog/posts/2026/rtx-5080-+-rtx-3090-setup-80+-tok-s-on-qwen-3.6-27b-q8/)

生成摘要时出错

---

## 88. Show HN: Bastion – isolated Linux VMs for background coding agents

**原文标题**: Show HN: Bastion – isolated Linux VMs for background coding agents

**原文链接**: [https://bastion.computer/](https://bastion.computer/)

生成摘要时出错

---

## 89. Human Routers of Machine Words

**原文标题**: Human Routers of Machine Words

**原文链接**: [https://borretti.me/article/human-routers-of-machine-words](https://borretti.me/article/human-routers-of-machine-words)

生成摘要时出错

---

## 90. The Neat Little Vehicles That Run a Cemetery

**原文标题**: The Neat Little Vehicles That Run a Cemetery

**原文链接**: [https://www.thedrive.com/news/meet-the-neat-little-vehicles-that-run-a-cemetery](https://www.thedrive.com/news/meet-the-neat-little-vehicles-that-run-a-cemetery)

生成摘要时出错

---

## 91. The experience of rendering Arabic typography and its technical debt

**原文标题**: The experience of rendering Arabic typography and its technical debt

**原文链接**: [https://lr0.org/blog/p/arabic/](https://lr0.org/blog/p/arabic/)

生成摘要时出错

---

## 92. Weave: Merging based on language structure and not lines

**原文标题**: Weave: Merging based on language structure and not lines

**原文链接**: [https://ataraxy-labs.github.io/weave/](https://ataraxy-labs.github.io/weave/)

生成摘要时出错

---

## 93. (Re//Verse 2026) Taxonomy and Deobfuscation of a Real World Binary Obfuscator [pdf]

**原文标题**: (Re//Verse 2026) Taxonomy and Deobfuscation of a Real World Binary Obfuscator [pdf]

**原文链接**: [https://github.com/AnalogCyberNuke/RE-Verse-2026-Slides/blob/main/Reverse26.pdf](https://github.com/AnalogCyberNuke/RE-Verse-2026-Slides/blob/main/Reverse26.pdf)

生成摘要时出错

---

## 94. Leaving Mozilla

**原文标题**: Leaving Mozilla

**原文链接**: [https://blog.unitedheroes.net/5751](https://blog.unitedheroes.net/5751)

生成摘要时出错

---

## 95. Arch Linux Now Believes Malware Incident Under Control: More Than 1,500 Packages

**原文标题**: Arch Linux Now Believes Malware Incident Under Control: More Than 1,500 Packages

**原文链接**: [https://www.phoronix.com/news/Arch-Linux-AUR-More-Than-1500](https://www.phoronix.com/news/Arch-Linux-AUR-More-Than-1500)

生成摘要时出错

---

## 96. An Interview with Intel's Kira Boyko: Xeon 6's Product Director

**原文标题**: An Interview with Intel's Kira Boyko: Xeon 6's Product Director

**原文链接**: [https://chipsandcheese.com/p/an-interview-with-intels-kira-boyko](https://chipsandcheese.com/p/an-interview-with-intels-kira-boyko)

生成摘要时出错

---

## 97. Show HN: Öcha – A minimalist, Kindle-style RSS and newsletter reader

**原文标题**: Show HN: Öcha – A minimalist, Kindle-style RSS and newsletter reader

**原文链接**: [https://readocha.com/](https://readocha.com/)

生成摘要时出错

---

## 98. Statement on US government directive to suspend access to Fable 5 and Mythos 5

**原文标题**: Statement on US government directive to suspend access to Fable 5 and Mythos 5

**原文链接**: [https://www.anthropic.com/news/fable-mythos-access](https://www.anthropic.com/news/fable-mythos-access)

生成摘要时出错

---

## 99. Sealed Super Mario Bros Sells for $3M Setting New Record for a Video Game

**原文标题**: Sealed Super Mario Bros Sells for $3M Setting New Record for a Video Game

**原文链接**: [https://www.ha.com/heritage-auctions-press-releases-and-news/highest-graded-super-mario-bros.-sells-for-record-3-million-at-heritage-auctions.s?releaseId=5484](https://www.ha.com/heritage-auctions-press-releases-and-news/highest-graded-super-mario-bros.-sells-for-record-3-million-at-heritage-auctions.s?releaseId=5484)

生成摘要时出错

---

## 100. Measles surge in Utah sparks fears US could undo decades of progress

**原文标题**: Measles surge in Utah sparks fears US could undo decades of progress

**原文链接**: [https://www.dailymail.com/news/article-15897903/measles-surge-utah-US-elimination-status.html](https://www.dailymail.com/news/article-15897903/measles-surge-utah-US-elimination-status.html)

生成摘要时出错

---

