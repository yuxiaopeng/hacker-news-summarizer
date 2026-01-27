# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-01-27.md)

*最后自动更新时间: 2026-01-27 17:57:40*
## 1. 43万年前保存完好的木制工具是迄今发现的最古老工具

**原文标题**: 430k-year-old well-preserved wooden tools are the oldest ever found

**原文链接**: [https://archaeologymag.com/2026/01/430000-year-old-wooden-tools-marathousa/](https://archaeologymag.com/2026/01/430000-year-old-wooden-tools-marathousa/)

考古学家在希腊梅格洛玻利斯盆地的马拉松萨1号（Marathousa 1）遗址发现了已知最古老的木制工具，其年代可追溯至约43万年前。这一发现显著提前了早期古人类（很可能是海德堡人）掌握复杂木工艺的时间线。

这些工具之所以能保存至今，得益于该遗址独特的饱水无氧环境，有效防止了木材在数十万年间腐烂。研究人员鉴定出了多件木制品，包括可能用于挖掘或防御的尖锐工具，以及带有明显刻意加工痕迹并用于屠宰的碎片。

具有重要意义的是，这些木制器物是与古菱齿象（*Palaeoloxodon antiquus*）及其他已灭绝动物的遗骸一同发现的。这表明早期人类曾利用这些工具处理大型动物尸体，彰显了旧石器时代早期极高的技术规划能力和环境适应水平。

这一发现挑战了长期以来关于“石器时代”的传统叙事，即认为早期人类几乎完全依赖石器技术。相反，它强调了木材曾是一种至关重要且用途广泛的资源，只是因其易腐烂的特性而在考古记录中极度罕见。这些发现为窥探“木器时代”提供了难得的机会，证明了早在现代人类出现之前，早期古人类就已具备复杂的认知能力和对自然材料的深刻理解。

---

## 2. 管理即AI超能力：在智能体AI时代蓬勃发展

**原文标题**: Management as AI superpower: Thriving in a world of agentic AI

**原文链接**: [https://www.oneusefulthing.org/p/management-as-ai-superpower](https://www.oneusefulthing.org/p/management-as-ai-superpower)

在《管理即AI超能力》一文中，伊森·莫里克（Ethan Mollick）认为，曾经被视为“软技能”的传统管理能力，正成为智能体AI（Agentic AI）时代至关重要的技术工具。

莫里克详细介绍了一门MBA实验课程，在这门课上，没有编程经验的学生利用Claude Code和ChatGPT等AI工具，在短短四天内就构建出了功能完备的创业原型。这代表着与AI时代之前相比，生产力实现了数量级的提升，这很大程度上是因为AI降低了转型和执行的成本。

文章引入了**“智能体工作方程式”**，通过权衡以下三个因素，帮助专业人士决定何时将任务委派给AI：
1. **人类基准时间：** 人类完成该任务所需的时间。
2. **成功概率：** AI产出高质量结果的可能性。
3. **AI处理时间：** 投入在提示（Prompting）以及更关键的评估输出结果上的时间。

莫里克指出，随着AI模型（以虚构或未来的“GPT-5.2”为例）在专家级任务上的成功率达到约72%，即便计入人工审核的时间，节省下的时间依然极其可观。

核心观点是：**委派即是新的提示词（Delegation is the new prompting）。** 用户不再需要钻研各种精巧的提示词技巧，而应使用成熟的管理框架——如产品需求文档（PRD）或“五段式命令”——来传达意图。领域专业知识依然至关重要，因为它能让“管理者”提供更好的指令，并更准确地评估AI的产出。

最终，随着AI使“才华”变得充沛且廉价，定义何为“优秀”并将其清晰表达出来的能力，将成为最稀缺、最有价值的技能。在这一新格局下，每个人都将成为数字劳动力的管理者。

---

## 3. Xfwl4：Xfce Wayland 合成器路线图

**原文标题**: Xfwl4 – The Roadmap for a Xfce Wayland Compositor

**原文链接**: [https://alexxcons.github.io/blogpost_15.html](https://alexxcons.github.io/blogpost_15.html)

Xfce 开发团队公布了 **xfwl4** 的路线图，这是一个由社区捐赠资助的全新 Wayland 混成器。资深核心开发者 Brian Tarricone 将领导该项目，旨在通过保持与当前基于 X11 的 `xfwm4` 功能对等并重用现有配置，为用户提供无缝过渡。

虽然团队最初尝试修改旧有的 `xfwm4` 代码，但出于以下原因，最终决定进行完全重写：
*   **架构：** 现有的 C 代码库与 X11 特定逻辑的耦合度过高。
*   **稳定性：** 维护一套并行的代码库可以在不影响稳定 X11 环境的前提下，进行快速的 Wayland 开发。
*   **现代工具链：** 新的混成器将使用 **Rust** 语言和 **Smithay** 库编写。选择 Rust 是考虑到其内存安全性及开发者的偏好，而选择 Smithay 而非 `wlroots` 则是看中其深度定制能力和更出色的 Rust 集成。

该项目的范围不仅限于窗口管理。它还包括对会话启动流程的重大调整（混成器现在将作为会话根进程）、`xdg-session-management` 协议的实现，以及对 XWayland 的全面支持。此外，Xfce 的 CI 基础设施将进行升级，以支持通过 Meson 构建 Rust 项目。

开发工作目前已经展开，预计 `xfwl4` 的首个实验版本将于 2026 年中期左右发布。该项目是 Xfce 面向未来 Linux 桌面实现现代化的重大战略投资。

---

## 4. OpenSSL：CMS AuthEnvelopedData 解析中的栈缓冲区溢出

**原文标题**: OpenSSL: Stack buffer overflow in CMS AuthEnvelopedData parsing

**原文链接**: [https://openssl-library.org/news/vulnerabilities/#CVE-2025-15467](https://openssl-library.org/news/vulnerabilities/#CVE-2025-15467)

2026年1月27日，OpenSSL 发布了安全公告，解决了严重程度从“低”到“高”不等的若干漏洞。这些问题主要影响 OpenSSL 3.x 系列，但部分旧版本也受到影响。

**高风险和中等风险漏洞：**
*   **CVE-2025-15467（高）：** CMS *AuthEnvelopedData* 解析中存在栈缓冲区溢出。恶意构造的 AEAD 参数（如过大的 IV）可能在身份验证前触发越界写入，潜在导致程序崩溃（DoS）或远程代码执行。受影响版本为 3.0 至 3.6。
*   **CVE-2025-11187（中）：** 对 PKCS#12 文件中 PBMAC1 参数的验证不当，可能在 MAC 校验期间导致栈缓冲区溢出或空指针解引用。受影响版本为 3.4、3.5 和 3.6。

**低风险漏洞：**
另有六个已识别的问题，包括：
*   **CVE-2025-15468：** QUIC 协议密码查找中的空指针解引用。
*   **CVE-2025-15469：** 使用单次（one-shot）算法（如 Ed25519）时，`openssl dgst` 命令会静默截断超过 16MB 的输入，存在数据完整性风险。
*   **CVE-2025-66199：** TLS 1.3 证书压缩期间分配内存过多（高达 22 MiB），可能导致 DoS。
*   **CVE-2025-68160：** `BIO_f_linebuffer` 中的堆越界写入，影响包括 1.0.2 和 1.1.1 在内的几乎所有版本。
*   **CVE-2025-69418：** 使用低级 OCB 硬件加速函数时，尾随字节可能保持未加密或未认证状态。
*   **CVE-2025-69419：** PKCS#12 UTF-8 转换过程中的越界写入。

**影响与缓解措施：**
大多数漏洞会导致应用程序崩溃并引发拒绝服务（DoS）。值得注意的是，OpenSSL FIPS 模块不受影响，因为受影响的实现在 FIPS 边界之外。建议用户升级到最新的修复版本（3.6.1、3.5.5、3.4.4、3.3.6 或 3.0.19）以缓解这些风险。

---

## 5. 我写了一个 Git

**原文标题**: I made my own Git

**原文链接**: [https://tonystr.net/blog/git_immitation](https://tonystr.net/blog/git_immitation)

在《我编写了自己的 Git》一文中，TonyStr 记录了他构建一个名为 **Grit** 的简化版版本控制系统的过程，旨在揭示 Git 底层运行机制的神秘面纱。他指出，Git 常被误解为是一个存储“差异”（变动）的工具，而实际上它是一个存储数据快照的**内容寻址文件系统**。

该项目专注于构成 Git 架构基础的三个核心对象：

1.  **Blobs（数据对象）：** 存储文件的实际内容。由于文件是通过其内容的 SHA-1 哈希值来标识的，Grit 会自动处理重复数据；如果两个文件的内容完全相同，它们将指向同一个 Blob。
2.  **Trees（树对象）：** 代表目录。Tree 将文件名映射到相应的 Blob 哈希或其他 Tree 哈希，从而有效地重建文件夹结构。
3.  **Commits（提交对象）：** 将特定的 Tree（项目快照）与元数据（如作者、时间戳以及指向“父”提交哈希的指针）关联起来，从而形成历史链条。

TonyStr 强调，Git 的“魔力”在于其简洁性。通过使用 Python 实现 `init`、`add` 和 `commit` 等基本命令，他证明了版本控制本质上只是一个由哈希构成的有向无环图（DAG）。

文章的核心观点是，理解了这些底层数据结构后，Git 更复杂的功能（如分支和合并）将变得非常容易掌握。文章最后总结道，只要你理解如何操作其指针，Git 本质上就是一个“永不丢失数据”的永久数据存储库。

---

## 6. Artie (YC S23) 正在招聘创始招聘官

**原文标题**: Artie (YC S23) Is Hiring a Founding Recruiter

**原文链接**: [https://www.ycombinator.com/companies/artie/jobs/MX163y2-founding-recruiter](https://www.ycombinator.com/companies/artie/jobs/MX163y2-founding-recruiter)

Artie 是一家总部位于旧金山、由 Y Combinator (S23) 支持的初创公司，目前正寻求一位**创始招聘人员 (Founding Recruiter)**，负责构建并领导其内部人才职能。Artie 提供实时数据流平台，实现从数据库到数据仓库的无缝、海量数据复制，服务于 ClickUp 和 Substack 等客户。

**职位描述**
作为公司首位内部招聘人员，成功候选人将主导端到端的招聘全生命周期，重点关注研发、产品、运营及设计 (EPOD) 领域。这是一个高影响力的“全栈”岗位，具体包括：
*   直接与创始人合作，定义岗位职责范围及评估标准。
*   在竞争激烈的市场中主动发掘并转化高级技术人才。
*   从零构建招聘基础设施（包括招聘管理系统 ATS、工具及流程）。
*   管理外部猎头机构合作关系，确保其符合 Artie 的质量标准。

**理想候选人**
公司寻求拥有 4 年以上经验的招聘人员，特别是在早期（A 轮至 C 轮）技术驱动型企业的从业经验。候选人必须具备“销售思维”、能够与资深工程师深入交流的技术直觉，以及极强的主人翁意识。此岗位要求每周五天在旧金山办公室实地办公。

**薪酬与福利**
*   **年薪：** 18 万 – 20.5 万美元
*   **股权：** 0.10% – 0.20%
*   **福利：** 医疗保险、401(k) 匹配、无限制带薪休假及每日免费膳食。

面试流程包括：招聘经理初筛、工作环节测试、居家案例分析以及实地考察。随着 Artie 持续扩展其关键任务型数据基础设施，该职位为未来晋升为人才负责人 (Head of Talent) 提供了独特的成长路径。

---

## 7. 亚马逊将关闭所有 Amazon Go 和 Amazon Fresh 门店

**原文标题**: Amazon to Shut Down All Amazon Go and Amazon Fresh Stores

**原文链接**: [https://www.wsj.com/business/retail/amazon-to-shut-down-all-amazon-go-and-amazon-fresh-stores-0301dfb7](https://www.wsj.com/business/retail/amazon-to-shut-down-all-amazon-go-and-amazon-fresh-stores-0301dfb7)

无法访问文章链接。

---

## 8. A simulation where life unfolds in real time

**原文标题**: A simulation where life unfolds in real time

**原文链接**: [https://soupof.life](https://soupof.life)

生成摘要时出错

---

## 9. Heathrow scraps liquid container limit

**原文标题**: Heathrow scraps liquid container limit

**原文链接**: [https://www.bbc.com/news/articles/c1evvx89559o](https://www.bbc.com/news/articles/c1evvx89559o)

生成摘要时出错

---

## 10. Snow Simulation Toy

**原文标题**: Snow Simulation Toy

**原文链接**: [https://potch.me/2026/snow-simulation-toy.html](https://potch.me/2026/snow-simulation-toy.html)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 2 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 3 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 4 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 5 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 6 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 7 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 8 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 9 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 10 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 11 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 12 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 13 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 14 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 15 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 16 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 17 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 18 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 19 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 20 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 21 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 22 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 23 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 24 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 25 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 26 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 27 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 28 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 29 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 30 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 31 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 32 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 33 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 34 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 35 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 36 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 37 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 38 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 39 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 40 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 41 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 42 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 43 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 44 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 45 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 46 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 47 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 48 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 49 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 50 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 51 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 52 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 53 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 54 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 55 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 56 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 57 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 58 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 59 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 60 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 61 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 62 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 63 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 64 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 65 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 66 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 67 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 68 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 69 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 70 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 71 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 72 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 73 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 74 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 75 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 76 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 77 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 78 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 79 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 80 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 81 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 82 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 83 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 84 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 85 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 86 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 87 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 88 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 89 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 90 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 91 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 92 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 93 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 94 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 95 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 96 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 97 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 98 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 99 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 100 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 101 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 102 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 103 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 104 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 105 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 106 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 107 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 108 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 109 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 110 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 111 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 112 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 113 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 114 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 115 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 116 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 117 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 118 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 119 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 120 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 121 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 122 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 123 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 124 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 125 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 126 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 127 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 128 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 129 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 130 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 131 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 132 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 133 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 134 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 135 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 136 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 137 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 138 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 139 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 140 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 141 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 142 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 143 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 144 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 145 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 146 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 147 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 148 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 149 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 150 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 151 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 152 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 153 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 154 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 155 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 156 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 157 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 158 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 159 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 160 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 161 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 162 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 163 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 164 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 165 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 166 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 167 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 168 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 169 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 170 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 171 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 172 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 173 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 174 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 175 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 176 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 177 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 178 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 179 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 180 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 181 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 182 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 183 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 184 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 185 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 186 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 187 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 188 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 189 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 190 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 191 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 192 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 193 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 194 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 195 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 196 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 197 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 198 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 199 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 200 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 201 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 202 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 203 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 204 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 205 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 206 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 207 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 208 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 209 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 210 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 211 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 212 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 213 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 214 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 215 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 216 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 217 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 218 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 219 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 220 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 221 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 222 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 223 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 224 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 225 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 226 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 227 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 228 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 229 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 230 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 231 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 232 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 233 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 234 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 235 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 236 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 237 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 238 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 239 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 240 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 241 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 242 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 243 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 244 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 245 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 246 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 247 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 248 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 249 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 250 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 251 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 252 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 253 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 254 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 255 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 256 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 257 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 258 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 259 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 260 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 261 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 262 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 263 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 264 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 265 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 266 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 267 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 268 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 269 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 270 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 271 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 272 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 273 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 274 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 275 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 276 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 277 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 278 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 279 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 280 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 281 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 282 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 283 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 284 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 285 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 286 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 287 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 288 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 289 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 290 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 291 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 292 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 293 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 294 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 295 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 296 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 297 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 298 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 299 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 300 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 301 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 302 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 303 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 304 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 305 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 306 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 307 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 308 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 309 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 310 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 311 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 312 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 313 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
