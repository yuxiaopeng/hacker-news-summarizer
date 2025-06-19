# Hacker News 热门文章摘要 (2025-06-19)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 曲面折痕折纸雕塑

**原文标题**: Curved-Crease Origami Sculptures

**原文链接**: [https://erikdemaine.org/curved/](https://erikdemaine.org/curved/)

埃里克和马丁·德曼创作弯曲折痕的折纸雕塑，探索纸张沿弯曲折痕折叠时呈现的自然平衡形态。这一领域尚未被充分理解，他们正在研究这种自折叠折纸类型中可能的形状，并设想其在可展开结构、制造和自组装领域的应用。

他们的作品将平面纸张转化为漩涡状的表面，创造出唤起生命感的雕塑。本页列出了他们从2008年到2024年的多个系列作品，包括“自由系列 (2024)”、“与文字的邂逅 (2024)”、“盲文系列 (2023)”等。这些系列曾在史密森尼美国艺术博物馆、纽约现代艺术博物馆以及众多大学美术馆等场所展出。

本页还简要介绍了弯曲折纸雕塑出人意料的悠久历史，追溯到20世纪20年代的包豪斯，并提供了一个链接，可以查看关于该主题更详细的历史。

---

## 2. Andrej Karpathy：人工智能时代的软件 [视频]

**原文标题**: Andrej Karpathy: Software in the era of AI [video]

**原文链接**: [https://www.youtube.com/watch?v=LCEmiRjPEtQ](https://www.youtube.com/watch?v=LCEmiRjPEtQ)

所提供的“内容”似乎是标准的YouTube页脚，而不是Andrej Karpathy的视频“人工智能时代的软件”的文字稿或摘要。因此，仅凭此信息无法概括视频的主要观点。

要获得摘要，需要：

* **视频本身的文字稿或摘要：** 这将提供Karpathy演讲的实际内容。
* **关于视频描述或相关文章的信息：** 这些资源可能会提供关于视频主要主题的线索。

在无法访问视频实际内容的情况下，我们只能说它可能讨论了人工智能对软件开发的影响，可能涵盖的主题包括：

* **人工智能辅助编码工具：** 人工智能如何帮助开发者更快、更高效地编写代码。
* **人工智能驱动的软件测试和调试：** 使用人工智能自动化测试和调试过程。
* **软件工程师角色的转变：** 随着人工智能在开发过程中变得越来越普遍，软件工程师的角色可能会如何演变。
* **软件架构和设计的未来：** 人工智能将如何影响软件的设计和架构方式。

简而言之，所提供的信息不足以提供对Andrej Karpathy视频的有意义的摘要。

---

## 3. Posit浮点数：细长三角形和其他技巧 (2019)

**原文标题**: Posit floating point numbers: thin triangles and other tricks (2019)

**原文链接**: [http://marc-b-reynolds.github.io/math/2019/02/06/Posit1.html](http://marc-b-reynolds.github.io/math/2019/02/06/Posit1.html)

本文批判了将Posit作为IEEE binary32浮点数的直接替代品，尤其是在通用计算中的应用。作者以“细长三角形”问题为例，论证了虽然Posit有时能提供更精确的结果，但其锥形精度分布并不能保证在所有情况下都表现更优。

作者强调，IEEE binary32尽管只有24位精度，有时也会在简单计算中失败。然而，他们也指出，仅基于十进制数字精度的比较具有误导性。文章强调，IEEE的设计优先考虑尺度不变性，而Posit则专注于接近于1的值的高精度，牺牲了远离该范围的精度。

作者引用了Trefethen的观点，即科学计算很少需要双精度浮点数的全部精度，认为建模和截断误差通常比舍入误差更为重要。文章倡导理解浮点模型的底层原理，而不是将其视为黑盒，并敦促从业者了解不同浮点格式之间的权衡。

文章揭示了“细长三角形”技巧之所以有效，是因为在这种特定情况下，IEEE数值必须进行舍入，而Posit则不需要。作者最后指出，Posit和IEEE存储有限值的方式不同，由于其特殊细节，在一般范围内比较两者并非明智之举。

---

## 4. Show HN: Claude 代码使用监控器 – 实时追踪，避免用量限制

**原文标题**: Show HN: Claude Code Usage Monitor – real-time tracker to dodge usage cut-offs

**原文链接**: [https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor)

本文是一篇“Show HN”帖子，介绍 Claude 代码使用监控器，这是一个实时终端工具，旨在帮助用户跟踪和管理他们的 Claude AI Token 消耗，以避免使用中断。它提供诸如 3 秒刷新率的实时监控、Token 和时间的视觉进度条、Token 耗尽的智能预测、自动计划检测以及可定制的调度等功能。

该帖子详细介绍了安装说明，包括快速启动方法和使用虚拟环境进行依赖隔离的推荐生产设置。它解释了如何使用具有不同配置选项的监控器，例如指定 Claude 计划（Pro、Max5、Max20 或自动检测）、自定义重置时间和时区。

它阐述了 Claude 的会话系统，该系统在 5 小时滚动窗口上运行，以及监控器如何计算消耗率并预测 Token 耗尽。本文还涵盖了常见的使用场景，例如早班开发者、夜猫子和国际用户，提供示例配置和最佳实践以实现最佳使用。最后，它鼓励用户反馈，提供联系方式，并提及未来的开发计划、贡献指南和故障排除部分。它感谢 @ryoppippi 的 ccusage 的贡献，并邀请用户为该存储库加星标。

---

## 5. 我们只需测量即可

**原文标题**: We Can Just Measure Things

**原文链接**: [https://lucumr.pocoo.org/2025/6/17/measuring/](https://lucumr.pocoo.org/2025/6/17/measuring/)

在他的文章《我们只需衡量事物》中，Armin Ronacher探讨了如何利用编程代理来客观评估代码库和工具的开发者体验。由于软件开发中常见的工具不足和文档质量差的问题，Ronacher感到沮丧，他认为代理提供了一种衡量代码质量和项目健康状况的方法，而这些方法对于人类开发者来说是困难的，甚至是无法实现的。

他建议使用代理来评估诸如测试覆盖率、错误报告、生态系统稳定性以及是否存在多余抽象等因素。 通过观察代理在与代码交互时的性能和挫败感，开发人员可以深入了解其项目的可用性和可维护性。 这种方法消除了情绪偏差，并允许进行可重复的客观实验。

Ronacher强调了良好开发环境的重要性，强调代理需要本地访问数据库和Docker等资源，而不是仅仅依赖于CI环境。 他认为，使代码库对代理友好的因素——良好的文档、清晰的错误消息和稳定的API——对人类开发人员也同样有益。

最终，Ronacher认为，使用代理来评估开发者体验可以带来更好的技术选择和更高质量的库，因为用户现在可以客观地衡量他们的挫败感。 他最后指出，他的代理和他一样，对Xcode等工具表达了挫败感，这证明了对开发者体验进行可衡量反馈的潜力。

---

## 6. 我现在大概是个理性主义者了

**原文标题**: Guess I'm a Rationalist Now

**原文链接**: [https://scottaaronson.blog/?p=8908](https://scottaaronson.blog/?p=8908)

在这篇博文中，Scott Aaronson回顾了他在理性主义博客大会LessOnline的经历，并宣布经过多年犹豫，他决定将自己定义为一名理性主义者。他将这次会议描述为一个充满活力的对话中心，与会者多元，包括理性主义社区的杰出人物。

Aaronson概述了他过去的保留意见，主要是社群对人工智能风险的关注，他现在认为这种关注是先见的，以及他自己与通常更年轻、更具实验性的理性主义者之间的文化差异。然而，他指出，这个社群已经成熟，许多成员现在有了家庭，并专注于建设更美好的未来。他还驳斥了关于该社群类似于邪教的担忧，认为它更像是具有共同信仰的知识社团。

他之前犹豫的主要原因是害怕来自学术界同事和其他人的评判。他现在感到可以坦然接受这个标签，并不理会“嘲笑者”的批评。他为理性主义社群辩护，反对其是极右或仇视女性者的指控，并引用了会议中的例子来反驳这些说法。最终，他强调，接受理性主义者的标签并不会改变他的核心信念，而是反映了他找到了一个重视他所能提供的价值的社群。最后，他宣布了一些无关的消息，关于他即将到来的旅行，他领导的哲学和理论计算机科学会议，以及对理论计算机科学奖项的提名呼吁。

---

## 7. Flowspace (YC S17) 招聘软件工程师

**原文标题**: Flowspace (YC S17) Is Hiring Software Engineers

**原文链接**: [https://flowspace.applytojob.com/apply/6oDtY2q6E9/Software-Engineer-II](https://flowspace.applytojob.com/apply/6oDtY2q6E9/Software-Engineer-II)

无法访问文章链接。

---

## 8. 从LLM到AI Agent：AI系统开发背后的真正旅程是什么？

**原文标题**: From LLM to AI Agent: What's the Real Journey Behind AI System Development?

**原文链接**: [https://www.codelink.io/blog/post/ai-system-development-llm-rag-ai-workflow-agent](https://www.codelink.io/blog/post/ai-system-development-llm-rag-ai-workflow-agent)

本文探讨了人工智能系统开发的演进过程，从基础的大型语言模型（LLMs）发展到更复杂的AI Agent，并强调并非每个AI系统都需要是完全自主的Agent。文章着重强调了基于具体问题选择正确架构的重要性。

文章概述了以下关键阶段：

*   **纯LLMs：** 擅长利用其现有知识，但缺乏实时信息和外部背景。
*   **RAG（检索增强生成）：** 通过外部数据增强LLMs，提高准确性、精确性和实时信息。
*   **工具使用和AI工作流：** 通过将LLMs连接到API来实现业务流程自动化，适用于定义明确、一致的任务。
*   **AI Agent：** 提供独立的推理和决策能力，可自动执行规划和行动排序。

文章以简历筛选应用程序为例，展示了每个阶段如何增加复杂性和能力。纯LLM可以根据其现有知识对简历进行分类，RAG通过检索公司特定数据来提高准确性，AI工作流使用外部API自动执行整个筛选过程，而AI Agent可以独立管理整个招聘过程。

主要结论是，像RAG或工作流这样更简单的解决方案通常是足够的，并且比AI Agent更具成本效益，尤其是在标准和行动明确的情况下。文章还强调需要优先考虑可靠性而非单纯的能力，建议使用沙箱环境、持续测试和防护栏来解决LLMs在将AI系统部署到生产环境时的非确定性问题。

---

## 9. Show HN: Unregistry – 无需镜像仓库，直接“docker push”到服务器

**原文标题**: Show HN: Unregistry – “docker push” directly to servers without a registry

**原文链接**: [https://github.com/psviderski/unregistry](https://github.com/psviderski/unregistry)

Unregistry 引入 `docker pussh`，它允许通过 SSH 直接将 Docker 镜像推送到远程服务器，无需中央镜像仓库。它通过提供一个简单高效的替代方案来解决繁琐的镜像传输问题，替代方案包括 Docker Hub、自托管镜像仓库和 `docker save/load`。`docker pussh` 只传输缺失的镜像层，类似于 rsync，使其更快，资源消耗更少。

该过程涉及建立 SSH 隧道，在远程服务器上启动一个临时的 Unregistry 容器，转发端口，将镜像推送到 Unregistry，然后停止容器。安装过程简单明了，可以通过 Homebrew (macOS/Linux) 或直接下载安装。该工具需要在本地安装带有插件支持的 Docker CLI 和 OpenSSH 客户端，以及在远程安装具有 SSH 访问权限的 Docker。

用例包括部署到生产服务器、简化 CI/CD 流程，以及在家庭实验室/气隙环境分发镜像。高级用法包括将 Unregistry 作为本地镜像仓库独立运行，以及通过 SSH 配置文件使用自定义 SSH 选项。该工具建议在远程 Docker 守护程序上使用 containerd 镜像存储以获得最佳性能。

---

## 10. 研究人员现在正从空气中吸取DNA

**原文标题**: Researchers are now vacuuming DNA from the air

**原文链接**: [https://www.sciencedaily.com/releases/2025/06/250603114822.htm](https://www.sciencedaily.com/releases/2025/06/250603114822.htm)

佛罗里达大学的研究人员开发了一种分析从空气中收集的环境DNA（eDNA）的方法，揭示了其追踪各种生物和物质的潜力，从野生动物到病毒，甚至非法药物。科学家们利用简单的空气过滤器，可以捕获漂浮在空气中的DNA片段，并破译它们以识别一个区域中存在的物种，监测病原体，并检测过敏原。

一项在都柏林进行的研究发现空气中含有大麻、罂粟和迷幻蘑菇的DNA痕迹。该技术还被用于识别佛罗里达森林中短尾猫和蜘蛛的来源。这种非侵入性方法提供了一种在不直接干扰物种的情况下研究它们的方式，并能为保护工作提供关键信息。

该过程快速高效，使得一名研究人员可以使用经济实惠的设备和基于云的软件，在一天内分析多种物种的DNA。这使得世界各地的科学家更容易进行高级环境研究。

然而，研究人员强调，由于存在获取敏感人类遗传数据的可能性，因此需要制定道德准则。这项技术的发展标志着环境监测和问题解决方面的重大进步。

---

## 11. Show HN：一个用 Rust 和 x86 汇编写的类 DOS 操作系统

**原文标题**: Show HN: A DOS-like hobby OS written in Rust and x86 assembly

**原文链接**: [https://github.com/krustowski/rou2exOS](https://github.com/krustowski/rou2exOS)

“Show HN”：rou2exOS Rusted Edition，一个用 Rust 和 x86 汇编写的类 DOS 业余操作系统。它是原始 RoureXOS 项目的重写版本。该帖子提供了关于如何使用 QEMU 模拟器中的 ISO 镜像构建和运行该操作系统的说明，以及如何在裸机硬件上进行测试。

可以使用 `make init`、`make build` 和 `make run_iso` 构建和运行该操作系统。该帖子还描述了使用 `cargo bootimage` 和 `make run` (并调整 `Cargo.toml`) 来运行内核的另一种方法。

该帖子还介绍了如何测试 ICMP/SLIP 功能。这包括在 QEMU 中运行内核以获取 pty 号码，然后使用 `slattach` 和 `ifconfig` 创建 SLIP 接口。 `tcpdump` 可用于捕获通过接口发送的数据包。该帖子包含了监听 SLIP 数据包、配置 `sl0` 接口以及使用 `tcpdump` 捕获数据包的命令。

---

## 12. 寻找失效的网站

**原文标题**: Finding Dead Websites

**原文链接**: [https://www.marginalia.nu/log/a_122_dead_websites/](https://www.marginalia.nu/log/a_122_dead_websites/)

本文详细介绍了Marginalia搜索引擎中一个名为“ping-process”的系统，该系统用于检测失效网站和重大变更，包括所有权转移和域名停放。其主要目标是提高数据质量并指导爬虫的行为。

该系统主要依靠HTTP HEAD请求和DNS查询来最大限度地减少服务器负载并避免被标记为恶意机器人。它监控可用性，并基于证书详细信息、安全态势和HTTP头部对网站进行指纹识别。数据主要存储在两个类别中：实时快照（当前可用性和网站指纹）和历史事件（变更摘要，变更前后的状态以JSON格式压缩）。

变更检测侧重于识别所有权变更、重大改版和域名停放。虽然证书或DNS变更等单个因素可能存在歧义，但变更的组合可以提供更强的信号。一个有趣的发现是，能够根据从HTTPS到HTTP的转换以及特定自治系统编号（ASN）的存在来识别停放的域名。

实施过程中遇到的挑战包括最初依赖SQL数据库进行作业调度（导致性能问题，通过在RAM中镜像解决）、管理每个域的请求限制以避免速率限制，以及应对证书验证的复杂性，特别是处理发送不完整证书链的配置错误的服务器。尽管使用了宽松的证书验证，该系统仍然难以应对配置错误。文中提到了AIA Fetching作为修复证书配置错误的解决方法。

---

## 13. 展示一下 HN: TrendFi – 我构建了可以自我优化的 AI 交易信号

**原文标题**: Show HN: TrendFi – I built AI trading signals that self-optimize

**原文链接**: [https://trend.fi](https://trend.fi)

TrendFi：一款人工智能驱动的交易平台，旨在通过提供交易信号，帮助用户做出更明智、数据驱动的投资决策。它跟踪资产、生成信号，并力求让用户领先于市场趋势。

该平台提供诸如通过电子邮件发送的即时交易提醒、一体化仪表板、市场更新和历史业绩数据等功能。它还强调风险管理，提供关于高风险的警告，以帮助用户避免重大损失。

TrendFi展示了最近的交易，包括已建仓和已平仓的交易，以及Coinbase、特斯拉、比特币、以太坊和其他资产的盈亏百分比。它还提供人工智能生成的分析片段，例如识别比特币潜在的看涨反转或特斯拉的超卖状况。

用户的评价称赞TrendFi的简单性、可靠性以及减轻投资压力的能力。他们强调了它对初学者和经验丰富的交易者的实用性，并赞扬了它提供数据驱动的信心。

该服务提供免费试用，无需信用卡。该页面还包括一个常见问题解答部分，解答有关该模型的优势、人工智能使用、风险管理、目标受众和测试方法等关键问题。

---

## 14. 入门史多德面包

**原文标题**: Getting Started Strudel

**原文链接**: [https://strudel.cc/workshop/getting-started/](https://strudel.cc/workshop/getting-started/)

本文介绍了 Strudel，一个 Tidal Cycles 模式语言的 JavaScript 移植，旨在用代码创作动态音乐。Strudel 入门门槛低，适合初学者和经验丰富的程序员，甚至可以同时用于音乐和编码教学。

Strudel 的功能包括实时编码音乐、使用模式操作进行算法作曲、通过 MIDI 或 OSC 与现有音乐设备集成，以及作为灵活的音序器。本文提供了一个代码示例，展示了 Strudel 的潜力，展示了鼓、和弦和旋律，并利用了诸如模式结构、效果和随机化等功能。

本文鼓励用户浏览展示以获取更多灵感，并提供了入门指南，建议从研讨会开始，然后开始创作第一个声音。最终，本文欢迎读者，告知他们 Strudel 的优点和潜力，并引导他们获取学习资源。

---

## 15. 椭圆曲线之美

**原文标题**: Elliptic Curves as Art

**原文链接**: [https://elliptic-curves.art/](https://elliptic-curves.art/)

这个名为“椭圆曲线艺术”的网页介绍了一个专注于椭圆曲线可视化的项目。该网站目前正在建设中，由Nadir Hajouji和Steve Trettel开发。核心理念似乎在于探索椭圆曲线的审美和视觉方面，可能通过图形表示突出其美丽和复杂性。页面提到旨在展示“一些精美的插图”，表明椭圆曲线的视觉诠释画廊将成为主要特色。此外，“论文”部分的加入表明该项目具有学术或研究导向的一面，可能涉及数学分析或对所用可视化技术的描述。本质上，该项目旨在通过以视觉上引人入胜且美观的方式呈现椭圆曲线，同时通过发表的论文提供更技术性和学术性的视角，从而弥合抽象数学和视觉艺术之间的差距。

---

## 16. 我的iPhone 8拒绝退役：现在它成了太阳能供电的视觉OCR服务器

**原文标题**: My iPhone 8 Refuses to Die: Now It's a Solar-Powered Vision OCR Server

**原文链接**: [https://terminalbytes.com/iphone-8-solar-powered-vision-ocr-server/](https://terminalbytes.com/iphone-8-solar-powered-vision-ocr-server/)

本文详细介绍了作者将旧iPhone 8改造为太阳能供电的OCR（光学字符识别）服务器的项目。出于避免使用云服务和利用闲置硬件的愿望，作者构建了一个使用Apple的Vision框架在本地处理图像的系统。

该设置包括一个运行定制SwiftUI应用程序进行OCR处理和显示实时分析的iPhone 8、一个带有太阳能电池板的EcoFlow River 2 Pro电源站用于离网供电、一台用于Web服务和API路由的迷你PC，以及一个用于连接所有设备的Tailscale网络。作者强调了iPhone 8令人惊讶的可靠性和效率，并指出它在一年内处理了超过83,000个OCR请求和48GB的图像。

本文强调了Apple的Vision框架与基于云的替代方案相比，在准确性和隐私方面的优势。作者还讨论了在加拿大多变的天气条件下运行太阳能供电系统所面临的挑战，并概述了一个用于电池管理的季节性策略。

成本分析表明，与云OCR服务相比，该项目具有潜在的节省，同时还有助于减少电子垃圾、实现能源独立和坚持本地优先计算原则。作者为有兴趣复制该项目的读者提供了资源，包括硬件建议、软件文档和电源管理工具。最终，该项目被认为是一种有趣、实用且具有环保意识的方式，可以重新利用旧技术并促进数据隐私。

---

## 17. OpenElections如何使用LLM

**原文标题**: How OpenElections Uses LLMs

**原文链接**: [https://thescoop.org/archives/2025/06/09/how-openelections-uses-llms/index.html](https://thescoop.org/archives/2025/06/09/how-openelections-uses-llms/index.html)

OpenElections 使用 Google Gemini LLM 将选举结果图像 PDF 转换为可用的 CSV 文件，克服了传统 OCR 和手动数据录入的挑战。OpenElections 面临的主要问题是将选举结果图片转换为 CSV 文件。虽然过去曾使用手动数据录入和 Able2Extract 等商业 OCR 软件，但它们要么成本高昂，要么容易出错，要么难以处理复杂的布局和标记。Gemini 凭借其高精度和大的上下文窗口脱颖而出，使其能够处理大型 PDF 文件。

文章详细介绍了来自德克萨斯州莱姆斯通县、活橡树县和卡梅隆县的成功案例。Gemini 可以有效地处理两栏布局、点分隔符，甚至绿色背景或不同的阴影。但是，由于 Gemini 在持续处理过程中可能出现问题，因此处理非常大的 PDF 文件（如卡梅隆县的 653 页文件）需要将其分割成较小的块。

OpenElections 倾向于使用 Gemini，因为其 AI Studio UI 可以控制“创造力”并禁用“思考模式”以执行简单的任务。虽然速度有所提高，但准确性仍然至关重要。OpenElections 使用格式检查、重复记录检测和基本数学不一致性来验证数据准确性。他们将从选区 CSV 得出的多个总数与官方累积报告中的数字进行比较。虽然 LLM 提供了一种解决方案，但 OpenElections 将它们与验证系统一起使用，以确保结果与原始数据一致。

---

## 18. 地球年代学支持新墨西哥州白沙国家公园人类足迹为末次盛冰期时代

**原文标题**: Geochronology supports LGM age for human tracks at White Sands, New Mexico

**原文链接**: [https://www.science.org/doi/10.1126/sciadv.adv4951](https://www.science.org/doi/10.1126/sciadv.adv4951)

无法访问文章链接。

---

## 19. 谷歌正使用YouTube视频来训练其AI视频生成器。

**原文标题**: Google is using YouTube videos to train its AI video generator

**原文链接**: [https://www.cnbc.com/2025/06/19/google-youtube-ai-training-veo-3.html](https://www.cnbc.com/2025/06/19/google-youtube-ai-training-veo-3.html)

谷歌正在利用其庞大的YouTube视频库来训练其AI模型，包括Gemini和Veo 3视频生成器。虽然谷歌承认使用YouTube内容，并声明他们仅使用其中一部分且遵守创作者协议，但这种做法引发了对知识产权的担忧。专家和创作者都对此表示不安，指出许多人并不知道他们的内容被用于AI训练，并且无法选择退出谷歌的内部训练。

使用YouTube视频来训练强大的AI视频生成器Veo 3尤其令人担忧。虽然YouTube声称已采取保护措施，但一些创作者担心该AI最终可能会在未经适当署名、许可或补偿的情况下与他们竞争或取而代之。该平台的服务条款授予YouTube广泛的使用上传内容的许可，但这对AI训练的影响尚未被广泛理解。

Vermillio等公司正在开发工具来检测AI生成内容与人类创作视频之间的重叠，突显了潜在的版权问题。虽然一些创作者对使用Veo 3持开放态度，并认为这是一种友好的竞争，但另一些创作者则对其对其生计的潜在影响表示担忧。虽然YouTube为肖像侵权提供了一些补救措施，但其有效性受到质疑，且创作者无法阻止谷歌自身的AI训练行为。这种情况凸显了关于AI和知识产权的更广泛辩论，并呼吁加强对艺术家和创作者的保护。

---

## 20. 展示 HN：Workout.cool – 开源健身指导平台

**原文标题**: Show HN: Workout.cool – Open-source fitness coaching platform

**原文链接**: [https://github.com/Snouzy/workout-cool](https://github.com/Snouzy/workout-cool)

Workout.cool 是一个全新的开源健身指导平台，脱胎于被废弃的 workout.lol 项目的复兴。原项目由于高昂的视频授权费用面临商业挑战，最终被出售并随后被放弃。为了给开源社区提供一个可靠且现代的健身平台，原开发者创建了 Workout.cool。

该平台允许用户创建锻炼计划、跟踪进度，并访问包含说明和视频演示的庞大运动数据库。快速入门指南解释了如何使用 Docker 或手动 PostgreSQL 安装来设置平台。CSV 导入过程允许将运动导入数据库，包括肌肉群和设备等属性。

该项目遵循 Feature-Sliced Design 原则，并采用 Next.js App Router。路线图包括添加更多运动、开发移动应用程序、整合游戏化元素、高级统计数据、可穿戴设备集成、多语言支持、OAuth 身份验证和一个社区论坛。

欢迎贡献，并提供贡献指南。部署选项包括 Docker 和手动部署。该项目采用 MIT 许可证。作者鼓励通过给仓库加星、加入 Discord、报告问题、提出建议、广而告之、贡献代码和赞助项目来支持社区。目标是重建一个社区驱动的健身工具。

---

## 21. 2025年6月 C2PA新闻

**原文标题**: June 2025 C2PA News

**原文链接**: [https://www.tbray.org/ongoing/When/202x/2025/06/17/More-C2PA](https://www.tbray.org/ongoing/When/202x/2025/06/17/More-C2PA)

在Tim Bray 2025年6月的C2PA新闻中，他探讨了内容来源倡议（C2PA）技术（以“内容凭证”为名进行推广）的进展，重点关注其对抗虚假信息的潜力。

他强调了Chrome扩展程序（ContentLens C2PA Validator，Digimarc的C2PA内容凭证）的可用性，这些扩展程序用于验证图像中的C2PA数据。这些扩展程序可确认图像是否具有C2PA清单，以及是否由受信任的发行者（如Adobe）签名。Bray详细介绍了这些扩展程序如何使用LinkedIn和Clear等服务来验证内容创建者的身份，并中继AI工具的使用情况。

Bray赞扬了C2PA的存在和功能，强调了在人工智能生成虚假信息的时代，来源（了解谁发布了内容）的重要性。他指出，社交媒体上可验证的媒体来源将是打击虚假信息的宝贵工具。

然而，他也指出了需要改进的领域：

*   **身份验证：** 将验证扩展到Fediverse和Bluesky句柄。
*   **浏览器集成：** 直接的浏览器支持C2PA验证，而不是依赖于缺少移动支持的扩展程序。
*   **JavaScript包：** 一个随时可用的JS包，以便在网站上轻松进行C2PA验证。
*   **开源支持：** 将C2PA清单创建集成到ImageMagick等开源图像处理工具中，并可能提供托管签名服务。
*   **Web3/NFT诈骗担忧。**

Bray提出了一项服务，网站所有者可以轻松地将来源信息嵌入到其图像的C2PA清单中。

他最后强调了社交媒体平台拥抱C2PA的必要性，并呼吁继续开发，使该技术更易于访问和有效。

---

## 22. 失踪的十一号 (2015)

**原文标题**: The Missing 11th of the Month (2015)

**原文链接**: [https://drhagen.com/blog/the-missing-11th-of-the-month/](https://drhagen.com/blog/the-missing-11th-of-the-month/)

本文探讨了为什么谷歌Ngrams数据库中每月11号出现的频率明显低于其他日期，这是xkcd的兰德尔·门罗观察到的一个现象。作者首先使用统计分析证实了这一观察结果，表明11号是一个显著的异常值，尤其是在1860年代之后。

调查发现，光学字符识别（OCR）错误是主要原因。数字“11”经常被误读为“ll”、“II”、“li”、“ii”以及类似的组合（“xxth”），尤其是在较旧的文本中。将这些误读添加到原始数据中会显著增加11号的出现频率。

进一步的分析揭示了另一个常见的错误：将“11th”误读为“nth”，尤其是在1860年代之后。将这些“nth”误读纳入考虑范围后，便能完整地解释这一现象，有效地消除了“缺失的11号”现象，并使其频率与其他日期相当。

作者将1860年代OCR错误增加的原因归因于打字机的普及，最初的打字机缺少专用的“1”键，鼓励使用小写字母“l”代替。这模糊了两种字符在字体上的区别，导致误读增加。即使在今天，这些字体相似性的持续存在也导致了错误率的持续（尽管有所降低）。对于“nth”误读的原因进行了推测，但最终没有给出答案。

---

## 23. 便当：键盘里的Steam Deck

**原文标题**: Bento: A Steam Deck in a Keyboard

**原文链接**: [https://github.com/lunchbox-computer/bento](https://github.com/lunchbox-computer/bento)

Bento：一款专为空间显示器设计的定制电脑，灵感来自 Commodore 64 和赛博朋克社区。其名称源于便当盒般的外观，能够整洁地放置在键盘下方，键盘兼作保护盖和储物仓。一个关键的设计元素是取消内置显示器，以消除冗余并减轻重量，从而增强便携性。

当前版本采用 Steam Deck OLED 的主板、散热器和电池，因其纤薄的外形和性能而被选中。但该设计适用于其他单板计算机（SBC）。项目创建者对现有XR“电脑”感到不满，它们本质上是限制级的iPad，依赖于真实电脑的屏幕镜像来进行任何严肃的工作，因此构建了 Bento，旨在直接解决这个问题，成为专为空间显示器设计的电脑。

创建者正在开源该设计，包括STEP、3MF和STL文件，以鼓励协作和扩展。目前的潜在贡献领域包括支持其他键盘、树莓派 5 版本（特别是寻找合适的电池解决方案）、Framework 笔记本电脑版本、支持更多SBC，以及可以放入储物仓的外围设备（如游戏手柄或鼠标）。鼓励贡献者提交拉取请求以分享他们的修改。

---

## 24. 基因组编辑器的可视化指南

**原文标题**: A Visual Guide to Genome Editors

**原文链接**: [https://www.asimov.press/p/a-visual-guide-to-genome-editors](https://www.asimov.press/p/a-visual-guide-to-genome-editors)

基因组编辑器的可视化指南：CRISPR-Cas 系统及其应用。本文以 Victoria Gray 使用 Casgevy（首个 FDA 批准的基于 CRISPR 的疗法）成功治疗镰状细胞贫血为例，重点介绍 CRISPR-Cas 系统。

文章解释说，CRISPR 系统起源于细菌防御病毒的机制，细菌将病毒 DNA 整合到自身基因组中，从而为未来的防御建立“记忆”。该系统的核心是一个引导 RNA (gRNA)，它与 CRISPR 相关 (Cas) 蛋白结合，形成核糖核蛋白 (RNP) 复合物。

文章随后深入探讨了特定的 CRISPR 系统，包括：

*   **Cas9：** 第一个被设计的基因组编辑器，因其效率而被广泛使用。它在找到特定的 PAM 序列后切割 DNA 双链，细胞使用 NHEJ 或 HDR 修复断裂，从而实现基因破坏或插入。人们正在通过设计更具特异性的酶来解决对脱靶活性（在非预期序列上切割）的担忧。
*   **Cas12：** CRISPR 蛋白的一个多样化家族，通常被认为比 Cas9 更具特异性。它在交错的位置切割 DNA 双链，留下“粘性末端”，从而促进 HDR。 Cas12 还表现出附带切割，无差别地切割 ssDNA，这被用于诊断工具。
*   **Cas13：** 结合并切割 RNA 而不是 DNA。

文章还提到了碱基编辑器、先导编辑器和桥接 RNA 系统等其他基因组编辑工具。 文章强调了目前使用 Cas9 和 Cas12 治疗各种疾病的临床试验，并简要介绍了这些 Cas 蛋白的进化起源。

---

## 25. 用数学作画：光线步进的温和研究 (2023)

**原文标题**: Painting with Math: A Gentle Study of Raymarching (2023)

**原文链接**: [https://blog.maximeheckel.com/posts/painting-with-math-a-gentle-study-of-raymarching/](https://blog.maximeheckel.com/posts/painting-with-math-a-gentle-study-of-raymarching/)

本文“用数学作画：Raymarching入门指南”介绍了光线步进(raymarching)技术，这是一种使用数学而非传统几何体创建3D场景的渲染技术。它解释了光线步进的工作原理，即从相机投射光线穿过每个像素，直到它们与使用有向距离场(SDFs)定义的对象相交。

SDFs计算光线上的点与对象表面之间的最短距离，从而允许通过数学公式定义场景。本文详细介绍了如何使用Three.js/React Three Fiber作为画布来实现一个基本的光线步进器，包括必要的着色器调整，例如标准化UV坐标和调整宽高比。

随后，本文深入探讨了通过漫反射光照增加深度，通过使用特定公式计算表面法线并将其与光照方向向量进行点积来实现。它解释了如何组合SDFs来渲染多个对象，主要使用`min`函数来确定最近的表面。还简要提及了`max`函数，用于创建形状的交集。作者展示了如何通过数学操作实现平滑的并集和交集。

---

## 26. 破解德州彩票的骗局

**原文标题**: The Scheme That Broke the Texas Lottery

**原文链接**: [https://www.newyorker.com/news/letter-from-the-southwest/the-scheme-that-broke-the-texas-lottery](https://www.newyorker.com/news/letter-from-the-southwest/the-scheme-that-broke-the-texas-lottery)

黎明·内特斯，德州乐透彩票的忠实监督者，通过她的出版物《乐透报告》，于2023年4月当德州乐透头奖迅速飙升至9500万美元时，开始感到不安。她怀疑有人大量购买彩票，实际上保证了中奖，并破坏了彩票的公平性。她的担忧变成了现实，头奖最终被赢得，后来发现是由一家位于伦敦的赌博集团通过乐透网(Lottery.com)（一家彩票快递服务公司）促成的。

这次批量购买暴露了德州彩票委员会内部根深蒂固的问题，特别是关于其与Jackpocket和Lotto.com等彩票快递公司的关系。这些公司在很大程度上不受监管的情况下运营，允许在线售票，吸引了年轻人群，但也引发了对未成年人赌博和州外购买的担忧。

内特斯持续的批评和审查，加上媒体的关注，引发了调查和政治影响。德州彩票委员会主任加里·格里夫被指控在法律的“灰色地带”运作，并驳回了对批量购买的担忧。丑闻导致他突然退休，随后他的副手瑞安·明德尔辞职。

事后，彩票快递公司受到了更多的审查，他们辩称自己成了委员会失职的替罪羊。立法者曾考虑彻底结束彩票，但最终决定解散并在不同的州机构下重新组建。 这次丑闻极大地阻碍了在德克萨斯州扩大赌博的任何尝试。内特斯曾经被认为是一个怪人，现在被认为是揭露该计划并促成改革的关键人物。

---

## 27. Zed调试器来了

**原文标题**: The Zed Debugger Is Here

**原文链接**: [https://zed.dev/blog/debugger](https://zed.dev/blog/debugger)

Zed发布调试器，旨在实现速度、熟悉度和可配置性。它开箱即用支持 Rust、C/C++、JavaScript、Go 和 Python 等语言，并通过调试适配器协议 (DAP) 扩展支持其他语言。为了简化设置，Zed 使用“定位器”自动将构建配置转换为调试配置，最初支持 Cargo、Python、JavaScript 和 Go。

该调试器具有可自定义的 UI、键盘导航和轻松检查程序状态的功能。核心基础由社区构建，并特别感谢 Remco Smits 对该项目的深入参与。

Zed 的调试器采用两层架构：数据层用于与调试适配器交互，UI 层用于获取数据。这种设计有助于协作调试并最大限度地减少带宽使用。扩展 API 支持允许开发者集成自己的调试适配器。

内联变量值通过 Tree-sitter 支持，确保在当前执行范围内准确识别 Python、Rust 和 Go 等语言的变量。

未来的计划包括添加高级视图（监视列表、内存视图等）、扩展更多语言和构建系统的自动配置，并根据用户反馈进一步改进调试器。

---

## 28. 3D打印六英寸f/5紧凑型旅行望远镜模型

**原文标题**: 3D printable 6" f/5 compact travel telescope model

**原文链接**: [https://www.printables.com/model/1325533-smallest-telescope-kit-for-150750](https://www.printables.com/model/1325533-smallest-telescope-kit-for-150750)

本文简述了一个可3D打印的紧凑型旅行望远镜模型，其孔径为6英寸，焦比为f/5。标题明确说明了目的：提供使用3D打印机制作望远镜的说明或文件，并优先考虑便携性。文中包含缩写“BHH”（很可能是背包固定钩的缩写），以及数字243、5和613。

根据上下文，这些数字可能指的是：

*   **测量值：** 与BHH相关的尺寸（例如，毫米、英寸）。可能是长度、宽度和高度。
*   **零件编号/数量：** 如果BHH是一个单独的组件，这些可能是零件编号或构建它所需的特定零件的数量。
*   **打印设置：** 与3D打印BHH相关的参数，例如填充密度、层高或打印速度。

虽然在没有更多上下文的情况下，“243、5、613”的确切含义仍然不明确，但核心要点是该文章描述了一个可3D打印的便携式望远镜，并提供了与其背包固定钩（BHH）相关的具体信息。这个钩子对于其作为旅行望远镜的功能至关重要，使其能够轻松地装在背包中携带。

---

## 29. 微软想让你买一台新电脑。想让你的旧电脑重新安全吗？

**原文标题**: Microsoft wants you to buy a new computer. Make your current one secure again?

**原文链接**: [https://endof10.org/](https://endof10.org/)

本文着重指出Windows 10将于2025年10月停止支持，并提出安装Linux操作系统作为购买新电脑的替代方案。文章认为2010年后购买的电脑很可能仍然可用，并且可以通过Linux来焕发新生。

文章概述了切换到Linux的几个优势：它消除了对新硬件和许可费用的需求，因为许多Linux发行版和软件更新都是免费的。文章还强调了相比Windows，Linux具有更强的隐私性，Windows因包含广告和间谍软件而受到批评。一个重要的好处是环保：延长现有电脑的使用寿命可以大幅减少碳排放。

文章指出了随手可得的支持，包括当地的维修咖啡馆、独立的电脑商店、在线论坛以及愿意帮助安装过程的潜在当地志愿者。最后，文章提倡用户控制，强调Linux提供的软件的四个自由，使用户能够使用、研究、分享和改进程序。文章鼓励读者寻找当地的维修资源，体验重新利用其“崭新的旧电脑”的好处。

---

## 30. 模糊测试在程序移植中的出人意料的有效性

**原文标题**: The unreasonable effectiveness of fuzzing for porting programs

**原文链接**: [https://rjp.io/blog/2025-06-17-unreasonable-effectiveness-of-fuzzing](https://rjp.io/blog/2025-06-17-unreasonable-effectiveness-of-fuzzing)

本文探讨了利用大型语言模型（LLMs）将C代码自动化移植到Rust的潜力，重点关注一种基于模糊测试的方法。作者认为，LLMs可以执行“根本性更新”，例如语言移植和API更改，这些更新在以前是不可行的。

作者借鉴了TensorFlow维护方面的挑战以及将Python代码移植到C++的潜在好处。然后，他们介绍了利用LLMs的优势来解决具体问题的想法，尤其是在与严格测试相结合时。

核心概念是使用LLMs将C代码增量地翻译成Rust模块。对于每个移植的模块，LLM生成模糊测试，以比较C和Rust版本在随机输入下的输出。这种方法旨在确保在移植过程中保持行为不变。

作者详细介绍了将Zopfli（一种压缩库）从C移植到Rust的三次尝试。第一次尝试突出了与C版本进行直接比较的重要性。最终，更严格的方法包括：

1. 符号的拓扑排序，以管理依赖关系。
2. LLM生成的FFI绑定和Rust实现。
3. LLM生成的模糊测试，用于直接比较C和Rust的输出。
4. 基于模糊测试失败的迭代修复。

文章表明，这种基于自动化模糊测试的方法可以显著减少移植项目所需的工作量，使其成为面临维护挑战或寻求代码库现代化的库更可行的选择。作者强调，该方法将移植更多地变成一项提示工程任务，而不是手动编码任务。

---

## 31. Base44 以 8000 万美元现金出售给 Wix

**原文标题**: Base44 sells to Wix for $80M cash

**原文链接**: [https://techcrunch.com/2025/06/18/6-month-old-solo-owned-vibe-coder-base44-sells-to-wix-for-80m-cash/](https://techcrunch.com/2025/06/18/6-month-old-solo-owned-vibe-coder-base44-sells-to-wix-for-80m-cash/)

以色列开发者Maor Shlomo将其成立仅六个月、自筹资金的氛围编码初创公司Base44以8000万美元现金出售给Wix。Base44允许非程序员使用文本提示构建软件应用程序，经历了快速增长，用户达到25万，5月份盈利18.9万美元，主要通过口碑营销实现。Shlomo曾创立Explorium，他在LinkedIn和X上公开记录了Base44的发展历程，包括他决定使用Anthropic的Claude LLM以提高成本效益。

虽然Shlomo并非真正意义上的“独角兽”，因为他有八名员工，他们将获得2500万美元的留任奖金，但该交易凸显了人工智能对个人生产力的潜在影响。Base44通过与eToro和Similarweb等以色列科技公司的合作获得了发展。

Shlomo表示，出售的原因是需要更大的规模和资源，并对Base44在Wix的未来感到兴奋。对Wix而言，此次收购是在盈利的LLM驱动的氛围编码平台的基础上扩展其无代码网站构建产品的合理步骤。文章还提到波士顿的TechCrunch活动，其中包括策略、研讨会和人脉拓展。

---

## 32. 德州仪器将投资600亿美元在美国制造基础半导体。

**原文标题**: TI to invest $60B to manufacture foundational semiconductors in the U.S.

**原文链接**: [https://www.ti.com/about-ti/newsroom/news-releases/2025/texas-instruments-plans-to-invest-more-than--60-billion-to-manufacture-billions-of-foundational-semiconductors-in-the-us.html](https://www.ti.com/about-ti/newsroom/news-releases/2025/texas-instruments-plans-to-invest-more-than--60-billion-to-manufacture-billions-of-foundational-semiconductors-in-the-us.html)

德州仪器（TI）宣布在美国半导体制造领域投资600亿美元巨资，创美国历史之最。这项投资将资助在得克萨斯州和犹他州三大基地新建七家晶圆厂，创造超过6万个美国就业岗位，并扩大TI生产基础模拟和嵌入式处理芯片的产能。

此次扩张旨在满足汽车、个人电子产品和数据中心等各行业对半导体日益增长的需求。苹果、福特、美敦力、英伟达和SpaceX等美国主要公司正在加强与TI的合作，以利用其扩大的国内制造能力。

具体项目包括在得克萨斯州谢尔曼市进行重大投资，最多分配400亿美元用于四家晶圆厂。该公司还在得克萨斯州理查森市和犹他州李海市的现有和新晶圆厂加速生产。

TI首席执行官Haviv Ilan强调了可靠、低成本的300毫米产能对于这些关键芯片的重要性。苹果、福特、美敦力、英伟达和SpaceX等合作伙伴赞扬了TI美国制造芯片对其各自创新的重要性，并列举了供应链安全、先进技术和性能改进等优势。

TI的投资符合美国政府促进国内半导体制造和减少对外国供应商依赖的倡议。

---

## 33. PWM闪烁：危害健康的隐形光？

**原文标题**: PWM flicker: Invisible light that's harming our health?

**原文链接**: [https://caseorganic.medium.com/the-invisible-light-thats-harming-our-health-and-how-we-can-light-things-better-d3916de90521](https://caseorganic.medium.com/the-invisible-light-thats-harming-our-health-and-how-we-can-light-things-better-d3916de90521)

本文探讨了LED照明中PWM闪烁的问题及其对健康和福祉的潜在影响。作者讲述了在历史悠久的城堡中的经历，现代LED照明尽管外观温暖，但由于闪烁而营造出不适的氛围。

核心问题在于脉冲宽度调制 (PWM)，这是一种通过快速开关光源来调光的方法，会导致闪烁。虽然许多人没有有意识地感知到它，但PWM闪烁会导致眼睛疲劳、不适、偏头痛，甚至对敏感人群（估计占人口的 5-20%）产生恶心。文章强调，PWM通常用于LED灯、OLED显示器和一些白炽灯泡。低于1kHz的闪烁尤其成问题。

作者提倡更好的替代方案，如恒流衰减 (CCR) 或直流调光，它们通过降低电流来调节光的亮度，而无需快速开关。CCR调光常见于高端、无闪烁照明中，并且在视觉舒适度和神经系统健康方面明显更好。

文章鼓励读者检查产品规格中的PWM频率，目标是超过20kHz或获得“无闪烁”认证。 同样推荐使用直流调光或混合调光的产品。平静科技研究所的认证计划，包括使用直流调光的Daylight Computer，被认为是优先考虑无闪烁技术以改善用户福祉的例子。 虽然CCR灯泡可能更昂贵，但它们被认为是对健康和生产力的投资。

---

## 34. 网站正在通过浏览器指纹追踪你

**原文标题**: Websites are tracking you via browser fingerprinting

**原文链接**: [https://engineering.tamu.edu/news/2025/06/websites-are-tracking-you-via-browser-fingerprinting.html](https://engineering.tamu.edu/news/2025/06/websites-are-tracking-you-via-browser-fingerprinting.html)

德州农工大学领衔的研究表明，网站正积极使用浏览器指纹技术追踪用户在线行为，即使Cookie被阻止或删除。浏览器指纹技术利用屏幕分辨率、时区和设备型号等浏览器细节的独特组合来创建数字“签名”，以此识别单个浏览器。这种方法难以检测和阻止，使其成为一种隐蔽的追踪技术。

研究人员开发了一种名为FPTrace的工具，用于分析广告系统如何响应浏览器指纹的变化。他们发现，指纹的改变显著影响了广告商的出价和HTTP记录，表明指纹技术被用于定位和追踪用户。重要的是，他们发现即使在用户根据GDPR和CCPA等隐私法选择退出追踪时，这种追踪仍然会发生。

该研究突显了当前隐私工具和政策在解决浏览器指纹方面的不足。研究人员提倡加强浏览器防御能力和对指纹识别行为的监管，以保护用户隐私。FPTrace框架为监管机构提供了一种在未经用户同意的情况下，审计从事这些活动的网站和供应商的手段。该研究是与约翰·霍普金斯大学合作进行的，并在ACM Web Conference (WWW) 2025上发布。

---

## 35. 同态加密的CRDT

**原文标题**: Homomorphically Encrypting CRDTs

**原文链接**: [https://jakelazaroff.com/words/homomorphically-encrypted-crdts/](https://jakelazaroff.com/words/homomorphically-encrypted-crdts/)

本文探讨了使用同态加密来解决本地优先软件中加密数据同步的问题。传统的端到端加密阻止同步服务器合并更新，要求用户同时在线或下载大量未压缩数据。

同态加密允许在加密数据上进行计算而无需解密。本文解释了这个概念，并使用 Rust 中的 THFE-rs 库演示了一个简单的加法示例。然后，它深入研究了“底层”工作原理，解释了部分、轻微、分级和完全同态加密，以及如何使用逻辑门（XOR，AND）对加密的位执行任何计算。

作者介绍了末次写入胜出寄存器 CRDT 的概念，它包括对等 ID、时钟和值，并解释了合并算法的工作原理。然后，它开始探索创建此 CRDT 的同态加密版本。目标是使同步服务器能够合并来自不同用户的更改，而无需查看底层数据，从而改善异步协作和数据压缩。作者指出，他们不是密码学家，并建议在生产环境中使用任何代码之前要谨慎。

---

## 36. SpaceX星舰36号异常

**原文标题**: SpaceX Starship 36 Anomaly

**原文链接**: [https://twitter.com/NASASpaceflight/status/1935548909805601020](https://twitter.com/NASASpaceflight/status/1935548909805601020)

JavaScript已禁用。

此内容并非关于SpaceX星舰36号异常的文章，而是网站（可能是x.com，前身为Twitter）的错误信息，表明用户的浏览器禁用了JavaScript。由于网站正常运行需要JavaScript，因此要求用户启用JavaScript或切换到受支持的浏览器。该信息包含指向帮助中心、服务条款、隐私政策、Cookie政策、版本说明和广告信息的链接，以及声明X Corp.在2025年拥有所有权的版权声明。

简而言之，用户由于浏览器禁用了JavaScript而无法访问x.com网站。没有关于星舰36号异常的实际内容。

---

## 37. 基于CPU的拣选车到货位式托盘仓库布局设计

**原文标题**: CPU-Based Layout Design for Picker-to-Parts Pallet Warehouses

**原文链接**: [https://arxiv.org/abs/2506.04266](https://arxiv.org/abs/2506.04266)

这篇由Timo Looms和Lin Xie于2025年6月3日提交的arXiv预印本(arXiv:2506.04266)提出了一种受CPU架构启发的拣货到货位托盘仓库的新型仓库布局设计。这篇题为“基于CPU的拣货到货位托盘仓库布局设计”的论文旨在解决传统仓库布局导致的过度行驶距离和高昂的人工成本等问题。

所提出的基于CPU的布局将仓库划分为专门的区域：性能（P）、效率（E）和共享（S）。该研究利用离散事件模拟来评估该设计的有效性。该基于CPU的布局与传统的矩形布局（采用随机和ABC存储策略）以及飞行V型布局进行了比较。

结果以8页和6个图表的形式呈现，表明与传统布局相比，吞吐时间显着改善，并且人工需求减少。这表明实施基于CPU的布局具有优化拣货到货位托盘仓库运营的潜力。该论文被归类为多智能体系统（cs.MA），旨在用于会议演示。

---

## 38. MCP规范 – 2025-06-18版本变更

**原文标题**: MCP Specification – version 2025-06-18 changes

**原文链接**: [https://modelcontextprotocol.io/specification/2025-06-18/changelog](https://modelcontextprotocol.io/specification/2025-06-18/changelog)

本文概述了自 2025-03-26 修订版以来对模型上下文协议 (MCP) 规范所做的更改。主要更新包括删除对 JSON-RPC 批处理的支持以及添加结构化工具输出支持。MCP 服务器现在被归类为 OAuth 资源服务器，需要用于授权服务器发现的元数据。为了增强安全性，MCP 客户端必须根据 RFC 8707 实现资源指示器。

该规范还纳入了明确的安全考虑、授权方面的最佳实践以及新的安全最佳实践页面。新增功能包括对启发请求的支持，使服务器能够请求额外的用户信息，以及工具调用结果中的资源链接。此外，在使用 HTTP 时，协商的协议版本必须在后续请求中通过 MCP-Protocol-Version 标头指定。

其他模式更改包括向更多接口类型添加 `_meta` 字段、指定 `_meta` 的用法以及向 CompletionRequest 添加 `context` 字段，允许包含先前解析的变量。最后，添加了 `title` 字段用于易于理解的显示名称，将易于理解的名称与程序标识符分开。完整的变更日志可在 GitHub 上找到。

---

## 39. 黑客帝国 (1999) 拍摄地点 – 逐帧还原 – 澳大利亚悉尼 [视频]

**原文标题**: The Matrix (1999) Filming Locations – Shot-for-Shot – Sydney, Australia [video]

**原文链接**: [https://www.youtube.com/watch?v=UVf7rMqnwI0](https://www.youtube.com/watch?v=UVf7rMqnwI0)

YouTube视频《黑客帝国 (1999) 拍摄地 – 逐帧对比 – 悉尼，澳大利亚》很可能探索并确定了电影《黑客帝国》1999年版中特定场景在澳大利亚悉尼的真实拍摄地点。“逐帧对比”表明该视频会将实际电影场景与现在的地点进行比较，让观众了解电影是如何拍摄的以及这些地点现在的样子。标题暗示了对电影在悉尼使用的拍摄地点的详细比较分析。

YouTube标题下方的附带文字是所有YouTube视频通用的标准样板文字，涉及法律免责声明、服务条款以及有关平台、版权和广告的常规信息。这些文字与视频本身关于《黑客帝国》的内容无关，并且没有提供关于视频内容的更多信息。

---

## 40. 区块链分析中的内存C++飞跃

**原文标题**: In-Memory C++ Leap in Blockchain Analysis

**原文链接**: [https://caudena.com/the-in-memory-c-leap-in-blockchain-analysis/](https://caudena.com/the-in-memory-c-leap-in-blockchain-analysis/)

Caudena的CashflowD (CFD) 是一款革命性的加密货币分析引擎，采用C++构建，提供实时、法庭认可的加密情报，与传统系统相比，可降低200倍至400倍的基础设施成本。面对区块链数据爆炸式增长的危机，CFD凭借其专有的内存数据库和JIT编译查询引擎，克服了传统工具的局限性，解锁了以前无法实现的分析能力。

CFD的架构针对Solana（400TB+）等区块链进行了优化，其内存C++核心采用定制存储，优先考虑RAM和积极的数据打包，从而有效管理PB级数据。定制的哈希数组映射尝试 (HAMT) 和分配器进一步提高了性能。

JIT编译利用LLVM ORCv2，使分析师能够将动态查询转换为优化的机器代码。智能聚类算法提供确定性的、法庭认可的结果，并具有完全的可解释性，而O(1)聚类连接和覆盖森林实现近乎瞬时的更新。

弹性评分模型可抵抗洗钱策略，使用数学上强大的传播和多阶段更新，以实现即时可用性和自定义。评分使用BitArrayMap项目高效存储。复杂的缓存和优化的迭代器，包括地址余额、实体和集群统计缓存，有助于实现亚毫秒级的响应时间。

CFD的技术优势转化为变革性的商业优势，尤其是在数据密集的区块链上，以显著更低的成本提供远优于传统系统的分析能力，从而建立了强大的经济护城河。

---

## 41. 更多前端网页技巧

**原文标题**: More Front End Web Tricks

**原文链接**: [https://kaiwenwang.com/writing/more-frontend-web-tricks](https://kaiwenwang.com/writing/more-frontend-web-tricks)

本文汇集了一系列前端Web开发技巧和观察。内容涵盖了从处理移动端过度滚动到解决文本渲染问题和图标可用性等多个方面。

作者强调在多种设备上测试设计的重要性，尤其是在13英寸Macbook等较小设备上，因为网站通常由于在大屏幕上开发而显得过大。解决方案包括使用clamp函数进行字体大小调整和采用比例边距。

文章深入探讨了移动端潜在的过度滚动问题，不鼓励完全禁用过度滚动，并建议采用固定头部的方式。使用`overflow-x-hidden`解决水平滚动bug。作者表示更偏爱`geometricPrecision`文本渲染属性，而不是`optimizeLegibility`。

文章批判了图标可用性，更喜欢带有文本的图标。文章还强调了“文本到任务”工作流程的未来，认为这是一种有前景的应用程序模式。文章还提到了底部封面页对行动号召的实用性。

作者还对抽象思维与社交情感思维进行了较长的、略带哲学意味的探讨，将其与清晰沟通的需求以及注重实质而非仅仅是表现联系起来。

最后，文章反思了营销和用户感知，指出产品质量与其呈现方式之间存在脱节。文章认为，虽然独立评估是理想的，但许多用户依赖于感知到的质量，因此，即使开发者觉得在美学上不吸引人，良好的呈现也至关重要。

---

## 42. Poline – 一款使用极坐标的神秘配色方案生成器

**原文标题**: Poline – An enigmatic color palette generator using polar coordinates

**原文链接**: [https://meodai.github.io/poline/](https://meodai.github.io/poline/)

Poline：一个基于极坐标生成调色板的 TypeScript 微型库。该名称由“polar”（极坐标）和“line”（线）组合而成，体现了其核心功能：在极坐标系中的锚点之间绘制线条，从而创建颜色变化。锚点代表特定的颜色点，库通过在这些锚点之间插值来生成颜色。每对锚点之间生成的颜色数量由指定的点数决定。这些点使用位置函数进行定位，从而可以对颜色渐变和整体调色板设计进行细致的控制。本质上，Poline 提供了一种独特且可能颇具神秘色彩的调色板生成方法，利用极坐标的几何特性来产生有趣且可定制的结果。

---

## 43. 游戏破解 – Valve反作弊系统 (VAC)

**原文标题**: Game Hacking – Valve Anti-Cheat (VAC)

**原文链接**: [https://codeneverdies.github.io/posts/gh-2/](https://codeneverdies.github.io/posts/gh-2/)

本文深入探讨 Valve 反作弊系统 (VAC)，探索其历史、著名的误封事件，以及其检测作弊的工作原理。VAC 于 2002 年推出，在用户模式下运行，并从服务器流式传输反作弊模块 (DLL)。

本文重点介绍了“VAC 绕过”，该方法涉及转储这些模块以分析其检测方法。文章详细介绍了使用 Binary Ninja 对 steamservice.dll 进行逆向工程的过程，以定位这些 DLL 的加载位置，特别是识别出最终调用 LoadLibrary 加载模块的函数 sub_10086f80 和 sub_10086c40。

绕过的核心在于强制使用 LoadLibrary 加载模块，从而允许转储它们。文章演示了如何通过在特定偏移量将“相等则跳转”指令更改为“不相等则跳转”来修补 steamservice.dll。这种操作导致反作弊模块通过 LoadLibrary 而不是反射方式加载。

最后，通过使用 Procmon，文章识别出 steamservice.exe 创建的包含转储的 VAC 模块的临时文件（.TMP 文件）。这些模块经过分析后，揭示了诸如 "_runfunc@20" 之类的函数，从而深入了解 VAC 的内部运作和检测策略。文章最后声明，下一篇文章将侧重于分析这些反作弊模块，以更深入地了解它们的功能。

---

## 44. Fang，CLI 快速启动工具包

**原文标题**: Fang, the CLI Starter Kit

**原文链接**: [https://github.com/charmbracelet/fang](https://github.com/charmbracelet/fang)

Fang：简化Cobra命令行应用创建的CLI启动套件。它是一个小型库，旨在提供一个包含多个关键功能的“开箱即用”体验。

这些功能包括：美观且风格化的帮助和使用页面、风格化的错误消息、自动`--version`标志管理、使用mango1生成manpage、shell补全生成、主题支持以及避免在用户出错后显示帮助的更友好的用户体验。

通过展示如何通过调用`fang.Execute`和一个`*cobra.Command`将Fang集成到Cobra应用程序中来演示用法。

该文档鼓励贡献，并提供了通过Twitter、Discord和Fediverse进行反馈的链接。Fang采用MIT许可，是Charm的一部分。脚注解释了使用Mango生成manpage的原因，这避免了为每个子命令生成manpage的过度行为（这是Cobra的默认行为），并直接从roff渲染更好看的man page。

---

## 45. 为人工智能编写文档：最佳实践

**原文标题**: Writing documentation for AI: best practices

**原文链接**: [https://docs.kapa.ai/improving/writing-best-practices](https://docs.kapa.ai/improving/writing-best-practices)

本文档提供了编写文档的最佳实践，这些实践既能使人类读者受益，也能使AI/LLM系统受益，尤其是在诸如Kapa之类的检索增强生成 (RAG) 系统中。核心原则是清晰、结构良好的文档可以改善AI的回答，反过来，这又揭示了需要进一步改进文档的领域。

本文强调了文档质量的重要性，尤其是在AI系统依赖它来回答用户问题时。AI系统以块的形式处理文档，侧重于内容匹配而不是逻辑文档结构，并且可能会丢失隐含的连接或未声明的信息。因此，文档应明确、自包含且在上下文中完整。

优化内容的关键建议包括：

*   **为网站源使用标准化的语义HTML**。
*   **首选HTML或Markdown**而非PDF，以改进文本提取。
*   **通过简化页面结构来创建对爬虫友好的内容**。
*   **使用描述性标题和有意义的URL来确保语义清晰**。
*   **为视觉效果提供文本等效项**。
*   **保持布局简单**。

本文还讨论了常见的内容设计挑战，例如上下文依赖关系（将关键细节分散在多个部分）、语义可发现性差距（缺少特定术语）、隐含知识假设（假设用户先前的知识）、视觉信息依赖关系（仅依赖图像）和布局依赖信息（依赖视觉布局来表达含义）。它为每个挑战提供了补救措施，重点是将相关信息放在一起，使用一致的术语，包括先决步骤，并为视觉元素提供基于文本的替代方案。

---

## 46. 人工智能编码乐趣减少

**原文标题**: AI coding is less fun

**原文链接**: [https://nicolaiarocci.com/ai-coding-is-less-fun/](https://nicolaiarocci.com/ai-coding-is-less-fun/)

作者探讨了像Claude Code这样的人工智能编码工具对其编程乐趣产生的矛盾影响。虽然人工智能编码在C#/.NET等成熟技术上显著提高了生产力，但它削弱了作者所热爱的沉浸式、解决问题的体验。他们觉得自己不像程序员，更像是一个“策展人”，提示和调整人工智能生成的代码，而不是深入参与创作行为并体验“心流”。

作者呼应了Matheus Lima的担忧，即这种转变可能导致一代高产但脱节的开发者，错失了从亲身编码中获得的内在满足感。尽管作者承认人工智能编码的巨大效用，尤其是在小型团队中，但他担心失去自己的“超能力”——进入深度专注状态并独立解决复杂问题的能力。

最终，作者计划通过有意识地选择在某些项目（尤其是他们维护的开源项目）中放弃人工智能辅助来缓解这个问题。这使他们能够保留沉浸式编码的机会，并在一个日益由人工智能驱动开发的世界中保持对这门手艺的热情。他们认为，在某些情况下有意识地抵制人工智能编码，是保留他们从传统编程中获得的乐趣和满足感的必要策略。

---

## 47. 美国签证新规将要求外国学生解锁社交媒体账号

**原文标题**: New US visa rules will force foreign students to unlock social media profiles

**原文链接**: [https://www.theguardian.com/us-news/2025/jun/18/social-media-student-visa-screening](https://www.theguardian.com/us-news/2025/jun/18/social-media-student-visa-screening)

美国国务院宣布新的签证规定，要求外国学生在获得教育和交流签证前解锁其社交媒体资料以供审查。外交官将寻找对美国公民、文化、政府、机构或建国原则的“敌意”迹象，以及对恐怖主义或反犹太主义的支持。未能解锁社交媒体将引起怀疑。

这些审查针对的是学术、职业教育和文化交流项目的F、M和J签证申请人。国务院官员表示，此举旨在加强国家安全，并由马可·卢比奥牵头。

特朗普政府此前曾暂停发放新的教育签证，同时考虑社交媒体审查策略。美国还在贸易紧张局势中对中国学生进行了审查。

新的指令允许领事馆恢复签证面谈，但要求对所有F、M和J签证申请人进行“全面和彻底的审查”，因此需要将社交媒体隐私设置调整为“公开”。这种加强的审查旨在确保对所有寻求进入美国的人进行适当的筛选。

---

## 48. 用 Rust 重写 Kafka

**原文标题**: Rewriting Kafka in Rust

**原文链接**: [https://wangjunfei.com/2025/06/18/Rewriting-Kafka-in-Rust-Async-Insights-and-Lessons-Learned/](https://wangjunfei.com/2025/06/18/Rewriting-Kafka-in-Rust-Async-Insights-and-Lessons-Learned/)

本文探讨了用 Rust 重写 Kafka 以追求卓越性能和效率的经验教训。作者强调在使用 Rust 的异步功能时，仔细设计和优化至关重要。

主要收获包括：

*   **避免不必要的 `async` 函数：** 仅在真正需要时使用 `async`，因为它们会编译成具有额外开销的状态机。分离同步和异步逻辑以实现更好的控制。

*   **最小化 Tokio 任务：** 过多的任务会导致 CPU 缓存抖动和延迟增加。整合任务并使用异步通道来减少任务数量。作者描述了 StoneMQ 的每个连接一个任务模型，使用共享通道和固定大小的工作线程池来高效地处理请求。监控机制会自动恢复失败的工作线程。

*   **倾向于无锁架构：** 避免使用异步锁 (Tokio Mutex/RwLock)，因为它们会带来性能开销和死锁风险。使用通道进行消息传递和任务所有权管理。当不可避免地需要锁时，使用细粒度的同步锁，并尽可能缩短持有锁的时间，切勿跨越 `.await` 点。

*   **谨慎使用 `unsafe` 代码：** 仅在性能关键路径上使用 `unsafe` 代码，并进行仔细的隔离和彻底的审计。

*   **分离可变和不可变数据：** 通过将需要锁定的可变数据与可以自由访问的不可变数据分开，来优化锁的粒度。

*   **分离异步和同步数据操作：** 通过在运行异步进程之前立即处理必要的同步操作（例如 Mutex 锁写入），来优化锁的使用。

*   **采用静态分发：** 尽可能在性能关键代码中使用枚举 (Enums) 来实现协议类型多态，以避免使用 trait 对象。

作者开发了实用程序类，以便在 StoneMQ 的 Utils 包中使用 `multiple_channel_worker_pool` 和 `single_channel_worker_pool` 模块轻松实现设计。

---

## 49. 编程有害论 (2001)

**原文标题**: Programming Considered Harmful (2001)

**原文链接**: [https://flownet.com/ron/papers/pch.html](https://flownet.com/ron/papers/pch.html)

在《编程有害论》中，Erann Gat认为，目前由程序员和大型公司主导的计算现状，是对个人电脑革命最初精神的一种倒退，在最初的精神中，用户拥有更多的控制权。他批评了程序员和用户之间的鸿沟，导致不可靠的软件盛行，而用户已经被训练成接受这些软件。

Gat认为，对程序员和“程序”的关注是核心问题。他将此追溯到计算机的数学起源，那时人们的重点是实现结果（解决问题），而不是重视过程。他提出要转向一个“无程序世界”，在这个世界里，软件是由小型、互连的“模块”构建而成，而不是大型、独立的应用程序。

在Gat的设想中，用户将组装这些模块来执行任务，从而模糊用户和程序员之间的界限。这些模块将遵守标准化接口，从而允许灵活组合和重用功能。他以Lisp编程语言和Unix管道为例，说明现有的系统已经暗示了这种模块化方法。

他认为，这种模块化系统将带来更高质量的软件，因为用户将更多地参与到创建过程中，并更好地理解软件的工作方式。工程工作将从添加功能转移到优化模块以提高效率，从而产生更强大、更用户友好的软件。他总结说，这种模块化方法会将权力从程序员和公司重新分配给普通用户，从而创造更好的计算体验。

---

## 50. 2025年重温明斯基的《心智社会》

**原文标题**: Revisiting Minsky's Society of Mind in 2025

**原文链接**: [https://suthakamal.substack.com/p/revisiting-minskys-society-of-mind](https://suthakamal.substack.com/p/revisiting-minskys-society-of-mind)

无法访问文章链接。

---

## 51. 公民科学照亮城市之光

**原文标题**: Citizen science illuminates the nature of city lights

**原文链接**: [https://www.nature.com/articles/s44284-025-00239-5](https://www.nature.com/articles/s44284-025-00239-5)

本文探讨了一个名为“Nachtlichter”的公民科学项目，该项目使用移动应用程序统计和分类德国和其他地区的光源，以更好地了解城市光污染。研究人员分析了22平方公里范围内的234044个光源，将地面观测与卫星辐射数据联系起来。

主要发现包括：光源数量与卫星辐射之间存在正相关关系，表明公民科学数据可以将天基观测转化为易于理解的指标。此外，在德国市中心，广告和美学照明超过了街道照明。据估计，德国各地午夜仍有7800万盏灯亮着，突显了缓解潜力。

该研究发现，私人窗户是被观察到的最常见的光源类型，其次是路灯和商业橱窗。光类型分布因土地覆盖而异，广告灯在人口稠密的城市地区占主导地位。大多数德国路灯都具有遮光罩，但其他光源（如泛光灯）通常没有遮光罩，导致向上发光。

这项研究解决了缺乏全面照明清单的问题，并为城市环境保护工作提供了宝贵的数据，为决策者提供关于光污染缓解策略的信息。详细的光源数据对于改进夜空辉光模型以及了解夜间人造光对生态和能源的影响至关重要。

---

## 52. 是的，我会读《尤利西斯》，是的。

**原文标题**: Yes I Will Read Ulysses Yes

**原文链接**: [https://www.theatlantic.com/magazine/archive/2025/07/zachary-leader-richard-ellmann-james-joyce-review/682907/](https://www.theatlantic.com/magazine/archive/2025/07/zachary-leader-richard-ellmann-james-joyce-review/682907/)

本文回顾了理查德·埃尔曼的鸿篇巨制传记《詹姆斯·乔伊斯》及其对文学研究和公众对乔伊斯认知的影响。文章详细描述了埃尔曼如何通过细致的研究和个人魅力，获取关键资料，并创作出一部全面而引人入胜的乔伊斯肖像，从而普及了这位作家及其作品，包括以晦涩难懂著称的《尤利西斯》和《芬尼根的守灵夜》。

随后，文章转向扎卡里·利德的埃尔曼传记《埃尔曼的乔伊斯》，该传记考察了埃尔曼这部杰作的创作过程。文章批评利德的作品缺乏对埃尔曼的动机和学术兴趣的更深入洞察。

文章进一步探讨了埃尔曼的成功在不断发展的文学研究领域中的背景。文章强调了学术扩张时期，这种扩张允许了如此雄心勃勃的项目，并将其与20世纪后期文学理论的兴起进行了对比，后者挑战了传统的传记方法，并将重点从作家的生活转移开来。文章最后感叹了当前文学研究的现状，其日益专业化和普通读者人数的下降，表明埃尔曼的作品代表了一个逝去的时代，当时文学学术研究可以接触到广泛的受众并塑造文化理解。文章最终强调了埃尔曼传记的持久价值，尽管学术趋势发生了变化，但它仍然是进入乔伊斯复杂作品的重要切入点。

---

## 53. 法律即修辞，修辞即法律：文化和社群生活的艺术 (1985) [pdf]

**原文标题**: Law as Rhetoric, Rhetoric as Law: The Arts of Cultural and Communal Life (1985) [pdf]

**原文链接**: [https://www.lwionline.org/sites/default/files/2016-09/v5%20White.pdf](https://www.lwionline.org/sites/default/files/2016-09/v5%20White.pdf)

抱歉，我无法总结文章，因为提供的文本似乎是PDF文件的底层代码，而不是实际的文本内容。要提供摘要，我需要文章的可读文本。

---

## 54. 本田成功进行实验性可重复使用火箭的发射和着陆

**原文标题**: Honda conducts successful launch and landing of experimental reusable rocket

**原文链接**: [https://global.honda/en/topics/2025/c_2025-06-17ceng.html](https://global.honda/en/topics/2025/c_2025-06-17ceng.html)

2025年6月17日，本田技术研究有限公司在日本北海道大树町成功进行了自主研发的实验性可重复使用火箭的发射和着陆测试。这标志着本田在达到近300米高度后，首次成功实现火箭着陆。

此次测试的主要目的是验证火箭可重复使用性的关键技术，包括飞行稳定性和着陆能力。火箭达到271.4米的高度，着陆点与目标点的偏差在37厘米以内，飞行时长为56.6秒。本田在上升和下降阶段收集了宝贵的数据。

本田的火箭研究源于该公司希望利用其核心技术，通过卫星发射和相关服务，为人们的日常生活做出贡献。该公司设想将卫星用于遥感、广域通信和互联移动功能。他们的目标是在2029年实现亚轨道发射能力。

为了确保安全，本田与地方当局和居民合作，实施了限制区域和防止偏离飞行路径的安全系统。本田强调，这项研究仍处于基础阶段，尚未做出商业化决策。

本田全球CEO三部敏宏对测试成功表示高兴，并强调了公司致力于迎接新挑战和创造改善人们生活价值的承诺。他指出，火箭研究利用了本田的技术优势。

---

## 55. Ink and Switch 的 BeeKEM 协议深度解析

**原文标题**: A deep-dive explainer on Ink and Switch's BeeKEM protocol

**原文链接**: [https://meri.garden/a-deep-dive-explainer-on-beekem-protocol/](https://meri.garden/a-deep-dive-explainer-on-beekem-protocol/)

本文深入探讨了Ink and Switch的BeeKEM协议，这是一种为Keyhive项目中的隐私保护、本地优先应用程序设计的关键封装机制。Keyhive利用基于能力的授权和CRDT（无冲突复制数据类型）同步，将数据控制权从中心化服务器转移到个人。

文章重点介绍了加密CRDT操作的挑战，以及传统群组消息协议（如Signal）在处理CRDT固有的并发性方面的局限性。然后，文章介绍了TreeKEM，一种在MLS（消息层安全）中用于高效安全群组消息传递的协议，它利用左平衡二叉树结构进行密钥管理。

文章的核心解释了BeeKEM如何改进TreeKEM，使其更能容忍网络分区和并发更新。与假设状态更新总排序的TreeKEM不同，BeeKEM通过考虑操作的因果上下文来解决冲突。当发生并发更新时（例如，两个成员将用户添加到同一棵树叶中），BeeKEM允许冲突节点上存在多个密钥，直到后续更新解决冲突为止。该系统通过将更新可视化为DAG，即使在冲突节点的情况下也能实现解密，确保使用从并发更新派生的密钥加密的消息仍然可以访问。该系统更新密钥以提供事后泄露安全性，并允许用户即使在离线时也可以更新密钥对。

---

## 56. Show HN: 我用 C++/CUDA 从头构建了一个张量库

**原文标题**: Show HN: I built a tensor library from scratch in C++/CUDA

**原文链接**: [https://github.com/nirw4nna/dsc](https://github.com/nirw4nna/dsc)

“Show HN”帖子介绍：DSC，一个全新的PyTorch兼容张量库及推理框架，完全由C++/CUDA构建。 DSC旨在兼顾易用性和性能，提供类似于NumPy/PyTorch的Python API，并有所改进。

主要特性包括：

*   **直观的API:** 设计与NumPy和PyTorch相似。
*   **内置神经网络支持:** 包含`nn.Module`，方便从PyTorch移植模型。
*   **多种后端:** 支持CPU和CUDA，并计划支持更多后端。 后端切换可通过简单命令完成。
*   **最小依赖项:** CPU操作依赖于可移植的C++，提高可移植性。
*   **自定义内存分配器:** 预先分配内存以避免运行时`malloc()`/`free()`调用，并提供线性分配器选项。

该帖子提供了安装说明，需要兼容C++20的编译器和GNU Make。 用户可以从源代码安装DSC并使用`make`构建C++库，并可选择配置日志记录、优化(`DSC_FAST`)、CUDA支持(`DSC_CUDA`)以及最大张量数量(`DSC_MAX_OBJS`)。

该指南演示了如何通过简单操作验证安装，以及如何启用和验证CUDA后端。 使用pytest的单元测试可用于验证相对于NumPy的正确性。 DSC基于BSD-3-Clause许可证。

---

## 57. 美国农业部果树水彩画

**原文标题**: USDA Pomological Watercolors

**原文链接**: [https://search.nal.usda.gov/discovery/collectionDiscovery?vid=01NAL_INST:MAIN&collectionId=81279629860007426](https://search.nal.usda.gov/discovery/collectionDiscovery?vid=01NAL_INST:MAIN&collectionId=81279629860007426)

此内容描述了美国农业部植物学水彩画集，并表明需要 Javascript 才能与展示该画集的系统交互。因此，该内容并非提供关于画集本身信息的文章，而是一则关于访问和观看水彩画的简短通知。

总而言之，这篇短文是一个通知，声明在线访问美国农业部植物学水彩画集需要启用 Javascript。它不提供关于画集本身、其历史或其意义的任何信息。它仅涉及观看这些图像的技术要求。

---

## 58. 拉丁字母可视历史

**原文标题**: Visual History of the Latin Alphabet

**原文链接**: [https://uclab.fh-potsdam.de/arete/en](https://uclab.fh-potsdam.de/arete/en)

拉丁字母视觉史：从古代到现代的拉丁字母发展时间线，展示了字母形式的演变及其与文化、社会和技术的联系。

时间线从古拉丁文开始，逐步展示各种罗马字体（纪念碑体、乡村大写体、罗马草书）和中世纪地区字体（安色尔字体、半安色尔字体、卡洛林小写体、哥特体）。然后过渡到文艺复兴时期，展示人文主义和文艺复兴字体，随后是巴洛克和古典主义风格。最后，它到达现代字体，包括无衬线字体、粗衬线字体和手写风格。

每种字体都附有示例和进一步信息的链接。重要的是，该时间线整合了历史背景，突出了罗马帝国衰落、大学兴起、印刷机发明、宗教改革、启蒙运动和工业革命等事件的影响。 诸如造纸、钢笔尖、自来水笔、轮转印刷、照相排版和数字字体等技术进步被证明对字母形式和书写实践产生了重大影响。 时间线最后以万维网作为一项重要的技术进步的影响作结。

该视觉历史成功地将拉丁字母的演变与重大的历史和文化变革联系起来，强调了技术创新与社会变革之间的相互作用。

---

## 59. Framework Laptop 12 评测

**原文标题**: Framework Laptop 12 review

**原文链接**: [https://arstechnica.com/gadgets/2025/06/framework-laptop-12-review-im-excited-to-see-what-the-2nd-generation-looks-like/](https://arstechnica.com/gadgets/2025/06/framework-laptop-12-review-im-excited-to-see-what-the-2nd-generation-looks-like/)

评测：Framework Laptop 12
这款评测审视了 Framework Laptop 12，它是 Framework 系列模块化、可修复和可升级笔记本电脑的最新产品。Laptop 12 以其色彩鲜艳的塑料外壳脱颖而出，与采用金属外壳的 Laptop 13 和 16 相比，提供了更平易近人的设计。它保留了 Framework 的标志性功能，包括可定制的端口（扩展卡）、易于维修、Linux 支持以及未来升级的潜力。

虽然塑料结构坚固耐用且具有有趣的颜色选项，但存在一些妥协。 12.2 英寸触摸屏亮度很高，但边框很厚，色域也很普通。 键盘虽然功能齐全，但缺少背光和用于生物识别的指纹传感器。

在内部，Laptop 12 专为使用 Framework 随附的螺丝刀轻松进行维修和升级而设计。但是，它使用较小的主板，只有一个 RAM 插槽（限制容量和内存带宽）和较短的 M.2 2230 SSD。

得益于其第 13 代英特尔酷睿处理器，其性能对于基本计算来说是体面的，但落后于较新的芯片，并且不适合游戏或要求苛刻的任务。电池续航时间令人满意，在测试中持续约 10 小时。

最大的问题是价格。DIY 版起价超过 1100 美元，Laptop 12 与 MacBook Air 和 Surface Laptop 等功能更强大的笔记本电脑竞争，同时提供的用户体验却不那么精致。它的魅力和可修复性是强项，但削减成本的妥协使其与包括 Framework Laptop 13 在内的替代产品相比，很难推销。

---

## 60. 经过数百万年，为什么食肉植物仍然如此矮小？

**原文标题**: After millions of years, why are carnivorous plants still so small?

**原文链接**: [https://www.smithsonianmag.com/articles/carnivorous-plants-have-been-trapping-animals-for-millions-of-years-so-why-have-they-never-grown-larger-180986708/](https://www.smithsonianmag.com/articles/carnivorous-plants-have-been-trapping-animals-for-millions-of-years-so-why-have-they-never-grown-larger-180986708/)

本文探讨了食肉植物的进化历史和对其大小的限制。虽然虚构故事中经常出现巨大的、吃人的植物，但真正的食肉植物仍然相对较小。最古老的食肉植物化石可以追溯到 3400 多万年前，表明植物的食肉性是一种古老的适应性。

本文重点介绍了食肉植物使用的各种捕获机制，例如粘性叶子（茅膏菜）、捕捉陷阱（维纳斯捕蝇草）和壶状结构。这些适应性的进化是因为食肉植物通常栖息在营养贫乏的环境中，这使得动物猎物成为重要的营养来源。

尽管经过数百万年的进化，食肉植物并没有长到足以吞噬人类。本文将此归因于几个因素。首先，较大的植物需要更肥沃的土壤，从而否定了食肉的必要性。其次，捕获大型动物的生物力学将是困难且耗能的。此外，已经在营养丰富的环境中的植物将不会从食肉中受益。

已知最大的食肉植物*Triphyophyllum peltatum*是一种巨大的藤蔓，但仅在其早期阶段是食肉的。虽然一些猪笼草可以捕获小型脊椎动物，但它们仍然远未达到虚构的食人植物的大小。最终，本文得出结论，食肉植物之所以小，是因为它们的大小是由其营养贫乏的栖息地的特定挑战和限制决定的，并且它们已经通过利用独特的生态位而蓬勃发展。

---

## 61. Demento博士宣布在55年电台生涯后退休

**原文标题**: Dr. Demento Announces Retirement After 55-Year Radio Career

**原文链接**: [https://sopghreporter.com/2025/06/01/dr-demento-announces-retirement/](https://sopghreporter.com/2025/06/01/dr-demento-announces-retirement/)

以幽默和另类音乐著称的电台名人“癫狂博士”迪门托宣布退休，结束其55年的职业生涯。84岁的巴雷特·汉森宣布他的最后一期常规节目已经播出，但回顾特辑将持续到十月，最终以节目历史上最受欢迎的40首歌曲的最终广播达到高潮。

“癫狂博士”迪门托于1970年首次亮相，并在洛杉矶的几个电台获得人气，之后于1974年开始联合播出。该节目随着技术的发展而演变，从卷盘录音带转向在线流媒体。汉森对另类音乐的热情始于斯派克·琼斯，并促使他积累了超过30万张专辑的收藏。

该节目向观众介绍了独特且经常被忽视的喜剧歌曲和音乐怪癖。值得注意的是，他被认为是“怪人奥尔”扬科维奇的伯乐。最受欢迎的歌曲包括《鱼头》和《死狗不好玩》。

“癫狂博士”迪门托于2009年入选广播名人堂。剩余的剧集将以十年为单位进行回顾并播放听众点播。1974年以后的往期节目可在该节目的网站上找到。

---

## 62. 大型模型实时动作分块

**原文标题**: Real-time action chunking with large models

**原文链接**: [https://www.pi.website/research/real_time_chunking](https://www.pi.website/research/real_time_chunking)

本文介绍了一种名为实时分块(RTC)的新型算法，该算法旨在使视觉-语言-动作(VLA)模型能够在机器人上实时运行。 目前的VLA模型虽然前景广阔，但存在推理速度慢的问题，尤其是在边缘设备上部署时，由于网络延迟更是如此。这种延迟会导致性能下降和不安全的机器人行为。

RTC通过允许机器人通过动作分块在执行先前动作的同时“思考”未来的动作来解决这个问题。该算法将动作块之间切换时出现的不连续性问题定义为一个“修复”问题。 RTC“冻结”新块的初始动作，使其与先前块已执行的动作相匹配，然后使用剩余动作进行部分注意力，以保持策略一致性，同时允许基于新信息进行更新。 这一切无需对现有模型进行任何重新训练即可实现。

本文证明，与同步推理方法相比，RTC显著提高了执行速度并提高了精度。 实验表明，RTC对高推理延迟（高达300毫秒）具有鲁棒性，并且在诸如划火柴或插入以太网电缆之类的动态任务中表现出色。研究人员强调，RTC通过消除暂停来克服同步方法固有的局限性，从而实现更自然，更高效的机器人性能。 他们认为，随着VLA模型复杂性的不断增长，RTC为更复杂的实时推理机制奠定了基础。

---

## 63. A*算法入门 (2014)

**原文标题**: Introduction to the A* Algorithm (2014)

**原文链接**: [https://www.redblobgames.com/pathfinding/a-star/introduction.html](https://www.redblobgames.com/pathfinding/a-star/introduction.html)

本文介绍了A*寻路算法及其相关算法，解释了它们的工作原理以及何时使用每种算法。文章首先解释了寻路算法在图上找到最短路径，该图将地图表示为位置（节点）和连接（边）。

文章探讨了广度优先搜索、Dijkstra算法和A*算法，突出了它们的区别。广度优先搜索在所有方向上平等地探索，Dijkstra算法考虑了不同的移动成本，而A*算法则使用启发式方法将探索重点放在目的地。

广度优先搜索使用队列来管理要探索的节点边界，从起点向外扩展。Dijkstra算法在此基础上进行了改进，使用基于到达节点的成本的优先级队列，从而允许可变的移动成本。A*算法通过结合估计到目标距离的启发式函数来增强Dijkstra算法，引导搜索朝着目的地前进。

文章展示了Python代码片段，演示了每种算法的核心逻辑。它还解释了图设计的权衡（例如，网格与非网格），并提供了选择适当算法的指南：广度优先搜索适用于统一成本并查找到达所有位置的路径，Dijkstra算法适用于可变成本并查找到达所有位置的路径，A*算法适用于单目的地寻路，并在启发式方法不高估的情况下提供最佳路径。

---

## 64. Haskell周刊 第477期

**原文标题**: Haskell Weekly Issue 477

**原文链接**: [https://haskellweekly.news/issue/477.html](https://haskellweekly.news/issue/477.html)

本期Haskell周刊第477期重点介绍了Haskell社区的几项激动人心的发展和资源。它包括使用Esqueleto进行复杂数据库查询的教程，并介绍了使用Haskell进行竞争性编程。GHCi迎来一项重大改进：9.14.1版本全面支持多个主单元。

本期还收录了富有洞察力的博客文章，讨论了具体示例在学习Monad中的重要性，并探讨了“双指针算法”问题。Magnus Therning解释了他编写新的Redis客户端软件包的动机，Tristan de Cacqueray分享了他在ZuriHac 2025的经验。

其中列出了几个Haskell工程师的职位机会，包括欧洲的远程职位和乌得勒支的混合职位。

简而言之，Stack 3.7.1 正处于候选发布阶段，一个用于在LaTeX文档中运行GHCi会话的工具（ghci4luatex）被介绍，并且Haskell基金会2025年5月的DevOps月度日志也被分享。Servant团队正准备发布一个主要版本0.21.0.0。

一个专为患有ADHD的成年人设计的Haskell后端应用程序被展示。最后，宣布了对慕尼黑Munihac 2025的参与邀请。

---

## 65. MiniMax-M1开放权重、大规模混合注意力推理模型

**原文标题**: MiniMax-M1 open-weight, large-scale hybrid-attention reasoning model

**原文链接**: [https://github.com/MiniMax-AI/MiniMax-M1](https://github.com/MiniMax-AI/MiniMax-M1)

MiniMax-M1：首个开源重量级大规模混合注意力推理模型。它基于 MiniMax-Text-01 模型构建，拥有 4560 亿参数，每个 token 激活 459 亿参数，并支持 100 万 token 的上下文长度。其闪电注意力机制能够实现高效的测试时计算缩放，与 DeepSeek R1 等模型相比，消耗的 FLOPs 显著减少。

该模型使用大规模强化学习 (RL) 在各种任务上进行训练，包括数学和软件工程。一种新型 RL 算法 CISPO 被引入，以提高训练效率，同时优化了混合架构下 RL 的缩放。提供两个版本，分别使用 4 万和 8 万的思考预算进行训练。

基准测试结果表明，MiniMax-M1 在软件工程、工具使用和长文本理解等复杂任务上优于其他开源模型。该文档提供了数学、通用编码、推理与知识、软件工程、长文本和 Agentic 工具使用等类别的详细性能指标。

文章提供了模型使用建议，特别是针对不同场景建议了推理参数（Temperature: 1.0, Top_p: 0.95）和系统提示定制。提供了 vLLM 和 Transformers 的部署指南。该模型还支持函数调用。提供了一个聊天机器人、API 和 MiniMax MCP Server，用于通用使用和评估。

---

## 66. “模型是正确的”：天文学家发现“丢失的”物质

**原文标题**: "The models were right": astronomers find 'missing' matter

**原文链接**: [https://www.esa.int/Science_Exploration/Space_Science/XMM-Newton/The_models_were_right_astronomers_find_missing_matter](https://www.esa.int/Science_Exploration/Space_Science/XMM-Newton/The_models_were_right_astronomers_find_missing_matter)

天文学家发现了连接沙普利超星系团内四个星系团的巨大热气体丝，该星系团包含超过8000个星系。这根气体丝的质量是银河系的10倍，延伸达2300万光年，可能包含宇宙中大量“缺失”的物质——即构建宇宙学模型所需的，但此前未被探测到的“普通”物质。

研究人员利用欧洲航天局的XMM-牛顿和日本宇宙航空研究开发机构的朱雀X射线空间望远镜，识别并描述了这根气体丝内热星系际气体发出的微弱X射线光。XMM-牛顿的精确度使其能够移除诸如超大质量黑洞等具有干扰性的X射线源，确保他们观测的是气体本身。

这项发现意义重大，因为它与领先的宇宙学模拟的预测高度一致，验证了数十年的理论研究。它还提供了对宇宙网的洞察，宇宙网是被认为构成宇宙结构基础的巨大丝状网络。这项研究突显了星系团如何在遥远的距离上相互连接。

该发现也为未来寻找这些微弱气体丝提供了一个基准，并巩固了宇宙的标准模型。欧洲航天局于2023年发射的欧几里得任务将继续探索宇宙网以及暗物质和暗能量的本质，从而进一步解决宇宙中一些最大的谜团。

---

## 67. Scrappy – 为你和你的朋友们制作小应用

**原文标题**: Scrappy – Make little apps for you and your friends

**原文链接**: [https://pontus.granstrom.me/scrappy/](https://pontus.granstrom.me/scrappy/)

Scrappy被定位为一种研究原型工具，用于创建“自制软件”——简单、定制化的应用程序，专为朋友和家人之间的个人使用而设计，而非面向大众市场或企业解决方案。作者John和Pontus设想一个任何人都可以轻松创建和修改软件以适应其特定需求的世界。

Scrappy提供类似于Figma或Miro的无限画布界面，用户可以在其中拖放交互式对象，并使用Javascript代码附加行为。其主要功能包括共享、持久、多人环境，应用程序“始终在线”，并且像Google Docs一样易于通过链接共享。文章展示了诸如与会者计数器、会议成本时钟和家务追踪器等示例。

Scrappy背后的动机源于 democratize 软件创建并赋予最终用户权力，其灵感来自Notion和HyperCard等工具。目标用户是“DIY爱好者”，他们希望创建定制应用程序，而无需传统编程的复杂性。

文章列举了各种潜在的Scrappy想法，强调了适合与朋友共享、需要调整、涉及计算并且受益于最小摩擦的问题。它将Scrappy与大众市场应用程序进行对比，突出了定制、协作和数据所有权的优势。最后，文章认为Scrappy在可理解性、协作性和用户控制方面优于AI生成的应用程序。

---

## 68. 叠加推理：对持续性链式思考的视角

**原文标题**: Reasoning by Superposition: A Perspective on Chain of Continuous Thought

**原文链接**: [https://arxiv.org/abs/2505.12514](https://arxiv.org/abs/2505.12514)

通过叠加推理：关于连续思维链的理论视角

本文《通过叠加推理：关于连续思维链的理论视角》探讨了在推理任务中，特别是对于有向图可达性问题，连续思维链(CoTs)为何优于离散CoTs。作者证明，使用*连续*CoTs的两层Transformer可以在*D*步内解决有向图可达性问题，其中*D*是图的直径。这与使用*离散*CoTs的固定深度Transformer所需的*O(n^2)*解码步骤形成对比，其中*n*是顶点数量。

核心论点是，连续CoTs利用“叠加状态”，其中每个思维向量同时编码多个搜索前沿，有效地执行并行广度优先搜索(BFS)。另一方面，离散CoTs被迫从这种叠加状态中采样单个路径，导致顺序搜索容易陷入局部最优，需要更多步骤。

本文通过实验结果支持了这一理论分析，表明训练连续CoTs会导致自动涌现基于叠加的多个搜索路径的编码，即使没有明确的监督。该研究为理解连续CoTs在图推理中的有效性提供了理论基础，并表明它们的优势在于能够同时探索多种可能性。这项研究有助于理解LLM的推理能力，并表明连续表示在复杂推理任务中具有潜在优势。

---

## 69. 多面体查看器

**原文标题**: Polyhedra Viewer

**原文链接**: [https://polyhedra.tessera.li/](https://polyhedra.tessera.li/)

“多面体查看器”仅是标题，内容重复标题，没有实际文章内容。假定存在文章，则“多面体查看器”软件可用于可视化和交互操作多面体。功能可能包括：

*   **可视化：**显示各种多面体的3D模型，包括正多面体、半正多面体和非正多面体。
*   **操作：**旋转、缩放和平移多面体，以便从不同角度查看。
*   **属性：**显示关于多面体的信息，如面数、顶点数和边数，以及其体积和表面积。
*   **构造/修改：**可能允许用户创建新的多面体或修改现有的多面体，例如添加顶点、边或面。
*   **文件格式支持：**能够导入和导出各种标准文件格式（例如，OBJ，STL）的多面体模型。
*   **应用：**用于教育（教授几何）、设计（建筑建模）和研究（数学可视化）。

在没有更多信息的情况下，这仍然是一个高度推测性的总结。

---

## 70. Show HN: Gifty – 用你的双脚玩转真实世界的寻宝游戏

**原文标题**: Show HN: Gifty – A real-world gift hunt you play with your feet

**原文链接**: [https://gifty-en.vercel.app/](https://gifty-en.vercel.app/)

Gifty：一款免费寻宝应用，将您的日常步行变成激动人心的冒险，通过奖励您城市中隐藏的真实礼品。该应用会显示一张地图，上面标明了这些数字礼品的位置，其中包括免费咖啡、折扣和其他惊喜。

用户只需打开地图，探索周围环境，并实际走到礼品所在位置即可自动解锁，无需二维码或额外安装。该应用强调易用性和惊喜感，每天提供不同的礼品。

要参与，用户需浏览地图查找可用礼品，导航至礼品位置，并解锁它。该应用完全免费，没有垃圾邮件或隐藏陷阱。用户可以期待获得各种奖励，例如免费饮品或折扣。“常见问题”部分解答了有关应用功能、奖励和可访问性的常见问题。

---

## 71. 本地托管互联网连接的服务器

**原文标题**: Locally hosting an internet-connected server

**原文链接**: [https://mjg59.dreamwidth.org/72095.html](https://mjg59.dreamwidth.org/72095.html)

该短文片段描述了一个系统，该系统使用验证码（CAPTCHA）来验证本地托管、联网服务器上的用户请求。验证码的目的是区分人类用户和自动机器人。消息表明用户是“半随机”选择进行检查的，这意味着对验证码的实施采用了一种选择性或速率限制的方法，而不是对每个请求都普遍应用。该文本直接指示用户完成验证码并提交。

---

## 72. 人工智能代理的成功率有半衰期吗？

**原文标题**: Is there a half-life for the success rates of AI agents?

**原文链接**: [https://www.tobyord.com/writing/half-life](https://www.tobyord.com/writing/half-life)

托比·奥德的文章探讨了人工智能体在研究工程任务中的成功率，重点关注Kwa等人(2025)的实证研究结果。奥德提出了一个简单的数学模型：每分钟人类任务时间内存在一个恒定的失败率，导致成功率呈指数下降，类似于具有半衰期的放射性衰变。这个“半衰期”代表人工智能体具有50%成功率的任务时长。

文章强调了METR的研究发现，即人工智能可以可靠解决的任务长度每7个月翻一番，但强调高成功率（80％，99％）的时间范围要短得多。奥德的恒定风险率模型预测了这些关系，表明80％成功率的时间范围约为50％成功率的1/3。

该模型提供了一个预测不同阈值成功率的框架，表明对于给定的任务长度，将成功率从50％提高到99％将滞后数年。文章还将该模型与替代解释进行了比较，例如拟合对数-logistic函数，并探讨了可能偏离指数衰减的情况，这可能揭示人工智能体行为的见解。

虽然承认METR任务套件的局限性，但奥德认为该模型为人工智能体失败的根本原因提供了有价值的见解，表明任务由连续的子任务组成，其中任何一个子任务的失败都会导致整体失败。他讨论了“无记忆”分布的含义，即失败概率与进度无关，并呼吁进一步研究以比较人类和人工智能在任务长度上的缩放行为。

---

## 73. Terpstra 键盘

**原文标题**: Terpstra Keyboard

**原文链接**: [http://terpstrakeyboard.com/web-app/keys.htm](http://terpstrakeyboard.com/web-app/keys.htm)

Terpstra键盘WebApp是实体Terpstra键盘的数字化版本，该键盘最初由Siemen Terpstra在20世纪80年代末设计。此WebApp由James Fenn开发，Brandon Lewis、Bo Constantinsen和Chengu Wang提供了贡献和修改。Scott Thompson和Ozan Yarman博士因提供应用内使用的样本而获得赞誉。此WebApp以GPL-3.0许可发布，属于自由/开源软件，欢迎用户通过在GitHub上修复问题和实现新功能来下载、派生并为其开发做出贡献。当前版本1.5.2涵盖了2015年1月至2019年5月的开发成果。

---

## 74. 格鲁格脑开发者 (2022)

**原文标题**: The Grug Brained Developer (2022)

**原文链接**: [https://grugbrain.dev/](https://grugbrain.dev/)

Grug脑开发员"以一种幽默的方式，从简化的、外行的角度呈现了软件开发原则。其核心信息是使用“不”这个魔法词来对抗复杂性（“永恒的敌人”），优先考虑简单性和可维护性，而不是过度的抽象。

Grug提倡实用的、80/20的解决方案，通常优先考虑完成工作，而不是完美地遵守流程。他强调逐步分解代码，让系统的结构有机地涌现出来，而不是过早地强加抽象。

测试至关重要，但Grug更喜欢集成测试（“中间测试”），而不是僵化的单元测试或脆弱的端到端测试。他以谨慎的怀疑态度看待敏捷方法论，警告不要盲目遵守流程和“敏捷巫师”。重构是有益的，但应谨慎和逐步进行，以避免引入更多问题。

Grug重视在进行大规模更改之前理解现有代码的重要性（“切斯特顿的栅栏”），并质疑微服务的使用。他赞扬工具的重要性，特别是具有代码完成和调试器的IDE。类型系统主要因其代码完成功能而受到青睐。文章警告不要采取过于理论化或抽象的开发方法，优先考虑实际解决方案和可维护性。总而言之，Grug强调软件开发中的实用主义和简单性。

---

## 75. 我用机器学习数了蒙古所有的蒙古包。

**原文标题**: I counted all of the yurts in Mongolia using machine learning

**原文链接**: [https://monroeclinton.com/counting-all-yurts-in-mongolia/](https://monroeclinton.com/counting-all-yurts-in-mongolia/)

本文详细介绍了作者使用机器学习统计蒙古所有蒙古包（蒙古语称ger）的旅程。受听完一个关于蒙古帝国的播客后的好奇心驱使，作者旨在量化当代蒙古社会的一个独特方面。

作者在没有机器学习经验的情况下，概述了一个三步计划：训练一个模型来识别蒙古包，通过关注人口稠密地区来缩小输入空间，并追踪找到的蒙古包。他们使用谷歌地图的卫星图像和Label Studio手动标注了数千个蒙古包，为模型创建训练数据。

作者选择了Ultralytics的YOLO11进行目标检测，因为它具有开源性、易于设置、速度快以及良好的默认设置。在最初的模型准确性问题之后，作者通过使用Overpass Turbo识别人类居住地来缩小搜索范围，并将切片搜索集中在一个更小、更相关的区域。

为了加快标注速度，作者使用 FastAPI 构建了一个模型后端，将训练好的模型与 Label Studio 集成，从而允许模型预测蒙古包的位置并简化标注过程。随着标注数据的增长，vast.ai 被用于租用 GPU 以加快模型训练速度。训练过程使用 Docker 进行容器化并部署到 vast.ai，训练好的模型和元数据上传到 S3 以进行监控和检索。

最后，Docker Swarm 被用于协调跨多个服务器的部署。

---

## 76. 贝塞斯达宣言

**原文标题**: The Bethesda Declaration

**原文链接**: [https://www.science.org/content/blog-post/bethesda-declaration](https://www.science.org/content/blog-post/bethesda-declaration)

无法访问文章链接。

---

## 77. 使用流式SQL查询构建代理

**原文标题**: Building agents using streaming SQL queries

**原文链接**: [https://www.morling.dev/blog/this-ai-agent-should-have-been-sql-query/](https://www.morling.dev/blog/this-ai-agent-should-have-been-sql-query/)

本文对比了传统SQL数据库查询与流式查询系统。传统SQL采用“拉取”模型，对数据集执行查询并返回完整结果集。而流式查询系统则采用“推送”模型，持续运行查询并增量更新结果。

核心区别在于数据变更的处理方式。在传统SQL中，任何数据修改都需要重新运行整个查询。在流式SQL中，仅处理受更改影响的数据，并且仅将结果集中的相应增量（差异）推送给客户端。

这使得查询结果能够进行实时或近实时更新，从而使流式SQL系统适用于需要对数据更改立即做出响应的应用程序。客户端不再重复查询整个数据集，而是仅接收必要的更新，从而为动态数据环境提供了一种更高效的方法。这对于构建需要快速响应变化情况的代理尤其重要。

---

## 78. OpenSERDES – 开源硬件串行器/解串器 (SerDes)，Verilog (2020) 实现

**原文标题**: OpenSERDES – Open Hardware Serializer/Deserializer (SerDes) in Verilog (2020)

**原文链接**: [https://github.com/SparcLab/OpenSERDES](https://github.com/SparcLab/OpenSERDES)

OpenSERDES 是一个开源的硬件串行器/解串器 (SerDes)，用 Verilog 实现，用于高速通信。 SerDes 将并行数据转换为串行数据进行传输，并在接收端将其转换回并行数据，这对于 LVDS 等技术至关重要。该项目利用 Skywater OpenPDK 130nm 工艺节点和 OpenLane 进行综合，以及 Virtuoso Cadence。

该项目包括用于串行器和解串器模块的综合 Verilog 代码、GDS、SPICE 和网表文件。 发送器 (TX) 使用 CMOS 反相器链来驱动通道的输入电容。 接收器 (RX) 具有电阻反馈反相器，用于感应微弱信号，随后是 CMOS 反相器，用于增益，以及 D 触发器 (DFF)，用于采样数据。 DFF 使用 NAND 逻辑门实现。 实现了一个过采样时钟数据恢复 (CDR) 电路，以从接收到的信号中恢复时钟，以确保正确的数据解码。 CDR 使用数据转换来调整时钟频率。 每个组件（包括反相器链、电阻反馈反相器、DFF、NAND 门和 CDR）的实现细节都在单独的文件夹中提供。

---

## 79. 大型语言模型给领域特定语言（DSL）设计者带来了一个有趣的问题。

**原文标题**: LLMs pose an interesting problem for DSL designers

**原文链接**: [https://kirancodes.me/posts/log-lang-design-llms.html](https://kirancodes.me/posts/log-lang-design-llms.html)

本文探讨了大型语言模型（LLM）对领域特定语言（DSL）设计的影响。作者认为，LLM，尤其是其在 Python 等语言上的熟练程度，对 DSL 构成了挑战。由于 LLM 在小众语言上的表现不佳，现在使用 DSL 可能意味着会牺牲 LLM 生成代码的优势。 这提高了 DSL 的入门门槛，要求它们提供显著的优势，以证明放弃 LLM 协助是值得的。

尽管存在这一挑战，作者仍然保持乐观，并为 LLM 时代的语言设计提出了三个潜在方向：

1.  **教 LLM 学习 DSL：** 通过为 LLM 提供上下文，可能通过 DSL 语义的 Python 描述，可以利用 LLM 为 DSL 生成代码，而无需进行大量的微调。这涉及创建 DSL 设计框架，其中还包括对其语义的 LLM 友好的 Python 描述。
2.  **利用 LLM 在 DSL 中桥接形式化和非形式化：** 探索将基于 LLM 的编码工作流程集成到 DSL 设计中的方法，通过利用 LLM 处理“胶水代码”，而开发人员则专注于核心逻辑。这涉及弥合形式化代码和非形式化文本之间的差距，可能通过基于 DSL 类型和分析自动生成自然语言规范。
3.  **为经验证的 LLM 合成而进行语言设计：** 设计可用于验证 DSL 中 LLM 生成的代码输出的规范语言。这涉及将规范集成到 DSL 中，并定制验证 DSL 以捕获特定于领域的属性。

作者总结说，虽然 LLM 提出了重大挑战，但它们也为 DSL 设计人员探索开辟了新的有趣问题。 为了避免停滞不前，语言设计必须适应这种新的局面。

---

## 80. 展示HN：用于即时分享代码片段的VS Code扩展

**原文标题**: Show HN: VS Code extension to share code snippets instantly

**原文链接**: [https://snippetshare.dev](https://snippetshare.dev)

SnippetShare 是一款 VS Code 扩展，旨在轻松共享、发现和管理代码片段。它旨在通过实现代码片段的无缝协作来提高团队生产力。

其核心功能允许用户在 VS Code 中高亮显示代码，并使用快捷键 CTRL+ALT+S（Windows/Linux）或 ⌘+⌥+S（Mac）立即生成可共享的链接。此链接会自动复制到剪贴板，方便共享。

该扩展可以通过多种方式安装：直接从 VS Code Marketplace 安装，通过 VS Code 命令行使用 `ext install snippetsharedev.snippet-share` 安装，或者通过高亮显示代码后使用快捷键安装。

描述强调了与现有 VS Code 工作流程的轻松集成，突出了与同事共享代码片段的速度和便利性。它还提到了其发现和管理片段的实用性，暗示了比仅仅共享更广泛的功能集，尽管所提供的内容中未详细说明这些功能的具体细节。

---

## 81. 基于图变换器的时序预测

**原文标题**: Time Series Forecasting with Graph Transformers

**原文链接**: [https://kumo.ai/research/time-series-forecasting/](https://kumo.ai/research/time-series-forecasting/)

这篇博客探讨了图结构数据上的时间序列预测，特别是使用关系深度学习 (RDL) 从关系数据库中导出的数据。核心思想是利用图中不同实体之间的关系来提高与特定节点相关的时间序列的预测准确性（例如，基于客户和营销数据预测产品销售额）。

所提出的框架使用图Transformer来编码图结构和节点特征，并结合序列编码器（例如，CNN）来处理过去的时间序列数据。日期时间和日历编码提供时间上下文。统一的预测头随后整合所有这些信息以预测未来值。使用时间邻域采样器提取实体周围的相关子图，以实现扩展。

该文章讨论了两种预测范式：预测式（回归）和生成式。回归模型效率很高，但可能会遭受均值坍塌。生成式预测，特别是使用条件扩散模型，提供了一种概率方法，该方法对未来值的分布进行建模，允许采样并比回归更好地捕获高频细节和罕见事件。对商店访问预测的实验表明，与简单的回归和 Facebook Prophet 相比，生成模型具有捕获更细微模式的潜力。

作者推荐使用 Pytorch Geometric 库和 RelBench，以便实际实施和评估基于图的时间序列预测。

---

## 82. 我感觉开源已经变成了两个世界。

**原文标题**: I feel open source has turned into two worlds

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/tech/OpenSourceTwoWorlds](https://utcc.utoronto.ca/~cks/space/blog/tech/OpenSourceTwoWorlds)

由于大量爬虫涌入，其中许多是为了收集LLM训练数据，Wandering Thoughts的作者Chris Siebenmann正在阻止使用旧版浏览器的用户访问他的博客。这些爬虫经常使用过时的Chrome用户代理，难以与合法用户区分。他采取了这项反爬虫措施，以减轻服务器的负载。

如果使用最新浏览器的用户被阻止，他们可以通过大学邮箱（可从他的隶属关系获取）联系他，并提供浏览器详细信息，包括User-Agent字符串。

作者特别指出archive.today、archive.ph和archive.is的用户，解释说这些存档服务的行为与恶意爬虫类似。它们旧的Chrome User-Agent值、广泛分布的IP地址和伪造的反向DNS条目（声称是Googlebot）使它们与不良行为者无法区分。他建议改用archive.org，因为它是一个行为更好的爬虫，可以访问他的博客。本质上，Siebenmann正在通过过滤掉可疑的爬虫活动来优先考虑合法用户的访问，即使这可能会无意中阻止一些合法的存档服务。

---

## 83. Show HN: Trieve CLI – 用于PDF的带搜索工具的基于终端的LLM代理循环

**原文标题**: Show HN: Trieve CLI – Terminal-based LLM agent loop with search tool for PDFs

**原文链接**: [https://github.com/devflowinc/trieve/tree/main/clients/cli](https://github.com/devflowinc/trieve/tree/main/clients/cli)

"Show HN: Trieve CLI" 帖子介绍了一个名为 Trieve 的命令行界面 (CLI) 工具，它使用户能够直接从终端创建和与 LLM (大型语言模型) 代理循环进行交互。 其核心功能围绕专门为 PDF 设计的搜索工具展开，使 LLM 代理能够访问和利用这些文档中包含的信息。

本质上，Trieve CLI 使用户能够在终端环境中构建智能代理。 这些代理可以利用 PDF 搜索功能从 PDF 文档中提取相关信息，并使用该信息来回答问题、生成内容或执行其他任务。

主要方面包括：

*   **基于终端：** 整个交互发生在终端内，提供了一个精简高效的工作流程。
*   **LLM 代理循环：** 该工具支持创建和利用 LLM 代理，从而实现迭代推理和任务执行。
*   **PDF 搜索：** 专门的搜索工具允许代理访问和处理来自 PDF 文件的数据。
*   **公共存储库：** 该项目是开源的，可在 GitHub 上以用户名 "devflowinc/trieve" 找到。
*   **受欢迎程度：** 该存储库已引起广泛关注，拥有 201 个 fork 和 2.3k 个星标，表明开发人员社区对此有浓厚的兴趣。

简而言之，Trieve CLI 提供了一种强大且易于访问的方式来构建基于终端的 LLM 代理，这些代理能够搜索和利用来自 PDF 文档的信息。

---

## 84. 与Liberux关于其欧盟制造的开源硬件Linux手机的访谈

**原文标题**: An interview with Liberux about their made-in-EU OSHW Linux Phone

**原文链接**: [https://linmob.net/liberux-nexx-an-interview-with-liberux/](https://linmob.net/liberux-nexx-an-interview-with-liberux/)

Liberux 为 Nexx 发起众筹，这是一款在欧洲设计和制造的 Linux 手机，专注于用户自由和数字自主。 Nexx 拥有令人印象深刻的规格，包括高达 32GB 内存、512GB 存储、5G、双 USB-C 端口、耳机插孔和模块化组件（调制解调器、内存、存储）。

采访突出了 Liberux 的动机：对监控的担忧以及对主流移动操作系统缺乏控制。他们的团队在硬件、软件和制造方面拥有经验，并与 Pleeda 和 Collabora 等公司合作。他们的目标是避免之前 Linux 手机项目（如 PinePhone 和 Librem 5）的陷阱，提供一款既可日常使用又具有高制造质量的设备，同时采取措施实现开源硬件。

与 Android 手机相比，更高的价格归因于优质组件、欧洲制造以及对透明度的承诺。选择 RockChip RK3588s 是因为它具有 Linux 兼容性以及通过物理开关隔离 5G 调制解调器的能力。双 USB-C 端口支持充电、配件以及通过 DisplayPort 输出的桌面使用。可更换的 5G 调制解调器和 Wi-Fi/蓝牙物理开关优先考虑用户控制。

基于 Debian 13 的 LiberuxOS 旨在实现道德和主要开源，并尽可能减少不可避免的固件 blobs。他们将采用裸机 Linux 方法，向上游贡献。他们选择 GNOME Shell Mobile 是因为其定制潜力，并且正在努力改善其移动体验。鼓励通过代码贡献、口头宣传和捐款来参与社区。

---

## 85. 无字证明

**原文标题**: Proofs Without Words

**原文链接**: [https://artofproblemsolving.com/wiki/index.php/Proofs_without_words](https://artofproblemsolving.com/wiki/index.php/Proofs_without_words)

这篇美国解题网站(AoPS)维基页面展示了“无字证明”，即一系列用视觉方式演示数学恒等式和定理的方法。它提供了多个主题的证明，主要分为求和、几何和杂项。

求和部分包括奇数自然数之和、正整数之和、交替和、尼科马霍斯定理（关于立方和）、五边形数和斐波那契数恒等式的视觉证明。还展示了几何级数。

几何部分主要侧重于勾股定理的视觉证明，提供了多种不同的排列和分割方法。它还包括与三角形面积（使用内切圆半径和半周长）、平行四边形面积、十二边形面积、最短距离问题、梯形性质、瓦里尼翁定理相关的证明，以及一个指向圆锥体积证明的链接。

杂项部分涵盖与不等式（均方根、算术平均数、几何平均数）、费马小定理、立体投影和反正切函数和相关的视觉表示。该页面还提供外部来源的参考文献，以便进一步了解，并注明了出处。其目的是通过图表和重组，而不是正式的代数运算，来提供对数学概念的直观理解。

---

## 86. 在 Crystal 中使用 CNode 从 Elixir 调用 Go

**原文标题**: Calling Go from Elixir with a CNode in Crystal

**原文链接**: [https://relistan.com/calling-go-from-elixir-with-a-cnode](https://relistan.com/calling-go-from-elixir-with-a-cnode)

本文详细介绍了 Mozi 如何使用 Crystal 实现的 C Node 将他们的 Elixir Phoenix LiveView 应用程序连接到现有的 Go 后端。面对在不复制代码或创建紧耦合的情况下将 Elixir 与 Go 后端集成的挑战，作者探索并放弃了 NIF 和 Ports，认为它们不是理想的解决方案。

最终选择的解决方案是 C Node，它利用 `erl_interface` 库通过 BEAM 分布协议建立 Elixir 应用程序和 Go 代码之间的通信。Go 代码被构建为一个 C ABI 库，并使用 C 封装器处理消息处理和调用 Go 函数。这种设置在编译和运行时解耦了代码库，从而实现了独立开发和部署。

为了提高可维护性，C 封装器用 Crystal（一种类似于 Ruby 的、编译为本机代码的语言）重写。这导致了一个三语言架构（Elixir、Crystal、Go）。

该系统运行可靠，Crystal/Go 代码作为 Docker 容器与 Elixir 应用程序一起部署。作者遇到了 Go 在 Alpine Linux 上对 MUSL libc 的支持问题，需要临时构建一个自定义的 Go 编译器。

作者还简要介绍了 BEAM 分布协议的 Go 实现 (Ergo)，解释了他们为什么选择构建自己的自定义解决方案。最后，作者表示如果有足够的兴趣，他们愿意开源 Crystal 封装器。

---

## 87. 我写了一个编译器

**原文标题**: I Wrote a Compiler

**原文链接**: [https://blog.singleton.io/posts/2021-01-31-i-wrote-a-compiler/](https://blog.singleton.io/posts/2021-01-31-i-wrote-a-compiler/)

本文介绍了作者在一个周末编写一个名为“toybasic”的自定义BASIC方言的简单编译器的经验。作者具有计算机科学背景，旨在创建一个功能齐全的简化BASIC语言编译器。代码可在GitHub上找到。

该编译器将toybasic代码翻译成Go代码，主要分为三个阶段：

1.  **词法分析器（Lexer）：** 使用`nex`库将源代码转换为令牌。`nex`库通过定义语言的关键词和标识符的正则表达式来生成Go代码。

2.  **语法分析器（Parser）：** 使用`goyacc`（Go版本的`yacc`）从令牌构建语法树。它检查语法错误，并使用定义的语法和相关的Go代码来生成程序的结构化树表示。

3.  **编译器（Compiler）：** 遍历语法树并生成等效的Go代码。树中的每个节点类型都有一个`Generate`函数来生成相应的Go代码。

作者提供了该语言的语法、词法分析器配置和编译过程的示例，说明了BASIC语句如何被翻译成Go代码。该项目是作者的一次实践练习，加强了他们对编译器设计的理解。

---

## 88. 构建有效的AI智能体

**原文标题**: Building Effective AI Agents

**原文链接**: [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)

Anthropic关于使用大型语言模型构建有效AI代理的实用建议：工作流与代理，以及渐进式复杂性

---

## 89. 克劳德代码的魔力在于它的迭代性。

**原文标题**: Claude Code feels like magic because it is iterative

**原文链接**: [https://omarabid.com/claude-magic](https://omarabid.com/claude-magic)

文章认为，Claude Code以及类似的AI工具之所以显得“神奇”，是因为它们具有迭代性和速度，有效地放大了底层LLM的智能。文章提出，即使LLM的性能趋于平缓，通过反复尝试和自主性也能实现有价值的提升。核心思想可以用公式概括：智能 = 启发式 * 尝试。

作者最初不以为然，认为手动与LLM交互就足够了。然而，在目睹了Claude Code在复杂依赖项更新任务中的自主迭代后，他们的观点发生了改变。该工具自主地进行了数十次尝试，编译、测试和调整了30-40分钟，仅需偶尔干预。

文章强调了扩展这种迭代方法的潜力。通过大规模并行计算，将依赖项更新时间从40分钟缩短到可能仅需1分钟，引发了人们对是否还应该回到手动方法的疑问。这促使人们思考，利用当前LLM的能力，今天还能自动化哪些其他任务？本质上，价值不仅在于LLM本身，还在于工具通过快速和自主迭代来利用它的能力。

---

## 90. Bzip2 包已从 C 切换到 100% Rust

**原文标题**: Bzip2 crate switches from C to 100% Rust

**原文链接**: [https://trifectatech.org/blog/bzip2-crate-switches-from-c-to-rust/](https://trifectatech.org/blog/bzip2-crate-switches-from-c-to-rust/)

bzip2 crate 已更新至 0.6.0 版本，以纯 Rust 实现 `libbz2-rs-sys` 替换了底层的 C 实现。这一变更带来了更佳的性能、更简易的交叉编译和更好的可维护性。

新的 Rust 实现通常在压缩和解压缩方面都优于 C 版本，在基准测试中观察到显著的加速。由于消除了 C 依赖，交叉编译（尤其是 WebAssembly、Windows 和 Android）现在变得更加简单。

此外，Rust 实现默认情况下不导出符号，避免了与其他依赖项的潜在冲突。该代码已经过 MIRI 的严格测试，未发现重大问题。Radically Open Security 的审计发现并修复了一个次要的逻辑错误。

迁移到 100% Rust 实现使 bzip2 库现代化，确保它对于仍然需要其支持的应用程序和协议保持合规性和高性能。该项目由 NLnet Foundation 资助，并得到 Alex Crichton 和 Radically Open Security 的支持。

---

## 91. DropZap世界 – 我耗时数年制作的带有激光的方块下落游戏

**原文标题**: DropZap World – My falling block game with lasers, released after years of work

**原文链接**: [https://apps.apple.com/us/app/dropzap-world/id1072858930](https://apps.apple.com/us/app/dropzap-world/id1072858930)

DropZap World，一款由Amir Michail开发的下落方块益智游戏，历经多年制作终于发布。可在iOS、iPadOS、tvOS和macOS上运行，它提供独特的游戏体验，包含激光、镜子、颜色匹配和120个关卡。

这款游戏基于DropZap系列，但引入了其自身的关卡式进度系统。游戏玩法围绕着将圆圈颜色与物体匹配，以使用沿八个方向发射的激光摧毁方块。目标是消除所有方块以完成每个关卡。

主要功能包括跨平台可用性，并支持iCloud同步，可在设备间无缝同步进度。该应用程序相对较小（2.6 MB），评级为4岁以上。它支持Game Center，提供挑战、排行榜和成就，并为部分应用内购买提供家庭共享。

该应用可免费下载和游玩，可以选择应用内购买“无限生命”，价格为1.99美元和4.99美元。开发者的隐私条款表明，用户内容可能会被收集并与用户的身份相关联。

---

## 92. AMD Zen架构前互连：Trinity北桥测试

**原文标题**: AMD's Pre-Zen Interconnect: Testing Trinity's Northbridge

**原文链接**: [https://chipsandcheese.com/p/amds-pre-zen-interconnect-testing](https://chipsandcheese.com/p/amds-pre-zen-interconnect-testing)

本文深入探讨AMD 2012年推出的 "Trinity" APU（加速处理器）的架构，重点关注其互连架构，特别是北桥，以及它如何将GPU与CPU核心集成在一起。在Infinity Fabric出现之前，AMD的互连架构最初旨在以低延迟将CPU核心和内存连接在一起。

本文重点介绍了在集成GPU时，这种前Infinity Fabric互连架构的局限性和妥协。Trinity使用两条链路将iGPU连接到内存：用于高带宽GPU访问的“Garlic”（蒜瓣）链路（Radeon内存总线），它绕过CPU缓存一致性；以及“Onion”（洋葱）链路（控制链路），它允许GPU通过XBAR和MCT访问可缓存的CPU内存，从而实现零拷贝，但带宽显著降低。

“Garlic”链路允许iGPU饱和DRAM带宽，绕过MCT和北桥的缓存一致性机制，防止功率浪费和探测。然而，这意味着iGPU无法使用“Garlic”链路访问CPU缓存中最新的数据。“Onion”链路提供缓存一致性，但带宽较低。

本文展示了基准测试，表明即使在通过“Garlic”链路进行大量GPU带宽需求的情况下，CPU延迟仍然相对稳定。它还指出了CPU和GPU在访问彼此的内存空间时所产生的性能损失，这与AMD后来的Infinity Fabric不同。尽管存在局限性，“Garlic”链路允许iGPU消耗大量带宽，而不会影响CPU端的内存延迟。在游戏负载中，iGPU大量利用“Garlic”链路进行DRAM访问，突显了Trinity对内存带宽的依赖。

---

## 93. 公元前3700年至公元2000年全球六千年城市化空间化

**原文标题**: Spatializing 6k years of global urbanization from 3700 BC to AD 2000

**原文链接**: [https://www.nature.com/articles/sdata201634](https://www.nature.com/articles/sdata201634)

本文介绍了一个新的、空间明确的城市聚落数据集，该数据集涵盖了公元前3700年至公元2000年，旨在解决全球范围内缺乏全面历史城市人口数据的问题。该数据集基于Tertius Chandler和George Modelski的研究成果，提供了6000多年来城市人口的地理位置和估计规模。创建过程包括对原始表格数据进行数字化、转录、地理编码、清理和协调。此外，还为每个地理编码位置分配了可靠性等级，以表明地理不确定性。

该数据集旨在更好地理解长期的城市化趋势和模式，以及城市增长与农业生产力等因素之间的关系。虽然最初的动机是检验城市在肥沃农业地区发展的假设，但作者强调了该数据集更广泛的应用，包括探索城市聚落的地理演变、资源利用以及城市增长和衰落的长期周期。

作者承认存在局限性，例如源于原始作品以及Chandler和Modelski使用的“城市”的不同定义所导致的时间和空间稀疏性。然而，他们认为这种多方面的方法改进了城市特征的描述。尽管存在这些局限性，该数据集为理解全球城市人口的历史地理分布提供了关键的第一步。这项研究解决了城市历史学家指出的一个关键知识空白，并为地理学、经济学和人类学等多个领域提供了宝贵的资源。

---

## 94. Show HN: Lstr – 一款用 Rust 编写的现代交互式树形命令

**原文标题**: Show HN: Lstr – A modern, interactive tree command written in Rust

**原文链接**: [https://github.com/bgreenwell/lstr](https://github.com/bgreenwell/lstr)

Lstr: 快速、简约且交互式的目录树查看器，用 Rust 编写，灵感来自经典的 `tree` 命令。它提供经典的树状输出和用于键盘驱动探索的交互式 TUI 模式。

主要功能包括：并行目录扫描以提高速度、可选的丰富信息显示（图标、权限、文件大小）、Git 集成以及使用 `.gitignore` 文件的智能过滤。克隆 GitHub 仓库后，可以使用 `cargo install --path .` 进行安装。

该工具提供多种自定义选项，例如显示隐藏文件、仅按目录过滤、控制递归深度以及显示 Git 状态。交互模式提供键盘控制，用于导航和操作，如打开文件或切换目录展开。

Lstr 通过管道与其它命令行工具良好集成。例如，使用 `fzf` 进行模糊查找，使用 `less` 或 `bat` 进行分页，以及使用自定义的 `lcd` 函数以可视方式更改目录。

性能通过使用 `rayon` 线程池的并行目录遍历进行优化，这可以通过 `RAYON_NUM_THREADS` 环境变量进行控制。该项目旨在用现代、安全的 Rust 复制基于 C 的 `tree` 命令的功能。

---

## 95. 从SDR到“伪HDR”：Switch 2上的马力欧卡丁车世界

**原文标题**: From SDR to 'Fake HDR': Mario Kart World on Switch 2

**原文链接**: [https://www.alexandermejia.com/from-sdr-to-fake-hdr-mario-kart-world-on-switch-2-undermines-modern-display-potential/](https://www.alexandermejia.com/from-sdr-to-fake-hdr-mario-kart-world-on-switch-2-undermines-modern-display-potential/)

本文批评任天堂Switch 2上的《马力欧卡丁车世界》，认为其HDR实现是一种“假HDR”体验。尽管Switch 2宣传具有4K60 + HDR输出，但作者认为该游戏主要针对SDR（标准动态范围）制作，然后表面上进行了色调映射到HDR，导致视觉体验不佳。

作者是一位杜比视界专家，他使用专业的采集设备分析了游戏的HDR输出，揭示了即使主机的HDR亮度设置得更高，游戏的亮度也被限制在950尼特左右。此外，色域被限制在Rec.709（SDR色彩空间），否定了HDR更宽广色彩范围的优势。作者演示了仅通过在达芬奇调色中将SDR图像拉伸到HDR即可轻松复制游戏的HDR外观，表明缺乏真正的HDR母版制作。天空中的条带也值得注意，这可能是由于较低的位深度精度造成的，而本应通过HDR美术审查发现。

文章认为，这种“SDR优先流程陷阱”在业界很常见，即开发者优先考虑SDR，然后在最后阶段匆忙添加HDR。这种方法限制了游戏的视觉潜力，并且未能利用现代HDR显示器。作者强调，真正的HDR需要开发实践的转变，包括承诺宽色域、允许动态范围以及构建动态色调映射服务。通过这样做，开发者可以交付视觉上更出色的游戏，真正发挥HDR技术的能力。

---

## 96. KiCad和Wayland支持

**原文标题**: KiCad and Wayland Support

**原文链接**: [https://www.kicad.org/blog/2025/06/KiCad-and-Wayland-Support/](https://www.kicad.org/blog/2025/06/KiCad-and-Wayland-Support/)

KiCad 对 Wayland 的支持功能尚可但已降级。虽然它能在 Wayland 系统上运行，但用户会遇到大量问题，KiCad 团队因 Wayland 协议、窗口管理器和合成器的限制，无法在应用层面上解决这些问题。这些问题包括窗口管理问题（窗口放置、停靠面板定位）、输入和交互问题（光标扭曲、焦点管理）、性能和稳定性问题（OpenGL 限制、高资源占用、崩溃）以及对话框/UI 限制。

KiCad 团队的策略是避免针对特定窗口管理器的变通方法，继续测试 Wayland 兼容性，并将开发重点放在使所有用户受益的功能上。他们不会调查或支持与 X11 上未发生的 Wayland 特定问题相关的错误报告。

对于专业用途，团队强烈建议使用基于 X11 的环境，如 XFCE、KDE Plasma 或 MATE。愿意接受限制的休闲用户可以在 Wayland 上使用 KiCad，但应该预料到会出现问题。

团队承认 Wayland 的发展，但优先考虑用户生产力和可靠性。他们鼓励向上游项目（Wayland、窗口管理器、wxWidgets）贡献代码，并提供赞助开发的机会。

总之，KiCad 对 Wayland 的支持有限，存在大量未解决的问题。建议用户使用 X11 以获得稳定的体验，直到 Wayland 成熟并解决根本问题。

---

## 97. 穿梭跑的魔力

**原文标题**: The magic of through running

**原文链接**: [https://www.worksinprogress.news/p/the-magic-of-through-running](https://www.worksinprogress.news/p/the-magic-of-through-running)

本文探讨了“贯通运营的魔力”，这是一种交通策略，通过将现有郊区铁路线路通过市中心隧道连接起来，将其转变为类似地铁的系统。

历史上，由于土地成本、技术限制和规章制度，19世纪的铁路网络终点通常位于城市边缘。这导致了以中央终点站为中心的轮辐式网络，这些终点站成为了瓶颈，限制了列车班次，并需要大型且昂贵的车站。另一方面，地铁可以在城市中的任何地方运行，易于互联互通，并且服务模式简单，避免了中央终点站的运力问题。

“贯通运营”通过隧道连接城市两侧的郊区线路来解决这个问题，以相对较小的成本为许多郊区提供类似地铁的服务进入市中心，因为大部分基础设施已经存在。本文以慕尼黑和伦敦为例进行研究。慕尼黑通过将郊区铁路网络与中央隧道整合，形成了S-Bahn（快铁），从而创建了被认为是其规模下世界上最好的交通网络之一。该系统将郊区城镇直接连接到市中心，并与U-Bahn（地铁）整合。伦敦凭借其庞大的维多利亚时代遗留网络，也从贯通运营中受益匪浅。

作者认为，对于拥有庞大维多利亚时代铁路网络的城市来说，贯通运营是一个至关重要的交通政策主题，有可能以建造全新地铁系统的一小部分成本，创建世界领先的交通系统。

---

## 98. Linux 中理解 NAT 和数据包修改

**原文标题**: Grokking NAT and packet mangling in Linux

**原文链接**: [https://vivekn.dev/blog/grokking-nat-and-packet-mangling-in-linux](https://vivekn.dev/blog/grokking-nat-and-packet-mangling-in-linux)

本文解释了网络地址转换 (NAT) 技术，该技术用于克服 IPv4 地址的局限性。它首先阐述了 NAT 如何允许专用网络上的多个设备共享单个公共 IP 地址，并使用路由器作为中介。文章强调，虽然 IPv6 可以解决 IPv4 地址短缺问题，但其广泛采用面临重大障碍。

文章随后详细介绍了不同类型的 NAT，包括基本/静态 NAT 和端口地址转换 (PAT)。它进一步阐述了锥形 NAT 的变体（完全锥形、受限锥形和端口受限锥形）和对称 NAT，解释了它们不同的限制级别以及对 WebRTC 等应用程序的影响。

文章深入探讨了路由器如何实现 NAT，特别提到了使用 nftables 的基于 Linux 的系统，如 OpenWrt。它考察了 `nf_nat_mangle_udp_packet` 函数，演示了 NAT 如何操作数据包头、有效负载和校验和。

作者通过提及 Docker 及其端口映射如何依赖于 iptables 规则进行 NAT，将 NAT 与日常工程联系起来。文章最后承认了 NAT 的局限性，例如破坏端到端连接、使加密和点对点应用程序复杂化，以及需要内存进行连接映射。最后，它重申 IPv6 提供了一个真正的解决方案，尽管采用仍然不完整。

---

## 99. Gumbel-Softmax分布

**原文标题**: The Gumbel-Softmax Distribution

**原文链接**: [https://sassafras13.github.io/GumbelSoftmax/](https://sassafras13.github.io/GumbelSoftmax/)

本文解释了Gumbel-Softmax分布，这是一种将分类分布融入神经网络，同时仍然能够进行反向传播优化的一种技术。核心问题在于，直接从神经网络中的分类分布进行采样会阻止梯度计算，因为其具有离散和随机的特性。

该解决方案建立在两个关键概念之上：重参数化技巧和Gumbel-Max技巧。重参数化技巧将随机采样过程重塑为确定性和随机元素的组合，从而允许通过确定性部分计算梯度。Gumbel-Max技巧通过将Gumbel分布的噪声添加到每个类别的对数概率中，然后取argmax来选择类别（表示为one-hot向量），从而促进从分类分布中采样。

Gumbel-Softmax分布通过用softmax函数替换不可微的argmax函数来改进Gumbel-Max技巧。它还引入了一个温度参数（lambda）来控制Gumbel-softmax对分类分布的近似程度。较高的温度会导致更均匀的分布，而较低的温度会将概率集中在单个类别上。

在神经网络训练期间，使用退火计划来逐渐降低温度。这平衡了模型的准确性和方差：高温在训练初期提供鲁棒性，而较低的温度允许在网络收敛时进行更细粒度的学习。本文最后提出了如何在实践中实现Gumbel-Softmax分布的问题。

---

## 100. 创建 JSON 的 Shell 命令：jo (2016)

**原文标题**: A shell command to create JSON: jo (2016)

**原文链接**: [https://jpmens.net/2016/03/05/a-shell-command-to-create-json-jo/](https://jpmens.net/2016/03/05/a-shell-command-to-create-json-jo/)

本文介绍 `jo`，一个命令行工具，旨在简化 shell 脚本中 JSON 的创建。作者对在 shell 脚本中生成 JSON 的传统方法（尤其是在处理环境变量、引号和嵌套结构时）的复杂性和可读性感到沮丧。

`jo` 通过提供简洁直观的语法解决了这些问题。用户可以直接在命令行上指定键值对，`jo` 会智能地推断数据类型（null、布尔值、字符串、数字）。它还支持数组和美化打印，以提高可读性。

一个关键特性是能够使用 `$(jo ...)` 语法或通过检测以 `{` 或 `[` 开头的字符串，将 JSON 对象和数组彼此嵌入。这使得轻松创建复杂的嵌套 JSON 结构成为可能。`jo` 也原生支持嵌套类型。

进一步的增强包括能够使用 `@file` 直接从文件中读取值，以及使用 `%file` 将二进制文件编码为 base64。该工具可以通过 Homebrew、HardenedBSD ports、voidlinux、ArchLinux、Debian 和 Win32 二进制文件在各种平台上使用。作者创建 `jo` 是为了改进 OwnTracks 的 JSON 处理，并赞赏其在脚本中的简洁性和可读性。

---

