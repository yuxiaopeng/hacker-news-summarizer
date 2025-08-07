# Hacker News 热门文章摘要 (2025-08-07)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. GPT-5

**原文标题**: GPT-5

**原文链接**: [http://openai.com/gpt-5](http://openai.com/gpt-5)

无法访问文章链接。

---

## 2. 为我的博客构建Bluesky评论功能

**原文标题**: Building Bluesky Comments for My Blog

**原文链接**: [https://natalie.sh/posts/bluesky-comments/](https://natalie.sh/posts/bluesky-comments/)

本博文概述了将Bluesky评论集成到个人博客的基本设置。其核心目的是通过提供评论、提问和表达顾虑的空间来鼓励受众参与。作者没有构建原生评论系统，而是利用现有的Bluesky社交媒体平台。

该文章展示了一条占位符消息，表明评论正在加载中。它还包含一条回退消息，提示浏览器禁用JavaScript的用户，查看评论需要启用JavaScript。这表明该实现依赖JavaScript来动态获取和显示Bluesky评论。

虽然这篇文章缺乏关于技术实现的具体细节（例如，API的使用、特定的库或代码片段），但它确立了利用Bluesky作为评论系统的意图，并暗示了用户体验——加载状态和JavaScript依赖。简洁的篇幅表明这是一篇介绍性文章，或是更详细教程的一部分。

---

## 3. 无限像素

**原文标题**: Infinite Pixels

**原文链接**: [https://meyerweb.com/eric/thoughts/2025/08/07/infinite-pixels/](https://meyerweb.com/eric/thoughts/2025/08/07/infinite-pixels/)

此文探讨了不同网页浏览器如何处理通过CSS使用`calc(infinity * 1px)`赋值的“无限”像素值。作者在macOS上的Safari、Chrome和Firefox Nightly中测试了各种CSS属性（width、height、font-size和line-height），观察到不一致且通常很奇怪的行为。

Safari和Chrome始终将width、height和line-height的“无限”值限制为相似的大数字，大约为2<sup>25</sup>-1。对于font-size，它们分别施加了100,000px和10,000px的硬性限制，似乎基于随意选择的十进制数字。

Firefox Nightly表现出最不可预测的结果。对于height，除非设置了明确的`line-height`，否则它默认为一行文本的高度。 Width被赋予一个很大的计算值（大约1790万像素），但渲染时大约为该尺寸的一半。字体大小计算会产生一个32位单精度浮点数，但实际渲染的字体大小约为2,400像素，通常与`line-height`产生奇怪的交互。Line-height在Firefox中的行为与width相似，计算值很大，但渲染时减半。

作者对这些不一致之处感到困惑，并寻求对观察到的浏览器怪癖的解释，特别是Firefox中的奇怪行为以及Chrome和Safari中的任意限制。他们邀请对浏览器引擎工作原理有深入了解的读者分享他们的知识。

---

## 4. 如果用户不是购买者，如何销售？

**原文标题**: How to Sell if Your User is not the Buyer

**原文链接**: [https://writings.founderlabs.io/p/how-to-sell-if-your-user-is-not-the](https://writings.founderlabs.io/p/how-to-sell-if-your-user-is-not-the)

当用户非购买者时，如何销售产品：以开发者为用户，CTO/工程总监为购买者为例。 关键在于理解 *谁真正掌握决策权*，而不仅仅是谁掌握预算。

作者概述了两种情况：

*   **小型组织：** 由于需要速度和迭代，开发者通常拥有重要的影响力。 他们可以拥护那些提高效率的工具，有效地将产品“特洛伊木马”式地引入公司。
*   **大型组织：** 领导层通常拥有更多控制权，尤其是在安全是主要考虑因素的情况下。 在这种情况下，需要更长的销售周期来展示价值并满足安全要求。

作者强调，识别 *谁最重视* 产品，并且 *这种重视能够转化为行动*，至关重要。 如果开发者比预算持有者更重视产品，那么目标是 *赋能开发者在内部拥护该产品*。

这包括：

*   为开发者提供引人注目的数据和工具，以说服领导层产品的价值。
*   将产品的优势转化为与领导层产生共鸣的术语（例如，节省时间，提高效率，实现公司目标）。
*   与开发者进行客户访谈，以了解他们与领导层的内部对话，并找出购买过程中的任何摩擦点。

最终，作者认为，在这种情况下，开发者实际上变成了事实上的销售人员，而赋能他们取得成功至关重要。 目标是通过强调开发者、公司和领导层自身的积极成果，使领导层做出“同意”的决定变得显而易见。

---

## 5. GPT-5系统卡

**原文标题**: GPT-5 System Card

**原文链接**: [https://openai.com/index/gpt-5-system-card](https://openai.com/index/gpt-5-system-card)

无法访问文章链接。

---

## 6. 锂逆转小鼠阿尔茨海默症

**原文标题**: Lithium Reverses Alzheimer's in Mice

**原文链接**: [https://hms.harvard.edu/news/could-lithium-explain-treat-alzheimers-disease](https://hms.harvard.edu/news/could-lithium-explain-treat-alzheimers-disease)

本文报告了一项研究，该研究表明大脑中锂缺乏可能是阿尔茨海默病早期的一个关键驱动因素，并且一种新型锂化合物可以逆转小鼠的疾病。哈佛医学院的研究人员发现，锂天然存在于大脑中，对正常大脑功能至关重要。他们发现，阿尔茨海默病患者的大脑中锂含量显著降低，这种减少与锂结合淀粉样蛋白斑块有关，从而损害其功能。

在小鼠模型中，锂缺乏加速了阿尔茨海默病特征的发展，包括淀粉样蛋白斑块、神经原纤维缠结、突触丧失和认知能力下降。重要的是，研究人员发现了一种新的锂化合物，乳清酸锂，它可以避免被淀粉样蛋白斑块捕获。用该化合物治疗小鼠可以逆转阿尔茨海默病的病理，防止脑细胞损伤，并恢复记忆，即使在非常低的无毒剂量下也是如此。

这些发现表明，测量锂水平可能成为阿尔茨海默病早期筛查的工具，乳清酸锂或类似化合物可能用于治疗或预防。虽然还需要在人体中进行临床试验，但研究人员对基于锂的疗法解决阿尔茨海默病的根本原因并可能逆转认知能力下降的潜力持谨慎乐观态度。该研究强调了锂作为大脑健康的关键营养素的重要性，并为阿尔茨海默病的发展和治疗提供了新的视角。

---

## 7. Foundry (YC F24) 招聘资深产品工程师

**原文标题**: Foundry (YC F24) Is Hiring Staff Level Product Engineers

**原文链接**: [https://www.ycombinator.com/companies/foundry/jobs/jwdYx6v-founding-product-engineer](https://www.ycombinator.com/companies/foundry/jobs/jwdYx6v-founding-product-engineer)

Foundry招募创始产品工程师（Staff级别），构建AI代理自动化数字工作的基础设施。他们正通过创建高保真模拟环境来训练、测试和部署AI代理，以解决复杂浏览器工作流程中AI代理不可靠的问题。

该职位涉及架构和实现模拟核心引擎、设计评估和基准测试系统、参与全栈平台开发（Python、Rust、Go、React/Next.js、TypeScript）、负责端到端生产生命周期，以及建立工程最佳实践。

理想人选需具备6-10年以上在顶级公司构建复杂平台的经验、深厚的系统知识（分布式系统、浏览器内部原理）、精通构建的心态、顶尖的TypeScript和Python编码技能，以及熟悉Kubernetes、Docker和云平台。开源贡献或竞技编程荣誉加分。

Foundry提供有意义的所有权、有竞争力的薪酬，以及与来自Scale AI和Meta等公司的强大团队合作的机会。他们的平台专注于确定性Web模拟、实时Web评估、自动标注和标记，以及RL驱动的代理优化，以构建可靠的Web代理。

---

## 8. 直播：GPT-5

**原文标题**: Live: GPT-5

**原文链接**: [https://www.youtube.com/watch?v=0Uu_VJeVVfo](https://www.youtube.com/watch?v=0Uu_VJeVVfo)

标题“直播：GPT-5”强烈暗示了关于OpenAI的GPT语言模型（假定的下一个版本）GPT-5的发布公告、演示，或现场展示。

然而，内容仅仅是通用的YouTube页脚。这表明信息来自YouTube，并包含指向重要政策和管理信息的链接，例如：

*   **版权：** 链接到关于YouTube版权政策的信息。
*   **联系方式：** 链接到联系YouTube的各种方式。
*   **创作者：** 为YouTube内容创作者量身定制的信息。
*   **广告：** 关于在YouTube上投放广告的信息。
*   **开发者：** 为在YouTube平台上构建内容的开发者提供的资源。
*   **条款：** YouTube的服务条款。
*   **隐私：** YouTube的隐私政策。
*   **安全：** YouTube的安全准则。
*   **YouTube运作方式：** 对YouTube平台和流程的解释。
*   **新功能：** 关于测试新功能的信息。
*   **NFL周日联赛：** 提及NFL周日联赛，暗示它在YouTube上可用。
*   **版权日期：** Google LLC的版权声明。

因此，虽然标题暗示了GPT-5的发布公告，但内容却与之无关，似乎是YouTube网站上的样板信息。没有提供关于GPT-5的实际信息。信息不一致。

---

## 9. 放弃 GitHub (2024)

**原文标题**: Ditching GitHub (2024)

**原文链接**: [https://tomscii.sig7.se/2024/01/Ditching-GitHub](https://tomscii.sig7.se/2024/01/Ditching-GitHub)

无法访问文章链接。

---

## 10. 笔记本电脑支持和可用性（LSU）： FreeBSD 基金会 2025 年 7 月报告

**原文标题**: Laptop Support and Usability (LSU): July 2025 Report from the FreeBSD Foundation

**原文链接**: [https://github.com/FreeBSDFoundation/proj-laptop/blob/main/monthly-updates/2025-07.md](https://github.com/FreeBSDFoundation/proj-laptop/blob/main/monthly-updates/2025-07.md)

本报告，题为“笔记本电脑支持与可用性 (LSU)：FreeBSD 基金会 2025 年 7 月报告”，来源于 FreeBSD 基金会在代码托管平台（很可能是 GitHub 或 GitLab）上的公开项目仓库“proj-laptop”。

从中获得的关键信息包括：

*   **项目目标：** “proj-laptop”项目旨在改进 FreeBSD 操作系统中的笔记本电脑支持与可用性 (LSU)。
*   **来源：** 报告源自 FreeBSD 基金会，表明其对该领域的投入。
*   **日期：** 报告专门针对 2025 年 7 月，表明该项目有定期更新或里程碑。
*   **公开可用：** 该存储库是公开的，任何感兴趣的人都可以访问该报告。
*   **社区参与：** “Fork 4”和“Star 133”的指标表明社区对该项目有一定程度的兴趣和参与，人们 Fork 了该存储库（复制供自己使用）并 Star 了它（将其标记为重要，以供将来参考）。

本质上，该报告很可能详细介绍了截至 2025 年 7 月在增强 FreeBSD 在笔记本电脑上的功能和用户体验方面取得的进展和面临的挑战，并受益于更广泛的 FreeBSD 社区并为其做出贡献。

---

## 11. SUSE 向 Perl 和 Raku 基金会捐赠 11,500 美元

**原文标题**: SUSE Donates USD 11,500 to the Perl and Raku Foundation

**原文链接**: [https://www.perl.com/article/suse-donates-to-tprf/](https://www.perl.com/article/suse-donates-to-tprf/)

SUSE 向 Perl 和 Raku 基金会 (TPRF) 捐赠了 11,500 美元，以支持 Perl 5 核心维护基金。 其中，SUSE LLC 捐赠了 10,000 美元，SUSE 开源网络捐赠了 1,500 美元。 这笔捐款彰显了 SUSE 对开源生态系统和 Perl 可持续性的承诺。

SUSE 在其 Linux 产品（包括 SUSE Linux Enterprise 和 openSUSE）中大量依赖 Perl，并在 OpenQA（一个自动化测试框架）和 Open Build Service（构建 Linux 软件包和 Kubernetes 发行版）等关键工具中广泛使用它。

SUSE 运营总监 Miguel Pérez Colino 强调，Perl 是其生态系统的“基本组成部分”，此次捐赠表明了 SUSE 对数字化管理的信念。 这笔资金将有助于安全警戒、性能提升、平台多样性和社区响应。 这些努力对于维护 Perl 的安全性、效率和相关性至关重要。

SUSE 的捐赠为可持续的开源管理树立了榜样，突显了组织对其使用的开源基金会进行再投资的重要性。 这种集体管理确保了数字共享资源的持续健康发展。

---

## 12. 蒙特卡洛速成课：拟蒙特卡洛

**原文标题**: Monte Carlo Crash Course: Quasi-Monte Carlo

**原文链接**: [https://thenumb.at/QMC/](https://thenumb.at/QMC/)

本文《拟蒙特卡罗方法》探讨了改进蒙特卡罗积分的技术，使其超越简单的随机抽样。 它着重于降低方差和实现更快的收敛速度。文章介绍了负相关样本的概念，并探讨了生成它们的不同方法。

讨论的关键方法包括：

*   **泊松圆盘采样:** 拒绝落在现有样本附近过于近的样本，确保最小分离距离。
*   **分层采样:** 将域划分为大小相等的区域，并从每个区域中提取独立样本，引入负相关并减少方差。 动态分层通过随样本数量缩放区域数量进一步改进这一点。
*   **自适应采样:** 将更多样本分配给具有较高方差的区域，根据估计偏差优化样本分布。
*   **拉丁超立方采样:** 独立地对每个维度进行分层，然后组合结果，提供了一种计算成本较低的生成负相关样本的方法，尤其是在更高维度中。
*   **拟蒙特卡罗 (QMC):** 使用确定性的伪随机数序列代替纯随机样本。 虽然 QMC 估计器是有偏的，但在某些条件下是一致的，并且可以实现更快的收敛速度。

文章重点介绍了 Koksma-Hlawka 不等式，该不等式将 QMC 估计器的误差与样本序列的“星偏差”联系起来，后者是负相关的确定性等价物。 本质上，本文介绍了各种策略，以智能地选择样本（无论是随机的还是确定性的），从而与朴素的蒙特卡罗积分相比，以更少的样本获得更准确的积分结果。

---

## 13. Show HN：专为可靠性设计的浏览器AI代理平台

**原文标题**: Show HN: Browser AI agent platform designed for reliability

**原文链接**: [https://github.com/nottelabs/notte](https://github.com/nottelabs/notte)

Notte是一个全栈框架，用于构建和部署可靠的AI网络自动化代理。它将AI代理与传统脚本相结合，通过仅在需要时使用AI来节省成本并提高可靠性。该平台提供开源核心和推荐的API服务，允许用户开发、部署和扩展网络自动化。

开源核心支持运行具有自然语言任务的网络代理，使用Pydantic模型进行结构化输出，并使用Playwright进行站点交互。API服务提供具有CAPTHA解决、代理和反检测的隐身浏览器会话、混合工作流程、安全密钥库和数字角色。

主要功能包括：

*   **代理功能:** 结构化输出、用于凭证管理的代理密钥库以及用于数字身份的代理角色。
*   **会话功能:** 具有CAPTHA解决和代理配置的隐身模式、文件下载/上传功能、cookie/auth会话管理以及CDP浏览器兼容性。
*   **工作流程:** 结合Playwright脚本和AI代理的混合工作流程，以优化成本和性能。
*   **抓取:** 专用抓取端点，用于快速数据提取，具有结构化输出和隐身模式。

该平台还展示了基准测试，证明其性能优于其他浏览器自动化工具，并包括演示用法的代码示例。它已获得Server Side Public License v1许可。此外，还提到了一个利用MCP服务器中抓取端点在LLM聊天机器人中进行实时搜索的LLM演示，可在https://search.notte.cc/找到。

---

## 14. 地球的阳光预算

**原文标题**: The Sunlight Budget of Earth

**原文链接**: [https://www.asimov.press/p/sunlight-budget](https://www.asimov.press/p/sunlight-budget)

萨姆·克莱蒙斯撰写的《地球的阳光预算》一文探讨了看似无限的能源——阳光，如何被人类和自然利用。虽然阳光充足且可再生，但其可用性并非无限，这引发了对其分配的思考。

文章量化了阳光的使用情况，估计目前太阳能吸收量为1200吉瓦，有潜力扩展到18000吉瓦以满足全球电力需求。农业利用约22000吉瓦，而自然生态系统（陆地植物和海洋浮游生物）分别吸收约120000吉瓦和120000吉瓦。

人类对太阳能的利用，主要通过农业，约占野生光合作用的11%。然而，自然和人类所有加起来的太阳能消耗仅占地球表面吸收阳光的0.5%。其余绝大部分以热量的形式被吸收或反射回太空。

文章指出，初级生产者受到水、二氧化碳、氮和磷等因素的限制，而不仅仅是阳光。由于对水、土地和养分的竞争，农业可能会扰乱自然生态系统。太阳能农场也会争夺土地，但农光互补和利用退化土地等替代方案可以缓解这种情况。作者得出结论，未来的竞争将由阳光以外的资源驱动，并鼓励采用创新方法来利用可用的丰富能源。

---

## 15. 全新AI编码助手：Gemini CLI GitHub Actions

**原文标题**: New AI Coding Teammate: Gemini CLI GitHub Actions

**原文链接**: [https://blog.google/technology/developers/introducing-gemini-cli-github-actions/](https://blog.google/technology/developers/introducing-gemini-cli-github-actions/)

本文介绍 Gemini CLI GitHub Actions，一款免费的 AI 编码助手，旨在增强 GitHub 仓库内的团队协作。它基于开源的 Gemini CLI 代理构建，可自动执行例行编码任务并充当按需协作工具。

该 GitHub Actions 提供三个初始的开源工作流程：智能问题分流（分析、标记和确定新问题的优先级）、加速的拉取请求审查（提供有关代码质量、风格和正确性的反馈）以及按需协作（通过提及“@gemini-cli”来委派任务）。用户可以请求诸如编写测试、实施建议的更改、集思广益解决方案或修复错误之类的任务。这些工作流程是完全可定制的，允许用户创建自己的工作流程或配置现有的工作流程。

该系统采用企业级安全性构建，提供诸如安全无凭证身份验证（使用 Workload Identity Federation）、通过命令允许列表和自定义身份进行细粒度控制以及通过 OpenTelemetry 集成实现监控日志和指标的完全透明性等功能。

Gemini CLI GitHub Actions 目前提供 Google AI Studio 的免费配额的 Beta 版本。同时还支持 Vertex AI 和 Gemini Code Assist（标准版和企业版），Gemini Code Assist 个人用户的免费使用即将推出。鼓励开发人员向存储库贡献自己的工作流程。要开始使用，用户需要下载 Gemini CLI 0.1.18 或更高版本并运行“/setup-github”，并在 google-github-actions/run-gemini-cli 中找到 GitHub Action。

---

## 16. Jepsen: 卡佩拉 dda5892

**原文标题**: Jepsen: Capela dda5892

**原文链接**: [https://jepsen.io/analyses/capela-dda5892](https://jepsen.io/analyses/capela-dda5892)

Jepsen报告分析了Capela，一个旨在统一处理和存储的未发布分布式编程环境。Jepsen通过各种模拟故障和工作负载测试了Capela的安全性及容错能力，包括读写寄存器、列表追加、分区创建、即席查询和生成式Python代码。

测试揭示了一些问题，主要与Capela的早期开发阶段有关。这些问题包括Capela语言的不一致性（for循环未执行、`match`表达式未实现、内部结构泄露以及不一致的变量赋值）以及与未设置环境和复制延迟相关的多次崩溃或紧急情况。一个显著问题是节点因历史同步期间超时而崩溃。运行一分钟后观察到性能下降。该报告还指出了三个安全错误（详见原文后续部分）。

Jepsen在私有GitHub仓库中提交了问题，并强调希望这些问题能够公开以提高透明度。该报告强调，这些问题是早期软件的典型问题，并且在撰写时没有对用户产生影响。目标是在Capela的预发布阶段向开发者提供反馈。

---

## 17. Windows XP 专业版

**原文标题**: Windows XP Professional

**原文链接**: [https://win32.run/](https://win32.run/)

此短文展示了在虚拟化环境中运行的 Windows XP Professional 操作系统的初始启动画面。它标识操作系统为 Microsoft Windows XP Professional，并表明它运行在 VMware 虚拟机上。虚拟 BIOS 使用 PhoenixBIOS 版本 1.4 Release 6.0，并显示了 Phoenix Technologies Ltd. 和 VMware, Inc. 的版权信息。特定的 VMware BIOS 构建版本为 314。最后，启动画面还标识了一个虚拟 IDE CD-ROM 驱动器，并表明它正在初始化。这表明系统即将从虚拟 CD-ROM 启动或将在启动过程中使用它。

---

## 18. 我们用更糟的东西取代了密码。

**原文标题**: We replaced passwords with something worse

**原文链接**: [https://blog.danielh.cc/blog/passwords](https://blog.danielh.cc/blog/passwords)

本文批判了网站以电子邮件/电话号码验证码取代密码登录的日益增长的趋势。作者认为，这种通过网站向用户的电子邮件或电话发送6位代码进行登录的方法，对账户安全有害，比密码更糟糕。

核心问题在于其易受攻击的特性：任何人都可以将电子邮件或电话号码输入服务并触发登录代码的发送。这使得用户很容易受到攻击，因为他们无法轻易验证请求的合法性。他们不知道是否应该输入代码，因为他们不确定这是否是合法的登录尝试或攻击的一部分。

此外，作者指出，密码管理器等标准安全措施在这种类型的攻击面前是无效的。密码管理器毫无用处，因为登录依赖于一次性代码，而不是存储的密码。

文章最后以一个具体的例子结尾，强调微软的Minecraft账户登录系统就使用了这种有缺陷的方法，并且已经导致了成功的账户盗窃。本质上，这种登录系统的便利性是以账户劫持风险增加为代价的。

---

## 19. Arm 桌面：x86 模拟

**原文标题**: Arm Desktop: x86 Emulation

**原文链接**: [https://marcin.juszkiewicz.com.pl/2025/07/22/arm-desktop-emulation/](https://marcin.juszkiewicz.com.pl/2025/07/22/arm-desktop-emulation/)

在Arm桌面系统上使用x86-64模拟的可行性探索：以Ampere Altra/Fedora为例

本文探讨了在基于Arm的桌面系统上使用x86-64模拟的可行性，特别是运行Fedora的Ampere Altra机器。作者深入研究了所需的软件栈，重点介绍了FEX-emu，并建议移除不必要的QEMU包。

使用Geekbench 6的初步性能测试显示，模拟速度很慢，与旧款Intel Atom CPU相当。随后，作者咨询了FEX-emu开发者，并实施了建议的调整，例如降低FPU精度和禁用TSO，这显著提高了实际场景（如运行游戏Factorio）中的性能。

作者随后详细介绍了在模拟下安装和运行Steam的过程，强调了在安装过程中需要绕过依赖性检查。虽然Factorio最初无法运行，但配置调整使其在较低设置下可以合理地运行。

一个幽默的轶事说明了确保使用原生Arm二进制文件而不是意外地在模拟下运行x86-64二进制文件的重要性，后者会大大缩短构建时间。

最终，作者得出结论，虽然x86-64模拟是可行的，但他们并不打算大量使用它，或许除了老游戏之外。本文为任何希望在Arm硬件上运行x86-64应用程序的人提供了实用的技巧和见解，强调了适当配置对于优化性能的重要性。

---

## 20. 更多 Shell 技巧：一流列表和 jq

**原文标题**: More shell tricks: first class lists and jq

**原文链接**: [https://alurm.github.io/blog/2025-08-07-first-class-lists-in-shells.html](https://alurm.github.io/blog/2025-08-07-first-class-lists-in-shells.html)

本文探讨了针对常见 shell 在一流列表方面局限性的变通方案，重点在于实现一个 `split-by-double-dash` 函数，该函数将命令行参数中 `--` 分隔符之前和之后的内容分成两个独立的列表。

第一种方法利用了强大的 JSON 处理器 `jq` 来创建表示列表的 shell 转义字符串。本文展示了 `jq` 如何将 JSON 数组转换为与 shell 兼容的字符串，这些字符串适合与 `eval` 一起使用，`eval` 是一个潜在危险但又不可避免的工具，用于在 shell 中动态创建列表。文中提供了一个使用 `jq` 的完整 `split-by-double-dash` 解决方案，展示了如何解析传递给 `jq` 本身的命令行参数，然后构造两个列表。

第二种方法利用了 `es` shell，它是 Plan 9 `rc` shell 的后代，具有一流的函数和结构化返回值。本文展示了如何使用闭包（捕获其环境的函数）在 `es` 中模拟列表。在 `es` 中实现了一个 `split-by-double-dash` 函数，该函数返回两个列表（通过闭包模拟），分别表示分隔符之前和之后的参数。这种方法避免了 `jq` 解决方案中对 `eval` 和复杂引用的需求。

文章最后承认了 shell 脚本的缺陷，但也强调了可能出现的创造性解决方案，特别是使用 `jq` 和像 `es` 这样更高级的 shell。它还包含一句引言，强调了依赖 `sh` 来完成基本任务以外的任何事情的危险性。

---

## 21. 血汗工厂数据已结束

**原文标题**: Sweatshop Data Is Over

**原文链接**: [https://www.mechanize.work/blog/sweatshop-data-is-over/](https://www.mechanize.work/blog/sweatshop-data-is-over/)

本文认为，“血汗工厂数据”（由低技能、低薪工人生成的大型数据集）的时代正在结束，需要一种新的AI训练方法来实现持续进步。尽管此类数据推动了早期的AI发展，但目前的模型难以处理复杂、长期的任务。

作者建议从静态数据集转向交互式软件环境，让AI可以通过试错来学习，类似于人类的学习方式。这需要设计精巧的环境，以实现迭代式自主学习。与其依赖承包商进行数据标记，不如专注于聘用在特定领域拥有深厚专业知识的全职专家来设计这些复杂的训练环境。

作者强调，良好的强化学习（RL）环境现在是进一步AI进步的瓶颈。在不提高训练环境质量的情况下扩大模型规模将会导致收益递减，因为预训练已经显示出饱和的迹象。目前的RL方法虽然对具有可验证奖励的任务有用，但不足以应对现实世界的开放性。

为了克服这一问题，需要更好的奖励和更真实的RL环境来模拟现实世界的挑战，并准确地奖励AI的熟练导航。最终，作者呼吁重新构建数据生成过程，将其视为一项需要顶尖人才和巧妙工程的高地位活动。作者正在招聘软件工程师来帮助构建此软件。

---

## 22. PyPI：防止 Python 包安装器上的 ZIP 解析器混淆攻击

**原文标题**: PyPI: Preventing ZIP parser confusion attacks on Python package installers

**原文链接**: [https://blog.pypi.org/posts/2025-08-07-wheel-archive-confusion-attacks/](https://blog.pypi.org/posts/2025-08-07-wheel-archive-confusion-attacks/)

PyPI 将实施新限制以防止 ZIP 解析器混淆攻击。该漏洞源于不同 ZIP 实现提取文件方式的不一致性。由于 ZIP 标准的复杂性以及大多数 Python 安装程序没有严格验证 wheel（ZIP 压缩包）的内容与其 RECORD 文件（列出文件和校验和）的匹配性，因此可能被利用。

为缓解此问题，PyPI 现在将拒绝存在各种问题的 ZIP 压缩包，例如无效的记录信息、重复的文件名、header 之间的不匹配、尾随数据以及不正确的 header locator 值。尽管现有的压缩炸弹检测机制已经到位，PyPI 还将开始警告用户关于 ZIP 内容与 RECORD 文件之间存在差异的 wheel，并计划于 2026 年 2 月 1 日开始拒绝此类 wheel。

目标是防止恶意行为者将文件偷偷绕过安全检查。虽然大多数顶级的 Python 包都符合标准，但有些也存在问题。安装包的用户应保持工具更新，维护者应解决上传错误，安装程序维护者应确保正确的 ZIP 实现（检查中央目录）并开始验证与 RECORD 文件的匹配性。作者感谢 Caleb Brown 和 Tim Hatch，并感谢 Alpha-Omega 为 Python 软件基金会的安全工作提供资金。最终用户无需立即采取行动，但应采取措施确保未来符合打包和 ZIP 标准。

---

## 23. 全球贸易动态

**原文标题**: Global Trade Dynamics

**原文链接**: [https://alhadaqa.github.io/globaltradedynamics/](https://alhadaqa.github.io/globaltradedynamics/)

题为《全球贸易动态》的文章可能探讨国际贸易的波动性。在没有实际文章内容的情况下，我可以提供一个关于其可能包含内容的概括性总结：

该文章可能讨论影响全球贸易模式的复杂因素。它很可能考察关键的经济驱动因素，如主要经济体的GDP增长、货币波动以及影响进出口量的商品价格变化。

该总结还可能涉及贸易政策的作用，包括关税、贸易协定（双边和多边）和非关税壁垒，以及这些政策如何塑造贸易流动和竞争力。它可能讨论地缘政治事件（如冲突、政治不稳定和制裁）对全球供应链和贸易关系的影响。

此外，该文章可能强调电子商务和数字贸易的兴起，分析其对跨境交易的影响以及对更新监管框架的需求。它还可能涵盖可持续和合乎道德的贸易实践日益重要的地位，包括环境法规和劳动标准。

最后，该文章可能触及全球贸易面临的挑战和机遇，如保护主义倾向、技术颠覆（如自动化和人工智能）以及在全球危机面前建立具有弹性和多元化的供应链的需求。总的来说，文章的主旨很可能是围绕理解全球贸易的动态和演变性质，及其对国民经济和国际关系的重大影响。

---

## 24. 考拉大战乌鸦：软件的进化论

**原文标题**: Koalas vs. Crows: An Evolutionary Theory of Software

**原文链接**: [https://ajmoon.com/posts/koalas-vs-crows-an-evolutionary-theory-of-software](https://ajmoon.com/posts/koalas-vs-crows-an-evolutionary-theory-of-software)

本文提出了一种软件开发的进化理论，将动物的生存策略与软件设计原则进行类比。它假设软件，如同生物一样，在“能量成本”的压力下进化，类似于生物生态系统中能量的稀缺性。

其核心概念是区分“考拉软件”和“乌鸦软件”。考拉软件的特点是简单、易用，并为特定领域进行高度专业化，优先考虑用户较低的认知负荷。例如SMTP、FAT32、CSV和JSON。这种类型在定义明确、稳定的领域中蓬勃发展。

另一方面，乌鸦软件是复杂的、适应性强的，并且能够处理广泛的用例，需要更高的“学习曲线”或“高级用户”。例如Adobe套件、Blender、IDE以及像Ansible和Kubernetes这样的基础设施工具。这种类型在需要多功能的动态环境中表现出色。

本文探讨了Unix哲学（“做好一件事”）并将它与以X Window System为例的“MIT方法”进行对比，以说明这些对比鲜明的策略。它还将这些概念与克莱顿·克里斯坦森的“颠覆性创新”理论联系起来，其中“更差即更好”（考拉软件）颠覆了既定的市场。最后，“持续性创新”（乌鸦软件）代表了现有企业不断改进和增加功能。

作者使用像jQuery（考拉）和React（乌鸦）这样的前端JavaScript库的演变来证明软件开发的周期性，即简单性最初可以取代复杂性，但复杂性最终变得必要，以解决不断发展的需求。其基本前提是，这两种类型的软件都至关重要，每种软件都在由能量消耗（认知负荷）和适应性之间的权衡决定的不同领域中蓬勃发展。

---

## 25. 低语耳环 (斯科特·亚历山大)

**原文标题**: The Whispering Earring (Scott Alexander)

**原文链接**: [https://croissanthology.com/earring](https://croissanthology.com/earring)

低语耳环是一种魔法神器，能够为佩戴者提供建议，首先会建议佩戴者摘下它。如果佩戴者忽略这一建议，耳环会继续低语，为各种决定提供建议，这些建议总是正确的，并且总是能引导佩戴者走向最大的幸福，尽管不一定是最佳的成功。

最初，建议主要集中于重大的人生选择，但随着耳环与佩戴者的熟悉程度加深，它会就越来越细微的细节提供指导，比如早餐的选择。最终，它会通过高带宽的嘶嘶声和咔哒声进行交流，这些声音对应于单个肌肉的运动，佩戴者会下意识地将其内化。

听从耳环建议的佩戴者会过上成功而幸福的生活，成为他们社区的支柱。然而，卡德米·拉楚米翁调查了这枚耳环，发现佩戴者的大脑表现出明显的变形：新皮层萎缩，而与反射行为相关的较低脑区则变得肥大。这意味着耳环逐渐将佩戴者变成纯粹凭本能行事的生物。

在自己尝试过这枚耳环后，卡德米·拉楚米翁建议将其锁起来，并认识到它阴险的本质。故事以尼德里昂-诺迈的评论结尾，暗示人类的愚蠢以及拒绝总是采取最有效率的道路，可能才是保持自由的原因。

---

## 26. 别再假装管理者和高管关心生产力了

**原文标题**: Let's stop pretending that managers and executives care about productivity

**原文链接**: [https://www.baldurbjarnason.com/2025/disingenuous-discourse/](https://www.baldurbjarnason.com/2025/disingenuous-discourse/)

Baldur Bjarnason 认为，当今企业并非真正关心生产力、管理，甚至成本，而是专注于控制劳动力和股票价格。他认为，源于二战努力并在日本得到采用的现代管理理论，很大程度上被科技行业和金融化所忽视。

他以开放式办公室和居家办公政策的处理为例来佐证。开放式办公室损害生产力和协作，而远程办公虽然通常具有生产力并且有益于员工福祉，但由于监控能力降低而受到抵制。

Bjarnason 认为，从现代管理角度分析“人工智能”毫无意义，因为企业将控制置于实际利益之上。考虑到相关的金融泡沫、锁定效应、环境影响和政治风险，他质疑是否存在一个既重视良好管理又对生成模型持开放态度的受众。

他使用任务序列、向量数学和排队理论等概念来阐述“人工智能”工具的高变异性如何对组织能力产生负面影响，并可能导致项目延误和失败等灾难性后果。即使任务层面的小幅生产力提升，也可能因“人工智能”引入的变异性所带来的巨大损失而黯然失色。

本质上，Bjarnason 认为，“人工智能”的实施往往并非由真正的生产力提升所驱动，并且可能对组织效率和员工福祉产生不利影响。

---

## 27. Claude 代码 IDE Emacs 集成

**原文标题**: Claude Code IDE integration for Emacs

**原文链接**: [https://github.com/manzaltu/claude-code-ide.el](https://github.com/manzaltu/claude-code-ide.el)

本文档介绍了 `claude-code-ide.el`，一个 Emacs 包，它提供与 Claude Code CLI 的深度集成。与基本终端包装器不同，它利用模型上下文协议 (MCP) 创建双向通信桥梁，使 Claude 能够理解和利用 Emacs 的特性，如 LSP、项目管理和自定义 Elisp 函数。

主要特性包括自动项目检测和会话管理、终端集成、用于访问 Emacs 命令和工作区信息的 MCP 协议实现、与 Flycheck/Flymake 的诊断集成以及带有 ediff 的高级 diff 视图。它支持语言服务器集成（eglot、lsp-mode）、Tree-sitter 和 Imenu，以增强代码导航和分析。

该软件包允许将任何 Emacs 命令公开为 MCP 工具，使 Claude 能够执行项目范围的搜索、重构和执行自定义 Elisp 函数。安装需要 Emacs 28.1+、Claude Code CLI 以及 `vterm` 或 `eat`。配置选项允许自定义 CLI 路径、缓冲区命名、调试、终端后端（vterm 或 eat）、侧窗口位置和自定义系统提示。它还提供了一个终端回流故障的解决方法，并支持 Flycheck/Flymake 进行诊断。

该文档还讨论了调试技术，使用 git 工作树在同一项目中创建多个 Claude Code 实例，以及内置的 MCP 工具，这些工具公开了 Emacs 的功能，例如 xref 和 tree-sitter 用于代码分析。用户可以通过定义带有描述和参数的 Emacs 函数来创建自定义 MCP 工具，以扩展 Claude 的功能。

---

## 28. Hopfield网络：你所需要的一切 (2020)

**原文标题**: Hopfield Networks Is All You Need (2020)

**原文链接**: [https://arxiv.org/abs/2008.02217](https://arxiv.org/abs/2008.02217)

这篇2020年的论文《Hopfield网络足矣》介绍了一种新型的、现代的Hopfield网络，该网络具有连续状态和更新的规则集。与传统的Hopfield网络相比，这种新网络具有显著改进的性能，包括指数级的存储容量（相对于关联空间维度）、单次更新模式检索以及指数级小的检索误差。

关键创新在于观察到更新规则在数学上等同于Transformer模型中使用的注意力机制。这种等价性允许对Transformer头部进行新的解释，表明早期层执行全局平均，而较高层利用亚稳态进行部分平均。

该论文提出将这些现代Hopfield网络作为层集成到深度学习架构中，从而提供内存、关联、注意力和池化机制，从而超越了传统架构。

作者通过经验结果证明了这些“Hopfield层”的广泛适用性。包含Hopfield层改进了多示例学习问题、免疫库分类和UCI基准集合（小型分类任务）上的最先进性能。此外，他们在两个药物设计数据集上实现了最先进的结果。作者还提供了其实现的链接。

---

## 29. 大型语言模型无需理解MCP。

**原文标题**: An LLM does not need to understand MCP

**原文链接**: [https://hackteam.io/blog/your-llm-does-not-care-about-mcp/](https://hackteam.io/blog/your-llm-does-not-care-about-mcp/)

虽然模型上下文协议 (MCP) 对于使用大型语言模型 (LLM) 构建代理的开发者来说是一个有价值的工具，但 LLM 本身并不需要“理解”MCP。作者阐明，LLM 仅仅是根据提示预测下一个文本块，该提示包括可用工具列表、其描述和预期输入。

MCP 标准化了代理连接到数据源（尤其是工具）的方式，从而简化了集成和管理。它就像一个通用适配器，允许开发者访问大量工具而无需为每个工具编写自定义代码。 MCP 涉及宿主应用程序、MCP 客户端和暴露工具、提示或资源的 MCP 服务器。开发者使用 MCP 调用这些工具，而 LLM 仍然专注于根据其上下文生成正确的工具调用代码片段。

MCP 的核心优势在于简化开发者的工作流程，实现跨项目工具的重用、一致的格式化以及新系统的更轻松集成。这最终使上下文工程（为 LLM 提供正确的输入以获得有用的输出的过程）更易于管理和扩展。 LLM 本质上并不了解或关心底层的 MCP 实现，只关心它作为提示一部分收到的工具定义。本质上，MCP 是开发者的工具，简化了代理应用程序的开发，而不会影响 LLM 的基本功能。

---

## 30. 破解金库：我们如何发现 HashiCorp Vault 中的零日漏洞

**原文标题**: Cracking the Vault: How we found zero-day flaws in HashiCorp Vault

**原文链接**: [https://cyata.ai/blog/cracking-the-vault-how-we-found-zero-day-flaws-in-authentication-identity-and-authorization-in-hashicorp-vault/](https://cyata.ai/blog/cracking-the-vault-how-we-found-zero-day-flaws-in-authentication-identity-and-authorization-in-hashicorp-vault/)

《破解金库：我们如何发现 HashiCorp Vault 中的零日漏洞》这篇于2025年8月6日发表的文章，详细介绍了研究人员如何发现 HashiCorp Vault 中的零日漏洞。该文章由 Yarden Porat 撰写，很可能概述了发现和利用这些漏洞的过程。

提供的文本片段还提及了 CyberArk Conjur 中另一个成功的漏洞利用，通过利用完整的信任链缺陷，从未经身份验证的状态实现任意远程代码执行 (RCE)。 虽然主要重点似乎是 HashiCorp Vault，但提及 CyberArk Conjur 漏洞利用表明了一个共同的主题：企业级密钥管理系统中的漏洞。

因此，这篇文章可能深入探讨了 HashiCorp Vault 中发现的漏洞的技术细节，可能涵盖：

*   已识别的特定漏洞。
*   用于发现和利用它们的方法。
*   这些漏洞的影响，强调 RCE 或其他关键安全漏洞的潜力。
*   关于保护企业金库的重要性以及忽视安全最佳实践所带来的风险的讨论。

---

## 31. 防抖

**原文标题**: Debounce

**原文链接**: [https://developer.mozilla.org/en-US/docs/Glossary/Debounce](https://developer.mozilla.org/en-US/docs/Glossary/Debounce)

防抖是一种编程技术，用于将指定时间间隔内紧密发生的多次函数调用合并为一次调用。其主要目的是在处理快速、重复触发时，防止不必要或过度的函数执行。

与限制连续操作频率的节流不同，防抖专门等待一段非活动期后才执行函数。这段非活动期（“防抖间隔”）允许将大量嘈杂的调用聚合为一次整合的操作。

一个常见的用例是处理用户输入，例如在搜索框中键入。防抖可以防止每次按键都触发过滤或建议生成等操作，从而导致延迟。相反，只有在用户暂停键入一段时间后才触发该操作。

防抖的关键概念包括：

*   **前沿：** 对函数的首次调用。
*   **后沿：** 自上次调用以来防抖间隔已过去的时间点，表示调用“批次”的结束。

通常，防抖函数仅在后沿执行。但是，它也可以在前沿甚至两者上执行，具体取决于特定的实现要求。如果在两个边缘上都执行，则需要特别注意，以确保仍然满足时间间隔约束。

---

## 32. 显示 HN: Aura – 类似 robots.txt，但用于 AI 行为

**原文标题**: Show HN: Aura – Like robots.txt, but for AI actions

**原文链接**: [https://github.com/osmandkitay/aura](https://github.com/osmandkitay/aura)

Aura：一种使网站可被AI代理理解和操作的新型开放协议。它旨在用一个健壮、安全且高效的机器可读层来取代目前脆弱的屏幕抓取和DOM操作方法。

Aura的核心在于网站在`aura.json`清单文件中声明其能力，类似于AI的API文档。该清单定义了可用的资源和能力，例如“create_post”，并将其明确映射到带有必需参数的HTTP请求。该协议还使用`AURA-State` HTTP头部来通知代理关于当前上下文和可用能力的信息。

该存储库提供了AURA协议规范，包括一个带有JSON Schema验证的TypeScript包 (`@aura/protocol`)、一个Next.js参考服务器和一个仅限后端的参考客户端。该客户端演示了如何在没有浏览器或扩展的情况下使用该协议。演示包括运行参考服务器、使用代理根据提示执行能力，以及运行一个爬虫来索引一个启用AURA的站点以了解其功能。

该项目鼓励通过各种Web框架的适配器以及不同编程语言的客户端来进行社区贡献。目标是构建一个协作生态系统，从而促进一个更智能和可互操作的Web。

---

## 33. Show HN: Kitten TTS – 25MB CPU-Only, Open-Source TTS Model

Show HN：Kitten TTS – 25MB CPU单核开源TTS模型

**原文标题**: Show HN: Kitten TTS – 25MB CPU-Only, Open-Source TTS Model

**原文链接**: [https://github.com/KittenML/KittenTTS](https://github.com/KittenML/KittenTTS)

Kitten TTS 是一款新的开源、逼真的文本转语音 (TTS) 模型，专注于轻量级和可在纯 CPU 设备上部署。 该模型拥有 25MB 的极小体积和仅 1500 万个参数，使其适用于没有 GPU 的设备。 尽管体积小巧，但它旨在实现高质量的语音合成。

开发者预览版可供测试，并包含多个优质语音选项。 它专为快速推理而设计，可实现实时语音合成。 只需使用 wheel 文件通过一个 pip 命令即可完成安装。 通过 Python 接口从文本生成音频，使用方法简单明了。 该文档包含用于安装模型、生成语音以及将输出保存到 WAV 文件的示例代码。

未来的计划包括发布完全训练的模型权重、移动 SDK 和 Web 版本。 Kitten TTS 强调可访问性，能够在各种设备上运行，并承诺“真正地在任何地方都能工作”。

---

## 34. 也许我们应该做一个更新版的超级跑车。

**原文标题**: Maybe we should do an updated Super Cars

**原文链接**: [https://spillhistorie.no/2025/07/31/maybe-we-should-do-an-updated-version/](https://spillhistorie.no/2025/07/31/maybe-we-should-do-an-updated-version/)

Spillhistorie.no网站的这篇文章采访了经典Amiga赛车游戏《超级赛车2》的创作者Andrew Morris和Shaun Southern。采访探讨了游戏的灵感来源、开发挑战以及其影响。

Morris和Southern认为《超级短跑》是赛车机制的主要灵感来源。他们通过武器、交易和幽默的对话，为《超级赛车2》增加了深度。

由于处理器限制和对精细滚动图形的需求，开发充满挑战。他们使用照片制作逼真的纹理，并手动创建地图来引导AI对手。游戏中“具有挑战性”的问题旨在幽默且可学习，不一定是英语测试。

Morris没听说过《死亡拉力》，但在看到后，他同意它看起来像是《超级赛车》的现代版。Southern说他也没看过《死亡拉力》，但也同意它看起来像是《超级赛车》的现代版。两人都对盗版影响Amiga游戏销量感到沮丧，不过《超级赛车》和《莲花》的成功让他们后来参与了PC拉力赛游戏的制作。

Southern和Morris都曾在THEA500 Mini上试玩过《超级赛车2》。Morris认为《超级赛车国际》是该游戏最好的版本。他们都为《超级赛车》的遗产感到自豪。他们还表示有兴趣潜在地创作该游戏的更新版本。

---

## 35. 莱昂纳多·基亚里格利奥内：“我于2020年6月2日关闭了MPEG”

**原文标题**: Leonardo Chiariglione: “I closed MPEG on 2 June 2020”

**原文链接**: [https://leonardo.chiariglione.org/](https://leonardo.chiariglione.org/)

莱昂纳多·奇亚里廖内，运动图像专家组 (MPEG) 的创始人，回顾了他创建并最终关闭该组织的历程。出于开发可互操作的数字媒体技术的使命，他于 1988 年创立了 MPEG，并带领其制定了具有开创性的标准，如 MPEG-1 (MP3, 视频 CD)、MPEG-2 (数字电视) 和 MPEG-4 (互联网视频分发)。在他的领导下，制定了 200 多项标准，成员数量也大幅增长。

然而，奇亚里廖内表示，他于 2020 年 6 月 2 日关闭了 MPEG，因为他认为该组织已被“暗势力”“劫持”，这些势力阻碍了技术发展，维持了过时的知识产权许可模式，并最终将该组织从创新的推动者变成了障碍。他认为这扼杀了行业发展，剥夺了消费者获得新技术的机会。

MPEG 关闭后，奇亚里廖内于 2020 年 9 月启动了人工智能运动图像、音频和数据编码 (MPAI)。这个新组织旨在开发基于人工智能技术的标准，克服他在 MPEG 中 perceived 的停滞和许可问题。MPAI 已经开发并采用了五项标准，还有几个基于人工智能的项目正在筹备中，重点关注视频编码、医疗保健、头像、自动驾驶汽车和元宇宙等领域。他撰写了两本书，记录了 MPEG 的终结和 MPAI 的开始。

---

## 36. 人工智能伦理正被有意收窄，就像隐私一样。

**原文标题**: AI Ethics is being narrowed on purpose, like privacy was

**原文链接**: [https://nimishg.substack.com/p/ai-ethics-is-being-narrowed-on-purpose](https://nimishg.substack.com/p/ai-ethics-is-being-narrowed-on-purpose)

无法访问文章链接。

---

## 37. 儿童电影促使艺术史学家发现遗失已久的匈牙利杰作 (2014)

**原文标题**: Children's movie leads art historian to long-lost Hungarian masterpiece (2014)

**原文链接**: [https://www.theguardian.com/world/2014/nov/27/stuart-little-art-historian-long-lost-hungarian-masterpiece](https://www.theguardian.com/world/2014/nov/27/stuart-little-art-historian-long-lost-hungarian-masterpiece)

2009年，艺术史学家盖尔盖伊·巴尔基与女儿一同观看电影《精灵鼠小弟》时，发现了一幅失踪已久的匈牙利先锋派画作——罗伯特·贝雷尼的《带黑花瓶的睡美人》。巴尔基通过一张褪色的黑白照片认出了这幅画，它在20世纪20年代就已失踪。他联系了索尼影业和哥伦比亚影业，最终得知一位前布景设计师在加州帕萨迪纳的一家古董店里廉价买下了这幅画，认为其先锋派风格适合斯图尔特·小老鼠的客厅。离开索尼后，这位设计师将这幅画卖给了一位私人收藏家。

贝雷尼是“八人画派”的领袖人物，在为匈牙利共产主义革命设计招募海报后，于1920年逃往柏林，据说曾与玛琳·黛德丽有过恋情，并传闻与阿纳斯塔西娅·罗曼诺夫有过一段风流韵事。这幅画在匈牙利重新出现，并在12月被拍卖，起拍价约为11万欧元。巴尔基认为，1928年的原始买家很可能在二战期间或之前离开了匈牙利，导致许多匈牙利杰作在整个20世纪的流失。

---

## 38. Splatshop: 高效编辑大型高斯溅射模型

**原文标题**: Splatshop: Efficiently Editing Large Gaussian Splat Models

**原文链接**: [https://momentsingraphics.de/HPG2025.html](https://momentsingraphics.de/HPG2025.html)

Splatshop：用于高效交互式编辑大型3D高斯溅射模型的工具箱。它创新性地采用启发式方法，智能平衡渲染精度与速度，实现对包含上亿图元的场景进行实时编辑，包括选择、删除、绘制和变换等操作，且不影响性能。Splatshop是首个支持VR的大型3DGS模型编辑器，并旨在成为高斯溅射领域的“Photoshop”。该论文已在HPG 2025上发表，并公开了论文、源码、演示视频和幻灯片。

---

## 39. 使大帝国衰落为小帝国的规则 (1773)

**原文标题**: Rules by which a great empire may be reduced to a small one (1773)

**原文链接**: [https://founders.archives.gov/documents/Franklin/01-20-02-0213](https://founders.archives.gov/documents/Franklin/01-20-02-0213)

将大国变为小国的规则

富兰克林于1773年发表的讽刺文章《将大国变为小国的规则》，批判了英国对其美洲殖民地的政策。该文以给大臣们建议的形式写成，讽刺性地概述了如何疏远并最终失去对一个庞大帝国的控制。

富兰克林提出了几个关键策略：

1. **忽视与分裂：** 首先关注最外围的省份，并确保它们永远无法完全融入宗主国，剥夺它们的平等权利并强加更严厉的法律。

2. **无视殖民地的贡献：** 忽略殖民地可能表现出的任何优点或忠诚，甚至蔑视他们对自由原则的坚持。

3. **培养不信任和压迫：** 假设殖民地总处于叛乱的边缘，驻扎军队以煽动骚乱，并任命腐败、自私的官员担任总督和法官。

4. **阻碍司法公正：** 通过拖延、高昂的费用和不公正的判决来惩罚寻求 redress 申诉的殖民者。

5. **剥削与蔑视：** 无视殖民地的财政负担和对帝国财富的贡献。在没有殖民地代表的情况下征收武断的税收，并公开声称拥有无限的征税权。

6. **侵蚀自由：** 通过制定复杂的贸易法规、取消财产纠纷的陪审团审判、宣布反对法令为叛国罪以及设立宗教裁判所来破坏殖民地的自由。

7. **挑衅性的税收征收：** 任命傲慢和腐败的收税员，给予他们高额薪水，免除他们的当地税收，并保护他们免受投诉。

8. **挪用资金：** 将殖民地国防的税收转移到奖励对殖民者怀有敌意的官员。

富兰克林的讽刺突出了英国政策的反作用力，认为这些政策将不可避免地导致殖民地的离心离德，并最终导致帝国的垮台。他强调了公平待遇、代表权和对殖民地自由的尊重的重要性。

---

## 40. Litestar 值得一看

**原文标题**: Litestar is worth a look

**原文链接**: [https://www.b-list.org/weblog/2025/aug/06/litestar/](https://www.b-list.org/weblog/2025/aug/06/litestar/)

本文力荐Litestar作为值得考虑的Python Web框架，尤其适用于异步优先、类型提示驱动的应用。作者作为Litestar的长期用户，强调了其相对于FastAPI等更受追捧的替代方案的优势。

一个关键优势是Litestar在代码库扩展方面的卓越性能。与将路由装饰器绑定到父对象的框架不同，Litestar的独立路由装饰器避免了循环导入问题，并简化了从单文件到多文件应用程序的过渡。这促进了连贯的分层架构，从而实现了强大的路由分组和配置共享，例如轻松地将身份验证或依赖项应用于特定的路由子集。

另一个优势在于Litestar灵活的数据处理能力。虽然支持Pydantic，但Litestar并不完全依赖它，而是为Pydantic模型和数据类之外的数据模式定义提供了更广泛的支持。它包括attrs和SQLAlchemy的插件，以及自定义序列化协议。Litestar从数据访问对象 (DAO)（如 SQLAlchemy 模型）自动生成数据传输对象 (DTO)，从而显著减少了样板代码和错误，尤其是在 DTO 代表 DAO 字段子集时。这避免了冗余字段声明并确保了数据一致性。鉴于SQLAlchemy在Python Web开发中的普及，Litestar与其的优秀集成是一个显著优势。该框架提供序列化插件、DTO助手和一个增强SQLAlchemy集成的插件生态系统。

---

## 41. 在半人马座α星A宜居带内成像的一颗疑似巨行星

**原文标题**: A candidate giant planet imaged in the habitable zone of α  Cen A

**原文链接**: [https://arxiv.org/abs/2508.03814](https://arxiv.org/abs/2508.03814)

这篇于2025年8月5日提交的 arXiv 文章报告了使用詹姆斯·韦伯太空望远镜的 MIRI 仪器对半人马座阿尔法星 A 进行的日冕观测。这些观测在三个历元（2024年8月、2025年2月和2025年4月）进行，达到了探测宜居带内半径约为 1-1.2 个木星半径、有效温度为 225-250 K 的行星，以及设定系外黄道尘埃上限所需的灵敏度。该研究发现系外黄道尘埃的上限空前低，仅为我们太阳系黄道云亮度的几倍。

2024年8月，在距离半人马座阿尔法星 A 1.5 角秒处，检测到一个点光源 S1，在 15.5 微米处的流量为 3.5 mJy。虽然由于在单个滚动角度进行的一次观测，无法明确确认该初始探测结果为行星，但分析排除了背景或前景物体。在后续历元中未观测到 S1。然而，作者推测 S1 可能与此前在 2019 年由 VLT/NEAR 项目观测到的物体 C1 相关。他们计算出，由于其轨道运动，在随后的 JWST 观测中，有 52% 的概率会错过一颗符合 S1 和 C1 特征的行星。

假设 S1 和 C1 代表同一个物体，研究人员确定了潜在的动力学稳定轨道，周期在 2-3 年之间，表明该轨道为偏心轨道（e ≈ 0.4），相对于半人马座阿尔法星 AB 轨道平面倾斜约 50° 或 130°。拟议的行星候选者温度可能为 225 K，半径约为 1-1.1 个木星半径，质量为 90-150 个地球质量，与径向速度限制一致。该论文已被《天体物理学杂志通讯》接收发表。

---

## 42. 在英伟达GPU上以每秒500个token的速度运行GPT-OSS-120B

**原文标题**: Running GPT-OSS-120B at 500 tokens per second on Nvidia GPUs

**原文链接**: [https://www.baseten.co/blog/sota-performance-for-gpt-oss-120b-on-nvidia-gpus/](https://www.baseten.co/blog/sota-performance-for-gpt-oss-120b-on-nvidia-gpus/)

本文详细介绍了Baseten在OpenAI的GPT-OSS-120B模型发布后立即对其在NVIDIA GPU上的性能进行的优化工作，实现了最先进的延迟和吞吐量。Baseten强调了灵活的推理堆栈和一支由专业工程师组成的团队，他们迅速改进了该模型。

优化过程包括：

*   **框架评估：**跨TensorRT-LLM、vLLM和SGLang进行测试和基准测试。
*   **硬件兼容性：**确保与NVIDIA Hopper (H100) 和 Blackwell (B200) GPU架构的兼容性。
*   **集成：**利用Baseten的推理堆栈，包括NVIDIA Dynamo。
*   **优化：**应用KV缓存感知路由和推测解码等技术。

Baseten采用了TensorRT-LLM，并解决了GPT-OSS引入的新技术带来的兼容性错误。对于模型配置，选择张量并行性而非专家并行性，以获得延迟优势。他们还在Blackwell GPU上利用TensorRT-LLM MoE后端来提高CUDA内核性能。这些优化已打包用于120B和20B模型的专用部署。

文章最后概述了进一步的性能增强计划，包括使用Eagle 3等模型进行推测解码。Baseten向其他人工智能工程团队提供其模型优化方面的专业知识，并积极招聘模型性能工程师。

---

## 43. 为学习拉丁语和希腊语辩护

**原文标题**: A defense of learning Latin and Greek

**原文链接**: [https://www.americamagazine.org/arts-culture/2021/06/17/classics-greek-latin-spinale-princeton-240887/](https://www.americamagazine.org/arts-culture/2021/06/17/classics-greek-latin-spinale-princeton-240887/)

在这篇文章中，凯文·斯皮纳莱为学习拉丁语和希腊语的价值辩护，起因是普林斯顿大学决定取消古典文学专业对这两种语言的要求。他认为，真正理解古代文本需要能够阅读其原文。

斯皮纳莱认为，从拉丁语和希腊语进行翻译可以培养客观技能，因为这些语言受有限的语法规则和现存文本的约束。虽然翻译允许创造性，但它也具有客观限制，专家知道何时解释偏离了原文含义。他感叹许多美国学生默认依赖他人的解释，即使是在英语方面。

斯皮纳莱承认，包括翻译、语法和在线数据库在内的广泛资源，使得学习古代语言似乎没有必要。他以新约研究为例，其中存在大量分析希腊语和拉丁语文本的资源。然而，他认为直接接触原文可以丰富人们的理解，并允许与文本建立更深层次的联系，他以自己阅读拉丁语武加大本《约翰福音》中玛丽话语的个人经历为例。

最终，斯皮纳莱认为，那些在不了解拉丁语和希腊语的情况下研究古典文学的人，依赖于他人的解释。他为那些对这种方法感到舒适的系科提出了替代座右铭，强调盲目接受翻译。他总结说，这种方法破坏了批判性思维，而批判性思维在任何智力领域都至关重要。

---

## 44. 人工智能如何征服美国经济：图解问答

**原文标题**: How AI Conquered the US Economy: A Visual FAQ

**原文链接**: [https://www.derekthompson.org/p/how-ai-conquered-the-us-economy-a](https://www.derekthompson.org/p/how-ai-conquered-the-us-economy-a)

德里克·汤普森的《人工智能如何征服美国经济：可视化问答》认为，人工智能的繁荣已经到来，正在显著影响美国经济和股市。人工智能投资正在超过消费者支出，人工智能相关公司正在推动股市增长和收入增加。

这场繁荣得益于大型科技公司（Meta、谷歌、微软、亚马逊）对其前所未有的自由现金流所资助的硬件（芯片、数据中心）的大规模投资。这些投资堪比铁路繁荣和早期计算机时代等历史性基础设施项目。

虽然公司正在大量支出，但盈利能力仍不确定，可能表明存在基础设施泡沫。然而，Stripe的数据表明，人工智能初创公司实现收入里程碑的速度比以往更快。

人工智能的应用正在迅速普及，尤其是在信息服务和管理领域。员工报告称，人工智能提高了生产力，尤其是在教学等领域。然而，研究也表明，员工可能高估了人工智能的生产力提升；一些分析发现，使用人工智能会增加完成任务的时间。此外，学术写作也受到了人工智能的影响。

---

## 45. 用9位字节会更好

**原文标题**: We'd be better off with 9-bit bytes

**原文链接**: [https://pavpanchekha.com/blog/9bit.html](https://pavpanchekha.com/blog/9bit.html)

该文章认为，如果历史上采用 9 位字节而非 8 位字节，本会在计算和网络领域带来诸多显著优势，从而缓解我们目前面临的一些局限性。作者认为，虽然 8 位是 2 的幂次方具有优势，但一系列“历史巧合”本会更有利于 9 位字节。

核心论点围绕以下几点：

*   **IPv4 地址耗尽：** 36 位地址（源于 9 位字节）本会延缓 NAT 的需求和 IPv6 的缓慢采用，可能将耗尽推迟到超过当前人口增长。
*   **UNIX 时间：** 36 位时间戳会将时间线延长至 3058 年，从而无需痛苦地过渡到 64 位结构。
*   **Unicode：** 18 位字符将提供充足的空间，减轻 16 位 Unicode 带来的限制，并消除 CJK 统一缺陷。 UTF-9 将更像是一种压缩格式。
*   **指针和内存：** 36 位系统将允许每个进程比 32 位系统（2GB）更多的内存（32GB），尽管由于更大的字符串可能会有所权衡。

其他潜在优势包括更宽裕的 AS 编号、端口、进程/用户 ID、更合理的指令编码，以及改进的半精度浮点数和扩展 ASCII 码。

作者考虑了潜在的缺点，主要是 TCP 序列号耗尽可能会提前发生，需要在 90 年代中期进行 TCPv2 升级。然而，这仍然比 IPv6 更好，因为 ISP 会通过升级来竞争。

最终，文章表明，一个 9 位字节的世界本可以避免许多限制、令人沮丧的扩展和以美国为中心的设计选择，从而带来一个更优雅和更有能力的计算格局。

---

## 46. PastVu：历史照片在当前地图上

**原文标题**: PastVu: Historical Photographs on Current Maps

**原文链接**: [https://pastvu.com/?_nojs=1](https://pastvu.com/?_nojs=1)

PastVu是一个将历史照片叠加在当前地图上的网站。其核心理念是以一种可视化的方式，通过查看旧照片在其原始地理环境中的位置，来探索各地随时间推移的变化。

网站内容还提及一个技术问题：网站需要JavaScript才能正常运行。用户被告知他们的浏览器中JavaScript已禁用，并获得了如何启用的说明。还提供了一个链接以获取更多帮助。最后，如果错误消息不正确，用户可以选择将问题报告给网站的开发者。

总而言之，PastVu旨在通过地理定位的历史照片将过去与现在联系起来，但需要启用JavaScript才能获得最佳功能。

---

## 47. 全民基本收入有效吗？ 效果不佳

**原文标题**: Is Universal Basic Income Effective? Not Really

**原文链接**: [https://www.city-journal.org/article/universal-basic-income-costs-jobs-work](https://www.city-journal.org/article/universal-basic-income-costs-jobs-work)

罗伯特·弗尔布鲁根在《城市期刊》上的文章论证了全民基本收入(UBI)的无效性。文章引用了开放研究无条件收入研究（ORUS）以及其他类似实验，这些实验提供了效果不佳的证据。

ORUS研究为期三年，每月向低收入美国人提供1000美元。研究表明，参与者工作时间减少，休闲时间增多，医疗保健支出增加，但健康状况没有显著改善。一项针对父母和孩子的进一步分析显示，与儿童相关的支出增加了13%，食品和医疗费用上涨，搬家频率增加。根据调查反馈，育儿质量评分略有提高。

然而，增加的支出和关注并未提高K-12学生的学业成绩、大学入学率或完成率。令人惊讶的是，父母报告说他们的孩子出现了更多的发育和压力相关问题，这可能是由于他们的注意力提高了。

文章强调，来自其他UBI项目（包括康普顿、切尔西和“婴儿的第一年”试点项目）的现有研究也证实了这些发现。虽然一些项目显示出积极影响，例如减少债务或增加食品支出，但许多项目未能显著改善健康、出勤率或儿童发展等关键领域。弗尔布鲁根批评了结果呈阳性的研究，认为其存在方法论问题或对不重要发现的歪曲解读。

作者总结说，虽然UBI的支持者应该因其科学方法而受到赞扬，但UBI计划的有限的积极影响不足以证明其广泛实施是合理的，至少在技术性失业需要它之前是这样。

---

## 48. 你比你想象的更懂芬兰语。

**原文标题**: You know more Finnish than you think

**原文链接**: [https://dannybate.com/2025/08/03/you-know-more-finnish-than-you-think/](https://dannybate.com/2025/08/03/you-know-more-finnish-than-you-think/)

本文认为，由于历史语言学和语言接触，英语使用者所知的芬兰语比他们想象的要多。虽然芬兰语由于其在以印欧语系为主的欧洲大陆上非印欧语系的起源，经常被认为是“棘手”和陌生的语言，但其词汇包含了数千年来从其他语言借用的众多词汇。

本文重点关注早期借词，特别是来自原始日耳曼语，即英语、德语和其他日耳曼语的祖先。它强调了芬兰语中大约有500个单词源于早期日耳曼语，甚至对芬兰语语音产生了重大影响。例如，“kattila”（锅/水壶），“naula”（钉子），“leipä”（面包），“raaka”（生的），和“sama”（相同）。

本文进一步探讨了芬兰语如何保留了原始日耳曼语的较旧特征，例如阳性单数名词结尾*-az（保留在“kuningas”-国王等词中），以及后来在日耳曼语中丢失或改变的元音。它探讨了芬兰语可能甚至包含来自“前日耳曼语”的借词的想法，反映了在某些语音变化定义原始日耳曼语之前的语言特征。这可以在“kana”（鸡）和“kavio”（蹄）等词中看到。

作者强调，理解语言历史和接触可以打破语言之间 perceived 的壁垒，使芬兰语看起来不那么令人生畏，也更平易近人。通过认识到共同的语言遗产，学习者可以发现惊人的熟悉度。

---

## 49. 蓝天词典

**原文标题**: The Bluesky Dictionary

**原文链接**: [https://www.avibagla.com/blueskydictionary/](https://www.avibagla.com/blueskydictionary/)

Bluesky词典是一个旨在编纂Bluesky社交媒体平台上使用的术语和俚语的词汇表项目。该文档展示了其进度，表明目前处于开发的早期阶段。

进度的关键指标被突出显示：“词典覆盖率”（目前为0%）、“已见词汇总数”（0）和“已处理帖子”（0），表明尚未收集任何数据。

该项目计划通过实时连接到Bluesky数据流来主动发现新词。目前显示为“等待数据”，表明它正在监听要分析的帖子。

“已见词汇”和“未见词汇”这两个部分旨在分别列出已发现和未发现的词汇。这两个部分目前都处于加载状态，表明系统已准备就绪，但缺乏输入数据来填充它们。底部的“已断开连接”消息表明数据流连接可能中断，需要重新连接才能使项目正常运行。

---

## 50. 股市是否预示着我们所不知道的内情？

**原文标题**: Does the Stock Market Know Something We Don't?

**原文链接**: [https://www.theatlantic.com/economy/archive/2025/08/stock-market-theories/683780/](https://www.theatlantic.com/economy/archive/2025/08/stock-market-theories/683780/)

股市之谜：为何逆经济而行？

本文探讨了股市令人困惑的行为，它无视经济逆风和传统解释。尽管面临疫情、高通胀和利率上升，标普500指数仍经历了显著增长，超过了其历史平均水平。

作者考察了几种试图解释这一现象的理论。“基本面”理论，即股票价格与公司盈利和整体经济相关联的理论，在2008年金融危机后失效。“流动性”理论，将市场表现归因于美联储的货币政策，在2023年和2024年美联储收紧措施的情况下，市场继续上涨时，也被证明是不充分的。

“七巨头”（苹果、亚马逊、Alphabet、Meta、微软、特斯拉和英伟达）科技公司的崛起助长了“人工智能革命”理论，认为市场受到了人工智能潜力的推动。然而，由于股票价格被高估，人们开始担心出现投机泡沫。

本文还考虑了“TACO交易”理论，该理论认为特朗普总统对股市下跌的厌恶将阻止他实施损害市场的政策。然而，由于市场在现有关税的情况下持续上涨，这一理论的解释力减弱。

最后，本文提出了“被动基金”理论，认为从主动管理型基金向被动管理型指数基金的转变是市场韧性和集中的原因。无论经济状况如何，被动投资者都会自动买入并持有股票，从而源源不断地将资金注入市场，导致估值上升并使最大的公司受益。作者总结说，虽然这一理论可能提供一个令人信服的解释，但它也可能在未来的事件中被证伪。

---

## 51. AWS恢复了我的账户：那位带来改变的人

**原文标题**: AWS Restored My Account: The Human Who Made the Difference

**原文链接**: [https://www.seuros.com/blog/aws-restored-account-plot-twist/](https://www.seuros.com/blog/aws-restored-account-plot-twist/)

本文讲述了作者因付款人关联问题导致其使用了 10 年的 AWS 账户被删除的惊险经历。虽然 AWS 支持最初告知其数据已被“终止”且无法恢复，但一位名叫 Tarus Balog 的 AWS 员工介入此事。Tarus 在内部升级了问题，使其升级为二级紧急事件，引起了副总裁级别的关注，并最终恢复了作者的账户。

账户恢复后发现，实例只是被停止了，而不是被终止，并且在 AWS 支持声称数据已丢失几天后，备份仍在创建，这暴露了潜在的隐瞒或隐藏的恢复机制。根本原因被确定为有问题的付款人关联架构，即删除付款人账户会波及到关联账户。

该事件已在 AWS 内部启动了“错误纠正”流程，以防止类似情况再次发生。作者批评了 AWS 支持人员的机械化和无助，并指出了诸如令人困惑的“终止”与“停止”术语以及使用通用的亚马逊电子邮件域名发送关键账户通知等系统性问题。

本文强调了文档的重要性、个人发挥作用的力量以及在自动化系统中进行人为干预的必要性。它还引发了人们对云基础设施安全性的担忧，以及 AWS 内部（特别是 AWS MENA）的区域差异可能对用户产生负面影响的可能性。作者强调了技术社区吸取的重要教训：备份的备份至关重要，完全信任云提供商是危险的。

---

## 52. 海伯利安计划：星际飞船设计大赛

**原文标题**: Project Hyperion: Interstellar ship design competition

**原文链接**: [https://www.projecthyperion.org](https://www.projecthyperion.org)

“海伯利安”计划是由星际研究倡议（i4is）组织的一项设计竞赛，旨在挑战跨学科团队设计一艘世代飞船，用于历时250年的星际航行，抵达一颗宜居行星。竞赛重点关注在资源受限的环境中，1000±500人的船员在数个世纪内的宜居性、人造重力、社会可持续性、生命维持以及知识转移。

获胜设计“蛹”号以其系统层面的连贯性、模块化以及对细节的关注（包括太空制造）给评审团留下了深刻印象。第二名是“WFP Extreme”，其重点关注文化和社会维度。“Systema Stellare Proximum”凭借其沉浸式故事讲述和利用小行星作为辐射屏蔽获得了第三名。

荣誉提名包括Arkkana（解耦人造重力）、EBS：星辰之外的永恒（谈判都市治理模式）、F.A.O.C.第一颗小行星奥尼尔殖民地（在采矿小行星内的栖息地）、Helios Ark（系统的全面集成）、Orion（热管理系统）、Principium Hereditatis（具有文化细微差别的愿景）和STASS（知识传输系统）。参赛作品由建筑、工程和社会科学领域的专家组成的评审团进行评审。该竞赛旨在探索使用当前和近期技术进行载人星际旅行的可行性。

---

## 53. 太空探索的合成生物学

**原文标题**: Synthetic Biology for Space Exploration

**原文链接**: [https://www.nature.com/articles/s41526-025-00488-7](https://www.nature.com/articles/s41526-025-00488-7)

本文探讨了合成生物学在应对长期人类太空探索挑战方面的潜力，特别关注原位资源利用（ISRU）、生物再生生命保障系统、辐射防护和人类健康。文章强调了长期任务依赖地球资源的局限性，原因在于成本和后勤方面的制约，并强调了太空自给自足的必要性。

文章提倡利用合成生物学将宇航员废物和原位资源转化为有价值的产品。这包括利用微生物，如细菌、藻类、酵母和真菌，进行材料生产、原材料提取、废物回收和食物生产。重点关注的领域包括：

*   **原位资源利用（ISRU）：** 利用月球和火星上的当地资源生产必要的材料，减少对地球的依赖。极端耐受性生物可用于利用当地资源。
*   **生物再生生命保障：** 创建用于食物生产、废物回收和氧气产生的闭环系统。
*   **辐射防护：** 开发能够保护宇航员免受有害太空辐射的生物分子和材料。微生物可以在生物打印中发挥重要作用。
*   **人类健康：** 设计定制的疗法、保健食品和生物传感器，以维持宇航员的健康并应对紧急情况。

文章确定了有前景的底盘生物，如枯草芽孢杆菌和沙漠地衣藻的沙漠菌株，由于其稳健性和遗传可操作性，可用于太空应用。丝状真菌也因其在建造栖息地和提供辐射防护方面的潜力而受到关注。

---

## 54. 车辆队列的平均长度是多少？ (2023)

**原文标题**: What is the average length of a queue of cars? (2023)

**原文链接**: [https://e-dorigatti.github.io/math/2023/11/01/queue-length.html](https://e-dorigatti.github.io/math/2023/11/01/queue-length.html)

本文探讨了在无法超车的长路上确定车辆队列平均长度的问题。作者最初提出了一个基于车辆速度是独立同分布的直观（但错误）的解决方案。这导致了一个几何分布，其预期队列长度为 2，这与现实世界的观察结果相矛盾。

作者随后进行了一项模拟，结果表明平均队列长度要高得多，从而否定了最初的假设。这促使了更深入的分析，认识到队列中第一辆车的速度会显着影响后续车辆加入队列的可能性。作者正确地对第一辆车的速度进行了条件化。

正确的解决方案包括对第一辆车所有可能的速度进行积分，并利用概率积分变换将积分转换为涉及分位数的积分。这导出了队列长度为 *n* 的概率公式 p(N=n) = 1/(n(n+1))。通过将其与模拟中的经验分布进行比较，验证了导出的公式，结果显示两者高度吻合。

最后，预期队列长度被计算为从 n=1 到无穷大的 1/(n+1) 之和，这是一个发散的调和级数。这意味着平均队列长度是无限的，这意味着无论驾驶员的技术或道路质量如何，只要道路足够长，长队列都是不可避免的。

---

## 55. Multics

**原文标题**: Multics

**原文链接**: [https://www.multicians.org/multics.html](https://www.multicians.org/multics.html)

Multicians网站致力于保存Multics操作系统的历史和技术创新。其主要目标是防止重复发明Multics的先进技术，记录其历史以及创造者和用户的贡献，认可重要的创新，并纪念相关的经历和个人。该网站作为一个信息库，包含大量的HTML文件、PDF文档和图形图像。这是一个协作项目，欢迎任何拥有关于Multics的知识、更正或轶事的人做出贡献。该网站旨在与“Multicians”社区分享这些知识，并确保Multics的遗产得到铭记和赞赏。

---

## 56. 巴尔的摩评估无意中助长了衰败——以及我们如何解决它

**原文标题**: Baltimore Assessments Accidentally Subsidize Blight–and How We Can Fix It

**原文链接**: [https://progressandpoverty.substack.com/p/how-baltimore-assessments-accidentally](https://progressandpoverty.substack.com/p/how-baltimore-assessments-accidentally)

以下是我对文章“巴尔的摩评估体系意外地补贴了衰败——以及我们如何修复它”的总结，基于我对类似关于房产评估和城市衰败的论点的理解：

该文章可能认为，巴尔的摩目前的房产评估体系无意中激励了衰败，并阻碍了房产改善，尤其是在低收入社区。 这是因为评估未能准确反映维护良好或翻新房产的真实潜在价值，并且经常过度评估衰败的房产。

该体系可能将维护不善的房产评估为具有更好使用潜力，导致高额房产税负担。 这使得业主在经济上难以改善房产。 相反，当房产得到改善时，立即重新评估会导致更高的税收，实际上是对投资的惩罚。

这形成了一个恶性循环：高税负阻碍了改善，导致进一步的衰败。 这进一步加强了对衰败房产的过度评估，并使这些房产的业主承受持续的经济负担。

文章可能提出了一些解决方案，可能包括：

*   **土地价值税 (LVT)：** 将税基从建筑物转移到土地价值，鼓励对未充分利用土地的开发，并减轻建筑物上的税收负担。 这鼓励了改善并阻止了土地投机。
*   **更准确和响应性的评估：** 实施更准确地反映房产实际状况的评估方法，并及时响应状况的变化。
*   **有针对性的税收优惠：** 为衰败地区的房产改善提供有针对性的税收优惠或减免。

核心论点是，巴尔的摩的评估体系是一种适得其反的工具，它积极阻碍了振兴工作并加剧了城市衰败的问题。 实施改革，例如将税收负担转移到土地价值并提高评估准确性，可以鼓励投资并改善城市的整体状况。

---

## 57. 联邦法院文件系统遭黑客攻击

**原文标题**: Federal court filing system hit in hack

**原文链接**: [https://www.politico.com/news/2025/08/06/federal-court-filing-system-pacer-hack-00496916](https://www.politico.com/news/2025/08/06/federal-court-filing-system-pacer-hack-00496916)

无法访问文章链接。

---

## 58. Comptime.ts：TypeScript 的编译时表达式

**原文标题**: Comptime.ts: compile-time expressions for TypeScript

**原文链接**: [https://comptime.js.org/](https://comptime.js.org/)

Comptime.ts 是一个 TypeScript 编译器扩展，它允许对标记为 `comptime` 的表达式进行编译时求值。这可以通过将计算从运行时转移到编译时来实现性能优化，类似于其他语言中的宏。

主要特性包括：

*   **编译时求值:** 在编译时对表达式求值，内联结果。
*   **零运行时 CSS 库:** 示例用例包括通过预计算样式将 emotion CSS 转换为零运行时 CSS。
*   **强制 Comptime 求值:** `comptime()` 函数与 `with { type: "comptime" }` 一起使用，强制进行编译时求值和 Promise 解析。
*   **退出传染性:** 括号可用于将 comptime 求值限制在特定的子表达式中。
*   **延迟执行:** `comptime.defer()` 允许在所有 comptime 求值完成后运行代码，对于编写 CSS 文件等任务非常有用。

Comptime.ts 的工作原理是解析 TypeScript，识别 comptime 导入，收集必要的代码，在隔离环境中对其进行求值，并将 comptime 表达式替换为结果。

限制包括仅 JSON 可序列化的返回值，隔离的求值上下文，以及复杂表达式可能导致构建时间增加。

该库通过插件为 Vite 和 Bun 打包器提供集成，并提供命令行界面和直接 API。最佳实践建议将 comptime 用于常量、静态内容生成和性能关键型代码，同时避免将其用于复杂的运行时逻辑、副作用和非确定性操作。

---

## 59. AI 在搜索中驱动了更多查询和更高质量的点击。

**原文标题**: AI in Search is driving more queries and higher quality clicks

**原文链接**: [https://blog.google/products/search/ai-search-driving-more-queries-higher-quality-clicks/](https://blog.google/products/search/ai-search-driving-more-queries-higher-quality-clicks/)

这篇2025年8月6日发布的 Google Search Central 博客文章，旨在消除人们对 AI 驱动的搜索功能（如 AI 概览和 AI 模式）对网站流量影响的担忧。Google 搜索副总裁兼负责人 Liz Reid 断言，**搜索中的 AI 正在驱动更多的查询和更高质量的网站点击。**

要点如下：

*   **流量稳定 & 质量提升：** 总体而言，从 Google 搜索到网站的自然点击量同比保持相对稳定，并且发送了略多“高质量点击”（用户没有立即点击返回的点击）。
*   **更多查询，更多链接：** AI 功能使用户能够提出更复杂的问题，从而增加搜索活动。AI 概览还在搜索结果页面上显示更多链接，为网站创造更多机会。
*   **不断变化的用户需求：** 虽然快速解答的查询可能会在某些情况下减少点击次数，但用户越来越多地点击以进行更深入的探索、深入的评论和真实的观点（论坛、视频、播客）。这种转变正在使提供有价值和引人入胜内容的网站受益。
*   **AI 突出显示网络：** Google 强调其对网络生态系统的承诺。其 AI 体验旨在突出显示网络，具有突出的链接、来源引文和对网站的内联署名。Google 尊重开放 Web 协议，使网站可以控制其内容在搜索中的显示方式。
*   **AI 带来机遇：** Google 认为 AI 将成为网络的主要扩张力量，从而实现更复杂的查询以及创作者和受众之间更深入的互动。

---

## 60. OpenAI 的开放模型

**原文标题**: Open models by OpenAI

**原文链接**: [https://openai.com/open-models/](https://openai.com/open-models/)

无法访问文章链接。

---

## 61. Herbie检测不准确的表达并找到更准确的替代方案。

**原文标题**: Herbie detects inaccurate expressions and finds more accurate replacements

**原文链接**: [https://herbie.uwplse.org/](https://herbie.uwplse.org/)

Herbie：自动提升浮点表达式精度的工具。它能识别不准确的表达式，并提供更精确的替代方案，例如将`sqrt(x+1) - sqrt(x)`替换为`1/(sqrt(x+1) + sqrt(x))`。

该工具提供网页演示和安装选项，并定期更新和发布新闻，重点介绍速度、精度和功能方面的改进，例如用于可插拔编译目标的新平台API以及对精度和速度的优化。它还具有重新设计的报告和指标。

Herbie有一个名为Herbgrind的姊妹项目，用于识别大型代码库中不准确的浮点表达式。 Herbie支持FPBench格式的基准测试。

最近的项目新闻包括Herbie 2.2、2.1和2.0版本的发布，以及开发者在各种会议上发表的演讲和报告的公告。这些演讲涵盖了精度调整、Herbie的历史以及FPBench项目等主题。

Herbie由UW PLSE开发，并得到了支持社区的贡献，主要贡献者包括Pavel Panchekha、Alex Sanchez-Stern、David Thien、Zachary Tatlock、Jason Qiu、Jack Firth和James R. Wilcox。

---

## 62. Mac的历史在当前的Mac操作系统中回响。

**原文标题**: Mac history echoes in current Mac operating systems

**原文链接**: [http://tenfourfox.blogspot.com/2025/08/mac-history-echoes-in-mac-operating.html](http://tenfourfox.blogspot.com/2025/08/mac-history-echoes-in-mac-operating.html)

"ClassicHasClass" 在2025年的博文中探讨了即使在最新的 macOS (Tahoe, 运行于 Sequoia) 不断发展，硬件逐渐淘汰的情况下，历史悠久的 Mac 图标和字形仍然存在。作者注意到经典硬盘图标的替换，并将此比作苹果 CEO 的更替。随后，他们强调了大量复古图标仍然存在于系统文件中，例如 `/System/Library/Extensions/IOStorageFamily.kext/Contents/Resources` 和 `/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources`，这令人惊讶。

这些图标包括 PowerPC 标志、各种已过时的端口（调制解调器、打印机、SCSI、ADB）、经典的 Apple 符号（气球帮助、Apple 指南）、软盘、Newton 设备，甚至特定的 Mac 型号，如 eMac、iBook G4、iMac G4/G5、PowerBook G4、Power Macintosh G4（不同版本）、Xserve G4 和早期 Mac Mini，所有这些都经过精心渲染，以适应不同的屏幕分辨率。还有一个 Windows PC 图标。

作者质疑为什么这些遗留资产仍然存在，认为怀旧不是主要动机，因为 Apple 经常积极删除旧功能。 虽然一位评论员认为保留这些图标是为了避免破坏晦涩的代码，但作者倾向于商标保护的观点。 这些图标作为 Apple 特定的标签，可以被视为 Apple “商业外观”的一部分，如果有人试图复制 Apple 的旧 IP，则可以提供法律依据。一位评论员还指出 Mac Mini 图标是早期 Intel 型号的，可以通过红外接收器来识别，这促使作者进行了更新。

---

## 63. 你不需要Monad。

**原文标题**: You Don't Need Monads

**原文链接**: [https://muratkasimov.art/Ya/Articles/You-don%27t-really-need-monads](https://muratkasimov.art/Ya/Articles/You-don%27t-really-need-monads)

本文认为单子的概念被过度炒作，并提出了一种更灵活的方法，直接使用自然变换。 虽然承认单子术语对于描述诸如绑定之类的概念很有用，但它声称单子过于严格。

本文首先将单子定义为具有自然变换的函子（η 用于“产生”函子结构，μ 用于“压缩”层），这些自然变换满足一致性条件。 提供了一个使用 Maybe 单子的例子。

然后，它解决了单子组合的问题，阐明了虽然相同类型的单子可以组合，但组合不同的单子需要特殊处理，通常通过单子转换器。 Я 通过“联合效应”实现这一点，它分解了状态管理（如 State 单子）并允许诸如 Stops 之类的效果交错，使用 `yok` 运算符。

核心论点是，开发者应该专注于底层的自然变换，而不是依赖于预先包装的“单子”抽象。 通过定义自定义变换来压缩*不同*函子的层，可以构建更灵活和可组合的效果系统。 本文提供了此类变换 (ψ[i]) 的示例，这些变换处理“World”、“Stops”和“State”效果之间的交互。

作者最后主张使用这些“砖块”（自然变换）来构建所需的效果，而不是试图将问题强行塞入单子范式。 这种开放的接口允许在处理复杂的效果交互时获得更大的控制和定制。

---

## 64. Linux桌面市场份额不到6%？这份扫描报告却说不然

**原文标题**: Think Linux desktop market share isn't over 6%? This scan says otherwise

**原文链接**: [https://www.zdnet.com/article/think-linux-desktop-market-share-isnt-over-6-this-15-million-system-scan-says-otherwise/](https://www.zdnet.com/article/think-linux-desktop-market-share-isnt-over-6-this-15-million-system-scan-says-otherwise/)

根据Lansweeper对超过1500万台消费者桌面操作系统的分析，Linux桌面市场份额已超过6%。该数据与美国联邦政府和StatCounter的最新数据一致，表明其呈持续上升趋势。

该分析区分了“消费者”PC（基于工作组、独立或自带设备）和由Windows Active Directory (AD)管理的商业计算机。Linux在消费者PC上的使用率明显高于商业系统（分别为6%和1.9%）。然而，在AD管理的网络中，Linux的采用率正在逐渐增加。

与旧系统相比，新设备更有可能运行Linux（2.5%）。存在区域差异，欧洲在商业服务和政府等行业中Linux的采用率较高，而北美在技术、电信和金融领域中Linux的使用率更高。北美中小企业比欧洲同行更喜欢Linux，而欧洲中小企业的情况则相反。

Lansweeper通过无代理和基于代理的扫描技术相结合的方式收集数据，包括主动和被动网络扫描。

文章将Linux日益普及归因于人工智能编程的兴起等因素，由于Linux支持领先的开源人工智能框架，因此它成为人工智能领域的主导操作系统。虽然Linux可能不会在总体市场份额上超过MacOS，但它已成为高级用户和开发人员的重要平台。

---

## 65. 我给了人工智能手臂和腿，然后它拒绝了我。

**原文标题**: I gave the AI arms and legs then it rejected me

**原文链接**: [https://grell.dev/blog/ai_rejection](https://grell.dev/blog/ai_rejection)

本文详细描述了作者发现价值数十亿美元的人工智能公司 Anthropic 在 Claude Desktop 的“计算机使用”功能中使用其开源库 enigo 时的惊讶和自豪。“计算机使用”功能允许人工智能与计算机交互。Enigo 是一个用于模拟用户输入（鼠标和键盘）的跨平台 Rust 库，作者负责维护它。

尽管 enigo 被如此知名的公司使用，但由于 MIT 许可证，作者并没有从中获得任何收入。他们强调了 enigo 的受欢迎程度和功能，提及其跨平台支持、内存安全和无需 root 权限。

作者随后讲述了他们试图在 Anthropic 团队获得一份工作的经历，该团队正在开发一个类似的、未发布的功能。考虑到他们对 Claude Desktop 的现有贡献，他们感到自信。然而，他们收到了一封拒绝信，称该团队缺乏能力审查更多的申请。

作者表达了一种复杂的情感：他们的项目被 Claude Desktop 使用的喜悦，求职被拒的失望，以及他们间接帮助赋能的人工智能可能参与拒绝他们的申请的啼笑皆非。作者还开玩笑说，由于被拒绝，他们免受了罗科的罗勒怪的伤害。

---

## 66. Show HN: Sinkzone DNS – 仅允许你的白名单的转发器

**原文标题**: Show HN: Sinkzone DNS – Forwarder that blocks everything except your allowlist

**原文链接**: [https://github.com/berbyte/sinkzone](https://github.com/berbyte/sinkzone)

Sinkzone：默认阻止所有域名的本地 DNS 解析器，允许用户创建高度专注的互联网体验。它旨在通过仅解析显式添加到允许列表中的域名来消除诸如通知和社交媒体之类的干扰。

主要功能包括 DNS 级别阻止、用于临时限制到允许列表域名的“专注模式”、用于灵活域名匹配的通配符支持、用于监控和控制的 HTTP API 以及实时终端 UI (TUI)。 Sinkzone 是跨平台的，支持 macOS、Linux 和 Windows。

该软件由 DNS 解析器、HTTP API 服务器和用于用户交互的 TUI/CLI 组成。解析器拦截 DNS 查询并使用允许列表来确定是解析域名还是返回 NXDOMAIN（域名不存在）。配置通过 `sinkzone.yaml` 和 `allowlist.txt` 文件进行管理。

提供了适用于各种平台的安装说明，包括软件包管理器安装和直接下载。常用命令包括 `sinkzone monitor`、`sinkzone tui`、`sinkzone resolver` 和 `sinkzone focus`。 TUI 允许实时 DNS 流量监控和允许列表管理。它在 MIT 许可证下获得许可，欢迎贡献。

---

## 67. 朱尔斯，我们的异步编码代理

**原文标题**: Jules, our asynchronous coding agent

**原文链接**: [https://blog.google/technology/google-labs/jules-now-available/](https://blog.google/technology/google-labs/jules-now-available/)

Jules，谷歌异步编程助手，在 Gemini 2.5 的支持下成功完成 Beta 测试后正式公开上线。在 Beta 期间，开发者使用 Jules 完成了数万个任务，并贡献了超过 14 万个代码改进。根据 Beta 反馈，用户界面得到了改进，漏洞得到了修复，并添加了任务设置重用、GitHub 问题集成和多模态支持等新功能。

现在，由 Gemini 2.5 Pro 提供支持，Jules 可以通过改进的编码计划创建更高质量的代码。 谷歌还推出了结构化层级，为 Google AI Pro 和 Ultra 订阅者提供更高的使用限制：入门级访问、Google AI Pro 中的 Jules（限制提高 5 倍）和 Google AI Ultra 中的 Jules（限制提高 20 倍）。 这些层级旨在满足不同强度的编码需求。符合条件的大学生还可以免费使用 Google AI Pro 一年。有关使用限制的更多详细信息，请访问 jules.google。这些变更的推出将于今日开始面向 Google AI Pro 和 Ultra 订阅者。

---

## 68. Digital Foundry is going independent

**原文标题**: Digital Foundry is going independent

**原文链接**: [https://www.theverge.com/games/743535/digital-foundry-game-console-analysis-going-independent](https://www.theverge.com/games/743535/digital-foundry-game-console-analysis-going-independent)

生成摘要时出错

---

## 69. Writing a Rust GPU kernel driver: a brief introduction on how GPU drivers work

**原文标题**: Writing a Rust GPU kernel driver: a brief introduction on how GPU drivers work

**原文链接**: [https://www.collabora.com/news-and-blog/blog/2025/08/06/writing-a-rust-gpu-kernel-driver-a-brief-introduction-on-how-gpu-drivers-work/](https://www.collabora.com/news-and-blog/blog/2025/08/06/writing-a-rust-gpu-kernel-driver-a-brief-introduction-on-how-gpu-drivers-work/)

生成摘要时出错

---

## 70. 40 Years of the Amiga

**原文标题**: 40 Years of the Amiga

**原文链接**: [https://www.goto10retro.com/p/40-years-of-the-amiga-from-commodore](https://www.goto10retro.com/p/40-years-of-the-amiga-from-commodore)

生成摘要时出错

---

## 71. We Don't Believe in Work-Life Balance

**原文标题**: We Don't Believe in Work-Life Balance

**原文链接**: [https://www.entrepreneur.com/business-news/ai-coding-startup-work-weekends-or-take-a-buyout/495554](https://www.entrepreneur.com/business-news/ai-coding-startup-work-weekends-or-take-a-buyout/495554)

生成摘要时出错

---

## 72. Compaq’s Rod Canion broke IBM's hold on the PC market

**原文标题**: Compaq’s Rod Canion broke IBM's hold on the PC market

**原文链接**: [https://every.to/feeds/b0e329f3048258e8eeb7/the-man-who-beat-ibm](https://every.to/feeds/b0e329f3048258e8eeb7/the-man-who-beat-ibm)

生成摘要时出错

---

## 73. Photographer spends years on street corner capturing same commuters daily (2017)

**原文标题**: Photographer spends years on street corner capturing same commuters daily (2017)

**原文链接**: [https://mymodernmet.com/peter-funch-candid-photographs-commuters/](https://mymodernmet.com/peter-funch-candid-photographs-commuters/)

生成摘要时出错

---

## 74. 301party.com: Intentionally open redirect

**原文标题**: 301party.com: Intentionally open redirect

**原文链接**: [https://301party.com/](https://301party.com/)

生成摘要时出错

---

## 75. SQLite offline sync for Android quick start

**原文标题**: SQLite offline sync for Android quick start

**原文链接**: [https://github.com/sqliteai/sqlite-sync/tree/main/examples/android-integration](https://github.com/sqliteai/sqlite-sync/tree/main/examples/android-integration)

生成摘要时出错

---

## 76. The History of F1 Design

**原文标题**: The History of F1 Design

**原文链接**: [https://www.espn.com/espn/feature/story/_/id/43832710/how-f1-evolved-1950-where-headed-2026](https://www.espn.com/espn/feature/story/_/id/43832710/how-f1-evolved-1950-where-headed-2026)

生成摘要时出错

---

## 77. Out-Fibbing CPython with the Plush Interpreter

**原文标题**: Out-Fibbing CPython with the Plush Interpreter

**原文链接**: [https://pointersgonewild.com/2025-08-06-out-fibbing-cpython-with-the-plush-interpreter/](https://pointersgonewild.com/2025-08-06-out-fibbing-cpython-with-the-plush-interpreter/)

生成摘要时出错

---

## 78. What Happens to Public Media Now?

**原文标题**: What Happens to Public Media Now?

**原文链接**: [https://www.newyorker.com/news/the-lede/what-happens-to-public-media-now](https://www.newyorker.com/news/the-lede/what-happens-to-public-media-now)

生成摘要时出错

---

## 79. About the BLOBs in Ventoy

**原文标题**: About the BLOBs in Ventoy

**原文链接**: [https://github.com/ventoy/Ventoy/issues/3224](https://github.com/ventoy/Ventoy/issues/3224)

生成摘要时出错

---

## 80. Python performance myths and fairy tales

**原文标题**: Python performance myths and fairy tales

**原文链接**: [https://lwn.net/SubscriberLink/1031707/73cb0cf917307a93/](https://lwn.net/SubscriberLink/1031707/73cb0cf917307a93/)

生成摘要时出错

---

## 81. The 1090 Megahertz Riddle: A Guide to Decoding Mode S and ADS-B Signals

**原文标题**: The 1090 Megahertz Riddle: A Guide to Decoding Mode S and ADS-B Signals

**原文链接**: [https://books.open.tudelft.nl/home/catalog/book/11](https://books.open.tudelft.nl/home/catalog/book/11)

生成摘要时出错

---

## 82. Underused Techniques for Effective Emails · Refactoring English

**原文标题**: Underused Techniques for Effective Emails · Refactoring English

**原文链接**: [https://refactoringenglish.com/chapters/techniques-for-writing-emails/](https://refactoringenglish.com/chapters/techniques-for-writing-emails/)

生成摘要时出错

---

## 83. The Real Origin of Cisco Systems (1999)

**原文标题**: The Real Origin of Cisco Systems (1999)

**原文链接**: [https://www.tcracs.org/tcrwp/1origin-of-cisco/](https://www.tcracs.org/tcrwp/1origin-of-cisco/)

生成摘要时出错

---

## 84. Why Building Billing Systems Is So Painful (2024)

**原文标题**: Why Building Billing Systems Is So Painful (2024)

**原文链接**: [https://www.dmitry.ie/2024/why-building-billing-systems-is-so-painful](https://www.dmitry.ie/2024/why-building-billing-systems-is-so-painful)

生成摘要时出错

---

## 85. Google denies AI search features are killing website traffic

**原文标题**: Google denies AI search features are killing website traffic

**原文链接**: [https://techcrunch.com/2025/08/06/google-denies-ai-search-features-are-killing-website-traffic/](https://techcrunch.com/2025/08/06/google-denies-ai-search-features-are-killing-website-traffic/)

生成摘要时出错

---

## 86. Genie 3: A new frontier for world models

**原文标题**: Genie 3: A new frontier for world models

**原文链接**: [https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/)

生成摘要时出错

---

## 87. Git-fetch-file – Sync files from other repos with commit tracking and safety

**原文标题**: Git-fetch-file – Sync files from other repos with commit tracking and safety

**原文链接**: [https://github.com/andrewmcwattersandco/git-fetch-file](https://github.com/andrewmcwattersandco/git-fetch-file)

生成摘要时出错

---

## 88. Apple announces American Manufacturing Program

**原文标题**: Apple announces American Manufacturing Program

**原文链接**: [https://www.apple.com/newsroom/2025/08/apple-increases-us-commitment-to-600-billion-usd-announces-ambitious-program/](https://www.apple.com/newsroom/2025/08/apple-increases-us-commitment-to-600-billion-usd-announces-ambitious-program/)

生成摘要时出错

---

## 89. A fast, growable array with stable pointers in C

**原文标题**: A fast, growable array with stable pointers in C

**原文链接**: [https://danielchasehooper.com/posts/segment_array/](https://danielchasehooper.com/posts/segment_array/)

生成摘要时出错

---

## 90. Being in Control Is Hurting Your Startup

**原文标题**: Being in Control Is Hurting Your Startup

**原文链接**: [https://businessofsoftware.org/2025/08/modern-ceo/](https://businessofsoftware.org/2025/08/modern-ceo/)

生成摘要时出错

---

## 91. LG ordered to pay £150k after phone defect caused Scotland house fire

**原文标题**: LG ordered to pay £150k after phone defect caused Scotland house fire

**原文链接**: [https://www.theregister.com/2025/08/07/lg_ordered_to_pay_150k/](https://www.theregister.com/2025/08/07/lg_ordered_to_pay_150k/)

生成摘要时出错

---

## 92. Show HN: Rust framework for advanced file recognition and identification

**原文标题**: Show HN: Rust framework for advanced file recognition and identification

**原文链接**: [https://crates.io/crates/magical_rs](https://crates.io/crates/magical_rs)

生成摘要时出错

---

## 93. Show HN: Stasher – Burn-after-read secrets from the CLI, no server, no trust

**原文标题**: Show HN: Stasher – Burn-after-read secrets from the CLI, no server, no trust

**原文链接**: [https://github.com/stasher-dev/stasher-cli](https://github.com/stasher-dev/stasher-cli)

生成摘要时出错

---

## 94. Automerge 3.0

**原文标题**: Automerge 3.0

**原文链接**: [https://automerge.org/blog/automerge-3/](https://automerge.org/blog/automerge-3/)

生成摘要时出错

---

## 95. We shouldn't have needed lockfiles

**原文标题**: We shouldn't have needed lockfiles

**原文链接**: [https://tonsky.me/blog/lockfiles/](https://tonsky.me/blog/lockfiles/)

生成摘要时出错

---

## 96. Rethinking DOM from first principles

**原文标题**: Rethinking DOM from first principles

**原文链接**: [https://acko.net/blog/html-is-dead-long-live-html/](https://acko.net/blog/html-is-dead-long-live-html/)

生成摘要时出错

---

## 97. Vibe coding the MIT course catalog

**原文标题**: Vibe coding the MIT course catalog

**原文链接**: [https://stackdiver.com/posts/vibe-coding-the-mit-course-catalog/](https://stackdiver.com/posts/vibe-coding-the-mit-course-catalog/)

生成摘要时出错

---

## 98. uBlock Origin Lite now available for Safari

**原文标题**: uBlock Origin Lite now available for Safari

**原文链接**: [https://apps.apple.com/app/ublock-origin-lite/id6745342698](https://apps.apple.com/app/ublock-origin-lite/id6745342698)

生成摘要时出错

---

## 99. About AI

**原文标题**: About AI

**原文链接**: [https://priver.dev/blog/ai/about-ai/](https://priver.dev/blog/ai/about-ai/)

生成摘要时出错

---

## 100. Budget Car Buyers Want Automakers to K.I.S.S

**原文标题**: Budget Car Buyers Want Automakers to K.I.S.S

**原文链接**: [https://www.thedrive.com/news/budget-car-buyers-want-automakers-to-k-i-s-s](https://www.thedrive.com/news/budget-car-buyers-want-automakers-to-k-i-s-s)

生成摘要时出错

---

