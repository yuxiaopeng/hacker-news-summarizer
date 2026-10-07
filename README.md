# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-07.md)

*最后自动更新时间: 2026-10-07 22:19:32*
## 1. Claude Haiku 5.5

**原文标题**: Claude Haiku 5.5

**原文链接**: [https://www.anthropic.com/claude-haiku-5-5](https://www.anthropic.com/claude-haiku-5-5)

Anthropic 推出了 Claude Haiku 5.5，这是其迄今为止速度最快、成本最低且功能最强大的小型模型。Haiku 5.5 专为大规模、成本敏感型任务（如摘要、分类和数据库查询）量身定制，并针对实时客户支持和浏览器操作等对速度要求极高的应用进行了优化。

**核心亮点：**
*   **性能：** Haiku 5.5 的表现显著优于 Haiku 4.5，并可与 GPT-6 Luna 等模型展开强力竞争。它引入了**可调节投入设置 (adjustable effort setting)**，允许用户在计算机操作 (OSWorld) 和专业知识 (GDPval-AA) 等任务中，根据需求灵活平衡成本与智能水平。
*   **成本效益：** 该模型的运行成本比 Haiku 4.5 降低了约 75%。对于 10 万 token 以下的提示词，其定价为每百万输入 token 0.10 美元，每百万输出 token 0.50 美元。
*   **生态系统更新：** Anthropic 将 **Claude Sonnet 5.5 缓存读取**的价格减半至每百万 token 0.10 美元，使代理化工作 (agentic work) 的成本降低了约 20%。此外，Max 和 Team 订阅用户现在每月将获得 100 至 500 美元不等的 API 额度，以支持平台开发。
*   **安全性与可用性：** 该模型具备更强的对齐性、更严格的网络安全防护以及经过改进的生物安全保护。它已在 Claude 平台、AWS、Google Cloud 和 Microsoft Azure 上同步上线。

Haiku 5.5 非常适合作为 Opus 5.5 和 Sonnet 5.5 等大型模型的子代理，为多步工作流提供低延迟、更迅捷的体验。更新后的 Python 和 TypeScript SDK 现已支持其处于 Beta 测试阶段的计算机与浏览器使用功能。

---

## 2. GPT-6 与全民智能 UI

**原文标题**: GPT‑6 and Intelligent UI for everyone

**原文链接**: [https://openai.com/index/gpt-6-for-everyone/](https://openai.com/index/gpt-6-for-everyone/)

2026年10月7日，OpenAI 宣布在全球范围内推出 **GPT-6**，为其 12 亿周活跃用户引入了一项名为“**智能界面 (Intelligent UI)**”的变革性功能。此次更新标志着从静态文本回复向动态交互体验的转变，使软件能够根据用户的需求进行自适应。

**核心功能与进展：**

*   **智能界面：** ChatGPT 现在可以使用交互式组件库来构建回复。根据查询需求，它可以生成自定义工具（如计算器或账单分摊器）、交互式图表、地图和可点击的图形，让用户能够直观地探索复杂话题。
*   **更快的性能：** GPT-6 引入了“交织思维 (interleaved thinking)”，使模型在持续进行复杂推理的同时即可开始输出回答。这显著缩短了等待时间；例如，GPT-6 启动基于网页搜索的回答速度比 GPT-5.6 快 44%。
*   **模型分级：** 此次发布包括两个针对日常对话优化的主要模型：面向付费层级（Plus、Pro、团队版和企业版）的 **GPT-6 Sol**，以及面向免费版和入门版 (Go) 的 **GPT-6 Luna**。
*   **安全与可靠性：** 基于“Astra”安全协议，GPT-6 增强了抵御对抗性攻击的能力，并能更好地识别高风险场景（如网络和生物威胁）。它也变得更加“诚实”，对自身的局限性有更清晰的认知。

**愿景：**

OpenAI 将此次发布视为迈向通用人工智能 (AGI) 的里程碑。通过摆脱用户必须学习操作的固定界面，GPT-6 旨在创造一个软件能够围绕当前任务动态塑造自身的未来，使技术对每个人都更加直观且易于使用。

---

## 3. Docker 代理

**原文标题**: Docker Agent

**原文链接**: [https://github.com/docker/docker-agent](https://github.com/docker/docker-agent)

**Docker Agent** 是一款 CLI 插件，旨在通过声明式的 YAML 配置来构建、运行和编排 AI 智能体。它允许用户创建智能的多智能体系统，无需手动编码即可协作完成复杂任务。

**核心特性：**
*   **多智能体编排：** 用户可以定义专门的智能体，实现任务在不同智能体之间的自动委派。
*   **模型无关：** 支持广泛的模型提供商，包括 OpenAI、Anthropic、Gemini、AWS Bedrock，以及通过 Docker Model Runner 运行的本地模型。
*   **工具与 RAG 集成：** 该平台拥有丰富的生态系统，利用模型上下文协议 (MCP) 集成工具。它还内置了支持混合搜索和重排序的 RAG（检索增强生成）功能。
*   **便携性：** 智能体被封装为符合 OCI 标准的镜像，便于进行版本管理和共享，并能使用标准 Docker 命令在任何环境中运行。

**安装与使用：**
该插件预装在 **Docker Desktop (4.63+)** 中，也可通过 Homebrew 或直接下载二进制文件获取。设置 API 密钥后，用户可以使用 `docker agent run` 启动智能体，通过 `docker agent new` 交互式地创建新智能体，或通过 YAML 文件执行自定义配置。

通过利用 Docker 在容器领域的专业技术积累，Docker Agent 简化了复杂 AI 工作流的部署，为管理智能体生命周期和工具集成提供了一种标准化的方式。

---

## 4. 提升 if，下沉 for：该惯用法、其代数及其局限性

**原文标题**: Push ifs up and fors down: The idiom, its algebra, and its limits

**原文链接**: [https://debasishg.github.io/blog/push-ifs-up-fors-down/](https://debasishg.github.io/blog/push-ifs-up-fors-down/)

本文探讨了“if 向上推，for 向下压”这一编程启发式准则，该原则旨在集中控制流并优化性能。

**if 向上推**涉及将条件逻辑（分支）从函数移至其调用者。这缩小了函数的输入状态空间（在范畴论中表示为子对象），确保函数仅接收有效数据。例如，将处理 `Option<Walrus>` 的函数替换为接收确定的 `Walrus` 对象的函数，可以明确前置条件并简化被调用方的逻辑。

**for 向下压**建议将循环移入助手函数以实现批处理。这减少了每次调用的开销，并使内部循环保持“轻量分支”，从而使其具备硬件向量化的潜力。

作者强调了该原则适用的三个主要领域：
*   **数据库查询优化**：优化器“下压”选择和投影操作以尽早过滤数据，同时“上推”（延迟）昂贵的连接操作。这确保了沉重的计算仅在最小的必要数据集上进行。
*   **函数式编程**：该原则植根于代数定律：`filter p . map f == map f . filter (p . f)`。当在输入上评估谓词 `p` 比在变换 `f` 之后评估更廉价时，这种重写最为有效。
*   **范畴论**：将“if”向上推被视为从余积（例如 `Sum` 类型）中提取出函数因子。它将处理不同情况的责任转移给调用者，使核心逻辑保持为特定子对象上的简单态射。

**结论**：虽然这些重写改进了系统结构，但它们受到代数约束的限制。只有当条件是循环不变式时，“if”才能被移动；而“for”向下移动主要是为了通过从逐元素处理转向面向批处理的“箭头（arrows）”来优化执行成本。

---

## 5. Show HN: Bigwords.page – Turn any screen into a sign. The URL is the app

**原文标题**: Show HN: Bigwords.page – Turn any screen into a sign. The URL is the app

**原文链接**: [https://bigwords.page/](https://bigwords.page/)

生成摘要时出错

---

## 6. Despite what Watson said, Rosalind Franklin understood structure of DNA first

**原文标题**: Despite what Watson said, Rosalind Franklin understood structure of DNA first

**原文链接**: [https://link.springer.com/article/10.1007/s10739-026-09866-7](https://link.springer.com/article/10.1007/s10739-026-09866-7)

生成摘要时出错

---

## 7. Shipping JPEG XL in Chrome

**原文标题**: Shipping JPEG XL in Chrome

**原文链接**: [https://developer.chrome.com/blog/jpeg-xl-in-chrome](https://developer.chrome.com/blog/jpeg-xl-in-chrome)

生成摘要时出错

---

## 8. Meta and Microsoft take steps to reduce employee usage of Claude AI

**原文标题**: Meta and Microsoft take steps to reduce employee usage of Claude AI

**原文链接**: [https://www.rswebsols.com/news/meta-and-microsoft-take-steps-to-reduce-employee-usage-of-claude-ai/](https://www.rswebsols.com/news/meta-and-microsoft-take-steps-to-reduce-employee-usage-of-claude-ai/)

生成摘要时出错

---

## 9. The Mathocalypse

**原文标题**: The Mathocalypse

**原文链接**: [https://scottaaronson.blog/?p=10169](https://scottaaronson.blog/?p=10169)

生成摘要时出错

---

## 10. Animated ASCII Art for Web Pages

**原文标题**: Animated ASCII Art for Web Pages

**原文链接**: [https://ascii.rest/](https://ascii.rest/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 2 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 3 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 4 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 5 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 6 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 7 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 8 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 9 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 10 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 11 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 12 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 13 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 14 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 15 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 16 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 17 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 18 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 19 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 20 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 21 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 22 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 23 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 24 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 25 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 26 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 27 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 28 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 29 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 30 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 31 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 32 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 33 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 34 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 35 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 36 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 37 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 38 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 39 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 40 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 41 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 42 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 43 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 44 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 45 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 46 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 47 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 48 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 49 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 50 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 51 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 52 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 53 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 54 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 55 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 56 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 57 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 58 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 59 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 60 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 61 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 62 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 63 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 64 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 65 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 66 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 67 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 68 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 69 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 70 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 71 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 72 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 73 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 74 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 75 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 76 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 77 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 78 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 79 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 80 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 81 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 82 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 83 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 84 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 85 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 86 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 87 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 88 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 89 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 90 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 91 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 92 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 93 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 94 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 95 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 96 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 97 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 98 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 99 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 100 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 101 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 102 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 103 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 104 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 105 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 106 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 107 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 108 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 109 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 110 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 111 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 112 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 113 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 114 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 115 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 116 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 117 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 118 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 119 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 120 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 121 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 122 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 123 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 124 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 125 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 126 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 127 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 128 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 129 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 130 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 131 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 132 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 133 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 134 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 135 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 136 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 137 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 138 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 139 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 140 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 141 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 142 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 143 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 144 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 145 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 146 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 147 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 148 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 149 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 150 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 151 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 152 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 153 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 154 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 155 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 156 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 157 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 158 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 159 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 160 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 161 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 162 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 163 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 164 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 165 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 166 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 167 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 168 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 169 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 170 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 171 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 172 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 173 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 174 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 175 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 176 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 177 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 178 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 179 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 180 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 181 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 182 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 183 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 184 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 185 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 186 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 187 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 188 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 189 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 190 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 191 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 192 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 193 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 194 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 195 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 196 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 197 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 198 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 199 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 200 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 201 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 202 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 203 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 204 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 205 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 206 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 207 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 208 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 209 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 210 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 211 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 212 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 213 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 214 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 215 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 216 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 217 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 218 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 219 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 220 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 221 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 222 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 223 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 224 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 225 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 226 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 227 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 228 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 229 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 230 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 231 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 232 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 233 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 234 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 235 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 236 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 237 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 238 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 239 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 240 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 241 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 242 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 243 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 244 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 245 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 246 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 247 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 248 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 249 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 250 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 251 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 252 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 253 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 254 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 255 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 256 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 257 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 258 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 259 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 260 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 261 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 262 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 263 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 264 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 265 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 266 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 267 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 268 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 269 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 270 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 271 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 272 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 273 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 274 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 275 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 276 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 277 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 278 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 279 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 280 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 281 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 282 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 283 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 284 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 285 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 286 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 287 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 288 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 289 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 290 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 291 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 292 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 293 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 294 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 295 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 296 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 297 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 298 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 299 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 300 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 301 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 302 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 303 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 304 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 305 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 306 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 307 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 308 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 309 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 310 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 311 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 312 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 313 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 314 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 315 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 316 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 317 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 318 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 319 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 320 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 321 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 322 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 323 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 324 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 325 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 326 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 327 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 328 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 329 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 330 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 331 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 332 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 333 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 334 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 335 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 336 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 337 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 338 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 339 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 340 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 341 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 342 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 343 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 344 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 345 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 346 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 347 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 348 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 349 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 350 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 351 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 352 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 353 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 354 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 355 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 356 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 357 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 358 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 359 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 360 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 361 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 362 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 363 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 364 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 365 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 366 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 367 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 368 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 369 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 370 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 371 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 372 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 373 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 374 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 375 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 376 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 377 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 378 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 379 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 380 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 381 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 382 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 383 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 384 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 385 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 386 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 387 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 388 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 389 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 390 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 391 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 392 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 393 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 394 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 395 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 396 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 397 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 398 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 399 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 400 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 401 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 402 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 403 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 404 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 405 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 406 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 407 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 408 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 409 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 410 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 411 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 412 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 413 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 414 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 415 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 416 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 417 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 418 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 419 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 420 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 421 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 422 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 423 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 424 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 425 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 426 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 427 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 428 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 429 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 430 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 431 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 432 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 433 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 434 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 435 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 436 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 437 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 438 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 439 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 440 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 441 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 442 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 443 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 444 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 445 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 446 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 447 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 448 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 449 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 450 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 451 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 452 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 453 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 454 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 455 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 456 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 457 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 458 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 459 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 460 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 461 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 462 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 463 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 464 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 465 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 466 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 467 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 468 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 469 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 470 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 471 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 472 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 473 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 474 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 475 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 476 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 477 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 478 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 479 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 480 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 481 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 482 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 483 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 484 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 485 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 486 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 487 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 488 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 489 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 490 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 491 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 492 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 493 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 494 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 495 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 496 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 497 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 498 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 499 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 500 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 501 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 502 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 503 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 504 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 505 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 506 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 507 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 508 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 509 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 510 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 511 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 512 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 513 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 514 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 515 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 516 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 517 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 518 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 519 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 520 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 521 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 522 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 523 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 524 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 525 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 526 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 527 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 528 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 529 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 530 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 531 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 532 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 533 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 534 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 535 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 536 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 537 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 538 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 539 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 540 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 541 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 542 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 543 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 544 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 545 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 546 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 547 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 548 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 549 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 550 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 551 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 552 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 553 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 554 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 555 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 556 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 557 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 558 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 559 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 560 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 561 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 562 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 563 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 564 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
