# Hacker News 热门文章摘要 (2025-04-09)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 使用内容安全策略加固 Firefox 前端

**原文标题**: Hardening the Firefox Front End with Content Security Policies

**原文链接**: [https://attackanddefense.dev/2025/04/09/hardening-the-firefox-frontend-with-content-security-policies.html](https://attackanddefense.dev/2025/04/09/hardening-the-firefox-frontend-with-content-security-policies.html)

本文探讨了通过利用内容安全策略 (CSP) 来加强 Firefox 前端防御注入攻击，特别是跨站脚本攻击 (XSS) 的努力。 由于 Firefox UI 是使用 Web 技术构建的，因此它容易受到 Web 应用程序中发现的类似漏洞的影响。

本文重点介绍了 Pwn2Own 2022 中的一个漏洞链如何利用 Firefox UI 中 JavaScript 内联事件处理程序的创建。 为了降低这种风险，Firefox 团队一直在从主 UI 文档 `browser.xhtml` 中删除内联事件处理程序，并用单独 JavaScript 文件中的 `addEventListener` 调用来替换它们。 然后，CSP 用于默认阻止内联脚本的执行，从而显着阻碍了依赖于注入和执行任意代码的 XSS 攻击。

已经重写了 600 多个内联事件处理程序，这表明在加强 UI 方面取得了重大进展。 本文还提到了将此安全措施扩展到 Firefox UI 的其他部分以及实施更严格的 CSP（例如已经为“about:”页面实施的 CSP）的计划。 最终目标是消除 Firefox 中的所有动态代码执行，包括 `eval`，以创建更安全的浏览体验。 这种积极主动的方法提高了攻击者的门槛，并使 Firefox 更具弹性，不易受到攻击。

---

## 2. Apache ECharts

**原文标题**: Apache ECharts

**原文链接**: [https://echarts.apache.org/en/index.html](https://echarts.apache.org/en/index.html)

Apache ECharts是一个声明式框架，专为快速创建基于Web的可视化图表而设计。文章强调了该框架的实用性，并鼓励用户在研究、开发、产品创建、报告、出版物、教育和专利申请等各种活动中使用ECharts时，引用2018年在Visual Informatics上发表的指定论文。本质上，这段文字是对ECharts的介绍，并要求在使用该框架时进行适当的引用。

---

## 3. 我所认识的最优秀的程序员

**原文标题**: The best programmers I know

**原文链接**: [https://endler.dev/2025/best-programmers/](https://endler.dev/2025/best-programmers/)

无法访问文章链接。

---

## 4. 类太阳恒星

**原文标题**: 'Sun-Like' Stars

**原文链接**: [https://www.centauri-dreams.org/2025/04/08/on-sun-like-stars/](https://www.centauri-dreams.org/2025/04/08/on-sun-like-stars/)

保罗·吉尔斯特的文章深入探讨了在讨论系外行星研究时，“类太阳”一词的复杂性和模糊性。他首先回忆了童年时期对寻找围绕类太阳恒星的可居住行星的迷恋。然而，他意识到“类太阳”一词缺乏严格的定义。

文章强调了“类太阳”的含义从科学论文到大众媒体的转变。虽然像太阳一样的G型恒星是主要焦点，但由于它们的长寿命和潜在的宜居世界，该定义经常扩展到包括F型和K型恒星。有些人甚至将其延伸到包括所有主序星（OBAFGKM），认为这些恒星处于适合生命发展的稳定的氢燃烧阶段。

吉尔斯特强调了澄清“类太阳”定义的重要性，因为它会影响对宜居行星频率的估计。它可以极大地改变人们对潜在的地球级行星数量的看法，从而影响公众认知，并可能影响系外行星研究的资金。作者还将“类地”这一模糊术语进行了类比，并强调科学家在与公众交流时需要使用精确的语言。

随后的评论进一步阐述了围绕宜居性的不确定性，承认我们对生命需求的有限理解以及可能影响宇宙中生命普遍存在的各种挑战。

---

## 5. PostgreSQL 全文搜索：正确配置，速度飞快（破除缓慢神话）

**原文标题**: PostgreSQL Full-Text Search: Fast When Done Right (Debunking the Slow Myth)

**原文链接**: [https://blog.vectorchord.ai/postgresql-full-text-search-fast-when-done-right-debunking-the-slow-myth](https://blog.vectorchord.ai/postgresql-full-text-search-fast-when-done-right-debunking-the-slow-myth)

无法访问文章链接。

---

## 6. Cyc讣告

**原文标题**: Obituary for Cyc

**原文链接**: [https://yuxi-liu-wired.github.io/essays/posts/cyc/](https://yuxi-liu-wired.github.io/essays/posts/cyc/)

这篇讣告记录了道格拉斯·列纳特雄心勃勃的项目Cyc的四十年历程，该项目旨在通过符号逻辑和庞大的知识库创造通用人工智能（AGI）。文章认为，Cyc最终未能实现其目标。

列纳特早期在自动数学发现（AM和EURISKO）方面的工作使他相信，AGI需要大量的常识知识基础。1985年，他启动了Cyc项目，手动编码了数百万个事实和规则。该项目耗资2亿美元和2000人年，积累了约3000万条断言。然而，尽管多次预测会有突破，Cyc从未实现真正的机器学习或AGI。

文章强调了Cyc的封闭性，指出它在学术界AI研究中的应用极少，并且在公开基准测试中缺乏表现。虽然Cyc背后的商业实体Cycorp通过专家系统、数据集成和信息检索应用程序实现了财务稳定，但没有证据表明Cyc的高级智能比传统方法提供了任何竞争优势。作者批评列纳特坚定地坚持符号逻辑，拒绝其他AI方法。OpenCyc的衍生项目也失败了。作者的结论是，Cyc的长期失败是对AI的符号逻辑方法的控诉。

---

## 7. 巴西政府运营的支付系统已占据主导地位。

**原文标题**: Brazil's government-run payments system has become dominant

**原文链接**: [https://www.economist.com/the-americas/2025/04/03/brazils-government-run-payments-system-has-become-dominant](https://www.economist.com/the-americas/2025/04/03/brazils-government-run-payments-system-has-become-dominant)

2020年11月，巴西中央银行（BCB）推出了Pix，这是一种迅速在该国占据主导地位的数字支付系统。在COVID-19疫情期间，非接触式交易需求旺盛，Pix恰好提供了一种即时、免费且易于使用的支付方式。

用户可以使用收款人的国民身份证号、电话号码或二维码进行转账。到2024年，Pix已超过现金和银行卡，成为巴西最受欢迎的支付技术。交易数量从2021年的90亿笔激增至2024年的630亿笔，价值达26万亿雷亚尔（4.5万亿美元）。巴西对Pix的采用率在全球范围内首屈一指。

虽然Pix使巴西的银行部门实现了现代化，但也将大量权力集中在中央银行手中，这是文章中提到的一个潜在令人担忧的方面。

---

## 8. Show HN: DrawDB – 开源在线数据库图表编辑器 (复古风)

**原文标题**: Show HN: DrawDB – open-source online database diagram editor (a retro)

**原文链接**: [https://www.drawdb.app/](https://www.drawdb.app/)

DrawDB：开源在线数据库图表编辑器及SQL生成器。此“Show HN”帖子介绍DrawDB，它允许用户可视化设计数据库模式并自动生成相应的SQL代码。“您需要启用JavaScript才能运行此应用”提示表明它是一个用JavaScript构建的客户端Web应用程序。 本质上，它是一款旨在通过可视化表示和自动代码生成来简化数据库设计和实现的工具。

---

## 9. Linux内核防御图 – 安全加固概念

**原文标题**: Linux Kernel Defence Map – Security Hardening Concepts

**原文链接**: [https://github.com/a13xp0p0v/linux-kernel-defence-map](https://github.com/a13xp0p0v/linux-kernel-defence-map)

本文介绍了 Linux 内核防御地图，一个旨在导航复杂的 Linux 内核安全领域的图形表示。该地图由 a13xp0p0v 创建，以可视化的方式将漏洞类别（带有 CWE 编号）、利用技术、漏洞检测机制以及各种防御技术（包括内核内和内核外的，以及硬件相关的解决方案）连接起来。 这些连接阐明了关系，不一定表示完全缓解。

该地图使用 DOT 语言编写，便于 Git 维护，可在 GitHub、Codeberg 和 GitFlic 上获取。 它可以使用 GraphViz 生成。作者强调，该地图侧重于内核安全加固，不包括攻击面缩小、用户空间安全功能和 LSM 策略。

此外，作者还提供了一个名为 "kernel-hardening-checker" 的工具，以帮助用户验证和改进其内核配置，通过识别主要发行版默认情况下通常未启用的安全加固选项。

本文还列出了几个关键参考文献，包括关于 Grsecurity、内核自我保护、安全文档、缓解清单以及分析内核漏洞及其缓解措施的研究论文的资源。当前地图版本专为 Linux 内核 v6.10 设计。

---

## 10. Tailscale 融资 1.6 亿美元

**原文标题**: Tailscale has raised $160M

**原文链接**: [https://tailscale.com/blog/series-c](https://tailscale.com/blog/series-c)

Tailscale 获 Accel 领投 1.6 亿美元 C 轮融资，加速实现网络隐形化，打造以身份而非 IP 地址为核心的新互联网。该轮融资将用于消除摩擦、在不增加复杂性的前提下扩展网络，并使身份成为安全连接的核心。

Tailscale 旨在解决日益复杂的网络问题，这在 AI 行业尤为突出，因为跨云连接 GPU 和保护工作负载极具挑战性。Perplexity、Mistral 和 Cohere 等领先的 AI 公司已在使用 Tailscale。其他知名客户包括 Instacart、SAP 和 Duolingo。

该公司计划扩大其工程和产品团队，投资于免费客户的免费支持，并保持向后兼容性。这项投资使 Tailscale 能够继续专注于简化所有人的网络连接，从初创公司到财富 500 强公司。此轮融资包括现有和新投资者的参与，包括 Accel 的 Amit Kumar、Anthony Casalena（Squarespace 首席执行官）、CRV、Heavybit、Insight、Uncork Capital 和 George Kurtz（Crowdstrike 首席执行官）。Tailscale 认为网络是安全和身份层的最佳位置，边界正在从数据中心转移到个人。

---

