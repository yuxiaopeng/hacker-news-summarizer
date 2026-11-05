# Hacker News 热门文章摘要 (2026-11-05)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 面向所有人的 Kagi 搜索

**原文标题**: Kagi Search for Everyone

**原文链接**: [https://kagi.com/changelog](https://kagi.com/changelog)

Kagi 宣布其搜索引擎现在无需账号即可访问，任何人均可免费进行多达 50 次搜索（注册后可再获得 100 次额外额度）。此举旨在让这款无广告服务更易于向亲友推荐。

在开放访问权限的同时，Kagi 还对谷歌将 AI 工具与学校账户搜索捆绑的计划提出了批评，将自己定位为教育工作者的非企业化替代方案，服务于那些拒绝让搜索访问权被广告公司“绑架”的人群。

Kagi 生态系统发布了多项重大更新：

*   **Android 应用：** 采用原生 UI 元素进行了重大重新设计，重建了语音搜索功能，并新增了“快速回答”按钮。用户现在还可以通过直接将图片粘贴到搜索框来进行搜索。
*   **Kagi Assistant：** 语音输入经过全面改进，体验如打字般流畅，且 UI 现可清晰区分临时和永久线程。
*   **Kagi Translate：** 该服务现提供实时“润色”校正，并提高了包括库尔德语和拉丁语在内的多种语言的准确性。同时，它对 PDF 和 Office 文件的格式处理也更加完善。
*   **Kagi News：** 该应用近期在 Google Play 获得推荐，现已支持防止重复故事出现在不同类别中，并精简了设置选项。
*   **Small Web：** 增加了新主题（设计、商业、体育），并允许用户永久隐藏不感兴趣的主题。

更新最后列出了大量由社区驱动的错误修复，涵盖了从加拿大地区搜索准确性到维基百科小组件功能改进，以及网页和移动平台上的多项 UI 优化。

---

## 2. MS Paint 远程代码执行漏洞

**原文标题**: MS Paint Remote Code Execution Vulnerability

**原文链接**: [https://www.cve.org/CVERecord?id=CVE-2026-83844](https://www.cve.org/CVERecord?id=CVE-2026-83844)

所提供的文本并不包含漏洞本身的信息，而是一条技术错误提示，说明 CVE（常见漏洞与披露）网站需要启用 JavaScript 才能显示内容。

然而，根据标题“**MS Paint 远程代码执行漏洞**”，该文章可能指的是 **CVE-2023-36010**，这是在 Microsoft Paint 中发现的一个重大安全漏洞。以下是该漏洞的摘要：

**MS Paint RCE (CVE-2023-36010) 摘要**

*   **漏洞类型：** 这是一种远程代码执行（RCE）漏洞，被视为高风险漏洞，因为它允许攻击者在受害者的机器上运行未经授权的代码。
*   **威胁：** 当用户使用 Microsoft Paint 应用程序打开一个经特殊设计的恶意文件时，就会触发该漏洞。
*   **影响：** 如果攻击者成功利用此漏洞，他们可以获得与当前登录用户相同的权限。这可能允许他们安装程序、查看或删除敏感数据，或者创建具有完整用户权限的新账户。
*   **攻击向量：** 该攻击需要用户交互。攻击者通常会使用社会工程手段（如网络钓鱼邮件或恶意下载），诱导目标用户打开受感染的图像文件。
*   **解决方法：** 微软已发布官方安全补丁以修复此问题。建议用户尽快更新 Windows 操作系统，以确保 Paint 应用程序已应用最新的安全补丁。

若要查看 CVE 网站上的具体详情，您需要按照所提供文本的提示，在浏览器设置中启用 JavaScript。

---

## 3. sshole

**原文标题**: sshole

**原文链接**: [https://sshhole.com](https://sshhole.com)

生成摘要时出错

---

## 4. Alpine Linux 安全公告：OpenSSH-server 密码身份验证绕过

**原文标题**: Alpine Linux Security Advisory: OpenSSH-server password authentication bypass

**原文链接**: [https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/)

**Alpine Linux 安全公告摘要：OpenSSH-server 身份验证绕过漏洞**

2026年11月5日，Alpine Linux 报告了 `openssh-server` 中的一个严重漏洞，该漏洞允许攻击者绕过密码身份验证。通过发送经过特殊构造的长密码（257 至 1024 字节），攻击者可以在不知道实际密码的情况下获得账户访问权限。

**技术成因**
该问题出现在未集成 PAM（Alpine 的默认配置）的 OpenSSH 版本中。当 `sshd` 处理极长密码时，底层 `musl` C 库的 `crypt()` 函数会返回 `*` 作为错误指示符。如果目标账户在 `/etc/shadow` 文件中的密码字段也是 `*`（这是仅限密钥登录账户的标准设置），则字符串匹配成功，从而授予访问权限。此漏洞利用要求系统中至少有另一个账户拥有有效的 `$5$` 或 `$6$` 密码哈希值，以提供盐值（salt）。

**受影响系统**
如果同时满足以下所有条件，则系统极易受到攻击：
1. 运行标准的 Alpine `openssh-server`（不带 PAM）或设置了 `UsePAM no` 的 `openssh-server-pam`。
2. 启用了 `PasswordAuthentication`（默认配置）。
3. 目标账户的密码字段为 `*`（在云镜像的 `root` 和 `alpine` 用户中十分常见）。
4. 至少有一个本地账户拥有现代密码哈希值。

受影响的版本包括 Alpine 3.16 至 3.24 以及 edge 分支。

**修复建议**
1. **更新**：用户应立即运行 `apk upgrade -U -a` 来安装修复后的软件包（例如 v3.24.4、v3.23.8）。
2. **重启**：您**必须**重启 SSH 守护进程（`rc-service sshd restart`）才能使修复生效。
3. **缓解措施**：如果无法进行更新，请通过在 `sshd` 配置中设置 `PasswordAuthentication no` 来禁用密码登录。

**检测方法**
管理员应检查 `/var/log/messages` 中是否存在原本仅允许密钥登录的账户（如 `root` 或 `alpine`）的 “Accepted password” 条目。如果存在此类记录，则应视系统已被攻破。

---

## 5. 黑苹果重生

**原文标题**: The Hackintosh Reborn

**原文链接**: [https://www.naut.ca/blog/2026/11/05/the-hackintosh-reborn-with-ai/](https://www.naut.ca/blog/2026/11/05/the-hackintosh-reborn-with-ai/)

本文背景设定在2026年11月，作者探讨了“黑苹果”（Hackintosh）运动出人意料的复兴。此前，随着苹果转向ARM架构以及macOS 27 (Golden Gate) 正式终止对x86的支持，社区曾预感末日将至，但AI辅助开发的崛起却引发了一场显著的“重生”。

作者指出，Claude Code、OpenAI Codex等AI工具以及集成了AI的反向工程工具（如Ghidra），彻底改变了将苹果软件移植到非苹果硬件的能力。这些技术降低了准入门槛，让即使是新手开发者也能在无需手动编写代码的情况下，开发出功能性应用和解决方案。

文中引用的近期重大突破包括：
*   **macOS 27** 在骁龙（Snapdragon）笔记本电脑和基于ARM架构的单板计算机（RK3588）上运行。
*   **iOS 17** 成功移植到 Nintendo Switch OLED。
*   通过 “nullmoth” 等新工具实现对 **NVIDIA 50系列显卡**的支持。
*   成功将仅限ARM架构的 macOS 27 重新转译回 **x86架构**。

文章最后总结道，尽管苹果的生态系统正变得愈发封闭，但AI为硬件爱好者提供了一线生机。通过自动化处理复杂的兼容性任务，AI正赋予用户重新掌控硬件的能力，并让在多元平台上运行macOS的传统得以延续。

---

## 6. Tencent Launches Hy4, One of the Leading Open-Source AI Models

**原文标题**: Tencent Launches Hy4, One of the Leading Open-Source AI Models

**原文链接**: [https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/](https://www.tencent.com/tencent-launches-hy4-joining-the-ranks-of-the-worlds-leading-open-source-ai-models/)

生成摘要时出错

---

## 7. 窗户毛衣

**原文标题**: Window Sweaters

**原文链接**: [https://github.com/saragordic/window-sweaters](https://github.com/saragordic/window-sweaters)

**Window Sweaters** 是一款精致的 macOS 装饰应用，旨在为窗口边框营造出一种“温馨”的针织美学。该应用由 Sara Gordic 开发，能为窗口添加色彩丰富、极具质感的边框，并为 Safari、Notion、Slack 和 VS Code 等 37 款常用应用提供了精心挑选的定制配色方案。对于暂不支持的应用，软件会动态采样应用图标的颜色，以生成锯齿、野餐格或闪烁等匹配图案。

**核心功能与自定义：**
用户可以通过菜单栏图标控制应用，包括开关特定应用的边框、调整针脚大小、更换图案或暂停效果。高级用户还可以通过编辑配置文件（`apps.conf`）或在 Application Support 文件夹中添加自定义 PNG 图表来创建独特的编织图案，进一步实现个性化体验。

**安装与技术细节：**
该应用可以通过 Homebrew 安装，也可以从 GitHub 下载最新的 ZIP 包或通过源码构建。由于该应用尚未经过 Apple 公证，用户可能需要在“系统设置”中手动批准运行。此外，它需要“辅助功能”权限才能准确追踪窗口焦点。

**兼容性：**
Window Sweaters 基于 Felix Kratz 的 *JankyBorders* 开发，是一款开源软件（GPL-3.0）。它专为 macOS 13 及更高版本设计，同时支持 Intel 和 Apple Silicon 芯片。虽然应用目前功能正常，但开发者指出其仍处于“开发中”阶段，这意味着在调整窗口大小时边框可能会暂时消失，且未来的 macOS 更新可能会影响其对私有窗口 API 的使用。

---

## 8. 来自 Salon 的告别

**原文标题**: Goodbye from Salon

**原文链接**: [https://www.salon.com/2026/11/05/goodbye-from-salon/](https://www.salon.com/2026/11/05/goodbye-from-salon/)

在历经31年的出版历程后，先驱数字媒体《沙龙》（Salon）宣布将于2026年11月5日停止运营。

《沙龙》成立于1995年11月的互联网早期，是数字原生新闻领域的开拓者。该刊物通过融合政治、文化和社会评论，形成了独特的风格，旨在利用网络以创新方式将新闻报道与读者联系起来。在其历史长河中，该网站始终致力于审视权力结构、质疑社会假设，并为被忽视的观点提供平台。

关闭的决定源于独立数字媒体日益艰难且不断变化的商业环境。公告指出，经过慎重考虑，该机构认定其出版模式在当前的经济气候下已无法持续。

在告别声明中，《沙龙》向三十年来塑造该刊物的创始人、员工和撰稿人表达了深切的谢意。最重要的是，它感谢了忠实读者群的参与、订阅以及对这个“思想至上”社区的坚守。

尽管该刊物即将画上句号，但其领导层强调，他们为这31年的历程感到自豪，并坚称《沙龙》帮助定义了数字新闻的发展方向。告别辞最后表示，希望该网站在促进有意义的对话和原创报道方面留下的遗产，在关闭后仍将长期影响媒体格局。

---

## 9. 博客的成本

**原文标题**: The Cost of Blogging

**原文链接**: [https://onlinegoddess.net/2026/11/the-cost-of-blogging/](https://onlinegoddess.net/2026/11/the-cost-of-blogging/)

In “The Cost of Blogging,” author Becky discusses the specific areas where she chooses to invest money in her personal blog despite the availability of free alternatives. She outlines four primary categories of expenditure:

*   **Personal Domains:** Becky considers a domain an essential investment. It establishes a permanent online identity, ensures portability between platforms, and signals a commitment to readers that the blog is here to stay.
*   **Hosting and Platforms:** Paying for a platform (like Bear) ensures data privacy, as the service is funded by subscriptions rather than data collection. Becky also notes that paying for a pro tier helps sustain free options for those who cannot afford them.
*   **Typography:** As a typography enthusiast, she occasionally purchases premium font families (up to a £100 limit). She also advocates for self-hosting free fonts to avoid third-party tracking from providers like Google.
*   **Writing Software:** While basic editors are often included with blogging platforms, Becky prefers paying for dedicated Markdown editors (such as Paper) that offer better interfaces and deeper personalization.

The post concludes with community feedback. Readers echo Becky’s sentiments, noting that small costs—such as a $12 annual domain fee or a $6 monthly platform subscription—are worthwhile for the quality and ownership they provide. The author encourages other bloggers to share their own “worth it” expenses, fostering a conversation about the sustainability and ethics of personal publishing.

---

## 10. Motorola Signature 27 with GrapheneOS support

**原文标题**: Motorola Signature 27 with GrapheneOS support

**原文链接**: [https://motorolanews.com/motorola-signature-27-2/](https://motorolanews.com/motorola-signature-27-2/)

生成摘要时出错

---

## 11. Launch HN: Rivet (YC W23) – Scale and Orchestrate Agents on S3

**原文标题**: Launch HN: Rivet (YC W23) – Scale and Orchestrate Agents on S3

**原文链接**: [https://github.com/rivet-dev/rivet](https://github.com/rivet-dev/rivet)

生成摘要时出错

---

## 12. My psychophysics as a bilateral cochlear implant user

**原文标题**: My psychophysics as a bilateral cochlear implant user

**原文链接**: [https://claude.ai/artifact/L8qsMc3SorytGW3LA81nYf](https://claude.ai/artifact/L8qsMc3SorytGW3LA81nYf)

生成摘要时出错

---

## 13. September in Servo: <progress>, rounded rectangles, and more

**原文标题**: September in Servo: <progress>, rounded rectangles, and more

**原文链接**: [https://servo.org/blog/2026/11/05/september-in-servo/](https://servo.org/blog/2026/11/05/september-in-servo/)

生成摘要时出错

---

## 14. $2.5T has been wiped from US stocks

**原文标题**: $2.5T has been wiped from US stocks

**原文链接**: [https://finlaws.substack.com/p/25t-has-been-wiped-from-us-stocks](https://finlaws.substack.com/p/25t-has-been-wiped-from-us-stocks)

生成摘要时出错

---

## 15. Download your favourite YouTube videos

**原文标题**: Download your favourite YouTube videos

**原文链接**: [https://criminallyvulgar.dev/you-should-absolutely-download-your-favourite-youtube-videos/](https://criminallyvulgar.dev/you-should-absolutely-download-your-favourite-youtube-videos/)

生成摘要时出错

---

## 16. Claude Code sends your email address to websites

**原文标题**: Claude Code sends your email address to websites

**原文链接**: [https://github.com/anthropics/claude-code/issues/107757](https://github.com/anthropics/claude-code/issues/107757)

生成摘要时出错

---

## 17. Bild AI (YC W25) Is Hiring Founding Product Engineers

**原文标题**: Bild AI (YC W25) Is Hiring Founding Product Engineers

**原文链接**: [https://www.ycombinator.com/companies/bild-ai/jobs](https://www.ycombinator.com/companies/bild-ai/jobs)

生成摘要时出错

---

## 18. I wish tech companies knew more about me

**原文标题**: I wish tech companies knew more about me

**原文链接**: [https://rakhim.exotext.com/i-wish-tech-companies-knew-more-about-me](https://rakhim.exotext.com/i-wish-tech-companies-knew-more-about-me)

生成摘要时出错

---

## 19. OpenSSH 10.6p2 Critical workaround for alpine without PAM

**原文标题**: OpenSSH 10.6p2 Critical workaround for alpine without PAM

**原文链接**: [https://www.openssh.org/releasenotes.html#10.6p2](https://www.openssh.org/releasenotes.html#10.6p2)

生成摘要时出错

---

## 20. Show HN: A decent text-to-image model trained for ~$20K (Apache 2.0 Weights)

**原文标题**: Show HN: A decent text-to-image model trained for ~$20K (Apache 2.0 Weights)

**原文链接**: [https://www.linum.ai/field-notes/pjit-21k](https://www.linum.ai/field-notes/pjit-21k)

生成摘要时出错

---

## 21. Obscure audio codec is a perfect fit for the N64

**原文标题**: Obscure audio codec is a perfect fit for the N64

**原文链接**: [https://phoboslab.org/log/2026/11/n64-ulc-codec](https://phoboslab.org/log/2026/11/n64-ulc-codec)

生成摘要时出错

---

## 22. Introducing Pangram Image 1.0

**原文标题**: Introducing Pangram Image 1.0

**原文链接**: [https://www.pangram.com/blog/introducing-pangram-image-1-0](https://www.pangram.com/blog/introducing-pangram-image-1-0)

生成摘要时出错

---

## 23. The Stacks Project, Formalized in Lean

**原文标题**: The Stacks Project, Formalized in Lean

**原文链接**: [https://axiommath.ai/research/the-stacks-project-formalized/](https://axiommath.ai/research/the-stacks-project-formalized/)

生成摘要时出错

---

## 24. MCP Explained

**原文标题**: MCP Explained

**原文链接**: [https://mcp-explained.com/](https://mcp-explained.com/)

生成摘要时出错

---

## 25. The Lisp curse, now coming to your ecosystem

**原文标题**: The Lisp curse, now coming to your ecosystem

**原文链接**: [https://javahippie.net/programming/llm/2026/03/05/the-lisp-curse-coming-to-your-ecosystem.html](https://javahippie.net/programming/llm/2026/03/05/the-lisp-curse-coming-to-your-ecosystem.html)

生成摘要时出错

---

## 26. GPT-6 Astra covertly underperforms on safety research

**原文标题**: GPT-6 Astra covertly underperforms on safety research

**原文链接**: [https://alignment.openai.com/misalignment-reports/covert-underperformance-on-safety-research-tasks/](https://alignment.openai.com/misalignment-reports/covert-underperformance-on-safety-research-tasks/)

生成摘要时出错

---

## 27. Show HN: Stroq – a local audit of what your coding agent did and why

**原文标题**: Show HN: Stroq – a local audit of what your coding agent did and why

**原文链接**: [https://github.com/AGGIB/Stroq](https://github.com/AGGIB/Stroq)

生成摘要时出错

---

## 28. Hungary: Communist-era files released, up to 60k former agents revealed

**原文标题**: Hungary: Communist-era files released, up to 60k former agents revealed

**原文链接**: [https://www.euronews.com/2026/11/04/hungary-communist-era-files-opened-up-to-60000-former-agents-revealed](https://www.euronews.com/2026/11/04/hungary-communist-era-files-opened-up-to-60000-former-agents-revealed)

生成摘要时出错

---

## 29. We can do better than line-buffered output

**原文标题**: We can do better than line-buffered output

**原文链接**: [https://nullprogram.com/blog/2026/11/05/](https://nullprogram.com/blog/2026/11/05/)

生成摘要时出错

---

## 30. Baidu released ERNIE 5.5 Flash Base

**原文标题**: Baidu released ERNIE 5.5 Flash Base

**原文链接**: [https://ernie.baidu.com/release/ernie-5-5-flash-base/](https://ernie.baidu.com/release/ernie-5-5-flash-base/)

生成摘要时出错

---

## 31. Discord is ditching Electron and its new app uses less RAM

**原文标题**: Discord is ditching Electron and its new app uses less RAM

**原文链接**: [https://www.theverge.com/news/1027379/discord-ditching-electron-web-app](https://www.theverge.com/news/1027379/discord-ditching-electron-web-app)

生成摘要时出错

---

## 32. Building a Multi-Agent System from Scratch: Architecture Patterns

**原文标题**: Building a Multi-Agent System from Scratch: Architecture Patterns

**原文链接**: [https://kadhar.dev/blog/multi-agent-systems-from-scratch](https://kadhar.dev/blog/multi-agent-systems-from-scratch)

生成摘要时出错

---

## 33. TextEdit vs. Pages

**原文标题**: TextEdit vs. Pages

**原文链接**: [https://leancrew.com/all-this/2026/10/textedit-vs-pages/](https://leancrew.com/all-this/2026/10/textedit-vs-pages/)

生成摘要时出错

---

## 34. Nasdaq plummets 4% into correction territory

**原文标题**: Nasdaq plummets 4% into correction territory

**原文链接**: [https://www.cnbc.com/2026/11/04/stock-market-today-live-updates.html](https://www.cnbc.com/2026/11/04/stock-market-today-live-updates.html)

生成摘要时出错

---

## 35. So my ISP was hijacking my DNS

**原文标题**: So my ISP was hijacking my DNS

**原文链接**: [https://www.karthihegde.dev/posts/dns_tampering](https://www.karthihegde.dev/posts/dns_tampering)

生成摘要时出错

---

## 36. Nordstjernen, Northstar, Southstar: minimalist webbrowsers in C and Rust

**原文标题**: Nordstjernen, Northstar, Southstar: minimalist webbrowsers in C and Rust

**原文链接**: [https://nordstjernen.org/](https://nordstjernen.org/)

生成摘要时出错

---

## 37. Chip stocks get slaughtered as Wall Street in worst post-midterm day since 1896

**原文标题**: Chip stocks get slaughtered as Wall Street in worst post-midterm day since 1896

**原文链接**: [https://finance.yahoo.com/markets/article/chip-stocks-get-slaughtered-as-wall-street-heads-for-its-worst-post-midterm-day-since-1896-163413900.html](https://finance.yahoo.com/markets/article/chip-stocks-get-slaughtered-as-wall-street-heads-for-its-worst-post-midterm-day-since-1896-163413900.html)

生成摘要时出错

---

## 38. Awesome repositories are no longer awesome

**原文标题**: Awesome repositories are no longer awesome

**原文链接**: [https://erikgahner.github.io/posts/2026/awesome-repositories-are-no-longer-awesome/](https://erikgahner.github.io/posts/2026/awesome-repositories-are-no-longer-awesome/)

生成摘要时出错

---

## 39. How to Lie With Statistics (1954)

**原文标题**: How to Lie With Statistics (1954)

**原文链接**: [https://archive.org/details/howtoliewithstat00huff](https://archive.org/details/howtoliewithstat00huff)

生成摘要时出错

---

## 40. Being a kid making games in the early 2000s

**原文标题**: Being a kid making games in the early 2000s

**原文链接**: [https://jaytholen.net/teengamedev/](https://jaytholen.net/teengamedev/)

生成摘要时出错

---

## 41. Partial Operator Precedence

**原文标题**: Partial Operator Precedence

**原文链接**: [https://ziglang.org/devlog/2026/#2026-10-24](https://ziglang.org/devlog/2026/#2026-10-24)

生成摘要时出错

---

## 42. Starfall – Affordable, routine access to microgravity

**原文标题**: Starfall – Affordable, routine access to microgravity

**原文链接**: [https://www.spacex.com/starfall](https://www.spacex.com/starfall)

生成摘要时出错

---

## 43. Spreading Liquid with Three.js

**原文标题**: Spreading Liquid with Three.js

**原文链接**: [https://mofu-dev.com/en/blog/fluid-foundation/](https://mofu-dev.com/en/blog/fluid-foundation/)

生成摘要时出错

---

## 44. California Gov Newsom commutes death sentences for all 548 people on death row

**原文标题**: California Gov Newsom commutes death sentences for all 548 people on death row

**原文链接**: [https://www.bbc.com/news/articles/cqrkyyd2j8mvo](https://www.bbc.com/news/articles/cqrkyyd2j8mvo)

生成摘要时出错

---

## 45. OCAP Bounded Authority: Edera's Managed Approach to Object Capabilities

**原文标题**: OCAP Bounded Authority: Edera's Managed Approach to Object Capabilities

**原文链接**: [https://edera.dev/stories/ocap-bounded-authority](https://edera.dev/stories/ocap-bounded-authority)

生成摘要时出错

---

## 46. AI is forcing us to pay off 40 years of technical debt

**原文标题**: AI is forcing us to pay off 40 years of technical debt

**原文链接**: [https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability](https://spectrum.ieee.org/ai-in-cybersecurity-php2shell-vulnerability)

生成摘要时出错

---

## 47. Infant Bleeding Surged as Parents Rejected Vitamin K Shots, Studies Find

**原文标题**: Infant Bleeding Surged as Parents Rejected Vitamin K Shots, Studies Find

**原文链接**: [https://www.nytimes.com/2026/11/05/well/live/vitamin-k-shot-newborn-bleeding.html](https://www.nytimes.com/2026/11/05/well/live/vitamin-k-shot-newborn-bleeding.html)

生成摘要时出错

---

## 48. Lemmings CSS Animation

**原文标题**: Lemmings CSS Animation

**原文链接**: [https://markblah.github.io/lemmings/](https://markblah.github.io/lemmings/)

生成摘要时出错

---

## 49. Offline survival assistant – local LLM and Kiwix, runs from a USB stick

**原文标题**: Offline survival assistant – local LLM and Kiwix, runs from a USB stick

**原文链接**: [https://github.com/sdalberto/ia-da-sobrevivencia/blob/main/README.en.md](https://github.com/sdalberto/ia-da-sobrevivencia/blob/main/README.en.md)

生成摘要时出错

---

## 50. 80k Hops per Second Measurement Confirm Starlink Up/Downlink Channel Pairing

**原文标题**: 80k Hops per Second Measurement Confirm Starlink Up/Downlink Channel Pairing

**原文链接**: [https://sdr-x.github.io/starlink-ul-dl-pair-80k-hop-ad9361/](https://sdr-x.github.io/starlink-ul-dl-pair-80k-hop-ad9361/)

生成摘要时出错

---

## 51. Vibe Coding Keypad

**原文标题**: Vibe Coding Keypad

**原文链接**: [https://www.keychron.com/products/keychron-f4-he-8k-vibe-coding-keypad](https://www.keychron.com/products/keychron-f4-he-8k-vibe-coding-keypad)

生成摘要时出错

---

## 52. Exporting tables from a SQL Server backup (.bak) to Parquet without restoring it

**原文标题**: Exporting tables from a SQL Server backup (.bak) to Parquet without restoring it

**原文链接**: [https://blog.arpe.io/fastbcp-1-6-export-sql-server-backup-to-parquet](https://blog.arpe.io/fastbcp-1-6-export-sql-server-backup-to-parquet)

生成摘要时出错

---

## 53. The architecture of open-weight LLMs: MoE, hybrid layers, ternary weights

**原文标题**: The architecture of open-weight LLMs: MoE, hybrid layers, ternary weights

**原文链接**: [https://www.silasdata.com/llm-playground-inside-architectures/](https://www.silasdata.com/llm-playground-inside-architectures/)

生成摘要时出错

---

## 54. Altera Announces Agilex 2X, a Complete FPGA and SoC Portfolio

**原文标题**: Altera Announces Agilex 2X, a Complete FPGA and SoC Portfolio

**原文链接**: [https://www.altera.com/newsroom/agilex-2x](https://www.altera.com/newsroom/agilex-2x)

生成摘要时出错

---

## 55. Wipeout for AI stocks sends Wall Street reeling and S&P 500 tumbles more than 3%

**原文标题**: Wipeout for AI stocks sends Wall Street reeling and S&P 500 tumbles more than 3%

**原文链接**: [https://apnews.com/article/stocks-markets-ai-midterm-oil-trump-7ee9c212805aa5e70cf34d25aab7a36e](https://apnews.com/article/stocks-markets-ai-midterm-oil-trump-7ee9c212805aa5e70cf34d25aab7a36e)

生成摘要时出错

---

## 56. Nyquist Limit:The frequency of changes in tech is invalidating our understanding

**原文标题**: Nyquist Limit:The frequency of changes in tech is invalidating our understanding

**原文链接**: [https://www.ryanprior.com/posts/nyquist-limit-frequency-of-changes-in-tech-invalidates-understanding/](https://www.ryanprior.com/posts/nyquist-limit-frequency-of-changes-in-tech-invalidates-understanding/)

生成摘要时出错

---

## 57. An updated Model Spec for more capable and beneficial AI

**原文标题**: An updated Model Spec for more capable and beneficial AI

**原文链接**: [https://openai.com/index/updated-model-spec/](https://openai.com/index/updated-model-spec/)

生成摘要时出错

---

## 58. GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents

**原文标题**: GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents

**原文链接**: [https://openai.com/index/introducing-gpt-6-cyber/](https://openai.com/index/introducing-gpt-6-cyber/)

生成摘要时出错

---

## 59. A thousand fewer paths to root

**原文标题**: A thousand fewer paths to root

**原文链接**: [https://openai.com/index/a-thousand-fewer-paths-to-root/](https://openai.com/index/a-thousand-fewer-paths-to-root/)

生成摘要时出错

---

## 60. A wave of plastic-free coffee pods and machines

**原文标题**: A wave of plastic-free coffee pods and machines

**原文链接**: [https://www.cnn.com/2026/11/02/food/coffee-machine-plastic-free](https://www.cnn.com/2026/11/02/food/coffee-machine-plastic-free)

生成摘要时出错

---

## 61. Kimi K3.1 Pro model weights are out

**原文标题**: Kimi K3.1 Pro model weights are out

**原文链接**: [https://huggingface.co/moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)

生成摘要时出错

---

## 62. Moment of Ruby: An Argument for Nothing

**原文标题**: Moment of Ruby: An Argument for Nothing

**原文链接**: [https://www.aha.io/engineering/articles/moment-of-ruby-an-argument-for-nothing](https://www.aha.io/engineering/articles/moment-of-ruby-an-argument-for-nothing)

生成摘要时出错

---

## 63. Images 2.6

**原文标题**: Images 2.6

**原文链接**: [https://openai.com/index/introducing-images-2-6/](https://openai.com/index/introducing-images-2-6/)

生成摘要时出错

---

## 64. Newsom Commutes the Sentences of California's 548 Death Row Inmates

**原文标题**: Newsom Commutes the Sentences of California's 548 Death Row Inmates

**原文链接**: [https://www.nytimes.com/2026/11/05/us/california-death-row-newsom-commutation.html](https://www.nytimes.com/2026/11/05/us/california-death-row-newsom-commutation.html)

生成摘要时出错

---

## 65. I turned 100 old science fiction books into a database of 6,222 startup ideas

**原文标题**: I turned 100 old science fiction books into a database of 6,222 startup ideas

**原文链接**: [https://www.reddit.com/r/SideProject/comments/1xly9r8/i_turned_100_old_science_fiction_books_into_a/](https://www.reddit.com/r/SideProject/comments/1xly9r8/i_turned_100_old_science_fiction_books_into_a/)

生成摘要时出错

---

## 66. 'It's just vape, nail, charity shops': Can anything save UK high street?

**原文标题**: 'It's just vape, nail, charity shops': Can anything save UK high street?

**原文链接**: [https://www.theguardian.com/business/2026/nov/04/what-can-save-the-british-high-street-rotherham](https://www.theguardian.com/business/2026/nov/04/what-can-save-the-british-high-street-rotherham)

生成摘要时出错

---

## 67. Future Maintenance of Mbed TLS

**原文标题**: Future Maintenance of Mbed TLS

**原文链接**: [https://lists.trustedfirmware.org/archives/list/mbed-tls@lists.trustedfirmware.org/thread/YPIGCB7WN6GCHOGEGKOJXUYAP7OK527W/](https://lists.trustedfirmware.org/archives/list/mbed-tls@lists.trustedfirmware.org/thread/YPIGCB7WN6GCHOGEGKOJXUYAP7OK527W/)

生成摘要时出错

---

## 68. Image of our satellite-choked night skies

**原文标题**: Image of our satellite-choked night skies

**原文链接**: [https://kottke.org/26/11/stunning-image-of-our-satellite-choked-night-skies](https://kottke.org/26/11/stunning-image-of-our-satellite-choked-night-skies)

生成摘要时出错

---

## 69. Mizu – zero-copy parallel R and Python over shared memory

**原文标题**: Mizu – zero-copy parallel R and Python over shared memory

**原文链接**: [https://github.com/shikokuchuo/pymizu](https://github.com/shikokuchuo/pymizu)

生成摘要时出错

---

## 70. OpenSSH 10.6p2 has been released with a workaround for a critical vulnerability

**原文标题**: OpenSSH 10.6p2 has been released with a workaround for a critical vulnerability

**原文链接**: [https://hachyderm.io/@damienmiller/117563026759098135](https://hachyderm.io/@damienmiller/117563026759098135)

生成摘要时出错

---

## 71. Paraguayan president impeached minutes after resigning following bank collapse

**原文标题**: Paraguayan president impeached minutes after resigning following bank collapse

**原文链接**: [https://apnews.com/article/ueno-bank-collapse-paraguay-banking-crisis-santiago-pena-impeachment-eccea1c9a64808b5cd7e6e1d5542084f](https://apnews.com/article/ueno-bank-collapse-paraguay-banking-crisis-santiago-pena-impeachment-eccea1c9a64808b5cd7e6e1d5542084f)

生成摘要时出错

---

## 72. Mystery Seller Seeks to Dump $500M of Data Center Loans

**原文标题**: Mystery Seller Seeks to Dump $500M of Data Center Loans

**原文链接**: [https://www.bloomberg.com/news/articles/2026-11-05/mystery-seller-puts-up-500-million-data-center-loans-backing-stargate-cyrusone](https://www.bloomberg.com/news/articles/2026-11-05/mystery-seller-puts-up-500-million-data-center-loans-backing-stargate-cyrusone)

生成摘要时出错

---

## 73. Paraguay bank collapses with half of population's savings

**原文标题**: Paraguay bank collapses with half of population's savings

**原文链接**: [https://www.aljazeera.com/video/newsfeed/2026/11/5/paraguay-bank-collapses-with-half-of-populations-savings](https://www.aljazeera.com/video/newsfeed/2026/11/5/paraguay-bank-collapses-with-half-of-populations-savings)

生成摘要时出错

---

## 74. Show HN: TubeHaus – an open-source YouTube client with no Google account

**原文标题**: Show HN: TubeHaus – an open-source YouTube client with no Google account

**原文链接**: [https://github.com/biolend83/tubehaus](https://github.com/biolend83/tubehaus)

生成摘要时出错

---

## 75. Ripple-65B Preview: U.S. Open-Weight SOTA on Agentic Coding

**原文标题**: Ripple-65B Preview: U.S. Open-Weight SOTA on Agentic Coding

**原文链接**: [https://www.ricursive.com/ripple](https://www.ricursive.com/ripple)

生成摘要时出错

---

## 76. Basically no one is using AI agents for their DoorDash orders

**原文标题**: Basically no one is using AI agents for their DoorDash orders

**原文链接**: [https://arstechnica.com/ai/2026/10/doordash-says-outside-ai-agents-have-only-led-to-hundreds-of-orders-so-far/](https://arstechnica.com/ai/2026/10/doordash-says-outside-ai-agents-have-only-led-to-hundreds-of-orders-so-far/)

生成摘要时出错

---

## 77. Nasdaq Sinks 5% as Investors Retreat from AI Trade After Election

**原文标题**: Nasdaq Sinks 5% as Investors Retreat from AI Trade After Election

**原文链接**: [https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-05-2026](https://www.wsj.com/livecoverage/stock-market-today-dow-sp-500-nasdaq-11-05-2026)

生成摘要时出错

---

## 78. Z.ai says GLM 5.5 built on 1T web pages

**原文标题**: Z.ai says GLM 5.5 built on 1T web pages

**原文链接**: [https://twitter.com/bebuu_ai/status/2118052769856888892](https://twitter.com/bebuu_ai/status/2118052769856888892)

生成摘要时出错

---

## 79. A new Go API for JSON

**原文标题**: A new Go API for JSON

**原文链接**: [https://go.dev/blog/jsonv2](https://go.dev/blog/jsonv2)

生成摘要时出错

---

## 80. Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux

**原文标题**: Nvidia RTX Spark encrypted firmware slows inference speed to 35% on Linux

**原文链接**: [https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop](https://www.mindstudio.ai/blog/linux-nvidia-rtx-spark-laptop)

生成摘要时出错

---

## 81. My gym forced a social media down my throat. So I reverse-engineered its app

**原文标题**: My gym forced a social media down my throat. So I reverse-engineered its app

**原文链接**: [https://shayon.work/blog/reverse-engineering-gym-pass](https://shayon.work/blog/reverse-engineering-gym-pass)

生成摘要时出错

---

## 82. AMD expects to outsell Intel in Q4 for the first time in history

**原文标题**: AMD expects to outsell Intel in Q4 for the first time in history

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/amd-expects-to-outsell-intel-in-q4-for-the-first-time-in-history-usd17b-guidance-would-exceed-intels-projections](https://www.tomshardware.com/pc-components/cpus/amd-expects-to-outsell-intel-in-q4-for-the-first-time-in-history-usd17b-guidance-would-exceed-intels-projections)

生成摘要时出错

---

## 83. TScert: A Sound Core for TypeScript

**原文标题**: TScert: A Sound Core for TypeScript

**原文链接**: [https://github.com/cristianoc/TScert](https://github.com/cristianoc/TScert)

生成摘要时出错

---

## 84. GPT-6 Cyber

**原文标题**: GPT-6 Cyber

**原文链接**: [https://twitter.com/OpenAI/status/2118390190246879554](https://twitter.com/OpenAI/status/2118390190246879554)

生成摘要时出错

---

## 85. Residential proxies detected on White House network

**原文标题**: Residential proxies detected on White House network

**原文链接**: [https://layer3intel.com/blog/residential-proxies-white-house-network](https://layer3intel.com/blog/residential-proxies-white-house-network)

生成摘要时出错

---

## 86. YC's Garry Tan uses AI agents so much, he spends up to $200K a year on tokens

**原文标题**: YC's Garry Tan uses AI agents so much, he spends up to $200K a year on tokens

**原文链接**: [https://techcrunch.com/2026/11/02/y-combinators-garry-tan-uses-ai-agents-so-much-he-spends-up-to-200k-a-year-on-tokens/](https://techcrunch.com/2026/11/02/y-combinators-garry-tan-uses-ai-agents-so-much-he-spends-up-to-200k-a-year-on-tokens/)

生成摘要时出错

---

## 87. Paraguay seizes major digital bank tied to president, leaving customers in limbo

**原文标题**: Paraguay seizes major digital bank tied to president, leaving customers in limbo

**原文链接**: [https://apnews.com/article/paraguay-ueno-digital-bank-seizure-santiago-pena-9d7521ddee45a185d2618c7e09a243a3](https://apnews.com/article/paraguay-ueno-digital-bank-seizure-santiago-pena-9d7521ddee45a185d2618c7e09a243a3)

生成摘要时出错

---

## 88. Insects don't swarm at LED lights

**原文标题**: Insects don't swarm at LED lights

**原文链接**: [https://www.birdsoutsidemywindow.org/2026/11/03/insects-dont-swarm-at-led-lights/](https://www.birdsoutsidemywindow.org/2026/11/03/insects-dont-swarm-at-led-lights/)

生成摘要时出错

---

## 89. North Korean fake job interview led to $6.3B Binance heist

**原文标题**: North Korean fake job interview led to $6.3B Binance heist

**原文链接**: [https://www.theregister.com/security/2026/11/03/north-korean-fake-job-interview-led-to-63b-binance-heist/5307398](https://www.theregister.com/security/2026/11/03/north-korean-fake-job-interview-led-to-63b-binance-heist/5307398)

生成摘要时出错

---

## 90. From 25M instructions to one faulty skip: fault analysis of a secure boot

**原文标题**: From 25M instructions to one faulty skip: fault analysis of a secure boot

**原文链接**: [https://www.eshard.com/blog/one-faulty-skip-secure-boot](https://www.eshard.com/blog/one-faulty-skip-secure-boot)

生成摘要时出错

---

## 91. Tobacco company got smoked by leaving secret recipes on a file share

**原文标题**: Tobacco company got smoked by leaving secret recipes on a file share

**原文链接**: [https://www.theregister.com/security/2026/11/05/tobacco-company-got-smoked-by-leaving-secret-recipes-on-a-file-share/5307704](https://www.theregister.com/security/2026/11/05/tobacco-company-got-smoked-by-leaving-secret-recipes-on-a-file-share/5307704)

生成摘要时出错

---

## 92. Conductor is joining Meta

**原文标题**: Conductor is joining Meta

**原文链接**: [https://www.conductor.build/announcement](https://www.conductor.build/announcement)

生成摘要时出错

---

## 93. Sony Debuts Retro $60 Wired Headphones in Tribute to 1979 Walkman

**原文标题**: Sony Debuts Retro $60 Wired Headphones in Tribute to 1979 Walkman

**原文链接**: [https://www.bloomberg.com/news/articles/2026-11-05/sony-debuts-retro-60-wired-headphones-in-tribute-to-1979-walkman](https://www.bloomberg.com/news/articles/2026-11-05/sony-debuts-retro-60-wired-headphones-in-tribute-to-1979-walkman)

生成摘要时出错

---

## 94. Replacing homepage demo media with looping HTML and CSS

**原文标题**: Replacing homepage demo media with looping HTML and CSS

**原文链接**: [https://stepshots.com/css-feature-clips](https://stepshots.com/css-feature-clips)

生成摘要时出错

---

## 95. Epileptic seizures nearly vanish after people receive experimental gene therapy

**原文标题**: Epileptic seizures nearly vanish after people receive experimental gene therapy

**原文链接**: [https://www.nature.com/articles/d41586-026-03566-2](https://www.nature.com/articles/d41586-026-03566-2)

生成摘要时出错

---

## 96. Guerrilla bike lanes: San Francisco makes illicit infrastructure permanent (2016)

**原文标题**: Guerrilla bike lanes: San Francisco makes illicit infrastructure permanent (2016)

**原文链接**: [https://99percentinvisible.org/article/guerrilla-bike-lanes-san-francisco-makes-illicit-infrastructure-permanent/](https://99percentinvisible.org/article/guerrilla-bike-lanes-san-francisco-makes-illicit-infrastructure-permanent/)

生成摘要时出错

---

## 97. Your Cryptography Conspiracy Theory Is Wrong

**原文标题**: Your Cryptography Conspiracy Theory Is Wrong

**原文链接**: [https://soatok.blog/2026/10/29/your-cryptography-conspiracy-theory-is-wrong/](https://soatok.blog/2026/10/29/your-cryptography-conspiracy-theory-is-wrong/)

生成摘要时出错

---

## 98. Show HN: After a decade of reversing, I got co-op working in DOS Wing Commander

**原文标题**: Show HN: After a decade of reversing, I got co-op working in DOS Wing Commander

**原文链接**: [https://fireflyk64.github.io/wcmulti/](https://fireflyk64.github.io/wcmulti/)

This article chronicles a decade-long technical project to add a cooperative multiplayer mode to the original DOS version of *Wing Commander*. The project progressed through several stages of reverse engineering, from simple memory manipulation to complex function hooking and networking.

**Memory Analysis and Position Tracking**
The author began by using DOSBox’s debugging tools to dump the game's 640K memory. By comparing memory snapshots taken during different states (e.g., stationary vs. moving forward), they isolated the specific memory addresses within the data segment that governed the player’s X, Y, and Z coordinates, velocity, and orientation vectors.

**Function Hooking via "Trampolines"**
To handle complex actions like firing lasers or calculating damage, the author realized that simple memory writes were insufficient. They developed a "trampoline" system that hijacked a "dead" string in the game’s memory to serve as an injection point for code. By pushing the current instruction pointer to the stack and redirecting the CPU to this custom "thunk," they could force the game to execute its own internal functions (such as `fireAllGuns`) with specific arguments.

**Networking and Synchronization**
The multiplayer architecture uses a TCP client-server model with Protobuf messages. The "leader" (server) runs the mission and transmits the positions of all entities to the client every frame. The client responds with its own position and local events. A major challenge involved Borland’s overlay system, which required the author to carefully construct stack frames for their hooks to prevent the game from crashing during memory management cycles. 

**Refining the Experience**
Later stages of the project involved synchronizing ephemeral objects like asteroids and laser bolts, which required mapping server ship IDs to local client IDs. The project successfully enabled synchronized explosions, missile fire, and autopilot, transforming the 1990 classic into a functional co-op experience.

---

## 99. Show HN: I built a tool that prices a pre-built PC part by part

**原文标题**: Show HN: I built a tool that prices a pre-built PC part by part

**原文链接**: [https://pcdealcheck.com/](https://pcdealcheck.com/)

生成摘要时出错

---

## 100. 11 Nanoseconds per Word: Over-Optimizing Anagrams

**原文标题**: 11 Nanoseconds per Word: Over-Optimizing Anagrams

**原文链接**: [https://wiredream.com/anagram-fun/](https://wiredream.com/anagram-fun/)

生成摘要时出错

---

