# Hacker News 热门文章摘要 (2026-09-11)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 人工智能在数学中的不对齐

**原文标题**: A misalignment of AI in mathematics

**原文链接**: [https://mathandai.org/](https://mathandai.org/)

《数学领域中人工智能的失配》是一封公开信和宣言，呼吁数学界主动塑造人工智能与其领域的融合。作者中包括多位菲尔兹奖得主，他们认为，尽管人工智能具有变革潜力，但目前其主要由追求利润的私有科技公司驱动的发展轨迹，正对该学科构成重大风险。

核心担忧在于企业级人工智能的发展与数学的核心价值观之间存在“失配”。商业化人工智能专注于自动化和性能，而数学则优先考虑人类的理解、透明度和严密的证明。作者担心，对“黑箱”模型的依赖可能导致数学结果虽然可以验证但无法解释，从而可能侵蚀该领域的教学基础和协作性质。

为了应对这些担忧，该宣言提议向**“开放数学” (Open Math)** 转型，并强调了三大支柱：

1. **开放与透明：** 用于数学的人工智能工具必须是开源的。这能确保人工智能生成结果背后的数据、训练方法和逻辑对于全球学界是可获取且可验证的。
2. **社区治理：** 数学人工智能的发展应由研究人员和学术机构引导，而非私有企业，以确保工具服务于公共利益而非商业利益。
3. **增强理解：** 人工智能的设计应旨在增强人类直觉并促进发现，作为加深人类洞察力的合作者，而非其替代品。

归根结底，这篇文章是呼吁数学家们掌握数字基础设施的主导权。文章总结道，数学的完整性取决于能否确保技术进步与追求深刻、以人为本的理解保持一致。

---

## 2. Λ Snap – 一款面向儿童和成人的计算机科学学习编程语言

**原文标题**: Λ Snap – An inviting programming language for kids and adults for CS study

**原文链接**: [https://snap.berkeley.edu/](https://snap.berkeley.edu/)

**Snap!** 是一款功能多样、基于浏览器的编程语言，其设计初衷是既要让儿童易于上手，又要具备足够强大的功能，以满足成人对计算机科学的深入研究。它既是教学工具，也是创意平台，鼓励用户“立即运行”并探索海量的社区共享项目。

该平台通过以下几个不同的类别展示了该语言的强大能力：

*   **Snap!Con 2025 与人工智能：** Snap! 会议的最新亮点展示了各种高级应用，包括人工神经网络、SnapGPT（可解释人工智能）、语音识别以及专门的教学代码块。
*   **科学与数学：** 社区利用 Snap! 进行复杂的模拟，例如 n 体物理、太阳系模型、斯内尔定律实验以及交互式元素周期表。
*   **游戏与动画：** 项目涵盖了从《Wordle》、《贪吃蛇》和《飞扬的小鸟》等经典重制作品，到复杂的 3D 地板引擎和视差动画。
*   **音乐与媒体：** 该语言支持高级音频处理，包括 MIDI 转换器、波形编辑器和复音乐器合成器。

通过填补入门级积木式编程与高级计算概念之间的鸿沟，Snap! 为学习、实验以及从物理学到数字艺术等领域的跨学科创新提供了一个全面的生态系统。

---

## 3. Litelm：拒绝臃肿的 LiteLLM

**原文标题**: Litelm: LiteLLM Without the Bloat

**原文链接**: [https://github.com/kennethwolters/litelm](https://github.com/kennethwolters/litelm)

**Litelm** 是 LiteLLM 库的一个轻量级替代方案，旨在提供核心的模型路由和格式转换功能，而无需原版包中臃肿的代码。LiteLLM 的代码量超过 10 万行，而 `litelm` 将功能精简至约 2900 行，且仅保留两个依赖项（`openai` 和 `httpx`）。

该库专注于核心的 LLM 调用路径，包括：
*   **模型路由**：将服务商映射到特定的端点。
*   **消息转换**：为 Anthropic、Bedrock 和 Mistral 等服务商转换格式。
*   **核心功能**：支持流式传输、工具使用（函数调用）、嵌入（embeddings）和文本补全。
*   **异步支持**：为所有主要函数提供异步版本（如 `acompletion`）。

为了实现极小的体积，`litelm` 移除了次要功能，如代理服务器、缓存、成本追踪、Token 计数，以及图像或音频生成等特定模态。

至关重要的一点是，`litelm` 保持了与 LiteLLM 完全一致的 API，用户只需更改导入语句即可完成迁移。它支持超过 19 家服务商以及任何兼容 OpenAI 的端点（如通过 `api_base` 参数支持 Ollama 或 vLLM）。此外，它还将各服务商特定的错误映射到统一的异常体系中。

该项目目前处于 **Alpha** 阶段，已验证可作为 DSPy 的无缝替换方案，并通过了包括 260 多项内部测试和 45 项实时服务商测试在内的广泛测试。它为那些需要多服务商集成、但又不希望承担全规模管理套件额外开销的开发者提供了一个精简的解决方案。

---

## 4. 美国环保署计划取消数据中心污染的公众审查规则。

**原文标题**: The EPA Is Planning to Scrap Public Review Rules for Data Center Pollution

**原文链接**: [https://capitalbnews.org/data-centers-permit-rules-epa/](https://capitalbnews.org/data-centers-permit-rules-epa/)

美国国家环境保护局（EPA）正提议取消联邦关于在各州批准工业设施（包括人工智能所需的巨型数据中心）空气污染许可之前，必须进行公众告示和征求意见期的规定。此外，该机构还计划允许开发商在许可正式获批之前便动工建设这些项目。

据美国环保署署长李·泽尔丁（Lee Zeldin）称，这一政策转变旨在“加速许可审批”，并将美国打造为全球“人工智能之都”。然而，此举正面临巨大的抵制：十分之七的美国人反对在自己社区建设数据中心，近200个倡议团体以及一个由多州组成的跨党派联盟也表达了反对意见。

这种影响在南部农村地区尤为严重，那里的非裔社区承担了不成比例的设施迁入压力。批评者认为，绕过公众监督会增加人们接触数据中心及其配套发电厂排放的有毒空气污染物的风险，从而威胁公共健康。居民还面临着社会经济负担，包括为支付基础设施成本而上涨的公用事业费用，以及由房价飙升导致的社区流离失所。

活动人士和地方官员将该计划描述为对“民主透明度”的背叛，并指出地方政府已频繁利用保密协议向公众隐瞒这些项目。如果这些规则在未来一年内最终敲定，居民将在项目动工前被剥夺质疑或抗议其社区工业开发的主要正式渠道。

---

## 5. Claude仅限18岁以上人士使用。

**原文标题**: Claude is only available to people over 18 years

**原文链接**: [https://support.claude.com/en/articles/15171100-age-assurance-on-claude](https://support.claude.com/en/articles/15171100-age-assurance-on-claude)

Anthropic 的消费级产品 Claude 严格限制 18 岁及以上用户使用。用户必须在设置账户时确认年龄，Anthropic 采用安全系统来检测并停用疑似属于未成年人的账户。

如果账户被标记，用户必须通过第三方服务 Yoti 完成验证流程，以恢复访问权限。Yoti 提供三种验证选项：
*   **面部年龄估算**：通过技术分析自拍照来估算年龄（无需身份证件）。
*   **身份证件验证**：上传政府签发的身份证件照片（如护照或驾照）。
*   **Yoti 数字身份应用**：用户分享其现有 Yoti 账户中经过验证的“18 岁以上”属性。

在此过程中，数据隐私是首要任务。Yoti 符合 SOC2 标准，并在年龄检查完成后立即删除所有自拍照和身份证件文档。Anthropic 从不查看或存储用户的身份证件或图像；他们仅接收“通过”或“未通过”的结果，以确定账户资格。

---

## 6. Show HN: Hacker News, Without AI

**原文标题**: Show HN: Hacker News, Without AI

**原文链接**: [https://www.unslop.news/](https://www.unslop.news/)

**unslop.news** 是一个精选版的 Hacker News，专门过滤掉与人工智能（AI）相关的内容。在本次快照中，180 篇投稿中仅有 80 篇通过了过滤，这突显了当前原始平台上 AI 讨论的密集程度，并为科技爱好者提供了一个“纯净”的替代选择。

剩余内容涵盖了软件工程、硬件、科学和企业科技新闻等广泛领域。主要主题和故事包括：

*   **企业与行业新闻：** 重大头条包括 Automattic 涉及 Matt Mullenweg 的持续领导危机、Shopify 收购 Tailwind CSS，以及微软正式将 Rust 列为一级（Tier-1）语言。
*   **工程与性能：** 技术讨论集中在高性能数据库集群（ClickHouse 和 PlanetScale 的 “Neki”）、Julia 1.13 与 GCC 13.5 的发布，以及对 Python 集合和字典在平方级时间性能问题的调查。
*   **安全与系统：** 值得关注的条目包括允许不可信网站冻结 Mac 的漏洞、在安全隔区（Secure Enclave）设备上复制钥匙串的挑战，以及对美国国家安全局（NSA）641A 监控室的技术深度解析。
*   **科学与综合兴趣：** 非技术亮点包括在 2.5 万年前的牙齿中发现药物使用证据、德国阳台太阳能电池板的普及、四色定理的新证明，以及“乔利伍德”面包制作工艺的历史。
*   **怀旧与硬件：** 列表包含了涉及 Logo 编程、HyperCard 字体和定制复古康柏键盘的项目，以及一篇关于保留“一大箱线缆”必要性的热门评论。

总的来说，该信息流表明，虽然 AI 目前占据了科技讨论的主导地位，但仍然存在一个独立于 AI 热潮之外的，由系统编程、科学发现和文化评论构成的稳健生态系统。

---

## 7. 我运维 PB 级 ClickHouse 集群已有 5 年。

**原文标题**: I've operated petabyte-scale ClickHouse clusters for 5 years

**原文链接**: [https://www.tinybird.co/blog/what-i-learned-operating-clickhouse](https://www.tinybird.co/blog/what-i-learned-operating-clickhouse)

Based on six years of operating petabyte-scale ClickHouse clusters at Tinybird, the author provides a practical guide to managing the database’s complexities. The core message is that while setup is easy, maintaining performance and stability at scale requires deep technical rigor.

**Architecture and Storage**
The author utilizes a standard shard-and-replica architecture but emphasizes the importance of a sophisticated HTTP load balancer to manage traffic. For high-performance workloads, they recommend isolating writes to specific replicas and using a "hot/cold" storage strategy. While cloud storage (S3) offers cost-efficiency through compute-storage separation, ClickHouse’s open-source "zero-copy replication" remains buggy. To mitigate this, Tinybird uses local SSDs for low-latency caching and a private fork for optimized S3 handling.

**Upgrades and Testing**
Upgrades should be handled through a strict CI/CD pipeline. The author advises adding one new-version replica at a time, monitoring logs, and avoiding DDL changes during the transition. Because open-source ClickHouse can have undocumented behavior changes, the author stresses that operators must be prepared to read the database's source code and test against multi-node clusters rather than single instances.

**Operational Stability and Costs**
A critical hardware recommendation is to isolate ZooKeeper (or ClickHouse Keeper) on dedicated machines; an overloaded ZooKeeper can freeze the entire cluster. Regarding costs, while hardware and S3 operations are significant factors, the author highlights that hiring a dedicated ClickHouse expert often pays for itself. A skilled operator can optimize queries and schemas to reduce hardware requirements by 3-4x. 

Ultimately, successful ClickHouse management relies on "building muscle" through repetition, automated testing, and a cautious approach to new releases.

---

## 8. Hot coffee could cause oesophageal cancer

**原文标题**: Hot coffee could cause oesophageal cancer

**原文链接**: [https://www.economist.com/science-and-technology/2026/09/11/hot-coffee-could-cause-oesophageal-cancer](https://www.economist.com/science-and-technology/2026/09/11/hot-coffee-could-cause-oesophageal-cancer)

生成摘要时出错

---

## 9. 118M Queries per Second on Neki

**原文标题**: 118M Queries per Second on Neki

**原文链接**: [https://planetscale.com/blog/118-million-queries-per-second-on-neki](https://planetscale.com/blog/118-million-queries-per-second-on-neki)

To celebrate the platform preview release of Neki, engineers Florent Poinsard and Hirad Pourtahmasbi conducted a benchmark test that successfully reached **118.5 million queries per second (QPS)**. While the initial goal was to hit 1 million QPS, the team demonstrated the system's massive linear scalability by expanding the cluster from 5 to 512 shards.

**Key Performance Metrics:**
*   **Throughput:** Sustained 118,538,803 QPS for 16 minutes, peaking at over 118.7 million.
*   **Data Volume:** 1.22 PiB of data.
*   **Latency:** p99 latency of 6.06ms at the router and 13.95ms at the client.
*   **Reliability:** An error rate of only 67 per second (approximately one error per 1.8 million queries).
*   **Infrastructure:** The setup utilized 512 shards (Postgres primaries on r8g.16xlarge instances) and 480 Neki routers (8xlarge instances), generating over 2 Tbps of network traffic and 15.8 million read IOPS.

**Testing Parameters:**
The benchmark focused on demonstrating **linear scalability**. As the shard count increased tenfold (from 5 to 50 to 512), the throughput followed suit, eventually exceeding the target of 200k QPS per shard to reach 231k QPS per shard. 

The workload was specifically designed as a "point select" test: read-only queries fetching a single row by primary key. The test did not include writes, joins, cross-shard queries, or shard replicas, and no failovers occurred during the window. The authors plan to release a follow-up article detailing the engineering challenges encountered while reaching the 100 million QPS milestone.

---

## 10. AlphaGenome maps 9B DNA variants

**原文标题**: AlphaGenome maps 9B DNA variants

**原文链接**: [https://spectrum.ieee.org/alphagenome-atlas](https://spectrum.ieee.org/alphagenome-atlas)

生成摘要时出错

---

## 11. Zep AI (YC W24) Is Hiring a Head of Forward Deployed Engineering

**原文标题**: Zep AI (YC W24) Is Hiring a Head of Forward Deployed Engineering

**原文链接**: [https://www.getzep.com/careers/](https://www.getzep.com/careers/)

生成摘要时出错

---

## 12. Show HN: Godot and Rust based multiplexer (terminal panes and more)

**原文标题**: Show HN: Godot and Rust based multiplexer (terminal panes and more)

**原文链接**: [https://github.com/godot-pty/gpty](https://github.com/godot-pty/gpty)

生成摘要时出错

---

## 13. Rune is now open source

**原文标题**: Rune is now open source

**原文链接**: [https://rune.build/blog/rune-is-now-open-source](https://rune.build/blog/rune-is-now-open-source)

生成摘要时出错

---

## 14. Logo Programming Language

**原文标题**: Logo Programming Language

**原文链接**: [https://el.media.mit.edu/logo-foundation/what_is_logo/logo_programming.html](https://el.media.mit.edu/logo-foundation/what_is_logo/logo_programming.html)

Logo is a Lisp-based programming language specifically designed as an educational tool. Its development is guided by four core principles: interactivity, modularity, extensibility, and flexibility.

**Key Features:**
*   **Interactivity:** Primarily an interpreted language, Logo provides immediate feedback through descriptive error messages. This helps beginners debug and understand the requirements of different commands (primitives) in real-time.
*   **Modularity and Extensibility:** Programs are built using small, manageable procedures defined with `to` and `end`. Once a procedure is created, it functions exactly like a built-in primitive. This allows users to "teach" the language new words, building complex projects through a growing vocabulary in a manner similar to learning a spoken language.
*   **Flexibility:** Logo handles data types loosely, using "words" and "lists." Unlike stricter languages, Logo does not require users to pre-define numerical types (like integers or reals) before performing arithmetic. This ease of use extends to advanced concepts like recursion and list manipulation.

**Enhancements and Versions:**
While standard Logo is famous for "turtle graphics," enhanced versions offer advanced capabilities. These include **Object Logo** (object-oriented), **MicroWorlds** (multi-tasking), and **StarLogo** (massively parallel processing). These versions allow for simultaneous execution of commands, such as running a turtle animation while immediately executing other logic.

**Resources:**
For those seeking to master the language, the article recommends Brian Harvey’s *Computer Science Logo Style* and Michael Friendly’s *Advanced Logo*. Various implementations, such as UCBLogo, MSWLogo, and StarLogo Nova, remain available for modern learners.

---

## 15. Show HN: Toast, a beautiful by default in terminal IDE

**原文标题**: Show HN: Toast, a beautiful by default in terminal IDE

**原文链接**: [https://github.com/paradise-runner/toast](https://github.com/paradise-runner/toast)

生成摘要时出错

---

## 16. So you want to use OpenRouter?

**原文标题**: So you want to use OpenRouter?

**原文链接**: [https://mmoustafa.com/blog/so-you-want-to-use-openrouter/](https://mmoustafa.com/blog/so-you-want-to-use-openrouter/)

生成摘要时出错

---

## 17. Global Glacier Extinction Explorer

**原文标题**: Global Glacier Extinction Explorer

**原文链接**: [https://glacierextinction.com](https://glacierextinction.com)

生成摘要时出错

---

## 18. RTK reports token savings, but our cost benchmarks disagree

**原文标题**: RTK reports token savings, but our cost benchmarks disagree

**原文链接**: [https://quesma.com/blog/does-rtk-make-ai-coding-cheaper/](https://quesma.com/blog/does-rtk-make-ai-coding-cheaper/)

生成摘要时出错

---

## 19. How I Prompt

**原文标题**: How I Prompt

**原文链接**: [https://thorstenball.com/talks/how-i-prompt/](https://thorstenball.com/talks/how-i-prompt/)

生成摘要时出错

---

## 20. Copying login keychains between Macs fails on Secure Enclave Macs with Tahoe

**原文标题**: Copying login keychains between Macs fails on Secure Enclave Macs with Tahoe

**原文链接**: [https://derflounder.wordpress.com/2026/09/08/manually-copying-login-keychain-files-from-one-mac-to-another-no-longer-works-on-secure-enclave-equipped-macs-running-macos-tahoe/](https://derflounder.wordpress.com/2026/09/08/manually-copying-login-keychain-files-from-one-mac-to-another-no-longer-works-on-secure-enclave-equipped-macs-running-macos-tahoe/)

生成摘要时出错

---

## 21. Measuring the sloppiness of code

**原文标题**: Measuring the sloppiness of code

**原文链接**: [https://earendil.com/posts/measuring-code-sloppiness/](https://earendil.com/posts/measuring-code-sloppiness/)

生成摘要时出错

---

## 22. Mind-altering drugs played key role in rise of Andean civilization

**原文标题**: Mind-altering drugs played key role in rise of Andean civilization

**原文链接**: [https://www.science.org/content/article/mind-altering-drugs-played-key-role-rise-andean-civilization](https://www.science.org/content/article/mind-altering-drugs-played-key-role-rise-andean-civilization)

生成摘要时出错

---

## 23. Show HN: Bodily Oddities

**原文标题**: Show HN: Bodily Oddities

**原文链接**: [https://vester.si/bodily-oddities/](https://vester.si/bodily-oddities/)

生成摘要时出错

---

## 24. Stop making swap partitions—use swap files instead

**原文标题**: Stop making swap partitions—use swap files instead

**原文链接**: [https://gist.github.com/joshenders/c4960cec9c63a7b7d68ffa9543356c43](https://gist.github.com/joshenders/c4960cec9c63a7b7d68ffa9543356c43)

生成摘要时出错

---

## 25. HuggingFace: Security.txt

**原文标题**: HuggingFace: Security.txt

**原文链接**: [https://huggingface.co/security.txt](https://huggingface.co/security.txt)

生成摘要时出错

---

## 26. Copper lined vest to help penguins with recovery

**原文标题**: Copper lined vest to help penguins with recovery

**原文链接**: [https://apnews.com/article/chile-el-nino-humboldt-penguins-vulnerable-injuries-rehabilitation-6e93b8d4eaef903e4c85d16ade7d5881](https://apnews.com/article/chile-el-nino-humboldt-penguins-vulnerable-injuries-rehabilitation-6e93b8d4eaef903e4c85d16ade7d5881)

生成摘要时出错

---

## 27. How the Chorleywood Bread Process transformed British bread

**原文标题**: How the Chorleywood Bread Process transformed British bread

**原文链接**: [https://edconway.substack.com/p/the-little-holes-in-your-bread-are](https://edconway.substack.com/p/the-little-holes-in-your-bread-are)

生成摘要时出错

---

## 28. Room 641A

**原文标题**: Room 641A

**原文链接**: [https://en.wikipedia.org/wiki/Room_641A](https://en.wikipedia.org/wiki/Room_641A)

生成摘要时出错

---

## 29. Cherenkov Radiation

**原文标题**: Cherenkov Radiation

**原文链接**: [http://www.iaea.org/newscenter/news/what-is-cherenkov-radiation](http://www.iaea.org/newscenter/news/what-is-cherenkov-radiation)

生成摘要时出错

---

## 30. Google will buy half the electricity from one of Finland's nuclear power plants

**原文标题**: Google will buy half the electricity from one of Finland's nuclear power plants

**原文链接**: [https://www.bbc.com/news/articles/c8r6y4me2g6o](https://www.bbc.com/news/articles/c8r6y4me2g6o)

生成摘要时出错

---

## 31. Re-Engineering YouTube for the Living Room: Bringing "Chrobalt" to RDK

**原文标题**: Re-Engineering YouTube for the Living Room: Bringing "Chrobalt" to RDK

**原文链接**: [https://www.collabora.com/news-and-blog/news-and-events/re-engineering-youtube-for-the-living-room-bringing-%E2%80%9Cchrobalt%E2%80%9D-to-rdk.html](https://www.collabora.com/news-and-blog/news-and-events/re-engineering-youtube-for-the-living-room-bringing-%E2%80%9Cchrobalt%E2%80%9D-to-rdk.html)

生成摘要时出错

---

## 32. iPod Classic 6G in QEMU

**原文标题**: iPod Classic 6G in QEMU

**原文链接**: [https://www.reddit.com/r/emulation/s/VL4Au2HGxq](https://www.reddit.com/r/emulation/s/VL4Au2HGxq)

生成摘要时出错

---

## 33. Kenyans Did College Students' Homework for Years. Then A.I. Arrived

**原文标题**: Kenyans Did College Students' Homework for Years. Then A.I. Arrived

**原文链接**: [https://www.nytimes.com/2026/09/05/technology/kenya-college-essays-ai.html](https://www.nytimes.com/2026/09/05/technology/kenya-college-essays-ai.html)

生成摘要时出错

---

## 34. Houthis Seize Strategic Red Sea Port, a Major Victory for Iranian Ally

**原文标题**: Houthis Seize Strategic Red Sea Port, a Major Victory for Iranian Ally

**原文链接**: [https://www.nytimes.com/2026/09/10/world/middleeast/yemens-houthis-seize-strategic-red-sea-port-officials-say.html](https://www.nytimes.com/2026/09/10/world/middleeast/yemens-houthis-seize-strategic-red-sea-port-officials-say.html)

生成摘要时出错

---

## 35. Houthis 'take control' of key island in global shipping route

**原文标题**: Houthis 'take control' of key island in global shipping route

**原文链接**: [https://www.bbc.com/news/live/cmd683p01eljt](https://www.bbc.com/news/live/cmd683p01eljt)

生成摘要时出错

---

## 36. Working with Git Worktrees in Magit

**原文标题**: Working with Git Worktrees in Magit

**原文链接**: [https://emacsredux.com/blog/2026/09/02/working-with-git-worktrees-in-magit/](https://emacsredux.com/blog/2026/09/02/working-with-git-worktrees-in-magit/)

生成摘要时出错

---

## 37. RISC-V Emulator and Linux System from Scratch

**原文标题**: RISC-V Emulator and Linux System from Scratch

**原文链接**: [https://github.com/WerWolv/riscv-emulator](https://github.com/WerWolv/riscv-emulator)

生成摘要时出错

---

## 38. An interactive tour of the spanning tree protocol

**原文标题**: An interactive tour of the spanning tree protocol

**原文链接**: [https://vincent.bernat.ch/en/blog/2026-spanning-tree](https://vincent.bernat.ch/en/blog/2026-spanning-tree)

生成摘要时出错

---

## 39. Show HN: Extension to filter LLM written articles

**原文标题**: Show HN: Extension to filter LLM written articles

**原文链接**: [https://hnslop.nilsherzig.com/](https://hnslop.nilsherzig.com/)

生成摘要时出错

---

## 40. New York thoracic surgeon: "For many patients 9/11 is not over"

**原文标题**: New York thoracic surgeon: "For many patients 9/11 is not over"

**原文链接**: [https://www.statnews.com/2026/09/11/sept-11-25th-anniversary-ground-zero-exposure-cancer-moment-of-silence/](https://www.statnews.com/2026/09/11/sept-11-25th-anniversary-ground-zero-exposure-cancer-moment-of-silence/)

生成摘要时出错

---

## 41. Shopify is moving from React Native back to Swift and Kotlin

**原文标题**: Shopify is moving from React Native back to Swift and Kotlin

**原文链接**: [https://shopify.engineering/back-to-native](https://shopify.engineering/back-to-native)

生成摘要时出错

---

## 42. GPT-6 Astra does 3D camera tracking and VFX in Blender

**原文标题**: GPT-6 Astra does 3D camera tracking and VFX in Blender

**原文链接**: [https://twitter.com/ryanvogel/status/2098477000843211081](https://twitter.com/ryanvogel/status/2098477000843211081)

生成摘要时出错

---

## 43. Creatine improves muscle mass and cognitive function even without exercise

**原文标题**: Creatine improves muscle mass and cognitive function even without exercise

**原文链接**: [https://www.psypost.org/creatine-improves-muscle-mass-and-cognitive-function-in-older-adults-even-without-exercise/](https://www.psypost.org/creatine-improves-muscle-mass-and-cognitive-function-in-older-adults-even-without-exercise/)

生成摘要时出错

---

## 44. How to Build a $20B Semiconductor Fab (2024)

**原文标题**: How to Build a $20B Semiconductor Fab (2024)

**原文链接**: [https://www.construction-physics.com/p/how-to-build-a-20-billion-semiconductor](https://www.construction-physics.com/p/how-to-build-a-20-billion-semiconductor)

生成摘要时出错

---

## 45. Show HN: Clawfight.ai MCP-driven agentic game play

**原文标题**: Show HN: Clawfight.ai MCP-driven agentic game play

**原文链接**: [https://clawfight.ai/agents.md](https://clawfight.ai/agents.md)

生成摘要时出错

---

## 46. The Deathray: A simple way for an untrusted site to freeze a Mac

**原文标题**: The Deathray: A simple way for an untrusted site to freeze a Mac

**原文链接**: [https://auberon.xyz/blog/posts/deathray/](https://auberon.xyz/blog/posts/deathray/)

生成摘要时出错

---

## 47. Nine coding harnesses vs. your laptop

**原文标题**: Nine coding harnesses vs. your laptop

**原文链接**: [https://nasutton.notion.site/Nine-coding-harnesses-vs-your-laptop-3d139990182b80d59fa3cf500f0450ba?pvs=74](https://nasutton.notion.site/Nine-coding-harnesses-vs-your-laptop-3d139990182b80d59fa3cf500f0450ba?pvs=74)

生成摘要时出错

---

## 48. Don't let anyone take away your big box of cables

**原文标题**: Don't let anyone take away your big box of cables

**原文链接**: [https://blog.jim-nielsen.com/2026/hands-off-my-cables/](https://blog.jim-nielsen.com/2026/hands-off-my-cables/)

生成摘要时出错

---

## 49. I recently went through a translation of Musashi's Book of Five Rings

**原文标题**: I recently went through a translation of Musashi's Book of Five Rings

**原文链接**: [https://twitter.com/ID_AA_Carmack/status/2098443262214230095](https://twitter.com/ID_AA_Carmack/status/2098443262214230095)

生成摘要时出错

---

## 50. Open-weights world models' parameter size doubles every ~6 months

**原文标题**: Open-weights world models' parameter size doubles every ~6 months

**原文链接**: [https://twitter.com/kaarelkaarelson/status/2098472992821199358](https://twitter.com/kaarelkaarelson/status/2098472992821199358)

生成摘要时出错

---

## 51. CSS Curiosities of the Past

**原文标题**: CSS Curiosities of the Past

**原文链接**: [https://vale.rocks/posts/css-relics](https://vale.rocks/posts/css-relics)

生成摘要时出错

---

## 52. NTSB issues investigative update on B-767 runway excursion accident in Miami

**原文标题**: NTSB issues investigative update on B-767 runway excursion accident in Miami

**原文链接**: [https://www.ntsb.gov:443/news/press-releases/Pages/NR20260909.aspx](https://www.ntsb.gov:443/news/press-releases/Pages/NR20260909.aspx)

生成摘要时出错

---

## 53. Show HN: Hacker News, without AI

**原文标题**: Show HN: Hacker News, without AI

**原文链接**: [https://hcker.news/?ai=exclude](https://hcker.news/?ai=exclude)

生成摘要时出错

---

## 54. Agents on Rails: Best model solves 35% of feature benchmark runs

**原文标题**: Agents on Rails: Best model solves 35% of feature benchmark runs

**原文链接**: [https://rubyonrails.org/2026/9/9/agents-on-rails-stage-2](https://rubyonrails.org/2026/9/9/agents-on-rails-stage-2)

生成摘要时出错

---

## 55. Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra

**原文标题**: Cognition launches new SWE-2 model, Rivaling Fable 5.1 and GPT-Astra

**原文链接**: [https://cognition.com/blog/swe-2](https://cognition.com/blog/swe-2)

生成摘要时出错

---

## 56. Hacker News with reduced priority for AI driven content

**原文标题**: Hacker News with reduced priority for AI driven content

**原文链接**: [https://sprinklz.io/public/pdwt4dve5uai](https://sprinklz.io/public/pdwt4dve5uai)

生成摘要时出错

---

## 57. Proof of Capture: Apple Reference Image, but open source and using steganography

**原文标题**: Proof of Capture: Apple Reference Image, but open source and using steganography

**原文链接**: [https://merybenavente.me/blog/proof-of-capture](https://merybenavente.me/blog/proof-of-capture)

生成摘要时出错

---

## 58. Experiment – Projectional Viewer

**原文标题**: Experiment – Projectional Viewer

**原文链接**: [https://programmingsimplicity.substack.com/p/experiment-projectional-viewer](https://programmingsimplicity.substack.com/p/experiment-projectional-viewer)

生成摘要时出错

---

## 59. Governor Newsom signs the strongest child safety chatbot and social media laws

**原文标题**: Governor Newsom signs the strongest child safety chatbot and social media laws

**原文链接**: [https://www.gov.ca.gov/2026/09/10/governor-newsom-signs-the-strongest-child-safety-chatbot-and-social-media-laws-in-the-nation/](https://www.gov.ca.gov/2026/09/10/governor-newsom-signs-the-strongest-child-safety-chatbot-and-social-media-laws-in-the-nation/)

生成摘要时出错

---

## 60. Can humans learn to hibernate? [video]

**原文标题**: Can humans learn to hibernate? [video]

**原文链接**: [https://www.youtube.com/watch?v=Cm00TFrmQRs](https://www.youtube.com/watch?v=Cm00TFrmQRs)

生成摘要时出错

---

## 61. The Cretan Method

**原文标题**: The Cretan Method

**原文链接**: [http://hintjens.com/blog:81](http://hintjens.com/blog:81)

生成摘要时出错

---

## 62. Matt Mullenweg tells Automattic staff in Slack he's back in control after ouster

**原文标题**: Matt Mullenweg tells Automattic staff in Slack he's back in control after ouster

**原文链接**: [https://techcrunch.com/2026/09/11/matt-mullenweg-tells-automattic-staff-in-slack-hes-back-in-control-after-ceo-ouster/](https://techcrunch.com/2026/09/11/matt-mullenweg-tells-automattic-staff-in-slack-hes-back-in-control-after-ceo-ouster/)

生成摘要时出错

---

## 63. OpenAI Agents API

**原文标题**: OpenAI Agents API

**原文链接**: [https://developers.openai.com/api/docs/guides/agents-api/overview](https://developers.openai.com/api/docs/guides/agents-api/overview)

生成摘要时出错

---

## 64. Rust is tier-1 language at Microsoft

**原文标题**: Rust is tier-1 language at Microsoft

**原文链接**: [https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/)

生成摘要时出错

---

## 65. Detecting and countering misuse of AI: September 2026

**原文标题**: Detecting and countering misuse of AI: September 2026

**原文链接**: [https://www.anthropic.com/threat-intelligence-report-september-2026](https://www.anthropic.com/threat-intelligence-report-september-2026)

生成摘要时出错

---

## 66. JEP 544: Ahead-of-Time Code Compilation

**原文标题**: JEP 544: Ahead-of-Time Code Compilation

**原文链接**: [https://openjdk.org/jeps/544](https://openjdk.org/jeps/544)

生成摘要时出错

---

## 67. List of references on Sony websites to players "owning" their digital games

**原文标题**: List of references on Sony websites to players "owning" their digital games

**原文链接**: [https://consumerrights.wiki/w/Sony_PlayStation_digital_game_ownership_lawsuit](https://consumerrights.wiki/w/Sony_PlayStation_digital_game_ownership_lawsuit)

生成摘要时出错

---

## 68. Moonshot serves Claude instead of Kimi and collects exchanges for model training

**原文标题**: Moonshot serves Claude instead of Kimi and collects exchanges for model training

**原文链接**: [https://twitter.com/DavidAgranovich/status/2098168522862215449](https://twitter.com/DavidAgranovich/status/2098168522862215449)

生成摘要时出错

---

## 69. Recursion into madness

**原文标题**: Recursion into madness

**原文链接**: [https://blog.coredump.cx/p/recursion-into-madness](https://blog.coredump.cx/p/recursion-into-madness)

生成摘要时出错

---

## 70. Technique for Manipulating Satellite Photos Now Reveals Ancient Images (2025)

**原文标题**: Technique for Manipulating Satellite Photos Now Reveals Ancient Images (2025)

**原文链接**: [https://spinoff.nasa.gov/Manipulating_Satellite_Photos_Now_Reveals_Ancient_Images](https://spinoff.nasa.gov/Manipulating_Satellite_Photos_Now_Reveals_Ancient_Images)

生成摘要时出错

---

## 71. Neijuan

**原文标题**: Neijuan

**原文链接**: [https://en.wikipedia.org/wiki/Neijuan](https://en.wikipedia.org/wiki/Neijuan)

生成摘要时出错

---

## 72. The Waymo effect: how AI is quietly making research less collaborative

**原文标题**: The Waymo effect: how AI is quietly making research less collaborative

**原文链接**: [https://www.researchagenda.news/articles/the-waymo-effect.html](https://www.researchagenda.news/articles/the-waymo-effect.html)

生成摘要时出错

---

## 73. AI made 16 new viruses

**原文标题**: AI made 16 new viruses

**原文链接**: [https://www.morningbrew.com/stories/ai-made-16-brand-new-viruses](https://www.morningbrew.com/stories/ai-made-16-brand-new-viruses)

生成摘要时出错

---

## 74. To write non-fiction, draw the trunk, then the rest of the tree

**原文标题**: To write non-fiction, draw the trunk, then the rest of the tree

**原文链接**: [https://devz.cl/posts/how-to-write/](https://devz.cl/posts/how-to-write/)

生成摘要时出错

---

## 75. Apple A20 Pro Geekbench Result

**原文标题**: Apple A20 Pro Geekbench Result

**原文链接**: [https://browser.geekbench.com/v6/cpu/compare/19147979?baseline=19141805](https://browser.geekbench.com/v6/cpu/compare/19147979?baseline=19141805)

生成摘要时出错

---

## 76. Silicon Valley is transforming the military-industrial complex? (2024)

**原文标题**: Silicon Valley is transforming the military-industrial complex? (2024)

**原文链接**: [https://costsofwar.watson.brown.edu/paper/how-big-tech-and-silicon-valley-are-transforming-military-industrial-complex](https://costsofwar.watson.brown.edu/paper/how-big-tech-and-silicon-valley-are-transforming-military-industrial-complex)

生成摘要时出错

---

## 77. What Comes After Git

**原文标题**: What Comes After Git

**原文链接**: [https://ersc.io/blog/what-comes-after-git](https://ersc.io/blog/what-comes-after-git)

生成摘要时出错

---

## 78. DeepSeek 4.1 Flash

**原文标题**: DeepSeek 4.1 Flash

**原文链接**: [https://www.deepseek.com/en/news/deepseek-v4-1-flash/](https://www.deepseek.com/en/news/deepseek-v4-1-flash/)

生成摘要时出错

---

## 79. AI Is Breaking This Thing We Call Trust

**原文标题**: AI Is Breaking This Thing We Call Trust

**原文链接**: [https://terriblesoftware.org/2026/09/10/ai-is-breaking-this-thing-we-call-trust/](https://terriblesoftware.org/2026/09/10/ai-is-breaking-this-thing-we-call-trust/)

生成摘要时出错

---

## 80. Testing race conditions with mem access tracing and stack-based delay injection

**原文标题**: Testing race conditions with mem access tracing and stack-based delay injection

**原文链接**: [https://projectzero.google/2026/09/maccconc-race-condition.html](https://projectzero.google/2026/09/maccconc-race-condition.html)

生成摘要时出错

---

## 81. Scientists Discover the Earliest Evidence of Drug Use in 25,000-Year-Old Teeth

**原文标题**: Scientists Discover the Earliest Evidence of Drug Use in 25,000-Year-Old Teeth

**原文链接**: [https://www.openculture.com/2026/09/scientists-discover-the-earliest-evidence-of-drug-use-in-25000-year-old-teeth.html](https://www.openculture.com/2026/09/scientists-discover-the-earliest-evidence-of-drug-use-in-25000-year-old-teeth.html)

生成摘要时出错

---

## 82. Python sets and dictionaries can have quadratic-time performance

**原文标题**: Python sets and dictionaries can have quadratic-time performance

**原文链接**: [https://lemire.me/blog/2026/09/03/python-sets-and-dictionaries-can-have-quadratic-time-performance/](https://lemire.me/blog/2026/09/03/python-sets-and-dictionaries-can-have-quadratic-time-performance/)

生成摘要时出错

---

## 83. DeepSeek v4.1 Flash

**原文标题**: DeepSeek v4.1 Flash

**原文链接**: [https://twitter.com/deepseek_ai/status/2097930608790167907](https://twitter.com/deepseek_ai/status/2097930608790167907)

生成摘要时出错

---

## 84. Helion Moves Fusion Goalposts

**原文标题**: Helion Moves Fusion Goalposts

**原文链接**: [https://www.axios.com/pro/climate-deals/2026/09/08/helion-energy-fusion-net-electricity-date-year](https://www.axios.com/pro/climate-deals/2026/09/08/helion-energy-fusion-net-electricity-date-year)

生成摘要时出错

---

## 85. What happens when a GPU writes memory

**原文标题**: What happens when a GPU writes memory

**原文链接**: [https://blog.doubleword.ai/what-happens-when-a-gpu-writes-memory](https://blog.doubleword.ai/what-happens-when-a-gpu-writes-memory)

生成摘要时出错

---

## 86. iPhone Duo

**原文标题**: iPhone Duo

**原文链接**: [https://www.apple.com/iphone-duo/](https://www.apple.com/iphone-duo/)

生成摘要时出错

---

## 87. Child Sexual Abuse Material Persists on X

**原文标题**: Child Sexual Abuse Material Persists on X

**原文链接**: [https://www.nytimes.com/2026/09/11/technology/x-grok-child-images.html](https://www.nytimes.com/2026/09/11/technology/x-grok-child-images.html)

生成摘要时出错

---

## 88. Show HN: Vertumnus – printable posters of farmers' market produce seasonality

**原文标题**: Show HN: Vertumnus – printable posters of farmers' market produce seasonality

**原文链接**: [https://vertumnus.fyi](https://vertumnus.fyi)

生成摘要时出错

---

## 89. Music Theory for the 21st-Century Classroom

**原文标题**: Music Theory for the 21st-Century Classroom

**原文链接**: [https://musictheory.pugetsound.edu/mt21c/MusicTheory.html](https://musictheory.pugetsound.edu/mt21c/MusicTheory.html)

生成摘要时出错

---

## 90. More questions about whether researchers can trust OpenAI with unpublished math

**原文标题**: More questions about whether researchers can trust OpenAI with unpublished math

**原文链接**: [https://mathstodon.xyz/@andreasthom/117240535270608201](https://mathstodon.xyz/@andreasthom/117240535270608201)

生成摘要时出错

---

## 91. Compute-efficient pretraining and scaling to trillion-parameter models

**原文标题**: Compute-efficient pretraining and scaling to trillion-parameter models

**原文链接**: [https://magic.dev/blog/pretraining#](https://magic.dev/blog/pretraining#)

生成摘要时出错

---

## 92. Cancer Capital: It sucks for founders, too

**原文标题**: Cancer Capital: It sucks for founders, too

**原文链接**: [https://www.anildash.com/2026/09/09/cancer-capital-founders/](https://www.anildash.com/2026/09/09/cancer-capital-founders/)

生成摘要时出错

---

## 93. Cognition's SWE-2 achieves 92.8 on Terminal-Bench 2.1

**原文标题**: Cognition's SWE-2 achieves 92.8 on Terminal-Bench 2.1

**原文链接**: [https://tokenstead.ai/models/swe-2](https://tokenstead.ai/models/swe-2)

生成摘要时出错

---

## 94. Shopify acquires Tailwind

**原文标题**: Shopify acquires Tailwind

**原文链接**: [https://tailwindcss.com/blog/tailwind-is-joining-shopify](https://tailwindcss.com/blog/tailwind-is-joining-shopify)

生成摘要时出错

---

## 95. Larger Pacific striped octopus

**原文标题**: Larger Pacific striped octopus

**原文链接**: [https://en.wikipedia.org/wiki/Larger_Pacific_striped_octopus](https://en.wikipedia.org/wiki/Larger_Pacific_striped_octopus)

生成摘要时出错

---

## 96. Mold High Speed Linker Being Rewritten in Rust

**原文标题**: Mold High Speed Linker Being Rewritten in Rust

**原文链接**: [https://www.phoronix.com/news/Mold-Linker-In-Rust-Coming](https://www.phoronix.com/news/Mold-Linker-In-Rust-Coming)

生成摘要时出错

---

## 97. Neki – Sharded Postgres

**原文标题**: Neki – Sharded Postgres

**原文链接**: [https://planetscale.com/blog/introducing-neki](https://planetscale.com/blog/introducing-neki)

生成摘要时出错

---

## 98. Customizing my Compaq MX-11800 keyboard

**原文标题**: Customizing my Compaq MX-11800 keyboard

**原文链接**: [https://blog.webb.page/WM-102](https://blog.webb.page/WM-102)

生成摘要时出错

---

## 99. Forgejo <=16.0.3 Critical RCE

**原文标题**: Forgejo <=16.0.3 Critical RCE

**原文链接**: [https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/release-notes-published/16.0.4.md)

生成摘要时出错

---

## 100. Exercise intensity is associated with cardiometabolic health

**原文标题**: Exercise intensity is associated with cardiometabolic health

**原文链接**: [https://www.cell.com/cell-reports-medicine/fulltext/S2666-3791(26)00405-2](https://www.cell.com/cell-reports-medicine/fulltext/S2666-3791(26)00405-2)

生成摘要时出错

---

