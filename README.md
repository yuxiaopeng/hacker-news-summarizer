# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-22.md)

*最后自动更新时间: 2025-07-22 17:52:37*
## 1. 为何事实无法改变想法——结构可以（信念的系统分析）

**原文标题**: Why Facts Don't Change Minds–Structure Does (A Systems Analysis of Belief)

**原文链接**: [https://vasily.cc/blog/facts-dont-change-minds/](https://vasily.cc/blog/facts-dont-change-minds/)

本文认为，仅靠事实很少能改变人们的观念，因为信念的结构是相互关联的系统，类似于概念大教堂。教会对伽利略日心说的抵制不仅仅是迷信，更是对其权力结构、神学教义和社会等级制度至关重要的地心模型的捍卫。这种地心世界观嵌入在从圣经到建筑的一切事物中。质疑它威胁了教会的权威。

本文将信念系统可视化为概念和连接的图表。它以“增长至上的资本主义”和“生态可持续性”为例，展示了紧密联系的结构如何实现自我稳定。挑战一个信念系统意味着攻击核心思想（节点）或它们之间的连接（边），这可能会导致认知失调，并引发有动机的推理来捍卫现有的世界观。

“节点攻击”针对核心信念，可能会削弱连接，并损害整个系统的运作或动员能力。“边攻击”旨在切断思想之间的连接，迫使系统重新调整其逻辑，使其说服力降低。最终，信念系统通过重塑彼此的潜在结构进行竞争，而理解这些结构性动作可以深入了解论点背后的机制。人们对信息系统的代理性有着广泛的直觉。有些人认为信念系统——模因、意识形态、概念结构——几乎具有代理性，不断进化和竞争以求生存。另一些人则认为它们只不过是抽象概念，真正的代理性只存在于人类思想中。在实践中，持久性和明显的自

---

## 2. 玛丽患有精神分裂症，然后突然痊愈了。

**原文标题**: Mary had schizophrenia, then suddenly didn't

**原文链接**: [https://www.newyorker.com/magazine/2025/07/28/mary-had-schizophrenia-then-suddenly-she-didnt](https://www.newyorker.com/magazine/2025/07/28/mary-had-schizophrenia-then-suddenly-she-didnt)

本文讲述了玛丽的故事。她在四十岁出头时患上精神分裂症，影响了她的家庭，特别是她的女儿克里斯汀和安吉。玛丽出现了妄想症，认为自己正在被一位前同事联系，并受到他人的迫害，导致行为失常，并在九年内多次住院治疗。

大女儿克里斯汀积极参与了解她母亲的病情并为她的护理奔走呼吁，甚至研究了DSM。小女儿安吉在适应母亲妄想的世界中长大。尽管多次住院治疗和服用抗精神病药物，玛丽的病情仍然没有改变。

出乎意料的是，在被诊断出淋巴瘤并接受化疗后，玛丽的精神分裂症似乎消失了。她的女儿和医生们都感到困惑，因为她没有表现出精神病症状，并且她的性格变得冷静、礼貌和理性。虽然玛丽的癌症病情缓解，但她精神分裂症突然消失的原因仍然是一个谜，医生们推测可能是其中一种癌症药物产生了意想不到的好处。这个故事突出了精神疾病的复杂性以及健康和康复方面的意外转折。

---

## 3. Go 分配探针

**原文标题**: Go Allocation Probe

**原文链接**: [https://www.scattered-thoughts.net/writing/go-allocation-probe/](https://www.scattered-thoughts.net/writing/go-allocation-probe/)

本文介绍了一个名为 `go_allocation_probe` 的自定义工具，它用于识别程序中发生的 Go 分配类型，这是标准 Go 分析工具所缺乏的。作者利用 `bpftrace` 挂钩到核心 Go 分配函数 `runtime.mallocgc`。

挑战在于从 `_type` 参数中提取类型名称，结果发现它是一个偏移量 (`NameOff`)，指向可执行文件中模块数据的链表。为了解决这个问题，作者读取 Go 可执行文件的 ELF 段（`.noptrdata`、`.rodata`），并在一个单独的 Go 程序中重新实现了 Go 运行时中的 `resolveNameOff` 逻辑。这涉及到遍历模块链表并使用 `NameOff` 来查找类型名称。

当 `mallocgc` 被调用时，如果类型为 `nil`（当类型不包含指针时），会出现一个重大问题，导致 "<type not found>" 条目。为了解决这个问题，作者探测了其他运行时函数，如 `makechan`、`makeslicecopy` 和 `growslice`，它们可能会使用 `nil` 类型调用 `mallocgc`，并将类型信息存储在线程局部变量 (`@typ[tid]`) 中。他们还手动为特定类型（如 string、bytes 和 itab）分配名称。

最终的结果是一个可以识别和报告 Go 分配的类型、计数和总大小的工具，从而揭示潜在的分配热点。但需要注意的是，`[]T` 和 `*T` 可能会被报告为不同的类型。该工具最终帮助作者识别了代码中不必要的 `*string` 分配。

---

## 4. 微型代码阅读器：7美元的二维码传感器

**原文标题**: Tiny Code Reader: a $7 QR code sensor

**原文链接**: [https://excamera.substack.com/p/tiny-code-reader-a-7-qr-code-sensor](https://excamera.substack.com/p/tiny-code-reader-a-7-qr-code-sensor)

无法访问文章链接。

---

## 5. 人工智能市场明朗化

**原文标题**: AI Market Clarity

**原文链接**: [https://blog.eladgil.com/p/ai-market-clarity](https://blog.eladgil.com/p/ai-market-clarity)

埃拉德·吉尔的文章《AI市场明朗化》探讨了过去一年中某些人工智能市场的固化，指出了可能的领导者，并强调了潜在的未来机遇。他指出，虽然人工智能领域曾经一片模糊，但特定领域已涌现出明显的赢家。

文章确定了几个已出现明显领导者的市场：

*   **基础模型（LLM）：** Anthropic、谷歌、Meta、微软、Mistral、OpenAI和X.AI是核心参与者，因为扩展这些模型需要大量资金。
*   **代码：** Github Copilot、Anthropic的Claude Code、Cognition / Windsurf、Cursor、Google / Windsurf、Microsoft/Github、OpenAI。
*   **法律：** Harvey和CaseText领先，Legora和Crosby等新兴玩家紧随其后。
*   **医疗记录：** Abridge、Ambience、Commure / Athelas和Nuance正在整合。
*   **客户服务：** Decagon和Sierra正在获得 traction，而现有企业正在适应。
*   **搜索和信息检索重塑：** 谷歌、OpenAI、Perplexity和Meta。

吉尔还强调了未来的市场机遇：会计、合规、金融工具、销售工具和安全。

一个关键问题是，模型限制、GTM挑战或团队经验是否阻碍了这些领域的市场形成。 文章讨论了“GPT阶梯”，表明模型的进步将解锁新的市场。

最后，文章强调了向代理工作流（人工智能代表您行事）的转变，并讨论了人工智能驱动的整合的潜力，即收购公司而不仅仅是向他们销售人工智能软件可以加速采用并改善经济效益。

---

## 6. 字体对比：阿特金森易读体单空格 vs. JetBrains Mono 和 Fira Code

**原文标题**: Font Comparison: Atkinson Hyperlegible Mono vs. JetBrains Mono and Fira Code

**原文链接**: [https://www.anthes.is/font-comparison-review-atkinson-hyperlegible-mono.html](https://www.anthes.is/font-comparison-review-atkinson-hyperlegible-mono.html)

本文评测了Atkinson Hyperlegible Mono字体，这是一款为提高可读性（特别是视力障碍人士的可读性）而设计的等宽字体，并将其与流行的编程字体JetBrains Mono和Fira Code进行了比较。

作者将Atkinson Hyperlegible Mono作为其主要终端字体，探讨了字符区分的重要性，以避免歧义，并强调了多字符和单字符同形字（相似字符）以及镜像字形的问题。

Atkinson Hyperlegible Mono由Applied Design Works为盲文研究所创建，优先考虑独特的轮廓、增强的字母形式、不对称的字脚和夸张的下伸部。

与JetBrains Mono和Fira Code的比较表明，Atkinson Hyperlegible Mono在区分相似字符（如8、B、5和S）以及镜像字形（如b、d、p和q）方面表现出色。然而，与其他字体相比，它在方括号和花括号（[]和{}）的区分上表现较弱。编程符号也具有可变长度，这与其他字体处理此功能的方式不同。

本文还提供了安装说明，并承认了一些注意事项，包括某些版本中缺少反引号/抑音符、其以品牌为中心的起源、缺少编程连字以及缺乏同行评审的研究来支持其可读性声明。尽管如此，作者认为它仍然是一个引人注目的选择。

---

## 7. Better Auth (YC X25) 正在招聘

**原文标题**: Better Auth (YC X25) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/better-auth/jobs/N0CtN58-staff-engineer](https://www.ycombinator.com/companies/better-auth/jobs/N0CtN58-staff-engineer)

Better Auth（YC X25）是一家TypeScript认证框架公司，现招聘一名资深工程师加入其小型远程团队。该公司旨在普及高质量的身份验证，并使开发者能够掌控自己的身份验证流程。他们的开源框架正在快速增长，并受到许多初创公司和YC公司的信任。

资深工程师将协作开发后端、前端和设计，使用TypeScript、React和Node.js构建功能。他们将端到端地负责各项功能，管理插件生态系统，并指导初级开发人员。

Better Auth提供具有竞争力的薪资（12万至20万美元），以及丰厚的股权、完全远程办公的机会和定义公司文化的机会。他们重视自主性、协作、主动性和持续成长。所需技能包括5年以上软件开发经验、强大的TypeScript专业知识以及对身份验证概念的熟悉。拥有开源项目经验或构建复杂身份验证系统的经验者优先。

该公司专注于创造一流的开发者体验，并积极建设社区。他们正在寻找能够为开发者解决有意义的问题并从头开始塑造公司文化的人。Better Auth强调专注构建和产生重大影响之间的平衡。

---

## 8. 不要动画高度

**原文标题**: Don't Animate Height

**原文链接**: [https://www.granola.ai/blog/dont-animate-height](https://www.granola.ai/blog/dont-animate-height)

吉姆·费舍尔的文章《不要动画高度》详细介绍了他的笔记应用 Granola 中的一个性能瓶颈，该瓶颈是由一个昂贵的 CSS 动画引起的。他发现对音频音量可视化器的 `height` 属性进行动画处理会消耗过多的 CPU 和 GPU 资源。

费舍尔使用 Chrome 的开发者工具，特别是“性能”和“图层”选项卡，发现了由 `height` 动画触发的持续重绘和布局偏移。他解释说，动画 `height` 的代价很高，因为它会迫使浏览器为每一帧重新计算布局、重绘图层并重新合成整个场景。

该文章随后概述了浏览器的渲染流水线（布局、绘制、合成），并解释了不同的 CSS 属性如何影响它。布局属性（如 `height`）的动画成本最高，其次是绘制属性（如 `fill`），最后是合成属性（如 `transform` 和 `opacity`），它们的成本最低。

费舍尔最初尝试用 `transform: scaleY()` 替换 `height`，导致了圆角失真。他最终通过为每个条使用两个圆角矩形，并使用 `translate` 动画化它们的位置来解决了这个问题。这利用了 `transform` 属性，允许浏览器跳过昂贵的布局和绘制步骤，从而显着提高了性能。渲染器进程的 CPU 使用率从 15% 降至 6%，GPU 使用率也大幅下降。这篇文章强调了理解浏览器渲染流水线以及为动画选择合适的 CSS 属性的重要性。

---

## 9. 破坏的理由

**原文标题**: The Case for Sabotage

**原文链接**: [https://collectiveactionintech.substack.com/p/the-case-for-sabotage](https://collectiveactionintech.substack.com/p/the-case-for-sabotage)

无法访问文章链接。

---

## 10. OSS重建：开源，重塑，历久弥新

**原文标题**: OSS Rebuild: open-source, Rebuilt to Last

**原文链接**: [https://security.googleblog.com/2025/07/introducing-oss-rebuild-open-source.html](https://security.googleblog.com/2025/07/introducing-oss-rebuild-open-source.html)

OSS重建：由谷歌开源安全团队 (GOSST) 宣布，是一项旨在通过独立复现和验证上游制品来增强对开源软件包生态系统信任的新项目。OSS重建旨在打击针对广泛使用的依赖项的供应链攻击，为安全团队提供可验证的数据，而无需增加维护人员的负担。

该项目具有以下特性：

*   **自动化构建定义生成：** 适用于PyPI、npm和Crates.io软件包。
*   **SLSA来源：** 适用于数千个软件包，无需发布者参与即可达到SLSA构建级别3。
*   **构建可观察性和验证工具：** 集成到现有的漏洞管理工作流程中。
*   **基础设施定义：** 使组织能够运行自己的OSS重建实例，用于重建、签名和分发来源。

OSS重建通过解决未提交的源代码、构建环境妥协和隐蔽的后门，来应对日益增长的开源软件漏洞问题。它帮助企业增强元数据、扩充SBOM并加速漏洞响应。发布者和维护人员受益于增强的软件包信任、历史软件包的追溯完整性以及降低的CI安全敏感性。

该项目支持检查软件包完整性、浏览重建版本以及使用CLI工具重建软件包。谷歌鼓励开发人员、企业和安全研究人员在github.com/google/oss-rebuild上为OSS重建的开发和改进做出贡献。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 2 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 3 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 4 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 5 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 6 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 7 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 8 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 9 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 10 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 11 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 12 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 13 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 14 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 15 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 16 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 17 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 18 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 19 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 20 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 21 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 22 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 23 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 24 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 25 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 26 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 27 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 28 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 29 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 30 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 31 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 32 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 33 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 34 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 35 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 36 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 37 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 38 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 39 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 40 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 41 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 42 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 43 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 44 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 45 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 46 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 47 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 48 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 49 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 50 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 51 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 52 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 53 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 54 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 55 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 56 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 57 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 58 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 59 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 60 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 61 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 62 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 63 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 64 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 65 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 66 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 67 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 68 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 69 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 70 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 71 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 72 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 73 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 74 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 75 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 76 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 77 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 78 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 79 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 80 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 81 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 82 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 83 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 84 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 85 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 86 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 87 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 88 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 89 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 90 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 91 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 92 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 93 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 94 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 95 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 96 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 97 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 98 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 99 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 100 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 101 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 102 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 103 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 104 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 105 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 106 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 107 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 108 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 109 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 110 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 111 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 112 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 113 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 114 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 115 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 116 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 117 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 118 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 119 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 120 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 121 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 122 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 123 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 124 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 125 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
