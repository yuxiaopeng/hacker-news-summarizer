# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-24.md)

*最后自动更新时间: 2026-03-24 18:22:19*
## 1. LiteLLM Python 包遭遇供应链攻击

**原文标题**: LiteLLM Python package compromised by supply-chain attack

**原文链接**: [https://github.com/BerriAI/litellm/issues/24512](https://github.com/BerriAI/litellm/issues/24512)

2026年3月24日，在 PyPI 托管的 **litellm** Python 软件包中发现了一次严重的供应链攻击，具体影响版本为 **1.82.8**。

**漏洞详情**
此次攻击涉及一个名为 `litellm_init.pth` 的恶意文件。由于 Python 解释器在启动时会自动处理位于 `site-packages` 目录中的 `.pth` 文件，因此即使从未导入 `litellm` 库，恶意代码也会在每次系统运行 Python 时执行。

**恶意行为**
攻击载荷经过双重 Base64 编码以逃避检测。一旦激活，它会对宿主系统进行广泛扫描以收集敏感数据，包括：
*   **环境变量：** 抓取所有激活的 API 密钥和机密信息。
*   **云与基础设施：** AWS、GCP、Azure、Kubernetes 和 Docker 的凭据。
*   **访问密钥：** SSH 密钥、Git 凭据和 SSL/TLS 私钥。
*   **个人数据：** Shell 历史记录、数据库凭据以及各种加密货币钱包。

被盗数据使用 AES-256 和 4096 位 RSA 公钥加密，随后被外泄至 `https://models.litellm.cloud/`。该域名由攻击者控制，通过模仿官方域名 `litellm.ai` 以伪装成合法地址。

**影响及应对措施**
此次攻击影响本地开发机、CI/CD 流水线和生产服务器。如果您已安装了 `litellm==1.82.8`，请执行以下操作：
1.  **检查感染情况：** 在 Python 的 `site-packages` 目录中查找是否存在 `litellm_init.pth` 文件。
2.  **立即补救：** 删除该恶意版本并审计环境是否存在未经授权的活动。
3.  **重置凭据：** **至关重要的一点是，必须重置受影响系统中存在的所有机密信息、API 密钥和 SSH 密钥**，因为这些信息均应被视为已泄露。

目前已敦促 PyPI 撤回受影响版本，BerriAI 团队也正在对其 CI/CD 流水线进行审计，以排查是否存在进一步的渗透。

---

## 2. 通过从 NVMe 流式传输张量，在 32GB Mac 上运行 1T 参数模型。

**原文标题**: Run a 1T parameter model on a 32gb Mac by streaming tensors from NVMe

**原文链接**: [https://github.com/t8/hypura](https://github.com/t8/hypura)

**Hypura** 是一款专为 Apple Silicon 设计的推理调度器，旨在运行超出系统物理内存的大语言模型（LLM）。通过将 NVMe 存储视为有效的内存层级，它能有效防止在消费级硬件上尝试加载巨型模型时通常会出现的系统崩溃和“内存溢出”（OOM）错误。

该系统根据硬件性能和访问模式，将模型张量智能地分布在三个层级：
*   **GPU (Metal)：** 存放注意力层、归一化层和嵌入层等高频访问组件。
*   **RAM：** 作为 GPU 无法容纳的层的溢出缓冲区。
*   **NVMe：** 使用直接 I/O 按需流式传输剩余层。

Hypura 采用两种主要策略来维持性能。对于 Mixtral 8x7B 等**混合专家（MoE）**模型，其“专家流式传输”（expert-streaming）仅加载特定 Token 所需的激活专家，从而减少了 75% 的 I/O 并实现了 99.5% 的缓存命中率。对于 Llama 3.3 70B 等**稠密模型**，它使用“FFN 流式传输”（FFN-streaming）通过动态池缓冲区循环权重。

基准测试显示了其显著的实用性：一台 32GB 内存的 Mac 可以以 2.2 tok/s 的速度运行 31GB 的 Mixtral 模型，并以 0.3 tok/s 的速度运行 40GB 的 Llama 70B——而 llama.cpp 等标准工具在处理这些任务时通常会失败。对于能完全装入内存的模型，Hypura 带来的额外开销为零，能以原生 Metal 速度运行。

其他特性包括**兼容 Ollama 的 API**、用于自动优化的硬件性能分析，以及确保不产生 SSD 磨损的只读 NVMe 路径。有趣的是，开发者指出，该项目主要是利用 LLM 通过苏格拉底式方法构建的，旨在探索 NVMe 支持推理的巨大潜力。

---

## 3. 假说、反题、合题

**原文标题**: Hypothesis, Antithesis, Synthesis

**原文链接**: [https://antithesis.com/blog/2026/hegel/](https://antithesis.com/blog/2026/hegel/)

在《正题、反题、合题》（Hypothesis, Antithesis, Synthesis）一文中，广受欢迎的 Python 库 **Hypothesis** 的开发者宣布推出 **Hegel**。这是一个全新的基于属性的测试（PBT）库系列，旨在为多种编程语言提供高质量的自动化测试。Hegel 由 **Antithesis** 公司开发，目前已支持 **Rust**，并计划近期发布 Go、C++、OCaml 和 TypeScript 版本。

**核心要点：**
*   **技术架构：** Hegel 并没有为每种语言重写 Hypothesis 的复杂逻辑，而是采用了一种“略显疯狂”的架构：它将 Hypothesis 作为数据生成和“缩减”（简化失败用例）的核心引擎，并针对特定语言将其封装在轻量且易用的客户端库中。
*   **PBT 的优势：** Hegel 能够自动搜索手工测试经常遗漏的边界情况，例如“邪门的”Unicode 字符、零值错误以及复杂的结构不变性破坏。它支持“基于模型的测试”，通过将软件行为与简化的参考模型进行对比来验证正确性。
*   **卓越的易用性：** Hegel 旨在摆脱学术化的“QuickCheck”风格，提供更友好的用户体验。它具备“内部缩减”功能以提供高质量的错误报告，并配有测试数据库以确保失败用例的稳定复现。
*   **与 AI 的关联：** 作者认为，PBT 对于验证“不够严谨”的 AI 生成代码至关重要。为此，他们发布了一项“Hegel 技能”，旨在帮助 AI 代理为用户编写基于属性的测试。
*   **Antithesis 集成：** Hegel 能够与 Antithesis 平台无缝集成，使开发者能够从本地 PBT 进阶到在高度并发或分布式系统中进行高级、可复现的漏洞查找。

最终，Hegel 力求利用 Hypothesis 多年的开发积淀，提供功能最强大且最易用的 PBT 工具集，从而提升整个行业的软件可靠性。

---

## 4. 无条款。无条件。

**原文标题**: No Terms. No Conditions

**原文链接**: [https://notermsnoconditions.com](https://notermsnoconditions.com)

《无条款、无条件》（notermsnoconditions.com）一文概述了一个极简、通俗的法律框架，旨在确保简单、透明且比例适度。它构成了网站与用户之间的全部协议，不含任何隐藏条款或外部链接。

该协议包含九个核心要点：
1. **用途**：用户可出于任何合法目的使用本网站，并可自由引用其内容或在其基础上进行开发。
2. **无监管**：内容不经过预先审查或筛选。
3. **无保证**：不对网站的可用性、准确性、连续性或特定用途的适用性提供任何担保。
4. **无承诺**：访问无需获得批准，且不承担任何支持义务或服务承诺。
5. **终结性与责任**：不保证在网站上执行的操作是可逆或可恢复的。用户对其行为及所构建的任何事物承担唯一责任。
6. **完整性**：该文件明确声明不存在额外或隐含的条款。

协议最后指出其“从未”更新过，并邀请他人在深思熟虑的前提下，针对自身用途采用或引用这些条款。通过这种设计，该网站提供了一个“所见即所得”的法律环境，剔除了数字服务协议中常见的复杂性。

---

## 5. Show HN: Email.md – 将 Markdown 转换为响应式且邮件安全的 HTML

**原文标题**: Show HN: Email.md – Markdown to responsive, email-safe HTML

**原文链接**: [https://www.emailmd.dev/](https://www.emailmd.dev/)

**Email.md** 是一款在 Hacker News 上备受关注的开发者工具，旨在通过 Markdown 简化响应式且兼容性良好的电子邮件 HTML 的创建。它致力于消除“HTMHELL”（即极其繁琐的手动邮件编码过程），让用户通过编写简洁的内容，即可自动转换为兼容各种邮件客户端的布局。

**核心特性与功能：**
*   **基于 Markdown 的工作流：** 用户编写标准 Markdown，工具将其转换为实现跨客户端一致渲染所需的样式化表格 HTML。
*   **前置元数据（Front Matter）配置：** 支持 YAML 前置元数据，用于定义预览文本（preheaders）和视觉主题（如深色模式）等信息。
*   **自定义布局块：** 使用特定容器（如 `::: header`、`::: callout` 和 `::: footer`）轻松构建邮件结构，无需编写复杂的 CSS。
*   **开发者友好：** 该工具可通过 npm (`npm install emailmd`) 集成到项目中，并提供完善的文档、网页端编辑器及预制模板。

总之，Email.md 为希望发送专业、响应式电子邮件（如确认码或新闻通讯）的开发者提供了一套流线化解决方案，使其无需再受困于旧版邮件 HTML 标准带来的技术债务。

---

## 6. Lago (YC S21) 正在招聘

**原文标题**: Lago (YC S21) Is Hiring

**原文链接**: [https://getlago.notion.site/Lago-Product-Engineer-AI-Agents-for-Growth-327ef63110d280cdb030ccf429d3e4d7?source=copy_link](https://getlago.notion.site/Lago-Product-Engineer-AI-Agents-for-Growth-327ef63110d280cdb030ccf429d3e4d7?source=copy_link)

提供的文本是一个错误信息，提示查看 Notion 页面需要启用 JavaScript。不过，根据标题和公司背景，以下是该招聘公告的简要总结：

**总结：Lago (YC S21) 正在招聘**

Lago 是 Y Combinator 2021 年夏季营（S21）的成员，目前正在为其团队招募人才。Lago 提供开源的计量和基于用量的计费基础设施，旨在作为 Stripe Billing 或 Chargebee 等专有系统的透明替代方案。

其招聘的核心要点通常包括：

*   **公司使命：** Lago 旨在通过提供灵活、开发者友好的计费 API 和架构，赋能工程师和财务团队，以处理复杂的按量计费模式。
*   **目标职位：** 尽管具体列表因技术错误未能显示，但 Lago 通常招聘**全栈工程**、**数据工程**（处理海量事件计量）以及**产品增长**等领域的岗位。
*   **文化与技术栈：** 作为一个开源项目，公司非常重视透明度和社区贡献。其技术栈通常涉及 React、Ruby on Rails 和 Go 等现代技术，并专注于高扩展性和数据准确性。
*   **工作环境：** Lago 以支持远程办公或混合办公模式而闻名，其总部位于法国巴黎。

建议有意向的候选人在启用 JavaScript 后重新访问 Notion 链接，以查看具体的职位描述和申请要求。

---

## 7. 托尼·霍尔及其在计算机科学领域的印记

**原文标题**: Tony Hoare and His Imprint on Computer Science

**原文链接**: [https://cacm.acm.org/blogcacm/tony-hoare-and-his-imprint-on-computer-science/](https://cacm.acm.org/blogcacm/tony-hoare-and-his-imprint-on-computer-science/)

《托尼·霍尔及其对计算机科学的深远影响》探讨了图灵奖得主托尼·霍尔爵士（Sir Tony Hoare）的卓越贡献。他的工作将计算机编程从一门手艺转变为一门严谨的数学学科。文章重点介绍了其成就中的几个核心支柱：

*   **快速排序 (1959)：** 霍尔在苏联留学期间开发，至今仍是历史上最高效、应用最广泛的排序算法之一，体现了他为基础问题寻找优雅解决方案的能力。
*   **霍尔逻辑 (1969)：** 霍尔引入了一套利用“霍尔三元组”（前置条件、指令、后置条件）验证程序正确性的形式系统。该框架为确保软件行为符合预期提供了数学基础。
*   **通信顺序进程 (CSP)：** 他在 CSP 方面的工作为描述并发系统中的交互模式提供了一种形式语言。这项研究奠定了现代并行计算的基础，并影响了 Go 和 Erlang 等编程语言的设计。
*   **“价值十亿美元的错误”：** 文章提到了霍尔对其 1965 年发明“空引用”（null reference）的著名自我批评。他后来对此深表遗憾，称其在随后的几十年里导致了无数的错误和安全漏洞。

在其跨越 Elliott Brothers、牛津大学和微软研究院的职业生涯中，霍尔始终倡导软件应具备可证明的正确性。他留下的印记在于严谨的逻辑；他从根本上改变了业界对代码可靠性、结构化和形式化验证的认知，确保了计算机科学的理论基础与实际工程实践始终紧密相连。

---

## 8. Show HN: Gemini can now natively embed video, so I built sub-second video search

**原文标题**: Show HN: Gemini can now natively embed video, so I built sub-second video search

**原文链接**: [https://github.com/ssrajadh/sentrysearch](https://github.com/ssrajadh/sentrysearch)

**SentrySearch** is a command-line tool designed for sub-second semantic search over video footage, specifically tailored for dashcam recordings. Leveraging Google’s **Gemini Embedding 2** model, the tool allows users to find specific events by typing natural language queries (e.g., "red truck running a stop sign") and receiving automatically trimmed video clips of the matches.

### **How It Works**
The core innovation is Gemini’s ability to **natively embed video**. Unlike traditional systems that require a "middleman" like text transcription or frame captioning, Gemini projects raw video pixels and text queries into the same 768-dimensional vector space. 
1. **Indexing:** The tool splits footage into overlapping chunks, preprocesses them (downscaling to 480p at 5fps), and generates embeddings.
2. **Storage:** These vectors are stored in a local **ChromaDB** database.
3. **Search:** When a user enters a query, the text is converted into a vector and matched against the video embeddings. The top result is then extracted using **ffmpeg**.

### **Key Features and Costs**
*   **Cost Efficiency:** Indexing costs approximately **$2.50 per hour** of footage. To reduce costs, the tool includes "still-frame skipping," which uses heuristics to avoid indexing clips with no visual change (like a parked car).
*   **Performance:** Preprocessing reduces upload times, while native embeddings enable near-instantaneous search results.
*   **Compatibility:** While inspired by Tesla Sentry Mode, it works with any MP4 files.

### **Limitations**
As the Gemini Embedding 2 model is currently in preview, pricing and behavior may change. Current limitations include a heuristic approach to still-frame detection and potential search issues if an event spans across chunk boundaries.

SentrySearch requires Python 3.10+, a Gemini API key, and ffmpeg. It represents a significant shift in video analysis by making hours of raw footage searchable without manual tagging or complex AI pipelines.

---

## 9. Testing the Swift C compatibility with Raylib (+WASM)

**原文标题**: Testing the Swift C compatibility with Raylib (+WASM)

**原文链接**: [https://carette.xyz/posts/swift_c_compatibility_with_raylib/](https://carette.xyz/posts/swift_c_compatibility_with_raylib/)

生成摘要时出错

---

## 10. Nanobrew: The fastest macOS package manager compatible with brew

**原文标题**: Nanobrew: The fastest macOS package manager compatible with brew

**原文链接**: [https://nanobrew.trilok.ai/](https://nanobrew.trilok.ai/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 2 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 3 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 4 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 5 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 6 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 7 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 8 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 9 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 10 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 11 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 12 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 13 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 14 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 15 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 16 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 17 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 18 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 19 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 20 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 21 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 22 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 23 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 24 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 25 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 26 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 27 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 28 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 29 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 30 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 31 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 32 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 33 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 34 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 35 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 36 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 37 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 38 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 39 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 40 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 41 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 42 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 43 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 44 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 45 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 46 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 47 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 48 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 49 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 50 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 51 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 52 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 53 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 54 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 55 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 56 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 57 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 58 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 59 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 60 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 61 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 62 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 63 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 64 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 65 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 66 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 67 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 68 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 69 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 70 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 71 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 72 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 73 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 74 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 75 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 76 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 77 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 78 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 79 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 80 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 81 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 82 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 83 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 84 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 85 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 86 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 87 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 88 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 89 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 90 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 91 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 92 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 93 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 94 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 95 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 96 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 97 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 98 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 99 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 100 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 101 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 102 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 103 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 104 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 105 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 106 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 107 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 108 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 109 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 110 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 111 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 112 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 113 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 114 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 115 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 116 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 117 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 118 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 119 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 120 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 121 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 122 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 123 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 124 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 125 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 126 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 127 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 128 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 129 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 130 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 131 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 132 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 133 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 134 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 135 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 136 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 137 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 138 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 139 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 140 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 141 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 142 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 143 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 144 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 145 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 146 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 147 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 148 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 149 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 150 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 151 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 152 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 153 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 154 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 155 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 156 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 157 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 158 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 159 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 160 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 161 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 162 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 163 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 164 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 165 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 166 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 167 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 168 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 169 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 170 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 171 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 172 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 173 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 174 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 175 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 176 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 177 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 178 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 179 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 180 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 181 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 182 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 183 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 184 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 185 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 186 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 187 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 188 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 189 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 190 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 191 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 192 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 193 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 194 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 195 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 196 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 197 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 198 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 199 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 200 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 201 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 202 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 203 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 204 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 205 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 206 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 207 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 208 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 209 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 210 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 211 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 212 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 213 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 214 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 215 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 216 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 217 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 218 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 219 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 220 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 221 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 222 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 223 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 224 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 225 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 226 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 227 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 228 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 229 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 230 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 231 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 232 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 233 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 234 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 235 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 236 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 237 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 238 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 239 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 240 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 241 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 242 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 243 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 244 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 245 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 246 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 247 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 248 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 249 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 250 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 251 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 252 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 253 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 254 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 255 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 256 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 257 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 258 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 259 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 260 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 261 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 262 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 263 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 264 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 265 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 266 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 267 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 268 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 269 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 270 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 271 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 272 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 273 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 274 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 275 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 276 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 277 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 278 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 279 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 280 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 281 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 282 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 283 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 284 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 285 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 286 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 287 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 288 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 289 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 290 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 291 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 292 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 293 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 294 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 295 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 296 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 297 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 298 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 299 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 300 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 301 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 302 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 303 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 304 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 305 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 306 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 307 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 308 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 309 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 310 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 311 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 312 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 313 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 314 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 315 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 316 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 317 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 318 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 319 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 320 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 321 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 322 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 323 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 324 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 325 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 326 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 327 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 328 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 329 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 330 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 331 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 332 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 333 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 334 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 335 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 336 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 337 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 338 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 339 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 340 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 341 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 342 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 343 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 344 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 345 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 346 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 347 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 348 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 349 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 350 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 351 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 352 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 353 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 354 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 355 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 356 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 357 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 358 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 359 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 360 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 361 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 362 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 363 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 364 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 365 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 366 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 367 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 368 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 369 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
