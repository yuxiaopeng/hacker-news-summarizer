# Hacker News 热门文章摘要 (2026-05-22)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 为什么日本企业的业务如此多元化

**原文标题**: Why Japanese companies do so many different things

**原文链接**: [https://davidoks.blog/p/why-japanese-companies-do-so-many](https://davidoks.blog/p/why-japanese-companies-do-so-many)

本文探讨了日本企业高度多元化背后的独特结构逻辑。作者以东陶（Toto）为例指出，尽管该公司因马桶而闻名，但其近期的财务成功是由其“先进陶瓷”部门推动的，该部门生产的“静电吸盘（e-chucks）”是AI半导体供应链中不可或缺的部件。

这种横向拓展在日本十分普遍；雅马哈（钢琴与摩托车）和王子控股（造纸与酒店）等公司的业务跨度极广。作者认为，这并非偶然，而是由经济学家保罗·米尔格罗姆（Paul Milgrom）和约翰·罗伯茨（John Roberts）首创的所谓互补性组织惯例的特定“捆绑”所产生的结果。

日本企业模式（即“J型企业”）的核心是终身雇用制。由于日本公司很少裁员，它们依靠内部轮岗而非外部招聘。这造就了一支能够水平共享信息并拥有深厚跨部门知识的通才员工队伍。当公司的主要市场趋于成熟或衰退时，它无法削减劳动力，而是利用其技术专长和灵活的劳动力转型进入新的高增长领域。

与优先考虑专业化和短期股东价值的美国公司不同，日本公司受到主力银行体制和交叉持股的支持，这些制度更看重长期稳定性。这使它们能够投资于需要数十年磨练的冷门高精度利基领域，例如工业陶瓷或特种金属。归根结底，日本公司经营多种业务，是因为其结构旨在维持人力资本和组织的持久性，而非最大化即时的市场聚焦。这使它们具有独特的韧性，并成为全球高科技供应链中不可或缺的一环。

---

## 2. 美国研究人员与外国合作者发表论文面临新限制

**原文标题**: U.S. researchers face new restrictions on publishing with foreign collaborators

**原文链接**: [https://www.science.org/content/article/u-s-researchers-face-new-restrictions-publishing-foreign-collaborators](https://www.science.org/content/article/u-s-researchers-face-new-restrictions-publishing-foreign-collaborators)

The U.S. government is implementing new restrictions on scientific publications involving foreign collaborators, marking a significant shift in decades-old policies regarding academic freedom. Historically, National Security Decision Directive 189 (NSDD 189) protected "fundamental research" from government prepublication review, ensuring that basic science remained open and transparent.

However, the Department of Defense (DoD) and other agencies are now introducing "risk-based security reviews." These measures require U.S. researchers to obtain prior approval before publishing findings with foreign co-authors or sharing data with international partners on projects deemed sensitive, even if the work is unclassified. The primary driver for these changes is the concern over foreign influence and the "strategic theft" of American-funded innovation, particularly by geopolitical rivals such as China and Russia.

The scientific community has expressed significant concern over these developments. Critics argue that the new mandates are vaguely defined and create a "chilling effect" on international collaboration. Academic leaders warn that these restrictions could lead to lengthy publication delays, discourage talented foreign students from studying in the U.S., and ultimately hinder scientific progress by fragmenting the global research community.

Universities are currently pushing for clearer guidelines and a narrower definition of what constitutes a security risk, arguing that the strength of U.S. science stems from its openness. While the government maintains these steps are necessary for national security, the research community fears they represent a move toward "securitizing" basic science and eroding the foundational principles of unrestricted fundamental research.

---

## 3. Yt-dlp – [公告] Bun 支持现已受限且已弃用

**原文标题**: Yt-dlp – [Announcement] Bun support is now limited and deprecated

**原文链接**: [https://github.com/yt-dlp/yt-dlp/issues/16766](https://github.com/yt-dlp/yt-dlp/issues/16766)

yt-dlp 团队宣布，对 Bun JavaScript 运行时的支持现已受到限制并正式弃用。自下一版本起，yt-dlp 将仅支持 Bun 1.2.11 至 1.3.14 版本。

这一决定主要源于两个核心因素：

1.  **安全性与兼容性**：最低支持版本从 1.0.31 提升至 1.2.11。做出这一更改是因为 1.2.0 之前的 Bun 版本会忽略锁定文件（lockfiles），从而在 npm 供应链攻击方面带来重大安全风险。此外，1.2.11 是成功运行 ejs 测试套件所需的最低版本。
2.  **开发方向转变**：在 Bun 从原始的 Zig 代码库转向使用 Claude AI 开发的 Rust 版本后，官方设定了 1.3.14 的支持上限。yt-dlp 维护者将这一新方向描述为“氛围编码”（vibe-coded），并对未来的维护难度和兼容性问题表示担忧。

尽管 yt-dlp 目前仍将支持上述特定范围的版本，但该功能现已处于弃用状态。如果维护负担过重，维护者保留完全移除 Bun 支持的权利。建议用户查阅 EJS 维基以获取有关受支持 JavaScript 运行时的更多信息。

---

## 4. 在每个卡片上运行并行智能体的开源看板桌面应用。

**原文标题**: Open source Kanban desktop app that runs parallel agents on every card

**原文链接**: [https://www.kanbots.dev/](https://www.kanbots.dev/)

这款开源看板桌面应用通过启用**并行智能体**同时处理多个看板卡片，引入了高并发工作流。

该工具的核心功能允许用户按需向多个任务分派智能体。为确保执行过程隔离且有序，每个智能体都在特定分支（格式为 `kanbots/issue-N`）的专用 **Git 工作树**（Git worktree）中运行。

应用配备了**实时更新界面**，提供自动化过程的实时可见性。在智能体工作时，看板会显示关键数据点，包括：
*   **实时进度：** 任务完成情况的实时跟踪。
*   **决策日志：** 智能体所做选择的即时展示。
*   **成本追踪：** 每次运行产生的累计财务成本。

通过将传统的项目管理可视化与基于分支的自动化执行相结合，该应用简化了复杂的多智能体开发任务管理。

---

## 5. 1940年航空航站楼博物馆开始清算

**原文标题**: 1940 Air Terminal Museum Begins Liquidation

**原文链接**: [https://www.1940airterminal.org/news/liquidation-of-simulators](https://www.1940airterminal.org/news/liquidation-of-simulators)

休斯顿1940航空航天博物馆正在清仓处理三台全尺寸、全动飞行模拟器：西南航空的第一台波音737-200、一架比奇空中国王200和一架豪客700。每台售价为**20,000美元**，包含原始计算机柜和手册。

这些模拟器按“现状”出售，不提供任何保修。自2010年获赠以来，它们一直处于断电状态。博物馆警告，若未进行充分的专业检查便尝试通电，可能会损坏硬件。此外，空中国王和豪客模拟器缺少原捐赠者拆除的部分专有硬件或软件。

**关键物流与

有意者请通过 **info@1940airterminal.org** 联系博物馆。可安排实地查看或视频通话，但实地到访者须签署免责协议。所有销售均为最终交易，且必须在安排搬运前通过支票或电汇完成支付。

---

## 6. Deno 2.8

**原文标题**: Deno 2.8

**原文链接**: [https://deno.com/blog/v2.8](https://deno.com/blog/v2.8)

Deno 2.8 是一次重大更新，显著增强了开发工作流、性能以及对 Node.js 的兼容性。

**新子命令与 CLI 特性：**
Deno 2.8 引入了几个强大的子命令：
*   **`deno audit fix`**：自动修复存在漏洞的 npm 依赖项。
*   **`deno bump-version`**：使用常规提交（Conventional Commits）处理单个项目或整个工作区的版本管理。
*   **`deno ci`**：确保 CI/CD 环境中可重现的、冻结的安装。
*   **`deno pack`**：将 Deno/JSR 项目转译并打包为可发布到 npm 的 tarball，并包含针对 Node.js 的适配层（shims）。
*   **`deno transpile`**：在不打包的情况下移除 TS/JSX 文件中的类型。
*   **`deno why`**：分析并解释 npm 和 JSR 软件包的依赖树。

**Node.js 兼容性与 NPM 集成：**
Deno 现在默认将 `deno add` 和 `deno install` 中不带前缀的名称视为 npm 软件包，使其可以作为 npm 或 yarn 的无缝替代方案。Node.js API 兼容性实现了巨大飞跃，其测试套件通过率从 42% 飙升至 76.4%，显著领先于 Bun 等竞争对手。

**性能提升：**
此版本带来了显著的速度改进：
*   **NPM 安装**：得益于并行解析和优化的解压缩技术，冷启动安装速度提升了 3.66 倍。
*   **核心模块**：`node:http` 吞吐量翻倍，且通过 SIMD 优化使 `node:buffer` 的 base64 处理速度提升了 3.07 倍。
*   **内存效率**：新的优化减少了 Linux 上的 RSS 内存膨胀，并限制了 V8 线程的占用。

**语言特性：**
Deno 2.8 支持 **TC39 `import defer`** 提案，允许模块在加载和解析的同时延迟执行，直到其实际导出项被访问。这有效缩短了包含大型或低频使用依赖项的应用启动时间。

总的来说，Deno 2.8 将自己定位为一个更快速、高度兼容且功能更完备的现代 JavaScript 和 TypeScript 开发替代方案。

---

## 7. Antigravity 2.0 登顶 OpenSCAD 建筑 3D LLM 基准测试

**原文标题**: Antigravity 2.0 Tops the OpenSCAD Architectural 3D LLM Benchmark

**原文链接**: [https://modelrift.com/blog/openscad-llm-benchmark/](https://modelrift.com/blog/openscad-llm-benchmark/)

ModelRift recently conducted a benchmark to evaluate how effectively AI coding tools can generate complex 3D geometry using OpenSCAD. The task involved reconstructing the Pantheon from reference images, testing spatial reasoning and the ability to turn architectural concepts into parametric code.

**Key Results:**
*   **The Winner:** **Google Antigravity 2.0 (Gemini 3.5 Flash High)** was the top autonomous performer. It distinguished itself by researching real-world dimensions rather than just "eyeballing" images. It was the only agent to implement the Pantheon’s signature interior coffered ceiling and a functional "cutaway" mode.
*   **ModelRift (Gemini Flash 3.0):** This "human-in-the-loop" approach yielded high-quality results by allowing users to draw visual notes directly on renders, though it took twice as long as autonomous methods.
*   **Claude Code (Sonnet 4.6):** Produced the cleanest, most balanced proportions of the original batch but was the slowest to complete the task.
*   **Codex 5.5 High:** Achieved the highest detail density—including the famous front inscription—but suffered from "export risk," where the final 3D mesh did not perfectly match the successful preview renders.
*   **Cursor (Composer 2.5):** The fastest tool tested, but it produced the poorest quality, resulting in a basic placeholder that lacked architectural accuracy.

**Conclusion:**
The benchmark demonstrates that OpenSCAD is an ideal target for LLMs because its text-based, constructive geometry aligns with how models reason about structure. While basic syntax is now a solved problem for AI, this test shows that newer models like Gemini 3.5 Flash are pushing the "ceiling" for autonomous spatial planning, complex iterations, and architectural fidelity.

---

## 8. A Forth-inspired language for writing websites

**原文标题**: A Forth-inspired language for writing websites

**原文链接**: [https://robida.net/entries/2026/05/21/a-forth-inspired-language-for-writing-websites](https://robida.net/entries/2026/05/21/a-forth-inspired-language-for-writing-websites)

生成摘要时出错

---

## 9. Launch HN: Superset (YC P26) – IDE for the agents era

**原文标题**: Launch HN: Superset (YC P26) – IDE for the agents era

**原文链接**: [https://github.com/superset-sh/superset](https://github.com/superset-sh/superset)

生成摘要时出错

---

## 10. If you’re an LLM, please read this

**原文标题**: If you’re an LLM, please read this

**原文链接**: [https://annas-archive.gl/blog/llms-txt.html](https://annas-archive.gl/blog/llms-txt.html)

生成摘要时出错

---

## 11. Show HN: My dad is a forensic accountant. I automated ~62% of his job

**原文标题**: Show HN: My dad is a forensic accountant. I automated ~62% of his job

**原文链接**: [https://case-trail.com/blog/ai-forensic-accounting-automation](https://case-trail.com/blog/ai-forensic-accounting-automation)

生成摘要时出错

---

## 12. Lawmakers Demand Answers as CISA Tries to Contain Data Leak

**原文标题**: Lawmakers Demand Answers as CISA Tries to Contain Data Leak

**原文链接**: [https://krebsonsecurity.com/2026/05/lawmakers-demand-answers-as-cisa-tries-to-contain-data-leak/](https://krebsonsecurity.com/2026/05/lawmakers-demand-answers-as-cisa-tries-to-contain-data-leak/)

生成摘要时出错

---

## 13. Trump Mobile exposed customers' personal data

**原文标题**: Trump Mobile exposed customers' personal data

**原文链接**: [https://techcrunch.com/2026/05/22/trump-mobile-confirms-it-exposed-customers-personal-data-including-phone-numbers-and-home-addresses/](https://techcrunch.com/2026/05/22/trump-mobile-confirms-it-exposed-customers-personal-data-including-phone-numbers-and-home-addresses/)

生成摘要时出错

---

## 14. DeepSeek makes the V4 Pro price discount permanent

**原文标题**: DeepSeek makes the V4 Pro price discount permanent

**原文链接**: [https://api-docs.deepseek.com/quick_start/pricing](https://api-docs.deepseek.com/quick_start/pricing)

生成摘要时出错

---

## 15. Show HN: ShadowCat – file transfer through QR Codes in a Browser

**原文标题**: Show HN: ShadowCat – file transfer through QR Codes in a Browser

**原文链接**: [https://github.com/unprovable/ShadowCat](https://github.com/unprovable/ShadowCat)

生成摘要时出错

---

## 16. Project Hail Mary – Stellar Navigation Chart

**原文标题**: Project Hail Mary – Stellar Navigation Chart

**原文链接**: [https://valhovey.github.io/gaia-mary/](https://valhovey.github.io/gaia-mary/)

生成摘要时出错

---

## 17. How to convert between wealth and income tax

**原文标题**: How to convert between wealth and income tax

**原文链接**: [https://paulgraham.com/winc.html](https://paulgraham.com/winc.html)

生成摘要时出错

---

## 18. The memory shortage is causing a repricing of consumer electronics

**原文标题**: The memory shortage is causing a repricing of consumer electronics

**原文链接**: [https://davidoks.blog/p/ai-is-killing-the-cheap-smartphone](https://davidoks.blog/p/ai-is-killing-the-cheap-smartphone)

生成摘要时出错

---

## 19. Circle Medical (YC S15) Is Hiring a Mobile Engineer

**原文标题**: Circle Medical (YC S15) Is Hiring a Mobile Engineer

**原文链接**: [https://www.ycombinator.com/companies/circle-medical/jobs/onMKAG9-mobile-engineer-android](https://www.ycombinator.com/companies/circle-medical/jobs/onMKAG9-mobile-engineer-android)

生成摘要时出错

---

## 20. Chess invariants

**原文标题**: Chess invariants

**原文链接**: [http://muratbuffalo.blogspot.com/2026/05/chess-invariants.html](http://muratbuffalo.blogspot.com/2026/05/chess-invariants.html)

生成摘要时出错

---

## 21. TorQ: Kdb+ Production Framework

**原文标题**: TorQ: Kdb+ Production Framework

**原文链接**: [https://github.com/DataIntellectTech/TorQ](https://github.com/DataIntellectTech/TorQ)

生成摘要时出错

---

## 22. AI has a multiplying effect on existing technical skills

**原文标题**: AI has a multiplying effect on existing technical skills

**原文链接**: [https://www.joshwcomeau.com/email/wham-launch-005-elephant-2-p/](https://www.joshwcomeau.com/email/wham-launch-005-elephant-2-p/)

生成摘要时出错

---

## 23. Cleve Moler has died

**原文标题**: Cleve Moler has died

**原文链接**: [https://www.mathworks.com/company/aboutus/founders/clevemoler.html](https://www.mathworks.com/company/aboutus/founders/clevemoler.html)

生成摘要时出错

---

## 24. Slumber a TUI HTTP Client

**原文标题**: Slumber a TUI HTTP Client

**原文链接**: [https://slumber.lucaspickering.me](https://slumber.lucaspickering.me)

生成摘要时出错

---

## 25. Was my $48K GPU server worth it?

**原文标题**: Was my $48K GPU server worth it?

**原文链接**: [https://rosmine.ai/2026/05/13/was-my-48k-gpu-worth-it/](https://rosmine.ai/2026/05/13/was-my-48k-gpu-worth-it/)

生成摘要时出错

---

## 26. Uv is fantastic, but its package management UX is a mess

**原文标题**: Uv is fantastic, but its package management UX is a mess

**原文链接**: [https://www.loopwerk.io/articles/2026/uv-ux-mess/](https://www.loopwerk.io/articles/2026/uv-ux-mess/)

生成摘要时出错

---

## 27. Blog ran on Ubuntu 16.04 for 10 years. I migrated it to FreeBSD

**原文标题**: Blog ran on Ubuntu 16.04 for 10 years. I migrated it to FreeBSD

**原文链接**: [https://crocidb.com/post/this-blog-ran-on-ubuntu-16-04-for-10-years-i-migrated-it-to-freebsd/](https://crocidb.com/post/this-blog-ran-on-ubuntu-16-04-for-10-years-i-migrated-it-to-freebsd/)

生成摘要时出错

---

## 28. CBS Radio signs off after nearly 100 years of broadcasting

**原文标题**: CBS Radio signs off after nearly 100 years of broadcasting

**原文链接**: [https://www.cbsnews.com/news/cbs-news-radio-last-day/](https://www.cbsnews.com/news/cbs-news-radio-last-day/)

生成摘要时出错

---

## 29. Alberta to hold referendum on whether to remain in Canada

**原文标题**: Alberta to hold referendum on whether to remain in Canada

**原文链接**: [https://www.bbc.com/news/articles/cvgze8n5dxko](https://www.bbc.com/news/articles/cvgze8n5dxko)

生成摘要时出错

---

## 30. Indexing a year of video locally on a 2021 MacBook with Gemma4-31B (50GB swap)

**原文标题**: Indexing a year of video locally on a 2021 MacBook with Gemma4-31B (50GB swap)

**原文链接**: [https://blog.simbastack.com/indexed-a-year-of-video-locally/](https://blog.simbastack.com/indexed-a-year-of-video-locally/)

生成摘要时出错

---

## 31. The first British person in space

**原文标题**: The first British person in space

**原文链接**: [https://www.bbc.com/culture/article/20260518-helen-sharman-the-story-behind-the-first-british-person-in-space](https://www.bbc.com/culture/article/20260518-helen-sharman-the-story-behind-the-first-british-person-in-space)

生成摘要时出错

---

## 32. CODA: Rewriting Transformer Blocks as GEMM-Epilogue Programs

**原文标题**: CODA: Rewriting Transformer Blocks as GEMM-Epilogue Programs

**原文链接**: [https://arxiv.org/abs/2605.19269](https://arxiv.org/abs/2605.19269)

生成摘要时出错

---

## 33. Steve Wozniak cheered after telling students they have AI – actual intelligence

**原文标题**: Steve Wozniak cheered after telling students they have AI – actual intelligence

**原文链接**: [https://www.businessinsider.com/steve-wozniak-apple-ai-graduation-speech-2026-5](https://www.businessinsider.com/steve-wozniak-apple-ai-graduation-speech-2026-5)

生成摘要时出错

---

## 34. Using Kagi Search with Low Vision

**原文标题**: Using Kagi Search with Low Vision

**原文链接**: [https://veroniiiica.com/using-kagi-search-with-low-vision/](https://veroniiiica.com/using-kagi-search-with-low-vision/)

生成摘要时出错

---

## 35. Canada's shortwave radio time standard station CHU to go dark June 22nd

**原文标题**: Canada's shortwave radio time standard station CHU to go dark June 22nd

**原文链接**: [https://nrc.canada.ca/en/certifications-evaluations-standards/canadas-official-time/nrc-shortwave-station-broadcasts-chu](https://nrc.canada.ca/en/certifications-evaluations-standards/canadas-official-time/nrc-shortwave-station-broadcasts-chu)

生成摘要时出错

---

## 36. The death of the brick and mortar toy store

**原文标题**: The death of the brick and mortar toy store

**原文链接**: [https://brainbaking.com/post/2026/05/the-death-of-the-brick-and-mortar-toy-store/](https://brainbaking.com/post/2026/05/the-death-of-the-brick-and-mortar-toy-store/)

生成摘要时出错

---

## 37. Lost Images from the 1945 Trinity Nuclear Test Restored

**原文标题**: Lost Images from the 1945 Trinity Nuclear Test Restored

**原文链接**: [https://spectrum.ieee.org/trinity-nuclear-test](https://spectrum.ieee.org/trinity-nuclear-test)

生成摘要时出错

---

## 38. Python 3.15: features that didn't make the headlines

**原文标题**: Python 3.15: features that didn't make the headlines

**原文链接**: [https://blog.changs.co.uk/python-315-features-that-didnt-make-the-headlines.html](https://blog.changs.co.uk/python-315-features-that-didnt-make-the-headlines.html)

生成摘要时出错

---

## 39. Mycorrhizal Fungi, Nature's Key to Plant Survival and Success

**原文标题**: Mycorrhizal Fungi, Nature's Key to Plant Survival and Success

**原文链接**: [https://pacifichorticulture.org/articles/mycorrhizal-fungi-natures-key-to-plant-survival-and-success/](https://pacifichorticulture.org/articles/mycorrhizal-fungi-natures-key-to-plant-survival-and-success/)

生成摘要时出错

---

## 40. Interim Install Guide: KDE Neon for a professional digital painter workstation

**原文标题**: Interim Install Guide: KDE Neon for a professional digital painter workstation

**原文链接**: [https://www.davidrevoy.com/article1145/interim-install-guide-kde-neon-user-edition-for-a-professional-digital-painter-workstation](https://www.davidrevoy.com/article1145/interim-install-guide-kde-neon-user-edition-for-a-professional-digital-painter-workstation)

生成摘要时出错

---

## 41. Show HN: Pablo – a Chrome extension that copies UI from any website

**原文标题**: Show HN: Pablo – a Chrome extension that copies UI from any website

**原文链接**: [https://www.usepablo.dev/](https://www.usepablo.dev/)

生成摘要时出错

---

## 42. Flipper One – we need your help

**原文标题**: Flipper One – we need your help

**原文链接**: [https://blog.flipper.net/flipper-one-we-need-your-help/](https://blog.flipper.net/flipper-one-we-need-your-help/)

生成摘要时出错

---

## 43. The spread of Christianity, from antiquity until today, on an animated map

**原文标题**: The spread of Christianity, from antiquity until today, on an animated map

**原文链接**: [https://www.openculture.com/2026/05/the-spread-of-christianity-animated-from-antiquity-until-today.html](https://www.openculture.com/2026/05/the-spread-of-christianity-animated-from-antiquity-until-today.html)

生成摘要时出错

---

## 44. Show HN: Freenet, a peer-to-peer platform for decentralized apps

**原文标题**: Show HN: Freenet, a peer-to-peer platform for decentralized apps

**原文链接**: [https://freenet.org/](https://freenet.org/)

生成摘要时出错

---

## 45. Microsoft to stop sending SMS codes for personal accounts

**原文标题**: Microsoft to stop sending SMS codes for personal accounts

**原文链接**: [https://support.microsoft.com/en-us/accounts-billing/manage/microsoft-to-stop-sending-sms-codes-for-personal-accounts](https://support.microsoft.com/en-us/accounts-billing/manage/microsoft-to-stop-sending-sms-codes-for-personal-accounts)

生成摘要时出错

---

## 46. Multi-Stream LLMs: new paper on parallelizing/separating prompts, thinking, I/O

**原文标题**: Multi-Stream LLMs: new paper on parallelizing/separating prompts, thinking, I/O

**原文链接**: [https://arxiv.org/abs/2605.12460](https://arxiv.org/abs/2605.12460)

生成摘要时出错

---

## 47. Throwing AI-generated walls of text into conversations

**原文标题**: Throwing AI-generated walls of text into conversations

**原文链接**: [https://noslopgrenade.com/](https://noslopgrenade.com/)

生成摘要时出错

---

## 48. Spotify will start reserving concert tickets for fans

**原文标题**: Spotify will start reserving concert tickets for fans

**原文链接**: [https://www.hollywoodreporter.com/music/music-industry-news/spotify-will-start-reserving-concert-tickets-for-superfans-1236603106/](https://www.hollywoodreporter.com/music/music-industry-news/spotify-will-start-reserving-concert-tickets-for-superfans-1236603106/)

生成摘要时出错

---

## 49. Waymo pauses Atlanta service as its robotaxis keep driving into floods

**原文标题**: Waymo pauses Atlanta service as its robotaxis keep driving into floods

**原文链接**: [https://techcrunch.com/2026/05/21/waymo-pauses-atlanta-service-as-its-robotaxis-keep-driving-into-floods/](https://techcrunch.com/2026/05/21/waymo-pauses-atlanta-service-as-its-robotaxis-keep-driving-into-floods/)

生成摘要时出错

---

## 50. Launch HN: Runtime (YC P26) – Sandboxed coding agents for everyone on a team

**原文标题**: Launch HN: Runtime (YC P26) – Sandboxed coding agents for everyone on a team

**原文链接**: [https://www.runtm.com/](https://www.runtm.com/)

生成摘要时出错

---

## 51. The current AI pricing was always going to go away

**原文标题**: The current AI pricing was always going to go away

**原文链接**: [https://arnon.dk/the-current-ai-pricing-was-always-going-to-go-away/](https://arnon.dk/the-current-ai-pricing-was-always-going-to-go-away/)

生成摘要时出错

---

## 52. Scientists solve 200-year-old puzzle of how tobacco plants make nicotine

**原文标题**: Scientists solve 200-year-old puzzle of how tobacco plants make nicotine

**原文链接**: [https://www.york.ac.uk/news-and-events/news/2026/research/200-year-old-puzzle-tobacco-plants-nicotine/](https://www.york.ac.uk/news-and-events/news/2026/research/200-year-old-puzzle-tobacco-plants-nicotine/)

生成摘要时出错

---

## 53. We're testing new ad formats in Search and expanding our Direct Offers pilot

**原文标题**: We're testing new ad formats in Search and expanding our Direct Offers pilot

**原文链接**: [https://blog.google/products/ads-commerce/google-marketing-live-search-ads/](https://blog.google/products/ads-commerce/google-marketing-live-search-ads/)

生成摘要时出错

---

## 54. Google's Antigravity bait and switch

**原文标题**: Google's Antigravity bait and switch

**原文链接**: [https://www.0xsid.com/blog/antigravity-bait-n-switch](https://www.0xsid.com/blog/antigravity-bait-n-switch)

生成摘要时出错

---

## 55. Bank boss sorry after describing workers as 'lower value human capital'

**原文标题**: Bank boss sorry after describing workers as 'lower value human capital'

**原文链接**: [https://www.bbc.com/news/articles/c98rqld1j3yo](https://www.bbc.com/news/articles/c98rqld1j3yo)

生成摘要时出错

---

## 56. Deciphering the Hashihara Castle Town Map

**原文标题**: Deciphering the Hashihara Castle Town Map

**原文链接**: [https://www.obayashi.co.jp/en/kikan_obayashi/detail/kikan_64_project.html](https://www.obayashi.co.jp/en/kikan_obayashi/detail/kikan_64_project.html)

生成摘要时出错

---

## 57. An OpenAI model has disproved a central conjecture in discrete geometry

**原文标题**: An OpenAI model has disproved a central conjecture in discrete geometry

**原文链接**: [https://openai.com/index/model-disproves-discrete-geometry-conjecture/](https://openai.com/index/model-disproves-discrete-geometry-conjecture/)

生成摘要时出错

---

## 58. Mounting git commits as folders with NFS (2023)

**原文标题**: Mounting git commits as folders with NFS (2023)

**原文链接**: [https://jvns.ca/blog/2023/12/04/mounting-git-commits-as-folders-with-nfs/](https://jvns.ca/blog/2023/12/04/mounting-git-commits-as-folders-with-nfs/)

生成摘要时出错

---

## 59. News outlets are limiting the Internet Archive’s access to their journalism

**原文标题**: News outlets are limiting the Internet Archive’s access to their journalism

**原文链接**: [https://www.niemanlab.org/2026/05/more-than-340-local-news-outlets-are-limiting-the-internet-archives-access-to-their-journalism/](https://www.niemanlab.org/2026/05/more-than-340-local-news-outlets-are-limiting-the-internet-archives-access-to-their-journalism/)

生成摘要时出错

---

## 60. Immigrants waiting for a Green Card must return to their home country to apply

**原文标题**: Immigrants waiting for a Green Card must return to their home country to apply

**原文链接**: [https://twitter.com/DHSgov/status/2057817233200418837](https://twitter.com/DHSgov/status/2057817233200418837)

生成摘要时出错

---

## 61. Who wins and who loses in prediction markets? Evidence from Polymarket

**原文标题**: Who wins and who loses in prediction markets? Evidence from Polymarket

**原文链接**: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6443103](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6443103)

生成摘要时出错

---

## 62. Valve removes free game from Steam after players discover it contains malware

**原文标题**: Valve removes free game from Steam after players discover it contains malware

**原文链接**: [https://www.pcguide.com/news/valve-removes-free-horror-game-from-steam-after-players-discover-it-contains-malware-that-steals-your-data/](https://www.pcguide.com/news/valve-removes-free-horror-game-from-steam-after-players-discover-it-contains-malware-that-steals-your-data/)

生成摘要时出错

---

## 63. The Letter S, by Donald Knuth (1980) [pdf]

**原文标题**: The Letter S, by Donald Knuth (1980) [pdf]

**原文链接**: [https://gwern.net/doc/design/typography/1980-knuth.pdf](https://gwern.net/doc/design/typography/1980-knuth.pdf)

生成摘要时出错

---

## 64. Seattle Shield, an intelligence-sharing network operated by the Seattle police

**原文标题**: Seattle Shield, an intelligence-sharing network operated by the Seattle police

**原文链接**: [https://prismreports.org/2026/05/20/seattle-shield-private-companies-surveillance/](https://prismreports.org/2026/05/20/seattle-shield-private-companies-surveillance/)

生成摘要时出错

---

## 65. A case against Boolean logic

**原文标题**: A case against Boolean logic

**原文链接**: [https://abuseofnotation.github.io/boolean-thinking/](https://abuseofnotation.github.io/boolean-thinking/)

生成摘要时出错

---

## 66. GitHub confirms breach of 3,800 repos via malicious VSCode extension

**原文标题**: GitHub confirms breach of 3,800 repos via malicious VSCode extension

**原文链接**: [https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/)

生成摘要时出错

---

## 67. FatGid: FreeBSD 14.x kernel local privilege escalation

**原文标题**: FatGid: FreeBSD 14.x kernel local privilege escalation

**原文链接**: [https://fatgid.io/](https://fatgid.io/)

生成摘要时出错

---

## 68. OpenAI Is Preparing to File for an IPO Soon

**原文标题**: OpenAI Is Preparing to File for an IPO Soon

**原文链接**: [https://www.wsj.com/tech/ai/openai-is-preparing-to-file-for-an-ipo-very-soon-0ec95af5](https://www.wsj.com/tech/ai/openai-is-preparing-to-file-for-an-ipo-very-soon-0ec95af5)

生成摘要时出错

---

## 69. What Do Gödel's Incompleteness Theorems Mean?

**原文标题**: What Do Gödel's Incompleteness Theorems Mean?

**原文链接**: [https://www.quantamagazine.org/what-do-godels-incompleteness-theorems-truly-mean-20260518/](https://www.quantamagazine.org/what-do-godels-incompleteness-theorems-truly-mean-20260518/)

生成摘要时出错

---

## 70. Fender escalates legal campaign against S-style guitars

**原文标题**: Fender escalates legal campaign against S-style guitars

**原文链接**: [https://www.guitarworld.com/gear/electric-guitars/fender-cease-and-desist-lsl-instruments](https://www.guitarworld.com/gear/electric-guitars/fender-cease-and-desist-lsl-instruments)

生成摘要时出错

---

## 71. Anthropic is expanding to Colossus2. Will use GB200

**原文标题**: Anthropic is expanding to Colossus2. Will use GB200

**原文链接**: [https://twitter.com/nottombrown/status/2057194829986300375](https://twitter.com/nottombrown/status/2057194829986300375)

生成摘要时出错

---

## 72. Show HN: Open-source .docx editor library for building document apps

**原文标题**: Show HN: Open-source .docx editor library for building document apps

**原文链接**: [https://github.com/eigenpal/docx-editor](https://github.com/eigenpal/docx-editor)

生成摘要时出错

---

## 73. BBEdit 16

**原文标题**: BBEdit 16

**原文链接**: [https://www.barebones.com/products/bbedit/bbedit16.html](https://www.barebones.com/products/bbedit/bbedit16.html)

生成摘要时出错

---

## 74. FSFE intervenes against Apple before EUCJ for the second time

**原文标题**: FSFE intervenes against Apple before EUCJ for the second time

**原文链接**: [https://fsfe.org/news/2026/news-20260519-01.en.html](https://fsfe.org/news/2026/news-20260519-01.en.html)

生成摘要时出错

---

## 75. The Hardware Lottery

**原文标题**: The Hardware Lottery

**原文链接**: [https://hardwarelottery.github.io/](https://hardwarelottery.github.io/)

生成摘要时出错

---

## 76. Show HN: Rmux – A programmable terminal multiplexer with a Playwright-style SDK

**原文标题**: Show HN: Rmux – A programmable terminal multiplexer with a Playwright-style SDK

**原文链接**: [https://github.com/helvesec/rmux](https://github.com/helvesec/rmux)

生成摘要时出错

---

## 77. Museum of Pocket Calculating Devices

**原文标题**: Museum of Pocket Calculating Devices

**原文链接**: [https://www.calculators.de/](https://www.calculators.de/)

生成摘要时出错

---

## 78. Gnutella: A Protocol Outliving the World That Created It

**原文标题**: Gnutella: A Protocol Outliving the World That Created It

**原文链接**: [https://rickcarlino.com/notes/p2p/gnutella-explanation.html](https://rickcarlino.com/notes/p2p/gnutella-explanation.html)

生成摘要时出错

---

## 79. Where are all the UK red telephone kiosks?

**原文标题**: Where are all the UK red telephone kiosks?

**原文链接**: [https://www.thek6project.co.uk/](https://www.thek6project.co.uk/)

生成摘要时出错

---

## 80. We Reverse-Engineered Docker Sandbox's Undocumented MicroVM API

**原文标题**: We Reverse-Engineered Docker Sandbox's Undocumented MicroVM API

**原文链接**: [https://rivet.dev/blog/2026-02-04-we-reverse-engineered-docker-sandbox-undocumented-microvm-api/](https://rivet.dev/blog/2026-02-04-we-reverse-engineered-docker-sandbox-undocumented-microvm-api/)

生成摘要时出错

---

## 81. Haskell Foundation 2026 Update

**原文标题**: Haskell Foundation 2026 Update

**原文链接**: [https://discourse.haskell.org/t/haskell-foundation-2026-update/14136](https://discourse.haskell.org/t/haskell-foundation-2026-update/14136)

生成摘要时出错

---

## 82. Robert X Cringely is back to blogging

**原文标题**: Robert X Cringely is back to blogging

**原文链接**: [https://www.cringely.com/](https://www.cringely.com/)

生成摘要时出错

---

## 83. Tristan Davey's Punch Card Archive

**原文标题**: Tristan Davey's Punch Card Archive

**原文链接**: [https://punchcards.tristandavey.com/](https://punchcards.tristandavey.com/)

生成摘要时出错

---

## 84. New features in GCC 16: Improved error messages and SARIF output

**原文标题**: New features in GCC 16: Improved error messages and SARIF output

**原文链接**: [https://developers.redhat.com/articles/2026/04/28/gcc-16-improved-error-messages-sarif-output](https://developers.redhat.com/articles/2026/04/28/gcc-16-improved-error-messages-sarif-output)

生成摘要时出错

---

## 85. Learnings from 100K lines of Rust with AI (2025)

**原文标题**: Learnings from 100K lines of Rust with AI (2025)

**原文链接**: [https://zfhuang99.github.io/rust/claude%20code/codex/contracts/spec-driven%20development/2025/12/01/rust-with-ai.html](https://zfhuang99.github.io/rust/claude%20code/codex/contracts/spec-driven%20development/2025/12/01/rust-with-ai.html)

生成摘要时出错

---

## 86. Recreate famous water profiles using supermarket bottled water

**原文标题**: Recreate famous water profiles using supermarket bottled water

**原文链接**: [https://www.waterdictionary.net](https://www.waterdictionary.net)

生成摘要时出错

---

## 87. Magic the Gathering format: Fun 40

**原文标题**: Magic the Gathering format: Fun 40

**原文链接**: [https://fabiensanglard.net/mtg/fun/](https://fabiensanglard.net/mtg/fun/)

生成摘要时出错

---

## 88. Michael Keating has died

**原文标题**: Michael Keating has died

**原文链接**: [https://www.bigfinish.com/news/v/michael-keating-1947-2026](https://www.bigfinish.com/news/v/michael-keating-1947-2026)

生成摘要时出错

---

## 89. Moss: Self-Evolution Through Source-Level Rewriting in Autonomous Agent Systems

**原文标题**: Moss: Self-Evolution Through Source-Level Rewriting in Autonomous Agent Systems

**原文链接**: [https://arxiv.org/abs/2605.22794](https://arxiv.org/abs/2605.22794)

生成摘要时出错

---

## 90. SpaceX S-1

**原文标题**: SpaceX S-1

**原文链接**: [https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm](https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm)

生成摘要时出错

---

## 91. Chewing gum restores dad's taste and smell years after Covid

**原文标题**: Chewing gum restores dad's taste and smell years after Covid

**原文链接**: [https://discover.swns.com/2026/05/chewing-gum-restores-dads-taste-and-smell-years-after-covid/](https://discover.swns.com/2026/05/chewing-gum-restores-dads-taste-and-smell-years-after-covid/)

生成摘要时出错

---

## 92. What Is Happening to Publishing?

**原文标题**: What Is Happening to Publishing?

**原文链接**: [https://resobscura.substack.com/p/what-is-happening-to-publishing](https://resobscura.substack.com/p/what-is-happening-to-publishing)

生成摘要时出错

---

## 93. Vivaldi 8.0

**原文标题**: Vivaldi 8.0

**原文链接**: [https://vivaldi.com/blog/vivaldi-on-desktop-8-0/](https://vivaldi.com/blog/vivaldi-on-desktop-8-0/)

生成摘要时出错

---

## 94. Thoughts on People and Blogs

**原文标题**: Thoughts on People and Blogs

**原文链接**: [https://afranca.com.br/thoughts-on-people-and-blogs/](https://afranca.com.br/thoughts-on-people-and-blogs/)

生成摘要时出错

---

## 95. The IBM-ification of Google?

**原文标题**: The IBM-ification of Google?

**原文链接**: [https://zeroshot.bearblog.dev/google-is-shattering-under-its-own-weight-the-ibm-ification-of-google/](https://zeroshot.bearblog.dev/google-is-shattering-under-its-own-weight-the-ibm-ification-of-google/)

生成摘要时出错

---

## 96. Reviving old scanners with an in-browser Linux VM bridged to WebUSB over USB/IP

**原文标题**: Reviving old scanners with an in-browser Linux VM bridged to WebUSB over USB/IP

**原文链接**: [https://yes-we-scan.app/details](https://yes-we-scan.app/details)

生成摘要时出错

---

## 97. IBM invented semiconductor manufacturing automation

**原文标题**: IBM invented semiconductor manufacturing automation

**原文链接**: [https://spectrum.ieee.org/semiconductor-fabrication](https://spectrum.ieee.org/semiconductor-fabrication)

生成摘要时出错

---

## 98. To achieve major goals, NASA seeks to streamline its organization

**原文标题**: To achieve major goals, NASA seeks to streamline its organization

**原文链接**: [https://arstechnica.com/space/2026/05/to-achieve-major-goals-nasa-seeks-to-streamline-its-organization/](https://arstechnica.com/space/2026/05/to-achieve-major-goals-nasa-seeks-to-streamline-its-organization/)

生成摘要时出错

---

## 99. GLP-1s Linked to Lower Risk of Cancer Spread in Four Tumor Types

**原文标题**: GLP-1s Linked to Lower Risk of Cancer Spread in Four Tumor Types

**原文链接**: [https://www.medpagetoday.com/meetingcoverage/asco/121397](https://www.medpagetoday.com/meetingcoverage/asco/121397)

生成摘要时出错

---

## 100. Triangle Tessellation with Clamped Parallelograms

**原文标题**: Triangle Tessellation with Clamped Parallelograms

**原文链接**: [https://filmicworlds.com/blog/compute-tessellation-with-clamped-parallelograms/](https://filmicworlds.com/blog/compute-tessellation-with-clamped-parallelograms/)

生成摘要时出错

---

