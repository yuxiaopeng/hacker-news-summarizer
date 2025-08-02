# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-02.md)

*最后自动更新时间: 2025-08-02 17:49:15*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 2 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 3 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 4 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 5 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 6 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 7 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 8 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 9 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 10 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 11 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 12 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 13 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 14 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 15 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 16 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 17 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 18 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 19 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 20 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 21 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 22 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 23 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 24 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 25 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 26 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 27 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 28 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 29 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 30 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 31 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 32 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 33 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 34 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 35 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 36 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 37 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 38 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 39 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 40 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 41 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 42 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 43 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 44 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 45 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 46 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 47 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 48 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 49 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 50 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 51 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 52 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 53 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 54 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 55 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 56 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 57 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 58 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 59 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 60 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 61 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 62 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 63 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 64 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 65 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 66 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 67 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 68 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 69 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 70 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 71 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 72 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 73 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 74 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 75 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 76 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 77 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 78 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 79 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 80 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 81 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 82 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 83 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 84 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 85 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 86 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 87 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 88 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 89 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 90 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 91 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 92 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 93 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 94 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 95 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 96 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 97 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 98 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 99 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 100 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 101 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 102 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 103 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 104 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 105 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 106 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 107 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 108 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 109 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 110 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 111 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 112 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 113 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 114 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 115 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 116 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 117 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 118 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 119 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 120 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 121 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 122 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 123 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 124 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 125 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 126 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 127 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 128 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 129 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 130 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 131 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 132 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 133 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 134 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 135 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 136 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
