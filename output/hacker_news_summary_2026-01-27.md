# Hacker News 热门文章摘要 (2026-01-27)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. SoundCloud Data Breach Now on HaveIBeenPwned

**原文标题**: SoundCloud Data Breach Now on HaveIBeenPwned

**原文链接**: [https://haveibeenpwned.com/Breach/SoundCloud](https://haveibeenpwned.com/Breach/SoundCloud)

生成摘要时出错

---

## 12. Two Twisty Shapes Resolve a Centuries-Old Topology Puzzle

**原文标题**: Two Twisty Shapes Resolve a Centuries-Old Topology Puzzle

**原文链接**: [https://www.quantamagazine.org/two-twisty-shapes-resolve-a-centuries-old-topology-puzzle-20260120/](https://www.quantamagazine.org/two-twisty-shapes-resolve-a-centuries-old-topology-puzzle-20260120/)

生成摘要时出错

---

## 13. TikTok users can't upload anti-ICE videos. The company blames tech issues

**原文标题**: TikTok users can't upload anti-ICE videos. The company blames tech issues

**原文链接**: [https://www.cnn.com/2026/01/26/tech/tiktok-ice-censorship-glitch-cec](https://www.cnn.com/2026/01/26/tech/tiktok-ice-censorship-glitch-cec)

生成摘要时出错

---

## 14. The Enchiridion by Epictetus

**原文标题**: The Enchiridion by Epictetus

**原文链接**: [https://www.gutenberg.org/files/45109/45109-h/45109-h.htm](https://www.gutenberg.org/files/45109/45109-h/45109-h.htm)

生成摘要时出错

---

## 15. Velox: A Port of Tauri to Swift by Miguel de Icaza

**原文标题**: Velox: A Port of Tauri to Swift by Miguel de Icaza

**原文链接**: [https://github.com/velox-apps/velox](https://github.com/velox-apps/velox)

生成摘要时出错

---

## 16. Cloudflare claimed they implemented Matrix on Cloudflare workers. They didn't

**原文标题**: Cloudflare claimed they implemented Matrix on Cloudflare workers. They didn't

**原文链接**: [https://tech.lgbt/@JadedBlueEyes/115967791152135761](https://tech.lgbt/@JadedBlueEyes/115967791152135761)

生成摘要时出错

---

## 17. The age of Pump and Dump software

**原文标题**: The age of Pump and Dump software

**原文链接**: [https://tautvilas.medium.com/software-pump-and-dump-c8a9a73d313b](https://tautvilas.medium.com/software-pump-and-dump-c8a9a73d313b)

生成摘要时出错

---

## 18. A list of fun destinations for telnet

**原文标题**: A list of fun destinations for telnet

**原文链接**: [https://telnet.org/htm/places.htm](https://telnet.org/htm/places.htm)

生成摘要时出错

---

## 19. Show HN: We Built the 1. EU-Sovereignty Audit for Websites

**原文标题**: Show HN: We Built the 1. EU-Sovereignty Audit for Websites

**原文链接**: [https://lightwaves.io/en/eu-audit/](https://lightwaves.io/en/eu-audit/)

生成摘要时出错

---

## 20. Handling Long Branches

**原文标题**: Handling Long Branches

**原文链接**: [https://maskray.me/blog/2026-01-25-handling-long-branches](https://maskray.me/blog/2026-01-25-handling-long-branches)

生成摘要时出错

---

## 21. Kimi Released Kimi K2.5, Open-Source Visual SOTA-Agentic Model

**原文标题**: Kimi Released Kimi K2.5, Open-Source Visual SOTA-Agentic Model

**原文链接**: [https://www.kimi.com/blog/kimi-k2-5.html](https://www.kimi.com/blog/kimi-k2-5.html)

生成摘要时出错

---

## 22. Apple introduces new AirTag with longer range and improved findability

**原文标题**: Apple introduces new AirTag with longer range and improved findability

**原文链接**: [https://www.apple.com/newsroom/2026/01/apple-introduces-new-airtag-with-expanded-range-and-improved-findability/](https://www.apple.com/newsroom/2026/01/apple-introduces-new-airtag-with-expanded-range-and-improved-findability/)

生成摘要时出错

---

## 23. ChatGPT Containers can now run bash, pip/npm install packages and download files

**原文标题**: ChatGPT Containers can now run bash, pip/npm install packages and download files

**原文链接**: [https://simonwillison.net/2026/Jan/26/chatgpt-containers/](https://simonwillison.net/2026/Jan/26/chatgpt-containers/)

生成摘要时出错

---

## 24. The hidden engineering of runways

**原文标题**: The hidden engineering of runways

**原文链接**: [https://practical.engineering/blog/2026/1/20/the-hidden-engineering-of-runways](https://practical.engineering/blog/2026/1/20/the-hidden-engineering-of-runways)

生成摘要时出错

---

## 25. The Universal Pattern Popping Up in Math, Physics and Biology (2013)

**原文标题**: The Universal Pattern Popping Up in Math, Physics and Biology (2013)

**原文链接**: [https://www.quantamagazine.org/in-mysterious-pattern-math-and-nature-converge-20130205/](https://www.quantamagazine.org/in-mysterious-pattern-math-and-nature-converge-20130205/)

生成摘要时出错

---

## 26. We Do Not Support Opt-Out Forms (2025)

**原文标题**: We Do Not Support Opt-Out Forms (2025)

**原文链接**: [https://consciousdigital.org/why-we-do-not-support-opt-out-forms/](https://consciousdigital.org/why-we-do-not-support-opt-out-forms/)

生成摘要时出错

---

## 27. Windows 11's Patch Tuesday nightmare gets worse

**原文标题**: Windows 11's Patch Tuesday nightmare gets worse

**原文链接**: [https://www.windowscentral.com/microsoft/windows-11/windows-11s-botched-patch-tuesday-update-nightmare-continues-as-microsoft-confirms-some-pcs-might-fail-to-boot](https://www.windowscentral.com/microsoft/windows-11/windows-11s-botched-patch-tuesday-update-nightmare-continues-as-microsoft-confirms-some-pcs-might-fail-to-boot)

生成摘要时出错

---

## 28. Over 36,500 killed in Iran's deadliest massacre, documents reveal

**原文标题**: Over 36,500 killed in Iran's deadliest massacre, documents reveal

**原文链接**: [https://www.iranintl.com/en/202601255198](https://www.iranintl.com/en/202601255198)

生成摘要时出错

---

## 29. There is an AI code review bubble

**原文标题**: There is an AI code review bubble

**原文链接**: [https://www.greptile.com/blog/ai-code-review-bubble](https://www.greptile.com/blog/ai-code-review-bubble)

生成摘要时出错

---

## 30. Amazon Closing Fresh and Go Stores

**原文标题**: Amazon Closing Fresh and Go Stores

**原文链接**: [https://finance.yahoo.com/news/amazon-closing-fresh-grocery-convenience-150437789.html](https://finance.yahoo.com/news/amazon-closing-fresh-grocery-convenience-150437789.html)

生成摘要时出错

---

## 31. Refinement Without Specification

**原文标题**: Refinement Without Specification

**原文链接**: [https://buttondown.com/hillelwayne/archive/refinement-without-specification/](https://buttondown.com/hillelwayne/archive/refinement-without-specification/)

生成摘要时出错

---

## 32. I let ChatGPT analyze a decade of my Apple Watch data, then I called my doctor

**原文标题**: I let ChatGPT analyze a decade of my Apple Watch data, then I called my doctor

**原文链接**: [https://www.msn.com/en-us/news/technology/i-let-chatgpt-analyze-a-decade-of-my-apple-watch-data-then-i-called-my-doctor/ar-AA1UZxip](https://www.msn.com/en-us/news/technology/i-let-chatgpt-analyze-a-decade-of-my-apple-watch-data-then-i-called-my-doctor/ar-AA1UZxip)

生成摘要时出错

---

## 33. JuiceSSH – Give me my pro features back

**原文标题**: JuiceSSH – Give me my pro features back

**原文链接**: [https://nproject.io/blog/juicessh-give-me-back-my-pro-features/](https://nproject.io/blog/juicessh-give-me-back-my-pro-features/)

生成摘要时出错

---

## 34. RIP Low-Code 2014-2025

**原文标题**: RIP Low-Code 2014-2025

**原文链接**: [https://www.zackliscio.com/posts/rip-low-code-2014-2025/](https://www.zackliscio.com/posts/rip-low-code-2014-2025/)

生成摘要时出错

---

## 35. India and EU announce landmark trade deal

**原文标题**: India and EU announce landmark trade deal

**原文链接**: [https://www.bbc.com/news/articles/crrnee01r9jo](https://www.bbc.com/news/articles/crrnee01r9jo)

生成摘要时出错

---

## 36. Dithering – Part 2: The Ordered Dithering

**原文标题**: Dithering – Part 2: The Ordered Dithering

**原文链接**: [https://visualrambling.space/dithering-part-2/](https://visualrambling.space/dithering-part-2/)

生成摘要时出错

---

## 37. Russia using Interpol's wanted list to target critics abroad, leak reveals

**原文标题**: Russia using Interpol's wanted list to target critics abroad, leak reveals

**原文链接**: [https://www.bbc.com/news/articles/c20gg729y1yo](https://www.bbc.com/news/articles/c20gg729y1yo)

生成摘要时出错

---

## 38. New York Times games are hard: A computational perspective

**原文标题**: New York Times games are hard: A computational perspective

**原文链接**: [https://arxiv.org/abs/2509.10846](https://arxiv.org/abs/2509.10846)

生成摘要时出错

---

## 39. The Adolescence of Technology

**原文标题**: The Adolescence of Technology

**原文链接**: [https://www.darioamodei.com/essay/the-adolescence-of-technology](https://www.darioamodei.com/essay/the-adolescence-of-technology)

生成摘要时出错

---

## 40. Porting 100k lines from TypeScript to Rust using Claude Code in a month

**原文标题**: Porting 100k lines from TypeScript to Rust using Claude Code in a month

**原文链接**: [https://blog.vjeux.com/2026/analysis/porting-100k-lines-from-typescript-to-rust-using-claude-code-in-a-month.html](https://blog.vjeux.com/2026/analysis/porting-100k-lines-from-typescript-to-rust-using-claude-code-in-a-month.html)

生成摘要时出错

---

## 41. France Aiming to Replace Zoom, Google Meet, Microsoft Teams, etc.

**原文标题**: France Aiming to Replace Zoom, Google Meet, Microsoft Teams, etc.

**原文链接**: [https://twitter.com/lellouchenico/status/2015775970330882319](https://twitter.com/lellouchenico/status/2015775970330882319)

生成摘要时出错

---

## 42. San Francisco Graffiti

**原文标题**: San Francisco Graffiti

**原文链接**: [https://walzr.com/sf-graffiti](https://walzr.com/sf-graffiti)

生成摘要时出错

---

## 43. People who know the formula for WD-40

**原文标题**: People who know the formula for WD-40

**原文链接**: [https://www.wsj.com/business/the-secret-society-of-people-who-know-the-formula-for-wd-40-e9c0ff54](https://www.wsj.com/business/the-secret-society-of-people-who-know-the-formula-for-wd-40-e9c0ff54)

生成摘要时出错

---

## 44. Television is 100 years old today

**原文标题**: Television is 100 years old today

**原文链接**: [https://diamondgeezer.blogspot.com/2026/01/tv100.html](https://diamondgeezer.blogspot.com/2026/01/tv100.html)

生成摘要时出错

---

## 45. Show HN: One Human + One Agent = One Browser From Scratch in 20K LOC

**原文标题**: Show HN: One Human + One Agent = One Browser From Scratch in 20K LOC

**原文链接**: [https://emsh.cat/one-human-one-agent-one-browser/](https://emsh.cat/one-human-one-agent-one-browser/)

生成摘要时出错

---

## 46. AI code and software craft

**原文标题**: AI code and software craft

**原文链接**: [https://alexwennerberg.com/blog/2026-01-25-slop.html](https://alexwennerberg.com/blog/2026-01-25-slop.html)

生成摘要时出错

---

## 47. Show HN: TetrisBench – Gemini Flash reaches 66% win rate on Tetris against Opus

**原文标题**: Show HN: TetrisBench – Gemini Flash reaches 66% win rate on Tetris against Opus

**原文链接**: [https://tetrisbench.com/tetrisbench/](https://tetrisbench.com/tetrisbench/)

生成摘要时出错

---

## 48. Model Market Fit

**原文标题**: Model Market Fit

**原文链接**: [https://www.nicolasbustamante.com/p/model-market-fit](https://www.nicolasbustamante.com/p/model-market-fit)

生成摘要时出错

---

## 49. After two years of vibecoding, I'm back to writing by hand

**原文标题**: After two years of vibecoding, I'm back to writing by hand

**原文链接**: [https://atmoio.substack.com/p/after-two-years-of-vibecoding-im](https://atmoio.substack.com/p/after-two-years-of-vibecoding-im)

生成摘要时出错

---

## 50. Qwen3-Max-Thinking

**原文标题**: Qwen3-Max-Thinking

**原文链接**: [https://qwen.ai/blog?id=qwen3-max-thinking](https://qwen.ai/blog?id=qwen3-max-thinking)

生成摘要时出错

---

## 51. Fedora Asahi Remix is now working on Apple M3

**原文标题**: Fedora Asahi Remix is now working on Apple M3

**原文链接**: [https://bsky.app/profile/did:plc:okydh7e54e2nok65kjxdklvd/post/3mdd55paffk2o](https://bsky.app/profile/did:plc:okydh7e54e2nok65kjxdklvd/post/3mdd55paffk2o)

生成摘要时出错

---

## 52. Show HN: Only 1 LLM can fly a drone

**原文标题**: Show HN: Only 1 LLM can fly a drone

**原文链接**: [https://github.com/kxzk/snapbench](https://github.com/kxzk/snapbench)

生成摘要时出错

---

## 53. Intel's Panther Lake Chip is its biggest win in years

**原文标题**: Intel's Panther Lake Chip is its biggest win in years

**原文链接**: [https://www.wired.com/story/intel-panther-lake-core-ultra-series-3-review/](https://www.wired.com/story/intel-panther-lake-core-ultra-series-3-review/)

生成摘要时出错

---

## 54. Knapsack Offline Internet Solution (satellite datacasting)

**原文标题**: Knapsack Offline Internet Solution (satellite datacasting)

**原文链接**: [https://www.netfreedompioneers.org/knapsack-content-station/](https://www.netfreedompioneers.org/knapsack-content-station/)

生成摘要时出错

---

## 55. Text Is King

**原文标题**: Text Is King

**原文链接**: [https://www.experimental-history.com/p/text-is-king](https://www.experimental-history.com/p/text-is-king)

生成摘要时出错

---

## 56. Google AI Overviews cite YouTube more than any medical site for health queries

**原文标题**: Google AI Overviews cite YouTube more than any medical site for health queries

**原文链接**: [https://www.theguardian.com/technology/2026/jan/24/google-ai-overviews-youtube-medical-citations-study](https://www.theguardian.com/technology/2026/jan/24/google-ai-overviews-youtube-medical-citations-study)

生成摘要时出错

---

## 57. MapLibre Tile: a modern and efficient vector tile format

**原文标题**: MapLibre Tile: a modern and efficient vector tile format

**原文链接**: [https://maplibre.org/news/2026-01-23-mlt-release/](https://maplibre.org/news/2026-01-23-mlt-release/)

生成摘要时出错

---

## 58. Pharos: The Lighthouse at Alexandria

**原文标题**: Pharos: The Lighthouse at Alexandria

**原文链接**: [https://penelope.uchicago.edu/encyclopaedia_romana/greece/paganism/pharos.html](https://penelope.uchicago.edu/encyclopaedia_romana/greece/paganism/pharos.html)

生成摘要时出错

---

## 59. TSMC Risk

**原文标题**: TSMC Risk

**原文链接**: [https://stratechery.com/2026/tsmc-risk/](https://stratechery.com/2026/tsmc-risk/)

生成摘要时出错

---

## 60. LED lighting undermines visual performance unless supplemented by wider spectra

**原文标题**: LED lighting undermines visual performance unless supplemented by wider spectra

**原文链接**: [https://www.nature.com/articles/s41598-026-35389-6](https://www.nature.com/articles/s41598-026-35389-6)

生成摘要时出错

---

## 61. The mountain that weighed the Earth

**原文标题**: The mountain that weighed the Earth

**原文链接**: [https://signoregalilei.com/2026/01/18/the-mountain-that-weighed-the-earth/](https://signoregalilei.com/2026/01/18/the-mountain-that-weighed-the-earth/)

生成摘要时出错

---

## 62. OpenFlexure Microscope

**原文标题**: OpenFlexure Microscope

**原文链接**: [https://openflexure.org/projects/microscope/](https://openflexure.org/projects/microscope/)

生成摘要时出错

---

## 63. Find 'Abbey Road when type 'Beatles abbey rd': Fuzzy/Semantic search in Postgres

**原文标题**: Find 'Abbey Road when type 'Beatles abbey rd': Fuzzy/Semantic search in Postgres

**原文链接**: [https://rendiment.io/postgresql/2026/01/21/pgtrgm-pgvector-music.html](https://rendiment.io/postgresql/2026/01/21/pgtrgm-pgvector-music.html)

生成摘要时出错

---

## 64. OSS ChatGPT WebUI – 530 Models, MCP, Tools, Gemini RAG, Image/Audio Gen

**原文标题**: OSS ChatGPT WebUI – 530 Models, MCP, Tools, Gemini RAG, Image/Audio Gen

**原文链接**: [https://llmspy.org/docs/v3](https://llmspy.org/docs/v3)

生成摘要时出错

---

## 65. The C-Shaped Hole in Package Management

**原文标题**: The C-Shaped Hole in Package Management

**原文链接**: [https://nesbitt.io/2026/01/27/the-c-shaped-hole-in-package-management.html](https://nesbitt.io/2026/01/27/the-c-shaped-hole-in-package-management.html)

生成摘要时出错

---

## 66. Not all Chess960 positions are equally complex

**原文标题**: Not all Chess960 positions are equally complex

**原文链接**: [https://arxiv.org/abs/2512.14319](https://arxiv.org/abs/2512.14319)

生成摘要时出错

---

## 67. First, make me care

**原文标题**: First, make me care

**原文链接**: [https://gwern.net/blog/2026/make-me-care](https://gwern.net/blog/2026/make-me-care)

生成摘要时出错

---

## 68. Study is stolen, sold, published. Now the victim is accused of plagiarism

**原文标题**: Study is stolen, sold, published. Now the victim is accused of plagiarism

**原文链接**: [https://retractionwatch.com/2026/01/26/study-is-stolen-sold-published-now-the-victim-is-accused-of-plagiarism/](https://retractionwatch.com/2026/01/26/study-is-stolen-sold-published-now-the-victim-is-accused-of-plagiarism/)

生成摘要时出错

---

## 69. OracleGPT: Thought Experiment on an AI Powered Executive

**原文标题**: OracleGPT: Thought Experiment on an AI Powered Executive

**原文链接**: [https://senteguard.com/blog/#post-7fYcaQrAcfsldmSb7zVM](https://senteguard.com/blog/#post-7fYcaQrAcfsldmSb7zVM)

生成摘要时出错

---

## 70. Things I've learned in my 10 years as an engineering manager

**原文标题**: Things I've learned in my 10 years as an engineering manager

**原文链接**: [https://www.jampa.dev/p/lessons-learned-after-10-years-as](https://www.jampa.dev/p/lessons-learned-after-10-years-as)

生成摘要时出错

---

## 71. Blade Runner Costume Design (2020)

**原文标题**: Blade Runner Costume Design (2020)

**原文链接**: [https://costumedesignarchive.blogspot.com/2020/12/blade-runner-1982.html](https://costumedesignarchive.blogspot.com/2020/12/blade-runner-1982.html)

生成摘要时出错

---

## 72. All In – a small tool to check real buyin after decisions

**原文标题**: All In – a small tool to check real buyin after decisions

**原文链接**: [https://www.cognu.app/all-in](https://www.cognu.app/all-in)

生成摘要时出错

---

## 73. The browser is the sandbox

**原文标题**: The browser is the sandbox

**原文链接**: [https://simonwillison.net/2026/Jan/25/the-browser-is-the-sandbox/](https://simonwillison.net/2026/Jan/25/the-browser-is-the-sandbox/)

生成摘要时出错

---

## 74. A History of Haggis

**原文标题**: A History of Haggis

**原文链接**: [https://www.historytoday.com/archive/historians-cookbook/history-haggis](https://www.historytoday.com/archive/historians-cookbook/history-haggis)

生成摘要时出错

---

## 75. CedarDB: The fastest database you've never heard of

**原文标题**: CedarDB: The fastest database you've never heard of

**原文链接**: [https://www.amplifypartners.com/blog-posts/the-fastest-database-youve-never-heard-of](https://www.amplifypartners.com/blog-posts/the-fastest-database-youve-never-heard-of)

生成摘要时出错

---

## 76. Google Books removed all search functions for any books with previews

**原文标题**: Google Books removed all search functions for any books with previews

**原文链接**: [https://old.reddit.com/r/google/comments/1qn1hk1/google_has_seemingly_entirely_removed_search/](https://old.reddit.com/r/google/comments/1qn1hk1/google_has_seemingly_entirely_removed_search/)

生成摘要时出错

---

## 77. Is It Time for a Nordic Nuke?

**原文标题**: Is It Time for a Nordic Nuke?

**原文链接**: [https://warontherocks.com/2026/01/is-it-time-for-a-nordic-nuke/](https://warontherocks.com/2026/01/is-it-time-for-a-nordic-nuke/)

生成摘要时出错

---

## 78. Surveillance companies track smartphone users through advertising data

**原文标题**: Surveillance companies track smartphone users through advertising data

**原文链接**: [https://www.lemonde.fr/en/pixels/article/2026/01/22/how-surveillance-companies-track-smartphone-users-through-advertising-data_6749674_13.html](https://www.lemonde.fr/en/pixels/article/2026/01/22/how-surveillance-companies-track-smartphone-users-through-advertising-data_6749674_13.html)

生成摘要时出错

---

## 79. Windows 11 January Update Breaks Notepad

**原文标题**: Windows 11 January Update Breaks Notepad

**原文链接**: [https://winbuzzer.com/2026/01/22/windows-11-january-update-breaks-notepad-snipping-tool-and-other-apps-xcxwbn/](https://winbuzzer.com/2026/01/22/windows-11-january-update-breaks-notepad-snipping-tool-and-other-apps-xcxwbn/)

生成摘要时出错

---

## 80. Exactitude in Science – Borges (1946) [pdf]

**原文标题**: Exactitude in Science – Borges (1946) [pdf]

**原文链接**: [https://kwarc.info/teaching/TDM/Borges.pdf](https://kwarc.info/teaching/TDM/Borges.pdf)

生成摘要时出错

---

## 81. The Holy Grail of Linux Binary Compatibility: Musl and Dlopen

**原文标题**: The Holy Grail of Linux Binary Compatibility: Musl and Dlopen

**原文链接**: [https://github.com/quaadgras/graphics.gd/discussions/242](https://github.com/quaadgras/graphics.gd/discussions/242)

生成摘要时出错

---

## 82. What “The Best” Looks Like

**原文标题**: What “The Best” Looks Like

**原文链接**: [https://www.kuril.in/blog/what-the-best-looks-like/](https://www.kuril.in/blog/what-the-best-looks-like/)

生成摘要时出错

---

## 83. Show HN: SF Microclimates

**原文标题**: Show HN: SF Microclimates

**原文链接**: [https://github.com/solo-founders/sf-microclimates](https://github.com/solo-founders/sf-microclimates)

生成摘要时出错

---

## 84. Running the Stupid Cricut Software on Linux

**原文标题**: Running the Stupid Cricut Software on Linux

**原文链接**: [https://arthur.pizza/2025/12/running-stupid-cricut-software-under-linux/](https://arthur.pizza/2025/12/running-stupid-cricut-software-under-linux/)

生成摘要时出错

---

## 85. Cyclic Subgroup Sum

**原文标题**: Cyclic Subgroup Sum

**原文链接**: [https://m-slee.netlify.app/posts/cyclic-subgroup-sum](https://m-slee.netlify.app/posts/cyclic-subgroup-sum)

生成摘要时出错

---

## 86. Pwn2own: Escaping VMware Workstation

**原文标题**: Pwn2own: Escaping VMware Workstation

**原文链接**: [https://www.synacktiv.com/en/publications/on-the-clock-escaping-vmware-workstation-at-pwn2own-berlin-2025](https://www.synacktiv.com/en/publications/on-the-clock-escaping-vmware-workstation-at-pwn2own-berlin-2025)

生成摘要时出错

---

## 87. Meta to test premium subscriptions on Instagram, Facebook, and WhatsApp

**原文标题**: Meta to test premium subscriptions on Instagram, Facebook, and WhatsApp

**原文链接**: [https://techcrunch.com/2026/01/26/meta-to-test-premium-subscriptions-on-instagram-facebook-and-whatsapp/](https://techcrunch.com/2026/01/26/meta-to-test-premium-subscriptions-on-instagram-facebook-and-whatsapp/)

生成摘要时出错

---

## 88. A macOS app that blurs your screen when you slouch

**原文标题**: A macOS app that blurs your screen when you slouch

**原文链接**: [https://github.com/tldev/posturr](https://github.com/tldev/posturr)

生成摘要时出错

---

## 89. A flawed paper in management science has been cited more than 6k times

**原文标题**: A flawed paper in management science has been cited more than 6k times

**原文链接**: [https://statmodeling.stat.columbia.edu/2026/01/22/aking/](https://statmodeling.stat.columbia.edu/2026/01/22/aking/)

生成摘要时出错

---

## 90. Guix for Development

**原文标题**: Guix for Development

**原文链接**: [https://dthompson.us/posts/guix-for-development.html](https://dthompson.us/posts/guix-for-development.html)

生成摘要时出错

---

## 91. ICE using Palantir tool that feeds on Medicaid data

**原文标题**: ICE using Palantir tool that feeds on Medicaid data

**原文链接**: [https://www.eff.org/deeplinks/2026/01/report-ice-using-palantir-tool-feeds-medicaid-data](https://www.eff.org/deeplinks/2026/01/report-ice-using-palantir-tool-feeds-medicaid-data)

生成摘要时出错

---

## 92. A static site generator written in POSIX shell

**原文标题**: A static site generator written in POSIX shell

**原文链接**: [https://aashvik.com/posts/shell-ssg/](https://aashvik.com/posts/shell-ssg/)

生成摘要时出错

---

## 93. I built a 2x faster lexer, then discovered I/O was the real bottleneck

**原文标题**: I built a 2x faster lexer, then discovered I/O was the real bottleneck

**原文链接**: [https://modulovalue.com/blog/syscall-overhead-tar-gz-io-performance/](https://modulovalue.com/blog/syscall-overhead-tar-gz-io-performance/)

生成摘要时出错

---

## 94. Scientists identify brain waves that define the limits of 'you'

**原文标题**: Scientists identify brain waves that define the limits of 'you'

**原文链接**: [https://www.sciencealert.com/scientists-identify-brain-waves-that-define-the-limits-of-you](https://www.sciencealert.com/scientists-identify-brain-waves-that-define-the-limits-of-you)

生成摘要时出错

---

## 95. Iran's internet blackout may become permanent, with access for elites only

**原文标题**: Iran's internet blackout may become permanent, with access for elites only

**原文链接**: [https://restofworld.org/2026/iran-blackout-tiered-internet/](https://restofworld.org/2026/iran-blackout-tiered-internet/)

生成摘要时出错

---

## 96. I was right about ATProto key management

**原文标题**: I was right about ATProto key management

**原文链接**: [https://notes.nora.codes/atproto-again/](https://notes.nora.codes/atproto-again/)

生成摘要时出错

---

## 97. Show HN: An interactive map of US lighthouses and navigational aids

**原文标题**: Show HN: An interactive map of US lighthouses and navigational aids

**原文链接**: [https://www.lighthouses.app/](https://www.lighthouses.app/)

生成摘要时出错

---

## 98. Kubernetes Remote Code Execution via Nodes/Proxy Get Permission

**原文标题**: Kubernetes Remote Code Execution via Nodes/Proxy Get Permission

**原文链接**: [https://grahamhelton.com/blog/nodes-proxy-rce](https://grahamhelton.com/blog/nodes-proxy-rce)

生成摘要时出错

---

## 99. Google confirms 'high-friction' sideloading flow is coming to Android

**原文标题**: Google confirms 'high-friction' sideloading flow is coming to Android

**原文链接**: [https://www.androidauthority.com/google-sideloading-android-high-friction-process-3633468/](https://www.androidauthority.com/google-sideloading-android-high-friction-process-3633468/)

生成摘要时出错

---

## 100. TikTok removals up 150% following U.S. joint venture

**原文标题**: TikTok removals up 150% following U.S. joint venture

**原文链接**: [https://www.cnbc.com/2026/01/26/tiktok-uninstalls-are-up-150percent-following-us-joint-venture.html](https://www.cnbc.com/2026/01/26/tiktok-uninstalls-are-up-150percent-following-us-joint-venture.html)

生成摘要时出错

---

