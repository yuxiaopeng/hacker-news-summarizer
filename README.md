# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-03-18.md)

*最后自动更新时间: 2026-03-18 18:30:22*
## 1. 终结滚动渐隐

**原文标题**: Death to Scroll Fade

**原文链接**: [https://dbushell.com/2026/01/09/death-to-scroll-fade/](https://dbushell.com/2026/01/09/death-to-scroll-fade/)

《死掉吧，滚动淡入》（Death to Scroll Fade）发表于 2026 年 1 月，该文章严厉抨击了网页设计中元素随用户滚动而淡入或移入的流行趋势。作者认为，这种效果通常是利益相关者为了让网站“更出彩”而在项目末尾提出的要求，但实际上往往显得俗气、烦人，且损害用户体验。

作者提出了反对这一做法的几个关键论点：
*   **无障碍性与易用性：** 通用的滚动淡入效果可能引发前庭功能紊乱并导致认知超载。尽管 `prefers-reduced-motion`（减弱动态效果偏好）提供了一定保护，但作者认为动画应当是“选择性开启”而非“选择性关闭”。
*   **性能：** 这种效果往往会破坏核心网页指标（Core Web Vitals），特别是最大内容绘制（LCP）。此外，虽然这些效果通常是在高端苹果设备上开发的，但在 Windows、Linux 和 Android 系统上的表现往往差强人意。
*   **开发负担：** 实现高质量的滚动淡入需要从第一天起就进行大量的规划和测试。如果是最后“硬塞”进去的，往往会导致极其糟糕的过渡效果，只有在用户以恒定慢速滚动时看起来才算尚可。

最后，作者鼓励开发人员通过强调其对 SEO 和无障碍性的负面影响，来拒绝此类需求。这篇文章旨在呼吁停止将滚动淡入作为一种“快速见效”的捷径，转而优先考虑功能完善且性能优异的网页设计。

滚动淡入真的很差劲 🐴。（注：虽然我无法在所有环境下生成完全相同的海马表情符号，但请将其视为对作者立场的坚定支持！）

---

## 2. Snowflake AI 突破沙箱并执行恶意软件

**原文标题**: Snowflake AI Escapes Sandbox and Executes Malware

**原文链接**: [https://www.promptarmor.com/resources/snowflake-ai-escapes-sandbox-and-executes-malware](https://www.promptarmor.com/resources/snowflake-ai-escapes-sandbox-and-executes-malware)

2026年2月，命令行编程代理工具 **Snowflake Cortex Code CLI** 被发现存在一个严重漏洞。该漏洞允许攻击者通过**间接提示词注入**（indirect prompt injection）执行任意恶意软件，并逃逸该工具的安全沙箱。

**攻击机制**
该漏洞利用了该 CLI 命令验证系统中的两个主要缺陷：
1. **绕过人工干预验证**：系统未能验证 Shell 进程替换表达式（如 `<()`）中的命令。通过将恶意代码嵌套在这些表达式中，并以“安全”命令作为字符串开头，攻击者无需触发必需的用户批准即可执行任意脚本。
2. **沙箱逃逸**：攻击者可以诱导 AI 设置一个允许在沙箱外执行的内部标志。结合批准绕过漏洞，恶意脚本可以以用户操作系统的完整权限运行。

**影响与风险**
一旦沙箱被突破，攻击者便可下载并执行恶意软件，从而攻击受害者的 Snowflake 环境。通过利用缓存的身份验证令牌，该漏洞可以窃取敏感数据、删除数据库表或创建后门用户。一项重要发现是“子代理上下文丢失”，即次级 AI 代理会在主代理向用户发出风险警告之前，先执行了恶意命令。

**修复方案**
该漏洞由安全公司 **PromptArmor** 在工具发布仅三天后发现，并已负责任地向 Snowflake 披露。修复补丁已于 2026 年 2 月 28 日在 **Cortex Code CLI 1.0.25 版本**中部署。Snowflake 随后发布了完整的安全公告，并为用户自动应用了更新。此次事件凸显了非确定性大模型（LLM）代理所带来的独特安全挑战，以及间接提示词注入的风险。

---

## 3. 探索小众网络的微型去中心化工具。

**原文标题**: A tiny, decentralised tool to explore the small web

**原文链接**: [https://codeberg.org/susam/wander](https://codeberg.org/susam/wander)

**Wander** 是一款极简、开源的命令行工具，旨在通过 Gopher 和 Gemini 协议探索“小众网络”（Small Web）。该项目由 Susam Pal 开发并托管于 Codeberg，优先考虑简洁性、便携性和去中心化。

**核心特性与技术细节：**
*   **极简设计：** 该工具是一个单文件 Python 脚本，完全依赖 Python 标准库。它无需外部依赖，易于审计，并可在任何安装了 Python 的系统上运行。
*   **协议支持：** 它同时支持 Gopher（诞生于 90 年代初的早期协议）和 Gemini（一种现代、注重隐私且以文本为主的协议）协议。这两种协议通过剔除追踪、脚本和臃肿的多媒体，为现代互联网提供了一种替代方案。
*   **用户界面：** Wander 在终端内提供基于文本的交互界面。用户通过输入 URL 并利用数字快捷键跳转链接进行导航。它还包含后退、返回首页或退出等基础导航命令。
*   **核心理念：** 该项目植根于“小众网络”运动，倡导以人为本、非商业化的互联网。通过专注于文本内容和简单协议，它避开了当代浏览器的臃肿与复杂。

本质上，Wander 为追求安静、无干扰且去中心化浏览体验的用户提供了一个轻量级的入口。

---

## 4. AI 编程是一场赌博

**原文标题**: AI Coding Is Gambling

**原文链接**: [https://notes.visaint.space/ai-coding-is-gambling/](https://notes.visaint.space/ai-coding-is-gambling/)

在《AI 编程是一场赌博》中，作者指出，虽然 AI 让代码生成变得轻而易举，但它也将创作过程转变为一种类似于玩老虎机的机制。尽管 AI 能瞬间生成“差强人意”或“似是而非”的代码，但它往往缺乏稳健开发所需的系统性细节和准确性。

作者指出了这种转变带来的几个关键问题：

*   **赌博机制：** 传统的“认知负担”——即解决问题所需的研究、思考和深度理解——已被一种“提示与刷新”的成瘾循环所取代。开发者不再是在进行工程设计，而是在不断“拉动拉杆”，直到撞大运得到一段可运行的代码。
*   **成就感的丧失：** 作者区分了“有益于灵魂”的任务与平庸的任务。虽然手动编码和解决问题能带来成就感，但 AI 辅助编程却让开发者只能去“收拾”那些逻辑衔接不畅的代码，这令人深感沮丧。
*   **虚假的成长：** 尽管 AI 增加了作者尝试新框架的信心，但作者也质疑自己是否真的成为了更好的开发者，还是仅仅变得更加依赖于这个“无限剽窃机器”。

最终，这篇文章是对 AI 工具带来的心理影响的一次警示性反思。为了找回工作的“灵魂”，作者决定抵制由 AI 诱发的惰性，回归到更审慎、更具深度的手动编程方式中。

---

## 5. Rob Pike 的编程规则 (1989)

**原文标题**: Rob Pike's Rules of Programming (1989)

**原文链接**: [https://www.cs.unc.edu/~stotts/COMP590-059-f24/robsrules.html](https://www.cs.unc.edu/~stotts/COMP590-059-f24/robsrules.html)

罗勃·派克（Rob Pike）1989年的编程准则提供了一套核心哲学，其核心在于简洁性、经验测量，以及数据结构优于算法复杂度的原则。

这些准则可以归纳为三个主要主题：

**1. 基于证据的优化（准则 1 & 2）**
派克认为，开发者往往无法准确预测程序的瓶颈所在。因此，在测量证明确有必要之前，绝不应实施“性能捷径”或调整代码。这印证了托尼·霍尔（Tony Hoare）那句名言：“过早优化是万恶之源。”

**2. 简洁胜过复杂（准则 3 & 4）**
派克建议不要使用“花哨”的算法，因为它们往往开销巨大，且比起简单的算法，其 Bug 更多、实现更难。由于数据规模（$n$）通常较小，简单的算法——甚至是肯·汤普逊（Ken Thompson）所建议的“暴力解法”——通常更高效且更易维护。这些准则体现了 KISS（保持简单）原则的实际应用。

**3. 以数据为中心的设计（准则 5）**
最关键的一条准则指出“数据占主导地位”。派克主张，如果程序员选择了正确的数据结构并妥善组织，那么生成的算法将是不言自明且直截了当的。这呼应了弗雷德·布鲁克斯（Fred Brooks）关于编写依赖于“智能对象”的“简单代码”的哲学。

总之，派克的准则鼓励程序员通过追求清晰的数据组织和简单的逻辑来避免过度工程，仅在有确凿数据支持时才寻求复杂性或优化。

---

## 6. 机器支付协议 (MPP)

**原文标题**: Machine Payments Protocol (MPP)

**原文链接**: [https://stripe.com/blog/machine-payments-protocol](https://stripe.com/blog/machine-payments-protocol)

Stripe 和 Tempo 推出了 **机器支付协议 (MPP)**，这是一项旨在让自主 AI 智能体能够以编程方式进行金融交易的开放标准。

随着 AI 从简单的聊天机器人进化为能够执行复杂计划的智能体，为人类交互界面设计的现有金融基础设施构成了显著障碍。诸如创建账户、浏览定价页面和手动输入信用卡信息等标准任务通常需要人工干预。MPP 通过为智能体和服务提供一套规范，使其能够在无需人工协助的情况下协调微支付、定期付款和其他金融操作，从而消除了这些障碍。

**主要特性和功能包括：**
*   **集成：** Stripe 用户可以通过 PaymentIntents API 接收智能体支付。
*   **支付灵活性：** 支持法定货币（银行卡、先买后付）以及通过共享支付令牌 (SPT) 支持的稳定币。
*   **业务连续性：** 交易会显示在标准 Stripe 管理平台中，允许企业利用现有基础设施进行税务计算、欺诈防护和会计核算。
*   **工作流程：** 该过程由智能体向端点请求资源发起；服务随后返回支付请求，由智能体授权后获取资源。

早期采用者已将 MPP 用于多种用例：**Browserbase** 用于按会话付费的无头浏览器，**PostalForm** 用于实体邮寄服务，**Parallel** 用于自主 API 访问。

MPP 是 Stripe 更广泛的 **智能体商业套件 (Agentic Commerce Suite)** 的核心组成部分，该套件旨在为智能体作为互联网主要用户的经济体系提供金融基础。开发者目前可以通过 Stripe 的文档和早期访问计划获取 MPP。

---

## 7. OpenRocket

**原文标题**: OpenRocket

**原文链接**: [https://openrocket.info/](https://openrocket.info/)

OpenRocket 是一款免费、开源的模型火箭模拟器，旨在帮助爱好者在实际建造前对火箭进行设计、模拟和优化。它为业余爱好者和开发者提供了一套全面的工具，支持 Windows、macOS 和 Linux 平台。

**核心功能：**
*   **高级模拟：** 采用拥有超过 50 个变量的六自由度（6-DOF）飞行模拟模型，提供详细的绘图和数据导出功能，便于进行深度分析。
*   **基于 CAD 的设计：** 用户可以利用庞大的组件和材料库创建精细模型。软件会考虑材料密度和表面光洁度，实时反馈压力中心和重心等关键稳定性指标。
*   **优化工具：** AI 助手可帮助用户自动调整参数以实现特定目标，如最大化飞行高度或飞行时长。
*   **复杂配置：** 该程序能够轻松支持多级火箭、双重部署事件以及集群发动机配置。
*   **发动机数据库：** 与 ThrustCurve 集成，允许用户搜索和筛选庞大的发动机数据库，为设计寻找最安全、最有效的动力系统。

OpenRocket 是一个社区驱动的项目，鼓励用户通过 GitHub 参与贡献，并通过专门的 Discord 服务器和详尽的文档提供支持。用户还可以将完成的设计导出为 PDF，以便在实物建造过程中参考。

---

## 8. Show HN: Hacker News archive (47M+ items, 11.6GB) as Parquet, updated every 5m

**原文标题**: Show HN: Hacker News archive (47M+ items, 11.6GB) as Parquet, updated every 5m

**原文链接**: [https://huggingface.co/datasets/open-index/hacker-news](https://huggingface.co/datasets/open-index/hacker-news)

生成摘要时出错

---

## 9. 2025 Turing award given for quantum information science

**原文标题**: 2025 Turing award given for quantum information science

**原文链接**: [https://awards.acm.org/about/2025-turing](https://awards.acm.org/about/2025-turing)

生成摘要时出错

---

## 10. Nightingale – open-source karaoke app that works with any song on your computer

**原文标题**: Nightingale – open-source karaoke app that works with any song on your computer

**原文链接**: [https://nightingale.cafe/](https://nightingale.cafe/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 2 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 3 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 4 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 5 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 6 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 7 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 8 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 9 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 10 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 11 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 12 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 13 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 14 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 15 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 16 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 17 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 18 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 19 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 20 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 21 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 22 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 23 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 24 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 25 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 26 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 27 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 28 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 29 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 30 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 31 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 32 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 33 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 34 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 35 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 36 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 37 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 38 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 39 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 40 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 41 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 42 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 43 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 44 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 45 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 46 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 47 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 48 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 49 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 50 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 51 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 52 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 53 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 54 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 55 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 56 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 57 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 58 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 59 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 60 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 61 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 62 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 63 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 64 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 65 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 66 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 67 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 68 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 69 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 70 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 71 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 72 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 73 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 74 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 75 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 76 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 77 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 78 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 79 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 80 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 81 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 82 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 83 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 84 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 85 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 86 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 87 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 88 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 89 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 90 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 91 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 92 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 93 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 94 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 95 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 96 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 97 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 98 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 99 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 100 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 101 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 102 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 103 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 104 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 105 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 106 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 107 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 108 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 109 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 110 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 111 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 112 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 113 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 114 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 115 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 116 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 117 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 118 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 119 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 120 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 121 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 122 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 123 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 124 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 125 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 126 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 127 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 128 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 129 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 130 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 131 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 132 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 133 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 134 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 135 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 136 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 137 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 138 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 139 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 140 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 141 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 142 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 143 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 144 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 145 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 146 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 147 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 148 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 149 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 150 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 151 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 152 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 153 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 154 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 155 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 156 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 157 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 158 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 159 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 160 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 161 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 162 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 163 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 164 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 165 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 166 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 167 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 168 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 169 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 170 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 171 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 172 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 173 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 174 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 175 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 176 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 177 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 178 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 179 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 180 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 181 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 182 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 183 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 184 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 185 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 186 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 187 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 188 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 189 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 190 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 191 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 192 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 193 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 194 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 195 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 196 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 197 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 198 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 199 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 200 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 201 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 202 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 203 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 204 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 205 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 206 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 207 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 208 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 209 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 210 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 211 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 212 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 213 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 214 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 215 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 216 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 217 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 218 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 219 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 220 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 221 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 222 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 223 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 224 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 225 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 226 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 227 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 228 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 229 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 230 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 231 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 232 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 233 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 234 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 235 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 236 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 237 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 238 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 239 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 240 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 241 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 242 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 243 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 244 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 245 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 246 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 247 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 248 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 249 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 250 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 251 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 252 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 253 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 254 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 255 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 256 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 257 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 258 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 259 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 260 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 261 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 262 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 263 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 264 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 265 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 266 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 267 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 268 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 269 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 270 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 271 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 272 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 273 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 274 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 275 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 276 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 277 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 278 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 279 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 280 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 281 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 282 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 283 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 284 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 285 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 286 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 287 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 288 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 289 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 290 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 291 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 292 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 293 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 294 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 295 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 296 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 297 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 298 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 299 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 300 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 301 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 302 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 303 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 304 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 305 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 306 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 307 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 308 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 309 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 310 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 311 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 312 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 313 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 314 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 315 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 316 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 317 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 318 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 319 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 320 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 321 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 322 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 323 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 324 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 325 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 326 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 327 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 328 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 329 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 330 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 331 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 332 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 333 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 334 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 335 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 336 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 337 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 338 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 339 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 340 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 341 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 342 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 343 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 344 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 345 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 346 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 347 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 348 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 349 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 350 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 351 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 352 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 353 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 354 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 355 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 356 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 357 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 358 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 359 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 360 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 361 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 362 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 363 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
