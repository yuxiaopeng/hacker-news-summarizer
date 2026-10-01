# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-01.md)

*最后自动更新时间: 2026-10-01 22:05:13*
## 1. Pi 1.0

**原文标题**: Pi 1.0

**原文链接**: [https://earendil.com/posts/pi-1-0/](https://earendil.com/posts/pi-1-0/)

Earendil has officially launched **Pi 1.0**, a hardened, minimal, and extensible AI agent harness designed for stability and professional use. Following months of refinement based on community feedback, the release marks Pi’s transition into a dependable tool for developers and businesses.

**Key Features and Philosophy**
Pi 1.0 maintains a philosophy of "minimalism and supermalleability," only adopting features that have proven their utility against inherent complexity. Key updates in this version include:
*   **Codemode:** Native support for the Model Context Protocol (MCP), image models, and non-LLM models like Jev.
*   **Technical Enhancements:** Extension support for virtual models, deferred tool loading, and cache warming for Anthropic models.
*   **User Interface:** A new TUI theme, default full-screen mode, and mid-conversation system messages that allow for transcript-aware prompt and tool adjustments.

**Introducing Pi Durable**
Alongside the standard release, Earendil introduced **Pi Durable**, an experimental package designed for long-running agentic applications. While Pi 1.0 remains a streamlined terminal-based coding agent, Pi Durable extends the platform’s core principles to support more complex, persistent tasks across various surfaces, offering builders greater dexterity in steering underlying intelligence.

**Mission and Availability**
Aligned with Earendil’s mission to strengthen human agency through open protocols, both tools are **MIT licensed**. Pi 1.0 can be installed via shell script (curl or PowerShell), while Pi Durable is available as an npm package. Comprehensive documentation and source code are available at pi.dev and GitHub.

---

## 2. Clef: Open-source decision models, and new RL fine-tuning platform

**原文标题**: Clef: Open-source decision models, and new RL fine-tuning platform

**原文链接**: [https://blog.cloudflare.com/clef-decision-models/](https://blog.cloudflare.com/clef-decision-models/)

生成摘要时出错

---

## 3. The death of web development education

**原文标题**: The death of web development education

**原文链接**: [https://molily.de/web-dev-education/](https://molily.de/web-dev-education/)

生成摘要时出错

---

## 4. Pi 耐用

**原文标题**: Pi Durable

**原文链接**: [https://earendil.com/posts/pi-durable/](https://earendil.com/posts/pi-durable/)

Earendil Engineering 宣布发布 **Pi Durable**，这是一个旨在构建长效、韧性且具可塑性的 AI 智能体（Agent）的实验性框架。与 Pi 1.0 同步推出的 Pi Durable 并非 Pi 编程智能体的替代品，而是一个用于构建多样化智能体应用的“底座”（harness），它可以在任何支持 JavaScript 运行时的环境（包括 Node、Bun 和 Cloudflare）中运行。

该框架建立在以下几个核心支柱之上：

*   **持久性与崩溃恢复：** 智能体运行的每一步都被视为一个“任务”，其检查点（checkpoint）会保存到存储（SQLite、JSONL 或内存）中。如果进程崩溃或机器重启，底座会自动从最后一个检查点恢复任务，确保“仅一次”（exactly-once）的提交保证。
*   **并行与分叉：** 单个底座可以管理多个并发对话。它支持“分叉”（forking），允许新对话从现有记录中派生出来，而无需复制历史记录。每个对话都可以自定义模型、工具和指令。
*   **可插拔架构：** 系统具有高度可扩展性。开发者可以将系统提示词、工具和钩子（hooks）打包为“扩展”。由于整个代码库约为 15,000 行，其设计足够精简，便于智能体对其自身源代码进行推理。
*   **高级工具与子智能体：** 工具作为持久任务执行。该框架简化了子智能体的创建——即通过工具调用启动次级对话——从而实现复杂且具备持久性和可追溯性的多智能体工作流。

最终，Pi Durable 将作为智能体设计的实验室。从该实验性框架中获得的经验最终将反馈到核心的 Pi 编程智能体中，从而延续 Earendil 对极简主义和可塑性的追求。

---

## 5. Car Is a Smartphone on Wheels. Here's Who's Listening

**原文标题**: Car Is a Smartphone on Wheels. Here's Who's Listening

**原文链接**: [https://automatictransmission.khoury.northeastern.edu/index.html](https://automatictransmission.khoury.northeastern.edu/index.html)

生成摘要时出错

---

## 6. Show HN: Janus – 一个通过 Vulkan 在 AMD/Intel/Nvidia 上运行 GGUF 模型的 Go 二进制程序

**原文标题**: Show HN: Janus – Go binary that runs GGUF models via Vulkan on AMD/Intel/Nvidia

**原文链接**: [https://github.com/Vibra-Ingenn/Janus](https://github.com/Vibra-Ingenn/Janus)

生成摘要时出错

---

## 7. 水下缺氧区域可能并非“死亡地带”，而是早期生命的线索。

**原文标题**: Oxygen-deprived underwater zones may not be "dead zones" but clue to early life

**原文链接**: [https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2026AV002570](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2026AV002570)

本摘要基于发表在《AGU Advances》上的研究《低氧海洋栖息地：早期动物演化的窗口》（尽管提供的链接中年份存在笔误，但对应的是该研究）。

### **摘要**

最近发表在《AGU Advances》上的一项研究挑战了人们对缺氧海域（通常被称为“死亡区”）的传统看法。研究人员指出，这些最低含氧带（OMZs）并非生物荒漠，而是繁荣的生态系统，为研究地球早期生命的演化提供了关键窗口。

**核心发现：**
*   **繁荣的生物多样性：** 通过对加利福尼亚湾最低含氧带的研究，研究人员发现，在氧气水平不足表层海水1%的环境中，生存着包括线虫和动吻动物在内的多种小型底栖动物（meiofauna）。
*   **演化模拟：** 这些区域是元古宙（约25亿至5亿年前）的现代模拟。研究表明，早期动物祖先可能是在类似的低氧环境中演化并实现多样化的，而非如先前认为的那样，复杂生命必须在高含氧量环境下才能生存。
*   **生命的韧性：** 研究强调，许多生物已经演化出了复杂的代谢策略，以便在极端条件下生存甚至繁衍。这表明“大氧化事件”可能并非动物演化的唯一触发因素；相反，动物早已适应了低氧生态位。

**重要意义：**
通过将“死亡区”重新定义为“低氧避难所”，该研究改变了科学叙事。它表明，极端海洋环境对于理解生命的生物极限和地球的演化史至关重要。此外，这也意味着随着当今气候变化导致这些区域不断扩大，我们正看到曾经主宰远古海洋的环境正在回归，而那些生存了数亿年的韧性物种则生活在其中。

---

## 8. 再见，向量数据库

**原文标题**: RIP, vector database

**原文链接**: [https://turbopuffer.com/blog/rip-vector-database](https://turbopuffer.com/blog/rip-vector-database)

生成摘要时出错

---

## 9. StreetComplete on iOS is now in public beta

**原文标题**: StreetComplete on iOS is now in public beta

**原文链接**: [https://github.com/streetcomplete/StreetComplete/issues/5421](https://github.com/streetcomplete/StreetComplete/issues/5421)

生成摘要时出错

---

## 10. Bez: Generating a browser engine from specs and tests

**原文标题**: Bez: Generating a browser engine from specs and tests

**原文链接**: [https://tangled.org/burrito.space/bez](https://tangled.org/burrito.space/bez)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 2 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 3 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 4 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 5 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 6 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 7 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 8 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 9 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 10 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 11 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 12 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 13 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 14 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 15 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 16 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 17 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 18 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 19 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 20 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 21 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 22 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 23 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 24 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 25 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 26 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 27 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 28 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 29 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 30 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 31 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 32 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 33 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 34 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 35 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 36 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 37 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 38 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 39 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 40 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 41 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 42 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 43 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 44 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 45 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 46 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 47 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 48 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 49 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 50 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 51 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 52 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 53 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 54 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 55 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 56 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 57 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 58 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 59 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 60 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 61 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 62 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 63 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 64 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 65 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 66 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 67 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 68 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 69 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 70 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 71 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 72 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 73 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 74 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 75 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 76 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 77 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 78 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 79 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 80 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 81 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 82 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 83 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 84 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 85 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 86 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 87 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 88 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 89 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 90 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 91 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 92 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 93 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 94 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 95 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 96 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 97 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 98 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 99 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 100 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 101 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 102 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 103 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 104 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 105 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 106 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 107 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 108 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 109 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 110 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 111 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 112 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 113 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 114 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 115 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 116 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 117 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 118 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 119 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 120 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 121 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 122 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 123 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 124 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 125 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 126 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 127 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 128 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 129 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 130 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 131 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 132 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 133 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 134 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 135 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 136 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 137 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 138 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 139 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 140 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 141 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 142 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 143 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 144 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 145 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 146 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 147 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 148 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 149 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 150 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 151 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 152 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 153 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 154 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 155 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 156 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 157 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 158 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 159 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 160 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 161 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 162 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 163 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 164 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 165 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 166 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 167 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 168 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 169 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 170 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 171 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 172 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 173 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 174 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 175 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 176 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 177 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 178 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 179 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 180 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 181 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 182 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 183 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 184 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 185 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 186 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 187 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 188 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 189 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 190 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 191 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 192 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 193 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 194 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 195 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 196 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 197 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 198 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 199 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 200 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 201 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 202 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 203 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 204 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 205 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 206 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 207 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 208 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 209 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 210 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 211 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 212 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 213 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 214 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 215 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 216 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 217 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 218 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 219 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 220 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 221 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 222 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 223 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 224 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 225 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 226 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 227 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 228 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 229 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 230 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 231 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 232 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 233 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 234 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 235 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 236 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 237 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 238 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 239 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 240 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 241 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 242 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 243 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 244 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 245 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 246 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 247 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 248 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 249 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 250 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 251 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 252 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 253 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 254 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 255 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 256 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 257 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 258 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 259 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 260 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 261 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 262 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 263 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 264 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 265 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 266 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 267 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 268 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 269 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 270 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 271 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 272 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 273 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 274 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 275 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 276 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 277 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 278 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 279 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 280 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 281 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 282 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 283 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 284 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 285 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 286 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 287 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 288 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 289 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 290 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 291 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 292 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 293 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 294 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 295 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 296 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 297 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 298 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 299 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 300 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 301 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 302 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 303 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 304 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 305 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 306 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 307 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 308 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 309 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 310 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 311 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 312 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 313 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 314 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 315 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 316 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 317 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 318 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 319 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 320 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 321 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 322 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 323 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 324 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 325 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 326 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 327 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 328 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 329 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 330 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 331 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 332 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 333 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 334 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 335 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 336 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 337 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 338 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 339 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 340 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 341 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 342 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 343 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 344 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 345 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 346 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 347 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 348 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 349 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 350 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 351 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 352 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 353 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 354 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 355 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 356 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 357 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 358 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 359 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 360 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 361 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 362 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 363 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 364 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 365 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 366 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 367 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 368 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 369 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 370 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 371 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 372 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 373 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 374 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 375 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 376 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 377 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 378 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 379 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 380 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 381 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 382 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 383 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 384 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 385 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 386 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 387 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 388 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 389 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 390 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 391 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 392 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 393 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 394 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 395 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 396 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 397 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 398 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 399 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 400 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 401 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 402 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 403 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 404 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 405 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 406 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 407 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 408 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 409 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 410 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 411 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 412 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 413 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 414 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 415 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 416 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 417 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 418 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 419 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 420 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 421 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 422 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 423 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 424 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 425 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 426 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 427 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 428 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 429 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 430 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 431 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 432 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 433 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 434 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 435 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 436 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 437 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 438 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 439 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 440 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 441 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 442 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 443 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 444 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 445 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 446 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 447 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 448 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 449 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 450 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 451 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 452 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 453 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 454 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 455 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 456 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 457 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 458 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 459 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 460 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 461 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 462 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 463 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 464 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 465 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 466 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 467 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 468 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 469 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 470 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 471 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 472 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 473 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 474 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 475 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 476 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 477 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 478 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 479 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 480 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 481 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 482 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 483 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 484 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 485 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 486 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 487 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 488 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 489 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 490 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 491 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 492 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 493 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 494 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 495 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 496 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 497 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 498 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 499 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 500 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 501 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 502 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 503 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 504 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 505 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 506 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 507 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 508 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 509 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 510 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 511 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 512 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 513 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 514 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 515 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 516 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 517 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 518 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 519 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 520 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 521 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 522 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 523 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 524 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 525 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 526 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 527 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 528 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 529 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 530 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 531 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 532 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 533 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 534 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 535 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 536 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 537 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 538 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 539 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 540 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 541 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 542 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 543 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 544 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 545 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 546 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 547 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 548 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 549 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 550 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 551 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 552 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 553 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 554 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 555 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 556 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 557 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 558 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
