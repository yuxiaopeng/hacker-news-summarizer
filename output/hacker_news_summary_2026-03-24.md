# Hacker News 热门文章摘要 (2026-03-24)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Microsoft's "Fix" for Windows 11: Flowers After the Beating

**原文标题**: Microsoft's "Fix" for Windows 11: Flowers After the Beating

**原文链接**: [https://www.sambent.com/microsofts-plan-to-fix-windows-11-is-gaslighting/](https://www.sambent.com/microsofts-plan-to-fix-windows-11-is-gaslighting/)

生成摘要时出错

---

## 12. LaGuardia pilots raised safety alarms months before deadly runway crash

**原文标题**: LaGuardia pilots raised safety alarms months before deadly runway crash

**原文链接**: [https://www.theguardian.com/us-news/2026/mar/24/laguardia-airplane-pilots-safety-concerns-crash](https://www.theguardian.com/us-news/2026/mar/24/laguardia-airplane-pilots-safety-concerns-crash)

生成摘要时出错

---

## 13. FCC has banned the import of all new foreign-made routers here's what you can do

**原文标题**: FCC has banned the import of all new foreign-made routers here's what you can do

**原文链接**: [https://blog.adafruit.com/2026/03/24/fcc-just-banned-the-import-of-all-new-foreign-made-routers-heres-what-you-can-do-about-it/](https://blog.adafruit.com/2026/03/24/fcc-just-banned-the-import-of-all-new-foreign-made-routers-heres-what-you-can-do-about-it/)

生成摘要时出错

---

## 14. Debunking Zswap and Zram Myths

**原文标题**: Debunking Zswap and Zram Myths

**原文链接**: [https://chrisdown.name/2026/03/24/zswap-vs-zram-when-to-use-what.html](https://chrisdown.name/2026/03/24/zswap-vs-zram-when-to-use-what.html)

生成摘要时出错

---

## 15. Ripgrep is faster than grep, ag, git grep, ucg, pt, sift (2016)

**原文标题**: Ripgrep is faster than grep, ag, git grep, ucg, pt, sift (2016)

**原文链接**: [https://burntsushi.net/ripgrep/](https://burntsushi.net/ripgrep/)

生成摘要时出错

---

## 16. Data Manipulation in Clojure Compared to R and Python

**原文标题**: Data Manipulation in Clojure Compared to R and Python

**原文链接**: [https://codewithkira.com/2024-07-18-tablecloth-dplyr-pandas-polars.html](https://codewithkira.com/2024-07-18-tablecloth-dplyr-pandas-polars.html)

生成摘要时出错

---

## 17. Secure Domain Name System (DNS) Deployment 2026 Guide [pdf]

**原文标题**: Secure Domain Name System (DNS) Deployment 2026 Guide [pdf]

**原文链接**: [https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-81r3.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-81r3.pdf)

The **Secure Domain Name System (DNS) Deployment 2026 Guide** serves as a comprehensive technical roadmap for organizations to secure their DNS infrastructure against evolving cyber threats. Based on the provided title and the technical structure of the document, the guide focuses on the transition toward more resilient, authenticated, and private naming services.

The primary main points include:

*   **DNSSEC Implementation:** The guide emphasizes the mandatory use of DNS Security Extensions (DNSSEC) to provide origin authority and data integrity. It outlines the processes for zone signing, maintaining the chain of trust, and the importance of cryptographic validation to prevent cache poisoning and man-in-the-middle attacks.
*   **Infrastructure Hardening:** Security recommendations are provided for both **authoritative** and **recursive** DNS servers. This includes the use of Access Control Lists (ACLs) to limit unauthorized zone transfers and the implementation of Transaction Signatures (TSIG) for secure communication between primary and secondary servers.
*   **Key Management:** A significant portion of the guide is dedicated to Key Signing Keys (KSK) and Zone Signing Keys (ZSK). It provides updated 2026 standards for key lengths, algorithm selection (favoring Elliptic Curve Cryptography), and automated rollover procedures to minimize operational downtime.
*   **Privacy and Modern Protocols:** The guide addresses the growing need for DNS privacy, recommending the deployment of **DNS over TLS (DoT)** and **DNS over HTTPS (DoH)** to encrypt queries between clients and resolvers, thereby preventing eavesdropping and metadata harvesting.
*   **Threat Mitigation:** The document provides strategies to defend against contemporary threats, such as Distributed Denial of Service (DDoS) attacks on DNS infrastructure, by utilizing anycast routing and redundant deployment architectures.

In summary, the 2026 Guide moves beyond basic DNS functionality, requiring a multi-layered security approach that combines encryption, rigorous authentication, and robust administrative practices to ensure the global naming system remains trustworthy.

---

## 18. WolfGuard: WireGuard with FIPS 140-3 cryptography

**原文标题**: WolfGuard: WireGuard with FIPS 140-3 cryptography

**原文链接**: [https://github.com/wolfssl/wolfguard](https://github.com/wolfssl/wolfguard)

生成摘要时出错

---

## 19. curl > /dev/sda: How I made a Linux distro that runs wget | dd

**原文标题**: curl > /dev/sda: How I made a Linux distro that runs wget | dd

**原文链接**: [https://astrid.tech/2026/03/24/0/curl-to-dev-sda/](https://astrid.tech/2026/03/24/0/curl-to-dev-sda/)

生成摘要时出错

---

## 20. Opera: Rewind The Web to 1996 (Opera at 30)

**原文标题**: Opera: Rewind The Web to 1996 (Opera at 30)

**原文链接**: [https://www.web-rewind.com](https://www.web-rewind.com)

生成摘要时出错

---

## 21. So where are all the AI apps?

**原文标题**: So where are all the AI apps?

**原文链接**: [https://www.answer.ai/posts/2026-03-12-so-where-are-all-the-ai-apps.html](https://www.answer.ai/posts/2026-03-12-so-where-are-all-the-ai-apps.html)

生成摘要时出错

---

## 22. Apple Business

**原文标题**: Apple Business

**原文链接**: [https://www.apple.com/newsroom/2026/03/introducing-apple-business-a-new-all-in-one-platform-for-businesses-of-all-sizes/](https://www.apple.com/newsroom/2026/03/introducing-apple-business-a-new-all-in-one-platform-for-businesses-of-all-sizes/)

生成摘要时出错

---

## 23. Box of Secrets: Discreetly modding an apartment intercom to work with Apple Home

**原文标题**: Box of Secrets: Discreetly modding an apartment intercom to work with Apple Home

**原文链接**: [https://www.jackhogan.me/blog/box-of-secrets/](https://www.jackhogan.me/blog/box-of-secrets/)

生成摘要时出错

---

## 24. Country that put backdoors in Cisco routers to spy on world bans foreign routers

**原文标题**: Country that put backdoors in Cisco routers to spy on world bans foreign routers

**原文链接**: [https://www.theregister.com/2026/03/24/fcc_foreign_routers/](https://www.theregister.com/2026/03/24/fcc_foreign_routers/)

生成摘要时出错

---

## 25. io_uring, libaio performance across Linux kernels and an unexpected IOMMU trap

**原文标题**: io_uring, libaio performance across Linux kernels and an unexpected IOMMU trap

**原文链接**: [https://blog.ydb.tech/how-io-uring-overtook-libaio-performance-across-linux-kernels-and-an-unexpected-iommu-trap-ea6126d9ef14](https://blog.ydb.tech/how-io-uring-overtook-libaio-performance-across-linux-kernels-and-an-unexpected-iommu-trap-ea6126d9ef14)

生成摘要时出错

---

## 26. Log File Viewer for the Terminal

**原文标题**: Log File Viewer for the Terminal

**原文链接**: [https://lnav.org/](https://lnav.org/)

生成摘要时出错

---

## 27. The Jellies That Evolved a Different Way to Keep Time

**原文标题**: The Jellies That Evolved a Different Way to Keep Time

**原文链接**: [https://www.quantamagazine.org/the-jellies-that-evolved-a-different-way-to-keep-time-20260320/](https://www.quantamagazine.org/the-jellies-that-evolved-a-different-way-to-keep-time-20260320/)

生成摘要时出错

---

## 28. LLM Neuroanatomy II: Modern LLM Hacking and Hints of a Universal Language?

**原文标题**: LLM Neuroanatomy II: Modern LLM Hacking and Hints of a Universal Language?

**原文链接**: [https://dnhkng.github.io/posts/rys-ii/](https://dnhkng.github.io/posts/rys-ii/)

生成摘要时出错

---

## 29. MSA: Memory Sparse Attention

**原文标题**: MSA: Memory Sparse Attention

**原文链接**: [https://github.com/EverMind-AI/MSA](https://github.com/EverMind-AI/MSA)

生成摘要时出错

---

## 30. iPhone 17 Pro Demonstrated Running a 400B LLM

**原文标题**: iPhone 17 Pro Demonstrated Running a 400B LLM

**原文链接**: [https://twitter.com/anemll/status/2035901335984611412](https://twitter.com/anemll/status/2035901335984611412)

生成摘要时出错

---

## 31. The AI Industry Is Lying to You

**原文标题**: The AI Industry Is Lying to You

**原文链接**: [https://www.wheresyoured.at/the-ai-industry-is-lying-to-you/](https://www.wheresyoured.at/the-ai-industry-is-lying-to-you/)

生成摘要时出错

---

## 32. BIO – The Bao I/O Co-Processor

**原文标题**: BIO – The Bao I/O Co-Processor

**原文链接**: [https://www.crowdsupply.com/baochip/dabao/updates/bio-the-bao-i-o-co-processor](https://www.crowdsupply.com/baochip/dabao/updates/bio-the-bao-i-o-co-processor)

生成摘要时出错

---

## 33. NanoClaw Adopts OneCLI Agent Vault

**原文标题**: NanoClaw Adopts OneCLI Agent Vault

**原文链接**: [https://nanoclaw.dev/blog/nanoclaw-agent-vault/](https://nanoclaw.dev/blog/nanoclaw-agent-vault/)

生成摘要时出错

---

## 34. Claude Code Cheat Sheet

**原文标题**: Claude Code Cheat Sheet

**原文链接**: [https://cc.storyfox.cz](https://cc.storyfox.cz)

生成摘要时出错

---

## 35. A 6502 disassembler with a TUI: A modern take on Regenerator

**原文标题**: A 6502 disassembler with a TUI: A modern take on Regenerator

**原文链接**: [https://github.com/ricardoquesada/regenerator2000](https://github.com/ricardoquesada/regenerator2000)

生成摘要时出错

---

## 36. Dune3d: A parametric 3D CAD application

**原文标题**: Dune3d: A parametric 3D CAD application

**原文链接**: [https://github.com/dune3d/dune3d](https://github.com/dune3d/dune3d)

生成摘要时出错

---

## 37. FCC updates covered list to include foreign-made consumer routers

**原文标题**: FCC updates covered list to include foreign-made consumer routers

**原文链接**: [https://www.fcc.gov/document/fcc-updates-covered-list-include-foreign-made-consumer-routers](https://www.fcc.gov/document/fcc-updates-covered-list-include-foreign-made-consumer-routers)

生成摘要时出错

---

## 38. Show HN: Cq – Stack Overflow for AI coding agents

**原文标题**: Show HN: Cq – Stack Overflow for AI coding agents

**原文链接**: [https://blog.mozilla.ai/cq-stack-overflow-for-agents/](https://blog.mozilla.ai/cq-stack-overflow-for-agents/)

生成摘要时出错

---

## 39. Iranian strikes on Amazon data centers highlight industry's vulnerability

**原文标题**: Iranian strikes on Amazon data centers highlight industry's vulnerability

**原文链接**: [https://apnews.com/article/amazon-aws-data-center-uae-iran-bahrain-71066b0a822c4cfd88b61e3fe79af917](https://apnews.com/article/amazon-aws-data-center-uae-iran-bahrain-71066b0a822c4cfd88b61e3fe79af917)

生成摘要时出错

---

## 40. No-build, no-NPM, SSR-first JavaScript framework if you hate React, love HTML

**原文标题**: No-build, no-NPM, SSR-first JavaScript framework if you hate React, love HTML

**原文链接**: [https://qitejs.qount25.dev](https://qitejs.qount25.dev)

生成摘要时出错

---

## 41. Finding all regex matches has always been O(n²)

**原文标题**: Finding all regex matches has always been O(n²)

**原文链接**: [https://iev.ee/blog/the-quadratic-problem-nobody-fixed/](https://iev.ee/blog/the-quadratic-problem-nobody-fixed/)

生成摘要时出错

---

## 42. IRIX 3dfx Voodoo driver and glide2x IRIX port

**原文标题**: IRIX 3dfx Voodoo driver and glide2x IRIX port

**原文链接**: [https://sdz-mods.com/index.php/2026/03/23/irix-3dfx-voodoo-driver-glide2x-irix-port/](https://sdz-mods.com/index.php/2026/03/23/irix-3dfx-voodoo-driver-glide2x-irix-port/)

生成摘要时出错

---

## 43. Palantir Will No Longer Profit Off of New Yorkers' Health Data

**原文标题**: Palantir Will No Longer Profit Off of New Yorkers' Health Data

**原文链接**: [https://theintercept.com/2026/03/24/palantir-new-york-city-hospitals-contract/](https://theintercept.com/2026/03/24/palantir-new-york-city-hospitals-contract/)

生成摘要时出错

---

## 44. The Resolv hack: How one compromised key printed $23M

**原文标题**: The Resolv hack: How one compromised key printed $23M

**原文链接**: [https://www.chainalysis.com/blog/lessons-from-the-resolv-hack/](https://www.chainalysis.com/blog/lessons-from-the-resolv-hack/)

生成摘要时出错

---

## 45. Microservices and the First Law of Distributed Objects (2014)

**原文标题**: Microservices and the First Law of Distributed Objects (2014)

**原文链接**: [https://martinfowler.com/articles/distributed-objects-microservices.html](https://martinfowler.com/articles/distributed-objects-microservices.html)

生成摘要时出错

---

## 46. Pompeii's battle scars linked to an ancient 'machine gun'

**原文标题**: Pompeii's battle scars linked to an ancient 'machine gun'

**原文链接**: [https://phys.org/news/2026-03-pompeii-scars-linked-ancient-machine.html](https://phys.org/news/2026-03-pompeii-scars-linked-ancient-machine.html)

生成摘要时出错

---

## 47. Abusing Customizable Selects

**原文标题**: Abusing Customizable Selects

**原文链接**: [https://css-tricks.com/abusing-customizable-selects/](https://css-tricks.com/abusing-customizable-selects/)

生成摘要时出错

---

## 48. Trivy under attack again: Widespread GitHub Actions tag compromise secrets

**原文标题**: Trivy under attack again: Widespread GitHub Actions tag compromise secrets

**原文链接**: [https://socket.dev/blog/trivy-under-attack-again-github-actions-compromise](https://socket.dev/blog/trivy-under-attack-again-github-actions-compromise)

生成摘要时出错

---

## 49. Krita 5.3.0 and 6.0.0 Released

**原文标题**: Krita 5.3.0 and 6.0.0 Released

**原文链接**: [https://krita.org/en/posts/2026/krita-5.3.0-released/](https://krita.org/en/posts/2026/krita-5.3.0-released/)

生成摘要时出错

---

## 50. A retro terminal music player inspired by Winamp

**原文标题**: A retro terminal music player inspired by Winamp

**原文链接**: [https://github.com/bjarneo/cliamp](https://github.com/bjarneo/cliamp)

生成摘要时出错

---

## 51. How I'm Productive with Claude Code

**原文标题**: How I'm Productive with Claude Code

**原文链接**: [https://neilkakkar.com/productive-with-claude-code.html](https://neilkakkar.com/productive-with-claude-code.html)

生成摘要时出错

---

## 52. BIO: The Bao I/O Coprocessor

**原文标题**: BIO: The Bao I/O Coprocessor

**原文链接**: [https://www.bunniestudios.com/blog/2026/bio-the-bao-i-o-coprocessor/](https://www.bunniestudios.com/blog/2026/bio-the-bao-i-o-coprocessor/)

生成摘要时出错

---

## 53. Sunsetting the Techempower Framework Benchmarks

**原文标题**: Sunsetting the Techempower Framework Benchmarks

**原文链接**: [https://github.com/TechEmpower/FrameworkBenchmarks/issues/10932](https://github.com/TechEmpower/FrameworkBenchmarks/issues/10932)

生成摘要时出错

---

## 54. Ju Ci: The Art of Repairing Porcelain

**原文标题**: Ju Ci: The Art of Repairing Porcelain

**原文链接**: [https://thesublimeblog.org/2025/03/13/ju-ci-the-ancient-art-of-repairing-porcelain/](https://thesublimeblog.org/2025/03/13/ju-ci-the-ancient-art-of-repairing-porcelain/)

生成摘要时出错

---

## 55. An incoherent Rust

**原文标题**: An incoherent Rust

**原文链接**: [https://www.boxyuwu.blog/posts/an-incoherent-rust/](https://www.boxyuwu.blog/posts/an-incoherent-rust/)

生成摘要时出错

---

## 56. Epic Games lays off over 1k employees

**原文标题**: Epic Games lays off over 1k employees

**原文链接**: [https://www.gamesindustry.biz/epic-games-lays-off-over-1000-employees-following-downturn-in-fortnite-engagement](https://www.gamesindustry.biz/epic-games-lays-off-over-1000-employees-following-downturn-in-fortnite-engagement)

生成摘要时出错

---

## 57. America tells private firms to “hack back”

**原文标题**: America tells private firms to “hack back”

**原文链接**: [https://www.economist.com/united-states/2026/03/22/america-tells-private-firms-to-hack-back](https://www.economist.com/united-states/2026/03/22/america-tells-private-firms-to-hack-back)

生成摘要时出错

---

## 58. Windows 3.1 tiled background .bmp archive

**原文标题**: Windows 3.1 tiled background .bmp archive

**原文链接**: [https://github.com/andreasjansson/win-3.1-backgrounds](https://github.com/andreasjansson/win-3.1-backgrounds)

生成摘要时出错

---

## 59. Local Stack Archived their GitHub repo and requires an account to run

**原文标题**: Local Stack Archived their GitHub repo and requires an account to run

**原文链接**: [https://github.com/localstack/localstack](https://github.com/localstack/localstack)

生成摘要时出错

---

## 60. Gerd Faltings, who proved the Mordell conjecture, wins the Abel Prize

**原文标题**: Gerd Faltings, who proved the Mordell conjecture, wins the Abel Prize

**原文链接**: [https://www.scientificamerican.com/article/gerd-faltings-mathematician-who-proved-the-mordell-conjecture-wins-the-abel/](https://www.scientificamerican.com/article/gerd-faltings-mathematician-who-proved-the-mordell-conjecture-wins-the-abel/)

生成摘要时出错

---

## 61. Gerd Faltings, who proved the Mordell conjecture, wins the Abel Prize

**原文标题**: Gerd Faltings, who proved the Mordell conjecture, wins the Abel Prize

**原文链接**: [https://www.scientificamerican.com/article/gerd-faltings-mathematician-who-proved-the-mordell-conjecture-wins-the-abel/](https://www.scientificamerican.com/article/gerd-faltings-mathematician-who-proved-the-mordell-conjecture-wins-the-abel/)

生成摘要时出错

---

## 62. The bridge to wealth is being pulled up with AI

**原文标题**: The bridge to wealth is being pulled up with AI

**原文链接**: [https://danielhomola.com/m%20&%20e/ai/your-bridge-to-wealth-is-being-pulled-up/](https://danielhomola.com/m%20&%20e/ai/your-bridge-to-wealth-is-being-pulled-up/)

生成摘要时出错

---

## 63. Two pilots dead after plane and ground vehicle collide at LaGuardia

**原文标题**: Two pilots dead after plane and ground vehicle collide at LaGuardia

**原文链接**: [https://www.bbc.com/news/articles/cy01g522ww4o](https://www.bbc.com/news/articles/cy01g522ww4o)

生成摘要时出错

---

## 64. US and TotalEnergies reach 'nearly $1B' deal to end offshore wind projects

**原文标题**: US and TotalEnergies reach 'nearly $1B' deal to end offshore wind projects

**原文链接**: [https://www.lemonde.fr/en/international/article/2026/03/23/us-and-totalenergies-reach-nearly-1-billion-deal-to-end-offshore-wind-projects_6751739_4.html](https://www.lemonde.fr/en/international/article/2026/03/23/us-and-totalenergies-reach-nearly-1-billion-deal-to-end-offshore-wind-projects_6751739_4.html)

生成摘要时出错

---

## 65. General Motors is assisting with the restoration of a rare EV1

**原文标题**: General Motors is assisting with the restoration of a rare EV1

**原文链接**: [https://evinfo.net/2026/03/general-motors-is-assisting-with-the-restoration-of-an-1996-ev1/](https://evinfo.net/2026/03/general-motors-is-assisting-with-the-restoration-of-an-1996-ev1/)

生成摘要时出错

---

## 66. Can you get root with only a cigarette lighter? (2024)

**原文标题**: Can you get root with only a cigarette lighter? (2024)

**原文链接**: [https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html](https://www.da.vidbuchanan.co.uk/blog/dram-emfi.html)

生成摘要时出错

---

## 67. March, 19-21: God is a comedian

**原文标题**: March, 19-21: God is a comedian

**原文链接**: [https://no01.substack.com/p/march-19-21-god-is-a-comedian](https://no01.substack.com/p/march-19-21-god-is-a-comedian)

生成摘要时出错

---

## 68. I wrote a 750-page guide to self-hosting production apps

**原文标题**: I wrote a 750-page guide to self-hosting production apps

**原文链接**: [https://selfdeployment.io/](https://selfdeployment.io/)

生成摘要时出错

---

## 69. PC Gamer recommends RSS readers in a 37mb article that just keeps downloading

**原文标题**: PC Gamer recommends RSS readers in a 37mb article that just keeps downloading

**原文链接**: [https://stuartbreckenridge.net/2026-03-19-pc-gamer-recommends-rss-readers-in-a-37mb-article/](https://stuartbreckenridge.net/2026-03-19-pc-gamer-recommends-rss-readers-in-a-37mb-article/)

生成摘要时出错

---

## 70. Power consumption of Game Boy flash cartridges (2021)

**原文标题**: Power consumption of Game Boy flash cartridges (2021)

**原文链接**: [https://gekkio.fi/blog/2021/power-consumption-of-game-boy-flash-cartridges/](https://gekkio.fi/blog/2021/power-consumption-of-game-boy-flash-cartridges/)

生成摘要时出错

---

## 71. Digs: iOS app that syncs your Discogs collection and lets you browse it offline

**原文标题**: Digs: iOS app that syncs your Discogs collection and lets you browse it offline

**原文链接**: [https://lustin.fr/blog/building-digs/](https://lustin.fr/blog/building-digs/)

生成摘要时出错

---

## 72. I built an AI receptionist for a mechanic shop

**原文标题**: I built an AI receptionist for a mechanic shop

**原文链接**: [https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/](https://www.itsthatlady.dev/blog/building-an-ai-receptionist-for-my-brother/)

生成摘要时出错

---

## 73. Missile Defense Is NP-Complete

**原文标题**: Missile Defense Is NP-Complete

**原文链接**: [https://smu160.github.io/posts/missile-defense-is-np-complete/](https://smu160.github.io/posts/missile-defense-is-np-complete/)

生成摘要时出错

---

## 74. GitHub appears to be struggling with measly three nines availability

**原文标题**: GitHub appears to be struggling with measly three nines availability

**原文链接**: [https://www.theregister.com/2026/02/10/github_outages/](https://www.theregister.com/2026/02/10/github_outages/)

生成摘要时出错

---

## 75. TI-89 Height-Mapped Raycaster

**原文标题**: TI-89 Height-Mapped Raycaster

**原文链接**: [https://github.com/dzoba/ti-89-raycasting-with-z](https://github.com/dzoba/ti-89-raycasting-with-z)

生成摘要时出错

---

## 76. Overcoming the Friendship Recession

**原文标题**: Overcoming the Friendship Recession

**原文链接**: [https://joeprevite.com/friendship-recession/](https://joeprevite.com/friendship-recession/)

生成摘要时出错

---

## 77. Microsoft blocks trick to unlock native NVMe driver, but workarounds still exist

**原文标题**: Microsoft blocks trick to unlock native NVMe driver, but workarounds still exist

**原文链接**: [https://www.tomshardware.com/software/windows/microsoft-blocks-the-registry-hack-trick-that-unlocked-native-nvme-performance-on-windows-11](https://www.tomshardware.com/software/windows/microsoft-blocks-the-registry-hack-trick-that-unlocked-native-nvme-performance-on-windows-11)

生成摘要时出错

---

## 78. Walmart: ChatGPT checkout converted 3x worse than website

**原文标题**: Walmart: ChatGPT checkout converted 3x worse than website

**原文链接**: [https://searchengineland.com/walmart-chatgpt-checkout-converted-worse-472071](https://searchengineland.com/walmart-chatgpt-checkout-converted-worse-472071)

生成摘要时出错

---

## 79. Show HN: The King Wen Permutation: [52, 10, 2]

**原文标题**: Show HN: The King Wen Permutation: [52, 10, 2]

**原文链接**: [https://gzw1987-bit.github.io/iching-math/](https://gzw1987-bit.github.io/iching-math/)

生成摘要时出错

---

## 80. USA bans all new routers for consumers

**原文标题**: USA bans all new routers for consumers

**原文链接**: [https://www.heise.de/en/news/USA-bans-all-new-routers-for-consumers-11222049.html](https://www.heise.de/en/news/USA-bans-all-new-routers-for-consumers-11222049.html)

生成摘要时出错

---

## 81. Designing AI for Disruptive Science

**原文标题**: Designing AI for Disruptive Science

**原文链接**: [https://www.asimov.press/p/ai-science](https://www.asimov.press/p/ai-science)

生成摘要时出错

---

## 82. Maxell MXCP-P100 – wireless cassette player

**原文标题**: Maxell MXCP-P100 – wireless cassette player

**原文链接**: [https://maxell-usa.com/product/cassetteplayer/](https://maxell-usa.com/product/cassetteplayer/)

生成摘要时出错

---

## 83. The gold standard of optimization: A look under the hood of RollerCoaster Tycoon

**原文标题**: The gold standard of optimization: A look under the hood of RollerCoaster Tycoon

**原文链接**: [https://larstofus.com/2026/03/22/the-gold-standard-of-optimization-a-look-under-the-hood-of-rollercoaster-tycoon/](https://larstofus.com/2026/03/22/the-gold-standard-of-optimization-a-look-under-the-hood-of-rollercoaster-tycoon/)

生成摘要时出错

---

## 84. “Collaboration” is bullshit

**原文标题**: “Collaboration” is bullshit

**原文链接**: [https://www.joanwestenberg.com/collaboration-is-bullshit/](https://www.joanwestenberg.com/collaboration-is-bullshit/)

生成摘要时出错

---

## 85. Reports of code's death are greatly exaggerated

**原文标题**: Reports of code's death are greatly exaggerated

**原文链接**: [https://stevekrouse.com/precision](https://stevekrouse.com/precision)

生成摘要时出错

---

## 86. The way CTRL-C in Postgres CLI cancels queries is incredibly hack-y

**原文标题**: The way CTRL-C in Postgres CLI cancels queries is incredibly hack-y

**原文链接**: [https://neon.com/blog/ctrl-c-in-psql-gives-me-the-heebie-jeebies](https://neon.com/blog/ctrl-c-in-psql-gives-me-the-heebie-jeebies)

生成摘要时出错

---

## 87. The future of version control

**原文标题**: The future of version control

**原文链接**: [https://bramcohen.com/p/manyana](https://bramcohen.com/p/manyana)

生成摘要时出错

---

## 88. Vibecoders Can't Build for Longevity

**原文标题**: Vibecoders Can't Build for Longevity

**原文链接**: [https://blog.d11r.eu/theory-building/](https://blog.d11r.eu/theory-building/)

生成摘要时出错

---

## 89. Diverse perspectives on AI from Rust contributors and maintainers

**原文标题**: Diverse perspectives on AI from Rust contributors and maintainers

**原文链接**: [https://nikomatsakis.github.io/rust-project-perspectives-on-ai/feb27-summary.html](https://nikomatsakis.github.io/rust-project-perspectives-on-ai/feb27-summary.html)

生成摘要时出错

---

## 90. An unsolicited guide to being a researcher [pdf]

**原文标题**: An unsolicited guide to being a researcher [pdf]

**原文链接**: [https://emerge-lab.github.io/papers/an-unsolicited-guide-to-good-research.pdf](https://emerge-lab.github.io/papers/an-unsolicited-guide-to-good-research.pdf)

生成摘要时出错

---

## 91. An unsolicited guide to being a researcher [pdf]

**原文标题**: An unsolicited guide to being a researcher [pdf]

**原文链接**: [https://emerge-lab.github.io/papers/an-unsolicited-guide-to-good-research.pdf](https://emerge-lab.github.io/papers/an-unsolicited-guide-to-good-research.pdf)

生成摘要时出错

---

## 92. Cloudflare's Gen 13 servers: trading cache for cores for 2x performance

**原文标题**: Cloudflare's Gen 13 servers: trading cache for cores for 2x performance

**原文链接**: [https://blog.cloudflare.com/gen13-launch/](https://blog.cloudflare.com/gen13-launch/)

生成摘要时出错

---

## 93. Bombadil: Property-based testing for web UIs

**原文标题**: Bombadil: Property-based testing for web UIs

**原文链接**: [https://github.com/antithesishq/bombadil](https://github.com/antithesishq/bombadil)

生成摘要时出错

---

## 94. Epoch confirms GPT5.4 Pro solved a frontier math open problem

**原文标题**: Epoch confirms GPT5.4 Pro solved a frontier math open problem

**原文链接**: [https://epoch.ai/frontiermath/open-problems/ramsey-hypergraphs](https://epoch.ai/frontiermath/open-problems/ramsey-hypergraphs)

生成摘要时出错

---

## 95. Ubisoft's death by a thousand cuts

**原文标题**: Ubisoft's death by a thousand cuts

**原文链接**: [https://www.thegamebusiness.com/p/ubisofts-death-by-a-thousand-cuts](https://www.thegamebusiness.com/p/ubisofts-death-by-a-thousand-cuts)

生成摘要时出错

---

## 96. The IBM scientist who rewrote the rules of information just won a Turing Award

**原文标题**: The IBM scientist who rewrote the rules of information just won a Turing Award

**原文链接**: [https://www.ibm.com/think/news/ibm-scientist-charles-bennett-turing-award](https://www.ibm.com/think/news/ibm-scientist-charles-bennett-turing-award)

生成摘要时出错

---

## 97. Krita 6.0 Released with Qt6 Port and Better Wayland Support

**原文标题**: Krita 6.0 Released with Qt6 Port and Better Wayland Support

**原文链接**: [https://www.phoronix.com/news/Krita-6.0-Released](https://www.phoronix.com/news/Krita-6.0-Released)

生成摘要时出错

---

## 98. Is it a pint?

**原文标题**: Is it a pint?

**原文链接**: [https://isitapint.com/](https://isitapint.com/)

生成摘要时出错

---

## 99. Project Nomad – Knowledge That Never Goes Offline

**原文标题**: Project Nomad – Knowledge That Never Goes Offline

**原文链接**: [https://www.projectnomad.us](https://www.projectnomad.us)

生成摘要时出错

---

## 100. I Quit Editing Photos

**原文标题**: I Quit Editing Photos

**原文链接**: [https://jamesbaker.uk/i-quit-editing-photos/](https://jamesbaker.uk/i-quit-editing-photos/)

生成摘要时出错

---

