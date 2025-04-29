# Hacker News 热门文章摘要 (2025-04-29)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. O3击败一位大师级GeoGuessr玩家——即使使用了伪造的EXIF数据

**原文标题**: O3 Beats a Master-Level GeoGuessr Player–Even with Fake EXIF Data

**原文链接**: [https://sampatt.com/blog/2025-04-28-can-o3-beat-a-geoguessr-master](https://sampatt.com/blog/2025-04-28-can-o3-beat-a-geoguessr-master)

本文探讨了南加州大学研究人员开发的O3物体检测模型，如何在与大师级GeoGuessr玩家的直接对抗中胜出，即使使用的图像带有伪造的EXIF数据。

GeoGuessr是一款流行的在线游戏，玩家需要根据提供的街景图像在世界地图上猜测自己的位置。人类玩家通常依赖环境线索、建筑风格、标牌和其他视觉指标。

O3模型旨在识别图像中的物体和特征，它能够利用其物体识别能力，以惊人的准确性精确定位，超过了人类GeoGuessr专家的表现。文章中强调的关键发现是，尽管有意引入了误导性或伪造的EXIF数据（嵌入在图像中的元数据，通常提供位置信息），O3仍然能够成功。这表明该模型依赖于图像本身固有的视觉线索，而不是仅仅依赖于现成的元数据。

文章表明，O3的成功强调了人工智能模型解决复杂地理问题的潜力，并引发了关于未来位置识别以及误导此类系统所面临的挑战的有趣问题。O3克服故意错误的EXIF数据的能力突出了其在视觉理解和位置识别方面的稳健性和先进能力。

---

## 2. ArkFlow：高性能Rust流处理引擎

**原文标题**: ArkFlow: High-performance Rust stream processing engine

**原文链接**: [https://github.com/arkflow-rs/arkflow](https://github.com/arkflow-rs/arkflow)

ArkFlow：一款高性能的Rust流处理引擎，专为强大的数据流操控而设计。它利用Rust的性能和Tokio的异步运行时来实现低延迟和高吞吐量。

主要特性包括支持多种输入源，如Kafka、MQTT、HTTP、文件（CSV、JSON、Parquet、Avro、Arrow）、生成器以及数据库（MySQL、PostgreSQL、SQLite、DuckDB）。它提供强大的处理能力，如SQL查询、JSON处理、Protobuf编码/解码和批处理。ArkFlow采用模块化架构设计，易于扩展新组件。

配置通过YAML文件管理，定义日志、流（包括输入、管道、输出和错误输出）以及缓冲区设置。处理器可以在管道中链接，并且ArkFlow支持多种输出目标，包括Kafka、MQTT、HTTP、标准输出以及“丢弃”选项。错误处理是可配置的，允许将错误定向到单独的输出。包含缓冲（特别是使用内存缓冲）来处理反压。

文档提供了从Kafka到Kafka处理数据以及生成和处理测试数据的示例。ArkFlow采用Apache 2.0许可。可通过Discord获得社区支持，并鼓励用户在GitHub上为该项目点亮星星。

---

## 3. 为什么性能优化是件苦差事

**原文标题**: Why performance optimization is hard work

**原文链接**: [https://purplesyringa.moe/blog/why-performance-optimization-is-hard-work/](https://purplesyringa.moe/blog/why-performance-optimization-is-hard-work/)

性能优化：苦差事而非能力问题

本文认为，性能优化是件苦差事，并非因为缺乏技能或知识，而是因为它本质上需要通过蛮力实验，并且面临诸多障碍。

作者强调了几个关键挑战：

*   **可组合性：** 优化方法之间的相互作用复杂，有些能协同增效，而另一些则会导致性能下降。确定最佳组合需要大量的测试。
*   **连续性：** 许多算法都有临界点，在不同的实现之间切换会极大地影响性能。为这些切换找到最佳参数值需要不断地重新进行基准测试。
*   **不兼容性：** 优化可能会因为缓存大小限制或 ISA 约束（寄存器压力）等外部约束而失败。作者感叹当前硬件架构的局限性。
*   **编译器：** 编译器常常无法执行对人类来说显而易见的高级优化。它们擅长零成本抽象，但经常错过巧妙的代码转换机会。
*   **文档：** 作者批评了苹果芯片等平台缺乏详细文档，使得优化工作变成了一种逆向工程。

结论强调需要手动探索大量案例，使用不完善的工具进行迭代，并克服不兼容的优化。尽管困难重重，作者认为即使是微小的改进也能产生累积效应，最终节省人们的时间，因此具有价值。

---

## 4. LibreLingo – Duolingo 的 FOSS 替代品

**原文标题**: LibreLingo – FOSS Alternative to Duolingo

**原文链接**: [https://librelingo.app](https://librelingo.app)

LibreLingo：一个社群驱动的开源语言学习平台，旨在成为Duolingo的免费替代品。它目前正在开发中，并提供多种语言的课程，包括西班牙语、德语、法语、孟加拉语、中古波斯语、巴斯克语和拉迪诺语（面向英语、希伯来语和西班牙语使用者）。它还提供侯马语课程（面向英语使用者）。

该项目由Dániel Kántor领导，并由其他人贡献，强调社群参与平台的建设和维护。开发文档目前仅提供英文版本。源代码以AGPL-3.0协议授权，以促进项目的开放和协作性质。

---

## 5. 编程语言应该提供树遍历原生支持。

**原文标题**: Programming languages should have a tree traversal primitive

**原文链接**: [https://blog.tylerglaiel.com/p/programming-languages-should-have](https://blog.tylerglaiel.com/p/programming-languages-should-have)

泰勒·格莱尔认为，编程语言缺少一个关键的控制流结构：一种树遍历原语，类似于线性结构的`for`或`foreach`循环。他提出了一个`for_tree`结构来简化和减少常见树遍历操作中的错误。

所提出的`for_tree`结构模仿了常规的`for`循环，包含`init`、`condition`和`branch`组件。`branch`组件是关键的区别，它定义了如何生成子节点以进行遍历。他认为这比为每个树操作编写递归函数更容易且不易出错，同时可能编译成类似的代码。

他还建议在简单的递归之外添加一些特性，例如`break`、`continue`和`prune`关键字在`for_tree`主体中使用。`prune`将停止遍历节点的子节点。他将`for_tree`与基于范围的`for`循环进行对比，强调了它在没有迭代器的情况下操作命令式树的能力，以及它在遍历现有数据结构之外的问题（如生成字符串）中的适用性。

他承认了广度优先搜索（BFS）的复杂性挑战，并将提案重点放在深度优先搜索（DFS）上以简化问题。

最后，他提供了一个使用模板和宏的C++概念验证实现，展示了其可行性，尽管与原生语言级实现相比，语法更丑陋且存在局限性。他希望能够启发语言设计者考虑添加这样的功能。

---

## 6. Show HN: 一款自动拒绝非必要 Cookie 的 Chrome 扩展

**原文标题**: Show HN: A Chrome extension that will auto-reject non-essential cookies

**原文链接**: [https://blog.bymitch.com/posts/reject-cookies/](https://blog.bymitch.com/posts/reject-cookies/)

这个“Show HN”帖子介绍了一款名为“Reject Cookies”的Chrome扩展程序，该程序旨在自动拒绝非必要的cookie同意横幅。作者强调了人们对这些横幅的普遍不满，并将该扩展程序定位为一种主动拒绝cookie的解决方案，而不是被动接受或清理它们。

该扩展程序的工作原理是首先尝试查找并点击常见cookie同意提供商（如OneTrust）的拒绝按钮。如果失败，则会回退到关闭同意弹出窗口或横幅。作者强调，根据GDPR和ePrivacy指令，省略接受应被解释为拒绝。

该扩展程序的开发涉及使用Cursor AI进行样板设置，尽管AI在针对特定cookie供应商实现的更细致的实现方面证明帮助不大。该扩展程序的逻辑涉及检查特定元素以识别提供商，然后采取相应的行动，要么单击拒绝按钮，要么删除同意横幅。

“Reject Cookies”是开源的，目前仍在开发中。作者鼓励用户通过报告扩展程序失败的网站、报告错误或通过扩展程序内的侧边栏或通过电子邮件提供一般反馈来做出贡献。目标是扩大扩展程序的覆盖范围，以包括更多的cookie同意供应商及其实现的变体。

---

## 7. Hestus公司（YC S24）正在招聘机器学习工程师，以彻底变革CAD

**原文标题**: Hestus, Inc. (YC S24) Is Hiring an ML Engineer to Revolutionize CAD

**原文链接**: [https://www.ycombinator.com/companies/hestus-inc/jobs/WQVdwX8-machine-learning-engineer](https://www.ycombinator.com/companies/hestus-inc/jobs/WQVdwX8-machine-learning-engineer)

Hestus公司（Y Combinator S24期孵化企业，致力于开发AI驱动的CAD软件）正在加州圣马特奥招聘机器学习工程师。此全职岗位提供11万至17.5万美元的年薪，并有机会与创始人Sohrab Haghighat和Kevin Chu直接合作。

Hestus旨在利用人工智能革新硬件开发。理想的候选人应具备6年以上经验（或4年以上经验加硕士/博士论文），精通Python，拥有创建和调整定制机器学习模型和嵌入的经验，并熟悉PyTorch等深度学习框架。他们应适应快节奏的创业环境，具备出色的问题解决和沟通能力，并持有计算机科学、工程或相关领域的学士学位。

职责包括设计、开发和维护可扩展的软件应用程序，实施机器学习模型，与跨职能团队协作，参与代码审查，开发后端组件，解决问题，并及时了解行业趋势。

加分项包括机器学习平台（如AWS SageMaker）、云平台（AWS、Google Cloud）、后端框架（Django、Flask、SQL）以及开发超越LLM或图像处理的新型嵌入的经验。

Hestus提供有竞争力的薪资、股权期权、全面的健康保险、免费午餐、无限休假、协作的工作环境以及职业发展机会。

---

## 8. Firefox标签页分组功能上线了

**原文标题**: Firefox tab groups are here

**原文链接**: [https://blog.mozilla.org/en/firefox/tab-groups-community/](https://blog.mozilla.org/en/firefox/tab-groups-community/)

火狐正式推出标签页分组功能，这一备受期待的功能是由Mozilla Connect上的社区反馈推动开发的。该功能允许用户将标签页组织成命名或彩色分组，以便更好地集中注意力和整理杂乱，无论管理少量还是数千个标签页。

开发过程深受用户见解的影响。产品经理积极采纳社区的建议，识别潜在需求，并优先开发能使大多数用户受益的功能。 Beta测试人员也发挥了至关重要的作用，他们发现了早期版本并提供了宝贵的反馈，从而塑造了最终产品。

团队目前正在探索“智能标签页分组”，这是一项人工智能驱动的功能，可根据标签页的内容建议名称和分组，从而提供更强大的组织能力。重要的是，此功能在本地处理数据，从而确保用户隐私。

文章强调，标签页分组不仅是为了整理杂乱，更是为了提高注意力和工作效率。文章强调了与社区的持续对话，并鼓励在Mozilla Connect上继续提供反馈，以进一步改进浏览器。标签页分组的推出被视为Mozilla致力于基于真实用户需求构建功能的证明，并展示了社区协作的力量。

---

## 9. Show HN: Flowcode – 图灵完备的可视化编程平台

**原文标题**: Show HN: Flowcode – Turing-complete visual programming platform

**原文链接**: [https://app.getflowcode.io/playground/example1](https://app.getflowcode.io/playground/example1)

无法访问文章链接。

---

## 10. 通义千问3：思深行敏

**原文标题**: Qwen3: Think deeper, act faster

**原文链接**: [https://qwenlm.github.io/blog/qwen3/](https://qwenlm.github.io/blog/qwen3/)

Qwen3发布：代码、数学及通用能力表现卓越，具备混合思维模式，支持119种语言和方言。

---

## 11. 一行代码价值八千美元

**原文标题**: A single line of code cost $8000

**原文链接**: [https://pietrasiak.com/one-line-of-code-that-did-cost-dollar8000](https://pietrasiak.com/one-line-of-code-that-did-cost-dollar8000)

屏幕录制应用Screen Studio因自动更新程序中的单行代码错误导致8000美元账单。代码重构无意中删除了阻止应用程序重复下载250MB更新文件的代码。结果，在后台运行该应用程序的用户不知不觉地每5分钟下载一次更新。

这种持续下载持续了一个多月，导致900万次文件下载和超过2PB的Google Cloud流量。问题源于应用程序每5分钟检查一次更新，并在下载更新文件后未能停止此过程。

作者强调了一系列失误，包括Google Cloud上缺少成本警报和监控频率不足。该事件对用户产生了负面影响，其中一位用户的互联网合同因产生大量流量而被取消。该公司表示愿意承担与不便相关的任何费用。

作者强调了在云服务上设置成本警报、编写自动更新代码（或任何产生费用的代码）时要谨慎、为强制更新实施服务器端信号以及定期监控云使用情况的重要性。该事件是关于在云环境中谨慎编码实践和主动监控的重要性的惨痛教训。

---

## 12. 为什么Windows 7如果使用纯色背景，登录速度会变慢好几个月？

**原文标题**: Why did Windows 7 log on slower for months if you had a solid color background?

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20250428-00/?p=111121](https://devblogs.microsoft.com/oldnewthing/20250428-00/?p=111121)

本文解释了为何Windows 7在2009年7月发布后的最初几个月内，对于使用纯色背景的用户，登录速度较慢（“欢迎”界面显示长达30秒）。该问题源于登录系统等待包括壁纸系统在内的各种桌面组件发出准备就绪信号的方式。

具体来说，负责报告壁纸就绪状态的代码仅在定义了壁纸位图时才执行。因此，使用纯色背景（无位图）的用户不会触发就绪信号，导致系统等待完整的30秒超时。

当启用“隐藏桌面图标”组策略时，也发生了类似的问题。由于围绕负责初始化桌面图标和报告就绪状态的代码放置了一个位置不当的“if”语句，这意味着在隐藏图标时，永远不会发送就绪信号，再次触发30秒延迟。

本文强调，实际的登录过程并未延长30秒，而是由于缺少就绪报告，“欢迎”屏幕保持可见状态达该时间。根本问题在于设计缺陷，即报告机制与特定桌面元素的存在与否相关联。

该问题已于2009年11月得到解决和修复，即Windows 7首次发布后的几个月。

---

## 13. 高斯溅射遇上ROS2

**原文标题**: Gaussian Splatting Meets ROS2

**原文链接**: [https://github.com/shadygm/ROSplat](https://github.com/shadygm/ROSplat)

ROSplat：一种基于 ROS2 的新型在线可视化工具，它利用高斯溅射技术实时渲染复杂的 3D 场景。它通过使用自定义 ROS2 消息（`SingleGaussian` 和 `GaussianArray`）传输高斯属性（如位置、旋转、缩放、不透明度和球谐函数），高效地可视化数百万个高斯分布。

该系统基于 ROS2 构建，支持高斯、图像和 IMU 数据的在线数据交换。它利用 GPU 加速的排序和渲染来实现实时性能。 ROSplat 支持从 PLY 文件加载数据，并与 ROS2 工具（如 bag 记录）集成。

设置需要 ROS2 Jazzy，以及可选的 `cupy` 和 `torch` 用于基于 GPU 的排序（CPU 备用）。安装说明通过 `pip` 或 Docker 提供。`run_docker.sh` 脚本简化了 Docker 设置，确保主机和容器之间的 CUDA 版本兼容性。

使用 `colcon build --packages-select gaussian_interface` 构建自定义高斯消息并配置工作空间是关键步骤。可视化工具通过 `python3 main.py` 启动。 欢迎贡献和反馈。 该项目感谢 Qihao Yuan 和 Kailai Li 的支持，以及 limacv 的 `GaussianSplattingViewer` 仓库的影响。

---

## 14. 试试切换到 Kagi

**原文标题**: Try Switching to Kagi

**原文链接**: [https://daringfireball.net/2025/04/try_switching_to_kagi](https://daringfireball.net/2025/04/try_switching_to_kagi)

本文强烈推荐从谷歌切换到Kagi进行网页搜索，主要原因是Kagi能提供更优质的搜索结果。作者列举了一些案例，表明谷歌优先展示赞助链接和人工智能摘要，导致结果不准确或代价高昂（例如，价格过高的旅行授权和酒店预订）。他强调，Kagi始终能提供更直接和相关的答案，甚至能找到谷歌和DuckDuckGo未能找到的较旧文章。

虽然作者承认Kagi在隐私和无广告方面的优势，但他强调切换的主要原因是搜索结果的准确性和相关性得到了提高。他用过去付费观看HBO的例子作类比，认为为Kagi付费是合理的，因为它质量更高，没有广告、人工智能概述（除非特别要求）以及赞助链接，这些链接往往使谷歌上的自然搜索结果黯然失色。

作者指出，DuckDuckGo曾经是一个可行的替代方案，但现在变得不太可靠，通常需要重定向到谷歌。相比之下，他很少发现在使用Kagi时需要回到谷歌。他认为Kagi可以完全取代谷歌，提供明显更好的搜索体验，尽管谷歌一直在努力清除真正的欺诈网站。文章最后强烈推荐Kagi，鼓励读者尝试一下。

---

## 15. 如何培养内在动机：一项科学综述

**原文标题**: How to build Intrinsic Motivation: a review of the science

**原文链接**: [https://erringtowardsanswers.substack.com/p/intrinsic-motivation](https://erringtowardsanswers.substack.com/p/intrinsic-motivation)

无法访问文章链接。

---

## 16. 经济学家称，生成式人工智能根本不会取代工作岗位或损害工资。

**原文标题**: Generative AI is not replacing jobs or hurting wages at all, say economists

**原文链接**: [https://www.theregister.com/2025/04/29/generative_ai_no_effect_jobs_wages/](https://www.theregister.com/2025/04/29/generative_ai_no_effect_jobs_wages/)

本文报道了丹麦经济学家Anders Humlum和Emilie Vestergaard的一项研究，该研究考察了ChatGPT等生成式AI聊天机器人对就业和工资的实际劳动力市场影响。与对普遍失业或工资下降的担忧相反，该研究发现，在被认为容易受到AI影响的11个职业中，包括会计师、记者和软件开发人员等，其经济影响微乎其微。

尽管工人迅速采用AI聊天机器人，且受到雇主的鼓励，但该研究发现，对收入或记录的工作时间没有显著影响。虽然投资AI的公司增加了对这些工具的采用，并节省了一些时间（平均占工作时间的2.8%），但工作质量和满意度显示出不同的结果。AI正在创造新的任务，例如检测学校中AI生成的作弊行为，这抵消了一些时间节省。

经济学家认为，由于AI对大多数任务的适用性有限，以及雇主对这些新工具的持续调整，AI带来的生产力提升可能无法完全实现。此外，只有一小部分生产力提升以更高的工资形式传递给工人。Humlum强调，虽然内部教育可以改善AI的使用，但关于收入和工资的硬性数据显示，这些工具尚未产生显著的经济影响，这表明它们在短期内具有一定的变革潜力上限。

---

## 17. 印度法院命令封锁Proton Mail

**原文标题**: Indian court orders blocking of Proton Mail

**原文链接**: [https://techcrunch.com/2025/04/29/indian-court-orders-blocking-of-proton-mail/](https://techcrunch.com/2025/04/29/indian-court-orders-blocking-of-proton-mail/)

印度一家法院已下令封锁加密电子邮件服务Proton Mail，此前一家位于新德里的公司M Moser Design Associates提出申诉。该公司声称其员工通过Proton Mail收到淫秽和粗俗的电子邮件，且该服务拒绝披露发件人的详细信息。卡纳塔克邦高等法院的M Nagaprasanna法官已指示政府根据2008年《信息技术法》封锁Proton Mail。

这并非Proton Mail首次在印度面临法律挑战。去年，泰米尔纳德邦当局在Proton Mail被用于发送虚假炸弹威胁后，试图封锁该服务。虽然当时瑞士当局进行了干预，阻止了封锁，但德里高等法院也在2024年10月要求调查Proton Mail在印度的使用情况。

Proton Mail辩称，封锁该服务限制了守法公民的安全通信，但不会阻碍可以使用其他电子邮件服务的网络犯罪分子，尤其是那些位于印度境外的犯罪分子。截至目前，卡纳塔克邦高等法院下令的封锁尚未实施。

---

## 18. Meta AI 应用，基于Llama 4 构建

**原文标题**: Meta AI App built with Llama 4

**原文链接**: [https://about.fb.com/news/2025/04/introducing-meta-ai-app-new-way-access-ai-assistant/](https://about.fb.com/news/2025/04/introducing-meta-ai-app-new-way-access-ai-assistant/)

Meta推出了一个基于Llama 4构建的全新独立Meta AI应用，旨在提供更具个性化和对话性的AI体验。首个版本允许用户通过语音和文本与Meta AI互动，集成了图像生成和编辑等功能。一个采用全双工语音技术的语音演示展示了未来自然语音交互的雏形，尽管它仍处于实验阶段。

通过学习用户偏好并利用其Meta个人资料（Facebook和Instagram）的信息（如果已关联），Meta AI能够实现个性化，从而提供更相关的回复。这种个性化体验目前在美国和加拿大可用。

该应用包含一个“发现动态”功能，供用户分享和探索AI提示词，从而促进社区驱动的体验。Meta AI旨在跨Meta生态系统访问，包括Facebook、WhatsApp、Messenger、雷朋Meta眼镜以及现在的网页。Meta AI应用正与雷朋Meta眼镜的Meta View配套应用合并，以整合跨设备的AI体验。

Meta AI的网页版已经针对更大的屏幕进行了优化，并包括图像生成的改进，以及对具有PDF导出和文档分析功能的文档编辑器的测试。用户可以控制其AI体验，并可以选择管理语音设置。此版本在美国、加拿大、澳大利亚和新西兰可用。Meta正在收集反馈以改进该应用。

---

## 19. 单人框架实战

**原文标题**: The One-Person Framework in Practice

**原文链接**: [https://link.mail.beehiiv.com/ss/c/u001.5SRwDQ9qxPQW8vmD5Do73b3R4eTCi2vXqPyztEk6wMFC9_fqEAcDVx6xEJ96T4BSMXrPS7z5exEBSTF4pF48z8SqJkJnkAwMUW9LtYdd8lWmvkDinT92nsk5HmXOHdWgLsysm9FMGrqmu7dnG57cXpga8ZOe8X0IV8pyeC3AswdRMaitfT307y7naP-_6W5CiolKhXCKrEndMGCW2PftFUu9ieYOxpVJ_fhu82gAh-4/4g1/wA_MG-I5SVCyR3KY66oEaQ/h30/h001.kLDFZMgisudi21zmTPbd_O8U7X98d4UxYqZjQTb_D7o](https://link.mail.beehiiv.com/ss/c/u001.5SRwDQ9qxPQW8vmD5Do73b3R4eTCi2vXqPyztEk6wMFC9_fqEAcDVx6xEJ96T4BSMXrPS7z5exEBSTF4pF48z8SqJkJnkAwMUW9LtYdd8lWmvkDinT92nsk5HmXOHdWgLsysm9FMGrqmu7dnG57cXpga8ZOe8X0IV8pyeC3AswdRMaitfT307y7naP-_6W5CiolKhXCKrEndMGCW2PftFUu9ieYOxpVJ_fhu82gAh-4/4g1/wA_MG-I5SVCyR3KY66oEaQ/h30/h001.kLDFZMgisudi21zmTPbd_O8U7X98d4UxYqZjQTb_D7o)

无法访问文章链接。

---

## 20. 地球六分之一的农田含有一种或多种金属的毒性水平。

**原文标题**: One-sixth of the planet's cropland has toxic levels of one or more metals

**原文链接**: [https://english.elpais.com/science-tech/2025-04-17/one-sixth-of-the-planets-cropland-has-toxic-levels-of-one-or-more-metals.html](https://english.elpais.com/science-tech/2025-04-17/one-sixth-of-the-planets-cropland-has-toxic-levels-of-one-or-more-metals.html)

《科学》杂志近期发表的一项研究显示，全球有相当一部分耕地，估计为14-17%（高达2.42亿公顷），含有有毒水平的重金属。这种污染影响了约9亿至14亿人，约占全球人口的11-18%。

研究人员分析了近80万个地点的数据，重点关注土壤最上面的30厘米，这是植物生长的最重要层。他们利用机器学习，模拟了来自七种特定金属和类金属（砷、镉、铬、钴、铜、镍和铅）的全球污染程度。

该研究区分了由采矿和工业事故等人为活动造成的污染，以及由自然过程造成的高浓度。虽然母岩的自然风化有所贡献，但化肥使用、废水灌溉和工业排放等人为活动加剧了这个问题。

地图突出显示了一条“富金属走廊”，从意大利北部延伸到中国东南部，将当前的污染与古代的采矿和冶炼活动联系起来。镉是分布最广的污染物。

该研究并未追究责任，但强调了人类对地球产生的持久影响。专家强调，建立明确的土壤有害金属浓度阈值非常重要，以保护环境和人类健康，并承认长期暴露，即使在低水平下，也会产生累积效应。

---

## 21. 全球心脏病死亡与塑料中广泛使用的化学物质有关

**原文标题**: Heart disease deaths worldwide linked to chemical widely used in plastics

**原文链接**: [https://medicalxpress.com/news/2025-04-heart-disease-deaths-worldwide-linked.html](https://medicalxpress.com/news/2025-04-heart-disease-deaths-worldwide-linked.html)

这篇2025年4月的文章重点介绍了一项研究，该研究将邻苯二甲酸酯DEHP（一种用于使塑料更柔韧的化学物质）的暴露与2018年全球55-64岁人群中超过36.5万例心脏病死亡病例联系起来。纽约大学朗格尼健康中心的研究人员估计，DEHP导致了该年龄组全球心脏病死亡人数的10%以上，估计造成的损失为5100亿美元至3.74万亿美元。

这项发表在《eBioMedicine》上的研究分析了来自200个国家/地区的健康和环境数据，包括尿液样本以估计DEHP暴露情况，以及来自健康指标与评估研究所的死亡率数据。结果表明，非洲、中东和东亚承担了这些死亡人数中不成比例的负担，其中印度死亡人数最多。研究人员认为，这种差异可能是由于塑料生产快速发展且限制较少导致更高的暴露率。

主要作者Sara Hyman强调了邻苯二甲酸酯对人类健康的危害，而资深作者Leonardo Trasande呼吁制定全球法规以减少暴露，尤其是在快速工业化的地区。虽然该研究并未建立直接的因果关系，但它建立在先前将邻苯二甲酸酯与健康问题联系起来的研究基础上，并且是首次对DEHP暴露导致的心血管死亡率进行的全球估计。未来的研究将跟踪减少邻苯二甲酸酯暴露对死亡率的影响，并将研究扩展到其他健康问题，如早产。

---

## 22. 服役53年后，苏联失败的金星探测器正坠向地球

**原文标题**: After 53 years, a failed Soviet Venus spacecraft is crashing back to Earth

**原文链接**: [https://gizmodo.com/after-53-years-a-failed-soviet-venus-spacecraft-is-crashing-back-to-earth-2000595234](https://gizmodo.com/after-53-years-a-failed-soviet-venus-spacecraft-is-crashing-back-to-earth-2000595234)

苏联的金星探测器“宇宙482号”于1972年发射，由于发动机故障未能到达金星，预计将于2025年5月10日左右不受控制地重返地球大气层。卫星追踪者马可·朗布鲁克估计，该着陆舱模块设计用于承受金星大气层，可能在重返大气层后幸存并完好地撞击地球。

该任务在发射后解体，一些碎片在不久后重返大气层。剩余的有效载荷和发动机装置目前位于较高的地球轨道上。该航天器超过1000磅的质量构成了类似于陨石撞击的风险。

由于太阳活动增加，地球大气层正在扩张，并增加了对轨道物体的阻力，因此很难确定确切的重返日期。确定着陆地点也具有挑战性，但碎片落在人口稠密地区的可能性很低。尽管概率较低，不受控制的重返始终构成不应被忽视的风险。

---

## 23. Pyrefly - 用 Rust 编写的更快的 Python 类型检查器

**原文标题**: Pyrefly - A faster Python type checker written in Rust

**原文链接**: [https://pyrefly.org/](https://pyrefly.org/)

本文介绍 Pyrefly，一个用 Rust 编写的 Python 新型静态类型检查器，旨在提高速度和性能，优于 MyPy 等现有工具。要点是 Pyrefly 利用 Rust 的高效内存管理和并发能力来实现明显更快的类型检查。

本文可能重点介绍 Pyrefly 的性能优势，并可能展示基准测试，证明其速度优势。它可能讨论了使用 Rust 构建 Pyrefly 的设计选择，重点关注错误处理、并行处理以及针对性能优化的数据结构等方面。它也可能涉及该工具与现有 Python 类型提示的兼容性及其集成到现有开发工作流程中的能力。

此外，本文可能将 Pyrefly 定位为 Python 开发人员加速类型检查过程并改善整体开发体验的有前途的替代方案，强调其尽早且更有效地捕获类型错误的潜力。 虽然可能不是一个全面的功能列表，但它可能提到核心功能和潜在的未来开发计划。 本质上，本文是对 Pyrefly 的介绍和价值主张。

---

## 24. 什么是“诱导大气振动”？

**原文标题**: What Is "Induced Atmospheric Vibration"?

**原文链接**: [https://physics.stackexchange.com/questions/848666/what-is-induced-atmospheric-vibration](https://physics.stackexchange.com/questions/848666/what-is-induced-atmospheric-vibration)

本文探讨了据称是伊比利亚半岛最近一次停电背后原因的“感应大气振动”现象。最初的报告将停电归因于西班牙极端温度变化导致的高压线路振荡，进而导致欧洲电网的同步故障。

讨论表明，对于“感应大气振动”缺乏具体的科学解释。猜测范围从天气相关的负载变化导致本地发电机频率降低，到温度变化影响高压线路阻抗，可能导致驻波和电压尖峰。受温度和湿度影响的电晕放电也被认为是电抗问题的潜在来源，从而扰乱电网同步。

一些回应表明，该术语可能是一种误解，或是一种试图掩盖更复杂问题的尝试，可能与电网设计缺陷或自动发电控制系统的协调不当有关。越来越多地依赖基于逆变器的电源而不是具有惯性的传统发电机也被认为是加剧电网不稳定性的一个因素。虽然提到了风引起的电缆振荡，但它们与电力频率波动的直接联系受到质疑。

---

## 25. 日本推出首款太阳能超级面板

**原文标题**: Japan unveils first solar super-panel

**原文链接**: [https://www.japanenergyevent.com/media-insights-hub/industry-news/japan-unveils-world-s-first-solar-super-panel-more-powerful-than-20-nuclear-reactors/](https://www.japanenergyevent.com/media-insights-hub/industry-news/japan-unveils-world-s-first-solar-super-panel-more-powerful-than-20-nuclear-reactors/)

日本正率先使用钙钛矿太阳能电池（PSCs）来彻底变革其可再生能源领域，并力争在2050年实现净零排放。日本政府优先发展PSC，目标是到2040年实现20吉瓦的发电量，相当于20座核反应堆。该战略利用了日本作为第二大碘生产国的地位，碘是PSC制造的关键成分，从而能够建立独立的供应链并加强经济安全。

与传统的硅基面板相比，PSCs具有重量轻、柔韧性好以及适应城市环境的优势。它们可以集成到建筑物墙壁、窗户、汽车顶棚和路灯中，从而在空间有限的密集人口区域最大限度地利用能源。这也使得混合风能和太阳能系统成为可能。

虽然日本曾经在太阳能电池板制造方面处于领先地位，但由于来自中国的竞争而落后。PSC技术使日本能够重新在太阳能市场中占据更有利的地位。积水化学工业株式会社在政府的支持下，正在开发先进的PSC模块，以便在2030年代更广泛地应用于市场。

目前，PSCs面临着挑战，包括耐用性和高昂的前期成本。然而，该技术正在不断改进，预计到2040年成本将降至每瓦10日元。目前，太阳能占日本总能源产量的近10%，高于2014年的1.9%，该国目标是在2030年将可再生能源占比提高到36%-38%。日本对PSCs的承诺使其成为可再生能源领域的全球领导者，为其他国家提供可持续的能源解决方案和典范。

---

## 26. 一百万个棋盘

**原文标题**: One Million Chessboards

**原文链接**: [https://onemillionchessboards.com/#199,276](https://onemillionchessboards.com/#199,276)

百万棋盘

鉴于标题“百万棋盘”以及内容仅为标题本身，因此无法提供全面的摘要。没有实际的文章内容可供总结。

然而，我们可以仅根据标题推测文章可能采取的潜在含义或方向：

*   **象棋的规模和复杂性：** 该标题可能暗示一篇探讨象棋战略的广度和复杂性的文章。“百万棋盘”可以代表游戏中无数种可能的局面和变化。文章可能讨论掌握象棋的难度以及即使是最强大的计算机也无法完全理解它的局限性。

*   **选择和可能性的隐喻：** “百万棋盘”可以隐喻生活或特定情况中的众多选择和可能性。每个棋盘代表不同的道路或结果，文章可能讨论决策、策略以及计划的重要性。

*   **象棋的变体和创造力：** 文章可能探讨象棋的不同变体，或对游戏采取的创造性新方法。每个棋盘可以代表经典规则的独特改编，展示创新和实验的潜力。

*   **象棋游戏的数据分析：** 该标题可能指的是分析大量象棋游戏的数据集，以寻找玩家行为和战略优势的模式、趋势或见解。“百万棋盘”可能代表了此类分析的显着样本量。

在没有更多上下文的情况下，不可能确定文章的实际主题。上面的摘要突出了基于有限信息的潜在解释。

---

## 27. Show HN: Memex - 一款基于 Rust+Tauri 的氛围编码 Claude Code 替代方案

**原文标题**: Show HN: Memex is a Claude Code alternative built on Rust+Tauri for vibe coding

**原文链接**: [https://memex.tech](https://memex.tech)

好的，以下是基于Memex登录页面（https://memex.tech）的摘要，假设我只能访问该页面，而无法访问原始链接的“Show HN”文章：

Memex被定位为专注于“氛围编码”的“Claude Code替代方案”。 这表明它的目标是AI辅助的代码生成和操作，但更强调用户体验、美学和创意探索，而不是纯粹的功能性代码输出。

该网站强调其底层技术栈使用Rust和Tauri。 Rust可能提供性能和可靠性，而Tauri用于构建跨平台桌面应用程序。 这种组合表明它是一个本地运行的应用程序，可能不依赖于外部云服务，从而可能解决隐私问题或提供离线功能。

“氛围编码”一词故意模糊，但似乎暗示了一种更直观和有趣的编码方法。 这可能涉及以下功能：

*   **可视化代码编辑：** 拖放界面、代码结构的可视化表示。
*   **主题代码生成：** 根据情感或风格提示生成代码，而不仅仅是功能规范。
*   **协作编码环境：** 促进头脑风暴和共享代码创建的工具。
*   **强调用户体验 (UX)：** 具有视觉吸引力且易于使用的界面。

该登录页面可能面向对尝试新的代码创建和操作方式感兴趣的开发人员，特别是那些重视美学、创造性表达和本地执行而不是纯粹基于云的代码生成的开发人员。 它将Memex定位为现有AI辅助编码工具的一种全新且创新的替代方案。 由于它是Show HN帖子，它可能是一个正在寻找反馈和早期采用者的新产品或测试版产品。

---

## 28. 使用 GraalVM 在 WASM 中运行 Clojure

**原文标题**: Running Clojure in WASM with GraalVM

**原文链接**: [https://romanliutikov.com/blog/running-clojure-in-wasm](https://romanliutikov.com/blog/running-clojure-in-wasm)

本文探讨了从25版本开始，使用GraalVM在WebAssembly (Wasm) 中运行Clojure程序的方法。虽然Wasm支持仍处于早期阶段且为单线程，但计算型的Clojure程序可以被编译并在浏览器中执行。

一个基本的 "Hello, World!" Clojure程序编译成一个5.6MB的Wasm二进制文件，可以使用`wasm-opt`将其缩小到约5MB，并进一步压缩到约2.5MB。 添加诸如`clojure.data.json`之类的库会增加二进制文件的大小（例如，增加130KB）。GraalVM提供构建报告，显示堆快照占据了二进制文件的大部分大小，其中字符串和哈希图消耗了很大一部分。 Java命名空间贡献了大部分方法。

性能基准测试表明，优化的Wasm二进制文件比未优化的二进制文件快约10％。 但是，相同的Clojure代码编译为本地镜像时，运行速度快2-3倍，而ClojureScript甚至更快。

本文还演示了Wasm-JavaScript互操作，展示了从Wasm中的Clojure进行DOM操作。 这涉及使用`org.graalvm.webimage.api`包来访问JavaScript环境。 `@JS`装饰器将本机Java方法绑定到在Wasm端执行的JavaScript代码。 本文最后提供了一个完整的Clojure设置的链接，演示了这些技术。

---

## 29. 西班牙和葡萄牙大范围停电

**原文标题**: Widespread power outage in Spain and Portugal

**原文链接**: [https://www.bbc.com/news/live/c9wpq8xrvd9t](https://www.bbc.com/news/live/c9wpq8xrvd9t)

西班牙和葡萄牙大范围停电引发调查以确定原因。虽然网络攻击已被排除，但西班牙首相佩德罗·桑切斯表示所有假设都在考虑之中。西班牙已启动调查委员会，葡萄牙已请求欧盟机构进行审计。目前正在探索的一个建议是与可再生能源有关联。

此次停电造成了重大破坏，特别是对交通运输，西班牙和葡萄牙的机场取消了数百个航班。英国广播公司（BBC）报道称，收到了大量关于停电影响的个人故事。

英国广播公司已结束直播报道，但继续报道事态发展，包括调查细节和恢复正常情况，并发布了有关影响和潜在原因的相关文章和视频内容。

---

## 30. 伊斯梅尔·贾扎里精巧机械装置手稿（约17世纪）

**原文标题**: Manuscript of Ismail al-Jazarī's Ingenious Mechanical Devices (ca. 17th century)

**原文链接**: [https://publicdomainreview.org/collection/arabic-machine-manuscript/](https://publicdomainreview.org/collection/arabic-machine-manuscript/)

伊斯兰科学手稿倡议（ISMI）的这篇条目聚焦于伊斯梅尔·贾扎里的著名著作《奇妙机械装置知识之书》的一份手稿。该书可追溯至大约17世纪，展示了贾扎里卓越的工程技能和伊斯兰黄金时代的创新。

该书的核心是对各种机械装置（包括水钟、喷泉、自动机（自动运转机器）和提水装置）的详细描述和插图的汇编。贾扎里细致地概述了每种装置的构造和操作，为他所采用的机械和液压原理提供了宝贵的见解。

这份手稿的意义在于它保存了贾扎里精巧的设计，并对技术史做出了贡献。它提供了对当时伊斯兰世界先进机械知识的第一手资料。伴随文本的插图对于理解所涉及的复杂机制至关重要。此外，它突出了伊斯兰学术在通过手稿保存和传播科学知识方面的重要性。ISMI对此类手稿的记录和研究对于理解更广泛的科学技术史以及伊斯兰学者在其发展中的作用至关重要。

---

## 31. Show HN: 纯 WebGL 图像编辑器，带滤镜、裁剪和透视校正

**原文标题**: Show HN: A pure WebGL image editor with filters, crop and perspective correction

**原文链接**: [https://github.com/xdadda/mini-photo-editor](https://github.com/xdadda/mini-photo-editor)

这个“Show HN”帖子介绍了一个纯WebGL图像编辑器，名为“mini-img-editor”。它是一个在线编辑器，可以通过提供的Netlify链接访问。主要功能包括滤镜、裁剪和透视校正。该编辑器利用WebGL2实现潜在的高性能图像处理。它使用作者创建的两个库：mini-js和mini-gl构建，两者都链接到各自的GitHub存储库。

---

## 32. 在SGLang中实现Flash Attention后端 – 基础知识与KV缓存

**原文标题**: Implement Flash Attention Back End in SGLang – Basics and KV Cache

**原文链接**: [https://hebiao064.github.io/fa3-attn-backend-basic](https://hebiao064.github.io/fa3-attn-backend-basic)

本文详细介绍了在SGLang LLM服务引擎中Flash Attention后端的实现，该后端现已成为SGLang 0.4.6中的默认注意力机制。文章解释了使用Flash Attention的动机，强调了其IO感知方法，从而减少内存读取/写入，并阐述了它如何融入SGLang架构。

文章概述了`AttentionBackend`类中的关键方法，包括`forward()`、`forward_extend()`、`forward_decode()`，以及支持CUDA图的方法（`init_cuda_graph_state()`、`init_forward_metadata()`等）。它还强调了`req_to_token_pool`在KV缓存管理中的重要性，阐述了它如何将请求映射到token KV缓存索引，以及`token_to_kv_pool`如何进一步将索引映射到实际的KV缓存数据。

文章深入探讨了实际实现，使用了Tri Dao的FlashAttention 3中的`flash_attn_with_kvcache` API。它解释了此API的必要参数，包括`k_cache`、`v_cache`、`page_table`和序列长度。文章进一步详细介绍了如何初始化`FlashAttentionMetadata`类来存储诸如序列长度、累积序列长度和页表等关键信息，从而确保在`forward_extend()`和`forward_decode()`方法中高效执行。文章还包含一个指向包含基本实现的pull request的链接。

---

## 33. Show HN: Sim Studio – 开源 Agent 工作流 GUI

**原文标题**: Show HN: Sim Studio – Open-Source Agent Workflow GUI

**原文链接**: [https://github.com/simstudioai/sim](https://github.com/simstudioai/sim)

Sim Studio 是一个开源平台，用于构建、测试和优化代理工作流程，并提供用户友好的 GUI。本文详细介绍了如何使用 Docker、Dev Containers 或手动设置来自行托管 Sim Studio。

**Docker 环境 (推荐):** 此方法使用 Docker Compose 便于设置，需要克隆存储库，配置环境变量（特别是 `BETTER_AUTH_SECRET`），并运行 `docker compose up -d --build`。提供了访问应用程序、查看日志、访问 PostgreSQL 数据库、停止环境以及在代码更改后重建的说明。 还包括通过 Ollama 将本地模型与 Sim Studio 结合使用或连接到现有 Ollama 实例的说明。

**Dev Containers:** 使用带有 Remote - Containers 扩展的 VS Code（或分支）可以通过在容器中重新打开项目来自动设置环境。

**手动设置:** 这包括克隆存储库，使用 `npm install` 安装依赖项，配置 `.env` 文件，使用 `npx drizzle-kit push` 设置数据库模式，以及使用 `npm run dev` 启动开发服务器。它强调了在生产环境中设置正确的电子邮件提供商的重要性。

本文最后列出了项目的技术栈（Next.js、PostgreSQL with Drizzle ORM、Better Auth、Shadcn、Tailwind CSS、Zustand、ReactFlow、Fumadocs），并邀请在 Apache License 2.0 下进行贡献。

---

## 34. 希腊语小品词 (1990)

**原文标题**: Greek Particles (1990)

**原文链接**: [https://specgram.com/Babel.I.2/07.sriyatha.greek.html](https://specgram.com/Babel.I.2/07.sriyatha.greek.html)

R.S. Sriyatha 的文章《希腊语助词》认为，古典学者从根本上误解了希腊语助词的功能，误将其视为有意义的副词或连词，而事实上，它们在很大程度上是毫无意义的感叹词，类似于现代英语中的“um”、“uh”或“you know”。

作者首先强调了书面语和口语之间的差异，指出口语中充满了犹豫和填充词，这些词很少被记录下来。他们用英语口语的例子来说明这一点，展示了感叹词如何出现在成分边界，通常在主要的句法成分之前或之后。

Sriyatha 随后将这种理解应用于古希腊语，并以色诺芬《远征记》中的一段文字为例。他们将一个典型的学生自然、充满感叹词的翻译与教师提供的正式、“正确”的翻译进行对比。作者认为，学生的版本更准确，反映了口语希腊语的真实性质。

文章最后断言，许多希腊语助词没有内在含义，主要起填充词的作用。作者认为，虽然有些助词可能源于具有语义内容的词，但共时分析表明，它们在使用中在很大程度上是毫无意义的。Sriyatha 呼吁对该主题进行进一步研究，但坚持认为，希腊语助词作为感叹词的核心概念现在已经显而易见。

---

## 35. Show HN: 我做了一个运行Python的硬件处理器

**原文标题**: Show HN: I built a hardware processor that runs Python

**原文链接**: [https://www.runpyxl.com/gpio](https://www.runpyxl.com/gpio)

此篇“Show HN”帖子介绍 PyXL，一款定制硬件处理器，可直接在硅芯片中执行 Python 代码，绕过传统的解释器、JIT 和操作系统。其主要优势在于速度和确定性，GPIO 往返测试表明，PyXL 耗时 480 纳秒，而 MicroPython (PyBoard) 耗时约 15,000 纳秒，经过时钟速度归一化后，性能提升了 30 到 50 倍。

PyXL 将 Python 代码编译成 CPython 字节码，然后将其转换为定制汇编语言，用于其流水线处理器。PyXL 在 Zynq-7000 FPGA 上运行，利用开发板的 ARM CPU 进行设置和内存管理，但完全在硬件中执行 Python 代码。

该帖子强调，PyXL 不是 C 扩展或 MicroPython 的变体，而是一个专用的 Python 处理器。它强调了确定性时序和实时行为，使其适用于需要亚微秒级精度的应用，例如实时控制系统、具有时序约束的 ML 推理、机器人技术和嵌入式工业系统。

作者承认，由于 PyXL 和 MicroPython 各自环境的差异，硬件访问的 API 调用有所不同，但标准 Python 代码在很大程度上仍然是可移植的。该帖子最后邀请读者联系作者进行进一步讨论。

---

## 36. 迁移出 Rust

**原文标题**: Migrating away from Rust

**原文链接**: [https://deadmoney.gg/news/articles/migrating-away-from-rust](https://deadmoney.gg/news/articles/migrating-away-from-rust)

2025年1月，《毁灭建筑师》的开发团队从Rust/Bevy转向C#/Unity。最初在2023年12月选择Bevy，是因为作者对Rust的热爱以及Bevy的ECS模型。尽管对Bevy充满热情并在tilemaps、角色逻辑和自定义渲染方面取得了显著进展，但实际挑战也随之而来。

由于将一个编程新手团队成员引入Rust具有挑战性，协作变得困难。Rust的底层特性阻碍了游戏机制的快速原型设计。Bevy中频繁的API更改导致耗时的更新迁移和意外的回归。此外，C#和Unity API的成熟性，以及充足的AI学习资源，与快速发展的Rust/Bevy生态系统相比，极大地提高了生产力。Modding潜力也是一个令人担忧的问题，因为在Rust/Bevy中找到一条清晰而自信的路径被证明是困难的。

最初对Unity不屑一顾的团队重新评估了他们的选择，对各种引擎进行了成本效益分析。一个为期三天的Unity核心功能（tilemap、角色、UI）实现实验产生了惊人的快速结果，证明了开发效率和易用性的提高。

随后为期六周的Unity/C#移植验证了这些发现，从而产生了更小、更易于维护的代码和更快的迭代速度。尽管缺少Rust中的Fluent本地化，但稳定生态系统和易于使用的工具所带来的好处超过了缺点。作者总结说，尽管个人对Rust和Bevy有亲和力，但Unity为《毁灭建筑师》的开发提供了一个更易于访问和更高效的环境。

---

## 37. 空中传播：AirPlay协议中可蠕虫式传播的零点击远程代码执行漏洞

**原文标题**: AirBorne: Wormable Zero-Click Remote Code Execution (RCE) in AirPlay Protocol

**原文链接**: [https://www.oligo.security/blog/airborne](https://www.oligo.security/blog/airborne)

Oligo Security Research发现了苹果AirPlay协议和SDK中的一组漏洞，名为“AirBorne”，可能使攻击者能够远程控制设备。这些漏洞影响苹果设备（Mac、iPhone、iPad、Apple TV等）和使用AirPlay SDK的第三方设备。

AirBorne可实现多种攻击途径，包括零点击和一点击远程代码执行（RCE）、访问控制列表（ACL）绕过、本地文件读取、敏感信息泄露、中间人（MITM）攻击和拒绝服务（DoS）。特别是，CVE-2025-24252和CVE-2025-24132允许可蠕虫化的零点击RCE漏洞利用，使恶意软件能够在本地网络上传播。

如果AirPlay接收器已启用并设置为“同一网络上的任何人”或“所有人”，则MacOS设备容易受到零点击RCE攻击。在“当前用户”配置下，可能发生一点击RCE。所有配置下，启用AirPlay SDK的扬声器和接收器容易受到零点击RCE攻击。CarPlay设备也容易受到RCE攻击，可能允许攻击者分散驾驶员的注意力或窃听。

Oligo向苹果披露了23个漏洞，导致了17个CVE。苹果已发布软件更新以解决这些问题。研究团队最初专注于端口7000，发现了可访问的命令和模式，从而开始了调查。这些攻击利用HTTP有效负载中的plist格式数据，利用了对plist参数的不当处理。

---

## 38. 展示HN: 心率区间Plus – 我开发的第一个iOS应用

**原文标题**: Show HN: Heart Rate Zones Plus – The first iOS app I developed

**原文链接**: [https://apps.apple.com/us/app/heart-rate-zones-plus/id6744743232](https://apps.apple.com/us/app/heart-rate-zones-plus/id6744743232)

“心率区间Plus”是由Tobias Willmann开发的iOS应用程序，旨在帮助用户追踪和了解他们在锻炼期间的心率区间表现。与一般的健身追踪器不同，这款应用程序专门分析在不同心率区间（1-5）所花费的时间，并帮助用户设定与心血管训练相关的有意义的健身目标。

主要功能包括：

*   **自定义时间段：**按天、周、月或自定义范围（过去7/30天）追踪在心率区间内的时间。
*   **锻炼归因：**识别哪些锻炼促成了在特定心率区间所花费的时间。
*   **多种区间计算方法：**允许用户选择各种科学支持的公式来计算最大心率，包括针对性别的选项，并调整静息心率。
*   **个人时间目标：**能够为每个心率区间设定和跟踪具体的时间目标进度。
*   **锻炼分解：**提供近期锻炼的详细概述，包括跨区间的时间和运动类型的分布。
*   **深色和浅色模式：**提供用户选择应用程序外观的选项。

该应用程序面向跑步者、骑自行车者、划船者、游泳者、生物黑客以及监测恢复期间运动量的人群。它强调用户隐私，仅将健康数据存储在设备上，并且仅在获得许可的情况下使用Apple HealthKit。该应用程序免费，体积小巧，需要iOS 18.2或更高版本。

---

## 39. 为拯救传统，哥伦比亚非裔砍刀击剑术最后的宗师奋力一战

**原文标题**: The last masters of Afro-Colombian machete fencing fight to save their tradition

**原文链接**: [https://globalvoices.org/2025/04/19/the-last-masters-of-afro-colombian-machete-fencing-fight-to-save-their-tradition/](https://globalvoices.org/2025/04/19/the-last-masters-of-afro-colombian-machete-fencing-fight-to-save-their-tradition/)

本文讨论了两个不同的主题，它们很可能是被错误地组合在一起的两篇文章：

1.  **哥伦比亚非裔砍刀击剑:** 核心重点似乎是非洲裔哥伦比亚人传统砍刀击剑的保护。"最后的宗师"正在努力拯救这一传统，这表明它正面临濒危和消失的风险。

2.  **巴西跨性别女性与美国签证:** 这部分重点讲述了一个问题，即巴西跨性别女性议员在美国签证上被归类为“男性”。这很可能是由于她们的性别认同与法定性别不符，或者可能是由于签证申请过程中的歧视性做法。文章指明作者为Luís Gustavo Carmo，译者为Fernanda Canofre，并指出文章于18小时前发表。

---

## 40. 我在2025年DjangoCon EU的收获

**原文标题**: My takeaways from DjangoCon EU 2025

**原文链接**: [https://www.zachbellay.com/posts/djangocon-eu-2025/](https://www.zachbellay.com/posts/djangocon-eu-2025/)

本文总结了在都柏林举行的DjangoCon EU 2025大会的主要收获。内容涵盖数据库优化、实用工具和库、最佳实践、Django社区更新、建模和架构模式以及其他观察。

**数据库：** 重点介绍了数据库优化技术，例如使用`select_for_update`锁定行、切换到BigInt主键、使用PostgresPartitionedModel分区表以及通过排除空值来优化Postgres索引。还提到了性能测试和分析方法。

**工具 & 库：** 作者列出了几个有用的工具，如`strace`、`django-neopolitan`、`django-auto-prefetch`、`django-csp`、`django-otp-webauthn`、`django-two-factor-auth`和`silence-lint-error`。他还推荐使用MaxMind来阻止恶意用户。

**最佳实践：** 文章强调了审查生成的SQL迁移、在测试中统计数据库查询以及清理旧的功能标志以防止错误的重要性。

**Django & 社区：** 作者注意到一个定制的Django管理仪表板以及Django功能提案转向使用GitHub issues。他还提到了一个用Rust编写的Django模板后端。

**其他主题包括：** 模式感知EAV建模、`{% spaceless %}`模板标签以及使用Django的公司。文章最后总结了作者对大会的印象，包括友好的氛围以及欧洲和美国之间的差异。他还列出了他最喜欢的演讲。

---

## 41. 动量工坊(2017)的缘起

**原文标题**: Why Momentum Works (2017)

**原文链接**: [https://distill.pub/2017/momentum/](https://distill.pub/2017/momentum/)

好的，仅根据提供的信息，我可以对一篇名为《动量为何有效（2017）》的假设性文章在Distill上发表的进行简要总结：

鉴于标题和Distill（一个清晰且互动性强的科学交流平台）的背景，这篇文章很可能探讨金融市场中动量效应背后的原因。

核心论点很可能是，动量，即近期表现良好的资产在短期至中期内继续表现良好的趋势，是一种稳健且持续存在的异常现象。

文章中可能讨论的解释（支持标题中的“为何”）可能包括：

*   **行为偏差：** 投资者对新信息反应不足、羊群效应和确认偏差。
*   **信息传播：** 信息传播缓慢，导致价格调整滞后。
*   **机构因素：** 投资组合经理面临的限制，例如基准或风险厌恶，阻止他们充分利用有利可图的机会。
*   **基于风险的解释：** 动量可能是对承担特定类型风险的补偿（尽管这并不是证明动量合理的常见论点）。

由于该文章发表在Distill上，它也很可能提供实证证据来支持动量策略的存在和盈利能力，可能包括交互式可视化来展示这种效应。

包含“Prize”和“Submit”表明该文章可能属于Distill平台上的竞赛或征稿活动的一部分，这意味着高标准的研究和清晰度。然而，这些仅仅是平台特征，并不增加文章的内容。

---

## 42. 12位彩虹调色板

**原文标题**: The 12-bit rainbow palette

**原文链接**: [https://iamkate.com/data/12-bit-rainbow/](https://iamkate.com/data/12-bit-rainbow/)

本文介绍了为“国家电网：实时”项目设计的12位彩虹调色板。作者解释说，传统的基于RGB的彩虹调色板存在颜色之间感知亮度不均匀的问题，因为我们的眼睛对红色、绿色和蓝色的亮度感知程度不同。

为了解决这个问题，作者探索了LCH色彩空间，该空间以感知均匀的方式定义颜色的亮度、色度和色相。虽然具有固定色度和亮度的LCH彩虹调色板可以创建更平衡的调色板，但它可能导致不良的颜色偏移（例如，黄色变暗为棕色）。

最终选择的解决方案包括允许亮度以受控方式变化。黄色被指定为最高亮度，红色和蓝色被选为锚点颜色。然后计算其他色相的亮度，从而产生具有更平滑亮度过渡的调色板。

由于12位颜色深度的限制，对亮度、色度和色相进行了细微调整，以创建最终的调色板，该调色板由十二种颜色组成，并用四字符十六进制代码表示（例如，#817）。由此产生的调色板具有均匀间隔的色相、最小的色度变化和流畅的亮度梯度，使其在视觉上具有吸引力并且对项目具有实用性。

---

## 43. Show HN: Web-eval-agent – 让编码代理自行调试

**原文标题**: Show HN: Web-eval-agent – Let the coding agent debug itself

**原文链接**: [https://github.com/Operative-Sh/web-eval-agent](https://github.com/Operative-Sh/web-eval-agent)

Operative.sh 引入 `web-eval-agent`，一种赋能编码智能体在代码编辑器内自主调试 Web 应用程序的工具，从而解放开发人员的时间。该工具利用浏览器使用代理和 MCP 服务器来端到端地执行和测试 Web 应用程序。

主要功能包括：

*   **浏览器导航：** 利用 BrowserUse 实现高效的 Web 应用程序导航。
*   **网络流量捕获：** 智能过滤并在上下文窗口内返回网络请求。
*   **控制台错误收集：** 捕获控制台日志和错误。
*   **自主调试：** 使智能体能够通过 Web QA 智能体/MCP 服务器自动测试其代码。

该服务为 macOS/Linux 用户提供了快速入门指南，其中包含一个简单的安装脚本。还提供了使用 `uv` 进行 Windows (Cline) 手动安装的说明。

该文档解决了与工具调用相关的初始 Playwright 问题（现已修复），并鼓励用户报告任何其他问题。

其中包含一个详细的 MCP 服务器输出报告示例，展示了一个成功的 API 密钥删除流程测试，演示了智能体导航、与元素交互以及验证结果的能力，同时捕获控制台日志、网络请求和事件的时间顺序时间线。该解决方案鼓励用户访问 "Operative Control Center" 以查看实时日志。

---

## 44. 西班牙即将面临“黑启动”的挑战

**原文标题**: Spain is about to face the challenge of a "black start"

**原文链接**: [https://arstechnica.com/science/2025/04/why-restarting-a-power-grid-is-so-hard/](https://arstechnica.com/science/2025/04/why-restarting-a-power-grid-is-so-hard/)

西班牙和葡萄牙面临大规模停电，需要复杂的“黑启动”过程来恢复电力。由于发电厂和电网管理系统本身也需要电力才能运行，这个过程非常困难。只有特定的设施，通常是配备柴油发电机的较小电厂，才具备黑启动能力。

来自这些设施的初始电力必须小心地导向其他发电厂，以使其上线，避免用一般需求压垮有限的初始供应。来自邻近电网（法国和摩洛哥）的外部电力可以提供帮助，但需要将其隔离并直接发送到闲置的发电厂。一旦有足够多的电厂上线，它们必须将输出同步到单一频率，然后才能满足需求。

文章强调了将电网恢复上线所需的微妙平衡。如果管理不当，等待供电的空调和其他设备的高需求可能会导致立即电网故障。维持电网频率至关重要，因为不正确的频率会损坏设备。电网运营商必须仔细估计需求，并逐步将电网的各个部分上线，使其与额外的发电能力相匹配。

西班牙和葡萄牙拥有水力发电资源，因其对外部电力需求较低，因此可用于黑启动。风能和太阳能等可再生能源可以做出贡献，太阳能的直流电有可能稳定频率。然而，太阳能受到日光时间的限制，风能的可用性取决于天气条件和黑启动设备。用于频率稳定和电厂启动的理想选择——电网级电池，目前在这两个国家都受到限制。由于其复杂性和可能导致进一步故障的风险，预计恢复需要数天时间。

---

## 45. Haskell 中的打包数据支持

**原文标题**: Packed Data Support in Haskell

**原文链接**: [https://arthi-chaud.github.io/posts/packed/](https://arthi-chaud.github.io/posts/packed/)

本博文介绍了一个 Haskell 库 `packed-data`，旨在为紧凑数据结构提供类型安全且可移植的支持，从而避免数据传输时的序列化/反序列化，以提高性能。紧凑数据在内存中连续存储数据，消除指针跳转并提高缓存利用率。

该库使用 Template Haskell 生成用于打包、解包和遍历数据类型的代码。它引入了 `NeedsBuilder` 用于构建紧凑数据缓冲区，并引入了 `PackedReader`，一个索引单子，以安全地管理数据访问期间的指针操作。生成的 `case` 函数有助于对紧凑数据进行模式匹配和遍历。为了处理数据结构中的可变大小字段，该库自动插入间接引用 (FieldSize) 以实现高效跳过。

基准测试比较了 `packed-data` 与标准 Haskell、C 和 Gibbon 在各种树操作上的性能。虽然某些操作显示出加速（例如 AST 评估），但其他操作由于单子 `PackedReader` 抽象的开销而较慢。作者建议未来的工作可能涉及从 `PackedReader` 生成 C 代码以减少开销，并探索在其他强类型语言中使用类似基于库的方法的潜力。 目标是在不需要编译器修改的情况下实现紧凑数据的性能优势。

---

## 46. 需求会一直变，直到不变为止。

**原文标题**: Requirements change until they don't

**原文链接**: [https://buttondown.com/hillelwayne/archive/requirements-change-until-they-dont/](https://buttondown.com/hillelwayne/archive/requirements-change-until-they-dont/)

本文探讨了形式化方法(FM)在软件开发中的价值，尤其是在需求不断演变的情况下。尽管承认形式化方法的高成本和复杂性使其在需求频繁变更时并不实用，但作者认为，当解决方案稳定下来，需要可靠地维护和扩展时，形式化方法就变得至关重要。

核心思想是，每个成功的特性都会产生“保持其正常运行”的需求，这是一种永久的期望。作者引入了软件中的“相变”隐喻，系统会经历重大的架构或设计转变，以应对不断增加的负载或复杂性。这些相变，比如从同步处理切换到异步处理，往往会引入bug，打破现有的客户期望。

形式化方法可以用于正式指定新旧系统的行为，并自动检查相变是否违反现有需求或引入新的bug。作者认为，这正是形式化方法的闪光点，它使开发人员能够确保新版本的软件继续解决最初设计要解决的问题，即使在重大变更之后。最终，形式化方法提供了必要的工具，以确保软件继续满足客户需求，并在系统演变过程中有效地工作。

---

## 47. 加州高铁之死被严重夸大了。

**原文标题**: Reports of the death of California High-Speed Rail have been greatly exaggerated

**原文链接**: [https://asteriskmag.com/issues/10/reports-of-the-death-of-california-high-speed-rail-have-been-greatly-exaggerated](https://asteriskmag.com/issues/10/reports-of-the-death-of-california-high-speed-rail-have-been-greatly-exaggerated)

加州高铁末日之说尚早，问题在于资金不足和政治犹豫。

---

## 48. 跑赢大众

**原文标题**: Beating the Crowd

**原文链接**: [https://www.withentropy.com/blog/2025-04-21-beating_the_crowd/](https://www.withentropy.com/blog/2025-04-21-beating_the_crowd/)

本文探讨了“逆向思维”的概念及其相关风险，并以拍卖和日常生活为例进行说明。文章首先从“赢者的诅咒”入手，阐述了即使理由看似充分，赢得拍卖也可能是一个负面信号，因为它表明你对该物品的估值高于其他人。

然后，文章将此与“群体智慧”进行对比，引用高尔顿的牛重实验作为证据，表明在缺乏其他信息的情况下，群体的平均猜测可能出人意料地准确。作者将这些观点应用于各种场景，例如在迪士尼乐园排队、预订餐厅、获得一份声望很高的工作以及开始一段浪漫关系，并强调了每个场景中潜在的陷阱。

作者概述了“群体智慧”的三个例外情况，在这些情况下，反其道而行之可能是有益的：拥有信息优势（比其他人知道更多），拥有意愿差异（由于个人情况而对某事物的估值不同），以及拥有不同的处境（他人不具备的独特经验和环境，如恋爱关系）。

最终，文章强调决策不应孤立地做出。作者提出了一个两步清单：首先，基于个人分析做出决策，然后，考虑该决策如何受到他人行为和观点的影响。作者强调，考虑更广泛的背景，避免在真空中做出决策对于避免后悔至关重要。

---

## 49. 克里斯·克雷布斯支持信

**原文标题**: Chris Krebs Support Letter

**原文链接**: [https://www.eff.org/document/chris-krebs-support-letter-april-28-2025](https://www.eff.org/document/chris-krebs-support-letter-april-28-2025)

这是电子前哨基金会 (EFF) 的一个网页，宣布了一封支持克里斯·克雷布斯的信件，日期为 2025 年 4 月 28 日。该页面提供了一个链接以下载该信件的 PDF 文档。EFF 是一个专注于捍卫数字世界公民自由的组织，致力于言论自由、隐私、安全、创造力与创新、透明度和国际数字权利等问题。这封支持信在 EFF 网站上被标记为“言论自由”和“安全”问题，表明该信函涉及克雷布斯在这些主题上的贡献或经验。该页面还提供了其他 EFF 资源的链接，参与方式（捐赠、志愿者、加入电子前哨联盟）、工具和联系方式。它还包括标准的网站页脚信息，例如版权详细信息、隐私政策、社交媒体链接以及有关 EFF 评级和历史的信息。

---

## 50. 外呼要死了吗？

**原文标题**: Is outbound going to die?

**原文链接**: [https://rnikhil.com/2025/04/25/sales-outbound-ai-dead](https://rnikhil.com/2025/04/25/sales-outbound-ai-dead)

本文探讨了在日益成熟的AI驱动的销售和营销工具背景下，主动销售的潜在未来。作者认为，虽然这些工具通过实现高度个性化、高容量的触达，在短期内提供了优势，但最终会导致用户疲劳和信任度下降，因为“AI垃圾”的数量巨大。随着每个人都能使用这些工具，当公司争夺同一目标受众时，主动销售的有效性将大大降低。

作者认为，这种饱和将迫使人们转向内容营销、推荐和培养个人关系。公司需要专注于建立强大的品牌，利用公司拥有的渠道直接访问客户，并培养充满活力的社区和网络效应。强大的社交媒体影响力，尤其是在Twitter等平台上，对于产生病毒式传播和品牌知名度至关重要。

本质上，未来将青睐那些能够建立基于客户忠诚度、社区参与和人际关系的强大自然增长引擎的公司，而不是仅仅依赖于AI驱动的主动销售策略。未来的守门人将是网络中的决策者，访问权限将通过关系而非仅仅是个性化消息传递来授予。

---

## 51. Palantir 为建立 ICE 主数据库的理由

**原文标题**: Palantir's Justification for Building ICE's Master Database

**原文链接**: [https://www.404media.co/this-is-palantirs-justification-for-building-ices-master-database/](https://www.404media.co/this-is-palantirs-justification-for-building-ices-master-database/)

本文详细介绍了Palantir在ICE移民执法工作中日益扩大的作用，特别是构建一个“主数据库”以利用来自各个政府机构的数据追踪移民。404 Media和其他媒体的报道揭示了Palantir参与了诸如“ImmigrationOS”等项目，并支持“执法优先级和目标制定”、“自我遣返追踪”和“移民生命周期运营”。

文章强调了Palantir对此项工作的内部理由，声称其能促进“效率、透明度和责任制”，并能实现对移民的“公平对待”。然而，Just Futures Law组织的Laura Rivera等批评人士谴责Palantir的措辞是对现实的扭曲，指责该公司同谋参与了“威权主义议程”。

泄露的Palantir内部维基页面揭示了该公司与ICE，特别是国土安全调查局(HSI)的长期关系，重点关注跨国犯罪活动。它强调了该公司在内部开发工作受挫以及该机构的重点转向移民执法后，重新与ICE合作的努力。

Palantir承认存在隐私和公民自由方面的风险，但相信其技术可以提高数据质量、机构协调和透明度。文章强调了隐私影响评估(PIA)和记录系统通知(SORN)的重要性。作者正在征集来自Palantir员工或与此工作相关人员的信息。

---

## 52. 为了电影而合法伪造艺术品 (2014)

**原文标题**: Legal art forgery, for the sake of movies (2014)

**原文链接**: [https://www.vanityfair.com/hollywood/2014/04/art-in-movies](https://www.vanityfair.com/hollywood/2014/04/art-in-movies)

本文探讨了电影中重现著名艺术品的复杂过程，重点关注其中涉及的法律和艺术挑战。 在 90 年代中期之前，艺术图像的权利监管较少； 然而，在发生重大版权诉讼后，制片公司变得更加谨慎，导致绘画的图像在电影中的使用过程变得错综复杂。

本文使用几个电影例子来说明这些观点。 由于遗产费过高，《巴斯奇亚》不得不重新创作艺术家的作品。 他们甚至在拍摄后不得不销毁他们绘制的毕加索《格尔尼卡》复制品，并为毕加索遗产机构记录了销毁过程，以避免伪造问题。 《戴珍珠耳环的少女》涉及细致地重现维米尔的画作，外包尝试失败，最终开发出一种独特的方法，将纸质复制品粘贴到画布上并进行纹理处理。 对于《波洛克》，遗产机构非常合作，允许复制许多作品，重点是重现滴画的能量和过程，而不是精确的复制品。 最后，《盟军夺宝队》大量依赖数字技术和高分辨率文件来复制大量艺术品，重点关注画框的质量和重现年代感的效果。 尽管付出了努力和保证了质量，但大多数重现的艺术品最终还是回到了制片公司，通常被储存起来。

---

## 53. Vision Transformers 需要寄存器

**原文标题**: Vision Transformers Need Registers

**原文链接**: [https://arxiv.org/abs/2309.16588](https://arxiv.org/abs/2309.16588)

视觉Transformer需要寄存器

本文《视觉Transformer需要寄存器》识别并解决了监督式和自监督式视觉Transformer (ViT) 特征图中的伪影。作者发现，在推理过程中，高范数标记出现在低信息量的背景区域中，并被用于内部计算。

为了解决这个问题，他们提出了一个简单而有效的解决方案：向ViT的输入序列提供额外的标记，作为“寄存器”发挥作用。这些寄存器有效地吸收了伪影行为。

实施该解决方案的结果非常显著。该论文证明，使用寄存器可以完全消除监督式和自监督式模型中存在的问题伪影。此外，它还在密集预测任务上实现了自监督视觉模型的最新性能，改进了对象发现方法，最重要的是，它实现了更平滑的特征图和注意力图，最终改进了下游视觉处理。该论文强调，这种方法对ViT的性能和可解释性都产生了积极影响。

---

## 54. 寻觅暗夜，星河寄愿

**原文标题**: Hunting for dark nights and wishing on stars

**原文链接**: [https://www.hcn.org/articles/hunting-for-dark-nights-and-wishing-on-stars/](https://www.hcn.org/articles/hunting-for-dark-nights-and-wishing-on-stars/)

在《追寻暗夜，星河寄愿》中，克雷格·查尔兹叙述了他和朋友欧文·福克斯-费尔南德斯的一次沙漠骑行观星之旅，旨在逃离现代生活的光污染，尤其是来自拉斯维加斯的光污染。查尔兹因自行车座而感到沮丧，却在充满挑战的风景和它所提供的自由中找到了慰藉。朋友们收集木柴，小心翼翼地生火，以便他们仍然能看到星星。

夜幕降临，他们尝试观察星星和星座，回忆过去人们可以轻松看到夜空的景象。查尔兹解释了如何重新与夜空互动，例如识别星座、追踪太阳的落日点以及专注于一颗星星。他还提到了占星术的影响。

这篇文章突出了来自拉斯维加斯日益严重的光污染，与查尔兹在20世纪80年代的经历相比，这种光污染已经大大降低了星星的可见度。尽管寒冷和光污染，他们还是使用天空质量测量仪来测量夜空的黑暗程度。查尔兹对读数表示失望，希望当他们进一步进入沙漠国家野生动物保护区时，能找到更黑暗的天空。最终，他们发现即使在偏远的沙漠中，逃离人类文明的普遍光辉也变得越来越困难。

---

## 55. Tiny-LLM – 面向系统工程师的Apple Silicon LLM部署课程

**原文标题**: Tiny-LLM – a course of serving LLM on Apple Silicon for systems engineers

**原文链接**: [https://github.com/skyzh/tiny-llm](https://github.com/skyzh/tiny-llm)

Tiny-LLM：利用MLX在Apple Silicon上高效部署大型语言模型的教程，面向系统工程师。本教程强调实践，使用MLX数组/矩阵API从零构建模型服务基础设施，而非更高级别的神经网络库，以便深入研究优化技术。该项目以Qwen2为例，因为作者对其熟悉，且其在vllm文档中较为突出。

本教程以周为单位组织，逐步涵盖注意力机制、RoPE、分组查询注意力、RMSNorm、MLP、Transformer模块、模型加载、解码、KV缓存、量化矩阵乘法（CPU和GPU）、Flash Attention、连续批处理、推测解码、Prompt/Prefix缓存、分页注意力、预填充-解码分离、调度器、并行性、AI Agent和流式API服务器等主题。

虽然仍在开发中，该课程已完成注意力、RoPE和响应生成等核心概念章节。本书可在GitHub上获取。存在一个Discord社区，用于协作学习。

---

## 56. 巨蟒与圣杯五十周年

**原文标题**: Monty Python and the Holy Grail turns 50

**原文链接**: [https://arstechnica.com/culture/2025/04/monty-python-and-the-holy-grail-turns-50/](https://arstechnica.com/culture/2025/04/monty-python-and-the-holy-grail-turns-50/)

本文庆祝《巨蟒与圣杯》上映五十周年，这部电影被广泛认为是喜剧杰作。文章重点介绍了该电影对娱乐和学术界的影响。文章指出，影片最初的评价褒贬不一，但最终票房大获成功，并经久不衰。

几位 Ars 的员工分享了他们个人对这部电影的体验，讨论了其标志性场景和喜剧技巧。珍妮弗·奥莱特专注于“椰子马”场景和关于燕子的荒诞辩论，强调了该电影早期“书呆子气息”的例子。雅各布·梅反思了意想不到的暴力杀手兔子，认为它教会了人们不要以貌取人的道理。

阿什利·贝朗格研究了罐头音乐的使用，解释了特里·琼斯如何战略性地利用它来增强喜剧节奏。凯文·珀迪幽默地回忆起他十几岁时意识到自己喜爱的电影部分资金来自他鄙视的经典摇滚乐队，模糊了他所认为的文化英雄和恶棍之间的界限。

文章强调了该电影的荒诞幽默、名言金句和文化影响力，说明了其持久的遗产和在上映 50 年后持续的意义。

---

## 57. 英特尔承认了我们都知道的事：没人买AI PC。

**原文标题**: Intel admits what we all knew: no one is buying AI PCs

**原文链接**: [https://www.xda-developers.com/intel-admits-what-we-all-knew-no-one-is-buying-ai-pcs/](https://www.xda-developers.com/intel-admits-what-we-all-knew-no-one-is-buying-ai-pcs/)

英特尔旧款CPU需求高于新款，AI PC普及受阻。

---

## 58. 股颂 (2024)

**原文标题**: An Ode to the Thigh (2024)

**原文链接**: [https://ponnekanti.net/posts/an-ode-to-the-thigh/](https://ponnekanti.net/posts/an-ode-to-the-thigh/)

股颂

2024年10月15日创作的《股颂》中，作者描述了一次令其印象深刻的医学院大腿解剖。他们强调了大腿解剖结构的美丽和功能优雅，特别是阔筋膜。这种“伟大的筋膜”就像一个有凝聚力的鞘，限制肌肉扩张，并利用肌肉收缩来按摩静脉，帮助下肢静脉回流，这在对抗重力影响方面尤其重要。

作者详细描述了解剖大腿的过程，将剥开筋膜比作剥橙子，露出了下面的肌肉：髂腰肌、股四头肌、像日本折扇一样的内收肌以及缝匠肌。

作者反思了为什么大腿，而不是大脑，给他们留下了更卓越设计典范的印象。他们认为，腿在运动中的主要功能，对于通过狩猎和逃避来实现生存和繁殖至关重要，这使其成为进化角度来看的根本重要的解剖结构。作者认为，虽然意识可能会在大脑中寻求美，但自然会优先考虑对运动至关重要的结构，强调后肢是这种进化动力的支点。

---

## 59. 博西 – 为我家三岁孩子打造的离线音频播放器

**原文标题**: Boxie – an always offline audio player for my 3 year old

**原文链接**: [https://mariozechner.at/posts/2025-04-20-boxie/](https://mariozechner.at/posts/2025-04-20-boxie/)

本文详细介绍了作者受Game Boy启发，为三岁的儿子打造离线音频播放器“Boxie”的历程。因不满Tonie Box的局限性，作者决定创造一款完全离线、基于卡带且易于幼儿使用的设备。

作者重点介绍了他们获得的技能，包括焊接、ESP32微控制器的使用、使用EasyEDA Pro进行PCB设计以及使用Fusion 360进行3D外壳建模。文章提供了一个全面的工具清单，包括焊接设备、热风枪、数码显微镜和3D打印机。

Boxie的设计强调简洁性和耐用性。它具有音量旋钮、导航按钮和一个卡带插槽，用于插入定制设计的卡带（装在3D打印外壳中的micro SD卡）。插入卡带即可打开设备，移除卡带即可关闭设备。这些卡带的设计带有可见的标签，以便儿童识别有声读物。

卡带本身是一个定制的PCB，带有micro SD卡插座和连接焊盘。作者分享了他们设计和组装卡带的过程，包括一次颇为痛苦的手工焊接经历。卡带阅读器采用了一种不同的方法将卡带焊盘连接到ESP32-S3。

作者鼓励读者超越Arduino，探索ESP32的功能，甚至暗示了他们自己在ESP-IDF之上的C-API框架。

---

## 60. 来自地狱的副业

**原文标题**: The side hustle from hell

**原文链接**: [https://blog.jacobstechtavern.com/p/the-side-hustle-from-hell](https://blog.jacobstechtavern.com/p/the-side-hustle-from-hell)

雅各布“地狱般的副业”：他在Fixr创业公司11个月的经历。Fixr是一款旨在连接车主和当地机械师的应用程序。受创业成功的诱惑，雅各布以联合创始人和首席技术官的身份加入，他的朋友格斯担任安卓开发人员。他们被承诺各自获得10%的股权。

最初，Fixr似乎很有前景，拥有一个网站、一些来自个人贷款的资金以及风险投资公司的兴趣。然而，雅各布很快发现现有的应用程序漏洞百出，并且是由之前的承包商糟糕地构建的。他和格斯从头开始重建了应用程序，创建了一个MVP。

尽管他们付出了努力，但发布还是失败了。这家创业公司没有签约的机械师，也没有吸引用户的营销策略。雅各布意识到创始人吉米、金和迈克功能失调：吉米和迈克彼此厌恶，金充当调解人，股权分配是随意的。

雅各布努力让机械师加入并投放社交媒体广告，但需求的缺乏和供应的短缺造成了僵局。他甚至考虑为企业贷款共同签名以获得更多股权，但最终拒绝了。

最终，雅各布意识到由于创始人无能和缺乏运营执行力，这家创业公司注定要失败。大约在那个时候，他被一家名为Carbn的绿色科技创业公司招募，该公司拥有更坚实的基础和一位愿意承诺和补偿的创始人。他离开了Fixr，变得更聪明了，但也留下了伤痕。

---

## 61. 知识社会，见鬼去吧

**原文标题**: Knowledge-based society, my ass

**原文链接**: [https://mihaiolteanu.me/knowledge-based-society-my-ass](https://mihaiolteanu.me/knowledge-based-society-my-ass)

这段自传体文章记录了作者在欧盟资助的、旨在创建“知识型社会”的项目中攻读工程科学博士学位时，令人失望的经历。作者最初对学术追求充满热情，辞掉了稳定的工作，却发现他的教授对他漠不关心、处处阻挠。

作者最初的热情很快消退，因为他难以获得诸如办公室、电脑和软件许可等基本资源，面临官僚障碍和一个更关心表面功夫而非实际研究的冷漠教授。作者被隔离在地下室“办公室”里，无法获得实验室设备、真实世界的数据以及有意义的合作。

尽管缺乏支持，作者还是通过大幅简化研究发表了几篇论文，承认自己工作的肤浅。他发现大学期刊内普遍存在抄袭现象，并发现学术环境的特点是肤浅的形式主义，侧重于头衔和外表，而不是真正的学术交流。

作者详细描述了功能失调的行政流程，突出了项目雄心勃勃的目标与资金不足、孤立的研究现实之间的差距。高潮是教授最初拒绝了论文，专注于细微的语法错误，而不是实质性问题。最终，作者完成了论文答辩，但对学术体制感到失望，并质疑其中产生的研究的相关性和完整性。这篇文章批判了理想化的知识型社会愿景与学术研究中常常存在的问题之间的差距。

---

## 62. 揭秘冰雪挑战赛的机制

**原文标题**: Uncovering the mechanics of The Games: Winter Challenge

**原文链接**: [https://mrwint.github.io/winter/writeup/writeup.html](https://mrwint.github.io/winter/writeup/writeup.html)

出于怀旧和好奇，身为计算机科学家的作者踏上了一段旅程，旨在理解DOS游戏《奥运会：冬季挑战》的内部运作机制，特别是跳台滑雪项目。其目标是确定理论上的最佳跳跃距离。

最初使用Ghidra反汇编游戏的计划演变成了一项复杂的调查，深入研究了基于DOS的程序架构、复制保护方法以及90年代早期游戏开发的复杂性。

文章详细介绍了获取不同版本游戏时遇到的挑战，包括原始软盘版本、GOG版本和破解版本。原始游戏使用密码轮进行复制保护。作者调查了密码轮检查的实现方式以及隐藏的复制保护措施是否会影响游戏体验。

调查发现，游戏二进制文件使用LZEXE压缩，需要解压。进一步分析表明，由于DOS的内存限制，游戏使用了覆盖层进行内存管理，这是一种常见的技术。该游戏采用了自定义的覆盖层管理实现，而不是标准的Microsoft C编译器覆盖层系统。

作者使用DOSBox-X模拟器的调试功能来监控文件I/O，并确定游戏在主程序段之后读取数据块。这表明需要提取资源文件才能完全逆向工程游戏逻辑。调查仍在进行中。

---

## 63. 网络罪犯声称对西班牙和葡萄牙停电负责

**原文标题**: Cybercriminals Take Responsibility for Spain and Portugal Power Outages

**原文链接**: [https://leakd.com/cyber-security/massive-power-outage-hits-spain-and-portugal-amid-claims-by-pro-russian-hacker-groups/](https://leakd.com/cyber-security/massive-power-outage-hits-spain-and-portugal-amid-claims-by-pro-russian-hacker-groups/)

西班牙和葡萄牙发生大规模停电，法国南部部分地区也出现相关报告。 尽管尚未确定官方原因，但怀疑指向潜在的网络攻击，尤其是西班牙气象机构排除了异常大气条件之后。

停电开始后不久，网络犯罪团伙“暗黑风暴团队”和“NoName057”通过Telegram和X声称对此负责。 他们发布链接，暗示葡萄牙政府网络遭到入侵，包括内政部、司法部、环境部和总统府，并有Check-Host.net的数据支持，显示这些服务中断。

文章强调了该事件的潜在严重性，将其与2021年的 Colonial Pipeline 勒索软件攻击进行了比较。“NoName057”这个亲俄黑客行动主义团体与“暗黑风暴团队”的结盟，引发了人们对可能的国家参与以及针对北约附属国家升级网络战的担忧。 问题仍然是，DDoS攻击还是更深层次的网络入侵，实际上是否能够瘫痪电网。 调查正在进行中，欧洲官员尚未正式回应网络攻击的说法，导致公众对情况一无所知。

---

## 64. 识别记忆中的模式 (2022)

**原文标题**: Recognizing Patterns in Memory (2022)

**原文链接**: [https://www.timdbg.com/posts/recognizing-patterns/](https://www.timdbg.com/posts/recognizing-patterns/)

本文重点在于识别内存转储中的模式，以帮助调试，尤其是在事后分析中。作者认为模式识别是一种通过经验磨练的技能，并旨在提供一些常见的模式供查找。

讨论的关键模式包括：

*   **对齐的32/64位数据：** 查找每4或8个字节重复出现的模式，表明对齐的值，通常小于分配的空间。
*   **指针：** Windows用户模式下的64位指针通常高16位为零（0x0000XXXX'XXXXXXXX）。`!address`命令可以验证一个值是否是有效的地址，`ln`和`!heap`提供额外的信息。
*   **UTF-16字符：** 这种编码通常显示ASCII字符与空字节交错，使其在十六进制查看器中易于识别。
*   **代码字节：** 可以通过缺乏对齐、存在用于断点的`CC`字节（INT 3指令）和指示返回指令的`C3`字节来识别x64代码。`4X`字节通常是用于访问较大寄存器的REX前缀，后面经常跟着代表ALU或MOV操作的`8X`字节。序列`54 55 57 56 53`指示一系列push/pop指令。
*   **高熵数据：** 缺乏上述模式可能表明是压缩或加密的数据。识别头部或应用程序特定的数据处理可以帮助理解格式。

作者鼓励读者训练他们的模式识别技能，并分享他们自己的调试技术。

---

## 65. 用 IPL-V 重现首个人工智能逻辑理论家 [视频]

**原文标题**: Reanimation of the original Logic Theorist, the first AI, in IPL-V [video]

**原文链接**: [https://www.youtube.com/watch?v=qmE5o2ezqBg](https://www.youtube.com/watch?v=qmE5o2ezqBg)

视频标题宣布了一个雄心勃勃的项目：**使用IPL-V编程语言复活最初的逻辑理论家，它被认为是第一个AI程序。** 这意味着对一个具有历史意义的AI程序的重新实现和潜在的复兴。

然而，正如描述的，视频的实际内容仅仅是YouTube的标准页脚信息，包括以下链接：

*   **法律信息：** 版权，服务条款，隐私政策，安全。
*   **实用链接：** 联系我们，创作者，广告客户，开发者。
*   **通用信息：** YouTube运作方式，测试新功能，NFL Sunday Ticket (提到2025年)。

这表明所提供的“内容”与视频标题无关，可能代表占位符文本或不相关的元数据。 因此，我们无法根据所提供的信息总结视频的实际内容。 我们拥有的唯一信息是该视频*打算*展示用IPL-V复活逻辑理论家。

---

## 66. 逆转计算机科学会议的僵化

**原文标题**: Reversing the fossilization of computer science conferences

**原文链接**: [https://cacm.acm.org/blogcacm/reversing-the-fossilization-of-computer-science-conferences/](https://cacm.acm.org/blogcacm/reversing-the-fossilization-of-computer-science-conferences/)

伯特兰·迈耶认为，计算机科学会议曾经对创新至关重要，但由于官僚主义和对职业晋升优先于科学进步的转变，正变得日益僵化。他指出，会议现在被视为年度“考试”，其中对僵化的亚文化标准的正式遵守，掩盖了对具有潜在影响的新颖想法的评估。由于这些限制，比特币和Transformer模型等著名创新都绕过了传统的会议出版。

迈耶批评了专注于细微偏差的“抓包”式审稿风格，以及论文必须符合固定结构的压力。他强调了过于具体的格式规则（如引文格式）的荒谬性，以及缺乏广泛实证评估的概念性工作的否定。

他将这种衰退归因于会议参与的职业化，即成为PC成员被视为简历助推器，导致缺乏经验、雄心勃勃的学者评判专家的工作。他认为，评审的匿名性加剧了这个问题。

迈耶提出了扭转这一趋势的实际解决方案。他倡导PC委员会内部转变思维，强调识别合理的创新，而不是寻找错误。他呼吁简化“论文征集”、减少官僚规则，并将论文选择的最终责任分配给该领域内已确立的领导者。他认为，会议应优先考虑推进知识，而不是增加个人Google Scholar档案，使其回归核心使命。

---

## 67. CSS禅意花园

**原文标题**: CSS Zen Garden

**原文链接**: [https://csszengarden.com/](https://csszengarden.com/)

CSS禅意花园：展示CSS强大功能和美感的项目。它邀请设计师提交CSS样式表，以完全改变单个、不变HTML文件的视觉外观。这展示了CSS对网页样式的完全控制能力。

该倡议旨在激励设计师、鼓励参与，并作为教育资源。它强调CSS如何从相同的底层结构创建视觉上令人惊叹且多样化的设计。设计师可以下载提供的HTML和CSS文件，以试验创建自己的样式表。

鼓励参与者专注于强大的视觉设计和CSS技能，提供的文件作为起点。虽然禁止修改HTML，但设计师可以自由发挥CSS。提交的设计应主要使用CSS 1和2，以及有限的、广泛支持的CSS 3和4功能，以确保在广泛的浏览器（IE9+、Chrome、Firefox、iOS和Android）上的功能。提交的CSS必须通过验证。

贡献的设计师将受益于认可、灵感，并为Web设计社区贡献有价值的资源。提交作品应为原创艺术作品，遵守版权法，并采用独特的视觉主题。设计师保留对其图形的版权，但根据知识共享许可发布其CSS，以促进社区内的学习和共享。

---

## 68. 国会通过“移除法案”，尽管存在重大缺陷。

**原文标题**: Congress passes Take It Down act despite major flaws

**原文链接**: [https://www.eff.org/deeplinks/2025/04/congress-passes-take-it-down-act-despite-major-flaws](https://www.eff.org/deeplinks/2025/04/congress-passes-take-it-down-act-despite-major-flaws)

美国众议院通过了“撤下法案”，评论家认为该法案提供了一种审查合法言论的危险工具。该法案已在参议院获得通过，允许个人要求撤下私密或性内容，可能涵盖范围广泛的材料。

担忧主要集中在缺乏针对无理撤下请求的保障措施以及对以不准确性著称的自动化过滤器的依赖上。强制性的48小时移除时限给在线服务提供商，尤其是小型服务提供商，带来了不应有的压力，这很可能导致他们为了避免法律风险而先发制人地移除内容，即使这些内容是合法的。

评论家认为，该法律迫使平台积极监控言论，包括加密内容，从而对在线安全和隐私构成威胁。他们认为，国会应该专注于加强对非自愿图像共享受害者的现有法律保护，而不是创建容易被滥用的新的撤下机制。文章表明，该法律尽管意图良好，但存在缺陷，并可能导致审查和侵犯隐私。

---

## 69. 一家同时治疗对死亡的恐惧和身体疼痛的医院

**原文标题**: The hospital where staff treat fear of death as well as physical pain

**原文链接**: [https://www.theguardian.com/society/2025/apr/22/palliative-care-denmark-hospital-death-dying](https://www.theguardian.com/society/2025/apr/22/palliative-care-denmark-hospital-death-dying)

本文探讨了丹麦希维德夫医院126病区（临终关怀病房）的姑息治疗，重点关注对绝症患者身心痛苦的治疗。与专注于治愈的其他病区不同，该病区优先考虑缓解和舒适。文章强调了“整体疼痛”的概念，包括身体症状、焦虑和存在性痛苦。

包括 Johan Randén 医生和 Sigrid Nielsen 护士在内的医护人员，为患者及其家属提供疼痛管理和情感支持，解决他们对死亡和哀伤过程的恐惧。Randén 强调与患者公开沟通，了解他们的意愿并帮助他们为临终做好准备的重要性。Nielsen 强调他们的工作不仅限于医疗任务，还包括拥抱和关怀患者及其亲属。

文章讲述了几个患者的故事，包括死于肺癌的 René Damgaard 和患有胃癌的享乐主义者 Niels Abrahamsen。这些故事展示了该病区对个体化护理的重视，以及对生活质量的重视，即使面对死亡。该病区通过专注于改善患者剩余的生命并在临终过程中支持他们，为协助死亡提供了一种替代方案。另一位患者 Liv Simonsen 也被提及，她被诊断出患有乳腺癌。通过她的故事，它展示了提供适当疼痛管理的重要性。

---

## 70. Show HN: 神经工具，一个帮助神经多样性人群的工具集合

**原文标题**: Show HN: Neuro Tools, a collection of tools to help neurodivergent people

**原文链接**: [https://neurotools.app](https://neurotools.app)

神经工具：帮助神经多样性人士改善日常的简单工具集。这些工具旨在*辅助*现有工作流程，而非取代它们。主要功能包括：

*   **任务分解：** 将大型任务分解为更小、可操作的步骤。
*   **拖延症解决：** 帮助识别并克服拖延症障碍。
*   **激励我：** 生成个性化的动力和引言。
*   **挑战内心批评家：** 帮助重塑自我批评的想法。
*   **捕捉冲动：** 识别触发因素并提供管理冲动的策略。

用户还可以请求新的工具。一个核心原则是**隐私**：数据保留在用户设备上，核心功能不需要帐户。

神经工具提供免费增值定价模式。免费层级包含基础 AI 模型，每月 50 次请求。Pro 计划提供完全访问权限、高级 AI 模型、每月 1000 次请求、新工具的优先请求以及优先支持，价格为每月 4 美元（按年计费）。文章强调了定价结构的简洁性和透明性。

---

## 71. 亚马逊想成为卫星互联网巨头，但还有很长的路要走。

**原文标题**: Amazon Wants to Be a Satellite-Internet Powerhouse. It Has a Long Way to Go

**原文链接**: [https://www.wsj.com/business/telecom/amazon-wants-to-be-a-satellite-internet-powerhouse-it-has-a-long-way-to-go-63554c28](https://www.wsj.com/business/telecom/amazon-wants-to-be-a-satellite-internet-powerhouse-it-has-a-long-way-to-go-63554c28)

亚马逊计划通过其价值100亿美元的“库珀计划”成为卫星互联网市场的主要参与者，旨在提供全球宽带接入。然而，《华尔街日报》的文章指出，亚马逊在实现这一目标方面面临重大挑战。

虽然亚马逊已经获得了发射大量卫星的协议，但其进展落后于SpaceX的星链，后者已经拥有庞大的运营卫星群和数百万的用户群。 亚马逊尚未发射任何运营卫星，首次发射计划于今年晚些时候进行。

文章指出，建造、发射和运营数千颗卫星涉及后勤障碍。 挑战包括管理卫星轨道以避免碰撞、获得各国监管部门的批准以及建设地面基础设施以支持网络。 此外，亚马逊需要开发价格合理的客户终端并建立强大的客户支持系统。

文章还提到来自SpaceX以外的其他公司的竞争，例如Telesat以及可能进入市场的其他公司。 亚马逊的成功取决于它克服这些挑战并高效执行其雄心勃勃的计划的能力，以赶上竞争对手并在不断增长的卫星互联网市场中占据相当大的份额。 文章表明，虽然亚马逊拥有雄厚的财力，但它面临着与时间赛跑和巨大的运营障碍。

---

## 72. Show HN: Rad Type - 我们能让手柄打字变快吗？

**原文标题**: Show HN: Rad Type - Can we make gamepad typing fast?

**原文链接**: [https://www.tyleo.com/projects/rad-type](https://www.tyleo.com/projects/rad-type)

Rad Type：一种旨在提高游戏主机文本输入速度的新型游戏手柄键盘，作者认为自 NES 时代以来，这一问题几乎停滞不前。其核心概念是将字母以环状排列在两个圆形周围，通过移动摇杆并在目标点到达中间环时松开来访问。中心字符通过向内按压摇杆来访问，并设有专门的空格键和删除键。

作者详细阐述了 Rad Type 的设计动机，源于使用传统游戏手柄输入在《极限竞速7》中搜索大量汽车选择和在《Rec Room》中搜索对象库的困难。他们展示了 Rad Type 的四个迭代版本，每个版本都解决了感知到的缺点：

*   **版本 1（时钟）：** 一种钟面式排列，可容纳 26 个字母和两个中心字符。
*   **版本 2（精度）：** 在周边增加了一个更大的环，以减少因摇杆不精确造成的错误。
*   **版本 3（交替）：** 从主界面移除一半字符，通过按住肩键来访问（在触摸/鼠标上模拟为 Alt 键）。
*   **版本 4（最终）：** 仅将四个最少使用的字符移除到备用界面，旨在平衡易用性和减少肩键的使用。

作者邀请 Hacker News 上的反馈和讨论，征求对首选变体、大小写和特殊字符的想法、可用性改进、相关游戏手柄输入、Rad Type 的整体可行性及其在触摸设备上的性能的意见。

---

## 73. AI生成的代码可能是软件供应链的一场灾难

**原文标题**: AI-generated code could be a disaster for the software supply chain

**原文链接**: [https://arstechnica.com/security/2025/04/ai-generated-code-could-be-a-disaster-for-the-software-supply-chain-heres-why/](https://arstechnica.com/security/2025/04/ai-generated-code-could-be-a-disaster-for-the-software-supply-chain-heres-why/)

Dan Goodin 在 Ars Technica 上发表的文章强调了人工智能生成代码带来的重大安全风险：“软件包幻觉”，即大型语言模型 (LLM) 生成的代码会引用不存在的第三方库。一项涉及来自 16 个 LLM 的 576,000 个代码样本的研究表明，近 20% 的软件包依赖项是虚构的，从而为软件供应链攻击创造了机会。

攻击者可以通过发布具有相同虚构名称的恶意软件包来利用这一点，诱使开发人员安装它们。这种“依赖混淆”技术可以通过执行恶意代码来危及系统。研究发现，开源 LLM 比商业 LLM 更频繁地产生幻觉，并且 JavaScript 代码的幻觉率高于 Python。重要的是，这些幻觉经常被重复，这使得它们对攻击者更有价值。

研究人员强调，开发人员不应盲目信任人工智能生成的代码，必须仔细验证依赖项。文章强调，随着人工智能生成的代码越来越普遍，存在广泛的软件供应链漏洞的潜力，并敦促面对这种新兴威胁时要谨慎和警惕。

---

## 74. AEAD到底是个啥来着？

**原文标题**: What the heck is AEAD again?

**原文链接**: [https://ochagavia.nl/blog/what-the-heck-is-aead-again/](https://ochagavia.nl/blog/what-the-heck-is-aead-again/)

本文解释了带有关联数据的认证加密 (AEAD)，强调了它作为当前行业加密标准的重要性，因为它已被 TLS 1.3、QUIC 以及 Google 的 Tink 等库所采用。

作者阐明，密码学中的认证意味着确保消息的完整性和来源，防止篡改。历史上，加密和认证是分开的、容易出错的过程。AEAD 通过结合这两个步骤简化了流程，降低了误用风险和漏洞，例如 Apple iMessage 漏洞。

AEAD 还解决了认证“关联数据”的需求，即与加密消息一起发送的未加密信息，例如聊天应用程序中的会话 ID。如果不认证这些数据，攻击者可以操纵它，导致安全漏洞。AEAD 提供了一种机制来认证加密数据及其关联数据，从而防止此类攻击。

本文使用伪代码示例来说明旧的加密方法的复杂性，与 libsodium 等 AEAD 库的简化方法相比。最后，文章承认虽然强烈建议使用 AEAD，但选择正确的 AEAD 原语（如 AES256-GCM 或 ChaCha20-Poly1305）需要仔细考虑，并可能需要专家建议，并参考了 Tink 的建议和潜在的注意事项。结论是，除非有值得信赖的专家另行建议，否则 AEAD 应该是默认的加密选择。

---

## 75. Soupault (静态网站生成器) 第5版发布

**原文标题**: Soupault (static website generator) version 5 released

**原文链接**: [https://soupault.app/blog/soupault-5.0.0-release/](https://soupault.app/blog/soupault-5.0.0-release/)

Soupault 5.0.0，一款静态网站生成器，引入了旨在简化采用和提升性能的重大变更，但也可能破坏一些现有配置。主要新增功能包括内置的CommonMark兼容Markdown支持，消除了许多用户对外部处理器的需求并提高了性能。新的`element_template`小部件允许创建简单的“短代码”，无需Lua脚本，即可基于模板转换自定义HTML元素。`exec`和`preprocess_element`小部件的`os_family`选项解决了特定于操作系统的命令差异，从而为可重用蓝图启用了更具可移植性的配置。

已移除多个功能，包括`index.index_first`、`settings.process_pages_first`、单独的post-save钩子以及从post-index钩子停止页面处理的能力。`persistent_data`和`global_data`插件变量也被移除，建议使用页面或索引来存储共享数据。

一个主要的行为变更在于移除了“严格模式”，使得所有错误都将是致命的。默认情况下，整个站点索引现在可供所有页面使用，消除了对`index.index_first`的需求，但也可能在处理非常大的网站时引入内存耗尽的风险。`html_context_body`选项被更通用的`html_context`替换。 此版本还包括错误修复、新的插件功能以及特定于Windows的改进。

---

## 76. 盒中互联网

**原文标题**: Internet in a Box

**原文链接**: [https://internet-in-a-box.org/](https://internet-in-a-box.org/)

盒中互联网 (IIAB) 提供教育资源的离线访问，如同为没有可靠互联网的偏远社区提供了一个“亚历山大图书馆”。该系统利用本地Wi-Fi从中央设备向附近的设备（智能手机、平板电脑、笔记本电脑）提供内容。

IIAB是可定制的，并提供免费的、开源的软件，兼容35美元的树莓派电脑。它被许多国家使用，为连接有限的地区提供学习机会。安装简单直接，既可以在Linux PC上安装，也可以直接安装到树莓派的microSD卡上。

用户可以从包括Kiwix、OER2Go和Archive.org在内的在线图书馆中选择并下载各种语言的内容包。这允许选择相关的YouTube和Vimeo学习视频、纪录片和广播剧集。学校可以整合近40个应用程序，包括诸如Kolibri、Moodle、Nextcloud、Sugarizer或WordPress等学习管理系统。

IIAB是一个社区驱动的项目，由志愿者支持，他们与学校、诊所、图书馆和维基百科社区合作。用户可以通过添加本地照片和文物来做出贡献。支持和常见问题的解答可在FAQ.IIAB.IO上找到，技术文档和YouTube频道提供进一步的帮助。该项目始于2013年。

---

## 77. Show HN: I486SX软浮点运算器 – NetBSD 10上486SX的软件FPU模拟器

**原文标题**: Show HN: I486SX_soft_FPU – Software FPU Emulator for NetBSD 10 on 486SX

**原文链接**: [https://github.com/mezantrop/i486SX_soft_FPU](https://github.com/mezantrop/i486SX_soft_FPU)

恢复NetBSD 10.x i486SX处理器FPU (浮点单元) 模拟

---

## 78. 改变美国的群聊

**原文标题**: The group chats that changed America

**原文链接**: [https://www.semafor.com/article/04/27/2025/the-group-chats-that-changed-america](https://www.semafor.com/article/04/27/2025/the-group-chats-that-changed-america)

本·史密斯的文章探讨了私人群聊的兴起及其对美国政治的影响，尤其是在科技精英群体中。始于新冠疫情期间，这些加密对话已成为塑造公众舆论的“暗物质”，并促成了硅谷与右翼之间的新联盟。

文章重点介绍了马克·安德森作为关键人物，策划这些讨论并推广一种反主流文化观点。这些通过Signal和WhatsApp等平台进行的聊天，允许进行未经审查的辩论和达成共识，而这些共识往往与主流叙事相悖。

最初，这些群组关注的是科技行业的挑战，但逐渐转向更广泛的政治主题，包括对唐纳德·特朗普的支持。“一切安好”等旨在建立两党对话的尝试，最终因意识形态冲突而失败。文章详细描述了像克里斯·鲁弗这样的人如何有意识地利用这些聊天来“激进化科技精英”，将他们视为右翼的关键伙伴。

由埃里克·托伦伯格创立的“查塔姆议事规则”群组，体现了将中间派人物转变为共和党人的持续努力。总而言之，文章认为这些私人对话已经成为一股强大的力量，影响着美国的公共 discourse 和政治立场。

---

## 79. Show HN: Autarkie – 使用 Rust 宏实现的即时语法模糊测试

**原文标题**: Show HN: Autarkie – Instant grammar fuzzing using Rust macros

**原文链接**: [https://github.com/R9295/autarkie](https://github.com/R9295/autarkie)

Autarkie：基于语法的原生模糊测试器

---

## 80. 诺尔的《编程作为理论构建》以及大型语言模型取代人类程序员

**原文标题**: Naur's "Programming as Theory Building" and LLMs replacing human programmers

**原文链接**: [https://ratfactor.com/cards/naur-vs-llms](https://ratfactor.com/cards/naur-vs-llms)

本文论证了大型语言模型（LLMs）无法取代人类程序员的观点，借鉴了Peter Naur的“编程即理论构建”和Gilbert Ryle的“理论”概念。作者认为，LLMs缺乏发展Ryleian理论的根本能力，而这种能力对于有效的编程至关重要。

核心论点是，在此语境下，“理论”不仅仅是解释或阐述程序的能力（LLMs可能可以模拟），而是通过积极构建和使用程序所获得的知识。Ryle的“开辟道路”与“使用道路”的类比突出了这种差异：LLMs可以“使用”现有的“道路”（现有代码），但它们没有进行“开辟道路”（理论发展）。

作者强调，LLMs通过“训练”现有代码，本质上是吸收理论构建的成果，但这并不等同于拥有底层的理论本身。Naur的论文强调，理解大型程序需要积极地使用它，并拥有创建它的程序员所掌握的特定知识。源代码或文档都无法取代这种“智慧”。

文章进一步论证，编程不仅仅是文本生成，而是构建和维护程序的“理论”。认为LLMs可以编写软件意味着错误地将编程视为仅仅是源代码的生产。因此，LLMs需要发展真正的“理论”，否则Naur对编程的理解就是错误的，而作者认为两者都不会发生。

---

## 81. 2025年4月28日葡萄牙/西班牙停电如何影响互联网流量

**原文标题**: How the April 28, 2025 power outage in Portugal/Spain impacted Internet traffic

**原文链接**: [https://blog.cloudflare.com/how-power-outage-in-portugal-spain-impacted-internet/](https://blog.cloudflare.com/how-power-outage-in-portugal-spain-impacted-internet/)

2025年4月28日，葡萄牙和西班牙发生大规模停电，严重影响互联网流量和连接。此次停电归因于西班牙电网故障，导致交通中断、商业停业和一般服务中断。虽然具体原因仍在争论中，但Cloudflare网络的广泛性使其能够详细观察停电的影响。

在葡萄牙，互联网流量立即骤降50%，并在五个小时内降至前一周水平的90%以下。DNS解析器请求也大幅下降。NOS、沃达丰、MEO和NOWO等主要ISP的流量迅速消失。然而，由于用户寻求信息，MEO-MOVEL的移动流量最初出现激增。下载速度从40 Mbps降至15 Mbps，而延迟从20 ms增加至50 ms。网络基础设施受到影响，宣布的IP地址空间有所下降。

西班牙经历了类似的影响，互联网流量最初下降60%，最终降至前一周水平的80%以下。DNS解析器请求也下降。西班牙排名前五的ASN流量大幅下降，但某些地区出现了部分流量恢复。下载速度从35 Mbps降至19 Mbps，延迟从22 ms升至40 ms。与葡萄牙一样，西班牙也面临着宣布的IP地址空间减少。

据报道，法国和安道尔的部分地区受到影响，但对互联网流量的影响微乎其微。摩洛哥的Orange Maroc报告称，由于西班牙和葡萄牙的停电，该公司的业务受到干扰。随着西班牙开始恢复供电，预计互联网流量和相关指标将逐步恢复。

---

## 82. 观看o3模型为保罗·墨菲的二步杀而绞尽脑汁

**原文标题**: Watching o3 model sweat over a Paul Morphy mate-in-2

**原文链接**: [https://alexop.dev/posts/how-03-model-tries-chess-puzzle/](https://alexop.dev/posts/how-03-model-tries-chess-puzzle/)

OpenAI的o3模型解莫菲“两步杀”棋局：一次令人惊叹的类人尝试

文章详细介绍了OpenAI的o3模型尝试解决保罗·墨菲“两步杀”棋局的过程。作者强调了该模型在整个过程中令人惊讶的类人行为。

最初，o3仔细地分析并从图像中重建了棋盘。然后，它测试了显而易见的走法，遇到疑问并在失败时自我纠正。由于缺少模块，它尝试使用Python编写一个国际象棋引擎（失败了），甚至试图通过逐像素图像分析来推断棋子位置，表现出顽固的坚持。

当时间耗尽（大约8分钟）时，o3转而使用必应搜索解决方案。它找到了一个讨论该棋局的国际象棋论坛，并在重新检查和理解了建议的走法（Ra6）后，宣布了解决方案。

作者发现这个过程令人着迷，因为它表明o3不仅仅是提供答案；它会像人类一样进行推理、挣扎、切换工具、自我纠正，甚至“作弊”。这突出了模型在解决问题方面的优势，但也揭示了它需要外部支持才能找到解决复杂难题的创造性方案。文章最后质疑了大型语言模型是否具备真正的创造力。

---

## 83. Linux内存管理器

**原文标题**: The Linux Memory Manager

**原文链接**: [https://nostarch.com/linux-memory-manager](https://nostarch.com/linux-memory-manager)

本文档《Linux内存管理器》是一份全面指南，旨在帮助读者理解Linux操作系统中内存管理的工作原理。目录概述了对内存管理的理论基础和实践方面的深入研究。

本书从引言开始，然后深入探讨物理内存，这是所有其他内存管理概念的基础。接着，它将探讨虚拟内存，这是一种至关重要的抽象，允许进程独立且高效地访问内存。接下来会检查进程内存，详细说明如何为各个进程分配和管理其内存空间。

本文还涵盖了内存映射，这是一种强大的技术，允许将文件和其他资源直接映射到进程的地址空间中。解释了页面错误，即虚拟内存系统处理对当前不在物理内存中的页面的访问的机制。深入探讨了诸如反向映射之类的相关概念，这些概念跟踪映射物理页面的虚拟地址。

此外，该文档还讨论了如何操作用户空间内存，从而深入了解应用程序如何与内存管理器交互。涵盖了页面缓存、回写机制和内存回收。最后，本书解释了交换内存和臭名昭著的内存不足 (OOM) 杀手的作用，最后总结了内存管理的实际考虑因素。抢先体验版 PDF 包括目录中以红色突出显示的章节，但整本书承诺对 Linux 的内存管理系统有完整的理解。

---

## 84. 编程语言应该具备树遍历原语。

**原文标题**: Programming languages should have a tree traversal primitive

**原文链接**: [https://blog.tylerglaiel.com/p/programming-languages-should-have](https://blog.tylerglaiel.com/p/programming-languages-should-have)

无法访问文章链接。

---

## 85. 管风琴的工作原理 (2020)

**原文标题**: How a Pipe Organ Works (2020)

**原文链接**: [https://www.pipedreams.org/page/how-a-pipe-organ-works](https://www.pipedreams.org/page/how-a-pipe-organ-works)

管风琴的工作原理：本文解释了这种复杂乐器的基本机械原理。它将管风琴比作一个“大型哨子盒”，强调每个音管对应一个特定的音符和音色。

管风琴的核心是风箱，一个由风箱或鼓风机提供压缩空气的空腔。管风琴控制台上的每个“音栓”控制着一组具有特定音色的音管。拉动音栓会激活滑块，使该组音管可以发声。

然而，只有在按下琴键时才会产生声音。键盘与位于风箱内的称为阀门的气阀相连。按下琴键会打开相应的气阀，使压缩空气流过相关的音管，从而产生声音。因此，即使已经启动音栓，在按下琴键之前也不会发出声音。

本文还强调了每个管风琴的独特性，将其与批量生产的乐器（如长号或小提琴）进行对比。管风琴是定制的，会考虑声音的数量和类型、房间的音响效果、乐器的视觉设计以及购买者的预算等因素。文章末尾还提供了一个链接和资源列表，以获取更详细的信息。

---

## 86. 使用 Power Macintosh 设置时间服务器

**原文标题**: Setting up a timekeeping server with a Power Macintosh

**原文链接**: [https://whatroute.net/timekeeping.html#serversetup](https://whatroute.net/timekeeping.html#serversetup)

使用Power Macintosh G4和Debian Linux搭建高精度授时服务器：利用带PPS同步的GPS接收器

---

## 87. 你不懂Git – Edward Thomson – NDC伦敦2025 [视频]

**原文标题**: You Don't Know Git – Edward Thomson – NDC London 2025 [video]

**原文链接**: [https://www.youtube.com/watch?v=DZI0Zl-1JqQ](https://www.youtube.com/watch?v=DZI0Zl-1JqQ)

此条目描述了一个名为“You Don't Know Git – Edward Thomson – NDC London 2025”的YouTube视频。这表明爱德华·汤姆森在2025年伦敦NDC会议上做了一场关于版本控制系统Git的演讲。

其余内容是样板式的YouTube信息：与平台相关的标准链接和版权声明。它没有提供关于Git演示实际内容的任何信息。

因此，主要的结论是有一个爱德华·汤姆森在2025年伦敦NDC会议上关于Git的演讲的YouTube视频，但所提供的信息没有提供关于演示本身涵盖的具体主题或论点的任何见解。你需要观看视频才能理解其内容。

---

## 88. 甲骨文工程师导致美国医院软件中断五天

**原文标题**: Oracle engineers caused five days software outage at U.S. hospitals

**原文链接**: [https://www.cnbc.com/2025/04/28/oracle-engineers-caused-days-long-software-outage-at-us-hospitals.html](https://www.cnbc.com/2025/04/28/oracle-engineers-caused-days-long-software-outage-at-us-hospitals.html)

甲骨文工程师失误导致多家社区健康系统(CHS)医院软件中断五天，迫使其恢复纸质病人记录。此次中断始于4月23日，源于工程师在维护甲骨文健康（该公司电子健康记录(EHR)系统）时删除了关键存储。行业出版物Becker's Hospital Review报道称，有45家医院受到影响。

在14个州运营72家医院的CHS表示，尽管受到干扰，但患者护理得以维持，没有“重大影响”。该公司强调，此次中断并非网络攻击，受影响的医院正在恢复全部功能。

此前，甲骨文的联邦EHR系统曾发生过一次全国性中断，并且该公司为退伍军人事务部推出的EHR系统也面临诸多挑战，该系统一直受到安全问题和部署暂停的困扰。甲骨文于2022年以283亿美元收购了EHR供应商Cerner，成为EHR市场的主要参与者。甲骨文尚未立即回复CNBC的置评请求。

---

## 89. 令人着迷的日式木工几何榫卯

**原文标题**: Mesmerizing Interlocking Geometric Patterns Produced with Japanese Woodworking

**原文链接**: [https://www.smithsonianmag.com/smithsonian-institution/see-the-mesmerizing-interlocking-geometric-patterns-produced-with-this-ancient-japanese-woodworking-technique-180986494/](https://www.smithsonianmag.com/smithsonian-institution/see-the-mesmerizing-interlocking-geometric-patterns-produced-with-this-ancient-japanese-woodworking-technique-180986494/)

本文探讨了复杂的日本木工技术——组子细工，重点介绍了它的历史、现代应用以及当代艺术家的作品。组子细工起源于公元538年至710年间的日本，它需要精确地切割和互锁薄木条，以创建重复的几何图案，传统上用于屏风和家具镶板。

本文重点介绍了即将于华盛顿特区史密森尼工艺品展上展出的组子细工匠人David Gootnick。Gootnick使用阿拉斯加雪松，精心将其铣削成薄条，并精确切割角度以创建类似格子状的设计。虽然植根于六边形和等边三角形等传统图案，但Gootnick融入了他自己的当代变化，使用不同的木材类型进行颜色对比，并将设计安装在色彩鲜艳的布料上。

另一位在工艺品展上展出的艺术家Michael Jury将组子细工镶板融入到他受Shaker和丹麦风格启发的家具中。他利用椴木来创建诸如asa-no-ha（麻叶）之类的传统图案，并在诸如带有momigami纸背衬的推拉门餐具柜等作品中展示了它。

本文强调了组子细工所需的精确度和技巧，Gootnick指出了他随着时间的推移所做的改进。虽然传统上不使用胶水进行组装，但Gootnick会使用少量胶水以确保其作品的寿命。最终，本文赞颂了组子细工是传统艺术和当代创造力的融合。

---

## 90. 法医粉丝

**原文标题**: Forensic Fandom

**原文链接**: [https://exiledfan.substack.com/p/introducing-forensic-fandom](https://exiledfan.substack.com/p/introducing-forensic-fandom)

无法访问文章链接。

---

## 91. 展示HN：每日越狱 – Prompt工程师的文字游戏

**原文标题**: Show HN: Daily Jailbreak – Prompt Engineer's Wordle

**原文链接**: [https://www.vaultbreak.ai/daily-jailbreak](https://www.vaultbreak.ai/daily-jailbreak)

无法访问文章链接。

---

## 92. 德国最大海上风电场首台15兆瓦巨型风机已启动。

**原文标题**: The first giant 15 MW turbine is up at Germany's largest offshore wind farm

**原文链接**: [https://electrek.co/2025/04/28/the-first-giant-15-mw-turbine-is-up-at-germanys-largest-offshore-wind-farm/](https://electrek.co/2025/04/28/the-first-giant-15-mw-turbine-is-up-at-germanys-largest-offshore-wind-farm/)

德国最大海上风电场EnBW He Dreiht安装首台15兆瓦巨型风机。该风电场位于北海。该项目标志着维斯塔斯巨型15兆瓦风机在全球首次安装，每次旋转可为四个家庭供电一天。

建成后，He Dreiht将包含64台风机，产生960兆瓦的清洁能源，足以为约110万户家庭供电。值得注意的是，该项目在没有政府补贴的情况下建造。EnBW的目标是到2030年将其可再生能源产量大幅增加到10吉瓦以上。

安装过程包括使用Wind Orca号船将风机部件从丹麦埃斯比约运到施工现场。64个基础已预先安装在海床上。在高峰期，有超过500名工人和60艘船参与建设。

安联资本合伙公司、AIP和挪威银行投资管理公司组成的财团拥有该项目49.9%的股份。该风电场位于博尔库姆西北约85公里，黑尔戈兰岛以西110公里。

---

## 93. 尊敬的“安全研究人员”

**原文标题**: Dear "Security Researchers"

**原文链接**: [https://ftp.bit.nl/pub/debian/](https://ftp.bit.nl/pub/debian/)

这是一位公共Debian镜像服务器所有者向“安全研究人员”发出的消息。该服务器是一个公共服务，托管开源软件，特别是Debian档案。所有者明确要求安全研究人员**不要**根据负责任的披露政策报告在服务器上发现的任何内容。他们强调服务器不包含任何敏感信息，并且不会对其公司构成任何安全威胁。数据包括Debian发行版（Buster、Bullseye、Bookworm、Trixie和Sid）以及文档、索引和实验性软件包。有关安装、升级、CD和镜像的信息以链接形式提供。旧版本可在archive.debian.org上找到。

---

## 94. 亚马逊工人发表科幻故事集，旨在“重塑未来创造”

**原文标题**: To 'Reclaim Future-Making', Amazon Workers Published Collection of SciFi Stories

**原文链接**: [https://afteramazon.world/](https://afteramazon.world/)

亚马逊之后的未来

---

## 95. 科技创业公司里，联合创始人比他们自认为的价值要低。

**原文标题**: Business co-founders in tech startups are less valuable than they think

**原文链接**: [https://verdikapuku.com/posts/business-founders-are-less-valuable-than-they-think/](https://verdikapuku.com/posts/business-founders-are-less-valuable-than-they-think/)

本文认为，科技初创企业中不具备技术背景的业务创始人通常会高估自身的价值，尤其是在难以找到技术合伙人的情况下。作者指出，许多业务创始人往往过分看重最初的想法，并且常常表现出自负的姿态，这使得他们对技术精湛的工程师缺乏吸引力。

核心问题在于对想法本身的过度强调，而非对执行的重视，而执行需要工程师的技术专长。作者强调，构建和执行产品的艰苦工作才是真正价值所在。

然而，本文并非完全否定业务创始人的作用。文章建议他们专注于自身的优势，特别是客户获取和关系建立。他们不应仅仅依赖想法，而应该在产品构建之前，通过产生对产品的浓厚兴趣来证明自己的价值，例如为B2C企业争取庞大的预订名单，或为B2B企业争取意向书。

关键在于，业务创始人的价值在于推动业务发展，特别是通过建立强大的网络，并展示获取客户和投资者的动力。这创造了一种难以忽视的有形资产，并将他们定位为对初创企业成功有价值的贡献者。通过专注于自身独特的优势，并展示其创造需求的能力，业务创始人可以成为不可或缺的合作伙伴，并大大增加他们找到熟练的技术合伙人的机会。

---

## 96. 展示一下：我做了一个免费的、基于网页的Screen Studio替代品

**原文标题**: Show HN: I made a web-based, free alternative to Screen Studio

**原文链接**: [https://www.screenrecorder.me](https://www.screenrecorder.me)

“Show HN”：Screenrecorder.Me，一款免费的在线屏幕录制工具，替代Screen Studio。用户无需登录即可直接在浏览器中创建产品演示和教程。

主要功能包括：

*   **屏幕录制：** 捕捉任何屏幕活动。
*   **壁纸定制：** 从预设壁纸中选择或生成随机壁纸。轻松调整内边距和模糊。
*   **屏幕样式：** 自定义圆角、阴影、边框和颜色，打造专业外观。
*   **摄像头特效：** 调整摄像头外观，提供形状、位置、边框、阴影和颜色选项。
*   **动画效果：** 实现流畅动画，可选择自动鼠标跟随或手动定位，并采用基于物理的运动效果。

该平台旨在提供一种快速简便的方式来捕获、编辑和分享屏幕录像，使其成为创建教程和演示的理想选择。它强调其基于浏览器的特性以及无需登录的特性，从而突出其可访问性。

---

## 97. 用 Markdown 制作演示文稿

**原文标题**: Presentation Slides with Markdown

**原文链接**: [https://sli.dev](https://sli.dev)

本文介绍Slidev，一款专为开发者设计的演示文稿工具。其核心理念是让开发者能够使用他们熟悉的工作流程和工具来创建演示文稿。“开始使用”链接表明本文将指导用户如何开始使用Slidev。重复出现的“为什么”可能暗示了选择Slidev而非传统演示软件的理由或好处。

本质上，本文推广Slidev作为一种对开发者友好的演示文稿创建方案，暗示它提供了针对其技术背景和首选方法的优势。深入阅读可能会揭示Slidev独特的具体特性和优势，例如它与代码编辑器、版本控制系统的潜在集成，或者使用Markdown进行内容创作。

---

## 98. 一行代码如何让你的iPhone变砖

**原文标题**: How a single line of code could brick your iPhone

**原文链接**: [https://rambo.codes/posts/2025-04-24-how-a-single-line-of-code-could-brick-your-iphone](https://rambo.codes/posts/2025-04-24-how-a-single-line-of-code-could-brick-your-iphone)

该文章详细描述了iOS中的一个漏洞，该漏洞允许使用达尔文通知（一种底层进程间通信机制）仅用一行代码就可能使iPhone变砖。作者发现，由于任何沙盒应用都可以发送达尔文通知，而无需特殊权限或验证发送者，因此恶意应用可以利用系统级操作。

概念验证“EvilNotify”演示了触发各种系统范围效果的能力，包括显示虚假的“液体检测”和连接状态，阻止系统手势，强制使用蜂窝数据，锁定屏幕，甚至模拟“恢复进行中”模式。后者通过`notify_post("com.apple.MobileSync.BackupAgent.RestoreStarted")`触发，会将设备强制进入需要重启的循环。

“VeryEvilNotify”应用程序通过一个配置为崩溃的小部件扩展，重复触发“恢复进行中”状态，从而将此漏洞升级为拒绝服务攻击。崩溃的扩展程序会自动重启，持续发布恶意通知，从而有效地软砖设备。

作者向苹果报告了该漏洞，苹果在iOS 18.3 (CVE-2025-24091) 中解决了该问题。缓解措施包括要求发送敏感达尔文通知时使用受限制的权利，特别是通过前缀权利`com.apple.private.darwin-notification.restrict-post.<notification>`。这强制验证发布过程，防止未经授权的应用程序操纵关键系统功能。作者因发现该漏洞获得了 17,500 美元的漏洞赏金。

---

## 99. Show HN: 开发中的 Common Lisp 实现，支持 ASDF

**原文标题**: Show HN: A Common Lisp implementation in development, supports ASDF

**原文链接**: [https://savannah.nongnu.org/p/alisp](https://savannah.nongnu.org/p/alisp)

这个“Show HN”帖子介绍了`alisp`，一个由Andrea Monaco开发的Common Lisp实现。它是一个托管在Savannah上的非GNU项目，目前是一个解释器，并计划进行编译。该实现旨在符合Common Lisp标准，使用C89、GNU readline（可选）和GNU mp作为外部库。

`alisp`拥有广泛的Common Lisp支持，`test.pl`脚本展示了它的功能。一个关键特性是其对程序员友好的方法，包括一个基本的分析器和一个带有单步调试的调试器，这在其他免费的Common Lisp实现中往往是缺乏的。

该项目是一个单人项目，欢迎提交错误报告和建议，但不接受补丁。它以GPL版本3或更高版本发布，并感谢捐赠。最新版本是1.1，之前发布的版本有1.0、0.999和0.99，详细说明了在LOOP、CLOS、路径名、调试、编译等方面的改进。

Savannah项目页面提供了下载、Git仓库、Bug追踪器和任务管理器的访问入口。作者建议克隆Git仓库以获取最新版本。相关文档可以在README和NOTES文件中找到。

---

## 100. 解锁 Ractors：Object_id

**原文标题**: Unlocking Ractors: Object_id

**原文链接**: [https://byroot.github.io/ruby/performance/2025/04/26/unlocking-ractors-object-id.html](https://byroot.github.io/ruby/performance/2025/04/26/unlocking-ractors-object-id.html)

本文深入探讨了Ruby中`#object_id`方法的性能挑战，尤其是在Ractors（Ruby的并发特性）的背景下。 历史上，`#object_id`只是简单地返回一个派生的内存地址，但这在Ruby 2.7中由于GC压缩（会在内存中移动对象）而变得有问题。 这导致引入了两个全局哈希表来存储对象ID，确保了稳定性，但也增加了内存使用和执行成本。

Ractors的引入加剧了这个问题，因为对这些表的并发访问需要一个全局VM锁，从而产生了一个争用点。 作者概述了他们优化此问题的努力。 第一步是仅在需要时才创建`ID_TO_OBJ_TABLE`（由罕见的`ObjectSpace._id2ref`使用），从而减少内存占用和GC工作。 他们还引入了一个新的`SHAPE_OBJ_ID`，用于将对象id存储在对象现有的Shape结构中。 其目的是允许在不锁定整个VM的情况下添加对象id，方法是将id直接存储在对象中。

---

