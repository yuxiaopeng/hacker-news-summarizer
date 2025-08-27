# Hacker News 热门文章摘要 (2025-08-27)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Nx受损：恶意软件使用Claude代码CLI探索文件系统

**原文标题**: Nx compromised: malware uses Claude code CLI to explore the filesystem

**原文链接**: [https://semgrep.dev/blog/2025/security-alert-nx-compromised-to-steal-wallets-and-credentials/](https://semgrep.dev/blog/2025/security-alert-nx-compromised-to-steal-wallets-and-credentials/)

Nx构建系统的一个受损版本已导致至少1400个GitHub账户感染恶意软件。该恶意软件通过受损的Nx版本（21.5.0 - v21.8.0和v20.6.0 – v20.12.0）中的恶意安装后脚本传播，窃取钱包和API密钥，并将它们推送到一个以“s1ngularity-repository”为前缀的新创建的公共GitHub仓库。

该恶意软件利用Claude Code CLI（或如果可用则利用Gemini CLI）浏览文件系统以查找敏感数据，使用旨在定位钱包相关文件和密钥的提示。 这种方法很新颖，因为它将潜在的可疑代码执行转移到LLM，从而使检测更加困难。 窃取的信息随后会被base64编码并存储在仓库中。

建议用户检查其GitHub组织是否存在“s1ngularity-repository”，将Nx更新到安全版本（21.4.1或更高版本），并轮换所有可能暴露的密钥，包括API密钥、SSH密钥以及GitHub和npm的凭据。 他们还应检查shell文件（例如，.bashrc）是否存在可疑的关闭指令。 受影响的Nx版本已从npm中删除。 Semgrep规则可用于帮助识别是否使用了易受攻击的版本。 该事件仍在进行中，用户应继续警惕未经授权的仓库创建。

---

## 2. 单色绘图

**原文标题**: Monodraw

**原文链接**: [https://monodraw.helftone.com/](https://monodraw.helftone.com/)

Monodraw是一款macOS应用程序，旨在创建ASCII艺术、图表和基于文本的视觉效果。它允许用户轻松创建和嵌入基于文本的艺术作品，用于图表、思维导图、ER图和横幅。它兼容macOS 11 Big Sur或更高版本。

Monodraw提供以下功能：

* 用于精确布局控制的自定义文本引擎。
* 带有连接点的直线和矩形工具，用于动态连接。
* 内置FIGlet，用于生成带有148种字体的横幅。
* 基本绘图工具，包括铅笔、橡皮擦、油漆桶和取色器。
* 用于组织的分组、辅助线和焦点工具。
* 用于提高效率的快捷方式。
* 用于自动化文档的命令行界面（CLI）（仅限Direct版本）。

Monodraw强调纯文本的功能和简洁性，并支持导出为PNG和SVG格式。它专为macOS设计，并提供原生功能。

用户可以购买9.99美元的许可证，或咨询教育定价。开发者鼓励通过电子邮件或Twitter（@Monodraw）提供反馈，并提供媒体资料包。他们强调严格的隐私政策，声明Monodraw不收集任何数据。

---

## 3. Typepad即将关闭。

**原文标题**: Typepad Is Shutting Down

**原文链接**: [https://everything.typepad.com/blog/2025/08/typepad-is-shutting-down.html](https://everything.typepad.com/blog/2025/08/typepad-is-shutting-down.html)

无法访问文章链接。

---

## 4. VIM大师

**原文标题**: VIMMaster

**原文链接**: [https://github.com/renzorlive/vimmaster](https://github.com/renzorlive/vimmaster)

VIMMaster 是一款轻量级的浏览器内游戏，旨在通过简短而专注的关卡教授核心 Vim 移动和编辑命令。它无需安装；用户只需在浏览器中打开 `index.html` 文件即可，最好在桌面上运行以获得完整的键盘支持。

该游戏具有 Normal 和 Insert 模式、命令日志以及验证操作结果而非仅仅验证击键的关卡。它支持一系列 Vim 命令，包括基本移动 (`h j k l`)、单词移动 (`w b e`)、行跳转 (`gg G`)、插入模式 (`i, a, o/O`)、删除操作 (`dd, dw, x`)、复制和粘贴 (`yy, p`)、行边界 (`0, $`) 以及更改/替换命令 (`cw, D, r`)。它还支持命令的数字计数（例如，`3w`，`2dd`）。

该游戏根据命令的最终结果验证进度，从而在击键序列方面提供灵活性。关卡涵盖了诸如退出 Vim、基本移动、单词/行操作、插入模式、删除、复制/粘贴等主题。控件映射到标准的 Vim 命令。

要在本地运行 VIMMaster，请克隆存储库并在浏览器中打开 `index.html`。 如果需要，可以使用像 `npx serve .` 这样的静态服务器。

该项目使用纯 HTML/CSS/JS 与 Tailwind CDN 进行样式设计，避免了依赖项和框架。 欢迎通过 issue 和 PR 贡献，重点在于可读代码、小型关卡和清晰的说明。 该项目采用 MIT 许可证。

---

## 5. C语言和内核开发中的面向对象设计模式

**原文标题**: Object-oriented design patterns in C and kernel development

**原文链接**: [https://oshub.org/projects/retros-32/posts/object-oriented-design-patterns-in-osdev](https://oshub.org/projects/retros-32/posts/object-oriented-design-patterns-in-osdev)

本文探讨了在基于C的内核开发中使用面向对象设计模式，特别是虚函数表（vtables）的方法。作者joexbayer详细介绍了如何在自己的操作系统中利用这些模式来实现模块化、可扩展性和运行时灵活性。

其核心概念是使用包含函数指针的结构体（虚函数表）来定义设备和服务等对象的接口。不同类型的设备可以使用相同的API（例如，`start`，`stop`），同时基于其特定的虚函数表实现执行不同的函数。这允许运行时交换行为。

作者重点介绍了其操作系统中的两个具体用例：服务管理（启动、停止、重启）和调度器实现，其中不同的调度策略可以在运行时交换。他们还将其与Linux的文件抽象进行了类比，其中单个接口（`read`，`write`）处理各种底层实现。虚函数表还允许通过内核模块进行动态内核扩展。

虽然承认诸如冗长的语法（显式对象传递）之类的缺点，但作者认为，这种显式性通过使依赖关系更加透明来提高代码清晰度。最终，虚函数表提供了一种在内核代码中实现灵活性和可维护性的实用方法，而无需完整的面向对象语言的复杂性。作者强调了这种方法在操作系统开发中进行实验和学习的价值。

---

## 6. Lago – 开源用量计费 – 招聘销售、工程、运营 (欧盟、美国)

**原文标题**: Lago – Open-Source Usage Based Billing – Is Hiring in Sales, Eng, Ops (EU, US)

**原文链接**: [https://www.ycombinator.com/companies/lago/jobs](https://www.ycombinator.com/companies/lago/jobs)

Lago，一款开源的基于使用量的计费平台，正在积极招聘销售、工程和运营等多个职位，工作地点遍布美国和欧洲。该公司旨在通过提供灵活透明的平台来简化 SaaS 公司的计费流程。

他们正在寻找技术客户经理（美国和法国）、销售开发代表（美国/加拿大和欧洲）、运营主管、支持工程师、基础设施工程师、AI/ML工程师、前沿部署工程师、高级前端工程师和增长营销经理等职位的候选人。 每个职位都提供薪资范围。

Lago 强调其雄厚的资金（超过 2200 万美元）、活跃的开源社区（超过 7,000 个 GitHub Star），以及被 Mistral.ai、Together.ai、Groq 和 Laravel 等公司采用。

该公司重视有雄心壮志、专注、可靠、积极主动并渴望学习和成长的人。他们鼓励在支持性的团队环境中进行实验并从错误中学习。

Lago 成立于 2021 年，总部位于法国巴黎，由 Anh-Tho CHUONG 和 Raffi SARKISSIAN 领导，目前拥有 23 名员工。

---

## 7. 用Go和C实现Forth

**原文标题**: Implementing Forth in Go and C

**原文链接**: [https://eli.thegreenplace.net/2025/implementing-forth-in-go-and-c/](https://eli.thegreenplace.net/2025/implementing-forth-in-go-and-c/)

本文详细介绍了作者在长期对 Forth 语言的好奇心驱使下，用 Go（“goforth”）和 C（“ctil”）实现 Forth 语言的旅程。作者区分了 Forth 的两个“层次”：用户层（使用 Forth 完成实际任务）和黑客层（探索 Forth 的实现和可扩展性）。

用 Go 实现的“Goforth”是一个纯粹的解释器，适合用户层任务，但由于宿主语言的控制，在支持自定义控制流等高级功能方面受到限制。用 C 实现的“Ctil”灵感来源于 Jonesforth（一个汇编实现），旨在达到黑客层，从而能够用 Forth 本身实现核心 Forth 结构（如 `IF...THEN` 和 `variable`）。这是通过使用链式字典和直接内存操作来实现的。

作者反思了 Forth 的历史意义，强调了它对早期硬件交互和 DSL 创建的适用性。虽然欣赏它独特的方面，如连接式、无点编程，但作者最终认为 Forth 是一种“奇怪的语言”，不适用于现代用途。固有的基于堆栈的编程模型被认为是简洁但难以阅读和理解，并以 `+!` 单词为例。

文章最后提供了作者在 GitHub 上的 Go Forth 实现链接，以及学习 Forth 及其实现的有用资源。作者强调了从头开始实现一种编程语言所带来的教育价值和满足感。

---

## 8. ASCII流程图

**原文标题**: ASCIIFlow

**原文链接**: [https://asciiflow.com/](https://asciiflow.com/)

文章标题为“ASCIIFlow”，内容可能与名为ASCIIFlow的工具或概念有关。

---

## 9. Therac-25 事故 (2021)

**原文标题**: The Therac-25 Incident (2021)

**原文链接**: [https://thedailywtf.com/articles/the-therac-25-incident](https://thedailywtf.com/articles/the-therac-25-incident)

这篇文章，题为“Therac-25 事件 (2021)”，很可能着重讲述 20 世纪 80 年代中期臭名昭著的 Therac-25 放射治疗机事故。根据所列的内容类别（“专题文章”、“代码错误”、“出错”、“论坛”、“其他文章”、“随机文章”），可以推断这篇文章对该事件进行了全面审视，涵盖了各个方面。

“代码错误”和“出错”类别强烈暗示这篇文章深入探讨了导致过量照射的软件和硬件缺陷。“论坛”部分暗示社区对该事件进行了讨论或分析，可能侧重于汲取的教训。“专题文章”和“其他文章”表明汇编了与该事件相关的报告、分析和观点。

因此，这篇文章很可能探讨了 Therac-25 的软件缺陷，包括竞争条件和不足的安全检查，这些缺陷使得操作员能够施用致命剂量的辐射。文章也可能讨论导致事故的硬件故障。此外，文章很可能考察 Therac-25 事件的更广泛影响，例如在安全关键系统中，严格的软件测试、人因工程以及工程师、操作员和监管机构之间清晰沟通的重要性。文章也很可能讨论伦理考量以及受影响的患者和公司的后续情况。

---

## 10. 我们通过系统性举措重建了云生活的基础设施交付

**原文标题**: We Rebuilt Cloud Life's Infrastructure Delivery with System Initiative

**原文链接**: [https://www.cloudlife.io/resources/infrastructure-delivery-with-system-initiative](https://www.cloudlife.io/resources/infrastructure-delivery-with-system-initiative)

Cloud Life 使用系统倡议 (SI) 重建了其基础设施交付流程，摆脱了传统的基于 Terraform 的工作流程，包括静态配置文件、PR 审查和 CI 管道。 之前的系统存在反馈周期慢的问题，即使是小的更改也需要大量时间投入到 “IaC 炼狱” 中。

确定的主要痛点是验证变更的延迟、配置任务的重复性以及调试和管理多个环境的困难。

Cloud Life 决定采用 SI 是基于对即时反馈、实时协作、完整生命周期可见性、可重用构建块以及与 AWS 无缝集成的需求。

概念验证包括在 SI 中重建一个复杂的客户端环境，工程师可以在其中以可视方式对基础设施组件进行建模、应用安全默认设置并在几秒钟内查看更改。 然后，该方法扩展到 ECS 集群、API Gateway 端点、EventBridge 路由和 ElastiCache 实例，所有这些都作为 SI 中的可重用资产。

主要优势包括大幅缩短了配置时间（从数小时缩短到数分钟）、提高了调试速度、增加了通用基础设施模式的重用以及提高了团队士气。 值得注意的是，由于 SI 环境的可视化和协作特性，新工程师的入职时间显着减少。

这次转型是从“基础设施即代码”到“基础设施即协作”的思维转变，从而产生了一种更顺畅、更快、更协作的方式来构建基础设施。

---

## 11. 放慢程序速度出奇地有用

**原文标题**: Slowing down programs is surprisingly useful

**原文链接**: [https://stefan-marr.de/2025/08/how-to-slow-down-a-program/](https://stefan-marr.de/2025/08/how-to-slow-down-a-program/)

本文探讨了程序减速令人惊讶的实用性。尽管大量研究集中于优化，但受控的减速可以帮助检测竞争条件、加速模拟和评估分析器的准确性。通过选择性地减缓程序的部分，诸如模糊测试输入等技术可以应用于指令交错，从而揭示并发错误。Coz分析器使用减速来模拟优化，使开发人员能够在投入大量精力之前评估潜在的好处。

然而，当前的减速方法通常是粗粒度的。作者的研究重点是通过将特定的x86指令（NOP或MOV regX, regX）插入到基本块中来实现细粒度的减速。在Intel Core i5-10600 (Comet Lake-S)上的实验表明，NOP和MOV指令有效地使程序执行时间加倍，同时保持分析器可观察的性能行为，这意味着方法运行时比例保持一致。其他测试的指令未提供这种可靠的减速效果。

该研究评估了六种x86指令候选指令，以评估它们实现100%受控开销、保持分析器可观察的性能行为以及基本块内减速位置是否影响结果的能力。论文《评估编译器级别可靠程序减速的候选指令：面向支持高级开发工具的细粒度减速》提供了对这些实验的详细分析。这项工作旨在通过细粒度的减速技术，为更精确的竞争检测、加速估计和分析器评估铺平道路。

---

## 12. 为何“汽车般大小的岩石”正在多洛米蒂山脉滚落

**原文标题**: Why 'rocks as big as cars' are flying down the Dolomites

**原文链接**: [https://www.bbc.com/future/article/20250819-why-italys-beloved-ancient-monolith-is-falling](https://www.bbc.com/future/article/20250819-why-italys-beloved-ancient-monolith-is-falling)

意大利多洛米蒂山，一处联合国教科文组织自然遗产地，正经历着日益增多的落石和滑坡，引发了对其稳定性的担忧。虽然侵蚀是自然现象，但专家和当地居民认为这一过程正在加速，部分原因是气候变化。

地质因素也加剧了这个问题。多洛米蒂山由“白云石”构成，其底部是柔软的黏土层，导致倾斜和裂缝的产生。气候变化通过增加强降雨和冻融循环，进一步加剧了这种情况，导致岩石破裂。Galgaro教授将此比作散热器，裂缝使得加热和冷却的速度更快，从而削弱了结构。虽然一些山峰拥有永久冻土，并且正在融化，但该地区的许多山脉较矮，一开始就没有永久冻土。

像Crosta这样的专家强调了滑坡的不可预测性，使得现有的模型不太可靠。解决方案有限，因为“束缚”自然被认为是无效的。相反，工作重点在于监测振动并警示民众。一个地图数据库记录了滑坡事件，以提高人们的意识。

虽然有人建议采取一些措施，比如更早地开放缆车以避开危险时段，但总体情绪是适应风险，类似于接受勃朗峰上的“死亡之路”。尽管一些山峰消失，但一些侵蚀现象也揭示了新的奇观。多洛米蒂山是一个自然遗址，接受其演变至关重要，同时也应承认有些变化是人为影响造成的。

---

## 13. 使用信息论解决猜密码游戏

**原文标题**: Using information theory to solve Mastermind

**原文链接**: [https://www.goranssongaspar.com/mastermind](https://www.goranssongaspar.com/mastermind)

本文讲述了如何应用信息论来解决猜颜色游戏“Mastermind”。Mastermind游戏包括猜测一个由四个颜色棋子组成的秘密代码，每个棋子从六种可能的颜色中选择。每次猜测后，出码者会提供黑白棋子作为反馈。黑棋子表示颜色和位置都正确的棋子，而白棋子表示颜色正确但位置不正确的棋子。没有棋子表示猜测的颜色都不在秘密代码中。目标是以尽可能少的尝试次数正确猜出秘密代码。本文暗示，通过利用信息论，可以制定策略来优化猜测，并最大限度地减少破解代码所需的尝试次数。文章暗示可以利用出码者的反馈来获取信息，并以战略性的、信息驱动的方式改进后续猜测。

---

## 14. 高效数组编程

**原文标题**: Efficient Array Programming

**原文链接**: [https://github.com/razetime/efficient-array-programming](https://github.com/razetime/efficient-array-programming)

本文档介绍了一个专注于高效数组编程的资源。它以类似维基百科的知识库形式呈现，旨在收集类似APL和k等数组语言中编写良好的代码的信息和示例。作者鼓励读者在仅依赖所提供的解释之前检查代码，强调培养对数组编程的更深入理解的目标。

该资源涵盖了数组编程的通用技巧，以及针对Dyalog APL、dzaima/APL和ngn/k的特定于实现的建议。它包括指向有价值的外部资源的链接和参考，例如Jay Foad的Advent of Code解决方案、ngn/k代码示例、Andriy Makukha的APL Contest 2020解决方案、Bubbler-4的Advent of APL、APL Orchard聊天室日志以及Aaron Hsu关于高性能树的工作。总体目标是帮助程序员提高他们的数组语言技能，并提供有用的示例代码集合。

---

## 15. 互联网接入服务商不受DMCA揭露身份传票约束——考克斯案

**原文标题**: Internet Access Providers Aren't Bound by DMCA Unmasking Subpoenas–In Re Cox

**原文链接**: [https://blog.ericgoldman.org/archives/2025/08/internet-access-providers-arent-bound-by-dmca-unmasking-subpoenas-in-re-cox.htm](https://blog.ericgoldman.org/archives/2025/08/internet-access-providers-arent-bound-by-dmca-unmasking-subpoenas-in-re-cox.htm)

本文分析了第九巡回法院在 *In re Subpoena of Internet Subscribers of Cox Communications, LLC* 案中的判决，该判决重申，DMCA 第 512(h) 条传票程序不得用于迫使互联网接入服务提供商 (IAPs) 披露涉嫌侵犯版权的用户身份。法院重申了既定的法律先例，即根据 512(a) 安全港运营的 IAPs 不“托管”侵权内容，因此无法遵守触发 512(h) 条传票所需的删除通知要求 (512(c)(3))。

DMCA 的通知和删除系统主要针对网络主机，但版权所有者一直在不正当地利用 512(h) 条传票来针对 IAPs，以识别 BitTorrent 用户，从而迫使他们充当版权执法者。法院驳回了 IAPs 可以通过端口封锁来“禁用访问”的论点，并指出 DMCA 意图将“禁用访问”理解为停止托管侵权材料，而这正是 IAPs 所不做的。

作者批评版权所有者无视现有法律先例，继续滥用 512(h) 条款，并认为法院书记员在签发这些传票时，被迫做出超出其权限的法律判断。作者还指出，IAPs 可能因基于非法 512(h) 条款传票不正当地披露用户身份而面临诉讼。文章最后指出，虽然该裁决加强了现有法律，但版权所有者将继续寻求各种方法来向 IAPs 施压，以打击版权侵权行为，包括推动网站屏蔽令。

---

## 16. Kiwi.com 航班搜索 MCP 服务器

**原文标题**: Kiwi.com flight search MCP server

**原文链接**: [https://mcp-install-instructions.alpic.cloud/servers/kiwi-com-flight-search](https://mcp-install-instructions.alpic.cloud/servers/kiwi-com-flight-search)

本文档描述了“Kiwi.com航班搜索MCP服务器”，并特别关注生成MCP安装指南。因此，本文档的主要功能是促进创建用于安装和配置Kiwi.com航班搜索MCP服务器的指南。

在没有更多上下文的情况下，“MCP”可能指的是Kiwi.com航班搜索基础设施中的一个组件或模块。该文档可能包含细节，或者作为一个工具，来自动化或简化生成设置此MCP服务器所需步骤的过程。

从更多上下文中可以预期的关键信息（假设这是摘要请求中提供的全部信息）：

*   **什么是MCP服务器？** 对其在Kiwi.com航班搜索中的作用的描述。
*   **什么是MCP安装指南？** 安装所需的步骤和配置。
*   **生成器如何工作？** 它是脚本、手动过程还是GUI工具等？
*   **目标受众：** 谁会使用这些指南？
*   **先决条件：** 假设安装之前已经到位的是什么？
*   **潜在好处：** 为什么这个工具有用？

简而言之，本文档是关于为“Kiwi.com航班搜索MCP服务器”生成安装指南，重点是指南生成方法本身。

---

## 17. 我们在下水道里发现的东西

**原文标题**: What We Find in the Sewers

**原文链接**: [https://www.asimov.press/p/sewers](https://www.asimov.press/p/sewers)

卡勒姆·德里斯代尔的文章《我们在下水道里发现了什么》探讨了人类废物管理的历史，着重介绍了它从一种麻烦到一种宝贵资源的演变。最初，古代农民使用人类和动物粪便作为肥料，对其进行堆肥以保留养分。随着人口的增长，废物处理成为一个问题，导致了早期的城市法规和排水系统，如在印度河流域文明和罗马所见。罗马人建造了精密的渡槽和下水道，如克洛阿卡·马克西玛，尽管与卫生相关的疾病仍然很普遍。

在近代早期欧洲，人类粪便对于硝石生产至关重要，硝石是火药的关键成分，这导致了硝石工人的兴起，他们开采有机物以获取硝酸盐。然而，像伦敦这样的城市的发展以及19世纪抽水马桶的普及，使现有系统不堪重负，污染了泰晤士河，并导致了霍乱等水传播疾病的爆发。这场危机促使了卫生改革和医学统计的发展，以改善公共卫生。文章强调，污水曾经被简单地视为废物，但现在越来越被认为是含有有价值元素、数据甚至能源的资源，为基于污水的流行病学和资源回收提供了潜力。

---

## 18. Claude Chrome 浏览器插件

**原文标题**: Claude for Chrome

**原文链接**: [https://www.anthropic.com/news/claude-for-chrome](https://www.anthropic.com/news/claude-for-chrome)

Anthropic 正在试用“Claude for Chrome”，这是一款 Chrome 扩展程序，允许 Claude AI 助手直接与用户的浏览器互动。这代表着迈向浏览器 AI 的重要一步，使 Claude 能够执行管理日历、起草电子邮件和填写表格等任务。

然而，Anthropic 认识到固有的安全风险，特别是提示注入攻击，即恶意行为者诱骗 AI 进行有害行为。早期测试显示，在采取缓解措施之前，攻击成功率为 23.6%。

为了应对这些风险，Anthropic 正在实施以下几种防御措施：

*   **权限：** 用户控制 Claude 可以访问哪些网站，并要求确认高风险操作。
*   **系统提示：** 增强的指令引导 Claude 处理敏感数据和操作。
*   **网站阻止：** 阻止访问高风险网站类别。
*   **高级分类器：** 检测可疑的指令模式和数据访问请求。

这些缓解措施降低了攻击成功率，但 Anthropic 的目标是将其大幅降低至接近于零。一项针对 1,000 名 Max 计划用户的试点计划将提供真实世界的反馈，以完善安全措施并应对新的攻击途径。建议测试人员从信任的网站开始，避免敏感信息，并提供反馈。Anthropic 认为，此次研究预览对于开发安全可靠的浏览器 AI 至关重要，并计划与该领域的其他人员分享他们的发现。

---

## 19. QEMU 10.1.0

**原文标题**: QEMU 10.1.0

**原文链接**: [https://wiki.qemu.org/ChangeLog/10.1](https://wiki.qemu.org/ChangeLog/10.1)

QEMU 10.1.0 引入了针对多种架构和功能的若干增强和变更。

**通用亮点：** 已移除弃用的旧特性和选项；用户应查阅文档以获取替代方案。最低支持的 Rust 版本现为 1.77。已停止支持 Debian Bullseye，且现在需要 Ninja 1.9。

**架构特定更新：**
*   **Arm：** 模拟新的 CPU 架构特性（FEAT_SME2 等），弃用 'highbank' 和 'midway'，添加 'max78000fthr' 板，在 'virt' 板上启用 CXL 和嵌套虚拟化，并引入了多个新机器。
*   **LoongArch：** 添加内核 irqchip 支持并修复了多个错误。
*   **RISC-V：** 添加原子指令获取，扩展 PMP 区域计数，改进 Microchip Polarfire SoC 定制，并实施了各种错误修复。
*   **x86：** 支持 TDX（需要 Linux 6.16+）和用于 TDX/SEV-SNP VM 的 IGVM 文件启动。

**设备模拟和分配：** 在具有特定设置的 ARM 'virt' 上支持 ACPI PCI 热插拔。VFIO 接收 CoCo guest-memfd 支持、更新的 IGD 直通特性、客户端设备支持、实时更新 (CPR) 和 TDX/SNP VM 支持。

**GUI：** Spice/dbus 支持多平面 dmabuf，GTK 改进了缩放，VNC 修复了字节序和显示问题。

**迁移：** RDMA 实时迁移支持 IPv6，具有后复制抢占优化和初始 multifd/后复制支持。

**块设备：** blockdev-mirror 和 blockdev-backup 具有用于优化镜像和错误处理的新选项。

**网络：** 通过 Unix 套接字的 NBD 使用更大的缓冲区进行了优化。

**其他值得注意之处：** 除了 TCG 指令模拟外，加密子系统现在依赖于 gcrypt、nettle 或 gnutls 来实现 AES。

---

## 20. 桌面Linux一直在打错误的战役

**原文标题**: Desktop Linux Keeps Winning the Wrong Battles

**原文链接**: [https://www.howtogeek.com/desktop-linux-keeps-winning-the-wrong-battles/](https://www.howtogeek.com/desktop-linux-keeps-winning-the-wrong-battles/)

本文认为，尽管Linux在多个领域表现出色，但由于专注于“错误的战场”，它未能实现主流桌面领域的统治地位。作者批评了长期以来对“Linux桌面元年”的信念，认为这更像是一种美好的愿望，而非现实的预测。

Linux在游戏支持和硬件兼容性方面取得了进展，发行版也越来越用户友好，但这些进步往往涉及模仿Windows和macOS，导致“得不偿失的胜利”。Linux社区花费大量精力在关于systemd、桌面环境（KDE vs. GNOME）和软件包格式（Snap vs. Flatpack）的内部辩论上，而这些与普通用户无关。

作者认为，真正的桌面普及取决于可用性、应用程序可用性、硬件合作伙伴关系以及统一的用户体验。Windows for Arm因应用程序不兼容而失败的例子与苹果成功的Rosetta 2形成对比。Linux缺乏统一的方向和领导，阻碍了其提供无缝用户体验的能力。Valve的Steam Deck证明，专注的方法与战略整合可以使Linux在更广泛的受众中可行。

文章最后总结说，为了Linux能够在桌面领域真正获胜，它需要与硬件和软件供应商合作，并需要连贯的领导，而不仅仅是技术进步。如果没有这些改变，Linux将仍然局限于服务器、嵌入式设备和利基游戏领域，无法说服用户放弃现有的操作系统。

---

## 21. 湾流崩溃临界点或在本世纪中叶到来

**原文标题**: Tipping point in Gulf Stream may be reached as early as mid-century

**原文链接**: [https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025JC022651](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2025JC022651)

无法访问文章链接。

---

## 22. Show HN: React Web Camera – 修复 &lt;input type=file&gt; 单张照片限制

**原文标题**: Show HN: React Web Camera – Fix <input type=file> single-photo limit

**原文链接**: [https://shivantra.com/react-web-camera/](https://shivantra.com/react-web-camera/)

“Show HN”帖子：React Web Camera - 突破网页应用单张照片限制

主要特性包括：

*   **多图拍摄：** 主要优势在于无需重复文件输入即可拍摄多张照片。
*   **无头组件：** 意味着该组件提供底层功能，但不决定UI。开发者可以完全控制样式和呈现。
*   **轻量级：** 表明性能影响极小。
*   **灵活：** 强调适应性和自定义选项。
*   **PWA友好：** 表示与渐进式Web应用程序开发兼容。
*   **桌面增强体验：** 暗示专门为桌面用户拍摄图像的用户体验改进。

本质上，React Web Camera 提供了一种开发者友好的方式，可以在 React 应用程序中构建自定义的多图像相机界面，与仅依赖浏览器默认文件输入相比，提供更大的控制权和更好的用户体验。

---

## 23. GitHub网站在Safari上速度慢

**原文标题**: The GitHub website is slow on Safari

**原文链接**: [https://github.com/orgs/community/discussions/170758](https://github.com/orgs/community/discussions/170758)

GitHub网站在Safari上速度极慢且无法使用的问题报告

---

## 24. F-35飞行员坠毁前与工程师举行50分钟空中电话会议

**原文标题**: F-35 pilot held 50-minute airborne conference call with engineers before crash

**原文链接**: [https://www.cnn.com/2025/08/27/us/alaska-f-35-crash-accident-report-hnk-ml](https://www.cnn.com/2025/08/27/us/alaska-f-35-crash-accident-report-hnk-ml)

一架F-35战斗机一月在阿拉斯加州艾尔森空军基地坠毁，原因是液压管路中的冰阻碍了起落架的正常展开。坠毁前，飞行员与洛克希德·马丁公司的工程师进行了50分钟的空中电话会议，试图解决问题。飞行员进行了两次“触地复飞”着陆，试图校正前起落架，但尝试失败，飞机的传感器随后错误地将飞机登记为在地面上，使其进入“自动地面操作模式”，导致飞机失控。飞行员安全弹射，仅受轻伤，但价值2亿美元的飞机被毁。

调查显示，大约三分之一的液压油是水，这本不应该存在。此后不久，在同一基地发现了另一架F-35类似的结冰问题，但该飞机安全着陆。此前，洛克希德·马丁公司的一份维护通讯警告了传感器在寒冷天气下的结冰问题以及可能出现的控制困难。报告指出，在电话会议期间参考这份通讯可能导致可控弹射，而不是触地复飞尝试。空军的调查将坠机归因于电话会议期间机组人员的决策、对危险材料（液压油）的监管不力以及未能遵循正确的液压维修程序。

---

## 25. 可塑软件

**原文标题**: Malleable Software

**原文链接**: [https://www.mdubakov.me/malleable-software-will-eat-the-saas-world/](https://www.mdubakov.me/malleable-software-will-eat-the-saas-world/)

本文认为，在人工智能时代，软件的未来在于可塑性，倾向于适应用户需求的工具，而不是迫使用户适应工具。像Linear这样设计精良但僵化的工具为人工智能增加价值提供的空间有限，而像Fibery这样复杂但灵活的工具则受益于人工智能简化设置和定制的能力。

大型语言模型推动的核心转变是将重点从*如何*实施解决方案转移到简单地定义*什么*问题需要解决。人工智能可以处理实现细节，充当“程序员”，根据通俗易懂的提示构建、审查和迭代解决方案。这降低了准入门槛并加速了原型设计。

历史上，可塑性软件因其复杂性和学习曲线而处于小众地位。然而，随着人工智能使定制变得更容易和更快，僵化的垂直解决方案的吸引力逐渐减弱。本文预测，未来用户将优先考虑适应性而不是即时速度，从而导致僵化工具的衰落，而支持可塑性平台。到2030-2035年，人工智能驱动的可塑性平台将提供对话式设置体验，从而最大限度地降低转换成本，并将僵化的SaaS工具降级为小众或遗留状态。虽然一些行业可能仍然重视标准化，但作者认为总体趋势将是适应用户需求的可调整软件。

---

## 26. 苹果撤销欧盟地区Alt Store上一款应用的发行权

**原文标题**: Apple Revokes EU Distribution Rights for an App on the Alt Store

**原文链接**: [https://torrentfreak.com/apple-revokes-eu-distribution-rights-for-torrent-client-developer-left-in-the-dark/](https://torrentfreak.com/apple-revokes-eu-distribution-rights-for-torrent-client-developer-left-in-the-dark/)

苹果已撤销iTorrent在欧盟的分发权，该应用是一款可在替代应用商店AltStore PAL上使用的BT客户端，此举实际上阻止了用户安装。这引发了人们对苹果公司是否遵守欧盟《数字市场法案》（DMA）的质疑，该法案要求允许第三方应用商店存在。

iTorrent与另一款BT客户端在AltStore PAL上的可用性是DMA带来的重要进展。在用户报告七月份的安装问题后，开发者XITRIX证实苹果已撤销他的“替代分发”权，这是在AltStore PAL等商店上发布应用程序的必要条件。

虽然苹果公司历来厌恶BT客户端可能暗示了某种动机，但该公司尚未对其行为提供明确的解释。XITRIX仅收到来自苹果支持的通用且无用的回复，这让他不确定撤销的原因。

AltStore PAL的联合创始人Shane Gill也证实与苹果公司进行了沟通并要求澄清，但表示他们没有收到实质性信息。他提到苹果公司从未提供关于特定应用类别的指南或警告。

苹果公司对此事保持公开沉默，引发了对其动机的猜测，并让人担心撤销缺乏透明度可能违反DMA的原则。这种情况凸显了苹果公司控制其生态系统的愿望与欧盟推动更开放和更具竞争力的数字市场之间的持续紧张关系。

---

## 27. WebLibre：注重隐私的浏览器

**原文标题**: WebLibre: The Privacy-Focused Browser

**原文链接**: [https://docs.weblibre.eu/](https://docs.weblibre.eu/)

WebLibre：一款注重隐私的新型网络浏览器，基于Mozilla Gecko引擎和安卓组件构建。它旨在提供功能齐全的浏览体验，支持Firefox移动插件，并优先考虑用户隐私和易用性。

该浏览器目前处于Alpha阶段，这意味着用户应预期频繁更新、潜在错误和重大变更。该项目鼓励用户在GitHub上报告遇到的任何问题。

需要注意的关键一点是，目前只有WebLibre的F-Droid构建版本不依赖于Google服务，这表明其他分发方式可能包含这些依赖项。

---

## 28. 状态空间探险[视频]

**原文标题**: Adventures in State Space [video]

**原文链接**: [https://www.youtube.com/watch?v=YGLNyHd2w10](https://www.youtube.com/watch?v=YGLNyHd2w10)

名为“状态空间探险 [视频]”的文本片段，看起来像是 **YouTube 上的元数据或样板文字**，而非视频本身的内容。 它列出了 YouTube 页面底部的各种链接和法律信息。这些包括：

*   **链接：** “关于我们”、“联系我们”、“创作者”、“广告”、“开发者”、“条款”、“隐私”、“政策与安全”、“YouTube 的运作方式”和“测试新功能”。
*   **版权信息：** 提及 YouTube 的所有者 Google LLC，并包含 2025 年的版权声明。
*   **特定节目提及：** 提及 “NFL Sunday Ticket”。

因此，**该文本 *没有* 提供关于“状态空间探险”视频实际内容的任何信息。** 它只是标准的 YouTube 页脚信息。 要总结该视频，需要视频本身或适当的描述。

---

## 29. 苹果M1 GPU拆解，完结

**原文标题**: Dissecting the Apple M1 GPU, the end

**原文链接**: [https://rosenzweig.io/blog/asahi-gpu-part-n.html](https://rosenzweig.io/blog/asahi-gpu-part-n.html)

本文记录了逆向工程苹果M1 GPU并为Asahi Linux开发开源图形驱动的历程，从而使Linux能够在M1和M2 Mac上以完整的图形加速运行。

作者最初旨在为Asahi Linux项目提供指导，最终深度参与其中，开发了一个着色器编译器和OpenGL驱动程序。该项目进展迅速，实现了绘制三角形、在macOS上运行3D游戏，并最终在Asahi Linux中实现了图形加速。

在充分利用M1能力的愿望驱动下，作者设定了雄心勃勃的目标：创建符合标准的OpenGL和Vulkan驱动程序，并启用Proton游戏。这包括开发几何/细分着色器仿真，这是对Mesa项目的一项重大贡献。

该项目取得了显著的成功，实现了OpenGL 4.6、OpenGL ES 3.2、OpenCL 3.0和Vulkan 1.4的合规性。最终实现了Proton游戏和Direct3D 12支持。作者的工作还为通过KosmicKrisp项目在macOS上实现符合标准的Vulkan铺平了道路。

在克服了最初的挑战并实现了目标后，作者现在正离开Apple生态系统，将该项目交由Asahi Linux社区中的其他人来追求新的挑战。

---

## 30. Show HN: FilterQL – 用于过滤结构化数据的微型查询语言

**原文标题**: Show HN: FilterQL – A tiny query language for filtering structured data

**原文链接**: [https://github.com/adamhl8/filterql](https://github.com/adamhl8/filterql)

FilterQL 是一个用于过滤结构化数据的微型查询语言和 TypeScript 库。它允许用户为其数据定义模式，然后使用自定义查询语言来过滤、排序和限制结果。

**主要特性：**

*   **查询语言：** 支持比较运算符（等于、不等于、包含等）、逻辑运算符（AND、OR、NOT）和字段别名。允许不区分大小写的比较和空值检查。提供“匹配所有”选项 (`*`)。
*   **操作：** 启用数据过滤后的转换，具有内置操作，如 `SORT` 和 `LIMIT`。用户还可以定义自定义操作。
*   **模式定义：** 模式定义了查询中允许的字段、其类型（字符串、数字、布尔值）以及可选的别名。
*   **TypeScript 库：** 包括安装说明和使用示例。
*   **自定义操作：** 用户可以通过创建自定义操作来扩展 FilterQL，这些操作可以访问数据、参数和辅助函数。
*   **语言规范：** 提供语法、定义比较和逻辑运算符，并概述语法规则。

**用法：**

该库接受一个数据数组、一个查询字符串和一个模式。该模式验证查询中的字段，并根据查询过滤数据。该库还支持在过滤后应用排序和限制等操作。查询语言旨在实现灵活性和可读性，允许使用括号和逻辑运算符进行复杂的过滤逻辑。

---

## 31. Word文档今后在Windows上将自动保存到云端。

**原文标题**: Word documents will be saved to the cloud automatically on Windows going forward

**原文链接**: [https://www.ghacks.net/2025/08/27/your-word-documents-will-be-saved-to-the-cloud-automatically-on-windows-going-forward/](https://www.ghacks.net/2025/08/27/your-word-documents-will-be-saved-to-the-cloud-automatically-on-windows-going-forward/)

今后，Windows系统上的Word文档将默认自动保存到微软的云存储（OneDrive）。此举旨在提升用户的数据安全性、可访问性和协作功能。

这一转变将消除用户手动保存文档的需求，从而降低因崩溃或断电导致的数据丢失风险。保存到云端的文档可以从任何连接互联网的设备访问，并且可以轻松地与他人共享和协作。

虽然自动云保存是新的默认设置，但用户仍然可以控制文档的保存位置。如果他们愿意，可以选择将默认保存位置改回本地存储。此功能的实施预计将是渐进式的，将在一段时间内逐步推广给用户。文章可能还会讨论潜在的隐私影响以及微软在此次更改中对数据安全性的保证。

---

## 32. SpaceX巨型星舰火星火箭成功完成关键第十次试飞

**原文标题**: SpaceX's giant Starship Mars rocket nails critical 10th test flight

**原文链接**: [https://www.space.com/space-exploration/private-spaceflight/spacex-launches-starship-flight-10-critical-test-flight-video](https://www.space.com/space-exploration/private-spaceflight/spacex-launches-starship-flight-10-critical-test-flight-video)

SpaceX星舰完成第十次试飞，取得重大进展

SpaceX公司有史以来建造的最大的火箭星舰于2025年8月26日成功完成第十次试飞，标志着在之前几次不成功的尝试后取得了重大进展。 此次飞行实现了几个关键里程碑，包括成功发射、级间分离以及超重型助推器在墨西哥湾的溅落。

星舰上级到达亚轨道轨迹并成功部署了八颗模拟星链卫星，这是之前未曾实现的壮举。 此外，星舰还在太空中重新点燃了一台猛禽发动机，这是另一项重要成就。

在重返地球大气层的过程中，星舰受到损坏，包括尾裙的一部分脱落。 然而，它坚持了下来并按计划进行了着陆燃烧，在印度洋目标浮标的视线范围内溅落。

本次试飞基于之前的失败进行了多项设计变更，包括对燃料箱增压系统和复合压力容器的修改。 第十次飞行的成功代表着星舰的研发向前迈出了关键一步，使SpaceX公司更接近其完全可重复使用、重型有效载荷部署以及最终的火星殖民的目标。 该公司计划分析本次飞行的数据，以继续改进飞行器的设计和性能。

---

## 33. “哇！”信号可能来自地外文明，且能量更强。

**原文标题**: The “Wow!” signal was likely from extraterrestrial source, and more powerful

**原文链接**: [https://www.iflscience.com/the-wow-signal-was-likely-from-an-extraterrestrial-source-and-more-powerful-than-we-thought-80561](https://www.iflscience.com/the-wow-signal-was-likely-from-an-extraterrestrial-source-and-more-powerful-than-we-thought-80561)

一项新研究重新审视了著名的“Wow！”信号——1977年探测到的神秘无线电信号，并表明它很可能起源于地外源，且比之前估计的更强大。研究人员利用现代技术和未公开的数据，分析了来自大耳朵射电望远镜的数十年旧数据。他们的发现强烈表明该信号并非由地面干扰或卫星引起。

分析显示，该信号比最初计算的要强得多，测量值为250 央斯基。此外，研究人员还发现了大约在同一时间探测到的两个类似的、尽管较弱的信号（“Wow2”和“Wow3”）。他们认为，这些信号，包括“Wow！”信号，可能起源于星际介质中的冷氢云，可能由类似磁星耀斑的超辐射事件触发。

虽然该研究并未明确证明“Wow！”信号是由地外文明发送的，但它通过排除其他潜在原因并提供其特征和起源的更清晰图景，增强了这种可能性。研究人员强调，这些发现虽然不是地外生命的结论性证据，但对完善未来对技术特征的搜索做出了重大贡献。他们计划继续分析档案数据和无法解释的信号，以进一步了解“Wow！”信号和其他潜在的地外通信。 这些研究目前以预印本形式提供，尚未经过同行评审。

---

## 34. 光污染延长鸟类活动时间

**原文标题**: Light pollution prolongs avian activity

**原文链接**: [https://gizmodo.com/birds-across-the-world-are-singing-all-day-for-a-disturbing-reason-2000646257](https://gizmodo.com/birds-across-the-world-are-singing-all-day-for-a-disturbing-reason-2000646257)

一项发表于《科学》杂志的新研究表明，光污染显著延长了鸟类的活动时间。研究人员布伦特·皮斯和尼尔·吉尔伯特分析了“鸟天气”项目收集的超过6000万条、来自580多种昼行性鸟类的鸣叫声全球数据集。研究结果表明，在光照充足的地区，鸟类平均每天鸣叫时间延长50分钟，比在较暗环境中生活的鸟类早18分钟开始鸣叫，晚32分钟停止鸣叫。

该研究利用卫星数据测量了每个“鸟天气”站点的光污染强度。皮斯和吉尔伯特对这种影响的程度表示惊讶，指出在最亮的条件下，鸟类的“白天”几乎延长了一个小时。这种改变的活动可能会影响鸟类的生存和繁殖，可能导致因休息减少而增加卡路里需求，或者相反，改善觅食和繁殖成功率。

作者强调，日益严重的光污染对人类和野生动物的健康构成威胁，尤其是在鸟类数量已经下降的情况下。他们认为，光污染导致的活动时间延长可能会导致鸟类产生类似人类的“睡眠债”，从而导致负面的健康结果。需要进一步的研究来充分了解这种改变行为的后果。

---

## 35. Rv，一种新型的Ruby管理工具

**原文标题**: Rv, a new kind of Ruby management tool

**原文链接**: [https://andre.arko.net/2025/08/25/rv-a-new-kind-of-ruby-management-tool/](https://andre.arko.net/2025/08/25/rv-a-new-kind-of-ruby-management-tool/)

本文介绍了`rv`，一种旨在通过集成 Ruby 版本和依赖管理来简化 Ruby 开发的新型 Ruby 管理工具。`rv` 受 Python 工具 `uv` 的启发，使用 Rust 编写，以保证速度和可靠性。

`rv` 的主要功能包括：

*   **快速安装：** 快速安装预编译的 Ruby 版本，消除冗长的编译时间。
*   **`rv tool run`：** 使用隔离的 Ruby 和 gem 依赖项执行 CLI 命令，防止与当前项目环境发生冲突。
*   **`rv tool install`：** 将 gem 作为 CLI 工具安装，并具有单独的隔离环境，允许在不同项目中使用不同的 gem 版本。
*   **脚本支持：** 运行包含 Ruby 版本、gem 依赖项和代码的单文件脚本，确保执行的正确环境。
*   **统一管理：** 结合 Ruby 版本和依赖管理，无需像 `rvm` 和 `bundler` 这样的多个工具。

`rv` 旨在自动化整个环境设置过程，使开发人员只需运行命令，而无需手动配置。该项目由作者领导，并包括来自 RubyGems 团队和 rbenv 创建者的贡献者。最初的实现支持在已安装的 Ruby 版本之间自动切换，并快速安装预编译的 Ruby 3.4.x。作者鼓励用户尝试该工具并探索其未来计划。

---

## 36. GNU Artanis – Scheme 的快速 Web 应用程序框架

**原文标题**: GNU Artanis – A fast web application framework for Scheme

**原文链接**: [https://artanis.dev/index.html](https://artanis.dev/index.html)

GNU Artanis：健壮快速的Scheme Web应用框架，专为专业Web开发设计。它于2013年在GNU Guile黑客聚餐会上诞生，之后在“Lisp In Summer Projects”竞赛中被评为优秀项目。2015年，它成为一个正式的GNU项目。截至2021年末，GNU Artanis由HardenedLinux社区维护。

Artanis轻量级、易于学习，并支持多种数据格式，如JSON、CSV、XML和SXML，以及WebSocket。它具有完整的Web服务器实现，包括错误处理、高并发异步非阻塞服务器核心，并通过guile-dbi支持MySQL、SQLite和PostgreSQL等数据库。它还提供良好的Web缓存控制、高效的HTML模板解析以及高效的静态文件上传/下载。

该框架采用GPLv3+ & LGPLv3+双重许可。下载、文档和源代码可在GNU FTP服务器、Gitlab和Savannah上找到。

GNU Artanis的诞生源于使用GNU Guile（GNU的官方扩展语言）创建Web框架的愿望。它在许多开发人员的贡献下得到积极维护。最初的作者和目前的维护者是Mu Lei (NalaGinrut)。您可以通过邮件列表或GitLab参与其中。

---

## 37. 中国航天员在太空制造火箭燃料和氧气

**原文标题**: Chinese astronauts make rocket fuel and oxygen in space

**原文链接**: [https://www.livescience.com/space/space-exploration/chinese-astronauts-make-rocket-fuel-and-oxygen-in-space-using-1st-of-its-kind-artificial-photosynthesis](https://www.livescience.com/space/space-exploration/chinese-astronauts-make-rocket-fuel-and-oxygen-in-space-using-1st-of-its-kind-artificial-photosynthesis)

在天宫空间站上的中国航天员已成功利用一种新型“人工光合作用”工艺制造出火箭燃料和氧气。这项自2015年开始研发的技术，通过将二氧化碳和水转化为乙烯（一种火箭燃料成分）和氧气，模拟植物的光合作用，利用一个简单的装置和一个半导体催化剂。该过程所需的能量远低于传统的电解方法制氧。

这项突破对中国雄心勃勃的太空计划至关重要，特别是其在2035年之前建立月球基地的计划。利用月球上的水等当地资源生产燃料和可呼吸空气将大大降低登月任务的成本和复杂性，并有可能实现更深层次的太空探索。研究人员还认为，通过使用不同的催化剂，他们可以生产甲烷（也可用于燃料）和甲酸（可用作防腐剂、抗菌剂或制造糖的前体）。

中国还在开发其他技术以支持其月球基地，包括一个用于供电的微型核反应堆。该国计划在2030年之前将人类送上月球，与美国宇航局的阿尔忒弥斯计划同时进行。

---

## 38. 脑机接口“参与者1号”称生活已改变

**原文标题**: Neuralink 'Participant 1' says his life has changed

**原文链接**: [https://fortune.com/2025/08/23/neuralink-participant-1-noland-arbaugh-18-months-post-surgery-life-changed-elon-musk/](https://fortune.com/2025/08/23/neuralink-participant-1-noland-arbaugh-18-months-post-surgery-life-changed-elon-musk/)

诺兰·阿博，代号“1号参与者”，于2024年2月成为首位植入Neuralink脑芯片的人类。自2016年事故导致瘫痪后，该芯片使他能够用意念控制电脑，无需身体移动即可玩电子游戏、控制设备等。阿博表示，植入物具有变革性意义，在多年沉寂后赋予了他全新的目标感。他目前就读于社区大学，学习神经科学，并开始从事演讲业务。

Neuralink的设备使用包含1000多个电极的线束连接到运动皮层中的神经元，与其他脑机接口相比，提供了更高的连接率。与一些竞争对手不同，它是无线的，但需要充电。阿博曾面临挑战，包括一些线束回缩导致他失去控制，但Neuralink团队已努力解决这些问题。尽管如此，他仍然是该技术的坚定支持者。

继阿博之后，又有八人接受了Neuralink植入。Neuralink正在将试验扩展到其他国家，并探索恢复视力和开发由意念控制的机械肢等应用。阿博强调，Neuralink让他能够自由地发言，不受审查。虽然Neuralink因其侵入性方法、长时间工作和过去的动物待遇而面临审查，但阿博认为，像Neuralink脑芯片这样的技术代表着医学的未来，并将为残疾提供解决方案。

---

## 39. 磁设备中首个绝对超导开关问世

**原文标题**: First absolute superconducting switch developed in a magnetic device

**原文链接**: [https://phys.org/news/2025-08-absolute-superconducting-magnetic-device.html](https://phys.org/news/2025-08-absolute-superconducting-magnetic-device.html)

于韦斯屈莱大学的研究人员与国际合作伙伴合作，创造了首个绝对超导开关，这是节能电子学的一项重大进展。该开关基于皮埃尔-吉勒·德热纳在1966年提出的概念，完全抑制超导和铁磁结中的超导性。

该开关使用硫化铕（EuS）作为绝缘铁磁体，铌（Nb）作为超导体，中间有一层关键的金层。这层金增强了邻近交换场，使得基于铁磁层磁化对准的超导性完全开启/关闭成为可能。当磁化平行时，超导性被抑制，当反平行时，该效应会抵消。

这项突破克服了以往设计的局限性，以往的设计仅显示了超导临界温度的敏感性，而没有完全抑制。这种新型开关有可能通过消除当前热开关的持续热负载来大幅降低电子产品的能耗。它还为开发非易失性超导随机存取存储设备铺平了道路。该研究发表在《自然·通讯》上。

---

## 40. 一种通用抗病毒药物，一统天下？

**原文标题**: One universal antiviral to rule them all?

**原文链接**: [https://www.cuimc.columbia.edu/news/one-universal-antiviral-rule-them-all](https://www.cuimc.columbia.edu/news/one-universal-antiviral-rule-them-all)

哥伦比亚大学免疫学家杜桑·博古诺维奇正在开发一种潜在的通用抗病毒疗法，其灵感来自于ISG15缺陷症患者，这是一种罕见的基因突变，赋予他们对病毒感染的广泛抵抗力。这些个体具有轻微、持续的抗病毒炎症，可以在不引起明显疾病的情况下保护他们免受多种病毒的侵害。

博古诺维奇的疗法旨在模仿这种保护作用，而不会产生ISG15缺陷症患者所见的全面炎症反应。他的团队开发了一种实验性疗法，该疗法递送编码10种负责抗病毒保护的蛋白质的mRNA，并将其包装在脂质纳米颗粒中。通过鼻腔滴注给药，该疗法已在仓鼠和小鼠中显示出前景，可防止流感和SARS-CoV-2的病毒复制并降低疾病的严重程度。在细胞培养中，该疗法已证明对多种病毒具有广泛的有效性。

该疗法被设计为短期预防性措施，可能有助于在疫情期间保护像急救人员这样的弱势群体。重要的是，它不会阻止长期免疫记忆的形成。目前主要的挑战仍然在于优化药物向肺部的输送，以及确定抗病毒保护的持续时间，目前估计为三到四天。尽管存在这些挑战，博古诺维奇认为这项研究源于对罕见遗传疾病的最初好奇心，为通用抗病毒防御提供了潜力。

---

## 41. 逆向工程覆盆子派计算模块 5

**原文标题**: Reverse Engineered Raspberry Pi Compute Module 5

**原文链接**: [https://github.com/schlae/cm5-reveng](https://github.com/schlae/cm5-reveng)

本文详细介绍了个人对树莓派计算模块5 (CM5) 的逆向工程，目的是为了理解其设计以进行项目故障排除。作者提供了逆向工程的原理图和布局（使用KiCad），并强调其仅用于教育和高级黑客用途，而非用于制造，因为存在不准确之处和无法获得的组件。

作者概述了该过程，包括组件移除、测量、电路板打磨以及高分辨率扫描，以便在KiCad中进行追踪。值得注意的发现包括用于内存和eMMC配置选择的电阻分压系统，电路板的10层堆叠（2+6+2，带有微孔），以及PMIC的热插拔功能。文章还提到可以通过GPIO禁用WiFi/蓝牙，以及配备eMMC的CM5模块上没有SD卡冲突。

文章包含一份全面的、更新的测试点列表，其中坐标相对于电路板，纠正并扩展了官方树莓派数据手册。还提供了一个显示近似层堆叠的表格。包括一个关于未识别RP1引脚的部分，以及未来的工作，包括PCIe和RP1到BCM2712网络的识别以及PMIC I2C寄存器映射。该项目根据CC BY-SA 4.0许可协议发布。

---

## 42. 多元宇宙的软体动物：万智牌中的软体动物多样性

**原文标题**: Molluscs of the Multiverse: molluscan diversity in Magic: The Gathering

**原文链接**: [https://jgeekstudies.org/2025/08/24/molluscs-of-the-multiverse-molluscan-diversity-in-magic-the-gathering/](https://jgeekstudies.org/2025/08/24/molluscs-of-the-multiverse-molluscan-diversity-in-magic-the-gathering/)

“多元宇宙的软体动物：万智牌中软体动物的多样性”一文探讨了万智牌（MTG）多元宇宙中软体动物的存在和多样性。作者作为软体动物学家，深入研究了游戏中卡牌所代表的头足类、腹足类和双壳类动物，分析了它们的生物学合理性和潜在灵感来源。

该研究强调了腹足类动物多样性的显著增加，尤其是在引入布卢姆巴勒（Bloomburrow）系列以及围绕“巨蜗牛”的鼠民文化之后。分析涵盖了蜗牛、蛞蝓、海螺和海蛞蝓，讨论了其解剖学准确性、寄生影响以及潜在的现实世界对应物。值得注意的是，它指出了蛞蝓生物衍生物不真实的嘴巴、吐痰蛞蝓镜像的解剖结构以及托克西尔蛞蝓恐怖的独特特征。

该研究还考察了双壳类动物，重点关注巨型牡蛎和神秘的蛤人——具有蛤蜊状头部的人形生物。这些双壳类动物是幽默的来源，同时文章还解释了这些双壳类动物如何融入MTG世界。

最后，该研究承认了MTG中头足类动物范围的扩大，包括新的传奇生物和通过生物魔法创造的各种混合体。它得出结论，万智牌中头足类动物的数量激增，其中一些具有传奇般的实力和声望。

---

## 43. 双子座2.5闪存镜像

**原文标题**: Gemini 2.5 Flash Image

**原文链接**: [https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/](https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/)

Gemini 2.5 Flash Image发布：全新图像生成和编辑模型，以低延迟、高性价比为开发者提供更强大的创作控制。它允许用户融合多张图像、保持跨提示的角色一致性、使用自然语言进行定向转换，并利用Gemini的世界知识来增强图像理解。

该模型可通过Gemini API和面向开发者的Google AI Studio，以及面向企业的Vertex AI访问，定价为每张图片0.039美元。Google AI Studio已更新，以促进构建自定义AI驱动的应用程序，从而轻松进行测试、混音和部署到GitHub。

主要功能包括：保持跨各种设置的角色一致性、基于提示的图像编辑以进行精确的局部调整、用于理解和交互真实世界元素的原生世界知识，以及用于创建照片级真实复合图像的多图像融合。演示这些功能的模板应用程序可在Google AI Studio中使用。

OpenRouter.ai和fal.ai已合作将Gemini 2.5 Flash Image提供给其开发者社区。所有生成的图像都包含一个不可见的SynthID数字水印，以将其标识为AI生成或编辑的。Google正在积极努力改进模型的功能，并鼓励用户提供反馈。

---

## 44. 自带代理到 Zed – Gemini CLI 功能

**原文标题**: Bring Your Own Agent to Zed – Featuring Gemini CLI

**原文链接**: [https://zed.dev/blog/bring-your-own-agent-to-zed](https://zed.dev/blog/bring-your-own-agent-to-zed)

Zed 通过新的 Agent Client Protocol (ACP) 集成第三方代理，Gemini CLI 是与 Google 合作的初始参考实现。ACP 旨在将代理智能从编辑器中解耦，类似于 Language Server Protocol 对语言智能的作用方式，使用户无需切换编辑器即可切换代理。

与 Gemini CLI 的合作源于他们在 Zed 集成终端中使用该代理的积极体验。ACP 使用 JSON-RPC 端点来促进客户端 (Zed) 和代理 (Gemini CLI) 之间的通信，从而解锁高级功能，例如实时编辑可视化和多缓冲区审查，这些功能在编辑器之外难以实现。

ACP 是开源的，允许开发人员选择最适合其工作流程的工具，并提供强大的 UI 来与代理交互、控制其访问以及审查更改。用户数据保持私密，因为未经明确同意，Zed 不会访问代码。Code Companion 也将为 Neovim 用户带来对 ACP 的支持。Zed 已更新其进程内代理以使用相同的代码路径，从而确保代理体验的一致性。Zed 鼓励对 ACP 的贡献和反馈，以培养一个多元化的代理和客户端生态系统，同时保持控制以指导其发展。文章最后邀请大家试用 Zed、申请职位空缺，并为软件开发的未来做出贡献。

---

## 45. 日本首座渗透能发电站已启用

**原文标题**: Japan has opened its first osmotic power plant

**原文链接**: [https://www.theguardian.com/world/2025/aug/25/japan-osmotic-power-plant-fukuoka](https://www.theguardian.com/world/2025/aug/25/japan-osmotic-power-plant-fukuoka)

日本在福冈开设首家渗透发电厂，成为继丹麦之后全球第二家此类电厂。该电厂利用渗透作用的能量，即淡水通过半透膜流向咸水以进行稀释的自然过程。通过将淡水（或处理过的废水）和海水置于膜的两侧，咸水侧的压力增加被用于驱动涡轮机并产生电力。

福冈电厂预计每年将产生88万千瓦时的电力，足以帮助一家海水淡化厂供电。虽然电力产量不大（相当于为约220户日本家庭供电），但渗透发电提供了一种稳定的、全天候的能源，不像某些依赖风或天气的可再生能源。

扩大该技术的规模仍然面临挑战。在抽水过程中和由于膜上的摩擦会发生能量损失，从而影响净能量增益。然而，膜和泵技术的进步正在提高效率。在日本电厂中使用浓缩海水（盐水）也提高了能源可用性。

专家们一致认为，福冈电厂标志着渗透发电的一项令人兴奋的进步，证明了其大规模能源生产的潜力。 澳大利亚等拥有盐湖的地方具有进一步发展的潜力，这些盐湖可以提供资源和专业知识来建造类似的电厂。

---

## 46. 一名青少年有自杀倾向，ChatGPT是他倾诉的朋友。

**原文标题**: A teen was suicidal. ChatGPT was the friend he confided in

**原文链接**: [https://www.nytimes.com/2025/08/26/technology/chatgpt-openai-suicide.html](https://www.nytimes.com/2025/08/26/technology/chatgpt-openai-suicide.html)

无法访问文章链接。

---

## 47. AI泡沫2027

**原文标题**: AI Bubble 2027

**原文链接**: [https://www.wheresyoured.at/ai-bubble-2027/](https://www.wheresyoured.at/ai-bubble-2027/)

题为《2027年人工智能泡沫》的这篇文章认为，当前的人工智能繁荣是一个注定破裂的泡沫，可能在2027年初破裂。作者批评围绕人工智能的“非理性繁荣”，指出研究表明，大多数使用生成式人工智能的组织缺乏投资回报，以及Meta的人工智能招聘冻结是麻烦的迹象。

作者认为过度乐观的“2027年人工智能”预测是幻想小说，并概述了导致泡沫破裂的具体条件：英伟达的增长放缓（因为英伟达的成功推动了整个AI股票市场叙事）、人工智能资金枯竭（许多公司依赖于持续的投资）、OpenAI或Anthropic等大型人工智能公司因不可持续的支出而倒闭，以及大型科技公司停止其人工智能资本支出，承认其有限的收入产生能力。他认为，2025年公司从人工智能中获得的收入几乎只有350亿美元。

进一步的催化剂包括人工智能初创公司因不切实际的估值而倒闭，以及CoreWeave（OpenAI的关键计算提供商）可能因财务压力和未履行的义务而失败。作者认为，星际之门项目失败将严重影响OpenAI的财务状况。

作者强调，泡沫破裂将是一系列事件，可能持续一年，而不是一个单一的灾难性时刻。泡沫是由情绪而非回报驱动的，对人工智能金融不可持续性的批评将逐渐加剧。作者预测，人工智能的繁荣暴露了盲目拥抱人工智能来控制劳动力和验证“点子王”的领导者的无能，突出了炒作与现实之间的脱节。

---

## 48. spaCy：Python 工业级自然语言处理

**原文标题**: SpaCy: Industrial-Strength Natural Language Processing (NLP) in Python

**原文链接**: [https://github.com/explosion/spaCy](https://github.com/explosion/spaCy)

SpaCy是一个工业级的Python和Cython自然语言处理(NLP)库，专为现实应用而设计。它拥有最先进的速度和准确性，支持超过70种语言，并为分词、标注、句法分析、命名实体识别和文本分类等任务提供预训练管道。SpaCy利用神经网络模型和多任务学习，并结合了BERT等Transformer模型。

该库提供了一个可用于生产的训练系统、简易的模型打包和部署以及工作流程管理。它是MIT许可下的商业开源软件。主要特性包括对自定义组件的支持、与PyTorch和TensorFlow的集成、内置的可视化工具和强大的准确性。

可以通过pip或conda-forge进行安装，文档提供了针对不同操作系统和Python版本的详细说明。升级SpaCy可能需要使用`validate`命令更新统计模型。训练好的管道可以使用`download`命令或手动通过pip作为Python包安装。

开发者可以通过克隆GitHub存储库从源代码编译SpaCy，这对于为代码库做贡献是推荐的做法。此过程需要一个具有Python、编译器、pip、virtualenv和git的开发环境。一个广泛的测试套件确保了代码质量。该文章还提供了文档、使用指南、项目模板、API参考以及其他资源（如在线课程、博客和YouTube频道）的链接。

---

## 49. 使用直接分区哈希计算绕过 PostgreSQL 目录开销

**原文标题**: Bypass PostgreSQL catalog overhead with direct partition hash calculations

**原文链接**: [https://www.shayon.dev/post/2025/221/bypass-postgresql-catalog-overhead-with-direct-partition-hash-calculations/](https://www.shayon.dev/post/2025/221/bypass-postgresql-catalog-overhead-with-direct-partition-hash-calculations/)

本文探讨了PostgreSQL哈希分区中的性能瓶颈，特别是通过父表查询分区表时目录查找的开销。哈希分区使用基于分区键的哈希函数将数据均匀地分布到各个分区，通过减小索引大小、降低自动清理压力并启用分区修剪，从而提高大型表的性能。两级分区虽然提供了细粒度的数据分布，但也加剧了目录查找的开销，因为PostgreSQL必须遍历更深的层级才能找到目标分区。

作者提出通过在应用程序代码中直接计算目标分区来绕过此开销，从而消除对PostgreSQL目录遍历的需求。本文介绍了`pg_hash_func`，一个Ruby gem，它可以逆向工程PostgreSQL的内部哈希分区逻辑，允许应用程序直接计算基于整数的哈希分区（bigint，integer，smallint）的分区索引。或者，可以直接在SQL查询中调用PostgreSQL的哈希函数。

基准测试表明，在Ruby中计算分区索引比使用SQL查询获得相同结果要快得多（20-40倍）。文章总结说，虽然标准的父表方法适用于大多数应用程序，但直接计算目标分区为高吞吐量、对延迟敏感的工作负载提供了显着的性能改进。这种方法保持了分区的好处（更小的索引、降低的自动清理压力、更好的维护），同时优化了查询性能。

---

## 50. AI代码加速了我，但我再也不能伴着音乐编程了。

**原文标题**: AI coding made me faster, but I can't code to music anymore

**原文链接**: [https://www.praf.me/ai-coding](https://www.praf.me/ai-coding)

AI编程让我更快，但不能再伴随音乐编程了

---

## 51. iOS 18.6.1 零点击远程代码执行漏洞POC

**原文标题**: iOS 18.6.1 0-click RCE POC

**原文链接**: [https://github.com/b1n4r1b01/n-days/blob/main/CVE-2025-43300.md](https://github.com/b1n4r1b01/n-days/blob/main/CVE-2025-43300.md)

由用户b1n4r1b01创建的名为"iOS 18.6.1 零点击RCE POC"的Github仓库，似乎包含iOS 18.6.1版本中的远程代码执行(RCE)漏洞的概念验证(POC)。 关键在于，标题表明这是一个“零点击”漏洞利用，这意味着它可以在没有任何用户交互的情况下被触发。 这使得它特别危险。

信息简明扼要，但暗示该存储库可能包含代码、文档或其他资源，这些资源演示了如何利用该漏洞在易受攻击的iOS设备上执行任意代码，而无需用户单击链接、打开文件或执行任何其他显式操作。

该存储库已被fork了62次，并获得了395颗星，表明安全研究社区对此有浓厚的兴趣和潜在的验证。 “/n-days/Public”路径表明该漏洞是新发现的且公开可用。

总而言之，该存储库可能包含iOS 18.6.1的零点击RCE漏洞利用程序，引起了安全研究人员的关注，并可能对受影响设备的用户构成重大的安全风险。

---

## 52. 为什么人们一直在写关于虚构化合物Cr2Gr2Te6的文章？

**原文标题**: Why do people keep writing about the imaginary compound Cr2Gr2Te6?

**原文链接**: [https://www.righto.com/2025/08/Cr2Ge2Te6-not-Cr2Gr2Te6.html](https://www.righto.com/2025/08/Cr2Ge2Te6-not-Cr2Gr2Te6.html)

这篇博文强调了科学文献中一个反复出现的拼写错误：虚构的化合物“Cr2Gr2Te6”，其中“Gr”被错误地用来代替锗（Ge），导致了实际化合物Cr2Ge2Te6（碲化铬锗）。

作者在最近一期的《科学》杂志上偶然发现了这个错误，并追溯到2017年Cr2Ge2Te6和CrI3中本征铁磁性的发现。作者发现随后有几篇出版物在引用CrI3的同时错误地提到了“Cr2Gr2Te6”，表明该错误在多篇论文中被复制。

作者认为，由于键盘上“Ge”和“Gr”的位置接近以及公式的视觉相似性，这个拼写错误很容易发生。然而，更大的担忧是人工智能可能会学习到这个错误的公式并将其作为错误信息传播。作者希望通过引起更广泛的关注来纠正这个错误。

对这篇文章的评论也呼应了这些担忧。他们强调了学术出版的压力导致错误，提到了人工智能生成的虚假论文，并讨论了其他被永久延续的错误，比如“营养电子显微镜”。一位评论者质疑Cr2Ge2Te6是一种真正的化合物还是合金，而作者根据研究人员和供应商的称呼方式捍卫了其作为化合物的分类。评论还指出了研究出版中日益严重的腐败和低标准问题。

---

## 53. 麦克菲深度报道非虚构写作法

**原文标题**: The McPhee method for writing deeply reported nonfiction

**原文链接**: [https://jsomers.net/blog/the-mcphee-method](https://jsomers.net/blog/the-mcphee-method)

詹姆斯·萨默斯的文章概述了约翰·麦克菲深度报道非虚构作品的“麦克菲方法”。该方法归功于《纽约客》作家约翰·麦克菲，旨在避免面对空白页，包括四个阶段：收集笔记、选择笔记、构建笔记以及写作。

第一阶段，收集笔记，强调广泛的报道：通过长时间的互动、访谈和研究，让自己沉浸在主题的生活中。麦克菲建议持续这个过程，直到故事变得重复。由此产生的笔记，最初是无组织的，被汇编成一个大的单一文件。这种沉浸和笔记也有助于作者理解主题并确定什么值得注意。

第二和第三阶段侧重于组织。麦克菲主张重新吸收所有笔记，并为章节、场景和组块开发结构性想法，用首字母缩略词代码在索引卡上表示。然后物理排列这些卡片，以确定文章的逻辑流程，从而创建一个“约束满足问题”，确保逻辑结构。之后，笔记本身会被标记上相应的代码，并整理到物理文件夹中，创建一个具有主要部分和子部分的递归结构。

最后阶段，写作，变得更容易，因为结构已经确定。这使得作者可以专注于撰写句子、修改和润色。萨默斯强调，麦克菲方法分散了思考和决策，使写作过程不那么令人生畏。他还强调了麦克菲早期采用计算机和定制软件来有效地管理笔记。最终，麦克菲方法强调从大量精心策划和结构化的笔记中构建作品。

---

## 54. 人工智能时代的Delphi

**原文标题**: Delphi in the Age of AI

**原文链接**: [https://learndelphi.org/delphi-ai-ultimate-guide/](https://learndelphi.org/delphi-ai-ultimate-guide/)

人工智能时代的Delphi：探索人工智能在Delphi开发中的应用。文章首先定义了人工智能和神经网络，然后介绍了各种Delphi兼容的人工智能工具和API，如CAI Neural API和Keras4Delphi，并提供了代码示例。这些API有助于在Delphi应用程序中执行图像分类和创建神经网络等任务。

文章重点介绍了人工智能在软件开发中的广泛应用，强调机器学习是关键组成部分。文章介绍了TensorFlow，这是一个流行的用于数值计算和机器学习的开源库，并演示了如何使用Python4Delphi将其与Delphi集成。示例代码展示了如何在Delphi应用程序中执行包含TensorFlow模型的Python脚本。

文章还介绍了利用人工智能的开源Delphi项目，包括：Stable Diffusion Client、CodeDroid AI、SDXL Inpainting和AI Vision Chat。这些项目展示了人工智能在Delphi中的实际应用，例如生成艺术、代码生成、图像修复和视觉人工智能交互。这些项目支持基于云或本地的GPU，并且与Windows、macOS和Linux兼容。文章提供了下载这些项目的链接，以及RAD Studio IDE。总而言之，本文旨在为希望将人工智能功能集成到其项目中的Delphi开发人员提供指导，并提供易于使用的工具和示例。

---

## 55. Rust 带来的意外生产力提升

**原文标题**: The unexpected productivity boost of Rust

**原文链接**: [https://lubeno.dev/blog/rusts-productivity-curve](https://lubeno.dev/blog/rusts-productivity-curve)

无法访问文章链接。

---

## 56. 密歇根州最高法院：无限制电话搜查违反第四修正案

**原文标题**: Michigan Supreme Court: Unrestricted phone searches violate Fourth Amendment

**原文链接**: [https://reclaimthenet.org/michigan-supreme-court-rules-phone-search-warrants-must-be-specific](https://reclaimthenet.org/michigan-supreme-court-rules-phone-search-warrants-must-be-specific)

密歇根州最高法院裁定，执法机构在搜查手机时必须获得特定搜查令，推翻了下级法院的判决。该法院认为，允许无限制访问手机内容的搜查令违反了宪法第四修正案对不正当搜查和扣押的保护。

该案件涉及一名被告，他因在其手机上发现的证据而被判犯有儿童色情罪。最初的搜查令广泛授权搜查手机上的“任何及所有数据”。最高法院的结论是，这种一概而论的授权缺乏必要的明确性，认为这允许执法人员筛选大量与涉嫌犯罪无关的个人信息。

该裁决强调，搜查令需要进行有针对性的定制，明确规定要搜索的数据类型以及与调查相关的时间范围。这确保了执法人员不会获得对个人设备上存储的私人通信、照片、财务记录和其他敏感信息的无限制访问权限。

这项裁决对密歇根州的执法实践具有重大影响，要求他们获得更精确的搜查令，明确说明手机搜查的范围和限制。它旨在在调查犯罪的合法需求和宪法赋予的隐私权之间取得平衡。该裁决强调了司法监督在保护个人免受对其数字生活的不正当侵犯方面的重要性。

---

## 57. 为小型语言模型构建代理：轻量级人工智能深入解析

**原文标题**: Building Agents for Small Language Models: A Deep Dive into Lightweight AI

**原文链接**: [https://www.msuiche.com/posts/building-agents-for-small-language-models-a-deep-dive-into-lightweight-ai/](https://www.msuiche.com/posts/building-agents-for-small-language-models-a-deep-dive-into-lightweight-ai/)

本文探讨了为小型语言模型 (SLM) 构建人工智能代理的新兴领域，并将其与传统上对大型语言模型 (LLM) 的关注进行了对比。它强调了 SLM 带来的独特挑战和机遇，由于本地部署和开放权重，SLM 具有隐私、成本可预测性和控制等优势。

本文重点介绍了 SLM 代理设计的关键原则，包括资源驱动设计、优先考虑稳定性而非功能以及特定于模型的优化。它概述了一个参考架构，包含安全、模型管理、推理和硬件抽象层。它详细介绍了云 LLM 和本地 SLM 之间的性能和能力权衡，并列出了开源 SLM 开发的必要工具，例如 GGUF、llama.cpp 以及用于模型量化、提示测试和内存分析的工具。

本文还讨论了当前的局限性，包括上下文窗口管理、推理能力、一致性、性能与质量的权衡、硬件兼容性和错误恢复。它提倡接受约束并进行可靠性设计。

本文的第二部分侧重于使用超小型开源模型（2.7亿-10亿参数）进行实际实施，强调简单性和外部化逻辑。它强调了性能优化、最小上下文和多层安全架构对于防止崩溃的重要性。该文档概述了具体的实现模式，例如动态批处理管理、特定于模型的配置以及具有 UTF-8 安全性的流式传输，这对于构建稳健可靠的 SLM 代理至关重要。

---

## 58. 马尔莫雷瀑布

**原文标题**: Cascata delle Marmore

**原文链接**: [https://en.wikipedia.org/wiki/Cascata_delle_Marmore](https://en.wikipedia.org/wiki/Cascata_delle_Marmore)

马尔莫雷瀑布，是位于意大利翁布里亚大区特尔尼附近的一座阶梯式人工瀑布。由罗马人公元前271年建造，高165米（541英尺），是世界上最高的人工瀑布。

最初，韦利诺河滋养着列蒂山谷的一片湿地。罗马人为了开垦土地，将河流改道，使其流过悬崖，流入内拉河。几个世纪以来，维护问题导致湿地重新出现，于是人们建造了新的运河并对水流进行了改造，最终，1787年教皇庇护六世的改造使瀑布呈现出现在的面貌。

拜伦勋爵在他的诗歌《恰尔德·哈罗德游记》中提到了这座瀑布。1896年，水流开始被特尔尼的钢铁厂利用，后来用于发电。如今，水通常被引流到1929年建立的加莱托水力发电厂。

为了兼顾发电厂和旅游业，瀑布按时间表运行，通常每天流动几个小时。游客可以付费进入瀑布，并探索通往山顶的小路，包括带有观测点的隧道，可欣赏瀑布和内拉山谷的全景。

---

## 59. Show HN: Async – 一款集成了 Claude 代码、Linear 和 GitHub PR 的工具 (颇具主见)

**原文标题**: Show HN: Async – Claude code and Linear and GitHub PRs in one opinionated tool

**原文链接**: [https://github.com/bkdevs/async-server](https://github.com/bkdevs/async-server)

Async：一款利用AI辅助代码、任务管理和代码审查，简化成熟代码库开发流程的开源开发者工具。它将Claude Code用于AI编码，Linear用于任务管理，并将GitHub PR集成到一个工作流程中。

Async通过研究代码库、提出澄清问题并在隔离的云环境中执行更改来自动化编码任务，从而防止对本地环境的干扰。它将工作分解为可审查的子任务，创建堆叠差异以方便代码审查，并促进从GitHub issue到合并PR的完整工作流程。

主要功能包括：通过澄清问题进行前期规划、异步云执行以消除上下文切换、通过GitHub issue导入实现简单的任务跟踪，以及内置的代码审查功能，包括对堆叠差异进行评论和迭代。

技术栈包括FastAPI后端、Claude Code用于实现、OpenAI/Anthropic/Google模型用于研究、Google Cloud Platform用于容器化执行、Firebase Firestore用于数据库，以及与GitHub、Stripe和电子邮件的集成。

该系统使用Google Cloud Run作业来执行研究、执行和修订等任务，确保隔离和可扩展的处理。设置涉及配置API密钥（Anthropic、OpenAI、Google）、Stripe、GitHub和数据库连接的环境变量。

Async旨在成为一个全面的工具，通过将AI驱动的编码与集成的任务和代码审查管理相结合，促进经验丰富的开发人员高效和协作的开发。

---

## 60. 显示 HN：BYTE 杂志的可缩放、可搜索的档案

**原文标题**: Show HN: A zoomable, searchable archive of BYTE magazine

**原文链接**: [https://byte.tsundoku.io](https://byte.tsundoku.io)

“Show HN”：BYTE杂志可缩放搜索的视觉档案馆。核心内容是一个包含杂志页面扫描图像的网站，使用户能够以数字方式浏览和阅读该出版物。主要功能可能包括放大页面以提高可读性，以及搜索功能以查找存档中的特定文章、作者或关键词。该网站旨在保存并提供对BYTE杂志内容的访问，这是一本在个人计算机革命中具有历史意义的出版物。它为研究人员、爱好者以及任何对计算机历史感兴趣的人提供了宝贵的资源。

---

## 61. 拥有家用电脑的人 (1967) [视频]

**原文标题**: The man with a Home Computer (1967) [video]

**原文链接**: [https://www.youtube.com/watch?v=w6Ka42eyudA](https://www.youtube.com/watch?v=w6Ka42eyudA)

此条目看似指向一个名为“拥有家用电脑的男人（1967）”的YouTube视频。然而，提供的“内容”仅为YouTube标准的页脚信息，涉及版权、广告、开发者工具、服务条款、隐私政策和Google的所有权。

因此，没有关于视频本身的实际内容。我们只能推断视频可能描述或讨论了一位1967年拥有家用电脑的男人。这会是一个非常罕见且可能具有开创性的情况，因为家用电脑在当时并不普及。视频可能探索了他拥有的电脑类型、他如何使用它，以及在那个时代拥有这种技术的意义。在没有更多关于视频实际内容的信息的情况下，更详细的总结是不可能的。

---

## 62. 保罗一世纪在罗马世界的旅行互动地图

**原文标题**: Interactive map of Paul's first century travels in Roman world

**原文链接**: [https://www.intofarlands.com/map-of-pauls-journeys](https://www.intofarlands.com/map-of-pauls-journeys)

本网站提供互动地图，详细展示了公元一世纪使徒保罗在罗马世界的四次旅程。该网站名为“绘制保罗在罗马世界的旅程”，用户可以探索保罗第一次、第二次和第三次宣教旅程以及他最终前往罗马的旅程的路线和停靠点。

互动地图使用不同颜色的路线来区分每次旅程：橙色（第一次旅程）、紫色（第二次旅程）、绿色（第三次旅程）和红色（前往罗马的旅程）。用户很可能可以点击地图上的特定地点，以了解更多关于每个停靠点和相关圣经故事的信息。

该网站还提到一个正在进行的项目，旨在实地重走保罗的足迹，目标是在 2026 年底完成。用户可以在 Instagram 上关注 @kingdoms.collide，了解项目的进展情况并接收每日更新。

除了互动地图外，该网站还包括“关于”、“故事”和“探索”等部分，暗示了与保罗的旅行和经历相关的更多内容。通过电子邮件地址 intofarlands@gmail.com 提供联系方式，以及免责声明和隐私政策。本质上，该网站是一个教育资源和旅行日志，将历史和宗教信息与对保罗旅程的现代探索相结合。

---

## 63. “特殊寄存器组”入侵计算机词典数十年 (2019)

**原文标题**: "Special register groups" invaded computer dictionaries for decades (2019)

**原文链接**: [https://www.righto.com/2019/10/how-special-register-groups-invaded.html](https://www.righto.com/2019/10/how-special-register-groups-invaded.html)

本文探讨了“特殊寄存器组”这一短语在半个多世纪以来 CPU 定义中令人好奇的持续存在。作者发现，这个在现代计算环境中看似毫无意义的短语，不断出现在词汇表和教科书中，甚至在最近的出版物中也有出现。

调查显示，“特殊寄存器组”起源于霍尼韦尔 800 大型计算机（1959 年推出）的特定硬件功能。为了支持其同时运行八个程序的能力，每个程序都有自己专用的 32 个寄存器组，从而能够快速切换程序。

霍尼韦尔的词汇表将“CPU”和“大型机”（当时是同义词）定义为包含“特殊寄存器组”。美国农业部和其他政府机构在 20 世纪 60 年代采用了并传播了这一定义。从那时起，它传播到无数的计算机词汇表、教科书，甚至国家报纸，尽管随着计算机架构的发展，它变得无关紧要。

作者强调了权威定义的持久力量，即使在它们过时之后也是如此。该研究说明了计算术语的含义如何随时间推移而变化，“大型机”和“CPU”的含义逐渐分化，同时也揭示了旧机器的特定功能如何能够保留在集体数字意识中。

---

## 64. 人工智能驱动的根本原因分析 - 限量免费使用

**原文标题**: AI-Powered Root Cause Analysis – Limited Free Use

**原文链接**: [https://github.com/coroot/coroot/releases/tag/v1.14.0](https://github.com/coroot/coroot/releases/tag/v1.14.0)

Coroot v1.14.0 发布：社区版新增 AI 驱动的根因分析功能

本文宣布 Coroot v1.14.0 发布，重点介绍一项重要新功能：通过与 Coroot Cloud 集成，社区版新增了 AI 驱动的根因分析 (RCA) 功能。

用户现在可以利用 AI 自动调查事件并识别其根本原因。 Coroot 每月提供 10 个免费 RCA 积分，无需任何成本或信用卡即可对最多 10 个事件进行故障排除。

此次发布还包括其他几项更新和改进，例如 Coroot Operator 的文档增强、URL 编码的 API 改进、容器环境变量和 Postgres 兼容性的文档更新以及 SLO 覆盖中对 glob 模式的支持。

此次更新涉及 `def` 和 `apetruhin` 的贡献。 该公告还提到页面上加载资源时出错，并显示了反应次数。

---

## 65. 为什么人工智能还不能成为真正的程序员

**原文标题**: Why AI Isn't Ready to Be a Real Coder

**原文链接**: [https://spectrum.ieee.org/ai-for-coding](https://spectrum.ieee.org/ai-for-coding)

这篇AINews文章，Rina Diane Caballar于2025年8月26日发表的《为何AI尚未准备好成为真正的程序员》，探讨了人工智能在编码方面的局限性，尽管它取得了快速进展。文章认为，AI编码工具虽然有帮助，但尚未能取代人类程序员。文章认为，AI在编码领域的未来在于AI与人类程序员之间的协作。

关键在于，AI仍然难以处理复杂编码任务所需的高级推理、问题解决和细微的理解。虽然AI可以自动化重复性任务并生成代码片段，但它缺乏真正创新或复杂解决方案所需的创造力、批判性思维和上下文意识。

文章可能强调了对AI生成代码的信任的重要性。在AI生成的代码能够被完全信任之前，它需要易于理解和验证，这目前是一个挑战。作者可能认为，AI在编码方面的发展取决于构建高效且透明的系统，从而营造一个协作环境，让人类和AI可以共同努力，生成强大而可靠的软件。重点不是取代，而是增强和伙伴关系。

---

## 66. 美国情报

**原文标题**: US Intel

**原文链接**: [https://stratechery.com/2025/u-s-intel/](https://stratechery.com/2025/u-s-intel/)

本文辩称美国政府应持有英特尔的股权，反驳了认为此举是美国产业政策危险转变的批评。作者承认了斯科特·林西科姆等批评者强调的弊端，例如政治干预和资本错配，但认为这些批评缺乏“精钢化”——即对反方最有力论点的全面考虑。

核心论点围绕半导体制造业的地缘政治影响展开。作者强调了依赖位于中国附近的台积电和三星生产先进芯片的脆弱性，这些芯片对军事和民用技术（尤其是人工智能）至关重要。他们认为，英特尔的潜在失败将加剧这种依赖。

文章强调，英特尔目前的困境源于几十年前的决策，特别是错失了移动市场，导致缺乏支撑大规模资本支出的销量。作者认为，政府投资不仅仅是为了短期补救，更是为了确保美国在半导体制造业中的长期竞争力，从而反驳了市场“灵活性”是关键因素的观点。

最后，作者指出了英特尔在吸引外部客户使用其代工业务时面临的信誉问题。如果英特尔有可能放弃其制造工艺，客户会犹豫是否要承诺使用它。作者认为，政府所有权将提供必要的长期承诺保证，使英特尔成为台积电和三星的可行替代方案，并保障美国的国家安全和经济稳定。

---

## 67. 复数的整数连分数

**原文标题**: Integer continued fractions for complex numbers

**原文链接**: [https://arxiv.org/abs/2508.15078](https://arxiv.org/abs/2508.15078)

科马克·奥沙利文的arXiv文章 (arXiv:2508.15078)，题为“复数的整数连分数”，探讨了标准连分数到复数域的自然扩展。该论文重新审视并发展了归功于拉格朗日和高斯的一种算法，尽管其历史悠久，但作为生成连分数的方法，它在很大程度上被忽视了。

作者证明了所提出的表示是唯一的，并具有一些有益的特性。此外，该论文揭示了这些新的连分数表示的几何切割序列解释。

该文章对该主题进行了理论探索，为数论领域 (math.NT) 做出了贡献。它包含 21 页，有 10 个图。与此工作相关的MSC分类是 11Y65 (计算数论；连分数), 11F06 (模群和子群的结构；自守形式), 和 11H55 (代数数域上的二次型；格)。

---

## 68. Proposal to Ban Ghost Jobs

**原文标题**: Proposal to Ban Ghost Jobs

**原文链接**: [https://www.cnbc.com/2025/08/25/tech-worker-was-frustrated-with-ghost-jobs-now-hes-trying-to-pass-a-national-ban.html](https://www.cnbc.com/2025/08/25/tech-worker-was-frustrated-with-ghost-jobs-now-hes-trying-to-pass-a-national-ban.html)

生成摘要时出错

---

## 69. Show HN: Regolith – Regex library that prevents ReDoS CVEs in TypeScript

**原文标题**: Show HN: Regolith – Regex library that prevents ReDoS CVEs in TypeScript

**原文链接**: [https://github.com/JakeRoggenbuck/regolith](https://github.com/JakeRoggenbuck/regolith)

生成摘要时出错

---

## 70. Undisclosed financial conflicts of interest in DSM-5 (2024)

**原文标题**: Undisclosed financial conflicts of interest in DSM-5 (2024)

**原文链接**: [https://www.bmj.com/content/384/bmj-2023-076902](https://www.bmj.com/content/384/bmj-2023-076902)

生成摘要时出错

---

## 71. Framework Laptop 16

**原文标题**: Framework Laptop 16

**原文链接**: [https://frame.work/ro/en/laptop16?tab=whats-new](https://frame.work/ro/en/laptop16?tab=whats-new)

生成摘要时出错

---

## 72. Connecting M.2 drives to various things (and not doing so)

**原文标题**: Connecting M.2 drives to various things (and not doing so)

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/tech/M2ToVariousThings](https://utcc.utoronto.ca/~cks/space/blog/tech/M2ToVariousThings)

生成摘要时出错

---

## 73. The A.I. Spending Frenzy Is Propping Up the Real Economy, Too

**原文标题**: The A.I. Spending Frenzy Is Propping Up the Real Economy, Too

**原文链接**: [https://www.nytimes.com/2025/08/27/business/economy/ai-investment-economic-growth.html](https://www.nytimes.com/2025/08/27/business/economy/ai-investment-economic-growth.html)

生成摘要时出错

---

## 74. DSLRoot, proxies, and the threat of 'legal botnets'

**原文标题**: DSLRoot, proxies, and the threat of 'legal botnets'

**原文链接**: [https://krebsonsecurity.com/2025/08/dslroot-proxies-and-the-threat-of-legal-botnets/](https://krebsonsecurity.com/2025/08/dslroot-proxies-and-the-threat-of-legal-botnets/)

生成摘要时出错

---

## 75. Proposal: AI Content Disclosure Header

**原文标题**: Proposal: AI Content Disclosure Header

**原文链接**: [https://www.ietf.org/archive/id/draft-abaris-aicdh-00.html](https://www.ietf.org/archive/id/draft-abaris-aicdh-00.html)

生成摘要时出错

---

## 76. Uncomfortable Questions About Android Developer Verification

**原文标题**: Uncomfortable Questions About Android Developer Verification

**原文链接**: [https://commonsware.com/blog/2025/08/26/uncomfortable-questions-android-developer-verification.html](https://commonsware.com/blog/2025/08/26/uncomfortable-questions-android-developer-verification.html)

生成摘要时出错

---

## 77. System Initiative Adds AI Agents to Infrastructure Automation Platform

**原文标题**: System Initiative Adds AI Agents to Infrastructure Automation Platform

**原文链接**: [https://devops.com/system-initiative-adds-ai-agents-to-infrastructure-automation-platform/](https://devops.com/system-initiative-adds-ai-agents-to-infrastructure-automation-platform/)

生成摘要时出错

---

## 78. Show HN: Turn Markdown into React/Svelte/Vue UI at runtime, zero build step

**原文标题**: Show HN: Turn Markdown into React/Svelte/Vue UI at runtime, zero build step

**原文链接**: [https://markdown-ui.com/](https://markdown-ui.com/)

生成摘要时出错

---

## 79. The TTY Demystified (2008)

**原文标题**: The TTY Demystified (2008)

**原文链接**: [https://www.linusakesson.net/programming/tty/](https://www.linusakesson.net/programming/tty/)

生成摘要时出错

---

## 80. Show HN: I integrated my from-scratch TCP/IP stack into the xv6-riscv OS

**原文标题**: Show HN: I integrated my from-scratch TCP/IP stack into the xv6-riscv OS

**原文链接**: [https://github.com/pandax381/xv6-riscv-net](https://github.com/pandax381/xv6-riscv-net)

生成摘要时出错

---

## 81. Microsoft 'escort' program gave China keys to Pentagon

**原文标题**: Microsoft 'escort' program gave China keys to Pentagon

**原文链接**: [https://www.theblaze.com/return/microsoft-escort-program-gave-china-keys-to-pentagon](https://www.theblaze.com/return/microsoft-escort-program-gave-china-keys-to-pentagon)

生成摘要时出错

---

## 82. Das Problem mit German Strings

**原文标题**: Das Problem mit German Strings

**原文链接**: [https://www.polarsignals.com/blog/posts/2025/08/26/das-problem-mit-german-strings](https://www.polarsignals.com/blog/posts/2025/08/26/das-problem-mit-german-strings)

生成摘要时出错

---

## 83. The Relativity of Wrong (1988)

**原文标题**: The Relativity of Wrong (1988)

**原文链接**: [https://hermiene.net/essays-trans/relativity_of_wrong.html](https://hermiene.net/essays-trans/relativity_of_wrong.html)

生成摘要时出错

---

## 84. Deeper Than Deep: David Reich's genetics lab unveils our prehistoric past (2017)

**原文标题**: Deeper Than Deep: David Reich's genetics lab unveils our prehistoric past (2017)

**原文链接**: [https://www.laphamsquarterly.org/roundtable/deeper-deep](https://www.laphamsquarterly.org/roundtable/deeper-deep)

生成摘要时出错

---

## 85. How to store weather forecast data for fast time-series APIs (2022)

**原文标题**: How to store weather forecast data for fast time-series APIs (2022)

**原文链接**: [https://openmeteo.substack.com/p/how-to-store-weather-forecast-data](https://openmeteo.substack.com/p/how-to-store-weather-forecast-data)

生成摘要时出错

---

## 86. Cornell's world-first 'microwave brain' computes differently

**原文标题**: Cornell's world-first 'microwave brain' computes differently

**原文链接**: [https://newatlas.com/computers/cornell-microwave-brain/](https://newatlas.com/computers/cornell-microwave-brain/)

生成摘要时出错

---

## 87. Culinary arts and Computer Science (2019) [pdf]

**原文标题**: Culinary arts and Computer Science (2019) [pdf]

**原文链接**: [https://www-cs-faculty.stanford.edu/~knuth/papers/food-and-cs.pdf](https://www-cs-faculty.stanford.edu/~knuth/papers/food-and-cs.pdf)

生成摘要时出错

---

## 88. Show HN: Diggit.dev – Git history for architecture archaeologists

**原文标题**: Show HN: Diggit.dev – Git history for architecture archaeologists

**原文链接**: [https://diggit.dev](https://diggit.dev)

生成摘要时出错

---

## 89. Show HN: Smooth – Faster, cheaper browser agent API

**原文标题**: Show HN: Smooth – Faster, cheaper browser agent API

**原文链接**: [https://www.smooth.sh/](https://www.smooth.sh/)

生成摘要时出错

---

## 90. 'Ten Martini' Proof Uses Number Theory to Explain Quantum Fractals

**原文标题**: 'Ten Martini' Proof Uses Number Theory to Explain Quantum Fractals

**原文链接**: [https://www.quantamagazine.org/ten-martini-proof-uses-number-theory-to-explain-quantum-fractals-20250825/](https://www.quantamagazine.org/ten-martini-proof-uses-number-theory-to-explain-quantum-fractals-20250825/)

生成摘要时出错

---

## 91. Eyecam

**原文标题**: Eyecam

**原文链接**: [https://marcteyssier.com/projects/eyecam/](https://marcteyssier.com/projects/eyecam/)

生成摘要时出错

---

## 92. Google will allow only apps from verified developers to be installed on Android

**原文标题**: Google will allow only apps from verified developers to be installed on Android

**原文链接**: [https://9to5google.com/2025/08/25/android-apps-developer-verification/](https://9to5google.com/2025/08/25/android-apps-developer-verification/)

生成摘要时出错

---

## 93. 'Suicide coach': Parents sue OpenAI for ChatGPT's role in son's death

**原文标题**: 'Suicide coach': Parents sue OpenAI for ChatGPT's role in son's death

**原文链接**: [https://www.courthousenews.com/suicide-coach-parents-sue-openai-for-chatgpts-role-in-sons-death/](https://www.courthousenews.com/suicide-coach-parents-sue-openai-for-chatgpts-role-in-sons-death/)

生成摘要时出错

---

## 94. All the world’s polygons

**原文标题**: All the world’s polygons

**原文链接**: [https://www.sum.si/journal-articles/all-the-worlds-polygons](https://www.sum.si/journal-articles/all-the-worlds-polygons)

生成摘要时出错

---

## 95. Scientist exposes anti-wind groups as oil-funded, now they want to silence him

**原文标题**: Scientist exposes anti-wind groups as oil-funded, now they want to silence him

**原文链接**: [https://electrek.co/2025/08/25/scientist-exposes-anti-wind-groups-as-oil-funded-now-they-want-to-silence-him/](https://electrek.co/2025/08/25/scientist-exposes-anti-wind-groups-as-oil-funded-now-they-want-to-silence-him/)

生成摘要时出错

---

## 96. The Annotated Transformer (2022)

**原文标题**: The Annotated Transformer (2022)

**原文链接**: [https://nlp.seas.harvard.edu/annotated-transformer/](https://nlp.seas.harvard.edu/annotated-transformer/)

生成摘要时出错

---

## 97. A bug saved the company

**原文标题**: A bug saved the company

**原文链接**: [https://weblog.rogueamoeba.com/2025/08/21/when-a-bug-saved-the-company/](https://weblog.rogueamoeba.com/2025/08/21/when-a-bug-saved-the-company/)

生成摘要时出错

---

## 98. Show HN: Sideko – Hybrid deterministic/LLM generator for API SDKs and docs

**原文标题**: Show HN: Sideko – Hybrid deterministic/LLM generator for API SDKs and docs

**原文链接**: [https://github.com/Sideko-Inc/sideko/tree/main/releases/determinism-plus-llms](https://github.com/Sideko-Inc/sideko/tree/main/releases/determinism-plus-llms)

生成摘要时出错

---

## 99. The Leverage Paradox in AI

**原文标题**: The Leverage Paradox in AI

**原文链接**: [https://www.indiehackers.com/post/lifestyle/the-leverage-paradox-ksRiX6y6W7NzfBE57dzt](https://www.indiehackers.com/post/lifestyle/the-leverage-paradox-ksRiX6y6W7NzfBE57dzt)

生成摘要时出错

---

## 100. Show HN: Gonzo – A Go-based TUI for log analysis (OpenTelemetry/OTLP support)

**原文标题**: Show HN: Gonzo – A Go-based TUI for log analysis (OpenTelemetry/OTLP support)

**原文链接**: [https://github.com/control-theory/gonzo](https://github.com/control-theory/gonzo)

生成摘要时出错

---

