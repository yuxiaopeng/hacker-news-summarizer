# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-02.md)

*最后自动更新时间: 2025-10-02 17:45:07*
## 1. 信号协议与后量子棘轮

**原文标题**: Signal Protocol and Post-Quantum Ratchets

**原文链接**: [https://signal.org/blog/spqr/](https://signal.org/blog/spqr/)

本文宣布稀疏后量子棘轮（SPQR），它是Signal协议的增强版，旨在防御未来量子计算威胁。SPQR加强了该协议的前向保密性（FS）和泄露后安全性（PCS）保证。

原始的Signal协议使用哈希函数（量子安全）来实现FS，并使用椭圆曲线Diffie-Hellman（ECDH）交换（非量子安全）来实现PCS。SPQR通过引入量子安全密钥封装机制（KEM）来解决ECDH对量子攻击的脆弱性。

KEM的实施面临诸多挑战，包括密钥尺寸过大以及处理离线客户端、消息丢失和重排序等问题。本文探讨了诸如使用状态机协调消息发送和使用纠删码以更小的块有效传输大型密钥等解决方案，从而减轻消息丢失和恶意干扰的影响。

SPQR棘轮与原始双棘轮混合使用时，被称为三重棘轮。对于Signal用户而言，此更新是无缝的，并将最终应用于所有对话，在保持现有安全保证的同时，加强通信以防御潜在的量子计算机威胁。

---

## 2. 我们买了整个GPU，就他妈要用整个GPU。

**原文标题**: We bought the whole GPU, so we're damn well going to use the whole GPU

**原文链接**: [https://hazyresearch.stanford.edu/blog/2025-09-28-tp-llama-main](https://hazyresearch.stanford.edu/blog/2025-09-28-tp-llama-main)

本文详细介绍了一种针对H100 GPU上Llama-70B模型张量并行推理的吞吐量优化型巨内核，其端到端吞吐量性能超过SGLang 22%以上。基于他们之前在Llama-1B低延迟巨内核方面的工作，作者解决了大批量Llama-70B推理的挑战，其中计算、内存带宽和GPU间通信成为瓶颈。

关键思想是重叠这些操作，以最大化GPU资源利用率。与顺序运行内核的传统方法不同，巨内核将整个前向传递融合到一个单元中，使用指令和解释器模型。前向传递被分解为细粒度的指令，由GPU上的解释器执行，从而实现积极的流水线和资源共享。

本文重点介绍了巨内核如何在多个层级上实现重叠：通过流水线化指令阶段在SM（流式多处理器）内部重叠，通过同时运行不同类型的指令在SM之间重叠，以及通过将通信与计算重叠在GPU之间重叠。一项关键创新是“分布式转置”操作，它取代了reduce-scatter，以方便O投影矩阵乘法与通信的重叠。

虽然代码面向研究且可能比较挑剔，但它通过最大化硬件资源利用率，展示了巨内核在高吞吐量推理方面的潜力。作者最后强调了他们的核心巨内核抽象在低延迟和高吞吐量领域的可迁移性。

---

## 3. 白内障手术史

**原文标题**: The history of cataract surgery

**原文链接**: [https://www.asimov.press/p/cataracts](https://www.asimov.press/p/cataracts)

本文追溯了白内障手术四千年的演变历程，从最初级的拨障术到如今高度成功的手术。白内障，即眼球晶状体的混浊，是全球失明的主要原因之一，这也使得白内障手术成为全球最常施行的外科手术。

这段历史始于《妙闻本集》(约公元前600年)中记载的拨障术，这种方法通过将混浊的晶状体移位来恢复有限的视力。虽然这种方法在几个世纪中被不同文化所采用，但它并没有移除白内障，而且常常导致视力不佳。伊斯兰世界在10世纪时有了进步，Al-Mawsili使用空心针来提取白内障。

1747年，雅克·达维尔的囊外白内障摘除术(ECCE)取得重大突破，保留了后囊并减少了并发症。塞缪尔·夏普后来提出了囊内白内障摘除术(ICCE)，即移除整个晶状体。这两种技术都使得患者成为“无晶状体眼”，需要佩戴厚厚的眼镜。

Harold Ridley在观察到二战受伤飞行员的眼睛对PMMA材料的耐受性后，产生了人工晶状体(IOL)植入这一关键创新。1949年，Ridley植入了第一枚IOL，在白内障摘除后恢复了聚焦能力。虽然最初的结果好坏参半，但它为现代白内障手术的高成功率和可及性铺平了道路，尽管更广泛的普及，特别是在低收入国家，仍然是一个挑战。

---

## 4. N8n新增了使用DataTables的原生持久化存储

**原文标题**: N8n added native persistent storage with DataTables

**原文链接**: [https://community.n8n.io/t/data-tables-are-here/192256](https://community.n8n.io/t/data-tables-are-here/192256)

N8n 将在 1.113 版本及以上的所有计划中推出数据表 (beta)，在 n8n 平台内直接提供原生持久存储。 这解决了用户长期以来希望拥有内置表格以便在工作流执行之间存储数据的需求，从而无需外部平台和凭据。

数据表使用户能够：

* 持久保存工作流运行中的数据。
* 跨多个工作流执行维护数据。
* 跟踪执行状态以防止重复运行。
* 存储 AI 工作流的可重用提示。
* 收集 AI 工作流的评估数据。
* 执行查找、合并和数据增强。

为了保持性能，默认大小限制为 50MB，可以使用 `N8N_DATA_TABLES_MAX_SIZE_BYTES` 环境变量为自托管实例调整此限制。 N8n 鼓励用户升级到 v1.113，试用数据表，并提供关于缺失功能和潜在改进的反馈。 文档已发布，可供查阅以获取更多信息。

---

## 5. 工作不是学校：如何在体制的愚蠢中生存

**原文标题**: Work is not school: Surviving institutional stupidity

**原文链接**: [https://www.leadingsapiens.com/surviving-institutional-stupidity/](https://www.leadingsapiens.com/surviving-institutional-stupidity/)

本文探讨了高成就人士从以能力为基础的学校环境过渡到职场时常遇到的挫折，职场往往充斥着非逻辑性和主观性，制度性的“愚蠢”也可能滋生。文章指出，虽然组织声称是精英体制，但接近权力、时机、认知和政治价值等因素往往发挥着重要作用。

作者建议读者将组织中的失误归因于“愚蠢”而非恶意，从而培养好奇心并防止愤世嫉俗。主要观点包括：认知通常被视为“数据”，必须有意识地进行管理；争取“客观公平”通常是浪费时间。相反，应该学习主观逻辑和不成文的规则。

文章还强调了有效定位工作的重要性，理解组织内部不同的标准和动机，以及承认更高层级存在的瓶颈。文章鼓励读者选择自己参与的“游戏”，并承担这个选择，专注于自己的控制范围，并通过工作之外的身份和社区多样化来建立平衡的“意义组合”。

最终，文章倡导理解组织内部的主观暗流，从而更巧妙地运作，不是愤世嫉俗地玩弄体制，而是积极参与、做出贡献并创造意义，同时认识到组织是不完美的，但可以改变的人类构造。

---

## 6. 两架亚马逊送货无人机在亚利桑那州托莱森商业区撞上起重机

**原文标题**: Two Amazon delivery drones crash into crane in commercial area of Tolleson, AZ

**原文链接**: [https://www.abc15.com/news/region-west-valley/tolleson/two-amazon-delivery-drones-crash-into-crane-in-commercial-area-of-tolleson](https://www.abc15.com/news/region-west-valley/tolleson/two-amazon-delivery-drones-crash-into-crane-in-commercial-area-of-tolleson)

周三上午，两架亚马逊送货无人机在亚利桑那州托勒森市96号大街和罗斯福街附近的一个商业区撞到了一台起重机。托勒森警察局正在调查这起事故。目前尚不清楚是否有人受伤。亚马逊已承认此事，并表示正在配合当局进行调查。该事件正在发展中，更多信息将在稍后更新。

---

## 7. Liva AI (YC S25) 正在招聘

**原文标题**: Liva AI (YC S25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/liva-ai/jobs/6xM8JYU-founding-operations-lead](https://www.ycombinator.com/companies/liva-ai/jobs/6xM8JYU-founding-operations-lead)

Liva AI (YC S25) 是一家致力于通过构建丰富的人类语音和视频数据资料库来实现人工智能人性化的初创公司，正在旧金山招聘创始运营负责人。该职位涉及管理数据收集项目、改进内部工作流程以及设计人/人工智能协作系统。

理想的候选人应具备高度的组织能力、强大的问题解决能力以及人员管理经验。 需对人工智能代理和数据有浓厚的兴趣，具备咨询、投资银行、产品管理或先前的人工智能代理/机器学习经验者优先。 该职位要求承诺长时间工作（每天12小时，每周6天）。

Liva AI提供具有竞争力的薪资、免费食品和设备等福利、带薪家事假，以及成为YC支持的初创公司早期成员的机会。 公司的使命是通过捕捉多样化的声音和面孔来创造更逼真的人工智能，从而解决当前通用人工智能的局限性。 Liva AI 成立于 2025 年，目前正在旧金山积极组建团队。

---

## 8. 科学家表示，自闭症不应被视为单一病因的单一疾病。

**原文标题**: Autism should not be seen as single condition with one cause, say scientists

**原文链接**: [https://www.theguardian.com/society/2025/oct/01/autism-should-not-be-seen-as-single-condition-with-one-cause-say-scientists](https://www.theguardian.com/society/2025/oct/01/autism-should-not-be-seen-as-single-condition-with-one-cause-say-scientists)

一项新研究表明，自闭症应被视为一系列不同的病症，而非具有单一根本原因的单一实体。 研究人员分析了超过45,000名自闭症患者的基因和行为数据，发现早期（6岁之前）和晚期（10岁之后）确诊的患者之间存在显著差异。

早期确诊的个体从小就表现出稳定的行为困难，包括社交互动问题，并显示出独特的基因特征。 相比之下，晚期确诊的个体在青春期经历了越来越多的社交和行为挑战，并且更有可能患有抑郁症等精神健康疾病。 他们的基因特征也更类似于患有 ADHD、抑郁症和 PTSD 的个体。

虽然科学家们并不主张设立单独的诊断类别，但他们强调，“自闭症”可能包含具有不同生物学和发育途径的多种病症。 该研究发现，早期和晚期诊断的自闭症患者的基因特征重叠程度有限。 这些发现可能有助于解释自闭症诊断率的不断上升，一些专家认为这归因于诊断标准的扩大以及对该病症的更好认知。

---

## 9. 荷兰法官：Meta 必须尊重用户对推荐系统的选择

**原文标题**: NL Judge: Meta must respect user's choice of recommendation system

**原文链接**: [https://www.bitsoffreedom.nl/2025/10/02/judge-in-the-bits-of-freedom-vs-meta-lawsuit-meta-must-respect-users-choice/](https://www.bitsoffreedom.nl/2025/10/02/judge-in-the-bits-of-freedom-vs-meta-lawsuit-meta-must-respect-users-choice/)

荷兰法院裁定，Meta公司因未尊重用户在Facebook和Instagram等平台上对推荐系统的选择，违反了《数字服务法案》(DSA)。该案件由数字人权组织Bits of Freedom提起，他们认为Meta的设计削弱了用户的自主权和对其信息流的控制。

法官对此表示赞同，称Meta的“非持久选择选项”与DSA赋予用户真正自主权和选择自由的目标相悖。法院认为，Meta的设计通过微妙地将用户推向最大化广告收入的基于兴趣的信息流，同时隐藏非个性化选项并限制在替代时间线内访问诸如私信之类的功能，从而严重扰乱了用户的自主权。

法院已责令Meta调整其应用程序，以确保用户的Feed偏好得以保留，即使在导航到不同部分或重新启动应用程序时也是如此。Bits of Freedom对该裁决表示欢迎，称少数美国科技公司来决定人们如何看待世界是不可接受的。Bits of Freedom承认该裁决只是迈出的一小步，并希望它能激励其他人挑战Meta的权力。

---

## 10. 大西洋量子团队加入谷歌

**原文标题**: The Atlantic Quantum team is joining Google

**原文链接**: [https://blog.google/technology/research/scaling-quantum-computing-even-faster-with-atlantic-quantum/](https://blog.google/technology/research/scaling-quantum-computing-even-faster-with-atlantic-quantum/)

谷歌量子AI收购大西洋量子团队，加速量子计算发展。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 2 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 3 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 4 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 5 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 6 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 7 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 8 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 9 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 10 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 11 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 12 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 13 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 14 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 15 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 16 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 17 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 18 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 19 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 20 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 21 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 22 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 23 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 24 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 25 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 26 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 27 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 28 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 29 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 30 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 31 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 32 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 33 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 34 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 35 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 36 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 37 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 38 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 39 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 40 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 41 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 42 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 43 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 44 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 45 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 46 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 47 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 48 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 49 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 50 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 51 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 52 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 53 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 54 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 55 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 56 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 57 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 58 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 59 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 60 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 61 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 62 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 63 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 64 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 65 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 66 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 67 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 68 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 69 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 70 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 71 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 72 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 73 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 74 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 75 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 76 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 77 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 78 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 79 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 80 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 81 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 82 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 83 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 84 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 85 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 86 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 87 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 88 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 89 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 90 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 91 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 92 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 93 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 94 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 95 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 96 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 97 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 98 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 99 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 100 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 101 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 102 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 103 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 104 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 105 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 106 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 107 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 108 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 109 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 110 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 111 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 112 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 113 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 114 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 115 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 116 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 117 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 118 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 119 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 120 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 121 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 122 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 123 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 124 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 125 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 126 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 127 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 128 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 129 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 130 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 131 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 132 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 133 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 134 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 135 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 136 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 137 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 138 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 139 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 140 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 141 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 142 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 143 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 144 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 145 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 146 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 147 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 148 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 149 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 150 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 151 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 152 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 153 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 154 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 155 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 156 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 157 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 158 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 159 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 160 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 161 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 162 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 163 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 164 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 165 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 166 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 167 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 168 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 169 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 170 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 171 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 172 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 173 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 174 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 175 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 176 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 177 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 178 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 179 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 180 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 181 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 182 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 183 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 184 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 185 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 186 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 187 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 188 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 189 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 190 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 191 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 192 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 193 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 194 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 195 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 196 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 197 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
