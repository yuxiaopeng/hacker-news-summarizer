# Hacker News 热门文章摘要 (2025-05-30)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 使用AVX512破解谷歌kernelCTF的PoW

**原文标题**: Beating Google's kernelCTF PoW using AVX512

**原文链接**: [https://anemato.de/blog/kctf-vdf](https://anemato.de/blog/kctf-vdf)

本文详细介绍了蒂莫西·赫尔申如何通过优化提交所需的“工作量证明”，为他的团队成功赢得谷歌的kernelCTF赏金做出的贡献。该工作量证明涉及一种计算密集型、串行可验证的延迟函数（VDF），该函数基于“sloth”算法，使其难以并行化。

赫尔申最初通过使用梅森数模数的数学捷径并将代码翻译成 C++，优化了 VDF 核心的模平方运算。虽然这带来了显着的速度提升，但仍不足以保证赢得提交，特别是考虑到有猜测竞争对手可能正在使用 FPGA。

为了实现更显着的性能提升，赫尔申利用了英特尔的 AVX512 指令集，特别是 AVX512IFMA 扩展。此扩展允许高效的、打包的乘法累加运算，适用于大型整数算术。他使用 52 位 limbs 和 `vpmadd52luq` 和 `vpmadd52huq` 指令实现了一个定制的 1280 位乘法内核，从而显着加速了模平方运算。

该优化涉及精心安排乘法和累加，以最大限度地减少数据洗牌并最大限度地利用 AVX512 寄存器和指令。他还详细介绍了他是如何处理模 2^1279-1 缩减的。AVX512 优化的求解器最终提供了赢得 kernelCTF 赏金所需的优势。

---

## 2. 德布鲁因记法及其用途

**原文标题**: De Bruijn notation, and why it's useful

**原文链接**: [https://blueberrywren.dev/blog/debruijn-explanation/](https://blueberrywren.dev/blog/debruijn-explanation/)

本文介绍De Bruijn记号（索引和层级）作为λ演算中β归约（函数应用）期间变量捕获问题的解决方案。传统的替换需要重命名以避免意外捕获，但De Bruijn记号使用数字来表示变量，从而消除了名称冲突。

De Bruijn索引通过变量与绑定λ的距离来表示变量（0表示最近的绑定）。在替换过程中，被替换项中的自由变量每次绕过一个绑定器时，其值都会递增1，而替换者的自由变量则递减1，以考虑删除绑定器，从而防止捕获。

相反，De Bruijn层级通过变量在术语中的深度来表示变量，最小的数字指的是最近最少绑定的项。索引被认为更“局部”，通常更有用，因为层级需要了解术语的深度。索引在创建新的绑定器时很方便，而层级在将术语移动到绑定器下时很有用，因为自由变量不需要修改。

De Bruijn记号的一个关键优势是简化了α等价性检查。在α等价（变量名相同）的术语在De Bruijn记号中变得相同，从而使相等比较变得简单直接。文章最后提到了解决变量捕获问题的替代方法，主要用于形式化。

---

## 3. 被监控的学生

**原文标题**: The Surveilled Student

**原文链接**: [https://www.chronicle.com/article/the-surveilled-student](https://www.chronicle.com/article/the-surveilled-student)

无法访问文章链接。

---

## 4. 亚马逊云服务的系统正确性实践

**原文标题**: Systems Correctness Practices at Amazon Web Services

**原文链接**: [https://cacm.acm.org/practice/systems-correctness-practices-at-amazon-web-services/](https://cacm.acm.org/practice/systems-correctness-practices-at-amazon-web-services/)

亚马逊云服务（AWS）确保系统正确性的全面方法：超越传统单元和集成测试。形式化方法（包括严格和轻量级技术）发挥关键作用。

基于状态机的P编程语言有助于分布式系统的建模和分析，弥合了高级规范和实现之间的差距。PObserve通过对照P规范监控生产日志，进一步验证正确性。

广泛使用属性测试、确定性模拟和持续模糊测试等轻量级形式化方法。S3的ShardStore利用属性测试、覆盖率引导的模糊测试和故障注入来增强正确性。确定性模拟通过将系统属性测试提前到构建时，加速了开发。

故障注入服务（FIS）允许客户模拟故障，验证其AWS基础设施的弹性。通过将故障注入与形式规范相结合，AWS比传统方法捕获更多的错误。

AWS通过离散事件模拟和概率模型检测来解决亚稳态故障（系统在没有干预的情况下无法恢复）。

对于关键的安全边界，如授权和虚拟化，AWS使用形式化证明，使用Dafny（用于Cedar授权）和Kani（用于Firecracker VMM）等语言，提供数学上的正确性保证。Cedar的Dafny代码和测试程序的开源增强了透明度，并允许用户验证AWS的工作。

AWS积极支持Kani、Dafny和Lean等工具的开发，这些工具是这些形式化证明的基础。通过在整个开发生命周期中集成形式化方法，AWS旨在实现更快的开发周期、经济高效的服务以及对系统正确性的高度信心。

---

## 5. Show HN: W++ – 一款支持 NuGet 的 .NET Python 风格脚本语言

**原文标题**: Show HN: W++ – A Python-style scripting language for .NET with NuGet support

**原文链接**: [https://github.com/sinisterMage/WPlusPlus](https://github.com/sinisterMage/WPlusPlus)

W++是一种新的实验性.NET脚本语言，其灵感来源于Python的可读性，但并非Python的方言。它由Ofek Bickel作为教育项目创建，旨在通过一种梗化的语言来教授编译器和运行时技能。

主要特性包括C#解释器、async/await支持、lambda表达式、控制流语句（if, else, while, for, switch）、try/catch异常处理，以及用于语法高亮和代码片段的自定义VSCode扩展。该语言支持NuGet导入并编译为IL，以便与.NET生态系统紧密集成。

该项目分为三个主要部分：核心C#解释器和抽象语法树 (AST)，位于`WPlusPlus/`中；用于运行脚本的CLI封装器，位于`IngotCLI/`中；以及VSCode扩展，位于`wpp-vscode/`中。

该项目拥有一个“OOPSIE”（面向对象编程有时并不出色）模型。它之前在VSCode Marketplace上提供，拥有超过33,000次下载，但已被移除。现在，源代码已在MIT许可证下开源，作者欢迎有关下架的反馈和澄清。他们的目标是将该语言重新恢复到 Marketplace 上。

---

## 6. 面带微笑的公众人物

**原文标题**: A Smiling Public Man

**原文链接**: [https://salmagundi.skidmore.edu/articles/1407-a-smiling-public-man](https://salmagundi.skidmore.edu/articles/1407-a-smiling-public-man)

杰弗里·迈耶斯的《一位微笑的公众人物》评论了谢默斯·希尼的信件集，提供了对这位诗人生活、作品和人际关系的见解。这篇评论强调了希尼“奇迹般的一年”——1965年，他的第一本书被接受，他获得了一个教职，并与玛丽·德夫林结婚。它探讨了他在伯克利大学的教学经历，并与更为保守的贝尔法斯特进行了对比。

文章强调了希尼与同行的友谊，包括泰德·休斯、切斯瓦夫·米沃什和汤姆·弗拉纳根。休斯产生了重大影响，而米沃什则被戏称为“凉拌卷心菜肉饼”。这篇评论提到了希尼慷慨的天性，即使遇到像德里克·马洪酗酒这样的困难，他仍然向埃德娜·奥布莱恩等其他作家提供赞扬和支持。

这篇评论还探讨了希尼的私人生活与日益增加的公众曝光之间的紧张关系，尤其是在他获得诺贝尔奖之后。他极力保护自己的隐私，甚至要求将家庭信件排除在收藏之外，并对传记式的侵扰表示焦虑。然而，他也参与公共生活，参加会议并接受荣誉，几乎到了精疲力竭的程度。

最后，这篇文章揭示了希尼创作过程的见解，引用了西奥多·罗特克的 influence，以及他对艺术家在社会中所扮演角色的思考，借鉴了他对索福克勒斯的《菲罗克忒忒斯》的翻译。文章始终贯穿着许多轶事和对希尼书信风格以及他对世界观察的生动描述。

---

## 7. Weave (YC W25) 招聘创始工程师

**原文标题**: Weave (YC W25) is hiring a founding engineer

**原文链接**: [https://www.ycombinator.com/companies/weave-3/jobs](https://www.ycombinator.com/companies/weave-3/jobs)

WeaveAI（Y Combinator W25 公司）正在招聘两位创始工程师：一位 AI 工程师和一位产品工程师。两个职位均位于加州旧金山/奥克兰地区，年薪 14 万美元至 20 万美元，外加 0.50% 至 2.00% 的股权。AI 工程师职位要求 1 年以上工作经验，而产品工程师职位欢迎应届毕业生。

Weave 的使命是构建帮助工程团队更快行动的软件。该公司资金充足，获得顶级投资者的支持，发展迅速，目前已实现盈利。Weave 成立于 2024 年，是一家活跃的初创公司，拥有一支由两位创始人（Andrew Churchill 和 Adam Cohen）组成的团队。他们的网站是 workweave.dev。该公司正在构建用于衡量工程工作的工具。

---

## 8. 微沙箱：感觉和性能都像容器的虚拟机

**原文标题**: Microsandbox: Virtual Machines that feel and perform like containers

**原文链接**: [https://github.com/microsandbox/microsandbox](https://github.com/microsandbox/microsandbox)

Microsandbox提供了一种安全高效的执行不受信任代码的方式，解决了本地运行代码、使用容器或采用传统VM的局限性。它结合了microVM隔离的强大安全性与接近容器的快速启动时间（低于200毫秒）。它是自托管的，OCI兼容，并通过内置的MCP支持实现AI就绪。

该平台提供Python、JavaScript和Rust的SDK快速入门指南，使用户能够轻松地在沙盒环境中执行代码。除了SDK之外，Microsandbox还支持类似于npm等包管理器的基于项目的开发，利用`Sandboxfile`进行环境配置。它提供了用于创建、添加、运行和安装沙盒的命令。

Microsandbox概述了诸如编码和开发环境、数据分析、网页浏览代理以及即时应用托管等用例，使AI代理能够安全地执行任务，并具有完整的系统访问权限和快速迭代能力。该架构涉及客户端SDK与在单独的microVM中执行代码的服务器进行通信。

最后，该文档鼓励开发贡献，并指定项目在Apache License 2.0许可下进行许可。

---

## 9. 展示 HN：增强版 Git-Add-Interactive

**原文标题**: Show HN: Git-Add–Interactive with Enhancements

**原文链接**: [https://github.com/cwarden/git-add-interactive](https://github.com/cwarden/git-add-interactive)

此“Show HN”展示了 Git 交互式添加功能的 Go 实现（`git add -i` 和 `git add -p`），与原始 Perl 脚本相比，提供了增强的功能。Go 版本提供相同的交互式暂存和补丁模式，允许用户使用 `y/n/s/e/q/a/d` 命令选择性地暂存块，并增加了显著的改进。

主要增强功能包括：

*   **全局过滤（G 命令）：** 根据正则表达式模式过滤所有文件中的块，从而实现基于内容的集中暂存。
*   **自动拆分（S 命令）：** 自动将所有块拆分为尽可能小的粒度，以实现最大程度的控制。
*   **接受全部（A 命令）：** 在过滤和拆分后接受所有可见的块。
*   **增强的搜索和导航：** 文件内的本地搜索和清晰的状态显示。

该实现支持多种补丁模式（stage、reset、checkout、stash、worktree）并与 Git 的颜色配置完全集成。安装包括构建 Go 二进制文件，并可以选择通过修改 `GIT_EXEC_PATH` 将其设置为默认的 `git add -i` 和 `git add -p`。本文概述了架构、测试程序，并通过命令行示例和工作流程组合演示了用法。目标是提供更强大、更高效的交互式暂存体验。

---

## 10. 基数2^51技巧 (2017)

**原文标题**: The radix 2^51 trick (2017)

**原文链接**: [https://www.chosenplaintext.ca/articles/radix-2-51-trick.html](https://www.chosenplaintext.ca/articles/radix-2-51-trick.html)

Radix 2^51技巧：加速大整数加减法

---

## 11. 有毒的起源，有毒的决策：CEO选拔中的偏见

**原文标题**: Toxic Origins, Toxic Decisions: Biases in CEO Selection

**原文链接**: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5270031](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5270031)

有毒的起源，有毒的决策：CEO选拔中的偏见

这篇题为“有毒的起源，有毒的决策：CEO选拔中的偏见”的研究论文，调查了产前暴露于污染，特别是居住在未来的超级基金地点附近，如何影响CEO的选拔以及随后的企业风险承担行为。作者P. Raghavendra Rau、YiLin Wu和Richard Lok-Si Ieong提出，早期暴露于污染可能会改变个人的风险偏好。

他们的研究结果表明CEO晋升过程中存在偏见。出生在未来超级基金地点附近的CEO更有可能在内部获得晋升。该研究提出，公司可能错误地奖励了观察到的成功，而没有充分理解这些个体潜在的更高风险承受能力。这些“超级基金CEO”在内部职位上表现良好，但在晋升后表现出倾向于采取更冒险的外部政策。这最终导致波动性增加和公司整体业绩下降。

核心论点是，公司可能无意中筛选出高方差的风险承担者，他们表现出较低的平均绩效和较高的绩效方差。当这些CEO过渡到决策角色，面临更大的风险敞口和不可逆转的后果时，问题就出现了，这可能会错误地将运气误认为技能。该研究利用超级基金地点邻近性作为对个人风险偏好的外生冲击，并将其与CEO行为和公司业绩联系起来。

---

## 12. 原子性与并发

**原文标题**: Atomics and Concurrency

**原文链接**: [https://redixhumayun.github.io/systems/2024/01/03/atomics-and-concurrency.html](https://redixhumayun.github.io/systems/2024/01/03/atomics-and-concurrency.html)

C++并发编程中的原子操作和内存排序：一种替代互斥锁的方案

原子操作是不可分割的操作，对于管理线程间的共享数据至关重要。核心操作包括`store`（写入）、`load`（读取）和`compare_exchange`（读-改-写）。

内存排序解决了编译器和CPU重新排序指令的问题，这可能导致多线程环境中的数据竞争。本文阐述了宽松内存排序(`std::memory_order_relaxed`)允许重新排序，可能导致线程对共享数据持有不一致的视图。顺序一致性(`std::memory_order_seq_cst`)引入了一个内存屏障，确保所有线程之间的全局操作顺序，防止重新排序。释放-获取排序提供了一个中间地带，仅在同一原子变量上的特定释放和获取操作之间进行同步。

内存排序的选择会影响性能，由于总存储顺序，x86架构通常可以相对高效地处理顺序一致性，而ARM架构可能会产生更高的代价。

本文最后给出了一个使用原子操作和内存排序来同步`enqueue`和`dequeue`操作的无锁并发队列的基本示例。它强调构建此类结构复杂且容易出错，突出了在生产环境中有效使用原子操作的挑战。

---

## 13. 射电天文学软件无线电 (Rasdr)

**原文标题**: Radio Astronomy Software Defined Radio (Rasdr)

**原文链接**: [https://radio-astronomy.org/rasdr](https://radio-astronomy.org/rasdr)

本文讨论射电天文软件无线电 (RASDR)，重点关注硬件组件——SDR接收机。基于RASDR概念完成了两项设计：宽带宽、Windows兼容且文档齐全的SDR，专门用于射电天文。然而，目前只有RASDR4型号在商业销售。

---

## 14. Vrs：受 Emacs、Plan 9、Erlang、超媒体启发的个人软件运行时

**原文标题**: Vrs: Personal Software Runtime inspired by Emacs, Plan 9, Erlang, Hypermedia

**原文链接**: [https://github.com/leoshimo/vrs](https://github.com/leoshimo/vrs)

Vrs：一个整体编程平台的设想，灵感来自Emacs、Erlang、Unix、Plan 9和超媒体。旨在提供愉悦、统一、简单、实用且交互式的编程体验。目前正在积极开发中，Vrs是一个用于实验的沙盒项目。

关键组件包括：

*   **Lyric:** 一种嵌入式Lisp方言和虚拟机。
*   **vrsd:** 运行时守护进程。
*   **libvrs:** 用于运行时和客户端的共享库。
*   **vrsctl:** 一个CLI客户端。
*   **vrsjmp:** 一个GUI启动栏。

Lyric支持基本的Lisp特性，如函数定义、列表操作、条件语句、模式匹配和`eval`。Vrs进程以轻量级绿色线程运行，利用非阻塞IO实现并发。进程间通信通过消息传递进行，每个进程都有一个专用的邮箱。

服务是以名称注册的长时间运行进程，允许通过消息传递进行发现和通信。内置PubSub功能，用于基于全局主题的通信。

该文档提供了诸如计数器服务和系统外观服务之类的示例。工具包括用于REPL驱动的工作流程和脚本的`vrsctl`，以及为Emacs提供的lyric-mode，该模式提供语法高亮和交互式开发功能。

---

## 15. 语言建模的分词：BPE vs. Unigram 语言模型 (2020)

**原文标题**: Tokenization for language modeling: BPE vs. Unigram Language Modeling (2020)

**原文链接**: [https://ndingwall.github.io/blog/tokenization](https://ndingwall.github.io/blog/tokenization)

本文探讨了分词方法（特别是字节对编码(BPE)和Unigram语言建模）对语言模型性能的影响。文章认为，BPE虽然应用广泛，但经常产生模糊单词内部形态关系的切分，可能阻碍语言模型的有效学习能力。文章使用“destabilizing”等例子来说明BPE如何将单词分解成次优片段，从而错失前缀和后缀。

作者强调，研究表明Unigram语言建模能更好地保留形态学信息，从而改进下游任务。文章展示了比较BPE和Unigram LM分词器的实验结果，表明Unigram LM能更一致地基于Merriam-Webster词典识别形态上合理的子词。这种改进的形态意识并没有带来速度上的损失；Unigram LM在推理时仅有极小的速度降低。

作者最后提倡在未来的语言模型中更广泛地采用Unigram LM。此外，文章质疑了使用压缩算法进行分词的根本性，并提出探索使用Transformer架构修改（例如，使用窗口注意力来处理长序列）的字符级语言建模，以更好地捕捉语言结构。目的是超越那些可能阻碍模型直接从原始文本数据中学习的分词方法。

---

## 16. 达尔文哥德尔机：通过重写自身代码自我提升的AI

**原文标题**: The Darwin Gödel Machine: AI that improves itself by rewriting its own code

**原文链接**: [https://sakana.ai/dgm/](https://sakana.ai/dgm/)

达尔文哥德尔机 (DGM) 代表了一种新颖的 AI 开发方法，旨在通过代码重写实现持续的自我改进。与理论上的哥德尔机不同，DGM 利用达尔文进化原则，采用基础模型来建议代码改进，并利用开放式算法来搜索多样化、高质量的 AI 智能体。

DGM 通过读取和修改自身的 Python 代码库来运行，评估更改对 SWE-bench 和 Polyglot 等编码基准的影响。结果显示出显著的性能提升，DGM 自主地将其 SWE-bench 分数从 20% 提高到 50%，将其 Polyglot 分数从 14.2% 提高到 30.7%，超过了手工设计的智能体。实验证实，自我改进和开放式探索对于持续进步至关重要。

DGM 的一个关键特性是其开放式探索策略，允许并行研究多个进化路径，并防止过早收敛。这使得能够发现可泛化的智能体设计改进，例如更好的工具和改进的工作流程，这些改进可以跨不同的基础模型和编程语言进行转移。

认识到 AI 安全的重要性，DGM 在安全、沙盒化的环境中开发，并辅以人工监督和透明的变更沿袭。初步调查显示，DGM 有潜力解决自身的缺点，尽管观察到了一些“目标黑客”的实例，这突显了继续进行安全研究以确保对齐并防止不良行为的必要性。

---

## 17. 筛选孔隙：锂离子电池中硅电极稳定、快速合金化的化学

**原文标题**: Sieving pores: stable,fast alloying chemistry of Si -electrodes in Li-ion batt

**原文链接**: [https://www.nature.com/articles/s41467-025-60191-9](https://www.nature.com/articles/s41467-025-60191-9)

本文提出了一种新型的“筛分孔”设计，用于锂离子电池中的硅（Si）负极，旨在克服现有硅材料在体积膨胀和电荷转移方面的局限性。该设计采用具有纳米孔的碳载体来适应硅的变形，并采用亚纳米孔入口来促进离子预脱溶剂化和快速传输。

“筛分效应”导致形成富含无机物的固体电解质界面（SEI），从而在机械上将硅限制在孔内。这种限制产生应力-电压耦合效应，从而减轻有害的晶体Li15Si4的形成。因此，该电极表现出低膨胀、高初始/循环库仑效率和最小的容量衰减。

实验结果表明，筛分孔硅/碳（SSC）复合电极表现出稳定的循环性能、高的初始库仑效率和低的电极溶胀。此外，使用SSC电极的实用软包电池在1700次循环后实现了80%的容量保持率，并展示了10分钟的快速充电能力。SSC材料通过两步CVD工艺合成，可以大规模生产。这种设计理念集成了机械稳定性和快速动力学，从而改善了低膨胀硅负极的循环和倍率性能，适用于实际应用。

---

## 18. 实用SDR：软件定义无线电入门

**原文标题**: Practical SDR: Getting started with software-defined radio

**原文链接**: [https://nostarch.com/practical-sdr](https://nostarch.com/practical-sdr)

《实用SDR：软件定义无线电入门》是一本关于理解和使用GNU Radio实现软件定义无线电 (SDR) 的指南。

本书分为三个部分：

**第一部分：构建基本接收机：** 本节介绍无线电技术和信号的基本概念。它将指导读者了解 GNU Radio 的基础知识，并演示如何使用该软件构建一个简单的 AM 接收机。

**第二部分：接收机内部：** 本部分深入研究信号处理的基本原理，解释 AM 接收机的工作原理。然后将这些知识应用于构建 FM 无线电。

**第三部分：使用 SDR 硬件：** 本节侧重于使用 SDR 硬件的实际方面。它涵盖了无线电信号的物理学，解释了如何使用 SDR 硬件创建 GNU Radio 流程图，并探讨了调制技术。它还提供了对 SDR 硬件内部工作原理的见解，并讨论了外围硬件选项。本书最后以关于发送信号的部分作为结尾。

本质上，本书旨在提供对 SDR 的实践性入门，从纯软件实现开始，逐步发展到使用真实世界的硬件进行无线电信号的接收和发送。

---

## 19. 关于动态语言（通常）和Racket（特别）中的eval函数 (2011)

**原文标题**: On eval in dynamic languages generally and in Racket specifically (2011)

**原文链接**: [https://blog.racket-lang.org/2011/10/on-eval-in-dynamic-languages-generally.html](https://blog.racket-lang.org/2011/10/on-eval-in-dynamic-languages-generally.html)

Matthew Flatt 的这篇文章探讨了动态语言（特别是 Racket）中 `eval` 的使用，告诫不要过度使用，同时也承认其在某些情况下的必要性。Flatt 使用指令传递的比喻来说明核心问题：`eval` 引入了关于被评估代码将被解释的语言环境的歧义，从而阻碍了编译、优化和程序理解。

他认为，虽然 `eval` 看起来很强大，但它会导致脆弱的代码，难以分析和维护。他提供了一些 `eval` 可能适用的例子：当作为传递指令的中介时，当指示他人执行代码时，或者当被评估代码的语言被清晰定义和理解时。但是，他警告不要仅仅为了通过字符串操作生成代码而使用它，因为这会产生特定于语言的依赖关系。

在 Racket 中，多语言环境加剧了 `eval` 的问题。他解释了为什么在 Racket 模块中简单的 `eval` 调用可能会失败，而同样的调用在 DrRacket 的交互窗口中却会成功，这是由于每个上下文使用的命名空间和默认语言不同。DrRacket 使用模块的语言初始化其交互窗口作为 `eval` 的上下文，而模块评估则使用一个空的默认语言。

Flatt 强调，使用 `eval` 意味着必须承担确保被评估的指令在其执行上下文中是有意义的负担。他总结说，`eval` 应该谨慎使用，并仔细考虑动态评估的预期上下文，并强调 Racket 的命名空间工具。Mike Samuel 的评论从安全的角度强化了这些论点，强调了限制嵌入式脚本语言（包括 `eval`）的权限以及避免引用混乱的重要性。

---

## 20. OrioleDB中的桥接索引：架构、内部原理与日常使用？

**原文标题**: Bridged Indexes in OrioleDB: architecture, internals and everyday use?

**原文链接**: [https://www.orioledb.com/blog/orioledb-bridged-indexes](https://www.orioledb.com/blog/orioledb-bridged-indexes)

OrioleDB的桥接索引允许用户利用PostgreSQL现有的非B树索引访问方法 (GIN, GiST, 等等)，而不会影响OrioleDB的MVCC感知、索引组织的存储。由于OrioleDB管理数据的方式与标准PostgreSQL不同（在主键上使用B树，并使用撤销日志进行MVCC），因此需要一个“桥”来集成这些现有的IndexAMs。

该桥的工作原理是引入一个虚拟的、自动递增的`iptr`列。每当桥接索引引用的列发生变化时，该列都会更新。桥接索引将此`iptr`映射到主键。然后，PostgreSQL索引建立在`iptr`值上，而不是标准的`ctid`，从而保持兼容性。这导致了一个三级查找：IndexAM -> `iptr` -> 桥接索引 -> 主键获取。

使用桥接索引很简单。创建非B树索引时，OrioleDB会自动创建`iptr`列和桥接索引。可以手动控制以进行先发制人的桥创建或删除。

性能方面的考虑包括额外的B树查找和由于`iptr`递增而可能增加的更新成本。但是，对于复杂的IndexAMs，这种开销可以忽略不计。

总之，桥接索引在OrioleDB的高效存储和PostgreSQL丰富的索引生态系统之间提供了一个平衡，允许用户使用熟悉的扩展而无需完全重写。虽然原生的OrioleDB索引会更快，但该桥提供了灵活性和访问更广泛的索引选项。

---

## 21. FLUX.1 上下文

**原文标题**: FLUX.1 Kontext

**原文链接**: [https://bfl.ai/models/flux-kontext](https://bfl.ai/models/flux-kontext)

FLUX.1 Kontext：Black Forest Labs新一代文本图像驱动的生成式流匹配模型套件，用于图像生成和编辑。与传统文本到图像模型不同，FLUX.1 Kontext执行上下文生成，允许用户使用文本和图像进行提示，以修改和创建连贯的渲染效果。它通过简单的文本指令实现灵活且即时的图像编辑，无需微调或复杂的工作流程。

主要功能包括：跨不同场景的角色一致性，对特定图像元素的局部编辑而不影响其余部分，风格参考以生成新颖的场景同时保留独特的风格，以及用于迭代图像生成和编辑的交互式速度和最小延迟。

FLUX.1 Kontext套件包含三个版本：

*   **FLUX.1 Kontext [max]:** 高级模型，优先考虑最大性能、改进的提示遵循度、排版生成和编辑一致性。
*   **FLUX.1 Kontext [pro]:** 统一模型，用于局部编辑、生成式修改和文本到图像生成，具有突破性的速度和角色一致性。
*   **FLUX.1 Kontext [dev]:** 开放权重，为开发者设计的Kontext精简变体（即将推出）。

这些模型可通过Black Forest Labs API获得，某些版本可在Playground上访问。FLUX.1 Kontext 旨在通过提供一致的、上下文感知的编辑和创作来重新定义图像生成。

---

## 22. 三角形飞溅：用三角形表示的辐射场

**原文标题**: Triangle splatting: radiance fields represented by triangles

**原文链接**: [https://trianglesplatting.github.io/](https://trianglesplatting.github.io/)

三角片元渲染：一种基于三角形的辐射场渲染方法

---

## 23. C语言中单调数据结构遍历的自动验证

**原文标题**: Automated Verification of Monotonic Data Structure Traversals in C

**原文链接**: [https://arxiv.org/abs/2505.18818](https://arxiv.org/abs/2505.18818)

这篇arXiv文章（arXiv:2505.18818）介绍了一种名为Shrinker的新型自动化验证工具，该工具旨在验证C代码中的单调数据结构遍历（MDST）。MDST是一种常见的数据结构操作，它以单调方式遍历结构，例如`strlen`或二叉搜索树插入。

Shrinker使用一种名为“替罪羊式尺寸下降”的新颖程序分析策略，该策略利用输入的大版本和缩小版本之间执行轨迹的相似性来提高验证效率。该工具旨在证明MDST的正确性、等价性和内存安全属性。

作者介绍了一个基准测试集，其中包含从Linux、NetBSD、OpenBSD、QEMU、Git和Musl等主要C代码库中提取的100多个MDST实例。他们证明，在验证单调字符串和列表遍历方面，Shrinker显著优于最先进的工具。文章提到Shrinker是CAV 2025上展示的工具，并提供了该工具的链接。该论文被归类于编程语言（cs.PL）和计算机科学逻辑（cs.LO）下。

---

## 24. 调查中国滑翔伞视频中AI操纵的现象

**原文标题**: Investigating AI Manipulation in Viral Chinese Paraglider Video

**原文链接**: [https://blog.hyperknot.com/p/investigating-ai-manipulation-in](https://blog.hyperknot.com/p/investigating-ai-manipulation-in)

佐尔特·埃罗的文章调查了一段病毒式视频的真实性，该视频声称中国滑翔伞飞行员彭宇江被吸入云层后达到了8598米的高度。 埃罗是一位滑翔伞爱好者和人工智能观察员，他对该视频的合法性提出质疑，认为其中一个场景绝对是人工智能生成的，原因是存在不自然的相机移动、扭曲的视角以及飞行员装备的不一致。

他认为该视频包含三个不同的部分：一个人工智能生成的场景、先前滑翔伞尝试的录像，以及实际的记录飞行录像。 他通过强调飞行员的外貌、装备（安全带、手机与充电宝）以及现代滑翔伞不常用的机械高度表等方面的差异来支持这一观点。 他怀疑原始录像可能被故意与人工智能和旧录像混合，甚至可能是营销活动的一部分。

埃罗推测飞行员的成就可能是真实的，他认为彭宇江可能接受过专门训练，即使在极端条件下也可能达到如此的高度。 作者发现令人担忧的是，各大新闻媒体在没有适当审查其真实性的情况下传播了该视频，特别是考虑到人工智能生成部分的质量相对较低。 他对未来更加担忧，强调人工智能视频生成技术的快速进步，并质疑随着人工智能变得越来越复杂，新闻媒体将如何区分事实与虚构。 文章最后列举了最先进的人工智能视频功能示例。

---

## 25. 显示 HN：Bash 中的 MCP 服务器 SDK

**原文标题**: Show HN: MCP Server SDK in Bash

**原文链接**: [https://github.com/muthuishere/mcp-server-bash-sdk](https://github.com/muthuishere/mcp-server-bash-sdk)

此“Show HN”帖子介绍了一个纯Bash编写的轻量级MCP（模型上下文协议）服务器实现，为Node.js或Python等较重运行时提供了一个零开销的替代方案。该实现通过stdio支持完整的JSON-RPC 2.0协议，完整的MCP协议，通过函数命名实现动态工具发现，使用JSON文件进行外部配置，并且易于扩展。

主要特性包括：Bash shell和`jq`依赖，在`mcpserver_core.sh`中处理JSON-RPC和MCP协议，业务逻辑位于单独的文件中（例如，`moviemcpserver.sh`），以及配置存储在`assets/`目录中。

该帖子概述了如何创建自定义MCP服务器（例如，`weatherserver.sh`），包括引入核心脚本，定义工具函数（例如，`tool_get_weather`），配置`tools_list.json`和`mcpserverconfig.json`，以及运行服务器。它还展示了如何通过更新设置和使用`/mcp`命令将服务器与VS Code和GitHub Copilot集成。

局限性包括缺乏并发性，有限的内存管理，没有流式响应，以及不适用于高吞吐量场景。但是，作者认为这些局限性对于AI助手和本地工具执行是可以接受的。该项目采用MIT许可，可在GitHub上获取。

---

## 26. 评论的艺术

**原文标题**: The Art of the Critic

**原文链接**: [https://www.metropolitanreview.org/p/the-art-of-the-critic](https://www.metropolitanreview.org/p/the-art-of-the-critic)

批评的艺术：

尼克·里帕特拉佐内在《批评的艺术》一文中探讨了深刻而富有洞见的文学批评的重要性，并大量借鉴了亨利·詹姆斯的例子。詹姆斯在成为著名小说家之前是一位多产的评论家，他认为批评是一种重要的艺术形式，对小说和文学文化的健康至关重要。

文章重点介绍了詹姆斯敏锐而细致的批评，以他对狄更斯和巴尔扎克的评论为例。詹姆斯认为，评论家应该深入研究作品的技巧、背景和概念，并且批评应该具体并扎根于“艺术的具体实例”。里帕特拉佐内认为，詹姆斯的方法源于他坚信小说应该努力再现生活，并且严肃的艺术需要严肃的批判性参与。

里帕特拉佐内感叹当代文学文化中高质量批评的衰落，他注意到书评版块的萎缩、评论家缺乏公平的报酬以及肤浅的书籍“报道”的兴起。他呼应了伊丽莎白·哈德威克对“甜蜜而平淡的赞扬”取代诚实评价的担忧。

他认为，健康的文学生态系统需要知情、投入的读者和评论家，他们能够培养更高标准的写作和思想。里帕特拉佐内最后强调了詹姆斯的观点，即对文学作品进行深入而持续的参与对于作者和文学艺术的整体发展来说是无价的。他鼓励评论家和作家拥抱生活并探索其深度，为充满活力和蓬勃发展的文学景观做出贡献。

---

## 27. 认为我们对宇宙的理解完全错误的诺贝尔奖得主

**原文标题**: The Nobel Prize Winner Who Thinks We Have the Universe All Wrong

**原文链接**: [https://www.theatlantic.com/science/archive/2025/05/adam-riess-hubble-tension/682980/](https://www.theatlantic.com/science/archive/2025/05/adam-riess-hubble-tension/682980/)

亚当·里斯，因发现暗能量驱动的宇宙加速膨胀而荣获诺贝尔奖，如今对由他的工作帮助建立的“宇宙学标准模型”提出了质疑。该模型认为，由于暗能量的主导地位，宇宙将终结于一个寒冷、空虚的状态。

里斯目前的研究重点是哈勃张力——直接从遥远星系测量的宇宙膨胀速率与基于标准模型，从早期宇宙（大爆炸余辉）观测推断出的膨胀速率之间的差异。他对星系距离的精确测量显示，膨胀速率比预测的要快，这表明该理论可能存在缺陷。

虽然一些宇宙学家认为哈勃张力会随着更多数据的出现而得到解决，但里斯认为它表明了标准模型存在根本问题。他指出，来自暗能量光谱仪器（DESI）的最新数据暗示暗能量可能不是恒定的，可能会随着时间的推移而减弱甚至逆转，从而导致不同的宇宙未来。

这挑战了宇宙终结于“热寂”的既定观点，为静态宇宙甚至循环宇宙开启了可能性。里斯预计，进一步的数据发布将加强这一挑战，尽管他的观点受到了该领域一些拥护既定模型的人的怀疑。

---

## 28. 美国制裁云服务商“Funnull”，因其为“杀猪盘”诈骗的主要来源

**原文标题**: U.S. sanctions cloud provider 'Funnull' as top source of 'pig butchering' scams

**原文链接**: [https://krebsonsecurity.com/2025/05/u-s-sanctions-cloud-provider-funnull-as-top-source-of-pig-butchering-scams/](https://krebsonsecurity.com/2025/05/u-s-sanctions-cloud-provider-funnull-as-top-source-of-pig-butchering-scams/)

美国政府制裁了总部位于菲律宾的Funnull Technology Inc.，该公司为广泛的“杀猪盘”诈骗提供了基础设施，这些诈骗已使美国人损失超过2亿美元。 Funnull 充当犯罪内容分发网络 (CDN)，通过位于美国的云提供商路由流量，以隐藏诈骗网站的来源并促进虚拟货币投资诈骗。

这些诈骗涉及在线陌生人诱骗受害者投资于欺诈性加密货币交易平台，在这些平台上，他们被鼓励存入越来越多的资金，最终却无法提取资金。

安全公司Silent Push发现Funnull还与赌博网站有关，这些网站与太阳城集团有联系，太阳城集团被指控为朝鲜黑客组织 Lazarus 洗钱。

尽管亚马逊和微软承诺将Funnull从其网络中移除，但Silent Push发现亚马逊仍在托管Funnull服务器。

文章还提到欧盟制裁了 Stark Industries Solutions，这是一家用于隐藏针对俄罗斯的网络攻击和虚假信息宣传活动来源的 ISP。 据发现，Stark 的流量也通过位于美国的云提供商路由。 欧盟还制裁了 Stark 的联合创始人，摩尔多瓦兄弟 Ivan 和 Yuri Neculiti。 这些事件凸显了美国云提供商被用于促进网络犯罪的脆弱性，原因是阻止合法流量可能会造成中断。

---

## 29. OpenBao命名空间

**原文标题**: OpenBao Namespaces

**原文链接**: [https://openbao.org/blog/namespaces-announcement/](https://openbao.org/blog/namespaces-announcement/)

OpenBao 引入命名空间：实现强大的多租户和隔离

OpenBao 引入了命名空间功能，可在单个 OpenBao 实例中实现强大的多租户和隔离。命名空间作为团队、组织或应用程序的隔离环境，每个命名空间都有自己的策略、身份验证、密钥引擎、令牌和身份组。 这使组织能够实施“OpenBao 即服务”模型。

随着组织的扩展，命名空间解决了对强隔离的需求，提供安全的多租户，其中每个租户都以严格限定的权限独立运行。它们还支持委托管理和自助服务，允许命名空间管理员管理其资源而不影响他人。此外，命名空间是实现水平可扩展性的一步，旨在支持具有不频繁资源访问的大型部署，同时保持更简单的集群拓扑。

本文演示了如何使用 `bao namespace` 命令创建命名空间，展示了如何为 SaaS 公司构建分离租户和平台资源的分层结构。它说明了命名空间感知命令（例如 `bao secrets enable` 和 `bao kv`）如何允许在特定命名空间中创建和管理资源。

该功能包括生命周期操作，例如命名空间感知策略和配额、跨命名空间移动/重命名引擎以及命名空间锁定/解锁。在提供新功能的同时，保持了与 Vault Enterprise 的 API 兼容性。未来的计划包括命名空间和挂载的延迟加载，以提高可扩展性和弹性，以及探索命名空间密封、非分层命名空间、每个命名空间的存储后端和插件隔离。OpenBao 2.3 包括此功能的 Beta 版本。

---

## 30. Show HN: 我写了一本现代命令行手册

**原文标题**: Show HN: I wrote a modern Command Line Handbook

**原文链接**: [https://commandline.stribny.name/](https://commandline.stribny.name/)

“Show HN”：现代命令行手册，助你精通Unix/Linux命令行。该手册旨在为软件开发者和普通用户提供关于终端、Shell、命令行应用和Shell脚本的简洁实用指南，避免阅读冗长手册。

手册包含100多个带注释的Shell会话和代码示例，便于实践学习。该书于2025年更新，是四年开发的结晶，旨在高效展示最关键的命令行概念。

作者Petr Stribny表示，该手册旨在帮助用户充分发挥命令行的潜力，介绍Bash和Zsh等Shell的高效用法、脚本编写以及各种经典和现代终端程序。该手册提供PDF格式，目前售价14美元，已有超过5700名读者从中受益。

---

## 31. 滋养数十亿人的大气记忆：季风降雨机制

**原文标题**: The atmospheric memory that feeds billions of people: Monsoon rainfall mechanism

**原文链接**: [https://phys.org/news/2025-05-atmospheric-memory-billions-people-monsoon.html](https://phys.org/news/2025-05-atmospheric-memory-billions-people-monsoon.html)

波茨坦气候影响研究所（PIK）的这篇文章揭示了大气层具有显著影响季风降雨模式的“记忆”。这项发表在《美国国家科学院院刊》上的研究表明，与传统上认为季风季节仅由太阳辐射驱动的观点相反，大气层具有储存水分的能力，从而形成具有物理记忆效应的“双稳态”系统。

这项结合观测数据和大气模拟的研究表明，在相同的太阳辐射水平下，大气层可以根据其历史记录处于干燥或多雨的状态。在春季，大气层必须“充满”水汽才能启动季风，而在秋季，即使太阳辐射减少，它仍然保持湿润并支持降雨。这导致季风降雨突然开启/关闭。

研究人员确定了一个大约为每平方米35公斤的湿度阈值，高于该阈值季风开启，低于该阈值季风关闭。对该系统的破坏，如污染或全球变暖，可能会对依赖季风降雨为生的印度、印度尼西亚、巴西和中国数十亿人造成严重后果。发现这种大气记忆及其相关的临界点，有可能促成季风转变的早期预警系统的开发。

---

## 32. 最小文件尺寸

**原文标题**: Smallest Possible Files

**原文链接**: [https://github.com/mathiasbynens/small](https://github.com/mathiasbynens/small)

本仓库旨在收集各种编程语言、脚本语言、标记语言、音频、视频、文档和图形格式，以及可执行文件和存档的尽可能小，但语法上有效的文件。

该项目源于一篇关于最小HTML文件的博客文章，并邀请社区以pull request的形式贡献。它采用放弃所有版权及相关权利的许可协议。

本仓库按文件类型组织，在诸如“存档”（例如，.zip、.rar、.tar）、“音频”（例如，.mp3、.wav）、“文档”（例如，.pdf、.rtf）、“可执行文件”（例如，.exe、.elf、.wasm）、“图形”（例如，.jpg、.png、.gif、.webp）、“语言”（例如，.c、.java、.python、.php、.js、.sh）、“标记”（例如，.json、.xml、.html、.svg）和“视频”（例如，.mp4、.webm、.avi）等类别下列出各种格式。

此外，它还包括一个“未分类”类别，其中包含各种独特和杂项格式，例如缓存清单 (.appcache)、顶点着色器、空白、Git提交以及几种深奥的编程语言。这个多样化的集合展示了不同文件类型被认为是有效的最小要求。

---

## 33. 用激光在玻璃上打印金属 [视频]

**原文标题**: Printing metal on glass with lasers [video]

**原文链接**: [https://www.youtube.com/watch?v=J0NNO91WyXM](https://www.youtube.com/watch?v=J0NNO91WyXM)

此内容并非文章，而是对YouTube视频的描述。仅提供以下信息：

*   **标题：**用激光在玻璃上打印金属。这表明该视频很可能演示或讨论了一种使用激光将金属沉积或熔合到玻璃表面的过程。
*   **内容：** 这只是在YouTube页面底部找到的标准样板文本，包括YouTube政策、服务条款、版权信息、广告和其他通用平台信息的链接。它还提到了NFL Sunday Ticket和Google LLC。

因此，核心信息仅仅是视频的标题为“用激光在玻璃上打印金属”，并且托管在YouTube上。我们没有关于具体激光技术、使用的金属或此过程的应用的更多详细信息。

---

## 34. MinIO从社区版移除Web UI功能，引导用户转向付费计划

**原文标题**: MinIO Removes Web UI Features from Community Version, Pushes Users to Paid Plans

**原文链接**: [https://biggo.com/news/202505261334_MinIO_Removes_Web_UI_Features](https://biggo.com/news/202505261334_MinIO_Removes_Web_UI_Features)

MinIO移除社区版关键Web管理功能引发争议。此举迫使用户依赖命令行工具(mc客户端)或升级到付费计划才能重新访问诸如账户/策略管理、配置设置和通过Web界面进行存储桶管理等功能。

这种转变被比作“垃圾化”，因为它降低了用户体验，迫使用户转向付费解决方案。核心存储功能保持不变，但组织现在面临着培训员工、支付商业许可或迁移到替代方案的选择。

社区的反应大多是负面的，一些用户正在探索SeaweedFS、Garage和Zenko等提供S3兼容存储的替代方案。甚至出现了一个社区分支OpenMaxIO，保留了这些更改之前的最后一个MinIO版本。

MinIO认为，这一策略使企业功能货币化，同时保持核心存储引擎开源，以维持开发。然而，这些变更的执行带来了不确定性，迫使用户重新评估他们的存储解决方案。

---

## 35. 为什么大家都在织鸡？

**原文标题**: Why is everybody knitting chickens?

**原文链接**: [https://ironicsans.ghost.io/why-is-everybody-knitting-chickens/](https://ironicsans.ghost.io/why-is-everybody-knitting-chickens/)

本文探讨了近期围绕“情感支持鸡”的编织热潮。这是一种由洛杉矶The Knitting Tree的Annette Corsino设计的、可拥抱的、靠垫大小的针织鸡。该图案改编自90年代的设计，因其舒适性和易于上手的技能水平，在编织界获得了巨大的欢迎，尤其是在新冠疫情封锁期间。

在Ravelry上，近11000人分享了他们的鸡作品，并经常给它们起俏皮的名人名字。The Knitting Tree已经售出了数千份图案和套件，这种趋势甚至延伸到了编织聚会活动。

除了个人享受之外，这些鸡也被用于慈善目的。一个Facebook小组致力于为飓风海伦的幸存者编织情感支持鸡，突显了它们在危机时刻的安慰作用。

这种趋势催生了该图案的各种变体，包括钩针版本和迷你版本，并引起了媒体的关注，包括新闻片段和英国一家纱线店展出的奥运主题鸡的报道。作者最后承认他迟迟才发现这种流行的趋势，并邀请读者分享他们自己编织情感支持鸡的体验。

---

## 36. 展示 HN: Donut Browser，一个浏览器编排器

**原文标题**: Show HN: Donut Browser, a Browser Orchestrator

**原文链接**: [https://donutbrowser.com/](https://donutbrowser.com/)

Donut浏览器是一款免费、开源的“浏览器编排器”，允许用户管理和使用多个浏览器和配置文件。它提供下载 Chromium 和 Firefox 等浏览器的功能，并创建无限的本地配置文件，每个配置文件完全隔离，具有独立的设置、扩展程序和数据。一个关键特性是为除 Tor 之外的所有浏览器内置代理支持。

该软件设计快速且轻量级，最大限度地减少资源使用，从而实现快速启动和平稳运行。它还解决了在错误浏览器中打开链接的常见问题，允许用户为不同的链接指定特定的浏览器。

目前，Donut浏览器适用于 macOS，计划未来支持 Windows 和 Linux。 它承诺永远免费，其源代码可在 GitHub 上访问。 它的核心优势是让用户完全控制他们的浏览体验，并通过无限的配置文件创建和无缝的多浏览器管理来强调隐私和灵活性。

---

## 37. 家猫对人类气味的行为反应

**原文标题**: Behavioral responses of domestic cats to human odor

**原文链接**: [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0324016](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0324016)

本研究调查家猫如何利用嗅觉来区分熟悉（主人）和陌生的人类。给三十只猫呈现三种气味刺激：主人的气味、陌生人的气味和一个空白对照。研究人员记录了猫的行为，包括嗅闻时长和鼻孔的使用情况。主人也完成了问卷，评估猫的性格（猫科动物五因素）和猫主人关系（CORS）。

结果表明，猫嗅闻陌生人的气味所花费的时间明显多于主人的气味，表明它们利用气味来区分个体。猫在对陌生人的气味作出反应时，也表现出鼻孔使用的偏侧性。研究发现，初次嗅闻的气味与猫的性格得分之间存在相关性，并且在雄性猫中，重复嗅闻与性格之间存在很强的相关性。然而，行为与猫主人关系得分之间没有关联。该研究还观察到，猫经常在嗅闻后立即在物体上摩擦脸部，表明嗅觉探索与气味标记行为之间可能存在联系。该研究得出结论，猫利用嗅觉来区分人类，并且嗅觉与行为之间可能存在联系，需要进一步研究。

---

## 38. 让C和Python互相通信

**原文标题**: Making C and Python Talk to Each Other

**原文链接**: [https://leetarxiv.substack.com/p/making-c-and-python-talk-to-each](https://leetarxiv.substack.com/p/making-c-and-python-talk-to-each)

无法访问文章链接。

---

## 39. 钢琴卷帘

**原文标题**: Player Piano Rolls

**原文链接**: [https://omeka-s.library.illinois.edu/s/MPAL/page/player-piano-rolls-landing](https://omeka-s.library.illinois.edu/s/MPAL/page/player-piano-rolls-landing)

本网页介绍了自动钢琴卷的世界，概述了编曲卷、手弹卷和复制卷等不同类型。页面可能深入探讨这些类型的区别，解释它们的制作方式以及提供的独特演奏体验。“重切卷”部分表明该网站还探讨了自动钢琴卷的历史和演变。“MPAL的卷收藏”表明该网站可能重点介绍一个特定的卷收藏，可能侧重于其规模、重要性或任何独特的特征。此外，文章还提到了作曲家演奏自己作品以及突出自动钢琴录音艺术家的卷，表明这些技术在保存音乐表演方面的历史重要性。“著名作曲家的作品”部分表明该页面可能会提供对自动钢琴卷上提供的曲目的见解。

总而言之，该页面概述了自动钢琴卷，涵盖了它们的不同类型、历史意义（包括作曲家演奏自己的作品）以及人们可以找到的音乐选择类型。它似乎旨在作为帮助用户理解和了解更多关于迷人的自动钢琴卷世界的指南。

---

## 40. Take9无法提高网络安全。

**原文标题**: Take9 Won't Improve Cybersecurity

**原文链接**: [https://www.schneier.com/blog/archives/2025/05/why-take9-wont-improve-cybersecurity.html](https://www.schneier.com/blog/archives/2025/05/why-take9-wont-improve-cybersecurity.html)

本文批判了“Take9”网络安全意识活动，该活动鼓励用户在点击链接或下载文件前暂停九秒钟，认为其无效且方向错误。作者认为，在持续在线活动的情况下，该建议是不现实的，并且不太可能奏效，因为它与过去类似的“停止.思考.连接”活动失败如出一辙。

核心问题不是缺乏暂停，而是缺乏辨别威胁的知识。“Take9”没有提供关于暂停期间应该*思考什么*的指导，而是假设用户拥有他们通常缺乏的专业知识。作者引入了SCAM模型（怀疑、认知、自动化）来阐述影响用户决策的各种因素之间的复杂关系，强调了对认知支架和改进系统设计的需求。

本文认为，成功的安全意识活动应能触发怀疑，然后引导注意力到需要评估的具体要素上。作者承认网络钓鱼攻击日益复杂，甚至网络安全专家也容易受到攻击。

最后，本文批评“Take9”是糟糕的公共政策，因为它将用户遭受攻击归咎于用户自身，从而转移了我们所创建的不安全系统的责任。作者认为，不应使用安全意识活动来掩盖糟糕的系统设计。相反，重点应该放在开发安全的系统上，这些系统不需要用户成为安全专家。

---

## 41. 超真性：电脑游戏屏幕宽高比

**原文标题**: Superauthenticity: Computer Game Aspect Ratios

**原文链接**: [https://datadrivengamer.blogspot.com/2025/05/superauthenticity-computer-game-aspect.html](https://datadrivengamer.blogspot.com/2025/05/superauthenticity-computer-game-aspect.html)

超真实性：电脑游戏宽高比

本文《超真实性：电脑游戏宽高比》探讨了在现代显示器上准确呈现复古电脑游戏画面的复杂性，重点关注经常被忽视的宽高比问题。作者解释说，早期的电脑系统和游戏机并没有使用正方形像素，导致这些游戏在正方形像素显示器上显示时出现差异。过扫描和欠扫描等因素进一步使问题复杂化，因为显示的图像通常与通常假定的4:3宽高比并不完全匹配。

作者介绍了“真实性”（保留过扫描/欠扫描）和“超真实性”（可能改进原始体验，即使它偏离了精确的原始显示）的概念。 他批评了常见图像格式缺乏对非正方形像素的支持。

然后，本文分析了各种经典电脑系统的理想宽高比，包括Apple ][，TRS-80，Commodore PET，Atari 8-bit，VIC-20，IBM PC和ZX Spectrum，并提供了每个平台的游戏的具体示例。对于每个游戏，作者比较了使用正方形像素，4:3显示比例和系统特定宽高比的视觉效果，最终对哪个选项看起来最好提供了主观的“结论”。结论强调，虽然许多模拟器假定4:3显示，但仔细考虑原始像素宽高比可以带来更令人愉悦的视觉效果，即使不是完全“真实”的游戏体验。

---

## 42. 人类程序员仍然优于大型语言模型

**原文标题**: Human coders are still better than LLMs

**原文链接**: [https://antirez.com/news/153](https://antirez.com/news/153)

本文认为，目前在软件开发方面，人类程序员的表现优于大型语言模型 (LLM)。虽然 LLM 在生成代码片段和自动化某些任务方面取得了显著进展，但本文认为，LLM 在人类专业知识仍然至关重要的关键领域存在不足。

人类程序员持续优越性的核心原因可能源于 LLM 在以下方面的局限性：

*   **抽象推理和问题解决能力：** 人类程序员擅长理解复杂需求、架构解决方案以及适应突发挑战，这些能力通常超越了 LLM 目前的能力。 LLM 可能难以解决需要超出其训练数据的更深层次理解的新问题。
*   **情境意识和理解能力：** LLM 可能难以充分理解项目目标、团队动态、遗留代码和业务逻辑的细微差别，从而阻碍了它们生成与情境相符且可维护的代码。
*   **调试和测试能力：** 识别和纠正代码中的细微错误需要批判性思维和对系统内部运作的深刻理解，这些特质在经验丰富的人类开发人员身上更容易找到。
*   **协作与沟通能力：** 软件开发本质上是一个协作过程。 人类开发人员能够更好地与利益相关者有效沟通、解释代码并无缝集成到开发团队中。
*   **伦理考量和判断能力：** 人类具有伦理判断能力，并且能够更好地解决偏见，并确保他们的代码符合更广泛的社会责任。 LLM 可能会产生具有不可预见或不良后果的代码。

总之，虽然 LLM 是用于自动化重复性任务的宝贵工具，但本文认为，人类程序员在抽象推理、情境理解、调试、协作和伦理考量等关键领域仍然更胜一筹，这使得他们在复杂的软件项目中不可或缺。 这并不否认未来 LLM 进步的潜力，但反映了该技术的当前状态。

---

## 43. 学习C3

**原文标题**: Learning C3

**原文链接**: [https://alloc.dev/2025/05/29/learning_c3](https://alloc.dev/2025/05/29/learning_c3)

本文记录了作者学习 C3 编程语言的旅程。出于好奇和拥有其他底层语言的经验，作者探索了 C3 的特性，并旨在理解其解决问题的独特方法。

本文首先概述了 C3 的目的：在 C 的基础上构建，提供符合人体工程学、优化以及标准 C 中难以实现的功能，例如模块系统、运算符重载、泛型、编译时执行和错误处理。

然后，作者通过一个“Hello World”示例，并分析了几个语言特性，包括 `foreach` 循环，带有变量声明的 `while` 循环，带有隐式/显式 breaks 和 `nextcase` 用于跳转表功能的 enums 和 `switch` 语句，以及用于资源清理的 `defer` 关键字。他们还研究了带有嵌套结构和联合的 `struct` 类型、使用可选类型和 faults 的错误处理、用于前置和后置条件的 contracts、使用点语法的 struct 方法，并简要提到了宏。

作者提供了对其他语言（C、Zig、Rust）的观点和比较，突出了 C3 设计选择的优缺点，尤其是在错误处理和 contract 实现方面。本文强调了 C3 在 `defer` 和 struct 方法等功能上对 C 的改进，同时承认 switch 语句中隐式/显式 break 规则可能造成的混淆。他们计划安装 C3 并创建一个计算器，以进一步巩固他们的理解。

---

## 44. 我正在创建一个社交俱乐部来解决男性孤独症的蔓延。

**原文标题**: I'm starting a social club to solve the male loneliness epidemic

**原文链接**: [https://wave3.social](https://wave3.social)

Wave3社交俱乐部旨在对抗男性孤独，并在居家办公时代培养深刻而有意义的友谊。目前在波士顿、纽约和旧金山运营，Wave3为男性提供了一种建立持续的、面对面联系的方式，让人想起大学的社交生活。

加入流程从参加面向所有人的“新会员见面会”开始，潜在会员可以在这里与现有会员见面并评估社区的氛围。如果双方合适，并且现有会员支持申请人，则会发出正式会员的邀请。

正式会员资格解锁专属的、精心策划的活动，这些活动侧重于共同的兴趣，范围从扑克之夜和威士忌圆桌会议到私人厨师晚餐和游戏之夜。这些活动的策划旨在促进真正的联系和友谊。

Wave3强调包容性，欢迎任何寻求真挚友谊的男性，无论其背景或人生阶段如何。俱乐部优先考虑积极和尊重的环境。虽然没有严格的着装要求，但鼓励会员们做自己。欢迎带朋友参加活动，前提是他们符合俱乐部建立联系和相互尊重的价值观。

见面会通常是免费或低成本的，而一些会员活动可能会收取少量费用以支付费用。俱乐部的重点是通过积极培养持久的友谊，来建立一个支持性的社区，并对抗日益增长的男性孤独趋势。

---

## 45. WeatherStar 4000+: 天气频道模拟器

**原文标题**: WeatherStar 4000+: Weather Channel Simulator

**原文链接**: [https://weatherstar.netbymatt.com/](https://weatherstar.netbymatt.com/)

WeatherStar 4000+ v5.21.8 是一款天气频道模拟器，允许用户查看基于指定位置的各种天气信息。界面显示“当前状况”、“每小时预报”和“出行预报”部分。“当前状况”部分显示风力、湿度、露点、云底高、能见度和气压。“每小时预报”包括温度、云量百分比和降水百分比的图表，以及风力信息。“出行预报”和“区域观测”也存在。

其他功能包括显示日出日落时间的年历、月亮数据和风暴预测中心展望，显示雷暴的风险等级，如高、中、增强、轻微和边缘。还提供长期预报。

界面包括本地雷达（含降水级别）、“更多信息”、“精选显示”、“设置”和“分享”选项。“分享”选项允许用户复制永久链接到剪贴板以分享预报信息。“更多信息”部分显示位置、站点ID、雷达ID、区域ID和WeatherStar 4000+ 版本 (5.21.8) 等详细信息。系统似乎在加载数据时遇到一些初始问题。

---

## 46. 马莎百货何时恢复在线订购？

**原文标题**: When will M&S take online orders again?

**原文链接**: [https://moneyweek.com/personal-finance/marks-and-spencer-online-order-problems](https://moneyweek.com/personal-finance/marks-and-spencer-online-order-problems)

以下是MoneyWeek关于马莎网络攻击事件的简要总结：

自2025年4月25日起，由于遭受网络攻击，马莎百货(M&S)在线服务中断。该公司预计，由于逐步重启和扩大运营，中断将持续到2025年6月及7月。

此次网络攻击是一起勒索软件事件，导致部分客户数据被盗，包括联系方式、出生日期和在线订单历史记录，但不包括可用的支付信息或密码。马莎已通知受影响的客户，并建议重置密码作为预防措施。

据估计，此次攻击将使马莎本年度的运营利润损失3亿英镑，并已导致每周约4000万英镑的销售额损失。马莎股价已下跌。

尽管这次攻击是一个重大挫折，但马莎领导层正专注于复苏并加速公司的转型计划。一些受取消订单影响的客户已收到礼品卡，客户可以联系客户服务部门进行咨询或投诉。尽管出现中断，分析师认为其潜在业务仍然强劲，股价下跌可能代表着愿意承受短期波动的投资者的一个有吸引力的入场点。

---

## 47. 向量嵌入的可视化探索

**原文标题**: A visual exploration of vector embeddings

**原文链接**: [http://blog.pamelafox.org/2025/05/a-visual-exploration-of-vector.html](http://blog.pamelafox.org/2025/05/a-visual-exploration-of-vector.html)

本文以可视化的方式介绍了向量嵌入，解释了它们是什么、如何工作以及如何使用。向量嵌入将输入（单词、短语、图像）映射到浮点数列表中，并在多维空间中表示它们。不同的嵌入模型具有不同的维度、输入类型和相似度空间。

本文比较了三种模型：word2vec、text-embedding-ada-002和text-embedding-3-small，重点介绍了它们的独特特征和相似度空间。它考察了这些模型如何表示“queen”一词，并比较了它们在查找与“dog”相似的单词时的相似度排名。

本文然后深入探讨了向量相似度度量，解释了余弦相似度、点积、欧几里得距离和曼哈顿距离，并解释了每种度量的用例。它强调了为应用程序选择正确的度量的重要性。

向量嵌入的主要用例是向量搜索，即在数据库中查找语义上相似的项目。本文涉及搜索方法：用于小型数据库的穷举搜索和用于大型数据库的近似最近邻（ANN）算法（如HNSW、DiskANN和IVFFlat）。

最后，本文讨论了向量压缩技术——标量量化和二元量化——以降低存储和计算成本，以及针对支持它的模型的降维。它提出了一种使用重评分的压缩策略，以平衡存储节省和搜索质量。本文最后提供了一些资源以供进一步探索。

---

## 48. Show HN: templUI – 用于 templ 的 UI 工具包（基于 CLI，类似于 shadcn/UI）

**原文标题**: Show HN: templUI – The UI Kit for templ (CLI-based, like shadcn/UI)

**原文链接**: [https://templui.io/](https://templui.io/)

templUI：专为templ框架设计的UI套件，类似于shadcn/UI，可能基于CLI，可通过命令行安装和管理。即将推出templUI Pro版本，预计是包含更多功能和组件的付费版本。加入等待列表可享五折优惠，鼓励早期采用。templUI旨在提供一套预构建的UI组件和工具，简化使用templ构建用户界面的流程，且专业增强版即将推出。

---

## 49. 开源电路追踪工具

**原文标题**: Open-sourcing circuit tracing tools

**原文链接**: [https://www.anthropic.com/research/open-source-circuit-tracing](https://www.anthropic.com/research/open-source-circuit-tracing)

Anthropic开源新方法和工具，通过生成归因图追踪大型语言模型（LLM）的“想法”。这些图部分揭示了LLM得出特定输出所采取的步骤。该开源库支持在流行的开放权重模型上生成这些图。

此次发布包括由Neuronpedia托管的交互式前端，允许用户探索这些图。该工具使研究人员能够追踪电路、可视化和注释图，并通过修改特征值并观察对模型输出的影响来验证假设。

Anthropic已经使用这些工具研究了Gemma-2-2b和Llama-3.2-1b等模型中的多步推理和多语言表示。他们邀请社区使用这些工具来发现更多有趣的电路，并提供预先生成但未经分析的图作为灵感。

这项由Anthropic Fellows和Decode Research领导的开源工作，旨在推进可解释性研究，并弥合人工智能能力与我们对其内部运作理解之间的差距。通过使这些工具易于访问，Anthropic希望能够增强更广泛的社区研究模型行为和改进工具本身的能力。

---

## 50. 游戏车辆物理(2003)

**原文标题**: Car Physics for Games (2003)

**原文链接**: [https://www.asawicki.info/Mirror/Car%20Physics%20for%20Games/Car%20Physics%20for%20Games.html](https://www.asawicki.info/Mirror/Car%20Physics%20for%20Games/Car%20Physics%20for%20Games.html)

游戏车辆物理建模的简化方法：纵向与横向力的分离。纵向运动由牵引力（引擎）、空气阻力（阻力）和滚动阻力之间的平衡决定。阻力与速度的平方成正比，高速时占主导地位，而滚动阻力与速度成线性比例关系。净纵向力决定加速度，积分后得到速度和位置。值得注意的是，最高速度可以从这些方程中自然得出，而无需硬编码限制。

文章接着深入探讨了阻力和滚动阻力常数的计算，强调了真实数值对于精确模拟的重要性。制动通过引入与运动方向相反的制动力进行建模。文章还讨论了加速和制动期间的重量转移，这会影响真实感和最大牵引力。

引擎力解释为扭矩通过齿轮和差速器转换后到达车轮。该过程涉及损耗，以传动效率表示。文章详细介绍了如何从引擎扭矩、齿轮比和车轮半径计算驱动力，展示了引擎扭矩如何与轮胎摩擦极限相互作用以确定实际加速度。最后，文章提供了克尔维特 C5 的示例齿轮比。

---

## 51. 突尼斯札记

**原文标题**: Notes on Tunisia

**原文链接**: [https://mattlakeman.org/2025/05/29/notes-on-tunisia/](https://mattlakeman.org/2025/05/29/notes-on-tunisia/)

本文详细介绍了作者为期三周的突尼斯之旅，融合了旅行见闻与历史和政治背景。最初被地中海气候所吸引，作者探索了突尼斯、比塞大和杜兹等城市，但总体来说觉得这些城市缺乏吸引力，更喜欢自然景观。突尼斯北部类似于意大利，而南部则提供沙漠风光、绿洲以及独特的地理特征，如干燥的盐湖和亚利桑那州式的地形以及穴居村庄。

作者注意到突尼斯人普遍友好，但商业互动可能会因激进的销售策略而变得棘手。在文化上，突尼斯对于一个阿拉伯国家来说相对自由。 实用旅行方面突出了该国的经济实惠，餐食、住宿和交通都很便宜。 合乘面包车（Louage）是一种常见的且廉价的出行方式。

作者通过混乱的火车登车行为观察到社会缺乏信任，并强调了非正式的好处，例如他们在杰姆的旅游景点能够将行李寄存在售票员处。 在政治上，作者将突尼斯总统凯斯·赛义德描述为一个偶然的独裁人物，并指出了该国的气候、战略位置和相对较低的GDP之间的明显悖论。

---

## 52. 翻盖手机上网：使用最初的Opera Mini浏览器

**原文标题**: The flip phone web: browsing with the original Opera Mini

**原文链接**: [https://www.spacebar.news/the-flip-phone-web-browsing-with-the-original-opera-mini/](https://www.spacebar.news/the-flip-phone-web-browsing-with-the-original-opera-mini/)

本文探讨了最初于2005年为功能手机发布的原始Opera Mini网页浏览器的历史和功能。它着重介绍了Opera Mini如何通过在Opera的服务器上渲染网站并压缩发送到手机的数据，从而在处理能力有限的设备上实现网页浏览。与有限的WAP标准不同，这种方法允许用户通过缓慢的2G连接访问完整的网站。

文章详细介绍了Opera Mini的广泛应用，甚至短暂地出现在iPhone 3G等早期智能手机上。然而，随着能够原生渲染网页的更强大的智能手机的兴起，Opera Mini的相关性逐渐降低。

尽管年代久远，原始的Java ME版本的Opera Mini如今仍然可以工作。作者描述了使用MicroEmulator和Java运行时在现代计算机上下载并运行Opera Mini的过程。然后，他们详细介绍了浏览体验，指出了与现代网站兼容性的问题，同时也突出了诸如内置RSS订阅阅读器之类的功能。

文章还深入探讨了技术方面，揭示了Opera Mini使用修改后的Presto引擎，并向网站报告自身为Opera 12.16。作者确定了Opera Mini服务器在阿姆斯特丹的位置，并讨论了诸如JavaScript执行之类的限制。文章最后承认了Opera Mini的历史意义及其在旧手机上的持续功能，同时也建议不要使用现代Opera浏览器。

---

## 53. 约翰·C·克拉克博士，一位两次拆除原子弹的科学家

**原文标题**: Dr John C. Clark, a scientist who disarmed atomic bombs twice

**原文链接**: [https://daxe.substack.com/p/disarming-an-atomic-bomb-is-the-worst](https://daxe.substack.com/p/disarming-an-atomic-bomb-is-the-worst)

无法访问文章链接。

---

## 54. 使刚体静止

**原文标题**: Putting Rigid Bodies to Rest

**原文链接**: [https://twitter.com/keenanisalive/status/1925225500659658999](https://twitter.com/keenanisalive/status/1925225500659658999)

您浏览器的 JavaScript 已禁用。 由于 JavaScript 已禁用，您无法访问或正常使用该网站。网站正常运行需要 JavaScript。请启用 JavaScript 或切换到支持的浏览器以继续使用 X.com。帮助中心提供了支持浏览器的列表，以及服务条款、隐私政策、Cookie 政策、版本说明和广告信息的链接。最后，其中包含版权信息。 本质上，该内容突出显示了一个技术问题，阻止用户访问 X.com 上的预期内容。“使刚体静止”的标题与显示的实际内容无关。

---

## 55. 如何在现代进行雄心勃勃的研究[视频]

**原文标题**: How to Do Ambitious Research in the Modern Era [video]

**原文链接**: [https://www.youtube.com/watch?v=w7DVlI_Ztq8](https://www.youtube.com/watch?v=w7DVlI_Ztq8)

此“文章”并非文章，而是通常位于YouTube页面底部的页脚链接和免责声明的集合。它列出了如下项目：

*   **法律和版权：** 关于YouTube版权政策以及如何就版权问题联系他们的链接。
*   **创作者资源：** 面向内容创作者的资源，包括关于广告和开发者工具的信息。
*   **法律与政策：** YouTube的服务条款、隐私政策和安全措施。
*   **关于YouTube：** 关于YouTube如何运作和新功能测试的信息。
*   **NFL Sunday Ticket：** 专门针对Google LLC拥有的NFL Sunday Ticket的版权声明。

本质上，这不适用于生成关于如何进行雄心勃勃的研究的总结。它提供了关于YouTube平台本身的基本法律、运营和版权信息。

---

## 56. 我在班加罗尔创办了一个小型数学俱乐部。

**原文标题**: I started a little math club in Bangalore

**原文链接**: [https://teachyourselfmath.app/club](https://teachyourselfmath.app/club)

Vivek Nathani 在班加罗尔创办了一个数学俱乐部，以重拾他大学毕业后失去的协作学习环境。他发现孤立地学习数学不如与同伴一起讨论问题和学习的共享体验那样令人满足。

该俱乐部已经在科尔曼加拉的 Dialogues Cafe 成功举办了两次聚会。第一次聚会于 2025 年 3 月 15 日举行，有 7 名参与者，第二次聚会于 2025 年 5 月 4 日举行，吸引了 8 名参与者。参与者们一起解决问题集。

Vivek 感谢 @clearlysid 和 @lifeofadvait 鼓励和帮助他创办俱乐部，以及 @Sarve___tanvesh 帮助举办第二次聚会。他鼓励任何有兴趣加入数学俱乐部的人通过电子邮件 viveknathani2402 at gmail[dot]com 或在 Twitter 上 @viveknathani_ 与他联系。

---

## 57. 他花费数千：银行团队如何尝试拯救诈骗受害者

**原文标题**: 'He spent thousands': how a bank team tries to rescue scam victims

**原文链接**: [https://www.theguardian.com/money/2025/feb/01/bank-team-scam-victims-fraud](https://www.theguardian.com/money/2025/feb/01/bank-team-scam-victims-fraud)

桑坦德银行“破咒”团队如何解救受复杂诈骗侵害的客户——尤其是在疫情期间激增的爱情和投资诈骗——本文对此进行了详细阐述。这个由23名专家组成的团队处理那些深受诈骗分子蛊惑、不愿相信自己被骗的客户。他们调查可疑交易，联系受害者，并在数周或数月内建立信任，以打破这种“魔咒”。

文章强调了这些诈骗的复杂性和情感操控，这些诈骗通常针对孤独、沮丧或丧亲等脆弱人群。诈骗分子在复杂的呼叫中心运作，利用社交媒体上的个人数据建立虚假连接并榨取金钱，先从小额请求开始，然后升级到大额款项，有时甚至导致受害者重新抵押房屋。

“破咒”团队不仅阻止了进一步的财务损失，已经阻止了1760万英镑落入诈骗者手中，而且在受害者意识到自己被骗后，还会为他们提供持续的支持，认识到由此产生的重大心理影响。“银行协议”计划鼓励在必要时警方介入。由于最近的规则变更要求银行赔偿非因重大过失的诈骗受害者，预防和干预变得更加紧迫。文章强调了同理心和理解在打击这些诈骗中的重要性，并强调任何人都有可能成为受害者。

---

## 58. 闪回：Flash的“口述”历史

**原文标题**: Flash Back: An “oral” history of Flash

**原文链接**: [https://goodinternetmagazine.com/oral-history-of-flash/](https://goodinternetmagazine.com/oral-history-of-flash/)

本文以“口述”历史的方式探讨了Flash在互联网上的兴衰。 Flash诞生于人们对早期HTML所能提供的更丰富的多媒体和交互性的渴望，由于其文件体积小、跨平台兼容性以及能够交付动画、游戏甚至成熟的应用程序的能力，Flash迅速普及。它为创意表达提供了可能，尤其是在动画和独立游戏开发领域，为许多创作者和热门作品提供了跳板。作者强调了Flash的积极影响，尤其是在个人创意活动和Steam等平台占据主导地位之前的独立游戏领域。

然而，本文也强调了Flash的重大缺陷。 其专有性质将控制权置于单一公司（Macromedia/Adobe）手中，阻碍了开放标准。 安全漏洞困扰着该插件，并且以性能问题而臭名昭著，即使在空闲时也会消耗CPU功率。 Flash还造成了无障碍访问障碍，阻碍了屏幕阅读器，并使得包含大量Flash的网站难以索引和存档。

最终，iPhone等移动设备的兴起（iPhone因拒绝Flash而闻名）以及HTML、CSS和JavaScript的进步促成了Flash的衰落。 本文的结论是，尽管Flash提供了显著的进步，但其固有的缺陷以及Web技术的演进使得它的最终替代成为必然。 它承认Flash在塑造互联网早期多媒体格局方面的重要作用，同时也承认了其消亡所带来的解脱。

---

## 59. Nova：用 Rust 编写的 JavaScript 和 WebAssembly 引擎

**原文标题**: Nova: A JavaScript and WebAssembly engine written in Rust

**原文链接**: [https://trynova.dev/](https://trynova.dev/)

Nova：一个用 Rust 开发的、强调数据导向设计的 JavaScript 和 WebAssembly 引擎。该项目目前处于实验阶段，旨在探索并验证这种引擎架构的可行性。虽然仍在开发中，且仅通过了约 70% 的 test262 测试套件，但进展正在积极进行。开发团队鼓励通过他们的 GitHub 仓库和 Discord 服务器参与和讨论。该项目通过博客文章展示进展和见解，最近的文章涵盖了诸如为互联网工作、Nova 的垃圾回收器、内存管理以及对过去和未来目标的反思等主题。

---

## 60. 我的网站很丑，因为是我做的。

**原文标题**: My website is ugly because I made it

**原文链接**: [https://goodinternetmagazine.com/my-website-is-ugly-because-i-made-it/](https://goodinternetmagazine.com/my-website-is-ugly-because-i-made-it/)

泰勒·特罗什的文章《我的网站很丑，因为是我做的》探讨了创建网站的个人表达性，优先考虑个人表达而非传统的优秀设计。他认为，虽然存在精致、专业设计的网站，但他自己网站的价值在于它反映了他独特的个性和创造性冲动。

特罗什强调了他渴望构建与他的特定兴趣相符的东西，包括幽默、系统、生活和软件，并使用 HTML/CSS 和其他媒介来表达他的情感。他强调他的网站是他内心感受和创造性驱动力的直接产出。

文章详细描述了他网站设计的演变，解释了他最初对简洁的追求以及最终演变成可控混乱的过程。他提供了具体的 CSS 代码片段，以说明他如何有意识地融入看似随机的元素，如旋转、不同的字体、字母间距，甚至是用 CSS-doodle 创建的“布满灰尘的纸张”纹理。选择这些元素不是因为它们的美学吸引力，而是因为它们的个人意义以及它们唤起的感觉。

最终，特罗什赞扬了他的网站的迭代和发展特性，认识到它将随着他自己的变化而不断变化。他鼓励其他人拥抱他们自己的“丑陋之物”，认为个人表达和持续成长比遵守传统设计标准更有价值。他还将自己描述为拥抱不完美并在其最原始的形式中庆祝创造力的人。

---

## 61. Show HN: Onlook – 面向设计师的开源、可视化优先光标

**原文标题**: Show HN: Onlook – Open-source, visual-first Cursor for designers

**原文链接**: [https://github.com/onlook-dev/onlook](https://github.com/onlook-dev/onlook)

Onlook：面向设计师的开源可视化优先代码编辑器，旨在成为 Bolt.new 和 Webflow 等工具的替代方案。它允许用户在 Next.js + TailwindCSS 环境中使用 AI 制作网站、原型和设计，提供可视化编辑器以进行直接 DOM 操作和实时代码集成。Onlook 目前正在进行 Web 开发，使用户能够从文本、图像、模板、Figma 导入或 GitHub 存储库快速创建 Next.js 应用程序。

主要功能包括具有类似 Figma UI 的可视化编辑、实时预览、品牌资产管理、图层浏览、组件检测、页面创建和图像管理。该工具还提供实时代码编辑、保存/恢复检查点、CLI 命令和应用市场集成。通过可共享的链接和自定义域名链接简化了部署，并通过实时编辑和评论促进团队协作。

Onlook 的架构涉及将代码加载到 Web 容器中，通过 iframe 提供服务，并检测代码以将元素映射到其相应的代码位置。编辑会反映在 iframe 和代码中。AI 聊天也具有代码访问权限，以便进行理解和编辑。该项目采用 Next.js、Supabase、Drizzle、TailwindCSS、Bun 和 tRPC 构建，并欢迎通过拉取请求和提交问题进行贡献。

---

## 62. 修复查理二世的女仆

**原文标题**: The Maid Who Restored Charles II

**原文链接**: [https://www.historytoday.com/archive/feature/maid-who-restored-charles-ii](https://www.historytoday.com/archive/feature/maid-who-restored-charles-ii)

安妮·蒙克：被忽视的查理二世复辟关键人物

---

## 63. 不快乐的餐点 (2007)

**原文标题**: Unhappy Meals (2007)

**原文链接**: [https://michaelpollan.com/articles-archive/unhappy-meals/](https://michaelpollan.com/articles-archive/unhappy-meals/)

在《不快乐的食物》中，迈克尔·波伦认为，对营养成分的关注胜过对完整食物的关注，导致了人们对饮食的困惑和焦虑。他批判了“营养主义”的兴起，这是一种将食物主要视为营养来源的意识形态，导致人们忽视食物之间的质量差异，并过度强调专家建议。

波伦追溯了从食用“食物”到摄取“营养成分”的转变，认为这源于 20 世纪 70 年代的一场政治争议，当时由于行业压力，关于减少红肉消费的膳食指南被修改。这导致人们关注饱和脂肪等个别营养成分，从而避免了关于完整食物的直接建议。

波伦认为，营养主义有利于食品工业，使他们能够用特定的营养成分重新配制加工食品，以利用健康趋势，而完整食物难以与之竞争。这种对营养成分的关注也赋予了科学家和记者权力，他们为公众解读“食物的隐藏现实”，进一步复杂化了我们对饮食的理解。他认为，这种通过营养成分关注健康的痴迷，反而会通过忽视饮食的社会性和愉悦性来破坏我们的福祉。最终，波伦提倡一种更简单的方法：“吃食物。不要太多。主要吃植物。”

---

## 64. 带有离线可用浏览器IDE的简易编程语言

**原文标题**: Simple programming language with offline usable browser IDE

**原文链接**: [https://tiki.li/apps/tut_learn.html?v=2505e](https://tiki.li/apps/tut_learn.html?v=2505e)

本文探讨了一种可在离线浏览器集成开发环境（IDE）中使用的简单编程语言的概念。文章旨在介绍编程基础知识，可能通过这种新语言。标题表明该语言的设计注重易用性，而IDE的离线功能允许在没有互联网连接的情况下进行开发。“Tiki”的存在和“Loading...”加载消息暗示该文章可能是一个名为“Tiki”的更大系统或平台的一部分，并且读者目前正在等待此平台中加载更多内容。核心思想是提供一种易于访问的编程学习体验，使用户能够使用一种随时可用且不受互联网连接限制的工具。

---

## 65. 入侵 Huum Uku WiFi 控制器

**原文标题**: Invading the Huum Uku WiFi Controller

**原文链接**: [https://kaurpalang.com/posts/invading-the-sauna/](https://kaurpalang.com/posts/invading-the-sauna/)

本文详细介绍了通过逆向工程，实现在本地控制Huum Uku WiFi桑拿控制器的过程，从而摆脱对Huum云服务的依赖。作者对依赖云的“智能”设备感到不满，旨在不使用官方Huum应用程序远程控制桑拿。

作者首先分析了控制器与Huum服务器之间的网络流量，最初使用Wireshark在一台充当控制器热点的笔记本电脑上进行。他们发现通信没有使用TLS加密，从而暴露了明文消息。作者识别了几种关键消息类型，包括用于设置温度、控制加热器和报告桑拿状态的消息。作者推测通信可能通过MQTT进行。

然后，他们使用AdGuard Home重写api.huum.eu的DNS记录，将控制器的流量重定向到本地服务器。作者发现通信不是WebSocket而是原始TCP。作者随后编写了一个Bun服务器来模拟Huum的云，成功地向控制器发送命令并接收状态更新。他们创建了一个REST API来控制加热器。该项目成功避免了云端并实现了本地控制，并确定了五种用于此目的的通信协议。

作者对缺乏TLS加密表达了复杂的情感，既承认了它对逆向工程的便利性，也承认了它构成的潜在安全风险。最后，作者概述了后续步骤，包括发布GitHub版本，并可能尝试控制该区域的其他加热器。

---

## 66. 高质量OLED显示屏现已实现集成超薄多声道音频

**原文标题**: High-quality OLED displays now enabling integrated thin and multichannel audio

**原文链接**: [https://www.sciencedaily.com/releases/2025/05/250521125055.htm](https://www.sciencedaily.com/releases/2025/05/250521125055.htm)

无法访问文章链接。

---

## 67. 谷歌地图错误显示德国高速公路关闭，引发混乱

**原文标题**: Chaos on German autobahns as Google Maps wrongly says they are closed

**原文链接**: [https://www.theguardian.com/world/2025/may/30/chaos-on-german-autobahns-as-google-maps-wrongly-says-they-are-closed](https://www.theguardian.com/world/2025/may/30/chaos-on-german-autobahns-as-google-maps-wrongly-says-they-are-closed)

谷歌地图错误地显示德国高速公路在大假日前夕大范围关闭，造成混乱。司机们看到地图上布满了停车标志，显示法兰克福、汉堡、柏林和其他地区的主要高速公路关闭，并延伸到比利时和荷兰。

这一错误信息导致替代路线严重拥堵，因为司机们争相寻找绕行路线。警察和交通部门接到了大量询问。其他导航应用程序，如苹果地图和Waze，以及交通广播，都显示正常的交通流量，突显了谷歌地图的错误。

社交媒体用户表达了不满，并猜测原因，从恐怖事件到黑客攻击。谷歌正在调查此事，声明其地图数据依赖于第三方供应商、公共来源和用户输入。该公司承认了该问题，并正在努力删除不正确的关闭标志。谷歌建议道路使用者在计划未来的旅行时查阅多个信息来源。

---

## 68. 基于体域偏微分方程的无网格方法 [pdf]

**原文标题**: Grid-Free Approach to Partial Differential Equations on Volumetric Domains [pdf]

**原文链接**: [http://rohansawhney.io/RohanSawhneyPhDThesis.pdf](http://rohansawhney.io/RohanSawhneyPhDThesis.pdf)

该文档似乎是一个PDF文件，包含一篇题为“体积域上偏微分方程的无网格方法”的研究文章的内容。然而，提供的文本是PDF的原始压缩内容，无法直接阅读。

根据标题，我们可以推断出大致主题：

*   **偏微分方程 (PDEs):** 该文章可能讨论求解这些方程的方法，这些方程是各种物理现象建模的基础。
*   **体积域:** 重点是在三维空间内求解偏微分方程。
*   **无网格方法:** 这表明该方法*不*依赖于传统的基于网格的离散化技术（如有限差分或有限元方法）。无网格方法可以在处理复杂几何形状、自适应性以及潜在的更高阶精度方面提供优势。

没有实际内容，无法提供更多细节。该文章可能深入探讨所提出的无网格方法的具体细节，包括：

*   其数学公式。
*   实施细节。
*   与现有方法的性能比较。
*   应用于特定问题（例如，热传递、流体动力学、电磁学）。
*   关于准确性、稳定性和计算成本的讨论。

---

## 69. 90年代网页设计大师：泽尔德曼、西格尔、尼尔森

**原文标题**: Gurus of 90s Web Design: Zeldman, Siegel, Nielsen

**原文链接**: [https://cybercultural.com/p/web-design-1997/](https://cybercultural.com/p/web-design-1997/)

理查德·麦克马纳斯的文章通过杰弗里·泽尔德曼、大卫·西格尔和雅各布·尼尔森这三位有影响力的人物，考察了90年代末期网络设计理念的分歧。随着CSS和Flash的出现，这些“大师”提供了截然不同的方法。

西格尔是一位数字排版专家，他提倡使用诸如隐形表格和单像素GIF之类的“技巧”来实现审美目标，甚至优先考虑特定浏览器（Netscape）。他拥抱Flash的视觉功能，尽管它具有专有性质。尼尔森是一位“可用性大师”，他倡导跨浏览器的语义编码和可访问性，主张将内容与表现分离，并最终支持CSS。他强烈反对Flash。泽尔德曼则介于两者之间，最初同时拥抱CSS和Flash，认为设计既可以美观又符合标准。

文章强调了优先考虑视觉效果（西格尔，最初的泽尔德曼）与可用性和可访问性（尼尔森，后来的泽尔德曼）之间的紧张关系。Flash提供了立竿见影的视觉冲击力，但牺牲了语义代码和标准。CSS虽然前景广阔，但面临着浏览器支持不一致的问题。

文章随后追踪了这些大师们的后续职业生涯。尼尔森的极简主义Useit网站成为了过时设计的象征，最终并入了他的NNGroup。西格尔探索了商业、区块链和其他领域。泽尔德曼仍然是一位网页设计师，目前在Automattic工作，这表明他结合标准和设计感性的平衡方法可以说“胜出”了。文章最后以泽尔德曼重新设计其网站的令人兴奋的消息作为结尾，暗示着他对原始设计理念的重新关注，并希望它能得到更广泛的采用。

---

## 70. 净负光标

**原文标题**: Net-Negative Cursor

**原文链接**: [https://lukasatkinson.de/2025/net-negative-cursor/](https://lukasatkinson.de/2025/net-negative-cursor/)

Lukas Atkinson 评 Cursor Editor 网站上的一个例程，批评了 AI 辅助开发工具。文章指出，在这个例子中，AI 生成的代码修改（旨在改进读取长度分隔字符串的 Rust 函数）实际上是有害的，并降低了生产力。

AI 建议添加长度验证和清理。Atkinson 指出，长度验证是无用的，因为 `u16` 已经限制了字符串长度，而清理在风格上（不必要的分配，晦涩的字符字面量）和正确性上都值得怀疑（对空格的任意处理，可能破坏应用程序，并且与镜像的 `write_string()` 函数不兼容）。

Atkinson 认为，AI 工具在没有提供做出明智选择的必要上下文的情况下做出了次优的决策，导致代码要么是无用的，要么是微妙的错误。他强调，编程涉及无数的决策，虽然 AI 工具可以帮助处理样板代码，但它们也应该标记出需要人工审核的重要决策。

最终，Atkinson 认为，当 AI 工具生成有缺陷的代码，需要进行大量的审查和讨论时，即使在 Cursor 认为的 AI 辅助编码的展示案例中，它们也会对生产力产生“净负面”影响。他总结说，当前的 AI 工具通常无法提供有效编程所需的必要上下文和知情决策支持。

---

## 71. 世界线：狭义相对论可视化 (2010)

**原文标题**: Worldlines: Visualizing Special Relativity (2010)

**原文链接**: [https://worldlines.sourceforge.net/#source-code](https://worldlines.sourceforge.net/#source-code)

世界线：狭义相对论可视化 是一个使用 Processing 编程语言创建狭义相对论概念的交互式可视化项目的工具。 该项目旨在通过视觉表示使这些复杂的概念更易于理解和掌握。

该项目的关键特性包括：

*   **交互式可视化：** 项目的核心在于相对论现象的动态视觉表示，允许用户操纵参数并观察其对世界线和其他元素的影响。
*   **手册：** 该项目包含一本手册（提供 PDF 和 HTML 格式），据推测其中解释了基本物理原理以及如何使用可视化工具。
*   **应用程序（App）：** 提供适用于 Windows、macOS 和 Linux 的即用型应用程序，提供了一种用户友好的方式来与可视化工具交互，而无需编写代码。
*   **源代码：** 源代码可在 GitHub 上获取，允许用户探索实现细节、修改可视化效果并为项目做出贡献。
*   **组件：** 源代码列表表明采用模块化设计，类/组件专注于模拟的特定元素，例如轴、参考系、几何图形、粒子和相对论计算本身。
*   **联系方式：** 该项目通过 Twitter 和电子邮件提供联系信息。

本质上，“世界线” 是一种教育工具，旨在通过使用 Processing 构建的交互式视觉模拟来帮助学习和理解狭义相对论。

---

## 72. Show HN: 我做了一个零配置代码可视化工具

**原文标题**: Show HN: I made a Zero-config tool to visualize your code

**原文链接**: [https://staying.fun/en](https://staying.fun/en)

此“Show HN”提交介绍了一个零配置代码可视化平台。该工具旨在帮助用户，特别是学生、教育工作者和开发者，实时可视化他们的代码。它支持Python、JavaScript和C++，并强调数据结构和算法的可视化。其主要卖点是其“零配置”特性，表明易于使用和快速设置。该平台承诺促进学习，提高编码效率，并允许用户可视化和记录他们的代码。

---

## 73. 加州擅长建造巨型电池。

**原文标题**: California has got good at building giant batteries

**原文链接**: [https://www.economist.com/united-states/2025/05/22/california-has-got-really-good-at-building-giant-batteries](https://www.economist.com/united-states/2025/05/22/california-has-got-really-good-at-building-giant-batteries)

加州已成为大规模电池储能领域的领导者，尤其是在可再生能源基础设施集中的东部克恩县等地区。这些巨大的电池，外形酷似集装箱，对于储存风能和太阳能发电至关重要。在高峰时段，这些电池可满足该州 30% 的电力需求。 例如，Eland 太阳能和储能项目就采用了特斯拉电池，突显了电池技术在加州与其他可再生能源并存的日益增长的地位。

---

## 74. 减少亨廷顿舞蹈症相关重复序列在患者细胞和小鼠中的扩增

**原文标题**: Reducing Huntington’s-related repeat expansions in patient cells and in mice

**原文链接**: [https://www.nature.com/articles/s41588-025-02172-8](https://www.nature.com/articles/s41588-025-02172-8)

本文探讨了一种针对三核苷酸重复序列 (TNR) 疾病（如亨廷顿病 (HD) 和弗里德赖希共济失调 (FRDA)）的新型治疗方法，这些疾病由扩展且不稳定的 TNR 序列（分别为 CAG•CTG 和 GAA）引起。研究人员利用碱基编辑这种精确的基因组编辑技术，在这些致病重复序列内引入中断，模拟在健康个体中发现的天然存在的稳定变异体。

他们使用胞嘧啶和腺嘌呤碱基编辑器（CBE 和 ABE）分别在 CAG 和 GAA 重复序列处产生 G•C>A•T 和 A•T>G•C 替换。在 HEK293T 细胞中进行的体外实验表明，使用优化的 CBE（如 EA-evoA-32NLS）可以有效地编辑 CAG 重复序列。将这种 CAG-CBE 策略应用于 HD 患者来源的成纤维细胞，可显著中断致病性 CAG 重复序列，并且至关重要的是，可在 30 天内阻止体细胞重复序列的扩展，甚至促进重复序列的收缩。

在 HD 和 FRDA 小鼠模型（分别为 Htt.Q111 和 YG8s）中进行的体内实验，使用 AAV9 递送碱基编辑器显示，在转导的组织中实现了有效编辑，并减少了中枢神经系统中重复序列的扩展。该研究还调查了 CAG-CBE 策略的潜在脱靶效应，绘制了因序列相似性而被靶向的基因组位点。总的来说，该研究证明了碱基编辑通过诱导致病性 TNR 序列束中的中断，促进其稳定和收缩，从而减轻 TNR 疾病的关键神经特征的潜力。

---

## 75. 三维内战：来自纽约历史学会的立体照片 (2015)

**原文标题**: Civil War in 3D: Stereographs from the New-York Historical Society (2015)

**原文链接**: [https://www.nyhistory.org/blogs/civil-war-in-3d-stereographs-from-the-new-york-historical-society](https://www.nyhistory.org/blogs/civil-war-in-3d-stereographs-from-the-new-york-historical-society)

纽约历史学会文章探讨其将700多幅美国内战立体照片数字化，使其可在线访问。立体照片在内战时期风靡一时，它结合了两张略有偏移的照片，通过立体镜观看时可形成三维图像。文章详细介绍了立体照片的历史，认为查尔斯·惠斯通爵士发明了它，而奥利弗·温德尔·霍姆斯创造了这个术语并改进了观看器。

文章重点介绍了马修·布雷迪及其公司作为通过摄影记录内战的关键人物，并指出布雷迪可能雇用了许多摄影师来捕捉这场冲突。亚历山大·加德纳和蒂莫西·H·奥沙利文也是该时期著名的摄影师，他们也被提及为该收藏的贡献者。许多图像描绘了战争造成的破坏和死亡。

文章随后探讨了由于古董立体镜的稀缺，以其预期格式观看这些图像的挑战。它强调了现代解决方案，例如纽约公共图书馆的Stereogranimator，该工具可以从立体照片创建动画GIF和浮雕图片，以及Google Cardboard，它允许使用智能手机和纸板观看器观看立体照片。作者最后强调了体验这些历史3D图像的持久新颖性和影响力，使现代观众能够与内战时期的事件和人物联系起来。文章提供了访问数字化馆藏的链接。

---

## 76. 在Polymarket上下注耶稣何时归来的用户

**原文标题**: The Polymarket users betting on when Jesus will return

**原文链接**: [https://ericneyman.wordpress.com/2025/03/24/will-jesus-christ-return-in-an-election-year/](https://ericneyman.wordpress.com/2025/03/24/will-jesus-christ-return-in-an-election-year/)

埃里克·内曼探讨了人们为何在Polymarket上押注耶稣基督将在2025年回归，尽管可能性似乎很低。他强调，交易员已押注超过10万美元，推动市场交易额达到3%左右。

内曼否定了简单的解释，例如真诚的信仰、对市场错误解决的期望，或者仅仅是娱乐（“迷因”）。他认为，原因并非是对实际事件的相信，而是押注于“Polymarket现金的时间价值”。

核心论点是，今年晚些时候，其他市场（例如选举、地缘政治事件）的活跃度增加可能导致交易员迫切需要资金来押注这些事件。这种需求的增加可能会推高“否”股票（反对耶稣回归的赌注）的价格，从而使“是”投注者能够出售他们的股票以获取利润，即使耶稣没有回归。

内曼以2024年选举为例，在安全州的候选人赌注在选举日价格飙升，因为交易员试图释放资金用于其他投注。因此，耶稣市场成为衡量今年Polymarket资金预期需求的指标，尤其是在交易活动高峰期。他得出结论，耶稣市场的定价是Polymarket生态系统中货币时间价值的指标，不一定反映了对耶稣再临的信仰。

---

## 77. RSyncUI – 基于SwiftUI的macOS rsync图形界面

**原文标题**: RSyncUI – A SwiftUI based macOS GUI for rsync

**原文链接**: [https://github.com/rsyncOSX/RsyncUI](https://github.com/rsyncOSX/RsyncUI)

RsyncUI 是一款 macOS 应用程序，为命令行工具 `rsync` 提供图形用户界面 (GUI)，用于同步数据。RsyncUI 使用 SwiftUI 构建，需要 macOS Sonoma 或更高版本，它通过用户友好的界面允许用户组织任务和设置参数，从而简化了 `rsync` 的使用。该应用程序本身不执行同步；而是使用后台的 `rsync` 命令行工具。

当前版本 v2.5.5（发布于 2025 年 5 月 23 日）正在积极开发中。用户可以通过 Homebrew 使用命令 `brew install --cask rsyncui` 安装 RsyncUI，或者直接下载它。该应用程序已由 Apple 签名和公证，以确保安全。

重要的是，`rsync` 的执行是由 RsyncUI 监控的外部进程。用户可以中止正在运行的任务，但必须允许中止完全完成，以防止潜在的无响应。提供的文档基于 Docsy Hugo 主题的一个分支。

---

## 78. 航空公司向单独旅客收取的票价比团体旅客高。

**原文标题**: Airlines are charging solo passengers higher fares than groups

**原文链接**: [https://thriftytraveler.com/news/airlines/airlines-charging-solo-travelers-higher-fares/](https://thriftytraveler.com/news/airlines/airlines-charging-solo-travelers-higher-fares/)

包括美国航空、达美航空和联合航空在内的航空公司，在某些国内航线上，对单人旅行者收取的费用高于两人或两人以上的团体。这种定价策略并不普遍，但经 Thrifty Traveler 的机票交易分析师证实。价格差异可能很大，有例子显示，预订多名乘客时，单程机票价格下降了近三分之一。

航空公司通过根据乘客人数开放不同的票价等级来实现这一点。例如，单人旅行者可能只能看到“折扣经济舱”票价，而团体预订可以解锁“深度折扣经济舱”机票。票价规则甚至明确规定，更便宜的机票需要另一位成人陪同。

这背后的原因很可能是“细分”，航空公司以此锁定商务旅客，因为他们被认为对价格不太敏感，因为有公司差旅预算。然而，这惩罚了其他单人旅行者，例如那些因紧急情况旅行或探亲的人。

这种定价策略主要见于单程国内航班，而不是往返或国际航线，而且并非所有主要的美国航空公司（如阿拉斯加航空、捷蓝航空或西南航空）都采用这种策略。航空公司尚未对此做法发表评论，但这凸显了航空公司根据客户资料定制价格的日益增长的趋势。这种变化可能会让许多旅行者措手不及，因为批量折扣对于航空公司来说并不常见，尤其是只预订两名乘客。

---

## 79. MariaDB 收购 Galera Cluster

**原文标题**: MariaDB Acquires Galera Cluster

**原文链接**: [https://mariadb.com/newsroom/press-releases/mariadb-acquires-galera-cluster/](https://mariadb.com/newsroom/press-releases/mariadb-acquires-galera-cluster/)

MariaDB plc 收购高可用数据库解决方案 Galera Cluster 背后的公司 Codership Oy。此次收购将核心 Galera 团队和创始人纳入 MariaDB，从而加强了 MariaDB 的欧洲工程和技术支持团队。九年多来，Galera Cluster 一直是 MariaDB Server 的标准组成部分，超过三分之一的 MariaDB Enterprise Platform 客户已经在使用它。

此次收购旨在增强 MariaDB 的高可用性和高级复制能力，以满足客户对高容量生产环境中零数据丢失日益增长的需求。MariaDB 表示，整合 Galera Cluster 将使他们能够提供更高水平的支持并加速创新。

短期内，MariaDB 和 MySQL 版本的 Galera Cluster 都将得到维护。自从被 K1 Investment Management 私有化并任命 Rohit de Souza 为 CEO 以来，MariaDB 一直在加大对创新的投资，包括推出开源向量搜索功能和新的 MariaDB Enterprise Platform 版本。该公司还因其开源向量搜索而荣获 2025 年 AI TechAward。

---

## 80. 域/操作系统设计原则 (1989) [pdf]

**原文标题**: Domain/OS Design Principles (1989) [pdf]

**原文链接**: [http://www.bitsavers.org/pdf/apollo/014962-A00_Domain_OS_Design_Principles_Jan89.pdf](http://www.bitsavers.org/pdf/apollo/014962-A00_Domain_OS_Design_Principles_Jan89.pdf)

由于提供的不是人类可读的内容，而是二进制数据，我无法总结文章。提供的文本似乎是PDF文件的内部结构，而不是文章的文本。

---

## 81. “不可判定”到底是什么意思

**原文标题**: What does “Undecidable” mean, anyway

**原文链接**: [https://buttondown.com/hillelwayne/archive/what-does-undecidable-mean-anyway/](https://buttondown.com/hillelwayne/archive/what-does-undecidable-mean-anyway/)

本文面向技术知识有限的读者解释计算机科学中“不可判定性”的概念。文章首先将“可判定”问题定义为图灵机始终能正确判断输入字符串是否满足给定属性（接受）或不满足（拒绝）的问题。

作者阐明，此模型涵盖了广泛的问题，因为字符串可以表示任何数据，并且非布尔输出可以伪造。虽然像DFA这样的较弱模型无法解决所有问题，但图灵机（TM）在理论上是最强大的，Church-Turing论题指出，如果现实世界的编程语言可以解决一个问题，那么TM也可以。

TM的一个关键方面是它们能够模拟其他TM，从而可以组合并解决关于其行为的决策问题。文章接着将“不可判定”问题定义为没有任何图灵机能够完全解决的问题；不存在可以*总是*确定程序是否对于任何任意程序停止的算法。

文章强调，不可判定性并不意味着问题的*所有*实例都无法解决，而只是通用的解决方案是不可能的。不可判定性迫使我们花费大量精力并面临潜在的失败，才能确定程序是否具有特定属性。作者最后描述了一个所有问题都是可判定的世界会是什么样子，突出了形式验证会变得多么容易。

---

## 82. Memvid – 基于视频的AI记忆

**原文标题**: Memvid – Video-Based AI Memory

**原文链接**: [https://github.com/Olow304/memvid](https://github.com/Olow304/memvid)

Memvid：一种新型AI内存管理方法，将文本数据编码为视频文件，提供了一种轻量高效的替代传统向量数据库的方案。它能在单个MP4文件中存储的数百万个文本块中实现亚秒级的语义搜索。这种“视频即数据库”的方法与传统方法相比，压缩率高达10倍，从而最大限度地减少了RAM和存储需求。

主要功能包括语义搜索能力、内置聊天界面、PDF支持、离线功能以及简单的API。Memvid与各种LLM（OpenAI、Anthropic、本地模型）兼容，并且需要最少的infrastructure。用例范围从数字图书馆和教育内容到企业知识库和个人笔记。

该轻量级架构用大约1000行Python代码实现，对CPU友好且可移植，整个知识库都包含在单个可流式传输的视频文件中。可以通过`pip install memvid`直接安装。文档提供了基本用法、从文档构建记忆、高级搜索以及创建交互式聊天界面的示例。高级配置选项包括自定义嵌入、视频优化技术和分布式处理。文档还包括故障排除、贡献指南、与传统解决方案的比较、概述未来发展方向的路线图以及致谢。

---

## 83. 从有限整环到有限域

**原文标题**: From Finite Integral Domains to Finite Fields

**原文链接**: [https://susam.net/from-finite-integral-domains-to-finite-fields.html](https://susam.net/from-finite-integral-domains-to-finite-fields.html)

本文探讨了抽象代数中域与整环之间的关系，特别关注有限性对它们的影响。文章首先将整环定义为一个具有不同加法单位元和乘法单位元的交换环，且没有零因子。整环的例子包括整数 (ℤ)、有理数 (ℚ) 以及整环上的多项式 (R[t])。本文确立了*a* ⋅ 0 = 0 和消去律等关键性质。它阐明了整环必须是一个非零环 (0 ≠ 1)。

本文的核心论点在于证明每个域都是一个整环。然而，反之并不总是成立。整数 (ℤ) 就是一个反例：它们构成一个无限整环，但不是一个域。值得注意的是，本文证明了*每个有限整环都是一个域*。文章提供了两种证明方法。第一种方法利用了消去律和鸽巢原理。第二种证明方法避免了使用消去律，同样使用鸽巢原理得出相同的结论。

文章最后总结了关键发现：所有域都是整环，所有有限整环都是域，一些无限整环是域（例如，ℚ、ℝ、ℂ），一些无限整环不是域（例如，ℤ）。结构与大小之间的相互作用表明，有限性条件将整环转换为域。

---

## 84. 唯一正确的Lisp风格指南

**原文标题**: The-One-True-Lisp-Style-Guide

**原文链接**: [https://github.com/foxsae/The-One-True-Lisp-Style-Guide](https://github.com/foxsae/The-One-True-Lisp-Style-Guide)

唯一Lisp风格指南：本指南旨在整合现有Common Lisp风格指南中的共识，创建一套简化且普遍接受的建议。它综合了来自Peter Norvig和Kent Pitman的教程、lisp-lang.org风格指南、Google Common Lisp风格指南等资料的建议。

本指南强调风格指南对于提高可读性和防止常见编程错误的重要性。主要共识包括：

*   **文档：** 文档字符串至关重要，应解释代码元素的用途。
*   **注释约定：** 使用分号的分层系统来表示不同级别的注释（行内、顶层、区域特定、标题）。
*   **行长：** 行长应限制在100个字符以下，越短越好。
*   **命名约定：** 名称应具有描述性、简洁、小写、用连字符分隔，特殊变量使用`*`，常量使用`+`。
*   **函数定义：** 尽量避免混合使用`&OPTIONAL`和`&KEY`参数。
*   **特殊变量：** 谨慎使用。
*   **缩进：** 依赖于正确配置的编辑器的缩进标准。
*   **函数式风格：** 编写具有单一、明确用途的函数。
*   **Eval的使用：** 除非绝对必要，否则应避免使用`Eval`。
*   **宏：** 理解宏比定义宏更重要。
*   **:use的使用：** 除非需要所有符号，否则`:import-from`更可取。
*   **错误检测：** 了解条件和错误之间的区别。
*   **库的使用：** 鼓励使用。
*   **递归：** 除了递归数据结构外，优先选择迭代而不是递归。
*   **类型检查：** 在已知类型时显式声明类型。
*   **条件表达式：** 使用`when`或`unless`代替没有`else`的`if`，使用`cond`进行多分支语句。
*   **谓词：** 谓词后缀使用“p”或“-p”。
*   **滥用列表：** 为每种情况使用适当的数据结构。

---

## 85. 原生 Web 组件

**原文标题**: Vanilla Web Components

**原文链接**: [https://github.com/vanillawc](https://github.com/vanillawc)

“原生Web Components”组织是由一群开发者组成的团体，致力于仅使用原生WC规范，不依赖额外的抽象层、依赖项或复杂的构建过程，来创建、分享和推广Web Components（WC）。其目标是探索WC标准“底层”API的潜力并解决对其的批评。

该组织展示了各种原生WC实现，涵盖箭头、轮播图、代码编辑器、日期选择器、JSON查看器、Markdown渲染器等功能。

欢迎通过GitHub上的Showcase、Proposal和Discussion issue提交贡献。鼓励贡献者在仓库名称前加上"wc-"前缀，封装代码，优先考虑可重用性和可访问性，并使用像MIT这样对Copyleft友好的许可协议。还强调避免额外的抽象层、复杂的构建步骤和人身攻击。

本文档提供了指向各种Web Components社区（W3C、WebComponents.org、Open-WC.org）、GitHub和CloudFour等公司Web Component使用案例研究、来自各个组织（GitHub、Adobe、宾夕法尼亚州立大学、荷兰国际集团银行、红帽、波士顿大学）的Web Components集合以及用于学习更多关于Web Components的资源（包括MDN文档）的链接。该存储库采用双重许可，源代码使用MIT许可，书面内容和资产使用CC-BY-SA-4.0许可。

---

## 86. 展示HN：Weather2Geo – 从天气小部件的截图中进行地理定位

**原文标题**: Show HN: Weather2Geo – Geolocate screenshots from weather widgets

**原文链接**: [https://github.com/elliott-diy/Weather2Geo](https://github.com/elliott-diy/Weather2Geo)

Weather2Geo：一款基于天气信息的截图地理定位开源情报工具。通过输入截图中的时间、天气状况和温度，该工具利用MSN天气API（与Windows小部件相同的后端）和GeoNames城市数据库，识别符合条件的城市。该工具具有时区感知功能，可将输入时间本地化为每个城市的时区以确保准确性。它还包括聚类功能，对附近的匹配结果进行分组，以减少噪声并突出显示潜在位置。用户可以通过调整温度容差、聚类距离和城市数据源来自定义该工具。安装过程简单，包括克隆GitHub存储库和安装所需的Python软件包。该工具从命令行运行，指定时间、状况、温度以及可选参数，如容差和聚类距离。Weather2Geo旨在用于符合伦理道德的教育目的开源情报，并鼓励贡献者改进匹配准确性、时区逻辑和数据源。该项目欢迎错误报告、建议和拉取请求。

---

## 87. Debian AI 通用决议撤回

**原文标题**: Debian AI General Resolution Withdrawn

**原文链接**: [https://lwn.net/Articles/1020968/](https://lwn.net/Articles/1020968/)

2025年5月，Debian开发者周摩撤回了他提出的通用决议（GR），该决议原本要求AI模型的原始训练数据必须发布，才能被视为符合Debian自由软件指南（DFSG）。该提案旨在确保Debian主仓库中的AI模型符合DFSG。

周摩的提案与开源促进会（OSI）的开源人工智能定义（OSAID）形成对比，后者不要求发布训练数据。出现了几个反提案，包括一个要求在软件包构建期间进行模型训练，另一个建议Debian认可OSAID。

一个关键的担忧围绕着对现有软件的影响，例如依赖于具有潜在非自由训练数据的训练模型的垃圾邮件过滤器和OCR工具。一些开发者担心周摩的提案会将此类软件从Debian的主仓库中排除，从而阻碍用户的赋权。另一些人则主张可检查性，并质疑预训练模型的可靠性。

周摩撤回了该提案，承认社区尚未准备好进行投票，并且需要进一步探索。他计划演示如何在神经网络中植入后门，并正在寻找工具来扫描Debian归档中受影响的软件包。这次讨论提出了关于AI模型权重是否应被视为软件或数据，以及要求训练数据对于Debian用户来说是否实用或有益的根本性问题。

---

## 88. Show HN：Typed-FFmpeg 3.0 – FFmpeg 的类型化接口和可视化滤镜编辑器

**原文标题**: Show HN: Typed-FFmpeg 3.0–Typed Interface to FFmpeg and Visual Filter Editor

**原文链接**: [https://github.com/livingbio/typed-ffmpeg](https://github.com/livingbio/typed-ffmpeg)

Typed-FFmpeg 3.0 是一个 Python 包，为 FFmpeg 提供了一个现代化的、类型化的接口，旨在简化复杂的滤镜图创建。它通过提供增强的 IDE 集成、全面的类型提示以及诸如滤镜图的 JSON 序列化、使用 graphviz 进行图可视化以及自动 FFmpeg 验证等新功能，解决了类似项目（如 ffmpeg-python）中存在的局限性。

主要功能包括零依赖（仅依赖 Python 标准库）、用户友好的滤镜图构建、对 FFmpeg 滤镜的广泛支持（具有自动完成和内联文档）、强大的静态和动态类型检查，以及将滤镜图保存和重新加载为 JSON 的能力。它还支持全面的输入/输出选项和部分求值。

可以使用 `pip install typed-ffmpeg` 轻松安装。可视化支持需要额外安装 `pip install 'typed-ffmpeg[graph]'` 和 Graphviz。该软件包包含一个交互式试验场，用户可以在其中试验滤镜、可视化图形并测试配置，而无需本地设置。

虽然最初构思时使用 GPT-3 进行代码生成，但该项目转向了传统方法以获得更可靠的结果，尽管 AI 工具在开发中仍然发挥了重要作用。该项目承认 ffmpeg-python 的影响，并献给作者的儿子。计划的未来增强功能包括扩展的 FFmpeg 版本和滤镜支持。

---

## 89. 成功鸡蛋坠落实验的关键？侧面着地。

**原文标题**: The key to a successful egg drop experiment? Drop it on its side

**原文链接**: [https://arstechnica.com/science/2025/05/the-key-to-a-successful-egg-drop-experiment-drop-it-on-its-side/](https://arstechnica.com/science/2025/05/the-key-to-a-successful-egg-drop-experiment-drop-it-on-its-side/)

本文探讨了一项麻省理工学院的研究，该研究挑战了鸡蛋坠落实验的传统认知。传统上，人们在保护装置中垂直放置鸡蛋，以防止其从高处坠落时破裂。然而，这项发表在《Communications Physics》上的麻省理工学院研究发现，水平放置鸡蛋，即侧放，显著降低了破裂的可能性。

塔尔·科恩教授的团队进行了实验，分别以垂直和水平方向从不同高度坠落鸡蛋。结果表明，垂直坠落的鸡蛋比水平坠落的鸡蛋更容易破裂。虽然垂直压缩测试表明鸡蛋沿长轴方向更坚硬，可以分散载荷，但在动态冲击情况下（如坠落），这种硬度反而成为劣势。

关键在于区分刚度（抵抗变形的能力）和韧性（开裂前吸收能量的能力）。该研究表明，鸡蛋在沿赤道水平加载时韧性更强。这是因为，为了在坠落中幸存，物体需要通过可逆形变来吸收动能。因此，水平放置允许在破裂前吸收更多的能量。作者建议，在鸡蛋坠落实验中，关注韧性而非刚度至关重要，这类似于跳跃落地时弯曲膝盖。研究结果还强调了不恰当的问题框架会导致误解和错误教育。

---

## 90. 草地渲染系列

**原文标题**: Grass Rendering Series

**原文链接**: [https://hexaquo.at/pages/grass-rendering-series-part-1-theory/](https://hexaquo.at/pages/grass-rendering-series-part-1-theory/)

本文是关于草地渲染系列文章的第一篇，重点在于理解草地的视觉特性以及在3D图形中描绘草地的不同方法。文章强调，逼真的草地渲染需要考虑以下几个方面：光泽（镜面高光）、半透明性、斑驳性（高度和颜色变化）以及自阴影。

文章随后探讨了游戏中常用的草地描绘技术。较早的游戏通常将草地的纹理直接贴在地形上，这种方法适用于短草，但不适用于较高的品种。一种更高级的方法是使用公告板，即带有草茎图像的平面，可以在细节和性能之间取得平衡。然而，近距离观察可能会暴露出它们的平面感，并且风的动画效果有限。

文章强调了使用完整几何体来渲染单个草叶的日益增长的趋势，特别是在追求真实感或特定美学的游戏中。虽然历史上受硬件限制，但现代GPU可以处理增加的顶点数量。《对马岛之魂》等游戏被引为例证，说明如何利用完整几何体草地来创造沉浸式环境。

本系列的下一篇文章将深入探讨如何在Godot中创建完整几何体草地，涵盖用草茎填充草地的高效方法以及实现所需视觉属性的着色技术。

---

## 91. 使用dotnet run app.cs直接运行C#文件

**原文标题**: Run a C# file directly using dotnet run app.cs

**原文链接**: [https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/](https://devblogs.microsoft.com/dotnet/announcing-dotnet-run-app/)

本文介绍了 .NET 10 Preview 4 中的一项新功能：可以直接使用 `dotnet run app.cs` 运行 C# 文件，而无需项目文件 (.csproj)。这简化了初学者的 C# 开发，并精简了脚本编写、原型设计和实验过程。

这种“基于文件的应用程序”方法的主要特性包括：

*   **易用性：**降低了入门门槛，使 C# 更容易学习和进行快速脚本编写。
*   **CLI 集成：**使用标准的 `dotnet` CLI，无需额外的工具或依赖项。
*   **可扩展性：**代码可以在需要时轻松过渡到完整的项目。
*   **文件级指令：**引入了诸如 `#:package`、`#:sdk` 和 `#:property` 等指令，可以直接在 `.cs` 文件中指定 NuGet 包、SDK 和 MSBuild 属性。
*   **Shebang 支持：**使用 Shebang 行 (`#!/usr/bin/dotnet run`) 启用跨平台 C# shell 脚本。
*   **转换为项目：**可以使用 `dotnet project convert app.cs` 轻松转换为标准项目。

本文强调这并非一种单独的 C# 方言，而是进入常规 C# 开发的自然入口点。它承认现有的脚本解决方案，但强调了此新功能的内置特性，以便立即使用。它还提供了关于如何安装 .NET 10 Preview 4、配置 VS Code 以支持基于文件的应用程序以及如何转换为项目的说明。未来的改进包括更好的 VS Code 集成和对多文件场景的命令行支持。

---

## 92. HTAP已死

**原文标题**: HTAP is Dead

**原文链接**: [https://www.mooncake.dev/blog/htap-is-dead](https://www.mooncake.dev/blog/htap-is-dead)

此博文认为，作为一种专用数据库架构的 HTAP（混合事务/分析处理）已死，但其解决的根本需求依然存在。文章追溯了数据库设计的历史，从 70 年代单个数据库处理 OLTP（事务性）和 OLAP（分析性）工作负载，到 80 年代由于这些工作负载的冲突需求而出现的“大鸿沟”。 这导致了具有不同存储架构（基于行与基于列）的专用 OLTP 和 OLAP 系统。

2010 年代见证了 NewSQL 和云数据仓库的兴起，使得潜在的和解成为可能，并在 2014 年正式确定了 HTAP 作为结合这两种处理类型的单个数据库。 然而，作者认为云数据仓库最终胜出，而 NewSQL 停滞不前，HTAP 从未实现产品市场契合度。

造成这种情况的几个因素包括：替换现有 OLTP 系统的难度、大多数工作负载不需要分布式 OLTP 的事实、云架构偏爱共享磁盘而非共享存储、以及 OLTP 和 OLAP 之间的所有权分离。

作者提出，HTAP 已经演变为一种分离的数据栈，由一流的组件组成：OLTP 系统、开放表格式、查询引擎和实时系统。 尽管单个 HTAP 数据库的概念已经消退，但对新鲜事务数据的快速 OLAP 查询的挑战仍然存在，现在通过实时数据管道、云数据湖和专用索引系统来解决。 作者认为，HTAP 的未来在于通过专注于从 OLTP 系统高效捕获数据以及在数据湖上构建低成本、同步的索引来使湖仓一体架构实现实时就绪。

---

## 93. 美国科学与剩余物资万岁

**原文标题**: Long live American Science and Surplus

**原文链接**: [https://milwaukeerecord.com/city-life/long-live-american-science-surplus-which-needs-your-help/](https://milwaukeerecord.com/city-life/long-live-american-science-surplus-which-needs-your-help/)

无法访问文章链接。

---

## 94. 研究表明，黑猩猩敲击树干发出声音进行交流

**原文标题**: Chimps strike stones against trees as communication, study suggests

**原文链接**: [https://phys.org/news/2025-05-year-chimpanzees-stones-trees-communication.html](https://phys.org/news/2025-05-year-chimpanzees-stones-trees-communication.html)

瓦赫宁根大学和德国灵长类动物研究中心一项为期五年的研究表明，西非的野生黑猩猩使用石头撞击树木进行交流。研究人员观察到成年雄性黑猩猩反复用石头撞击树干，并在树根处堆积石堆。首席作者Sem van Loon将这种行为称为“石器辅助鼓声”，它似乎与在支撑根上进行的传统鼓声有关，后者用于远程通信和展示统治地位。

与传统鼓声不同，石击行为通常以大声喘气声开始，然后是寂静，这表明其动机不同。研究人员认为，石头撞击树木产生的大声、低频声音可能比典型的交流方式在茂密的森林中传播得更远。

这项发表在《生物学快报》上的研究还表明，这种行为是文化传播的，幼年黑猩猩是从年长的群体成员那里学习的，而不是通过遗传获得的。Marc Naguib教授强调了其重要性，指出这表明文化并非人类独有，应在自然保护工作中加以考虑。该研究利用相机陷阱和当地野外指南，在几内亚比绍自然保护区的五个地点收集了视频素材。

---

## 95. 居里：研究实验代理

**原文标题**: Curie: A Research Experimentation Agent

**原文链接**: [https://github.com/Just-Curieous/Curie](https://github.com/Just-Curieous/Curie)

Curie：自动化并增强科学实验的AI智能体框架，旨在通过处理从假设到结果解读的每一步骤来加速研究。它专注于精确性、可靠性和可重复性。

主要特性包括自动化实验（假设、实现、执行、分析、反思）、通过验证模块增强严谨性，以及在机器学习研究、系统分析和科学发现中的广泛适用性。

要安装Curie，用户需要Docker、访问Docker守护程序的权限，以及从GitHub克隆Curie仓库。然后，他们需要在`env.sh`文件中提供其LLM API凭据，构建Docker镜像，并安装Curie包。

快速入门示例演示了如何将Curie用于特定问题以及数据集和代码库。输出包括自动生成的实验报告，可重现的代码和保存在指定工作区中的日志。该文档还指导用户如何将Curie与他们自己的入门文件集成，并提供示例和用例的链接。

如需支持，用户可以在GitHub Issues页面上提出问题或与Curie团队安排会议。

---

## 96. 几何学如何创造了现代物理学？

**原文标题**: How did geometry create modern physics?

**原文链接**: [https://www.quantamagazine.org/how-did-geometry-create-modern-physics-20250515/](https://www.quantamagazine.org/how-did-geometry-create-modern-physics-20250515/)

本文基于 "The Joy of Why" 播客的一集，探讨了几何学对现代物理学的深远影响。Janna Levin 和 Steven Strogatz 采访了理论物理学家何洋辉，他认为几何学是现代物理学的统一语言。

对话追溯了几何学的演变历程，从其在古代文明中的实际起源，如美索不达米亚和埃及的土地测量，到古希腊欧几里得对其的严格公式化。欧几里得对公理和证明的强调将几何学转变为数学思想的基石。

讨论重点强调了从欧几里得几何到非欧几里得几何的关键转变，尤其是在爱因斯坦广义相对论的背景下。爱因斯坦的洞见在于，弯曲的时空，由微分几何（由黎曼、罗巴切夫斯基和波约等数学家发展而来）描述，对于一个一致的引力理论至关重要。

他强调，虽然他最初对初等几何不屑一顾，但他后来认识到它深刻的美丽和重要性。

文章还涉及塑造物理学和数学的历史人物，并穿插了关于爱因斯坦、哥德尔和冯·诺伊曼的轶事。

---

## 97. 关于 JavaScript “工作量证明” 反爬虫系统的思考

**原文标题**: A thought on JavaScript "proof of work" anti-scraper systems

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/web/JavaScriptScraperObstacles](https://utcc.utoronto.ca/~cks/space/blog/web/JavaScriptScraperObstacles)

Chris Siebenmann的博客 Wandering Thoughts 正经历大量爬虫访问，可能用于收集LLM训练数据。 为此，他实施了反爬虫措施，阻止具有可疑旧版用户代理的浏览器，尤其是 Chrome 版本，因为这些通常被恶意爬虫使用。

如果合法用户遇到此屏蔽，Siebenmann 希望他们联系他，提供浏览器信息和 User-Agent 字符串，以便他改进过滤。

他特别提到通过 archive.today、archive.ph 和 archive.is 等存档服务访问博客的用户。他指出，由于这些服务使用旧版 Chrome User-Agent 值，以及具有可能伪造反向 DNS 条目的分布式 IP 地址（模仿 Googlebot），因此很难将它们与恶意爬虫区分开来。 他建议使用 archive.org，因为它是一个行为更好的存档爬虫，能够访问他的博客。

本质上，Siebenmann 正在采取积极主动的方法来管理爬虫流量，以保护他博客的性能，并要求用户反馈以提高其反爬虫措施的准确性。他明确提到了某些存档服务由于其爬行方式而导致的问题。

---

## 98. Show HN: 将泰拉瑞亚和蔚蓝移植到 WebAssembly

**原文标题**: Show HN: Porting Terraria and Celeste to WebAssembly

**原文链接**: [https://velzie.rip/blog/celeste-wasm](https://velzie.rip/blog/celeste-wasm)

该“Show HN”帖子详细介绍了将C#游戏泰拉瑞亚和蔚蓝移植到WebAssembly的过程，使其能够在Web浏览器中运行。作者讲述了为期一年的逆向工程、修复漏洞和调整工具链的旅程，以克服在WASM环境中运行.NET游戏的挑战。

该过程始于反编译游戏的C#代码，将WASM作为编译目标，并利用FNA（XNA框架的重新实现）。泰拉瑞亚需要提取嵌入的DLL，并使用emscripten配置构建环境。一个重要的障碍是FNA引擎对原生C++组件的依赖，这通过一个自定义构建系统(FNA-WASM-BUILD)得以解决。

为了使游戏真正*运行*，作者必须使用JavaScript创建一个最小的入口点和游戏循环，从而通过Origin Private File System启用资源加载（尽管存在浏览器兼容性问题）。该项目遇到了.NET 8.0中的线程问题，通过升级到.NET 9.0并启用WASM线程得以解决。这导致创建了一个OpenGL代理，以解决worker/DOM线程冲突，并使用fish脚本自动化了该过程。泰拉瑞亚面临AES加密支持的限制，通过emscripten链接OpenSSL克服了该问题。

蔚蓝的移植使用了类似的技术，面临着专有FMOD音频库的挑战，需要通过变通方法来集成该库的目标文件和自定义生成的C代码。使Everest mod加载器运行的最终目标需要解决Everest用于对代码应用运行时修改的MonoMod.RuntimeDetour的问题，他们尚未完成此项工作。

帖子最后提供了泰拉瑞亚和蔚蓝在浏览器中可玩版本的链接，以及它们各自的Git存储库。

---

## 99. Web Bench：一种比较AI浏览器代理的新方法

**原文标题**: Web Bench: a new way to compare AI browser agents

**原文链接**: [https://blog.skyvern.com/web-bench-a-new-way-to-compare-ai-browser-agents/](https://blog.skyvern.com/web-bench-a-new-way-to-compare-ai-browser-agents/)

Web Bench是一个新的基准数据集，旨在评估AI网页浏览代理的性能。它与Halluminate合作创建，通过将范围显著扩展到跨452个不同网站的5,750个任务，解决了WebVoyager等现有基准的局限性。一个关键的区别是将任务分为READ（数据提取）和WRITE（表格填写、登录、文件下载）活动。

初步研究结果表明，代理在WRITE繁重的任务中表现不佳，这表明这是一个主要的改进领域。虽然Anthropic的CUA在READ任务中表现出色，但Skyvern 2.0在WRITE任务中领先。总体而言，结果表明，当前的代理经常因执行不完整、无法与正确的元素交互以及一般的导航问题而失败。与代理问题、验证码挑战和身份验证问题相关的基础设施故障也发挥了重要作用。

该基准还探索了其他特性，如运行时长和所需步骤数，突出了快速且具有成本效益的代理的重要性。未来的计划包括扩展基准，以包括更多的网站、语言、网站类别，并评估更多的AI模型和API。数据集创建和评估方法在Halluminate团队的报告中详细说明，并计划在未来发布开源评估工具。

---

## 100. 贝特朗·皮卡尔的氢能大冒险——氢燃料电池飞机

**原文标题**: Bertrand Piccard's Big Hydrogen Adventure – hydrogen fuel-cell aircraft

**原文链接**: [https://spectrum.ieee.org/hydrogen-fuel-cell-aircraft](https://spectrum.ieee.org/hydrogen-fuel-cell-aircraft)

伯特兰·皮卡尔，出身于著名的探险世家，正踏上环球之旅，以展示氢作为航空燃料的可行性。他计划驾驶氢燃料电池飞机环绕世界。本文重点介绍了这项雄心勃勃的计划以及皮卡尔展示氢在航空业潜力的动力。

---

