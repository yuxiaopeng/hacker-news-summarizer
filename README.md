# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-04-30.md)

*最后自动更新时间: 2025-04-30 18:08:44*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 2 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 3 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 4 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 5 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 6 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 7 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 8 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 9 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 10 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 11 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 12 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 13 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 14 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 15 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 16 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 17 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 18 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 19 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 20 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 21 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 22 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 23 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 24 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 25 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 26 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 27 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 28 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 29 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 30 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 31 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 32 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 33 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 34 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 35 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 36 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 37 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 38 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 39 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 40 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 41 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 42 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
