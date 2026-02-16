# Hacker News 热门文章摘要 (2026-02-16)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 英国司法部下令删除英国最大的庭审报告数据库。

**原文标题**: Ministry of Justice orders deletion of the UK's largest court reporting database

**原文链接**: [https://www.legalcheek.com/2026/02/ministry-of-justice-orders-deletion-of-the-uks-largest-court-reporting-database/](https://www.legalcheek.com/2026/02/ministry-of-justice-orders-deletion-of-the-uks-largest-court-reporting-database/)

英国司法部（MoJ）已下令永久删除该国最大的法庭报道数据库 Courtsdesk，此举引发了关于“司法公开”与数据隐私的激烈辩论。

**冲突焦点**
英国法院及法庭事务局（HMCTS）向该平台发布了关停通知，理由是其涉嫌与第三方人工智能公司“未经授权共享”敏感庭审信息。因此，司法部强制要求抹除该档案库中的所有记录。

**对新闻业的影响**
Courtsdesk 于 2020 年在政府批准下推出，是来自 39 家媒体机构的 1500 多名记者追踪地方法院案件的重要工具。创始人恩达·莱希（Enda Leahy）辩称，该服务至关重要，因为据称 HMCTS 的官方记录准确率仅为 4.2%。她进一步声称，已有 160 万场刑事听证会在未预先通知媒体的情况下进行，并断言 Courtsdesk 是唯一能让记者获悉法庭实况的系统。

**政府回应**
尽管有 16 次暂缓执行的呼吁，且前司法部部长克里斯·菲利普（Chris Philp）也曾介入，但现任法院部部长萨拉·萨克曼（Sarah Sackman）仍拒绝保留该档案库。司法部发言人坚称，记者的信息获取权并未受损，因为官方名单和记录仍可通过政府渠道获取。

**公众舆论**
此举遭到了法律评论员和记者的严厉批评，他们认为这是对透明度的打击，并将其视为迈向“媒体封锁”的一步。相反，一些支持该决定的人士认为，保护个人数据免受人工智能剥削是必要的安全措施。

此次删除标志着一个中心化、可搜索的数字档案库的终结，而媒体界的许多人曾将其视为现代刑事法庭报道的支柱。

---

## 2. 运行我自己的 XMPP 服务器

**原文标题**: Running My Own XMPP Server

**原文链接**: [https://blog.dmcc.io/journal/xmpp-turn-stun-coturn-prosody/](https://blog.dmcc.io/journal/xmpp-turn-stun-coturn-prosody/)

本文概述了使用 **Prosody** 和 **Docker** 搭建个人联邦化 XMPP 服务器的指南。出于对数字主权以及摆脱 Signal 等中心化平台的渴望，作者展示了 XMPP 如何提供一种可靠的自托管消息传递备选方案。

**关键技术步骤：**
*   **基础设施：** 该方案使用 Docker Compose 运行 Prosody 13.0。它需要一个带有特定 **DNS SRV 记录**（用于客户端和服务器发现）的域名，以及通过 Let’s Encrypt 和 Cloudflare 获取的 TLS 证书。
*   **移动端优化：** 为确保现代化的用户体验，作者强调了几个核心模块：用于多设备同步的 `carbons`、用于处理连接不稳定的 `smacks`，以及用于移动推送通知的 `cloud_notify`。
*   **安全性：** 配置要求强制加密连接（c2s/s2s）并禁用公开注册。尽管服务器本身是安全的，作者仍建议使用 **OMEMO** 进行客户端端到端加密。
*   **高级功能：**
    *   **文件共享：** 通过带有 Caddy 反向代理的 HTTP 上传组件实现。
    *   **群聊：** 通过多用户聊天 (MUC) 模块启用。
    *   **音视频通话：** 需要独立的 **Coturn** 容器提供 STUN/TURN 服务以实现 NAT 穿透。
*   **客户端兼容性：** 推荐的客户端包括 **Monal** (iOS/macOS)、**Conversations** (Android) 和 **Gajim** (桌面端)，它们均支持现代 XMPP 标准。

作者总结道，虽然 Signal 仍是其主要工具，但自托管 XMPP 服务器是一个轻量且稳健的“周末项目”，能确保用户不会被锁定在单一供应商的生态系统中。该配置可通过 `prosodyctl check` 工具和 XMPP 合规性测试器轻松验证。

---

## 3. 蓝牙设备揭示了你的哪些信息

**原文标题**: What Your Bluetooth Devices Reveal About You

**原文链接**: [https://blog.dmcc.io/journal/2026-bluetooth-privacy-bluehood/](https://blog.dmcc.io/journal/2026-bluetooth-privacy-bluehood/)

在本文中，作者介绍了 **Bluehood**，这是一款旨在演示持续蓝牙广播带来的重大隐私风险的开源蓝牙扫描器。受近期 **WhisperPair** 漏洞 (CVE-2025-36911) 的启发，作者探讨了我们的“常开”设备如何充当数字面包屑（digital breadcrumbs）。

**关键点：**
*   **被动元数据泄露：** 仅通过监听而不进行连接，Bluehood 工具就能识别生活模式，例如邻居何时出门上班、哪些设备属于同一个人（如手机与智能手表的配对），以及送货车辆到达的频率。
*   **控制权问题：** 许多设备（包括助听器、心脏起搏器和物流车队）会持续广播信号，且未向用户提供禁用选项。
*   **隐私悖论：** 像 **Briar** 和 **BitChat** 这样安全的点对点通讯应用在网络中断期间依赖蓝牙运行。这造成了一种矛盾：旨在保护隐私的工具同时暴露了用户的物理存在。
*   **Bluehood 的功能：** 该工具利用 Python 在 AI 辅助下构建，具备被动扫描、设备分类和模式分析（热图和停留时间）功能。它专为教育目的而非黑客攻击设计，可在树莓派或笔记本电脑等基础硬件上运行。

**结论：**
该项目提供了一个“发人深省”的提醒：即使没有恶意，任何具备基础技术知识的人都能收集到有关家庭习惯的敏感信息。作者总结道，虽然蓝牙通常是出于便利或医疗需求所必需的，但用户必须理解保持无线电功能开启所固有的隐私权衡。

---

## 4. Show HN：简单的 org-mode Web 适配器

**原文标题**: Show HN: Simple org-mode web adapter

**原文链接**: [https://github.com/SpaceTurth/Org-Web-Adapter](https://github.com/SpaceTurth/Org-Web-Adapter)

**Org Web Adapter** 是一款轻量级的本地 Web 应用程序，专为通过浏览器浏览和编辑 Emacs Org-mode 文件而设计。它由极简的 Python 后端（`main.py`）和单页面 HTML/CSS 前端构建，提供了一个实用的三窗格界面，无需复杂的基础设施即可管理个人笔记。

**核心功能：**
*   **导航与搜索：** 递归扫描指定目录下的 `.org` 文件，并将其呈现在可搜索的侧边栏中。支持按创建日期、反向链接数量或随机排序。
*   **链接管理：** 支持解析 `file:` 和 `id:` 链接，并自动计算反向链接，在专用窗格中显示笔记之间的关联。
*   **编辑与渲染：** 用户可以在预览模式和内置编辑器之间切换，修改将直接保存至本地磁盘。内置 MathJax 支持以实现 LaTeX 数学公式渲染，并采用兼容桌面与移动端的响应式设计。
*   **自定义：** 界面支持浅色/深色主题切换，服务器可通过 YAML 文件或命令行参数进行配置。

**技术考量：**
该应用的设计初衷是追求简单而非高性能扩展。它在每次请求时都会重新扫描笔记目录以确保数据实时性，并使用简化的自定义 Org 解析器而非完整实现。

**安全警告：**
该工具不含内置身份验证或加密功能。因此，开发者建议仅在受信任的本地网络中运行。对于希望快速通过 Web 访问 Org-mode 知识库的用户，它提供了一个精简的“单文件”解决方案。

---

## 5. NSA 开发的 Ghidra

**原文标题**: Ghidra by NSA

**原文链接**: [https://github.com/NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

Ghidra是由美国国家安全局（NSA）研究局开发并维护的一款综合性软件逆向工程（SRE）框架。它旨在处理大规模、复杂的分析任务，支持用户在Windows、macOS和Linux平台上检查已编译的代码。其核心功能包括反汇编、反编译、汇编、图形化分析和脚本编写，支持大量的处理器指令集和可执行文件格式。

Ghidra最初是为辅助NSA的网络安全任务而构建的——专门用于分析恶意代码和识别网络漏洞——现在已成为一个开源平台。它具有高度的可扩展性，允许用户通过集成Eclipse或Visual Studio Code，使用Java或Python开发自定义组件和脚本。

**关键技术信息：**
*   **环境

NSA鼓励开源社区做出贡献，并利用该项目为有志于开发网络安全工具以保护国家利益的美国公民展示职业机会。

---

## 6. Qwen3.5: Towards Native Multimodal Agents

**原文标题**: Qwen3.5: Towards Native Multimodal Agents

**原文链接**: [https://qwen.ai/blog?id=qwen3.5](https://qwen.ai/blog?id=qwen3.5)

生成摘要时出错

---

## 7. The Sideprocalypse

**原文标题**: The Sideprocalypse

**原文链接**: [https://johan.hal.se/wrote/2026/02/03/the-sideprocalypse/](https://johan.hal.se/wrote/2026/02/03/the-sideprocalypse/)

生成摘要时出错

---

## 8. WebMCP Proposal

**原文标题**: WebMCP Proposal

**原文链接**: [https://webmachinelearning.github.io/webmcp/](https://webmachinelearning.github.io/webmcp/)

生成摘要时出错

---

## 9. I want to wash my car. The car wash is 50 meters away. Should I walk or drive?

**原文标题**: I want to wash my car. The car wash is 50 meters away. Should I walk or drive?

**原文链接**: [https://mastodon.world/@knowmadd/116072773118828295](https://mastodon.world/@knowmadd/116072773118828295)

生成摘要时出错

---

## 10. I’m joining OpenAI

**原文标题**: I’m joining OpenAI

**原文链接**: [https://steipete.me/posts/2026/openclaw](https://steipete.me/posts/2026/openclaw)

生成摘要时出错

---

## 11. How to take a photo with scotch tape (lensless imaging) [video]

**原文标题**: How to take a photo with scotch tape (lensless imaging) [video]

**原文链接**: [https://www.youtube.com/watch?v=97f0nfU5Px0](https://www.youtube.com/watch?v=97f0nfU5Px0)

生成摘要时出错

---

## 12. Rolling your own serverless OCR in 40 lines of code

**原文标题**: Rolling your own serverless OCR in 40 lines of code

**原文链接**: [https://christopherkrapu.com/blog/2026/ocr-textbooks-modal-deepseek/](https://christopherkrapu.com/blog/2026/ocr-textbooks-modal-deepseek/)

生成摘要时出错

---

## 13. MessageFormat: Unicode standard for localizable message strings

**原文标题**: MessageFormat: Unicode standard for localizable message strings

**原文链接**: [https://github.com/unicode-org/message-format-wg](https://github.com/unicode-org/message-format-wg)

生成摘要时出错

---

## 14. planckforth: Bootstrapping a Forth interpreter from hand-written tiny ELF binary

**原文标题**: planckforth: Bootstrapping a Forth interpreter from hand-written tiny ELF binary

**原文链接**: [https://github.com/nineties/planckforth](https://github.com/nineties/planckforth)

生成摘要时出错

---

## 15. UK Discord users were part of a Peter Thiel-linked data collection experiment

**原文标题**: UK Discord users were part of a Peter Thiel-linked data collection experiment

**原文链接**: [https://www.rockpapershotgun.com/good-news-uk-discord-users-were-part-of-a-peter-thiel-linked-data-collection-experiment](https://www.rockpapershotgun.com/good-news-uk-discord-users-were-part-of-a-peter-thiel-linked-data-collection-experiment)

生成摘要时出错

---

## 16. Anthropic tries to hide Claude's AI actions. Devs hate it

**原文标题**: Anthropic tries to hide Claude's AI actions. Devs hate it

**原文链接**: [https://www.theregister.com/2026/02/16/anthropic_claude_ai_edits/](https://www.theregister.com/2026/02/16/anthropic_claude_ai_edits/)

生成摘要时出错

---

## 17. Richard Carrington's first portrait has been found

**原文标题**: Richard Carrington's first portrait has been found

**原文链接**: [https://www.cnn.com/2026/02/12/science/solar-storm-richard-carrington-photo](https://www.cnn.com/2026/02/12/science/solar-storm-richard-carrington-photo)

生成摘要时出错

---

## 18. Looks: A Halide Mark III Preview

**原文标题**: Looks: A Halide Mark III Preview

**原文链接**: [https://www.lux.camera/mark-iii-looks/](https://www.lux.camera/mark-iii-looks/)

生成摘要时出错

---

## 19. Modern CSS Code Snippets: Stop writing CSS like it's 2015

**原文标题**: Modern CSS Code Snippets: Stop writing CSS like it's 2015

**原文链接**: [https://modern-css.com](https://modern-css.com)

生成摘要时出错

---

## 20. Vim-pencil: Rethinking Vim as a tool for writing

**原文标题**: Vim-pencil: Rethinking Vim as a tool for writing

**原文链接**: [https://github.com/preservim/vim-pencil](https://github.com/preservim/vim-pencil)

生成摘要时出错

---

## 21. picol: A Tcl interpreter in 500 lines of code

**原文标题**: picol: A Tcl interpreter in 500 lines of code

**原文链接**: [https://github.com/antirez/picol](https://github.com/antirez/picol)

生成摘要时出错

---

## 22. Magnus Carlsen Wins the Freestyle (Chess960) World Championship

**原文标题**: Magnus Carlsen Wins the Freestyle (Chess960) World Championship

**原文链接**: [https://www.fide.com/magnus-carlsen-wins-2026-fide-freestyle-world-championship/](https://www.fide.com/magnus-carlsen-wins-2026-fide-freestyle-world-championship/)

生成摘要时出错

---

## 23. Expensively Quadratic: The LLM Agent Cost Curve

**原文标题**: Expensively Quadratic: The LLM Agent Cost Curve

**原文链接**: [https://blog.exe.dev/expensively-quadratic](https://blog.exe.dev/expensively-quadratic)

生成摘要时出错

---

## 24. Audio is the one area small labs are winning

**原文标题**: Audio is the one area small labs are winning

**原文链接**: [https://www.amplifypartners.com/blog-posts/arming-the-rebels-with-gpus-gradium-kyutai-and-audio-ai](https://www.amplifypartners.com/blog-posts/arming-the-rebels-with-gpus-gradium-kyutai-and-audio-ai)

生成摘要时出错

---

## 25. LT6502: A 6502-based homebrew laptop

**原文标题**: LT6502: A 6502-based homebrew laptop

**原文链接**: [https://github.com/TechPaula/LT6502](https://github.com/TechPaula/LT6502)

生成摘要时出错

---

## 26. Palantir CEO wants to spray "fentanyl-laced urine" on analysts

**原文标题**: Palantir CEO wants to spray "fentanyl-laced urine" on analysts

**原文链接**: [https://twitter.com/jawwwn_/status/2023207418922959234](https://twitter.com/jawwwn_/status/2023207418922959234)

生成摘要时出错

---

## 27. Thanks a lot, AI: Hard drives are sold out for the year, says WD

**原文标题**: Thanks a lot, AI: Hard drives are sold out for the year, says WD

**原文链接**: [https://mashable.com/article/ai-hard-drive-hdd-shortages-western-digital-sold-out](https://mashable.com/article/ai-hard-drive-hdd-shortages-western-digital-sold-out)

生成摘要时出错

---

## 28. I gave Claude access to my pen plotter

**原文标题**: I gave Claude access to my pen plotter

**原文链接**: [https://harmonique.one/posts/i-gave-claude-access-to-my-pen-plotter](https://harmonique.one/posts/i-gave-claude-access-to-my-pen-plotter)

生成摘要时出错

---

## 29. Hard problems in social media archiving

**原文标题**: Hard problems in social media archiving

**原文链接**: [https://alexwlchan.net/2025/hard-problems-in-social-media-archiving/](https://alexwlchan.net/2025/hard-problems-in-social-media-archiving/)

生成摘要时出错

---

## 30. 1,300-year-old world chronicle unearthed in Sinai

**原文标题**: 1,300-year-old world chronicle unearthed in Sinai

**原文链接**: [https://www.heritagedaily.com/2026/02/1300-year-old-world-chronicle-unearthed-in-sinai/156948](https://www.heritagedaily.com/2026/02/1300-year-old-world-chronicle-unearthed-in-sinai/156948)

生成摘要时出错

---

## 31. Show HN: Microgpt is a GPT you can visualize in the browser

**原文标题**: Show HN: Microgpt is a GPT you can visualize in the browser

**原文链接**: [https://microgpt.boratto.ca](https://microgpt.boratto.ca)

生成摘要时出错

---

## 32. JavaScript-heavy approaches are not compatible with long-term performance goals

**原文标题**: JavaScript-heavy approaches are not compatible with long-term performance goals

**原文链接**: [https://sgom.es/posts/2026-02-13-js-heavy-approaches-are-not-compatible-with-long-term-performance-goals/](https://sgom.es/posts/2026-02-13-js-heavy-approaches-are-not-compatible-with-long-term-performance-goals/)

生成摘要时出错

---

## 33. Arm wants a bigger slice of the chip business

**原文标题**: Arm wants a bigger slice of the chip business

**原文链接**: [https://www.economist.com/business/2026/02/12/arm-wants-a-bigger-slice-of-the-chip-business](https://www.economist.com/business/2026/02/12/arm-wants-a-bigger-slice-of-the-chip-business)

生成摘要时出错

---

## 34. EU bans the destruction of unsold apparel, clothing, accessories and footwear

**原文标题**: EU bans the destruction of unsold apparel, clothing, accessories and footwear

**原文链接**: [https://environment.ec.europa.eu/news/new-eu-rules-stop-destruction-unsold-clothes-and-shoes-2026-02-09_en](https://environment.ec.europa.eu/news/new-eu-rules-stop-destruction-unsold-clothes-and-shoes-2026-02-09_en)

生成摘要时出错

---

## 35. iOS 27 'Rave' Update to Clean Up Code, Could Boost Battery Life

**原文标题**: iOS 27 'Rave' Update to Clean Up Code, Could Boost Battery Life

**原文链接**: [https://www.macrumors.com/2026/02/16/apple-plans-snow-leopard-cleanup-ios-27/](https://www.macrumors.com/2026/02/16/apple-plans-snow-leopard-cleanup-ios-27/)

生成摘要时出错

---

## 36. Gwtar: A static efficient single-file HTML format

**原文标题**: Gwtar: A static efficient single-file HTML format

**原文链接**: [https://gwern.net/gwtar](https://gwern.net/gwtar)

生成摘要时出错

---

## 37. Real-time PathTracing with global illumination in WebGL

**原文标题**: Real-time PathTracing with global illumination in WebGL

**原文链接**: [https://erichlof.github.io/THREE.js-PathTracing-Renderer/](https://erichlof.github.io/THREE.js-PathTracing-Renderer/)

生成摘要时出错

---

## 38. Show HN: Knock-Knock.net – Visualizing the bots knocking on my server's door

**原文标题**: Show HN: Knock-Knock.net – Visualizing the bots knocking on my server's door

**原文链接**: [https://knock-knock.net](https://knock-knock.net)

生成摘要时出错

---

## 39. How DSQL makes sure sequences scale

**原文标题**: How DSQL makes sure sequences scale

**原文链接**: [https://blog.benjscho.dev/technical/2026/02/13/dsql-sequences.html](https://blog.benjscho.dev/technical/2026/02/13/dsql-sequences.html)

生成摘要时出错

---

## 40. Pocketblue – Fedora Atomic for mobile devices

**原文标题**: Pocketblue – Fedora Atomic for mobile devices

**原文链接**: [https://github.com/pocketblue/pocketblue](https://github.com/pocketblue/pocketblue)

生成摘要时出错

---

## 41. Amazon's Ring and Google's Nest reveal the severity of U.S. surveillance state

**原文标题**: Amazon's Ring and Google's Nest reveal the severity of U.S. surveillance state

**原文链接**: [https://greenwald.substack.com/p/amazons-ring-and-googles-nest-unwittingly](https://greenwald.substack.com/p/amazons-ring-and-googles-nest-unwittingly)

生成摘要时出错

---

## 42. Evaluating AGENTS.md: are they helpful for coding agents?

**原文标题**: Evaluating AGENTS.md: are they helpful for coding agents?

**原文链接**: [https://arxiv.org/abs/2602.11988](https://arxiv.org/abs/2602.11988)

生成摘要时出错

---

## 43. Building SQLite with a small swarm

**原文标题**: Building SQLite with a small swarm

**原文链接**: [https://kiankyars.github.io/machine_learning/2026/02/12/sqlite.html](https://kiankyars.github.io/machine_learning/2026/02/12/sqlite.html)

生成摘要时出错

---

## 44. GNU Pies – Program Invocation and Execution Supervisor

**原文标题**: GNU Pies – Program Invocation and Execution Supervisor

**原文链接**: [https://www.gnu.org.ua/software/pies/](https://www.gnu.org.ua/software/pies/)

生成摘要时出错

---

## 45. I fixed Windows native development

**原文标题**: I fixed Windows native development

**原文链接**: [https://marler8997.github.io/blog/fixed-windows/](https://marler8997.github.io/blog/fixed-windows/)

生成摘要时出错

---

## 46. Error payloads in Zig

**原文标题**: Error payloads in Zig

**原文链接**: [https://srcreigh.ca/posts/error-payloads-in-zig/](https://srcreigh.ca/posts/error-payloads-in-zig/)

生成摘要时出错

---

## 47. Lost Soviet Moon Lander May Have Been Found

**原文标题**: Lost Soviet Moon Lander May Have Been Found

**原文链接**: [https://www.nytimes.com/2026/02/10/science/luna-9-moon-lander-soviet.html](https://www.nytimes.com/2026/02/10/science/luna-9-moon-lander-soviet.html)

生成摘要时出错

---

## 48. Editor's Note: Retraction of article containing fabricated quotations

**原文标题**: Editor's Note: Retraction of article containing fabricated quotations

**原文链接**: [https://arstechnica.com/staff/2026/02/editors-note-retraction-of-article-containing-fabricated-quotations/](https://arstechnica.com/staff/2026/02/editors-note-retraction-of-article-containing-fabricated-quotations/)

生成摘要时出错

---

## 49. Radio host David Greene says Google's NotebookLM tool stole his voice

**原文标题**: Radio host David Greene says Google's NotebookLM tool stole his voice

**原文链接**: [https://www.washingtonpost.com/technology/2026/02/15/david-greene-google-ai-podcast/](https://www.washingtonpost.com/technology/2026/02/15/david-greene-google-ai-podcast/)

生成摘要时出错

---

## 50. Designing a 36-key custom keyboard layout (2021)

**原文标题**: Designing a 36-key custom keyboard layout (2021)

**原文链接**: [https://peterxjang.medium.com/designing-a-36-key-custom-keyboard-layout-24498a0eecd4](https://peterxjang.medium.com/designing-a-36-key-custom-keyboard-layout-24498a0eecd4)

生成摘要时出错

---

## 51. I love the work of the ArchWiki maintainers

**原文标题**: I love the work of the ArchWiki maintainers

**原文链接**: [https://k7r.eu/i-love-the-work-of-the-archwiki-maintainers/](https://k7r.eu/i-love-the-work-of-the-archwiki-maintainers/)

生成摘要时出错

---

## 52. Transforming a Clojure Database into a Library with GraalVM Native Image and FFI

**原文标题**: Transforming a Clojure Database into a Library with GraalVM Native Image and FFI

**原文链接**: [https://avelino.run/chrondb-polyglot-ffi-clojure-graalvm-native-image/](https://avelino.run/chrondb-polyglot-ffi-clojure-graalvm-native-image/)

生成摘要时出错

---

## 53. Btrfs disk errors to fall asleep to

**原文标题**: Btrfs disk errors to fall asleep to

**原文链接**: [https://ounapuu.ee/btrfs-disk-errors-to-fall-asleep-to/index.html](https://ounapuu.ee/btrfs-disk-errors-to-fall-asleep-to/index.html)

生成摘要时出错

---

## 54. Turning Our Back on Clean Energy

**原文标题**: Turning Our Back on Clean Energy

**原文链接**: [https://paulkrugman.substack.com/p/turning-our-back-on-clean-energy](https://paulkrugman.substack.com/p/turning-our-back-on-clean-energy)

生成摘要时出错

---

## 55. SCM as a database for the code

**原文标题**: SCM as a database for the code

**原文链接**: [https://gist.github.com/gritzko/6e81b5391eacb585ae207f5e634db07e](https://gist.github.com/gritzko/6e81b5391eacb585ae207f5e634db07e)

生成摘要时出错

---

## 56. Reversed engineered game Starflight (1986)

**原文标题**: Reversed engineered game Starflight (1986)

**原文链接**: [https://github.com/s-macke/starflight-reverse](https://github.com/s-macke/starflight-reverse)

生成摘要时出错

---

## 57. Towards Autonomous Mathematics Research

**原文标题**: Towards Autonomous Mathematics Research

**原文链接**: [https://arxiv.org/abs/2602.10177](https://arxiv.org/abs/2602.10177)

生成摘要时出错

---

## 58. Show HN: VOOG – Moog-style polyphonic synthesizer in Python with tkinter GUI

**原文标题**: Show HN: VOOG – Moog-style polyphonic synthesizer in Python with tkinter GUI

**原文链接**: [https://github.com/gpasquero/voog](https://github.com/gpasquero/voog)

生成摘要时出错

---

## 59. Hideki Sato, designer of all Sega's consoles, has died

**原文标题**: Hideki Sato, designer of all Sega's consoles, has died

**原文链接**: [https://www.videogameschronicle.com/news/hideki-sato-designer-of-segas-consoles-dies-age-75/](https://www.videogameschronicle.com/news/hideki-sato-designer-of-segas-consoles-dies-age-75/)

生成摘要时出错

---

## 60. Pentagon Threatens Anthropic Punishment

**原文标题**: Pentagon Threatens Anthropic Punishment

**原文链接**: [https://www.axios.com/2026/02/16/anthropic-defense-department-relationship-hegseth](https://www.axios.com/2026/02/16/anthropic-defense-department-relationship-hegseth)

生成摘要时出错

---

## 61. AI is going to kill app subscriptions

**原文标题**: AI is going to kill app subscriptions

**原文链接**: [https://nichehunt.app/blog/ai-going-to-kill-app-subscriptions](https://nichehunt.app/blog/ai-going-to-kill-app-subscriptions)

生成摘要时出错

---

## 62. Show HN: Pangolin: Open-source identity-based VPN (Twingate/Zscaler alternative)

**原文标题**: Show HN: Pangolin: Open-source identity-based VPN (Twingate/Zscaler alternative)

**原文链接**: [https://github.com/fosrl/pangolin](https://github.com/fosrl/pangolin)

生成摘要时出错

---

## 63. 1940s Irish sci-fi novel features early mecha and gravity assists

**原文标题**: 1940s Irish sci-fi novel features early mecha and gravity assists

**原文链接**: [https://github.com/cavedave/Manannan](https://github.com/cavedave/Manannan)

生成摘要时出错

---

## 64. Databases should contain their own Metadata – Use SQL Everywhere

**原文标题**: Databases should contain their own Metadata – Use SQL Everywhere

**原文链接**: [https://floedb.ai/blog/databases-should-contain-their-own-metadata-instrumentation-in-floe](https://floedb.ai/blog/databases-should-contain-their-own-metadata-instrumentation-in-floe)

生成摘要时出错

---

## 65. Two different tricks for fast LLM inference

**原文标题**: Two different tricks for fast LLM inference

**原文链接**: [https://www.seangoedecke.com/fast-llm-inference/](https://www.seangoedecke.com/fast-llm-inference/)

生成摘要时出错

---

## 66. Why I don't think AGI is imminent

**原文标题**: Why I don't think AGI is imminent

**原文链接**: [https://dlants.me/agi-not-imminent.html](https://dlants.me/agi-not-imminent.html)

生成摘要时出错

---

## 67. LEDs Enter the Nanoscale, But efficiency hurdles challenge the smallest LEDs yet

**原文标题**: LEDs Enter the Nanoscale, But efficiency hurdles challenge the smallest LEDs yet

**原文链接**: [https://spectrum.ieee.org/nanoled-research-approaches](https://spectrum.ieee.org/nanoled-research-approaches)

生成摘要时出错

---

## 68. Oat – Ultra-lightweight, zero dependency, semantic HTML, CSS, JS UI library

**原文标题**: Oat – Ultra-lightweight, zero dependency, semantic HTML, CSS, JS UI library

**原文链接**: [https://oat.ink/](https://oat.ink/)

生成摘要时出错

---

## 69. Palantir Gets Millions of Dollars from New York City's Public Hospitals

**原文标题**: Palantir Gets Millions of Dollars from New York City's Public Hospitals

**原文链接**: [https://theintercept.com/2026/02/15/palantir-contract-new-york-city-health-hospitals/](https://theintercept.com/2026/02/15/palantir-contract-new-york-city-health-hospitals/)

生成摘要时出错

---

## 70. Flashpoint Archive – Over 200k web games and animations preserved

**原文标题**: Flashpoint Archive – Over 200k web games and animations preserved

**原文链接**: [https://flashpointarchive.org](https://flashpointarchive.org)

生成摘要时出错

---

## 71. The Israeli spyware firm that accidentally just exposed itself

**原文标题**: The Israeli spyware firm that accidentally just exposed itself

**原文链接**: [https://ahmedeldin.substack.com/p/the-israeli-spyware-firm-that-accidentally](https://ahmedeldin.substack.com/p/the-israeli-spyware-firm-that-accidentally)

生成摘要时出错

---

## 72. My smart sleep mask broadcasts users' brainwaves to an open MQTT broker

**原文标题**: My smart sleep mask broadcasts users' brainwaves to an open MQTT broker

**原文链接**: [https://aimilios.bearblog.dev/reverse-engineering-sleep-mask/](https://aimilios.bearblog.dev/reverse-engineering-sleep-mask/)

生成摘要时出错

---

## 73. Cogram (YC W22) – Hiring former technical founders

**原文标题**: Cogram (YC W22) – Hiring former technical founders

**原文链接**: [https://www.ycombinator.com/companies/cogram/jobs/LDTrViN-ex-technical-founder-product-engineer](https://www.ycombinator.com/companies/cogram/jobs/LDTrViN-ex-technical-founder-product-engineer)

生成摘要时出错

---

## 74. Show HN: JeffTube

**原文标题**: Show HN: JeffTube

**原文链接**: [https://jmail.world/jefftube](https://jmail.world/jefftube)

生成摘要时出错

---

## 75. Language a Wood for Thought: Susan Howe's Work

**原文标题**: Language a Wood for Thought: Susan Howe's Work

**原文链接**: [https://www.poetryfoundation.org/articles/1769037/language-a-wood-for-thought](https://www.poetryfoundation.org/articles/1769037/language-a-wood-for-thought)

生成摘要时出错

---

## 76. Continuous batching from first principles (2025)

**原文标题**: Continuous batching from first principles (2025)

**原文链接**: [https://huggingface.co/blog/continuous_batching](https://huggingface.co/blog/continuous_batching)

生成摘要时出错

---

## 77. Kimi Claw

**原文标题**: Kimi Claw

**原文链接**: [https://www.kimi.com/bot](https://www.kimi.com/bot)

生成摘要时出错

---

## 78. Palantir vs. the "Republik": US analytics firm takes magazine to court

**原文标题**: Palantir vs. the "Republik": US analytics firm takes magazine to court

**原文链接**: [https://www.heise.de/en/news/Palantir-vs-the-Republik-US-analytics-firm-takes-magazine-to-court-11176508.html](https://www.heise.de/en/news/Palantir-vs-the-Republik-US-analytics-firm-takes-magazine-to-court-11176508.html)

生成摘要时出错

---

## 79. Sony Jumbotron Image Control System (1998) [pdf]

**原文标题**: Sony Jumbotron Image Control System (1998) [pdf]

**原文链接**: [https://pro.sony/s3/cms-static-content/operation-manual/3864848111.pdf](https://pro.sony/s3/cms-static-content/operation-manual/3864848111.pdf)

生成摘要时出错

---

## 80. Pink noise reduces REM sleep and may harm sleep quality

**原文标题**: Pink noise reduces REM sleep and may harm sleep quality

**原文链接**: [https://www.pennmedicine.org/news/pink-noise-reduces-rem-sleep-and-may-harm-sleep-quality](https://www.pennmedicine.org/news/pink-noise-reduces-rem-sleep-and-may-harm-sleep-quality)

生成摘要时出错

---

## 81. Ooh.directory: a place to find good blogs that interest you

**原文标题**: Ooh.directory: a place to find good blogs that interest you

**原文链接**: [https://ooh.directory/](https://ooh.directory/)

生成摘要时出错

---

## 82. OpenAI should build Slack

**原文标题**: OpenAI should build Slack

**原文链接**: [https://www.latent.space/p/ainews-why-openai-should-build-slack](https://www.latent.space/p/ainews-why-openai-should-build-slack)

生成摘要时出错

---

## 83. Peter Thiel: 2,436 emails with Epstein from 2014 to 2019

**原文标题**: Peter Thiel: 2,436 emails with Epstein from 2014 to 2019

**原文链接**: [https://jmail.world/wiki/peter-thiel](https://jmail.world/wiki/peter-thiel)

生成摘要时出错

---

## 84. DjVu and its connection to Deep Learning (2023)

**原文标题**: DjVu and its connection to Deep Learning (2023)

**原文链接**: [https://scottlocklin.wordpress.com/2023/05/31/djvu-and-its-connection-to-deep-learning/](https://scottlocklin.wordpress.com/2023/05/31/djvu-and-its-connection-to-deep-learning/)

生成摘要时出错

---

## 85. Interference Pattern Formed in a Finger Gap Is Not Single Slit Diffraction

**原文标题**: Interference Pattern Formed in a Finger Gap Is Not Single Slit Diffraction

**原文链接**: [https://note.com/hydraenids/n/nbe89030deaba](https://note.com/hydraenids/n/nbe89030deaba)

生成摘要时出错

---

## 86. Breaking the spell of vibe coding

**原文标题**: Breaking the spell of vibe coding

**原文链接**: [https://www.fast.ai/posts/2026-01-28-dark-flow/](https://www.fast.ai/posts/2026-01-28-dark-flow/)

生成摘要时出错

---

## 87. A review of M Disc archival capability with long term testing results (2016)

**原文标题**: A review of M Disc archival capability with long term testing results (2016)

**原文链接**: [http://www.microscopy-uk.org.uk/mag/artsep16/mol-mdisc-review.html](http://www.microscopy-uk.org.uk/mag/artsep16/mol-mdisc-review.html)

生成摘要时出错

---

## 88. News publishers limit Internet Archive access due to AI scraping concerns

**原文标题**: News publishers limit Internet Archive access due to AI scraping concerns

**原文链接**: [https://www.niemanlab.org/2026/01/news-publishers-limit-internet-archive-access-due-to-ai-scraping-concerns/](https://www.niemanlab.org/2026/01/news-publishers-limit-internet-archive-access-due-to-ai-scraping-concerns/)

生成摘要时出错

---

## 89. One Server. Small Business

**原文标题**: One Server. Small Business

**原文链接**: [https://chodounsky.com/2026/02/14/one-server-small-business/](https://chodounsky.com/2026/02/14/one-server-small-business/)

生成摘要时出错

---

## 90. One Server. Small Business

**原文标题**: One Server. Small Business

**原文链接**: [https://chodounsky.com/2026/02/14/one-server-small-business/](https://chodounsky.com/2026/02/14/one-server-small-business/)

生成摘要时出错

---

## 91. AI Fails at 96% of (General Work) Jobs (New Study)

**原文标题**: AI Fails at 96% of (General Work) Jobs (New Study)

**原文链接**: [https://www.youtube.com/watch?v=z3kaLM8Oj4o](https://www.youtube.com/watch?v=z3kaLM8Oj4o)

生成摘要时出错

---

## 92. Shingles Vaccine Linked to Slower Biological Aging in Older Adults

**原文标题**: Shingles Vaccine Linked to Slower Biological Aging in Older Adults

**原文链接**: [https://gero.usc.edu/2026/01/19/shingles-vaccine-slower-biological-aging/](https://gero.usc.edu/2026/01/19/shingles-vaccine-slower-biological-aging/)

生成摘要时出错

---

## 93. An AI agent published a hit piece on me – more things have happened

**原文标题**: An AI agent published a hit piece on me – more things have happened

**原文链接**: [https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me-part-2/](https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me-part-2/)

生成摘要时出错

---

## 94. A practical guide to observing the night sky for real skies and real equipment

**原文标题**: A practical guide to observing the night sky for real skies and real equipment

**原文链接**: [https://stargazingbuddy.com/](https://stargazingbuddy.com/)

生成摘要时出错

---

## 95. An Enslaved Gardener Transformed the Pecan into a Cash Crop

**原文标题**: An Enslaved Gardener Transformed the Pecan into a Cash Crop

**原文链接**: [https://lithub.com/how-an-enslaved-gardener-transformed-the-pecan-into-a-cash-crop/](https://lithub.com/how-an-enslaved-gardener-transformed-the-pecan-into-a-cash-crop/)

生成摘要时出错

---

## 96. Show HN: Tanin – TUI Noise Generator

**原文标题**: Show HN: Tanin – TUI Noise Generator

**原文链接**: [https://github.com/AnonMiraj/Tanin](https://github.com/AnonMiraj/Tanin)

生成摘要时出错

---

## 97. How often do full-body MRIs find cancer?

**原文标题**: How often do full-body MRIs find cancer?

**原文链接**: [https://www.usatoday.com/story/life/health-wellness/2026/02/11/full-body-mris-cancer-aneurysm/88396037007/](https://www.usatoday.com/story/life/health-wellness/2026/02/11/full-body-mris-cancer-aneurysm/88396037007/)

生成摘要时出错

---

## 98. Build Gaussian Splat Experiences with SuperSplat Studio

**原文标题**: Build Gaussian Splat Experiences with SuperSplat Studio

**原文链接**: [https://blog.playcanvas.com/build-gaussian-splat-experiences-with-supersplat-studio/](https://blog.playcanvas.com/build-gaussian-splat-experiences-with-supersplat-studio/)

生成摘要时出错

---

## 99. Anthropic raises $30B in Series G funding at $380B post-money valuation

**原文标题**: Anthropic raises $30B in Series G funding at $380B post-money valuation

**原文链接**: [https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation)

生成摘要时出错

---

## 100. Guitars of the USSR and the Jolana Special in Azerbaijani Music (2012)

**原文标题**: Guitars of the USSR and the Jolana Special in Azerbaijani Music (2012)

**原文链接**: [https://caucascapades.wordpress.com/2012/06/14/guitars-of-the-ussr-and-the-jolana-special-in-azerbaijani-music/](https://caucascapades.wordpress.com/2012/06/14/guitars-of-the-ussr-and-the-jolana-special-in-azerbaijani-music/)

生成摘要时出错

---

