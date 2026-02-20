# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-20.md)

*最后自动更新时间: 2026-02-20 18:11:49*
## 1. Ggml.ai 加入 Hugging Face，以确保本地 AI 的长期发展。

**原文标题**: Ggml.ai joins Hugging Face to ensure the long-term progress of Local AI

**原文链接**: [https://github.com/ggml-org/llama.cpp/discussions/19759](https://github.com/ggml-org/llama.cpp/discussions/19759)

2026年2月20日，影响力深远的 `llama.cpp` 库背后的创始团队 **ggml.ai** 负责人 Georgi Gerganov 宣布，该团队已加入 **Hugging Face**。此次合作旨在确保“本地 AI”生态系统的长期可持续性与增长。

**此次转型的关键细节包括：**
*   **持续性与开源：** ggml-org 项目将保持 100% 开源并由社区驱动。Gerganov 及其团队将继续全职领导并维护 `ggml` 和 `llama.cpp`，社区将保留技术自主权。
*   **增强资源：** Hugging Face 将提供扩展项目所需的必要资源，确保其始终是消费级硬件上高效本地推理的权威标准。
*   **技术集成：** 未来将致力于实现 Hugging Face `transformers` 库与 ggml 生态系统之间的“一键式”集成。这旨在提升模型支持能力、加强质量控制，并缩短新模型量化版本的发布周期。
*   **用户体验：** 此次合作旨在简化本地模型部署，使其成为普通用户眼中相比云端推理更具竞争力和易于获取的选择。

此举使双方长期的合作关系正式化。此前，Hugging Face 的工程师已为该项目贡献了核心功能、多模态支持，并提升了对 GGUF 文件格式的兼容性。

**长期愿景：**
共同的目标是构建一个足够高效、能在个人设备上运行的终极推理技术栈，最终让“开源超级智能”惠及每个人。社区对此反响热烈，贡献者们普遍认为 Hugging Face 是该项目持续演进的理想归宿。

---

## 2. 我在泄露的 CIA 开发者文档中发现了一个实用的 Git 一行命令

**原文标题**: I found a useful Git one liner buried in leaked CIA developer docs

**原文链接**: [https://spencer.wtf/2026/02/20/cleaning-up-merged-git-branches-a-one-liner-from-the-cias-leaked-dev-docs.html](https://spencer.wtf/2026/02/20/cleaning-up-merged-git-branches-a-one-liner-from-the-cias-leaked-dev-docs.html)

本文介绍了一个实用的 Git 命令，该命令源自 2017 年维基解密发布的“Vault7”中泄露的 CIA 内部开发文档。在众多高级黑客工具中，作者发现了一个虽简单却极其实用的单行命令，用于解决本地仓库分支杂乱的问题。

**问题**
随着时间的推移，本地仓库会堆积大量“陈旧”的分支。这些已完成并合并的功能或修复分支仍保留在列表中，形成了一个分支“墓地”。

**解决方案**
CIA 文档建议使用一条命令来自动化清理这些分支。其逻辑分为三步：
1. **列出：** 识别所有已合并到当前分支的分支。
2. **过滤：** 使用 `grep` 排除当前正在使用的分支（`*`）和主分支（如 `master` 或 `main`）。
3. **删除：** 使用 `xargs` 将剩余的分支名称传递给 `git branch -d` 进行安全删除。

**现代版本**
为了适应现代命名规范及 `develop` 等常见持久分支，作者提供了一个更新版本：

`git branch --merged origin/main | grep -vE "^\s*(\*|main|develop)" | xargs -n 1 git branch -d`

通过将此命令保存为 Shell 别名（例如 `ciaclean`），开发人员可以快速修剪本地分支列表，保持工作区整洁，从而提高日常工作效率。

---

## 3. 儿戏：科技新一代与思考的终结

**原文标题**: Child's Play: Tech's new generation and the end of thinking

**原文链接**: [https://harpers.org/archive/2026/03/childs-play-sam-kriss-ai-startup-roy-lee/](https://harpers.org/archive/2026/03/childs-play-sam-kriss-ai-startup-roy-lee/)

在《孩童游戏》（Child’s Play）中，萨姆·克里斯（Sam Kriss）探讨了旧金山令人不安的转型，以及以罗伊·李（Roy Lee）及其初创公司 Cluely 为代表的新兴技术特权阶级的崛起。

克里斯描绘了一座被“普遍的无意识”定义的城市，在这里，铺天盖地的 AI 服务 B2B 广告与街道上流浪者和心理健康危机的现实形成了鲜明对比。在这种环境下，Cluely 已成为业内最令人厌恶的初创公司。Cluely 最初被设计为帮助求职者在技术面试中作弊的工具，现在则被推广为面向“普通办公室工蜂”的实时 AI 助手，在 Zoom 会议甚至社交约会中为用户提供答案。

文章强调了硅谷哲学的根本性转变：该行业正从基于智力和推理（这些特质如今极易被 AI 复制）的精英管理制度，转向一场“分化事件”。这种分化将“无用的”底层阶级与由“能动性”（agency）定义的超强特权阶级隔离开来。这些具有“能动性”的个体，其特征不在于思考或创造的能力，而在于其强烈的行动欲望，以及利用机器替代自己思考的手段。

曾因使用 AI 作弊而被哥伦比亚大学停学的李，正是这一新原型的化身。他的办公室文化是“兄弟会”派头、病毒视频创作与极简主义痴迷的怪异结合。尽管产品故障频发，李依然维持着一种“零延迟”的人设，以机器般的直接方式行事。最终，克里斯描绘了一幅惨淡的未来图景：人类的洞察力被“杠杆”所取代，人变得不过是接收 AI 生成指令的肉身接口，预示着一场自愿的“思考的终结”。

---

## 4. 通往无处不在的 AI 之路 (1.7万 token/秒)

**原文标题**: The path to ubiquitous AI (17k tokens/sec)

**原文链接**: [https://taalas.com/the-path-to-ubiquitous-ai/](https://taalas.com/the-path-to-ubiquitous-ai/)

在《通往普及人工智能之路》一文中，Taalas 创始人 Ljubisa Bajic 指出，当前依赖庞大且耗能的数据中心的 AI 发展路径是不可持续的，这类似于计算机史上的“怪异原型”ENIAC。要实现广泛普及，AI 必须克服两大核心障碍：高延迟和极高的成本。

Taalas 提议从通用 GPU 转向**完全专用化**。他们的平台能在短短两个月内将特定的 AI 模型转化为定制芯片（即“硬件化模型”）。其核心创新在于以 DRAM 级别的密度在单颗芯片上融合存储与计算。通过消除内存与处理器之间的传统界限，Taalas 摆脱了对 HBM、先进封装和液冷等昂贵组件的需求。

该公司首款产品——硬接线版 **Llama 3.1 8B**（运行在其 HC1 芯片上）展示了这一方案的成效：
*   **性能**：单用户每秒 17,000 个 token（比目前领先水平快近 10 倍）。
*   **效率**：制造成本降低 20 倍，功耗降低 10 倍。
*   **灵活性**：尽管采用硬接线设计，但仍支持通过低秩自适应（LoRA）进行微调。

Taalas 拥有一支 24 人的精干团队，强调严谨的工程设计，而非业内常见的“暴力”高资本投入模式。继 Llama 3.1 8B 之后，该公司计划于春季推出中型推理模型，并于冬季在第二代（HC2）芯片上发布前沿大语言模型。通过提供亚毫秒级延迟和近乎零的成本，Taalas 旨在开启此前因技术限制而无法实现的智能体及交互式 AI 应用新领域。

---

## 5. 美国最高法院推翻特朗普全球关税计划。

**原文标题**: Trump's global tariffs struck down by US Supreme Court

**原文链接**: [https://www.bbc.com/news/live/c0l9r67drg7t](https://www.bbc.com/news/live/c0l9r67drg7t)

美国最高法院推翻了特朗普总统的全球关税政策，引发了白宫立即且罕见的回应。现场记者 Bernd Debusmann Jr 描述了原本宁静的早晨如何因记者们争相参加一场突如其来的总统简报会而瞬间变成“忙碌的中心”。

此次裁决的重要性通过简报会的罕见程度得以体现：这是特朗普重返总统职位以来第二次举行临时简报会，上一次是在一年多前发生一起航空事故之后。政府决定紧急面对媒体，凸显了该司法裁决的严重性及其对白宫经济议程的影响。

---

## 6. 学习代码库的未发掘途径：构建可视化工具

**原文标题**: Untapped Way to Learn a Codebase: Build a Visualizer

**原文链接**: [https://jimmyhmiller.com/learn-codebase-visualizer](https://jimmyhmiller.com/learn-codebase-visualizer)

在《学习代码库的另类途径：构建可视化工具》一文中，Jimmy Miller 认为，理解庞大且陌生的代码库最有效的方法是主动交互，而非被动阅读。他提议将构建可视化工具作为核心策略，并辅以设定明确目标、调查真实 Bug 报告以及进行实验性“随机”修改以观察系统反应等技巧。

Miller 以 Next.js 基于 Rust 的打包工具 Turbopack 为案例，展示了如何通过忽略“主”入口点并追踪特定路径（本例中为一个导致死代码未被移除的 Tree-shaking Bug）来缩小关注范围。他强调了“支线任务”的普遍性，即在探索过程中出现的意外技术障碍。例如，在调查该 Bug 之前，他必须先调试并修复 Next.js 构建系统中一个导致原生依赖项无法正确加载的错误正则表达式。

在追踪代码从 TypeScript AST（通过 SWC）转换为 JavaScript “分块”（chunks）的过程中，Miller 指出了在高性能、异步 Rust 环境中穿行的难度。他强调，这一过程的目标未必是修复 Bug 或精通整个代码仓库，而是要将代码库从一个“黑盒”转变为理解其内部机制的透明体，从而能够提出正确的问题。最终，通过构建工具来可视化系统中的数据流，可以揭示出仅凭文档和阅读无法获取的架构洞察。

---

## 7. Legion Health (YC) Is Hiring Cracked SWEs for Autonomous Mental Health

**原文标题**: Legion Health (YC) Is Hiring Cracked SWEs for Autonomous Mental Health

**原文链接**: [https://jobs.ashbyhq.com/legionhealth/ffdd2b52-eb21-489e-b124-3c0804231424](https://jobs.ashbyhq.com/legionhealth/ffdd2b52-eb21-489e-b124-3c0804231424)

**Legion Health**, a Y Combinator-backed health-tech startup, is currently recruiting for a **Founding Engineer** to help build its AI-native mental health care platform. The company is specifically seeking high-performing software engineers (described as "cracked SWEs") to develop autonomous mental health solutions.

**Key Highlights:**
*   **Market Position:** Legion Health identifies as an "AI-native" mental health provider.
*   **Financial Success:** The company has demonstrated significant traction with over **$3.3 million in Annual Recurring Revenue (ARR)**.
*   **Funding:** To date, they have raised more than **$7 million** in capital.
*   **Role Focus:** As a Founding Engineer, the hire will be instrumental in scaling the technology behind their autonomous care model.

This recruitment drive signals a period of high growth for the company as they leverage their venture backing and established revenue to disrupt the mental health space using artificial intelligence.

---

## 8. PayPal discloses data breach that exposed user info for 6 months

**原文标题**: PayPal discloses data breach that exposed user info for 6 months

**原文链接**: [https://www.bleepingcomputer.com/news/security/paypal-discloses-data-breach-exposing-users-personal-information/](https://www.bleepingcomputer.com/news/security/paypal-discloses-data-breach-exposing-users-personal-information/)

生成摘要时出错

---

## 9. Web Components: The Framework-Free Renaissance

**原文标题**: Web Components: The Framework-Free Renaissance

**原文链接**: [https://www.caimito.net/en/blog/2026/02/17/web-components-the-framework-free-renaissance.html](https://www.caimito.net/en/blog/2026/02/17/web-components-the-framework-free-renaissance.html)

In "Web Components: The Framework-Free Renaissance," Stephan Schwab argues that modern browser evolution has rendered heavy JavaScript frameworks like React, Vue, and Angular increasingly optional. By leveraging native web standards—specifically **Custom Elements, Shadow DOM, and the native event system**—developers can build sophisticated, modular UIs without the "framework tax" of heavy bundles and constant version churn.

The article highlights several key advantages of this standards-based approach:

*   **Longevity and Stability:** Unlike frameworks that require frequent, breaking upgrades, web standards are built for long-term backward compatibility. Code written to these standards today is likely to function for decades.
*   **Built-in Communication:** The DOM acts as a natural event bus. Using a "data down, events up" pattern, components communicate via attributes and properties for inputs and custom bubbling events for outputs, eliminating the need for complex state management libraries.
*   **True Encapsulation:** Shadow DOM provides genuine CSS and DOM isolation, ensuring styles do not leak and preventing global conflicts—a problem frameworks often solve with additional layers of abstraction.
*   **AI-Enhanced Learning:** Schwab notes that AI assistants have lowered the barrier to entry, allowing developers to experiment with native specifications and master complex lifecycle callbacks through real-time, contextual pair programming.

While acknowledging that frameworks still hold value for teams with established expertise, the author suggests a hybrid or incremental transition. Ultimately, the "renaissance" lies in rediscovering the power of the web platform itself to create maintainable, interoperable, and lightweight applications that are built to last.

---

## 10. No Skill. No Taste

**原文标题**: No Skill. No Taste

**原文链接**: [https://blog.kinglycrow.com/no-skill-no-taste/](https://blog.kinglycrow.com/no-skill-no-taste/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 2 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 3 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 4 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 5 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 6 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 7 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 8 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 9 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 10 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 11 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 12 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 13 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 14 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 15 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 16 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 17 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 18 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 19 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 20 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 21 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 22 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 23 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 24 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 25 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 26 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 27 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 28 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 29 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 30 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 31 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 32 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 33 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 34 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 35 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 36 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 37 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 38 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 39 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 40 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 41 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 42 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 43 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 44 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 45 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 46 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 47 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 48 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 49 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 50 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 51 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 52 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 53 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 54 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 55 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 56 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 57 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 58 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 59 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 60 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 61 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 62 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 63 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 64 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 65 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 66 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 67 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 68 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 69 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 70 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 71 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 72 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 73 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 74 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 75 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 76 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 77 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 78 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 79 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 80 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 81 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 82 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 83 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 84 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 85 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 86 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 87 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 88 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 89 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 90 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 91 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 92 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 93 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 94 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 95 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 96 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 97 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 98 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 99 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 100 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 101 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 102 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 103 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 104 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 105 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 106 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 107 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 108 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 109 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 110 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 111 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 112 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 113 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 114 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 115 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 116 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 117 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 118 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 119 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 120 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 121 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 122 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 123 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 124 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 125 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 126 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 127 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 128 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 129 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 130 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 131 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 132 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 133 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 134 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 135 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 136 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 137 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 138 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 139 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 140 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 141 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 142 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 143 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 144 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 145 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 146 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 147 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 148 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 149 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 150 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 151 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 152 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 153 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 154 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 155 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 156 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 157 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 158 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 159 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 160 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 161 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 162 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 163 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 164 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 165 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 166 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 167 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 168 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 169 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 170 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 171 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 172 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 173 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 174 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 175 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 176 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 177 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 178 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 179 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 180 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 181 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 182 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 183 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 184 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 185 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 186 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 187 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 188 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 189 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 190 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 191 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 192 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 193 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 194 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 195 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 196 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 197 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 198 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 199 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 200 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 201 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 202 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 203 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 204 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 205 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 206 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 207 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 208 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 209 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 210 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 211 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 212 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 213 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 214 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 215 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 216 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 217 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 218 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 219 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 220 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 221 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 222 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 223 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 224 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 225 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 226 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 227 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 228 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 229 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 230 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 231 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 232 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 233 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 234 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 235 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 236 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 237 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 238 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 239 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 240 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 241 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 242 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 243 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 244 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 245 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 246 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 247 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 248 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 249 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 250 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 251 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 252 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 253 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 254 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 255 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 256 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 257 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 258 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 259 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 260 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 261 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 262 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 263 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 264 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 265 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 266 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 267 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 268 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 269 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 270 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 271 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 272 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 273 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 274 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 275 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 276 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 277 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 278 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 279 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 280 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 281 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 282 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 283 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 284 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 285 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 286 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 287 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 288 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 289 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 290 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 291 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 292 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 293 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 294 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 295 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 296 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 297 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 298 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 299 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 300 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 301 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 302 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 303 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 304 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 305 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 306 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 307 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 308 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 309 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 310 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 311 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 312 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 313 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 314 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 315 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 316 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 317 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 318 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 319 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 320 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 321 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 322 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 323 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 324 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 325 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 326 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 327 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 328 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 329 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 330 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 331 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 332 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 333 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 334 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 335 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 336 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 337 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
