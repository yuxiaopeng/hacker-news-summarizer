# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-09-25.md)

*最后自动更新时间: 2026-09-25 20:42:09*
## 1. Ollaya – 面向开源 Jev 风格决策模型的 Ollama

**原文标题**: Ollaya – Ollama for open-source, Jev-style decision models

**原文链接**: [https://ollaya.dev/](https://ollaya.dev/)

Ollaya 是一个开源的本地平台，专为运行“决策模型”而设计。这些模型是专门的分类器，能够在毫秒级时间内为问题提供经过校准的、强类型的答案。受到 Ollama 运行大语言模型（LLM）方式的启发，Ollaya 允许用户在自己的硬件上私密地执行意图检测、情感分析和任务分诊等任务，且无需支付 Token 费用。

核心特性与优势包括：

*   **极速性能：** 由于这些模型通过单次前向传播而非逐 Token 生成来运行，其延迟显著低于标准 LLM。在 NVIDIA RTX 4090 上，处理一个包含五个问题的请求通常仅需约 10 毫秒，而托管 API 替代方案则需要 200 毫秒以上。
*   **API 兼容性：** Ollaya 与 TypeSafe 的 API 无缝兼容。开发者只需更改基础 URL，即可将 TypeSafe Python SDK 指向本地 Ollaya 服务器。
*   **开放模型：** 该平台支持多种权重开放的模型，包括 **Laya**（多语言和英语决策模型）、**Decider**（基于 Qwen 的精确模型）、**NLI**（零样本蕴含分类器）以及 **GliClass**。
*   **隐私与校准：** 所有数据均保留在本地，并通过 ONNX Runtime 进行处理。模型经过高度校准，可提供可靠的概率评分（例如，Laya 的校准误差仅为 0.081，而托管竞品为 0.246）。
*   **跨平台支持：** Ollaya 支持 macOS、Windows、Linux 和 Docker。虽然它可以在 CPU 上运行，但针对 NVIDIA GPU（需要 R580 或更高版本的驱动程序）进行了优化，以实现最高性能。

总之，Ollaya 提供了一种快速、私密且极具成本效益的方式，利用开源硬件和权重将高速分类和决策功能集成到应用程序中。

---

## 2. Alan Kay: Shannon gave us a way of dealing with noisy channels [video]

**原文标题**: Alan Kay: Shannon gave us a way of dealing with noisy channels [video]

**原文链接**: [https://www.youtube.com/watch?v=Cjntrqhn8pk](https://www.youtube.com/watch?v=Cjntrqhn8pk)

生成摘要时出错

---

## 3. Platform-independent SIMD in Go

**原文标题**: Platform-independent SIMD in Go

**原文链接**: [https://go.dev/blog/simd-experiment](https://go.dev/blog/simd-experiment)

生成摘要时出错

---

## 4. Show HN: Jev Plays Pokémon Red

**原文标题**: Show HN: Jev Plays Pokémon Red

**原文链接**: [https://jev-pokemon.vercel.app/](https://jev-pokemon.vercel.app/)

生成摘要时出错

---

## 5. Advice to a Beginning Graduate Student (2001)

**原文标题**: Advice to a Beginning Graduate Student (2001)

**原文链接**: [https://www.cs.cmu.edu/~mblum/research/pdf/grad.html](https://www.cs.cmu.edu/~mblum/research/pdf/grad.html)

生成摘要时出错

---

## 6. First Principles Thinking

**原文标题**: First Principles Thinking

**原文链接**: [https://sunilsadasivan.com/writing/first-principles-thinking/](https://sunilsadasivan.com/writing/first-principles-thinking/)

生成摘要时出错

---

## 7. Git-bug: Distributed, offline-first bug tracker embedded in Git

**原文标题**: Git-bug: Distributed, offline-first bug tracker embedded in Git

**原文链接**: [https://github.com/git-bug/git-bug](https://github.com/git-bug/git-bug)

生成摘要时出错

---

## 8. Google's first Suncatcher orbital data center test launches October 1

**原文标题**: Google's first Suncatcher orbital data center test launches October 1

**原文链接**: [https://arstechnica.com/google/2026/09/googles-first-suncatcher-orbital-data-center-test-launches-october-1/](https://arstechnica.com/google/2026/09/googles-first-suncatcher-orbital-data-center-test-launches-october-1/)

生成摘要时出错

---

## 9. 美国上诉法院维持将 Anthropic 列为供应链风险的认定。

**原文标题**: U.S. appeals court upholds designation of Anthropic as supply chain risk

**原文链接**: [https://www.cnbc.com/2026/09/25/pentagon-anthropic-ai-risk-appeals-court.html](https://www.cnbc.com/2026/09/25/pentagon-anthropic-ai-risk-appeals-court.html)

A federal appeals court in Washington, D.C., has upheld the Pentagon’s designation of AI startup Anthropic as a "supply chain risk." The 2-1 ruling maintains a ban that prevents the U.S. military and its defense contractors from using Anthropic’s Claude models, citing national security concerns.

The legal battle stems from failed negotiations between Anthropic and the Department of Defense (DOD) regarding the deployment of AI on the military’s "GenAI.mil" platform. Anthropic sought guarantees that its technology would not be used for fully autonomous weaponry or domestic mass surveillance. In response, Defense Secretary Pete Hegseth accused the company of attempting to "seize veto power" over military operations. The DOD argued that "overly constrained" models could be subject to manipulation or unexpected shutdowns during critical operations.

The majority opinion, written by Judge Gregory Katsas, stated that the executive branch holds the constitutional authority to balance national security risks. This decision follows a conflicting ruling from a San Francisco federal judge last month, who found a parallel DOD designation against the company to be illegal.

The ruling highlights the deepening rift between the Trump administration and Anthropic CEO Dario Amodei. President Trump has publicly criticized Amodei on social media and excluded him from high-profile events, such as a recent state dinner for Chinese President Xi Jinping.

Anthropic expressed "respectful disagreement" with the court’s decision, pointing to the favorable ruling in San Francisco as evidence of its position. The appellate panel has delayed the decision’s immediate effect to allow Anthropic time to petition for a rehearing or appeal the case to the Supreme Court.

---

## 10. Bug: Border radius has infected VSCode editor

**原文标题**: Bug: Border radius has infected VSCode editor

**原文链接**: [https://github.com/microsoft/vscode/issues/338035](https://github.com/microsoft/vscode/issues/338035)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 2 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 3 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 4 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 5 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 6 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 7 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 8 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 9 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 10 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 11 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 12 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 13 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 14 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 15 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 16 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 17 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 18 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 19 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 20 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 21 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 22 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 23 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 24 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 25 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 26 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 27 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 28 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 29 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 30 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 31 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 32 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 33 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 34 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 35 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 36 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 37 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 38 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 39 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 40 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 41 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 42 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 43 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 44 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 45 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 46 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 47 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 48 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 49 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 50 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 51 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 52 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 53 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 54 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 55 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 56 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 57 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 58 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 59 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 60 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 61 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 62 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 63 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 64 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 65 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 66 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 67 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 68 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 69 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 70 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 71 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 72 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 73 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 74 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 75 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 76 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 77 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 78 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 79 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 80 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 81 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 82 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 83 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 84 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 85 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 86 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 87 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 88 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 89 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 90 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 91 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 92 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 93 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 94 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 95 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 96 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 97 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 98 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 99 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 100 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 101 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 102 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 103 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 104 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 105 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 106 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 107 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 108 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 109 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 110 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 111 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 112 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 113 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 114 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 115 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 116 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 117 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 118 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 119 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 120 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 121 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 122 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 123 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 124 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 125 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 126 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 127 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 128 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 129 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 130 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 131 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 132 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 133 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 134 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 135 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 136 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 137 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 138 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 139 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 140 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 141 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 142 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 143 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 144 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 145 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 146 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 147 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 148 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 149 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 150 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 151 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 152 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 153 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 154 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 155 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 156 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 157 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 158 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 159 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 160 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 161 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 162 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 163 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 164 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 165 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 166 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 167 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 168 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 169 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 170 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 171 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 172 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 173 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 174 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 175 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 176 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 177 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 178 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 179 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 180 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 181 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 182 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 183 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 184 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 185 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 186 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 187 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 188 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 189 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 190 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 191 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 192 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 193 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 194 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 195 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 196 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 197 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 198 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 199 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 200 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 201 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 202 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 203 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 204 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 205 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 206 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 207 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 208 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 209 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 210 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 211 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 212 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 213 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 214 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 215 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 216 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 217 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 218 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 219 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 220 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 221 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 222 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 223 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 224 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 225 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 226 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 227 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 228 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 229 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 230 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 231 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 232 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 233 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 234 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 235 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 236 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 237 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 238 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 239 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 240 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 241 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 242 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 243 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 244 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 245 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 246 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 247 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 248 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 249 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 250 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 251 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 252 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 253 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 254 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 255 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 256 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 257 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 258 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 259 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 260 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 261 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 262 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 263 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 264 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 265 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 266 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 267 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 268 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 269 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 270 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 271 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 272 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 273 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 274 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 275 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 276 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 277 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 278 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 279 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 280 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 281 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 282 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 283 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 284 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 285 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 286 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 287 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 288 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 289 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 290 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 291 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 292 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 293 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 294 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 295 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 296 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 297 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 298 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 299 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 300 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 301 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 302 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 303 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 304 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 305 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 306 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 307 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 308 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 309 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 310 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 311 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 312 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 313 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 314 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 315 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 316 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 317 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 318 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 319 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 320 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 321 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 322 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 323 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 324 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 325 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 326 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 327 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 328 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 329 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 330 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 331 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 332 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 333 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 334 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 335 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 336 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 337 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 338 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 339 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 340 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 341 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 342 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 343 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 344 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 345 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 346 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 347 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 348 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 349 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 350 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 351 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 352 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 353 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 354 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 355 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 356 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 357 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 358 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 359 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 360 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 361 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 362 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 363 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 364 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 365 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 366 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 367 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 368 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 369 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 370 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 371 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 372 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 373 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 374 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 375 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 376 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 377 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 378 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 379 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 380 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 381 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 382 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 383 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 384 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 385 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 386 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 387 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 388 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 389 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 390 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 391 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 392 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 393 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 394 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 395 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 396 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 397 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 398 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 399 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 400 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 401 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 402 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 403 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 404 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 405 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 406 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 407 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 408 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 409 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 410 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 411 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 412 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 413 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 414 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 415 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 416 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 417 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 418 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 419 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 420 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 421 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 422 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 423 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 424 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 425 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 426 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 427 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 428 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 429 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 430 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 431 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 432 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 433 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 434 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 435 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 436 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 437 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 438 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 439 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 440 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 441 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 442 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 443 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 444 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 445 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 446 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 447 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 448 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 449 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 450 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 451 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 452 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 453 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 454 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 455 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 456 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 457 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 458 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 459 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 460 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 461 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 462 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 463 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 464 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 465 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 466 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 467 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 468 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 469 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 470 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 471 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 472 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 473 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 474 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 475 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 476 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 477 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 478 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 479 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 480 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 481 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 482 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 483 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 484 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 485 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 486 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 487 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 488 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 489 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 490 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 491 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 492 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 493 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 494 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 495 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 496 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 497 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 498 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 499 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 500 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 501 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 502 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 503 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 504 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 505 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 506 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 507 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 508 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 509 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 510 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 511 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 512 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 513 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 514 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 515 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 516 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 517 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 518 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 519 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 520 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 521 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 522 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 523 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 524 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 525 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 526 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 527 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 528 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 529 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 530 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 531 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 532 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 533 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 534 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 535 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 536 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 537 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 538 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 539 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 540 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 541 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 542 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 543 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 544 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 545 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 546 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 547 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 548 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 549 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 550 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 551 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 552 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
