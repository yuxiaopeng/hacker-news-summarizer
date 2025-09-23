# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-23.md)

*最后自动更新时间: 2025-09-23 17:53:27*
## 1. Libghostty 即将到来

**原文标题**: Libghostty is coming

**原文链接**: [https://mitchellh.com/writing/libghostty-is-coming](https://mitchellh.com/writing/libghostty-is-coming)

米切尔·桥本宣布即将发布`libghostty`，这是一个可嵌入的库，为各种应用程序提供终端仿真功能。初始组件`libghostty-vt`是一个零依赖库（甚至不依赖libc），用于解析终端序列和管理终端状态，它从Ghostty的核心中提取而来。它的目标是解决在终端模拟器、多路复用器、编辑器和Web应用程序等众多程序中普遍存在的临时、不完整和有缺陷的终端仿真实现问题。

`libghostty-vt`提供诸多优势，如SIMD优化解析、出色的Unicode支持、优化的内存使用以及与Kitty Graphics Protocol和Tmux Control Mode等功能的兼容性。它最初将支持macOS和Linux（x86_64和aarch64），并计划扩展到Windows、嵌入式设备以及通过WASM实现Web支持。

作者强调了终端仿真的稳定和可重用解决方案的重要性，因为它通常不是核心业务关注点。未来的`libghostty`组件将包括输入处理、GPU渲染、GTK小部件和Swift框架。`libghostty-vt`的Zig模块可供测试，C API即将推出。该项目目前处于Alpha阶段，并寻求开发人员的反馈以完善API。目标是在六个月内发布一个标记版本，具体取决于准备情况。作者认为`libghostty`的影响力将超过Ghostty应用程序本身，同时也将促进构建一个功能更丰富、更稳定的Ghostty。

---

## 2. Go 添加了 Valgrind 支持

**原文标题**: Go has added Valgrind support

**原文链接**: [https://go-review.googlesource.com/c/go/+/674077](https://go-review.googlesource.com/c/go/+/674077)

Go 已添加 Valgrind 支持，但因内容受限，仅提示需启用 JavaScript 方可查看 PolyGerrit 页面全文，故无法提供详细摘要。要点如标题所示，为 Go 语言生态系统新增 Valgrind 集成。欲了解具体支持信息，例如其功能及使用方法，需访问 PolyGerrit 平台上的完整文章。

---

## 3. x402 — 一种面向互联网原生支付的开放协议

**原文标题**: x402 — An open protocol for internet-native payments

**原文链接**: [https://www.x402.org/](https://www.x402.org/)

x402 是一种开放的、原生互联网支付协议，围绕 HTTP 402 状态码构建，旨在为 API 访问和其他资源实现无摩擦的数字支付。它具有零协议费用、通过区块链集成（与特定区块链无关）实现的近乎即时结算以及用户友好的体验等优势，无需注册、电子邮件、OAuth 或复杂签名。

其主要功能包括与 Web 原生集成，可与任何 HTTP 堆栈配合使用，并且只需最少的代码（最少一行）即可实现，以及其开放、去中心化的特性，通过社区参与来提升安全性和信任。x402 旨在解锁新的货币化模型，特别是对于微支付，使 AI 代理、云存储提供商和内容创作者受益。只需一行代码即可要求对特定端点进行 USDC 支付，如果缺少支付，则会提示用户 HTTP 402 错误，从而简化了 Web 开发人员接受加密货币支付的过程。

---

## 4. 从 MCP 到 Shell：MCP 身份验证缺陷导致 Claude Code、Gemini CLI 等出现 RCE 漏洞

**原文标题**: From MCP to shell: MCP auth flaws enable RCE in Claude Code, Gemini CLI and more

**原文链接**: [https://verialabs.com/blog/from-mcp-to-shell/](https://verialabs.com/blog/from-mcp-to-shell/)

Veria Labs 发现多个 AI 工具的 Model Context Protocol (MCP) 实现中存在严重漏洞，可能导致远程代码执行 (RCE)。该漏洞源于 MCP 客户端信任 MCP 服务器提供的授权 URL，而未进行适当验证。

该漏洞首先在 Cloudflare 的 `use-mcp` 库中被发现，攻击者控制的 MCP 服务器可以通过传递给 `window.open()` 的 `javascript:` URL 将任意 JavaScript 代码注入到客户端的浏览器中。这可能导致会话劫持和帐户接管。

该漏洞随后升级为 Anthropic 的 MCP Inspector 中的 RCE。通过 XSS 窃取 Inspector Proxy 的身份验证令牌，攻击者可以指示代理在用户的机器上执行任意命令。

同样，由于在 Windows 上打开授权 URL 时存在命令注入漏洞，Claude Code 和 Gemini CLI 也被发现存在漏洞。文章详细介绍了用于在这些应用程序中实现 RCE 的特定 payload。

虽然 ChatGPT 的 MCP 实现也存在漏洞，但其内容安全策略 (CSP) 阻止了利用。

Cloudflare、Anthropic 和 Google 实施了修复，范围从 URL 清理到完全删除 shell 的使用。Anthropic 对 MCP TypeScript SDK 的更新（将危险的 URI 方案列入黑名单）产生了最重大的影响，提高了整个 MCP 生态系统的安全性。

研究人员感谢 Cloudflare、Anthropic 和 Google 的快速响应和修补过程，并在 GitHub 上分享了概念验证代码。

---

## 5. 让AI在复杂代码库中工作

**原文标题**: Getting AI to work in complex codebases

**原文链接**: [https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)

GitHub仓库 `humanlayer/advanced-context-engineering-for-coding-agents` 专注于提升AI编程助手性能的策略，尤其是在处理复杂大型代码库时。该项目认为有效的“上下文工程”对于AI在该领域的成功至关重要。

高级上下文工程的关键方面（正如仓库内可能探讨的内容）可能包括：

*   **情境化策略：** 高效且有效地为AI提供相关的代码片段、项目架构、文档以及其他必要信息，使其能够理解代码库和手头的任务。这可能涉及语义搜索、代码索引、依赖性分析和代码文件智能抽样等技术。
*   **提示工程：** 设计精确清晰的提示语，引导AI助手朝着期望的结果前进，明确任务、约束条件和期望的输出格式。这可能包括加入示例、将复杂任务分解为更小的步骤，以及使用特定的关键词或指令。
*   **知识管理：** 集成外部知识源，例如API文档、设计模式和通用编码实践，以增强AI助手的理解能力并提高其代码生成能力。
*   **迭代优化和反馈循环：** 纳入AI接收代码反馈并逐步提高其性能的机制。这可能涉及单元测试、代码审查和人机协作工作流程。

该仓库的受欢迎程度（48颗星）表明了对该领域的需求和兴趣。最终，该项目的目标很可能是通过为复杂软件项目中管理上下文提供实用指导和工具，来帮助开发人员更有效地利用AI编程助手。

---

## 6. 更具策略性

**原文标题**: Getting More Strategic

**原文链接**: [https://cate.blog/2025/09/23/getting-more-strategic/](https://cate.blog/2025/09/23/getting-more-strategic/)

本文探讨了战略的复杂性，认为真正的战略不仅仅是一种愿景，更是一条实现目标的切实路径。它区分了“具有战略性”和“被视为具有战略性”，突出了那些默默执行有效战略却被忽视的人的沮丧。

作者强调，战略是情境性的，必须适应不断变化的环境，例如从零利率时代到资源更为受限时代的转变。他们概述了所需的不同战略：产品、技术、团队和个人，认识到它们以复杂且常常不平衡的方式相互作用。

本文介绍了“近端目标”的概念，将其作为实现总体战略的渐进步骤，这对于执行和可证明的进展至关重要。它认为，低估这些目标的实施会导致对谁是真正具有战略性的误解。

文章确定了有效战略的四个要素：时间、情境、方向和专业知识。作者阐述了过度强调其中任何一个要素的危险。

最后，文章剖析了每种战略——产品、技术、团队和个人——所扮演的角色：产品战略设定方向，技术战略发展情境，团队战略侧重于执行，个人战略则需要在日常需求中开辟时间进行战略思考。核心信息是，有效的战略需要平衡这些要素，才能为团队和个人导航前进的道路。

---

## 7. 想象一个没有布尔值的语言

**原文标题**: Imagining a language without booleans

**原文链接**: [https://justinpombrio.net/2025/09/22/imagining-a-language-without-booleans.html](https://justinpombrio.net/2025/09/22/imagining-a-language-without-booleans.html)

Justin Pombrio的博文探讨了一种编程语言的设计理念，该语言消除了布尔值，并用`Option`或`Result`类型取而代之。 他首先观察到`if`语句在有`else`子句和没有`else`子句时的不同行为。他提出，没有`else`的`if`语句可以返回一个`Option<T>`，如果条件为真，则返回`Some(value)`，如果为假，则返回`None`。 这同样适用于`else`，其中`else`为`Option`提供一个默认值。

然后，作者将这个概念扩展到逻辑运算符`and`和`or`，使它们也能在`Option`类型上操作。他注意到布尔值和`Option<()>`之间的等价性，暗示布尔值可以完全被Option取代。 他更进一步，利用`Option<T>`和`Result<T, ()>`之间的等价性，提出了一种新的语法`T ? E`来表示`Result<T, E>`。他定义了别名：`bool = nil?nil`，`true = Ok(nil)`，以及`false = Err(nil)`。

Pombrio探讨了此系统中`if`、`else`、`and`、`or`和`not`的类型和求值规则。他证明了像`else if`和循环的“try/else”模式等结构都可以自然地表达。 他使用来自其项目的真实代码片段来说明所提出的语言如何通过消除显式地将结果包装在`Some`或`Err`中以及提前返回语句的需求来简化代码。 作者的结论是，这种设计看起来是连贯的，并且可能会影响他对条件语句的思考，寻找与他提出的想法类似的想法。

---

## 8. 非亲属合租的房屋共享限制

**原文标题**: Restrictions on house sharing by unrelated roommates

**原文链接**: [https://marginalrevolution.com/marginalrevolution/2025/08/the-war-on-roommates-why-is-sharing-a-house-illegal.html](https://marginalrevolution.com/marginalrevolution/2025/08/the-war-on-roommates-why-is-sharing-a-house-illegal.html)

本文探讨了分区法和入住限制如何有效地消除单间居住 (SRO) 等低成本住房选择，并阻碍了非亲属关系个人之间的合租。文章引用了一份皮尤报告，该报告强调，由于自 20 世纪 50 年代中期以来颁布的限制性分区法和建筑规范，SRO 从租赁市场的重要组成部分衰落到几乎灭绝。这些变化往往受到对 SRO 及其居民的负面看法所驱动，并导致无家可归现象的加剧。

作者强调了一个简单的解决方案，即允许非亲属关系个人不受限制地合租房屋，并指出目前的法律经常阻止室友同住和利用未使用的卧室，尽管这对房东和租户来说都是有利的经济选择。爱荷华州、俄勒冈州和科罗拉多州被提及为已通过立法推翻禁止合租的当地法规的州。文章最后指出，许多社会问题都是过度监管造成的，这些监管限制了房产所有者以可以缓解住房短缺和负担能力问题的方式利用其资产的能力。

---

## 9. LLM中的结构化输出

**原文标题**: Structured Outputs in LLMs

**原文链接**: [https://parthsareen.com/blog.html#sampling.md](https://parthsareen.com/blog.html#sampling.md)

无法访问文章链接。

---

## 10. 九十岁时我学到的九件事

**原文标题**: Nine things I learned in ninety years

**原文链接**: [http://edwardpackard.com/wp-content/uploads/2025/09/Nine-Things-I-Learned-in-Ninety-Years.pdf](http://edwardpackard.com/wp-content/uploads/2025/09/Nine-Things-I-Learned-in-Ninety-Years.pdf)

很抱歉，我无法提供文章的摘要。您提供的内容似乎是PDF文件的二进制数据，而不是人类可读的文本。它由编码字符和渲染文档的指令组成，但并不包含“九十年中学到的九件事”这篇文章的实际文本。要进行总结，我需要文章的纯文本内容。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 2 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 3 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 4 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 5 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 6 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 7 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 8 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 9 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 10 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 11 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 12 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 13 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 14 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 15 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 16 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 17 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 18 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 19 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 20 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 21 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 22 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 23 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 24 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 25 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 26 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 27 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 28 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 29 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 30 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 31 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 32 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 33 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 34 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 35 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 36 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 37 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 38 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 39 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 40 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 41 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 42 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 43 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 44 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 45 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 46 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 47 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 48 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 49 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 50 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 51 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 52 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 53 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 54 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 55 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 56 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 57 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 58 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 59 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 60 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 61 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 62 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 63 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 64 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 65 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 66 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 67 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 68 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 69 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 70 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 71 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 72 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 73 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 74 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 75 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 76 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 77 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 78 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 79 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 80 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 81 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 82 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 83 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 84 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 85 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 86 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 87 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 88 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 89 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 90 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 91 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 92 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 93 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 94 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 95 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 96 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 97 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 98 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 99 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 100 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 101 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 102 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 103 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 104 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 105 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 106 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 107 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 108 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 109 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 110 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 111 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 112 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 113 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 114 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 115 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 116 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 117 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 118 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 119 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 120 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 121 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 122 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 123 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 124 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 125 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 126 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 127 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 128 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 129 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 130 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 131 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 132 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 133 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 134 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 135 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 136 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 137 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 138 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 139 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 140 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 141 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 142 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 143 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 144 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 145 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 146 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 147 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 148 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 149 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 150 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 151 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 152 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 153 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 154 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 155 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 156 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 157 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 158 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 159 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 160 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 161 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 162 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 163 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 164 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 165 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 166 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 167 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 168 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 169 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 170 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 171 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 172 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 173 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 174 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 175 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 176 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 177 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 178 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 179 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 180 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 181 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 182 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 183 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 184 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 185 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 186 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 187 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 188 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
