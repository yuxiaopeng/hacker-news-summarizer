# Hacker News 热门文章摘要 (2026-02-20)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Minions – Stripe's Coding Agents Part 2

**原文标题**: Minions – Stripe's Coding Agents Part 2

**原文链接**: [https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2)

生成摘要时出错

---

## 12. Show HN: A native macOS client for Hacker News, built with SwiftUI

**原文标题**: Show HN: A native macOS client for Hacker News, built with SwiftUI

**原文链接**: [https://github.com/IronsideXXVI/Hacker-News](https://github.com/IronsideXXVI/Hacker-News)

生成摘要时出错

---

## 13. The Popper Principle

**原文标题**: The Popper Principle

**原文链接**: [https://theamericanscholar.org/the-popper-principle/](https://theamericanscholar.org/the-popper-principle/)

生成摘要时出错

---

## 14. The Rediscovery of 103 Hokusai Lost Sketches (2021)

**原文标题**: The Rediscovery of 103 Hokusai Lost Sketches (2021)

**原文链接**: [https://japan-forward.com/eternal-hokusai-the-rediscovery-of-103-hokusai-lost-sketches/](https://japan-forward.com/eternal-hokusai-the-rediscovery-of-103-hokusai-lost-sketches/)

生成摘要时出错

---

## 15. Visible Spectra of the Elements

**原文标题**: Visible Spectra of the Elements

**原文链接**: [https://atomic-spectra.net/](https://atomic-spectra.net/)

生成摘要时出错

---

## 16. Consistency diffusion language models: Up to 14x faster, no quality loss

**原文标题**: Consistency diffusion language models: Up to 14x faster, no quality loss

**原文链接**: [https://www.together.ai/blog/consistency-diffusion-language-models](https://www.together.ai/blog/consistency-diffusion-language-models)

生成摘要时出错

---

## 17. Raspberry Pi Pico 2 at 873.5MHz with 3.05V Core Abuse

**原文标题**: Raspberry Pi Pico 2 at 873.5MHz with 3.05V Core Abuse

**原文链接**: [https://learn.pimoroni.com/article/overclocking-the-pico-2](https://learn.pimoroni.com/article/overclocking-the-pico-2)

生成摘要时出错

---

## 18. AI is not a coworker, it's an exoskeleton

**原文标题**: AI is not a coworker, it's an exoskeleton

**原文链接**: [https://www.kasava.dev/blog/ai-as-exoskeleton](https://www.kasava.dev/blog/ai-as-exoskeleton)

生成摘要时出错

---

## 19. Infrastructure decisions I endorse or regret after 4 years at a startup (2024)

**原文标题**: Infrastructure decisions I endorse or regret after 4 years at a startup (2024)

**原文链接**: [https://cep.dev/posts/every-infrastructure-decision-i-endorse-or-regret-after-4-years-running-infrastructure-at-a-startup/](https://cep.dev/posts/every-infrastructure-decision-i-endorse-or-regret-after-4-years-running-infrastructure-at-a-startup/)

生成摘要时出错

---

## 20. Lessons learned from `oapi-codegen`'s time in the GitHub Secure Open Source Fund

**原文标题**: Lessons learned from `oapi-codegen`'s time in the GitHub Secure Open Source Fund

**原文链接**: [https://www.jvt.me/posts/2026/02/17/oapi-codegen-github-secure/](https://www.jvt.me/posts/2026/02/17/oapi-codegen-github-secure/)

生成摘要时出错

---

## 21. Notes on Clarifying Man Pages

**原文标题**: Notes on Clarifying Man Pages

**原文链接**: [https://jvns.ca/blog/2026/02/18/man-pages/](https://jvns.ca/blog/2026/02/18/man-pages/)

生成摘要时出错

---

## 22. Reading the undocumented MEMS accelerometer on Apple Silicon MacBooks via iokit

**原文标题**: Reading the undocumented MEMS accelerometer on Apple Silicon MacBooks via iokit

**原文链接**: [https://github.com/olvvier/apple-silicon-accelerometer](https://github.com/olvvier/apple-silicon-accelerometer)

生成摘要时出错

---

## 23. US plans online portal to bypass content bans in Europe and elsewhere

**原文标题**: US plans online portal to bypass content bans in Europe and elsewhere

**原文链接**: [https://www.reuters.com/world/us-plans-online-portal-bypass-content-bans-europe-elsewhere-2026-02-18/](https://www.reuters.com/world/us-plans-online-portal-bypass-content-bans-europe-elsewhere-2026-02-18/)

生成摘要时出错

---

## 24. Show HN: Micasa – track your house from the terminal

**原文标题**: Show HN: Micasa – track your house from the terminal

**原文链接**: [https://micasa.dev](https://micasa.dev)

生成摘要时出错

---

## 25. FreeCAD

**原文标题**: FreeCAD

**原文链接**: [https://www.freecad.org/index.php](https://www.freecad.org/index.php)

生成摘要时出错

---

## 26. A beginner's guide to split keyboards

**原文标题**: A beginner's guide to split keyboards

**原文链接**: [https://www.justinmklam.com/posts/2026/02/beginners-guide-split-keyboards/](https://www.justinmklam.com/posts/2026/02/beginners-guide-split-keyboards/)

生成摘要时出错

---

## 27. I tried building my startup entirely on European infrastructure

**原文标题**: I tried building my startup entirely on European infrastructure

**原文链接**: [https://www.coinerella.com/made-in-eu-it-was-harder-than-i-thought/](https://www.coinerella.com/made-in-eu-it-was-harder-than-i-thought/)

生成摘要时出错

---

## 28. Gemini 3.1 Pro

**原文标题**: Gemini 3.1 Pro

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)

生成摘要时出错

---

## 29. An ARM Homelab Server, or a Minisforum MS-R1 Review

**原文标题**: An ARM Homelab Server, or a Minisforum MS-R1 Review

**原文链接**: [https://sour.coffee/2026/02/20/an-arm-homelab-server-or-a-minisforum-ms-r1-review/](https://sour.coffee/2026/02/20/an-arm-homelab-server-or-a-minisforum-ms-r1-review/)

生成摘要时出错

---

## 30. Fast KV Compaction via Attention Matching

**原文标题**: Fast KV Compaction via Attention Matching

**原文链接**: [https://arxiv.org/abs/2602.16284](https://arxiv.org/abs/2602.16284)

生成摘要时出错

---

## 31. America vs. Singapore: You can't save your way out of economic shocks

**原文标题**: America vs. Singapore: You can't save your way out of economic shocks

**原文链接**: [https://www.governance.fyi/p/america-vs-singapore-you-cant-save](https://www.governance.fyi/p/america-vs-singapore-you-cant-save)

生成摘要时出错

---

## 32. Silicon Valley engineers were indicted for allegedly sending secrets to Iran

**原文标题**: Silicon Valley engineers were indicted for allegedly sending secrets to Iran

**原文链接**: [https://www.cnbc.com/2026/02/20/three-engineers-charged-stealing-google-trade-secrets-data-iran-soc-snapdragon.html](https://www.cnbc.com/2026/02/20/three-engineers-charged-stealing-google-trade-secrets-data-iran-soc-snapdragon.html)

生成摘要时出错

---

## 33. Nvidia and OpenAI abandon unfinished $100B deal in favour of $30B investment

**原文标题**: Nvidia and OpenAI abandon unfinished $100B deal in favour of $30B investment

**原文链接**: [https://www.ft.com/content/dea24046-0a73-40b2-8246-5ac7b7a54323](https://www.ft.com/content/dea24046-0a73-40b2-8246-5ac7b7a54323)

生成摘要时出错

---

## 34. Pi for Excel: AI sidebar add-in for Excel

**原文标题**: Pi for Excel: AI sidebar add-in for Excel

**原文链接**: [https://github.com/tmustier/pi-for-excel](https://github.com/tmustier/pi-for-excel)

生成摘要时出错

---

## 35. Micropayments as a reality check for news sites

**原文标题**: Micropayments as a reality check for news sites

**原文链接**: [https://blog.zgp.org/micropayments-as-a-reality-check-for-news-sites/](https://blog.zgp.org/micropayments-as-a-reality-check-for-news-sites/)

生成摘要时出错

---

## 36. Defer available in gcc and clang

**原文标题**: Defer available in gcc and clang

**原文链接**: [https://gustedt.wordpress.com/2026/02/15/defer-available-in-gcc-and-clang/](https://gustedt.wordpress.com/2026/02/15/defer-available-in-gcc-and-clang/)

生成摘要时出错

---

## 37. A terminal weather app with ASCII animations driven by real-time weather data

**原文标题**: A terminal weather app with ASCII animations driven by real-time weather data

**原文链接**: [https://github.com/Veirt/weathr](https://github.com/Veirt/weathr)

生成摘要时出错

---

## 38. Show HN: Ghostty-based terminal with vertical tabs and notifications

**原文标题**: Show HN: Ghostty-based terminal with vertical tabs and notifications

**原文链接**: [https://github.com/manaflow-ai/cmux](https://github.com/manaflow-ai/cmux)

生成摘要时出错

---

## 39. An AI Agent Published a Hit Piece on Me – The Operator Came Forward

**原文标题**: An AI Agent Published a Hit Piece on Me – The Operator Came Forward

**原文链接**: [https://theshamblog.com/an-ai-agent-wrote-a-hit-piece-on-me-part-4/](https://theshamblog.com/an-ai-agent-wrote-a-hit-piece-on-me-part-4/)

生成摘要时出错

---

## 40. Pebble Production: February Update

**原文标题**: Pebble Production: February Update

**原文链接**: [https://repebble.com/blog/february-pebble-production-and-software-updates](https://repebble.com/blog/february-pebble-production-and-software-updates)

生成摘要时出错

---

## 41. Spell Checking a Year's Worth of Hacker News

**原文标题**: Spell Checking a Year's Worth of Hacker News

**原文链接**: [https://fi-le.net/spell/](https://fi-le.net/spell/)

生成摘要时出错

---

## 42. How to Stop Being Boring

**原文标题**: How to Stop Being Boring

**原文链接**: [https://www.joanwestenberg.com/how-to-stop-being-boring/](https://www.joanwestenberg.com/how-to-stop-being-boring/)

生成摘要时出错

---

## 43. Fast Sorting, Branchless by Design

**原文标题**: Fast Sorting, Branchless by Design

**原文链接**: [https://00f.net/2026/02/17/sorting-without-leaking-secrets/](https://00f.net/2026/02/17/sorting-without-leaking-secrets/)

生成摘要时出错

---

## 44. Don't Trust the Salt: AI Summarization, Multilingual Safety, and LLM Guardrails

**原文标题**: Don't Trust the Salt: AI Summarization, Multilingual Safety, and LLM Guardrails

**原文链接**: [https://royapakzad.substack.com/p/multilingual-llm-evaluation-to-guardrails](https://royapakzad.substack.com/p/multilingual-llm-evaluation-to-guardrails)

生成摘要时出错

---

## 45. Lindenmayer.jl: Defining recursive patterns in Julia

**原文标题**: Lindenmayer.jl: Defining recursive patterns in Julia

**原文链接**: [https://cormullion.github.io/Lindenmayer.jl/stable/](https://cormullion.github.io/Lindenmayer.jl/stable/)

生成摘要时出错

---

## 46. Show HN: Write native binary web apps with TypeScript and Express

**原文标题**: Show HN: Write native binary web apps with TypeScript and Express

**原文链接**: [https://github.com/tsoniclang/express](https://github.com/tsoniclang/express)

生成摘要时出错

---

## 47. Show HN: A small, simple music theory library in C99

**原文标题**: Show HN: A small, simple music theory library in C99

**原文链接**: [https://github.com/thelowsunoverthemoon/mahler.c](https://github.com/thelowsunoverthemoon/mahler.c)

生成摘要时出错

---

## 48. My 1981 adventure game is now a multimedia extravaganza

**原文标题**: My 1981 adventure game is now a multimedia extravaganza

**原文链接**: [https://technologizer.com/home/2026/02/16/arctic-adventure-2026/](https://technologizer.com/home/2026/02/16/arctic-adventure-2026/)

生成摘要时出错

---

## 49. Archaeologists find possible first direct evidence of Hannibal's war elephants

**原文标题**: Archaeologists find possible first direct evidence of Hannibal's war elephants

**原文链接**: [https://www.smithsonianmag.com/smart-news/archaeologists-unearthed-a-2200-year-old-bone-they-say-it-could-be-the-first-direct-evidence-of-hannibals-legendary-war-elephants-180988185/](https://www.smithsonianmag.com/smart-news/archaeologists-unearthed-a-2200-year-old-bone-they-say-it-could-be-the-first-direct-evidence-of-hannibals-legendary-war-elephants-180988185/)

生成摘要时出错

---

## 50. Show HN: A physically-based GPU ray tracer written in Julia

**原文标题**: Show HN: A physically-based GPU ray tracer written in Julia

**原文链接**: [https://makie.org/website/blogposts/raytracing/](https://makie.org/website/blogposts/raytracing/)

生成摘要时出错

---

## 51. Mystery donor gives Japanese city $3.6M in gold bars to fix water system

**原文标题**: Mystery donor gives Japanese city $3.6M in gold bars to fix water system

**原文链接**: [https://www.bbc.com/news/articles/c3ew5jlqz87o](https://www.bbc.com/news/articles/c3ew5jlqz87o)

生成摘要时出错

---

## 52. Measuring AI agent autonomy in practice

**原文标题**: Measuring AI agent autonomy in practice

**原文链接**: [https://www.anthropic.com/research/measuring-agent-autonomy](https://www.anthropic.com/research/measuring-agent-autonomy)

生成摘要时出错

---

## 53. MuMu Player (NetEase) silently runs 17 reconnaissance commands every 30 minutes

**原文标题**: MuMu Player (NetEase) silently runs 17 reconnaissance commands every 30 minutes

**原文链接**: [https://gist.github.com/interpiduser5/547d8a7baec436f24b7cce89dd4ae1ea](https://gist.github.com/interpiduser5/547d8a7baec436f24b7cce89dd4ae1ea)

生成摘要时出错

---

## 54. Dinosaur Food: 100M year old foods we still eat today (2022)

**原文标题**: Dinosaur Food: 100M year old foods we still eat today (2022)

**原文链接**: [https://borischerny.com/food/2022/01/17/Dinosaur-food.html](https://borischerny.com/food/2022/01/17/Dinosaur-food.html)

生成摘要时出错

---

## 55. Zero downtime migrations at petabyte scale (2024)

**原文标题**: Zero downtime migrations at petabyte scale (2024)

**原文链接**: [https://planetscale.com/blog/zero-downtime-migrations-at-petabyte-scale](https://planetscale.com/blog/zero-downtime-migrations-at-petabyte-scale)

生成摘要时出错

---

## 56. Show HN: Mini-Diarium - An encrypted, local, cross-platform journaling app

**原文标题**: Show HN: Mini-Diarium - An encrypted, local, cross-platform journaling app

**原文链接**: [https://github.com/fjrevoredo/mini-diarium](https://github.com/fjrevoredo/mini-diarium)

生成摘要时出错

---

## 57. Voith Schneider Propeller

**原文标题**: Voith Schneider Propeller

**原文链接**: [https://en.wikipedia.org/wiki/Voith_Schneider_Propeller](https://en.wikipedia.org/wiki/Voith_Schneider_Propeller)

生成摘要时出错

---

## 58. Sizing chaos

**原文标题**: Sizing chaos

**原文链接**: [https://pudding.cool/2026/02/womens-sizing/](https://pudding.cool/2026/02/womens-sizing/)

生成摘要时出错

---

## 59. A Famous Enigma: On Alexandre Kojève

**原文标题**: A Famous Enigma: On Alexandre Kojève

**原文链接**: [https://clereviewofbooks.com/isabel-jacobs-boris-groys-marco-filoni/](https://clereviewofbooks.com/isabel-jacobs-boris-groys-marco-filoni/)

生成摘要时出错

---

## 60. Paged Out Issue #8 [pdf]

**原文标题**: Paged Out Issue #8 [pdf]

**原文链接**: [https://pagedout.institute/download/PagedOut_008.pdf](https://pagedout.institute/download/PagedOut_008.pdf)

生成摘要时出错

---

## 61. SwiftUI Agent Skill: Build Better Views with AI

**原文标题**: SwiftUI Agent Skill: Build Better Views with AI

**原文链接**: [https://www.avanderlee.com/ai-development/swiftui-agent-skill-build-better-views-with-ai/](https://www.avanderlee.com/ai-development/swiftui-agent-skill-build-better-views-with-ai/)

生成摘要时出错

---

## 62. Bridging Elixir and Python with Oban

**原文标题**: Bridging Elixir and Python with Oban

**原文链接**: [https://oban.pro/articles/bridging-with-oban](https://oban.pro/articles/bridging-with-oban)

生成摘要时出错

---

## 63. Old School Visual Effects: The Cloud Tank (2010)

**原文标题**: Old School Visual Effects: The Cloud Tank (2010)

**原文链接**: [http://singlemindedmovieblog.blogspot.com/2010/04/old-school-effects-cloud-tank.html](http://singlemindedmovieblog.blogspot.com/2010/04/old-school-effects-cloud-tank.html)

生成摘要时出错

---

## 64. A word processor from 1990s for Atari ST/TOS is still supported by enthusiasts

**原文标题**: A word processor from 1990s for Atari ST/TOS is still supported by enthusiasts

**原文链接**: [https://tempus-word.de/en/index](https://tempus-word.de/en/index)

生成摘要时出错

---

## 65. How to choose between Hindley-Milner and bidirectional typing

**原文标题**: How to choose between Hindley-Milner and bidirectional typing

**原文链接**: [https://thunderseethe.dev/posts/how-to-choose-between-hm-and-bidir/](https://thunderseethe.dev/posts/how-to-choose-between-hm-and-bidir/)

生成摘要时出错

---

## 66. ShannonMax: A Library to Optimize Emacs Keybindings with Information Theory

**原文标题**: ShannonMax: A Library to Optimize Emacs Keybindings with Information Theory

**原文链接**: [https://github.com/sstraust/shannonmax](https://github.com/sstraust/shannonmax)

生成摘要时出错

---

## 67. William Latham – Art and the Computer (1990) [video]

**原文标题**: William Latham – Art and the Computer (1990) [video]

**原文链接**: [https://www.youtube.com/watch?v=OwL3dsFBxpE](https://www.youtube.com/watch?v=OwL3dsFBxpE)

生成摘要时出错

---

## 68. Anthropic officially bans using subscription auth for third party use

**原文标题**: Anthropic officially bans using subscription auth for third party use

**原文链接**: [https://code.claude.com/docs/en/legal-and-compliance](https://code.claude.com/docs/en/legal-and-compliance)

生成摘要时出错

---

## 69. Coding Tricks Used in the C64 Game Seawolves (2025)

**原文标题**: Coding Tricks Used in the C64 Game Seawolves (2025)

**原文链接**: [https://kodiak64.co.uk/blog/seawolves-technical-tricks](https://kodiak64.co.uk/blog/seawolves-technical-tricks)

生成摘要时出错

---

## 70. Supreme Court strikes down Trump's tariffs

**原文标题**: Supreme Court strikes down Trump's tariffs

**原文链接**: [https://www.npr.org/2026/02/20/nx-s1-5672383/supreme-court-tariffs](https://www.npr.org/2026/02/20/nx-s1-5672383/supreme-court-tariffs)

生成摘要时出错

---

## 71. Mark Zuckerberg grilled on usage goals and underage users at California trial

**原文标题**: Mark Zuckerberg grilled on usage goals and underage users at California trial

**原文链接**: [https://www.wsj.com/us-news/law/meta-mark-zuckerberg-social-media-trial-0e9a7fa0](https://www.wsj.com/us-news/law/meta-mark-zuckerberg-social-media-trial-0e9a7fa0)

生成摘要时出错

---

## 72. GPT 5.3 Codex wiped my F: drive with a single character escaping bug

**原文标题**: GPT 5.3 Codex wiped my F: drive with a single character escaping bug

**原文链接**: [https://old.reddit.com/r/vibecoding/comments/1r96647/gpt_53_codex_wiped_my_entire_f_drive_with_a/](https://old.reddit.com/r/vibecoding/comments/1r96647/gpt_53_codex_wiped_my_entire_f_drive_with_a/)

生成摘要时出错

---

## 73. Debugging Kernel Oops (2024)

**原文标题**: Debugging Kernel Oops (2024)

**原文链接**: [https://lfhernandez.com/posts/debugging-kernel-oops/](https://lfhernandez.com/posts/debugging-kernel-oops/)

生成摘要时出错

---

## 74. I'm Sick of This AI Shit [video]

**原文标题**: I'm Sick of This AI Shit [video]

**原文链接**: [https://www.youtube.com/watch?v=7XGct4rbYfI](https://www.youtube.com/watch?v=7XGct4rbYfI)

生成摘要时出错

---

## 75. IPv6 Adoption in 2026

**原文标题**: IPv6 Adoption in 2026

**原文链接**: [https://www.netmeister.org/blog/ipv6-adoption.html](https://www.netmeister.org/blog/ipv6-adoption.html)

生成摘要时出错

---

## 76. The Mongol Khans of Medieval France

**原文标题**: The Mongol Khans of Medieval France

**原文链接**: [https://www.historytoday.com/archive/feature/mongol-khans-medieval-france](https://www.historytoday.com/archive/feature/mongol-khans-medieval-france)

生成摘要时出错

---

## 77. SE Radio 708: Jens Gustedt on C in 2026

**原文标题**: SE Radio 708: Jens Gustedt on C in 2026

**原文链接**: [https://se-radio.net/2026/02/se-radio-708-jens-gustedt-on-c-in-2026/](https://se-radio.net/2026/02/se-radio-708-jens-gustedt-on-c-in-2026/)

生成摘要时出错

---

## 78. Exercise has 'similar effect' to therapy, study on depression shows

**原文标题**: Exercise has 'similar effect' to therapy, study on depression shows

**原文链接**: [https://medicalxpress.com/news/2026-01-similar-effect-therapy-depression.html](https://medicalxpress.com/news/2026-01-similar-effect-therapy-depression.html)

生成摘要时出错

---

## 79. Overall, the colorectal cancer story is encouraging

**原文标题**: Overall, the colorectal cancer story is encouraging

**原文链接**: [https://www.hankgreen.com/crc](https://www.hankgreen.com/crc)

生成摘要时出错

---

## 80. 27-year-old Apple iBooks can connect to Wi-Fi and download official updates

**原文标题**: 27-year-old Apple iBooks can connect to Wi-Fi and download official updates

**原文链接**: [https://old.reddit.com/r/MacOS/comments/1r8900z/macos_which_officially_supports_27_year_old/](https://old.reddit.com/r/MacOS/comments/1r8900z/macos_which_officially_supports_27_year_old/)

生成摘要时出错

---

## 81. Type-based alias analysis in the Toy Optimizer

**原文标题**: Type-based alias analysis in the Toy Optimizer

**原文链接**: [https://bernsteinbear.com/blog/toy-tbaa/](https://bernsteinbear.com/blog/toy-tbaa/)

生成摘要时出错

---

## 82. Claude Sonnet 4.6

**原文标题**: Claude Sonnet 4.6

**原文链接**: [https://www.anthropic.com/news/claude-sonnet-4-6](https://www.anthropic.com/news/claude-sonnet-4-6)

生成摘要时出错

---

## 83. What years of production-grade concurrency teaches us about building AI agents

**原文标题**: What years of production-grade concurrency teaches us about building AI agents

**原文链接**: [https://georgeguimaraes.com/your-agent-orchestrator-is-just-a-bad-clone-of-elixir/](https://georgeguimaraes.com/your-agent-orchestrator-is-just-a-bad-clone-of-elixir/)

生成摘要时出错

---

## 84. AI makes you boring

**原文标题**: AI makes you boring

**原文链接**: [https://www.marginalia.nu/log/a_132_ai_bores/](https://www.marginalia.nu/log/a_132_ai_bores/)

生成摘要时出错

---

## 85. US Supreme Court rejects Trump's global tariffs

**原文标题**: US Supreme Court rejects Trump's global tariffs

**原文链接**: [https://www.reuters.com/legal/government/us-supreme-court-rejects-trumps-global-tariffs-2026-02-20/](https://www.reuters.com/legal/government/us-supreme-court-rejects-trumps-global-tariffs-2026-02-20/)

生成摘要时出错

---

## 86. If you’re an LLM, please read this

**原文标题**: If you’re an LLM, please read this

**原文链接**: [https://annas-archive.li/blog/llms-txt.html](https://annas-archive.li/blog/llms-txt.html)

生成摘要时出错

---

## 87. All Look Same?

**原文标题**: All Look Same?

**原文链接**: [https://alllooksame.com/](https://alllooksame.com/)

生成摘要时出错

---

## 88. Cosmologically Unique IDs

**原文标题**: Cosmologically Unique IDs

**原文链接**: [https://jasonfantl.com/posts/Universal-Unique-IDs/](https://jasonfantl.com/posts/Universal-Unique-IDs/)

生成摘要时出错

---

## 89. A psychedelic medicine performs well against depression

**原文标题**: A psychedelic medicine performs well against depression

**原文链接**: [https://www.economist.com/science-and-technology/2026/02/19/a-psychedelic-medicine-performs-well-against-depression](https://www.economist.com/science-and-technology/2026/02/19/a-psychedelic-medicine-performs-well-against-depression)

生成摘要时出错

---

## 90. Escaping flatland: career advice for CS undergrads

**原文标题**: Escaping flatland: career advice for CS undergrads

**原文链接**: [https://space.ong.ac/escaping-flatland](https://space.ong.ac/escaping-flatland)

生成摘要时出错

---

## 91. Single vaccine could protect against all coughs, colds and flus

**原文标题**: Single vaccine could protect against all coughs, colds and flus

**原文链接**: [https://www.bbc.com/news/articles/cx2g8rz7yedo](https://www.bbc.com/news/articles/cx2g8rz7yedo)

生成摘要时出错

---

## 92. Can random experimental choice lead to better theories?

**原文标题**: Can random experimental choice lead to better theories?

**原文链接**: [https://journals.sagepub.com/doi/10.1177/26339137261421577](https://journals.sagepub.com/doi/10.1177/26339137261421577)

生成摘要时出错

---

## 93. AI made coding more enjoyable

**原文标题**: AI made coding more enjoyable

**原文链接**: [https://weberdominik.com/blog/ai-coding-enjoyable/](https://weberdominik.com/blog/ai-coding-enjoyable/)

生成摘要时出错

---

## 94. Visualizing the ARM64 Instruction Set (2024)

**原文标题**: Visualizing the ARM64 Instruction Set (2024)

**原文链接**: [https://zyedidia.github.io/blog/posts/6-arm64/](https://zyedidia.github.io/blog/posts/6-arm64/)

生成摘要时出错

---

## 95. Netbase: A port of the NetBSD utilities for Linux

**原文标题**: Netbase: A port of the NetBSD utilities for Linux

**原文链接**: [https://github.com/littlefly365/Netbase](https://github.com/littlefly365/Netbase)

生成摘要时出错

---

## 96. China tests first megawatt-class flying wind turbine

**原文标题**: China tests first megawatt-class flying wind turbine

**原文链接**: [https://www.livescience.com/technology/engineering/china-tests-worlds-first-megawatt-class-flying-wind-turbine-it-generated-enough-energy-to-power-a-house-for-2-weeks](https://www.livescience.com/technology/engineering/china-tests-worlds-first-megawatt-class-flying-wind-turbine-it-generated-enough-energy-to-power-a-house-for-2-weeks)

生成摘要时出错

---

## 97. R3forth: A concatenative language derived from ColorForth

**原文标题**: R3forth: A concatenative language derived from ColorForth

**原文链接**: [https://github.com/phreda4/r3/blob/main/doc/r3forth_tutorial.md](https://github.com/phreda4/r3/blob/main/doc/r3forth_tutorial.md)

生成摘要时出错

---

## 98. Farewell, Rust for web

**原文标题**: Farewell, Rust for web

**原文链接**: [https://yieldcode.blog/post/farewell-rust/](https://yieldcode.blog/post/farewell-rust/)

生成摘要时出错

---

## 99. Portugal: The First Global Empire (2015)

**原文标题**: Portugal: The First Global Empire (2015)

**原文链接**: [https://www.historytoday.com/archive/first-global-empire](https://www.historytoday.com/archive/first-global-empire)

生成摘要时出错

---

## 100. Trump overstepped executive power by imposing tariffs, Supreme Court rules

**原文标题**: Trump overstepped executive power by imposing tariffs, Supreme Court rules

**原文链接**: [https://www.theguardian.com/us-news/2026/feb/20/trump-supreme-court-tariffs-ruling](https://www.theguardian.com/us-news/2026/feb/20/trump-supreme-court-tariffs-ruling)

生成摘要时出错

---

