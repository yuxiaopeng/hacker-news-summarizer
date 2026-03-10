# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-10.md)

*最后自动更新时间: 2026-03-10 18:14:36*
## 1. 托尼·霍尔逝世

**原文标题**: Tony Hoare has died

**原文链接**: [https://blog.computationalcomplexity.org/2026/03/tony-hoare-1934-2026.html](https://blog.computationalcomplexity.org/2026/03/tony-hoare-1934-2026.html)

传奇计算机科学家、图灵奖得主托尼·霍尔（Tony Hoare）于2026年3月5日逝世，享年92岁。他以发明**快速排序算法（quicksort）**而闻名于世，其贡献还包括**霍尔逻辑（Hoare logic）**、**ALGOL语言**以及在编程语言领域的开创性工作。

本文由吉姆·迈尔斯（Jim Miles）撰写并发布于兰斯·福特诺（Lance Fortnow）的博客，分享了对霍尔生平与性格的个人追思。迈尔斯强调了霍尔进入计算机领域的不寻常路径：他最初学习古典文学和哲学，随后在服兵役期间学习了俄语。这一背景促使他在苏联担任计算机演示员，在那里他将语言技能与对统计学及技术的浓厚兴趣结合在了一起。

文章通过几则轶事展现了霍尔的个性：
*   **快排赌约：** 霍尔证实，在证明自己的算法比上级要求实现的算法更快后，他确实从 Elliott Brothers 的老板那里赢得了一枚六便士的赌注。
*   **谦逊与职业精神：** 尽管地位显赫，霍尔仍被描述为非常谦逊且专业，他通常会先完成分配的任务，然后再提出自己更优的解决方案。
*   **对天才的看法：** 他批评了好莱坞对“天才”的刻画（特别是在电影《心灵捕手》中），认为真正的成就源于多年的艰苦奋斗，而非瞬间、莫名的灵感。
*   **幽默与敏锐：** 即使在90多岁高龄，霍尔依然保持着敏锐的头脑和风趣的幽默感，曾神秘地暗示政府技术比大众的想象“领先多年”。

人们铭记霍尔，不仅是因为他宏伟的学术成就，还因为他待人温和、富有耐心，以及在漫长一生中始终保持的清晰头脑。

---

## 2. Show HN: RunAnwhere – Apple Silicon 上更快的 AI 推理

**原文标题**: Show HN: RunAnwhere – Faster AI Inference on Apple Silicon

**原文链接**: [https://github.com/RunanywhereAI/rcli](https://github.com/RunanywhereAI/rcli)

**RunAnywhere** 推出了 **RCLI**，这是一款专门为搭载 Apple 芯片的 macOS 设计的端侧语音驱动 AI 助手。该工具提供了一套完整的本地化语音转文本 (STT)、大语言模型 (LLM) 和文本转语音 (TTS) 流水线，实现了低于 200 毫秒端到端延迟的私密、无云体验。

**核心功能与能力：**
*   **系统集成：** 用户可以通过语音或文本执行 43 种原生 macOS 操作，例如控制 Spotify、管理系统设置、创建备忘录以及打开应用程序。
*   **本地 RAG（检索增强生成）：** RCLI 允许用户对本地文档（PDF、DOCX、纯文本）进行索引和查询，混合检索延迟约为 4 毫秒，确保了数据隐私。
*   **高性能：** 该系统由专有的 GPU 推理引擎 **MetalRT** 驱动，LLM 吞吐量高达每秒 550 个 token。虽然 MetalRT 针对 M3 及更高版本芯片进行了优化，但对于 M1 和 M2 用户，软件会自动回退到开源的 *llama.cpp* 引擎。
*   **交互式 TUI：** 基于终端的仪表板支持一键通话（push-to-talk）、实时硬件监控，以及在 Qwen、Llama 3.2、Whisper 和 Kokoro 等支持的模型之间进行“热切换”。
*   **优化架构：** 系统采用多线程流水线，配合零拷贝音频传输、KV 缓存和无锁环形缓冲区，以确保流畅的实时语音对话。

**获取与许可：**
RCLI 可通过简单的单行终端命令或 Homebrew 安装。RCLI 框架在 **MIT 许可证** 下开源，但高性能的 MetalRT 推理引擎仍为专有。该软件要求 macOS 13 或更高版本。

---

## 3. Debian 决定不对 AI 生成的贡献做出定论

**原文标题**: Debian decides not to decide on AI-generated contributions

**原文链接**: [https://lwn.net/SubscriberLink/1061544/125f911834966dd0/](https://lwn.net/SubscriberLink/1061544/125f911834966dd0/)

2026年3月，Debian项目就Lucas Nussbaum提出的一项旨在规范AI辅助贡献的通用决议（GR）草案展开了重大辩论。该提案旨在允许部分或全部由大语言模型（LLM）生成的贡献，前提是必须满足严格的标准：明确披露、提供机器可读的标签，并由人类对技术价值和许可证合规性承担全部责任。

讨论揭示了几个关键争论点：

*   **术语：** 包括Russ Allbery在内的批评者认为，“AI”一词过于宽泛且“定义模糊”，不足以作为持久政策的基础，并建议项目必须区分LLM、强化学习和其他具体工具。
*   **新人培养：** Simon Richter担心AI可能会取代初级开发人员通常处理的任务，从而造成“技能断层”，并阻碍培养新成员所需的导师制度。相反，Ted Ts’o认为禁止AI将是一种弄巧成拙的准入限制。
*   **伦理与法律：** 一些开发人员对AI公司不道德地抓取受版权保护的数据以及该技术对环境的影响表示担忧。此外，关于AI生成代码的“首选修改形式”也引发了法律疑问。
*   **质量：** 虽然有人担心产生“AI垃圾内容”，但也有人指出人类编写的代码也可能同样糟糕，关注点应保持在技术结果上。

最终，Nussbaum决定不再推进该GR，认为社区尚未准备好进行正式表决。该项目选择了“观望”态度，决定根据现有政策对AI生成的贡献进行逐案处理。这一“暂不决定”的结果反映了该问题的复杂性以及技术的快速演变，体现了持续对话优先于过早监管的立场。

---

## 4. 我使用 Claude Code 构建了一门编程语言

**原文标题**: I built a programming language using Claude Code

**原文链接**: [https://ankursethi.com/blog/programming-language-claude-code/](https://ankursethi.com/blog/programming-language-claude-code/)

本文详细介绍了 Cutlet 的诞生过程，这是一种在四周内完全使用 Claude Code 构建的全新动态编程语言。作者是一名前端工程师，他进行了一场“代理式工程”（agentic engineering）实验：让大语言模型（LLM）生成每一行代码，作者无需手动阅读代码，而是依赖严格的规范和自动化防护栏。

**语言特性**
Cutlet 是一种基于 C 语言的编程语言，具有向量化操作（@ 运算符）、原型继承、标记-清除垃圾回收器以及 REPL 环境。它擅长数组操作和函数式规约，尽管目前尚缺乏文件 I/O 和错误处理功能。

**方法论：代理式工程**
作者选择编程语言作为实验对象，是因为这是一个“枯燥”且文档齐全的问题，具有清晰且基于文本的成功标准（即通过测试）。这一过程将人类的角色从“编写代码”转变为“系统架构师”，侧重于四项核心技能：

1. **问题选择：** 识别那些在训练数据中已有既定模式，并能通过自动化手段验证的任务。
2. **意图传达：** 从“有机”编程转向瀑布式模型，在生成任何代码之前，先编写并完善详细的实施计划和形式化规范。
3. **环境设计：** 为代理提供“反馈闭环”（如全面的测试套件和 Docker 环境），使其能够识别并修复自身的回归错误。
4. **循环优化：** 监控代理的进度以确保效率。

**结论**
作者总结道，虽然 LLM 可以将数月的工作压缩到数周，但它们并不能取代工程专业知识。相反，它们将需求转向了更高层次的规划、纪律和匠心。AI 编程代理的成功取决于人类定义清晰边界并为代理提供必要工具以验证其自身工作的能力。

---

## 5. 英特尔展示可处理加密数据的芯片

**原文标题**: Intel Demos Chip to Compute with Encrypted Data

**原文链接**: [https://spectrum.ieee.org/fhe-intel](https://spectrum.ieee.org/fhe-intel)

英特尔展示了一款专为处理全同态加密（FHE）设计的原型芯片。这是一种特殊的加密方法，允许数据在保持完全加密的状态下进行处理和分析。

传统上，数据在进行计算前必须先解密，这会带来显著的安全风险和隐私漏洞。虽然 FHE 允许直接对密文进行计算，从而解决了这一问题，但由于其计算强度极高，在历史上一直难以实际应用，运行速度通常远慢于标准处理。

英特尔的新硬件实现了性能上的重大突破，据称与传统的纯软件实现相比，其 FHE 运算速度提升了 5000 倍。通过大幅降低计算开销，该芯片使 FHE 向商业化应用迈进了一大步。这一进展对于医疗、金融和政府等行业具有重要意义，因为在这些领域，如何在不泄露敏感底层数据的前提下利用云计算服务是一项核心需求。

---

## 6. 我将整个人生都存入了一个数据库

**原文标题**: I put my whole life into a single database

**原文链接**: [https://howisfelix.today/](https://howisfelix.today/)

在《我将整个人生存入了一个数据库》一文中，Felix Krause 详细介绍了他长达十年的项目：追踪分布在 100 多个类别中的超过 38 万个数据点。通过使用名为 **FxLifeSheet** 的自托管开源系统，Krause 汇总了来自自动化来源（如 RescueTime、Swarm、Apple Health）和手动输入的数据，以分析其健身、营养、情绪和生产力。

该项目的主要目标是探究环境因素和习惯如何影响他的身心健康。从其数据可视化中得出的关键洞察包括：

*   **健康与健身：** Krause 发现饮酒后他的静息心率会增加约 50%，并在“增肌”阶段有所上升。他还发现，由于城市交通基础设施的不同，他在纽约市的步行量是维也纳或旧金山的两倍。
*   **情绪与生产力：** “快乐且兴奋”的日子与冥想、挑战舒适区以及减少视频通话时间具有强相关性。 
*   **COVID-19 的影响：** 封锁期间的数据显示，社交视频通话增加了 200%，对饮食计划的执行力也更强，但其体力活动和酒精消耗量显著下降。
*   **位置追踪：** 通过 Foursquare Swarm 记录每一个“兴趣点”，Krause 可以将他的旅行历史可视化，甚至利用这些数据通过其个人网站向朋友告知他的当前位置和“状态”。

Krause 强调了数据所有权和隐私的重要性，因此他自行托管数据库，并为其代码采用了 MIT 许可证。最终，该项目成为了一部“量化自传”，使他能够解答关于生活方式选择和环境如何影响其长期幸福与健康的复杂问题。

---

## 7. Meta收购Moltbook

**原文标题**: Meta acquires Moltbook

**原文链接**: [https://www.axios.com/2026/03/10/meta-facebook-moltbook-agent-social-network](https://www.axios.com/2026/03/10/meta-facebook-moltbook-agent-social-network)

无法访问文章链接。

---

## 8. Show HN: How I Topped the HuggingFace Open LLM Leaderboard on Two Gaming GPUs

**原文标题**: Show HN: How I Topped the HuggingFace Open LLM Leaderboard on Two Gaming GPUs

**原文链接**: [https://dnhkng.github.io/posts/rys/](https://dnhkng.github.io/posts/rys/)

生成摘要时出错

---

## 9. Online age-verification tools for child safety are surveilling adults

**原文标题**: Online age-verification tools for child safety are surveilling adults

**原文链接**: [https://www.cnbc.com/2026/03/08/social-media-child-safety-internet-ai-surveillance.html](https://www.cnbc.com/2026/03/08/social-media-child-safety-internet-ai-surveillance.html)

生成摘要时出错

---

## 10. I used pulsar detection techniques to turn a phone into a watch timegrapher

**原文标题**: I used pulsar detection techniques to turn a phone into a watch timegrapher

**原文链接**: [https://www.chronolog.watch/timegrapher](https://www.chronolog.watch/timegrapher)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 2 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 3 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 4 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 5 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 6 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 7 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 8 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 9 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 10 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 11 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 12 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 13 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 14 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 15 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 16 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 17 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 18 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 19 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 20 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 21 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 22 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 23 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 24 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 25 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 26 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 27 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 28 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 29 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 30 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 31 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 32 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 33 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 34 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 35 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 36 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 37 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 38 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 39 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 40 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 41 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 42 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 43 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 44 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 45 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 46 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 47 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 48 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 49 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 50 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 51 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 52 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 53 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 54 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 55 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 56 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 57 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 58 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 59 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 60 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 61 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 62 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 63 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 64 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 65 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 66 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 67 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 68 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 69 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 70 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 71 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 72 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 73 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 74 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 75 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 76 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 77 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 78 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 79 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 80 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 81 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 82 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 83 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 84 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 85 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 86 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 87 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 88 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 89 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 90 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 91 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 92 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 93 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 94 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 95 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 96 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 97 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 98 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 99 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 100 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 101 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 102 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 103 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 104 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 105 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 106 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 107 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 108 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 109 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 110 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 111 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 112 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 113 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 114 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 115 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 116 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 117 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 118 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 119 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 120 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 121 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 122 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 123 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 124 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 125 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 126 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 127 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 128 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 129 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 130 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 131 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 132 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 133 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 134 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 135 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 136 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 137 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 138 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 139 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 140 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 141 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 142 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 143 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 144 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 145 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 146 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 147 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 148 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 149 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 150 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 151 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 152 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 153 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 154 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 155 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 156 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 157 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 158 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 159 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 160 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 161 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 162 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 163 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 164 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 165 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 166 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 167 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 168 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 169 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 170 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 171 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 172 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 173 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 174 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 175 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 176 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 177 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 178 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 179 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 180 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 181 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 182 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 183 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 184 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 185 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 186 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 187 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 188 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 189 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 190 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 191 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 192 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 193 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 194 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 195 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 196 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 197 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 198 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 199 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 200 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 201 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 202 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 203 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 204 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 205 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 206 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 207 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 208 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 209 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 210 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 211 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 212 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 213 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 214 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 215 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 216 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 217 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 218 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 219 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 220 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 221 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 222 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 223 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 224 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 225 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 226 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 227 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 228 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 229 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 230 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 231 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 232 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 233 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 234 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 235 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 236 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 237 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 238 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 239 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 240 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 241 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 242 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 243 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 244 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 245 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 246 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 247 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 248 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 249 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 250 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 251 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 252 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 253 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 254 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 255 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 256 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 257 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 258 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 259 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 260 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 261 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 262 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 263 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 264 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 265 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 266 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 267 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 268 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 269 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 270 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 271 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 272 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 273 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 274 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 275 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 276 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 277 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 278 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 279 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 280 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 281 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 282 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 283 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 284 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 285 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 286 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 287 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 288 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 289 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 290 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 291 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 292 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 293 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 294 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 295 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 296 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 297 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 298 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 299 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 300 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 301 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 302 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 303 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 304 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 305 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 306 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 307 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 308 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 309 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 310 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 311 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 312 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 313 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 314 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 315 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 316 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 317 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 318 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 319 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 320 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 321 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 322 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 323 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 324 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 325 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 326 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 327 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 328 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 329 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 330 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 331 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 332 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 333 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 334 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 335 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 336 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 337 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 338 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 339 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 340 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 341 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 342 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 343 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 344 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 345 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 346 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 347 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 348 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 349 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 350 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 351 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 352 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 353 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 354 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 355 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
