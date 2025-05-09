# Hacker News 热门文章摘要 (2025-05-09)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. ALICE探测到大型强子对撞机中铅转化为金

**原文标题**: ALICE detects the conversion of lead into gold at the LHC

**原文链接**: [https://www.home.cern/news/news/physics/alice-detects-conversion-lead-gold-lhc](https://www.home.cern/news/news/physics/alice-detects-conversion-lead-gold-lhc)

CERN大型强子对撞机ALICE实验组报告称，通过一种新颖的机制实现了铅到金的人工嬗变：高能铅核的近失碰撞。与传统的中子或质子轰击方法不同，这一过程依赖于围绕铅核的强烈电磁场。这些电磁场产生光子，与原子核相互作用，导致它们喷射出质子和中子。具体来说，去除三个质子可以将铅（82个质子）转化为金（79个质子）。

这个过程被称为电磁解离，利用了大型强子对撞机的超外围碰撞，在这种碰撞中，铅核在近距离通过而不直接碰撞。虽然夸克-胶子等离子体的产生需要正面碰撞，但这些近失相互作用提供了独特的探索机会。ALICE的探测器，特别是零度量热器（ZDC），灵敏到足以量化这一过程中各种元素的产生。

实验发现，在铅-铅碰撞期间，在ALICE碰撞点，金的产生速率约为每秒89,000个原子核。然而，产生的金原子核是短寿命的，很快会分裂成其他粒子。在大型强子对撞机的Run 2（2015-2018）期间，大约产生了860亿个金原子核，相当于仅仅29皮克。虽然Run 3由于光度的增加使这一数量几乎翻了一番，但仍然远远不能产生可用量的黄金。

尽管未能实现炼金术士的财富梦想，但这项研究为电磁解离提供了宝贵的见解，并改进了用于预测大型强子对撞机和未来对撞机中束流损失的理论模型。由于ALICE ZDC的功能，大型强子对撞机首次对金的产生进行了系统检测和分析的实验。

---

## 2. Sorbet类型语法的过去、现在和未来

**原文标题**: Past, Present, and Future of Sorbet Type Syntax

**原文链接**: [https://blog.jez.io/history-of-sorbet-syntax/](https://blog.jez.io/history-of-sorbet-syntax/)

本文深入探讨了Sorbet类型语法的历史、原理和潜在未来。作者Jake在Sorbet工作了七年，他解释说，Sorbet的出现源于Stripe内部对静态类型检查的明确需求，以解决其大型Ruby代码库中的代码组织和模块化挑战。

最初，Stripe工程师使用Ruby DSL进行运行时类型检查和显式接口。从头开始构建Sorbet的决定是由于现有Ruby类型检查器的局限性以及用类型化语言重写整个代码库的不切实际。

本文探讨了考虑过的潜在语法设计方法，强调了Ruby生态系统的约束，这使得打破与现有工具和实践的兼容性不受鼓励。 考虑了三个主要选项：TypeScript方法（由于缺乏工具支持而被拒绝），头文件方法（被认为不完整，因为它不支持方法内类型），以及JSDoc方法（由于最初关注运行时类型检查以及避免Hyrum定律等相关好处而被排除）。

作者最后暗示了Sorbet语法未来可能的变化，并呼吁对语法感兴趣的开发者为项目的演进做出贡献。

---

## 3. Sofie：用于自动化直播电视新闻制作的开源网络系统

**原文标题**: Sofie: open-source web based system for automating live TV news production

**原文链接**: [https://nrkno.github.io/sofie-core/](https://nrkno.github.io/sofie-core/)

Sofie：开源的、基于网络的直播电视新闻自动化制作系统。文档按用户类型划分。用户指南提供关于Sofie系统功能、安装和操作的通用信息。开发者文档专注于代码库的开发和贡献。另有关于Sofie系统当前、过往和未来发布的信息。文档鼓励用户加入Sofie社区Slack频道，与开发者和其他用户交流。总而言之，Sofie提供了一个全面的、有文档支持的直播电视新闻自动化平台，并由一个活跃的社区提供支持。

---

## 4. AMD 9950X 上使用 SIMD 的 21 GB/s CSV 解析

**原文标题**: 21 GB/s CSV Parsing Using SIMD on AMD 9950X

**原文链接**: [https://nietras.com/2025/05/09/sep-0-10-0/](https://nietras.com/2025/05/09/sep-0-10-0/)

本文详细介绍了 Sep CSV 解析库所取得的性能提升，最终在使用 SIMD 优化的 AMD 9950X (Zen 5) CPU 上实现了惊人的 21 GB/s 解析速度。作者重点介绍了 Sep 的性能从 0.1.0 版本到 0.10.0 版本的演变，展示了代码更改、新版 .NET 以及从 AMD Ryzen 9 5950X (Zen 3) 到 9950X 的硬件升级所带来的改进。

重点关注解决 .NET 中次优的 AVX-512 代码生成问题，特别是关于掩码寄存器的使用。最初，在 9950X 上，AVX-512 解析器比 AVX2 解析器更慢。通过将 MoveMask 调用提前到代码中，作者减少了在掩码寄存器和普通寄存器之间传输数据的开销，从而显著提高了性能。

作者随后引入了一种新的“AVX-512-to-256”解析器，该解析器利用 AVX-512 指令进行数据加载，但使用 `ConvertToVector256ByteWithSaturation` 将数据转换为 256 位寄存器，从而有效地绕过了效率低下的 AVX-512 掩码寄存器。这种方法被证明是最快的，实现了 21 GB/s 的解析速度。本文包括代码片段和汇编比较，以说明 .NET 中与 AVX-512 代码生成相关的改进和挑战。

---

## 5. Show HN: BlenderQ – 用于管理多个Blender渲染的TUI

**原文标题**: Show HN: BlenderQ – A TUI for managing multiple Blender renders

**原文链接**: [https://github.com/KyleTryon/BlenderQ](https://github.com/KyleTryon/BlenderQ)

BlenderQ：一个命令行工具，让用户可以直接从终端管理和监控Blender渲染队列。它使用Node.js编写并基于Ink构建，提供了一个TUI（终端用户界面），用于将多个.blend文件添加到渲染队列、跟踪进度并管理渲染过程。

BlenderQ目前处于beta阶段，提供交互式导航、状态跟踪和主题支持等功能。要使用它，用户需要Node.js (v20+)、Blender (v3.5+)，以及可选的Nerd Fonts图标。可以通过npm或pnpm进行全局安装。

用户可以使用 `--blend` 标志后跟文件路径，将特定的.blend文件添加到队列中，或者使用 `--dir` 标志在指定目录中浏览.blend文件。

作者选择Node.js是因为其快速开发能力和现成的TUI组件（如Ink），尽管曾考虑过Python和Go。未来的开发可能会探索使用Python进行更深入的Blender集成。

---

## 6. Rollstack (YC W23) 正在招聘 TypeScript 工程师（美国/加拿大远程）

**原文标题**: Rollstack (YC W23) Is Hiring TypeScript Engineers (Remote US/CA)

**原文链接**: [https://www.ycombinator.com/companies/rollstack-2/jobs/QPqpb1n-software-engineer-typescript-us-canada](https://www.ycombinator.com/companies/rollstack-2/jobs/QPqpb1n-software-engineer-typescript-us-canada)

Rollstack，一家由 Y Combinator (W23) 支持的公司，通过报告自动化革新数据呈现方式，现正招聘软件工程师（TypeScript）。他们将 BI 工具连接到幻灯片和文档，为 SoFi、1Password 和 Zillow 等公司自动化创建和更新过程。

该职位包括构建面向用户的新功能、优化数据同步、集成 BI 和内容平台（Tableau、Looker、Google Slides 等）以及定义整个技术栈的最佳实践。技术栈包括 TypeScript、React、Node.js、Prisma ORM、Temporal 工作流、OpenAI API 和基于 AWS 的 K8s。

Rollstack 提供远程友好的工作场所，拥有全球化和包容性的文化，提供半年一次的团队聚会、丰厚的薪酬和股权参与。理想的候选人拥有 2-6 年的经验，包括 2 年 TypeScript、Node.js/ORM 和 React 的经验，以及对软件工程基础、CI/CD 和云基础设施的扎实理解。

面试流程包括两次技术面试（编码练习和技术问题）和两次与联合创始人的匹配度面试。Rollstack 寻求迭代、快速交付、解决客户问题并展现强烈主人翁意识的工程师。

---

## 7. Show HN: 用于构建响应式桌面应用的后端无关Ruby框架

**原文标题**: Show HN: A backend agnostic Ruby framework for building reactive desktop apps

**原文链接**: [https://codeberg.org/skinnyjames/hokusai](https://codeberg.org/skinnyjames/hokusai)

无法访问文章链接。

---

## 8. Show HN: Aberdeen – 一种优雅的响应式UI方案

**原文标题**: Show HN: Aberdeen – An elegant approach to reactive UIs

**原文链接**: [https://aberdeenjs.org/](https://aberdeenjs.org/)

Aberdeen v1.0.1 是一个新的 JavaScript/TypeScript 库，用于构建反应式 UI，无需虚拟 DOM。 它使用小型匿名函数来生成 DOM 元素，并在其底层代理数据发生更改时自动重新运行它们。

**主要特性和优势：**

*   **简单优雅：** 使用原生 JS/TS，避免了复杂的抽象、构建步骤、JSX 或状态管理库。
*   **快速：** 通过利用代理数据更改，仅更新 UI 的必要部分。
*   **列表优化：** 提供反应式数据列表的高性能渲染和操作。
*   **体积小巧：** 仅 5KB（压缩和 gzip 后），无运行时依赖。
*   **功能齐全：** 提供客户端路由、乐观 UI 更新、组件局部 CSS 和数据转换辅助函数。

**局限性：**

*   **社区较小：** 社区支持有限，可用资源较少。
*   **生态不足：** 需要更多手动编码，而不是利用已建立的 React 生态系统库。

该库提供了井字游戏应用、输入字段、列表和路由等示例。 学习资源包括教程和参考文档。 1.0.1 版本标志着该库的 API 已稳定，并包含交互式文档。

---

## 9. Itter.sh – 终端上的微型博客

**原文标题**: Itter.sh – Micro-Blogging via Terminal

**原文链接**: [https://www.itter.sh/](https://www.itter.sh/)

Itter.sh：一款仅通过 SSH 终端访问的微型博客平台。它提供了一种极简的社交媒体替代方案，摒弃了网页浏览器、JavaScript 和算法推荐，以基于文本的体验和 180 字符的限制（“eets”）为特色。

新用户通过 SSH 使用 `register:` 前缀加上期望的用户名进行注册。注册和登录都需要 SSH 密钥。注册后，用户使用 `ssh YOUR_USERNAME@app.itter.sh` 登录。

该平台提供命令行界面用于发布 eets (`ittereet`)、查看时间线 (`ittertimeline`, `itterwatch` - 用于实时更新)、关注/取消关注用户 (`itterfollow`, `itterunfollow`)、查看和编辑个人资料 (`itterprofile`)、清除屏幕 (`itterclear`) 和退出应用程序 (`itterexit`)。Eets 支持标签和提及。

Itter.sh 基于 Python、AsyncSSH、Supabase 构建，并专注于“终端怀旧”。

---

## 10. 前最高法院大法官戴维·苏特去世

**原文标题**: Former Supreme Court justice David Souter has died

**原文链接**: [https://www.npr.org/2025/05/09/g-s1-65326/justice-david-souter-dies](https://www.npr.org/2025/05/09/g-s1-65326/justice-david-souter-dies)

前最高法院大法官戴维·苏特在新罕布什尔州的家中去世，享年85岁。苏特于1990年由乔治·H·W·布什总统任命，尽管人们期望他成为一位保守派大法官，但他与最高法院中较为自由派的阵营保持一致，令许多共和党人感到惊讶。

首席大法官约翰·罗伯茨赞扬了苏特的“非凡智慧和善良”。苏特在69岁时退休，表达了离开华盛顿并返回他的故乡新罕布什尔州的愿望，他一直不喜欢这座城市。

苏特毕业于哈佛学院、哈佛法学院和牛津大学莫德林学院，他在被任命后打破了人们的意识形态期望。他加入了最高法院的温和派，后来成为自由派核心小组的一员。他的转变让包括白宫办公厅主任约翰·苏努努在内的人感到惊讶，苏努努曾认为他是一位保守派的新罕布什尔州最高法院大法官。

苏特以其独立性而闻名，他经常返回新罕布什尔州，更喜欢开车而不是坐飞机。他还避开了手机和电子邮件等现代科技，用钢笔手写他的意见。作为一名终身单身汉，苏特在华盛顿过着简朴的生活，远离城市的社交场所，始终渴望着他在新罕布什尔州乡村的家。

---

## 11. Show HN: 奥利芬特 – macOS 平台的原生 Mastodon 客户端

**原文标题**: Show HN: Oliphaunt – A native Mastodon client for macOS

**原文链接**: [https://testflight.apple.com/join/Epq1P3Cw](https://testflight.apple.com/join/Epq1P3Cw)

本文档提供了关于使用 TestFlight 在 Apple 平台（iOS、iPadOS、macOS、tvOS、visionOS 和 watchOS）上进行应用 beta 测试的全面指南。它涵盖了从接受邀请和安装 TestFlight 到安装 beta 应用、管理更新以及测试特定应用功能（如 iMessage 扩展和 App Clips）的所有内容。

要点包括：

*   **接受邀请：** 用户可以通过电子邮件或公共链接接受 beta 测试邀请。
*   **安装：** 需要在目标设备上安装 TestFlight 并接受邀请。 Beta 应用最多可安装在 30 台设备上。
*   **系统

总而言之，本文是成为 TestFlight 用户并在 Apple 设备上有效测试 beta 应用的完整指南。

---

## 12. Show HN: Hydra (YC W22) – 基于 Postgres 的 Serverless 分析

**原文标题**: Show HN: Hydra (YC W22) – Serverless Analytics on Postgres

**原文链接**: [https://www.hydra.so/](https://www.hydra.so/)

Hydra：基于Postgres的无服务器分析平台

---

## 13. LegoGPT：生成物理稳定且可建造的乐高

**原文标题**: LegoGPT: Generating Physically Stable and Buildable Lego

**原文链接**: [https://avalovelace1.github.io/LegoGPT/](https://avalovelace1.github.io/LegoGPT/)

LegoGPT 是一种新颖方法，可以直接从文本提示生成物理上稳定且可建造的乐高模型。LegoGPT 的核心是一个自回归大型语言模型 (LLM)，它在一个新创建的大规模数据集 StableText2Lego 上进行了微调，该数据集包含超过 47,000 个乐高结构及其相关标题。该数据集通过从 3D 形状生成乐高设计，引入结构变化，过滤物理稳定性，然后使用 GPT-4o 生成描述性标题来构建。

LegoGPT 流程将乐高设计标记化为文本标记序列，并使用 LLaMA-3.2-Instruct-1B 根据文本提示预测下一个砖块。为了确保生成的模型稳定且可建造，该系统在推理过程中执行多项有效性检查：它验证砖块格式、库中砖块的存在以及避碰。此外，一种具有物理感知的回滚机制通过移除不稳定的砖块及其后续组件来检测和纠正不稳定的结构，然后从上一个稳定状态恢复生成。

生成的乐高模型与提供的文本提示高度一致，可以手动或通过机械臂进行组装。该方法还可以扩展到生成纹理化和着色的乐高设计。作者公开提供了他们的数据集、代码和模型。

---

## 14. 研究指控数据操控为微软量子芯片铺平道路

**原文标题**: Data manipulations alleged in study that paved way for Microsoft's quantum chip

**原文链接**: [https://www.science.org/content/article/data-manipulations-alleged-study-paved-way-microsoft-s-quantum-chip](https://www.science.org/content/article/data-manipulations-alleged-study-paved-way-microsoft-s-quantum-chip)

无法访问文章链接。

---

## 15. Show HN: Hyvector – 一款快速且现代的SVG编辑器

**原文标题**: Show HN: Hyvector – A fast and modern SVG editor

**原文链接**: [https://www.hyvector.com](https://www.hyvector.com)

这篇文章是一个“Show HN”帖子，介绍了Hyvector，一个自称“快速且现代的SVG编辑器”。然而，提供的内容仅包含一条消息，说明Hyvector需要JavaScript才能运行，因此在未启用JavaScript的情况下无法访问。这表明发布者正在展示一个用JavaScript构建的基于Web的SVG编辑器。该消息暗示用户需要在浏览器中启用JavaScript才能正确体验和交互Hyvector编辑器。因此，在无法访问该应用程序的情况下，除了其声称的快速和现代之外，无法了解其功能、能力或优势。核心信息仅仅是Hyvector的发布公告以及启用JavaScript才能使用的提示。

---

## 16. 解构建筑小组

**原文标题**: The Anarchitecture Group

**原文链接**: [https://www.spatialagency.net/database/the.anarchitecture.group](https://www.spatialagency.net/database/the.anarchitecture.group)

无建筑小组，1972年至1975年活跃于纽约，是一个艺术家团体，成员包括劳里·安德森、蒂娜·吉鲁阿尔和受过建筑训练的艺术家戈登·马塔-克拉克。该小组的名字融合了“无政府状态”和“建筑”，反映了他们对现代主义建筑的批判，他们认为现代主义建筑是文化停滞和资本主义过度扩张的象征。

他们1974年的展览“无建筑”匿名地展示了通过建筑视角批判当代文化的作品。他们探讨了建筑在资本主义生产中的共谋，通过文字游戏和发现的摄影作品探索了与城市、居住和财产相关的问题。

马塔-克拉克的“虚假地产”项目，购买微小的、无法建造的地块，讽刺了美国人对土地所有权的梦想。他的“食物”餐厅项目，虽然是独立的，但涉及了许多相同的人，并培育了一个当地的艺术家网络，创造了一个社会和经济中心。

马塔-克拉克后来的“建筑切割”，通过切割和重组改造了废弃的建筑物，进一步发展了该小组的主题，通过解构的建筑评论了社会对物质财富和永恒的渴望。因此，该小组的作品始终挑战着建筑结构的可见坚固性和社会意义。

---

## 17. CryptPad：谷歌套件的替代方案

**原文标题**: CryptPad: An Alternative to the Google Suite

**原文链接**: [https://cryptpad.org/](https://cryptpad.org/)

CryptPad被定位为注重隐私、开源的谷歌办公套件替代品。它强调协作、实时编辑和端到端加密，提供全套应用程序，同时优先考虑用户隐私。

文章重点介绍了来自不同用户的评价，他们称赞CryptPad的易用性、数据安全性以及无需收件人创建帐户即可共享文件的能力。用户欣赏其简洁的界面、匿名工作的能力以及缺乏数据跟踪。许多人认为它是主流选项的可靠替代品，尤其是在协作写作、项目管理（使用看板）和安全文件存储方面。

反复受到称赞的具体功能包括其隐私政策、密码学、共享选项和跨设备兼容性。一些用户注意到它在个人和专业用途方面的价值，尤其是在敏感文档和协作项目方面。它是免费的、开源的并且托管在欧盟的事实也被经常提到。一些用户很高兴Cryptpad现在是他们的Google Drive替代品。最终，CryptPad被描绘成一个可靠且符合道德规范的解决方案，适合那些寻求安全且用户友好的在线办公套件的人。

---

## 18. 人工智能扑克的诞生？来自1984年WSOP的信件

**原文标题**: The birth of AI poker? Letters from the 1984 WSOP

**原文链接**: [https://www.poker.org/latest-news/the-birth-of-ai-poker-letters-from-the-1984-wsop-a4v2W4N4X3EP/](https://www.poker.org/latest-news/the-birth-of-ai-poker-letters-from-the-1984-wsop-a4v2W4N4X3EP/)

文章《人工智能扑克的诞生？来自1984年WSOP的信件》围绕着扑克理论家和策略家迈克·卡罗写给亨利·博林格的一张未注明日期的便条展开，这张便条很可能写于1984年世界扑克大赛（WSOP）期间。虽然文章没有透露便条的具体内容，但其标题和背景暗示了对人工智能在扑克策略和决策中潜力的讨论。

标题提出卡罗的便条可能代表着对将计算逻辑，甚至可能是人工智能概念应用于扑克游戏的早期思考。其意义在于历史时机。1984年是计算机技术取得重大进展的时期，使得像卡罗这样的先驱者已经开始考虑使用计算机来分析和改进扑克游戏的可能性成为可能。

因此，这篇文章可能探讨了新兴的人工智能领域与扑克复杂战略格局之间的历史联系，并将该便条作为早期探索这一交叉点的潜在证据。由于便条本身缺乏具体细节，因此需要根据标题和相关人物所提供的隐含背景进行解读。

---

## 19. 展示HN: Agents.erl (Erlang中的AI智能体)

**原文标题**: Show HN: Agents.erl (AI Agents in Erlang)

**原文链接**: [https://github.com/arthurcolle/agents.erl](https://github.com/arthurcolle/agents.erl)

Agents.erl 是一个 Erlang 框架，用于与 OpenAI API 集成。它提供了一种分布式架构，其中每个 API 端点都作为一个受监控的进程运行，从而确保容错性和稳定性。该框架从 OpenAI API 规范动态生成 API 客户端模块，涵盖所有端点，例如聊天、补全和嵌入。

主要功能包括内置的监督树、自动速率限制以防止配额问题以及对流式响应的支持。它允许用户注册和执行自定义工具，从而扩展代理的功能。配置是集中式的，并使用环境变量回退以便于设置。

该架构组织为一个分层监督树，管理 OpenAI API 客户端、速率限制、配置、工具注册表和活动代理进程。

使用方法包括启动代理应用程序，使用简单的 `agent:run_agent` 函数运行带有预定义或自定义工具的代理，以及使用模式和执行器函数定义自定义工具。直接 API 访问也受支持，方法是确保特定 API 客户端的可用性，然后调用其函数，例如 `openai_chat:create_chat_completion`。

该框架使用 `OPENAI_API_KEY` 和 `OPENAI_ORGANIZATION` 环境变量进行身份验证，并且可以使用标准的 Erlang 编译命令轻松构建。它在 MIT 许可下获得许可。

---

## 20. 美国国家科学基金会面临改革，官员们废除了其37个部门

**原文标题**: NSF faces shake-up as officials abolish its 37 divisions

**原文链接**: [https://www.science.org/content/article/exclusive-nsf-faces-radical-shake-officials-abolish-its-37-divisions](https://www.science.org/content/article/exclusive-nsf-faces-radical-shake-officials-abolish-its-37-divisions)

无法访问文章链接。

---

## 21. 实现结构体数组

**原文标题**: Implementing a Struct of Arrays

**原文链接**: [https://brevzin.github.io/c++/2025/05/02/soa/](https://brevzin.github.io/c++/2025/05/02/soa/)

本文演示了如何在 C++26 中使用反射实现“数组结构体”（SoA）数据结构，模仿 Zig 编程语言中的一项特性。SoA 不是将数据存储为结构体数组（AoS），而是将每个结构体成员存储在单独的数组中，从而可能提高内存使用率和性能。

本文重点介绍如何创建 `SoaVector<T>` 模板，其中 `T` 表示结构体类型（例如，`Point {char x; int y;}`）。它利用 C++26 的反射特性，特别是 `std::meta::define_aggregate`，来动态生成存储结构。这会为 `T` 的每个非静态数据成员动态创建指针（例如，`char* x; int* y;`），以及一个共享的大小和容量。

然后，本文详细介绍了 `push_back`、`grow`（用于动态调整大小）和析构函数的实现，以便正确管理内存。它强调了使用 `std::define_static_array` 来解决 C++26 在非瞬态分配方面的限制。

此外，它还实现了索引运算符 (`operator[]`)。 const 版本返回 `Point` 对象的副本。 可变版本更有趣，它返回 `PointRef` 类型，这是一种生成的结构体，包含对 SoA 结构体中各个数据成员的引用（例如，`char& x; int& y;`）。 这允许通过 `PointRef` 进行的修改直接更新底层 SoA 存储。 最后，它使用注解来增强调试和格式化，使 `SoaVector` 更加用户友好。 为了调试目的，定义了到 `Point` 的转换。

---

## 22. 渲染引擎分类法

**原文标题**: A Taxonomy for Rendering Engines

**原文链接**: [https://c0de517e.com/021_taxonomy.htm](https://c0de517e.com/021_taxonomy.htm)

本文倡导一种更结构化的渲染引擎设计讨论方式，超越单纯的特性展示，提供评估设计选择所需的背景信息。作者认为，实时渲染行业虽然创新不断，但往往缺乏对基础架构决策的“不那么光鲜”的讨论。为了解决这个问题，他们建议开发一套渲染引擎的分类方法，类似于数据库的分类方式（关系型、键值型等）。

作者提出了一个初步的 3x3 分类法，包括：

1.  **产品特性：** 引擎用户（从专有到 UGC 平台）、平台支持（单模态到多模态）以及可扩展性需求（内容缩放）。
2.  **生产：** 内容抽象（API 驱动 vs. 数据驱动）、迭代工作流（实时编辑 vs. 烘焙）以及目标用户（艺术家 vs. 工程师）。
3.  **技术

作者还将“成功（或规模）”确定为一个关键维度，强调用户群和团队规模如何影响算法选择和代码结构。

核心信息并非要僵化地采用这种特定的分类方法，而是鼓励在讨论渲染引擎架构时进行周到的背景信息呈现。通过理解产品特性、生产工作流程和技术要求，关于线程模型、API 抽象和数据结构的讨论将变得更有意义和相关性。随着行业成熟并专注于高效地覆盖更广泛的受众，一种用于描述这些基本方面的通用语言变得越来越重要。

---

## 23. 通过技能树构建基于能力的课程

**原文标题**: Structuring Competency-Based Courses Through Skill Trees

**原文链接**: [https://arxiv.org/abs/2504.16966](https://arxiv.org/abs/2504.16966)

本文《通过技能树构建基于能力的课程》（作者：Hildo Bijl）探讨了计算机科学教育中改进课程结构的需求，尤其是在基于能力的教学和日益增长的自动化背景下。作者认为，现有的结构化方法侧重于理论，未能充分模拟技能之间的依赖关系，而这对于有效的基于能力的教育和自动化辅导至关重要。

本文介绍了一种名为“技能树”的新框架，旨在围绕学生需要掌握的技能来构建教学内容。这些技能树以可视化的方式表示不同技能之间的依赖关系。然后，该框架将这些技能树与概念树相结合，概念树描绘了与每个技能相关的直观想法或“概念机器”。由于计算机科学的算法特性，这种循序渐进的方法尤其适用。

本文包括技能树和概念树的正式定义，以及如何设计它们并利用它们来规划课程的指南。

“技能树”框架被用于改进一门大学数据库课程。实施后的学生访谈显示出积极的结果，包括减少了困惑和压力，以及达到所需技能水平所需的学习时间减少。

该论文已提交至Koli Calling '25发表，并侧重于计算机科学中的“计算机与社会”主题。

---

## 24. 亚马逊的Vulcan机器人现在存储物品比人类更快

**原文标题**: Amazon's Vulcan Robots Now Stow Items Faster Than Humans

**原文链接**: [https://spectrum.ieee.org/amazon-stowing-robots](https://spectrum.ieee.org/amazon-stowing-robots)

亚马逊“Vulcan”机器人仓库存货速度超越人类

---

## 25. Linux内核的PGP信任网络

**原文标题**: The Linux Kernel's PGP Web of Trust

**原文链接**: [https://blog.kleine-koenig.org/ukl/the-linux-kernels-pgp-web-of-trust.html](https://blog.kleine-koenig.org/ukl/the-linux-kernels-pgp-web-of-trust.html)

Linux内核开发依赖PGP进行安全通信，特别是使用拉取请求中的签名标签。Konstantin Ryabitsev维护着一个git仓库(korg-pgpkeys)，其中包含内核开发者使用的有效PGP密钥。如果密钥与Linus Torvalds的密钥之间有5或更少的信任路径，则会添加密钥。

GnuPG 2.4.x拒绝被认为不安全的SHA-1签名，这带来了一个潜在的问题。虽然内核的信任路径检查工具目前接受SHA-1，但当密钥更新时，GnuPG的“清理”可能会删除这些签名，正如Theodore Ts'o的密钥所发生的那样。

文章揭示了korg-pgpkeys仓库中很大一部分密钥签名（7976个中的6045个）使用SHA-1。如果删除SHA-1签名，将有485个密钥会失去来自Linus Torvalds的信任路径，并且不符合该仓库的资格。这将影响像Andrew Morton、Greg Kroah-Hartman等著名的内核开发者。内核强集将急剧缩小。

作者和Ahmad Fatoum正在Embedded Recipes 2025上组织一次密钥签名活动，以改善这种情况，并鼓励开发者创建新的、SHA-256签名的信任路径。感兴趣的参与者请在UTC时间2025-05-12 08:00之前提交他们的公钥。

---

## 26. CL1：首个可部署的生物计算机

**原文标题**: The CL1: the first code deployable biological computer

**原文链接**: [https://corticallabs.com/cl1.html](https://corticallabs.com/cl1.html)

Cortical Labs CL1：一款突破性的可代码部署的生物计算机，将硅技术与活神经元融合。这些神经元在富含营养的溶液中培养，生长在发送和接收电脉冲的硅芯片上。生物智能操作系统 (biOS) 模拟神经元的环境，允许用户与它们互动并影响它们的模拟世界。

CL1 允许直接连接和代码部署到这些真实神经元，通过利用生物神经网络的自编程和适应性，提供了一种解决复杂问题的独特方法。这是一个闭环系统，软件和真实神经元实时互动，维持长达六个月的稳定环境。

功能包括：自给自足（所有记录、应用和生命支持都在设备上）、与各种设备的即插即用兼容性、可编程的双向刺激、触摸屏界面以及高可扩展性。CL1 提倡无动物测试，为医学和研究实验室提供了一种更合乎伦理且更相关的替代传统动物研究的方案。通过清晰地研究大脑功能，它可以实现更深入的学习，揭示疾病机制和化合物对认知的影响。最后，CL1 专为低功耗设计，强调可持续性和延长的研究时间。

---

## 27. 空芯光纤

**原文标题**: Hollow Core Fiber (HCF)

**原文链接**: [https://www.holightoptic.com/what-is-hollow-core-fiber-hcf%ef%bc%9f/](https://www.holightoptic.com/what-is-hollow-core-fiber-hcf%ef%bc%9f/)

本文探讨了空芯光纤(HCF)技术，这是光纤光学领域的一项革命性进展，它通过空芯（空气或真空）来引导光，而不是像传统光纤那样通过实心玻璃或塑料纤芯。HCF最大限度地减少了信号损耗和色散，从而实现了更快、更高效的数据传输。

本文详细介绍了HCF的关键组成部分（纤芯、包层、保护层），并强调了其相对于实心光纤的优势：由于空气中较低的吸收而减少的信号损耗，由于光在空气中传播速度更快而降低的延迟，由于空芯最大限度地减少了光-材料相互作用而带来的更高功率处理能力，减少了非线性效应从而改善了信号质量，以及降低了色散从而能够在更长的距离上实现更好的信号完整性。

尽管有这些优点，HCF也面临着挑战。制造过程复杂且昂贵，并且光纤可能比传统光纤更脆弱。然而，HCF在电信（更快的网络）、医疗设备（精确的光传输）、高功率激光系统（高效的光束传输）、传感和测量（提高的精度）以及数据中心（降低的延迟）等应用中具有巨大的潜力。本文的结论是，HCF有潜力通过提供跨多个领域的性能增强来改变光通信。

---

## 28. 大上Paperlike 13K是一款13.3英寸E Ink彩色显示器

**原文标题**: Dasung Paperlike 13K is a 13.3 inch E Ink color monitor

**原文链接**: [https://liliputing.com/dasung-paperlike-13k-is-a-13-3-inch-e-ink-color-monitor-crowdfunding/](https://liliputing.com/dasung-paperlike-13k-is-a-13-3-inch-e-ink-color-monitor-crowdfunding/)

大上Paperlike 13K是一款13.3英寸的E Ink彩色显示器，具有3200 x 2400分辨率，灰阶内容显示为300 ppi，刷新率高达37 Hz。 然而，由于采用支持4096色的E Ink Kaleido 3显示技术，彩色内容会将像素密度降低至150 ppi。 预购价为749美元（彩色）和679美元（仅黑白），预计将于2025年5月中下旬发货。

该显示器具有USB-C和HDMI输入接口、用于镜像安卓设备的带有反向触摸控制的触摸屏、一个3.5毫米音频插孔、一个内置扬声器和用于调节设置的物理按钮。 其铝合金机身纤薄轻巧，重721克，并包含HDMI/USB-C线缆、两种支架选项（便携式支架和保护套）以及VESA支架兼容性等配件。

虽然E Ink技术具有低功耗和环境光下可视的优点，但与LCD/AMOLED相比，颜色显得较为柔和，并且更快的刷新率可能会导致残影。 彩色版本具有前置灯，而黑白版本则没有。 苹果设备尚未完全支持，但支持Windows、Linux和Android。

---

## 29. 星链用户终端拆解

**原文标题**: Starlink User Terminal Teardown

**原文链接**: [https://www.darknavy.org/blog/a_first_glimpse_of_the_starlink_user_ternimal/](https://www.darknavy.org/blog/a_first_glimpse_of_the_starlink_user_ternimal/)

DARKNAVY拆解并分析了星链标准驱动（Rev3）用户终端天线（UTA），重点关注其硬件和固件。 UTA包含一个大型PCB，带有射频前端芯片和一个类似于物联网设备的核心区域，采用定制的意法半导体四核Cortex-A53 SoC（保密且不可用）。

为了分析UTA的软件，DARKNAVY将eMMC芯片拆焊并转储了固件。提取的固件显示了一个未加密的启动链、内核和部分文件系统。分析表明，网络堆栈架构类似于DPDK，主要依赖于用户空间的C++程序来处理网络数据包，从而绕过内核以提高效率。有趣的是，该固件还包含通常属于卫星或地面网关的功能。

DARKNAVY构建了一个基于QEMU的仿真环境来促进分析，并成功运行和调试了部分软件。

一个专用的安全芯片STSAFE-A110（CC EAL5+）提供了一个唯一的标识符（UUID），管理用于卫星通信认证的公钥证书，并为用户数据传输导出对称加密密钥。它作为独立于SoC安全启动机制的信任根。

发现了一个“以太网数据记录器”程序，该程序捕获卫星遥测数据包（使用硬件密钥加密）。虽然令人担忧，但没有迹象表明它在收集用户数据。在设备初始化期间，41个SSH公钥被添加到/root/.ssh/authorized_keys文件中，这引起了安全担忧。文章最后强调了空间安全的重要性以及未来在数字和物理领域发生战斗的可能性。

---

## 30. Zombieverter：开源VCU，用于再利用报废电动汽车部件

**原文标题**: Zombieverter: Open source VCU for reusing salvage EV components

**原文链接**: [https://openinverter.org/wiki/ZombieVerter_VCU](https://openinverter.org/wiki/ZombieVerter_VCU)

“ZombieVerter”是一款开源车辆控制单元（VCU），专为电动汽车改装设计，特别针对回收利用电机、电池和充电器等报废电动汽车部件。它通过提供一个具有多样化输入输出、控制逻辑和基于Web的配置及数据记录界面的通用VCU，解决了不同制造商之间控制和通信方法各异的难题。

ZombieVerter支持来自日产聆风、三菱欧蓝德、丰田/雷克萨斯混合动力汽车的常用报废电动汽车部件，并支持CHAdeMO/CCS直流快速充电。其硬件功能包括板载WiFi、PWM驱动器、低端输出、输入引脚、CANbus接口、LIN总线、同步串行接口和OBD-II接口。软件功能涵盖接触器、充电器、电机和加热器控制、油门映射、电机再生、巡航控制（潜在）、BMS限制、数据记录等。

本文提供了组装VCU的指南，包括外壳选择和视频教程。它详细介绍了电源、接触器、油门踏板、启动/运行/方向以及输入/输出引脚的接线说明。包含了初始启动和测试说明，重点介绍连接到Web界面和基本配置。其中包含初始化ISA分流器的章节。此外，它还提供故障排除技巧以及指向相关资源的链接，如开发线程、软件版本和GitHub存储库。

---

## 31. 利用计算机视觉重建蛾翅膀上的幻觉伪装图案

**原文标题**: Reconstructing illusory camouflage patterns on moth wings using computer vision

**原文链接**: [https://royalsocietypublishing.org/doi/10.1098/rsif.2024.0757](https://royalsocietypublishing.org/doi/10.1098/rsif.2024.0757)

无法访问文章链接。

---

## 32. WASM 2.0

**原文标题**: WASM 2.0

**原文链接**: [https://www.w3.org/TR/wasm-core-2/](https://www.w3.org/TR/wasm-core-2/)

本文档是 WebAssembly (WASM) 2.0 核心规范的草案，描述了底层、类似汇编的虚拟指令集架构。WASM 旨在实现快速、安全和可移植的执行，在沙盒环境中实现接近原生的性能。它与硬件、语言和平台无关，支持模块化、高效编译和流式传输。

该规范侧重于核心 ISA 层，定义了指令集、二进制编码、验证和执行语义，而不详细说明特定于环境的 API。WASM 通过缺乏环境访问来解决安全性问题，依赖于嵌入器通过导入的函数来控制与环境的交互。该规范依赖于 IEEE-754-2019 进行浮点表示，依赖于 UNICODE 进行命名。

WASM 操作基本数字类型（32/64 位宽度的整数和 IEEE-754 浮点数），以及支持打包数据的 128 位向量类型。代码包含在堆栈机上执行的指令，以及块和循环等控制流结构。陷阱会中止执行并报告给环境。函数接受和返回值的序列，并可以使用局部变量。表是函数引用的数组，用于促进间接调用。线性内存为加载/存储操作提供可变的字节数组。模块包含函数、表、内存和全局变量的定义，这些定义可以导入和导出。

在语义上，WASM 分为解码（将二进制格式转换为内部表示）、验证（良好性和类型检查）和执行（实例化和调用）。本文档详细介绍了用于定义 WASM 抽象语法的语法符号和约定。向量是具有最多 2^32 -1 个元素的有界序列，对于表示数据结构至关重要。

---

## 33. 美国专利商标局拒绝特斯拉Robotaxi商标，因其“仅具描述性”。

**原文标题**: USPTO refuses Tesla Robotaxi trademark as "merely descriptive"

**原文链接**: [https://arstechnica.com/cars/2025/05/robotaxi-and-cybercab-are-too-unoriginal-to-trademark-uspto-tells-tesla/](https://arstechnica.com/cars/2025/05/robotaxi-and-cybercab-are-too-unoriginal-to-trademark-uspto-tells-tesla/)

特斯拉推出无人驾驶“机器人出租车”的计划受阻，美国专利商标局驳回了该公司“robotaxi”商标申请，认为该术语过于通用且仅具描述性。该机构引用维基百科、《The Verge》以及自动驾驶汽车初创公司Zoox等广泛使用该术语的情况作为证据。

这并非特斯拉首次遭遇品牌问题。该公司试图注册“Cybercab”商标的尝试也因可能与使用“Cyber-”前缀的现有商标产生混淆而被驳回。

这款缺乏方向盘和踏板的双座电动“机器人出租车”计划于下个月在德克萨斯州奥斯汀市投入使用。特斯拉计划依靠远程操控来处理其自动驾驶系统无法应对的情况。文章强调了对特斯拉“FSD”系统可靠性的担忧，并引用独立测试表明该系统需要频繁的人工干预，以及美国国家公路交通安全管理局（NHTSA）对其驾驶辅助系统的持续调查。此外，作者还提到了特斯拉之前与Alcon Entertainment就使用《银翼杀手2049》图像一事发生的纠纷，以及埃隆·马斯克对监管机构的潜在影响力。

---

## 34. Audiobookshelf：自托管有声读物和播客服务器

**原文标题**: Audiobookshelf: Self-hosted audiobook and podcast server

**原文链接**: [https://www.audiobookshelf.org/](https://www.audiobookshelf.org/)

本文介绍 Audiobookshelf，一个用于管理和收听有声读物和播客的自托管服务器。它强调 Audiobookshelf 是自托管的，让用户可以控制自己的数据和收听体验。本文也作为官方 Audiobookshelf 文档的入口，引导用户查找更多关于用户指南、常见问题、如何支持项目以及功能展示的信息。

---

## 35. 马来亚的隽永设计

**原文标题**: Malaya's Timeless Design

**原文链接**: [https://www.linyangchen.com/Philately](https://www.linyangchen.com/Philately)

林扬琛著《马来亚永恒的设计》深入探讨了马来亚椰子主题邮票的设计与制作，涵盖了广泛的历史、技术和艺术层面。

本书细致地研究了设计元素，从建筑和几何图形到独特的手工字体。它追溯了这些设计的演变，探索了演化先驱和全球“双椰子设计”的影响。作者还将“椰子”美学与“帝国”风格进行了对比。

本书对邮票生产的技术细节给予了极大的关注，包括雕刻周期、印刷工艺（可能在伦敦）、水印、纸张识别与分析（厚度、纤维、条纹形态发生、表面轮廓测定）以及所用颜色和墨水的成分（“椰子蓝”、“品红狂想曲”等）。

本书还涵盖了历史背景，包括二战时期、邮票的早期、槟城印章以及不同时期使用的各种加盖（例如，丁加奴、英国军事管理局）。本书细致地分析了加盖形态、伪造加盖和版模缺陷，甚至关注了具体的邮票，如5美元高面值邮票和25分双重加盖邮票。

本书考察了新加坡和马来各邦（柔佛、吉打等）独立后的发展，突出了椰子设计的变化。本书还涉及伪造品、安全标记以及计算分析在邮票研究中的应用，包括紫外荧光、扫描电子显微镜和拉曼光谱等技术。最后的部分包括统计信息、稀有度图表、百科全书和技术附录。

---

## 36. 推算航法

**原文标题**: Dead Reckoning

**原文链接**: [https://www.damninteresting.com/dead-reckoning/](https://www.damninteresting.com/dead-reckoning/)

1741年，英国皇家海军的“瓦格号”作为舰队的一部分，试图在针对西班牙帝国的战时任务中，穿越合恩角附近险恶的德雷克海峡。 “瓦格号”原本是一艘不适合这种环境的货船，它面临着猛烈的风暴、坏血病肆虐的船员和已故的船长，这使得他们危险地落后于舰队的其他船只。

由于“詹金斯的耳朵战争”而构思的任务，旨在掠夺西班牙在南美洲西海岸的领地。 安森准将的舰队因补给和人员短缺而延误，其中包括有争议的征召体弱退伍军人。 尽管知道在短暂的夏季窗口之外绕过合恩角的危险，但舰队还是在季节后期起航。

德雷克海峡无情的风和洋流迫使他们不断抢风行驶，阻碍了航行进度。 简陋的导航工具导致不准确的航位推算，加剧了他们位置上的误差。 经过数周的艰难困苦，“瓦格号”的船员们认为他们已经绕过了海角并转向北方，但随即被警告附近有岩石。 他们恢复了南下的航线，进一步消耗了补给。

炮手约翰·巴克利建议选择更安全的替代方案，即胡安·费尔南德斯岛，但奇普船长坚持原定的集合点。 实行了定量配给，军官们携带手枪以防止哗变。 文章结尾，“瓦格号”沿着南美洲西海岸航行，为即将到来的海难埋下了伏笔。

---

## 37. 由于计算机系统故障，整个湾区捷运系统瘫痪。

**原文标题**: Entire BART system is down due to computer systems failure

**原文链接**: [https://www.bart.gov/](https://www.bart.gov/)

由于电脑系统故障，整个BART系统目前已瘫痪。除了这次重大中断之外，BART网站还重点介绍了其他近期更新和正在进行的举措，包括Embarcadero车站新扶梯的启用，将站台详细信息整合到行程规划器中，以及为2025年海湾到堤坝赛跑活动提供的特别早班服务。

BART也在应对近期的挑战，由于影响BART总部的PG&E电力中断，BART董事会会议已重新安排。 同时也有好消息，BART报告称，2025年第一季度暴力犯罪率下降了23%，公共交通乘客人数总体增加。

该网站还为乘客提供资源，包括行程规划器、实时出发信息、时刻表和地图、票价计算器、停车信息以及有关机场服务和正在进行的BART项目的详细信息。它还推广探索可通过BART到达的夜生活场所。

---

## 38. Usenix ATC 公告

**原文标题**: Usenix ATC Announcement

**原文链接**: [https://www.usenix.org/blog/usenix-atc-announcement](https://www.usenix.org/blog/usenix-atc-announcement)

无法访问文章链接。

---

## 39. Void：开源光标替代方案

**原文标题**: Void: Open-source Cursor alternative

**原文链接**: [https://github.com/voideditor/void](https://github.com/voideditor/void)

Void：开源AI代码编辑器，作为Cursor的替代方案。它允许用户在其代码库上使用AI代理，检查点和可视化变更，并集成各种模型，包括本地托管。关键的隐私特性是Void直接将消息发送给提供商，不存储用户数据。

该仓库包含完整的源代码，并通过HOW_TO_CONTRIBUTE指南欢迎新的贡献者。开发者鼓励通过每周的Discord会议参与，并欢迎合作和建议。

Void基于VS Code仓库，并提供VOID_CODEBASE_GUIDE以帮助导航代码库。通过Discord服务器或电子邮件hello@voideditor.com提供支持。还提供了路线图、变更日志和网站等资源，以获取更多信息。

---

## 40. Fui：用于在TTY环境中与帧缓冲区交互的C语言库

**原文标题**: Fui: C library for interacting with the framebuffer in a TTY context

**原文链接**: [https://github.com/martinfama/fui](https://github.com/martinfama/fui)

Fui 是一个 C 语言库，它可以在 TTY 环境中实现帧缓冲用户界面。它直接操作帧缓冲设备，并使用分层绘图系统实现高效渲染。 主要功能包括：

*   **分层绘图:** 允许将像素值绘制到多个图层上，然后将这些图层合成并渲染到帧缓冲。
*   **图元绘制:** 提供用于绘制基本形状（如线条、矩形和圆形）的函数。
*   **文本渲染:** 支持使用位图字体显示文本。
*   **输入处理:** 通过 libevdev 提供键盘和鼠标输入的事件处理，以及用于其他事件类型的通用事件系统。
*   **声音系统:** 包括一个基于 ALSA 的基本声音系统，能够播放正弦音和和弦。

安装过程包括使用 `make` 和 `sudo make install` 编译和安装库。要使用该库，请在编译器标志中包含 `-Lfui -l:libfui.a`。该库是静态链接的，消除了共享库依赖。

由于帧缓冲和输入访问需要 root 权限，因此建议使用 `sudo usermod -aG video "$USER"` 和 `sudo usermod -aG input "$USER"` 将用户添加到 `video` 和 `input` 组。 必须注销并重新登录或重新启动才能使更改生效。

`examples` 文件夹中的示例展示了该库的功能，其中包括 `main.c` 和 `bodies.c`，它们演示了核心组件，以及 `asteroids` 文件夹中的 Asteroids 游戏，它演示了声音系统。 `tests` 文件夹中还提供了使用 cmocka 的单元测试。

---

## 41. Claude Code的统一价格订阅

**原文标题**: A flat pricing subscription for Claude Code

**原文链接**: [https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-max-plan](https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-max-plan)

Anthropic Max计划现提供Claude Code，这是一个命令行工具，允许直接在终端中使用Claude模型进行编码任务。这为Claude（网页、桌面、移动端）和Claude Code提供了一个统一的订阅。Claude Code有助于委派复杂的编码任务，同时保持控制和透明度。

要使用Claude Code，用户需要有效的Max计划订阅（5个Pro席位，每月100美元，或20个Pro席位，每月200美元），然后从文档页面下载并安装Claude Code，并使用其Claude凭据进行身份验证。

Max计划在Claude和Claude Code之间共享使用限制，影响消息和提示的数量。使用情况变化取决于多种因素，例如消息/对话长度、文件附件（对于Claude）以及项目复杂性、代码库大小和自动接受设置（对于Claude Code）。 5个Pro席位计划的预计使用量为每5小时225条Claude消息或50-200条Claude Code提示。 20个Pro席位计划提供相应更高的限制（每5小时900条Claude消息或200-800条Claude Code提示）。

达到速率限制时，用户会收到警告，并且可以选择升级到更高等级的Max计划，通过Anthropic Console切换到按需付费模式，或者等待重置。 文章引导用户查阅关于使用限制最佳实践的资源。

---

## 42. 根据劳森判据衡量的聚变能量增益进展

**原文标题**: Progress toward fusion energy gain as measured against the Lawson criteria

**原文链接**: [https://www.fusionenergybase.com/articles/continuing-progress-toward-fusion-energy-breakeven-and-gain-as-measured-against-the-lawson-criteria](https://www.fusionenergybase.com/articles/continuing-progress-toward-fusion-energy-breakeven-and-gain-as-measured-against-the-lawson-criteria)

本文探讨了在实现聚变能量增益方面取得的进展，重点关注劳森判据作为关键基准。劳森判据本质上定义了聚变反应产生比启动和维持反应所需能量更多能量所需的条件。这些条件涉及实现足够高的等离子体密度、温度和约束时间。

本文可能详细介绍了不同聚变反应堆设计的进展，如托卡马克、仿星器和惯性约束聚变装置，以及每种设计在满足劳森判据方面的进展。它可能讨论了具体的实验及其相应的结果，突出了在等离子体温度、密度和约束时间方面的改进。

本文可能还承认在实现持续聚变能量增益方面仍然存在的重大技术和科学挑战。这些挑战可能包括控制等离子体不稳定性、开发用于反应堆组件的耐用材料以及有效提取聚变反应中的能量。最后，它可能以评估当前聚变研究的现状以及对实现实际聚变能量的未来时间表的展望作为结尾。重点是了解当前的实验结果与满足劳森判据的接近程度，以及需要哪些进展来弥合剩余的差距。

---

## 43. 机器人邂逅烹饪艺术

**原文标题**: Robotics meets the culinary arts

**原文链接**: [https://actu.epfl.ch/news/robotics-meets-the-culinary-arts/](https://actu.epfl.ch/news/robotics-meets-the-culinary-arts/)

一个瑞士-意大利团队创造了RoboCake，一款可食用机器人结婚蛋糕，展示了机器人食品研究的进展。该项目是欧盟资助的RoboFood计划的一部分，融合了机器人技术和美食学，探索可食用机器人和智能食品的潜力。

RoboCake的特色是由内部气动系统驱动的可食用石榴味泰迪熊。研究人员还开发了由维生素B2、槲皮素、活性炭和巧克力制成的可食用可充电电池。这些电池具有黑巧克力味，并带有酸爽的回味，可以为蛋糕上的LED蜡烛供电，并为减少电子垃圾提供潜在的解决方案。

来自EPFL、意大利理工学院和EHL的研究人员合作，以确保RoboCake既美味又安全。其目标是开发用于各种应用的可食用机器人，包括紧急营养、药物输送和食品监测。 RoboFood项目是一项耗资350万欧元的计划，旨在以一种全新的方式结合食品科学和机器人技术，重点关注食品保鲜、紧急营养、人类和兽医医学或新的烹饪体验。该项目强调食品是一种宝贵的资源，并旨在潜在地减少过度饮食。

---

## 44. Podfox：首个容器感知浏览器

**原文标题**: Podfox: First Container-Aware Browser

**原文链接**: [https://val.packett.cool/blog/podfox/](https://val.packett.cool/blog/podfox/)

本文详细介绍了作者在使用Podman运行多个容器化项目时消除端口冲突的历程。由于端口转发管理带来的困扰，作者开发了Podfox，一个容器感知的SOCKS代理。Podfox允许Web浏览器（Firefox）通过进入Podman的无根网络命名空间直接与容器通信，从而消除了对端口转发和基于主机的DNS配置的需求。

Podfox的工作原理是解析`<容器>.<网络>.podman`主机名，查询Podman以获取网络信息，并代理请求。通过简单的Firefox PAC文件配置，可以将对`.podman` TLD的请求定向到Podfox。

文章随后探讨了命令行开发环境的容器化。作者没有使用专门的容器开发工具，而是提倡将整个环境引入到项目特定的容器中。这通过将只读的Homebrew安装（包含作者的工具）挂载到容器中，并将入口点设置为Homebrew安装的shell（fish）来实现。这种方法允许在任何容器镜像中立即访问熟悉的工具，而无需冗余安装。

为了简化此过程，作者创建了Podchamp，一个fish脚本，它可以读取项目特定的配置文件，自动执行`podman run`或`podman exec`命令，并通过OSC序列将容器信息传递给Ptyxis终端模拟器。最终实现了一个无缝且高效的容器化开发工作流程。

---

## 45. 来自：史蒂夫·乔布斯。“好主意，谢谢。”

**原文标题**: From: Steve Jobs. "Great idea, thank you."

**原文链接**: [https://blog.hayman.net/2025/05/06/from-steve-jobs-great-idea.html](https://blog.hayman.net/2025/05/06/from-steve-jobs-great-idea.html)

1991年10月，作为NeXT公司的一名新系统工程师，史蒂夫·海曼（shayman@next.com）发现他可以申请电子邮件别名。他注意到尽管公司里有多位名叫史蒂夫的员工，但“steve@next.com”这个邮箱尚未被使用，便天真地请求将它转发到自己的地址。

这很快变成了一场灾难，他开始收到发给史蒂夫·乔布斯（sjobs@next.com）的，来自记者、CEO和金融专业人士的误发邮件。海曼惊慌失措，立即将别名更改为转发至sjobs@next.com，然后给乔布斯发邮件坦白错误并道歉。

出乎意料的是，史蒂夫·乔布斯回复了一条简单的信息：“好主意，谢谢你。” 海曼始终不明白乔布斯所说的“好主意”是什么意思，但他珍视这封邮件，因为这是他收到的唯一一封来自乔布斯的私人信件。他开玩笑说，这个可能的“好主意”是苹果公司后来的成功。海曼最终以蒂姆·库克的一封邮件结束了自己的职业生涯，并感叹自己的幸运。

---

## 46. 完全控制.xyz 自由形式G代码

**原文标题**: Full Control.xyz Freeform Gcode

**原文链接**: [https://fullcontrol.xyz/#/models](https://fullcontrol.xyz/#/models)

《FullControl.xyz自由形式G代码》简介：该文推介FullControl系统，旨在实现3D打印中不受约束的设计。它认为传统CAD/CAM流程存在局限性，而FullControl通过直接生成G代码提供了一种替代方案。这意味着一种更注重实践、以代码为中心的设计和控制3D打印过程的方法。其核心信息是设计的自由度和灵活性，允许用户创建超出标准设计软件约束的形状和结构。

本质上，FullControl使用户能够直接定义工具路径和打印参数，从而实现对打印过程的精细控制。虽然本文未详细介绍具体功能或特性，但它将FullControl定位为实现更复杂和非常规几何形状的一种方式，从而突破了3D打印的可能性边界。它暗示了向更程序化3D设计方法的转变，可能吸引具有编码技能的用户以及寻求探索高级3D打印技术的用户。

---

## 47. eBPF谜团：IPv4何时非IPv4？当它伪装成IPv6时

**原文标题**: eBPF Mystery: When is IPv4 not IPv4? When it's pretending to be IPv6

**原文链接**: [https://blog.gripdev.xyz/2025/05/06/ebpf-mystery-when-is-ipv4-not-ipv4-when-its-ipv6/](https://blog.gripdev.xyz/2025/05/06/ebpf-mystery-when-is-ipv4-not-ipv4-when-its-ipv6/)

使用 eBPF 程序调试 .NET DualMode 套接字的探险记

此文详述了一次涉及 eBPF 程序的调试冒险，尤其是在处理 .NET 的 DualMode 套接字时。作者最初的目标是使用 `BPF_CGROUP_INET4_CONNECT` 透明地重定向来自 Docker 容器的 DNS 请求，并使用 `BPF_PROG_TYPE_CGROUP_SKB` 程序阻止 IPv6 流量。

问题出现在 .NET CLI 挂起时，尽管 Wireshark 显示只有 IPv4 流量，但仍触发了出口 eBPF 程序中的 IPv6 阻止。`connect4` eBPF 程序没有被触发，表明没有发出 IPv4 连接调用。

通过内核和 .NET 源代码分析，作者发现 .NET 使用 DualMode 套接字，即使对于 IPv4 流量，也请求 IPv6 套接字，并利用 IPv4 映射的 IPv6 地址 (::ffff:x.x.x.x)。这意味着内核看到了 IPv6 连接尝试，但底层流量是 IPv4。

解决方案包括：

1. 创建一个 `connect6` eBPF 程序来拦截 IPv6 连接调用。
2. 在 `connect6` 中，识别 IPv4 映射的 IPv6 地址，并提取嵌入的 IPv4 地址以执行所需的重定向。
3. 修改出口 eBPF 程序，通过检查 `skb->protocol` 而不是 `skb->family` 来区分真正的 IPv6 流量和 IPv4 映射的流量，允许后者，同时仍然阻止 IPv6。

本文强调了现代网络堆栈的复杂性以及理解协议如何分层和隧道化的重要性。作者强调了 `bpf_ringbuf_output` 在调试 eBPF 程序中的实用性。

---

## 48. 苹果iMessage PQ3协议的形式化分析 [pdf]

**原文标题**: A Formal Analysis of Apple's iMessage PQ3 Protocol [pdf]

**原文链接**: [https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-595-linker.pdf](https://www.usenix.org/system/files/conference/usenixsecurity25/sec25cycle1-prepub-595-linker.pdf)

本文档似乎是对苹果iMessage PQ3协议的底层分析，可能是一项逆向工程。内容经过编码，使用FlateDecode解码后，输出结果仍然在很大程度上无法读取。它似乎包含二进制数据，可能代表PQ3协议的技术规范、数据结构或算法细节。诸如“/Type /XObject”、“/Subtype /Form”和“/Filter /FlateDecode”之类的元数据表明它是PDF结构中的一个对象，可能包含与分析相关的图形元素或其他资源。

鉴于解码数据的不可读性，无法从此摘录中对PQ3协议的功能或所采用的特定加密技术进行具体总结。 然而，该文档的存在表明对iMessage的端到端加密协议进行了正式、深入的探索，可能旨在了解其安全属性或潜在漏洞。它包含看似图像或图形元素，文件名为“usenixbadges-available.pdf”，暗示此分析可能已在USENIX等安全会议上展示或计划展示。该数据可能包括PQ3中涉及的底层加密原语、密钥交换机制和消息格式的详细规范。

---

## 49. 水塘抽样

**原文标题**: Reservoir Sampling

**原文链接**: [https://samwho.dev/reservoir-sampling/](https://samwho.dev/reservoir-sampling/)

本文解释了水库抽样，这是一种从未知大小的数据流中选择项目随机样本的技术，它使用一个固定大小的“水库”来保存样本。本文使用从一次显示一张的牌组中选择纸牌的比喻来阐述问题和解决方案。

最初，作者描述了适用于项目总数已知时更简单的随机抽样技术。然后，它介绍了从事先不知道项目总数的流中进行抽样的挑战。

水库抽样的核心思想是，根据与目前为止已看到的项目数量成比例的概率，用新项目替换水库中的现有项目。对于单个项目，新项目替换现有项目的概率为 1/n，其中 n 是已看到的项目数量。作者清楚地解释了这如何确保公平性，这意味着每个项目都有同等的被选择机会。解释包括详细的概率计算。

然后，本文将该概念扩展到选择多个项目（k 个项目），其中替换概率变为 k/n。一种实际的实现方法是生成一个随机数，如果随机数小于 k，则替换水库中的一个随机元素。

本文说明了水库抽样在日志收集服务中的效用，在日志收集服务中，需要对日志进行抽样，以避免在高峰时段使服务不堪重负。该方法确保仅在峰值期间进行抽样，同时保持公平性。最后，本文简要提到了加权水库抽样的存在，适用于某些项目比其他项目更有价值的场景。

---

## 50. 腓尼基文化主要通过文化交流传播。

**原文标题**: Phoenician culture spread mainly through cultural exchange

**原文链接**: [https://www.mpg.de/24574685/0422-evan-phoenician-culture-spread-mainly-through-cultural-exchange-150495-x](https://www.mpg.de/24574685/0422-evan-phoenician-culture-spread-mainly-through-cultural-exchange-150495-x)

本文挑战了腓尼基文化在地中海传播的传统观点。一项基于古代DNA分析的新研究表明，其传播并非主要源于来自黎凡特的大规模移民，而是一种文化交流和同化的动态过程。

研究人员分析了来自黎凡特、北非、伊比利亚和地中海岛屿等14个腓尼基和布匿考古遗址的人类遗骸的基因组。令人惊讶的结果是，布匿人口具有高度可变和异质的遗传谱，具有显著的北非和西西里-爱琴海血统，而来自黎凡特腓尼基人的直接遗传贡献很少。

这突显了布匿世界的国际化特性，包括北非和西西里-爱琴海血统在内的不同祖先的人们并肩生活并相互融合。该研究还发现了地中海地区紧密的家庭联系的证据，进一步支持了古代地中海社会通过贸易、通婚和人口流动紧密相连的观点。这些发现强调了文化传播在传播腓尼基文化方面的作用，而非大规模移民，并为公元前一千纪该地区复杂的人口历史提供了新的见解。

---

## 51. 二战时期美国如何建造五千艘舰船

**原文标题**: How the US built 5k ships in WWII

**原文链接**: [https://www.construction-physics.com/p/how-the-us-built-5000-ships-in-wwii](https://www.construction-physics.com/p/how-the-us-built-5000-ships-in-wwii)

二战期间，美国大幅提升造船能力，从停滞不前的产业转型为在1939年至1945年间生产了近四千万总吨的商船。这一壮举是通过政府和私营企业的合作实现的，美国海事委员会发挥了关键作用。

由埃默里·兰德海军上将领导的海事委员会，旨在通过鼓励效率和大规模生产技术来振兴美国造船业。这项工作的关键是六大公司的参与，这是一个以快速完成大型建设项目而闻名的财团。他们建造了新的造船厂，并在亨利·凯撒和斯蒂芬·贝克特尔的领导下，创新了建造方法。

建造的船只分为两类：海军采用传统方法建造的先进军用舰艇，以及海事委员会采用焊接和预制等创新技术建造的运输船只。其中最著名的是自由轮，这是一种经过改进的英国设计，适用于大规模生产。

自由轮采用流水线方式建造。钢板被塑形和制造，然后焊接成更大的部分。凯撒的造船厂为战争作出了重大贡献，生产了海事委员会吨位的大部分。通过采用新颖的生产方法和培养竞争精神，美国得以以前所未有的速度生产大量的船只，这对支持盟军的战争努力至关重要。

---

## 52. 为您的应用做好Google Play 16 KB页面大小兼容性要求的准备

**原文标题**: Prepare your apps for Google Play's 16 KB page size compatibility requirement

**原文链接**: [https://android-developers.googleblog.com/2025/05/prepare-play-apps-for-devices-with-16kb-page-size.html](https://android-developers.googleblog.com/2025/05/prepare-play-apps-for-devices-with-16kb-page-size.html)

此Android开发者博客宣布Google Play针对Android 15+设备的新兼容性

支持16 KB页面大小可以带来性能提升，例如更快的应用启动速度（3-30%）、改进的电池使用率（4.5%）、更快的相机启动速度（4.5-6.6%）以及更快的系统启动速度（8%）。不支持此功能的应用程序可能无法在新设备上正常运行。

许多流行的SDK（如React Native、Flutter）和游戏引擎（Unity）已经兼容或提供兼容版本。没有原生代码的应用可能已经兼容。使用原生库的应用程序可能需要更新，而具有自定义原生代码的应用程序可能需要使用更新的工具链重新编译。

该博客建议尽早检查应用程序的兼容性，特别是依赖项。开发者可以使用Play管理中心的应用包资源管理器页面来检查构建合规性并识别需要更新的区域。还鼓励在16 KB环境中进行测试。提供了更详细的技术解释和完整文档的链接。

---

## 53. 在 Chromium 中发现一个 Bug

**原文标题**: Finding a Bug in Chromium

**原文链接**: [https://bou.ke/blog/chromium-bug/](https://bou.ke/blog/chromium-bug/)

2025年5月，作者详述了在开发Atrium时发现Chromium漏洞的经过。Atrium是作者所在机器人公司Monumental所开发的Electron应用，使用编译为WASM的Rust，并依赖JavaScript的`FinalizationRegistry`，通过为垃圾回收对象注册清理回调来管理Rust内存。

作者发现了一个内存泄漏问题，表现为终结器停止被调用，导致WASM内存持续增长。该问题在同一窗口内重新加载后依然存在，需要新建窗口才能解决。

经过深入调查和指标跟踪，作者成功创建了一个最小化的可重现示例，摆脱了其复杂的Electron应用环境。该示例涉及持续向`FinalizationRegistry`中插入大量对象并多次重新加载选项卡。几次重新加载后，这些对象的垃圾回收停止，从而导致内存泄漏。

作者在Chrome Canary（2025年5月2日的138.0.7156.0版本）中确认了该漏洞。鉴于Chromium代码库的复杂性以及存在发生竞争条件的可能性，作者选择提交错误报告，而不是尝试自行修复，希望Chromium团队能够解决此问题。文章最后刊登了一则招聘广告，招募对将浏览器引擎推向极限充满热情的人才。

---

## 54. 37signals告别AWS：完整S3迁移，预计节省1000万美元

**原文标题**: 37signals Says Goodbye to AWS: Full S3 Migration and $10M in Projected Savings

**原文链接**: [https://systemadministration.net/37signals-says-goodbye-to-aws-full-s3-migration-and-10m-in-projected-savings/](https://systemadministration.net/37signals-says-goodbye-to-aws-full-s3-migration-and-10m-in-projected-savings/)

37signals 迁移出 AWS，预计节省一千万美元。文章还简要提及了 Kalker，一款“重新定义高级计算的科学计算器”。

---

## 55. 首位美国籍教皇当选，将被称为利奥十四世。

**原文标题**: First American pope elected and will be known as Pope Leo XIV

**原文链接**: [https://www.cnn.com/world/live-news/new-pope-conclave-day-two-05-08-25](https://www.cnn.com/world/live-news/new-pope-conclave-day-two-05-08-25)

芝加哥的罗伯特·普雷沃斯特枢机主教当选为首位美国籍教皇，尊号为良十三世。这位69岁的教皇在圣彼得大教堂的就职演说中，呼吁和平并缅怀了他的前任教皇方济各。

良十三世为教皇职位带来了丰富的全球经验。他职业生涯的大部分时间都在南美洲担任传教士，拥有美国和秘鲁双重国籍，最近领导着梵蒂冈一个负责主教任命的重要部门。预计他将继续教皇方济各发起的改革。

他的当选获得了广泛的积极反响，世界各国领导人纷纷表示祝贺，并希望与他就重要的全球事务进行合作。美国总统唐纳德·特朗普称赞这次历史性的选举是美国的一项重大荣誉。

---

## 56. 埃及学家发现巴黎标志性方尖碑上的隐藏信息

**原文标题**: Egyptologist uncovers hidden messages on Paris’s iconic obelisk

**原文链接**: [https://news.artnet.com/art-world/hidden-messages-paris-luxor-obelisk-2636508](https://news.artnet.com/art-world/hidden-messages-paris-luxor-obelisk-2636508)

据报道，一位埃及古物学家在巴黎协和广场卢克索方尖碑上发现了以前未被注意或误解的象形文字信息。这座方尖碑原产于埃及卢克索神庙，19世纪被赠予法国。该研究可能集中于解读方尖碑四面以及在巴黎添加的基座上的特定椭圆纹饰和铭文。

这些“隐藏的信息”可能涉及对该方尖碑最初献给拉美西斯二世、他的成就以及他与太阳神阿蒙-拉的神圣联系的更深入理解。这位埃及古物学家可能已经发现了之前被忽略的关于拉美西斯二世统治时期、他的军事胜利或他的宗教信仰的细节，从而揭示了对这位法老自我展示的新见解。

这篇文章也可能讨论方尖碑抵达巴黎是一个象征性行为，以及这些信息如何与其新的背景相互作用。译文可能会强调埃及和法国文化之间的关系，或者揭示运输期间的政治气候。文章很可能以强调埃及古物学研究在理解古埃及历史及其对全球文化和卢克索方尖碑等地标的持久影响方面持续的重要性而告终。

---

## 57. 作为服务器的静态资源

**原文标题**: Static as a Server

**原文链接**: [https://overreacted.io/static-as-a-server/](https://overreacted.io/static-as-a-server/)

本文探讨了“服务器”和“静态”框架之间日益模糊的界限，尤其是在React服务器组件（RSC）的背景下。作者强调，尽管RSC传统上与服务器端渲染相关联，但它们可以用于生成完全静态的网站，正如他们自己托管在免费Cloudflare CDN上的博客所展示的那样。

核心论点是，支持服务器端和静态输出的“混合”框架提供了更大的灵活性，并减少了工具碎片化。这些框架本质上在构建过程中“运行服务器”，生成静态HTML、CSS和JavaScript文件。这消除了对Jekyll或Hugo等独立“纯静态”工具的需求，作者认为这些工具并没有提供任何独特的优势。

“混合”方法允许开发人员在每个路由的基础上选择服务器端和静态渲染，从而提供细粒度的控制和适应性。项目可以无缝地从完全静态的内容过渡到动态内容，而无需进行大量的代码重构或生态系统转换。

作者以支持服务器和静态功能的Next.js为例。他们通过禁用服务器功能来强制执行静态输出。这使得他们的RSC可以在构建时运行，获取数据并生成静态HTML，而不是在运行时。文章最后倡导接受这种二元性，认识到“静态”本质上是一个“提前运行的服务器”。统一的代码库和灵活的部署选项使“混合”框架成为Web开发更具优势的选择。

---

## 58. 块扩散：自回归语言模型与扩散语言模型的插值

**原文标题**: Block Diffusion: Interpolating Autoregressive and Diffusion Language Models

**原文链接**: [https://m-arriola.com/bd3lms/](https://m-arriola.com/bd3lms/)

本文介绍了“块扩散”(Block Diffusion)，一种新型语言模型，弥合了自回归模型和扩散模型之间的差距。扩散语言模型具有并行生成和可控性等优点，但在似然建模和固定长度生成方面存在局限性。“块扩散”通过实现灵活长度生成，并通过KV缓存和并行令牌采样等技术提高推理效率，克服了这些缺点。

作者提出了一种构建高性能“块扩散”模型的综合策略，包括高效的训练算法、梯度方差估计器和数据驱动的噪声调度，旨在最大限度地减少训练期间的方差。通过在离散去噪扩散和自回归方法之间进行插值，“块扩散”充分利用了两种架构的优势。

主要成果在于，“块扩散”在标准语言建模基准测试中，与其他扩散语言模型相比，实现了最先进的性能，同时支持生成任意长度的序列。这使其成为该领域的重大进步，解决了以前扩散语言模型中固有的关键局限性。

---

## 59. 让我们现实地看待依赖关系。

**原文标题**: Let's be real about dependencies

**原文链接**: [https://wiki.alopex.li/LetsBeRealAboutDependencies](https://wiki.alopex.li/LetsBeRealAboutDependencies)

文章《让我们正视依赖关系》探讨了软件中过度依赖的问题，特别是将Rust在这方面的声誉与Unix系统上C和C++程序的实际情况进行了比较。作者认为，虽然Rust明确地声明了依赖关系，但C和C++通常依赖于系统级库，从而有效地隐藏了依赖关系的复杂性。

为了说明这一点，作者使用`ldd`来检查真实C++应用程序（如RViz、Evolution、OBS Studio和VLC）使用的动态库。结果显示了令人惊讶的依赖库数量，即使对于看似适中的应用程序，也常常超过100个库。作者深入研究了RViz的依赖关系，表明虽然其直接依赖关系可能看起来易于管理，但传递依赖关系会导致更大的`.so`文件集。

这篇文章强调了一个常见的误解，即C和C++代码的依赖关系较少。相反，作者认为区别在于如何管理和暴露这些依赖关系。在C/C++中，发行版处理依赖关系，掩盖了复杂性。 使用Rust，程序员直接管理它们，导致臃肿的 perception。最终，作者得出结论，依赖关系问题并不是新的或Rust独有的，而是现代软件开发的一个基本方面，通常隐藏在“传统”C/C++环境中。

---

## 60. 一颗恒星被一个流浪的超大质量黑洞摧毁了

**原文标题**: A star has been destroyed by a wandering supermassive black hole

**原文链接**: [https://arstechnica.com/science/2025/05/a-star-has-been-destroyed-by-a-wandering-supermassive-black-hole/](https://arstechnica.com/science/2025/05/a-star-has-been-destroyed-by-a-wandering-supermassive-black-hole/)

2024年，兹威基瞬变源观测设施探测到一个不寻常的天体AT2024tvd，结果证实是一颗恒星在潮汐瓦解事件(TDE)中被超大质量黑洞撕裂。该事件引人注目，因为它是在可见光波段首次识别出的TDE，并且负责的超大质量黑洞并非位于星系中心，而是位于约2500光年之外，同时星系中心的黑洞也在积极地吞噬物质。

后续在各种波段的观测证实了AT2024tvd是一个TDE，其特征是持续的高温、紫外光谱特征元素以及与超新星相比更少的高能X射线。

该发现引发了关于两个超大质量黑洞存在以及其中一个偏离中心位置的问题。文章表明，星系合并可能导致多个黑洞，其中一些会被抛出或在距离核心的位置停留数百万年。

该发现还强调，由于过去频繁的合并留下了更多的“游荡”黑洞，因此在大型星系中，偏离中心的TDE可能更为常见。此外，文章还推测，在非常大的星系中，中心超大质量黑洞的事件视界可能非常大，以至于它会完整地吞噬恒星，从而阻止可观测的TDE，并使偏离中心的事件成为唯一可见的事件。

---

## 61. 司法部的极端提议将损害消费者和美国的科技领导地位。

**原文标题**: DOJ's extreme proposals will hurt consumers and America's tech leadership

**原文链接**: [https://blog.google/outreach-initiatives/public-policy/doj-search-remedies-may-2025/](https://blog.google/outreach-initiatives/public-policy/doj-search-remedies-may-2025/)

谷歌监管事务副总裁李-安妮·穆尔霍兰德撰文反对司法部对其谷歌搜索案提出的补救措施，声称这些措施将损害消费者利益并扼杀美国科技领导地位。

文章称，司法部忽视了ChatGPT、Grok和Perplexity等服务的激烈竞争，这些服务正迅速获得关注并快速创新。文章强调，促销协议并未阻碍这些竞争对手，并列举了苹果整合ChatGPT以及摩托罗拉整合Perplexity和微软的CoPilot等例子。

作者认为，司法部的提议会减少消费者的选择，因为这会使访问首选搜索引擎变得更加困难，并损害像Firefox这样的浏览器。此外，强制性的数据披露将威胁到美国的隐私，可能导致广泛的数据泄露。

文章认为，司法部的提议相当于对搜索业务的“实际剥离”，通过消除研发投资的激励因素来阻碍谷歌的创新。强制共享数据和知识产权将鼓励竞争对手克隆谷歌，而不是独立创新。剥离Chrome会破坏它，降低安全性，并对ChromeOS等相关项目产生负面影响。

最终，作者得出结论，司法部的提议主要惠及那些寻求在不进行自身创新的情况下访问谷歌技术的竞争对手，而未能考虑消费者的最佳利益，这才是美国反垄断法的核心原则。谷歌将继续倡导有利于所有人的创新产品。

---

## 62. 《活死人之夜》如何意外进入公有领域

**原文标题**: How "Night of the Living Dead" Accidentally Became Public Domain

**原文链接**: [https://screenrant.com/night-living-dead-movie-public-domain-copyright-accident/](https://screenrant.com/night-living-dead-movie-public-domain-copyright-accident/)

由于发行商的失误，乔治·罗梅罗的《活死人之夜》这部定义了现代僵尸的里程碑式恐怖片，出人意料地进入了公有领域。在将影片名称从《食人肉之夜》更改后，发行商未能在新拷贝上添加必要的版权声明。这一疏忽意味着任何人都可以自由复制、分享和发行这部电影。

尽管《活死人之夜》票房收入超过3000万美元，但罗梅罗并没有从中获得多少利润。他还错失了众多公司利用公有领域地位发行的家庭录像带所带来的巨额收入。罗梅罗对此感到惋惜，因为版权错误使他无法从他的开创性作品中获得经济利益。

尽管遭遇了经济上的挫折，但本文认为《活死人之夜》的公有领域地位反而促进了其持久的受欢迎程度。通过无数版本的发行和频繁的电视播放，这部电影的易于访问性确保了更广泛的观众群，巩固了其作为受人尊敬的经典作品的地位。这部以11.4万美元的适度预算制作的电影在烂番茄上获得了很高的评分，证明了其广受好评和观众喜爱。《活死人之夜》彻底改变了恐怖类型，探讨了危机期间的人性和偏执主题。

---

## 63. Show HN: 使用 eBPF 无代理透视加密流量

**原文标题**: Show HN: Using eBPF to see through encryption without a proxy

**原文链接**: [https://github.com/qpoint-io/qtap](https://github.com/qpoint-io/qtap)

Qtap是一款eBPF代理，可以直接从Linux内核拦截和解密TLS/SSL流量，无需修改应用程序、代理或证书管理即可提供对发送和接收数据的可见性。这使得用户能够查看带有上下文（进程、容器、用户等）的未加密数据，并可用于安全审计、调试网络问题、API开发、解决第三方集成问题、协议学习、调查遗留系统以及验证测试。

Qtap以带外方式工作，开销极小，不会引入延迟。它可以增强现有的可观察性管道，或构成自定义解决方案的基础。用户可以快速在演示模式下进行测试，或直接安装。它需要启用BTF和eBPF的Linux内核5.10+，以及提升的权限。

该项目正处于早期开发阶段，欢迎社区反馈和贡献。它以AGPLv3.0（开源）和商业许可双重许可。提供了安装和开发说明，包括Go、Make和Clang等先决条件。贡献者必须同意贡献者许可协议。

---

## 64. 不！忏悔吧！来自哈兰！(1998)

**原文标题**: No! Repent! From! Harlan! (1998)

**原文链接**: [https://harlanellison.com/text/amaz_int.htm](https://harlanellison.com/text/amaz_int.htm)

这篇1998年对哈兰·埃里森的采访涵盖了他对技术的看法、写作过程以及近期出版的书籍。埃里森强烈捍卫了他对手动打字机的偏爱，认为电脑是不必要的，并且对写作艺术有害。他认为艺术应该充满挑战，并且书写的物理行为对于他的创作过程至关重要。

这次采访还深入探讨了他最著名的短篇小说之一《“忏悔吧，小丑！”嘀嗒人说》。埃里森透露，这个故事写得很快，从初稿开始基本没有改变，并获得了星云奖和雨果奖。

最后，埃里森讨论了他的“刃之工作”系列，该项目旨在以20卷双册的形式重新印刷他的31个作品。他强调这些版本不仅仅是重印，而是更新和更正过的“首选文本”，提供了极高的价值。他还强调了新作品或未收集作品的收录，以及大量的自传式文章，使它们成为对其作品的全面介绍。他将自己的作品与科幻小说区分开来，说他更像是一个作家或幻想家，并谴责将他对电视的评论贴上科幻小说的标签。

---

## 65. 设计稳健性

**原文标题**: Stability by Design

**原文链接**: [https://potetm.com/devtalk/stability-by-design.html](https://potetm.com/devtalk/stability-by-design.html)

本文探讨了人们对Clojure库稳定性的认知，并将其与动态语言因库升级中潜在的重大更改而导致不稳定性的普遍担忧进行了对比。作者认为，尽管Clojure是动态语言，但由于社区惯例和设计原则，它拥有一个稳定的生态系统。

文章通过Slack讨论、代码保留图表（显示Clojure及其库与Scala相比变化最小）以及Fusebox库中优先考虑向后兼容性的错误修复的轶事，展示了Clojure稳定性的证据。

文章解释说，Clojure的稳定性源于以下几个因素：依赖命名空间、函数和不可变数据结构，而不是频繁修改的对象；使用EDN进行序列化，确保数据一致性；以及使用命名空间键来避免命名冲突。

核心论点强调，库的更改是导致破坏的主要原因，特别是重命名（方法、类型、字段等）和方法签名更改。作者建议，增强功能应主要涉及添加新功能，而不是修改现有功能。通过避免重命名、接受可选参数以及创建新函数而不是更改旧函数，Clojure库最大限度地减少了重大更改。文章总结说，任何语言都可以采用这些原则，静态类型虽然有用，但并不是根本的解决方案。关键在于对向后兼容性的承诺和周全的库设计。

---

## 66. 如何加固 GitHub Actions

**原文标题**: How to harden GitHub Actions

**原文链接**: [https://www.wiz.io/blog/github-actions-security-guide](https://www.wiz.io/blog/github-actions-security-guide)

本文旨在指导如何强化 GitHub Actions 的安全性，其动机源于近期利用 GitHub Actions 工作流漏洞发起的供应链攻击。文章强调了组织层面的配置以及安全的工作流构建。

主要要点包括：

*   **术语：** 了解 GitHub Actions 的组成部分，例如工作流、Action、事件和任务。
*   **组织安全：** 设置只读默认工作流权限，限制 Action 的来源为经过验证的来源和允许列表，通过将 Runner 限制为特定存储库来管理工作流的采用，并避免自动创建和批准拉取请求。
*   **分支保护：** 强制执行合并代码的规则，但承认其局限性，并考虑提交签名和带外检测。
*   **密钥管理：** 默认使用存储库级别的密钥，利用组织级别的密钥进行共享基础设施，并为敏感操作利用需要批准的环境级别密钥。在工作流中按名称单独访问密钥。
*   **工作流安全：** 尽量减少使用第三方 Action，优先使用经过验证的或 GitHub 创建的 Action。使用它们时，请考虑贡献者人数、代码复杂性和受欢迎程度。使用哈希值而不是标签来锁定 Action 版本。谨慎管理权限，在任务级别明确定义必要的权限，以强制执行最小权限原则。
*   **漏洞：** 通过小心管理高权限触发器、清理输入以及避免在不受信任的上下文中使用 GITHUB_ENV 和 GITHUB_PATH 来避免中毒管道执行 (PPE)。
*   **工件：** 小心处理工件，以防止凭据泄露。
*   **Runner：** 尽可能使用 GitHub 托管的 Runner，因为它们是临时的且经过沙盒处理。由于安全风险增加，使用自托管 Runner 时要谨慎。

---

## 67. 一次性代码：不要回收，直接扔掉（2017）

**原文标题**: Throwaway Code: Don't recycle, throw it away (2017)

**原文链接**: [https://www.sung.codes/blog/2017/throwaway-code-dont-recycle-throw-away](https://www.sung.codes/blog/2017/throwaway-code-dont-recycle-throw-away)

“一次性代码：不要回收，扔掉它！”这篇博文认为，为特定、有限目的编写的代码（一次性代码）在完成其功能后，应该被*扔掉*，而不是被重新利用或集成到主代码库中。

作者强调，一次性代码通常编写迅速，没有像生产代码那样经过严格考虑。因此，它可能缺乏适当的文档，缺少正确的错误处理，并且通常不是为可维护性或可重用性而设计的。

尝试回收此类代码可能会导致技术债务，从而在项目中引入错误和复杂性。调试和调整一次性代码以用于其他目的通常比从头开始编写新的、干净的代码花费更多的时间和精力。

关键的结论是，虽然一次性代码可以成为快速原型设计、实验或一次性任务的宝贵工具，但认识到它的局限性并避免重用它的诱惑至关重要。相反，应该优先创建设计良好、可维护的代码以供长期使用，并在一次性代码完成其直接目的后正确地将其丢弃。

---

## 68. Apple Lisa Pascal 源码 – 小型机器的 Pascal

**原文标题**: Apple Lisa Pascal sources – Pascal for small machines

**原文链接**: [http://pascal.hansotten.com/apple-lisa-pascal/apple-lisa-pascal-sources/](http://pascal.hansotten.com/apple-lisa-pascal/apple-lisa-pascal-sources/)

本文详细介绍了Apple Lisa Pascal和Silicon Valley Software (SVS) Pascal编译器源代码的可用性。 Lisa Pascal最初基于SVS Pascal编译器，后由Apple扩展。 SVS还销售用于其他系统（如CP/M）的Pascal编译器。

该编译器本身是多通道的，生成带有优化代码生成器和链接器的68000目标代码。 Lisa Pascal通过诸如Units（INTERFACE和IMPLEMENTATION）、高级文件I/O（SEEK、BLOCKREAD、BLOCKWRITE）、字符串操作（DELETE、COPY、INSERT）和程序控制（EXIT、HALT）等功能增强了标准Pascal。值得注意的是，它不是面向对象的，也不是UCSD Pascal的变体，而是借鉴了“Wirth编译器学派”和UCSD Pascal的灵感。

Apple以纯文本格式发布了用Lisa Pascal和汇编语言编写的Lisa操作系统源代码。 本文还描述了从Lisa磁盘映像（dc42格式）中发现和转换原始SVS Pascal编译器源代码的过程。 这些源代码使用AppleSauce软件提取并转换为纯ASCII文本，剥离了Apple Lisa TEXT格式的伪像。

本文提供了下载Lisa操作系统源代码、Lisa Pascal编译器的dc42磁盘映像、以Lisa TEXT格式导出的编译器源代码和对象，以及编译器源代码的纯文本版本以及从TEXT文件转换的工具的链接。 还提到了Lisa Pascal和SVS Pascal的手册。

---

## 69. 质谱法可在数分钟内而非数天内识别病原体

**原文标题**: Mass spectrometry method identifies pathogens within minutes instead of days

**原文链接**: [https://phys.org/news/2025-05-mass-spectrometry-method-pathogens-minutes.html](https://phys.org/news/2025-05-mass-spectrometry-method-pathogens-minutes.html)

慕尼黑工业大学（TUM）和伦敦帝国理工学院的研究人员开发了一种快速质谱方法，可在数分钟内识别细菌病原体，与需要数天的传统培养方法相比，大大缩短了等待时间。

这项发表在《自然·通讯》上的新方法，直接在组织和粪便样本中识别细菌的特定代谢产物，而不是直接检测细菌本身。这是通过将样本与包含232种具有重要医学意义的细菌及其代谢产物的数据库进行比较来实现的。从该数据库衍生的特定生物标志物能够快速识别病原体。

该技术可以识别导致各种疾病的细菌，包括胃癌、肺炎、脑膜炎、早产、淋病和败血症。第一作者Wei Chen表示，关注代谢产物可以实现更快的检测。

Nicole Strittmatter教授强调了个性化医疗的潜力，能够实现量身定制的疗法，从而显著改善治疗效果。该团队计划扩展数据库，纳入超过1400种已知细菌病原体的代谢产物，以实现更广泛的临床应用。这种快速识别方法为医生提供了一个重要的工具，有助于有针对性的干预和改善患者护理。

---

## 70. 我的Stack Overflow问题被关闭了，所以这是一篇关于CoreWCF的博文。

**原文标题**: My stackoverflow question was closed so here's a blog post about CoreWCF

**原文链接**: [https://richardcocks.github.io/2025-05-08-CoreWCF.html](https://richardcocks.github.io/2025-05-08-CoreWCF.html)

Richard Cocks 详述了他对 Stack Overflow 的不满，因为他关于 CoreWCF 的问题在没有获得有帮助的答案的情况下被关闭。他正在探索使用 CoreWCF 在 .NET Framework 和 .NET 8 应用程序之间流式传输随机数以进行 RPC 吞吐量测试。他遇到了一个问题，即使客户端断开连接后，服务器仍在继续消耗 CPU，并无休止地写入流。

他怀疑自己对 WCF 流的实现不正确，尤其是在处理未知长度的流方面。他担心达到最大消息长度，这进一步表明他错误地使用了 WCF 进行连续数据传输。他提供了服务合约 `StreamingService`、`RandomStream` 和客户端实现的代码片段。客户端成功接收数据，但即使客户端关闭连接后，服务器仍无限期地继续写入流。

Richard 不确定 WCF 流是否适用于此场景，并且正在考虑其他方法，例如发送单个消息（尽管吞吐量有限）或使用会话模式进行外部流协调。他希望获得关于使用 CoreWCF 在进程之间高效且可靠地流式传输数据的正确方法的指导。他认为，即使他的方法存在缺陷，解决他在 Stack Overflow 上的问题也会使其他有类似问题的人受益。他邀请大家提供反馈，并指向他的 GitHub 存储库以获取完整代码。

---

## 71. 物理学家将铅变成了金——仅持续一瞬间

**原文标题**: Physicists turn lead into gold – for a fraction of a second

**原文链接**: [https://www.nature.com/articles/d41586-025-01484-3](https://www.nature.com/articles/d41586-025-01484-3)

欧洲核子研究中心（CERN）大型强子对撞机（LHC）的物理学家们实现了一种现代炼金术，将铅转化为金，尽管只是短暂一瞬，且代价高昂。这并非通过化学反应实现，而是通过以接近光速的速度撞击铅离子。当离子擦肩而过时，强烈的电磁场会产生一个能量脉冲。这个脉冲导致一个铅原子核射出三个质子，有效地将其转化为金。

大型强子对撞机上的ALICE实验在碰撞碎片中识别出了这些嬗变事件。研究人员计算得出，在2015年至2018年期间，大约产生了860亿个金原子核，相当于约29万亿分之一克。然而，这些金原子极不稳定，寿命很短，存在时间仅约百万分之一秒，之后便与实验装置碰撞或衰变为其他粒子。

---

## 72. 教授称UAB“篡改”研究提案，施压教员：信函

**原文标题**: Professors say UAB is 'altering' research proposals, pressuring faculty: Letter

**原文链接**: [https://www.al.com/news/2025/05/professors-say-uab-is-altering-research-proposals-pressuring-faculty-letter.html](https://www.al.com/news/2025/05/professors-say-uab-is-altering-research-proposals-pressuring-faculty-letter.html)

阿拉巴马大学伯明翰分校教职员工指控校方干预研究计划，特别是针对少数族裔健康的研究。一份在教职工中流传的草拟信件指责阿拉巴马大学伯明翰分校的律师和工作人员通过删除文本、移除引用或阻止研究启动等方式，篡改资助提案，以削弱科学目标。

教职员工认为，这些归因于赞助项目办公室的行为构成了审查，侵犯了学术自由。他们声称，该大学正在将受保护群体的健康风险和担忧排除在研究之外，并举例说明了诸如黑人妇女的孕产妇死亡率或特定群体中的疾病传播等研究。他们担心针对特定种族群体中普遍存在的独特遗传疾病的研究也受到威胁。

这封致阿拉巴马大学伯明翰分校教职工参议院院长和研究副校长的信件敦促校方发布一项正式的拨款申请政策，以确保研究可以在不受不当干预的情况下进行。教职员工强调，他们的担忧源于希望维护阿拉巴马大学伯明翰分校作为一所受人尊敬的学术机构的地位。

文章还提到阿拉巴马大学伯明翰分校最近为遵守联邦和州指令而采取的行动，包括终止少数族裔奖学金并退还相关捐款。阿拉巴马大学伯明翰分校发言人表示，学校正在评估州和联邦层面的发展，尊重学术自由，并致力于改善所有人的健康和福祉。

---

## 73. 专注于大脑区域的人工智能重现你的所见 (2024)

**原文标题**: AI focused on brain regions recreates what you're looking at (2024)

**原文链接**: [https://www.newscientist.com/article/2438107-mind-reading-ai-recreates-what-youre-looking-at-with-amazing-accuracy/](https://www.newscientist.com/article/2438107-mind-reading-ai-recreates-what-youre-looking-at-with-amazing-accuracy/)

2024年文章报道人工智能在基于脑活动记录重建图像方面的突破。研究人员开发出人工智能系统，仅根据猕猴的脑活动记录，就能生成对受试者所见事物的高度精确重建。

一项关键发现是，当人工智能被训练专注于大脑中特定的、相关的区域时，这些重建的准确性会显著提高。这种“注意力机制”使人工智能能够优先处理信息量最大的神经信号。

拉德堡德大学的乌穆特·居克吕表示，这些是迄今为止最接近且最准确的重建，突显了这在神经解码和人工智能领域的进步。文章还暗示，更多细节可在《新科学家》中的一篇较长文章中找到。

---

## 74. 欧洲启动项目以吸引科学家离开美国

**原文标题**: Europe launches program to lure scientists away from the US

**原文链接**: [https://es.wired.com/articulos/europa-lanza-iniciativa-para-atraer-talento-cientifico-tras-recortes-en-ee-uu](https://es.wired.com/articulos/europa-lanza-iniciativa-para-atraer-talento-cientifico-tras-recortes-en-ee-uu)

欧盟启动“选择欧洲搞科研”计划，吸引科研人员，尤其是来自美国的科研人员，以应对美国科学经费削减和限制性政策。该计划由欧盟委员会主导，将在2025年至2027年间投资5亿欧元，旨在抵消特朗普政府时期对科学的负面影响以及近期对艾滋病毒研究和新冠病毒研究等领域的经费削减。

欧盟的目标是到2030年将研发投资增加到GDP的3%，并提供“超级资助”以确保稳定性。他们计划将迁往欧洲的科学家的资助增加一倍。 尽管承认存在官僚障碍，欧盟强调其强大的科研基础设施、对开放科学的承诺以及提供基本服务的社会市场经济。 一项新的欧洲研究区法律将保障科研自由。

由于上述问题，越来越多的美国科学家正在考虑离开美国，其中75%的人正在考虑离开。外国机构的申请激增，而国际社会对在美国工作的兴趣则有所下降。

各个欧洲国家也在加大力度。法国的艾克斯-马赛大学正在为流离失所的美国研究人员提供“避风港”计划，德国的马克斯·普朗克学会正在与美国机构建立联合研究中心。 西班牙正在积极招聘量子计算和人工智能等领域的人才，并通过诸如“国家人才吸引计划”和“拉蒙·卡哈尔”计划等项目提供大量资金增加，以吸引年轻和资深的科研人员，尤其是那些在美国感到“被轻视”的人。

---

## 75. 账号封禁的阴暗面

**原文标题**: The dark side of account bans

**原文链接**: [https://madelinemiller.dev/blog/dark-side-account-bans/](https://madelinemiller.dev/blog/dark-side-account-bans/)

Maddy Miller的文章深入探讨了在线账号封禁对现代生活的重大影响，她根据自己因恶意举报而被Meta服务（Facebook、Instagram、WhatsApp）封锁近两个月的亲身经历，突显了这些平台已成为日常活动不可或缺的一部分。

作者详细描述了与朋友的沟通中断所带来的挑战，因为许多人仅依赖Facebook Messenger或WhatsApp。她还强调了访问餐厅菜单（通常只在Instagram上）、买卖二手物品（Facebook Marketplace）以及参加公共活动（Facebook活动）的困难。

Miller认为，失去对Meta等关键平台的访问权限会将个人与社会的重要方面隔离开来，引发了人们对这些公司所掌握权力的担忧。她批评大型公司提供的客户支持不足，使得在没有重要关系的情况下几乎不可能对账户封禁提出申诉。

作者强调，这个问题超越了Meta，影响了各种平台。个人经常陷入被人工智能审核错误标记或成为恶意举报的受害者，却求助无门。

Miller倡导社会转变对这些平台的看法。它们现在几乎像社会服务一样运作，但缺乏问责制。文章总结说，个人可以轻易失去账户，加上恢复的困难，这是一个令人担忧的趋势，需要改善客户支持并重新评估这些公司所掌握的权力。作者声明，这不仅仅是她的个人经历，而是一个需要关注的普遍问题。

---

## 76. Cogentcore: 使用Go构建多平台应用的开源框架

**原文标题**: Cogentcore: Open-source framework for building multi-platform apps with Go

**原文链接**: [https://github.com/cogentcore/core](https://github.com/cogentcore/core)

Cogent Core 是一款用 Go 编写的开源框架，使开发者能够使用单一代码库为 macOS、Windows、Linux、iOS、Android 和 Web 等多个平台创建 2D 和 3D 应用程序。这种“一次编码，处处运行（Core）”的方法简化了开发和部署。Cogent Core 官方网站提供了大量的文档和交互式示例，可以直接编辑和运行。该网站本身通过使用 WebAssembly (wasm) 作为 Web 应用程序运行，展示了 Cogent Core 的功能。要开始开发，用户必须首先完成网站上提供的安装说明。该项目感谢 October Swimmer 等赞助商的支持，以改进 Cogent Core。本质上，Cogent Core 旨在通过使用 Go 简化跨平台应用程序开发，为不同的操作系统和环境提供统一的代码库。

---

## 77. 数学问题解决

**原文标题**: Mathematical Problem Solving

**原文链接**: [https://www.cip.ifi.lmu.de/~grinberg/t/20f/](https://www.cip.ifi.lmu.de/~grinberg/t/20f/)

本文档介绍数学 235：数学问题解决，这是一门由 Darij Grinberg 于 2020 年秋季在德雷塞尔大学讲授的课程。本课程介绍解决竞赛和期刊中常见数学问题的技巧和工具，例如数学归纳法、鸽巢原理和模算术。

本课程包括视频讲座、研讨课（协作解决问题环节）和每周作业。所需材料包括教师的笔记，推荐资源包括来自各种数学竞赛和期刊的书籍和在线问题集。

评估完全基于作业，并提供具体的评分标准和量表。允许在作业中进行协作和使用外部资源，但解决方案必须用学生自己的语言撰写，并注明出处。不接受迟交作业。

本课程的主要资源包括用于提交作业的 Gradescope、用于交流的 Piazza 以及用于家庭作业帮助的数学资源中心。本课程旨在为学生提供解决竞赛式问题的实践经验，并使他们熟悉标准的解题技巧及其应用。此外，还包括有关大学在学术不诚实、残疾资源和写作中心方面的政策信息。

---

## 78. 狗狗币软件工程师的电脑感染信息窃取恶意软件

**原文标题**: Doge software engineer's computer infected by info-stealing malware

**原文链接**: [https://arstechnica.com/security/2025/05/doge-software-engineers-computer-infected-by-info-stealing-malware/](https://arstechnica.com/security/2025/05/doge-software-engineers-computer-infected-by-info-stealing-malware/)

一名同时受雇于DOGE和CISA的软件工程师Kyle Schutt的设备可能已被信息窃取恶意软件入侵。自2023年以来，与其多个账户相关的凭据已出现在公开的数据泄露和窃取日志中。这引起了人们的担忧，因为Schutt可以访问这两个机构的敏感信息。在DOGE，他可以访问FEMA的财务管理系统；而在CISA，他可能了解关键基础设施安全信息。

记者Micah Lee注意到Schutt的凭据反复出现在泄露的数据中，表明其设备可能已遭入侵。该窃取恶意软件可以窃取登录信息、记录键盘输入并捕获屏幕输出。虽然凭据出现在泄露事件中并不一定表示个人设备遭入侵（可能是服务提供商泄露），但Schutt的信息持续重新出现强烈暗示他的凭据在某个时间点已被泄露。

令人担忧的是，如果Schutt在他的政府工作中使用了类似的凭据，攻击者可能会访问CISA和DOGE的敏感数据。DOGE的批评者认为这进一步证明了其糟糕的安全实践，暗示可能存在故意泄露机密的行为。CISA和国土安全部均未回应置评请求。

---

## 79. 废弃矿井坍塌时

**原文标题**: When Abandoned Mines Collapse

**原文链接**: [https://practical.engineering/blog/2025/5/6/when-abandoned-mines-collapse](https://practical.engineering/blog/2025/5/6/when-abandoned-mines-collapse)

当废弃矿井坍塌之时

本文《当废弃矿井坍塌之时》探讨了矿山地面沉陷问题，重点关注废弃矿井坍塌的原因、后果和减缓措施。文章首先强调了新泽西州沃顿附近最近出现的、归因于旧铁矿的塌陷坑。文章解释说，早期的采矿实践常常缺乏远见，地图绘制不足，且忽视了长期稳定性，导致了当前的问题。一个物理模型被用来展示“房柱式”开采如何导致最终的坍塌，特别是当与水蚀和缺乏支撑相结合时。

文章讨论了废弃的、被淹没的矿井对环境和基础设施的影响，导致塌陷坑和更广泛的地面沉陷，损害建筑物，扰乱排水系统，并破坏农田。文章提到，财产保险通常不包括矿山地面沉陷造成的损失，促使一些州设立政府补贴的项目。

文章还涉及现代采矿实践，特别是长壁采矿，这种方法会故意导致地面沉陷。文章强调了预测、测量和复垦受矿山地面沉陷影响的土地的重要性。工程措施包括使用各种数据和建模技术以及仪器来监测地面移动。复垦范围从简单的土地平整到广泛的结构改造和空隙填充。文章总结说，虽然采矿在历史上一直存在问题，但现代实践更加负责任，并侧重于平衡资源开采与环境保护。

---

## 80. Valkey一周岁：社区分支如何将Redis甩在身后

**原文标题**: Valkey Turns One: How the Community Fork Left Redis in the Dust

**原文链接**: [https://gomomentodev.wpenginepowered.com/blog/valkey-turns-one-how-the-community-fork-left-redis-in-the-dust/](https://gomomentodev.wpenginepowered.com/blog/valkey-turns-one-how-the-community-fork-left-redis-in-the-dust/)

Valkey：Redis闭源一年后的社区分支，性能卓越

---

## 81. CVE-2025-46336 (rack-session): Rack会话删除后恢复

**原文标题**: CVE-2025-46336 (rack-session): Rack session gets restored after deletion

**原文链接**: [https://rubysec.com/advisories/CVE-2025-46336/](https://rubysec.com/advisories/CVE-2025-46336/)

本文档描述了 CVE-2025-46336，一个中等严重性的漏洞，存在于 `rack-session` gem 中，特别是影响 `Rack::Session::Pool` 中间件。该漏洞允许攻击者在特定条件下恢复已删除的 rack session，从而在用户注销后授予未经授权的访问权限。

根本原因是会话管理中的竞争条件。 并发的 rack 请求可能导致已删除会话的恢复，因为会话在请求开始时准备好并在结束时保存。 如果攻击者可以使用受损的会话 cookie 发起长时间运行的请求，同时合法用户注销（删除其会话），则攻击者的请求在用户注销*之后*完成，可能会保存旧的会话数据，从而有效地恢复会话。

为了缓解此漏洞，建议用户升级到 `rack-session` 版本 2.1.1 或更高版本。 或者，应用程序可以使用 "logged_out" 标志来实现原子会话失效，或者使用跟踪失效时间戳的自定义会话存储来防止重用旧数据。 此漏洞与之前在 Rack 版本 < 3 中发现的类似问题有关。

该公告强调了会话管理中固有的竞争条件风险，并强调了适当的会话失效策略的重要性。 它还提供了相关资源的链接，包括 CVE 条目、修复该问题的 GitHub commit 以及相关的 Rack 公告。

---

## 82. 推出 Cursor 和 Claude Code 的注意事项

**原文标题**: Notes on rolling out Cursor and Claude Code

**原文链接**: [https://ghiculescu.substack.com/p/nobody-codes-here-anymore](https://ghiculescu.substack.com/p/nobody-codes-here-anymore)

无法访问文章链接。

---

## 83. Ty：快速的Python类型检查器和语言服务器

**原文标题**: Ty: A fast Python type checker and language server

**原文链接**: [https://github.com/astral-sh/ty](https://github.com/astral-sh/ty)

Ty 是一款用 Rust 编写的快速 Python 类型检查器和语言服务器。目前处于预发布和积极开发阶段，用户应预期存在错误和缺失功能。可以使用 `uv tool install ty` 安装。

用户可以使用 `ty check myfile.py` 或 `ty check my_project/` 检查 Python 文件或项目，并使用 `ty server` 启动语言服务器以进行 IDE 集成。详细的命令行选项可以在 CLI 文档中找到。

如有问题、错误报告或贡献，用户应在存储库中提交 issue。开发（包括对 Rust 源代码的 pull request，位于 `ruff` 子模块中）在 Ruff 存储库中进行，如贡献指南中所述。

Ty 采用 MIT 许可证，除非另有说明，否则贡献也采用 MIT 许可证。

---

## 84. DNA大约包含60到750兆字节的数据。

**原文标题**: DNA is maybe 60-750MB of data

**原文链接**: [https://dynomight.net/dna/](https://dynomight.net/dna/)

本文探讨了人类DNA包含多少信息的问题，挑战了最初基于碱基对数量的62亿比特的简单计算。它深入研究了“信息”的不同定义以及它们如何影响答案。

作者介绍了两个主要定义：存储空间定义（计算潜在的存储容量）和基于压缩的定义。存储空间定义得出女性DNA约为1.5 GB（120亿比特），男性DNA约为1.49 GB（119.4亿比特）的数字。然而，这并没有考虑到冗余和共同的祖先。

基于压缩的定义探讨了可以压缩多少DNA。使用参考基因组（代表共享DNA）的算法可以实现超过99％的压缩，表明只有少量独特信息。但是，这种方法低估了重要的、普遍共享的DNA。在没有参考基因组的情况下进行压缩只能实现大约25％的压缩（或者考虑到相同的染色体对，约为62％），从而导致更高的信息估计。

文章进一步区分了柯尔莫哥洛夫复杂度（输出字符串的最短程序）和香农信息（基于池中出现概率的信息）。将这些定义应用于DNA会导致信息估计差异很大，从大约1.2亿比特（香农）到46亿比特（柯尔莫哥洛夫）。作者更倾向于柯尔莫哥洛夫复杂度定义，认为它更好地捕捉了编码共享人类特征的信息。

最后，文章提到了生物过程的复杂性，指出只有一小部分DNA直接编码蛋白质，其余部分参与调节和其他功能，其中一些功能尚未完全理解。这突出了精确量化DNA中的“有用”信息的难度。文章提出了一个新的“比特”定义的想法——一种以我们目前的科学知识水平无法了解的比特。

---

## 85. 视觉电报的兴衰 (2017)

**原文标题**: The Rise and Fall of the Visual Telegraph (2017)

**原文链接**: [https://parisianfields.com/2017/11/05/the-rise-and-fall-of-the-visual-telegraph/](https://parisianfields.com/2017/11/05/the-rise-and-fall-of-the-visual-telegraph/)

巴黎田野的《视觉电报的兴衰》详细讲述了克劳德·夏普的光学电报系统在法国的历史，这是世界上第一个长途通信系统。受到一系列偶然事件的启发，作者追溯了夏普的发明从最初的构想到最终被淘汰的过程，而最初的推动力来自于法国大革命。

最初立志成为牧师的夏普，开发了一种视觉系统，利用塔楼上的铰链臂来远距离传输编码信息。尽管早期遭遇挫折，包括受到革命暴徒的袭击，但他的系统获得了政府的支持，并在法国各地实施，将巴黎与各个城市和战区连接起来。拿破仑甚至设想了一条横跨英吉利海峡的线路。

文章还提到了夏普面临的挑战，包括竞争对手的发明家和布兰克兄弟利用电报系统进行内幕交易。尽管光学电报最终在1852年被电报取代，但它在法国历史上留下了重要的印记。

作者指出，在法国仍然可以看到电报系统的遗迹，包括剩余的塔楼和街道名称。尽管纪念夏普的雕像在二战期间被移除，但人们正在努力保护和纪念他的遗产，以确保他对通信技术的贡献不会被遗忘。

---

## 86. 用户应在甲骨文年底临近之际审查其Java使用情况

**原文标题**: Users advised to review Oracle Java use as Big Red's year end approaches

**原文链接**: [https://www.theregister.com/2025/05/09/users_advised_to_review_oracle_java_use/](https://www.theregister.com/2025/05/09/users_advised_to_review_oracle_java_use/)

随着甲骨文财政年度末临近，专家建议各公司审查其Oracle Java使用情况，因为可能面临审计以及转向按员工许可模式，这已导致价格大幅上涨（两到五倍）。甲骨文正在全球建立Java销售团队，并开始对下载该软件的公司进行审计。

文章强调了人们对开源Java替代方案日益增长的兴趣，最近的一项调查表明，88%的Oracle Java用户正在考虑切换到开源JVM或JDK。像Azul这样的公司正在提供工具来跟踪Oracle Java实例，并帮助过渡到替代方案。

顾问建议考虑放弃Oracle Java，以避免许可问题，并增强与甲骨文的谈判能力，甚至有可能确保现有的按用户定价。他们建议各公司做好准备，证明他们可以在没有甲骨文产品的情况下运作，以便谈判出有利的条款。

另一位专家告诫不要理会甲骨文Java销售团队主动打来的电话，特别是如果公司对其合规性有信心。他建议大多数客户应考虑转向开源替代方案，以完全避免Oracle Java许可。文章强调了了解合同续签权利以及主动探索替代Java解决方案的重要性。

---

## 87. 验证，人工智能之钥 (2001)

**原文标题**: Verification, the Key to AI (2001)

**原文链接**: [http://incompleteideas.net/IncIdeas/KeytoAI.html](http://incompleteideas.net/IncIdeas/KeytoAI.html)

验证：人工智能的关键

里奇·萨顿在《验证：人工智能的关键》一文中指出，创建成功且稳健的人工智能系统的关键要素是自我验证，即人工智能自行判断其是否正常运作的能力。他认为，如果没有这种能力，人工智能系统仍然依赖于人为干预进行评估和修改，从而限制了它们的可扩展性和可靠性。萨顿将此称为“验证原则”，指出人工智能系统只能在能够验证的范围内创建和维护知识。

他通过人工智能历史上的例子来说明他的观点，强调了像深蓝这样的基于搜索的系统的成功，这些系统通过广泛的搜索树来验证它们的选择。然而，他也指出了局限性：深蓝依赖于人工调整的位置评分函数。他进一步强调了在更广泛的人工智能环境中，对不确定和变化的行动结果进行建模的挑战，在这些环境中，大多数系统都假定存在准确的、手动输入的行动模型。

萨顿批评了当前的人工智能领域，其中大型知识库和本体的构建依赖于人工构建和维护，无法验证自己的知识。他认为这种依赖导致系统脆弱且不可靠，并受到人类理解和监控的限制。他总结说，克服这种局限性，并赋予人工智能系统自我验证知识的能力，对于构建真正庞大、稳健和可扩展的人工智能至关重要。

---

## 88. 光标补全简史

**原文标题**: A Brief History of Cursor's Tab-Completion

**原文链接**: [https://www.coplay.dev/blog/a-brief-history-of-cursor-s-tab-completion](https://www.coplay.dev/blog/a-brief-history-of-cursor-s-tab-completion)

本文记录了Cursor卓越的Tab补全功能的历史，重点介绍了其收购Supermaven的Babble。Babble源于Jacob Jackson早期的项目TabNine，它通过使用编辑序列训练模型，而不是常见的中间填充（FIM）方法，超越了竞争对手。这使得建议不仅仅局限于直接的向下编辑，还能实现诸如从文件顶部导入包，甚至完全跳转到新文件等操作。

Babble凭借其巨大的上下文窗口脱颖而出，达到了100万个token，而其他模型则远远落后。这使其速度更快，建议范围更广。再加上编辑序列训练，使其整体表现更好。

Cursor收购Babble为他们带来了显著的优势。Cursor自己的编辑器使他们能够独家访问开发人员的交互和编辑序列，从而产生大量且有价值的数据集。只要未来Copilot工作流程的变化不改变格局，这种数据护城河就使Cursor成为人工智能驱动的编码助手的领导者。

---

## 89. 利用NASA的SMAP卫星探测L波段干扰

**原文标题**: Using NASA’s SMAP satellite to detect L-band interference

**原文链接**: [https://radioandnukes.substack.com/p/how-dare-you-transmit-at-14-ghz](https://radioandnukes.substack.com/p/how-dare-you-transmit-at-14-ghz)

利用NASA的SMAP卫星探测L波段干扰

---

## 90. 我的新期限：20年内捐出几乎所有财富

**原文标题**: My new deadline: 20 years to give away virtually all my wealth

**原文链接**: [https://www.gatesnotes.com/home/home-page-topic/reader/n20-years-to-give-away-virtually-all-my-wealth](https://www.gatesnotes.com/home/home-page-topic/reader/n20-years-to-give-away-virtually-all-my-wealth)

比尔·盖茨文章《我的新期限：20年内捐出几乎所有财富》摘要：

比尔·盖茨宣布大幅加快慈善捐赠步伐，目标是在未来20年内支出盖茨基金会的几乎所有资源。他将这种紧迫感归因于他所看到的全球危机，包括疫情、气候变化、乌克兰战争以及政治两极分化加剧。他认为慈善事业在应对这些挑战方面发挥着至关重要的作用。

为了实现这一雄心勃勃的目标，盖茨正在增加盖茨基金会的年度支出，到2026年从60亿美元增加到90亿美元。他承认，这种加速的步伐需要更大的捐赠基金，这就是他和梅琳达·弗兰奇·盖茨向基金会额外捐赠200亿美元的原因。他还提到，沃伦·巴菲特仍然是基金会的重要捐助者。

盖茨强调了基金会的重点领域，包括全球健康、减贫、性别平等和教育。他认为，创新解决方案和战略伙伴关系对于在这些复杂问题上取得进展至关重要。

他承认，有效地捐出这么多钱是一项具有挑战性的任务。然而，他表示乐观，盖茨基金会的工作，加上其他慈善家、政府和组织的努力，可以对改善世界各地人民的生活产生有意义的影响。最终，他表示希望通过捐献财富来应对世界挑战，从而从世界最富有的人名单中消失。

---

## 91. 传递消息

**原文标题**: Passing Messages

**原文链接**: [https://thedailywtf.com/articles/passing-messages](https://thedailywtf.com/articles/passing-messages)

文章“传递消息”似乎是一个着陆页或内容索引，而非一篇单一、连贯的文章。它主要列出了各种可用的内容类型，暗示着一个致力于信息共享的平台或网站，可能与编程或技术相关。

列出的内容类型包括：

*   **专题文章：** 暗示着对特定主题的深入探索。
*   **Codesod：** 这可能指的是网站上的一个特定版块或内容类型，可能与代码片段、代码挑战或代码相关的社区方面有关。
*   **Error'd：** 可能突出显示侧重于调试、错误处理或记录常见错误的文章或版块。
*   **论坛：** 表明一个社区讨论空间，用户可以在其中互动和交流信息。
*   **其他文章：** 一个用于不完全适合其他特定分类的文章的通用类别。
*   **随机文章：** 这个版块为用户提供了一个发现新的或不太突出的内容的途径。

本质上，“传递消息”充当了一个门户，通往涵盖软件、编码和技术相关讨论的各种信息。

---

## 92. 好也罢，坏也罢，超载（2024）

**原文标题**: For better or for worse, the overload (2024)

**原文链接**: [https://consteval.ca/2024/07/25/overload/](https://consteval.ca/2024/07/25/overload/)

本文深入探讨了C++中重载决议的复杂性，特别关注类型限定转换及其如何影响重载函数的选择。文章从一个看似简单的重载决议例子开始，然后逐步剖析其底层机制。

作者解释了隐式转换序列，强调了标准转换序列（左值到右值、数组到指针、函数到指针、整型/浮点型转换以及类型限定转换）的重要性。文章用了相当大的篇幅来解释cv限定符（const和volatile）及其如何影响类型转换。作者通过数学符号和示例简化了标准中对类型限定转换的描述，演示了编译器如何确定“cv组合类型”以及cv限定类型之间的转换是否有效。

文章随后回到重载决议，重新审视了可行候选者和“更好”函数的定义。文章介绍了标准转换序列的排序，并概述了确定哪个序列更优的规则，特别关注引用绑定中类型限定转换的复杂性。最后，作者提供了具体的例子来说明如何应用这些规则，包括一个忽略顶层cv限定符而导致重载歧义的例子。 关键结论是对编译器如何解决重载，尤其是在涉及const和volatile时，有了深入的理解。

---

## 93. Julia 中的 AMD GPU 编程

**原文标题**: AMD GPU Programming in Julia

**原文链接**: [https://amdgpu.juliagpu.org/dev/](https://amdgpu.juliagpu.org/dev/)

AMDGPU.jl 是一个 Julia 包，它允许直接从 Julia 编程 AMD GPU。它促进了利用 AMD ROCm 平台的高性能应用程序的开发。

**要点：**

*   **安装：** 可以使用 Julia 的包管理器通过 `Pkg.add("AMDGPU")` 轻松安装该包。
*   **

---

## 94. 使用Coalton实现量子编译器 (2022)

**原文标题**: Using Coalton to implement a quantum compiler (2022)

**原文链接**: [https://coalton-lang.github.io/20220906-quantum-compiler/](https://coalton-lang.github.io/20220906-quantum-compiler/)

本文探讨了使用Coalton语言（Common Lisp中的一种静态类型语言）实现名为“离散编译”的量子编译器特性。量子编译的主要挑战是将任意量子操作（通常表示为连续矩阵）转换为特定量子计算机上可用的原生操作序列。由于其模拟特性，真实的量子计算机具有有限的精度，因此有必要进行离散编译，即使用一组离散的原生操作来近似程序。

本文重点介绍了Ross-Selinger算法，该算法使用Clifford+T门集合离散化参数化操作，例如RZ(θ)。这涉及使用特定数环中的元素来近似RZ(θ)矩阵。一个关键的实现难点在于处理多个可互操作的数字类型，例如分圆整数和二次整数。

虽然Common Lisp可以表示这些环，但它缺乏与现有数值运算符的无缝集成以及对恒等式的统一处理。Coalton凭借其类型类和特设多态性，提供了一种更自然和类型安全的方式来实现这些数学对象。本文通过在Coalton中实现代数数（Z[√2]）来演示这一点，展示了类型类如何以可组合的方式扩展+、-和*等运算符，从而简化Ross-Selinger算法复杂数学要求的实现。

---

## 95. Show HN: Hyper – 首重标准的 React 替代方案

**原文标题**: Show HN: Hyper – Standards first React alternative

**原文链接**: [https://nuejs.org/blog/standards-first-react-alternative/](https://nuejs.org/blog/standards-first-react-alternative/)

Hyper：以标准优先的方式替代 React 构建用户界面，强调使用 HTML、CSS 和 JavaScript，避免复杂的抽象。它追求简洁性、强大的设计系统和可扩展性。本文将 Hyper 与 React 进行对比，突出了 React 的单体架构与 Hyper 的无头视图层方法。

Hyper 强调相比 React 更简洁的语法和更小的包体积，尤其是在处理涉及排序和筛选的复杂组件时。它演示了在 Hyper 中，通过简单更改 CSS 文件即可轻松替换设计系统，这与 React 不同，在 React 中，设计通常与组件紧密耦合，导致维护方面的挑战。

该项目旨在解决现代 React 开发中紧密耦合的设计和样板代码问题。Hyper 提倡真正可重用的组件、集中维护的设计系统以及关注点分离。

本文概述了 Hyper 的未来计划，包括全栈应用程序演示、直观的路由、数据库集成以及面向开发者和 AI 模型的生成式 UI 功能。它承认了开发者认知和产品完成度等挑战，但相信 Hyper 的简洁性和对标准的坚持将使其获得吸引力。Hyper 使用 Bun 构建，因为它支持 Web 标准且性能出色。

---

## 96. 产品炼狱：当他们喜欢它却仍然不买

**原文标题**: Product Purgatory: When they love it but still don't buy

**原文链接**: [https://longform.asmartbear.com/purgatory/](https://longform.asmartbear.com/purgatory/)

杰森·科恩的“产品炼狱”探讨了令人沮丧的状况：潜在客户对产品表达了真正的兴趣，但最终并未购买。 这不仅仅是礼貌的拒绝，而是一个更深层次的问题，即感知价值并未超过相关的风险、努力和实施中断。

科恩引入了“魔杖测试”来说明这一点：即使产品完全免费实施，许多客户仍然会因固有的摩擦和潜在的负面影响而拒绝。 他强调，价值主张必须大大超过这些惩罚才能促成购买。

文章随后超越了产品的可行性，探讨了紧迫性的关键因素。 即使产品通过了“魔杖测试”，如果它不是客户的首要任务，他们也可能不会购买。 科恩认为，公司需要确定特定的细分市场，在这些市场中，他们的产品可以解决紧急需求，这些需求是由紧急情况、战略决策或竞争压力驱动的。

他提出了一些问题，以帮助识别那些“现在就需要”产品的“完美客户”，重点关注产品对收入至关重要、受合规性、竞争压力或财务考虑驱动的情况。

最终，科恩认为，摆脱“产品炼狱”需要将注意力集中在一个利基市场，在这个市场中，产品可以解决一个迫在眉睫的问题。 虽然这似乎违反直觉，但吸引这些最初的紧急采用者最终将随着产品证明其价值而导致更广泛的采用。

---

## 97. 约翰·S·福斯特，小，研制弹头的五角大楼科学家，逝世，享年102岁

**原文标题**: John S. Foster Jr., Pentagon scientist who developed warheads, dies at 102

**原文链接**: [https://www.washingtonpost.com/obituaries/2025/05/07/john-foster-dead-nuclear-physics/](https://www.washingtonpost.com/obituaries/2025/05/07/john-foster-dead-nuclear-physics/)

冷战时期研发先进核弹头并影响美国国防政策的五角大楼科学家约翰·S·福斯特去世，享年102岁。福斯特曾担任劳伦斯利弗莫尔国家实验室主任，后在肯尼迪和约翰逊总统时期担任五角大楼国防研究与工程主任。

他的职业生涯主要集中在推进核武器和战略防御方面。他在导弹小型化核弹头的研发中发挥了关键作用，从而实现了更通用和可部署的核能力。他倡导开发多弹头独立重返大气层载具（MIRV）技术，该技术大大提高了核武库的破坏潜力。他强烈主张保持强大的核威慑力量来对抗苏联。

除了政府部门的工作外，福斯特还继续为国防部和多家公司提供有关国家安全问题的咨询。他因对科学和国防的贡献而获得了无数奖项和荣誉。他的工作与冷战时期的军备竞赛息息相关，并对全球安全格局产生了持久影响。讣告强调了他对国防技术进步的承诺以及他在塑造美国军事战略方面的巨大影响力。

---

## 98. 蛋白质设计工具能解决蛇毒血清短缺问题吗？

**原文标题**: Will protein design tools solve the snake antivenom shortage?

**原文链接**: [https://www.owlposting.com/p/will-protein-design-tools-solve-the](https://www.owlposting.com/p/will-protein-design-tools-solve-the)

本文深入探讨了蛇抗蛇毒血清生产的复杂性，以及利用蛋白质设计工具来解决当前短缺和无效问题的潜力。作者强调了严峻的形势：蛇咬伤每年导致数万人死亡，数十万人残疾，但抗蛇毒血清通常价格昂贵、稀缺，甚至存在欺诈行为。

一个重大挑战是蛇毒异质性，它因蛇科、物种、种群甚至单条蛇的生命周期而异，并受到饮食等因素驱动。这使得制造有效的抗蛇毒血清变得极其复杂。目前的抗蛇毒血清是通过将毒液注入动物体内并收获由此产生的抗体而生产的。理想情况下，抗蛇毒血清应与特定的毒液成分相匹配，但这通常是不切实际的，导致治疗效果不佳，尤其是在蛇种多样的地区。

文章随后探讨了使用蛋白质设计工具（如贝克实验室开发的RFDiffusion）来创建合成蛋白质的想法，这些蛋白质可以结合并中和蛇毒毒素。这种方法有可能创造出更广泛有效的抗蛇毒血清，克服了传统方法的局限性，传统方法依赖于针对特定毒液成分定制的动物源抗体。文章建议从单价抗蛇毒血清转向多价抗蛇毒血清，将抗蛇毒血清组合在一起，以便更有效地进行治疗。

虽然前景广阔，但作者承认，要创造出针对任何任意毒液的结合剂，仍有大量工作要做，并质疑何时能实现这一目标。文章强调需要更多的研究和开发，以解决蛇毒的复杂性，并改进抗蛇毒血清的生产和分销。

---

## 99. 幽灵学生正在给加州大学带来问题。

**原文标题**: Ghost students are creating problems for California colleges

**原文链接**: [https://www.sfgate.com/bayarea/article/ghost-students-creating-problem-calif-colleges-20311708.php](https://www.sfgate.com/bayarea/article/ghost-students-creating-problem-calif-colleges-20311708.php)

**摘要：**

旧金山纪事报（SFGate）上的文章《幽灵学生正给加州大学带来问题》详细描述了社区大学学生注册但从不上课，从而产生“幽灵学生”这一日益严重的问题。这种虚假注册对大学产生多方面的负面影响。

首先，它夸大了入学人数，而入学人数通常用于确定州政府的拨款。大学会为从未真正接受教育的学生获得资金，从而将资源从那些积极上学的学生那里转移开。

其次，这些幽灵学生可能会为试图注册热门课程的真正学生造成瓶颈。座位被从未露面的学生占据，阻止了其他人选修他们需要的课程。

该文章将这种现象归因于诸如在线注册的便利以及学生作为备用计划注册但不退学等因素。加州旨在扩大高等教育机会的免费社区大学项目加剧了这个问题。虽然这些项目旨在使学生受益，但它们无意中激励了注册而没有承诺。

大学正在努力解决这个问题。一些学校正在实施更严格的退学政策，并积极联系未上课的学生。然而，文章强调了在可访问性与确保入学人数准确反映实际学生参与度之间取得平衡的挑战。这个问题破坏了加州社区大学系统的效率和有效性，因此需要一个全面的解决方案。

---

## 100. 谷歌将支持三项新的核能项目

**原文标题**: Google to back three new nuclear projects

**原文链接**: [https://www.esgtoday.com/google-to-back-three-new-advanced-nuclear-projects/](https://www.esgtoday.com/google-to-back-three-new-advanced-nuclear-projects/)

2025年5月，谷歌宣布与Elementl Power合作，投资三个先进核能项目，每个项目发电能力至少为600兆瓦。此举旨在帮助谷歌实现其雄心勃勃的无碳能源目标，包括到2030年实现净零排放并全天候使用无碳能源。由于数据中心电力需求的增长超过了其目前的Renewable能源努力，谷歌的排放量一直在增加。

这项新协议是继之前与Kairos Power的核能合作之后达成的，也符合谷歌与Meta和其他公司共同承诺到2050年将全球核能产能增加两倍的目标。谷歌认为先进核能技术是一种可靠的、提供基础负荷的、全天候能源，对于加强电网以及支持人工智能和美国创新至关重要。

Elementl Power成立于2023年，旨在使用下一代技术，到2035年在美国上线超过10吉瓦的核电。他们强调有必要进行此类合作以调动新核能项目的资金，并提供安全、经济、清洁的基础负荷电力，以帮助企业实现净零目标。

---

