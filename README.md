# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-08.md)

*最后自动更新时间: 2026-11-08 21:22:22*
## 1. 高盛正撤回面向其银行家和交易员的 Claude Code

**原文标题**: Goldman Sachs Is Pulling Claude Code from Its Bankers and Traders

**原文链接**: [https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers](https://www.thestateofai.com/news/goldman-sachs-claude-code-traders-bankers)

高盛已将 AI 编程工具（包括 Anthropic 的 Claude Code 和微软旗下的 GitHub）的使用权限缩减至仅限其 1.2 万名工程师。这一政策取消了银行家和交易员的使用权限，此前他们已开始利用这些工具监测客户资金流并构建市场模型。

此举标志着高盛立场较今年早些时候发生了转变，当时首席信息官马尔科·阿根蒂（Marco Argenti）曾称赞“氛围编程”（vibe coding）——即非技术人员构建自用工具的行为。高盛此次立场逆转主要源于以下几点担忧：

*   **风险与监督：** 与工程师编写的代码不同，交易员创建的脚本往往绕过了正式的审查和测试。如果 AI 生成的代码在处理异常市场情况时出错，将带来财务损失风险。
*   **合规性：** AI 代理可能会突破隔离不同银行业务职能的法定信息壁垒（“中国墙”）。
*   **运营安全：** 编程代理可以在含有敏感客户数据的机器上自主编写并执行程序。
*   **成本：** 这些工具按 Token 计费；在大型机构中若不加控制地使用，可能导致巨额且难以预见的支出。

这一变动的时机尤其引人注目，因为高盛正是 Anthropic 即将进行的 IPO 的主承销商。在高盛收紧权限的同时，巴克莱银行等竞争对手则反其道而行之，正在扩大 Claude Code 的使用范围以提升开发效率。

归根结底，这一限制反映了受严格监管的行业中日益增长的诉求：即确保 AI 生成的软件必须接受专业的工程控制。尽管此举令部分员工感到沮丧，但它凸显了 AI 的快速普及与交易大厅严苛安全标准之间的冲突。

---

## 2. 我如何对抗 AI 脑疲劳

**原文标题**: How I Fight AI Brain Fry

**原文链接**: [https://sergeykuhne.com/blog/fighting-ai-brain-fry](https://sergeykuhne.com/blog/fighting-ai-brain-fry)

在《我如何对抗 AI 大脑疲劳》（How I Fight AI Brain Fry）一文中，作者探讨了因同时处理多个并发的 AI 对话线程和终端上下文而导致的认知超负荷——即“大脑疲劳”问题。为了解决高速 AI 开发中固有的精疲力竭和注意力破碎问题，作者从瞬时的对话会话转向了结构化的、集成 Git 的**优先级队列**。

**系统的核心组件：**
*   **基于 Git 的工作流：** 每一项任务都以 Markdown 文件的形式记录在代码库中。这确保了项目状态是已提交的记录，而非仅存在于对话窗口或用户的记忆中。
*   **智能代理处理：** 由 AI 代理负责处理重复性的“循环”，包括研究工单、在分支上构建代码以及运行测试。关键在于，代理被禁止做出最终决策或部署到生产环境。
*   **所有者收件箱：** 通过脚本解析 Git 看板，为用户呈现一份需要人工判断的优先级清单，例如代码审查或架构权衡。
*   **简化的审查界面：** 作者不再翻阅终端历史记录，而是利用 Claude Artifact（一个基于 Git 重建的单页仪表板）来审查变更并给出裁定。

**心理层面的益处：**
该策略的核心在于“上下文闭合”。通过加载一个工单、做出决定并立即将其返回队列，作者卸下了记忆未完成任务的心理负担。这种“一次只做一件事”的方法防止了心理“内存”溢满，从而在没有多任务干扰的情况下实现深度专注。尽管工作依然繁重，但该系统建立了一种可持续的线性工作流，防止开发者在复杂的 AI 驱动开发中迷失方向。

---

## 3. Dux: Free, open-source Wayland desktop shell with file manager and theming

**原文标题**: Dux: Free, open-source Wayland desktop shell with file manager and theming

**原文链接**: [https://duxlabs.dev/](https://duxlabs.dev/)

生成摘要时出错

---

## 4. 英伟达董事会正在调查黄仁勋

**原文标题**: Nvidia Board of Directors Is Investigating Jensen Huang

**原文链接**: [https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors](https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors)

2026年11月8日，英伟达（NVIDIA）董事会宣布对创始人兼首席执行官黄仁勋启动一项独立调查。此次调查源于有报道称，黄仁勋曾是外国情报活动的目标。

该调查由独立董事委员会在外部法律顾问的协助下进行监督。董事会强调，其首要任务是维护美国的国家安全和经济安全。

声明的关键细节包括：
*   **目前调查结果：** 董事会目前没有理由认为英伟达的专有机密或国家安全已遭到损害。
*   **配合情况：** 黄仁勋对此次审查表示全力支持，并正配合委员会的工作。
*   **领导地位：** 在调查进行期间，董事会维持对黄仁勋及其领导团队的信心。

董事会承诺将随着调查的进展提供进一步的更新。

---

## 5. Outlook.com 正悄悄拦截未配置 DMARC 域名的邮件

**原文标题**: Outlook.com Is Quietly Rejecting Email from Domains Without DMARC

**原文链接**: [https://mailroute.net/blog/outlook-rejecting-email-without-dmarc](https://mailroute.net/blog/outlook-rejecting-email-without-dmarc)

Beginning November 5, 2024, Microsoft’s consumer email services—including Outlook.com, Hotmail, Live, and MSN—began quietly rejecting emails from domains that do not have a DMARC record. Unlike previous mandates targeting bulk senders (those sending over 5,000 messages daily), this change affects small, low-volume senders and was implemented without an official announcement.

**Key Issues**
The primary danger of this update is its inconsistency. Microsoft is only rejecting a portion of affected traffic, meaning some emails pass through while others bounce with a "550 5.7.1" error. This intermittent failure makes the problem difficult to detect, as senders may assume a one-time glitch while recipients remain unaware that messages were sent. Even domains with functional SPF and DKIM records are being blocked if they lack the DMARC record that ties those protocols to the "From" address.

**The Solution**
The immediate fix is to add a single TXT record to the domain's DNS:
`v=DMARC1; p=none`

The `p=none` policy is a "safe" entry that satisfies Microsoft’s requirement without altering how other email providers handle the mail. However, for DMARC to work, the sender must also ensure that either SPF or DKIM is correctly configured and aligned with their "From" domain.

**The Broader Context**
This shift reflects a growing industry trend where major mailbox providers are making DMARC the baseline requirement for all email, not just bulk marketing. While currently a hurdle for small businesses, implementing DMARC is a critical step in preventing domain spoofing and improving overall email security. Senders are encouraged to add the record immediately to avoid delivery disruptions.

---

## 6. 声明式拖拽

**原文标题**: Declarative Dragging

**原文链接**: [https://declarative-dragging.github.io/](https://declarative-dragging.github.io/)

由 Joshua Horowitz、Andrew Blinn 和 Jeffrey Heer 撰写的 UIST 2026 最佳论文 **Declarative Dragging**（声明式拖拽）提出了一种创建拖放交互的新颖方法。传统上，构建此类功能是一个“琐碎且繁杂”的过程，需要为几何图形和动画编写复杂的代码。Declarative Dragging (D2) 通过让开发者指定**未来的模型状态**而非手动定义视觉行为，简化了这一过程。

其核心机制涉及一个能够推测性地渲染应用程序潜在未来状态的引擎。通过识别被拖拽元素在这些推测渲染中出现的位置，系统会自动合成流畅且响应迅速的交互。这使开发者的重心从底层的坐标操作转向了高层的语义规则。

作者在 **Dragology** 中实现了这一概念，这是一个针对 SVG Web 界面的库。Dragology 采用模型驱动且具备可组合性，允许用户叠加吸附（snapping）、漂浮（floating）和过渡（transitions）等功能。该系统对于“并行表示”特别有效，即当用户与系统的一个视图（如数学排列）交互时，可以实时流利地更新其他视图。

该项目源于将数字数学和编程变得更加“触感化”的愿景。它已被应用于多个领域，包括：
*   **教育与数学：** 可视化扭曲树、代数和辫子理论（braid theory）。
*   **游戏设计：** 利用 3D 环境和游戏手柄的具身数学游戏。
*   **软件开发：** 集成到学术编程环境“Hazel”中，使代码重构可以通过触控进行探索。

通过降低丰富触觉交互的实现门槛，Declarative Dragging 使教育工作者、研究人员和创意工具开发者能够创建更具表现力、更“生动”（juicy）的界面，而无需承担传统复杂几何编程的额外负担。

---

## 7. RAM Altman：Linux 脚本每天向 Sam Altman 汇报你电脑中的闲置内存量

**原文标题**: RAM Altman: Linux Script Emails Sam Altman Daily How Much Unused RAM in Your PC

**原文链接**: [https://respawnfirst.com/linux-script-emails-sam-altman-unused-ram-ram-altman/](https://respawnfirst.com/linux-script-emails-sam-altman-unused-ram-ram-altman/)

针对 OpenAI 首席执行官萨姆·奥特曼（Sam Altman）关于优先满足 AI 数据中心需求而非消费电子产品的争议性言论，开源开发者伊恩·凯（Iain Kay）发布了一款名为“Ram Altman”的 Linux BASH 脚本。

该脚本旨在监控系统的空闲内存。如果未使用内存超过 10%，该工具会从一系列讽刺性的邮件模板中进行选择并发送给奥特曼，以嘲讽其“超级大反派”般的言论。其中一封示例邮件告知奥特曼，用户正将特定容量的内存“负责任地囤积”在书桌上，而非投入到数据中心。

为防止该工具被用于针对 OpenAI 的自动化邮件伪造或拒绝服务攻击，凯特意将邮件服务器设为默认未配置状态。用户必须具备自行设置外发邮件的技术能力，不过该代码库包含了一个用于本地测试的“空运行”（dry-run）标志，以及一个嘲讽苹果焊接内存和全球 DRAM 短缺的幽默问答（FAQ）板块。

“Ram Altman”项目突显了互联网对 OpenAI 硬件立场的强烈抵制。在该脚本发布并引发广泛批评后，奥特曼在 X（原 Twitter）上改口，声称其原始言论被断章取义，并坚称他希望消费者能够拥有所需的全部硬件。

---

## 8. Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU

**原文标题**: Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU

**原文链接**: [https://github.com/synchopate/llama-modchip](https://github.com/synchopate/llama-modchip)

生成摘要时出错

---

## 9. 爱德华·霍普的标志性画作《夜游者》

**原文标题**: Edward Hopper's Iconic Painting, "Nighthawks

**原文链接**: [https://lithub.com/the-story-behind-edward-hoppers-iconic-painting-nighthawks/](https://lithub.com/the-story-behind-edward-hoppers-iconic-painting-nighthawks/)

In this excerpt from *Edward Hopper: A Life*, Louis Shadwick explores the creation, context, and enduring legacy of Hopper’s most famous painting, *Nighthawks*. 

**Process and Inspiration**
Started in late 1941, the painting was a product of meticulous planning, involving nineteen preparatory sketches. Hopper and his wife, Jo, modeled for the figures in the diner. While art historians have long searched for the exact location of the restaurant on Greenwich Avenue, Shadwick suggests the diner is likely an amalgamation of several New York landmarks—including "Crawford Lunch" and the Flatiron Building—designed to create a stylized, "fishbowl" aesthetic.

**Wartime Context**
The painting’s production coincided with the United States' entry into World War II following the attack on Pearl Harbor. Letters from Jo Hopper reveal a period of intense anxiety, marked by fears of New York being bombed and the enforcement of nightly blackouts. Shadwick argues that Hopper’s obsession with the canvas served as both a distraction and a response to this tension. The diner, glowing with artificial light amidst the darkness, symbolizes a "poignantly American resilience" and a gesture of endurance during the nation’s darkest hours.

**Themes and Legacy**
Though *Nighthawks* is frequently cited as the definitive portrayal of modern loneliness and urban alienation, Hopper himself felt these interpretations were "overdone," preferring the painting’s emotional depth to remain unformulated. Shadwick highlights how the work bridges European influences—such as Van Gogh’s night scenes and Surrealist mystery—with a uniquely American realist tradition. Ultimately, the painting captures a sense of "heroic isolation" and Emersonian self-reliance, turning the "quiet menace" of the city into something iconic, stoic, and alluring.

---

## 10. 作为思考工具的写作

**原文标题**: Writing as a thinking tool

**原文链接**: [http://muratbuffalo.blogspot.com/2026/11/writing-as-thinking-tool.html](http://muratbuffalo.blogspot.com/2026/11/writing-as-thinking-tool.html)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 2 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 3 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 4 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 5 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 6 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 7 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 8 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 9 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 10 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 11 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 12 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 13 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 14 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 15 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 16 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 17 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 18 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 19 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 20 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 21 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 22 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 23 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 24 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 25 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 26 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 27 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 28 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 29 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 30 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 31 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 32 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 33 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 34 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 35 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 36 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 37 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 38 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 39 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 40 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 41 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 42 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 43 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 44 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 45 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 46 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 47 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 48 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 49 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 50 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 51 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 52 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 53 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 54 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 55 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 56 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 57 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 58 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 59 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 60 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 61 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 62 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 63 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 64 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 65 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 66 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 67 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 68 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 69 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 70 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 71 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 72 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 73 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 74 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 75 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 76 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 77 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 78 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 79 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 80 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 81 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 82 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 83 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 84 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 85 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 86 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 87 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 88 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 89 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 90 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 91 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 92 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 93 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 94 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 95 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 96 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 97 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 98 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 99 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 100 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 101 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 102 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 103 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 104 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 105 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 106 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 107 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 108 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 109 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 110 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 111 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 112 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 113 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 114 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 115 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 116 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 117 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 118 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 119 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 120 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 121 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 122 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 123 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 124 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 125 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 126 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 127 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 128 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 129 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 130 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 131 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 132 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 133 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 134 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 135 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 136 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 137 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 138 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 139 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 140 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 141 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 142 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 143 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 144 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 145 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 146 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 147 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 148 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 149 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 150 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 151 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 152 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 153 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 154 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 155 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 156 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 157 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 158 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 159 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 160 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 161 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 162 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 163 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 164 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 165 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 166 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 167 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 168 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 169 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 170 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 171 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 172 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 173 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 174 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 175 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 176 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 177 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 178 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 179 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 180 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 181 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 182 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 183 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 184 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 185 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 186 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 187 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 188 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 189 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 190 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 191 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 192 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 193 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 194 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 195 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 196 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 197 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 198 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 199 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 200 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 201 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 202 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 203 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 204 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 205 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 206 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 207 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 208 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 209 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 210 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 211 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 212 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 213 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 214 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 215 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 216 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 217 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 218 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 219 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 220 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 221 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 222 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 223 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 224 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 225 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 226 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 227 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 228 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 229 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 230 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 231 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 232 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 233 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 234 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 235 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 236 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 237 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 238 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 239 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 240 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 241 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 242 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 243 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 244 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 245 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 246 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 247 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 248 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 249 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 250 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 251 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 252 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 253 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 254 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 255 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 256 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 257 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 258 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 259 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 260 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 261 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 262 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 263 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 264 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 265 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 266 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 267 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 268 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 269 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 270 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 271 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 272 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 273 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 274 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 275 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 276 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 277 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 278 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 279 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 280 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 281 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 282 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 283 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 284 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 285 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 286 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 287 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 288 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 289 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 290 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 291 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 292 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 293 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 294 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 295 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 296 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 297 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 298 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 299 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 300 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 301 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 302 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 303 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 304 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 305 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 306 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 307 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 308 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 309 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 310 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 311 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 312 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 313 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 314 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 315 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 316 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 317 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 318 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 319 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 320 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 321 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 322 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 323 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 324 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 325 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 326 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 327 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 328 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 329 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 330 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 331 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 332 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 333 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 334 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 335 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 336 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 337 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 338 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 339 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 340 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 341 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 342 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 343 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 344 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 345 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 346 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 347 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 348 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 349 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 350 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 351 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 352 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 353 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 354 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 355 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 356 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 357 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 358 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 359 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 360 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 361 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 362 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 363 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 364 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 365 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 366 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 367 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 368 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 369 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 370 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 371 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 372 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 373 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 374 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 375 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 376 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 377 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 378 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 379 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 380 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 381 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 382 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 383 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 384 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 385 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 386 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 387 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 388 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 389 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 390 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 391 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 392 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 393 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 394 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 395 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 396 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 397 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 398 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 399 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 400 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 401 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 402 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 403 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 404 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 405 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 406 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 407 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 408 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 409 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 410 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 411 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 412 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 413 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 414 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 415 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 416 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 417 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 418 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 419 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 420 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 421 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 422 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 423 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 424 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 425 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 426 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 427 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 428 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 429 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 430 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 431 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 432 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 433 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 434 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 435 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 436 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 437 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 438 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 439 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 440 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 441 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 442 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 443 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 444 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 445 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 446 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 447 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 448 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 449 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 450 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 451 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 452 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 453 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 454 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 455 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 456 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 457 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 458 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 459 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 460 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 461 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 462 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 463 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 464 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 465 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 466 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 467 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 468 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 469 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 470 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 471 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 472 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 473 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 474 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 475 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 476 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 477 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 478 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 479 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 480 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 481 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 482 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 483 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 484 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 485 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 486 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 487 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 488 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 489 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 490 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 491 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 492 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 493 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 494 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 495 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 496 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 497 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 498 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 499 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 500 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 501 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 502 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 503 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 504 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 505 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 506 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 507 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 508 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 509 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 510 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 511 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 512 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 513 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 514 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 515 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 516 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 517 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 518 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 519 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 520 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 521 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 522 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 523 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 524 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 525 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 526 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 527 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 528 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 529 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 530 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 531 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 532 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 533 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 534 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 535 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 536 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 537 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 538 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 539 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 540 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 541 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 542 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 543 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 544 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 545 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 546 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 547 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 548 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 549 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 550 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 551 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 552 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 553 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 554 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 555 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 556 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 557 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 558 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 559 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 560 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 561 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 562 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 563 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 564 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 565 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 566 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 567 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 568 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 569 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 570 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 571 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 572 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 573 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 574 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 575 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 576 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 577 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 578 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 579 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 580 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 581 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 582 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 583 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 584 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 585 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 586 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 587 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 588 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 589 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 590 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 591 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 592 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 593 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 594 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 595 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
