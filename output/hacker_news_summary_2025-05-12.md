# Hacker News 热门文章摘要 (2025-05-12)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Tailscale 4via6 – 大规模连接边缘部署

**原文标题**: Tailscale 4via6 – Connect Edge Deployments at Scale

**原文链接**: [https://tailscale.com/blog/4via6-connectivity-to-edge-devices](https://tailscale.com/blog/4via6-connectivity-to-edge-devices)

此博文宣布 Tailscale 的 4via6 子网路由，该方案旨在连接复杂的边缘部署，在这些部署中，传统 VPN 会因 IP 重叠、NAT 和严格的防火墙而举步维艰。4via6 允许用户将 Tailscale 的网状网络扩展到具有大量相同网络的环境中，例如机器人或边缘设备群，而无需管理 IP、CIDR 范围或端口的复杂性。

传统的站点到站点 VPN 通常不适用于这些场景，因为它们假定存在唯一的 CIDR 范围、长期连接和公共 IP，而这些在边缘部署中很少存在。4via6 通过为每个连接的网络分配一个唯一标识符来解决这些挑战，从而实现无缝连接和安全的远程访问。

用例包括管理具有多个可寻址 IP 组件的机器人，连接具有重叠 CIDR 范围的不同环境或云提供商的 VPC，以及启用可重现的测试环境。优势包括隔离客户部署、连接单个客户的所有部署以及为支持团队提供安全的远程访问。Dexory 使用 4via6 安全地访问其全球机器人群并管理嵌入式网络设备。

网络上的设备可以使用 MagicDNS 名称或 IPv6 地址访问。4via6 在所有 Tailscale 计划中均可用，并在高级版和企业版中提供增强的安全监控。

---

## 12. Ruby 3.5 新特性：读取时的命名空间

**原文标题**: Ruby 3.5 Feature: Namespace on read

**原文链接**: [https://bugs.ruby-lang.org/issues/21311](https://bugs.ruby-lang.org/issues/21311)

本文介绍了一个为 Ruby 3.5 提出的名为“读取时命名空间”的新特性，旨在解决库之间的命名冲突，防止模块/对象的意外共享，并可能允许在一个应用程序中需要多个版本的 gem。该特性引入了虚拟顶层命名空间的概念，这些命名空间可以独立地 require/load 库，从而分离它们的依赖关系。

“读取时”意味着在 require/load 代码之前创建命名空间，允许程序员逐步控制隔离。这与“写入时”方法（如 Java 包）形成对比，后者由库本身声明命名空间，作者认为这对于 Ruby 生态系统来说是不切实际的。

该特性区分了“根”命名空间（内置类、模块、常量和 RubyGems）和“用户”命名空间（用于用户脚本）。用户命名空间可以是主脚本执行的“main”命名空间，也可以是通过 `Namespace.new` 创建的可选命名空间。内置定义会被复制到用户命名空间，而新的定义则被隔离。

常量、类变量和全局变量也按命名空间进行分离。方法和 proc 从其他地方调用时，会保留其定义的命名空间。动态链接库在命名空间内加载。可以通过写时复制语义在用户命名空间中修改内置类，而不会影响根命名空间。

该特性最初处于禁用状态，通过 `RUBY_NAMESPACE=1` 环境变量启用。讨论包括使用 `namespace` 关键字改进 Ruby 4.x 的潜在语法，以及关于在命名空间创建期间如何处理对象引用和常量的担忧（内置类/模块使用写时复制，其他对象使用共享引用）。讨论还包括在一个命名空间中创建的对象将不会 `is_a?` 来自主命名空间的类（例如，`ns1::Date.today.is_a?(Date) # => false`），从而导致潜在的混淆。

---

## 13. 复兴1930年代的模块化货运自行车设计

**原文标题**: Reviving a Modular Cargo Bike Design from the 1930s

**原文链接**: [https://www.core77.com/posts/136773/Reviving-a-Modular-Cargo-Bike-Design-from-the-1930s](https://www.core77.com/posts/136773/Reviving-a-Modular-Cargo-Bike-Design-from-the-1930s)

Core77文章讨论了一款名为Cyclauto的货运自行车，由一家法国移动出行公司设计，它复兴了法国实业家奥古斯特·雷蒙德在1930年代提出的模块化设计。与常见的将车架分为骑行者和货物区域的长车架货运自行车不同，Cyclauto将骑行者直接置于前轮上方，骑行者直接踩踏前轮，无需链条，减少了维护。为了便于启动，采用了三速花鼓。

一个关键特性是可以拆卸的载货部分，类似于半挂车，允许安装各种样式的拖车，从而创建一个满足不同用户需求的模块化系统，包括货物、乘客，甚至商业设施，如餐车。这种两件式车架也允许自行车拆卸，便于放入汽车后备箱运输。该公司声称较短的轴距提供了更小的转弯半径，从而提高了在城市环境中的机动性。

文章指出，Cyclauto已在自行车展上展出，但尚未公布生产日期。评论者提出了对骑行姿势、缺乏杠杆作用的方向盘设计、后刹车机制以及只想骑前轮的诱惑等方面的担忧。

---

## 14. Show HN: 识别虚假 GitHub 星星、高风险依赖项和许可证陷阱的 CLI 工具

**原文标题**: Show HN: CLI that spots fake GitHub stars, risky dependencies and licence traps

**原文链接**: [https://github.com/m-ahmed-elbeskeri/Starguard](https://github.com/m-ahmed-elbeskeri/Starguard)

StarGuard是一个命令行工具，旨在自动化开源尽职调查，通过检测与GitHub仓库相关的风险，例如虚假刷星活动、依赖劫持和许可证风险信号。它分析公共GitHub数据以生成信任评分，为手动审查提供快速且可扩展的替代方案。

主要功能包括：

*   **星级分析：** 使用突发检测、机器人相似度分析和虚假星级指数检测虚假刷星。
*   **依赖分析：** 解析SBOM/清单文件，标记各种包管理器（npm、PyPI、Maven、Go、Ruby）中未锁定版本、影子依赖或非注册依赖项。
*   **许可证分析：** 识别仓库及其直接依赖项中未知或高风险的许可证，如GPL/AGPL。
*   **维护者分析：** 评估贡献者集中度、提交频率和不活跃性。
*   **代码信号分析：** 扫描指示混淆、远程执行、加密挖矿或数据泄露的代码模式。

StarGuard使用GitHub API、突发检测算法、用户画像和依赖/许可证解析器来评估风险。它以JSON、Markdown或纯文本格式输出报告，并能生成星级历史图表和shields.io徽章。

它需要Python 3.9+和一个GitHub个人访问令牌才能获得最佳性能。用例包括：CTO审查开源新增内容、安全团队安排扫描、风险投资进行尽职调查，以及开源维护者提高透明度。该项目以Apache-2.0许可授权，并通过仅读取公共元数据和执行静态分析来强调安全性和隐私。

---

## 15. OpenEoX 旨在标准化产品生命周期结束（EOL）和支持结束（EOS）信息

**原文标题**: OpenEoX to Standardize End-of-Life (EOL) and End-of-Support (EOS) Information

**原文链接**: [https://openeox.org/](https://openeox.org/)

OpenEoX 旨在标准化软硬件行业产品生命周期结束 (EOL) 和支持结束 (EOS) 信息的交换，从而使供应商和开源维护者受益。它致力于解决产品生命周期状态表示不一致的问题，提供透明、高效和统一的方法。创始成员包括思科、微软、红帽、西门子、BSI 和 CISA。

OpenEoX 采用机器可读的格式，允许自动化和与 SBOM 和 CSAF/VEX 文档等工具集成，通过将生命周期信息纳入安全和合规工作流程来增强网络安全和漏洞管理。其轻量级和独立的模式使其能够在无需大规模系统改造的情况下被广泛采用。

OpenEoX 的重要性在于通过更快地识别和更换不受支持的产品来降低网络安全风险。它通过自动跟踪产品生命周期来改进漏洞管理，并通过与安全工具集成来实现更好的决策。其他好处包括简化产品管理、通过透明度增强客户信心以及促进向新技术解决方案的过渡。最终，OpenEoX 通过标准化 EOL 和 EOS 实践来促进更安全高效的 IT 环境。

---

## 16. 黑桃硬件描述语言

**原文标题**: Spade Hardware Description Language

**原文链接**: [https://spade-lang.org/](https://spade-lang.org/)

Spade：一种新型硬件描述语言，旨在通过融合现代软件编程语言的特性来简化硬件设计并减少错误。其关键特性包括通过`reg`关键字在语言层面支持流水线，使时序调整更加容易，以及具有结构体、数组、元组和枚举（包括带有有效载荷的枚举）的强大类型系统。模式匹配有助于实现清晰且全面的条件逻辑。

Spade提供类型推断，减少了对显式类型声明的需求，并强调有用的错误消息以帮助调试。它包含诸如Swim构建工具之类的工具，支持cocotb和Verilator进行测试，以及具有Spade类型信息的VCD转换。计划中的功能包括作为类型的整数范围、带有特性的泛型以及时钟域感知。

Spade正在林雪平大学积极开发中，并且可以使用，但用户应预期存在潜在的错误和缺失的功能。Spade网站提供了一本正在编写中的书籍以及提供概述的演讲链接。该项目是开源的，并鼓励通过Gitlab和Discord进行社区参与。还提供了详细介绍该语言设计和功能的出版物。编译器在EUPL-1.2下获得许可，标准库/网站在MIT和Apache许可下获得许可。

---

## 17. 前英国特种部队打破沉默，揭露同事犯下的“战争罪行”

**原文标题**: Ex-UK Special Forces break silence on 'war crimes' by colleagues

**原文链接**: [https://www.bbc.com/news/articles/cj3j5gxgz0do](https://www.bbc.com/news/articles/cj3j5gxgz0do)

前英国特种部队成员打破沉默，指控同事在伊拉克和阿富汗犯下战争罪行。他们描述了SAS和SBS部队谋杀手无寸铁的平民（包括儿童）、处决被铐上手铐的被拘留者以及故意杀害受伤人员的事件。他们说，这些行为变得司空见惯，并会“放置武器”掩盖真相，并伪造报告。

这些指控跨越十年以上，首次牵涉到SBS，并且超过了目前公开调查的时间范围。这些退伍军人指责一些特种部队成员表现出“精神病特征”，并表现得“不可触碰”。一位退伍军人描述了搜查、铐上手铐后枪杀被拘留者，然后在尸体旁放置手枪的情况。

他们声称，高级指挥官知道这些行为，并且SAS内部存在一种围绕杀戮的竞争文化，一些成员似乎对杀戮“上瘾”。文章称，时任首相戴维·卡梅伦在与阿富汗总统哈米德·卡尔扎伊的会晤中，曾多次被警告英国特种部队造成平民伤亡，但卡梅伦勋爵的一位发言人声称，提出的问题是关于北约部队的总体情况。国防部表示，他们“完全致力于”支持公开调查。

---

## 18. 宇宙预计在10⁷⁸年内衰变，比先前认为的要早得多

**原文标题**: Universe expected to decay in 10⁷⁸ years, much sooner than previously thought

**原文链接**: [https://phys.org/news/2025-05-universe-decay-years-sooner-previously.html](https://phys.org/news/2025-05-universe-decay-years-sooner-previously.html)

拉德堡德大学一项新研究表明宇宙衰变速度远超预期，预计约在10^78年后终结。这一修正后的估计基于对包括白矮星、中子星甚至人类在内的各种天体发出类霍金辐射的计算。

该研究发表在《宇宙学和天体粒子物理学杂志》上，建立在之前一篇论文的基础上，该论文表明除黑洞之外的物体也可以通过类似于霍金辐射的过程“蒸发”。研究人员根据各种物体在理想环境中的密度计算了它们的衰变时间。他们发现白矮星是持续时间最长的天体，将在大约10^78年后衰变，这比之前估计的10^1100年短得多。

令人惊讶的是，尽管黑洞具有更强的引力场，但中子星和恒星黑洞的衰变时间相似，约为10^67年。这归因于黑洞会重新吸收一部分自身的辐射。该研究还计算了月球和人类的衰变时间，估计均为10^90年，但承认其他因素可能会导致它们更快地消亡。

该研究强调了天体物理学、量子物理学和数学之间的跨学科合作在理解宇宙基本过程以及潜在地揭开霍金辐射之谜方面的重要性。该文章的主要作者是海诺·法尔克。

---

## 19. FTC推迟执行“点击取消”规则

**原文标题**: The FTC puts off enforcing its 'click-to-cancel' rule

**原文链接**: [https://www.theverge.com/news/664730/ftc-delay-click-to-cancel-rule](https://www.theverge.com/news/664730/ftc-delay-click-to-cancel-rule)

美国联邦贸易委员会将“一键取消”规则（又称“否定选择规则”）的执行日期从2024年5月14日推迟至2025年7月14日。该规则要求公司取消订阅的流程必须和注册订阅一样简单。如果消费者可以在网上注册，就必须能够在网上取消，且不得设置额外障碍。

美国联邦贸易委员会在重新评估公司在原定期限内遵守规则的潜在负担后，决定推迟执行。推迟执行的投票结果为3比0，但由于三月份解雇委员引发争议导致出现两个空缺，当时只有三名委员在场。

美国联邦贸易委员会声明，在7月14日之后，将全面执行该规则，要求受监管实体完全合规。 然而，该机构也表示，如果执行过程中发现任何未预见的问题，愿意修改该规则。 核心原则仍然是，取消订阅应与最初的注册过程一样简单直接。

---

## 20. 我逆向工程WSC毁了我的假期。

**原文标题**: I ruined my vacation by reverse engineering WSC

**原文链接**: [https://blog.es3n1n.eu/posts/how-i-ruined-my-vacation/](https://blog.es3n1n.eu/posts/how-i-ruined-my-vacation/)

作者es3n1n讲述了他们的假期项目：逆向工程Windows安全中心(WSC)以禁用Windows Defender。受到之前被DMCA的“no-defender”项目的启发，他们的目标是进行一个干净的实现，不依赖第三方杀毒软件。

最初，通过使用COM API，他们成功注册了一个虚假的AV，但由于WSC的进程验证，遇到了访问被拒绝的错误。这个过程包括调试WSC服务，这是一个具有挑战性的任务，因为作者使用M4Pro MacBook，并且需要一个x86 Windows环境。这导致了一个复杂的环境设置，包括远程访问朋友的电脑（具有高延迟）以及最终订阅shadow.tech以获得专用VM。

核心问题是WSC使用PPL保护、WinDefend SID、提权、签名和DllCharacteristics（特别是ForceIntegrity）的检查来验证调用者进程。作者最初错误地认为需要模仿WinDefend。纠正这个错误后，他们发现通过模仿WinDefend，WSC将对Windows Defender本身进行操作，这不允许禁用Defender。通过使用所需特征定位特定二进制文件（如Taskmgr.exe），他们绕过了这些检查。

作者最终克服了调试障碍（无效的AV名称、Parsec延迟），并成功创建了一个通过WSC API禁用Windows Defender的工具（“defendnot”）。结论强调了具有挑战性的调试环境以及作者完成项目的决心。

---

## 21. Show HN: Airweave – 让智能体搜索任何应用

**原文标题**: Show HN: Airweave – Let agents search any app

**原文链接**: [https://github.com/airweave-ai/airweave](https://github.com/airweave-ai/airweave)

Airweave：赋能AI代理语义搜索任何应用数据。它通过REST和MCP端点将结构化或非结构化的各种数据源转换为代理可用的知识，弥合了代理与数据源之间的差距。

主要功能包括：

*   **数据同步：** 以最少的配置连接到25+个数据源。
*   **实体提取和转换：** 提供处理数据的流水线。
*   **语义搜索：** 使代理能够基于含义查询数据。
*   **其他功能：** 包括具有OAuth2的多租户、增量更新、版本控制和白标。

Airweave提供Python和TypeScript/JavaScript的SDK，方便集成。该平台构建于React/TypeScript（前端）、FastAPI（后端）、PostgreSQL（元数据）和Qdrant（向量数据库）之上。通过Docker Compose支持开发部署，通过Kubernetes支持生产部署。

路线图包括额外的源集成、用于大规模同步的Redis工作队列、用于事件驱动同步的Webhooks以及通过Helm charts支持Kubernetes。该项目欢迎贡献，并以MIT许可证发布。您可以通过Discord、GitHub Issues或Twitter与Airweave团队联系。

---

## 22. 日本五金工具店的典型工作日 [视频]

**原文标题**: A Typical Workday at a Japanese Hardware Tool Store [video]

**原文链接**: [https://www.youtube.com/watch?v=A98jyfB5mws](https://www.youtube.com/watch?v=A98jyfB5mws)

这篇“文章”根本不是文章；它是一个YouTube视频标题和一些标准的YouTube链接及免责声明。实际内容缺失。

仅根据现有信息，该视频可能展示了日本五金工具店里典型的一天。在没有观看视频的情况下，我们只能推测它会提供关于日常运营、客户互动的信息，以及可能在日本经营此类业务的独特之处。这可能是一个生活片段的写照，旨在让观众了解这种特定的工作环境。

所列出的链接是样板化的YouTube内容，没有提供关于视频本身的任何信息。它们涉及版权、广告、服务条款、隐私以及其他标准的YouTube相关主题。

---

## 23. 优化我的 Hacker News 体验

**原文标题**: Optimizing My Hacker News Experience

**原文链接**: [https://reorientinglife.substack.com/p/optimizing-my-hacker-news-experience](https://reorientinglife.substack.com/p/optimizing-my-hacker-news-experience)

无法访问文章链接。

---

## 24. Ash (Almquist Shell) 变体

**原文标题**: Ash (Almquist Shell) Variants

**原文链接**: [https://www.in-ulm.de/~mascheck/various/ash/](https://www.in-ulm.de/~mascheck/various/ash/)

本文详细介绍了Ash（Almquist Shell）变体的历史和关系，追溯了其从Kenneth Almquist最初于 89 年发布的版本开始的血统，该版本旨在替代System V Release 4 Bourne shell。它重点介绍了Ash和SVR4 shell之间的关键差异，例如对“$(...)”命令替换和`export VAR=value`语法的支持。

然后，本文概述了Ash在各种BSD发行版（4.3BSD-Net/2、4.4BSD-Alpha等）、386BSD、BSD/OS、NetBSD和FreeBSD中的演变，并记录了每个版本中的特定更改和错误修复。它还涵盖了NetBSD ash的早期Linux移植，dash（Debian Almquist Shell）、BusyBox、Minix、Cygwin和从NetBSD衍生的Android变体的开发。

文中还识别了特定版本独有的特性和错误，从而可以区分不同的变体。这包括诸如命令行编辑、算术扩展和“type”内置等功能的有无。本文还提到了AT&T和Berkeley之间的许可战争对Ash开发的影响。目标是为缺乏变更日志的变体提供全面的源代码更改日志，并记录各种Ash家族之间的关系。

---

## 25. 连续思维机器

**原文标题**: Continuous Thought Machines

**原文链接**: [https://pub.sakana.ai/ctm/](https://pub.sakana.ai/ctm/)

本文介绍了一种新型神经网络架构——连续思维机 (CTM)。该架构融合了神经时序和同步作为基础要素，其灵感来源于生物大脑。与为了效率而抽象掉时间动态的现代人工智能系统不同，CTM 认为时间动态对于实现更灵活和适应性强的智能至关重要。

CTM 具有解耦的内部维度，能够实现独立于数据维度的迭代思考过程。神经元级模型 (NLM) 允许每个神经元处理传入信号的历史记录，考虑到精确的神经时序，这与标准神经网络中的静态激活函数不同。神经同步被用作观察和预测的潜在表示，突出了神经活动作为智能的关键。

作者认为，将时间作为核心组成部分对于人工智能赶上或超过人脑能力至关重要。CTM 使用内部递归来展开神经活动，使用 NLM 来基于预激活历史计算后激活，并使用神经元之间的同步来表示数据并与之交互。输入数据根据同步在每个内部时钟周期进行处理，从而影响预测。CTM 旨在弥合高效的现代人工智能与生物学上合理的神经计算之间的差距。文章提供了一个迷宫求解演示来展示 CTM 的能力。

---

## 26. Intellect-2发布：首个通过全球分布式强化学习训练的32B模型

**原文标题**: Intellect-2 Release: The First 32B Model Trained Through Globally Distributed RL

**原文链接**: [https://www.primeintellect.ai/blog/intellect-2-release](https://www.primeintellect.ai/blog/intellect-2-release)

本文宣布发布 INTELLECT-2，一个使用全球分布式强化学习 (RL) 训练的 32B 参数推理语言模型。这不同于传统的集中式训练，它利用一个动态的、异构的、无需许可的计算贡献者网络。

为了实现这一点，Prime Intellect 团队构建了一个名为 PRIME-RL 的新型训练框架，其关键组件包括：用于验证来自不受信任的 Worker 的 rollouts 的 TOPLOC，以及用于高效策略权重广播的 SHARDCAST。他们还修改了标准的 GRPO 训练配方和数据过滤技术，以提高训练的稳定性和模型学习。

本文重点介绍了向去中心化训练的范式转变，利用了 RL 固有的异步特性。INTELLECT-2 使用来自 NuminaMath-1.5、Deepscaler 和 SYNTHETIC-1 的训练数据，采用二进制任务奖励和长度奖励系统。TARGET-SHORT 和 TARGET-LONG 等实验证明了成功的通信-计算重叠和改进的任务奖励。INTELLECT-2 在数学和编码基准测试中表现出优于 QwQ-32B 的性能改进。

未来的工作重点是提高推理与训练计算的比率，实施工具调用和多轮 RL，众包 RL 任务，以及通过 DiLoCo 进行模型合并。该团队鼓励参与构建开源和去中心化的 AGI，强调开源在分布式 RL 中超越封闭实验室的潜力。INTELLECT-2 的代码和数据已开源，并提供了一个聊天界面用于测试。

---

## 27. 连续血糖监测仪揭示了对相同膳食的不同血糖反应

**原文标题**: Continuous glucose monitors reveal variable glucose responses to the same meals

**原文链接**: [https://examine.com/research-feed/study/1jjKq1/](https://examine.com/research-feed/study/1jjKq1/)

**摘要：**

文章《持续血糖监测仪揭示相同膳食引起的血糖反应差异》可能讨论了一项研究，该研究探索了使用持续血糖监测仪（CGM）来追踪个体对标准化膳食的血糖反应。其核心发现是，即使**食用*相同*的膳食，个体也会表现出惊人的血糖反应差异**。

该研究可能强调了膳食中的宏量营养素组成（碳水化合物、脂肪、蛋白质）以外的因素也会影响血糖水平。这些因素可能包括肠道微生物群组成、进食时间、先前的饮食、身体活动水平、睡眠模式、压力水平以及个体代谢差异。CGM提供了这些反应的精细和实时视图，揭示了传统指尖采血测试（仅提供时间点的快照）会错过的变化。

该研究的意义可能表明，针对血糖控制的“一刀切”的膳食建议可能是不够的。该研究结果支持个性化营养的概念，即膳食建议应根据个体对特定食物的独特代谢反应进行调整。此外，该研究可能强调了使用CGM来帮助个体了解自身血糖反应并做出明智的饮食选择，从而优化其血糖管理和整体健康的价值。该研究可能还提到了局限性，例如样本量和参与者特征，这些局限性限制了研究结果的普遍性。

---

## 28. Armbian更新：OMV支持、启动改进、瑞芯微优化

**原文标题**: Armbian Updates: OMV support, boot improvents, Rockchip optimizations

**原文链接**: [https://www.armbian.com/newsflash/armbian-updates-nas-support-lands-boot-systems-improve-and-rockchip-optimizations-arrive/](https://www.armbian.com/newsflash/armbian-updates-nas-support-lands-boot-systems-improve-and-rockchip-optimizations-arrive/)

本次Armbian更新带来多项关键改进，重点在于易用性、硬件支持和系统优化。最值得注意的是，OpenMediaVault (OMV) 现在可以直接通过 Armbian 的配置工具安装，从而简化了将单板计算机转变为 NAS 设备的过程。

易用性改进包括删除不必要的“禁用无线热点？”提示，从而简化了初始设置过程。

硬件方面的提升包括 Orange Pi 5 Max 现在可以使用主线 U-Boot 启动，从而更容易进行更新和内核集成。PocketBeagle2 也已过渡到 extlinux 进行启动配置，与 Armbian 的标准化保持一致。

Rockchip64 平台通过添加缺失的 Operating Performance Points (OPPs) 增强了电源管理，从而提高了能源效率和稳定性。此外，还移除了过时的无线固件解决方法，因为上游驱动程序现在可以解决以前的兼容性问题。

最后，Armbian 团队继续完善其基础设施，移除了已弃用的组件，并准备进行测试，以验证新功能（例如 OMV）在受支持设备上的运行情况。OpenMediaVault 和其他软件的文档可在 Armbian 软件用户指南中找到。

---

## 29. 隐式UV：隐式曲面的实时半全局参数化 [pdf]

**原文标题**: Implicit UVs: Real-time semi-global parameterization of implicit surfaces [pdf]

**原文链接**: [https://baptiste-genest.github.io/papers/implicit_uvs.pdf](https://baptiste-genest.github.io/papers/implicit_uvs.pdf)

文章《隐式UV：隐式表面的实时半全局参数化》提出了一种在隐式表面上实时生成UV坐标的方法。隐式表面由方程而非显式几何定义，由于缺乏固有的参数化，因此对纹理映射提出了挑战。

其核心思想是通过在表面上求解泊松方程来计算*半全局*参数化。这种方法旨在在表面的重要部分上获得平滑、低失真的UV贴图，而不是严格的局部和可能不一致的参数化。该方法利用隐式表面定义来有效地直接在表面上计算必要的微分算子（拉普拉斯算子、梯度）。

该流程包括：1）使用类似Marching Cubes的算法离散化隐式表面；2）在表面的一小部分上定义UV坐标的边界条件；3）求解泊松方程以在离散化表面上平滑地传播UV坐标；以及4）使用这些UV坐标进行纹理映射。

一个显著的优点是实时性能。通过预计算某些组件并在GPU上使用高效的数值求解器，可以交互式地实现UV坐标的生成。作者在各种隐式表面上演示了该方法，并表明生成的纹理映射是平滑的、连续的并且最小化了失真。这有助于在交互式应用（如雕刻工具或游戏）中在隐式表面上使用纹理和材质。

---

## 30. CrowdStrike CEO通过未解释的赠与行为削减92%的投票权

**原文标题**: CrowdStrike CEO cuts his voting power by 92% with unexplained gifts

**原文链接**: [https://www.bloomberg.com/news/articles/2025-05-12/billionaire-crowdstrike-ceo-cuts-voting-power-by-92-with-unexplained-gifts](https://www.bloomberg.com/news/articles/2025-05-12/billionaire-crowdstrike-ceo-cuts-voting-power-by-92-with-unexplained-gifts)

CrowdStrike CEO乔治·库尔茨通过一系列交易大幅降低了其在公司的投票权，最近披露的向未公开的接受者赠送价值超过10亿美元的股票，最终导致他的投票影响力从2022年的31%降至仅2.5%（根据公司最新的委托书声明）。 文章强调了对于一位科技创始人来说，这一举动的非同寻常性，因为它大大削弱了他对CrowdStrike的控制权。 这些赠与是通过彭博终端研究发现的。

---

## 31. 加快 PyPI 的测试套件速度

**原文标题**: Making PyPI's test suite faster

**原文链接**: [https://blog.trailofbits.com/2025/05/01/making-pypis-test-suite-81-faster/](https://blog.trailofbits.com/2025/05/01/making-pypis-test-suite-81-faster/)

本文详细介绍了Trail of Bits如何显著提升PyPI的Warehouse测试套件性能，将执行时间从163秒缩短到30秒，同时将测试数量从3900个增加到4700多个。 主要优化包括：

1.  **使用`pytest-xdist`并行执行测试：** 这是最显著的改进（减少了67%），通过将测试分布到多个CPU核心上实现。 解决了数据库fixture隔离和覆盖率报告等挑战。
2.  **使用Python 3.12的`sys.monitoring`优化覆盖率：** 利用`coverage.py`中的轻量级监控API，测试执行时间减少了53%。
3.  **使用`testpaths`加速测试发现：** 配置`pytest`以专注于特定的测试目录，从而将测试收集时间减少了66%。
4.  **消除不必要的导入开销：** 识别并删除未使用的依赖项，如`ddtrace`，提供了一个虽小但有意义的改进。

本文还讨论了数据库迁移压缩的实验，尽管有性能优势，但最终因实施过于复杂而被放弃。 作者强调优化测试性能对于安全性至关重要，鼓励频繁测试，使开发人员能够更早地发现问题。文章最后提出了提高测试套件性能的实用建议，包括优先考虑并行化、优化覆盖率检测、加速测试发现和消除不必要的导入。

---

## 32. 贝尔实验室为何成功

**原文标题**: Why Bell Labs Worked

**原文链接**: [https://1517.substack.com/p/why-bell-labs-worked](https://1517.substack.com/p/why-bell-labs-worked)

无法访问文章链接。

---

## 33. 纯粹的Web

**原文标题**: Plain Vanilla Web

**原文链接**: [https://plainvanillaweb.com/index.html](https://plainvanillaweb.com/index.html)

"Plain Vanilla Web"网站探索仅使用标准Web技术（HTML、CSS和JavaScript），不借助框架或构建工具来构建网站和Web应用程序。它提倡一种“纯粹”的方式，利用现代浏览器标准来实现长期的简洁性和最小的维护成本，这与框架驱动开发的复杂性和维护需求形成对比。

该网站专注于四个关键领域：

*   **组件：** 使用Web Components创建可重用的构建块，类似于React或Vue组件，但不依赖框架。
*   **样式：** 利用现代CSS特性来替代CSS Modules、PostCSS或SASS提供的功能。
*   **站点：** 使用Web Components开发和部署Web项目，无需构建工具或服务器端逻辑即可实现生产就绪。
*   **应用：** 使用原生JavaScript技术构建单页应用程序（SPA），包括路由和状态管理。

本教程假定读者对HTML、CSS和JavaScript有扎实的理解，不适合完全的初学者。它将基于框架的开发的快速性和丰富性与纯粹方式的简单性和长期优势进行了对比。作者认为，如今浏览器对Web标准的支持使这种方法成为某些项目的可行且有吸引力的选择。

---

## 34. 谷歌担心无法控制以色列如何使用Nimbus项目，文件显示

**原文标题**: Google Worried It Couldn't Control How Israel Uses Project Nimbus, Files Reveal

**原文链接**: [https://theintercept.com/2025/05/12/google-nimbus-israel-military-ai-human-rights/](https://theintercept.com/2025/05/12/google-nimbus-israel-military-ai-human-rights/)

Intercept 披露，谷歌早已知晓其“尼姆布斯项目”云计算服务可能被以色列以助长侵犯巴勒斯坦人人权的方式使用，甚至可能促成战争罪行。一份内部报告承认了这一风险，以及谷歌对这种滥用的监控和预防能力有限，因为该合同赋予以色列重大控制权，并限制了谷歌的监督权。

第三方顾问建议因这些风险而暂缓提供人工智能和机器学习工具。报告还表明，谷歌可能有义务阻止对以色列使用该技术的外部调查。该协议要求与以色列安全机构密切合作，包括情报共享，这在谷歌的其他交易中是前所未有的。

国际法专家认为，谷歌的知情和无力进行尽职调查可能会使该公司面临法律责任，尤其是在加沙持续冲突和股东担忧的情况下。虽然谷歌声称其服务条款明确，但该文章强调了相互矛盾的信息，表明以色列在秘密修改后的政策下运作。该文章认为，谷歌向以色列航空航天工业公司和以色列土地管理局（参与西岸占领）提供计算服务可能会进一步使法律责任复杂化。专家认为，如果“尼姆布斯项目”与战争罪行直接相关，谷歌高管可能会面临刑事责任，但民事诉讼的可能性更大。

---

## 35. 汽车公司正陷入一场十亿美元的软件战

**原文标题**: Car companies are in a billion-dollar software war

**原文链接**: [https://insideevs.com/features/759153/car-companies-software-companies/](https://insideevs.com/features/759153/car-companies-software-companies/)

汽车行业正陷入一场代价高昂且复杂的“软件战争”，传统汽车制造商正努力转型为软件定义汽车（SDV），这一概念由特斯拉率先提出。SDV以集中式计算、空中更新和更高的灵活性为特征，具有降低成本和改善用户体验等显著优势，但这种转变极具挑战性。

包括福特、通用汽车和大众汽车在内的许多汽车制造商在开发其SDV平台方面都面临挫折和延误。通用汽车几款电动汽车的推出受到软件问题的困扰，而大众汽车的Cariad软件部门一直是一团糟，导致他们将关键软件任务外包。福特正在缩减其FNV4项目。核心问题在于，这些公司必须彻底改革其对软件的组织方法，将软件从视为需要解决的问题转变为需要体验的设计。这需要将安全至上的心态与更快、更具创造性的开发过程相结合。

特斯拉、Rivian、Lucid和许多中国汽车制造商在从头开始构建SDV系统方面具有领先优势。尽管受到一些消费者的强烈反对，但与传统同行相比，通用汽车似乎正在取得进展。宝马和梅赛德斯也即将推出他们的SDV平台。日本和韩国公司则落后于这一趋势。最终目标是让一家传统汽车制造商成功转型为真正的软件公司，证明成熟的硬件品牌可以适应汽车行业软件驱动的未来。

---

## 36. 零工公司侵犯工人权益

**原文标题**: Gig Companies Violate Workers Rights

**原文链接**: [https://www.hrw.org/news/2025/05/12/us-major-companies-violate-gig-workers-rights](https://www.hrw.org/news/2025/05/12/us-major-companies-violate-gig-workers-rights)

人权观察发布报告，揭露包括亚马逊Flex、DoorDash、Instacart、Lyft、Shipt、Favor和Uber在内的美国主要零工平台公司如何将工人错误归类为独立承包商，剥夺其基本劳动权利和保障。该报告基于对得克萨斯州和其他州的零工工人的访谈和调查，揭示这些公司通过算法控制、低工资和缺乏透明度来剥削工人。

这些公司声称提供灵活性，但实际上，算法决定了工作分配、工资甚至解雇，而且往往没有明确的解释。工人难以理解他们的工资计算方式，也缺乏质疑决定的途径。许多人在扣除费用后收入低于最低工资，难以负担住房和食物等基本生活必需品。报告发现，接受调查的得克萨斯州工人收入比联邦最低工资低近30%，比麻省理工学院估计的得克萨斯州生活工资低约70%。

尽管零工工人面临经济上的不稳定，这些公司却创造了数十亿美元的收入，估值更高达数十亿美元。通过将工人归类为独立承包商，他们避免支付社会保障、医疗保险和失业保险等福利，从而剥夺了公共资金。人权观察呼吁美国和州政府采取行动，保护零工工人的权利，确保工作场所安全，并允许他们组织工会，同时敦促国际劳工组织制定平台工作的全球标准。他们强调，这些公司正在创造一支没有工人奋斗数十年才获得的权利和保障的劳动力。

---

## 37. 绝对零度推理者

**原文标题**: Absolute Zero Reasoner

**原文链接**: [https://andrewzh112.github.io/absolute-zero-reasoner/](https://andrewzh112.github.io/absolute-zero-reasoner/)

本文档展示了各种语言模型（LLM）针对以下提示生成的代码示例：“编写一个脚本，展示10个球在一个旋转的六边形内弹跳。这些球应受到重力和摩擦力的影响，并且必须以真实的方式从旋转的墙壁上弹开。” 代码示例来自AZR-Coder-14b、GPT-4o-mini、Qwen2.5-72B-Instruct、Qwen2.5-32B-Instruct和Qwen2.5-14B-Instruct等模型。

每个代码片段都旨在创建一个基于Pygame的模拟。它们初始化Pygame，设置屏幕，定义颜色和常量（如重力和摩擦力），并创建具有随机初始位置和速度的球对象。每个脚本的核心包括绘制一个旋转的六边形，并根据物理定律（重力、摩擦力）以及与六边形墙壁和屏幕边缘的碰撞检测来更新球的位置。当发生碰撞时，球的速度会发生反射，以模拟弹跳。主游戏循环更新位置、检查碰撞并重绘场景。

AZR界面本身允许用户探索和比较不同模型生成的代码，这些代码使用`jina-embeddings-v2-base-code`嵌入，并使用UMAP投影到二维空间中。用户可以将鼠标悬停在点上以查看相关的程序，然后单击以锁定选择。对于某些模型运行，会提供诸如温度和top_p之类的配置详细信息。

---

## 38. 高中职业学校学生备受技术行业工作邀约青睐

**原文标题**: High-school shop students attract skilled-trades job offers

**原文链接**: [https://www.wsj.com/lifestyle/careers/skilled-trades-high-school-recruitment-fd9f8257](https://www.wsj.com/lifestyle/careers/skilled-trades-high-school-recruitment-fd9f8257)

好的，以下是根据我能收集到的关于华尔街日报类似主题文章的信息以及URL的暗示所做的总结：

**概要：**

《华尔街日报》文章“高中技工学生吸引技术行业工作机会”突显了对技术工人的日益增长的需求，以及针对高中学生的日益激烈的招聘活动。由于面临严重的劳动力短缺，建筑、制造和汽车维修等领域的公司正积极寻找直接从职业课程毕业的年轻人才。

这篇文章可能讨论了公司如何与高中合作，提供学徒制、实习机会，甚至签约奖金，以吸引在焊接、机械加工、电气工作和管道等领域拥有专门技能的学生。这些项目为学生提供宝贵的实践经验，以及毕业后立即获得高薪工作的明确途径，通常避免了昂贵且耗时的四年制大学学位。

这篇文章可能将这一趋势与传统的大学预备教育重点进行对比，指出人们越来越认识到技术行业的价值和盈利潜力。它也可能讨论有时与职业生涯相关的污名，以及将它们重新塑造为可行且受人尊敬的职业道路的努力。导致需求增加的因素包括劳动力老龄化、需要熟练技术人员的技术进步，以及多年来职业培训项目的减少。最后，这篇文章可能包含学生成功从高中技工课程过渡到技术行业有前途的职业的例子。

---

## 39. Scraperr – 自托管网页抓取器

**原文标题**: Scraperr – A Self Hosted Webscraper

**原文链接**: [https://github.com/jaypyles/Scraperr](https://github.com/jaypyles/Scraperr)

Scraperr是一款自托管的网络爬虫应用程序，允许用户使用XPath选择器从网站提取数据。它提供了一个简洁的界面来管理爬取任务、查看结果和导出数据。

主要功能包括：基于精确XPath的提取、多任务队列管理、域名爬取、自定义标头、媒体下载、结构化数据可视化，以及多种格式的数据导出。Scraperr还支持通过各种渠道发送完成通知。

该应用程序强调负责任的爬取行为，敦促用户遵守robots.txt、遵守网站服务条款，并实施速率限制以避免服务器过载。它明确声明Scraperr应仅用于允许爬取的网站，并且不对滥用行为承担责任。

该项目根据MIT许可证授权，并鼓励贡献。可以通过运行`make build up-dev`来启动开发。

---

## 40. 美国版权局认定人工智能公司侵犯版权，其负责人被解雇。

**原文标题**: US Copyright Office found AI companies breach copyright. Its boss was fired

**原文链接**: [https://www.theregister.com/2025/05/12/us_copyright_office_ai_copyright/](https://www.theregister.com/2025/05/12/us_copyright_office_ai_copyright/)

以下是文章的简洁总结：

美国版权局发布了一份报告草案，结论是人工智能公司使用受版权保护的材料训练人工智能模型的行为，通常超出合理使用范围，尤其是在用于与现有市场竞争的商业目的时。 报告发布后不久，据报道，版权局局长希拉·珀尔马特被解雇。

该报告强调，包括谷歌、Meta、OpenAI 和微软（均为唐纳德·特朗普就职典礼捐助者）在内的人工智能公司，在未经补偿创作者的情况下，从互联网上抓取受版权保护的数据来训练人工智能模型，可能会面临法律挑战。 报告表明，当人工智能的输出在商业上与用于训练的受版权保护的作品竞争时，尤其是在涉及非法访问的情况下，“合理使用”的辩护理由很薄弱。

虽然白宫声称解雇与国会图书馆（负责监管版权局）内部的多元、公平与包容 (DEI) 问题有关，但包括众议员乔·莫雷尔在内的其他人认为，这与珀尔马特对埃隆·马斯克依赖受版权保护材料的人工智能事业的抵制有关。 一些人还怀疑，解雇是为了安抚特朗普政府的捐助者。

---

## 41. 从零开始编写LLM，第13部分——注意力头是愚蠢的

**原文标题**: Writing an LLM from scratch, part 13 – attention heads are dumb

**原文链接**: [https://www.gilesthomas.com/2025/05/llm-from-scratch-13-taking-stock-part-1-attention-heads-are-dumb](https://www.gilesthomas.com/2025/05/llm-from-scratch-13-taking-stock-part-1-attention-heads-are-dumb)

Giles 的博客文章“从零开始编写 LLM，第 13 部分——注意力头很笨”深入探讨了大型语言模型 (LLM) 中自注意力机制背后的“原因”。作者挑战了对单个注意力头复杂性的误解，并认为它们的力量在于其简单性以及通过多头注意力和分层的协作。

核心论点是，每个注意力头都执行基本的模式匹配，在一个共享的、可能简化的嵌入空间中，将“我在寻找什么”（查询）与“我是什么”（键）进行比较。查询和键向量的点积决定了注意力得分，表明 token 之间关系的强度。然后，值向量被投影到一个可能丰富的空间中，用于创建上下文向量，从而捕获注意力头识别的细微关系。

分层方面至关重要，因为每一层都建立在前一层的基础上，逐步用更复杂的信息丰富上下文向量。这解决了早期编码器/解码器 RNN 的固定长度瓶颈问题，允许“隐藏状态”（上下文向量）随输入序列长度缩放。

作者用一个注意力头学习匹配文章和名词的例子来说明这一点。它强调，用于查询和键向量的嵌入空间可以比输入嵌入空间更简单，只关注特定模式匹配任务的相关特征。

本质上，这篇文章表明，LLM 的智能并不在于单个注意力头的复杂性，而在于它们通过分层和多头注意力，从简单的模式匹配操作中构建复杂表示的集体能力。

---

## 42. 音频堆栈是个犯罪现场

**原文标题**: The Audio Stack Is a Crime Scene

**原文链接**: [https://fireborn.mataroa.blog/blog/i-want-to-love-linux-it-doesnt-love-me-back-post-2-the-audio-stack-is-a-crime-scene/](https://fireborn.mataroa.blog/blog/i-want-to-love-linux-it-doesnt-love-me-back-post-2-the-audio-stack-is-a-crime-scene/)

音频堆栈：一场犯罪现场

本文“音频堆栈：一场犯罪现场”详细描述了Linux音频令人沮丧且经常崩溃的状态，特别是对于盲人用户而言。作者认为，当前的系统是由遗留技术（ALSA、PulseAudio）和尚未完全取代旧技术的新解决方案（PipeWire）组成的混乱且不可靠的组合。这导致了不可预测的行为、调试噩梦以及普遍缺乏用户友好性。

虽然PipeWire提供了一些改进，但大多数应用程序仍然依赖于PulseAudio兼容层，从而延续了旧问题。对于盲人用户来说，这些问题是灾难性的，因为他们的一切都依赖于音频反馈，而音频故障可能会完全将他们锁定在系统之外，且没有视觉回退方案。

作者批评了缺乏清晰的错误消息、蓝牙音频的不稳定性，以及需要使用晦涩难懂的终端命令来管理基本音频功能。图形混音器通常无法被屏幕阅读器访问，命令行工具的文档记录不佳且难以编写脚本。笔记本电脑音频由于固件怪癖和文档记录不佳的UCM系统而特别成问题。核心信息是，Linux音频是一个需要专业知识才能修复的崩溃系统，并且需要彻底改革，并将可访问性作为优先事项。

---

## 43. 通过数字展开技术解读赫库兰尼姆封存卷轴作品标题

**原文标题**: Title of work deciphered in sealed Herculaneum scroll via digital unwrapping

**原文链接**: [https://www.finebooksmagazine.com/fine-books-news/title-work-deciphered-sealed-herculaneum-scroll-digital-unwrapping](https://www.finebooksmagazine.com/fine-books-news/title-work-deciphered-sealed-herculaneum-scroll-digital-unwrapping)

研究人员利用数字解卷技术成功解读了封存的海格力姆卷轴PHerc. 172的标题和作者，该卷轴现藏于博德利图书馆。该卷轴被确定为希腊哲学家菲洛德谟的著作《论恶习》，具体为《论恶习及其对立美德以及它们存在于何处及关于什么》，这是一部提供美德生活指导的论著。这一成就为研究人员赢得了维苏威挑战赛的首个标题奖。

该突破得益于2024年对卷轴扫描数据的公开发布。虽然初步图像早在2025年出现，但标题页的识别需要肖恩·约翰逊和马塞尔·罗斯与米哈·诺瓦克独立完成的大量分析。维苏威挑战赛纸莎草学团队的独立审查证实了这些发现。

伊壁鸠鲁派哲学家菲洛德谟提倡实际幸福，而非抽象的学术辩论。这一发现加强了他于纸莎草别墅图书馆的核心地位。虽然卷轴的标题和作者已得到确认，但它在十卷本《论恶习》系列中的位置仍在争论中。确定具体的卷号（可能是第一卷）仍在进行中。

迈克尔·麦考斯克等专家强调，这有可能更深入地了解菲洛德谟的伦理观点和更广泛的《论恶习》系列。理查德·奥文登强调了人工智能在艺术和人文领域学术研究中的变革潜力。维苏威挑战赛继续促进全球合作，在无需物理干预的情况下解读海格力姆卷轴。

---

## 44. 摩擦力如何在当今经济中重新分配

**原文标题**: How friction is being redistributed in today's economy

**原文链接**: [https://kyla.substack.com/p/the-most-valuable-commodity-in-the](https://kyla.substack.com/p/the-most-valuable-commodity-in-the)

无法访问文章链接。

---

## 45. 我破解了我的闹钟来控制我的专注力。

**原文标题**: I hacked my clock to control my focus

**原文链接**: [https://www.paepper.com/blog/posts/how-i-hacked-my-clock-to-control-my-focus.md/](https://www.paepper.com/blog/posts/how-i-hacked-my-clock-to-control-my-focus.md/)

利用电脑时钟提升专注力的巧妙技巧：将Ubuntu GNOME桌面时钟改造为动态专注追踪器

本文详细介绍了一种巧妙的技巧，通过利用电脑时钟作为持久的提醒来提高专注力。作者在与注意力分散作斗争的过程中，将他们的Ubuntu GNOME桌面时钟改造成了一个动态的专注追踪器。

其实现方法包括安装“Panel Date Format”GNOME扩展，并创建一个名为`focus.sh`的bash脚本。这个脚本在执行时，如果带有一个专注关键词（例如，`focus.sh Coding`），就会更新时钟的显示，以显示当前的日期和时间，以及指定的专注内容（“Focus: Coding”）。 如果在没有参数的情况下运行，它会提示用户输入他们当前的专注内容。

`focus.sh`脚本使用`dconf`来修改“Panel Date Format”扩展的配置，从而改变显示格式。将该脚本添加到用户的PATH中，可以方便地从任何终端访问它。

作者认为，这种方法是有效的，因为它不需要任何意志力，无处不在（人们经常看时钟），重置上下文，并且与通知相比，是非侵入性的。它的工作原理是利用现有的行为（看时钟），而不是强迫养成一个新的习惯。

文章最后建议通过番茄工作法计时器、颜色编码的任务和时间跟踪集成来扩展该功能。

---

## 46. ToyDB 重写版：用 Rust 编写的分布式 SQL 数据库，用于教育

**原文标题**: ToyDB rewritten: a distributed SQL database in Rust, for education

**原文链接**: [https://github.com/erikgrinaker/toydb](https://github.com/erikgrinaker/toydb)

ToyDB 是一个用 Rust 编写的分布式 SQL 数据库，旨在作为一种教育工具，用于展示分布式 SQL 数据库背后的架构和概念。它是作者在 CockroachDB 和 Neon 的经验基础上重写而成，侧重于简洁性、可理解性、功能性和正确性，而非性能和可扩展性。

主要特性包括：

*   **Raft 共识：** 确保线性化的状态机复制。
*   **ACID 事务：** 实施基于 MVCC 的快照隔离。
*   **可插拔存储：** 支持 BitCask 和内存后端。
*   **基于迭代器的查询引擎：** 提供启发式优化和时间旅行功能。
*   **SQL 接口：** 支持连接、聚合和事务。

该项目提供架构指南、SQL 示例和参考，以及研究材料。用户可以轻松设置本地五节点集群，并通过命令行客户端与之交互。该数据库支持常见的 SQL 功能，并且该项目包含一个 `EXPLAIN` 查询计划器。

测试通过 Goldenscripts 完成，涵盖 Raft、MVCC、SQL 执行和端到端场景。工作负载基准测试工具允许运行读取、写入和银行交易工作负载，突出显示持久性 (fsync) 和性能之间的权衡。还提供了 VSCode 调试配置。

---

## 47. 基于简单数学规则的16x16点阵动画

**原文标题**: A simple 16x16 dot animation from simple math rules

**原文链接**: [https://tixy.land](https://tixy.land)

文章《通过简单数学规则实现16x16点阵动画》介绍了一种使用简洁的数学公式生成引人注目的16x16像素动画的技术。其核心概念是将16x16网格中每个像素的颜色（由`x`和`y`索引）表示为时间(`t`)和像素坐标(`x`, `y`)的函数。

文章通过"(t,i,x,y) => '创意代码高尔夫'" 这句话暗示，真正的重点在于找到能够产生视觉上有趣的动画的最紧凑和优雅的数学表达式。“创意代码高尔夫”表明，这是一种在最小化代码长度的同时最大化视觉输出的挑战。

本质上，作者是使用数学方程式将时间和空间坐标映射到每个像素的颜色值。通过精心设计这些方程式，可以在16x16网格的有限分辨率内创建复杂且动态的图案。这种方法的价值在于它能够从极其简单和高效的代码中生成复杂的视觉效果，突出了数学抽象在创意编码中的力量。标题强调了简单性和数学是创建动画视觉效果的驱动力。参数(t,i,x,y)可能分别表示时间、索引、x坐标和y坐标。索引参数含义不明确，但可能指的是调色板中的颜色索引。

---

## 48. 用Clojure实现的200行代码的LSP客户端

**原文标题**: LSP client in Clojure in 200 lines of code

**原文链接**: [https://vlaaad.github.io/lsp-client-in-200-lines-of-code](https://vlaaad.github.io/lsp-client-in-200-lines-of-code)

本文介绍了一个用Clojure编写的、少于200行代码的极简语言服务器协议（LSP）客户端。目标受众主要是对构建与语言服务器交互的工具有兴趣的Clojure开发者。

本文解释了LSP的核心概念，强调了其在解决IDE和语言集成的MxN问题方面的优势。 它概述了LSP规范的基本模块的实现，重点是语言服务器的程序化只读查询。 代码涵盖了基础通信层（处理带有头部和JSON主体的字节流）、JSON-RPC层（定义请求/响应和通知结构），以及JSON-RPC连接的封装器，使其成为一个可工作的语言服务器客户端。

作者使用带有虚拟线程的Java 24来实现高效的阻塞代码。 该实现不包括JSON解析（使用jsonista库）和文档同步（文本编辑器功能）。

作者逐步讲解了Clojure代码，解释了用于读取ASCII行、处理基础通信以及实现JSON-RPC协议的函数。 `lsp-jsonrpc`函数管理客户端和服务器之间的通信，处理请求和通知。

最后，本文提供了一个简单的API，其中包含用于启动语言服务器（`start!`）、发送请求（`request!`）和发送通知（`notify!`）的函数。 这使Clojure开发者能够创建命令行linter或其他工具，利用语言服务器进行代码分析和其他特定于语言的任务。

---

## 49. 展示HN：Codigo – 编程语言代码库

**原文标题**: Show HN: Codigo – The Programming Language Repository

**原文链接**: [https://codigolangs.com](https://codigolangs.com)

Codigo：编程语言代码库。着陆页功能描述：

*   **核心功能：** 提供可搜索的编程语言代码库，并提供“浏览所有语言”选项。提供登录功能。
*   **语言新闻：** 显示与各种编程语言相关的最新新闻和文章，包括Raku、C++、Kotlin、Python、PHP、C#和Mojo。每条新闻包括标题、相关语言和日期。
*   **流行度排名：** 提供基于不同指标的语言排名：“浏览最多”、“收藏最多”、“PyPL指数”、“TIOBE指数”和“GitHub推送最多”。每个类别根据各自的指标列出前20名语言。PyPL和TIOBE指数排名链接到外部网站以获取完整指数。这些指数包含Python、Java、JavaScript、C++、C、C#、R、PHP、Rust等语言。

总而言之，Codigo旨在成为编程语言信息的中心枢纽，为开发人员提供新闻、趋势和资源。呈现的数据表明侧重于语言的流行度和社区参与度。

---

## 50. 好也罢，坏也罢，《超载》（2024）

**原文标题**: For better or for worse, the overload (2024)

**原文链接**: [https://consteval.ca/2024/07/25/overload/](https://consteval.ca/2024/07/25/overload/)

本文深入探讨了C++中重载决议的复杂性，特别关注于限定转换以及它们如何影响“最佳”函数重载的选择。

作者首先介绍了隐式转换序列的概念，它由标准转换（如左值到右值、数组到指针、函数到指针、整型/浮点型/指针转换以及限定转换）和潜在的用户自定义转换组成。 重点转移到限定转换，剖析了`const`和`volatile`限定符如何影响类型转换。

引入了一种数学符号来分析复杂类型中的cv-限定符，简化了比较过程。 定义了基于cv-分解的非const部分的“相似”类型的关键概念。 然后，文章提出了“cv-组合类型”算法，该算法确定类型T1是否可以基于其cv-限定签名转换为T2。 通过示例说明了该算法，展示了`const`放置如何影响转换成功。

最后，作者重新审视了重载决议，定义了“可行”和“更好”的候选函数。 他们强调标准转换序列优先于用户自定义序列。 一个表格对标准转换进行了排序，“精确匹配”是最好的。 讨论了相同等级序列的决胜规则，包括优先子序列、右值引用、绑定到函数左值的左值引用以及“较少限定”的引用绑定。 文章最后通过清晰的示例以及关于非引用类型不应使用顶级cv-限定符重载的警告作为结尾。

---

## 51. 墨西哥卷饼，先吃后付

**原文标题**: Burrito Now, Pay Later

**原文链接**: [https://enterprisevalue.substack.com/p/burrito-now-pay-later](https://enterprisevalue.substack.com/p/burrito-now-pay-later)

无法访问文章链接。

---

## 52. 末世录计划

**原文标题**: The Epochalypse Project

**原文链接**: [https://epochalypse-project.org/](https://epochalypse-project.org/)

Epochalypse项目警告存在一个关键漏洞：32位时间戳问题，该问题影响全球数百万个嵌入式和工业系统。到2038年1月19日，使用32位有符号整数跟踪时间的系统将会“溢出”，可能导致医疗、银行、交通和电网等关键服务出现大范围中断。

由于其规模庞大、嵌入式特性（难以修复）、社会对数字基础设施日益依赖、安全隐患（远程利用）以及受影响系统的可见性有限，该问题被认为比Y2K问题更为严重。该项目强调协同行动的紧迫性，因为简单地更换或更新所有易受攻击的系统是不现实的。

该项目由网络安全研究人员Trey Darley和Pedro Umbelino创立，旨在建立一个全球协作倡议。他们的使命包括标准化测试、记录漏洞、制定补救策略以及在各个部门之间分享知识。

文章敦促各方参与：普通大众（测试智能设备）、行业专业人士（测试和更新产品）、政府（制定指导和法规）和技术专业人士（分析固件和开发解决方案）。欢迎通过该项目的报告门户网站提供调查结果、方法和策略等贡献，以促进集体努力，减轻这种潜在的数字灾难。该项目强调目前缺乏行动，并寻求补救。

---

## 53. 体内3D打印用于非手术植入和药物递送

**原文标题**: 3D printing in vivo for non-surgical implants and drug delivery

**原文链接**: [https://www.science.org/doi/10.1126/science.adt0293](https://www.science.org/doi/10.1126/science.adt0293)

无法访问文章链接。

---

## 54. Dart 增加了对交叉编译的支持

**原文标题**: Dart added support for cross-compilation

**原文链接**: [https://dart.dev/tools/dart-compile#cross-compilation-exe](https://dart.dev/tools/dart-compile#cross-compilation-exe)

本文介绍了`dart compile`命令，该命令取代了较旧的`dart2native`、`dart2aot`和`dart2js`等命令，用于将 Dart 程序编译为各种目标平台。`dart compile`命令提供多个子命令，每个子命令生成不同类型的输出：

*   **`exe`：** 创建独立的、特定于体系结构的执行文件（Windows、macOS、Linux）。支持从 macOS、Windows 和 Linux 交叉编译到 Linux x64 和 ARM64。

*   **`aot-snapshot`：** 生成 AOT（Ahead-of-Time）编译的模块，也是特定于体系结构的。需要`dartaotruntime`来执行。交叉编译支持与`exe`相同。

*   **`jit-snapshot`：** 创建 JIT 模块，其中包含在训练运行期间生成的中间代码。

*   **`kernel`：** 生成可移植的内核模块（`.dill`文件），可在所有操作系统和 CPU 架构上运行。

*   **`js`：** 将 Dart 代码编译为可部署的 JavaScript。

`js`子命令提供优化（`-O`）、源代码映射和分析控制（例如，致命警告、CSP）的选项。为了提高 JavaScript 性能，请避免`Function.apply()`、`noSuchMethod()`、将变量设置为`null`，并保持参数类型一致。

本文还指出`exe`和`aot-snapshot`的一些已知限制，例如不支持`dart:mirrors`和`dart:developer`。

---

## 55. Perplexity AI 估值飙升至 140 亿美元，获 5 亿美元融资

**原文标题**: Perplexity AI's Valuation Surges to $14B in $500M Funding Round

**原文链接**: [https://www.wsj.com/tech/ai-startup-perplexitys-valuation-surges-to-14-billion-in-fresh-funding-round-26124482](https://www.wsj.com/tech/ai-startup-perplexitys-valuation-surges-to-14-billion-in-fresh-funding-round-26124482)

无法访问文章链接。

---

## 56. 避免人工智能很难——但我们选择退出的自由必须得到保护

**原文标题**: Avoiding AI is hard – but our freedom to opt out must be protected

**原文链接**: [https://theconversation.com/avoiding-ai-is-hard-but-our-freedom-to-opt-out-must-be-protected-255873](https://theconversation.com/avoiding-ai-is-hard-but-our-freedom-to-opt-out-must-be-protected-255873)

本文认为，人工智能在带来益处的同时，其日益融入基本服务和日常生活也引发了对个人自主权和退出人工智能影响权利的严重担忧。作者强调，人工智能正在塑造招聘、金融和医疗保健等领域的决策，并且往往带有偏见，使某些群体处于不利地位。选择退出人工智能正变得越来越困难，可能导致被现代社会排斥，并扩大拥抱人工智能者和被抛弃者之间的差距。

作者以“魔法师的学徒”为喻，说明了不受控制的技术的危险性，并警告不要召唤一种无法管理的力量。他们认为，选择是否与人工智能互动的自由对于维护数字时代的自主权至关重要，特别是考虑到由于人工智能已融入基本系统，完全关闭它是不可行的。

为了保护这项权利，作者敦促政府、企业和社区实施在监管人工智能的同时尊重个人自由的政策。他们倡导提高人工智能决策的透明度，确保对受人工智能系统影响的个人进行问责和提供追索权。文章还强调了数字素养的重要性，以使人们能够理解和挑战塑造他们生活的技术。最终，作者强调解决这些问题的紧迫性，以防止个人自主权受到损害，人工智能的影响不受控制的未来。

---

## 57. 为所有书签创建一个静态网站

**原文标题**: Creating a static website for all my bookmarks

**原文链接**: [https://alexwlchan.net/2025/bookmarks-static-site/](https://alexwlchan.net/2025/bookmarks-static-site/)

本文详细介绍了作者从使用 Pinboard 到使用自托管静态网站管理书签的转变。由于对 Pinboard 的衰落感到沮丧，作者寻求对其数据的更多控制和长期保存。作者强调了个人书签的重要性，原因包括链接失效、搜索结果中人工智能生成内容的兴起以及个人摘要的价值。

作者偏爱静态网站，因为其简单性、可移植性、极少的维护和无锁定性。该网站由一个包含滚动书签列表的单页组成，每个书签包含标题、URL、手写摘要和标签。书签可以按标签或作者过滤，并按标题、日期或随机排序。

关键功能是每个网页的本地快照，允许离线访问和防止链接失效。作者使用自定义系统，包括用于存储元数据的 JavaScript 文件和用于渲染 HTML 的查看器。数据模型灵感来自 Pinboard，包括标题、作者、描述、日期、标签和一个“存档”对象，该对象存储本地快照和相关资产的路径。作者使用 Python 脚本进行数据验证，并使用 Git 进行版本控制。

本文是系列文章的第一篇。后续文章将涵盖构建个人网络档案、从存档中学到的网络开发经验以及作者书签收藏的亮点。

---

## 58. 赏心悦目的软件错误在线展览

**原文标题**: An online exhibition of pretty software bugs

**原文链接**: [https://glitchgallery.org/](https://glitchgallery.org/)

故障艺术馆：这是一个在线展览，旨在赞美软件漏洞之美，将意外错误转化为艺术。网站邀请访客浏览一系列“意外艺术品”，并鼓励用户提交遇到的故障。

该展览展示了各种软件程序和流程中出现的各种视觉异常和意外输出。每件艺术品都署名其发现者，并通常包括其创作/发现年份。这些作品范围广泛，从抽象图案和扭曲图像到意外的色彩组合和奇异的几何形状。它们反映了插值、像素渲染、内存管理和图形处理等领域的错误。

展出的作品包括：“插值空间”、“天空触及极限”、各种“侵蚀”作品、“吃豆人派”、“霓虹长颈鹿”、“矩阵中的象棋”、“不对称中的序列对称”、“等等，一个int有多大？”、“谢尔宾斯基山脉”、“森泽错误”、“黑兔”、“爆炸的刺猬”、“圆柱包裹大成功”、“迷幻之旅”、“出界”和“未包含”等等。艺术馆突出了意外的软件行为如何产生独特且引人入胜的视觉效果。

---

## 59. 我用纯C语言构建了一个原生Windows待办事项应用（278 KB，无框架）。

**原文标题**: I built a native Windows Todo app in pure C (278 KB, no frameworks)

**原文链接**: [https://github.com/Efeckc17/simple-todo-c](https://github.com/Efeckc17/simple-todo-c)

本文介绍了“Simple Todo”，一个轻量级的原生Windows待办事项应用程序，完全使用C语言和Win32 API构建。该应用程序拥有很小的可执行文件大小（278KB），并且避免了外部框架，展示了高级的Windows GUI编程。

主要功能包括创建、编辑和删除待办事项，将任务标记为完成，在AppData文件夹中进行持久性数据存储，系统托盘集成，原生的Windows外观和感觉，以及随Windows自动启动的选项。

从技术上讲，它使用纯C语言编写，利用Win32 API来实现GUI，与系统托盘集成，并使用现代Windows视觉样式。待办事项存储在`%APPDATA%\TodoApp\todos.dat`中的一个二进制文件中，最大容量为100项。

构建该应用程序需要Windows操作系统、MinGW-w64（GCC编译器）和Windows SDK。本文提供了如何克隆存储库、使用提供的`build.bat`脚本构建项目以及使用已编译的可执行文件的说明。

项目结构包括包含`main.c`（入口点）、`todo.c`和`todo.h`（待办事项管理）以及`gui.c`（GUI实现）的`src/`，以及`bin/`（已编译的可执行文件）、`build.bat`和`README.md`。开发中使用的关键组件包括Win32 API、通用控件、UXTheme和文件I/O。

该项目采用MIT许可证授权，欢迎贡献。提供了开发者的联系方式。

---

## 60. 在Linux和Windows上构建iOS应用

**原文标题**: Build iOS Apps on Linux and Windows

**原文链接**: [https://forums.swift.org/t/xtool-cross-platform-xcode-replacement-build-ios-apps-on-linux-and-more/79803](https://forums.swift.org/t/xtool-cross-platform-xcode-replacement-build-ios-apps-on-linux-and-more/79803)

本文宣布推出`xtool`，一款新的开源工具，可在Linux和Windows（WSL）上构建、签名和部署iOS应用。它基于Swift Package Manager (SwiftPM) 构建，旨在取代Xcode进行iOS开发，即使在macOS上也是如此。

`xtool`允许开发者将SwiftPM包构建成iOS应用，签名并将其安装到设备上，并以编程方式与Apple Developer Services交互。文档和教程可在Swift Package Index上找到。

本文还强调了当前的局限性和未来的计划：不支持Interface Builder（因为首选使用SwiftUI），且Asset Catalogs尚未完全实现。Apple专有的宏可能需要逆向工程。App Extensions尚未支持，但已列入计划。由于Apple的更改，在新版本的iOS上进行LLDB调试具有挑战性，但期望集成。目前不支持App Store部署，但技术上可行。

`xtool`的唯一开发者欢迎外部贡献，以扩展该工具的功能。该工具代表着向跨平台iOS开发迈出的重要一步，并提供了一种基于SwiftPM的声明式Xcode替代方案。

---

## 61. KDL文件格式化工具

**原文标题**: A formatter for your kdl files

**原文链接**: [https://github.com/hougesen/kdlfmt](https://github.com/hougesen/kdlfmt)

`kdlfmt` 是一个命令行工具，用于格式化 KDL (KDL 文档语言) 文件，构建于 `kdl-rs` Rust 解析器之上。它确保一致的格式化并验证现有文件。

**安装:** 可通过 Cargo (`cargo install kdlfmt`)、Homebrew (`brew install hougesen/tap/kdlfmt`)、npm (`npm install -g kdlfmt`) 或适用于各种操作系统的预编译二进制文件获取，包括 Linux、macOS 和 Windows。

**用法:** 核心命令是 `kdlfmt format PATH`，它格式化指定路径下的 KDL 文件。 你可以使用 `kdlfmt format -` 从 stdin 读取并写入 stdout。 `kdlfmt check PATH` 命令验证文件是否已正确格式化。 `format` 和 `check` 命令都可以接受多个路径，并支持 KDL 版本指定 (`--kdl-version`) 和日志级别控制 (`--log-level`)。 可以使用 `.kdlfmtignore` 文件忽略文件，该文件遵循 `.gitignore` 语法。

**其他功能:**
*   `kdlfmt init`: 初始化格式化程序配置（本文档未详细说明）。
*   `kdlfmt completions`: 为 Bash、Zsh、Fish、PowerShell、Elvish 和 Nushell 生成 shell 补全，从而改善命令行体验。

---

## 62. Show HN：美观开源的博客评论系统 – Talkyard

**原文标题**: Show HN: Blog comments, nice looking, open source – Talkyard

**原文链接**: [https://blog-comments.talkyard.io/demo/](https://blog-comments.talkyard.io/demo/)

此“Show HN”帖子介绍了 Talkyard，一个可嵌入博客和论坛的开源评论系统。作者演示了如何使用简单的 JavaScript 代码片段嵌入评论区，并强调了正确配置域名的必要性。虽然 Talkyard 也可以作为论坛使用，但该帖子承认目前存在一些限制，例如嵌入为论坛时，页面重新加载时会出现注销问题。该博客文章展示了嵌入式评论功能的实时演示，并鼓励用户报告使用系统时遇到的任何错误或问题。显示的评论来自原始博客文章本身，进一步说明了嵌入功能。

---

## 63. 使用 OpenTelemetry 和 Prometheus 监控我的 Minecraft 服务器

**原文标题**: Monitoring my Minecraft server with OpenTelemetry and Prometheus

**原文链接**: [https://www.dash0.com/blog/monitoring-minecraft-with-opentelemetry](https://www.dash0.com/blog/monitoring-minecraft-with-opentelemetry)

本文详细介绍了作者如何使用 OpenTelemetry、Prometheus 和 Dash0 为其 Minecraft 服务器设置监控，以确保其可靠性和正常运行时间。目标是在家庭成员（最终用户）注意到之前主动解决服务器问题。

监控架构涉及三个主要组件：
1. **OpenTelemetry Java Agent：** 在 Minecraft 服务器的 JVM 中运行，它收集运行时指标，如 CPU 和内存使用情况。
2. **Minecraft Prometheus Exporter：** 抓取 Minecraft 特定的指标（玩家数量、挖掘的方块、吃掉的蛋糕）。作者探索了各种 exporter，并选择了一个用 Go 编写的，因为它易于使用。
3. **OpenTelemetry Collector：** 聚合来自 Java Agent 和 Prometheus exporter 的遥测数据，添加元数据，并将其转发到 Dash0。它还从 Systemd (journald) 收集日志。

本文重点介绍了 OpenTelemetry agent（推送指标）和 Prometheus exporter（需要拉取）之间的区别。 Collector 可以处理这两种情况。

Alerting 在 Dash0 中使用 PromQL 实现，以检测服务器停机、重启和崩溃。由于日志的信息丰富性高于简单的“up”指标，作者使用日志进行 alerting。具体而言，本文详细介绍了如何监控 systemd 日志，以检测启动或重启 minecraft 服务器进程中的问题。

作者总结说，这个项目令人愉快，提供了一个利用 Java 和 Linux 系统管理员技能的借口。 优先考虑的是服务器正常运行时间，而不是复杂的仪表板，因此重点放在有效的 alerting 上。

---

## 64. 展示HN：受《魔兽世界》启发的MMORPG原型

**原文标题**: Show HN: MMORPG prototype inspired by World of Warcraft

**原文链接**: [https://github.com/nickyvanurk/everwilds](https://github.com/nickyvanurk/everwilds)

Everwilds 是一个MMORPG原型项目，灵感来源于《魔兽世界》，旨在为开发者提供学习资源。它演示了实时在线RPG背后的网络和网络代码架构，重点关注同步和客户端-服务器交互。虽然不是一个完整的游戏，但它包含了角色移动、基本战斗、等级系统和聊天系统等功能。一个关键特性是它实现了玩家移动同步，模仿了《魔兽世界》所使用的技术，以最小的带宽实现平滑的复制。该项目使用Three.js、TypeScript和HTML/CSS构建。创建者旨在分享从研究和实现该系统中所获得的见解。提供了使用Git、NPM在本地运行该项目的说明，以及在Windows上手动复制资源的操作。

---

## 65. Show HN: 在浏览器上进行方言互译并分享SQL查询

**原文标题**: Show HN: Translate between dialects and share SQL queries on the browser

**原文链接**: [https://sqlscope.netlify.app](https://sqlscope.netlify.app)

此“Show HN”帖子介绍了一个名为SQL Scope的Web应用程序，旨在允许用户在不同SQL方言之间转换查询并分享它们。描述非常简短，表明其核心功能围绕SQL方言转换和查询共享，直接在用户的Web浏览器中进行。“你需要启用JavaScript才能运行此应用程序”的消息表明该应用程序高度依赖客户端JavaScript进行操作，这意味着处理和转换可能在浏览器中发生，而不是服务器端进程。

---

## 66. “人人可替代”：老板们谈论员工的新方式

**原文标题**: 'Everybody's Replaceable': The New Ways Bosses Talk About Workers

**原文链接**: [https://www.wsj.com/lifestyle/workplace/corporate-bosses-workers-culture-changing-cbd19c2c](https://www.wsj.com/lifestyle/workplace/corporate-bosses-workers-culture-changing-cbd19c2c)

无法访问文章链接。

---

## 67. 墨与算法：钢笔绘图的技巧、工具与工艺

**原文标题**: Ink and Algorithms: Techniques, tools and the craft of pen plotting

**原文链接**: [https://penplotter.art/](https://penplotter.art/)

墨水与算法：每周探索笔式绘图，涵盖其技术、工具及推动该媒介发展的艺术家。内容重点介绍笔式绘图仪从 20 世纪 50 年代的技术工具到如今几乎完全用于艺术创作的历程。

精选文章涵盖一系列主题，包括“绘图仪明信片交流”(#PTPX)，这是绘图仪艺术界一项成功的活动。另一篇文章深入探讨了笔式绘图演变成一种艺术形式的过程，追溯了它从实用工具到创意出口的转变。该系列还探索了特定的艺术技巧，例如 Truchet 瓷砖图案，展示了利用该图案创作独特而复杂绘图的艺术家。

该系列还包含艺术家简介，例如 James Nolan Gandy 的简介，重点介绍了他的模拟绘图机器以及他使用笔、滑轮和纸张进行笔式绘图的独特方法。“档案”部分提供了先前文章的便捷摘要，使读者可以轻松回顾过去的主题和艺术家简介。

---

## 68. 你见过薪水飞走吗？

**原文标题**: Have you ever seen an emolument fly?

**原文链接**: [https://reason.com/volokh/2025/05/11/have-you-ever-seen-an-emolument-fly/](https://reason.com/volokh/2025/05/11/have-you-ever-seen-an-emolument-fly/)

卡塔尔王室拟赠送美国一架豪华波音747-8巨型喷气式飞机，供特朗普总统在卸任前用作空军一号，之后所有权将转移至特朗普总统图书馆基金会，飞机估价4亿美元。此举引发争议，涉及宪法薪酬条款、反贿赂法以及潜在安全风险。据报道，白宫和司法部律师认定该礼物在法律上是允许的，理由是该飞机是赠送给美国空军和总统图书馆基金会，而非直接赠予个人，且未附加任何具体官方行为的条件，因此不构成受贿。

文章还重点介绍了特朗普家族集团在卡塔尔达成的一项新的高尔夫度假村协议。该协议涉及由沙特阿拉伯公司建造的豪华别墅和一个18洞高尔夫球场，标志着特朗普集团自特朗普上任以来达成的第一笔外国交易，与其此前避免外国交易以防止利益冲突的承诺形成对比。 这笔交易进一步引发了人们对潜在利益冲突以及外国实体对特朗普第二任政府时期美国政策的影响的质疑。

---

## 69. 用 Emacs 替代 tmux 和 GNU screen

**原文标题**: Replacing tmux and GNU screen with Emacs

**原文链接**: [https://www.masteringemacs.org/article/replacing-tmux-gnu-screen-emacs](https://www.masteringemacs.org/article/replacing-tmux-gnu-screen-emacs)

本文论证了Emacs可以有效地替代像tmux和GNU screen这样的终端复用器，特别是对于已经熟悉Emacs的用户。文章承认tmux在远程服务器以及Emacs不可用的情况下具有实用性，但作者强调了Emacs处理分离/重新连接会话、窗口管理、终端模拟和运行shell的能力。

作者首先阐述了在终端中运行Emacs的弊端，包括按键冲突、功能受限、缺乏保真度（图像/PDF支持）和流量控制问题。他们强调了Emacs的客户端-服务器架构，允许用户在持久服务器实例中运行程序，并通过`emacsclient`访问它们。

文章随后探讨了在Emacs中运行程序的各种方法，包括`M-x shell`、`M-x term`、`M-x vterm`、`M-x eat`和`M-x eshell`，推荐使用`vterm`以获得接近终端的体验，并推荐使用`M-x shell`以获得更以Emacs为中心的方法。作者还建议利用Emacs的编译和脚本编写功能，而不是仅仅依赖于shell。文章提供了一个 bash 脚本 `emux.sh`，用于从环境外部在 Emacs 中启动程序。

最后，文章将Emacs的窗口系统与tmux和screen的窗口系统进行了比较，阐明了术语（frame, window, buffer, pane, session），并强调了Emacs的高级窗口管理能力。文中列出了一个表格，比较了常见的tmux/screen快捷键及其Emacs等效键，强调虽然Emacs不能直接替代tmux/screen，但它可以满足大多数的复用需求。

---

## 70. Show HN: Vom决策平台（决策分析师的Cursor）

**原文标题**: Show HN: Vom Decision Platform (Cursor for Decision Analyst)

**原文链接**: [https://www.vomdecision.com](https://www.vomdecision.com)

Vom：一个无需代码的决策平台，旨在帮助企业自动化并改进信贷、保险核保等领域的决策流程。它提供诸如基于Excel公式的决策流程编辑器、REST API集成、用于策略改进的AI副驾驶、数据提供商和服务连接器以及简易的A/B测试功能。

主要优势包括用于审计和安全性的版本控制系统、用于快速决策执行的可扩展云基础设施以及全面的决策历史记录。Vom致力于通过便捷的数据访问、无需代码的策略创建和简单的A/B测试，赋能用户持续改进其自动化决策。

该平台的创始团队拥有跨行业经验，创建Vom旨在解决自动化决策所面临的挑战。他们的愿景是帮助企业有效利用数据、自动化、人工智能/机器学习，并驾驭监管。他们在技术中强调用户友好性、性能和安全性，使其适用于各种规模的企业。用户可以通过预约演示或请求联系来与Vom取得联系，以讨论该平台如何帮助他们。

---

## 71. 冈萨洛·格雷罗

**原文标题**: Gonzalo Guerrero

**原文链接**: [https://en.wikipedia.org/wiki/Gonzalo_Guerrero](https://en.wikipedia.org/wiki/Gonzalo_Guerrero)

冈萨洛·格雷罗是一位西班牙水手，1511年在尤卡坦半岛附近遭遇海难，被当地玛雅人奴役。他融入玛雅社会，成为切图马尔领主手下备受尊敬的战士("nakom")，皈依玛雅多神教，并娶了总督的女儿萨齐尔·哈为妻。他们的孩子是美洲最早的混血儿之一。

1519年，埃尔南·科尔特斯登陆科苏梅尔时，得知了格雷罗和他幸存的船员赫罗尼莫·德·阿吉拉尔，并邀请他们加入他的探险队。阿吉拉尔接受了邀请，成为一名翻译，但格雷罗拒绝了，理由是他有家庭和对玛雅总督的义务。他曾对阿吉拉尔说，他不能回到西班牙，因为他身上有纹身和穿孔，而且被玛雅人视为领主。

格雷罗在抵抗西班牙征服中发挥了关键作用，他为玛雅军队提供建议，并领导他们对抗埃尔南德斯·德·科尔多瓦、胡安·德·格里哈尔瓦、弗朗西斯科·德·蒙特霍、阿隆索·德·阿维拉和佩德罗·德·阿尔瓦拉多的西班牙入侵。他被认为是帮助挫败蒙特霍1527-1528年战役的关键人物。格雷罗于1536年在洪都拉斯苏拉山谷对抗阿尔瓦拉多军队的战斗中阵亡，可能死于火绳枪射击。

在墨西哥文化中，格雷罗被视为西班牙和土著文化融合的象征，是混血人民的父亲。虽然没有来自格雷罗的第一手资料，但他的故事在无数的历史编年史、文学作品和流行文化中被重述和重新诠释，巩固了他作为西班牙征服美洲历史上一个复杂而关键人物的遗产。

---

## 72. 内存铁电差分器

**原文标题**: In-Memory Ferroelectric Differentiator

**原文链接**: [https://www.nature.com/articles/s41467-025-58359-4](https://www.nature.com/articles/s41467-025-58359-4)

本文介绍了一种利用铁电材料的动态畴反转实现高效差分计算的内存微分器，旨在解决边缘计算处理大型数据集时面临的能效和速度挑战。该微分器的核心是一个由铁电 P(VDF-TrFE) 电容器组成的 40x40 无源交叉阵列。

该器件利用铁电材料的非线性畴动力学，特别是窄开关窗口，以最大限度地减少无源交叉阵列中普遍存在的潜行路径问题，从而实现整个阵列中可靠且均匀的畴切换。这种架构使设备能够在存储单元内部直接执行差分计算，与传统的基于MCU的方法相比，显著减少了数据传输和能量消耗。

本文展示了该微分器在解决导数函数和视觉处理任务（如移动物体提取和图像差异识别）方面的能力。通过将视频像素转换为施加到电容器阵列的电压信号，连续帧之间的变化会触发畴切换，从而揭示运动信息。每次差分计算的估计能耗非常低（0.24 fJ），并且有进一步提高速度的潜力。该器件还表现出超过五天的保持能力，使其适用于慢动态场景。

---

## 73. 从UART启动RP2350

**原文标题**: Booting the RP2350 from UART

**原文链接**: [https://pfister.dev/blog/2025/rp2350-uart-bl.html](https://pfister.dev/blog/2025/rp2350-uart-bl.html)

托马斯·普菲斯特探讨了通过Raspberry Pi RP2350微控制器的UART引导加载程序进行启动的方法，这是一种替代更常见的USB方式的选择。他的目标是将多个RP2350用作端口扩展器，并且更喜欢UART的简洁性，而不是管理复杂的固件版本。

文章详细介绍了该过程：用魔术模式解锁引导加载程序，以32字节的块发送固件，然后运行它。虽然固件需要驻留在SRAM中，但RP2350充足的520 KiB应该足以满足预期用途。

普菲斯特概述了启用UART启动所需的硬件修改：将CSn拉低，将SD1拉高。他提供了代码示例，用于编译从SRAM运行的二进制文件，并将其嵌入到另一个微控制器的固件中。文章展示了一个用于传输固件的Python脚本，然后他将代码移植到C语言。

他通过计算理论传输速率并承认其Python实现中的差异，解决了UART的速度限制问题。最后，他通过使用TI的THVD1450收发器和标准以太网电缆实施RS-485，解决了UART在长电缆上的鲁棒性问题，从而能够在10米连接上实现可靠启动，并且可能更远。他还强调并提供了解决SDK关于GPIO Bank与引导加载程序一起使用的限制的方法。

---

## 74. 华硕预装驱动软件中的一键RCE漏洞

**原文标题**: One-Click RCE in Asus's Preinstalled Driver Software

**原文链接**: [https://mrbruh.com/asusdriverhub/](https://mrbruh.com/asusdriverhub/)

本文详细介绍了一个在华硕预装的 DriverHub 软件中发现的一键远程代码执行 (RCE) 漏洞。作者发现 DriverHub 旨在通过与 `driverhub.asus.com` 通信的后台进程管理驱动程序，但其远程过程调用 (RPC) 机制安全性不足。虽然 RPC 最初似乎只接受来自 `driverhub.asus.com` 的请求，但作者发现它容易受到子域名通配符匹配的攻击（例如，`driverhub.asus.com.mrbruh.com`），从而允许恶意网站向本地 DriverHub 进程发送命令。

可利用的 RPC 端点包括获取设备信息、重启系统、下载日志，以及至关重要的更新应用程序 (`UpdateApp`)。虽然 `UpdateApp` 需要签名可执行文件，但作者通过利用华硕的 WiFi 驱动程序安装包，特别是 `AsusSetup.exe` 文件，读取来自 `AsusSetup.ini` 的安装参数，从而利用了这一点。通过提供一个包含自定义 `SilentInstallRun` 参数（指向 `calc.exe`）的恶意 `AsusSetup.ini` 文件，作者可以在 DriverHub 下载并执行经过合法签名的 `AsusSetup.exe` 时触发任意代码的执行。这允许网站通过一键执行具有管理员权限的任意代码。

作者向华硕报告了该漏洞，华硕迅速对其进行了修补。分配了 CVE。作者的跟踪工作表明，该漏洞在他们发现之前没有被积极利用。尽管没有收到漏洞赏金，但作者在华硕的“名人堂”中得到了认可。作者还讽刺地指出，促使此次调查的 WiFi 驱动程序仍然无法工作。

---

## 75. 无点域名

**原文标题**: Dotless Domains

**原文链接**: [https://lab.avl.la/dotless/](https://lab.avl.la/dotless/)

本文探讨了“无点域名”，这指的是可以直接通过网络浏览器（例如，`http://com/`）或电子邮件服务器（例如，`contact@gov`）访问的顶级域名（TLD），如`.com`或`.gov`。ICANN和IAB通常反对这种做法，特别是对于通用顶级域名（gTLD），但国家代码顶级域名（ccTLD）通常在其自身的国家管辖下运作。

本文详细介绍了无点域名的技术要求，指出它们需要在域名的根部（apex）设置A/AAAA记录以实现Web访问，以及MX记录以实现电子邮件功能。文章强调了这与标准电子邮件协议（SMTP）的冲突，后者通常至少需要两个标签（例如，`domain.tld`）。

文章提供了截至2025年3月31日更新的，表现出无点行为的ccTLD的综合列表。这些列表被分类为：

*   **当前A/AAAA：** 具有活跃的A或AAAA记录，使其可以进行Web访问的ccTLD。例如`.bd`（孟加拉国）和`.uz`（乌兹别克斯坦）。
*   **历史A/AAAA：** 以前具有A/AAAA记录但现在不再具有的ccTLD。
*   **当前仅MX：** 仅具有MX记录，理论上能够接收电子邮件的ccTLD。例如`.cf`（中非共和国）和`.gt`（危地马拉）。
*   **历史仅MX：** 以前仅具有MX记录的ccTLD。

文章简要讨论了ICANN要求新顶级域名在有限的时间内具有信息性的根记录，以防止命名冲突。最后，它探讨了“无点之点”的理论可能性，认为根域名（用`.`表示）在技术上可以具有DNS记录，尽管这极不可能。

---

## 76. 迁移到 Codeberg

**原文标题**: Migrating to Codeberg

**原文链接**: [https://guix.gnu.org/blog/2025/migrating-to-codeberg/](https://guix.gnu.org/blog/2025/migrating-to-codeberg/)

Guix项目将在下个月内将其代码仓库、缺陷跟踪和补丁跟踪迁移到 Codeberg，这项决定是通过集体共识构建过程达成的。此举在第二份 Guix 共识文档 (GCD) 中有所概述，旨在改进维护 Guix 庞大软件包集合的工具和服务。

主要里程碑包括在 6 月 7 日之前将 Git 代码仓库迁移到 Codeberg，其中 Guix 代码仓库本身将于 5 月 25 日迁移。旧的 Savannah URL 至少在 2026 年 5 月 25 日之前仍将作为镜像存在。Bug 报告和补丁将继续通过电子邮件接受，直至 2025 年 12 月 31 日，同时还将使用 Codeberg 的 issue 和 pull request 系统。

对于用户而言，主要变化包括更新 channel.scm 配置文件以指向 Codeberg URL，尽管 `guix pull` 将提供指导，并且旧 URL 将保持镜像。即使在 Savannah 最终因 Software Heritage 而消失后，`guix describe` 和时间机器部署也将继续运行。

对于贡献者而言，迁移引入了通过 Codeberg 使用 pull request 的选项，这对某些人来说是一个受欢迎的改变，但可能会对那些习惯于基于电子邮件的工作流程的人产生干扰。正在努力开发用于 Codeberg 交互的命令行和 Emacs 界面。对于需要 Codeberg 帐户的担忧已得到承认，并希望未来能够提供联邦支持。仍然会接受通过电子邮件提交到 guix-devel 的偶尔贡献。

此举旨在提高项目管理其规模的能力（100 多名贡献者，每月 2,000 多次提交，33,000 多个软件包）。

---

## 77. 为什么不使用对象能力语言？

**原文标题**: Why not object capability languages?

**原文链接**: [https://blog.plan99.net/why-not-capability-languages-a8e6cbdf9682](https://blog.plan99.net/why-not-capability-languages-a8e6cbdf9682)

Mike Hearn的文章探讨了采用对象能力语言来缓解软件供应链攻击所面临的挑战。他认为，尽管能力（如句柄和令牌）已经被使用，但在程序中应用它们却很困难。

核心问题包括定义合适的威胁模型（资源耗尽、DoS、Spectre攻击），防止组件之间的内存篡改，以及平衡安全性和可用性。他以Java和Chrome的Mojo为例。Java的Joe-E语言子集展示了实现纯粹能力编程所需的根本性改变，包括移除反射、授予环境权限的全局方法、原生方法和可变全局状态。

文章强调了“上帝对象”问题，即主方法需要访问所有环境权限，导致复杂的代理对象和向后不兼容的API变更。Java安全管理器试图通过堆栈遍历和权限交集来解决这个问题，但最终因性能成本、漏洞利用和缺乏开发者采用而被放弃。

Spectre攻击允许代码读取整个地址空间，进一步使问题复杂化，导致一些人认为只有硬件强制执行的地址空间才足够。Chrome的Mojo提供了一种硬件隔离方法，通过不可伪造的管道进行进程间通信，有效地在微服务之间实现对象能力。然而，它需要针对沙盒的操作系统特定反向工程，不易重用，主要作为RPC系统运行，并且具有很高的上下文切换成本。

本质上，这篇文章描绘了一个现实的画面，即在实践中使基于能力的系统真正可用所涉及的陡峭坡度，突出了可用性和性能问题。

---

## 78. 如何在 Lean 中（真正地）证明它——数学与计算的新前沿

**原文标题**: How to (actually) prove it – New Frontiers of Mathematics and Computing in Lean

**原文链接**: [https://kirancodes.me/posts/log-how-to-prove-it-maths.html](https://kirancodes.me/posts/log-how-to-prove-it-maths.html)

本文重点介绍了使用 Lean 定理证明器的“机械化数学”这一令人兴奋的新领域，它为数学家实际开发证明的方式提供了前所未有的洞察力。其关键创新是“Lean 蓝图”工具，由数学家设计，用于规划形式化，可视化定义、引理和定理之间的依赖关系，并跟踪其进展。

作者强调，这些蓝图与版本控制系统相结合，提供了一个独特的机会来观察数学家如何解决问题、推测引理以及将复杂的证明分解为可管理的步骤。文章展示了各种活跃的 Lean 项目的蓝图演变动画可视化，包括 Polynomial Freiman Ruzsa 猜想、Kelley-Meka 界、Carleson 定理等的形式化。

这些可视化揭示了不同的发展模式，例如定理的“寒武纪”爆发、零星的进展或知识的逐步积累。作者认为，这些可视化为理解数学推理提供了一个丰富的数据集，并有可能训练机器学习模型来协助数学家。此外，像 Equational Theories 形式化这样的项目旨在在 Lean 中开发新的数学，让我们得以一窥人机协作数学的未来。作者最后鼓励读者探索可用的数据并为这个不断发展的领域做出贡献。

---

## 79. 离开谷歌

**原文标题**: Leaving Google

**原文链接**: [https://www.airs.com/blog/archives/670](https://www.airs.com/blog/archives/670)

Go语言关键贡献者 Ian Lance Taylor 宣布离开 Google，结束 19 年任期。Taylor 于 2008 年加入 Go 团队，在 Go 语言的开发和推广中发挥了重要作用。

他回顾了 Go 语言出乎意料的成功，超越了最初仅影响其他语言的期望，并强调了他的贡献，包括为 GCC 创建 Go 前端，以及为 Google 的构建系统和 SWIG 添加 Go 支持。他还曾管理团队一段时间，并帮助开发和实施了泛型。

Taylor 指出，他的方法侧重于解决当前和近期的难题，这被证明是有价值的，但可能阻碍了对更具创新性和前瞻性想法的追求。他认为 Google 和 Go 内部的变化，以及不断发展的编程格局，导致了他的离开，他感到自己不再适合。

尽管离开 Google，Taylor 仍然对 Go 感兴趣，并认为该语言需要不断发展，尤其是其标准库。他计划休息一段时间，但希望将来能再次为 Go 做出贡献。

该帖子包含其他人对 Taylor 的工作和他在 Go 社区的贡献表示感谢的评论。一位评论者 cuishuang 表示，Taylor 的离开对该语言和社区来说是不可估量的损失。

---

## 80. Jax中的SDFs和快速扫描算法

**原文标题**: SDFs and the Fast sweeping algorithm in Jax

**原文链接**: [https://rohangautam.github.io/blog/fast_sweeping/fastsweeping/](https://rohangautam.github.io/blog/fast_sweeping/fastsweeping/)

本文探讨了快速扫描法(FSM)作为在JAX中求解Eikonal方程的一种方法，尤其适用于涉及符号距离函数(SDFs)的应用。Eikonal方程模拟波前传播，其解可用于各种问题，包括最短路径、医学成像以及为机器学习中的隐式表面表示创建SDF。

文章对比了拉格朗日前沿演化和欧拉水平集方法，强调后者如何使用函数的零水平集在固定网格上隐式地跟踪界面。传统的数值方法难以处理Eikonal方程中可能出现的奇点和冲击波，这促使人们使用像FSM这样手工设计的算法。

相比于快速行进法(FMM)的O(n log n)时间复杂度，FSM提供了一种更快的O(n)解决方案。该算法通过在不同方向上扫描网格来工作，近似每个方向上的到达时间并将它们组合起来。空间导数使用Godunov迎风差分格式进行近似。

作者提供了FSM算法的NumPy和JAX实现，强调了通过JAX的即时编译所获得的效率提升。基准测试表明，JAX代码的性能优于NumPy，尽管专用的C++库(skfmm)速度甚至更快。文章最后讨论了使用JAX并行化FSM算法的尝试，但由于跟踪限制而面临挑战。

---

## 81. 能侵染医院的微生物能分解医用塑料，尚属首次

**原文标题**: Microbe that infests hospitals can digest medical-grade plastic ― a first

**原文链接**: [https://www.nature.com/articles/d41586-025-01412-5](https://www.nature.com/articles/d41586-025-01412-5)

一种常见于医院且已知会导致感染的细菌铜绿假单胞菌，被发现可以分解医用级塑料，特别是聚己内酯（PCL）。英国的研究人员在该菌株中发现了一种酶，Pap1，使之能够降解PCL，一种常用于医疗保健的可生物降解塑料。这非常重要，因为之前，降解塑料的酶只在环境细菌中发现，而不是在医院病原体中。

这一发现引起了人们的担忧，因为如果铜绿假单胞菌能够降解塑料，它可能会损害含有塑料的医疗设备（如缝线和植入物）的完整性，从而对患者的治疗结果产生负面影响。研究人员通过将该基因插入大肠杆菌，使其分解PCL，以及从铜绿假单胞菌中删除该基因，使其丧失降解塑料的能力，从而证实了Pap1的作用。

此外，该研究发现该酶会增加生物膜的形成，可能导致抗生素耐药性的增加。用大蜡螟幼虫进行的实验表明，当存在PCL植入物时，该细菌的危害更大，突显了这种塑料降解能力在生物环境中的潜在后果。

---

## 82. Klarna转变AI策略，重新启用人工客服

**原文标题**: Klarna changes its AI tune and again recruits humans for customer service

**原文链接**: [https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/](https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/)

Klarna 扭转策略：重新引入人工客服，不再过度依赖 AI

---

## 83. Show HN: GlassFlow – 从 Kafka 到 ClickHouse 的 OSS 流式去重和连接

**原文标题**: Show HN: GlassFlow – OSS streaming dedup and joins from Kafka to ClickHouse

**原文链接**: [https://github.com/glassflow/clickhouse-etl](https://github.com/glassflow/clickhouse-etl)

GlassFlow：一款开源实时流处理器，旨在简化 Kafka 和 ClickHouse 之间的数据管道创建和管理。它面向数据工程师，提供内置的去重和时间连接功能，以处理延迟到达的事件并确保数据正确性。

主要功能包括：

*   **流式去重：** 具有可配置时间窗口（最长 7 天）的实时去重，防止 ClickHouse 中出现重复数据。
*   **时态流连接：** 实时连接两个 Kafka 流，同样具有可配置时间窗口（最长 7 天），简化了 ClickHouse 连接数据流的创建。
*   **内置 Kafka 连接器：** 由 NATS-Kafka Bridge 驱动，自动从 Kafka 主题提取数据，并支持多个分区和 JSON 数据。
*   **优化的 ClickHouse Sink：** 原生连接、可配置的批处理大小和重试机制确保将数据高效摄取到 ClickHouse 中，包括 JSON 数据。
*   **用户友好的 Web UI：** 方便管道配置、管理和监控。

GlassFlow 提供了一个使用 Docker Compose 的快速入门指南、一个本地开发设置，以及一个包含 Kafka、ClickHouse、示例数据和示例管道的综合演示环境。 该架构涉及 GlassFlow API（用 Go 编写）、Web UI、用于内部通信的 NATS 和 Kafka Bridge。 管道配置在 JSON 中定义，指定源（Kafka）、Sink（ClickHouse）和可选的连接参数。 该项目在 Apache License 2.0 许可下发布，并欢迎贡献。

---

## 84. Lazarus 4.0 发布

**原文标题**: Lazarus Release 4.0

**原文链接**: [https://forum.lazarus.freepascal.org/index.php?topic=71050.0](https://forum.lazarus.freepascal.org/index.php?topic=71050.0)

这是Lazarus 4.0版本发布的论坛公告。该论坛致力于Lazarus IDE和Free Pascal编译器，包含Lazarus和Free Pascal网站、下载、文档、Bug追踪器、邮件列表和项目信息等各种资源链接。论坛还展示了近期发布的帖子列表，涵盖与Lazarus开发相关的各种主题，包括移植、启动选项、可视化组件、Free Pascal问题、求助请求和通用编程问题。它显示帖子标题和作者，以及上次发帖的时间。论坛导航包含上一页和下一页的链接，允许用户浏览讨论内容。页面底部提供了关于论坛软件（SMF）和TinyPortal插件的信息。

---

## 85. 美国版权局：生成式人工智能训练 [pdf]

**原文标题**: US Copyright Office: Generative AI Training [pdf]

**原文链接**: [https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf)

这份文件标题显示为美国版权局关于生成式AI训练的文件。然而，其内容为编码数据，可能是PDF的二进制信息，目前无法读取。因此，无法从提供的文本中提取关于版权局对生成式AI训练的立场、指南或讨论的具体信息。为了提供准确的摘要，需要提取并解读PDF的实际文本内容。

---

## 86. Ruby on Rails 的 Solid Queue 简介

**原文标题**: An Introduction to Solid Queue for Ruby on Rails

**原文链接**: [https://blog.appsignal.com/2025/05/07/an-introduction-to-solid-queue-for-ruby-on-rails.html](https://blog.appsignal.com/2025/05/07/an-introduction-to-solid-queue-for-ruby-on-rails.html)

本文介绍了 Rails 8 中新的后台任务处理库 Solid Queue，强调了其仅依赖数据库的独特功能，无需 Redis 或其他外部依赖项。这符合 Rails 降低新应用程序运营开销的目标。

文章解释了核心组件：任务（代表任务的 ActiveRecord 模型）和工作进程（执行任务的进程）。任务和工作进程之间的通信通过数据库进行，使用多个表来管理任务状态（例如，`solid_queue_jobs`、`solid_queue_ready_executions`、`solid_queue_claimed_executions`）。

文章详细介绍了任务的生命周期，从入队（在 `jobs` 和 `ready_executions` 表中创建记录）到工作进程声明（在 `claimed_executions` 中创建记录）以及最终执行。

通过巧妙的数据库设计实现了性能，特别是使用 `solid_queue_ready_executions` 表进行快速轮询，并使用 `FOR UPDATE SKIP LOCKED` 来防止工作进程在轮询期间阻塞。SQLite 不支持 `SKIP LOCKED`，因此存在需要考虑的限制。

文章强调了任务安全性，解释了 `solid_queue_claimed_executions` 和 `solid_queue_processes` 表，以及一个监督进程如何防止任务在工作进程崩溃时丢失。监督进程监视工作进程的心跳，并重新排队由不活动工作进程声明的任务。

文章最后提到了一些其他功能，例如调度重复性和顺序性任务，并承诺在下一部分中进行更深入的探讨。

---

## 87. JEP 515：提前编译方法分析

**原文标题**: JEP 515: Ahead-of-Time Method Profiling

**原文链接**: [https://openjdk.org/jeps/515](https://openjdk.org/jeps/515)

JEP 515 提议“提前编译方法分析”，通过利用在训练运行期间收集的方法执行配置文件来改善 Java 应用程序的启动和预热时间。目前，JVM 在应用程序执行的初始阶段收集配置文件，导致预热期间性能下降。此 JEP 旨在将配置文件收集转移到单独的训练运行中，并将配置文件存储在 JEP 483 引入的现有 AOT（提前编译）缓存中。

通过在启动时使这些配置文件可供 JVM 使用，JIT（即时）编译器可以立即生成优化的本机代码，从而缩短预热时间。主要目标包括加速预热、无需修改代码、不引入新的执行约束以及使用现有的 AOT 缓存工作流程。

缓存的配置文件将补充，而不是取代生产运行期间的持续分析，从而使 JVM 能够适应潜在的行为变化。这种方法结合了 AOT 配置文件、在线分析和 JIT 编译的优势。测试将涉及新的单元测试和现有的 AOT 缓存测试，以确保功能和稳定性。基本假设是，训练运行提供有用的数据，可以转化为生产中的性能改进。

---

## 88. 不成功便成仁

**原文标题**: Hill or High Water

**原文链接**: [https://royalsociety.org/blog/2025/05/hill-or-high-water/](https://royalsociety.org/blog/2025/05/hill-or-high-water/)

Ainsley Vinall 的《不顾一切》（Hill or High Water）重点介绍了近期编目的、由探险队队长 Martin Holdgate 爵士捐赠的 1958-59 年英国皇家学会南智利探险队的 300 多张幻灯片。该探险队恰逢达尔文《物种起源》一百周年纪念，旨在重新评估达尔文考察过的地点，并调查新西兰、澳大利亚和南美洲共有的物种，从而促进对板块构造的新兴理解。

该团队由五位科学家组成，包括动物学家 Holdgate、植物学家 Eric Godley、海洋生物学家 George Knox、地质学家 William Watters 和昆虫学家 Guillermo Kuschel，他们探索了智利的多个地点，从圣地亚哥开始，到奇洛埃岛的 Chepu、圣佩德罗山脉、惠灵顿岛的 Puerto Edén、蓬塔阿雷纳斯，最后到达纳瓦里诺岛的 Puerto Williams。

探险队记录了当地的景观、野生动物以及 Puerto Edén 当地 Kawésqar 人的日常生活，为了解他们独特的文化提供了宝贵的见解。这些照片展示了相对未受破坏的景观，尤其是在最南端的岛屿上。回到英国后，该团队在一次会议上分享了他们的发现，并在 Proceedings B 上发表了成果，还在 1961 年举办了一次展览。编目的照片记录了 65 多年前的探险、景观和南智利人民的生活，具有重要的历史意义。

---

## 89. 观察人

**原文标题**: Observations from people-watching

**原文链接**: [https://skincontact.substack.com/p/21-observations-from-people-watching](https://skincontact.substack.com/p/21-observations-from-people-watching)

无法访问文章链接。

---

## 90. PCB应变计

**原文标题**: Strain gauge made out of PCB

**原文链接**: [https://github.com/vapetrov/PCB_strain_gauge](https://github.com/vapetrov/PCB_strain_gauge)

本文介绍了一种PCB应变计，这是一种利用电路板本身作为传感元件来测量微小挠度的传感器。它非常灵敏，能够测量微米级的挠度，满量程范围为+/- 3厘米。该项目提供了多种PCB设计，包括带有4元件和2元件传感桥的版本（可能降低热漂移），以及用于元件侧的加强筋。建议的板厚为0.6毫米，但可以根据具体应用进行调整。

该项目设计易于手工组装，无需热风或回流焊炉等专用设备。它可以与微控制器（Seeed Studio XIAO RP2040）独立使用，也可以通过排针与外部微控制器连接。该设计允许通过少量修改省略某些组件，例如外部ADC和偏置电压发生器。

提供了用于校准和连续采样的示例固件，以及用于数据可视化的Python脚本。本文强调了在高灵敏度测量之前，允许电路板达到稳定的工作温度的重要性。用户可以使用提供的Python notebook和SVG编辑工具自定义传感元件的形状，以生成自定义的KiCad封装。设计文件，包括PCB布局和示例代码，均可供下载。

---

## 91. 肯尼迪对我们食物中的化学物质是正确的

**原文标题**: Kennedy Is Right About the Chemicals in Our Food

**原文链接**: [https://www.nytimes.com/2025/05/12/opinion/kennedy-ultraprocessed-food-dyes.html](https://www.nytimes.com/2025/05/12/opinion/kennedy-ultraprocessed-food-dyes.html)

本文认为，尽管小罗伯特·F·肯尼迪曾有推广伪科学的历史，但他对美国食品供应中化学物质的担忧是合理且可能被低估的。文章强调，美国允许估计有10,000种食品添加剂，这些添加剂通常用于超加工食品。

一个关键问题是GRAS（“通常被认为是安全的”）监管途径，该途径允许公司自行证明许多化学品的安全性，而无需事先获得FDA的批准。这意味着通常是食品行业，而不是联邦监管机构，来审查成分的安全性。研究人员估计，我们食物中大约有1000种化学物质是监管机构未知的。据报道，肯尼迪正在努力堵住这个漏洞。

文章进一步批评了FDA有限的测试范围，主要侧重于癌症、基因突变和器官损伤，而忽略了调查这些化学物质对肥胖、心血管疾病和糖尿病等慢性疾病的微妙而长期的影响。 此外，对食用数百或数千种化学物质的累积效应的研究也不足。而且，与欧洲监管机构不同，FDA不会根据新的科学发现来例行地重新检查现有化学物质。 文章总结说，FDA对过时科学和原则的依赖不足以确保食品安全。

---

## 92. Visual Basic 的历史与遗产

**原文标题**: The History and Legacy of Visual Basic

**原文链接**: [https://retool.com/visual-basic](https://retool.com/visual-basic)

本文详细介绍了Visual Basic的起源，追溯至Alan Cooper在20世纪80年代末创建的shell构建工具集Tripod（后更名为Ruby）。Cooper旨在通过允许用户使用拖放式的“小工具”自定义Windows shell，从而改进其简陋的用户界面。

Cooper对Tripod的演示给比尔·盖茨留下了深刻印象，他收购了该项目供微软使用。Cooper及其团队重写了Tripod，并更名为Ruby，但由于内部政治和微软向OS/2战略的转变，最终未能包含在Windows 3.0中。

盖茨意识到可视化编程环境的潜力，将Ruby重新定位，用BASIC取代了其内部语言，从而创建了Visual Basic。最初不太情愿的商业语言组指派了一个年轻的团队（代号为“Thunder”）来开发它，并大量依赖Cooper原始团队中的Michael Geary的专业知识。

开发过程比预期的时间更长、更复杂，涉及重大的架构变更，包括用Omega的嵌入式BASIC代码编辑器和事件模型替换Ruby的事件传递系统。虽然Cooper最初的可定制shell的愿景并未以相同的方式实现，但它为Visual Basic铺平了道路，后者成为一种主导性的编程环境。

---

## 93. 在简单的层级模型和……之间，是否需要寻求某种平衡？

**原文标题**: Is there a balance to be struck between simple hierarchical models and

**原文链接**: [https://statmodeling.stat.columbia.edu/2024/05/26/is-there-a-balance-to-be-struck-between-simple-hierarchical-models-and-more-complex-hierarchical-models-that-augment-the-simple-frameworks-with-more-modeled-interactions-when-analyzing-real-data/](https://statmodeling.stat.columbia.edu/2024/05/26/is-there-a-balance-to-be-struck-between-simple-hierarchical-models-and-more-complex-hierarchical-models-that-augment-the-simple-frameworks-with-more-modeled-interactions-when-analyzing-real-data/)

无法访问文章链接。

---

## 94. 粉丝福利

**原文标题**: Fan Service

**原文链接**: [https://flak.tedunangst.com/post/fan-service](https://flak.tedunangst.com/post/fan-service)

本文详细介绍了作者为 OpenBSD 创建 ASUS ACPI WMI 驱动以控制笔记本电脑风扇速度的历程。该功能通常可以通过 ASUS 笔记本电脑上的 Fn-F5 或 Fn-F 访问，但在 OpenBSD 中无法使用。

作者解释了 ACPI 和 WMI 的基础知识，强调了它们如何允许操作系统与硬件通信并访问供应商特定的功能。OpenBSD 缺乏 WMI 驱动，这促使作者利用从 Linux 的 ASUS 笔记本电脑驱动程序中获得的见解来构建一个。

该过程涉及几个阶段：识别 GUID 和 ACPI 事件代码，使用 acpidump 和 iasl 解读 ACPI 代码，以及了解如何设置设备状态以实现键盘背光和风扇配置文件等功能。作者遇到了诸如错误的字节顺序、误解 ACPI 事件代码以及识别用于风扇控制的正确设备 ID 等挑战。

最终，通过分析 Linux 驱动程序和系统的 ACPI 代码，作者成功创建了一个驱动程序，该驱动程序允许在静音模式和超速涡轮模式之间切换风扇速度。 这会影响性能和电池续航时间。

作者将 OpenBSD 的代码组织方式与 Linux 进行了对比，OpenBSD 将相关的 C 和头文件放在一起以便于导航，而 Linux 的文件安排更结构化但不太直观。 最终的结果是一个可用的风扇控制解决方案，可改善在运行 OpenBSD 的 ASUS 笔记本电脑上的用户体验和电池性能。

---

## 95. BIOS 从D盘启动

**原文标题**: Bios Boot to D

**原文链接**: [https://theartofmachinery.com/2017/01/24/boot_to_d.html](https://theartofmachinery.com/2017/01/24/boot_to_d.html)

本文详细介绍了在PC上创建加载并执行D代码的BIOS引导加载程序的过程。首先解释了汇编语言的基础知识，特别是Intel语法。然后，作者逐步介绍了PC在启动过程中所采取的步骤，从BIOS POST到将可引导磁盘的前512个字节加载到地址0x7c00的内存中。

本文强调了在16位实模式的约束下工作的挑战，包括有限的内存访问（1MiB）和处理臭名昭著的A20栅极的必要性。引导加载程序的任务包括保存启动磁盘号，设置段寄存器，启用A20线以及从磁盘加载OS有效负载。

一个关键的挑战是在BIOS磁盘驱动程序仅在实模式下起作用时加载OS（D代码），而更大的OS有效负载需要保护模式。本文解释了一种在实模式和保护模式之间切换以分块加载OS的策略，使用始终返回到实模式的函数。

作者描述了进入32位保护模式的过程，包括设置全局描述符表（GDT）以定义内存段。最后，它涵盖了将OS块复制到高位内存以及最终执行加载的D代码。

---

## 96. 为什么Apple II不支持小写字母 (2020)

**原文标题**: Why the Apple II Didn't Support Lowercase Letters (2020)

**原文链接**: [https://www.vintagecomputing.com/index.php/archives/2833/why-the-apple-ii-didnt-support-lowercase-letters](https://www.vintagecomputing.com/index.php/archives/2833/why-the-apple-ii-didnt-support-lowercase-letters)

史蒂夫·沃兹尼亚克在 How-To Geek 上发表的文章解释了最初的 Apple II 电脑为何不支持小写字母。沃兹尼亚克透露，20世纪70年代初他有限的财政资源是主要原因。

最初，他为了访问 ARPAnet 创建了一个电视终端，使用了一个 60 美元（相当于今天的约 333 美元）的仅支持大写的键盘，这是当时最便宜的选择。 这种财务限制延续到了 Apple I 和 II 的开发中。

在构思 Apple 电脑之前，沃兹尼亚克已经用大写键盘构建了他的电视终端。 虽然他想要小写字母支持，但添加它将需要重写他的 BASIC 解释器代码，这是一项“可怕且冒险的工作”，完全是手工完成的，因为没有资金购买分时汇编器。 他与史蒂夫·乔布斯讨论了这个问题，乔布斯并没有优先考虑小写字母，最终，财务限制决定了设计。 沃兹尼亚克手工编写了 Apple II 的全部 8KB 代码，进一步巩固了仅支持大写的限制。

文章还包括读者评论，讨论了版权问题、潜在的克隆版本，以及用于在某些 Apple II 型号上启用小写字母输入的“切割走线”修改方法。 编辑本杰·爱德华兹补充说，沃兹尼亚克的足智多谋，源于必要性，最终促成了 Apple I 和 II 的诞生。

---

## 97. HTML时间标签与DRY原则 (HARC Stack)

**原文标题**: HTML Time Tags and DRY (HARC Stack)

**原文链接**: [https://rakujourney.wordpress.com/2025/05/12/harc-stack-semantic-time/](https://rakujourney.wordpress.com/2025/05/12/harc-stack-semantic-time/)

本文是关于HARC堆栈（HTMX、Raku Air、Red和Cro）系列文章的第四篇，重点介绍HTML中的`time`标签，以及Air::Base如何以DRY（不要重复自己）的方式实现它。

作者强调了语义化HTML标签的重要性，以及Air::Functional如何让开发者使用函数式代码风格来构建HTML。标准的HTML `time`标签的问题在于，它需要冗余且可能容易出错地同时输入机器可读的datetime属性和人类可读的文本。

Air::Base的`time`标签解决方案利用Raku的服务器端功能，从代码中提供的`datetime`属性自动生成人类可读的日期和时间。这消除了冗余并确保了一致性。开发者可以使用`mode`属性（`time`、`datetime`或`date`）指定格式，其中`date`为默认值。

作者强调了这种方法的好处：提高可维护性，减少错误，以及使语义化时间与程序化时间值对齐。Air::Base中的`Time`角色也是可组合的，允许在其他Raku类或角色中进行自定义和重用。文章最后总结说，这种DRY方法符合HARC堆栈的核心原则，鼓励高效可靠的Web开发，并邀请读者在GitHub上探索源代码。

---

## 98. 众包破解二维码

**原文标题**: Crowd Sourcing Broken QR Codes

**原文链接**: [https://www.humanqr.com/news/qr-code-not-scanning-well-try-to-help/](https://www.humanqr.com/news/qr-code-not-scanning-well-try-to-help/)

本文呼吁大家参与众包活动，以改进二维码修复技术。作者Daniel讲述了自己成功修复在流浪猫吊牌上发现的受损二维码的个人经历。这次经历，加上与一位名叫Greg的人讨论二维码的未知失效模式，促使作者寻求更可靠的解决方案来修复无法扫描的二维码。

目前，确定二维码失效的原因很困难。作者的目标是创建一个软件工具来自动修复二维码，使其能够再次扫描。为了实现这个目标，作者正在收集损坏或损坏的二维码数据集。

本文敦促读者通过Google表格（文章中链接）或电子邮件至daniel@humanqr.com提交无法扫描的二维码。通过提交，参与者有助于构建有价值的数据集。作者还将尝试单独修复提交的二维码，并将结果返回给提交者。最终目标是向公众发布这个经过整理的数据集，使其他人能够进一步开发二维码修复技术，并最终创建一个自动二维码修复工具。作者要求读者不要故意损坏二维码进行提交。

---

## 99. 工程师开发可穿戴的心脏病发作检测技术

**原文标题**: Engineers develop wearable heart attack detection technology

**原文链接**: [https://medicalxpress.com/news/2025-04-wearable-heart-technology.html](https://medicalxpress.com/news/2025-04-wearable-heart-technology.html)

密西西比大学工程师正在开发一种可穿戴的实时心脏病发作检测技术，有望显著改善患者的治疗效果。这项技术被设计成一种轻量级、节能芯片，利用人工智能分析心电图 (ECG)，并以 92.4% 的准确率检测心脏病发作。这可能比传统方法快两倍。

研究人员在 Kasem Khalil 助理教授的带领下，强调了心脏病发作治疗中速度的重要性，指出更快的诊断可以减少永久性损伤。该设备旨在嵌入到手表或手机等可穿戴设备中，从而实现连续的心脏监测和更快的干预，而目前的方法需要去医疗机构进行心电图或血液测试。

博士生 Tamador Mohaidat 专注于开发人工神经网络，而研究生 Md. Rahat Kader Khan 构建了软件。该团队强调其整体方法，专注于硬件和软件两方面，以实现最佳的系统性能。研究人员设想通过调整人工智能和传感器能力，将该技术的应用扩展到检测其他健康问题，如癫痫或痴呆症。该研究发表在智能系统、区块链和通信技术国际会议的论文中。

---

## 100. Linux下C/POSIX标准库实现的比较

**原文标题**: Comparison of C/POSIX standard library implementations for Linux

**原文链接**: [https://www.etalabs.net/compare_libcs.html](https://www.etalabs.net/compare_libcs.html)

本文比较了Linux上的几种C/POSIX标准库实现：musl、uClibc、dietlibc和glibc，重点关注功能丰富性和臃肿之间的权衡。该比较由与musl相关的人员撰写，涵盖了多个方面，包括臃肿、资源耗尽时的行为、性能、ABI/版本控制、算法、功能特性、目标架构、构建环境和安全性。

“臃肿比较”部分评估了库的大小和开销，指出glibc由于iconv模块而拥有最大的占用空间。本文讨论了每个库如何处理资源耗尽场景，例如线程局部存储分配失败。性能基准测试涵盖了分配、字符串操作、线程创建和I/O等任务。

ABI和版本控制考察了稳定性、兼容性和原子升级，突出了musl的原子升级能力。算法比较深入研究了子字符串搜索、正则表达式匹配和排序算法的效率。

功能特性比较突出了C99数学库支持、POSIX线程、区域设置定义以及UTF-8解码和堆栈粉碎保护等安全功能方面的差异。目标架构列出了支持的架构。还讨论了构建环境方面，例如头文件设计和工具链依赖性。结论强调了不同库在功能丰富性和开销之间的权衡。

---

