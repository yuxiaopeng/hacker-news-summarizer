# Hacker News 热门文章摘要 (2026-08-29)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Show HN: Typebase – A single-folder back end you write in TypeScript

**原文标题**: Show HN: Typebase – A single-folder back end you write in TypeScript

**原文链接**: [https://typebase.io](https://typebase.io)

生成摘要时出错

---

## 12. Quantifying Colour

**原文标题**: Quantifying Colour

**原文链接**: [https://ekunazanu.foo/lab/quantifying-colour/](https://ekunazanu.foo/lab/quantifying-colour/)

生成摘要时出错

---

## 13. Vim's UserGettingBored Autocmd

**原文标题**: Vim's UserGettingBored Autocmd

**原文链接**: [https://evanhahn.com/usergettingbored-vim/](https://evanhahn.com/usergettingbored-vim/)

生成摘要时出错

---

## 14. Glacier Mice

**原文标题**: Glacier Mice

**原文链接**: [https://en.wikipedia.org/wiki/Glacier_mice](https://en.wikipedia.org/wiki/Glacier_mice)

生成摘要时出错

---

## 15. Kmart Digicam Mod Part 2

**原文标题**: Kmart Digicam Mod Part 2

**原文链接**: [https://mason.bearblog.dev/kmart-digicam-mod-part-2/](https://mason.bearblog.dev/kmart-digicam-mod-part-2/)

生成摘要时出错

---

## 16. Samsung's Processing-in-Memory (PIM)

**原文标题**: Samsung's Processing-in-Memory (PIM)

**原文链接**: [https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing](https://chipsandcheese.com/p/hot-chips-2026-samsungs-processing)

生成摘要时出错

---

## 17. EVE Online moves to Python 3

**原文标题**: EVE Online moves to Python 3

**原文链接**: [https://www.eveonline.com/news/view/the-move-to-python-3-begins](https://www.eveonline.com/news/view/the-move-to-python-3-begins)

生成摘要时出错

---

## 18. Creating the Aetheryte Radio

**原文标题**: Creating the Aetheryte Radio

**原文链接**: [https://haz.ee/posts/aetheryte-radio.html](https://haz.ee/posts/aetheryte-radio.html)

生成摘要时出错

---

## 19. A better SQL in 11 lines of code

**原文标题**: A better SQL in 11 lines of code

**原文链接**: [https://prela-lang.org/tutorial/](https://prela-lang.org/tutorial/)

生成摘要时出错

---

## 20. Nancy Grace Roman Space Telescope

**原文标题**: Nancy Grace Roman Space Telescope

**原文链接**: [https://science.nasa.gov/mission/roman-space-telescope/](https://science.nasa.gov/mission/roman-space-telescope/)

生成摘要时出错

---

## 21. GrapheneOS project: pixel 11 no longer supports hardware memory tagging (MTE)

**原文标题**: GrapheneOS project: pixel 11 no longer supports hardware memory tagging (MTE)

**原文链接**: [https://bsky.app/profile/grapheneos.org/post/3mua32q4ds22e](https://bsky.app/profile/grapheneos.org/post/3mua32q4ds22e)

生成摘要时出错

---

## 22. Trees for a Changing Climate and Resilient Urban Forest (2022)

**原文标题**: Trees for a Changing Climate and Resilient Urban Forest (2022)

**原文链接**: [https://www.coolboulder.org/news/trees-for-a-changing-climate-resilient-urban-forest](https://www.coolboulder.org/news/trees-for-a-changing-climate-resilient-urban-forest)

生成摘要时出错

---

## 23. Htmx 4.0

**原文标题**: Htmx 4.0

**原文链接**: [https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released)

生成摘要时出错

---

## 24. Boot a Virtual iPhone via Apple's Virtualization.framework

**原文标题**: Boot a Virtual iPhone via Apple's Virtualization.framework

**原文链接**: [https://github.com/Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli)

生成摘要时出错

---

## 25. Show HN: Galaxium, an experimental WebGPU space explorer

**原文标题**: Show HN: Galaxium, an experimental WebGPU space explorer

**原文链接**: [https://galaxium.app](https://galaxium.app)

生成摘要时出错

---

## 26. Hunting Down a Go Runtime Bug on 32-Bit Embedded Systems

**原文标题**: Hunting Down a Go Runtime Bug on 32-Bit Embedded Systems

**原文链接**: [https://sigma-star.at/blog/2026/08/go-runtime-netpoll-bug/](https://sigma-star.at/blog/2026/08/go-runtime-netpoll-bug/)

生成摘要时出错

---

## 27. StemDeck, a free, open-source and local AI stem separator

**原文标题**: StemDeck, a free, open-source and local AI stem separator

**原文链接**: [https://github.com/stemdeckapp/stemdeck](https://github.com/stemdeckapp/stemdeck)

生成摘要时出错

---

## 28. Time complexity of operations on Python's built-in types

**原文标题**: Time complexity of operations on Python's built-in types

**原文链接**: [https://docs.python.org/3.16/library/time-complexity.html](https://docs.python.org/3.16/library/time-complexity.html)

生成摘要时出错

---

## 29. I accidentally turned LLM memory into program analysis

**原文标题**: I accidentally turned LLM memory into program analysis

**原文链接**: [https://pwning.systems/posts/llm-memory-program-analysis/](https://pwning.systems/posts/llm-memory-program-analysis/)

生成摘要时出错

---

## 30. Europe's last regular standard-gauge steam passenger service

**原文标题**: Europe's last regular standard-gauge steam passenger service

**原文链接**: [https://parowozowniawolsztyn.pl/?page_id=2141](https://parowozowniawolsztyn.pl/?page_id=2141)

生成摘要时出错

---

## 31. Inception-style curved map for turn-by-turn directions

**原文标题**: Inception-style curved map for turn-by-turn directions

**原文链接**: [https://www.orbify.eu/demo/](https://www.orbify.eu/demo/)

生成摘要时出错

---

## 32. Just the rumour of a bug is enough to find an exploit these days

**原文标题**: Just the rumour of a bug is enough to find an exploit these days

**原文链接**: [https://anil.recoil.org/notes/rumour-is-the-exploit](https://anil.recoil.org/notes/rumour-is-the-exploit)

生成摘要时出错

---

## 33. TurboKV: Insanely fast Rust key-value store

**原文标题**: TurboKV: Insanely fast Rust key-value store

**原文链接**: [https://github.com/kingroryg/turbokv](https://github.com/kingroryg/turbokv)

生成摘要时出错

---

## 34. Debian votes to allow "responsible use of generative AI"

**原文标题**: Debian votes to allow "responsible use of generative AI"

**原文链接**: [https://lwn.net/Articles/1091231/](https://lwn.net/Articles/1091231/)

生成摘要时出错

---

## 35. Manifesto – who we are and what do we want (2002)

**原文标题**: Manifesto – who we are and what do we want (2002)

**原文链接**: [https://www.inventati.org/who/manifesto](https://www.inventati.org/who/manifesto)

生成摘要时出错

---

## 36. Parsing the Infamous Japanese Postal CSV

**原文标题**: Parsing the Infamous Japanese Postal CSV

**原文链接**: [https://www.dampfkraft.com/posuto.html](https://www.dampfkraft.com/posuto.html)

生成摘要时出错

---

## 37. Monzo Stand-In

**原文标题**: Monzo Stand-In

**原文链接**: [https://monzo.com/blog/tolerating-full-cloud-outages-with-monzo-stand-in](https://monzo.com/blog/tolerating-full-cloud-outages-with-monzo-stand-in)

生成摘要时出错

---

## 38. Our decision on Cursor following its acquisition by SpaceX

**原文标题**: Our decision on Cursor following its acquisition by SpaceX

**原文链接**: [https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/](https://openai.com/index/our-decision-on-cursor-following-its-acquisition-by-spacex/)

生成摘要时出错

---

## 39. Experiments with Plotter Art

**原文标题**: Experiments with Plotter Art

**原文链接**: [https://sometimes.digital/posts/experiments-with-plotter-art/](https://sometimes.digital/posts/experiments-with-plotter-art/)

生成摘要时出错

---

## 40. GUIs should be fully keyboard-driven

**原文标题**: GUIs should be fully keyboard-driven

**原文链接**: [https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html](https://ckardaris.com/blog/2026/08/28/keyboard-driven-guis.html)

生成摘要时出错

---

## 41. The Twelve-Factor App (2025)

**原文标题**: The Twelve-Factor App (2025)

**原文链接**: [https://12factor.net/](https://12factor.net/)

生成摘要时出错

---

## 42. Attimet (YC F24) Is Hiring Members of Technical Staff – Engineering and Research

**原文标题**: Attimet (YC F24) Is Hiring Members of Technical Staff – Engineering and Research

**原文链接**: [https://www.ycombinator.com/companies/attimet/jobs/6btZFDg-member-of-technical-staff-engineering](https://www.ycombinator.com/companies/attimet/jobs/6btZFDg-member-of-technical-staff-engineering)

生成摘要时出错

---

## 43. Does the Sumerian King List Align with Paleoclimate Events?

**原文标题**: Does the Sumerian King List Align with Paleoclimate Events?

**原文链接**: [https://www.vectorian.be/articles/2026-06-07/sumerian-king-list-paleoclimate-alignment-explorer/](https://www.vectorian.be/articles/2026-06-07/sumerian-king-list-paleoclimate-alignment-explorer/)

生成摘要时出错

---

## 44. Queen Caroline turned King Arthur into an 18C royal PR strategy

**原文标题**: Queen Caroline turned King Arthur into an 18C royal PR strategy

**原文链接**: [https://theconversation.com/how-queen-caroline-turned-king-arthur-into-an-18th-century-royal-pr-strategy-288244](https://theconversation.com/how-queen-caroline-turned-king-arthur-into-an-18th-century-royal-pr-strategy-288244)

生成摘要时出错

---

## 45. Curvature Beziers: Improving on a timeless recipe

**原文标题**: Curvature Beziers: Improving on a timeless recipe

**原文链接**: [https://acko.net/blog/curvature-beziers/](https://acko.net/blog/curvature-beziers/)

生成摘要时出错

---

## 46. EasyEffects can improve laptop speaker sound quality

**原文标题**: EasyEffects can improve laptop speaker sound quality

**原文链接**: [https://www.osnews.com/story/145883/easyeffects-should-be-part-of-every-linux-distribution-and-desktop-environment-to-massively-improve-laptop-speaker-sound-quality/](https://www.osnews.com/story/145883/easyeffects-should-be-part-of-every-linux-distribution-and-desktop-environment-to-massively-improve-laptop-speaker-sound-quality/)

生成摘要时出错

---

## 47. GLM-5.3 is now open-weight

**原文标题**: GLM-5.3 is now open-weight

**原文链接**: [https://huggingface.co/zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3)

生成摘要时出错

---

## 48. Visual Analysis of Binary Files

**原文标题**: Visual Analysis of Binary Files

**原文链接**: [https://binvis.io/#/](https://binvis.io/#/)

生成摘要时出错

---

## 49. Verschlimmbesserung: The Word Your Software Updates Need

**原文标题**: Verschlimmbesserung: The Word Your Software Updates Need

**原文链接**: [https://geekyschmidt.com/post/2026-08-25-verschlimmbesserung/](https://geekyschmidt.com/post/2026-08-25-verschlimmbesserung/)

生成摘要时出错

---

## 50. Migrating to HTTPX2

**原文标题**: Migrating to HTTPX2

**原文链接**: [https://github.com/openai/openai-python/blob/main/httpx2.md](https://github.com/openai/openai-python/blob/main/httpx2.md)

生成摘要时出错

---

## 51. 法官裁定特朗普政府将 Anthropic 列入黑名单违法。

**原文标题**: Judge rules Trump administration’s blacklisting of Anthropic was illegal

**原文链接**: [https://www.nytimes.com/2026/08/27/technology/anthropic-government-blacklisting-ruling.html](https://www.nytimes.com/2026/08/27/technology/anthropic-government-blacklisting-ruling.html)

Unable to access the article link.

---

## 52. Iceland votes on whether to restart talks on joining EU

**原文标题**: Iceland votes on whether to restart talks on joining EU

**原文链接**: [https://www.bbc.com/news/articles/cn45vdxyvvlo](https://www.bbc.com/news/articles/cn45vdxyvvlo)

生成摘要时出错

---

## 53. Run Qwen3.8 27B locally: real numbers from my Mac Studio

**原文标题**: Run Qwen3.8 27B locally: real numbers from my Mac Studio

**原文链接**: [https://terminalbytes.com/run-qwen-3-8-27b-locally/](https://terminalbytes.com/run-qwen-3-8-27b-locally/)

生成摘要时出错

---

## 54. Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment

**原文标题**: Autonomous Mathematical Discovery in an Open-World Multi-Agent Environment

**原文链接**: [https://arxiv.org/abs/2608.23691](https://arxiv.org/abs/2608.23691)

生成摘要时出错

---

## 55. State of the Map 2026

**原文标题**: State of the Map 2026

**原文链接**: [https://2026.stateofthemap.org/](https://2026.stateofthemap.org/)

生成摘要时出错

---

## 56. Box of 300 Love Letters Showed Up, What Whimsical WWII Soldier Who Wrote Them?

**原文标题**: Box of 300 Love Letters Showed Up, What Whimsical WWII Soldier Who Wrote Them?

**原文链接**: [https://www.smithsonianmag.com/history/this-box-of-300-love-letters-showed-up-out-of-the-blue-who-was-the-whimsical-world-war-ii-soldier-who-wrote-them-180989300/](https://www.smithsonianmag.com/history/this-box-of-300-love-letters-showed-up-out-of-the-blue-who-was-the-whimsical-world-war-ii-soldier-who-wrote-them-180989300/)

生成摘要时出错

---

## 57. U.S. sanctions against the A/I Collective

**原文标题**: U.S. sanctions against the A/I Collective

**原文链接**: [https://www.inventati.org/](https://www.inventati.org/)

生成摘要时出错

---

## 58. Smaller reactors bring nuclear power closer to fulfilling its promise

**原文标题**: Smaller reactors bring nuclear power closer to fulfilling its promise

**原文链接**: [https://www.nature.com/articles/d41586-026-02506-4](https://www.nature.com/articles/d41586-026-02506-4)

生成摘要时出错

---

## 59. Doctors are finally learning to manage antidepressant withdrawal

**原文标题**: Doctors are finally learning to manage antidepressant withdrawal

**原文链接**: [https://www.newscientist.com/article/2584861-antidepressant-withdrawal-symptoms-are-prompting-a-radical-rethink-of-how-we-treat-depression/](https://www.newscientist.com/article/2584861-antidepressant-withdrawal-symptoms-are-prompting-a-radical-rethink-of-how-we-treat-depression/)

生成摘要时出错

---

## 60. 9th Circuit sides with states in Kalshi gambling fight

**原文标题**: 9th Circuit sides with states in Kalshi gambling fight

**原文链接**: [https://azmirror.com/2026/08/28/9th-circuit-sides-with-states-in-kalshi-gambling-fight-potentially-reviving-arizonas-prosecution/](https://azmirror.com/2026/08/28/9th-circuit-sides-with-states-in-kalshi-gambling-fight-potentially-reviving-arizonas-prosecution/)

生成摘要时出错

---

## 61. Nvidia agrees to acquire Hugging Face for $13B

**原文标题**: Nvidia agrees to acquire Hugging Face for $13B

**原文链接**: [https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8](https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8)

生成摘要时出错

---

## 62. Get your Windows license refund

**原文标题**: Get your Windows license refund

**原文链接**: [https://en.refund4freedom.org/](https://en.refund4freedom.org/)

生成摘要时出错

---

## 63. SteamOS 3.9.0 Preview

**原文标题**: SteamOS 3.9.0 Preview

**原文链接**: [https://store.steampowered.com/news/app/1675200/view/689767056035283412](https://store.steampowered.com/news/app/1675200/view/689767056035283412)

生成摘要时出错

---

## 64. Global demand for sand spawned a worldwide boom in illegal mining (2015)

**原文标题**: Global demand for sand spawned a worldwide boom in illegal mining (2015)

**原文链接**: [https://www.wired.com/2015/03/illegal-sand-mining/](https://www.wired.com/2015/03/illegal-sand-mining/)

生成摘要时出错

---

## 65. Interactive Warhammer 40k Galaxy Map

**原文标题**: Interactive Warhammer 40k Galaxy Map

**原文链接**: [https://cartographia40k.com/](https://cartographia40k.com/)

生成摘要时出错

---

## 66. HTTPX2 – A next-generation HTTP client for Python

**原文标题**: HTTPX2 – A next-generation HTTP client for Python

**原文链接**: [https://github.com/pydantic/httpx2](https://github.com/pydantic/httpx2)

生成摘要时出错

---

## 67. Debugging my new network, when 10 Gigabit Ethernet Runs at 300 Megabits

**原文标题**: Debugging my new network, when 10 Gigabit Ethernet Runs at 300 Megabits

**原文链接**: [https://www.hanselman.com/blog/debugging-my-new-network-when-10-gigabit-ethernet-runs-at-300-megabits](https://www.hanselman.com/blog/debugging-my-new-network-when-10-gigabit-ethernet-runs-at-300-megabits)

生成摘要时出错

---

## 68. An investigation into the state of corvid–human relations

**原文标题**: An investigation into the state of corvid–human relations

**原文链接**: [https://www.audubon.org/magazine/are-crows-really-our-friends](https://www.audubon.org/magazine/are-crows-really-our-friends)

生成摘要时出错

---

## 69. Some conservationists are helping to restore Africa’s wild dog populations

**原文标题**: Some conservationists are helping to restore Africa’s wild dog populations

**原文链接**: [https://www.smithsonianmag.com/science-nature/africa-wild-dogs-most-hated-carnivores-continent-heres-why-conservationists-saving-them-anyway-180989287/](https://www.smithsonianmag.com/science-nature/africa-wild-dogs-most-hated-carnivores-continent-heres-why-conservationists-saving-them-anyway-180989287/)

生成摘要时出错

---

## 70. Sloc Cloc and Code 4.0 (scc) – Finding the files that need the most attention

**原文标题**: Sloc Cloc and Code 4.0 (scc) – Finding the files that need the most attention

**原文链接**: [https://boyter.org/posts/sloc-cloc-code-hotspots-finding-files-that-need-attention/](https://boyter.org/posts/sloc-cloc-code-hotspots-finding-files-that-need-attention/)

生成摘要时出错

---

## 71. Luanti removed from Google Play due to baseless AI copyright notice

**原文标题**: Luanti removed from Google Play due to baseless AI copyright notice

**原文链接**: [https://blog.luanti.org/2026/08/27/luanti-dmca-tracer-ai/](https://blog.luanti.org/2026/08/27/luanti-dmca-tracer-ai/)

生成摘要时出错

---

## 72. Show HN: Sesame - a local-first, open-source password manager

**原文标题**: Show HN: Sesame - a local-first, open-source password manager

**原文链接**: [https://usesesame.app/](https://usesesame.app/)

生成摘要时出错

---

## 73. Identifying fake cosmetics using AI

**原文标题**: Identifying fake cosmetics using AI

**原文链接**: [https://groverlab.org/hnbfpr/2026-08-26-ai-counterfeit-cosmetics.html](https://groverlab.org/hnbfpr/2026-08-26-ai-counterfeit-cosmetics.html)

生成摘要时出错

---

## 74. Kumander Linux – A Linux Distro with a Windows 7 Desktop

**原文标题**: Kumander Linux – A Linux Distro with a Windows 7 Desktop

**原文链接**: [https://www.kumander.org/](https://www.kumander.org/)

生成摘要时出错

---

## 75. Senator calls for criminal investigation of RFK Jr after Guardian report

**原文标题**: Senator calls for criminal investigation of RFK Jr after Guardian report

**原文链接**: [https://www.theguardian.com/us-news/2026/aug/27/rfk-jr-confirmation-hearing-investigation](https://www.theguardian.com/us-news/2026/aug/27/rfk-jr-confirmation-hearing-investigation)

生成摘要时出错

---

## 76. “It works better in the app”

**原文标题**: “It works better in the app”

**原文链接**: [https://shkspr.mobi/blog/2026/08/it-works-better-in-the-app/](https://shkspr.mobi/blog/2026/08/it-works-better-in-the-app/)

生成摘要时出错

---

## 77. ICE eyes spending up to $2M on Boston Dynamics robot dogs to up 'officer safety'

**原文标题**: ICE eyes spending up to $2M on Boston Dynamics robot dogs to up 'officer safety'

**原文链接**: [https://www.bostonglobe.com/2026/08/29/business/boston-dynamics-robot-dog-ice/](https://www.bostonglobe.com/2026/08/29/business/boston-dynamics-robot-dog-ice/)

生成摘要时出错

---

## 78. Show HN: SubSmith – Turn your own videos into language-learning material

**原文标题**: Show HN: SubSmith – Turn your own videos into language-learning material

**原文链接**: [https://subsmith.app](https://subsmith.app)

生成摘要时出错

---

## 79. Saving 100 terabytes of memory by optimizing 1.1.1.1's DNS cache

**原文标题**: Saving 100 terabytes of memory by optimizing 1.1.1.1's DNS cache

**原文链接**: [https://blog.cloudflare.com/dns-cache-memory-optimization-1111/](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/)

生成摘要时出错

---

## 80. Processing in Memory: DRAM Is About to Do Math

**原文标题**: Processing in Memory: DRAM Is About to Do Math

**原文链接**: [https://ben3d.ca/blog/processing-in-memory](https://ben3d.ca/blog/processing-in-memory)

生成摘要时出错

---

## 81. “Weird” is a weird word

**原文标题**: “Weird” is a weird word

**原文链接**: [https://www.deadlanguagesociety.com/p/weird-is-a-weird-word](https://www.deadlanguagesociety.com/p/weird-is-a-weird-word)

生成摘要时出错

---

## 82. Introduction to Probability – 2nd Edition

**原文标题**: Introduction to Probability – 2nd Edition

**原文链接**: [https://open.umn.edu/opentextbooks/textbooks/introduction-to-probability](https://open.umn.edu/opentextbooks/textbooks/introduction-to-probability)

生成摘要时出错

---

## 83. Bhartrhari's Paradox

**原文标题**: Bhartrhari's Paradox

**原文链接**: [https://www.futilitycloset.com/2026/08/18/bhartrharis-paradox/](https://www.futilitycloset.com/2026/08/18/bhartrharis-paradox/)

生成摘要时出错

---

## 84. Review: Chuwi's $449 Unibook laptop is a funhouse-mirror MacBook Neo

**原文标题**: Review: Chuwi's $449 Unibook laptop is a funhouse-mirror MacBook Neo

**原文链接**: [https://arstechnica.com/gadgets/2026/08/review-chuwis-449-unibook-laptop-is-a-funhouse-mirror-macbook-neo/](https://arstechnica.com/gadgets/2026/08/review-chuwis-449-unibook-laptop-is-a-funhouse-mirror-macbook-neo/)

生成摘要时出错

---

## 85. Small Models Have Arrived

**原文标题**: Small Models Have Arrived

**原文链接**: [https://calv.info/small-models-have-arrived](https://calv.info/small-models-have-arrived)

生成摘要时出错

---

## 86. Aspirational Clownmaxxing and Joey's cadillac todo list

**原文标题**: Aspirational Clownmaxxing and Joey's cadillac todo list

**原文链接**: [https://charlesleifer.com/blog/aspirational-clownmaxxing-and-joey-s-cadillac-todo-list/](https://charlesleifer.com/blog/aspirational-clownmaxxing-and-joey-s-cadillac-todo-list/)

生成摘要时出错

---

## 87. Music publishers sue Anthropic, allege "blantant theft" of copyrighted music

**原文标题**: Music publishers sue Anthropic, allege "blantant theft" of copyrighted music

**原文链接**: [https://www.axios.com/2026/08/29/anthropic-sony-warner-music-copyright](https://www.axios.com/2026/08/29/anthropic-sony-warner-music-copyright)

生成摘要时出错

---

## 88. Show HN: Qwiksi a CLI tool for adding your signature to a PDFs

**原文标题**: Show HN: Qwiksi a CLI tool for adding your signature to a PDFs

**原文链接**: [https://github.com/krisraven/qwiksi](https://github.com/krisraven/qwiksi)

生成摘要时出错

---

## 89. Hilariously fast volume computation with the divergence theorem (2018)

**原文标题**: Hilariously fast volume computation with the divergence theorem (2018)

**原文链接**: [https://alyssarosenzweig.ca/blog/hilariously-fast-volume-computation-with-the-divergence-theorem.html](https://alyssarosenzweig.ca/blog/hilariously-fast-volume-computation-with-the-divergence-theorem.html)

生成摘要时出错

---

## 90. Zohran and the Short Link

**原文标题**: Zohran and the Short Link

**原文链接**: [https://iamwillwang.com/notes/zohran-and-the-short-link/](https://iamwillwang.com/notes/zohran-and-the-short-link/)

生成摘要时出错

---

## 91. 507 Mechanical Movements

**原文标题**: 507 Mechanical Movements

**原文链接**: [https://507movements.com/](https://507movements.com/)

生成摘要时出错

---

## 92. Microduck

**原文标题**: Microduck

**原文链接**: [https://pollen-robotics.com/microduck/](https://pollen-robotics.com/microduck/)

生成摘要时出错

---

## 93. Terminal-Bench-Science: Evaluating AI agents on scientific research workflows

**原文标题**: Terminal-Bench-Science: Evaluating AI agents on scientific research workflows

**原文链接**: [https://www.terminal-bench-science.ai/announcement](https://www.terminal-bench-science.ai/announcement)

生成摘要时出错

---

## 94. Sony Music and Warner Chappell Are Suing Anthropic

**原文标题**: Sony Music and Warner Chappell Are Suing Anthropic

**原文链接**: [https://www.theverge.com/ai-artificial-intelligence/986438/sony-music-warner-chappell-anthropic-lawsuit-copyright](https://www.theverge.com/ai-artificial-intelligence/986438/sony-music-warner-chappell-anthropic-lawsuit-copyright)

生成摘要时出错

---

## 95. Service Discontinued

**原文标题**: Service Discontinued

**原文链接**: [https://twitterwebviewer.com/?rev=1](https://twitterwebviewer.com/?rev=1)

生成摘要时出错

---

## 96. How Dactyl Works

**原文标题**: How Dactyl Works

**原文链接**: [https://dactyl.dev/blog/how-dactyl-works/](https://dactyl.dev/blog/how-dactyl-works/)

生成摘要时出错

---

## 97. Sovereign Tech Agency invests €500k in Flatpak

**原文标题**: Sovereign Tech Agency invests €500k in Flatpak

**原文链接**: [https://modal.cx/blog/announcing-flatpak-sta/](https://modal.cx/blog/announcing-flatpak-sta/)

生成摘要时出错

---

## 98. The IBM PC, Part 2: Tsunami

**原文标题**: The IBM PC, Part 2: Tsunami

**原文链接**: [https://technicshistory.com/2026/08/29/the-ibm-pc-part-2-tsunami/](https://technicshistory.com/2026/08/29/the-ibm-pc-part-2-tsunami/)

生成摘要时出错

---

## 99. Show HN: The load-bearing vocabulary of Claude

**原文标题**: Show HN: The load-bearing vocabulary of Claude

**原文链接**: [https://louisabraham.github.io/load-bearing/](https://louisabraham.github.io/load-bearing/)

生成摘要时出错

---

## 100. Stopping the smart TV from being used against you

**原文标题**: Stopping the smart TV from being used against you

**原文链接**: [https://www.s-config.com/stopping-a-smart-tv-from-being-used-against-you/](https://www.s-config.com/stopping-a-smart-tv-from-being-used-against-you/)

生成摘要时出错

---

