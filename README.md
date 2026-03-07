# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-07.md)

*最后自动更新时间: 2026-03-07 17:53:00*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 2 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 3 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 4 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 5 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 6 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 7 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 8 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 9 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 10 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 11 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 12 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 13 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 14 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 15 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 16 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 17 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 18 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 19 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 20 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 21 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 22 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 23 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 24 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 25 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 26 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 27 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 28 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 29 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 30 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 31 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 32 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 33 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 34 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 35 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 36 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 37 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 38 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 39 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 40 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 41 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 42 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 43 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 44 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 45 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 46 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 47 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 48 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 49 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 50 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 51 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 52 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 53 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 54 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 55 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 56 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 57 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 58 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 59 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 60 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 61 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 62 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 63 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 64 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 65 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 66 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 67 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 68 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 69 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 70 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 71 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 72 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 73 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 74 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 75 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 76 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 77 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 78 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 79 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 80 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 81 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 82 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 83 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 84 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 85 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 86 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 87 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 88 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 89 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 90 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 91 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 92 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 93 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 94 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 95 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 96 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 97 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 98 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 99 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 100 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 101 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 102 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 103 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 104 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 105 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 106 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 107 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 108 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 109 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 110 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 111 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 112 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 113 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 114 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 115 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 116 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 117 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 118 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 119 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 120 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 121 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 122 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 123 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 124 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 125 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 126 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 127 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 128 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 129 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 130 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 131 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 132 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 133 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 134 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 135 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 136 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 137 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 138 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 139 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 140 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 141 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 142 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 143 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 144 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 145 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 146 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 147 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 148 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 149 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 150 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 151 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 152 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 153 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 154 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 155 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 156 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 157 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 158 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 159 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 160 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 161 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 162 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 163 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 164 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 165 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 166 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 167 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 168 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 169 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 170 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 171 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 172 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 173 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 174 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 175 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 176 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 177 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 178 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 179 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 180 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 181 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 182 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 183 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 184 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 185 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 186 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 187 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 188 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 189 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 190 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 191 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 192 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 193 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 194 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 195 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 196 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 197 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 198 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 199 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 200 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 201 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 202 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 203 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 204 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 205 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 206 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 207 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 208 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 209 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 210 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 211 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 212 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 213 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 214 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 215 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 216 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 217 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 218 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 219 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 220 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 221 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 222 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 223 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 224 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 225 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 226 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 227 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 228 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 229 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 230 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 231 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 232 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 233 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 234 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 235 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 236 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 237 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 238 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 239 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 240 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 241 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 242 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 243 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 244 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 245 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 246 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 247 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 248 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 249 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 250 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 251 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 252 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 253 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 254 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 255 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 256 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 257 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 258 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 259 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 260 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 261 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 262 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 263 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 264 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 265 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 266 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 267 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 268 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 269 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 270 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 271 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 272 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 273 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 274 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 275 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 276 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 277 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 278 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 279 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 280 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 281 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 282 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 283 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 284 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 285 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 286 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 287 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 288 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 289 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 290 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 291 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 292 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 293 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 294 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 295 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 296 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 297 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 298 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 299 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 300 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 301 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 302 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 303 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 304 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 305 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 306 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 307 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 308 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 309 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 310 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 311 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 312 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 313 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 314 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 315 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 316 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 317 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 318 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 319 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 320 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 321 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 322 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 323 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 324 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 325 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 326 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 327 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 328 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 329 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 330 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 331 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 332 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 333 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 334 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 335 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 336 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 337 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 338 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 339 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 340 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 341 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 342 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 343 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 344 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 345 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 346 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 347 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 348 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 349 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 350 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 351 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 352 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
