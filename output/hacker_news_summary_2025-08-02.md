# Hacker News 热门文章摘要 (2025-08-02)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 运动为何是灵丹妙药

**原文标题**: Why Exercise Is a Miracle Drug

**原文链接**: [https://www.derekthompson.org/p/the-sunday-morning-post-why-exercise](https://www.derekthompson.org/p/the-sunday-morning-post-why-exercise)

德里克·汤普森的《为何运动是奇效药》一文指出，运动是最有效的医疗发明，胜过任何药物。他引用了斯坦福大学尤安·阿什利领导的研究，该研究发现运动深刻地改变了老鼠几乎所有组织和分子系统，影响了肌肉、心脏、肝脏、肾上腺、脂肪和免疫系统。阿什利认为，运动的效果过于广泛，任何单一药物都无法复制，它可以改善新陈代谢、线粒体功能、免疫力，并提供疾病保护。

文章还强调了《新英格兰医学杂志》上的一项研究，该研究表明，手术后的结肠癌患者通过运动显著提高了生存率并减少了新癌症的发生。运动不仅可以预防疾病，还可以在患病后提供帮助。

文章随后转向美国在全球健康和发展方面的支出，特别是美国国际开发署的影响。《柳叶刀》杂志的一项研究估计，此类资金在20年内通过对抗艾滋病毒/艾滋病、腹泻疾病、呼吸道感染、被忽视的热带疾病、疟疾、肺结核和营养不良，在低收入国家拯救了大约9000万人的生命。该计划的成本仅占美国国家支出的一小部分，使其成为“道德投资的惊人回报”。

汤普森最后主张继续进行全球健康支出，认为富裕国家拥有一块“魔法石”，可以通过对贫困地区进行简单的干预，将一小部分财富转化为数百万条被拯救的生命。他还想知道为什么医疗保险和医疗补助通常不包括健身房会员资格。

---

## 2. 多处理器编程艺术（第二版）读书会

**原文标题**: The Art of Multiprocessor Programming 2nd Edition Book Club

**原文链接**: [https://eatonphil.com/2025-art-of-multiprocessor-programming.html](https://eatonphil.com/2025-art-of-multiprocessor-programming.html)

本书社群：Herlihy等人《多处理器编程的艺术（第二版）》

本文宣布成立一个读书社群，专注于研读Herlihy、Shavit、Luchangco和Spear所著的《多处理器编程的艺术（第二版）》。该读书社群是Software Internals Email Book Club的一部分，运行时间为8月16日至12月13日。参与者需要购买本书第二版（ISBN 9780124159501），并在指定的讨论日期前阅读每个章节。

读书社群的核心是通过Google Group进行异步的文本讨论。参与者需要一个Google帐户才能加入和发帖。每周，指定的“讨论发起人”将通过一封简短的电子邮件来启动对话，反思指定的章节，分享个人背景，并突出显示感兴趣或困惑的点。

时间表详细说明了每周要讨论的章节。主题包括互斥、并发对象、共享内存基础、同步原语、共识、自旋锁、监视器、链表、队列、堆栈、排序、哈希、跳跃表、优先级队列、调度、数据并行性和屏障。

欢迎感兴趣的个人通过提供的表格注册。欢迎通过电子邮件或Twitter提供反馈、问题、更正和想法。

---

## 3. WebGPU实现浏览器本地LLM。AI聊天演示站点

**原文标题**: WebGPU enables local LLM in the browser. Demo site with AI chat

**原文链接**: [https://andreinwald.github.io/browser-llm/](https://andreinwald.github.io/browser-llm/)

WebGPU赋能：在浏览器中运行大型语言模型

---

## 4. 如果人工智能解决了孤独，我们可能不会喜欢我们将变成的样子。

**原文标题**: We may not like what we become if A.I. solves loneliness

**原文链接**: [https://www.newyorker.com/magazine/2025/07/21/ai-is-about-to-solve-loneliness-thats-a-problem](https://www.newyorker.com/magazine/2025/07/21/ai-is-about-to-solve-loneliness-thats-a-problem)

人工智能伴侣：对抗孤独的复杂影响

---

## 5. 将冰岛语姓名变格模式压缩成3.27kB的trie树

**原文标题**: Compressing Icelandic name declension patterns into a 3.27 kB trie

**原文链接**: [https://alexharri.com/blog/icelandic-name-declension-trie](https://alexharri.com/blog/icelandic-name-declension-trie)

本文详细介绍了一种巧妙的方法，用于将冰岛语姓名变格模式压缩成一个小型高效的数据结构，以供 JavaScript 库使用。冰岛语变格需要根据语法格（主格、宾格、与格、属格）来了解姓名的正确形式。挑战在于如何紧凑地存储此信息。

作者使用冰岛语形态数据库 (DIM) 和个人姓名登记处的数据来构建一个系统，该系统可以推导出给定语法格的正确姓名形式。直接存储所有形式的简单方法过于庞大。解决方案包括：

1.  **后缀编码：** 通过存储姓名的最长公共前缀，然后存储每个语法格的后缀（以逗号分隔的字符串），来表示变格模式。这消除了冗余。

2.  **Trie 数据结构：** 将后缀编码存储在 trie（前缀树）数据结构中。键（姓名）以*相反*的顺序插入，以便具有相似后缀的姓名在子树中分组在一起。

3.  **Trie 压缩：** 通过识别所有叶节点共享相同值（后缀编码）的子树来压缩 trie。然后，将子树替换为具有该公共值的单个节点。

这种压缩允许 trie 进行泛化，根据共享后缀预测未明确包含在初始数据集中的姓名的变格模式。 这产生了一个小的 (3.27 kB) trie，可以准确地预测很大一部分冰岛语姓名的变格模式。`trieLookup` 函数被修改为在缺少姓名的情况下返回最后命中的节点。

---

## 6. 特洛 MT1

**原文标题**: Telo MT1

**原文链接**: [https://www.telotrucks.com/](https://www.telotrucks.com/)

TELO MT1 是一款全电动迷你卡车，专为城市生活和周末探险而设计。它拥有丰田塔科马的性能和特斯拉般的效率，却仅占MINI Cooper 的空间。这款紧凑型皮卡配备 5 英尺长的货箱，带可配置的中间隔板，可容纳 4x8 英尺的胶合板，或通过货箱下方的储物通道选装第三排座椅，最多可容纳 8 名乘客。

主要特点包括安全的卷帘盖、采用天然面料的简约内饰设计、先进的安全技术以及 350 英里的续航里程和快速充电电池组。它设计高效、强大，适合城市通勤和户外活动。

MT1 提供不同的配置，包括单电机和双电机选项，双电机版本可在 4 秒内实现 0-60 英里/小时的加速。有效载荷为 2,000 磅。尺寸为 152" x 73" x 66"，货箱尺寸为 60-96" x 56" x 18"。电池续航里程选项包括标准（260 英里）和长续航（350 英里），30 分钟即可充电至 80%。该公司正在接受该车辆的预订。

---

## 7. Great Question (YC W21) 正在招聘工程副总裁 (远程)

**原文标题**: Great Question (YC W21) Is Hiring a VP of Engineering (Remote)

**原文链接**: [https://www.ycombinator.com/companies/great-question/jobs/ONBQUqe-vp-of-engineering](https://www.ycombinator.com/companies/great-question/jobs/ONBQUqe-vp-of-engineering)

Great Question (Y Combinator W21支持的A轮B2B SaaS公司，致力于普及客户研究) 正在寻找工程总监。此远程职位（位于美国）薪资为15万至20万美元，要求6年以上经验，并具备美国公民/签证身份。

工程总监将向首席技术官汇报，负责扩展工程团队、系统和技术基础。主要职责包括：

*   **交付与卓越运营：** 领导多个团队的交付，改进发布流程，提高效率并保持可见性。
*   **技术领导力与平台架构：** 维护工程标准，塑造架构方向，并确保战略技术决策得到记录。
*   **人员领导力与组织设计：** 构建团队，吸引和留住人才，培养领导者，并定义职业发展框架。
*   **跨职能执行：** 与产品、客户成功和设计团队合作，协调路线图，并将技术投资转化为业务影响。
*   **文化与战略：** 扩展工程文化，营造高度信任的环境，将工程师与客户成果联系起来，并为高层规划做出贡献。

理想的候选人需要在高增长的B2B SaaS环境中扩展工程团队（理想情况下是A轮到B/C轮），在资深工程师中具有公信力，具有招聘和指导的记录，并且是其他部门值得信赖的合作伙伴。公司提供有竞争力的薪资、股权、福利、远程工作和慷慨的休假。招聘流程包括与创始人及技术人员的多次面试，然后进行背景调查。

---

## 8. 克劳德代码六周速成

**原文标题**: 6 Weeks of Claude Code

**原文链接**: [https://blog.puzzmo.com/posts/2025/07/30/six-weeks-of-claude-code/](https://blog.puzzmo.com/posts/2025/07/30/six-weeks-of-claude-code/)

本文反思了 Claude Code（一种 LLM 代码助手）在过去六周内对作者在 Puzzmo 编程工作流程产生的变革性影响。作者认为，Claude Code 正在彻底改变编程，类似于摄影的引入，它使开发者不必编写每一行代码，而是专注于塑造和改进生成的代码。

主要优势包括：
*   **更低的维护成本：**能够快速完成之前令人望而却步的技术债务任务。
*   **“先写后定”方法：** 促进快速实验和探索想法。
*   **游戏设计协作：** 简化了创建和集成原型游戏的过程，以“Missing Link”的发布为例。 这对原型代码是否适合长期生产提出了新的挑战。
*   **更快的 Issue 分类：** 在 Issue 分类期间，LLM 尝试操作提供了快速的第一步。

作者强调，Claude Code 对具备产品、技术技能和自主性的开发者最有效。 Monorepo 和明确且完善的技术（如 React、GraphQL 和 TypeScript）可提高其性能。 虽然提交和代码行数等传统指标并未发生巨大变化，但团队内部感知到的变化速度已显著提高。 作者总结说，专注于掌握 Claude Code 本身比追逐每一个新的 LLM 趋势更有益，并且良好地构建工作比特定的模型更重要。 他指出，Puzzmo 的业务在 LLM 模型基准测试中表现良好。

---

## 9. 在光线中隐藏秘密代码可防止伪造视频

**原文标题**: Hiding secret codes in light protects against fake videos

**原文链接**: [https://news.cornell.edu/stories/2025/07/hiding-secret-codes-light-protects-against-fake-videos](https://news.cornell.edu/stories/2025/07/hiding-secret-codes-light-protects-against-fake-videos)

康奈尔大学研究人员开发了一种新型“水印”技术，利用难以察觉的光线波动来对抗虚假视频的传播。该方法将秘密代码隐藏在场景的光照中，可在任何在该光线下拍摄的视频中被检测到。这些代码旨在让人眼无法察觉，但会被记录为视频素材中的水印。

这些带有水印的光源，如电脑屏幕、摄影灯和内置照明，包含一个秘密代码，可用于验证视频的真实性并检测任何恶意编辑。该水印包含在略微不同的光照条件下未被篡改视频的时间戳版本，被称为“代码视频”。如果视频被篡改，被操纵的部分将与代码视频相矛盾，从而揭示更改。人工智能生成的虚假视频将在代码视频中产生随机变化，从而暴露其虚假性。

研究人员将代码设计成类似于光线中的随机变化，使其在没有秘密代码的情况下难以检测。该系统可以识别镜头中的间隙和被修改的物体，这些物体在恢复的代码视频中显示为黑色。该团队已成功地在同一场景中使用多个代码，使得伪造更加困难。虽然该方法适用于户外和不同的肤色，但研究人员承认，在信息误导的军备竞赛中仍然存在挑战，并且需要不断改进检测技术。

---

## 10. Ruby 正则表达式中的 /o 代表 “哦，人类啊”

**原文标题**: The /o in Ruby regex stands for "oh the humanity "

**原文链接**: [https://jpcamara.com/2025/08/02/the-o-in-ruby-regex.html](https://jpcamara.com/2025/08/02/the-o-in-ruby-regex.html)

深入剖析 Ruby 正则表达式中晦涩且危险的 `/o` 修饰符，又称“插值模式”。作者回顾了由该修饰符引起的调试噩梦，并解释了其令人惊讶的行为。

`/o` 修饰符会在首次求值后缓存正则表达式，这意味着任何插值仅处理 *一次*，仅此而已。这可能会导致意外和不一致的结果，尤其是在实例方法、循环或多线程环境中。作者演示了对正则表达式的首次调用如何决定其在程序生命周期内的值，而与对象实例化或后续输入无关。

通过将代码反汇编为 Ruby VM 字节码并检查 `insns.def` 文件，作者发现了 `once` 指令和 `vm_once_dispatch` 函数，它们管理着这种缓存机制。这些内部机制揭示了第一个遇到正则表达式的线程决定其值，而后续线程要么重用缓存的值，要么等待初始求值。

文章进一步说明了该修饰符在多线程场景中的非确定性行为，并探讨了一个奇怪的递归示例。作者得出结论，`/o` 的性能优势远不及它可能造成的令人困惑的错误，尤其是在开发人员可以轻松地自己缓存正则表达式对象的情况下。重新加载代码，例如在 Rails 控制台中，是强制重新求值的一种方法。作者最终建议不要使用 `/o` 修饰符，这与早期 Perl 文档中发现的观点相呼应。

---

## 11. Unikernel指南：构建和部署轻量、安全的应用

**原文标题**: Unikernel Guide: Build and Deploy Lightweight, Secure Apps

**原文链接**: [https://tallysolutions.com/technology/introduction-to-unikernel-2/](https://tallysolutions.com/technology/introduction-to-unikernel-2/)

本文全面介绍了Unikernel，重点介绍了它们的优势、局限性以及使用Nanos的实际应用。Unikernel被描述为轻量级的单应用虚拟机，通过将应用程序和必要的操作系统组件合并到单个可执行镜像中，从而提高速度、效率和安全性。

本文将Unikernel与传统操作系统进行了对比，强调了Unikernel通过消除不必要的内核功能来减少开销。文章详细介绍了两种流行的Unikernel实现——Nanos和Unikraft之间的差异，并指出Nanos能够在各种云提供商上运行。

文章提供了从源代码构建Nanos及其操作工具(OPS)的逐步指南，然后介绍了如何在AWS上创建和部署Nanos镜像和实例。文章还演示了如何使用QEMU在本地运行Nanos。Linux和Nanos之间的性能比较（侧重于I/O操作和执行时间）表明Nanos通常能获得更快的运行结果。

文章重点介绍了轻量级微服务、嵌入式系统和快速原型设计等用例。它还讨论了包括开发复杂性、有限的生态系统、调试困难以及潜在的网络限制在内的挑战。

总之，Unikernel为应用程序部署提供了一种变革性的方法，但开发人员应了解其当前的局限性。随着技术的不断发展，Unikernel有潜力成为高效、安全地交付应用程序的关键工具。

---

## 12. 魔方完美打乱

**原文标题**: The Rubik's Cube Perfect Scramble

**原文链接**: [https://www.solutionslookingforproblems.com/post/the-rubik-s-cube-perfect-scramble](https://www.solutionslookingforproblems.com/post/the-rubik-s-cube-perfect-scramble)

本文详述了作者寻找“完美”魔方打乱方案的探索过程，该方案要求没有两个相同颜色的方块相邻，同时满足若干约束条件：每个面都包含所有颜色，每个面上的同色方块数量有限制，没有对角线相邻，每个面上的图案各不相同，且跨面没有角块相邻。

面对天文数字般的可能排列，作者开发了一个程序来系统地生成和评估潜在的解决方案。该程序通过构建有效的角块和棱块排列列表来工作，并剪枝违反约束条件的搜索树分支。它利用魔方可解性原理（角块和棱块奇偶性）来避免生成无法解的状态。

经过五天的计算，该程序找到了一种“完美打乱”解决方案，根据魔方的方向和镜像，它可以表现为 48 种独特的排列方式。本文提供了创建和解决这种完美打乱及其镜像的步骤序列。

作者反思了该程序的潜在优化方案，例如多线程和进一步基于约束的剪枝。他们还讨论了添加更多要求的局限性，因为任何新的约束要么已经满足，要么会在不放松现有约束的情况下使解决方案变得不可能。该程序的源代码已公开提供。

---

## 13. 我家长期护理保险经历带来的财务教训

**原文标题**: Financial Lessons from My Family's Experience with Long-Term Care Insurance

**原文链接**: [https://www.whitecoatinvestor.com/financial-lessons-father-long-term-care-insurance/](https://www.whitecoatinvestor.com/financial-lessons-father-long-term-care-insurance/)

亚当·萨夫迪分享了其父亲被诊断出患有痴呆症后，他们一家人使用长期护理保险（LTC）的经历。文章重点介绍了在申请和获得理赔过程中遇到的挑战和经验教训。

在他父亲走失的一件令人不安的事件发生后，家人意识到他需要持续的照顾。幸运的是，亚当的父母多年前购买了LTC保险。理赔过程非常复杂，涉及多个步骤：联系保险公司申请，尽管有神经科医生的诊断，仍需应对他们的内部评估，以及理解90天的免赔期，而免赔期仅计算专业护理的“服务日”。

亚当强调了赔偿附加条款的重要性，该条款无论发生的费用多少都会支付预定的福利。他还强调需要仔细记录服务日期，仔细核对保险公司的计算，并确保提交所有必需的文件，包括护理记录。

文章指出了持续存在的问题，例如需要不断警惕的错误标记的发票。亚当强调了他们的保险经纪人提供的宝贵帮助，这有助于加快流程。最终，LTC保险在经济上为他父亲的居家护理提供了关键支持，使他能够舒适地在自己家中养老，并减轻了家人长途老年护理的负担。他最后鼓励读者分享他们自己与年迈的父母和LTC保险的经历。

---

## 14. 注册机音乐在线收藏

**原文标题**: Online Collection of Keygen Music

**原文链接**: [https://keygenmusic.tk](https://keygenmusic.tk)

Keygenmusic.tk是一个在线tracker音乐播放器，专注于注册机中的音乐，支持.mod、.xm、.s3m和.it格式。它是一个测试版本（目前是β15），已经经历了多次更新。该网站提供一个注册机音乐库，并允许用户收藏曲目。该服务强调它不包含任何非法内容，严格来说是从注册机中提取的音乐。

最近的更新包括修复了Firefox的问题、禁用自动播放、改进了样式、更好的图标、对播放/暂停/下一个/上一个的媒体键支持以及移动优化。较早的更新包括添加歌曲标题、搜索功能和更新音乐包。

该网站感谢其开发中使用的各种库、工具和个人，包括chiptune2.js、libopenmpt、emscripten、jsTabs、baron、Sergio Camalich、wothke.ch/webaudio68、Darcula配色方案和一个随机播放开关。开发归功于Mikhailo Onikiienko。

该网站提供联系信息（keygenmusic.tk{at}outlook.com），并包含有关总播放次数和曲目的信息。它还警告用户，如果他们的浏览器不支持AudioContext，请使用Firefox。

---

## 15. 缓存：LRU 与随机

**原文标题**: Caches: LRU vs. Random

**原文链接**: [https://danluu.com/2choices-eviction/](https://danluu.com/2choices-eviction/)

本文探讨了缓存驱逐策略，特别比较了最近最少使用（LRU）算法与随机方法。它挑战了LRU直观上的优越性，认为当工作集超过缓存大小时，随机驱逐策略可以更平缓地降低性能。

作者研究了“2-random”策略，即在两个随机缓存行中选择LRU。使用SPEC CPU基准程序在类似Sandy Bridge的缓存层次结构上的模拟表明，2-random的性能与LRU相当，甚至在更大的缓存（L3）中略胜一筹。对各个基准程序的分析表明，LRU在未命中率较低时表现更好，而2-random在高未命中率时表现出色。

文章进一步研究了缓存大小和层次结构的影响，将单级缓存与分层缓存进行了比较。结果表明，2-random在较大缓存中的优势不仅仅是因为它是层次结构中的最后一级。

作者随后考察了伪LRU和伪2-random的实现，指出伪3-random（在三个随机选项中选择LRU）的性能接近真正的2-random，并且在大缓存中超过LRU。文章还探讨了集合相联性的影响，发现增加相联性会放大LRU和2-random之间的性能差异。

结论认为，虽然LRU在较小缓存中有利，但2-random（或k-random变体）在较大缓存中变得具有竞争力甚至更优越，可能为更复杂的自适应策略提供一种经济高效的替代方案。文章将k-random策略的有效性与“两个随机选择的力量”的数学原理联系起来，解释了其在负载平衡和其他领域的应用。

---

## 16. 微软将开源Windows 11的UI框架。

**原文标题**: Microsoft is open sourcing Windows 11's UI framework

**原文链接**: [https://www.neowin.net/news/microsoft-is-taking-steps-to-open-sourcing-windows-11-user-interface-framework/](https://www.neowin.net/news/microsoft-is-taking-steps-to-open-sourcing-windows-11-user-interface-framework/)

微软正逐步开源 Windows 11 的用户界面框架 WinUI，但由于该框架的复杂性及其与操作系统专有部分的深度集成，这是一个分阶段进行的方法。 完全开源 WinUI 并非一蹴而就，需要将其与这些依赖项分离。

该公司已制定了一个四阶段计划。 第一阶段侧重于增加内部提交镜像到 WinUI GitHub 仓库的频率，从而提高透明度。 第二阶段将使外部开发人员能够克隆并在本地构建存储库，并提供完整的设置文档。 第三阶段将允许通过 pull request 进行第三方贡献并在本地运行测试。 最终目标是使 GitHub 成为 WinUI 开发、问题跟踪和社区参与的主要枢纽，逐步淘汰内部镜像。

在此过程中，微软优先考虑安全性、稳定性以及对现有产品的支持。 开源之旅将是渐进的，开发人员可以在 GitHub 上跟踪其进展。 同时，开发人员可以通过提供反馈、报告问题和赞成现有反馈来做出贡献。

---

## 17. 用于语法高亮多行 YAML 字符串的 VSCode 扩展

**原文标题**: VSCode extension for syntax highlighting multi-line YAML strings

**原文链接**: [https://github.com/harrydowning/vscode-yaml-embedded-languages](https://github.com/harrydowning/vscode-yaml-embedded-languages)

此 VSCode 扩展“YAML 嵌入语言”通过为块标量中嵌入的代码提供语法高亮来增强 YAML 文件。它支持超过 50 种内置语言，并允许用户通过 `yaml-embedded-languages.include` 设置添加对其他语言的支持。

该扩展提供灵活的高亮选项：使用 `# <语言标识符>` 注释在块标识符旁边进行单块高亮，以及使用 `# yaml-embedded-languages: <语言标识符>` 进行连续高亮，以高亮所有后续块。可以使用 `# yaml-embedded-languages` 停止高亮。

该扩展列出了所有内置语言的有效语言标识符，例如 "python"（使用 "py" 或 "python" 作为标识符）、"javascript"（"js" 或 "javascript"）和 "html"（"html"）。

`yaml-embedded-languages.include` 设置允许用户使用正则表达式定义自定义语言标识符，并指定 TextMate 作用域名称以进行准确的高亮显示。该值可以指定语言名称（如果语言标识符不同），所需的作用域名称以及一个 "stripIndent" 标志。

该扩展不需要外部依赖项。已知问题和贡献指南以及详细说明更改的发行说明均可用。

---

## 18. Ana Marie Cox 论 Substack 作为一项业务的摇摇欲坠的基础

**原文标题**: Ana Marie Cox on the Shaky Foundation of Substack as a Business

**原文链接**: [https://newsletter.anamariecox.com/archive/substack-did-not-see-that-coming/](https://newsletter.anamariecox.com/archive/substack-did-not-see-that-coming/)

在她的时事通讯中，安娜·玛丽·考克斯认为Substack的商业模式从根本上是不可靠的，并对依赖它的记者构成风险。虽然承认Substack作为一个独立作家可访问的平台的吸引力，但她认为，在风险资本的驱动下，Substack追求成为像Twitter一样的“万能应用”是不可持续且可能有害的。

考克斯强调了几个危险信号，包括Substack难以获得其期望估值的资金，其越来越依赖于两极分化的内容来提高参与度，以及来自奥米德·马利克等人物的投资，表明可能转向意识形态的影响。她批评Substack吸引TikTok明星的雄心，认为此举偏离了其支持独立新闻业的初衷。

考克斯担心Substack对投资者的依赖将导致对不可持续增长的压力，这可能使其容易被寻求控制该平台用于政治目的的人收购，就像埃隆·马斯克收购Twitter一样。这可能会让记者们被困在一个不再符合他们价值观的平台上，因为离开会危及他们的收入。

她倡导记者探索替代平台，并鼓励支持为高风险写作提供社会安全网的倡议，强调需要集体支持而不是个人奋斗。最终，考克斯认为，虽然Substack提供了一个临时的解决方案，但它并不是解决媒体行业所面临挑战的长期答案。

---

## 19. 塞雷布拉斯代码

**原文标题**: Cerebras Code

**原文链接**: [https://www.cerebras.ai/blog/introducing-cerebras-code](https://www.cerebras.ai/blog/introducing-cerebras-code)

Cerebras推出Cerebras Code，该服务旨在通过开放权重编码模型Qwen3-Coder加速AI编码，提供高达每秒2000个token的速度和131k-token上下文窗口。该服务避免了专有IDE锁定和每周限制。

核心优势是近乎即时的代码生成，这对于涉及多个LLM调用的复杂代理工作流程至关重要。Qwen3-Coder是阿里巴巴推出的一个4800亿参数模型，在编码和代理任务方面可与Claude Sonnet 4和GPT-4.1相媲美。

Cerebras Code支持OpenAI兼容的推理端点，允许用户将其与现有的代码编辑器和Cursor、Continue.dev等工具集成，无需额外设置。

提供两种订阅计划：

*   **Cerebras Code Pro（50美元/月）：** 每天最多1000条消息，适合个人开发者和更简单的项目。
*   **Cerebras Code Max（200美元/月）：** 每天最多5000条消息，适用于全职开发、IDE集成、代码重构和多代理系统。

这两个计划都可以立即使用，无需等待，用户可以注册并立即开始编码。

---

## 20. Pet 2001 上的字符位图图形

**原文标题**: Character Bitmap Graphics on the Pet 2001

**原文链接**: [https://www.masswerk.at/nowgobang/2025/character-bitmaps-on-the-pet2001](https://www.masswerk.at/nowgobang/2025/character-bitmaps-on-the-pet2001)

本文探讨了如何在Commodore PET 2001这款图形功能有限的机器上实现“PECBM Graphics”——一种显示高分辨率图形的技术。PET 2001缺少专用的视频芯片，依赖于ROM中基于字符的图形，没有光栅中断或视频缓冲。Genesis Project的“A Bright Shining Star”演示通过每条光栅线操纵字符指针展示了这项技术，从而在垂直条带内实现了80像素宽的位图图形。

关键在于在每条扫描线分配的64个CPU周期内重写字符指针。通过策略性地改变显示的字符，利用字符ROM甚至反转字符集，可以实现更高分辨率图形的效果。

本文还重点介绍了先前的技术：Glen Fisher和Dave Dixon在1980年Cursor杂志上发表的一篇文章介绍了一个“Hi-Res”演示，该演示类似地在PET 2001上实现了字符位图图形，在9x5字符区域内操纵屏幕内存。这个早期的演示包含一个用BASIC实现的简陋图形命令语言。

本文详细介绍了“Hi-Res”演示背后的机器语言例程，解释了它是如何劫持系统中断以在屏幕渲染过程中重写字符的。通过仔细地控制内存写入的时序，可以在PET 2001硬件的限制下，创造出更高分辨率的假象。这两个演示都展现了克服PET 2001图形限制的惊人创造力。

---

## 21. Go 的竞态检测器存在互斥锁盲点

**原文标题**: Go's race detector has a mutex blind spot

**原文链接**: [https://doublefree.dev/go-race-mutex-blindspot/](https://doublefree.dev/go-race-mutex-blindspot/)

本文探讨了 Go 语言数据竞争检测器中一个与互斥锁相关的特定盲点。作者解释说，虽然 Go 的竞争检测器通常能有效地发现对共享内存的未同步并发访问，但在互斥锁存在但未持续用于保护共享变量的情况下，它可能会漏掉竞争。

作者提供了一个代码示例，其中两个 goroutine 递增一个受互斥锁保护的共享计数器，但其中一个 goroutine 在互斥锁之外执行额外的递增操作。竞争检测器并不总是检测到这种竞争，因为它将互斥锁的获取/释放建模为 "先发生" 关系。如果带有无保护递增的 goroutine 首先获取锁，则检测器会正确识别出竞争。但是，如果另一个 goroutine 首先获取锁，则 "先发生" 关系会使无保护的写入可以从受保护的写入访问到，从而导致检测器错过竞争。

本质上，当对共享变量的访问没有始终受到同一互斥锁的保护时，竞争检测器对互斥锁建立的 "先发生" 关系的依赖性可能会造成盲点。作者总结说，虽然 Go 的竞争检测器是一个优秀的工具，但理解其局限性对于确保无竞争代码至关重要。仅仅因为检测器报告没有竞争并不能保证不存在潜在的竞争条件。

---

## 22. ThinkPad设计师David Hill揭秘未面世的设计

**原文标题**: ThinkPad designer David Hill spills secrets, designs that never made it

**原文链接**: [https://www.theregister.com/2025/08/02/thinkpad_david_hill_interview/](https://www.theregister.com/2025/08/02/thinkpad_david_hill_interview/)

本文采访了戴维·希尔，他于1995年至2017年间在IBM和联想公司担任ThinkPad的首席设计师，探讨了ThinkPad的历史以及一些未上市的设计。希尔透露，他曾多次尝试在后来的型号中实现ThinkPad 701C的“蝴蝶键盘”，但均未成功。他还设想过一种可折叠的一体式桌面工作站，但最终未能实现。

采访深入探讨了希尔对TrackPoint指点杆的影响，重点介绍了他对红色指点帽的纹理和高度的改进，以及滚动按钮的实现。他还讨论了ThinkLight键盘灯，他构思了一种顶置键盘灯，强调其与背光相比的实用性和成本效益，并表达了对它停产的遗憾。

希尔回忆了联想收购IBM的ThinkPad，以及他通过打造高度成功的轻薄ThinkPad X300来证明联想对该品牌承诺的努力。他谈到了从七行键盘到六行键盘的争议性转变，将这种变化归因于不断变化的屏幕宽高比，同时承认人们对原始设计的怀旧之情。最后，他提到了他在ThinkPad 25周年纪念版上的工作，以及对恢复七行键盘的想法的压倒性积极回应。

---

## 23. Coffeematic PC – 一款向CPU泵送热咖啡的咖啡机电脑

**原文标题**: Coffeematic PC – A coffee maker computer that pumps hot coffee to the CPU

**原文链接**: [https://www.dougmacdowell.com/coffeematic-pc.html](https://www.dougmacdowell.com/coffeematic-pc.html)

道格·麦克道威尔的“Coffeematic PC”是一款独特的、自称“近乎自毁”的复古通用电气咖啡机与游戏电脑的混合体。它建于2024年，是咖啡机电脑谱系的一部分，但其独特之处在于使用煮好的Java咖啡作为CPU的冷却剂。热咖啡通过散热器泵送到CPU，然后返回到玻璃壶中，形成一个连续的循环，从而保持令人惊讶的稳定温度平衡。

这台电脑功能齐全，使用了废弃的电子元件（2000年代中期的主板、CPU、RAM、显卡）与新的硬件（SSD、电源、冷却系统）相结合，并在Linux Mint上运行。麦克道威尔提供了详细的零件清单，并将构建过程描述为跨越不同的技术时代。

文章探讨了咖啡机电脑的历史，指出2002年首次构建（“咖啡因机器”）与2018年第二次构建（“Zotac Mekspresso”）之间存在15年的空白。麦克道威尔推测了造成这种空白的原因，认为它可能反映了技术和文化方面的更广泛趋势。他在名为“Sparklines”的艺术展览中，以图表的形式将这个空白与计算机历史的时间线并列，并在展览中展示了“艺术家黑客”的手绘数据肖像。他邀请读者分享他可能遗漏的任何咖啡机电脑的知识。

---

## 24. 为什么皮革是最佳摩托车防护[视频]

**原文标题**: Why leather is best motorcycle protection [video]

**原文链接**: [https://www.youtube.com/watch?v=xwuRUcAGIEU](https://www.youtube.com/watch?v=xwuRUcAGIEU)

这段YouTube视频，标题为“为何皮革是最佳摩托车防护”，可能旨在解释骑摩托车时穿戴皮革装备的优势。然而，提供的文本片段仅包含标准的YouTube页脚信息，如版权声明、服务条款、隐私政策和联系平台的方式。它没有提供关于视频实际内容或其可能提出的支持皮革作为摩托车防护的论点的任何见解。因此，仅凭提供的文本无法总结视频的内容。

---

## 25. 冰山，正确的想法 – 错误的规范 – 第二部分，共二部分：规范

**原文标题**: Iceberg, the Right Idea – The Wrong Spec – Part 2 of 2: The Spec

**原文链接**: [https://www.database-doctor.com/posts/iceberg-is-wrong-2.html](https://www.database-doctor.com/posts/iceberg-is-wrong-2.html)

本文批判了 Apache Iceberg 规范，认为它是解决大型数据湖元数据问题的一种有缺陷的方法。文章强调了开放格式和 Parquet 作为通用存储格式的必要性，但指出如果没有适当的元数据管理、事务控制和模式演变，一堆 Parquet 文件就不是数据库表。

批判的重点在于 Iceberg 使用清单文件和清单列表（采用 AVRO 格式），它们包含指向 Parquet 文件和元数据的指针。作者认为这种设计会导致元数据膨胀，因为信息重复，并阻止了跨文件的高效压缩。具体来说，添加数据需要客户端编写包含指向*所有*清单文件的指针的清单列表，给客户端带来过多的簿记负担。

文章还声称行级安全性从根本上被破坏，因为客户端必须访问所有清单文件，从而暴露了所有 S3 文件的位置。 元数据文件设计需要列出创建的每个快照，这进一步加剧了空间效率低下。

最后，作者批评 Iceberg 的乐观并发控制，认为它不适合该规范的设计。 由于每次写入都会重复之前的元数据，因此并发写入*总是*会冲突，从而导致乐观并发失效。 该规范实际上对表的元数据使用了最糟糕的锁定语义。 作者认为，乐观并发只有在服务器可以解决写入冲突时才有效，而 Iceberg 的设计本身就阻止了这一点。

---

## 26. 17岁的汉娜·开罗解决了重要的数学谜题。

**原文标题**: At 17, Hannah Cairo solved a major math mystery

**原文链接**: [https://www.quantamagazine.org/at-17-hannah-cairo-solved-a-major-math-mystery-20250801/](https://www.quantamagazine.org/at-17-hannah-cairo-solved-a-major-math-mystery-20250801/)

本文介绍了汉娜·开罗，一位17岁的数学天才，她在伯克利修读研究生课程期间推翻了有40年历史的溝畑-竹内猜想。开罗在家自学，数学课程进展迅速，14岁时已自学了高等本科教材。由于感到孤立，她开始寻找数学社群，最终参加了伯克利的课程。

尽管她拥有非凡的能力，开罗仍然谦逊，对自己的天赋缺乏自信，在研究该猜想的过程中，她最初经历了挫折和怀疑。最终，她构建了一个打破预期的函数，证明该猜想是错误的。她的工作震惊并激励了数学界，激发了新的研究，并迫使人们重新评估相关的猜想。

本文着重介绍了开罗不同寻常的求学之路，她跳过了高中和本科学习，直接在马里兰大学攻读博士学位。文章强调了她的自主学习、毅力以及她已经对调和分析领域产生的重大影响。

---

## 27. JavaScript 复古音效生成器

**原文标题**: JavaScript retro sound effects generator

**原文链接**: [https://github.grumdrig.com/jsfxr/](https://github.grumdrig.com/jsfxr/)

此网页展示jsfxr，一款基于JavaScript的复古音效生成器。它是原始 "sfxr" 程序的网页移植版，允许用户直接在浏览器中创建经典的8位风格音效。

该界面提供了各种预设音效类型，如“拾取/硬币”、“激光/射击”、“爆炸”、“能量提升”、“击中/受伤”、“跳跃”和“嘟嘟声/选择”，以及生成随机声音、音调或变异现有声音的选项。

用户可以使用手动设置来微调音效，这些设置分为“包络”、“频率”、“琶音”、“占空比”、“重触发”、“镶边”、“低通滤波器”和“高通滤波器”等部分。每个部分包含攻击时间、持续时间、衰减时间、起始频率、滑音、颤音、截止频率和共振等参数，从而实现详细的自定义。

该生成器具有一个“播放”按钮来试听创建的声音。然后，用户可以通过右键单击链接并选择“另存为...”将生成的声音保存为 .wav 文件。该页面还显示有关生成声音的信息，包括文件大小、样本数量以及是否发生削波。创作者是 Eric Fredricksen，页面包含指向源代码的链接。

---

## 28. 基于ADS-B的天气模型

**原文标题**: Weather Model based on ADS-B

**原文链接**: [https://obrhubr.org/adsb-weather-model](https://obrhubr.org/adsb-weather-model)

尼古拉斯·奥伯胡贝尔的文章探讨了如何使用ADS-B数据构建天气模型。ADS-B数据是飞机广播的未加密消息，包含诸如位置、航向、地速和空速等信息。他使用RTL-SDR接收器和天线来收集这些数据，类似于为ADS-B Exchange等服务贡献数据的业余爱好者。

其核心思想是通过计算ADS-B数据中（空速，航向）矢量和（地速，航迹）矢量之间的差异来推断风矢量。通过聚合来自数千架飞机的数据，可以创建一个基本的风模型。此外，还可以提取温度和压力数据来增强传统气象模型，从而改进预报。

奥伯胡贝尔使用了来自ADS-B Exchange的历史ADS-B数据，并实现了一个受孙军研究启发的基于粒子的模型。该模型将飞机放置在网格上，在其周围生成粒子，并根据计算出的风矢量更新它们的位置，从而创建风向模式的可视化效果。

通过将其输出与卡梅伦·贝卡里奥的全球风向可视化进行比较，评估了模型的准确性，发现风向模式和速度非常接近，尤其是在地中海地区。这篇文章证明了利用现成的ADS-B数据构建一个出人意料的精确的风模型的潜力，突出了其在天气预报和可视化方面的价值。他还展示了一个模仿earth.nullschool.net风格的最终可视化效果。

---

## 29. 瓢虫月报

**原文标题**: This Month in Ladybird

**原文链接**: [https://ladybird.org/newsletter/2025-07-31/](https://ladybird.org/newsletter/2025-07-31/)

2025年7月瓢虫浏览器月度报告：本月，瓢虫浏览器项目取得显著进展。共合并来自47位贡献者的319个拉取请求，并迎来新的赞助商：Scraping Fish和Blacksmith。

主要进展包括Web平台测试取得实质性进展，新增13090个通过测试，总数达到1831856个，并修复了一个长期存在的postMessage问题，现在允许Google reCAPTCHA在google.com上通过。瓢虫浏览器现在支持高刷新率（高达120Hz），以实现更流畅的动画和滚动，并通过curl 8.14.0支持HTTP/3。

安全改进包括对Trusted Types的初步支持，以防止XSS攻击，以及增强了SVG foreignObject元素的处理方式。新增了CSS功能，如`content: url(...)`、`:state(foo)`和`:unchecked`伪类，以及逻辑属性组的改进。`var()`和`attr()`的实现已重写，以符合CSS规范。瓢虫浏览器现在支持`<syntax>`解析属性值，并正在扩展其用于CSS Houdini的`@property`实现。

最后，LibJS在内部过渡到原生UTF-16字符串，简化了实现并防止了与Unicode相关的错误。报告最后感谢众多个人的贡献。

---

## 30. 我没法提交PR，所以干脆自己入职把它修好了。

**原文标题**: I couldn't submit a PR, so I got hired and fixed it myself

**原文链接**: [https://www.skeptrune.com/posts/doing-the-little-things/](https://www.skeptrune.com/posts/doing-the-little-things/)

为了贡献代码，他/她竟然去这家公司上班了。

---

## 31. 编译器的强化模式

**原文标题**: Hardening mode for the compiler

**原文链接**: [https://discourse.llvm.org/t/rfc-hardening-mode-for-the-compiler/87660](https://discourse.llvm.org/t/rfc-hardening-mode-for-the-compiler/87660)

本提案概述了一项在Clang中引入“强化模式”的计划，旨在提高C和C++程序的安全性和安全性。作者认为，现有的安全机制分散、缺乏文档记录且不易访问。“强化模式”旨在将这些功能统一在一个用户友好的选项下。

核心思想是优先考虑安全和保障，即使这意味着可能会破坏现有代码。这需要用户明确预期，在强化模式下，编译器升级可能会导致破坏，但这应被视为一项功能，而不是缺陷。

该提案参考了GCC的`-fhardened`模式，但主张Clang追求自己的实现，以避免受到兼容性的限制。

强化模式的目标是默认启用各种`-f`、`-m`、`-D`和`-W`标志，启用标准库的强化模式，预定义与安全相关的宏，要求显式指定语言标准，拒绝针对不安全的旧标准进行编译，并传递诸如ASLR之类的链接器标志。

该提案提出了四种实现选项：

1.  **配置文件：** 使用Clang附带的配置文件。
2.  **驱动程序：** 引入一种新的驱动程序模式，以清晰地区分强化构建。
3.  **正交标志：** 使用单独的`-fhardened`、`-mhardened`和`-Whardened`选项。
4.  **单个标志：** 引入诸如`-fhardened`之类的单个标志以启用所有功能。

作者正在寻求社区对总体概念和首选实施方法的反馈，然后再制定包含特定标志和行为的详细提案。

---

## 32. 年度记事本

**原文标题**: Yearly Organiser

**原文链接**: [https://neatnik.net/calendar/](https://neatnik.net/calendar/)

本文提供一个可打印的2025年年历，设计成横向单页排布。 鼓励用户打印该日历，将其折叠起来，并用它来计划和跟踪全年的时间。 日历以网格格式显示每个月的日期（1月至12月）。 本文强调善待他人，并提供指向Neatnik的2026年日历和日历来源的链接。 此外，还建议在打印设置中禁用页眉和页脚，以获得最佳效果。

---

## 33. 以太同步：本地文本文件的点对点协同编辑

**原文标题**: Ethersync: Peer-to-peer collaborative editing of local text files

**原文链接**: [https://github.com/ethersync/ethersync](https://github.com/ethersync/ethersync)

Ethersync：本地文本文件实时协同编辑工具，支持文本编辑器多人模式。允许多用户同时编辑文件，查看彼此光标，并协作处理整个项目，无需中央服务器。连接采用端到端加密，且支持离线工作。

该工具可以通过预编译二进制文件（Linux、macOS、Android）、包管理器（如`yay`(Arch Linux)、`nix`或`cargo`）安装。Neovim和VS Code/Codium有相应的插件可用。

基本用法是在要共享的目录中运行`ethersync share`，其他人可以使用`ethersync join`，然后输入生成的代码进行连接。连接后，更改会立即同步。

该项目正在积极开发中，并已获得NLNet的NGI0 Core Fund和Prototype Fund的资助。它基于Automerge、Iroh和Magic Wormhole构建。欢迎贡献，特别是小型补丁，鼓励开发者参考插件开发指南来创建编辑器插件。该项目基于GNU Affero General Public License v3或更高版本授权。

---

## 34. 凯登思向中国军方大学出口半导体设计工具，认罪并支付1.4亿美元罚款

**原文标题**: Cadence Guilty, Pays $140M for Exporting Semi Design Tools to PRC Military Uni

**原文链接**: [https://www.justice.gov/opa/pr/cadence-design-systems-agrees-plead-guilty-and-pay-over-140-million-unlawfully-exporting](https://www.justice.gov/opa/pr/cadence-design-systems-agrees-plead-guilty-and-pay-over-140-million-unlawfully-exporting)

Cadence设计系统公司已同意认罪并支付超过1.4亿美元的刑事和民事罚款，原因是其非法向受限的中国军事院校——国防科技大学（NUDT）出口半导体设计工具。在2015年2月至2021年4月期间，Cadence及其中国子公司Cadence China共谋违反出口管制，通过幌子公司中南CAD中心（CSCC）和飞腾技术有限公司向国防科技大学提供EDA工具，且未获得必要的许可。国防科技大学因在其支持核与军事模拟的超级计算机中使用美国原产部件而被列入实体清单。

Cadence承认，其员工在国防科技大学安装了硬件，国防科技大学人员下载了软件，且明知国防科技大学的实体清单地位。员工向其他Cadence人员隐瞒了真实的接收方，并通过佣金激励销售。

罚款包括近1.18亿美元的刑事罚款和商务部处以的超过9500万美元的民事罚款。司法部和BIS协调了罚款，将部分付款记入对方，最终净支付超过1.4亿美元。鉴于Cadence未能自愿披露不当行为、违规行为的严重性以及其补救措施，达成了该决议，尽管Cadence因未主动披露信息而仅获得部分合作信用。

---

## 35. 苦涩的教训有极限吗？

**原文标题**: Does the Bitter Lesson Have Limits?

**原文链接**: [https://www.dbreunig.com/2025/08/01/does-the-bitter-lesson-have-limits.html](https://www.dbreunig.com/2025/08/01/does-the-bitter-lesson-have-limits.html)

本文探讨了“惨痛教训”的局限性，即利用计算的通用人工智能方法总是胜过以人为本、基于知识的方法。虽然承认惨痛教训在国际象棋和计算机视觉等领域的历史有效性，但作者认为它并非普遍适用。

作者介绍了组织理论的“垃圾桶模型”，强调了许多现实世界过程的混乱和缺乏记录的性质。这使得应用惨痛教训变得困难，因为组织难以定义高质量的输出，并为人工智能学习提供充足的高质量数据。现有的诸如 OKR 之类的指标通常具有还原性，并导致“玩弄”系统。

此外，文章认为简单地增加计算能力并不总是实用或最优的。以顶级国际象棋程序 Stockfish 为例，Stockfish 将巧妙的搜索算法与较小的、专门构建的深度学习模型相结合，而不是像 Leela 那样完全依赖于大规模计算，Leela 是一个严格遵循惨痛教训的模型。这使得 Stockfish 能够实现卓越的性能，并在功能较弱的硬件上运行。

同样，ARC-AGI-1 推理基准测试在使用昂贵计算的情况下获得了突破性分数，但最近的模型 (HRM) 通过专注于特定任务的训练，以远少于参数的数量实现了可比的分数。

作者总结说，虽然惨痛教训提供了宝贵的见解，但不应阻止开发人员在适当的时候应用自定义逻辑或使用非通用模型。计算是一种约束，以较低的成本获得略微降低的精度通常是实际应用的最佳方法。将挑战表示为数据的能力也至关重要，这在某些领域（如国际象棋）比其他领域（如工作场所动态）容易得多。

---

## 36. 小型自行车队形中的空气动力阻力：对受保护骑手的屏蔽作用 [pdf]

**原文标题**: Aerodynamic drag in small cyclist formations: shielding the protected rider [pdf]

**原文链接**: [http://www.urbanphysics.net/2025_Formation_Paper_Preprint_v1.pdf](http://www.urbanphysics.net/2025_Formation_Paper_Preprint_v1.pdf)

该PDF文档似乎是题为“小型自行车队形中的空气动力阻力：保护骑手的屏蔽作用”的科学文章内容，但内容以原始压缩格式呈现。

基于标题，该文章可能研究小型队形中的自行车手如何减少空气动力阻力，特别是对于受到保护的骑手。该研究可能探讨利用尾流的优势，即自行车手紧随另一位身后以减少空气阻力。它可能涉及实验或计算流体动力学（CFD）方法来量化不同队形所实现的阻力减少。

文章可能涵盖的关键主题包括：

*   **空气动力阻力：** 解释空气动力阻力的概念及其在自行车运动表现中的重要性。
*   **自行车队形：** 描述用于最小化阻力的各种自行车队形策略。
*   **屏蔽效应：** 分析队形中的领骑者如何减少后方骑手的阻力。
*   **骑手位置：** 自行车手在队形中的具体位置，以实现最佳的阻力减少（例如，距离，横向偏移）。
*   **实验或CFD方法：** 详细说明用于测量或模拟空气动力的方法。
*   **结果与讨论：** 介绍不同自行车队形实现的空气动力阻力减少的发现。
*   **实际意义：** 讨论结果对自行车队和个人自行车手的实际意义，提供对队形策略及其对表现的影响的见解。

由于提供的PDF内容无法阅读，因此无法在基于标题和自行车空气动力学常识的这些有根据的推论之外提供更具体的摘要。

---

## 37. 展示HN：画条鱼，看它和其它鱼一起游泳

**原文标题**: Show HN: Draw a fish and watch it swim with the others

**原文链接**: [https://drawafish.com](https://drawafish.com)

这个“Show HN”帖子邀请用户参与一个互动体验：画一条鱼（特别是面向右侧的鱼），然后观看它与其他用户创作的鱼一起游动。标题和“画一条鱼！”的指示简单明了，强调了核心活动。这种简单性暗示着一个有趣且引人入胜的项目，专注于用户创造力和共享的视觉体验。其含义是，绘制的鱼将被整合到一个虚拟环境或模拟中，从而创建一个协作的、不断进化的水下场景，其中充满了用户生成的内容。该项目可能旨在具有视觉吸引力、互动性和社区驱动性，提供一种展示用户创造力并创建共享虚拟空间的新颖方式。

---

## 38. 人工智能研究人员正在谈判2.5亿美元的薪酬方案。

**原文标题**: A.I. Researchers Are Negotiating $250 Million Pay Packages

**原文链接**: [https://www.nytimes.com/2025/07/31/technology/ai-researchers-nba-stars.html](https://www.nytimes.com/2025/07/31/technology/ai-researchers-nba-stars.html)

无法访问文章链接。

---

## 39. 罗伯特·威尔逊去世了

**原文标题**: Robert Wilson has died

**原文链接**: [https://www.theartnewspaper.com/2025/08/01/robert-wilson-playwright-director-artist-obituary](https://www.theartnewspaper.com/2025/08/01/robert-wilson-playwright-director-artist-obituary)

颇具影响力的实验戏剧家、导演和艺术家罗伯特·威尔逊，以其视觉效果惊人、风格独特的戏剧表演而闻名，因短暂疾病于纽约家中去世，享年83岁。威尔逊的职业生涯长达六十年，曾与菲利普·格拉斯、劳里·安德森、玛丽娜·阿布拉莫维奇和 Lady Gaga 等著名艺术家合作。

他因《聋人一瞥》等原创作品以及与菲利普·格拉斯合作的鸿篇巨制《海滩上的爱因斯坦》而获得认可，后者以其史诗般的长度和非传统的结构而闻名。威尔逊还执导了经典作品的改编版。他的戏剧风格拒绝自然主义，融入了默片、哑剧和各种音乐元素。威尔逊的艺术手法通常以视觉效果为先，光线在创造空间方面发挥了关键作用。

除了戏剧之外，威尔逊还是一位多产的视觉艺术家，创作绘画、雕塑和装置作品。他的作品曾在世界各地的机构展出，包括旧金山现代艺术博物馆、蓬皮杜中心和维特拉设计博物馆。他还为乔治·阿玛尼回顾展设计了展览。在 2010 年代，他创作了“视频肖像”系列，以古典绘画的风格描绘了 Lady Gaga 等人物。

威尔逊创立了纽约的艺术组织水磨坊中心，并在保守的环境中长大。他最初学习舞蹈是为了克服口吃，后来在普拉特学院学习建筑学。建筑学仍然是他作品的重要影响因素。

---

## 40. 在我的开发流程中替换 tmux

**原文标题**: Replacing tmux in my dev workflow

**原文链接**: [https://bower.sh/you-might-not-need-tmux](https://bower.sh/you-might-not-need-tmux)

在7+年每日使用后，本文详述了作者因担心tmux对终端生态系统的影响，以及对其颜色渲染、回滚、鼠标选择和缺乏对新型终端协议（如kitty图形协议）支持等问题的沮丧而放弃tmux的过程。

作者承认tmux在提供会话持久性和窗口管理方面的价值，但由于这些限制，他们探索了替代方案。他们讨论了诸如`ctrl-z`、`nohup`和`disown`等基本命令，但发现它们不足。

作者尝试了诸如`dtach`、`abduco`和`shpool`等轻量级替代方案，所有这些方案都侧重于会话持久性。虽然有希望，但他们发现这些方案存在错误，尤其是在从Neovim内部分离时。`shpool`成为最可行的选择，允许作者创建用于分离的键盘映射。

对于窗口管理，作者利用他们现有的窗口管理器（Ghostty和Sway+Foot）结合SSH。通过配置`ssh_config`并使用`autossh`，他们可以通过本地计算机无缝连接和管理远程服务器上的`shpool`会话。

最终，作者得出结论，他们已经成功取代了tmux，并指出改进的原生回滚、终端通知和标题是关键优势。他们承认`shpool`仍然存在问题，例如Neovim中的调整大小中断和缺乏“多人”支持，但认为这些权衡是值得的。

---

## 41. 研究人员绘制出太阳能带来最大气候效益的地区图

**原文标题**: Researchers map where solar energy delivers the biggest climate payoff

**原文链接**: [https://www.rutgers.edu/news/researchers-map-where-solar-energy-delivers-biggest-climate-payoff](https://www.rutgers.edu/news/researchers-map-where-solar-energy-delivers-biggest-climate-payoff)

本文介绍了两个不同的研究领域：一个侧重于太阳能及其气候影响，另一个探索华人老年群体中内化压力与认知能力下降之间的联系。

标题“研究人员绘制太阳能带来最大气候效益的地点”表明，一项研究旨在确定部署太阳能基础设施对减缓气候变化影响最大的地理位置。这意味着研究人员考虑了太阳辐射水平、电网基础设施和当地碳排放情况等因素，以确定太阳能项目的最佳位置。重点可能是一张地图或数据，揭示这些区域并量化在每个区域部署太阳能的潜在气候效益。

第二条信息“内化压力可能导致华人老年群体认知能力下降”总结了一项研究，该研究表明，在美籍华人老年人中，抑制或内化压力与认知功能下降之间存在相关性。这表明一项研究可能调查了抑制情绪和压力反应对该特定人群认知健康的心理和生理影响。该研究可能强调了具有文化敏感性的心理健康干预措施和压力管理技术的重要性，以可能预防或延缓华人老年群体的认知能力下降。

---

## 42. 帕洛阿尔托网络公司同意以250亿美元收购CyberArk

**原文标题**: Palo Alto Networks agrees to buy CyberArk for $25B

**原文链接**: [https://techcrunch.com/2025/07/30/palo-alto-networks-agrees-to-buy-cyberark-for-25-billion/](https://techcrunch.com/2025/07/30/palo-alto-networks-agrees-to-buy-cyberark-for-25-billion/)

Palo Alto Networks 宣布计划以 250 亿美元的现金加股票收购身份管理和安全公司 CyberArk。 这项于 2025 年 7 月 30 日宣布的收购标志着 Palo Alto 进入身份安全领域，也是该公司历史上最大的一笔收购。

在首席执行官 Nikesh Arora 的领导下，Palo Alto Networks 一直在进行收购，自 2018 年以来已花费超过 70 亿美元。 最近的收购包括 Dig Security、Talon Cyber Security 和 Bridgecrew。

这笔交易是 2025 年最大的网络安全收购案之一，仅次于谷歌以 320 亿美元收购 Wiz。 这项收购引人注目，因为它标志着 Palo Alto Networks 战略性地扩展到身份安全市场，并在其现有的网络安全解决方案组合的基础上进行构建。

---

## 43. Anthropic 撤销 OpenAI 对 Claude 的访问权限

**原文标题**: Anthropic revokes OpenAI's access to Claude

**原文链接**: [https://www.wired.com/story/anthropic-revokes-openais-access-to-claude/](https://www.wired.com/story/anthropic-revokes-openais-access-to-claude/)

Anthropic 撤销 OpenAI 对 Claude AI 模型的 API 访问权限，指控 OpenAI 违反其服务条款。Anthropic 声称 OpenAI 使用其 AI 编码工具 Claude Code 来改进其即将推出的 GPT-5 模型，这违反了禁止用户构建竞争产品或逆向工程 Claude 的条款。

据报道，OpenAI 使用特殊的开发者 API 对 Claude 进行测试，评估其编码、创意写作和安全响应。这使得 OpenAI 能够将其 Claude 的能力与自己的 AI 模型进行基准测试，并找出需要改进的领域。OpenAI 对此表示失望，称评估其他 AI 系统是行业进步和安全改进的标准做法，并指出 Anthropic 仍然可以访问 OpenAI 的 API。

Anthropic 表示，他们将确保 OpenAI 拥有 API 访问权限，用于基准测试和安全评估。这并非 Anthropic 首次限制访问；此前，他们因传闻 OpenAI 收购 AI 编码初创公司 Windsurf 而撤销了其访问权限。文章强调了 AI 行业的竞争性质，并引用了科技公司限制竞争对手 API 访问权限的类似案例。在切断 OpenAI 访问权限之前，Anthropic 宣布因高使用率和服务条款违规行为，对 Claude Code 实施速率限制。

---

## 44. 朝鲜派我出国当秘密IT人员。

**原文标题**: North Korea sent me abroad to be a secret IT worker

**原文链接**: [https://www.bbc.com/news/articles/c15wk77zxngo](https://www.bbc.com/news/articles/c15wk77zxngo)

朝鲜派遣公民海外充当秘密IT工人，绕过国际制裁为政权创收：脱北者揭露该计划利用虚假身份（通常从西方国家毫无戒心的人那里获得）来获得主要面向美国和欧洲公司的远程IT工作。这些工人以团队形式组织，将约85%的收入汇回朝鲜，每年贡献约2.5亿至6亿美元。

这种做法随着疫情期间远程工作的兴起而激增。虽然大多数工人只是为了赚钱，但有些人参与了数据盗窃、黑客攻击和敲诈勒索。美国当局已起诉几名参与这些行动的朝鲜人。

该文章强调了识别这些工人的困难，他们经常利用远程工作中缺乏面对面互动的特点。 然而，招聘经理们越来越意识到这个问题，并采取策略来识别可疑的候选人。 尽管存在叛逃的风险，包括其国内家人可能受到的惩罚，但像Jin-su这样的一些工人已经逃脱，并利用他们的IT技能来建立新的生活。 Jin-su证实了这些工人所经历的压迫性环境和有限的自由，强调了国外生活与朝鲜国内现实之间的巨大差异。

---

## 45. 告别谷歌应用商店

**原文标题**: Our Farewell from Google Play

**原文链接**: [https://secuso.aifb.kit.edu/english/2809.php](https://secuso.aifb.kit.edu/english/2809.php)

SECUSO研究组将于2025年停止在Google Play商店提供隐私友好应用，此前已提供八年注重隐私的主流应用替代品。该项目始于2016年的隐私友好手电筒，已发展到30多个应用，安装量超过35万次。该研究组感谢用户的支持。

退出原因是与F-Droid相比，在Google Play商店维护应用所需的精力日益增加，对于研究组而言不再可行。虽然现有安装仍然可以正常使用，但更新将会停止，可能导致与未来的Android更新出现兼容性问题。

SECUSO建议用户迁移到F-Droid商店以获得持续支持和更新，隐私友好应用仍将在那里提供。他们提供了迁移说明，以方便平稳过渡，同时保留用户数据。

---

## 46. 铁电助力突破晶体管极限

**原文标题**: Ferroelectric Helps Break Transistor Limits

**原文链接**: [https://spectrum.ieee.org/negative-capacitance-schottky-limit](https://spectrum.ieee.org/negative-capacitance-schottky-limit)

铁电材料助力突破晶体管极限

凯瑟琳·布尔扎克的文章《铁电材料助力突破晶体管极限》讨论了一种利用铁电材料提高氮化镓(GaN)晶体管性能的新方法。该文章于2025年7月28日发表在SemiconductorsNews上，重点介绍了铁电材料实现的负电容如何在没有晶体管设计中常见的性能权衡的情况下增强氮化镓器件。其意义在于，这项创新可能带来比当前限制允许的更高效、性能更好的晶体管。

---

## 47. 原生稀疏注意力

**原文标题**: Native Sparse Attention

**原文链接**: [https://aclanthology.org/2025.acl-long.1126/](https://aclanthology.org/2025.acl-long.1126/)

本文介绍原生稀疏注意力机制(NSA)，这是一种新颖的稀疏注意力机制，专为下一代语言模型中的高效长程上下文建模而设计。NSA通过将算法创新与硬件对齐优化相结合，解决了标准注意力机制的计算限制。它采用动态分层稀疏策略，结合粗粒度token压缩和细粒度token选择，有助于保持全局上下文感知和局部精度。

NSA的关键创新之处在于两点：首先，它通过算术强度平衡的算法设计和硬件优化实现了显著的加速。其次，它支持端到端训练，减少了预训练计算量，且不牺牲模型性能。

实验表明，使用NSA预训练的模型在各种基准测试中，包括通用任务、长程上下文任务和基于指令的推理，性能与全注意力模型相当甚至超过全注意力模型。此外，NSA在解码、前向传播和反向传播期间，在64k长度的序列上实现了相对于全注意力模型的显著加速，展示了其在整个模型生命周期中的效率。本文强调了NSA在高效且有效的长程上下文建模方面的潜力，使其成为该领域一个有希望的进步。

---

## 48. 忙碌开发者的柔术，第二部分：“我该怎么办？”

**原文标题**: Jujutsu for Busy Devs, Part 2: "How Do I?"

**原文链接**: [https://maddie.wtf/posts/2025-07-21-jujutsu-for-busy-devs/entry/1](https://maddie.wtf/posts/2025-07-21-jujutsu-for-busy-devs/entry/1)

这并非文章，而是一条机器人检测消息，具体来自名为Anubis的系统。该消息解释了用户为何遇到加载页面并被要求证明自己并非机器人。

要点总结：

*   **问题：** 人工智能公司正大量抓取网站数据，导致网站宕机并使合法用户无法访问资源。
*   **解决方案：** Anubis作为一种“够用就好”的临时方案被实施。它使用类似于Hashcash的工作量证明机制，使大规模机器人抓取成本高昂。
*   **技术解释：** Anubis需要JavaScript才能运行，因此用户需要确保JavaScript已启用，并禁用该域名的JShelter等插件。
*   **长期目标：** 工作量证明挑战是一种临时措施，目的是在开发出更好的识别无头浏览器（机器人使用）的方法之前使用，特别是侧重于字体渲染等指纹识别方法。
*   **原因：** 由于人工智能公司的行为，网站托管的动态正在发生变化，使用JavaScript和工作量证明是对这种情况的必要回应。目前正在开发无需JavaScript的解决方案。

---

## 49. Svalboard人体工学键盘半年回顾

**原文标题**: Ergonomic keyboarding with the Svalboard: a half-year retrospective

**原文链接**: [https://twey.io/hci/svalboard/](https://twey.io/hci/svalboard/)

本文是对作者使用Svalboard Lightly（一款以手指为导向的人体工学键盘）半年经验的回顾。作者是长期使用Dvorak键盘的用户，有重复性劳损病史，之前使用过Ergodox EZ等键盘，看重其分离式设计、倾斜角度、拇指键区和可编程性。最初，他们被CharaChorder所吸引，希望通过最小化手指移动和组合键来提高打字速度，但发现其闭源性质和人体工学设计不足。

Svalboard受DataHand启发，通过为每根手指设置按键群和红外按键检测来解决这些问题。作者称赞其QMK固件、Vial集成（通过Keybard）、可定制性和开放式设计。他们强调了轻松调整按键位置和配置的能力，从而显著提高了舒适度和工作效率。

然而，作者也指出了一些注意事项：轻微的制造质量问题（磁铁脱落）、价格高昂以及需要精确配置。键盘的灵敏度也可能会惩罚马虎的打字。最后，在Svalboard上重复按键可能比在传统键盘上更具挑战性。尽管存在这些缺点，作者仍然认为Svalboard是一款出色的设备，也是他们唯一的日常键盘，尤其是在使用椅子支架时。文章最后简要概述了作者特定的Svalboard设置。

---

## 50. 周六早晨的消失

**原文标题**: The Disappearance of Saturday Morning

**原文链接**: [https://www.awn.com/animationworld/disappearance-saturday-morning](https://www.awn.com/animationworld/disappearance-saturday-morning)

无法访问文章链接。

---

## 51. 打造你的专属备份系统 – 第二部分：构建 FreeBSD 备份堡垒

**原文标题**: Make Your Own Backup System – Part 2: Forging the FreeBSD Backup Stronghold

**原文链接**: [https://it-notes.dragas.net/2025/07/29/make-your-own-backup-system-part-2-forging-the-freebsd-backup-stronghold/](https://it-notes.dragas.net/2025/07/29/make-your-own-backup-system-part-2-forging-the-freebsd-backup-stronghold/)

本文详述如何以 FreeBSD 为核心构建一个安全备份系统。它强调对备份数据的完全控制，并提倡本地和远程备份，且内部副本独立于外部副本，以防止级联故障。

FreeBSD 因其通过 jail 或 VM 进行服务分区的能力而备受青睐，ZFS 因其灵活性和工具集而备受推荐。磁盘冗余（镜像、RaidZ1/2）对于备份数据完整性至关重要。

安全性至关重要。备份服务器应进行安全加固，最好仅通过 VPN 访问，或完全与互联网隔离。必须进行加密以保护数据，以防数据泄露。对于本地备份，建议使用 GELI 全盘加密，而对于远程服务器，首选 ZFS 原生加密。

本文提供了设置 GELI 加密和创建 ZFS 池的分步说明。然后介绍了基本系统设置，包括用于管理 jail 的 BastilleBSD 和用于运行诸如 Proxmox Backup Server 等 VM 的 vm-bhyve。还涵盖了网络桥接和防火墙配置。

最后，它讨论了备份策略，倾向于使用 zfs-autobackup 进行 FreeBSD/ZFS 环境备份，并使用 BorgBackup 进行非 ZFS 系统备份，强调了对备份服务器进行快照以减轻勒索软件风险的重要性。每个要备份的服务器都有其自己专用的 jail 以实现最大安全性。

---

## 52. 人类与人工智能语境的权衡

**原文标题**: The tradeoff between human and AI context

**原文链接**: [https://softwaredoug.com/blog/2025/07/30/layers-of-ai-coding](https://softwaredoug.com/blog/2025/07/30/layers-of-ai-coding)

道格·特恩布尔的文章讨论了使用AI编码工具时，人类和AI上下文之间的权衡。它提出了人类参与程度的光谱，从高级抽象讨论到完全的AI委托。关键思想是，开发者需要决定在自己脑海中保留多少上下文，以及将多少上下文委托给AI，从而平衡学习和效率。

文章概述了四个互动层级：

1.  **ChatGPT对话：** 使用ChatGPT进行基础教育和高级反思，类似于与另一家公司的同事讨论问题。价值在于重塑问题并获得视角。
2.  **Claude/Codex提问：** 在项目上下文中向AI询问有关代码的特定问题，就像咨询一位值得信赖的同事。这是深入学习和快速获得答案之间的权衡。
3.  **Claude/Codex建议修改：** 允许AI提出修改建议，由人类选择性地采纳。当不确定AI对特定语言或框架的理解时，这很有用。
4.  **Claude/Codex实际编码：** 将任务委托给AI，并设置安全措施以防止错误，适用于核心技术。用户需要仔细调整给予AI的自由度。

最终，文章强调每个层级都涉及人类处理的上下文量与AI处理的上下文量之间的权衡，以及对AI能力的信任程度。作者最后鼓励读者考虑这种平衡，就像管理一家公司一样，并推广了他关于将LLM应用于搜索应用程序的课程。

---

## 53. 售出的故事：儿童阅读教学为何误入歧途

**原文标题**: Sold a Story: How Teaching Kids to Read Went So Wrong

**原文链接**: [https://features.apmreports.org/sold-a-story/](https://features.apmreports.org/sold-a-story/)

售卖的故事：儿童阅读教学为何误入歧途

---

## 54. OpenAI“学习模式”与谄媚的风险

**原文标题**: OpenAI's "Study Mode" and the risks of flattery

**原文链接**: [https://resobscura.substack.com/p/openais-new-study-mode-and-the-risks](https://resobscura.substack.com/p/openais-new-study-mode-and-the-risks)

无法访问文章链接。

---

## 55. 出售：1990年款 Airstream NASA 025 指挥车。千载难逢。

**原文标题**: For Sale: 1990 Airstream NASA 025 Command Vehicle. Once-in-a-Lifetime

**原文链接**: [https://www.hemmings.com/listing/1990-airstream-all-models-478166](https://www.hemmings.com/listing/1990-airstream-all-models-478166)

这辆Hemmings.com的房车出售信息广告了一件独特的历史：一辆1990年款的Airstream NASA 025指挥车。它被描述为“一生只有一次的投资机会”，这辆定制的34英尺Airstream房车最初被设计用于在爱德华兹空军基地降落载人任务，并作为现场指挥中心。

卖方由于一次沟通失误从范登堡空军基地获得了这辆车，当时美国国家航空航天局的销售团队并不了解它的重要性。他们强调了该车辆作为营销工具的潜力，预计可带来显著的租金收入（15万美元以上）和活动吸引力，超过了典型的租赁房产回报。

该车辆仅行驶了8240英里，目前在加利福尼亚州处于运行状态。出售包括大量文件，包括3000多页和完整的CAD图纸和计划。卖方已投资45,000美元用于创建竣工图。该车辆保留了其原始的美国国家航空航天局状态，但目前涂成白色底色，带有红色/蓝色细节。

该清单强调了该车辆的稀有性，声明它是唯一出售给公众的带有美国国家航空航天局标签的单元。虽然其他美国国家航空航天局的Airstream房车存在于博物馆中，但那些是乘员运输车，而不是指挥车。由于其ITAR指定，这辆Airstream房车不能出口或出售给敌对实体，只能用于娱乐或获得国务院许可。该车辆正在出售，不接受任何交易。

---

## 56. 双子座2.5深度思考

**原文标题**: Gemini 2.5 Deep Think

**原文链接**: [https://blog.google/products/gemini/gemini-2-5-deep-think/](https://blog.google/products/gemini/gemini-2-5-deep-think/)

Gemini 应用将于 2025 年 8 月 1 日向 Google AI Ultra 订阅用户推出“深度思考”。“深度思考”是 Gemini 2.5 模型的一个变体，在国际数学奥林匹克竞赛 (IMO) 中达到了金牌标准，并且代表了对先前模型的重大改进，即使在其更快、更可用的形式中，也在 2025 年 IMO 基准测试中达到了铜牌水平。 一小部分数学家和学者正在获得完整金牌版本的访问权限。

“深度思考”采用并行思考技术，使 AI 能够同时生成和考虑多个想法，通过延长“思考时间”和新颖的强化学习技术来提高解决问题的能力。它擅长创造性问题解决，包括迭代开发和设计、科学和数学发现以及算法开发和编码。

“深度思考”在编码、科学、知识和推理基准测试（如 LiveCodeBench V6 和 Humanity's Last Exam）中表现出最先进的性能。 Google 强调正在努力将安全性和责任融入 Gemini，并指出与 Gemini 2.5 Pro 相比，“深度思考”中的内容安全性有所提高，但对良性请求的拒绝率也更高。

Google AI Ultra 订阅用户可以在 Gemini 应用程序中访问“深度思考”，每天有一定数量的提示，并使用代码执行和 Google 搜索等工具。该公司计划通过 Gemini API 向开发者和企业用户发布带有和不带工具的“深度思考”给可信测试者。

---

## 57. 里科弗文集：里科弗海军上将演讲和备忘录数字档案馆

**原文标题**: The Rickover Corpus: A digital archive of Admiral Rickover's speeches and memos

**原文链接**: [https://rickovercorpus.org/](https://rickovercorpus.org/)

里科弗文集设想为一个包含海曼·G·里科弗海军上将演讲和备忘录的数字档案馆。该文件很可能是一份提案或项目描述，概述了创建此存储库的意图。虽然该文件本身细节不足，但我们可以推断出该档案馆将围绕特定的内容片段构建，每个条目可能包括：

*   **标题：**演讲或备忘录的标题。
*   **年份：**发表或撰写演讲或备忘录的年份。
*   **摘要：**内容的简短描述或概要。
*   **来源：**演讲或备忘录的原始来源（例如，出版物、文集等）。
*   **链接：**指向演讲或备忘录全文的指针，很可能直接是数字文件或指向外部网站的链接。

里科弗文集的目的大概是为了保存并使里科弗海军上将的著作和声明可访问，从而促进对他在各种主题（可能包括核能、教育和领导力）的观点的研究和理解。该文件作为该项目的初始框架，突出了计划包含在档案馆中的关键要素。档案馆的成功取决于收集相关材料并以所述格式组织它们。

---

## 58. Hyper 如何构建百万级精度室内 GPS

**原文标题**: How Hyper built a 1M-accurate indoor GPS

**原文链接**: [https://andrewhart.me/hyper/](https://andrewhart.me/hyper/)

安德鲁·哈特打造Hyper，一种1米精度的室内GPS的旅程，源于零售商对不准确室内导航的沮丧。他意识到现有的蓝牙信标、WiFi、磁力计和计算机视觉等解决方案，由于精度、可扩展性或用户体验问题而不足。

哈特创立Hyper是为了解决这个根本问题。他们的解决方案结合了WiFi定位和SLAM（即时定位与地图构建），也就是自动驾驶汽车背后的技术。WiFi提供最初的“蓝点”，而SLAM利用加速度计、陀螺仪和摄像头数据，追踪精确运动，将位置精度提升到1米。

为了克服SLAM漂移（随时间累积的误差）和方向不确定性等挑战，Hyper开发了锚定到WiFi数据的算法，并模拟运动场景来确定准确的航向。他们还创建了一个自助式调查应用程序，允许商店员工绘制WiFi信号强度图，从而提高可扩展性并降低成本。

最终成果是一种精确可靠的室内GPS体验，为高级AR导航提供支持。Hyper已经在大型零售商店秘密部署了这项技术，现在正专注于扩展到十亿用户，并寻求更大的合作伙伴来实现企业级规模的发行。他们的目标是将精确的室内导航带到各种室内空间，提高效率并改善用户体验。

---

## 59. Google更改goo.gl政策：非活跃链接停用，活跃链接保留

**原文标题**: Google shifts goo.gl policy: Inactive links deactivated, active links preserved

**原文链接**: [https://blog.google/technology/developers/googl-link-shortening-update/](https://blog.google/technology/developers/googl-link-shortening-update/)

谷歌正在修改停用 goo.gl 网址的计划。原本所有 goo.gl 链接计划于 2025 年 8 月 25 日后停用。但由于用户反馈，谷歌现在将保留活跃使用的链接。只有 2024 年底处于非活跃状态且目前重定向至显示未来停用信息的 goo.gl 链接会受到影响。这些链接将于 8 月 25 日后停止工作，建议用户过渡到其他网址缩短服务。所有其他正常重定向且没有停用信息的 goo.gl 链接将继续正常工作。用户可以通过访问链接来检查其链接是否会被保留；如果它们在没有警告信息的情况下重定向，则它们将保持活动状态。

---

## 60. Anandtech.com 现在重定向至其论坛。

**原文标题**: Anandtech.com now redirects to its forums

**原文链接**: [https://forums.anandtech.com/](https://forums.anandtech.com/)

Anandtech.com 现在重定向至其论坛，该论坛是关于技术、硬件、软件和交易讨论的中心。论坛按主题分类，包括 CPU、主板、显卡、内存、显示器、电源、机箱、笔记本电脑、网络、苹果产品、外围设备、电脑组装、消费电子产品、主机游戏、移动设备、音频、电视以及各种软件和操作系统类别。

论坛还包括专门讨论购物优惠、社交讨论、政治、技术问题、汽车话题、健康、家居装修和论坛反馈的部分。用户可以加入社区参与讨论、提问和分享他们的知识。

主页显示来自各个论坛的热门帖子和最新帖子，涵盖诸如 CPU 猜测、英特尔的未来处理器计划、Apple Silicon 和股票市场等主题。该网站是 Future plc 的一部分，并提供诸如广告信息、Cookie 政策、隐私信息以及条款和条件等资源。它还鼓励用户在 Facebook 和 Twitter 上关注 AnandTech。

---

## 61. 编写“永久产权”软件

**原文标题**: Write "Freehold" Software

**原文链接**: [https://deadbeef.io/freehold_software?resubmit=hn](https://deadbeef.io/freehold_software?resubmit=hn)

这篇“文章”似乎只是一行字，建议将软件命名为“Freehold”，接着是一个域名（“deadbeef.io”），该域名导向一个显示“发生未知错误”的错误页面。

因此，没有实质内容可供总结。 这篇“文章”没有提供任何关于以下方面的信息：

*   **“Freehold”软件是什么：** 没有对该软件的用途、功能或目标受众的描述。
*   **与 deadbeef.io 的联系：** 该域名可能属于与“Freehold”软件相关的开发人员或组织，但该错误阻止了任何进一步的调查。
*   **选择名称“Freehold”的原因：** 没有对建议名称的解释或理由。

本质上，这篇“文章”仅仅是一个建议和一个失效的链接，除了建议名称“Freehold”和一个无法正常使用的域名之外，没有提供任何具体信息或有意义的内容可供总结。

---

## 62. 二十七 1.0

**原文标题**: Twentyseven 1.0

**原文链接**: [https://blog.poisson.chat/posts/2025-08-01-twentyseven.html](https://blog.poisson.chat/posts/2025-08-01-twentyseven.html)

"Twentyseven" 是一款基于 Haskell 的魔方解算器，是作者的一个长期项目，为了确保与最新 GHC 的兼容性，发布了 1.0.0 版本。作者强调 Haskell 非常适合解决像魔方这样的数学问题，因为它融合了编程和数学能力，尤其适用于群论的应用。

该解算器受到 Herbert Kociemba 的 "Cube Explorer" 的启发，使用迭代加深 A* (IDA*) 算法来寻找最短解法路径。由于魔方状态空间的巨大性，IDA* 因其内存效率而更受青睐，它采用具有递增移动限制的深度优先搜索。该算法依赖于从将魔方状态投影到更简单的拼图（如角块排列）中得出的启发式算法来估计剩余移动。

虽然 "Twentyseven" 提供最佳解，但与 Kociemba 的 Cube Explorer 相比，速度可能较慢，这可能是由于启发式选择造成的。"Twentyseven" 也实现了 Kociemba 的两阶段算法，这是一种更快但并非最佳的替代方案。该算法将求解过程分为两个阶段：第一阶段确定魔方小块的方向并分离边缘，第二阶段限制移动以保持这种方向并切割边缘，从而显着减少搜索空间。

---

## 63. 自签名JWT

**原文标题**: Self-Signed JWTs

**原文链接**: [https://www.selfref.com/self-signed-jwts](https://www.selfref.com/self-signed-jwts)

本文批判了传统API密钥管理的复杂性和麻烦，并提出了一种使用自签名JSON Web令牌 (JWT) 的简化替代方案。开发者可以本地生成自己的JWK密钥对，从而有效创建自己的自颁发API密钥，而无需依赖外部服务来生成和管理API密钥。

作者提倡消除“秘密”密钥和“可发布”密钥以及单独的客户端/管理SDK之间的区别。特权操作通过嵌入在JWT中的声明进行控制，该声明使用应用程序的私有JWK进行签名。 客户端SDK随后将签名的JWT附加到请求。服务器使用相应的公共JWK验证JWT签名，并根据声明授权操作。

文章进一步讨论了API货币化，建议来自未付费帐户的请求返回一个支付URL，并在支付后将公钥与付费帐户关联。

最后，文章探讨了B2B2C场景，提出了一种分层JWK派生方法。开发者创建主JWK，并为其最终用户派生子JWK。 JWT包含一个零知识证明，用于验证最终用户的密钥是从开发者的主密钥派生的，从而可以在无需开发者管理单个API密钥的情况下验证最终用户的授权。

---

## 64. 深度智能体

**原文标题**: Deep Agents

**原文链接**: [https://blog.langchain.com/deep-agents/](https://blog.langchain.com/deep-agents/)

本文探讨了“深度代理”的概念，它们比仅仅通过工具调用循环的简单LLM驱动的代理更具能力。这些深度代理擅长规划和执行跨越更长时间范围的复杂任务，并从Claude Code、Manus和Deep Research agent等成功案例中汲取灵感。

作者确定了区分深度代理的四个关键特征：

1.  **详细的系统提示：** 复杂而全面的提示为工具的使用和期望的行为提供了具体的说明和示例。
2.  **规划工具：** 即使是一个简单的、非功能性的规划工具（如待办事项清单）也有助于代理保持专注并跟踪多步骤任务的进度。
3.  **子代理：** 生成子代理的能力允许任务分解和专业化关注，从而提高上下文管理和效率。
4.  **文件系统：** 访问文件系统使代理能够存储和检索信息、管理大量上下文，并促进子代理之间的协作。

文章最后介绍了一个名为“deepagents”的开源Python包，旨在简化自定义深度代理的创建。该软件包包括一个通用的系统提示、一个待办事项清单规划工具、子代理生成功能和一个虚拟文件系统。开发者可以通过提供自定义提示、工具和子代理来为特定的垂直应用定制代理。文中还提到了一个简单的“深度研究”代理示例。

---

## 65. Supporting the BEAM community with free CI/CD security audits

**原文标题**: Supporting the BEAM community with free CI/CD security audits

**原文链接**: [https://www.erlang-solutions.com/blog/supporting-the-beam-community-with-free-ci-cd-security-audits/](https://www.erlang-solutions.com/blog/supporting-the-beam-community-with-free-ci-cd-security-audits/)

Erlang Solutions is offering free CI/CD-based security audits for open-source Erlang and Elixir projects to support the BEAM community. These audits, powered by their SAFE (Security Audit for Erlang/Elixir) tool, integrate directly into development pipelines (like GitHub Actions), automatically scanning for vulnerabilities with each code commit or update. This helps projects detect issues early, maintain a secure codebase, and improve risk visibility. Results are delivered quickly, providing clear and actionable feedback.

Open-source maintainers can request a free SAFE license by emailing safe@erlang-solutions.com, providing a link to their repository. Licenses are granted for one month to a year, depending on the project's needs.

Beyond the free audits, Erlang Solutions also offers expert-led audit services for production BEAM systems, including code reviews, architecture assessments, and performance audits. These are suited for complex or critical systems and complement SAFE audits.

Erlang Solutions demonstrates a broader commitment to the BEAM community through sponsorship of events like Code Sync, support for the Erlang Ecosystem Foundation (EEF), backing inclusion initiatives like Women in BEAM, and sharing learning resources. They aim to support the ecosystem through expertise and action, ensuring secure, scalable, and reliable BEAM-based systems.


---

## 66. Show HN: TraceRoot – Open-source agentic debugging for distributed services

**原文标题**: Show HN: TraceRoot – Open-source agentic debugging for distributed services

**原文链接**: [https://github.com/traceroot-ai/traceroot](https://github.com/traceroot-ai/traceroot)

生成摘要时出错

---

## 67. A DH106 1A Comet has been restored at the de Havilland Aircraft Museum

**原文标题**: A DH106 1A Comet has been restored at the de Havilland Aircraft Museum

**原文链接**: [https://www.cnn.com/travel/de-havilland-comet-dh106-first-passenger-jet](https://www.cnn.com/travel/de-havilland-comet-dh106-first-passenger-jet)

生成摘要时出错

---

## 68. Tim Cook rallying Apple employees around AI efforts

**原文标题**: Tim Cook rallying Apple employees around AI efforts

**原文链接**: [https://www.bloomberg.com/news/articles/2025-08-01/apple-ceo-tells-staff-ai-is-ours-to-grab-in-hourlong-pep-talk](https://www.bloomberg.com/news/articles/2025-08-01/apple-ceo-tells-staff-ai-is-ours-to-grab-in-hourlong-pep-talk)

生成摘要时出错

---

## 69. Pseudo, a Common Lisp macro for pseudocode expressions

**原文标题**: Pseudo, a Common Lisp macro for pseudocode expressions

**原文链接**: [http://funcall.blogspot.com/2025/07/pseudo.html](http://funcall.blogspot.com/2025/07/pseudo.html)

生成摘要时出错

---

## 70. Slow

**原文标题**: Slow

**原文链接**: [https://michaelnotebook.com/slow/index.html](https://michaelnotebook.com/slow/index.html)

生成摘要时出错

---

## 71. Show HN: An interactive dashboard to explore NYC rentals data

**原文标题**: Show HN: An interactive dashboard to explore NYC rentals data

**原文链接**: [https://leaseswap.nyc/analytics](https://leaseswap.nyc/analytics)

生成摘要时出错

---

## 72. The Math Is Haunted

**原文标题**: The Math Is Haunted

**原文链接**: [https://overreacted.io/the-math-is-haunted/](https://overreacted.io/the-math-is-haunted/)

生成摘要时出错

---

## 73. The AI age is the "age of no consent"

**原文标题**: The AI age is the "age of no consent"

**原文链接**: [https://productpicnic.beehiiv.com/p/the-ai-age-is-the-age-of-no-consent-7559](https://productpicnic.beehiiv.com/p/the-ai-age-is-the-age-of-no-consent-7559)

生成摘要时出错

---

## 74. OpenAI raises $8.3B at $300B valuation

**原文标题**: OpenAI raises $8.3B at $300B valuation

**原文链接**: [https://www.nytimes.com/2025/08/01/business/dealbook/openai-ai-mega-funding-deal.html](https://www.nytimes.com/2025/08/01/business/dealbook/openai-ai-mega-funding-deal.html)

生成摘要时出错

---

## 75. Vikings grew barley in Greenland – climate was mild when they landed

**原文标题**: Vikings grew barley in Greenland – climate was mild when they landed

**原文链接**: [https://www.sciencenordic.com/agriculture-archaeology-denmark/vikings-grew-barley-in-greenland/1447746](https://www.sciencenordic.com/agriculture-archaeology-denmark/vikings-grew-barley-in-greenland/1447746)

生成摘要时出错

---

## 76. The First Widespread Cure for HIV Could Be in Children

**原文标题**: The First Widespread Cure for HIV Could Be in Children

**原文链接**: [https://www.wired.com/story/the-first-widespread-cure-for-hiv-could-be-in-children/](https://www.wired.com/story/the-first-widespread-cure-for-hiv-could-be-in-children/)

生成摘要时出错

---

## 77. Fast (2019)

**原文标题**: Fast (2019)

**原文链接**: [https://patrickcollison.com/fast](https://patrickcollison.com/fast)

生成摘要时出错

---

## 78. Hyrum's Law

**原文标题**: Hyrum's Law

**原文链接**: [https://www.hyrumslaw.com](https://www.hyrumslaw.com)

生成摘要时出错

---

## 79. Replacing cron jobs with a centralized task scheduler

**原文标题**: Replacing cron jobs with a centralized task scheduler

**原文链接**: [https://mayhul.com/posts/scheduled-tasks/](https://mayhul.com/posts/scheduled-tasks/)

生成摘要时出错

---

## 80. Programmers aren’t so humble anymore, maybe because nobody codes in Perl

**原文标题**: Programmers aren’t so humble anymore, maybe because nobody codes in Perl

**原文链接**: [https://www.wired.com/story/programmers-arent-humble-anymore-nobody-codes-in-perl/](https://www.wired.com/story/programmers-arent-humble-anymore-nobody-codes-in-perl/)

生成摘要时出错

---

## 81. Build an AI telephony agent for inbound and outbound calls

**原文标题**: Build an AI telephony agent for inbound and outbound calls

**原文链接**: [https://github.com/videosdk-community/ai-telephony-demo](https://github.com/videosdk-community/ai-telephony-demo)

生成摘要时出错

---

## 82. Corporation for Public Broadcasting ceasing operations

**原文标题**: Corporation for Public Broadcasting ceasing operations

**原文链接**: [https://cpb.org/pressroom/Corporation-Public-Broadcasting-Addresses-Operations-Following-Loss-Federal-Funding](https://cpb.org/pressroom/Corporation-Public-Broadcasting-Addresses-Operations-Following-Loss-Federal-Funding)

生成摘要时出错

---

## 83. Show HN: Print the daily weather forecast on a thermal receipt printer

**原文标题**: Show HN: Print the daily weather forecast on a thermal receipt printer

**原文链接**: [https://github.com/chr15m/print-weather](https://github.com/chr15m/print-weather)

生成摘要时出错

---

## 84. The untold impact of cancellation

**原文标题**: The untold impact of cancellation

**原文链接**: [https://pretty.direct/impact](https://pretty.direct/impact)

生成摘要时出错

---

## 85. A criminal enterprise run by monkeys

**原文标题**: A criminal enterprise run by monkeys

**原文链接**: [https://www.wsj.com/lifestyle/monkeys-thieves-bali-temple-0b63a432](https://www.wsj.com/lifestyle/monkeys-thieves-bali-temple-0b63a432)

生成摘要时出错

---

## 86. 150 years of Hans Christian Andersen

**原文标题**: 150 years of Hans Christian Andersen

**原文链接**: [https://www.newstatesman.com/culture/books/book-of-the-day/2025/07/150-years-of-the-bizarre-hans-christian-andersen](https://www.newstatesman.com/culture/books/book-of-the-day/2025/07/150-years-of-the-bizarre-hans-christian-andersen)

生成摘要时出错

---

## 87. What's Not to Like?

**原文标题**: What's Not to Like?

**原文链接**: [https://theamericanscholar.org/whats-not-to-like/](https://theamericanscholar.org/whats-not-to-like/)

生成摘要时出错

---

## 88. Andrew Ng and Yann LeCun: US Is Losing AI Race Due to Closed Models

**原文标题**: Andrew Ng and Yann LeCun: US Is Losing AI Race Due to Closed Models

**原文链接**: [https://haebom.dev/archive?post=1q3vdn2p97v8xmxy49pr](https://haebom.dev/archive?post=1q3vdn2p97v8xmxy49pr)

生成摘要时出错

---

## 89. Every satellite orbiting earth and who owns them (2023)

**原文标题**: Every satellite orbiting earth and who owns them (2023)

**原文链接**: [https://dewesoft.com/blog/every-satellite-orbiting-earth-and-who-owns-them](https://dewesoft.com/blog/every-satellite-orbiting-earth-and-who-owns-them)

生成摘要时出错

---

## 90. Qwen3 Coder 480B is Live on Cerebras

**原文标题**: Qwen3 Coder 480B is Live on Cerebras

**原文链接**: [https://www.cerebras.ai/blog/qwen3-coder-480b-is-live-on-cerebras](https://www.cerebras.ai/blog/qwen3-coder-480b-is-live-on-cerebras)

生成摘要时出错

---

## 91. Face it: you're a crazy person

**原文标题**: Face it: you're a crazy person

**原文链接**: [https://www.experimental-history.com/p/face-it-youre-a-crazy-person](https://www.experimental-history.com/p/face-it-youre-a-crazy-person)

生成摘要时出错

---

## 92. Problem solving using Markov chains (2007) [pdf]

**原文标题**: Problem solving using Markov chains (2007) [pdf]

**原文链接**: [http://math.uchicago.edu/~shmuel/Network-course-readings/Markov_chain_tricks.pdf](http://math.uchicago.edu/~shmuel/Network-course-readings/Markov_chain_tricks.pdf)

生成摘要时出错

---

## 93. OpenAI's ChatGPT Agent casually clicks through "I am not a robot" verification

**原文标题**: OpenAI's ChatGPT Agent casually clicks through "I am not a robot" verification

**原文链接**: [https://arstechnica.com/information-technology/2025/07/openais-chatgpt-agent-casually-clicks-through-i-am-not-a-robot-verification-test/](https://arstechnica.com/information-technology/2025/07/openais-chatgpt-agent-casually-clicks-through-i-am-not-a-robot-verification-test/)

生成摘要时出错

---

## 94. Fast

**原文标题**: Fast

**原文链接**: [https://www.catherinejue.com/fast](https://www.catherinejue.com/fast)

生成摘要时出错

---

## 95. New research finds that ivermectin could help control malaria transmission

**原文标题**: New research finds that ivermectin could help control malaria transmission

**原文链接**: [https://www.ndm.ox.ac.uk/news/new-research-supports-ivermectin-as-an-effective-strategy-to-control-malaria-transmission](https://www.ndm.ox.ac.uk/news/new-research-supports-ivermectin-as-an-effective-strategy-to-control-malaria-transmission)

生成摘要时出错

---

## 96. Show HN: Mcp-use – Connect any LLM to any MCP

**原文标题**: Show HN: Mcp-use – Connect any LLM to any MCP

**原文链接**: [https://github.com/mcp-use/mcp-use](https://github.com/mcp-use/mcp-use)

生成摘要时出错

---

## 97. When Flatpak's Sandbox Cracks

**原文标题**: When Flatpak's Sandbox Cracks

**原文链接**: [https://www.linuxjournal.com/content/when-flatpaks-sandbox-cracks-real-life-security-issues-beyond-ideal](https://www.linuxjournal.com/content/when-flatpaks-sandbox-cracks-real-life-security-issues-beyond-ideal)

生成摘要时出错

---

## 98. Carbon Language: An experimental successor to C++

**原文标题**: Carbon Language: An experimental successor to C++

**原文链接**: [https://docs.carbon-lang.dev/](https://docs.carbon-lang.dev/)

生成摘要时出错

---

## 99. Man Kept a Meticulous List of All 3,599 Books He'd Read Since 1962

**原文标题**: Man Kept a Meticulous List of All 3,599 Books He'd Read Since 1962

**原文链接**: [https://www.smithsonianmag.com/smart-news/this-man-kept-a-meticulous-list-of-all-3599-books-hed-read-since-1962-when-he-died-his-family-published-it-online-180987074/](https://www.smithsonianmag.com/smart-news/this-man-kept-a-meticulous-list-of-all-3599-books-hed-read-since-1962-when-he-died-his-family-published-it-online-180987074/)

生成摘要时出错

---

## 100. Show HN: AgentMail – Email infra for AI agents

**原文标题**: Show HN: AgentMail – Email infra for AI agents

**原文链接**: [https://chat.agentmail.to/](https://chat.agentmail.to/)

生成摘要时出错

---

