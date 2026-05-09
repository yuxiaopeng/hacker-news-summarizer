# Hacker News 热门文章摘要 (2026-05-09)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. America's carpet capital: an empire and its toxic legacy

**原文标题**: America's carpet capital: an empire and its toxic legacy

**原文链接**: [https://apnews.com/projects/pfas-forever-stained/](https://apnews.com/projects/pfas-forever-stained/)

生成摘要时出错

---

## 12. OpenAI’s WebRTC problem

**原文标题**: OpenAI’s WebRTC problem

**原文链接**: [https://moq.dev/blog/webrtc-is-the-problem/](https://moq.dev/blog/webrtc-is-the-problem/)

生成摘要时出错

---

## 13. GrapheneOS fixes Android VPN leak Google refused to patch

**原文标题**: GrapheneOS fixes Android VPN leak Google refused to patch

**原文链接**: [https://cyberinsider.com/grapheneos-fixes-android-vpn-leak-google-refused-to-patch/](https://cyberinsider.com/grapheneos-fixes-android-vpn-leak-google-refused-to-patch/)

生成摘要时出错

---

## 14. Introduction to Beaver Triples

**原文标题**: Introduction to Beaver Triples

**原文链接**: [https://stoffelmpc.com/stoffel-blog/beaver-triples-tuples](https://stoffelmpc.com/stoffel-blog/beaver-triples-tuples)

生成摘要时出错

---

## 15. Building the TD4 4-Bit CPU

**原文标题**: Building the TD4 4-Bit CPU

**原文链接**: [https://jayakody2000lk.blogspot.com/2026/05/building-td4-4-bit-cpu.html](https://jayakody2000lk.blogspot.com/2026/05/building-td4-4-bit-cpu.html)

生成摘要时出错

---

## 16. David Attenborough's 100th Birthday

**原文标题**: David Attenborough's 100th Birthday

**原文链接**: [https://www.bbc.com/news/articles/cp3pww9g0p5o](https://www.bbc.com/news/articles/cp3pww9g0p5o)

生成摘要时出错

---

## 17. Reviving the IBM Selectric Composer Fonts (2023)

**原文标题**: Reviving the IBM Selectric Composer Fonts (2023)

**原文链接**: [https://www.kutilek.de/selectric/](https://www.kutilek.de/selectric/)

生成摘要时出错

---

## 18. Show HN: I wrote a flight simulator in my own programming language

**原文标题**: Show HN: I wrote a flight simulator in my own programming language

**原文链接**: [https://github.com/navid-m/flightsim](https://github.com/navid-m/flightsim)

生成摘要时出错

---

## 19. What causes lightning? The answer keeps getting more interesting

**原文标题**: What causes lightning? The answer keeps getting more interesting

**原文链接**: [https://www.quantamagazine.org/what-causes-lightning-the-answer-keeps-getting-more-interesting-20260506/](https://www.quantamagazine.org/what-causes-lightning-the-answer-keeps-getting-more-interesting-20260506/)

生成摘要时出错

---

## 20. Show HN: Mochi.js: bun-native high-fidelity browser automation library

**原文标题**: Show HN: Mochi.js: bun-native high-fidelity browser automation library

**原文链接**: [https://mochijs.com/](https://mochijs.com/)

生成摘要时出错

---

## 21. Killswitch: Per-function short-circuit mitigation primitive

**原文标题**: Killswitch: Per-function short-circuit mitigation primitive

**原文链接**: [https://lwn.net/ml/all/20260507070547.2268452-1-sashal@kernel.org/](https://lwn.net/ml/all/20260507070547.2268452-1-sashal@kernel.org/)

生成摘要时出错

---

## 22. Making Julia as Fast as C++ (2019)

**原文标题**: Making Julia as Fast as C++ (2019)

**原文链接**: [https://flow.byu.edu/posts/julia-c++](https://flow.byu.edu/posts/julia-c++)

生成摘要时出错

---

## 23. Wi is Fi: Understanding Wi-Fi 4/5/6/6E/7/8 (802.11 n/AC/ax/be/bn)

**原文标题**: Wi is Fi: Understanding Wi-Fi 4/5/6/6E/7/8 (802.11 n/AC/ax/be/bn)

**原文链接**: [https://www.wiisfi.com/](https://www.wiisfi.com/)

生成摘要时出错

---

## 24. Show HN: Free tool to mark points and polygon regions

**原文标题**: Show HN: Free tool to mark points and polygon regions

**原文链接**: [https://tack.pics](https://tack.pics)

生成摘要时出错

---

## 25. Read Programming as Theory Building

**原文标题**: Read Programming as Theory Building

**原文链接**: [https://codeutopia.net/blog/2026/05/09/you-should-read-programming-as-theory-building/](https://codeutopia.net/blog/2026/05/09/you-should-read-programming-as-theory-building/)

生成摘要时出错

---

## 26. AI is breaking two vulnerability cultures

**原文标题**: AI is breaking two vulnerability cultures

**原文链接**: [https://www.jefftk.com/p/ai-is-breaking-two-vulnerability-cultures](https://www.jefftk.com/p/ai-is-breaking-two-vulnerability-cultures)

生成摘要时出错

---

## 27. Cartoon Network Flash Games

**原文标题**: Cartoon Network Flash Games

**原文链接**: [https://www.webdesignmuseum.org/flash-game-exhibitions/cartoon-network-flash-games](https://www.webdesignmuseum.org/flash-game-exhibitions/cartoon-network-flash-games)

生成摘要时出错

---

## 28. An Introduction to Meshtastic

**原文标题**: An Introduction to Meshtastic

**原文链接**: [https://meshtastic.org/docs/introduction/](https://meshtastic.org/docs/introduction/)

生成摘要时出错

---

## 29. The React2Shell Story

**原文标题**: The React2Shell Story

**原文链接**: [https://lachlan.nz/blog/the-react2shell-story/](https://lachlan.nz/blog/the-react2shell-story/)

生成摘要时出错

---

## 30. Removing fsync from our local storage engine

**原文标题**: Removing fsync from our local storage engine

**原文链接**: [https://fractalbits.com/blog/remove-fsync/](https://fractalbits.com/blog/remove-fsync/)

生成摘要时出错

---

## 31. The React2Shell Story

**原文标题**: The React2Shell Story

**原文链接**: [https://lachlan.nz/blog/the-react2shell-story/](https://lachlan.nz/blog/the-react2shell-story/)

生成摘要时出错

---

## 32. Teaching Claude Why

**原文标题**: Teaching Claude Why

**原文链接**: [https://www.anthropic.com/research/teaching-claude-why](https://www.anthropic.com/research/teaching-claude-why)

生成摘要时出错

---

## 33. The context window has been shattered: Subquadratic debuts a 12M token window

**原文标题**: The context window has been shattered: Subquadratic debuts a 12M token window

**原文链接**: [https://thenewstack.io/subquadratic-12-million-context-window/](https://thenewstack.io/subquadratic-12-million-context-window/)

生成摘要时出错

---

## 34. You gave me a u32. I gave you root. (io_uring ZCRX freelist LPE)

**原文标题**: You gave me a u32. I gave you root. (io_uring ZCRX freelist LPE)

**原文链接**: [https://ze3tar.github.io/post-zcrx.html](https://ze3tar.github.io/post-zcrx.html)

生成摘要时出错

---

## 35. A new hash table for Lwan

**原文标题**: A new hash table for Lwan

**原文链接**: [https://tia.mat.br/posts/2026/05/06/a-new-hash-table-for-lwan.html](https://tia.mat.br/posts/2026/05/06/a-new-hash-table-for-lwan.html)

生成摘要时出错

---

## 36. First, the FBI Searched Her Home. Then, She Won a Pulitzer.

**原文标题**: First, the FBI Searched Her Home. Then, She Won a Pulitzer.

**原文链接**: [https://www.nytimes.com/2026/05/05/business/media/hannah-natanson-washington-post-pulitzer.html](https://www.nytimes.com/2026/05/05/business/media/hannah-natanson-washington-post-pulitzer.html)

生成摘要时出错

---

## 37. Can LLMs model real-world systems in TLA+?

**原文标题**: Can LLMs model real-world systems in TLA+?

**原文链接**: [https://www.sigops.org/2026/can-llms-model-real-world-systems-in-tla/](https://www.sigops.org/2026/can-llms-model-real-world-systems-in-tla/)

生成摘要时出错

---

## 38. Serving a website on a Raspberry Pi Zero running in RAM

**原文标题**: Serving a website on a Raspberry Pi Zero running in RAM

**原文链接**: [https://btxx.org/posts/memory/](https://btxx.org/posts/memory/)

生成摘要时出错

---

## 39. Forking the Web

**原文标题**: Forking the Web

**原文链接**: [https://dillo-browser.org/lab/web-fork/](https://dillo-browser.org/lab/web-fork/)

生成摘要时出错

---

## 40. US Government releases first batch of UAP documents and videos

**原文标题**: US Government releases first batch of UAP documents and videos

**原文链接**: [https://www.war.gov/UFO/](https://www.war.gov/UFO/)

生成摘要时出错

---

## 41. Light without electricity? Glowing algae could make it possible

**原文标题**: Light without electricity? Glowing algae could make it possible

**原文链接**: [https://www.colorado.edu/today/2026/05/06/light-without-electricity-glowing-algae-could-make-it-possible](https://www.colorado.edu/today/2026/05/06/light-without-electricity-glowing-algae-could-make-it-possible)

生成摘要时出错

---

## 42. Mux (YC W16) Is Hiring

**原文标题**: Mux (YC W16) Is Hiring

**原文链接**: [https://www.mux.com/jobs](https://www.mux.com/jobs)

生成摘要时出错

---

## 43. CAD and Cam Applications on HP-UX Unix Workstations

**原文标题**: CAD and Cam Applications on HP-UX Unix Workstations

**原文链接**: [https://www.openpa.net/hp-ux_cad.html](https://www.openpa.net/hp-ux_cad.html)

生成摘要时出错

---

## 44. All means are fair except solving the problem

**原文标题**: All means are fair except solving the problem

**原文链接**: [https://yosefk.com/blog/all-means-are-fair-except-solving-the-problem.html](https://yosefk.com/blog/all-means-are-fair-except-solving-the-problem.html)

生成摘要时出错

---

## 45. The soul of maintaining a new machine

**原文标题**: The soul of maintaining a new machine

**原文链接**: [https://books.worksinprogress.co/book/maintenance-of-everything/communities-of-practice/the-soul-of-maintaining-a-new-machine/3](https://books.worksinprogress.co/book/maintenance-of-everything/communities-of-practice/the-soul-of-maintaining-a-new-machine/3)

生成摘要时出错

---

## 46. Roadside Attraction

**原文标题**: Roadside Attraction

**原文链接**: [https://theoffingmag.com/essay/roadside-attraction/](https://theoffingmag.com/essay/roadside-attraction/)

生成摘要时出错

---

## 47. Singapore introduces caning for boys who bully others at school

**原文标题**: Singapore introduces caning for boys who bully others at school

**原文链接**: [https://www.theguardian.com/world/2026/may/06/singapore-caning-school-bullies](https://www.theguardian.com/world/2026/may/06/singapore-caning-school-bullies)

生成摘要时出错

---

## 48. When is your birthday? The math behind hash collisions

**原文标题**: When is your birthday? The math behind hash collisions

**原文链接**: [https://0xkrt26.github.io/math_behind_security/2026/05/08/birthday-problem.html](https://0xkrt26.github.io/math_behind_security/2026/05/08/birthday-problem.html)

生成摘要时出错

---

## 49. Bitter Lessons from the ISSpresso

**原文标题**: Bitter Lessons from the ISSpresso

**原文链接**: [https://mceglowski.substack.com/p/bitter-lessons-from-the-isspresso](https://mceglowski.substack.com/p/bitter-lessons-from-the-isspresso)

生成摘要时出错

---

## 50. PortalVR Motion – use any VR content in 2D with 3D tracked Joy-Cons

**原文标题**: PortalVR Motion – use any VR content in 2D with 3D tracked Joy-Cons

**原文链接**: [https://portalvr.io/motion](https://portalvr.io/motion)

生成摘要时出错

---

## 51. Poland is now among the 20 largest economies

**原文标题**: Poland is now among the 20 largest economies

**原文链接**: [https://apnews.com/article/poland-economy-growth-g20-gdp-26fe06e120398410f8d773ba5661e7aa](https://apnews.com/article/poland-economy-growth-g20-gdp-26fe06e120398410f8d773ba5661e7aa)

生成摘要时出错

---

## 52. Cloudflare to cut about 20% of its workforce

**原文标题**: Cloudflare to cut about 20% of its workforce

**原文链接**: [https://www.reuters.com/business/world-at-work/cloudflare-cut-over-1100-jobs-2026-05-07/](https://www.reuters.com/business/world-at-work/cloudflare-cut-over-1100-jobs-2026-05-07/)

生成摘要时出错

---

## 53. Meta Shuts Down End-to-End Encryption for Instagram Messaging

**原文标题**: Meta Shuts Down End-to-End Encryption for Instagram Messaging

**原文链接**: [https://www.pcmag.com/news/meta-shuts-down-end-to-end-encryption-for-instagram-dms-messaging](https://www.pcmag.com/news/meta-shuts-down-end-to-end-encryption-for-instagram-dms-messaging)

生成摘要时出错

---

## 54. Apple Is Holding My Pictures Hostage Until I Accept Their New Terms of Service

**原文标题**: Apple Is Holding My Pictures Hostage Until I Accept Their New Terms of Service

**原文链接**: [https://probablydance.com/2026/05/01/apple-is-holding-my-pictures-hostage-until-i-accept-their-new-terms-of-service/](https://probablydance.com/2026/05/01/apple-is-holding-my-pictures-hostage-until-i-accept-their-new-terms-of-service/)

生成摘要时出错

---

## 55. The Disappearance of the Public Bench

**原文标题**: The Disappearance of the Public Bench

**原文链接**: [https://placesjournal.org/article/the-disappearance-of-the-public-bench/](https://placesjournal.org/article/the-disappearance-of-the-public-bench/)

生成摘要时出错

---

## 56. PC Engine CPU

**原文标题**: PC Engine CPU

**原文链接**: [https://jsgroth.dev/blog/posts/pc-engine-cpu/](https://jsgroth.dev/blog/posts/pc-engine-cpu/)

生成摘要时出错

---

## 57. Hardening Firefox with Claude Mythos Preview

**原文标题**: Hardening Firefox with Claude Mythos Preview

**原文链接**: [https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/)

生成摘要时出错

---

## 58. How do I deal with memory leaks? (2022)

**原文标题**: How do I deal with memory leaks? (2022)

**原文链接**: [https://www.stroustrup.com/bs_faq2.html#memory-leaks](https://www.stroustrup.com/bs_faq2.html#memory-leaks)

生成摘要时出错

---

## 59. GeoJSON

**原文标题**: GeoJSON

**原文链接**: [https://geojson.org/](https://geojson.org/)

生成摘要时出错

---

## 60. Canvas online again as ShinyHunters threatens to leak schools’ data

**原文标题**: Canvas online again as ShinyHunters threatens to leak schools’ data

**原文链接**: [https://www.theverge.com/tech/926458/canvas-shinyhunters-breach](https://www.theverge.com/tech/926458/canvas-shinyhunters-breach)

生成摘要时出错

---

## 61. ClojureScript Gets Async/Await

**原文标题**: ClojureScript Gets Async/Await

**原文链接**: [https://clojurescript.org/news/2026-05-07-release](https://clojurescript.org/news/2026-05-07-release)

生成摘要时出错

---

## 62. Podman rootless containers and the Copy Fail exploit

**原文标题**: Podman rootless containers and the Copy Fail exploit

**原文链接**: [https://garrido.io/notes/podman-rootless-containers-copy-fail/](https://garrido.io/notes/podman-rootless-containers-copy-fail/)

生成摘要时出错

---

## 63. Mojo 1.0 Beta

**原文标题**: Mojo 1.0 Beta

**原文链接**: [https://mojolang.org/](https://mojolang.org/)

生成摘要时出错

---

## 64. The surprisingly complex journey to text-selectable client-side generated PDFs

**原文标题**: The surprisingly complex journey to text-selectable client-side generated PDFs

**原文链接**: [https://sdocs.dev/blogs/journey-to-pdf-generation](https://sdocs.dev/blogs/journey-to-pdf-generation)

生成摘要时出错

---

## 65. EU calls VPNs "a loophole that needs closing" in age verification push

**原文标题**: EU calls VPNs "a loophole that needs closing" in age verification push

**原文链接**: [https://cyberinsider.com/eu-calls-vpns-a-loophole-that-needs-closing-in-age-verification-push/](https://cyberinsider.com/eu-calls-vpns-a-loophole-that-needs-closing-in-age-verification-push/)

生成摘要时出错

---

## 66. Maybe you shouldn't install new software for a bit

**原文标题**: Maybe you shouldn't install new software for a bit

**原文链接**: [https://xeiaso.net/blog/2026/abstain-from-install/](https://xeiaso.net/blog/2026/abstain-from-install/)

生成摘要时出错

---

## 67. GPT-5.5 Price Increase: What It Costs

**原文标题**: GPT-5.5 Price Increase: What It Costs

**原文链接**: [https://openrouter.ai/announcements/gpt55-cost-analysis](https://openrouter.ai/announcements/gpt55-cost-analysis)

生成摘要时出错

---

## 68. All my clients wanted a carousel, now it's an AI chatbot

**原文标题**: All my clients wanted a carousel, now it's an AI chatbot

**原文链接**: [https://adele.pages.casa/md/blog/all-my-clients-wanted-a-carousel-now-it-s-an-ai-chatbot.md](https://adele.pages.casa/md/blog/all-my-clients-wanted-a-carousel-now-it-s-an-ai-chatbot.md)

生成摘要时出错

---

## 69. Dirty Frag: Universal Linux LPE

**原文标题**: Dirty Frag: Universal Linux LPE

**原文链接**: [https://www.openwall.com/lists/oss-security/2026/05/07/8](https://www.openwall.com/lists/oss-security/2026/05/07/8)

生成摘要时出错

---

## 70. Aids Creeps Back in Parts of Zambia, a Year After U.S. Cuts to HIV Assistance

**原文标题**: Aids Creeps Back in Parts of Zambia, a Year After U.S. Cuts to HIV Assistance

**原文链接**: [https://www.nytimes.com/2026/04/25/health/pepfar-hiv-aids-zambia.html](https://www.nytimes.com/2026/04/25/health/pepfar-hiv-aids-zambia.html)

生成摘要时出错

---

## 71. My first in-prod corrupted hard drive problem

**原文标题**: My first in-prod corrupted hard drive problem

**原文链接**: [https://blog.pavementlink.ch/2026/05/07/my-first-corrupted-hard-drive-problem/](https://blog.pavementlink.ch/2026/05/07/my-first-corrupted-hard-drive-problem/)

生成摘要时出错

---

## 72. Looking at the data behind prediction markets

**原文标题**: Looking at the data behind prediction markets

**原文链接**: [https://asteriskmag.com/issues/14/are-prediction-markets-good-for-anything](https://asteriskmag.com/issues/14/are-prediction-markets-good-for-anything)

生成摘要时出错

---

## 73. Lua as a practical "soft-bedrock" language

**原文标题**: Lua as a practical "soft-bedrock" language

**原文链接**: [https://portal.mozz.us/gemini/zaibatsu.circumlunar.space/~solderpunk/gemlog/lua-as-a-practical-soft-bedrock-language.gmi](https://portal.mozz.us/gemini/zaibatsu.circumlunar.space/~solderpunk/gemlog/lua-as-a-practical-soft-bedrock-language.gmi)

生成摘要时出错

---

## 74. Valve releases Steam Controller CAD files under Creative Commons license

**原文标题**: Valve releases Steam Controller CAD files under Creative Commons license

**原文链接**: [https://www.digitalfoundry.net/news/2026/05/valve-releases-steam-controller-cad-files-under-creative-commons-license](https://www.digitalfoundry.net/news/2026/05/valve-releases-steam-controller-cad-files-under-creative-commons-license)

生成摘要时出错

---

## 75. QBE – Compiler Back End

**原文标题**: QBE – Compiler Back End

**原文链接**: [https://c9x.me/compile/](https://c9x.me/compile/)

生成摘要时出错

---

## 76. Apple May Drop Base $599 MacBook Neo as Chip, DRAM Costs Climb

**原文标题**: Apple May Drop Base $599 MacBook Neo as Chip, DRAM Costs Climb

**原文链接**: [https://www.macrumors.com/2026/05/07/apple-drop-base-macbook-neo-costs-climb/](https://www.macrumors.com/2026/05/07/apple-drop-base-macbook-neo-costs-climb/)

生成摘要时出错

---

## 77. Non-determinism is an issue with patching CVEs

**原文标题**: Non-determinism is an issue with patching CVEs

**原文链接**: [https://flox.dev/blog/achieving-rapid-cve-remediation-in-an-era-of-escalating-vulnerabilities/](https://flox.dev/blog/achieving-rapid-cve-remediation-in-an-era-of-escalating-vulnerabilities/)

生成摘要时出错

---

## 78. Inventing Cyrillic (2024)

**原文标题**: Inventing Cyrillic (2024)

**原文链接**: [https://www.historytoday.com/archive/history-matters/inventing-cyrillic](https://www.historytoday.com/archive/history-matters/inventing-cyrillic)

生成摘要时出错

---

## 79. Solar on canals reduces water evaporation by 70% and algae growth by 85%

**原文标题**: Solar on canals reduces water evaporation by 70% and algae growth by 85%

**原文链接**: [https://www.pv-magazine.com/2026/05/04/solar-on-canals-reduces-water-evaporation-by-70-and-algae-growth-by-85/](https://www.pv-magazine.com/2026/05/04/solar-on-canals-reduces-water-evaporation-by-70-and-algae-growth-by-85/)

生成摘要时出错

---

## 80. The map that keeps Burning Man honest

**原文标题**: The map that keeps Burning Man honest

**原文链接**: [https://www.not-ship.com/burning-man-moop/](https://www.not-ship.com/burning-man-moop/)

生成摘要时出错

---

## 81. Show HN: CADara – I made an open-source in-browser CAD

**原文标题**: Show HN: CADara – I made an open-source in-browser CAD

**原文链接**: [https://cadara.app](https://cadara.app)

生成摘要时出错

---

## 82. Show HN: GETadb.com – every GET request creates a DB

**原文标题**: Show HN: GETadb.com – every GET request creates a DB

**原文链接**: [https://www.getadb.com/](https://www.getadb.com/)

生成摘要时出错

---

## 83. AI slop is killing online communities

**原文标题**: AI slop is killing online communities

**原文链接**: [https://rmoff.net/2026/05/06/ai-slop-is-killing-online-communities/](https://rmoff.net/2026/05/06/ai-slop-is-killing-online-communities/)

生成摘要时出错

---

## 84. Hondurasgate: US, Israeli Plot to Destabilize Mexico, Latin America

**原文标题**: Hondurasgate: US, Israeli Plot to Destabilize Mexico, Latin America

**原文链接**: [https://english.elpais.com/international/2026-05-07/hondurasgate-the-alleged-us-and-israeli-interference-plot-to-destabilize-mexico-and-other-progressive-governments.html](https://english.elpais.com/international/2026-05-07/hondurasgate-the-alleged-us-and-israeli-interference-plot-to-destabilize-mexico-and-other-progressive-governments.html)

生成摘要时出错

---

## 85. Dithering with CSS

**原文标题**: Dithering with CSS

**原文链接**: [https://ikesau.co/blog/dithering-with-css/](https://ikesau.co/blog/dithering-with-css/)

生成摘要时出错

---

## 86. Man finds $1M worth of Yu-Gi-Oh cards in a dumpster

**原文标题**: Man finds $1M worth of Yu-Gi-Oh cards in a dumpster

**原文链接**: [https://www.404media.co/man-finds-1-million-worth-of-yu-gi-oh-cards-in-a-dumpster/](https://www.404media.co/man-finds-1-million-worth-of-yu-gi-oh-cards-in-a-dumpster/)

生成摘要时出错

---

## 87. Apple, Intel have reached preliminary chip-making deal

**原文标题**: Apple, Intel have reached preliminary chip-making deal

**原文链接**: [https://www.reuters.com/business/apple-intel-have-reached-preliminary-chip-making-deal-wsj-reports-2026-05-08/](https://www.reuters.com/business/apple-intel-have-reached-preliminary-chip-making-deal-wsj-reports-2026-05-08/)

生成摘要时出错

---

## 88. Show HN: TRUST – Coding Rust like it's 1989

**原文标题**: Show HN: TRUST – Coding Rust like it's 1989

**原文链接**: [https://github.com/wojtczyk/trust](https://github.com/wojtczyk/trust)

生成摘要时出错

---

## 89. GNU IFUNC is the real culprit behind CVE-2024-3094

**原文标题**: GNU IFUNC is the real culprit behind CVE-2024-3094

**原文链接**: [https://github.com/robertdfrench/ifuncd-up](https://github.com/robertdfrench/ifuncd-up)

生成摘要时出错

---

## 90. Two Home Affairs officials suspended after AI 'hallucinations' found

**原文标题**: Two Home Affairs officials suspended after AI 'hallucinations' found

**原文链接**: [https://www.citizen.co.za/news/home-affairs-officials-suspended-ai-hallucinations/](https://www.citizen.co.za/news/home-affairs-officials-suspended-ai-hallucinations/)

生成摘要时出错

---

## 91. Boosting multimodal inference performance by >10% with a single Python dict

**原文标题**: Boosting multimodal inference performance by >10% with a single Python dict

**原文链接**: [https://modal.com/blog/boosting-multimodal-inference-performance-by-greater-than-10-with-a-single-python-dictionary](https://modal.com/blog/boosting-multimodal-inference-performance-by-greater-than-10-with-a-single-python-dictionary)

生成摘要时出错

---

## 92. Fiber optic cables can eavesdrop on nearby conversations

**原文标题**: Fiber optic cables can eavesdrop on nearby conversations

**原文链接**: [https://www.science.org/content/article/fiber-optic-cables-can-eavesdrop-nearby-conversations](https://www.science.org/content/article/fiber-optic-cables-can-eavesdrop-nearby-conversations)

生成摘要时出错

---

## 93. Jetro – JSON query engine for Rust (jq-like DSL with compilation and VM)

**原文标题**: Jetro – JSON query engine for Rust (jq-like DSL with compilation and VM)

**原文链接**: [https://github.com/mitghi/jetro](https://github.com/mitghi/jetro)

生成摘要时出错

---

## 94. Plasticity and language in the anaesthetized human hippocampus

**原文标题**: Plasticity and language in the anaesthetized human hippocampus

**原文链接**: [https://www.bcm.edu/news/researchers-discover-advanced-language-processing-in-the-unconscious-human-brain](https://www.bcm.edu/news/researchers-discover-advanced-language-processing-in-the-unconscious-human-brain)

生成摘要时出错

---

## 95. RSS feeds send me more traffic than Google

**原文标题**: RSS feeds send me more traffic than Google

**原文链接**: [https://shkspr.mobi/blog/2026/05/rss-feeds-send-me-more-traffic-than-google/](https://shkspr.mobi/blog/2026/05/rss-feeds-send-me-more-traffic-than-google/)

生成摘要时出错

---

## 96. I want to live like Costco people

**原文标题**: I want to live like Costco people

**原文链接**: [https://tastecooking.com/i-want-to-live-like-costco-people/](https://tastecooking.com/i-want-to-live-like-costco-people/)

生成摘要时出错

---

## 97. GrapheneOS isn't vulnerable to the 3 recent Linux memory logic vulnerabilities

**原文标题**: GrapheneOS isn't vulnerable to the 3 recent Linux memory logic vulnerabilities

**原文链接**: [https://discuss.grapheneos.org/d/35353-grapheneos-isnt-vulnerable-to-the-3-recent-linux-memory-logic-vulnerabilities](https://discuss.grapheneos.org/d/35353-grapheneos-isnt-vulnerable-to-the-3-recent-linux-memory-logic-vulnerabilities)

生成摘要时出错

---

## 98. A polynomial autoencoder beats PCA on transformer embeddings

**原文标题**: A polynomial autoencoder beats PCA on transformer embeddings

**原文链接**: [https://ivanpleshkov.dev/blog/polynomial-autoencoder/](https://ivanpleshkov.dev/blog/polynomial-autoencoder/)

生成摘要时出错

---

## 99. Blaise – A modern self-hosting zero-legacy Object Pascal compiler targeting QBE

**原文标题**: Blaise – A modern self-hosting zero-legacy Object Pascal compiler targeting QBE

**原文链接**: [https://github.com/graemeg/blaise](https://github.com/graemeg/blaise)

生成摘要时出错

---

## 100. Appearing productive in the workplace

**原文标题**: Appearing productive in the workplace

**原文链接**: [https://nooneshappy.com/article/appearing-productive-in-the-workplace/](https://nooneshappy.com/article/appearing-productive-in-the-workplace/)

生成摘要时出错

---

