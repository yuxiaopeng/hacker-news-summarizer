# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-02.md)

*最后自动更新时间: 2025-11-02 17:45:55*
## 1. 你为什么不用依赖类型？

**原文标题**: "Why don't you use dependent types?"

**原文链接**: [https://lawrencecpaulson.github.io//2025/11/02/Why-not-dependent.html](https://lawrencecpaulson.github.io//2025/11/02/Why-not-dependent.html)

为什么不用依赖类型？

本文探讨了作者从接触到最终放弃依赖类型理论，转而支持高阶逻辑（特别是在Isabelle证明助手中）的历程。

作者回忆了早期与N G de Bruijn的AUTOMATH以及后来的Martin-Löf类型理论的经历，甚至用它实现了Isabelle的第一个版本。然而，对Martin-Löf类型理论周围“教条式的态度”以及内涵相等问题的不满导致了转变。

作者承认依赖类型的理论优雅性和潜力，但认为高阶逻辑，特别是在Isabelle/HOL中，已被证明在形式化高级数学方面出奇地有效。ALEXANDRIA项目证明了这一点，该项目成功地形式化了Grothendieck概型和其他复杂的数学概念，而没有遇到高阶逻辑中无法克服的限制。

作者强调了开发新的形式体系和专注于已有的形式体系之间的权衡。选择后者允许利用Isabelle中现有的库、自动化和证明可读性。尽管依赖类型理论和像Lean这样的工具取得了进步，但作者仍然不相信，他引用了性能问题以及由内涵相等和过度使用依赖类型可能引起的并发症。最终，作者更看重Isabelle/HOL已被证明的实用性和现有生态系统，而不是依赖类型理论的理论前景。

---

## 2. 通义深研 – 比肩OpenAI DeepResearch的开源30B MoE模型

**原文标题**: Tongyi DeepResearch – open-source 30B MoE Model that rivals OpenAI DeepResearch

**原文链接**: [https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/](https://tongyi-agent.github.io/blog/introducing-tongyi-deep-research/)

通义千问DeepResearch是由阿里巴巴开发的完全开源的Web Agent，在多个基准测试中性能可与OpenAI的DeepResearch相媲美。它在诸如 Humanity's Last Exam (HLE)、BrowseComp 和 xbench-DeepSearch 等任务上取得了最先进的结果。

本文详细介绍了创建这种高级Agent的方法，重点介绍了在整个训练流程中使用的一种新颖的数据合成解决方案。这包括 Agentic 持续预训练 (CPT) 和监督微调 (SFT) 以建立基础，然后进行强化学习 (RL) 以进行行为对齐。RL 方法包括算法创新、自动化数据管理和强大的基础设施。

主要创新包括：

*   **AgentFounder:** 一种系统化且可扩展的数据合成解决方案，用于大规模 Agentic 预训练数据。
*   **合成数据生成:** 一个完全自动化的流程，无需人工干预即可创建高质量数据集。这包括构建知识图谱、生成问答对，并通过混淆信息来有意识地增加难度。
*   **IterResearch范式:** 一种通过将任务分解为研究轮次，并在每一轮重建简化的工作空间来缓解“认知窒息”的方法。
*   **研究-合成框架:** 并行研究Agent探索一个问题，最终由一个合成Agent整合报告以获得全面的答案。
*   **定制的On-Policy RL:** 利用 Group Relative Policy Optimization (GRPO) 和 on-policy 训练方案，使 Agent 的行为与高级目标保持一致。

该 Agent 支持 Native ReAct 模式（思考-行动-观察周期）以获得内在能力，并支持 Heavy 模式（IterResearch）以进行复杂的推理。作者强调了数据质量和训练环境稳定性对于成功进行 RL 的重要性。开发了一种使用离线 Wikipedia 数据库和自定义工具套件的模拟训练环境，以确保一致性并加速研究。

---

## 3. 1991年Autodesk的约翰·沃克解读惠普和IBM

**原文标题**: Autodesk's John Walker Explained HP and IBM in 1991

**原文链接**: [https://www.cringely.com/2015/06/03/autodesks-john-walker-explained-hp-and-ibm-in-1991/](https://www.cringely.com/2015/06/03/autodesks-john-walker-explained-hp-and-ibm-in-1991/)

本文分析了1991年惠普和IBM的困境，并将其与约翰·沃克在《Autodesk的末日》备忘录中概述的Autodesk面临的挑战相提并论。文章认为，惠普和IBM都在华尔街的期望驱使下，优先考虑短期利润率，而牺牲了长期投资和创新。沃克的备忘录表明，为了保持高利润率，公司常常忽视对未来产品和营销的投资，这种策略最终使它们容易受到具有更长远眼光的竞争对手的攻击。

文章解释了会计方法如何激励公司削减关键支出。具体来说，直接向主要客户销售虽然总体上有利，但由于佣金成本被归类为“销售成本”，导致营销和销售预算被削减，从而在账面上降低了利润率。

这篇文章强调了优先考虑会计规则而非实际战略的危险，导致了诸如在创纪录销售额期间削减营销等违反直觉的决策。文章批评了IBM收购公司后又剥夺其资源以维持利润率的策略，沃克认为这种做法尽管在会计上有好处，但却是“疯狂的”。

核心论点是，与沃克分析中的Autodesk一样，惠普和IBM都在牺牲长期增长以换取短期财务表现，最终危及其未来的成功。缺乏内部沟通以及重视外部投资而非内部需求进一步加剧了这些问题。

---

## 4. 老鼠首次被拍到从空中捕食蝙蝠

**原文标题**: Rats filmed snatching bats from air for first time

**原文链接**: [https://www.science.org/content/article/rats-filmed-snatching-bats-air-first-time](https://www.science.org/content/article/rats-filmed-snatching-bats-air-first-time)

南大西洋戈夫岛上的老鼠首次被拍摄到在半空中捕食成年活蝙蝠。研究人员记录的这种前所未有的行为，揭示了入侵物种造成的生态破坏的新程度。这些老鼠是19世纪由水手引入该岛的，此前已知它们捕食海鸟雏鸟和鸟蛋，导致多个物种濒临灭绝。

发表在《濒危物种研究》期刊上的这项研究详细介绍了研究人员如何使用红外摄像机拍摄到老鼠从地面跳起，成功伏击并杀死从栖息洞穴中出来的戈夫岛本地蝙蝠的镜头。这些蝙蝠是一种小型食虫物种，以前人们认为由于它们夜间飞行，相对安全，不易受到老鼠的捕食。这一新的观察结果表明了老鼠的适应能力及其对该岛脆弱生态系统的严重影响。

该发现强调了在戈夫岛上紧急开展灭鼠工作以保护剩余本地物种的必要性。“戈夫岛恢复计划”是一项主要的保护倡议，旨在消除老鼠种群并恢复该岛的生态平衡。这一发现进一步强调了该计划的重要性，并加强了持续监测和研究的必要性，以了解入侵物种对全球岛屿生态系统影响的全部程度。

---

## 5. URL是状态容器

**原文标题**: URLs are state containers

**原文链接**: [https://alfy.blog/2025/10/31/your-url-is-your-state.html](https://alfy.blog/2025/10/31/your-url-is-your-state.html)

本文提倡将URL作为Web应用程序中一个强大且经常被忽视的状态管理工具。文章认为，精心设计的URL可以通过提供可分享性、可收藏性、浏览器历史记录支持和深度链接功能，显著提升用户体验。

作者强调，URL不仅仅是地址，更是接口和状态容器。URL的不同部分，如路径段、查询参数和锚点，可以编码各种类型的状态，例如资源导航、过滤器、UI偏好和页面部分。文章重点介绍了查询参数的常见模式，包括多值的分隔符、嵌套数据编码、布尔标志和数组表示法。

文章展示了真实世界的案例，如PrismJS配置、GitHub行高亮、Google Maps、Figma设计和电子商务过滤器，所有这些都有效地使用URL来存储应用程序状态。文章提供了关于哪些类型的状态适合URL（搜索查询、分页、UI配置）以及应该避免哪些状态（敏感数据、临时UI状态、极其复杂的数据）的指导方针。

作者演示了如何使用纯JavaScript（URLSearchParams API）和React（React Router hooks）来实现URL状态管理。最佳实践包括优雅地处理默认值、消除URL更新的抖动，以及适当地选择`pushState`和`replaceState`。文章最后强调了使用URL作为缓存、性能、版本控制和清晰边界的契约的优势，并警告了常见的反模式，例如将敏感数据存储在URL中以及在SPA中仅依赖于内存状态。

---

## 6. Mock - API 创建和测试工具：示例

**原文标题**: Mock – An API creation and testing utility: Examples

**原文链接**: [https://dhuan.github.io/mock/latest/examples.html](https://dhuan.github.io/mock/latest/examples.html)

本文提供了使用`mock`工具创建和测试API的示例，演示了如何延迟特定API端点、构建一个由多种编程语言驱动的API，以及创建一个有状态的API。

**延迟端点：** 你可以模拟缓慢的API响应。本文展示了如何使用带有`--base`选项的`--delay`选项延迟所有请求，或者如何使用中间件脚本选择性地延迟特定端点。该中间件使用`MOCK_REQUEST_ENDPOINT`环境变量来识别目标端点，并引入了一个sleep命令。

**多语言API：** `mock`工具可以使用`--route`和`--exec`选项通过多种语言处理请求。示例使用Node.js、Python和PHP来响应不同的路由。每个路由执行一段代码片段，该代码片段打印来自相应语言的问候语，并将输出通过管道传递给`mock write`。

**有状态API：** 本文解释了如何在请求之间维护状态。使用一个临时文件来存储计数器。每个请求使用`bc`和`sponge`递增计数器，然后在API响应中显示当前计数。`--route`和`--exec`选项定义了一个路由并执行shell命令来更新和检索计数器。

---

## 7. 反向传播是一种有漏洞的抽象 (2016)

**原文标题**: Backpropagation is a leaky abstraction (2016)

**原文链接**: [https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b](https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b)

Andrej Karpathy 的文章《反向传播是一个有漏洞的抽象》认为，即使在使用 TensorFlow 等自动化框架的情况下，对反向传播的深入理解对于有效构建和调试神经网络至关重要。他断言反向传播不是一个“黑盒”，其内部运作对训练产生重大影响。

作者提供了几个盲目依赖自动化反向传播导致问题的例子：

1.  **Sigmoid 上的梯度消失：** 不正确的权重初始化或数据预处理可能使 sigmoid 或 tanh 激活饱和，导致梯度消失并停止学习。
2.  **ReLU 死亡：** 如果 ReLU 神经元的权重导致它们永远不会激活（“死亡”），则可能永久失效，从而浪费容量。
3.  **RNN 中的梯度爆炸：** 循环神经网络 (RNN) 由于反向传播期间的重复矩阵乘法而容易出现梯度爆炸，需要进行梯度裁剪。
4.  **DQN 裁剪：** 来自深度 Q 学习实现的一个例子表明，旨在提高鲁棒性的 Q 值增量裁剪无意中阻止了梯度流动，突出了考虑反向传播的重要性。

Karpathy 强调，理解反向传播的细微之处使开发者能够预测和解决潜在问题，例如饱和激活、死亡神经元和梯度爆炸。他推荐 CS231n 讲座和作业等资源，以获得对反向传播的实践理解。核心信息是，将反向传播视为一种神奇的解决方案而不理解其底层机制，将导致神经网络开发和调试的效率降低。

---

## 8. 用C语言编写FreeDOS程序

**原文标题**: Writing FreeDOS Programs in C

**原文链接**: [https://www.freedos.org/books/cprogramming/](https://www.freedos.org/books/cprogramming/)

本文介绍了一篇关于使用C语言编写FreeDOS程序的指南，该指南最初是一个由Patreon赞助的YouTube视频系列。特定等级（“C语言编程”级别）的Patreon支持者享有以下几项权益：

*   **提前观看**C语言编程视频。
*   **独家访问**比视频内容更详细的编程指南。
*   参加**每周论坛**，提问有关视频中涵盖的C语言编程主题。

视频系列结束后，该编程指南被转化为一本自学书籍，并通过出版合作伙伴以成本价提供给Patreon支持者。本文主要详细介绍了FreeDOS编程资源的演变过程，并重点介绍了向Patreon支持者提供的权益。

---

## 9. djb 关于使用 Fil-C (2025) 的笔记

**原文标题**: Notes by djb on using Fil-C (2025)

**原文链接**: [https://cr.yp.to/2025/fil-c.html](https://cr.yp.to/2025/fil-c.html)

本文是djb（Daniel J. Bernstein）记录的2025年使用内存安全的C/C++编译器Fil-C的经验笔记。他对Fil-C的兼容性印象深刻，指出许多库和应用程序无需修改即可运行。他的主要目标是通过使用Fil-C编译代码来保护他管理的机器。

本文档详细说明：

*   **Fil-C设置和安装：** 使用`filian-install-compiler`脚本在Debian 13上下载、编译和安装Fil-C的说明。它强调了编译期间的资源需求，特别是内存。
*   **软件包构建：** 描述了一个用于使用Fil-C编译Debian源码包的`filian-install-packages`脚本，以及其当前的局限性。
*   **性能：** 提及了比较Fil-C和clang的微基准测试结果，通常显示Fil-C代码需要1倍到4倍的周期。
*   **替代安装：** 介绍了Mikael Brockman的Filnix，这是一种使用`nix-user-chroot`在Debian 12下运行Fil-C的方法。
*   **构建更多库：** 详细介绍了`build-parallel.py`脚本，它是Fil-C的`build_all_slow.sh`的并行化替代方案，并报告了成功编译大量库和应用程序的情况。
*   **其他库和应用程序：** 记录了编译和使用各种库和应用程序的说明，包括boost、cdb、libcpucycles、libgc（使用`gcshim`作为替代）、libntruprime、lpeg、luv、mutt、tig和w3m。
*   **Debian集成：** 解释了将Fil-C集成到Debian软件包构建的过程，旨在通过`apt install bash:amd64fil0`安装一个用Fil-C编译的版本。这包括处理包含文件，并解决Fil-C和Debian管理它们的方式的差异。

这些笔记为在Debian环境中使用Fil-C时遇到的常见问题提供了实用指导和解决方案，使其对那些希望试验或采用Fil-C的人来说非常有价值。

---

## 10. X.org 安全公告：多个安全问题影响 X.Org X 服务器和 Xwayland

**原文标题**: X.org Security Advisory: multiple security issues X.Org X server and Xwayland

**原文链接**: [https://lists.x.org/archives/xorg-announce/2025-October/003635.html](https://lists.x.org/archives/xorg-announce/2025-October/003635.html)

X.Org 安全公告（2025年10月28日），宣布修复 X.Org X server 21.1.18 之前版本和 Xwayland 24.1.8 之前版本中发现的多个漏洞的安全补丁。这些修复已包含在 xorg-server-21.1.19 和 xwayland-24.1.9 中。

解决了以下三个具体漏洞：

1. **CVE-2025-62229:** 在 XPresentNotify 结构创建中的释放后使用漏洞，该漏洞在处理 Present 扩展通知时的错误处理期间触发。

2. **CVE-2025-62230:** Xkb 客户端资源移除中的释放后使用漏洞。`XkbRemoveResourceClient()` 函数释放了 XkbInterest 数据，但没有释放相关的资源，导致客户端终止时出现释放后使用的情况。

3. **CVE-2025-62231:** Xkb 扩展的 `XkbSetCompatMap()` 函数中的值溢出。该函数未能检查在对存储为 unsigned short 的输入数据求和时可能发生的溢出。

所有三个漏洞均由 Jan-Niklas Sohn 与 Trend Micro Zero Day Initiative 合作发现。每个漏洞的修复程序都以指向 gitlab 提交的链接形式提供。该公告感谢报告、修复、审查和发布修复程序的人员。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 2 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 3 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 4 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 5 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 6 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 7 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 8 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 9 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 10 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 11 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 12 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 13 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 14 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 15 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 16 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 17 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 18 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 19 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 20 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 21 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 22 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 23 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 24 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 25 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 26 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 27 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 28 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 29 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 30 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 31 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 32 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 33 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 34 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 35 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 36 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 37 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 38 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 39 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 40 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 41 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 42 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 43 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 44 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 45 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 46 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 47 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 48 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 49 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 50 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 51 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 52 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 53 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 54 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 55 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 56 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 57 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 58 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 59 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 60 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 61 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 62 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 63 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 64 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 65 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 66 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 67 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 68 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 69 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 70 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 71 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 72 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 73 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 74 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 75 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 76 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 77 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 78 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 79 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 80 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 81 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 82 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 83 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 84 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 85 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 86 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 87 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 88 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 89 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 90 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 91 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 92 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 93 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 94 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 95 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 96 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 97 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 98 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 99 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 100 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 101 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 102 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 103 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 104 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 105 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 106 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 107 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 108 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 109 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 110 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 111 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 112 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 113 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 114 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 115 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 116 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 117 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 118 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 119 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 120 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 121 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 122 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 123 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 124 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 125 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 126 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 127 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 128 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 129 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 130 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 131 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 132 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 133 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 134 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 135 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 136 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 137 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 138 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 139 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 140 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 141 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 142 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 143 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 144 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 145 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 146 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 147 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 148 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 149 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 150 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 151 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 152 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 153 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 154 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 155 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 156 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 157 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 158 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 159 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 160 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 161 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 162 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 163 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 164 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 165 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 166 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 167 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 168 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 169 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 170 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 171 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 172 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 173 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 174 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 175 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 176 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 177 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 178 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 179 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 180 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 181 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 182 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 183 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 184 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 185 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 186 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 187 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 188 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 189 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 190 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 191 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 192 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 193 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 194 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 195 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 196 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 197 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 198 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 199 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 200 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 201 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 202 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 203 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 204 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 205 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 206 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 207 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 208 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 209 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 210 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 211 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 212 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 213 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 214 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 215 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 216 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 217 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 218 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 219 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 220 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 221 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 222 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 223 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 224 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 225 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 226 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 227 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
