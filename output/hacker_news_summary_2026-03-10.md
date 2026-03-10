# Hacker News 热门文章摘要 (2026-03-10)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Rebasing in Magit

**原文标题**: Rebasing in Magit

**原文链接**: [https://entropicthoughts.com/rebasing-in-magit](https://entropicthoughts.com/rebasing-in-magit)

生成摘要时出错

---

## 12. The Gervais Principle, or the Office According to "The Office" (2009)

**原文标题**: The Gervais Principle, or the Office According to "The Office" (2009)

**原文链接**: [https://www.ribbonfarm.com/2009/10/07/the-gervais-principle-or-the-office-according-to-the-office/](https://www.ribbonfarm.com/2009/10/07/the-gervais-principle-or-the-office-according-to-the-office/)

生成摘要时出错

---

## 13. PgAdmin 4 9.13 with AI Assistant Panel

**原文标题**: PgAdmin 4 9.13 with AI Assistant Panel

**原文链接**: [https://www.pgadmin.org/docs/pgadmin4/9.13/query_tool.html#ai-assistant-panel](https://www.pgadmin.org/docs/pgadmin4/9.13/query_tool.html#ai-assistant-panel)

生成摘要时出错

---

## 14. Sending Jabber/XMPP Messages via HTTP

**原文标题**: Sending Jabber/XMPP Messages via HTTP

**原文链接**: [https://gultsch.de/posts/xmpp-via-http/](https://gultsch.de/posts/xmpp-via-http/)

生成摘要时出错

---

## 15. Yann LeCun's AI startup raises $1B in Europe's largest ever seed round

**原文标题**: Yann LeCun's AI startup raises $1B in Europe's largest ever seed round

**原文链接**: [https://www.ft.com/content/e5245ec3-1a58-4eff-ab58-480b6259aaf1](https://www.ft.com/content/e5245ec3-1a58-4eff-ab58-480b6259aaf1)

生成摘要时出错

---

## 16. We are building data breach machines and nobody cares

**原文标题**: We are building data breach machines and nobody cares

**原文链接**: [https://idealloc.me/posts/we-are-building-data-breach-machines-and-nobody-cares/](https://idealloc.me/posts/we-are-building-data-breach-machines-and-nobody-cares/)

生成摘要时出错

---

## 17. How many options fit into a boolean?

**原文标题**: How many options fit into a boolean?

**原文链接**: [https://herecomesthemoon.net/2025/11/how-many-options-fit-into-a-boolean/](https://herecomesthemoon.net/2025/11/how-many-options-fit-into-a-boolean/)

生成摘要时出错

---

## 18. Amazon is holding a mandatory meeting about AI breaking its systems

**原文标题**: Amazon is holding a mandatory meeting about AI breaking its systems

**原文链接**: [https://twitter.com/lukolejnik/status/2031257644724342957](https://twitter.com/lukolejnik/status/2031257644724342957)

生成摘要时出错

---

## 19. Show HN: DD Photos – open-source photo album site generator (Go and SvelteKit)

**原文标题**: Show HN: DD Photos – open-source photo album site generator (Go and SvelteKit)

**原文链接**: [https://github.com/dougdonohoe/ddphotos](https://github.com/dougdonohoe/ddphotos)

生成摘要时出错

---

## 20. MariaDB innovation: vector index performance

**原文标题**: MariaDB innovation: vector index performance

**原文链接**: [http://smalldatum.blogspot.com/2026/02/mariadb-innovation-vector-index.html](http://smalldatum.blogspot.com/2026/02/mariadb-innovation-vector-index.html)

生成摘要时出错

---

## 21. A New Version of Our Oracle Solaris Environment for Developers

**原文标题**: A New Version of Our Oracle Solaris Environment for Developers

**原文链接**: [https://blogs.oracle.com/solaris/announcing-a-new-version-of-our-oracle-solaris-environment-for-developers](https://blogs.oracle.com/solaris/announcing-a-new-version-of-our-oracle-solaris-environment-for-developers)

生成摘要时出错

---

## 22. Caxlsx: Ruby gem for xlsx generation with charts, images, schema validation

**原文标题**: Caxlsx: Ruby gem for xlsx generation with charts, images, schema validation

**原文链接**: [https://github.com/caxlsx/caxlsx](https://github.com/caxlsx/caxlsx)

生成摘要时出错

---

## 23. Practical Guide to Bare Metal C++

**原文标题**: Practical Guide to Bare Metal C++

**原文链接**: [https://arobenko.github.io/bare_metal_cpp/#_abstract_classes](https://arobenko.github.io/bare_metal_cpp/#_abstract_classes)

生成摘要时出错

---

## 24. Two Years of Emacs Solo

**原文标题**: Two Years of Emacs Solo

**原文链接**: [https://www.rahuljuliato.com/posts/emacs-solo-two-years](https://www.rahuljuliato.com/posts/emacs-solo-two-years)

生成摘要时出错

---

## 25. LoGeR – 3D reconstruction from extremely long videos (DeepMind, UC Berkeley)

**原文标题**: LoGeR – 3D reconstruction from extremely long videos (DeepMind, UC Berkeley)

**原文链接**: [https://loger-project.github.io](https://loger-project.github.io)

生成摘要时出错

---

## 26. $3 ChromeOS Flex stick will revive old and outdated computers

**原文标题**: $3 ChromeOS Flex stick will revive old and outdated computers

**原文链接**: [https://9to5google.com/2026/03/10/this-3-chromeos-stick-will-revive-old-and-outdated-computers/](https://9to5google.com/2026/03/10/this-3-chromeos-stick-will-revive-old-and-outdated-computers/)

生成摘要时出错

---

## 27. Lotus 1-2-3 on the PC with DOS

**原文标题**: Lotus 1-2-3 on the PC with DOS

**原文链接**: [https://stonetools.ghost.io/lotus123-dos/](https://stonetools.ghost.io/lotus123-dos/)

生成摘要时出错

---

## 28. TCXO Failure Analysis

**原文标题**: TCXO Failure Analysis

**原文链接**: [https://serd.es/2026/03/06/TCXO-failure-analysis.html](https://serd.es/2026/03/06/TCXO-failure-analysis.html)

生成摘要时出错

---

## 29. Microsoft Copilot Update Hijacks Default Browser Links

**原文标题**: Microsoft Copilot Update Hijacks Default Browser Links

**原文链接**: [https://reclaimthenet.org/microsoft-copilot-update-hijacks-default-browser-links](https://reclaimthenet.org/microsoft-copilot-update-hijacks-default-browser-links)

生成摘要时出错

---

## 30. BC got rid of Daylight Savings

**原文标题**: BC got rid of Daylight Savings

**原文链接**: [https://news.gov.bc.ca/releases/2026AG0013-000209](https://news.gov.bc.ca/releases/2026AG0013-000209)

生成摘要时出错

---

## 31. TCXO Failure Analysis

**原文标题**: TCXO Failure Analysis

**原文链接**: [https://serd.es/2026/03/06/TCXO-failure-analysis.html](https://serd.es/2026/03/06/TCXO-failure-analysis.html)

生成摘要时出错

---

## 32. Traffic from Russia to Cloudflare is 60% down from last year

**原文标题**: Traffic from Russia to Cloudflare is 60% down from last year

**原文链接**: [https://radar.cloudflare.com/traffic/ru?dateRange=52w](https://radar.cloudflare.com/traffic/ru?dateRange=52w)

生成摘要时出错

---

## 33. No, it doesn't cost Anthropic $5k per Claude Code user

**原文标题**: No, it doesn't cost Anthropic $5k per Claude Code user

**原文链接**: [https://martinalderson.com/posts/no-it-doesnt-cost-anthropic-5k-per-claude-code-user/](https://martinalderson.com/posts/no-it-doesnt-cost-anthropic-5k-per-claude-code-user/)

生成摘要时出错

---

## 34. Optimizing Top K in Postgres

**原文标题**: Optimizing Top K in Postgres

**原文链接**: [https://www.paradedb.com/blog/optimizing-top-k](https://www.paradedb.com/blog/optimizing-top-k)

生成摘要时出错

---

## 35. YouTube ads are about to get even longer and they'll be unskippable

**原文标题**: YouTube ads are about to get even longer and they'll be unskippable

**原文链接**: [https://www.dexerto.com/youtube/youtube-ads-are-about-to-get-even-longer-and-theyll-be-unskippable-3332420/](https://www.dexerto.com/youtube/youtube-ads-are-about-to-get-even-longer-and-theyll-be-unskippable-3332420/)

生成摘要时出错

---

## 36. Show HN: A playable version of the Claude Code Terraform destroy incident

**原文标题**: Show HN: A playable version of the Claude Code Terraform destroy incident

**原文链接**: [https://www.youbrokeprod.com](https://www.youbrokeprod.com)

生成摘要时出错

---

## 37. Redox OS has adopted a Certificate of Origin policy and a strict no-LLM policy

**原文标题**: Redox OS has adopted a Certificate of Origin policy and a strict no-LLM policy

**原文链接**: [https://gitlab.redox-os.org/redox-os/redox/-/blob/master/CONTRIBUTING.md](https://gitlab.redox-os.org/redox-os/redox/-/blob/master/CONTRIBUTING.md)

生成摘要时出错

---

## 38. Foreign-funded lobby groups outside EU are pushing ChatControl with propaganda

**原文标题**: Foreign-funded lobby groups outside EU are pushing ChatControl with propaganda

**原文链接**: [https://digitalcourage.social/@echo_pbreyer/116205371224315359](https://digitalcourage.social/@echo_pbreyer/116205371224315359)

生成摘要时出错

---

## 39. Hugging Face Storage Buckets: Mutable, non-versioned object storage at $12/TB

**原文标题**: Hugging Face Storage Buckets: Mutable, non-versioned object storage at $12/TB

**原文链接**: [https://huggingface.co/blog/storage-buckets](https://huggingface.co/blog/storage-buckets)

生成摘要时出错

---

## 40. Show HN: Remotely use my guitar tuner

**原文标题**: Show HN: Remotely use my guitar tuner

**原文链接**: [https://realtuner.online/](https://realtuner.online/)

生成摘要时出错

---

## 41. The hidden compile-time cost of C++26 reflection

**原文标题**: The hidden compile-time cost of C++26 reflection

**原文链接**: [https://vittorioromeo.com/index/blog/refl_compiletime.html](https://vittorioromeo.com/index/blog/refl_compiletime.html)

生成摘要时出错

---

## 42. AI Agent hacked McKinsey's chatbot and gained full read-write access in 2 hours

**原文标题**: AI Agent hacked McKinsey's chatbot and gained full read-write access in 2 hours

**原文链接**: [https://www.theregister.com/2026/03/09/mckinsey_ai_chatbot_hacked/](https://www.theregister.com/2026/03/09/mckinsey_ai_chatbot_hacked/)

生成摘要时出错

---

## 43. Darkrealms BBS

**原文标题**: Darkrealms BBS

**原文链接**: [http://www.darkrealms.ca/](http://www.darkrealms.ca/)

生成摘要时出错

---

## 44. Meta Acquired Moltbook

**原文标题**: Meta Acquired Moltbook

**原文链接**: [https://techcrunch.com/2026/03/10/meta-acquired-moltbook-the-ai-agent-social-network-that-went-viral-because-of-fake-posts/](https://techcrunch.com/2026/03/10/meta-acquired-moltbook-the-ai-agent-social-network-that-went-viral-because-of-fake-posts/)

生成摘要时出错

---

## 45. RFC 454545 – Human Em Dash Standard

**原文标题**: RFC 454545 – Human Em Dash Standard

**原文链接**: [https://gist.github.com/bignimbus/a75cc9d703abf0b21a57c0d21a79e2be](https://gist.github.com/bignimbus/a75cc9d703abf0b21a57c0d21a79e2be)

生成摘要时出错

---

## 46. macOS Tahoe windows have different corner radiuses

**原文标题**: macOS Tahoe windows have different corner radiuses

**原文链接**: [https://lapcatsoftware.com/articles/2026/3/1.html](https://lapcatsoftware.com/articles/2026/3/1.html)

生成摘要时出错

---

## 47. Baochip-1x: A Mostly-Open, 22nm SoC for High Assurance Applications

**原文标题**: Baochip-1x: A Mostly-Open, 22nm SoC for High Assurance Applications

**原文链接**: [https://www.bunniestudios.com/blog/2026/baochip-1x-a-mostly-open-22nm-soc-for-high-assurance-applications/](https://www.bunniestudios.com/blog/2026/baochip-1x-a-mostly-open-22nm-soc-for-high-assurance-applications/)

生成摘要时出错

---

## 48. Germany's Solar Boom Eases Power Costs as Gas Price Jumps

**原文标题**: Germany's Solar Boom Eases Power Costs as Gas Price Jumps

**原文链接**: [https://www.bloomberg.com/news/articles/2026-03-06/germany-s-solar-boom-eases-power-costs-as-gas-price-jumps](https://www.bloomberg.com/news/articles/2026-03-06/germany-s-solar-boom-eases-power-costs-as-gas-price-jumps)

生成摘要时出错

---

## 49. What's My JND?

**原文标题**: What's My JND?

**原文链接**: [https://www.keithcirkel.co.uk/whats-my-jnd/](https://www.keithcirkel.co.uk/whats-my-jnd/)

生成摘要时出错

---

## 50. The U.S.‑Israel war with Iran could shatter the United Nations‑led global order

**原文标题**: The U.S.‑Israel war with Iran could shatter the United Nations‑led global order

**原文链接**: [https://theconversation.com/the-u-s-israel-war-with-iran-could-shatter-the-united-nations-led-global-order-277441](https://theconversation.com/the-u-s-israel-war-with-iran-could-shatter-the-united-nations-led-global-order-277441)

生成摘要时出错

---

## 51. Show HN: DenchClaw – Local CRM on Top of OpenClaw

**原文标题**: Show HN: DenchClaw – Local CRM on Top of OpenClaw

**原文链接**: [https://github.com/DenchHQ/DenchClaw](https://github.com/DenchHQ/DenchClaw)

生成摘要时出错

---

## 52. DARPA’s new X-76

**原文标题**: DARPA’s new X-76

**原文链接**: [https://www.darpa.mil/news/2026/darpa-new-x-76-speed-of-jet-freedom-of-helicopter](https://www.darpa.mil/news/2026/darpa-new-x-76-speed-of-jet-freedom-of-helicopter)

生成摘要时出错

---

## 53. An opinionated take on how to do important research that matters

**原文标题**: An opinionated take on how to do important research that matters

**原文链接**: [https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html](https://nicholas.carlini.com/writing/2026/how-to-win-a-best-paper-award.html)

生成摘要时出错

---

## 54. Graphing how the 10k* most common English words define each other

**原文标题**: Graphing how the 10k* most common English words define each other

**原文链接**: [https://wyattsell.com/experiments/word-graph/](https://wyattsell.com/experiments/word-graph/)

生成摘要时出错

---

## 55. Building a Procedural Hex Map with Wave Function Collapse

**原文标题**: Building a Procedural Hex Map with Wave Function Collapse

**原文链接**: [https://felixturner.github.io/hex-map-wfc/article/](https://felixturner.github.io/hex-map-wfc/article/)

生成摘要时出错

---

## 56. Is legal the same as legitimate: AI reimplementation and the erosion of copyleft

**原文标题**: Is legal the same as legitimate: AI reimplementation and the erosion of copyleft

**原文链接**: [https://writings.hongminhee.org/2026/03/legal-vs-legitimate/](https://writings.hongminhee.org/2026/03/legal-vs-legitimate/)

生成摘要时出错

---

## 57. The “JVG algorithm” only wins on tiny numbers

**原文标题**: The “JVG algorithm” only wins on tiny numbers

**原文链接**: [https://scottaaronson.blog/?p=9615](https://scottaaronson.blog/?p=9615)

生成摘要时出错

---

## 58. Getting Started in Common Lisp

**原文标题**: Getting Started in Common Lisp

**原文链接**: [https://lisp-stat.dev/blog/2026/03/09/getting-started/](https://lisp-stat.dev/blog/2026/03/09/getting-started/)

生成摘要时出错

---

## 59. Device that can extract 1k liters of clean water a day from desert

**原文标题**: Device that can extract 1k liters of clean water a day from desert

**原文链接**: [https://www.tomshardware.com/tech-industry/device-that-can-extract-1-000-liters-of-clean-water-a-day-from-desert-air-revealed-by-2025-nobel-prize-winner-claimed-to-work-in-desert-air-with-20-percent-humidity-or-lower-delivering-off-grid-personalized-water](https://www.tomshardware.com/tech-industry/device-that-can-extract-1-000-liters-of-clean-water-a-day-from-desert-air-revealed-by-2025-nobel-prize-winner-claimed-to-work-in-desert-air-with-20-percent-humidity-or-lower-delivering-off-grid-personalized-water)

生成摘要时出错

---

## 60. JSLinux Now Supports x86_64

**原文标题**: JSLinux Now Supports x86_64

**原文链接**: [https://bellard.org/jslinux/](https://bellard.org/jslinux/)

生成摘要时出错

---

## 61. Notes on Baking at the South Pole

**原文标题**: Notes on Baking at the South Pole

**原文链接**: [https://www.newyorker.com/culture/the-weekend-essay/the-most-beautiful-freezer-in-the-world](https://www.newyorker.com/culture/the-weekend-essay/the-most-beautiful-freezer-in-the-world)

生成摘要时出错

---

## 62. OpenAI is walking away from expanding its Stargate data center with Oracle

**原文标题**: OpenAI is walking away from expanding its Stargate data center with Oracle

**原文链接**: [https://www.cnbc.com/2026/03/09/oracle-is-building-yesterdays-data-centers-with-tomorrows-debt.html](https://www.cnbc.com/2026/03/09/oracle-is-building-yesterdays-data-centers-with-tomorrows-debt.html)

生成摘要时出错

---

## 63. Mercury – Transforming Drone

**原文标题**: Mercury – Transforming Drone

**原文链接**: [https://github.com/L42ARO/Mercury-Transforming-Drone](https://github.com/L42ARO/Mercury-Transforming-Drone)

生成摘要时出错

---

## 64. FreeBSD 14.4-Release Announcement

**原文标题**: FreeBSD 14.4-Release Announcement

**原文链接**: [https://www.freebsd.org/releases/14.4R/announce/](https://www.freebsd.org/releases/14.4R/announce/)

生成摘要时出错

---

## 65. Meta to Acquire Moltbook

**原文标题**: Meta to Acquire Moltbook

**原文链接**: [https://www.bloomberg.com/news/articles/2026-03-10/meta-to-acquire-moltbook-viral-social-network-for-ai-agents](https://www.bloomberg.com/news/articles/2026-03-10/meta-to-acquire-moltbook-viral-social-network-for-ai-agents)

生成摘要时出错

---

## 66. Flash media longevity testing – 6 years later

**原文标题**: Flash media longevity testing – 6 years later

**原文链接**: [https://old.reddit.com/r/DataHoarder/comments/1q6xnun/flash_media_longevity_testing_6_years_later/](https://old.reddit.com/r/DataHoarder/comments/1q6xnun/flash_media_longevity_testing_6_years_later/)

生成摘要时出错

---

## 67. FFmpeg at Meta: Media Processing at Scale

**原文标题**: FFmpeg at Meta: Media Processing at Scale

**原文链接**: [https://engineering.fb.com/2026/03/02/video-engineering/ffmpeg-at-meta-media-processing-at-scale/](https://engineering.fb.com/2026/03/02/video-engineering/ffmpeg-at-meta-media-processing-at-scale/)

生成摘要时出错

---

## 68. Microsoft 365 confirms new premium tier, stuffed with AI and few discounts

**原文标题**: Microsoft 365 confirms new premium tier, stuffed with AI and few discounts

**原文链接**: [https://www.theregister.com/2026/03/09/microsoft_adds_a_premium_tier/](https://www.theregister.com/2026/03/09/microsoft_adds_a_premium_tier/)

生成摘要时出错

---

## 69. Reverse-engineering the UniFi inform protocol

**原文标题**: Reverse-engineering the UniFi inform protocol

**原文链接**: [https://tamarack.cloud/blog/reverse-engineering-unifi-inform-protocol](https://tamarack.cloud/blog/reverse-engineering-unifi-inform-protocol)

生成摘要时出错

---

## 70. On Thinking Machines

**原文标题**: On Thinking Machines

**原文链接**: [https://www.sicpers.info/2026/03/on-thinking-machines/](https://www.sicpers.info/2026/03/on-thinking-machines/)

生成摘要时出错

---

## 71. Drosophila Fly Brain Emulation

**原文标题**: Drosophila Fly Brain Emulation

**原文链接**: [https://github.com/eonsystemspbc/fly-brain](https://github.com/eonsystemspbc/fly-brain)

生成摘要时出错

---

## 72. Show HN: The Mog Programming Language

**原文标题**: Show HN: The Mog Programming Language

**原文链接**: [https://moglang.org](https://moglang.org)

生成摘要时出错

---

## 73. Algebraic topology: knots links and braids

**原文标题**: Algebraic topology: knots links and braids

**原文链接**: [https://aeb.win.tue.nl/at/algtop-5.html](https://aeb.win.tue.nl/at/algtop-5.html)

生成摘要时出错

---

## 74. Bluesky CEO Jay Graber is stepping down

**原文标题**: Bluesky CEO Jay Graber is stepping down

**原文链接**: [https://bsky.social/about/blog/03-09-2026-a-new-chapter-for-bluesky](https://bsky.social/about/blog/03-09-2026-a-new-chapter-for-bluesky)

生成摘要时出错

---

## 75. The window chrome of our discontent

**原文标题**: The window chrome of our discontent

**原文链接**: [https://pxlnv.com/blog/window-chrome-of-our-discontent/](https://pxlnv.com/blog/window-chrome-of-our-discontent/)

生成摘要时出错

---

## 76. Unlocking Python's Cores:Energy Implications of Removing the GIL

**原文标题**: Unlocking Python's Cores:Energy Implications of Removing the GIL

**原文链接**: [https://arxiv.org/abs/2603.04782](https://arxiv.org/abs/2603.04782)

生成摘要时出错

---

## 77. Learnings from paying artists royalties for AI-generated art

**原文标题**: Learnings from paying artists royalties for AI-generated art

**原文链接**: [https://www.kapwing.com/blog/learnings-from-paying-artists-royalties-for-ai-generated-art/](https://www.kapwing.com/blog/learnings-from-paying-artists-royalties-for-ai-generated-art/)

生成摘要时出错

---

## 78. Fixfest is a global gathering of repairers, tinkerers, and activists

**原文标题**: Fixfest is a global gathering of repairers, tinkerers, and activists

**原文链接**: [https://fixfest.therestartproject.org/](https://fixfest.therestartproject.org/)

生成摘要时出错

---

## 79. Restoring a Sun SPARCstation IPX part 1: PSU and NVRAM (2020)

**原文标题**: Restoring a Sun SPARCstation IPX part 1: PSU and NVRAM (2020)

**原文链接**: [https://www.rs-online.com/designspark/restoring-a-sun-sparcstation-ipx-part-1-psu-and-nvram](https://www.rs-online.com/designspark/restoring-a-sun-sparcstation-ipx-part-1-psu-and-nvram)

生成摘要时出错

---

## 80. F3 – Fight Flash Fraud, tool that tests flash cards capacity and performance

**原文标题**: F3 – Fight Flash Fraud, tool that tests flash cards capacity and performance

**原文链接**: [https://fight-flash-fraud.readthedocs.io/en/latest/introduction.html](https://fight-flash-fraud.readthedocs.io/en/latest/introduction.html)

生成摘要时出错

---

## 81. How fast does a protein fold? Real-time technique captures the moment

**原文标题**: How fast does a protein fold? Real-time technique captures the moment

**原文链接**: [https://www.nature.com/articles/d41586-026-00755-x](https://www.nature.com/articles/d41586-026-00755-x)

生成摘要时出错

---

## 82. Rethinking Syntax: Binding by Adjacency

**原文标题**: Rethinking Syntax: Binding by Adjacency

**原文链接**: [https://github.com/manifold-systems/manifold/blob/master/docs/articles/binding_exprs.md](https://github.com/manifold-systems/manifold/blob/master/docs/articles/binding_exprs.md)

生成摘要时出错

---

## 83. Family of child injured in Canada school shooting sues OpenAI

**原文标题**: Family of child injured in Canada school shooting sues OpenAI

**原文链接**: [https://www.bbc.com/news/articles/c309y25prnlo](https://www.bbc.com/news/articles/c309y25prnlo)

生成摘要时出错

---

## 84. FontCrafter: Turn your handwriting into a real font

**原文标题**: FontCrafter: Turn your handwriting into a real font

**原文链接**: [https://arcade.pirillo.com/fontcrafter.html](https://arcade.pirillo.com/fontcrafter.html)

生成摘要时出错

---

## 85. Durdraw – ANSI art editor for Unix-like systems

**原文标题**: Durdraw – ANSI art editor for Unix-like systems

**原文链接**: [https://durdraw.org/](https://durdraw.org/)

生成摘要时出错

---

## 86. M5 Max: Chiplets, Thermals, and Performance per Watt

**原文标题**: M5 Max: Chiplets, Thermals, and Performance per Watt

**原文链接**: [https://creativestrategies.com/research/m5-max-chiplets-thermals-and-performance-per-watt/](https://creativestrategies.com/research/m5-max-chiplets-thermals-and-performance-per-watt/)

生成摘要时出错

---

## 87. FreeBSD Capsicum vs. Linux Seccomp Process Sandboxing

**原文标题**: FreeBSD Capsicum vs. Linux Seccomp Process Sandboxing

**原文链接**: [https://vivianvoss.net/blog/capsicum-vs-seccomp](https://vivianvoss.net/blog/capsicum-vs-seccomp)

生成摘要时出错

---

## 88. The first airplane fatality

**原文标题**: The first airplane fatality

**原文链接**: [https://www.amusingplanet.com/2026/03/thomas-selfridge-first-airplane-fatality.html](https://www.amusingplanet.com/2026/03/thomas-selfridge-first-airplane-fatality.html)

生成摘要时出错

---

## 89. Gabibi is a tool for intentionally degrading images (in Japanese)

**原文标题**: Gabibi is a tool for intentionally degrading images (in Japanese)

**原文链接**: [https://amix-design.com/tl/tool-gabibi/](https://amix-design.com/tl/tool-gabibi/)

生成摘要时出错

---

## 90. Removing recursion via explicit callstack simulation

**原文标题**: Removing recursion via explicit callstack simulation

**原文链接**: [https://jnkr.tech/blog/removing-recursion](https://jnkr.tech/blog/removing-recursion)

生成摘要时出错

---

## 91. I'd had several careers but no degree – then I became a palaeontologist at 62

**原文标题**: I'd had several careers but no degree – then I became a palaeontologist at 62

**原文链接**: [https://www.theguardian.com/lifeandstyle/2026/mar/09/a-new-start-after-60-career-palaeontologist](https://www.theguardian.com/lifeandstyle/2026/mar/09/a-new-start-after-60-career-palaeontologist)

生成摘要时出错

---

## 92. I don't know Apple's endgame for the Fn/Globe key–or if Apple does

**原文标题**: I don't know Apple's endgame for the Fn/Globe key–or if Apple does

**原文链接**: [https://aresluna.org/fn/](https://aresluna.org/fn/)

生成摘要时出错

---

## 93. Segagaga Has Been Translated into English

**原文标题**: Segagaga Has Been Translated into English

**原文链接**: [https://www.thedreamcastjunkyard.co.uk/2026/02/segagaga-has-finally-been-translated.html](https://www.thedreamcastjunkyard.co.uk/2026/02/segagaga-has-finally-been-translated.html)

生成摘要时出错

---

## 94. Show HN: I Was Here – Draw on street view, others can find your drawings

**原文标题**: Show HN: I Was Here – Draw on street view, others can find your drawings

**原文链接**: [https://washere.live](https://washere.live)

生成摘要时出错

---

## 95. Velxio, Arduino Emulator

**原文标题**: Velxio, Arduino Emulator

**原文链接**: [https://velxio.dev/](https://velxio.dev/)

生成摘要时出错

---

## 96. Worming out molecular secrets behind collective behaviour

**原文标题**: Worming out molecular secrets behind collective behaviour

**原文链接**: [https://iisc.ac.in/events/worming-out-molecular-secrets-behind-collective-behaviour/](https://iisc.ac.in/events/worming-out-molecular-secrets-behind-collective-behaviour/)

生成摘要时出错

---

## 97. Jolla on track to ship new phone with Sailfish OS, user-replaceable battery

**原文标题**: Jolla on track to ship new phone with Sailfish OS, user-replaceable battery

**原文链接**: [https://liliputing.com/the-new-jolla-phone-with-sailfish-os-is-on-track-to-start-shipping-in-the-first-half-of-2026/](https://liliputing.com/the-new-jolla-phone-with-sailfish-os-is-on-track-to-start-shipping-in-the-first-half-of-2026/)

生成摘要时出错

---

## 98. Show HN: VS Code Agent Kanban: Task Management for the AI-Assisted Developer

**原文标题**: Show HN: VS Code Agent Kanban: Task Management for the AI-Assisted Developer

**原文链接**: [https://www.appsoftware.com/blog/introducing-vs-code-agent-kanban-task-management-for-the-ai-assisted-developer](https://www.appsoftware.com/blog/introducing-vs-code-agent-kanban-task-management-for-the-ai-assisted-developer)

生成摘要时出错

---

## 99. SigNoz (YC W21) is hiring for engineering, growth and product roles

**原文标题**: SigNoz (YC W21) is hiring for engineering, growth and product roles

**原文链接**: [https://signoz.io/careers](https://signoz.io/careers)

生成摘要时出错

---

## 100. A college student's perspective on using AI in class

**原文标题**: A college student's perspective on using AI in class

**原文链接**: [https://www.npr.org/2026/03/06/nx-s1-5732793/college-student-perspective-using-ai-in-class](https://www.npr.org/2026/03/06/nx-s1-5732793/college-student-perspective-using-ai-in-class)

生成摘要时出错

---

