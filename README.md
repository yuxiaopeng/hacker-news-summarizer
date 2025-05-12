# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-05-12.md)

*最后自动更新时间: 2025-05-12 17:49:13*
## 1. 嵌入被低估了

**原文标题**: Embeddings Are Underrated

**原文链接**: [https://technicalwriting.dev/ml/embeddings/overview.html](https://technicalwriting.dev/ml/embeddings/overview.html)

嵌入：技术写作中被低估的机器学习技术

本文认为，嵌入是一种被低估的机器学习技术，它可以发现文本之间以前无法实现的大规模连接。 嵌入是通过将文本输入到模型中生成的，模型会输出一个固定大小的数字数组（一个向量）。 数组的大小取决于模型（例如，Gemini 的 text-embedding-004 为 768 个数字，Voyage AI 的 voyage-3 为 1024 个数字）。 关键在于，这些数字允许对任意两段文本进行数学比较，而不管它们的大小如何。

作者解释了使用 Gemini 的 API 创建嵌入的过程，并讨论了成本和环境影响。 他还比较了不同的嵌入模型，强调了输入大小的重要性（voyage-3 目前具有最大的输入大小）。

作者将嵌入比作地图上的点，数组中的每个数字代表一个维度。 比较嵌入之间的距离揭示了文本的语义接近度。 这个概念与潜在空间有关。

一个应用是文档站点上的相关页面推荐。 通过为每个页面生成嵌入并进行比较，系统可以识别相关内容，其成本可能低于传统方法。 作者在 Sphinx 文档上进行了一项实验，使用自定义 Sphinx 扩展生成嵌入，并使用线性代数找到最近邻。 他发现结果很有希望，并建议免费提供文档内容的嵌入，以促进社区发展。

---

## 2. 我破解了一个约会软件（以及如何不对待安全研究员）

**原文标题**: I hacked a dating app (and how not to treat a security researcher)

**原文链接**: [https://alexschapiro.com/blog/security/vulnerability/2025/04/21/startups-need-to-take-security-seriously](https://alexschapiro.com/blog/security/vulnerability/2025/04/21/startups-need-to-take-security-seriously)

安全研究员发现Cerca约会应用存在严重漏洞，可能暴露数千用户的个人数据。该研究员发现一次性密码直接在API响应中发送，仅凭电话号码即可实现账户接管。此外，该研究员绕过身份验证访问未受保护的端点，其中包括一个显示用户个人资料的端点，其中包含敏感信息，如电话号码、电子邮件、性偏好和私密消息。至关重要的是，该研究员还可以访问提交的护照/身份证信息。

该研究员使用脚本枚举了6000多名用户，发现其中200多人提交了身份证信息。这代表着严重的隐私泄露，与Cerca声称采用行业标准加密的说法相悖。

该研究员于2025年2月负责任地向Cerca披露了这些漏洞，Cerca最初承认了这些问题并承诺迅速采取行动。然而，Cerca随后保持沉默，未提供更新、解决用户的问题或公开承认该事件。该研究员独立确认漏洞已得到修复，并决定公布其发现，以提高人们的意识并倡导更好的安全实践。该研究员强调了暴露的敏感数据可能造成的现实危害，包括身份盗窃、跟踪和敲诈勒索。文章强调，初创公司需要优先考虑用户数据安全，而不是快速进入市场。

---

## 3. 巴比肯

**原文标题**: The Barbican

**原文链接**: [https://arslan.io/2025/05/12/barbican-estate/](https://arslan.io/2025/05/12/barbican-estate/)

作者追溯了其对巴比肯住宅区的迷恋——这个位于伦敦，建于1965年至1976年的住宅群，而这份迷恋的开端源于一次对维索家具的寻找。这份兴趣促使作者通过视频、书籍，最终通过一次实地参观来研究巴比肯。

在最近一次伦敦之旅中，作者参加了一个由居民带领的两个小时的建筑之旅，揭示了许多引人入胜的细节。巴比肯被设计成一个自给自足的社区，居民可以在这里度过一生。这个建筑群刻意设计成迷宫状，据说是为了阻止窃贼。它拥有地下停车场（里面有废弃的汽车）、以英国历史人物命名的建筑，以及来自古埃及的建筑灵感等设施。

作者重点介绍了专属的居民权限，包括可以通过钥匙扣进入的隐藏入口。巴比肯的历史悠久，建在罗马和中世纪的废墟之上，包括一个犹太墓地。居民依靠集中供暖，但供暖控制不稳定，他们通过在线论坛barbicantalk.com进行交流。该建筑群还包含对著名建筑师如勒·柯布西耶的致敬，甚至还设有一所音乐学校的分校。

作者最后推荐了三本供那些有兴趣了解更多关于巴比肯的人阅读的书籍：《巴比肯居民》、《巴比肯住宅区》和《建造乌托邦：巴比肯中心》，其中后者因其最新的和内部信息而尤其值得关注。

---

## 4. 一路走好，Usenix ATC

**原文标题**: RIP Usenix ATC

**原文链接**: [https://bcantrill.dtrace.org/2025/05/11/rip-usenix-atc/](https://bcantrill.dtrace.org/2025/05/11/rip-usenix-atc/)

本文反思了曾经作为系统实践者先锋论坛的USENIX年度技术会议（ATC）的衰落。作者回忆了ATC的黄金时代，重点介绍了1994年USENIX夏季会议和2004年ATC上DTrace的成功发布。然而，作者注意到ATC向学术界的转变，并感叹行业参与度和相关性的下降。

作者将ATC的困境与系统领域的更广泛变化联系起来。由专业人士驱动并在生产中部署的Go和Rust等开源项目已成为创新的主要驱动力，从而减少了对正式会议出版的需求。作者承认维持线下会议固有的挑战，并建议在线形式可能提供更多价值。

尽管ATC衰落，作者仍强调其过去作为展示突破性系统工作的论坛所做的贡献。他重点介绍了最后一篇最佳论文，该论文侧重于一个真实的AI基础设施验证系统，以此证明会议的最初精神。作者最后感谢USENIX为重要思想提供了一个平台，甚至承认多年来的复杂关系。他最终将ATC的失败归因于未能适应不断发展的系统开发格局以及学术出版模式的主导地位。

---

## 5. 德克萨斯大学领衔团队解决聚变能源领域一大难题

**原文标题**: University of Texas-led team solves a big problem for fusion energy

**原文链接**: [https://news.utexas.edu/2025/05/05/university-of-texas-led-team-solves-a-big-problem-for-fusion-energy/](https://news.utexas.edu/2025/05/05/university-of-texas-led-team-solves-a-big-problem-for-fusion-energy/)

德克萨斯大学领导的团队在聚变能源研究方面取得了重大突破，他们开发了一种新方法来设计用于仿星器反应堆的防漏磁约束系统。这项进展解决了困扰70年的难题，即如何在反应堆内约束高能粒子（特别是α粒子），防止它们逸出并阻碍聚变反应。

现有的用于识别磁场泄漏（对于防止粒子逸出至关重要）的方法要么计算成本高昂（使用牛顿定律），要么不准确（使用微扰理论）。这种基于对称理论的新方法提供了一条捷径，既准确又比传统的黄金标准方法快10倍。这使得工程师能够快速迭代设计并消除泄漏。

这项突破是仿星器设计中的一个“范式转变”，仿星器是一种使用外部线圈产生磁场以约束等离子体的聚变反应堆。这种新方法在托卡马克反应堆中也具有潜在应用，可以解决可能损坏反应堆壁的失控电子问题。这项发表在《物理评论快报》上的研究得到了美国能源部的支持，并涉及德克萨斯大学奥斯汀分校、洛斯阿拉莫斯国家实验室和Type One能源集团（一家计划建造仿星器用于发电的公司）的研究人员之间的合作。

---

## 6. Legion Health (YC S21) 招聘创始工程师，利用人工智能改善心理健康

**原文标题**: Legion Health (YC S21) Is Hiring Founding Engineers to Fix Mental Health with AI

**原文链接**: [https://www.workatastartup.com/jobs/75011](https://www.workatastartup.com/jobs/75011)

Legion Health (YC S21) 招募创始工程师：该公司致力于构建人工智能驱动的心理健康运营系统，从零开始重塑精神病学，利用AI和LLM自动化运营，减轻行政负担，并改善患者护理。与将AI附加到现有流程的其他AI初创公司不同，Legion Health正在重新设计整个系统。

该职位涉及构建AI原生护理基础设施，包括日程安排、文档记录、账单、入院登记和风险检测，直接影响实际患者和临床医生。该公司已经拥有一个实时代理副驾驶，并以最少的支持人员服务超过2,000名患者。

主要职责包括架构和扩展后端（Node.js、Next.js、TypeScript、PostgreSQL、AWS）、构建LLM代理基础设施、塑造人机协同运营的用户体验、定义患者旅程的世界状态模拟以及设计安全、符合HIPAA的数据管道。理想的候选人具有构建复杂系统的经验，以系统和事件流的方式思考，并且精通或渴望学习LLM。

Legion Health 拥有超过 100 万美元的年度经常性收入，增长迅速，并已筹集了 600 万美元的资金。他们提供塑造人工智能原生心理健康未来，并成为工程文化创始成员的机会。他们正在寻找欣赏清晰架构和速度的个人。该公司提供薪资和股权。

---

## 7. 社区主导的Organic Maps分支

**原文标题**: A community-led fork of Organic Maps

**原文链接**: [https://www.comaps.app/news/2025-05-12/3/](https://www.comaps.app/news/2025-05-12/3/)

一个由社区主导的Organic Maps分支，暂命名为CoMaps，正在迅速发展，其核心原则是透明、社区决策、非营利性质、开源和隐私。由于Organic Maps股东之间未解决的分歧，Organic Maps的未来充满不确定性，该项目旨在提供一个社区驱动的替代方案。

CoMaps正在专注于构建其技术基础，并准备首次发布。社区积极参与通过Codeberg上的投票选择最终项目名称，投票将于5月20日结束。

社区可以通过多种方式参与：在Codeberg上参与开发，参与Governance仓库中的组织活动，传播意识，协助社交媒体内容，帮助构建网站，并通过Open Collective捐款。

与Organic Maps股东的谈判进展甚微。Viktor愿意保证不出售该项目，但坚持保留完全控制权，而股东分歧仍未解决。下一次更新将公布CoMaps的最终项目名称。

---

## 8. 交通事故死亡是一种选择

**原文标题**: Traffic Fatalities Are a Choice

**原文链接**: [https://asteriskmag.com/issues/10/traffic-fatalities-are-a-choice](https://asteriskmag.com/issues/10/traffic-fatalities-are-a-choice)

Abi Olvera的文章《交通事故死亡是一种选择》认为，美国高交通事故死亡率是政策选择的结果，而非不可避免的。在道路安全方面，美国显著落后于其他发达国家，死亡率远高于荷兰、瑞典和西班牙等国。

这些更安全的国家采用了“安全系统”方法，该方法承认人为错误，并通过道路设计来减轻其后果。这包括将行人与高速交通物理隔离、通过街道设计减缓交通速度，以及创建直观引导驾驶员的“自我解释”道路。例如，荷兰的分隔自行车道和步行街，以及瑞典的带有缆索护栏的2+1道路。

虽然一些美国城市已经实施了安全系统设计的某些方面，例如受保护的自行车道和改进的交叉路口，但美国缺乏统一的国家级努力。一个主要的障碍是各州交通运输部对主要道路的控制，他们经常优先考虑车辆的畅通，而不是安全，有时甚至否决地方安全倡议。此外，《统一交通控制设备手册》(MUTCD)历来根据驾驶员行为而非安全性来设定速度限制。

作者强调，像高汽车拥有量和广阔的乡村这样的因素并不是不可逾越的借口，因为加拿大和芬兰等国也有类似的条件，但死亡率较低。通过更强大的联邦支持和基层行动主义来克服各州的惰性，对于实现“零愿景”，即零交通事故死亡的目标至关重要。

---

## 9. 使用Nix构建可验证的安全软件供应链

**原文标题**: Demonstrably Secure Software Supply Chains with Nix

**原文链接**: [https://nixcademy.com/posts/secure-supply-chain-with-nix/](https://nixcademy.com/posts/secure-supply-chain-with-nix/)

本文论述了包和依赖管理器 Nix 提供了一个强大的解决方案，以实现可论证的安全软件供应链，从而应对全球政府机构日益增长的软件完整性证明需求。文章强调了传统安全措施（如气隙环境）如何阻碍开发并增加成本，而 Nix 提供了一种在不影响开发者工作流程的情况下证明软件来源和完整性的方法。

Nix 允许组织保证特定的一组源代码产生了镜像，且不受第三方干扰；跟踪所有应用程序的来源和工具链以提高透明度；并通过存档每个版本的确切来源来审核输出。文章详细介绍了 Nix 如何通过关注可重现的构建和固定输出推导 (FOD) 来实现这一点。它使用一个 GitHub 项目的例子，展示了如何创建一个“源闭包”（包含所有必需的源包的集合），该闭包可以导出到离线、经过验证的系统，以便从头开始完全重建。这个过程证明了最终二进制文件（包括编译器及其编译器）的完整性，超越了从二进制分发开始所提供的验证深度。

其好处包括为开发人员提供最新的工具，简化合规人员的工作，并为安全专业人员减轻供应链攻击。虽然采用 Nix 需要克服最初的挑战，但它将合规性转变为一个可管理的最终验证步骤，将开发与严格的预先安全协议分离。Nix 使强大的供应链保证成为一个现实且廉价的开发后流程。

---

## 10. GADTs为何对性能至关重要 (2015)

**原文标题**: Why GADTs matter for performance (2015)

**原文链接**: [https://blog.janestreet.com/why-gadts-matter-for-performance/](https://blog.janestreet.com/why-gadts-matter-for-performance/)

Yaron Minsky认为GADTs（广义代数数据类型）对OCaml的性能很有价值，尤其是在控制内存表示方面。他最初认为GADTs只与编译器编写者相关。然而，在Jane Street，他们发现GADTs能够实现原本难以或不安全实现的内存表示调整。

核心问题是OCaml对多态类型的统一内存表示，这可能导致低效的空间使用。标准数组对每个元素使用相同的空间，而不管元素的大小如何。

Minsky演示了如何创建一个`Compact_array`类型，该类型对字符使用字节，否则使用通用数组。他首先尝试使用常规变体来实现这一点，但未能为`get`和`set`函数生成所需的类型签名。然后，他尝试使用“穷人对象”方法（使用闭包），但这为每个`Compact_array`引入了分配的闭包开销。

然后，他使用GADTs重写了`Compact_array`。通过定义类型`'a t`，并使用构造函数`Array`和`Bytes`，并专门将`Bytes`键入为`bytes -> char t`，他可以强制执行所需的类型行为。但是，类型推断变得棘手，需要使用局部抽象类型来引导编译器。通过使用局部抽象类型注释函数，编译器可以推断出该类型在match语句的不同分支中是不同的。

由此产生的基于GADT的`Compact_array`提供了类型安全的访问，同时可能提高内存效率，而没有闭包开销。文章总结说，GADTs提供了一种强大的机制，可以构建对内存表示进行精确控制的抽象，这对于高性能应用程序至关重要。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 2 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 3 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 4 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 5 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 6 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 7 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 8 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 9 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 10 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 11 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 12 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 13 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 14 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 15 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 16 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 17 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 18 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 19 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 20 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 21 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 22 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 23 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 24 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 25 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 26 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 27 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 28 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 29 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 30 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 31 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 32 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 33 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 34 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 35 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 36 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 37 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 38 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 39 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 40 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 41 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 42 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 43 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 44 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 45 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 46 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 47 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 48 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 49 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 50 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 51 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 52 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 53 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 54 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
