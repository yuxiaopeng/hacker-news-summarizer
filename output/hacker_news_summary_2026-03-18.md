# Hacker News 热门文章摘要 (2026-03-18)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Federal Cyber Experts Called Microsoft's Cloud "A Pile of Shit", yet Approved It

**原文标题**: Federal Cyber Experts Called Microsoft's Cloud "A Pile of Shit", yet Approved It

**原文链接**: [https://www.propublica.org/article/microsoft-cloud-fedramp-cybersecurity-government](https://www.propublica.org/article/microsoft-cloud-fedramp-cybersecurity-government)

生成摘要时出错

---

## 12. Wander – A tiny, decentralised tool (just 2 files) to explore the small web

**原文标题**: Wander – A tiny, decentralised tool (just 2 files) to explore the small web

**原文链接**: [https://susam.net/wander/](https://susam.net/wander/)

生成摘要时出错

---

## 13. Nvidia NemoClaw

**原文标题**: Nvidia NemoClaw

**原文链接**: [https://github.com/NVIDIA/NemoClaw](https://github.com/NVIDIA/NemoClaw)

生成摘要时出错

---

## 14. Write up of my homebrew CPU build

**原文标题**: Write up of my homebrew CPU build

**原文链接**: [https://willwarren.com/2026/03/12/building-my-own-cpu-part-3-from-simulation-to-hardware/](https://willwarren.com/2026/03/12/building-my-own-cpu-part-3-from-simulation-to-hardware/)

生成摘要时出错

---

## 15. Mistral AI Releases Forge

**原文标题**: Mistral AI Releases Forge

**原文链接**: [https://mistral.ai/news/forge](https://mistral.ai/news/forge)

生成摘要时出错

---

## 16. Google Engineers Launch "Sashiko" for Agentic AI Code Review of the Linux Kernel

**原文标题**: Google Engineers Launch "Sashiko" for Agentic AI Code Review of the Linux Kernel

**原文链接**: [https://www.phoronix.com/news/Sashiko-Linux-AI-Code-Review](https://www.phoronix.com/news/Sashiko-Linux-AI-Code-Review)

生成摘要时出错

---

## 17. North Korean's 100k fake IT workers net $500M a year for Kim

**原文标题**: North Korean's 100k fake IT workers net $500M a year for Kim

**原文链接**: [https://www.theregister.com/2026/03/18/researchers_lift_the_lid_on/](https://www.theregister.com/2026/03/18/researchers_lift_the_lid_on/)

生成摘要时出错

---

## 18. A Decade of Slug

**原文标题**: A Decade of Slug

**原文链接**: [https://terathon.com/blog/decade-slug.html](https://terathon.com/blog/decade-slug.html)

生成摘要时出错

---

## 19. CVE-2026-3888: Important Snap Flaw Enables Local Privilege Escalation to Root

**原文标题**: CVE-2026-3888: Important Snap Flaw Enables Local Privilege Escalation to Root

**原文链接**: [https://blog.qualys.com/vulnerabilities-threat-research/2026/03/17/cve-2026-3888-important-snap-flaw-enables-local-privilege-escalation-to-root](https://blog.qualys.com/vulnerabilities-threat-research/2026/03/17/cve-2026-3888-important-snap-flaw-enables-local-privilege-escalation-to-root)

生成摘要时出错

---

## 20. Restoring the first recording of computer music (2018)

**原文标题**: Restoring the first recording of computer music (2018)

**原文链接**: [https://www.bl.uk/stories/blogs/posts/restoring-the-first-recording-of-computer-music](https://www.bl.uk/stories/blogs/posts/restoring-the-first-recording-of-computer-music)

生成摘要时出错

---

## 21. Using calculus to do number theory

**原文标题**: Using calculus to do number theory

**原文链接**: [https://hidden-phenomena.com/articles/hensels](https://hidden-phenomena.com/articles/hensels)

生成摘要时出错

---

## 22. Celebrating Tony Hoare's mark on computer science

**原文标题**: Celebrating Tony Hoare's mark on computer science

**原文链接**: [https://bertrandmeyer.com/2026/03/16/celebrating-tony-hoares-mark-on-computer-science/](https://bertrandmeyer.com/2026/03/16/celebrating-tony-hoares-mark-on-computer-science/)

生成摘要时出错

---

## 23. Ndea (YC W26) is hiring a symbolic RL search guidance lead

**原文标题**: Ndea (YC W26) is hiring a symbolic RL search guidance lead

**原文链接**: [https://ndea.com/jobs/search-guidance](https://ndea.com/jobs/search-guidance)

生成摘要时出错

---

## 24. A data center opened next door. Then came the high-pitched whine

**原文标题**: A data center opened next door. Then came the high-pitched whine

**原文链接**: [https://www.politico.com/news/2026/03/11/data-centers-ai-electricity-virginia-00815219](https://www.politico.com/news/2026/03/11/data-centers-ai-electricity-virginia-00815219)

生成摘要时出错

---

## 25. A Fuzzer for the Toy Optimizer

**原文标题**: A Fuzzer for the Toy Optimizer

**原文链接**: [https://bernsteinbear.com/blog/toy-fuzzer/](https://bernsteinbear.com/blog/toy-fuzzer/)

生成摘要时出错

---

## 26. The pleasures of poor product design

**原文标题**: The pleasures of poor product design

**原文链接**: [https://www.inconspicuous.info/p/the-pleasures-of-poor-product-design](https://www.inconspicuous.info/p/the-pleasures-of-poor-product-design)

生成摘要时出错

---

## 27. Meta will shut down VR Horizon Worlds access June 15

**原文标题**: Meta will shut down VR Horizon Worlds access June 15

**原文链接**: [https://www.engadget.com/ar-vr/meta-will-shut-down-vr-horizon-worlds-access-in-june-222028919.html](https://www.engadget.com/ar-vr/meta-will-shut-down-vr-horizon-worlds-access-in-june-222028919.html)

生成摘要时出错

---

## 28. Show HN: Sub-millisecond VM sandboxes using CoW memory forking

**原文标题**: Show HN: Sub-millisecond VM sandboxes using CoW memory forking

**原文链接**: [https://github.com/adammiribyan/zeroboot](https://github.com/adammiribyan/zeroboot)

生成摘要时出错

---

## 29. A ngrok-style secure tunnel server written in Rust and Open Source

**原文标题**: A ngrok-style secure tunnel server written in Rust and Open Source

**原文链接**: [https://github.com/joaoh82/rustunnel](https://github.com/joaoh82/rustunnel)

生成摘要时出错

---

## 30. Get Shit Done: A meta-prompting, context engineering and spec-driven dev system

**原文标题**: Get Shit Done: A meta-prompting, context engineering and spec-driven dev system

**原文链接**: [https://github.com/gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done)

生成摘要时出错

---

## 31. Python 3.15 JIT 现已重回正轨。

**原文标题**: Python 3.15's JIT is now back on track

**原文链接**: [https://fidget-spinner.github.io/posts/jit-on-track.html](https://fidget-spinner.github.io/posts/jit-on-track.html)

生成摘要时出错

---

## 32. Have a fucking website

**原文标题**: Have a fucking website

**原文链接**: [https://www.otherstrangeness.com/2026/03/14/have-a-fucking-website/](https://www.otherstrangeness.com/2026/03/14/have-a-fucking-website/)

生成摘要时出错

---

## 33. How the Eon Team Produced a Virtual Embodied Fly

**原文标题**: How the Eon Team Produced a Virtual Embodied Fly

**原文链接**: [https://eon.systems/updates/embodied-brain-emulation](https://eon.systems/updates/embodied-brain-emulation)

生成摘要时出错

---

## 34. Unsloth Studio

**原文标题**: Unsloth Studio

**原文链接**: [https://unsloth.ai/docs/new/studio](https://unsloth.ai/docs/new/studio)

生成摘要时出错

---

## 35. Cheap drones are reshaping the war in the sky (scrolling infographic)

**原文标题**: Cheap drones are reshaping the war in the sky (scrolling infographic)

**原文链接**: [https://www.reuters.com/graphics/IRAN-CRISIS/DRONES/dwpkyamxqpm/](https://www.reuters.com/graphics/IRAN-CRISIS/DRONES/dwpkyamxqpm/)

生成摘要时出错

---

## 36. A tale about fixing eBPF spinlock issues in the Linux kernel

**原文标题**: A tale about fixing eBPF spinlock issues in the Linux kernel

**原文链接**: [https://rovarma.com/articles/a-tale-about-fixing-ebpf-spinlock-issues-in-the-linux-kernel/](https://rovarma.com/articles/a-tale-about-fixing-ebpf-spinlock-issues-in-the-linux-kernel/)

生成摘要时出错

---

## 37. Mamba-3

**原文标题**: Mamba-3

**原文链接**: [https://www.together.ai/blog/mamba-3](https://www.together.ai/blog/mamba-3)

生成摘要时出错

---

## 38. Show HN: Reprompt – Score your AI coding prompts with NLP papers

**原文标题**: Show HN: Reprompt – Score your AI coding prompts with NLP papers

**原文链接**: [https://github.com/reprompt-dev/reprompt](https://github.com/reprompt-dev/reprompt)

生成摘要时出错

---

## 39. Government backtracks on AI and copyright after outcry from major artists

**原文标题**: Government backtracks on AI and copyright after outcry from major artists

**原文链接**: [https://www.bbc.co.uk/news/articles/cvg1gr5v333o](https://www.bbc.co.uk/news/articles/cvg1gr5v333o)

生成摘要时出错

---

## 40. Microsoft's 'unhackable' Xbox One has been hacked by 'Bliss'

**原文标题**: Microsoft's 'unhackable' Xbox One has been hacked by 'Bliss'

**原文链接**: [https://www.tomshardware.com/video-games/console-gaming/microsofts-unhackable-xbox-one-has-been-hacked-by-bliss-the-2013-console-finally-fell-to-voltage-glitching-allowing-the-loading-of-unsigned-code-at-every-level](https://www.tomshardware.com/video-games/console-gaming/microsofts-unhackable-xbox-one-has-been-hacked-by-bliss-the-2013-console-finally-fell-to-voltage-glitching-allowing-the-loading-of-unsigned-code-at-every-level)

生成摘要时出错

---

## 41. Iran's South Pars Gas Field Is Attacked by Israel, Sending Energy Prices Soaring

**原文标题**: Iran's South Pars Gas Field Is Attacked by Israel, Sending Energy Prices Soaring

**原文链接**: [https://www.nytimes.com/2026/03/18/world/middleeast/israel-strikes-south-pars-gas-oil-prices.html](https://www.nytimes.com/2026/03/18/world/middleeast/israel-strikes-south-pars-gas-oil-prices.html)

生成摘要时出错

---

## 42. Tech hobbyist makes shoulder-mounted guided missile prototype with $96 in parts

**原文标题**: Tech hobbyist makes shoulder-mounted guided missile prototype with $96 in parts

**原文链接**: [https://www.tomshardware.com/3d-printing/tech-hobbyist-makes-shoulder-mounted-guided-missile-prototype-with-usd96-in-parts-and-a-3d-printer-diy-manpads-includes-wi-fi-guidance-ballistics-calculations-optional-camera-for-tracking](https://www.tomshardware.com/3d-printing/tech-hobbyist-makes-shoulder-mounted-guided-missile-prototype-with-usd96-in-parts-and-a-3d-printer-diy-manpads-includes-wi-fi-guidance-ballistics-calculations-optional-camera-for-tracking)

生成摘要时出错

---

## 43. Americans Recognize AI as a Wealth Inequality Machine, Polls Find

**原文标题**: Americans Recognize AI as a Wealth Inequality Machine, Polls Find

**原文链接**: [https://gizmodo.com/americans-recognize-ai-as-a-wealth-inequality-machine-pollsters-find-2000734713](https://gizmodo.com/americans-recognize-ai-as-a-wealth-inequality-machine-pollsters-find-2000734713)

生成摘要时出错

---

## 44. Aliens.gov ~ domain registered 17MAR2026

**原文标题**: Aliens.gov ~ domain registered 17MAR2026

**原文链接**: [https://whois.domaintools.com/aliens.gov](https://whois.domaintools.com/aliens.gov)

生成摘要时出错

---

## 45. Why AI systems don't learn – On autonomous learning from cognitive science

**原文标题**: Why AI systems don't learn – On autonomous learning from cognitive science

**原文链接**: [https://arxiv.org/abs/2603.15381](https://arxiv.org/abs/2603.15381)

生成摘要时出错

---

## 46. Never Trust the Science - On the need to identify bias & interpret data yourself

**原文标题**: Never Trust the Science - On the need to identify bias & interpret data yourself

**原文链接**: [https://adam.rochussen.xyz/p/never-trust-the-science](https://adam.rochussen.xyz/p/never-trust-the-science)

生成摘要时出错

---

## 47. Kagi Small Web

**原文标题**: Kagi Small Web

**原文链接**: [https://kagi.com/smallweb/](https://kagi.com/smallweb/)

生成摘要时出错

---

## 48. Edge.js: Run Node apps inside a WebAssembly sandbox

**原文标题**: Edge.js: Run Node apps inside a WebAssembly sandbox

**原文链接**: [https://wasmer.io/posts/edgejs-safe-nodejs-using-wasm-sandbox](https://wasmer.io/posts/edgejs-safe-nodejs-using-wasm-sandbox)

生成摘要时出错

---

## 49. Show HN: Pgit – A Git-like CLI backed by PostgreSQL

**原文标题**: Show HN: Pgit – A Git-like CLI backed by PostgreSQL

**原文链接**: [https://oseifert.ch/blog/building-pgit](https://oseifert.ch/blog/building-pgit)

生成摘要时出错

---

## 50. Node.js needs a virtual file system

**原文标题**: Node.js needs a virtual file system

**原文链接**: [https://blog.platformatic.dev/why-nodejs-needs-a-virtual-file-system](https://blog.platformatic.dev/why-nodejs-needs-a-virtual-file-system)

生成摘要时出错

---

## 51. OpenSUSE Kalpa

**原文标题**: OpenSUSE Kalpa

**原文链接**: [https://kalpadesktop.org/](https://kalpadesktop.org/)

生成摘要时出错

---

## 52. Observation of the doubly charmed heavy proton Ξcc+

**原文标题**: Observation of the doubly charmed heavy proton Ξcc+

**原文链接**: [https://lhcb-outreach.web.cern.ch/2026/03/17/observation-of-the-doubly-charmed-heavy-proton-%CE%BEcc/](https://lhcb-outreach.web.cern.ch/2026/03/17/observation-of-the-doubly-charmed-heavy-proton-%CE%BEcc/)

生成摘要时出错

---

## 53. Meta is shutting down VR social platform Horizon Worlds

**原文标题**: Meta is shutting down VR social platform Horizon Worlds

**原文链接**: [https://www.cnbc.com/2026/03/18/meta-horizon-worlds-metaverse-vr.html](https://www.cnbc.com/2026/03/18/meta-horizon-worlds-metaverse-vr.html)

生成摘要时出错

---

## 54. Honda is killing its EVs

**原文标题**: Honda is killing its EVs

**原文链接**: [https://techcrunch.com/2026/03/14/honda-is-killing-its-evs-and-any-chance-of-competing-in-the-future/](https://techcrunch.com/2026/03/14/honda-is-killing-its-evs-and-any-chance-of-competing-in-the-future/)

生成摘要时出错

---

## 55. 'The Secret Agent': Exploring a Vibrant, yet Violent Brazil (2025)

**原文标题**: 'The Secret Agent': Exploring a Vibrant, yet Violent Brazil (2025)

**原文链接**: [https://theasc.com/articles/the-secret-agent-cinematography](https://theasc.com/articles/the-secret-agent-cinematography)

生成摘要时出错

---

## 56. Review of Microsoft's ClearType Font Collection (2005)

**原文标题**: Review of Microsoft's ClearType Font Collection (2005)

**原文链接**: [https://typographica.org/on-typography/microsofts-cleartype-font-collection-a-fair-and-balanced-review/](https://typographica.org/on-typography/microsofts-cleartype-font-collection-a-fair-and-balanced-review/)

生成摘要时出错

---

## 57. Building a Shell

**原文标题**: Building a Shell

**原文链接**: [https://healeycodes.com/building-a-shell](https://healeycodes.com/building-a-shell)

生成摘要时出错

---

## 58. I Simulated 38,612 Countryle Games to Find the Best Strategy

**原文标题**: I Simulated 38,612 Countryle Games to Find the Best Strategy

**原文链接**: [https://stoffregen.io/posts/countryle/](https://stoffregen.io/posts/countryle/)

生成摘要时出错

---

## 59. Show HN: Crust – A CLI framework for TypeScript and Bun

**原文标题**: Show HN: Crust – A CLI framework for TypeScript and Bun

**原文链接**: [https://github.com/chenxin-yan/crust](https://github.com/chenxin-yan/crust)

生成摘要时出错

---

## 60. FFmpeg 8.1

**原文标题**: FFmpeg 8.1

**原文链接**: [https://ffmpeg.org/index.html#pr8.1](https://ffmpeg.org/index.html#pr8.1)

生成摘要时出错

---

## 61. Robotocore · a Digital Twin of AWS

**原文标题**: Robotocore · a Digital Twin of AWS

**原文链接**: [https://github.com/robotocore/robotocore](https://github.com/robotocore/robotocore)

生成摘要时出错

---

## 62. Kagi Translate now supports LinkedIn Speak as an output language

**原文标题**: Kagi Translate now supports LinkedIn Speak as an output language

**原文链接**: [https://translate.kagi.com/?from=en&to=LinkedIn+speak](https://translate.kagi.com/?from=en&to=LinkedIn+speak)

生成摘要时出错

---

## 63. Launch an autonomous AI agent with sandboxed execution in 2 lines of code

**原文标题**: Launch an autonomous AI agent with sandboxed execution in 2 lines of code

**原文链接**: [https://amaiya.github.io/onprem/examples_agent.html](https://amaiya.github.io/onprem/examples_agent.html)

生成摘要时出错

---

## 64. Leviathan (1651)

**原文标题**: Leviathan (1651)

**原文链接**: [https://www.gutenberg.org/files/3207/3207-h/3207-h.htm](https://www.gutenberg.org/files/3207/3207-h/3207-h.htm)

生成摘要时出错

---

## 65. Java 26 is here

**原文标题**: Java 26 is here

**原文链接**: [https://hanno.codes/2026/03/17/java-26-is-here/](https://hanno.codes/2026/03/17/java-26-is-here/)

生成摘要时出错

---

## 66. Ryugu asteroid samples contain all DNA and RNA building blocks

**原文标题**: Ryugu asteroid samples contain all DNA and RNA building blocks

**原文链接**: [https://phys.org/news/2026-03-ryugu-asteroid-samples-dna-rna.html](https://phys.org/news/2026-03-ryugu-asteroid-samples-dna-rna.html)

生成摘要时出错

---

## 67. Aggregated File System (AGFS), a modern tribute to the spirit of Plan 9

**原文标题**: Aggregated File System (AGFS), a modern tribute to the spirit of Plan 9

**原文链接**: [https://github.com/c4pt0r/agfs](https://github.com/c4pt0r/agfs)

生成摘要时出错

---

## 68. Show HN: Horizon – GPU-accelerated infinite-canvas terminal in Rust

**原文标题**: Show HN: Horizon – GPU-accelerated infinite-canvas terminal in Rust

**原文链接**: [https://github.com/peters/horizon](https://github.com/peters/horizon)

生成摘要时出错

---

## 69. Leanstral: Open-source agent for trustworthy coding and formal proof engineering

**原文标题**: Leanstral: Open-source agent for trustworthy coding and formal proof engineering

**原文链接**: [https://mistral.ai/news/leanstral](https://mistral.ai/news/leanstral)

生成摘要时出错

---

## 70. Beyond has dropped “meat” from its name and expanded its high-protein drink line

**原文标题**: Beyond has dropped “meat” from its name and expanded its high-protein drink line

**原文链接**: [https://plantbasednews.org/news/alternative-protein/beyond-meat-not-the-moment-rebrand/](https://plantbasednews.org/news/alternative-protein/beyond-meat-not-the-moment-rebrand/)

生成摘要时出错

---

## 71. Hundreds of Millions of iPhones Can Be Hacked With a New Tool Found in the Wild

**原文标题**: Hundreds of Millions of iPhones Can Be Hacked With a New Tool Found in the Wild

**原文链接**: [https://www.wired.com/story/hundreds-of-millions-of-iphones-can-be-hacked-with-a-new-tool-found-in-the-wild/](https://www.wired.com/story/hundreds-of-millions-of-iphones-can-be-hacked-with-a-new-tool-found-in-the-wild/)

生成摘要时出错

---

## 72. DarkSword: iOS Exploit Chain Adopted by Multiple Threat Actors

**原文标题**: DarkSword: iOS Exploit Chain Adopted by Multiple Threat Actors

**原文链接**: [https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain](https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain)

生成摘要时出错

---

## 73. Meta Horizon Worlds on Meta Quest is being discontinued

**原文标题**: Meta Horizon Worlds on Meta Quest is being discontinued

**原文链接**: [https://communityforums.atmeta.com/blog/AnnouncementsBlog/updates-to-your-meta-quest-experience-in-2026/1369435](https://communityforums.atmeta.com/blog/AnnouncementsBlog/updates-to-your-meta-quest-experience-in-2026/1369435)

生成摘要时出错

---

## 74. Meta and TikTok let harmful content rise to drove engagement, say whistleblowers

**原文标题**: Meta and TikTok let harmful content rise to drove engagement, say whistleblowers

**原文链接**: [https://www.bbc.com/news/articles/cqj9kgxqjwjo](https://www.bbc.com/news/articles/cqj9kgxqjwjo)

生成摘要时出错

---

## 75. Every layer of review makes you 10x slower

**原文标题**: Every layer of review makes you 10x slower

**原文链接**: [https://apenwarr.ca/log/20260316](https://apenwarr.ca/log/20260316)

生成摘要时出错

---

## 76. Illinois Introducing Operating System Account Age Bill

**原文标题**: Illinois Introducing Operating System Account Age Bill

**原文链接**: [https://www.ilga.gov/Legislation/BillStatus?DocTypeID=HB&DocNum=5511](https://www.ilga.gov/Legislation/BillStatus?DocTypeID=HB&DocNum=5511)

生成摘要时出错

---

## 77. Show HN: Claude Code skills that build complete Godot games

**原文标题**: Show HN: Claude Code skills that build complete Godot games

**原文链接**: [https://github.com/htdt/godogen](https://github.com/htdt/godogen)

生成摘要时出错

---

## 78. UC Irvine researchers bring down AI powered drones with painted umbrellas

**原文标题**: UC Irvine researchers bring down AI powered drones with painted umbrellas

**原文链接**: [https://arxiv.org/abs/2509.20362](https://arxiv.org/abs/2509.20362)

生成摘要时出错

---

## 79. The Proliferation of DarkSword: iOS Exploit Chain Adopted by Hackers

**原文标题**: The Proliferation of DarkSword: iOS Exploit Chain Adopted by Hackers

**原文链接**: [https://login.corp.google.com/request?s=cloud-blog-transform.corp.google.com:443/uberproxy/&d=https://cloud-blog-transform.corp.google.com/blog/preview/58463%3Fhl%3Den%26upxsrf%3DAM2vRLkFeUi0ZDl5yOEqxceriJM_3Rb7hCVJHfwSDHN-DUIlTA:1773846867432&maxAge=1200&authLevel=2000000&keyIds=588916238,1331854303,-337386367,788849210,-1430978537,1163017845,-100563820,2023603197&c=1](https://login.corp.google.com/request?s=cloud-blog-transform.corp.google.com:443/uberproxy/&d=https://cloud-blog-transform.corp.google.com/blog/preview/58463%3Fhl%3Den%26upxsrf%3DAM2vRLkFeUi0ZDl5yOEqxceriJM_3Rb7hCVJHfwSDHN-DUIlTA:1773846867432&maxAge=1200&authLevel=2000000&keyIds=588916238,1331854303,-337386367,788849210,-1430978537,1163017845,-100563820,2023603197&c=1)

生成摘要时出错

---

## 80. Switzerland Built an Alternative to BGP

**原文标题**: Switzerland Built an Alternative to BGP

**原文链接**: [https://www.theregister.com/2026/03/17/switzerland_bgp_alternative/](https://www.theregister.com/2026/03/17/switzerland_bgp_alternative/)

生成摘要时出错

---

## 81. SSH has no Host header

**原文标题**: SSH has no Host header

**原文链接**: [https://blog.exe.dev/ssh-host-header](https://blog.exe.dev/ssh-host-header)

生成摘要时出错

---

## 82. Give Django your time and money, not your tokens

**原文标题**: Give Django your time and money, not your tokens

**原文链接**: [https://www.better-simple.com/django/2026/03/16/give-django-your-time-and-money/](https://www.better-simple.com/django/2026/03/16/give-django-your-time-and-money/)

生成摘要时出错

---

## 83. Reverse-engineering Viktor and making it open source

**原文标题**: Reverse-engineering Viktor and making it open source

**原文链接**: [https://matijacniacki.com/blog/openviktor](https://matijacniacki.com/blog/openviktor)

生成摘要时出错

---

## 84. Duranium: A More Reliable PostmarketOS

**原文标题**: Duranium: A More Reliable PostmarketOS

**原文链接**: [https://postmarketos.org/blog/2026/03/17/introducing-duranium/](https://postmarketos.org/blog/2026/03/17/introducing-duranium/)

生成摘要时出错

---

## 85. GPT‑5.4 Mini and Nano

**原文标题**: GPT‑5.4 Mini and Nano

**原文链接**: [https://openai.com/index/introducing-gpt-5-4-mini-and-nano](https://openai.com/index/introducing-gpt-5-4-mini-and-nano)

生成摘要时出错

---

## 86. Bill C-22, the Lawful Access Act: Dangerous backdoor surveillance risks remain

**原文标题**: Bill C-22, the Lawful Access Act: Dangerous backdoor surveillance risks remain

**原文链接**: [https://www.michaelgeist.ca/2026/03/a-tale-of-two-bills-lawful-access-returns-with-changes-to-warrantless-access-but-dangerous-backdoor-surveillance-risks-remains/](https://www.michaelgeist.ca/2026/03/a-tale-of-two-bills-lawful-access-returns-with-changes-to-warrantless-access-but-dangerous-backdoor-surveillance-risks-remains/)

生成摘要时出错

---

## 87. Judge orders restoration of Voice of America

**原文标题**: Judge orders restoration of Voice of America

**原文链接**: [https://apnews.com/article/voice-of-america-kari-lake-trump-cd6d1ef05272f842705da0ed38d3de24](https://apnews.com/article/voice-of-america-kari-lake-trump-cd6d1ef05272f842705da0ed38d3de24)

生成摘要时出错

---

## 88. Meta’s renewed commitment to jemalloc

**原文标题**: Meta’s renewed commitment to jemalloc

**原文链接**: [https://engineering.fb.com/2026/03/02/data-infrastructure/investing-in-infrastructure-metas-renewed-commitment-to-jemalloc/](https://engineering.fb.com/2026/03/02/data-infrastructure/investing-in-infrastructure-metas-renewed-commitment-to-jemalloc/)

生成摘要时出错

---

## 89. The “small web” is bigger than you might think

**原文标题**: The “small web” is bigger than you might think

**原文链接**: [https://kevinboone.me/small_web_is_big.html](https://kevinboone.me/small_web_is_big.html)

生成摘要时出错

---

## 90. Lazycut: A simple terminal video trimmer using FFmpeg

**原文标题**: Lazycut: A simple terminal video trimmer using FFmpeg

**原文链接**: [https://github.com/emin-ozata/lazycut](https://github.com/emin-ozata/lazycut)

生成摘要时出错

---

## 91. The American Healthcare Conundrum

**原文标题**: The American Healthcare Conundrum

**原文链接**: [https://github.com/rexrodeo/american-healthcare-conundrum](https://github.com/rexrodeo/american-healthcare-conundrum)

生成摘要时出错

---

## 92. Corruption erodes social trust more in democracies than in autocracies

**原文标题**: Corruption erodes social trust more in democracies than in autocracies

**原文链接**: [https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2026.1779810/full](https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2026.1779810/full)

生成摘要时出错

---

## 93. Speed at the cost of quality: Study of use of Cursor AI in open source projects (2025)

**原文标题**: Speed at the cost of quality: Study of use of Cursor AI in open source projects (2025)

**原文链接**: [https://arxiv.org/abs/2511.04427](https://arxiv.org/abs/2511.04427)

生成摘要时出错

---

## 94. The bureaucracy blocking the chance at a cure

**原文标题**: The bureaucracy blocking the chance at a cure

**原文链接**: [https://www.writingruxandrabio.com/p/the-bureaucracy-blocking-the-chance](https://www.writingruxandrabio.com/p/the-bureaucracy-blocking-the-chance)

生成摘要时出错

---

## 95. Animation 10k Starlink Satellites

**原文标题**: Animation 10k Starlink Satellites

**原文链接**: [https://spaceweather.com/archive.php?view=1&day=18&month=03&year=2026](https://spaceweather.com/archive.php?view=1&day=18&month=03&year=2026)

生成摘要时出错

---

## 96. Measuring progress toward AGI: A cognitive framework

**原文标题**: Measuring progress toward AGI: A cognitive framework

**原文链接**: [https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/measuring-agi-cognitive-framework/)

生成摘要时出错

---

## 97. Toward automated verification of unreviewed AI-generated code

**原文标题**: Toward automated verification of unreviewed AI-generated code

**原文链接**: [https://peterlavigne.com/writing/verifying-ai-generated-code](https://peterlavigne.com/writing/verifying-ai-generated-code)

生成摘要时出错

---

## 98. Why I love FreeBSD

**原文标题**: Why I love FreeBSD

**原文链接**: [https://it-notes.dragas.net/2026/03/16/why-i-love-freebsd/](https://it-notes.dragas.net/2026/03/16/why-i-love-freebsd/)

生成摘要时出错

---

## 99. Language model teams as distributed systems

**原文标题**: Language model teams as distributed systems

**原文链接**: [https://arxiv.org/abs/2603.12229](https://arxiv.org/abs/2603.12229)

生成摘要时出错

---

## 100. MoD sources warn Palantir role at heart of government is threat to UK security

**原文标题**: MoD sources warn Palantir role at heart of government is threat to UK security

**原文链接**: [https://www.thenerve.news/p/palantir-technologies-uk-mod-sources-government-data-insights-security-state-secrets](https://www.thenerve.news/p/palantir-technologies-uk-mod-sources-government-data-insights-security-state-secrets)

生成摘要时出错

---

