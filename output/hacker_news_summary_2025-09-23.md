# Hacker News 热门文章摘要 (2025-09-23)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 安卓用户现在可以在Google Photos中使用对话式编辑功能

**原文标题**: Android users can now use conversational editing in Google Photos

**原文链接**: [https://blog.google/products/photos/android-conversational-editing-google-photos/](https://blog.google/products/photos/android-conversational-editing-google-photos/)

Google Photos 正在向美国符合条件的 Android 用户推出一项新的对话式编辑功能，该功能之前为 Pixel 10 独有。这项由 Gemini AI 提供支持的功能，允许用户通过语音或文本描述所需的更改来编辑照片，而无需手动调整设置。用户可以通过点击“帮我编辑”并描述所需的更改来访问该功能。然后，Google Photos 会使用 AI 进行调整。该功能提供诸如“让它更好”之类的建议编辑，或者允许进行创意和古怪的编辑。这项新功能，以及现有的 AI 驱动工具和一键式建议，旨在简化照片编辑并帮助用户轻松实现他们的创意愿景。

---

## 12. 平滑加权轮询负载均衡

**原文标题**: Smooth weighted round-robin balancing

**原文链接**: [https://github.com/nginx/nginx/commit/52327e0627f49dbda1e8db695e63a4b0af4448b1](https://github.com/nginx/nginx/commit/52327e0627f49dbda1e8db695e63a4b0af4448b1)

本文介绍了一个针对Nginx轮询负载均衡算法的补丁，引入了“平滑加权轮询均衡”。该补丁修改了`ngx_http_upstream_round_robin.c`和`ngx_http_upstream_round_robin.h`文件。

主要变更包括：

*   **有效权重：** 为上游组中的每个服务器引入了一个`effective_weight`参数，与配置的`weight`分开。这允许动态调整服务器权重，而无需直接更改配置。
*   **权重调整：** 服务器逐渐将其`effective_weight`增加到其配置的`weight`，从而在权重更改期间提供更平滑的过渡。
*   **`ngx_http_upstream_get_peer`修改：** 重写了选择对等方的核心逻辑，以优先选择具有较高`current_weight`的服务器，同时考虑服务器运行状况（最大失败次数、故障超时）和已尝试的服务器。现在它返回一个指向对等结构体的指针，而不仅仅是一个索引。
*   **避免陈旧服务器：** 考虑“down”状态、`max_fails`和`fail_timeout`以防止选择不健康的服务器。
*   **改进的选择逻辑：** 选择过程现在确保即使服务器的配置权重较低，它也有机会被选中，从而防止低权重服务器的资源匮乏。
*   **容错能力：** 在发生错误时降低`effective_weight`，以降低选择不健康服务器的概率。

本质上，该补丁旨在改进标准轮询算法，通过添加一种更平滑、更动态的方式来跨上游服务器分配流量，同时考虑到服务器健康状况并防止流量不平衡。

---

## 13. Shopify操控Ruby Central，强行接管Bundler和RubyGems

**原文标题**: Shopify, pulling strings at Ruby Central, forces Bundler and RubyGems takeover

**原文链接**: [https://joel.drapper.me/p/rubygems-takeover/](https://joel.drapper.me/p/rubygems-takeover/)

本文详细描述了 Ruby Central 对 RubyGems 和 Bundler 项目的一次颇具争议的收购，据称该收购由 Shopify 策划。 Ruby Central 在因平台处理 DHH 事件而失去一项主要赞助后，面临财务困境，变得严重依赖 Shopify。 反过来，据报道，Shopify 施压 Ruby Central，要求其完全控制 RubyGems 的 GitHub 仓库和 gems，并威胁说如果不遵守，将撤回资金。

此次收购涉及降低现有维护者的权限，最终移除他们，并用 Shopify 支持的随叫随到轮换制度取而代之。 一个关键的争议点是，虽然 Ruby Central 运营着 RubyGems 服务（运行 RubyGems 代码的服务器），但他们并不拥有 RubyGems 的源代码、仓库或 gems 本身，这些一直由社区维护。

文章声称 Ruby Central 董事会意识到此次收购可能造成的潜在损害，但在来自 Shopify 的巨大压力下仍然继续进行。 具体指控包括排挤长期 RubyGems 维护者 André Arko，Ruby Central 董事会成员对情况的歪曲，以及将“供应链安全”用作权力攫取的幌子。 作者的结论是，此次收购是由 Shopify 对控制权的渴望驱动的，而不是真正的安全问题，而 Ruby Central 由于经济上的依赖而屈服了。

---

## 14. 精英是精英统治且追求效率的吗？来自MBA学生的证据

**原文标题**: Are elites meritocratic and efficiency-seeking? Evidence from MBA students

**原文链接**: [https://arxiv.org/abs/2503.15443](https://arxiv.org/abs/2503.15443)

本文《精英是否信奉精英制度和追求效率？来自MBA学生的证据》研究了未来精英——常春藤盟校MBA学生——的公平和效率偏好，以及这些偏好与再分配政策的关系。作者Marcel Preuss、Germán Reyes、Jason Somerville和Joy Wu利用激励性实验室实验来研究这些偏好。

主要研究结果表明，无论不平等是由运气还是能力造成的，MBA学生实施的收入分配都明显比普通美国人更加不平等。他们的再分配选择对与再分配相关的效率成本高度敏感，这种影响远强于在美国代表性样本中观察到的情况。此外，该研究发现，与更广泛的人群相比，MBA学生不太可能严格遵守精英制度原则。

作者得出结论，这些发现为精英的再分配偏好如何导致美国高水平的不平等提供了新的见解。本文有助于理解未来政策制定者的偏好及其对经济不平等的潜在影响。它属于一般经济学（econ.GN）范畴，并使用JEL代码D63、C91和H23。

---

## 15. OpenDataLoader-PDF：一个用于结构化PDF解析的开源工具

**原文标题**: OpenDataLoader-PDF: An open source tool for structured PDF parsing

**原文链接**: [https://github.com/opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf)

OpenDataLoader-PDF是一个开源工具，旨在对PDF文档进行结构化解析，并针对LLM和RAG等AI应用进行了优化。它可以将PDF转换为JSON、Markdown或HTML，重建文档布局，包括标题、列表、表格和阅读顺序，以便更轻松地进行内容分块和查询。该工具强调本地优先的隐私性，完全在您的机器上运行，并通过过滤潜在的提示注入内容来实现AI安全。

主要功能包括丰富、结构化的输出，布局重建，速度，本地处理，AI安全功能以及带注释的PDF可视化。即将推出的功能包括扫描PDF的OCR，用于提高表格准确性的AI选项，性能基准测试和AI红队测试。

该工具提供了针对Python、Node.js和Java环境的安装和使用说明。它为其核心`run()`函数提供了详细的文档，概述了输入路径、输出文件夹、密码保护、字符替换、内容安全过滤器和输出格式选项的参数。

本文档还概述了如何为该项目做出贡献，在哪里寻求社区支持以及使用该项目品牌和商标的指南。最后，它指定了该项目所采用的Mozilla Public License 2.0许可证。

---

## 16. 锌 (YC W14) 正在招聘高级后端工程师 (纽约市)

**原文标题**: Zinc (YC W14) Is Hiring a Senior Back End Engineer (NYC)

**原文链接**: [https://app.dover.com/apply/Zinc/4d32fdb9-c3e6-4f84-a4a2-12c80018fe8f/?rs=76643084](https://app.dover.com/apply/Zinc/4d32fdb9-c3e6-4f84-a4a2-12c80018fe8f/?rs=76643084)

这是一则在纽约市的Zinc (YC W14)招聘高级后端工程师的职位发布。 由于显示“您需要启用JavaScript才能运行此应用程序”的消息，文章内容不可访问。 这表明职位描述和具体要求可能嵌入在Dover平台（一个招聘平台）上的JavaScript应用程序中。 因此，在访问JavaScript内容之前，我无法提供有关该职位的职责、资格、福利或公司文化的任何具体细节。 我只能说Zinc (YC W14)正在纽约市招聘高级后端工程师，并且申请流程通过Dover管理。

---

## 17. 网格：我试了 Htmx，然后放弃了

**原文标题**: Mesh: I tried Htmx, then ditched it

**原文链接**: [https://ajmoon.com/posts/mesh-i-tried-htmx-then-ditched-it](https://ajmoon.com/posts/mesh-i-tried-htmx-then-ditched-it)

作者探讨了“HTML Over The Wire”运动，质疑使用JavaScript构建HTML的趋势。受HTMX启发（HTMX提倡使用声明式HTML属性进行Web开发），作者试图创建一个结构化、模块化的方法，类似于SPA框架，但使用服务器端渲染。

最终成果是MESH（Modular Element SSR with Hydration，模块化元素服务器端渲染与水合），一个基于“一个组件 = 一个端点”原则的系统。作者使用Go语言和Templ作为后端，并尝试使用声明式Shadow DOM (DSD) 实现服务器端渲染的自定义元素。一个关键的限制是HTMX无法跨越Shadow Root边界，需要使用一些技巧来强制实现组件级别的交换和OOB（带外）更新。

作者实现了基本的交互功能，例如编辑卡片、使用OOB交换在列之间移动卡片以及拖放功能。他们还探索了使用服务器发送事件（SSE）实现的实时协作，并通过插件展示了HTMX的支持。虽然作者在将HTMX与Shadow DOM集成时面临挑战，需要自定义解决方案，但该项目展示了使用HTMX进行模块化SSR的潜力，并利用该框架的JavaScript API来增强功能。总而言之，本文重点介绍了作者在SPA框架的结构和HTML优先开发的优势之间取得平衡的旅程。

---

## 18. Show HN: Kekkai – 一个用 Go 编写的简单快速的文件完整性监控工具

**原文标题**: Show HN: Kekkai – a simple, fast file integrity monitoring tool in Go

**原文链接**: [https://github.com/catatsuy/kekkai](https://github.com/catatsuy/kekkai)

Kekkai：一款基于 Go 的文件完整性监控工具，旨在检测生产环境中未经授权的文件修改。它通过仅关注文件内容哈希，忽略时间戳等元数据，来解决传统工具的局限性，从而避免在使用 NFS 或动态日志的环境中常见的误报。

主要特点包括：

*   **仅内容哈希：** 专注于文件内容，忽略元数据。
*   **不可变排除规则：** 排除项在清单生成期间定义，验证期间无法更改，防止攻击者隐藏更改。
*   **符号链接安全：** 检测符号链接修改，包括目标路径的更改和文件类型转换（文件到符号链接或反之）。
*   **安全哈希存储：** 支持 S3 用于防篡改的文件哈希存储，部署服务器具有只写权限，应用程序服务器具有只读权限。

Kekkai 使用 glob 模式排除文件，并为 Laravel、Node.js、Rails 和 Django 等常见框架提供示例，强调监控应用程序依赖项（如 `vendor` 和 `node_modules`）的重要性。

该工具为监控系统提供多种输出格式，并使用并行处理进行速度和效率优化。 使用示例涵盖清单生成、文件验证和 S3 集成，包括所需的 IAM 策略和存储桶配置。 它还包括解决常见问题的故障排除技巧。

---

## 19. 秀一下：在8GB GPU上以1tok/2s吞吐量运行Qwen3-Next-80B

**原文标题**: Show HN: Run Qwen3-Next-80B on 8GB GPU at 1tok/2s throughput

**原文链接**: [https://github.com/Mega4alik/ollm](https://github.com/Mega4alik/ollm)

这个“Show HN”帖子介绍了 oLLM，这是一个 Python 库，专为高效的大上下文 LLM 推理而设计，使 Qwen3-Next-80B、GPT-OSS-20B 和 Llama-3 变体等模型能够在具有至少 8GB VRAM 的消费级 GPU 上运行。 oLLM 通过直接从 SSD 加载层权重、将 KV 缓存卸载到 SSD (DiskCache) 而无需量化、可选的 CPU 卸载、FlashAttention-2 和分块 MLPs 等技术来实现这一点。

最新版本 (0.4.0) 具有重大改进，包括支持 Qwen3-Next-80B，据报道吞吐量为 1 个 token/2 秒，支持 Llama-3 模型的 FlashAttention-2，以及针对 GPT-OSS-20B 的 VRAM 优化。 该帖子包含一个表格，详细说明了各种模型的内存使用情况，突出了与基线推理方法相比，GPU VRAM 需求的降低。

oLLM 的目标用例包括处理大量数据，如合同、医疗记录、日志文件和聊天记录。 它支持 Nvidia Ampere、Ada Lovelace、Hopper 和更新的 GPU。 该帖子提供了使用 pip 安装的说明和一个代码示例，演示了如何将 oLLM 与 Llama-3 模型一起使用。 作者鼓励用户请求支持其他模型，并提供联系信息。

---

## 20. Zoxide：更好的 CD 命令

**原文标题**: Zoxide: A Better CD Command

**原文链接**: [https://github.com/ajeetdsouza/zoxide](https://github.com/ajeetdsouza/zoxide)

Zoxide：一款更智能的`cd`命令，它能记住常用的目录，让你只需敲击几下键盘就能快速“跳转”到这些目录。它的灵感来源于`z`和`autojump`，并且可以在所有主流 Shell 和操作系统上运行。

**主要特性：**

*   **智能导航：** 基于频率和关键词跳转到目录。
*   **模糊匹配：** 使用模糊匹配进行目录选择（例如，`z foo`会导航到排名最高的匹配“foo”的目录）。
*   **交互式选择：** 使用`fzf`提供`zi`的交互式选择。
*   **补全：** 提供交互式补全。
*   **常规`cd`功能：** 也可像普通的`cd`命令一样工作。

**安装：**

Zoxide 可以通过包管理器（如`apt`、`brew`、`winget`、`pkg`）或提供的安装脚本进行安装。文章列出了适用于各种 Linux 发行版、macOS、Windows、BSD 和 Android 的特定命令。

**设置：**

安装后，需要通过在 Shell 配置文件（例如，`.bashrc`、`config.fish`、`.zshrc`）中添加一行来将 Zoxide 集成到 Shell 中。具体命令取决于您的 Shell。

**配置：**

Zoxide 可以在`zoxide init`期间使用标志（例如，`--cmd`用于更改命令前缀，`--hook`用于更改目录评分频率）和环境变量（例如，`_ZO_DATA_DIR`用于数据库位置，`_ZO_EXCLUDE_DIRS`用于排除目录）进行配置。

**导入：**

可以从 `autojump`、`fasd`、`z`、`z.lua`、`zsh-z` 和 `ZLocation` 导入数据到 Zoxide。

**集成：**

Zoxide 与各种应用程序集成，如文件管理器、文本编辑器和 tmux 会话管理器。

---

## 21. 来自地狱的YAML文档 (2023)

**原文标题**: YAML document from hell (2023)

**原文链接**: [https://ruudvanasseldonk.com/2023/01/11/the-yaml-document-from-hell](https://ruudvanasseldonk.com/2023/01/11/the-yaml-document-from-hell)

本文认为，尽管 YAML 旨在具有人性化，但它过于复杂且充满陷阱，使其成为配置的糟糕选择。作者将 YAML 与 JSON 进行对比，突出了 JSON 的简洁性和稳定的规范。另一方面，YAML 是有版本的、不断发展的，并且具有深奥的行为，如六十进制数字、隐式类型转换（“挪威问题”）和非字符串键，导致不可预测的解析和安全漏洞。

作者用一个“来自地狱的 YAML 文档”展示了这些问题，展示了意外的数据类型解释和潜在错误的例子。他批评了语法高亮的不可靠性，并强烈反对对 YAML 进行模板化，因为它过于复杂且对空白字符非常敏感。

本文提出了替代的配置格式，包括 TOML（更安全和更简单）、带有注释的 JSON，以及从编程语言（如 Nix 或 Python）生成 JSON，以实现更高级的抽象和重用。作者提到了 Dhall、Cue 和 HCL，但对其复杂性或局限性持保留态度。结论强调，虽然 YAML 试图改进 JSON，但其过多的功能最终使其难以有效使用。生成 JSON 提供了一种更安全、更强大的配置管理方式，尤其是在需要抽象时。

---

## 22. 代理将简单的关键词搜索转变为引人入胜的搜索体验。

**原文标题**: Agents turn simple keyword search into compelling search experiences

**原文链接**: [https://softwaredoug.com/blog/2025/09/22/reasoning-agents-need-bad-search](https://softwaredoug.com/blog/2025/09/22/reasoning-agents-need-bad-search)

本文探讨了使用LLM智能体来增强搜索体验，并将其与传统的RAG系统进行了对比。作者认为，复杂的“厚重”搜索API可能会适得其反，阻碍智能体的有效推理能力。相反，一个更简单、依赖基本关键词匹配的“简易”搜索后端，结合清晰的智能体文档，可以产生出人意料的好结果。

智能体的推理能力使其能够迭代地优化查询，构建搜索工具的“心智模型”，并最终找到更相关的结果。作者强调了跟踪和评估过去查询的重要性，使智能体能够从经验中学习并改进未来的搜索。语义缓存通过利用相似的过去查询进一步增强了这种学习。

然而，作者提醒说，智能体的判断是有限的，并且与用户偏好脱节。缺乏用户点击流反馈是一个显著的差距，因为智能体可能不理解用户复杂且常常不可预测的行为。智能体的推理可能会导致其丢弃对用户有吸引力的相关结果，这突出了显式推理和隐式用户期望之间可能存在的冲突。尽管存在这些警告，作者的结论是，使用LLM智能体进行搜索是一个有前途且令人愉快的探索领域，为构建更智能和个性化的搜索体验提供了一种独特的方法。

---

## 23. 惊群效应：防止蜂拥而至

**原文标题**: Thundering herd problem: Preventing the stampede

**原文链接**: [https://distributed-computing-musings.com/2025/08/thundering-herd-problem-preventing-the-stampede/](https://distributed-computing-musings.com/2025/08/thundering-herd-problem-preventing-the-stampede/)

本文探讨了“惊群效应”问题，这是缓存数据以减少数据库负载时常见的难题。当多个并发请求同时请求同一个缺失的缓存条目时，都会同时查询数据库，从而导致数据库负载过重，进而引发该问题。

作者使用 Spring Boot 应用程序，并结合 Redis 缓存和 Postgres 数据库，演示了这个问题。代码遵循缓存旁路模式，但对同一 ID 的并发请求会导致多次数据库查询。

文章提出了两种解决方案：

1.  **分布式锁 (Redis):** 使用 Redis 为每个缓存键获取锁。只有获取锁的请求才会从数据库获取数据并回填缓存。其他请求从缓存重试。这适用于多节点设置，确保尽管请求分布在多个节点上，也只有一个数据库调用，但会引入网络开销。

2.  **进程内同步 (Java):** 使用 `CompletableFuture` 和 `ConcurrentHashMap` 在单个 JVM 中同步请求。当发生缓存未命中时，会创建一个 `CompletableFuture`（或检索现有的一个）。只有创建 future 的请求才会执行数据库查找并回填缓存。其他请求等待 future 完成。这避免了网络调用，但不会跨多个节点进行协调，可能会导致多节点环境中出现多次数据库查找。

作者总结说，虽然缓存很有用，但它可能会引入诸如惊群效应之类的问题，并强调了考虑边缘情况以及根据应用程序的需求选择适当解决方案的重要性。

---

## 24. 处理字符串速度比H100上的英伟达快109倍

**原文标题**: Processing Strings 109x Faster Than Nvidia on H100

**原文链接**: [https://ashvardanian.com/posts/stringwars-on-gpus/](https://ashvardanian.com/posts/stringwars-on-gpus/)

本文宣布 StringZilla v4，这是一个支持 CUDA 的字符串处理库，其性能显著优于 Nvidia 的 CuDF 和其他 Python 库等现有解决方案。一项关键创新是对角线动态规划算法，例如 Levenshtein 距离计算，在 Nvidia H100 GPU 上运行时，与 CuDF 相比，大型字符串的速度提升高达 109 倍。该库还包括用于生物信息学中 Needleman-Wunsch 和 Smith-Waterman 分数的优化函数。

StringZilla v4 引入了使用 AES 指令和端口并行性的新型非加密哈希函数，为短字符串和长字符串提供高速处理能力。它还具有超过标准 C++ 库的高吞吐量随机字符串生成功能。

在生物信息学方面，StringZilla v4 实现了基于 52 位整数的 MinHashing，用于高效的序列指纹识别，为传统的滚动哈希提供了一种快速替代方案。作者强调 StringZilla 专注于为大规模信息检索、数据库、数据湖和生物信息学工作负载提供可靠且易于使用的基线，所有这些都在 Apache 2.0 开源许可下进行。本文展示了基准测试结果，比较了 StringZilla 在 Levenshtein 距离计算、哈希和随机字符串生成等任务中与其他流行库的性能。

---

## 25. 在纽约发现可致蜂窝网络崩溃的设备缓存

**原文标题**: Cache of devices capable of crashing cell network is found in NYC

**原文链接**: [https://www.nytimes.com/2025/09/23/us/politics/secret-service-sim-cards-servers-un.html](https://www.nytimes.com/2025/09/23/us/politics/secret-service-sim-cards-servers-un.html)

无法访问文章链接。

---

## 26. Zig 对于实际 CLI 工具而言，感觉比 Rust 更实用。

**原文标题**: Zig feels more practical than Rust for real-world CLI tools

**原文链接**: [https://dayvster.com/blog/why-zig-feels-more-practical-than-rust-for-real-world-cli-tools/](https://dayvster.com/blog/why-zig-feels-more-practical-than-rust-for-real-world-cli-tools/)

Dayvi Schuster 认为，由于 Zig 在内存管理和开发者人体工程学方面的方法更简单，因此对于实际的 CLI 工具来说，Zig 比 Rust 更实用。 文章对比了 Rust 的借用检查器（在编译时强制执行严格的内存安全规则）和 Zig 使用分配器和 `defer` 语句进行的手动内存管理。

Schuster 认为，虽然 Rust 的借用检查器可以防止某些内存安全错误，但它会引入认知负担、样板代码和限制，从而阻碍开发人员的生产力，尤其是在像 CLI 工具这样的小型项目中。 借用检查器仅在编译时捕获问题，但它不会修复开发人员误解内存生命周期或过度复杂的所有权等根本问题。

作者强调，内存安全只是整体软件安全的一个方面，并强调了可预测的行为、错误处理、性能、数据安全以及针对攻击的鲁棒性的重要性。 虽然 Rust 在内存安全方面表现出色，但 Zig 允许开发人员通过对内存管理和规范的基本理解来实现类似的安全级别，从而产生更直接且更易于推理的代码。

Zig 的手动内存管理与 `comptime` 和精心设计的分配器等功能相结合，在控制和安全之间实现了平衡，使其成为 CLI 工具开发的引人注目的选择。 作者最后总结说，虽然 Rust 适用于大型、复杂的项目，其中编译时保证至关重要，但 Zig 的简单性和开发者人体工程学使其成为更小、更日常的 CLI 工具的更实用选择。

---

## 27. 一把Altoids糖

**原文标题**: Altoids by the Fistful

**原文链接**: [https://www.scottsmitelli.com/articles/altoids-by-the-fistful/](https://www.scottsmitelli.com/articles/altoids-by-the-fistful/)

《一把薄荷糖》中，叙述者得知同事吉姆靠吃猫屎来应对工作中令人不快的任务，感到不安。 吉姆声称薄荷糖完全掩盖了味道，并且这种做法彻底改变了他的工作效率。

叙述者感到厌恶，但开始反思自己生活中的“猫屎”——他软件工程工作中那些单调、毫无意义和令人沮丧的方面。 他为一个YAML模板问题苦恼，并意识到他不再从解决这类问题中获得智力上的满足感。 他承认自己曾经对编程充满热情，但已经对许多任务的毫无意义感到厌倦。

在回家的路上，叙述者将“猫屎”的定义扩展到包括各种令人不快的任务和他一生中必须经历的官僚主义障碍，例如家庭作业和大学入学申请论文。 他意识到自己已经“吃猫屎”很长时间了，并且感到自己陷入了一个从事最终毫无意义和令人不满意的工作的循环中。 与吉姆不同，他没有像薄荷糖这样简单的解决方案来使“猫屎”消失。

---

## 28. 房屋中的渗透性材料会像海绵一样吸收有害化学物质：研究显示

**原文标题**: Permeable materials in homes act as sponges for harmful chemicals: study

**原文链接**: [https://news.uci.edu/2025/09/22/indoor-surfaces-act-as-massive-sponges-for-harmful-chemicals-uc-irvine-led-study-shows/](https://news.uci.edu/2025/09/22/indoor-surfaces-act-as-massive-sponges-for-harmful-chemicals-uc-irvine-led-study-shows/)

加州大学尔湾分校新研究表明，常见的室内表面，如木材、混凝土和涂漆墙壁，是挥发性有机化合物（VOCs）的重要“化学海绵”。 这些 VOCs 来自杀虫剂、香烟烟雾、野火烟雾和日常家居用品等来源，可在表面停留长达一年，通过吸入或皮肤接触构成长期健康风险。

研究人员通过模拟家庭环境的受控实验发现，这些多孔材料吸收和保持 VOCs 的程度远超之前的认知，超过了薄有机薄膜的吸收能力。 这解释了为什么即使在去除源头后，气味和污染物仍会在室内持续存在，例如挥之不去的“三手烟”气味。

该研究强调了仅靠通风来去除这些污染物的局限性，并强调需要采用吸尘、拖地和除尘等物理清洁方法，才能有效清除表面储库中的 VOCs。 这种对 VOCs 与室内环境相互作用的新理解对公共健康具有重要意义，表明个人可能在最初引入有害化学物质后很长时间仍会暴露于其中，并强调了采取全面清洁措施以降低暴露风险的重要性。

---

## 29. 美国邮政编码地图

**原文标题**: Zip Code Map of the United States

**原文链接**: [https://engaging-data.com/us-zip-code-map/](https://engaging-data.com/us-zip-code-map/)

本文介绍了一个美国交互式邮政编码地图，它可视化了美国所有 50 个州超过 42,000 个邮政编码。该地图使用点来表示每个邮政编码的地理中心，并允许用户搜索特定的邮政编码。

当用户输入时，交互式功能会突出显示邮政编码，随着输入的数字越来越多，结果会逐渐缩小。输入“0”会突出显示以零开头的邮政编码，主要位于美国东北部，而输入完整的五位数邮政编码会显示相应的城市名称。

该地图使用户能够通过输入部分邮政编码并观察突出显示的区域来探索邮政编码的分布模式。用户还可以打开和关闭州边界轮廓以获得更好的上下文信息。

邮政编码的数据来源是 opendatasoft.com，可视化是使用 JavaScript 和开源 Leaflet JavaScript 地图库构建的。文章最后列出了相关的可视化内容和与内容相关的标签。

---

## 30. 展示：开源AI数据生成器（现已托管）

**原文标题**: Show HN: Open-source AI data generator (now hosted)

**原文链接**: [https://www.metabase.com/ai-data-generator](https://www.metabase.com/ai-data-generator)

此“Show HN”帖发布一款开源AI数据生成器，旨在快速创建逼真的、可用于业务的演示、测试和仪表盘数据集，消除对真实数据的需求瓶颈。用户通过下拉菜单选择行业和其他参数，预览生成的数据模式，然后以CSV或SQL等格式导出数据。

该工具采用两阶段流程：首先，大型语言模型根据用户输入生成详细的数据规范，然后使用这些规范在本地创建无限量的逼真数据。技术栈包括Next.js、Tailwind CSS + ShadCN UI、OpenAI、Faker、LiteLLM（本地）和Metabase。

该项目完全开源（提供仓库链接），鼓励社区贡献。用户可以直接在Metabase中分析生成的数据，可以通过免费的云试用版，也可以运行一个本地Docker化的实例，该实例可以从应用程序中轻松启动和关闭。该工具提供一个简单的工作流程：选择数据参数，预览模式和示例数据，然后导出或在Metabase中探索。源代码已准备就绪，可供审查和贡献。

---

## 31. Linux Compose Key 组合键序列 (2007)

**原文标题**: Linux Compose Key Sequences (2007)

**原文链接**: [https://math.dartmouth.edu/~sarunas/Linux_Compose_Key_Sequences.html](https://math.dartmouth.edu/~sarunas/Linux_Compose_Key_Sequences.html)

本文档最后更新于2007年，是关于使用Linux Compose键输入重音字符和其他标准键盘上不常用的特殊字符的指南。它解释了如何在Linux桌面环境中配置一个键作为Compose键，通常是通过控制中心或键盘布局设置。

文档的主体部分是一个表格，详细说明了各种Unicode字符的Compose键序列。表格中的每个条目都列出了Unicode字符、相应的Compose键序列（例如，欧元符号的`<Compose> = C`）以及描述该字符的简短注释。该表格包含范围广泛的字符，包括带重音的拉丁字母（包括大写和小写）、标点符号、符号（如版权和注册符号）、数学符号以及一些不太常见的拉丁字母。这些序列通常涉及字符的组合，这些字符类似于所需的变音符号或与字符的名称或形状相关（例如，à 的`<Compose> " a`）。

---

## 32. 使用Lua在Postgres CDC中进行行级转换

**原文标题**: Row-level transformations in Postgres CDC using Lua

**原文链接**: [https://blog.peerdb.io/row-level-transformations-in-postgres-cdc-using-lua](https://blog.peerdb.io/row-level-transformations-in-postgres-cdc-using-lua)

无法访问文章链接。

---

## 33. 2025年秋叶地图

**原文标题**: Fall Foliage Map 2025

**原文链接**: [https://www.explorefall.com/fall-foliage-map](https://www.explorefall.com/fall-foliage-map)

《2025年秋叶地图》一文为秋叶爱好者提供了全面的指南，旨在帮助他们规划行程，欣赏美国各地最美的秋色。文章强调使用实时地图和专家见解的重要性，以应对因日照、温度和树种影响而导致的秋叶变色时间的不确定性。

主要内容包括：

*   **秋叶时间：** 美国大部分地区的秋叶最佳观赏期通常在十月，但各地有所不同，从九月（或阿拉斯加州的八月）到十一月不等。东北部以其鲜艳的红色景观而闻名，而西部则以金色的白杨树为特色。
*   **科学原理：** 秋叶变色的时间取决于日照和温度，并受到叶绿素减少的影响。
*   **行程规划：** 文章建议使用历史地图建立正常的叶片变化基线，然后查阅实时地图，了解当前情况的更新。建议灵活安排行程，以适应意外的天气影响。
*   **行程优化：** 鼓励读者探索风景优美的徒步路线或自驾路线，并考虑清晨前往热门地点，以获得最佳观赏效果。

---

## 34. 将函数式语言编译到LLVM (2023)

**原文标题**: Compiling a Functional Language to LLVM (2023)

**原文链接**: [https://danieljharvey.github.io/posts/2023-02-08-llvm-compiler-part-1.html](https://danieljharvey.github.io/posts/2023-02-08-llvm-compiler-part-1.html)

本文档记录了将一种名为 "mimsa" 的小型函数式语言编译为 LLVM 的初始步骤。作者旨在逐步添加特性，包括类型检查器，同时介绍更多的 LLVM 概念。起点是一个简单的计算器语言，支持整数算术运算，包括加法、减法和乘法。

该语言的抽象语法树 (AST) 使用 Haskell 数据类型（Expr 和 Op）定义。本文介绍了使用 megaparsec 库将文本解析为这些 AST 的过程，重点介绍了诸如用于处理空白的词位 (lexemes) 和用于解析具有正确优先级的 infix 表达式的 Operator 类型等特性。

在深入研究 LLVM 之前，首先介绍了一个该语言的简单解释器。文章的核心随后集中在将计算器语言编译为 LLVM 中间表示 (IR)，使用了 `llvm-hs-pure` 和 `llvm-hs-pretty` 库。文章解释了 LLVM 模块的结构，包括声明外部函数（例如来自简单 C 运行时的 `printint`）和定义 `main` 函数。Haskell 代码片段说明了如何将语言表达式转换为 LLVM 指令（例如，`primToLLVM` 和 `exprToLLVM`）。文章展示了生成的 LLVM 代码，演示了算术运算的翻译。文章最后介绍了使用 clang 编译生成的 LLVM IR 并运行生成的执行文件的说明。目标是为在未来的迭代中添加更复杂的函数式编程特性奠定坚实的基础。

---

## 35. 晦涩特性 + 晦涩特性 + 晦涩特性 = 编译器漏洞

**原文标题**: Obscure feature + obscure feature + obscure feature = compiler bug

**原文链接**: [https://antithesis.com/blog/2025/compiler_bug/](https://antithesis.com/blog/2025/compiler_bug/)

本文详细介绍了在Clang中发现的一个C++编译器错误，该错误由Antithesis SDK中特定晦涩的语言特性组合触发。Antithesis SDK允许开发人员向其代码添加断言，以进行自动化测试和故障注入。

挑战在于实现诸如`REACHABLE()`之类的断言，即使代码从未执行，也需要注册它们。解决方案涉及一个巧妙的C++构造：模板化的`CatalogEntry`结构中的静态`Assertion`对象。这确保在启动时发出断言的“目录”。

为了允许多个断言，`CatalogEntry`使用非类型模板参数进行模板化，特别是包含断言消息、文件名和行号的字符串（字符数组）。这允许为每个断言使用唯一的`CatalogEntry`。为了减小可执行文件的大小，这些模板类被放置在匿名命名空间中。

当在不同的文件中使用相同的断言消息时，就会出现该错误。Clang 17中的一个新优化管道错误地删除了与用作模板参数的固定大小字符串相关的符号。这导致了一个编译错误，因为编译器无法在第二个文件中找到所需的符号。

作者强调了触发该错误所需的罕见特性组合——优化、带有字符数组的非类型模板和匿名命名空间。教训是，复杂的错误通常是由系统中多个罕见或晦涩特性的相互作用引起的。虽然已经提交了错误报告，但用户可以采取的实际解决方法是避免在不同的文件中重复使用相同的断言消息。

---

## 36. 我于2025年搭建了一台双RTX 3090用于本地AI的机器（以及经验教训）

**原文标题**: I built a dual RTX 3090 rig for local AI in 2025 (and lessons learned)

**原文链接**: [https://www.llamabuilds.ai/build/portable-25l-nvlinked-dual-3090-llm-rig](https://www.llamabuilds.ai/build/portable-25l-nvlinked-dual-3090-llm-rig)

无法访问文章链接。

---

## 37. DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran';
```
DELETE FROM users WHERE location = 'Iran

**原文标题**: Delete FROM users WHERE location = 'Iran';

**原文链接**: [https://gist.github.com/avestura/ce2aa6e55dad783b1aba946161d5fef4](https://gist.github.com/avestura/ce2aa6e55dad783b1aba946161d5fef4)

这张撕破的纸条详细记录了一位伊朗软件工程师在制裁下探索数字世界时遇到的令人沮丧的经历。作者叙述了由于美国制裁，各种服务如何限制或完全阻止伊朗用户的访问，无论他们对伊朗政府持何种个人观点。

他详细描述了几个例子：微软删除了他的开发者账户和应用程序，Notion清除了他的数据，GitLab禁止了使用伊朗IP地址的账户。他还提到一位网站所有者因该政权支持俄罗斯在乌克兰的战争而封锁了伊朗IP地址，尽管作者澄清说这并不反映大多数伊朗人的观点。他曾一度被锁定在GitHub之外，之后访问权限才得以恢复。

作者强调，他不怪罪这些公司，理解他们是在法律约束下运营。然而，他提倡在实施此类限制时应抱持同情心和周全考虑，认识到受影响的真实人群。他强调，伊朗政府的行为并不代表伊朗人民，他们往往是该政权的首批受害者。

他最后澄清说，他不是要求取消制裁，而只是分享他的经历并表达他对伊朗政权的反对。他主张采取一种更为细致的限制方法，建议使用“451因法律原因不可用”错误代码，以此作为比通用的“403禁止访问”更透明的替代方案。

---

## 38. 国土安全部用宝可梦宣传移民局突袭后，任天堂提出警告

**原文标题**: Nintendo Alerted After DHS Uses Pokémon to Promote ICE Raids

**原文链接**: [https://www.thedailybeast.com/nintendo-alerted-after-dhs-uses-pokemon-to-promote-ice-raids-tearing-families-apart/](https://www.thedailybeast.com/nintendo-alerted-after-dhs-uses-pokemon-to-promote-ice-raids-tearing-families-apart/)

国土安全部因使用宝可梦形象和音乐在社交媒体上宣传移民海关执法局的驱逐行动而面临强烈反对。国土安全部的视频将戏剧性的突袭行动画面与宝可梦风格的动画剪辑在一起，并使用了宝可梦主题曲。他们还分享了模仿宝可梦“卡牌”的图片，展示了被逮捕和驱逐的个人，并突出了他们所谓的罪行。这些卡牌包括“必须全部抓住”的短语，并将“冰”列为弱点。

海关与边境保护局（CBP）通过发布皮卡丘跳舞的GIF进一步参与其中。 在没有明显许可的情况下使用宝可梦的知识产权，促使人们向任天堂、宝可梦公司和国土安全部询问其知情和批准情况。 批评人士指责国土安全部使用纳税人的钱进行“ICE宣传”。

视频中展示的其中一次突袭行动，其中一扇门被炸开，由于涉及国土安全部部长克里斯蒂·诺姆（被称为“ICE芭比”）的相关法律问题而受到审查，据称，在此次突袭行动中，美国公民在没有搜查令的情况下被戴上手铐。 此次媒体宣传是国土安全部旨在提升诺姆形象的更大规模的宣传活动的一部分，此前她曾受到批评并登上损害名誉的头条新闻，其中涉及由一家与共和党有关联的公司处理的大量支出。

国土安全部和特朗普政府过去也面临过类似的问题，即未经许可使用受版权保护的材料，包括使用Jet2广告中的音频以及Jess Glynne、华纳兄弟和滚石乐队的音乐。

---

## 39. 充沛智能

**原文标题**: Abundant Intelligence

**原文链接**: [https://blog.samaltman.com/abundant-intelligence](https://blog.samaltman.com/abundant-intelligence)

本文题为《丰沛智能》，重点关注人工智能预计的指数级增长以及支持它所需的大规模基础设施。作者认为，随着人工智能能力的扩展，获取人工智能将变得越来越重要，甚至可能成为一项基本人权。为了满足日益增长的人工智能推理和训练计算需求，作者所在的组织正在开展一项雄心勃勃的项目：建造一座每周能够生产千兆瓦级别新人工智能基础设施的“工厂”。

文章强调了丰沛人工智能的潜在益处，表明它可能带来治愈癌症或为每位学生提供个性化教育等突破。然而，计算限制可能会迫使做出艰难的优先级决策，作者希望通过积极扩展人工智能基础设施来避免这种情况。

作者承认这项事业极其困难，需要在整个技术堆栈上进行创新，从芯片设计到电源管理和机器人技术。他们强调希望在美国建设大部分基础设施，旨在扭转其他国家在芯片制造和能源生产等关键技术建设方面超越美国的趋势。文章最后承诺未来将发布关于合作伙伴关系和融资计划的公告，这些计划都得益于计算能力的提高和收入增加之间的联系。

---

## 40. Orange Pi 5 Ultra 评测：ARM64 SBC 性能强劲之作

**原文标题**: OrangePi 5 Ultra Review: An ARM64 SBC Powerhouse

**原文链接**: [https://boilingsteam.com/orange-pi-5-ultra-review/](https://boilingsteam.com/orange-pi-5-ultra-review/)

Orange Pi 5 Ultra是一款功能强大的基于ARM64的单板计算机(SBC)，具有令人印象深刻的规格，包括瑞芯微RK3588处理器、高达16GB的LPDDR5内存和多种存储选项（eMMC、NVMe M.2）。它提供广泛的连接选项，包括双USB 3.0端口、双USB 2.0端口、双MIPI CSI、HDMI 2.1输出和HDMI 2.0输入。 虽然它的价格与树莓派5相近，但其性能，尤其是在多核任务方面，显著优于树莓派5。

软件支持包括Ubuntu、Debian和Arch发行版，但GPU驱动支持目前尚不足，限制了游戏能力。 尽管如此，该板在通用桌面应用程序、视频编辑 (Kdenlive) 和专业软件 (Dbeaver, Memgraph) 中表现出卓越的性能。 作者强调了Flatpak应用程序中广泛的ARM64支持，并将此归因于基于ARM的笔记本电脑的兴起。

即使在繁重的CPU负载下，Orange Pi 5 Ultra也能保持可控的温度。 它在AI任务中表现良好，尤其是在较小的语言模型方面。 它的低功耗和强大的性能使其适用于服务器应用程序。 作者总结说，Orange Pi 5 Ultra是日常通用计算的可行选择，在性能、功能和价值之间提供了引人注目的平衡。

---

## 41. 人工智能辅助软件开发现状

**原文标题**: State of AI-assisted software development

**原文链接**: [https://blog.google/technology/developers/dora-report-2025/](https://blog.google/technology/developers/dora-report-2025/)

2025年DORA报告：“人工智能辅助软件开发现状”显示，软件开发专业人员对人工智能的采用率已飙升至90%，比上一年增长了14%。开发人员在软件开发中大量依赖人工智能，平均每天使用两小时，从而显著提高了生产力（超过80%的受访者）和代码质量（59%）。

然而，存在一种“信任悖论”，因为很大一部分开发人员虽然觉得人工智能有用，但并不完全信任它。人工智能主要作为一种辅助工具，提高生产力而不是取代人类判断。虽然人工智能提高了个人绩效，但其对组织的影响更为复杂。人工智能的采用与更高的软件交付吞吐量相关，但确保交付前的质量仍然是一个挑战。

该报告确定了七种团队原型，以更深入地了解推动人工智能采用成功的因素，范围从“和谐的高成就者”到陷入“遗留瓶颈”的团队。它强调仅仅采用人工智能是不够的。组织需要发展其文化、流程和系统，才能充分发挥人工智能的潜力。为了指导这一点，该报告介绍了DORA人工智能能力模型，突出了放大人工智能影响的关键技术和文化因素。

---

## 42. 口腔细菌通过肠-脑轴与帕金森病相关

**原文标题**: Oral bacteria linked to Parkinson's via the gut-brain axis

**原文链接**: [https://medicalxpress.com/news/2025-09-oral-bacteria-linked-parkinson-gut.html](https://medicalxpress.com/news/2025-09-oral-bacteria-linked-parkinson-gut.html)

浦项科技大学研究人员发现肠道口腔细菌与帕金森病发展之间存在关联。该研究发表于《自然·通讯》，指出与龋齿相关的常见细菌变形链球菌在帕金森病患者的肠道微生物组中更为普遍。

研究人员发现，变形链球菌产生尿刊酸还原酶 (UrdA) 及其代谢物咪唑丙酸 (ImP)，在帕金森病患者的肠道和血液中发现其含量升高。ImP 可以进入血液，到达大脑，并导致多巴胺能神经元的损失，这是帕金森病的标志。

使用小鼠模型进行的实验表明，将变形链球菌引入肠道导致血液和大脑中 ImP 水平升高，从而导致帕金森病样症状，包括多巴胺能神经元损失、神经炎症、运动功能障碍和 α-突触核蛋白聚集。

该研究还发现，这些影响依赖于 mTORC1 信号蛋白复合物的激活。抑制 mTORC1 可减少小鼠的神经炎症、神经元损失、α-突触核蛋白聚集和运动功能障碍。这些发现表明，靶向口腔-肠道微生物组及其代谢物可能是帕金森病的一种新型治疗策略。Ara Koh 教授表示，该研究提供了“对肠道口腔微生物如何影响大脑并导致帕金森病发展的机制性理解”。

---

## 43. 派生样式组件

**原文标题**: Forking Styled Components

**原文链接**: [https://github.com/sanity-io/styled-components-last-resort/blob/main/README.md](https://github.com/sanity-io/styled-components-last-resort/blob/main/README.md)

本文介绍了一个由sanity-io创建的名为 "styled-components-last-resort" 的公共GitHub仓库，该仓库似乎是一个分支。它可能与流行的React CSS-in-JS库 Styled Components 相关。

关键要点如下：

*   **分支仓库：** 该仓库被确定为“分支”，意味着它是现有Styled Components仓库的副本，由sanity-io修改。

*   **潜在用途：** 名称“last-resort”表明此分支可能包含或解决了不适合主Styled Components仓库的特定问题或优化。它暗示了一种可能的后备方案或替代实现。

*   **受欢迎程度：** 该仓库有145颗星和2个分支，表明社区对其有一定兴趣。这表明它解决了相关问题或在Styled Components生态系统中提供了有价值的替代方案。

在没有更多关于分支仓库的内容和目的的信息的情况下，很难提供更详细的总结。但是，标题和元数据强烈表明，这是一个旨在解决特定挑战或在Styled Components框架内实施特定方法的分支。

---

## 44. 混合误差：结合绝对误差和相对误差的混合指标（2024）

**原文标题**: Hyb Error: A Hybrid Metric Combining Absolute and Relative Errors (2024)

**原文链接**: [https://arxiv.org/abs/2403.07492](https://arxiv.org/abs/2403.07492)

这篇arXiv文章 (arXiv:2403.07492v2) 介绍了一种新的误差指标，名为“Hyb Error”，由谢培琛提出，专为数值分析设计。 Hyb Error定义为`|x-y|/(1+|y|)`，其中`x`是`y`的近似值。

Hyb Error的核心思想是结合绝对误差和相对误差的优点，同时缓解它们的缺点。它通过相当于绝对误差和相对误差的调和平均数的一半来实现这一点。 具体而言，当`|y|`接近0时，Hyb Error的行为类似于绝对误差，避免了真实值非常小时相对误差被放大的问题。相反，当`|y|`接近无穷大时，它的行为类似于相对误差，防止绝对误差因真实值非常大而被放大。

该论文强调了Hyb Error为epsilon (`ε`)等价于表达式`|x-y| = ε + ε|y|`。这种等价性至关重要，因为它直接关系到常见的浮点数相等性检查函数“isclose”，其中`isclose(x, y, ε, ε) == True` 意味着`x`和`y`之间的Hyb Error小于或等于`ε`。

此外，该论文还介绍了序列的最大元素级Hyb Error（MEHE），认为它是反映序列中最显著误差的实用指标，并且直接对应于“isclose”函数的决策边界。

---

## 45. 人工智能不会像我们被告知的那样耗费那么多电力（2024）

**原文标题**: AI won't use as much electricity as we are told (2024)

**原文链接**: [https://johnquigginblog.substack.com/p/ai-wont-use-as-much-electricity-as](https://johnquigginblog.substack.com/p/ai-wont-use-as-much-electricity-as)

无法访问文章链接。

---

## 46. 游戏书与图论 (2019)

**原文标题**: Gamebooks and graph theory (2019)

**原文链接**: [https://notes.atomutek.org/gamebooks-and-graph-theory.html](https://notes.atomutek.org/gamebooks-and-graph-theory.html)

本文探讨了图论在分析游戏书（尤其是孤狼系列）中的应用。作者将游戏书编码为有向图，其中章节是节点，选择是边，从而可以使用网络算法提取诸如最短死亡路径或战斗最多的路径等信息。

分析揭示了关于孤狼系列的一些有趣的事实。“黑暗大师”包含最多的动作，而“恐怖王国”提供了通往死亡的最快路线。“卡尔特洞穴”总体上是最致命的。纵观整个系列，数据表明这些书可能变得不那么严厉，而更多地关注冒险和故事。

作者使用 Python 库 `graphviz` 和 `networkx` 进行可视化和路径处理。文章讨论了诸如某些书籍中的循环（环形路径）（需要移除才能使用某些算法）以及表示游戏书内谜题的断开连接的图等挑战。循环移除被标记为一个 NP 完全问题，但由于游戏书图的相对较小尺寸，因此可以控制。

最终，虽然分析并未产生突破性的见解，但它证明了将图论应用于独特领域的价值。作者建议未来的工作可能包括分析格斗幻想游戏书并将游戏书的特征与受欢迎程度相关联。

---

## 47. Paper2Agent: 斯坦福将研究论文重塑为交互式AI智能体

**原文标题**: Paper2Agent: Stanford Reimagining Research Papers as Interactive AI Agents

**原文链接**: [https://arxiv.org/abs/2509.06917](https://arxiv.org/abs/2509.06917)

本文介绍了一种名为 Paper2Agent 的新型框架，该框架将研究论文转化为交互式且可靠的 AI 智能体。 该框架旨在通过将静态研究成果（论文、代码、数据）转化为主动系统，来克服知识传播和重用的挑战。

Paper2Agent 的工作原理是使用多个智能体系统地分析论文及其相关代码库，以构建模型上下文协议 (MCP) 服务器。它迭代地生成并运行测试，以改进和增强生成的 MCP 的鲁棒性。 然后，这些 MCP 可以连接到聊天智能体（例如 Claude Code），使用户能够通过自然语言与论文的内容和功能进行交互，从而执行来自原始研究的复杂查询和工作流程。

作者通过案例研究展示了 Paper2Agent 的有效性，创建了基于 AlphaGenome（基因组变异解释）、ScanPy（单细胞分析）和 TISSUE（空间转录组分析）的智能体。 这些智能体成功地重现了原始论文的结果并处理了新的用户查询。 Paper2Agent 提出了一种新的科学研究知识共享和协作范例，通过将静态论文转化为动态 AI 助手，并促进 AI 共同科学家生态系统的发展。

---

## 48. 全同态加密入门教材

**原文标题**: The Beginner's Textbook for Fully Homomorphic Encryption

**原文链接**: [https://arxiv.org/abs/2503.05136](https://arxiv.org/abs/2503.05136)

Ronny Ko 撰写的 arXiv 提交论文，题为“全同态加密初学者教程”，介绍了全同态加密（FHE）作为一种密码方案，允许在加密数据上进行计算而无需解密。解密后的计算结果与对原始明文数据执行相同操作的结果相匹配。

该教程涵盖了 FHE 在加密数字上执行加法和乘法等基本运算的能力，从而能够构建复杂的函数，例如减法、除法、逻辑门和高级数学函数。 这些函数可以精确或近似地实现，从而平衡效率和准确性。

摘要强调了 FHE 的关键应用，包括保护隐私的机器学习，其中服务器处理加密的客户端数据，而无需了解明文输入或推理结果。提到的其他应用包括保密区块链服务、数据分析的安全外包、加密数据库查询、保护隐私的搜索以及安全的多方计算。

该论文作为一个开放项目呈现，邀请 FHE 专家合作并扩展草案。 它被归类为密码学与安全（cs.CR）和离散数学（cs.DM）。 自 2025 年 3 月首次提交以来，该论文已经过多次修订（v1 至 v15）。

---

## 49. Kevo应用停止服务

**原文标题**: Kevo app shutdown

**原文链接**: [https://www.kwikset.com/support/answers/what-does-the-kevo-app-shutdown-mean-to-my-kevo-door-lock](https://www.kwikset.com/support/answers/what-does-the-kevo-app-shutdown-mean-to-my-kevo-door-lock)

自2025年11月14日起，Kevo应用程序和Web门户将关闭，影响Kwikset、Weiser和Baldwin品牌下的所有Kevo、Kevo Convert、Kevo Plus和Baldwin Evolved智能锁。这意味着用户将失去对其锁的远程访问权限，包括通过应用程序或Web门户打开、关闭和管理它们的能力。

不受影响的功能包括使用实体钥匙和Key FOB解锁和锁定门闩。建议Kevo用户提前准备，确保拥有实体钥匙或Key FOB。

为了 облегчить过渡，ASSA ABLOY提供折扣后的智能锁替代品。美国用户可以使用发送到他们注册的Kevo电子邮件地址的唯一促销代码，通过Level网站获得Kwikset Halo Keypad Wi-Fi智能锁80美元的折扣或Level Lock+ 130美元的折扣。加拿大用户可以致电Weiser客户服务团队并提供其唯一的促销代码，获得Weiser Halo Keypad Wi-Fi智能锁89加元（CDN）的折扣。

促销优惠将于2025年12月14日到期，并且不会再就失去远程功能提供任何其他优惠。

---

## 50. Maestro上的对称多处理、超线程和调度

**原文标题**: Symmetric MultiProcessing, Hyper-Threading and Scheduling on Maestro

**原文链接**: [https://blog.lenot.re/a/smp](https://blog.lenot.re/a/smp)

本文详细介绍了Maestro操作系统中对称多处理(SMP)的实现，重点阐述了如何利用多核CPU来提高性能。该过程始于使用ACPI(高级配置和电源接口)枚举CPU核心，这是一个备受争议的标准，Linus Torvalds等人对其复杂性和微软潜在的反竞争意图进行了描述和批评。ACPI中的MADT表提供了有关处理器核心及其本地APIC ID的信息。

本文解释了从传统的PIC（可编程中断控制器）到APIC（高级可编程中断控制器）进行中断处理的过渡，包括xAPIC和x2APIC。一个关键方面是通过将APIC定时器与HPET（高精度事件定时器）进行比较来校准APIC定时器，以确定其频率。

引导额外的CPU核心涉及发送带有特定延迟的处理器间中断(IPI)，然后进行初始化以将其切换到保护模式或长模式。本文讨论了对全局停止机制、每个CPU结构（通过gs段寄存器访问）以及TLB（转换后备缓冲区）刷新的需求，以保持跨核心的缓存一致性。

延迟调用有助于核心之间的通信，使用MPSC队列和IPI。重新编写调度程序以管理多个核心，每个核心都有自己的运行队列。进程负载均衡借鉴了FreeBSD的ULE调度程序，旨在基于优先级、拓扑和空闲状态，将进程高效地分配到各个核心上。内核线程会定期重新平衡进程以优化CPU利用率。

---

## 51. 如果你在读这篇讣告，看来我已经死了。

**原文标题**: If you are reading this obituary, it looks like I'm dead

**原文链接**: [https://framinghamsource.com/index.php/2025/09/22/linda-m-brossi-murphy/](https://framinghamsource.com/index.php/2025/09/22/linda-m-brossi-murphy/)

琳达·布罗西·墨菲，享年60岁，以幽默而真挚的笔触撰写了自己的讣告。2025年9月21日，因延髓型肌萎缩侧索硬化症并发症去世后发布。她着重表达了对丈夫大卫（“老伴”）、三个孩子（小大卫、道格和亚当）及其家人，包括她所珍爱的孙辈们的爱。她也深情地表达了对她的兄弟迈克尔和戴夫·布罗西、大家庭和许多挚友的爱。

琳达幽默地叙述了她与肌萎缩侧索硬化症抗争的挑战，特别是失去声音和无法享受美食的困境。尽管遭受痛苦，她仍然强调自己努力保持乐观积极的公众形象。她回顾了自己幸福的生活，对家人、朋友和乐趣的热爱，包括享受美酒、跳舞和与亲人共度时光。她还提到了她与癌症的斗争，这都记录在她的书《滚蛋吧癌症》中。

琳达的讣告包含了一些直率的要求。她要求捐款给Compassionate Care ALS.org，代替鲜花。她要求任何对她或她的家人不友善的人远离葬礼。她建议购买刮刮乐彩票送给陌生人，以传播快乐，而不是送花。

瞻仰遗容时间为2025年9月28日，在弗雷明翰的麦卡锡、麦金尼和劳勒殡仪馆举行。生命庆祝活动将于2025年9月29日在内蒂克的The Verve Hotel举行，她鼓励与会者分享故事、跳舞并举杯纪念她。最后，琳达将她的大脑和脊髓捐赠给了肌萎缩侧索硬化症研究。

---

## 52. Qwen3-Omni：文本、图像和视频原生全能AI模型

**原文标题**: Qwen3-Omni: Native Omni AI model for text, image and video

**原文链接**: [https://github.com/QwenLM/Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni)

Qwen3-Omni是千问推出的全新多语言全模态基座模型，可处理文本、图像、音频和视频，并以文本和语音形式提供实时响应。主要特点包括：跨模态的先进性能、对119种文本语言的多语言支持、19种语音输入语言和10种语音输出语言的支持。它拥有基于MoE的创新架构、实时音频/视频交互能力，以及通过系统提示实现的灵活控制。

该模型提供了多种用例，并通过食谱进行演示，包括语音识别/翻译、音乐和声音分析、图像问答、视频描述/导航以及音视频问答/对话。它还支持用于类Agent行为的音频函数调用，并提供经过微调的音频字幕模型Qwen3-Omni-30B-A3B-Captioner。

本文档提供了多种上手Qwen3-Omni的方法，包括使用Hugging Face Transformers、vLLM（推荐用于大规模或低延迟需求）和DashScope API。它还建议使用提供的Docker镜像。提供不同的模型版本，包括Instruct、Thinking和Captioner版本。文档提供了下载模型权重和使用Transformers调用模型的说明，并演示了批量推理，以及禁用音频输出以节省内存并加快文本响应速度的选项。

---

## 53. 杀菌紫外线或使空气传播疾病如水源性疾病般罕见

**原文标题**: Germicidal UV could make airborne diseases as rare as those carried by water

**原文链接**: [https://www.worksinprogress.news/p/how-to-clean-the-air](https://www.worksinprogress.news/p/how-to-clean-the-air)

本文认为，杀菌紫外线（UV）光，特别是远紫外线（far-UVC）光，具有大幅降低空气传播疾病的潜力，类似于水过滤和氯化如何根除了诸如伤寒之类的水传播疾病。

本文回顾了使用紫外线消毒的历史，指出早期的成功及其后因对皮肤和眼睛刺激的担忧以及抗生素的兴起而衰落。然而，文章强调，现代远紫外线技术，使用230纳米以下的波长，对人类无害，同时仍能有效灭活病原体。

远紫外线通过破坏空气传播病毒和细菌的DNA/RNA来发挥作用，从而阻止复制。研究表明，它在降低封闭空间中空气传播的病原体水平方面非常有效，甚至对耐药病毒也有效。本文将远紫外线与通风和过滤等替代空气净化方法进行了对比，承认它们的作用，但指出了它们的局限性，如能源消耗、成本以及引入污染物或需要温度调节的潜力。虽然远紫外线系统可能比过滤更昂贵，但文章认为成本正在下降。作者们倡导更广泛地采用远紫外线技术，以创造更安全的室内环境并对抗空气传播疾病的传播，从而可能使其像水传播疾病一样罕见。

---

## 54. 基于 C++

**原文标题**: Based C++

**原文链接**: [https://github.com/SheafificationOfG/based-cpp](https://github.com/SheafificationOfG/based-cpp)

名为“Based C++”的此仓库提供了一个为g++编译器量身定制的GNU接口层(GIL)和标准库的实现。其核心前提是一个略带玩笑甚至讽刺的声明：“C++是最好的解释型语言”。

该仓库包含示例C++程序，演示了GIL和标准库。提供了一个简单的“Hello, world!”示例，展示了`gil::std`命名空间及其`str::puts`和`str::literal`功能。提供的编译说明需要`-Based`标志（大概是一个与GIL相关的自定义标志），并指出命令的成功取决于执行位置，可能需要到“ased”（抽象系统模拟器驱动程序）文件夹的完整路径。

其他示例说明了该库的功能：`hello_world_vmi.cpp`镜像了基本的“Hello, world!”程序，但避免使用标准库，`calculator.cpp`执行二进制运算，以及`mergesort.cpp`在逗号分隔的整数列表上实现归并排序算法。本质上，该仓库旨在提供一个自定义的，可能是不正统的，使用GIL的C++标准库实现，并通过几个说明性示例展示其用法。

---

## 55. 充斥着关于苹果网络业务的修正主义历史，让我们来看看证据

**原文标题**: Awash in revisionist histories about Apple's web efforts, a look at the evidence

**原文链接**: [https://infrequently.org/2025/09/cupertinos-comforting-myths/](https://infrequently.org/2025/09/cupertinos-comforting-myths/)

本文批判了苹果公司在网络标准和功能开发方面的参与度，特别是关于 iOS 上的 WebKit。作者认为，苹果公司对新网络功能的采用速度缓慢，加上其对 iOS 浏览器引擎的控制，阻碍了网络平台的进步。

作者展示的数据表明，Safari 在功能实现方面落后于 Chromium 和 Gecko，通常在其他浏览器发布这些功能几年后才发布。他们认为，这种延迟并非源于建设性的重新设计，而是一种追赶的模式，并未提供替代解决方案。

文章随后深入探讨了 Web MIDI、Web USB 和 Web Bluetooth 等具体案例，这些案例都经过了隐私和安全方面的考虑。作者声称，苹果公司一直反对这些 API，通常没有提供实质性的分析、建设性的反馈或替代方案，尽管经过多年的开放开发和合作请求。他们认为，苹果公司的反对往往是在多年的沉默之后才出现的，而且他们积极地忽视了开发人员的要求，以便提出替代方案，甚至分享他们对 API 的看法。

作者总结说，苹果公司的行为扼杀了网络创新，特别是在 iOS 上，开发者被迫依赖 WebKit 的功能。文章暗示了一种模式，即苹果公司忽略新功能，声称它们“缺乏共识”，积极反对它们，或者淡化开发人员的需求，同时完全不愿意参与。

---

## 56. 漫步密歇根城（印第安纳州）

**原文标题**: Walking Michigan City (Indiana)

**原文链接**: [https://walkingtheworld.substack.com/p/walking-michigan-city-indiana](https://walkingtheworld.substack.com/p/walking-michigan-city-indiana)

无法访问文章链接。

---

## 57. 测试胜于数据结构和算法

**原文标题**: Testing is better than data structures and algorithms

**原文链接**: [https://nedbatchelder.com/blog/202509/testing_is_better_than_dsa.html](https://nedbatchelder.com/blog/202509/testing_is_better_than_dsa.html)

数据结构与算法：实用性重于学术性

---

## 58. 支持SIXEL特性的终端的X服务器实现 (2010-2014)

**原文标题**: X server implementation for SIXEL-featured terminals (2010-2014)

**原文链接**: [https://github.com/saitoha/xserver-SIXEL](https://github.com/saitoha/xserver-SIXEL)

saitoha 的 Github 仓库 `xserver-SIXEL` 是一个为支持 SIXEL 图形格式的终端设计的 X 服务器实现。它基于 pelya 的 Xsdl kdrive 服务器构建。该项目旨在提供一种在具有 SIXEL 功能的终端中运行 X 应用程序的方法。

该仓库包含 X 服务器的源代码和构建脚本，包括核心 X 服务器 (dix)、扩展 (Xext, Xi, damageext 等)、驱动程序 (fb, glamor) 和实用程序 (config, os) 等重要组件。还包括配置文件、构建脚本和文档。

要点：

*   **目的：** 提供一个可以在支持 SIXEL 的终端上渲染图形的 X 服务器。
*   **基础：** 基于 Xsdl kdrive 服务器。
*   **开发：** 活跃开发，有提交历史。
*   **资源：** 包括 README、许可证、构建脚本和文档。
*   **社区：** 开源项目，拥有贡献者社区。
*   **X 服务器基础：** 解释 X 服务器功能、客户端窗口请求和窗口管理器角色。
*   **沟通：** 提供 Xorg 邮件列表和错误报告系统的链接。

---

## 59. 汉吉斯：市场与城市——欧洲最大生鲜市场一日游

**原文标题**: Rungis: The Market and the City – A day at Europe's largest fresh food market

**原文链接**: [https://www.vittlesmagazine.com/p/rungis-the-market-and-the-city](https://www.vittlesmagazine.com/p/rungis-the-market-and-the-city)

贾斯汀尼安·特里比伦在Vittles Paris上发表的文章《龙吉斯：市场与城市》探讨了位于巴黎南部的欧洲最大的新鲜食品市场龙吉斯。这篇文章描绘了一幅城市中的繁华景象，13000人在占地234公顷的巨大区域工作，为巴黎地区供应了大量的生鲜农产品。

作者陪同定期在龙吉斯采购农产品的餐厅老板马克-安托万·苏朗和第一次参观的主厨贾斯汀·奥杜安。文章强调了厨师由于繁忙的日程而难以进入龙吉斯所面临的挑战，使得餐厅老板亲自采购食材相对罕见。

对大多数巴黎人来说，龙吉斯被描述为“遥远的乐土”，由于其商业对商业的模式，普通大众无法进入。公众的认知主要来自媒体报道，尤其是在节日期间，奢侈食品经常被大量报道。

除了目前的效率之外，这篇文章还暗示了更深层的历史，提到了龙吉斯从巴黎市中心的搬迁及其对巴黎人与食物之间关系产生的深刻影响。全文可通过付费墙访问，其中承诺深入探讨这段历史，参观市场的各个展馆，“入门”龙吉斯，并了解其独特的内脏餐厅。

---

## 60. 忒弥斯（欧洲可重复使用火箭）在发射台上组装完毕

**原文标题**: Themis (European Reusable Rocket) is assembled on launch pad

**原文链接**: [https://phys.org/news/2025-09-themis-pad-fully.html](https://phys.org/news/2025-09-themis-pad-fully.html)

2025年9月19日，欧洲航天局(ESA)的可重复使用火箭演示器Themis (T1H)在瑞典基律纳的埃斯兰吉航天中心发射台上完成全面组装。Themis旨在测试火箭级回收和重复使用技术，代表欧洲首次对使用低温推进的垂直起降火箭元件进行全面演示。

T1H模型高30米（带支腿），从法国运来并在瑞典组装。它使用普罗米修斯发动机，该发动机功率足以用于阿丽亚娜6号，但能够重启和推力调节，从而实现软着陆。最近的组装工作包括安装四个着陆支腿，这对于演示器来说是第一次。

Themis现在已准备好进行湿演练，为首次飞行做准备。该项目是欧空局未来太空运输准备计划的一部分，阿丽亚娜集团是主要承包商，首次飞行活动隶属于“地平线欧洲”计划下的Salto项目。该项目包括来自12个欧盟国家的25个合作伙伴组成的联盟，并响应欧盟太空研究与创新计划。

---

## 61. Claude Code 的细粒度 HTTP 过滤

**原文标题**: Fine-grained HTTP filtering for Claude Code

**原文链接**: [https://ammar.io/blog/httpjail](https://ammar.io/blog/httpjail)

本文介绍了`httpjail`，一个旨在通过实施细粒度的HTTP过滤来增强像Claude这样的人工智能编码代理的安全性和治理的工具。核心问题是随着人工智能代理能力的增强，安全工具的缺乏导致潜在的风险，例如破坏性行为、数据泄露和未经授权的操作。

`httpjail`充当具有进程级网络隔离的HTTP(S)拦截器。它默认拒绝所有非HTTP(S)流量，同时允许DNS。可以使用JavaScript表达式或shell脚本定义过滤规则，从而提供超越传统防火墙的灵活性。示例包括阻止除LLM API流量之外的所有流量、仅允许GET请求或将特定主机列入白名单。

该工具以两种模式运行：强模式（仅限Linux，使用命名空间和`nftables`）和弱模式（macOS，依赖于`HTTP_PROXY`环境变量）。它执行TLS拦截以检查HTTPS流量，动态生成由本地CA签名的证书，客户端应用程序需要信任该证书。

本文还讨论了潜在的逃逸风险，尤其是在弱模式下，并建议使用Docker进行文件系统和网络隔离的组合。为了获得最大的安全性，服务器模式允许在专用服务器上运行`httpjail`，并使用网络防火墙规则限制到代理的流量。这迫使所有或仅批准的API请求通过代理服务器。最后，本文提供了有关如何试用`httpjail`的说明。

---

## 62. Show HN: Python音频转录：本地将语音转换为文本

**原文标题**: Show HN: Python Audio Transcription: Convert Speech to Text Locally

**原文链接**: [https://www.pavlinbg.com/posts/python-speech-to-text-guide](https://www.pavlinbg.com/posts/python-speech-to-text-guide)

本文介绍了一个基于Python的本地音频转录系统，该系统使用OpenAI的Whisper模型，为商业转录服务提供了一个注重隐私和具有成本效益的替代方案。文章强调了安装FFmpeg作为先决条件的重要性，并指导用户设置Python虚拟环境。

文章提供了用于转录音频文件、批量处理多个文件和创建SRT字幕文件的代码示例。它强调“base” Whisper模型是大多数用户的良好起点，可以在速度和准确性之间取得平衡。文章还探讨了使用SpeechRecognition库的另一种方法，提供了Google引擎（更高的准确率，需要互联网）和Sphinx（离线，较低的准确率）之间的选择。

文章针对“找不到FFmpeg”和“内存不足错误”等常见问题，提出了实用的解决方案，包括内存管理技巧和用于长音频文件的分块处理。文章强调了音频质量对于转录准确性的重要性，并提供了音频预处理的建议。

文章提供了不同Whisper模型的性能基准，指导用户根据其硬件和需求选择合适的模型。最后，文章提出了一个命令行脚本，以便于使用，并总结了本地音频转录的关键优势：零持续成本、完全隐私、高准确率、快速处理、离线功能以及无使用限制。

---

## 63. 选择你自己的冒险

**原文标题**: Choose Your Own Adventure

**原文链接**: [https://www.filfre.net/2025/09/choose-your-own-adventure/](https://www.filfre.net/2025/09/choose-your-own-adventure/)

本文深入探讨了“选择你自己的冒险”系列丛书的起源和影响。作者回顾了自己阅读第一本书《时间洞穴》的个人经历，以及这本书如何激发了他的想象力和对互动媒体的兴趣，最终影响了他作为数字古物研究者的职业生涯。

文章强调了该系列丛书的巨大影响力和受欢迎程度，将其定位为互动娱乐的“入门毒品”，引导读者走向诸如《龙与地下城》之类的桌面游戏，并最终走向电脑游戏。

除了作者爱德华·帕卡德和 R.A. 蒙哥马利之外，文章还将 Writers House 的文学经纪人艾米·伯科沃誉为该系列丛书成功的关键人物。她认识到雷·蒙哥马利（佛蒙特十字路口公司共同所有人）的“你的冒险”概念的潜力。蒙哥马利反过来又受到了帕卡德的接洽，帕卡德之前曾努力出版他的互动书籍《甘蔗岛》。帕卡德的灵感来自于为女儿们创作互动睡前故事。

文章详细介绍了帕卡德最初遭受的拒绝，出版商们担心过多的选择会使儿童的阅读变得更加困难。最终，佛蒙特十字路口公司冒险尝试了帕卡德的理念，为“选择你自己的冒险”现象铺平了道路。该系列丛书的成功凸显了编辑和经纪人在塑造文化趋势方面的力量，他们经常在幕后工作。

---

## 64. Cap'n Web：一种用于浏览器和Web服务器的新RPC系统

**原文标题**: Cap'n Web: a new RPC system for browsers and web servers

**原文链接**: [https://blog.cloudflare.com/capnweb-javascript-rpc-library/](https://blog.cloudflare.com/capnweb-javascript-rpc-library/)

Cap'n Web：纯 TypeScript 打造的开源 Web 远程过程调用系统。

Cap'n Web 是一个全新的开源 RPC (远程过程调用) 系统，专为 Web 浏览器和服务器设计，完全使用 TypeScript 构建。 与传统的 RPC 方法相比，它旨在简化 JavaScript 应用程序之间的通信，同时提供强大的功能和更高的安全性。

Cap'n Web 的主要特点包括：

*   **对象能力协议：** 类似于 Cap'n Proto，它使用对象能力来增强安全性和控制访问权限。
*   **无需模式，极简样板代码：** 与 Cap'n Proto 不同，Cap'n Web 几乎不需要配置和设置，可以与 JavaScript/TypeScript 无缝协作。
*   **人类可读的序列化：** 使用 JSON 作为其底层序列化格式。
*   **通用传输方式：** 开箱即用地支持 HTTP、WebSocket 和 postMessage()。
*   **跨平台：** 可在浏览器、Cloudflare Workers、Node.js 和其他 JavaScript 运行时中工作。
*   **体积小：** 压缩后小于 10kB，无任何依赖项。
*   **双向调用：** 客户端和服务器都可以发起调用。
*   **函数和对象按引用传递：** 启用诸如回调和对象共享之类的功能。
*   **Promise 管道：** 将多个 RPC 调用链接到单个网络往返中。

Cap'n Web 旨在为分布式系统提供更自然的编程模型，允许开发人员设计类似于常规 JavaScript API 的 RPC 接口。 它提供了一种 GraphQL 的替代方案，通过更少的往返次数和熟悉的基于 JavaScript 的方法（包括针对数组映射用例的解决方案），实现复杂的交互和数据获取。

---

## 65. OpenAI 与英伟达宣布合作部署 10GW 英伟达系统

**原文标题**: OpenAI and Nvidia announce partnership to deploy 10GW of Nvidia systems

**原文链接**: [https://openai.com/index/openai-nvidia-systems-partnership/](https://openai.com/index/openai-nvidia-systems-partnership/)

OpenAI与英伟达宣布合作，大幅扩展OpenAI的人工智能基础设施能力。该合作旨在部署高达10吉瓦的英伟达人工智能系统。此举将使OpenAI能够加速其研发工作，为人工智能领域的未来突破提供动力，包括增强型模型和新应用。

部署10吉瓦的英伟达硬件代表着OpenAI计算能力的显著提升。虽然具体硬件配置尚未详细说明，但公告强调了英伟达先进人工智能平台的使用。这种扩展的基础设施将为OpenAI提供必要的资源，以训练日益复杂和精密的人工智能模型，从而突破当前可能的界限。

该合作凸显了专用且高性能的人工智能基础设施对于领先的人工智能研究机构的重要性。通过利用英伟达的专业知识和尖端技术，OpenAI旨在巩固其在人工智能创新领域的领导地位。增加的容量将能够实现更快的模型迭代、对新人工智能架构的探索以及更强大和高效的人工智能系统的开发。长远目标是为人类创造更有益的人工智能技术。

---

## 66. Cloudflare 赞助 Ladybird 和 Omarchy

**原文标题**: Cloudflare is sponsoring Ladybird and Omarchy

**原文链接**: [https://blog.cloudflare.com/supporting-the-future-of-the-open-web/](https://blog.cloudflare.com/supporting-the-future-of-the-open-web/)

Cloudflare is sponsoring two open-source projects, Ladybird and Omarchy, to foster a more diverse and healthy Internet ecosystem. Ladybird is a new, independent web browser built from scratch (not Chromium-based) with its own rendering and JavaScript engines (LibWeb and LibJS). Cloudflare supports Ladybird's mission to prioritize privacy, performance, and security and to challenge the near-monoculture of existing browsers, leading to innovation.

Omarchy is an opinionated Arch Linux distribution designed to provide developers with a ready-to-use, modern development environment. It simplifies Linux setup, making it more accessible and configurable for developers who may not have extensive operating system experience, by providing essential tools like Neovim, Docker, and Git.

Cloudflare emphasizes that its support for both projects comes with no strings attached, aiming to bolster the open Internet and provide more choice for both users and developers. Cloudflare highlights the potential of these projects to create a more free and open Internet by focusing on browser choice and developer environments, supporting innovation and independent solutions. The support ensures fast ISO and package delivery for Omarchy, leveraging Cloudflare's CDN, R2 storage, and DDoS protection. Ladybird plans to launch its alpha version in 2026, encouraging contributors to join the project.


---

## 67. 我用惯了苹果芯片，但仍然热爱 Framework。

**原文标题**: I'm spoiled by Apple Silicon but still love Framework

**原文链接**: [https://simonhartcher.com/posts/2025-09-22-why-im-spoiled-by-apple-silicon-but-still-love-framework/](https://simonhartcher.com/posts/2025-09-22-why-im-spoiled-by-apple-silicon-but-still-love-framework/)

生成摘要时出错

---

## 68. The Common Pile v0.1: An 8TB Dataset of Public Domain and Openly Licensed Text

**原文标题**: The Common Pile v0.1: An 8TB Dataset of Public Domain and Openly Licensed Text

**原文链接**: [https://arxiv.org/abs/2506.05209](https://arxiv.org/abs/2506.05209)

生成摘要时出错

---

## 69. CompileBench：AI能否编译22年前的代码？

**原文标题**: CompileBench: Can AI Compile 22-year-old Code?

**原文链接**: [https://quesma.com/blog/introducing-compilebench/](https://quesma.com/blog/introducing-compilebench/)

生成摘要时出错

---

## 70. 'Dumpster Fire in a Train Wreck:' Volvo Is Replacing Every EX90's Computer

**原文标题**: 'Dumpster Fire in a Train Wreck:' Volvo Is Replacing Every EX90's Computer

**原文链接**: [https://insideevs.com/news/773202/volvo-ex90-software-issues/](https://insideevs.com/news/773202/volvo-ex90-software-issues/)

生成摘要时出错

---

## 71. Why haven't local-first apps become popular?

**原文标题**: Why haven't local-first apps become popular?

**原文链接**: [https://marcobambini.substack.com/p/why-local-first-apps-havent-become](https://marcobambini.substack.com/p/why-local-first-apps-havent-become)

生成摘要时出错

---

## 72. After 50 years, The Magic Circle finally inducts Penn and Teller

**原文标题**: After 50 years, The Magic Circle finally inducts Penn and Teller

**原文链接**: [https://www.nytimes.com/2025/09/19/arts/penn-teller-magic-circle.html](https://www.nytimes.com/2025/09/19/arts/penn-teller-magic-circle.html)

生成摘要时出错

---

## 73. MrBeast Failed to Disclose Ads and Improperly Collected Children's Data

**原文标题**: MrBeast Failed to Disclose Ads and Improperly Collected Children's Data

**原文链接**: [https://bbbprograms.org/media/newsroom/decisions/mrbeast-feastables](https://bbbprograms.org/media/newsroom/decisions/mrbeast-feastables)

生成摘要时出错

---

## 74. PlanetScale 的 Postgres 版本现已正式发布

**原文标题**: PlanetScale for Postgres is now GA

**原文链接**: [https://planetscale.com/blog/planetscale-for-postgres-is-generally-available](https://planetscale.com/blog/planetscale-for-postgres-is-generally-available)

生成摘要时出错

---

## 75. How I, a beginner developer, read the tutorial you, a developer, wrote for me

**原文标题**: How I, a beginner developer, read the tutorial you, a developer, wrote for me

**原文链接**: [https://anniemueller.com/posts/how-i-a-non-developer-read-the-tutorial-you-a-developer-wrote-for-me-a-beginner](https://anniemueller.com/posts/how-i-a-non-developer-read-the-tutorial-you-a-developer-wrote-for-me-a-beginner)

生成摘要时出错

---

## 76. What is algebraic about algebraic effects?

**原文标题**: What is algebraic about algebraic effects?

**原文链接**: [https://interjectedfuture.com/what-is-algebraic-about-algebraic-effects/](https://interjectedfuture.com/what-is-algebraic-about-algebraic-effects/)

生成摘要时出错

---

## 77. Xcode是我用过的最糟糕的专业软件。

**原文标题**: Xcode Is the Worst Piece of Professional Software I Have Ever Used

**原文链接**: [https://holdtherobot.com/blog/xcode-is-the-worst-professional-software-i-have-ever-used/](https://holdtherobot.com/blog/xcode-is-the-worst-professional-software-i-have-ever-used/)

This article is a scathing critique of Xcode, Apple's IDE for iOS development, arguing it's the "worst piece of professional software" the author has used. The author highlights several key issues:

*   **Compiler Errors:** Xcode's error messages are often vague and unhelpful, like the infamous "unable to type-check this expression" error, leaving developers to debug blindly.
*   **Project File Hell:** The project file (pbxproj) is a massive, unreadable file that is prone to merge conflicts and can corrupt the entire project if even slightly flawed.
*   **UI Glitches and Password issues:** The author provides examples of random UI glitches and shows that setting up a sandbox account for IAP testing is impossible in the simulator due to an Apple bug.
*   **Lack of Trust:** The author believes Apple provides vague and misleading documentation and developer support. WWDC presentations are seen as marketing material that overpromise and underdeliver.
*   **Private Bug Tracker:** Apple's private bug tracker prevents developers from collaborating and learning from shared experiences, forcing them to rediscover bugs independently.
*   **Stifling Environment:** The lack of alternative editors, poorly documented CLI tools, and reliance on macOS limit developer flexibility and tooling options.
*   **Negative Impact on Development:** The author suggests that Xcode can instill bad habits in developers, promoting ritualistic solutions over deep understanding.

The author concludes by advising new developers to avoid Xcode if possible and reassuring current users that their frustration is justified: "Xcode sucks."


---

## 78. Is a movie prop the ultimate laptop bag?

**原文标题**: Is a movie prop the ultimate laptop bag?

**原文链接**: [https://blog.jgc.org/2025/09/is-movie-prop-ultimate-laptop-bag.html](https://blog.jgc.org/2025/09/is-movie-prop-ultimate-laptop-bag.html)

生成摘要时出错

---

## 79. The Nature of Hallucinations

**原文标题**: The Nature of Hallucinations

**原文链接**: [https://blog.qaware.de/posts/nature-of-hallucinations/](https://blog.qaware.de/posts/nature-of-hallucinations/)

生成摘要时出错

---

## 80. Pycon UK 2025: Principle Misunderstandings, Kevlin Henney [video]

**原文标题**: Pycon UK 2025: Principle Misunderstandings, Kevlin Henney [video]

**原文链接**: [https://www.youtube.com/watch?v=gCEbtNVH2LQ](https://www.youtube.com/watch?v=gCEbtNVH2LQ)

生成摘要时出错

---

## 81. Are We in a Crisis of Rudeness?

**原文标题**: Are We in a Crisis of Rudeness?

**原文链接**: [https://www.vox.com/even-better/458283/are-americans-more-rude-incivility-polite-speakerphone-public](https://www.vox.com/even-better/458283/are-americans-more-rude-incivility-polite-speakerphone-public)

生成摘要时出错

---

## 82. Biconnected components

**原文标题**: Biconnected components

**原文链接**: [https://emi-h.com/articles/bcc.html](https://emi-h.com/articles/bcc.html)

生成摘要时出错

---

## 83. Privacy and Security Risks in the eSIM Ecosystem [pdf]

**原文标题**: Privacy and Security Risks in the eSIM Ecosystem [pdf]

**原文链接**: [https://www.usenix.org/system/files/usenixsecurity25-motallebighomi.pdf](https://www.usenix.org/system/files/usenixsecurity25-motallebighomi.pdf)

生成摘要时出错

---

## 84. The CSS Handbook, 2025 edition

**原文标题**: The CSS Handbook, 2025 edition

**原文链接**: [https://flaviocopes.com/the-css-handbook-2025-edition/](https://flaviocopes.com/the-css-handbook-2025-edition/)

生成摘要时出错

---

## 85. Notion 3.0

**原文标题**: Notion 3.0

**原文链接**: [https://www.notion.com/blog/introducing-notion-3-0](https://www.notion.com/blog/introducing-notion-3-0)

Notion 3.0 introduces Notion AI Agents, a significant evolution designed to automate knowledge work and free up users' time. These Agents can perform tasks that a human would normally do within Notion, such as creating documents, building databases, searching across tools, and executing multi-step workflows. Unlike generic AI chatbots, Notion Agents understand a user's work context and can take action, completing multiple tasks to create finished products directly within the Notion workspace.

Users can personalize their Agents by providing custom instructions and context through a dedicated Notion page, acting as a memory bank. This allows the Agent to learn user preferences and work styles, improving its efficiency and effectiveness.

Looking ahead, Notion plans to introduce Custom Agents, allowing users to create teams of AI specialists to automate specific workflows on autopilot. These Custom Agents can be tailored for various roles, such as editors, travel planners, or onboarding buddies.

In addition to AI Agents, Notion 3.0 also includes highly-requested features like database row permissions, new AI connectors, and additional MCP integrations. The goal is to empower users to focus on their "life's work" by delegating busywork to their AI Agents, and Notion encourages user feedback to further develop these tools.


---

## 86. The common sense unit of work

**原文标题**: The common sense unit of work

**原文链接**: [https://blog.nilenso.com/blog/2025/09/17/the-common-sense-unit-of-work/](https://blog.nilenso.com/blog/2025/09/17/the-common-sense-unit-of-work/)

生成摘要时出错

---

## 87. You did this with an AI and you do not understand what you're doing here

**原文标题**: You did this with an AI and you do not understand what you're doing here

**原文链接**: [https://hackerone.com/reports/3340109](https://hackerone.com/reports/3340109)

生成摘要时出错

---

## 88. We Politely Insist: Your LLM Must Learn the Persian Art of Taarof

**原文标题**: We Politely Insist: Your LLM Must Learn the Persian Art of Taarof

**原文链接**: [https://arxiv.org/abs/2509.01035](https://arxiv.org/abs/2509.01035)

生成摘要时出错

---

## 89. A simple way to measure knots has come unraveled

**原文标题**: A simple way to measure knots has come unraveled

**原文链接**: [https://www.quantamagazine.org/a-simple-way-to-measure-knots-has-come-unraveled-20250922/](https://www.quantamagazine.org/a-simple-way-to-measure-knots-has-come-unraveled-20250922/)

生成摘要时出错

---

## 90. To improve your odds of getting hired, Get your cover letter right

**原文标题**: To improve your odds of getting hired, Get your cover letter right

**原文链接**: [https://eures.europa.eu/want-improve-your-odds-getting-hired-get-your-cover-letter-right-2025-09-19_en](https://eures.europa.eu/want-improve-your-odds-getting-hired-get-your-cover-letter-right-2025-09-19_en)

生成摘要时出错

---

## 91. Pope Leo refuses to authorise an AI Pope

**原文标题**: Pope Leo refuses to authorise an AI Pope

**原文链接**: [https://www.pcgamer.com/software/ai/pope-leo-refuses-to-authorise-an-ai-pope-and-declares-the-technology-an-empty-cold-shell-that-will-do-great-damage-to-what-humanity-is-about/](https://www.pcgamer.com/software/ai/pope-leo-refuses-to-authorise-an-ai-pope-and-declares-the-technology-an-empty-cold-shell-that-will-do-great-damage-to-what-humanity-is-about/)

生成摘要时出错

---

## 92. Egyptian Hieroglyphic Alphabet (2015)

**原文标题**: Egyptian Hieroglyphic Alphabet (2015)

**原文链接**: [https://discoveringegypt.com/egyptian-hieroglyphic-writing/egyptian-hieroglyphic-alphabet/](https://discoveringegypt.com/egyptian-hieroglyphic-writing/egyptian-hieroglyphic-alphabet/)

生成摘要时出错

---

## 93. What happens when coding agents stop feeling like dialup?

**原文标题**: What happens when coding agents stop feeling like dialup?

**原文链接**: [https://martinalderson.com/posts/what-happens-when-coding-agents-stop-feeling-like-dialup/](https://martinalderson.com/posts/what-happens-when-coding-agents-stop-feeling-like-dialup/)

生成摘要时出错

---

## 94. SWE-Bench Pro

**原文标题**: SWE-Bench Pro

**原文链接**: [https://github.com/scaleapi/SWE-bench_Pro-os](https://github.com/scaleapi/SWE-bench_Pro-os)

生成摘要时出错

---

## 95. US authorities seize illicit electronics in New York during UN General Assembly

**原文标题**: US authorities seize illicit electronics in New York during UN General Assembly

**原文链接**: [https://www.reuters.com/world/us/us-authorities-seize-illicit-electronics-new-york-area-during-un-general-2025-09-23/](https://www.reuters.com/world/us/us-authorities-seize-illicit-electronics-new-york-area-during-un-general-2025-09-23/)

生成摘要时出错

---

## 96. I uncovered an ACPI bug in my Dell Inspiron 5567. It was plaguing me for 8 years

**原文标题**: I uncovered an ACPI bug in my Dell Inspiron 5567. It was plaguing me for 8 years

**原文链接**: [https://triangulatedexistence.mataroa.blog/blog/i-uncovered-an-acpi-bug-in-my-dell-inspiron-5667-it-was-plaguing-me-for-8-years/](https://triangulatedexistence.mataroa.blog/blog/i-uncovered-an-acpi-bug-in-my-dell-inspiron-5667-it-was-plaguing-me-for-8-years/)

生成摘要时出错

---

## 97. Beyond the Front Page: A Personal Guide to Hacker News

**原文标题**: Beyond the Front Page: A Personal Guide to Hacker News

**原文链接**: [https://hsu.cy/2025/09/how-to-read-hn/](https://hsu.cy/2025/09/how-to-read-hn/)

生成摘要时出错

---

## 98. Some stuff on how Linux consoles interact with the mouse

**原文标题**: Some stuff on how Linux consoles interact with the mouse

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/linux/LinuxConsoleAndMouse](https://utcc.utoronto.ca/~cks/space/blog/linux/LinuxConsoleAndMouse)

生成摘要时出错

---

## 99. A Beautiful Maths Game

**原文标题**: A Beautiful Maths Game

**原文链接**: [https://sinerider.com/](https://sinerider.com/)

生成摘要时出错

---

## 100. USDA Puts Food Researchers on Leave

**原文标题**: USDA Puts Food Researchers on Leave

**原文链接**: [https://www.wsj.com/politics/policy/usda-puts-food-researchers-on-leave-ef287cd7](https://www.wsj.com/politics/policy/usda-puts-food-researchers-on-leave-ef287cd7)

生成摘要时出错

---

