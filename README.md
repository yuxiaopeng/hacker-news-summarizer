# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-20.md)

*最后自动更新时间: 2026-05-20 19:55:27*
## 1. 事件报告：2026年5月19日 – GCP 账户停用

**原文标题**: Incident Report: May 19, 2026 – GCP Account Suspension

**原文链接**: [https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage](https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage)

2026年5月19日，由于谷歌云平台（GCP）错误地停用了 Railway 的生产账号，Railway 经历了约 8 小时的全平台故障。此次自动停用立即导致 Railway 的控制面板、API 以及托管在 GCP 上的计算基础设施失效。

故障随后波及到托管在 Railway Metal 和 AWS 上的工作负载。虽然这些环境最初保持在线，但它们依赖于托管在 GCP 的控制平面进行网络路由。当本地路由缓存失效后，边缘代理无法解析地址，导致 Railway 在所有区域的所有工作负载均无法访问。

**时间线与恢复：**
*   **22:19 UTC：** 确定根源为 GCP 账号被停用。
*   **22:29 UTC：** 账号访问权限恢复，但所有基础设施仍处于离线状态。
*   **01:38 UTC：** 网络和边缘流量恢复。
*   **04:00 UTC：** 确认 API、控制面板及 OAuth 恢复运行。
*   **07:58 UTC：** 事件完全解决。

在恢复期间，Railway 面临着次生挑战，包括海量部署任务积压以及 GitHub 的速率限制，后者导致登录和构建功能暂时受阻。

**预防措施：**
Railway 对导致单点供应商故障引发全站停机的架构依赖负全部责任。为防止此类事件再次发生，他们正在实施以下变更：
1.  **消除单一依赖：** 将工作负载的可发现性与 GCP 托管的控制平面解耦，构建即使在单一供应商故障时也能运作的“真网格（true mesh）”架构。
2.  **多云数据库仲裁：** 将数据库分片扩展至 AWS 和 Metal，以确保在整个云供应商下线时具备故障转移能力和持久性。
3.  **重新设计数据平面：** 将 GCP 从数据平面的“热路径”中移除，仅将其作为次要或备用容量，以确保独立于供应商的架构弹性。

Railway 强调了其对系统可用性的承诺，并表示未来的架构将确保核心服务不再依赖任何单一平台。

---

## 2. OpenAI 模型证伪了离散几何中的一个核心猜想。

**原文标题**: An OpenAI model has disproved a central conjecture in discrete geometry

