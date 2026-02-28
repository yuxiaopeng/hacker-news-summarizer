# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-02-28.md)

*最后自动更新时间: 2026-02-28 17:49:48*
## 1. 认知债：当速度超越理解

**原文标题**: Cognitive Debt: When Velocity Exceeds Comprehension

**原文链接**: [https://www.rockoder.com/beyondthecode/cognitive-debt-when-velocity-exceeds-comprehension/](https://www.rockoder.com/beyondthecode/cognitive-debt-when-velocity-exceeds-comprehension/)

《认知债：当速率超过理解》探讨了 AI 辅助代码生成的产出速度与人类理解能力之间日益加剧的脱节。传统上，手动编码的摩擦力迫使工程师形成深刻的心智模型；而 AI 将这些过程剥离，实现了远超人类“吸收速率”的高速产出。

文章将**认知债（Cognitive Debt）**定义为产出与理解之间的差距。这种债务在 DORA 或故事点（story points）等传统指标中是不可见的，因为这些指标默认交付功能即代表理解功能。这导致了以下几个系统性问题：

*   **评审者的困境：** AI 使初级工程师生成代码的速度超过了高级工程师严谨审计的速度。为了维持开发速率，评审深度往往被牺牲，导致未经验证的代码不断扩散。
*   **新的倦怠模式：** 工程师正经历“认知断连”——一种高产出但低信心的状态，他们对自己亲手完成的工作感到陌生。
*   **隐性知识的侵蚀：** 由于绕过了通过手动解决问题而形成的“疤痕组织”，组织无法积累长期维护所需的隐性知识。这造成了“黑盒”效应，即无人真正理解系统。
*   **领导力断层：** 未来的高级架构师难以成长，因为建立架构直觉所需的磨练过程正在被自动化取代。

核心问题在于衡量体系：工程绩效系统奖励可见的速率，却忽视了理解力。由于领导者倾向于优化可见的指标，他们在无意中激励了认知债的积累。作者警告称，这种债务最终会表现为故障恢复时间的延长和架构的脆弱性，这预示着我们当前的指标仍停留在“产出与理解高度耦合”的旧时代，而那个时代已不复存在。

---

## 2. Obsidian Sync 现已支持无头客户端

**原文标题**: Obsidian Sync now has a headless client

**原文链接**: [https://help.obsidian.md/sync/headless](https://help.obsidian.md/sync/headless)

Obsidian 为其同步服务推出了**无头客户端 (headless client)**，提供了一个命令行界面 (CLI)，允许用户在不运行图形化 Obsidian 应用程序的情况下同步他们的库 (vaults)。该工具主要面向高级用户、开发者和系统管理员。

**核心功能与使用场景：**
*   **服务器集成：** 非常适合在私有服务器、NAS 或树莓派等通常没有图形界面 (GUI) 的设备上维护库的同步副本。
*   **自动化与工作流：** 无头客户端支持自动备份、Web 发布流水线以及与其他服务器端脚本的集成。
*   **高效能：** 由于去除了图形界面，它占用的系统资源远少于标准桌面端应用。
*   **跨平台支持：** 二进制文件适用于 Linux (x64 和 ARM64) 以及 macOS。

**运行细节：**
*   **

对于希望将笔记纳入更大规模、自动化数据生态系统，同时又想保持官方同步服务私密性与可靠性的 Obsidian 用户来说，此次更新是一个重要的里程碑。

---

## 3. Woxi：Wolfram Mathematica 的 Rust 重新实现

**原文标题**: Woxi: Wolfram Mathematica Reimplementation in Rust

**原文链接**: [https://github.com/ad-si/Woxi](https://github.com/ad-si/Woxi)

生成摘要时出错

---

## 4. 处理反重力禁令并恢复访问权限

**原文标题**: Addressing Antigravity Bans and Reinstating Access

**原文链接**: [https://github.com/google-gemini/gemini-cli/discussions/20632](https://github.com/google-gemini/gemini-cli/discussions/20632)

2026年2月27日，Gemini CLI 维护者宣布解决了由“Antigravity 封禁”引起的大规模账号中断问题。这些封禁是由于违反服务条款（ToS）触发的，具体表现为通过 Gemini CLI 的身份验证，使用第三方工具或代理来访问 Antigravity 的资源和配额。

为解决该问题，谷歌实施了全系统重置，恢复了近期被标记账号的访问权限。今后，一种全新的自服务恢复流程将取代通用的封锁措施。因违反服务条款而被标记的用户将收到通知，引导其填写重新认证表。在正式承认禁止绕过系统措施或使用限制后，账号将自动恢复。然而，该政策严格指出，第二次违规将导致永久封禁。

公告明确澄清，使用第三方软件“搭便车”利用 Gemini CLI 的 OAuth 身份验证属于直接违规行为。

社区对该公告的反应褒贬不一：
*   **认可：** 一些用户称赞了向更好沟通以及“更公平”的自动化修复路径的转变。
*   **条款模糊：** 评论者要求对禁止使用的工具给出更清晰的定义，特别是询问开源分支或用量监控工具（如 OpenUsage）是否在封禁之列。
*   **账号风险：** 一个主要的争论点是谷歌账号“全有或全无”的特性。用户担心因 Gemini 相关的违规行为，可能导致失去对 Gmail 等核心服务的访问权限。
*   **透明度：** 一些用户认为，由于缺乏官方且透明的配额监控工具，迫使他们不得不依赖谷歌正在封禁的第三方软件。

总的来说，虽然此次更新为解封用户提供了途径，但社区对于使用谷歌服务进行开发的风险以及缺乏细粒度的账号保护仍深感忧虑。

---

## 5. 盗取无穷的人

**原文标题**: A Man Who Stole Infinity

**原文链接**: [https://www.quantamagazine.org/the-man-who-stole-infinity-20260225/](https://www.quantamagazine.org/the-man-who-stole-infinity-20260225/)

在《窃取无穷的人》一文中，约瑟夫·霍利特详细阐述了一项挑战格奥尔格·康托尔历史地位的发现。康托尔一直被公认为证明了无穷大具有不同规模的数学家。尽管康托尔1874年的论文被视为现代数学和集合论的基石，但新披露的通信往来表明，这项工作可能涉及对他同事理查德·戴德金的剽窃。

这一发现由哈雷大学的数学家兼记者德米安·古斯做出。古斯发现了一封此前“遗失”的、日期为1873年11月30日的信件，该信提供的证据表明，康托尔的突破性进展很大程度上依赖于戴德金的洞见。文章追溯了两人的关系，这段关系始于1872年，当时他们各自独立发表论文，将数轴重新定义为连续且“完备”的整体。尽管两人性格迥异——康托尔喧闹且焦虑，戴德金则内敛而严谨——但他们建立了紧密的智识伙伴关系。

在一种坚信理解无穷是神圣使命的宗教信念驱动下，康托尔痴迷于实数的无穷是否大于整数的无穷。他试图确定这两个集合是否可以建立“一一对应”关系。尽管长期以来，历史一直将康托尔描绘成一位在同行排挤下独立变革数学的孤胆天才，但这封1873年的信件表明，他的里程碑式证明可能未注明来源，甚至是窃取自戴德金。通过揭示这段隐秘的历史，古斯旨在纠正关于无穷如何演变为严谨数学现实的叙事，从而告别将康托尔视为集合论唯一缔造者的“错误故事”。

---

## 6. 验证规格驱动开发 (VSDD)

**原文标题**: Verified Spec-Driven Development (VSDD)

**原文链接**: [https://gist.github.com/dollspace-gay/d8d3bc3ecf4188df049d7a4726bb2a00](https://gist.github.com/dollspace-gay/d8d3bc3ecf4188df049d7a4726bb2a00)

**验证化规格驱动开发 (Verified Spec-Driven Development, VSDD)** 是一种高完整性的 AI 原生工程方法论，它将规格驱动开发 (SDD)、测试驱动开发 (TDD) 和验证驱动开发 (VDD) 融为一体。在人类的战略监督下，VSDD 由 AI “构建者” (Builders) 和 “对抗者” (Adversaries) 协同编排，旨在生产每一行代码在数学和逻辑上均有据可依的“零冗余 (Zero-Slop)”软件。

VSDD 流水线由六个主要阶段组成：

1.  **规格晶化 (Spec Crystallization)：** 在编码之前，构建者 AI 定义功能契约和**验证架构**。这确保了“纯粹核心”（确定性逻辑）与“有副作用的外壳”（I/O）相分离，从而使系统具备形式化可验证性。
2.  **TDD 核心：** 遵循严格的“红-绿-重构”纪律，AI 为每个规格需求和边缘情况编写可执行测试。在失败的测试提出要求之前，不允许编写任何实现代码。
3.  **对抗性精炼 (Adversarial Refinement)：** 一个全新的、极度挑剔的 AI “对抗者” (Sarcasmotron) 会对规格、测试和代码进行严厉评审，以发现歧义、隐藏的技术债务或安全漏洞。
4.  **反馈循环 (Feedback Loop)：** 对抗者发现或测试过程中暴露出的任何缺陷，都会触发返回规格或实现阶段的迭代。
5.  **形式化加固 (Formal Hardening)：** 对“纯粹核心”应用形式化验证工具（如 Kani、TLA+ 或 Dafny）及模糊测试。这验证了标准测试可能遗漏的不变量和安全属性。
6.  **收敛 (Convergence)：** 只有当对抗者无法再发现合理缺陷，且所有形式化证明均通过时，流程才会结束。

VSDD 的核心优势是**全链路可追溯性**。每一个架构决策和每一行代码都通过“契约链”相连——从最初的规格需求，经过具体的测试用例和对抗性评审，直至最终的形式化证明。通过优先构建验证优先的架构，VSDD 确保了软件不仅是“可运行”的，而且是可证明正确的。

---

## 7. Show HN：适用于 Rivet Actors 的 SQLite —— 每个智能体、租户或文档一个数据库

**原文标题**: Show HN: SQLite for Rivet Actors – one database per agent, tenant, or document

**原文链接**: [https://github.com/rivet-dev/rivet](https://github.com/rivet-dev/rivet)

Rivet Actors 是一种为有状态工作负载设计的新型无服务器原语（Serverless Primitive），实现了“每个实体一个数据库”的架构。通过为每个智能体、租户或文档分配专用的 Actor，开发者可以将计算与存储同地部署，从而构建低延迟、高可扩展的应用程序。

**核心功能**
每个 Rivet Actor 都是一个自包含的微服务，内置以下功能：
*   **状态与持久化：** 内存状态支持即时读写，并由 SQLite 或 JSON 持久化提供支持，以确保在重启后数据不丢失。
*   **持久执行：** 集成工作流，具备自动重试、消息队列和调度（定时器/定时任务）功能。
*   **实时通信：** 原生支持 WebSocket，实现双向流传输。
*   **高效扩缩容：** Actor 在活跃时持续运行，在闲置时休眠至零，确保成本效益。

**应用场景**
该平台专门针对“有思想的软件”进行了优化，例如：
*   **AI 智能体：** 每个智能体维护其独立的持久化内存和上下文。
*   **协作工具：** 实时文档编辑，每个文件即为一个 Actor。
*   **多租户应用：** 为每个租户提供隔离的逻辑和存储。
*   **工作流编排：** 管理具有持久状态的复杂多步操作。

**生态系统与部署**
Rivet 采用 Rust 编写，基于 Apache 2.0 协议开源。它可以通过 Docker 进行自托管，也可以通过托管云服务访问。它支持主流 JavaScript 环境（包括 Node.js、Bun 和 Cloudflare Workers），并能与 Next.js 和 Hono 等框架集成。此外，Rivet 还提供“技能（skills）”，帮助 AI 编程辅助工具（如 Cursor 或 Claude Code）将该平台集成到现有项目中。

总之，Rivet 通过将计算、存储和网络整合为一个单一、可扩展的原语，简化了分布式系统，是专为现代有状态应用量身定制的解决方案。

---

## 8. We Will Not Be Divided

**原文标题**: We Will Not Be Divided

**原文链接**: [https://notdivided.org](https://notdivided.org)

“We Will Not Be Divided” is a digital platform and movement dedicated to fostering national unity and protecting individual liberties in the face of growing societal polarization. The site advocates for the preservation of fundamental human rights, with a specific focus on medical freedom, informed consent, and parental rights.

The core message of the initiative is a rejection of the "two-tier society" created by medical mandates and political tribalism. It calls on Americans to transcend political, social, and medical differences—specifically vaccination status—to stand in solidarity against what it characterizes as government and corporate overreach. The movement argues that coercive policies infringe upon bodily autonomy and undermine the democratic principles of the United States.

Key components of the website include:

*   **The Pledge:** A central call to action where visitors commit to standing with fellow citizens who face discrimination, loss of employment, or social exclusion due to their personal medical choices.
*   **Non-Partisanship:** The movement emphasizes that the defense of constitutional rights is not a partisan issue and should unite people across the political spectrum.
*   **Empowerment and Community:** The site provides a space for individuals to find support and join a collective effort to rebuild community trust and mutual respect.

In summary, the platform serves as a hub for those seeking to resist societal division and reclaim a sense of national community based on the shared values of personal autonomy and constitutional freedom.

---

## 9. From Noise to Image – interactive guide to diffusion

**原文标题**: From Noise to Image – interactive guide to diffusion

**原文链接**: [https://lighthousesoftware.co.uk/projects/from-noise-to-image/](https://lighthousesoftware.co.uk/projects/from-noise-to-image/)

生成摘要时出错

---

## 10. OpenAI Fires an Employee for Prediction Market Insider Trading

**原文标题**: OpenAI Fires an Employee for Prediction Market Insider Trading

**原文链接**: [https://www.wired.com/story/openai-fires-employee-insider-trading-polymarket-kalshi/](https://www.wired.com/story/openai-fires-employee-insider-trading-polymarket-kalshi/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 2 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 3 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 4 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 5 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 6 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 7 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 8 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 9 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 10 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 11 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 12 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 13 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 14 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 15 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 16 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 17 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 18 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 19 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 20 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 21 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 22 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 23 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 24 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 25 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 26 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 27 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 28 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 29 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 30 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 31 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 32 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 33 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 34 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 35 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 36 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 37 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 38 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 39 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 40 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 41 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 42 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 43 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 44 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 45 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 46 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 47 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 48 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 49 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 50 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 51 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 52 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 53 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 54 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 55 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 56 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 57 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 58 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 59 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 60 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 61 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 62 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 63 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 64 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 65 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 66 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 67 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 68 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 69 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 70 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 71 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 72 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 73 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 74 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 75 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 76 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 77 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 78 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 79 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 80 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 81 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 82 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 83 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 84 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 85 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 86 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 87 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 88 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 89 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 90 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 91 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 92 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 93 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 94 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 95 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 96 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 97 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 98 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 99 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 100 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 101 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 102 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 103 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 104 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 105 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 106 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 107 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 108 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 109 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 110 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 111 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 112 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 113 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 114 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 115 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 116 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 117 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 118 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 119 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 120 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 121 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 122 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 123 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 124 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 125 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 126 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 127 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 128 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 129 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 130 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 131 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 132 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 133 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 134 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 135 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 136 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 137 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 138 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 139 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 140 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 141 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 142 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 143 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 144 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 145 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 146 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 147 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 148 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 149 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 150 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 151 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 152 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 153 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 154 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 155 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 156 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 157 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 158 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 159 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 160 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 161 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 162 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 163 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 164 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 165 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 166 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 167 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 168 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 169 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 170 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 171 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 172 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 173 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 174 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 175 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 176 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 177 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 178 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 179 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 180 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 181 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 182 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 183 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 184 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 185 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 186 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 187 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 188 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 189 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 190 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 191 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 192 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 193 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 194 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 195 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 196 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 197 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 198 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 199 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 200 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 201 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 202 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 203 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 204 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 205 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 206 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 207 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 208 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 209 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 210 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 211 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 212 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 213 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 214 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 215 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 216 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 217 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 218 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 219 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 220 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 221 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 222 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 223 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 224 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 225 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 226 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 227 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 228 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 229 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 230 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 231 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 232 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 233 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 234 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 235 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 236 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 237 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 238 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 239 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 240 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 241 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 242 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 243 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 244 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 245 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 246 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 247 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 248 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 249 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 250 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 251 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 252 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 253 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 254 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 255 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 256 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 257 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 258 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 259 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 260 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 261 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 262 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 263 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 264 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 265 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 266 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 267 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 268 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 269 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 270 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 271 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 272 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 273 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 274 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 275 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 276 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 277 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 278 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 279 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 280 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 281 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 282 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 283 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 284 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 285 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 286 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 287 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 288 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 289 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 290 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 291 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 292 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 293 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 294 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 295 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 296 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 297 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 298 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 299 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 300 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 301 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 302 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 303 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 304 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 305 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 306 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 307 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 308 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 309 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 310 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 311 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 312 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 313 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 314 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 315 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 316 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 317 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 318 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 319 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 320 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 321 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 322 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 323 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 324 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 325 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 326 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 327 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 328 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 329 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 330 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 331 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 332 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 333 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 334 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 335 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 336 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 337 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 338 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 339 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 340 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 341 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 342 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 343 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 344 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 345 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
