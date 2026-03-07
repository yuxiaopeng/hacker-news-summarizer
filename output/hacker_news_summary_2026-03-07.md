# Hacker News 热门文章摘要 (2026-03-07)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Docker 容器十年

**原文标题**: A Decade of Docker Containers

**原文链接**: [https://cacm.acm.org/research/a-decade-of-docker-containers/](https://cacm.acm.org/research/a-decade-of-docker-containers/)

Docker 容器十年回顾

《Docker 容器十年》回顾了 Docker 自 2013 年问世以来对软件行业产生的变革性影响。Docker 最初作为 PaaS 提供商 dotCloud 的内部工具开发，解决了“地狱矩阵”难题——即确保软件在不同环境和硬件上保持运行一致性这一复杂挑战。

通过利用 Linux 内核特性（如 namespaces 和 cgroups），Docker 将“容器”标准化为一种轻量级、可移植的软件单元。正如实体集装箱革新了全球贸易一样，Docker 容器通过将应用程序与底层基础设施解耦，彻底改变了计算领域。这一转变促使行业从沉重的虚拟机 (VM) 转向敏捷、可扩展的微服务。

文章的核心要点包括：

*   **标准化与生态系统**：Docker 培育了一个庞大的生态系统，促成了旨在确保互操作性的开放容器倡议 (OCI) 的创建，并推动了容器编排工具 Kubernetes 的兴起。
*   **开发人员生产力**：“一次构建，到处运行”的理念简化了 CI/CD 流水线，并极大地解决了“在我的机器上能运行”的问题。
*   **对科研的影响**：容器已成为科学复现性的关键，允许研究人员打包复杂的计算环境，以便他人能够精准复刻实验结果。
*   **未来方向**：随着 Docker 进入第二个十年，重点正转向增强软件供应链安全（使用 SBOM）、缩减镜像体积，以及与 WebAssembly (Wasm) 等新兴技术集成。

最终，文章将 Docker 定义为开发人员与运维人员之间“社会契约”的根本性转变，而不仅仅是一个工具；它实现了系统级技术的民主化，并定义了现代云原生时代。

---

## 2. 可能改变癌症治疗的毫秒瞬间

**原文标题**: The Millisecond That Could Change Cancer Treatment

**原文链接**: [https://spectrum.ieee.org/flash-radiotherapy](https://spectrum.ieee.org/flash-radiotherapy)

FLASH放射治疗是一种革命性的癌症治疗方法，它在不到十分之一秒的单次脉冲中释放超高功率辐射。与需要多次疗程且往往会损伤健康组织的常规放疗不同，FLASH能有效清除肿瘤，同时使周围器官几乎不受损伤。

这种“FLASH效应”是由研究人员Vincent Favaudon和Marie-Catherine Vozenin发现的，他们观察到高速、高剂量的辐射并不会在动物组织中产生预期的疤痕。虽然确切的生物机制仍是一个谜，但目前的理论认为，健康细胞和癌细胞对辐射产生的活性氧的处理方式有所不同。

为了将这种疗法推向临床应用，研究人员正与欧洲核子研究中心（CERN）和斯坦福大学SLAC国家加速器实验室等粒子物理机构展开合作。目前面临的一个重大挑战，是从仅能治疗表面肿瘤的低能电子束，过渡到能够触及肺部或大脑深处肿瘤的高能系统。

CERN的CLEAR设施正在重新利用基础物理项目（如紧凑型线性对撞机CLIC）的硬件，以开发能以亚毫米级精度引导高能电子的紧凑型线性加速器。与此同时，其他研究人员也在探索将质子和碳离子作为照射粒子，尽管这些通常需要更庞大、更昂贵的设施。

通过将高能物理与放射肿瘤学相结合，FLASH疗法有望变革癌症护理。如果正在进行的试验取得成功，该技术将提供疗效更好且副作用显著减少的治疗方案，使原本为揭开宇宙奥秘而设计的工具产生更直接的“社会影响”。

---

## 3. Show HN：Argus —— 用于 Claude Code 会话的 VSCode 调试器

**原文标题**: Show HN: Argus – VSCode debugger for Claude Code sessions

**原文链接**: [https://github.com/yessGlory17/argus](https://github.com/yessGlory17/argus)

**Argus** 是一款新发布的 VS Code 扩展，旨在作为 Claude Code 会话的全方位调试器和性能分析器。该工具以希腊神话中的百眼巨人命名，为开发人员提供了对 Claude Code 与项目交互过程的深度可见性，有助于优化工作流程并降低成本。

**核心功能与能力：**
*   **智能分析：** Argus 采用基于规则的引擎，可检测文件重复读取、重试循环、工具调用失败和上下文窗口压力等低效问题。
*   **成本与性能追踪：** 它提供了 Token 使用情况、API 成本和缓存命中率的详细明细，方便用户识别“浪费”的支出并提升会话效率。
*   **可视化仪表盘：** 该扩展包含八个专业标签页，包括一个交互式 **Flow** 流程图（由 D3.js 驱动）用于可视化文件依赖关系，以及一个 **Steps** 日志用于检查特定的工具调用。
*   **无缝集成：** Argus 会自动扫描用户目录中的 Claude Code 会话，并直接集成到 VS Code 侧边栏中。它支持实时监控、多项目管理以及原生深色模式。

**技术基础：**
Argus 最初是使用 Wails 构建的独立桌面应用，现已完全重写为原生 VS Code 扩展。它采用 React 19 前端和高性能 TypeScript 后端，能够流式传输和解析大型 JSONL 会话文件。

**价值主张：**
对于个人开发者和团队而言，Argus 既是调试工具，也是教育资源。它帮助用户理解基于大语言模型（LLM）的开发模式，审计 AI 使用情况，并精炼其提示词策略，从而以更低的成本获得更快的反馈结果。

该项目采用 MIT 许可证开源，可在 GitHub 上获取并欢迎社区贡献。

---

## 4. Ki Editor - 一款基于 AST 的编辑器

**原文标题**: Ki Editor - an editor that operates on the AST

**原文链接**: [https://ki-editor.org/](https://ki-editor.org/)

**Ki Editor** 是一款旨在直接操作编程语言抽象语法树 (AST)，而非将代码仅视为简单文本的代码编辑器。通过缩小意图与行动之间的差距，它允许开发者直接操控语法结构，从而消除了对复杂键盘或鼠标操作的需求。

核心特性包括：
*   **语法节点交互：** 直接操控代码结构，实现更直观的编辑体验。
*   **多光标：** 通过对语法节点的并行操作提升效率，助力快速批量编辑与重构。
*   **重新定义的模态编辑：** 灵活的“选择模式”系统规范了在单词、行和语法节点间的导航与移动，确保一致且流畅的用户体验。

---

## 5. 将 Prolog 编译为 Forth [pdf]

**原文标题**: Compiling Prolog to Forth [pdf]

**原文链接**: [https://vfxforth.com/flag/jfar/vol4/no4/article4.pdf](https://vfxforth.com/flag/jfar/vol4/no4/article4.pdf)

这篇文章题为**《将 Prolog 编译为 Forth》**，探讨了在基于栈的底层语言框架（Forth）中实现逻辑编程环境（Prolog）的技术方法。该论文主要关注如何弥合 Prolog 的高级声明式特性与 Forth 高效的线索化代码（threaded-code）执行之间的差距。

**核心要点：**

1.  **华伦抽象机 (WAM) 映射：** 研究的核心通常在于使用 Forth 实现 WAM 的某个版本（WAM 是 Prolog 执行的标准）。Forth 是实现这一目标的理想选择，因为其原生的“线索化代码”结构允许高效地实现虚拟机指令。
2.  **内存管理：** 系统在 Forth 环境中定义了特定的内存区域来处理 Prolog 独特的数据结构。这包括**堆**（用于存储项）、**栈**（用于局部变量和环境）以及**轨迹堆栈**（Trail，用于跟踪变量绑定以实现回溯）。
3.  **合一与回溯：** 论文描述了如何在 Forth 中实现 Prolog 的核心引擎。合一过程通过比较项的专门 Forth “词”（words）来处理，而回溯则通过“选择点”进行管理——即保存在栈上的记录，允许系统在目标失败时恢复之前的状态。
4.  **性能与紧凑性：** 讨论的主要动机之一是 Forth 的小巧占用。将 Prolog 编译为 Forth 可以得到一个具有高度可移植性和内存效率的系统，使其适用于全尺寸 Prolog 解释器过于沉重的嵌入式系统或资源有限的硬件。
5.  **集成性：** 该方法允许建立一种“混合”编程环境，开发人员可以使用原生 Forth 编写底层的、对时间要求严格的任务，并使用 Prolog 编写高级逻辑，两者共享同一个执行环境。

综上所述，本文表明 Forth 的可扩展性和底层控制能力为构建高性能 Prolog 编译器提供了坚实基础，同时保持了栈式语言特有的可移植性和高效性。

---

## 6. Show HN: ANSI-Saver – 一款 macOS 屏幕保护程序

**原文标题**: Show HN: ANSI-Saver – A macOS Screensaver

**原文链接**: [https://github.com/lardissone/ansi-saver](https://github.com/lardissone/ansi-saver)

**AnsiSaver** 是一款专为 macOS 设计的屏幕保护程序，旨在将 BBS（电子公告牌系统）时代的审美带入现代桌面。它能够渲染源自庞大的 **16colo.rs** 在线存档或本地目录的 ANSI 和 ASCII 艺术，并以令人回想起 20 世纪 90 年代终端连接风格的方式在屏幕上滚动。

**主要特性：**
*   **原汁原味的渲染：** 使用 `libansilove` 库和 CP437 位图字体，准确渲染包括 .ANS、.ICE、.BIN 和 .XB 在内的多种格式。
*   **流畅的视觉效果：** 支持 60fps 滚动，具有可调速度和“连续滚动”模式（将艺术作品堆叠成无尽的垂直流）。它还提供淡入淡出过渡效果，并支持高达 4 倍的渲染缩放，确保在 Retina 显示屏上清晰输出。
*   **高度定制：** 用户可以将屏幕保护程序指向特定的 16colo.rs 资源包或个人本地收藏。
*   **技术架构：** 资源包会被下载并缓存至本地，利用 Core Animation 实现高效渲染和极低的内存占用。

**要求与安装：**
AnsiSaver 专为运行 **macOS Sequoia (15.0)** 或更高版本的 **Apple 芯片 Mac** 构建。由于该软件未经过 Apple 开发者证书签名，用户在安装后必须通过系统设置的“隐私与安全性”部分手动允许其运行。高级用户还可以使用 Xcode 和 Homebrew 从源代码自行构建。

该项目在 **MIT 许可证**下开源，既是一个实用的工具，也是对 ACiD、iCE 和 Blocktronics 等数字艺术团体的致敬。

---

## 7. SigNoz (YC W21，开源版 Datadog) 正在多岗位招聘

**原文标题**: SigNoz (YC W21, open source Datadog) Is Hiring across roles

**原文链接**: [https://signoz.io/careers](https://signoz.io/careers)

**SigNoz**, a member of the Y Combinator Winter 2021 batch, has announced that it is actively hiring for various positions across the company. 

Positioned as an **open-source alternative to Datadog**, SigNoz provides a comprehensive observability platform that helps developers monitor applications and troubleshoot problems. The tool integrates metrics, traces, and logs into a single dashboard, offering a transparent and community-driven approach to system monitoring.

**Key Information:**
*   **Company Background:** SigNoz is a YC W21 alumnus building developer-focused observability tools.
*   **Product Focus:** Open-source software designed to compete with proprietary services like Datadog.
*   **Hiring Status:** The company is currently scaling and looking for talent across multiple roles.
*   **Action Required:** Interested candidates should visit the SigNoz careers page (noting that JavaScript must be enabled to view the specific job listings).

In summary, this announcement highlights a growth phase for the company as it seeks to expand its team to further develop its open-source monitoring ecosystem.

---

## 8. Plasma Bigscreen – 10-foot interface for KDE plasma

**原文标题**: Plasma Bigscreen – 10-foot interface for KDE plasma

**原文链接**: [https://plasma-bigscreen.org](https://plasma-bigscreen.org)

生成摘要时出错

---

## 9. The yoghurt delivery women combatting loneliness in Japan

**原文标题**: The yoghurt delivery women combatting loneliness in Japan

**原文链接**: [https://www.bbc.com/travel/article/20260302-the-yoghurt-delivery-women-combatting-loneliness-in-japan](https://www.bbc.com/travel/article/20260302-the-yoghurt-delivery-women-combatting-loneliness-in-japan)

生成摘要时出错

---

## 10. Re-creating the complex cuisine of prehistoric Europeans

**原文标题**: Re-creating the complex cuisine of prehistoric Europeans

**原文链接**: [https://arstechnica.com/science/2026/03/recreating-the-complex-cuisine-of-prehistoric-europeans/](https://arstechnica.com/science/2026/03/recreating-the-complex-cuisine-of-prehistoric-europeans/)

生成摘要时出错

---

## 11. PC processors entered the Gigahertz era today in the year 2000 with AMD's Athlon

**原文标题**: PC processors entered the Gigahertz era today in the year 2000 with AMD's Athlon

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/pc-processors-entered-the-gigahertz-era-today-in-the-year-2000-with-amds-athlon-amd-hit-marketing-gold-with-its-1-ghz-athlon-beat-intel-by-a-nose](https://www.tomshardware.com/pc-components/cpus/pc-processors-entered-the-gigahertz-era-today-in-the-year-2000-with-amds-athlon-amd-hit-marketing-gold-with-its-1-ghz-athlon-beat-intel-by-a-nose)

生成摘要时出错

---

## 12. Tech jobs are getting demolished in ways not seen since 2008

**原文标题**: Tech jobs are getting demolished in ways not seen since 2008

**原文链接**: [https://www.businessinsider.com/tech-jobs-getting-demolished-great-recession-dot-com-era-2026-3](https://www.businessinsider.com/tech-jobs-getting-demolished-great-recession-dot-com-era-2026-3)

生成摘要时出错

---

## 13. Filesystems Are Having a Moment

**原文标题**: Filesystems Are Having a Moment

**原文链接**: [https://madalitso.me/notes/why-everyone-is-talking-about-filesystems/](https://madalitso.me/notes/why-everyone-is-talking-about-filesystems/)

生成摘要时出错

---

## 14. UUID package coming to Go standard library

**原文标题**: UUID package coming to Go standard library

**原文链接**: [https://github.com/golang/go/issues/62026](https://github.com/golang/go/issues/62026)

生成摘要时出错

---

## 15. Self-Portrait by Ernst Mach (1886)

**原文标题**: Self-Portrait by Ernst Mach (1886)

**原文链接**: [https://publicdomainreview.org/collection/self-portrait-by-ernst-mach-1886/](https://publicdomainreview.org/collection/self-portrait-by-ernst-mach-1886/)

生成摘要时出错

---

## 16. this css proves me human

**原文标题**: this css proves me human

**原文链接**: [https://will-keleher.com/posts/this-css-makes-me-human/](https://will-keleher.com/posts/this-css-makes-me-human/)

生成摘要时出错

---

## 17. 48x32, a 1536 LED Game Computer (2023)

**原文标题**: 48x32, a 1536 LED Game Computer (2023)

**原文链接**: [https://jacquesmattheij.com/48x32-introduction/](https://jacquesmattheij.com/48x32-introduction/)

生成摘要时出错

---

## 18. Helix: A post-modern text editor

**原文标题**: Helix: A post-modern text editor

**原文链接**: [https://helix-editor.com/](https://helix-editor.com/)

生成摘要时出错

---

## 19. Uploading Pirated Books via BitTorrent Qualifies as Fair Use, Meta Argues

**原文标题**: Uploading Pirated Books via BitTorrent Qualifies as Fair Use, Meta Argues

**原文链接**: [https://torrentfreak.com/uploading-pirated-books-via-bittorrent-qualifies-as-fair-use-meta/](https://torrentfreak.com/uploading-pirated-books-via-bittorrent-qualifies-as-fair-use-meta/)

生成摘要时出错

---

## 20. Seurat Most Famous for Paris Park Painting Yet Half His Paintings Were Seascapes

**原文标题**: Seurat Most Famous for Paris Park Painting Yet Half His Paintings Were Seascapes

**原文链接**: [https://www.smithsonianmag.com/smart-news/georges-seurat-is-most-famous-for-his-pointillist-painting-of-a-paris-park-but-more-than-half-of-his-canvases-were-stunning-seascapes-180988245/](https://www.smithsonianmag.com/smart-news/georges-seurat-is-most-famous-for-his-pointillist-painting-of-a-paris-park-but-more-than-half-of-his-canvases-were-stunning-seascapes-180988245/)

生成摘要时出错

---

## 21. Tinnitus Is Connected to Sleep

**原文标题**: Tinnitus Is Connected to Sleep

**原文链接**: [https://www.sciencealert.com/tinnitus-is-somehow-connected-to-a-crucial-bodily-function](https://www.sciencealert.com/tinnitus-is-somehow-connected-to-a-crucial-bodily-function)

生成摘要时出错

---

## 22. Galileo's handwritten notes found in ancient astronomy text

**原文标题**: Galileo's handwritten notes found in ancient astronomy text

**原文链接**: [https://www.science.org/content/article/galileo-s-handwritten-notes-found-ancient-astronomy-text](https://www.science.org/content/article/galileo-s-handwritten-notes-found-ancient-astronomy-text)

生成摘要时出错

---

## 23. Working and Communicating with Japanese Engineers

**原文标题**: Working and Communicating with Japanese Engineers

**原文链接**: [https://www.tokyodev.com/articles/working-and-communicating-with-japanese-engineers](https://www.tokyodev.com/articles/working-and-communicating-with-japanese-engineers)

生成摘要时出错

---

## 24. LLMs work best when the user defines their acceptance criteria first

**原文标题**: LLMs work best when the user defines their acceptance criteria first

**原文链接**: [https://blog.katanaquant.com/p/your-llm-doesnt-write-correct-code](https://blog.katanaquant.com/p/your-llm-doesnt-write-correct-code)

生成摘要时出错

---

## 25. QGIS 4.0

**原文标题**: QGIS 4.0

**原文链接**: [https://changelog.qgis.org/en/version/4.0/](https://changelog.qgis.org/en/version/4.0/)

生成摘要时出错

---

## 26. Lock Scroll with a Vengeance

**原文标题**: Lock Scroll with a Vengeance

**原文链接**: [https://unsung.aresluna.org/lock-scroll-with-a-vengeance/](https://unsung.aresluna.org/lock-scroll-with-a-vengeance/)

生成摘要时出错

---

## 27. Show HN: µJS, a 5KB alternative to Htmx and Turbo with zero dependencies

**原文标题**: Show HN: µJS, a 5KB alternative to Htmx and Turbo with zero dependencies

**原文链接**: [https://mujs.org](https://mujs.org)

生成摘要时出错

---

## 28. Show HN: Moongate – Ultima Online server emulator in .NET 10 with Lua scripting

**原文标题**: Show HN: Moongate – Ultima Online server emulator in .NET 10 with Lua scripting

**原文链接**: [https://github.com/moongate-community/moongatev2](https://github.com/moongate-community/moongatev2)

生成摘要时出错

---

## 29. Migrating from Heroku to Magic Containers

**原文标题**: Migrating from Heroku to Magic Containers

**原文链接**: [https://bunny.net/blog/migrating-from-heroku-to-magic-containers/](https://bunny.net/blog/migrating-from-heroku-to-magic-containers/)

生成摘要时出错

---

## 30. Compiling Match Statements to Bytecode

**原文标题**: Compiling Match Statements to Bytecode

**原文链接**: [https://xnacly.me/posts/2026/compiling-match-statements-to-bytecode/](https://xnacly.me/posts/2026/compiling-match-statements-to-bytecode/)

生成摘要时出错

---

## 31. My application programmer instincts failed when debugging assembler

**原文标题**: My application programmer instincts failed when debugging assembler

**原文链接**: [https://landedstar.com/blog/posts/how-my-application-programmer-instincts-failed-when-debugging-assembler/](https://landedstar.com/blog/posts/how-my-application-programmer-instincts-failed-when-debugging-assembler/)

生成摘要时出错

---

## 32. The Banality of Surveillance

**原文标题**: The Banality of Surveillance

**原文链接**: [https://benn.substack.com/p/the-banality-of-surveillance](https://benn.substack.com/p/the-banality-of-surveillance)

生成摘要时出错

---

## 33. The Case of the Disappearing Secretary

**原文标题**: The Case of the Disappearing Secretary

**原文链接**: [https://rowlandmanthorpe.substack.com/p/the-case-of-the-disappearing-secretary](https://rowlandmanthorpe.substack.com/p/the-case-of-the-disappearing-secretary)

生成摘要时出错

---

## 34. Sarvam 105B, the first competitive Indian open source LLM

**原文标题**: Sarvam 105B, the first competitive Indian open source LLM

**原文链接**: [https://www.sarvam.ai/blogs/sarvam-30b-105b](https://www.sarvam.ai/blogs/sarvam-30b-105b)

生成摘要时出错

---

## 35. CT Scans of Health Wearables

**原文标题**: CT Scans of Health Wearables

**原文链接**: [https://www.lumafield.com/scan-of-the-month/health-wearables](https://www.lumafield.com/scan-of-the-month/health-wearables)

生成摘要时出错

---

## 36. Querying 3B Vectors

**原文标题**: Querying 3B Vectors

**原文链接**: [https://vickiboykis.com/2026/02/21/querying-3-billion-vectors/](https://vickiboykis.com/2026/02/21/querying-3-billion-vectors/)

生成摘要时出错

---

## 37. Editing changes in patch format with Jujutsu

**原文标题**: Editing changes in patch format with Jujutsu

**原文链接**: [https://www.knifepoint.net/~kat/kb-jj-patchedit.html](https://www.knifepoint.net/~kat/kb-jj-patchedit.html)

生成摘要时出错

---

## 38. Tech employment now significantly worse than the 2008 or 2020 recessions

**原文标题**: Tech employment now significantly worse than the 2008 or 2020 recessions

**原文链接**: [https://twitter.com/JosephPolitano/status/2029916364664611242](https://twitter.com/JosephPolitano/status/2029916364664611242)

生成摘要时出错

---

## 39. Entomologists use a particle accelerator to image ants at scale

**原文标题**: Entomologists use a particle accelerator to image ants at scale

**原文链接**: [https://spectrum.ieee.org/3d-scanning-particle-accelerator-antscan](https://spectrum.ieee.org/3d-scanning-particle-accelerator-antscan)

生成摘要时出错

---

## 40. Claude Code deletes developers' production setup, including database

**原文标题**: Claude Code deletes developers' production setup, including database

**原文链接**: [https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-code-deletes-developers-production-setup-including-its-database-and-snapshots-2-5-years-of-records-were-nuked-in-an-instant](https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-code-deletes-developers-production-setup-including-its-database-and-snapshots-2-5-years-of-records-were-nuked-in-an-instant)

生成摘要时出错

---

## 41. What canceled my Go context?

**原文标题**: What canceled my Go context?

**原文链接**: [https://rednafi.com/go/context-cancellation-cause/](https://rednafi.com/go/context-cancellation-cause/)

生成摘要时出错

---

## 42. Hardening Firefox with Anthropic's Red Team

**原文标题**: Hardening Firefox with Anthropic's Red Team

**原文链接**: [https://www.anthropic.com/news/mozilla-firefox-security](https://www.anthropic.com/news/mozilla-firefox-security)

生成摘要时出错

---

## 43. A tool that removes censorship from open-weight LLMs

**原文标题**: A tool that removes censorship from open-weight LLMs

**原文链接**: [https://github.com/elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS)

生成摘要时出错

---

## 44. Workers who love ‘synergizing paradigms’ might be bad at their jobs

**原文标题**: Workers who love ‘synergizing paradigms’ might be bad at their jobs

**原文链接**: [https://news.cornell.edu/stories/2026/03/workers-who-love-synergizing-paradigms-might-be-bad-their-jobs](https://news.cornell.edu/stories/2026/03/workers-who-love-synergizing-paradigms-might-be-bad-their-jobs)

生成摘要时出错

---

## 45. The Longing (1999)

**原文标题**: The Longing (1999)

**原文链接**: [https://www.cluetrain.com/book/longing.html](https://www.cluetrain.com/book/longing.html)

生成摘要时出错

---

## 46. US economy sheds 92,000 jobs in February in sharp slide

**原文标题**: US economy sheds 92,000 jobs in February in sharp slide

**原文链接**: [https://www.ft.com/content/6542bd0c-59ca-493b-ab5d-2d69e4e00cae](https://www.ft.com/content/6542bd0c-59ca-493b-ab5d-2d69e4e00cae)

生成摘要时出错

---

## 47. Good Bad ISPs

**原文标题**: Good Bad ISPs

**原文链接**: [https://community.torproject.org/relay/community-resources/good-bad-isps/](https://community.torproject.org/relay/community-resources/good-bad-isps/)

生成摘要时出错

---

## 48. Show HN: I open-sourced my Steam game, 100% written in Lua, engine is also open

**原文标题**: Show HN: I open-sourced my Steam game, 100% written in Lua, engine is also open

**原文链接**: [https://github.com/willtobyte/reprobate](https://github.com/willtobyte/reprobate)

生成摘要时出错

---

## 49. It took four years until 2011’s iOS 5 gave everyone an emoji keyboard

**原文标题**: It took four years until 2011’s iOS 5 gave everyone an emoji keyboard

**原文链接**: [https://unsung.aresluna.org/im-obviously-taking-a-risk-here-by-advertising-emoji-directly/](https://unsung.aresluna.org/im-obviously-taking-a-risk-here-by-advertising-emoji-directly/)

生成摘要时出错

---

## 50. Boy I was wrong about the Fediverse

**原文标题**: Boy I was wrong about the Fediverse

**原文链接**: [https://matduggan.com/boy-i-was-wrong-about-the-fediverse/](https://matduggan.com/boy-i-was-wrong-about-the-fediverse/)

生成摘要时出错

---

## 51. Modernizing swapping: virtual swap spaces

**原文标题**: Modernizing swapping: virtual swap spaces

**原文链接**: [https://lwn.net/Articles/1059201/](https://lwn.net/Articles/1059201/)

生成摘要时出错

---

## 52. Analytic Fog Rendering with Volumetric Primitives (2025)

**原文标题**: Analytic Fog Rendering with Volumetric Primitives (2025)

**原文链接**: [https://matejlou.blog/2025/02/11/analytic-fog-rendering-with-volumetric-primitives/](https://matejlou.blog/2025/02/11/analytic-fog-rendering-with-volumetric-primitives/)

生成摘要时出错

---

## 53. Apple Used to Design Its Laptops for Repairability

**原文标题**: Apple Used to Design Its Laptops for Repairability

**原文链接**: [https://www.ifixit.com/News/115995/how-apple-used-to-design-its-laptops-for-repairability](https://www.ifixit.com/News/115995/how-apple-used-to-design-its-laptops-for-repairability)

生成摘要时出错

---

## 54. Show HN: Kula – Lightweight, self-contained Linux server monitoring tool

**原文标题**: Show HN: Kula – Lightweight, self-contained Linux server monitoring tool

**原文链接**: [https://github.com/c0m4r/kula](https://github.com/c0m4r/kula)

生成摘要时出错

---

## 55. GPT-5.4

**原文标题**: GPT-5.4

**原文链接**: [https://openai.com/index/introducing-gpt-5-4/](https://openai.com/index/introducing-gpt-5-4/)

生成摘要时出错

---

## 56. Show HN: Claude-replay – A video-like player for Claude Code sessions

**原文标题**: Show HN: Claude-replay – A video-like player for Claude Code sessions

**原文链接**: [https://github.com/es617/claude-replay](https://github.com/es617/claude-replay)

生成摘要时出错

---

## 57. Global warming has accelerated significantly

**原文标题**: Global warming has accelerated significantly

**原文链接**: [https://www.researchsquare.com/article/rs-6079807/v1](https://www.researchsquare.com/article/rs-6079807/v1)

生成摘要时出错

---

## 58. Global warming has accelerated significantly

**原文标题**: Global warming has accelerated significantly

**原文链接**: [https://www.researchsquare.com/article/rs-6079807/v1](https://www.researchsquare.com/article/rs-6079807/v1)

生成摘要时出错

---

## 59. Ada 2022

**原文标题**: Ada 2022

**原文链接**: [https://www.adaic.org/ada-resources/standards/ada22/](https://www.adaic.org/ada-resources/standards/ada22/)

生成摘要时出错

---

## 60. SPA vs. Hypermedia: Real-World Performance Under Load

**原文标题**: SPA vs. Hypermedia: Real-World Performance Under Load

**原文链接**: [https://zweiundeins.gmbh/en/methodology/spa-vs-hypermedia-real-world-performance-under-load](https://zweiundeins.gmbh/en/methodology/spa-vs-hypermedia-real-world-performance-under-load)

生成摘要时出错

---

## 61. Some Words on WigglyPaint

**原文标题**: Some Words on WigglyPaint

**原文链接**: [https://beyondloom.com/blog/onwigglypaint.html](https://beyondloom.com/blog/onwigglypaint.html)

生成摘要时出错

---

## 62. Show HN: 1v1 coding game that LLMs struggle with

**原文标题**: Show HN: 1v1 coding game that LLMs struggle with

**原文链接**: [https://yare.io](https://yare.io)

生成摘要时出错

---

## 63. Astra: An open-source observatory control software

**原文标题**: Astra: An open-source observatory control software

**原文链接**: [https://github.com/ppp-one/astra](https://github.com/ppp-one/astra)

生成摘要时出错

---

## 64. 10% of Firefox crashes are caused by bitflips

**原文标题**: 10% of Firefox crashes are caused by bitflips

**原文链接**: [https://mas.to/@gabrielesvelto/116171750653898304](https://mas.to/@gabrielesvelto/116171750653898304)

生成摘要时出错

---

## 65. Maybe there's a pattern here?

**原文标题**: Maybe there's a pattern here?

**原文链接**: [https://dynomight.net/pattern/](https://dynomight.net/pattern/)

生成摘要时出错

---

## 66. Paul Brainerd, founder of Aldus PageMaker, has died

**原文标题**: Paul Brainerd, founder of Aldus PageMaker, has died

**原文链接**: [https://blog.adafruit.com/2026/03/04/pagemaker-and-aldus-founder-pioneer-paul-brainerd-1947-2026/](https://blog.adafruit.com/2026/03/04/pagemaker-and-aldus-founder-pioneer-paul-brainerd-1947-2026/)

生成摘要时出错

---

## 67. Show HN: OculOS – Any desktop app as a JSON API via OS accessibility tree

**原文标题**: Show HN: OculOS – Any desktop app as a JSON API via OS accessibility tree

**原文链接**: [https://github.com/huseyinstif/oculos](https://github.com/huseyinstif/oculos)

生成摘要时出错

---

## 68. A Modular Robot Dashboard

**原文标题**: A Modular Robot Dashboard

**原文链接**: [https://github.com/transitiverobotics/transact](https://github.com/transitiverobotics/transact)

生成摘要时出错

---

## 69. The shady world of IP leasing

**原文标题**: The shady world of IP leasing

**原文链接**: [https://acid.vegas/blog/the-shady-world-of-ip-leasing/](https://acid.vegas/blog/the-shady-world-of-ip-leasing/)

生成摘要时出错

---

## 70. 70k Books Found in Hidden Library in This Germany Home (2023)

**原文标题**: 70k Books Found in Hidden Library in This Germany Home (2023)

**原文链接**: [https://bookstr.com/article/70k-books-found-in-hidden-library-in-this-germany-home/](https://bookstr.com/article/70k-books-found-in-hidden-library-in-this-germany-home/)

生成摘要时出错

---

## 71. Fork Off: Surveillance States Need to Fork Linux Themselves

**原文标题**: Fork Off: Surveillance States Need to Fork Linux Themselves

**原文链接**: [https://blog.devrupt.io/posts/fork-off-california-linux/](https://blog.devrupt.io/posts/fork-off-california-linux/)

生成摘要时出错

---

## 72. LibreSprite – open-source pixel art editor

**原文标题**: LibreSprite – open-source pixel art editor

**原文链接**: [https://libresprite.github.io/](https://libresprite.github.io/)

生成摘要时出错

---

## 73. Show HN: Reconstruct any image using primitive shapes, runs in-browser via WASM

**原文标题**: Show HN: Reconstruct any image using primitive shapes, runs in-browser via WASM

**原文链接**: [https://github.com/taiseiue/primitive-playground](https://github.com/taiseiue/primitive-playground)

生成摘要时出错

---

## 74. C# strings silently kill your SQL Server indexes in Dapper

**原文标题**: C# strings silently kill your SQL Server indexes in Dapper

**原文链接**: [https://consultwithgriff.com/dapper-nvarchar-implicit-conversion-performance-trap](https://consultwithgriff.com/dapper-nvarchar-implicit-conversion-performance-trap)

生成摘要时出错

---

## 75. Anthropic, please make a new Slack

**原文标题**: Anthropic, please make a new Slack

**原文链接**: [https://www.fivetran.com/blog/anthropic-please-make-a-new-slack](https://www.fivetran.com/blog/anthropic-please-make-a-new-slack)

生成摘要时出错

---

## 76. Art Bits from HyperCard

**原文标题**: Art Bits from HyperCard

**原文链接**: [https://archives.somnolescent.net/web/mari_v2/junk/hypercard/](https://archives.somnolescent.net/web/mari_v2/junk/hypercard/)

生成摘要时出错

---

## 77. MacBook Neo

**原文标题**: MacBook Neo

**原文链接**: [https://www.apple.com/newsroom/2026/03/say-hello-to-macbook-neo/](https://www.apple.com/newsroom/2026/03/say-hello-to-macbook-neo/)

生成摘要时出错

---

## 78. Htmx Infinite Scroll

**原文标题**: Htmx Infinite Scroll

**原文链接**: [https://alchemists.io/articles/htmx_infinite_scroll](https://alchemists.io/articles/htmx_infinite_scroll)

生成摘要时出错

---

## 79. Game about Data of America

**原文标题**: Game about Data of America

**原文链接**: [https://americaindata.com/](https://americaindata.com/)

生成摘要时出错

---

## 80. Doomscroll 14,333 cat pictures

**原文标题**: Doomscroll 14,333 cat pictures

**原文链接**: [https://cat.aadishv.dev/](https://cat.aadishv.dev/)

生成摘要时出错

---

## 81. We might all be AI engineers now

**原文标题**: We might all be AI engineers now

**原文链接**: [https://yasint.dev/we-might-all-be-ai-engineers-now/](https://yasint.dev/we-might-all-be-ai-engineers-now/)

生成摘要时出错

---

## 82. A GitHub Issue Title Compromised 4k Developer Machines

**原文标题**: A GitHub Issue Title Compromised 4k Developer Machines

**原文链接**: [https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another](https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another)

生成摘要时出错

---

## 83. Claude's Cycles [pdf]

**原文标题**: Claude's Cycles [pdf]

**原文链接**: [https://www-cs-faculty.stanford.edu/~knuth/papers/claude-cycles.pdf](https://www-cs-faculty.stanford.edu/~knuth/papers/claude-cycles.pdf)

生成摘要时出错

---

## 84. My dad made the biggest jewelled egg in the world

**原文标题**: My dad made the biggest jewelled egg in the world

**原文链接**: [https://www.theguardian.com/books/2026/mar/07/paul-kutchinsky-egg-obsession-destroy-marriage-family-fortune](https://www.theguardian.com/books/2026/mar/07/paul-kutchinsky-egg-obsession-destroy-marriage-family-fortune)

生成摘要时出错

---

## 85. From Fargo to Zebra

**原文标题**: From Fargo to Zebra

**原文链接**: [https://cendyne.dev/posts/2026-02-27-from-fargo-to-zebra.html](https://cendyne.dev/posts/2026-02-27-from-fargo-to-zebra.html)

生成摘要时出错

---

## 86. Poor Man's Polaroid

**原文标题**: Poor Man's Polaroid

**原文链接**: [https://boxart.lt/blog/poor_mans_polaroid?locale=en](https://boxart.lt/blog/poor_mans_polaroid?locale=en)

生成摘要时出错

---

## 87. Linux 7.0 File-System Benchmarks

**原文标题**: Linux 7.0 File-System Benchmarks

**原文链接**: [https://www.phoronix.com/review/linux-70-filesystems](https://www.phoronix.com/review/linux-70-filesystems)

生成摘要时出错

---

## 88. Pentagon Refuses to Say If AI Was Used to Bomb Elementary School

**原文标题**: Pentagon Refuses to Say If AI Was Used to Bomb Elementary School

**原文链接**: [https://futurism.com/artificial-intelligence/pentagon-ai-claude-bombing-elementary-school](https://futurism.com/artificial-intelligence/pentagon-ai-claude-bombing-elementary-school)

生成摘要时出错

---

## 89. The Brand Age

**原文标题**: The Brand Age

**原文链接**: [https://paulgraham.com/brandage.html](https://paulgraham.com/brandage.html)

生成摘要时出错

---

## 90. Google Workspace CLI

**原文标题**: Google Workspace CLI

**原文链接**: [https://github.com/googleworkspace/cli](https://github.com/googleworkspace/cli)

生成摘要时出错

---

## 91. Polar Factor Beyond Newton-Schulz – Fast Matrix Inverse Square Root

**原文标题**: Polar Factor Beyond Newton-Schulz – Fast Matrix Inverse Square Root

**原文链接**: [https://jiha-kim.github.io/posts/polar-factor-beyond-newton-schulz-fast-matrix-inverse-square-root/](https://jiha-kim.github.io/posts/polar-factor-beyond-newton-schulz-fast-matrix-inverse-square-root/)

生成摘要时出错

---

## 92. Supertoast tables

**原文标题**: Supertoast tables

**原文链接**: [https://hatchet.run/blog/supertoast-tables](https://hatchet.run/blog/supertoast-tables)

生成摘要时出错

---

## 93. The disappearing Form D (2018)

**原文标题**: The disappearing Form D (2018)

**原文链接**: [https://techcrunch.com/2018/11/07/the-disappearing-form-d/](https://techcrunch.com/2018/11/07/the-disappearing-form-d/)

生成摘要时出错

---

## 94. Cameras built to police Iranians became the regime's Achilles' heel

**原文标题**: Cameras built to police Iranians became the regime's Achilles' heel

**原文链接**: [https://royapakzad.substack.com/p/youre-welcome-mr-supreme-leader](https://royapakzad.substack.com/p/youre-welcome-mr-supreme-leader)

生成摘要时出错

---

## 95. How to install and start using LineageOS on your phone

**原文标题**: How to install and start using LineageOS on your phone

**原文链接**: [https://lockywolf.net/2026-02-19_How-to-install-and-start-using-LineageOS-on-your-phone.d/index.html](https://lockywolf.net/2026-02-19_How-to-install-and-start-using-LineageOS-on-your-phone.d/index.html)

生成摘要时出错

---

## 96. Motorola GrapheneOS devices will be bootloader unlockable/relockable

**原文标题**: Motorola GrapheneOS devices will be bootloader unlockable/relockable

**原文链接**: [https://grapheneos.social/@GrapheneOS/116160393783585567](https://grapheneos.social/@GrapheneOS/116160393783585567)

生成摘要时出错

---

## 97. Good software knows when to stop

**原文标题**: Good software knows when to stop

**原文链接**: [https://ogirardot.writizzy.com/p/good-software-knows-when-to-stop](https://ogirardot.writizzy.com/p/good-software-knows-when-to-stop)

生成摘要时出错

---

## 98. Show HN: A trainable, modular electronic nose for industrial use

**原文标题**: Show HN: A trainable, modular electronic nose for industrial use

**原文链接**: [https://sniphi.com/](https://sniphi.com/)

生成摘要时出错

---

## 99. TypeScript 6.0 RC

**原文标题**: TypeScript 6.0 RC

**原文链接**: [https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/](https://devblogs.microsoft.com/typescript/announcing-typescript-6-0-rc/)

生成摘要时出错

---

## 100. Dulce et Decorum Est (1921)

**原文标题**: Dulce et Decorum Est (1921)

**原文链接**: [https://www.poetryfoundation.org/poems/46560/dulce-et-decorum-est](https://www.poetryfoundation.org/poems/46560/dulce-et-decorum-est)

生成摘要时出错

---

