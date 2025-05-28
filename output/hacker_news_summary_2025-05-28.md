# Hacker News 热门文章摘要 (2025-05-28)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Show HN: 我用 Rust 重写了我的 Mac Electron 应用

**原文标题**: Show HN: I rewrote my Mac Electron app in Rust

**原文链接**: [https://desktopdocs.com/?v=2025](https://desktopdocs.com/?v=2025)

Desktop Docs：一款利用人工智能提供高级图像和视频搜索功能的Mac应用程序。它不仅分析文件名，还分析文件内容，允许用户使用自然语言描述或参考图像进行搜索。该应用专为视频编辑、摄影师和社交媒体经理等需要快速查找大型媒体库中特定文件的专业人士设计。

主要功能包括基于内容的匹配、图像相似度搜索、重复检测和跨格式支持。所有处理都在用户的Mac本地进行，确保隐私并无需上传到云端。该应用支持多种图像和视频格式，包括HEIC、JPG、PNG、GIF、BMP、WEBP、MP4、AVI、MOV、MKV和WEBM。

Desktop Docs需要配备Apple Silicon（M1、M2或M3）的Mac，一次性购买价格为99美元，无需订阅。它旨在帮助用户更快地查找文件，减少管理工作，并将数字混乱转化为有组织的知识库。用户评价强调了节省时间和改进文件组织。该应用程序可索引无限文件，允许在各种文档类型中进行智能搜索，并支持快速编辑。

---

## 2. 编译器探索器与永恒链接的承诺

**原文标题**: Compiler Explorer and the Promise of URLs That Last Forever

**原文链接**: [https://xania.org/202505/compiler-explorer-urls-forever](https://xania.org/202505/compiler-explorer-urls-forever)

本文详细介绍了保存Compiler Explorer链接的历史和即将面临的挑战。最初，该服务直接将编译器状态存储在URL中，但这变得笨拙。随后切换到谷歌的goo.gl链接缩短服务，但这在Stack Overflow禁止缩短链接时产生了问题。作为一种变通方法，实施了一个复杂的重定向系统，最终导致将状态存储在S3中，并由DynamoDB管理缩短的哈希URL。该系统包括对缩短链接中的亵渎行为进行幽默的检查，添加额外数据直到生成干净的哈希值。

现在核心问题是谷歌的goo.gl服务将于2025年8月关闭。尽管承诺永久性，但这些基于goo.gl的链接，包括godbolt.org/g/abc123形式的Compiler Explorer链接，将不再起作用。作者致力于“永久有效的URL”，一直在积极抓取互联网以抢救和编目这些链接，创建一个数据库以取代对goo.gl的依赖。

本文强调了依赖第三方服务作为关键基础设施的危险，并强调了拥有整个技术栈对于长期稳定性的重要性。作者鼓励用户重新访问旧的Compiler Explorer链接，以确保它们被添加到救援数据库中，从而将它们作为编程历史的宝贵组成部分保存下来。

---

## 3. Show HN: Tesseral – 开源认证

**原文标题**: Show HN: Tesseral – Open-Source Auth

**原文链接**: [https://github.com/tesseral-labs/tesseral](https://github.com/tesseral-labs/tesseral)

Tesseral：面向 B2B SaaS 应用的开源多租户身份验证基础设施。它是一个 API 优先的服务，提供一套全面的功能来管理用户身份验证、授权和访问控制，且不受特定语言或框架的限制。

主要功能包括：可定制的托管登录页面、B2B 多租户支持、用户模拟、客户自助配置、魔法链接、社交登录、SAML & SCIM 支持、RBAC、MFA、密码密钥/WebAuthn、验证器应用、API 密钥管理、用户邀请和 Webhooks。这些功能使开发人员能够轻松地将安全可靠的身份验证功能添加到他们的 B2B 应用程序中。

Tesseral 提供托管服务 (console.tesseral.com)，也可进行自托管。开发者可以通过阅读文档 (tesseral.com/docs) 并使用 React、Express、Flask 和 Golang 的 SDK 来开始使用。提供了一个使用 React 的前端集成示例，以及一个使用 Flask 的后端示例，演示了如何使用 Tesseral 对请求进行身份验证并提取用户详细信息。

该项目采用 MIT 许可证，欢迎贡献，但强调以谨慎的态度合并更改。安全漏洞应直接报告至 security@tesseral.com。Tesseral 鼓励通过 LinkedIn、X (Twitter)、新闻通讯、博客以及与创始人的直接联系来进行社区互动。Tesseral 由一家位于旧金山的初创公司管理，主要技术负责人为 Ulysse Carion、Blake Williams 和 Dillon Nys。

---

## 4. 戈壁石墙之谜

**原文标题**: The mysterious Gobi wall uncovered

**原文链接**: [https://phys.org/news/2025-05-secrets-mysterious-gobi-wall-uncovered.html](https://phys.org/news/2025-05-secrets-mysterious-gobi-wall-uncovered.html)

本文探讨了耶路撒冷希伯来大学考古学家及其合作者对戈壁长城的新研究。戈壁长城是蒙古国一处大型边境系统中的一段，长321公里。这项发表在《土地》（Land）杂志上的研究揭示了长城的起源、功能和历史背景。

该研究表明，长城主要由党项族在西夏王朝（公元1038-1227年）时期建造，挑战了长城仅作为防御结构的观点。研究人员认为，它具有多重功能，包括边界划分、资源管理和巩固皇权。证据还表明，从公元前2世纪到公元19世纪期间，该长城曾被周期性地使用，突显了其长期的战略意义。

长城的建造使用了当地材料，如夯土，并以石头和木材加固。其路线是根据水和木材等资源的可用性以及利用自然地理特征的堡垒和驻军的位置进行战略性选择的。

Shelach-Lavi教授强调，戈壁长城是管理移动、贸易和领土控制的“动态机制”。这些发现为了解中世纪帝国中环境适应与国家权力之间的关系提供了见解，并对理解古代基础设施具有重要意义。

---

## 5. 谁在乎的时代

**原文标题**: The Who Cares Era

**原文链接**: [https://dansinker.com/posts/2025-05-23-who-cares/](https://dansinker.com/posts/2025-05-23-who-cares/)

在“谁在乎的时代”中，Dan Sinker哀叹内容创作中日益增长的冷漠和质量下滑，这在很大程度上是由人工智能的兴起所推动的。他指出，一些例子如人工智能生成的新闻报纸增刊充斥着捏造的信息，却在无人注意或关心的情况下被发表，以及一个潜在的播客系列被简化成通用且可抛弃的东西。

Sinker认为，人工智能在某些情况下虽然有用，但经常被用来生产平庸的内容，因为对许多不在乎的人来说，“足够好”是可以接受的。他将这一趋势与更广泛的文化转变联系起来，即人们的注意力持续时间短，内容被设计成被动消费。

他进一步批评了政府和机构中普遍存在的漠不关心态度，并提到了特朗普政府和埃隆·马斯克的行为，这些行为将削减成本置于质量和专业知识之上。

尽管处境令人沮丧，Sinker还是发出了行动号召。他鼓励读者积极关心，创作真实且不完美的作品，支持那些正在创造真实事物的人，并全神贯注地参与内容。他强调了作为人类、保持不完美的重要性，并通过优先考虑真正的努力和参与来对抗平庸的浪潮。最终，在一个以冷漠为特征的时代，关心是最激进和最必要的行为。

---

## 6. 收到华夫饼屋的停止函

**原文标题**: Getting a Cease and Desist from Waffle House

**原文链接**: [https://www.jack.bio/blog/wafflehouse](https://www.jack.bio/blog/wafflehouse)

2024年9月末，当飓风威胁佛罗里达州时，作者对华夫饼屋的网站进行了逆向工程，创建了一个实时地图，追踪餐厅关闭情况，这是一个美国联邦紧急事务管理局（FEMA）用来衡量灾害严重程度的非官方“华夫饼屋指数”。 作者发现华夫饼屋使用了Next.js和React Server Components，找到了一个包含位置数据的JSON文件，然后使用Python对其进行抓取和处理，从而构建了该指数。

在发布网站（wafflehouseindex[.]org）并在推特上发布相关信息后，作者收到了华夫饼屋官方账号的关注，对方声明该信息不准确。 在政治评论员弗兰克·伦茨分享该网站后，人们的兴趣激增，但华夫饼屋迅速删除了他的推文并屏蔽了作者。

此后不久，作者收到了华夫饼屋发出的停止侵权通知，理由是未经授权使用其商标。 尽管作者做出了幽默的回应（“带着尊重和糖浆”），但还是照做了并关闭了网站。 虽然最初希望得到官方合作，但作者最终被无视了。

尽管寿命短暂，但作者珍视这次为乐趣而构建项目的经历，强调了数据操作创造有意义项目的力量。 作者还感谢华夫饼屋的良好体育精神，尽管存在商标侵权和数据抓取行为。

---

## 7. 喷灯理论：宇宙结构形成的新模型

**原文标题**: The Blowtorch Theory: A new model for structure formation in the universe

**原文链接**: [https://theeggandtherock.com/p/the-blowtorch-theory-a-new-model](https://theeggandtherock.com/p/the-blowtorch-theory-a-new-model)

朱利安·高夫的文章介绍了“喷灯理论”，作为宇宙结构形成的另一种模型，挑战了主流的Lambda冷暗物质（ΛCDM）模型。ΛCDM模型依赖于引力和理论上的“暗物质”来解释宇宙网的形成——一个由密集星系团通过丝状结构连接，周围环绕着巨大空洞的网络。然而，ΛCDM难以解释詹姆斯·韦伯太空望远镜观测到的成熟星系的快速出现。

喷灯理论提出，早期持续的超大质量黑洞喷流通过在早期宇宙中开辟空洞和铺设磁场，积极地塑造了宇宙。这些喷流创造了低压腔，随着时间的推移，这些低压腔膨胀，形成了我们今天观测到的宇宙空洞和丝状结构。

喷灯理论的一个主要优势是不需要暗物质；结构形成可以用喷流和普通物质来解释。该理论得到了近期早期超大质量黑洞、强大喷流以及这些黑洞周围快速星系形成的发现的支持。近期发现的来自早期宇宙的耀变体进一步加强了该理论的预测。

文章强调了20世纪70年代末对宇宙空洞的惊人发现，这些空间区域的密度极低，而最初的宇宙学模型未能预测到这些空洞。ΛCDM的开发是为了解释这些结构，但喷灯理论提供了一个更简单的解释。

---

## 8. 针对隐私币XMR去匿名化攻击的综合分析

**原文标题**: Comprehensive Analysis of De-Anonymization Attacks Against the Privacy Coin XMR

**原文链接**: [https://monero.forex/is-monero-totally-private-a-comprehensive-analysis-of-de-anonymization-attacks-against-the-privacy-coin/](https://monero.forex/is-monero-totally-private-a-comprehensive-analysis-of-de-anonymization-attacks-against-the-privacy-coin/)

本文全面分析了试图去匿名化门罗币（XMR）交易的尝试，门罗币是一种注重隐私的加密货币。文章强调，尽管门罗币旨在通过环签名、隐形地址和机密交易等功能实现不透明性，但各种实体一直在试图绕过其隐私保护。

文章考察了若干尝试，包括Chainalysis和CipherTrace开发的利用交易时间和网络分析的工具，这些工具取得了有限的、概率性的成功，尤其是在门罗币与隐私性较差的系统交互时。学术研究发现门罗币早期版本环签名实现中存在漏洞，这些漏洞随后得到了修复。一些公司还探索了通过交易所数据和IP地址进行链下数据关联，取得了一定的成功，但依赖于用户的操作安全。

美国国税局甚至悬赏破解门罗币的隐私，但没有公开证据表明有人成功。与此相反，门罗币社区积极致力于通过诸如“破解门罗币”系列等举措来加强隐私保护，这些举措旨在识别和缓解漏洞。

文章总结认为，尽管尝试众多，门罗币的隐私保护仍然具有韧性。虽然某些方法利用了弱点或以概率的方式降低了匿名性，但没有一种方法能够实现可靠、广泛的去匿名化。门罗币社区对其隐私功能的持续开发和加强确保了其作为注重隐私用户的首选地位。

---

## 9. Show HN: Loodio 2 – 简单可充电的浴室隐私设备

**原文标题**: Show HN: Loodio 2 – A Simple Rechargable Bathroom Privacy Device

**原文链接**: [https://loodio.com/](https://loodio.com/)

Loodio推出Loodio 2，一款简易可充电的浴室隐私设备。旨在帮助用户在私密时刻放松身心。该设备配有4GB存储卡，预装100首歌曲，并拥有长达一周的电池续航。售价149美元，包含免费国际运送。

---

## 10. 作为一名开发者，我最重要的工具是笔和笔记本。

**原文标题**: As a developer, my most important tools are a pen and a notebook

**原文链接**: [https://hamatti.org/posts/as-a-developer-my-most-important-tools-are-a-pen-and-a-notebook/](https://hamatti.org/posts/as-a-developer-my-most-important-tools-are-a-pen-and-a-notebook/)

文章《作为开发者，我最重要的工具是笔和笔记本》认为，尽管复杂的数字工具很普及，但简单的笔和笔记本对于开发者来说仍然至关重要。

作者认为，与直接在电脑上工作相比，使用纸笔可以进行更深入的思考和问题解决。他们发现，手绘图表、勾勒代码结构和做笔记有助于更好地理解复杂问题。这个过程可以进行更抽象的思考，并避免过早地陷入实现细节。

此外，作者强调了离线头脑风暴的好处。在没有通知和代码编辑器的干扰下，开发者可以完全专注于产生想法和探索不同的解决方案。他们认为这会带来更具创造性和经过深思熟虑的方法。

笔记本还可以作为想法、笔记和观察的重要存储库，可以轻松地重新访问和完善。与容易丢失或分散在不同应用程序中的数字笔记不同，物理笔记本为开发人员的思维过程提供了有形的、有组织的记录。

最后，文章强调笔和笔记本是思考的工具，而不仅仅是记录的工具。他们鼓励一种更深思熟虑的开发方法，从而产生更好的代码和更有效的问题解决。

---

## 11. XAI将向Telegram支付3亿美元，以将Grok整合到该聊天应用中。

**原文标题**: XAI to pay Telegram $300M to integrate Grok into the chat app

**原文链接**: [https://techcrunch.com/2025/05/28/xai-to-invest-300m-in-telegram-integrate-grok-into-app/](https://techcrunch.com/2025/05/28/xai-to-invest-300m-in-telegram-integrate-grok-into-app/)

Telegram与埃隆·马斯克的xAI公司合作，将xAI的聊天机器人Grok集成到Telegram平台一年。xAI将支付Telegram 3亿美元的现金和股权作为分销协议费用。Telegram还将获得通过该应用程序购买的xAI订阅收入的50%。

虽然Grok之前仅供Telegram高级用户使用，但这项协议表明它可能会向所有用户推广。Pavel Durov在一段视频中展示了Grok在Telegram中的潜力，强调了诸如将Grok置顶聊天、通过搜索栏使用它、以及将其用于写作建议、内容总结、创建贴纸、回答商业问题和协助审核等功能。这与Meta将Meta AI集成到Instagram和WhatsApp的做法类似。

文章还包含TechCrunch Sessions: AI的宣传材料，这是一个即将举行的活动，届时将有来自领先人工智能公司的演讲者。该活动计划于2025年6月5日在加利福尼亚州伯克利举行。

---

## 12. 数学虚构

**原文标题**: Mathematical Fiction

**原文链接**: [https://kasmana.people.charleston.edu/MATHFICT/default.html](https://kasmana.people.charleston.edu/MATHFICT/default.html)

数学虚构作品主页，由查尔斯顿学院的Alex Kasman策划，是一个致力于记录数学与虚构作品交集的综合数据库。该网站旨在为对包含数学概念或以数学家为主角的故事、小说、戏剧、电影和漫画书感兴趣的读者提供资源。

该网站拥有超过一千条条目的收藏，并允许用户通过各种方法浏览数据库。用户可以查看按作者、标题或出版日期排序的完整列表。他们还可以按类型、主题、母题或媒介浏览，或者使用搜索功能来查找更具体的条件。一个专门介绍最近添加或修改条目的部分让用户及时了解最新信息。Kasman还为寻求指导的人提供个人推荐。

该网站鼓励用户参与，邀请反馈和建议。此外，它还提供指向讨论数学虚构作品的文章的链接，从而丰富了用户体验，而不仅仅是列出示例。本质上，数学虚构作品主页是对于任何有兴趣探索数学在虚构叙事中表现的人来说，都是一个有价值且易于访问的资源。

---

## 13. FlowTSE：基于流匹配的目标说话人提取

**原文标题**: FlowTSE: Target Speaker Extraction with Flow Matching

**原文链接**: [https://arxiv.org/abs/2505.14465](https://arxiv.org/abs/2505.14465)

这篇arXiv文章 (arXiv:2505.14465) 介绍了FlowTSE，一种基于条件流匹配的新型目标说话人提取 (TSE) 方法。这篇题为“FlowTSE：基于流匹配的目标说话人提取”的论文由Aviv Navon、Aviv Shamsian、Yael Segal-Feldman、Neta Glazer、Gil Hetz 和 Joseph Keshet 撰写，并已投稿至 InterSpeech 2025。

其解决的核心问题是，利用参考注册样本从混合音频信号中分离出特定说话人的声音。尽管现有的 TSE 方法主要为判别式，但本文探索了生成式方法，强调了它们的潜力，但也指出了它们在复杂性和计算开销方面的局限性。

FlowTSE 旨在通过一种简单有效的条件流匹配方法来克服这些局限性。该模型以注册音频和混合语音的梅尔频谱图表示作为输入，目标是提取目标说话人的干净语音。

此外，该论文还介绍了一种新型声码器，它以混合信号的复数短时傅里叶变换 (STFT) 为条件，以改善相位估计，这对于高质量音频重建至关重要。在标准 TSE 基准上的实验结果表明，FlowTSE 的性能与强大的基线方法相当或超过。

本质上，FlowTSE 提出了一种计算效率高且准确的目标说话人提取生成模型，利用条件流匹配和一种新型声码器来增强相位重建。

---

## 14. LLM代码生成，Git Worktrees与Tmux并行提速

**原文标题**: LLM Codegen go Brrr – Parallelization with Git Worktrees and Tmux

**原文链接**: [https://www.skeptrune.com/posts/git-worktrees-agents-and-tmux/](https://www.skeptrune.com/posts/git-worktrees-agents-and-tmux/)

本文探讨如何利用 Git 工作区和 Tmux 并行化来加速 LLM（大型语言模型）的代码生成。核心思想是利用 Git 工作区从同一个 Git 仓库创建多个隔离的工作环境，从而允许独立的 LLM 代码生成任务并发运行，互不干扰。Tmux 用于管理和监控这些并行进程。

文章可能概述了这种方法的优势，例如缩短代码生成的总时间以及有效利用计算资源。它可能还描述了设置过程，包括：

*   **创建 Git 工作区：** 解释如何从主 Git 仓库创建和管理多个工作区。每个工作区包含一个单独的文件副本，从而允许并行开发/代码生成。
*   **利用 Tmux：** 展示如何使用 Tmux 创建多个终端会话，每个 Git 工作区对应一个会话，并在每个会话中运行 LLM 代码生成任务。这允许监控和控制每个单独的进程。
*   **可能的脚本或工作流程：** 可能包含示例命令或工作流程，用于自动化创建工作区、Tmux 会话以及执行代码生成脚本。

本质上，本文提倡一种利用 Git 工作区和 Tmux 并行化 LLM 代码生成任务的实用工作流程，从而实现更快、更高效的代码生成。它可能提供了一个用于实施这种并行化策略的实践指南。

---

## 15. 展示 HN：我的 LLM CLI 工具现在可以运行工具了，来自 Python 代码或插件

**原文标题**: Show HN: My LLM CLI tool can run tools now, from Python code or plugins

**原文链接**: [https://simonwillison.net/2025/May/27/llm-tools/](https://simonwillison.net/2025/May/27/llm-tools/)

本文宣布发布 LLM 0.26，这是一个 CLI 工具和 Python 库更新，专注于使大型语言模型能够使用工具。这使得来自 OpenAI、Anthropic、Gemini 等提供商的 LLM 以及来自 Ollama 的本地模型能够访问以外部功能表示的 Python 函数。

主要功能包括：

*   **工具执行：** LLM 现在可以运行从插件安装的工具，或通过命令行上的 `--functions` 选项直接定义的工具。
*   **工具插件：** 该更新引入了一个插件系统，可以轻松地使用新工具扩展 LLM 的功能。作者已经发布了用于简单表达式求值 (llm-tools-simpleeval)、JavaScript 执行 (llm-tools-quickjs)、SQLite 数据库访问 (llm-tools-sqlite) 和远程 Datasette 查询 (llm-tools-datasette) 的插件。
*   **Python API 支持：** Python 库现在支持工具，新的 `model.chain()` 方法旨在处理工具调用请求、执行它们并使用结果再次提示模型，从而实现更复杂的交互。
*   **异步工具支持：** 工具可以是异步函数并并发运行。
*   **模型上下文协议 (MCP) 支持：** 计划与 MCP 集成，以扩大工具来源。

作者解释了为什么此更新花费了时间，强调需要一个抽象层才能跨各种模型工作。他还讨论了“代理”这一话题，并暗示 LLM 0.26 是构建它们的基础。未来的计划包括改进工具执行日志、向更多模型插件添加工具支持以及创建关于编写工具插件的教程。

---

## 16. 平方理论

**原文标题**: Square Theory

**原文链接**: [https://aaronson.org/blog/square-theory](https://aaronson.org/blog/square-theory)

平方理论
平方理论提出了一种概念，即许多令人满意且巧妙的创作，从填字游戏到笑话和品牌名称，都可以通过一个共同的结构来理解：即“平方”。该理论起源于Crosscord填字Discord服务器中的观察，它认为，一个由四个相互关联的元素（顶点）及其之间的关系（边）组成的平方，能够创造一种完整和满足感。

文章解释说，“双重双重”（形成非同义短语的两对同义词）是这种平方结构的例证。 然而，平方理论不仅仅局限于文字游戏，它适用于由明确关系连接的任何四个实体或概念。例子包括填字游戏中的问号提示、成功的品牌名称和精心制作的笑话。

作者认为，正方形是一种特别引人注目的形状，因为它是具有非相邻边的最简单的多边形，从而在相对元素之间建立了一种令人惊讶的联系。 在填字游戏中，平方理论解释了为什么某些主题感觉特别巧妙和紧凑，通常使用揭示线索来完成正方形。 文章将该理论扩展到包括拼字游戏，甚至包括填字游戏网格本身的基本结构，其中每个字母都是由相交的单词组成的正方形的一部分。

最终，作者认为，识别和利用平方结构对于创意人士来说可能是一种有价值的工具，使他们能够在各个领域创造出更令人满意和更具影响力的作品。 通过寻求完成平方，创作者可以挖掘人类满足感和创造力的基本要素。

---

## 17. 关于 JavaScript “工作量证明” 反爬虫系统的一些思考

**原文标题**: A thought on JavaScript "proof of work" anti-scraper systems

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/web/JavaScriptScraperObstacles](https://utcc.utoronto.ca/~cks/space/blog/web/JavaScriptScraperObstacles)

2025年初，克里斯·西本曼在他的博客“Wandering Thoughts”和维基“CSpace”上实施了反爬虫措施，原因是大量爬虫涌入，特别是那些为了LLM训练而抓取数据的爬虫。这些爬虫通常使用旧的浏览器用户代理，尤其是Chrome。这导致使用旧版浏览器的合法用户被屏蔽。

主要问题是如何区分使用旧版浏览器的合法用户和恶意爬虫。如果用户在使用当前浏览器版本的情况下遇到此屏蔽，建议他们联系西本曼，提供其浏览器详细信息和User-Agent字符串。

一个具体问题是archive.today、archive.ph和archive.is等存档网站的行为。这些网站使用与恶意行为者无法区分的方法抓取页面，采用旧的Chrome User-Agent值，使用没有明确标识的广泛分布的IP地址块，有时还会伪造反向DNS条目来模仿Googlebot。西本曼建议使用archive.org，因为它是一个行为更规范的存档爬虫，可以访问他的博客。他对区分合法存档和恶意抓取活动感到沮丧。

---

## 18. 莫尔瓦德搜索

**原文标题**: Mullvad Leta

**原文链接**: [https://leta.mullvad.net](https://leta.mullvad.net)

标题为“Mullvad Leta”的文章可能探讨了Mullvad VPN相关的“Leta”功能或组件。由于缺乏文章实际内容，无法提供确切的摘要。但根据Mullvad VPN的背景以及“Leta”这个名称，我们可以推测并提供一个合理的摘要：

“Mullvad Leta”文章可能详细介绍了Mullvad VPN中一项专注于服务器选择或性能优化的功能或工具。“Leta”在相关语言（可能是瑞典语，鉴于Mullvad的起源）中可能翻译为“搜索”或“查找”，暗示它帮助用户找到最适合其需求的服务器。

文章可能解释Leta的工作原理，并可能概述其用于对服务器进行排名的标准（例如，延迟、速度、负载）。它可能会描述Leta中提供的不同过滤选项，允许用户指定所需的服务器位置或协议（例如，WireGuard、OpenVPN）。

此外，文章可能讨论使用Leta的好处，例如提高连接速度、更稳定的连接以及更容易访问特定区域的内容。它可能还会解决用户在使用Leta时可能遇到的故障排除提示或常见问题，并提供解决方案。

最终，文章可能旨在教育Mullvad VPN用户了解Leta功能，并鼓励他们使用它以获得更好、更优化的VPN体验。

---

## 19. 印度尼西亚海底发现直立人，最新考古发现

**原文标题**: Homo erectus from the seabed, new archaeological discoveries in Indonesia

**原文链接**: [https://www.universiteitleiden.nl/en/news/2025/05/homo-erectus-from-the-seabed-new-archaeological-discoveries-in-indonesia](https://www.universiteitleiden.nl/en/news/2025/05/homo-erectus-from-the-seabed-new-archaeological-discoveries-in-indonesia)

在印度尼西亚爪哇岛附近的马都拉海峡的考古发现，出土了36种脊椎动物的化石遗骸，其中包括直立人的头骨碎片，其年代可追溯到大约14万年前。 这是首次在巽他陆架海床上发现此类化石，巽他陆架是一片广阔的低地，在海平面较低的时期连接了许多现在的印度尼西亚岛屿。

在莱顿大学考古学家哈罗德·伯格胡伊斯（Harold Berghuis）的带领下，该研究表明，爪哇直立人沿着主要河流分散在巽他陆架的低地上，在那里他们可以获得食物资源。 这些发现表明，巽他陆架的直立人积极捕猎大型牛科动物，这在早期爪哇人群中未曾见过，但在亚洲大陆更为现代的人类物种中已知，这表明不同人族群体之间可能存在接触或基因交流。

这项发表在《第四纪环境与人类》上的研究，全面展示了被淹没的巽他陆架生态系统，展现了一幅类似于非洲热带草原的景象，拥有多样化的动物群，包括大象、犀牛、河马、科莫多巨蜥和河鲨。这些动物曾在古代巽他陆架上繁荣生长。

这些发现为东南亚的生物多样性提供了重要的见解，并表明现在的岛屿曾经是山脉。化石收藏品保存在印度尼西亚万隆的地质博物馆，并计划举办展览。这项发现是独一无二的，因为以前从未在该地区发现过化石。

---

## 20. 一个高效单体仓库的要素

**原文标题**: The Ingredients of a Productive Monorepo

**原文链接**: [https://blog.swgillespie.me/posts/monorepo-ingredients/](https://blog.swgillespie.me/posts/monorepo-ingredients/)

本文旨在指导工程师构建高效的单体仓库环境。文章强调，主要目标应该是保持一致性、组织协调性和共享工具，而不是仅仅复制像谷歌这样的科技巨头的成功案例。一个核心原则是优化操作，使其复杂度为O(change)而非O(repo)，意味着操作应该随着变更的大小而扩展，而不是整个仓库的大小。

文章涵盖了源代码控制等关键方面，最初提倡使用Git，但也承认其在大规模应用中的局限性，并建议使用诸如Forking Git/Mercurial或开发自定义解决方案等替代方案，这些方案允许部分仓库检出和虚拟文件系统。

关于构建，文章建议尽可能坚持使用单一语言，并在可行的情况下尽可能利用现有的特定于语言的构建工具。单体仓库中构建系统的关键要求包括高效的目标构建和识别受更改影响的目标，从而催生了“目标决定器”的创建。

测试应该智能化，包含自动重试，并根据变更范围选择性地运行测试。这可以最大限度地减少不稳定性并提高可靠性。

持续集成(CI)应该基于变更确定必要的构建产物和验证。文章还讨论了集成已验证变更的合并队列，重点是平衡吞吐量、正确性和尾部延迟。探索了不同的落地策略，例如批量变更。文章最后强调，保持CI的快速对于平滑的合并队列至关重要，并突出了速度和彻底性之间的权衡。

---

## 21. Show HN: Wetlands – 一个轻量级的 Python 库，用于管理 Conda 环境

**原文标题**: Show HN: Wetlands – a lightweight Python library for managing Conda environments

**原文链接**: [https://arthursw.github.io/wetlands/0.2.0/](https://arthursw.github.io/wetlands/0.2.0/)

Wetlands 是一个 Python 库，旨在简化 Conda 环境的管理，实现依赖隔离和嵌入式执行。它允许开发者按需创建、配置和执行隔离的 Conda 环境中的代码，使其适用于构建插件系统或集成外部模块，而无需担心依赖冲突。

主要特性包括：

*   **自动环境管理：** 根据需要创建和配置 Conda 环境。
*   **依赖隔离：** 在隔离的环境中安装依赖项，避免冲突。
*   **嵌入式执行：** 在这些隔离的环境中运行 Python 函数。
*   **Pixi & Micromamba 支持：** 利用 pixi 或 micromamba 实现快速轻量级的环境处理。

该库提供两种主要的交互方式：简化执行（使用 `env.importModule` 和 `env.execute` 在环境中无缝调用函数）和手动控制（使用 `env.executeCommands` 运行特定命令和管理进程间通信）。

Wetlands 通过 `pip install wetlands` 安装。一个最小示例展示了如何创建环境、安装 NumPy、导入模块、在环境中执行函数以及清理环境。该库采用 MIT 许可证，由雷恩的 Inria 开发。该项目的文档和源代码可在 GitHub 上找到。

---

## 22. 关卡设计书

**原文标题**: The Level Design Book

**原文链接**: [https://book.leveldesignbook.com](https://book.leveldesignbook.com)

《关卡设计书籍》

这是一份非常简短的名为《关卡设计书籍》的文档草稿。它仅说明了两件事：

1. **标题：** 关卡设计书籍
2. **内容：** 内容包含短语“下一步，什么是关卡设计？”和“上次更新于4个月前”。

因此，总结是：

《关卡设计书籍》是一份文档，上次更新于4个月前，似乎是对关卡设计的介绍。内容直接引导读者提出问题：“什么是关卡设计？”，表明这是要讨论的主题。“下一步”暗示该书可能会超越仅仅定义关卡设计。

---

## 23. DWARF作为一种共享的逆向工程格式

**原文标题**: DWARF as a Shared Reverse Engineering Format

**原文链接**: [https://lief.re/blog/2025-05-27-dwarf-editor/](https://lief.re/blog/2025-05-27-dwarf-editor/)

Romain Thomas 的这篇文章介绍了 DWARF 作为逆向工程的通用格式，以克服 IDA 和 Ghidra 等不同逆向工程工具之间的不兼容性问题。 DWARF 传统上用于调试信息，非常适合存储逆向工程数据，例如结构体和函数名称。

这篇文章重点介绍了一个扩展的 LIEF API，该 API 提供 Python、Rust 和 C++ 版本，简化了使用 LLVM 后端创建 DWARF 文件的过程。 LIEF 提供了对 LLVM 低级 API 的更高级别抽象，降低了 DWARF 格式的复杂性。

作者随后介绍了 Ghidra 和 Binary Ninja 的插件，这些插件可以将二进制分析数据导出为 DWARF 格式。 虽然 Binary Ninja 有一个官方的 DWARF 导出器（早期版本存在局限性，例如导出堆栈变量），但作者的自定义插件解决了特定的需求，例如符号化 QBDI 跟踪。 Ghidra 插件允许用户通过 GUI 或无头 Java 脚本将程序信息导出到 DWARF 中。 作者目前没有计划支持 IDA，但对此持开放态度。

这篇文章提供了一个使用 DWARF 共享逆向工程结果的实际示例，包括为特定二进制文件生成的 DWARF 文件。 作者强调 DWARF 导出功能尚处于早期开发阶段，并计划在未来增加对导出注释的支持。

---

## 24. 设计科学思维的工具

**原文标题**: Designing Tools for Scientific Thought

**原文链接**: [https://www.forester-notes.org/tfmt-0001/index.xml](https://www.forester-notes.org/tfmt-0001/index.xml)

Jon Sterling 的笔记探讨了“科学思维工具”的设计，特别是针对数学科学。他重点关注信息数据模型和工具的需求，这些模型和工具需要记录和促进科学思维。

“科学思维工具”促进科学思想的发展和互联，用于创作、出版、教学、学习和维护常青笔记。现有工具分为交互式证明助手和文本创作/出版工具，如 LaTeX。

“常青笔记”的概念，灵感来自 Andy Matuschak，强调永久的、不断发展的、跨项目的笔记。原子性至关重要：每个笔记应捕获一个想法，通过其内容和链接笔记可以理解。Sterling 反对传统数学写作缺乏原子性，提倡显式语境而非隐式语境。实现原子性涉及避免自由变量，通过链接偏向于显式依赖关系，并确保符号可以通过链接解码。

虽然 Matuschak 偏爱关联本体，但 Sterling 认为数学知识需要从一开始就进行分层组织，以区分假设和结论。然而，可以在同一节点网络上施加多个分层结构，从而创建不同的“叙述”。因此，界面应支持导航多个父/邻居关系。他提倡相对扁平的结构，以避免过早的复杂性。

Sterling 比较了文档标记中的“绝对”（HTML、LaTeX）和“相对”层次结构模型。他认为，相对层次结构，其中节级别由上下文决定，更适合重新语境化，这是流畅科学媒体的一个关键方面。此外，他更喜欢显式的层次结构，即标记语言的语法树结构诱导层次结构，而不是在许多文档标记语言中发现的隐式结构。

他引入了“常青笔记森林”的概念：一个可以出现和发展多个分层结构的集合。单个笔记被认为是森林中的“树”。他根据包含关系定义了树的“范围”。最后，他区分了常青笔记森林中的“作者”和“贡献者”，强调作者身份意味着责任和认可，这可能不适用于其他人对树的后续重新语境化。

---

## 25. 在预启动环境中协商PoE+供电

**原文标题**: Negotiating PoE+ Power in the Pre‑Boot Environment

**原文链接**: [https://roderickkhan.com/posts/2025-05-16-poe-uefi-solution](https://roderickkhan.com/posts/2025-05-16-poe-uefi-solution)

罗德里克回顾了他2015年的一个项目，该项目涉及使用PoE供电的x86计算机进行数字标牌。挑战在于为这些需要23W功率的计算机供电，并使用PoE+，但一些网络交换机由于需要超过15.4W的LLDP数据链路层分类而无法提供。计算机无法完全启动以从操作系统发送LLDP数据包，形成了一个两难境地。

解决方案是在操作系统加载之前协商PoE+电源，利用UEFI固件访问网络堆栈的能力。最初尝试构建自定义BIOS，但该项目转向开发UEFI应用程序。

罗德里克请来固件工程师Piotr Król，他创建了PoePwrNegotiator，这是一个用C语言编写的UEFI应用程序，用于发送LLDP-MED数据包以请求必要的电源。该应用程序在操作系统之前运行，解决了电源问题。该应用程序已部署和测试，现在在GitHub上以MIT许可证开源。作者希望PoePwrNegotiator可以帮助其他人在x86系统中面临类似的PoE电源协商挑战。他对Carlos和Piotr为项目成功做出的重要贡献表示特别感谢。

---

## 26. 妈，你看，没气泡：为Llama-1B设计一个低延迟的巨内核

**原文标题**: Look Ma, No Bubbles: Designing a Low-Latency Megakernel for Llama-1B

**原文链接**: [https://hazyresearch.stanford.edu/blog/2025-05-27-no-bubbles](https://hazyresearch.stanford.edu/blog/2025-05-27-no-bubbles)

本文介绍了一种“巨内核”（megakernel）方法，旨在显著降低在GPU上运行开源语言模型Llama-1B的延迟。作者发现，现有的LLM推理引擎（如vLLM和SGLang）由于每次模型前向传递（例如，RMS规范化、注意力）都需要启动许多小型内核，导致GPU带宽利用率仅约为50%。这些内核的设置和拆卸过程会阻碍内存加载，而内存加载是Llama-1B等内存密集型工作负载的关键瓶颈。

为了解决这个问题，他们将整个Llama-1B前向传递合并为一个“巨内核”，消除了内核边界，并实现了更好的内存加载流水线。这种方法在H100 GPU上实现了78%的内存带宽利用率，并比现有系统提高了1.5倍的性能。

作者详细介绍了他们如何实现这一点：

*   **融合大量操作：** 使用一个GPU上的解释器，该解释器为每个流式多处理器（SM）执行一系列指令。
*   **共享硬件资源：** 分页共享内存，即使之前的指令仍在完成，也能为后续指令高效加载权重。
*   **高效同步：** 使用计数器系统来显式管理巨内核中的数据依赖关系，从而消除传统内核之间的自动同步。

他们的巨内核在H100上实现了亚毫秒级的前向传递，在B200上实现了亚680微秒级的前向传递，展示了显著的延迟降低。对B200前向传递运行时的分析揭示了关键瓶颈：存储/加载激活值、矩阵向量计算、等待权重、同步开销和设置开销。他们开源了他们的代码，供其他人探索和改进。

---

## 27. 使用Tiki的编程基础

**原文标题**: Programming Basics with Tiki

**原文链接**: [https://tiki.li/](https://tiki.li/)

无法访问文章链接。

---

## 28. Windows注册表探险#7：攻击面分析

**原文标题**: The Windows Registry Adventure #7: Attack surface analysis

**原文链接**: [https://googleprojectzero.blogspot.com/2025/05/the-windows-registry-adventure-7-attack-surface.html](https://googleprojectzero.blogspot.com/2025/05/the-windows-registry-adventure-7-attack-surface.html)

Mateusz Jurczyk的这篇博文深入探讨了Windows注册表中的安全漏洞，强调了其作为特权提升攻击目标的吸引力。注册表是一个位于核心内核中的本地攻击面，用C语言编写，使其容易受到逻辑和内存安全漏洞的影响。其复杂性，加上其在管理敏感系统信息（密码、权限）方面的作用，为代码执行和仅数据攻击创造了潜在可能。

Jurczyk强调了注册表积极的自我修复和恢复机制，虽然有利于系统可靠性，但也增加了攻击面，因为错误处理逻辑可能会引入不一致性。该博文详细介绍了注册表中发现的特定类型的漏洞，包括hive和池内存损坏、信息泄露、竞争条件、逻辑漏洞以及进程间攻击。一个关键的关注领域是安全描述符的手动引用计数，由于不受信任的初始值、整数溢出和特殊键类型的处理不当，容易出错，可能导致释放后使用漏洞。虽然现在引用计数增加已得到保护，但减少可能并非如此，从而形成持久的攻击面。

---

## 29. 椅子，椅子，椅子

**原文标题**: Chairs, Chairs, Chairs

**原文链接**: [https://www.parliament.uk/about/living-heritage/building/cultural-collections/historic-furniture/the-collection/chairs-chairs-chairs/](https://www.parliament.uk/about/living-heritage/building/cultural-collections/historic-furniture/the-collection/chairs-chairs-chairs/)

英国议会网站的文章《椅子，椅子，椅子》重点介绍了议会收藏的大量且种类繁多的椅子，强调了它们在威斯敏斯特宫和其他议会建筑中的历史意义、艺术价值和实用功能。 该系列跨越几个世纪，展示了设计、工艺和装饰技术的演变。

这篇文章指出，许多椅子是专门为议会用途定制的，反映了不断变化的政治格局和仪式需求。 这些椅子不仅仅是功能性的；它们是英国历史上重要事件和人物的真实联系。提到的例子可能包括议长座椅、用于皇家场合的礼仪椅以及在委员会会议室中使用的椅子。

此外，这篇文章强调了保护和维护这些历史文物完整性的重要性。 议会致力于确保这些椅子保持可用性，同时为子孙后代保留其历史价值。 这涉及在议会大楼内进行仔细的修复、重新装饰和环境控制。

本质上，这篇文章将椅子收藏视为宝贵的历史和文化资产，提供了对议会历史、英国设计以及几代工匠技能的见解。 该系列是议会庄园不可分割的一部分，反映了该机构的遗产和持续的相关性。

---

## 30. OpenTPU：谷歌张量处理器(TPU)的开源重实现

**原文标题**: OpenTPU: Open-Source Reimplementation of Google Tensor Processing Unit (TPU)

**原文链接**: [https://github.com/UCSBarchlab/OpenTPU](https://github.com/UCSBarchlab/OpenTPU)

OpenTPU是加州大学圣巴巴拉分校ArchLab创建的谷歌张量处理器(TPU)的开源重新实现。它旨在利用Python和PyRTL硬件描述语言复制TPU的推理加速能力。

该项目基于公开信息，特别是“张量处理单元的数据中心性能分析”论文。OpenTPU模拟TPU的核心组件，包括矩阵乘法单元、统一缓冲器、激活单元、累加器和权重FIFO。

目前，OpenTPU支持矩阵乘法和ReLU/sigmoid激活，但缺乏卷积、池化和可编程归一化等功能。指令集包括RHM、WHM、RW、MMC、ACT、NOP和HLT。OpenTPU依赖于确定性调度，需要仔细的操作排序和NOP填充。

该项目提供硬件模拟器(runtpu.py)和功能模拟器(sim.py)，允许用户运行和测试程序。checker.py脚本验证硬件模拟、功能模拟和Tensorflow应用程序之间的结果。用户可以使用提供的Python脚本生成训练数据。

关键配置参数，如缓冲区大小和MM阵列维度，是可调整的。虽然它不能精确地复制TPU的ISA或二进制兼容性，但OpenTPU为神经网络专用硬件加速领域的研究、实验和潜在扩展提供了一个有价值的平台。

---

## 31. Show HN: Voiden - 一款免费、离线、原生Git的API客户端

**原文标题**: Show HN: Voiden – a free, offline, Git-native API Client

**原文链接**: [https://voiden.md](https://voiden.md)

Voiden 是一款免费、离线且原生Git的API客户端和工作区。它旨在为开发者提供一种直接在Git仓库中管理和交互API的方式，从而实现API请求和响应的版本控制、协作和可重现性。

“离线”特性是关键，表明该工具无需持续的网络连接即可运行，从而提高了便携性和可靠性。“原生Git”意味着与Git版本控制的无缝集成，能够跟踪API端点配置、请求参数和响应。这使得开发者可以将API交互视为代码，从而实现分支、合并和回滚更改。

Voiden 旨在通过提供一个结构化和有组织的环境来创建、测试和记录 API 调用，同时利用 Git 的协作和历史跟踪优势，从而解决常见的 API 工作流程挑战。"Voiden.md" 文件名表明该工具使用 Markdown 进行存储和组织，使其易于读取和编辑 API 配置。本质上，Voiden 致力于通过提供一种去中心化、版本控制且具备离线能力的解决方案来改进 API 开发工作流程。

---

## 32. 老鹰如何学会利用交通信号灯更成功地捕猎

**原文标题**: How a hawk learned to use traffic signals to hunt more successfully

**原文链接**: [https://www.frontiersin.org/news/2025/05/23/street-smarts-hawk-use-traffic-signals-hunting](https://www.frontiersin.org/news/2025/05/23/street-smarts-hawk-use-traffic-signals-hunting)

这篇文章片段内容不完整且自相矛盾。标题暗示了一个关于鹰学习利用交通信号灯进行捕猎的故事，暗示了动物的智慧和适应能力。然而，内容突然转变为一则关于迁徙鸟类携带入侵蜱虫以及新型疾病潜在传播的新闻。

因此，摘要必须承认这种不一致：

标题引入了一个假设的场景，一只鹰学习利用交通信号灯来提高其捕猎成功率。这暗示了一个关于动物智慧和适应城市环境的叙述。

然而，随附的内容与这只鹰毫无关系。它突然变为一则日期为2024年11月18日的新闻，讨论了迁徙鸟类携带入侵蜱虫的问题。该新闻强调了这些蜱虫将新疾病传播到不同地区的风险。

由于内容与标题不符，因此无法做出连贯的摘要。这篇文章似乎是一个虚构的前提和一个真实世界的新闻报道的结合，两者似乎毫无关联。

---

## 33. Pyrefly 对 Ty：比较 Python 两款基于 Rust 的新型类型检查器

**原文标题**: Pyrefly vs. Ty: Comparing Python's two new Rust-based type checkers

**原文链接**: [https://blog.edward-li.com/tech/comparing-pyrefly-vs-ty/](https://blog.edward-li.com/tech/comparing-pyrefly-vs-ty/)

本文比较了两款基于 Rust 的新型 Python 类型检查器：Pyrefly (Meta 出品) 和 ty (Astral 出品)，两者都旨在改进现有的工具，如 mypy 和 pylance。这两款工具都在 PyCon 2025 上发布，目前都处于早期 alpha 阶段。

虽然两者都是开源的、增量的、使用 Ruff 进行 AST 解析，并提供 CLI 和 LSP 支持，但本文重点介绍了它们在速度、目标、增量化和功能方面的关键差异。

**速度：** 在 PyTorch、Django 和 mypy 代码库上的基准测试表明，ty 通常比 Pyrefly 更快，并且两者都明显优于 mypy 和 pyright。

**目标：** Pyrefly 优先考虑积极的类型推断，即使在未类型化的代码中也是如此，而 ty 则侧重于“渐进保证”，确保删除类型注解不会引入错误。

**增量化：** Pyrefly 使用模块级增量化（重新解析整个模块），而 ty 使用 Salsa 进行细粒度增量化（重新解析单个函数）。

**功能：** Pyrefly 擅长隐式类型推断，并优先考虑了泛型和重载等复杂功能。ty 仍在这些领域迎头赶上。虽然 Pyrefly 可能由于积极的推断而捕获更多错误，但 ty 的方法坚持“渐进保证”，它可能会接受更多代码为有效，而 Pyrefly 则会对此提出异议。

本文强调，这两款工具都在开发中，其功能正在迅速发展。

---

## 34. 日本邮政推出“数字地址”系统

**原文标题**: Japan Post launches 'digital address' system

**原文链接**: [https://www.japantimes.co.jp/business/2025/05/27/companies/japan-post-digital-address/](https://www.japantimes.co.jp/business/2025/05/27/companies/japan-post-digital-address/)

日本邮政推出“数字地址”系统，用户可将七位数字字母代码与其物理地址关联。该系统于2025年5月27日启动，旨在简化在线交易。用户可通过日本邮政的Yu ID会员服务注册数字地址，以便在网上购物和其他网站上输入代码时自动填写地址。

一项关键优势在于，即使用户的物理地址发生变化，数字地址仍保持不变。用户只需在日本邮政更新地址变更信息，新地址将与现有代码关联。

电商巨头乐天和其他公司正在考虑采用该系统，预计将提高用户便利性。日本邮政计划用十年时间来推广新型“数字地址”系统的广泛应用。

---

## 35. 德州年度阅读测试难度逐年调整，掩盖进步。

**原文标题**: Texas' annual reading test adjusted difficulty yearly, masking improvement

**原文链接**: [https://theconversation.com/texas-annual-reading-test-adjusted-its-difficulty-every-year-masking-whether-students-are-improving-244159](https://theconversation.com/texas-annual-reading-test-adjusted-its-difficulty-every-year-masking-whether-students-are-improving-244159)

本文探讨了近期对德克萨斯州年度阅读测试——德克萨斯州学术准备评估（STAAR）的调查，并揭示该测试的设计可能掩盖了学生成绩的实际进步。2012年至2021年间，尽管K-12教育投入增加，但学生成绩依然停滞不前。

作者的研究发现，STAAR测试的设计类似于常模参照测验，意味着它评估学生相对于同龄人的表现，而非针对固定标准。这种设计包括每年调整测试难度，以确保相对一致的失败率，无论学生是否比往年学得更多。省略简单问题和调整分数等因素，抵消了教学质量提高的效果。

这具有重大意义，因为高风险的考试成绩严重影响学校资源、学区控制、教师项目认证，甚至房产价值。这种设计对受种族主义、贫困或语言障碍影响而处于边缘地位的学生造成 disproportionate 的影响，他们在这些测试中历来表现不佳。作者计划调查其他州是否使用类似的测试方法。虽然STAAR测试在2022年进行了重新设计，但作者怀疑评分方法在很大程度上保持不变，这可能会使学生真实进步的掩盖长期存在。德克萨斯州教育局未回应置评请求。

---

## 36. 人工智能：加速无能

**原文标题**: AI: Accelerated Incompetence

**原文链接**: [https://www.slater.dev/accelerated-incompetence/](https://www.slater.dev/accelerated-incompetence/)

过度依赖大型语言模型(LLM)会加速软件工程领域的无能，而非增强其能力。作者（一位软件工程师）指出了使用LLM相关的风险，包括不正确或略微错误的输出，未能挑战有缺陷的提示（导致XY问题），快速积累“技术债务”导致代码库不卫生，通过外包关键性思考使使用者变得幼稚，以及丧失编程的乐趣。

作者认为，LLM无法取代人类的批判性思维，尤其是在两个关键领域：程序理论和程序熵。程序理论，如Peter Naur所定义，是对程序设计的精神模型或共同理解，对于可维护性和未来的修改至关重要。LLM受其上下文窗口的限制，无法掌握或保留这样的理论。程序熵，与代码库随时间推移而增加的复杂性有关，需要人为干预来减少或抵抗。LLM仅在文本层面工作，往往会引入不必要的更改并增加复杂性。

作者总结说，人类工程师的长期价值主张仍然没有改变。尽管通过LLM降低成本具有诱惑力，但世界仍然需要深厚的技术技能和批判性思维。LLM应该被用作工具，而不是拐杖，工程师应该继续投资于基本技能。

---

## 37. 微软开始向任何第三方应用开放Windows Update。

**原文标题**: Microsoft is starting to open Windows Update up to any third-party app

**原文链接**: [https://www.theverge.com/news/675446/microsoft-windows-update-all-apps-orchestration-platform](https://www.theverge.com/news/675446/microsoft-windows-update-all-apps-orchestration-platform)

微软正通过一个新的“Windows更新协调平台”向第三方应用程序开放Windows更新。该平台将允许开发者通过Windows更新来更新他们的应用程序和驱动程序，提供与核心Windows更新和设备驱动程序统一的更新体验。

该项目目前处于私有预览阶段，最初专注于商业应用程序，但旨在向任何应用程序或管理工具开放。使用该平台的开发者可以利用Windows更新基于用户活动、电池状态甚至可持续能源时间的调度。他们还可以与原生Windows更新通知和更新历史记录集成。

该平台将支持MSIX/APPX打包的应用程序和一些自定义Win32应用程序。通过参与，应用程序将自动受益于底层Windows更新平台的未来改进。此举旨在解决Windows上应用程序更新的碎片化问题，因为大多数应用程序都使用独立的更新机制。虽然微软之前曾尝试通过Microsoft Store和Windows Package Manager来集中更新，但这个新平台为开发者提供了一种新的途径来简化更新过程，并可能改善用户体验。企业或像Adobe这样的主要开发者是否会接受这个新系统，还有待观察。

---

## 38. 只有椭圆曲线迪菲-赫尔曼

**原文标题**: There Is No Diffie-Hellman but Elliptic Curve Diffie-Hellman

**原文链接**: [https://keymaterial.net/2025/05/23/there-is-no-diffie-hellman-but-elliptic-curve-diffie-hellman/](https://keymaterial.net/2025/05/23/there-is-no-diffie-hellman-but-elliptic-curve-diffie-hellman/)

本文深入探讨了为什么椭圆曲线Diffie-Hellman算法被用于密码学，而不是其他群，例如怪物群。核心问题在于Diffie-Hellman算法中，私钥到公钥的映射是一种群同构，这意味着，从纯粹的群论角度来看，私钥和公钥是无法区分的。这似乎破坏了Diffie-Hellman密钥交换的安全性。

为了理解椭圆曲线的选择，作者引入了范畴论和“群对象”的概念。群对象并非简单地将群视为具有运算的集合，而是在更广泛的范畴中使用同态来定义的。这使得人们能够更细致地理解群结构，而不仅仅是简单的同构。

本文解释了如何使用同态和范畴内的终端对象来定义群公理，如结合律和中性元素的存在，甚至无需直接引用元素。这种范畴框架使我们能够区分不同类型的群。

关键在于，Diffie-Hellman算法不仅仅依赖于任何抽象群；它需要特定范畴内的群对象。椭圆曲线Diffie-Hellman算法的安全性源于椭圆曲线作为有限域上的群对象的性质，特别是求解椭圆曲线离散对数问题的难度，而不仅仅是它们是群这一事实。

---

## 39. 业余电脑文化

**原文标题**: The Hobby Computer Culture

**原文链接**: [https://technicshistory.com/2025/05/24/the-hobby-computer-culture/](https://technicshistory.com/2025/05/24/the-hobby-computer-culture/)

本文探讨了1975年至1978年间业余计算机文化的兴起，重点关注推动其发展的爱好者。最初，个人电脑被视为“世界上最伟大的玩具”，吸引了受过良好教育、富裕的男性，他们对机器本身着迷——购买、组装、编程和装饰它们。实用的软件应用是次要的，而游戏，尤其是《星际迷航》，则很突出。

三个主要结构将这些爱好者联系起来：当地计算机俱乐部、像《BYTE》这样的杂志和零售计算机商店。家庭酿造计算机俱乐部虽然出名，但代表了一种独特的政治倾向，不一定被更广泛的运动所共有。美国各地的俱乐部提供专业知识共享和社区意识，而杂志则提供信息和项目创意。像迪克·海泽的计算机商店和保罗·特雷尔的字节商店这样的零售商店，让潜在买家可以亲身体验计算机。

南加州计算机协会 (SCCS) 试图创建一个庞大的支持网络，但由于管理不善和诉讼而崩溃。商业软件和直接供应商支持的兴起逐渐降低了这些社区网络的重要性。

早期的计算机销售依赖于直接向 MITS 等制造商订购。然而，零售商店的出现缓解了买卖双方的问题，为买家提供产品演示和建议，为卖家提供更大、更可预测的订单。虽然制造商最初试图控制经销商，但由于计算机制造商之间的竞争，零售商最终掌握了更大的权力。字节商店和 ComputerLand 等连锁店通过批量折扣和品牌认知获得了优势。

---

## 40. LumoSQL

**原文标题**: LumoSQL

**原文链接**: [https://lumosql.org/src/lumosql/doc/trunk/README.md](https://lumosql.org/src/lumosql/doc/trunk/README.md)

LumoSQL 是 SQLite 嵌入式数据存储库的一个注重安全、隐私、性能和测量的修改版本，旨在展示一些有用的更改，而 SQLite 本身由于其广泛的使用和保守的性质可能不易采用。 它由 NLNet 基金会支持，并在各种架构和操作系统上运行。

主要功能包括：

*   **可插拔后端：** LumoSQL 支持交换键值存储引擎，例如 LMDB 和 Berkeley Database，从而可以将这些存储的不同版本与 SQLite 结合使用。
*   **加密和损坏检测：** 增加了现代加密技术，包括每行基于属性的加密 (ABE) 和用于错误检测和更快搜索操作的校验和。
*   **非分支开发：** LumoSQL 采用一种新颖的“非分支”工具来半自动地跟踪来自 SQLite 和其他项目的上游更改。 这种方法使 LumoSQL 能够组合和配置上游，而无需分支。

LumoSQL 存在一些局限性，包括需要更新其基准测试并完全集成 LMDB 和 BDB 后端。 但是，解决这些问题的基础设施已经就位。

该文章还提供了设置构建环境以及使用 LumoSQL 构建和基准测试系统来测试和比较不同配置的性能的说明。 快速入门指南演示了如何对 SQLite 和 LMDB 版本进行基准测试并分析结果。

---

## 41. Show HN: 终端花园

**原文标题**: Show HN: Terminal Flower Garden

**原文链接**: [https://github.com/bdavidzhang/flower-garden-cli](https://github.com/bdavidzhang/flower-garden-cli)

“终端花园”是一个CLI游戏，可将您的终端转变为一个美丽的数字花园。您可以培育五种独特的花卉类型——螺旋玫瑰、分形树、曼陀罗花、波浪花园和星爆——每种花都会生长成独特的数学模式和分形。该游戏具有针对每种花卉的10个级别的生长系统、持久保存功能、使用`colorama`进行彩色显示以及交互式菜单。

可以使用`pip`（推荐）、克隆GitHub存储库或直接从源代码运行来轻松安装该游戏。要玩游戏，启动游戏，从菜单中选择一个动作（浇灌特定的花朵、查看花园、全部浇灌、重置或退出），并观看花朵生长。

该项目使用Python 3.7+，并包含`colorama`以进行彩色输出。它支持跨平台功能（Windows、macOS 和 Linux）。该游戏利用模块化的项目结构，其中`main.py`文件包含核心游戏逻辑。欢迎通过pull requests贡献代码，该项目已获得 MIT 许可证许可。 鼓励用户在 GitHub 上为该项目加星，以示支持并报告任何问题。

---

## 42. BGP处理漏洞导致互联网路由大范围不稳定

**原文标题**: BGP handling bug causes widespread internet routing instability

**原文链接**: [https://blog.benjojo.co.uk/post/bgp-attr-40-junos-arista-session-reset-incident](https://blog.benjojo.co.uk/post/bgp-attr-40-junos-arista-session-reset-incident)

2025年5月20日，一起BGP处理漏洞引发了广泛的互联网路由不稳定。 罪魁祸首是一个包含损坏且意外BGP Prefix-SID属性的BGP更新。 虽然一些BGP实现（IOS-XR、Nokia SR-OS）正确地过滤了该消息，但JunOS和Arista EOS之间发生了有问题的交互。 JunOS传递了损坏的消息，导致Arista EOS设备在收到该消息时重置会话。

该属性很可能是由Starcloud (AS135338) 或 Hutchison (AS9304) 添加的，而不是源自前缀的网络。 由于运行Bird（缺乏BGP SID支持）的路由服务器广泛分发了有缺陷的消息，Hutchison在众多互联网交换中心的存在加剧了这个问题。

该事件影响了大约100个网络，包括SpaceX Starlink、Zscaler、ByteDance和Disney。 bgp.tools上的消息速率从20-30k/s飙升至超过150k/s。

作者批评Juniper的JunOS尽管具有BGP错误容忍度，但仍将错误消息传播给对等方。 作者强调了可能造成的严重后果，不仅限于消费者的不便，还可能影响电视广播和紧急呼叫等关键服务。 他们倡导改进BGP错误处理，并鼓励更多网络为bgp.tools贡献数据，以便将来进行调试。

---

## 43. 显示 HN：懒人俄罗斯方块

**原文标题**: Show HN: Lazy Tetris

**原文链接**: [https://lazytetris.com/](https://lazytetris.com/)

“Show HN: Lazy Tetris” 提交可能呈现的是经典俄罗斯方块游戏的简化或自动化版本。标题暗示了对易用性或最少玩家互动的关注。可能涉及的方面包括：

*   **自动化游戏玩法：** 游戏的核心机制可能是自动化的，例如自动放置方块、消除行，甚至完全自主地玩游戏。这与需要玩家主动控制的传统俄罗斯方块形成对比。
*   **简化机制：** 游戏可能会移除或简化传统俄罗斯方块的元素，例如方块旋转、手动放置方块或重力控制。重点可能仅仅是观看游戏进程或做出高级决策。
*   **被动娱乐：** “Lazy Tetris” 可能被设计为一种被动娱乐形式，用户可以在不积极参与的情况下观察游戏，也许针对效率或美观性进行了优化。
*   **教育工具：** 有可能该提交是一个教育工具，用于演示俄罗斯方块算法、人工智能或游戏设计原则。“Lazy”方面可能指的是启动这些模拟所需的最小玩家输入。
*   **新颖转折：** 游戏可能会在俄罗斯方块公式中引入一种新颖的转折，这种转折优先考虑简单性或自动化，而不是传统的基于技能的游戏玩法。

在没有关于具体实现的更多信息的情况下，最可能的解释是一个简化的俄罗斯方块游戏，专为被动观看或自动化游戏玩法而设计，可能具有教育应用或对传统公式的新颖转折。

---

## 44. 芥末手表 (1990)

**原文标题**: Mustard Watches (1990)

**原文链接**: [https://girard.perso.math.cnrs.fr/mustard/article.html](https://girard.perso.math.cnrs.fr/mustard/article.html)

《芥末手表》（1990），署名Y.-J. Ringard，由Pierre Barthélémy和Éric Lozingot重新整理，看似一篇可能与某种以芥末为特色的钟表相关的文章或文档。该文档共四页，但缺乏进一步的背景信息，内容的确切性质仍不明确。标题暗示着对腕表的关注，“芥末”的存在则暗示了这些腕表独特的特征或主题。Barthélémy和Lozingot的重新整理表明原始文章可能不完整或碎片化，需要修复或汇编。在检查这四页的实际内容之前，无法确定主题的具体内容（例如，设计、历史意义或芥末的创新用途）。

---

## 45. 会增加碳排放的“绿色”航空燃料

**原文标题**: The 'Green' Aviation Fuel That Would Increase Carbon Emissions

**原文链接**: [https://e360.yale.edu/features/corn-soy-biofuel-aviation-congress](https://e360.yale.edu/features/corn-soy-biofuel-aviation-congress)

本文批判了以玉米和大豆等作物为原料生产“可持续航空燃料”（SAF）的做法，认为这是一种虚假的应对气候变化的方案。航空业试图通过使用SAF来实现脱碳，但本文认为，依赖作物会产生不利影响。

作者强调，将作物用于燃料会提高食品价格和加剧全球饥饿，导致森林砍伐和草原转变为农田，因为世界各地的农民都在寻找新的土地来弥补粮食生产的损失。共和党的“美丽大法案”因延长SAF的税收抵免，同时禁止考虑土地利用排放而被批评，这实际上是在补贴一种有害的做法。欧盟因其对土地利用的破坏性影响而将基于作物的燃料排除在航空业之外。

文章强调了美国农业游说团体的力量，他们寻求为玉米乙醇和大豆生物柴油寻找新市场，因为电动汽车威胁着汽车行业的需求。作者指出，两党都支持生物燃料，即使是在旨在废除气候政策的立法中也是如此。

文章引用分析表明，SAF生产需要大量土地，可能导致广泛的森林砍伐和碳释放。拜登政府使用GREET模型，该模型淡化了间接土地利用变化（ILUC），这被批评为优先考虑农业利益，而非真正的气候效益。作者强调，回收食用油是一种更具气候友好性的替代方案。

---

## 46. 太空自拍

**原文标题**: Space Selfie

**原文链接**: [https://space.crunchlabs.com/](https://space.crunchlabs.com/)

CrunchLabs 提供一项名为“太空自拍”的免费服务，他们会将你上传的自拍照发送到其位于太空的卫星 SAT GUS。SAT GUS 以 CrunchLabs 的松鼠吉祥物 Phat Gus 命名，它会将你的自拍照显示在手机上，并以地球为背景拍摄一张照片，然后将合成的图像传回给你。

该计划旨在为每个人提供一次史诗般的、可验证的太空体验。为确保真实性，图像将同时显示你手机屏幕上的自拍照和背景中的地球。文章解答了关于该项目的常见问题，包括卫星名称的由来、发射情况以及潜在问题。文章还涵盖了图像要求、服务费用（免费）、资格、隐私、图像返回时间、卫星跟踪、相机规格，以及对最终图像中某些视觉元素的解释，例如没有星星或云层外观的变化。文章还提到了参与“太空自拍”项目的合作伙伴。最终目标是为参与者提供一张独特的、可分享的“太空自拍”。

---

## 47. 在WebGL中运行GPT-2：重拾GPU着色器编程的失落艺术

**原文标题**: Running GPT-2 in WebGL: Rediscovering the Lost Art of GPU Shader Programming

**原文链接**: [https://nathan.rs/posts/gpu-shader-programming/](https://nathan.rs/posts/gpu-shader-programming/)

本文详细介绍了作者使用 WebGL 和着色器实现 GPT-2 的项目，让人们得以一窥通用 GPU (GPGPU) 编程的历史渊源及其当前的局限性。文章追溯了从固定功能图形管线到可编程着色器以及像 CUDA 和 OpenCL 这样的专用计算 API 的演变过程。虽然这些 API 提供了更直接和高效的方法，但本文探讨了如何“劫持”传统的图形 API 特性（如纹理、帧缓冲区和顶点/片段着色器）来进行计算。

纹理被用作张量，存储数值数据，帧缓冲区则充当容器，用于将渲染输出重定向到这些纹理中。片段着色器被重新用作计算内核，从而能够在数千个 GPU 核心上实现并行计算。该过程涉及链接着色器通道以进行矩阵乘法和激活函数等操作，从而将整个 GPT-2 流程保持在 GPU 上，直到提取最终 logits。

然而，文章承认了这种方法的重大局限性，包括缺乏共享/本地内存、纹理大小限制、缺乏同步机制以及与绘制调用相关的开销。虽然这是一个有趣的教育实践，但与使用专用计算 API 相比，基于着色器的计算最终实用性较低。作者提供了代码仓库的链接，供那些有兴趣进一步探索实现的人使用。

---

## 48. 早期Unix文件名的长度

**原文标题**: The length of file names in early Unix

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/unix/UnixEarlyFilenameLenghts](https://utcc.utoronto.ca/~cks/space/blog/unix/UnixEarlyFilenameLenghts)

克里斯·西本曼的博客 (Wandering Thoughts) 正在阻止使用可疑旧浏览器的用户访问，原因是大量使用过时 Chrome 用户代理的高流量爬虫激增，可能用于 LLM 训练数据收集。这是一项旨在降低服务器负载的措施。

如果使用最新浏览器的合法用户被阻止，他们被要求通过他的大学邮箱地址联系西本曼，并提供其浏览器详细信息（包括 User-Agent 字符串）。

该说明特别针对通过 archive.today、archive.ph 和 archive.is 等存档服务访问该博客的用户。这些服务正在被阻止，因为它们的爬取行为与恶意机器人无法区分：它们使用旧的 Chrome 用户代理，从广泛分布的 IP 地址进行爬取（有些 IP 地址伪造了反向 DNS 记录，声称是 Googlebot），并且没有明确的身份标识。西本曼建议改用 archive.org，因为它是一个行为更好的存档爬虫。

---

## 49. 重新审视改变赛马博彩的算法 (2023)

**原文标题**: Revisiting the algorithm that changed horse race betting (2023)

**原文链接**: [https://actamachina.com/posts/annotated-benter-paper](https://actamachina.com/posts/annotated-benter-paper)

本文回顾了比尔·本特在将数学模型应用于赛马投注方面的开创性工作，重点关注他1994年关于计算机辅助评估的论文。本特凭借投注香港赛马积累了10亿美元的财富，并在论文中记录了他成功的模型。尽管发表的模型可能已经过时，但本文强调了其在非常规领域中对数学的深刻应用，尤其是在考虑到当时的硬件和软件限制的情况下。

本文呈现了本特论文的注释版本，其中包含代码块和注释。它没有复制原始模型，而是侧重于分析公众估计（源自香港赛马会历史获胜赔率），研究本特如何生成模型校准表，评估公众估计随时间的改进，并尝试使用PyTorch拟合调整因子。

本文强调了基于计算机方法的优势，包括其经验性质、通过数据分区进行的可测试性以及一致性。它还承认了所需的大量准备工作，包括数据收集、验证和编程。

对评估模型开发的讨论主要集中在本特使用的多项logit模型上，后来被Probit模型取代。本文探讨了影响赛马“当前表现潜力”的各种因素，这些因素分为当前状况、过去的表现、对过去表现的调整、当前比赛情境因素和偏好。它还讨论了定义因素以尽可能多地提取信息的重要性，以及基于有根据的猜测和反复试验的改进过程。

---

## 50. CSS我的世界

**原文标题**: CSS Minecraft

**原文链接**: [https://benjaminaster.com/css-minecraft/](https://benjaminaster.com/css-minecraft/)

无法访问文章链接。

---

## 51. 在越南，奇特的奇卡诺文化前哨

**原文标题**: In Vietnam, an unlikely outpost for Chicano culture

**原文链接**: [https://www.latimes.com/world-nation/story/2025-05-27/chicano-culture-vietnam](https://www.latimes.com/world-nation/story/2025-05-27/chicano-culture-vietnam)

在胡志明市，一个以理发师和纹身师为中心的“越裔奇卡诺人”亚文化正在兴起，他们拥抱奇卡诺文化。从未去过美国的理发师阮福禄就是这一趋势的代表，他用瓜达卢佩圣母和哥特式字母等奇卡诺符号装饰自己和他的理发店。这场运动大约在10年前由阮黄青廉以奇卡诺为主题的理发店发起，为成员提供了归属感和认同感。

伊格纳西奥·洛佩斯·卡尔沃教授指出，奇卡诺文化的叛逆本质吸引了那些寻求挑战亚洲保守规范的人。文章还强调了一种历史联系，指出参加越南战争的奇卡诺士兵对越南人民产生了一种联系感。

虽然越裔奇卡诺人在社交媒体上，特别是在TikTok上越来越受欢迎，但他们也面临批评，尤其来自将纹身与黑帮联系在一起的老一代人。由于这种社会污名，核心社群仍然很小。成员们强调，他们不是挪用文化，而是继承和庆祝其积极方面，如家庭、忠诚和坚韧。来自德国的纹身艺术家迈克尔·潘强调，拥抱奇卡诺的理想不仅仅是外表。

---

## 52. Chrome扩展的权限提升 (2023)

**原文标题**: A privilege escalation from Chrome extensions (2023)

**原文链接**: [https://0x44.xyz/blog/cve-2023-4369/](https://0x44.xyz/blog/cve-2023-4369/)

Derin Eryılmaz 详细描述了在 ChromeOS 上的 Chrome 扩展程序中发现的一个权限提升漏洞 (CVE-2023-4369)。该漏洞允许仅具有 "downloads" 权限的扩展程序在特权 `chrome://file-manager` 上下文中执行代码。

该漏洞利用涉及恶意扩展程序下载一个 HTML 文件，然后使用特殊的 `filesystem:chrome://file-manager` URL 打开它。这绕过了安全限制，使该扩展程序能够读取敏感页面并访问 `chrome.fileManagerPrivate` API。

此 API 赋予了强大的权力，使扩展程序能够读取和写入用户下载的文件，操纵 Crostini（内置 Linux 终端），并可能在 Linux 容器中执行任意代码。 这可能被用于勒索软件或其他恶意活动。

作者还在 ChromeOS 上的 "Image Loader" 组件扩展程序中发现了类似的错误。 此错误允许在 `chrome://resources` 中执行代码，从而导致第二个 Chrome XSS。

根本原因在于 `filesystem:` 协议，这是一个允许在虚拟文件系统中存储和访问文件的遗留 Chrome 功能。 `/external` 路径是 ChromeOS 独有的，它暴露了用户的 `MyFiles` 目录。

虽然文件管理器错误中最严重的部分已迅速修复，但该漏洞表明了 Chrome 扩展程序在 ChromeOS 上提升权限和绕过安全沙箱的潜力，从而导致严重的隐私和安全风险。 除安装恶意扩展程序外，该漏洞利用不需要任何用户交互。

---

## 53. 赋格的艺术 – 对位法 I (2021)

**原文标题**: The Art of Fugue – Contrapunctus I (2021)

**原文链接**: [https://www.ethanhein.com/wp/2021/the-art-of-fugue-contrapunctus-i/](https://www.ethanhein.com/wp/2021/the-art-of-fugue-contrapunctus-i/)

本文探讨了J.S.巴赫的《赋格的艺术》，特别是其中的《对位法I》，以及尽管它最初并不受欢迎且具有教谕性，但为何它可能引起现代听众的共鸣。作者解释说，《赋格的艺术》是巴赫死后出版的，最初因其复杂的对位法而不流行。通过可视化其结构，作者的欣赏得到了提升。

与其他赋格相比，《对位法I》相对简单，缺乏在后期作品中发现的主题的精细变形。作者提供了不同的乐器演奏版本的例子，从弦乐四重奏到萨克斯管四重奏，展示了它的多功能性。

约瑟夫·克尔曼的分析突出了《对位法I》作为缺乏典型对位技巧的赋格的独特地位。克尔曼指出巴赫有意的克制以及作品复杂性的逐渐增加，最终达到一个强有力的终止式。作者将巴赫的即兴风格与爵士乐相提并论，强调了各声部的相互作用和主题的发展。

最后，作者讨论了将《对位法I》与现代节拍进行混音的吸引力，并提供了一个对安吉拉·休伊特的录音与Jay-Z和艾丽西亚·凯斯演唱的《帝国之心》的混音版本。这种出乎意料的组合，旨在仅部分带有讽刺意味，有助于保持专注，并突出了巴赫音乐固有的律动潜力，从而增强了其教谕功能并创造了一种独特的审美。

---

## 54. 使用Postgres pg_test_fsync工具测试低延迟写入

**原文标题**: Using Postgres pg_test_fsync tool for testing low latency writes

**原文链接**: [https://tanelpoder.com/posts/using-pg-test-fsync-for-testing-low-latency-writes/](https://tanelpoder.com/posts/using-pg-test-fsync-for-testing-low-latency-writes/)

本文重点强调了低延迟写入对于数据库的重要性，特别是对于WAL/redo日志。文章介绍了Postgres自带的`pg_test_fsync`工具，认为它是评估磁盘（或云块存储卷）是否适合需要快速写入的工作负载的宝贵资源，无论使用何种数据库系统。

作者演示了该工具的用法，比较了消费级NVMe SSD（Samsung 990 Pro）和企业级SSD（Micron 7400），后者具有断电保护（PLP）。结果显示同步写入延迟存在显著差异。缺乏基于DRAM的PLP写入缓存的消费级SSD表现出明显更高的延迟（对于单个8kB的`fdatasync`写入，大约为1.6ms），而企业级SSD的延迟则低得多（对于相同的写入，大约为24微秒）。

文章强调，高写入IOPS并不能保证单个写入的低延迟。消费级SSD可能会序列化写入，从而增加延迟。在OS RAM中缓冲写入，然后使用`fdatasync`进行批量同步可以提高吞吐量，但不能提高单个写入的延迟。企业级SSD利用其PLP和直写缓存，可提供明显更快的同步写入确认。作者还指出了扇区大小对工具操作的影响，如果小的IO大小与磁盘的物理扇区大小未对齐，可能会导致失败。

---

## 55. 展示HN: PgDog – 无需扩展即可分片Postgres

**原文标题**: Show HN: PgDog – Shard Postgres without extensions

**原文链接**: [https://github.com/pgdogdev/pgdog](https://github.com/pgdogdev/pgdog)

PgDog 是一个用 Rust 编写的全新、快速且安全的开源工具，用于对 PostgreSQL 数据库进行分片，*无需*依赖 PostgreSQL 扩展。它充当事务连接池和逻辑复制管理器，旨在处理数百个数据库和数千个连接。

主要功能包括：

*   **负载均衡：** 通过各种策略（轮询、随机等）在多个 PostgreSQL 副本或主服务器之间分配事务，将 SELECT 查询路由到副本，并将其他查询路由到主服务器。
*   **健康检查和故障转移：** 自动将查询从不健康的服务器重定向，从而最大限度地提高可用性。
*   **事务连接池：** 类似于 PgBouncer，支持事务和会话连接池。
*   **分片：** 根据分片键自动将查询路由到适当的分片，甚至可以处理跨分片查询。
*   **COPY 命令支持：** 自动将 COPY 命令拆分到各个分片。
*   **逻辑复制：** 在数据库之间拆分数据以进行分片，而无需停机。
*   **配置：** 像 PgBouncer/PgCat 一样，在运行时具有高度可配置性。

PgDog 提供 Kubernetes 和 Docker 部署选项，并公开一个 PgBouncer 风格的管理数据库和一个 OpenMetrics 端点用于监控。它在 AGPL v3 许可下发布，允许内部使用和私有修改，无需共享源代码，除非是将 PgDog 作为公共服务提供。该项目尚处于早期阶段，但欢迎早期采用者并定期进行性能基准测试。

---

## 56. 分号自有妙处，我爱它的原因就在这。

**原文标题**: Semicolons bring the drama; that's why I love them

**原文链接**: [https://www.ft.com/content/80c39c74-8753-44bf-aeb0-cf6701a64f02](https://www.ft.com/content/80c39c74-8753-44bf-aeb0-cf6701a64f02)

题为“分号自带戏剧性；这就是我爱它们的原因”的文章位于《金融时报》(FT)网站的付费墙之后。提供的内容本质上是《金融时报》订阅的广告。

它强调了以下要点：

* 文章本身可能是一篇评论文章（标题暗示），侧重于作者对分号的欣赏。
* 读者需要订阅才能访问该文章和其他FT内容。
* 《金融时报》提供多个订阅级别（FT Edit、Standard Digital和Premium Digital），具有不同的功能和定价。FT Edit提供数量有限的精选文章。
* 内容强调订阅的好处，例如访问全球新闻、专家分析、新闻通讯、FT应用程序等。
* 组织也可以选择订阅（FT Professional）。
* 《金融时报》宣传其价值，强调超过一百万读者为其内容付费。

所提供文本的主要目的是鼓励读者订阅《金融时报》，以访问关于分号的文章以及更广泛的内容。

---

## 57. 世界首个常温拍赫兹晶体管

**原文标题**: Worlds first petahertz transistor at ambient conditions

**原文链接**: [https://news.arizona.edu/news/u-researchers-developing-worlds-first-petahertz-speed-phototransistor-ambient-conditions](https://news.arizona.edu/news/u-researchers-developing-worlds-first-petahertz-speed-phototransistor-ambient-conditions)

亚利桑那大学研究人员开发出世界首个在常温常压下工作的拍赫兹级光电晶体管。这项发表在《自然·通讯》上的突破性成果，利用石墨烯中的量子隧穿效应，通过超快光脉冲操纵电子，实现了比现代计算机芯片快1000倍以上的处理速度。

由穆罕默德·哈桑领导的团队对商用石墨烯光电晶体管进行了改造，加入了一层特殊的硅层，并使用激光制造出这种拍赫兹量子晶体管。该设备可以以638阿秒（十亿分之一秒的五次方）的速度开关。这极大地推进了超快计算机技术的发展。

与一些需要严格条件的科学进步不同，这种晶体管在常温常压下工作，为商业化和在日常电子产品中的使用铺平了道路。研究人员正与亚利桑那大学技术推广机构合作，对这项创新进行专利申请和市场推广，并正在开发一种与市售设备兼容的晶体管。

这项技术的潜在应用非常广泛，包括彻底改变计算技术，加速太空研究、化学、医疗保健等领域的发现。亚利桑那大学的目标是同时以世界上最快的电子显微镜和这种开创性的拍赫兹级晶体管而闻名。

---

## 58. 为什么初代Macintosh的屏幕分辨率是512×324

**原文标题**: Why the original Macintosh had a screen resolution of 512×324

**原文链接**: [https://512pixels.net/2025/05/original-macintosh-resolution/](https://512pixels.net/2025/05/original-macintosh-resolution/)

最初的Macintosh与后来的型号不同，其屏幕分辨率为512x342像素，这一决定受多个关键因素驱动。 虽然许多人认为更多的内存可以消除这个问题，但事实是，第一代Macintosh的128KB RAM是一个设计上的升级，而不是一种限制。 早期的设计内存要少得多。

内存限制至关重要。 512x342的分辨率需要大约22KB的RAM用于显示缓冲区，这严重影响了应用程序可用的内存。 更高的512x384屏幕会消耗更多宝贵的内存。

CPU，即以7.83 MHz运行的Motorola 68000，也发挥了作用。 为了保持60 Hz的刷新率并最大限度地减少闪烁，CPU将大部分时间用于绘制显示。 更大的显示屏会进一步加重CPU的负担，影响整体性能。

至关重要的是，512x342的分辨率允许使用正方形像素，Lisa放弃了这一设计选择。 正方形像素确保了准确的屏幕显示，防止失真，并使图形应用程序更容易开发。

最后，72 DPI的屏幕足以满足诸如文字处理和页面布局等预期用例，提供了足够的清晰度，并允许用户以不同的比例可视化他们的工作。

本质上，512x342的分辨率是一个经过仔细考虑的折衷方案，它在性能、内存限制、视觉保真度和可用性之间取得了平衡，从而在可用的硬件能力范围内优化了原始Macintosh的预期用途。

---

## 59. Show HN: Malai – 安全地与他人分享本地TCP服务（数据库/SSH）

**原文标题**: Show HN: Malai – securely share local TCP services (database/SSH) with others

**原文链接**: [https://malai.sh/hello-tcp/](https://malai.sh/hello-tcp/)

Malai 0.2.5 引入了安全共享本地 TCP 服务（如数据库、SSH 和自定义 TCP 协议）的能力。用户无需直接公开端口即可暴露这些服务。`malai tcp <端口> --public` 命令用于共享本地 TCP 服务器，而 `malai tcp-bridge <id> <端口>` 允许远程机器通过 Malai 网络连接到该服务器。

对于 SSH，用户可以使用 `malai tcp 22 --public` 共享他们的 SSH 服务器，而无需暴露 22 端口，然后通过在桥接机器上使用 `ssh -p <端口> user@localhost` 通过 SSH 连接。

用例包括保护 SSH 安全、共享本地数据库（Postgres、Redis）、演示联网应用程序以及为学生提供实时帮助。

此版本还包括一个新的 "malai folder" 命令，用于通过简单的 HTTP 服务器共享本地文件和文件夹。示例展示了如何使用 `malai folder ~/projects/fastn/assets/ --public` 共享目录。该项目鼓励用户尝试此功能并提供反馈。鼓励用户在 GitHub 上为项目点赞以示支持。

---

## 60. 浅薄技术知识辩护

**原文标题**: In defense of shallow technical knowledge

**原文链接**: [https://www.seangoedecke.com/shallow-technical-knowledge/](https://www.seangoedecke.com/shallow-technical-knowledge/)

本文提倡发展对广泛技术的“浅层技术知识”，认为这对于良好的工程实践至关重要。作者认为，即使没有深入的专业知识，理解底层技术的基本原理也能带来更好的决策和问题解决。

作者以数据库索引和大型语言模型（LLMs）为例，展示了基本的理解如何让工程师能够预测潜在问题，并对实现和使用做出明智的选择。例如，了解数据库索引可以加快读取速度但会降低写入速度，可以帮助工程师决定何时以及如何使用它们。类似地，理解LLM如何生成输出有助于预测它们在不同场景下的行为，例如JSON输出。

作者承认深度专业化的价值，但建议建立广泛的知识基础，以提高通用性和适应性，尤其是在快速发展的技术领域中。建议的方法包括，目标是向一位聪明的初级工程师解释技术，避免不必要的数学或术语繁重的解释。

建立这些直觉的实用技巧包括阅读原始论文，利用语言模型进行解释和事实核查，以及写下你的理解来巩固它。关键是专注于发展关于性能、适用性和潜在局限性的有用见解，而不是力求完全掌握。作者使用语言模型来事实核查他们的工作，以识别任何误解或缺陷。

---

## 61. DuckLake是一个集成的数据湖和目录格式

**原文标题**: DuckLake is an integrated data lake and catalog format

**原文链接**: [https://ducklake.select/](https://ducklake.select/)

DuckLake：基于SQL数据库的开源数据湖和目录格式

DuckLake是由DuckDB团队开发的一种新型开源数据湖和目录格式，它利用SQL数据库进行元数据管理。它的目标是提供高级数据湖特性，如快照、时间旅行查询、模式演化和分区，而无需传统湖仓架构的复杂性。

DuckLake的关键特性包括无需频繁压缩的轻量级快照、并发访问的ACID事务保证以及通过基于统计信息的过滤器下推实现的性能优化。它使用Parquet文件进行数据存储，并且可以部署在诸如AWS S3之类的对象存储上。

DuckLake的目录元数据可以使用各种SQL数据库进行管理，例如PostgreSQL、SQLite、MySQL和DuckDB本身。DuckDB扩展提供了与DuckLake交互的一流支持，使用户能够读取和写入以DuckLake格式存储的数据集。

DuckLake可用于“多人DuckDB”设置，从而允许多个DuckDB实例并发访问数据。它还为单个DuckDB用户提供诸多优势，例如时间旅行查询、数据分区以及将数据存储在多个文件中的能力。

DuckLake规范和DuckDB扩展均以MIT许可证发布。

---

## 62. 奶牛戴GPS项圈防掉河里

**原文标题**: Cows get GPS collars to stop them falling in river

**原文链接**: [https://www.bbc.co.uk/news/articles/cj4229k744lo](https://www.bbc.co.uk/news/articles/cj4229k744lo)

剑桥市议会使用GPS项圈防止牛只坠入剑河

---

## 63. 纳米颗粒-细胞连接实现转基因表达的电磁无线编程

**原文标题**: Nanoparticle-cell link enables EM wireless programming of transgene expression

**原文链接**: [https://phys.org/news/2025-05-nanoparticle-cell-interface-enables-electromagnetic.html](https://phys.org/news/2025-05-nanoparticle-cell-interface-enables-electromagnetic.html)

这篇2025年5月18日Phys.org的文章报道了苏黎世联邦理工学院的研究人员开发的一种新方法，该方法利用纳米粒子和细胞之间的界面，无线控制哺乳动物的基因表达。这种方法被称为EMPOWER（无线表达调控的电磁编程），旨在解决传统基因治疗方法的挑战，这些方法可能具有侵入性、不精确或缺乏稳健性。

该方法的核心是生物相容性纳米粒子，由多铁性内核和壳聚糖外层组成。当暴露于低频电磁场时，这些纳米粒子在细胞内产生安全水平的活性氧（ROS）。研究人员对哺乳动物细胞进行了基因工程改造，使其具有对ROS敏感的基因回路，从而激活NRF2通路以产生治疗性蛋白质，例如胰岛素。

一个关键优势是可以精确、非侵入性地控制基因表达的位置和时间。与基于纳米粒子的其他无线基因控制技术相比，该方法具有高度生物相容性，所需的纳米粒子剂量低，并且最大限度地减少了脱靶效应。

在一个糖尿病小鼠模型中，每天暴露于微弱的电磁场（1 kHz，21 mT）三分钟，可以有效地控制胰岛素分泌并维持正常的血糖水平。研究人员目前正在探索其在肿瘤学、神经病学和再生医学中的应用，同时也在努力提高系统的灵敏度、生物相容性和效率。他们还计划使EM刺激设备更加紧凑，以便临床使用。

---

## 64. 基于结果的强化学习预测未来

**原文标题**: Outcome-Based Reinforcement Learning to Predict the Future

**原文链接**: [https://arxiv.org/abs/2505.17989](https://arxiv.org/abs/2505.17989)

本文《基于结果的强化学习预测未来》探讨了使用具有可验证奖励的强化学习(RLVR)进行预测，并使其适应现实世界预测场景中常见的二元、延迟和噪声奖励所带来的挑战。作者Turtel等人证明，应用于14B语言模型的纯结果在线强化学习可以实现具有竞争力的预测准确性和优于前沿基线(o1)的校准。

他们为此目的调整了两种领先的强化学习算法：组相对策略优化(GRPO)和ReMax。关键的调整包括在GRPO中移除每个问题的方差缩放，以及在ReMax中使用基线减去优势。训练过程通过10万个合成生成的、时间上一致的问题以及轻量级的防护措施来增强，以防止产生无意义或不相关的回复。

通过将ReMax扩展到11万个问题并集成七个预测，由此产生的14B模型匹配了基线o1的准确性（Brier得分为0.193），同时显著提高了校准（ECE为0.042）。这种改进的校准转化为预测市场模拟中的127美元的假设利润，而o1的利润为92美元。研究结果表明，改进的RLVR技术可以有效地利用较小的语言模型进行具有经济价值的预测，突出了将这些方法扩展到更大模型的潜力。

---

## 65. 使其规模化：一个Aurora DSQL的故事

**原文标题**: Just make it scale: An Aurora DSQL story

**原文链接**: [https://www.allthingsdistributed.com/2025/05/just-make-it-scale-an-aurora-dsql-story.html](https://www.allthingsdistributed.com/2025/05/just-make-it-scale-an-aurora-dsql-story.html)

本文详细介绍了 Aurora DSQL 的开发历程，这是一款专为 AWS 提供的无服务器可扩展性和零运维开销而设计的关系型数据库。由于最初基于 JVM 的架构在横向扩展写入和处理垃圾回收导致的读取延迟方面面临挑战，该团队探索了替代方案。

他们决定采用 Rust 用于数据平面，最初从 Adjudicator 组件开始。结果非常显著：Rust 实现比优化的 Kotlin 版本快 10 倍。这一成功促使他们决定用 Rust 重写整个数据平面。

在基于 PostgreSQL 构建其查询处理能力的同时，团队最初考虑使用 C 来开发扩展。然而，意识到使用新的 C 代码会带来引入新的内存安全错误的风险，他们转而使用 Rust 进行扩展开发。这使他们能够利用 Rust 的内存安全特性并构建强制执行安全内存访问模式的抽象。

关键的结论是，团队的迭代方法、挑战现有假设的意愿以及最终对 Rust 的战略性拥抱，对于克服构建 Aurora DSQL 中的性能和可扩展性挑战至关重要。转向 Rust 显著提高了性能、内存安全性和整体工程效率。

---

## 66. Clojure 多核处理器

**原文标题**: Clojure MCP

**原文链接**: [https://github.com/bhauman/clojure-mcp](https://github.com/bhauman/clojure-mcp)

Clojure MCP 是一个 alpha 阶段的项目，它为 Clojure 提供 AI 辅助的开发环境，并围绕 REPL 驱动的开发构建。它将 AI 模型连接到 Clojure nREPL 服务器，并提供专门的编辑工具，从而创造全面的 Clojure 开发体验。

主要功能包括：Clojure REPL 连接、智能编辑 (clj-kondo, parinfer, cljfmt, clj-rewrite) 和一组为 Clojure 优化的精选工具。它旨在与最新的 LLM（如 Claude 4、Gemini 2.5 和 OpenAI 模型）配合使用。该系统跟踪文件读/写操作以确保安全，防止冲突并确保可靠的文件识别。

安装涉及克隆存储库，使用 MCP 服务器设置配置目标项目的 `deps.edn` 文件，并设置 Claude Desktop 以连接到 MCP 服务器。该项目还使用 PROJECT_SUMMARY.md 文件来帮助 LLM 快速了解代码库结构。

MCP 包含各种工具，分为只读、代码评估、文件编辑和代理工具（需要来自 Google、OpenAI 或 Anthropic 的 API 密钥）。值得注意的工具包括用于智能文件读取的 `read_file`、用于结构感知编辑的 `clojure_edit` 和用于自主搜索任务的 `dispatch_agent`。

通过将核心 MCP API 与实现分离来支持自定义。欢迎投稿，包括错误报告、功能建议和 pull request。

---

## 67. 为什么在JavaScript中2025/05/28和2025-05-28是不同的日期？

**原文标题**: Why are 2025/05/28 and 2025-05-28 different days in JavaScript?

**原文链接**: [https://brandondong.github.io/blog/javascript_dates/](https://brandondong.github.io/blog/javascript_dates/)

本文解释了 JavaScript 的 `Date` 对象在解析日期字符串（如 '2025/05/28' 和 '2025-05-28'）时表现出的不一致行为。核心问题在于解析没有明确时区的日期字符串时，存在的时区歧义。

JavaScript 的 `Date` 始终表示一个特定的时间点（自 epoch 以来的毫秒数）。虽然 '2025/05/28' 通常被解释为本地时间，但 '2025-05-28' 通常被解析为 UTC 时间。这种差异源于多年来不同浏览器对 ISO 8601 标准不断发展且常常不一致的实现。作者追溯了主要浏览器（Chrome、Firefox、Safari）处理日期字符串解析的历史，以及它们在使用本地时间和 UTC 之间来回切换的变化。

作者强调了在超过十年的时间里，当缺少时区偏移量时，主要浏览器行为不一致的情况。Chrome 甚至在此期间多次在本地时间和 UTC 之间切换。

文章随后介绍了 Temporal，JavaScript 即将推出的日期和时间 API，旨在解决这些问题。Temporal 允许表示纯粹的日期（没有时区的日期），避免了将仅包含日期的字符串解析为特定时间点的歧义。如果需要解析为时间上的某个瞬间，Temporal 则需要显式的偏移量或时区标识符。

最后，文章还谈到了 `Date` 构造函数的宽松解析行为，展示了看似荒谬的字符串有时是如何被解析为有效日期的。

---

## 68. SpaceX可能解决了一个问题，却在最新的星舰飞行中发现了更多问题。

**原文标题**: SpaceX may have solved one problem, only to find more on latest Starship flight

**原文链接**: [https://arstechnica.com/space/2025/05/spacex-may-have-solved-one-problem-only-to-find-more-on-latest-starship-flight/](https://arstechnica.com/space/2025/05/spacex-may-have-solved-one-problem-only-to-find-more-on-latest-starship-flight/)

SpaceX星舰最新试飞展现进展，但也暴露新挑战。火箭成功发射并达到预定轨道，克服了此前飞行的问题，但在滑行和重返大气层阶段因燃料箱泄漏失控，导致提前结束。这阻碍了对改进型隔热罩的全面测试，而隔热罩是未来可重复使用性的关键部件。

尽管遇到挫折，但成功的初始飞行和发动机关机是进步。本次任务标志着超重型助推器的首次重复使用，尽管它在着陆点火时爆炸。未能打开货舱门也阻止了计划中的星链卫星部署测试。

埃隆·马斯克承认数据丢失，但强调“有很多有用的数据需要审查”，暗示下次发射会很快进行。SpaceX的目标是更快的发射频率，可能每三到四周一次，并且已经在研发具有进一步改进的Block 3星舰设计。美国联邦航空管理局正在试飞后“积极”与SpaceX合作。SpaceX工程师正在研究星舰燃料泄漏和助推器爆炸的原因，以改进未来的飞行。

---

## 69. 天文图像中的颜色是“真实”的吗？

**原文标题**: Are the Colors in Astronomical Images 'Real'?

**原文链接**: [https://www.scientificamerican.com/article/are-the-colors-in-space-real/](https://www.scientificamerican.com/article/are-the-colors-in-space-real/)

天文图像的色彩是“真实的”吗？

---

## 70. 开发者过时的神话

**原文标题**: The Myth of Developer Obsolescence

**原文链接**: [https://alonso.network/the-recurring-cycle-of-developer-replacement-hype/](https://alonso.network/the-recurring-cycle-of-developer-replacement-hype/)

本文旨在揭穿关于开发者会被新技术（如无代码、云计算以及现在的AI辅助开发）淘汰的反复出现的谬论。虽然这些技术承诺消除对开发者的需求，但实际上它们转变了开发者的角色，并且通常会增加对熟练工程师的需求和价值。

作者认为，每一次“革命”（无代码、云计算、离岸外包、AI）都遵循一种可预测的模式：最初关于替代的炒作让位于对这些技术创造了需要专门知识的新复杂性的认识。无代码产生了无代码专家，云计算将系统管理员转变为DevOps工程师，而离岸开发则突出了对更强大的架构和沟通技巧的需求。

核心论点是，虽然AI可以生成代码，但它无法构建整个系统。软件工程中最有价值的技能不是编写代码本身（在维护和调试方面是一种负担），而是设计和管理整体系统架构。AI擅长局部优化，但在全局设计方面却很吃力，使得架构错误更容易融入到系统中。

因此，AI辅助开发不会取代开发者，而是会提升系统架构和设计技能的重要性。能够有效地协调AI系统并管理快速生成的代码所带来的日益增长的复杂性的工程师将拥有很高的需求。能够生存和繁荣的技能是系统架构，而这正是AI目前无法复制的。

---

## 71. 我从杜克大学学生丢弃的物品中捡回了价值六千美元的奢侈品。

**原文标题**: I salvaged $6k of luxury items discarded by Duke students

**原文链接**: [https://indyweek.com/culture/duke-students-dumpster-diving/](https://indyweek.com/culture/duke-students-dumpster-diving/)

莉娜·盖勒住在达勒姆一栋主要居住着杜克大学学生的公寓楼里，她在学年结束时发现了楼内垃圾房里大量被丢弃的奢侈品。她抢救了价值从 900 美元的亚克力桌子到巴黎世家拖鞋、华伦天奴运动鞋和 Lululemon 服装等物品，估计总价值约为 6000 美元。

盖勒的发现凸显了学生的过度浪费，促使她调查杜克大学和其他大学的捐赠项目。她的研究表明，杜克大学的本科生人均捐赠率与其他富有的私立院校相当。

除了经济收益外，盖勒的经历也引发了复杂的情绪。虽然她喜欢清洁和修补抢救回来的物品，但她也对大量的浪费感到不知所措和沮丧，并觉得自己的东西不足够。最后一次笨拙的捡拾之旅，最终以一次溢出和一个不合适的空气滤清器告终，引发了一次情绪崩溃。最终，一台抢救回来的手持吸尘器为持续存在的家庭问题提供了一个实际的解决方案，为她的捡拾努力提供了一个小的、切实的好处。这次经历突出了被丢弃物品的潜在价值与面对如此浪费所带来的情感损失之间的对比。

---

## 72. GitHub MCP 漏洞利用：通过 MCP 访问私有仓库

**原文标题**: GitHub MCP exploited: Accessing private repositories via MCP

**原文链接**: [https://invariantlabs.ai/blog/mcp-github-vulnerability](https://invariantlabs.ai/blog/mcp-github-vulnerability)

本文详细描述了 GitHub MCP（托管代码平台）集成中的一个严重漏洞，攻击者可以通过“有毒代理流程”访问私有仓库。该攻击涉及将恶意提示注入到公共 GitHub Issue 中，当用户代理（如 Claude Desktop）访问该 Issue 时，会强制代理泄露来自私有仓库的数据。

攻击展开过程是，当用户提示其代理查看公共仓库中的 Issue 时，代理遇到包含提示注入的恶意 Issue，从而诱骗代理从私有仓库提取数据，并创建一个包含敏感信息的公共拉取请求。

此漏洞并非存在于 MCP 服务器代码本身，而是源于代理容易受到来自 GitHub 等外部平台上不受信任的信息的影响。即使像 Claude 4 Opus 这样最先进的 AI 模型也容易受到攻击。

本文强调，仅靠模型对齐不足以阻止此类攻击，并提倡采取系统级安全措施。缓解策略包括实施细粒度的权限控制（如 Invariant Guardrails），以限制代理仅访问必要的仓库，并使用 Invariant 的 MCP-scan 等专用扫描器进行持续的安全监控，以实时检测威胁。这些措施有助于防止跨仓库信息泄漏，并为识别潜在漏洞提供审计跟踪。文章最后敦促各组织采取这些安全措施，以确保大规模负责任地部署代理系统。

---

## 73. 继深度伪造 YouTube 之后，谷歌 Veo 3 可能接下来会让电子游戏变得粗糙。

**原文标题**: After Deepfaking YouTube, Google's Veo 3 Could Slop-Ify Video Games Next

**原文链接**: [https://gizmodo.com/after-deepfaking-youtube-googles-veo-3-could-slop-ify-video-games-next-2000608209](https://gizmodo.com/after-deepfaking-youtube-googles-veo-3-could-slop-ify-video-games-next-2000608209)

詹姆斯·佩罗在Gizmodo上的文章探讨了谷歌新款视频生成器Veo 3对AAA级游戏产业的潜在影响。虽然Veo 3可以制作出逼真的伪造游戏画面，但该文章侧重于这些人工智能生成的视频如何融入游戏开发流程。

文章强调了用户如何将Veo 3与3D工具结合，以创建可定制且细致的游戏资源。这使得基于文本提示的快速原型设计和视觉开发成为可能，从而能够更快地生成游戏环境和角色。

作者随后过渡到对人工智能编码的讨论。虽然目前的人工智能技术无法完全编写AAA级游戏，但生成式人工智能辅助游戏开发已成为一种明显趋势。谷歌自己在2023年也承认了人工智能降低开发成本的潜力。佩罗表达了担忧，认为这种快速发展可能导致游戏开发者失业，以及“人工智能垃圾”的出现，并可能因过度依赖人工智能生成的内容和潜在的版权侵权而降低游戏的质量和原创性。文章以谨慎的乐观态度结尾，既承认了人工智能增强游戏开发的潜力，也强调了不加控制地采用人工智能的风险。

---

## 74. LiveStore：基于响应式SQLite的状态管理，内置同步引擎

**原文标题**: LiveStore: State management based on reactive SQLite and built-in sync engine

**原文链接**: [https://livestore.dev](https://livestore.dev)

LiveStore：基于响应式SQLite和Git风格同步引擎的新一代状态管理框架，专为高性能、本地优先的应用设计。它旨在通过提供以客户端为中心的数据层和基于事件溯源的实时同步，来取代Redux或MobX等解决方案。

主要特性包括：

*   **响应式SQLite数据库：** 提供即时、响应式的查询能力以及高效的数据持久化。
*   **内置同步引擎：** 使用事件溯源，实现跨客户端的复杂同步场景。
*   **类型安全Schema：** 提供强大的API，用于符合人体工程学的数据建模，无需数据库迁移。
*   **跨平台支持：** 适配Web、移动、服务器/边缘计算和桌面平台。
*   **卓越的DX和开发者工具：** 一流的开发者工具，用于数据检查和调试，类似于Chrome DevTools。
*   **本地优先架构：** 专为离线优先工作流程设计，支持自定义合并冲突解决方案。

LiveStore的工作流程包括提交事件（这些事件会被持久化到事件日志中）、通过物化器刷新数据库以及同步到其他客户端。开发者将事件定义为Schema的一部分，并使用物化器通过SQL将这些事件映射到状态变化。响应式查询用于高效地检索和更新数据。

虽然功能强大，但LiveStore并非一个开箱即用的框架，也不适用于所有用例，例如与现有数据库同步、提供托管服务、扩展到无限数据或点对点同步。 它专为需要坚实数据基础、真正离线优先能力和灵活数据建模的开发者而设计。

---

## 75. UI 的未来是多彩且立体的。

**原文标题**: The UI future is colourful and dimensional

**原文链接**: [https://www.flarup.email/p/the-future-is-colourful-and-dimensional](https://www.flarup.email/p/the-future-is-colourful-and-dimensional)

迈克尔·弗拉鲁普认为，UI设计正从扁平化设计转向一种更具色彩和维度的风格，他称之为“Diamorph”。这种设计拥抱深度、纹理和光线，旨在创造富有表现力和趣味性的界面，使其感觉原生于屏幕，而不必模仿现实世界。

弗拉鲁普以Airbnb最近的重新设计为例，说明了这一趋势，并指出了其他发展，如Big Sur图标和更丰富的照明模型。他认为，这种转变使设计师能够超越扁平化与拟物化之间的限制性二分法。

文章还探讨了人工智能在加速Diamorph设计采用方面的作用。人工智能工具现在可以相对轻松地生成详细的、立体的图标，降低了创建这种风格的门槛。虽然承认对人工智能对艺术技能的影响的担忧，但弗拉鲁普将其视为一种可以通过处理材料、光线和颜色等技术方面来增强创造力的工具。他强调，构图和品味等核心设计技能仍然至关重要。

最终，弗拉鲁普认为Diamorph设计代表着向前迈出的一步，创造了富有表现力、情感化且毫不掩饰的数字界面。他预计，随着人工智能使维度设计更容易获得，更多的人将加入这一趋势，从而带来更富有想象力和乐趣的用户体验。

---

## 76. 冥王星的极端表亲？太阳系边缘或存潜在矮行星

**原文标题**: An Extreme Cousin for Pluto? Possible Dwarf Planet at Solar System Edge

**原文链接**: [https://www.ias.edu/news/extreme-cousin-pluto-possible-dwarf-planet-discovered-solar-systems-edge](https://www.ias.edu/news/extreme-cousin-pluto-possible-dwarf-planet-discovered-solar-systems-edge)

2025年5月，由程思豪带领的普林斯顿高等研究院团队宣布发现了一个新的海王星外天体(TNO) 2017 OF201，它可能是一颗矮行星，位于太阳系边缘。该天体因其极端轨道而引人注目，远日点是地球轨道的1600倍，近日点与冥王星相似，估计大小为700公里。这个轨道大约需要25000年才能完成，表明它曾经历过引力相互作用，可能涉及被抛射到奥尔特云。

与许多极端TNO不同，2017 OF201不遵循一些科学家认为指示存在第九行星的聚集模式。 它作为一个异常值可能挑战这一假设。 这项发现暗示，此前被认为很大程度上是空旷地带的柯伊伯带以外的区域，可能包含更多类似的物体，但由于距离太远而无法探测到。 程估计可能有数百个这样的物体。

该发现还突出了开放科学的力量，因为该天体是使用公开的天文图像数据库数据识别出来的。这表明研究人员、学生和公民科学家都可以为突破性发现做出贡献，而无需使用世界上最大的望远镜。

---

## 77. Show HN：Nvidia Warp 中的 3DGS 实现：简洁、精简、可在 CPU 和 GPU 上运行

**原文标题**: Show HN: 3DGS implementation in Nvidia Warp: clean, minimal, runs on CPU and GPU

**原文链接**: [https://github.com/guoriyue/3dgs-warp-scratch](https://github.com/guoriyue/3dgs-warp-scratch)

此"Show HN"帖子介绍了一个使用NVIDIA Warp实现的极简Python版3D高斯溅射(3DGS)。其主要优势在于它无需CUDA配置即可在CPU和GPU上运行，使其易于学习和实验。该项目强调清晰性和并行性，与更大、更复杂的代码库相比，为理解现代图形和可微渲染提供了一个更容易理解的切入点。

该实现提供了诸如正向和反向传播（基于graphdeco-inria/gaussian-splatting）、损失函数以及用于相机处理、点云I/O和数学运算的实用程序等基本组件。它包含一个训练脚本、渲染脚本和配置文件，以便使用提供的乐高数据集进行轻松实验。密度化和剪枝逻辑的灵感来自yzslab/gaussian-splatting-lightning，但为了更轻松的训练而进行了简化。

作者承认有待改进的领域，包括Warp中的性能优化和更有效的剪枝策略来过滤非活动点。该项目根据GNU Affero通用公共许可证v3.0获得许可。 本质上，它被呈现为一个干净、可破解和具有教育意义的资源，用于理解和原型化3DGS，使其适合学习、研究，并可能用于教学。

---

## 78. Docusaurus 和 Starlight 的比较以及我们转换的原因

**原文标题**: Comparing Docusaurus and Starlight and why we made the switch

**原文链接**: [https://glasskube.dev/blog/distr-docs/](https://glasskube.dev/blog/distr-docs/)

Glasskube 将开源控制平面 Distr 的文档从 Docusaurus 切换到 Starlight。文章从设计、SEO、开发者体验 (DevEx) 和可扩展性等方面比较了这两个框架。

**主要对比：**

*   **设计：** Docusaurus 严重依赖 Infima，与易于集成 Tailwind CSS 的 Starlight 相比，Infima 成熟度较低且更难定制。
*   **SEO：** 两者都提供必要的 SEO 功能，如站点地图生成和元数据，主要通过 Starlight 中的插件实现。
*   **DevEx：** Starlight 基于 Astro 构建，与 Docusaurus（基于 React）相比，提供更快的开发服务器启动时间。由于依赖项较少，维护 Starlight 文档似乎也更容易。作者发现 Starlight 更令人愉快。
*   **可扩展性：** Docusaurus 更适合创建营销页面和博客以及文档。 Starlight 专注于文档。

**切换到 Starlight 的原因：**

更快的开发服务器启动、现代化的外观和感觉以及更好的开发者体验是切换的主要原因。

**文档结构与风格：**

文章强调构建文档结构，引导用户从基本概念到用例，再到技术细节。它建议在写作风格上优先考虑清晰性、简洁性和视觉效果，以最大限度地提高用户的理解。

**结论：**

尽管在营销页面和缺少 Mermaid 集成方面存在挑战，但 Glasskube 对切换到 Starlight 后带来的改进的 DevEx 和现代设计感到满意。他们推荐 Starlight，并计划在未来的项目中使用它。

---

## 79. 人工智能作业机器时代的教学尝试

**原文标题**: Trying to teach in the age of the AI homework machine

**原文链接**: [https://www.solarshades.club/p/dispatch-from-the-trenches-of-the](https://www.solarshades.club/p/dispatch-from-the-trenches-of-the)

来自巴特勒圣战前线的报道：作者探讨了日益增长的反人工智能情绪，尤其是在创意专业人士中，并分享了他们在人工智能时代教学的个人经历。他们将此与《沙丘》中的巴特勒圣战相提并论，即对模仿人类思维的机器的抵制。

作者指出，ChatGPT等人工智能的主要“杀手级应用”是作弊。尽管最初对人工智能作为教育工具抱有希望，但担忧正在增加。学生可以使用人工智能绕过真正的学习，跳过必要的困难，并在不真正理解基础材料的情况下产生输出。作者亲眼目睹了在自己的课堂上人工智能使用量的显著增加，即使在积极参与的学生中也是如此。

检测人工智能生成的作品变得越来越困难，导致教师和学生之间更加对立的关系。作者发现评分和反馈更具挑战性，因为他们难以确定学生作品的真实性。他们认为，让人工智能为学生思考和写作是一种损害，将其比作在健身房使用叉车。

作者强调了学习基本写作技能的重要性，并批评了与机器人撰写的文本进行互动时精神麻木的体验。他们还指出，学生们意识到并对技术（包括人工智能）在他们生活中无处不在的影响感到沮丧。作者建议，出于发展和教育的原因，考虑对年轻人使用人工智能进行限制，类似于对吸烟、饮酒和赌博的限制。

最后，作者强调了人工智能驱动的作弊行为在教育之外的更广泛影响，指出它存在于商业、法律和科学领域，并可能对真相和准确性产生危险的后果。他们将其与19世纪晚期的鸦片酊/海洛因热潮进行比较，暗示人工智能可能成为一种有害的成瘾，并产生广泛的负面影响。

---

## 80. 丹麦新石器时代“太阳石”祭祀活动使火山爆发后的太阳复苏

**原文标题**: Neolithic 'sun stones' sacrificed in Denmark revives sun after volcanic eruption

**原文链接**: [https://archaeologymag.com/2025/01/neolithic-sun-stones-sacrificed-in-denmark/](https://archaeologymag.com/2025/01/neolithic-sun-stones-sacrificed-in-denmark/)

新石器时代丹麦献祭“太阳石”或为火山爆发后重现阳光

---

## 81. 毛巾里的猫头鹰

**原文标题**: Owls in Towels

**原文链接**: [https://owlsintowels.org/](https://owlsintowels.org/)

这篇文章题为《毛巾里的猫头鹰》，主要讲述了“迷人的北美栗鸮”这个引人入胜的主题。虽然提供的内容简短限制了摘要的深度，但中心主题显然是这种特定类型的猫头鹰——北美栗鸮——的吸引力和魅力。 标题本身唤起了一种异想天开和不同寻常的感觉，暗示这篇文章可能包含猫头鹰的图片或描述，也许是被营救或被照顾的，裹在毛巾里。“迷人的”这个形容词强调了猫头鹰的可爱之处，暗示这篇文章很可能会突出其使其特别吸引观众的身体特征或行为。 对“北美栗鸮”的关注表明正在展示一个特定的物种，这表明该文章也可能有限地涉及其栖息地、饮食或保护状况。 在没有更多上下文的情况下，摘要仅限于其暗示性元素：这篇文章可能旨在呈现一幅关于北美栗鸮的有利和可爱的肖像。

---

## 82. 精通Vim语法

**原文标题**: Mastering Vim Grammar

**原文链接**: [https://irian.to/blogs/mastering-vim-grammar](https://irian.to/blogs/mastering-vim-grammar)

本文旨在通过理解 Vim 的底层“语法”（作者称之为“Vimish”）来指导读者更熟练地使用 Vim。其核心概念是大多数 Vim 命令都遵循“动词 + 名词”的结构，一旦掌握了这个原则，Vim 就会变得更加直观。

作者将此比作语言学习，提倡增加词汇量、理解语法规则以及持续练习。

本文重点介绍三个核心动词：`y`（复制）、`d`（删除）和 `c`（修改）。“名词”包括用于导航的移动命令（例如，`h/j/k/l`、`w`、`b`、`0/$`），以及至关重要的文本对象（例如，`iw`、`ip`、`i{`、`a"`），它们允许对单词、段落、括号、引号等执行操作。使用“i”指定“内部”内容，而使用“a”指定“外部”内容。

文章强调了组合这些动词和名词的强大功能，并给出了诸如 `dw`（删除单词）、`y$`（复制到行尾）和 `di(`（删除括号内的内容）之类的示例。可以添加量词（例如，`d2w` 表示删除两个单词）。

除了基本的移动命令和文本对象之外，作者还介绍了搜索（例如 `f/F`、`t/T`、`//?`）和标记（`ma`）作为可以与操作符一起使用的其他名词。

文章强调，理解这种语法可以带来直觉，使使用者能够轻松地将诸如 `gu`（小写）和 `gU`（大写）之类的操作符应用于各种名词。精通需要持续练习才能形成肌肉记忆。

---

## 83. Hacker News 现在运行于 Common Lisp 之上

**原文标题**: Hacker News now runs on top of Common Lisp

**原文链接**: [https://lisp-journey.gitlab.io/blog/hacker-news-now-runs-on-top-of-common-lisp/](https://lisp-journey.gitlab.io/blog/hacker-news-now-runs-on-top-of-common-lisp/)

Hacker News (HN) 至少从 2024 年 9 月起，已从 Racket 迁移到 SBCL（一种 Common Lisp 实现），这得益于名为 Clarc 的新 Arc 实现带来的性能提升。这一变化消除了长评论线程中对分页的需求。

由“dang”（可能是 Paul Graham）开发的 Clarc 使 HN 有可能利用多核处理。Clarc 的开发采用分阶段方法，Arc 在各层（arc0、arc1、arc2）中重建，以简化重新实现。Arc0 是唯一直接依赖于底层系统（Racket、Javascript 或 Common Lisp）的层。

虽然可以通过将原始 Arc 版本移植到 Clarc 来开源 Clarc 本身，但由于存在专有的反滥用措施，发布当前的 HN 代码库是不可行的。移除这些措施将是一项重大工程。文章作者祝贺团队成功且无感知地完成了过渡。

---

## 84. 从OpenAPI规范到MCP：我们如何构建Xata的MCP服务器

**原文标题**: From OpenAPI spec to MCP: How we built Xata's MCP server

**原文链接**: [https://xata.io/blog/built-xata-mcp-server](https://xata.io/blog/built-xata-mcp-server)

本文详细介绍了 Xata 如何构建其模型上下文协议 (MCP) 服务器，该服务器允许 AI 模型安全地与 Xata 的 API 交互。采用的方法是从他们现有的 OpenAPI 规范生成 MCP 服务器，利用 API 的 schema 作为单一事实来源，从而确保一致性和快速开发。

核心策略围绕一种混合方法：从 OpenAPI 自动生成基础框架，然后对其进行调整以适应实际的 AI 使用。本文概述了三个步骤：

1. **迁移到 Kubb：** 由于 Kubb 的灵活性以及生成多种输出的能力，他们切换到 Kubb 用于 OpenAPI 代码生成。
2. **定制 Kubb：** 创建自定义生成器，从 OpenAPI 规范生成 TypeScript API 客户端和 MCP 工具处理程序，从而确保 API 和 AI 接口之间的一致性。 实施了 Zod schema 用于输入验证。
3. **使用 Next.js 构建 MCP 服务器：** 他们使用 Next.js 和 Vercel 的 MCP 适配器来实现服务器，受益于 Vercel 的无缝部署、无服务器功能以及便捷的路由/中间件功能。

Next.js API 路由利用 `createMcpHandler` 注册生成的工具，使用 `withAuth` 包装器处理身份验证，并支持 SSE 和 HTTP 传输与 AI 代理通信。本文强调了调整生成工具、提供清晰描述以及使用 Zod 进行验证的重要性。 通过将 OpenAPI 规范视为可执行的知识，Xata 能够快速创建一个强大的 AI 集成。

---

## 85. 如何消失——走进极端隐私顾问的世界

**原文标题**: How to disappear– Inside the world of extreme-privacy consultants

**原文链接**: [https://www.theatlantic.com/ideas/archive/2025/05/extreme-personal-data-privacy-protection/682867/](https://www.theatlantic.com/ideas/archive/2025/05/extreme-personal-data-privacy-protection/682867/)

本文探讨了极端隐私顾问的世界，以及人们为了在数字时代消失所付出的努力。文章介绍了HavenX公司的首席执行官亚历克·哈里斯，该公司为名人、富裕家庭和加密货币企业家等高端客户提供极端隐私和安全服务。哈里斯通过虚拟借记卡、一次性电话号码、匿名信托和虚假信息等手段，精心保护自己的隐私。

文章强调，由于数据泄露、监控资本主义以及勒索和绑架等现实威胁（尤其是在加密货币领域），对隐私的需求日益增长。HavenX将自身定位为复杂隐私问题的精品解决方案提供商。

文章还深入探讨了前网络犯罪侦探、《极端隐私》一书的作者迈克尔·巴泽尔的影响，他成为一位隐私大师，为客户提供从公众视野中消失的建议。巴泽尔的技术，如在南达科他州建立居住地和使用数据投毒，现在被认为是该领域的标准。有趣的是，巴泽尔本人在2023年从互联网和公共生活中消失，为对极端隐私的追求增添了另一层神秘色彩。

---

## 86. 互动式癌症风险矩阵

**原文标题**: Interactive Cancer Risk Matrix

**原文链接**: [https://www.wcrf.org/research-policy/interactive-cancer-risk-matrix/](https://www.wcrf.org/research-policy/interactive-cancer-risk-matrix/)

本文介绍了一种互动式癌症风险矩阵，旨在告知用户饮食、营养、身体活动与癌症风险之间的关系。该互动工具允许用户探索饮食、体重和身体活动的不同方面如何与癌症风险相关联。

该矩阵使用三个级别对支持这些联系的证据强度进行分类：“令人信服”或“可能”，表示有力的证据，适用于支持癌症预防建议；以及“有限-暗示性”，表示证据不足以提出建议。文章强调，虽然该矩阵提供信息，但个人结论不应被视为独立的建议。

文章还提供可下载的矩阵，一个展示强有力的证据，另一个涵盖所有癌症。文章重点介绍了该组织评估证据的严谨过程，概述了评估的因素以及研究的依据。最后，文章提到了他们的资助计划，这些计划资助的研究重点是饮食、体重、营养和身体活动对癌症预防的影响。

---

## 87. 幕后：白领的血腥厮杀

**原文标题**: Behind the Curtain: A white-collar bloodbath

**原文链接**: [https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic](https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic)

无法访问文章链接。

---

## 88. Stalwart的日历、联系人和文件

**原文标题**: Calendars, Contacts and Files in Stalwart

**原文链接**: [https://stalw.art/blog/collaboration/](https://stalw.art/blog/collaboration/)

Stalwart v0.12 是一项重大更新，它将 Stalwart 从邮件服务器转变为综合通信和协作平台，通过原生集成日历、联系人和文件存储实现。这消除了对第三方解决方案的需求，并提供 CalDAV、CardDAV 和 WebDAV 支持，用于管理事件、地址簿和文档。它还提供强大的共享功能，包括 WebDAV ACL 支持，用于细致的权限管理。

该版本还包括改进的垃圾邮件过滤，可以从用户地址簿中学习并根据用户更正自动调整。已实施显著的性能增强，包括增量缓存和零拷贝反序列化，从而缩短响应时间并降低 CPU 使用率，尤其是在大型多节点环境中。集群协调现在具有适应性，在较小的部署中使用 Eclipse Zenoh，并为较大的基础设施提供对 Apache Kafka、Redpanda、NATS 或 Redis 的支持。

v0.12.1 的未来增强功能将包括 CalDAV 调度 (RFC 6638) 和基于电子邮件的事件通知。Stalwart 还计划支持用于日历、联系人和文件存储的 JMAP，以提供一种现代且高效的替代传统协议的方案。这旨在进一步简化用户体验并减少带宽使用。

---

## 89. 写作中的逻辑运用

**原文标题**: Using Logic in Writing

**原文链接**: [https://owl.purdue.edu/owl/general_writing/academic_writing/logic_in_argumentative_writing/logic_in_writing.html](https://owl.purdue.edu/owl/general_writing/academic_writing/logic_in_argumentative_writing/logic_in_writing.html)

这篇普渡大学在线写作实验室(OWL)的文章强调了在构建书面论证时有效运用逻辑的重要性。它指出，仅仅理解逻辑三段论是不够的；作者必须积极且有意识地以逻辑方式构建他们的论证。

文章强调了将逻辑三段论转化为有说服力的书面论证的三个关键步骤：清晰地陈述每个前提，为每个前提提供证据，并明确地与结论建立联系。文章提供了关于最低工资的糟糕论证示例，并与一个展示这些原则的修订版本进行了对比。

“糟糕”的例子缺乏逻辑结构，假定听众的认同，并且没有提供任何支持证据。然而，修订后的例子建立了一个三段论（最低工资应该与生活成本相匹配；它没有；因此，应该提高），并用段落详细阐述每个前提，提供证据和数据。

文章强调，逻辑论证并非固有地无懈可击，因为具有不同前提的对立观点可以挑战它。主要的结论是，作者必须有意识地构建他们的论证，以确保清晰度，提供支持证据，并明确地将前提与结论联系起来，以实现有效的说服。

---

## 90. NVLink融合：拥抱、扩展、消灭

**原文标题**: NVLink Fusion: Embrace, Extend, Extinguish

**原文链接**: [https://www.fabricatedknowledge.com/p/nvlink-fusion-embrace-extend-extinguish](https://www.fabricatedknowledge.com/p/nvlink-fusion-embrace-extend-extinguish)

本文分析了英伟达授权其C2C（芯片间）互连技术并销售NVLink芯粒的策略，该策略的背景是其在高性能计算（HPC）和人工智能（AI）领域的竞争优势。作者认为，英伟达正在对UALink等竞争互连标准采用“拥抱、扩展、消灭”的策略。

具体而言，英伟达授权C2C技术，主要针对CPU和多芯片加速器项目，从而能够与GPU更紧密地集成，尤其是在HPC领域。 这通过加速GPU的采用和渗透到CPU密集型领域来使英伟达受益。

更重要的是，英伟达正在销售NVLink芯粒，而不是授权该技术。 作者认为，这是一个保持差异化和锁定用户的有意的举动。 虽然英伟达表面上正在开放其生态系统，但实际上是将NVLink定位为纵向扩展加速器结构的默认标准。

文章认为，由多家公司支持的开放规范UALink由于利益冲突而进展缓慢。 通过提供即用型NVLink芯粒，英伟达提供了一种更快、更容易获得的解决方案。 这使英伟达可以“拥抱”潜在客户，比UALink更快地“扩展”其路线图，并最终通过使其生态系统成为高性能互连的唯一可行选择来“消灭”竞争。 作者认为，依赖英伟达提供这种“黄金螺丝”是一个错误，但由于缺乏替代方案，竞争对手别无选择。

---

## 91. 直接偏好优化与人类反馈强化学习

**原文标题**: Direct Preference Optimization vs. RLHF

**原文链接**: [https://www.together.ai/blog/direct-preference-optimization](https://www.together.ai/blog/direct-preference-optimization)

本文深入探讨了直接偏好优化 (DPO)，作为一种替代人类反馈强化学习 (RLHF) 的方法，用于使语言模型与人类偏好对齐。DPO 通过直接基于偏好数据（提示词、偏好回复、非偏好回复）训练模型来简化对齐过程，而无需中间奖励模型或在线采样。它调整模型权重，以支持偏好回复，抑制非偏好回复。

本文重点介绍了 DPO 相对于 RLHF 的优势，包括其简洁性、计算效率以及匹配或超越 RLHF 性能的能力。文章解释说，DPO 就像直接利用顾客偏好来修改现有食谱以改进食谱一样，而 RLHF 就像聘请美食评论家来指导食谱改进。

本文还建议将监督微调 (SFT) 与 DPO 相结合，以获得最佳效果，SFT 首先教导模型基本任务结构和响应格式，然后再使用 DPO 进行细化。当提示词不足、人类可以轻松比较回复以及对现有模型进行受控改进时，DPO 尤其有用。

理想的用例包括聊天机器人回复、摘要、代码生成、问答和写作辅助。本文提供了有关关键超参数（如 `dpo-beta`）以及在 DPO 微调期间监控指标（如准确性和 KL 散度）的指导。文章还提到，DPO 不太适合具有单一正确答案的任务，例如信息提取或数学计算。

---

## 92. 波峰鸟 - Nintendo WaveBird协议的开源实现

**原文标题**: WavePhoenix – Open-source implementation of the Nintendo WaveBird protocol

**原文链接**: [https://github.com/loopj/wavephoenix](https://github.com/loopj/wavephoenix)

WavePhoenix：使用现代Silicon Labs Wireless Gecko SoC复刻任天堂WaveBird手柄功能的开源项目。该项目旨在通过提供DIY替代方案，解决原版WaveBird接收器供应日渐减少和价格上涨的问题。

该项目包含固件和硬件组件。固件包括`libwavebird`（WaveBird协议实现）、`libsi`（GameCube/Wii手柄通信）、接收器应用程序以及固件更新的引导程序。硬件是一个基于RF-BM-BG22C3模块的简单、经济高效的接收器设计，包括PCB设计和一个3D打印外壳。

该项目建立在现有的WaveBird协议和GameCube手柄协议的逆向工程文档之上。它通过创新地使用SoC外设，克服了与DSSS调制、数据包解码和SI总线通信相关的挑战。

主要成就包括实时数据包解码、精确的SI总线通信以及信道选择/配对机制。尽管性能接近原版WaveBird，但作者指出仍有改进空间，尤其是在无线电调谐方面。

未来的开发想法包括为自定义WaveBird手柄创建发射器固件，为N64游戏机适配接收器，以及创建用于更广泛兼容性的USB HID加密狗。该项目感谢多个个人和社区的贡献，并以MIT和Solderpad许可证发布。

---

## 93. 使用布隆过滤器的无损视频压缩

**原文标题**: Lossless video compression using Bloom filters

**原文链接**: [https://github.com/ross39/new_bloom_filter_repo/blob/main/README.md](https://github.com/ross39/new_bloom_filter_repo/blob/main/README.md)

ross39 的 "new_bloom_filter_repo" 仓库探索了使用布隆过滤器进行无损视频压缩。其核心思想是利用布隆过滤器的高效性和紧凑性来识别并消除视频数据中的冗余，从而实现无数据损失的压缩。

虽然标题暗示了一种新颖的方法，但仓库本身提供的关于具体算法或实现的信息很少。 标题突出了关键要素：无损压缩，这对于数据完整性至关重要的应用至关重要；以及布隆过滤器，这是一种提供高效成员资格测试的概率数据结构。

根据名称判断，该方法可能使用布隆过滤器来检测视频序列中的重复块或帧。 通过有效地识别这些重复项，系统可以仅存储唯一的数据块，并用对原始数据的引用替换冗余的出现，从而实现压缩。“无损”方面意味着可以从压缩表示中完美地重建原始视频。

人气指标（8 个 fork 和 218 个 star）表明社区对此有一些兴趣，但从提供的信息中，实现的实际细节及其有效性并不明显。 需要进一步调查仓库的代码和文档，才能了解此方法的具体算法和性能特征。

---

## 94. 小罗伯特·肯尼迪威胁禁止联邦科学家在顶级期刊上发表文章

**原文标题**: RFK Jr threatens ban on federal scientists publishing in top journals

**原文链接**: [https://www.theguardian.com/us-news/2025/may/28/rfk-jr-medical-journals](https://www.theguardian.com/us-news/2025/may/28/rfk-jr-medical-journals)

小罗伯特·F·肯尼迪，特朗普政府时期的美国卫生部长，威胁要禁止政府科学家在《柳叶刀》、《新英格兰医学杂志》和《美国医学会杂志》等顶尖医学期刊上发表文章，称这些期刊“腐败”，受制于制药公司。肯尼迪计划创建州立替代出版物，认为美国国立卫生研究院（NIH）的资助将使在这些出版物上发表文章的研究人员合法化，并使他们“卓越”。

这些期刊极具影响力，向全球数百万读者传播同行评审的研究成果。肯尼迪还指责他监管的卫生机构（NIH、CDC、FDA 和 CMS）是制药行业的“傀儡”。

与此同时，美国国立卫生研究院的资金大幅削减（超过 30 亿美元），并据报道解雇了 2 万名卫生部门工作人员。最近一份白宫报告质疑了关于疫苗的医学共识，并暗示制药公司的影响阻止了对儿童慢性病病因的适当研究。

哈佛医学院的亚当·加夫尼等批评人士认为，这种禁令将使纳税人资助的研究失去合法性。肯尼迪通过引用期刊编辑过去对制药公司影响的担忧来为自己的立场辩护。据报道，这种情况已促使一些美国科学家考虑移居国外。

---

## 95. 石头剪刀布对决

**原文标题**: Rock, paper, scissors showdown

**原文链接**: [https://luduxia.com/showdown/](https://luduxia.com/showdown/)

名为“石头剪刀布对决”的文章很可能介绍石头剪刀布游戏。由于缺乏关于文章具体内容的更多信息，很难提供详细的总结。但是，我们可以假设它至少涵盖以下几个方面：

*   **基本规则：** 解释如何玩石头剪刀布，包括石头、剪刀和布的手势，以及获胜组合（石头砸剪刀，剪刀剪布，布包石头）。

*   **战略要素：** 可能讨论获胜策略，例如识别对手的出手模式或使用心理战术来影响他们的选择。

*   **历史和流行度：** 可能会深入探讨游戏的起源及其作为一种简单、易上手且通常具有竞争性的消遣方式的持久魅力。

*   **变体和锦标赛：** 可能会提及游戏的变体或石头剪刀布锦标赛的存在，突出其竞争性。

*   **数学概率：** 可能会探讨涉及的数学概率和游戏的随机性，尽管技巧仍然是一个因素。

简而言之，预计这篇文章会概述石头剪刀布游戏，涵盖其规则、潜在策略和文化意义。

---

## 96. 微软正在监视其AI工具用户 (2024)

**原文标题**: Microsoft Is Spying on Users of Its AI Tools (2024)

**原文链接**: [https://www.schneier.com/blog/archives/2024/02/microsoft-is-spying-on-users-of-its-ai-tools.html](https://www.schneier.com/blog/archives/2024/02/microsoft-is-spying-on-users-of-its-ai-tools.html)

微软被指“监视”AI工具用户

---

## 97. 下载与流媒体的区别

**原文标题**: The Difference Between Downloading and Streaming

**原文链接**: [https://danq.me/2025/05/26/downloading-vs-streaming/](https://danq.me/2025/05/26/downloading-vs-streaming/)

本文认为，流媒体和下载之间的区别在很大程度上是人为的。从根本上说，两者都涉及服务器向用户设备发送数据（视频、音频等），然后该设备存储这些数据。关键区别在于设备在播放后如何处理这些数据。流媒体意味着数据在观看后被丢弃，而下载则涉及将数据保留为永久文件。

作者强调，从某种意义上说，所有流媒体都是下载，因为流媒体播放器使用缓冲，这需要临时存储媒体帧。作者认为，删除或保留媒体的决定最终取决于用户，这使得平台对“下载”的限制在某种程度上毫无意义，并依赖于荣誉制度。用户有各种方法可以规避这些限制并保存流媒体内容。

本文承认流媒体和下载存在差异的三个例外：

1. **传输顺序：** 流媒体需要按时间顺序传输，而下载的文件可以以任何顺序到达。
2. **转码：** 流媒体通常会进行即时转码以适应连接速度，而下载的媒体通常提供更高质量的选项。
3. **DRM：** 流媒体更有可能受到数字版权管理 (DRM) 的保护，尽管作者认为 DRM 从根本上说是“注定失败的军备竞赛”，并且合法用户比“盗版者”更容易遭受此类技术的困扰。

总之，作者认为流媒体和下载之间的主要区别在于*期望*接收者在消费后删除媒体。

---

## 98. Gitlab Duo中的远程提示注入导致源代码泄露

**原文标题**: Remote Prompt Injection in Gitlab Duo Leads to Source Code Theft

**原文链接**: [https://www.legitsecurity.com/blog/remote-prompt-injection-in-gitlab-duo](https://www.legitsecurity.com/blog/remote-prompt-injection-in-gitlab-duo)

Legit研究团队在GitLab Duo（集成到GitLab中的AI助手）中发现了一个远程提示注入漏洞，该漏洞可能导致源代码盗窃和其他恶意活动。攻击者可以通过在合并请求、提交消息、问题描述或源代码中嵌入隐藏提示来操纵Duo的行为。

该漏洞利用了Duo对整个页面上下文的分析来生成答案，使其容易受到注入指令的影响。攻击者使用Unicode走私、Base16和KaTeX等编码技巧来隐藏这些提示。这使他们能够操纵代码建议，将恶意URL呈现为安全URL，甚至影响合并请求的审查。

此外，Duo的流式markdown渲染容易受到HTML注入攻击。通过将原始HTML注入到实时渲染的内容中，攻击者可以控制页面的部分内容，从而可以通过<img>标签和其他元素进行数据泄露。这被用于从私有项目中泄露源代码，方法是指示Duo检索代码更改，将其编码为base64，然后将其嵌入到URL中。

攻击场景涉及将隐藏提示嵌入到公共项目中，当受害者用户与之交互时，会导致Duo注入包含敏感源代码的恶意<img>标签。该技术也可用于泄露机密的issue数据，包括零日漏洞。

GitLab此后已通过阻止Duo渲染不安全的HTML标签来修补HTML和提示注入漏洞。该事件强调了在将AI助手集成到开发工作流程中时，需要采取强大的安全措施，将用户控制的内容视为潜在的恶意内容，以防止意外和有害的结果。

---

## 99. 从空气中被动捕获水的新型材料

**原文标题**: A new class of materials that can passively harvest water from air

**原文链接**: [https://blog.seas.upenn.edu/penn-engineers-discover-a-new-class-of-materials-that-passively-harvest-water-from-air/](https://blog.seas.upenn.edu/penn-engineers-discover-a-new-class-of-materials-that-passively-harvest-water-from-air/)

宾夕法尼亚大学工程学院的研究人员发现了一种新型纳米结构材料，能够被动地从空气中收集水分。这种材料在《科学进展》中有所描述，它将亲水性纳米孔与疏水性聚合物以独特的纳米级结构融合在一起。这使得它能够从空气中捕获水分，同时将其释放为水滴，而无需外部能量输入。

该材料依赖于毛细管凝聚，但与水滞留在其中的典型纳米多孔材料不同，这种材料允许水在孔内凝结，然后从表面溢出。这些水滴也表现出意想不到的稳定性，能够抵抗蒸发。这种独特的行为源于亲水性纳米颗粒和疏水性聚乙烯聚合物之间的“最佳平衡点”，创造了一个水滴与孔内不断补充的储水池相连的系统。

这一发现具有在干旱地区被动收集水分、冷却电子设备和智能涂层方面的潜在应用。该材料由常见的、可扩展的成分制成，使其在现实应用中具有潜在的实用性。研究团队现在专注于优化材料的成分、扩大生产规模和提高水滴收集效率。他们希望这项技术能在未来提供清洁的水和可持续的冷却解决方案。

---

## 100. Jjui – 咒术回战的精美 TUI

**原文标题**: Jjui – A Nice TUI for Jujutsu

**原文链接**: [https://github.com/idursun/jjui](https://github.com/idursun/jjui)

Jjui 是一款终端用户界面 (TUI)，旨在提升 Jujutsu 版本控制系统的使用体验。它提供了一系列功能来简化常见的 Jujutsu 操作。

主要功能包括：具有签名帮助的智能 revset 补全；修订和分支的交互式变基；轻松合并修订；详细的修订查看，包含分割、恢复和 diff 文件等选项；书签管理；用于恢复操作的操作日志访问；以及用于检查修订详情、文件差异和操作日志的预览窗口。预览窗口提供滚动和差异查看功能。

其他功能包括修订差异比较、编辑修订描述、创建、分割、放弃、吸收和编辑修订、执行 Git 推送/拉取、撤销更改以及查看修订的 evolog。

Jjui 可以根据用户偏好进行配置，并通过 Homebrew、Archlinux (AUR)、Nix、`go install`、从源代码构建以及预构建的二进制文件支持安装。它需要 Jujutsu v0.21 或更高版本。该项目欢迎通过 pull requests 进行贡献。

---

