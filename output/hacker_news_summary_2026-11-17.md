# Hacker News 热门文章摘要 (2026-11-17)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 卡内基梅隆大学在 YouTube 上免费提供计算机科学课程

**原文标题**: Carnegie Mellon is putting computer science courses on YouTube for free

**原文链接**: [https://www.cs.cmu.edu/learn/](https://www.cs.cmu.edu/learn/)

卡内基梅隆大学（CMU）通过将多门计算机科学课程免费上传至 YouTube，显著扩大了其世界级教育资源的覆盖范围。这一举措主要由 CMU 计算机科学学院推动，旨在促进高水平技术知识的普及，让全球受众都能获取与在校学生相同的课程资源。

“CMU Courses” YouTube 频道提供完整的学期系列讲座，涵盖了从基础到高级的广泛主题。重点领域包括：

*   **数据库系统：** 包括高级实现和分布式数据库。
*   **计算机系统：** 涵盖架构及现代硬件的内部运作。
*   **操作系统：** 深入探讨内核开发和系统管理。
*   **软件工程与算法：** 专注于实际应用和理论基础的专业内容。

由于卡内基梅隆大学始终位居世界顶尖计算机科学机构之列，这一举措显得尤为重要。通过免费提供这些资源，该大学为自学者、其他院校的学生以及终身学习者消除了经济和地理障碍。

与短篇教程不同，这些视频是实际课堂教学的全程记录，提供了严谨的学术体验。虽然观看者无法获得大学学分或导师评分，但这些高质量材料的公开是对开源教育运动的重大贡献，也为全球研究人员和工程师群体提供了有力支持。

---

## 2. Windows 11 正在收集你使用的编程助手和开发工具数据

**原文标题**: Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use

**原文链接**: [https://xusheng.dev/posts/windows-coding-agent-telemetry/](https://xusheng.dev/posts/windows-coding-agent-telemetry/)

最近对 Windows 11 二进制文件 `MissionControlAggregator.dll` 的逆向工程显示，微软正在专门追踪 AI 编程助手和开发工具的使用情况。调查发现，该系统会监控 `claude.exe`、`cursor.exe`、`copilot.exe` 和 `codex.exe` 等可执行文件，以及 `python.exe`、`gcc.exe`、`node.exe` 和 `code.exe` 等标准开发工具。

该追踪机制并不直接扫描进程；相反，它通过订阅现有的 Windows 事件追踪 (ETW) 日志和 WSL (Windows Subsystem for Linux) 事件来实现。当检测到匹配的可执行文件时，系统会更新存储在 `C:\ProgramData\Microsoft\Diagnosis\` 中的本地位图 (bitset)。这些信息随后会被编译成名为 `Segments.SubCohorts` 的报告，将使用情况分类到特定的工具和助手“槽位”中。

至关重要的一点是，这些报告会通过 `DiagTrack` 服务（连接的用户体验和遥测）传输给微软。该数据被归类为“可选诊断数据”，这一设置在包括美国在内的许多地区默认是开启的。测试证实，即使只是将一个可执行文件重命名为受追踪的名称之一，也会触发检测并将遥测报告加入上传队列。

虽然目前的报告似乎仅追踪工具的存在，而非具体的源代码或 AI 提示词，但对开发者工作流的这种细颗粒度监控引发了严重的隐私疑虑。希望阻止此数据收集的用户必须手动选择退出，方法是在 Windows“**隐私与安全**”设置的“**诊断与反馈**”部分中禁用“发送可选诊断数据”。

---

## 3. BugMeNot has closed

**原文标题**: BugMeNot has closed

**原文链接**: [https://www.bugmenot.com/](https://www.bugmenot.com/)

生成摘要时出错

---

## 4. 全球最大品牌经由 Optimizely 感染恶意软件

**原文标题**: World's Largest Brands Infected With Malware Via Optimizely

**原文链接**: [https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)

2026年11月16日，一场重大的供应链攻击通过 Optimizely Web 实验平台，导致 178 家机构的 188 个 JavaScript 代码片段遭到破坏。受影响的高知名度目标包括 Zoom、BBC、CNN、Salesforce、汇丰银行（HSBC）和宜家（IKEA）。

此次攻击利用了 Optimizely 的“Project JavaScript”字段，使得恶意代码可以直接从受信任的 `cdn.optimizely.com` 域名分发。由于这些脚本来自受影响网站已经信任的主机，这种注入方式绕过了许多标准安全过滤器。该恶意软件具有多种功能，可执行以下恶意活动：

*   **加密货币窃取：** 它会自动将页面文本、剪贴板和传出的网络请求中的合法钱包地址替换为攻击者的地址。
*   **财务信息窃取：** 它从表单提交和 POST 请求中获取信用卡详情（卡号、有效期和 CVV 码）。
*   **数据外泄：** 它窃取了（未标记为 HttpOnly 的）Cookie，并利用 `html2canvas` 截取受感染页面的屏幕截图。
*   **iOS 漏洞利用：** 它向运行易受攻击版本（iOS 18.6 或更早版本）的 iPhone 和 iPad 投送 Coruna 和 DarkSword 漏洞利用工具包。

在漏洞影响被基本消除时，攻击者已窃取了价值约 7,040 美元的加密货币。尽管大部分恶意代码在 24 小时内被移除，但此次事件敲响了警钟：即使原始基础设施未被攻破，第三方依赖项仍可能被武器化。安全专家强调，实施强大的内容安全策略（CSP）并监控受信任 JavaScript 的异常更改，对于检测此类复杂的注入攻击至关重要。

---

## 5. 如何进入安全领域：Ptacek 版 (2012)

**原文标题**: How to Break into Security, Ptacek Edition (2012)

**原文链接**: [https://krebsonsecurity.com/2012/06/how-to-break-into-security-ptacek-edition/](https://krebsonsecurity.com/2012/06/how-to-break-into-security-ptacek-edition/)

在2012年的这场访谈中，Matasano Security的创始人托马斯·普塔塞克（Thomas Ptacek）为进入信息安全领域提供了一份路线图。他强调，相比传统的软件开发，信息安全是一个高薪、唯才是举且充满智力挑战的选择。

普塔塞克的首要建议是**学习编程**。他认为，通过代码解决问题的能力是获得职业自主权最重要的因素。虽然掌握各种语言（如 Python、Ruby、Java）都是可以的，但理解底层逻辑对于高阶安全工作至关重要。

他将**应用安全（AppSec）**视为该领域中最关键且最具前景的细分方向。与防火墙管理等被动防御角色不同，应用安全涉及通过攻击软件来发现漏洞，或制定对策来预防漏洞。

对于想要进入该行业的人，普塔塞克概述了具体的三个实践步骤：
1. **学习：** 阅读《Web应用黑客手册》（*The Web Application Hacker’s Handbook*）。
2. **练习：** 利用 Amazon EC2 账号搭建一个“打靶场”。
3. **实验：** 安装存在漏洞的旧版软件（如 WordPress），并使用 Burp Suite 或 WebScarab 等行业标准工具来寻找漏洞。

对于已在 IT 行业的专业人士，普塔塞克建议通过担任**测试（QA）或运维（DevOps）**角色来靠近软件开发，从而实现转型。通过在这些部门建立基础的安全测试流程，个人可以获得显著的影响力，并晋升至高级安全管理职位。

最终，普塔塞克将安全定义为操纵技术的艺术。他鼓励向往者深入研究系统的工作原理——从微架构到编译原理——并通过不断的实验积累实践经验。

---

## 6. OpenCode 浏览

**原文标题**: OpenCode Browse

**原文链接**: [https://opencode.ai/product/browse](https://opencode.ai/product/browse)

生成摘要时出错

---

## 7. Optimizely 遭入侵，在 Zoom 和 GitLab 分发恶意软件

**原文标题**: Optimizely Compromised, Served Malware on Zoom, GitLab

**原文链接**: [https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)

2026年11月16日，Optimizely Web 实验平台遭遇了一场重大的供应链攻击，导致 178 家机构的访客被植入了恶意 JavaScript。受影响的高知名度目标包括 **Zoom、BBC、GitLab、Salesforce、汇丰银行 (HSBC) 以及艾可飞 (Equifax)**。

**攻击机制**
攻击者获得了对 Optimizely “项目 JavaScript” (Project JavaScript) 字段的未经授权写入权限，使他们能够直接在通过 Optimizely 受信任 CDN 分发的代码片段中注入恶意代码。由于脚本是从受信任域名 (`cdn.optimizely.com`) 分发并带有有效证书，这种注入绕过了许多标准的安全性过滤。

**恶意软件功能**
注入的有效载荷是一个精密的多功能套件，执行了以下操作：
*   **加密货币替换：** 识别页面或剪贴板中的加密货币钱包地址，并将其替换为攻击者的地址。
*   **信用卡盗刷：** 从非托管表单字段中拦截信用卡数据（卡号、CVV 和有效期）。
*   **数据窃取：** 捕获 Cookie 并利用 `html2canvas` 对敏感页面进行截图。
*   **iOS 漏洞利用：** 向运行旧版本 iOS 的 iPhone 和 iPad 投送 “Coruna” 和 “DarkSword” 漏洞利用套件。

**影响与启示**
此次攻击在短短数小时内造成了已确认的总计达数千美元的加密货币窃取。虽然大部分恶意代码在深夜前已被清除，但此事件凸显了一个关键漏洞：**第三方依赖**。即使网站自身的基础设施未被入侵，如果其信任的外部脚本被武器化，该网站仍会受到侵害。

安全专家指出，强大的**内容安全策略 (CSP)** 和子资源监控原本可以检测或阻断这些未经授权的外部连接和脚本更改，即便它们源自像 Optimizely 这样受信任的合作伙伴。

---

## 8. Chemistry is Actually Geometry

**原文标题**: Chemistry is Actually Geometry

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/chemistry-is-actually-geometry](https://chillphysicsenjoyer.substack.com/p/chemistry-is-actually-geometry)

生成摘要时出错

---

## 9. Grazing sheep in fields with solar arrays

**原文标题**: Grazing sheep in fields with solar arrays

**原文链接**: [https://news.cornell.edu/stories/2026/10/sheep-grazing-solar-fields-offers-farmers-economic-ecological-gains](https://news.cornell.edu/stories/2026/10/sheep-grazing-solar-fields-offers-farmers-economic-ecological-gains)

生成摘要时出错

---

## 10. Jiff 1.0: A datetime library for Rust

**原文标题**: Jiff 1.0: A datetime library for Rust

**原文链接**: [https://burntsushi.net/jiff/](https://burntsushi.net/jiff/)

生成摘要时出错

---

## 11. Frame – 31.5" color ePaper display

**原文标题**: Frame – 31.5" color ePaper display

**原文链接**: [https://trmnl.com/blog/introducing-frame](https://trmnl.com/blog/introducing-frame)

生成摘要时出错

---

## 12. Technical issue at JPMorgan Chase triggers online banking delays for US banks

**原文标题**: Technical issue at JPMorgan Chase triggers online banking delays for US banks

**原文链接**: [https://apnews.com/article/bank-outage-chase-wells-fargo-truist-50fee2693c22f597fa6ca51a97ef2cda](https://apnews.com/article/bank-outage-chase-wells-fargo-truist-50fee2693c22f597fa6ca51a97ef2cda)

生成摘要时出错

---

## 13. Formal Verification Is Not Verifiable

**原文标题**: Formal Verification Is Not Verifiable

**原文链接**: [https://alperenkeles.com/posts/formal-verification-is-not-verifiable/](https://alperenkeles.com/posts/formal-verification-is-not-verifiable/)

生成摘要时出错

---

## 14. Rust changed me as a developer

**原文标题**: Rust changed me as a developer

**原文链接**: [https://blog.startifact.com/posts/how-rust-changed-me/](https://blog.startifact.com/posts/how-rust-changed-me/)

生成摘要时出错

---

## 15. Do Repeat Yourself

**原文标题**: Do Repeat Yourself

**原文链接**: [https://arcentry.com/blog/do-repeat-yourself/](https://arcentry.com/blog/do-repeat-yourself/)

生成摘要时出错

---

## 16. Squircles

**原文标题**: Squircles

**原文链接**: [https://linebender.org/wiki/curves/squircle/](https://linebender.org/wiki/curves/squircle/)

生成摘要时出错

---

## 17. United Airlines experiencing a widespread system outage, airline says

**原文标题**: United Airlines experiencing a widespread system outage, airline says

**原文链接**: [https://www.cnn.com/2026/11/16/us/united-airlines-outage](https://www.cnn.com/2026/11/16/us/united-airlines-outage)

生成摘要时出错

---

## 18. Show HN: Sutra-OS – A self-hosted ontology platform

**原文标题**: Show HN: Sutra-OS – A self-hosted ontology platform

**原文链接**: [https://github.com/0nelight/sutra-os](https://github.com/0nelight/sutra-os)

生成摘要时出错

---

## 19. Spamhaus new email sender requirements in November

**原文标题**: Spamhaus new email sender requirements in November

**原文链接**: [https://www.spamhaus.org/sender-guidelines/](https://www.spamhaus.org/sender-guidelines/)

生成摘要时出错

---

## 20. My Quest to push native Three.js quality match AAA Game Engines

**原文标题**: My Quest to push native Three.js quality match AAA Game Engines

**原文链接**: [https://ben3d.ca/blog/building-the-aaa-lighting-pipeline-in-threejs](https://ben3d.ca/blog/building-the-aaa-lighting-pipeline-in-threejs)

生成摘要时出错

---

## 21. 微软将大规模邮件故障归咎于7月修复程序引入的软件缺陷

**原文标题**: Microsoft blames monster email outage on software defect introduced in July fix

**原文链接**: [https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026](https://www.theregister.com/saas/2026/11/16/microsoft-blames-monster-email-outage-on-software-defect-introduced-in-july-fix/5310026)

生成摘要时出错

---

## 22. The Secret ThinkPad Powerbutton Code to Bring Dead Laptops Back to Life (2007)

**原文标题**: The Secret ThinkPad Powerbutton Code to Bring Dead Laptops Back to Life (2007)

**原文链接**: [https://masnick.com/posts/the-secret-thinkpad-powerbutton-code-to-bring-dead-laptops-back-to-life/](https://masnick.com/posts/the-secret-thinkpad-powerbutton-code-to-bring-dead-laptops-back-to-life/)

生成摘要时出错

---

## 23. Michael Mann's 'Heat' Copyright Fight Turns on a Deal with Himself

**原文标题**: Michael Mann's 'Heat' Copyright Fight Turns on a Deal with Himself

**原文链接**: [https://copyrightlately.com/michael-mann-heat-copyright-termination/](https://copyrightlately.com/michael-mann-heat-copyright-termination/)

生成摘要时出错

---

## 24. How to Intercept HTTP/3 Traffic: QUIC and Qpack

**原文标题**: How to Intercept HTTP/3 Traffic: QUIC and Qpack

**原文链接**: [https://interceptsuite.com/blog/intercept-http3-traffic-quic-qpack-explained/](https://interceptsuite.com/blog/intercept-http3-traffic-quic-qpack-explained/)

生成摘要时出错

---

## 25. Aristotle Expands into Rust

**原文标题**: Aristotle Expands into Rust

**原文链接**: [https://www.harmonic.fun/news/aristotle-rust-verification/](https://www.harmonic.fun/news/aristotle-rust-verification/)

Aristotle has announced its expansion into the Rust programming language, adding to its existing support for C and Verilog. This development marks a significant step in the company’s mission to move beyond traditional testing toward formal verification—mathematically proving that code functions exactly as intended before it is deployed.

The expansion is particularly vital for mission-critical sectors such as aerospace, finance, and cybersecurity. A primary focus is the Solana blockchain, where Aristotle helps secure smart contracts. Because blockchain transactions are irreversible and high-stakes, Aristotle provides a crucial layer of security by proving code properties across all possible inputs and catching flaws that manual audits might miss. Key capabilities include proving the absence of undefined behavior (even in `unsafe` blocks) and ensuring that C-to-Rust rewrites maintain behavioral equivalence to the original code.

Early real-world successes include identifying a rounding bug in the Manifest open-source order book and proving the transaction consistency of Project 0’s prime brokerage system. To support wider adoption, Aristotle is partnering with the Solana Foundation to help developers verify their programs continuously with every code update.

Aristotle for Rust is available now through a self-serve, consumption-based pricing model at aristotle.harmonic.fun, with custom enterprise options and dedicated support also available.

---

## 26. Many of Amazon’s Black Friday and Cyber Monday “deals” offered no savings

**原文标题**: Many of Amazon’s Black Friday and Cyber Monday “deals” offered no savings

**原文链接**: [http://groundworkcollaborative.org/news/amazons-decoy-deals-groundwork-investigation-reveals-nearly-1-in-3-black-friday-and-cyber-monday-deals-advertised-by-amazon-offered-no-savings-to-shoppers-nearly-1-in-10-w/](http://groundworkcollaborative.org/news/amazons-decoy-deals-groundwork-investigation-reveals-nearly-1-in-3-black-friday-and-cyber-monday-deals-advertised-by-amazon-offered-no-savings-to-shoppers-nearly-1-in-10-w/)

生成摘要时出错

---

## 27. Jolt – Clojure that speaks C

**原文标题**: Jolt – Clojure that speaks C

**原文链接**: [https://jolt-lang.net/](https://jolt-lang.net/)

生成摘要时出错

---

## 28. Strengthening the fight against online child sexual abuse

**原文标题**: Strengthening the fight against online child sexual abuse

**原文链接**: [https://openai.com/index/strengthening-online-child-safety/](https://openai.com/index/strengthening-online-child-safety/)

生成摘要时出错

---

## 29. The origins of the placenta

**原文标题**: The origins of the placenta

**原文链接**: [https://www.caltech.edu/about/news/uncovering-the-hidden-origins-of-the-placenta](https://www.caltech.edu/about/news/uncovering-the-hidden-origins-of-the-placenta)

生成摘要时出错

---

## 30. Kubernetes Is Strengthening Its Position as the AI Platform of Choice

**原文标题**: Kubernetes Is Strengthening Its Position as the AI Platform of Choice

**原文链接**: [https://cloudnativenow.com/features/kubernetes-is-strengthening-its-position-as-the-ai-platform-of-choice/](https://cloudnativenow.com/features/kubernetes-is-strengthening-its-position-as-the-ai-platform-of-choice/)

生成摘要时出错

---

## 31. Comcast's "fiber-powered Wi-Fi" is cable, AT&T says in false advertising case

**原文标题**: Comcast's "fiber-powered Wi-Fi" is cable, AT&T says in false advertising case

**原文链接**: [https://arstechnica.com/tech-policy/2026/11/comcast-falsely-advertises-cable-internet-as-fiber-powered-att-lawsuit-says/](https://arstechnica.com/tech-policy/2026/11/comcast-falsely-advertises-cable-internet-as-fiber-powered-att-lawsuit-says/)

生成摘要时出错

---

## 32. OOS – an open operating system for the Rigol Scopes

**原文标题**: OOS – an open operating system for the Rigol Scopes

**原文链接**: [https://www.eevblog.com/forum/testgear/oos-an-open-operating-system-for-the-rigol-scopes/](https://www.eevblog.com/forum/testgear/oos-an-open-operating-system-for-the-rigol-scopes/)

生成摘要时出错

---

## 33. Nvidia was in trouble before the Jensen Huang mess

**原文标题**: Nvidia was in trouble before the Jensen Huang mess

**原文链接**: [https://www.wired.com/story/nvidia-was-already-in-trouble-before-the-jensen-huang-mess/](https://www.wired.com/story/nvidia-was-already-in-trouble-before-the-jensen-huang-mess/)

生成摘要时出错

---

## 34. Beyond Floating Point: Next-Generation Computer Arithmetic

**原文标题**: Beyond Floating Point: Next-Generation Computer Arithmetic

**原文链接**: [https://web.stanford.edu/class/ee380/Abstracts/170201.html](https://web.stanford.edu/class/ee380/Abstracts/170201.html)

生成摘要时出错

---

## 35. Coffeehouses and the Rise of Science [pdf]

**原文标题**: Coffeehouses and the Rise of Science [pdf]

**原文链接**: [https://www.monirbounadi.com/Bounadi_JMP.pdf](https://www.monirbounadi.com/Bounadi_JMP.pdf)

生成摘要时出错

---

## 36. First phase of embedded assessments at OpenAI

**原文标题**: First phase of embedded assessments at OpenAI

**原文链接**: [https://openai.com/index/our-first-phase-of-embedded-assessments/](https://openai.com/index/our-first-phase-of-embedded-assessments/)

生成摘要时出错

---

## 37. Interpreting claims that a theorem is correct because it was checked in Lean

**原文标题**: Interpreting claims that a theorem is correct because it was checked in Lean

**原文链接**: [https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/](https://xenaproject.wordpress.com/2026/11/12/and-the-proof-is-checked-in-lean/)

生成摘要时出错

---

## 38. Researchers track whole body movement with just a smartwatch

**原文标题**: Researchers track whole body movement with just a smartwatch

**原文链接**: [https://news.cornell.edu/stories/2026/11/researchers-track-whole-body-movement-just-smartwatch](https://news.cornell.edu/stories/2026/11/researchers-track-whole-body-movement-just-smartwatch)

生成摘要时出错

---

## 39. Software is breaking down at a systemic level

**原文标题**: Software is breaking down at a systemic level

**原文链接**: [https://www.breck-mckye.com/blog/2026/11/software-is-breaking-down-at-a-systemic-level/](https://www.breck-mckye.com/blog/2026/11/software-is-breaking-down-at-a-systemic-level/)

生成摘要时出错

---

## 40. A 512 KiB binary message teaching chess without a shared language

**原文标题**: A 512 KiB binary message teaching chess without a shared language

**原文链接**: [https://artemlegotin.com/golden-board/](https://artemlegotin.com/golden-board/)

生成摘要时出错

---

## 41. Eight years of running DocSpring on Convox

**原文标题**: Eight years of running DocSpring on Convox

**原文链接**: [https://docspring.com/blog/posts/eight-years-running-docspring-convox/](https://docspring.com/blog/posts/eight-years-running-docspring-convox/)

生成摘要时出错

---

## 42. US will say "no" to global ban on killer robots

**原文标题**: US will say "no" to global ban on killer robots

**原文链接**: [https://www.newsweek.com/us-expected-to-block-killer-robot-treaty-talks-12722369](https://www.newsweek.com/us-expected-to-block-killer-robot-treaty-talks-12722369)

生成摘要时出错

---

## 43. Uber says hackers stole information on close to 150k DLs during data breach

**原文标题**: Uber says hackers stole information on close to 150k DLs during data breach

**原文链接**: [https://techcrunch.com/2026/11/16/uber-confirms-hackers-stole-thousands-of-drivers-license-information-in-data-breach/](https://techcrunch.com/2026/11/16/uber-confirms-hackers-stole-thousands-of-drivers-license-information-in-data-breach/)

生成摘要时出错

---

## 44. Smallest possible nopert polyhedra: the Septopert

**原文标题**: Smallest possible nopert polyhedra: the Septopert

**原文链接**: [https://github.com/tom7/noperts/blob/main/septopert.md](https://github.com/tom7/noperts/blob/main/septopert.md)

生成摘要时出错

---

## 45. Show HN: Open-source, real-time object tracking for live video feeds

**原文标题**: Show HN: Open-source, real-time object tracking for live video feeds

**原文链接**: [https://github.com/aryamandarda/tamserve](https://github.com/aryamandarda/tamserve)

生成摘要时出错

---

## 46. How to make almost anything

**原文标题**: How to make almost anything

**原文链接**: [https://pub.cba.mit.edu/863.26/site/](https://pub.cba.mit.edu/863.26/site/)

生成摘要时出错

---

## 47. FBI has possession of router that the FAA says is behind Friday's ATC meltdown

**原文标题**: FBI has possession of router that the FAA says is behind Friday's ATC meltdown

**原文链接**: [https://www.cnn.com/2026/11/16/politics/video/the-arena-fbi-possesion-router-faa-atc-meltdown](https://www.cnn.com/2026/11/16/politics/video/the-arena-fbi-possesion-router-faa-atc-meltdown)

生成摘要时出错

---

## 48. Winudf – DVD / BluRay driver for DOS, Windows 1.x – 3x / 95 / 98 / ME

**原文标题**: Winudf – DVD / BluRay driver for DOS, Windows 1.x – 3x / 95 / 98 / ME

**原文链接**: [https://github.com/ages2001/WINUDF](https://github.com/ages2001/WINUDF)

生成摘要时出错

---

## 49. The Active Directory Era Is Finally Over

**原文标题**: The Active Directory Era Is Finally Over

**原文链接**: [https://infisical.com/blog/active-directory-machine-identity](https://infisical.com/blog/active-directory-machine-identity)

生成摘要时出错

---

## 50. Pentagon fails ninth straight audit despite progress in organizing finances

**原文标题**: Pentagon fails ninth straight audit despite progress in organizing finances

**原文链接**: [https://www.reuters.com/business/aerospace-defense/pentagon-fails-ninth-straight-audit-despite-progress-organizing-finances-2026-11-16/](https://www.reuters.com/business/aerospace-defense/pentagon-fails-ninth-straight-audit-despite-progress-organizing-finances-2026-11-16/)

生成摘要时出错

---

## 51. Psychic: Like fzf but learns from your actions

**原文标题**: Psychic: Like fzf but learns from your actions

**原文链接**: [https://klauria.tech/psychic/](https://klauria.tech/psychic/)

生成摘要时出错

---

## 52. Universal XSS in uBlock Origin from website-driven element picker

**原文标题**: Universal XSS in uBlock Origin from website-driven element picker

**原文链接**: [https://iter.ca/post/ubo-uxss/](https://iter.ca/post/ubo-uxss/)

生成摘要时出错

---

## 53. Elementary Applied Topology, 2nd Ed by Robert Ghrist [pdf]

**原文标题**: Elementary Applied Topology, 2nd Ed by Robert Ghrist [pdf]

**原文链接**: [https://www2.math.upenn.edu/~ghrist/books/EAT.pdf](https://www2.math.upenn.edu/~ghrist/books/EAT.pdf)

生成摘要时出错

---

## 54. The Fed Is Worried AI Agents Could Trigger a Bank Run

**原文标题**: The Fed Is Worried AI Agents Could Trigger a Bank Run

**原文链接**: [https://gizmodo.com/the-fed-is-worried-ai-agents-could-trigger-a-bank-run-2000840566](https://gizmodo.com/the-fed-is-worried-ai-agents-could-trigger-a-bank-run-2000840566)

生成摘要时出错

---

## 55. How Billions in Safe Insurance Money Is Being Bet on A.I. Debt

**原文标题**: How Billions in Safe Insurance Money Is Being Bet on A.I. Debt

**原文链接**: [https://www.nytimes.com/2026/11/16/business/insurance-ai-debt.html](https://www.nytimes.com/2026/11/16/business/insurance-ai-debt.html)

生成摘要时出错

---

## 56. Show HN: Fakemetrics.com – "build in public" like a superstar

**原文标题**: Show HN: Fakemetrics.com – "build in public" like a superstar

**原文链接**: [https://fakemetrics.com/](https://fakemetrics.com/)

生成摘要时出错

---

## 57. 3D Sword Coast Map with weather and day/night cycle (Rust to WebGL)

**原文标题**: 3D Sword Coast Map with weather and day/night cycle (Rust to WebGL)

**原文链接**: [https://swordcoastmap.com/](https://swordcoastmap.com/)

生成摘要时出错

---

## 58. Nature-Based Sanitation. Cihuatlán: A Large-Scale Artificial Wetland

**原文标题**: Nature-Based Sanitation. Cihuatlán: A Large-Scale Artificial Wetland

**原文链接**: [https://revista.unaminternacional.unam.mx/en/nota/12/saneamiento-basado-en-la-naturaleza-cihuatlan-un-humedal-construido-de-gran-escala](https://revista.unaminternacional.unam.mx/en/nota/12/saneamiento-basado-en-la-naturaleza-cihuatlan-un-humedal-construido-de-gran-escala)

生成摘要时出错

---

## 59. A quest to create the perfect whiskey glass

**原文标题**: A quest to create the perfect whiskey glass

**原文链接**: [https://www.nytimes.com/2026/11/13/dining/drinks/kurt-josef-zalto-whiskey-glass.html](https://www.nytimes.com/2026/11/13/dining/drinks/kurt-josef-zalto-whiskey-glass.html)

生成摘要时出错

---

## 60. Do we still have to denormalize? Have your schema and search it too

**原文标题**: Do we still have to denormalize? Have your schema and search it too

**原文链接**: [https://www.paradedb.com/blog/joins](https://www.paradedb.com/blog/joins)

生成摘要时出错

---

## 61. Obituaries

**原文标题**: Obituaries

**原文链接**: [https://stratechery.com/2026/obituaries/](https://stratechery.com/2026/obituaries/)

生成摘要时出错

---

## 62. The Lasting Influence of John Berger

**原文标题**: The Lasting Influence of John Berger

**原文链接**: [https://www.newyorker.com/magazine/2026/11/16/john-berger-a-life-tom-overton-book-review](https://www.newyorker.com/magazine/2026/11/16/john-berger-a-life-tom-overton-book-review)

生成摘要时出错

---

## 63. United Halts Flights as It Addresses 'Widespread System Outage'

**原文标题**: United Halts Flights as It Addresses 'Widespread System Outage'

**原文链接**: [https://www.nytimes.com/2026/11/16/business/united-airlines-outage-flights.html](https://www.nytimes.com/2026/11/16/business/united-airlines-outage-flights.html)

生成摘要时出错

---

## 64. What's Next for Nvidia?

**原文标题**: What's Next for Nvidia?

**原文链接**: [https://steveblank.com/2026/11/15/whats-next-for-nvidia/](https://steveblank.com/2026/11/15/whats-next-for-nvidia/)

生成摘要时出错

---

## 65. SpaceX catches the Starship to end Flight 15

**原文标题**: SpaceX catches the Starship to end Flight 15

**原文链接**: [https://www.spacex.com/launches/starship-flight-15](https://www.spacex.com/launches/starship-flight-15)

生成摘要时出错

---

## 66. Qwen4-Max

**原文标题**: Qwen4-Max

**原文链接**: [https://qwen.ai/blog?id=qwen4-max](https://qwen.ai/blog?id=qwen4-max)

生成摘要时出错

---

## 67. FBI says Artex AI open-source hacking tool used to breach networks

**原文标题**: FBI says Artex AI open-source hacking tool used to breach networks

**原文链接**: [https://techcrunch.com/2026/11/16/fbi-says-artex-ai-open-source-hacking-tool-used-to-breach-networks-in-under-three-hours/](https://techcrunch.com/2026/11/16/fbi-says-artex-ai-open-source-hacking-tool-used-to-breach-networks-in-under-three-hours/)

生成摘要时出错

---

## 68. Old Bitly links are being hijacked

**原文标题**: Old Bitly links are being hijacked

**原文链接**: [https://ransomnews.com/burger-king-tweet-bitly-link-hijack-2026/](https://ransomnews.com/burger-king-tweet-bitly-link-hijack-2026/)

生成摘要时出错

---

## 69. Making Atuin sync 32x faster with packfiles

**原文标题**: Making Atuin sync 32x faster with packfiles

**原文链接**: [https://blog.atuin.sh/making-atuin-sync-32x-faster-with-packfiles/](https://blog.atuin.sh/making-atuin-sync-32x-faster-with-packfiles/)

生成摘要时出错

---

## 70. Some OLED MacBook Pro Owners Report Eye Strain and Dizziness

**原文标题**: Some OLED MacBook Pro Owners Report Eye Strain and Dizziness

**原文链接**: [https://www.macrumors.com/2026/11/16/oled-macbook-pro-owners-report-eye-strain/](https://www.macrumors.com/2026/11/16/oled-macbook-pro-owners-report-eye-strain/)

生成摘要时出错

---

## 71. The Opportunivore's Dilemma

**原文标题**: The Opportunivore's Dilemma

**原文链接**: [https://www.vqronline.org/essays/opportunivores-dilemma](https://www.vqronline.org/essays/opportunivores-dilemma)

生成摘要时出错

---

## 72. SignuDoc: Open-source document signature platform

**原文标题**: SignuDoc: Open-source document signature platform

**原文链接**: [https://github.com/NYLLON-SOFTWARE/signudoc](https://github.com/NYLLON-SOFTWARE/signudoc)

生成摘要时出错

---

## 73. Artificial Intelligence for the Z80

**原文标题**: Artificial Intelligence for the Z80

**原文链接**: [https://www.dfsantos.com/en/libro-ia-z80](https://www.dfsantos.com/en/libro-ia-z80)

生成摘要时出错

---

## 74. Protomaps: Self-hosting map tiles has gotten cheap and easy

**原文标题**: Protomaps: Self-hosting map tiles has gotten cheap and easy

**原文链接**: [https://bruceroettgers.eu/blog/protomaps/](https://bruceroettgers.eu/blog/protomaps/)

生成摘要时出错

---

## 75. What is w2rt6byl5nf1opmc-a.com?

**原文标题**: What is w2rt6byl5nf1opmc-a.com?

**原文链接**: [https://jack.cab/blog/siterate](https://jack.cab/blog/siterate)

生成摘要时出错

---

## 76. Simple 8085 Computer

**原文标题**: Simple 8085 Computer

**原文链接**: [https://www.hackster.io/mit41301/simple-8085-computer-9fe156](https://www.hackster.io/mit41301/simple-8085-computer-9fe156)

生成摘要时出错

---

## 77. United Airlines experiencing 'widespread system outage'

**原文标题**: United Airlines experiencing 'widespread system outage'

**原文链接**: [https://www.nbcchicago.com/news/local/united-airlines-experiencing-widespread-system-outage/4017556/](https://www.nbcchicago.com/news/local/united-airlines-experiencing-widespread-system-outage/4017556/)

生成摘要时出错

---

## 78. Microsoft 365 outage leads to chlorine gas poisoning of 15 hotel guests

**原文标题**: Microsoft 365 outage leads to chlorine gas poisoning of 15 hotel guests

**原文链接**: [https://www1.wdr.de/nrw/rheinland/rhein-erft-kreis/technischer-defekt-chlor-phantasialand-100.html](https://www1.wdr.de/nrw/rheinland/rhein-erft-kreis/technischer-defekt-chlor-phantasialand-100.html)

生成摘要时出错

---

## 79. Handwriting, as a Font

**原文标题**: Handwriting, as a Font

**原文链接**: [https://ductus.sorenblank.com](https://ductus.sorenblank.com)

生成摘要时出错

---

## 80. Tor Project Issues Rapid-Response DoS-Defense Fix Amid Sustained DDoS Attack

**原文标题**: Tor Project Issues Rapid-Response DoS-Defense Fix Amid Sustained DDoS Attack

**原文链接**: [https://forum.torproject.org/t/security-release-0-4-9-17/22454](https://forum.torproject.org/t/security-release-0-4-9-17/22454)

生成摘要时出错

---

## 81. Eclipse Mosquitto – An open source MQTT broker

**原文标题**: Eclipse Mosquitto – An open source MQTT broker

**原文链接**: [https://github.com/eclipse-mosquitto/mosquitto](https://github.com/eclipse-mosquitto/mosquitto)

生成摘要时出错

---

## 82. Exact Gradients Through a BRep Kernel

**原文标题**: Exact Gradients Through a BRep Kernel

**原文链接**: [https://muni.works/research/vcad](https://muni.works/research/vcad)

生成摘要时出错

---

## 83. Skydio's asymmetrical F10 Lightrunner solves a problem with fixed-wing drones

**原文标题**: Skydio's asymmetrical F10 Lightrunner solves a problem with fixed-wing drones

**原文链接**: [https://spectrum.ieee.org/skydio-f10-lightrunner-asymmetrical-drone](https://spectrum.ieee.org/skydio-f10-lightrunner-asymmetrical-drone)

生成摘要时出错

---

## 84. Reports of AI-related child sexual abuse material rise 8,400% in two years

**原文标题**: Reports of AI-related child sexual abuse material rise 8,400% in two years

**原文链接**: [https://www.theguardian.com/technology/2026/nov/16/ai-related-child-sexual-abuse-material-rise-exploitation-deepfakes](https://www.theguardian.com/technology/2026/nov/16/ai-related-child-sexual-abuse-material-rise-exploitation-deepfakes)

生成摘要时出错

---

## 85. Show HN: ThingStudio, Node-RED style programming for microcontrollers

**原文标题**: Show HN: ThingStudio, Node-RED style programming for microcontrollers

**原文链接**: [https://thingstudio.net/](https://thingstudio.net/)

生成摘要时出错

---

## 86. C-like bit flags in Ruby

**原文标题**: C-like bit flags in Ruby

**原文链接**: [https://citizen428.net/blog/c-like-bit-flags-ruby/](https://citizen428.net/blog/c-like-bit-flags-ruby/)

生成摘要时出错

---

## 87. U.S. tightens controls on remote access to AI technology amid Nvidia fallout

**原文标题**: U.S. tightens controls on remote access to AI technology amid Nvidia fallout

**原文链接**: [https://www.npr.org/2026/11/16/nx-s1-6042883/nvidia-jensen-huang-commerce-department](https://www.npr.org/2026/11/16/nx-s1-6042883/nvidia-jensen-huang-commerce-department)

生成摘要时出错

---

## 88. Mini.nvim Is Now on Tangled

**原文标题**: Mini.nvim Is Now on Tangled

**原文链接**: [https://tangled.org/nvim-mini.org/mini.nvim](https://tangled.org/nvim-mini.org/mini.nvim)

生成摘要时出错

---

## 89. Atomic Nuked Veteran

**原文标题**: Atomic Nuked Veteran

**原文链接**: [https://www.armscontrolwonk.com/archive/201309/atomic-nuked-veteran/](https://www.armscontrolwonk.com/archive/201309/atomic-nuked-veteran/)

生成摘要时出错

---

## 90. No matter how you ask, more Americans are negative than positive about AI

**原文标题**: No matter how you ask, more Americans are negative than positive about AI

**原文链接**: [https://ourworldindata.org/no-matter-how-you-ask-more-americans-are-negative-than-positive-about-ai](https://ourworldindata.org/no-matter-how-you-ask-more-americans-are-negative-than-positive-about-ai)

生成摘要时出错

---

## 91. The MacBook Pro's OLED PWM problem

**原文标题**: The MacBook Pro's OLED PWM problem

**原文链接**: [https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/](https://macanorak.com/the-macbook-pros-oled-pwm-problem-when-a-better-display-becomes-worse-to-use/)

生成摘要时出错

---

## 92. Giant Roadside Attractions Face Mounting Costs and an Uncertain Future

**原文标题**: Giant Roadside Attractions Face Mounting Costs and an Uncertain Future

**原文链接**: [https://www.nytimes.com/2026/11/08/world/canada/roadside-attractions-giant-dinosaur.html](https://www.nytimes.com/2026/11/08/world/canada/roadside-attractions-giant-dinosaur.html)

生成摘要时出错

---

## 93. Lovable apps expose passport details and more than 200K private messages

**原文标题**: Lovable apps expose passport details and more than 200K private messages

**原文链接**: [https://www.crissyfield.de/research/lovable-en/](https://www.crissyfield.de/research/lovable-en/)

生成摘要时出错

---

## 94. Clice v1.0 Released: Welcome to Modern C++

**原文标题**: Clice v1.0 Released: Welcome to Modern C++

**原文链接**: [https://ykiko.me/en/articles/2105384023094834022/](https://ykiko.me/en/articles/2105384023094834022/)

生成摘要时出错

---

## 95. Claude Code and Codex reverse engineered my 1994 Jeep's ECU over a $3 Arduino [video]

**原文标题**: Claude Code and Codex reverse engineered my 1994 Jeep's ECU over a $3 Arduino [video]

**原文链接**: [https://www.youtube.com/watch?v=WPj3aQ-xxpI](https://www.youtube.com/watch?v=WPj3aQ-xxpI)

生成摘要时出错

---

## 96. Parcel: A desktop mail client for Linux, built with Zig

**原文标题**: Parcel: A desktop mail client for Linux, built with Zig

**原文链接**: [https://tangled.org/rockorager.dev/parcel](https://tangled.org/rockorager.dev/parcel)

生成摘要时出错

---

## 97. Notes on Mathematics for Engineers (1959) [pdf]

**原文标题**: Notes on Mathematics for Engineers (1959) [pdf]

**原文链接**: [https://websites.umich.edu/~ners311/CourseLibrary/MathNotes.pdf](https://websites.umich.edu/~ners311/CourseLibrary/MathNotes.pdf)

生成摘要时出错

---

## 98. Chinese frontier AI models carry the fingerprint of export-controlled GPUs

**原文标题**: Chinese frontier AI models carry the fingerprint of export-controlled GPUs

**原文链接**: [https://unemploymentlabs.com/checkpoint-forensics](https://unemploymentlabs.com/checkpoint-forensics)

生成摘要时出错

---

## 99. A NES emulator written in Odin

**原文标题**: A NES emulator written in Odin

**原文链接**: [https://lucypero.com/lucynes.html](https://lucypero.com/lucynes.html)

生成摘要时出错

---

## 100. Show HN: Deslop skill based on corpus-linguistics and psycholinguistics research

**原文标题**: Show HN: Deslop skill based on corpus-linguistics and psycholinguistics research

**原文链接**: [https://github.com/etodanik/deslop](https://github.com/etodanik/deslop)

生成摘要时出错

---

