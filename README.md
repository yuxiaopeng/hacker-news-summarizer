# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-11.md)

*最后自动更新时间: 2026-09-11 19:53:53*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 2 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 3 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 4 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 5 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 6 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 7 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 8 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 9 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 10 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 11 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 12 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 13 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 14 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 15 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 16 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 17 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 18 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 19 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 20 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 21 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 22 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 23 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 24 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 25 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 26 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 27 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 28 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 29 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 30 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 31 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 32 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 33 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 34 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 35 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 36 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 37 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 38 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 39 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 40 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 41 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 42 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 43 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 44 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 45 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 46 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 47 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 48 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 49 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 50 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 51 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 52 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 53 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 54 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 55 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 56 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 57 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 58 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 59 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 60 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 61 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 62 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 63 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 64 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 65 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 66 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 67 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 68 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 69 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 70 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 71 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 72 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 73 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 74 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 75 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 76 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 77 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 78 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 79 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 80 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 81 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 82 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 83 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 84 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 85 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 86 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 87 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 88 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 89 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 90 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 91 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 92 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 93 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 94 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 95 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 96 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 97 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 98 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 99 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 100 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 101 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 102 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 103 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 104 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 105 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 106 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 107 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 108 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 109 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 110 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 111 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 112 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 113 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 114 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 115 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 116 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 117 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 118 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 119 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 120 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 121 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 122 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 123 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 124 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 125 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 126 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 127 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 128 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 129 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 130 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 131 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 132 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 133 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 134 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 135 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 136 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 137 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 138 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 139 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 140 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 141 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 142 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 143 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 144 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 145 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 146 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 147 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 148 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 149 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 150 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 151 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 152 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 153 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 154 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 155 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 156 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 157 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 158 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 159 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 160 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 161 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 162 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 163 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 164 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 165 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 166 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 167 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 168 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 169 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 170 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 171 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 172 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 173 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 174 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 175 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 176 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 177 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 178 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 179 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 180 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 181 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 182 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 183 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 184 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 185 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 186 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 187 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 188 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 189 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 190 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 191 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 192 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 193 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 194 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 195 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 196 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 197 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 198 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 199 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 200 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 201 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 202 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 203 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 204 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 205 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 206 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 207 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 208 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 209 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 210 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 211 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 212 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 213 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 214 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 215 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 216 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 217 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 218 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 219 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 220 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 221 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 222 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 223 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 224 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 225 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 226 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 227 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 228 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 229 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 230 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 231 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 232 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 233 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 234 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 235 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 236 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 237 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 238 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 239 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 240 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 241 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 242 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 243 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 244 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 245 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 246 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 247 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 248 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 249 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 250 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 251 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 252 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 253 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 254 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 255 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 256 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 257 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 258 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 259 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 260 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 261 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 262 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 263 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 264 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 265 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 266 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 267 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 268 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 269 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 270 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 271 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 272 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 273 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 274 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 275 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 276 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 277 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 278 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 279 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 280 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 281 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 282 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 283 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 284 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 285 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 286 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 287 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 288 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 289 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 290 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 291 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 292 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 293 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 294 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 295 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 296 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 297 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 298 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 299 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 300 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 301 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 302 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 303 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 304 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 305 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 306 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 307 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 308 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 309 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 310 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 311 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 312 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 313 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 314 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 315 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 316 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 317 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 318 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 319 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 320 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 321 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 322 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 323 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 324 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 325 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 326 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 327 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 328 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 329 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 330 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 331 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 332 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 333 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 334 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 335 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 336 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 337 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 338 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 339 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 340 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 341 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 342 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 343 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 344 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 345 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 346 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 347 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 348 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 349 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 350 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 351 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 352 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 353 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 354 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 355 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 356 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 357 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 358 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 359 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 360 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 361 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 362 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 363 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 364 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 365 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 366 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 367 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 368 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 369 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 370 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 371 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 372 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 373 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 374 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 375 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 376 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 377 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 378 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 379 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 380 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 381 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 382 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 383 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 384 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 385 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 386 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 387 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 388 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 389 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 390 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 391 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 392 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 393 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 394 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 395 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 396 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 397 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 398 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 399 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 400 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 401 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 402 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 403 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 404 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 405 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 406 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 407 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 408 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 409 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 410 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 411 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 412 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 413 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 414 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 415 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 416 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 417 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 418 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 419 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 420 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 421 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 422 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 423 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 424 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 425 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 426 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 427 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 428 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 429 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 430 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 431 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 432 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 433 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 434 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 435 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 436 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 437 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 438 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 439 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 440 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 441 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 442 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 443 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 444 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 445 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 446 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 447 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 448 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 449 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 450 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 451 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 452 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 453 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 454 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 455 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 456 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 457 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 458 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 459 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 460 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 461 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 462 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 463 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 464 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 465 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 466 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 467 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 468 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 469 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 470 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 471 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 472 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 473 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 474 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 475 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 476 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 477 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 478 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 479 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 480 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 481 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 482 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 483 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 484 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 485 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 486 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 487 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 488 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 489 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 490 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 491 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 492 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 493 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 494 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 495 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 496 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 497 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 498 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 499 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 500 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 501 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 502 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 503 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 504 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 505 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 506 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 507 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 508 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 509 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 510 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 511 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 512 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 513 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 514 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 515 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 516 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 517 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 518 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 519 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 520 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 521 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 522 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 523 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 524 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 525 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 526 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 527 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 528 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 529 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 530 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 531 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 532 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 533 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 534 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 535 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 536 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 537 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 538 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
