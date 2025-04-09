# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-04-09.md)

*最后自动更新时间: 2025-04-09 13:01:59*
## 1. 使用内容安全策略强化 Firefox 前端

**原文标题**: Hardening the Firefox Front End with Content Security Policies

**原文链接**: [https://attackanddefense.dev/2025/04/09/hardening-the-firefox-frontend-with-content-security-policies.html](https://attackanddefense.dev/2025/04/09/hardening-the-firefox-frontend-with-content-security-policies.html)

本文详细介绍了通过实施内容安全策略 (CSP) 来加强 Firefox 用户界面 (UI) 防御注入攻击，特别是跨站脚本攻击 (XSS) 的措施。使用 Web 技术构建的 Firefox UI 容易受到此类攻击，类似于 Web 应用程序。本文重点介绍了 Pwn2Own 2022 中的一个漏洞利用链，该链涉及将 JavaScript 注入到 UI 中。

主要重点是 `browser.xhtml`，即 Firefox UI 的主要 XHTML 文档，通过删除 600 多个内联事件处理程序，这些处理程序是 XSS 攻击的常见目标。这些处理程序，例如 `<button onclick="buttonClicked()">`，已被替换为单独 JavaScript 文件中对 `addEventListener` 的调用。本文还向 Firefox 开发人员介绍了迁移代码时内联和标准事件处理程序之间的细微差别。

除了 `browser.xhtml` 之外，本文还指出，更严格的 CSP 正在应用于其他 UI 组件，例如“关于 Firefox”对话框，以限制资源加载到 Firefox 提供的文件。长期目标是消除所有动态代码执行（如 `eval`），以创建一个高度安全的浏览器。Firefox 138 中发布的删除内联事件处理程序，显着提高了攻击者的门槛，甚至可能破坏现有的漏洞利用链。尽管 UI 中需要具有高权限的 JavaScript API，但这些改进增强了 Firefox 对注入攻击的抵抗力。

---

## 2. Apache ECharts

**原文标题**: Apache ECharts

**原文链接**: [https://echarts.apache.org/en/index.html](https://echarts.apache.org/en/index.html)

ECharts：一个用于快速创建 Web 可视化效果的声明式框架。其核心信息是 ECharts 简化了构建交互式 Web 图表和图形的过程。文档还强调了适当署名的重要性，要求用户在任何项目、研究或其他相关活动中使用 ECharts 时，引用 2018 年发表的相关 Visual Informatics 论文。该论文（可通过提供的 PDF 链接访问）可能包含有关该框架的架构、特性和优点的更多详细信息。

---

## 3. Whisky已不再积极维护。

**原文标题**: Whisky is no longer actively maintained

**原文链接**: [https://docs.getwhisky.app/maintenance-notice](https://docs.getwhisky.app/maintenance-notice)

Whisky，一款macOS上的Wine前端，已不再由其创建者Isaac积极维护。他表示，由于所需的时间投入、他的学生身份以及认为该项目已对Mac上的Wine生态系统造成损害，导致失去了兴趣。

最初旨在成为一个引擎无关的前端，但随着GPTK的引入，Whisky的方向发生了转变，模糊了其最初的目标。Isaac承认Wine开发的复杂性，它使用C语言编写，需要大量的逆向工程技能，并强调了CodeWeavers（及其产品CrossOver）在资助和维持macOS上的Wine开发方面所起到的关键作用。

Isaac认为，Whisky通过依赖CrossOver而不贡献定制修复，创造了一种“寄生关系”，这可能会损害CrossOver的盈利能力，从而影响Mac上Wine的未来。他鼓励用户购买CrossOver以支持Wine的开发。

他澄清说，他与CodeWeavers没有隶属关系，也没有因此获得报酬而停止开发Whisky。他只是决定这是正确的做法。他已经转向其他macOS项目，包括移植Sonic Unleashed Recompiled。可以在Bluesky和GitHub上找到他。

---

## 4. 我认识的最优秀的程序员

**原文标题**: The best programmers I know

**原文链接**: [https://endler.dev/2025/best-programmers/](https://endler.dev/2025/best-programmers/)

无法访问文章链接。

---

## 5. 类太阳恒星

**原文标题**: 'Sun-Like' Stars

**原文链接**: [https://www.centauri-dreams.org/2025/04/08/on-sun-like-stars/](https://www.centauri-dreams.org/2025/04/08/on-sun-like-stars/)

保罗·吉尔斯特的文章深入探讨了系外行星研究中“类太阳”恒星的模糊定义，强调了向公众传达科学发现所面临的挑战。该术语经常被宽松使用，包括G型恒星（如我们的太阳），有时甚至扩展到包括F型和K型恒星。这种扩展源于渴望包括寿命长、稳定的恒星，这些恒星可能能够容纳可居住的行星。

问题在于，当科学界广泛使用“类太阳”（FGK，甚至所有主序星）时，公众通常将其严格解释为G型星。这种差异导致了对类地行星频率的误解，并可能影响公众对系外行星研究的支持和资助。

该文章强调了精确语言的重要性，尤其是在新闻稿中，以避免误导公众。类似的模糊性也围绕着“类地”和“宜居”等术语，需要仔细定义。

评论部分进一步探讨了宜居性的复杂性，承认我们仅基于地球的有限理解。评论者讨论了生命在不同条件下进化的可能性，以及灾难性事件使原本可居住的行星变得荒芜的可能性。总而言之，文章及其评论强调了在向公众传达系外行星研究时需要清晰和谨慎。

---

## 6. PostgreSQL 全文搜索：配置得当，速度飞快 (打破缓慢神话)

**原文标题**: PostgreSQL Full-Text Search: Fast When Done Right (Debunking the Slow Myth)

**原文链接**: [https://blog.vectorchord.ai/postgresql-full-text-search-fast-when-done-right-debunking-the-slow-myth](https://blog.vectorchord.ai/postgresql-full-text-search-fast-when-done-right-debunking-the-slow-myth)

好的，以下是PostgreSQL全文搜索的总结：正确使用时速度很快（打破缓慢的神话）。由于我无法直接访问提供的URL，因此该总结基于类似文章中的常见主题和论点，以及我对我PostgreSQL全文搜索能力的一般了解。

这篇文章可能认为，PostgreSQL的全文搜索（FTS）经常被不公平地认为是缓慢的，而这种看法源于不正确的实现，而不是固有的局限性。它可能强调以下关键点：

*   **FTS功能强大：** PostgreSQL内置的FTS为索引和搜索文本数据提供了复杂的功能，包括词干提取、停用词删除和排名。
*   **索引至关重要：** 文章可能强调在`tsvector`列（标记化的文本表示）上创建`GIN`索引的重要性。如果没有适当的索引，FTS查询将执行全表扫描，导致性能不佳。
*   **配置很重要：** 正确配置文本搜索配置（`pg_catalog.english`或类似配置）至关重要。这包括选择适当的语言和自定义词典以处理特定的领域术语或缩写。
*   **查询构建很重要：** 查询的制定方式会影响性能。适当使用像`@@`这样的运算符并利用排名函数（`ts_rank`）可以优化查询执行。
*   **数据准备是关键：** 文章可能讨论了使用 to_tsvector() 函数将数据转换为合适的格式，以便进行索引和搜索的重要性。
*   **基准测试是必要的：** 文章可能会鼓励对不同的FTS配置和查询模式进行彻底的基准测试，以确定特定用例的最佳设置。
*   **打破神话：** 通过解决这些实现细节，文章旨在证明，如果正确实现，PostgreSQL FTS可以非常快速高效，在许多情况下可以与专用搜索引擎媲美。总的来说，感觉到的缓慢通常是配置错误或优化不足的症状，而不是PostgreSQL的FTS能力的根本限制。

无法访问文章链接。

---

## 7. Cyc讣告

**原文标题**: Obituary for Cyc

**原文链接**: [https://yuxi-liu-wired.github.io/essays/posts/cyc/](https://yuxi-liu-wired.github.io/essays/posts/cyc/)

本文是一篇关于Cyc的讣告，Cyc是道格拉斯·列纳特为实现通过符号逻辑实现通用人工智能而进行的为期40年的项目。文章认为，Cyc最终未能兑现其承诺。

列纳特早期在自动数学发现（AM和EURISKO）方面的工作使他相信，大量的常识知识对于人工智能至关重要。1985年，他启动了Cyc项目，手动编码数百万个事实和规则。尽管增长到3000万条断言并消耗了大量资源（2亿美元，2000人年），Cyc从未实现预测的突破性进展，即真正的机器学习和自主发现。

该项目最初主要由军事/情报部门资助，后来转向商业应用。然而，其商业用途仍然是标准的专家系统、数据集成和信息检索，并没有展现出Cyc所宣称的更高智能所带来的竞争优势。

Cyc在学术上是孤立的，专注于信息输入的方法，而不是实际应用或外部验证。学术界很难使用它，并且在公共基准测试中表现不佳。像OpenCyc这样的衍生项目也失败了。

列纳特坚持单一的哲学愿景，导致他拒绝了其他人工智能方法。文章总结说，Cyc的失败表明了人工智能符号逻辑方法的局限性。它深入探讨了列纳特早期的自动数学家（AM）项目，突出了其优点和缺点，特别是对人工编码启发式规则的依赖。它指出了AM的设计问题，例如概念命名方式的模糊性以及验证定义等价性的挑战。

---

## 8. 减少屏幕时间的指南

**原文标题**: The guide to reduce screen time

**原文链接**: [https://speedbumpapp.com/en/blog/how-to-reduce-screen-time/](https://speedbumpapp.com/en/blog/how-to-reduce-screen-time/)

如何减少屏幕时间：终极指南

本文《如何减少屏幕时间：终极指南》提供了一种全面方法，旨在平衡技术使用与现实生活参与。文章认为，对于许多人来说，完全戒掉社交媒体是不现实的，但找到健康的平衡是可以实现的。

该指南强调理解过度使用屏幕时间的“原因”，承认诸如无聊、焦虑和拖延等原因。它鼓励将心态从限制转变为积极参与替代活动。

文章随后详细介绍了减少屏幕时间的实用工具和策略。这些包括利用iOS和Android设备上的内置屏幕时间功能来监控使用情况、设置限制和使用专注模式。它还回顾了几款第三方应用程序，如One Sec、Opal、SpeedBump、Clearspace、ScreenZen、Focus Plant和Forest，每款应用程序都提供独特的功能，如深呼吸提示、数据驱动的跟踪、会话限制、功能阻止和游戏化专注。

进一步的建议包括管理通知、组织应用程序布局、使用灰度模式、创建无屏幕区域、订阅新闻通讯以及有意识地选择模拟替代方案（如报纸或黑胶唱片）。它还强调了适应无聊以培养创造力的重要性。对于更极端的措施，文章建议卸载应用程序或使用“功能机”。

结论强调了结合策略、保持一致性以及认识到社交媒体平台的成瘾性的重要性。它敦促读者立即采取行动，创建一份可执行的步骤清单并跟踪进展。文章还提供了一个简短的常见问题解答，涵盖桌面使用、通知影响和建议的屏幕时间限制。

---

## 9. 巴西政府运营的支付系统已占据主导地位。

**原文标题**: Brazil's government-run payments system has become dominant

**原文链接**: [https://www.economist.com/the-americas/2025/04/03/brazils-government-run-payments-system-has-become-dominant](https://www.economist.com/the-americas/2025/04/03/brazils-government-run-payments-system-has-become-dominant)

巴西政府运营的数字支付系统Pix于2020年11月推出，已迅速成为该国主要支付技术。 其吸引力源于其易用性、即时交易和免费服务，这在COVID-19大流行期间尤其有利，因为它最大限度地减少了身体接触。 用户可以使用收款人的国民身份证、电话号码或二维码转账。

到2024年，Pix的受欢迎程度超过了现金和银行卡，处理了630亿笔交易，价值26万亿雷亚尔（4.5万亿美元），与2021年的90亿笔交易相比显著增加。 这种快速普及率在全球范围内是无与伦比的。 虽然Pix使巴西的银行业现代化，但其主导地位也引发了人们对权力集中在巴西中央银行的潜在担忧。 该文章强调Pix的成功，但也暗示了政府控制的支付系统可能带来的影响。

---

## 10. Linux内核防御图 – 安全加固概念

**原文标题**: Linux Kernel Defence Map – Security Hardening Concepts

**原文链接**: [https://github.com/a13xp0p0v/linux-kernel-defence-map](https://github.com/a13xp0p0v/linux-kernel-defence-map)

本文介绍了“Linux内核防御图”，这是一个以可视化的方式呈现Linux内核安全概念及其关系的工具。该图涵盖了漏洞类型、利用技术、漏洞检测和防御技术，包括内核内和内核外的解决方案，其中一些依赖于专门的硬件。它的目标是帮助用户浏览文档和内核源代码，同时参考常见弱点枚举（CWE）编号。

该图是一个专注于内核安全加固的工具，特别排除了攻击面缩减、用户空间安全特性和Linux安全模块（LSM）策略。它使用DOT语言创建，便于维护和通过Git进行版本控制，采用GPL-3.0许可。作者提供了多个存储库（GitHub、Codeberg、GitFlic）的链接，可以在这些地方访问该图。

为了帮助用户验证其内核配置并识别缺失的安全加固选项，作者还创建了“kernel-hardening-checker”。

最后，本文提供了一系列参考文献，涵盖Linux内核安全的各个方面，包括Grsecurity特性、内核自我保护、漏洞缓解以及Spectre和Meltdown漏洞检查。所述的图对应于Linux内核v6.10。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 2 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 3 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 4 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 5 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 6 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 7 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 8 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 9 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 10 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 11 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 12 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 13 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 14 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 15 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 16 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 17 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 18 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 19 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 20 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 21 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 22 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