**原文链接**: [https://openai.com/index/model-disproves-discrete-geometry-conjecture/](https://openai.com/index/model-disproves-discrete-geometry-conjecture/)

OpenAI 宣布在数学领域取得重大突破，一个通用推理模型自主推翻了离散几何中一个长期存在的猜想。该问题被称为**平面单位距离问题**（planar unit distance problem），最早由保罗·埃尔德什（Paul Erdős）于 1946 年提出，旨在求解 $n$ 个点的集合中，距离恰好为一个单位的点对的最大数量。

80 年来，数学界普遍认为其最优增长率约为 $n^{1+o(1)}$。然而，OpenAI 的模型构造了一个无穷反例族，实现了 $n^{1+\delta}$ 的多项式级别改进。虽然模型最初的证明给出的 $\delta$ 是非显式的，但数学家威尔·萨温（Will Sawin）随后的进一步完善确定了其值为 **$\delta = 0.014$**。

这一发现因以下几点原因而备受瞩目：
*   **自主推理：** 证明是由一个通用模型生成的，而非专门针对数学训练或特定搜索的模型。
*   **跨学科创新：** 模型通过应用代数数论中的高级工具（具体为无穷类域塔和 Golod–Shafarevich 理论）解决了一个初等几何问题——这种关联令专家们感到震惊。
*   **专家验证：** 包括菲尔兹奖得主蒂姆·高尔斯（Tim Gowers）和诺加·阿隆（Noga Alon）在内的知名数学家验证了该证明。阿隆称其为“卓越的成就”，高尔斯则将其描述为“AI 数学领域的里程碑”。

这一里程碑标志着 AI 首次自主解决了数学子领域的一个核心开放问题。OpenAI 表示，这证明了先进模型有能力作为具备“独创见解”的研究伙伴，预示着 AI 未来将在生物学、物理学和工程学等领域的复杂研究中做出贡献。

---

## 3. 每秒 N 个 token 到底有多快？

**原文标题**: How fast is N tokens per second really?

**原文链接**: [https://mikeveerman.github.io/tokenspeed/](https://mikeveerman.github.io/tokenspeed/)

本文探讨了难以直观理解大语言模型（LLM）性能评估中常用的“每秒 Token 数”（tok/s）基准测试的问题。虽然硬件测评中经常出现 47 tok/s 或 500 tok/s 等标准数据，但在缺乏直接参照的情况下，用户很难想象其实际速度。

为了弥补这一差距，作者提供了一个包含四种内容模式的可视化工具：
*   **代码：** 带有语法高亮的伪代码。
*   **文本：** 标准散文（乱数假文）。
*   **思考：** 推理式输出（灰色斜体）与代码交替显示。
*   **代理：** 包含工具调用和代码生成，并伴有间歇性的处理停顿。

文章将常见的硬件和服务划分为不同的速度等级，以帮助用户理解实际的使用体验：
*   **5 tok/s：** 运行在树莓派等低功耗硬件上的本地模型。
*   **60 tok/s：** GPT-4 或 Claude 等托管模型的典型性能。
*   **200 tok/s：** Groq 等高速服务商。
*   **800 tok/s：** Cerebras 等超高速硬件，其速度已超过了人类的阅读极限。

一个核心观点是，模型的**感知速度**会因内容类型而显著不同。代码的 Token 密度比散文更高；因此，即使 tok/s 速率相同，模型在编写脚本和创作故事时的体感速度也大不相同。作者指出，对于英文散文，30 tok/s 约等于每秒 23 个单词（平均每个单词 1.3 个 Token）。该工具最终旨在揭示技术基准测试的客观数据与人类主观感知之间的差距。

---

## 4. Qwen3.7-Max：智能体前沿

**原文标题**: Qwen3.7-Max: The Agent Frontier

**原文链接**: [https://qwen.ai/blog?id=qwen3.7](https://qwen.ai/blog?id=qwen3.7)

所提供的内容仅包含“Qwen”一词，不足以生成文章的完整摘要。

然而，根据标题**“Qwen3.7-Max: The Agent Frontier（Qwen3.7-Max：智能体前沿）”**，本文可能讨论了以下要点：

*   **AI 智能体的进化：** 重点在于从简单的文本生成转向“智能体”能力——即模型可以自主规划、使用工具并执行多步任务，以解决复杂问题。
*   **“Max”级别的性能：** 由于“Max”版本通常代表 Qwen 系列中最强大的迭代，文章可能强调了其在推理、编程和数学能力方面的突破，足以媲美 GPT-4o 或 Claude 3.5 等其他顶级模型。
*   **下一代前沿：** 将 Qwen3.7 定位为下一代 AI 的领导者，特别是探讨模型如何与外部环境和 API 交互，从而成为功能性助手，而非仅仅是聊天机器人。

**如果您打算提供全文，请粘贴文本，我将很乐意为您提供详细摘要。**

---

## 5. 为什么 Inkwell 审核卡住了？

**原文标题**: Why is Inkwell stuck in review

**原文链接**: [https://www.manton.org/2026/05/19/why-is-inkwell-stuck-in.html](https://www.manton.org/2026/05/19/why-is-inkwell-stuck-in.html)

Manton Reece 的 iOS 应用 Inkwell 自 4 月 21 日起就一直陷于苹果的 App Store 审核流程中，期间经历了多次拒绝、技术调整以及一次正式申诉。Reece 概述了他在应对苹果《App Store 审核指南》时面临的几项具体障碍：

*   **安全与隐私 (1.2 & 5.1.1)：** 尽管 Inkwell 只是 Micro.blog 的一款 RSS 辅助应用，但苹果仍要求其添加内容举报、用户屏蔽和账号注销功能。
*   **技术与设计 (2.1 & 4)：** 该应用因“通过 Apple 登录”的漏洞及通用设计问题遭到拒绝，导致 Reece 最终禁用了某些登录功能。
*   **盈利模式 (3.1)：** 为了避开苹果的应用内购买佣金，Reece 删除了应用的发布功能和外部链接。他还将该应用限制在美国区商店上架，以利用 *Epic 诉苹果案* 裁决后的规则，将 Inkwell 定位为“阅读器”或“辅助”类应用。
*   **商标纠纷 (5.2.5)：** 主要症结在于“Inkwell”这个名称。苹果声称它侵犯了其 2002 年一项手写识别功能的商标。Reece 则辩称，根据美国专利及商标局 (USPTO) 的记录，该商标已正式“失效”，且商店中还存在许多其他名为“Inkwell”的应用。

Reece 对苹果在 iOS 分发上的绝对控制权表示沮丧，并指出 Inkwell 的安卓版本在一个月前就已通过谷歌审核。他认为苹果坚持使用一个已失效的商标属于权力扩张，超出了法律的必要范畴。目前，他正在等待应用审核委员会的回应。

---

## 6. GitHub 确认 3800 个仓库因恶意 VSCode 扩展遭到入侵。

**原文标题**: GitHub confirms breach of 3,800 repos via malicious VSCode extension

**原文链接**: [https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/](https://www.bleepingcomputer.com/news/security/github-confirms-breach-of-3-800-repos-via-malicious-vscode-extension/)

GitHub 确认，因一名员工安装了恶意的 VS Code 扩展程序，导致约 3,800 个内部代码库受到安全漏洞影响。在检测到入侵后，GitHub 已从 VS Code 市场中移除了该木马化插件，隔离了受影响的设备，并启动了事件响应程序。

该公司的调查目前显示，数据泄露仅限于 GitHub 内部代码库，没有证据表明存储在其他位置的客户数据受到影响。

黑客组织 TeamPCP 声称对此次攻击负责，并在一家网络犯罪论坛上发帖称其持有约 4,000 个私有代码库。该组织为这些失窃数据索价至少 5 万美元，并威胁称若无人购买将免费公开。TeamPCP 曾多次针对 NPM、PyPI 和 Docker 等开发者平台发起高调的供应链攻击，近期还开展了针对 OpenAI 员工的攻击活动。

此次事件凸显了 VS Code 市场中“中毒”插件日益增多的趋势。近年来，多款恶意扩展程序（部分安装量达数百万次）被用于窃取凭据、加密货币挖矿及数据窃取。尽管 GitHub 规模庞大，服务于 1.8 亿名开发者和 90% 的财富 100 强企业，但此次泄露事件再次强调了开发者环境在复杂的供应链攻击面前依然存在脆弱性。

---

## 7. SBCL：终极汇编代码面包板 (2014)

**原文标题**: SBCL: the ultimate assembly code breadboard (2014)

**原文链接**: [https://pvk.ca/Blog/2014/03/15/sbcl-the-ultimate-assembly-code-breadboard/](https://pvk.ca/Blog/2014/03/15/sbcl-the-ultimate-assembly-code-breadboard/)

This article explores the implementation of a high-performance, stack-based virtual machine (VM) using SBCL (Steel Bank Common Lisp) as a "breadboard" for assembly code experimentation. Inspired by the x87 floating-point unit and Chuck Moore’s F18 processor, the author proposes an optimization technique for VMs with small, fixed-size stacks (in this case, 8 slots).

**Key Technical Concepts:**
*   **Register-Based Stack Rotation:** Rather than moving data between registers or memory during push and pop operations, the VM maps the stack to eight physical CPU registers (R8–R15). It uses a modular counter to track the Top of Stack (TOS).
*   **Primitive Specialization:** To avoid the overhead of indexing registers at runtime, the author generates eight specialized versions of every VM primitive—one for each possible value of the stack pointer. 
*   **Efficient Dispatch:** The VM uses a direct-threaded model. Specialized primitives are stored at regular intervals (4288 bytes apart). The dispatch sequence (`NEXT`) calculates the jump address by combining a base address, the instruction offset, and the variant offset determined by the current stack pointer.
*   **SBCL as a Toolchain:** The author leverages SBCL’s internal assembler (`sb-assem`) and VM-definition tools (`sb-vm`) to programmatically emit machine code. This allows for rapid iteration and the use of Lisp to handle the repetitive task of generating multiple versions of each opcode.

**Implementation Details:**
The article provides Lisp code for basic primitives like `swap`, `dup`, `add`, and `sub`, as well as control-flow instructions like `jmp`, `call`, and `ret`. Finally, it demonstrates how to interface the VM with Common Lisp using a VOP (Virtual Operation) to handle the transition, including "entering" the VM by copying data from a Lisp buffer into the dedicated registers.

---

## 8. Saying Goodbye to Asm.js

**原文标题**: Saying Goodbye to Asm.js

**原文链接**: [https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html](https://spidermonkey.dev/blog/2026/05/20/saying-goodbye-to-asmjs.html)

生成摘要时出错

---

## 9. Sharla Boehm, the programmer whose code underpins the Internet

**原文标题**: Sharla Boehm, the programmer whose code underpins the Internet

**原文链接**: [https://www.scientificamerican.com/article/the-programmer-whose-code-underpins-the-internet/](https://www.scientificamerican.com/article/the-programmer-whose-code-underpins-the-internet/)

生成摘要时出错

---

## 10. Tracking Starbucks' 'widely recyclable' cups: none ended up at recycling

**原文标题**: Tracking Starbucks' 'widely recyclable' cups: none ended up at recycling

**原文链接**: [https://www.beyondplastics.org/press-releases/starbucks-cups-recyclable-report](https://www.beyondplastics.org/press-releases/starbucks-cups-recyclable-report)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 2 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 3 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 4 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 5 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 6 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 7 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 8 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 9 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 10 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 11 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 12 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 13 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 14 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 15 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 16 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 17 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 18 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 19 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 20 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 21 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 22 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 23 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 24 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 25 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 26 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 27 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 28 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 29 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 30 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 31 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 32 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 33 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 34 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 35 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 36 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 37 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 38 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 39 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 40 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 41 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 42 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 43 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 44 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 45 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 46 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 47 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 48 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 49 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 50 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 51 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 52 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 53 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 54 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 55 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 56 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 57 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 58 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 59 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 60 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 61 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 62 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 63 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 64 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 65 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 66 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 67 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 68 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 69 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 70 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 71 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 72 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 73 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 74 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 75 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 76 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 77 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 78 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 79 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 80 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 81 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 82 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 83 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 84 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 85 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 86 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 87 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 88 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 89 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 90 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 91 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 92 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 93 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 94 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 95 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 96 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 97 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 98 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 99 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 100 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 101 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 102 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 103 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 104 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 105 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 106 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 107 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 108 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 109 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 110 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 111 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 112 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 113 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 114 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 115 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 116 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 117 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 118 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 119 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 120 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 121 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 122 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 123 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 124 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 125 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 126 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 127 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 128 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 129 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 130 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 131 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 132 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 133 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 134 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 135 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 136 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 137 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 138 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 139 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 140 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 141 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 142 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 143 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 144 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 145 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 146 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 147 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 148 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 149 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 150 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 151 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 152 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 153 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 154 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 155 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 156 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 157 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 158 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 159 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 160 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 161 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 162 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 163 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 164 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 165 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 166 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 167 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 168 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 169 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 170 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 171 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 172 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 173 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 174 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 175 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 176 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 177 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 178 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 179 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 180 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 181 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 182 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 183 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 184 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 185 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 186 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 187 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 188 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 189 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 190 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 191 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 192 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 193 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 194 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 195 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 196 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 197 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 198 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 199 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 200 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 201 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 202 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 203 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 204 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 205 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 206 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 207 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 208 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 209 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 210 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 211 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 212 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 213 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 214 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 215 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 216 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 217 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 218 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 219 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 220 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 221 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 222 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 223 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 224 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 225 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 226 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 227 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 228 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 229 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 230 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 231 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 232 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 233 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 234 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 235 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 236 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 237 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 238 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 239 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 240 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 241 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 242 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 243 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 244 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 245 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 246 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 247 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 248 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 249 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 250 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 251 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 252 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 253 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 254 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 255 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 256 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 257 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 258 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 259 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 260 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 261 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 262 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 263 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 264 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 265 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 266 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 267 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 268 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 269 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 270 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 271 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 272 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 273 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 274 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 275 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 276 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 277 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 278 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 279 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 280 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 281 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 282 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 283 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 284 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 285 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 286 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 287 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 288 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 289 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 290 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 291 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 292 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 293 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 294 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 295 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 296 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 297 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 298 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 299 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 300 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 301 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 302 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 303 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 304 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 305 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 306 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 307 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 308 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 309 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 310 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 311 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 312 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 313 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 314 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 315 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 316 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 317 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 318 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 319 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 320 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 321 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 322 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 323 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 324 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 325 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 326 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 327 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 328 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 329 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 330 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 331 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 332 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 333 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 334 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 335 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 336 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 337 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 338 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 339 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 340 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 341 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 342 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 343 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 344 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 345 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 346 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 347 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 348 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 349 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 350 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 351 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 352 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 353 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 354 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 355 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 356 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 357 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 358 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 359 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 360 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 361 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 362 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 363 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 364 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 365 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 366 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 367 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 368 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 369 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 370 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 371 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 372 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 373 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 374 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 375 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 376 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 377 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 378 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 379 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 380 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 381 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 382 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 383 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 384 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 385 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 386 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 387 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 388 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 389 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 390 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 391 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 392 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 393 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 394 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 395 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 396 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 397 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 398 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 399 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 400 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 401 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 402 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 403 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 404 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 405 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 406 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 407 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 408 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 409 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 410 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 411 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 412 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 413 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 414 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 415 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 416 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 417 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 418 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 419 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 420 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 421 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 422 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 423 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 424 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 425 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 426 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
