# Hacker News 热门文章摘要 (2025-09-06)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 996

**原文标题**: 996

**原文链接**: [https://lucumr.pocoo.org/2025/9/4/996/](https://lucumr.pocoo.org/2025/9/4/996/)

Armin Ronacher 的博文《996》讨论了公司推崇“996”工作文化（早 9 点到晚 9 点，每周工作 6 天）这种有问题的趋势。他承认自己热爱高强度工作和深夜编程，但认为这不应成为常态或公司的积极标志。

Ronacher 强调了工作与生活平衡的重要性，特别是对于有家庭和个人兴趣的人来说。他区分了创始人的奉献精神（他们的风险和杠杆与员工不同）以及期望员工遵守如此艰苦的作息时间之间的区别。他批评那些推崇这种模式的创始人是不负责任的。

他认为成功是一场马拉松，而不是短跑，可持续的生产力比在办公室里花费的时间更重要。虽然他喜欢偶尔通宵，但他强调这应该是个人的选择，而不是公司文化的要求，并承认它们造成的生产力低下后果。最终，Ronacher 倡导抵制对 996 工作文化的推崇，强调这种模式的不可持续性和潜在危害性。他认为产出和满足感比单纯的工作时长更重要。

---

## 2. DuckDuckGo创始人：应禁止人工智能监控

**原文标题**: DuckDuckGo founder: AI surveillance should be banned

**原文链接**: [https://gabrielweinberg.com/p/ai-surveillance-should-be-banned](https://gabrielweinberg.com/p/ai-surveillance-should-be-banned)

本文中，DuckDuckGo的创始人主张禁止人工智能监控，强调其相比传统在线追踪放大了隐私风险。他认为，由于人工智能聊天机器人的对话特性和收集详细个人信息的能力，它们会创建全面的性格侧写，容易受到商业和政治操纵。他指出，这些侧写可能被利用，通过定制化的论点和微妙的产品推荐来影响用户。

他强调，围绕搜索引擎的隐私辩论更适用于人工智能聊天。虽然DuckDuckGo提供受保护的聊天机器人对话和匿名人工智能辅助搜索，但他指出，隐私泄露已经发生，并引用了Grok泄露的对话和Perplexity易受黑客攻击等例子。他警告说，OpenAI设想的全面“超级助手”以及Anthropic默认对用户对话的训练。

鉴于美国缺乏通用的在线隐私法，作者呼吁国会迅速采取行动，确保受保护的聊天成为标准做法。他警告说，进一步拖延将巩固有害的隐私实践，重蹈在线追踪的覆辙。他总结说，DuckDuckGo将继续为寻求在线效率而不牺牲隐私的用户提供尊重隐私的服务，包括人工智能。他主张在为时已晚之前禁止人工智能监控。

---

## 3. Qwen3 30B A3B 在 4 个树莓派 5 上达到 13 token/s

**原文标题**: Qwen3 30B A3B Hits 13 token/s on 4xRaspberry Pi 5

**原文链接**: [https://github.com/b4rtaz/distributed-llama/discussions/255](https://github.com/b4rtaz/distributed-llama/discussions/255)

本文详细描述了一项实验，该实验成功地在由四台树莓派5 8GB设备组成的集群上运行了Qwen3 30B A3B语言模型。该实验使用了Distributed Llama框架（版本0.16.0），并将模型量化到Q40。树莓派通过TP-Link交换机连接并分配工作负载。

主要结果强调了所实现的性能：系统在评估期间达到了14.33 tokens/秒，在预测期间达到了13.04 tokens/秒。本文档提供了用于运行推理的具体命令，并展示了详细的输出，包括网络初始化、权重加载和令牌生成过程。它指出了模型的内存需求、正在使用的CPU特性以及分布式工作节点之间的同步时间。用于推理的提示是一个关于波兰位置的简单问题。模型生成的响应将波兰置于相对于其他国家的地理环境中。

本文档还展示了模型的架构和配置（Qwen3 MoE，包括隐藏维度、层数和头数以及rope theta等参数），并提供了分布式llama设置的版本信息。

---

## 4. 理解大型语言模型所需的数学基础

**原文标题**: The maths you need to start understanding LLMs

**原文链接**: [https://www.gilesthomas.com/2025/09/maths-for-llms](https://www.gilesthomas.com/2025/09/maths-for-llms)

Giles 的这篇博文解释了理解大型语言模型 (LLM) 如何运作所需的基本数学知识，重点在于推理（使用现有 AI），而非训练过程。它面向具有基本技术背景但没有深入 AI 知识的读者。

涵盖的核心概念是向量和高维空间。向量不仅仅是数字数组，还代表 n 维空间中的距离和方向，在 LLM 中，它们代表 logits 和含义。Giles 介绍了“词汇空间”，其中 logits（下一个 token 的可能性）被表示为向量，并重点介绍了“混乱”（未归一化）和整洁（归一化）版本的词汇空间。独热向量，即只有一个元素设置为 1 的向量，也被作为一个概念引入。

该文章随后深入探讨了“嵌入空间”，其中向量代表含义，相似的概念聚集在一起。这些向量的长度并不总是关键；方向更重要。

接下来，Giles 解释了矩阵（堆叠的向量）如何通过矩阵乘法用于不同多维空间之间的投影。具体来说，一个 d1×d2 矩阵将 d1 维空间投影到 d2 维空间。他强调，这种投影可能是有损的，这意味着信息可能在降维过程中丢失。

最后，该文章将矩阵乘法与神经网络联系起来，表明一个单层计算，在简化后，本质上是一个矩阵乘法，从而强调了矩阵在理解 LLM 中的重要性。神经网络中的权重矩阵的作用类似于投影矩阵，有助于转换和抽象。

---

## 5. 最早记录的交易

**原文标题**: Oldest Recorded Transaction

**原文链接**: [https://avi.im/blag/2025/oldest-txn/](https://avi.im/blag/2025/oldest-txn/)

这篇文章探讨了现代数据库在处理极其古老日期时的局限性，起因是一张5000年前的苏美尔交易记录图片。作者调查了MySQL、Postgres和SQLite支持的最早时间戳。MySQL的限制是公元1000年，而Postgres和SQLite利用儒略历，可以追溯到公元前4713年1月1日。

作者成功地将公元前4713年插入到Postgres和SQLite中，但在尝试插入公元前4714年时遇到错误，表明了这些数据库的下限。这一限制引发了如何存储和管理比公元前4713年更早的日期的问题，例如英国博物馆等机构的历史记录。

文章考虑了潜在的解决方案，包括将日期存储为 epoch 时间戳、文本字符串或使用自定义系统。一个关键的挑战是在使用这些替代存储方法时，如何保持标准 TIMESTAMP 操作的功能。作者最后感谢了贡献者，并引用了初始图片来源和 Joran Dirk Greef 的相关演讲。

---

## 6. Anthropic 同意支付 15 亿美元与图书作者达成和解

**原文标题**: Anthropic agrees to pay $1.5B to settle lawsuit with book authors

**原文链接**: [https://www.nytimes.com/2025/09/05/technology/anthropic-settlement-copyright-ai.html?unlocked_article_code=1.jk8.bTTt.Zir9wmtPaTp2&smid=url-share](https://www.nytimes.com/2025/09/05/technology/anthropic-settlement-copyright-ai.html?unlocked_article_code=1.jk8.bTTt.Zir9wmtPaTp2&smid=url-share)

无法访问文章链接。

---

## 7. 扎克伯格在白宫晚宴上被意外录到私下谈话

**原文标题**: Zuckerberg Caught in Revealing Hot Mic Moment During White House Dinner

**原文链接**: [https://www.pcmag.com/news/zuckerberg-caught-in-revealing-hot-mic-moment-during-white-house-dinner](https://www.pcmag.com/news/zuckerberg-caught-in-revealing-hot-mic-moment-during-white-house-dinner)

白宫晚宴：科技巨头与特朗普讨论AI投资，扎克伯格或夸大Meta投资额

---

## 8. 我们黑了汉堡王：认证绕过如何导致了得来速音频监控

**原文标题**: We Hacked Burger King: How Auth Bypass Led to Drive-Thru Audio Surveillance

**原文链接**: [https://bobdahacker.com/blog/rbi-hacked-drive-thrus/](https://bobdahacker.com/blog/rbi-hacked-drive-thrus/)

好的，以下是基于所提供URL内容对“我们入侵了汉堡王：认证绕过如何导致得来速语音监控”文章的总结作者BobDaHacker详细描述了他们如何发现并利用Restaurant Brands International (RBI) 在线订购平台上的一个漏洞，该漏洞影响了汉堡王的得来速服务。该漏洞使他们能够绕过身份验证，访问敏感的客户数据，甚至可以收听来自得来速对讲机的实时音频流。

最初的漏洞源于一个未正确实施的API端点，该端点用于员工身份验证和菜单更新。通过操纵API请求，作者能够在不需要有效凭据的情况下冒充餐厅经理。这种未经授权的访问使他们能够查看餐厅的特定数据，包括销售额、员工信息（用户名、哈希密码），以及关键的得来速通信系统的配置设置。

该漏洞利用最令人担忧的方面是能够收听来自得来速的实时音频。作者发现了为远程监控和维护得来速系统而设计的API端点，其中包括访问实时音频流的权限。这使他们能够窃听顾客在得来速窗口的订单和对话，引发了严重的隐私问题。

作者负责任地向RBI披露了这些漏洞，RBI承认了这个问题并实施了修复。该博客文章详细介绍了识别和利用这些漏洞的技术步骤，强调了在线系统中正确身份验证和授权机制的重要性，特别是那些处理敏感客户数据并可能启用音频监控的系统。作者还建议RBI进行定期的安全审计和渗透测试，以防止将来出现类似的漏洞。

---

## 9. 让我们摆脱它，愤怒的GitHub用户们如是说，针对强制Copilot功能。

**原文标题**: Let us git rid of it, angry GitHub users say of forced Copilot features

**原文链接**: [https://www.theregister.com/2025/09/05/github_copilot_complaints/](https://www.theregister.com/2025/09/05/github_copilot_complaints/)

本文报道了GitHub用户对强制整合微软AI服务Copilot日益增长的不满。一个热门社区讨论帖要求提供一种方法来阻止Copilot生成问题和拉取请求，而另一个则指出无法禁用Copilot代码审查。这些请求尚未得到回应，加剧了用户的沮丧。

开发者Andi McClure对Copilot基于GitHub发布的代码进行训练以及Copilot“广告”入侵其工作流程表示担忧。其他开发者也对Copilot传播不准确信息、代码建议引发的版权问题以及缺乏代码正确性保证表示担忧。包括Servo、GNOME的Loupe、FreeBSD、Gentoo、NetBSD和QEMU在内的多个项目已禁止AI代码贡献，原因正是这些问题。

文章指出，对Copilot整合的不满，加上GitHub整合到微软CoreAI集团，正推动开发者转向替代平台，如Codeberg和自托管的Forgejo实例。软件自由保护协会(SFC)长期以来一直倡导远离GitHub。一些开发者已经迁移了他们的代码，并用搬迁通知替换了他们的GitHub仓库。

文章最后提到McClure的观察，即微软默认启用功能并在用户禁用后反复重新引入这些功能的策略正在加剧问题。她认为，避免Copilot的唯一方法是停止使用任何出现它的微软产品，尽管由于GitHub近乎垄断和网络效应，这很困难。最终，开发者担心微软对AI指标的推动正在掩盖客户保留。

---

## 10. 宝宝的第一个类型检查器

**原文标题**: Baby's first type checker

**原文链接**: [https://austinhenley.com/blog/babytypechecker.html](https://austinhenley.com/blog/babytypechecker.html)

本文介绍了一个Python中“婴儿类型检查器”的实现，逐步讲解构建一个基本类型检查工具的过程。它解释了类型检查的工作原理，强调了它在及早发现错误和充当文档方面的作用。与C++等语言不同，Python没有内置的类型检查器，而是依赖于运行时错误或第三方工具。

本文概述了该方法：使用`ast`模块解析Python代码，识别类型注解，并验证类型兼容性。它介绍了`SymbolCollector`类，一个`ast.NodeVisitor`子类，用于查找和保存函数和变量的类型注解。核心逻辑围绕检查赋值和函数调用展开。

本文涵盖了处理原始类型、列表、字典和类型联合等基本方面。它定义了一个兼容性检查(`is_compatible`)，以确保分配的类型与声明的类型匹配。代码示例展示了如何扩展类型检查器以支持各种数据结构和操作，例如索引和字面量的类型推断。它演示了类型检查器如何在示例Python代码片段中识别类型错误。本文引导读者逐步开发类型检查器，强调了类型检查中涉及的挑战和复杂性，并提供了GitHub上完整代码的链接。

---

## 11. Rug pulls、分叉和开源封建主义

**原文标题**: Rug pulls, forks, and open-source feudalism

**原文链接**: [https://lwn.net/SubscriberLink/1036465/e80ebbc4cee39bfb/](https://lwn.net/SubscriberLink/1036465/e80ebbc4cee39bfb/)

这篇2025年9月5日发表于LWN.net的文章探讨了开源软件开发中的权力动态，重点关注“拔地毯”（重新许可为更严格的许可证）和“分叉”（从现有代码创建新项目）作为转移权力的策略。Dawn Foster在2025年欧洲开源峰会上发表讲话，强调了公司，尤其是云提供商，如何利用其对小型公司、贡献者和用户的权力。

该文章详细介绍了Elastic重新许可Elasticsearch（导致亚马逊的OpenSearch分叉）、Hashicorp的Terraform（导致OpenTofu分叉）和Redis（导致Valkey分叉）等案例。Foster分析了这些事件发生前后贡献者的构成，发现由用户发起或拥有先前存在的外部贡献者的分叉，在建立活跃社区方面更成功。

Foster建议贡献者和用户警惕授予公司重新许可权力的贡献者许可协议（CLA），偏爱具有中立治理和多样化贡献者基础的项目，并积极为他们依赖的项目做出贡献。文章总结说，虽然重新许可被用来对抗云提供商的统治地位，但它可能会损害贡献者，他们随后依赖分叉作为重新获得控制权的一种手段。文章还提到了一场关于SSPL许可证是否为自由许可证的讨论，评论员对其定义和限制意见不一。

---

## 12. 我们写给互联网中继聊天的一封情书 [视频]

**原文标题**: Our love letter to Internet Relay Chat [video]

**原文链接**: [https://www.youtube.com/watch?v=6UbKenFipjo](https://www.youtube.com/watch?v=6UbKenFipjo)

这似乎是一个名为“我们写给互联网中继聊天的情书”的YouTube视频，而提供的“内容”仅仅是标准的YouTube页脚信息。

因此，仅凭提供的信息无法对视频的*内容*进行总结。我们只知道：

*   **标题：** 视频是一封献给互联网中继聊天（IRC）的“情书”。这表明它很可能对IRC持积极或怀旧的态度。
*   **平台：** 该视频托管在YouTube上。
*   **标准的YouTube法律信息：** 包含的文本是关于版权、法律条款、广告、开发者、隐私、安全以及谷歌整体版权的标准YouTube声明。这*并不能*告诉我们任何关于视频内容的信息。

要获得适当的摘要，需要观看视频本身。

---

## 13. 不生成未使用的工具提示来加速Unreal Editor的启动

**原文标题**: Speeding up Unreal Editor launch by not spawning unused tooltips

**原文链接**: [https://larstofus.com/2025/09/02/speeding-up-the-unreal-editor-launch-by-not-spawning-38000-tooltips/](https://larstofus.com/2025/09/02/speeding-up-the-unreal-editor-launch-by-not-spawning-38000-tooltips/)

本文探讨了一种通过优化工具提示创建来加速 Unreal Editor 启动时间的方法。作者发现编辑器在启动期间会创建大量工具提示（在一个简单的项目中大约 38,000 个），即使大多数从未使用过。此过程涉及生成完整的工具提示小部件，包括子小部件和辅助对象，从而消耗大量时间和内存。

作者提出了一种解决方案，即将工具提示文本保存为属性，而不是立即生成小部件。实际的小部件创建被推迟到需要工具提示时，即当用户将鼠标悬停在相关的 UI 元素上时。

这种“按需”创建显著减少了启动时间，而不会明显影响运行时性能。作者认为用户不太可能在单个会话中访问所有工具提示，并且创建单个工具提示的速度足够快（在调试版本中为 0.05 毫秒），不会影响帧速率。

作者提供了包含建议代码更改的 pull request 的链接，并提到了一项更新，澄清了许多工具提示来自可选来源，例如项目设置和编辑器首选项面板。关闭这些面板可以减少启动期间创建的工具提示数量，从而加快加载速度。

---

## 14. 用于规范LLM协作的软件开发方法

**原文标题**: A Software Development Methodology for Disciplined LLM Collaboration

**原文链接**: [https://github.com/Varietyz/Disciplined-AI-Software-Development](https://github.com/Varietyz/Disciplined-AI-Software-Development)

本文档概述了一种“严谨的AI软件开发方法”，旨在解决在软件开发中与AI模型协作时遇到的代码膨胀、架构漂移和上下文稀释等问题。该方法强调在四个阶段中进行系统性约束和实证验证。

**阶段1（AI配置）** 涉及使用 `AI-PREFERENCES.md` 为AI模型设置自定义指令，以建立行为约束和不确定性标记。

**阶段2（协作计划）** 侧重于与AI合作定义项目范围、识别组件、合理构建阶段，以及生成带有可衡量检查点的系统性任务，并记录在 `METHODOLOGY.md` 中。

**阶段3（系统化实施）** 涉及按阶段实施组件，将文件大小保持在150行以下，以提高上下文管理和专注度。这包括请求-验证-基准测试-继续的流程。

**阶段4（数据驱动迭代）** 利用基准测试套件（在阶段0中构建）提供性能数据，然后将数据反馈给AI，以便根据测量结果进行优化。

该方法提倡基于聚焦请求的决策处理、通过小文件和有限问题进行上下文管理、使用性能数据进行实证验证，以及通过架构检查点和文件大小限制进行系统性约束。

该文档包括使用此方法开发的项目示例、实施步骤、质量保证措施以及项目状态提取工具 (`project_extract.py`)，用于生成结构化的代码库快照，以便与AI共享。它还包括一个FAQ部分和一个流程图，以可视化工作流程。

---

## 15. 游戏模糊效果（以及最佳效果的实现原理）

**原文标题**: Video Game Blurs (and how the best one works)

**原文链接**: [https://blog.frost.kiwi/dual-kawase/](https://blog.frost.kiwi/dual-kawase/)

本文介绍了模糊在视频游戏后处理中的重要性，它被用于景深、泛光和GUI元素等效果。文章旨在引导读者了解实时模糊技术的演变，强调数学理论与技术限制之间的权衡。

文章使用交互式WebGL可视化来演示不同的模糊技术及其性能特征。它侧重于实现实时模糊，并探索各种技术，最终讨论双Kawase模糊算法。

交互式演示允许用户试验不同的模式（场景、光照、泛光），以了解模糊算法在各种用例中的表现。用户可以调整光照亮度等参数，并观察其对性能（FPS、帧时间）和视觉质量的影响。文章还提供了用于这些模糊技术的着色器代码的见解。

起始点演示了一个未应用任何模糊的场景渲染，为后续章节中实施和比较不同的模糊算法奠定了基础。文章还涉及了不同模糊技术的性能考量及其对各种应用的适用性。

---

## 16. 新型空芯光纤以创纪录的低损耗更快地传输数据

**原文标题**: Novel hollow-core optical fiber transmits data faster with record low loss

**原文链接**: [https://phys.org/news/2025-09-hollow-core-optical-fiber-transmits.html](https://phys.org/news/2025-09-hollow-core-optical-fiber-transmits.html)

2025年9月2日Phys.org文章报道，空芯光纤(HCF)技术取得重大突破，有望彻底改变数据传输。南安普顿大学和微软的研究人员开发出一种新型HCF设计，在1550纳米波长下实现了0.091分贝/公里的创纪录低损耗，超过了传统硅基光纤0.14分贝/公里的最低损耗。这种新型光纤还拥有快45%的传输速度，并在66太赫兹带宽内保持0.2分贝/公里左右的低损耗。

该创新解决了硅芯光纤的局限性，过去40年来，硅芯光纤在降低损耗方面一直停滞不前。虽然理论上HCF由于光在空气中传播速度更快而提供更快的速度，但以前的设计难以超越硅电缆的性能。这种新型设计，一种嵌套反谐振无节点空芯光纤(DNANF)，通过先进的建模最大限度地减少泄漏、表面散射和微弯，克服了这些挑战。

所实现的低损耗使得信号能够在无需放大的情况下传输更远的距离，从而实现更快的互联网、更高效的网络，并有可能在以前无法访问的波长下实现低损耗传输。研究人员认为，进一步的改进可以将损耗降低到低至0.01分贝/公里。潜在的应用包括海底和陆地电缆中更长的未放大跨度、高功率激光传输和传感。作者表示，随着产量的增加和几何一致性的提高，DNANF HCF将成为关键的波导技术。该研究发表在《自然·光子学》(Nature Photonics)上（DOI: 10.1038/s41566-025-01747-5）。

---

## 17. 使用Clojure开发太空飞行模拟器

**原文标题**: Developing a Space Flight Simulator in Clojure

**原文链接**: [https://www.wedesoft.de/software/2025/09/05/clojure-game/](https://www.wedesoft.de/software/2025/09/05/clojure-game/)

本文详细介绍了过去五年用Clojure开发太空飞行模拟器的过程。作者受Orbiter 2016的启发，选择Clojure是因为其不变性、并行特性、快速数据结构和多方法。最初的重点是解决复杂的图形渲染问题：行星、大气层、阴影和体积云，使用了OpenGL以及从检查Orbiter的开源代码中获得的知识。

该项目使用了各种Clojure和Java库，包括用于图形的LWJGL、用于物理模拟的Jolt Physics、用于数学运算的Fastmath、用于着色器模板的Comb以及用于解析NASA空间数据的Instaparse/Gloss。开发的一个重要部分是使用NASA的Bluemarble和高程数据高效渲染行星表面，这需要生成和管理大量的地图瓦片。大气渲染采用了Bruneton的预计算大气散射，其中计算密集型表格生成使用`pmap`进行并行化。

性能优化策略包括使用ZGC垃圾收集器、启用反射警告和未检查的数学警告，以及利用`clj-async-profiler`来识别瓶颈。该项目使用`tools.build`来管理构建和生成Uberjar，并使用Packr为Linux和Windows创建原生可执行文件。Steam部署涉及创建多个存储仓库来存放数据和平台特定的二进制文件。未来的工作包括添加更详细的图形、音效和更多的天体，以及探索Modding功能。源代码可在Github上找到，游戏可以被加入愿望单。

---

## 18. 12.5光年内的宇宙

**原文标题**: The Universe Within 12.5 Light Years

**原文链接**: [http://www.atlasoftheuniverse.com/12lys.html](http://www.atlasoftheuniverse.com/12lys.html)

本文概述了距离太阳12.5光年内的恒星。该文强调，在此半径范围内有33颗恒星，其中绝大多数是昏暗的红矮星，约占宇宙中所有恒星的80%。比邻星是距离太阳最近的恒星，也是一颗典型的红矮星。

本文包含指向其他地图的链接，这些地图显示了地球相对于这些恒星的位置以及20光年内的恒星地图。此外，本文还提供了数据和目录，其中包含20光年内的恒星列表以及多星系统的动画。

各个条目描述了各种著名的恒星，包括太阳、比邻星（一颗耀星，也是半人马座α星系统的一部分）、半人马座α星A和B（一个明亮的双星系统）、巴纳德星（以其高自行而闻名）、沃尔夫359、拉兰德21185、天狼星A和B（夜空中最亮的恒星，拥有一颗白矮星伴星）、Luyten 726-8 A和B（一个耀星系统）、罗斯154、罗斯248、天苑星（有证据表明可能存在太阳系，并探测到一颗木星大小的行星）、拉卡伊9352、罗斯128、Luyten 789-6 A、B、C（一个三红矮星系统）、南河三A和B、天鹅座61 A和B、Struve 2398 A和B、Groombridge 34 A和B、Giclas 51-15、印第安座ε星A、B、C（被棕矮星环绕）、鲸鱼座τ星以及Luyten 372-58、Luyten 725-32和卢伊滕星。每个条目都详细介绍了恒星的类型、星等、距离以及任何独特的特征或历史意义。有几颗恒星因是耀星而备受关注。此外，文章指出，一些恒星曾被研究是否存在智慧生命的迹象。

---

## 19. 富有目的性的动画

**原文标题**: Purposeful animations

**原文链接**: [https://emilkowal.ski/ui/you-dont-need-animations](https://emilkowal.ski/ui/you-dont-need-animations)

本文强调在用户界面中使用有目的且精心设计的动画的重要性。虽然动画可以通过使界面感觉反应灵敏、可预测和令人愉快来增强用户体验，但如果使用不当，也会产生不利影响。

核心信息是动画应始终服务于某个目的，无论是解释功能、提供反馈还是增添一丝乐趣。在实施动画之前，至关重要的是要考虑其使用频率。重复使用的动画可能会变得令人烦恼并降低用户速度，在某些情况下，不使用动画才是最佳解决方案，特别是对于像 Raycast 的命令菜单这样经常使用的功能。

本文还强调了速度的重要性。用户界面动画，尤其是与核心功能相关的动画，应快速（低于 300 毫秒）以提高感知性能并保持响应速度。更快的动画使应用程序看起来反应更快。工具提示被用作一个主要例子。初始延迟应该存在，以避免工具提示随机且无目的地出现。然而，连续的工具提示应该在没有动画的情况下打开。

最终目标是创建用户友好的界面，虽然动画可以在其中发挥作用，但应仔细考虑并在考虑到目的、频率和速度的情况下实施。有时，最好的动画就是没有动画。

---

## 20. GLM 4.5与Claude代码

**原文标题**: GLM 4.5 with Claude Code

**原文链接**: [https://docs.z.ai/guides/llm/glm-4.5](https://docs.z.ai/guides/llm/glm-4.5)

本文介绍了GLM-4.5，这是Z.AI推出的新型语言模型，专为面向Agent的应用设计，尤其为Claude Code用户提供优质编码体验，起价为每月3美元。GLM-4.5采用混合专家模型（MoE）架构，并提供多个版本，包括GLM-4.5、GLM-4.5-Air、GLM-4.5-X、GLM-4.5-AirX和GLM-4.5-Flash。它在15万亿个tokens上进行训练，并针对代码、推理和Agent任务进行微调，上下文长度为128k个tokens。

主要功能包括深度思考、流式输出、函数调用、上下文缓存和结构化输出（JSON）。GLM-4.5集成了先进的推理、编码和Agent能力，在基准测试中名列前茅。它比DeepSeek-R1和Kimi-K2等竞争对手拥有更高的参数效率，以更少的参数实现顶级性能。其API定价为每百万输入tokens 0.2美元起，每百万输出tokens 1.1美元起，高速版本超过每秒100个tokens。

实际评估表明，GLM-4.5在Agent编码场景中表现出极具竞争力的性能，尤其是在工具调用和任务完成率方面。该模型支持Python、JavaScript和Java的编码技能。用户可以通过`thinking.type`参数控制“思考模式”，以适应不同的复杂程度。本文档提供了基本API调用和流式API调用的代码示例（cURL、Python、Java）。

---

## 21. 制作我的手写字体

**原文标题**: Making a font of my handwriting

**原文链接**: [https://chameth.com/making-a-font-of-my-handwriting/](https://chameth.com/making-a-font-of-my-handwriting/)

克里斯·史密斯想用手写字体来个性化他的网站。他最初尝试使用开源工具Inkscape和FontForge创建字体。但他发现FontForge的用户界面令人沮丧，Inkscape的路径操作也过于复杂。

由于对开源选项感到沮丧，他选择了闭源的在线工具Calligraphr。Calligraphr使用用户填写的打印模板，然后进行扫描和处理。作者付费购买了一个月的专业版使用权，利用了他们的一次性付款选项。

他用Sharpie笔填写模板，力求达到剪贴簿的效果。他使用Calligraphr的工具迭代调整字体，包括基线、缩放和字母间距。他还添加了自定义连字。在本地网站副本上测试字体比使用Calligraphr的预览更有效。他认为这个过程很有意义，并且值得投入时间。

最终的字体捕捉到了他的手写风格，并且出乎意料地清晰易读。他对Calligraphr友好的商业实践印象深刻，包括他们透明的定价、取消自动续订以及自动数据导出。文章最后推荐了Calligraphr，并预览了该字体在标题、说明文字和其他位置的使用效果。

---

## 22. 梅谢尔斯：不可能物体的几何处理

**原文标题**: Meschers: Geometry Processing of Impossible Objects

**原文链接**: [https://anadodik.github.io/publication/meschers/](https://anadodik.github.io/publication/meschers/)

本文介绍了一种名为“Meschers”的新型几何表示法，用于处理不可能物体——那些对人类来说似乎合理但物理上不可能的几何结构。与现有涉及在3D空间中切割或弯曲物体的方法（可能破坏几何结构和重新光照）不同，“Meschers”利用了不可能物体局部可积分但全局不可积分的原理。

该表示法由一个网格组成，网格存储顶点的2D屏幕空间位置和边的深度差。关键在于，网格环路周围的深度差之和不必为零，从而在数学上捕捉到“不可能”性。这使得可以将离散几何处理算子（例如拉普拉斯算子）直接应用于不可能物体。

本文重点介绍了“Meschers”的几种应用：平滑、测地距离查询和热扩散，展示了在切割或弯曲表示中不存在的几何属性的保留。值得注意的是，作者演示了如何使用逆向渲染将一个可能的物体（一个圆环）变形为一个不可能的物体（三角形），由目标图像驱动，从而产生一个可测量和可验证的不可能性。“Meschers”的理论基础在于离散外微分。

---

## 23. MentraOS – 开源智能眼镜操作系统

**原文标题**: MentraOS – open-source Smart glasses OS

**原文链接**: [https://github.com/Mentra-Community/MentraOS](https://github.com/Mentra-Community/MentraOS)

MentraOS：面向智能眼镜的开源操作系统，旨在为开发者提供统一平台。它支持包括Even Realities G1、Mentra Mach 1和Mentra Live在内的多种智能眼镜型号，并且兼容型号列表不断增长。Mentra商店提供各种现成可用的应用程序，例如实时字幕、Merge、Notes和翻译。

MentraOS的核心价值在于使开发者能够“一次编写，随处运行”。它处理配对、数据流和交叉兼容性的复杂性，使开发者能够专注于使用TypeScript SDK进行应用程序创建，从而缩短开发时间。开发者可以控制智能眼镜的I/O，包括显示器、麦克风、摄像头和扬声器。MentraOS还通过Mentra商店提供分发渠道，将开发者与智能眼镜用户连接起来。

MentraOS社区鼓励协作和贡献，以构建一个开放、交叉兼容且用户可控的智能眼镜平台。开发者可以通过Discord加入社区，并欢迎通过pull request为项目做出贡献，请遵循提供的贡献者指南。该项目采用MIT许可证授权，并由Mentra Labs提供支持。

---

## 24. 我家自建 DNS 服务器 – 第一部分：IPv4

**原文标题**: My Own DNS Server at Home – Part 1: IPv4

**原文链接**: [https://jan.wildeboer.net/2025/08/My-DNS-Part-1/](https://jan.wildeboer.net/2025/08/My-DNS-Part-1/)

本文是一篇关于在家庭网络中使用树莓派 4 上的 BIND 设置私有 DNS 服务器以实现数字主权的指南。作者 Jan Wildeboer 分享了他配置 BIND 为三个网络提供服务的经验：主家庭网络 (192.168.1.0/24)、第二个以太网网络 (172.16.0.0/16) 和 Podman 容器网络 (10.88.0.0/16)。

该设置包括安装 BIND 和必要的实用程序，为 DNS 流量打开防火墙，以及配置四个关键文件：`/etc/named.conf`（主配置文件）、`/var/named/forward.homelab.jhw`（用于主机名到 IP 地址映射的正向区域文件）、`/var/named/reverse.homelab.jhw`（用于 192.168.1.0/24 的 IP 地址到主机名映射的反向区域文件）和 `/var/named/reverse2.homelab.jhw`（用于 172.16.0.0/16 的 IP 地址到主机名映射的反向区域文件）。作者使用 fritz.box 进行 DHCP 条目，但为实验室网络创建了一个本地域名 homelab.jhw。

本文详细解释了配置文件的每个部分，强调了区域文件中序列号的重要性以及主机名记录中的尾随点。 它还包括 A 记录（将主机名映射到 IP 地址）和 CNAME 记录（创建别名）的示例。 最后，反向区域（PTR 记录）将 IP 地址映射回主机名。 本文强调了每次更改时增加区域文件中序列号的重要性，并提供了用于检查配置和启动 BIND 服务的命令。

---

## 25. 我买了最便宜的电动汽车，一辆二手日产聆风。

**原文标题**: I bought the cheapest EV, a used Nissan Leaf

**原文链接**: [https://www.jeffgeerling.com/blog/2025/i-bought-cheapest-ev-used-nissan-leaf](https://www.jeffgeerling.com/blog/2025/i-bought-cheapest-ev-used-nissan-leaf)

作者于2025年以17,000美元（抵扣旧车和退税后实际为11,000美元）购入一辆2023年二手尼桑聆风SV Plus，并表示价格是主要考虑因素，尽管他们已经研究电动汽车十年。他们之前拥有几辆报废的二手燃油车，现在通勤距离很短。这辆聆风尽管有些年份，但提供了车道保持、自适应巡航控制以及CarPlay/Android Auto等便利功能。

他们详细介绍了为提升电动汽车体验而购买的各种配件，包括二级充电器、便携式充电器、充电适配器（NACS转J1772和CCS1转CHAdeMO）以及行车记录仪。电池健康监测是重点，他们使用LeLink 2 OBD-II适配器和LeafSpy Pro应用程序，作者的电池显示出93.16%的健康状态(SoH)。他们还讨论了延长电池寿命的策略，例如限制快速充电并将充电量保持在50-80%之间。

作者强调了拥有电动汽车的乐趣（单踏板驾驶、扭矩、安静运行、更低的维护成本、便利性）和痛苦（价格、里程焦虑、缺乏充电标准、丑陋的电动汽车设计、电缆杂乱）。关于聆风的具体抱怨包括缺少物理播放/暂停按钮、难以换入空挡以及有限的后备箱开启选项。他们总结说，虽然聆风非常适合他们的需求，但由于成本和基础设施的限制，他们不建议大多数车主购买电动汽车。

---

## 26. 什么是傅里叶变换？

**原文标题**: What Is the Fourier Transform?

**原文链接**: [https://www.quantamagazine.org/what-is-the-fourier-transform-20250903/](https://www.quantamagazine.org/what-is-the-fourier-transform-20250903/)

这篇文章《什么是傅里叶变换？》解释了傅里叶变换及其在各个领域的重要性。傅里叶变换由让-巴蒂斯特·约瑟夫·傅里叶于19世纪初发展而来，它可以将任何函数分解成其组成频率或简谐波。这使得通过将复杂信号分解为更简单的成分来分析它们成为可能。

文章用人耳将声音分离成不同音高的类比，以及数学上分解函数（即使是具有尖锐边缘的函数）的能力来说明了这一点。该变换通过扫描所有可能的频率并确定每个频率对原始函数的贡献程度来实现。

傅里叶变换具有广泛的应用。它被用于信号处理（音频压缩、降噪）、图像压缩（JPEG）、医学成像（MRI）和引力波探测。它也是量子力学中不确定性原理的基础。在数学中，它导致了调和分析领域，并与数论有着意想不到的联系，有助于素数分布的研究。快速傅里叶变换算法极大地加快了它的实际应用，使其在现代技术和科学研究中无处不在。

---

## 27. Protobuf有问题 (2018)

**原文标题**: Protobuffers Are Wrong (2018)

**原文链接**: [https://reasonablypolymorphic.com/blog/protos-are-wrong/](https://reasonablypolymorphic.com/blog/protos-are-wrong/)

本文论证了反对使用 Protocol Buffers (Protobufs) 的理由，声称其设计拙劣、临时拼凑，并且解决的问题只有 Google 真正面临。作者，一位前 Google 员工，批评 Protobufs 的类型系统薄弱且具有限制性，并将其与 Java 有缺陷的类型系统相提并论。

一个主要的批评是 Protobufs 缺乏组合性，并列举了对 `oneof` 和 `map` 字段等功能的众多任意限制，这些限制源于无原则的设计和后期附加的功能。作者提出了一种更简单、更强大的类型系统，该系统基于必需字段（乘积类型）、独立的 `oneof` 类型（共积类型）和类型参数化。

文章还批评了 Protobufs 对标量和消息类型的处理方式，强调了无法区分标量的未设置值和默认值，以及消息类型的怪异访问器行为，打破了预期的编程规则。作者进一步论证说，`oneof` 字段不能作为适当的共积类型发挥作用，导致潜在的错误并阻碍通用、多态代码。

作者驳斥了 Protobufs 被吹捧的向后和向前兼容性，认为这是一种“谎言”，其实现方式是过度放任，默认情况下默默地做错事，并将健全性检查的责任转移到整个代码库。文章认为，虽然 Google 的规模可能证明 Protobufs 的字节节省优化是合理的，但大多数公司规模太小，不足以保证浪费相关的工程师时间。

最后，文章认为 Protobufs 通过迫使开发人员选择维护单独的、不断发展的数据类型，或直接在应用程序中使用线路格式，从而污染了代码库，阻碍了更丰富的数据结构和编程技术的使用。

---

## 28. 我弃用了Docker，转而使用Podman。

**原文标题**: I ditched Docker for Podman

**原文链接**: [https://codesmash.dev/why-i-ditched-docker-for-podman-and-you-should-too](https://codesmash.dev/why-i-ditched-docker-for-podman-and-you-should-too)

无法访问文章链接。

---

## 29. 特斯拉改变“完全自动驾驶”的含义，放弃自动驾驶承诺

**原文标题**: Tesla changes meaning of 'Full Self-Driving', gives up on promise of autonomy

**原文链接**: [https://electrek.co/2025/09/05/tesla-changes-meaning-full-self-driving-give-up-promise-autonomy/](https://electrek.co/2025/09/05/tesla-changes-meaning-full-self-driving-give-up-promise-autonomy/)

文章报道称，特斯拉已实际上放弃了其长期承诺的完全自动驾驶（FSD）能力，重新定义该术语，将其代表一种受监督的高级驾驶辅助系统（ADAS），而非无人监督的自动驾驶。自2016年以来，特斯拉一直在销售“完全自动驾驶能力”，首席执行官埃隆·马斯克多次承诺在每年年底实现完全自动驾驶。然而，较旧的车辆（2016-2023年）缺乏必要的硬件，该公司现在销售“完全自动驾驶（受监督）”，明确声明它不是自动驾驶。

这一定义的改变在新的首席执行官薪酬方案中得到进一步凸显，该方案将马斯克获得股票期权的里程碑与“1000万活跃的FSD订阅”挂钩。该方案中对FSD的定义含糊不清，仅要求一个能够实现“自动或类似功能”的“高级驾驶系统”，而当前受监督的系统可能满足这一要求。Electrek认为，这使得特斯拉有可能降低FSD价格，并推动更多客户购买它，从而使马斯克受益，而无需兑现最初的承诺。

文章还指出，随着销量下降，特斯拉降低了FSD的价格，这与马斯克最初声称价格会随着功能改进而上涨的说法形成鲜明对比。作者认为这可能构成虚假宣传。一位顶级评论员强调了特斯拉在技术上正确但具有误导性的声明的历史。

---

## 30. 清晰度还是准确性——什么造就好的科学图像？

**原文标题**: Clarity or accuracy – what makes a good scientific image?

**原文链接**: [https://www.nature.com/articles/d41586-025-02757-7](https://www.nature.com/articles/d41586-025-02757-7)

本文探讨了科学图像中清晰度和准确性之间复杂的关系，并以阿尼卡·伯吉斯（Anika Burgess）的著作《闪耀的光芒》（Flashes of Brilliance）为切入点。作者是一位科学可视化专家，反思了科学图像的功能，不仅将其视为文档，还将其视为发现和交流的工具。文章重点介绍了早期摄影技术在揭示以前未见过的现实方面的应用，例如雅各布·里斯（Jacob Riis）拍摄的纽约市廉租房生活图像。

然而，本文强调了图像中操纵和误导性表达的可能性。作者讨论了诸如爱德华·布盖（Édouard Buguet）的欺诈性“灵魂”照片和埃德沃德·迈布里奇（Eadweard Muybridge）编辑过的马运动序列等案例，质疑了作为科学真理呈现的图像的完整性。在承认迈布里奇对理解马的运动的贡献的同时，作者强调了在科学背景下图像处理透明度的重要性。

本文将这些历史例子与当代的担忧联系起来，隐含地提及了诸如图像创建中伦理人工智能等问题，并强调了创建视觉上引人注目的图像与保持科学严谨性之间的紧张关系。本文还与苏珊·桑塔格（Susan Sontag）的观点相呼应，即照片“挪用”现实，塑造人们的看法并影响什么被认为是重要的。核心信息是，虽然引人注目的视觉效果很强大，但它们的科学价值取决于诚实的表达和对所做任何修改的清晰沟通。

---

## 31. 机器学习需要一种新的编程语言——克里斯·拉特纳访谈

**原文标题**: ML needs a new programming language – Interview with Chris Lattner

**原文链接**: [https://signalsandthreads.com/why-ml-needs-a-new-programming-language/](https://signalsandthreads.com/why-ml-needs-a-new-programming-language/)

本文是Jane Street的Ron Minsky对LLVM和Swift的创造者Chris Lattner的采访。Lattner在采访中谈论了他进入计算机领域的历程、对编译器的热爱以及他对编译器工程和语言设计交叉领域的独特见解。

Lattner强调，他的职业生涯是由他不断变化的兴趣和解决实际问题的愿望所驱动的。他解释了他从LLVM到C++再到Swift的演变过程，强调了在现有技术基础上进行构建的价值。他创建Swift的动机是，他认为像C++这样的现有语言并不理想，并且他有一些想要探索的好想法。

采访深入探讨了Lattner的语言设计哲学，特别是关于模式匹配等特性。他优先考虑实用性和用户体验，而不是纯粹的理论考虑，同时他也承认强大的数学基础对于泛化和可组合性的重要性。

Lattner将设计过程视为在简洁和连贯性中寻找真理和美的方式，并将其比作物理学中对简单但基本原理的追求。他谈到这种方法如何引导他重新发现已知的数学真理，以及设计如何源于工程学的视角。本文突出了语言设计的迭代性质，以及结合不同视角来创建强大而有用的工具的重要性。

---

## 32. 老旧机器人网站

**原文标题**: The Old Robots Web Site

**原文链接**: [https://www.theoldrobots.com/index2.html](https://www.theoldrobots.com/index2.html)

“老式机器人网站”是一个个人收藏网站，专注于机器人，主要是玩具和教育机器人。该网站于2008年1月14日更新，是与所有者热情相关的资料和资源的存储库。

主要特点包括：

*   **藏品展示：** 该网站展示了所有者的机器人藏品，分为Tomy玩具机器人、其他玩具机器人、教育/个人机器人和受欢迎的Omnibot机器人等类别。这些部分进一步细分为“杂项”页面和编号的“其他机器人”部分（I到VII），表明藏品数量庞大且种类繁多。
*   **导航结构：** 该网站组织了一个清晰的菜单，包括主页、指南、链接、新闻、下载和愿望清单等页面。
*   **教育重点：** 设有一个专门的“教育机器人”部分，表明对教育环境中使用的机器人的历史和发展的兴趣。

---

## 33. 色彩博物馆

**原文标题**: Museum of Color

**原文链接**: [https://emergencemagazine.org/essay/museum-of-color/](https://emergencemagazine.org/essay/museum-of-color/)

这是一个标题和文章信息的识别。没有实际的文章内容可以总结。

根据提供的信息，我们可以推断出以下内容：

*   **标题:** 该文章的标题为“南极洲，女人”。
*   **作者:** 该文章由Stephanie Krzywonos撰写。
*   **日期:** 该文章写于2023年8月31日。
*   **潜在主题:** 鉴于标题，该文章可能探索南极洲，可能将其拟人化或通过女性视角对其进行分析。没有文章本身，任何进一步的总结都是不可能的。

---

## 34. 麻雀：Apache Arrow 列式格式的 C++20 惯用 API

**原文标题**: Sparrow: C++20 Idiomatic APIs for the Apache Arrow Columnar Format

**原文链接**: [https://github.com/man-group/sparrow](https://github.com/man-group/sparrow)

Sparrow 是一个 C++20 库，为使用 Apache Arrow 柱状格式提供符合 C++ 习惯的 API。它简化了 C++ 应用程序中 Arrow 数据结构的创建、操作和交换。

主要特性和优势包括：

*   **符合 C++ 习惯的 API：** Sparrow 提供了用户友好的 C++ 接口来与 Arrow 数据交互，从而抽象化了 C 接口的复杂性。
*   **转换能力：** 方便 Sparrow 数组结构和底层 Arrow C 接口之间的轻松转换，从而实现与其他 Arrow 兼容的库和系统的无缝集成。
*   **内存管理选项：** 支持托管和非托管内存场景，允许用户控制 Arrow C 结构的生命周期。用户既可以允许 Sparrow 管理内存，也可以自行负责释放资源。
*   **安装：** 通过 mamba 包管理器安装或使用 CMake 从源代码构建。
*   **编译器支持：** 需要一个现代 C++ 编译器，具体为 Clang 18+、GCC 11.2+、Apple Clang 16+ 或 MSVC 19.41+。
*   **文档：** 虽然目前正在开发中，但在线提供了文档。

Sparrow 提供了示例，演示了如何初始化数据、提取 Arrow C 结构、将 C 结构传递给 Sparrow 以及转移数据所有权。它采用 Apache License 2.0 许可证。

---

## 35. 对日本Demoscener 0b5vr的采访

**原文标题**: Interview with Japanese Demoscener 0b5vr

**原文链接**: [https://6octaves.com/2025/09/interview-with-demoscener-0b5vr.html](https://6octaves.com/2025/09/interview-with-demoscener-0b5vr.html)

本文采访了日本demoscene制作人0b5vr，他以其64K和4K演示作品而闻名，尤其是“0b5vr GLSL Techno Live Set”(0mix)。0b5vr解释了0mix背后的灵感，它结合了techno演示、现场编码和64K intros，需要大量个人努力来创建演示引擎、现场编码环境、音乐和视觉效果。他讨论了单人项目的挑战和回报，以及0mix虽然参加了64K比赛，但由于合并最终赢得了PC Demo Compo中的“最受欢迎奖”。

0b5vr讨论了在0mix中使用GLSL（通常用于视觉效果）制作音乐，以及屏幕上呈现的代码实际上是音乐代码，观众可能会将其理解为设计。他强调，他很高兴所有技术水平的人都可以按照他们自己的方式来解读他的作品。0b5vr还分享了他对“机器现场”表演（使用groovebox和模块化合成器等硬件）的研究，以及它如何影响了他的GLSL现场编码方法。他回顾了在“draw(tokyo); #2”中使用他的定制Wavenerd系统进行现场编码的经历，该系统利用了预先编写的代码、DJ风格的混音以及由demoscener伙伴ukonpower和Renard生成的视觉效果。他谈到了需要平衡才能吸引具有不同技术知识水平的不同受众。最后，他阐述了他创作4K intros的动机，这些intro通常使用minimalGL等工具快速制作，与要求更高的64K作品形成对比。文章最后探讨了日本demoscene的当前趋势。

---

## 36. Apertus 70B：真正开放 - ETH、EPFL和CSCS的瑞士LLM

**原文标题**: Apertus 70B: Truly Open - Swiss LLM by ETH, EPFL and CSCS

**原文链接**: [https://huggingface.co/swiss-ai/Apertus-70B-2509](https://huggingface.co/swiss-ai/Apertus-70B-2509)

文章《Apertus 70B：真正开放 - 由ETH、EPFL和CSCS开发的瑞士LLM》介绍了Apertus 70B，这是一个由苏黎世联邦理工学院(ETH Zurich)、洛桑联邦理工学院(EPFL)和瑞士国家超级计算中心(CSCS)在瑞士开发的大型语言模型(LLM)。文章强调的关键是其“真正开放”的特性，意味着该模型、其权重，以及可能的训练数据和代码，都可公开访问，用于研究和开发目的。该条目于4天前更新，并已获得193次浏览，表明该项目的最新动态和人们的兴趣。标题表明重点在于模型的开放性及其瑞士血统，暗示着对开源LLM社区的贡献以及瑞士语言AI的潜在进步。

---

## 37. 展示一下：开源我们的文本转CAD应用

**原文标题**: Show HN: Open-sourcing our text-to-CAD app

**原文链接**: [https://github.com/Adam-CAD/CADAM](https://github.com/Adam-CAD/CADAM)

CADAM 是一款开源、基于浏览器的 Web 应用程序，它利用人工智能将自然语言和图像转换为 3D 模型。它具有参数化控制、多种导出格式（.STL、.SCAD），并支持 BOSL、BOSL2 和 MCAD 库。用户可以使用纯英文输入描述或上传图像来指导模型生成，并使用 Three.js 提供实时预览。

该应用的关键功能包括自动参数提取、用于高效尺寸更改的智能更新以及内置的 Geist 字体支持。技术栈包括 React 18 + TypeScript + Vite 用于前端，Three.js + React Three Fiber 用于 3D 渲染，OpenSCAD WebAssembly 作为 CAD 引擎，Supabase 用于后端，Anthropic Claude API 用于 AI，以及 Tailwind CSS + shadcn/ui 用于样式设计。

要开始使用，用户需要 Node.js、npm、Supabase CLI 和 ngrok。设置包括克隆存储库、安装依赖项、启动 Supabase 以及配置前端和 Supabase 函数的环境变量，包括设置 ngrok 隧道以用于 Anthropic 的本地开发。欢迎通过 pull 请求贡献代码。该项目采用 GPLv3 许可。

---

## 38. 自Java 21以来所有新的Java语言特性

**原文标题**: All New Java Language Features Since Java 21

**原文链接**: [https://inside.java/2025/08/31/roadto25-java-language/](https://inside.java/2025/08/31/roadto25-java-language/)

本文由José Paumard于2025年8月31日撰写，宣布Java 25中包含的新语言特性。这些特性主要针对三个目标：增强面向数据编程的能力，降低新开发者的学习曲线，以及提高Java作为自动化脚本语言的适用性。本文旨在介绍这些新特性，并鼓励读者通过“Road to 25”播放列表进一步探索它们。总而言之，Java 25被认为是在使Java成为一种更加通用和易于使用的语言方面迈出的重要一步。

---

## 39. 展示HN：用英语书写阿拉伯语

**原文标题**: Show HN: Writing Arabic in English

**原文链接**: [https://sherifelmetwally.com/writing/writing-arabic-in-english](https://sherifelmetwally.com/writing/writing-arabic-in-english)

这个“Show HN”帖子详细介绍了作者创建一款面向英语使用者的语音阿拉伯语键盘的历程。其核心思想是将英文字母映射到最接近的阿拉伯语发音，让初学者无需学习新的键盘布局就能更轻松地输入阿拉伯语。

作者概述了挑战，包括阿拉伯语的从右到左书写（通过 CSS 轻松解决）、草书特性（很大程度上由浏览器处理）以及英文字母到阿拉伯语音的映射。该项目巧妙地解决了并非所有阿拉伯字母都有直接对应的英文字母的问题。

该解决方案将 11 个独特的阿拉伯字母分为“强调音”和“独特音”两类。“强调音”听起来像是现有声音的更强版本，被映射到大写英文字母。对于没有明显英语对应物的“独特音”，则通过添加撇号 (') 作为“点洒水器”来创建现有字母映射。例如，`s'` 产生 ش (sheen)。

该键盘还使用 `-` 作为特殊字符来处理 Hamza (ء)，并使用读音符号作为发音提示，将其映射到使用 `=` 的组合（例如，`a=` 表示 Fatḥah）。作者提供了使用键盘的示例，包括书写带和不带读音符号的常用单词和短语。

该键盘被构建为一个 Web 组件，易于集成，提供通过 CDN 和 npm 进行安装的选项，并在作者的语言学习平台 Parallel Arabic 中展示。作者承认这种方法的实用性值得商榷，但强调了该项目的乐趣和探索性。

---

## 40. Gym Class VR (YC W22) 正在招聘 – 用户体验设计工程师

**原文标题**: Gym Class VR (YC W22) Is Hiring – UX Design Engineer

**原文链接**: [https://www.ycombinator.com/companies/gym-class-by-irl-studios/jobs/ywXHGBv-ux-design-engineer-senior-staff-principal](https://www.ycombinator.com/companies/gym-class-by-irl-studios/jobs/ywXHGBv-ux-design-engineer-senior-staff-principal)

Gym Class VR 招聘 UX 设计工程师（高级/资深/首席）：领导移动端 Web 应用和 VR 内 Web 界面的开发。

---

## 41. 高速公路护栏成盗贼新宠

**原文标题**: Freeway guardrails are now a favorite target of thieves

**原文链接**: [https://laist.com/news/transportation/guardrails-aluminum-theft](https://laist.com/news/transportation/guardrails-aluminum-theft)

洛杉矶及文图拉县高速公路护栏盗窃案增多：一男子试图盗窃10号公路护栏，加州交通局已花费巨额维修费。

---

## 42. 量子力学简明教程

**原文标题**: Quantum Mechanics, Concise Book

**原文链接**: [https://github.com/basketballguy999/Quantum-Mechanics-Concise-Book](https://github.com/basketballguy999/Quantum-Mechanics-Concise-Book)

篮球小子999的Github仓库“Quantum-Mechanics-Concise-Book”提供了一本关于量子力学(QM)的简明PDF教材。该教材的主要目标是为包括计算机科学、工程、数学和物理专业的本科生，以及对该主题普遍感兴趣的任何人，提供一个适合广泛受众的量子力学入门概述。

本书假定读者具备线性代数、微积分和高中物理的基础知识。这表明其内容结构便于那些具有这些领域基础知识但不必具备物理专业知识的个人理解。

该仓库受到了相当的关注，获得了103个星标，突显了其对于寻求清晰简明量子力学入门介绍的用户的价值。然而，它没有任何fork，表明用户主要直接利用该资源，而不是进行分支和修改。总而言之，该仓库为学习量子力学基础知识提供了一个随时可用的、简洁的入门资源。

---

## 43. 我与评论文化告别。

**原文标题**: I kissed comment culture goodbye

**原文链接**: [https://sustainableviews.substack.com/p/the-day-i-kissed-comment-culture](https://sustainableviews.substack.com/p/the-day-i-kissed-comment-culture)

无法访问文章链接。

---

## 44. 学术档案馆如何成为科技巨头

**原文标题**: An Academic Archive Became a Tech Juggernaut

**原文链接**: [https://www.philanthropy.com/article/how-an-academic-archive-became-a-tech-juggernaut](https://www.philanthropy.com/article/how-an-academic-archive-became-a-tech-juggernaut)

无法访问文章链接。

---

## 45. 视觉查找功能耗电量是多少？

**原文标题**: How much power does Visual Look Up use?

**原文链接**: [https://eclecticlight.co/2025/09/02/how-much-power-does-visual-look-up-use/](https://eclecticlight.co/2025/09/02/how-much-power-does-visual-look-up-use/)

本文 дослі査了在 Apple silicon Mac 上 Visual Look Up (VLU) 的功耗，具體是在運行 macOS 15.6.1 的 M4 Pro Mac mini 上。作者使用 `powermetrics` 以 100 毫秒的間隔測量 CPU、GPU 和神經引擎 (ANE) 的功耗，並在使用 LogUI 提取日誌條目的同時，將這些測量值與對牛的圖像執行 VLU 時的情況相關聯。

分析表明，VLU 的功率需求出人意料地低。 在 6.5 秒的 VLU 活動期間，CPU 消耗了絕大部分功率 (93%)，其次是 GPU (4.6%) 和 ANE (2.2%)。 VLU 的總能量消耗估計為 6.9 焦耳，分解為 CPU (6.4 焦耳)、GPU (0.3 焦耳) 和 ANE (0.2 焦耳)。

日誌分析顯示，ANE 主要在短時間內（1.4-2.2 秒）活躍，使用物件檢測和自然世界識別模型。 CPU 顯示的峰值功耗與最初的 VLU 處理以及稍後打開查找視窗時相符。 GPU 功率峰值與圖像顯示和潛在的處理相對應。

作者得出結論，儘管 ANE 提供了性能優勢，但 VLU 在功耗和能量方面嚴重依賴 CPU，並且對神經引擎和 GPU 的需求相對較小。 總之，VLU 在計算上是密集的，但在 Apple silicon 上並非特別耗電。

---

## 46. Mac克隆史：利润微薄与时运不济的故事

**原文标题**: Mac Clones History: A Tale of Poor Margins and Bad Timing

**原文链接**: [https://tedium.co/2025/09/02/apple-macintosh-clones-history/](https://tedium.co/2025/09/02/apple-macintosh-clones-history/)

这篇 Tedium 文章探讨了 20 世纪 90 年代中期短暂且最终失败的 Mac 授权克隆实验。在它的大部分历史中，苹果公司严格控制着 Mac 市场，但不断变化的市场格局以及像 Stephen Kahng（Power Computing）这样的企业家的影响，促成了一个短暂的授权计划。文章重点介绍了早期不太正式的 Mac 兼容性尝试，例如 Unitron 512 克隆机和 Chuck Colby 的 Mac 改装，说明了对替代 Mac 解决方案的需求。

作者认为，苹果公司 1995 年允许克隆机的决定时机不佳。虽然旨在扩大 Mac 市场并与 Windows 95 的崛起竞争，但克隆计划反而引发了价格战，削弱了苹果公司自身的产品线（当年提供了 47 款型号），并且未能吸引新用户。像 Power Computing 和 UMAX 这样的公司生产了更便宜的 Mac 替代品，直接与苹果公司的产品竞争，蚕食了他们的市场份额。

文章总结说，虽然像 Colby 那样的利基转换是无害的，但授权克隆计划最终损害了苹果公司的品牌和盈利能力。克隆机强调了操作系统而非硬件设计，削弱了苹果公司的“哇”因素，并损害了利润率。在史蒂夫·乔布斯重返苹果公司后，该实验被关闭，这一决定可能对 PowerPC 芯片的开发产生了负面影响。 最终，Mac 克隆实验是一个关于品牌识别、市场细分以及保护利润率的重要性的警示故事。

---

## 47. 我们的嵌入现在有多大？为什么？

**原文标题**: How big are our embeddings now and why?

**原文链接**: [https://vickiboykis.com/2025/09/01/how-big-are-our-embeddings-now-and-why/](https://vickiboykis.com/2025/09/01/how-big-are-our-embeddings-now-and-why/)

机器学习模型中嵌入尺寸的演变：从Word2Vec到ChatGPT

---

## 48. 所需的SQL结构

**原文标题**: SQL needed structure

**原文链接**: [https://www.scattered-thoughts.net/writing/sql-needed-structure/](https://www.scattered-thoughts.net/writing/sql-needed-structure/)

本文探讨了在使用关系数据库中的数据构建用户界面时出现的“对象关系不匹配”问题。核心问题在于，用户界面通常需要层级数据结构，而关系数据库则将数据存储在扁平表格中。将这种扁平数据转换为必要的层级结构既繁琐又容易出错，尤其是在SQL中，因为SQL并非为生成层级数据而设计的。

作者通过一个从PostgreSQL中的IMDb数据集获取电影数据（标题、导演、编剧、演员、角色）的例子来演示了这一点。传统的SQL查询需要多次连接，并且通常返回比所需更多的数据（例如，用于连接的外键）。这些查询在处理可选或多个相关实体时也很吃力，要么导致错误的结果，要么需要多个查询。

通常使用ORM来自动化此过程，但它们可能导致多个查询（数据结构中每个路径一个查询）或因延迟加载而导致一致性问题。

然后，作者介绍了一种使用SQL的JSON聚合功能的解决方案。通过嵌套查询并使用`jsonb_agg`等函数，单个SQL查询可以生成所需的层级JSON结构。虽然生成的查询可能很复杂，但它具有显着的优势：在单个网络往返中获取所有必需的数据，减少后端服务器的负载，并为UI渲染实现更有效的数据检索。作者认为，拥抱这些较新的SQL特性是满足现代Web开发需求的必要演变，其中UI构建是数据库的主要用例。

---

## 49. Show HN: 技术债务缠身

**原文标题**: Show HN: Swimming in Tech Debt

**原文链接**: [https://helpthisbook.com/lou-franco/swimming-in-tech-debt](https://helpthisbook.com/lou-franco/swimming-in-tech-debt)

好的，以下是“Show HN：技术债缠身”帖子的简洁总结，基于标题和提供的内容片段：

该帖子是一个“Show HN”提交，意味着作者正在展示他们创建或正在从事的项目。标题“技术债缠身”直接表明该项目涉及技术债，这是软件开发中常见的问题。

内容“获取你的书...技术债缠身 - 帮助这本书”，强烈表明展示的项目是一本书，或者与一本关于管理或理解技术债的书有关。“帮助这本书”可能意味着作者正在为他们的图书项目寻求反馈、贡献或支持。“获取你的书...”可能是用户将要访问的网页的摘录。

本质上，作者正在分享一本专注于技术债的书（或与书相关的项目），并寻求 Hacker News 社区的意见或帮助。这很可能是一个旨在帮助开发人员和组织更好地理解和解决与积累和管理技术债相关的挑战的项目。

---

## 50. 欧盟委员会因滥用广告技术行为对谷歌处以 29.5 亿欧元罚款

**原文标题**: European Commission fines Google €2.95B over abusive ad tech practices

**原文链接**: [https://ec.europa.eu/commission/presscorner/detail/en/ip_25_1992](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_1992)

欧盟委员会因滥用广告技术市场支配地位对谷歌处以29.5亿欧元罚款。委员会认定，谷歌偏袒其自身广告交易平台AdX及其广告投放工具Google Ad Manager（前身为DoubleClick for Publishers），损害了竞争对手广告交易平台和发布商的利益。

具体而言，谷歌被发现限制竞争对手广告交易平台对其Ad Manager的访问，增加了它们的竞争难度。它还涉嫌利用其在广告投放领域的主导地位在广告竞价过程中偏袒AdX。这种反竞争行为使谷歌得以巩固其对广告技术生态系统的控制，损害了依赖广告收入的发布商和竞争对手的利益。

委员会的调查得出结论，谷歌的行为扼杀了创新，并可能通过导致广告多样性和相关性降低而最终损害了消费者利益。巨额罚款反映了违规行为的严重性，旨在阻止谷歌以及其他具有类似市场力量的公司从事反竞争行为。新闻稿表明，更多关于该决定的细节和影响可从欧盟委员会获取。

---

## 51. 投毒井

**原文标题**: Poisoning Well

**原文链接**: [https://heydonworks.com/article/poisoning-well/](https://heydonworks.com/article/poisoning-well/)

“投毒井”探讨了大型语言模型(LLM)在未经作者同意的情况下，使用网络内容进行训练的问题。由于阻止LLM爬虫很困难，作者探索了一种替代方案：诱使它们消费“受污染”的内容，以降低其输出质量和感知效用。

作者创建了其文章的无意义版本，仅通过 `rel="nofollow"` 链接访问，这些链接本应被Googlebot等信誉良好的爬虫忽略，却被LLM爬虫跟踪。受损内容包含语法扭曲、词汇荒谬和奇怪的拼写错误，这些错误是基于静态词典进行单词替换生成的。

技术实现包括在其基于11ty的站点中创建一个无意义模板，使用transform和JSDOM来操作文本元素，并使用JSON文件中的随机对应词替换单词。他们还为Googlebot等信誉良好的爬虫实施了robot.txt规则。

作者承认这种方法可能不是一个完美的解决方案，但希望如果足够多的作者采用类似的策略，可能会导致生成式AI输出中出现更多的胡言乱语，并可能迫使LLM所有者尊重 `nofollow` 协议。目标是消耗LLM爬虫资源，并且至少是对LLM制造商的行径竖中指。作者欢迎专家就改进方法提出反馈。

---

## 52. 我们所有的人生都在时间网络中交织。

**原文标题**: All of our lives overlap in the Network Of Time

**原文链接**: [https://networkoftime.com/](https://networkoftime.com/)

“时间网络”网站通过真实照片探索人与人之间的关联，展示历史中生命的重叠。用户可以搜索两个人之间的联系，也可以将自己添加到网络中，以发现自己与过去的联系。该网站拥有用户评价，例如杰西·艾森伯格赞扬其概念的评价。

其核心功能围绕着使用照片可视化个人之间的联系，有效地展示看似不同的生活如何交织。用户可以订阅“时间网络”Substack，以获取新的发现并持续探索这些联系。

该网站包括“主页”、“关于”、“提交”、“联系方式”、“新闻”、“注册”和“登录”等标准功能，表明这是一个社区驱动的平台。它还显示加载动画，其中包含“正在加载...”和“正在加载人物详情...”等消息，表明具有交互功能以及人物和照片的动态数据库。

重要的是，该网站包含一项声明，声明其不声明对显示的任何图像的版权或所有权，也不声明获得任何照片中人物或任何图像来源的认可。它鼓励用户联系他们，提出任何问题、更正或请求。该网站还包括特定连接的分享按钮。

---

## 53. 996工作制

**原文标题**: 996 Working Hour System

**原文链接**: [https://en.wikipedia.org/wiki/996_working_hour_system](https://en.wikipedia.org/wiki/996_working_hour_system)

“996工作制”是中国一种非法的工作时间制度，要求员工从早上9点工作到晚上9点，每周工作6天（总计72小时）。这种制度在中国互联网和科技公司中较为常见，被批评为“现代奴隶制”并违反了劳动法。

加班文化长期存在于中国IT企业中，并通过各种方式激励，但与员工的健康问题有关，包括疲劳、肌肉骨骼疼痛和精神健康问题。2013年的一项调查显示，几乎所有中国IT从业者都报告了健康问题。过劳死和自杀也被归因于996制度。

包括58同城、字节跳动（TikTok）、京东、拼多多、有赞、华为和阿里巴巴在内的多家公司都与996制度有关。2019年，一场在线“反996”抗议活动通过GitHub发起，获得了广泛支持，并催生了Anti 996 License。

虽然马云和刘强东等一些人士为该制度辩护，但许多中国媒体和国际人士批评其有害且不人道。最高人民法院于2021年8月裁定996制度违法，但执法问题仍然存在。

---

## 54. 尼泊尔拟封禁脸书、X、YouTube等平台

**原文标题**: Nepal moves to block Facebook, X, YouTube and others

**原文链接**: [https://www.aljazeera.com/news/2025/9/4/nepal-moves-to-block-facebook-x-youtube-and-others](https://www.aljazeera.com/news/2025/9/4/nepal-moves-to-block-facebook-x-youtube-and-others)

尼泊尔政府宣布，由于Facebook、X和YouTube等主要社交媒体平台未能遵守周三的最后期限，向通信和信息技术部注册，将封锁对其的访问。政府声称此举旨在遏制网络仇恨、谣言和网络犯罪，要求公司提供当地联系人、申诉处理人员和负责自我监管的人员。

尽管尼泊尔有数百万用户，但只有少数平台（包括TikTok和Viber）已正式注册。通信部长普里特维·苏巴·古隆表示，这些平台无视了多次要求遵守注册的请求。

尼泊尔数字权利组织主席波拉·纳特·杜哈纳批评这种突然关闭是一种“控制”手段，侵犯了公众权利，并主张在实施此类措施之前建立法律基础设施。尼泊尔此前曾限制过Telegram和TikTok等平台（TikTok在合规后后来被解除禁令）。

文章指出，由于对虚假信息、数据隐私、网络危害和国家安全的担忧，全球范围内出现了一种政府收紧对社交媒体和大型科技公司监管的趋势，并引用了美国、欧盟、巴西、澳大利亚、印度和中国的例子。

---

## 55. 我有两个亚马逊Echo，我从不用它们，但它们显然每天消耗几个GB流量。

**原文标题**: I have two Amazon Echos that I never use, but they apparently burn GBs a day

**原文链接**: [https://twitter.com/davepl1968/status/1963803025572770212](https://twitter.com/davepl1968/status/1963803025572770212)

用户报告称，他们拥有两台很少使用的亚马逊 Echo 设备。尽管不经常使用，这些设备显然每天消耗数 GB 的数据。

提供的内容还显示了网站 X（前身为 Twitter）的典型页脚，包括一条关于 JavaScript 被禁用的消息，以及指向其帮助中心、服务条款、隐私政策、Cookie 政策、版本说明、广告信息和版权声明的链接。出现此页脚的原因可能是原始用户的消息来自 Twitter (X)，而 AI 难以仅提取用户的消息。

---

## 56. Nest 第一代和第二代恒温器将于10月25日起停止支持

**原文标题**: Nest 1st gen and 2nd gen thermostats no longer supported from Oct 25

**原文链接**: [https://community.hubitat.com/t/nest-1st-gen-and-2nd-gen-thermostats-no-longer-supported-by-google-from-10-25-2025/152952](https://community.hubitat.com/t/nest-1st-gen-and-2nd-gen-thermostats-no-longer-supported-by-google-from-10-25-2025/152952)

谷歌发邮件通知西蒙，第一代和第二代Nest恒温器将于10月25日停止支持。恒温器仍可在本地维持温度，但无法再通过Nest或Google Home应用程序控制。西蒙担心这对他的Hubitat集成的影响，质疑更改后是否还能通过Hubitat控制恒温器。关键在于这些旧款Nest恒温器型号将失去远程控制和智能家居集成功能。

---

## 57. 我绝对正确。

**原文标题**: I'm absolutely right

**原文链接**: [https://absolutelyright.lol/](https://absolutelyright.lol/)

标题“我绝对正确”的这篇短文表达了对某事坚信不疑的信念。内容两次重复“绝对正确”来强调这种确定性。它还声称“Claude Code今天说了0次”，暗示断言的主题与Claude Code（可能指语言模型或人工智能）最近没有说过的内容有关。“恰到好处”这个短语增添了一丝微妙的意味，也许意味着这个观点不仅正确，而且是完美地正确。总的来说，这篇文章是对特定信念或观点的自信宣言，可能与特定人工智能模型所说的内容形成对比。

---

## 58. 过去如何充分利用一个简易传真切换盒

**原文标题**: Making the most of a dumb fax switcher box in the old days

**原文链接**: [https://rachelbythebay.com/w/2025/09/01/fax/](https://rachelbythebay.com/w/2025/09/01/fax/)

无法访问该文章链接。

---

## 59. 瑞昱RTL8127万兆以太网PCIe网卡和M.2模块开始出现

**原文标题**: Realtek RTL8127 10GbE PCIe cards and M.2 modules are starting to show up

**原文链接**: [https://www.cnx-software.com/2025/09/05/buy-realtek-rtl8127-10gbe-pcie-cards-and-m2-modules/](https://www.cnx-software.com/2025/09/05/buy-realtek-rtl8127-10gbe-pcie-cards-and-m2-modules/)

本文探讨了基于瑞昱RTL8127的万兆以太网PCIe卡和M.2模块的出现，这是一种低成本的万兆以太网连接替代方案。RTL8127作为经济实惠的解决方案推出，旨在实现30-40美元的价格范围。

文章重点介绍了Auvidea M20E M.2万兆以太网模块，详细介绍了其规格以及Linux/Windows驱动程序支持。然而，其价格（99.99至112.99欧元）高于最初预期。用户测试表明，Auvidea模块实现了高达7,400 Mbps的速度，同时具有低功耗和稳定的性能，优于Marvell AQC107卡。

阿里巴巴和全球速卖通上提供了一种更经济实惠的OEM RTL8127万兆以太网PCIe卡（35-51.62美元）。用户评论表明，与AQC107相比，其具有良好的稳定性和更低的功耗。

文章总结称，基于RTL8127的解决方案的可用性标志着向更实惠的万兆以太网迈出了积极的一步。作者预计未来将看到更多RTL8127产品，包括迷你电脑、单板计算机和主板。

---

## 60. 维提纳里的钟 (2011)

**原文标题**: Vetinari's Clock (2011)

**原文链接**: [https://www.waitingforfriday.com/?p=264](https://www.waitingforfriday.com/?p=264)

本文详细介绍了如何制作一个维提纳里时钟，其灵感来源于碟形世界系列，该时钟以不规则的滴答声制造一种令人迷惑的效果。作者西蒙·英斯使用PIC12F683微控制器取代了标准的石英钟机芯控制器，创建了一个DIY版本。

该时钟通过脉冲驱动标准石英钟机芯中的步进电机来工作，每次脉冲都会反转极性。PIC微控制器以32.768kHz的时钟频率运行，每秒使用四次timer0中断来保持精确计时，同时消耗最小的功率。

固件生成一个32秒的“随机”脉冲序列，使秒针以每秒0-4次的速度移动，在该时间内总共移动32秒。一个额外的延迟可以防止时钟精确地在四分之一秒时前进，进一步增强了不规则的滴答声。

该电路包括限流电阻，以保护PIC和时钟，以及肖特基二极管，以钳位来自线圈的电压尖峰。本文提供了原理图、PCB布局（Eagle CAD格式）以及PIC12F683固件源代码（适用于HiTech C），供读者构建自己的维提纳里时钟。英斯还提到Akafugu.jp提供了一个商业化的套件，供那些喜欢现成选项的人选择。

---

## 61. 光栅化器：一个约4千行代码的GPU加速2D矢量图形引擎

**原文标题**: Rasterizer: A GPU-accelerated 2D vector graphics engine in ~4k LOC

**原文链接**: [https://github.com/mindbrix/Rasterizer](https://github.com/mindbrix/Rasterizer)

光栅化器是一个GPU加速的2D矢量图形引擎，历经10年开发，灵感来源于Adobe Flash。采用C++ 11编写，并使用Metal（适用于macOS，但可通过实例化和浮点渲染目标适应其他GPU），与CPU渲染相比，速度提升高达60倍，非常适合动画UI。计划开发iOS端口。

该引擎专注于将矢量路径高效地转换为高质量、抗锯齿的像素，采用了优化的解决方案，包括一种用于像素面积覆盖的新型窗口逆插值算法。光栅化器支持Postscript风格的路径、奇偶和非零填充规则以及描边。它对填充路径采用两阶段渲染过程：首先渲染到浮点掩码缓冲区，然后渲染到颜色缓冲区。描边路径使用GPU三角剖分直接光栅化到颜色缓冲区。二次贝塞尔曲线在GPU上求解，从而实现粗略的曲线几何。

其架构涉及Path对象、Scene对象（将路径与绘制参数分组）和SceneList对象（将场景与绘制参数分组）。CPU使用批量并行以提高效率，而GPU保持无状态，将帧写入双缓冲共享内存。

演示应用程序使用包含的依赖项构建，允许打开SVG和PDF文件，通过键盘导航，以及使用鼠标/触控板操纵画布。它使用XXHash、NanoSVG、STB Truetype和PDFium库。该库根据个人使用的zlib许可证授权。

---

## 62. 澳大利亚防晒霜丑闻

**原文标题**: A sunscreen scandal shocking Australia

**原文链接**: [https://www.bbc.com/news/articles/c4gzl41rpdqo](https://www.bbc.com/news/articles/c4gzl41rpdqo)

澳大利亚，皮肤癌发病率最高的国家之一，正面临着一场防晒霜丑闻。消费者权益保护组织Choice Australia的一份报告显示，在独立测试中，几款广受欢迎且价格昂贵的防晒霜未能达到其SPF值的宣称。这引发了大规模的反弹，治疗商品管理局（TGA）的调查以及产品召回。

Ultra Violette的Lean Screen SPF 50+被认为是“最严重的失败”，其SPF值仅为4。其他品牌如露得清、香蕉船和癌症委员会也面临审查，尽管他们对调查结果提出异议。Ultra Violette在测试结果不一致后召回了Lean Screen，而其他品牌则暂停了其他产品的销售。

这场丑闻动摇了公众对该行业的信任，并引发了对全球防晒霜监管的质疑。人们对一家位于美国的实验室产生了担忧，该实验室认证了许多不合格的防晒霜，以及不同品牌之间共享基础配方的情况。TGA正在调查并审查SPF测试要求。

专家强调，有效的防晒霜很难制造，而且测试可能具有主观性。尽管存在争议，他们强调持续和充分使用防晒霜的重要性，同时还应采取其他保护措施，如衣物和阴凉处。虽然这场丑闻引起了恐慌，但一些专家认为，大多数防晒霜在降低皮肤癌风险方面的根本有效性仍然有效。这场丑闻提醒人们，只有得到有效执行的法规才能发挥作用。

---

## 63. 菲尔不可思议的垃圾回收器

**原文标题**: Fil's Unbelievable Garbage Collector

**原文链接**: [https://fil-c.org/fugc](https://fil-c.org/fugc)

Fil 的不可思议垃圾回收器 (FUGC) 是一种并行、并发、即时、灰栈、Dijkstra 精确、非移动的垃圾回收器，用于 Fil-C 语言。它拥有以下几个关键特性：

*   **并行和并发：** 利用多个线程进行标记和清理，与程序的线程并发运行。
*   **即时，采用“软握手”：** 避免全局停顿，使用线程上的异步回调（“不规则安全点”）进行栈扫描和其他 GC 任务。
*   **灰栈和 Dijkstra 屏障：** 采用灰栈方法，需要重新扫描线程栈以达到不动点，并结合 Dijkstra 存储屏障，该屏障在标记阶段标记新指向的对象。这消除了对加载屏障的需求。
*   **精确和非移动：** 精确识别指向对象的指针，而不在内存中移动它们，从而简化并发。 回收器作为一个波前推进并实现增量更新。
*   **安全点：** 依靠轮询检查和软握手来实现线程安全并避免竞争条件。
*   **高效清理：** 使用位向量 SIMD 实现非常快速的清理。

FUGC 支持释放对象、终结器、弱引用和弱映射，提供强大的内存安全保证。释放陷阱后续访问和双重释放，而未能释放允许自动回收。 它受到 DLG 回收器的启发，但使用灰栈 Dijkstra 方法和更简单的存储屏障。安全点基础设施还允许调试和安全信号传递。

---

## 64. 在Illumos上调试Rustler

**原文标题**: Debugging Rustler on Illumos

**原文链接**: [https://system-illumination.org/01-rustler.html](https://system-illumination.org/01-rustler.html)

本文详细介绍了作者在Illumos操作系统上调试Rustler（一个用于在Rust中创建Erlang NIFs（本地函数）的工具）的历程。在将项目从Linux迁移到Illumos之后，NIFs加载失败，导致`nif_not_loaded`错误。

作者广泛使用`dtrace`来理解加载过程，追踪诸如`open`之类的系统调用，并检查负责NIF加载的Erlang代码。他们发现Erlang认为库已成功加载，但实际上没有任何NIF被注册。

调查显示，Rustler项目在Illumos上没有正确填充函数数组。深入研究Rustler的内部机制后，作者发现这些函数是通过`inventory` crate添加的，这是一个使用与ELF文件中`.init_array`节相关的编译器内在函数在运行时动态注册插件的系统。

本文解释了`inventory` crate如何使用ELF文件的`.init_array`节在加载时注册NIFs。作者验证了构造函数（`__CTOR`）存在于`.init_array`节中，表明编译器正在正确设置函数。

目前尚未解决的问题已缩小到Illumos运行时链接器（`ld.so.1`）在加载共享库时是否正确调用`.init_array`节中的构造函数。作者计划使用DTrace来验证这些函数在库加载过程中是否被实际调用。

---

## 65. 绝佳的预训练优化器及其发现途径

**原文标题**: Fantastic pretraining optimizers and where to find them

**原文链接**: [https://arxiv.org/abs/2509.02046](https://arxiv.org/abs/2509.02046)

论文：神奇的预训练优化器及其寻觅之处

本文研究了十种深度学习优化器在不同模型规模（0.1B-1.2B参数）和数据模型比率下，对语言模型预训练的性能。作者强调了严格的超参数调整和在训练结束时对不同模型规模和数据比例进行全面评估的必要性，从而解决了优化器之间不公平比较的问题。他们指出，将最佳超参数从一个优化器转移到另一个优化器通常不是最优的，并且中间检查点可能会产生误导。

该研究表明，许多提出的优化器提供的加速效果不如精心调整的AdamW最初声称的那么明显，并且随着模型尺寸的增加，加速效果会减弱。Muon和Soap等速度最快的优化器使用基于矩阵的预条件子（将梯度与矩阵相乘）。然而，来自基于矩阵的优化器的加速与模型规模成反比，与AdamW相比，从0.1B参数模型的1.4倍降至1.2B参数模型的仅1.1倍。论文结论是，彻底的超参数优化和在不同模型规模下的评估对于公平且信息丰富的语言模型预训练优化器比较至关重要。提供了可重复的运行，以供进一步研究。

---

## 66. 解码UTF-8 (三)：确定序列长度——查表法

**原文标题**: Decoding UTF-8. Part III: Determining Sequence Length – A Lookup Table

**原文链接**: [https://nemanjatrifunovic.substack.com/p/decoding-utf-8-part-iii-determining](https://nemanjatrifunovic.substack.com/p/decoding-utf-8-part-iii-determining)

无法访问文章链接。

---

## 67. Apple sued by 2 authors over use of books in AI training [pdf]

**原文标题**: Apple sued by 2 authors over use of books in AI training [pdf]

**原文链接**: [https://storage.courtlistener.com/recap/gov.uscourts.cand.455858/gov.uscourts.cand.455858.1.0_1.pdf](https://storage.courtlistener.com/recap/gov.uscourts.cand.455858/gov.uscourts.cand.455858.1.0_1.pdf)

该文件似乎是一份法律诉状的文本，具体而言是由两位作者提起的针对苹果公司的版权侵权诉讼。核心问题围绕苹果公司涉嫌未经授权使用作者的书籍来训练其人工智能（AI）模型。

该文件结构包括标准的法律诉状要素，例如：

*   **介绍：** 概述诉讼的目的和范围。
*   **管辖权和审判地点：** 确立法院审理此案的法律依据。
*   **诉讼请求：** 明确作者向苹果公司寻求的损害赔偿和补救措施，可能包括对版权侵权的经济赔偿。
*   **要求陪审团审判：** 要求该案件由陪审团而非法官单独裁决。

诉状声称，苹果公司未经许可使用作者的书籍来提高其人工智能系统的功能和能力，从而侵犯了作者的版权。作者正在寻求对此未经授权使用的补救，并认为这损害了他们作为版权持有人的专有权利。

基于PDF结构，这很可能是一份已向法院提交的正式法律文件。该诉讼表明，作者和版权持有人越来越关注他们的作品在人工智能技术开发中的使用，尤其是在未经他们同意或适当补偿的情况下。

---

## 68. Development speed is not a bottleneck

**原文标题**: Development speed is not a bottleneck

**原文链接**: [https://pawelbrodzinski.substack.com/p/development-speed-is-not-a-bottleneck](https://pawelbrodzinski.substack.com/p/development-speed-is-not-a-bottleneck)

Unable to access the article link.


---

## 69. Zuckerberg on hot mic telling Trump he wasn't sure how much to spend on AI

**原文标题**: Zuckerberg on hot mic telling Trump he wasn't sure how much to spend on AI

**原文链接**: [https://www.engadget.com/zuckerberg-caught-on-hot-mic-telling-trump-i-wasnt-sure-how-much-to-promise-to-spend-on-ai-in-the-us-211915608.html](https://www.engadget.com/zuckerberg-caught-on-hot-mic-telling-trump-i-wasnt-sure-how-much-to-promise-to-spend-on-ai-in-the-us-211915608.html)

This article reports on a White House dinner hosted by President Donald Trump for tech CEOs, focusing on the interactions between Trump and Meta CEO Mark Zuckerberg. After Trump jokingly threatened Zuckerberg with jail a year prior, the relationship seems to have improved significantly.

The article highlights a moment where Trump asks Zuckerberg how much Meta plans to spend on AI in the coming years. Zuckerberg estimates "$600 billion through 2028 in the US," seemingly pleasing Trump. However, a later "hot mic" moment reveals Zuckerberg apologizing to Trump for not being ready and "not sure what number you wanted to go with."

The article suggests that Zuckerberg has been actively working to gain Trump's favor through actions such as donating to his inauguration, changing Meta's policies, renouncing DEI, adding a pro-Trump board member, settling a lawsuit, and holding private meetings. The article implies that these efforts have paid off, as Trump now appears to approve of Zuckerberg's AI spending commitment.

Zuckerberg later addressed the "hot mic" incident on Threads, claiming he wasn't sure which spending figure Trump was referring to and shared the lower estimate for the period through 2028, clarifying afterwards that the company might spend even more by the end of the decade.


---

## 70. A computer upgrade shut down BART

**原文标题**: A computer upgrade shut down BART

**原文链接**: [https://www.bart.gov/news/articles/2025/news20250905](https://www.bart.gov/news/articles/2025/news20250905)

BART service has resumed throughout the system after a computer upgrade caused a shutdown. All stations are now open, however, passengers should anticipate residual delays across the entire BART system.


---

## 71. Rearchitecting GitHub Pages (2015)

**原文标题**: Rearchitecting GitHub Pages (2015)

**原文链接**: [https://github.blog/news-insights/rearchitecting-github-pages/](https://github.blog/news-insights/rearchitecting-github-pages/)

生成摘要时出错

---

## 72. Stripe Launches L1 Blockchain: Tempo

**原文标题**: Stripe Launches L1 Blockchain: Tempo

**原文链接**: [https://tempo.xyz](https://tempo.xyz)

生成摘要时出错

---

## 73. What Is the Fourier Transform?

**原文标题**: What Is the Fourier Transform?

**原文链接**: [https://www.quantamagazine.org/what-is-the-fourier-transform-20250903/](https://www.quantamagazine.org/what-is-the-fourier-transform-20250903/)

生成摘要时出错

---

## 74. 30 minutes with a stranger

**原文标题**: 30 minutes with a stranger

**原文链接**: [https://pudding.cool/2025/06/hello-stranger/](https://pudding.cool/2025/06/hello-stranger/)

生成摘要时出错

---

## 75. LLM Visualization

**原文标题**: LLM Visualization

**原文链接**: [https://bbycroft.net/llm](https://bbycroft.net/llm)

生成摘要时出错

---

## 76. Leptos

**原文标题**: Leptos

**原文链接**: [https://leptos.dev/](https://leptos.dev/)

生成摘要时出错

---

## 77. GOP may succeed in unrelenting quest to kill two NASA climate satellites

**原文标题**: GOP may succeed in unrelenting quest to kill two NASA climate satellites

**原文链接**: [https://arstechnica.com/space/2025/09/gop-may-finally-succeed-in-unrelenting-quest-to-kill-two-nasa-climate-satellites/](https://arstechnica.com/space/2025/09/gop-may-finally-succeed-in-unrelenting-quest-to-kill-two-nasa-climate-satellites/)

生成摘要时出错

---

## 78. Age verification doesn’t work

**原文标题**: Age verification doesn’t work

**原文链接**: [https://pornbiz.com/post/17/the_scam_of_age_verification](https://pornbiz.com/post/17/the_scam_of_age_verification)

生成摘要时出错

---

## 79. Jonathan's Space Report

**原文标题**: Jonathan's Space Report

**原文链接**: [https://planet4589.org/index.html](https://planet4589.org/index.html)

生成摘要时出错

---

## 80. Forking Chrome to render in a terminal (2023)

**原文标题**: Forking Chrome to render in a terminal (2023)

**原文链接**: [https://fathy.fr/carbonyl](https://fathy.fr/carbonyl)

生成摘要时出错

---

## 81. Wikipedia survives while the rest of the internet breaks

**原文标题**: Wikipedia survives while the rest of the internet breaks

**原文链接**: [https://www.theverge.com/cs/features/717322/wikipedia-attacks-neutrality-history-jimmy-wales](https://www.theverge.com/cs/features/717322/wikipedia-attacks-neutrality-history-jimmy-wales)

生成摘要时出错

---

## 82. PostgreSQL 18 RC 1 Released

**原文标题**: PostgreSQL 18 RC 1 Released

**原文链接**: [https://www.postgresql.org/about/news/postgresql-18-rc-1-released-3130/](https://www.postgresql.org/about/news/postgresql-18-rc-1-released-3130/)

生成摘要时出错

---

## 83. Musk's $1T pay package is full of watered-down takes on his own broken promises

**原文标题**: Musk's $1T pay package is full of watered-down takes on his own broken promises

**原文链接**: [https://techcrunch.com/2025/09/06/musks-1t-pay-package-is-full-of-watered-down-versions-of-his-own-broken-promises/](https://techcrunch.com/2025/09/06/musks-1t-pay-package-is-full-of-watered-down-versions-of-his-own-broken-promises/)

生成摘要时出错

---

## 84. A PM's Guide to AI Agent Architecture

**原文标题**: A PM's Guide to AI Agent Architecture

**原文链接**: [https://www.productcurious.com/p/a-pms-guide-to-ai-agent-architecture](https://www.productcurious.com/p/a-pms-guide-to-ai-agent-architecture)

生成摘要时出错

---

## 85. Polars Cloud and Distributed Polars now available

**原文标题**: Polars Cloud and Distributed Polars now available

**原文链接**: [https://pola.rs/posts/polars-cloud-launch/](https://pola.rs/posts/polars-cloud-launch/)

生成摘要时出错

---

## 86. Should we revisit Extreme Programming in the age of AI?

**原文标题**: Should we revisit Extreme Programming in the age of AI?

**原文链接**: [https://www.hyperact.co.uk/blog/should-we-revisit-xp-in-the-age-of-ai](https://www.hyperact.co.uk/blog/should-we-revisit-xp-in-the-age-of-ai)

生成摘要时出错

---

## 87. We already live in social credit, we just don't call it that

**原文标题**: We already live in social credit, we just don't call it that

**原文链接**: [https://www.thenexus.media/your-phone-already-has-social-credit-we-just-lie-about-it/](https://www.thenexus.media/your-phone-already-has-social-credit-we-just-lie-about-it/)

生成摘要时出错

---

## 88. Show HN: Inception: Automatic Rust Trait Implementation by Induction

**原文标题**: Show HN: Inception: Automatic Rust Trait Implementation by Induction

**原文链接**: [https://github.com/nicksenger/Inception](https://github.com/nicksenger/Inception)

生成摘要时出错

---

## 89. Supercharger for Business – Tesla

**原文标题**: Supercharger for Business – Tesla

**原文链接**: [https://www.tesla.com/supercharger-for-business](https://www.tesla.com/supercharger-for-business)

生成摘要时出错

---

## 90. Melvyn Bragg steps down from presenting In Our Time

**原文标题**: Melvyn Bragg steps down from presenting In Our Time

**原文链接**: [https://www.bbc.co.uk/mediacentre/2025/melvyn-bragg-decides-to-step-down-from-presenting-in-our-time/](https://www.bbc.co.uk/mediacentre/2025/melvyn-bragg-decides-to-step-down-from-presenting-in-our-time/)

生成摘要时出错

---

## 91. Debian 13.1 Released

**原文标题**: Debian 13.1 Released

**原文链接**: [https://www.debian.org/News/2025/20250906](https://www.debian.org/News/2025/20250906)

生成摘要时出错

---

## 92. Building Supabase-Like OAuth Authentication for MCP Servers

**原文标题**: Building Supabase-Like OAuth Authentication for MCP Servers

**原文链接**: [https://hyprmcp.com/blog/mcp-server-authentication/](https://hyprmcp.com/blog/mcp-server-authentication/)

生成摘要时出错

---

## 93. Atlassian is acquiring The Browser Company

**原文标题**: Atlassian is acquiring The Browser Company

**原文链接**: [https://www.cnbc.com/2025/09/04/atlassian-the-browser-company-deal.html](https://www.cnbc.com/2025/09/04/atlassian-the-browser-company-deal.html)

生成摘要时出错

---

## 94. Action was the best 8-bit programming language

**原文标题**: Action was the best 8-bit programming language

**原文链接**: [https://www.goto10retro.com/p/action-was-the-best-8-bit-programming](https://www.goto10retro.com/p/action-was-the-best-8-bit-programming)

生成摘要时出错

---

## 95. WiFi signals can measure heart rate

**原文标题**: WiFi signals can measure heart rate

**原文链接**: [https://news.ucsc.edu/2025/09/pulse-fi-wifi-heart-rate/](https://news.ucsc.edu/2025/09/pulse-fi-wifi-heart-rate/)

生成摘要时出错

---

## 96. I should have loved electrical engineering

**原文标题**: I should have loved electrical engineering

**原文链接**: [https://blog.tdhttt.com/post/love-ee/](https://blog.tdhttt.com/post/love-ee/)

生成摘要时出错

---

## 97. Étoilé – desktop built on GNUStep

**原文标题**: Étoilé – desktop built on GNUStep

**原文链接**: [http://etoileos.com/](http://etoileos.com/)

生成摘要时出错

---

## 98. io_uring is faster than mmap

**原文标题**: io_uring is faster than mmap

**原文链接**: [https://www.bitflux.ai/blog/memory-is-slow-part2/](https://www.bitflux.ai/blog/memory-is-slow-part2/)

生成摘要时出错

---

## 99. API Blueprint

**原文标题**: API Blueprint

**原文链接**: [https://apiblueprint.org](https://apiblueprint.org)

生成摘要时出错

---

## 100. Le Chat: Custom MCP Connectors, Memories

**原文标题**: Le Chat: Custom MCP Connectors, Memories

**原文链接**: [https://mistral.ai/news/le-chat-mcp-connectors-memories](https://mistral.ai/news/le-chat-mcp-connectors-memories)

生成摘要时出错

---

