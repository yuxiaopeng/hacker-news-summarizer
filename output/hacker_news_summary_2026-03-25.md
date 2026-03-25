# Hacker News 热门文章摘要 (2026-03-25)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我在电影《挽救计划》中的天文摄影

**原文标题**: My Astrophotography in the Movie Project Hail Mary

**原文链接**: [https://rpastro.square.site/s/stories/phm](https://rpastro.square.site/s/stories/phm)

根据提供的内容，简要总结如下：

**Rod Prazeres** 宣布，他的天文摄影作品将出现在电影版《挽救计划》（Project Hail Mary）中。具体而言，他的天文影像已被选中用于该片的**片尾字幕序列**。此次合作凸显了专业真实的天文摄影在增强这部根据安迪·威尔小说改编的重磅科幻电影视觉呈现方面的应用。

---

## 2. Ente 的本地 LLM 应用

**原文标题**: Local LLM App by Ente

**原文链接**: [https://ente.com/blog/ensu/](https://ente.com/blog/ensu/)

Ente 宣布推出 Ensu，这是一款全新的离线、开源大语言模型 (LLM) 应用。该项目源于一种信念，即人工智能技术至关重要，不应仅由“科技巨头”掌控，并对隐私泄露、监控风险以及中心化依赖的风险表示了担忧。

Ensu 的功能类似于 ChatGPT，但完全在设备本地运行，从而确保了绝对隐私和零成本使用。虽然 Ente 承认本地模型目前在原始性能上仍落后于前沿模型，但他们认为这些模型正跨越一个“能力阈值”，足以胜任大多数任务——例如私人反思、文学讨论，或在没有网络连接的旅途中使用。

**核心技术细节：**
*   **跨平台：** 支持 iOS、Android、macOS、Linux、Windows 及网页端。
*   **架构：** 核心逻辑采用 Rust 编写，移动端利用原生包装器，桌面端则使用 Tauri。
*   **开源：** 代码已公开，履行了 Ente 对透明度的承诺。
*   **安全性：** 虽然端到端加密 (E2EE) 同步和备份功能已开发完成，但为了根据初始用户反馈灵活调整架构，这些功能在首个版本中暂时禁用。

**未来方向：**
Ensu 目前属于 “Ente Labs” 项目。开发者正在探索多个方向，包括将该应用发展为记录笔记的“第二大脑”、实用型 Android 启动器，或是具备长期记忆的个人智能体。团队正积极寻求社区反馈，以规划产品路线图。

---

## 3. 关于慢他妈下来的思考

**原文标题**: Thoughts on Slowing the Fuck Down

**原文链接**: [https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/](https://mariozechner.at/posts/2026-03-25-thoughts-on-slowing-the-fuck-down/)

《关于“彻底慢下来”的思考》一文批判了当前业界对高速度、代理式（agentic）AI 编程的痴迷。在反思了一整年的“进展”后，作者认为，将完整项目委托给自主代理已导致软件质量下降，具体表现为代码脆弱、UI 故障以及无法挽回的技术债。

作者强调了人类开发者与 AI 开发者之间的本质区别：人类充当了天然的“瓶颈”。因为人类能感受到错误带来的“痛苦”，且产出能力有限，所以最终会选择学习和重构。相比之下，代理缺乏这种学习闭环，能瞬间“倾泻出”数千行代码。这导致微小的错误（即“小瑕疵”）以不可持续的速度累积，在开发者意识到之前，就已经制造出了一个“代码库怪兽”。

此外，作者指出，“代理式搜索”存在**低召回率**的问题。代理通常只做局部决策，缺乏对系统的全局理解，导致大量的代码重复和“习得性复杂”。过去大型人类组织需要数年才能搞砸的事情，现在一个小团队利用代理在短短几周内就能将其摧毁。

为了防止这场“狂热之梦”演变成噩梦，作者提出了一套更严谨的方法：
*   **在限定任务中使用代理：** 将“乏味的琐事”或非关键工具交给代理，但人类必须作为最终的质量把关者。
*   **人工架构设计：** 亲手编写核心 API 和架构，以保持系统的“整体感”并确保深刻理解。
*   **慢下来：** 为 AI 生成的代码量设置限制，使其与你彻底审查代码的能力相匹配。
*   **拥抱摩擦：** 意识到编写代码时的阻力，正是让开发者能够学习并保持自主性的关键。

最终，作者认为，保持人类的自主性和纪律是构建“激发喜悦而非产出垃圾”的软件的唯一途径。

---

## 4. 陪审团认定 Meta 为牟利蓄意伤害儿童，做出里程碑式裁决。

**原文标题**: Jury says Meta knowingly harmed children for profit, awarding landmark verdict

**原文链接**: [https://www.latimes.com/business/story/2026-03-25/jury-says-meta-knowingly-harmed-children-for-profit-awarding-landmark-verdict](https://www.latimes.com/business/story/2026-03-25/jury-says-meta-knowingly-harmed-children-for-profit-awarding-landmark-verdict)

新墨西哥州的一个陪审团对 Meta 作出了一项具有里程碑意义的裁决，认定该公司明知其平台（包括 Instagram 和 Facebook）损害儿童心理健康并隐瞒儿童性剥削证据，应承担法律责任。

陪审团认定，Meta 将利润置于安全之上，并通过利用未成年人弱点的“违背良知”的贸易行为违反了该州的《不公平行为法》。因此，Meta 被勒令支付 3.75 亿美元的罚金——即针对所认定的数千项违规行为，按每项 5000 美元的最高标准处罚。

这场为期七周的审判依据了内部通信、举报人证词以及一项卧底调查，调查中特工伪装成儿童并记录了性诱导行为。检察官成功辩称，Meta 的算法旨在以牺牲儿童安全为代价来最大化用户参与度，同时在平台风险方面误导了公众。

虽然这一裁决标志着 Meta 在法律上的重大挫败，但该公司股价在消息传出后有所上涨。一名发言人确认了上诉计划，并坚称公司正努力保护青少年。

此案是日益高涨的诉讼浪潮中的“分水岭时刻”，目前已有 40 多个州的州总检察长提起类似诉讼，指控社交媒体功能具有刻意诱导成瘾的特性。新墨西哥州审判的第二阶段将于 5 月进行，届时法官将裁定 Meta 的平台是否构成“公共滋扰”，以及该公司是否必须资助公共项目以治理所造成的危害。

---

## 5. Meta和YouTube在具有里程碑意义的社交媒体成瘾案中被判定有过失

**原文标题**: Meta and YouTube Found Negligent in Landmark Social Media Addiction Case

**原文链接**: [https://www.nytimes.com/2026/03/25/technology/social-media-trial-verdict.html](https://www.nytimes.com/2026/03/25/technology/social-media-trial-verdict.html)

无法访问文章链接。

---

## 6. TurboQuant：以极致压缩重新定义 AI 效率

**原文标题**: TurboQuant: Redefining AI efficiency with extreme compression

**原文链接**: [https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/)

Google Research 推出了 TurboQuant，这是一套具有理论支撑的量化算法，旨在大幅压缩大语言模型 (LLM) 和向量搜索引擎中使用的高维向量。

TurboQuant 的主要目标是消除传统量化中的“内存开销”——传统方法通常需要存储额外的常数，这往往会抵消压缩带来的收益。它通过以下两项核心创新实现了这一目标：

*   **PolarQuant：** 该方法将笛卡尔坐标转换为极坐标系（半径和角度）。由于这些角度的几何结构是可预测的，该模型避免了传统“方形”网格量化所需的昂贵数据归一化和常数存储。
*   **量化 Johnson-Lindenstrauss (QJL)：** 这种“1 比特技巧”利用数学变换在缩小数据规模的同时保留关键关系。它充当纠错阶段，仅使用一个符号位来消除偏差，并保持注意力评分的高准确性。

**关键结果与影响：**
*   **效率：** 在使用 Gemma 和 Mistral 等模型的测试中，TurboQuant 将键值 (KV) 缓存内存减少了 6 倍，并在 H100 GPU 上实现了高达 8 倍的注意力逻辑值 (attention logits) 计算加速。
*   **准确性：** 该系统在实现这些提升的同时保持了零精度损失和接近最优的失真率，性能优于 PQ 和 RabbiQ 等现有基准。
*   **通用性：** TurboQuant 具有“数据无关性” (data-oblivious)，这意味着它无需特定数据集调优或模型微调即可高效工作。

通过解决 KV 缓存瓶颈，TurboQuant 使大语言模型能够更高效地处理更长的上下文。除大语言模型外，该技术预计将变革 Google 的大规模语义搜索，从而以极低的内存需求在数十亿个向量中实现更快速、更准确的检索。

---

## 7. Antimatter has been transported for the first time

**原文标题**: Antimatter has been transported for the first time

**原文链接**: [https://www.nature.com/articles/d41586-026-00950-w](https://www.nature.com/articles/d41586-026-00950-w)

欧洲核子研究中心（CERN）的科学家们首次成功运输反物质，实现了历史性的里程碑。3月24日，一支研究团队将92个反质子装载于卡车后部的特制“瓶子”中进行移动。该车辆在日内瓦附近的CERN场区行驶了超过8公里，最高时速达到42公里。

反物质因其在与普通物质接触时会瞬间湮灭并完全转化为能量，而极其难以存储和移动。为了克服这一难题，研究团队利用一种特殊的陷阱，通过磁场使粒子悬浮，从而防止它们触碰容器壁。

此次实验的主要目标是将反质子从其诞生的“反物质工厂”转移到不受实验噪声干扰、更安静的环境中。移动这些粒子使物理学家能够进行比目前在生产现场更高精度的测量。

该项目由杜塞尔多夫海因里希·海涅大学的研究人员领导，实现了科学界数十年来的夙愿。CERN目前是世界上唯一能够生产可用数量反质子的机构。这一技术突破为探究宇宙的基本奥秘（如大爆炸后物质与反物质之间不明原因的差异）提供了新方法。参与该项目的物理学家称此次成功运输为“技术奇迹”，为粒子物理研究开启了新的大门。

---

## 8. Show HN: I built a site that maps the web from a bounty hunter's perspective

**原文标题**: Show HN: I built a site that maps the web from a bounty hunter's perspective

**原文链接**: [https://www.neobotnet.com/](https://www.neobotnet.com/)

**Neobotnet** is a specialized web reconnaissance platform designed specifically for bug bounty hunters and cybersecurity researchers. Launched as a "Show HN" project, the site aims to map the internet from an adversarial perspective, providing a comprehensive view of an organization's digital footprint.

The core purpose of Neobotnet is to streamline the reconnaissance phase of security testing. It functions as a powerful search engine and discovery tool that aggregates data on subdomains, IP addresses, open ports, and underlying technologies. By continuously scanning and indexing the web, the platform allows users to visualize a target's attack surface and identify potential vulnerabilities that might be missed by standard search engines.

**Key features include:**
*   **Subdomain Discovery:** Identifying hidden or forgotten subdomains belonging to a target organization.
*   **Technology Profiling:** Mapping the specific software, frameworks, and services running on various servers.
*   **Asset Tracking:** Monitoring changes in an organization’s infrastructure over time to spot newly exposed risks.
*   **Advanced Filtering:** Allowing researchers to narrow down results by specific criteria, such as geographic location, hosting provider, or port status.

The project emphasizes scale and automation, seeking to provide security professionals with the data necessary to find "low-hanging fruit" and complex misconfigurations. By centralizing infrastructure data, Neobotnet helps bounty hunters more efficiently map out perimeters and uncover security gaps before they can be exploited by malicious actors.

---

## 9. Goodbye to Sora

**原文标题**: Goodbye to Sora

**原文链接**: [https://twitter.com/soraofficialapp/status/2036532795984715896](https://twitter.com/soraofficialapp/status/2036532795984715896)

The provided text does not contain the content of an article titled "Goodbye to Sora." Instead, it is a **technical error message from the social media platform X (formerly Twitter)**.

The main points of the provided text are:
*   **Access Issue:** The website detected that JavaScript is disabled in the user's browser.
*   **Requirement:** To view the content on x.com, the user must enable JavaScript or switch to a supported browser.
*   **Support Links:** The page provides links to the Help Center, Terms of Service, Privacy Policy, and Cookie Policy for further assistance.

Because the actual article content was blocked by these browser settings, it is impossible to summarize the "Goodbye to Sora" story based on this text. To get a summary, please provide the full text of the article itself.

---

## 10. VitruvianOS – Desktop Linux Inspired by the BeOS

**原文标题**: VitruvianOS – Desktop Linux Inspired by the BeOS

**原文链接**: [https://v-os.dev](https://v-os.dev)

生成摘要时出错

---

## 11. Looking at Unity made me understand the point of C++ coroutines

**原文标题**: Looking at Unity made me understand the point of C++ coroutines

**原文链接**: [https://mropert.github.io/2026/03/20/unity_cpp_coroutines/](https://mropert.github.io/2026/03/20/unity_cpp_coroutines/)

生成摘要时出错

---

## 12. Sony V. Cox Decision Reversed

**原文标题**: Sony V. Cox Decision Reversed

**原文链接**: [https://supreme.justia.com/cases/federal/us/607/24-171/](https://supreme.justia.com/cases/federal/us/607/24-171/)

生成摘要时出错

---

## 13. Flighty Airports

**原文标题**: Flighty Airports

**原文链接**: [https://flighty.com/airports](https://flighty.com/airports)

生成摘要时出错

---

## 14. Building a coding agent in Swift from scratch

**原文标题**: Building a coding agent in Swift from scratch

**原文链接**: [https://github.com/ivan-magda/swift-claude-code](https://github.com/ivan-magda/swift-claude-code)

This article introduces **swift-claude-code**, a 9-part learning series by Ivan Magda that explores the architecture of coding agents by rebuilding a Claude Code-style CLI in Swift. 

The project is driven by the hypothesis that effective coding agents are defined by **architectural restraint** rather than complexity. Magda argues that a small set of high-quality tools combined with thin orchestration—trusting the LLM to do the heavy lifting—outperforms large, complex frameworks. 

**Key Architectural Principles:**
*   **Minimalist Tools:** A focus on a few robust tools (shell execution, file editing) rather than a vast catalog.
*   **The Invariant Loop:** A consistent "while true" loop that handles user queries, manages tool calls, and processes results.
*   **Task State & Context:** Using explicit task tracking and "context compaction" to maintain reliability and efficiency without overwhelming the model’s memory.

**Roadmap and Tech Stack:**
The project is divided into two phases. **Phase 1** establishes the core loop and basic tool dispatch (bash, file I/O). **Phase 2** introduces advanced "product mechanics" like subagents, skill loading, and actor-based background tasks. 

Technically, the project utilizes **Swift 6.2** with strict concurrency, **AsyncHTTPClient** for cross-platform support (macOS and Linux), and the **Anthropic Messages API**. The author emphasizes that this is a staged educational exploration rather than a production-ready IDE tool or a general-purpose framework. By isolating specific mechanisms at each stage, the project demonstrates how little architecture is actually required to build a functional and effective coding assistant.

---

## 15. Tell HN: Litellm 1.82.7 and 1.82.8 on PyPI are compromised

**原文标题**: Tell HN: Litellm 1.82.7 and 1.82.8 on PyPI are compromised

**原文链接**: [https://github.com/BerriAI/litellm/issues/24512](https://github.com/BerriAI/litellm/issues/24512)

生成摘要时出错

---

## 16. Show HN: I took back Video.js after 16 years and we rewrote it to be 88% smaller

**原文标题**: Show HN: I took back Video.js after 16 years and we rewrote it to be 88% smaller

**原文链接**: [https://videojs.org/blog/videojs-v10-beta-hello-world-again](https://videojs.org/blog/videojs-v10-beta-hello-world-again)

生成摘要时出错

---

## 17. Slovenian officials blame Israeli firm Black Cube for trying to manipulate vote

**原文标题**: Slovenian officials blame Israeli firm Black Cube for trying to manipulate vote

**原文链接**: [https://www.wsj.com/world/europe/spies-lies-and-fake-investors-in-disguise-how-plotters-tried-to-flip-a-european-election-1f42b39a](https://www.wsj.com/world/europe/spies-lies-and-fake-investors-in-disguise-how-plotters-tried-to-flip-a-european-election-1f42b39a)

生成摘要时出错

---

## 18. Musketeer d'Artagnan's remains believed found under Dutch church

**原文标题**: Musketeer d'Artagnan's remains believed found under Dutch church

**原文链接**: [https://www.bbc.co.uk/news/articles/cm2rew2dgzzo](https://www.bbc.co.uk/news/articles/cm2rew2dgzzo)

生成摘要时出错

---

## 19. Miscellanea: The War in Iran

**原文标题**: Miscellanea: The War in Iran

**原文链接**: [https://acoup.blog/2026/03/25/miscellanea-the-war-in-iran/](https://acoup.blog/2026/03/25/miscellanea-the-war-in-iran/)

生成摘要时出错

---

## 20. Data centers are transitioning from AC to DC

**原文标题**: Data centers are transitioning from AC to DC

**原文链接**: [https://spectrum.ieee.org/data-center-dc](https://spectrum.ieee.org/data-center-dc)

生成摘要时出错

---

## 21. Quantization from the Ground Up

**原文标题**: Quantization from the Ground Up

**原文链接**: [https://ngrok.com/blog/quantization](https://ngrok.com/blog/quantization)

生成摘要时出错

---

## 22. VNDB founder Yorhel has died

**原文标题**: VNDB founder Yorhel has died

**原文链接**: [https://vndb.org/t24787](https://vndb.org/t24787)

生成摘要时出错

---

## 23. Apple Business

**原文标题**: Apple Business

**原文链接**: [https://www.apple.com/newsroom/2026/03/introducing-apple-business-a-new-all-in-one-platform-for-businesses-of-all-sizes/](https://www.apple.com/newsroom/2026/03/introducing-apple-business-a-new-all-in-one-platform-for-businesses-of-all-sizes/)

生成摘要时出错

---

## 24. Supreme Court Sides with Cox in Copyright Fight over Pirated Music

**原文标题**: Supreme Court Sides with Cox in Copyright Fight over Pirated Music

**原文链接**: [https://www.nytimes.com/2026/03/25/us/politics/supreme-court-cox-music-copyright.html](https://www.nytimes.com/2026/03/25/us/politics/supreme-court-cox-music-copyright.html)

生成摘要时出错

---

## 25. I wanted to build vertical SaaS for pest control, so I took a technician job

**原文标题**: I wanted to build vertical SaaS for pest control, so I took a technician job

**原文链接**: [https://www.onhand.pro/p/i-wanted-to-build-vertical-saas-for-pest-control-i-took-a-technician-job-instead](https://www.onhand.pro/p/i-wanted-to-build-vertical-saas-for-pest-control-i-took-a-technician-job-instead)

生成摘要时出错

---

## 26. Hubble Snaps a New Dazzling Photo of the Crab Nebula

**原文标题**: Hubble Snaps a New Dazzling Photo of the Crab Nebula

**原文链接**: [https://nautil.us/hubble-snaps-a-new-dazzling-photo-of-the-crab-nebula-1279203](https://nautil.us/hubble-snaps-a-new-dazzling-photo-of-the-crab-nebula-1279203)

生成摘要时出错

---

## 27. Arm AGI CPU

**原文标题**: Arm AGI CPU

**原文链接**: [https://newsroom.arm.com/blog/introducing-arm-agi-cpu](https://newsroom.arm.com/blog/introducing-arm-agi-cpu)

生成摘要时出错

---

## 28. Tracy Kidder, Author of 'The Soul of a New Machine,' Dies at 80

**原文标题**: Tracy Kidder, Author of 'The Soul of a New Machine,' Dies at 80

**原文链接**: [https://www.nytimes.com/2026/03/25/books/tracy-kidder-dead.html](https://www.nytimes.com/2026/03/25/books/tracy-kidder-dead.html)

生成摘要时出错

---

## 29. Microbenchmarking Chipsets for Giggles

**原文标题**: Microbenchmarking Chipsets for Giggles

**原文链接**: [https://chipsandcheese.com/p/microbenchmarking-chipsets-for-giggles](https://chipsandcheese.com/p/microbenchmarking-chipsets-for-giggles)

生成摘要时出错

---

## 30. Meta and Google found liable in social media addiction trial

**原文标题**: Meta and Google found liable in social media addiction trial

**原文链接**: [https://www.bbc.co.uk/news/articles/c747x7gz249o](https://www.bbc.co.uk/news/articles/c747x7gz249o)

生成摘要时出错

---

## 31. Algorithm Visualizer

**原文标题**: Algorithm Visualizer

**原文链接**: [https://algorithm-visualizer.org/](https://algorithm-visualizer.org/)

生成摘要时出错

---

## 32. The Last Testaments of Richard II and Henry IV

**原文标题**: The Last Testaments of Richard II and Henry IV

**原文链接**: [https://www.historytoday.com/archive/feature/last-testaments-richard-ii-and-henry-iv](https://www.historytoday.com/archive/feature/last-testaments-richard-ii-and-henry-iv)

生成摘要时出错

---

## 33. Meta told to pay $375M for misleading users over child safety

**原文标题**: Meta told to pay $375M for misleading users over child safety

**原文链接**: [https://www.bbc.com/news/articles/cql75dn07n2o](https://www.bbc.com/news/articles/cql75dn07n2o)

生成摘要时出错

---

## 34. Show HN: Email.md – Markdown to responsive, email-safe HTML

**原文标题**: Show HN: Email.md – Markdown to responsive, email-safe HTML

**原文链接**: [https://www.emailmd.dev/](https://www.emailmd.dev/)

生成摘要时出错

---

## 35. Why I forked httpx

**原文标题**: Why I forked httpx

**原文链接**: [https://tildeweb.nl/~michiel/httpxyz.html](https://tildeweb.nl/~michiel/httpxyz.html)

生成摘要时出错

---

## 36. Wine 11 rewrites how Linux runs Windows games at kernel with massive speed gains

**原文标题**: Wine 11 rewrites how Linux runs Windows games at kernel with massive speed gains

**原文链接**: [https://www.xda-developers.com/wine-11-rewrites-linux-runs-windows-games-speed-gains/](https://www.xda-developers.com/wine-11-rewrites-linux-runs-windows-games-speed-gains/)

生成摘要时出错

---

## 37. Show HN: Gemini can now natively embed video, so I built sub-second video search

**原文标题**: Show HN: Gemini can now natively embed video, so I built sub-second video search

**原文链接**: [https://github.com/ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch)

生成摘要时出错

---

## 38. Fun with CSF firmware (RK3588 GPU firmware)

**原文标题**: Fun with CSF firmware (RK3588 GPU firmware)

**原文链接**: [https://icecream95.gitlab.io/fun-with-csf-firmware.html](https://icecream95.gitlab.io/fun-with-csf-firmware.html)

生成摘要时出错

---

## 39. Show HN: DuckDB community extension for prefiltered HNSW using ACORN-1

**原文标题**: Show HN: DuckDB community extension for prefiltered HNSW using ACORN-1

**原文链接**: [https://github.com/cigrainger/duckdb-hnsw-acorn](https://github.com/cigrainger/duckdb-hnsw-acorn)

生成摘要时出错

---

## 40. Hypothesis, Antithesis, synthesis

**原文标题**: Hypothesis, Antithesis, synthesis

**原文链接**: [https://antithesis.com/blog/2026/hegel/](https://antithesis.com/blog/2026/hegel/)

生成摘要时出错

---

## 41. Ubuntu wants to strip some of GRUB features in 26.10 for security purposes

**原文标题**: Ubuntu wants to strip some of GRUB features in 26.10 for security purposes

**原文链接**: [https://discourse.ubuntu.com/t/streamlining-secure-boot-for-26-10/79069](https://discourse.ubuntu.com/t/streamlining-secure-boot-for-26-10/79069)

生成摘要时出错

---

## 42. A Compiler Writing Journey

**原文标题**: A Compiler Writing Journey

**原文链接**: [https://github.com/DoctorWkt/acwj](https://github.com/DoctorWkt/acwj)

生成摘要时出错

---

## 43. Missile defense is NP-complete

**原文标题**: Missile defense is NP-complete

**原文链接**: [https://smu160.github.io/posts/missile-defense-is-np-complete/](https://smu160.github.io/posts/missile-defense-is-np-complete/)

生成摘要时出错

---

## 44. Lago (YC S21) Is Hiring Product Engineers (Growth Team)

**原文标题**: Lago (YC S21) Is Hiring Product Engineers (Growth Team)

**原文链接**: [https://getlago.notion.site/Lago-Product-Engineer-AI-Agents-for-Growth-327ef63110d280cdb030ccf429d3e4d7?source=copy_link](https://getlago.notion.site/Lago-Product-Engineer-AI-Agents-for-Growth-327ef63110d280cdb030ccf429d3e4d7?source=copy_link)

生成摘要时出错

---

## 45. Apple Can Create Smaller On-Device AI Models from Google's Gemini

**原文标题**: Apple Can Create Smaller On-Device AI Models from Google's Gemini

**原文链接**: [https://www.macrumors.com/2026/03/25/apple-google-gemini-distill-models/](https://www.macrumors.com/2026/03/25/apple-google-gemini-distill-models/)

生成摘要时出错

---

## 46. Hypura – A storage-tier-aware LLM inference scheduler for Apple Silicon

**原文标题**: Hypura – A storage-tier-aware LLM inference scheduler for Apple Silicon

**原文链接**: [https://github.com/t8/hypura](https://github.com/t8/hypura)

生成摘要时出错

---

## 47. You can run a DNS server (2025)

**原文标题**: You can run a DNS server (2025)

**原文链接**: [https://simonsafar.com/2025/running_dns/](https://simonsafar.com/2025/running_dns/)

生成摘要时出错

---

## 48. Apple Just Lost Me

**原文标题**: Apple Just Lost Me

**原文链接**: [https://andregarzia.com/2026/03/apple-just-lost-me.html](https://andregarzia.com/2026/03/apple-just-lost-me.html)

生成摘要时出错

---

## 49. Nanobrew: The fastest macOS package manager compatible with brew

**原文标题**: Nanobrew: The fastest macOS package manager compatible with brew

**原文链接**: [https://nanobrew.trilok.ai/](https://nanobrew.trilok.ai/)

生成摘要时出错

---

## 50. How the world’s first electric grid was built

**原文标题**: How the world’s first electric grid was built

**原文链接**: [https://worksinprogress.co/issue/how-the-worlds-first-electric-grid-was-built/](https://worksinprogress.co/issue/how-the-worlds-first-electric-grid-was-built/)

生成摘要时出错

---

## 51. Show HN: AI Roundtable – Let 200 models debate your question

**原文标题**: Show HN: AI Roundtable – Let 200 models debate your question

**原文链接**: [https://opper.ai/ai-roundtable/](https://opper.ai/ai-roundtable/)

生成摘要时出错

---

## 52. What happened to GEM?

**原文标题**: What happened to GEM?

**原文链接**: [https://dfarq.homeip.net/whatever-happened-to-gem/](https://dfarq.homeip.net/whatever-happened-to-gem/)

生成摘要时出错

---

## 53. An Aural Companion for Decades, CBS News Radio Crackles to a Close

**原文标题**: An Aural Companion for Decades, CBS News Radio Crackles to a Close

**原文链接**: [https://www.nytimes.com/2026/03/21/business/media/cbs-news-radio-appraisal.html](https://www.nytimes.com/2026/03/21/business/media/cbs-news-radio-appraisal.html)

生成摘要时出错

---

## 54. Box of Secrets: Discreetly modding an apartment intercom to work with Apple Home

**原文标题**: Box of Secrets: Discreetly modding an apartment intercom to work with Apple Home

**原文链接**: [https://www.jackhogan.me/blog/box-of-secrets/](https://www.jackhogan.me/blog/box-of-secrets/)

生成摘要时出错

---

## 55. Overcoming the friendship recession

**原文标题**: Overcoming the friendship recession

**原文链接**: [https://joeprevite.com/friendship-recession/](https://joeprevite.com/friendship-recession/)

生成摘要时出错

---

## 56. Debunking Zswap and Zram Myths

**原文标题**: Debunking Zswap and Zram Myths

**原文链接**: [https://chrisdown.name/2026/03/24/zswap-vs-zram-when-to-use-what.html](https://chrisdown.name/2026/03/24/zswap-vs-zram-when-to-use-what.html)

生成摘要时出错

---

## 57. Intel Device Modeling Language for virtual platforms

**原文标题**: Intel Device Modeling Language for virtual platforms

**原文链接**: [https://github.com/intel/device-modeling-language](https://github.com/intel/device-modeling-language)

生成摘要时出错

---

## 58. Show HN: ProofShot – Give AI coding agents eyes to verify the UI they build

**原文标题**: Show HN: ProofShot – Give AI coding agents eyes to verify the UI they build

**原文链接**: [https://github.com/AmElmo/proofshot](https://github.com/AmElmo/proofshot)

生成摘要时出错

---

## 59. A Eulogy for Vim

**原文标题**: A Eulogy for Vim

**原文链接**: [https://drewdevault.com/2026/03/25/2026-03-25-Forking-vim.html](https://drewdevault.com/2026/03/25/2026-03-25-Forking-vim.html)

生成摘要时出错

---

## 60. Microsoft's "fix" for Windows 11

**原文标题**: Microsoft's "fix" for Windows 11

**原文链接**: [https://www.sambent.com/microsofts-plan-to-fix-windows-11-is-gaslighting/](https://www.sambent.com/microsofts-plan-to-fix-windows-11-is-gaslighting/)

生成摘要时出错

---

## 61. Microsoft's "fix" for Windows 11

**原文标题**: Microsoft's "fix" for Windows 11

**原文链接**: [https://www.sambent.com/microsofts-plan-to-fix-windows-11-is-gaslighting/](https://www.sambent.com/microsofts-plan-to-fix-windows-11-is-gaslighting/)

生成摘要时出错

---

## 62. Data Manipulation in Clojure Compared to R and Python

**原文标题**: Data Manipulation in Clojure Compared to R and Python

**原文链接**: [https://codewithkira.com/2024-07-18-tablecloth-dplyr-pandas-polars.html](https://codewithkira.com/2024-07-18-tablecloth-dplyr-pandas-polars.html)

生成摘要时出错

---

## 63. No Terms. No Conditions

**原文标题**: No Terms. No Conditions

**原文链接**: [https://notermsnoconditions.com](https://notermsnoconditions.com)

生成摘要时出错

---

## 64. curl > /dev/sda: How I made a Linux distro that runs wget | dd

**原文标题**: curl > /dev/sda: How I made a Linux distro that runs wget | dd

**原文链接**: [https://astrid.tech/2026/03/24/0/curl-to-dev-sda/](https://astrid.tech/2026/03/24/0/curl-to-dev-sda/)

生成摘要时出错

---

## 65. Scientists Discover Protein That Turns Brown Fat into a Calorie-Burning Machine

**原文标题**: Scientists Discover Protein That Turns Brown Fat into a Calorie-Burning Machine

**原文链接**: [https://scitechdaily.com/scientists-discover-protein-that-turns-brown-fat-into-a-calorie-burning-machine/](https://scitechdaily.com/scientists-discover-protein-that-turns-brown-fat-into-a-calorie-burning-machine/)

生成摘要时出错

---

## 66. Log File Viewer for the Terminal

**原文标题**: Log File Viewer for the Terminal

**原文链接**: [https://lnav.org/](https://lnav.org/)

生成摘要时出错

---

## 67. Fiber optic cables reveal a serious problem at the heart of modern farming

**原文标题**: Fiber optic cables reveal a serious problem at the heart of modern farming

**原文链接**: [https://grist.org/drought/fiber-optic-cables-reveal-a-serious-problem-at-the-heart-of-modern-farming/](https://grist.org/drought/fiber-optic-cables-reveal-a-serious-problem-at-the-heart-of-modern-farming/)

生成摘要时出错

---

## 68. Epic Games to cut more than 1k jobs as Fortnite usage falls

**原文标题**: Epic Games to cut more than 1k jobs as Fortnite usage falls

**原文链接**: [https://www.reuters.com/legal/litigation/epic-games-said-tuesday-that-it-will-lay-off-more-than-1000-employees-2026-03-24/](https://www.reuters.com/legal/litigation/epic-games-said-tuesday-that-it-will-lay-off-more-than-1000-employees-2026-03-24/)

生成摘要时出错

---

## 69. ARM AGI CPU: Specs and SKUs

**原文标题**: ARM AGI CPU: Specs and SKUs

**原文链接**: [https://sbcwiki.com/docs/soc-manufacturers/arm/arm-silicon/](https://sbcwiki.com/docs/soc-manufacturers/arm/arm-silicon/)

生成摘要时出错

---

## 70. LaGuardia pilots raised safety alarms months before deadly runway crash

**原文标题**: LaGuardia pilots raised safety alarms months before deadly runway crash

**原文链接**: [https://www.theguardian.com/us-news/2026/mar/24/laguardia-airplane-pilots-safety-concerns-crash](https://www.theguardian.com/us-news/2026/mar/24/laguardia-airplane-pilots-safety-concerns-crash)

生成摘要时出错

---

## 71. Mystery jump in oil trading ahead of Trump post draws scrutiny

**原文标题**: Mystery jump in oil trading ahead of Trump post draws scrutiny

**原文链接**: [https://www.bbc.com/news/articles/cg547ljepvzo](https://www.bbc.com/news/articles/cg547ljepvzo)

生成摘要时出错

---

## 72. Opera: Rewind The Web to 1996 (Opera at 30)

**原文标题**: Opera: Rewind The Web to 1996 (Opera at 30)

**原文链接**: [https://www.web-rewind.com](https://www.web-rewind.com)

生成摘要时出错

---

## 73. 'Tiny Shortcuts' Are Poisoning Science

**原文标题**: 'Tiny Shortcuts' Are Poisoning Science

**原文链接**: [https://nautil.us/how-tiny-shortcuts-are-poisoning-science-1279176](https://nautil.us/how-tiny-shortcuts-are-poisoning-science-1279176)

生成摘要时出错

---

## 74. Epoch confirms GPT5.4 Pro solved a frontier math open problem

**原文标题**: Epoch confirms GPT5.4 Pro solved a frontier math open problem

**原文链接**: [https://epoch.ai/frontiermath/open-problems/ramsey-hypergraphs](https://epoch.ai/frontiermath/open-problems/ramsey-hypergraphs)

生成摘要时出错

---

## 75. So where are all the AI apps?

**原文标题**: So where are all the AI apps?

**原文链接**: [https://www.answer.ai/posts/2026-03-12-so-where-are-all-the-ai-apps.html](https://www.answer.ai/posts/2026-03-12-so-where-are-all-the-ai-apps.html)

生成摘要时出错

---

## 76. Is anybody else bored of talking about AI?

**原文标题**: Is anybody else bored of talking about AI?

**原文链接**: [https://blog.jakesaunders.dev/is-anybody-else-bored-of-talking-about-ai/](https://blog.jakesaunders.dev/is-anybody-else-bored-of-talking-about-ai/)

生成摘要时出错

---

## 77. Welcome to FastMCP

**原文标题**: Welcome to FastMCP

**原文链接**: [https://gofastmcp.com/getting-started/welcome](https://gofastmcp.com/getting-started/welcome)

生成摘要时出错

---

## 78. Show HN: Gridland: make terminal apps that also run in the browser

**原文标题**: Show HN: Gridland: make terminal apps that also run in the browser

**原文链接**: [https://www.gridland.io/](https://www.gridland.io/)

生成摘要时出错

---

## 79. I quit editing photos

**原文标题**: I quit editing photos

**原文链接**: [https://jamesbaker.uk/i-quit-editing-photos/](https://jamesbaker.uk/i-quit-editing-photos/)

生成摘要时出错

---

## 80. LLM Neuroanatomy II: Modern LLM Hacking and Hints of a Universal Language?

**原文标题**: LLM Neuroanatomy II: Modern LLM Hacking and Hints of a Universal Language?

**原文链接**: [https://dnhkng.github.io/posts/rys-ii/](https://dnhkng.github.io/posts/rys-ii/)

生成摘要时出错

---

## 81. The final switch: Goldsboro, 1961 (2013)

**原文标题**: The final switch: Goldsboro, 1961 (2013)

**原文链接**: [https://blog.nuclearsecrecy.com/2013/09/27/final-switch-goldsboro-1961/](https://blog.nuclearsecrecy.com/2013/09/27/final-switch-goldsboro-1961/)

生成摘要时出错

---

## 82. Testing the Swift C compatibility with Raylib (+WASM)

**原文标题**: Testing the Swift C compatibility with Raylib (+WASM)

**原文链接**: [https://carette.xyz/posts/swift_c_compatibility_with_raylib/](https://carette.xyz/posts/swift_c_compatibility_with_raylib/)

生成摘要时出错

---

## 83. Secure Domain Name System (DNS) Deployment 2026 Guide [pdf]

**原文标题**: Secure Domain Name System (DNS) Deployment 2026 Guide [pdf]

**原文链接**: [https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-81r3.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-81r3.pdf)

生成摘要时出错

---

## 84. WolfGuard: WireGuard with FIPS 140-3 cryptography

**原文标题**: WolfGuard: WireGuard with FIPS 140-3 cryptography

**原文链接**: [https://github.com/wolfssl/wolfguard](https://github.com/wolfssl/wolfguard)

生成摘要时出错

---

## 85. Dune3d: A parametric 3D CAD application

**原文标题**: Dune3d: A parametric 3D CAD application

**原文链接**: [https://github.com/dune3d/dune3d](https://github.com/dune3d/dune3d)

生成摘要时出错

---

## 86. Why So Many Control Rooms Were Seafoam Green (2025)

**原文标题**: Why So Many Control Rooms Were Seafoam Green (2025)

**原文链接**: [https://bethmathews.substack.com/p/why-so-many-control-rooms-were-seafoam](https://bethmathews.substack.com/p/why-so-many-control-rooms-were-seafoam)

生成摘要时出错

---

## 87. Implementing automatic eSIM installation on Android

**原文标题**: Implementing automatic eSIM installation on Android

**原文链接**: [https://medium.com/proandroiddev/integration-of-automatic-esim-installation-on-android-6c5f6d7124cb](https://medium.com/proandroiddev/integration-of-automatic-esim-installation-on-android-6c5f6d7124cb)

生成摘要时出错

---

## 88. FCC updates covered list to include foreign-made consumer routers

**原文标题**: FCC updates covered list to include foreign-made consumer routers

**原文链接**: [https://www.fcc.gov/document/fcc-updates-covered-list-include-foreign-made-consumer-routers](https://www.fcc.gov/document/fcc-updates-covered-list-include-foreign-made-consumer-routers)

生成摘要时出错

---

## 89. Claude Code Cheat Sheet

**原文标题**: Claude Code Cheat Sheet

**原文链接**: [https://cc.storyfox.cz](https://cc.storyfox.cz)

生成摘要时出错

---

## 90. Ripgrep is faster than grep, ag, git grep, ucg, pt, sift (2016)

**原文标题**: Ripgrep is faster than grep, ag, git grep, ucg, pt, sift (2016)

**原文链接**: [https://burntsushi.net/ripgrep/](https://burntsushi.net/ripgrep/)

生成摘要时出错

---

## 91. io_uring, libaio performance across Linux kernels and an unexpected IOMMU trap

**原文标题**: io_uring, libaio performance across Linux kernels and an unexpected IOMMU trap

**原文链接**: [https://blog.ydb.tech/how-io-uring-overtook-libaio-performance-across-linux-kernels-and-an-unexpected-iommu-trap-ea6126d9ef14](https://blog.ydb.tech/how-io-uring-overtook-libaio-performance-across-linux-kernels-and-an-unexpected-iommu-trap-ea6126d9ef14)

生成摘要时出错

---

## 92. MSA: Memory Sparse Attention

**原文标题**: MSA: Memory Sparse Attention

**原文链接**: [https://github.com/EverMind-AI/MSA](https://github.com/EverMind-AI/MSA)

生成摘要时出错

---

## 93. Show HN: Cq – Stack Overflow for AI coding agents

**原文标题**: Show HN: Cq – Stack Overflow for AI coding agents

**原文链接**: [https://blog.mozilla.ai/cq-stack-overflow-for-agents/](https://blog.mozilla.ai/cq-stack-overflow-for-agents/)

生成摘要时出错

---

## 94. BIO – The Bao I/O Co-Processor

**原文标题**: BIO – The Bao I/O Co-Processor

**原文链接**: [https://www.crowdsupply.com/baochip/dabao/updates/bio-the-bao-i-o-co-processor](https://www.crowdsupply.com/baochip/dabao/updates/bio-the-bao-i-o-co-processor)

生成摘要时出错

---

## 95. A Chess Playing Machine – Shannon (1950) [pdf]

**原文标题**: A Chess Playing Machine – Shannon (1950) [pdf]

**原文链接**: [https://www.paradise.caltech.edu/ist4/lectures/shannonchess1950.pdf](https://www.paradise.caltech.edu/ist4/lectures/shannonchess1950.pdf)

生成摘要时出错

---

## 96. A 6502 disassembler with a TUI: A modern take on Regenerator

**原文标题**: A 6502 disassembler with a TUI: A modern take on Regenerator

**原文链接**: [https://github.com/ricardoquesada/regenerator2000](https://github.com/ricardoquesada/regenerator2000)

生成摘要时出错

---

## 97. Trivy under attack again: Widespread GitHub Actions tag compromise secrets

**原文标题**: Trivy under attack again: Widespread GitHub Actions tag compromise secrets

**原文链接**: [https://socket.dev/blog/trivy-under-attack-again-github-actions-compromise](https://socket.dev/blog/trivy-under-attack-again-github-actions-compromise)

生成摘要时出错

---

## 98. iPhone 17 Pro Demonstrated Running a 400B LLM

**原文标题**: iPhone 17 Pro Demonstrated Running a 400B LLM

**原文链接**: [https://twitter.com/anemll/status/2035901335984611412](https://twitter.com/anemll/status/2035901335984611412)

生成摘要时出错

---

## 99. GitHub is once again down

**原文标题**: GitHub is once again down

**原文链接**: [https://www.githubstatus.com/incidents/kp06czybl7dw](https://www.githubstatus.com/incidents/kp06czybl7dw)

生成摘要时出错

---

## 100. IRIX 3dfx Voodoo driver and glide2x IRIX port

**原文标题**: IRIX 3dfx Voodoo driver and glide2x IRIX port

**原文链接**: [https://sdz-mods.com/index.php/2026/03/23/irix-3dfx-voodoo-driver-glide2x-irix-port/](https://sdz-mods.com/index.php/2026/03/23/irix-3dfx-voodoo-driver-glide2x-irix-port/)

生成摘要时出错

---

