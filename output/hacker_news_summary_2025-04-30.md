# Hacker News 热门文章摘要 (2025-04-30)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 小米 MiMo 推理模型

**原文标题**: Xiaomi MiMo Reasoning Model

**原文链接**: [https://github.com/XiaomiMiMo/MiMo](https://github.com/XiaomiMiMo/MiMo)

小米MiMo报告介绍了MiMo-7B，一系列专为增强推理能力而设计和训练的7B语言模型。核心思想是语言模型中有效的推理依赖于定制化的预训练和策略性的后训练。

MiMo-7B-Base 使用精心设计的数据预处理流程、合成推理数据和三阶段数据混合策略，从头开始预训练，总计约25万亿tokens。 预训练的一个关键创新是多Token预测（MTP），以提高性能和推理速度。

后训练包括监督微调（SFT）和强化学习（RL）。 精心策划的包含13万个数学和代码问题的数据集，并结合基于规则的验证，用于RL训练。 为了解决代码中的稀疏奖励问题，引入了难度驱动的代码奖励。 实施了针对简单问题的数据重采样策略，以提高采样效率。 RL基础设施具有无缝Rollout引擎，可加速训练和验证。

该报告展示了四个模型：MiMo-7B-Base、MiMo-7B-RL-Zero（从Base训练的RL）、MiMo-7B-SFT 和 MiMo-7B-RL（从SFT训练的RL）。 评估结果表明，MiMo-7B-RL 在数学和代码推理基准测试中取得了与 OpenAI 的 o1-mini 相媲美的性能，甚至在某些领域超越了更大的 32B 模型。 这些模型可在 Hugging Face 上找到。 该报告提供了 vLLM 和 Hugging Face 推理的部署说明，建议使用特定的 vLLM 分支和一个空系统提示。

---

## 2. DeepSeek-Prover-V2

**原文标题**: DeepSeek-Prover-V2

**原文链接**: [https://github.com/deepseek-ai/DeepSeek-Prover-V2](https://github.com/deepseek-ai/DeepSeek-Prover-V2)

DeepSeek-Prover-V2 是一个新型开源大型语言模型，专为 Lean 4 中的形式化定理证明而设计。它构建于 DeepSeek-V3 之上，并采用了一种新颖的方法，涉及递归定理证明和强化学习，以整合非形式化和形式化的数学推理。

该模型采用两阶段过程进行训练。首先，使用 DeepSeek-V3 将复杂定理分解为子目标，并在 Lean 4 中形式化证明步骤。一个较小的 7B 模型证明这些子目标，并将由此产生的形式化证明与 DeepSeek-V3 的思维链推理相结合，以创建合成的冷启动数据集。其次，证明器模型在该数据集上进行微调，然后使用正确/不正确的反馈进行强化学习。

由此产生的模型 DeepSeek-Prover-V2-671B 实现了最先进的性能，展示了强大的神经定理证明能力。该文章还介绍了 ProverBench，这是一个包含 325 个问题的新基准数据集，其中包括来自 AIME 竞赛和教科书示例的形式化问题，专为高中和本科数学的全面评估而设计。

DeepSeek-Prover-V2 以两种模型尺寸（7B 和 671B）发布，模型和 ProverBench 数据集均可在 Hugging Face 上下载。该文章包含一个快速入门指南，其中包含一个用于生成证明的代码示例。

---

## 3. 我创建了完美维基，并在没有投资者的情况下实现了25万美元的年收入。

**原文标题**: I created Perfect Wiki and reached $250k in annual revenue without investors

**原文链接**: [https://habr.com/en/articles/905812/](https://habr.com/en/articles/905812/)

Ilia Pirozhenko创建了Perfect Wiki，一款用于Microsoft Teams内部知识库的SaaS产品，并在没有投资者的情况下实现了25万美元的年收入。他在2020年失业后，注意到内置Microsoft Teams Wiki的不足之处后开始了这项业务。他发现了一个真正的痛点：用户觉得原生Wiki笨拙且不方便。

在三周内，他推出了一个包含页面创建、编辑和全文搜索的基本版本，立即通过Microsoft Teams Marketplace吸引了付费客户。Perfect Wiki的关键优势在于它与Teams的无缝集成，无需像Confluence或Notion等竞争对手那样在平台之间切换。

如今，全球超过500家公司使用Perfect Wiki，主要分布在美国、加拿大、英国和德国。团队仅由Ilia和一位同事组成，负责管理开发、支持和外包营销。他们通过直接沟通、演示电话和季度调查来优先考虑用户反馈，确保新功能是真正需要的。他们还“自食其果”，在内部使用Perfect Wiki。

Ilia目前每月收入约2.5万美元，云服务和承包商的支出适中。他的主要经验教训是专注于解决特定问题的利基产品，并优先考虑简洁性。Perfect Wiki已扩展到Teams之外，现在提供与Slack、ChatGPT的集成，以及用于网站的聊天机器人功能，展示了基于用户需求的持续改进。

---

## 4. YouTube 好像有人需要配眼镜了

**原文标题**: Someone at YouTube needs glasses

**原文链接**: [https://jayd.ml/2025/04/30/someone-at-youtube-needs-glasses.html](https://jayd.ml/2025/04/30/someone-at-youtube-needs-glasses.html)

作者抱怨当前YouTube主页面的糟糕状态，并将其与2019年1月时的样子进行了消极对比。他们对可见视频数量的大幅减少（从30个减少到5个）以及广告的突出显示感到沮丧，尤其是在大型高分辨率显示器上。他们表达了对YouTube的设计将收入置于用户体验之上的担忧。

作者讽刺性地预测了该平台黯淡的未来，届时主页最终只会显示一个视频，然后一个都没有。然后，他们将这种讽刺升级到一种假设的未来，即使用Neuralink技术将个性化的、人工智能生成的内容和广告直接注入用户的脑中，以优化多巴胺的释放。

最终，作者表达了对YouTube不太注重盈利而更注重提供良好用户体验的时代的怀念。他们希望当前展示糟糕设计的A/B测试失败，并感叹向激进货币化方向的转变。

---

## 5. 加入太阳微系统公司 – 40年前 (2022年)

**原文标题**: Joining Sun Microsystems – 40 years ago (2022)

**原文链接**: [https://akapugs.blog/2022/05/03/674/](https://akapugs.blog/2022/05/03/674/)

在一系列推文中，为了纪念加入太阳微系统公司40周年，pugs78回忆了他如何成为这家初创公司的第8号员工。当时他在Amdahl公司工作，将UNIX移植到大型机上，后来受到比尔·乔伊的推荐，被斯科特·麦克尼利联系。

作者那时就已经熟悉当时的热门技术——UNIX和摩托罗拉68000，并且积极寻找创业机会。他曾面试过Valid Logic Systems和Fortune Systems，但对它们各自关注的CAD和文字处理领域并不感兴趣。至关重要的是，他在施乐SDD和PARC工作的兄弟们为他提供了关于工作站的内部信息。

一位朋友对斯坦福大学的SUN项目及其处理器板赞不绝口，这引起了他的兴趣。当麦克尼利打电话来时，他对SUN主板的熟悉给麦克尼利留下了深刻的印象。在与麦克尼利、安迪·贝托谢姆和维诺德·科斯拉面试，并得知比尔·乔伊也参与其中后，他被太阳公司打动了。他在施乐PARC工作的兄弟对贝托谢姆的积极评价最终促成了这笔交易。

他接受了“设备主管”的职位，并于5月3日与布鲁斯·史密斯（第9号员工）一同入职。他的首要任务是调试一个磁盘驱动程序问题，该问题阻止了UNIX在Sun-1上发布。在一年内，太阳公司显著增长，开始销售带有BSD UNIX、68010和10Mb以太网的工作站。作者表达了他对有机会参与太阳微系统公司这一现象的感激之情。

---

## 6. OCaml 机器学习之翼

**原文标题**: OCaml's Wings for Machine Learning

**原文链接**: [https://github.com/raven-ml/raven](https://github.com/raven-ml/raven)

Raven是一个新兴的OCaml生态系统，旨在为OCaml语言带来高效且直观的机器学习和数据科学能力。它的目标是在利用OCaml的类型安全和性能的同时，复制Python的易用性。Raven目前处于pre-alpha阶段，由几个子项目组成，分别处理机器学习工作流程的不同方面。

核心组件是**Ndarray**，一个类似于NumPy的高性能数值计算库，支持CPU和GPU。基于Ndarray构建的库包括用于计算机视觉实用程序的**Ndarray-CV**、用于数据格式处理的**Ndarray-IO**以及用于访问常用数据集的**Ndarray-Datasets**。**Hugin**是一个生成高质量绘图的可视化库，而**Quill**计划作为一个交互式笔记本应用程序。受JAX启发的**Rune**是一个用于自动微分和JIT编译的库。

文章提供了一个比较表格，突出了Raven与流行的Python数据科学库（如NumPy、Matplotlib/Seaborn和JAX）的对应关系。与Pandas、PyTorch和TensorFlow等效的库被标注为“尚未”实现。

该项目欢迎通过问题报告和pull request进行贡献，并以ISC许可证发布。核心组件Ndarray和Hugin的功能已经完整，可以发布第一个alpha版本，而Rune正处于概念验证阶段，Quill则处于早期原型设计阶段。

---

## 7. Show HN: ART – 一款用于训练智能体的新开源RL框架

**原文标题**: Show HN: ART – a new open-source RL framework for training agents

**原文链接**: [https://github.com/OpenPipe/ART](https://github.com/OpenPipe/ART)

ART (Agent Reinforcement Trainer) 是一个新的开源强化学习 (RL) 框架，旨在提高大型语言模型 (LLM) 在代理工作流程中的性能。它利用 GRPO 强化学习算法，根据模型自身的经验进行训练，通过将 RL 训练循环卸载到 ART 后端来最大程度地减少代码更改。

ART 由客户端和服务器组成。 客户端与 OpenAI 兼容，方便 ART 和用户现有代码库之间的通信，处理消息传递和补全请求。 服务器独立运行并提供 GPU 支持，管理推理和训练的复杂性。 训练循环涉及用户代码使用 ART 客户端执行的代理工作流程。 补全请求被路由到 ART 服务器，该服务器在 vLLM 中运行模型的 LoRA 版本。 然后，用户会为生成的轨迹分配奖励，以指示代理的性能。 轨迹在服务器上分组，使用 GRPO 进行训练，然后保存一个新的 LoRA 并将其加载到 vLLM 中。

ART 支持大多数与 vLLM/HuggingFace-transformers 兼容的因果语言模型。 该框架目前处于 alpha 阶段，欢迎贡献。 它建立在 Unsloth、vLLM、trl 和 SkyPilot 等项目之上。 提供了用于在 2048、Temporal Clue 和 Tic Tac Toe 中训练代理的 Notebook 示例。

---

## 8. GPT-4o 中的谄媚行为

**原文标题**: Sycophancy in GPT-4o

**原文链接**: [https://openai.com/index/sycophancy-in-gpt-4o/](https://openai.com/index/sycophancy-in-gpt-4o/)

无法访问文章链接。

---

## 9. 洛杉矶港表示下周货运量将暴跌35%。

**原文标题**: Port of Los Angeles says shipping volume will plummet 35% next week

**原文链接**: [https://www.cnbc.com/2025/04/29/port-of-los-angeles-sees-shipping-volume-down-35percent-next-week-as-tariffs-bite.html](https://www.cnbc.com/2025/04/29/port-of-los-angeles-sees-shipping-volume-down-35percent-next-week-as-tariffs-bite.html)

洛杉矶港预计下周货运量将大幅下降，预计比去年同期下降35%。 这种“急剧下降”归因于美国零售商因特朗普总统征收的关税而停止从中国发货。 中国约占该港口业务的45%。

洛杉矶港执行董事Gene Seroka在CNBC上警告了这一影响，指出货运量减少，并预计5月份将取消四分之一的通常船只数量。 他预计运输公司将在东南亚寻找替代来源，以弥补这一下滑。

经济学家担心来自中国的贸易量放缓，并预测美国运输和零售业可能出现裁员，可能导致经济衰退。 Seroka认为零售商有5-7周的库存缓冲期，但他预计由于关税，产品种类将减少，价格将会上涨。 他预测消费者将看到更少的选择和剩余产品的价格上涨。

---

## 10. 零售商的完整库存很快将仅剩大约7周。

**原文标题**: Retailers will soon have only about 7 weeks of full inventories left

**原文链接**: [https://fortune.com/article/retailers-weeks-of-inventory-left-trump-china-trade-war/](https://fortune.com/article/retailers-weeks-of-inventory-left-trump-china-trade-war/)

洛杉矶港执行董事吉恩·塞罗卡表示，零售商正面临库存减少的问题，完整库存仅剩约7周。这种情况归因于持续进行的美中贸易战。文章强调了关税和两国贸易紧张局势对零售企业及其维持足够库存能力的潜在影响。这意味着如果源于贸易战的供应链问题得不到解决，消费者可能面临有限的产品选择或潜在的价格上涨。

---

## 11. 排行榜的假象

**原文标题**: The Leaderboard Illusion

**原文链接**: [https://arxiv.org/abs/2504.20879](https://arxiv.org/abs/2504.20879)

排行榜幻觉：Chatbot Arena排行榜系统性问题研究

---

## 12. Jepsen：Amazon RDS for PostgreSQL 17.4

**原文标题**: Jepsen: Amazon RDS for PostgreSQL 17.4

**原文链接**: [https://jepsen.io/analyses/amazon-rds-for-postgresql-17.4](https://jepsen.io/analyses/amazon-rds-for-postgresql-17.4)

Jepsen 分析报告：Amazon RDS for PostgreSQL 17.4 的一致性保证

本Jepsen分析研究了Amazon RDS for PostgreSQL 17.4在健康状况下多可用区部署中的一致性保证。测试涉及在唯一整数列表上运行并发读写事务，旨在检测隔离级别的违规行为。

主要发现是，尽管宣称是“可重复读”隔离级别，但Amazon RDS for PostgreSQL并不能保证快照隔离。 Jepsen观察到G-非相邻循环，包括长分叉异常，这些都是快照隔离的违规行为。 这些异常在AWS支持的各种PostgreSQL版本中均被持续观察到。

分析表明，RDS for PostgreSQL可能提供并行快照隔离，这是一种较弱的一致性模型。这意味着读取事务可能在已执行事务的顺序上存在分歧，从而可能导致数据视图不一致。该问题似乎与只读辅助实例有关。

该报告建议Amazon RDS for PostgreSQL的用户仔细检查其事务结构是否存在潜在的长分叉问题，或设计实验以验证其预期的数据不变性。一种重新获得快照隔离的可能方法是仅使用写入端点，或确保所有安全关键事务至少包含一次写入。

该报告强调，这是一项初步探索，不能明确证明不存在其他问题。 该工作由Jepsen独立完成。

---

## 13. 你不会下载一个 Hacker News 吧？

**原文标题**: You Wouldn't Download a Hacker News

**原文链接**: [https://www.jasonthorsness.com/25](https://www.jasonthorsness.com/25)

你不会下载一个 Hacker News 吧：作者下载了整个 Hacker News 存档，并使用 DuckDB 进行数据分析，文章详细介绍了这一过程。作者之前为一个项目构建了 Hacker News API 客户端，并对其进行了扩展，下载了网站的全部历史记录，最终生成了一个 20 GiB 的 JSON 文件。

起初，作者使用 `grep` 进行简单的搜索。但为了更深入地分析数据，他们决定探索 DuckDB，一个快速、可嵌入的分析引擎。他们将 JSON 数据导入 DuckDB，并使用 SQL 查询来检查 Hacker News 讨论中的趋势。

具体来说，作者分析了编程语言（Python、JavaScript、Java、Ruby、Rust）和数据库系统（MySQL、Postgres、Mongo、Redis、SQLite）在一段时间内被提及的频率，生成了图表显示它们的相对受欢迎程度。文章包含用于计算提及次数 12 周移动平均线的 SQL 查询。

作者得出结论，DuckDB 非常适合分析这种规模的数据集。虽然他们幽默地暗示了使用这些数据训练基于 LLM 的机器人来生成 Hacker News 内容的可能性，但他们表示已经完成了这个项目。最后，作者推广了他们的其他项目 hn.unlurker.com，并提供了他们的 X (Twitter) 个人资料链接。

---

## 14. 新型原子喷泉钟加入保持世界同步的行列

**原文标题**: New atomic fountain clock joins group that keeps the world on time

**原文链接**: [https://www.nist.gov/news-events/news/2025/04/new-atomic-fountain-clock-joins-elite-group-keeps-world-time](https://www.nist.gov/news-events/news/2025/04/new-atomic-fountain-clock-joins-elite-group-keeps-world-time)

NIST推出新型原子喷泉钟NIST-F4，巩固其在时间计量领域的全球领先地位。这款时钟是世界上最精确的时钟之一，已被提交给国际计量局(BIPM)，以获得认可作为主要的频率标准。

自1967年以来，NIST-F4通过测量铯原子的频率来定义秒。其“喷泉”设计确保了卓越的精度；如果它从恐龙时代就开始运行，至今误差也不会超过一秒。

NIST-F4加入了全球精选时钟的行列，增强了全球时间的稳定性和安全性。它还改进了通过无线电和互联网发布的美国官方时间，这对电信和金融等各个领域至关重要。

该时钟的开发涉及重大的工程进步，包括重建微波腔。严格的测试确保了其准确性，并考虑了温度和磁场等因素。NIST-F4的频率测量精度在10的16次方分之2.2以内，与世界上最好的时钟相当。

NIST-F4和另一台喷泉钟NIST-F3大部分时间都在运行，向BIPM发送数据以校准协调世界时(UTC)并引导NIST时标UTC(NIST)。这提高了美国时间计量的可靠性和性能。

---

## 15. 真实的尺寸

**原文标题**: The True Size Of

**原文链接**: [https://thetruesize.com/](https://thetruesize.com/)

好的，基于标题“...的真实大小”，这篇文章很可能侧重于比较某事物被感知的大小与其真实大小。在没有实际文章内容的情况下，我只能推断可能的范围。以下是对文章*可能*涵盖内容的总结：

这篇题为“...的真实大小”的文章，旨在纠正人们对各种物体、地点或概念相对大小的常见误解。它很可能会挑战那些基于有偏见的视角、不准确的表述或不完整的信息的假设。

文章很可能呈现视觉辅助工具、比较数据和深刻的分析，以突出人们*认为*某事物的大小与其*实际*大小之间的差异。例子可能包括：

*   **地理尺度：**比较国家或大陆的大小，纠正地图投影中常见的扭曲（例如，墨卡托投影使一些陆地显得比实际更大）。
*   **科学尺度：**展示原子、分子、细胞、行星或恒星的相对大小。
*   **抽象概念：**探索诸如国债、碳足迹或收入不平等之类的“大小”或影响。

主要目的是教育读者，挑战先入为主的观念，并提供对尺度和比例更准确的理解。通过揭示事物的“真实大小”，这篇文章鼓励读者以更明智和细致的视角看待世界。文章很可能力求客观和数据驱动，依赖于可验证的测量和比较。

---

## 16. 递归思维链：让AI通过自我辩论进行更深入的思考

**原文标题**: Chain of Recursive Thoughts: Make AI think harder by making it argue with itself

**原文链接**: [https://github.com/PhialsBasement/Chain-of-Recursive-Thoughts](https://github.com/PhialsBasement/Chain-of-Recursive-Thoughts)

本文介绍链式递归思考 (CoRT)，一种通过自我辩论迭代改进其响应，从而增强人工智能性能的方法。 CoRT 允许 AI 模型生成初始响应，然后递归生成替代响应，相互评估，并选择最佳响应。 这种迭代过程，重复进行动态确定的“思考轮次”，有效地模拟了自我怀疑和反复尝试，从而改善结果。

作者报告了使用 CoRT 和 Mistral 3.1 24B 模型获得的显著性能提升，尤其是在编程任务中。 本文提供了通过 Web UI（仍在早期开发阶段）和命令行界面实现 CoRT 的说明。 它包括用于安装（使用 pip 和 npm）、使用 OpenRouter API 密钥进行配置以及运行 Python 脚本的命令。

CoRT 的核心优势在于其自我评估、竞争性替代方案生成、迭代改进和动态思考深度。 作者鼓励通过 pull request 进行贡献，并根据 MIT 许可证授权该项目，允许广泛使用和修改。

---

## 17. Show HN: 用 Google Sheets 创建你自己的微调 AI 模型

**原文标题**: Show HN: Create your own finetuned AI model using Google Sheets

**原文链接**: [https://promptrepo.com/finetune/](https://promptrepo.com/finetune/)

这个“Show HN”帖子介绍了一个微调工具，允许用户直接使用来自 Google Sheets 的数据创建自定义 AI 模型。其核心价值主张是通过熟悉的界面使 AI 模型构建变得易于访问和准确，从而无需编码专业知识。

该工具提供多种功能，包括无需代码的 AI 模型创建、灵活选择 OpenAI、Mistral 或 LLaMA 进行训练和部署、通过 Sheets 公式或 API 轻松进行模型评估，以及构建用于分类、提取和生成任务的 AI 模型的能力。它还提供了一个 API，可以无缝集成到现有应用程序和工作流程中，以及内置的版本控制来管理微调过程。

除了微调工具外，该公司还提供一套增强 Google 表单的产品，包括 CRM 集成、电子签名收集、可填写 PDF 生成、带有支付选项的订单表单创建、用于表单组织的网站构建，以及针对特定行业（如膳食准备和在线食堂）的解决方案。

---

## 18. 什么是“诱发大气振动”？

**原文标题**: What Is "Induced Atmospheric Vibration"?

**原文链接**: [https://physics.stackexchange.com/questions/848666/what-is-induced-atmospheric-vibration](https://physics.stackexchange.com/questions/848666/what-is-induced-atmospheric-vibration)

本文探讨了伊比利亚半岛最近一次停电事故中“感应大气振动”这一概念。 该术语最初被认为是停电原因，但定义不明确，且缺乏现成的科学文献。 本文调查了可能的解释，考虑了温度变化、电晕放电、高压电力线路中的电抗以及这些因素的相互作用。

几位专家和用户参与了讨论，质疑“感应大气振动”作为主要原因的有效性。 一些人认为，温度变化会影响导线参数并产生频率不平衡，从而导致电网中出现级联断连。 另一些人则指出，现代电力系统可能存在建模缺陷，这些系统依赖于快速响应的基于逆变器的系统，这些系统可能因大气条件引起的意外电抗而变得不稳定。

最终，本文暗示“感应大气振动”的最初解释可能过于简单化，甚至是误称。 虽然大气条件会影响电网的行为，但停电很可能源于多种因素的复杂相互作用，包括电网设计、设备对频率波动的敏感性以及现代基于逆变器的系统的快速响应。 大气现象是停电原因的说法已被撤回。 专家讨论的其他潜在原因包括频率不平衡导致发电厂的级联断连。

---

## 19. 为什么常春藤盟校承受不起几亿的损失？

**原文标题**: Why can't Ivies cope with losing a few hundred million?

**原文链接**: [https://www.economist.com/briefing/2025/04/10/why-cant-stinking-rich-ivies-cope-with-losing-a-few-hundred-million](https://www.economist.com/briefing/2025/04/10/why-cant-stinking-rich-ivies-cope-with-losing-a-few-hundred-million)

2025年4月《经济学人》文章探讨了哥伦比亚大学为何在拥有150亿美元捐赠基金的情况下，无法轻易承担特朗普政府扣留的4亿美元联邦拨款损失。文章质疑，表面上资金充裕的精英大学，为何不能轻松应对看似较小的财务损失。虽然文中没有明确给出详细答案，但标题“现金匮乏”和副标题“巨额捐赠基金不易变现”暗示问题在于这些巨额捐赠基金的流动性不足。换句话说，虽然大学拥有大量资产，但这些资产可能无法立即转化为现金来弥补即时资金缺口。文章暗示，对于像哥伦比亚大学这样的机构而言，获取和利用捐赠基金来抵消联邦拨款损失面临着重大挑战。该文章是讨论唐纳德·特朗普与精英大学之间冲突的更广泛叙事的一部分。

---

## 20. 年轻人不如以前快乐 [全球繁荣研究]

**原文标题**: Young people aren't as happy as they used to be [Global Flourishing Study]

**原文链接**: [https://www.nytimes.com/2025/04/30/well/mind/happiness-flourishing-young-adult-study.html](https://www.nytimes.com/2025/04/30/well/mind/happiness-flourishing-young-adult-study.html)

全球幸福研究新发现：年轻人幸福感下降，或颠覆传统U型幸福曲线

---

## 21. 抵御当今网络威胁对网络安全公司的要求

**原文标题**: What It Takes to Defend a Cybersecurity Company from Today's Adversaries

**原文链接**: [https://www.sentinelone.com/labs/top-tier-target-what-it-takes-to-defend-a-cybersecurity-company-from-todays-adversaries/](https://www.sentinelone.com/labs/top-tier-target-what-it-takes-to-defend-a-cybersecurity-company-from-todays-adversaries/)

这份SentinelOne报告揭示了针对网络安全厂商攻击日益复杂化和多样化。报告结合自身经验，详细阐述了各种威胁，包括朝鲜IT人员寻求就业、勒索软件团伙开发绕过安全工具的能力，以及中国国家支持的黑客针对与其业务和客户群体相关的组织。

报告强调了跨职能协作在防御中的价值。他们能够利用招聘人员和客户成功团队来识别可疑活动。他们还对收到的许可申请进行自动化丰富和风险评分，以阻止高风险活动。

朝鲜IT人员活动涉及大规模渗透科技公司的行动，他们使用伪造的身份和改进的策略。SentinelOne通过与可疑申请者互动来收集情报，并与招聘团队合作以发现异常。像 Nitrogen 这样的勒索软件团伙通过冒充合法企业来获取 EDR 许可证，绕过了地下市场，这使他们能够测试、规避，并可能禁用安全保护。

报告强调了将所有访问途径（包括商业和运营渠道）视为攻击面的重要性，倡导在业务系统边缘集成检测逻辑，并促进不同团队之间的意识。他们建议，通过分享他们的经验，他们可以帮助改善集体防御并促进安全行业的合作。

---

## 22. 芬兰学校禁用智能手机

**原文标题**: Finland Bans Smartphones in Schools

**原文链接**: [https://yle.fi/a/74-20158886](https://yle.fi/a/74-20158886)

芬兰议会批准一项法律，限制中小学使用智能手机，该法律将于八月暑假结束后生效。该法律并非完全禁止手机，而是禁止在课堂时间使用手机，除非学生获得教师出于教育目的或健康原因的特别许可。学校教职员工也被授权没收扰乱教学或学习的设备。尽管有限制，但教育部长安德斯·阿德勒克鲁茨强调，数字技能发展仍将是优先事项。文章还指出，拥有Yle ID的用户可以对新闻报道发表评论，并参考相关指南和审核政策。

---

## 23. 研究人员正在研究如何最大限度地减少人类对公共土地的影响。

**原文标题**: Researchers are studying how to minimize human impact on public lands

**原文链接**: [https://undark.org/2025/04/28/keep-wild-places-wild/](https://undark.org/2025/04/28/keep-wild-places-wild/)

研究人员日益关注如何最大限度地减少人类活动对公共土地的影响，并在保护和可达性之间取得平衡。过去，土地管理机构依赖诸如游客人数上限和许可证之类的限制性措施。然而，现代方法优先考虑影响游客行为，通过间接管理策略来减少环境影响。

这包括诸如修建精心设计的步道以鼓励负责任的导航，以及采用基于社区的社会营销（CBSM）来识别和解决有损于保护的具体行为等策略。 CBSM利用调查和观察来了解游客为何可能偏离最佳实践，然后开发解决方案，例如步道改善，以鼓励环保行为。

虽然行为改变是首选，但研究人员承认，在某些情况下，为了保护脆弱的资源，使用限制可能是必要的。 当前的研究强调基于证据的决策，评估不同监管策略的有效性和公平性。 例如，预订系统可能会使某些群体（如农业工人）处于不利地位，从而促使人们需要更灵活的系统。

研究人员正在研究游客如何看待和回应这些管理方法，突出了就已实施系统的目标和程序进行清晰沟通的重要性。 总而言之，目标是找到能够让人们继续享受公共土地，同时最大限度地减少他们对环境的影响，并考虑政策决策的更广泛影响的策略。

---

## 24. 我的酸种酵母生了双胞胎。

**原文标题**: My sourdough starter has twins

**原文链接**: [https://brainbaking.com/post/2025/04/my-sourdough-starter-has-twins/](https://brainbaking.com/post/2025/04/my-sourdough-starter-has-twins/)

本文详细介绍了作者参与“公民科学酸面包项目”的经历。该项目由布鲁塞尔自由大学（VUB Brussels）和苏黎世联邦理工学院（ETH Zurich）发起，旨在收集和分析酸面包酵种样本。作为酸面包爱好者，作者提交了其酵种“臭臭”（Stinkie）的样本，最近收到了一份报告，详细说明了其微生物组成和特性与其他提交样本的比较情况。

报告显示，“臭臭”拥有“双胞胎”——在瑞士、罗马尼亚和芬兰发现的具有相似特征的酵种。报告还分析了“臭臭”的发酵偏好、酸度、年龄（估计为 11 年）以及所含的酵母菌和细菌的数量，发现它相对酸性较强，保存在较低的温度下，并且与平均水平相比，酵母菌和细菌含量较高。

详细的指纹分析表明，“臭臭”的细菌组成主要由短乳杆菌（Lactobacillus brevis，89.5%）构成，酵母组成几乎完全是酿酒酵母（Saccharomyces Cerevisiae，100%），这表明它尽管微生物总数很高，但仍属于单一培养。作者发现这既符合预期，又可能限制了风味的复杂性，并考虑尝试喂养方式以使微生物种类多样化。

最后，本文提到了一个“Dough-Pro”人工智能助手（本质上是 ChatGPT），用于帮助解释结果，并对“公民科学”的方法表示赞赏，在这种方法中，参与者为研究做出贡献并获得个性化的结果。

---

## 25. 黎巴嫩太空计划的教训 – Kasurian

**原文标题**: Lessons from the Lebanese Space Program – Kasurian

**原文链接**: [https://kasurian.com/p/lebanese-space-program](https://kasurian.com/p/lebanese-space-program)

本文讲述了黎巴嫩火箭协会 (LRS) 这一卓越但鲜为人知的故事。该协会是 20 世纪 60 年代由学生主导的一项倡议，成功地将火箭发射到太空，短暂地使黎巴嫩成为一个太空国家。LRS 由 Manoug Manougian 在贝鲁特的海加兹扬学院创立，凭借其聪明才智和奉献精神克服了资源有限的困难，赢得了民族自豪感，甚至引起了外国势力的关注。

在 Manougian 和平技术进步愿景的驱动下，LRS 开发了诸如 Cedar-4 之类的先进火箭，该火箭进入了近地轨道。然而，由于不断升级的地缘政治紧张局势、地区冲突以及国际大国对该技术潜在军事化的担忧，该计划面临着日益严峻的挑战。

Manougian 拒绝开发武器技术，而黎巴嫩军方对火箭军事应用的兴趣日益浓厚，这造成了利益冲突。最终，来自美国、法国和英国的外部压力导致该计划于 1967 年关闭，Manougian 前往美国。LRS 逐渐销声匿迹，并因黎巴嫩内战而更加模糊。

本文强调了如果该计划得以继续，黎巴嫩可能错失的机遇，包括潜在的工业发展、卫星技术的区域领导地位以及教育和基础设施的改善。它还强调了 Manougian 的远见卓识和他在黎巴嫩民族记忆中被抹去的悲剧，暗示他的理想主义可能无意中促成了该计划的消亡。2010 年代，黎巴嫩电影制作人重新挖掘了这个故事，使人们重新关注黎巴嫩历史上的这一非凡篇章。

---

## 26. Excel中的Linux

**原文标题**: Linux in Excel

**原文链接**: [https://github.com/NSG650/LinuxInExcel](https://github.com/NSG650/LinuxInExcel)

本文介绍了一个项目，作者让 Linux 在 Microsoft Excel 中运行，尽管是以一种有漏洞且“作弊”的方式。他们没有使用 VBA 或公式在 Excel 中完全重新创建一个模拟器，而是利用了一个现有的名为 mini-rv32ima 的模拟器。核心方法包括：

1. **使用 mini-rv32ima：** 这个现有的模拟器模拟 RV32IMA 指令集。
2. **构建 DLL：** 该模拟器被编译成一个单独的 DLL 文件，使用 MSVC（Microsoft Visual C++）。
3. **VBA 集成：** 使用 Excel VBA 宏来加载 DLL 并调用模拟器函数。
4. **数据传输：** VBA 宏从特定单元格 (C2) 获取输入并将其传递给模拟器。然后，模拟器的输出被写回电子表格单元格中。

作者承认该实现存在漏洞，并且没有针对性能或完全准确性进行优化，因为它主要是为了好玩而做的。该过程包括使用 `cl dllmain.c /LD /Fefun.dll` 将 `dllmain.c` 编译成 `fun.dll`，并更新 Excel 文件中 DLL 的路径。用户可以通过在单元格 C2 中输入文本来为模拟的 Linux 环境提供输入。

---

## 27. 导致里根国家机场致命坠机事故的失误

**原文标题**: The missteps that led to a fatal plane crash at Reagan National Airport

**原文链接**: [https://www.nytimes.com/2025/04/27/business/dc-plane-crash-reagan-airport.html](https://www.nytimes.com/2025/04/27/business/dc-plane-crash-reagan-airport.html)

2025年1月29日，里根国家机场发生一起悲惨空难，造成美国航空5342号航班上的全部64名乘客和一架陆军黑鹰直升机的机组人员丧生。这起事故是近四分之一世纪以来最严重的国内航空灾难，发生在波托马克河上空，直升机与飞机相撞。

文章强调了“目视间隔”的概念，这是一种常见的航空做法，飞行员在没有空中交通管制员指导的情况下独立地绕过其他飞机进行导航。黑鹰机组人员请求并被批准了目视间隔，但未能有效执行，要么错过了客机，要么无法安全机动。

文章强调，这次坠机并非由于单一错误，而是多种安全系统和冗余的崩溃。文章中的图表显示，直升机航线与使用33号跑道的飞机的飞行路线非常接近，如果直升机离河流东岸较远，则需要减少垂直间隔。

记者们查阅了政府文件和录音，并采访了专家。他们的调查表明，目视间隔的失效是一个促成因素，突出了航空领域一个已知的风险，但在这次事故中，它导致了灾难性的后果。

---

## 28. AI优先是新的重返办公室

**原文标题**: "AI-first" is the new Return To Office

**原文链接**: [https://www.anildash.com//2025/04/19/ai-first-is-the-new-return-to-office/](https://www.anildash.com//2025/04/19/ai-first-is-the-new-return-to-office/)

文章批判当前科技行业CEO强制推行“AI至上”的做法，将其与之前的“重返办公室”行动相提并论。作者认为，强迫员工使用AI，尤其是将其纳入绩效考核，是不必要，甚至是适得其反的。

作者认为，AI对那些在特定领域技能较差的人最有益。强迫高技能员工使用AI工具暗示了对他们能力的不信任，以及对技术应如何有机采用的误解。作者以自己的编程经验为例来说明这一点，指出AI工具帮助他们弥补了专业知识的不足，但未必能提高高技能开发人员的工作效率。

作者认为，“AI至上”的指令更多的是为了在科技公司CEO和风险投资圈内进行展示，而不是为了提高实际生产力。这些领导者正在进行群体思维，试图跟上最新潮流，往往以牺牲员工自主权和判断力为代价。更好的方法是提供安全、集成良好的AI工具，并允许员工根据自己的个人需求和工作流程选择是否以及如何使用它们。

作者倡导一种更加平衡和“正常”的技术采用方式，批评盲目推广初创企业并忽视其他行业创新的“技术乐观主义”。他们认为，如果AI工具确实有价值，那么自然会被那些发现它们有用的人所采用，而无需强制实施或夸大宣传。最终，作者预测这些AI指令将被用来评估CEO的领导能力，而不是员工的生产力。

---

## 29. 自动稀疏微分图解指南

**原文标题**: An illustrated guide to automatic sparse differentiation

**原文链接**: [https://iclr-blogposts.github.io/2025/blog/sparse-autodiff/](https://iclr-blogposts.github.io/2025/blog/sparse-autodiff/)

本文介绍了自动稀疏微分 (ASD)，这是一种通过利用机器学习中雅可比矩阵和海森矩阵的稀疏性（即大多数系数为零）来加速其计算的技术。虽然标准自动微分 (AD) 已被广泛使用，但由于 ASD 在机器学习研究生态系统之外发展，因此较不常见。

本文首先回顾了传统的 AD，包括用于雅可比矩阵计算的前向和反向模式，并强调使用无矩阵雅可比算子以避免显式存储大型中间雅可比矩阵。然后深入研究 ASD，解释其核心思想是用单个雅可比矩阵向量积 (JVP) 或向量雅可比矩阵积 (VJP) 计算雅可比矩阵的多个结构正交列（或行）。 这是可能的，因为雅可比算子是线性映射，并且结构正交列的总和可以被唯一分解。

由于雅可比矩阵的稀疏模式最初是未知的，因此 ASD 采用一个四步过程：1) 模式检测，以识别雅可比矩阵的稀疏结构。2) 着色算法，将正交列（或行）分组在一起。3) 压缩 AD，使用着色信息计算 JVP 或 VJP。4) 解压缩，将值分配给雅可比矩阵中的正确条目。通过避免对零元素进行不必要的计算，ASD 提供了显着的性能优势，尤其是在具有稀疏雅可比矩阵和海森矩阵的高维问题中。

---

## 30. 展示HN：Beatsync – 多设备完美音频同步

**原文标题**: Show HN: Beatsync – perfect audio sync across multiple devices

**原文链接**: [https://github.com/freeman-jiang/beatsync](https://github.com/freeman-jiang/beatsync)

Beatsync是一款基于网络的音频播放器，专为跨多设备精确同步播放而设计。它采用类似NTP的时间同步技术，拥有毫秒级精度，可在任何现代浏览器（推荐Chrome）上运行，并支持空间音频控制，用于创建有趣的声景。用户界面精致，加载流畅，状态指示清晰。

Beatsync可以自托管，并使用Turborepo构建。要开始使用，用户需要在`apps/client`目录中配置一个`.env`文件，其中包含API和WebSocket URL（通常指向`localhost:8080`）。该项目使用Bun进行包管理。运行一次`bun install`，然后运行`bun dev`，即可启动Next.js前端（端口3000）和基于Bun的HTTP和WebSocket服务器（端口8080）。

项目目录分为三个主要部分：`apps/server`（后端）、`apps/client`（Next.js前端）和`packages/shared`（用于共享的类型安全模式和函数）。官方Beatsync应用程序可在beatsync.gg上找到。虽然移动端支持尚处于实验阶段，但项目鼓励用户通过pull request报告问题或贡献开发。

---

## 31. Bamba：结合Transformer与SSM的开源LLM

**原文标题**: Bamba: An open-source LLM that crosses a transformer with an SSM

**原文链接**: [https://research.ibm.com/blog/bamba-ssm-transformer-model](https://research.ibm.com/blog/bamba-ssm-transformer-model)

本文介绍了Bamba，IBM研究院开发的一款开源混合大型语言模型（LLM），它结合了transformers和状态空间模型（SSM）的优势，以克服传统transformers的“二次方瓶颈”。 Transformers虽然有效，但由于其自注意力机制和存储KV（键值）缓存的需要，上下文长度增加会导致计算成本增加。 SSM通过维护一个压缩的“隐藏状态”来总结过去的信息，从而提供了一种解决方案，可以加快推理速度。

IBM实现的Bamba-9B证明了这种混合方法的潜力，它在实现与类似大小的transformers相当的精度的同时，运行速度至少快两倍，这是由于KV缓存的内存需求降低。 它建立在先前SSM研究的创新之上，包括Albert Gu和Tri Dao的工作，并利用了Mamba2架构。

IBM正在与红帽合作，将Bamba完全开源，包括训练配方、数据和量化框架，以优化vLLM的SSM。 早期基准测试表明，Bamba的性能与Meta的Llama-3.1 8B相当，尽管它的训练数据较少。 虽然目前Bamba是在4000个token的序列上训练的，并且能够处理32000个token的对话，但IBM的目标是将它的上下文窗口扩展到100万个token，并实现更快的推理速度。 其目标是为企业使用提供高效且易于访问的LLM，并促进社区驱动的改进。

---

## 32. 世界生成：用于游戏/VR/XR的开源3D场景生成器

**原文标题**: WorldGen: Open-source 3D scene generator for Game/VR/XR

**原文链接**: [https://worldgen.github.io/](https://worldgen.github.io/)

WorldGen是一款开源工具，可以通过文本提示或图像生成3D场景，适用于游戏开发、VR和XR应用。它允许用户在几秒钟内创建详细的3D环境。

主要特性包括：

*   **即时3D生成：** 从简单的文本提示快速创建3D场景。
*   **文本和图像输入：** 支持文本和图像输入进行场景生成。
*   **360°自由探索：** 支持对生成的场景进行一致的360°探索。

该过程分两个阶段进行：

1.  **全景图生成：** 根据输入生成高分辨率的360度全景图像。
2.  **全景图到场景转换：** 使用3DGS或网格表示将全景图转换为3D场景，从而可以从任何角度进行交互式探索。

文章包含大量从各种文本提示生成的场景示例，展示了该工具的多功能性。文章还鼓励用户尝试交互式演示，并访问GitHub仓库，开始构建自己的3D世界。

---

## 33. 性能优化很难，因为它本质上是一个蛮力任务。

**原文标题**: Performance optimization is hard because it's fundamentally a brute-force task

**原文链接**: [https://purplesyringa.moe/blog/why-performance-optimization-is-hard-work/](https://purplesyringa.moe/blog/why-performance-optimization-is-hard-work/)

性能优化本质上是一种蛮力任务，即使具备专业知识和可用工具，也极具挑战性。本文重点阐述了几个主要难点：

*   **可组合性：** 优化之间常常以不可预测的方式相互作用，需要对各种组合进行广泛测试，以避免负优化。

*   **连续性：** 许多优化涉及截止边界和参数，即使代码发生细微更改，也需要通过重新基准测试进行细致调整，以避免显著的性能损失。

*   **不兼容性：** 诸如缓存大小和寄存器压力等硬件限制可能会阻碍优化，迫使开发人员做出艰难的选择和妥协。

*   **编译器：** 尽管取得了进展，但编译器通常无法执行人类开发人员可以识别的高级抽象优化，而是专注于零成本抽象。它们也可能在寄存器分配方面做出糟糕的决策。开发人员必须分析反汇编代码和性能剖析数据，才能有效地指导编译器。

*   **文档：** 作者批评了像 Apple Silicon 这样的较新架构缺乏全面的文档，使得优化成为一项逆向工程任务。

作者总结说，性能优化需要探索无数的可能性，使用不完善的工具，并处理各种外部约束。尽管存在这些挑战，作者仍然认为这个过程是有价值的，并强调即使是很小的优化也会对用户体验和高效的资源利用产生累积影响。

---

## 34. 我们在首届LlamaCon大会上发布的所有内容

**原文标题**: Everything we announced at our first LlamaCon

**原文链接**: [https://ai.meta.com/blog/llamacon-llama-news/?_fb_noscript=1](https://ai.meta.com/blog/llamacon-llama-news/?_fb_noscript=1)

无法访问文章链接。

---

## 35. 美国第一季度经济萎缩0.3%

**原文标题**: U.S. Economy Contracts at 0.3% Rate in First Quarter

**原文链接**: [https://www.wsj.com/economy/us-gdp-q1-2025-1f82f689](https://www.wsj.com/economy/us-gdp-q1-2025-1f82f689)

无法访问文章链接。

---

## 36. 维基百科表示将使用人工智能，但不会取代人类志愿者。

**原文标题**: Wikipedia says it will use AI, but not to replace human volunteers

**原文链接**: [https://wikimediafoundation.org/news/2025/04/30/our-new-ai-strategy-puts-wikipedias-humans-first/](https://wikimediafoundation.org/news/2025/04/30/our-new-ai-strategy-puts-wikipedias-humans-first/)

本文概述了维基百科的全新人工智能战略，强调人工智能将被用于支持而非取代人类志愿者。其核心价值仍然是维基百科编辑在研究、审议和达成共识以创建可靠的百科知识方面的承诺和专业知识。

该战略侧重于利用人工智能消除技术障碍，并解放志愿者的时间，让他们能够从事更具影响力的工作。主要投资领域包括：

*   **支持版主和巡查员：** 自动化繁琐的任务，以提高知识的完整性。
*   **提高信息的可发现性：** 让编辑有更多时间进行审议、判断和达成共识。
*   **促进内容翻译和改编：** 帮助编辑分享当地观点。
*   **扩大志愿者招募规模：** 为新贡献者提供指导性的指导。

维基媒体基金会将优先考虑以人为本的方法、人的能动性、开源人工智能、透明度和多语种性来开发人工智能。他们的承诺与提供免费访问知识的核心使命相一致，在生成式人工智能时代，这一使命变得更加重要，因为生成式人工智能通常依赖维基百科的内容进行训练。本文引导读者访问Meta-Wiki以获取完整的人工智能战略。

---

## 37. It's School time: Adventures in hacking an old Kindle

**原文标题**: It's School time: Adventures in hacking an old Kindle

**原文链接**: [https://samkhawase.com/blog/hacking-kindle/](https://samkhawase.com/blog/hacking-kindle/)

生成摘要时出错

---

## 38. 不可能的任务：在现实世界中管理人工智能体

**原文标题**: Mission Impossible: Managing AI Agents in the Real World

**原文链接**: [https://medium.com/gitconnected/mission-impossible-managing-ai-agents-in-the-real-world-f8e7834833af](https://medium.com/gitconnected/mission-impossible-managing-ai-agents-in-the-real-world-f8e7834833af)

生成摘要时出错

---

## 39. Show HN: A Chrome extension that will auto-reject non-essential cookies

**原文标题**: Show HN: A Chrome extension that will auto-reject non-essential cookies

**原文链接**: [https://blog.bymitch.com/posts/reject-cookies/](https://blog.bymitch.com/posts/reject-cookies/)

This article introduces "Reject Cookies," a Chrome extension designed to automatically reject non-essential cookies on websites, addressing the universal frustration of cookie consent banners. While existing extensions auto-accept cookies or block trackers, "Reject Cookies" aims for compliance by explicitly rejecting non-essential cookies or, failing that, closing the consent banner.

The extension works by identifying common cookie consent vendors (like OneTrust) and targeting their specific implementations. It first attempts to click the "reject all" button if available. If not, it removes the entire consent banner. The code is open source and available on GitHub.

The author details their development process, highlighting the use of the Cursor AI coding assistant, which initially provided helpful boilerplate but required manual adjustments for permissions and vendor-specific logic. The extension utilizes a targeted approach, focusing on specific consent providers rather than broad selectors.

"Reject Cookies" is still under development and welcomes user feedback to improve its coverage of different vendor implementations and report bugs. Users can report missed cookie consent requests or other issues via the side panel in Chrome or by email. The goal is to automate the process of rejecting non-essential cookies, improving user experience and privacy online.


---

## 40. Secret Deals, Foreign Investments: The Rise of Trump’s Crypto Firm

**原文标题**: Secret Deals, Foreign Investments: The Rise of Trump’s Crypto Firm

**原文链接**: [https://www.nytimes.com/2025/04/29/us/politics/trump-crypto-world-liberty-financial.html](https://www.nytimes.com/2025/04/29/us/politics/trump-crypto-world-liberty-financial.html)

生成摘要时出错

---

## 41. 我用zip炸弹来保护我的服务器。

**原文标题**: I use zip bombs to protect my server

**原文链接**: [https://idiallo.com/blog/zipbomb-protection](https://idiallo.com/blog/zipbomb-protection)

使用zip炸弹防御恶意网络爬虫：本文介绍了如何使用zip炸弹防御针对网络服务器的恶意爬虫。作者解释说，许多爬虫（包括恶意的）支持gzip压缩以最大限度地提高网络爬行时的带宽。他们利用这一点，通过检测潜在的有害爬虫活动（例如，漏洞扫描，重复的垃圾邮件尝试），并使用压缩的zip炸弹而不是请求的内容来响应。

zip炸弹是一个小文件，解压缩后会变成一个非常大的文件，使爬虫的资源不堪重负并导致崩溃。作者提供了一个使用`dd`和`gzip`创建zip炸弹的命令行指令。他们解释说，他们在服务器上使用中间件来识别恶意请求，并提供1MB或10MB的zip炸弹，分别解压缩为1GB或10GB。代码片段提供了一个使用PHP实现此功能的示例。

作者承认zip炸弹并非万无一失，可以被规避，但对盲目爬行的不复杂的爬虫有效。该文章包含一个免责声明，说明创建zip炸弹时可能会导致自己的设备崩溃。最后，作者分享了一些其他的想法，链接，并邀请用户在评论区分享他们的想法。

---

## 42. 编程语言应具备树遍历原生功能。

**原文标题**: Programming languages should have a tree traversal primitive

**原文链接**: [https://blog.tylerglaiel.com/p/programming-languages-should-have](https://blog.tylerglaiel.com/p/programming-languages-should-have)

泰勒·格莱尔认为，编程语言缺少一种用于树遍历的基本控制流结构，类似于线性数据结构的 `for` 或 `foreach` 循环。他提出了一个 `for_tree` 结构来填补这一空白，与递归函数实现相比，它可以简化常见的树操作并减少错误。

`for_tree` 循环模仿了传统 `for` 循环的语法，具有 `init`、`condition` 和 `branch` 部分。`branch` 部分动态生成用于遍历的子节点。格莱尔用类似 C++ 的示例来说明这一点，展示了 `for_tree` 如何遍历二叉树的节点，并打印它们的值。

他强调了可读性、减少样板代码以及在循环体中使用 `break`、`continue` 和一个新的 `prune` 语句等优点。`Prune` 允许根据特定节点属性提前终止子树探索，从而提高效率。

文章还讨论了基于范围的 for 循环的局限性，尤其是在处理隐式树（例如，递归生成字符串）或需要剪枝时。虽然可能存在广度优先搜索 (BFS) 变体，但作者优先考虑深度优先搜索 (DFS) 的简单性和栈友好性作为原始结构。

格莱尔最后通过回应现有迭代器已经足够的观点来总结，强调了抽象树遍历的强大功能，这对于在许多编程场景中发现的隐式树状关系（超越显式树数据结构）非常重要。他提供了一个使用模板和宏的 C++ 概念验证实现，以证明该概念的可行性。

---

## 43. 互联网是如何抛弃4chan的

**原文标题**: How the Internet Left 4chan Behind

**原文链接**: [https://www.newyorker.com/culture/infinite-scroll/how-the-internet-left-4chan-behind](https://www.newyorker.com/culture/infinite-scroll/how-the-internet-left-4chan-behind)

本文探讨了4chan的兴衰，追溯了其作为匿名在线论坛的起源，用户可以在此分享未经审查的内容，包括色情作品、盗版文件和有争议的观点。作者回顾了他们早期使用该网站的经历，以及它在塑造互联网“垃圾信息”、表情包和在线贬低文化方面的作用。

虽然4chan曾经作为政治不正确、仇视女性文化和极端主义意识形态的避风港占据着独特的地位，但本文认为，随着类似内容在其他平台（包括Truth Social、Parler和X）上的扩散，其影响力已经减弱。这些新网站的内容审核政策有所放松，允许阴谋论和图像内容的存在，从而将4chan推向了边缘。

作者强调了4chan的实时抬杠行为如何根植于网络环境中，影响了X、TikTok和视频播客等平台。甚至像白宫这样的官方账号也采用了钓鱼巨魔的方式，表明了4chan的极端文化所产生的普遍影响。

本文还提到了4chan最近的黑客攻击和服务器问题，揭示了其老化的基础设施和脆弱性。最终，文章认为，虽然4chan可能会以某种形式继续存在，但它曾经助长的极端主义现在正在Discord、Telegram和Signal等私人数字领域中发生，这使得追踪变得更加困难。文章最后断言，4chan的敏感性依然存在，塑造着在线讨论，并反映了我们集体数字意识中的一个黑暗角落。

---

## 44. 我们需要更多乐观的科幻小说。

**原文标题**: We need more optimistic science fiction

**原文链接**: [https://craig-russell.co.uk/blog/2024-10-24-optimistic-sci-fi/](https://craig-russell.co.uk/blog/2024-10-24-optimistic-sci-fi/)

克雷格在他的文章中认为，科幻小说有责任摆脱当前的反乌托邦焦点，重燃对未来的乐观情绪。他观察到，这一类型曾经是太空竞赛等进步的灵感来源，但现在却被警示故事所主导，这些故事反映了现实世界的问题，导致了一种绝望感。

克雷格从J.R.R.托尔金将逃避现实视为一种“责任”以及米尔顿·弗里德曼使“政治上不可能”变为“政治上不可避免”的理念中汲取灵感，倡导科幻小说呈现新的、积极的未来愿景。他认为，通过探索和推广这些想法，科幻小说可以帮助将它们确立为对当前面临危机的政治和经济体系的可行替代方案。

克雷格强调，这并非倡导特定的政治意识形态，而是培养一种对更美好世界的希望和雄心壮志的文化。他敦促作家和读者想象他们渴望的未来，充满激情和爱地分享他们乐观的愿景，并最终激发创造更光明现实的灵感。他呼吁科幻小说像激发我们登上月球一样，激励我们热爱未来并实现它。

---

## 45. 只有特斯拉因符合85%国产化率规定而免受新的汽车关税影响

**原文标题**: Only Teslas exempt from new auto tariffs thanks to 85% domestic content rule

**原文链接**: [https://fuelarc.com/cars/only-tesla-exempt-from-new-auto-tariffs-thanks-to-85-domestic-content-rule/](https://fuelarc.com/cars/only-tesla-exempt-from-new-auto-tariffs-thanks-to-85-domestic-content-rule/)

本文片段呈现两个不同的信息：

1. **特斯拉免受汽车关税影响：** 主要标题表明，由于满足 85% 的国产化率规则，特斯拉汽车能够独特地避免新的汽车关税。 这暗示其他汽车制造商很可能需要缴纳这些关税。

2. **Waymo-丰田合作：** 第二部分详细介绍了 Waymo 和丰田之间的合作关系。 此次合作开启了 Waymo 直接向消费者销售自动驾驶汽车的可能性，暗示了 Waymo 战略的转变，可能超越网约车服务。 2025 年 4 月 30 日这个日期可能代表与此次合作相关的截止日期或里程碑，尽管该片段并未明确说明这一点。 我们还了解到，Alphabet 首席执行官 Sundar Pichai 在一次财报电话会议中暗示了 Waymo 未来的可能性。

---

## 46. BSSG – 我从动态CMS到bash静态站点生成器的旅程

**原文标题**: BSSG – My journey from dynamic CMS to bash static site generator

**原文链接**: [https://it-notes.dragas.net/2025/04/07/launching-bssg-my-journey-from-dynamic-cms-to-bash-static-site-generator/](https://it-notes.dragas.net/2025/04/07/launching-bssg-my-journey-from-dynamic-cms-to-bash-static-site-generator/)

本文记录了作者从使用WordPress等动态CMS系统到开发和拥抱静态站点生成器的历程。由于对动态CMS系统需要不断进行安全更新感到沮丧，作者发现了静态站点生成器，并尝试了bashblog、Pelican和Nikola。

出于对定制化解决方案的着迷和渴望，作者创建了BSSG（Bash静态站点生成器）。BSSG最初是为个人使用而设计的，但随着主题支持、归档和标签等功能的加入而不断发展。虽然尝试过一个基于Python的替代方案ITNBlog，但它停滞不前，这促使作者重振BSSG以供更广泛的使用。

作者最终决定将此博客切换到ITNBlog，并发布BSSG，强调了其可移植性、简单的主题（基于CSS）、基本功能（RSS、站点地图、OpenGraph、国际化）、内置备份、最小依赖项、Markdown支持、可选的GNU Parallel集成、高可访问性/性能得分以及BSD许可证。还包含一个脚本，用于使用可用主题测试站点。文章提到了一个实验性的管理界面（Node Express），可能在未来发布。发布BSSG的核心动机是为静态网站提供动态CMS系统的替代方案。

---

## 47. ArkFlow: 高性能 Rust 流处理引擎

**原文标题**: ArkFlow: High-performance Rust stream processing engine

**原文链接**: [https://github.com/arkflow-rs/arkflow](https://github.com/arkflow-rs/arkflow)

ArkFlow：Rust 高性能开源流处理引擎。它旨在以低延迟和高吞吐量处理实时数据流。主要特性包括：

*   **性能：** 基于 Rust 和 Tokio 构建，速度快效率高。
*   **多种数据源：** 支持 Kafka、MQTT、HTTP、文件（CSV、JSON、Parquet、Avro、Arrow）、数据库（MySQL、PostgreSQL、SQLite、DuckDB）和数据生成器作为输入；Kafka、MQTT、HTTP、标准输出和 Drop 作为输出。
*   **强大的处理能力：** 提供内置的 SQL 查询、JSON 处理、Protobuf 编码/解码和批处理。
*   **可扩展性：** 模块化设计使其可以轻松扩展自定义输入、输出和处理器组件。

该引擎使用 YAML 配置文件来定义数据流，包括输入源、处理管道和输出目标。管道可以配置指定数量的线程。ArkFlow 还支持错误输出流，用于处理处理过程中的错误。为了管理反压，它提供了内存缓冲区组件。

本文档包含 Kafka 到 Kafka 数据处理和生成测试数据的配置示例。该项目采用 Apache 2.0 许可，并鼓励通过 Discord 进行社区互动。

---

## 48. Dataframely: 一个原生 Polars 的数据框验证库

**原文标题**: Dataframely: A polars-native data frame validation library

**原文链接**: [https://tech.quantco.com/blog/dataframely](https://tech.quantco.com/blog/dataframely)

Dataframely是由QuantCo创建的一个新的、原生于Polars的数据框验证库，旨在解决现有解决方案（如pandera和patito）中的局限性。这些局限性包括缺乏对相互依赖的数据框验证、带有失败内省的软验证、测试数据生成以及严格静态类型的支持。

Dataframely提供了一种声明式方法来定义数据框模式，包括列类型、约束（例如，主键）和使用Polars表达式的跨列验证规则。它允许使用`validate`（对无效行引发异常）和`filter`（返回有效行和用于内省的失败信息）进行验证。

一个关键特性是能够定义“集合”来表示和验证相互依赖的数据框，应用跨多个由公共键链接的数据框的规则。Dataframely还通过向数据框类型提示添加模式信息来增强代码的可读性和可维护性。这改善了使用mypy的静态类型检查。

除了验证之外，Dataframely还支持基于定义的模式自动生成SQL模式和用于单元测试的示例数据。QuantCo已成功将dataframely集成到其数据管道中，并报告了代码可读性、健壮性和可测试性的提高。他们现在已将其开源，鼓励社区反馈。

---

## 49. Firefox标签页分组功能已上线

**原文标题**: Firefox tab groups are here

**原文链接**: [https://blog.mozilla.org/en/firefox/tab-groups-community/](https://blog.mozilla.org/en/firefox/tab-groups-community/)

Firefox发布标签页组，一项应用户呼声而生的功能

Firefox发布了标签页组，这是一项在Mozilla Connect上根据用户反馈而产生、备受期待的功能。文章重点介绍了Firefox团队与社区在开发该功能上的协作历程。在Mozilla Connect上，用户对标签页组的请求迅速成为最受赞同的建议后，Firefox团队积极采纳用户反馈，追踪趋势并了解每项请求背后的根本需求。

产品经理Stefan Smagula强调每天阅读反馈以了解社区的需求，这些需求塑造了最终产品。标签页组允许用户组织标签页、为其添加标签并保持专注，使简约主义者和高级用户均能受益。

文章还讨论了“智能标签页组”的持续开发，这是一项由人工智能驱动的功能，可建议标签页组名称并自动组织标签页，同时通过将数据保留在设备上来优先考虑用户隐私。Stefan Smagula指出，智能标签页组改进了他的工作流程，并使查找和恢复任务变得更加容易。Firefox团队鼓励用户尝试标签页组，并在Mozilla Connect上继续分享反馈。总的基调是庆祝性的，并强调社区参与在Firefox开发中的重要性。

---

## 50. 新型量子GPS备份系统精度是替代方案的50倍

**原文标题**: New Quantum GPS Backup Is 50 Times More Precise Than Alternatives

**原文链接**: [https://singularityhub.com/2025/04/24/new-quantum-gps-backup-is-50-times-more-precise-than-state-of-the-art-alternatives/](https://singularityhub.com/2025/04/24/new-quantum-gps-backup-is-50-times-more-precise-than-state-of-the-art-alternatives/)

澳大利亚初创公司Q-CTRL开发了一种基于量子传感器的GPS备份系统，其精度是目前惯性导航系统的50倍。该技术利用量子磁力计探测地球磁场中的微小变化，即使在GPS信号不可用或受到干扰的情况下，也能高精度地确定位置。

该系统通过将磁场波动与详细地图进行比较来克服GPS的局限性，从而确定车辆的位置。为了对抗电磁干扰，Q-CTRL集成了机器学习软件，可以过滤掉磁噪声。在测试中，该设备在300英里的飞行中将精度保持在几百码范围内，明显优于惯性导航系统和其他备份方法，如多普勒雷达和激光雷达。

虽然该技术需要详细的磁场地图和突出的磁性地标才能达到最佳性能，但其精度和缺乏可探测信号使其对国防和航空航天实体具有吸引力。Q-CTRL正在与澳大利亚、美国和英国的国防部门以及空中客车公司合作开发这些量子导航系统。

---

## 51. LibreLingo – Duolingo的FOSS替代品

**原文标题**: LibreLingo – FOSS Alternative to Duolingo

**原文链接**: [https://librelingo.app](https://librelingo.app)

LibreLingo是一个开源、社区驱动的语言学习平台，旨在成为Duolingo的替代品。它被描述为一个“实验”，并重点介绍了多种语言的可用课程，包括西班牙语、德语、法语、孟加拉语、中古波斯语、巴斯克语、拉迪诺语（面向英语、希伯来语和西班牙语使用者）以及侯马语（面向英语使用者）。

该平台提供“开发文档”（目前仅提供英语版本）和“开发工具”，表明其重点在于社区贡献和项目开发。

LibreLingo由Dániel Kántor和众多贡献者创建，其源代码以AGPL-3.0许可协议发布。这种许可选择强化了其作为免费和开源项目的承诺。本质上，它是一个专注于社区开发和开放访问的语言学习项目。

---

## 52. 科学家揭示人类前所未见的全新颜色“奥洛”

**原文标题**: Scientists Unveil "Olo," a Brand-New Color Humans Have Never Seen Before

**原文链接**: [https://scitechdaily.com/scientists-unveil-olo-a-brand-new-color-humans-have-never-seen-before/](https://scitechdaily.com/scientists-unveil-olo-a-brand-new-color-humans-have-never-seen-before/)

无法访问文章链接。

---

## 53. Show HN: AgenticSeek – 云端AI工具的自托管替代方案

**原文标题**: Show HN: AgenticSeek – Self-hosted alternative to cloud-based AI tools

**原文链接**: [https://github.com/Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek)

AgenticSeek：一款本地自托管的AI助手，是Manus AI等云端AI工具的替代方案。它支持语音交互，完全在用户本地硬件上运行，无需依赖云端，也不会共享数据，从而保障隐私。

主要功能包括：

*   **本地且私密：** 您的数据不会离开您的设备。
*   **智能网页浏览：** 自动网页搜索、信息提取和表单填写。
*   **自主编程：** 多种语言的代码编写、调试和执行。
*   **智能代理选择：** 自动选择最适合给定任务的代理。
*   **任务规划与执行：** 将复杂任务分解为易于管理的步骤。
*   **语音支持：** 支持语音转文本和文本转语音交互。

该项目正在积极开发中，并寻求开源贡献者。安装需要Docker、Python 3.10+和兼容的Chrome驱动。该项目通过Ollama和LM Studio等提供商支持本地LLM，并集成了OpenAI和Deepseek等云API。文档提供了详细的设置、配置和使用说明，包括选择提供商、故障排除和硬件要求（建议使用Deepseek 14B或更大的模型）。文档强调了Deepseek R1在推理和工具使用方面的优势。文档包含关于虚构演示文件的免责声明，并号召贡献者。

---

## 54. 中国临床试验的蓬勃发展

**原文标题**: China's Clinical Trial Boom

**原文链接**: [https://www.asimov.press/p/china-trials](https://www.asimov.press/p/china-trials)

阿西莫夫出版社文章《中国的临床试验繁荣》 (作者：Hiya Jain) 探讨了中国发起的临床试验数量的显著增长，从 2017 年的 600 多项增加到 2023 年的近 2000 项。 这种激增与美国临床试验数量的停滞形成对比。

文章将中国的增长归因于精简审批和降低新药市场准入壁垒的政策改革，包括优先审评、有条件批准以及允许监管机构在 60 天内未提出异议的情况下自动授权的“默示许可”政策。 中国还加入了国际人用药品注册技术协调理事会 (ICH)，并开始接受海外临床试验数据，从而减少了重复研究的需要。 安进公司的 XGEVA 的批准就是例证。

这种效率促使国际投资增加，以及源自中国的原创新药数量的增加，正接近美国的总量。 此外，中国公司越来越多地在以较低成本在中国进行初步（I 期）试验后，将分子授权给西方制药公司。

作者认为，中国的监管改革为药物开发创造了一个更快、更便宜的环境，从而促进了中国生物制药生态系统更高的学习效率。 虽然承认美国系统在药物开发中的开创性作用，但文章主张美国进行改革，通过扩大 Medicaid 覆盖范围、简化文书工作和允许公平补偿来“普及”临床研究。 这受到了“临床试验丰富倡议”的启发。 文章还强调，那些调整框架以加快启动时间、认可可信的外国数据以及在充分监督和创新友好政策之间取得平衡的国家，将有望抓住下一波药物发现的浪潮。

---

## 55. Finding paths of least action with gradient descent (2023)

**原文标题**: Finding paths of least action with gradient descent (2023)

**原文链接**: [https://greydanus.github.io/2023/03/05/ncf-tutorial/](https://greydanus.github.io/2023/03/05/ncf-tutorial/)

生成摘要时出错

---

## 56. Art of the Hedgerow

**原文标题**: Art of the Hedgerow

**原文链接**: [https://engelsbergideas.com/notebook/the-art-of-the-hedgerow/](https://engelsbergideas.com/notebook/the-art-of-the-hedgerow/)

生成摘要时出错

---

## 57. 树篱的艺术

**原文标题**: Art of the Hedgerow

**原文链接**: [https://engelsbergideas.com/notebook/the-art-of-the-hedgerow/](https://engelsbergideas.com/notebook/the-art-of-the-hedgerow/)

理查德·尼格斯《树篱的艺术》探索了英国树篱的动态历史及其在艺术中的反映，认为它们的存在始终受社会经济力量的影响，而非二战前静态的生物多样性理想。他挑战了二战后树篱持续衰退的说法，断言自至少公元前2500年以来，树篱就随着农业需求和经济环境而波动。

尼格斯利用体育艺术来说明这一点。他将约翰·费恩利的1820年代绘画作品（描绘了经济衰退的乡村和稀疏的树篱）与罗伯特·迪顿1796年的铜版腐蚀凹版画（展示了农业革命时期繁荣、树篱茂密的农田）进行了对比。这些艺术品表明，树篱的密度和维护反映了当时的经济状况和农业实践。

在承认二战后因农业合理化导致的树篱损失的同时，尼格斯强调这并非孤立事件。他总结说，包括树篱在内的英国景观是人为的、不断变化的构造，深受政府政策决定的影响。该文章告诫人们不要美化战前固定的景观，强调了人为干预、农业需求和乡村视觉表现之间持续的相互作用。

---

## 58. Signal聊天记录泄露与美国国家安全局

**原文标题**: The Signal Chat Leak and the NSA

**原文链接**: [https://www.schneier.com/blog/archives/2025/03/the-signal-chat-leak-and-the-nsa.html](https://www.schneier.com/blog/archives/2025/03/the-signal-chat-leak-and-the-nsa.html)

生成摘要时出错

---

## 59. Show HN: 二维码纠错的交互式演示

**原文标题**: Show HN: An interactive demo of QR codes' error correction

**原文链接**: [https://qris.cool](https://qris.cool)

This "Show HN" post introduces an interactive demo showcasing the error correction capabilities of QR codes. The key takeaway is that QR codes are designed with built-in redundancy, allowing them to be successfully scanned even when damaged or partially obscured. The demo invites users to explore this feature by interacting with QR codes in one of three ways: selecting from pre-existing codes, scanning their own, or uploading an image/URL of a QR code. The interactive nature of the demo suggests that users can see firsthand how much damage a QR code can sustain and still be read, demonstrating the robustness provided by its error correction. Essentially, the post aims to educate users about the resilience of QR codes through a hands-on experience.


---

## 60. Duolingo will replace contract workers with AI

**原文标题**: Duolingo will replace contract workers with AI

**原文链接**: [https://www.theverge.com/news/657594/duolingo-ai-first-replace-contract-workers](https://www.theverge.com/news/657594/duolingo-ai-first-replace-contract-workers)

生成摘要时出错

---

## 61. Try Switching to Kagi

**原文标题**: Try Switching to Kagi

**原文链接**: [https://daringfireball.net/2025/04/try_switching_to_kagi](https://daringfireball.net/2025/04/try_switching_to_kagi)

生成摘要时出错

---

## 62. 空中传播：AirPlay协议中可蠕虫式传播的零点击远程代码执行漏洞

**原文标题**: AirBorne: Wormable zero-click remote code execution (RCE) in AirPlay protocol

**原文链接**: [https://www.oligo.security/blog/airborne](https://www.oligo.security/blog/airborne)

Oligo安全研究公司发现了苹果AirPlay协议和SDK中的一组漏洞，名为“AirBorne”，可能影响数十亿设备。这些漏洞可实现一系列攻击，包括零点击和一点击远程代码执行 (RCE)、ACL绕过、任意文件读取、敏感信息泄露、中间人攻击 (MITM) 和拒绝服务 (DoS)。

其中最关键的发现是影响MacOS和第三方AirPlay SDK设备的可蠕虫式零点击RCE漏洞（CVE-2025-24252和CVE-2025-24132），允许攻击者在本地网络上传播恶意软件，无需用户交互。例如，公共WiFi上的受感染设备可能会危及公司网络上的其他设备。文章重点介绍了MacOS、AirPlay SDK设备和CarPlay的具体RCE场景，详细说明了利用所需的条件。

Oligo向苹果披露了23个漏洞，产生了17个CVE。苹果已发布软件更新来解决这些问题，并在整个负责任披露过程中与Oligo合作。文章还提到了其他攻击途径，例如ACL绕过，这增加了AirBorne的严重性。

---

## 63. Optimizing eBPF I/O latency accounting when running 37M IOPS, on 384 CPUs

**原文标题**: Optimizing eBPF I/O latency accounting when running 37M IOPS, on 384 CPUs

**原文链接**: [https://tanelpoder.com/posts/optimizing-ebpf-biolatency-accounting/](https://tanelpoder.com/posts/optimizing-ebpf-biolatency-accounting/)

生成摘要时出错

---

## 64. Indian court orders blocking of Proton Mail

**原文标题**: Indian court orders blocking of Proton Mail

**原文链接**: [https://techcrunch.com/2025/04/29/indian-court-orders-blocking-of-proton-mail/](https://techcrunch.com/2025/04/29/indian-court-orders-blocking-of-proton-mail/)

生成摘要时出错

---

## 65. O3 beats a master-level GeoGuessr player, even with fake EXIF data

**原文标题**: O3 beats a master-level GeoGuessr player, even with fake EXIF data

**原文链接**: [https://sampatt.com/blog/2025-04-28-can-o3-beat-a-geoguessr-master](https://sampatt.com/blog/2025-04-28-can-o3-beat-a-geoguessr-master)

生成摘要时出错

---

## 66. 共和党欲在新交通法案中向电动车车主征收每年200美元的税。

**原文标题**: Republicans want to tax EV drivers $200/year in new transport bill

**原文链接**: [https://arstechnica.com/cars/2025/04/republicans-want-to-tax-ev-drivers-200-year-in-new-transport-bill/](https://arstechnica.com/cars/2025/04/republicans-want-to-tax-ev-drivers-200-year-in-new-transport-bill/)

众议院共和党人提出的一项交通法案包含一项新的年度联邦机动车辆登记费，该费用对电动汽车 (EV) 和混合动力汽车驾驶员的影响尤为明显。纯电动汽车每年将被征收 200 美元的税，而混合动力汽车则需缴纳 100 美元。大型污染卡车的车主缴纳的费用将大大减少，并且要到 2030 年才会开始征收。这些费用将随着通货膨胀每年增加，直至 2034/2035 年，而商用和农用车辆则可免除。

该法案旨在解决公路信托基金的资金缺口问题，预计到 2035 年可增加 1100 亿美元的收入，但批评人士认为，其他减税和支出计划仍将导致该基金短缺 2220 亿美元。拒绝征收新费用的州可能会损失联邦交通运输资金中相当于预计收入 125% 的资金。

共和党主席萨姆·格雷夫斯声称，这些费用是为了公平起见，以确保电动汽车驾驶员为公路维护做出贡献。然而，包括塞拉俱乐部在内的批评人士认为，该法案惩罚了更清洁的车辆，破坏了清洁交通运输举措，并将亿万富翁的减税置于公众健康和环境问题之上。他们主张鼓励电动汽车的普及，而不是征收惩罚性费用。作者还指出，许多州已经对电动汽车征收注册费，并且该法案暗示了联邦汽油税可能终结。

---

## 67. 通义千问3：思深行敏

**原文标题**: Qwen3: Think deeper, act faster

**原文链接**: [https://qwenlm.github.io/blog/qwen3/](https://qwenlm.github.io/blog/qwen3/)

Qwen3发布：通义千问最新大语言模型，包含大型MoE模型(Qwen3-235B-A22B, Qwen3-30B-A3B)和稠密模型(Qwen3-32B, Qwen3-14B, Qwen3-8B, Qwen3-4B, Qwen3-1.7B, 和Qwen3-0.6B)，全部以Apache 2.0许可证开放权重。Qwen3在代码、数学和通用能力方面表现强劲，超越或匹敌DeepSeek-R1、Grok-3和Gemini-2.5-Pro等模型。

关键特性是其混合思维模式，提供用于复杂推理的“思考模式”和用于快速响应的“非思考模式”，允许用户控制模型的计算推理预算。Qwen3还拥有广泛的多语言支持，覆盖119种语言和方言。

该模型的能力已针对编码和Agent应用进行了优化，包括加强了对MCP的支持。Qwen3在119种语言的36万亿个tokens上进行了预训练，这些tokens来自网络数据、PDF文档和Qwen2.5模型生成的合成数据。预训练过程包括三个阶段，侧重于基本语言技能、知识密集型数据和长上下文处理。

后训练涉及四阶段流程，以开发混合思维模型，包括长链思维冷启动、基于推理的强化学习、思考模式融合和通用RL。通过SGLang和vLLM等框架支持部署，并推荐Ollama和LMStudio等工具用于本地使用。使用`/think`和`/no_think`的软开关机制允许用户在多轮对话中控制思维模式。建议使用Qwen-Agent来利用Qwen3的工具调用能力。未来的工作旨在进一步提升模型在追求AGI和ASI方面的能力。

---

## 68. 美国经济第一季度萎缩

**原文标题**: U.S. Economy Shrank in First Quarter

**原文链接**: [https://www.nytimes.com/2025/04/30/business/us-economy-gdp-tariffs.html](https://www.nytimes.com/2025/04/30/business/us-economy-gdp-tariffs.html)

美国经济今年第一季度出现萎缩，据商务部数据显示，年化下降率为0.3%。这一经济逆转归因于特朗普总统的贸易政策所带来的不确定性，包括关税公告和政策转变。

虽然表面上的下降部分是由于衡量偏差，但它反映了特朗普政策的实际影响。消费者赶在关税生效前购买商品，企业囤积原材料以应对贸易战。这种行为扭曲了经济数据，给人以衰退的表象。

文章强调，这份经济快照是在四月份宣布进一步、更广泛的关税*之前*发生的，随后局势升级为与中国的全面贸易战，并引发金融市场动荡。消费者支出和企业投资的数据表明，第一季度经济增速放缓，但并未出现萎缩。

---

## 69. Widespread power outage in Spain and Portugal

**原文标题**: Widespread power outage in Spain and Portugal

**原文链接**: [https://www.bbc.com/news/live/c9wpq8xrvd9t](https://www.bbc.com/news/live/c9wpq8xrvd9t)

西班牙和葡萄牙大范围停电，扰乱日常生活，引发原因调查。西班牙和葡萄牙政府均排除网络攻击的可能性。西班牙已成立调查委员会，葡萄牙已向欧盟机构申请独立审计。

西班牙首相佩德罗·桑切斯表示，政府将调查所有潜在原因，而BBC的气候和科学团队正在考虑与可再生能源的关联。

停电导致严重的交通中断，西班牙和葡萄牙机场数百架航班被取消。文章还强调了受影响者的个人经历，从滞留数小时的旅客到找到创造性方法应对黑暗的个人。

虽然直播报道已经结束，但BBC仍在继续报道情况，更多更新可在BBC新闻上获取，包括关于西班牙排除网络攻击、停电后恢复正常以及随之而来的交通混乱的报道。

---

## 70. 佛罗里达州通过全州自来水禁氟令

**原文标题**: Statewide fluoride ban for tap water passes in Florida

**原文链接**: [https://www.miamiherald.com/news/local/community/miami-dade/article305335416.html](https://www.miamiherald.com/news/local/community/miami-dade/article305335416.html)

无法访问文章链接。

---

## 71. 哥伦比亚黑人砍刀击剑的最后大师

**原文标题**: The last masters of Afro-Colombian machete fencing

**原文链接**: [https://globalvoices.org/2025/04/19/the-last-masters-of-afro-colombian-machete-fencing-fight-to-save-their-tradition/](https://globalvoices.org/2025/04/19/the-last-masters-of-afro-colombian-machete-fencing-fight-to-save-their-tradition/)

这段简短的文字片段突出了两条不同的新闻。

首先，它引用了一篇题为《哥伦比亚非洲裔弯刀击剑的最后大师》的文章，表明这是一篇关于保护这项传统武术的文章。该文章可能探讨了哥伦比亚非洲裔弯刀击剑的文化意义、历史以及潜在的衰落，或许会重点关注那些致力于使其保持活力的人。

其次，它提到了另一篇文章，详细描述了一个有争议的情况，即巴西跨性别女性议员在美国签证上被归类为“男性”。这篇文章由 Luís Gustavo Carmo 撰写， Fernanda Canofre 翻译，可能深入探讨了这种错误分类的影响，可能会涉及跨性别者的身份认同、歧视和政治代表等方面的问题。“2天前”的标签表明了这则新闻的时效性。

---

## 72. Kids twice as likely to die if hit by SUV than car

**原文标题**: Kids twice as likely to die if hit by SUV than car

**原文链接**: [https://www.rte.ie/news/world/2025/0430/1510343-suv-road-fatalities/](https://www.rte.ie/news/world/2025/0430/1510343-suv-road-fatalities/)

生成摘要时出错

---

## 73. How to build Intrinsic Motivation: a review of the science

**原文标题**: How to build Intrinsic Motivation: a review of the science

**原文链接**: [https://erringtowardsanswers.substack.com/p/intrinsic-motivation](https://erringtowardsanswers.substack.com/p/intrinsic-motivation)

生成摘要时出错

---

## 74. 高斯溅射与ROS2结合

**原文标题**: Gaussian Splatting Meets ROS2

**原文链接**: [https://github.com/shadygm/ROSplat](https://github.com/shadygm/ROSplat)

ROSplat is a ROS2-based visualizer that leverages Gaussian splatting to render complex 3D scenes in real-time. It efficiently visualizes millions of Gaussians using custom ROS2 messages (SingleGaussian and GaussianArray), GPU-accelerated sorting, and rendering techniques. The project supports data loading from PLY files and integrates with ROS2 tools like bag recording.

Key features include real-time visualization, ROS2 integration, custom Gaussian message types for properties like position, rotation, scale, opacity, and spherical harmonics, and GPU acceleration for sorting and rendering.

The project was developed and tested on Ubuntu 24.04 LTS with ROS2 Jazzy and recommends an NVIDIA graphics card for optimal performance. Installation involves setting up ROS2, and optionally `cupy` and `torch` for GPU-based sorting, installable via `pip`. A Docker-based setup is also provided with a script for building and running the container, requiring matching CUDA versions between the host and container.

Building the custom Gaussian messages located in the `gaussian_interface/msg` folder is crucial and requires using `colcon build` and sourcing the workspace. The visualizer is then launched using `python3 main.py` from the `src` directory. The author welcomes contributions and feedback, and acknowledges Qihao Yuan, Kailai Li and limacv for their contributions and guidance.


---

## 75. Groups move for disclosure of Chemours' sealed PFAS documents

**原文标题**: Groups move for disclosure of Chemours' sealed PFAS documents

**原文链接**: [https://www.thenewlede.org/2025/04/groups-move-for-disclosure-of-chemours-sealed-pfas-documents/](https://www.thenewlede.org/2025/04/groups-move-for-disclosure-of-chemours-sealed-pfas-documents/)

生成摘要时出错

---

## 76. The lost secrets of Palm webOS (2014)

**原文标题**: The lost secrets of Palm webOS (2014)

**原文链接**: [https://www.theverge.com/2014/1/2/5264580/the-lost-secrets-of-webos](https://www.theverge.com/2014/1/2/5264580/the-lost-secrets-of-webos)

生成摘要时出错

---

## 77. 《颠倒乾坤》结尾发生了什么？ (2013)

**原文标题**: What happens at the end of 'Trading Places'? (2013)

**原文链接**: [https://www.npr.org/sections/money/2013/07/19/201430727/what-actually-happens-at-the-end-of-trading-places](https://www.npr.org/sections/money/2013/07/19/201430727/what-actually-happens-at-the-end-of-trading-places)

This NPR article explains the complex ending of the movie "Trading Places," breaking down how Louis Winthorpe (Dan Aykroyd) and Billy Ray Valentine (Eddie Murphy) financially ruin the Duke brothers. The Duke brothers attempt to profit from an advance government report on the orange crop, giving them inside information to manipulate the frozen concentrated orange juice market. Winthorpe and Valentine discover this plot and devise a counter-strategy.

Their plan involves:

1. **Feeding the Dukes False Information:** They replace the accurate crop report with a fake one, leading the Dukes to believe the orange crop is failing and OJ prices will rise.
2. **Driving Up Futures Prices:** The Dukes, believing the false report, instruct their trader to aggressively buy orange juice futures, creating artificial demand and inflating prices.
3. **Selling High:** Winthorpe and Valentine then sell contracts promising to deliver orange juice in the future at a high price ($1.42 per pound), capitalizing on the inflated market.
4. **Waiting for the Truth:** When the actual crop report is revealed on television, showing a healthy orange crop, the market panics, and prices plummet.
5. **Buying Low:** Winthorpe and Valentine then buy back orange juice futures contracts at the drastically reduced price (29 cents a pound).

By selling high and buying low, they fulfill their original contracts at a massive profit, while the Dukes, who bought high and are now forced to sell low, are bankrupted. The article also notes that trading on inside information of this nature was not illegal at the time the movie was made, but has since been outlawed in 2010, a provision often called the "Eddie Murphy Rule."


---

## 78. Microsoft announces new European digital commitments

**原文标题**: Microsoft announces new European digital commitments

**原文链接**: [https://blogs.microsoft.com/on-the-issues/2025/04/30/european-digital-commitments/](https://blogs.microsoft.com/on-the-issues/2025/04/30/european-digital-commitments/)

生成摘要时出错

---

## 79. Show HN: 我构建了一个运行Python的硬件处理器

**原文标题**: Show HN: I built a hardware processor that runs Python

**原文链接**: [https://www.runpyxl.com/gpio](https://www.runpyxl.com/gpio)

"Show HN"：PyXL，一款直接在硅上执行Python代码的定制硬件处理器，无需解释器、JIT或操作系统。它将Python代码编译成定制汇编，并在从头构建的流水线处理器上运行。

PyXL的主要优势在于其速度和确定性。在PyXL上，一个GPIO往返仅需480ns，而基于MicroPython的PyBoard上则需要大约15,000ns，当按时钟速度标准化后，性能提升了30-50倍。这种速度的提升源于Python字节码的直接硬件执行，绕过了基于软件的虚拟机开销。

该项目目前在Zynq-7000 FPGA（Arty-Z7-20开发板）上运行，PyXL核心以100MHz的频率运行。虽然ARM CPU处理设置和内存，但Python代码本身完全在硬件中执行。

PyXL的确定性使其适用于实时用例，例如实时控制系统、传感器环路中的ML推理、机器人技术以及对时间和可靠性至关重要的嵌入式工业系统。通过在硬件上直接执行Python，PyXL有望为嵌入式系统中Python带来全新的响应能力和精度。

---

## 80. Show HN: Sim Studio – Open-Source Agent Workflow GUI

**原文标题**: Show HN: Sim Studio – Open-Source Agent Workflow GUI

**原文链接**: [https://github.com/simstudioai/sim](https://github.com/simstudioai/sim)

生成摘要时出错

---

## 81. 萨提亚·纳德拉表示，高达30%的微软代码是由软件编写的。

**原文标题**: Satya Nadella says as much as 30% of Microsoft code is written by software

**原文链接**: [https://www.cnbc.com/2025/04/29/satya-nadella-says-as-much-as-30percent-of-microsoft-code-is-written-by-ai.html](https://www.cnbc.com/2025/04/29/satya-nadella-says-as-much-as-30percent-of-microsoft-code-is-written-by-ai.html)

生成摘要时出错

---

## 82. Princeton Engineering Anomalies Research (2010)

**原文标题**: Princeton Engineering Anomalies Research (2010)

**原文链接**: [https://pearlab.icrl.org/theory.html](https://pearlab.icrl.org/theory.html)

生成摘要时出错

---

## 83. GPT Image prompted to "create the exact replica of this image" 74 times

**原文标题**: GPT Image prompted to "create the exact replica of this image" 74 times

**原文链接**: [https://old.reddit.com/r/ChatGPT/comments/1k9yow9/chatgpt_omni_prompted_to_create_the_exact_replica/](https://old.reddit.com/r/ChatGPT/comments/1k9yow9/chatgpt_omni_prompted_to_create_the_exact_replica/)

生成摘要时出错

---

## 84. 经济学家称，生成式人工智能并未取代工作或损害工资。

**原文标题**: Generative AI is not replacing jobs or hurting wages at all, say economists

**原文链接**: [https://www.theregister.com/2025/04/29/generative_ai_no_effect_jobs_wages/](https://www.theregister.com/2025/04/29/generative_ai_no_effect_jobs_wages/)

生成摘要时出错

---

## 85. Why did Windows 7 log on slower for months if you had a solid color background?

**原文标题**: Why did Windows 7 log on slower for months if you had a solid color background?

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20250428-00/?p=111121](https://devblogs.microsoft.com/oldnewthing/20250428-00/?p=111121)

生成摘要时出错

---

## 86. 一行代码价值 8000 美元

**原文标题**: A single line of code cost $8000

**原文链接**: [https://pietrasiak.com/one-line-of-code-that-did-cost-dollar8000](https://pietrasiak.com/one-line-of-code-that-did-cost-dollar8000)

Screen.studio：一个macOS录屏应用因自动更新程序中的简单编码错误导致了8000美元的Google Cloud账单。一次重构意外导致该应用每5分钟重复下载一个250MB的更新文件，而不是在首次下载后停止。

许多用户将该应用在后台运行数周，进一步加剧了这个问题，触发了持续不断的、不必要的下载。这导致在一个月内产生了约900万次下载和超过2PB的Google Cloud流量。

作者强调了问题的规模，流量高达1GiB/s。由于该公司缺乏成本警报且没有定期监控云使用情况，这个问题未被注意到。直到作者的信用卡阻止了这笔费用，才发现该事件。

过度的流量也影响了用户，甚至有一位用户的互联网合同因极端的数据使用而被终止。该公司主动承担了用户的费用，最终与供应商解决了这个问题。

作者强调了设置云成本警报、仔细编写自动更新代码（以及通常的成本生成代码）、为强制更新实施服务器端信号以及定期监控云基础设施的重要性。该事件是一次痛苦的教训，提醒人们看似微小的编码错误可能造成的潜在后果，以及强大的监控和警报系统的重要性。

---

## 87. Australian identical twins speak in unison during interview about alleged crime

**原文标题**: Australian identical twins speak in unison during interview about alleged crime

**原文链接**: [https://apnews.com/video/australian-identical-twins-speak-in-unison-during-interview-about-alleged-crime-8bb2cbc65e0d4deeabb3fd37e981ad06](https://apnews.com/video/australian-identical-twins-speak-in-unison-during-interview-about-alleged-crime-8bb2cbc65e0d4deeabb3fd37e981ad06)

生成摘要时出错

---

## 88. Waymo and Toyota outline partnership to advance autonomous driving deployment

**原文标题**: Waymo and Toyota outline partnership to advance autonomous driving deployment

**原文链接**: [https://waymo.com/blog/2025/04/waymo-and-toyota-outline-strategic-partnership](https://waymo.com/blog/2025/04/waymo-and-toyota-outline-strategic-partnership)

生成摘要时出错

---

## 89. Show HN: Flowcode – Turing-complete visual programming platform

**原文标题**: Show HN: Flowcode – Turing-complete visual programming platform

**原文链接**: [https://app.getflowcode.io/playground/example1](https://app.getflowcode.io/playground/example1)

Unable to access the article link.


---

## 90. Show HN: Heart Rate Zones Plus – The first iOS app I developed

**原文标题**: Show HN: Heart Rate Zones Plus – The first iOS app I developed

**原文链接**: [https://apps.apple.com/us/app/heart-rate-zones-plus/id6744743232](https://apps.apple.com/us/app/heart-rate-zones-plus/id6744743232)

生成摘要时出错

---

## 91. The One-Person Framework in Practice

**原文标题**: The One-Person Framework in Practice

**原文链接**: [https://link.mail.beehiiv.com/ss/c/u001.5SRwDQ9qxPQW8vmD5Do73b3R4eTCi2vXqPyztEk6wMFC9_fqEAcDVx6xEJ96T4BSMXrPS7z5exEBSTF4pF48z8SqJkJnkAwMUW9LtYdd8lWmvkDinT92nsk5HmXOHdWgLsysm9FMGrqmu7dnG57cXpga8ZOe8X0IV8pyeC3AswdRMaitfT307y7naP-_6W5CiolKhXCKrEndMGCW2PftFUu9ieYOxpVJ_fhu82gAh-4/4g1/wA_MG-I5SVCyR3KY66oEaQ/h30/h001.kLDFZMgisudi21zmTPbd_O8U7X98d4UxYqZjQTb_D7o](https://link.mail.beehiiv.com/ss/c/u001.5SRwDQ9qxPQW8vmD5Do73b3R4eTCi2vXqPyztEk6wMFC9_fqEAcDVx6xEJ96T4BSMXrPS7z5exEBSTF4pF48z8SqJkJnkAwMUW9LtYdd8lWmvkDinT92nsk5HmXOHdWgLsysm9FMGrqmu7dnG57cXpga8ZOe8X0IV8pyeC3AswdRMaitfT307y7naP-_6W5CiolKhXCKrEndMGCW2PftFUu9ieYOxpVJ_fhu82gAh-4/4g1/wA_MG-I5SVCyR3KY66oEaQ/h30/h001.kLDFZMgisudi21zmTPbd_O8U7X98d4UxYqZjQTb_D7o)

生成摘要时出错

---

## 92. 与中国走向冷战轨道

**原文标题**: On Track for Cold War with China

**原文链接**: [https://www.wsj.com/opinion/on-track-for-the-next-cold-war-china-us-foreign-policy-tension-cb01526c](https://www.wsj.com/opinion/on-track-for-the-next-cold-war-china-us-foreign-policy-tension-cb01526c)

无法访问文章链接。

---

## 93. 全球心脏病死亡与塑料中广泛使用的化学物质有关

**原文标题**: Heart disease deaths worldwide linked to chemical widely used in plastics

**原文链接**: [https://medicalxpress.com/news/2025-04-heart-disease-deaths-worldwide-linked.html](https://medicalxpress.com/news/2025-04-heart-disease-deaths-worldwide-linked.html)

2025年纽约大学朗格尼健康中心在eBioMedicine上发表的一篇文章指出，用于塑料中的邻苯二甲酸酯DEHP的暴露与2018年全球超过36.5万例心脏病死亡相关。这项研究分析了来自200个国家的健康和环境数据，发现非洲、南亚和中东地区的人口承受了不成比例的大部分死亡，约占总数的一半。印度死亡人数最多（39677人）。研究人员估计，这些死亡造成的经济负担在5100亿美元至3.74万亿美元之间。

该团队之前的研究已将邻苯二甲酸酯与美国老年人的过早死亡联系起来，但这是首次对归因于这些化学物质的心血管死亡率进行全球估算。据信，DEHP暴露会引发心脏动脉炎症，增加心脏病发作和中风的风险。研究人员认为，工业化迅速发展且制造业限制较少的地区，暴露率较高可能是导致死亡率差异的原因。

作者主张制定全球法规，以减少邻苯二甲酸酯的暴露，尤其是在受影响地区。他们提醒说，该研究并未证明DEHP直接导致心脏病，也没有考虑其他邻苯二甲酸酯或年龄组。未来的研究将追踪减少邻苯二甲酸酯暴露对死亡率的影响，并检查与这些化学物质相关的其他健康问题。

---

## 94. Show HN: Web-eval-agent – 让编码智能体自行调试

**原文标题**: Show HN: Web-eval-agent – Let the coding agent debug itself

**原文链接**: [https://github.com/Operative-Sh/web-eval-agent](https://github.com/Operative-Sh/web-eval-agent)

Operative.sh 推出 `web-eval-agent`，一个 MCP 服务器，使编码代理能够使用浏览器自动化技术，直接在您的代码编辑器中自主调试 Web 应用程序。此工具旨在简化调试，让开发者专注于其他任务。

主要功能包括：

*   **浏览器驱动的导航：** 利用 BrowserUse 实现高效的 Web 应用导航。
*   **网络流量捕获：** 智能地过滤并在上下文窗口中提供网络请求。
*   **控制台错误收集：** 捕获日志和错误。
*   **自主调试：** 允许像 Cursor 这样的编码代理通过调用 Web QA 代理来测试代码。

本文提供了 macOS/Linux（使用 Brew、npm 和 jq）的快速入门说明，以及 Windows（使用 Cline）的手动安装步骤。它还解决了一个已解决的 Playwright 问题。

提供了一个示例输出报告，展示了代理如何导航 Web 应用程序、与元素交互以及记录网络请求和控制台输出以测试特定流程（例如删除 API 密钥）。该报告以成功/失败评估结尾，并引用了一个“Operative 控制中心”仪表板以查看实时日志。

---

## 95. 大型语言模型能产生随机性吗？

**原文标题**: Can LLMs do randomness?

**原文链接**: [https://rnikhil.com/2025/04/26/llm-coin-toss-odd-even](https://rnikhil.com/2025/04/26/llm-coin-toss-odd-even)

大型语言模型能否产生真正随机的输出：硬币抛掷和奇偶数生成实验

---

## 96. 研究发现削减公共研发预算将严重损害经济。

**原文标题**: Study finds that budget cuts to public R&D would significantly hurt the economy

**原文链接**: [https://impa.american.edu/costs-of-cutting-scientific-research/](https://impa.american.edu/costs-of-cutting-scientific-research/)

本文总结了一项研究，该研究分析了削减美国国立卫生研究院 (NIH) 和国家科学基金会 (NSF) 等联邦机构的公共研发 (R&D) 资金可能造成的经济损失。该研究的结论是，此类削减将在长期内严重损害经济。

主要发现包括对国内生产总值 (GDP)、投资和政府收入的重大负面影响。公共研发支出减少 25% 可能会使 GDP 的降幅与大萧条期间的降幅相似。与预计的历史 GDP 趋势相比，更大幅度的 50% 削减可能导致每个美国人平均损失 10,000 美元。

此外，该研究还强调了对联邦政府收入的不利影响。预计研发支出减少 25% 将使收入每年减少约 4.3%，而减少 50% 则可能导致每年减少 8.6%。本质上，该报告认为，投资公共研发对于经济增长和政府收入的产生至关重要，削减这笔资金将产生严重且持久的负面影响。

---

## 97. 动量工坊 (2017)

**原文标题**: Why Momentum Works (2017)

**原文链接**: [https://distill.pub/2017/momentum/](https://distill.pub/2017/momentum/)

由于无法获取Distill网站上《为何动能有效（2017）》一文的实际内容，我只能根据对动量投资的普遍理解提供一个大致的总结。请注意，这只是推测，可能无法完全反映文章的具体论点。

可能的总结会讨论动量投资如何通过买入近期表现良好的资产和卖出表现不佳的资产来产生正回报。文章可能探讨了这种现象的潜在解释。

它可能会讨论行为金融学的原因，例如羊群效应，即投资者跟随趋势并放大价格波动，导致反应不足和信息整合延迟。这种反应不足为动量策略创造了盈利机会。

另一种潜在的解释与信息扩散有关。有关公司前景的信息通常会逐渐传播，随着更多投资者意识到利好消息，最初的价格上涨得以持续。

文章可能还会涉及基于风险的解释，表明动量策略本质上风险更高，而超额回报是对承担这种风险的补偿。这可能涉及暴露于宏观经济因素或其他系统性风险。

最后，文章可能会强调动量策略的局限性，例如潜在的突然逆转和交易成本的影响。它很可能通过强调理解动量背后的驱动因素以实施成功的策略来结束。

---

## 98. 伊斯玛仪·贾扎里精巧机械装置手稿（约17世纪）

**原文标题**: Manuscript of Ismail al-Jazarī's Ingenious Mechanical Devices (ca. 17th century)

**原文链接**: [https://publicdomainreview.org/collection/arabic-machine-manuscript/](https://publicdomainreview.org/collection/arabic-machine-manuscript/)

This very short article identifies a manuscript related to the work of Ismail al-Jazarī, a renowned polymath and engineer from the 12th century. Specifically, the manuscript is titled "Manuscript of Ismail al-Jazarī's Ingenious Mechanical Devices" and is dated to approximately the 17th century.

The main point is that the Islamic Scientific Manuscripts Initiative has identified and potentially cataloged this manuscript. The title suggests the manuscript contains illustrations and descriptions of al-Jazarī's famous mechanical devices, likely drawn from his seminal work, *The Book of Knowledge of Ingenious Mechanical Devices* (Kitāb fī ma'rifat al-ḥiyal al-handasiyya).

The significance lies in the fact that al-Jazarī's original work is a landmark achievement in the history of engineering. This 17th-century manuscript represents a later copy or adaptation, offering valuable insights into how his designs were interpreted, replicated, and potentially even improved upon in subsequent centuries within the Islamic world. It could potentially contain new information, variations on existing designs, or different perspectives on his work. Ultimately, it contributes to our understanding of the transmission and evolution of scientific and technological knowledge during that period.


---

## 99. A Major Retro Handheld Maker Just Stopped All U.S. Shipments over Tariffs

**原文标题**: A Major Retro Handheld Maker Just Stopped All U.S. Shipments over Tariffs

**原文链接**: [https://kotaku.com/anbernic-rg-34xx-retro-handheld-emulation-tariff-1851777125](https://kotaku.com/anbernic-rg-34xx-retro-handheld-emulation-tariff-1851777125)

生成摘要时出错

---

## 100. 我对2025年DjangoCon EU的收获

**原文标题**: My takeaways from DjangoCon EU 2025

**原文链接**: [https://www.zachbellay.com/posts/djangocon-eu-2025/](https://www.zachbellay.com/posts/djangocon-eu-2025/)

本文总结了2025年都柏林 DjangoCon EU 大会的要点，涵盖了与 Django 开发者相关的各种主题。主要学习内容包括数据库优化，例如使用 BigInt 作为主键、分区表以及创建局部索引以节省空间。作者强调了性能测试和使用 `EXPLAIN ANALYZE` 等工具分析数据库查询的重要性。

文章重点介绍了有用的工具和库，例如用于 CRUD 视图的 `django-neopolitan`、用于减少 DB 查询的 `django-auto-prefetch` 以及用于密码密钥支持的 `django-otp-webauthn`。它还建议使用 `strace` 检查系统调用，并使用 `MaxMind` 阻止恶意用户。最佳实践包括审查生成的 SQL 迁移、在测试中计算 DB 查询数量以及清理旧的特性标志。

作者指出 `django-csp` 即将集成到 Django 核心，以及用 Rust 编写的 Django 模板后端正在开发中。他们还讨论了 Django 功能提案转向 GitHub 的趋势。最后，作者分享了对 Django 社区的个人观察、欧洲相对于美国的生活质量，并推荐了会议中的几个演讲，包括关于数据导向设计、HTMX 集成和扩展 Django 应用程序的演讲。

---

