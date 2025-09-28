# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-28.md)

*最后自动更新时间: 2025-09-28 17:43:25*
## 1. 人工智能编码陷阱

**原文标题**: The AI coding trap

**原文链接**: [https://chrisloy.dev/post/2025/09/28/the-ai-coding-trap](https://chrisloy.dev/post/2025/09/28/the-ai-coding-trap)

本文认为，虽然像Claude Code这样的人工智能编码代理可以显著加快代码生成速度，但它们也可能适得其反地阻碍整体软件开发效率。作者将这种现象称为“AI编码陷阱”，将“快10倍”的代码生成承诺与现实世界软件交付中看到的边际收益进行了对比。

核心问题在于，人工智能擅长独立生成代码，但在复杂系统的更广泛环境中却显得力不从心。这导致工程师花费更多时间理解和修复人工智能生成的代码，这项任务掩盖了编码的乐趣和创新方面。 这也与“技术主管的困境”类似，即经验丰富的领导者优先考虑个人速度而非团队成长，霸占最具挑战性的任务。

文章提出，最好将人工智能编码代理视为“速度极快的初级工程师”。为了避免陷入陷阱，作者倡导采用传统软件开发的最佳实践，并将人工智能视为增强而非取代人类工程师的工具。 解决方案是将人工智能集成到软件开发生命周期的每个阶段，从规范和文档到模块化设计、测试驱动开发、编码标准和监控。 这需要将重点从简单地更快地编写代码转变为构建可维护、可扩展的系统，从而受益于人类和人工智能的优势。 最终，通过将人工智能代理视为需要指导和结构的初级工程师，我们可以释放他们的潜力，并扩大我们交付可工作软件的能力。

---

## 2. 隐私獾是由 EFF 开发的一款免费浏览器扩展，旨在阻止跟踪监视。

**原文标题**: Privacy Badger is a free browser extension made by EFF to stop spying

**原文链接**: [https://privacybadger.org/](https://privacybadger.org/)

Privacy Badger，一款由 EFF 提供的免费浏览器扩展，可自动阻止公司在线跟踪您。它与传统的广告拦截器不同，专注于隐私，仅当广告跟踪您时才会阻止广告。它使用算法而非人工编辑的列表，根据跟踪器的行为而非预定义的列表来识别和阻止跟踪器。

Privacy Badger 会学习阻止跨多个网站跟踪用户的域名，尤其是在这些域名忽略“请勿跟踪”(DNT) 和“全局隐私控制”(GPC) 信号时。它可以阻止第三方跟踪器，还可以删除 Facebook 和 Google 上的外部链接点击跟踪。Privacy Badger 菜单中的红色滑块表示完全禁止的内容，黄色表示阻止 Cookie，绿色表示不采取任何操作。

该扩展旨在通过阻止不尊重用户隐私的广告商来激励他们尊重用户隐私。通过发送 GPC 和 DNT 信号，Privacy Badger 请求公司尊重您的隐私，并通过阻止不合规的跟踪器来强制执行此要求。它会分析 Cookie，阻止具有唯一跟踪 ID 的 Cookie，同时允许具有低熵值的 Cookie，例如语言偏好。

Privacy Badger 由电子前哨基金会 (Electronic Frontier Foundation) 开发，适用于 Chrome、Firefox、Edge 和 Opera。为了避免被阻止，域名应尊重 DNT 和 GPC 信号。域名也可以在其网站上发布 EFF 的 DNT 政策，作为遵守承诺。

---

## 3. 我说“字母顺序”的时候，我指的就是“字母顺序”。

**原文标题**: When I say "alphabetical order", I mean "alphabetical order"

**原文链接**: [https://sebastiano.tronto.net/blog/2025-09-28-alphabetic-order/](https://sebastiano.tronto.net/blog/2025-09-28-alphabetic-order/)

作者叙述了一段令人沮丧的经历：以时间戳命名（IMG_YYYYMMDD_HHmmss）的文件在各种操作系统和文件管理器（Windows、Google Drive、KDE Dolphin、Gnome、手机文件管理器）中无法按字母顺序正确排序。他们原本期望按字母顺序排序的结果应等于按时间顺序排列，因为命名约定如此。

问题产生的原因是作者和其父亲的安卓手机拍摄的文件混合在一起，作者的所有文件都显示在前面，即使其中一些文件的时间戳晚于父亲的文件。起初，作者怀疑是漏洞或不同的字符编码。然而，Linux中的`ls -l`命令可以正确地对文件进行排序。

问题根源在于文件管理器采用了“自然排序”算法。该算法将文件名中的数字序列视为数字，而不仅仅是字符。因此，"file-9.txt"会如人们期望的那样排在"file-10.txt"之前，但这并非真正的字母排序。

作者的手机在文件名中包含一个额外的下划线分隔秒和毫秒（"IMG_YYYYMMDD_HHmmss_mmm.jpg"），而父亲的手机没有（"IMG_YYYYMMDD_HHmmssmmm.jpg"）。由于文件管理器采用了“自然排序”，作者手机的文件根据时间戳正确排序，而父亲手机的文件则被视为结尾处具有更高的数字，因此被放置在最前面。

作者最后感叹软件“揣测人心”并偏离严格、字面意义上的用户指令的趋势，并表达了希望计算机简单地执行指令的愿望。

---

## 4. 我为什么不急于在RubyGems风波中站队

**原文标题**: Why I'm not rushing to take sides in the RubyGems fiasco

**原文链接**: [https://justin.searls.co/posts/why-im-not-rushing-to-take-sides-in-the-rubygems-fiasco/](https://justin.searls.co/posts/why-im-not-rushing-to-take-sides-in-the-rubygems-fiasco/)

本文解释了作者为何对 2025 年 RubyGems 争议持谨慎态度，不愿轻易站队。他认为目前的公开叙述过于片面，源于 Ruby 生态系统中关键人物之间未解决的冲突，主要涉及 Andre Arko 和 Ruby Central。

作者详细阐述了对 Ruby Together 的担忧，这是一个由 Arko 创立的旨在资助开源开发的非营利组织，后来被 Ruby Central 吸收。他叙述了一些故事和事件，暗示可能存在资金滥用和利用对 Bundler（一个关键的 Ruby 依赖管理器）的控制来获取经济利益的行为。这些包括关于误导捐助者资金分配、提议限制 RubyGems.org 访问除非公司向 Ruby Together 付费、以及公开羞辱像 Shopify 这样的公司不赞助该组织的指控。

作者重点介绍了泄露的 Ruby Together 董事会会议，会议讨论了包括限制 RubyGems.org 访问在内的创收策略。他还提到了公众对 Arko 添加“安装后消息”敦促用户资助 Ruby Together 的强烈反对。Ruby Central 后来澄清说，Ruby Together 的筹款活动与 RubyGems.org 的运营成本是分开的。

最后，作者回忆了一个案例，Arko 指责 Google 抄袭代码并威胁采取法律行动，同时抱怨 Google 未能资助 Ruby Together，但最终证实这是毫无根据的。作者将这种过去的行径与最近的行动联系起来。

作者总结说，虽然 Ruby Central 对当前情况的处理存在问题，但历史背景以及对 Arko 过去行为的担忧使他对当前事件的简单“善与恶”的解读持谨慎态度。

---

## 5. 测试“异构”P2P VPN

**原文标题**: Testing "Exotic" P2P VPN

**原文链接**: [https://blog.nommy.moe/blog/exotic-mesh-vpn/](https://blog.nommy.moe/blog/exotic-mesh-vpn/)

本文详细介绍了作者对 Wireguard 的替代 P2P VPN 解决方案的探索，起因是 Wireguard 在特定国家/地区受到封锁，以及对更去中心化、自托管和符合意识形态的解决方案的渴望。 作者测试了 EasyTier、Nebula 和 Tinc，并根据易用性、安全性、性能以及与 Nix 打包的兼容性对它们进行了评估。

EasyTier 因其简单性以及通过各种协议（TCP、UDP、WG、WS、WSS）自动建立连接而受到赞扬。 然而，它缺乏 IP 绑定，并且由于其中国血统而引起了意识形态方面的担忧。 来自 Slack 创始人的 Nebula 提供了更多的安全功能，如椭圆曲线加密和其自身的 PKI，但其基于 SSH 的配置笨拙，性能令人失望。 Tinc 是一个较旧的项目，出人意料地表现良好，利用其自身基于 UDP 的协议、椭圆曲线以及记录在案的用于直接节点到节点通信的“黑魔法”。

作者概述了一种测量方法，包括 ICMP ping、使用 /dev/zero 的 SSH 数据传输、Wget 下载以及 IPerf2 和 IPerf3 测试，并承认 IPerf 可能存在不准确之处。 测试是在一台家用笔记本电脑、一台公共 Lighthouse 服务器和一台位于防火墙后面的 Raspberry Pi 上进行的。

结果表明，Tinc 在速度方面提供了最佳性能，而 EasyTier 鉴于其临时性质，被认为是可接受的。 Nebula 的性能被认为令人失望。 尽管存在缺陷，作者计划使用所有三个 VPN，这表明多 VPN 方法优于仅依赖一个解决方案。

---

## 6. 超微服务器主板可能感染无法移除的恶意软件

**原文标题**: Supermicro server motherboards can be infected with unremovable malware

**原文链接**: [https://arstechnica.com/security/2025/09/supermicro-server-motherboards-can-be-infected-with-unremovable-malware/](https://arstechnica.com/security/2025/09/supermicro-server-motherboards-can-be-infected-with-unremovable-malware/)

Supermicro服务器主板存在关键漏洞，攻击者可在操作系统启动前安装持久性、无法检测的恶意软件。安全公司Binarly发现，先前已知漏洞 (CVE-2024-10237) 的不完整补丁仍然可以被利用。他们还发现了新的漏洞 (CVE-2025-7937 和 CVE-2025-6198)。

这些缺陷存在于基板管理控制器 (BMC) 中，该控制器控制远程服务器管理功能并允许重新刷新 UEFI 固件。攻击者可以利用这些漏洞用恶意版本替换合法的固件，绕过安全检查。这提供了“前所未有的持久性”，可能导致数据破坏或供应链攻击，其中固件更新服务器被入侵。

利用需要事先获得对 BMC 的管理访问权限或入侵固件更新服务器。这些漏洞允许攻击者操纵“fwmap 表”以将恶意代码注入到引导加载程序中。

Supermicro 声称已更新 BMC 固件以解决此问题，并建议客户查看发行说明，但 Binarly 报告称更新后的固件尚未公开提供。修复的困难性表明 Supermicro 可能需要更多时间才能完全解决这些漏洞。

---

## 7. Show HN: Toolbrew – 无需注册或广告的免费小工具集

**原文标题**: Show HN: Toolbrew – Free little tools without signups or ads

**原文链接**: [https://toolbrew.co/](https://toolbrew.co/)

Toolbrew是一个提供免费且实用在线工具的网站。其主要卖点是这些工具干净（可能意味着简单易用），且无需用户注册账号或被大量广告轰炸即可使用。核心理念是提供一个易于访问和使用便捷的实用工具库，通过消除强制注册和干扰性广告等在线工具使用中的常见问题，来优先考虑用户体验。

---

## 8. 猪肾移植六个月后男子仍然存活

**原文标题**: Man still alive six months after pig kidney transplant

**原文链接**: [https://www.nature.com/articles/d41586-025-02851-w](https://www.nature.com/articles/d41586-025-02851-w)

一位67岁的男子蒂姆·安德鲁斯，患有终末期肾病，在今年一月接受基因改造猪肾后，存活至今已超过六个月。这标志着异种移植领域的一个重要里程碑，也是猪器官在活人体内存活时间最长的一次。安德鲁斯此前已透析两年多，现在已无需透析。

该肾脏来自一头经过三种基因改造的猪：去除三种抗原以防止排异，添加七个人类基因以降低炎症和出血风险，以及灭活逆转录病毒。安德鲁斯是eGenesis公司出于同情考虑，进行此类移植的三名患者之一。

专家认为达到六个月是一个重大成功，因为这是发生贫血和移植排斥等并发症风险最高的时期。此前，接受者托瓦娜·卢尼的猪肾功能正常维持了四个多月，但最终因排异而被移除。达到12个月将是另一个重要的成就。该案例的成功为异种移植作为解决器官短缺的方案带来了希望。

---

## 9. Show HN: 用 Cloudflare 代码模式模式构建了一个 MCP 服务器

**原文标题**: Show HN: Built an MCP server using Cloudflare's Code Mode pattern

**原文链接**: [https://github.com/jx-codes/codemode-mcp](https://github.com/jx-codes/codemode-mcp)

此“Show HN”帖子介绍了一个受 Cloudflare Code Mode 启发的 MCP（模型上下文协议）服务器实现，旨在改进 LLM 与 MCP 的交互。该方法没有依赖直接工具调用，而是通过提供一个 `execute_code` 工具，利用 LLM 的编码能力。该工具执行 TypeScript/JavaScript 代码，与本地 HTTP 代理交互，然后将请求转发到实际的 MCP 服务器。

主要优势在于，LLM 更擅长编写代码而不是直接使用工具，从而可以实现更复杂的编排和操作链。该设置涉及安装 Bun 和 Deno，使用 `codemode-config.json` 配置服务器，并在 `.mcp.json` 文件中定义 MCP 服务器配置。

服务器提供用于列出服务器、工具和调用工具的代理端点。示例工作流程演示了单个 MCP 服务器调用以及使用已执行代码中的 `fetch` 进行的链式操作。通过 Deno 沙箱确保安全性，该沙箱限制通过代理进行网络通信的访问、30 秒的执行超时以及自动临时文件清理。该帖子还包括故障排除技巧和潜在的未来改进，例如更简单的 API 和更多的配置选项。该代码基于来自一个单独项目的 Deno remix，旨在利用编写代码而不是依赖直接工具调用所带来的组合优势。

---

## 10. C++和Rust中OpenMP之外的选择：Taskflow、Rayon、Fork Union

**原文标题**: Beyond OpenMP in C++ and Rust: Taskflow, Rayon, Fork Union

**原文链接**: [https://ashvardanian.com/posts/beyond-openmp-in-cpp-rust/](https://ashvardanian.com/posts/beyond-openmp-in-cpp-rust/)

本文指出，许多流行的C++和Rust线程池库，如Taskflow和Rayon，在fork-join并行工作负载下的性能远低于OpenMP，通常差一个数量级。这归因于“低性能的四大杀手”：锁和互斥锁、堆分配、比较并交换停顿以及伪共享。

为了解决这个问题，作者介绍了Fork Union，一个仅使用标准库特性且代码极简（300行）的库，其性能可达到OpenMP的80%。基准测试表明，与Taskflow、Rayon、Tokio，甚至直接使用`std::thread`相比，Fork Union具有更优越的性能。关键在于，对于简单的并行规约，应避免异步任务队列及其相关开销。

本文进一步阐述了锁、内存分配、原子操作和伪共享的性能陷阱。虽然承认Rayon和Taskflow等库的高级功能，但文章强调了选择正确工具的重要性。Fork Union提供了一个更简单的API，专注于fork-join并行，包括`for_each_thread`、`for_each_static`、`for_each_slice`和`for_each_dynamic`。文章的结论是，无论使用何种语言，避免互斥锁、动态队列、CAS操作和伪共享对于在并行计算中实现高性能至关重要。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 2 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 3 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 4 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 5 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 6 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 7 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 8 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 9 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 10 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 11 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 12 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 13 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 14 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 15 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 16 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 17 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 18 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 19 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 20 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 21 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 22 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 23 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 24 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 25 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 26 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 27 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 28 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 29 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 30 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 31 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 32 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 33 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 34 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 35 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 36 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 37 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 38 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 39 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 40 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 41 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 42 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 43 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 44 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 45 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 46 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 47 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 48 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 49 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 50 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 51 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 52 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 53 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 54 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 55 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 56 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 57 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 58 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 59 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 60 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 61 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 62 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 63 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 64 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 65 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 66 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 67 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 68 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 69 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 70 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 71 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 72 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 73 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 74 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 75 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 76 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 77 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 78 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 79 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 80 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 81 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 82 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 83 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 84 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 85 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 86 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 87 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 88 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 89 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 90 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 91 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 92 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 93 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 94 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 95 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 96 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 97 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 98 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 99 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 100 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 101 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 102 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 103 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 104 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 105 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 106 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 107 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 108 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 109 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 110 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 111 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 112 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 113 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 114 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 115 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 116 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 117 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 118 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 119 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 120 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 121 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 122 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 123 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 124 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 125 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 126 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 127 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 128 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 129 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 130 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 131 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 132 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 133 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 134 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 135 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 136 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 137 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 138 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 139 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 140 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 141 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 142 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 143 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 144 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 145 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 146 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 147 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 148 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 149 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 150 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 151 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 152 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 153 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 154 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 155 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 156 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 157 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 158 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 159 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 160 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 161 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 162 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 163 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 164 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 165 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 166 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 167 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 168 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 169 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 170 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 171 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 172 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 173 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 174 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 175 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 176 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 177 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 178 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 179 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 180 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 181 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 182 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 183 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 184 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 185 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 186 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 187 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 188 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 189 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 190 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 191 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 192 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 193 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
