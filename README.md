# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-09.md)

*最后自动更新时间: 2025-07-09 17:51:00*
## 1. 树木借阅

**原文标题**: Tree Borrows

**原文链接**: [https://plf.inf.ethz.ch/research/pldi25-tree-borrows.html](https://plf.inf.ethz.ch/research/pldi25-tree-borrows.html)

本文介绍了 Tree Borrows，一套旨在提升 Rust 不安全代码的安全性和优化潜力的新规则。Rust 基于所有权的类型系统提供了强大的保证，但由于不安全代码的存在，需要明确定义何种不安全代码属于“行为不良”，以避免编译器优化失效。先前的尝试，如 Stacked Borrows，被证明过于严格，拒绝了真实世界 Rust 不安全代码中常见的模式，并且未能考虑到 Rust 借用检查器的最新进展。

Tree Borrows 通过将 Stacked Borrows 的基于栈的结构替换为树状结构来解决这些限制。这种改变使其能够接受更多有效的非安全代码模式，同时仍然保持安全保证。作者在 30,000 个最流行的 Rust crates 上评估了 Tree Borrows，结果表明，与 Stacked Borrows 相比，它拒绝的测试用例明显更少（减少了 54%）。

此外，作者提供了形式化的证明 (使用 Rocq)，证明 Tree Borrows 保留了 Stacked Borrows 启用的大部分优化，并引入了新的优化机会，特别是读-读重排序。这使得 Tree Borrows 成为推理和优化不安全 Rust 代码的更实用和更强大的基础。该文章的重要性在于其在 PLDI'25 上荣获杰出论文奖。文章、工件和源代码等资源已提供，以供进一步研究。

---

## 2. 为什么大型语言模型无法编写Q/Kdb+：从右向左编写代码

**原文标题**: Why LLMs Can't Write Q/Kdb+: Writing Code Right-to-Left

**原文链接**: [https://medium.com/@gabiteodoru/why-llms-cant-write-q-kdb-writing-code-right-to-left-ea6df68af443](https://medium.com/@gabiteodoru/why-llms-cant-write-q-kdb-writing-code-right-to-left-ea6df68af443)

本文探讨了大型语言模型(LLM)难以编写q/kdb+代码的原因。q/kdb+语言的特点是自右向左、无运算符优先级(RL-NOP)的求值方式。作者认为，LLM主要接受的是像Python这样自左向右语言的训练，这使得它们难以掌握和实现RL-NOP逻辑。虽然LLM知道RL-NOP规则，但它们经常产生不正确或混合(Python/q)的代码。

核心问题不仅仅是方向逆转（如在从右到左的语言中），而是token产生的时间顺序。编写q代码通常需要首先思考和编写表达式的“结尾”。

作者认为，由于市场规模小以及可能扰乱LLM在常见任务中的表现，重新训练LLM以适应RL-NOP语言不太可能。相反，他们提出了一种名为“Qython”的实用解决方案：一种编译成q的类Python语言。

关键思想是利用LLM对Python的熟练程度，提供一种可以清晰地翻译成q的语法。翻译器处理优先级和求值顺序的转换，允许LLM使用熟悉的Python约定编写代码。本文展示了一个使用更新的、支持Qython的q-MCP服务器的概念验证，其中Claude成功地用Qython编写了一个牛顿法平方根函数，然后将其翻译成q。作者承认也需要一个q→Qython翻译器，并概述了创建它所涉及的挑战。

---

## 3. Ruby 3.4 冻结字符串字面量：Rails 开发者需要了解的内容

**原文标题**: Ruby 3.4 frozen string literals: What Rails developers need to know

**原文链接**: [https://www.prateekcodes.dev/ruby-34-frozen-string-literals-rails-upgrade-guide/](https://www.prateekcodes.dev/ruby-34-frozen-string-literals-rails-upgrade-guide/)

Prateek Codes 的这篇文章解释了 Ruby 中即将到来的默认冻结字符串字面量的过渡，从 Ruby 3.4 开始。 最重要的结论是**现有的 Rails 应用程序在 Ruby 3.4 中将继续像以前一样工作**。 Ruby 3.4 引入了*选择启用*警告，以帮助开发者为未来冻结字符串字面量成为默认设置做好准备。

该过渡计划在三个版本中完成：Ruby 3.4（选择启用警告），Ruby 3.7（默认启用警告），以及 Ruby 4.0（默认冻结字符串）。 冻结字符串提供了性能优势，例如减少垃圾回收和通过字符串去重节省内存。

文章强调，最初的最大影响可能在于 gem 依赖项。它引入了“冷冻字符串”作为一种机制，允许发出警告，同时保持兼容性。

作者提供了在 Rails 应用程序中查找和修复问题的实用步骤：在开发和测试环境中启用警告，使用调试模式，以及解决常见的模式，例如字符串构建和就地修改。

解决方案包括使用 `+ "string"` 创建字符串的可变副本，并避免使用 `gsub!` 等方法进行就地修改。

文章建议将新代码中的字符串视为不可变的，并逐步修复现有代码中的警告。它提供了 CI/CD 集成的指导，以跟踪新的警告，并强调升级到 Ruby 3.4 是安全的，并提供对开发者友好的过渡。

---

## 4. 快速3D碰撞检测算法

**原文标题**: A fast 3D collision detection algorithm

**原文链接**: [https://cairno.substack.com/p/improvements-to-the-separating-axis](https://cairno.substack.com/p/improvements-to-the-separating-axis)

无法访问文章链接。

---

## 5. 文档机器人是文档，还是不是？

**原文标题**: Is the doc bot docs, or not?

**原文链接**: [https://www.robinsloan.com/lab/what-are-we-even-doing-here/](https://www.robinsloan.com/lab/what-are-we-even-doing-here/)

作者质疑Shopify的LLM驱动的开发者文档机器人的可靠性和价值。他们遇到了一个问题，机器人提供了错误的Liquid语法来检测订单确认邮件中的Shopify Collective商品。建议的代码依赖于邮件生成时不可用的订单标签，导致了令人沮丧的测试和退款流程。

作者认为，一个猜测性的文档机器人破坏了准确文档的目的，尤其是在错误的建议导致时间和精力浪费的情况下。虽然承认该机器人在基本搜索查询方面的用处，但他们认为在更复杂的情况下，错误信息的可能性超过了其益处。他们强调官方文档应优先考虑准确性而非速度。

作者最终通过检查订单明细中的产品级标签找到了解决方案，这被证明是一个可靠的替代方法。他们最后质疑一个并非始终准确的“官方”文档机器人的作用，并认为它减损了那些创建详尽文档的人的努力。

---

## 6. 考古学家在秘鲁发现一座3500年历史的古城

**原文标题**: Archaeologists unveil 3,500-year-old city in Peru

**原文链接**: [https://www.bbc.co.uk/news/articles/c07dmx38kyeo](https://www.bbc.co.uk/news/articles/c07dmx38kyeo)

考古学家在秘鲁巴兰卡省发掘出一座有3500年历史的城市佩尼科，揭示了卡拉尔文明遗产的重要信息。佩尼科位于利马以北200公里处，海拔600米，据信曾是连接沿海社区与安第斯山脉和亚马逊地区的 vital 重要贸易枢纽。

由挖掘过卡拉尔遗址的 Ruth Shady 博士领导的此次发现，揭示了卡拉尔文明在因气候变化而衰落后的命运。佩尼科的战略位置促进了各个地区之间的贸易和交流。该遗址的挖掘工作可追溯到公元前 1800 年至公元前 1500 年，已发现了 18 座建筑物，包括祭祀神庙和住宅区。无人机拍摄的画面显示，城市中心有一个圆形建筑，周围环绕着石头和泥土建筑。研究人员还发现了祭祀用品、粘土雕塑和贝壳项链。

考古学家 Marco Machacuay 强调佩尼科是卡拉尔社会的延续，具有重要意义。此次发现为秘鲁丰富的考古遗产增添了新内容，与马丘比丘和纳斯卡线等遗址齐名。

---

## 7. 大多数RESTful API实际上并不是RESTful的

**原文标题**: Most RESTful APIs aren't really RESTful

**原文链接**: [https://florian-kraemer.net//software-architecture/2025/07/07/Most-RESTful-APIs-are-not-really-RESTful.html](https://florian-kraemer.net//software-architecture/2025/07/07/Most-RESTful-APIs-are-not-really-RESTful.html)

本文挑战了对“RESTful” API的普遍理解，认为许多实现偏离了Roy Fielding对REST的最初构想。Fielding的论文强调REST是一种以可扩展性、简洁性和适应性为重点的架构风格，并将Web作为模型。他批评CRUD风格的API过于简化REST，尤其忽略了超媒体作为应用程序状态引擎（HATEOAS）。HATEOAS涉及在服务器响应中嵌入超媒体链接来指导客户端操作，将客户端与服务器的URI结构解耦，并提高可演化性。

本文阐明了REST中“资源”的概念，指出它是URI可寻址的任何事物——物理对象、概念、文档或服务。它是一种概念映射，不一定是持久化实体。

Fielding关于REST API的六条规则被解释如下：1）不要依赖单一协议，2）不要改变协议，3）关注媒体类型，而不是URI，4）不要硬编码URI结构，5）避免对客户端重要的资源“类型”，以及6）从书签开始并跟随链接。这些规则通过超媒体促进了松耦合和客户端驱动的交互。

本文总结道，基于HTTP的更简单、类似RPC的API的流行可能是由于实际的权衡。像OpenAPI这样的工具提供了诸如代码生成和文档之类的直接好处，使得HATEOAS的长期架构优势显得不那么紧迫。

---

## 8. 通过恶意Chart实现的Helm本地代码执行

**原文标题**: Helm local code execution via a malicious chart

**原文链接**: [https://github.com/helm/helm/security/advisories/GHSA-557j-xg8c-q2mm](https://github.com/helm/helm/security/advisories/GHSA-557j-xg8c-q2mm)

本安全公告详细说明了 Helm（3.18.3 及更早版本）中一个高危漏洞，该漏洞可能允许本地代码执行。 此漏洞源于恶意制作的 `Chart.yaml` 文件，以及一个特别链接的 `Chart.lock` 文件。 当依赖项更新时（使用 `helm dependency update` 或通过 Helm SDK），`Chart.lock` 文件会被写入，如果它是指向可执行文件的符号链接（例如 `.bashrc` 文件或 shell 脚本），则锁文件的内容可以写入到链接的文件中，从而导致意外的代码执行。

核心问题在于，即使 Helm 发出警告，它也不会阻止在依赖项更新期间写入符号链接的文件。 这使得攻击者可以制作包含恶意代码的 `Chart.lock` 文件，并通过符号链接将其注入到目标文件中。

Helm 版本 3.18.4 中已修复此漏洞。 建议用户升级到此版本。 作为一种解决方法，用户应确保图表中的 `Chart.lock` 文件在更新依赖项之前不是符号链接。 该漏洞由 AlphaSense 的 Jakub Ciolek 发现。 它的 CVSS 评分为 8.5，突出了对保密性、完整性和可用性的潜在影响。 CVE ID 为 CVE-2025-53547。

---

## 9. 美国法院废止联邦贸易委员会“点击取消”的要求

**原文标题**: US Court nullifies FTC requirement for click-to-cancel

**原文链接**: [https://arstechnica.com/tech-policy/2025/07/us-court-cancels-ftc-rule-that-would-have-made-canceling-subscriptions-easier/](https://arstechnica.com/tech-policy/2025/07/us-court-cancels-ftc-rule-that-would-have-made-canceling-subscriptions-easier/)

美国一家上诉法院推翻了联邦贸易委员会(FTC)的“点击取消”规定，该规定本将强制公司使取消服务与注册一样容易。法院裁定，在Lina Khan担任主席期间，联邦贸易委员会未能遵循适当的规则制定程序。具体而言，法院发现，在一位行政法法官认定该规则的经济影响将超过1亿美元后，联邦贸易委员会并未进行必需的初步监管分析。

法院承认联邦贸易委员会旨在防止与订阅取消相关的不公平和欺骗行为，但强调程序上的缺陷是“致命的”。法官们认为，缺乏初步分析剥夺了行业团体充分质疑联邦贸易委员会关于成本效益分析和替代方案的调查结果的机会。

包括有线电视公司在内的行业团体和企业在法庭上对该规则提出了质疑。该裁决表明，联邦贸易委员会的行为可能为通过低估规则的初始经济影响以避免公众参与来操纵规则制定过程开创先例。

联邦贸易委员会于2024年10月批准了该规则，共和党委员对此表示反对，认为该规则过于宽泛，无法经受住法律挑战。

---

## 10. X 负责人表示她将离开该社交媒体平台。

**原文标题**: X Chief Says She Is Leaving the Social Media Platform

**原文链接**: [https://www.nytimes.com/2025/07/09/technology/linda-yaccarino-x-steps-down.html](https://www.nytimes.com/2025/07/09/technology/linda-yaccarino-x-steps-down.html)

无法访问文章链接。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 2 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 3 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 4 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 5 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 6 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 7 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 8 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 9 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 10 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 11 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 12 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 13 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 14 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 15 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 16 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 17 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 18 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 19 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 20 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 21 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 22 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 23 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 24 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 25 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 26 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 27 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 28 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 29 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 30 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 31 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 32 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 33 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 34 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 35 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 36 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 37 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 38 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 39 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 40 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 41 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 42 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 43 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 44 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 45 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 46 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 47 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 48 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 49 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 50 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 51 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 52 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 53 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 54 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 55 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 56 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 57 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 58 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 59 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 60 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 61 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 62 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 63 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 64 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 65 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 66 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 67 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 68 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 69 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 70 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 71 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 72 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 73 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 74 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 75 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 76 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 77 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 78 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 79 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 80 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 81 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 82 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 83 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 84 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 85 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 86 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 87 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 88 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 89 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 90 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 91 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 92 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 93 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 94 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 95 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 96 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 97 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 98 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 99 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 100 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 101 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 102 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 103 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 104 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 105 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 106 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 107 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 108 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 109 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 110 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 111 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 112 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
