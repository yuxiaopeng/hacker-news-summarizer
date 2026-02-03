# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-03.md)

*最后自动更新时间: 2026-02-03 18:19:33*
## 1. Qwen3-Coder-Next

**原文标题**: Qwen3-Coder-Next

**原文链接**: [https://qwen.ai/blog?id=qwen3-coder-next](https://qwen.ai/blog?id=qwen3-coder-next)

所提供的文本标题为“Qwen3-Coder-Next”，内容仅包含“Qwen”一词。由于没有实质性的正文，无法从“文章”本身提取具体信息进行摘要。

然而，根据标题可以推断，这指的是备受期待的阿里云通义千问（Qwen）模型中专为编程优化的下一代迭代版本。在目前的 Qwen2.5-Coder 系列基础上，“Qwen3”继任者可能会重点关注：

*   **增强的推理能力：** 提升应对复杂调试和架构规划的逻辑能力。
*   **更广泛的语言支持：** 在更多编程语言和框架中实现更精细的表现。
*   **更长的上下文窗口：** 能够同时处理并理解更大规模的代码库或整个仓库。
*   **顶尖的基准测试表现：** 旨在超越现有的开源及商业编程助手。

如果您有需要摘要的文章全文，请提供，我将竭诚为您服务。

---

## 2. 智能体技能

**原文标题**: Agent Skills

**原文链接**: [https://agentskills.io/home](https://agentskills.io/home)

**智能体技能 (Agent Skills)** 是由指令、脚本和资源组成的标准化包，旨在为 AI 智能体提供执行特定任务所需的上下文和过程性知识，从而提高其任务执行的准确性。通过弥合通用智能与专业化工作之间的差距，这些技能使智能体能够按需加载特定的能力，例如数据分析、法律审查或工作流自动化。

该框架为不同的利益相关者带来了显著优势：
*   **技能作者：** 开发者只需构建一次能力，即可将其部署到多个兼容智能体交互的产品中。
*   **AI 智能体：** 兼容的智能体针对构建服务器或制作演示文稿等复杂任务，可获得即插即用的功能。
*   **企业：** 组织可以通过便携、可重用的包来沉淀、进行版本控制并共享专有知识。

除了提供领域专业知识外，智能体技能还支持可重复、可审计的工作流和跨平台互操作性。这确保了无论使用哪种特定的智能体工具，同一种技能都能保持一致的功能。

智能体技能最初由 **Anthropic** 开发，现已作为开放标准发布。目前，它已获得领先 AI 开发工具的支持，并向社区贡献开放。开发者和组织可以通过 GitHub 上的 **SKILL.md** 规范和参考库开始使用。

---

## 3. Deno 沙盒

**原文标题**: Deno Sandbox

**原文链接**: [https://deno.com/blog/introducing-deno-sandbox](https://deno.com/blog/introducing-deno-sandbox)

Deno 推出了 Deno Sandbox，这是一个专为应对运行 LLM 生成代码所带来的独特风险而设计的安全执行环境。该服务目前处于测试阶段，提供启动时间不到一秒的轻量级 Linux 微型虚拟机 (microVMs)，为需要网络访问和 API 凭据的不可信脚本提供了一种“深度防御”方案。

该沙箱的一项核心创新是其**机密管理系统**。代码看到的只是占位符，而非暴露在环境中的真实 API 密钥。只有当沙箱向预先批准的主机发起出站请求时，实际凭据才会显现，从而有效防止遭受提示词注入攻击的代码窃取敏感密钥。与之相辅相成的是**网络出口控制**，允许开发人员将虚拟机级别的通信限制在特定域名内。

关键特性和技术细节包括：
*   **开发者体验：** 可通过 JavaScript 或 Python SDK 管理沙箱，并支持通过 SSH、HTTP 或直接的 VS Code 集成进行交互。
*   **无缝部署：** `sandbox.deploy()` 函数允许用户将代码直接从沙箱迁移到 Deno Deploy 上生产就绪、自动扩缩容的无服务器环境，无需重新构建。
*   **持久化：** 支持读写**卷 (Volumes)** 和只读**快照 (Snapshots)**，从而支持预装工具链和持久化状态。
*   **规格：** 实例提供 2 个 vCPU 和高达 4GB 的内存，最长运行时间为 30 分钟。

Deno Sandbox 已包含在 Deno Deploy 计划中，采用按需计费模式（CPU 时间 0.05 美元/小时，内存 0.016 美元/GB-小时）。它针对 AI 代理、安全插件系统和临时 CI 运行器进行了优化。此公告发布之际，正值 Deno Deploy 正式商用 (GA)。

---

## 4. Prek：更出色、更快速、可无缝替换的 pre-commit 替代方案，由 Rust 打造

**原文标题**: Prek: A better, faster, drop-in pre-commit replacement, engineered in Rust

**原文链接**: [https://github.com/j178/prek](https://github.com/j178/prek)

**Prek** 是基于 Rust 构建的高性能替代品，旨在取代流行的 `pre-commit` 框架。作为一种更快速、无依赖的“无缝替换”方案，它通过提供单一的独立二进制文件，消除了对 Python 运行时的需求。尽管这是一个相对较新的工具，但它已在行业内得到广泛应用，为 CPython、Apache Airflow、FastAPI 和 Ruff 等重大项目提供支持。

Prek 的主要优势包括：

*   **性能与效率：** Prek 的速度显著快于原版工具，支持并行克隆和钩子（hook）执行。它通过在不同钩子间共享工具链和依赖项而非重复创建，有效减少了磁盘占用。
*   **增强的功能：** 它引入了内置的单体仓库（monorepo/workspace）支持、常用钩子的原生 Rust 实现，以及与 `uv` 的无缝集成，从而实现极速的 Python 环境管理。
*   **提升的用户体验：** 其命令行界面（CLI）提供了高级功能，例如在特定目录上运行钩子、按最后一次提交进行过滤以及 Shell 自动补全。它还包含用于提高配置可见性的 `prek list` 命令和 `self update` 自动更新功能。

虽然 Prek 旨在完全兼容现有的 `.pre-commit-config.yaml` 文件，但某些特定语言的功能仍处于对齐阶段。安装方式极其灵活，支持几乎所有主流包管理器——包括 Homebrew、PyPI、npm、Nix、Conda 和 Cargo——以及适用于 Linux、macOS 和 Windows 的独立脚本。Prek 深受原版 `pre-commit` 和 Astral 的 `uv` 启发，代表了 pre-commit 工作流的一次现代化、优化后的演进。

---

## 5. 那些等号到底是怎么回事？

**原文标题**: What's up with all those equals signs anyway?

**原文链接**: [https://lars.ingebrigtsen.no/2026/02/02/whats-up-with-all-those-equals-signs-anyway/](https://lars.ingebrigtsen.no/2026/02/02/whats-up-with-all-those-equals-signs-anyway/)

本文解释道，最近曝光的旧邮件摘要中出现的大量等号（=）既不是秘密代码，也不是 OCR 错误。相反，它是 Quoted-Printable 编码产生的技术痕迹，这种编码方法旨在确保邮件能顺利通过那些难以处理长行或特殊字符的旧式邮件服务器。

作者强调了文中出现这些等号的两个主要原因：

1.  **软换行（Soft Line Breaks）：** 为了防止传输错误，邮件软件会通过插入一个等号，后接回车符和换行符（CRLF）来折断长文本行。合格的邮件阅读器应当去除这些字符以还原原始行。然而，作者认为这些特定的邮件在解码前，很可能已从 Windows 风格的换行符（CRLF）被转换成了 Unix 风格（NL）。这导致解码算法失效，从而留下了等号。
2.  **特殊字符编码：** 等号还用于对非 ASCII 字符进行编码，例如不换行空格（如 `=C2=A0`）。在泄露的邮件中出现这些符号，是因为处理数据时使用了不当工具——很可能是简单的搜索替换方法——而非专业的邮件解码器。

最终，作者得出结论，这些邮件之所以显得“凌乱”，是“垃圾进，垃圾出（garbage in, garbage out）”的结果。处理和转换这些存档的人员可能极不专业，使用了带有漏洞或不恰当的算法，未能考虑到传统邮件标准的技术细节。

---

## 6. 法国弃用 Zoom 和 Teams，欧洲力求实现对美数字自主。

**原文标题**: France dumps Zoom and Teams as Europe seeks digital autonomy from the US

**原文链接**: [https://apnews.com/article/europe-digital-sovereignty-big-tech-9f5388b68a0648514cebc8d92f682060](https://apnews.com/article/europe-digital-sovereignty-big-tech-9f5388b68a0648514cebc8d92f682060)

欧洲各国政府正在加速转向“数字主权”，寻求利用本土或开源替代方案取代美国科技巨头的服务。受安全担忧和地缘政治紧张局势推动，法国、德国和奥地利等国正致力于减少对微软（Microsoft）、Zoom和谷歌（Google）等美国供应商的依赖。

**主要进展：**
*   **法国：** 政府宣布，到2027年，250万名公务员将从美国的视频会议工具（Zoom、Teams、Webex）转向名为“Visio”的本土平台，以确保数据机密性。
*   **区域性转变：** 奥地利军队和德国石勒苏益格-荷尔斯泰因州已采用 LibreOffice 和 Nextcloud 等开源软件。丹麦及意大利的多个城市也在探索类似的“独立于供应商”的解决方案。

**驱动因素：**
*   **地缘政治脆弱性：** 特朗普政府的“强硬”姿态加剧了人们对美国技术可能被用作政治杠杆的担忧。一个关键时刻是，在遭受美国制裁后，微软断开了国际刑事法院检察官的电子邮件连接，这引发了人们对关键基础设施可能面临“远程切断”的恐惧。
*   **数据隐私：** 对美国监控和云端托管数据安全性的持续担忧，使得由欧洲控制的“主权云”成为优先事项。
*   **战略自主：** 欧洲领导人认为，依赖包括埃隆·马斯克的“星链”（Starlink）在内的少数外国实体，会危及欧洲大陆独立行动的能力。

尽管微软等美国公司强调其对欧洲数据驻留和当地合作伙伴关系的承诺，但欧洲的“时代思潮”已发生转变。向开源和本土软件的转型最初主要受成本驱动，而现在则被视为防止外部胁迫和保护敏感创新的战略必然。

---

## 7. 定义安全硬件设计 [pdf]

**原文标题**: Defining Safe Hardware Design [pdf]

**原文链接**: [https://people.csail.mit.edu/rachit/files/pubs/safe-hdls.pdf](https://people.csail.mit.edu/rachit/files/pubs/safe-hdls.pdf)

This article, **"Defining Safe Hardware Design"** by Rachit Nigam (published via the ACM), addresses the critical lack of a unified, formal definition for "safety" within the context of Hardware Description Languages (HDLs). While software engineering has long benefited from established concepts like "memory safety," hardware design—despite its higher cost of failure—has lacked a similar foundational framework to prevent common design errors at compile-time.

The article identifies three primary pillars that constitute safe hardware design:

1.  **Structural Safety:** This ensures that components are composed correctly, preventing issues such as multiple drivers on a single wire or unconnected ports.
2.  **Timing and Interface Safety:** A central focus of the paper, this property ensures that data is only consumed when it is valid and produced according to a strict temporal contract. It aims to eliminate bugs caused by "garbage" data being read before a computation is complete or after a signal has lapsed.
3.  **Resource Safety:** This involves preventing resource contention, ensuring that two different parts of a design do not attempt to use the same physical hardware resource (such as a specific multiplier or memory port) at the same time.

Nigam argues that traditional HDLs like Verilog and VHDL are too low-level to catch these errors statically. The article proposes that the next generation of hardware design tools should utilize **advanced type systems**—drawing inspiration from languages like Filament and Calyx—to bake these safety properties into the compiler. 

By formally defining these safety constraints, the work provides a roadmap for shifting hardware verification "to the left." This allows designers to catch complex temporal and structural bugs during the initial design phase rather than relying on expensive post-silicon testing or exhaustive simulation. Ultimately, the paper advocates for a design philosophy where hardware components are treated as typed abstractions with strict, checkable temporal contracts.

---

## 8. Kilobyte is precisely 1000 bytes

**原文标题**: Kilobyte is precisely 1000 bytes

**原文链接**: [https://waspdev.com/articles/2026-01-11/kilobyte-is-1000-bytes](https://waspdev.com/articles/2026-01-11/kilobyte-is-1000-bytes)

生成摘要时出错

---

## 9. Heritability of intrinsic human life span is about 50%

**原文标题**: Heritability of intrinsic human life span is about 50%

**原文链接**: [https://www.science.org/doi/10.1126/science.adz1187](https://www.science.org/doi/10.1126/science.adz1187)

生成摘要时出错

---

## 10. Bunny Database

**原文标题**: Bunny Database

**原文链接**: [https://bunny.net/blog/meet-bunny-database-the-sql-service-that-just-works/](https://bunny.net/blog/meet-bunny-database-the-sql-service-that-just-works/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 2 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 3 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 4 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 5 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 6 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 7 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 8 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 9 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 10 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 11 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 12 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 13 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 14 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 15 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 16 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 17 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 18 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 19 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 20 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 21 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 22 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 23 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 24 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 25 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 26 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 27 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 28 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 29 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 30 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 31 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 32 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 33 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 34 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 35 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 36 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 37 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 38 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 39 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 40 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 41 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 42 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 43 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 44 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 45 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 46 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 47 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 48 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 49 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 50 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 51 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 52 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 53 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 54 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 55 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 56 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 57 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 58 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 59 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 60 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 61 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 62 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 63 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 64 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 65 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 66 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 67 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 68 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 69 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 70 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 71 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 72 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 73 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 74 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 75 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 76 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 77 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 78 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 79 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 80 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 81 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 82 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 83 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 84 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 85 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 86 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 87 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 88 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 89 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 90 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 91 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 92 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 93 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 94 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 95 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 96 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 97 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 98 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 99 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 100 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 101 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 102 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 103 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 104 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 105 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 106 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 107 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 108 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 109 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 110 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 111 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 112 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 113 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 114 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 115 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 116 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 117 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 118 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 119 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 120 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 121 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 122 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 123 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 124 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 125 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 126 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 127 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 128 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 129 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 130 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 131 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 132 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 133 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 134 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 135 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 136 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 137 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 138 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 139 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 140 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 141 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 142 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 143 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 144 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 145 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 146 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 147 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 148 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 149 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 150 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 151 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 152 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 153 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 154 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 155 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 156 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 157 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 158 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 159 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 160 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 161 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 162 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 163 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 164 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 165 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 166 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 167 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 168 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 169 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 170 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 171 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 172 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 173 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 174 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 175 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 176 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 177 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 178 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 179 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 180 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 181 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 182 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 183 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 184 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 185 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 186 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 187 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 188 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 189 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 190 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 191 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 192 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 193 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 194 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 195 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 196 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 197 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 198 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 199 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 200 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 201 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 202 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 203 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 204 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 205 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 206 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 207 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 208 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 209 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 210 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 211 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 212 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 213 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 214 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 215 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 216 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 217 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 218 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 219 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 220 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 221 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 222 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 223 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 224 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 225 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 226 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 227 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 228 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 229 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 230 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 231 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 232 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 233 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 234 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 235 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 236 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 237 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 238 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 239 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 240 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 241 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 242 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 243 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 244 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 245 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 246 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 247 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 248 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 249 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 250 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 251 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 252 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 253 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 254 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 255 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 256 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 257 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 258 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 259 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 260 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 261 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 262 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 263 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 264 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 265 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 266 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 267 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 268 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 269 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 270 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 271 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 272 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 273 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 274 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 275 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 276 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 277 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 278 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 279 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 280 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 281 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 282 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 283 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 284 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 285 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 286 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 287 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 288 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 289 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 290 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 291 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 292 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 293 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 294 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 295 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 296 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 297 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 298 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 299 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 300 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 301 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 302 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 303 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 304 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 305 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 306 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 307 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 308 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 309 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 310 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 311 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 312 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 313 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 314 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 315 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 316 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 317 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 318 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 319 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 320 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
