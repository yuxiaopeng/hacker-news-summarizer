# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-31.md)

*最后自动更新时间: 2025-08-31 17:43:41*
## 1. 人人都能练的柔术

**原文标题**: Jujutsu for Everyone

**原文链接**: [https://jj-for-everyone.github.io/](https://jj-for-everyone.github.io/)

本文档是为Jujutsu版本控制系统(VCS)编写的入门级教程，专为没有Git或其他VCS工具使用经验的个人设计。与现有面向有经验Git用户的Jujutsu教程不同，本教程旨在为新手提供易于理解的学习材料。

本教程分为多个级别，每个级别侧重于特定的技能组合，从基本用法到高级工作流程。它从单人工作的最低要求开始，逐步发展到协作、问题解决、历史重写和生产力提升。每个级别都建立在前一个级别的基础上，并提供重置脚本来帮助用户恢复到任何特定章节的开头。

作者提倡学习Jujutsu而不是Git，因为它与Git兼容、易于学习且功能强大。虽然承认一些缺点，如同行中的不熟悉以及潜在的CLI不稳定，但作者认为Jujutsu的优势大于缺点，使其成为作为第一个VCS的有价值的选择。本教程旨在成为一个全面的资源，根据需要整合Git功能，并与最新的Jujutsu版本保持同步。鼓励读者提供反馈和建议，以提高教程的清晰度和完整性。

---

## 2. 此电报必须经过严密释义后方可传达。为什么？

**原文标题**: "This telegram must be closely paraphrased before being communicated" Why?

**原文链接**: [https://history.stackexchange.com/questions/79371/this-telegram-must-be-closely-paraphrased-before-being-communicated-to-anyone](https://history.stackexchange.com/questions/79371/this-telegram-must-be-closely-paraphrased-before-being-communicated-to-anyone)

二战时期电报中“密切释义”指令的原因是为了防止密码系统遭受“已知明文攻击”。当时的美国军方理论不鼓励使用不同加密方法（或不加密）发送完全相同的消息两次。释义是改变消息并避免这种做法的手段。根据一份解密的美国陆军密码学手册，释义包括在保留消息含义的同时对其进行广泛改写，包括改变句子结构、使用同义词以及避免重复的词语或专有名词。删除措辞比扩展措辞更可取。潜在的危险在于，如果对手可以将消息的未加密版本与其加密版本进行比较，则可能提供有价值的信息，从而帮助他们破解密码。盟军深知这一点，因为德国人使用了多种加密方式，并且捕获具有更容易破解的密码的机器，使得盟军能够解开来自更强大的恩尼格玛密码的消息。德国的程序缺陷和操作员失误也同样使盟军得以破解恩尼格玛密码。因此，“密切释义”指令是一项关键的安全措施，旨在通过防止可能危及密码系统的明文泄露来保护敏感信息。“密切”在这种情况下既意味着保持原始含义，也意味着在释义过程中要谨慎。

---

## 3. 管理注意力缺陷多动症笔记

**原文标题**: Notes on Managing ADHD

**原文链接**: [https://borretti.me/article/notes-on-managing-adhd](https://borretti.me/article/notes-on-managing-adhd)

本文详细介绍了管理多动症的方法，强调双管齐下的策略：策略（高级控制系统）和战术（微观改进）。文章认为药物治疗是首选方法，解决多动症的生物学基础并消除对其使用的羞耻感。作者以褪黑素为例，强调内部改变（如药物治疗）如何促成外部改变（更好的睡眠习惯）。

文章强调记忆辅助工具（如待办事项清单）作为“认知假肢”的重要性，用于记住任务、排序任务并将其分层分解。能量管理也至关重要，应在精力最充沛的早晨优先处理困难或令人畏惧的任务。

作者概述了三种类型的拖延症：多动症拖延症（通过药物治疗和生产力系统解决）、焦虑性拖延症（需要立即采取行动，尽管存在焦虑，并进行长期的情感根源分析）以及决策瘫痪性拖延症（需要外部输入和书面分析）。

最后，文章提倡将写日记作为内省的手段，以识别不良模式、跟踪进展并促进行为改变。作者以分层结构（每日、每周、每月、每年）组织日记，并对较高时间段进行更高级别的结构化回顾。

---

## 4. 为什么量子计算机还没能分解21？

**原文标题**: Why haven't quantum computers factored 21 yet?

**原文链接**: [https://algassert.com/post/2500](https://algassert.com/post/2500)

本文解释了为什么量子计算机尚未分解21，尽管它们在2001年已经分解了15，从而挑战了这种缺乏进展表明量子计算停滞不前的说法。 关键原因是分解21所需的电路复杂度比分解15的电路复杂度大幅增加。虽然分解15的电路有21个纠缠门，但分解21的电路需要惊人的2405个，复杂度超过100倍。

这种复杂性产生的原因是Shor算法依赖于条件模乘，对于15来说，由于其特定的属性，条件模乘的成本要低得多：许多乘法是乘以1（实际上是免费的），第一次乘法也几乎是免费的，并且剩余的乘法可以用简单的循环移位来实现。 这些优化不适用于分解21的情况。

具体而言，当分解21时，没有乘以1的乘法，第一次乘法提供的比例节省较少，并且剩余的乘法在计算上昂贵得多，需要更多的Toffoli门。 这三个因素导致了电路成本增加一百倍。

作者还指出，2001年对15的分解是用核磁共振计算机完成的，该计算机具有固有的扩展限制。 此外，量子纠错对于处理增加的门数量是必需的，这增加了额外的开销。 最后，作者警告不要产生误导性的“量子分解”结果，这些结果依赖于有效预先确定因子的优化。 他总结说，分解像21这样的小数字并不是衡量量子计算进展的好基准，并建议关注量子纠错和核心扩展挑战方面的进展。

---

## 5. F-Droid网站证书已过期

**原文标题**: F-Droid site certificate expired

**原文链接**: [https://gitlab.com/fdroid/fdroid-website/-/issues/883](https://gitlab.com/fdroid/fdroid-website/-/issues/883)

F-Droid网站的SSL证书于2023年3月17日过期，导致用户无法访问该网站，浏览器中出现安全警告。此问题已通过链接的GitLab issue报告并确认。

主要问题是证书需要续订，过期导致大范围中断，因为用户无法安全地访问F-Droid网站以下载应用程序或更新。这影响了主网站以及F-Droid客户端使用的API。

团队迅速响应并采取行动续订证书。他们表示需要改进监控和自动化，以防止将来再次发生证书过期的情况。修复措施包括续订Let's Encrypt证书，该证书用于加密往返网站的流量。

问题已相对较快地解决，用户报告说证书续订后网站再次可以访问。GitLab issue还记录了事件，允许用户跟踪解决进度，并为讨论预防措施提供空间。团队还表示，对根本原因的调查仍在进行中，以确保将来更好地管理证书。

---

## 6. 用数据库替换缓存服务

**原文标题**: Replacing a Cache Service with a Database

**原文链接**: [https://avi.im/blag/2025/db-cache/](https://avi.im/blag/2025/db-cache/)

本文探讨了用数据库取代缓存的想法，认为虽然数据库提供了一些优势，例如更简单的操作和使用熟悉的SQL，但由于缓存的成本更低、仅存储频繁访问数据的效率更高，以及能够处理高并发，因此缓存仍然占据主导地位。

作者建议使用只读副本作为缓存的潜在替代方案，利用数据库缓冲池中的内存数据以及许多缓存场景的非强一致性要求。 然而，文章强调了几个缺点：数据库由于存储更大的数据集而需要更多的资源，缺乏缓存中存在的对数据优先级进行细粒度控制的能力，并且难以扩展以处理缓存的连接需求。

作者指出了增量视图维护 (IVM) 引擎（如 Noria 和 ReadySet）的潜力，可以在数据库上下文中预先计算和缓存复杂的查询结果。他们还建议利用部分只读副本和分离式存储来进一步降低资源开销。 核心问题是如何将数据子集放入近缓存环境中。

总而言之，作者认为，虽然 IVM 和数据库架构的进步前景广阔，但目前用数据库直接取代缓存对于所有用例来说并不可行。 他们设想未来 IVM 和部分只读副本可以弥合差距，并可能导致 IVM 为外部缓存服务提供动力。

---

## 7. Infisical (YC W23) 正在招聘解决方案工程师，以扩展开源安全堆栈

**原文标题**: Infisical (YC W23) Is Hiring Solutions Engineers to Scale the OSS Security Stack

**原文链接**: [https://www.ycombinator.com/companies/infisical/jobs/yaEvock-solutions-engineer](https://www.ycombinator.com/companies/infisical/jobs/yaEvock-solutions-engineer)

Infisical（一家由Y Combinator (W23) 支持的公司，也是排名第一的开发者开源密钥管理平台）正在招聘解决方案工程师。Infisical 帮助企业管理敏感凭证，如 API 密钥和数据库访问令牌。他们的客户范围从 Hugging Face 这样的初创公司到大型企业。

解决方案工程师将专注于客户成功，包括引导新客户、扩大产品在客户帐户中的使用、运行概念验证、提供技术指导、收集客户反馈和改进文档。他们将与 CEO 和工程团队密切合作。该职位涉及识别客户工作流程中的痛点，并塑造产品路线图。

理想的候选人将拥有开发或系统工程方面的技术经验（理想情况下具有开源项目经验）、面向客户的经验（最好是技术产品），并且了解基础设施/DevSecOps 领域。还需要强大的沟通能力和强烈的工作热情。

该职位提供塑造产品路线图、扩大客户群以及建立客户成功和销售团队的巨大发展机会。薪酬包括 12 万美元至 18 万美元的工资、0.10% 至 0.30% 的股权，以及午餐补贴和工作设备预算等福利。Infisical 拥有一支远程团队，但在旧金山设有一间办公室，并计划举办团队聚会。

Infisical 已从 Gradient Ventures 等投资者以及 Elad Gil 和 Dropbox 和 Supabase 创始人等天使投资者那里筹集了 300 万美元。

---

## 8. 认知负荷至关重要

**原文标题**: Cognitive load is what matters

**原文链接**: [https://github.com/zakirullin/cognitive-load](https://github.com/zakirullin/cognitive-load)

本文强调**认知负荷**是影响代码可维护性和开发者生产力的主要因素。文章认为，降低认知负荷应成为软件开发实践的指导原则，超越诸如“小函数”或严格遵循单一职责原则等流行但经常被误用的概念。

文章区分了内在认知负荷（不可避免的任务难度）和外在认知负荷（由糟糕的设计选择引入）。重点在于最小化外在负荷。文章提供了实际案例，说明了常见的编码实践，如复杂的条件语句、深度嵌套的继承和过多的微服务，如何增加认知负担。

降低认知负荷的关键策略包括：

*   **使用描述性的变量名**来阐明复杂逻辑。
*   **采用提前返回**来简化代码流程并专注于“happy path”。
*   **优先使用组合而非继承**以避免复杂的类层次结构。
*   **创建具有简单接口的“深层”模块**，而不是需要理解复杂交互的众多“浅层”模块。
*   **限制语言特性**以减少选择和复杂性。
*   **在 API 中使用自描述字符串而不是数字状态**，以避免心理映射。

核心信息是，代码应该为了可读性和易于理解而编写，优先考虑开发者处理信息的心理能力。文章鼓励根据设计决策对认知负荷的影响进行评估，而不是盲目地遵循刻板的规则。

---

## 9. 微软员工家属警示科技公司勿过度压榨员工

**原文标题**: Family of MSFT employee who died warn tech companies not to overwork workers

**原文链接**: [https://padailypost.com/2025/08/29/family-of-microsoft-employee-who-died-warn-tech-companies-not-to-overwork-workers/](https://padailypost.com/2025/08/29/family-of-microsoft-employee-who-died-warn-tech-companies-not-to-overwork-workers/)

普拉提克·潘迪，一位35岁的微软员工，在公司山景城办公室去世。其家人正在敦促科技公司解决员工过度工作的问题。8月20日，潘迪被发现死于办公室庭院，初步评估显示死因为心脏病发作。

家人和朋友表示，潘迪工作时间很长，压力很大，需要同时处理多个项目。他的叔叔，马诺杰·潘迪，强调科技公司需要认识并缓解员工的压力，建议在员工经常熬夜工作时进行干预。

潘迪来自印度，事业有成，在2020年加入微软之前，曾在苹果、Illumina和沃尔玛实验室工作过。他被描述为一个积极且乐于助人、喜欢运动的人。他的家人在弗里蒙特举行了遗体告别仪式，然后将他的遗体送回印度，交给他的父母和姐妹。他们希望他的去世能促使科技公司优先考虑员工的福祉，并防止类似的悲剧发生。

---

## 10. 我的手机现在是电子阅读器了

**原文标题**: My phone is an ereader now

**原文链接**: [https://www.davepagurek.com/blog/minimal-phone/](https://www.davepagurek.com/blog/minimal-phone/)

好的，我需要更多信息才能总结文章。我只有标题和日期。

为了提供简洁的摘要，我需要2025年8月30日发表的题为“我的手机现在是电子阅读器了”的文章内容。

请提供文章的文本，我将很乐意在300字以内为您总结。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 2 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 3 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 4 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 5 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 6 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 7 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 8 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 9 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 10 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 11 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 12 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 13 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 14 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 15 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 16 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 17 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 18 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 19 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 20 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 21 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 22 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 23 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 24 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 25 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 26 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 27 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 28 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 29 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 30 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 31 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 32 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 33 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 34 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 35 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 36 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 37 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 38 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 39 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 40 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 41 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 42 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 43 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 44 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 45 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 46 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 47 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 48 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 49 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 50 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 51 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 52 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 53 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 54 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 55 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 56 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 57 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 58 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 59 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 60 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 61 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 62 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 63 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 64 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 65 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 66 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 67 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 68 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 69 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 70 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 71 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 72 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 73 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 74 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 75 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 76 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 77 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 78 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 79 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 80 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 81 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 82 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 83 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 84 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 85 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 86 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 87 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 88 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 89 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 90 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 91 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 92 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 93 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 94 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 95 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 96 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 97 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 98 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 99 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 100 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 101 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 102 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 103 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 104 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 105 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 106 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 107 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 108 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 109 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 110 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 111 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 112 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 113 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 114 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 115 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 116 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 117 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 118 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 119 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 120 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 121 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 122 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 123 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 124 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 125 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 126 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 127 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 128 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 129 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 130 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 131 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 132 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 133 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 134 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 135 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 136 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 137 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 138 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 139 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 140 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 141 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 142 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 143 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 144 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 145 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 146 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 147 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 148 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 149 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 150 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 151 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 152 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 153 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 154 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 155 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 156 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 157 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 158 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 159 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 160 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 161 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 162 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 163 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 164 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 165 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
