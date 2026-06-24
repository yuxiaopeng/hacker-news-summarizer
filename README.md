# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-06-24.md)

*最后自动更新时间: 2026-06-24 19:28:14*
## 1. OpenAI发布首款由博通打造的定制芯片

**原文标题**: OpenAI unveils its first custom chip, built by Broadcom

**原文链接**: [https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/)

OpenAI 发布了首款自研处理器，这是一款名为 Jalapeño 的推理芯片，由其与博通（Broadcom）合作开发。该芯片专为处理推理任务（即运行预构建 AI 模型的过程）而设计，而非资源密集型的预训练阶段，后者预计仍将依赖英伟达（Nvidia）的硬件。

此次发布的一个关键亮点是，OpenAI 利用其自身的 AI 模型辅助了该芯片的开发。初步结果显示，Jalapeño 的能效比显著优于目前最先进的替代产品。通过研发自研芯片，OpenAI 旨在减少对英伟达 GPU 的高度依赖，并降低运行代码模型等实时服务的运营成本。

此举标志着 OpenAI 向垂直整合迈出了战略性的一步。通过设计包括芯片架构、内存系统和网络在内的自有基础设施，OpenAI 可以优化其技术栈的每一个层面。这种做法与谷歌（Google）和亚马逊（Amazon）等竞争对手采用的“AI 加速器”策略如出一辙。

OpenAI 总裁格雷格·布罗克曼（Greg Brockman）强调，该处理器的设计初衷是加速特定的、目前尚未得到充分支持的工作负载。最终，该公司希望通过优化底层基础设施的经济效益，使 Jalapeño 芯片能让其 AI 模型对用户而言变得更快、更可靠且更实惠。

---

## 2. RubyLLM：支持所有主流 AI 提供商的 Ruby 框架

**原文标题**: RubyLLM: A Ruby framework for all major AI providers

