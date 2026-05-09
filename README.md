# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-09.md)

*最后自动更新时间: 2026-05-09 18:18:04*
## 1. 瑞士互联网档案馆

**原文标题**: Internet Archive Switzerland

**原文链接**: [https://internetarchive.ch/](https://internetarchive.ch/)

瑞士互联网档案馆 (IAS) 是一家总部位于圣加仑的独立非营利基金会，致力于实现“普及所有知识”的使命。IAS 意识到，由于文件格式更迭、介质失效以及付费墙的影响，数字信息表现出惊人的脆弱性，因此基金会专注于为研究和教育目的长期保存数字材料。

该基金会设立了两项旗舰计划：
*   **生成式人工智能档案馆 (Gen AI Archive)：** 该项目与圣加仑大学合作，旨在通过为后代保存当前的 AI 模型和大型语言模型 (LLM)，记录人工智能的演变历程。
*   **濒危档案馆 (Endangered Archives)：** 该倡议与联合国教科文组织及其他国际组织合作，旨在抢救并数字化那些因冲突、自然灾害或压制而面临风险的脆弱文化遗产和历史记录。

在执行董事 Roman Griesfelder 的领导下，IAS 的使命与全球互联网档案馆网络（包括加拿大和欧洲的分支机构）保持一致。基金会选址于圣加仑具有象征意义，其灵感汲取自该市圣加仑修道院档案馆长达千年的档案传统。

该基金会将于 2026 年 5 月正式启动，目前正积极寻求与研究人员、图书馆及开发者的合作，以守护集体记忆，并确保数字信息作为公共利益供大众获取。

---

## 2. cPanel 的黑色星期：4.4 万台服务器遭攻击后修复 3 个新漏洞

**原文标题**: CPanel's Black Week: 3 New Vulnerabilities Patched After Attack on 44k Servers

**原文链接**: [https://www.copahost.com/blog/cpanels-black-week-three-new-vulnerabilities-patched-after-ransomware-attack-on-44000-servers/](https://www.copahost.com/blog/cpanels-black-week-three-new-vulnerabilities-patched-after-ransomware-attack-on-44000-servers/)

在导致超过 44,000 台服务器沦陷的大规模勒索软件攻击后，cPanel 在十天内发布了第二次紧急技术安全发布 (TSR)。本次补丁解决了在初始危机引发的深度代码审计中发现的三个新漏洞：CVE-2026-29201、CVE-2026-29202 和 CVE-2026-29203。

**新漏洞详情：**
三个漏洞中有两个被评为**高危（CVSS 8.8）**：
*   **CVE-2026-29202：** 允许通过 `create_user` API 执行任意 Perl 代码。这对共享主机环境尤为危险，因为任何经过身份验证的用户都可能执行系统级代码。
*   **CVE-2026-29203：** 涉及不安全的符号链接处理，允许攻击者通过修改文件权限（通过 `chmod`）来提升权限或导致拒绝服务。
*   **CVE-2026-29201 (CVSS 4.3)：** 中危漏洞，允许读取任意文件，可被用于窃取凭据或配置数据。

**背景与紧迫性：**
在此次披露之前，4 月下旬曾发生过 CVE-2026-41940 漏洞被利用的事件，该漏洞是一个严重的身份验证绕过漏洞，黑客曾利用它部署“Sorry”勒索软件。由于该漏洞自 2026 年 2 月起就被作为零日漏洞利用，安全专家警告称，受 AI 辅助研究的影响，补丁修复的窗口期正在迅速缩小。

**建议措施：**
管理员应立即运行 `/scripts/upcp`，重启 `cpsrvd` 服务并验证其版本。此外，鉴于此前数月的漏洞利用情况，应对服务器进行取证审计，检查追溯至 2026 年 2 月 23 日的异常日志，并扫描带有 `.sorry` 扩展名的文件。文章强调，启用自动更新现已成为维护服务器完整性的关键必要条件。

---

## 3. Acorn Archimedes 上的 PipeDream

**原文标题**: PipeDream on the Acorn Archimedes

**原文链接**: [https://stonetools.ghost.io/pipedream-archimedes/](https://stonetools.ghost.io/pipedream-archimedes/)

本文探讨了 Acorn Archimedes 独特且充满实验性质的计算生态系统。这一来自英国的系统将革命性的硬件、风格独特的操作系统以及一套跨越边界的办公套件结合在了一起。

**硬件与操作系统**
Archimedes 搭载了由 Acorn 自主研发的 ARM（Acorn RISC Machine）处理器，这是在 Acorn 发现当时的 16 位芯片性能不足后开发的。虽然 Archimedes 未能统治家庭电脑市场，但 ARM 架构却实现了全球性的长久影响力，最终驱动了现代智能手机行业和苹果的硬件生态系统。

该硬件运行的是 RISC OS（最初名为“Arthur”），这是一种采用“WIMP”界面的协作式多任务系统。作者将该系统描述为“令人迷茫”且“反常规”的，并强调了其独特的三键鼠标系统——选择（Select）、菜单（Menu）和调整（Adjust），以及传统菜单栏的缺失。其显著特征包括中央应用程序“停靠栏”（dock），以及强制性的文件管理拖拽交互机制，即用户必须将文档图标物理拖动到文件夹中才能完成保存。

**PipeDream**
软件体验的核心是由 Mark Colton 开发的 PipeDream。PipeDream 建立在一种“大统一理论”之上，即文字处理器、电子表格和数据库之间的界限是人为划分的。PipeDream 并没有采用相互独立的应用程序，而是使用了一种基于有序单元格矩阵的单一文档格式。

在这种模式下，一份文字处理文档本质上就是一个电子表格，每一行都作为一行文本，并在特定标记处折行。这使得用户能够在单一界面内整合强大的数学函数、数据库记录和长篇文本。

**结论**
尽管作者认为该系统的学习曲线陡峭且界面“令人不适”，但文章仍将 Archimedes 和 PipeDream 描绘成一个迷人的“计算演化死胡同”——尽管它未能延续，但却提供了一种极具远见且集成化的办公生产力方案。

---

## 4. The Intolerable Hypocrisy of Cyberlibertarianism

**原文标题**: The Intolerable Hypocrisy of Cyberlibertarianism

**原文链接**: [https://matduggan.com/the-intolerable-hypocrisy-of-cyberlibertarianism/](https://matduggan.com/the-intolerable-hypocrisy-of-cyberlibertarianism/)

In "The Intolerable Hypocrisy of Cyberlibertarianism," the author argues that the modern internet is built upon a flawed ideological foundation that prioritizes corporate power under the guise of individual freedom. While acknowledging the internet’s practical benefits, the author traces its systemic issues back to the 1990s and the rise of "cyberlibertarianism."

The article highlights foundational documents like John Perry Barlow’s 1996 "Declaration of the Independence of Cyberspace" and the "Magna Carta for the Knowledge Age." These texts championed a digital realm immune to government sovereignty and regulation, framing any oversight as an obsolete burden on innovation.

Drawing on the 1997 critiques of scholar Langdon Winner, the author outlines the four pillars of this ideology:
1.  **Technological Determinism:** The belief that rapid tech acceleration is an unstoppable natural force.
2.  **Radical Individualism:** The rejection of social and regulatory obligations in favor of personal liberation.
3.  **Free-Market Absolutism:** The insistence that deregulated markets will solve all social ills.
4.  **Utopian Fantasies:** The "insane" claim that radical egoism and corporate deregulation would naturally produce a harmonious, decentralized community.

Winner’s most vital observation was the "trick" at the heart of this movement: the conflation of individual liberty with the interests of massive, profit-seeking corporations. By rebranding "private ownership" as "ownership by the people," cyberlibertarians provided a moral shield for monopolies.

Ultimately, the author asserts that the promises of cyberlibertarianism were lies. Instead of a decentralized utopia, the movement delivered a system where tech giants reap massive profits while offloading the "consequences, harms, and costs" of their platforms onto the public. Decades later, the industry continues to evade the essential question of whether this is the society we actually want to foster.

---

## 5. 当你委派任务时，LLM 会损坏你的文档

**原文标题**: LLMs Corrupt Your Documents When You Delegate

**原文链接**: [https://arxiv.org/abs/2604.15597](https://arxiv.org/abs/2604.15597)

论文《当你委派任务时，大语言模型（LLM）会损坏你的文档》（2026年4月）探讨了与“委派”（delegation）相关的风险——即用户信任 AI 自主执行复杂、多步骤任务的模式。为评估这一风险，作者引入了 DELEGATE-52 基准测试，模拟涵盖晶体学、编程和乐谱等52个专业领域的长期文档编辑任务。

该研究测试了19个大语言模型，包括 GPT 5.4、Claude 4.6 Opus 和 Gemini 3.1 Pro 等前沿模型。研究结果揭示了显著的可靠性差距：在长期工作流结束时，即使是这些顶级模型平均也会导致 25% 的文档内容损坏。其他模型的表现则更差。

研究的核心观点包括：
* **隐蔽式损坏：** LLM 引入的错误虽然稀疏但极其严重，最初难以察觉，却会随时间推移而累积。
* **缓解措施失效：** 使用智能体工具（agentic tools）并未改善模型在 DELEGATE-52 基准测试中的表现。
* **风险因素：** 文档体积增加、交互链延长以及干扰文件的存在会显著加剧文档退化。

作者总结认为，目前的 LLM 是“不可靠的受托人”。尽管其市场定位是提高生产力，但由于它们会静默破坏专业文档的完整性，这为实现自主工作流构成了重大障碍。研究指出，在这些累积错误得到解决之前，委派任务给 LLM 仍需严密的人工监督，以防止文档被彻底损坏。

---

## 6. 谷歌导致去谷歌化安卓用户的 reCAPTCHA 失效。

**原文标题**: Google broke reCAPTCHA for de-googled Android users

**原文链接**: [https://reclaimthenet.org/google-broke-recaptcha-for-de-googled-android-users](https://reclaimthenet.org/google-broke-recaptcha-for-de-googled-android-users)

根据提供的标题和内容，以下是该情况的简要总结：

**摘要：谷歌安全机制与注重隐私的安卓用户之间的摩擦**

谷歌最近更新了其 **reCAPTCHA** 系统，这一举动实际上切断了“去谷歌化”安卓用户的网站访问路径。该问题主要影响使用 GrapheneOS 或 LineageOS 等以隐私为中心的操作系统的人群，这些系统特意去除了专有的谷歌服务框架（Google Play Services）。

**关键点：**
*   **冲突点：** 谷歌最新的 reCAPTCHA 版本日益依赖 **Play Integrity API**（前身为 SafetyNet）。该 API 用于检测设备是否经过谷歌“认证”。由于去谷歌化的设备缺少这些专有接口，或者因其定制特性而无法通过“完整性”检查，它们常被标记为机器人或可疑流量。
*   **对用户的影响：** 这一变化实质上将注重隐私的用户拒于大部分互联网门外，迫使他们在数字自主权与通过标准安全检查的能力之间做出选择。
*   **Brave 的“精简版”选项：** 为了响应隐私社区的不同需求，Brave 推出了一个“精简版”选项。该工具旨在为不同“等级”的隐私用户提供更一致的用户体验。
*   **受众关注：** 是否需要这些新工具取决于用户的具体“威胁模型”。虽然普通用户可能不会察觉到这种转变，但那些避开谷歌生态系统的“硬核”隐私倡导者，现在正面临着一个对非标准、去谷歌化配置日益不友好的网络环境。

归根结底，这种情况凸显了科技生态系统中日益扩大的分歧：谷歌激进的反机器人措施在成功过滤自动化流量的同时，也造成了“附带损害”——排斥了那些将数据隐私置于谷歌集成之上的合法用户。

---

## 7. 使用 Claude Code：HTML 的非凡效能

**原文标题**: Using Claude Code: The unreasonable effectiveness of HTML

**原文链接**: [https://twitter.com/trq212/status/2052809885763747935](https://twitter.com/trq212/status/2052809885763747935)

您提供的内容并不包含文章正文，而是来自 **X（原 Twitter）** 的一条技术错误信息，提示您的浏览器禁用了 JavaScript。

不过，根据您提供的标题（**“使用 Claude Code：HTML 超乎寻常的有效性”**），以下是该标题在技术社区中所指代内容的简要总结：

### 总结：Claude Code 中 HTML 超乎寻常的有效性

该标题涉及关于 **Claude Code**（Anthropic 开发的 AI 驱动型命令行编程工具）的一项技术洞察。其核心观点是：与计算机视觉或 JSON API 等更复杂的方法相比，原始 HTML 是大语言模型（LLM）理解网页并与其交互的一种意想不到的优越格式。

**关键点：**
*   **语义丰富性：** HTML 提供了网页的结构化、层级化地图。`<button>`、`<form>` 和 `<a>` 等标签为 AI 提供了即时的功能上下文，而这些信息在视觉截图中往往会丢失。
*   **Token 效率：** 视觉模型需要处理海量的“像素”数据，而 Claude 可以快速解析基于文本的 DOM（文档对象模型），使其能在上下文窗口内更高效地“看到”界面。
*   **可靠的导航：** 通过专注于 HTML 结构，Claude Code 能够以远高于尝试猜测屏幕坐标的模型的精度来识别页面元素并与其交互（例如点击特定的 ID 或类名）。
*   **化繁为简：** 这种“超乎寻常的有效性”在于，一个已有 30 年历史的标记语言，仍然是现代人工智能对以人为本的 Web 界面进行推理和自动化操作最有效的方式。

*(注：如果您有特定文章的全文并希望进行更深入的分析，请粘贴实际内容，而非网页错误信息。)*

---

## 8. How LEDs are made (2014)

**原文标题**: How LEDs are made (2014)

**原文链接**: [https://learn.sparkfun.com/tutorials/how-leds-are-made/all](https://learn.sparkfun.com/tutorials/how-leds-are-made/all)

生成摘要时出错

---

## 9. A recent experience with ChatGPT 5.5 Pro

**原文标题**: A recent experience with ChatGPT 5.5 Pro

**原文链接**: [https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/](https://gowers.wordpress.com/2026/05/08/a-recent-experience-with-chatgpt-5-5-pro/)

生成摘要时出错

---

## 10. Mythical Man Month

**原文标题**: Mythical Man Month

**原文链接**: [https://martinfowler.com/bliki/MythicalManMonth.html](https://martinfowler.com/bliki/MythicalManMonth.html)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 2 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 3 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 4 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 5 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 6 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 7 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 8 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 9 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 10 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 11 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 12 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 13 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 14 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 15 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 16 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 17 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 18 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 19 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 20 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 21 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 22 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 23 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 24 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 25 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 26 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 27 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 28 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 29 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 30 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 31 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 32 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 33 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 34 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 35 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 36 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 37 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 38 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 39 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 40 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 41 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 42 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 43 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 44 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 45 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 46 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 47 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 48 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 49 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 50 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 51 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 52 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 53 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 54 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 55 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 56 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 57 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 58 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 59 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 60 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 61 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 62 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 63 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 64 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 65 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 66 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 67 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 68 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 69 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 70 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 71 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 72 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 73 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 74 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 75 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 76 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 77 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 78 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 79 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 80 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 81 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 82 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 83 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 84 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 85 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 86 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 87 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 88 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 89 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 90 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 91 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 92 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 93 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 94 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 95 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 96 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 97 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 98 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 99 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 100 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 101 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 102 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 103 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 104 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 105 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 106 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 107 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 108 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 109 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 110 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 111 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 112 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 113 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 114 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 115 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 116 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 117 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 118 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 119 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 120 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 121 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 122 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 123 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 124 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 125 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 126 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 127 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 128 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 129 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 130 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 131 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 132 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 133 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 134 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 135 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 136 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 137 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 138 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 139 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 140 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 141 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 142 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 143 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 144 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 145 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 146 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 147 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 148 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 149 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 150 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 151 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 152 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 153 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 154 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 155 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 156 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 157 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 158 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 159 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 160 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 161 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 162 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 163 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 164 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 165 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 166 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 167 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 168 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 169 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 170 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 171 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 172 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 173 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 174 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 175 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 176 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 177 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 178 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 179 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 180 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 181 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 182 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 183 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 184 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 185 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 186 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 187 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 188 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 189 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 190 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 191 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 192 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 193 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 194 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 195 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 196 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 197 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 198 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 199 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 200 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 201 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 202 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 203 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 204 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 205 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 206 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 207 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 208 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 209 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 210 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 211 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 212 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 213 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 214 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 215 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 216 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 217 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 218 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 219 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 220 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 221 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 222 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 223 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 224 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 225 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 226 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 227 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 228 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 229 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 230 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 231 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 232 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 233 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 234 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 235 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 236 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 237 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 238 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 239 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 240 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 241 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 242 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 243 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 244 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 245 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 246 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 247 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 248 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 249 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 250 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 251 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 252 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 253 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 254 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 255 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 256 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 257 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 258 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 259 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 260 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 261 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 262 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 263 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 264 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 265 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 266 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 267 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 268 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 269 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 270 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 271 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 272 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 273 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 274 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 275 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 276 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 277 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 278 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 279 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 280 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 281 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 282 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 283 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 284 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 285 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 286 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 287 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 288 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 289 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 290 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 291 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 292 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 293 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 294 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 295 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 296 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 297 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 298 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 299 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 300 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 301 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 302 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 303 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 304 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 305 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 306 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 307 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 308 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 309 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 310 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 311 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 312 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 313 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 314 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 315 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 316 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 317 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 318 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 319 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 320 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 321 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 322 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 323 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 324 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 325 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 326 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 327 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 328 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 329 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 330 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 331 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 332 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 333 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 334 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 335 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 336 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 337 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 338 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 339 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 340 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 341 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 342 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 343 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 344 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 345 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 346 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 347 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 348 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 349 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 350 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 351 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 352 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 353 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 354 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 355 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 356 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 357 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 358 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 359 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 360 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 361 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 362 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 363 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 364 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 365 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 366 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 367 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 368 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 369 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 370 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 371 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 372 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 373 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 374 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 375 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 376 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 377 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 378 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 379 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 380 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 381 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 382 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 383 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 384 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 385 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 386 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 387 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 388 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 389 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 390 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 391 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 392 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 393 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 394 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 395 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 396 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 397 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 398 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 399 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 400 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 401 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 402 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 403 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 404 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 405 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 406 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 407 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 408 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 409 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 410 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 411 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 412 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 413 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 414 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 415 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
