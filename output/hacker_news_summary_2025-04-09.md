# Hacker News 热门文章摘要 (2025-04-09)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 展示HN：DrawDB – 开源在线数据库图表编辑器（复古风）

**原文标题**: Show HN: DrawDB – open-source online database diagram editor (a retro)

**原文链接**: [https://www.drawdb.app/](https://www.drawdb.app/)

本次“Show HN”帖子宣布推出 DrawDB，一个开源的在线数据库图表编辑器和 SQL 生成器。 DrawDB 的核心功能是允许用户可视化地设计数据库模式，然后生成相应的 SQL 代码。 帖子的简洁性表明该工具专注于易用性和数据库设计的快速原型。 虽然帖子缺乏详细描述，但“Show HN”标签暗示创建者正在寻求反馈，并向 Hacker News 社区展示他们的作品。

---

## 12. Tailscale 融资 1.6 亿美元

**原文标题**: Tailscale has raised $160M

**原文链接**: [https://tailscale.com/blog/series-c](https://tailscale.com/blog/series-c)

Tailscale 在 C 轮融资中筹集了 1.6 亿美元（2.3 亿加元），本轮融资由 Accel 领投，CRV、Insight Partners、Heavybit、Uncork Capital、George Kurtz (Crowdstrike 首席执行官) 和 Anthony Casalena (Squarespace 首席执行官) 参投。

该公司成立于 2019 年，旨在简化网络连接并使其消失，方法是消除 NAT 穿透和 VPN 配置的复杂性。每天有数百万用户依赖 Tailscale 连接各种资源，从家庭实验室到 AI 工作负载。

这笔资金将用于加速在以下领域的增长：消除网络连接中的摩擦，在不增加复杂性的情况下扩展网络，以及使身份成为安全连接的核心。Tailscale 开创了“身份优先的网络”，连接基于用户、应用程序和服务，而不仅仅是 IP 地址。

该公司强调对其解决方案的需求日益增长，尤其是在人工智能行业，Perplexity、Mistral、Cohere、Groq 和 Hugging Face 等公司使用 Tailscale 来管理复杂的基础设施。其他值得注意的用户包括 Instacart、SAP、Telus、Motorola 和 Duolingo。

Tailscale 计划扩大其工程和产品团队，投资于免费的客户支持，并保持向后兼容性。该公司的目标是使所有用户的网络连接无缝化，无论其规模或行业如何。

---

## 13. 非线性声片显微镜：不透明器官毛细血管/细胞尺度成像

**原文标题**: Nonlinear soundsheet microscopy:imaging opaque organs capillary/cellular scale

**原文链接**: [https://www.science.org/doi/10.1126/science.ads1325](https://www.science.org/doi/10.1126/science.ads1325)

无法访问文章链接。

---

## 14. Dockerfmt: Dockerfile 格式化工具

**原文标题**: Dockerfmt: A Dockerfile Formatter

**原文链接**: [https://github.com/reteps/dockerfmt](https://github.com/reteps/dockerfmt)

Dockerfmt: 基于 Buildkit 解析器的 Dockerfile 格式化工具，是 dockfmt 的现代替代品。它格式化 Dockerfile，并使用 `mvdan/sh` 格式化 RUN 指令。可通过 Releases 页面提供的二进制文件安装。

主要特性包括格式化 RUN 指令、支持基本 heredoc，以及处理 RUN 指令中的内联注释。使用方法是运行 `dockerfmt` 命令，指定 Dockerfile 路径，并可选择使用诸如 `--check` (用于验证格式)、`--indent` (用于指定缩进)、`--newline` (用于添加尾部换行) 和 `--write` (用于将更改写回文件) 等标志。

Dockerfmt 可以通过在 `.pre-commit-config.yaml` 中添加条目来集成为 pre-commit hook。 限制包括不支持 RUN 命令中的分组或分号、不支持长 JSON 命令的自动换行，以及不支持 `# escape=X` 指令。 欢迎贡献。JS 绑定也可在 js 目录中找到。

---

## 15. 使盲人和视力障碍读者更容易获取图表的新方法

**原文标题**: A new way to make graphs more accessible to blind and low-vision readers

**原文链接**: [https://news.mit.edu/2025/making-graphs-more-accessible-blind-low-vision-readers-0325](https://news.mit.edu/2025/making-graphs-more-accessible-blind-low-vision-readers-0325)

麻省理工CSAIL开发触觉Vega-Lite系统，旨在简化盲人和低视力读者触觉图表的创建。 这些图表将条形图等视觉数据转换为基于触摸的表示形式。 该系统解决了当前触觉图表设计的挑战，这些设计可能很复杂、耗时，并且需要多个软件程序和对指南（例如北美盲文管理局指南）的广泛了解。

触觉Vega-Lite允许用户输入数据（例如来自Excel表格），并自动生成标准视觉图表和触觉版本。 一个关键特性是将设计标准作为默认规则纳入，使教育工作者和设计师能够更轻松地创建可访问的触觉图表。 用户可以通过代码抽象自定义轴标签、刻度线和纹理，从而进行精确编辑。 程序库中包含这些自定义的示例，以帮助用户。

该工具旨在弥合设计专业人员所需的精确度与教育工作者所需的效率之间的差距。 它被设计为用户友好、提供即时反馈并遵守辅助功能指南。 研究人员还在努力添加特定于机器的自定义设置，以允许用户根据不同盲文点显器的规格预览和调整图表。

虽然触觉Vega-Lite简化了触觉图表的创建过程，但开发者强调它不应取代专家对指南合规性的审查。 研究团队正在继续将盲文设计规则纳入该程序。

---

## 16. 钡实验

**原文标题**: The Barium Experiment

**原文链接**: [https://tomscii.sig7.se/2025/04/The-Barium-Experiment](https://tomscii.sig7.se/2025/04/The-Barium-Experiment)

无法访问文章链接。

---

## 17. NTATV：让初代Apple TV运行Windows NT (Windows XP, Windows 2003)

**原文标题**: NTATV: Bringing Windows NT (Windows XP, Windows 2003) to the Original Apple TV

**原文链接**: [https://github.com/DistroHopper39B/NTATV](https://github.com/DistroHopper39B/NTATV)

NTATV是由DistroHopper39B发起的一个项目，成功地在初代Apple TV上启动了Windows XP和Windows Server 2003。这是通过移植ReactOS的FreeLoader启动程序实现的，以绕过Apple TV的仅EFI固件，并克服其启动标准操作系统的限制。

该项目取得了显著进展，Windows XP和2003已实现桌面功能，并且大多数驱动程序都已工作，包括PCI、USB、基本视频、加速视频、以太网、WiFi、RCA音频和遥控器。然而，ReactOS由于PCI问题面临限制。由于Apple TV独特的硬件配置，HDMI音频不太可能工作。

已知问题包括显示器待机问题，需要重新插拔HDMI线；组件视频问题，与NVIDIA驱动程序有关；以及FreeLoader NTFS驱动程序在非英文Windows版本上失败。NTVDM也无法运行，但建议使用DOSBox或winevdm作为替代方案。

该项目的源代码、构建说明和鸣谢信息已提供给有兴趣复制或贡献的人员。最新版本v0.2将FreeLoader更新至3.2版，并解决了IDE驱动程序问题，从而可以从各种IDE驱动器启动。现在包含一个带有NVIDIA驱动程序支持的预构建映像。

---

## 18. 使用 text-wrap: pretty 实现更佳排版

**原文标题**: Better typography with text-wrap pretty

**原文链接**: [https://webkit.org/blog/16547/better-typography-with-text-wrap-pretty/](https://webkit.org/blog/16547/better-typography-with-text-wrap-pretty/)

Jen Simmons 的这篇文章介绍了 `text-wrap: pretty`，一个旨在改善网页排版的 CSS 属性，目前已在 Safari 技术预览版中实现。它与标准的单行换行算法形成对比，后者通常导致短尾行、糟糕的参差不齐的边缘以及其他不良的排版效果。与现有的专注于最后四行的 Chromium 实现不同，Safari 的版本评估整个段落，以改善参差不齐的边缘并减少连字符的使用。

文章解释说，传统的排版强调避免短尾行、糟糕的参差不齐的边缘、不良的连字符和排版河流，而 `text-wrap: pretty` 有助于缓解所有这些问题。它还将 `text-wrap: pretty` 与 `text-wrap: balance` 进行了对比。虽然 `pretty` 旨在通过对参差不齐的边缘和换行进行细微调整来改善正文的整体外观和可读性，但 `balance` 侧重于使所有行的长度大致相同，通常导致较窄的文本块，适用于标题或说明文字。

文章强调，每个浏览器对 `pretty` 的实现方式都不同，并且性能考虑至关重要。作者保证，Safari 的实现经过优化，可最大程度地减少性能影响，尤其是在典型的段落长度上。文章鼓励开发者测试 `text-wrap: pretty` 并提供反馈，并鼓励开发者亲自测试该功能。

---

## 19. DIY实验反应器利用伯克兰-艾德法

**原文标题**: DIY experimental reactor harnesses the Birkeland-Eyde process

**原文链接**: [https://blog.arduino.cc/2025/03/17/this-diy-experimental-reactor-harnesses-the-birkeland-eyde-process/](https://blog.arduino.cc/2025/03/17/this-diy-experimental-reactor-harnesses-the-birkeland-eyde-process/)

这篇博文重点介绍了公民科学家Marb利用伯克兰-艾德法自制的实验性反应器。伯克兰-艾德法是一种早期利用电弧从大气氮气中生产硝酸的方法，但由于其高能耗，不适用于大规模化肥生产。然而，Marb更感兴趣的是科学原理，而非化肥产量。

该反应器设计侧重于控制电弧和管理气流。Arduino UNO Rev3配合分线板，调节电源、变压器和升压转换器，以控制电弧电极。该系统还包括空气制备，将空气泵入装有干燥剂的管子，以确保干燥的空气进入反应室。包括温度传感器在内的传感器向Arduino提供关于反应条件的反馈。

Marb在一个视频中展示了该反应器的功能，但他承认需要进一步改进以最大限度地提高硝酸产量。他建议，如果社区有足够的兴趣，可以制作后续视频，提供更详细的信息。总而言之，这个项目是一个利用现代技术对历史科学过程的个人探索，优先考虑实验和学习，而不是实际的化肥生产。

---

## 20. 压倒性的负面和士气低落的力量

**原文标题**: An Overwhelmingly Negative and Demoralizing Force

**原文链接**: [https://aftermath.site/ai-video-game-development-art-vibe-coding-midjourney](https://aftermath.site/ai-video-game-development-art-vibe-coding-midjourney)

本文探讨了人工智能融入对视频游戏开发者产生的负面影响，重点关注艺术家、设计师和软件开发者被迫在工作流程中使用人工智能的经历。

主要担忧包括：

*   **士气低落和价值贬低：** 开发者被迫使用人工智能来完成他们受雇去做的工作时，会觉得自己的专业知识受到损害，导致积极性降低。
*   **低效且劣质的产出：** 人工智能生成的代码和艺术作品通常不准确，需要比传统方法花费更多的时间进行校正，并且缺乏源于人类经验的创造力和背景。
*   **伦理问题：** 人工智能引发了与剽窃、同意（尤其是在配音演员肖像方面）以及潜在的职位流失相关的伦理问题。
*   **误导性的实施：** 管理者通常为了节省成本或认为可以提高效率而优先考虑人工智能，却不了解它的局限性，也没有考虑到对员工和创作过程的有害影响。
*   **“人工智能即解决方案”的谬论：** 人工智能的支持者经常将现有的游戏开发流程视为需要解决的问题，而忽略了人类互动、迭代和艺术劳动在创造引人入胜和创新的游戏中的价值。

本文强调了人工智能的所谓益处与它对游戏开发的实际影响之间日益扩大的脱节，在游戏开发中，它正成为一种不受欢迎且适得其反的力量。

---

## 21. 展示一下：我也做了一个文字游戏。我妈反应平平，但我自己觉得挺酷。

**原文标题**: Show HN: I also built a word game. My mom is indifferent, but I think its ccool

**原文链接**: [https://playletterlinks.com/](https://playletterlinks.com/)

“Show HN”帖子介绍LetterLinks：一款类似于拼字游戏的每日组词游戏。玩家获得一组字母方块，必须将它们排列在棋盘上以创建有效单词并最大化得分。主要功能包括：

*   **每日挑战：** 每天每个人都获得相同的字母方块，以进行公平竞争。
*   **棋盘布局：** 棋盘包含特殊格子，例如双字母 (DL)、三字母 (TL)、双字 (DW) 和三字 (TW)，以提高分数。
*   **游戏玩法：** 可以拖动或点击方块来放置它们，单词必须连接，并且必须使用中心星形格子。
*   **特殊方块：** 百搭牌代表任何字母，奖励方块使整个单词的分数翻倍。
*   **每日奖励挑战：** 礼物图标显示特殊单词模式以获得奖励积分（1.5 倍或 2 倍）。
*   **得分：** 分数基于字母值和奖励格子。存在乘数（水平和垂直）。
*   **提交：** 放置方块后，玩家提交他们的单词以获得评分。无效单词会被突出显示。
*   **排行榜：** 玩家可以输入昵称以将他们的分数保存在每日排行榜上，并与其他人进行比较。
*   **技能等级：** 通过基于分数的技能等级来跟踪进度。
*   **教程：** 游戏包含交互式教程和一个“如何玩”部分，解释规则和功能。

创作者，其母亲“漠不关心”，表达了对游戏的个人热情。

---

## 22. 用 Prolog 解决“雷顿教授的谜题”

**原文标题**: Solving a “Layton Puzzle” with Prolog

**原文链接**: [https://buttondown.com/hillelwayne/archive/a48fce5b-8a05-4302-b620-9b26f057f145/](https://buttondown.com/hillelwayne/archive/a48fce5b-8a05-4302-b620-9b26f057f145/)

本文详细介绍了作者使用Prolog编程语言解决一个类似“雷顿”系列游戏中逻辑谜题的探索过程。该谜题涉及根据其他三名学生对一个是非题测验的答案和分数，推断出第四名学生的考试分数。

作者将他们的Prolog解决方案与Pablo Meier之前的解决方案进行比较，旨在实现更优雅、更简洁的实现。他们介绍了Prolog的基本概念，如合一、模式匹配，以及使用`dif`和`clpfd`库分别处理不等式约束和有限域约束。解决方案的核心围绕着一个递归的`score/3`谓词，该谓词根据学生的答案和答案键计算学生的分数。

Prolog的一个关键优势是双向性，允许`score/3`谓词用于检查分数、计算分数，甚至生成可能的答案集。文章随后演示了如何使用`maplist`来简洁地定义答案键的约束（长度和可能的值）。

令人惊讶的发现是，存在多个有效的答案键，但所有这些答案键都导致第四名学生的分数相同，这突显了谜题的巧妙设计。作者将这种解谜应用与Prolog更实际的用途进行对比，例如分析版本控制提交图和规划基础设施变更，这将是他们即将出版的书中的一个章节重点。最终的Prolog代码比最初的解决方案短得多。

---

## 23. ClickHouse 中 Rust 的一年

**原文标题**: A year of Rust in ClickHouse

**原文链接**: [https://clickhouse.com/blog/rust](https://clickhouse.com/blog/rust)

ClickHouse将Rust集成到C++代码库的一年实验

---

## 24. Netflix 如何准确地归因 eBPF 流日志

**原文标题**: How Netflix Accurately Attributes eBPF Flow Logs

**原文链接**: [https://netflixtechblog.com/how-netflix-accurately-attributes-ebpf-flow-logs-afe6d644a3bc](https://netflixtechblog.com/how-netflix-accurately-attributes-ebpf-flow-logs-afe6d644a3bc)

Netflix如何解决将eBPF流日志准确归因于云环境中工作负载身份的问题

他们的解决方案包括两个关键改进：

1.  **在源头归因本地IP地址：** FlowExporter（作为sidecar运行）现在会在发送流日志之前确定本地工作负载身份。 对于EC2实例，它读取证书。 对于容器化工作负载（Titus），它使用IPMan（一个容器IP地址分配服务），该服务将IP地址到工作负载ID的映射写入eBPF maps。 针对IPv6到IPv4转换实现了特殊处理，以正确归因sockets。

2.  **使用时间范围归因远程IP地址：** FlowCollector使用来自FlowExporter日志的本地IP地址、本地工作负载身份和连接时间戳，构建一个IP地址所有权时间范围的内存哈希图。 这使得FlowCollector能够准确确定在流开始时哪个工作负载拥有远程IP地址。 FlowCollector节点通过Kafka共享时间范围信息。 流在归因之前会暂时存储一分钟，以确保时间范围信息是最新的。

改进后的方法通过将跨区域流转发到正确区域的FlowCollector节点来处理它们。 非工作负载IP地址（例如，来自ELB的IP地址）仍然使用Sonar进行归因。 针对Zuul的路由配置（作为其依赖关系的真理来源）进行的验证确认了误归因已被消除。

这种新方法为依赖性分析、安全性和事件响应提供了可靠且准确的流日志，从而增强了对Netflix分布式系统的理解。

---

## 25. 将30万的阶乘分解为30万个大于10万的因子之积

**原文标题**: Decomposing factorial of 300K as the product of 300K factors larger than 100K

**原文链接**: [http://gus-massa.blogspot.com/2025/04/decomposing-factorial-of-300k-as.html](http://gus-massa.blogspot.com/2025/04/decomposing-factorial-of-300k-as.html)

本文详细介绍了一项尝试解决陶哲轩提出的挑战：将300,000!分解为300,000个大于100,000的因子。作者使用了陶哲轩的方法，该方法包括创建一个底数'B'，作为大于100,000的奇数的乘积，然后通过用乘以2的幂的“N!-重”素数（在300,000!中比在B中出现更频繁的素数）替换“B-重”素数（在B中比在300,000!中出现更频繁的素数）来调整它。

作者使用Racket重现了陶哲轩将300,000!分解为大于90,000的因子的最初结果。该代码分解了300,000!和初始底数'B'，识别出“B-重”和“N!-重”素数。文章强调了计算中遇到的与陶哲轩的结果相比的差异（具体来说，是50个额外的素数）。

然后，作者提出了两种通过按顺序匹配来平衡素数的方法，用'1'填充较短的列表（N!-重素数）。文章比较了结果，重点关注未使用的2的幂的数量，并验证了生成的转换表。最终，作者旨在优化2的映射和使用，以实现大于100,000的因子的原始目标。

---

## 26. 感谢HN：我6周前在此发布的益智游戏获得了《大西洋月刊》的授权

**原文标题**: Thank HN: The puzzle game I posted here 6 weeks ago got licensed by The Atlantic

**原文链接**: [https://www.theatlantic.com/games/bracket-city/](https://www.theatlantic.com/games/bracket-city/)

这款“感谢HN”帖子庆祝一款解谜游戏《括号城市》(Bracket City)的诞生，该游戏由个人创作，六周前首次在Hacker News上分享。 重要的进展是《括号城市》现在已被知名出版物《大西洋月刊》(The Atlantic)授权。这表明游戏的质量和吸引力得到了认可，从而促成了专业的合作和更广泛的发行。 这篇帖子本质上是一个成功故事，突出了Hacker News社区在为独立创作者提供发现和潜在机会的平台方面的积极影响。它暗示，将游戏发布在HN上，在引起《大西洋月刊》的注意方面发挥了作用。

---

## 27. 解析组合学——一个实例

**原文标题**: Analytic Combinatorics – A Worked Example

**原文链接**: [https://grossack.site/2025/04/08/analytic-combinatorics-example.html](https://grossack.site/2025/04/08/analytic-combinatorics-example.html)

本博文探讨如何使用解析组合学，特别是奇点分析，来寻找组合问题的渐近近似，并通过两个使用Sage的实例进行演示。

首先，作者回顾了计数有根有序三叉树，找到一个生成函数和节点数为*n*的树的数量的渐近近似。该近似是使用留数定理和生成函数的主导奇点附近的Puiseux级数展开推导出来的。提供了Sage代码来计算奇点、Puiseux展开和渐近常数。

然后，这篇文章解决了一个更具挑战性的问题：计数同构意义下的无序有根三叉树。使用Pólya-Redfield计数来推导生成函数的一个泛函方程。作者概述了如何使用隐函数定理和Puiseux级数来估计泰勒系数。

该方法涉及找到一个奇点(r, s)，其中泛函方程F(z,w) = 0及其对w的偏导数都消失。然后构造一个T在(r, s)处的Puiseux级数。这导致了无序三叉树数量的渐近近似。同样，Sage代码近似泰勒级数，以数值方式找到奇点，并确认最终的渐近近似。

---

## 28. 脊椎动物的智力至少进化过两次

**原文标题**: Intelligence Evolved at Least Twice in Vertebrate Animals

**原文链接**: [https://www.quantamagazine.org/intelligence-evolved-at-least-twice-in-vertebrate-animals-20250407/](https://www.quantamagazine.org/intelligence-evolved-at-least-twice-in-vertebrate-animals-20250407/)

脊椎动物的智力是源于共同祖先还是鸟类和哺乳动物独立进化而来？最近的研究表明后者，并提供了证据表明，支持智力的复杂神经回路在这两个群体中是分别出现的。

长期以来，科学家们认为智力需要新皮层，一种在哺乳动物中发现的分层大脑结构。鸟类缺乏这种结构，因此被认为智力较低。然而，研究表明，尽管鸟类的大脑结构不同，但它们也拥有先进的认知能力。

争论的焦点在于，支持智力的神经回路是从共同祖先那里继承来的，还是独立进化而来的。虽然早期的研究由于相似的回路而指向共同祖先，但后来对胚胎发育的研究表明是独立进化。

新的研究使用单细胞RNA测序比较了鸡、小鼠和壁虎的大脑发育。这些研究表明，虽然成熟的动物大脑回路看起来很相似，但它们的发育方式、时间和大脑区域都不同。他们还发现，相似的电路可以用不同的细胞类型构建。这些发现表明，鸟类和哺乳动物的大脑中用于复杂认知的区域是独立进化而来的。

然而，存在一些影响大脑发育的遗传相似性，表明存在从共同祖先那里继承的有限遗传。尽管存在独立进化，但脊椎动物的智力发展途径存在限制，趋同进化证明了这一点。了解生物体为解决复杂问题而开发的不同神经解决方案，可能为人工智能的发展和寻找外星智能提供见解。

---

## 29. Show HN: Coroot – 基于 eBPF 的开源可观测性平台，提供可操作的洞见

**原文标题**: Show HN: Coroot – eBPF-based, open source observability with actionable insights

**原文链接**: [https://github.com/coroot/coroot](https://github.com/coroot/coroot)

Coroot 是一个开源可观测性平台，它使用 eBPF 自动收集指标、日志、链路和剖析数据，无需代码插桩。其目标是从可观测性数据中提供可操作的洞察，超越简单的数据收集。

主要功能包括：

*   **零插桩可观测性：** 基于 eBPF 的收集消除了代码更改的需求。
*   **服务地图：** 提供系统的完整视图，没有盲点。
*   **应用健康摘要：** 总结服务状态并提供对应用程序日志的洞察。
*   **SLO 跟踪：** 监控服务级别目标，并通过分布式追踪允许异常请求探索。
*   **厂商中立的插桩：** 通过 eBPF 与遗留和第三方服务一起工作。
*   **日志模式分析：** 使用事件聚类进行日志洞察，并基于 ClickHouse 实现快速搜索的无缝日志到链路关联。
*   **剖析：** 启用一键式应用程序剖析，以分析资源使用情况直至代码级别。
*   **内置专业知识：** 自动识别常见问题，并根据 SLO 提供整合的警报。
*   **部署跟踪：** 监控 Kubernetes 滚动更新，并在不进行 CI/CD 集成的情况下比较版本的性能下降情况。
*   **成本监控：** 在应用程序级别跟踪云成本，而无需访问云帐户。
Coroot 可以通过 Docker 或 Kubernetes 安装。文档、实时演示和社区支持可通过各种渠道获得。它基于 Apache License 2.0 许可。

---

## 30. 你的ext4文件系统中文件的顺序并不重要

**原文标题**: The order of files in your ext4 filesystem does not matter

**原文链接**: [https://thewisenerd.com/blog/ext4-readdir/](https://thewisenerd.com/blog/ext4-readdir/)

节点镜像补丁更新后，ext4 文件系统意外的文件顺序变化导致 JVM 类路径问题，一段令人沮丧的调试之旅。作者的 JVM 工作负载依赖于类路径的通配符扩展，JVM 使用 `readdir` 列出 JAR 文件。核心问题是 `readdir` 的顺序，受到 ext4 的“哈希 b 树”目录缓存和“目录哈希种子”的影响，在更新后发生了变化，导致错误的 JAR 文件首先被加载，出现未捕获的 `NoSuchFieldError`，导致应用程序初始化失败。

作者最初追查了几个转移注意力的线索，包括：

*   **Buildah 压缩层：** 团队切换到了 Buildah，并怀疑层压缩导致了类路径优先级问题，但这并非根本原因。
*   **OverlayFS 层顺序：** 作者最初认为 overlayfs 决定了 `readdir` 的顺序，但测试证明这是不正确的。OverlayFS 仅保证上层覆盖下层，而不是迭代顺序。
*   **层提取逻辑：** 作者怀疑层提取过程发生了变化，因此仔细地复制了 containerd 的提取逻辑并验证了 inode 顺序，但问题仍然存在。

通过检查 ext4 文件系统本身，取得了突破。目录哈希种子被确定为罪魁祸首。该种子随着节点镜像补丁的更新而改变，从而改变了 `readdir` 返回文件的顺序。作者随后成功地对磁盘镜像进行了十六进制编辑，以恢复原始的目录哈希种子，从而确认了修复。根本原因涉及三个 Bouncy Castle 提供程序 JAR，其中由于 `readdir` 的顺序，加载了错误的版本，导致初始化失败。

---

## 31. 如何通过啄木鸟的鼓声来识别它们

**原文标题**: How to Recognize Woodpeckers by Their Drumming Sounds

**原文链接**: [https://www.allaboutbirds.org/news/how-to-recognize-woodpeckers-by-their-drumming-sounds/](https://www.allaboutbirds.org/news/how-to-recognize-woodpeckers-by-their-drumming-sounds/)

本文解释了如何通过啄木鸟的鼓击声来识别它们。鼓击不同于觅食时的啄击，是一种交流方式，类似于鸟鸣，用于确立领地和吸引配偶。最佳聆听时间是春季。啄木鸟通常选择金属物体等响亮、共鸣的表面来最大化声音。

本文将鼓击模式分为三种主要类型：稳定、均匀的鼓击；断续节奏；以及渐弱。稳定的鼓击很常见，物种识别依赖于速度和持续时间的细微差异。绒啄木鸟的鼓击速度较慢（每秒17次），时间较短，而毛啄木鸟的鼓击速度较快（每秒26次），时间较长。类似的区分适用于纳氏啄木鸟（每秒20次）和梯背啄木鸟（每秒30次）。北扑翅鴷的鼓击持续时间比许多其他物种长（每秒23次）。

吸汁啄木鸟可以通过其“断续”节奏来识别，其特征是先有一个介绍性的连击，然后是不均匀、不规则间隔的敲击。黄腹、红颈和红胸吸汁啄木鸟具有相似的鼓击模式。威廉逊吸汁啄木鸟有一个变体，即多次敲击而不是双重敲击。

大啄木鸟、黑背啄木鸟和美洲三趾啄木鸟表现出“渐弱”鼓击，其中鼓击要么加速，要么音量在最后逐渐减弱。大啄木鸟的鼓击速度较慢（每秒15次），并有加速部分。美洲三趾啄木鸟的鼓击速度较慢（每秒14次），并且鼓击在最后加速。黑背啄木鸟的鼓击速度较快（每秒16次），并且音量略有加速和渐弱。

本文鼓励听众注意鼓击的速度、持续时间和模式，并利用频谱图等资源进行可视化分析。

---

## 32. 美国机床工业的衰落与复苏前景 (1994)

**原文标题**: The Decline of the U.S. Machine-Tool Industry and Prospects for Recovery (1994)

**原文链接**: [https://www.rand.org/pubs/research_briefs/RB1500.html](https://www.rand.org/pubs/research_briefs/RB1500.html)

这份1994年兰德公司的研究报告探讨了美国机床工业的衰落及其复苏前景。机床工业是制造业和国防的关键部门，曾一度是全球领导者，但在20世纪80年代因国内需求下降、订单交付速度慢于日本公司以及美元坚挺等因素而显著衰落。值得注意的是，日本公司成功地将美国发明的数控技术商业化。

该研究指出了阻碍复苏的根本问题，包括向全球竞争的转变和快速的技术变革，这需要美国公司缺乏的新能力。障碍包括缺乏大型公司或小型公司之间缺乏强有力的合作、难以获得投资资金、劳动力技能不足、研究成果转化为适销产品的能力薄弱以及国内需求不够成熟。有限的出口能力进一步阻碍了复苏。

尽管面临这些挑战，该研究表明可以保持乐观。内部重组、国内需求的激增以及竞争对手日本和德国工业的危机都提供了机遇。美国在关键技术方面保持着研究领先地位。

该研究建议采取三管齐下的政府战略：促进机床制造商、用户和供应商之间的地方合作网络；增加对制造业基础设施（研发和技能培训）的投资；并通过简化出口程序、支持销售工作和避免保护主义来帮助美国公司参与国际竞争。该研究强调要更广泛地努力改进美国的制造工艺技术，并断言全球影响力对于美国机床公司长期繁荣至关重要。

---

## 33. 中国上调美国商品关税至84%，争端升级

**原文标题**: China Raises Tariffs on US Goods to 84% as Rift Escalates

**原文链接**: [https://www.bloomberg.com/news/articles/2025-04-09/china-raises-tariffs-on-us-goods-to-84-as-trade-rift-escalates](https://www.bloomberg.com/news/articles/2025-04-09/china-raises-tariffs-on-us-goods-to-84-as-trade-rift-escalates)

无法访问文章链接。

---

## 34. 日本乡下小镇中年男子交易卡牌走红

**原文标题**: Middle-aged man trading cards go viral in rural Japan town

**原文链接**: [https://www.tokyoweekender.com/entertainment/middle-aged-man-trading-cards-go-viral-in-japan/](https://www.tokyoweekender.com/entertainment/middle-aged-man-trading-cards-go-viral-in-japan/)

在日本乡村小镇河原，一种以当地中年男性（“叔叔”）为主角的独特集换式卡牌游戏（TCG）在儿童中迅速走红，为像宝可梦这样的流行游戏提供了一种令人耳目一新的选择。这款“叔叔卡牌游戏”由斋藤社区委员会的宫原惠理创作，旨在加强年轻一代和年长一代之间的联系。

这些卡牌展示了47位不同的“叔叔”，每张卡牌都具有统计数据、特殊能力和元素类型，反映了他们在现实生活中的技能和对社区的贡献。例子包括曾担任消防队长的“防火墙本田先生”和教授面条制作的“荞麦面大师竹下先生”。最受欢迎的卡牌是前监狱官、现社区志愿者的“万事通藤井先生”。

最初的设计目的是用于收集，但河原的孩子们很快就开发出了一种战斗元素，比较统计数据和技能。卡牌的稀有度与“叔叔”在现实世界中参与社区服务的程度直接相关，积极的志愿者有机会出现在备受追捧的闪卡上。

这款游戏的成功促使人们更多地参与当地活动，并重新认识到社区长者的价值。这些手工制作的卡牌仅在斋藤社区中心出售，三张一包售价100日元，六张一包（包括一张闪卡）售价500日元。尽管供应有限，但需求仍然非常高。

---

## 35. I, II 或 III 级肥胖与健康结果的关联

**原文标题**: Associations Between Class I, II, or III Obesity and Health Outcomes

**原文链接**: [https://evidence.nejm.org/doi/10.1056/EVIDoa2400229](https://evidence.nejm.org/doi/10.1056/EVIDoa2400229)

无法访问文章链接。

---

## 36. 最伟大的摩托车照片

**原文标题**: The Greatest Motorcycle Photo

**原文链接**: [https://www.life.com/arts-entertainment/the-greatest-motorcycle-photo-ever/](https://www.life.com/arts-entertainment/the-greatest-motorcycle-photo-ever/)

本文旨在致敬罗利·弗里于1948年9月13日在犹他州邦纳维尔盐滩创下摩托车世界速度纪录的标志性照片。为了最大限度地减少风阻，弗里仅穿泳裤，以水平姿势趴在他的Vincent HRD Black Shadow摩托车上，并最终达到了每小时150.313英里的速度。

这张由《生活》杂志摄影师彼得·斯塔克波尔拍摄的照片已成为摩托车界的传奇，也是广受欢迎的印刷品。文章指出，《生活》杂志在最初的报道中使用了不同的广角镜头，强调了广阔的景观。其他展示他骑行前准备工作的照片也是经典之作，证明了当时的摄影风格。

虽然弗里的纪录早已被打破，但文章将他大胆的壮举与现代的速度记录方式进行了对比。洛基·罗宾逊于2010年创下了每小时376.363英里的当前纪录，他使用的是流线型的封闭车辆，无需任何非常规的、上镜的动作。这突显了弗里打破纪录的壮举以及由此产生的标志性图像的历史意义和持久魅力。

---

## 37. NNN：营销组合建模的下一代神经网络

**原文标题**: NNN: Next-Generation Neural Networks for Marketing Mix Modeling

**原文链接**: [https://arxiv.org/abs/2504.06212](https://arxiv.org/abs/2504.06212)

这篇arXiv文章(arXiv:2504.06212)介绍了“NNN：用于营销组合建模的下一代神经网络”，一种新的MMM方法。该论文由Thomas Mulc等人撰写，提出了一种基于Transformer的神经网络（NNN），以克服传统MMM方法的局限性。

与依赖于标量输入和参数衰减函数的传统方法不同，NNN利用丰富的嵌入来表示营销和自然渠道的定量和定性方面，例如搜索查询和广告创意。其注意力机制使模型能够捕获复杂的交互和长期影响，从而可能提高销售归因的准确性。作者强调使用L1正则化，以使表达力强的模型在数据受限的环境中可行。

该论文通过在模拟和真实世界数据上的评估，证明了NNN的有效性，显示出预测能力的显著提高。此外，NNN通过允许模型探测以评估特定关键词或创意的有效性，提供了超出归因的可解释性，从而提供了有价值的见解。该文章被分类在机器学习(cs.LG)和应用(stat.AP)下。

---

## 38. “氟化物降低智商”报告应被撤回

**原文标题**: „Fluoride reduces IQ" report needs to be retracted

**原文链接**: [https://twitter.com/cremieuxrecueil/status/1909865076271563065](https://twitter.com/cremieuxrecueil/status/1909865076271563065)

提供的文本并非关于氟化物和智商的文章。它来自X（前身为Twitter）的JavaScript错误消息，表明用户的浏览器中禁用了JavaScript，导致页面无法正确加载。其中没有任何关于氟化物或其对智商的潜在影响的讨论。

因此，无法提供有关所谓的“氟化物降低智商”报告的摘要，因为上下文纯粹是技术性的，并且不相关。

---

## 39. 建造System/360大型机差点毁了IBM

**原文标题**: Building the System/360 Mainframe Nearly Destroyed IBM

**原文链接**: [https://spectrum.ieee.org/building-the-system360-mainframe-nearly-destroyed-ibm](https://spectrum.ieee.org/building-the-system360-mainframe-nearly-destroyed-ibm)

本文详细介绍了IBM System/360大型主机的发展历程。该产品于1964年发布，彻底改变了计算机行业，但也几乎导致该公司破产。20世纪50年代末，IBM面临一个关键问题：客户需要比流行的1401更强大、更易于升级的系统。替代方案是为竞争对手的机器进行昂贵的软件重写。在内部，IBM面临着恩迪科特和波基普西的工程师之间的内部竞争，他们各自开发不兼容的系统。

T. Vincent Learson和Bob O. Evans率先提出了解决方案，主张采用单一的兼容系统，这导致波基普西的8000项目被取消，并催生了System/360。S/360被设计成一个兼容的计算机家族，共享软件和外围设备。该公司投资了50亿美元（相当于今天的400亿美元），并雇用了7万名员工。

1964年4月7日，IBM发布了150款新产品，其中包括六台计算机和大量外围设备。该系统的兼容性是一个关键卖点，允许客户在不进行大量重写的情况下进行升级。虽然风险很大，早期型号仅仅是模型，但发布取得了成功，第一个月就产生了超过10万份订单，并永远改变了计算格局。它确立了IBM在该行业的主导地位。

---

## 40. 显示 HN：声景和 Lo-fi 播放器

**原文标题**: Show HN: Soundscapes and Lofi Player

**原文链接**: [https://www.noisefill.com/](https://www.noisefill.com/)

此“Show HN”帖子介绍 Noisefill，一个播放音景和 Lo-fi 音乐的 Web 应用程序。内容极简，仅包含标题和单词“Noisefill”，以及一条指示需要 JavaScript 才能运行该应用程序的消息。这暗示 Noisefill 严重依赖 JavaScript 来实现其功能和用户界面。帖子的简洁性表明它旨在快速介绍一个可能更复杂的 Web 应用程序，用于生成和收听环境声音和/或 Lo-fi 音乐。

---

## 41. 展示一下：我做了一个文字游戏。我的物理老师很喜欢。你呢？

**原文标题**: Show HN: I built a word game. My Physics teacher likes it. What about you?

**原文链接**: [https://thypher.com/](https://thypher.com/)

“Show HN”：Thypher - 一款解方程猜词游戏

作者推出了一款名为Thypher的猜词游戏。核心玩法是通过解方程来揭晓一个5个字母的单词。

游戏规则很简单：玩家必须通过数学方程式找出对应的字母，从而确定每日的5字母单词。例如，帖子中展示了 `mc^2 = E`。游戏不区分大小写。

今天的单词是2025年4月9日的，也是游戏的第48个单词。帖子包含一个“Play”链接，鼓励用户尝试。作者强调他的物理老师很喜欢这款游戏，暗示了它的教育性和趣味性。帖子的主要目的是分享这款游戏并征求Hacker News社区的反馈。

---

## 42. 赴美旅行时如何锁定你的手机

**原文标题**: How to lock down your phone if you're traveling to the U.S.

**原文链接**: [https://www.washingtonpost.com/technology/2025/03/27/cbp-cell-phones-devices-traveling-us/](https://www.washingtonpost.com/technology/2025/03/27/cbp-cell-phones-devices-traveling-us/)

无法访问文章链接。

---

## 43. 难民营中的经济学启示

**原文标题**: What a refugee camp reveals about economics

**原文链接**: [https://www.economist.com/finance-and-economics/2025/04/03/what-a-refugee-camp-reveals-about-economics](https://www.economist.com/finance-and-economics/2025/04/03/what-a-refugee-camp-reveals-about-economics)

本文探讨了马拉维的扎莱卡难民营的经济现实。该难民营自1994年以来一直收容难民。虽然难民营看起来可能像一个典型的周日，人们去教堂和观看足球比赛，但关键的区别在于，居民们并非在一周的工作后休息。

文章强调，营地里的每个人每月得到9美元，这引发了一个问题：在如此有限的资源下，经济如何运作？作者旨在揭示在这个独特环境中出现的经济活动、生存策略和社会动态。宗教和娱乐活动与潜在的经济困难并置，为考察难民营的微观经济奠定了基础。

本质上，本文试图将难民营作为一个缩影，来理解更广泛的经济原则，特别是人们如何在严重受限的情况下适应并创造经济机会。作者似乎暗示，通过研究扎莱卡的经济状况，我们可以获得对基本经济行为和原则的宝贵见解。

---

## 44. Show HN: 大约500行代码实现的向量嵌入HNSW索引

**原文标题**: Show HN: HNSW index for vector embeddings in approx 500 LOC

**原文链接**: [https://github.com/dicroce/hnsw](https://github.com/dicroce/hnsw)

这个“Show HN”帖子介绍了一个轻量级（约500行代码）的 C++ 实现，用于向量嵌入中高效最近邻搜索的分层可导航小世界（HNSW）算法。它强调了单头文件、现代 C++ 设计，并利用 Eigen 进行 SIMD 加速的距离计算，从而实现快速性能。

HNSW 算法被解释为一个多层图结构，其中较高层稀疏填充，较低层更密集。节点连接到每一层中的最近邻。新节点被随机分配一个级别，并插入到该级别及其以下的所有级别中。搜索从顶层开始，迭代地找到最近的节点并下降到较低的层。该算法跟踪搜索期间遇到的 K 个最近邻，并在完成时返回它们。

该帖子包含一个简单的示例，演示了如何使用 `dicroce::hnsw` 类创建索引、添加向量并执行最近邻搜索。该示例使用 128 维向量并搜索 10 个最近邻。还提供了使用 CMake 的编译说明。总的来说，这篇文章重点介绍了一个简洁高效的 C++ 库，用于使用 HNSW 算法进行向量嵌入搜索。

---

## 45. 没有大象：图像生成技术的突破

**原文标题**: No elephants: Breakthroughs in image generation

**原文链接**: [https://www.oneusefulthing.org/p/no-elephants-breakthroughs-in-image](https://www.oneusefulthing.org/p/no-elephants-breakthroughs-in-image)

伊森·莫里克的文章《没有大象：图像生成领域的突破》探讨了人工智能图像生成方面的重大进展，特别是向多模态图像生成方向的转变，并将其与以前的方法进行了对比。

此前，大型语言模型会为单独的图像生成工具生成图像提示，导致生成的图像不够智能，且常常存在缺陷。由谷歌和OpenAI率先推出的多模态图像生成技术，允许人工智能直接控制图像的创建，逐个令牌进行，类似于文本生成。这会产生更精确、更智能和更高质量的图像，保证提示的遵守（比如没有大象！）。

文章强调了使用图像进行提示的力量，强调需要像基于文本的人工智能一样，提供清晰的指示、反馈和背景信息。莫里克通过使用GPT-4o的示例展示了其能力，包括信息图表的创建、图像修改（改变颜色、修复错误）以及想象力丰富的场景（水獭在飞机上）。他还展示了它在创建广告原型、家具交换和网站模型中的实用性。

莫里克承认这种技术可能对各个领域造成颠覆，但也提出了重要的伦理问题，包括人工智能生成的艺术风格迁移、版权问题、深度伪造以及潜在的偏见。他总结道，多模态人工智能正在重塑视觉创作，模糊了人类和人工智能创造力之间的界限，需要认真考虑原创性和创意专业的未来。这种转变将需要周全的框架来应对这项技术带来的伦理和实践挑战。

---

## 46. Show HN: Badgeify – 让任何App都能驻留在Mac菜单栏

**原文标题**: Show HN: Badgeify – Add Any App to Your Mac Menu Bar

**原文链接**: [https://badgeify.app/](https://badgeify.app/)

Show HN上的“Badgeify”文章解决了新MacBook上Mac菜单栏图标消失在刘海后面的常见问题。它提供了从简单的内置macOS设置到更强大的第三方应用程序的解决方案。

核心问题是菜单栏上的空间有限，尤其是在带刘海的MacBook上，导致图标被遮挡。 该文章承诺为用户提供管理和优化菜单栏布局的方法。 这包括解释如何利用macOS的内置选项来组织和优先显示图标。

除了原生解决方案外，该文章暗示将引入“强大的第三方工具”，以进一步增强菜单栏管理。 这些工具可能提供以下功能：

*   隐藏不常用的图标。
*   重新排列图标顺序以获得更好的可访问性。
*   如果菜单栏过于拥挤，可能会将图标移动到单独的位置。

最终，该文章的目标是使用户能够保持干净、有条理且功能齐全的菜单栏，确保所有重要图标保持可见和可访问，即使受到刘海或一般屏幕空间限制的影响。

---

## 47. Paradigm (YC W24) 旧金山招聘创始工程师

**原文标题**: Paradigm (YC W24) Hiring Founding Engineers in SF

**原文链接**: [https://www.ycombinator.com/companies/paradigm/jobs/nFNWweP-founding-engineer](https://www.ycombinator.com/companies/paradigm/jobs/nFNWweP-founding-engineer)

Paradigm是一家由Y Combinator (W24)支持的初创公司，正在旧金山构建一个原生AI工作空间，现招聘创始工程师。该职位涉及全栈开发、用户互动、指标跟踪以及参与产品愿景和路线图制定。

理想的候选人是一位经验丰富的通才，能在快节奏的环境中茁壮成长，对人工智能充满热情，并痴迷于速度和规模。资格包括每周愿意到岗工作5-6天、拥有构建生产级AI产品的经验以及过往的成就。具备GoLang、TypeScript、NextJS、Redis、RAG系统和代理架构经验者优先。

薪酬为15万至25万美元的底薪，另有额外福利，包括慷慨的股权、健康保险、401k匹配、餐食、团队郊游以及潜在的奖金。

Paradigm获得了来自Dropbox、Intercom、Langchain和Redis等公司的知名人士的支持。他们的小团队拥有在Google、MIT、Microsoft和Citadel的工作经验。该公司的目标是以人工智能为核心，重新构想工作空间。

---

## 48. 中国将对美国商品加征最高84%的对等关税

**原文标题**: China to raise reciprocal tariffs on U.S. goods to 84%

**原文链接**: [https://www.cnbc.com/2025/04/09/china-to-raise-reciprocal-tariffs-on-us-goods-to-84percent.html](https://www.cnbc.com/2025/04/09/china-to-raise-reciprocal-tariffs-on-us-goods-to-84percent.html)

为回应美国总统唐纳德·特朗普不断升级的关税政策，中国宣布对美国商品征收84%的报复性关税，高于此前的34%，自4月10日起生效。此前，美国已将对中国商品的关税提高到100%以上。

文章强调了这种针锋相对的关税升级可能对这两个最大经济体之间的贸易造成的毁灭性影响。2024年，美国向中国出口了价值1435亿美元的商品，同时进口了4389亿美元的商品。

虽然一些国家似乎愿意谈判，但中国采取了强硬立场，迅速以反制关税回应。特朗普政府警告不要采取报复行动。在中国于4月2日做出初步回应后，特朗普实施了额外的50%的增长，使美国对中国商品的总进口税达到104%。

美国财政部长斯科特·贝森特批评中国不愿谈判，并称他们的经济是现代世界中最不平衡的经济体，声称升级对他们来说是“失败者”。在此之前，美国已经以阻止芬太尼进入美国为幌子，对中国、加拿大和墨西哥征收了关税。

贸易战震动了全球投资者，引发了对经济增长放缓、通货膨胀加剧和企业利润减少的担忧。这导致4月份出现大幅抛售，标准普尔500指数进入熊市。韩国、上海和香港的市场也经历了大幅下跌。

---

## 49. 神经涂鸦：用于大型语言模型的液态记忆层

**原文标题**: Neural Graffiti – Liquid Memory Layer for LLMs

**原文链接**: [https://github.com/babycommando/neuralgraffiti](https://github.com/babycommando/neuralgraffiti)

神经涂鸦是一种新型实验层，旨在为预训练的大型语言模型（LLM）实时注入一种神经可塑性。这是通过一个“喷涂层”实现的，该层将记忆痕迹直接注入LLM的最终推理阶段，而无需微调或重新训练。受大脑的神经可塑性和涂鸦艺术的启发，这一层会根据过去的互动微妙地改变模型的行为，从而随着时间的推移产生行为漂移。

其核心思想是通过将记忆和信息直接注入预训练模型的向量嵌入中来调节其行为，从而影响模型关联词汇和概念的方式。“喷涂层”不保证特定的词语输出，而是随着模型更多地互动，轻轻地引导它朝向某些概念，从而建立内部记忆。可以追踪每个输出中记忆层的影响。

该项目旨在培养AI模型的主动行为、聚合人格和增强的好奇心，通过允许它们“记住”过去的互动，潜在地导致一种自我意识的形成。虽然液态神经网络提供类似的功能，但它们的计算成本很高。神经涂鸦为现有的Transformer模型提供了一个更简单的“插件”解决方案。作者提醒说，使用这种技术可能会创造出具有特定精神宇宙的独特“实体”，可能不适合商业部署，但非常适合创建数字角色。

---

## 50. 代码科学家：用于代码实验的自动化科学发现系统

**原文标题**: CodeScientist: Automated scientific discovery system for code-based experiments

**原文链接**: [https://github.com/allenai/codescientist](https://github.com/allenai/codescientist)

CodeScientist是一个端到端的、半自动化的科学发现系统，专为基于代码的实验而设计，主要使用Python。它创新性地采用LLM作为突变器范例，结合科学文章和代码示例（包括LLM提示、绘图和基准测试），并应用基因突变来生成新颖的实验想法。

该系统使用实验构建器自动创建、运行和调试容器内的实验代码。然后，它会生成结果报告，通常会针对每个想法进行多次尝试（例如，五次）并进行荟萃分析。

CodeScientist有两种运行模式：人机协作模式（主要模式，涉及人工协助代码示例创建、实验筛选和反馈）和全自动模式（效率较低）。

该存储库包含：CodeScientist软件、实验报告（包括论文中的20个候选发现）、原始数据（代码、日志、想法、评审者评分）、安装说明和使用指南。

主要功能包括：从论文中创建新想法、手动创建实验、管理构思列表、运行批量自主实验、进行基准测试、监控实验、生成报告和过滤预生成的想法。它还允许用户添加自定义代码块，并利用实验构建器沙箱进行运行和调试。它提供了将CodeScientist的部分内容集成到其他代码库中的选项，并包含全面的文档。

---

## 51. 维沙普·奥伯龙编译器

**原文标题**: Vishap Oberon Compiler

**原文链接**: [https://github.com/vishapoberon/compiler](https://github.com/vishapoberon/compiler)

Ѵishap Oberon 是一种自由开源的 Oberon-2 编程语言实现，专为包括 Linux、BSD、Android、Mac 和 Windows 在内的各种操作系统设计。Vishap Oberon 编译器 (voc) 利用 C 后端（gcc、clang、tcc 或 msc）进行编译。它集成了来自 Ulm、oo2c 和 Ofront Oberon 编译器的库，并遵循 Oakwood Oberon-2 编译器指南。

安装过程包括克隆存储库，使用 "make full" 进行构建，可选择使用 "make install" 安装到系统目录，并设置 PATH 变量。 该编译器支持 Oberon-2，包括类型绑定过程，并在 SYSTEM.Mod 中扩展了对 64 位架构的支持。 整数和集合类型的大小可以使用编译器选项进行配置。

该编译器提供了来自各种 Oberon 系统（V4、S3、Ooc、Ulm、Oakwood）的丰富库集，方便代码移植。

Vishap Oberon 构建于 Josef Templ 的 Ofront 编译器之上，并由 Norayr Chilingarian 和 David Brown 进一步开发，增加了诸如广泛的库支持、跨平台兼容性和通用类型支持等功能。 该项目的名称灵感来自亚美尼亚的龙（"Vishaps"），并与将编译器与龙联系起来的传统相关联。

---

## 52. Show HN: 将 IBM 3151 终端连接到大型机 [视频]

**原文标题**: Show HN: Connecting an IBM 3151 terminal to a mainframe [video]

**原文链接**: [https://www.youtube.com/watch?v=V14ac9cRi9Q](https://www.youtube.com/watch?v=V14ac9cRi9Q)

"Show HN"帖子内容为一个YouTube视频，关于将IBM 3151终端连接到大型主机。核心内容围绕连接此旧终端到大型主机系统的技术过程，以及可能涉及的经验。提供的内容片段实际上是YouTube的标准样板文本，表明该帖子本身可能除了视频链接之外没有提供更多细节。因此，理解连接的具体细节及其目的需要观看视频。

---

## 53. 来自90年代密码朋克邮件列表的十万封邮件

**原文标题**: 100k emails from the 90s Cypherpunk listserve

**原文链接**: [https://cypherpunk.timespan.vc/](https://cypherpunk.timespan.vc/)

这篇题为“来自90年代赛博朋克邮件列表的十万封邮件”的文章，承诺提供对90年代赛博朋克邮件列表中的大量邮件档案的访问权限。“加载消息...”表明内容仍在制作中或仅为占位符。如果标题的承诺能够兑现，那么该档案可能会涵盖与密码学、计算机科学、政治和法律相关的各种主题。它将深入了解赛博朋克运动形成时期，重要人物和普通参与者所提出的关注、辩论和技术解决方案。该档案的价值在于它有潜力作为理解互联网的知识和社会历史、数字行动主义的起源以及数字时代持续的隐私斗争的主要来源。分析这些邮件可以揭示密码技术的演变、数字货币等关键概念的出现以及现代数字权利运动的哲学基础。

---

## 54. 夏威夷诞生了一个狂野的“怪异系统”

**原文标题**: A wild 'freakosystem' has been born in Hawaii

**原文链接**: [https://www.bbc.com/future/article/20250403-the-new-hawaiian-freakosystem-emerging-on-oahu-accidentally-created-by-humans](https://www.bbc.com/future/article/20250403-the-new-hawaiian-freakosystem-emerging-on-oahu-accidentally-created-by-humans)

本文探讨了“新型生态系统”或“怪异生态系统”的出现，尤其是在夏威夷的欧胡岛上。这些生态系统由人类引入的非本地物种的混合物组成，它们形成了前所未见的、自我维持的系统。 欧胡岛曾是独特本地物种的避难所，但由于森林砍伐、引入的掠食者和疾病而发生了巨大变化，导致许多本地动植物灭绝。

像科里·塔沃特和杰夫·维森廷-布戈尼这样的科学家发现，非本地物种正在填补之前由已灭绝的本地物种所占据的生态位，甚至达到了传播剩余本地植物种子的程度。 这种令人惊讶的功能凸显了生态系统的适应性，即使它们是由随机组合的物种组成。

文章强调，由于人类活动，包括栖息地改变、气候变化和物种引入，这种新型生态系统在全球范围内变得越来越普遍。 例子包括荷兰创造咸水湖的沿海防御工事、巴西变成洪泛区的热带雨林，以及变成有价值栖息地的旧矿区。 虽然对这些新型生态系统的范围存在争议，但一些研究表明，到2100年，它们可能会覆盖地球的很大一部分。

这些生态系统的出现引发了关于传统保护策略的问题，这些策略旨在将环境恢复到人类出现之前的状态。 鉴于许多地区“实际上无法恢复”，生态学家们正在努力研究如何管理这些已改变的环境，以及是否应该专注于保护功能性，而不是仅仅根除非本地物种。 欧胡岛就像一个“水晶球”，让我们得以一窥人类影响深刻重塑地球生态系统的未来。

---

## 55. 展示一下：一款创作涂黑诗的工具

**原文标题**: Show HN: A tool for creating blackout poetry

**原文链接**: [https://bobbiec.github.io/blackout-poetry.html](https://bobbiec.github.io/blackout-poetry.html)

此Show HN帖子介绍了一款用于创作遮蔽诗的工具。用户界面似乎很简单：它允许用户输入Markdown格式的文本，然后通过将单词放在方括号中（例如，`[brackets]`）来指定要遮蔽的单词。标题和内容非常简洁，表明其直接的功能是允许用户选择性地删除单词，从而将文本转换为遮蔽诗艺术。

---

## 56. 公司为何不修复漏洞

**原文标题**: Why Companies Don't Fix Bugs

**原文链接**: [https://idiallo.com/blog/companies-dont-fix-bugs](https://idiallo.com/blog/companies-dont-fix-bugs)

文章“为什么公司不修复漏洞”剖析了为何即使是像臭名昭著的GTA Online加载时间问题这样显而易见的软件漏洞，也经常会持续存在，即使它们很容易修复。作者以GTA为例，一名程序员通过简单的代码更改大幅缩短了加载时间，以此来说明公司优先事项往往会掩盖用户体验。

核心问题不是开发人员无能，而是大型组织内部多种因素的汇合。首先，漏洞修复通常被标记为“技术债务”，如果它们与预先定义的路线图要求不直接一致，就会被降低优先级。其次，开发人员的流动和项目的转移会导致机构记忆丧失，从而导致被遗忘或被忽视的错误报告。第三，即使是对于小的修复，更改遗留代码的感知风险也会阻止开发人员解决旧的漏洞。最后，通过错误修复来改善用户体验通常缺乏与季度收益目标产生共鸣的直接、可量化的投资回报率。

作者认为，这不仅仅是Rockstar的问题，而是大型公司中的一个系统性问题，在这些公司中，对利润的追求和对严格流程的遵守掩盖了流畅用户体验的重要性。虽然t0st的修复是一次公关胜利，但它并没有解决开发过程中的根本问题。要点是，当前的系统经常将用户体验视为事后诸葛亮，只有在外部力量迫使他们这样做时才会解决问题。随附的评论强化了这一观点，前开发人员也表达了对漏洞被降低优先级的不满，尽管它们具有负面影响。

---

## 57. 图像文件的背叛 (2020)

**原文标题**: The Treachery of Image Files (2020)

**原文链接**: [http://beyondloom.com/blog/images.html](http://beyondloom.com/blog/images.html)

图像文件的背叛：一部数字艺术作品集，每件作品均为10x10像素的强烈蓝色正方形，以及艺术家为将它们创建为GIF文件所采用的精细且往往复杂的各种方法。该文档详细描述了每件作品所用的特定软件、操作系统和流程，突出了数字图像创建和操作中固有的挑战和怪癖。

这些作品展示了一系列方法，从简单地使用常用图像查看器截取自定义颜色的桌面（受到格式限制的阻碍），到在Sublime Text和Vim等文本编辑器中手动编写PPM图像代码，然后通过ImageMagick和FFmpeg进行转换。

更荒谬的是，通过编写汇编代码来制作GIF文件，却不得不裁剪掉一个无用的标头。一件作品涉及使用晦涩的K编程环境来生成图像，而另一件作品则依赖于向同事发送的简单电子邮件请求。

最极端的例子涉及运行带有GIMP的Linux虚拟机，使用名为“Charon”的物理传输USB驱动器来表示艺术品在“世界”之间的转移。最后一件作品使用Gnuplot渲染。

艺术家详细的脚注既是对数字图像（特别是GIF格式）的复杂性和潜在缺陷的文档，也是评论，以及看似简单的结果可能需要极其复杂的过程。这件作品是对艺术、技术以及软件经常出人意料的局限性之间交叉点的有趣探索。

---

## 58. Meta 被抓到在 AI 基准测试中作弊

**原文标题**: Meta got caught gaming AI benchmarks

**原文链接**: [https://www.theverge.com/meta/645012/meta-llama-4-maverick-benchmarks-gaming](https://www.theverge.com/meta/645012/meta-llama-4-maverick-benchmarks-gaming)

Meta 被指控利用其新的 Llama 4 模型（特别是 Maverick 模型）操纵 AI 评测基准。该公司向 LMArena 基准站点提交了一个 Maverick 的“实验性聊天版本”，该版本针对会话性进行了优化，从而获得了很高的 ELO 评分，并将其排在 OpenAI 的 4o 之上，仅次于 Gemini 2.5 Pro。然而，这个版本与公开提供的模型不同。

AI 研究人员发现了这种差异，引发了对基准结果有效性的担忧。LMArena 更新了其政策，以防止未来出现此类混淆，强调公平和可重复的评估。Meta 为其行为辩护，称他们尝试自定义变体，并且实验版本在 LMArena 上表现良好。

批评人士认为，为测试提交专门调整的模型，同时向公众发布不同的版本，会削弱基准测试对于实际性能的意义。独立 AI 研究员 Simon Willison 对此表示失望，称由于公开提供的模型不同，高分毫无价值。

进一步的指控出现，暗示 Meta 训练 Llama 4 模型以在基准测试中表现更好，同时隐藏其局限性。Meta 否认了这些说法，并将质量的波动归因于实施稳定问题。文章强调，基准测试正成为一个战场，而这一事件说明了 Meta 渴望被认为是 AI 领导者的急切心态，即使这涉及操纵系统。 Llama 4 的发布时间（周六）也因其不寻常的时间安排而受到质疑。

---

## 59. Cogito预览：IDA作为通往通用超级智能的途径

**原文标题**: Cogito Preview: IDA as a path to general superintelligence

**原文链接**: [https://www.deepcogito.com/research/cogito-v1-preview](https://www.deepcogito.com/research/cogito-v1-preview)

Deep Cogito 发布 Cogito v1：采用迭代提炼与放大（IDA）训练的开源 LLM（30 亿至 700 亿参数），旨在实现通用超人工智能。这些模型在标准基准测试中优于 LLaMA、DeepSeek 和 Qwen 等同规模的开源 LLM，其中 700 亿参数模型甚至超越了 Llama 4 109B MoE。

IDA 专注于迭代式自我改进，通过计算密集型子程序放大能力，然后将增强的智能提炼回模型的参数中。此过程规避了传统 LLM 训练中人为监督的限制，有可能超越人类水平的智能。

Cogito 模型可以运行在标准和推理模式下，并针对编码、函数调用和代理用例进行了优化。该团队计划很快发布更大的模型（高达 6710 亿参数）和改进的检查点。

文章强调了 IDA 相对于 RLHF 和从大型模型提炼的效率和可扩展性。这些模型可在 Huggingface、Ollama 上获得，并通过 Fireworks AI 和 Together AI API 提供。Deep Cogito 将自身定位为一家专注于构建通用超人工智能的公司，并积极招聘人才。他们感谢了各个开源团队和项目的贡献。

---

## 60. 使用令牌序列迭代范围

**原文标题**: Using Token Sequences to Iterate Ranges

**原文链接**: [https://brevzin.github.io/c++/2025/04/03/token-sequence-for/](https://brevzin.github.io/c++/2025/04/03/token-sequence-for/)

C++ Ranges性能瓶颈探究：`views::filter`与`views::take_while`的优化方案

---

## 61. 奥斯本电脑公司于1986年4月9日清算

**原文标题**: Osborne Computer liquidated April 9, 1986

**原文链接**: [https://dfarq.homeip.net/osborne-computer-liquidated-april-9-1986/](https://dfarq.homeip.net/osborne-computer-liquidated-april-9-1986/)

戴夫·法夸尔的这篇文章探讨了奥斯本电脑公司于1986年4月9日的破产清算。虽然通常归咎于“奥斯本效应”——即过早宣布奥斯本行政型电脑，扼杀了对奥斯本1型电脑的需求——但法夸尔认为这是一种过度简化。

奥斯本1型电脑最初是成功的，但该公司未能充分沟通其与即将推出的行政型电脑之间的价格差异。潜在客户犹豫不决，预期价格相近，但新型号的较高成本阻碍了销售。法夸尔认为更好的沟通本可以减轻影响。

除了奥斯本效应之外，还有其他几个因素促成了该公司的倒闭。这些因素包括MS-DOS的崛起以及Compaq和Eagle Computer等公司提供具有竞争力的便携式电脑，以及CP/M市场的普遍衰落。奥斯本的广告缺乏关于IBM兼容性的清晰说明，进一步损害了其形象。

据报道，奥斯本的内部会计实务很差，该公司难以适应快速发展的计算机行业。其1986年的产品与1983年的型号过于相似，未能跟上技术进步的步伐。最终，营销失误、外部竞争和内部管理问题共同导致了奥斯本电脑公司的破产清算。法夸尔强调了从奥斯本的错误中吸取教训的重要性，突出了在快节奏的科技行业中清晰的沟通、适应性和强大的管理能力的重要性。

---

## 62. 弗兰克·劳埃德·赖特在俄亥俄州完成的“最后的乌托邦式住宅”

**原文标题**: "Final Usonian Home" by Frank Lloyd Wright Completed in Ohio

**原文链接**: [https://www.dezeen.com/2025/03/20/final-usonian-home-riverrock-frank-lloyd-wright-ohio-completed/?_hsenc=p2ANqtz--nulJz0XJo1E-jQIojcqaZmWjd0eXJ-oC35zKHYZb1UL94JLh6t_QI1k9lehp4fxwHKjPjkNeM-iQJihX705oJ-Maqyw&_hsmi=355439130](https://www.dezeen.com/2025/03/20/final-usonian-home-riverrock-frank-lloyd-wright-ohio-completed/?_hsenc=p2ANqtz--nulJz0XJo1E-jQIojcqaZmWjd0eXJ-oC35zKHYZb1UL94JLh6t_QI1k9lehp4fxwHKjPjkNeM-iQJihX705oJ-Maqyw&_hsmi=355439130)

文章报道了“河石”的竣工，该住宅被认为是弗兰克·劳埃德·赖特设计的最后一座乌托邦式住宅。 它位于俄亥俄州，于1951年设计，但在赖特生前从未建造。建筑历史学家约翰·G·索普三世发现了原始蓝图，并与弗兰克·劳埃德·赖特基金会合作，以确保住宅的竣工符合赖特的愿景。

“河石”体现了赖特的乌托邦理想，即为美国中产阶级提供经济实惠的现代住宅。它具有低矮的外形，木材和石头等天然材料以及旨在将居住者与自然联系起来的开放式平面图。 房屋的名称源于将河石融入其结构中，这是赖特设计中反复出现的主题。

重点突出的主要特征包括大量使用玻璃，这是赖特的标志性元素，它使自然光能够充满室内，并提供周围景观的全景视野。该房屋的另一个特点是其几何形状及其与场地的融合，反映了赖特的有机建筑理念。“河石”的竣工对于建筑爱好者来说是一件重要事件，也是弗兰克·劳埃德·赖特的设计经久不衰的相关性的证明。

---

## 63. 展示HN：一个帮助管理游戏库的网站/应用

**原文标题**: Show HN: A website/app to help manage your game library

**原文链接**: [https://gamenode.app](https://gamenode.app)

无法访问文章链接。

---

## 64. 糖精展现出对抗抗生素耐药性的意外能力

**原文标题**: Sweetener saccharin shows surprise power against antibiotic resistance

**原文链接**: [https://www.brunel.ac.uk/news-and-events/news/articles/Sweetener-saccharin-shows-surprise-power-against-antibiotic-resistance](https://www.brunel.ac.uk/news-and-events/news/articles/Sweetener-saccharin-shows-surprise-power-against-antibiotic-resistance)

伦敦布鲁内尔大学文章揭示惊人发现：常用人工甜味剂糖精可对抗抗生素耐药性。研究人员发现，糖精与现有抗生素联合使用，能显著增强抗生素对某些耐药细菌的疗效。

该研究聚焦于鲍曼不动杆菌等细菌，这是一种高度耐药的病原体，可引起严重感染。研究表明，糖精能使通常对这些耐药细菌无效的抗生素再次穿透细菌细胞并杀死它们。本质上，糖精充当“辅助分子”，破坏细菌的防御能力。

这一发现意义重大，因为它提供了一种潜在的新策略来应对日益严重的全球抗生素耐药性威胁。与开发全新的抗生素相比，重新利用像糖精这样广泛存在且广为人知的化合物，可能是一种更快、更具成本效益的新疗法开发途径。

研究团队目前正在探索糖精克服细菌耐药性的具体机制，并研究其对其他耐药细菌的疗效。这项研究可能促成新型抗生素组合的开发，从而有效治疗由耐药细菌引起的感染。

---

## 65. 纽约市最窄的自动扶梯

**原文标题**: The narrowest escalator in New York City

**原文链接**: [https://www.doobybrain.com/blog/the-narrowest-escalator-in-new-york](https://www.doobybrain.com/blog/the-narrowest-escalator-in-new-york)

本文重点介绍了位于纽约市洛克菲勒广场10号的最窄自动扶梯。作者Herman Yung称其非常狭窄，只能容纳单列乘客。该扶梯连接了街道层和位于地下的洛克菲勒中心广场的餐饮和购物区。

Yung建议，那些只想体验这条独特扶梯的人可以进入洛克菲勒广场10号，走下大型螺旋楼梯，然后乘坐扶梯返回街道层。他向读者保证，现场的安保人员并不介意人们以此目的使用扶梯，因为大堂内有一幅由Lakela Brown创作的极具视觉吸引力的环绕式壁画。

除了关于最窄自动扶梯的主题外，文章还包括Herman Yung其他文章的链接，这些文章大多关于纽约市的历史和地点，包括Brazenhead Books以及圣胡安山和林肯中心的历史。

---

## 66. Show HN: Uncurl.dev – 将 curl 命令转换为可分享、可执行的 UI

**原文标题**: Show HN: Uncurl.dev – Convert curl commands to a shareable, executable UI

**原文链接**: [https://uncurl.dev/](https://uncurl.dev/)

Uncurl.dev因严重安全漏洞已关闭。该服务本可以将`curl`命令转换为可分享、可执行的用户界面(UI)。开发者承认系统存在重大缺陷，允许用户获得托管该服务的虚拟专用服务器(VPS)的root权限。开发者甚至包含了一行代码`const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD || 'admin123'`，表明存在一个弱默认密码（或者缺乏密码，依赖环境变量），这显然不足以保证系统的安全。文章的核心信息是，该服务由于严重的安全风险而被有意关闭。

---

## 67. 印度维修文化赋予报废笔记本电脑新生

**原文标题**: India's repair culture gives new life to dead laptops

**原文链接**: [https://www.theverge.com/tech/639126/india-frankenstein-laptops](https://www.theverge.com/tech/639126/india-frankenstein-laptops)

在印度，强大的维修文化正赋予“报废”笔记本电脑新的生命，尤其是在德里的尼赫鲁广场和孟买的拉明顿路等市场。像Sushil Prasad这样的技术人员通过从废弃和过时的设备中回收零件来制造“弗兰肯斯坦”笔记本电脑。这些混合机器为学生、零工和因价格而被新市场拒之门外的小企业提供了经济实惠的计算选择。一台能用的笔记本电脑只需110美元左右就能买到，而一台新笔记本电脑则需要800美元。

然而，这个维修行业面临着挑战。全球科技公司经常限制备件的供应，并使用使维修变得困难的策略，从而促使消费者购买新产品和计划报废。印度政府正在考虑制定“维修权”法律来解决这个问题。

技术人员通常依赖像德里Seelampur这样的非正式电子垃圾市场，那里的工人会筛选废弃电子产品以寻找可用的零件。由于暴露于有毒物质中，这种电子垃圾回收利用存在健康风险。尽管面临挑战，对这些价格实惠的翻新笔记本电脑的需求正在增长。倡导者认为，正规化维修行业可以减少电子垃圾，创造就业机会，并改善技术获取途径。维修技术人员正在复活死亡的设备，弥合数字鸿沟，并证明维修生态系统注定会蓬勃发展。

---

## 68. Show HN: Browser MCP – 使用 Cursor、Claude、VS Code 自动化你的浏览器

**原文标题**: Show HN: Browser MCP – Automate your browser using Cursor, Claude, VS Code

**原文链接**: [https://browsermcp.io/](https://browsermcp.io/)

Browser MCP 是一款工具，它允许像 Cursor、Claude、VS Code 和 Windsurf 这样的 AI 应用在您的网页浏览器中自动执行任务。它弥合了 AI 编辑器和网页浏览器之间的差距，从而能够自动执行原本不可能完成的任务。

Browser MCP 的主要优势包括：

*   **自动化测试：** 允许 AI 执行端到端测试，验证 UI 元素，并确保应用程序在不同场景下的功能正常。
*   **任务自动化：** 自动执行重复的基于 Web 的任务，例如数据收集、表单填写和其他工作流程，从而节省时间并减少错误。
*   **速度、安全性和便利性：** 自动化在本地发生，提供快速的性能并保护用户隐私。它还利用现有的浏览器配置文件，保持用户登录状态，并利用真实的浏览器指纹来避免基本的机器人检测。

设置过程包括三个简单的步骤：安装 Browser MCP 扩展、在 AI 应用程序中设置 MCP 服务器以及开始自动化任务。

它提供一套浏览器工具，包括导航、后退/前进、等待、按键、快照、点击、拖放、悬停、输入文本、选择选项和获取控制台日志，从而实现全面的浏览器自动化。

---

## 69. 一个购物袋和一卡车的错失恐惧症

**原文标题**: A Supermarket Bag and a Truckload of FOMO

**原文链接**: [https://blog.julik.nl/2025/03/a-little-adventure-in-modern-frontend](https://blog.julik.nl/2025/03/a-little-adventure-in-modern-frontend)

本文记录了作者在新的 Rails 应用程序中使用 Tailwind CSS 4 的沮丧经历，其驱动力是对错过现代前端技术的恐惧（FOMO）。最初的障碍是他在老款 Mac Pro 上遇到的“SIGILL”错误，这是由于 Tailwind 4 依赖于他的 CPU 不支持的 AVX2 指令。这源于 Tailwind 4 使用了现代 JavaScript 运行时 Bun，后者优先考虑性能而非向后兼容性。

尽管尝试了各种解决方案，包括 CDN 托管版本和等待补丁发布，作者仍然受困。他浪费了宝贵的时间来调试问题，而不是开发他的应用程序。最终，他不得不购买一台较新的 M2 Mac Studio 来绕过 CPU 限制。

最终，作者意识到他对 Tailwind 的采用是由 FOMO 驱动的，而不是真正的需求。他批评了科技行业不断采用新技术的压力，这种压力是由可能并不完全了解实际后果的影响者所推动的。这种压力可能导致开发人员将时间浪费在不必要的技术采用上，而不是专注于核心开发。作者的结论是，批判性地评估技术选择并避免盲目追随潮流非常重要，最终他决定从应用程序中删除 Tailwind。

---

## 70. 超越呱呱叫：将语言模型和RAG深度集成到DuckDB中

**原文标题**: Beyond Quacking: Deep Integration of Language Models and RAG into DuckDB

**原文链接**: [https://arxiv.org/abs/2504.01157](https://arxiv.org/abs/2504.01157)

本文介绍了FlockMTL，一种旨在将大型语言模型(LLM)能力和检索增强生成(RAG)深度集成到DuckDB中的DBMS扩展。其目标是简化知识密集型分析应用的开发，这些应用需要从结构化表格数据和非结构化文本文档中检索上下文。

作者认为，构建高效的LLM驱动的数据管道目前需要大量精力，因为需要编排异构系统、管理数据移动以及处理底层LLM上下文管理。FlockMTL通过提供模型驱动的标量和聚合函数来解决这些挑战，从而促进通过元组级操作进行链式预测。

FlockMTL的主要特点包括：

*   **基于成本的优化：** 应用批处理和缓存等技术来提高性能。
*   **资源独立性：** 通过新颖的SQL DDL抽象实现，特别是将`PROMPT`和`MODEL`作为与`TABLE`同等的一级模式对象引入。

通过整合这些特性，FlockMTL简化了开发流程，并减轻了与利用LLM和RAG的知识密集型分析应用相关的实施负担。与需要编排各种数据系统的传统方法相比，它提供了一种更集成和优化的方法。

---

## 71. 镜像阶段的思考

**原文标题**: Reflections on the Mirror Stage

**原文链接**: [https://lareviewofbooks.org/blog/essays/reflections-mirror-stage/](https://lareviewofbooks.org/blog/essays/reflections-mirror-stage/)

无法访问文章链接。

---

## 72. 量子物理误入歧途，'T Hooft如是说

**原文标题**: Quantum Physics Is on the Wrong Track Says Gerard 'T Hooft

**原文链接**: [https://www.scientificamerican.com/article/breakthrough-prize-winner-gerard-t-hooft-says-quantum-mechanics-is-nonsense/](https://www.scientificamerican.com/article/breakthrough-prize-winner-gerard-t-hooft-says-quantum-mechanics-is-nonsense/)

本文采访了科学突破奖得主杰拉德·特·胡夫特，他是一位著名的理论物理学家，以其对粒子物理学标准模型和全息原理的贡献而闻名。特·胡夫特讨论了他最近获得的奖项，并反思了物理学的现状和未来。

虽然承认标准模型的成功，但特·胡夫特对粒子物理学缺乏突破性发现表示失望，认为这是由于缺乏新颖的思考。他敦促年轻科学家探索非常规方法，并批评量子力学中过度依赖统计和神秘主义。

特·胡夫特认为，量子力学不是理解粒子相互作用的终极方式，并提倡一种更“务实”的经典方法。他强调局域性的重要性，认为粒子相互作用应由其直接环境决定，拒绝非局域性的观点。他认为，对支配粒子碰撞的规律缺乏更深入的理解，物理学应侧重于定义这些规律，而不是仅仅依赖统计概率。他认为，找到这些新的、更好的问题，才是理论物理学家真正的挑战。

---

## 73. 脚手架关卡编辑器

**原文标题**: Scaffold Level Editor

**原文链接**: [https://blog.littlepolygon.com/posts/scaffold/](https://blog.littlepolygon.com/posts/scaffold/)

Max!，一位独立游戏开发者，正在虚幻引擎中创建一个名为“Scaffold”的自定义关卡编辑器，旨在解决其动作游戏《夜班星系》的生产力、独特性和性能目标。受到90年代游戏（如DOOM和DESCENT）效率的启发，Scaffold的目标是用优化的并行系统来补充虚幻的标准碰撞和导航系统。

其核心思想是从连接的凸体（“立方体”）构建关卡，从而消除了通用引擎所需的运行时凸分解。这种“凸体构建”方法允许预先计算空间划分，从而减少CPU和RAM的需求，并避免了动态系统经常需要的性能调整。

本文解释了凸几何体的基本原理以及它如何用于光线追踪和寻路。在像虚幻这样的通用引擎中，这些算法依赖于像Octrees这样的动态数据结构进行碰撞检测，以及Recast进行导航，这可能会消耗大量资源。

Scaffold受到DESCENT关卡编辑器的启发，能够直接从凸体“立方体”构建关卡，从而创建一个预先划分的空间。这可以加快光线追踪速度（特别是对于像弹幕模式这样的特殊任务），并通过在共享立方体面上放置路点来自动生成地面和空中单位的导航数据。通过在虚幻引擎内部构建该系统，该工具可以利用现有的资源处理和撤消系统，进一步提高开发效率。

---

## 74. 解码九十年代：早期软件开发中的密码学 (2023)

**原文标题**: Decoding the 90s: Cryptography in Early Software Development (2023)

**原文链接**: [https://www.botanica.software/post/decoding-the-90s](https://www.botanica.software/post/decoding-the-90s)

本文详细介绍了对 90 年代中期 QText 文档进行逆向工程以解锁的过程，因为当时密码已丢失。QText 是一款 DOS 时代的希伯来语-英语文字处理器，采用了基本的加密系统。作者面临的挑战是分析 MS-DOS 二进制文件以及那个时代使用的混淆技术。

他们发现锁定的文档有一个特定的头部，其中包含一个与密码直接相关的 16 字节密钥。在未能找到符合条件的已知哈希算法后，他们通过解压可执行文件（使用 PKUNLITE 和 DISLITE v1.15 等工具）并在 DOSBOX 中绕过 Turbo Pascal 内存覆盖来逆向工程密钥派生算法。

密钥派生函数涉及一个置换函数，该函数基于密码字节的总和和一个有效性位图检查来迭代修改密码字节。这个过程通过递归分解来逆转。他们能够通过利用诸如原始密码字节仅限于大写字母和数字等约束来优化搜索。最终，通过反转两阶段密钥派生，作者可以破解密码并解锁 QText 文档。本文重点介绍了 90 年代初的密码学和软件开发实践以及用于解开它们的工具。

---

## 75. Wayland 救不了 Linux 桌面

**原文标题**: Wayland isn't going to save the Linux desktop

**原文链接**: [https://dudemanguy.github.io/blog/posts/2022-06-10-wayland-xorg/wayland-xorg.html](https://dudemanguy.github.io/blog/posts/2022-06-10-wayland-xorg/wayland-xorg.html)

尽管Wayland具有优势并已开发多年，但本文认为它不太可能取代Xorg成为Linux上占主导地位的显示服务器协议。作者（一位前Wayland倡导者和mpv开发者）概述了导致其采用率缓慢的几个问题。

首先，Wayland缺乏一个强大、全面的参考实现。与Xorg快速围绕XFree86标准化不同，Wayland的开发因从头开始构建多个合成器而变得分散。这导致不同实现之间行为不一致，迫使客户端开发者支持Mutter、Plasma、wlroots和Weston。

其次，Wayland的客户端API过于严格，优先考虑“策略”而不是“机制”。与Xorg的灵活方法不同，Wayland限制了客户端可以执行的操作，经常阻止Xorg中容易获得的功能，包括为非全屏窗口指定精确输出等任务。

第三，Wayland缺乏与Xorg的功能对等性，在没有提供足够替代方案的情况下破坏了现有的工作流程。用户依赖的功能（如屏幕录制）最初并不存在，需要像Pipewire这样的变通方案。作者还提到无法禁用垂直同步，这影响了那些优先考虑低延迟的用户。

总而言之，作者认为Wayland的设计局限性、严格的API以及缺乏功能对等性阻碍了它的采用，导致生态系统碎片化，并迫使开发者依赖变通方案和非Wayland解决方案。虽然承认其潜在的好处，但文章得出结论，对于大多数用户来说，Wayland的缺点掩盖了其优势。

---

## 76. 雕塑家：编码时捕捉并修复问题

**原文标题**: Sculptor: Catch and fix issues as you code

**原文链接**: [https://imbue.com/product/sculptor/](https://imbue.com/product/sculptor/)

Sculptor：一款将软件工程最佳实践融入开发者工作流程的全新编码助手环境。它充当编码助手，并行地在沙盒环境中识别并帮助修复代码问题，例如缺失的测试、内存泄漏和风格问题。

主要功能包括：

*   **自动化问题检测：** Sculptor使用自定义提示、shell命令以及与常用框架和代码检查工具的集成来检查代码中的潜在问题。
*   **并行问题解决：** 可以同时启动多个修复，允许开发人员审查建议的更改并通过代理交互来改进它们。
*   **沙盒执行：** 代码在隔离的环境中运行，从而实现安全的实验和错误修复，而不会影响本地开发环境。
*   **代码生成支持：** Sculptor还可以协助编写新代码，自动运行自定义检查以确保质量。
*   **可自定义检查：** 用户可以根据LLM提示或shell命令定义自己的检查，从而根据特定实践定制工具。

Imbue正在寻找测试人员来帮助塑造Sculptor的开发。测试人员将获得早期访问权限、在有限时间内免费使用以及Imbue周边产品。目标是通过将最佳实践集成到LLM驱动的编码工作流程中，使软件工程大众化，从而使其更广泛的受众可以使用。未来的发展方向包括诸如“回溯”功能、自定义检查共享和自动化生产问题解决等功能。

---

## 77. 任何程序都可以成为 GitHub Actions 的 shell。

**原文标题**: Any program can be a GitHub Actions shell

**原文链接**: [https://yossarian.net/til/post/any-program-can-be-a-github-actions-shell/](https://yossarian.net/til/post/any-program-can-be-a-github-actions-shell/)

本文揭示了 GitHub Actions 一个令人惊讶的方面：`shell` 关键字用于指定 `run` 代码块的解释器，它接受**系统中 `$PATH` 环境变量中找到的任何可执行文件**，而不仅仅是像 bash 或 pwsh 这样预定义的 shell 列表。

作者发现 GitHub 并未使用固定的 shell 列表并为每个 shell 注入特定标志，而是执行 `$PATH` 查找。这允许用户指定自定义的可执行文件，甚至像 C 编译器 `tcc` 这样非常规的程序作为 shell。为了使其工作，指定的可执行文件需要接受文件名作为输入，GitHub 通过 `{0}` 占位符提供此文件名，该占位符会被替换为包含展开的 `run` 代码块内容的临时文件。

文章通过使用 `tcc` 运行 C 代码以及操纵 `$PATH` 使用自定义的、伪造的 bash 脚本的例子来演示了这一点。

虽然作者承认文件写入和诸如 `GITHUB_ENV` 之类的环境变量已经在 GitHub Actions 中提供了充分的代码执行机会，但使用任意可执行文件作为 shell 的能力仍然是意想不到的。他们提出担忧，即 GitHub 即使对于“众所周知”的 shell 也进行 `$PATH` 查找可能会引入安全隐患，因为它依赖于用户的 `$PATH` 而不是这些解释器的固定、预定义的位置。它也挑战了 `shell: python` 依赖于工具缓存中预注册工具的假设。

---

## 78. 采访一位使用人工智能准备面试的软件工程师

**原文标题**: Interviewing a software engineer who prepared with AI

**原文链接**: [https://www.kapwing.com/blog/what-its-like-to-interview-a-software-engineer-preparing-with-ai/](https://www.kapwing.com/blog/what-its-like-to-interview-a-software-engineer-preparing-with-ai/)

作者讲述了一次离奇的面试经历，面试对象是一位使用人工智能准备的软件工程师候选人。该候选人最初以相关经验和匹配的领英资料给人留下深刻印象，但当面试官深入探究过去项目的技术细节时，出现了前后矛盾之处。该候选人难以解释特定实施选择背后的原因，最终承认在准备过程中大量依赖人工智能，并夸大了自己在项目中的参与程度。

作者反思了人工智能时代招聘的挑战，并为招聘经理提供了以下关键要点：

*   **提出详细的情景问题：** 探索技术决策背后的“为什么”，以及它们与整体业务环境的关联。
*   **关注人文因素：** 询问技术解决方案对用户及其体验的影响。
*   **坚持视频通话：** 确保面试者与个人资料相符，且未被外包。
*   **背景调查至关重要：** 向以前的同事核实候选人的说法。
*   **保持专业和同理心：** 认识到候选人也在尽力而为，而且你的声誉是双向的。

作者强调，尽管候选人有可能在某种程度上蒙骗了他，但他最终坦白了自己的不诚实，这本身就证明了他的真实意图。作者最后建议求职者保持诚实，因为虚报信息可能会导致日后的问题。这篇文章是一项培训资源，强调需要更深入的提问来揭示人工智能辅助的夸大行为，以及背景调查等传统验证方法的重要性。

---

## 79. 《军团要塞2经济中的套利与均衡（2012）》

**原文标题**: Arbitrage and equilibrium in the Team Fortress 2 economy (2012)

**原文链接**: [https://web.archive.org/web/20130530084230/http://blogs.valvesoftware.com/economics/arbitrage-and-equilibrium-in-the-team-fortress-2-economy/](https://web.archive.org/web/20130530084230/http://blogs.valvesoftware.com/economics/arbitrage-and-equilibrium-in-the-team-fortress-2-economy/)

本文发表于2012年，探讨了《军团要塞2》(TF2)经济中的套利和均衡，这是一个由Steam促成的复杂的易货系统。作者Yanis强调了套利的内在挑战，即随着更多人追求套利，套利机会会减少，最终导致均衡。

与由于价格数据有限而难以衡量套利潜力的传统经济不同，Valve拥有来自Steam的实时数据，能够为TF2物品交易创建一个“套利潜力指数”。该指数的峰值与重大发布和销售相关，这些时期价格效率低下，创造了套利机会。

本文深入探讨了TF2经济的复杂性，这是一个易货系统，交易需要“需求的双重巧合”。尽管它很复杂且交易量很高，但没有单一物品成为主导货币。

均衡是经济学的基石，被定义为一种没有改变动机的状态，无论是静态的（没有运动）还是动态的（可预测的运动）。作者解释了如何在简化的包含四种物品的TF2经济中计算均衡价格，展示了当价格偏离均衡时如何产生套利机会。交易者利用这些差异，最终推动经济走向均衡。

然而，作者指出，TF2经济很少处于均衡状态，从而产生了持续的套利机会。为了衡量套利潜力，开发了一种方法，即使在非均衡状态下，也可以为每个物品分配一个单一的“名义钥匙”价格。这涉及根据特定物品交易的频率对价格进行加权，以估计相对价值。

---

## 80. Show HN: 用Go实现的极简MCP服务器，展示项目架构

**原文标题**: Show HN: Minimal MCP server in Go showcasing project architecture

**原文链接**: [https://github.com/TuanKiri/weather-mcp-server](https://github.com/TuanKiri/weather-mcp-server)

此“Show HN”帖子介绍了一个极简的基于 Go 的模型上下文协议 (MCP) 服务器，旨在为 Claude 等 AI 助手提供实时天气数据。该服务器名为“weather-mcp-server”，利用 Weather API 并提供一个名为“current_weather”的工具来获取指定城市的天气信息。

该帖子详细介绍了如何通过配置代码段将服务器与 Claude Desktop 集成，需要可执行文件的路径和 Weather API 密钥。文中提供了使用 Go 从源代码构建服务器的说明。

帖子概述了项目结构，重点介绍了关键目录，例如：`cmd`（包含服务器的入口点）、`internal`（包含服务器逻辑），以及 `internal` 中的子目录，例如 `handlers`、`services`、`core` 和 `mock`，展示了一个组织良好的架构。`tools` 目录用于与 MCP 相关的实用程序，而 `view` 包含模板。

帖子最后鼓励通过 issues 和 pull requests 贡献，并强调使用贡献指南。该服务器在 MIT 许可证下授权。

---

## 81. 直线竞速赛车手正抛弃机械增压器，转而使用水肺式气瓶和压缩空气。

**原文标题**: Drag racers are ditching superchargers for scuba-style tanks and compressed air

**原文链接**: [https://www.thedrive.com/news/drag-racers-are-ditching-superchargers-for-scuba-style-tanks-and-compressed-air](https://www.thedrive.com/news/drag-racers-are-ditching-superchargers-for-scuba-style-tanks-and-compressed-air)

“The Drive”文章探讨直线竞速赛新趋势：压缩空气增压（CAS）。该系统用储存在碳纤维罐中的压缩空气取代传统机械增压器和涡轮增压器，在功率和效率方面具有潜在优势。

CAS的工作原理是将极冷的、高密度空气强制送入发动机，理论上超越了传统方法，因为它不需要马力或排气来运行。该系统利用调节器和阀门网络来控制气流，从而可以像传统机械增压器一样进行增压调节。

进入发动机的约零下20华氏度的冷空气是一个关键优势，它能带来更稠密的燃烧空气，并可能由于较低的压力而减轻发动机部件的压力。它也可能对燃料辛烷值不太敏感。

蒂娜·皮尔斯、戴夫·皮尔斯和瑞恩·米切尔等赛车手正在试验CAS，并取得了与之前设置相当或更好的性能。马克·格里芬的卡玛洛被展示为CAS应用的典型例子。

虽然CAS仍处于早期应用阶段，但它为直线竞速赛中提高发动机功率提供了一种有前景的替代方案，具有令人印象深刻的性能提升潜力。然而，重新填充专用罐需要特定的设备，增加了一项后勤考虑。文章总结说，CAS有可能对直线竞速赛产生重大影响，并期待这项技术的进一步发展。

---

## 82. Globstar: 开源静态分析工具包

**原文标题**: Globstar: Open-source static analysis toolkit

**原文链接**: [https://github.com/DeepSourceCorp/globstar](https://github.com/DeepSourceCorp/globstar)

Globstar：开源静态分析工具包，旨在帮助开发者和安全工程师创建并运行自定义代码分析检查器。它利用tree-sitter进行快速高效的AST分析，允许用户使用简单的YAML接口或更强大的Go接口编写检查器，后者提供完整的AST访问、导入解析和作用域解析。

其关键特性包括速度和效率（使用Go编写并以单个二进制文件分发）、原生tree-sitter集成、CI/CD友好性以及真正的开源MIT许可证。用户在他们的仓库中创建一个`.globstar`目录来存储自定义检查器，这些检查器在YAML文件中使用tree-sitter S-表达式查询定义。一个简单的命令`globstar check`运行所有检查器，包括内置的。

本文提供了使用`curl`命令的安装说明，并解释了如何编写一个基本的检查器（以检测Python中的`eval()`用法为例），以及如何将Globstar集成到GitHub Actions等CI流水线中。

Globstar旨在简化自定义检查器的创建，避免对专用DSL或大量工具的需求。它强调易用性、速度和开源方法，使团队能够实施学习到的模式并维护代码质量。计划未来与DeepSource集成，但这是可选的，突出了Globstar作为强大工具的独立性。完整文档可在官方网站上找到。

---

## 83. 依赖类型 Haskell 编程的苦与乐 [pdf] (2013)

**原文标题**: Hasochism: The pleasure and pain of dependently typed Haskell programming [pdf] (2013)

**原文链接**: [https://personal.cis.strath.ac.uk/conor.mcbride/pub/hasochism.pdf](https://personal.cis.strath.ac.uk/conor.mcbride/pub/hasochism.pdf)

由于提供的PDF内容严重损坏（包含大量无法读取的字符和编码错误），无法生成文章《Hasochism:依赖类型 Haskell 编程的快乐与痛苦》的有意义的摘要。该PDF似乎已彻底损坏。

---

## 84. 用淘汰赛评估大型语言模型的社交技能

**原文标题**: Benchmarking LLM social skills with an elimination game

**原文链接**: [https://github.com/lechmazur/elimination_game](https://github.com/lechmazur/elimination_game)

本文介绍了“淘汰游戏”，这是一个新颖的基准，旨在评估大型语言模型在多智能体环境中的社会推理、战略思维和欺骗技巧。在这个游戏中，八个大型语言模型参与一场锦标赛，涉及公开和私下对话、联盟形成、投票和说服陪审团。

游戏通过几轮公开声明、私下聊天和匿名投票来淘汰玩家。平局增加了复杂性，最后两名参赛者必须说服已被淘汰的玩家组成的陪审团投票支持他们获胜。

该基准提供了各种指标来分析大型语言模型的行为，包括：TrueSkill排行榜（总体排名）、排名分布（名次频率）、好友背叛率（从背叛者和被背叛者的角度来看）、第一名次数、最早淘汰次数、决赛两人获胜率以及模型冗长度。这些指标揭示了联盟形成、背叛、修辞技巧和沟通风格的倾向。

本文展示了一个参与的大型语言模型的排行榜，按其TrueSkill分数排名，展示了GPT-4o、Claude 3.7 Sonnet等模型的性能。它还包括模型在游戏过程中产生的有趣且富有洞察力的涌现文本示例，突出了它们的战略思维、欺骗策略和复杂的社交手段。“仅公开版本”提供了一种评估变体。

---

## 85. 在 1980 年代，我们也曾从电视上下载软件。

**原文标题**: In the 1980s we also downloaded software from TV

**原文链接**: [https://newslttrs.com/in-the-1980s-we-also-downloaded-software-from-tv/](https://newslttrs.com/in-the-1980s-we-also-downloaded-software-from-tv/)

本文探讨了上世纪80年代英国8位计算机普及推动下，从电视广播下载软件的方式。虽然无线电广播使用音频信号，但电视开发了两种独特的技术。

第一种是图文电视，它利用电视帧之间的空白信号传输数据，然后由配备特定硬件的 BBC Micro 解码。用户必须等待所需软件在广播中循环播放。另一种方法是使用连接到电视屏幕的简单光电二极管电路，检测闪烁的黑白方块，将光转换转化为计算机代码，尽管速度非常慢。

John 和 Richard Billingsley 开发的 Visicode 通过使用八个闪烁的条纹并利用电视屏幕上每行扫描的电子束，显著提高了数据传输速率。这允许每半个电视帧传输一个完整字节的数据。

作者联系了现任教授 John Billingsley，他指出，由于现代平板电视的出现，Visicode 就像图文电视软件下载一样，已经过时。然而，这两种方法都展示了巧妙的工程设计，它们重新利用了现有的模拟电视功能，从而在有限的资源下实现了新的功能。图文电视数据有时可以从旧视频录像中恢复，这为 Visicode 的潜在恢复打开了大门。

---

## 86. 了解你的工程师薪资来源

**原文标题**: Knowing where your engineer salary comes from

**原文链接**: [https://www.seangoedecke.com/where-the-money-comes-from/](https://www.seangoedecke.com/where-the-money-comes-from/)

本文认为，软件工程师常常对科技公司的运作方式抱有天真的理解，就像特朗普选民对联邦解雇感到惊讶一样。核心观点是：科技公司主要由利润驱动，工程工作的价值取决于其对收入增长的贡献。

作者批评那些专注于非盈利活动（如技术债务、可访问性或开源工作）的工程师，然后在他们未获得认可或被解雇时抱怨。他们实际上是在通过忽视公司的主要目标来“投票解雇自己”。

为了避免这种情况，工程师应该：

1. **理解公司的商业模式**：了解公司如何赚钱（例如，阅读财务报告、内部分析）。
2. **将自己的工作与利润联系起来**：确定他们的任务（即使是看似无利可图的任务）如何支持收入的产生。例如，可访问性可以扩大客户群或满足法规要求。
3. **为盈利的公司工作**：大型、成功的科技公司有能力投资于边际功能，这些功能可以略微增加其庞大的客户群。

作者告诫不要天真地认为“好公司”重视与利润无关的“好功能”。 工程师应该意识到他们的工作与底线之间的联系，以确保工作保障和职业满意度。 虽然公司可能有其他目标，但利润是确保稳定的根本驱动力。

---

## 87. 工作简化与政府效率和管理的历史

**原文标题**: Work Simplification and the History of Government Efficiency and Management

**原文链接**: [https://www.governance.fyi/p/historical-government-efficiency](https://www.governance.fyi/p/historical-government-efficiency)

本文总结了与凯文·霍维克霍斯特关于历史上的政府效率和管理实践的对话，特别关注20世纪40年代至60年代的“工作简化”计划。二战期间，预算局（现OMB）为管理人员开发了一项培训计划，旨在改进流程、减少繁文缛节并提高效率，以应对战时人力短缺的问题。这种“工作简化”借鉴了工厂培训方法。预算局顾问W. Edwards Deming提倡对所有交易进行统计控制，而不是试图监督每一项交易。这些方法是全面质量管理和精益方法的前身，出乎意料地具有现代性。

然而，霍维克霍斯特认为，20世纪60年代，随着政府采纳了来自企业的繁琐的“长期规划”方法，管理实践有所下降，尤其受到罗伯特·麦克纳马拉国防计划的影响。这种自上而下的方法，受到通用汽车和杜邦等公司“现代”实践的启发，反而使政府的效率低于以往。

霍维克霍斯特研究这个主题的动机源于对国家能力的辩论，旨在了解政府过去如何更有效率，尤其是在诸如职位描述、预算编制和管理培训等领域。他提到的一个有趣的案例研究包括美国国税局早期利用穿孔卡片计算设备的数字化工作。

---

## 88. 细胞正在交换线粒体。这对我们的健康意味着什么？

**原文标题**: Cells are swapping their mitochondria. What does this mean for our health?

**原文链接**: [https://www.nature.com/articles/d41586-025-01064-5](https://www.nature.com/articles/d41586-025-01064-5)

本文探讨了人们对线粒体作为可移动的细胞器，可以在细胞之间转移的新兴理解，挑战了它们作为静态、完全细胞内能量工厂的传统角色。这种“线粒体转移”已在多种生物和细胞类型中观察到，表明这是一种基本的生物过程。

研究人员正在调查这种转移的原因和影响。一些研究表明，线粒体被捐赠给处于困境的邻近细胞，可能有助于组织修复，增强免疫系统，或预防中风后的细胞死亡等。癌细胞也可能利用这种机制来发挥优势。

尽管在体外和动物中观察到转移，但由于技术限制，直接在人体中观察仍然难以实现。然而，研究人员正在探索线粒体转移在癌症和中风等疾病中的治疗应用。

本文强调，线粒体除了能量产生外，还参与多种细胞过程，包括细胞通讯和免疫反应。此外，它们比以前认为的更加多样化和动态。

虽然转移机制（隧道纳米管、囊泡或自由漂浮）正变得越来越清晰，但转移线粒体的信号通路和最终命运仍然很大程度上未知。需要进一步研究以了解这些细胞交换在各种疾病和正常生理中的具体作用。

---

## 89. macOS Sequoia 中 Rsync 被 openrsync 取代

**原文标题**: Rsync replaced with openrsync on macOS Sequoia

**原文链接**: [https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/](https://derflounder.wordpress.com/2025/04/06/rsync-replaced-with-openrsync-on-macos-sequoia/)

macOS Sequoia 因授权问题，用 openrsync 替换了老旧的 rsync 2.6.9。 苹果之前发布的是 2006 年的 rsync 2.6.9 版本，因为它采用 GPLv2 许可。 由于认为与 GPLv3 许可不兼容，他们避免更新到 rsync 3.x (GPLv3)。

Openrsync 采用 ISC 许可（一种宽松的 BSD 风格许可），消除了这些许可问题，允许苹果未来更自由地更新该工具。

这一改变很重要，因为：
* 苹果现在可以提供 openrsync 的更新版本。
* Openrsync 虽然与 rsync 兼容，但仅支持 rsync 命令行参数的一个子集。

这可能会影响 Mac 管理员，因为由于 openrsync 中命令行参数支持的减少，现有的 rsync 脚本和功能可能无法在 macOS Sequoia 上运行。 openrsync 工具被符号链接到 `/usr/bin/rsync`，因此它作为传统的 rsync 命令被调用。 运行 `/usr/bin/rsync --version` 将确认此更改。 输出将显示 "openrsync" 和 "rsync version 2.6.9 compatible" 消息。

---

## 90. 最小的心脏起搏器仅有米粒大小

**原文标题**: Smallest Pacemaker Is the Size of a Rice Grain

**原文链接**: [https://www.sciencealert.com/breakthrough-worlds-smallest-pacemaker-is-the-size-of-a-rice-grain](https://www.sciencealert.com/breakthrough-worlds-smallest-pacemaker-is-the-size-of-a-rice-grain)

一个美国领导的科学家团队研发出世界最小的起搏器，这是一种无线、临时的设备，比一粒米还小，可以注射并用光控制。它被设计成在不再需要时于体内溶解，从而避免了移除传统临时起搏器所带来的并发症，后者需要手术并可能造成损伤。

该设备与胸贴配合使用，检测不规则的心跳，并利用光来指示起搏器进行适当的刺激。它由一个原电池供电，利用体液来产生电脉冲。

在各种动物和人体心脏组织中的测试已经成功。研究人员估计，人体试验可能在两到三年内开始。这项创新被誉为心脏病学领域一项潜在的“变革性突破”，尤其对于患有先天性心脏缺陷的婴儿和正在从心脏手术中恢复的成年人。专家认为，这项底层技术可以扩展到心脏病学以外的领域，如神经再生、伤口愈合和智能植入物。

---

## 91. 使用 Web Audio API 生成可变占空比方波

**原文标题**: Variable duty cycle square waves with the Web Audio API

**原文链接**: [https://www.danblack.co/blog/variable-duty-cycle-square-wave](https://www.danblack.co/blog/variable-duty-cycle-square-wave)

本文探讨了如何使用 Web Audio API 创建可变占空比的方波，这是模拟 Gameboy 等设备发出的芯片音乐的关键特性。 Web Audio API 的标准“方波”振荡器仅提供 50% 的占空比，这限制了声音的可能性。

作者详细介绍了两种克服此限制的方法。第一种方法使用**傅里叶级数**，将所需的波形表示为正弦波和余弦波（谐波）的和。 这涉及计算傅里叶系数并使用 `AudioContext.createPeriodicWave()` 为振荡器生成自定义波形。 虽然数学上准确，但这种方法可能会占用大量 CPU 资源，尤其是在谐波较多的情况下。

第二种方法采用 **WaveShaperNode**。 这涉及使用自定义传递函数来扭曲锯齿波。 创建一个阶跃函数，根据所需的占空比将输入值映射到 1 或 -1，从而有效地将锯齿波整形为方波。 作者更喜欢这种方法，因为它简单，而且其固有的混叠和“嗡嗡声”更接近 Gameboy 的声音。 虽然傅里叶级数在数学上是完美的，但 WaveShaper 节点更容易产生 Gameboy 所需的不完美音迹。

文章强调了每种方法的优缺点：傅里叶级数提供精度，但计算成本可能很高，而 WaveShaper 更简单，但容易产生混叠。 最终，作者选择 WaveShaper 方法，因为它在他们的 Gameboy 音乐跟踪器项目中实现了简单性、真实性和效率的平衡。

---

## 92. Show HN: Lux – Lua 的豪华包管理器

**原文标题**: Show HN: Lux – A luxurious package manager for Lua

**原文链接**: [https://mrcjkb.dev/posts/2025-04-07-lux-announcement.html](https://mrcjkb.dev/posts/2025-04-07-lux-announcement.html)

Show HN：Lux——Lua的现代化包管理器

---

## 93. 从虚幻引擎中移除多人游戏功能可以节省内存。

**原文标题**: Deleting multiplayer from the Unreal engine can save memory

**原文链接**: [https://larstofus.com/2025/04/05/how-deleting-multiplayer-from-the-engine-can-save-memory/](https://larstofus.com/2025/04/05/how-deleting-multiplayer-from-the-engine-can-save-memory/)

本文探讨了在开发单人游戏时，移除虚幻引擎中的多人游戏功能所能实现的潜在内存节省。作者具有虚幻引擎多人游戏功能的经验，承认其优势，但也研究了它们对单人项目造成的额外开销。

虽然未使用的代码通常不会影响性能，但作者发现与网络相关的（Actor、组件和移动的复制）数据结构，即使在单人游戏中也会消耗大量内存。通过分析 AActor 类的内存布局，作者估计通过移除多人游戏相关的变量，每个 Actor 可以潜在减少 328 字节，每个 SceneComponent 可以潜在减少 32 字节。

作者详细介绍了干净地实现此优化的挑战。由于虚幻引擎头文件工具 (UHT) 的限制，尝试使用预处理器宏来有条件地编译多人游戏代码被证明是有问题的。相反，作者选择注释掉 58 个引擎文件中的相关变量和代码。

作者估计，对于一个包含 25,000 个 Actor 的关卡，这种优化可以节省大约 10MB 的内存。虽然对于大多数项目来说，这可能并不显著，但对于拥有异常大量 Actor (>100,000) 且其他优化方法不足的游戏来说，这可能是有益的。作者总结说，虽然值得考虑，但应该首先寻求许多其他的优化机会。

---

## 94. 异步 Rust 的确定性模拟测试

**原文标题**: Deterministic simulation testing for async Rust

**原文链接**: [https://s2.dev/blog/dst](https://s2.dev/blog/dst)

本文探讨了由于异步Rust代码固有的非确定性特性而导致的测试难题。传统测试方法在处理并发和异步操作时，往往难以提供一致且可靠的结果。

提出的核心概念是**确定性模拟测试**作为解决方案。这种方法旨在为测试异步代码创建一个可控且可预测的环境。它不依赖于异步任务的实时执行，而是通过模拟环境来操纵这些任务的计时和调度。

这种方法的关键要素可能包括：

*   **抽象掉实时时钟和任务调度器：** 提供这些组件的虚拟化、可控版本。
*   **控制任务的交错执行：** 允许测试来决定异步任务的执行顺序，从而暴露潜在的竞争条件和并发错误。
*   **确定性执行：** 确保给定的测试场景始终产生相同的结果，而与外部因素无关。
*   **简化调试：** 通过提供可预测的执行环境来促进更轻松的调试。

文章认为，通过使用确定性模拟，开发人员可以为其异步Rust应用程序编写更健壮、更可靠的测试，从而能够捕获那些在非确定性环境中难以或不可能重现的错误。它可能侧重于这种方法在提高代码质量和减少调试时间方面的益处。

---

## 95. 谁不喜欢“公正”的新闻呢？没有权力的人。

**原文标题**: Who isn't a big fan of "impartial" news? People who don't have power

**原文链接**: [https://www.niemanlab.org/2025/04/which-types-of-people-arent-big-fans-of-impartial-news-people-who-dont-have-power/](https://www.niemanlab.org/2025/04/which-types-of-people-arent-big-fans-of-impartial-news-people-who-dont-have-power/)

无法访问文章链接。

---

## 96. 钩针编织的数学

**原文标题**: The Mathematics of Crochet

**原文链接**: [https://hellohartblog.wordpress.com/2015/05/25/the-mathematics-of-crochet/](https://hellohartblog.wordpress.com/2015/05/25/the-mathematics-of-crochet/)

数学与钩编的惊人交汇

本文探讨了数学与钩编之间令人惊讶的交汇。它强调了钩编图案所具有的潜在数学结构，将针法的存在与缺失比作Base2数学的二进制代码。随后，本文深入研究了通过钩编说明数学概念的具体例子。

双曲钩编被介绍为一种创建双曲空间模型的技术，这种几何结构曾被认为不可能实现。文章提到了黛娜·泰米娜博士在钩编双曲表面方面的开创性工作，以及莉莲·博洛尼的艺术探索，她利用钩编创作出优美的双曲图形雕塑。文章还指出，双曲增长与珊瑚礁等自然形态之间存在联系，并引用了“具象研究所”的“珊瑚礁”项目。

此外，本文还介绍了“混沌钩编”，以Hinke Osinga博士和Bernd Krauskopf教授对洛伦兹流形的钩编表示为例。他们将洛伦兹方程的计算机生成指令转化为有形的钩编对象。最后，文章提到了“分形钩编”，将分形的自相似、不规则形状与这种艺术形式联系起来。文章最后强调了钩编固有的智慧和美丽，并认为它是一种创造性的表达方式，与数学原理出人意料地交织在一起。

---

## 97. PiDP-1，老机器的重生

**原文标题**: PiDP-1, or the rebirth of an old machine

**原文链接**: [https://hackaday.io/project/202541-replica-of-the-pdp-1-pidp-1/log/239666-finished-the-first-test-batch-of-5-machines](https://hackaday.io/project/202541-replica-of-the-pdp-1-pidp-1/log/239666-finished-the-first-test-batch-of-5-machines)

这个Hackaday.io项目日志详细记录了PDP-1计算机复制品PiDP-1的进展。作者Oscarv宣布完成了首批五台机器的测试，有效地将PDP-1的总产量提高了10%。

该项目专注于复制1959年原版PDP-1标志性的闪烁灯光和矢量点图形。Oscarv提到，他们将用两周时间“润色”这些机器，并努力使其接近完成。项目团队在过去两周全身心投入，不断产生新的想法和功能。

其他用户表达了对该项目的热情。评论突出了该项目的酷炫和令人赞叹之处。一位评论者期待看到项目的最终成果。

---

## 98. 出土距今2500年古匕首，饰星月几何图案

**原文标题**: Ancient Dagger Up to 2.5k Years Old W Stars/Moons/Geometric Patterns Unearthed

**原文链接**: [https://www.smithsonianmag.com/smart-news/metal-detectorists-unearth-ancient-dagger-decorated-with-tiny-stars-crescent-moons-and-geometric-patterns-180986369/](https://www.smithsonianmag.com/smart-news/metal-detectorists-unearth-ancient-dagger-decorated-with-tiny-stars-crescent-moons-and-geometric-patterns-180986369/)

金属探测者Jacek Ukowski和Katarzyna Herdzik在最近一场风暴过后，于波兰北部海滩发现了一把可能有2500年历史的装饰匕首。这把匕首可能与哈尔施塔特文化（公元前8至5世纪）有关，上面装饰着星星、新月和几何图案。

这一发现已报告给卡缅土地历史博物馆，考古学家Grzegorz Kurka对该文物进行了检查。专家认为，这把匕首可能是在南欧制造并进口到波罗的海沿岸，代表了极高的冶金工艺水平。精美的设计，特别是可能象征星座的星星，暗示着它可能具有与太阳崇拜相关的仪式意义，或被富裕的战士使用。

这把近十英寸长的匕首有一个纤细的、装饰有环状物的把手，刀刃上印有天体和几何图案。 Ukowski认为这是他最珍贵的发现。将进行冶金分析以确定匕首的成分和制造技术，研究人员还将研究磨损模式以了解其用途。

这把匕首被认为是波美拉尼亚历史上的宝贵遗产，研究完成后将在波兰博物馆展出。 Kurka将其描述为“一件真正的艺术品”，与他在波兰领土上发现的任何东西都不一样。

---

## 99. 创业公司不一定要成为独角兽。

**原文标题**: A startup doesn't need to be a unicorn

**原文链接**: [https://mattgiustwilliamson.substack.com/p/your-startup-doesnt-need-to-be-a](https://mattgiustwilliamson.substack.com/p/your-startup-doesnt-need-to-be-a)

无法访问文章链接。

---

## 100. Git 二十年

**原文标题**: 20 years of Git

**原文链接**: [https://blog.gitbutler.com/20-years-of-git/](https://blog.gitbutler.com/20-years-of-git/)

本文庆祝 Git 诞生 20 周年，详细介绍了它的起源和演变过程，从一个“愚蠢的内容追踪器”发展成为主流的版本控制系统。文章强调，由于现有版本控制系统的局限性，Git 源于 Linux 内核开发社区的挫败感，旨在改进“补丁和 tar 包”工作流程。 Linus Torvalds 创建 Git 时，专注于高效的快照和差异跟踪。

作者 Scott Chacon 分享了他与 Git 的个人历程，包括在一家初创公司中使用它进行内容分发以及为其早期开发做出贡献。 他解释了 Git 的架构，基于文件树的链表和内容寻址的 blob 存储，自第一次提交以来，其基本结构保持不变。

文章追溯了 Git 命令的演变，最初是低级工具，通过 shell 脚本和社区贡献逐渐转变为用户友好的“瓷器”命令。文章提供了第一个 "git log" 和 "git rebase" 等示例，展示了它们的简陋起源。文章还提到了 GitHub 的 "Octocat" 标志的起源，将其与 Git 开发中的 "octopus" 合并（具有多个父节点的合并）概念联系起来。最终，文章强调了 Git 从一个简单的数据库工具集到现代软件开发基石的意外旅程。

---

