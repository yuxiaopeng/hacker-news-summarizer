# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-22.md)

*最后自动更新时间: 2026-05-22 19:19:40*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 2 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 3 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 4 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 5 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 6 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 7 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 8 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 9 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 10 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 11 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 12 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 13 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 14 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 15 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 16 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 17 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 18 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 19 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 20 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 21 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 22 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 23 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 24 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 25 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 26 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 27 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 28 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 29 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 30 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 31 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 32 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 33 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 34 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 35 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 36 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 37 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 38 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 39 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 40 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 41 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 42 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 43 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 44 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 45 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 46 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 47 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 48 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 49 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 50 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 51 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 52 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 53 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 54 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 55 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 56 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 57 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 58 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 59 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 60 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 61 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 62 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 63 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 64 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 65 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 66 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 67 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 68 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 69 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 70 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 71 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 72 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 73 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 74 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 75 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 76 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 77 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 78 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 79 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 80 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 81 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 82 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 83 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 84 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 85 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 86 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 87 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 88 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 89 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 90 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 91 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 92 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 93 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 94 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 95 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 96 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 97 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 98 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 99 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 100 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 101 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 102 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 103 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 104 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 105 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 106 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 107 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 108 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 109 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 110 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 111 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 112 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 113 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 114 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 115 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 116 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 117 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 118 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 119 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 120 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 121 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 122 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 123 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 124 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 125 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 126 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 127 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 128 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 129 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 130 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 131 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 132 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 133 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 134 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 135 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 136 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 137 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 138 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 139 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 140 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 141 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 142 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 143 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 144 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 145 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 146 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 147 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 148 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 149 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 150 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 151 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 152 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 153 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 154 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 155 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 156 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 157 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 158 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 159 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 160 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 161 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 162 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 163 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 164 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 165 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 166 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 167 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 168 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 169 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 170 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 171 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 172 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 173 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 174 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 175 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 176 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 177 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 178 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 179 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 180 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 181 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 182 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 183 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 184 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 185 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 186 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 187 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 188 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 189 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 190 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 191 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 192 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 193 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 194 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 195 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 196 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 197 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 198 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 199 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 200 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 201 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 202 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 203 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 204 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 205 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 206 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 207 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 208 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 209 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 210 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 211 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 212 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 213 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 214 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 215 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 216 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 217 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 218 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 219 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 220 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 221 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 222 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 223 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 224 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 225 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 226 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 227 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 228 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 229 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 230 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 231 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 232 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 233 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 234 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 235 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 236 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 237 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 238 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 239 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 240 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 241 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 242 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 243 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 244 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 245 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 246 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 247 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 248 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 249 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 250 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 251 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 252 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 253 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 254 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 255 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 256 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 257 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 258 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 259 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 260 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 261 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 262 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 263 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 264 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 265 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 266 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 267 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 268 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 269 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 270 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 271 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 272 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 273 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 274 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 275 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 276 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 277 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 278 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 279 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 280 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 281 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 282 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 283 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 284 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 285 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 286 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 287 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 288 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 289 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 290 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 291 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 292 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 293 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 294 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 295 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 296 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 297 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 298 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 299 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 300 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 301 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 302 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 303 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 304 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 305 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 306 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 307 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 308 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 309 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 310 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 311 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 312 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 313 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 314 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 315 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 316 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 317 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 318 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 319 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 320 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 321 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 322 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 323 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 324 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 325 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 326 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 327 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 328 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 329 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 330 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 331 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 332 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 333 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 334 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 335 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 336 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 337 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 338 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 339 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 340 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 341 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 342 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 343 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 344 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 345 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 346 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 347 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 348 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 349 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 350 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 351 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 352 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 353 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 354 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 355 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 356 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 357 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 358 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 359 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 360 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 361 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 362 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 363 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 364 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 365 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 366 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 367 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 368 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 369 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 370 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 371 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 372 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 373 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 374 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 375 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 376 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 377 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 378 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 379 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 380 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 381 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 382 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 383 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 384 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 385 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 386 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 387 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 388 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 389 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 390 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 391 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 392 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 393 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 394 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 395 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 396 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 397 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 398 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 399 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 400 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 401 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 402 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 403 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 404 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 405 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 406 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 407 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 408 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 409 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 410 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 411 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 412 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 413 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 414 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 415 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 416 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 417 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 418 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 419 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 420 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 421 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 422 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 423 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 424 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 425 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 426 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 427 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 428 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