**原文链接**: [https://rubyllm.com/](https://rubyllm.com/)

**RubyLLM** 是一个统一、轻量级的框架，旨在简化 AI 在 Ruby 应用程序中的集成。它通过为涵盖所有主要供应商（包括 OpenAI、Anthropic (Claude)、Google (Gemini/VertexAI)、xAI、Mistral 以及通过 Ollama 运行的本地模型）的 800 多种模型提供单一、优美的接口，消除了使用多个不一致客户端库带来的阻碍。

**核心特性：**
*   **多模态能力：** 除了标准的文本聊天，该框架还通过简洁的 `with:` 语法处理视觉（图像/视频）、音频转录和文档分析（PDF、CSV 等）。
*   **全面的 AI 工具：** 内置对图像生成 (`paint`)、嵌入 (`embed`) 和内容审核的支持。
*   **高级架构：** 开发者可以创建自定义 **Tools**（允许 AI 执行 Ruby 方法），定义具有特定指令的 **Agents**，并使用 JSON schema 强制执行**结构化输出**。
*   **性能与开发者体验：** 该库经过“实战检验”，且依赖极少（Faraday、Zeitwerk 和 Marcel）。它支持流式响应、基于 Fiber 的并发以及深度思考（Extended Thinking）推理。

**Rails 集成：**
RubyLLM 为 Ruby on Rails 提供了深度集成，包括通过 `acts_as_chat` 实现的 ActiveRecord 支持。它提供了数据库迁移生成器和开箱即用的聊天 UI，让开发者几乎可以瞬间在 `localhost:3000/chats` 部署功能完备的 AI 界面。

总之，RubyLLM 为 Ruby 开发者提供了一个“一站式解决方案”，用于构建从简单聊天机器人到复杂的 RAG（检索增强生成）应用及自主代理的一切，而无需承担管理多种 API 规范的开销。

---

## 3. NSA 在与 Anthropic 的纠纷中失去了对 Mythos 的访问权限

**原文标题**: NSA lost access to Mythos amid Anthropic dispute

**原文链接**: [https://www.nytimes.com/2026/06/23/us/politics/nsa-lost-access-anthropic-tool.html](https://www.nytimes.com/2026/06/23/us/politics/nsa-lost-access-anthropic-tool.html)

无法访问文章链接。

---

## 4. There are a few things that I look back on as my mistakes in the early days

**原文标题**: There are a few things that I look back on as my mistakes in the early days

**原文链接**: [https://twitter.com/ID_AA_Carmack/status/2069799283369345247](https://twitter.com/ID_AA_Carmack/status/2069799283369345247)

In this retrospective, legendary programmer John Carmack reflects on his management and technical mistakes during the early days of id Software, particularly during the development of *Quake*.

Carmack highlights several key areas of regret:

*   **Technical Over-ambition:** He believes *Quake* was too ambitious for its time. He suggests that building on an enhanced *Doom* engine first would have provided a more stable foundation for designers, rather than "rug-pulling" the technology during development. 
*   **Management and Burnout:** Carmack admits to pushing his team too hard with "startup intensity," failing to recognize that a maturing company needs more "slack" to prevent burnout. He also acknowledges reaching his own personal limits of productivity during this era.
*   **Business Structure:** He criticizes the company’s original stock and buy/sell agreements, noting that they created poor incentives. He suggests that the standard Silicon Valley approach of vesting stock would have been a superior model.
*   **Design Culture:** A major point of friction was the requirement for level designers to also be high-end visual artists. This expectation, while set early on, led to internal infighting and the disparagement of designers who focused more on gameplay than aesthetics.

Carmack concludes by specifically apologizing to designer Sandy Petersen for the toxic environment created by these design expectations, acknowledging that the company should have paired specialized artists with designers much earlier.

---

## 5. 我们将 Bunny DNS 设为免费

**原文标题**: We’re making Bunny DNS free

**原文链接**: [https://bunny.net/blog/were-making-bunny-dns-free/](https://bunny.net/blog/were-making-bunny-dns-free/)

生成摘要时出错

---

## 6. PR spam today looks like email spam in the early 2000s

**原文标题**: PR spam today looks like email spam in the early 2000s

**原文链接**: [https://www.greptile.com/blog/prs-on-openclaw](https://www.greptile.com/blog/prs-on-openclaw)

生成摘要时出错

---

## 7. I taught a bucket to speak Git

**原文标题**: I taught a bucket to speak Git

**原文链接**: [https://www.tigrisdata.com/blog/objgit/](https://www.tigrisdata.com/blog/objgit/)

生成摘要时出错

---

## 8. Computer use in Gemini 3.5 Flash

**原文标题**: Computer use in Gemini 3.5 Flash

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/)

生成摘要时出错

---

## 9. Show HN: Nub – A Bun-like all-in-one toolkit for Node.js

**原文标题**: Show HN: Nub – A Bun-like all-in-one toolkit for Node.js

**原文链接**: [https://github.com/nubjs/nub](https://github.com/nubjs/nub)

生成摘要时出错

---

## 10. Stealing Is a Skill

**原文标题**: Stealing Is a Skill

**原文链接**: [https://ben-mini.com/2026/stealing-is-a-skill](https://ben-mini.com/2026/stealing-is-a-skill)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 2 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 3 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 4 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 5 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 6 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 7 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 8 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 9 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 10 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 11 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 12 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 13 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 14 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 15 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 16 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 17 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 18 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 19 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 20 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 21 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 22 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 23 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 24 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 25 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 26 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 27 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 28 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 29 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 30 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 31 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 32 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 33 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 34 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 35 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 36 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 37 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 38 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 39 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 40 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 41 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 42 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 43 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 44 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 45 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 46 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 47 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 48 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 49 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 50 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 51 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 52 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 53 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 54 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 55 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 56 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 57 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 58 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 59 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 60 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 61 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 62 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 63 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 64 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 65 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 66 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 67 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 68 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 69 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 70 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 71 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 72 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 73 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 74 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 75 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 76 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 77 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 78 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 79 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 80 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 81 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 82 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 83 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 84 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 85 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 86 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 87 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 88 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 89 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 90 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 91 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 92 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 93 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 94 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 95 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 96 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 97 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 98 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 99 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 100 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 101 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 102 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 103 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 104 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 105 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 106 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 107 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 108 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 109 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 110 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 111 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 112 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 113 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 114 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 115 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 116 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 117 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 118 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 119 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 120 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 121 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 122 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 123 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 124 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 125 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 126 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 127 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 128 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 129 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 130 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 131 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 132 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 133 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 134 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 135 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 136 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 137 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 138 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 139 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 140 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 141 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 142 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 143 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 144 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 145 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 146 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 147 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 148 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 149 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 150 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 151 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 152 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 153 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 154 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 155 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 156 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 157 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 158 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 159 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 160 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 161 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 162 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 163 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 164 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 165 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 166 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 167 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 168 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 169 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 170 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 171 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 172 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 173 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 174 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 175 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 176 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 177 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 178 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 179 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 180 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 181 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 182 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 183 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 184 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 185 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 186 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 187 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 188 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 189 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 190 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 191 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 192 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 193 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 194 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 195 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 196 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 197 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 198 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 199 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 200 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 201 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 202 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 203 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 204 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 205 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 206 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 207 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 208 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 209 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 210 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 211 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 212 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 213 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 214 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 215 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 216 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 217 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 218 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 219 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 220 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 221 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 222 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 223 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 224 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 225 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 226 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 227 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 228 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 229 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 230 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 231 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 232 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 233 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 234 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 235 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 236 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 237 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 238 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 239 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 240 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 241 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 242 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 243 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 244 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 245 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 246 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 247 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 248 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 249 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 250 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 251 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 252 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 253 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 254 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 255 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 256 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 257 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 258 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 259 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 260 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 261 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 262 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 263 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 264 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 265 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 266 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 267 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 268 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 269 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 270 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 271 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 272 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 273 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 274 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 275 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 276 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 277 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 278 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 279 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 280 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 281 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 282 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 283 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 284 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 285 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 286 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 287 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 288 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 289 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 290 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 291 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 292 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 293 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 294 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 295 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 296 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 297 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 298 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 299 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 300 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 301 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 302 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 303 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 304 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 305 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 306 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 307 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 308 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 309 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 310 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 311 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 312 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 313 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 314 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 315 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 316 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 317 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 318 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 319 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 320 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 321 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 322 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 323 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 324 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 325 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 326 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 327 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 328 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 329 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 330 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 331 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 332 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 333 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 334 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 335 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 336 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 337 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 338 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 339 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 340 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 341 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 342 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 343 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 344 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 345 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 346 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 347 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 348 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 349 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 350 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 351 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 352 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 353 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 354 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 355 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 356 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 357 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 358 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 359 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 360 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 361 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 362 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 363 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 364 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 365 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 366 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 367 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 368 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 369 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 370 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 371 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 372 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 373 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 374 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 375 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 376 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 377 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 378 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 379 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 380 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 381 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 382 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 383 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 384 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 385 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 386 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 387 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 388 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 389 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 390 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 391 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 392 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 393 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 394 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 395 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 396 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 397 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 398 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 399 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 400 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 401 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 402 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 403 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 404 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 405 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 406 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 407 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 408 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 409 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 410 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 411 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 412 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 413 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 414 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 415 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 416 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 417 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 418 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 419 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 420 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 421 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 422 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 423 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 424 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 425 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 426 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 427 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 428 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 429 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 430 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 431 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 432 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 433 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 434 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 435 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 436 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 437 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 438 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 439 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 440 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 441 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 442 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 443 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 444 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 445 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 446 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 447 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 448 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 449 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 450 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 451 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 452 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 453 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 454 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 455 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 456 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 457 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 458 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 459 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 460 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 461 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
