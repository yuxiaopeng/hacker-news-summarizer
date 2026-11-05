# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-11-05.md)

*最后自动更新时间: 2026-11-05 22:59:33*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-11-05](output/hacker_news_summary_2026-11-05.md) |
| 2 | [2026-11-03](output/hacker_news_summary_2026-11-03.md) |
| 3 | [2026-10-31](output/hacker_news_summary_2026-10-31.md) |
| 4 | [2026-11-01](output/hacker_news_summary_2026-11-01.md) |
| 5 | [2026-11-04](output/hacker_news_summary_2026-11-04.md) |
| 6 | [2026-10-29](output/hacker_news_summary_2026-10-29.md) |
| 7 | [2026-10-25](output/hacker_news_summary_2026-10-25.md) |
| 8 | [2026-10-30](output/hacker_news_summary_2026-10-30.md) |
| 9 | [2026-10-27](output/hacker_news_summary_2026-10-27.md) |
| 10 | [2026-10-28](output/hacker_news_summary_2026-10-28.md) |
| 11 | [2026-10-26](output/hacker_news_summary_2026-10-26.md) |
| 12 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 13 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 14 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 15 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 16 | [2026-10-24](output/hacker_news_summary_2026-10-24.md) |
| 17 | [2026-10-23](output/hacker_news_summary_2026-10-23.md) |
| 18 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 19 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 20 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 21 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 22 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 23 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 24 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 25 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 26 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 27 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 28 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 29 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 30 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 31 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 32 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 33 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 34 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 35 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 36 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 37 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 38 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 39 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 40 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 41 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 42 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 43 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 44 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 45 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 46 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 47 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 48 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 49 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 50 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 51 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 52 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 53 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 54 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 55 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 56 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 57 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 58 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 59 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 60 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 61 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 62 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 63 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 64 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 65 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 66 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 67 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 68 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 69 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 70 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 71 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 72 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 73 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 74 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 75 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 76 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 77 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 78 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 79 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 80 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 81 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 82 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 83 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 84 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 85 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 86 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 87 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 88 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 89 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 90 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 91 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 92 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 93 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 94 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 95 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 96 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 97 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 98 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 99 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 100 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 101 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 102 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 103 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 104 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 105 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 106 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 107 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 108 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 109 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 110 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 111 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 112 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 113 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 114 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 115 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 116 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 117 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 118 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 119 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 120 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 121 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 122 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 123 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 124 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 125 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 126 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 127 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 128 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 129 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 130 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 131 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 132 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 133 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 134 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 135 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 136 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 137 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 138 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 139 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 140 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 141 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 142 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 143 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 144 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 145 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 146 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 147 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 148 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 149 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 150 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 151 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 152 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 153 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 154 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 155 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 156 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 157 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 158 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 159 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 160 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 161 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 162 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 163 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 164 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 165 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 166 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 167 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 168 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 169 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 170 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 171 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 172 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 173 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 174 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 175 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 176 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 177 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 178 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 179 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 180 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 181 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 182 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 183 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 184 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 185 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 186 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 187 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 188 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 189 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 190 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 191 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 192 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 193 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 194 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 195 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 196 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 197 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 198 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 199 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 200 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 201 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 202 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 203 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 204 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 205 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 206 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 207 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 208 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 209 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 210 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 211 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 212 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 213 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 214 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 215 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 216 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 217 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 218 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 219 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 220 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 221 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 222 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 223 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 224 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 225 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 226 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 227 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 228 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 229 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 230 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 231 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 232 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 233 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 234 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 235 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 236 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 237 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 238 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 239 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 240 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 241 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 242 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 243 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 244 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 245 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 246 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 247 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 248 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 249 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 250 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 251 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 252 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 253 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 254 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 255 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 256 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 257 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 258 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 259 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 260 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 261 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 262 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 263 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 264 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 265 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 266 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 267 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 268 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 269 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 270 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 271 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 272 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 273 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 274 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 275 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 276 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 277 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 278 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 279 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 280 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 281 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 282 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 283 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 284 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 285 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 286 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 287 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 288 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 289 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 290 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 291 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 292 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 293 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 294 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 295 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 296 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 297 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 298 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 299 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 300 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 301 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 302 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 303 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 304 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 305 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 306 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 307 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 308 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 309 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 310 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 311 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 312 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 313 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 314 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 315 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 316 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 317 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 318 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 319 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 320 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 321 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 322 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 323 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 324 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 325 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 326 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 327 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 328 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 329 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 330 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 331 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 332 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 333 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 334 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 335 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 336 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 337 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 338 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 339 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 340 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 341 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 342 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 343 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 344 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 345 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 346 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 347 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 348 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 349 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 350 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 351 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 352 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 353 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 354 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 355 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 356 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 357 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 358 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 359 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 360 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 361 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 362 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 363 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 364 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 365 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 366 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 367 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 368 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 369 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 370 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 371 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 372 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 373 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 374 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 375 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 376 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 377 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 378 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 379 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 380 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 381 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 382 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 383 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 384 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 385 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 386 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 387 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 388 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 389 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 390 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 391 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 392 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 393 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 394 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 395 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 396 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 397 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 398 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 399 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 400 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 401 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 402 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 403 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 404 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 405 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 406 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 407 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 408 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 409 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 410 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 411 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 412 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 413 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 414 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 415 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 416 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 417 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 418 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 419 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 420 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 421 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 422 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 423 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 424 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 425 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 426 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 427 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 428 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 429 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 430 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 431 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 432 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 433 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 434 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 435 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 436 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 437 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 438 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 439 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 440 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 441 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 442 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 443 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 444 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 445 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 446 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 447 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 448 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 449 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 450 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 451 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 452 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 453 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 454 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 455 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 456 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 457 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 458 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 459 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 460 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 461 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 462 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 463 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 464 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 465 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 466 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 467 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 468 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 469 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 470 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 471 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 472 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 473 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 474 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 475 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 476 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 477 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 478 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 479 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 480 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 481 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 482 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 483 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 484 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 485 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 486 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 487 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 488 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 489 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 490 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 491 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 492 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 493 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 494 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 495 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 496 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 497 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 498 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 499 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 500 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 501 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 502 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 503 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 504 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 505 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 506 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 507 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 508 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 509 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 510 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 511 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 512 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 513 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 514 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 515 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 516 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 517 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 518 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 519 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 520 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 521 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 522 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 523 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 524 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 525 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 526 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 527 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 528 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 529 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 530 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 531 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 532 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 533 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 534 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 535 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 536 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 537 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 538 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 539 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 540 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 541 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 542 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 543 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 544 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 545 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 546 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 547 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 548 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 549 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 550 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 551 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 552 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 553 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 554 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 555 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 556 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 557 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 558 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 559 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 560 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 561 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 562 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 563 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 564 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 565 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 566 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 567 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 568 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 569 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 570 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 571 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 572 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 573 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 574 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 575 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 576 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 577 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 578 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 579 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 580 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 581 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 582 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 583 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 584 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 585 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 586 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 587 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 588 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 589 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 590 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 591 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 592 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
