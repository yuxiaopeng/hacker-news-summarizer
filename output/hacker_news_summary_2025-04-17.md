# Hacker News 热门文章摘要 (2025-04-17)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. OpenAI顶级灾难风险官员突然辞职

**原文标题**: Top OpenAI Catastrophic Risk Official Steps Down Abruptly

**原文链接**: [https://garrisonlovely.substack.com/p/breaking-top-openai-catastrophic](https://garrisonlovely.substack.com/p/breaking-top-openai-catastrophic)

无法访问文章链接。

---

## 2. DeepSeek分布式文件系统入门

**原文标题**: An Intro to DeepSeek's Distributed File System

**原文链接**: [https://maknee.github.io/blog/2025/3FS-Performance-Journal-1/](https://maknee.github.io/blog/2025/3FS-Performance-Journal-1/)

本文介绍DeepSeek的开源分布式文件系统3FS（Fire-Flyer File System）。它阐述了分布式文件系统的概念，强调了其将数据碎片化分布在多台机器上的复杂性抽象化，从而使用户感觉就像在使用单个本地文件系统。分布式文件系统的优势包括海量数据服务能力、高吞吐量、容错性和冗余性。

3FS由四种主要节点类型组成：Meta（管理元数据）、Mgmtd（管理集群配置和节点发现）、Storage（存储实际文件数据）和Client（与其他节点通信）。本文详细介绍了每个节点的功能，包括Mgmtd在节点注册和配置中的作用，Meta使用FoundationDB处理文件操作和元数据存储，以及Storage使用ChunkEngine（用Rust编写）通过将文件分成块并将元数据存储在LevelDB中来管理物理存储。

3FS的一个重要方面是它使用CRAQ（具有分配查询的链式复制）来实现强一致性和容错。CRAQ确保数据复制到一系列节点上，写入操作按顺序传播，读取操作可以从干净或脏数据中获取，并且尾节点始终具有最新的数据。

文章最后将3FS与其他分布式文件系统进行比较，强调了实际应用性、调优灵活性和实际实现细节的重要性。作者概述了未来博客文章的计划，以对3FS性能进行基准测试，找出瓶颈，并将其与现有系统进行比较。最后，该文章提供了指向设计说明、技术文档和学术论文的链接，其中包含更深入的信息。

---

## 3. Erlang/OTP SSH 中未经身份验证的远程代码执行

**原文标题**: Unauthenticated Remote Code Execution in Erlang/OTP SSH

**原文链接**: [https://nvd.nist.gov/vuln/detail/CVE-2025-32433](https://nvd.nist.gov/vuln/detail/CVE-2025-32433)

CVE-2025-32433 描述了 Erlang/OTP 的 SSH 服务器中的一个未经身份验证的远程代码执行 (RCE) 漏洞。受影响的版本包括 OTP-27.3.3 之前的版本、OTP-26.2.5.11 之前的版本以及 OTP-25.3.2.20 之前的版本。攻击者可以利用 SSH 协议消息处理中的缺陷，在无需有效凭据的情况下获得未授权访问权限并执行任意命令。

GitHub, Inc. 将此漏洞评级为 CRITICAL（严重），CVSS 3.1 评分为 10.0，向量为 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H。这表明该漏洞可通过网络利用，无需用户交互或权限，攻击复杂度低，并可能导致受影响系统的机密性、完整性和可用性完全受损。

补丁已在 OTP-27.3.3、OTP-26.2.5.11 和 OTP-25.3.2.20 版本中提供。临时的解决方案是禁用 SSH 服务器或使用防火墙规则阻止访问。此漏洞是由于关键功能缺少身份验证 (CWE-306) 导致的。更多详细信息和与修复相关的代码提交可以在链接的 GitHub 资源中找到。

---

## 4. 谷歌是线上广告技术领域的垄断者，法官表示

**原文标题**: Google Is a Monopolist in Online Advertising Tech, Judge Says

**原文链接**: [https://www.nytimes.com/2025/04/17/technology/google-ad-tech-antitrust-ruling.html](https://www.nytimes.com/2025/04/17/technology/google-ad-tech-antitrust-ruling.html)

联邦法官裁定谷歌非法垄断部分在线广告技术市场

---

## 5. 软件制作

**原文标题**: Making Software

**原文链接**: [https://www.makingsoftware.com/](https://www.makingsoftware.com/)

《软件制作》一书面向那些对日常技术如何运作充满好奇心，但又不是技术专家的读者。它不是教程或指南，而是一本解释触摸屏、图像模糊、矢量图形等底层机制的手册。

本书旨在弥合我们对技术的使用与理解之间日益扩大的差距。它旨在提供对事物如何运作的更深入（但不一定是可操作的）的知识，这有助于解决问题或满足纯粹的求知欲。本书使用插图和图表来方便理解。

目录揭示了本书涵盖的广泛主题，包括像素和颜色、字体和矢量、3D和着色器、人工智能和机器学习、压缩和数据、网络和Web、以及编译器和解释器。它还将探讨更具体的例子，如正则表达式、二维码和量子计算。

本书最初将以数字形式发布，之后可能会进行印刷。预购选项允许读者在章节撰写时访问它们，并允许读者提出主题建议。虽然价格尚未确定，但某些内容将是免费的，特别是对于那些在邮件列表中的人。

---

## 6. 不锈钢强化：扭转产生亚微米级“防撞墙”

**原文标题**: Stainless steel strengthened: Twisting creates submicron 'anti-crash wall'

**原文链接**: [https://techxplore.com/news/2025-04-stainless-steel-technique-submicron-anti.html](https://techxplore.com/news/2025-04-stainless-steel-technique-submicron-anti.html)

发表于2025年4月12日Tech Xplore上的一篇文章报道了中国科学院、山东大学和佐治亚理工学院的研究人员开发的一种新型不锈钢强化方法。该研究发表在《科学》杂志上，详细介绍了一种扭转技术，该技术显著提高了金属的抗金属疲劳和循环蠕变能力。

这种创新方法包括重复扭转304奥氏体不锈钢，创造一种空间梯度蜂窝结构，形成亚微米级的三维“防撞墙”。显微分析显示，超细的、小于10纳米的相干层状结构有效地通过阻止堆垛层错来减缓位错运动。这种“防撞墙”像弹簧一样，吸收冲击力，使金属的抗循环蠕变能力更加均匀。

测试表明，与未处理的钢相比，处理后的不锈钢强度提高了2.6倍，棘轮效应引起的应变减少了2到4个数量级。研究人员声称，这种改进可能会使由处理后的钢制成的产品抗疲劳能力提高多达10,000倍，为航空航天等行业的专业应用开辟了可能性。

---

## 7. EasyPost (YC S13) 正在招聘

**原文标题**: EasyPost (YC S13) Is Hiring

**原文链接**: [https://www.easypost.com/careers](https://www.easypost.com/careers)

EasyPost (YC S13) 积极招聘，寻找平易近人、充满活力、富有创造力、才智过人且值得信赖的候选人，共同定义航运的未来。他们正在寻找能够协作、提出挑战性问题、探索新解决方案并承担责任的问题解决者。

该公司强调他们专注于现代、灵活的技术，以改善航运的客户体验，展望实现当日送达和减少环境浪费的未来。他们强调一种适应性强、简单和包容的文化。

EasyPost 以其工程至上的公司理念和务实的软件开发方法而自豪。他们提供一个有趣、充满激情和创业精神的环境，团队拥有多样化的经验。关键技术特性包括受 CI/CD 启发的Workflow、小型服务而非单体应用、强大的工程工具和开发者支持，以及一种不咎责任的文化。

他们提供医疗、牙科和视力保险计划、弹性休假、股票期权机会、跨职能学习和每月虚拟活动等福利和津贴。文章还警告存在冒充 EasyPost 的招聘诈骗，并敦促申请人保持警惕，并通过官方渠道验证任何可疑的职位邀请。

---

## 8. 展示 HN: AgentAPI – Claude Code、Goose、Aider 和 Codex 的 HTTP API

**原文标题**: Show HN: AgentAPI – HTTP API for Claude Code, Goose, Aider, and Codex

**原文链接**: [https://github.com/coder/agentapi](https://github.com/coder/agentapi)

AgentAPI 是一个 HTTP API，它允许对 Claude Code、Goose、Aider 和 Codex 等编码代理进行编程控制。它解决了通过基于终端的界面与这些代理交互的难题，提供了一种统一的方式来构建聊天界面、创建多代理系统和自动化代码审查流程。

该工具可以通过预构建的二进制文件安装，也可以使用 Go 从源代码构建。它提供了 CLI 命令来运行代理服务器 (`agentapi server`) 和连接到正在运行的代理的终端会话 (`agentapi attach`)。该服务器公开了一个 OpenAPI 模式和文档 UI。

主要功能包括：

*   **API 端点：** `/messages` (获取历史记录), `/message` (发送消息), `/status` (获取状态), `/events` (SSE 流).
*   **终端模拟：** 将 API 调用转换为终端击键。
*   **消息解析：** 将终端输出拆分为用户和代理消息，删除不需要的 TUI 元素。
*   **代理兼容性：** 适用于 Claude Code、Goose、Aider 和 Codex，并具有适应未来 TUI 更新的灵活性。

AgentAPI 的长期愿景是，要么因标准化官方 SDK 的出现而变得过时，要么在代理继续使用专有 API 的情况下，充当通用适配器。正在考虑的未来功能包括支持 MCP 和 Agent2Agent 协议。

---

## 9. HDR加持的表情符号

**原文标题**: HDR‑Infused Emoji

**原文链接**: [https://sharpletters.net/2025/04/16/hdr-emoji/](https://sharpletters.net/2025/04/16/hdr-emoji/)

本文解释了如何在Slack中创建HDR（高动态范围）表情符号。作者指出，这些HDR表情符号以增强的亮度渲染，使其在视觉上引人注目，尤其是在支持HDR显示的硬件上。

HDR表情符号的创建过程涉及使用`imagemagick`来处理图像。具体来说，该脚本执行以下操作：

1. 将图像的色彩空间调整为RGB。
2. 应用自动伽马校正。
3. 乘以并幂运算图像值以增加亮度。乘法因子需要根据源图像进行调整。
4. 将色彩空间转换回sRGB。
5. 将颜色深度调整为16位。
6. 应用2020\_profile.icc颜色配置文件。

文章强调HDR表情符号的支持并不普遍。它在Chrome和Slack中运行良好，但在很大程度上与Safari和Android设备不兼容。建议用户在Slack中测试表情符号，以验证它们在不同平台上的渲染效果。一个关键要求是在执行`imagemagick`脚本的工作目录中拥有`2020_profile.icc`文件。

---

## 10. Zoom宕机因意外“关闭”zoom.us域名导致。

**原文标题**: Zoom outage caused by accidental 'shutting down' of the zoom.us domain

**原文链接**: [https://status.zoom.us/incidents/pw9r9vnq5rvk](https://status.zoom.us/incidents/pw9r9vnq5rvk)

2025年4月16日，Zoom遭遇中断，影响了包括Zoom Meetings、Zoom Phone、Zoom Contact Center和Zoom网站在内的多项服务。根本原因是Zoom的域名注册商Markmonitor与GoDaddy Registry之间发生通信错误。此错误导致GoDaddy Registry错误地屏蔽了zoom.us域名，使其在东部时间下午2:25至下午4:12之间无法访问。

Zoom、Markmonitor和GoDaddy迅速采取行动，确定并解决了问题，恢复了zoom.us域名的服务。Zoom澄清说，中断并非由于任何产品故障、安全漏洞、网络问题或分布式拒绝服务(DDoS)攻击所致。

恢复后，Zoom建议遇到连接问题的用户刷新其DNS缓存，并为Windows和Mac用户提供了执行此操作的说明。GoDaddy和Markmonitor正在合作以防止未来发生类似事件。

---

## 11. MCP运行Python

**原文标题**: MCP Run Python

**原文链接**: [https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python](https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python)

本文介绍了`@pydantic/mcp-run-python`，一个模型上下文协议(MCP)服务器，它使用Pyodide和Deno在沙箱环境中执行Python代码。这种隔离防止了代码直接与主机操作系统交互。该服务器旨在与PydanticAI和其他使用MCP的工具集成。

为了运行服务器，本文提供了一个Deno命令，其中包含允许网络访问以及对本地`node_modules`目录进行读/写权限的特定标志，这对于Pyodide下载和缓存Python库是必需的。它还指定了`node_modules-dir=auto`标志来自动管理本地`node_modules`目录。

文章介绍了两种MCP传输选项：`stdio`用于本地子进程执行，`sse`用于将服务器作为HTTP服务器运行，允许本地或远程连接。`warmup`选项运行一个基本的Python脚本来预先下载和缓存Python标准库，同时也作为服务器功能测试。

本文包含一个代码示例，演示了如何将`@pydantic/mcp-run-python`与PydanticAI一起使用。它展示了与`MCPServerStdio`的集成，设置了一个PydanticAI Agent来通过沙箱服务器执行Python脚本。该示例最终使用在MCP服务器中执行的Python代码计算两个日期之间的天数。

---

## 12. 为什么日本“最弱武士领主”至今仍受敬仰

**原文标题**: Why Japan's "Weakest Samurai Warlord" Is Still Admired to This Day

**原文链接**: [https://www.tokyoweekender.com/art_and_culture/japanese-culture/oda-ujiharu-the-weakest-samurai-warlord/](https://www.tokyoweekender.com/art_and_culture/japanese-culture/oda-ujiharu-the-weakest-samurai-warlord/)

对“最弱武将”小田氏治的矛盾性敬佩：韧性与复兴

---

## 13. 超快光探测器

**原文标题**: Ultrafast Optical Detector

**原文链接**: [https://www.tdk.com/en/about_tdk/innovation/spin-photo-detector/index.html](https://www.tdk.com/en/about_tdk/innovation/spin-photo-detector/index.html)

TDK发布全球首款“自旋光电探测器”，有望革新光电转换技术，尤其适用于人工智能应用。该探测器采用磁性隧道结（MTJ）元件，与传统半导体光电探测器不同，可在近红外到可见光的宽波长范围内实现超快光检测。

自旋光电探测器的主要优势包括其数据传输速度有望提高10倍，从而加快人工智能系统中的数据处理速度并降低功耗。此外，该技术用途广泛，可集成到各种板卡和设备上。

TDK设想该创新技术可应用于数据中心、生成式人工智能的光通信和互连以及增强/虚拟现实（AR/VR）领域。该公司的媒体新闻稿和专题报道文章提供了更多详细信息。

---

## 14. 下半场

**原文标题**: The Second Half

**原文链接**: [https://ysymyth.github.io/The-Second-Half/](https://ysymyth.github.io/The-Second-Half/)

第二篇章：人工智能正步入新纪元，重心从开发新的训练方法和模型（“解决问题”）转向定义需要解决的正确问题以及如何衡量实际进展（“定义问题”）。作者认为，由语言预训练和推理驱动的强化学习 (RL) 终于实现了泛化，创造出了一种能够解决各种任务的“配方”。

人工智能的上半场侧重于训练方法和模型的突破，主要通过基准性能进行评估。之所以成功，是因为方法比任务更难，适用性更广。如今，这种“配方”变得非常有效，降低了对新方法的需求，并能快速解决新的基准问题。

作者认为，下半场需要从根本上重新思考评估方式。现有的评估设置，例如自动和独立的任务运行，并不能反映现实世界的效用，即人工智能代理在顺序任务中与人类互动。这导致了“效用问题”，即人工智能在基准测试中表现出色，但尚未对经济产生重大影响。

未来的游戏包括开发反映现实世界效用的新型评估设置和任务，并使用现有配方解决它们或用新的组件来增强它。这种转变需要质疑基本假设，并专注于构建有用的产品，从而带来比上半场中看到的增量改进更大的影响和创新。本质上，重点正在从学术进步转向现实世界的应用和价值创造。

---

## 15. 脂肪组织在减肥后保留了肥胖的表观遗传记忆

**原文标题**: Adipose tissue retains an epigenetic memory of obesity after weight loss

**原文链接**: [https://www.nature.com/articles/s41586-024-08165-7](https://www.nature.com/articles/s41586-024-08165-7)

本研究调查了维持减肥困难背后的分子机制，重点关注脂肪组织中的“致肥胖记忆”概念。研究人员利用单细胞核RNA测序 (snRNA-seq) 分析了接受过减肥手术的人类和饮食诱导减肥的小鼠的脂肪组织。

主要发现如下：

*   **人类脂肪组织在显著减肥后保留了转录变化。** snRNA-seq 显示，即使在减肥后，肥胖期间差异表达的许多基因在脂肪细胞、脂肪细胞祖细胞 (APCs) 和内皮细胞中仍然失调。这些保留的变化与脂肪细胞代谢和功能相关的通路下调以及与纤维化和细胞凋亡相关的通路上调有关。
*   **小鼠脂肪细胞表现出表观遗传的致肥胖记忆。** 研究发现，小鼠脂肪细胞在减肥后存在长期持续的表观遗传改变。
*   **致肥胖记忆导致体重快速反弹。** 具有这种“记忆”的小鼠在再次暴露于高脂肪饮食时表现出更快的反弹性体重增加。这种表观遗传记忆可以解释脂肪细胞在未来对进一步高脂肪饮食的反应中出现的转录失调。
*   **体重减轻诱导的(部分) epiAT重塑后，转录变化持续存在。** 体重减轻后，只有少数轻微的代谢损伤持续存在，包括HC小鼠的葡萄糖不耐受，HHC小鼠的高胰岛素血症和轻微的肝脏脂肪变性，以及两组小鼠体重减轻后epiAT储存库大小的显著减少。

总之，该研究为致肥胖记忆提供了证据，这种记忆主要由脂肪细胞和潜在的其他细胞类型的稳定表观遗传变化驱动，使细胞为在致肥胖环境中的病理反应做好准备，从而导致溜溜球节食效应。针对这些变化可能有助于改善长期体重管理策略。

---

## 16. 飞机的轰鸣和其他嗖嗖声

**原文标题**: Passing planes and other whoosh sounds

**原文链接**: [https://www.windytan.com/2025/04/passing-planes-and-other-whoosh-sounds.html](https://www.windytan.com/2025/04/passing-planes-and-other-whoosh-sounds.html)

本文探讨了飞机飞过头顶时常听到的“呼啸”声，认为它不仅仅是多普勒效应造成的。虽然多普勒效应解释了发动机音调的降低，但本文侧重于一种更广泛、更气息化的声音，这种声音的音调首先降低，然后在飞机经过后又升高。

作者认为这种声音是由梳状滤波引起的，梳状滤波是一种现象，其中同一声音的两个略有延迟的副本相互干扰，在频谱中产生移动的峰谷。作者假设这种延迟是由于地面回声造成的——听者既听到来自飞机的直接声音，也听到来自地面的延迟反射。

倒谱被用于分析延迟时间，揭示了一个与感知到的音调变化相对应的扫动峰值。基于听者的高度和到地面的距离的计算支持了这样的观点，即回声延迟落在观测到的范围内（当飞机在头顶时为4-9毫秒，成角度时接近4毫秒）。

文章进一步解释说，“呼啸”声并不局限于飞机，它需要结构化的声音、附近的反射表面和运动。例子包括瀑布反射墙壁的声音以及高速公路护栏附近的声音。作者鼓励读者自己尝试创造这种效果，并包含一个交互式 JavaScript 图，以可视化飞机位置、听者位置和由此产生的时间延迟之间的关系。

---

## 17. 人工智能作为普通技术

**原文标题**: AI as Normal Technology

**原文链接**: [https://knightcolumbia.org/content/ai-as-normal-technology](https://knightcolumbia.org/content/ai-as-normal-technology)

本文认为，应将人工智能视为“普通技术”，类似于电力或互联网，而非独立、超智能的实体。作者将此观点作为对当前人工智能的描述、对其可预见的未来的预测以及对其应如何对待的建议。他们反对技术决定论，并强调技术采纳的缓慢和不确定性，从过去的技术革命中汲取经验教训。

本文分为四个部分。第一部分解释了为何变革性影响会很慢（以数十年为单位），因为人工智能方法、应用和采纳的速度各不相同。第二部分讨论了人机分工，其中人类保留控制权，越来越多的工作集中在人工智能控制上。第三部分考察了人工智能的风险（事故、军备竞赛、滥用、未对齐），并认为与将人工智能视为类人相比，“普通技术”的视角会导致不同的缓解策略。第四部分主张减少人工智能政策的不确定性并培养韧性，告诫不要基于对超智能的恐惧而采取激烈的干预措施。

作者强调，由于监管监督和对可解释模型的需求，人工智能在安全关键领域的扩散尤其缓慢。他们还指出，即使在安全关键领域之外，人工智能的采用也受到人类、组织和制度变革速度的限制。他们预测，在高后果任务中的缓慢扩散将持续下去，并强调随着人工智能应用新领域的出现，调整法规的重要性。

---

## 18. 停机问题是NP-难的一个糟糕例子

**原文标题**: The Halting Problem is a terrible example of NP-Harder

**原文链接**: [https://buttondown.com/hillelwayne/archive/the-halting-problem-is-a-terrible-example-of-np/](https://buttondown.com/hillelwayne/archive/the-halting-problem-is-a-terrible-example-of-np/)

作者认为，将停机问题（HALT）作为比NP完全问题更难的主要例子是一个糟糕的选择。虽然技术上正确（HALT是不可判定的），但作者觉得它不够简洁且容易混淆。他们指出，NP仅要求对“是”实例进行多项式时间验证，而HALT的“是”实例（“它在N步内停止”） *可以* 被验证。复杂之处在于证明此验证过程超出多项式时间，原因是忙碌海狸函数的不可计算性。

作者希望有一个更直观的例子，但指出许多确定比NP难的问题需要大量的理论背景。他们提出了一个基于在多维网格上移动令牌的替代方案。确定一系列移动能否到达此网格中的目标点，其难度从PSPACE完全开始，并随着维数的增加而急剧升级，变为EXPSPACE完全，然后是TOWER完全，最终变为ACKERMANN完全。这个问题虽然比NP难得多，但仍然是可判定的并且容易解释，提供了一个比停机问题更清晰的“比NP更难”的说明。作者还提到NP的另一种定义（可以用非确定性图灵机在多项式时间内解决）是HALT不能属于NP的原因。

---

## 19. BitNet b1.58 2B4T 技术报告

**原文标题**: BitNet b1.58 2B4T Technical Report

**原文链接**: [https://arxiv.org/abs/2504.12285](https://arxiv.org/abs/2504.12285)

本技术报告介绍了BitNet b1.58 2B4T，首个拥有20亿参数的开源1比特大型语言模型(LLM)。该模型在包含4万亿tokens的大规模语料库上进行训练，并在包括语言理解、数学推理、编码和对话能力等一系列基准上进行了评估。

主要发现是，BitNet b1.58 2B4T的性能与同等规模的领先开源、全精度LLM相当。然而，它在计算效率方面具有显著优势，包括大幅减少的内存占用、更低的能耗以及更低的解码延迟。

为了促进进一步的研究和应用，作者将在Hugging Face上发布模型权重，以及针对GPU和CPU架构的开源推理实现。文章还包含了与该论文相关的各种资源链接，例如代码仓库、演示和参考文献工具。本文是一项正在进行中的工作。

---

## 20. 构建一个观看橄榄球比赛的AI

**原文标题**: Building an AI That Watches Rugby

**原文链接**: [https://nickjones.tech/ai-watching-rugby/](https://nickjones.tech/ai-watching-rugby/)

本文详细介绍了作者构建一个AI系统的项目，该系统能够“观看”橄榄球比赛，并生成比传统事件流提供的数据更丰富、更具上下文的数据。其目标是理解场上动作背后的“原因”，捕捉裁判的解释、争球优势以及比赛中其他无法量化的方面等细微之处。

作者尝试使用OpenAI的视觉模型从广播截图中提取比分和比赛计时器。最初，使用了全分辨率截图，但通过裁剪图像以仅关注记分牌来降低了成本。作者还探索了图像差异和OCR等替代方案，但发现LLM方法提供了最可靠的结果。

此外，作者使用OpenAI的Whisper转录广播中的音频，捕捉解说和裁判音频，以提供更多上下文。这使得AI能够识别官方统计数据中遗漏的事件，例如令人印象深刻的球员表现或处罚。

虽然仍是一个原型，但该项目展示了使用AI生成深入橄榄球数据的潜力，使Gainline应用程序能够为球迷提供更丰富、更具沉浸感的第二屏幕体验。作者承认扩展该系统所面临的挑战以及AI驱动的体育分析的伦理考量，但对AI在体育广播和数据分析中的未来潜力仍然持乐观态度。

---

## 21. 达尔文的孩子们在《物种起源》手稿上乱涂乱画（2014）

**原文标题**: Darwin's children drew all over the “On the Origin of Species” manuscript (2014)

**原文链接**: [https://theappendix.net/posts/2014/02/darwins-children-drew-vegetable-battles-on-the-origin-of-species](https://theappendix.net/posts/2014/02/darwins-children-drew-vegetable-battles-on-the-origin-of-species)

本文发表于2014年达尔文日，通过展示查尔斯·达尔文手稿和家庭物品中发现的绘画和涂鸦，探索了达尔文作品中令人惊讶的个人一面。作者重点介绍了达尔文在线和达尔文手稿项目等数字化工作，这些项目允许人们访问这些私密的历史文物。

文章重点介绍了据说是达尔文孩子们的画作，包括在《物种起源》手稿背面上的奇幻“水果蔬菜士兵之战”、反映家庭观察能力的自然素描，以及儿童眼中达尔文的家，可能描绘了达尔文著名的“沙道”。

作者还深入研究了艾玛·达尔文的日记，展示了她通过素描和涂鸦所展现的艺术才华。日记也留下了达尔文孩子们顽皮破坏的痕迹，提醒读者达尔文科学研究周围的家庭生活。

文章的更新内容包括关于查尔斯已故女儿安妮·达尔文的一段感人笔记，以及一盒她的纪念品，包括针绣花朵。作者将安妮的去世与达尔文的个人生活以及它可能对他的科学思想和信仰衰退产生的影响联系起来。文章最终认为，理解历史人物的个人生活对于更完整和人性化地理解他们的工作和遗产至关重要。

---

## 22. 科学家发现迄今为止外星生命的最有力证据

**原文标题**: Scientists find strongest evidence yet of life on an alien planet

**原文链接**: [https://www.reuters.com/science/scientists-find-strongest-evidence-yet-life-an-alien-planet-2025-04-16/](https://www.reuters.com/science/scientists-find-strongest-evidence-yet-life-an-alien-planet-2025-04-16/)

无法访问文章链接。

---

## 23. 使用一千个 crate 将 Rust 编译时间从 30 分钟缩短到 2 分钟

**原文标题**: Cutting down Rust compile times from 30 to 2 minutes with one thousand crates

**原文链接**: [https://www.feldera.com/blog/cutting-down-rust-compile-times-from-30-to-2-minutes-with-one-thousand-crates](https://www.feldera.com/blog/cutting-down-rust-compile-times-from-30-to-2-minutes-with-one-thousand-crates)

Feldera 通过将大型单代码仓库拆分为 1000 多个小型代码仓库，显著缩短了 Rust 编译时间，从 30 分钟降至 2 分钟。 之前，编译复杂的 SQL 程序会生成约 10 万行 Rust 代码，即使使用拥有 64 个内核的强大机器，也会导致编译时间过长。 分析显示，LLVM 传递和代码生成是单线程的瓶颈，导致大多数内核处于空闲状态。

该解决方案涉及修改 SQL 到 Rust 的编译器，以生成许多小型、相互连接的代码仓库，而不是一个大型代码仓库。 每个 SQL 运算符都变成自己的代码仓库，导出一个函数来构建数据流的一部分。 代码仓库名称基于其 Rust 代码的哈希值，从而实现高效的增量构建。 当 SQL 代码略有更改时，只会重新编译具有修改后的哈希值的相应代码仓库，从而利用未更改代码仓库的缓存工件。

这种方法充分利用了所有 CPU 内核，大大缩短了编译时间。 虽然最初担心许多代码仓库的开销，但作者发现并行化的好处超过了缺点。 他们承认仍然存在一些谜团，因为尽管 CPU 使用率很高，但观察到的加速并不是线性的，这暗示了潜在的瓶颈，例如硬件资源争用或文件系统限制。 尽管存在这些未解之谜，但将他们的 Rust 代码拆分成数千个代码仓库，极大地改善了客户的编译时间。

---

## 24. 从零开始的可微编程

**原文标题**: Differentiable Programming from Scratch

**原文链接**: [https://thenumb.at/Autodiff/](https://thenumb.at/Autodiff/)

本文《从零开始的可微编程》介绍了可微编程，及其在机器学习以外领域日益增长的相关性，并阐述了区分代码的各种技术。文章首先回顾了微积分，重点关注导数、梯度、方向导数和链式法则。它强调了将导数视为向量之间映射的重要性。

文章随后讨论了通过梯度下降进行优化，解释了它的迭代过程、学习率的作用，以及诸如局部最小值和发散等潜在陷阱。文章强调了正则化技术的重要性。

文章的核心深入探讨了区分代码的不同方法：数值微分、符号微分和自动微分。数值微分虽然通过有限差分易于实现，但对于高维输入而言，计算成本很高，并且只能提供近似值。符号微分使用具有已知微分规则的特定领域语言，但生成的导数表达式可能会变得非常大。

---

## 25. OpenAI Codex CLI：轻量级终端编码助手

**原文标题**: OpenAI Codex CLI: Lightweight coding agent that runs in your terminal

**原文链接**: [https://github.com/openai/codex](https://github.com/openai/codex)

OpenAI Codex CLI 是一个轻量级的开源编码助手，可在您的终端中运行，利用 ChatGPT 级别的推理能力与您的代码进行交互和修改。它允许开发人员使用自然语言提示来自动化任务，例如重构、生成测试、更新文档和识别漏洞。

主要功能包括：

* **基于终端的交互：** 专为喜欢在终端中工作的开发人员而构建。
* **代码执行：** 可以在安全的沙盒中运行代码、操作文件和安装依赖项。
* **灵活的批准模式：** 通过 `--approval-mode` 标志提供不同级别的自主权：建议、自动编辑和完全自动。完全自动模式运行命令时禁用网络并进行目录沙盒化，以确保安全。
* **多模态输入：** 接受屏幕截图和图表。
* **可自定义的指令：** 通过 Markdown 文件支持个人和项目特定的指令。
* **非交互模式：** 可在 CI/CD 管道中使用。
* **安全性：** 利用平台特定的沙盒技术（macOS 上的 Apple Seatbelt，Linux 上的 Docker），并且需要明确批准才能执行潜在的风险操作。

该 CLI 需要 Node.js 22+ 和 Git（可选）。安装通过 npm 进行。配置通过 `~/.codex/config.yaml` 完成，并支持自定义模型偏好和定义自定义指令。

OpenAI 正在为使用 Codex CLI 的开源项目提供资金机会。欢迎贡献，指南强调重点明确的更改、测试覆盖率、文档和原子提交。

---

## 26. 用于轻松自信地构建MCP服务器的类型安全、直观的Go SDK

**原文标题**: A type-safe, intuitive Go SDK for building MCP servers with ease and confidence

**原文链接**: [https://github.com/ktr0731/go-mcp](https://github.com/ktr0731/go-mcp)

`go-mcp` 是一个 Go SDK，旨在简化模型上下文协议 (MCP) 服务器的开发。它提供了一个类型安全且直观的接口，用于构建具有工具、日志和提示等功能的服务器。

主要优势包括：

*   **类型安全：** 代码生成强制静态类型，防止运行时错误。
*   **直观 API：** Go 语言风格的接口简化了服务器开发。
*   **开发者友好：** 设计易于使用。

快速入门指南演示了如何通过定义服务器功能、使用 Go 结构体和描述定义工具、使用 `mcpgen` 生成代码以及实现服务器逻辑来创建 MCP 服务器。提供了示例目录结构和可运行的代码片段。

支持的功能包括 ping、工具、提示、资源订阅、更新通知、日志记录和取消。正在开发的功能包括批处理、可流式传输的 HTTP 传输和进度通知。由于 Go 在动态类型方面的限制，有意排除了动态提示和工具更改。欢迎在 MIT 许可证下贡献代码。

---

## 27. 这个“大学抗议者”不是真人，而是警方用于卧底的人工智能机器人。

**原文标题**: This 'College Protester' Isn't Real. It's an AI-Powered Undercover Bot for Cops

**原文链接**: [https://www.wired.com/story/massive-blue-overwatch-ai-personas-police-suspects/](https://www.wired.com/story/massive-blue-overwatch-ai-personas-police-suspects/)

本文揭露了“巨蓝”公司向美墨边境附近的美国警察部门出售人工智能驱动的“守望者”技术。“守望者”利用人工智能生成的网络身份，渗透并收集“大学抗议者”、“激进化”的活动人士和疑似人口贩运者的情报。这些人物角色拥有详细的背景故事和人工智能生成的图像，他们在社交媒体和通讯应用上与嫌疑人互动，试图获取证据。

亚利桑那州和德克萨斯州的执法机构正为此未经证实的技术支付巨额资金，理由是其具有打击人口贩运的潜力。然而，人们对其有效性、通过针对抗议者而可能违反第一修正案，以及其旨在解决的定义不清的问题表示担忧。例子包括旨在模仿对激进主义感兴趣的孤独离异女性、来自也门的年轻人，甚至未成年儿童的角色。

电子前沿基金会的戴夫·马斯等批评人士质疑这些人工智能驱动的卧底行动的目的和伦理影响。“巨蓝”公司声称其目标是将人口贩运者绳之以法并保护受害者，但关于其行动和逮捕结果的具体细节却很少。执法机构对这项技术讳莫如深，一些机构承认该技术尚未促成任何逮捕行动。此外，人们越来越担心人工智能可能会被用于贩运调查之外的移民和抗议活动中。

---

## 28. Show HN: Plandex v2 – 大型项目及任务的开源AI编码代理

**原文标题**: Show HN: Plandex v2 – open source AI coding agent for large projects and tasks

**原文链接**: [https://github.com/plandex-ai/plandex](https://github.com/plandex-ai/plandex)

Plandex v2 是一款开源的、基于终端的 AI 编码代理，旨在管理大型编码任务和真实项目。它支持高达 200 万 tokens 的上下文，并可以使用 tree-sitter 索引包含 2000 万以上 tokens 的目录。主要功能包括差异审查沙箱、用于调试的受控命令执行，以及结合 Anthropic、OpenAI、Google 和开源供应商的模型的能力。

Plandex 具有适应性，既为加载文件、规划、实施、命令执行和调试等任务提供完全自主性，也为开发人员提供精细控制。它专为处理大型项目而构建，具有智能上下文管理、可靠的文件编辑和快速的项目地图生成功能。

它支持可配置的自主性、终端命令和浏览器应用程序的自动调试，并提供用于头脑风暴的项目感知聊天模式。它通过语法和逻辑验证来优先考虑正确性，并具有版本控制、Git 集成（包括提交消息生成）和节省成本的上下文缓存功能。

安装非常简单，只需一行 CLI 命令即可安装。托管选项包括 Plandex Cloud（带有集成模型或 BYO API 密钥）以及使用 Docker 的自托管/本地模式。要开始使用，用户 `cd` 进入项目目录并运行 `plandex` 或 `pdx`。REPL 界面提供帮助文本，并提示用户在聊天模式和讲述模式之间切换，分别用于完善想法和进行详细规划。我们鼓励查阅文档，加入 Discord 服务器并参与社区贡献。

---

## 29. Haskell中的并发：快速、简单、正确

**原文标题**: Concurrency in Haskell: Fast, Simple, Correct

**原文链接**: [https://bitbashing.io/haskell-concurrency.html](https://bitbashing.io/haskell-concurrency.html)

本文推崇Haskell的并发处理方式，认为与传统线程或续传传递相比，它提供了一种快速、简单且正确的解决方案。文章首先强调了利用多核处理器和管理慢速I/O操作对并发的需求。虽然存在像Node.js这样使用事件驱动I/O的替代方案，但它们可能会导致调试难题。

Haskell使用由其运行时管理的绿色线程，结合了线程和事件驱动I/O的优点。`forkIO`函数产生线程，`async`包通过promises（`Async a`）提供控制，可以等待（`wait`）和取消（`cancel`）。文章介绍了更高级的抽象，如`concurrently`、`race`和`mapConcurrently`，它们通过自动处理线程取消和故障传播，简化了并发任务管理。

真正的魔力在于STM（软件事务内存），它使用诸如`TVar`和`TBQueue`等特殊类型以及`atomically`函数来确保原子读/写操作。这消除了对显式互斥锁的需求，并避免了诸如死锁和竞争条件等常见的并发问题。一个关键示例是可关闭队列（`TBCQueue`），其中读写操作与“打开”标志进行原子协调，使用`retry`进行阻塞操作，展示了STM的强大功能和易用性。作者认为，STM就像Rust的内存安全特性一样，消除了整个类别的并发错误。

---

## 30. Bash高级Shell脚本编程 (2006) [pdf]

**原文标题**: Advanced Shell Scripting with Bash (2006) [pdf]

**原文链接**: [http://uniforumchicago.org/slides/bash1.pdf](http://uniforumchicago.org/slides/bash1.pdf)

这份名为“Bash高级Shell脚本编程（2006）”的文档，似乎是一个损坏或不完整的PDF文件。其内容主要由编码数据组成，可能是构成PDF文档的文本、图像和格式指令的压缩表示。在提供的片段中，没有任何容易辨认的人类可读文本可以让我们理解其主题、目标受众或学习目标。因此，无法总结文章的内容。“/ProcSet [ /PDF /Text ]”的存在表明它打算包含文本元素，而“/ImageB /ImageC /ImageI”则指向可能包含位图、彩色和索引图像。“Bash高级Shell脚本编程（2006）”这个标题表明了主题，但如果没有正确的渲染，文档的实际内容仍然无法访问。本质上，它是没有解码器的数据，所以任何“摘要”都将是仅基于标题的推测。

---

## 31. 科学家开创橡胶废料再利用化学工艺

**原文标题**: Scientists pioneer chemical process to repurpose rubber waste

**原文链接**: [https://phys.org/news/2025-03-cleaner-future-scientists-chemical-repurpose.html](https://phys.org/news/2025-03-cleaner-future-scientists-chemical-repurpose.html)

本文详细介绍了北卡罗来纳大学教堂山分校的科学家开发的一种新的化学工艺，用于再利用橡胶废料，特别是废弃轮胎。该方法为热解等产生有害副产品的传统回收方法提供了一种可持续的替代方案。

该研究由 Aleksandr Zhukhovitskiy 博士领导，介绍了一种涉及 C–H 胺化和聚合物重排策略的两步工艺。该工艺将橡胶复杂的交联结构分解成可溶的、胺基功能化的材料，适用于制造环氧树脂。该过程在温和的条件（35-50°C）下在水性介质中进行，与需要极端温度或昂贵催化剂的方法相比，更环保且更具成本效益。

测试表明，模型聚合物的分子量显著降低，并且使用过的橡胶在六小时内完全分解。所得材料可用于生产强度与商业石油基树脂相似的环氧树脂。

研究人员还使用环境影响因子（E-factor）评估了环境影响。虽然由于溶剂的使用，总体E-factor 较高，但简单E-factor 较低得多，表明可以通过优化溶剂系统和反应条件来改进。这项研究为将橡胶废料转化为有价值的材料、减少对垃圾填埋场的依赖并最大限度地减少环境危害提供了一种有希望的方法。

---

## 32. 制冷如何改变了我们的食物

**原文标题**: How refrigeration changed our food

**原文链接**: [https://www.nytimes.com/2024/06/24/books/review/frostbite-nicola-twilley.html](https://www.nytimes.com/2024/06/24/books/review/frostbite-nicola-twilley.html)

萨莉·蒂斯代尔对尼古拉·特威利的《冻伤》的评论探讨了冷藏技术对我们的食物系统及其他领域的深刻影响。特威利深入研究了复杂的“冷链”，并以超市的香蕉为例，说明了将热带水果全年带给消费者所需的错综复杂的冷藏网络。

该评论强调了冷藏如何改变了食品生产、消费，甚至环境。19世纪，冷藏铁路车厢消除了城市屠宰场，导致肉类消费增加，土地利用发生巨大变化，包括野牛数量下降和美洲原住民流离失所。

家用冰箱的出现，这项相对较新的创新，进一步彻底改变了我们的饮食方式和内容。特威利认为，冷藏不仅重新设计了我们的餐盘，还重塑了我们的身体、家园、城市、景观和全球大气。虽然冷链为消费者提供了无尽的丰富，但该评论暗示了潜在的代价，表明为了追求全年供应和广泛分销，风味可能会被牺牲。

---

## 33. 该死的漏洞百出的MCP服务器

**原文标题**: Damn Vulnerable MCP Server

**原文链接**: [https://github.com/harishsg993010/damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)

DVMCP（即 Damn Vulnerable Model Context Protocol，易受攻击的模型上下文协议）是一个旨在突出 MCP 实现中安全漏洞的教育项目。 MCP 是一种标准化协议，允许应用程序以结构化方式向大型语言模型 (LLM) 提供上下文。

DVMCP 包含 10 个挑战，分为三个难度级别（简单、中等、困难），展示了各种攻击媒介，包括提示注入、工具中毒、过度权限、Rug Pull 攻击、工具阴影、间接提示注入、令牌盗窃、恶意代码执行、远程访问控制和多向量攻击。

该项目包括一个易受攻击的 MCP 服务器、文档和解决方案指南。建议使用 Docker 以获得稳定的环境。 推荐使用 CLINE (VSCode Extension) 作为推荐的 MCP 客户端。

该项目旨在教育安全研究人员、开发人员和 AI 安全专业人员了解 MCP 实现中潜在的安全问题以及如何缓解这些问题。它强调了在实现 MCP 服务器时安全最佳实践的重要性，并采用 MIT 许可证。它由 Harish Santhanalakshmi Ganesan 使用 cursor IDE 和 Manus AI 创建。

---

## 34. 12要素代理：可靠LLM应用模式

**原文标题**: 12-factor Agents: Patterns of reliable LLM applications

**原文链接**: [https://github.com/humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents)

AI智能体黑客Dex提出“十二要素智能体”，一套用于构建可靠的、适用于生产环境的LLM驱动应用程序的原则。他观察到，许多“AI智能体”主要由具有战略性LLM集成的确定性代码组成，这与通常与智能体框架相关的“提示-工具循环”范式不同。Dex认为，真正有效的智能体更依赖于传统的软件工程实践。

文章概述了一个从传统软件开发（以由Airflow等编排器管理的有向无环图(DAG)为代表）到智能体的最初承诺（即无需预定义的DAG，依靠LLM来确定路径，自主导航任务）的演变过程。这种“智能体循环”涉及LLM确定下一步，确定性代码执行工具，以及将结果反馈到上下文窗口。然而，这种方法在实践中常常不尽如人意。

核心论点是，将模块化智能体概念集成到现有产品中比仅仅依赖于完整的框架更有效。Dex概述了涵盖构建强大LLM应用程序的关键方面的12个要素，包括：

*   自然语言到工具调用
*   提示和上下文窗口所有权
*   将工具视为结构化输出
*   统一执行和业务状态
*   启动/暂停/恢复能力
*   通过工具调用实现人机协作
*   控制流管理
*   错误处理
*   智能体关注点和规模
*   触发和用户可访问性
*   无状态Reducer架构。

这篇文章是一篇实用指南，旨在通过将智能体设计的元素融入现有产品中，帮助软件工程师为客户构建高质量的AI驱动功能。

---

## 35. CVE基金会

**原文标题**: CVE Foundation

**原文链接**: [https://www.thecvefoundation.org/home](https://www.thecvefoundation.org/home)

CVE基金会成立，保障通用漏洞披露 (CVE) 项目的未来。该项目作为全球网络安全的重要组成部分已走过 25 年。此次行动的起因是美国政府决定不再续签与 MITRE 公司的合同，后者负责管理该项目。

此前，CVE 项目是一项由美国政府资助的倡议，这引发了人们对其可持续性和中立性的担忧。CVE 基金会旨在通过成为一个专注的非营利组织来解决这个问题，该组织的目标完全专注于 CVE 项目的使命：提供高质量的漏洞识别，并为全球防御者维护 CVE 数据的完整性。

据该基金会官员肯特·兰德菲尔德称，CVE 对于网络安全生态系统至关重要。 CVE 基金会的成立旨在消除漏洞管理中的单一故障点，并确保 CVE 项目成为一个值得信赖、社区驱动的倡议，反映了全球威胁形势的本质。有关基金会的结构、过渡计划以及社区参与机会的更多信息即将发布。

---

## 36. 太阳系外行星发现外星生命“最具希望的迹象”

**原文标题**: “Most promising signs yet” of alien life on a planet beyond our Solar System

**原文链接**: [https://www.skyatnightmagazine.com/news/k2-18b-dimethyl-sulfide](https://www.skyatnightmagazine.com/news/k2-18b-dimethyl-sulfide)

天文学家使用詹姆斯·韦伯太空望远镜在系外行星K2-18b的大气层中探测到有希望的“生物特征”——二甲基硫醚和二甲基二硫醚。该行星距离地球124光年，位于其恒星的宜居带内。这些化学物质主要由地球上的海洋生物产生，可能暗示着生命的存在。

K2-18b是一颗“海洋”行星，表明它拥有液态海洋和富氢大气层。虽然之前的研究在K2-18b的大气层中发现了甲烷和二氧化碳，但这项最新的研究提供了更强的证据表明存在二甲基硫醚和二甲基二硫醚，这些物质是用韦伯望远镜上的不同仪器探测到的。

该团队仍然保持谨慎，承认其他非生物过程也可能解释这些化学物质的存在。目前的探测结果具有“三西格玛”的统计显著性，低于确认为科学发现所需的“五西格玛”阈值。

科学家通过研究恒星光在凌日期间穿过系外行星大气层的情况来分析其大气层，这会留下化学指纹。K2-18b上二甲基硫醚和二甲基二硫醚的浓度明显高于地球，与海洋世界的理论预测相符。进一步的研究对于确定这些分子是否能在观察到的水平上非生物地产生至关重要。在承认需要保持怀疑态度和进一步测试的同时，研究人员认为这项发现代表着在回答“我们在宇宙中是否孤独”这个问题上迈出了重要一步。

---

## 37. 一场被遗忘的战役如何创造了一个更和平的世界

**原文标题**: How a Forgotten Battle Created a More Peaceful World

**原文链接**: [https://worldhistory.substack.com/p/how-a-forgotten-battle-created-a](https://worldhistory.substack.com/p/how-a-forgotten-battle-created-a)

无法访问文章链接。

---

## 38. Erlang Solutions博客精选

**原文标题**: Erlang Solutions' Blog round-up

**原文链接**: [https://www.erlang-solutions.com/blog/erlang-solutions-blog-round-up/](https://www.erlang-solutions.com/blog/erlang-solutions-blog-round-up/)

Erlang Solutions博客综述涵盖了科技界一系列重要议题，旨在为企业和科技爱好者提供资讯。文章重点介绍了大数据在医疗保健领域的变革力量，强调使用Erlang、Elixir和SAFE等技术的预测性健康趋势、精准医疗和数据安全。

该博客还探讨了数字钱包日益增长的重要性，详细介绍了其优势，如提高安全性、节省成本和全球访问，同时也承认了相关的挑战。另一篇文章介绍了关于“BEAM中的女性”调查的主要结论，讨论了代表性差距以及Elixir社区内榜样的重要性。

此外，该综述还提供了提高物联网业务安全性的实用技巧，包括强密码、数据加密、定期审计、团队培训以及禁用未使用的功能。最后，它还探讨了金融科技企业的DORA合规性问题，解释了该法案的影响，并概述了构建弹性和合规运营的步骤。Erlang Solutions旨在为受众简化复杂的技术话题，并邀请进一步讨论。

---

## 39. 小丑表演：小丑艺术原理

**原文标题**: Clowning Around: On the Principles of Clowning

**原文链接**: [https://funnyhow.substack.com/p/clowning-around-](https://funnyhow.substack.com/p/clowning-around-)

无法访问文章链接。

---

## 40. 自己建ISP不付康卡斯特费用男子，将其服务扩展到数百户家庭 (2022)

**原文标题**: Man who built ISP instead of paying Comcast expands to hundreds of homes (2022)

**原文链接**: [https://arstechnica.com/tech-policy/2022/08/man-who-built-isp-instead-of-paying-comcast-50k-expands-to-hundreds-of-homes/](https://arstechnica.com/tech-policy/2022/08/man-who-built-isp-instead-of-paying-comcast-50k-expands-to-hundreds-of-homes/)

密歇根男子Jared Mauch凭借《美国救援计划》提供的260万美元政府资助，正在扩展他的光纤到户ISP，Washtenaw光纤地产有限责任公司。Mauch对AT&T和Comcast提供的宽带服务选择不足感到失望（Comcast报价5万美元才肯扩展网络），最初他自建网络，仅为自己家和几个邻居提供服务。

现在，有了政府资助，他将把14英里的光纤网络再扩展38英里，目标是覆盖Washtenaw县近600处房产，超出合同要求的417处。他提供对称的100Mbps服务，每月55美元；1Gbps服务，每月79美元，两者都提供无限流量，没有隐藏费用，并且参与FCC的经济适用连接计划。

在Akamai担任网络架构师的Mauch计划在2023年底前完成项目的一半，并在2024年底前完成剩余部分，远早于2026年的截止日期。尽管面临设备成本上涨，他还是投资了工业空气压缩机等设备。该县将此誉为“历史性的”宽带投资，并选择了包括Comcast和Charter在内的其他三家ISP来覆盖其他地区。Mauch已成为当地名人，甚至被邻居保存在电话里，备注为“光纤电缆人”，并为以前服务不足的农村社区提供了至关重要的服务。

---

## 41. 美国低估了制造业回流的难度。

**原文标题**: America underestimates the difficulty of bringing manufacturing back

**原文链接**: [https://www.molsonhart.com/blog/america-underestimates-the-difficulty-of-bringing-manufacturing-back](https://www.molsonhart.com/blog/america-underestimates-the-difficulty-of-bringing-manufacturing-back)

莫尔森·哈特认为，美国政府为将制造业迁回美国而征收的最新关税是错误的，并且很可能会失败。 他提出了 14 个理由，主要集中在美国低估了制造业回流的复杂性和难度这一事实上。

关键原因包括关税不足以抵消在中国等国家制造业的现有成本优势，这些国家拥有强大的工业供应链、成熟的专业知识和强大的职业道德。 他断言，美国的工业供应链薄弱，关键部件主要在亚洲生产。

哈特批评了美国的劳动力，指出与中国劳动力相比，美国劳动力存在职业道德和基本技能不足等问题。 他还强调缺乏足够的基础设施，例如可靠的电力和充足的运输，来支持国内制造业的显著增长。

他指出，建造工厂和建立高效生产需要很长的交付周期，再加上围绕关税的不确定性和复杂性，导致商业投资停滞不前。 最终，他认为许多美国人不愿意或没有准备好从事要求苛刻的制造业工作，而且劳动力市场已经相对紧张。

---

## 42. 查询引擎：推送与拉取 (2021)

**原文标题**: Query Engines: Push vs. Pull (2021)

**原文链接**: [https://justinjaffray.com/query-engines-push-vs.-pull/](https://justinjaffray.com/query-engines-push-vs.-pull/)

本文探讨查询引擎中的“推”与“拉”执行模型，旨在阐明它们的差异和实际意义。

**基于拉取（火山/迭代器）的引擎**是消费者驱动的；算子只有在下游算子请求时才生成行。本文提供了一个基本的 Javascript 实现。

**基于推送（反应式/流式）的引擎**是生产者驱动的；算子在数据可用时向下游推送数据。提供了一个基于推送引擎的 Javascript 实现。

本文探讨了 Snowflake 的 SIGMOD 论文提出的两个关键问题：

1. **DAG 形计划：** 基于推送的系统比基于拉取的系统更有效地处理有向无环图 (DAG)，而基于拉取的系统传统上是树状结构的。SQL 的 `WITH` 子句和查询计划器优化可以受益于 DAG。基于拉取的系统在 DAG 中调度和管理中间结果的生命周期方面面临挑战，可能需要无限缓冲。基于推送的系统将调度与输出请求分离，允许算子强制消费者处理行，从而消除对大量缓冲的需求。

2. **缓存效率：** 虽然 Snowflake 的论文表明基于推送的系统提高了缓存效率，但作者认为，其优势更多地源于将查询编译为机器代码（例如，使用 LLVM），而不是推送模型本身。编译基于推送的查询可以产生更直接、更容易展开的代码。

本文总结道，虽然入门数据库材料侧重于迭代器（拉取）模型，但现代分析系统越来越多地探索推送模型。“最佳”选择取决于查询引擎的特定需求。边界阻抗不匹配和算法适用性被提及为考虑因素。

---

## 43. eInk模式：让网页更易读

**原文标题**: eInk Mode: Making web pages easier to read

**原文链接**: [https://jackscogito.blogspot.com/2025/04/e-ink-mode-making-web-pages-easier-to.html](https://jackscogito.blogspot.com/2025/04/e-ink-mode-making-web-pages-easier-to.html)

本文介绍了“墨水屏模式”，这是一种网页浏览模式，旨在优化在如电子阅读器和显示器等墨水屏设备上浏览网站的体验，模仿阅读实体书籍的感觉。墨水屏模式以分页格式呈现网页内容，通过点击屏幕左侧或右侧进行导航，类似于翻页。它通过最小化用户界面元素来优先呈现内容。

本文详细介绍了墨水屏模式的功能和操作。用户可以通过点击墨水屏图标或在网页上从左向右滑动来进入墨水屏模式。该模式支持丰富的姿势控制，例如向上/向下滑动跳到页面顶部/底部，以及为桌面用户提供的键盘快捷键。

一个关键功能是防止意外点击超链接和图像，需要长按才能激活它们。用户还可以使用双指捏合手势调整文本大小，确保没有文本被截断。另一个功能是跳转到目录。

墨水屏模式提供高亮注释工具，可以通过滑动或键盘快捷键访问，可以通过多指轻敲或键盘命令选择多种颜色。一个浮动操作按钮提供对高亮颜色的访问和突出显示内容的“笔记本”。这个笔记本编译所有突出显示的段落，按颜色分类，并且可以保存为PDF文件，其中包含指向原始网页的链接，用于笔记和存档。文章最后提到跨页高亮功能。

---

## 44. OpenAI o3 和 o4-mini

**原文标题**: OpenAI o3 and o4-mini

**原文链接**: [https://openai.com/index/introducing-o3-and-o4-mini/](https://openai.com/index/introducing-o3-and-o4-mini/)

无法访问文章链接。

---

## 45. 4chan 沙提駭客與清潔工電郵洩露

**原文标题**: 4chan Sharty Hack And Janitor Email Leak

**原文链接**: [https://knowyourmeme.com/memes/events/april-2025-4chan-sharty-hack-and-janitor-email-leak](https://knowyourmeme.com/memes/events/april-2025-4chan-sharty-hack-and-janitor-email-leak)

无法访问文章链接。

---

## 46. WordPress 功能 API

**原文标题**: WordPress Feature API

**原文链接**: [https://github.com/Automattic/wp-feature-api](https://github.com/Automattic/wp-feature-api)

WordPress功能API是一个旨在标准化和暴露WordPress功能的系统，供服务器、客户端和人工智能系统（如LLM）使用。它提供了一个统一的WordPress功能注册表，利用现有的REST端点等功能，使其更易于发现和访问。该API采用MCP规范，专为WordPress的双服务器和客户端特性量身定制，使功能可以在后端和前端使用。虽然没有实现完整的MCP服务器，但功能注册表可以被现有的MCP服务器使用。

该项目结构为一个单一代码仓库，包含多个包，其中包括：用于与功能注册表交互的客户端SDK（`@wp-feature-api/client`）；包含标准客户端功能的库（`@wp-feature-api/client-features`）；以及展示API用法的演示插件（`wp-feature-api-demo`）。

一个关键方面是能够基于属性、关键字、类别、资格回调和上下文匹配来过滤功能，确保为特定用户意图和上下文提供最相关的工具。安装包括克隆存储库，使用`npm run setup`安装依赖项，以及使用`npm run build`构建包。可以使用`@wordpress/env`运行演示，并激活主“WordPress Feature API”插件和“wp-feature-api-demo”插件。该API旨在为WordPress中超越LLM消费的功能提供一个通用接口。

---

## 47. 违反Llama社区许可协议

**原文标题**: Breaking the Llama Community License

**原文链接**: [https://notes.victor.earth/youre-probably-breaking-the-llama-community-license/](https://notes.victor.earth/youre-probably-breaking-the-llama-community-license/)

本文深入探讨Llama社区许可协议的潜在违规行为，重点关注人工智能社区经常忽略的方面。文章突出了Llama被宣传为“开源”与其实际限制性许可条款之间的差异。

作者认为，仅仅使用或分发Llama材料，无论是否点击“我接受”，都会使使用者受到协议的约束。主要违规行为包括未在网站或产品上显著显示“Built with Llama”（使用Llama构建），该要求在Llama 3.x许可中引入。Ollama和Openrouter.ai等知名平台被列为潜在的违规者。

文章还指出许可规定的命名规范，要求所有从Llama衍生的微调模型都以“Llama-”开头，这一规则被广泛忽视。例如，“Hermes 3”被认为是违规行为。 NVIDIA的“Llama-3.3-Nemotron-Super-49B-v1”被强调为符合许可条款。

最后，作者讨论了“可接受使用政策”，特别是披露使用Llama构建的AI系统的任何已知危险（包括偏见和事实错误）的义务。作者强调了“适当披露”的模糊性。

作者最后推测了广泛无视许可的原因，提出了可能的无知、精打细算的冒险或与Meta达成的单独协议。文章强调，对于任何分发或使用基于Llama产品的个人来说，仔细审查Llama社区许可至关重要，因为Meta保留在未来执行这些条款的权利。

---

## 48. Zig编程语言的高吞吐量解析器

**原文标题**: A high-throughput parser for the Zig programming language

**原文链接**: [https://github.com/Validark/Accelerated-Zig-Parser](https://github.com/Validark/Accelerated-Zig-Parser)

本文详细介绍了 Zig 编程语言的高吞吐量词法分析器和语法分析器的开发，旨在显著提高性能，超越主线 Zig 词法分析器。该项目探索了两种词法分析器实现：一种使用位串来跳过延续字符匹配，另一种采用向量压缩来同时查找所有 token 范围。

性能基准测试表明了显著的提升。在一个测试环境中，一个版本相比于旧版词法分析器，速度提高了 2.75 倍，内存使用量减少了 2.47 倍。作者概述了高性能的设计原则：SIMD（单指令多数据）用于字节的并行处理，以及 SWAR（寄存器内的 SIMD）技术。这些技术被用于识别标识符、关键字、空格和注释。

该设计还强调通过使用完美哈希函数进行关键字和运算符识别来减少不可预测的分支。作者利用 Zig 的编译时执行特性来自动管理哈希方案中的虚拟运算符/关键字。其他优化包括为 token 分配上限内存，并在文件边界使用哨兵来简化代码并消除边界检查。该工作通过存储 token 长度而不是起始索引来解决内存消耗问题，从而进一步压缩数据。

---

## 49. Meta AI 如何认定超过 700 万本书籍没有“经济价值”

**原文标题**: How Meta AI Staff Deemed More Than 7M Books to Have No "Economic Value"

**原文链接**: [https://www.vanityfair.com/news/story/meta-ai-lawsuit](https://www.vanityfair.com/news/story/meta-ai-lawsuit)

本文详细介绍了 Richard Kadrey 等人诉 Meta Platforms 的版权诉讼，该诉讼涉及 Meta 使用数百万盗版书籍来训练其 Llama AI 模型。原告包括 Andrew Sean Greer、Junot Díaz 和 Sarah Silverman 等著名作家，他们声称 Meta 未经许可或支付费用，使用 LibGen 和 Z-Library 等非法数据库获取书籍，侵犯了他们的版权。

Meta 辩称其行为属于“合理使用”，认为其 LLM 项目具有“高度转化性”，并且使用受版权保护的材料对于开源 AI 的开发至关重要。他们还辩称，单本书籍在训练 AI 方面的经济价值微不足道，因为任何单本书籍的贡献都极小。这一论点是其合理使用主张的核心。

该诉讼揭示了 Meta 内部对使用盗版材料的讨论，一些员工对其中的伦理和法律影响表示担忧。内部沟通显示，Meta 研究人员寻求尽可能多的长篇写作，包括所有类型的书籍，同时也试图删除版权页。

文章还提到了 Meta 与出版商就许可费进行的初步讨论失败，理由是与数百万作者谈判的复杂性和成本。Meta 前律师 Mark Lemley 认为，版权法应侧重于 AI 的输出，而不是训练数据。

该案件是针对 AI 公司的众多版权诉讼之一，提出了关于生成式 AI 时代艺术和文学的价值，以及大型语言模型是否应被允许摄取受版权保护的作品以产生其输出的根本问题。

---

## 50. 两步棋，AlphaGo与李世乭重新定义未来 (2016)

**原文标题**: In Two Moves, AlphaGo and Lee Sedol Redefined the Future (2016)

**原文链接**: [https://www.wired.com/2016/03/two-moves-alphago-lee-sedol-redefined-future/](https://www.wired.com/2016/03/two-moves-alphago-lee-sedol-redefined-future/)

本文回顾了围棋世界冠军李世石与谷歌人工智能系统AlphaGo之间具有历史意义的围棋对弈。AlphaGo的胜利标志着一个重要的里程碑，展示了人工智能的快速发展，尤其是在复杂战略游戏领域。

本文重点介绍了两个关键的落子：AlphaGo在第二局中的第37手，这一步棋非常不寻常，甚至专家最初都认为这是一个错误；以及李世石在第四局中的第78手，因其精妙和出人意料而被誉为“神之一手”。据说这两步棋的落子概率都只有万分之一。

这些落子的意义不仅在于其出人意料的性质，还在于它们揭示了人机交互的未来。AlphaGo的胜利展示了人工智能在某些领域超越人类能力的潜力。然而，李世石的“神之一手”强调了人类的直觉和创造力仍然是无价的。

作者认为，未来不是人与机器的对立，而是人与机器的合作。通过向人工智能学习，人类可以扩展自己的理解和能力。围棋棋手樊麾的排名飙升，李世石本人也表示AlphaGo让他对围棋有了新的认识。文章总结说，人类智能和人工智能的融合将带来双方都无法单独实现的进步。

---

## 51. TikTok正以工业规模危害儿童

**原文标题**: TikTok Is Harming Children at an Industrial Scale

**原文链接**: [https://www.afterbabel.com/p/industrial-scale-harm-tiktok](https://www.afterbabel.com/p/industrial-scale-harm-tiktok)

TikTok正以工业规模危害儿童
本文《TikTok正以工业规模危害儿童》认为，TikTok正在对儿童和年轻人造成重大危害。作者乔恩·海特和扎克·劳施主要引用了14个州的总检察长在针对TikTok的诉讼中提交的法律摘要，其中引用了内部报告、备忘录和员工声明。

文章将证据归纳为五类危害：成瘾和强迫性使用、抑郁和焦虑、接触色情内容、暴力和毒品、性剥削和儿童性虐待材料。TikTok内部人士承认这些危害，但通常将参与度指标置于用户福祉之上。文章强调了TikTok对其成瘾算法、操纵性设计功能（如无限滚动和持续通知）以及年轻用户对此类策略的脆弱性的认知。

作者还指出，TikTok的家长控制功能无效，内容审核不力，并引用内部研究表明，有害内容的泄露率很高，例如恋童癖正常化和未成年人性招揽。本文旨在告知家长TikTok的商业行为，展示该公司如何意识到其对儿童心理健康和发展的负面影响，但仍然优先考虑增长和参与度。最终，作者认为，由于TikTok对儿童造成广泛的危害，美国应欢迎潜在的TikTok禁令。

---

## 52. 展示HN：初创公司成功计算器

**原文标题**: Show HN: Startup Success Calculator

**原文链接**: [https://app.tactyqal.com](https://app.tactyqal.com)

“Show HN：创业成功计算器”帖子可能指向一个旨在帮助创始人评估其创业成功潜力的工具或资源。 标题表明是一个计算器，这意味着一个利用指标和信号来预测或估计成功可能性的互动工具。由于内容仅为“startup-success-signal”，因此在没有访问链接资源的情况下，不可能了解该工具的具体细节。 但是，我们可以根据标题推断出以下内容：

*   **目的：** 该工具旨在提供有关创业公司成功几率的指示。
*   **方法：** 它可能使用计算器格式，表明存在用于各种创业公司指标或特征（例如，市场规模、团队经验、资金）的输入字段。
*   **输出：** 输出可能是一个分数、百分比或定性评估（例如，“高潜力”、“中等风险”），表明成功的可能性。
*   **目标受众：** 该工具专为寻求以可量化或结构化方式评估创业公司潜力的创业公司创始人、投资者，以及潜在的导师而设计。

本质上，这篇文章突出了一个新的资源，旨在帮助评估创业成功，大概是通过计算或公式化方法。 需要更多信息来了解“计算器”考虑的具体因素和使用的底层算法。

---

## 53. TLS证书有效期将正式缩短至47天

**原文标题**: TLS certificate lifetimes will officially reduce to 47 days

**原文链接**: [https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days](https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days)

DigiCert博客：TLS证书最长有效期将于2029年缩短至47天

该DigiCert博客文章讨论了CA/浏览器论坛决定于2029年3月15日前将TLS证书的最长有效期缩短至47天，并从2026年3月开始逐步缩短。此变更的原因是人们担心证书信息随着时间的推移而失去可信度，以及证书吊销系统不可靠。

推出时间表如下：

*   **2026年3月15日前：** 最长有效期和验证重用期为398天。
*   **2026年3月15日：** 最长有效期和验证重用期为200天，SII验证重用期缩短至398天。
*   **2027年3月15日：** 最长有效期和验证重用期为100天。
*   **2029年3月15日：** 最长有效期为47天，验证重用期为10天。

苹果公司提出了这项变更，他们认为更短的有效期要求必须实现自动化才能有效地管理证书生命周期，并降低与吊销证书相关的风险。 缩短的验证重用期突显了频繁重新验证的必要性。

DigiCert强调，更短的证书有效期不会增加年度订阅客户的成本。 他们预计将转向自动化，并提供Trust Lifecycle Manager和CertCentral等解决方案（包括ACME支持）来促进这一过渡。 该公司鼓励读者探索自动化选项，以有效管理证书生命周期。

---

## 54. 6502程序员使用的脏技巧 (2019)

**原文标题**: Dirty tricks 6502 programmers use (2019)

**原文链接**: [https://nurpax.github.io/posts/2019-08-18-dirty-tricks-6502-programmers-use.html](https://nurpax.github.io/posts/2019-08-18-dirty-tricks-6502-programmers-use.html)

本文探讨了Commodore 64编程竞赛中，6502程序员为了用最少字节绘制两条对角线而使用的各种“肮脏”技巧。文章分析了提交的作品，并详细介绍了用于优化的技术。

核心挑战在于操纵屏幕和颜色RAM来绘制线条。最初的方法涉及直接内存写入和展开循环，但这些方法效率不高。然后，文章深入研究了几种减少代码大小的“肮脏”技巧：

*   **滚动：** 代码不是为每个像素计算内存地址，而是在屏幕的最后一行绘制，并使用ROM例程(`JSR $E8EA`)向上滚动整个屏幕，从而节省了地址计算的开销。
*   **自修改代码 (SMC)：** 用自修改代码替换冗余的代码序列可以减少总字节数。
*   **利用开机状态：** 假设程序启动时的寄存器值和内存内容，从而节省初始化字节。具体来说，利用零页内存（$d5, $22）来避免显式加载常量。
*   **更小的启动：** 使用堆栈操作或BASIC热启动向量覆盖来消除BASIC启动序列，使程序可以直接执行。
*   **非常规控制流：** 重构控制流并利用条件分支而不是绝对跳转可以最大限度地减少分支代码的大小。将滚动操作移动到循环的顶部可减少跳过最后一帧的开销。
*   **位压缩线条绘制：** 将线条模式打包成一个8位常量，可以节省递增线条计数器的开销。

获胜作品通过结合这些技巧实现了34字节，突出了内存利用和指令级优化对于最小化6502上的代码大小的重要性。

---

## 55. 随机微积分导论 (2022)

**原文标题**: An Introduction to Stochastic Calculus (2022)

**原文链接**: [https://bjlkeng.io/posts/an-introduction-to-stochastic-calculus/](https://bjlkeng.io/posts/an-introduction-to-stochastic-calculus/)

本文旨在介绍随机微积分，它是标准微积分的扩展，用于分析随机过程。其动机是需要对涉及随机性的物理和金融现象进行建模，这些现象通常由随机微分方程表示。一个关键挑战来自噪声项，特别是“白噪声”，这是一种具有非相关波动和无限方差等属性的理论构造，使得传统积分变得困难。

然后，本文深入探讨概率的测度论定义、概率空间和随机变量，为理解随机微积分提供所需的严格基础。它涵盖了诸如σ-代数、可测空间和概率测度等概念，强调了它们在处理连续时间随机过程中常见的不可数无穷时的重要性。

本文概述了随机过程的结构，包括定义、示例（如伯努利过程）以及诸如适应过程和维纳过程等概念。它进一步探讨了伊藤微积分，这是一种用于布朗运动的特定类型的随机微积分，涵盖了伊藤过程、伊藤积分和伊藤引理。最后，它讨论了随机微积分的应用，特别是在期权定价的布莱克-斯科尔斯-莫顿模型和用于模拟随机现象的朗之万方程中。本文旨在提供直觉、严谨和示例的结合，以促进对这一复杂主题的理解。

---

## 56. 雅达利1200XL惨败

**原文标题**: The Atari 1200XL Fiasco

**原文链接**: [https://www.goto10retro.com/p/the-atari-1200xl-fiasco](https://www.goto10retro.com/p/the-atari-1200xl-fiasco)

本文讨论了雅达利1200XL，这是一款旨在取代雅达利800并与Commodore 64竞争的短命电脑。它于1983年初发布，拥有时尚的新设计、64K内存以及多项键盘改进，包括功能键和帮助键。

然而，1200XL因兼容性和价格这两个关键问题而商业上失败。更新后的ROM导致与流行软件（如Letter Perfect）不兼容，令用户不满。此外，其800美元的售价远高于Commodore 64，使其对消费者缺乏吸引力。其他问题包括缺少内置BASIC以及SIO端口缺少+12V电源。

1200XL的失败导致更便宜且更兼容的雅达利800销量增加。雅达利于1983年6月迅速停产了1200XL，并用更成功的600XL和800XL取而代之。

尽管最初失败，但雅达利1200XL现在因其稀有性而成为备受追捧的收藏品。它的键盘备受好评，并且可以通过修改来解决其硬件兼容性问题。如今，软件兼容性已不再是问题，因为旧程序有可用的解决方法。虽然比其后继者更大且缺少内置BASIC，但1200XL仍然是雅达利历史上令人着迷的一部分。

---

## 57. 从零开始的Nix三角函数数学库

**原文标题**: Nix Trigonometric Math Library from Ground Zero

**原文链接**: [https://lantian.pub/en/article/modify-computer/nix-trigonometric-math-library-from-zero.lantian/](https://lantian.pub/en/article/modify-computer/nix-trigonometric-math-library-from-zero.lantian/)

本文详细介绍了作者使用纯Nix实现三角函数，以计算其VPS节点间网络延迟的历程。该方法基于经纬度坐标，并使用Haversine公式。最初使用Python的`geopy`库由于Nix为每次计算创建隔离的构建环境而速度缓慢。

随后，作者从头开始开发了一个Nix库，实现了：

*   **sin, cos, tan:** 使用泰勒展开，通过迭代计算每个展开项来优化，以避免精度损失，并在该项低于指定的精度阈值时终止。余弦从正弦派生，正切从正弦和余弦派生。
*   **arctan:** 泰勒展开被证明太慢。因此采用了一种近似方法：反正切函数使用多项式回归在[0,1]区间上进行近似，其他范围使用反正切恒等式映射到此区间。
*   **sqrt:** 使用牛顿法实现迭代近似。

最后，使用这些函数实现Haversine公式来计算距离，然后基于光速计算理论网络延迟。作者提供了每个函数的代码片段，并包含一个指向其GitHub存储库 (xddxdd/nix-math) 的链接，其中包含完整的库。文章最后演示了如何在Nix Flake中使用该库。目标已实现：无需依赖Python等外部工具即可计算近似网络延迟，从而实现更快、更可重现的Nix构建。

---

## 58. 嗅嗅：一款针对蓝牙5和4.x LE的嗅探器

**原文标题**: Sniffle: A sniffer for Bluetooth 5 and 4.x LE

**原文链接**: [https://github.com/nccgroup/Sniffle](https://github.com/nccgroup/Sniffle)

Sniffle：基于TI CC1352/CC26x2硬件的蓝牙5和4.x(LE)嗅探器。支持BT5 PHY模式、扩展广播、信道选择算法，并可在所有三个主要信道上嗅探广播，以提高可靠性。

**主要特性：**

*   支持蓝牙5和4.x LE。
*   BT5/4.2扩展长度数据包。
*   BT5信道选择算法。
*   BT5 PHY模式。
*   通过MAC、RSSI、IRK或字符串进行广播过滤。
*   BT5扩展广播（非周期性）。
*   捕获目标MAC在所有三个主要信道上的广播。
*   PCAP导出（兼容Ubertooth）和Wireshark插件。
*   可扩展的Python主机端软件。

**硬件

支持多种TI Launchpad开发板，包括CC26x2R、CC2652RB、CC1352R、CC1352P、CC2652R7、CC1352P7、CC2651P3和CC1354P10，以及SONOFF CC2652P USB Dongle Plus和EC Catsniffer V3。

**软件

需要ARM GNU工具链、TI SimpleLink Low Power F2 SDK、TI DSLite Programmer和带有PySerial的Python 3.9+。固件可以从源代码构建，也可以使用UniFlash/DSLite刷入预编译的二进制文件。

**安装：**

提供了安装GCC、TI SDK、DSLite以及将固件刷入各种支持设备（TI Launchpad、SONOFF dongle、Catsniffer V3）的说明。应仔细遵循每种设备类型的具体说明。

**用法：**

`sniff_receiver.py`脚本提供了命令行选项，用于指定串口、波特率、广播信道、RSSI滤波器、MAC地址滤波器、IRK滤波器、字符串滤波器和输出文件。它还支持主动/被动扫描、扩展广播捕获和CRC错误捕获。提供了有关利用MAC/IRK过滤来跟随广播并进行可靠的连接嗅探的说明。

---

## 59. 科学：无尽的前沿 (1945) [pdf]

**原文标题**: Science, the Endless Frontier (1945) [pdf]

**原文链接**: [https://nsf-gov-resources.nsf.gov/2023-04/EndlessFrontier75th_w.pdf](https://nsf-gov-resources.nsf.gov/2023-04/EndlessFrontier75th_w.pdf)

我无法直接分析PDF文件的内容，从而提供对《科学：无尽的前沿》（1945）的全面总结。提供的文本似乎是PDF的原始编码内容，而不是报告的实际可读文本。

然而，根据标题和历史背景，我可以推断出报告可能的主要观点：

《科学：无尽的前沿》（1945）由范内瓦·布什应富兰克林·D·罗斯福总统的要求撰写，是一份具有里程碑意义的文件，倡导政府资助美国的科学研究。

**可能的主要观点：**

*   **战后对科学的需求：** 该报告可能认为，二战期间取得的科学进步应继续并应用于和平时期的需求。
*   **政府资助至关重要：** 它倡导联邦政府支持基础科学研究，强调这种研究对于长期经济增长、公共卫生和国家安全至关重要。
*   **基础研究的重要性：** 该报告可能强调了基础研究（基础探究）和应用研究（实际应用）之间的区别，并主张优先发展基础研究，将其作为未来创新的基础。
*   **支持教育和培训：** 它可能强调了教育和培训未来一代科学家和工程师的重要性。
*   **分散式管理：** 该报告可能建议，政府资助应通过大学等分散式机构进行管理，而不是直接由政府机构管理，以确保学术自由并培养创造力。
*   **影响：** 该报告的建议对美国科技政策的发展产生了重大影响，促成了国家科学基金会（NSF）的成立，并塑造了沿用至今的政府支持科学研究的模式。

---

## 60. Jellyfin：Spotify的替代方案

**原文标题**: Jellyfin as a Spotify alternative

**原文链接**: [https://coppolaemilio.com/entries/i-left-spotify-what-happened-next/](https://coppolaemilio.com/entries/i-left-spotify-what-happened-next/)

Emi 记录了他们离开 Spotify 的旅程，详细描述了寻找合适的本地音乐播放替代品的挫败感。起初，他们对 Winamp、VLC 和 Foobar2000 等传统音乐播放器感到失望，觉得它们笨重且难以使用。他们甚至尝试构建一个自定义的基于 Web 的音乐播放器，但遇到了离线访问的限制。Apple Music 曾作为临时解决方案，但存储限制和持续不断的广告令人不满。

最终，Emi 通过 Jeff Geerling 的视频发现了 Jellyfin，一个开源媒体服务器解决方案。Jellyfin 提供了他们想要的所有功能，包括流媒体和通过 Finamp 等专用应用程序进行离线播放的功能。虽然自托管最初是一个令人担忧的问题，但 Emi 发现设置起来出奇地容易，甚至使用一台旧电脑作为家庭服务器。

Jellyfin 的积极体验促使 Emi 进一步拥抱自托管，并将 Immich（一个 Google 相册替代品）添加到他们的设置中。作者鼓励读者探索自托管，以此来更好地控制他们的数字内容并从任何地方访问它。他们设想了一个未来，个人将减少对集中式服务的依赖，更多地依赖于个人管理的媒体解决方案。文章最后呼吁大家尝试自托管，强调它的可访问性和潜在好处。

---

## 61. 谷歌人...前谷歌人

**原文标题**: Googler... ex-Googler

**原文链接**: [https://nerdy.dev/ex-googler](https://nerdy.dev/ex-googler)

前谷歌员工亚当对其在谷歌的角色被意外取消表示震惊和愤怒。他强调，他被告知解雇并非基于绩效，并且他有可能在谷歌内部找到另一个职位，但他的公司资源访问权限却立即被撤销，这让他感到不受欢迎。

他强调了裁员的时机具有讽刺意味，发生在他参加Chrome团队建设活动，并积极为创新项目做出贡献之时。他感叹失去了他所期待的机会，包括在Google I/O上的演讲以及他参与的与CSS和Web开发者工具相关的各种Google项目。

亚当列举了大量现在已失去的职责和贡献，包括他作为CSS工作组成员、开发者办公时间以及对重要代码库的访问权限。他还承认，他多年来建立的关系也可能失去。

他表达了背叛、缺乏赏识、羞耻和愤怒的感觉，声称自己感觉像一个大型公司里可随意丢弃的“齿轮”。他提供了Bluesky上的联系方式和一个个人电子邮件地址，供那些想联系他的人使用，但他预计由于情况过于复杂，回复可能会延迟。

---

## 62. 没有废话的马尔可夫链蒙特卡洛 (2015)

**原文标题**: Markov Chain Monte Carlo Without All the Bullshit (2015)

**原文链接**: [https://www.jeremykun.com/2015/04/06/markov-chain-monte-carlo-without-all-the-bullshit/](https://www.jeremykun.com/2015/04/06/markov-chain-monte-carlo-without-all-the-bullshit/)

本文《去伪存真的马尔可夫链蒙特卡洛法》旨在以清晰、通俗易懂的方式解释MCMC方法。 它批评了统计学对MCMC的解释中经常使用的过于复杂的术语。

MCMC解决的核心问题是，当只有黑盒访问概率函数p(x)时，如何有效地从复杂的概率分布D中采样。 这意味着您可以输入一个元素“x”并获得其概率p(x)，但您不知道生成“x”的底层过程。 文章用估计婴儿名字概率的例子来说明这一点。 由于样本空间可能呈指数级增长，因此随机生成和基于概率的抛硬币这种幼稚的方法效率低下。

MCMC使用马尔可夫链（图上的随机游走）来解决这个问题。 关键是构建一个图，其中平稳分布（位于给定顶点的长期概率）与所需的概率分布D相匹配。 文章解释了平稳分布定理以及使其成立所需的诸如强连通性之类的条件。 顶点之间的转移概率由矩阵A表示，从而可以使用线性代数技术。

然后，文章描述了 Metropolis-Hastings 算法，这是一种构建具有所需平稳分布的马尔可夫链的方法。 它涉及将样本空间X的元素放置在格子上，并向相邻点添加边。 然后，基于对p(x)的黑盒访问，仔细定义这些点之间的转移概率。 目标是创建一个快速收敛到平稳分布的随机游走，从而能够有效地从D中采样。

---

## 63. 拆除伯班克Fry's电子商店

**原文标题**: Demolishing the Fry's Electronics in Burbank

**原文链接**: [https://www.latimes.com/00000196-230a-d4c4-abd7-fb5a95770000-123](https://www.latimes.com/00000196-230a-d4c4-abd7-fb5a95770000-123)

2025年4月，位于加州伯班克、以标志性宇宙飞船设计著称的Fry's Electronics商店被拆除。这家自1995年开业以来一直是地标的商店于2021年关闭。受社交媒体帖子的启发，丽贝卡·卡斯蒂略参观了现场并目睹了拆除过程。虽然宇宙飞船外观未能保留，但拆除人员设法保存了一件来自建筑内部的外星文物。该地块位于好莱坞路和凡诺文街的拐角处，计划重新开发成一个拥有约800个单元的大型公寓综合体。本文由洛杉矶时报的视频创作者和特殊项目负责人丽贝卡·卡斯蒂略撰写，她是南加州本地人，也是斯沃斯莫尔学院和南加州大学的校友。

---

## 64. Show HN: 我们在Unikernel上运行了Chromium (开源 Apache 2.0)

**原文标题**: Show HN: We Put Chromium on a Unikernel (OSS Apache 2.0)

**原文链接**: [https://github.com/onkernel/kernel-images](https://github.com/onkernel/kernel-images)

此“Show HN”帖子介绍了一个将 Chromium 浏览器置于 unikernel 之上的项目，为自动化工作流程、AI 代理开发和自定义工具提供了一个沙盒化且即用的浏览器环境。该项目提供 Docker 和 unikernel 两种实现。

主要功能包括一个与 Chrome DevTools 框架（如 Playwright 和 Puppeteer）兼容的预配置 Chrome 浏览器，通过 noVNC 进行 GUI 访问以实现可视化监控，以及与 Anthropic 的 Computer Use 代理循环集成。unikernel 实现提供独特的优势，例如用于资源节约的自动待机模式、用于会话重用的状态快照以及极快的冷启动。

该项目旨在支持基于浏览器的自动化任务、利用浏览器的 AI 代理开发以及创建需要受控浏览器环境的自定义应用程序。该帖子包括 unikernel 和 Docker 版本的快速入门指南、演示视频，并邀请大家贡献代码。帖子还提到团队正在招聘后端工程师，并提供联系方式以供咨询。最后，帖子引导用户前往 GitHub Issues 获取支持，并引导用户加入候补名单和 Discord 以了解有关托管服务的更多信息。

---

## 65. Herb: 强大且无缝的 HTML 感知 ERB 解析与工具

**原文标题**: Herb: Powerful and seamless HTML-aware ERB parsing and tooling

**原文链接**: [https://herb-tools.dev/](https://herb-tools.dev/)

Herb：一款强大且无缝的ERB模板解析与工具，尤其擅长HTML感知。这意味着Herb能智能地理解和解析ERB文件中交织的HTML结构与Ruby代码。HTML感知的关键优势在于更准确和精确的解析，确保工具能够正确地解释和处理ERB模板中的HTML标记和嵌入的Ruby代码。本质上，Herb通过理解HTML标签和属性的上下文，提供了一种比传统方法更复杂和准确的处理ERB文件的方式。

---

## 66. 斐波那契散列：被世界遗忘的优化

**原文标题**: Fibonacci Hashing: The Optimization That the World Forgot

**原文链接**: [https://probablydance.com/2018/06/16/fibonacci-hashing-the-optimization-that-the-world-forgot-or-a-better-alternative-to-integer-modulo/](https://probablydance.com/2018/06/16/fibonacci-hashing-the-optimization-that-the-world-forgot-or-a-better-alternative-to-integer-modulo/)

Malte Skarupke 的文章强调了斐波那契哈希这种令人惊讶地被忽视的哈希表优化技术。他认为，对于将哈希值映射到表槽，斐波那契哈希优于常用的整数取模运算，但它在像 `std::unordered_map` 这样的主要实现中却基本被忽略了。

文章解释说，整数取模速度慢且容易受到输入数据模式的影响。直接的取模实现速度较慢，而更快的“二进制与”方法（在表大小为 2 的幂时使用）会丢弃高位，如果哈希函数没有经过仔细设计，可能会导致冲突。

另一方面，斐波那契哈希速度更快（整数乘法后跟移位），并且更擅长混合输入模式，有效地提供了第二个哈希步骤。这使其对有问题的的数据模式更具鲁棒性。该技术利用黄金比例在整个表中均匀分布哈希值。

作者对各种 `unordered_map` 实现进行了基准测试，表明使用斐波那契哈希的 `ska::unordered_map` 可以比标准实现快得多（高达两倍）。文章认为，Knuth 的“计算机程序设计艺术”中整数取模的历史流行可能导致了它尽管存在缺点但仍被继续使用。他倡导广泛采用斐波那契哈希以提高哈希表性能。

---

## 67. 用-fsanitize=undefined和Picolibc的乐趣

**原文标题**: Fun with -fsanitize=undefined and Picolibc

**原文链接**: [https://keithp.com/blogs/sanitizer-fun/](https://keithp.com/blogs/sanitizer-fun/)

本文详细介绍了作者在使用GCC和Clang时，通过Picolibc库启用并使用`-fsanitize=undefined`标志来检测C代码中未定义行为和实现定义行为的经验。

作者描述了在Picolibc中实现消毒器处理程序以支持trap-on-error和handler模式的过程，从而能够调试已识别的问题。大部分工作涉及处理无害的未定义行为实例，例如超出数组边界的指针算术和有符号算术溢出，这通常会带来更清晰的代码。

文章强调了处理有符号整数移位的挑战，这是由于C标准的模糊性，特别是缺乏算术右移运算符。作者提供了自定义宏`lsl`和`asr`来分别处理左移和右移，确保在不同的编译器和架构中都能正确运行。

尽管最初的预期，消毒器还是发现了Picolibc中的八个实际错误，从区域设置函数中不正确的输入验证到`memcpy`中的内存损坏问题以及浮点转换中的错误。

最后，作者建议扩展消毒器以检测其他常见的编程错误，例如内存分配中无符号整数溢出，这些错误目前未被发现。作者建议使用未定义行为消毒器作为提高C代码质量和可靠性的宝贵工具。

---

## 68. Show HN: 不确定计算器 – 草稿纸上的概率计算器

**原文标题**: Show HN: Unsure Calculator – back-of-a-napkin probabilistic calculator

**原文链接**: [https://filiph.github.io/unsure/](https://filiph.github.io/unsure/)

Filip Hracek推出“不确定计算器”，这是一款概率计算器，旨在处理以范围表示（例如，4~6）的不确定数字的计算。该工具旨在通过提供一个用户友好的界面来输入代表95%置信区间的范围，从而简化更广泛受众的统计推理。

该计算器采用蒙特卡洛方法，基于提供的范围进行大量计算，与使用单个任意数字相比，提供了更真实和细致的结果。作者通过评估一份工作邀请的个人案例来说明其效用，展示了它如何提供一系列可能的Outcome和相关概率，从而帮助做出明智的决策。第二个例子使用德雷克方程来说明该工具在估计不确定变量（例如，银河系中潜在的通信文明的数量）方面的用途。

作者建议了其他各种用例，包括商业可行性评估、收入估算和投资回报计算。虽然承认这个早期版本的局限性（计算速度慢、简单的正态分布假设、基本的用户界面和脆弱的公式解析），但他希望它能成为快速、草稿式估算的宝贵工具。他提供了一个指向GitHub存储库的链接，以供贡献，以及一个指向更近期的笔记本版本应用程序的链接，供高级用户使用。

---

## 69. 谷歌利用人工智能暂停了超过3900万个涉嫌欺诈的广告账户。

**原文标题**: Google used AI to suspend over 39M ad accounts suspected of fraud

**原文链接**: [https://techcrunch.com/2025/04/16/google-used-ai-to-suspend-over-39m-ad-accounts-committing-fraud/](https://techcrunch.com/2025/04/16/google-used-ai-to-suspend-over-39m-ad-accounts-committing-fraud/)

2024年，谷歌大幅加强了打击广告欺诈的力度，暂停了3920万个广告商账户，比上一年增加了两倍。此次打击主要得益于使用大型语言模型（LLM）和人工智能来检测欺诈活动，例如商业冒充和非法支付详情，从而使谷歌能够在广告投放前暂停账户。

去年，谷歌实施了超过50项LLM增强功能，并推出了超过30项广告政策更新。 这还包括针对深度伪造广告诈骗的反制措施，在暂停了70万个违规账户后，报告的深度伪造广告下降了90%。

美国被暂停账户数量最多（3920万个账户），并删除了18亿个广告，其次是印度，暂停了290万个账户并删除了2.474亿个广告。 与诈骗相关的违规行为导致500万个账户被暂停，总体上删除了近5亿个诈骗广告。

虽然谷歌在2024年拦截了51亿个广告并删除了13亿个页面，但这些数字低于2023年，谷歌将其归因于早期检测和预防的改进。该公司还在一个重要的选举年验证了超过8900名新的选举广告商，并删除了1070万个选举广告。

为了解决对公平应用规则的担忧，谷歌提供人工审核的上诉流程，并正在努力提高其向广告商发布的有关暂停理由的信息透明度。

---

## 70. 一家创业公司的验尸报告

**原文标题**: A Postmortem of a Startup

**原文链接**: [https://buildwithtract.com/](https://buildwithtract.com/)

名为Tract的初创公司，旨在通过改善规划许可流程来解决英国的住房危机，但在获得74.4万英镑种子前融资后，经过近两年的努力，最终失败。该公司于2023年5月成立，探索了各种商业模式，包括场地搜寻工具（Tract Source）、免费土地评估工具（Attract）、成为技术赋能的土地推广商以及人工智能驱动的规划文件平台（Tract Editor）。

事后分析突显了向保守行业销售软件的难度、土地推广的运营复杂性以及对实用工具的低支付意愿。创始人还意识到英国房地产市场的分散性和保守性限制了风险投资支持的颠覆。

主要经验教训包括：更大的、更具接受度的市场（如美国）的重要性、关注市场质量、在证明收入之前保持精简、从一开始就积极进行商业活动以及优先考虑客户学习。具体错误包括高估英国市场、为不合适的模式筹集风险投资、优先考虑技术而非业务发展、过早地组建团队以及没有专注于创收。

最终，Tract于2025年3月停止运营，并将资金返还给投资者。创始人Jamie Rumbelow和Henry Dashwood分享他们的经验，作为一个案例研究，目的是整理经验教训、记录他们的旅程、解释花费的资源并实现结束。他们强调，失败最终在于他们自己的决定，同时也承认外部因素并对他们的支持者表示感谢。

---

## 71. 未来芯片将比以往更热

**原文标题**: Future Chips Will Be Hotter Than Ever

**原文链接**: [https://spectrum.ieee.org/hot-chips](https://spectrum.ieee.org/hot-chips)

本文探讨了未来芯片中日益严峻的散热挑战，其原因是晶体管密度不断增加以及此前用于控制功耗的登纳德缩放定律的终结。随着芯片变得更加紧凑和强大，传统的空气和液体冷却方法已不足以满足纳米片晶体管和互补场效应晶体管(CFET)等技术的需求，可能导致数据中心发生热失控。

本文探讨了微流体冷却和浸没式冷却等替代冷却技术，但也指出，仅依靠冷却是不切实际的，尤其是在移动设备中，以及由于数据中心的基础设施成本问题。 然后，本文深入研究了系统级解决方案，如热传感器和热敏加速，这些解决方案涉及动态调整电压、频率或核心使用量来管理热量，但这些可能会影响性能。

一种有前景的策略是利用晶圆背面，通过背面供电网络（BSPDN）、背面电容器和背面集成电压调节器（IVR）等技术来改善功率传输。这些技术可以降低电压需求和热量产生。然而，本文警告说，这些技术可能会引入新的热问题，例如由于硅基板变薄而导致的热点增加。

本文最后倡导采用一种整体的芯片设计方法，称为系统技术协同优化（STCO），该方法考虑了系统、物理设计和工艺技术之间的相互作用。 这涉及在早期设计阶段使用先进的热分析工具，并促进不同工程领域专家之间的合作。作者强调在芯片设计过程的早期解决散热问题的重要性，以避免后期采用影响性能的软件解决方案。

---

## 72. 杂项数学符号

**原文标题**: Miscellaneous Mathematical Symbols

**原文链接**: [https://www.johndcook.com/blog/2025/04/14/miscellaneous-mathematical-symbols/](https://www.johndcook.com/blog/2025/04/14/miscellaneous-mathematical-symbols/)

这篇博文探讨了“杂项数学符号”Unicode区段，着重介绍了其中主要是一些晦涩符号的集合。作者指出，虽然一些符号可能看起来很冷门，但它们可能在特定领域内有常规用途。

博文重点介绍了几个例子：

*   **垂直符号 (⟂):** 虽然技术上是“假”符号 (⊥) 的变体，但它用于表示垂直，有时用于数论中的互质。
*   **几何代数符号 (⟑, ⟇):** 这些符号表示几何代数中的几何积（点-楔积）和对偶算子（几何反积），尤其受到 Eric Lengyel 的推广。
*   **数据库连接符号:** 博文提到，Unicode 区段包含左连接、右连接和完全外部连接的符号，补充了另一个区段中的内连接弓形符号 (⨝)。
*   **角括号 (⟨, ⟩):** 这些 Unicode 字符对应于 LaTeX 命令 \langle 和 \rangle，作者回忆起在之前一篇关于格拉姆矩阵的博文中使用了它们。

总而言之，主题强调了 Unicode 的广度和深度，以及它对小众数学符号的收录，即使作者自己对它们的熟悉程度有所不同。该博文还包含指向其他与数学符号相关的博文的链接。

---

## 73. 一个记录同事口头失误的福特高管

**原文标题**: A Ford executive who kept score of colleagues' verbal flubs

**原文链接**: [https://www.wsj.com/lifestyle/ford-motor-mike-obrien-malaprops-6e560520](https://www.wsj.com/lifestyle/ford-motor-mike-obrien-malaprops-6e560520)

无法访问文章链接。

---

## 74. 科米特：一款儿童字体

**原文标题**: Kermit: A typeface for kids

**原文链接**: [https://microsoft.design/articles/introducing-kermit-a-typeface-for-kids/](https://microsoft.design/articles/introducing-kermit-a-typeface-for-kids/)

本文介绍了 Kermit，这是一款由 Underware 设计的全新字体，旨在帮助儿童（尤其是患有阅读障碍的儿童）提高阅读理解能力和乐趣。 鉴于阅读可能具有挑战性，尤其是对于估计占人口十分之一的阅读障碍患者，设计师的目标是创造一种友好、平易近人且具有科学依据的字体。

Kermit 具有较大的 x 高度、较粗的笔画、较大的间距和熟悉的字母形状，以最大限度地提高可读性。 除了基本的可读性之外，Kermit 还探索了以排版方式表示韵律（语调）的创新方法，使用粗体表示音量，宽度表示持续时间，垂直偏移表示音高。 这种方法旨在增强表达力和理解力，即使对于听力障碍者也是如此。

本文还深入探讨了研究表明阅读障碍可能涉及视觉空间处理问题。 为了解决这个问题，Underware 创建了 Kermit 的动画版本，其中字母会自行绘制。 他们使用可变字体技术和一种名为高阶插值 (HOI) 的新型数学方法，实现了平滑、自然的动画效果。 希望这种动画能够加强阅读障碍大脑中的高级通路信号，从而提高字母顺序理解和单词识别能力。

Kermit 不仅仅是一种字体；它是一个探索和实施基于科学的方法的平台，旨在让所有儿童都能更轻松、更愉快地阅读。 基本样式目前可用，全套样式即将推出。

---

## 75. 四种优化 (2023)

**原文标题**: Four Kinds of Optimisation (2023)

**原文链接**: [https://tratt.net/laurie/blog/2023/four_kinds_of_optimisation.html](https://tratt.net/laurie/blog/2023/four_kinds_of_optimisation.html)

劳伦斯·特拉特的《四种优化》挑战了软件性能改进方面的常见假设。他认为，识别性能瓶颈和知道如何修复它们通常比我们想象的要复杂得多，并提倡严格的性能剖析和对可用解决方案的细致理解。

特拉特概述了四种主要的优化方法：

1.  **使用更好的算法：** 需要理解上下文、输入以及最佳、平均和最坏情况性能之间的权衡。他告诫不要假设理论性能会转化为实际速度，并强调了实现复杂算法时引入错误的风险。
2.  **使用更好的数据结构：** 需要仔细思考和测量。他建议使用现有的数据结构库，并优化结构体/类的大小、减少指针追踪以及改善内存局部性。
3.  **使用更底层的系统：** 提倡在用Rust等语言重写代码之前，探索替代的语言实现（例如，Python的PyPy）和编译器优化。这通常能以更少的努力和风险提供显著的性能提升。
4.  **接受不太精确的解决方案：** 涉及针对具有巨大解空间复杂问题的局部搜索等技术。它也可能意味着为了提高速度而故意接受近似或概率性答案（例如，快速平方根倒数或布隆过滤器）。

这篇文章强调，选择正确的优化策略涉及权衡以及对软件行为、数据和上下文的深入理解。

---

## 76. Rust 的前景

**原文标题**: The Promise of Rust

**原文链接**: [https://fasterthanli.me/articles/the-promise-of-rust](https://fasterthanli.me/articles/the-promise-of-rust)

文章《Rust的承诺》探讨了Rust独特的内存管理方法及其与JavaScript和Go等其他流行语言相比的意义。作者fasterthanlime强调了Rust的所有权和借用系统如何强制执行内存安全，从而在编译时防止悬挂指针和数据竞争等问题。

文章展示了Rust的移动语义，即当变量传递给函数时，数据的所有权会被转移。与自动按值传递原始类型的JavaScript不同，Rust需要显式克隆或借用才能允许多次使用数据而无需转移所有权。这迫使开发者意识到内存影响并防止意外的堆分配。作者批评了JavaScript缺乏清晰的“按值”或“按引用”语义，以及像`JSON.parse(JSON.stringify(o))`用于深度克隆和`Object.freeze()`用于防止突变等方法的局限性。

作者认为，虽然Rust的严格性最初可能具有挑战性，但最终会产生更健壮和可预测的代码。编译器提供的信息丰富的错误消息充当了一种教学工具，引导开发者进行高效且安全的内存管理。文章表明，理解这些概念对于开发者至关重要，即使是来自垃圾回收语言的开发者，尤其是在处理原生扩展或对性能敏感的代码时。文章的剩余部分仅对赞助商和订阅者开放。

---

## 77. 英国士兵用无线电波武器击落无人机群

**原文标题**: British soldiers take down drone swarm with radio wave weapon

**原文链接**: [https://www.gov.uk/government/news/british-soldiers-take-down-drone-swarm-in-groundbreaking-use-of-radio-wave-weapon](https://www.gov.uk/government/news/british-soldiers-take-down-drone-swarm-in-groundbreaking-use-of-radio-wave-weapon)

英军成功使用新型射频定向能武器摧毁无人机群

---

## 78. RakuAST资助报告

**原文标题**: RakuAST Grant Report

**原文链接**: [https://niner.name/blog/rakuast_grant_report/index.html](https://niner.name/blog/rakuast_grant_report/index.html)

本报告详细介绍了RakuAST项目的进展和挑战，该项目是对Raku编译器前端的重写。目标是用一种新的、基于AST的前端来取代旧的前端，使其能够处理Raku语言的复杂性。

虽然最初的基础设施已经就位，但实现Raku的高级特性，如各种方法调用类型和编译时代码执行，被证明是困难的。最大的挑战是确定声明、定义、类型设置和代码生成的正确顺序，因为这个顺序没有文档记录，并且对于成功编译至关重要。

该项目面临着大量特殊情况、编译时检查和错误处理的“长尾”，导致了超过900次的提交，远远超过了最初估计的200次。由于循环依赖关系和直接访问内部对象属性的需求，引导编译器（即用自身编译它）提出了进一步的挑战。标准库及其高级Raku代码揭示了规范测试未涵盖的缺陷。还发现许多规范测试是不完整的、不正确的或依赖于旧前端的特定错误行为，需要进行调整。

尽管该项目非常复杂且代码库令人望而生畏，但Elizabeth Mattijsen、John Haltiwanger、Vadim Belman、Jimmy Zhuo和Daniel Green的贡献对于项目的进展至关重要。

---

## 79. Chroma：育碧用于模拟色盲的内部工具

**原文标题**: Chroma: Ubisoft's internal tool used to simulate color-blindness

**原文链接**: [https://github.com/ubisoft/Chroma](https://github.com/ubisoft/Chroma)

育碧Chroma：一款内部工具，用于模拟不同类型的色盲（红色盲、绿色盲和蓝色盲），以测试和提高其游戏的可访问性。Chroma使开发人员能够了解他们的游戏对色觉障碍玩家的呈现效果。

Chroma的主要功能包括：在单个显示器上进行实时色彩模拟、与所有游戏（不限引擎）的兼容性、高性能（高达60 FPS）、准确的结果、所有主要色盲形式的模拟、实时游戏画面捕获和模拟、便捷的屏幕截图记录以及用户友好的界面。由于其捕获和模拟实时游戏画面的能力，Chroma被认为是一种独特的解决方案。

本文还提到CMake过程中一个与过时的CPPWinRT库相关的已知问题。建议的解决方案是安装Microsoft.Windows.CppWinRT NuGet包或更新CPPWinRT库，并建议使用Visual Studio 2022以完全避免此问题。本文还指出了您可以找到更多详细信息和下载官方Chroma徽标的位置。

---

## 80. 欺骗世界的假照片

**原文标题**: Fake images that fooled the world

**原文链接**: [https://www.theguardian.com/artanddesign/2025/apr/12/28-fake-images-that-fooled-the-world](https://www.theguardian.com/artanddesign/2025/apr/12/28-fake-images-that-fooled-the-world)

乔纳森·弗里德兰的文章探讨了照片造假的悠久历史及其影响，指出这种现象并非人工智能深度伪造的现代发明，而是自摄影术诞生之初就已存在。文章列举了各种例子，从政治宣传（例如将林肯的头像叠加在另一人的身体上，或裁剪掉墨索里尼的马夫以创造更强大的形象），到为了让拍摄对象显得更具威胁性而篡改图像的案例，例如《时代》杂志的辛普森封面。

文章还涉及了造假动机不太明确的案例，例如罗伯特·卡帕的“倒下的士兵”摆拍照片，以及恶作剧者在世贸中心屋顶上的照片。文章强调，虚假图像之所以泛滥，是因为它们通常向观众展示他们想相信的东西，满足幻想或证实既有偏见。

文章讨论的具体例子包括伊夫·克莱因的“纵身入虚空”，威尔士王妃编辑过的家庭照片，帕特森-吉姆林大脚怪电影，乔纳斯·本迪克森的“维莱斯之书”以及比利·迈耶的UFO图像。作者认为，这些图像表明，如果呈现方式符合人们的期望和愿望，人们就很容易被欺骗。最终，文章强调，照片的说服力是建立在我们对照片真实性的固有信任之上的，而这种信任在历史上一直被利用。

---

## 81. 微软研究人员开发出一种可在 CPU 上运行的超高效 AI 模型。

**原文标题**: Microsoft researchers developed a hyper-efficient AI model that can run on CPUs

**原文链接**: [https://techcrunch.com/2025/04/16/microsoft-researchers-say-theyve-developed-a-hyper-efficient-ai-model-that-can-run-on-cpus/](https://techcrunch.com/2025/04/16/microsoft-researchers-say-theyve-developed-a-hyper-efficient-ai-model-that-can-run-on-cpus/)

微软研究人员开发出BitNet b1.58 2B4T，一种可在CPU（包括Apple M2）上运行的超高效AI模型。这种“位网络”是同类中最大的，使用量化权重，仅限于-1、0和1，从而使其在内存和计算方面都非常高效。它在海量数据集上训练，拥有20亿个参数，并在GSM8K和PIQA等基准测试中优于类似规模的传统模型，超越了Meta的Llama 3.2 1B、Google的Gemma 3 1B和阿里巴巴的Qwen 2.5 1.5B。

BitNet b1.58 2B4T也明显快于同类模型，有时速度快两倍，同时使用更少的内存。然而，这种性能取决于微软的自定义框架bitnet.cpp，该框架目前缺乏GPU支持，鉴于GPU在AI基础设施中的主导地位，这是一个主要缺点。虽然位网络为资源受限的设备提供了潜力，但兼容性仍然是一个重大挑战。该模型在MIT许可下公开提供。

---

## 82. 重现Hacker News写作风格指纹识别

**原文标题**: Reproducing Hacker News writing style fingerprinting

**原文链接**: [https://antirez.com/news/150](https://antirez.com/news/150)

本文可能详述了一项尝试，旨在重现或验证基于写作风格识别 Hacker News 用户身份的技术，通常称为“写作风格指纹识别”。

其核心概念包括分析用户评论中的各种语言特征，以创建独特的个人资料或“指纹”。这些特征可能包括：

*   **词汇选择：** 常用的词语、短语以及特定术语。
*   **句法模式：** 句子结构、语法偏好以及常见的语法错误。
*   **标点符号和格式：** 逗号、括号、强调以及代码格式的使用。
*   **内容主题和论点：** 反复讨论的主题、偏爱的观点以及论证风格。

该重现工作可能涉及：

*   **数据收集：** 收集来自各种 Hacker News 用户的评论数据集。
*   **特征提取：** 开发或利用方法从收集的数据中提取相关的语言特征。
*   **模型训练：** 构建一个模型（通常是机器学习分类器），该模型可以学习根据这些特征将写作风格与特定作者联系起来。
*   **评估：** 测试该模型根据写作风格准确识别新的、未见过的评论作者身份的能力。

重现这些技术的目的是了解写作风格指纹识别在 Hacker News 等平台上的有效性和局限性。它可能探讨影响准确性的因素，例如数据集的大小、使用的特征数量以及模型的复杂程度。文章可能还会讨论与隐私和匿名相关的伦理影响。

---

## 83. 马里兰州最后一家无线电小屋即将关闭。

**原文标题**: The last RadioShack in Maryland is closing

**原文链接**: [https://marylandmatters.org/2025/04/14/end-of-an-era-the-last-radioshack-in-maryland-is-closing-its-doors/](https://marylandmatters.org/2025/04/14/end-of-an-era-the-last-radioshack-in-maryland-is-closing-its-doors/)

无法访问文章链接。

---

## 84. 入侵Postgres线协议

**原文标题**: Hacking the Postgres wire protocol

**原文链接**: [https://pgdog.dev/blog/hacking-postgres-wire-protocol](https://pgdog.dev/blog/hacking-postgres-wire-protocol)

本文介绍 PgDog，一个网络代理，旨在对 Postgres 数据库进行分片，而无需更改应用程序代码。PgDog 拦截并操作 Postgres 线协议，将查询路由到适当的分片。它支持简单查询协议和扩展查询协议。对于简单协议，PgDog 解析 SQL 查询，以识别读/写意图并使用 `pg_query`（一个利用 Postgres 自身 SQL 解析代码的 Rust 库）提取分片键。对于扩展协议（预处理语句），PgDog 缓存解析后的查询，并使用 `Bind` 消息来确定分片键值。

一个关键方面是分片函数，PgDog 直接采用 Postgres 声明式分区（基于哈希）中的分片函数，以确保不同数据访问方法之间的一致性。它从 SQL 查询中提取参数以确定分片位置，处理各种 `WHERE` 子句的复杂性，甚至 INSERT 语句。

对于跨分片查询，PgDog 管理 Postgres 的消息序列（`RowDescription`、`DataRow`、`CommandComplete`、`ReadyForQuery`），通过合并 `RowDescription`、在 `CommandComplete` 中求和行数，以及处理 `DataRow` 消息（通过缓冲以获得有序结果或立即流式传输以获得无序结果）。它还操作客户端消息以进行分布式 `COPY` 命令，确保每个分片接收完整的行以进行高效摄取。PgDog 旨在实现数据摄取中的线性可扩展性，并使用 Tokio 构建以实现并发和并行处理。下一步涉及将类似的技术应用于逻辑复制流。

---

## 85. 台积电称将在美国建立“独立”芯片中心。

**原文标题**: TSMC says it will build 'independent' chip hub in U.S.

**原文链接**: [https://asia.nikkei.com/Business/Tech/Semiconductors/TSMC-says-it-will-build-independent-chip-hub-in-U.S.](https://asia.nikkei.com/Business/Tech/Semiconductors/TSMC-says-it-will-build-independent-chip-hub-in-U.S.)

台积电计划在亚利桑那州生产全球30%的最先进的2纳米芯片，助力美国建立“独立”芯片中心的目标。据台积电董事长兼首席执行官魏哲家表示，该公司目前未参与任何关于合资企业、技术许可或技术转让的讨论，特别是针对与英特尔合作的传言。发表此声明之际，正值美国关税上涨和人工智能芯片出口管制收紧等挑战，台积电正在积极应对这些挑战。文章强调了台积电在支持美国芯片产业的同时，保持其技术独立性和保护其知识产权的承诺。

---

## 86. K玛特顾客请注意

**原文标题**: Attention K-Mart Shoppers

**原文链接**: [https://archive.org/details/attentionkmartshoppers](https://archive.org/details/attentionkmartshoppers)

注意 K-Mart 顾客：您将被重定向到 archive.org 的简化版。

---

## 87. 为什么两位德州参议员想从史密森尼学会夺取一架航天飞机？

**原文标题**: Why are two TX senators trying to wrest a Space Shuttle from the Smithsonian?

**原文链接**: [https://arstechnica.com/space/2025/04/why-are-two-texas-senators-trying-to-wrest-a-space-shuttle-from-the-smithsonian/](https://arstechnica.com/space/2025/04/why-are-two-texas-senators-trying-to-wrest-a-space-shuttle-from-the-smithsonian/)

两位德克萨斯州参议员约翰·科宁和特德·克鲁兹提出了“将航天飞机带回家法案”，旨在将“发现号”航天飞机从史密森尼国家航空航天博物馆移至休斯顿。文章认为，这是一项出于政治动机、不切实际且代价高昂的举措。

休斯顿虽然与航天飞机计划有着密切的联系，但在15年前分配航天飞机时，由于提案薄弱以及对保存航天飞机的担忧，并未获得一架。现在移动“发现号”将耗资巨大（估计为10亿美元），可能损坏航天飞机，并且需要大量工作来翻新航天飞机运输机。

文章认为，该法案主要用于政治宣传，特别是为了支持科宁对抗一位强大的党内挑战者的连任竞选。科宁旨在将自己塑造成一位对抗华盛顿特区，为德克萨斯州利益而战的斗士。

在提交该法案之前，休斯顿太空中心和美国国家航空航天局均未被咨询。由于重新启动航天飞机运输机的复杂性和成本，美国国家航空航天局尤其不愿意参与。文章强调，史密森尼博物馆收藏着最具历史意义的“发现号”航天飞机是有充分理由的，并强调了它作为国家珍宝的重要性。作者的结论是，拟议的搬迁是一个“极其愚蠢的主意”，会浪费纳税人的钱，并有损坏太空历史重要组成部分的风险。

---

## 88. 受够了Oh-my-ZSH的臃肿，我自己构建了极简的、只包含所需功能的点文件。

**原文标题**: Tired of Oh-my-ZSH bloat, built my own minimal dotfiles with just what I need

**原文链接**: [https://github.com/cassiozen/dotfiles](https://github.com/cassiozen/dotfiles)

Cassio Zen 的 dotfiles 提供了一个轻量级、无依赖的 macOS ZSH 配置，旨在避免通常与 Oh-my-ZSH 等框架相关的臃肿。该设置优先考虑基本功能和自定义。

主要功能包括：一个显示 Git 分支和状态的极简 ZSH 提示符，增强的带菜单选择的 Tab 补全，箭头键历史记录搜索，以及方便的目录导航别名。Git 功能通过常用命令的别名、改进的日志工具（如 `git lol` 和 `git graph`）以及简化的分支管理（通过 `git publish`、`git unpublish` 和 `git cleanup`）得到增强。生活质量方面的改进包括：rebase 期间的自动储藏，设置为 `main` 的默认分支，以及全局的 `.gitignore` 配置。

安装过程包括克隆存储库（最好到 `~/.dotfiles`）并运行 `bootstrap.sh` 脚本。强烈建议用户在使用前 fork 存储库并查看配置文件，因为这些设置是针对 Cassio Zen 的个人偏好而设计的。更新通过导航到 `.dotfiles` 目录并重新运行 `bootstrap.sh` 来执行。本地自定义可以添加到 `~/.gitconfig.local` 和 `~/.zshrc.local` 文件中，允许用户进一步定制设置，而无需修改核心 dotfiles。

---

## 89. 饲养员：实验室动物管理员偶然发现一个秘密[小说]

**原文标题**: "Vivarium": The keeper of a lab's animals stumbles onto a secret [fiction]

**原文链接**: [https://jsomers.net/vivarium/](https://jsomers.net/vivarium/)

在詹姆斯·萨默斯的小说《动物饲养所》中，一所大学的实验动物管理员在他的工作场所的无菌墙壁内偶然发现了一个令人不安的秘密。 这位管理员将毕生精力都奉献给了实验用的小鼠，他工作时间不规律，与大学白天的喧嚣隔绝，并且与正常生活越来越疏远。 尽管这些动物忍受着往往是残酷的实验，但他还是从日常的照顾中找到了慰藉。

故事围绕着“贝克尔实验”展开，在这个实验中，尽管小鼠遭受严重的痛苦，但仍被故意保持存活，从而突破了伦理治疗的界限。 管理员越来越不安，因为博士后坚持要延长受苦小鼠的生命，即使安乐死显然是必要的。

一天晚上，面对对贝克尔实验中最后两只小鼠实施安乐死的任务，管理员萌生了一个计划。 他发现雌鼠（安娜·K）充满活力，这使得她不可避免的死亡前景更加令人不安。 他给安娜·K注射了镇静剂，并打算欺骗博士后，让他相信她已经病得太重，无法继续实验，从而免除她进一步的痛苦。 他的欺骗奏效了，博士后被误导，认为这两只小鼠都已经无法挽救。 管理员的伦理困境突显了科学进步与动物福利之间的冲突，并且这个故事突出了科学抽象的非人化影响，在这种影响下，动物被简化为单纯的实验对象，而科学家们却对它们所遭受的个体痛苦视而不见。

---

## 90. JSLinux

**原文标题**: JSLinux

**原文链接**: [https://www.bellard.org/jslinux/](https://www.bellard.org/jslinux/)

JSLinux是一个基于网络的模拟器，允许用户直接在网页浏览器中运行各种操作系统。它提供多个模拟系统，包括不同版本的Linux（Alpine、Buildroot、Fedora）、Windows 2000和FreeDOS。这些系统无需任何本地安装即可访问和操作。

该平台为Linux发行版提供控制台和图形（X Window）界面，使用户能够与模拟的操作系统环境交互。每个系统都有一个相应的链接，可以直接在浏览器中启动它。某些系统具有特定的说明，例如使用鼠标右键访问菜单。

用户还应注意与某些操作系统相关的免责声明和警告，例如可能较长的启动时间。该平台由Fabrice Bellard开发，并包含新闻、虚拟机列表、常见问题解答和技术说明的链接，以获取更多信息。

---

## 91. Kotlin 101：类型类快速讲解

**原文标题**: Kotlin 101: Type Classes Quickly Explained

**原文链接**: [https://rockthejvm.com/articles/kotlin-101-type-classes](https://rockthejvm.com/articles/kotlin-101-type-classes)

本文以数据验证为例，对 Kotlin 中的类型类进行了实用介绍。它解决了使用可重用和通用代码验证不同数据类型（DTO）的挑战，利用了 Arrow Kt 库和 Kotlin 的上下文接收者。

文章首先强调了传统面向对象方法的局限性，例如直接子类型化，这可能违反单一职责原则并使代码的可维护性降低，尤其是在处理外部或自动生成的类型时。

然后，它介绍了类型类作为一种函数式编程解决方案。它定义了一个 `ValidatorScope<T>` 接口，其中 `T.validate()` 作为一个扩展函数，允许验证逻辑与 DTO 解耦。这实现了特设多态性，并避免了修改 DTO 类本身。

文章还讨论了分发器接收器，通过 `ValidatorScope` 限制 validate 扩展函数的可见性，使扩展函数具有上下文相关性。此外，还解释了 `with` 函数和上下文接收器的使用，以进一步改进代码并提供更简洁的语法。文章还提到了围绕类型类自动发现的限制，这是 Scala 和 Haskell 等语言中存在的功能。

最后，它简要地提到了如何递归地使用类型类，扩展验证框架以纳入 DTO 字段的特定验证规则，为后续章节（在给定的文本中不存在）中的进一步解释奠定了基础。

---

## 92. 任天堂如何扼杀了雅达利游戏

**原文标题**: How Nintendo bled Atari games to death

**原文链接**: [https://thereader.mitpress.mit.edu/how-nintendo-bled-atari-games-to-death/](https://thereader.mitpress.mit.edu/how-nintendo-bled-atari-games-to-death/)

任天堂与雅达利（腾根）关于未经授权的NES游戏卡带的法律战

---

## 93. 一个蛋白质折叠谜团解开：研究解释核心堆积率

**原文标题**: A protein folding mystery solved: Study explains core packing fractions

**原文链接**: [https://phys.org/news/2025-03-protein-mystery-core-fractions.html](https://phys.org/news/2025-03-protein-mystery-core-fractions.html)

本文探讨了发表在PRX Life上的一项耶鲁大学研究，该研究阐明了蛋白质折叠过程。在Corey O'Hern的带领下，研究人员分析了蛋白质数据库中球状蛋白质的核心堆积密度，发现它们始终以55%的密度堆积，这意味着核心空间中有55%被原子占据。

该研究解答了为什么这种堆积密度是一致的以及为什么是55%的问题。研究人员得出结论，蛋白质核心会发生堵塞或刚性化，从而阻止进一步压缩。与球形物体在64%时发生堵塞不同，氨基酸复杂、细长和凹凸不平的形状导致它们在较低的堆积密度下发生堵塞。

研究结果表明，操纵诸如溶剂、压力或温度等折叠条件，有可能导致更密集的堆积和不同的蛋白质结构，即使使用相同的氨基酸序列。这可能为蛋白质设计开辟新的途径，超越仅仅操纵氨基酸序列，用于药物治疗和生物材料等应用。

此外，模拟深海热液喷口条件的高压研究表明，蛋白质核心堆积密度可增加到58-60%，这与生命的起源有关。在博士候选人Alex Grigas的带领下，该研究强调了通过改变折叠条件来设计具有新结构和功能的蛋白质的潜力。

---

## 94. Unix文件至少有两个大小。

**原文标题**: Unix files have (at least) two sizes

**原文链接**: [https://utcc.utoronto.ca/~cks/space/blog/unix/UnixFilesTwoSizes](https://utcc.utoronto.ca/~cks/space/blog/unix/UnixFilesTwoSizes)

由于爬虫活动激增，尤其是伪装成旧版 Chrome 的机器人，Chris Siebenmann 的博客 ("Wandering Thoughts") 正在屏蔽较旧的浏览器。这是一种预防措施，旨在减少为 LLM 训练和其他目的收集数据的爬虫造成的服务器负载。

如果用户看到此消息，很可能是因为他们的浏览器因版本过旧而被标记为可疑。如果用户认为这是一个错误，建议他们联系 Siebenmann 并提供其浏览器详细信息和 User-Agent 字符串。

一个具体的问题是关于 archive.today、archive.ph 和 archive.is 等归档服务。这些服务通常与恶意爬虫无法区分，因为它们使用旧的 Chrome User-Agent 值，从广泛分布的 IP 地址进行爬取，甚至有时会使用伪造的反向 DNS 条目来模仿 Googlebot。Siebenmann 建议使用 archive.org，因为它是一个行为更好的归档爬虫。他于 2025 年初实施了这项屏蔽措施，以打击高流量、可疑的爬虫活动。

---

## 95. 使用UTM在Apple Silicon上进行开发

**原文标题**: Development on Apple Silicon with UTM

**原文链接**: [https://rkiselenko.dev/blog/development-on-mac-with-utm/development-on-mac-with-lima/](https://rkiselenko.dev/blog/development-on-mac-with-utm/development-on-mac-with-lima/)

本文详细介绍了如何使用UTM虚拟机和cloud-init脚本在Apple Silicon Mac上创建Linux开发环境。该过程包括安装UTM和cdrtools，下载适用于Fedora或Ubuntu的云镜像（涵盖aarch64和x86_64架构），以及编写cloud-init脚本（user-data）以自动安装必要的开发工具（git、jq、go、docker等），配置用户设置并设置SSH访问。

cloud-init脚本使用mkisofs打包成init.iso。然后创建一个新的UTM虚拟机，配置为模拟（x86_64）或虚拟化（aarch64），对于Fedora禁用UEFI启动，并将Fedora或Ubuntu云镜像添加为VirtIO驱动器。init.iso也作为VirtIO驱动器添加，用于初始设置。

启动虚拟机后，cloud-init脚本执行，配置系统。默认用户名/密码（fedora/password）允许初始登录。初始化完成后，虚拟机断电，并移除init.iso驱动器。可以使用`sudo cat /var/log/cloud-init-output.log`查看日志。对于Apple Silicon虚拟机（aarch64），选择虚拟化并使用arm64镜像。Ubuntu过程类似，但不需要禁用UEFI启动，且`.img.xz`镜像必须解压。

---

## 96. 清洁能源项目并网优先

**原文标题**: Clean energy projects prioritised for grid connections

**原文链接**: [https://www.gov.uk/government/news/clean-energy-projects-prioritised-for-grid-connections](https://www.gov.uk/government/news/clean-energy-projects-prioritised-for-grid-connections)

英国政府正优先考虑清洁能源项目的电网连接，以加速向清洁能源的转型，刺激经济增长并增强能源安全。英国天然气电力市场管理局(Ofgem)预计将批准国家能源系统运营商(NESO)起草的电网连接改革计划，从而每年释放估计400亿英镑的主要来自私人投资。

这些改革旨在消除因阻碍队列的“僵尸”项目造成的延误，优先考虑推动增长的企业，尤其是在数据中心、人工智能、风能和太阳能等领域。此举旨在加速可再生能源项目的连接，减少对动荡的全球化石燃料市场的依赖并降低能源费用。自2024年7月以来，英国清洁能源产业已宣布了437亿英镑的私人投资，突显了日益增长的势头。

能源大臣埃德·米利班德强调了英国致力于成为清洁能源投资安全港的承诺。该计划支持一项以英国工业为中心的“强有力的产业政策”。英国天然气电力市场管理局首席执行官乔纳森·布雷尔利指出，这些改革将简化流程，将“僵尸项目”送入历史，并为清洁能源雄心壮志提供强大动力。国家能源系统运营商首席运营官凯特·奥尼尔强调了能源行业在制定该计划中的密切合作。预计这些改革将通过避免不必要的电网加固为账单支付者节省50亿英镑。

---

## 97. Show HN: 我用 Python 从零开始构建了一个深度学习引擎

**原文标题**: Show HN: I built a deep learning engine from scratch in Python

**原文链接**: [https://github.com/whitegra/dolphin](https://github.com/whitegra/dolphin)

Dolphin：一个纯Python实现的深度学习引擎，从零开始构建，摒弃了NumPy和PyTorch等库，以实现完全的透明性和控制。它旨在提供一个清晰且富有表现力的平台，用于理解Transformer和自动微分的内部运作原理。

主要特性包括：

*   **符号自动微分引擎：** 一个自定义的Tensor类，支持1D、2D和3D张量，跟踪计算图和梯度，并实现反向传播。
*   **纯Python Transformer栈：** 实现多头自注意力、层归一化、GELU激活函数、前馈层和残差连接。
*   **零依赖机器学习系统：** 仅使用原生Python运行，无需任何外部库。
*   **模块化结构：** 组织成张量、Transformer、激活函数、层和优化器（SGD、Adam、动量）等模块。

完整的示例（`DolphinTest01.py`）展示了该框架的功能，包括文本预处理、基于Transformer的序列建模、端到端训练和文本生成，所有这些都不依赖于外部库。

Dolphin旨在用于教育、研究和探索深度学习的基础知识，无需依赖黑盒抽象。它需要Python 3.7+版本，并采用MIT许可证。

---

## 98. CT扫描可能导致5%的癌症，研究发现；专家指出不确定性。

**原文标题**: CT scans could cause 5% of cancers, study finds; experts note uncertainty

**原文链接**: [https://arstechnica.com/health/2025/04/ct-scans-could-cause-5-of-cancers-study-finds-experts-note-uncertainty/](https://arstechnica.com/health/2025/04/ct-scans-could-cause-5-of-cancers-study-finds-experts-note-uncertainty/)

基于JAMA内科学发表的一项新研究，该文章探讨了基于2023年进行的9300万次扫描的数据，CT扫描可能与美国每年诊断的约5%的癌症相关。 研究人员估计，这相当于未来将有103,000例癌症，使CT扫描与酒精消费和肥胖等风险因素相当。 肺癌和结肠癌是估计由CT扫描引起的最常见的癌症类型，其中腹部和盆腔扫描是最常见的相关扫描。

虽然该研究建议谨慎使用CT扫描并优化剂量，但专家强调建模中的不确定性，并警告不要避免必要的扫描。 他们认为，诊断和治疗的益处通常大于小的风险增加，估计每次扫描仅增加0.1%的终生癌症风险。 文章还提到自2007年以来CT扫描的使用量增加了35%，引发了对潜在过度使用的担忧。 鼓励医生考虑替代成像选择，如超声波和MRI，并让患者参与决策过程。

---

## 99. 他为何要冒如此风险？我的审查者和我

**原文标题**: 'Why would he take such a risk?' My censor and me

**原文链接**: [https://www.theguardian.com/news/2025/apr/17/why-would-he-take-such-risk-my-censor-and-me-weibo-china](https://www.theguardian.com/news/2025/apr/17/why-would-he-take-such-risk-my-censor-and-me-weibo-china)

慕容雪村的文章通过刘力朋的故事探讨了中国审查制度的悖论。刘力朋是一名微博审查员，但他违背职责帮助了作者。 2013年，刘力朋对删除批评共产党的内容的工作感到幻灭，开始“全部通过”大量帖子，让数百万人看到。

刘力朋还使用个人微博账号“普通法西斯”匿名批评政府。他还通过秘密恢复被禁用户的账户来帮助他们，例如珍妮·何。此外，他收集了内部“交班文件”，详细记录了审查命令，认为这些文件是重要的历史记录。

作者慕容雪村是一位受欢迎的微博用户，因发表批评性评论而被取消账户。雪村有一位“微博守门员”贾葭，他会温和地审查他的帖子并警告他敏感话题。账户被封禁后，刘力朋在最后一天工作时，访问了雪村的账户详细信息，并将审查命令的截图匿名发送给了慕容雪村的联系人之一余大有。 雪村收到了截图，并知道了自己被审查的原因。刘力朋的行为突显了中国审查制度的复杂性和矛盾性，提出了一个问题：为什么有人会冒如此大的风险去帮助一个他们不认识的人。虽然刘力朋淡化了风险，声称最坏的结果是被解雇，但文章强调了他的行为可能带来的潜在危险。

---

## 100. 特拉克博物馆

**原文标题**: Terak Museum

**原文链接**: [https://www.threedee.com/jcm/terak/index.html](https://www.threedee.com/jcm/terak/index.html)

泰拉克博物馆： 位于杰斐逊电脑博物馆内，致力于展示20世纪70年代末至80年代初的早期个人电脑泰拉克。本网站提供有关泰拉克的历史、规格以及对计算领域的影响的信息。

泰拉克基于PDP-11处理器，以其图形功能、在Pascal教学中的应用以及对UCSD P-System的采用而闻名。 它具有位图显示和用户定义的字符字体，使其适用于从CAD到语言学习的各种应用。 博物馆详细介绍了其功能，包括内存映射图形、可编程声音以及可用的操作系统，如UCSD P-System和RT-11。 1981年的定价信息用于说明当时该系统的成本。

强调了泰拉克在计算机历史上的重要性，特别是它在早期图形用户界面、使用T-Square软件的计算机辅助设计以及对Macintosh的MacPaint的间接影响方面的作用。 博物馆还提到它在开发康奈尔程序合成器（一个早期的IDE）中的应用以及它作为智能终端存在于“termcap”文件中。

该网站还收录了作者收藏的泰拉克硬件、软件和文档，包括工厂照片和转换后的位图图像。 作者还表达了创建泰拉克模拟器的愿望。 该网站鼓励访问者分享有关泰拉克硬件和软件的信息，并表示愿意为遗弃的物品提供家园。 还提供了有关UCSD P-System和磁盘归档工具的信息。

---

