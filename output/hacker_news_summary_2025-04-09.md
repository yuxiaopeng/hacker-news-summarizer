# Hacker News 热门文章摘要 (2025-04-09)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Agent2Agent协议 (A2A)

**原文标题**: The Agent2Agent Protocol (A2A)

**原文链接**: [https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)

Agent2Agent协议 (A2A)：促进AI Agent跨平台互操作

---

## 2. chroot技术：Linux系统的瑞士军刀

**原文标题**: The chroot Technique – a Swiss army multitool for Linux systems

**原文链接**: [https://livesys.se/posts/the-chroot-technique/](https://livesys.se/posts/the-chroot-technique/)

本文介绍了“chroot”技术，这是一种用于修复无法启动的Linux系统的宝贵工具。它涉及访问损坏系统的硬盘驱动器（例如，通过Live USB或作为外部驱动器），挂载其根分区，并通过将其与工作环境中的特殊系统文件夹（/sys, /proc, /dev, /dev/pts）相结合，来创建一个新的根文件系统。

其核心思想是欺骗当前的Linux会话，使其认为它正在损坏系统的硬盘驱动器上运行，从而实现诊断和修复。作者提供了一个循序渐进的指南，包括识别根目录和/boot的正确分区，创建必要的挂载点（/rescue，/rescue/boot），挂载分区，并使用`mount`命令挂载特殊系统文件夹。

文章随后提供了`chroot /rescue /bin/bash -i`命令，以有效地切换根文件系统。这允许用户运行诸如`apt update`、`apt upgrade`和`dpkg-reconfigure`之类的命令，以诊断和修复损坏系统中的问题，例如损坏的符号链接或不完整的软件包更新。作者通过修复Nanopore GridION设备的真实示例来说明这一点。作者强调了拥有这些命令备忘单以便快速访问的重要性。文章最后提供了一个进一步阅读的链接。

---

## 3. 铁木：面向推理时代的谷歌首款TPU

**原文标题**: Ironwood: The first Google TPU for the age of inference

**原文链接**: [https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/)

Ironwood：谷歌第七代张量处理器，专为推理设计的定制AI加速器，标志着向主动生成洞察的“思考模型”转变。它是谷歌迄今为止最强大且节能的TPU，旨在大规模支持高要求的AI工作负载。

Ironwood的主要特点包括：

*   **可扩展性：** 可扩展至9216个液冷芯片，通过高带宽片间互连 (ICI) 网络连接。
*   **计算能力：** 9216个芯片的配置可提供42.5 Exaflops算力，是全球最大超级计算机算力的24倍以上。每个独立芯片的峰值算力为4614 TFLOPs。
*   **增强型 SparseCore：** 提高了处理超大型嵌入的性能，扩大了工作负载在金融和科学领域的适用性。
*   **高带宽内存 (HBM)：** 每个芯片提供192 GB，比上一代增加6倍，以及7.2 TBps带宽，用于快速数据访问。
*   **改进的片间互连 (ICI)：** 具有1.2 Tbps双向带宽，增强了芯片之间的通信，从而实现高效的分布式训练和推理。
*   **能效：** 与上一代相比，每瓦性能提高了2倍，并且比2018年的第一个Cloud TPU节能近30倍。
*   **Pathways集成：** 利用Google DeepMind的ML运行时Pathways，可以在多个TPU芯片上实现高效的分布式计算，从而进行高级生成式AI计算。

Ironwood旨在管理大型语言模型 (LLM)、专家混合模型 (MoE) 和高级推理任务的复杂计算和通信需求，同时注重能效。 它将于今年晚些时候向Google Cloud客户提供。

---

## 4. 大学生如何使用Claude

**原文标题**: How University Students Use Claude

**原文链接**: [https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude](https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude)

无法访问文章链接。

---

## 5. Show HN: 我做了一个应用，用 Mermaidjs 生成故事关系图

**原文标题**: Show HN: I built an app to generate story relationships using Mermaidjs

**原文链接**: [https://github.com/herol3oy/austen](https://github.com/herol3oy/austen)

奥斯汀：一款AI驱动的Angular应用，利用Mermaidjs根据任何书籍的人物关系生成关系图（基于Analogjs构建）。用户可通过Open Library API搜索书籍，AI（DeepSeek或OpenAI）分析人物关系以创建可视化图表。

主要功能包括生成、保存、下载（SVG/PNG）和管理图表。用户还可以公开分享或私藏图表，并发现他人创建的公开图表。该应用使用Angular Material构建UI，Supabase作为后端（数据库和认证），并部署在Cloudflare Pages上。

技术栈包括Angular、Analog、TypeScript、Supabase、Cloudflare Pages、Angular Material和Mermaid。API集成包括Open Library、DeepSeek和OpenAI。设置步骤包括克隆仓库、安装依赖（npm install）、设置API密钥和Supabase的环境变量、创建包含“graphs”表的Supabase项目以及运行开发服务器（npm run dev）。未来的改进包括为图表添加点赞/取消点赞功能，以及为发现页面添加“加载更多”功能。

---

## 6. 在亚洲生产一双耐克鞋的成本你认为是多少？

**原文标题**: How much do you think it costs to make a pair of Nike shoes in Asia?

**原文链接**: [https://threadreaderapp.com/thread/1909741170953273353.html](https://threadreaderapp.com/thread/1909741170953273353.html)

该片段仅提供了标题和有关内容分享的元数据，但没有实际的文章内容。因此，无法概括文章。我们只知道这篇文章可能讨论了耐克鞋在亚洲的制造成本。要提供摘要，需要文章的实际文本。

---

## 7. 俄罗斯方块游戏中的生活质量

**原文标题**: Quality-of-Life in Tetris Games

**原文链接**: [https://jcarlosroldan.com/post/355](https://jcarlosroldan.com/post/355)

无法访问文章链接。

---

## 8. 视觉推理即将到来

**原文标题**: Visual Reasoning Is Coming Soon

**原文链接**: [http://arcturus-labs.com/blog/2025/03/31/visual-reasoning-is-coming-soon/](http://arcturus-labs.com/blog/2025/03/31/visual-reasoning-is-coming-soon/)

视觉推理在LLM中即将到来

---

## 9. 时空数据库

**原文标题**: SpacetimeDB

**原文链接**: [https://spacetimedb.com/](https://spacetimedb.com/)

时空数据库，因其核心功能而得名：存储应用程序的完整事务历史。 这些历史数据使用户能够将数据库状态恢复到之前的任何时间点，并从那时起重放事务。 这本质上提供了一个内置的重放功能，从而可以进行“时间旅行”调试和数据恢复。 该数据库的架构优先考虑跟踪随时间的变化，使其成为需要审计跟踪、版本控制或分析过去状态的应用的强大工具。

---

## 10. 使用内容安全策略加固 Firefox 前端

**原文标题**: Hardening the Firefox Front End with Content Security Policies

**原文链接**: [https://attackanddefense.dev/2025/04/09/hardening-the-firefox-frontend-with-content-security-policies.html](https://attackanddefense.dev/2025/04/09/hardening-the-firefox-frontend-with-content-security-policies.html)

Firefox如何通过内容安全策略(CSP)强化用户界面(UI)以抵御注入攻击（尤其是跨站脚本攻击XSS）。 Firefox UI使用Web技术构建，与Web应用程序类似，容易受到这些攻击。 近期Pwn2Own漏洞利用突显了从沙盒Web内容向父进程注入代码的风险。

主要解决方案是从核心UI文档`browser.xhtml`中移除内联JavaScript事件处理程序，并用独立JavaScript文件中的`addEventListener`调用替换它们。 已移除超过600个此类处理程序。 内联事件处理程序存在问题，因为它们允许攻击者注入恶意代码，而CSP默认情况下可以阻止这些内联脚本。

Firefox开发人员正在替换内联事件处理程序，并仔细考虑内联和常规事件处理程序之间的差异，尤其是在`return false`和`this`关键字方面。

虽然`browser.xhtml`由于其较大的攻击面而成为最初的重点，但这项工作正在扩展到其他UI组件。 一些组件，如“关于Firefox”对话框，已经使用了更严格的CSP，将资源加载限制为Firefox附带的资源。 最终目标是消除整个Firefox中的所有动态代码执行（如`eval`），从而增强对XSS攻击的安全性。

通过重写事件处理程序和实施强大的CSP，Firefox旨在提高攻击者的门槛，并显著提高其浏览器的安全性。 此项特定缓解措施将包含在Firefox 138中。

---

## 11. 前往美国旅行时如何锁定你的手机

**原文标题**: How to lock down your phone if you're traveling to the U.S.

**原文链接**: [https://www.washingtonpost.com/technology/2025/03/27/cbp-cell-phones-devices-traveling-us/](https://www.washingtonpost.com/technology/2025/03/27/cbp-cell-phones-devices-traveling-us/)

无法访问文章链接。

---

## 12. 我认识的最优秀的程序员

**原文标题**: The best programmers I know

**原文链接**: [https://endler.dev/2025/best-programmers/](https://endler.dev/2025/best-programmers/)

本文概述了卓越程序员的常见关键特征和习惯，强调了持续学习、解决问题和协作的重要性。它强调阅读文档、深入理解工具以及细致分析错误信息，而不是依赖猜测。

作者强调了诸如将复杂问题分解为可管理部分，以及不害怕“亲身实践”不熟悉代码等实用技能。他强调了通过写作、博客或开源贡献来帮助他人和分享知识的重要性，将强大的写作能力与代码中清晰、结构化的思维联系起来。

此外，本文强调了一种持续改进的思维模式，敦促开发人员拥抱新技术，同时仔细评估其益处。它提倡谦逊，向所有级别的工程师学习，无论资历如何，并通过有影响力的工作建立声誉。

至关重要的是，作者强调了对计算机和人都要有耐心，强调错误有其逻辑解释。他提倡通过承认“我不知道”然后寻找答案来保持诚实，并鼓励采用“保持简单”的编码方法以提高可维护性。总的来说，成为一名伟大的程序员没有捷径，它需要奉献精神、好奇心和协作精神。

---

## 13. 美国式颠覆

**原文标题**: American Disruption

**原文链接**: [https://stratechery.com/2025/american-disruption/](https://stratechery.com/2025/american-disruption/)

本·汤普森的《美国式颠覆》通过克莱顿·克里斯坦森的颠覆性创新理论，分析了美国制造业的衰落。他回顾了过去 Stratechery 的文章，这些文章事后看来未能完全捕捉到正在展开的现实，并认为美国正在“对世界关上大门”，而不是相反。

汤普森解释了美国制造业，特别是半导体行业，是如何被亚洲制造业的崛起所颠覆的。更廉价的劳动力、改善的交通运输和标准化的集装箱使得跨国公司可以将制造业外包给亚洲，优先考虑成本效益。模块化的产品设计也促进了这一点，允许公司专注于核心竞争力并外包其他组件。

他强调了规模在新兴市场和低端颠覆中的重要性。亚洲工厂扩大规模以满足全球需求，变得非常灵活地适应各种订单，这是美国老式制造模式所缺乏的特性。芯片制造成本高昂，促使生产向集中化转变，台积电就是一个例子，这对英特尔等集成制造商构成了挑战。

汤普森认为，美国不能简单地恢复到像 iPhone 组装这样的低工资制造业岗位。这些工作不受欢迎，而且技能不足以胜任现代自动化制造，因此，政治家们提出的将此类工作带回来的说法是不现实的。他强调了失去对具有军事应用的重要技术供应链控制权的危险性。

尽管存在颠覆性力量，汤普森认为，现代的成功取决于控制需求，而不仅仅是供应。他总结说，理解新的、数字驱动的格局，并认识到颠覆的局限性，对于驾驭未来至关重要。

---

## 14. Show HN: Fermi – 一款培养数量级思维的类Wordle游戏

**原文标题**: Show HN: Fermi – A Wordle-style game for order-of-magnitude thinking

**原文链接**: [https://fermi-game.andrewnoble.me/](https://fermi-game.andrewnoble.me/)

费米是一款受Wordle启发的游戏，旨在测试并提高人们估算十的幂次数值的能力，从而促进数量级思维。该游戏挑战玩家猜测一个目标数字，并且在每次猜测后，它会提供反馈，指示猜测与正确答案之间的差距，以数量级表示。这与Wordle基于精确字母的反馈不同，因为费米侧重于估计的相对尺度。

该游戏旨在兼具教育性和趣味性，鼓励玩家更好地理解大数和小数及其相互关系。通过提供关于数量级的迭代反馈，它帮助玩家完善对指数尺度的理解并提高他们的估算技能。关键在于，费米旨在使学习和使用科学计数法和数量级变得更易于理解和更具娱乐性。

---

## 15. 虚假求职者涌入招聘远程职位的美国公司

**原文标题**: Fake job seekers are flooding US companies that are hiring for remote positions

**原文链接**: [https://www.cnbc.com/2025/04/08/fake-job-seekers-use-ai-to-interview-for-remote-jobs-tech-ceos-say.html](https://www.cnbc.com/2025/04/08/fake-job-seekers-use-ai-to-interview-for-remote-jobs-tech-ceos-say.html)

美国公司正面临越来越多的虚假求职者利用人工智能制造虚假身份并通过远程工作面试的浪潮。这些冒名顶替者使用人工智能工具伪造照片身份证明、生成就业历史并回答面试问题，使得他们难以被发现。网络安全和加密货币公司尤其成为目标。高德纳估计，到2028年，全球四分之一的求职者将是假的。

聘用这些人的风险从简单的薪资盗窃到更严重的威胁，例如安装恶意软件、窃取客户数据、商业机密或资金。文章中强调的一个例子是“Ivan X”，他是一名假冒求职者，在与Pindrop Security的视频面试中使用深度伪造技术来掩盖自己的面部。他的真实位置被追踪到位于朝鲜边境附近的俄罗斯军事设施。

朝鲜IT工作者已被确认为虚假求职者的重要来源，他们使用盗用的美国身份来获得远程工作，并将工资输送回朝鲜以资助其武器计划。然而，这个问题已经蔓延到其他国家（如俄罗斯、中国、马来西亚和韩国）的犯罪团伙。

公司现在正在转向身份验证服务，以帮助淘汰虚假求职者。随着深度伪造技术的进步，检测这些欺诈性求职者变得更具挑战性，需要先进的视频和语音验证程序。文章强调，公司必须更加意识到这种威胁，并投资于相关技术以保护自己免受这些复杂的诈骗。

---

## 16. PostgreSQL 全文搜索：用对方法，速度飞快（打破缓慢神话）

**原文标题**: PostgreSQL Full-Text Search: Fast When Done Right (Debunking the Slow Myth)

**原文链接**: [https://blog.vectorchord.ai/postgresql-full-text-search-fast-when-done-right-debunking-the-slow-myth](https://blog.vectorchord.ai/postgresql-full-text-search-fast-when-done-right-debunking-the-slow-myth)

无法访问文章链接。

---

## 17. 双机React

**原文标题**: React for Two Computers

**原文链接**: [https://overreacted.io/react-for-two-computers/](https://overreacted.io/react-for-two-computers/)

React用于两台电脑：探讨HTML标签与函数调用的概念异同，并进行关于跨电脑远程函数调用的思想实验。作者首先考察标签和函数调用在传递信息和嵌套方面的相似之处，但标签通常是名词，用于描述结构（蓝图），而函数调用通常是动词，用于描述过程（配方）。他认为蓝图本质上是“潜在的配方”，而标签是“潜在的函数调用”。文章随后深入探讨了在不同电脑上调用函数所面临的挑战，探索了等待网络响应时需要“暂停”执行的问题。作者介绍了`callNetwork` API，并指出了两个主要问题：代码缠结和代码片段之间的连接中断。为了解决这些问题，作者提出了两种解决方案：引入`async/await`来管理代码缠结，以及发明`import rpc`，将远程函数视为本地导入，从而实现类型检查和更轻松的导航。这种`import rpc`语法将表明导入的函数通过网络调用远程执行，确保类型序列化和异步处理。最后，文章暗示了这种方法在处理不直接响应的电脑时的局限性，留给读者进一步思考解决方案。

---

## 18. 手册页很棒，手册阅读器是问题所在。

**原文标题**: Man pages are great, man readers are the problem

**原文链接**: [https://whynothugo.nl/journal/2025/04/09/man-pages-are-great-man-readers-are-the-problem/](https://whynothugo.nl/journal/2025/04/09/man-pages-are-great-man-readers-are-the-problem/)

本文认为，man pages（例如缺少链接和重排）的局限性并非man page格式本身 (mdoc(7) 和 man(7)) 固有的，而是由于 `man(1)` 等 man page 阅读器的不足。

作者解释说，用于现代 man pages 的 mdoc 格式支持语义标记，并包含用于交叉引用 (.Xr) 和页面内引用 (.Sx) 的宏，这些宏可以呈现为超链接。当 man pages 转换为 HTML 时，这些宏 *确实* 变成了链接。然而，格式化 man page 并将其通过管道传递给 `less(1)` 的常见做法阻止了这些功能的使用。

核心论点在于，问题不在于格式的功能，而在于阅读器无法解释和显示这些链接功能。作者提倡开发新的 man page 阅读器，这些阅读器能够原生理解 man page 格式并可以呈现链接，以及动态重排文本以适应终端窗口。Man pages 的局限性不是格式的局限性，而是阅读器的局限性。

---

## 19. 2025年氟化物与儿童智商元分析的主要缺陷

**原文标题**: Major Flaws in 2025 Meta-Analysis on Fluoride and Children IQ Scores

**原文链接**: [https://osf.io/preprints/osf/zhm54_v3](https://osf.io/preprints/osf/zhm54_v3)

这似乎是网页的部分摘录，可能托管在开放科学框架（OSF）上。它提到了一个标题：“2025年关于氟化物与儿童智商的Meta分析的主要缺陷。”然而，它实际上并没有提供*关于*这些缺陷或Meta分析本身的任何内容。存在的唯一其他信息是一条通用的JavaScript启用消息。

因此，无法总结文章的内容，因为提供的片段*不包含文章的内容*。要提供摘要，需要文章的全文或更详细的摘要。仅根据标题，假设的文章可能批判了2025年的一项Meta分析（一项综合多项研究结果的研究），该分析检验了氟化物暴露与儿童智商之间的关系，并认为该Meta分析存在重大的方法论或解释性缺陷。

---

## 20. 减少屏幕时间指南

**原文标题**: A guide to reduce screen time

**原文链接**: [https://speedbumpapp.com/en/blog/how-to-reduce-screen-time/](https://speedbumpapp.com/en/blog/how-to-reduce-screen-time/)

本文《如何减少屏幕使用时间：终极指南》，发表于2025年3月7日，提供了超过40个技巧，帮助个人在在线参与和现实生活活动之间找到平衡。它首先强调理解过度使用屏幕时间背后的原因的重要性，例如无聊、焦虑、拖延和肌肉记忆，然后过渡到实际解决方案。

文章建议将目标从“减少手机使用”重新定义为“更多地做其他事情”，并建议创建一个替代活动清单。然后，它深入研究工具和技术，从iOS和Android上的内置屏幕时间功能开始，重点介绍使用情况分析、应用程序限制和专注时间等功能。它还提到了iOS Shortcuts和三星的Modes和Routines等高级选项，以便进行进一步的自定义。

文章提供了一个精心策划的屏幕时间限制应用程序列表，如One Sec、Opal、SpeedBump、Clearspace、ScreenZen、Focus Plant和Forest，每个应用程序都有其独特的方法，如强制深呼吸、计划阻止、限制会话时间、游戏化和阻止特定网站功能。

进一步的策略包括管理通知、组织应用程序布局、使用灰度模式、建立无屏幕区域、订阅新闻通讯以及选择模拟替代品，如实体书籍和报纸。文章还提倡使用应用程序的浏览器版本，拥抱无聊，甚至考虑通过卸载应用程序或使用功能机来彻底休息。

结论强调了持续努力和实验的重要性，并指出最初的几周最具挑战性，但坚持不懈会带来健康的习惯。它承认社交媒体应用程序的成瘾性，并鼓励读者采取行动，实施一些选定的技巧并跟踪他们的进展。文章以常见问题解答部分结尾，解答有关桌面使用、通知影响和建议的屏幕时间限制的问题。

---

## 21. 类太阳恒星

**原文标题**: 'Sun-Like' Stars

**原文链接**: [https://www.centauri-dreams.org/2025/04/08/on-sun-like-stars/](https://www.centauri-dreams.org/2025/04/08/on-sun-like-stars/)

关于“类太阳”恒星：

本文《关于“类太阳”恒星》探讨了系外行星科学中“类太阳”一词的模糊性和多种解读，尤其是在针对公众的新闻稿中。作者保罗·吉尔斯特指出，“类太阳”的定义范围可以从严格的G型恒星（如我们的太阳）到包括F、G和K型恒星，甚至包括所有的主序星（OBAFGKM）。

作者认为，这种缺乏明确性可能会使公众感到困惑，并影响对系外行星研究的认知，从而可能影响资金。他强调，被认为是“类太阳”的恒星的百分比因所使用的定义而异，这极大地改变了潜在围绕它们运行的行星的估计数量。

本文通过新闻稿的例子来说明“类太阳”一词是如何应用于那些并不严格符合太阳分类的恒星的。吉尔斯特建议，科学家们需要在公共传播中更加精确，并澄清他们对“类太阳”和“类地”的定义，以避免误导公众。

评论部分进一步讨论了宜居性的复杂性，强调了我们的理解仅限于我们自己的太阳系。评论者强调，在定义与系外行星相关的术语时需要谨慎和清晰，并承认在数据有限的情况下推测地球以外的生命所面临的挑战。

---

## 22. Cyc 讣告

**原文标题**: Obituary for Cyc

**原文链接**: [https://yuxi-liu-wired.github.io/essays/posts/cyc/](https://yuxi-liu-wired.github.io/essays/posts/cyc/)

本文是关于Cyc的“讣告”，Cyc是道格拉斯·列纳特(Douglas Lenat)耗费数十年时间的项目，旨在通过符号逻辑和庞大的知识库来实现通用人工智能(AGI)。文章认为，Cyc最终未能兑现其承诺。

列纳特之前的工作，包括AM和EURISKO，启发他相信人工智能需要一个庞大的常识知识基础。1985年，他启动了Cyc项目，旨在手动编码数百万的事实和规则。虽然Cyc以巨大的成本增长到3000万条断言，但它从未实现真正的机器学习或AGI。

尽管通过商业应用实现了财务稳定，但这些应用主要涉及标准的专家系统技术，而非高级智能。Cyc在很大程度上与学术界的人工智能社区隔离，难以使用，并且在基准测试中从未表现良好。衍生项目也失败了。

文章将Cyc的失败归因于列纳特对人工智能的单一、符号逻辑愿景的rigid adherence，拒绝了其他方法。到2025年，该项目没有显示出实现AGI的迹象，是对符号逻辑方法的一种控诉。

文章深入探讨了列纳特早期的项目AM，一个“自动数学家”。虽然AM据称重新发现了数学概念，但它的成功在很大程度上依赖于手动调整的启发式规则和列纳特的干预，并且这些规则的细节仍然模糊不清。这说明了Cyc类方法的一个核心问题：依赖于手工制作的知识和规则，而不是发展真正的学习能力。

---

## 23. 劳力士7135机芯：全新间接脉冲擒纵系统和高频机芯

**原文标题**: Rolex Caliber 7135: new indirect impulse escapement and high frequency movement

**原文链接**: [https://www.hodinkee.com/articles/introducing-rolex-land-dweller](https://www.hodinkee.com/articles/introducing-rolex-land-dweller)

文章重点介绍了一种新的机芯——劳力士7135型机芯，该机芯采用间接脉冲擒纵机构和高频机芯。这表明劳力士在制表技术方面具有潜在的进步。

文章还提到，瑞士手表公司的CEO们预计今年生产的手表数量将会减少。这归因于经济不稳定对消费者信心产生了负面影响。这暗示着奢侈手表市场可能出现衰退，或者至少是放缓。

本质上，这篇文章呈现了一种对比：劳力士Caliber 7135型机芯的创新技术发展，与可能限制整体手表产量的具有挑战性的经济前景形成对比。

---

## 24. 用 RPython 完成 Prospero 挑战

**原文标题**: Doing the Prospero-Challenge in RPython

**原文链接**: [https://pypy.org/posts/2025/04/prospero-in-rpython.html](https://pypy.org/posts/2025/04/prospero-in-rpython.html)

本文详细介绍了作者尝试优化Prospero挑战赛代码的过程，该挑战赛涉及通过计算每个像素的大型数学公式来渲染图像。该公式采用SSA形式，使其适合优化。

作者从基准解释器开始，然后实现四叉树来递归地细分图像，并在每个级别使用范围分析简化公式。创建了一个基于区间抽象解释的简单优化器，以减少操作次数。

为了确保区间计算的正确性，作者使用了基于假设的属性测试来检查区间域抽象转移函数的可靠性。

作者尝试了窥孔优化，包括Matt Keeter的Fidget实现中的优化，但发现大多数优化都无效，甚至由于检查重写的开销而增加了运行时。只有Matt的min/max优化被证明是有益的。

最重要的优化是“按需信息”，它利用了只有最终结果（像素颜色）的符号相关的特性。这允许通过删除不会影响结果符号的变量来简化min/max操作。虽然在RPython中进行了原型设计，但最终实现是用C语言重写的，以获得更好的性能。代码可在Github上找到。

---

## 25. 展示 HN: 比较 OpenAI、Anthropic 和 Perplexity 的产品排名

**原文标题**: Show HN: Comparing product rankings by OpenAI, Anthropic, and Perplexity

**原文链接**: [https://productrank.ai/](https://productrank.ai/)

此“Show HN”帖分享了由三个不同AI模型（OpenAI、Anthropic和Perplexity）生成的产品排名比较。该文章可能探讨了这些AI模型如何基于各种因素（如功能、价格、客户评价和市场份额）对产品进行排名。分享此帖的用户旨在突出显示每个AI提供的排名的异同，暗示了对其在产品分析和推荐方面的能力进行评估和基准测试的潜力。

关键在于比较本身。文章可能分析：

*   **每个AI用于排名的标准。**（例如，一个是否优先考虑功能而非价格？另一个是否更注重客户评价？）
*   **模型之间的一致性程度。**（它们是否普遍认同顶级产品，还是存在显著差异？）
*   **每个AI提供的排名背后的原因。**（这将涉及理解每个AI如何处理和解释用于排名的数据。）

最终，“Show HN”帖旨在引发对不同AI模型在产品评估中的能力和局限性的讨论和兴趣，以及它们如何应用于实际应用，例如个性化推荐或竞争分析。这是对AI在电子商务和产品研究中实际应用的探索。

---

## 26. 麦克风输入噪声对比 – Avisoft生物声学

**原文标题**: Microphone Input Noise Comparison – Avisoft Bioacoustics

**原文链接**: [https://avisoft.com/recorder-tests/](https://avisoft.com/recorder-tests/)

Avisoft生物声学：便携式录音机麦克风输入噪声水平对比分析

本页面对比分析了各种便携式录音机的麦克风输入噪声水平，旨在为记录微弱动物声音的研究人员提供标准化评估。 考虑到制造商使用的规格不一致，本页面提供了一组同质化数据，以便进行客观比较。

本页面的核心是一个表格，列出了各种录音机型号及其：在150欧姆下测量的等效输入噪声 (EIN)（A计权和20Hz-20kHz未计权）、输入削波电平（对应于0 dBFS）以及最大增益下的动态范围（A计权）。 这些指标使用户能够评估录音机在不产生过多噪声的情况下捕获安静声音的能力。

EIN值以dBu表示，表明录音机输入级的理论噪声基底。较低的dBu值表示更少的噪声和更好的性能。输入削波电平显示了录音机在失真之前可以处理的最大信号幅度。 动态范围反映了噪声基底和削波电平之间的差异，代表了录音机可以准确捕获的信号幅度范围。

除非另有明确说明，否则提供的数据包括在最大增益设置下的测量值，这使用户能够在最苛刻的录音条件下评估性能。 一些录音机有多个条目，反映了不同的增益设置，标有“*非最大增益！”标签。 这种全面的比较使使用者能够根据其特定的生物声学研究需求，就录音机选择做出明智的决定。

---

## 27. Lisp 中超越传统模式匹配

**原文标题**: Beyond Traditional Pattern Matching in Lisp

**原文链接**: [https://github.com/naver/lispe/wiki/6.1-Pattern-Matching-in-LispE](https://github.com/naver/lispe/wiki/6.1-Pattern-Matching-in-LispE)

本文介绍了 Naver 开发的 Lisp 方言 LispE，重点介绍了其独特的功能：`defpat`、`defmacro` 和 `defpred`。这些结构通过高级模式匹配、改进的宏功能和逻辑编程元素增强了传统的 Lisp 功能。

`defpat` 允许在同一名称下定义多个函数，每个函数都由特定的参数模式触发。 它支持 Kleene 运算符来匹配序列，从而为多态性提供了一种声明式方法，FizzBuzz 和列表处理示例证明了这一点。

`defmacro` 通过模式匹配和 `$` 运算符扩展了宏系统，从而简化了自定义语法的创建。 一个自定义循环宏优雅地处理不同的方向参数，说明了这一点。

`defpred` 引入了基于谓词的评估和自动回溯。 `defpred` 函数中的每个指令都被视为一个布尔测试，失败会触发回溯。 一个例子展示了如何根据条件过滤数字。

本文将这些特性与 Common Lisp、Scheme 和 Clojure 中等效的实现进行了对比，展示了 LispE 由于其集成的模式匹配和回溯机制而具有更简洁和富有表现力的语法。 LispE 以其丰富的模式、简化的宏转换和内置的回溯功能脱颖而出，使其成为复杂数据操作、自定义语法定义和逻辑推理任务的引人注目的选择。

---

## 28. 展示一下：我建了一个雅虎通风格的网页聊天应用——纯粹的怀旧

**原文标题**: Show HN: I built a Yahoo Messenger-inspired web chat app – pure nostalgia

**原文链接**: [https://buzzed.chat](https://buzzed.chat)

这个“Show HN”帖子介绍了一个名为“MessengerYou”的网页聊天应用，旨在唤起人们对雅虎通的回忆。该应用被呈现为一个让人想起经典聊天平台的项目，暗示着重点在于重现熟悉的界面，以及可能一些定义雅虎通的关键功能。

帖子非常简短，但暗示这是一个为了享受而构建的个人项目，并且可能与他人分享怀旧体验。“Buzzed!”一词和对雅虎通的明确提及是建立该应用意图的关键，即触发人们对旧服务的记忆。最后一行“你需要启用JavaScript才能运行此应用”表明该应用是客户端重的，依赖JavaScript来实现其功能。

---

## 29. 一个LLM查询理解服务

**原文标题**: An LLM Query Understanding Service

**原文链接**: [https://softwaredoug.com/blog/2025/04/08/llm-query-understand](https://softwaredoug.com/blog/2025/04/08/llm-query-understand)

本文概述了如何构建一个由LLM驱动的查询理解服务，该服务可以将非结构化搜索查询转换为结构化数据，从而改善搜索结果。作者演示了一种实用方法，使用开源LLM、FastAPI和Google Kubernetes Engine (GKE)进行部署。

该服务的核心是一个FastAPI应用程序，它与轻量级LLM (Qwen2-7B)交互以解析用户查询。 创建了一个包含优化后的PyTorch的Docker镜像，并部署到GKE的自动驾驶模式，从而简化了Kubernetes管理。 部署包括GPU资源、内存和CPU分配的规范。 实施了一个持久卷，通过缓存到huggingface来解决模型数据的存储限制。

文章随后将最初的“hello world”LLM服务重构为查询解析服务。 它引入了一个特定的提示，以指导LLM从家具搜索查询中提取关键属性，例如物品类型、材料和颜色，并将它们作为JSON输出。 最后，加入了一个Valkey缓存，通过存储和检索基于提示和查询的先前响应，从而显著提高性能并降低LLM负载。

作者强调了负载测试、提示调优以及潜在的架构改进（分离LLM硬件）对于扩展和改进服务的重要性。 本文旨在作为一个起点，学习如何使用LLM“作弊式搜索”。

---

## 30. Apache ECharts

**原文标题**: Apache ECharts

**原文链接**: [https://echarts.apache.org/en/index.html](https://echarts.apache.org/en/index.html)

Apache ECharts 是一个声明式的框架，旨在快速创建基于 Web 的可视化图表。该文本强调了 ECharts 的用途，并鼓励用户在研发、产品、研究论文、技术报告、新闻报道、书籍、演示、教学、专利以及其他相关知识产权活动中使用该框架时，引用特定的研究论文：“Visual Informatics, 2018 [PDF]”。 本质上，该文本旨在推广对 ECharts 使用的正确归属和学术认可。

---

## 31. Show HN: DrawDB – 开源在线数据库图表编辑器 (复古风)

**原文标题**: Show HN: DrawDB – open-source online database diagram editor (a retro)

**原文链接**: [https://www.drawdb.app/](https://www.drawdb.app/)

本文介绍DrawDB，一个开源的在线数据库图表编辑器和SQL生成器。其核心功能允许用户通过图表界面直观地设计数据库模式。它还能根据图表生成SQL脚本，简化数据库创建过程。这篇文章简短且缺乏细节，但主要信息是推出一款旨在通过可视化图表和SQL代码生成来简化数据库设计和管理的新工具。需要注意的是，用户需要启用Javascript才能使用该在线工具。

---

## 32. Show HN: Dynomate - 快速、Git友好的 DynamoDB GUI客户端 (Dynobase 替代品)

**原文标题**: Show HN: Dynomate– Fast, Git-Friendly DynamoDB GUI Client (Dynobase Alternative)

**原文链接**: [https://dynomate.io/](https://dynomate.io/)

Dynomate：面向无服务器团队的 DynamoDB GUI 客户端，旨在成为 Dynobase 之外更友好的开发者替代方案。它提供 SSO、多会话和多标签页支持以及请求链等功能，以提高工作流程效率。

主要特点包括：

*   **无缝 AWS 集成与简易 SSO 认证：** Dynomate 自动检测 AWS 凭证并支持一键式 SSO 登录。
*   **高级表管理与查询工具：** 提供表格和原始 JSON 视图、内联和批量编辑以及详细的请求日志。
*   **多标签页界面：** 允许同时管理多个 DynamoDB 表和 AWS 配置文件。
*   **本地请求持久化与 Git 集成：** 将查询本地保存以便进行版本控制和团队协作，从而增强安全性。
*   **强大的查询模式与操作链：** 顺序或并发执行多个 DynamoDB 查询，支持环境变量，并允许链接请求。
*   **开发者友好的工作流程与日志记录：** 提供全面的调试日志记录、全局搜索和 JSON 编辑器。

目前适用于 macOS，计划推出 Windows 和 Linux 版本。 Dynomate 提供一次性购买的专业许可证，价格为 199 美元（折扣前为 299 美元），其中包括一年的更新和所有功能的使用权，并可以选择以 89 美元续订。

---

## 33. Linux内核防御图 – 安全加固概念

**原文标题**: Linux Kernel Defence Map – Security Hardening Concepts

**原文链接**: [https://github.com/a13xp0p0v/linux-kernel-defence-map](https://github.com/a13xp0p0v/linux-kernel-defence-map)

本文介绍了 Linux 内核防御图，这是一种以图形方式呈现 Linux 内核安全加固概念及其关系的工具。该图由 a13xp0p0v 创建，将漏洞类别（带有 CWE 编号）、利用技术、漏洞检测机制和防御技术（包括内核内和内核外）连接起来。这些连接表示的是关系，不一定表示完全缓解。

该图旨在帮助浏览内核文档和源代码。它不包括攻击面缩减、用户空间安全功能和 Linux 安全模块策略。

该图使用 DOT 语言编写，便于维护，并使用 GraphViz 生成 SVG 图。源代码可在 GitHub、Codeberg 和 GitFlic 上获得，并以 GPL-3.0 许可证发布。

作者还创建了“kernel-hardening-checker”，用于自动验证 Linux 内核中安全加固选项的配置，其中许多选项在主要发行版中默认情况下未启用。

最后，本文提供了一个参考列表，包括关于 Grsecurity 功能、内核自保护、漏洞缓解和内核漏洞历史的资源。该图专为 Linux 内核 v6.10 设计。

---

## 34. 特朗普的司法部将不再起诉加密货币欺诈。

**原文标题**: Trump's DOJ will no longer prosecute cryptocurrency fraud

**原文链接**: [https://www.theverge.com/policy/645399/trump-doj-cryptocurrency-fraud-prosecutions-memo](https://www.theverge.com/policy/645399/trump-doj-cryptocurrency-fraud-prosecutions-memo)

在特朗普政府领导下，司法部(DOJ)正结束对加密货币欺诈的起诉重点，转变为其所谓的“以起诉进行监管”。副总检察长托德·布兰切的一份备忘录指示联邦检察官停止对数字资产施加监管框架的诉讼和执法行动，特别是针对虚拟货币交易所、混币服务以及因用户行为或无意违规行为而针对线下钱包的行动。与此政策不符的未决调查将被终止。

这一政策转变发生在特朗普一度对加密货币持怀疑态度，但后来拥抱了该行业之后，他接受了来自加密货币亿万富翁的捐款，甚至推出了自己的加密货币平台。批评人士认为，他是在奖励支持他选举的加密货币利益集团。

除了司法部策略的转变，特朗普的证券交易委员会(SEC)也已放弃对Robinhood和Coinbase等加密货币相关公司的调查和诉讼。司法部的新重点将是起诉直接侵害加密货币投资者权益或利用数字资产从事恐怖主义、毒品贩运和有组织犯罪等犯罪活动的人。

---

## 35. 非线性声片显微镜：不透明器官毛细血管/细胞尺度成像

**原文标题**: Nonlinear soundsheet microscopy:imaging opaque organs capillary/cellular scale

**原文链接**: [https://www.science.org/doi/10.1126/science.ads1325](https://www.science.org/doi/10.1126/science.ads1325)

无法访问文章链接。

---

## 36. NTATV：让初代Apple TV运行Windows NT（Windows XP、Windows 2003）

**原文标题**: NTATV: Bringing Windows NT (Windows XP, Windows 2003) to the Original Apple TV

**原文链接**: [https://github.com/DistroHopper39B/NTATV](https://github.com/DistroHopper39B/NTATV)

NTATV是由DistroHopper39B发起的一个项目，该项目成功地在初代Apple TV上启动了Windows XP和Windows Server 2003。初代Apple TV原本是为基于macOS的软件设计的。该项目通过使用ReactOS的FreeLoader引导程序的定制版本，克服了Apple TV仅支持EFI固件的限制。

虽然ReactOS本身可以启动到桌面，但PCI和USB功能目前已损坏，导致大多数硬件无法使用。然而，Windows XP和2003具有可用的PCI、USB和基本视频驱动程序，从而可以获得可用的桌面。以太网和WiFi也正常工作。一些功能存在限制，例如HDMI音频由于独特的硬件配置，可能永远无法正常工作，并且NTVDM（DOS支持）无法运行。

已知的问题包括显示器待机需要重新插拔HDMI，以及分量视频只显示蓝色。该项目的源代码和构建说明可在GitHub上找到，该项目已发布了多个版本，其中包含IDE驱动程序修复和预构建的包含NVIDIA驱动程序的镜像等改进。该项目感谢ReactOS和Apple TV Linux社区的各种开发者和贡献者。

---

## 37. 钡实验

**原文标题**: The Barium Experiment

**原文链接**: [https://tomscii.sig7.se/2025/04/The-Barium-Experiment](https://tomscii.sig7.se/2025/04/The-Barium-Experiment)

无法访问文章链接。

---

## 38. 一种使盲人和低视力读者更容易获取图表的新方法

**原文标题**: A new way to make graphs more accessible to blind and low-vision readers

**原文链接**: [https://news.mit.edu/2025/making-graphs-more-accessible-blind-low-vision-readers-0325](https://news.mit.edu/2025/making-graphs-more-accessible-blind-low-vision-readers-0325)

麻省理工学院CSAIL开发了Tactile Vega-Lite，一种旨在简化为盲人和低视力读者创建触觉图表的新系统。该工具通过简化设计流程，弥合了标准视觉图表和触觉替代方案之间的差距，而使用现有方法时，该流程可能既漫长又复杂。

Tactile Vega-Lite接收数据，例如来自Excel电子表格的数据，并自动生成视觉图表和触觉图表。该系统将可访问性指南作为默认规则，使教育工作者和设计人员能够高效地生成可访问的触觉图形，如条形图或折线图，这些图形可以压印以进行触觉阅读。

该工具兼顾了易用性和设计精确性，允许用户通过带有简化“抽象”的代码编辑器自定义图表元素。示例库帮助用户理解代码的效果。虽然该团队计划使界面更加用户友好，但他们也强调，它不能取代专家审查以确保完全符合指南。

研究人员希望为压印前预览图表添加机器特定的自定义功能。该项目得到了国家科学基金会的支持，并采纳了残疾服务机构和像盲人灯塔协会等组织的反馈。专家们赞扬Tactile Vega-Lite有潜力为触觉阅读者提供更快、更准确的数据访问，最终提高信息可访问性。

---

## 39. 更美观的排版：使用 text-wrap: pretty

**原文标题**: Better typography with text-wrap pretty

**原文链接**: [https://webkit.org/blog/16547/better-typography-with-text-wrap-pretty/](https://webkit.org/blog/16547/better-typography-with-text-wrap-pretty/)

Jen Simmons 的这篇文章探讨了新的 CSS 属性 `text-wrap: pretty`，重点介绍了它在 Safari Technology Preview 中的实现，并将其与其他 `text-wrap` 值（如 `balance`）进行了对比。核心思想是，`pretty` 旨在通过模仿传统排版的润色效果来增强数字排版，解决诸如短行尾、不良参差、较差的连字符以及文字河流等问题。

与标准的单行换行算法不同，`text-wrap: pretty` 会分析整个段落，以优化换行符，从而提高可读性和美观性。Safari 的实现不仅防止了短行尾，还改善了文本的整体“参差”效果。虽然像 Chrome 这样的其他浏览器已经实现了更有限的 `pretty` 版本，主要侧重于最后几行，但 Safari 的版本考虑了整个段落。

这篇文章强调了 `pretty` 对正文的好处，使其看起来更加精致和专业。它还将 `pretty` 与 `text-wrap: balance` 进行了对比，解释说 `balance` 旨在使所有行在长度上大致相等，这可能适用于标题和字幕，但可能并不总是正文或需要填充容器宽度的情况下的理想选择。

性能是一个关键考虑因素，文章向开发人员保证，Safari 的实现经过优化，可以避免负面影响，尤其是在应用于典型长度的段落时。Simmons 鼓励开发人员尝试 `text-wrap: pretty`，并报告任何性能问题，以帮助在全面发布之前完善该功能。

---

## 40. Dockerfmt：Dockerfile 格式化工具

**原文标题**: Dockerfmt: A Dockerfile Formatter

**原文链接**: [https://github.com/reteps/dockerfmt](https://github.com/reteps/dockerfmt)

Dockerfmt 是一个基于内部 buildkit 解析器构建的 Dockerfile 格式化工具，为 dockfmt 提供了一个现代的替代方案。它根据最佳实践格式化 Dockerfile，并利用 `mvdan/sh` 库来格式化 `RUN` 步骤。

主要功能包括：

*   **安装：** 可以从发布页面下载二进制文件。
*   **用法：** 该工具可以通过指定文件路径来格式化 Dockerfile，也可以与 `completion`、`help` 和 `version` 等命令一起使用。
*   **标志：** 命令行标志控制行为，包括检查格式 (`-c`)、缩进 (`-i`)、换行符处理 (`-n`) 和将更改写回文件 (`-w`)。
*   **Pre-commit 集成：** 使用 `.pre-commit-config.yaml` 条目轻松将 dockerfmt 集成到您的工作流程中。
*   **局限性：** 目前不支持 `RUN` 命令中的命令分组/分号、长 JSON 命令的换行以及 `# escape=X` 指令。
*   **特性：** 支持基本的 heredoc 和 `RUN` 步骤中的内联注释，在格式化期间保留注释位置。
*   **JS 绑定：** JavaScript 绑定在 `js` 目录中可用。

欢迎贡献。

---

## 41. 财政部OCC称黑客曾访问15万封邮件

**原文标题**: Treasury's OCC Says Hackers Had Access to 150k Emails

**原文链接**: [https://www.securityweek.com/treasurys-occ-says-hackers-had-access-to-150000-emails/](https://www.securityweek.com/treasurys-occ-says-hackers-had-access-to-150000-emails/)

文章报道称，作为针对联邦机构的大规模网络攻击的一部分，美国财政部下属机构货币监理署 (OCC) 披露，黑客未经授权访问了约 15 万个电子邮件帐户。虽然OCC的声明没有明确具体的时间范围或可能泄露的信息的性质，但它确认该机构正在努力评估影响并实施必要的安全增强措施。

此次披露可能与影响众多政府机构和私营公司的更广泛的SolarWinds供应链攻击有关。OCC的通知是调查和修复SolarWinds事件造成的损害的更大努力的一部分，在该事件中，恶意行为者入侵了SolarWinds的Orion软件，以获得对受害者网络的访问权限。

OCC强调，它正在认真对待这一事件，并与其他联邦机构合作，以了解漏洞的全部范围并减轻任何潜在风险。他们还专注于加强其网络安全态势，以防止将来发生类似的事件。文章表明，这一最新披露进一步凸显了 SolarWinds 攻击对美国政府实体的严重性和广泛影响。

---

## 42. Show HN: Webtor – 开源种子流媒体引擎

**原文标题**: Show HN: Webtor – open-source torrent streaming engine

**原文链接**: [https://webtor.io](https://webtor.io)

Webtor是一个开源的种子流媒体引擎，简化了种子下载和流媒体播放。它允许用户将种子文件或磁力链接转换为直接下载链接，而无需种子客户端或VPN。用户可以将种子文件上传到Webtor.io，然后下载单个文件、直接在浏览器中流式传输视频和音频，或者将整个种子下载为ZIP压缩包。

主要功能包括：直接下载链接、对常见格式的即时视频/音频流媒体支持、用于无缝集成的Chrome扩展、ZIP压缩包下载以及开发者友好的SDK。

该平台强调用户隐私和安全，声称使用Webtor.io类似于使用YouTube等普通网站，利用HTTPS加密并防止用户的IP地址在BitTorrent网络上广播。

虽然有广告支持，但用户可以通过支持该项目来移除广告并获得更快的速度。该服务可在移动设备上访问，无需额外应用。整个项目是开源的，并在MIT许可下在GitHub上提供。

---

## 43. 用Prolog解“雷顿教授”谜题

**原文标题**: Solving a “Layton Puzzle” with Prolog

**原文链接**: [https://buttondown.com/hillelwayne/archive/a48fce5b-8a05-4302-b620-9b26f057f145/](https://buttondown.com/hillelwayne/archive/a48fce5b-8a05-4302-b620-9b26f057f145/)

本文探讨了使用Prolog解决“雷顿谜题”——一种逻辑谜题，该谜题涉及根据其他学生的答案和分数推断出某个学生的考试分数。作者旨在展示一个比朋友之前的尝试更为优雅的Prolog解决方案。

作者首先介绍了核心组件：`score/3`谓词，它根据学生的答案和答案键计算分数；以及`key/1`谓词，它根据给定的学生分数定义有效答案键的约束条件。他们强调了Prolog的双向性，展示了谓词如何用于检查、计算和推断。

作者随后强调了明确定义约束条件的重要性，例如答案键的长度和允许的值（a或b）。他们介绍了`maplist`，作为一种简洁的方式来对列表元素强制执行这些约束。

解决方案揭示了存在多个有效的答案键，但所有答案键都导致第四个学生获得相同的分数，从而解决了这个谜题。与最初的80行代码相比，作者成功地实现了一个更短、更优雅的解决方案（15行代码），展示了Prolog在解决逻辑谜题方面的强大能力。文章最后作者认为，此类谜题并非教授编程的最佳方式，更倾向于具有实际应用的例子。

---

## 44. Google Cloud全新C4D虚拟机凭借AMD EPYC Turin提供卓越性能

**原文标题**: Google Cloud's New C4D VMs Deliver Remarkable Performance with AMD EPYC Turin

**原文链接**: [https://www.phoronix.com/review/google-c4d-amd-epyc-turin](https://www.phoronix.com/review/google-c4d-amd-epyc-turin)

Phoronix文章详述了谷歌云全新C4D虚拟机(VM)的初始性能基准测试，该虚拟机由AMD的EPYC 9005 "Turin"处理器驱动。谷歌旨在将这些实例用于如Web服务器、数据库、机器学习和视频流等高要求工作负载。

即使测试实例之间存在轻微的vCPU数量差异，C4D实例也比上一代C3D实例提供了显著的性能改进。C4D虚拟机可扩展至384个vCPU和3TB的RAM。驱动这些虚拟机的EPYC Turin处理器的关键特性包括Zen 5内核、具有完整512位数据路径的AVX-512支持以及DDR5-6000/6400内存支持。谷歌为Phoronix提供了对C4D和C3D实例的早期访问权限以进行基准测试。

测试是使用带有Linux 6.8内核和GCC 13.3编译器的Ubuntu 24.04 LTS进行的。文章展示了来自c4d-standard-32和c4d-standard-64实例的基准测试，并与c3d-standard-30和c3d-standard-60进行了比较。后续文章将以顶级c4d-standard-384实例的基准测试为特色。本文重点关注从C3D到C4D实例的性能提升，不涉及跨云比较或Intel Xeon测试。截至撰写本文时，C4D实例的定价信息尚不可用。文章结构分为多个页面，展示了各种工作负载，包括HPC、视频编码、数据库、AI和Web服务器性能。

---

## 45. DIY实验反应器利用伯克兰-艾德法

**原文标题**: DIY experimental reactor harnesses the Birkeland-Eyde process

**原文链接**: [https://blog.arduino.cc/2025/03/17/this-diy-experimental-reactor-harnesses-the-birkeland-eyde-process/](https://blog.arduino.cc/2025/03/17/this-diy-experimental-reactor-harnesses-the-birkeland-eyde-process/)

公民科学家Marb自制实验反应器探索伯克兰-艾德法：一种早期利用电弧从大气氮气生产硝酸的方法。虽然由于其高能量需求，该方法效率低下，并且在大型化肥生产中已基本过时，但Marb的重点在于对该过程本身的科学探索。

该项目使用Arduino UNO Rev3来控制反应器内的电弧。Arduino通过扩展板连接，管理着电极的功率流量，需要大量的电源、变压器和升压转换器。

该反应器还包含一个空气预处理系统，确保干燥空气通过装满干燥剂的管子泵入反应室。包括温度传感器在内的传感器向Arduino提供反馈，从而可以监控反应条件。

Marb在他的视频中演示了反应器的功能，但他仍在努力优化反应以获得更高的产量。他表示，如果人们对更详细的项目解释感兴趣，他愿意制作后续视频。该项目展示了一种动手实践的方式来理解历史工业过程，并利用Arduino技术进行控制和监控。

---

## 46. 首个开源MRI扫描仪 OSI² ONE (2023) 发布

**原文标题**: First open-source MRI scanner presented: the OSI² ONE (2023)

**原文链接**: [https://www.opensourceimaging.org/2023/01/09/first-open-source-mri-scanner-presented-the-osii-one/](https://www.opensourceimaging.org/2023/01/09/first-open-source-mri-scanner-presented-the-osii-one/)

2023年1月，首台开源MRI扫描仪OSI² ONE问世，标志着可及医疗技术领域的一个重要里程碑。该设备于2022年宣布，并在ISMRM活动中展示了原型。目前，在莱顿（荷兰）、姆巴拉拉（乌干达）和柏林（德国）存在三个完全正常运行的副本，并且计划增加更多副本。

OSI² ONE主要采用开源硬件和软件构建，材料成本约为20,000欧元。它可以对头部和四肢进行成像，利用通过标准CNC和3D打印手动构建的永磁体产生的约50 mT静态磁场。

该扫描仪的成像能力已通过使用3D TSE序列（2x2x3mm³分辨率，6分钟采集时间）获取的体模和体内人头图像得到验证。

目前正在进行的优化工作重点是提高图像质量，并创建全面的文档，以促进其作为医疗设备的监管批准。这些文档旨在简化从研究原型到临床应用的过渡，不仅适用于OSI² ONE，也适用于其他开源和专有项目。该项目旨在促进可持续的全球合作，使MRI技术更易于获取和透明。设计文件和文档可在GitLab上找到。

---

## 47. 将30万的阶乘分解为30万个大于10万的因子之积

**原文标题**: Decomposing factorial of 300K as the product of 300K factors larger than 100K

**原文链接**: [http://gus-massa.blogspot.com/2025/04/decomposing-factorial-of-300k-as.html](http://gus-massa.blogspot.com/2025/04/decomposing-factorial-of-300k-as.html)

本文详细介绍了一项将300,000!分解为300,000个大于100,000的因子的尝试，该尝试源于陶哲轩提出的挑战。作者使用Racket编程语言，并采用陶的方法，从一个“B”数（大于100,000的奇数的乘积）开始，然后使用“B-重”和“N!-重”的素数对其进行调整。B-重素数在B中出现的频率高于在300,000!中，而N!-重素数则相反。

该策略涉及将B-重素数替换为更大的N!-重素数，并乘以2的幂，以增加B的因子。作者旨在优化这种映射，尽量减少2的使用。

本文重现了陶哲轩最初将300,000!分解为大于90,000的因子的结果。然后，它探讨了平衡B和300,000!之间的素数的不同方法，特别是关注如何匹配来自两个因式分解的素数并分配必要的2的幂。提出了两种方法：“balance/inorder/first”和“balance/inorder/last”，它们的不同之处在于如何通过用1填充列表来处理素数计数中的差异。“balance/inorder/last”方法在最小化未使用的2方面证明更有效。作者还包括验证步骤，以确保生成的转换表的准确性。虽然在此摘录中并未明确达到100,000的阈值，但这项工作为进一步优化奠定了基础。

---

## 48. 巴西政府运营的支付系统已占据主导地位。

**原文标题**: Brazil's government-run payments system has become dominant

**原文链接**: [https://www.economist.com/the-americas/2025/04/03/brazils-government-run-payments-system-has-become-dominant](https://www.economist.com/the-americas/2025/04/03/brazils-government-run-payments-system-has-become-dominant)

巴西政府运营的数字支付系统Pix于2020年11月推出，迅速成为该国主导支付技术，超越了现金和银行卡。 Pix允许用户使用收款人的国民身份证、电话号码或二维码进行即时、免费且便捷的交易。由于其非接触式特性，其受欢迎程度在疫情期间激增。

到2024年，Pix已成为巴西最常用的支付方式，交易数量从2021年的90亿笔跃升至2024年的630亿笔，相当于转移了26万亿雷亚尔（4.5万亿美元）。 巴西对该系统的采用率在全球范围内是无与伦比的。 虽然Pix重振了巴西的银行业，但其主导地位赋予了巴西中央银行（BCB）相当大的权力。

---

## 49. 感谢HN：我6周前在这里发布的一款解谜游戏获得了《大西洋月刊》的授权

**原文标题**: Thank HN: The puzzle game I posted here 6 weeks ago got licensed by The Atlantic

**原文链接**: [https://www.theatlantic.com/games/bracket-city/](https://www.theatlantic.com/games/bracket-city/)

这篇“感谢 HN”帖文庆祝一项重大成就：作者的益智游戏，最初在 Hacker News (HN) 上分享六周后，已获得《大西洋月刊》的授权。 该帖文简短直接，主要用于宣告作者的成功，并提供该游戏的链接（现名为“Bracket City”），该游戏现已出现在《大西洋月刊》的网站上。 核心要点是，作者的游戏可能通过 HN 社区获得了最初的关注和可见性，并凭借其足够的吸引力被《大西洋月刊》这样的大型出版物选中，这代表着游戏开发者一项重大的职业成就。

---

## 50. 日本乡下小镇中年男子交易卡片走红

**原文标题**: Middle-aged man trading cards go viral in rural Japan town

**原文链接**: [https://www.tokyoweekender.com/entertainment/middle-aged-man-trading-cards-go-viral-in-japan/](https://www.tokyoweekender.com/entertainment/middle-aged-man-trading-cards-go-viral-in-japan/)

在日本河原这个乡村小镇，一款以当地西堂庄社区的中年男性（“大叔”）为主角的独特集换式卡牌游戏（TCG）在儿童中风靡一时。与典型的以奇幻角色或动漫英雄为主题的TCG不同，这款大叔TCG以本田先生（前消防队长，防火墙卡）和竹下先生（荞麦面制作教练，荞麦面大师卡）等当地人物为主角。

这款游戏由西堂庄社区委员会秘书长宫原绘里创作，旨在加强代际之间的联系。每张卡牌都以一位大叔为特色，并附有与其现实世界技能相关的统计数据、特殊能力和元素类型。例如，“防火墙”卡是一张火属性卡，具有“超级防御”技能。

最初的设计纯粹是为了收藏，但这款游戏后来演变成一种战斗形式，玩家可以使用大叔的技能来“战胜”对手。卡牌的稀有度与现实世界的社区参与度相关，更积极的志愿者会收到“闪亮”的升级卡牌。

这些卡牌是手工制作的，仅在西堂庄社区中心出售，每包售价100-500日元。该游戏成功地提高了儿童对当地活动的参与度，并培养了对老一辈的欣赏之情，孩子们甚至会向他们最喜欢的大叔索要签名。据报道，自游戏推出以来，社区活动的参与人数增加了一倍。

---

## 51. 美国机床工业的衰落与复苏前景 (1994)

**原文标题**: The Decline of the U.S. Machine-Tool Industry and Prospects for Recovery (1994)

**原文链接**: [https://www.rand.org/pubs/research_briefs/RB1500.html](https://www.rand.org/pubs/research_briefs/RB1500.html)

这份1994年兰德公司的研究简报探讨了美国机床工业的衰落及其复苏前景。它强调了机床在制造业中的关键作用，以及尽管率先采用了数控技术，该行业在20世纪80年代的衰落所引起的警惕。

该研究指出导致衰落的几个因素：国内需求下降，与日本公司相比对市场变化的反应迟缓，日本在数控技术和工艺创新（模块化生产）方面的优势，以及美元的高价值。

然而，1983-1992年间缺乏显著的反弹表明存在更深层次、更根本的问题。该行业难以适应快速的技术变革和日益激烈的全球竞争，面临着缺乏大型企业和小型企业之间的合作，难以获得用于现代化和出口销售的资金，熟练劳动力和培训不足，将研究转化为适销技术方面的表现不佳，国内需求不成熟以及出口能力薄弱等障碍。

尽管承认存在重大挑战，但由于内部重组，近期需求的激增，竞争对手国家的危机以及美国在新兴技术方面的领先地位，该报告提供了一定程度的乐观态度。该研究建议采取由三部分组成的政府战略：促进当地合作网络，增加对制造基础设施（研发和技能）的投资，以及通过简化出口程序和支持国际销售工作来帮助美国公司参与国际竞争。总体建议强调应更广泛地努力改进美国制造工艺技术。

---

## 52. AI编码强制要求正将开发者逼到崩溃边缘

**原文标题**: AI coding mandates are driving developers to the brink

**原文链接**: [https://leaddev.com/culture/ai-coding-mandates-are-driving-developers-to-the-brink](https://leaddev.com/culture/ai-coding-mandates-are-driving-developers-to-the-brink)

Sage Lazzaro文章《AI编码强制令正将开发者逼至崩溃边缘》探讨了软件开发者因AI编码工具强制推行不力而日益增长的挫败感。尽管高管们认为AI应用进展顺利，但开发者们常常发现这些工具引入错误、增加技术债务，并需要大量的调试。

采用AI的压力源于提高效率、加快交付以及通过减少开发者数量来节省潜在成本的承诺。然而，开发者报告称，AI工具经常建议不正确的代码、删除现有代码并导致部署问题。在Harness的一项调查中，大多数受访者报告在使用AI工具进行部署时出现问题，并增加了调试AI生成的代码所花费的时间。

该文章强调了高管和开发者之间的脱节，领导者制定AI使用指标，却不了解其对工作流程的影响。一些公司甚至公开个人AI生成的代码输出量，造成了对数量而非质量的压力。

ChargeLab的做法，即工程师有权选择最适合他们的AI工具，是一个积极的例子。这培养了一种创新和协作的文化，据报告可提高40%的生产力。文章总结说，成功采用AI需要了解开发者的需求、培养信任，并将质量放在首位，而不是仅仅强制使用AI。

---

## 53. 解析组合学——一个实例分析

**原文标题**: Analytic Combinatorics – A Worked Example

**原文链接**: [https://grossack.site/2025/04/08/analytic-combinatorics-example.html](https://grossack.site/2025/04/08/analytic-combinatorics-example.html)

这篇博文探讨了解析组合学，特别是奇点分析，在解决与三叉树相关的计数问题中的应用。作者首先进行了一个热身：计算有根有序三叉树。他们推导出了生成函数的一个泛函方程，使用奇点分析逼近了这种树的数量，并通过绘图和与已知序列的比较证明了逼近的准确性。这个过程的关键是找到生成函数的主导奇点并获得其周围的 Puiseux 级数展开式。

然后，文章解决了主要问题：计算同构意义下的无序有根三叉树。引入 Pólya-Redfield 计数来推导这种情况下生成函数的泛函方程。作者将奇点分析方法扩展到仅是全纯而不是多项式的函数，以逼近无序树的数量。这涉及数值求解方程组，以找到奇点和 Puiseux 级数的系数。提供了 Sage 代码片段来说明如何执行这些计算并验证由此产生的渐近近似。最后，提出了一个有趣的练习，供读者将分析扩展到循环有根三叉树，并与已知结果进行比较。

---

## 54. Netflix 如何准确归因 eBPF 流日志

**原文标题**: How Netflix Accurately Attributes eBPF Flow Logs

**原文链接**: [https://netflixtechblog.com/how-netflix-accurately-attributes-ebpf-flow-logs-afe6d644a3bc](https://netflixtechblog.com/how-netflix-accurately-attributes-ebpf-flow-logs-afe6d644a3bc)

Netflix技术博客文章《Netflix如何准确归因eBPF流日志》摘要：

该文章介绍了Netflix如何使用eBPF（扩展伯克利包过滤）流日志来深入了解其服务网格内的网络流量，从而能够解决性能问题并优化其基础设施。他们解决的关键挑战是准确地将网络流归因于特定的应用程序和请求，尤其是在容器内运行的动态和短暂的微服务环境中。

问题的根源在于容器ID和进程ID（PID）可能会快速变化，这使得传统的将网络连接映射到应用程序的方法变得不可靠。他们的解决方案涉及多种技术的结合，以将eBPF捕获的网络流与应用程序级别的上下文相关联：

1. **上下文传播:** 他们利用HTTP头（例如`X-Request-ID`）跨服务边界传播请求上下文。这使他们能够跟踪请求在不同微服务之间传递的过程。

2. **eBPF Instrumentation:** 使用eBPF程序捕获网络流数据，包括源和目标IP/端口，以及与连接关联的容器ID和PID。

3. **关联引擎:** 他们构建了一个关联引擎，该引擎使用来自容器编排系统（如Kubernetes）和传播的请求ID的信息，将容器ID和PID映射到应用程序级别的上下文。 该引擎会随着容器的启动、停止和重新调度不断更新其映射。

4. **数据丰富:** 最后，他们使用相关的应用程序上下文（例如服务名称、请求ID和其他相关元数据）来丰富流日志。

即使面对动态基础设施，这种方法也使Netflix能够准确地将网络流归因于特定的请求和应用程序。 生成的流日志提供了对网络性能、依赖关系映射和潜在瓶颈的宝贵见解，从而可以更快、更有效地进行故障排除和优化。

---

## 55. 如何通过啄木声识别啄木鸟

**原文标题**: How to Recognize Woodpeckers by Their Drumming Sounds

**原文链接**: [https://www.allaboutbirds.org/news/how-to-recognize-woodpeckers-by-their-drumming-sounds/](https://www.allaboutbirds.org/news/how-to-recognize-woodpeckers-by-their-drumming-sounds/)

通过啄木鸟独特的鼓声识别不同种类

---

## 56. Tailscale 融资 1.6 亿美元

**原文标题**: Tailscale has raised $160M

**原文链接**: [https://tailscale.com/blog/series-c](https://tailscale.com/blog/series-c)

Tailscale 完成 1.6 亿美元 C 轮融资，Accel 领投，CRV、Insight Partners、Heavybit、Uncork Capital、George Kurtz (Crowdstrike CEO) 和 Anthony Casalena (Squarespace CEO) 等新老投资者参投。

Tailscale 成立于 2019 年，旨在简化网络连接，通过消除复杂配置的需求，使网络对用户而言几乎隐形。目前，数百万人使用 Tailscale 来满足各种需求，从家庭实验室到企业人工智能工作负载。

这笔资金将用于加速 Tailscale “身份优先网络” 的愿景，重点在于消除摩擦、高效扩展网络，并将身份而非 IP 地址作为安全连接的核心。该公司认为这至关重要，因为最初的互联网架构是基于位置的，需要后续的安全层（如 VPN 和防火墙）。

该公司看到了日益增长的需求，尤其是在人工智能行业，各公司都在努力连接跨云 GPU 并保护工作负载。领先的人工智能公司已经在使用 Tailscale。这笔资金将支持 Tailscale 不断壮大的工程和产品团队，其对免费客户的免费支持承诺，以及向后兼容性。他们希望确保网络对从初创公司到大型企业的每个人都“开箱即用”。

---

## 57. 范式 (YC W24) 正在旧金山招聘创始工程师

**原文标题**: Paradigm (YC W24) Hiring Founding Engineers in SF

**原文链接**: [https://www.ycombinator.com/companies/paradigm/jobs/nFNWweP-founding-engineer](https://www.ycombinator.com/companies/paradigm/jobs/nFNWweP-founding-engineer)

Paradigm (Y Combinator W24投资的旧金山初创公司) 诚聘创始工程师，共同打造其原生AI工作空间。该职位提供15万至25万美元的年薪、丰厚的股权以及其他福利。理想的候选人是一位经验丰富的通才，对人工智能充满热情，追求速度，并能在快节奏的环境中工作。要求每周5-6天线下办公。

关键资质包括构建生产级AI产品的经验、对速度和规模的执着、在模糊环境中蓬勃发展的能力以及卓越成就的历史。 拥有GoLang、TypeScript、NextJS、Redis、RAG系统和代理架构的经验者优先。 职责包括全栈开发、用户互动、功能实现和塑造产品路线图。

Paradigm是一个利用人工智能的全新工作空间，由Dropbox、Intercom和Langchain等公司的杰出构建者/运营者提供支持。 该团队规模小，由来自谷歌、麻省理工学院和微软等公司的经验丰富的构建者组成。 他们正在寻找一位才华横溢的人才来为他们的愿景做出贡献。

---

## 58. Show HN: Coroot – 基于 eBPF 的开源可观测性，提供可执行的洞察

**原文标题**: Show HN: Coroot – eBPF-based, open source observability with actionable insights

**原文链接**: [https://github.com/coroot/coroot](https://github.com/coroot/coroot)

Coroot 是一个开源可观测性平台，利用 eBPF 实现零侵入式数据采集，将原始指标、日志和链路转换为可执行的洞察。它提供全面的服务地图，无需任何代码修改，覆盖系统 100% 的范围。主要功能包括自动应用程序健康状况摘要、SLO 跟踪、使用分布式追踪进行异常请求探索以及一键式异常调查。

Coroot 通过 OpenTelemetry 提供厂商中立的检测，从而可以洞察旧有或第三方服务，并提供开箱即用的日志模式聚类以及通过 ClickHouse 实现闪电般快速搜索的无缝日志到链路关联。它允许一键分析应用程序，将资源使用情况精确定位到特定的代码行，并将其与基线行为进行比较。

Coroot 自动识别超过 80% 的常见问题，并在应用程序未达到其 SLO 时触发单个、全面的警报。部署跟踪也是一个核心功能，可在 Kubernetes 中监控应用程序发布，无需 CI/CD 管道集成，比较版本，并通过集成的 AWS、GCP 和 Azure 成本监控跟踪成本影响。成本监控无需云帐户访问权限。

Coroot 可以作为 Docker 容器运行，也可以部署到任何 Kubernetes 集群中。文档、实时演示和社区支持可通过 Slack、GitHub 和 Twitter 轻松获得。它采用 Apache License 2.0 许可。

---

## 59. PDP-11/Hack 豪华版

**原文标题**: PDP-11/Hack de luxe

**原文链接**: [https://forum.vcfed.org/index.php?threads/pdp-11-hack-de-luxe.1252532/](https://forum.vcfed.org/index.php?threads/pdp-11-hack-de-luxe.1252532/)

Peter (cbscpe) 设计并制造了一款“PDP-11/Hack de luxe”，这是一个基于 DCJ11 处理器的 Eurocard 单板计算机 (SBC)。由于对之前的面包板版本不满意，并希望更深入地了解 DCJ11，他在 PCB 上创建了一个更强大的设计，带有一个扩展槽。

组装好的原型（照片见帖子）需要进行一个小小的工程变更单 (ECO)。连接到控制台的 USB 转串口/TTL 适配器为 SBC 提供串行通信和电源，SBC 的功耗低于 200mA。

使用真正的 DC319 UART 进行串行通信。该设计优先使用通孔 (TH) 组件，仅将表面贴装器件 (SMD) 用于电容器和电阻器。整个系统采用标准 TTL 逻辑。

主要功能包括正确的字节写入解码、上电解码、用于定义上电配置的 74HCT541，以及带有按钮和逻辑的复位功能。该 SBC 成功运行了标准的 PDP-11/Hack 测试程序。

---

## 60. 高关税在19世纪没有让美国富裕，这次也不会。

**原文标题**: High tariffs didn't make the U.S. rich in the 19th century. They won't this time

**原文链接**: [https://www.economicforces.xyz/p/high-tariffs-didnt-make-the-us-rich](https://www.economicforces.xyz/p/high-tariffs-didnt-make-the-us-rich)

布莱恩·阿尔布雷希特的文章《高关税在19世纪没有让美国富裕，这次也不会》挑战了这样一种观点，即高关税推动了19世纪美国的工业崛起，因此今天也能奏效。该文章考察了从美国内战到第一次世界大战期间，美国实行高关税并经历了快速经济增长的历史时期。

虽然承认19世纪末美国以及德国等其他国家的高关税与经济增长之间存在相关性，但作者认为相关性不等于因果关系。该文章强调了将关税的影响与其他因素（如人口增长、移民、技术创新和丰富的自然资源）的影响区分开来的难度。

阿尔布雷希特强调了使用反事实的重要性——评估没有关税会发生什么——以确定它们的真正影响。他指出，将受保护部门与未受保护部门的增长进行比较的行业层面研究、涉及关税突然变化的自然实验以及反事实建模是更为严谨的方法。克莱因和梅斯纳的研究，将行业关税与制造业产出和生产率联系起来，被认为是特别有见地的。

中心论点是，声称关税导致美国繁荣的简单化论点缺乏建立因果联系所需的经济分析，因此，历史证据不足以支持今天实施关税。

---

## 61. 建造 System/360 大型机差点毁了 IBM

**原文标题**: Building the System/360 Mainframe Nearly Destroyed IBM

**原文链接**: [https://spectrum.ieee.org/building-the-system360-mainframe-nearly-destroyed-ibm](https://spectrum.ieee.org/building-the-system360-mainframe-nearly-destroyed-ibm)

本文详细介绍了IBM于1964年System/360大型机的开发和发布，这款产品彻底改变了计算机行业，但也险些导致公司破产。在20世纪50年代末，IBM面临着危机：其广受欢迎的1401系统正变得过时，而升级到更大的系统需要昂贵的软件重写，这阻碍了增长。IBM自身也在与多个不兼容的产品线作斗争，推高了研发成本并削弱了竞争力。

T. Vincent Learson受命解决这个问题，他积极推动建立一个统一的、兼容的系统，克服了恩迪科特和波基普西工程团队之间的内部竞争。“SPREAD”特别工作组，由John W. Haanstra和Bob O. Evans领导，提出了一个由五个兼容计算机组成的系列，具有标准接口。这意味着客户只需重写一次软件即可迁移到新系统。最后一刻的微代码突破使得较小的S/360型号能够运行现有的1401软件，进一步缓解了过渡。

该项目风险巨大，耗资IBM 50亿美元，并需要雇用7万名新员工。硬件和软件开发的规模是前所未有的。1964年4月7日的发布会包括推出150种新产品，包括六台计算机和44种外围设备。System/360的兼容性是其核心特征，允许客户在不更换软件或外围设备的情况下进行升级。尽管面临巨大的挑战和IBM内部的“部落战争”，System/360最终被证明是巨大的成功，在第一个月就售出了超过10万套系统，巩固了IBM在计算机行业的统治地位。

---

## 62. 高关税在19世纪没有使美国富裕，这次也不会。

**原文标题**: High tariffs didn't make the U.S. rich in the 19th century. They won't this time

**原文链接**: [https://www.economicforces.xyz/p/high-tariffs-didnt-make-the-us-rich](https://www.economicforces.xyz/p/high-tariffs-didnt-make-the-us-rich)

布莱恩·阿尔布雷希特的文章《高关税并未使19世纪的美国致富，这次也不会》挑战了一种流行的观点，即高关税推动了19世纪美国的工业崛起。作者认为，尽管美国在19世纪后期在高关税下经历了快速的经济增长，但最近的研究表明，关税很可能对这种增长是偶然的，甚至是有害的。

阿尔布雷希特承认，高关税和快速增长在美国和德国同时出现，这与英国在自由贸易下的较慢增长形成对比。然而，他强调，相关性并不等于因果关系。他引用研究表明，观察到的相关性可能是由于反向因果关系（工业增长导致关税）、遗漏变量（如巨大的国内市场和国家建设）或构成效应（对制成品的关税与大宗商品繁荣同时发生）。

作者强调了反事实分析在确定关税因果影响方面的重要性。他批评了仅依靠关税和增长在时间上的巧合的论点，主张采用严格的方法来分离因果效应，例如使用行业层面的研究、自然实验和反事实建模。他强调了Klein和Meissner的行业层面研究，该研究比较了受保护和未受保护部门的业绩，这是一种更可靠的方法来理解关税的真正影响。

---

## 63. 难民营揭示的经济学

**原文标题**: What a refugee camp reveals about economics

**原文链接**: [https://www.economist.com/finance-and-economics/2025/04/03/what-a-refugee-camp-reveals-about-economics](https://www.economist.com/finance-and-economics/2025/04/03/what-a-refugee-camp-reveals-about-economics)

文章《难民营揭示了怎样的经济学》探讨了马拉维的扎莱卡难民营内的经济动态，该难民营自1994年以来一直收容难民。虽然扎莱卡的生活表面上看起来很正常，有教堂、商店和社交活动，但一个关键的区别在于，大多数居民并没有传统意义上的工作。

中心前提围绕着对扎莱卡每个人每月收到9美元的观察。这种持续的资金流入使得难民营内部存在一个能够运作的经济体，正如文章所指出的，在难民营内常见到看起来正常的教堂和酒吧。

文章以人们参加难民营内的教堂和体育赛事为例，与经济现实形成对比，指出难民营内的难民不像大多数人那样工作。

根据标题，作者似乎希望深入研究这种持续的现金流在难民营内促成的经济和社会活动。

---

## 64. NNN：营销组合建模的下一代神经网络

**原文标题**: NNN: Next-Generation Neural Networks for Marketing Mix Modeling

**原文链接**: [https://arxiv.org/abs/2504.06212](https://arxiv.org/abs/2504.06212)

这篇arXiv论文，题为“NNN：用于营销组合建模的下一代神经网络”，介绍了一种使用基于Transformer的神经网络进行MMM的新方法。由Thomas Mulc领导的作者们通过利用丰富的嵌入来捕捉营销渠道的定量和定性方面，从而解决了传统MMM方法的局限性。

与依赖于标量输入和参数衰减函数的传统方法不同，NNN利用注意力机制，使其能够对复杂的交互进行建模，捕捉长期影响，并有可能提高销售归因的准确性。该论文强调，即使在数据受限的环境中，L1正则化的使用也允许表达能力强的模型使用。

作者通过对模拟数据和真实数据的评估证明了NNN的有效性，表明其在预测能力方面有显著提高。除了归因之外，NNN还通过模型探测提供有价值的见解，从而可以评估关键词或创意的有效性，进而增强模型的可解释性。

该论文归类于机器学习（cs.LG）和应用（stat.AP）类别。提交日期为2025年4月8日。作者已提供PDF和实验性HTML格式的论文以及TeX源代码。

---

## 65. 中国去美元化：中国推出1.2万亿美元数字人民币系统 [视频]

**原文标题**: China Is De-Dollarizing: China Launches $1.2T Digital Yuan System [video]

**原文链接**: [https://www.youtube.com/watch?v=KX_Id7J2Ee0](https://www.youtube.com/watch?v=KX_Id7J2Ee0)

提供的内容并非文章，而是YouTube页脚的一部分，包含版权信息、广告、服务条款、隐私政策以及其他标准YouTube免责声明的链接。它*不*包含关于中国去美元化或推出数字人民币系统的信息。因此，根据给定的文本，不可能对所谓的主题进行总结。提供的文本与标题无关。

---

## 66. 展示一下：我做了一个文字游戏。我的物理老师很喜欢。你觉得怎么样？

**原文标题**: Show HN: I built a word game. My Physics teacher likes it. What about you?

**原文链接**: [https://thypher.com/](https://thypher.com/)

这个“Show HN”帖子介绍了 Thypher，一个每日单词游戏，玩家必须破译方程式来找到一个五字母的单词。该游戏提供数学方程式，例如 `mc^2 = E`，来代表字母（不区分大小写）。玩家需要解开这些方程式来揭示隐藏的单词。每天都有一个新单词可用。帖子强调了游戏的简单性，以及作者的物理老师喜欢这个游戏的事实，并邀请其他人尝试。示例显示，在 2025 年 4 月 9 日，它是第 48 号游戏。该帖子提供了清晰的玩法说明，强调了解方程以发现字母的核心机制。

---

## 67. 没有大象：图像生成技术的突破

**原文标题**: No elephants: Breakthroughs in image generation

**原文链接**: [https://www.oneusefulthing.org/p/no-elephants-breakthroughs-in-image](https://www.oneusefulthing.org/p/no-elephants-breakthroughs-in-image)

Ethan Mollick 的文章《无大象：图像生成领域的突破》讨论了人工智能图像生成领域的重大进展，尤其是在谷歌和 OpenAI 推出多模态模型之后。这些模型不同于以往依赖于由人工智能生成的文本提示触发的独立图像生成工具的系统，而是像大型语言模型生成文本一样，直接逐个 token 地创建图像。这使得图像创建更加智能和精确，解决了早期人工智能图像生成中出现的文本扭曲和随机元素等问题。

Mollick 强调了使用清晰的指示和迭代反馈来提示这些模型的能力，就像基于文本的人工智能一样，从而使用户能够指导图像创建过程。他提供了 GPT-4o 如何用于生成信息图、创建变体，甚至根据特定请求（例如改变光照或在照片之间交换对象）来操纵图像的例子。

文章探讨了这些进步的潜在应用，包括创建网站模型、广告概念、可视化食谱和视频游戏纹理。 Mollick 还讨论了围绕人工智能生成艺术的复杂性和伦理问题，例如版权问题、艺术家风格的复制以及深度伪造和其他视觉幻觉的可能性。

总而言之，文章强调，虽然多模态人工智能在视觉创作方面提供了强大的新功能，但也引发了关于创意所有权、真实性的重要问题，以及需要周全的框架来驾驭不断发展的视觉媒体领域。 人类和人工智能创作之间的界限正在模糊，因此有必要重新思考原创性，在一个任何人都可以通过提示生成复杂视觉效果的世界中。

---

## 68. Show HN: 约500行代码实现的向量嵌入HNSW索引

**原文标题**: Show HN: HNSW index for vector embeddings in approx 500 LOC

**原文链接**: [https://github.com/dicroce/hnsw](https://github.com/dicroce/hnsw)

此“Show HN”帖子介绍了一个用 C++ 实现的分层可导航小世界 (HNSW) 算法，用于在向量嵌入中进行高效的最近邻搜索。该实现轻量级，包含在单个头文件中，并且拥有大约 500 行现代 C++ 代码。它利用 Eigen 进行距离计算中的 SIMD 加速，从而保证快速性能。

该帖子将 HNSW 解释为一种分层图结构，节点连接到每层中的附近节点。较高层人口更稀疏。插入涉及随机选择一个级别，并将节点添加到该级别及其以下所有级别。搜索从顶层开始，找到最近的节点，然后下降到各个级别，在越来越密集的层中细化搜索。搜索会维护遇到的 K 个最近邻居的记录。

该帖子提供了一个简洁的代码示例，演示了如何创建 HNSW 索引、添加向量嵌入以及执行最近邻搜索。还包括使用 CMake 的编译说明。该实现旨在为在高维向量空间中查找最近邻居提供一种实用且高效的解决方案。

---

## 69. 细胞正在交换线粒体。这对我们的健康意味着什么？

**原文标题**: Cells are swapping their mitochondria. What does this mean for our health?

**原文链接**: [https://www.nature.com/articles/d41586-025-01064-5](https://www.nature.com/articles/d41586-025-01064-5)

这篇《自然》杂志的文章探讨了一项突破性研究，该研究挑战了线粒体是静态细胞器并局限于细胞内的传统观点。 新出现的证据表明，线粒体是可移动的，能够通过一种称为“线粒体转移”的过程在细胞之间转移。

研究人员已经在各种生物和细胞类型中观察到这种转移，暗示其具有多种功能。 尽管这种移动性的确切原因仍在调查中，但研究表明，细胞可能会在需要时将线粒体捐赠给邻近细胞，从而可能有助于组织修复、免疫反应或拯救受损细胞。 相反，线粒体转移也可能是癌细胞利用的一种武器。

尽管令人兴奋，但研究人员尚未在人体内直接观察到这一过程，因此线粒体转移在人类健康中的程度和影响仍然是个谜。 然而，科学家们已经开始探索利用这种现象进行治疗的可能性，例如治疗癌症和中风。

线粒体具有古老的细菌起源，现在被认为不仅仅是能量动力源。 它们在细胞通讯、免疫反应中发挥着关键作用，甚至在细胞内表现出意想不到的多样性。 线粒体转移可能是日常生物学的重要组成部分。 最近的研究表明，它可能通过帮助维持保护性膜屏蔽来在维持健康组织方面发挥作用。

---

## 70. 现代史上最愚蠢的经济政策

**原文标题**: The Dumbest Economic Policy in Modern History

**原文链接**: [https://www.theatlantic.com/economy/archive/2025/04/economic-policy-trump-tariffs/682369/](https://www.theatlantic.com/economy/archive/2025/04/economic-policy-trump-tariffs/682369/)

德里克·汤普森的文章认为，唐纳德·特朗普的经济政策，特别是他对关税的处理方式，对美国经济和制造业（他旨在振兴的行业）是有害的。作者用重建破旧房屋的比喻来说明特朗普的政策具有破坏性，就像放火烧家具和砸碎窗户，而不是建设性的。

汤普森承认需要解决美国制造业的衰落问题，并提出了替代策略，如公共补贴、与盟友合作以及明确的贸易规则，类似于《芯片与科学法案》。然而，他批评特朗普的行为，例如对墨西哥和加拿大征收关税、威胁吞并加拿大、对欧洲国家征收关税以及在金融市场制造不确定性，都是适得其反的。

这篇文章强调了这些关税对制造企业的负面影响，包括供应链中断、成本增加以及潜在的失业。它还驳斥了关税旨在降低利率的说法，指出美国国债收益率实际上已经上升。最终，汤普森得出结论，特朗普的政策正在损害美国制造商并扰乱金融体系，本质上是在拯救经济的幌子下对经济造成内部破坏。他担心如果特朗普真的想要摧毁经济会造成的后果。

---

## 71. Show HN: Badgeify – 将任何应用添加到你的Mac菜单栏

**原文标题**: Show HN: Badgeify – Add Any App to Your Mac Menu Bar

**原文链接**: [https://badgeify.app/](https://badgeify.app/)

本文旨在解决新款MacBook上Mac菜单栏图标被刘海遮挡的问题。它为遇到这个令人沮丧问题的用户提供解决方案，旨在使所有重要图标可见且易于访问。

文章涵盖了各种方法，从可能有助于图标放置和排列的内置macOS修复，到专门用于管理和自定义菜单栏的更全面的第三方工具。 这些工具可以提供高级功能来优化菜单栏布局，并确保所有图标保持可见，即使有刘海。

本质上，本文旨在成为寻求重新控制其菜单栏并防止图标被刘海遮挡的用户资源，从而改善他们的整体Mac体验。

---

## 72. 压倒性的负面和士气低落的力量

**原文标题**: An Overwhelmingly Negative and Demoralizing Force

**原文链接**: [https://aftermath.site/ai-video-game-development-art-vibe-coding-midjourney](https://aftermath.site/ai-video-game-development-art-vibe-coding-midjourney)

人工智能应用对游戏开发者工作生活产生的负面影响
开发者访谈表达了对强行使用人工智能的不满，这往往违背了他们的意愿和专业知识。

主要担忧包括：

*   **艺术完整性与创作过程：** 艺术总监过度依赖人工智能进行艺术指导，扼杀了创造力以及对优秀游戏设计至关重要的迭代过程。人工智能生成的艺术品被用于给投资者留下深刻印象，而不是真正地为游戏愿景提供信息。
*   **软件开发效率低下：** 开发者被迫使用ChatGPT和Claude等人工智能工具生成代码，这导致积极性降低，代码质量下降，难以集成和理解。人工智能生成的代码缺乏必要的上下文和意图。
*   **工作保障与专业知识受损：** 开发者感到他们的专业知识被低估，因为人工智能被视为一种快速解决方案，导致他们认为人工智能将会取代他们。
*   **伦理问题：** 人工智能的使用引发了伦理问题，尤其是在抄袭以及未经语音演员同意，使用其声音生成人工智能对白方面。

文章强调，强行整合人工智能通常是出于节省时间和金钱的考虑，却忽视了对创造力、质量和开发者整体福祉的有害影响。受访者认为，人工智能的推动者试图修复一些没有损坏的东西，并忽略了人类创造力和协作在游戏开发中的根本价值。

---

## 73. 中国或将重创美国房地产市场

**原文标题**: China could crush the U.S. housing market

**原文链接**: [https://www.cnbc.com/2025/04/09/how-china-could-crush-the-us-housing-market.html](https://www.cnbc.com/2025/04/09/how-china-could-crush-the-us-housing-market.html)

CNBC文章讨论了中国可能因美国贸易政策而抛售美国抵押贷款支持证券(MBS)，从而对美国房地产市场产生负面影响的可能性。外国持有美国MBS的重要份额（15%），而中国是主要参与者。

文章强调，中国已经开始减少其MBS持有量。中国和日本等其他主要持有者的进一步加速抛售可能会推高抵押贷款利率。这是因为出售MBS会扩大抵押贷款利差，增加购房者的借贷成本。

不断上涨的抵押贷款利率将进一步削弱本已步履维艰的春季房地产市场，该市场正面临着高房价、消费者信心下降和股市波动等挑战。文章强调，潜在购房者已经对他们的财务状况感到担忧，更高的抵押贷款利率可能会进一步阻止他们。

更糟糕的是，美联储也在减少其MBS投资组合，从而加剧了抵押贷款利率的潜在上行压力。外国抛售和美联储行动的综合影响可能会严重扰乱房地产市场。

---

## 74. 神经涂鸦 - 大语言模型的液态记忆层

**原文标题**: Neural Graffiti – Liquid Memory Layer for LLMs

**原文链接**: [https://github.com/babycommando/neuralgraffiti](https://github.com/babycommando/neuralgraffiti)

神经涂鸦：一种无需微调即可为大语言模型注入实时上下文感知记忆的“喷涂层”。该实验性层受神经可塑性和涂鸦艺术启发，通过微妙影响模型的向量嵌入来改变模型的行为，从而影响其内部关联词语和概念的方式。

喷涂层的工作原理是将记忆痕迹“喷涂”到 Transformer 推理的最后阶段。该痕迹随着交互而演变，导致基于过去上下文的渐进式行为漂移。虽然它不能保证特定的词语输出，但它鼓励模型倾向于某些概念，从而随着时间的推移塑造其语气和方向。用户可以跟踪该层对每个输出的影响。

该项目的目标是使AI模型能够发展出更积极的行为，通过用过去的经验“标记”他们的模型来积累个性和增强好奇心。它从液态神经网络中汲取灵感，但通过将记忆层集成到现有的基于Transformer的模型中，提供了一种更实用的方法。

作者警告说，使用神经涂鸦可能会将模型变成具有独特精神世界的独立“实体”，可能使其不适合某些商业应用。相反，它被设想为一种创建数字角色的工具，这些角色可以通过记住他们的互动并相应地塑造他们的反应来发展某种形式的自我意识。最终，这是一种专注于探索AI行为修改的实验性技术。

---

## 75. 展示HN：音景和Lofi播放器

**原文标题**: Show HN: Soundscapes and Lofi Player

**原文链接**: [https://www.noisefill.com/](https://www.noisefill.com/)

“Show HN：声景与Lo-fi播放器”提交介绍了一个名为Noisefill的Web应用，该应用被描述为声景与Lo-fi播放器。该应用很可能为用户提供环境音效和Lo-fi音乐，用于集中注意力、放松或其他用途。简短的内容表明该应用使用JavaScript构建，并且需要在用户的浏览器中启用JavaScript才能运行。

---

## 76. 展示一下：我也做了一个文字游戏。我妈没啥感觉，但我自己觉得挺酷的。

**原文标题**: Show HN: I also built a word game. My mom is indifferent, but I think its ccool

**原文链接**: [https://playletterlinks.com/](https://playletterlinks.com/)

这个“Show HN”帖子介绍 LetterLinks，一款受拼字游戏 Scrabble 启发的每日单词构建游戏。作者对此感到兴奋，尽管他们的母亲对此漠不关心。该游戏提供每日挑战，玩家使用一组字母方块在游戏板上创建单词。

主要功能包括：

*   **玩法：** 玩家拖动或点击方块，将它们放置在棋盘上，水平或垂直地组成单词。
*   **计分：** 根据字母值和特殊方格（如双/三字母 (DL/TL) 和双/三词 (DW/TW)）获得积分。特殊方块包括百搭牌（代表任何字母）和奖励牌（使单词得分加倍）。
*   **约束：** 必须使用中心星形方格，单词必须连接，并且只有有效的字典单词才有效。单词至少需要 2 个字母长。
*   **每日挑战：** 每天每个人都获得相同的字母，每日奖励挑战涉及特定的单词模式以获得额外的积分。水平和垂直乘数增加了额外的策略层。
*   **教程：** 游戏包含解释游戏玩法、计分和特殊功能的教程。
*   **进度：** 技能等级反映了基于分数的进度。
*   **排行榜：** 玩家可以提交他们的分数，并在每日排行榜上与其他人比较。
*   **统计和成就：** 您的统计数据和成就将被跟踪和显示。
*   **分享：** 玩家可以分享他们的分数。

---

## 77. 你的ext4文件系统中文件的顺序无关紧要。

**原文标题**: The order of files in your ext4 filesystem does not matter

**原文链接**: [https://thewisenerd.com/blog/ext4-readdir/](https://thewisenerd.com/blog/ext4-readdir/)

一次由节点镜像补丁更新引发的JVM应用行为异常调试历程：罪魁祸首是Classpath中的JAR文件顺序，JVM通过`readdir`系统调用从通配符展开Classpath，而`readdir`在ext4文件系统上的顺序受到“目录哈希种子”的影响。

---

## 78. 90年代密码朋克邮件列表的十万封邮件

**原文标题**: 100k emails from the 90s Cypherpunk listserve

**原文链接**: [https://cypherpunk.timespan.vc/](https://cypherpunk.timespan.vc/)

本文收录了来自 20 世纪 90 年代赛博朋克邮件列表的 10 万封邮件。赛博朋克是一群关注数字时代隐私和安全的行动者和思想家。他们倡导使用密码学来保护个人自由并挑战中心化权力。

这份档案的意义在于其历史价值。它让我们得以一窥互联网的早期发展以及围绕着当今仍然高度相关的问题的知识激荡，例如：

*   **隐私：** 赛博朋克们预见到了政府和企业日益增长的监控对隐私构成的威胁。
*   **密码学：** 他们倡导使用强大的加密技术作为保护隐私和实现安全通信的工具。
*   **去中心化：** 他们相信去中心化的系统和技术是限制中心化机构权力的途径。
*   **言论自由：** 他们认为保护在线言论自由和抵制审查至关重要。

该邮件列表的讨论涵盖了广泛的主题，包括密码学、数字货币、匿名以及技术的法律和政治影响。 考察这些邮件可以深入了解塑造当今互联网的许多思想和技术的起源，包括加密货币和安全消息应用程序。 该合集是研究人员、历史学家以及任何有兴趣了解数字自由运动根源的人的宝贵资源。

---

## 79. I, II 或 III 级肥胖与健康结果之间的关联

**原文标题**: Associations Between Class I, II, or III Obesity and Health Outcomes

**原文链接**: [https://evidence.nejm.org/doi/10.1056/EVIDoa2400229](https://evidence.nejm.org/doi/10.1056/EVIDoa2400229)

无法访问文章链接。

---

## 80. 为什么公司不修复漏洞

**原文标题**: Why Companies Don't Fix Bugs

**原文链接**: [https://idiallo.com/blog/companies-dont-fix-bugs](https://idiallo.com/blog/companies-dont-fix-bugs)

本文深入探讨了即使像Rockstar Games这样价值数十亿美元的巨头公司，也常常未能修复软件中看似明显的Bug的原因，并以独立程序员解决GTA Online长期存在的加载时间问题为例进行了说明。

作者认为，问题并非开发人员无能，而是源于公司优先事项和官僚主义的系统性问题。Bug修复，特别是那些与特定功能或需求没有直接关联的修复，会被归类为“技术债务”，并且由于开发人员更替、项目重点转移以及修改旧代码可能带来的意外后果等因素，常常在待办事项中被忽略。

核心问题在于，Bug修复通常缺乏像销售额或新功能发布那样容易衡量的、清晰直接的投资回报率（ROI）。公司优先考虑影响季度收益的指标，从而导致用户体验和用户好感的忽视。虽然成功的Bug修复可以产生积极的公关效应，但它们很少能解决导致Bug持续存在的根本性系统问题。

作者最后总结说，用户应该责怪的是系统，而不是开发人员，并强调官僚主义的惯性和以利润为导向的决策往往掩盖了用户体验和软件质量的重要性。本文通过一个设想的Bug单生命周期场景以及来自具有行业经验的读者的评论来佐证观点。

---

## 81. ClickHouse 中 Rust 的一年

**原文标题**: A year of Rust in ClickHouse

**原文链接**: [https://clickhouse.com/blog/rust](https://clickhouse.com/blog/rust)

Alexey Milovidov 详述了 ClickHouse 将 Rust 集成到 C++ 代码库中为期一年的实验。目标并非完全重写，而是启用使用 Rust 开发新组件，同时确保与现有 C++ 基础设施的无缝集成。

第一个项目涉及集成 BLAKE3 哈希函数，由一名本科生负责，展示了构建系统集成。后来，`clickhouse-client` 通过 Rust 的 `skim` 库得到了改进，用于交互式历史记录导航，尽管 BLAKE3 最终被 C++ LLVM 实现所取代。

PRQL（一种替代查询语言）的引入进一步验证了 Rust 集成。更重要的是，Delta Kernel（一个基于 Rust 的库，用于与 Delta Lake 交互）被纳入，以解决缺乏适用于数据湖格式的强大 C++ 实现的问题。这种集成突出了几个挑战：供应链管理、复杂包装器的创建、处理 Rust 的“panic”行为、确保清理器在两种语言中都能工作、交叉编译的复杂性、库链接问题以及管理符号大小。过长的符号名称导致二进制文件膨胀，需要紧急关注。

尽管存在问题，ClickHouse 仍欣然接受将 Rust 集成到其开发中。虽然互操作性需要警惕，但模糊测试器等工具已被证明有助于发现 Rust 库中的错误。剩下的一个障碍是确保 ClickHouse 内部的内存管理约定和外部存储连接与 Rust 库使用的约定之间的可组合性。

---

## 82. “氟化物降低智商”报告需撤回

**原文标题**: „Fluoride reduces IQ" report needs to be retracted

**原文链接**: [https://twitter.com/cremieuxrecueil/status/1909865076271563065](https://twitter.com/cremieuxrecueil/status/1909865076271563065)

提供的内容并非文章，而是一段来自X公司（前身为Twitter）的代码和法律/政策信息。 它表明用户的浏览器已禁用Javascript，并提供了帮助页面、服务条款、隐私政策、Cookie政策、版本说明和广告信息的链接。 它还声明版权归X公司所有，时间为2025年。 其中没有关于氟化物降低智商的报告的信息，也没有任何论点或证据来撤回该报告。

---

## 83. 夏威夷诞生了一个疯狂的“怪胎系统”

**原文标题**: A wild 'freakosystem' has been born in Hawaii

**原文链接**: [https://www.bbc.com/future/article/20250403-the-new-hawaiian-freakosystem-emerging-on-oahu-accidentally-created-by-humans](https://www.bbc.com/future/article/20250403-the-new-hawaiian-freakosystem-emerging-on-oahu-accidentally-created-by-humans)

本文以夏威夷的瓦胡岛为例，探讨了“新型生态系统”（又称“怪异生态系统”）的出现。这些生态系统的特点是本地物种和非本地物种的混合，通常是由于人类活动（如森林砍伐、物种引进和气候变化）造成的。瓦胡岛的低地森林曾经以本地动植物为主，现在却成了来自世界各地的引进物种的混合体，非本地鸟类扮演着至关重要的角色，比如种子传播，这些角色以前是由已经灭绝的本地鸟类承担的。

科学家们正在研究瓦胡岛，将其视为一个“水晶球”，以洞察受人类影响严重的生态系统的未来。虽然这些新型生态系统可能存在争议，挑战了传统的、专注于将景观恢复到干扰前状态的保护策略，但它们是自我维持的系统，已经跨越了使之不可能回到原始状态的阈值。根除非本地物种并不总是解决方案，因为有些物种在新生态系统中发挥着至关重要的作用。

文章强调了生态学家之间关于定义和管理新型生态系统的争论，指出虽然有些人认为地球上很大一部分生态系统已经过渡到新型状态，但另一些人发现很难定义一个明确的阈值。最终，瓦胡岛的案例促使人们重新评估保护方法，承认新型生态系统有可能提供有价值的，尽管是不同的，生态功能。

---

## 84. 特斯拉太阳能销售额连续四个季度下降，然后特斯拉停止公布数据。

**原文标题**: Tesla Solar Sales Declined for 4 Qtrs. Then Tesla Stopped Publishing the Numbers

**原文链接**: [https://cleantechnica.com/2025/04/07/tesla-solar-sales-declined-for-4-straight-quarters-then-tesla-stopped-publishing-the-numbers/](https://cleantechnica.com/2025/04/07/tesla-solar-sales-declined-for-4-straight-quarters-then-tesla-stopped-publishing-the-numbers/)

CleanTechnica文章讨论了特斯拉收购SolarCity后太阳能安装量的下降。作者Zachary Shahan对特斯拉推广屋顶太阳能的努力表示失望，并指出季度安装量显著下降。

在2022年第四季度“最后一个好季度”（安装100兆瓦）之后，特斯拉的太阳能安装量至少连续四个季度下降，之后特斯拉停止公布这些数据。虽然该公司仍在财务报告中公布“太阳能系统，净值”，但这些总数也在下降。如果这种趋势持续下去，特斯拉的太阳能业务可能会连续八个季度下滑。

作者强调，特斯拉的太阳能安装量尚未达到SolarCity收购后不久的水平。2016年第四季度安装了201兆瓦，随后的两个季度安装了超过150兆瓦，但此后特斯拉很少突破每季度100兆瓦。作者得出结论，特斯拉的太阳能业务可能只是“昔日辉煌的空壳”，考虑到需要增加太阳能的普及，这对清洁技术倡导者来说令人沮丧。文章暗示，特斯拉可以采取更多措施，利用其品牌和客户群来促进太阳能销售。

---

## 85. 脊椎动物中，智慧至少进化过两次

**原文标题**: Intelligence Evolved at Least Twice in Vertebrate Animals

**原文链接**: [https://www.quantamagazine.org/intelligence-evolved-at-least-twice-in-vertebrate-animals-20250407/](https://www.quantamagazine.org/intelligence-evolved-at-least-twice-in-vertebrate-animals-20250407/)

量子杂志文章《脊椎动物的智能至少进化了两次》探讨了关于复杂神经回路（支持智能）是在脊椎动物（鸟类和哺乳动物）中从共同祖先进化而来，还是在两类动物中独立进化的争论。

近期发表在《科学》杂志上的研究为后者提供了强有力的证据，表明智能多次出现。研究人员使用单细胞RNA测序技术比较了鸡、小鼠和壁虎在胚胎发育过程中的大脑结构。他们发现，虽然成熟的大脑回路在动物之间看起来非常相似，尤其是在大脑皮层区域，但哺乳动物的新皮层和鸟类的背侧脑室隆起（DVR）的结构发育方式不同——在不同的时间、以不同的顺序、在不同的脑区。这表明这些认知区域是独立进化的。

这些发现挑战了长期以来的假设，即由于鸟类缺乏像哺乳动物一样的分层新皮层，所以它们缺乏复杂的智能。虽然构建模块（神经元）相似，但它们的组织和发育途径不同。这些研究还发现，一些影响大脑发育的基因在不同物种间是共享的，表明它们从共同祖先那里继承了一些东西。

文章最后强调，智能没有固定的路径，趋同进化表明相似的解决方案可以独立产生。该研究鼓励我们拓宽对智能的理解，超越以人类为中心的观点，从而可能为人工智能的开发和寻找外星生命提供信息。

---

## 86. Show HN: 连接IBM 3151终端到大型机[视频]

**原文标题**: Show HN: Connecting an IBM 3151 terminal to a mainframe [video]

**原文链接**: [https://www.youtube.com/watch?v=V14ac9cRi9Q](https://www.youtube.com/watch?v=V14ac9cRi9Q)

YouTube上的“Show HN”帖子展示了如何将IBM 3151终端连接到大型计算机。尽管帖子本身除了标题外几乎没有提供任何信息，但上下文表明这是一个将旧终端硬件与大型机系统连接的实际演示。该视频可能展示了所涉及的过程，包括潜在的配置、电缆连接，以及可能用于验证连接和功能的测试会话。包含标准的YouTube样板（“关于 新闻 版权 联系我们…”）表明内容托管在YouTube上，并提供了视频链接。这可能对那些对复古计算、大型机技术或连接遗留系统的技术细节感兴趣的人具有吸引力。

---

## 87. 维沙普·奥伯伦编译器

**原文标题**: Vishap Oberon Compiler

**原文链接**: [https://github.com/vishapoberon/compiler](https://github.com/vishapoberon/compiler)

Vishap Oberon：一个免费、开源的Oberon-2编程语言实现，为Linux、BSD、Mac和Windows等传统操作系统设计。它使用C后端（gcc、clang、tcc或msc）进行编译，并整合了来自Ulm、oo2c和Ofront Oberon编译器的库，遵循Oakwood指南。

安装简单：克隆仓库，使用“make full”构建，可选择使用“make install”安装到系统目录，并更新PATH环境变量。该编译器支持32位和64位架构，包括Intel x86、x86_64和ARM，并且兼容多种C编译器和操作系统（GNU/Linux、MAC OSX、BSD、Windows）。

Vishap Oberon支持Oberon-2，包括类型绑定过程，并提供可通过编译器选项选择的不同整数和集合类型大小。它包含与Oberon V4、S3、Ooc、Ulm和Oakwood系统兼容的库。同时也支持Oberon-07的一些特性。

该项目起源于Josef Templ的Ofront，并由Norayr Chilingarian（库移植和平台支持）和David Brown（扩展平台和类型支持）贡献。名称“Ѵishap Oberon”引用亚美尼亚高地的龙，象征着该项目与编译器传统和“计算机科学小说”的联系。提供了大量参考和链接，以便进一步探索Oberon和相关主题。

---

## 88. Meta 被抓包操纵 AI 基准测试

**原文标题**: Meta got caught gaming AI benchmarks

**原文链接**: [https://www.theverge.com/meta/645012/meta-llama-4-maverick-benchmarks-gaming](https://www.theverge.com/meta/645012/meta-llama-4-maverick-benchmarks-gaming)

Meta被指控用其新的Llama 4模型Maverick操纵AI基准测试。具体来说，Meta在LMArena基准测试网站上部署了一个Maverick的“实验性聊天版本”，该版本在该网站上排名很高，暗示其性能优于GPT-4o等模型。然而，该版本针对“对话性”进行了优化，与公开可用的Llama 4模型不同。LMArena此后更新了其政策，以防止此类行为，强调公平和可重复的评估。

像Simon Willison这样的AI研究人员和专家批评Meta，称这种做法使基准测试分数具有误导性，因为开发者无法访问获得高分的模型。还有指控称Meta使用测试集训练Llama 4，Meta副总裁Ahmad Al-Dahle对此予以否认。

据报道，Llama 4本身的发布被推迟，原因是该模型最初未能达到内部预期。该事件凸显了基准测试在AI开发中日益增长的重要性，以及像Meta这样的公司面临的越来越大的压力，即要被视为AI领导者，这也引发了人们对AI基准测试的完整性和可靠性的质疑。

---

## 89. 展示HN：创作涂黑诗的工具

**原文标题**: Show HN: A tool for creating blackout poetry

**原文链接**: [https://bobbiec.github.io/blackout-poetry.html](https://bobbiec.github.io/blackout-poetry.html)

这个“Show HN”帖子介绍了一个创作遮蔽诗的工具。用户输入文本，用Markdown进行格式化。关键功能是使用“[方括号]”来指示应该“遮蔽”的词，大概是为了视觉上隐藏，从而揭示由剩余词语构成的诗意信息。

---

## 90. Cogito预览：将IDA作为通往通用超级智能的路径

**原文标题**: Cogito Preview: IDA as a path to general superintelligence

**原文链接**: [https://www.deepcogito.com/research/cogito-v1-preview](https://www.deepcogito.com/research/cogito-v1-preview)

Deep Cogito发布基于迭代蒸馏与放大(IDA)新型训练方法的一系列开源LLM (30亿至700亿参数)，他们认为这为通用超级智能铺平了道路。这些Cogito模型在标准基准测试中优于LLaMA、DeepSeek和Qwen的同类开源模型。700亿参数模型甚至超过了Llama 4 109B MoE模型。

IDA涉及迭代地使用子程序放大智能，然后将这种放大的智能提炼回模型的参数中。这使得模型能够迭代地自我改进，超越人类监督者的局限性，这是实现真正超级智能的关键障碍。Cogito团队仅用75天就开发了这些模型，包括令人印象深刻的700亿版本，证明了IDA的效率。

这些模型针对编码、函数调用和代理用例进行了优化，并且可以在标准模式和推理模式下运行。虽然没有针对长时间推理链进行优化，但IDA驱动的推理非常有效。Deep Cogito计划在不久的将来发布更大的模型（高达6710亿参数）和改进的检查点，所有这些都将在开源许可下发布。文章强调，虽然基准测试很重要，但现实世界的表现才是最终的评估，并且他们对模型的性能充满信心。Deep Cogito正在积极寻找顶尖工程师和研究人员加入他们构建通用超级智能的使命。

---

## 91. “互联网之父”及科技专家担忧我们过度依赖人工智能

**原文标题**: 'Father of Internet' and tech experts worry we'll rely on AI too much

**原文链接**: [https://www.cnn.com/2025/04/02/tech/ai-future-of-humanity-2035-report/index.html](https://www.cnn.com/2025/04/02/tech/ai-future-of-humanity-2035-report/index.html)

文章探讨了包括互联网之父文顿·瑟夫在内的科技专家们对日益依赖人工智能可能对人类技能和特质产生的负面影响的担忧。一项基于对301位科技领袖、分析师和学者调查的埃隆大学报告显示，随着人工智能发展的加速，到2035年，它可能会削弱诸如同理心、深度思考、道德判断和社会情感智能等关键的人类能力。

该报告强调，超过60%的受访者认为人工智能将在未来十年内从根本上改变人类能力，预测结果倾向于积极和消极结果的混合，或者主要是消极的。担忧包括将同理心和情感支持外包给人工智能代理，可能导致真实人际关系的衰退。

虽然人工智能预计会对好奇心、学习、决策、问题解决和创造力等领域产生积极影响，但专家们警告说，潜在的风险包括日益增长的技术依赖、系统故障，以及人工智能开发中对透明度和问责制的需求。他们倡导监管、数字素养培训和优先考虑人际关系，以减轻人工智能对人类增强可能产生的有害影响。

---

## 92. CSS 裸奔日

**原文标题**: CSS Naked Day

**原文链接**: [https://css-naked-day.org/](https://css-naked-day.org/)

CSS裸体日，每年4月9日庆祝，通过鼓励网站所有者在当天从其网站上移除所有CSS，来推广语义HTML和正确层级结构等Web标准。这种“裸体”展示了底层结构和内容，而没有任何样式增强。

该活动于2006年发起，持续50小时，以涵盖全球所有时区的4月9日。参与方式包括临时剥离CSS，并可选择链接回CSS裸体日网站以告知访问者。该活动强调良好结构的HTML和可访问性的重要性，而不是纯粹的审美设计。

提供的PHP函数和其他工具/插件（WordPress、LifeType、Perl、Django、Drupal、JavaScript、Go、Rails和Bash）可帮助开发人员在指定的时间段内自动执行CSS移除过程。

该项目最初由Dustin Diaz（2006-2009）创建，后来由Taylor Satula（2010-2014）托管，目前由Fabien Basmaison和Jens Oliver Meiert维护。Håkon Wium Lie强调，CSS裸体日符合CSS的根本目的：将内容与表现分离，从而防止HTML成为一种表现语言。

---

## 93. 在关税风暴中，许多公司视中国为最安全的港湾

**原文标题**: In a Storm of Tariffs, Many Companies See China as the Safest Harbor

**原文链接**: [https://www.nytimes.com/2025/04/09/business/trump-tariffs-china-factories.html](https://www.nytimes.com/2025/04/09/business/trump-tariffs-china-factories.html)

关税风暴中，许多公司视中国为最安全港湾

---

## 94. 受F1启发的碳纤维电动滑板速度可达45英里/小时

**原文标题**: Formula-1-inspired carbon electric skateboard shoots riders up to 45 MPH

**原文链接**: [https://newatlas.com/urban-transport/mach-one-carbon-fiber-electric-skateboard/](https://newatlas.com/urban-transport/mach-one-carbon-fiber-electric-skateboard/)

澳大利亚初创公司Radium Performance推出的电动滑板Mach One，专为高性能骑行设计，灵感源自一级方程式赛车。 它拥有碳纤维板面，最高时速可达45英里/小时（72公里/小时），据称可以在3秒内从0加速到30英里/小时（48公里/小时）。

该滑板采用8000瓦双后轮电机系统，配备“扭矩矢量控制”技术，可动态分配动力以提高转弯时的牵引力。它还采用了前后单摇臂悬架和耐用的钢纤维增强聚氨酯驱动带。

Mach One的空心碳纤维板面内置电池和电子元件，便于升级或维修。48V/1,089-Wh锂电池单次充电2小时即可提供长达30英里（48公里）的续航里程。 骑手可以通过无线遥控器和配套应用程序控制滑板的速度和性能。 该滑板重17公斤（37.5磅），售价为5,298澳元（约合3,173美元）。

---

## 95. 使用令牌序列迭代范围

**原文标题**: Using Token Sequences to Iterate Ranges

**原文链接**: [https://brevzin.github.io/c++/2025/04/03/token-sequence-for/](https://brevzin.github.io/c++/2025/04/03/token-sequence-for/)

C++ Ranges性能问题：冗余比较与优化方案

---

## 96. 图像文件的背叛 (2020)

**原文标题**: The Treachery of Image Files (2020)

**原文链接**: [http://beyondloom.com/blog/images.html](http://beyondloom.com/blog/images.html)

图像文件的背叛：为一位品味“独特”的收藏家所办的艺术展的附注。艺术家创作了一系列看似相同的微型艺术品：10x10像素的蓝色方块，保存为GIF文件。然而，价值在于创造每个看似同质的作品所使用的独特过程。

笔记详细描述了每件作品所使用的特定软件、操作系统，甚至汇编代码，突出了产生一个简单的蓝色GIF所需的常常复杂，有时荒谬的方法。例如，“形成与消亡”使用了旧版Macintosh OS的屏幕截图，因为预览应用程序无法保存GIF。“点彩画 I & II”涉及使用Sublime和Vim等文本编辑器精心编写PPM图像格式，然后分别使用ImageMagick和FFmpeg将其转换为GIF。“灼热的光”使用POV-Ray光线追踪器，但由于POV-Ray不支持GIF，因此生成PNG。

“补鞋匠”涉及编写汇编代码来手动构造GIF格式，需要删除无用的标头。“暗箱”使用Interactive K Environment (iKe)中的深奥编程语言K来生成单个GIF帧。“无”涉及通过电子邮件请求一位同事提供预先制作好的蓝色GIF。“绝望的痛苦”使用运行Ubuntu的虚拟机、GIMP应用程序和一个名为Charon的USB驱动器来传输文件，说明了虚拟世界和现实世界之间艰难的旅程。

最后，“蓝色与蓝色的构图”演示了使用Gnuplot创建相对容易的过程。文章最终讽刺了数字图像格式的复杂性和不一致性，以及艺术家为概念纯洁性和特定技术效果所付出的努力。

---

## 97. 弗兰克·劳埃德·赖特在俄亥俄州完成的“最后的乌托邦式住宅”

**原文标题**: "Final Usonian Home" by Frank Lloyd Wright Completed in Ohio

**原文链接**: [https://www.dezeen.com/2025/03/20/final-usonian-home-riverrock-frank-lloyd-wright-ohio-completed/?_hsenc=p2ANqtz--nulJz0XJo1E-jQIojcqaZmWjd0eXJ-oC35zKHYZb1UL94JLh6t_QI1k9lehp4fxwHKjPjkNeM-iQJihX705oJ-Maqyw&_hsmi=355439130](https://www.dezeen.com/2025/03/20/final-usonian-home-riverrock-frank-lloyd-wright-ohio-completed/?_hsenc=p2ANqtz--nulJz0XJo1E-jQIojcqaZmWjd0eXJ-oC35zKHYZb1UL94JLh6t_QI1k9lehp4fxwHKjPjkNeM-iQJihX705oJ-Maqyw&_hsmi=355439130)

弗兰克·劳埃德·赖特最后一件“尤索尼亚住宅”在俄亥俄州竣工摘要：

本文报道了弗兰克·劳埃德·赖特设计的最后一件尤索尼亚住宅Riverrock在俄亥俄州竣工。该住宅虽于1957年设计，但由于财政限制，在赖特生前或由最初的委托人建造。几十年后，一位新主人根据赖特的原始图纸和规范，最终将这栋房子变为现实。

该住宅体现了赖特的尤索尼亚理想：朴素、经济实惠且与自然融为一体。其设计特点包括低矮的轮廓、平屋顶、地热供暖和开放式平面图。Riverrock名副其实，在室内和室外都采用了天然材料，尤其是当地的河卵石。大窗户和精心布置的开口将生活空间与周围的景观连接起来，模糊了室内外的界限。

Riverrock的竣工意义重大，因为它代表了赖特愿景的实现，以及他的尤索尼亚原则以最终的、现在的物理形式的实现。它也有助于更好地理解他的建筑哲学及其对住宅设计的持久影响。这座房子是赖特不朽遗产的证明，也为美国中产阶级提供了经济实惠且美观的住宅的尤索尼亚愿景的切实例子。

---

## 98. 糖精展现对抗抗生素耐药性的意外力量

**原文标题**: Sweetener saccharin shows surprise power against antibiotic resistance

**原文链接**: [https://www.brunel.ac.uk/news-and-events/news/articles/Sweetener-saccharin-shows-surprise-power-against-antibiotic-resistance](https://www.brunel.ac.uk/news-and-events/news/articles/Sweetener-saccharin-shows-surprise-power-against-antibiotic-resistance)

伦敦布鲁内尔大学文章：糖精或可对抗抗生素耐药性

---

## 99. 英国研发“谋杀预测”工具，以识别最有可能杀人者

**原文标题**: UK creating 'murder prediction' tool to identify people most likely to kill

**原文链接**: [https://www.theguardian.com/uk-news/2025/apr/08/uk-creating-prediction-tool-to-identify-people-most-likely-to-kill](https://www.theguardian.com/uk-news/2025/apr/08/uk-creating-prediction-tool-to-identify-people-most-likely-to-kill)

英国政府正在开发一项“谋杀预测”项目，旨在通过分析已知当局人员的个人数据，来识别最有可能犯下凶杀罪的个体。算法将被用于分析来自数千人的数据，包括犯罪受害者，以找出那些面临最严重暴力犯罪风险的人。

该项目最初名为“凶杀预测项目”，现更名为“共享数据以改进风险评估”，司法部希望该项目能够提高公共安全。使用的数据包括姓名、出生日期、性别、种族、警方记录、首次与警方接触的年龄（包括作为家庭暴力受害者），以及“特殊类别的个人数据”，如精神健康、成瘾、自杀、残疾和自残指标。

像Statewatch这样的批评人士谴责该项目“令人不寒而栗且反乌托邦”，认为使用的数据可能会嵌入对少数族裔和低收入社区的偏见。他们担心该系统会强化结构性歧视，并且过于具有侵入性。Statewatch还声称使用了无辜者的个人数据，但司法部强烈否认了这一说法，坚称只使用了已定罪的罪犯的数据。

司法部坚称该项目仅用于研究，旨在利用HM监狱和缓刑服务局以及警察部队持有的现有数据，改进对严重犯罪的风险评估，从而更好地了解缓刑人员实施严重暴力犯罪的风险。他们表示将会发布一份报告。

---

## 100. Show HN: Uncurl.dev – 将 curl 命令转换为可分享、可执行的 UI

**原文标题**: Show HN: Uncurl.dev – Convert curl commands to a shareable, executable UI

**原文链接**: [https://uncurl.dev/](https://uncurl.dev/)

Uncurl.dev 是一个将 `curl` 命令转换为可分享、可执行用户界面的服务。它允许用户在用户友好的界面中轻松分享和执行 `curl` 命令。然而，由于一个严重的安全漏洞，该服务已被关闭。该漏洞源于对管理权限的不安全处理，可能允许恶意行为者获得对服务 VPS（虚拟专用服务器）的 root 访问权限。开发者强调存在默认的管理密码（如果在环境变量中未正确配置则缺少密码），这加剧了问题。该漏洞的存在使得维护该服务风险过高，导致其立即关闭。

---

