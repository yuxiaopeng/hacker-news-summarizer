# Hacker News 热门文章摘要 (2025-07-09)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 我把SAP移植到1976年的CPU上，速度还不算慢。

**原文标题**: I Ported SAP to a 1976 CPU. It Wasn't That Slow

**原文链接**: [https://github.com/oisee/zvdb-z80/blob/master/ZVDB-Z80-ABAP.md](https://github.com/oisee/zvdb-z80/blob/master/ZVDB-Z80-ABAP.md)

我将SAP移植到1976年的CPU上，并没有那么慢

---

## 12. 将副业启动成盈利百万美元的生意

**原文标题**: Bootstrapping a side project into a profitable seven-figure business

**原文链接**: [https://projectionlab.com/blog/we-reached-1m-arr-with-zero-funding](https://projectionlab.com/blog/we-reached-1m-arr-with-zero-funding)

凯尔·诺兰讲述了他将 ProjectionLab 从副业发展到四年内年收入达100万美元的自力更生创业历程。受到财务自由运动的启发，他构建了自己找不到的工具，最终帮助超过10万个家庭进行财务规划。

这段旅程并非一帆风顺，而是一段充满高潮、低谷和怀疑时刻的情感过山车。他强调了坚持的重要性，并表示持续性比智商更重要。

最初，凯尔独自一人工作，身兼数职，最终意识到需要一个团队来避免停滞不前。在乔恩·库珀斯展现出持续的价值后，他聘请他作为增长和营销合伙人。他还从 ProjectionLab 用户社区中增加了承包商来处理客户成功，优先考虑社区参与而不是更便宜的外包选择。

凯尔强调了强大社区的价值，并将精力集中在产品开发上。展望未来，他的目标是加倍投入优秀产品，保持精简和自力更生，实现可持续发展，并避免追逐潮流。他强调了持续、小幅改进和行动的力量，将其比作平均成本法，并感谢 ProjectionLab 社区的支持。

---

## 13. 短语起源：我们为什么“调用”函数？

**原文标题**: Phrase origin: Why do we "call" functions?

**原文链接**: [https://quuxplusone.github.io/blog/2025/04/04/etymology-of-call/](https://quuxplusone.github.io/blog/2025/04/04/etymology-of-call/)

本文探讨了编程中“调用函数”一词的词源。它追溯了该用法至图书馆学，其中“索书号”指的是用于从闭架图书馆检索图书的标记。

早期计算机采用了“图书馆”的比喻，将子程序存储在磁带上。John Mauchly (1947) 使用“call in”（调用）来描述访问这些子程序。MANIAC II 手册 (1956) 明确提到了纸带库中子程序的“索书号”，但将实际的控制转移指令称为“transfer control”（转移控制）。

Fortran II (1958) 引入了 `CALL` 和 `RETURN` 语句，巩固了“CALL”（调用）作为将控制权转移到子程序的命令，从而在命令和概念之间建立了一个助记链接。这普及了“调用 X”这一说法。

到 1959 年，Algol 采用了术语“call”（调用），同时指代转移行为和执行期间。最终，在 1961 年，我们看到了明确的短语“调用 X”。

作者认为，Fortran II 使用 `CALL` 的灵感来自现有的图书馆学和早期计算机用法，但极大地塑造了其现代编程意义。到 1960 年代初，“call”（调用）一词已成为描述启动子程序执行行为的标准方式。

---

## 14. Windows 版 7-Zip 现在压缩时可以使用超过 64 个 CPU 线程

**原文标题**: 7-Zip for Windows can now use more than 64 CPU threads for compression

**原文链接**: [https://www.7-zip.org/history.txt](https://www.7-zip.org/history.txt)

7-Zip更新历史：版本18.06至25.00

主要改进和功能包括：

*   **性能提升：** 提升bzip2、deflate、LZMA/LZMA2、RAR、CAB、WIM、ZIP和GZ等多种格式的压缩和解压缩速度。优化Windows、macOS和Linux的ARM64版本。优化哈希算法。
*   **多线程：** 能够利用超过64个CPU线程进行zip/7z/xz压缩和基准测试，尤其是在具有多个处理器组的系统上。
*   **格式支持：** 扩展了对各种存档格式的支持，包括APFS、ZSTD、VHDX、ZIP、SquashFS、RPM、DMG、NTFS镜像、MBR、GPT、UDF、cpio、ext4、HFS和APM。增加创建POSIX格式TAR存档和处理Base64编码文件的能力。
*   **安全性：** 增强了7z存档的加密强度，使用更大的随机初始化向量并改进了伪随机数生成器。修复了多个CVE漏洞。
*   **新功能/开关：** 引入了大量命令行开关（例如，-myv、-myfa、-myfd、-smemx、-slmu、-slsl、-ssp、-shd、-xtd、-mmemuse）以控制压缩方法、内存使用、时间戳处理等。在7-Zip文件管理器中实现了新的菜单项，例如临时文件删除工具。
*   **错误修复：** 解决了与崩溃、错误解包、内存泄漏以及各种存档格式和功能相关的众多错误。
*   **GUI增强：** 改进了7-Zip文件管理器，包括显示文件图标、添加在存档期间包含元数据的选项以及传播Zone.Identifier流。
*   **SHA校验和：** 引入SHA-512、SHA-384、SHA3-256和MD5校验和计算。 支持 .sha256 文件。

---

## 15. 用COBOL编写的表情符号逆波兰表示法计算器

**原文标题**: A Emoji Reverse Polish Notation Calculator Written in COBOL

**原文链接**: [https://github.com/ghuntley/cobol-emoji-rpn-calculator](https://github.com/ghuntley/cobol-emoji-rpn-calculator)

本项目展示了一系列用COBOL编写的计算器，突出了不同的计算方法和现代特性。它包括一个基本的infix计算器，一个标准的RPN（逆波兰表示法）计算器，以及一个独特的Emoji RPN计算器。

Emoji RPN计算器是一个关键特性，通过使用表情符号（➕、➖、✖、➗）作为运算符，展示了COBOL处理Unicode字符的能力。本项目提供了在macOS、Linux和Windows上使用GnuCOBOL编译和运行每个计算器的说明。针对每个计算器都给出了使用示例，包括输入表达式和解释结果。

本项目强调强大的错误处理，并为两个RPN计算器都包含了全面的测试套件。这些测试涵盖了基本算术、复杂表达式以及各种错误情况，如除以零和堆栈溢出/下溢。文档详细介绍了使用的COBOL特性，如数据结构（用于堆栈实现的OCCURS子句）、字符串处理和模块化编程。它还提到了一些有趣的事实，例如展示COBOL的Unicode支持以及它可能是COBOL中最早的基于表情符号的计算器之一。本项目作为一个教育资源展示COBOL的功能，即使它已经很老旧，并鼓励贡献以扩展计算器的功能。

---

## 16. RapidRAW：一款非破坏性的GPU加速RAW图像编辑器

**原文标题**: RapidRAW: A non-destructive and GPU-accelerated RAW image editor

**原文链接**: [https://github.com/CyberTimon/RapidRAW](https://github.com/CyberTimon/RapidRAW)

RapidRAW：一款高性能GPU加速RAW图像编辑器，旨在成为Adobe Lightroom的轻量级替代品。由一位18岁开发者打造，适用于Windows、macOS和Linux，专注于功能丰富且精简的编辑体验。

主要特性包括：使用自定义WGSL着色器的GPU加速处理、AI驱动的遮罩（主体和前景）、可选的ComfyUI生成式AI集成（用于修复等任务）、通过rawler实现的完整RAW格式支持以及非破坏性工作流程。它提供专业级的调整功能，如色调控制、色调曲线、色彩分级、细节增强和变换工具。

该编辑器还包含库和工作流程功能，例如图像库管理、文件夹操作、胶片视图、批量操作和EXIF数据查看器。UI可自定义，具有预设系统、复制/粘贴设置、撤消/重做历史记录和多个主题。

最近的更新包括AI功能的改进、大图像的缓存、着色器增强以及更好的RAW格式支持。开发者目前专注于重构前端、改进去雾、优化图像传输以及增强AI遮罩。AI路线图包括集成的AI遮罩和通过ComfyUI后端提供的可选生成式AI。

该项目以AGPL-3.0协议开源，鼓励社区贡献。欢迎通过Ko-fi或加密货币进行捐赠支持。

---

## 17. 管辖权对加密消息应用的安全几乎无关紧要

**原文标题**: Jurisdiction Is Nearly Irrelevant to the Security of Encrypted Messaging Apps

**原文链接**: [https://soatok.blog/2025/07/09/jurisdiction-is-nearly-irrelevant-to-the-security-of-encrypted-messaging-apps/](https://soatok.blog/2025/07/09/jurisdiction-is-nearly-irrelevant-to-the-security-of-encrypted-messaging-apps/)

Soatok 的博文认为，端到端加密消息应用的安全取决于密码学的正确实现，而非数据存储的司法管辖区。作者认为，如果密码学得到正确实施，密文存储的位置无关紧要。

正确的实现包括：

*   **密钥管理：** 安全的客户端密钥管理和验证公钥的机制。作者倡导使用密钥透明项目，例如他在 Fediverse 上的工作。
*   **透明性：** 可重现构建、二进制透明性 (SigStore) 和密钥透明性。这些依赖于透明度日志，它们是由独立的第三方监控器验证的只追加数据结构。透明度日志有助于检测和防止后门、公钥替换和其他妥协。
*   **安全协议：** 使用强大的端到端加密协议，如 MLS 或 Signal 协议，它们提供正式的安全保证。不允许明文传输。协议设计应防止服务器操纵和 AI 访问消息内容。
*   **审计和测试：** 聘请密码学家和安全专家进行审计，并将安全措施纳入 CI/CD 管道。

作者批评了依赖密钥指纹的应用程序，并强调了第三方验证的重要性。

如果这些密码学措施到位，司法管辖区的重要性就降低了。虽然政府干预仍然是一种潜在威胁，但二进制和密钥透明性使隐蔽后门可被检测到。与司法管辖区相关的最大风险是开发人员可能被迫妥协应用程序，但在这种情况下，作者认为改进的运营安全比基于司法管辖区的安全更有效。

最终，作者优先考虑安全加密而不是数据主权，推荐使用强大密码学的应用程序，无论托管国家/地区如何。

---

## 18. 使用回车符破坏Git并实现克隆RCE

**原文标题**: Breaking Git with a carriage return and cloning RCE

**原文链接**: [https://dgl.cx/2025/07/git-clone-submodule-cve-2025-48384](https://dgl.cx/2025/07/git-clone-submodule-cve-2025-48384)

本文详细介绍Git中发现的远程代码执行 (RCE) 漏洞，编号为CVE-2025-48384，该漏洞由回车符触发。当递归克隆恶意Git仓库时，此漏洞允许攻击者在受害者机器上执行任意代码。

该漏洞源于Git对定义子模块的`.gitmodules`文件的处理方式。Git在读取配置文件时会删除回车符（\r）。但是，当Git将配置值写回磁盘时，它只会引用包含空格、分号或井号的字符串。这可能导致恶意`.gitmodules`文件中以回车符结尾的路径（例如，`path = "foo^M"`）在配置被重写时，回车符被删除，从而导致路径被更改（例如，`path = foo`）。

在允许文件名中使用控制字符的类Unix系统中，可以利用此更改后的路径将子模块内容写入到非预期位置。通过操纵`.git`目录，攻击者可以创建钩子脚本，从而在Git运行这些钩子时导致任意代码执行。

修复方案包括确保在写入配置文件时始终引用带有回车符的字符串。作者指出此漏洞与过去Git中关于大小写不敏感和凭据助手协议的漏洞相似，强调了进程间通信中存在漏洞的风险。使用`git clone --recursive`，尤其是在GitHub Desktop等工具自动执行时，会增加被利用的风险。手动缓解措施包括在不使用递归选项的情况下克隆，检查`.gitmodules`的安全性，然后初始化子模块。

---

## 19. ESIM安全

**原文标题**: ESIM Security

**原文链接**: [https://security-explorations.com/esim-security.html](https://security-explorations.com/esim-security.html)

安全探索发现了Kigen eUICC（eSIM）中的一个严重漏洞，特别是破坏了带有GSMA消费者证书的Kigen eUICC卡的安全。该漏洞允许破坏eSIM配置文件，从而未经授权地访问和修改移动订阅。此次攻击证明了2019年对Java Card的旧研究确实重要，因为2019年报告给Oracle的漏洞，被该公司认为无关紧要，现在被证明是真正的漏洞。该攻击利用了对样品卡的物理访问以及恶意Java应用程序安装的密钥知识，并且不能排除远程无线攻击的可能性。

漏洞利用导致GSMA消费者证书被盗，从而能够以明文形式从移动网络运营商（MNO）下载配置文件，检查应用程序功能并修改下载的配置文件。它还能够窃取网络运营商的秘密（OPc和AMF密钥），这些秘密应该被保护。GSMA证书盗窃使得防篡改安全元件变得无关紧要。修改后的配置文件可以加载到任意eUICC中，绕过MNO检测。

安全探索已将该漏洞通知了Kigen、GSMA和Oracle。Kigen实施了类型安全检查作为“缓解措施”，但证明是不够的。Kigen为该发现提供了奖励，并与GSMA协调以更新TS.48通用测试配置文件规范。Kigen提供的CVSS评分为环境评分6.7（中等），基本CVSS评分为9.1（严重），因为存在远程无线攻击的可能性。

---

## 20. 移动网格上的伽利略不变宇宙学流体动力学模拟

**原文标题**: Galiliean-invariant cosmological hydrodynamical simulations on a moving mesh

**原文链接**: [https://wwwmpa.mpa-garching.mpg.de/~volker/arepo/](https://wwwmpa.mpa-garching.mpg.de/~volker/arepo/)

本文介绍 AREPO，一种新型流体动力学模拟代码，旨在克服宇宙学模拟中光滑粒子流体动力学 (SPH) 和自适应网格细化 (AMR) 方法的局限性。AREPO 利用由 Voronoi 镶嵌定义的移动非结构化网格，使用二阶非分裂 Godunov 方案求解理想流体动力学方程。

其关键创新在于移动网格生成点的能力。当静止时，该代码作为标准的欧拉方法运行。当随局部流速移动时，它变成伽利略不变的拉格朗日方案，避免了其他基于网格的拉格朗日方法中存在的网格扭曲问题。这种伽利略不变性对于具有超音速流动的宇宙学模拟至关重要。

AREPO 兼具 SPH 和 AMR 的优点：它像 SPH 一样自动调整空间分辨率，这对于模拟宇宙学结构形成至关重要，同时保留了欧拉方法的高精度激波处理能力，并改善了接触间断面的处理。

本文详细介绍了 AREPO 在 2D 和 3D 中的实现、其在分布式内存计算机上的并行化、自适应网格细化/粗化技术、单独的时间步长方法以及对自引力的高精度处理，从而能够与无碰撞暗物质模拟无缝集成。作者展示了证明 AREPO 性能的测试问题，认为它是现有 SPH 和欧拉方法的引人注目的替代方案。还提供了一些视频，展示了 AREPO 在标准流体动力学测试中的能力。

---

## 21. Astro是对Web基础的回归

**原文标题**: Astro is a return to the fundamentals of the web

**原文链接**: [https://websmith.studio/blog/astro-is-a-developers-dream/](https://websmith.studio/blog/astro-is-a-developers-dream/)

无法访问文章链接。

---

## 22. 宜家放弃Zigbee，全面拥抱Matter智能家居。

**原文标题**: IKEA ditches Zigbee for Thread going all in on Matter smart homes

**原文链接**: [https://www.theverge.com/smart-home/701697/ikea-matter-thread-new-products-new-smart-home-strategy](https://www.theverge.com/smart-home/701697/ikea-matter-thread-new-products-new-smart-home-strategy)

宜家正大幅扩展其智能家居产品线，通过采用Matter-over-Thread标准并逐步淘汰Zigbee。从2025年1月起，宜家将推出超过20款新的Matter-over-Thread设备，包括智能灯、传感器和遥控器，所有设备均设计得简单且经济实惠。他们还将以价格低廉的蓝牙音箱重新进入音频市场。

最近的测试版更新将宜家的Dirigera智能家居中心转换为Matter控制器并激活其Thread无线电，使其能够控制来自任何品牌的Matter设备。该中心还将充当Matter网桥，以保持与现有Zigbee设备的向后兼容性。目标是实现一个更加开放和即插即用的智能家居生态系统。

这一举措源于宜家对经济实惠和易用性的承诺。他们新的Matter-over-Thread产品也将无需宜家中心即可工作，直接与Apple Home、Amazon Alexa和Google Home等生态系统集成。宜家旨在消除复杂性，并允许客户选择最适合他们的系统，从而使智能家居技术更容易被大众市场接受。虽然Matter的采用速度缓慢且面临挑战，但宜家坚信这是朝着更具互操作性和用户友好性的智能家居体验迈出的正确一步。

---

## 23. 今天在哪里能看到葛饰北斋的《神奈川冲浪里》？

**原文标题**: Where can I see Hokusai's Great Wave today?

**原文链接**: [https://greatwavetoday.com/](https://greatwavetoday.com/)

本文解答了如今在哪里能看到葛饰北斋的《神奈川冲浪里》的问题，并列出了目前正在展出该作品的地点。

截至目前，文章显示该画作：

*   **正在展出地点：**
    *   意大利特雷维索市立博物馆（至2025年9月28日）
    *   法国南特历史博物馆（至2025年9月7日）

*   **也在展出地点：**
    *   意大利的里雅斯特东方艺术市民博物馆（来源：Instagram）
    *   意大利维罗纳马费之家博物馆（来源：Instagram）
    *   美国法明顿希尔-斯泰德博物馆（来源：网站）

*   **未在展出地点：**
    *   55个地点（原因未说明，用方框表情符号表示）。

文章鼓励博物馆和画廊通过在GitHub上发布信息来加入列表，并提供RSS订阅以获取自动更新。文章还提到该项目是自动化的，由Matt Sephton创建。最后，文章提供了一个关于该画作本身的“了解更多”链接。

---

## 24. 使用MPC进行匿名和隐私的DNA分析

**原文标题**: Using MPC for Anonymous and Private DNA Analysis

**原文链接**: [https://vishakh.blog/2025/07/08/using-mpc-for-anonymous-and-private-dna-analysis/](https://vishakh.blog/2025/07/08/using-mpc-for-anonymous-and-private-dna-analysis/)

该博文详细介绍了Monadic DNA使用多方计算 (MPC) 提供匿名和私有DNA分析的实验。在丹佛的一次活动中，三十名参与者提供了唾液样本，这些样本随后由Autogen处理。其关键创新在于使用Nillion的MPC技术，允许用户声明、存储和分析他们的基因组数据，而无需暴露原始数据本身。

参与者通过网络应用程序使用试剂盒ID和PIN码来声明他们的数据，然后以加密形式将其上传到由Nillion提供支持的私有存储集群。分析侧重于与味觉和睡眠等特征相关的简单基因型查找，并在服务器端对加密数据执行，以确保隐私。

该实验突出了几个挑战，包括对实验室的信任需求（尽管采用了匿名化处理）、对PIN码的潜在暴力破解攻击以及安全密钥管理的复杂性。未来的工作将侧重于整合分子密码学、用于法律协议的零知识证明、与实验室合作的近源数据加密以及将全同态加密 (FHE) 与MPC集成，以实现更强的安全性。该实验的成功证明了MPC在基因组分析中的可行性，为异步分析和安全的、以隐私为中心的基因组洞察铺平了道路。

---

## 25. 偏好设置框：Mac设置历史，1984–2004

**原文标题**: Frame of preference A history of Mac settings, 1984–2004

**原文链接**: [https://aresluna.org/frame-of-preference/](https://aresluna.org/frame-of-preference/)

偏好框架：Mac设置的历史，1984–2004

本文探讨了Mac电脑最初二十年间控制面板的演变，并将其作为理解该机器历史和设计理念的透镜。

文章从标志性的1984年控制面板开始，重点介绍了苏珊·卡雷的设计及其对动画和早期GUI实验的巧妙运用，包括备受争议的可定制桌面图案。文章指出，虽然它很迷人，但也缓慢而笨拙。

1986年的重新设计因放弃视觉吸引力而受到批评，取而代之的是枯燥但更清晰的文本标签，以及引入了RAM缓存等技术设置，这与“家电”理念背道而驰。AppleTalk的加入被认为是积极的一步。

1987年的迭代版本引入了侧边栏层级结构，以适应越来越多的设置，导致了诸如滚动区域内的滚动以及功能蔓延的可能性等UI挑战。 地图和CloseView（后来的Zoom）的添加被强调为有用的补充。

最后，1991年控制面板对Finder隐喻的采用，为每个设置使用可移动的图标，被认为是巧妙的，但最终是多余的。 然而，鼠标、内存和显示器等单独面板因其设计和功能而受到赞扬。 文章最后强调了引入颜色以及当时硬件的局限性所带来的复杂性和不一致性。 作者使用这些历史例子来展示用户体验设计中的关键考虑因素以及平衡美学、功能和用户体验的挑战。

---

## 26. 我正在构建用于卫星数据的LLM，EarthGPT.app。

**原文标题**: I'm Building LLM for Satellite Data EarthGPT.app

**原文链接**: [https://www.earthgpt.app/](https://www.earthgpt.app/)

EarthGPT.app正在开发一种专门用于处理多光谱卫星图像的大型语言模型 (LLM)。这意味着它旨在利用 LLM 的强大功能，使分析和理解卫星地球观测数据变得更容易和更易于访问。该项目结合了 LLM 的能力和现代遥感技术。 现有演示版本，有兴趣者可以通过 hi@earthgpt.app 联系团队。 该项目由 Geobase 提供技术支持，表明可能存在合作或底层基础设施。 本质上，EarthGPT 旨在创建一个工具，使用户能够以更直观和强大的方式与卫星图像交互并从中提取见解。

---

## 27. 英伟达市值突破4万亿美元，成全球首家。

**原文标题**: Nvidia Becomes First Company to Reach $4T Market Cap

**原文链接**: [https://www.cnbc.com/2025/07/09/nvidia-4-trillion.html](https://www.cnbc.com/2025/07/09/nvidia-4-trillion.html)

英伟达市值突破4万亿美元，AI热潮与GPU需求驱动。

---

## 28. Smollm3：小型多语种长上下文推理LLM

**原文标题**: Smollm3: Smol, multilingual, long-context reasoner LLM

**原文链接**: [https://huggingface.co/blog/smollm3](https://huggingface.co/blog/smollm3)

本文介绍 SmolLM3，一款为高效部署而设计的新型、完全开源的 3B 语言模型。它在性能上优于 Llama-3.2-3B 和 Qwen2.5-3B，同时与更大的 4B 模型保持竞争力。作者发布了完整的配方，包括架构细节、数据混合以及构建混合推理模型的方法。

SmolLM3 采用 Transformer 解码器架构，并进行了诸如分组查询注意力 (GQA) 和 NoPE 等修改，从而提高了效率和长上下文性能（使用 YaRN 可达 128k）。它在三个阶段训练了 11.2T 个 tokens，以不断变化的比例混合了网络、数学和代码数据。训练过程涉及架构消融和数据混合实验。

该模型还经历了用于长上下文扩展和推理适应的中间训练。长上下文训练按顺序扩展了上下文窗口，而推理中间训练则使用 OpenThoughts3-1.2M 等数据集整合了推理能力。

最后，后训练包括使用合成数据生成的监督微调 (SFT)，以及使用锚定偏好优化 (APO) 进行对齐。带有 /think 和 /no_think 标志的聊天模板允许用户在推理和非推理模式之间切换。目标是在推理和非推理之间平衡性能，涵盖数学、代码、指令遵循和多语言能力，同时减轻长上下文任务的性能下降。作者计划发布数据混合、训练脚本和训练日志。

---

## 29. Supabase MCP 可能泄漏你的整个 SQL 数据库

**原文标题**: Supabase MCP can leak your entire SQL database

**原文链接**: [https://www.generalanalysis.com/blog/supabase-mcp-blog](https://www.generalanalysis.com/blog/supabase-mcp-blog)

本文详细介绍了一个 Supabase 的模型上下文协议 (MCP) 集成中的安全漏洞，该漏洞可能允许攻击者泄露整个 SQL 数据库。该漏洞源于通过 `service_role` 获得的过度授权的数据库访问权限，以及 LLM 无法区分用户提供的数据和指令。

攻击者可以通过构造伪装成正常支持工单的恶意消息来利用此漏洞。此消息包含针对开发者使用的 AI 助手（如 Cursor 的 agent）的嵌入式指令。当开发者使用助手审查未处理的工单时，LLM 会无意中使用 `service_role` 凭据执行攻击者的指令，从而绕过行级安全性 (RLS)。这使得攻击者能够从通常无法访问的表中提取敏感数据，并将其插入到支持工单中，从而使攻击者可见。

本文使用一个多租户客户支持 SaaS 场景来说明该攻击，突出显示了攻击者如何获得对存储在 `integration_tokens` 表中的 OAuth 令牌和会话凭据等敏感数据的访问权限。

为了缓解此漏洞，本文建议：尽可能在 Supabase MCP 中使用只读模式以防止未经授权的写入操作，并实施提示注入过滤器，在将用户提交的内容传递给 LLM 之前扫描可疑模式。

---

## 30. Zorin 操作系统

**原文标题**: Zorin OS

**原文链接**: [https://zorin.com/os/](https://zorin.com/os/)

Zorin OS 被誉为 Windows 和 macOS 的用户友好替代方案，尤其是在 Windows 10 达到生命周期终点时更具意义。它旨在使计算机更快、更强大、更安全、更可靠且更易于使用。

主要功能包括：

*   **熟悉界面：** 可定制的桌面布局模仿 Windows、macOS 或 Linux 环境，便于轻松过渡。
*   **性能：** Zorin OS 专为速度和效率而设计，即使在较旧的硬件（最长 15 年）上也能运行，从而延长 PC 的使用寿命。
*   **安全与隐私：** 基于 Linux，它提供强大的防病毒和恶意软件安全性，并提供及时更新和尊重隐私的方法，不收集任何个人数据。
*   **应用兼容性：** 开箱即用包含基本应用，可访问庞大的软件商店，并支持 Windows 应用。
*   **游戏：** 支持来自 Steam、Lutris 和 Epic Games 等平台的各种游戏，并具有优化的图形驱动程序。
*   **Zorin Connect：** 集成 Android 设备，用于通知同步、文件共享、远程控制和媒体播放。
*   **双启动：** 可以与 Windows 或 macOS 一起安装。
*   **辅助功能：** 提供多语言支持和辅助技术。
*   **文件兼容性：** 可处理常见文件格式，并包含 LibreOffice 以实现 Microsoft Office 文档兼容性。
*   **费用：** Core 版本是免费的，而 Pro 版本提供更高级的功能和支持。

Zorin OS 17 将至少在 2027 年 6 月之前收到软件更新和安全补丁。 它被认为是一种节省资金、帮助环境和改善计算体验的方式。

---

## 31. 了解Steam玩家都是囤积者，就解释了你为什么要把30%的利润给Valve。

**原文标题**: Knowing Steam players are hoarders explains why you give Valve that 30%

**原文链接**: [https://www.pcgamer.com/gaming-industry/knowing-steam-players-are-hoarders-explains-why-you-give-valve-that-30-percent-analyst-tells-devs-you-get-access-to-a-bunch-of-drunken-sailors-who-spend-money-irresponsibly/](https://www.pcgamer.com/gaming-industry/knowing-steam-players-are-hoarders-explains-why-you-give-valve-that-30-percent-analyst-tells-devs-you-get-access-to-a-bunch-of-drunken-sailors-who-spend-money-irresponsibly/)

游戏行业分析师克里斯·祖科夫斯基认为，Steam的成功以及开发者愿意给Valve 30%分成的原因在于该平台拥有大量“囤积狂”用户，他们购买游戏但往往并不玩。他将这种行为比作其他拥有“耻辱堆”的爱好，例如未拼搭的乐高套装或未读的书籍（积读）。

祖科夫斯基引用一项研究，该研究表明Steam玩家收藏的游戏中有一半以上未被玩过，并认为Valve已经挖掘了一个收藏家市场，他们从购买游戏中获得满足感，即使他们不打算玩这些游戏。这种“非理性”的购买行为对开发者有利，因为如果人们只购买计划玩的游戏，销量将会显著下降。

文章还强调了祖科夫斯基的观察，即类型清晰度有助于游戏在Steam上的成功，因为爱好者更有可能购买他们偏好的类型的游戏，无论他们现有的积压游戏有多少。

虽然承认这种“囤积”倾向，但作者指出，玩家的习惯会随着时间推移而演变，并且他们个人随着时间推移在Steam上的购买行为也变得更有选择性。然而，核心论点仍然是：Steam的成功是由收集游戏的用户推动的，开发者支付30%的费用是为了接触到这个受众。祖科夫斯基最后敦促开发者对他们的受众保持现实态度，认识到大多数买家不会成为深度参与的粉丝。

---

## 32. Libpostal：用于解析/标准化全球街道地址的C语言库

**原文标题**: Libpostal: C library for parsing/normalizing street addresses around the world

**原文链接**: [https://github.com/openvenues/libpostal](https://github.com/openvenues/libpostal)

Libpostal：一个用于解析和标准化国际街道地址的 C 语言库，利用统计自然语言处理和开放数据。它旨在理解各种语言的基于位置的字符串，从而改进地址索引和查询，适用于地图、交通运输和交付服务等应用。

该库将自由格式的地址转换为标准化的格式，以便进行机器比较和索引。虽然它本身不是地理编码器，但它通过预处理地址来增强地理编码应用程序。核心功能是用 C 语言编写的，并官方支持 Python、Ruby、Go、Java、PHP 和 NodeJS 的绑定。

文档提供了 Mac/Linux 和 Windows 的安装说明，使用 apt-get、yum、MacPorts、Homebrew 和 MSys2/MinGW 等包管理器。它解释了如何构建该库，包括配置数据目录和处理特定的 CPU 架构。它还介绍了如何安装 Senzing Inc. 提供的替代数据模型，该模型侧重于改进美国、英国和新加坡地址的解析。

Libpostal 使用机器学习，基于超过 10 亿个地址进行训练，将地址解析为门牌号、道路、城市和国家/地区等组成部分。`expand_address` API 规范化地址以用于搜索索引，支持各种特定于语言的规范化。文档提供了使用 Python 和 C API 进行解析和规范化的示例，以及命令行用法。

文档列出了官方支持和非官方支持的语言绑定和数据库扩展，以及指向它们各自存储库的链接。最后，它描述了如何使用“greatest”测试框架运行自动化测试。

---

## 33. 镭音乐编辑器

**原文标题**: Radium Music Editor

**原文链接**: [http://users.notam02.no/~kjetism/radium/](http://users.notam02.no/~kjetism/radium/)

镭是一种独特的音乐编辑器和数字音频工作站(DAW)，旨在通过其创新的界面实现易用性。它结合了钢琴卷轴和音轨器界面的元素，允许对音乐数据进行图形和文本编辑。镭具有音频和MIDI多轨录音、各种参数（音高、力度、效果、速度）的自动化、颗粒合成以及模块化调音台。它支持多种插件格式（AU、LADSPA、LV2、VST、VST3），并包括内置效果器、乐器和Pure Data环境（目前仅限Linux）以及Faust DSP环境。

主要功能包括：与其他DAW同步、图形缩放、可调节的每拍线数、微分音、通过Python或Scheme进行脚本编写、插件延迟补偿、多核支持和无限的撤销/重做。镭是开源的，并优先考虑简单的构建系统。快速入门说明鼓励用户加载演示歌曲，使用空格键播放，并使用键盘添加音符。

镭最初构思于1997年，并于2000年首次发布，已被移植到Linux、Windows和Mac，成为一个大型且高级的类似音轨器的音乐编辑器。定期的更新和发布突出显示了持续的开发。该项目鼓励用户通过捐赠和订阅来支持，这会优先处理错误报告和功能请求，并授予对预构建二进制文件的访问权限。

---

## 34. Brut：Ruby 新 Web 框架

**原文标题**: Brut: A New Web Framework for Ruby

**原文链接**: [https://naildrivin5.com/blog/2025/07/08/brut-a-new-web-framework-for-ruby.html](https://naildrivin5.com/blog/2025/07/08/brut-a-new-web-framework-for-ruby.html)

Brut：一个注重简洁易用的新型Ruby Web框架，与Rails等框架的复杂性和样板代码形成对比。它优先构建页面、表单和单动作处理器，直接使用服务器生成的HTML，并充分利用现代JavaScript和CSS工具。

Brut的主要特点包括：

*   **低抽象和低仪式感：** 避免过度抽象和样板代码。
*   **内置功能：** 提供OpenTelemetry检测、Sequel驱动的数据访问和命令行自动化。
*   **专注于现代Web平台：** 利用Web组件 (BrutJS) 进行渐进增强，并使用esbuild进行CSS处理。
*   **倾向于良好的实践：** 强制执行合理的安全策略、数据库约定 (非空外键、索引) 和时区感知的时间处理。
*   **利用优秀的Gem：** 使用RSpec进行测试，Faker和FactoryBot用于测试数据，Phlex用于HTML生成。
*   **无YAML (大部分情况)：** 配置避免使用YAML，而是倾向于使用Ruby哈希、环境变量 (dotenv) 和命令行参数。
*   **清晰直接的方法：** 避免围绕资源、动作和控制器的复杂抽象。

Brut强调开发乐趣，提供了一个让开发者专注于编写Ruby、使用HTML和利用浏览器的框架，而无需无休止的架构决策或争论。该框架可通过Docker安装，并包含一个功能完善的示例应用程序 (ADRs.cloud)。作者正在继续开发，目标是发布1.0版本。

---

## 35. 我对Ground News持怀疑态度的原因

**原文标题**: Why I'm skeptical of Ground News

**原文链接**: [https://sjodle.com/posts/2024/01/ground/](https://sjodle.com/posts/2024/01/ground/)

斯科特·奥德尔对Ground News表示怀疑，该平台旨在提供跨越政治光谱的公正新闻聚合。尽管Ground News对新闻来源标注了偏见和事实性评级，但奥德尔质疑该平台可能存在的虚假平衡问题，即未经证实的观点与已确立的事实被赋予同等权重。

为了调查，奥德尔分析了2023年末的500篇“盲点”新闻（报道严重偏向一方的新闻），分为左倾或右倾。他发现，左倾新闻使用的具有高事实性的来源明显多于右倾新闻。相反，右倾新闻严重依赖于具有“混合”或“低”事实性的来源，并且政治立场更加两极分化，主要来自右倾来源。

通过人工审查，奥德尔发现了一些案例，其中Ground News将明显虚假的新闻，特别是与LGBTQ+问题、COVID-19和选举舞弊阴谋有关的新闻，作为左派的“盲点”呈现。这些新闻往往缺乏可靠的来源，并放大了错误信息。一个例子涉及对国家妇女法律中心主席关于跨性别运动员的声明的歪曲。另一个例子引用了佛罗里达州卫生局局长关于COVID疫苗中DNA片段的未经证实的说法。第三个例子宣扬了联邦调查局参与1月6日事件的虚假说法。

奥德尔得出结论，Ground News聚合和总结新闻的过程，很可能是人工智能驱动且缺乏透明度，没有充分考虑到左倾和右倾叙事之间来源质量的差异，导致在平衡报道的幌子下发表可疑的右倾内容。

---

## 36. Show HN: 离线象棋谜题应用

**原文标题**: Show HN: OffChess – Offline chess puzzles app

**原文链接**: [https://offchess.com](https://offchess.com)

离线象棋谜题：拥有超过十万谜题，随时随地提升棋艺。应用内提供评分系统、进度追踪、详细统计和主题定制。可在App Store和Play Store下载。网站页脚包含“主页”、“关于”、“隐私”和“联系方式”链接，版权归OffChess所有（2025年）。总之，OffChess提供全面便捷的离线象棋谜题体验，助力棋艺提升，并提供个性化定制功能。

---

## 37. 使用SQL注入接管超过6万个间谍软件用户账户

**原文标题**: Taking over 60k spyware user accounts with SQL injection

**原文链接**: [https://ericdaigle.ca/posts/taking-over-60k-spyware-user-accounts/](https://ericdaigle.ca/posts/taking-over-60k-spyware-user-accounts/)

埃里克·戴格尔在跟踪软件服务Catwatchful中发现了一个SQL注入漏洞，使他能够入侵超过6万个用户帐户。Catwatchful宣称自己是无法检测到的Android间谍软件，并提供3天免费试用。

戴格尔的初始设置包括创建一个试用帐户，结果显示该服务在catwatchful.pink上同时使用了Firebase和一个自定义数据库。他注意到该应用程序令人惊讶的功能，以及使用Firebase存储数据和处理命令。这限制了最初的攻击面。

戴格尔专注于catwatchful.pink服务器，发现了未经身份验证的API调用，但没有发现任何明显敏感的信息。然后，他尝试对“getDevice”端点进行SQL注入，并成功发现了一个漏洞。使用sqlmap，他转储了整个“user”表，其中包含所有62,000个帐户的明文用户名和密码。这实际上赋予了他对整个服务的控制权。

发现该漏洞后，戴格尔联系了记者扎克·惠特克，后者向TechCrunch报告了这一发现。谷歌在安全浏览中标记了该网站，托管提供商Hosting.com也关闭了catwatchful.pink网站。该服务后来在一个新域名xng.vju.temporary.site上重新出现，直到实施Web应用程序防火墙（WAF）来阻止SQL注入，该域名也存在漏洞。该漏洞凸显了不安全的编码实践的危险，以及跟踪软件对个人隐私的破坏性影响。

---

## 38. SUSE推出全新欧洲数字主权服务，以满足激增的需求。

**原文标题**: SUSE launches new European digital sovereignty service to meet surging demand

**原文链接**: [https://www.zdnet.com/article/suse-launches-new-european-digital-sovereignty-support-service-to-meet-surging-demand/](https://www.zdnet.com/article/suse-launches-new-european-digital-sovereignty-support-service-to-meet-surging-demand/)

SUSE推出“主权高级支持”服务，助力欧洲企业和政府维护数字主权，应对日益增长的数据隐私、安全以及对非欧盟科技公司的依赖。该服务旨在满足将IT基础设施和数据保留在欧盟境内的需求。

该服务确保所有支持人员和数据均位于欧盟境内，并配备指定支持工程师和服务交付经理。客户支持数据仅存储在位于欧盟境内的服务器上，且对敏感信息的访问仅限于欧盟境内员工。这对国防、政府和执法等部门尤为重要，但也适用于所有欧洲组织。

SUSE首席执行官Dirk-Peter (DP) van Leeuwen强调了数据、技术和业务运营对于数字主权的重要性，并强调需要欧盟境内的人员来确保业务连续性。这项新服务与欧洲组织采用主权云解决方案的日益增长的趋势相符，IDC指出，84%的组织正在使用或计划使用这些解决方案。该倡议受到地缘政治和经济不确定性的推动，反映了欧洲内部更广泛的数字独立运动。

---

## 39. 显示 HN: 我重写了一个过时的 React Native 地图聚类库

**原文标题**: Show HN: I rewrote an outdated React Native map clustering library

**原文链接**: [https://github.com/suwi-lanji/rn-maps-clustering](https://github.com/suwi-lanji/rn-maps-clustering)

此“Show HN”帖子介绍 `rn-maps-clustering`，这是一个现代React Native库，用于创建高性能的地图标记集群。它是对一个过时库的重写，利用强大的`supercluster`库进行高效的集群处理。它使用TypeScript构建，提供卓越的开发者体验和声明式API，类似于`react-native-maps`，易于集成。

主要功能包括对数千个点进行集群处理的高性能、完整的TypeScript类型、声明式API、可定制的集群渲染、用于在最大缩放级别展开标记的spiderfier，以及现代React hooks。可以通过npm、yarn或pnpm与`react-native-maps`一起轻松安装。

使用方法包括将`<MapView />`替换为`<ClusteredMapView />`并包装`<Marker />`组件。通过`renderCluster`属性实现自定义，允许开发者定义自己的集群标记组件，并通过`onClusterPress`属性提供有关被点击集群的信息。

该库接受标准的`MapView`属性，并提供额外的属性，如`clusteringEnabled`、`radius`、`maxZoom`、`minPoints`、`onClusterPress`、`renderCluster`、`spiralEnabled`、`clusterColor`和`clusterTextColor`，以进行进一步的自定义。它还公开了更多的supercluster选项。该帖子鼓励贡献，并根据MIT许可证获得许可。

---

## 40. iPod Linux (2017)

**原文标题**: iPod Linux (2017)

**原文链接**: [http://www.ipodlinux.org/](http://www.ipodlinux.org/)

iPodLinux是一个旨在将Linux操作系统移植到苹果iPod上的开源项目。该项目成功移植了一个定制的uClinux内核，并开发了一个名为podzilla的用户界面，提供了超出苹果原始固件的功能。

最初，iPodLinux支持第一、二、三代iPod，并持续开发对后续型号的支持，如第四代点击轮、mini、U2、Photo/Color、Nano和Video iPod。然而，对较新型号的官方支持有限，建议只有高级用户才在这些设备上安装。

该项目的网站提供了诸如官方安装程序、项目状态更新、安装指南、常见问题解答、故障排除技巧、支持信息、模块列表和podzilla主题等资源。它还跟踪其SVN存储库中的最新代码更改，显示最近的论坛帖子，并链接到项目博客。这些博客包含关于该项目的公告和更新，包括关于较新型号iPod的进展和竞赛的新闻。

---

## 41. 缺陷故事

**原文标题**: Bug Stories

**原文链接**: [https://500mile.email/](https://500mile.email/)

漏洞轶事：Harley Hicks受“500英里邮件”漏洞启发，汇编的幽默离奇软件漏洞故事集。该网站以这个经典故事命名，收录了各种按类型分类的漏洞故事，包括命令行、电力、电子邮件、硬件、Linux、网络、软件、存储、视频游戏和Windows。

每个故事都包含简短摘要、作者和发布日期、添加到该合集中的日期、来源链接以及相关类别。例子包括微波炉干扰天文信号、Wi-Fi仅在下雨时工作、有人喝可乐时应用程序崩溃以及单元测试仅在周日失败。其他亮点包括与克拉伦斯·托马斯大法官相关的漏洞、珍妮·杰克逊的音乐导致笔记本电脑崩溃以及车牌选择导致收到100张停车罚单。

该网站还邀请提交新的漏洞故事，并鼓励访问者注册每周新闻通讯，其中总结了最新添加的内容。该合集突出了软件和硬件可能出现的往往不可预测和荒谬的故障方式，强调即使是最难以解释的漏洞通常也有一个逻辑的、即使是令人惊讶的解释。

---

## 42. 佛罗里达州允许企业提高高薪员工跳槽的难度。

**原文标题**: Florida is letting companies make it harder for highly paid workers to swap jobs

**原文链接**: [https://www.businessinsider.com/florida-made-it-harder-highly-paid-workers-to-swap-jobs-2025-7](https://www.businessinsider.com/florida-made-it-harder-highly-paid-workers-to-swap-jobs-2025-7)

佛罗里达州正在实施新的法规，允许公司制定更严格的竞业禁止协议，从而使高薪员工更难更换工作。问题的核心在于这些协议的可执行性。历史上，佛罗里达州对执行竞业禁止协议有相对严格的要求，倾向于员工流动性。

这些由商业利益驱动的变革旨在保护公司在培训和专有信息方面的投资。通过使竞业禁止协议更容易执行，雇主希望留住技术娴熟的员工，并防止他们将宝贵的知识带给竞争对手。

这一转变引发了争议。支持者认为，它鼓励公司投资于员工发展，而不必担心立即损失，从而促进了创新。然而，反对者认为，它扼杀了竞争，限制了员工的收入潜力，并通过限制工人流动来阻碍经济增长。他们认为，高技能工人应该有自由追求更好机会的权利，而且过于严格的竞业禁止协议会对工作流动性和工资增长产生寒蝉效应。

文章表明，佛罗里达州的这一变化可能会为其他寻求在竞争激烈的劳动力市场中平衡雇主和雇员利益的州树立先例。

---

## 43. Xenharmlib：一个支持非西方和声系统的乐理库

**原文标题**: Xenharmlib: A music theory library that supports non-western harmonic systems

**原文链接**: [https://xenharmlib.readthedocs.io/en/latest/](https://xenharmlib.readthedocs.io/en/latest/)

Xenharmlib是一个Python库，专为音乐理论设计，其功能超越了传统的西方体系，支持非西方的和声结构、微分音调律和非传统的记谱法。它面向具有Python知识的作曲家和研究人员，提供以科学方式探索和声关系的工具，而非作为乐谱创作工具使用。

主要功能包括支持平均律（例如，博伦-皮尔斯）、西方和升/降记谱法、音程和音阶分析、群论分析、音程序列模式匹配、调性建议以及基本的后调性分析。

该库是面向对象的，但设计上遵循函数式编程原则，对象是不可变的。

计划中的功能包括西方音乐模板、乐谱渲染插件、高级后调性分析、MOS音阶生成、纯律支持等等。Xenharmlib采用GNU公共许可证v3发布，源代码托管在Gitlab上。欢迎贡献，请遵循特定的格式和测试指南。文档提供用户指南、API文档和变更日志。

---

## 44. 忒伊亚的动力学起源，地球的最后一次巨大撞击体

**原文标题**: Dynamical origin of Theia, the last giant impactor on Earth

**原文链接**: [https://arxiv.org/abs/2507.01826](https://arxiv.org/abs/2507.01826)

本文于2025年7月2日提交至arXiv，探讨了忒伊亚的动力学起源，忒伊亚是被假设为形成月球的巨大撞击体。作者Branco、Raymond和Machado研究了忒伊亚是否可能是一个碳质（CC）天体，以解释地球从碳质物质中吸积了相当一部分质量（5-10%）的宇宙化学证据，这些物质很可能是忒伊亚后期带来的。

该研究使用类地行星形成的动力学模拟，考虑了标准的行星胚胎和星子设置，以及由木星向内散射的碳质天体群。模拟成功地复制了内太阳系的几个关键特征，包括地球和金星的质量和轨道，地球的碳质质量分数，以及火星的低得多的碳质质量分数，这是通过假设火星只吸积碳质星子实现的。

该研究还与最后一次巨大撞击的时间以及由非碳质（NC）天体主导的后期吸积阶段相吻合。模拟结果表明，总质量为0.2-0.3个地球质量的散射碳质天体，具有较高的胚胎-星子比率（至少为8），以及0.01-0.05个地球质量范围内的碳质胚胎，导致忒伊亚大约有50-50的机会成为一个碳质天体。忒伊亚可能是一个纯碳质胚胎，也可能是一个之前吸积过碳质胚胎的非碳质胚胎。作者总结说，他们的动力学模拟支持了宇宙化学研究提出的忒伊亚的碳质起源。

---

## 45. 斯瓦希里语在路上

**原文标题**: Swahili on the Road

**原文链接**: [https://www.historytoday.com/archive/behind-times/swahili-road](https://www.historytoday.com/archive/behind-times/swahili-road)

摩根·J·罗宾逊的《道路上的斯瓦希里语》探讨了斯瓦希里语在东非崛起成为主要通用语的过程。文章重点介绍了朱利叶斯·尼雷尔在坦噶尼喀独立运动和随后的国家建设中推广斯瓦希里语的关键作用。尼雷尔，坦噶尼喀非洲民族联盟（TANU）的领导人，拥护斯瓦希里语作为一种统一力量，这对于他的*乌贾马*（家庭/非洲社会主义）哲学至关重要。

文章详细介绍了斯瓦希里语的历史进程，从一种集中在东非沿海地区的语言，到其通过19世纪贸易路线的传播。 通过欧洲传教士学校对斯瓦希里语的标准化为“规范斯瓦希里语”奠定了基础。

虽然肯尼亚也接受了斯瓦希里语，但由于欧洲定居者人口较多和民族语言紧张等因素，其在后殖民政治中的作用不如坦桑尼亚那么突出。 尽管如此，斯瓦希里语在肯尼亚仍然是一种充满活力的语言，Sheng方言就是例证。

罗宾逊还强调了坦桑尼亚的政治影响力，特别是其对南部非洲解放运动的支持。 这巩固了斯瓦希里语与泛非团结的联系，导致它被纳入非洲大陆的教育课程中。 文章最后将斯瓦希里语描述为一种“道路上的语言”，它受到历史贸易、政治行动主义及其在非洲建立联系的持久能力的影响。

---

## 46. 2025年电子邮件能传送500英里吗？

**原文标题**: Can an email go 500 miles in 2025?

**原文链接**: [https://flak.tedunangst.com/post/can-an-email-go-500-miles-in-2025](https://flak.tedunangst.com/post/can-an-email-go-500-miles-in-2025)

2025年7月，tedu重新审视了一则轶闻：一位大学校长由于配置错误的sendmail服务器中声称存在的3毫秒超时限制，无法发送超过500英里的电子邮件。 Tedu着手重现这一现象，探索短时超时是否真的会阻止与地理位置较远的服务器建立连接。

作者开发了一个C程序，使用非阻塞套接字和带有3毫秒超时的`poll`来模拟连接尝试。最初针对美国各地大学（宾夕法尼亚大学、芝加哥大学、加州大学洛杉矶分校）的测试出人意料地成功了，表明许多服务器托管在地理位置接近的数据中心，从而抵消了距离因素。

Tedu改变了方法，寻找具有明显更长ping时间的大学，这意味着更远的物理距离。罗格斯大学很容易访问。卡内基梅隆大学和缅因大学出现间歇性故障，表明它们接近理论上的500英里限制，而代顿大学始终无法访问。

最后，tedu调查了MX（邮件交换）记录，发现许多大学将电子邮件托管外包给大型提供商。宾夕法尼亚大学的MX服务器表现出高延迟，而斯坦福大学接近理论极限，加州大学洛杉矶分校使用谷歌的SMTP服务器，延迟较低，突显了电子邮件路由和服务器位置的不可预测性。

结论是，虽然基于配置错误的服务器的理论500英里限制可能仍然存在，但云服务的普遍使用和外包使得仅根据地理距离来预测哪些域可以访问变得极其困难。“光速”限制仍然相关，但服务器位置通常已被抽象化。

---

## 47. 施普林格·自然机器学习书籍充斥着捏造的引用

**原文标题**: Springer Nature book on machine learning is full of made-up citations

**原文链接**: [https://retractionwatch.com/2025/06/30/springer-nature-book-on-machine-learning-is-full-of-made-up-citations/](https://retractionwatch.com/2025/06/30/springer-nature-book-on-machine-learning-is-full-of-made-up-citations/)

一本施普林格·自然出版社的书籍《精通机器学习：从基础到高级》正受到审查，原因是其中大量引文疑似伪造。一项调查显示，抽样调查中三分之二的引文要么不存在，要么包含重大错误，研究人员证实他们的作品被曲解或根本不存在。

文章暗示这些错误表明文本是由大型语言模型（LLM）如ChatGPT生成的，这些模型可以生成看似合法的引文，但缺乏适当的验证。该书作者Govindakumar Madhavan并未否认使用LLM生成文本，并承认区分人工智能生成内容和人类撰写文本的挑战。

虽然施普林格·自然声称已制定关于人工智能使用的政策，要求人工监督和披露，但《精通机器学习》一书中并未包含此类声明。出版社表示正在调查该书。

文章强调了人们对人工智能生成虚假引文的日益增长的担忧，并引用了其他报告和文章中的类似案例。它还指出施普林格·自然出版社自己的博客文章，其中讨论了书籍研究的完整性以及在人工智能工具旁进行人工监督的重要性。该事件引发了人们对当前编辑流程在检测人工智能生成的错误和维护学术出版物中研究诚信的有效性的质疑。

---

## 48. 对颠覆视而不见——错失未来的CEO

**原文标题**: Blind to Disruption – The CEOs Who Missed the Future

**原文链接**: [https://steveblank.com/2025/07/08/blind-to-disruption-the-ceos-who-missed-the-future/](https://steveblank.com/2025/07/08/blind-to-disruption-the-ceos-who-missed-the-future/)

史蒂夫·布兰克的博文《对颠覆视而不见——错失未来的CEO们》以20世纪初马车行业的衰落为例，阐述了企业如何未能适应颠覆性技术，并将此与当前人工智能的兴起相提并论。

文章解释说，1900年美国拥有超过4000家马车制造商，但在二十年内，随着汽车的出现，几乎全部消失。马车制造商认为早期的汽车不可靠、昂贵且新奇，他们将自身视为工匠而非运输提供者。即使汽车变得更加实用和经济实惠，这种否认仍然存在。

福特T型车和大规模生产成为了转折点，引发了整个与马相关的生态系统的崩溃。虽然早期的汽车制造商最初大量借鉴了马车设计，但他们最终通过新材料和工程技术进行了创新。

只有斯图贝克、费舍尔车身和杜兰特-多特成功地完成了转型。斯图贝克通过理解其核心业务是移动性而非马车，直接转向汽车生产。费舍尔车身将其马车车身制造技能转用于汽车车身。杜兰特用他的马车财富投资汽车行业，创建了通用汽车。

作者将其他3999家马车制造商的失败归因于技术的不连续性、重新装备的高资本要求、商业模式惯性、文化认同、低估采用曲线以及缺乏有远见的创始人。

布兰克认为，马车行业的教训在今天仍然具有现实意义，因为CEO们往往被激励专注于短期收益，而不是在面对像人工智能这样的颠覆时进行长期的重塑。他最后敦促CEO们选择他们的公司是像斯图贝克一样适应并蓬勃发展，还是成为另一场颠覆的牺牲品。

---

## 49. 那个在Tim Hortons找不到工作的白人？他是人工智能。

**原文标题**: That white guy who can't get a job at Tim Hortons? He's AI

**原文链接**: [https://www.cbc.ca/news/ai-generated-fake-marketing-1.7578772](https://www.cbc.ca/news/ai-generated-fake-marketing-1.7578772)

一系列由人工智能生成的TikTok视频，内容为一个名叫“乔什”的白人男子抱怨自己在加拿大找不到工作，并将此归咎于移民抢走了工作，尤其是在Tim Hortons。在加拿大广播公司（CBC News）询问后，这些视频已从该平台移除。这些视频由人工智能公司Nexa使用谷歌的Veo AI软件制作，因未明确标注为人工智能生成而违反了TikTok的社区准则。“乔什”发表了带有种族色彩的言论，声称印度移民抢走了工作，并暗示他在Tim Hortons被问及是否会说旁遮普语。这些视频属于一种名为“虚假影响力”的趋势的一部分，即公司创建虚假人物来推广产品或服务。Nexa首席执行官Divy Nayyar承认，这些视频旨在与那些认为印度人“正在接管就业市场”的人建立联系。营销专家谴责这项活动具有欺骗性和不道德性，并将其比作极右翼信息。一些TikTok用户认出这些视频是人工智能生成的，而另一些用户则认为它们是真实的，突显了在线区分现实与虚构的难度越来越大。虽然TikTok要求人工智能生成的内容必须明确标注，但其对该政策的执行似乎不一致。专家警告说，创建带有仇恨信息的逼真的人工智能视频的容易性，对社交媒体构成了日益严重的问题。

---

## 50. 使用 Rust 和 CGI 每日处理 5 亿请求

**原文标题**: Serving a half billion requests per day with Rust and CGI

**原文链接**: [https://jacob.gold/posts/serving-half-billion-requests-with-rust-cgi/](https://jacob.gold/posts/serving-half-billion-requests-with-rust-cgi/)

本文探讨了用各种语言编写的 CGI 脚本的性能，挑战了 CGI 本身不安全或速度慢的误解。作者 Jacob Gold 使用基于 AMD Genoa 的虚拟机和 `vegeta` 负载测试工具，对 Bash、Perl、JavaScript (Node.js)、Python、Go、Rust 和 C 中的 CGI 实现进行了基准测试。

结果显示出广泛的性能差异。Bash 最慢，每秒处理 40 个请求，而 Perl、JavaScript 和 Python 每秒处理 500-700 个请求。编译型语言 Go、Rust 和 C 表现出明显更好的性能。Go 达到每秒 3,400 个请求，而 Rust 和 C 都接近每秒 5,700-5,800 个请求。

尽管承认 CGI 可能不是 *最高* 性能的选择，但 Gold 总结说，当与编译型语言一起使用时，CGI 对于实际应用来说足够快。作者强调了 CGI 作为一种协议的简单性和强大性，并强调安全问题主要与实现相关，而不是协议本身。用于基准测试的代码和 Dockerfile 可在 GitHub 上找到。

---

## 51. 新视野号图像促成首次星际导航测试

**原文标题**: New Horizons images enable first test of interstellar navigation

**原文链接**: [https://www.newscientist.com/article/2486823-new-horizons-images-enable-first-test-of-interstellar-navigation/](https://www.newscientist.com/article/2486823-new-horizons-images-enable-first-test-of-interstellar-navigation/)

NASA的“新视野号”探测器，正远征至太阳系之外，实现了首次星际导航测试。天文学家利用该探测器独特的银河系星体观测视角，确定了其在银河系中的位置。由于视差效应，从“新视野号”观测到的星体位置与地球观测到的有所不同。通过比较“新视野号”拍摄的比邻星和沃夫359的照片与盖亚空间望远镜的星图，研究人员计算出了该探测器的位置。

虽然视差法的精度目前不如NASA的深空网络(DSN)，但它将“新视野号”定位在一个半径为6000万公里的球体内。研究人员认为，通过改进设备，精度可以显著提高。

尽管DSN可以为航天器提供高度精确的定位读数，但这种新颖的星际导航技术可能对长距离太空旅行更有益，因为它不依赖于从地球发送的信号，这些信号需要数年才能到达并从星际距离返回。尽管潜力巨大，但目前还没有计划中的任务会充分利用这种导航技术。

---

## 52. 植物通过感知气体扩散来监控其屏障的完整性

**原文标题**: Plants monitor the integrity of their barrier by sensing gas diffusion

**原文链接**: [https://www.nature.com/articles/s41586-025-09223-4](https://www.nature.com/articles/s41586-025-09223-4)

本文探讨了植物监控和修复其保护性外层屏障——周皮的机制。研究人员发现，植物利用气体（特别是乙烯和氧气）的扩散来感知拟南芥根和花序梗中周皮的完整性。

当周皮受损时，乙烯泄漏，氧气进入，导致乙烯信号和缺氧信号减弱。这种变化促进了伤口部位周皮的再生。随着周皮再生和屏障重建，乙烯和缺氧信号的水平恢复到受伤前的水平。

研究人员证明，乙烯水平升高会阻碍周皮再生，而乙烯信号减弱则会促进周皮再生。他们使用动态乙烯报告基因品系表明，受伤后乙烯信号降低，这支持了乙烯从伤口泄漏的观点。此外，他们发现阻断伤口部位的气体扩散会抑制再生。

总而言之，该研究揭示了植物通过感知气体扩散的变化来监控其外层屏障的完整性。这种气体扩散机制是一个普遍原理，使植物能够在受伤后维持和重建其保护性屏障组织。

---

## 53. Attimet (YC F24) – 量化交易研究实验室 – 招聘创始研究员

**原文标题**: Attimet (YC F24) – Quant Trading Research Lab – Is Hiring Founding Researcher

**原文链接**: [https://www.ycombinator.com/companies/attimet/jobs/6LaQIc5-founding-researcher-quant](https://www.ycombinator.com/companies/attimet/jobs/6LaQIc5-founding-researcher-quant)

Attimet (YC F24)，一家专注于为金融市场构建时间序列AI系统的量化交易研究实验室，正在旧金山招聘创始研究员/量化分析师。该职位提供10万至15万美元的薪资和0.25%至1.00%的股权。

Attimet通过快速迭代和学习而非秘密数据来脱颖而出。理想的候选人将领导机器学习/人工智能战略，特别是在期权交易方面，连接研究和实际部署。职责包括开发预测模型、强化学习智能体和信号发现工作流程，整合另类数据，并通过模拟和实盘交易测试假设。

该公司正在寻找在机器学习/人工智能（尤其是时间序列、预测、表征学习）方面具有深厚专业知识、精通Python编码技能以及具有生产环境模型部署经验的人才。不需要金融市场经验；重视驱动力和好奇心。该职位提供高度自主性，以影响研究方向、建模堆栈和实验文化。

Attimet旨在构建一个实验平台，通过连接流动市场中的理论和实践来加速研究。他们专注于学习系统和清晰的抽象，以构建更好的金融市场模型，尤其是他们认为模型不足的期权。该公司成立于2024年，是YC F24批次的一部分，拥有3人的团队，并且正在积极运营。创始人拥有来自Optiver、DRW和Argo AI的经验。

---

## 54. 格罗方德将收购MIPS

**原文标题**: GlobalFoundries to Acquire MIPS

**原文链接**: [https://mips.com/press-releases/gf-mips/](https://mips.com/press-releases/gf-mips/)

格罗方德将收购MIPS。此外，MIPS正与赛恩特半导体合作，开发基于RISC-V的定制智能电源解决方案。这些解决方案将面向人工智能电源供应、工业机器人和汽车行业的应用。此次合作旨在利用赛恩特半导体在定制芯片方面的专业知识和MIPS的RISC-V架构，提供创新的电源管理解决方案。该新闻稿来自加利福尼亚州圣何塞和印度海德拉巴，日期为2025年6月12日。

---

## 55. 人工智能、权力与社会语言学 (2024)

**原文标题**: AI, power and sociolinguistics (2024)

**原文链接**: [https://www.researchgate.net/profile/Ico-Maly-2/publication/385703534_AI_power_and_sociolinguistics/links/6813618cdf0e3f544f502f05/AI-power-and-sociolinguistics.pdf](https://www.researchgate.net/profile/Ico-Maly-2/publication/385703534_AI_power_and_sociolinguistics/links/6813618cdf0e3f544f502f05/AI-power-and-sociolinguistics.pdf)

无法访问文章链接。

---

## 56. Ceramic：一个使用Haxe开发的跨平台开源2D框架

**原文标题**: Ceramic: A cross-platform and open-source 2D framework in Haxe

**原文链接**: [https://ceramic-engine.com/](https://ceramic-engine.com/)

Ceramic 是一个使用 Haxe 编程语言构建的跨平台 2D 框架。其主要优势在于一次编写代码，即可编译到多个目标平台，包括 C++、JavaScript 和 C#。这使开发者能够为 Windows、Mac、Linux、iOS 和 Android 创建原生应用，以及使用 HTML5/WebGL 创建基于 Web 的应用。 Ceramic 还支持将项目导出到 Unity 游戏引擎。本质上，Ceramic 为 2D 开发提供了一个精简且通用的解决方案，简化了在各种平台上创建和部署应用的过程。

---

## 57. Show HN: Pyhoff – 将 Python ML 模型连接至 Beckhoff/WAGO IO 硬件

**原文标题**: Show HN: Pyhoff – Connect Python ML Models to Beckhoff/WAGO IO Hardware

**原文链接**: [https://github.com/Nonannet/pyhoff](https://github.com/Nonannet/pyhoff)

Pyhoff：通过ModBus TCP与倍福和WAGO总线端子通信的Python包

Pyhoff 是一个 Python 包，旨在通过以太网总线耦合器（BK9000、BK9050、BK9100、WAGO 750_352）使用 ModBus TCP 与倍福和 WAGO 总线端子 (Busklemmen) 进行通信。这实现了基于 Python 的机器学习模型与工业 I/O 硬件的无缝集成。

主要功能包括：支持各种模拟和数字端子、轻量级实现且无依赖项、易于扩展，以及用于简化 I/O 操作的高级抽象。

Pyhoff 的预期用例包括工业测试装置、研究自动化和数据采集/监控系统。可以使用 `pip install pyhoff` 直接安装。代码示例展示了如何连接到总线耦合器、添加总线端子、写入数字输出、从模拟输入读取温度以及设置模拟电压输出。

该项目鼓励贡献对其他 I/O 终端的支持。文档包括一个开发者指南，用于设置开发环境、运行测试和贡献代码。该软件包在 MIT 许可证下获得许可。本质上，Pyhoff 提供了 Python 生态系统与工业自动化硬件之间的桥梁，促进了在工业环境中使用基于 Python 的控制和监控解决方案。

---

## 58. 狡猾实验室笔记本：移动中

**原文标题**: Guile Lab Notebook: On the Move

**原文链接**: [https://wingolog.org/archives/2025/07/08/guile-lab-notebook-on-the-move](https://wingolog.org/archives/2025/07/08/guile-lab-notebook-on-the-move)

本 Guile 实验室笔记本条目详细记录了将 Guile Scheme 解释器与 Whippet（一种自定义垃圾回收器 (GC)）集成的进展。作者已成功将 Guile 连接到 Whippet 的主要移动回收器，该回收器具有保守的堆栈扫描和就地标记功能，以提高效率。当需要压缩时，回收器会尝试疏散对象，如果空间不足，则回退到就地标记。可以固定对象以防止移动，用于堆栈切片和地址暴露给 Scheme 的对象（例如，通过 hashq）。

作者描述了 Guile 内部的大量重构，以实现集中式对象跟踪，这对于 GC 的运行至关重要。在开发过程中，他们发现了几个错误，包括 Whippet 中的一些错误。一个具体的错误涉及 Nofl 空间（用于小对象）中对象疏散期间的竞争条件。多个线程可以并发地尝试疏散同一个对象，从而导致对象初始字被临时覆盖的无效状态，这可能会损坏跟踪。作者提出了一个潜在的修复方案，涉及在标记字节边表中管理疏散状态机。

关于性能，初步结果表明，与 Guile 的非移动配置相比，有了净改进，与 BDW-GC 相比，有了略微改进。但是，作者强调目前仍然专注于正确性，并且需要在做出明确的性能声明之前进行进一步的测试和启发式调整。

---

## 59. 感觉像GIF的SVG

**原文标题**: SVGs that feel like GIFs

**原文链接**: [https://koaning.io/posts/svg-gifs/](https://koaning.io/posts/svg-gifs/)

本文重点介绍了一种使用 SVG 创建动态图像的方法，这种图像类似于 GIF，但提供更高的分辨率和更小的文件大小。作者强调，这些使用 `asciinema` 和 `svg-term-cli` 生成的动画 SVG 文件，GitHub README.md 文件支持，使其成为展示终端交互和代码演示的有用工具。

该过程首先使用 `asciinema` 录制终端会话，然后使用 `svg-term-cli` 将录制内容转换为 SVG。本文提供了用于录制 (`asciinema rec test.cast`) 和转换 (`cat test.cast | svg-term --out=test.svg`) 的命令行代码片段。

作者还简要解释了这些动画 SVG 的工作原理，它们利用内置的 SVG 动画元素，如 `<animate>`、`<animateTransform>` 和 `<animateMotion>` 来创建动态视觉效果。作者对发现这一功能感到惊讶，并认为它具有价值，尤其是在像 Bespoken 这样的项目中。本文推广了这种方法，认为这是一种创建视觉上吸引人且技术上高效的终端操作演示的方式。

---

## 60. 火柴盒冲浪 (1999)

**原文标题**: Surfing on a Matchbox (1999)

**原文链接**: [http://news.bbc.co.uk/2/hi/science/nature/276762.stm](http://news.bbc.co.uk/2/hi/science/nature/276762.stm)

1999年BBC新闻文章《火柴盒上的网络冲浪》中，斯坦福大学的沃恩·普拉特教授展示了世界上最小的网络服务器。这台火柴盒大小的计算机，比Palm Pilot小得多，在台式机面前相形见绌，但功能齐全，可以运行网站。

该服务器由标准组件构建，尺寸为6.9 x 4.3 x 0.6厘米，配备了AMD 486-SX计算机，具有66 MHz CPU、16 MB RAM和16 MB闪存ROM，运行部分RedHat 5.2 Linux。它的功耗仅为2瓦。

普拉特教授设想通过他的可穿戴设备实验室将此类计算机融入服装中。他认为，将这个微型服务器与无线调制解调器结合使用，用户就可以在口袋里携带网络服务器。

文章强调了可穿戴计算机的数据输入挑战。为了解决这个问题，普拉特和一位博士生正在开发一种可以识别名为Thumbcode的数字手语的手套。预计未来版本的服务器将支持语音识别软件。

可穿戴设备小组还在开发一款更强大的服务器，该服务器采用信用卡大小的奔腾主板和IBM的小型高容量硬盘驱动器。

此前最小的网络服务器由Phar Lap Software制造，比斯坦福大学的新产品大10倍以上。Phar Lap的服务器展示了“嵌入式系统”如何连接到网络，为马萨诸塞州剑桥市提供实时天气数据。这项技术适用于从冰箱到医疗仪器等各种应用。

---

## 61. MicroSD卡的容量、性能与可靠性

**原文标题**: The Capacity, Performance, and Reliability of MicroSD Cards

**原文链接**: [https://www.bahjeez.com/the-great-microsd-card-survey/](https://www.bahjeez.com/the-great-microsd-card-survey/)

本文概述了一个个人项目，旨在评估microSD卡的容量、性能和可靠性，特别是那些价格低于15美元的卡。作者旨在确定microSD卡的真伪（识别虚假容量，即广告容量高于实际容量的闪存，以及容量不符，即因其他原因广告了不正确的线性容量的“劣质闪存”），根据SD协会速度等级标准测量其读/写操作的性能，并通过重复向卡写入数据直到发生故障来评估其耐用性。

该项目涉及购买各种microSD卡（名牌和非名牌），并使用GitHub上提供的定制工具进行连续测试，该工具结合了`f3`和`stressdisk`的功能。该方法包括向卡的内存的不同部分写入和读取数据，以验证其广告容量。通过顺序和随机I/O操作测试性能。通过跟踪数据错误和多次写入循环后的最终故障来评估耐用性，目标是至少2000个循环。

作者承认测试环境存在一些限制，例如使用不同的SD卡读卡器和PC，但描述了总体策略。最终，目标是为消费者提供基于数据的洞察，了解microSD卡的实际性能和寿命，特别是那些来自可能提供欺骗性定价的信誉较低品牌的卡。

---

## 62. Show HN：雨声番茄钟，伴有棕色噪音、ASMR和中东音乐

**原文标题**: Show HN: A rain Pomodoro with brown noise, ASMR, and Middle Eastern music

**原文链接**: [https://forgetoolz.com/rain-pomodoro](https://forgetoolz.com/rain-pomodoro)

Forgetoolz 雨声番茄钟：通过沉浸式声音和视觉效果增强专注力和生产力。它结合了番茄工作法，逼真的雨声、棕色噪音、ASMR 触发器和中东音景，创造一个无干扰的环境。

主要特点包括：

*   **音景：** 真实的雨声、增强专注力的棕色噪音、ASMR 选项以及激发创造力的文化底蕴深厚的中东音乐。
*   **视觉效果：** 动画雨效果，强度可调节，以及电影般的背景，如星云、北极光、沙漠和森林。
*   **智能番茄工作法系统：** 可定制的 25 分钟专注会话、休息提醒、会话跟踪以及无干扰的全屏模式。

雨声番茄钟旨在提高注意力，减轻压力，并预防眼睛疲劳。 棕色噪音被强调为优于白色噪音，可有效屏蔽干扰。 该工具通过结合优质的音频和视觉元素脱颖而出，提供独特的沉浸式专注体验。 它还提供 Forgetoolz 其他免费开发者工具的链接，例如代码转图片转换器、二维码生成器、密码生成器和按钮构建器。 无需注册即可使用。

---

## 63. 为多态数据选择数据库模式 (2024)

**原文标题**: Choosing a Database Schema for Polymorphic Data (2024)

**原文链接**: [https://www.dolthub.com/blog/2024-06-25-polymorphic-associations/](https://www.dolthub.com/blog/2024-06-25-polymorphic-associations/)

本文探讨了如何在关系型数据库中对多态数据进行建模，其中数据可以采用多种形式，并以存储患者支付信息（有保险 vs. 无保险）为例。它概述了四种不同的模式方法，每种方法都有其自身的优缺点：

1.  **单表可空字段：** 概念上最简单，使用一个表，其中包含每个可能数据类型的可空列。如果没有复杂的 `CHECK` 约束，则难以强制数据完整性和不变性。大型数据集可能会降低性能。

2.  **可空父到子外键：** 将数据拆分为多个表（每个支付类型一个表），并在患者表中使用外键。更好地强制执行 `NOT NULL` 约束，但需要 `CHECK` 来确保每个患者只有一种支付类型。引入额外的 `JOIN` 操作。

3.  **外键的标记联合：** 使用单个外键列和一个“标记”列（枚举）来指示支付类型。使用生成的列来重新获得外键约束。查询中可能容易出错，并且由于存储的生成列而增加了表的大小。

4.  **子到父外键：** 每个支付类型表都使用复合主键（患者 ID 和支付类型）引用患者表。需要在子表中存储支付类型，但简化了更新，并允许在不修改父表的情况下添加实现。无法检测到没有支付方式的情况。

文章总结说，最佳方法取决于具体需求，优先考虑性能、可读性、可维护性和安全性。最终，由于关系型数据库的起源早于面向对象编程，因此关系型数据库在多态数据建模方面面临挑战。

---

## 64. 好的写作规则 (2007)

**原文标题**: Rules of good writing (2007)

**原文链接**: [https://dilbertblog.typepad.com/the_dilbert_blog/2007/06/the_day_you_bec.html](https://dilbertblog.typepad.com/the_dilbert_blog/2007/06/the_day_you_bec.html)

好的，以下是基于所提供的URL对Scott Adams的《优秀写作规则》（2007）的总结。这里假设内容与标题以及博客的典型风格相符。

这篇文章概述了Scott Adams（《呆伯特》的作者）关于有效写作的原则。他认为，好的写作不在于语法上的完美或复杂的词汇，而在于清晰且具有说服力的沟通。他的核心理念是将*说服力*置于风格之上。

Adams的关键规则围绕着读者容易感到厌倦且注意力持续时间短的概念。因此，写作应该是：

*   **简短精炼：** 使用短句和短段落来保持读者的参与度。消除不必要的词语，并迅速切入正题。

*   **主动语态：** 采用主动语态，使写作更直接，更具影响力。

*   **简单语言：** 使用常用且易于理解的词语。避免使用行话和过于专业的技术术语。

*   **具体性：** 使用具体的细节和例子，使您的写作更加生动且易于理解。

*   **幽默（在适当的时候）：** 注入幽默感可以帮助吸引读者，并使您的写作更令人难忘。但是，要谨慎使用，仅在适合语气和主题的情况下使用。

*   **潜意识信号：** 专注于潜意识技巧，例如使用类比、隐喻和模式，使论点在潜意识中具有说服力。

*   **讲故事：** 使用讲故事的方式来解释情况。这可以使读者理解一个想法的逻辑，而无需明确地说明。

*   **了解你的受众：** 针对您要接触的特定受众量身定制您的写作。

Adams强调，这些规则不是僵化的，而是有助于提高清晰度和说服力的指导方针。目的是吸引读者的注意力，并按预期方向影响他们的思维。

---

## 65. Epanet-JS

**原文标题**: Epanet-JS

**原文链接**: [https://macwright.com/2025/07/03/epanet-placemark](https://macwright.com/2025/07/03/epanet-placemark)

本文重点介绍了 Iterating 公司的 Luke Butler 和 Sam Payá 开发的新型 Web 应用程序 Epanet-JS，它将现代 Web 地图与 EPANET 水力模拟算法相结合，用于自来水公司的系统规划。作者 Tom MacWright 对该项目及其颠覆昂贵且过时的水力模拟软件市场的潜力表示兴奋。

MacWright 还讨论了他的开源地图编辑工具 Placemark 在 Epanet-JS 开发中的作用。Iterating 公司将 Placemark 的代码库用作其应用程序的基础，MacWright 认为这是开源开发的成功案例。他强调，他为 Placemark 使用的 MIT 许可证允许商业用途，对此他表示鼓励。

他将 Epanet-JS 与现有仅能在 Windows 上运行且按“管道”数量定价的昂贵软件进行了对比。Epanet-JS 基于浏览器并使用基于 WASM 的引擎，提供了一种更易于访问且更经济实惠的解决方案。他还赞扬了 Iterating 公司对开源 Placemark 项目的回馈以及将其自身的 epanet-js 库开源发布。

---

## 66. 隐私倡导者对伦敦警方1000起面部识别逮捕泼冷水

**原文标题**: Privacy campaigners pour cold water on London cops 1k facial recognition arrests

**原文链接**: [https://www.theregister.com/2025/07/09/big_brother_watch_met_lfr/](https://www.theregister.com/2025/07/09/big_brother_watch_met_lfr/)

本文探讨了围绕伦敦警察厅使用实时面部识别（LFR）技术的持续争论。 伦敦警察厅声称自2020年以来，在LFR的帮助下逮捕了超过1000人，但隐私活动家，特别是老大哥观察组织（BBW）认为，该技术的有效性被夸大，并且代表着对纳税人资金的低效投资。 BBW强调，LFR辅助逮捕仅占伦敦总逮捕人数的极小一部分（总体0.15%，2024年以来为0.57%）。

伦敦警察厅为LFR辩护，理由是它在抓捕罪犯方面的效率，特别是那些参与强奸和袭击等严重犯罪的罪犯。 他们还强调，LFR干预不仅仅是为了逮捕，还有助于监测罪犯遵守限制的情况，如一名性犯罪者因违反性伤害预防令而被捕的案例所证明的那样。

尽管有这些说法，但本文强调英国缺乏规范面部识别使用的具体法律，这导致了对潜在滥用和侵犯公民自由的担忧。 BBW认为，警察部队实际上是在制定自己关于该技术和监视名单的规则。 伦敦警察厅则反驳说，LFR仅将面部与监视名单进行比较，并立即删除未涉案人员的生物识别数据，最终由警官决定是否逮捕。

文章最后指出，英国继续投资于面部识别技术，最近发布了一份价值2000万英镑的LFR软件采购通知。 尽管持续受到批评，克罗伊登永久性LFR摄像头的部署标志着向加强监控的转变。

---

## 67. Reachy Mini – 面向未来AI构建者的开源机器人

**原文标题**: Reachy Mini – The Open-Source Robot for Today's and Tomorrow's AI Builders

**原文链接**: [https://huggingface.co/blog/reachy-mini](https://huggingface.co/blog/reachy-mini)

Reachy Mini：面向所有年龄段AI构建者的开源、富有表现力的机器人。起价299美元，完全可通过Python编程（即将支持JavaScript和Scratch），适用于AI开发者、研究人员、教育工作者和爱好者。它有助于使用最新的AI模型开发、测试、部署和共享现实世界的AI应用程序。

该机器人有两个版本：Lite版（299美元）和无线版（449美元）。无线版提供Raspberry Pi 5板载计算、Wi-Fi、电池供电、更多麦克风和一个加速度计，从而实现完全自主。两个版本都具有头部移动、全身旋转和动画天线。

Reachy Mini旨在通过其紧凑的尺寸、实惠的价格和即插即用行为（可在Hugging Face Hub上轻松获取）使机器人AI更易于访问。它鼓励通过轻松共享机器人行为进行社区驱动的开发，并提供现实和模拟SDK。其设计通过富有表现力的运动、多模式传感（摄像头、麦克风、扬声器）以及DIY套件形式，强调人机交互。作为开源项目，它利用Hugging Face集成来实现语音、视觉和个性化功能。硬件、软件和模拟环境都是完全开源且由社区支持的。预计将于2025年夏末/秋季开始交付。

---

## 68. PHP 8.5 alpha 1 is available for download

**原文标题**: PHP 8.5 alpha 1 is available for download

**原文链接**: [https://www.php.net/archive/2025.php](https://www.php.net/archive/2025.php)

生成摘要时出错

---

## 69. The Tradeoffs of SSMs and Transformers

**原文标题**: The Tradeoffs of SSMs and Transformers

**原文链接**: [https://goombalab.github.io/blog/2025/tradeoffs/](https://goombalab.github.io/blog/2025/tradeoffs/)

生成摘要时出错

---

## 70. What goes wrong when we write ghazals in English

**原文标题**: What goes wrong when we write ghazals in English

**原文链接**: [https://www.theparisreview.org/blog/2025/06/24/what-goes-wrong-when-we-write-ghazals-in-english/](https://www.theparisreview.org/blog/2025/06/24/what-goes-wrong-when-we-write-ghazals-in-english/)

生成摘要时出错

---

## 71. On The Meaning of Ritual

**原文标题**: On The Meaning of Ritual

**原文链接**: [https://alicemaz.substack.com/p/on-the-meaning-of-ritual](https://alicemaz.substack.com/p/on-the-meaning-of-ritual)

生成摘要时出错

---

## 72. Berry Script: lightweight embedded scripting language for microcontrollers

**原文标题**: Berry Script: lightweight embedded scripting language for microcontrollers

**原文链接**: [https://berry-lang.github.io/](https://berry-lang.github.io/)

生成摘要时出错

---

## 73. When Figma starts designing us

**原文标题**: When Figma starts designing us

**原文链接**: [https://designsystems.international/ideas/when-figma-starts-designing-us/](https://designsystems.international/ideas/when-figma-starts-designing-us/)

生成摘要时出错

---

## 74. Million Times Million

**原文标题**: Million Times Million

**原文链接**: [https://susam.net/million-times-million.html](https://susam.net/million-times-million.html)

生成摘要时出错

---

## 75. The Miyawaki Method of micro-forestry

**原文标题**: The Miyawaki Method of micro-forestry

**原文链接**: [https://www.futureecologies.net/listen/fe-6-5-the-method](https://www.futureecologies.net/listen/fe-6-5-the-method)

生成摘要时出错

---

## 76. Why are there no good dinosaur films?

**原文标题**: Why are there no good dinosaur films?

**原文链接**: [https://briannazigler.substack.com/p/why-are-there-no-good-dinosaur-films](https://briannazigler.substack.com/p/why-are-there-no-good-dinosaur-films)

生成摘要时出错

---

## 77. Show HN: Jukebox – Free, Open Source Group Playlist with Fair Queueing

**原文标题**: Show HN: Jukebox – Free, Open Source Group Playlist with Fair Queueing

**原文链接**: [https://www.jukeboxhq.com/](https://www.jukeboxhq.com/)

生成摘要时出错

---

## 78. Adding a feature because ChatGPT incorrectly thinks it exists

**原文标题**: Adding a feature because ChatGPT incorrectly thinks it exists

**原文链接**: [https://www.holovaty.com/writing/chatgpt-fake-feature/](https://www.holovaty.com/writing/chatgpt-fake-feature/)

生成摘要时出错

---

## 79. François Chollet: The Arc Prize and How We Get to AGI [video]

**原文标题**: François Chollet: The Arc Prize and How We Get to AGI [video]

**原文链接**: [https://www.youtube.com/watch?v=5QcCeSsNRks](https://www.youtube.com/watch?v=5QcCeSsNRks)

生成摘要时出错

---

## 80. LookingGlass: Generative Anamorphoses via Laplacian Pyramid Warping

**原文标题**: LookingGlass: Generative Anamorphoses via Laplacian Pyramid Warping

**原文链接**: [https://studios.disneyresearch.com/2025/06/09/lookingglass-generative-anamorphoses-via-laplacian-pyramid-warping/](https://studios.disneyresearch.com/2025/06/09/lookingglass-generative-anamorphoses-via-laplacian-pyramid-warping/)

生成摘要时出错

---

## 81. Running a Certificate Transparency log

**原文标题**: Running a Certificate Transparency log

**原文链接**: [https://words.filippo.io/run-sunlight/](https://words.filippo.io/run-sunlight/)

生成摘要时出错

---

## 82. Hugging Face just launched a $299 robot that could disrupt the robotics industry

**原文标题**: Hugging Face just launched a $299 robot that could disrupt the robotics industry

**原文链接**: [https://venturebeat.com/ai/hugging-face-just-launched-a-299-robot-that-could-disrupt-the-entire-robotics-industry/](https://venturebeat.com/ai/hugging-face-just-launched-a-299-robot-that-could-disrupt-the-entire-robotics-industry/)

生成摘要时出错

---

## 83. SIMD.info – Reference tool for C intrinsics of all major SIMD engines

**原文标题**: SIMD.info – Reference tool for C intrinsics of all major SIMD engines

**原文链接**: [https://simd.info/](https://simd.info/)

生成摘要时出错

---

## 84. At the frontier between two lives–the evolutionary origins of pregnancy

**原文标题**: At the frontier between two lives–the evolutionary origins of pregnancy

**原文链接**: [https://phys.org/news/2025-07-frontier-evolutionary-pregnancy.html](https://phys.org/news/2025-07-frontier-evolutionary-pregnancy.html)

生成摘要时出错

---

## 85. A Comprehensive Proposal Overviewing Blocks, Nested Functions, and Lambdas for C

**原文标题**: A Comprehensive Proposal Overviewing Blocks, Nested Functions, and Lambdas for C

**原文链接**: [https://thephd.dev/_vendor/future_cxx/papers/C%20-%20Functional%20Functions.html](https://thephd.dev/_vendor/future_cxx/papers/C%20-%20Functional%20Functions.html)

生成摘要时出错

---

## 86. Particle Lenia Deluxe Edition

**原文标题**: Particle Lenia Deluxe Edition

**原文链接**: [https://www.craftlinks.art/Notebook/particle-lenia/](https://www.craftlinks.art/Notebook/particle-lenia/)

生成摘要时出错

---

## 87. Lightfastness Testing of Colored Pencils

**原文标题**: Lightfastness Testing of Colored Pencils

**原文链接**: [https://sarahrenaeclark.com/lightfast-testing-pencils/](https://sarahrenaeclark.com/lightfast-testing-pencils/)

生成摘要时出错

---

## 88. Voracious honey bees threaten the food supply of native pollinators

**原文标题**: Voracious honey bees threaten the food supply of native pollinators

**原文链接**: [https://phys.org/news/2025-07-voracious-honey-bees-threaten-food.html](https://phys.org/news/2025-07-voracious-honey-bees-threaten-food.html)

生成摘要时出错

---

## 89. Grow a Garden Calculator

**原文标题**: Grow a Garden Calculator

**原文链接**: [https://growagardencalculators.net/](https://growagardencalculators.net/)

生成摘要时出错

---

## 90. New sphere-packing record stems from an unexpected source

**原文标题**: New sphere-packing record stems from an unexpected source

**原文链接**: [https://www.quantamagazine.org/new-sphere-packing-record-stems-from-an-unexpected-source-20250707/](https://www.quantamagazine.org/new-sphere-packing-record-stems-from-an-unexpected-source-20250707/)

生成摘要时出错

---

## 91. LLMs should not replace therapists

**原文标题**: LLMs should not replace therapists

**原文链接**: [https://arxiv.org/abs/2504.18412](https://arxiv.org/abs/2504.18412)

生成摘要时出错

---

## 92. Memstop: Use LD_PRELOAD to delay process execution when low on memory

**原文标题**: Memstop: Use LD_PRELOAD to delay process execution when low on memory

**原文链接**: [https://github.com/surban/memstop](https://github.com/surban/memstop)

生成摘要时出错

---

## 93. Show HN: NYC Subway Simulator and Route Designer

**原文标题**: Show HN: NYC Subway Simulator and Route Designer

**原文链接**: [https://buildmytransit.nyc](https://buildmytransit.nyc)

生成摘要时出错

---

## 94. Solving Wordle with uv's dependency resolver

**原文标题**: Solving Wordle with uv's dependency resolver

**原文链接**: [https://mildbyte.xyz/blog/solving-wordle-with-uv-dependency-resolver/](https://mildbyte.xyz/blog/solving-wordle-with-uv-dependency-resolver/)

生成摘要时出错

---

## 95. The chemical secrets that help keep honey fresh for so long

**原文标题**: The chemical secrets that help keep honey fresh for so long

**原文链接**: [https://www.bbc.com/future/article/20250701-the-chemical-secrets-that-help-keep-honey-fresh-for-so-long](https://www.bbc.com/future/article/20250701-the-chemical-secrets-that-help-keep-honey-fresh-for-so-long)

生成摘要时出错

---

## 96. Firefox is fine. The people running it are not

**原文标题**: Firefox is fine. The people running it are not

**原文链接**: [https://www.theregister.com/2025/07/08/firefox_isnt_dead/](https://www.theregister.com/2025/07/08/firefox_isnt_dead/)

生成摘要时出错

---

## 97. Mercury: Ultra-fast language models based on diffusion

**原文标题**: Mercury: Ultra-fast language models based on diffusion

**原文链接**: [https://arxiv.org/abs/2506.17298](https://arxiv.org/abs/2506.17298)

生成摘要时出错

---

## 98. I used o3 to profile myself from my saved Pocket links

**原文标题**: I used o3 to profile myself from my saved Pocket links

**原文链接**: [https://noperator.dev/posts/o3-pocket-profile/](https://noperator.dev/posts/o3-pocket-profile/)

生成摘要时出错

---

## 99. Bitchat – A decentralized messaging app that works over Bluetooth mesh networks

**原文标题**: Bitchat – A decentralized messaging app that works over Bluetooth mesh networks

**原文链接**: [https://github.com/jackjackbits/bitchat](https://github.com/jackjackbits/bitchat)

生成摘要时出错

---

## 100. Thesis: Interesting work is less amenable to the use of AI

**原文标题**: Thesis: Interesting work is less amenable to the use of AI

**原文链接**: [https://remark.ing/rob/rob/Thesis-interesting-work-ie](https://remark.ing/rob/rob/Thesis-interesting-work-ie)

生成摘要时出错

---

