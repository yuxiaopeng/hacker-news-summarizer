# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-17.md)

*最后自动更新时间: 2026-11-17 01:06:18*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-17](output/hacker_news_summary_2026-11-17.md) |
| 2 | [2026-11-11](output/hacker_news_summary_2026-11-11.md) |
| 3 | [2026-11-14](output/hacker_news_summary_2026-11-14.md) |
| 4 | [2026-11-12](output/hacker_news_summary_2026-11-12.md) |
| 5 | [2026-11-13](output/hacker_news_summary_2026-11-13.md) |
| 6 | [2026-11-15](output/hacker_news_summary_2026-11-15.md) |
| 7 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 8 | [2026-11-06](output/hacker_news_summary_2026-11-06.md) |
| 9 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 10 | [2026-11-08](output/hacker_news_summary_2026-11-08.md) |
| 11 | [2026-11-07](output/hacker_news_summary_2026-11-07.md) |
| 12 | [2026-11-10](output/hacker_news_summary_2026-11-10.md) |
| 13 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 14 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 15 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 16 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 17 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 18 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 19 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 20 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 21 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 22 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 23 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 24 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 25 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 26 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 27 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 28 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 29 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 30 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 31 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 32 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 33 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 34 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 35 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 36 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 37 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 38 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 39 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 40 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 41 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 42 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 43 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 44 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 45 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 46 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 47 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 48 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 49 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 50 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 51 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 52 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 53 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 54 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 55 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 56 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 57 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 58 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 59 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 60 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 61 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 62 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 63 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 64 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 65 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 66 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 67 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 68 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 69 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 70 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 71 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 72 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 73 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 74 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 75 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 76 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 77 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 78 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 79 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 80 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 81 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 82 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 83 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 84 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 85 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 86 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 87 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 88 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 89 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 90 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 91 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 92 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 93 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 94 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 95 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 96 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 97 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 98 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 99 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 100 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 101 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 102 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 103 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 104 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 105 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 106 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 107 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 108 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 109 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 110 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 111 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 112 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 113 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 114 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 115 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 116 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 117 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 118 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 119 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 120 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 121 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 122 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 123 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 124 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 125 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 126 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 127 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 128 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 129 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 130 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 131 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 132 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 133 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 134 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 135 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 136 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 137 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 138 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 139 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 140 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 141 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 142 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 143 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 144 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 145 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 146 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 147 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 148 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 149 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 150 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 151 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 152 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 153 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 154 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 155 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 156 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 157 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 158 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 159 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 160 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 161 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 162 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 163 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 164 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 165 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 166 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 167 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 168 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 169 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 170 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 171 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 172 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 173 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 174 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 175 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 176 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 177 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 178 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 179 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 180 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 181 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 182 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 183 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 184 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 185 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 186 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 187 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 188 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 189 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 190 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 191 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 192 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 193 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 194 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 195 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 196 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 197 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 198 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 199 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 200 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 201 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 202 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 203 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 204 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 205 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 206 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 207 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 208 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 209 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 210 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 211 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 212 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 213 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 214 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 215 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 216 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 217 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 218 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 219 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 220 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 221 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 222 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 223 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 224 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 225 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 226 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 227 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 228 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 229 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 230 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 231 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 232 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 233 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 234 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 235 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 236 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 237 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 238 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 239 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 240 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 241 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 242 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 243 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 244 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 245 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 246 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 247 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 248 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 249 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 250 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 251 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 252 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 253 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 254 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 255 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 256 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 257 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 258 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 259 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 260 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 261 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 262 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 263 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 264 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 265 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 266 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 267 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 268 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 269 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 270 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 271 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 272 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 273 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 274 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 275 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 276 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 277 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 278 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 279 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 280 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 281 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 282 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 283 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 284 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 285 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 286 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 287 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 288 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 289 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 290 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 291 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 292 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 293 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 294 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 295 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 296 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 297 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 298 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 299 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 300 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 301 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 302 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 303 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 304 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 305 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 306 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 307 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 308 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 309 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 310 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 311 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 312 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 313 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 314 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 315 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 316 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 317 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 318 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 319 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 320 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 321 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 322 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 323 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 324 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 325 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 326 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 327 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 328 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 329 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 330 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 331 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 332 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 333 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 334 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 335 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 336 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 337 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 338 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 339 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 340 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 341 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 342 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 343 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 344 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 345 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 346 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 347 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 348 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 349 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 350 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 351 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 352 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 353 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 354 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 355 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 356 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 357 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 358 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 359 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 360 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 361 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 362 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 363 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 364 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 365 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 366 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 367 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 368 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 369 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 370 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 371 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 372 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 373 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 374 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 375 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 376 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 377 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 378 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 379 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 380 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 381 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 382 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 383 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 384 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 385 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 386 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 387 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 388 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 389 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 390 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 391 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 392 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 393 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 394 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 395 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 396 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 397 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 398 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 399 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 400 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 401 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 402 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 403 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 404 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 405 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 406 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 407 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 408 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 409 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 410 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 411 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 412 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 413 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 414 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 415 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 416 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 417 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 418 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 419 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 420 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 421 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 422 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 423 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 424 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 425 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 426 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 427 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 428 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 429 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 430 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 431 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 432 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 433 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 434 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 435 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 436 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 437 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 438 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 439 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 440 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 441 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 442 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 443 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 444 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 445 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 446 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 447 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 448 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 449 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 450 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 451 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 452 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 453 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 454 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 455 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 456 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 457 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 458 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 459 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 460 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 461 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 462 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 463 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 464 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 465 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 466 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 467 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 468 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 469 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 470 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 471 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 472 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 473 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 474 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 475 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 476 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 477 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 478 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 479 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 480 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 481 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 482 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 483 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 484 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 485 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 486 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 487 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 488 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 489 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 490 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 491 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 492 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 493 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 494 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 495 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 496 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 497 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 498 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 499 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 500 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 501 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 502 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 503 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 504 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 505 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 506 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 507 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 508 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 509 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 510 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 511 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 512 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 513 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 514 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 515 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 516 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 517 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 518 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 519 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 520 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 521 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 522 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 523 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 524 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 525 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 526 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 527 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 528 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 529 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 530 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 531 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 532 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 533 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 534 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 535 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 536 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 537 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 538 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 539 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 540 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 541 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 542 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 543 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 544 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 545 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 546 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 547 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 548 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 549 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 550 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 551 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 552 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 553 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 554 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 555 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 556 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 557 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 558 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 559 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 560 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 561 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 562 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 563 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 564 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 565 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 566 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 567 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 568 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 569 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 570 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 571 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 572 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 573 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 574 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 575 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 576 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 577 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 578 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 579 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 580 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 581 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 582 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 583 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 584 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 585 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 586 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 587 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 588 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 589 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 590 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 591 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 592 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 593 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 594 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 595 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 596 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 597 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 598 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 599 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 600 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 601 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 602 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
