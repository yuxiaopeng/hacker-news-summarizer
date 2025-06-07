# Hacker News 热门文章摘要 (2025-06-07)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 仇恨电台

**原文标题**: Hate Radio

**原文链接**: [https://rwandanstories.org/genocide/hate_radio.html](https://rwandanstories.org/genocide/hate_radio.html)

无法访问文章链接。

---

## 2. 无家可归实验——或如何用人工智能保护你的生活

**原文标题**: The Homelessness Experiment – or how to AI-proof your life

**原文链接**: [https://corentin.trebaol.com/Blog/8.+The+Homelessness+Experiment](https://corentin.trebaol.com/Blog/8.+The+Homelessness+Experiment)

无家可归实验——或如何让你的生活不受人工智能影响

---

## 3. 比尔·阿特金森去世了。

**原文标题**: Bill Atkinson has passed away

**原文链接**: [https://m.facebook.com/story.php?story_fbid=10238073579963378&id=1378467145](https://m.facebook.com/story.php?story_fbid=10238073579963378&id=1378467145)

无法访问文章链接。

---

## 4. 我们为何放弃Nix

**原文标题**: Why We're Moving on from Nix

**原文链接**: [https://blog.railway.com/p/introducing-railpack](https://blog.railway.com/p/introducing-railpack)

Railway正在用名为Railpack的新系统取代其现有的构建系统Nixpacks。虽然Nixpacks对许多用户来说运行良好，但其局限性阻碍了平台扩展到更大的用户群。

Nixpacks的主要问题在于其依赖于Nix基于提交的软件包版本控制。这使得细粒度的版本控制变得困难，并导致软件包版本更新时出现不可预测的构建失败。由于Nix的单体依赖结构，镜像尺寸也过大，阻碍了缓存效率。

Railpack通过一个全新的架构解决了这些问题。主要优势包括：

*   **细粒度的版本控制：** 支持软件包的特定major.minor.patch版本。
*   **更小的构建：** 与Nixpacks相比，镜像尺寸减少了38-77%。
*   **更好的缓存：** 与BuildKit的直接集成提供了更精确的层和文件系统控制，从而提高了缓存命中率。
*   **锁定的依赖项：** 依赖项在成功构建后被锁定，防止版本更新导致意外失败。

Railpack利用定制的BuildKit LLB + Frontend进行细粒度的镜像构建，并使用Mise进行版本解析和软件包安装。构建过程分为分析、计划和生成阶段，从而实现高度并行的构建和精确的层控制。

Railpack目前处于测试阶段，支持Node、Python、Go、PHP和静态HTML部署，并内置支持Vite、Astro、CRA和Angular等流行的静态站点生成器。Railway的目标是专注于为流行的语言提供更深层次的支持。Railpack是开源的。

---

## 5. 使用 Zig 进行底层优化

**原文标题**: Low-Level Optimization with Zig

**原文链接**: [https://alloc.dev/2025/06/07/zig_optimization](https://alloc.dev/2025/06/07/zig_optimization)

本文推崇 Zig 语言，认为它因其详尽的表达能力和强大的编译时执行 (comptime) 功能，非常适合底层优化。虽然编译器通常擅长优化，但由于缺乏意图，它们有时会错过机会，尤其是在高级语言中。Zig 的详尽表达能力允许开发者表达更多意图，为编译器提供关键信息，如对齐、别名和大小，从而实现更好的代码生成。

Comptime 是 Zig 的秘密武器，它能够在编译时生成代码，取代了对传统宏、模板和泛型的需求。它允许对类型进行检查、反射和生成。与宏不同，comptime 代码只是在编译时运行的常规 Zig 代码，没有副作用。

本文通过一个字符串比较的例子展示了 comptime 的优势。一个简单的字符串比较方法与一个 comptime 版本进行了对比，comptime 版本通过在编译时知道其中一个字符串来优化代码，从而显著改进了汇编代码。文章进一步展示了如何优化这种 comptime 比较，使用 SIMD 寄存器比较更大的块。

最后，文章强调了 comptime 的实用性不仅限于编译时常量，还展示了如何将其用于基于编译时生成过程的运行时调度。作者最后赞扬了 Zig 使编写高性能代码变得更容易的能力，并鼓励读者超越语言之争，拥抱图灵完备性的力量，同时仍然拥有自己喜欢的语言。

---

## 6. Radiant AI 到底是什么？

**原文标题**: What was Radiant AI, anyway?

**原文链接**: [https://blog.paavo.me/radiant-ai/](https://blog.paavo.me/radiant-ai/)

本文深入探讨了Bethesda公司《上古卷轴IV：湮灭》中“Radiant AI”背后的真相。许多人认为这个承诺的功能从未完全实现。在《湮灭》重制版重新引发人们的兴趣后，作者开始调查Radiant AI最初的设想、实际效果以及它在Bethesda后续作品中的遗产。

文章探讨了发布前的宣传，重点关注GameInformer的封面故事和2005年E3展会的演示。这些来源承诺了动态的NPC行为，角色可以自主地满足吃饭、工作甚至犯罪等需求，所有这些都独立于玩家的互动。Todd Howard的演示展示了一个店主独立练习射箭和使用药水，进一步激发了人们的期望。

作者通过粉丝访谈来考察Bethesda自己的声明，揭示了他们创造一个NPC行为感觉自然且非脚本化的世界的意图，类似于《晨风》中的任务。然而，它也强调了使这些独立行为对玩家来说有意义且可感知的挑战。

文章认为，虽然雄心勃勃，但现实可能并未达到预期。它为进一步探索Radiant AI的机制、揭穿神话以及考察其在后续游戏（如《辐射3》、《天际》和《星空》）中的存在（或缺失）奠定了基础。核心问题仍然是：Radiant AI是一个革命性的系统，一个营销夸张，还是介于两者之间？

---

## 7. OneText (YC W23) 招聘 DevOps/DBA 首席工程师

**原文标题**: OneText (YC W23) Is Hiring a DevOps/DBA Lead Engineer

**原文链接**: [https://jobs.ashbyhq.com/one-text/b95952a2-9bc2-4c3a-9da1-3dcc157b4a27](https://jobs.ashbyhq.com/one-text/b95952a2-9bc2-4c3a-9da1-3dcc157b4a27)

OneText (YC W23) 招聘 DevOps/DBA 首席工程师。需要 JavaScript 运行应用。

---

## 8. 引发大规模科技裁员的税法定时炸弹

**原文标题**: The time bomb in the tax code that's fueling mass tech layoffs

**原文链接**: [https://qz.com/tech-layoffs-tax-code-trump-section-174-microsoft-meta-1851783502](https://qz.com/tech-layoffs-tax-code-trump-section-174-microsoft-meta-1851783502)

石英财经一篇报道指出，美国税法第174条中一项鲜为人知的变更——深藏于2017年《减税与就业法案》(TCJA)之中——是导致自2023年以来大规模科技裁员的一个关键因素。 近70年来，公司可以立即扣除100%的研发支出，从而激励国内创新。 TCJA大幅降低了公司税率，但也包含一项延迟生效的条款来抵消成本：即对第174条的修改。

从2022年开始，公司不再能够立即将研发费用列为支出； 相反，他们必须在五年到十五年内分期摊销。 这增加了税收负担，减少了现金流，尤其影响了那些依赖研发注销来减少应纳税收入的公司。

该文章将这一变化与Meta、微软、亚马逊、Salesforce等大型科技公司以及规模较小的公司发生的裁员联系起来。 尽管公司公开声称过度招聘和人工智能是原因，但该文章认为，税收变化起到了重要但未被充分重视的作用。 它迫使公司削减员工数量（最大的研发支出）以应对增加的税务责任。

这种影响超出了科技行业，影响了任何依赖内部开发和创新的公司。 该文章强调，这项旨在实现短期收入的政策，通过抑制研发投资，无意中损害了美国的竞争力和经济增长。 尽管两党都在努力废除这一变更，但对于许多已经失业的人来说，可能为时已晚。 该文章警告说，华盛顿正准备通过第二项特朗普税收法案，其中包含更多晦涩的条款，而分析师们才刚刚开始了解上一轮税改的实际影响。

---

## 9. 在光盘表面刻录可见图片的工具

**原文标题**: A tool for burning visible pictures on a compact disc surface

**原文链接**: [https://github.com/arduinocelentano/cdimage](https://github.com/arduinocelentano/cdimage)

本文档介绍了CDImage，一个将可见图片刻录到光盘表面的工具。该项目受到早期其他尝试的启发，并基于他们的工作，特别是在坐标转换方面。作者创建了一个带有视觉预览的GUI，但由于不同光盘品牌和类型之间的校准困难，最终在2008年放弃了该项目。

现在，作者重新启动并共享了该代码，以此致敬CD时代，将其移植到Qt6并修复了一些错误。构建CDImage需要Qt 6库。 还提供了一个Windows二进制版本，但未经彻底测试。

该工具的一个关键方面是精确的光盘几何形状，因为细微的变化会显著影响图像计算。该工具包含一些光盘型号的参数，并且可以手动输入，但校准很复杂且需要实验。该过程涉及生成一个大的音频轨道（约800MB），该轨道编码图像数据，然后可以使用标准的CD刻录软件以音频CD模式刻录。

本文档深入探讨了校准的挑战，将其呈现为一个需要专家反馈的双准则优化问题。作者讨论了现有的校准方法、它们的局限性以及使用寻道时间延迟或人工智能图像识别进行潜在改进的方法。作者还鼓励分享有关校准过程的新想法。最后，本文档指向了包括“红皮书”和其他项目的进一步阅读材料。

---

## 10. 如果有效，那就不是人工智能：人工智能创业公司的商业视角（1999）

**原文标题**: If it works, it's not AI: a commercial look at AI startups (1999)

**原文链接**: [https://dspace.mit.edu/handle/1721.1/80558](https://dspace.mit.edu/handle/1721.1/80558)

夏娃·M·菲利普斯1999年麻省理工学院论文《如果有效，就不是人工智能：人工智能创业公司的商业视角》探讨了人工智能创业公司的商业层面。标题本身暗示了一个中心主题：随着人工智能技术成熟并变得实际可行，它通常会失去其“人工智能”的标签，而被简单地视为标准软件或工程。

该论文可能探讨了人工智能创业公司如何在定义和营销其产品方面应对挑战，因为成功的AI解决方案经常被重新归类为其他东西。它可能考察了区分真正的人工智能创新与更传统的软件解决方案的难度，以及这如何影响资金、市场认知和整体商业策略。

该研究由帕特里克·温斯顿指导，可能深入研究了人工智能创业公司的真实案例和案例研究。参考文献的存在表明对人工智能及其商业应用的现有文献进行了彻底的探索。元数据证实该论文已提交给麻省理工学院电气工程与计算机科学系。可打印的完整版本意味着一项详细的研究，可能包括理论背景和实际例子。

---

## 11. 研究人员开发“透明纸”作为塑料替代品

**原文标题**: Researchers develop ‘transparent paper’ as alternative to plastics

**原文链接**: [https://japannews.yomiuri.co.jp/science-nature/technology/20250605-259501/](https://japannews.yomiuri.co.jp/science-nature/technology/20250605-259501/)

日本海洋研究开发机构（JAMSTEC）的研究人员开发出一种由纤维素制成的可生物降解的“透明纸”，有望取代塑料。这种纸由棉籽纤维提取的纤维素粉末制成，溶解在溴化锂水溶液中，加热成凝胶，塑形并干燥。所得材料强度与聚碳酸酯塑料相当，可用于制造杯子和吸管等物品。

透明度源于致密堆积的纳米级纤维，它们允许光线通过而不发生漫射，从而即使是厚片也能清晰可见。研究人员发现，该材料在海水中四个月内即可生物降解，即使在深海中也是如此，但由于微生物较少，降解过程在较深处较慢。

虽然纸质包装目前是塑料容器最常见的替代品，但消费者通常更喜欢看到产品。透明纸解决了这个问题，但需要工厂进行大规模生产。

据 JAMSTEC 称，生产这种透明纸的成本约为普通纸的三倍，但与塑料生产相比，可以减少约一半的二氧化碳排放。一位专家指出，与之前的透明纸不同，这种新材料已被证明可以在深海中生物降解。

---

## 12. 公平软件包管理器：去中心化的WordPress基础设施

**原文标题**: The FAIR Package Manager: Decentralized WordPress infrastructure

**原文链接**: [https://joost.blog/path-forward-for-wordpress/](https://joost.blog/path-forward-for-wordpress/)

本文宣布“FAIR”（联邦式独立代码库）计划，这是一项旨在分散WordPress基础设施并建立更负责任治理的新举措。FAIR源于对WordPress生态系统中中心化控制的担忧，是由Linux基金会支持的技术项目，旨在为WordPress插件和主题提供替代分发层。

该项目由多个并行工作推动产生，包括创建AspirePress（WordPress.org代码库的社区运营镜像）以及核心贡献者倡导治理改革的公开信。FAIR利用Composer和Linux软件包管理器等现有工具，创建了一个用户友好的WordPress安装管理系统。

FAIR的主要功能包括去中心化的软件包管理系统、支持联邦的镜像、对商业插件的支持以及密码签名。它旨在与当前的WordPress核心兼容，同时消除中心化造成的瓶颈，并提供一个独立管理的系统。

FAIR并非旨在分叉WordPress或创建一个独立的平台，而是提供一种新的分发途径。用户仍然可以从WordPress.org安装WordPress。但是，FAIR提供了一个选项，可以更好地控制插件交付并建立一个去中心化的系统。作者强调，FAIR是对WordPress更好的基础设施和治理的贡献，并邀请其他人加入这项工作。

---

## 13. Pornhub离开法国后，该VPN在30分钟内注册量激增1000%

**原文标题**: After Pornhub left France, this VPN saw a 1,000% surge in signups in 30 minutes

**原文链接**: [https://mashable.com/article/proton-vpn-pornhub-france](https://mashable.com/article/proton-vpn-pornhub-france)

鉴于一项新的年龄验证法，Pornhub决定封锁在法国的访问。此后，Proton VPN报告称，仅仅30分钟内注册量激增1000%。这一增长幅度甚至超过了TikTok在美国面临潜在禁令时所见的增幅。

Pornhub宁愿退出其第二大市场法国，也不愿遵守法国新的年龄验证法，该法律要求使用面部识别或政府身份证等方法进行年龄验证。虽然VPN通常用于保护在线隐私和规避审查，但此次事件突显了它们在绕过地域限制以访问内容方面的用途。

Proton VPN承认了这种用途，并表示虽然促进对色情内容的访问并非其最初的意图，但VPN可以被用于此类目的。该公司还对年龄验证法表示担忧，强调它们会影响到每个人，并可能导致创建易被滥用的个人身份数据库。他们建议在个人设备上进行内容控制，认为这是更有效且侵犯隐私较少的解决方案。

Proton VPN是一家总部位于瑞士的公司，成立于2014年，提供一系列以隐私为中心的服务。其VPN服务于2017年推出，拥有庞大的网络，在117个国家/地区拥有超过13,000台服务器。该服务曾获得Mashable Choice Award。

---

## 14. 电子前哨基金会致函联邦贸易委员会：数字千年版权法第1201条制造反竞争监管壁垒

**原文标题**: EFF to the FTC: DMCA Section 1201 Creates Anti-Competitive Regulatory Barriers

**原文链接**: [https://www.eff.org/deeplinks/2025/06/eff-files-comments-ftc-regarding-reducing-anti-competitive-regulatory-barriers](https://www.eff.org/deeplinks/2025/06/eff-files-comments-ftc-regarding-reducing-anti-competitive-regulatory-barriers)

电子前哨基金会 (EFF) 与作家联盟合作，已敦促联邦贸易委员会 (FTC) 承认《数字千年版权法案》(DMCA) 第 1201 条及其三年一次的豁免程序属于反竞争法规。EFF 认为，旨在防止规避受版权保护作品技术保护措施的第 1201 条，实际上通过阻止出于研究、教育和维修等合法目的访问内容，从而限制了合理使用。

虽然国会设立了由国会图书馆管理的三年一次的豁免程序作为安全阀，但 EFF 认为该程序过于繁琐和耗时，反而成为了一个瓶颈。这阻碍了个人和组织行使其合理使用权，最终阻碍了版权法旨在服务的公共利益。

EFF 承认联邦贸易委员会对国会和国会图书馆的直接控制有限，但希望联邦贸易委员会的调查能够突出第 1201 条的负面影响以及豁免程序的无效性。EFF 敦促联邦贸易委员会建议国会废除或改革第 1201 条。如果做不到这一点，EFF 倡导对国会图书馆三年一次的规则制定程序进行重大修订，从 2026 年的审查开始，以确保版权法支持而非抑制竞争和独立创新。

---

## 15. 我们如何将 GitLab 仓库备份时间从 48 小时缩短至 41 分钟

**原文标题**: How we decreased GitLab repo backup times from 48 hours to 41 minutes

**原文链接**: [https://about.gitlab.com/blog/2025/06/05/how-we-decreased-gitlab-repo-backup-times-from-48-hours-to-41-minutes/](https://about.gitlab.com/blog/2025/06/05/how-we-decreased-gitlab-repo-backup-times-from-48-hours-to-41-minutes/)

GitLab通过解决与引用计数相关的Git扩展性问题，将代码仓库备份时间从48小时大幅缩短至41分钟。问题源于一个已有15年历史的Git函数 `object_array_remove_duplicates()`，该函数在`git bundle create`过程中使用，复杂度为O(N²)。随着代码仓库积累的引用越来越多，该函数导致处理时间呈指数级增长。

GitLab使用火焰图识别出瓶颈，并贡献了一个上游修复方案，用映射数据结构替换了嵌套循环，确保只保留每个引用的单个副本进行处理。这种算法上的改变使基准测试性能提高了6倍。

备份时间的改进为GitLab客户带来了切实的利益，包括：

*   **转变备份策略：** 使全面的夜间计划成为可能，而不会影响开发工作流程。
*   **增强业务连续性：** 最大限度地减少恢复点目标（RPO），降低灾难情况下的业务风险。
*   **降低运营成本：** 降低服务器资源消耗和维护窗口，从而降低计算成本。
*   **面向未来的基础设施：** 允许备份策略随着不断增长的代码库无缝扩展。

自18.0版本起，所有GitLab客户（无论许可证级别）均可使用此修复程序。GitLab强调其对可扩展Git基础设施的持续承诺以及与更广泛的Git社区的合作。

---

## 16. 克服拖延症

**原文标题**: Getting Past Procrastination

**原文链接**: [https://spectrum.ieee.org/getting-past-procastination](https://spectrum.ieee.org/getting-past-procastination)

文章《克服拖延症》由Taro创始人Rahul Pandey撰写，Taro是一个面向科技专业人士的职业平台。文章可能提供了旨在帮助读者克服拖延症并提高工作效率的策略和系统。鉴于Pandey在科技行业的背景，该建议可能对技术岗位的人员尤其有帮助。

主要内容可能包括制定结构和常规以尽量减少拖延症的可行性建议，例如设定明确的目标、将大型任务分解为更小更易于管理的步骤，以及设定截止日期。文章可能强调持续高效的重要性，而非偶尔的爆发式工作。因为这是一篇短文（阅读时间3分钟），所以它可能是一个有针对性且简洁的指南，侧重于可以立即实施的实用技巧。

---

## 17. 烟囱为什么要那么高？

**原文标题**: Why are smokestacks so tall?

**原文链接**: [https://practical.engineering/blog/2025/6/3/why-are-smokestacks-so-tall](https://practical.engineering/blog/2025/6/3/why-are-smokestacks-so-tall)

为什么烟囱这么高？

本文探讨了烟囱背后的工程原理及其在空气污染管理中的作用。文章首先强调，虽然完全消除排放是理想的，但目前尚不可行，因此管理其影响至关重要。

烟囱的核心功能是将污染物扩散到局部安全浓度水平。虽然主要的排放控制措施可以去除污染物，但烟囱有助于扩散。烟囱的高度利用了“烟囱效应”：内部较热、密度较低的空气上升，产生压力差，从而驱动向上气流。这使得污染物能够到达更高的高度，以便更好地扩散。增加烟囱高度和温度有助于这种效应，但热力学和其他实际限制，如气体冷却和摩擦阻力，会降低更高烟囱高度带来的益处。

早期烟囱旨在增加气流以实现高效燃烧，而现在的环境法规则优先考虑空气质量。烟羽行为复杂，受风、大气稳定性和周围建筑物等因素的影响。大气稳定性由绝热递减率与实际环境的比较决定，它会显著影响烟羽形状，导致锥形、环状、扇形、滞留、抬升和熏蒸烟羽。理解和预测烟羽行为需要考虑平流（风力输送）和扩散（湍流扩散），需要复杂的模型来确保符合空气污染物监管标准。

---

## 18. 一年资助的FreeBSD开发

**原文标题**: A year of funded FreeBSD development

**原文链接**: [https://www.daemonology.net/blog/2025-06-06-A-year-of-funded-FreeBSD.html](https://www.daemonology.net/blog/2025-06-06-A-year-of-funded-FreeBSD.html)

本文详细介绍了作者在亚马逊通过 GitHub Sponsors 资助下，为期一年的 FreeBSD 开发工作，主要集中在 FreeBSD 版本的发布以及对 Amazon EC2 平台的增强。该赞助原计划为每月 40 小时，但实际上达到了每月约 50 小时，这些时间分配在 EC2 相关的任务、FreeBSD 版本管理以及相关的工程工作上。

主要成就包括管理了四个 FreeBSD 版本（13.4、14.2、13.5 和 14.3），开发了一个用于在 AWS Graviton 实例上实现优雅关机的“电源驱动程序”，并解决了各种 EC2 实例类型上的许多热插拔问题。 这些修复程序需要 ACPI quirks 来解决 EC2 的错误以及 FreeBSD 和 EC2 固件之间的不一致性。

除了亚马逊的优先事项之外，作者还解决了 EC2 实例上的启动时间过长的问题。这包括增加根磁盘大小，改进 Graviton 2 实例上的内核熵种子，以及解决 `makefs` 和 ZFS 之间的交互导致 ZFS 镜像启动缓慢的问题。`aws-ec2-imdsv2-get` 端口中的 IPv6 支持问题被迅速发现并修复，从而缩短了启动时间。最后，添加了“小型” AMI，从而显着减少了磁盘空间的使用。还创建了一个测试脚本来自动化热插拔测试，以确保未来的兼容性。

---

## 19. 为什么从R转到Pandas会觉得笨拙 (2024)

**原文标题**: Why Pandas feels clunky when coming from R (2024)

**原文链接**: [https://www.sumsar.net/blog/pandas-feels-clunky-when-coming-from-r/](https://www.sumsar.net/blog/pandas-feels-clunky-when-coming-from-r/)

一位资深的R用户Rasmus Bååth讨论了为什么即使在每天使用五年后，Python中的pandas与R中的tidyverse相比仍然感觉笨拙。他认为向那些视pandas为出色的数据科学工具的“Python人”解释这些挫折感是很困难的。

文章通过一个简单的购买数据集的逐步分析来说明这些差异。在R中，分析简洁明了，可以使用tidyverse直观的管道进行增量开发。相比之下，pandas的实现需要更冗长的代码，处理诸如列名、索引操作以及分组和未分组数据的不同方法行为等问题。

作者强调了以下具体痛点：

*   **API不一致：** 方法名称和参数令人困惑（例如，`.filter()` 不会过滤值）。
*   **行为不同：** 分组和未分组的DataFrames具有不同的可用方法，即使方法名称相同。
*   **缺少便捷函数：** tidyverse中的简单操作在pandas中需要更复杂的代码。
*   **索引操作：** Pandas经常将列移动到索引中，需要经常使用`.reset_index()`。

Bååth总结说，虽然pandas是一个强大的工具，但这些不一致和缺乏便捷函数会导致习惯于R的tidyverse的用户体验笨拙。他鼓励“Python人”对过渡到pandas的R用户表示同情，并承认这些API问题在更大、更真实的项目中仍然存在。

---

## 20. 我所理解的梯度噪声分享

**原文标题**: Sharing everything I could understand about gradient noise

**原文链接**: [https://blog.pkh.me/p/42-sharing-everything-i-could-understand-about-gradient-noise.html](https://blog.pkh.me/p/42-sharing-everything-i-could-understand-about-gradient-noise.html)

本文全面地从GPU角度解释了梯度噪声，从一维版本入手，逐步深入到二维和三维的实现。它强调对底层数学原理和实际实现细节的理解，这些内容在其他资源中往往被忽视。

作者首先解释了确定性的、基于坐标的伪随机系统的必要性，特别是整数哈希，以便为每个晶格点生成随机值。他们重点介绍了Chris Wellons的“lowbias32”哈希函数及其在GLSL中针对归一化浮点数的适配。

文章随后探讨了一维值噪声的创建，使用线性和五次插值技术。它过渡到一维梯度噪声，将随机值解释为影响信号的斜率或角度。扩展到二维和三维后，解释涵盖了梯度向量和晶格角向量之间点积的计算，利用双线性插值和三线性插值，以及用于生成均匀分布在圆（二维）和球体（三维）上的随机单位向量的正确方法。

最后，文章讨论了分形布朗运动（fBm），它涉及对多个倍频程的噪声进行求和，以创建更精细的模式。最后，它强调了导数（变化率）在各种应用中的实用性，例如生成用于光照的法线以及模拟地形生成中的侵蚀。所有概念均通过GLSL代码片段和视觉示例进行说明，强调基于GPU的实际实现。

---

## 21. 思考的错觉：理解推理LLM的局限性 [pdf]

**原文标题**: The Illusion of Thinking: Understanding the Limitations of Reasoning LLMs [pdf]

**原文链接**: [https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf](https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf)

名为“思考的幻觉：理解推理型LLM的局限性”的这份文档，是一个PDF文件，尽管其内容主要是机器可读的代码和压缩文本。从标题和可辨认的文本片段中，我们可以推断出其主题。该文章可能讨论大型语言模型（LLM）在真正“思考”或推理方面的局限性。

PDF结构元素的存在表明该文档包含页面布局、大纲、注释以及潜在的交互元素。然而，解压缩文本的乱码性质表明其内容是专有或专业的，无法使用现成的工具轻松解析。

根据标题，可以预见作者将考察和批判LLM的能力，论证它们可能模拟了智能和推理，但并未真正拥有这些特质。该文档可能分析LLM如何处理信息、识别模式、生成文本和解决问题，同时指出与人类认知过程相比存在的不足。它可能会讨论诸如缺乏常识、难以进行抽象推理、容易受到偏见影响以及无法真正理解意义和上下文等问题。总而言之，该研究可能警告不要高估LLM的能力，并倡导对它们的局限性进行更细致的理解。

---

## 22. 阿西莫夫与无聊之疾 (1964)

**原文标题**: Asimov and the Disease of Boredom (1964)

**原文链接**: [https://archive.nytimes.com/www.nytimes.com/books/97/03/23/lifetimes/asi-v-fair.html](https://archive.nytimes.com/www.nytimes.com/books/97/03/23/lifetimes/asi-v-fair.html)

在1964年的文章中，艾萨克·阿西莫夫受纽约世界博览会启发，设想了2014年的世界。他预见到一个科技进步的未来，包括电致发光住宅、地下城市和由自动化厨房单元制作的“自动餐”。机器人虽然不普遍，但将存在，执行家务。电力将由放射性同位素电池和核聚变发电厂产生，沙漠地区将建有太阳能发电站。

交通运输将会发展，气垫车辆将取代汽车，城市地区将出现自动人行道。通讯将是即时和可视的，由卫星促进，允许直接拨打地球上任何地方的电话，包括月球殖民地。

然而，阿西莫夫也承认挑战。人口增长是一个主要问题，他预测全球人口将达到65亿，并且波士顿到华盛顿之间将出现高度城市化的走廊。他预计水下殖民地的出现和基于藻类的食物来源的发展，以应对资源限制。节育将受到大力推广，但可能效果不足。

自动化将导致一个机器照看者的社会，需要教育向计算机技术转型。阿西莫夫警告说，由于缺乏有意义的工作，将会出现普遍的厌倦感，使得精神病学成为一个至关重要的医学领域。他总结说，从事创造性事业的人将是这个未来世界的“真正精英”。

---

## 23. 逆向工程 Cursor 的 LLM 客户端

**原文标题**: Reverse Engineering Cursor's LLM Client

**原文链接**: [https://www.tensorzero.com/blog/reverse-engineering-cursors-llm-client/](https://www.tensorzero.com/blog/reverse-engineering-cursors-llm-client/)

本文详细介绍了作者如何使用他们的开源框架 TensorZero 来逆向工程 Cursor 的 LLM 客户端，从而观察、分析和实验 Cursor 发出的 LLM 请求。他们的目的是深入了解 Cursor 的内部运作，并有可能针对个体用户对其进行优化。

该过程涉及将 TensorZero 设置为 Cursor 和 LLM 提供商之间的自托管代理。由于 Cursor 最初无法连接到 localhost 以及随后的 CORS 问题，这变得很复杂，这些问题通过使用 Ngrok、Nginx 和特定的 Nginx 配置得以克服。

成功后，他们获得了对 Cursor 提示的完全可观察性，包括系统提示和用户提示。他们发现 Cursor 使用相对较短的系统提示来指导 LLM，并揭示了一个明确的层次结构，其中使用“智能较低”的模型来应用主 LLM 建议的代码编辑。

作者现在正在对不同的 LLM（Claude、GPT-4、o4 Mini 和 Gemini）进行 A/B 测试，以了解哪一个在 Cursor 环境中表现最佳。他们报告了稳定的性能，并且没有明显的延迟。文章最后预告了后续文章，该文章将详细介绍他们评估实际使用情况并根据个人用户模式优化模型的方法，包括使用 git hooks 和 tree-sitter 的技术。目标是演示 TensorZero 如何通过个性化优化改进预构建的 LLM 代理。

---

## 24. 中世纪非洲人用玻璃提纯黄金的独特工艺 (2019)

**原文标题**: Medieval Africans had a unique process for purifying gold with glass (2019)

**原文链接**: [https://www.atlasobscura.com/articles/medieval-african-gold](https://www.atlasobscura.com/articles/medieval-african-gold)

本文探讨了中世纪西非，特别是约11世纪马里Tadmekka地区使用的一种独特的黄金提纯工艺。考古学家萨姆·尼克松发现的铸币模具碎片和玻璃碎片引发了对这项创新技术的调查。

与欧洲使用铅的灰吹法不同，中世纪的非洲人将金矿石与回收的玻璃混合。金的性质稳定，不会溶解在熔融的玻璃中，而矿石中的杂质则会溶解。这使得在熔炼过程后可以提取出相对纯净的黄金残留物。

马克·沃尔顿及其在艺术科学研究中心的团队使用现代材料重现了这一过程，用当地资源替代了马里人可用的资源。他们将金粉与密歇根湖的沙子和合成玻璃混合，加热混合物以溶解沙子中的矿物质，从而留下提纯的黄金。

重现的结果证实了中世纪马里黄金提纯技术的精妙和独创性，突显了他们对黄金和玻璃性能的理解。回收玻璃的使用也表明了工匠们在繁华的贸易中心利用现有资源的勤劳和创造力。

---

## 25. Mojo 中的高效矩阵转置

**原文标题**: Highly efficient matrix transpose in Mojo

**原文链接**: [https://veitner.bearblog.dev/highly-efficient-matrix-transpose-in-mojo/](https://veitner.bearblog.dev/highly-efficient-matrix-transpose-in-mojo/)

这篇博文详细介绍了如何在Mojo中实现高效的矩阵转置内核，达到与手工优化的CUDA相媲美的性能。作者专注于利用Hopper架构的功能，特别是使用张量内存加速器 (TMA)。

文章首先介绍了一种使用TMA的简单转置实现，实现了1056.08 GB/s的带宽，已经超过了可比的CUDA实现 (875.46 GB/s)。最初的改进归功于在Mojo中使用PTX API进行TMA传输。

接下来，作者介绍了混洗（swizzling）作为一种优化技术。混洗涉及调整内存访问模式以提高合并和内存利用率。在Mojo中实现混洗需要调整TMA描述符并在内核中使用混洗索引。这种方法在Mojo中实现了1437.55 GB/s的带宽，而CUDA中为1251.76 GB/s。

最大的性能提升来自线程粗化（每个线程处理一批列）。通过让每个线程处理多个列，内核实现了2775.49 GB/s的带宽，与在同一硬件上使用高度优化的CUDA内核实现的2771.35 GB/s非常接近。 这突显了Mojo实现类似CUDA性能的能力。

文章总结说，Mojo可用于高性能GPU计算。完整的代码可在作者的GitHub上找到。

---

## 26. 程序员对航空的常见误解

**原文标题**: Falsehoods programmers believe about aviation

**原文链接**: [https://flightaware.engineering/falsehoods-programmers-believe-about-aviation/](https://flightaware.engineering/falsehoods-programmers-believe-about-aviation/)

程序员关于航空的常见谬误

---

## 27. 桑迪亚启动类脑无存储超级计算机

**原文标题**: Sandia turns on brain-like storage-free supercomputer

**原文链接**: [https://blocksandfiles.com/2025/06/06/sandia-turns-on-brain-like-storage-free-supercomputer/](https://blocksandfiles.com/2025/06/06/sandia-turns-on-brain-like-storage-free-supercomputer/)

桑迪亚国家实验室推出SpiNNaker 2超级计算机，一种“大脑启发”系统，放弃GPU和内部存储，采用独特的神经形态架构。该系统与SpiNNcloud合作开发，旨在模拟1.5亿至1.8亿个神经元，使其跻身全球顶级神经形态平台之列。

SpiNNaker 2架构最初由Arm先驱Steve Furber构思，采用高度并行处理，每个服务器板配备48个SpiNNaker 2芯片，每个芯片包含152个核心和专用加速器。每个芯片具有20MB的SRAM，每个板具有96GB的外部LPDDR4外部存储器。该机器实现了高速芯片间通信，并利用其庞大的内存容量消除了对集中式存储的需求。

桑迪亚的初始设置包括一个24板、175,000核的系统，该系统与现有的HPC基础设施集成，在没有操作系统或磁盘的情况下运行。该系统的速度源于其将数据保存在SRAM和DRAM中的能力。SpiNNcloud表示，其最大系统拥有超过1050万个核心。

据SpiNNcloud称，神经形态设计比GPU系统具有更高的功率效率优势，使其适用于国家安全等计算密集型应用。SpiNNcloud首席执行官Hector A. Gonzalez设想SpiNNaker 2能够应对下一代国防挑战及其他领域。

---

## 28. 网络开发受虐指南

**原文标题**: A masochist's guide to web development

**原文链接**: [https://sebastiano.tronto.net/blog/2025-06-06-webdev/](https://sebastiano.tronto.net/blog/2025-06-06-webdev/)

本文指导 C/C++ 开发者使用 Emscripten 将他们的代码移植到 WebAssembly (WASM) 用于 Web 应用程序。 它从一个基本的 "Hello, web!" 示例开始，演示了如何将 C 代码编译成 WASM 并在浏览器中运行。

然后，作者介绍了构建一个 C 库以在 JavaScript 中使用，涵盖了使用 `-sEXPORTED_FUNCTIONS` 导出函数以及使用 `onRuntimeInitialized` 处理异步运行时初始化的基本步骤。 克服最初的陷阱后，成功构建并执行了一个简单的乘法库。

本文包含两个间奏：第一个关于 WebAssembly 技术，它的起源、基于文本的表示以及 WASM64 的未来发展；第二个关于 JavaScript 和 DOM（文档对象模型），解释了如何使用 `document.getElementById()` 和事件监听器等函数从 JavaScript 与 HTML 元素交互。 演示了一个动态按钮，以及它在事件监听器下的外观。

本指南最终创建了一个基本的 HTML 页面，其中包含 JavaScript 来与最终的 WASM 库进行交互。 HTML 代码包括输入字段和一个按钮。 目前 JS 代码使用的是 * 运算符。

---

## 29. 展示一下：AI游戏动画精灵生成器

**原文标题**: Show HN: AI game animation sprite generator

**原文链接**: [https://www.godmodeai.cloud/ai-sprite-generator](https://www.godmodeai.cloud/ai-sprite-generator)

上帝模式AI：一款强大的AI精灵生成器，旨在帮助游戏开发者从图像或文本描述中创建专业的游戏动画精灵。用户上传角色设计，AI即可生成可用于生产的动画，包含跳跃、跑步、拳击和特殊攻击等各种动作，并配有透明背景、中心偏移和边界框。

该工具面向独立开发者、游戏工作室和艺术家，通过自动化精灵创建来节省成本和时间。它支持从像素艺术到动漫的多种风格。一项关键的新功能是能够使用最少五个动画样本来训练自定义动作模型，允许用户为独特的游戏机制创建个性化动画。这些自定义模型可以保持私有或公开分享以获取收入。

该服务采用积分系统，一个积分等于一个精灵生成。用户可以购买积分包，积分永不过期。提供多个预设积分包。该平台提供包含初始积分的免费层级，还提供免费的模型训练，包含标准和自定义动作选项。

对于企业和游戏工作室，上帝模式AI提供定制AI解决方案，包括量身定制的AI模型和专门的支持，以加速游戏开发并显著提高生产力。常见问题解答部分解决了常见的用户问题，例如支持的文件格式、输出格式、商业使用权和生成时间。

---

## 30. Odyc.js – 一个用于叙事游戏的微型 JavaScript 库

**原文标题**: Odyc.js – A tiny JavaScript library for narrative games

**原文链接**: [https://odyc.dev](https://odyc.dev)

Odyc.js 是一个小型 JavaScript 库，旨在简化叙事视频游戏的创作。 它的目标是让用户能够编写游戏代码，即使没有编程经验。 该库的网站展示了用 Odyc.js 创建的游戏作品集，并提供学习资源来帮助用户入门。 本质上，Odyc.js 定位为构建叙事驱动型游戏的一种易用工具，强调易用性和非程序员的可访问性。

---

## 31. Odyc.js – 用于叙事游戏的微型JavaScript库

**原文标题**: Odyc.js – A tiny JavaScript library for narrative games

**原文链接**: [https://odyc.dev](https://odyc.dev)

Odyc.js 是一个小型 JavaScript 库，旨在简化叙事视频游戏的创作，甚至适用于没有编程经验的个人。该库专注于提高游戏开发的可访问性，允许用户在没有广泛编程知识的情况下“编写视频游戏”。提供的文本强调了 Odyc.js 作为游戏开发工具的核心目的，并鼓励用户探索其功能，包括学习资源和一个展示使用该库创作的游戏的画廊。

---

## 32. 文德尔施泰因7-X 创下新的聚变记录

**原文标题**: Wendelstein 7-X sets new fusion record

**原文链接**: [https://www.heise.de/en/news/Wendelstein-7-X-sets-new-fusion-record-10422955.html](https://www.heise.de/en/news/Wendelstein-7-X-sets-new-fusion-record-10422955.html)

德国格赖夫斯瓦尔德的仿星器聚变装置Wendelstein 7-X (W7-X) 在聚变能量产生方面取得新纪录。在最近的实验中，W7-X 维持了一个温度超过1.35亿摄氏度（约2.43亿华氏度）的等离子体长达重要的八分钟，产生了1.3吉焦耳的能量转换。这代表了对先前结果的显著改进。

这一成功归功于加热和控制系统的改进，使等离子体能够更稳定和更持久地约束。长时间维持稳定、高温的等离子体对于开发具有商业可行性的聚变发电厂至关重要。

虽然这是一项重大成就，但W7-X并非旨在产生比消耗更多的能量。相反，它作为一个研究装置，旨在证明仿星器概念的可行性，与托卡马克相比，仿星器在等离子体稳定性方面具有内在优势。来自W7-X的结果正在为未来聚变反应堆的设计提供信息。该团队目前正在努力实现更长、更强大的放电，目标是展示未来的连续运行。

---

## 33. 人工智能应用时代“工作”的意义

**原文标题**: What “working” means in the era of AI apps

**原文链接**: [https://a16z.com/revenue-benchmarks-ai-apps/](https://a16z.com/revenue-benchmarks-ai-apps/)

Andreessen Horowitz 文章《人工智能应用时代“工作”的意义》指出，人工智能已显著加速初创公司的增长，企业和消费者公司实现收入里程碑的速度都快于人工智能时代之前。

主要发现包括：

*   **增长加速：** 企业人工智能公司中位数在第一年达到超过 200 万美元的年度经常性收入 (ARR)，而消费者公司则达到 420 万美元的年度经常性收入，并在货币化后的 8-9 个月内完成 A 轮融资。这种快速增长要求寻求风险投资的初创公司拥有强大的增长速度故事。
*   **差距扩大：** 优秀公司和卓越公司之间的差距正在扩大，顶级公司在第一年表现出持续增长。然而，诸如使用率和留存率之类的传统指标对于后期融资仍然至关重要。
*   **消费者公司是收入驱动力：** B2C 人工智能公司正在产生可观的收入，这得益于模型训练的资金和新模型发布后的收入激增。虽然转化率可能较低，但用户留存率与人工智能之前的企业相当。

作者总结说，初创公司发展速度更快，企业和消费者都愿意为新的人工智能产品付费，这为应用层软件公司创造了一个有利的环境。他们强调，迭代速度和产品开发正在成为一种竞争优势（护城河）。

---

## 34. 打开文件过多

**原文标题**: Too Many Open Files

**原文链接**: [https://mattrighetti.com/2025/06/04/too-many-files-open](https://mattrighetti.com/2025/06/04/too-many-files-open)

解决Rust测试中“打开文件过多”错误的经验

---

## 35. 关于电磁脉冲武器你需要知道的

**原文标题**: What you need to know about EMP weapons

**原文链接**: [https://www.aardvark.co.nz/daily/2025/0606.shtml](https://www.aardvark.co.nz/daily/2025/0606.shtml)

《食蚁兽日报》的这篇文章讨论了电磁脉冲（EMP）武器的威胁，特别是高空核爆炸产生的电磁脉冲。作者解释说，电磁脉冲是由伽马射线与地球大气层和磁场相互作用产生的，会对电子设备造成广泛破坏。

这篇文章将电磁脉冲分为三个阶段：E1，一种快速、高频的脉冲，会烧毁敏感设备；E2，一种持续时间更长、频率更低的阶段；以及E3，一种低频阶段，会损坏电力线和其他长导体。

防御电磁脉冲的主要方法是法拉第笼，一种能够转移电磁脉冲能量的导电外壳。文章强调了完全封闭的重要性，即导电层中不能有间隙，并且设备要与屏蔽材料绝缘。

一种基本的、临时的保护方法是将电子设备包裹在塑料薄膜和铝箔层中。作者还指出，像真空管收音机和没有大量电子设备的汽车等老式技术，可能比现代设备更能抵抗电磁脉冲。总的来说，这篇文章旨在告知读者电磁脉冲的潜在危险和基本的缓解策略。

---

## 36. Smalltalk、Haskell和Lisp

**原文标题**: Smalltalk, Haskell and Lisp

**原文链接**: [https://storytotell.org/smalltalk-haskell-and-lisp](https://storytotell.org/smalltalk-haskell-and-lisp)

本文详细介绍了作者使用Haskell、Common Lisp和Smalltalk编写一个小型程序的经验，该程序最初是为NRAO的求职者用Java编写的。其目标是巩固现有的编程知识，但作者意外地发现，除了实用性之外，还对Haskell产生了强烈的偏好。

作者对比了用每种语言编写的代码片段，认为Haskell版本感觉更像是一组可组合的操作，而Smalltalk和Lisp则感觉像是捏造出来的。对Lisp的主要不喜欢之处在于，它感觉像是“欺骗”语言，而不是直接表达意图。作者欣赏Haskell的语法以及将问题分解为小的、易于理解的部分的能力。

作者反思了他们对编译器/解释器的依赖，承认缺乏强大的预执行代码分析技能，以及与Lisp和Smalltalk相比，Haskell如何帮助他们更早地避免开发过程中出现荒谬的编码实践。

作者总结说，他们对Haskell的热爱可能是不理性的，承认它的局限性和潜在的教学困难。他们还质疑为什么像Lisp和Smalltalk这样的语言缺乏Haskell强大的类型系统，并反思了拥抱代码进化和失败与努力实现编译时正确性之间的挑战。他们表示对Autotest和TDD作为潜在的未来解决方案感兴趣。最终，编程是一段旅程，作者拥抱持续学习带来的不适。

---

## 37. Meta：关闭你侵入式的AI探索内容

**原文标题**: Meta: Shut down your invasive AI Discover feed

**原文链接**: [https://www.mozillafoundation.org/en/campaigns/meta-shut-down-your-invasive-ai-discover-feed-now/](https://www.mozillafoundation.org/en/campaigns/meta-shut-down-your-invasive-ai-discover-feed-now/)

Mozilla 要求 Meta 关闭其“发现”AI 信息流，因担忧私人 AI 聊天在未经用户明确同意或知情的情况下被公开。该组织认为 Meta 正在模糊私人和公共对话之间的界限，危害用户隐私。

Mozilla 呼吁 Meta 采取以下关键行动：

* 关闭“发现”信息流，直到实施稳健的隐私保护措施。
* 默认情况下将所有 AI 互动设置为私密，公开分享需获得明确、知情的同意。
* 公开有多少用户在不知情的情况下分享了私人信息。
* 创建一个跨所有 Meta 平台的通用退出系统，以防止数据被用于 AI 训练。
* 通知可能已被公开对话的用户，并允许他们永久删除其内容。

核心问题在于缺乏明确和知情的同意，导致用户可能在不知情的情况下分享私人信息。 Mozilla 认为用户有权知道他们何时进行公开交流，并倡导采取明确的选择加入措施以确保隐私。该组织鼓励用户签署请愿书，要求 Meta 解决这些问题。

---

## 38. Show HN: 空气实验室 – 一款便携式开源空气质量测量设备

**原文标题**: Show HN: Air Lab – A portable and open air quality measuring device

**原文链接**: [https://networkedartifacts.com/airlab/simulator](https://networkedartifacts.com/airlab/simulator)

此“Show HN”帖子介绍了一款名为“Air Lab”的便携式开源空气质量测量设备。标题突出了其主要特点：便携性和开源设计。虽然背景信息有限，但我们可以推断出Air Lab允许用户随时随地测量和分析空气质量，并可能由于其开源特性而自定义设备或其软件。“Air Lab Simulator”的包含表明可能存在一个软件组件，或许允许用户模拟空气质量状况或分析设备收集的数据。该设备和模拟器组合可能旨在为空气质量监测、教育和潜在的研究目的提供一个全面的解决方案。

---

## 39. 喀迈拉 – 非GNU/Linux的Linux

**原文标题**: Chimera – a Linux that isn't GNU/Linux

**原文链接**: [https://www.theregister.com/2023/02/13/chimera_non_gnu_linux/](https://www.theregister.com/2023/02/13/chimera_non_gnu_linux/)

本文介绍了Chimera Linux，一个旨在完全摆脱GNU和systemd的新Linux发行版。Chimera由Daniel "q66" Kolesa开发，使用LLVM、musl C库（如Alpine Linux）、Dinit init系统以及FreeBSD的用户空间组件构建。

Chimera Linux致力于为Linux带来设计上的清晰性，与典型发行版中数千个独立开发的组件相比，它提供更集成的操作系统体验。虽然仍然基于Linux且二进制兼容，但它本质上颠覆了Debian GNU/kFreeBSD，将源自FreeBSD的用户空间置于Linux内核之上。其中的关键部分是用名为chimerautils的fork版本替换GNU coreutils。

该发行版采用Alpine Package Keeper (apk) 进行包管理，使用APK版本3和自定义包格式以提高安全性。尽管处于早期阶段，Chimera已经支持ppc64le、x86_64、aarch64和RISC-V_64架构。它提供GNOME on Wayland作为其初始桌面环境，选择GNOME是因为其复杂性以及移植带来的挑战。

Chimera优先考虑使用LLVM和Clang特性进行强化和错误检查。除了简单地移除systemd之外，它还旨在用Turnstile会话跟踪器等工具来重现其功能。该项目虽然雄心勃勃且不完整（目前缺少安装程序），但旨在成为一个可行的替代系统，具有更清洁、更好的核心功能实现。

---

## 40. 管理你的Shell历史记录

**原文标题**: Curate your shell history

**原文链接**: [https://esham.io/2025/05/shell-history](https://esham.io/2025/05/shell-history)

本文探讨了关于 shell 历史管理的不同哲学，将极简主义方法与作者自身的“shell 历史最大化”倾向进行了对比。文章首先强调了 Simon Tatham 完全禁用 shell 历史文件的做法，他提倡有意识地将有价值的命令保存到其他地方，以避免因失败的尝试和意外的回调而导致混乱。

另一方面，作者更喜欢大型 shell 历史，但也承认了积累无用命令（如拼写错误和不正确的尝试）的问题。为了解决这个问题，作者介绍了一个名为 `smite` 的 zsh 函数，该函数使用 `fzf` 提供了一个交互式界面，用于浏览和删除不需要的历史条目。默认情况下，`smite` 对当前会话的历史记录进行操作，但 `-a` 选项允许修剪整个历史记录文件。选定的命令将从历史记录文件中永久删除。

作者承认 `smite` 在处理多行命令方面的局限性，但希望这个概念能促使读者考虑他们自己的 shell 历史习惯，并探索改进它们的方法。即使特定的 zsh 代码没有用，本文也提倡积极地整理 shell 历史，以删除“杂草”（不需要的命令），并使其成为更有价值的资源。

---

## 41. 主力LLM：为何开源模型在批量任务中胜过闭源模型

**原文标题**: Workhorse LLMs: Why Open Source Models Dominate Closed Source for Batch Tasks

**原文链接**: [https://sutro.sh/blog/workhorse-llms-why-open-source-models-win-for-batch-tasks](https://sutro.sh/blog/workhorse-llms-why-open-source-models-win-for-batch-tasks)

Sutro Components博客文章认为，对于诸如分类、摘要和数据提取等“主力”批量任务，开源LLM通常优于闭源替代方案。虽然闭源模型在尖端智能方面领先，但开源模型在这些常见业务应用中提供了更好的性能和成本效益。

文章使用人工智能分析指数和每token成本数据比较了性能和成本，强调开源模型可以提供2倍-10倍的更高性价比，尤其是在使用像Sutro这样的批量推理提供商时。例如，Qwen3 4B显示出与GPT-4o-mini等模型相当或更好的性能，但成本显著降低。

该帖子还提供了一个转换图表，以帮助用户为流行的闭源模型选择合适的开源替代方案，并估算潜在的成本节省。虽然像Gemini 2.5 Flash这样的一些闭源模型提供具有竞争力的定价，但开源替代方案通常在整体成本效益方面胜出。结论强调，关注特定任务的成本与性能比，揭示了开源LLM在主力类别中的主导地位，尤其是在利用批量处理时。最后，它鼓励读者向Sutro寻求咨询，以优化他们的LLM战略。

---

## 42. C轮融资及规模

**原文标题**: Series C and scale

**原文链接**: [https://www.cursor.com/en/blog/series-c](https://www.cursor.com/en/blog/series-c)

AI 编码助手 Cursor 背后的公司 Anysphere 宣布成功完成 C 轮融资，以 99 亿美元的估值融资 9 亿美元。本轮投资来自 Thrive、Accel、Andreessen Horowitz 和 DST 等知名风险投资公司。

这笔新资金将用于进一步推动 Anysphere 的 AI 编码研究并改进 Cursor。文章强调了 Cursor 的显著增长，实现了超过 5 亿美元的年度经常性收入 (ARR)。该工具也实现了显著的市场渗透，目前已被超过一半的财富 500 强公司使用，包括 NVIDIA、Uber 和 Adobe 等知名企业。

该公告强调了 Anysphere 的核心使命：开发卓越的编码体验。C 轮融资和现有的市场吸引力表明，Anysphere 完全有能力实现其愿景，并推动人工智能驱动的编码工具的边界。

---

## 43. 武器化Dependabot：精妙的Pwn请求

**原文标题**: Weaponizing Dependabot: Pwn Request at its finest

**原文链接**: [https://boostsecurity.io/blog/weaponizing-dependabot-pwn-request-at-its-finest](https://boostsecurity.io/blog/weaponizing-dependabot-pwn-request-at-its-finest)

本文详细介绍了如何通过“混乱代理”攻击方式利用 GitHub 的依赖项更新机器人 Dependabot，注入恶意代码并绕过分支保护。攻击者可以欺骗信任 Dependabot 的自动合并工作流，从而合并来自派生存储库的恶意代码。

核心技术包括：派生一个具有自动合并工作流的仓库，引入恶意代码，然后操纵 Dependabot 更新来自派生仓库的 PR，从而触发合并。作者重点介绍了两种新的 TTP，通过操纵分支名称来实现命令注入。这包括创建合并冲突和交换默认分支，将恶意代码注入到 Dependabot 的分支中。这允许通过分支名称执行进行命令注入。

此外，本文还概述了，借助 `contents: write` 权限，攻击者如何通过将恶意代码直接推送到 Dependabot 的分支，然后使用 `@dependabot merge` 命令触发合并来绕过分支保护。文章最后总结道，虽然 Dependabot 是一个受欢迎的目标，但如果需要自动化，任何受信任且可控的机器人都可以被类似地利用。作者的团队已经发现了多个机器人，它们是类似恶作剧的主要候选对象，表明存在更广泛的威胁格局。

---

## 44. 货运铁路推动新型豪华卧铺列车初创公司

**原文标题**: Freight rail fueled a new luxury overnight train startup

**原文链接**: [https://www.freightwaves.com/news/how-freight-rail-fueled-a-new-luxury-overnight-train-startup](https://www.freightwaves.com/news/how-freight-rail-fueled-a-new-luxury-overnight-train-startup)

Dreamstar 计划重振洛杉矶至旧金山的豪华夜间火车旅行，让人想起 20 世纪 40 年代南太平洋铁路公司的云雀号列车。联合创始人 Joshua Dominic 和 Thomas Eastmond 计划利用货运铁路基础设施，并已与联合太平洋铁路公司达成协议备忘录，以获得在夜间货运流量最少的路线上使用轨道的权限。

Dreamstar 的愿景包括全卧室住宿、美食餐饮和高端酒店服务。他们还在寻求与 Caltrain 和 Metrolink 等通勤机构达成协议。这家初创公司声称碳排放量比飞行减少 75%，并计划提供与机票加酒店住宿相当的具有竞争力的价格。

受 Budd Hi-Level 车厢的启发，Dreamstar 的列车设计包括各种私人客舱等级、休息室、用餐空间和水疗中心，以及用于汽车运输的汽车渡轮。该公司最初计划建造一列新火车，现在打算重建现有车厢。宝马设计工作室已完成概念阶段。

列车建设预计需要 18 到 24 个月，目标是在 2028 年洛杉矶奥运会之前开始运营。虽然尚未选定机车供应商，但正在考虑多种选择。该公司还在与行业专家合作，以获得监管部门的批准，并已从包括房屋建筑商 Bill Lyon 在内的投资者那里获得了初步融资。与传统运营商相比，Dreamstar 强调精简、资本高效的商业模式。

---

## 45. 4-7-8呼吸法

**原文标题**: 4-7-8 Breathing

**原文链接**: [https://www.breathbelly.com/exercises/4-7-8-breathing](https://www.breathbelly.com/exercises/4-7-8-breathing)

这则摘要表明存在一种名为“4-7-8呼吸法”的呼吸练习，由一家名为“Breathbelly”的公司或网站提供（可能免费）。 它强调这项练习是一种可能涉及“腹式呼吸”或针对“breathbelly”的呼吸锻炼。 核心要点是，这篇文章可能详细介绍或推广4-7-8呼吸法，而Breathbelly是与该技术相关的资源提供商。 因为唯一的背景是标题和网站名称，所以该技术的具体益处、步骤以及Breathbelly关于此呼吸练习的具体服务尚不清楚，需要进一步浏览链接文章。

---

## 46. Windows 10 窥探您对系统设置的使用 (2021)

**原文标题**: Windows 10 spies on your use of System Settings (2021)

**原文链接**: [https://www.michaelhorowitz.com/Windows10.spying.onsettings.php](https://www.michaelhorowitz.com/Windows10.spying.onsettings.php)

迈克尔·霍洛维茨的文章详细介绍了Windows 10如何在系统设置中监视用户活动。霍洛维茨使用Nir Sofer的DNS和TCP日志记录工具发现，仅仅打开系统设置就会触发对`www.bing.com`和`cxcs.microsoft.net`的DNS查询，然后向这些域发出出站HTTPS请求。即使使用本地帐户、禁用遥测和锁定设置，也会发生这种情况。

作者怀疑`cxcs.microsoft.net`与微软的客户体验中心有关，而`www.bing.com`除了搜索引擎功能外，还用于遥测。 阻止`cxcs.microsoft.net`导致进一步的DNS请求，这次是对`ctldl.windowsupdate.com`的请求。

霍洛维茨建议采取防御性计算措施，例如修改路由器DNS设置以阻止特定域（例如，使用Pepwave路由器或Pi-Hole），使用YogaDNS与NextDNS，或使用具有出站控制的防火墙。 他指出，当使用VPN或安全DNS时，路由器级别阻止的局限性。

他发现修改“hosts”文件以阻止`www.bing.com`的结果不一致，`nslookup`忽略了这些更改。最终，霍洛维茨主张在网络范围内阻止遥测域，并建议使用DuckDuckGo作为Bing的替代方案。 他根据自己的观察提供了一个要阻止的域列表。 一项更新提到微软会重写bing.com的子域名，并指出`svchost.exe`和`SearchApp.exe`也会对`www.bing.com`进行DNS查询。 该文章还引用了Helge Klein的一项研究，该研究表明Windows与数百个主机和数千个IP地址进行通信。

---

## 47. SaaS只是换了更好说辞的厂商锁定。

**原文标题**: SaaS is just vendor lock-in with better branding

**原文链接**: [https://rwsdk.com/blog/saas-is-just-vendor-lock-in-with-better-branding](https://rwsdk.com/blog/saas-is-just-vendor-lock-in-with-better-branding)

文章认为，虽然SaaS解决方案承诺通过处理身份验证、队列和存储等任务来简化开发，但集成它们会带来货币支出以外的隐藏成本。这些“税收”包括花费在以下方面的时间和精力：

1. **发现：** 研究和评估不同的SaaS选项，以了解其功能、兼容性和定价。
2. **注册：** 在编写任何代码之前，就承诺使用一项服务，通常要交出付款信息。
3. **集成：** 实施SaaS服务，与文档作斗争，并解决意想不到的边缘情况。
4. **本地开发：** 在本地复制SaaS服务进行测试，可能需要复杂的配置。
5. **生产：** 确保服务的可靠性，安全地管理API密钥，并解决生产问题。

作者认为，所有选择，包括开源和自托管解决方案，都会导致供应商锁定，因为切换时需要重写代码。因此，作者提倡选择像Cloudflare或Supabase这样的集成平台，这些平台将基本服务捆绑在一起，并无缝协同工作。这种方法最大限度地减少了上下文切换、API密钥管理和兼容性问题，从而创造了更流畅的开发者体验并促进了“心流”。通过选择一体化平台，开发者可以专注于构建其核心软件，而不是不断管理和集成不同的SaaS解决方案。

---

## 48. Swift与可爱的2D游戏框架：使用CMake设置项目

**原文标题**: Swift and the Cute 2d game framework: Setting up a project with CMake

**原文链接**: [https://layer22.com/swift-and-cute-framework-setting-up-a-project-with-cmake](https://layer22.com/swift-and-cute-framework-setting-up-a-project-with-cmake)

本文提供了一个分步指南，介绍如何使用 Swift 设置基于 Cute Framework (用 C/C++ 编写) 的 2D 游戏开发项目。它利用 CMake 管理构建过程，使开发者能够用 Swift 编写游戏逻辑，同时利用 C/C++ 的性能优势进行渲染。

该指南涵盖了必要的先决条件（Swift、CMake、Ninja）、项目结构创建以及 `CMakeLists.txt` 文件的配置，以管理依赖项，包括下载和链接 Cute Framework。它还详细介绍了如何使用 shim 头文件 (`shim.h`) 和模块映射 (`module.modulemap`) 设置 Swift 与 C 代码的互操作性。

示例代码演示了如何创建 Cute Framework 应用程序、实例化精灵、播放动画、更新应用程序和精灵状态，以及在游戏循环中将精灵绘制到屏幕上。最后，本文提供了使用 CMake 和 Ninja 配置和构建项目的命令，以及运行生成的可执行文件的说明。 关键在于利用 Swift 的表达能力与 C/C++ 在使用 Cute Framework 进行游戏开发时的性能。

---

## 49. 如何在安卓系统上（真正地）发送DTMF信号，且不成为默认通话应用

**原文标题**: How to (actually) send DTMF on Android without being the default call app

**原文链接**: [https://edm115.dev/blog/2025/01/22/how-to-send-dtmf-on-android](https://edm115.dev/blog/2025/01/22/how-to-send-dtmf-on-android)

无法访问文章链接。

---

## 50. 速率限制互动指南

**原文标题**: An Interactive Guide to Rate Limiting

**原文链接**: [https://blog.sagyamthapa.com.np/interactive-guide-to-rate-limiting](https://blog.sagyamthapa.com.np/interactive-guide-to-rate-limiting)

无法访问文章链接。

---

## 51. 研究人员找到使艾滋病毒在白细胞内可见的方法。

**原文标题**: Researchers find a way to make the HIV virus visible within white blood cells

**原文链接**: [https://www.theguardian.com/global-development/2025/jun/05/breakthrough-in-search-for-hiv-cure-leaves-researchers-overwhelmed](https://www.theguardian.com/global-development/2025/jun/05/breakthrough-in-search-for-hiv-cure-leaves-researchers-overwhelmed)

墨尔本多尔蒂研究所的研究人员在艾滋病治愈研究方面取得重大突破。他们开发出一种新方法，使艾滋病毒在白细胞内显现，而病毒通常隐藏在其中，逃避免疫系统和药物治疗。这种隐藏能力一直是寻找治疗方法的重大障碍。

这种新方法利用了mRNA技术，类似于新冠疫苗中使用的技术。研究人员将mRNA封装在一种新设计的名为LNP X的脂肪泡中，可以将其输送到艾滋病毒所在的特定白细胞。然后，mRNA指示这些细胞暴露病毒。

这一进展解决了将mRNA输送到这些细胞的难题，这之前被认为是不可行的。研究人员对新方法的有效性感到“震惊”。

虽然该研究目前基于实验室，使用艾滋病患者捐赠的细胞，但它代表了艾滋病治愈研究的重要一步。还需要进一步研究，以确定暴露病毒是否足以让免疫系统消除它，或者是否需要与其他疗法结合使用。动物和人体试验也是必要的，这个过程可能需要数年时间。

专家们承认这一进展的潜力，并指出它可能对涉及相同白细胞的其他疾病（包括癌症）产生更广泛的影响。然而，仍然存在挑战，包括需要消除整个病毒库，以及实现这一目标是否可能的问题。

---

## 52. 我读了 Cloudflare 所有 Claude 生成的提交记录

**原文标题**: I Read All of Cloudflare's Claude-Generated Commits

**原文链接**: [https://www.maxemitchell.com/writings/i-read-all-of-cloudflares-claude-generated-commits/](https://www.maxemitchell.com/writings/i-read-all-of-cloudflares-claude-generated-commits/)

米切尔的文章分析了Cloudflare几乎完全使用Claude构建OAuth 2.1库的经验，重点介绍了有据可查的人工智能协作过程。他强调了在提交消息中包含提示的价值，将git历史转化为意图记录，并促进更轻松的审查。

该协作揭示了诸如“示例提示”和迭代反馈（“你做了X，但我们应该做Y。请修复。”）之类的模式。人工智能擅长生成文档。然而，人工智能在诸如重构代码之类的任务中表现不佳，需要人工干预来进行样式调整和错误修复。

米切尔强调了使用人工智能编码工具的实用经验：专注于可交付成果（例如，端点行为、示例用法），将提示视为版本控制资产，期望进行多轮提示，并知道何时进行手动干预。

他提出了一个未来，即提示是源代码，允许使用改进的模型和自文档化的业务逻辑来重新生成代码库。这引发了一个问题，即随着模型的发展，是否“应用程序”本身会成为提示提交的历史记录，从而消除代码生成步骤。

最终，该经验例证了一种新的创造性动态，即人工智能处理实施，而人类提供指导和判断，即使在提示创建、错误修复和战略监督方面仍然需要大量的人工参与。

---

## 53. 美国数字服务局的起源

**原文标题**: United States Digital Service Origins

**原文链接**: [https://usdigitalserviceorigins.org/](https://usdigitalserviceorigins.org/)

本文宣布启动一项口述历史项目，旨在记录美国数字服务局 (USDS) 的起源和早期发展历程。该项目于 2025 年 6 月 6 日发布，旨在保存 USDS 奠基者所吸取的经验教训，尤其是在其最近的重组和更名之后。

该口述历史收录了 2009 年至 2015 年期间近 50 次访谈，记录了创始人、机构团队领导者和实践社区成员的观点。这些访谈共同讲述了 USDS 的概念化、创建以及在政府环境中实施新技术的挑战。该项目确定了关键主题、经验教训和事件年表，展示了在美国数字服务局 (USDS) 工作的经历，包括不同的观点。

作者 Kathy Pham 和 Emily Tavoulareas 强调，这项口述历史是更大、持续进行的公民科技运动的一部分，该运动相信利用数字专业知识来改善公共服务。他们认为，无论政府技术团队的未来形式如何，USDS 的遗产和经验教训仍然很有价值，因为它展示了积极变革的潜力及其对服务人员的影响。文章最后邀请读者注册以获取项目更新。

---

## 54. 像SQLite一样在Python中测试Postgres

**原文标题**: Test Postgres in Python Like SQLite

**原文链接**: [https://github.com/wey-gu/py-pglite](https://github.com/wey-gu/py-pglite)

Py-PGlite: 简化 PostgreSQL 测试的 Python 库，提供零配置、即时可用的测试方案，媲美 SQLite 的易用性。无需 Docker、手动设置或配置文件，开发者只需极少的工作量即可使用真实的 PostgreSQL 进行测试。

主要特点包括：

*   **零配置快速启动:** 与 SQLAlchemy 和 Django 无缝集成，自动配置数据库和模型。
*   **原生 SQL 支持:** 允许直接执行 SQL 查询，充分利用 PostgreSQL 的全部功能，如 JSON 和数组。
*   **框架就绪:** 兼容 SQLAlchemy、Django 和 FastAPI。
*   **快速设置:** 相比基于 Docker 的 PostgreSQL 测试，启动时间显著缩短 (2-3 秒 vs. 30-60 秒)。
*   **隔离测试:** 每个测试都获得一个全新的数据库实例，确保隔离性。
*   **自定义配置:** 提供自定义配置选项，如端口范围、超时和清理。
*   **性能测试:** 方便使用真实的 PostgreSQL 功能进行性能测试。
*   **框架隔离:** 能够针对特定框架 (SQLAlchemy 或 Django) 或目录隔离进行定向测试。

Py-PGlite 的架构基于与框架无关的核心以及可选的集成，侧重于零配置、智能默认值和完美隔离。它简化了 PostgreSQL 测试，使其对 Python 开发者来说更易于访问和高效。

---

## 55. 改善人类种族的梦想不再是科幻小说。

**原文标题**: Dreams of improving the human race are no longer science fiction

**原文链接**: [https://www.economist.com/briefing/2025/03/20/dreams-of-improving-the-human-race-are-no-longer-science-fiction](https://www.economist.com/briefing/2025/03/20/dreams-of-improving-the-human-race-are-no-longer-science-fiction)

在2025年3月《经济学人》发表的题为《改善人类的梦想不再是科幻》的文章中，探讨了一个“人类增强”产业的兴起。受克里斯蒂安·安格迈尔等人的推动，此行业旨在使人们更强壮、更聪明、更长寿，安格迈尔的灵感来自于致幻体验。

安格迈尔的投资基金支持用于精神健康的迷幻药物治疗，并推动更广泛的人类增强。他还支持诸如为抗衰老突破设立的1.01亿美元奖金和增强运动会等项目，后者是一项奖励运动员使用通常在传统体育运动中被禁止的兴奋剂打破世界纪录的比赛。

文章表明，尽管增强人类的想法曾经被归为科幻小说，但它正变得越来越现实，尽管仍然受到过时法规的阻碍。文章还涉及其他相关话题，包括不断变化的性别偏好、萨尔瓦多和越南的政治转变、越南的经济担忧、加密货币在美国政治中日益增长的影响力以及对俄罗斯军工行业的见解。

---

## 56. 死亡蝾螈的绝境

**原文标题**: The impossible predicament of the death newts

**原文链接**: [https://crookedtimber.org/2025/06/05/occasional-paper-the-impossible-predicament-of-the-death-newts/](https://crookedtimber.org/2025/06/05/occasional-paper-the-impossible-predicament-of-the-death-newts/)

道格·缪尔的《死亡蝾螈的困境》探讨了太平洋西北地区粗皮蝾螈（Taricha granulosa）和普通束带蛇（Thamnophis sirtalis）之间的进化军备竞赛。这种蝾螈由于其皮肤中细菌产生的河豚毒素而具有极高的毒性，能够杀死人类。

束带蛇已经进化出对这种毒素的抵抗力，从而驱动蝾螈变得更具毒性，形成了一个生物反馈循环。这种毒性给蝾螈带来了代谢成本，而抵抗力可能也会给蛇带来缺陷，尽管这些缺陷难以衡量。

束带蛇食用蝾螈以将河豚毒素储存在它们的肝脏中，使它们自身对捕食者有毒。作者解释说，蝾螈无法进化出警戒色作为警告，因为这会使它们更容易成为蛇的目标。蝾螈面临三重困境：它们必须具有超强的毒性，进化出针对自身毒素的防御机制，并且无法发出毒性信号。

文章随后深入探讨了区域差异，例如阿拉斯加（束带蛇稀少）和温哥华岛毒性较低的蝾螈，在这些地方，蛇和蝾螈的关系似乎更加和谐。作者提出了蛇进化出警戒色的可能性，因为它们本身也具有毒性。他强调太平洋西北地区的生态系统还很年轻，表明这场军备竞赛仍在进化，并且不一定是长期稳定的。这篇文章强调，虽然人们已经了解了很多，但围绕着这种迷人的生物相互作用仍然存在着许多谜团。

---

## 57. 我们如何回应《纽约时报》的数据需求，以保护用户隐私

**原文标题**: How we’re responding to The NYT’s data demands in order to protect user privacy

**原文链接**: [https://openai.com/index/response-to-nyt-data-demands/](https://openai.com/index/response-to-nyt-data-demands/)

OpenAI博客文章《我们如何回应纽约时报的数据要求以保护用户隐私》概述了他们对《纽约时报》(NYT)的回应，该回应涉及一起关于OpenAI在训练其大型语言模型时使用NYT文章的版权侵权诉讼。回应的核心在于保护用户隐私并维持其人工智能模型的核心功能。

OpenAI辩称，他们正在采取措施解决纽约时报的担忧，特别是关于其模型几乎逐字复制纽约时报文章摘录的问题。他们认为这些情况是罕见的“漏洞”，是模型意外行为的结果，而不是固有的设计缺陷，也不能表明存在广泛的版权侵权行为。

该公司正在积极改进其模型以防止此类输出，包括实施措施以限制模型逐字背诵或重复内容的能力。然而，OpenAI强调，他们的首要任务是在*不*大幅降低其模型对用户的效用和有用性的前提下做到这一点。他们担心，广泛限制模型根据其训练数据提供有帮助和信息丰富的响应能力的更改可能会损害用户体验。

该文章表明，纽约时报要求的过于宽泛或限制性的措施可能弊大于利。OpenAI旨在在尊重版权问题和坚持为用户提供最佳人工智能工具的承诺之间取得平衡。他们认为，通过有针对性的技术调整，而不是全面的限制，这是可以实现的。本质上，OpenAI正在努力避免因纽约时报的数据要求而削弱其模型。

---

## 58. 能动系统系列

**原文标题**: The Agentic Systems Series

**原文链接**: [https://gerred.github.io/building-an-agentic-system/](https://gerred.github.io/building-an-agentic-system/)

"自主代理系统系列" 是一套旨在帮助工程师构建可用于生产环境的 AI 编码助手的综合指南。这套共三册的书籍深入探讨了高效 AI 编码工具背后的模式、架构和工程决策，并借鉴了 Amp、Claude Code 和 anon-kode 等真实案例。

**第一册：构建自主代理系统** 专注于构建单用户 AI 编码代理的基础，涵盖核心架构、工具系统、权限模型、并行执行和命令系统。

**第二册：增强自主代理系统** 探讨如何将单用户代理扩展到企业级协作平台，解决可扩展架构、身份验证、协作模式、企业功能、高级编排和生产策略等问题。

**第三册：情境化自主代理系统** 深入研究高级工具系统和上下文管理，涵盖工具系统架构、命令系统设计以及如何维护对话上下文。

本系列面向对 AI 驱动的开发工具有兴趣的系统工程师、平台团队、技术领导者和研究人员。它要求读者熟悉系统设计、基本的 AI/LLM 集成以及一些后端技术经验。

本系列提供架构模式、实施策略、决策框架、代码示例和真实案例研究，所有这些都源于对生产系统的广泛分析。

作者 Gerred 是一位在 AI 和基础设施方面拥有经验的系统工程师，包括参与 CNCF 项目、Kubernetes 以及在受监管环境中部署 AI 系统。他提供咨询服务，并鼓励读者支持他的研究。

---

## 59. 科莱寇亚当电脑

**原文标题**: The Coleco Adam Computer

**原文链接**: [https://dfarq.homeip.net/coleco-adam-computer/](https://dfarq.homeip.net/coleco-adam-computer/)

戴夫·法夸尔的文章探讨了科莱寇亚当电脑的兴衰。这款1983年由玩具制造商科莱寇推出的产品，旨在打入家用电脑市场。亚当电脑发布时备受期待，承诺提供一套完整的系统，包括80K内存、全尺寸键盘、磁带存储、菊花式打印机和软件，总价525美元（后涨至725美元）。它的目标是与Commodore竞争，特别是通过提供一种“开箱即用”的系统，这与Commodore 64的裸机不同。它还提供了与 ColecoVision 游戏机的兼容性。

然而，亚当电脑问题缠身。科莱寇难以按时完成生产，最初的设备存在很高的缺陷率。设计缺陷包括不可靠的数据包（基于磁带的存储）、一个噪音大且速度慢的打印机（该打印机容纳了整个系统的电源），以及褒贬不一的评论。评论家喜欢键盘和打印质量，但不喜欢电源的位置。

此外，Commodore解决了其供应问题，以相似的价格提供了一套可比的系统。Commodore制造自己的芯片的能力使其在定价方面具有优势。最终，科莱寇损失了近5000万美元，并在1985年初停止生产亚当电脑，仅售出30万至40万台。整个公司于1988年倒闭。

尽管亚当电脑失败了，但它仍然拥有一批狂热的追随者，并且在概念上类似于日本成功的MSX电脑。法夸尔推测，如果科莱寇能及时交付一台功能正常的亚当电脑，它可能会对电脑市场产生重大影响，甚至可能吸引克隆产品并改变竞争格局。文章还强调了亚当电脑发布的一个有趣的副作用：它间接导致了雅达利和任天堂之间谈判的破裂，导致 NES 没有由雅达利生产。

---

## 60. 亚历克斯·奇内克在伦敦广场打造的波纹联排别墅立面

**原文标题**: A Rippling Townhouse Facade by Alex Chinneck Takes a Seat in a London Square

**原文链接**: [https://www.thisiscolossal.com/2025/05/alex-chinneck-a-week-at-the-knees/](https://www.thisiscolossal.com/2025/05/alex-chinneck-a-week-at-the-knees/)

英国艺术家Alex Chinneck在伦敦Charterhouse广场为克勒肯维尔设计周揭幕了引人注目的公共雕塑作品“跪姿一周”。该作品从他2013年的作品“从我的鼻子到脚趾的膝盖”中汲取灵感，后者似乎展现了一栋联排别墅的正面滑落，而这个新装置则以一种俏皮的方式重新构想了一个经典的乔治亚风格的建筑立面。

这个雕塑由320米长的再生钢材和7000块砖砌成。它描绘了一栋建筑立面的下两层在一条小路上弯曲和弯曲，创造了一种建筑“坐着”，膝盖抬起的印象。这种拟人化的方法邀请游客将这件作品作为一个独特的门户，与伦敦著名的绿地互动。

这座雕塑高五米，重达12吨，厚度仅为15厘米，巧妙地模仿了一个真人大小的建筑物，并具有令人惊讶的轻量化美感。Chinneck与众多英国公司合作制造了该作品，采购了定制的钢梁、弧形窗户和砖块。最终的结果是一个建筑结构，它在重量和优雅、俏皮的个性之间取得了平衡。这件艺术品将在伦敦展出至六月。

---

## 61. 我做了一个比Elasticsearch还差的搜索引擎 (2024)

**原文标题**: I made a search engine worse than Elasticsearch (2024)

**原文链接**: [https://softwaredoug.com/blog/2024/08/06/i-made-search-worse-elasticsearch](https://softwaredoug.com/blog/2024/08/06/i-made-search-worse-elasticsearch)

Doug Turnbull详细介绍了构建 Pandas 全文搜索库 SearchArray 的经验，并使用 BEIR 信息检索基准，特别是 MSMarco Passage Retrieval 语料库，将其与 Elasticsearch 进行了基准测试。他幽默地分享了 SearchArray 在几乎所有方面都比 Elasticsearch 表现更差的失望：NDCG@10（相关性指标）、搜索吞吐量（每秒查询次数）和索引吞吐量（每秒文档数）。

Turnbull 随后深入研究了性能差距背后的原因。一个关键区别在于 Elasticsearch 如何利用 Weak-AND (WAND) 等算法来优化搜索，通过关注高影响力、稀有词项并选择性地扫描文档列表。另一方面，SearchArray 天真地计算所有文档的 BM25 分数，导致效率低下。

他还解释了 SearchArray 的内部架构，该架构使用基于 roaring bitmap 的位置索引，主要为短语匹配而设计。虽然该系统允许计算词频，但它不如 Elasticsearch 使用的倒排列表高效。此外，与专用搜索引擎不同，SearchArray 没有为 BM25 组件或整个查询实施积极的缓存策略。

作者总结说，SearchArray 适用于原型设计和较小的数据集，并承认了 Elasticsearch、Solr 和 Vespa 等大型搜索引擎的复杂性和精妙之处。他强调了搜索工程师所做工作的价值，并认为能够为查询构建和优化提供更面向 dataframe 的 DSL 的工具将是有益的。最后，他宣传了他关于将 LLM 应用于搜索的课程。

---

## 62. 什么是OAuth及其工作原理？

**原文标题**: What Is OAuth and How Does It Work?

**原文链接**: [https://fusionauth.io/articles/oauth/modern-guide-to-oauth](https://fusionauth.io/articles/oauth/modern-guide-to-oauth)

本文全面概述了 OAuth 2.0，侧重于实际应用和真实场景的集成，而不仅仅是理论规范。它解释了 OAuth 如何允许应用程序将身份验证和授权委托给其他服务，从而提高安全性并改善用户体验，而无需直接请求凭据。

文章的核心在于定义和解释八种常见的“OAuth 模式”，这些模式代表了 OAuth 的不同实现方式。这些模式包括：

*   **本地登录和注册：** 使用您控制的 OAuth 服务器进行本地身份验证。
*   **第三方登录和注册：** 利用 Facebook 或 Google 等服务进行用户身份验证，通常会授予对用户数据的访问权限。
*   **第一方登录和注册（反向联邦身份）：** 构建一个平台，并允许其他开发者使用用户登录来访问您的服务。
*   **企业登录和注册：** 通过与 SAML 和其他企业身份验证系统集成，满足企业客户的需求。
*   **第三方服务授权：** 代表用户访问第三方服务。
*   **第一方服务授权：** 类似于第三方授权，但用于您自己的 API。
*   **机器对机器的身份验证和授权：** 无需用户参与即可实现服务之间的安全通信。
*   **设备登录和注册：** 允许从输入能力有限的设备（如电视）进行登录。

本文帮助读者根据其特定需求（例如外包身份验证、避免密码存储或促进服务间通信）确定合适的 OAuth 模式。它使用“ToDo List”应用程序示例来说明本地登录和注册以及第三方登录和注册的流程。

---

## 63. 最高法院允许狗狗币访问社保数据

**原文标题**: Supreme Court allows DOGE to access social security data

**原文链接**: [https://www.nbcnews.com/politics/supreme-court/supreme-court-trump-doge-social-security-data-access-elon-musk-rcna206515](https://www.nbcnews.com/politics/supreme-court/supreme-court-trump-doge-social-security-data-access-elon-musk-rcna206515)

最高法院允许特朗普政府效率部访问社保署数据，引发争议

最高法院，以保守派占多数，已允许特朗普政府的政府效率部（DOGE）访问社会保障管理局（SSA）的数据，推翻了下级法院的禁令。 这项决定使由埃隆·马斯克创立的DOGE能够审查SSA的记录，包括社会保障号码、医疗记录和税务信息，以实现系统现代化并打击浪费和欺诈。

进步团体、工会和美国退休人员联盟提起了诉讼，挑战DOGE的访问权限，他们对这项裁决可能导致美国人个人数据被盗表示担忧。 白宫官员称这项决定是政府现代化的胜利。 法官凯坦吉·布朗·杰克逊对此表示异议，质疑干预的紧迫性。

在另一项裁决中，最高法院还保护DOGE免受《信息自由法》（FOIA）的请求，暂停发布文件和DOGE管理员艾米·格里森的取证，直到诉讼继续进行。 华盛顿公民责任与道德组织对此表示失望，但对允许继续进行调查取证感到满意。

社会保障管理局局长对该裁决表示欢迎，称其将推动现代化并改善对受益人的服务。

---

## 64. 思考需要多少能量？

**原文标题**: How much energy does it take to think?

**原文链接**: [https://www.quantamagazine.org/how-much-energy-does-it-take-to-think-20250604/](https://www.quantamagazine.org/how-much-energy-does-it-take-to-think-20250604/)

人类大脑的能量消耗：专注思考并未显著增加能量支出

这篇文章探讨了人类大脑的能量消耗，挑战了一种观点，即专注思考会显著增加能量支出。神经科学家沙尔纳·贾马达尔的研究表明，费力的任务仅比大脑休息时的活动多消耗约5%的能量。大脑的大部分能量（95%）用于维护功能，例如调节身体系统（体内平衡）和预测处理。

大脑虽然仅占体重的2%，却消耗身体20%的能量，依赖于葡萄糖和氧气产生的ATP。 使用PET和fMRI扫描的研究表明，虽然活跃的任务会增加相关脑区域的神经元放电，但整体能量增加非常小。 大部分休息时的大脑活动都涉及默认模式网络，该网络负责内部精神体验和维持体内平衡。 乔丹·特里奥认为，大脑不断预测未来的需求，以有效地分配资源。

神经科学家扎希德·帕达姆西强调，精神疲劳的感觉并非源于缺乏能量，而是源于一种旨在节约资源的进化适应。 人类祖先在卡路里稀缺的环境中进化，即使是很小的能量增加也意义重大。 大脑还在神经元信号传导中优化能量效率，放电率和突触传递远低于理论上的可能性，从而优先考虑每消耗一个单位ATP的信息传输。文章总结认为，人类大脑的巨大尺寸和复杂性与其能量成本相平衡，从而塑造其功能和效率。

---

## 65. 随时随地使用自由高斯基元进行动态场景重建

**原文标题**: Free Gaussian Primitives at Anytime Anywhere for Dynamic Scene Reconstruction

**原文链接**: [https://zju3dv.github.io/freetimegs/](https://zju3dv.github.io/freetimegs/)

本文介绍FreeTimeGS，一种重建具有复杂运动的动态3D场景的新方法。该方法解决了现有技术依赖于变形规范高斯基元时遇到的局限性，这些技术通常难以处理复杂的运动。FreeTimeGS提出了一种4D表示，其中高斯基元可以存在于任何时间和位置，从而为动态场景建模提供更大的灵活性。

FreeTimeGS的关键在于为每个高斯基元分配一个运动函数，该函数决定了其随时间的运动，从而减少了时间冗余。该方法使用时间不透明度函数来调节每个高斯随时间的影响。然后使用4D正则化损失来正则化这些4D高斯，并通过渲染损失来优化光栅化，从而能够从多视角视频中重建动态3D场景。

实验表明，与其他最先进的方法（如4DGS、STGS和Deform-3DGS）相比，FreeTimeGS实现了卓越的渲染质量。作者提供了补充材料，包括交互式演示、具有慢动作回放的实时渲染示例、使用Waymo数据集的街道重建演示，以及在Apple Vision Pro和Meta Quest 3上的实时VR演示，以展示FreeTimeGS的功能。代码将被发布以供重现。作者还鼓励商业咨询和合作。

---

## 66. 黑客行为是必要的

**原文标题**: Hacking Is Necessary

**原文链接**: [https://scharenbroch.dev/blog/hacking-is-necessary/](https://scharenbroch.dev/blog/hacking-is-necessary/)

本文认为，“黑客式开发”（定义为优先考虑速度和便利性，而非理想的代码结构和安全性）是软件开发中一个必要的方面。作者认为，追求完美代码（以清晰性、可扩展性和安全性等理想为目标）是一个渐近过程，真正达到完美是不可能的。因此，开发人员必须不断在理想主义和实用主义之间做出权衡。

作者以类型强度为例说明。虽然更强的类型假设（例如，将整数限制在特定范围内）可以提高代码安全性和文档质量，但也会增加维护负担，并且可能过于严格，尤其是在假设不确定或硬件限制介入时。

文章进一步认为，类似于类型，代码的复杂结构通常也需要务实的方法。重构虽然强大，但可能非常耗时且有风险。文章强调，有时“足够好”比追求难以捉摸的理想更好，特别是对于“棘手的问题”——那些复杂到无法预先规划完整解决方案的问题。本质上，黑客式开发充当了临时支架，以帮助开发实际的解决方案。

结论提倡有意识的黑客式开发，承认妥协的必要性。作者鼓励开发人员有意识地选择在哪里投入理想，在哪里优先考虑实用性，强调同时拥抱两种方法并从错误中学习的重要性。

---

## 67. 没有条纹的衬衫 (2021)

**原文标题**: Shirt Without Stripes (2021)

**原文链接**: [https://github.com/elsamuko/Shirt-without-Stripes](https://github.com/elsamuko/Shirt-without-Stripes)

名为“无条纹衬衫（2021）”的这份文档，似乎是对各平台关于搜索词“无条纹衬衫”的搜索结果和链接的汇编。

第一部分列出了在谷歌、亚马逊和必应上搜索“无条纹衬衫”的结果，表明该文档的目的是追踪与纯色衬衫相关的信息或产品。

文档的其余部分提供了在“AI/ML”和“助手”标题下分类的亚马逊、微软和谷歌资源的链接。这表明衬衫搜索与这些技术之间可能存在关联或间接联系。也许这些平台被用于以某种方式促进或分析衬衫搜索。

最后，文档列出了亚马逊、必应、谷歌，以及一个 Hacker News (news.ycombinator.com) 线程的链接。包含 Hacker News 线程表明，技术社区中可能存在围绕“无条纹衬衫”主题或潜在相关问题的讨论或评论。

总而言之，该文档似乎是搜索结果、相关技术资源以及可能与最初的纯色衬衫搜索查询相关的讨论论坛链接的集合。在没有进一步背景信息的情况下，衬衫搜索与 AI/ML/助手链接之间的具体联系仍然不清楚。

---

## 68. 根据 YouTube 的说法，自行托管媒体被认为是有害的

**原文标题**: Self-hosting your own media considered harmful according to YouTube

**原文链接**: [https://www.jeffgeerling.com/blog/2025/self-hosting-your-own-media-considered-harmful](https://www.jeffgeerling.com/blog/2025/self-hosting-your-own-media-considered-harmful)

作者叙述了在YouTube上收到两次社区准则警告，一次是关于一个演示在Raspberry Pi 5上使用LibreELEC播放4K视频的视频，另一次是之前关于展示Jellyfin的视频。尽管作者强调其媒体来源合法且避免使用盗版工具，YouTube仍将这些视频标记为宣传未经授权访问付费内容。作者主要使用这些软件来托管合法获取的媒体库。

作者质疑YouTube的判断，强调LibreELEC视频已经上线一年多，拥有百万观看量后才被标记。作者提出申诉，但最初被驳回，YouTube似乎认为开源媒体管理是“有害的”。在公众强烈抗议后，LibreELEC视频被恢复。

作者已将该视频重新上传到Internet Archive和Floatplane。作者正在探索YouTube的替代方案，如PeerTube，但也承认由于受众较小和资金选择有限，难以实现可持续的内容制作。

作者还对YouTube的AI摘要表示担忧，认为内容可能被滥用于AI模型。评论区强调了虚假版权声明、大型媒体公司拥有的权力失衡，以及内容分享领域需要更公平的监管和竞争等问题。许多用户建议使用Rumble和Odysee作为替代平台，而另一些用户则对这些平台以及Floatplane商业模式的可持续性表示保留。

---

## 69. 有条件地热情捍卫副词

**原文标题**: Defending adverbs exuberantly if conditionally

**原文链接**: [https://countercraft.substack.com/p/defending-adverbs-exuberantly-if](https://countercraft.substack.com/p/defending-adverbs-exuberantly-if)

无法访问文章链接。

---

## 70. Show HN: Ask-human-mcp – 零配置人机协作舱，阻止幻觉

**原文标题**: Show HN: Ask-human-mcp – zero-config human-in-loop hatch to stop hallucinations

**原文链接**: [https://masonyarbrough.com/blog/ask-human](https://masonyarbrough.com/blog/ask-human)

本文介绍了一种名为“ask-human-mcp”的零配置方案，通过引入人机协作（HITL）机制来防止大型语言模型（LLM）产生幻觉。其核心思想是在LLM对其答案的置信度低于特定阈值时，插入人工验证步骤。

该系统监控LLM对其生成回复的“信念”或置信度评分。如果置信度高，LLM的答案将直接传递给用户。但是，如果置信度低，问题将被路由到人工审核员进行验证或更正。这可以防止LLM自信地呈现不正确的信息（幻觉）。

本文强调了“零配置”方面，表明易于集成且设置要求极低。该系统旨在在自动化和人工干预之间取得平衡，优化准确性，同时最大限度地减少人工工作。名称中的“mcp”可能指的是“最小关键路径”，表明仅在绝对必要时才会触发人工干预。

本文还表明，该工具旨在成为一个“舱口”——一种在潜在错误到达最终用户之前捕获它们的机制，从而提高LLM驱动应用程序的整体可靠性和可信度。它旨在通过战略性地利用人类判断来提供更强大、更可靠的体验。作者可能将此工具推广为一种实用且易于部署的解决方案，用于缓解LLM幻觉这一普遍问题。

---

## 71. Jepsen：TigerBeetle 0.16.11

**原文标题**: Jepsen: TigerBeetle 0.16.11

**原文链接**: [https://jepsen.io/analyses/tigerbeetle-0.16.11](https://jepsen.io/analyses/tigerbeetle-0.16.11)

此 Jepsen 报告调查了 TigerBeetle 的安全性，TigerBeetle 是一款高性能、容错的 OLTP 数据库，专为金融应用设计。TigerBeetle 专注于复式记账，以速度和可靠性为重点存储账户和转账数据。它使用 Viewstamped Replication (VR)，并声称即使在副本发生故障的情况下也能提供强可串行化。

该报告强调了 TigerBeetle 的独特功能，包括用于高争用工作负载的单节点写入核心、广泛的容错机制（ECC RAM 假设、通过校验和和多副本写入处理进程/时钟/存储/网络故障）以及跨集群的自动协调升级。

Jepsen 测试旨在通过构建一个测试套件来验证强可串行化，该套件利用 Jepsen 基于属性的测试和故障注入功能（版本 0.16.11 到 0.16.30）。一个关键挑战是将 Jepsen 的标准列表/集合/寄存器检查适应 TigerBeetle 的特定领域数据模型（账户和转账）。他们通过检查操作的明显时间戳是否具有强可串行性以及这些操作按时间戳顺序执行时的语义是否合理，绕过了这个限制。

测试策略侧重于一个两阶段的方法：一个包含读/写操作的主阶段和一个用于观察写入效果并推断其时间戳的最终读取阶段。通过分析推断的时间戳并将其与已知的成功写入进行比较，研究人员旨在识别与强可串行化的偏差。 本文仅详细介绍了测试设计，报告的其余部分未提供。

---

## 72. Show HN: Cpdown – 将任何网页/YouTube字幕复制为干净的Markdown格式(LLM就绪)

**原文标题**: Show HN: Cpdown – Copy any webpage/YouTube subtitle as clean Markdown(LLM-ready)

**原文链接**: [https://github.com/ysm-dev/cpdown](https://github.com/ysm-dev/cpdown)

Cpdown 浏览器扩展程序简化了将网页内容和 YouTube 字幕复制为干净、可用于 LLM 的 Markdown 格式的过程。它旨在通过清理和格式化内容以供 LLM 使用，从而改进典型的“复制-粘贴”功能。

主要功能包括一键（或键盘快捷键）复制网页内容和 YouTube 字幕、使用 Defuddle 或 Mozilla 的 Readability 自动提取内容、删除不必要的 HTML 元素以及为 LLM 应用进行 token 计数。它提供选项将复制的内容包装在三个反引号中以增强可读性，显示成功提示，甚至在成功复制后显示 Raycast 五彩纸屑动画。

目前可用于 Chrome，Firefox 版本“即将推出”，Cpdown 可以从 Chrome 网上应用店安装，也可以通过克隆存储库、使用 Bun 安装依赖项、构建扩展程序，然后在 Chrome 的扩展程序设置中加载解压缩的目录来手动安装。

该扩展程序提供配置选项，包括选择 Defuddle 和 Mozilla Readability 用于内容提取的能力，以及切换视觉反馈（提示、五彩纸屑）。

Cpdown 使用各种工具和框架构建，包括 Cursor、WXT、React、Shadcn UI、Sonner、Tailwind CSS、Defuddle、Mozilla Readability、Turndown 和 tiktoken。该扩展程序根据 MIT 许可证获得许可。

---

## 73. 半同步会议：别再浪费时间

**原文标题**: Semi-Sync Meetings: Stop Wasting Our Time

**原文链接**: [https://lukebechtel.com/blog/semi-sync-meetings-stop-wasting-our-time](https://lukebechtel.com/blog/semi-sync-meetings-stop-wasting-our-time)

卢克·贝克特尔认为，大多数会议都是低效、单线程的过程，浪费时间和人才。AI笔记并非解决方案，需要的是结构性变革：半同步会议。这种会议开始于共享文档中的静默并行工作，然后过渡到专注讨论。

作者强调了同步会议的问题：串行处理（一次只能一人发言）、等级偏见（资深声音主导）和问责制表演（模糊的责任归属）。

半同步解决方案包括一个“半同步阶段”（10-15分钟），在此阶段，每个人都在共享文档（Notion、Miro或Jira）中静默协作，随后进入“同步阶段”（15-20分钟），针对标记的项目进行专注讨论。主持人引导流程，监控文档，添加结构，并做笔记。参与者添加信息，评论他人的输入，标记需要讨论的项目，并回复评论。

文章针对 sprint 计划、回顾、设计评审、头脑风暴和状态更新提出了具体的会议形式建议。这种方法利用并行思考，促进平等参与，实时构建文档，并加速收敛。

他还建议通过整合会前异步工作来扩展这种方法。

对于反对意见，作者承认最初会有些尴尬，但强调了更高生产力以及更安静的团队成员的贡献。他敦促读者尝试将这种方法应用于一种会议类型，并跟踪结果。

---

## 74. 顶尖研究人员离开英特尔，打造拥有“最强大CPU”的初创公司

**原文标题**: Top researchers leave Intel to build startup with 'the biggest, baddest CPU'

**原文链接**: [https://www.oregonlive.com/silicon-forest/2025/06/top-researchers-leave-intel-to-build-startup-with-the-biggest-baddest-cpu.html](https://www.oregonlive.com/silicon-forest/2025/06/top-researchers-leave-intel-to-build-startup-with-the-biggest-baddest-cpu.html)

一群前英特尔顶级芯片架构师离职，在俄勒冈州比弗顿成立了一家名为AheadComputing的初创公司。该公司由首席执行官兼联合创始人黛比·马尔领导，旨在基于开源RISC-V架构构建一款强大的CPU，与英特尔专有的x86设计不同。创始人认为，向专用“芯片组”和开放标准的转变为规模较小、灵活的公司提供了在半导体行业进行创新的机会。

AheadComputing专注于RISC-V，可以实现定制化的芯片设计和高效的处理，有潜力吸引谷歌、亚马逊和三星等客户。该公司已筹集了2200万美元的风险投资，并邀请了半导体专家吉姆·凯勒加入董事会。虽然RISC-V传统上用于嵌入式系统，但AheadComputing的目标是将其应用于PC、笔记本电脑和数据中心。

这一举动反映了一个更广泛的趋势，即英特尔的离职员工在俄勒冈州创办新的芯片业务，为该州不断发展的半导体生态系统做出贡献。文章强调，虽然英特尔仍然是一支主导力量，但其最近面临的挑战和裁员为AheadComputing等创新型初创公司创造了机会，使其得以涌现并有可能推动微处理器技术的未来发展。创始人认为，他们较小的规模和专注的策略将使他们能够比在英特尔这样的大公司内部更快地行动，更具颠覆性。

---

## 75. 限制网站访问用户本地网络的提议

**原文标题**: A proposal to restrict sites from accessing a users’ local network

**原文链接**: [https://github.com/explainers-by-googlers/local-network-access](https://github.com/explainers-by-googlers/local-network-access)

本文档提出一项新的浏览器功能：“本地网络访问”，以限制网站在未经明确许可的情况下访问用户的本地网络。目前，网站可以利用用户的浏览器攻击本地网络上易受攻击的设备。本提案旨在通过要求网站在向私有 IP 地址、回环地址或具有“.local”域名的地址发起请求之前请求用户许可，来缓解此风险。

核心思想是通过新的“本地网络访问”权限来限制对本地网络的访问。如果网站尝试在没有此权限的情况下连接到本地 IP 地址，浏览器将显示提示，要求用户授权。本提案将“本地网络请求”定义为跨越地址空间边界到更私密空间的请求（公共 -> 本地，公共 -> 回环，本地 -> 回环）。

为了方便现有工作流程，本提案为 `fetch()` API 包含了一个 `targetAddressSpace` 参数，允许开发者明确声明应将请求视为前往本地或回环地址的请求，即使它使用 HTTP。 这有助于解决由于许多本地网络设备缺乏 HTTPS 而引起的混合内容阻止问题。 本提案还考虑了与 WebRTC、权限策略和权限 API 的集成。 依赖本地网络访问的现有工作流程将需要更新以明确请求该权限。

---

## 76. 美国研究表明：自述种族、族裔与基因祖源不符

**原文标题**: Self-reported race, ethnicity don't match genetic ancestry in the U.S.: study

**原文链接**: [https://www.science.org/content/article/race-ethnicity-don-t-match-genetic-ancestry-according-large-u-s-study](https://www.science.org/content/article/race-ethnicity-don-t-match-genetic-ancestry-according-large-u-s-study)

无法访问文章链接。

---

## 77. 小程序与小语言

**原文标题**: Small Programs and Languages

**原文链接**: [https://ratfactor.com/cards/pl-small](https://ratfactor.com/cards/pl-small)

本文探讨了小型程序、小型语言以及一般微型事物的吸引力，认为它们提供了一种独特的理解和控制形式。作者重点介绍了诸如一个 25 行的 DOM 差异库、一个 46 字节的“Forth”以及 Lisp 解释器用 Lisp 编写等简洁的语言实现示例。

作者认为这些例子之所以有意义，是因为它们揭示了一个概念的最小复杂度，并引用了柯尔莫哥洛夫复杂度。他们引用了诸如可放在名片上的光线追踪器，或仅有 436 字节且带有垃圾回收的 LISP 实例，认为这些微型事物证明概念是可以被掌握和理解的。

然后，文章转向小型编程语言，将汇编语言与 Forth、Lisp、Tcl 和 Lua 等高级语言进行对比，指出了大小和表达能力之间的权衡。它强调了简单性比表达能力更重要，呼应了 David Ungar 的观点。

最后，文章深入探讨了对微型事物的一般迷恋，认为它们在混乱的世界中提供了一种掌控感、秩序感和控制感。作者引用了关于微型事物的作者的观点，断言缩小事物会使其更易于访问、更易于管理，并允许低风险的实验，最终恢复我们的秩序感和价值感。文章最后将这种吸引力与计算机科学领域联系起来，在这个领域中，解决“小”问题的个体方案会积累成重大的进步。

---

## 78. ThornWalli/web-workbench: 将旧操作系统作为主页

**原文标题**: ThornWalli/web-workbench: Old operating system as homepage

**原文链接**: [https://github.com/ThornWalli/web-workbench](https://github.com/ThornWalli/web-workbench)

ThornWalli 的 "web-workbench" 项目将一个交互式的、模拟的老式操作系统作为主页呈现。有两个可用实例：`https://lammpee.de/` 和测试版 `https://beta.lammpee.de/`。

该系统通过 GET 参数提供多种调试选项，以修改启动顺序和功能。这些选项包括禁用启动顺序 (`?no-boot`)、禁用 "WebDOS" 顺序 (`?no-webdos`)、禁用云存储 (`?no-cloud-storage`)、指定启动后要运行的初始命令 (`?start-command`) 以及显示软盘提示 (`?no-disk`)。一个示例展示了如何禁用启动和 WebDOS，同时自动启动 "Synthesizer" 应用程序。

模拟环境中提供了多个应用程序，可以使用 `?start-command` 参数直接启动。可用的应用程序及其对应 URL 的示例包括：Clock、Calculator、Cloud、DocumentEditor、DocumentReader、Say、Guestbook、WebPainting、WebBasic、Synthesizer 和 Moon City。每个应用程序的 URL 会在 workbench 环境初始化后预加载特定的应用程序。

---

## 79. iFixit称Switch 2比初代更难维修。

**原文标题**: iFixit says the Switch 2 is even harder to repair than the original

**原文链接**: [https://www.theverge.com/news/681568/ifixit-nintendo-switch-2-repairability](https://www.theverge.com/news/681568/ifixit-nintendo-switch-2-repairability)

iFixit拆解任天堂Switch 2，发现其维修难度甚至高于初代，维修评分仅为3分（满分10分）。主要问题包括电池被大量胶水固定、闪存模块和USB-C接口焊接在主板上，以及隐藏在易损贴纸下的Y字螺丝。虽然耳机接口和散热风扇等组件相对容易拆卸，但更换电池被描述为“一项艰巨的任务”。

一个显著的降级是游戏卡槽，现在被焊接到主板上，不像初代Switch的模块化设计。iFixit还强调使用了多种类型的散热硅脂，这引发了人们对初代Switch可能存在的过热问题的担忧。

即使是新的Joy-Cons手柄也更难拆卸，考虑到它们与初代手柄一样使用容易漂移的摇杆技术，这是一个主要问题。这将使未来的维修或摇杆更换更加困难。任天堂缺乏官方维修零件或手册进一步加剧了这个问题。

---

## 80. Cloudflare警告欧盟注意大规模盗版过度封锁，呼吁采取保护措施

**原文标题**: Cloudflare Warns EU About Extensive Piracy Overblocking, Calls for Safeguards

**原文链接**: [https://torrentfreak.com/cloudflare-warns-eu-about-extensive-piracy-overblocking-calls-for-safeguards/](https://torrentfreak.com/cloudflare-warns-eu-about-extensive-piracy-overblocking-calls-for-safeguards/)

Cloudflare警告欧盟勿扩大自动化盗版封锁措施，特别是针对体育赛事直播，称其会导致过度封锁，损害合法互联网用户和企业。欧盟委员会目前正在评估其打击网络盗版的建议，并考虑制定更有力的立法，以支持更先进的封锁系统。

Cloudflare强调了意大利、西班牙和法国的经验，这些国家的广泛封锁令导致了附带损害，影响了数千个非目标网站。该公司特别批评了意大利的“盗版盾牌”法律造成的大规模过度封锁，以及西班牙的广泛法院命令，阻止了数百万用户访问合法网站。Cloudflare认为，此类措施误解了互联网的运作方式，并可能违反欧盟法律。

Cloudflare敦促欧盟限制而非扩大封锁权力，特别是针对全球DNS解析器和VPN等核心互联网技术，这些技术用于保护隐私和自由表达。该公司倡导一种多方面的方法，侧重于透明度、保障措施和合作，包括优先考虑通知-移除程序、独立验证封锁请求、透明度报告、快速纠正不正确的封锁、独立争议解决，以及追究版权所有者对过度封锁后果的责任。Cloudflare认为，打击盗版需要数据共享、执法、行业合作以及改善合法内容的传播，而不是仅仅依靠可能造成损害的封锁措施。

---

## 81. 最高法院允许狗狗访问社保数据

**原文标题**: Supreme Court Gives Doge Access to Social Security Data

**原文链接**: [https://www.bloomberg.com/news/articles/2025-06-06/supreme-court-gives-doge-access-to-social-security-data](https://www.bloomberg.com/news/articles/2025-06-06/supreme-court-gives-doge-access-to-social-security-data)

无法访问文章链接。

---

## 82. 在线体育博彩：赢钱多了，就会限制你。

**原文标题**: Online sports betting: As you do well, they cut you off

**原文链接**: [https://doc.searls.com/2025/05/21/online-sports-betting-is-for-losers/](https://doc.searls.com/2025/05/21/online-sports-betting-is-for-losers/)

Doc Searls 的博文认为，在线体育博彩存在庄家作弊，最终让“庄家”获利，牺牲“输家”的利益。 他通过引用 ESPN、《华尔街日报》和《纽约邮报》的报道来支持这一观点，强调体育博彩公司如何限制或禁止成功的博彩者。 Searls 还引用了迈克尔·刘易斯的播客节目“违反规则”，该节目说明了体育博彩公司会多么迅速地切断开始赢钱的博彩者。

他还批评体育博彩公司更擅长识别有利可图的赌徒，而不是帮助问题赌徒，这表明这些平台旨在制造上瘾，尤其是在年轻人中。 虽然承认体育博彩公司需要盈利，但 Searls 认为他们对“休闲博彩者”的关注具有剥削性，因为他们本质上更喜欢那些乱花钱的人。

该博文最后预测，体育博彩最终会像吸烟和酒后驾车一样受到社会谴责。 评论部分强化了作者的观点，一位评论员将这种体验比作在赌场输钱，另一位评论员则认为在线博彩算法会利用天真的博彩者。

---

## 83. 通用科技树

**原文标题**: The Universal Tech Tree

**原文链接**: [https://asteriskmag.com/issues/10/the-universal-tech-tree](https://asteriskmag.com/issues/10/the-universal-tech-tree)

艾蒂安·福蒂埃-杜布瓦介绍了“通用科技树”项目，该项目旨在绘制技术的历史发展图谱，并揭示发明之间意想不到的联系。受《文明》系列电子游戏中科技树的启发，这个互动可视化工具将超过1550项技术置于时间线上，并根据影响和传承关系将它们连接起来。

文章以枪械和相机为例说明了这种相互关联性。艾蒂安-朱尔·马雷的“摄影枪”直接受到枪械的启发，而它的发展最终导致了电影摄影机的发明。这种联系可以追溯到柯尔特左轮手枪的旋转部件，这些部件本身就源于早期的枪械创新。

福蒂埃-杜布瓦概述了构建科技树的过程，其中包括将“技术”定义为在物理基质中实现的有意知识，将创新离散为具体的发明，并建立确定发明日期的规则。他主要使用维基百科和学术来源，同时优先建立自己的心智模型，而不是依赖于自动数据挖掘。

科技树揭示了一些令人惊讶的联系，例如自行车、汽车和摩托车于1885年同时被发明，以及无人机在动力飞行发明后不久的早期起源。它强调了一项发明如何出乎意料地导致其他发明，例如莱特兄弟的自行车业务影响了他们的飞机设计。最终，通用科技树为技术史提供了一个新的视角，揭示了隐藏的关系，并促使人们对创新有更深入的理解。

---

## 84. 特斯拉试图阻止奥斯汀市公开关于机器人出租车试验的记录

**原文标题**: Tesla seeks to block city of Austin from releasing records on robotaxi trial

**原文链接**: [https://www.reuters.com/business/autos-transportation/tesla-seeks-block-city-austin-releasing-records-robotaxi-trial-2025-06-06/](https://www.reuters.com/business/autos-transportation/tesla-seeks-block-city-austin-releasing-records-robotaxi-trial-2025-06-06/)

特斯拉正试图阻止德克萨斯州奥斯汀市公布与其计划于2025年进行的Robotaxi试验相关的文件。特斯拉辩称，被要求的记录包含专有信息和商业机密，如果公开，可能会为竞争对手提供显著优势并损害特斯拉的竞争地位。

该公司已在德克萨斯州州法院提起诉讼，试图阻止该市遵守一个匿名方提交的公共信息请求。特斯拉声称，这些文件详细说明了其自动驾驶技术的技术规格、性能数据和其他关键方面，包括支持Robotaxi功能的神经网络和软件。特斯拉认为，发布这些信息实际上会将该公司的研发成果拱手让给竞争对手。

此案凸显了政府运营透明度与保护敏感公司信息之间持续存在的紧张关系，尤其是在快速发展的自动驾驶汽车技术领域。特斯拉坚称，这些记录具有商业价值，并且披露它们将对公司造成无法弥补的损害。诉讼结果将决定奥斯汀市是否有义务公布这些文件，或者是否可以保护特斯拉声称的商业机密。除了特斯拉提起的诉讼之外，请求方和所请求文件的具体内容仍未公开。

---

## 85. 我向谷歌出卖灵魂的那个时代的末世故事

**原文标题**: Dystopian tales of that time when I sold out to Google

**原文链接**: [https://wordsmith.social/elilla/deep-in-mordor-where-the-shadows-lie-dystopian-stories-of-my-time-as-a-googler](https://wordsmith.social/elilla/deep-in-mordor-where-the-shadows-lie-dystopian-stories-of-my-time-as-a-googler)

在这篇博文中，作者回忆了2007年在巴西谷歌工作时令人失望的经历，突显了该公司作为“最佳工作场所”的形象与实际工作环境之间的差异。谷歌承诺提供“20%时间”用于个人项目等福利，但作者发现自己过度劳累地修复bug，并面临无偿加班的压力。

他们试图通过一篇内部博文来解决“20%时间”未被充分利用的问题，却受到了训斥，因为表达不满被视为“背后捅刀”。他们还描述了创建一个机器人来为新员工定义公司术语，结果导致该词汇表对临时工、兼职员工和合同工进行了限制，从而导致他们的处境更加糟糕。

作者回忆了另一个例子，一位Android项目程序员最初对项目的方向表示失望，但后来撤回了他的声明，暗示他面临着保持积极形象的压力。作为一名公开的酷儿员工（“Gaygler”），作者还被AdSense团队联系，要求为广告提供俚语和文化参考，这让他们感到被利用。

作者强调了工程师和“谷歌无产阶级”（临时工、兼职员工和合同工）之间的鸿沟，指出虽然工程师获得了免费零食和玩具等福利，但他们的薪水仍然偏低，并且面临着压力。该公司利用全球北方高薪机会的幻想来保持员工的积极性，尽管工作条件恶劣。这造成了一种局面，即工程师受到肤浅的好处的宠爱，而无产阶级则被视为低人一等。

---

## 86. 以太：一款让你轻松使用的内容管理系统

**原文标题**: Aether: A CMS That Gets Out of Your Way

**原文链接**: [https://lebcit.github.io/post/meet-aether-a-cms-that-actually-gets-out-of-your-way/](https://lebcit.github.io/post/meet-aether-a-cms-that-actually-gets-out-of-your-way/)

Aether CMS：快速、极简、模块化的内容管理系统。基于实际开发经验构建，Aether致力于解决WordPress等平台臃肿和诸多JAMstack工具复杂性的问题，仅通过四个核心模块实现。

Aether提倡“文件优于数据库”的理念，将内容存储为带有YAML frontmatter的Markdown文件，保证内容的可移植性和版本控制。这种方式提高了开发速度、内容创建速度（通过熟悉的管理界面）和运行时速度（通过静态站点生成）。

主题是简单的HTML、CSS和JavaScript文件夹，采用LiteNode的Simple Template Engine。Aether的设计适用于各种用例，包括个人博客、公司文档、营销网站、多作者出版物和作品集网站，无需插件或大量配置。

Aether旨在成为一个无损的解决方案——对内容创作者来说简单，对开发者来说灵活，对用户来说快速。它基于Node.js和原生JavaScript构建，利用LiteNode、Marked、基于文件的存储和Argon2。通过简单的CLI命令即可快速上手。

未来的开发计划包括定时发布、搜索功能、高级用户权限、页面缓存、插件系统扩展、评论系统、SEO工具、编辑器增强和新主题。文章最后邀请用户尝试Aether，并强调其基于文件的特性避免了供应商锁定。

---

## 87. LongCodeBench：百万窗口规模下编码LLM的评估

**原文标题**: LongCodeBench: Evaluating Coding LLMs at 1M Context Windows

**原文链接**: [https://arxiv.org/abs/2505.07897](https://arxiv.org/abs/2505.07897)

该arXiv文章于2025年5月12日提交，介绍了LongCodeBench (LCB)，这是一个新的基准，旨在评估具有极长上下文窗口（高达100万个token）的大型语言模型（LLM）的编码能力。由Stefano Rando领导的作者认为，代码理解和修复是评估这些模型在真实的、长上下文场景中能力的合适任务。

LCB借鉴了真实世界的GitHub问题，创建了两种任务类型：LongCodeQA（问答）和LongSWE-Bench（错误修复）。该基准经过精心分层，按复杂性划分，从而可以评估各种模型，从较小的模型（如Qwen2.5 14B Instruct）到较大的模型（如Google的Gemini）。

该研究的发现表明，长上下文性能仍然是所有测试模型的显著弱点。结果突显了性能下降，例如Claude 3.5 Sonnet从29%降至3%，Qwen2.5从70.2%降至40%，这表明LLM在处理非常长的代码上下文时面临挑战。该研究强调，需要持续改进LLM有效利用和理解广泛上下文窗口内信息以完成编码任务的能力。

---

## 88. Terraform模块的用例：扩展您的基础设施组织

**原文标题**: The Case for Terraform Modules: Scaling Your Infrastructure Organization

**原文链接**: [https://infisical.com/blog/terraform-modules-organization-scaling](https://infisical.com/blog/terraform-modules-organization-scaling)

Terraform 模块是高效扩展基础设施组织的关键。初期团队常重复 Terraform 代码，导致技术债务。模块通过将基础设施模式封装为可重用、版本控制的组件来解决此问题。优点包括标准化配置、减少配置漂移和前瞻性基础设施设计。

本文探讨了不同的模块方法：本地、Git 托管和注册表托管。本地模块适用于早期开发，而 Git 托管模块支持跨项目共享和版本锁定。对于大型复杂的基础设施，TACOS 平台内的私有模块注册表可提供结构化版本控制、自动化和治理。

一个关键考虑因素是构建自定义模块还是利用公共社区注册表。内部模块通常更安全，但需要更多开发工作。外部模块提供现成的解决方案，但需要仔细的安全审查，并可能引入不必要的复杂性。

本文强调了模块中管理密钥的挑战，并建议使用 Infisical，一种与 Terraform 无缝集成的密钥管理解决方案。Infisical 利用临时资源来防止密钥存储在状态文件中，从而实现安全的凭证轮换和灵活、可重用的模块。

总之，本文强调，随着基础设施的扩展，结构化的模块管理、版本控制和自动化对于保持一致性并避免基础设施代码中的陷阱至关重要。

---

## 89. 展示 HN: Lambduck，一种函数式编程 Brainfuck

**原文标题**: Show HN: Lambduck, a Functional Programming Brainfuck

**原文链接**: [https://imjakingit.github.io/lambduck/](https://imjakingit.github.io/lambduck/)

Lambduck是一种基于lambda演算原理并深受Brainfuck启发的函数式编程语言。它使用极简的语法，仅包含少量字符：`\`、`|`、`-`、`+`和`*`，分别代表lambda抽象、函数应用和参数访问等核心函数式构造。

该语言是急求值的（最左-最内求值顺序），并为I/O提供了特定的构造。顶层程序接收一个Church编码的`getchar`（从stdin读取一个字节，并使用Church数码表示调用其参数）和`putchar`（解码Church数码模256，将其写入stdout，并返回原始数码）的pair。程序在成功求值或`getchar`遇到EOF时终止。

文档提供了一个表格，概述了Lambduck中每个字符的含义。然后，它展示了几个示例函数（true、false、identity、pair、fst、snd、left、right、either、ap、fix），并演示了两个简单的示例程序：“echo”，用于回显输入，以及一个打印“@”字符的程序。该程序强调函数式编程原则，并利用Church数码进行数据表示和操作。

---

## 90. 从词元到思想：大型语言模型与人类如何以压缩换取意义

**原文标题**: From tokens to thoughts: How LLMs and humans trade compression for meaning

**原文链接**: [https://arxiv.org/abs/2505.17117](https://arxiv.org/abs/2505.17117)

从词元到思想：大型语言模型与人类如何以压缩换取意义

---

## 91. CRDTs #4: 收敛性、确定性、下界和膨胀

**原文标题**: CRDTs #4: Convergence, Determinism, Lower Bounds and Inflation

**原文链接**: [https://jhellerstein.github.io/blog/crdt-inflationary/](https://jhellerstein.github.io/blog/crdt-inflationary/)

本文深入探讨了CRDT（无冲突复制数据类型）设计的微妙而关键的方面，重点关注确定性、收敛性以及更新函数性质之间的关系。它强调了CRDT中的强最终一致性(SEC)并不必然保证确定性。具体而言，如果CRDT要具有确定性，或者如果读取要被视为下界，则更新函数必须是膨胀性的。

作者定义了诸如并半格和膨胀函数等关键术语，强调虽然CRDT中的合并操作本质上是膨胀性的，但更新函数可能会引入非确定性。当更新不是膨胀性的时，这种非确定性就会出现，可能导致基于更新和消息的交错的不同收敛状态。

本文通过示例证明，非膨胀性更新会破坏CRDT读取的下界属性，从而使得依赖中间值作为稳定观察变得不安全。为了确保膨胀性，作者建议要么修改更新API，将更新结果与当前状态合并，要么完全删除更新API，强制开发人员显式处理合并。

最后，本文阐明了单调性在此上下文中的相关性，表明虽然它通常是一个重要的属性，但膨胀性是实现CRDT中确定性收敛的关键要求。

---

## 92. 开源蒸馏

**原文标题**: Open Source Distilling

**原文链接**: [https://opensourcedistilling.com/](https://opensourcedistilling.com/)

本文题为《开源蒸馏》，重点介绍iSpindel及其组件，特别是“The Jeffrey 2.69”。文章着重介绍了一个视频演示，涵盖了使用该技术的关键方面。视频内容包括：

*   **The Jeffrey 2.69：** 展示与此特定版本的iSpindel组件相关的新功能。
*   **平面焊接技术：** 指导如何进行平面焊接，这是一种可能与组装或修改iSpindel相关的特定焊接方法。
*   **平衡方法：** 详细介绍了一种将iSpindel平衡至25度角的新方法。该方法涉及使用焊盘配重来实现所需的平衡。

总而言之，本文指向一个资源（视频），该资源提供了关于使用、焊接和平衡iSpindel设备的实用指导和演示，重点介绍了“The Jeffrey 2.69”版本的功能。使用焊盘配重进行平衡的方法被提出作为一种新颖的技术。

---

## 93. HZ程序 (赫尔曼·察普夫排版算法)

**原文标题**: HZ-program (Typesetting algorithm by Hermann Zapf)

**原文链接**: [https://en.wikipedia.org/wiki/Hz-program](https://en.wikipedia.org/wiki/Hz-program)

Hz程序，由赫尔曼·察普夫创建，是一项获得专利的排版合成计算机程序，旨在通过最大限度地减少多余的字间距来产生均匀的文本对齐效果。察普夫的目标是创造一个没有“河流和孔洞”的“完美的灰色文字区域”。

该程序的开发横跨哈佛大学至罗切斯特理工学院。算法的关键要素包括缩放（压缩和扩展）字母以及快速字距调整程序。该程序可以对字符之间的间距进行负向和正向调整。

URW对Hz程序进行了专利注册；该专利现已过期。Adobe Systems后来收购了该程序，用于Adobe InDesign中。虽然尚不清楚该算法是否仍在当前版本的InDesign中使用，但Hàn Thế Thành对其进行了详细分析，从而在TeX排版系统（pdfTeX）中实现了微排版扩展，这些扩展可在LaTeX和ConTeXt中使用。

该程序的质量以及围绕其内部运作方式的模糊性导致了一定程度的神秘感。将其输出与古登堡作品质量相提并论的主张也引发了争议，尤其是在字形缩放技术方面。一些排版师，例如Ari Rafaeli和Torbjørn Eng，表达了批评，并质疑了与古登堡的比较。

---

## 94. 展示一下：Claude Composer

**原文标题**: Show HN: Claude Composer

**原文链接**: [https://github.com/possibilities/claude-composer](https://github.com/possibilities/claude-composer)

Claude Composer：通过自动化权限对话框处理、管理Claude的工具访问权限以及通过系统通知提供更好的可见性来增强Claude Code体验的工具。它基于可配置的规则集自动处理权限提示，减少中断，并灵活控制Claude允许执行的操作。它还通过定义指定Claude可以使用的工具集的工具集来启用工具管理。

该工具可以使用`npm`、`yarn`或`pnpm`全局安装。配置通过`claude-composer cc-init`初始化，允许全局或项目特定的配置。`config.yaml`文件允许用户定义规则集、工具集、受信任的项目根目录和通知首选项。

Claude Composer提供了各种命令行选项，用于指定规则集和工具集、控制通知显示、启用调试功能和管理安全设置。诸如`cc-init`之类的子命令提供了使用特定规则集或工具集初始化配置的选项。它还支持将无法识别的选项直接传递给Claude Code。该工具利用环境变量进行进一步配置。可以定义受信任的根目录，以便自动接受指定目录的信任提示。最后，本文档概述了不同类型更新的发布流程。

---

## 95. Dino编程语言及其实现

**原文标题**: Programming language Dino and its implementation

**原文链接**: [https://github.com/dino-lang/dino](https://github.com/dino-lang/dino)

Dino编程语言是一种高级的、脚本的、面向对象的语言，目前正在开发中（版本 0.98）。它从 C 语言中汲取灵感，但融入了诸如多精度整数、异构数组、关联表、强大的类组合、一等函数、并发、模式匹配和 Unicode 支持等特性。它旨在实现安全性和效率，利用数组切片和哈希表作为数据结构。

Dino 的实现强调性能。它具有带优化的字节码编译器（死代码消除、跳转优化、内联）、带有垃圾回收器（标记清除/标记复制）的快速优化解释器以及函数级 JIT 编译器。类型推断用于专门化字节码指令以进一步加速。通过绿色线程实现并发，承诺确定性行为和死锁检测，并计划支持操作系统线程以实现并行性。

通过类组合支持面向对象，提供继承和特征。模式匹配简化了代码结构，而正则表达式匹配则通过 `rmatch` 语句提供。异常处理通过 `try-catch` 块支持。该语言包含一个内置的 Earley 解析器 (YAEP)，用于快速语言原型设计。

Dino 使用 COCOM 工具（SPRUT、MSTA、SHILKA、AMMUNITION）、GMP（用于多精度整数）和 Oniguruma（用于正则表达式）构建。该文档预计会与 Python、PyPy、Ruby、JS、Scala 和 OCaml 进行性能比较。

---

## 96. Mixtela精密时钟MkIV

**原文标题**: Mixtela Precision Clock MkIV

**原文链接**: [https://mitxela.com/shop/clock4](https://mitxela.com/shop/clock4)

Mixtela精密时钟Mk IV是一款通过GPS同步的高精度挂钟，具有毫秒显示功能，可自动调节亮度，即使在高速拍摄时也能避免闪烁。其独特之处在于其精度绑定显示：如果GPS信号丢失且时间漂移，最低有效位数字将会消失，直到重新同步。

该时钟通过利用内置的世界地图和时区数据库以及GPS坐标，自动确定正确的当地时间，包括夏令时。这些数据库的更新可以通过USB端口以拖放方式轻松完成，该端口显示为大容量存储设备。

它提供多种显示模式，如ISO-序数、ISO-周、Unix时间戳、儒略日，以及高精度倒计时模式，未来固件更新可能会增加更多模式，同样通过USB传送。

该时钟可以对折以实现紧凑性，顶部显示屏自动旋转，由磁铁固定。展开时，宽度为53厘米（21英寸）；折叠时，宽度为27厘米（10.5英寸），高度为7厘米（3英寸）。

它以套件形式（表面贴装元件预先焊接）的售价为250英镑，完全组装的售价为350英镑。由于需求量大，该时钟目前缺货，潜在买家可以注册邮件通知，以便在有更多产品可用时收到通知。时钟从英国发货，国际订单可能需要缴纳进口关税。

---

## 97. Show HN: 通过 REST API 获取 iOS 屏幕使用时间

**原文标题**: Show HN: iOS Screen Time from a REST API

**原文链接**: [https://www.thescreentimenetwork.com/api/](https://www.thescreentimenetwork.com/api/)

此“Show HN”帖子介绍“屏幕时间网络”，一个通过REST API提供iOS屏幕时间数据访问的项目。主要亮点是该API使开发者（或潜在的高级用户）能够以编程方式访问和分析由iOS设备收集的屏幕时间数据。

该帖子很可能旨在展示提取这些数据并通过标准API以结构化格式提供数据的可行性。 这可能具有多种潜在应用，例如：

*   **家长控制和监控：** 与现有家长控制应用程序集成或创建新的应用程序。
*   **个人分析和自我提升：** 跟踪和分析自己的屏幕时间习惯，以识别模式并设定目标。
*   **研究和开发：** 为数字健康、成瘾以及屏幕时间对不同人群影响的研究提供数据。
*   **与其他服务集成：** 将屏幕时间数据连接到其他平台，以实现全面的数字生活管理。

本质上，该项目提供了一种突破Apple屏幕时间实施的围墙花园的方式，并以更灵活和潜在创新的方式使用数据。 虽然帖子本身没有详细说明实现或具体的API端点，但它作为公告和邀请，旨在与Hacker News社区进行讨论和潜在的协作。 它暗示该项目可能是开源的，或者具有一定程度的开放性，供其他人在此基础上进行构建。

---

## 98. Tokasaurus：一种用于高吞吐量工作负载的LLM推理引擎

**原文标题**: Tokasaurus: An LLM inference engine for high-throughput workloads

**原文链接**: [https://scalingintelligence.stanford.edu/blogs/tokasaurus/](https://scalingintelligence.stanford.edu/blogs/tokasaurus/)

Tokasaurus：一款新型LLM推理引擎，专为高吞吐量工作负载设计，在某些基准测试中性能超越现有引擎vLLM和SGLang高达3倍以上。它针对大小模型进行了优化，旨在高效处理批量任务，而非单个请求延迟。

对于小型模型，Tokasaurus采用自适应异步管理器，最大限度减少CPU开销，优先保持GPU繁忙。它还采用贪婪深度优先搜索算法进行动态前缀识别，以利用序列中的共享前缀，这对于重复采样等工作负载尤其有利。

对于大型模型，Tokasaurus利用流水线并行 (PP) 技术，显著提升无NVLink GPU的吞吐量，优于vLLM和SGLang。它还支持带NVLink GPU的异步张量并行 (Async-TP)，并在大批量情况下动态启用，以最大限度地重叠通信并提高性能。

该引擎用Python编写，支持具有数据并行、张量并行和流水线并行的Llama-3和Qwen-2模型。用户可以通过pip安装。作者在GitHub上提供了基准测试详情和代码，以确保可复现性。他们感谢Prime Intellect和Together AI提供的计算资源，以及beta测试者提供的反馈。

---

## 99. 垃圾站七日

**原文标题**: Seven Days at the Bin Store

**原文链接**: [https://defector.com/seven-days-at-the-bin-store](https://defector.com/seven-days-at-the-bin-store)

Jen Kinney的文章《垃圾箱商店七日记》探索了位于西费城的折扣店Amazing Binz，该店出售沃尔玛、亚马逊和塔吉特等大型零售商的积压商品和退货商品。该商店采用每日降价模式，周五补货后起价为10美元，周三降至1美元。

Kinney花了一周时间观察这家商店，从周四的补货开始，店主Ahmed收到一卡车未分类的商品，凸显了由不断增长的在线退货和积压仓库推动的日益壮大的“逆向物流”行业。她观察到周五开业时场面火爆，吸引了寻求以低价购买有价值商品的廉价商品爱好者和经销商。

这篇文章还探讨了当地居民对Amazing Binz的反应。一些居民对低廉的价格和转售商品的机会感到兴奋，而另一些居民则对商店对社区特色和消费主义伦理的影响表示担忧。一些人认为这家商店是晚期资本主义的症状，是无用消费品最终可能进入垃圾填埋场的渠道。

最终，这篇文章描绘了一幅关于Amazing Binz的复杂图景，它既受益于又促进了过度消费和浪费的循环，同时又为社区中的一些人提供了负担得起的商品和潜在的收入机会。该商店位于士绅化和各种意见的背景下，使其成为更大经济和社会趋势的缩影。

---

## 100. 十一 v3

**原文标题**: Eleven v3

**原文链接**: [https://elevenlabs.io/v3](https://elevenlabs.io/v3)

Eleven v3 (alpha) 是 ElevenLabs 迄今为止最具表现力的文本转语音 (TTS) 模型，通过内联音频标签提供广泛的动态范围控制，以增加情感、音频事件和沉浸式声景。 它支持多个说话者之间的动态对话，共享上下文和情感，从而实现听起来自然的对话。 该模型支持 70 多种语言的类人语音，使用户能够覆盖全球受众。

主要功能包括支持使用音频标签来控制情感、表达和方向，生成动态的多说话者对话的能力，以及支持广泛的情感、方向和音频效果。

在 2025 年 6 月底之前，自助服务用户可以通过 UI 享受 8 折优惠使用 alpha 版本。 网站上的音频样本完全由 Eleven v3 生成。 对话生成将多个声音融合在一起，匹配韵律和情感范围。 公共 API 访问即将推出，通过联系销售人员可以获得早期访问权限。 支持多种音频标签。 本文包含所有支持语言的列表。

---

