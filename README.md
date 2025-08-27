# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-27.md)

*最后自动更新时间: 2025-08-27 17:47:27*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 2 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 3 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 4 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 5 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 6 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 7 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 8 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 9 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 10 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 11 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 12 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 13 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 14 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 15 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 16 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 17 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 18 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 19 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 20 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 21 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 22 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 23 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 24 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 25 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 26 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 27 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 28 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 29 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 30 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 31 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 32 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 33 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 34 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 35 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 36 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 37 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 38 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 39 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 40 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 41 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 42 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 43 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 44 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 45 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 46 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 47 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 48 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 49 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 50 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 51 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 52 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 53 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 54 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 55 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 56 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 57 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 58 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 59 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 60 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 61 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 62 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 63 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 64 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 65 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 66 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 67 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 68 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 69 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 70 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 71 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 72 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 73 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 74 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 75 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 76 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 77 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 78 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 79 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 80 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 81 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 82 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 83 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 84 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 85 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 86 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 87 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 88 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 89 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 90 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 91 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 92 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 93 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 94 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 95 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 96 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 97 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 98 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 99 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 100 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 101 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 102 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 103 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 104 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 105 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 106 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 107 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 108 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 109 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 110 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 111 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 112 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 113 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 114 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 115 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 116 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 117 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 118 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 119 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 120 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 121 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 122 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 123 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 124 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 125 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 126 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 127 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 128 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 129 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 130 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 131 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 132 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 133 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 134 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 135 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 136 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 137 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 138 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 139 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 140 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 141 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 142 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 143 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 144 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 145 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 146 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 147 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 148 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 149 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 150 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 151 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 152 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 153 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 154 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 155 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 156 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 157 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 158 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 159 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 160 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 161 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
