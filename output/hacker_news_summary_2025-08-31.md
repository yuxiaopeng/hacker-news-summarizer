# Hacker News 热门文章摘要 (2025-08-31)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 以资深程序员的姿态进行氛围编程：从8位汇编到英语即代码

**原文标题**: Vibe Coding as a Coding Veteran. From 8-Bit Assembly to English-as-Code

**原文链接**: [https://levelup.gitconnected.com/vibe-coding-as-a-coding-veteran-cd370fe2be50](https://levelup.gitconnected.com/vibe-coding-as-a-coding-veteran-cd370fe2be50)

马可·贝内代蒂，一位拥有40年经验的资深程序员，探索了“氛围编码”，即由AI助手处理编码任务。他进行了一项为期40小时的实验，与OpenAI的o3、Anthropic的Claude Sonnet 4和Google的Gemini Pro 2.5等AI助手共同开发了一个Python版的汉诺塔解算器。虽然o3最适合作为辅助助手，但Claude Sonnet 4因其卓越的理解和互动能力而成为主要助手。

贝内代蒂对AI理解代码和自然语言的能力印象深刻，往往超出他的预期。AI在Python中表现出超人的准确性和速度，甚至可以证明数学概念。他发现这种对话式的开发过程令人满意，并注意到与人类协作的相似之处。

然而，这些AI助手并非完美，也出现过各种错误。大约20%的交流涉及修复AI引入的问题。问题包括过度复杂的重构、对并发和并行的混淆、冗长的命名约定、不必要的代码重复以及性能折衷的解决方案。大约60%是需要迭代的“缺陷”，40%是需要大量修复的有缺陷的代码。尽管存在这些缺陷，贝内代蒂仍然承认AI编码助手的潜力，但强调需要人工监督和批判性评估。

---

## 12. FDA官员要求移除YouTube上他本人批评疫苗的视频。

**原文标题**: FDA official demands removal of YouTube videos of himself criticizing vaccines

**原文链接**: [https://www.theguardian.com/us-news/2025/aug/31/fda-official-youtube-videos](https://www.theguardian.com/us-news/2025/aug/31/fda-official-youtube-videos)

一位顶尖FDA疫苗监管者Vinay Prasad博士要求移除YouTube上批评新冠疫苗的个人视频。这些视频由Jonathan Howard博士编辑，旨在“保存”包括Prasad在内的各界人士在疫情早期的言论。YouTube以涉嫌侵犯版权为由删除了Howard的整个频道，其中包含约350个视频。

Howard辩称，这些视频只是记录了医生（包括Prasad等有影响力的人物）在疫情期间的言论，包括夸大疫苗对儿童的危害和低估新冠风险的言论。他认为这些视频对于理解Prasad目前的信誉至关重要。

Prasad的行为引发了关于审查制度和压制异议的质疑，尤其考虑到他过去曾抱怨社交媒体公司的审查行为。尽管Prasad早期的言论仍在反疫苗平台上流传，但他的删除要求似乎专门针对一位批评者。

该文章强调了Prasad备受争议的过往，包括他对新冠加强针、疫苗强制令和FDA下属CBER前负责人的批评。他的过去被描述为具有两面性，他曾是一位严谨的研究方法专家，但最近以批评支持口罩派而闻名。尽管面临过去的批评和短暂的辞职，Prasad还是回到了他的职位，并在限制新冠疫苗供应方面发挥了作用。

---

## 13. Bitwig Studio 6 详情公布，编辑功能大幅提升

**原文标题**: Bitwig Studio 6 details revealed, and editing gets a big boost

**原文链接**: [https://cdm.link/bitwig-studio-6-details/](https://cdm.link/bitwig-studio-6-details/)

Bitwig Studio 6 专注于增强编辑和工作流程，而非追逐 AI 或 stem 分离等潮流。此次更新旨在使 Bitwig 的编辑能力与其在即兴创作和项目创建方面的现有优势相媲美。拥有有效升级计划的用户目前可以使用 Beta 版本，完整版本预计将于秋季发布。

主要功能包括：

*   **自动化模式：** 轨道可以覆盖自动化通道，以进行专注编辑，不同于其他 DAW 的“一次全部通道”方法。
*   **改进的编辑手势：** 更容易抓取、拖动和覆盖自动化。
*   **自动化行为：** 自动化的扩散、保持和曲率选项。
*   **改进的工具：** 增强的喷枪工具、试听工具和带预览的铅笔工具。
*   **自动化片段：** 自动化可以与片段同时存在，并具有可选的父子关系。
*   **表情编辑：** 音符上直接可编辑增益、压力等。
*   **多片段编辑：** 在细节编辑器面板中一起编辑多个片段。
*   **片段别名：** 更新所有共享相同模式的副本的“主模板”片段。
*   **项目范围内的调号：** 适用于钢琴卷帘、捕捉到调性和音符效果。
*   **更新的界面：** 包括工具调色板、网格调整、编曲器自动缩放、动态轨道标题等。

此次更新还包括打开旧版本时自动备份项目文件。 虽然还没有主题，但文章强调了对自定义选项的需求。 作者对音阶/调性功能不太热情，但承认它们的用处。

---

## 14. 一个20年前的算法能帮助我们理解Transformer嵌入

**原文标题**: A 20-Year-Old Algorithm Can Help Us Understand Transformer Embeddings

**原文链接**: [http://ai.stanford.edu/blog/db-ksvd/](http://ai.stanford.edu/blog/db-ksvd/)

本文探讨了使用字典学习来理解大型语言模型（LLMs）的内部状态，通过将复杂的嵌入分解为可解释的概念向量。虽然稀疏自编码器（SAEs）最近在该任务中广受欢迎，但作者提倡重新审视有20年历史的KSVD算法。

作者证明，通过修改（双批次KSVD或DB-KSVD）和高效的实现，KSVD可以在语言模型可解释性的SAEBench基准测试中达到与SAE相当的性能，但处理速度明显更快（将处理时间从30天减少到8分钟）。DB-KSVD使用交替优化来更新概念向量的分配和概念向量本身。作者还提供了一个开源的Julia软件包KSVD.jl，方便实现和与Python集成。

除了DB-KSVD的性能之外，本文还探讨了字典学习的理论极限，指出恢复概念向量的可行性取决于数据集的大小和嵌入的维度。可恢复的概念向量的数量与样本数量的平方成正比，而每个样本可恢复的概念数量与嵌入维度的平方成正比。作者认为，鉴于有足够的数据和高维嵌入，字典学习在语言之外的各个领域（如机器人和视觉）具有潜在的应用。

---

## 15. eBPF 101：内核编程入门

**原文标题**: eBPF 101: Your First Step into Kernel Programming

**原文链接**: [https://journal.hexmos.com/ebpf-introduction/](https://journal.hexmos.com/ebpf-introduction/)

本文为初学者提供了eBPF（扩展伯克利包过滤）的入门介绍，并通过构建一个简单的防火墙来演示其在内核编程中的应用。eBPF允许用户在Linux内核中运行沙盒程序，从而扩展其功能而无需修改内核源代码。

本文指导读者创建两个文件：`probe.c`，其中包含用C语言编写的eBPF程序，以及`runner.py`，一个用于加载、附加和监视eBPF程序的Python脚本。C程序计算传入的网络数据包，并阻止到指定IP地址（8.8.8.8）的流量。Python脚本使用`bcc`库与eBPF程序交互，包括将其加载到内核中，使用XDP（eXpress Data Path）将其附加到网络接口，监视数据包计数，以及处理调试事件（丢弃的数据包）。

代码演示了解析网络头部，使用原子操作递增数据包计数器，以及基于目标IP地址丢弃数据包。本文还介绍了设置Python虚拟环境、安装必要的依赖项，以及使用信号处理实现优雅的关闭机制。

结论部分强调了eBPF被主要科技公司广泛采用，用于网络可观测性、安全性和基础设施调试，突出了其在现代系统中的重要性。它鼓励读者学习和采用eBPF。

---

## 16. Show HN: 基于ncurses的CUDA流体模拟

**原文标题**: Show HN: An ncurses CUDA-based fluid simulation

**原文链接**: [https://github.com/seanwevans/fluid-sims](https://github.com/seanwevans/fluid-sims)

此“Show HN”帖子展示了一个使用 ncurses 库实现的基于 CUDA 的流体模拟。作者展示了不同配置和场景下的模拟演示视频，具体包括 Burgers' 方程模拟、天气相关模拟、3D 流体模拟和 2D 流体模拟。帖子依赖于提供的视频链接来展示流体模拟的能力和视觉效果。本质上，作者是在分享他们的基于 ncurses 的流体模拟项目，突出其多功能性，并通过各种模拟示例展示不同的视觉输出。

---

## 17. 如何在Windows 7 x64上运行最新Vegas Pro 22

**原文标题**: How to run latest Vegas Pro 22 in Windows 7 x64

**原文链接**: [https://trackerninja.codeberg.page/post/how-to-run-latest-vegas-pro-22-in-windows-7-no-matter-what/](https://trackerninja.codeberg.page/post/how-to-run-latest-vegas-pro-22-in-windows-7-no-matter-what/)

本文详细介绍了如何在已停止支持的Windows 7 x64系统上运行最新的Vegas Pro 22，由于其已停止支持，该操作属于官方不支持的行为。作者将此过程描述为“dirty-hack”，并概述了几个强制步骤。

首先，用户必须使用Simplix补丁更新Windows 7，安装.NET Framework 4.8.0（而非4.8.1），更新DirectX9，并安装Visual C++ 2005-2022。然后，通过将特定的DLL文件（api-ms-win-core-version-l1-1-1.dll，d3d11on12.dll，d3d12.dll，dxilconv7.dll）提取到“C:\Windows\System32”文件夹来安装DirectX12兼容层。可能需要再次运行Simplix补丁以安装其他更新。

最关键的部分是解决“Createdxgifactory2 could not be located in the dynamic link library dxgi.dll”错误。作者不建议全局替换系统的DXGI.DLL，因为这可能会导致系统不稳定。相反，他们建议使用Vegas 22的本地副本。

作者发现使用从旧版本Reshade（特别是v4.9.1，v5.2.0或v6.4.0）中提取的DXGI.DLL可以成功解决问题，将提取的文件RESHADE64.DLL重命名为DXGI.DLL，并将其放置在与Vegas 22可执行文件相同的目录中。这提供了Windows 7版本的DXGI.DLL中缺少的必要图形功能。作者还提到可能需要将其重命名为D3D11.DLL。

最后，文章包含一个脚本，用于在退出应用程序后终止Vegas Pro的残留进程，以防止内存泄漏。文章指出此过程中不需要VxKex。

---

## 18. 谷歌：千元手机装应用需经我许可 [视频]

**原文标题**: Google: 'Your $1000 phone needs our permission to install apps now' [video]

**原文链接**: [https://www.youtube.com/watch?v=QBEKlIV_70E](https://www.youtube.com/watch?v=QBEKlIV_70E)

文章题为“谷歌：‘你花1000美元买的手机现在需要我们的许可才能安装应用’[视频]”，可能讨论的是一项备受争议的谷歌政策变更，该变更涉及安卓设备上的应用安装。虽然提供的内容只是YouTube的页脚，没有提供文章细节，但我们可以推断出核心问题。

标题强烈暗示谷歌正在实施一项系统，用户需要在他们的安卓手机上安装应用程序时获得谷歌的许可或批准，即使是昂贵的高端设备也是如此。这意味着控制权发生了重大转变，可能会限制侧载（在Google Play商店之外安装应用程序）。

令人担忧的是，这种改变可能会限制用户的自由，并可能影响在Play商店之外分发应用程序的开发者以及喜欢替代应用程序来源的用户。这篇文章可能探讨了这项改变背后的原因（安全性、恶意软件预防、收入控制）、对用户隐私和应用程序生态系统的潜在影响，以及对谷歌因声称对安卓设备拥有更大控制权而受到的批评。该视频可能对这一政策变更进行了更深入的分析。

---

## 19. Red：一种受 REBOL 启发的编程语言

**原文标题**: Red: A programming language inspired by REBOL

**原文链接**: [https://github.com/red/red](https://github.com/red/red)

Red 是一种受 REBOL 启发的编程语言，旨在通过其原生代码编译器实现更广泛的应用。它支持多种编程范式，并内置了 DSL，如 Red/System（系统编程）、Parse（PEG 解析器）、VID（GUI 布局）、Draw（2D 绘图）和富文本。

目前 Red 处于 alpha 阶段且仅支持 32 位，它拥有诸如人性化语法、同像性、函数式/命令式/响应式/符号编程、基于原型的对象、多类型、模式匹配宏和丰富的数据类型等特性。它提供静态和 JIT 编译到原生代码（JIT 尚未实现）、交叉编译、无依赖的小型可执行文件、强大的并发支持（actor，并行集合 - 尚未实现）、底层系统编程、强大的 PEG 解析器、快速垃圾回收以及跨平台 GUI 系统。

该工具链包括封装器、编译器、解释器和链接器，在 1.0 版本之后将自托管。您可以通过 GUI 或 CLI 控制台运行 Red，使用 `redc -c hello.red` 等命令生成独立的可执行文件进行编译，并使用 `-r` 进行发布模式。使用 `-t` 选项支持交叉编译到其他平台。

对于贡献者，Red 可以使用 Rebol 解释器从源代码运行。贡献需要遵循准则，将更改告知 Red 团队，并确保测试通过。某些防病毒程序可能会报告 Red 二进制文件的误报，应向供应商报告。Red 和 Red/System 在 BSD 许可下授权，而运行时在 BSL 许可下授权。

---

## 20. 我对V语言的初探

**原文标题**: My Foray into Vlang

**原文链接**: [https://kristun.dev/posts/my-foray-into-vlang/](https://kristun.dev/posts/my-foray-into-vlang/)

本文记录了作者对 Vlang 的探索，并将其与 Go 进行了比较。作者认为 Go 语言具有实用性，但缺乏趣味性。Vlang 被描述为 “vanilla++”，提供了类似 Go 的熟悉语法，并添加了额外的功能。

作者重点介绍了 Vlang 中他欣赏的几个方面，包括其 map 处理、具有必需字段和默认值的结构体，以及 `WithOption` 模式，解决了 Go 中与可选参数相关的冗长问题。枚举是另一个受欢迎的补充，它提供了一种更简洁的方式来表示离散值。此外，作者还赞扬了 Vlang 的 lambda 表达式和数组方法，从而增强了代码的表达能力。

尽管有这些优点，作者也承认 Vlang 的不成熟性和潜在挑战。他们详细描述了在使用 `net.http` 模块时遇到的问题，需要在编译期间使用 `-d use_openssl` 标志，以及 `veb` HTTP 服务器中令人困惑的导入顺序依赖性。文章还提到了由于 Vlang 的 C 后端而导致的构建过程的复杂性增加，这需要使用标志进行性能优化和交叉编译。最后，作者注意到在并发基准测试中，Vlang 的性能与 Go 相比存在差异，需要手动调整构建过程。

总而言之，作者发现 Vlang 前景广阔，具有令人向往的功能，但他也认识到，与 Go 更直接的方法相比，其不成熟性和更复杂的构建过程带来了障碍。

---

## 21. 老程序员也能跟上编程的节奏

**原文标题**: Older developers are down with the vibe coding vibe

**原文链接**: [https://www.theregister.com/2025/08/28/older_developers_ai_code/](https://www.theregister.com/2025/08/28/older_developers_ai_code/)

调查显示资深开发者更常使用AI代码生成工具

---

## 22. 层化：通往数学精通的最佳路径：速成之道 (2022)

**原文标题**: Sheafification – The optimal path to mathematical mastery: The fast track (2022)

**原文链接**: [https://sheafification.com/the-fast-track/](https://sheafification.com/the-fast-track/)

无法访问文章链接。

---

## 23. 使用 Harbor 在本地运行 Docker 镜像仓库

**原文标题**: Running our Docker registry on-prem with Harbor

**原文链接**: [https://dev.37signals.com/running-our-docker-registry-on-prem-with-harbor/](https://dev.37signals.com/running-our-docker-registry-on-prem-with-harbor/)

2025年8月，Farah Schüller详细介绍了37signals公司因在云迁移和采用Kamal的过程中，使用Dockerhub和Amazon ECR等外部注册表时遇到的成本、性能、安全和独立性问题，而将其Docker注册表迁移到使用Harbor的内部部署方案。

选择Harbor的原因是其丰富的功能集和可扩展性，他们使用docker-compose部署了一个单服务器设置。v1版本的实现侧重于使用他们自己的S3存储（Pure FlashBlade），复制站点以实现故障转移，并启用保留策略以优化存储。他们确定了Harbor正常运行所需的最低S3存储桶权限。

最初的设置涉及位于阿什本和芝加哥的两个独立Harbor实例，由F5负载均衡器提供前端服务。端点之间的复制使用Terraform配置，采用双向方案，确保每10分钟同步一次数据，并复制Pure集群上的底层S3存储桶。

为了迁移现有的Dockerhub镜像目录，由于Dockerhub API的限制，他们为每个存储库创建了单独的复制规则，并使用脚本进行自动化。他们开发了一个脚本来从Dockerhub拉取存储库列表，生成Terraform配置，并创建复制规则。另一个脚本按字母顺序分批启用这些规则。一个监控脚本跟踪Harbor UI中复制任务的进度。

---

## 24. OpenTelemetry 中的 Traces 和 Spans 是什么？

**原文标题**: What Are Traces and Spans in OpenTelemetry?

**原文链接**: [https://oneuptime.com/blog/post/2025-08-27-traces-and-spans-in-opentelemetry/view](https://oneuptime.com/blog/post/2025-08-27-traces-and-spans-in-opentelemetry/view)

本文全面介绍了如何使用 OpenTelemetry 理解和实施分布式追踪，尤其是在 Node.js/TypeScript 应用程序中。文章强调，追踪显示了时间在整个系统中的花费，是对指标和日志的补充。

文章解释了核心概念，包括：**追踪（Traces）**（请求的完整旅程）、**跨度（Spans）**（追踪中已计时的工作单元）、**上下文（Context）**（在系统中传播的追踪信息）、**采样器（Samplers）**（决定记录哪些追踪），以及**导出器（Exporters）**（将追踪数据发送到 OneUptime 或 Jaeger 等后端）。

文章详细介绍了跨度的结构，重点关注名称、时间戳、ID、父 ID、属性、事件、状态和类型等元素。文章使用可视化模型来说明跨度如何形成表示请求流程的树，并识别延迟区域。跨度类型（SERVER、CLIENT、INTERNAL、PRODUCER、CONSUMER）对于正确解释和分析追踪数据至关重要。

文章涵盖了实际实现，包括在 Node.js 中使用自动插桩设置 OpenTelemetry，以及使用 `withSpan` 进行手动插桩以实现自定义控制。文章提供了用于插桩 Express 中间件、数据库查询和外部 API 调用的示例。文章还讨论了错误记录的最佳实践、属性和事件的使用，以及需要避免的反模式。

---

## 25. 你得去感受它

**原文标题**: You Have to Feel It

**原文链接**: [https://mitchellh.com/writing/feel-it](https://mitchellh.com/writing/feel-it)

米切尔·桥本的文章《你必须亲身感受》认为，成功的工作不仅仅是满足需求和达到指标。虽然时间表、需求和演示很重要，但它们往往无法捕捉到感觉这一关键要素。

作者认为，每一次互动，包括与我们创造的产品和服务的互动，都会唤起一种感觉。这种感觉，无论是喜悦、沮丧还是解脱，都是工作本身不可或缺的一部分，应该被视为一项要求。

桥本强调了亲身体验工作的重要性。当一个功能“感觉对了”，当它引起积极的情感反应和重复使用的愿望时，它就标志着真正的成功。这种直观的满足感无法被传统指标准确量化或捕捉。

这篇文章敦促创作者积极参与他们的工作，去“体验它、使用它、与它共处”，以便了解它在用户身上唤起的感觉。通过优先考虑用户的情感体验，创作者可以超越简单地打勾勾，交付真正引起共鸣并改善日常生活的作品。本质上，这篇文章强调，除了技术熟练之外，还需要同理心和直觉理解，才能创造出有影响力和成功的产品。

---

## 26. 最新研究显示寿命增长放缓，百岁人生不太可能实现

**原文标题**: New research reveals longevity gains slowing, life expectancy of 100 unlikely

**原文链接**: [https://lafollette.wisc.edu/news/new-research-reveals-longevity-gains-slowing-life-expectancy-of-100-unlikely/](https://lafollette.wisc.edu/news/new-research-reveals-longevity-gains-slowing-life-expectancy-of-100-unlikely/)

威斯康星大学麦迪逊分校拉福莱特公共事务学院的最新研究表明，人类寿命增长速度正在放缓，这使得百岁寿命在不久的将来变得普遍的可能性降低。这项由Kristen Malecki教授和Collin Strawhacker研究员领导的研究，分析了几个发达国家在寿命不平等、平均寿命以及人口活到非常高龄（85岁以上）的比例方面的趋势。

他们的研究结果表明，虽然过去一个世纪平均寿命显着增加，但近几十年来增长速度已大大放缓。他们还观察到达到极高年龄的人数趋于稳定，表明人类寿命存在固有的生物学限制。该研究表明人类寿命存在“上限”，这可能受到遗传倾向、环境因素和医疗进步的局限性等因素的影响。

此外，该研究强调了寿命不平等的重要性——人们寿命长短的差异。虽然平均寿命是一个有用的指标，但如果由于贫困、缺乏医疗保健或环境危害等因素导致某些人口的寿命明显缩短，它就无法说明全部情况。因此，即使平均寿命不太可能大幅增加，减少寿命不平等对于改善整体公共卫生和福祉至关重要。该研究强调需要关注改善健康公平，解决导致寿命差异的根本因素，而不是仅仅追求平均寿命的进一步提高。

---

## 27. shared_ptr<T>: (并非总是)原子引用计数智能指针 (2019)

**原文标题**: Shared_ptr<T>: the (not always) atomic reference counted smart pointer (2019)

**原文链接**: [https://snf.github.io/2019/02/13/shared-ptr-optimization/](https://snf.github.io/2019/02/13/shared-ptr-optimization/)

本文研究了GNU的libstdc++中`std::shared_ptr<T>`令人惊讶的行为，特别是其引用计数机制。作者最初注意到，在C++中复制共享指针比Rust中等效的`Arc::clone`调用快得多。通过性能分析发现，libstdc++对引用计数采用了有条件的原子/非原子递增。

文章深入研究了实现细节，表明`__gthread_active_p()`决定了是否使用原子或非原子操作。此函数检查`pthread_key_create`符号的存在，并由此推断多线程的使用情况。如果该符号不存在，表明是单线程上下文，则使用非原子操作作为优化。

作者质疑了这种方法的安全性，探讨了在没有`pthread`的情况下实现并行性的场景，例如通过原始OS系统调用或静态编译二进制文件中的动态链接库。虽然这些情况被认为是罕见的，但它们可能导致不正确的共享指针行为（悬挂指针、内存泄漏）。

作者将libstdc++的行为与libcxx（允许在编译时禁用线程）和VisualC++（始终使用原子操作）进行了比较。最终，作者得出结论，虽然libstdc++优化在典型场景中通常是安全的，但非常见的环境可能会暴露潜在问题。本文是对微基准测试以及理解底层库实现重要性的一个警示。作者还强调了Rust的等效项`Arc`，它*总是*使用原子操作，提供更强的线程安全保证。

---

## 28. 用于临床辅助的眼科基础模型

**原文标题**: An eyecare foundation model for clinical assistance

**原文链接**: [https://www.nature.com/articles/s41591-025-03900-7](https://www.nature.com/articles/s41591-025-03900-7)

本文介绍 EyeFM，一种多模态视觉-语言 AI 模型，旨在作为眼科临床辅助工具。它使用 1450 万张眼部图像和临床文本配对的大型数据集进行预训练。

该研究对 EyeFM 进行了多方面的评估，包括回顾性验证、一项涉及 44 位眼科医生的多国疗效验证，以及在中国进行的涉及 668 名参与者的双盲随机对照试验 (RCT)。 该 RCT 评估了 EyeFM 在高危人群中对视网膜疾病筛查的影响。

RCT 结果显示，与标准治疗相比，使用 EyeFM 的眼科医生实现了显著更高的正确诊断率（92.2% 对 75.4%）和转诊率（92.2% 对 80.5%）。 EyeFM 还提高了临床报告的标准化程度。 各组患者满意度相似，但 EyeFM 组在随访中表现出更高的自我管理依从性和转诊建议依从性。 部署后评估表明用户接受度很高。

该研究得出结论，EyeFM 可以提高眼科医生的表现和患者的治疗效果，表明其作为临床眼科有价值工具的潜力。 数据和代码的可用性已提供，以供研究之用。

---

## 29. 是否能在允许侧载的同时保障用户安全？

**原文标题**: Is it possible to allow sideloading and keep users safe?

**原文链接**: [https://shkspr.mobi/blog/2025/08/is-it-possible-to-allow-sideloading-and-keep-users-safe/](https://shkspr.mobi/blog/2025/08/is-it-possible-to-allow-sideloading-and-keep-users-safe/)

本文探讨了安卓系统侧载的复杂问题，及其对用户安全与用户自由的影响。谷歌要求开发者在侧载应用前必须注册并进行数字签名的新规，一方面被视为打击诈骗和恶意软件蔓延的必要措施，另一方面则被认为是限制用户自主权的一种权力攫取。

作者承认，银行和游戏开发商等公司希望保护其系统和客户免受已root或被入侵设备上的恶意活动侵害，这种担忧是合理的。作者认为，虽然自定义设备的自由是可取的，但公司有权保护自己免受不值得信任的软件环境造成的损害。

然而，作者强烈反对谷歌的新政策，认为这是试图控制安卓生态系统，并扼杀独立开发者和开源项目的举措。他们担心谷歌对开发者账户的控制将导致审查，并限制用户运行他们想要运行的代码的能力。

尽管作者承认侧载应用带来的诈骗问题非常严重，尤其是在巴西、印度尼西亚、新加坡和泰国等国家，但作者质疑谷歌解决方案的有效性及其潜在的滥用可能性。最终，本文提出了关于平衡用户自由、安全和大型公司权力等方面的几个难题。文章在没有明确解决方案的情况下结束，突出了在保护弱势用户的同时又不侵犯他人权利的内在困境。

---

## 30. 无点击，无内容：AI搜索不可持续的未来

**原文标题**: No Clicks, No Content: The Unsustainable Future of AI Search

**原文链接**: [https://bradt.ca/blog/no-clicks-no-content/](https://bradt.ca/blog/no-clicks-no-content/)

人工智能搜索模式难以为继：威胁内容生态系统

---

## 31. Sniffly – Claude 代码分析仪表盘

**原文标题**: Sniffly – Claude Code Analytics Dashboard

**原文链接**: [https://github.com/chiphuyen/sniffly](https://github.com/chiphuyen/sniffly)

Sniffly：Claude 代码使用分析面板，旨在帮助用户理解并改进 Claude 代码的使用。它分析 Claude 代码日志，以识别使用模式、分解错误，并允许用户查看消息历史记录。主要功能包括：了解使用模式、识别常见错误以及分析消息历史记录，从而改进代码执行。

使用 Sniffly 入门很简单，可以使用 UV、pip 或从 GitHub 克隆源代码。安装后，`sniffly init` 命令会初始化仪表板，可通过 Web 浏览器访问。

可以使用 `sniffly config` 命令自定义仪表板，以调整端口号和自动打开浏览器等设置。用户还可以通过生成的链接与同事分享其项目的统计信息和说明，并可以选择隐私设置（私有或公开）以及是否包含命令文本。

文档包括针对常见问题的故障排除提示，例如端口冲突或浏览器打开问题。它强调 Sniffly 优先考虑隐私，通过完全在本地运行、在用户机器上处理数据而不进行遥测，并确保对话保持私密，除非明确共享。

---

## 32. 你可以收藏的终端会话

**原文标题**: Terminal sessions you can bookmark

**原文链接**: [https://poor.dev/blog/building-zellij-web-terminal/](https://poor.dev/blog/building-zellij-web-terminal/)

本文详细介绍了Zellij内置Web客户端的开发，该客户端允许用户通过Web浏览器访问并与终端会话交互。核心思想是扩展Zellij现有的客户端/服务器架构，其中服务器在后台维护终端会话。Web客户端充当另一个客户端，通过Web服务器中介与服务器通信。

该架构涉及每台机器运行一个Web服务器来处理多个会话。会话通过其URL唯一标识，允许用户将其加入书签。通信通过WebSockets进行，终端数据（STDOUT/STDIN）和控制消息使用单独的通道。

安全是关键考虑因素。用户使用在Zellij会话中生成的令牌进行身份验证，该令牌在服务器端进行哈希处理，并交换为临时Cookie。HTTPS对外部接口强制执行。

Web服务器使用Rust和`axum`框架构建，利用其灵活性以及与`tokio`的集成来实现异步操作。静态资源直接包含在可执行文件中。守护进程化由`daemonize` crate处理，错误报告通过Unix管道进行。

客户端使用`xterm.js`进行终端仿真，并针对鼠标AnyEvent跟踪和窗口标题更新等功能进行了自定义集成。虽然考虑过TypeScript，但由于额外的构建步骤带来的开销，最终被拒绝。

未来的计划包括扩展带有原生UI组件的Web界面，混合多个Zellij会话，并可能提供托管解决方案。

---

## 33. 地主老农：一个致力于将网络农民变成网络地主的网站

**原文标题**: LandChad, a site dedicated to turning internet peasants into Internet Landlords

**原文链接**: [https://landchad.net](https://landchad.net)

LandChad.net 是一个网站，旨在帮助个人通过指导他们设置自己的网站、电子邮件服务器和其他在线服务，从而成为“互联网房东”。该网站提倡去中心化的互联网所有权，认为更多个人平台可以解决互联网当前的许多问题。

该网站提供两个主要的“课程”：一个是设置基本网站，另一个是建立个人电子邮件服务器。网站课程涵盖域名注册、服务器获取、DNS配置、Nginx Web服务器设置以及使用Certbot实施HTTPS。电子邮件课程包括发送/接收电子邮件、rDNS设置、DNS电子邮件验证、收件箱设置和服务器强化。这两个课程的设计目标是相对快速地完成。

除了这些核心课程之外，LandChad.net 还提供设置各种自托管服务的教程，分类为“[服务]”，包括网络邮件（AlpsAlps，Rainloop）、数字图书馆（Calibre）、Git服务器（Cgit，Gitea）、聊天服务器（Coturn，ejabberd，Matrix Synapse，Matrix Dendrite，Prosody，IRC，Jitsi，Mumble）、云存储（Nextcloud）、视频托管（PeerTube）、微博（Pleroma）、支付网关（Fosspay）和隐私工具（Dnsmasq，i2p，Monero，Tor，Wireguard，SearXNG）。

最后，该网站在“[服务器]”标签下提供文章，以帮助掌握服务器管理，涵盖诸如Certbot、cronjobs、Gemini、SSH、UFW防火墙、页面质量、HTTP身份验证、Rsync、服务器端脚本和一般自托管等主题。LandChad.net 还提供加密货币地址，供用户支持该项目。

---

## 34. 书籍为何开始分章节？一段新的历史

**原文标题**: Why did books start being divided into chapters? A new history

**原文链接**: [https://sydneyreviewofbooks.com/reviews/just-a-little-longer](https://sydneyreviewofbooks.com/reviews/just-a-little-longer)

提供的文字并非关于书籍章节历史的文章，而是劳伦斯·斯特恩的小说《项狄传》的节选。这段文字描绘了叙述者在一次谈话后一时冲动决定前往法国的情景。他和某人争论，对方断言自己在法国的经历。这促使叙述者质疑如此短暂的航行所带来的好处，并最终导致他突然收拾行装，亲自前往法国。他优先考虑携带最少的衣物，并冲动地开始了旅程。这段节选突出了叙述者异想天开且离题万里的风格，这是斯特恩小说的特点。它并未涉及文学中章节划分的历史或发展。

---

## 35. 代理客户端协议 (ACP)

**原文标题**: Agent Client Protocol (ACP)

**原文链接**: [https://agentclientprotocol.com/overview/introduction](https://agentclientprotocol.com/overview/introduction)

智能体客户端协议 (ACP) 是一种正在开发的标准，旨在简化代码编辑器（IDE、文本编辑器）和编码智能体（修改代码的 AI 程序）之间的通信。它旨在解决编辑器和智能体之间紧密耦合和互操作性有限的问题，即每个编辑器都需要为每个智能体进行自定义集成，反之亦然。

ACP 的目标是将智能体和编辑器解耦，使它们能够独立创新，并为开发者提供更多选择。它允许实现 ACP 的智能体与任何兼容的编辑器一起工作，而支持 ACP 的编辑器可以访问广泛的智能体生态系统。这消除了集成开销，扩大了兼容性，并减少了开发者的锁定。

该协议的工作方式是让智能体作为代码编辑器的子进程运行，并使用基于 stdio 的 JSON-RPC 进行通信。它在适用的情况下利用 MCP 的 JSON 表示，并结合自定义类型来实现类似智能体的编码 UX 元素，如显示差异。默认文本格式是 Markdown，因为它具有丰富的格式化功能，而无需在代码编辑器中进行 HTML 渲染。目前，Zed 和 neovim（通过 CodeCompanion 插件）是支持的编辑器，而 Gemini 是支持的智能体，预计将添加更多。

---

## 36. Bcachefs 进入“外部维护”阶段

**原文标题**: Bcachefs Goes to "Externally Maintained"

**原文链接**: [https://lwn.net/Articles/1035736/](https://lwn.net/Articles/1035736/)

LWN.net文章讨论了Linux内核中Bcachefs维护者状态变更为“外部维护”，表明未来更改不太可能很快合并到主线内核中。此举引发了人们对树内Bcachefs代码未来的质疑。

一些评论者推测了潜在的结果。一种建议是指定一位Linus Torvalds可以接受的新维护者来处理向上游推送补丁。另一种可能性是内核将继续发布一个过时的版本，最终会逐渐腐烂并被移除，Bcachefs可能会像ZFS一样以树外方式分发。第三种可能性较小的情况是内核会fork Bcachefs并维护一个修改后的版本。

Bcachefs的原始开发者Kent Overstreet表达了对内核发布过程和维护者倦怠的担忧。他强调了稳定的发布过程对于支持用户和响应错误报告的重要性。虽然Overstreet确认了他开发一个健壮的文件系统的承诺，但他承认与内核的发布过程合作所面临的挑战。他强调说，他可以接受bcachefs作为DKMS模块发布。

Overstreet还讨论了其他Linux文件系统的当前状态，表达了对XFS维护者流失以及Btrfs持续存在的可靠性问题的担忧。他最终表示他的目标是创建一个可靠的文件系统，无论内核发生什么。

---

## 37. 强化火狐浏览器——提升浏览器隐私的检查清单

**原文标题**: Hardening Firefox – a checklist for improved browser privacy

**原文链接**: [https://andrewmarder.net/firefox/](https://andrewmarder.net/firefox/)

本文提供了一份强化 Firefox 以提升用户隐私的清单。文章认为，虽然像 Brave 这样的浏览器提供了开箱即用的隐私保护，但由于 Mozilla 的非营利地位、开源承诺以及对 Chromium 引擎的规避，Firefox 是一个更优的选择。

该清单分为三个部分：基本隐私设置、推荐扩展和高级配置。

**基本隐私设置：** 包括将默认搜索引擎更改为像 DuckDuckGo 这样注重隐私的选项，启用 HTTPS-Only 模式以强制安全连接，禁用遥测以防止 Mozilla 收集数据，以及将增强跟踪保护设置为“严格”以实现强大的跟踪器阻止。

**推荐扩展：** 建议安装 uBlock Origin 以进行全面的内容和广告拦截，安装 ClearURLs 以从 URL 中删除跟踪元素，以及安装 Privacy Badger 以根据行为自动阻止隐形跟踪器。

**高级配置（about:config）：** 需要访问 `about:config` 页面（并警告潜在风险）来修改内部设置。最初建议将 `privacy.firstparty.isolate` 设置为 `true` 以将 Cookie 隔离到第一方域名（但这可能会破坏单点登录）。作者还提到尝试使用 `privacy.resistFingerprinting` 来抵抗浏览器指纹识别，但由于兼容性问题，最终恢复为默认设置。

文章最后鼓励读者使用该清单来改善他们的 Firefox 隐私，并在评论中提供反馈。

---

## 38. 地裂正在撕裂城市

**原文标题**: Cracks in the Earth Are Slicing Through Cities

**原文链接**: [https://www.scientificamerican.com/article/giant-gullies-in-the-earth-threaten-cities-in-africa-amid-rapid-urbanization/](https://www.scientificamerican.com/article/giant-gullies-in-the-earth-threaten-cities-in-africa-amid-rapid-urbanization/)

非洲城市巨型冲沟迅速扩张，受强降雨等自然因素以及排水不足和城市化等人为因素共同驱动。《自然》杂志发表的一项研究发现，26个城市中存在近3000条城市冲沟，绵延数百公里。这些冲沟吞噬房屋和企业，仅在刚果民主共和国，2004年至2023年间就导致平均118,600人流离失所，这一数字自2020年以来翻了一番。

研究人员估计，未来十年将有数十万人面临风险。道路沿线积水加剧了这个问题，由于排水系统不良，道路充当了运河。该研究强调了冲沟扩张带来的灾难性，有时甚至是致命的后果，特别是对于缺乏替代住房的弱势群体而言。

作者强调需要投资于预防措施，因为稳定现有冲沟的成本要高得多。他们建议优先发展可持续基础设施，包括有效的排水系统，并让受影响的社区参与规划干预措施。预计到2050年非洲人口将增加两倍，降雨强度预计也会增加，因此，采取紧急行动对于缓解城市冲沟扩张日益增长的威胁至关重要。

---

## 39. AI模型需要虚拟机

**原文标题**: AI models need a virtual machine

**原文链接**: [https://blog.sigplan.org/2025/08/29/ai-models-need-a-virtual-machine/](https://blog.sigplan.org/2025/08/29/ai-models-need-a-virtual-machine/)

本文倡议开发一个标准化的“AI模型虚拟机”(MVM)，以提高人工智能应用的安全、可靠性和互操作性。微软和华盛顿大学的一组研究人员观察到，当前的人工智能应用，尤其是那些利用大型语言模型(LLM)的应用，正变得越来越复杂，需要强大的控制软件来管理模型、外部工具和用户之间的交互。

借鉴Java虚拟机(JVM)的经验，他们提出了一种MVM，作为AI模型和系统其余部分之间的中间层。该MVM将定义一组指令，用于加载模型、调用工具、管理内存和执行安全策略等任务。

本文重点介绍了现有工作，如OpenAI的工具调用、Anthropic的MCP以及诸如FIDES和AC4A等以安全为中心的项目，作为MVM概念的前身。然后详细介绍了良好定义的MVM的关键优势，包括关注点分离、内置安全和治理、透明的性能跟踪以及模型输出的可验证性。作者强调，MVM可以为AI模型创建一个“一次编写，随处运行”的环境，从而促进更广泛的采用和创新。最后，他们敦促社区参与建立对这种规范的需求的共识，以及它应该包含哪些内容，以提高AI系统的可移植性、互操作性、安全性和可靠性。

---

## 40. SQL设计模式 (2010)

**原文标题**: SQL Design Patterns (2010)

**原文链接**: [https://vadimtropashko.wordpress.com/%e2%80%9csql-design-patterns%e2%80%9d-book/about/](https://vadimtropashko.wordpress.com/%e2%80%9csql-design-patterns%e2%80%9d-book/about/)

SQL设计模式（2010）概括了在SQL数据库中解决常见数据操作挑战的各种技术和方法。它侧重于利用SQL来实现超出基本查询和数据管理的特定功能。

本文涵盖了一系列主题，包括：

*   **计数：** 执行复杂计数的技术，可能涉及条件聚合或唯一值识别。

*   **整数生成器：** 在SQL中生成整数序列的方法，可用于各种任务，如数据填充、填补数据集中的空白或创建测试数据。

*   **奇异运算符：** 利用较少见的SQL运算符或函数来实现专门的任务，可能在特定情况下提高性能或简化代码。

*   **约束：** 实施各种约束类型，以确保数据完整性并在数据库中强制执行业务规则。

*   **树和图：** 使用SQL在关系数据库中表示和操作树状和图结构化数据，包括遍历层次结构和查找关系的技术。

本质上，本文充当开发人员的指南，旨在通过提供更高级的数据操作和表示问题的解决方案来充分利用SQL的强大功能。

---

## 41. 我们去中心化了吗？

**原文标题**: Are we decentralized yet?

**原文链接**: [https://arewedecentralizedyet.online/](https://arewedecentralizedyet.online/)

我们去中心化了吗？ (这个网站用于衡量去中心化社交网络，如联邦宇宙（长毛象，像素联邦）和大气层（蓝天，白风）上用户数据的集中度。它使用赫芬达尔-赫希曼指数（HHI）和香农指数来评估联邦宇宙中用户数据在服务器/实例之间的分布，以及大气层中用户数据在PDS（个人数据服务器）之间的分布。

HHI借鉴于经济学，用于指示市场集中度。较低的值表明系统更加去中心化，而较高的值则表明用户数据更集中在少数服务器/PDS上。香农指数用于生态学，用于衡量熵，并提供了数据分布的另一种视角。较高的值意味着更均匀的分布。

该网站汇总了由同一实体运行的服务器的数据（例如，mastodon.social和mastodon.online）。它侧重于活跃用户，并承认数据位置只是去中心化的一个方面。其他因素包括网络结构、身份管理、托管基础设施、法律管辖权以及平台内的权力集中程度。创建者鼓励通过GitHub贡献其他去中心化指标。

---

## 42. 秃鹰公司的库斯科RISC-V核心将在2025年Hot Chips大会上亮相

**原文标题**: Condor's Cuzco RISC-V Core at Hot Chips 2025

**原文链接**: [https://chipsandcheese.com/p/condors-cuzco-risc-v-core-at-hot](https://chipsandcheese.com/p/condors-cuzco-risc-v-core-at-hot)

本文预览Condor Computing公司在2025年Hot Chips大会上展示的Cuzco RISC-V内核。Condor是晶心科技(Andes Technology)的子公司，旨在提供类似于Arm和SiFive的可授权RISC-V内核。Cuzco内核是一款高性能的8路乱序设计，目标市场与SiFive的P870和Veyron的V1相同。它拥有先进的分支预测器，并计划在台积电5nm工艺上实现2-2.5 GHz的时钟频率。

一项关键创新是其“基于时间”的调度方案，该方案使用时间资源矩阵 (TRM) 在重命名/分配阶段预测指令调度，从而降低后端调度器的复杂性和功耗。这不需要任何ISA修改或特殊的编译器处理。

Cuzco具有高度可配置性，允许客户调整执行切片的数量、L2 TLB大小、总线宽度以及L2/L3缓存容量。内核以最多八个为一组进行集群排列，并通过CHI总线进行通信以实现可扩展性。

前端采用先进的TAGE-SC-L分支预测器和两级分支目标缓冲区。指令提取逻辑从64KB指令缓存中获取指令。

后端利用来自重命名器的预先计算的调度，简化了乱序执行。指令重放处理可变延迟指令，例如缓存未命中。执行资源被分组到具有专用执行队列 (XEQ) 的切片中。该内核支持256/512位VLEN，并提供每周期8个FMA操作。加载/存储单元具有专用队列和物理索引、物理寻址的L1数据缓存。L3缓存被分成切片以匹配核心数量。

文章总结指出，Cuzco试图在已建立的乱序执行模型中进行创新，提供一种潜在的高效方法，同时保持RISC-V兼容性。

---

## 43. 关税实施六个月，企业不知如何定价。

**原文标题**: Six months into tariffs, businesses have no idea how to price anything

**原文链接**: [https://www.wsj.com/business/retail/trump-tariff-business-price-impact-37b630c8](https://www.wsj.com/business/retail/trump-tariff-business-price-impact-37b630c8)

无法访问文章链接。

---

## 44. 不具有鲁珀特性质的凸多面体

**原文标题**: A convex polyhedron without Rupert's property

**原文链接**: [https://arxiv.org/abs/2508.18475](https://arxiv.org/abs/2508.18475)

Jakob Steininger和Sergey Yurkevich于2025年8月25日提交的这篇arXiv预印本，探讨了度量几何中与鲁珀特性质相关的问题。如果一个三维凸体的一个全等副本可以通过穿过它的一个直孔，则该凸体具有鲁珀特性质。该论文构建了一个凸多面体，该多面体明显*不具备*鲁珀特性质，从而反驳了一个可以追溯到2017年的猜想。此外，作者还找到了一个*是*鲁珀特性质但*不是*局部鲁珀特性质的多面体。该文章被归类为度量几何、计算几何和组合数学，并使用了MSC分类51-08和51-04。提交内容包括论文的PDF和实验性HTML版本以及TeX源代码的链接。本质上，作者通过提供一个反例来解决了一个开放问题，证明并非所有凸多面体都具有鲁珀特性质，并提供了一个具有该性质条件形式的对象。

---

## 45. 安杜里尔的产品工程体系

**原文标题**: Anduril's product engineering machine

**原文链接**: [https://joincolossus.com/article/the-amusement-park-for-engineers/](https://joincolossus.com/article/the-amusement-park-for-engineers/)

阿德南·伊斯梅尔的文章罕见地展现了安杜里尔公司快速产品工程方法的内部运作，回顾了他从第20名员工到工程高级副总裁的经历。他强调了安杜里尔公司非传统的运作方式，正是这些方式推动了其快速增长，并对美国国防科技产生了巨大影响。

伊斯梅尔认为，安杜里尔公司成功的核心在于其挑战既定规范和优先考虑速度的意愿。早期，该公司专注于使用现成的材料（例如改造过的电线杆和游戏PC）来创建最小可行演示，以快速交付功能性解决方案。这种敏捷性使他们能够获得合同并根据实际表现进行迭代。

伊斯梅尔强调了安杜里尔公司的“质疑一切”原则，其反无人机技术（Anvil）和巡航导弹侦测方法就是典范。他们挑战了现有的假设，改造了商业技术，并快速构建了原型解决方案，其性能优于传统且昂贵的系统。

安杜里尔公司的文化培养了对战略影响的执着追求，甚至在工作时间之外，并强调从第一性原理进行工程设计。这包括将问题分解为基本组成部分，并在设计解决方案时考虑到部署问题。这篇文章赞扬了安杜里尔公司快速构建原型、测试和交付解决方案的能力，并强调速度和对结果的关注是他们成功的关键。

---

## 46. 出版商为何准备将其网站联合起来

**原文标题**: Why publishers are preparing to federate their sites

**原文链接**: [https://digiday.com/media/why-publishers-are-preparing-to-federate-their-sites/](https://digiday.com/media/why-publishers-are-preparing-to-federate-their-sites/)

在平台式微之际，出版商为何准备联合网站？

本文探讨了出版商为何准备联合其网站，原因在于他们希望在 Facebook 和 X 等平台可靠性下降之际，重新掌控引荐流量和受众参与度。允许不同平台互操作的联邦宇宙提供了一个解决方案。《The Verge》和 404 Media 正率先采用这种方法。他们的目标是在自己的网站和 Threads、Mastodon 和 Bluesky 等联邦平台同时分发内容，并将回复整合到网站的评论区。这得益于 ActivityPub，一种促进与联邦平台集成的插件，WordPress 和 Ghost CMS 等平台正在采用它。Flipboard 也积极参与其中，聚合内容并将出版商与联邦社交网络连接起来。文章强调，联邦宇宙提供了与读者的直接关系，消除了对大型平台的依赖。虽然与 Facebook 和 X 等巨头相比，联邦平台目前的用户群较小，但《The Verge》和 404 Media 等出版商将其视为一种有前景的替代方案。他们认为联邦宇宙提供了一个更人性化、更去中心化的互联网，赋予出版商和受众更大的控制权。通过专注于改进其主页和网站，出版商旨在创建吸引忠实读者的目的地。《The Verge》已经看到了积极的结果，其主页的读者人数和访问时长均有所增加。

---

## 47. 做最简单可行的事情。

**原文标题**: Do the simplest thing that could possibly work

**原文链接**: [https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/](https://www.seangoedecke.com/the-simplest-thing-that-could-possibly-work/)

本文倡导“做可能工作的最简单的事情”这一软件设计原则。它反对过度设计，并强调在增加不必要的复杂性之前，要深刻理解当前的系统。作者认为，软件设计的真正精髓往往在于少做，从而产生看似简单却有效的解决方案。

文章引用了 Unicorn 和 Rails REST API 等例子，认为它们是令人印象深刻的设计，因为它们以最直接的方式解决了问题。作者以速率限制为例，说明在求助于 Redis 等更复杂的基础设施之前，应该考虑更简单的解决方案，如内存存储或边缘代理配置。

文章还探讨了对此方法的常见反对意见，例如创建“大泥球”和忽视可扩展性的风险。作者反驳说，hack 本质上是复杂的，而简单性涉及更少的活动部件、清晰的接口和稳定性。关于可扩展性，作者认为，过早地针对规模进行优化往往适得其反，并导致代码库缺乏灵活性。他们建议专注于当前的需求，并根据需要逐步扩展。核心要点是优先理解当前系统，并选择满足当前需求的最简单解决方案，同时保持对随着需求演变而进行调整的开放态度。

---

## 48. 默认陷阱：Anthropic数据政策变更为何重要

**原文标题**: The Default Trap: Why Anthropic's Data Policy Change Matters

**原文链接**: [https://natesnewsletter.substack.com/p/the-default-trap-why-anthropics-data](https://natesnewsletter.substack.com/p/the-default-trap-why-anthropics-data)

无法访问文章链接。

---

## 49. 猪肺移植入人体

**原文标题**: Pig lung transplanted into a human

**原文链接**: [https://www.sciencealert.com/pig-lung-transplanted-into-a-human-in-major-scientific-first](https://www.sciencealert.com/pig-lung-transplanted-into-a-human-in-major-scientific-first)

2025年8月，中国进行了一项开创性实验，将一只基因改造猪的肺移植到一位脑死亡患者体内。 这标志着猪肺首次移植到人体，代表了异种器官移植领域的一项重大进展。

该猪肺来自一只六基因编辑的巴马小型猪，在受体内工作了九天。 该实验旨在观察患者对异体器官的免疫反应，而不是寻求长期解决方案。 虽然避免了立即发生的超急性排斥反应，但患者表现出越来越多的器官排斥迹象，包括严重的肿胀和抗体介导的损伤，导致原发性移植功能障碍。 实验最终被终止。

文章强调了肺移植的复杂性，因为肺脏直接暴露于外部环境，并作为抵御病原体的第一道防线。 尽管面临挑战，研究人员证明了猪肺可以移植到人体内而不会立即发生超急性排斥反应。

研究人员强调，需要继续研究以优化免疫抑制方案，完善基因改造，改进肺脏保存策略，并评估长期移植功能。 他们得出结论，这项研究为克服必须克服的障碍提供了重要的见解，从而可以更接近肺异种器官移植的临床应用。

---

## 50. SQL上的组合式Datalog：环境的关系代数

**原文标题**: Compositional Datalog on SQL: Relational Algebra of the Environment

**原文链接**: [https://www.philipzucker.com/compose_datalog/](https://www.philipzucker.com/compose_datalog/)

本文探讨了一种使用SQL实现Datalog的新方法，重点是将Datalog环境（变量绑定）表示为SQL中的关系。作者不是直接操作Datalog关系（如`edge`或`path`），而是使用SQL的关系代数来操作Datalog主体表达式所产生的环境。

核心思想是Datalog主体、SQL的SELECT-FROM-WHERE结构和关系代数表达式都是表达合取查询的不同方式。作者展示了一个基于Python的组合器实现，该实现将基本Datalog关系转换为环境关系。然后，这些关系通过SQL擅长的内部连接进行连接。

本文介绍了`RelDecl`和`EnvRel`类来表示SQL中的关系和环境。`RelDecl`用于定义关系（如`edge/2`），而`EnvRel`表示查询产生的环境（变量绑定集）。重载运算符（`&`用于合取，`<=`用于规则定义）允许以更自然的语法表达Datalog规则，从而生成SQL查询。

作者展示了如何使用SQL中的朴素评估来实现不动点计算（运行规则直到没有产生新的结果）。作为奖励，本文探索了使用自动微分中的“对偶数”概念的半朴素评估，有效地跟踪SQL中的主要关系和增量关系。此方法通过仅考虑每次迭代中的新事实来实现更高效的不动点计算。该方法展示了一种利用SQL的关系能力来增强Datalog的逻辑表达能力的方法，并增强了不动点计算和半朴素评估等功能。

---

## 51. 瑞克·比托批评音乐版权警告是对的

**原文标题**: Rick Beato is right to rant about music copyright strikes

**原文链接**: [https://savingcountrymusic.com/rick-beato-is-right-to-rant-about-music-copyright-strikes/](https://savingcountrymusic.com/rick-beato-is-right-to-rant-about-music-copyright-strikes/)

乡村音乐拯救者：播客音乐版权侵权问题——Rick Beato的怒吼

---

## 52. 维利布

**原文标题**: WeLib

**原文链接**: [https://welib.org](https://welib.org)

无法访问文章链接。

---

## 53. 吴恩达称人工智能初创公司的瓶颈不是编码，而是产品管理。

**原文标题**: Andrew Ng says bottleneck in AI startups isn't coding – it's product management

**原文链接**: [https://www.businessinsider.com/andrew-ng-product-management-bottleneck-coding-ai-startups-2025-8](https://www.businessinsider.com/andrew-ng-product-management-bottleneck-coding-ai-startups-2025-8)

这篇文章引自《商业内幕》，强调了吴恩达的观点，即人工智能初创公司面临的主要障碍不是技术编码能力，而是有效的产品管理。吴恩达认为，虽然编码技能至关重要，但真正的瓶颈在于定义清晰、有价值且可行的产品。

他认为，许多人工智能初创公司拥有强大的技术能力，但难以识别人工智能能够有效解决并以用户友好的方式交付的现实问题。本质上，他们缺乏强大的产品愿景和对用户需求、市场机遇以及如何将复杂的人工智能技术转化为切实解决方案的深刻理解。

吴恩达认为，扎实的产品管理技能对于指导开发过程、确保产品与市场需求相符，以及应对人工智能部署和采用的挑战至关重要。这包括市场调研、用户体验设计、数据分析和战略规划方面的技能。他强调，如果一个技术上出色的人工智能解决方案不能解决真正的需求，或者用户难以理解并将其融入工作流程，那么它就是毫无用处的。本质上，这篇文章强调了产品思维和强大的产品管理在推动人工智能初创公司成功中的重要性，并认为在当前环境下，这比纯粹的编码能力更为关键。

---

## 54. 有时软件已完成，或为什么是 Hugo (2024)

**原文标题**: Sometimes Software Is Done, or Why Hugo Why (2024)

**原文链接**: [https://commaok.xyz/post/on_hugo/](https://commaok.xyz/post/on_hugo/)

这篇题为“有时软件就该完工，或 Hugo 为什么（2024）”的博文，表达了对 Hugo 静态网站生成器的不满。作者最初喜爱 Hugo 的速度、简洁和高效。然而，他们认为持续开发已使 Hugo 变得更大、更复杂，并且容易破坏向后兼容性。

作者感叹于修复由更新和弃用造成的构建失败所浪费的时间，这些时间原本可以用来写作。他们对无关紧要的文件更改和导致破坏的晦涩弃用警告感到恼火。作者强调，他们只将 Hugo 用于一个小博客，并不关心其内部运作，只想要一个可靠的工具。

厌倦了持续的维护需求，作者宣布他们正在考虑 Hugo 的替代方案。与此同时，他们计划从源代码编译 Hugo，避免未来的更新，并从根本上冻结其功能，以保留一个可用的版本。核心信息是对向后兼容性的呼吁，以及“有时软件应该被认为是‘完成’的”以维持稳定并防止不必要的复杂性的论点。他们欢迎关于替代静态网站生成器的建议。

---

## 55. 更便宜的激光器能处理短距离吗？

**原文标题**: Can cheaper lasers handle short distances?

**原文链接**: [https://semiengineering.com/can-cheaper-lasers-handle-short-distances/](https://semiengineering.com/can-cheaper-lasers-handle-short-distances/)

本文探讨了使用更廉价的激光器，特别是垂直腔面发射激光器（VCSEL），进行短距离光通信的应用，尤其是在数据中心内部。虽然光纤技术在长途通信中已成熟应用，但重点正在转向更短的距离，以用光纤代替铜线，实现更快、更高效的数据传输。

文章强调了激光器与硅集成的挑战，包括可靠性、温度敏感性和能耗。目前使用的是分布式反馈激光器（DFB），但其成本高于VCSEL。

VCSEL常见于光电鼠标等应用中，具有易于制造和成本较低等优点，但也存在波长非标准化、带宽较宽和功率较低等局限性，使其不太适合硅光子学应用。然而，对于简单的互连，这些局限性可能并不重要。

文章讨论了改进VCSEL的努力，包括开发更长的波长，并解决模式和偏振问题。像Volantis Semiconductor这样的公司正在为光学中介层设计改进型VCSEL，强调提高耐温性和能效。

结论表明，虽然VCSEL由于某些特性历来不太受欢迎，但最近的进步和改进可能使其成为数据中心内短距离光互连的可行且经济高效的选择，并有可能用于非光子应用。

---

## 56. 历史学家认为特朗普对科学的攻击是专制剧本的再现

**原文标题**: Historians See Autocratic Playbook in Trump's Attacks on Science

**原文链接**: [https://www.nytimes.com/2025/08/31/science/trump-science-autocrats.html](https://www.nytimes.com/2025/08/31/science/trump-science-autocrats.html)

无法访问文章链接。

---

## 57. Spectrum – 在编译时捕获 clojure.spec 一致性错误

**原文标题**: Spectrum – catching clojure.spec conform errors at compile time

**原文链接**: [https://github.com/arohner/spectrum](https://github.com/arohner/spectrum)

Spectrum是一个用于Clojure的静态分析库，旨在编译时捕获`clojure.spec`的conform错误，其功能类似于基于`clojure.spec`注解的可选静态类型系统。目前它处于开发者预览阶段，尚未准备好用于生产环境。

该库优先考虑可用性和速度，而不是完美性，旨在以最少的误报捕获大部分错误（约80%），即使它不能保证100%的错误检测。

使用方法是像往常一样使用`clojure.spec`，然后在REPL中使用`(f/infer-var #'foo)`或`(f/infer-form '(foo 3))`来检查代码。`infer-form`可以用来调试form的签名，并且可以接受一个变量到类型映射的map。

Spectrum通过以下方式解决了`clojure.spec`的局限性：检查返回值（`instrument`不检查），处理非纯函数，解决编写生成器的难题，启用对非`defn`函数、高阶函数和非fn变量的规范，确保所有代码路径都被检查，并减轻慢速生成测试。目前的开发重点是使Spectrum具有自检能力。

---

## 58. SynthID – 用于给人工智能生成的内容添加水印和识别的工具

**原文标题**: SynthID – A tool to watermark and identify content generated through AI

**原文链接**: [https://deepmind.google/science/synthid/](https://deepmind.google/science/synthid/)

SynthID是一种新的谷歌工具，旨在为人工智能生成的内容添加水印和识别，从而促进生成式人工智能使用的透明度和信任。它旨在解决区分人工智能生成内容和人类创建内容的问题。

SynthID通过将数字水印直接嵌入到人工智能生成的图像、音频、文本或视频中来工作。这些水印对人类来说是不可见的，但可以被SynthID的技术检测到。该工具将被集成到谷歌的生成式人工智能消费者产品中。

SynthID检测器允许用户上传内容（图像、视频、音频文件或文本片段）以确定它是否是使用谷歌人工智能创建的。

谷歌正在积极与各公司合作，使用SynthID为他们的人工智能生成内容添加水印，这是其更广泛的目标的一部分，即提高人工智能生成作品的透明度和信任度。用户有机会加入早期测试者候补名单，公司有机会成为SynthID合作伙伴。

---

## 59. 多重定时器工具

**原文标题**: Multi-Timer Gizmo

**原文链接**: [https://pgadey.ca/notes/multi-timer/](https://pgadey.ca/notes/multi-timer/)

帕克·格林-阿迪记录了他们创建“多重定时器”的项目，灵感来源于一位学者使用多个时钟追踪不同任务的记忆。该项目由朋友（戴夫·高尔）基于树莓派的多重定时器所启发。

该项目始于试图通过添加拨动开关来改装一个廉价闹钟。在努力打开闹钟却不小心将其损坏后，他们转而使用“电池消除器”从外部切换时钟的电源。

接下来，他们的目标是同时为多个时钟供电。最初考虑使用单选按钮和旋转开关（探索“旋钮术语”），但最终他们创建了一个面板，每个时钟都有单独的开关。

文章强调了作者缺乏电子背景，并在学习的过程中享受拆卸和重建的过程，让人想起他们的童年。虽然不确定多重定时器的使用频率，但他们预计它可用于粗略估计花费在任务上的时间。他们还提到了与“万用表”混淆的可能性，并澄清了命名。

作者还回忆起童年时一位瑞士制表匠邻居，他影响了他们对修补的兴趣。

---

## 60. 太阳能热电发电机性能提升15倍

**原文标题**: 15-Fold increase in solar thermoelectric generator performance

**原文链接**: [https://www.nature.com/articles/s41377-025-01916-9](https://www.nature.com/articles/s41377-025-01916-9)

本文提出了一种光谱调控和热管理策略，旨在显著提高太阳能热电发电机（STEG）的性能。研究人员通过优化发电机的冷热两端，在重量仅增加25%的情况下，实现了STEG发电量15倍的提升。

在热端，利用飞秒（fs）激光处理将常规钨（W）表面转化为选择性太阳能吸收器（W-SSA）。该技术提高了太阳能吸收率（超过80%的效率），同时最大限度地减少了红外发射率。还设计了一个温室腔室，以进一步减少W-SSA的对流热损失。

在冷端，使用飞秒激光处理将常规铝（Al）转化为微结构散热器（μ-散热器），与常规铝制散热片相比，冷却性能提高了一倍。这是通过增强辐射和对流散热实现的。

结合光谱调控和热管理策略，增加了STEG的温差（ΔT），从而大幅提高了输出功率。飞秒激光处理被强调为一种与传统方法相比具有可扩展性和环境友好性的技术。优化的W-SSA表现出良好的光谱选择性和温度稳定性，使其成为一种合适的吸收材料。数值模拟和实验结果证明了该方法的有效性。高效STEG的潜在应用包括无线传感器网络、可穿戴电子设备和医疗传感器。

---

## 61. Show HN: Hacker News em dash 用户排行榜（ChatGPT 之前）

**原文标题**: Show HN: Hacker News em dash user leaderboard pre-ChatGPT

**原文链接**: [https://www.gally.net/miscellaneous/hn-em-dash-user-leaderboard.html](https://www.gally.net/miscellaneous/hn-em-dash-user-leaderboard.html)

gally.net 的文章《Show HN：ChatGPT 前 Hacker News 破折号用户排行榜》展示了一个排行榜，该榜单根据 Hacker News 用户在评论中历史使用破折号（—）的情况进行排名，特别关注 ChatGPT 和其他大型语言模型广泛应用 *之前* 的时期。作者认为，分析聊天机器人时代之前破折号的使用情况，或许能更真实地了解个人写作风格，避免 AI 辅助写作显著扭曲结果。

该排行榜是通过抓取和分析 Hacker News 评论生成的，统计每位用户使用的破折号数量。作者强调了其中涉及的技术挑战，特别是处理嵌套 HTML 的复杂性和高效处理大量文本数据的难题。

作者指出，该排行榜是一个有趣且可能略显荒谬的项目，但也表明它为 Hacker News 社区内的交流模式和写作风格提供了一个古怪的窗口。他还提到了分析的局限性，例如没有考虑引用文本中的破折号，也没有区分不同类型的破折号。该项目提醒我们，即使关注像破折号使用这样看似微不足道的元素，对在线交流的风格分析也能揭示一些信息。

---

## 62. 上帝创造了实数

**原文标题**: God created the real numbers

**原文链接**: [https://www.ethanheilman.com/x/34/index.html](https://www.ethanheilman.com/x/34/index.html)

伊森·海尔曼的文章《上帝创造了实数》探讨了一个哲学问题，即某些数学概念是神启的还是人为的，文章以利奥波德·克罗内克的名言“上帝创造了整数，其余皆为人的工作”为出发点。作者认为，整数以其简洁和优雅，感觉像是人类的创造，而实数以其内在的复杂性和“存在的恶心感”，感觉更接近于自然界的奇异，暗示着一种可能的上帝起源。

海尔曼引入了一个“怪异层级”，表明从人类的角度来看，越接近“永恒自然”（神圣）的事物越怪异，而越接近人类思想的事物则越简单且更易于理解。他将克罗内克对无穷的反感与康托尔对超穷数的拥抱进行了对比，并指出康托尔相信他的工作是神启的。这也提到了笛卡尔基于人类对无穷的感知而提出的上帝存在的标志性论证。

作者最终倾向于认为，实数令人不安的本质表明它与人类无法理解的事物有关，而整数更像是人类为解决特定问题而设计的工具。文章以一种“基于感觉的漫谈”结束，留给读者思考数学真理的本质及其潜在的起源。

---

## 63. 新的解释表明“热寂”假说可能不成立 (2023)

**原文标题**: New interpretations suggest the "heat death" hypothesis might not hold (2023)

**原文链接**: [https://www.noemamag.com/life-need-not-ever-end/](https://www.noemamag.com/life-need-not-ever-end/)

本文挑战了“热寂”假说，该假说认为宇宙会因热力学第二定律而不可避免地变得越来越混乱且毫无生气。本文重点介绍了新兴的解释，表明情况可能并非如此。

热寂假说指出，在封闭系统中，熵（混乱度）会增加，导致所有可用能量最终耗散，以及复杂性、组织和生命本身的终结。然而，本文认为，宇宙作为一个膨胀的系统，可能不受与封闭系统相同的约束，而这些约束被用于推导热力学第二定律。

包括Seth Lloyd、Eric Chaisson、Freeman Dyson、Stuart Kauffman、Christof Koch和Ray Kurzweil在内的几位著名科学家被提及，他们认为宇宙随着时间的推移变得更加复杂和有组织，生命可能在其中发挥着关键作用。朱利安·巴伯在他的著作《雅努斯点》中认为，通常解释的第二定律并不适用于膨胀的宇宙，暗示秩序可以无限增加。大卫·多伊奇更进一步，认为知识创造没有根本的限制，暗示了生命持续存在的潜力。

本文深入探讨了热力学的历史，区分了第二定律的经典和统计解释。经典观点侧重于能量的耗散，而路德维希·玻尔兹曼推广的统计观点则侧重于分子水平上的混乱度增加。玻尔兹曼将第二定律应用于整个宇宙，将其设想为一个趋于混乱的封闭系统，从而导致了热寂情景。

然而，本文暗示，如果宇宙不是一个封闭系统，复杂性和秩序的持续增长是可能的，从而挑战了与热寂假说相关的末日预言。文章总结说，只要智能生命找到自由能，就可以增加组织度。

---

## 64. 诺基亚的传奇字体是优秀的用户界面字体。

**原文标题**: Nokia’s legendary font makes for a great user interface font

**原文链接**: [https://www.osnews.com/story/143222/it-turns-out-nokias-legendary-font-makes-for-a-great-general-user-interface-font/](https://www.osnews.com/story/143222/it-turns-out-nokias-legendary-font-makes-for-a-great-general-user-interface-font/)

本文探讨了作者的发现，即诺基亚Sans字体（2002年至2013年诺基亚设备上使用的标志性字体）作为通用用户界面(UI)字体，效果出人意料地好。作者Thom Holwerda出于怀旧，在网上找到各个变体后，决定尝试使用诺基亚Sans。

他推荐使用“Wide”变体，呼应了该字体的创造者Erik Spiekermann的观点，Spiekermann不同意诺基亚放弃它的决定，声称它不能作为UI字体使用。Spiekermann批评替代字体平淡无奇，浪费了品牌认知度。

Holwerda发现诺基亚Sans具有高度可读性和个性，取代Inter成为他首选的UI字体。他承认这是一种个人偏好，并鼓励读者自己尝试。他指出他的经验是在高DPI显示器和Wayland上的KDE环境下，在Windows或macOS等其他系统，或者在较低DPI显示器上，结果可能有所不同。

评论区揭示了其他人使用该字体的体验，特别是其与N900等诺基亚设备的怀旧联系。一些用户报告在Xfce上成功使用它，而另一些用户，特别是在较低DPI显示器上，认为它太宽了。对话还涉及诺基亚过去在软件支持方面的问题，以及与其他Linux UI体验的比较。

---

## 65. 新的风暴强度等级可能引入飓风6级

**原文标题**: Hurricane category 6 could be introduced under new storm severity scale

**原文链接**: [https://www.livescience.com/planet-earth/hurricanes/now-is-the-time-hurricane-category-6-could-be-introduced-under-new-storm-severity-scale](https://www.livescience.com/planet-earth/hurricanes/now-is-the-time-hurricane-category-6-could-be-introduced-under-new-storm-severity-scale)

本文探讨了一种拟议的新飓风分级系统——热带气旋强度等级（TCSS），旨在提高公众对飓风危险的认识，使其超越风速。目前的萨菲尔-辛普森飓风等级（SSHWS）仅依赖于风速，未能考虑到风暴潮和降雨带来的重大风险，而风暴潮和降雨约占飓风相关死亡人数的 80%。

卡特里娜飓风（3 级）和弗洛伦斯飓风（1 级）等案例表明，SSHWS可能会低估风暴的严重程度，导致准备不足和悲惨后果。TCSS 旨在通过将风速、风暴潮和降雨纳入六个等级的量表来解决这些缺点。它为每种危害分配分数，并使用特定规则将它们组合起来以确定最终等级。

一项测试 TCSS 的研究表明，与收到 SSHWS 预报的参与者相比，收到 TCSS 预报的参与者能够更好地识别主要危害，并且更有可能因非风力相关危险而撤离。研究人员认为，采用 TCSS 将提高公众对飓风风险的理解，并促进更明智的决策，最终带来更好的准备和更少的生命损失。

---

## 66. 删除测试

**原文标题**: Delete tests

**原文链接**: [https://andre.arko.net/2025/06/30/you-should-delete-tests/](https://andre.arko.net/2025/06/30/you-should-delete-tests/)

This article argues that deleting tests, a practice often considered taboo, is sometimes necessary and beneficial for software development. The core purpose of tests is to provide confidence that changes won't break existing functionality. However, when tests become unreliable or hinder the development process, they undermine this confidence.

The author identifies several scenarios where deleting tests is advisable:

*   **Flaky tests:** Randomly failing tests erode trust and cause developers to ignore genuine failures. The cost of maintaining flaky tests outweighs the potential benefit of catching future bugs.
*   **Overly coupled tests:** Tests that require extensive modification for minor code changes reduce efficiency and don't significantly increase confidence.
*   **Slow tests:** Test suites that take too long to run lead to skipping tests, creating a false sense of security and potentially masking bugs.
*   **Obsolete tests:** Tests that reflect outdated business requirements waste time and resources if updated. It's better to focus on testing the new behavior directly.

In essence, the article advocates for a pragmatic approach to testing, prioritizing quality and relevance over quantity. Deleting tests that are no longer effective or efficient can improve developer productivity and maintain confidence in the codebase.


---

## 67. Scottish brothers finish mammoth row across Pacific Ocean after 139 days

**原文标题**: Scottish brothers finish mammoth row across Pacific Ocean after 139 days

**原文链接**: [https://www.abc.net.au/news/2025-08-30/scottish-maclean-brothers-finish-pacific-ocean-row/105711488](https://www.abc.net.au/news/2025-08-30/scottish-maclean-brothers-finish-pacific-ocean-row/105711488)

生成摘要时出错

---

## 68. Bi-directional accountability: A leadership shift most organizations avoid

**原文标题**: Bi-directional accountability: A leadership shift most organizations avoid

**原文链接**: [https://www.alnewkirk.com/bidirectional-accountability/](https://www.alnewkirk.com/bidirectional-accountability/)

生成摘要时出错

---

## 69. Income Equality in Nordic Countries: Myths, Facts, and Lessons

**原文标题**: Income Equality in Nordic Countries: Myths, Facts, and Lessons

**原文链接**: [https://www.aeaweb.org/articles?id=10.1257/jel.20251636](https://www.aeaweb.org/articles?id=10.1257/jel.20251636)

生成摘要时出错

---

## 70. Taylor Otwell: What 14 Years of Laravel Taught Me About Maintainability

**原文标题**: Taylor Otwell: What 14 Years of Laravel Taught Me About Maintainability

**原文链接**: [https://maintainable.fm/episodes/taylor-otwell-what-14-years-of-laravel-taught-me-about-maintainability](https://maintainable.fm/episodes/taylor-otwell-what-14-years-of-laravel-taught-me-about-maintainability)

生成摘要时出错

---

## 71. University of Cambridge Cognitive Ability Test

**原文标题**: University of Cambridge Cognitive Ability Test

**原文链接**: [https://planning.e-psychometrics.com/test/icar60](https://planning.e-psychometrics.com/test/icar60)

生成摘要时出错

---

## 72. Lucky 13: a look at Debian trixie

**原文标题**: Lucky 13: a look at Debian trixie

**原文链接**: [https://lwn.net/Articles/1033474/](https://lwn.net/Articles/1033474/)

生成摘要时出错

---

## 73. FBI cyber cop: Salt Typhoon pwned 'nearly every American'

**原文标题**: FBI cyber cop: Salt Typhoon pwned 'nearly every American'

**原文链接**: [https://www.theregister.com/2025/08/28/fbi_cyber_cop_salt_typhoon/](https://www.theregister.com/2025/08/28/fbi_cyber_cop_salt_typhoon/)

生成摘要时出错

---

## 74. Trying to get error backtraces in Rust libraries right

**原文标题**: Trying to get error backtraces in Rust libraries right

**原文链接**: [https://www.iroh.computer/blog/error-handling-in-iroh](https://www.iroh.computer/blog/error-handling-in-iroh)

生成摘要时出错

---

## 75. Make any site multiplayer in a few lines. Serverless WebRTC matchmaking

**原文标题**: Make any site multiplayer in a few lines. Serverless WebRTC matchmaking

**原文链接**: [https://oxism.com/trystero/](https://oxism.com/trystero/)

生成摘要时出错

---

## 76. Flunking my Anthropic interview again

**原文标题**: Flunking my Anthropic interview again

**原文链接**: [https://taylor.town/flunking-anthropic](https://taylor.town/flunking-anthropic)

生成摘要时出错

---

## 77. God created the real numbers

**原文标题**: God created the real numbers

**原文链接**: [https://www.ethanheilman.com/x/34/index.html](https://www.ethanheilman.com/x/34/index.html)

生成摘要时出错

---

## 78. The Rise of Hybrid PHP: Blending PHP with Go and Rust

**原文标题**: The Rise of Hybrid PHP: Blending PHP with Go and Rust

**原文链接**: [https://yekdeveloper.com/p/4-the-rise-of-hybrid-php](https://yekdeveloper.com/p/4-the-rise-of-hybrid-php)

生成摘要时出错

---

## 79. John Carmack's arguments against building a custom XR OS at Meta

**原文标题**: John Carmack's arguments against building a custom XR OS at Meta

**原文链接**: [https://twitter.com/ID_AA_Carmack/status/1961172409920491849](https://twitter.com/ID_AA_Carmack/status/1961172409920491849)

生成摘要时出错

---

## 80. Internet Relay Chat

**原文标题**: Internet Relay Chat

**原文链接**: [https://www.youtube.com/watch?v=6UbKenFipjo](https://www.youtube.com/watch?v=6UbKenFipjo)

生成摘要时出错

---

## 81. Josef Bacik Leaving Meta and Stepping Back from Kernel Development

**原文标题**: Josef Bacik Leaving Meta and Stepping Back from Kernel Development

**原文链接**: [https://www.phoronix.com/news/Josef-Bacik-Leaves-Meta](https://www.phoronix.com/news/Josef-Bacik-Leaves-Meta)

生成摘要时出错

---

## 82. Affiliates flock to scam gambling machine

**原文标题**: Affiliates flock to scam gambling machine

**原文链接**: [https://krebsonsecurity.com/2025/08/affiliates-flock-to-soulless-scam-gambling-machine/](https://krebsonsecurity.com/2025/08/affiliates-flock-to-soulless-scam-gambling-machine/)

生成摘要时出错

---

## 83. From multi-head to latent attention: The evolution of attention mechanisms

**原文标题**: From multi-head to latent attention: The evolution of attention mechanisms

**原文链接**: [https://vinithavn.medium.com/from-multi-head-to-latent-attention-the-evolution-of-attention-mechanisms-64e3c0505f24](https://vinithavn.medium.com/from-multi-head-to-latent-attention-the-evolution-of-attention-mechanisms-64e3c0505f24)

生成摘要时出错

---

## 84. Enrollment at trade schools is expected to grow

**原文标题**: Enrollment at trade schools is expected to grow

**原文链接**: [https://finance.yahoo.com/news/ai-cant-install-an-hvac-system-why-gen-z-is-flocking-to-jobs-in-the-trades-171735856.html](https://finance.yahoo.com/news/ai-cant-install-an-hvac-system-why-gen-z-is-flocking-to-jobs-in-the-trades-171735856.html)

生成摘要时出错

---

## 85. Show HN: I made an Animal Crossing style letter editor

**原文标题**: Show HN: I made an Animal Crossing style letter editor

**原文链接**: [https://acmail.idreesinc.com](https://acmail.idreesinc.com)

生成摘要时出错

---

## 86. Show HN: Sosumi.ai – Convert Apple Developer docs to AI-readable Markdown

**原文标题**: Show HN: Sosumi.ai – Convert Apple Developer docs to AI-readable Markdown

**原文链接**: [https://sosumi.ai/](https://sosumi.ai/)

生成摘要时出错

---

## 87. Open Source is one person

**原文标题**: Open Source is one person

**原文链接**: [https://opensourcesecurity.io/2025/08-oss-one-person/](https://opensourcesecurity.io/2025/08-oss-one-person/)

生成摘要时出错

---

## 88. Why Romania excels in international Olympiads

**原文标题**: Why Romania excels in international Olympiads

**原文链接**: [https://www.palladiummag.com/2025/08/29/why-romania-excels-in-international-olympiads/](https://www.palladiummag.com/2025/08/29/why-romania-excels-in-international-olympiads/)

生成摘要时出错

---

## 89. AI coding made me faster, but I can't code to music anymore

**原文标题**: AI coding made me faster, but I can't code to music anymore

**原文链接**: [https://www.praf.me/ai-coding](https://www.praf.me/ai-coding)

生成摘要时出错

---

## 90. My Failures Onboarding at Splunk

**原文标题**: My Failures Onboarding at Splunk

**原文链接**: [https://people-work.io/blog/my-failures-onboarding-at-splunk/](https://people-work.io/blog/my-failures-onboarding-at-splunk/)

生成摘要时出错

---

## 91. The Space Shuttle Columbia disaster and the over-reliance on PowerPoint (2019)

**原文标题**: The Space Shuttle Columbia disaster and the over-reliance on PowerPoint (2019)

**原文链接**: [https://mcdreeamiemusings.com/blog/2019/4/13/gsux1h6bnt8lqjd7w2t2mtvfg81uhx](https://mcdreeamiemusings.com/blog/2019/4/13/gsux1h6bnt8lqjd7w2t2mtvfg81uhx)

生成摘要时出错

---

## 92. Lisp from Nothing, Second Edition

**原文标题**: Lisp from Nothing, Second Edition

**原文链接**: [http://t3x.org/lfn/index.html](http://t3x.org/lfn/index.html)

生成摘要时出错

---

## 93. Just use `git` to manage your dotfiles

**原文标题**: Just use `git` to manage your dotfiles

**原文链接**: [https://ericgreer.info/post/2025-08-31-simple-dotfiles-script/](https://ericgreer.info/post/2025-08-31-simple-dotfiles-script/)

生成摘要时出错

---

## 94. De minimis exemption ends

**原文标题**: De minimis exemption ends

**原文链接**: [https://www.washingtonpost.com/business/2025/08/30/de-minimis-tax-canceled-orders-delays/](https://www.washingtonpost.com/business/2025/08/30/de-minimis-tax-canceled-orders-delays/)

生成摘要时出错

---

## 95. Some users have noticed settings that let Meta analyze and retain phone photos

**原文标题**: Some users have noticed settings that let Meta analyze and retain phone photos

**原文链接**: [https://www.zdnet.com/article/meta-might-be-secretly-scanning-your-phones-camera-roll-how-to-check-and-turn-it-off/](https://www.zdnet.com/article/meta-might-be-secretly-scanning-your-phones-camera-roll-how-to-check-and-turn-it-off/)

生成摘要时出错

---

## 96. Tinyrenderer second edition: software rendering in 500 lines of bare C++

**原文标题**: Tinyrenderer second edition: software rendering in 500 lines of bare C++

**原文链接**: [https://haqr.eu/tinyrenderer/](https://haqr.eu/tinyrenderer/)

生成摘要时出错

---

## 97. How did .agakhan, .ismaili and .imamat get their own TLDs?

**原文标题**: How did .agakhan, .ismaili and .imamat get their own TLDs?

**原文链接**: [https://data.iana.org/TLD/tlds-alpha-by-domain.txt](https://data.iana.org/TLD/tlds-alpha-by-domain.txt)

生成摘要时出错

---

## 98. Git Diagramming "The Weave"

**原文标题**: Git Diagramming "The Weave"

**原文链接**: [https://daverupert.com/2025/08/git-diagramming-the-weave/](https://daverupert.com/2025/08/git-diagramming-the-weave/)

生成摘要时出错

---

## 99. Why did dlclose not unload the library? (2023)

**原文标题**: Why did dlclose not unload the library? (2023)

**原文链接**: [https://kishoreganesh.com/post/why-dl-close-did-not-work/](https://kishoreganesh.com/post/why-dl-close-did-not-work/)

生成摘要时出错

---

## 100. A convex polyhedron without Rupert's property

**原文标题**: A convex polyhedron without Rupert's property

**原文链接**: [https://arxiv.org/abs/2508.18475](https://arxiv.org/abs/2508.18475)

生成摘要时出错

---

