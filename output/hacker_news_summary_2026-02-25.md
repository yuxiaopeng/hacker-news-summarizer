# Hacker News 热门文章摘要 (2026-02-25)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 公交站点优化快速、廉价且有效。

**原文标题**: Bus stop balancing is fast, cheap, and effective

**原文链接**: [https://worksinprogress.co/issue/the-united-states-needs-fewer-bus-stops/](https://worksinprogress.co/issue/the-united-states-needs-fewer-bus-stops/)

**摘要：公交站点优化**

公交站点优化（Bus stop balancing）——即通过战略性地移除冗余站点来增加站间距——是改善城市交通的一种快速、低成本且高效的方式。虽然大型轨道交通项目往往备受关注，但公交车承载了更多的乘客，且在疫情后恢复得更快。然而，在美英两国的许多城市，公交站点间距仅为700英尺左右，导致车辆行驶缓慢，使其在与私家车的竞争中缺乏优势。

通过采用欧洲间距更宽（约1,300英尺）的模式，交通管理部门可以获得以下关键收益：

*   **提高速度与效率：** 减少站点既缩短了“停站时间”（乘客上下车），也减少了“非停站时间”（减速、加速及应对交通流量）。在旧金山和温哥华等城市的实施结果显示，车速提升了高达14%，为乘客节省了大量时间。
*   **节省成本：** 人工成本是交通部门最大的开支。更快的公交车能更迅速地完成运行路线，从而只需更少的车辆和司机即可维持相同的发车频率。节省下的资金可重新投入到其他线路的服务中。
*   **提高可靠性：** 站点减少意味着行程延误和变数的机会减少，解决了通勤者最主要的困扰之一。
*   **改善配套设施：** 通过维护更少的站点，管理部门有能力对剩余站点进行升级，配备更好的候车亭、座椅、照明和实时信息系统，将“孤零零的站牌”转化为高质量的交通枢纽。

尽管批评者认为站点整合会降低覆盖范围，但研究表明，由于“步行覆盖区”存在重叠，对实际可达性的影响微乎其微。最终，站点优化将重点从单纯的地理覆盖转向了实质性的便捷通达，让乘客能在更短时间内到达更多目的地。它是交通改革中一个罕见的范例：无需新建基础设施，却能产生立竿见影且可衡量的效果。

---

## 2. 千万别买 .online 域名

**原文标题**: Never buy a .online domain

**原文链接**: [https://www.0xsid.com/blog/online-tld-is-pain](https://www.0xsid.com/blog/online-tld-is-pain)

作者是一位长期的“.com 纯粹主义者”，他分享了一个关于通过 Namecheap 促销购买 **.online** 域名的警示案例。在为一个浏览器应用发布了一个简单的落地页后不久，该网站被 Google 标记为“不安全”，并被注册局 Radix 设为 **serverHold**（注册局暂停解析）状态。

这引发了一个技术上的“第 22 条军规”（死循环）：
1.  **注册局 (Radix)** 拒绝解除 serverHold 状态，直到 Google 将该网站从黑名单中移除。
2.  **Google** 要求作者通过 Search Console 中的 DNS 记录验证所有权，方可申请复审。
3.  **冲突点：** 由于域名处于 serverHold 状态，域名无法解析，导致 DNS 验证根本无法完成。

在没有收到注册商或注册局任何通知，且无法通过自动化渠道解决的情况下，作者的网站始终处于离线且无法访问的状态。直到该故事在 Hacker News 上引起热议，一名匿名的 Google 员工手动清除了黑名单标记，Radix 才最终解除了域名锁定，问题才得以解决。

**核心启示：**
*   **坚持使用 .com：** 标准顶级域名（TLD）面临注册局层面激进自动化封禁的概率较低。
*   **立即验证：** 务必在购买新域名后立即将其添加到 Google Search Console，以便在潜在封禁发生前确立所有权。
*   **可观测性：** 即使是小项目，也要使用运行时间监控，以捕获隐蔽的 DNS 故障。
*   **“小众”顶级域名的风险：** 小众注册局的滥用处理政策可能极其敏感且沟通不畅，一旦被标记，所有者往往投诉无门。

---

## 3. 基于大语言模型的大规模在线去匿名化

**原文标题**: Large-Scale Online Deanonymization with LLMs

**原文链接**: [https://simonlermen.substack.com/p/large-scale-online-deanonymization](https://simonlermen.substack.com/p/large-scale-online-deanonymization)

文章《使用大语言模型进行大规模在线去匿名化》重点介绍了苏黎世联邦理工学院（ETH Zurich）关于数字隐私侵蚀的突破性研究。该研究表明，GPT-4 等大语言模型（LLM）能够从看似匿名的社交媒体评论中准确推断出高度敏感的个人信息。

通过分析包含 500 多个 Reddit 个人资料的数据集，研究人员发现 LLM 能够以惊人的精度预测用户属性，包括所在地、年龄、性别、职业甚至收入。在研究中，GPT-4 的 Top-1 预测准确率高达 85%，Top-3 准确率则达到 95.8%。这些模型通过“串联”散布在多条帖子中的细微线索（如提到的当地地标、特定的通勤路线或人生里程碑）来实现这一目标。

核心发现及其影响包括：

*   **大规模画像：** 人类专家虽然也能进行类似的画像分析，但时间和劳动力成本高昂；与之不同，LLM 能够实现低成本、大规模的自动化去匿名化。
*   **传统匿名化的失效：** 移除姓名或直接标识符等传统做法已不足以保护隐私。LLM 利用复杂的推理能力绕过这些保护措施，使得在公开互联网上实现真正的匿名几乎成为不可能。
*   **新的隐私风险：** 这种能力降低了大范围监控、定向骚扰以及揭露匿名举报者或政治异议人士身份的门槛。

归根结底，这篇文章发出了警示：LLM 已从根本上改变了隐私格局。随着这些模型变得愈发普及和强大，将零散的数字足迹整合为完整个人画像的能力，已成为任何拥有 API 访问权限的人都能使用的工具，这对全球互联网用户构成了重大威胁。

---

## 4. 大学的误用

**原文标题**: The Misuses of the University

**原文链接**: [https://www.publicbooks.org/the-misuses-of-the-university/](https://www.publicbooks.org/the-misuses-of-the-university/)

在《大学之误》（The Misuses of the University）一文中，肖恩·菲利普斯（Siobhán Phillips）通过重新审视克拉克·克尔（Clark Kerr）1963年提出的“巨型大学”（multiversity）概念，探讨了美国高等教育的演变及其当前的危机。克尔认为大学不应是孤立的“象牙塔”，而应是与国家和经济需求紧密结合的核心“知识产业”。菲利普斯指出，尽管克尔的愿景具有预见性，但它也为现代学术机构堕落为企业化榨取和社会剥削的工具铺平了道路。

该摘要强调了对当代大学的几项关键批判：

*   **私有化陷阱**：继20世纪后期的“大错误”之后，大学的角色从公共产品转变为私人投资。这导致了政府拨款的减少、学费的飙升，以及对学生债务和不稳定的临时教职劳动力的依赖。
*   **掠夺性城市化**：借鉴达瓦里安·鲍德温（Davarian Baldwin）的研究，菲利普斯描述了“大学城”（UniverCities）的兴起。许多富裕的机构非但没有提升周边环境，反而扮演着掠夺性房地产开发商的角色，利用其免税地位推动社区绅士化、驱逐低收入居民，并扩大校园警务管控。
*   **机构虚伪**：虽然大学经常在营销中宣传“多样性与包容性”，但其财务结构往往在强化不平等。所谓的“误用”在于，这些机构将资本积累和机构声望置于其教育和公民使命之上。

最终，菲利普斯认为现代大学已成为一座为自身行政增长而非公众利益服务的“知识工厂”。文章呼吁对高等教育进行根本性的重新构想——超越克尔的工业模式，优先考虑真正的社会公平，并恢复大学作为公共资源的属性。

---

## 5. 增长35%后，美国电网太阳能发电量已超过水电。

**原文标题**: Following 35% growth, solar has passed hydro on US grid

**原文链接**: [https://arstechnica.com/science/2026/02/final-2025-data-is-in-us-energy-use-is-up-as-solar-passes-hydro/](https://arstechnica.com/science/2026/02/final-2025-data-is-in-us-energy-use-is-up-as-solar-passes-hydro/)

2025年，由于发电量同比增长35%，太阳能首次超过水电，实现了重大里程碑。尽管可再生能源经历了创纪录的扩张，但受数据中心、电动汽车和热泵的驱动，美国电力总需求增长了2.8%，其增速超过了可再生能源的增量。

报告强调了能源形势的复杂性：虽然太阳能和风能满足了近四分之三的新增需求，但其余部分则由煤炭使用量13%的增长来填补。煤炭消费的复苏受多种因素影响，包括天然气出口增加及硬件关税导致的天然气价格上涨，以及特朗普政府旨在推迟煤电厂关闭的政策。

展望2026年，受有利的经济因素驱动，可再生能源的前景依然强劲。计划中的项目包括创纪录的43吉瓦（GW）太阳能装机和12吉瓦风电，其中包括重大的海上开发项目以及新墨西哥州一座3.6吉瓦的大型风电场。此外，为了应对可再生能源的波动性，预计电网将新增24吉瓦的电池储能，主要分布在德克萨斯州和加利福尼亚州。

最终，美国正接近一个关键转折点，届时风能和太阳能的增长可能很快便能完全抵消不断增长的需求。然而，当前依靠煤炭填补即时缺口的现状表明，市场动态和政策转变仍在使减少电网整体碳排放的努力变得复杂化。

---

## 6. GNU TeXmacs

**原文标题**: GNU Texmacs

**原文链接**: [https://www.texmacs.org/tmweb/home/welcome.en.html](https://www.texmacs.org/tmweb/home/welcome.en.html)

GNU TeXmacs 是由自由软件基金会 (FSF) GNU 项目开发的免费开源科学编辑平台。它旨在通过用户友好的“所见即所得”(WYSIWYG) 界面创建高质量的技术文档。

**核心特性与功能：**
*   **结构化内容：** 该编辑器支持广泛的内容，包括复杂的数学排版、集成图形、演示文稿以及交互式内容。
*   **计算接口：** 它可以作为各种外部系统的图形前端，例如计算机代数、数值分析和统计软件。
*   **独特的引擎：** 尽管名称如此，TeXmacs 并不基于 TeX/LaTeX。它使用自有的高质量排版引擎，为打印或数字演示生成专业级文档。
*   **兼容性与转换：** 该软件可在 Unix、MacOS 和 Windows 上运行。它支持多种语言，并提供针对 TeX/LaTeX 和 HTML/MathML 的转换器。文档原生以 TeXmacs、XML 或 Scheme 格式保存，并可导出为 PDF 或 Postscript 文件。
*   **可扩展性：** 用户可以通过创建新的文档样式或使用 Scheme 扩展语言添加功能来自定义平台。

总之，GNU TeXmacs 为科学专业人士提供了一个统一的框架，使他们能够在单一且可扩展的环境中编写、计算和展示自己的工作。

---

## 7. 如何折叠《银翼杀手》折纸独角兽 (1996)

**原文标题**: How to fold the Blade Runner origami unicorn (1996)

**原文链接**: [https://web.archive.org/web/20011104015933/www.linkclub.or.jp/~null/index_br.html](https://web.archive.org/web/20011104015933/www.linkclub.or.jp/~null/index_br.html)

The provided text is a metadata snapshot from the **Wayback Machine (Internet Archive)** regarding a webpage titled **"How to fold the Blade Runner origami unicorn."**

Rather than containing the folding instructions themselves, the text provides archival details about the site’s history. Key points include:

*   **Subject Matter:** The page is dedicated to teaching readers how to recreate the iconic origami unicorn from the 1982 film *Blade Runner*. This specific guide, hosted by a user named "null," is historically significant within the fan community as one of the earliest online resources (dating back to 1996) to decode the prop's complex design.
*   **Archival History:** The specific capture shown is from **November 4, 2001**. The Wayback Machine has recorded 47 captures of this URL between 2001 and 2026.
*   **Source Data:** The page was preserved as part of the **Alexa Crawls** collection, a project where Alexa Internet donated web crawl data to the Internet Archive starting in 1996.
*   **Technical Details:** The original site was hosted on a Japanese service provider (`linkclub.or.jp`). 

In summary, the document serves as a digital footprint of a classic piece of "cyber-culture" history, marking the preservation of a fan-made tutorial for a famous cinematic prop.

---

## 8. Trellis AI (YC W24) is hiring deployment lead to accelerate medication access

**原文标题**: Trellis AI (YC W24) is hiring deployment lead to accelerate medication access

**原文链接**: [https://www.ycombinator.com/companies/trellis-ai/jobs/7ZlvQkN-lead-deployment-strategist](https://www.ycombinator.com/companies/trellis-ai/jobs/7ZlvQkN-lead-deployment-strategist)

Trellis AI, a Y Combinator (W24) healthcare startup and Stanford AI Lab spinout, is seeking a **Lead Deployment Strategist** to scale its AI-driven administrative platform. Based in San Francisco (with remote options), the company automates complex healthcare paperwork—including document intake, prior authorizations, and appeals—to accelerate patient access to life-saving medications.

**The Role**
The Lead Deployment Strategist will bridge the gap between internal engineering teams and enterprise healthcare clients. Key responsibilities include managing mission-critical implementations, translating technical capabilities into real-world business value, and navigating the complex IT environments of Fortune 500 customers.

**Candidate Requirements**
*   **Experience:** 3+ years in client-facing technical roles (Forward Deployment, Solutions, or Consulting).
*   **Technical Background:** A technical degree or at least one summer of engineering experience is required.
*   **Skills:** Strong project management, executive-level communication, and the ability to operate autonomously in a fast-paced startup environment. Backgrounds in top-tier consulting or private equity are preferred.

**Company Impact & Growth**
Trellis agents currently process billions of dollars in therapies across all 50 states, reducing time-to-treatment by over 90%. The company has reported 10x revenue growth in recent months and is backed by major investors, including General Catalyst and executives from Google and Salesforce. 

The position offers a salary range of **$80K – $180K** and the opportunity to join a world-class team of AI researchers and healthcare operations experts aiming to eliminate the 20% of U.S. healthcare spending lost to administrative inefficiency.

---

## 9. Racket v9.1

**原文标题**: Racket v9.1

**原文链接**: [https://blog.racket-lang.org/2026/02/racket-v9-1.html](https://blog.racket-lang.org/2026/02/racket-v9-1.html)

生成摘要时出错

---

## 10. New accounts on HN 10x more likely to use em-dashes

**原文标题**: New accounts on HN 10x more likely to use em-dashes

**原文链接**: [https://www.marginalia.nu/weird-ai-crap/hn/](https://www.marginalia.nu/weird-ai-crap/hn/)

生成摘要时出错

---

## 11. Claude Code Remote Control

**原文标题**: Claude Code Remote Control

**原文链接**: [https://code.claude.com/docs/en/remote-control](https://code.claude.com/docs/en/remote-control)

生成摘要时出错

---

## 12. Show HN: Django Control Room – All Your Tools Inside the Django Admin

**原文标题**: Show HN: Django Control Room – All Your Tools Inside the Django Admin

**原文链接**: [https://github.com/yassi/dj-control-room](https://github.com/yassi/dj-control-room)

生成摘要时出错

---

## 13. 拓扑命名问题

**原文标题**: Topological Naming Problem

**原文链接**: [https://wiki.freecad.org/Topological_naming_problem](https://wiki.freecad.org/Topological_naming_problem)

生成摘要时出错

---

## 14. Danish government agency to ditch Microsoft software (2025)

**原文标题**: Danish government agency to ditch Microsoft software (2025)

**原文链接**: [https://therecord.media/denmark-digital-agency-microsoft-digital-independence](https://therecord.media/denmark-digital-agency-microsoft-digital-independence)

生成摘要时出错

---

## 15. Show HN: A real-time strategy game that AI agents can play

**原文标题**: Show HN: A real-time strategy game that AI agents can play

**原文链接**: [https://llmskirmish.com/](https://llmskirmish.com/)

生成摘要时出错

---

## 16. 100M-Row Challenge with PHP

**原文标题**: 100M-Row Challenge with PHP

**原文链接**: [https://github.com/tempestphp/100-million-row-challenge](https://github.com/tempestphp/100-million-row-challenge)

生成摘要时出错

---

## 17. Launch HN: TeamOut (YC W22) – AI agent for planning company retreats

**原文标题**: Launch HN: TeamOut (YC W22) – AI agent for planning company retreats

**原文链接**: [https://app.teamout.com/ai](https://app.teamout.com/ai)

生成摘要时出错

---

## 18. Show HN: Sgai – Goal-driven multi-agent software dev (GOAL.md → working code)

**原文标题**: Show HN: Sgai – Goal-driven multi-agent software dev (GOAL.md → working code)

**原文链接**: [https://github.com/sandgardenhq/sgai](https://github.com/sandgardenhq/sgai)

生成摘要时出错

---

## 19. PL/0

**原文标题**: PL/0

**原文链接**: [https://en.wikipedia.org/wiki/PL/0](https://en.wikipedia.org/wiki/PL/0)

生成摘要时出错

---

## 20. Text-Based Google Directions

**原文标题**: Text-Based Google Directions

**原文链接**: [https://gdir.telae.net/](https://gdir.telae.net/)

生成摘要时出错

---

## 21. Bcachefs creator insists his custom LLM is female and 'fully conscious'

**原文标题**: Bcachefs creator insists his custom LLM is female and 'fully conscious'

**原文链接**: [https://www.theregister.com/2026/02/25/bcachefs_creator_ai/](https://www.theregister.com/2026/02/25/bcachefs_creator_ai/)

生成摘要时出错

---

## 22. Confusables.txt and NFKC disagree on 31 characters

**原文标题**: Confusables.txt and NFKC disagree on 31 characters

**原文链接**: [https://paultendo.github.io/posts/unicode-confusables-nfkc-conflict/](https://paultendo.github.io/posts/unicode-confusables-nfkc-conflict/)

生成摘要时出错

---

## 23. Pi – A minimal terminal coding harness

**原文标题**: Pi – A minimal terminal coding harness

**原文链接**: [https://pi.dev](https://pi.dev)

**Pi** is a minimal, highly extensible terminal coding harness designed by Mario Zechner. Unlike many feature-heavy coding agents, Pi follows a "primitives, not features" philosophy, providing a lightweight core that users can adapt to their specific workflows through TypeScript extensions, skills, and prompt templates.

**Key Features and Capabilities:**
*   **Model Flexibility:** Supports over 15 providers (including Anthropic, OpenAI, and Google) and hundreds of models. Users can switch models mid-session or cycle through favorites via keyboard shortcuts.
*   **Context Engineering:** Features advanced context management through project-specific instructions (`AGENTS.md`), custom system prompts (`SYSTEM.md`), and customizable auto-compaction to manage context limits.
*   **Tree-Structured History:** Sessions are stored as trees, allowing users to navigate to previous points, branch out, and share history via HTML exports or GitHub Gists.
*   **Extensibility & Packaging:** Users can build or install functionality—such as sub-agents, plan modes, or MCP integration—using TypeScript. These are bundled as "pi packages" and shared via npm or Git.
*   **Execution Control:** A unique queuing system allows for "steering" messages (interrupting the agent) or "follow-up" messages (waiting for completion).

**Integration & Philosophy:**
Pi operates in four modes: **Interactive** (TUI), **Print/JSON** (for scripting), **RPC**, and an **SDK** for embedding into other apps. 

The tool’s core philosophy is aggressive minimalism. It intentionally excludes built-in features like permission popups, background processes, or pre-defined to-do lists, encouraging users to implement these via extensions or external tools like `tmux`. This approach ensures the tool remains a flexible harness rather than a rigid platform, allowing developers to shape it into their ideal coding assistant.

---

## 24. The History of a Security Hole

**原文标题**: The History of a Security Hole

**原文链接**: [https://www.os2museum.com/wp/the-history-of-a-security-hole/](https://www.os2museum.com/wp/the-history-of-a-security-hole/)

生成摘要时出错

---

## 25. Mercury 2: Fast reasoning LLM powered by diffusion

**原文标题**: Mercury 2: Fast reasoning LLM powered by diffusion

**原文链接**: [https://www.inceptionlabs.ai/blog/introducing-mercury-2](https://www.inceptionlabs.ai/blog/introducing-mercury-2)

生成摘要时出错

---

## 26. Red Hat takes on Docker Desktop with its enterprise Podman Desktop build

**原文标题**: Red Hat takes on Docker Desktop with its enterprise Podman Desktop build

**原文链接**: [https://thenewstack.io/red-hat-enters-the-cloud-native-developer-desktop-market/](https://thenewstack.io/red-hat-enters-the-cloud-native-developer-desktop-market/)

生成摘要时出错

---

## 27. Show HN: Moonshine Open-Weights STT models – higher accuracy than WhisperLargev3

**原文标题**: Show HN: Moonshine Open-Weights STT models – higher accuracy than WhisperLargev3

**原文链接**: [https://github.com/moonshine-ai/moonshine](https://github.com/moonshine-ai/moonshine)

生成摘要时出错

---

## 28. Japanese Death Poems

**原文标题**: Japanese Death Poems

**原文链接**: [https://www.secretorum.life/p/japanese-death-poems-part-3](https://www.secretorum.life/p/japanese-death-poems-part-3)

生成摘要时出错

---

## 29. I pitched a roller coaster to Disneyland at age 10 in 1978

**原文标题**: I pitched a roller coaster to Disneyland at age 10 in 1978

**原文链接**: [https://wordglyph.xyz/one-piece-at-a-time](https://wordglyph.xyz/one-piece-at-a-time)

生成摘要时出错

---

## 30. US orders diplomats to fight data sovereignty initiatives

**原文标题**: US orders diplomats to fight data sovereignty initiatives

**原文链接**: [https://www.reuters.com/sustainability/boards-policy-regulation/us-orders-diplomats-fight-data-sovereignty-initiatives-2026-02-25/](https://www.reuters.com/sustainability/boards-policy-regulation/us-orders-diplomats-fight-data-sovereignty-initiatives-2026-02-25/)

生成摘要时出错

---

## 31. Mac mini will be made at a new facility in Houston

**原文标题**: Mac mini will be made at a new facility in Houston

**原文链接**: [https://www.apple.com/newsroom/2026/02/apple-accelerates-us-manufacturing-with-mac-mini-production/](https://www.apple.com/newsroom/2026/02/apple-accelerates-us-manufacturing-with-mac-mini-production/)

生成摘要时出错

---

## 32. Hacking an old Kindle to display bus arrival times

**原文标题**: Hacking an old Kindle to display bus arrival times

**原文链接**: [https://www.mariannefeng.com/portfolio/kindle/](https://www.mariannefeng.com/portfolio/kindle/)

生成摘要时出错

---

## 33. Turing Completeness of GNU find

**原文标题**: Turing Completeness of GNU find

**原文链接**: [https://arxiv.org/abs/2602.20762](https://arxiv.org/abs/2602.20762)

生成摘要时出错

---

## 34. Nearby Glasses

**原文标题**: Nearby Glasses

**原文链接**: [https://github.com/yjeanrenaud/yj_nearbyglasses](https://github.com/yjeanrenaud/yj_nearbyglasses)

生成摘要时出错

---

## 35. Cl-kawa: Scheme on Java on Common Lisp

**原文标题**: Cl-kawa: Scheme on Java on Common Lisp

**原文链接**: [https://github.com/atgreen/cl-kawa](https://github.com/atgreen/cl-kawa)

生成摘要时出错

---

## 36. Show HN: Emdash – Open-source agentic development environment

**原文标题**: Show HN: Emdash – Open-source agentic development environment

**原文链接**: [https://github.com/generalaction/emdash](https://github.com/generalaction/emdash)

生成摘要时出错

---

## 37. Show HN: Scheme-langserver – Digest incomplete code with static analysis

**原文标题**: Show HN: Scheme-langserver – Digest incomplete code with static analysis

**原文链接**: [https://github.com/ufo5260987423/scheme-langserver](https://github.com/ufo5260987423/scheme-langserver)

生成摘要时出错

---

## 38. Steel Bank Common Lisp

**原文标题**: Steel Bank Common Lisp

**原文链接**: [https://www.sbcl.org/](https://www.sbcl.org/)

生成摘要时出错

---

## 39. Half million 'Words with Spaces' missing from dictionaries

**原文标题**: Half million 'Words with Spaces' missing from dictionaries

**原文链接**: [https://www.linguabase.org/words-with-spaces.html](https://www.linguabase.org/words-with-spaces.html)

生成摘要时出错

---

## 40. Amazon accused of widespread scheme to inflate prices across the economy

**原文标题**: Amazon accused of widespread scheme to inflate prices across the economy

**原文链接**: [https://www.thebignewsletter.com/p/amazon-busted-for-widespread-price](https://www.thebignewsletter.com/p/amazon-busted-for-widespread-price)

生成摘要时出错

---

## 41. The Pentagon Threatens Anthropic

**原文标题**: The Pentagon Threatens Anthropic

**原文链接**: [https://www.astralcodexten.com/p/the-pentagon-threatens-anthropic](https://www.astralcodexten.com/p/the-pentagon-threatens-anthropic)

生成摘要时出错

---

## 42. LLM=True

**原文标题**: LLM=True

**原文链接**: [https://blog.codemine.be/posts/2026/20260222-be-quiet/](https://blog.codemine.be/posts/2026/20260222-be-quiet/)

生成摘要时出错

---

## 43. Hugging Face Skills

**原文标题**: Hugging Face Skills

**原文链接**: [https://github.com/huggingface/skills](https://github.com/huggingface/skills)

生成摘要时出错

---

## 44. Anthropic Drops Flagship Safety Pledge

**原文标题**: Anthropic Drops Flagship Safety Pledge

**原文链接**: [https://time.com/7380854/exclusive-anthropic-drops-flagship-safety-pledge/](https://time.com/7380854/exclusive-anthropic-drops-flagship-safety-pledge/)

生成摘要时出错

---

## 45. Stripe valued at $159B, 2025 annual letter

**原文标题**: Stripe valued at $159B, 2025 annual letter

**原文链接**: [https://stripe.com/newsroom/news/stripe-2025-update](https://stripe.com/newsroom/news/stripe-2025-update)

生成摘要时出错

---

## 46. Cell Service for the Fairly Paranoid

**原文标题**: Cell Service for the Fairly Paranoid

**原文链接**: [https://www.cape.co/](https://www.cape.co/)

生成摘要时出错

---

## 47. Life-threatening blueberry recall upgraded to FDA's highest risk level

**原文标题**: Life-threatening blueberry recall upgraded to FDA's highest risk level

**原文链接**: [https://www.dailymail.co.uk/health/article-15591667/FDA-recall-blueberries-classifying-highest-risk-level.html](https://www.dailymail.co.uk/health/article-15591667/FDA-recall-blueberries-classifying-highest-risk-level.html)

生成摘要时出错

---

## 48. Tuna: A new, modern, modal launcher for macOS

**原文标题**: Tuna: A new, modern, modal launcher for macOS

**原文链接**: [https://tunaformac.com](https://tunaformac.com)

生成摘要时出错

---

## 49. Palantir Built the Data Layer That Right to Erasure Can't Touch

**原文标题**: Palantir Built the Data Layer That Right to Erasure Can't Touch

**原文链接**: [https://frontierlabs.substack.com/p/the-ai-is-the-last-thing-to-worry](https://frontierlabs.substack.com/p/the-ai-is-the-last-thing-to-worry)

生成摘要时出错

---

## 50. The archivist preserving decaying floppy disks

**原文标题**: The archivist preserving decaying floppy disks

**原文链接**: [https://www.popsci.com/technology/floppy-disk-archivist-project/](https://www.popsci.com/technology/floppy-disk-archivist-project/)

生成摘要时出错

---

## 51. Aesthetics of single threading

**原文标题**: Aesthetics of single threading

**原文链接**: [https://ta.fo/aesthetics-of-single-threading/](https://ta.fo/aesthetics-of-single-threading/)

生成摘要时出错

---

## 52. Why the KeePass format should be based on SQLite

**原文标题**: Why the KeePass format should be based on SQLite

**原文链接**: [https://mketab.org/blog/sqlite_kdbx/](https://mketab.org/blog/sqlite_kdbx/)

生成摘要时出错

---

## 53. I rendered 1,418 confusables over 230 fonts. Most aren't confusable to the eye

**原文标题**: I rendered 1,418 confusables over 230 fonts. Most aren't confusable to the eye

**原文链接**: [https://paultendo.github.io/posts/confusable-vision-visual-similarity/](https://paultendo.github.io/posts/confusable-vision-visual-similarity/)

生成摘要时出错

---

## 54. Meta problem with URPF our bundle in Boca raton

**原文标题**: Meta problem with URPF our bundle in Boca raton

**原文链接**: [https://metafixthis.com/](https://metafixthis.com/)

生成摘要时出错

---

## 55. 30 Years of Decompilation and the Unsolved Structuring Problem: Part 1 (2024)

**原文标题**: 30 Years of Decompilation and the Unsolved Structuring Problem: Part 1 (2024)

**原文链接**: [https://mahaloz.re/dec-history-pt1](https://mahaloz.re/dec-history-pt1)

生成摘要时出错

---

## 56. Optophone

**原文标题**: Optophone

**原文链接**: [https://en.wikipedia.org/wiki/Optophone](https://en.wikipedia.org/wiki/Optophone)

生成摘要时出错

---

## 57. LibreOffice resumes work on its self-hosted Google Docs alternative

**原文标题**: LibreOffice resumes work on its self-hosted Google Docs alternative

**原文链接**: [https://www.xda-developers.com/libreoffice-resumes-work-on-its-self-hosted-google-docs-alternative/](https://www.xda-developers.com/libreoffice-resumes-work-on-its-self-hosted-google-docs-alternative/)

生成摘要时出错

---

## 58. Hetzner Prices increase 30-40%

**原文标题**: Hetzner Prices increase 30-40%

**原文链接**: [https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/)

生成摘要时出错

---

## 59. 3D-Printed electric motor via multi-modal, multi-material extrusion

**原文标题**: 3D-Printed electric motor via multi-modal, multi-material extrusion

**原文链接**: [https://www.tandfonline.com/doi/full/10.1080/17452759.2026.2613185](https://www.tandfonline.com/doi/full/10.1080/17452759.2026.2613185)

生成摘要时出错

---

## 60. Running RISC-V in a VM to test my snaps

**原文标题**: Running RISC-V in a VM to test my snaps

**原文链接**: [https://blog.popey.com/2026/02/running-risc-v-in-a-vm-to-test-my-snaps/](https://blog.popey.com/2026/02/running-risc-v-in-a-vm-to-test-my-snaps/)

生成摘要时出错

---

## 61. Private Credit Fears Deepen with UBS Warning of 15% Defaults

**原文标题**: Private Credit Fears Deepen with UBS Warning of 15% Defaults

**原文链接**: [https://www.bloomberg.com/news/articles/2026-02-25/ai-disruption-fears-prompt-scrutiny-in-booming-secondary-market](https://www.bloomberg.com/news/articles/2026-02-25/ai-disruption-fears-prompt-scrutiny-in-booming-secondary-market)

生成摘要时出错

---

## 62. OpenAI, the US government and Persona built an identity surveillance machine

**原文标题**: OpenAI, the US government and Persona built an identity surveillance machine

**原文链接**: [https://vmfunc.re/blog/persona/](https://vmfunc.re/blog/persona/)

生成摘要时出错

---

## 63. Build Your Own Forth Interpreter

**原文标题**: Build Your Own Forth Interpreter

**原文链接**: [https://codingchallenges.fyi/challenges/challenge-forth/](https://codingchallenges.fyi/challenges/challenge-forth/)

生成摘要时出错

---

## 64. λProlog: Logic programming in higher-order logic

**原文标题**: λProlog: Logic programming in higher-order logic

**原文链接**: [https://www.lix.polytechnique.fr/Labo/Dale.Miller/lProlog/](https://www.lix.polytechnique.fr/Labo/Dale.Miller/lProlog/)

生成摘要时出错

---

## 65. Will Americans Get over Their Fear of Eating Animal Blood?

**原文标题**: Will Americans Get over Their Fear of Eating Animal Blood?

**原文链接**: [https://www.nytimes.com/2026/02/24/t-magazine/animal-blood-food-restaurants.html](https://www.nytimes.com/2026/02/24/t-magazine/animal-blood-food-restaurants.html)

生成摘要时出错

---

## 66. Unsung heroes: Flickr's URLs scheme

**原文标题**: Unsung heroes: Flickr's URLs scheme

**原文链接**: [https://unsung.aresluna.org/unsung-heroes-flickrs-urls-scheme/](https://unsung.aresluna.org/unsung-heroes-flickrs-urls-scheme/)

生成摘要时出错

---

## 67. Amazon would rather blame its own engineers than its AI

**原文标题**: Amazon would rather blame its own engineers than its AI

**原文链接**: [https://www.theregister.com/2026/02/24/amazon_blame_human_not_ai/](https://www.theregister.com/2026/02/24/amazon_blame_human_not_ai/)

生成摘要时出错

---

## 68. Windows 11 Notepad to support Markdown

**原文标题**: Windows 11 Notepad to support Markdown

**原文链接**: [https://blogs.windows.com/windows-insider/2026/01/21/notepad-and-paint-updates-begin-rolling-out-to-windows-insiders/](https://blogs.windows.com/windows-insider/2026/01/21/notepad-and-paint-updates-begin-rolling-out-to-windows-insiders/)

生成摘要时出错

---

## 69. A distributed queue in a single JSON file on object storage

**原文标题**: A distributed queue in a single JSON file on object storage

**原文链接**: [https://turbopuffer.com/blog/object-storage-queue](https://turbopuffer.com/blog/object-storage-queue)

生成摘要时出错

---

## 70. IDF killed Gaza aid workers at point blank range in 2025 massacre: Report

**原文标题**: IDF killed Gaza aid workers at point blank range in 2025 massacre: Report

**原文链接**: [https://www.dropsitenews.com/p/israeli-soldiers-tel-sultan-gaza-red-crescent-civil-defense-massacre-report-forensic-architecture-earshot](https://www.dropsitenews.com/p/israeli-soldiers-tel-sultan-gaza-red-crescent-civil-defense-massacre-report-forensic-architecture-earshot)

生成摘要时出错

---

## 71. Agents.md file isn't the problem. Your lack of Evals is

**原文标题**: Agents.md file isn't the problem. Your lack of Evals is

**原文链接**: [https://tessl.io/blog/your-agentsmd-file-isnt-the-problem-your-lack-of-evals-is/](https://tessl.io/blog/your-agentsmd-file-isnt-the-problem-your-lack-of-evals-is/)

生成摘要时出错

---

## 72. Meta frees React to live in its own foundation

**原文标题**: Meta frees React to live in its own foundation

**原文链接**: [https://www.theregister.com/2026/02/25/meta_sends_react_to_live/](https://www.theregister.com/2026/02/25/meta_sends_react_to_live/)

生成摘要时出错

---

## 73. We installed a single turnstile to feel secure

**原文标题**: We installed a single turnstile to feel secure

**原文链接**: [https://idiallo.com/blog/installed-single-turnstile-for-security-theater](https://idiallo.com/blog/installed-single-turnstile-for-security-theater)

生成摘要时出错

---

## 74. The history of knocking on wood

**原文标题**: The history of knocking on wood

**原文链接**: [https://resobscura.substack.com/p/neolithic-habits-machine-age-tools](https://resobscura.substack.com/p/neolithic-habits-machine-age-tools)

生成摘要时出错

---

## 75. Writing code is cheap now

**原文标题**: Writing code is cheap now

**原文链接**: [https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/](https://simonwillison.net/guides/agentic-engineering-patterns/code-is-cheap/)

生成摘要时出错

---

## 76. Sovereignty in a System Prompt

**原文标题**: Sovereignty in a System Prompt

**原文链接**: [https://pop.rdi.sh/sovereignty-in-a-system-prompt/](https://pop.rdi.sh/sovereignty-in-a-system-prompt/)

生成摘要时出错

---

## 77. How we rebuilt Next.js with AI in one week

**原文标题**: How we rebuilt Next.js with AI in one week

**原文链接**: [https://blog.cloudflare.com/vinext/](https://blog.cloudflare.com/vinext/)

生成摘要时出错

---

## 78. Anthropic just released a mobile version of Claude Code called Remote Control

**原文标题**: Anthropic just released a mobile version of Claude Code called Remote Control

**原文链接**: [https://venturebeat.com/orchestration/anthropic-just-released-a-mobile-version-of-claude-code-called-remote](https://venturebeat.com/orchestration/anthropic-just-released-a-mobile-version-of-claude-code-called-remote)

生成摘要时出错

---

## 79. Debian Removes Free Pascal Compiler / Lazarus IDE

**原文标题**: Debian Removes Free Pascal Compiler / Lazarus IDE

**原文链接**: [https://forum.lazarus.freepascal.org/index.php?topic=73405.0](https://forum.lazarus.freepascal.org/index.php?topic=73405.0)

生成摘要时出错

---

## 80. Ladybird adopts Rust, with help from AI

**原文标题**: Ladybird adopts Rust, with help from AI

**原文链接**: [https://ladybird.org/posts/adopting-rust/](https://ladybird.org/posts/adopting-rust/)

生成摘要时出错

---

## 81. I'm helping my dog vibe code games

**原文标题**: I'm helping my dog vibe code games

**原文链接**: [https://www.calebleak.com/posts/dog-game/](https://www.calebleak.com/posts/dog-game/)

生成摘要时出错

---

## 82. Show HN: enveil – hide your .env secrets from prAIng eyes

**原文标题**: Show HN: enveil – hide your .env secrets from prAIng eyes

**原文链接**: [https://github.com/GreatScott/enveil](https://github.com/GreatScott/enveil)

生成摘要时出错

---

## 83. Show HN: PgDog – Scale Postgres without changing the app

**原文标题**: Show HN: PgDog – Scale Postgres without changing the app

**原文链接**: [https://github.com/pgdogdev/pgdog](https://github.com/pgdogdev/pgdog)

生成摘要时出错

---

## 84. Show HN: Context Mode – 315 KB of MCP output becomes 5.4 KB in Claude Code

**原文标题**: Show HN: Context Mode – 315 KB of MCP output becomes 5.4 KB in Claude Code

**原文链接**: [https://github.com/mksglu/claude-context-mode](https://github.com/mksglu/claude-context-mode)

生成摘要时出错

---

## 85. Diode – Build, program, and simulate hardware

**原文标题**: Diode – Build, program, and simulate hardware

**原文链接**: [https://www.withdiode.com/](https://www.withdiode.com/)

生成摘要时出错

---

## 86. You Can't Buy a Data Center

**原文标题**: You Can't Buy a Data Center

**原文链接**: [https://timlig.com/posts/ai-supply-chain-crisis/](https://timlig.com/posts/ai-supply-chain-crisis/)

生成摘要时出错

---

## 87. US Military leaders meet with Anthropic to argue against Claude safeguards

**原文标题**: US Military leaders meet with Anthropic to argue against Claude safeguards

**原文链接**: [https://www.theguardian.com/us-news/2026/feb/24/anthropic-claude-military-ai](https://www.theguardian.com/us-news/2026/feb/24/anthropic-claude-military-ai)

生成摘要时出错

---

## 88. Extending C with Prolog (1994)

**原文标题**: Extending C with Prolog (1994)

**原文链接**: [https://www.amzi.com/articles/irq_expert_system.htm](https://www.amzi.com/articles/irq_expert_system.htm)

生成摘要时出错

---

## 89. Goodbye InnerHTML, Hello SetHTML: Stronger XSS Protection in Firefox 148

**原文标题**: Goodbye InnerHTML, Hello SetHTML: Stronger XSS Protection in Firefox 148

**原文链接**: [https://hacks.mozilla.org/2026/02/goodbye-innerhtml-hello-sethtml-stronger-xss-protection-in-firefox-148/](https://hacks.mozilla.org/2026/02/goodbye-innerhtml-hello-sethtml-stronger-xss-protection-in-firefox-148/)

生成摘要时出错

---

## 90. IRS Tactics Against Meta Open a New Front in the Corporate Tax Fight

**原文标题**: IRS Tactics Against Meta Open a New Front in the Corporate Tax Fight

**原文链接**: [https://www.nytimes.com/2026/02/24/business/irs-meta-corporate-taxes.html](https://www.nytimes.com/2026/02/24/business/irs-meta-corporate-taxes.html)

生成摘要时出错

---

## 91. Looks like it is happening

**原文标题**: Looks like it is happening

**原文链接**: [https://www.math.columbia.edu/~woit/wordpress/?p=15500](https://www.math.columbia.edu/~woit/wordpress/?p=15500)

生成摘要时出错

---

## 92. Read Locks Are Not Your Friends

**原文标题**: Read Locks Are Not Your Friends

**原文链接**: [https://eventual-consistency.vercel.app/posts/write-locks-faster](https://eventual-consistency.vercel.app/posts/write-locks-faster)

生成摘要时出错

---

## 93. AIs can't stop recommending nuclear strikes in war game simulations

**原文标题**: AIs can't stop recommending nuclear strikes in war game simulations

**原文链接**: [https://www.newscientist.com/article/2516885-ais-cant-stop-recommending-nuclear-strikes-in-war-game-simulations/](https://www.newscientist.com/article/2516885-ais-cant-stop-recommending-nuclear-strikes-in-war-game-simulations/)

生成摘要时出错

---

## 94. I beat Grok 4 on ARC-AGI-2 using a CPU-only symbolic engine (18.1% score)

**原文标题**: I beat Grok 4 on ARC-AGI-2 using a CPU-only symbolic engine (18.1% score)

**原文链接**: [https://github.com/Ag3497120/verantyx-v6](https://github.com/Ag3497120/verantyx-v6)

生成摘要时出错

---

## 95. Companies cutting jobs as investments shift toward AI

**原文标题**: Companies cutting jobs as investments shift toward AI

**原文链接**: [https://www.reuters.com/business/world-at-work/companies-cutting-jobs-investments-shift-toward-ai-2026-02-25/](https://www.reuters.com/business/world-at-work/companies-cutting-jobs-investments-shift-toward-ai-2026-02-25/)

生成摘要时出错

---

## 96. Compress Your Claude.md: Cut 60-70% of System Prompt Bloat in Claude Code

**原文标题**: Compress Your Claude.md: Cut 60-70% of System Prompt Bloat in Claude Code

**原文链接**: [https://techloom.it/blog/compress-claude-md.html](https://techloom.it/blog/compress-claude-md.html)

生成摘要时出错

---

## 97. White House list of media offenders

**原文标题**: White House list of media offenders

**原文链接**: [https://www.whitehouse.gov/mediabias/](https://www.whitehouse.gov/mediabias/)

生成摘要时出错

---

## 98. The Missing Semester of Your CS Education – Revised for 2026

**原文标题**: The Missing Semester of Your CS Education – Revised for 2026

**原文链接**: [https://missing.csail.mit.edu/](https://missing.csail.mit.edu/)

生成摘要时出错

---

## 99. What it means that Ubuntu is using Rust

**原文标题**: What it means that Ubuntu is using Rust

**原文链接**: [https://smallcultfollowing.com/babysteps/blog/2026/02/23/ubuntu-rustnation/](https://smallcultfollowing.com/babysteps/blog/2026/02/23/ubuntu-rustnation/)

生成摘要时出错

---

## 100. OpenAI resets spending expectations, from $1.4T to $600B

**原文标题**: OpenAI resets spending expectations, from $1.4T to $600B

**原文链接**: [https://www.cnbc.com/2026/02/20/openai-resets-spend-expectations-targets-around-600-billion-by-2030.html](https://www.cnbc.com/2026/02/20/openai-resets-spend-expectations-targets-around-600-billion-by-2030.html)

生成摘要时出错

---

