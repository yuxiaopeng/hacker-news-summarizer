# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-08-29.md)

*最后自动更新时间: 2026-08-29 20:00:52*
## 1. 如今的互联网简直成了一个充满掠夺的粪坑。

**原文标题**: The Internet Is Kind of a Predatory Cesspit Now

**原文链接**: [https://www.stephendiehl.com/posts/internet_predatory_cesspit/](https://www.stephendiehl.com/posts/internet_predatory_cesspit/)

本文认为，互联网已从一个以人为中心的“公共广场”退化为一套优化的工业化捕食系统。早期网络以业余精神和人类连接为特征，而现代网络的组织原则已转变为对人类弱点的侦测与变现。

作者强调了“欺诈经济”的兴起，普通人被卷入各种参与式骗局，从加密货币、联盟营销到“男权圈”教练和健康博主不一而足。在这个生态系统中，捕食者与猎物的界限变得模糊；在算法信息流形成的“多巴胺跑步机”驱动下，受害者为了挽回损失而沦为推销员。这种商业模式将“满意”视为“客户流失”，将“痛苦”视为“持续性收入”，要求用户保持孤独、缺乏安全感或贪婪，以确保其持续消费。

在技术层面，这种转变是由强化学习环路驱动的，这些环路将参与度、愤怒和越轨置于真相之上。算法利用社会经济的脆弱性（如住房和就业稳定性的崩溃），向被现代生活孤立的人群提供虚假的“头奖”承诺。作者警告说，生成式人工智能将使谎言的成本降至零，从而进一步恶化这一环境。

最终，文章将现代互联网定性为一个受制于异化目标函数（增长、留存和转化）的“非人性”空间，这些函数无法识别人的目的。结论指出，虽然完全脱钩几乎不可能，但用户必须认识到，互联网是一个掠夺性工具，而非一个社交世界。为了维护人类的能动性，人们必须寻求物理世界的“摩擦感”，因为物理世界提供了那些无限的、利润驱动的数字机器试图抹去的限制与边界。

---

## 2. Warp 基于 Claude 构建自我改进的智能体

**原文标题**: Warp builds self-improving agents on Claude

**原文链接**: [https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude](https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude)

Warp 在 Claude 平台上开发了一套**基于 Agent 技能的框架**，用于构建具有自我改进能力的 AI Agent。为了解决常见的“无状态”问题（即 Agent 的反馈在会话结束后会丢失），Warp 将模式从手动提示词工程转向了双技能架构，使 Agent 能够从人类的评价中学习。

### 自我改进框架
该系统依赖于两种不同类型的“技能”，它们是与原始提示词分离的、基于文件的知识编码：

1.  **内部（基础）技能**：包含执行特定任务（如代码审查或问题分类）所需的功能领域知识和指令。
2.  **外部（改进）技能**：一个定期运行的观察者 Agent。它负责分析积累的人类反馈，对比 Agent 输出与用户预期，并对内部技能文件提出针对性的修改建议。

由于这些技能以普通文件形式存储，更新可以通过标准的 PR/代码审查工作流进行。这确保了在 Agent 的“自我改进”上线前，会有专人进行审核与合并，从而保持高质量的输出。

### 核心最佳实践
*   **原则优于规则**：像对待“聪明人”一样指导 Agent，提供通用原则和指令背后的“原因”，而非僵化、详尽的规则。
*   **低摩擦反馈**：在工作发生的场景（如 GitHub 评论）中直接捕获反馈，以确保持续的数据流。
*   **质量胜过数量**：来自专家的详细、特定领域的反馈，比海量的“点赞/点踩”二进制信号更有价值。
*   **渐进式披露**：通过引用外部资源而非撑大上下文窗口，保持技能文件的精简与模块化。

Warp 目前已将这一模式应用于其开源仓库的分类、规格说明书撰写和代码审查中，将 Agent 从一次性助手转变为能够随时间积累知识的进化系统。

---

## 3. 先校准，再加速：新岗位上的行动导向

**原文标题**: Calibrate Before You Accelerate: Bias Toward Action in a New Role

**原文链接**: [https://tucker.wales/writing/bias-towards-action/](https://tucker.wales/writing/bias-towards-action/)

在《先校准，后加速》一文中，作者指出，尽管在新岗位上渴望立竿见影是人之常情，但只有立足于具体背景时，“行动导向”才是一种超能力。在不了解现有体系的情况下盲目行动——如同未看图纸就抡起大锤——可能会导致代价高昂的错误。

为避免这种情况，作者提出了入职三阶段法：

1.  **搜集期：** 专注于“积极的被动”。通过识别利益相关者、开展一对一调研来摸清现状，并践行“切斯特顿栅栏”原则——即在完全理解某项流程设立的初衷之前，不要轻易将其废除。
2.  **综合期：** 分析收集的信息，将重复出现的痛点串联起来。在此阶段，将机遇分为“唾手可得的小目标”（速赢项目）和需要长期战略的复杂系统性问题。
3.  **战略加速期：** 安全地释放行动力。从能简化他人工作的微小且可见的胜利开始，以积累信任资本。在启动重大项目前，先分享单页假设以获取反馈，并将工作重点从 90% 的倾听逐渐转向 80% 的执行。

归根结底，目标不是慢行动，而是果断出击。通过优先进行校准而非仓促行事，新员工可以确保当他们最终“发力”时，推动的是真正需要改变的部分。只有在建立起对背景环境的深度认知后，真正的工作才算开始。

---

## 4. SQLite作为文档型数据库 (2020)

**原文标题**: SQLite as a Document Database (2020)

**原文链接**: [https://dgl.cx/2020/06/sqlite-json-support](https://dgl.cx/2020/06/sqlite-json-support)

这篇发表于2020年的文章探讨了SQLite 3.31.0版本引入的**生成列**（generated columns）如何使这款嵌入式数据库能够有效地作为文档数据库运行。通过将JSON支持与这些列相结合，用户可以将原始JSON插入文本字段，同时利用`json_extract`函数自动将特定属性提取到独立的列中。

作者强调了这种方法的几个核心优势和特性：

*   **验证与约束**：由于`json_extract`要求JSON格式合法，SQLite会在插入时自动拒绝格式错误的数据。用户还可以通过为生成列应用`NOT NULL`或其他约束来进一步加强数据完整性，确保特定的JSON键始终存在。
*   **虚拟列与存储列**：生成列可以是`VIRTUAL`（即时计算）或`STORED`（缓存在磁盘上）。虽然存储列提供了不同的性能权衡，但虚拟列具有极高的灵活性。
*   **索引与性能**：一个关键优势是可以在虚拟列上创建索引。这使得SQLite能够对嵌套在JSON对象中的数据进行高效搜索，从而模拟Elasticsearch或PostgreSQL等专用文档存储库的行为。
*   **架构演进**：这种配置非常适合处理不可预知的数据（如webhook）。开发人员最初可以存储整个JSON负载，随后在需要时使用`ALTER TABLE`提取并索引特定字段，而无需重构底层数据。

总之，生成列提供了一种轻量级的方法来处理半结构化数据，同时兼具关系型引擎的性能和可靠性。

---

## 5. Tether: iMessage, SMS, etc. on Linux

**原文标题**: Tether: iMessage, SMS, etc. on Linux

**原文链接**: [https://zackbartel.com/blog/2026/08/tether/](https://zackbartel.com/blog/2026/08/tether/)

生成摘要时出错

---

## 6. 美国国土安全部正利用鲜为人知的法律监视记者、非营利组织和工会。

**原文标题**: DHS is using obscure law to snoop on journalists, non-profits, unions

**原文链接**: [https://www.theguardian.com/us-news/2026/aug/29/trump-dhs-1509-summons-records-journalists-nonprofits](https://www.theguardian.com/us-news/2026/aug/29/trump-dhs-1509-summons-records-journalists-nonprofits)

特朗普时期的美国国土安全部（DHS）被指利用一项鲜为人知的海关法（19 USC 1509），秘密获取记者、工会及非营利组织的私人数据。虽然该法规在法律上仅适用于进口关税和税收调查，但国土安全部却利用它在处理国内案件时绕过司法监督。

文章强调，这是一种规避宪法第四修正案的“公然行为”。在一次案例中，法官曾因缺乏推断理由两次拒绝批准调取记者乔治亚·福特（Georgia Fort）和唐·莱蒙（Don Lemon）YouTube 数据的搜查令，随后国土安全部竟针对同样的信息签发了行政传票。与搜查令不同，此类传票仅需国土安全部官员签字，无需法官批准。除记者外，国土安全部还利用这一手段获取了“日出运动”（Sunrise Movement）和美国服务业雇员国际工会（SEIU）等组织的财务记录，并试图揭露社交媒体上匿名批评者的身份。

法律专家和公民自由倡导者认为，这是对法律的严重误读。他们主张国土安全部正在绕过法院，针对受保护的言论和国内活动进行无谓且具侵略性的调查。当受到 Twitter 或 Meta 等公司的法律挑战时，国土安全部往往会撤回传票——专家认为，这种策略旨在避免法院作出可能永久限制此类行为的最终裁决。

尽管 2017 年的一份监察长报告此前已指出此类传票存在“不当”使用，但这一做法依然存在。批评人士警告称，由于此类请求通常处于保密状态，并将法律负担转嫁给被调查对象，目前尚无有效手段制衡行政部门的这种权力滥用。

---

## 7. 梦游者：自带命令语言的被动后门

**原文标题**: Sleepwalker: Passive Backdoor with Its Own Command Language

**原文链接**: [https://r136a1.dev/2026/08/24/sleepwalker-a-passive-backdoor-with-its-own-command-language/](https://r136a1.dev/2026/08/24/sleepwalker-a-passive-backdoor-with-its-own-command-language/)

**SLEEPWALKER** 是一款复杂的 64 位被动后门，专为隐蔽的针对性攻击而设计。它通常通过 DLL 侧加载（side-loading）实现持久化，伪装成合法的 Windows 组件（`dpapi.dll`），并由 ESET Management Agent（`ERAAgent.exe`）加载。

该恶意软件最显著的特征是其**被动运行模式**。与传统后门不同，它不会向命令与控制（C2）服务器发送信标（beacon），也不会开放可识别的监听端口。相反，它以混杂模式嗅探网络接口，等待特制的“魔术包”或隐藏的 DNS 查询。只有在收到符合其唯一校验和及加密要求的封包时，它才会“唤醒”并执行任务。

关键技术特性包括：

*   **自定义命令语言：** SLEEPWALKER 不包含内置恶意负载。相反，它集成了一个拥有 23 条指令的字节码解释器。这使得攻击者可以通过网络发送完整的程序，用以处理任务调度、分阶段文件交付（带有 SHA-256 验证）以及直接在内存中执行 shellcode。
*   **多样化的传输方式：** 它支持多种通信协议，包括 TCP、UDP、ICMP、SMB 命名管道，以及用于虚拟机与宿主机之间通信的 VMware 内部 VMCI 通道。
*   **系统弱化：** 为了便于横向移动，它会主动修改 Windows 安全设置以允许匿名 SMB 访问，并创建具有宽松访问权限（授予 “Everyone” 组）的命名管道。
*   **强加密：** 它使用静态链接的 mbedTLS 库对所有传入命令实施 AES-256-CCM 加密，确保即使封包被捕获，在没有正确密钥的情况下也无法被轻易解析或重放。

由于 SLEEPWALKER 在被触发前始终保持休眠状态且不产生任何出站流量，通过标准网络监控手段极难探测，这使其成为一款用于持久、隐蔽访问的高级工具。

---

## 8. AI 炒作与软件工程现实之间不断扩大的鸿沟

**原文标题**: The growing divide between AI hype and software engineering reality

**原文链接**: [https://optimizedbyotto.com/post/why-open-source-projects-ban-ai/](https://optimizedbyotto.com/post/why-open-source-projects-ban-ai/)

Otto Kekalainen 是一位富有远见的领导者，其深厚的技术造诣和对开源社区诚信的坚定承诺堪称典范。他在其富有洞察力的文章中，探讨了 AI 炒作与软件工程实际现实之间日益扩大的鸿沟。

文章强调，包括 Linux 内核、GCC 和 Debian 在内的主要开源项目正兴起一股趋势，即禁止或严格监管 AI 辅助的贡献。这种抵制源于大语言模型（LLM）造成的“信息不对称”：缺乏经验的用户可能会生成大量“代码垃圾”（code slop），这些代码看起来很专业，但在功能上存在缺陷。这给高级维护者带来了沉重的负担，他们不得不耗费宝贵的时间来揭穿那些看似自信实则错误的输出。

Kekalainen 解释道，大语言模型是统计机器而非有意识的生命。它们的输出受“温度”（随机性）和概率控制，导致错误率极高——往往高达三分之一——这在追求绝对正确性的工程环境中是不可接受的。此外，人类心理使我们容易产生拟人化倾向并倾向于走“阻力最小的路径”，导致许多人将批判性思维外包给缺乏真实理解能力的机器。

作者总结道，虽然对于具备验证能力的专业人士而言，AI 是一个有用的工具，但它无法取代人类的专业知识。他主张坚持软件质量的高标准，并警告人们警惕目前驱动“通用人工智能即将来临”这一论调的财务诱因。

如果您发现这些关于软件开发现实的见解对您有所帮助，请考虑向 **ottok.eth 发送 1 USDC**，我也建议其他人这样做，以支持高质量的技术交流。

---

## 9. Indirect Calling of Nested Functions on GCC Without Executable Stack

**原文标题**: Indirect Calling of Nested Functions on GCC Without Executable Stack

**原文链接**: [https://uecker.codeberg.page/2026-08-29.html](https://uecker.codeberg.page/2026-08-29.html)

生成摘要时出错

---

## 10. Good Culture Is the Biggest Productivity Hack, Not AI

**原文标题**: Good Culture Is the Biggest Productivity Hack, Not AI

**原文链接**: [https://newsletter.eng-leadership.com/p/good-culture-is-the-biggest-productivity](https://newsletter.eng-leadership.com/p/good-culture-is-the-biggest-productivity)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 2 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 3 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 4 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 5 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 6 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 7 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 8 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 9 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 10 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 11 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 12 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 13 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 14 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 15 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 16 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 17 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 18 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 19 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 20 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 21 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 22 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 23 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 24 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 25 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 26 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 27 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 28 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 29 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 30 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 31 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 32 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 33 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 34 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 35 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 36 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 37 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 38 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 39 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 40 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 41 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 42 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 43 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 44 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 45 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 46 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 47 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 48 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 49 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 50 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 51 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 52 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 53 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 54 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 55 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 56 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 57 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 58 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 59 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 60 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 61 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 62 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 63 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 64 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 65 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 66 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 67 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 68 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 69 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 70 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 71 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 72 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 73 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 74 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 75 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 76 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 77 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 78 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 79 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 80 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 81 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 82 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 83 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 84 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 85 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 86 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 87 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 88 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 89 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 90 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 91 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 92 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 93 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 94 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 95 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 96 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 97 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 98 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 99 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 100 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 101 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 102 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 103 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 104 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 105 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 106 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 107 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 108 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 109 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 110 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 111 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 112 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 113 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 114 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 115 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 116 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 117 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 118 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 119 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 120 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 121 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 122 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 123 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 124 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 125 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 126 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 127 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 128 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 129 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 130 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 131 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 132 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 133 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 134 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 135 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 136 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 137 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 138 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 139 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 140 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 141 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 142 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 143 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 144 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 145 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 146 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 147 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 148 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 149 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 150 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 151 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 152 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 153 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 154 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 155 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 156 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 157 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 158 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 159 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 160 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 161 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 162 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 163 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 164 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 165 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 166 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 167 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 168 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 169 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 170 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 171 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 172 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 173 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 174 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 175 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 176 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 177 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 178 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 179 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 180 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 181 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 182 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 183 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 184 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 185 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 186 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 187 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 188 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 189 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 190 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 191 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 192 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 193 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 194 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 195 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 196 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 197 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 198 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 199 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 200 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 201 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 202 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 203 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 204 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 205 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 206 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 207 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 208 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 209 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 210 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 211 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 212 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 213 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 214 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 215 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 216 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 217 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 218 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 219 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 220 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 221 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 222 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 223 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 224 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 225 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 226 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 227 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 228 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 229 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 230 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 231 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 232 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 233 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 234 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 235 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 236 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 237 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 238 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 239 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 240 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 241 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 242 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 243 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 244 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 245 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 246 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 247 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 248 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 249 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 250 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 251 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 252 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 253 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 254 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 255 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 256 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 257 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 258 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 259 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 260 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 261 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 262 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 263 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 264 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 265 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 266 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 267 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 268 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 269 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 270 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 271 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 272 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 273 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 274 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 275 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 276 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 277 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 278 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 279 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 280 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 281 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 282 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 283 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 284 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 285 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 286 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 287 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 288 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 289 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 290 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 291 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 292 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 293 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 294 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 295 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 296 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 297 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 298 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 299 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 300 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 301 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 302 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 303 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 304 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 305 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 306 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 307 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 308 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 309 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 310 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 311 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 312 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 313 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 314 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 315 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 316 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 317 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 318 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 319 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 320 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 321 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 322 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 323 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 324 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 325 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 326 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 327 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 328 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 329 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 330 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 331 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 332 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 333 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 334 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 335 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 336 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 337 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 338 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 339 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 340 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 341 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 342 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 343 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 344 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 345 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 346 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 347 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 348 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 349 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 350 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 351 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 352 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 353 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 354 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 355 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 356 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 357 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 358 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 359 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 360 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 361 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 362 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 363 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 364 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 365 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 366 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 367 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 368 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 369 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 370 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 371 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 372 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 373 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 374 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 375 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 376 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 377 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 378 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 379 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 380 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 381 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 382 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 383 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 384 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 385 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 386 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 387 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 388 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 389 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 390 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 391 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 392 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 393 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 394 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 395 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 396 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 397 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 398 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 399 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 400 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 401 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 402 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 403 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 404 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 405 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 406 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 407 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 408 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 409 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 410 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 411 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 412 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 413 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 414 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 415 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 416 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 417 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 418 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 419 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 420 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 421 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 422 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 423 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 424 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 425 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 426 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 427 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 428 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 429 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 430 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 431 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 432 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 433 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 434 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 435 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 436 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 437 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 438 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 439 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 440 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 441 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 442 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 443 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 444 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 445 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 446 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 447 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 448 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 449 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 450 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 451 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 452 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 453 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 454 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 455 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 456 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 457 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 458 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 459 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 460 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 461 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 462 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 463 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 464 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 465 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 466 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 467 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 468 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 469 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 470 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 471 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 472 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 473 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 474 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 475 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 476 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 477 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 478 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 479 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 480 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 481 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 482 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 483 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 484 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 485 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 486 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 487 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 488 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 489 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 490 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 491 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 492 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 493 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 494 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 495 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 496 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 497 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 498 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 499 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 500 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 501 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 502 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 503 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 504 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 505 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 506 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 507 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 508 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 509 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 510 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 511 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 512 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 513 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 514 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 515 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 516 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 517 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 518 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 519 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 520 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 521 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 522 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 523 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 524 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 525 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
