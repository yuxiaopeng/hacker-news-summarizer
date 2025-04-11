# Hacker News 热门文章摘要 (2025-04-11)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 但如果我想要一匹更快的马呢？

**原文标题**: But what if I want a faster horse?

**原文链接**: [https://rakhim.exotext.com/but-what-if-i-really-want-a-faster-horse](https://rakhim.exotext.com/but-what-if-i-really-want-a-faster-horse)

作者认为，科技行业痴迷于颠覆式创新，以“更快的马”类比为代表，往往导致可用性和用户控制权的下降，转而倾向于算法参与和内容发现。作者认为，有时用户仅仅希望对现有解决方案进行改进，即“更快的马”，而不是全新的范式。

文章以Netflix和Spotify为例。最初，Netflix是一个方便可靠的电影和节目库，具有个性化推荐和库管理等实用功能。现在，它成了一个由算法驱动的、令人不知所措且混乱的“体验”，优先考虑持续的内容轮换和通用类别，而非用户控制和清晰的目录。同样，Spotify也从一个庞大的音乐库转变为一个算法策展的、充斥着播客的内容流，牺牲了用户控制和库管理。

作者认为，包括YouTube、LinkedIn，甚至Substack在内的许多平台，正朝着TikTok模式靠拢：由算法驱动的无休止的短视频流，最大限度地减少用户控制，并优先考虑参与度而非用户自定义的组织和可发现性。这种趋势类似于“蟹化现象”，优先考虑吸引注意力，却牺牲了核心功能和用户体验。作者总结说，虽然创新很重要，但仅仅专注于颠覆可能会降低有价值的功能，并使那些只想让现有解决方案变得更好、而不是完全不同的用户感到沮丧。

---

## 2. Fedora 变革旨在实现 99% 的软件包可重复构建

**原文标题**: Fedora change aims for 99% package reproducibility

**原文链接**: [https://lwn.net/Articles/1014979/](https://lwn.net/Articles/1014979/)

LWN.net 文章探讨 Fedora 计划：到 2025 年 10 月 Fedora 43 发布时实现 99% 的软件包可重现性。可重现构建确保相同的源代码、构建环境和指令产生完全相同的二进制文件。

虽然 Fedora 历来优先控制其构建过程，但现在它的目标是加强供应链安全并实现软件包的独立验证。Fedora 对可重现性的定义与 Debian 略有不同，侧重于 RPM 中相同的有效载荷，不包括签名和某些元数据，如构建时间 (BUILDTIME) 和构建主机 (BUILDHOST)。

该项目已经实施了诸如钳制文件修改时间和使用 `add-determinism` 工具来标准化元数据等更改，实现了 90% 的可重现性。为了达到 99%，Fedora 将要求打包者将可重现性问题作为错误处理。`fedora-repro-build` 实用程序将支持本地重新构建测试，而公共 `rebuilderd` 实例将提供独立验证。

该提案建议更新 Fedora 的打包指南，以鼓励可重现的构建。虽然安全优势是主要驱动因素，但这项工作也有望通过发现错误和马虎来提高软件包质量。关于 `rebuilderd` 实例的位置和维护及其与现有 Fedora 基础设施（如 Koji 和 Copr）的集成正在进行讨论。Fedora 工程指导委员会 (FESCo) 将在工作开始前审查该提案，目标是在 Fedora 43 发布时完成。

---

## 3. 使用重心坐标在四边形上进行双线性插值

**原文标题**: Bilinear interpolation on a quadrilateral using Barycentric coordinates

**原文链接**: [https://gpuopen.com/learn/bilinear-interpolation-quadrilateral-barycentric-coordinates/](https://gpuopen.com/learn/bilinear-interpolation-quadrilateral-barycentric-coordinates/)

此文章宣布AgilitySDK预览版1.716.0发布，该版本引入了对全新Microsoft DirectX和视频编码功能的支持。公告简短，主要强调了这些新功能在指定的AgilitySDK预览版中的可用性。

---

## 4. Erlang并非仅关于轻量级进程和消息传递。

**原文标题**: Erlang's not about lightweight processes and message passing

**原文链接**: [https://stevana.github.io/erlangs_not_about_lightweight_processes_and_message_passing.html](https://stevana.github.io/erlangs_not_about_lightweight_processes_and_message_passing.html)

本文认为，Erlang构建可靠分布式系统的核心优势并非主要在于其轻量级进程和消息传递，而在于其定义明确的通用组件，即“行为”（behaviours）。文章承认Erlang起源于Prolog以及在爱立信公司为电话交换机所做的开发，但作者强调Joe Armstrong的博士论文是理解行为重要性的关键资源。

行为类似于其他语言中的接口，可以强制执行结构和最佳实践。文章详细介绍了几个核心Erlang行为：`gen_server`（用于并发有状态服务器）、`gen_event`（用于事件管理）、`gen_statem`（状态机）和`supervisor`（用于进程监控和重启）。监督者结合“让它崩溃”的理念，通过重启失败的进程来提供容错能力。作者指出，监督者机制在线程/轻量级进程级别运行，这使其与 Kubernetes 等工具不同。

文章将 `application` 和 `release` 描述为更高级别的组织单元，其中 `application` 封装了一个监督树和相关组件，而 `release` 打包一个或多个 `application`，包括升级/回滚机制。

作者总结说，Erlang 的行为提供了一种强大的结构，可以促进可靠的软件开发。他质疑为什么其他语言和框架专注于轻量级进程和消息传递，而没有采用 Erlang 行为的结构化方法。文章提出了一个简单的 `gen_server` 接口签名，并提出了如何实现它来处理并发请求。

---

## 5. 倭黑猩猩使用一种一度被认为是人类独有的句法

**原文标题**: Bonobos use a kind of syntax once thought to be unique to humans

**原文链接**: [https://www.newscientist.com/article/2474993-bonobos-use-a-kind-of-syntax-once-thought-to-be-unique-to-humans/](https://www.newscientist.com/article/2474993-bonobos-use-a-kind-of-syntax-once-thought-to-be-unique-to-humans/)

倭黑猩猩叫声展现“非平凡组合性”，挑战人类语言独特性研究

---

## 6. 伦敦地铁实时地图

**原文标题**: Live Map of the London Underground

**原文链接**: [https://www.londonunderground.live/](https://www.londonunderground.live/)

本文简要介绍了伦敦地铁的“实时线路图”，提供列车位置的实时信息。 这不仅仅是一张静态地图；用户可以通过右键单击来旋转视角，并放大以查看建筑物细节。 将光标悬停在特定点上可提供更多信息（可能是关于线路、车站或延误）。 该地图清晰地标有“实时”字样，强调其时效性。 本文感谢Ben James的创作。 重要的是，它还承认了底层数据的来源以及“The London Minute”对地图瓦片的赞助。 总之，本文介绍了一个伦敦地铁的交互式实时地图，突出了其功能、创建者、数据来源和赞助。

---

## 7. Mosaic (YC W25) 正在构建一个通用的视频编辑代理。

**原文标题**: Mosaic (YC W25) is building a general purpose agent for video editing

**原文链接**: [https://www.ycombinator.com/companies/mosaic-2/jobs/ru8Nwdq-founding-engineer](https://www.ycombinator.com/companies/mosaic-2/jobs/ru8Nwdq-founding-engineer)

Mosaic，一家Y Combinator W25孵化的初创公司，正在开发一款用于视频编辑的通用人工智能代理。他们正在寻找一位创始工程师，以加速开发他们的“代理视频编辑范式”，该系统允许用户在基于节点的画布中创建和运行自己的多模态视频编辑代理。这些代理可以自动执行编辑，在项目中重复使用并自我改进。

该职位需要从第一性原理出发解决具有挑战性的技术问题，构建可扩展的视频处理和推理流水线，创建评估指标，并为设计和产品决策做出贡献。Mosaic的初始原型在Google Gemini Kaggle竞赛中获得第一名，并被评为Y Combinator批次中最佳演示。

该公司由Adish Jain和Kyle Wade创立，拥有一支由前特斯拉工程师组成的高技术团队。他们的目标是将视频编辑时间从数小时缩短到数秒。创始工程师职位提供10万至15万美元的薪水和0.50%至3.00%的股权，位于旧金山，并向包括应届毕业生在内的所有经验水平的候选人开放。

---

## 8. 优势即劣势

**原文标题**: Strengths Are Your Weaknesses

**原文链接**: [https://terriblesoftware.org/2025/03/31/your-strengths-are-your-weaknesses/](https://terriblesoftware.org/2025/03/31/your-strengths-are-your-weaknesses/)

本文认为，一个人的最大优势往往与他们的弱点内在相关，本质上是同一枚硬币的两面。文章通过作者的个人经历以及对工程师的管理观察，突出了诸如“编码速度”之类的特征如何既能带来快速的功能交付，又会导致边缘案例被忽略。

作者强调这种现象具有普遍性，并为管理者提供了三种应对策略：

1.  **在1对1会议中承认二元性：** 帮助个人理解他们的优势和劣势不是分离的实体，而是同一潜在特性的表现。这有助于培养自我意识，减少自我批评。
2.  **提供清晰的背景指导：** 明确定义某些倾向有利或不利的情况。这使个人能够就如何适当地利用他们的优势做出明智的决定。
3.  **战略性地利用张力：** 不要寻求同质化的团队，而是拥抱多样化的工作方式。将具有对比方法的人配对可以带来创新和成长，因为他们可以互相学习。

总的来说，目标不是通过创造统一“平衡”的个人来消除弱点。相反，管理者应专注于培养自我意识，并授权团队成员根据具体情况理解和调整他们的自然倾向。这种方法将感知的缺陷转化为一个人整体技能组合中可管理的部分，并促进个人成长和团队效率。最终，它强调了对个体内部固有复杂性的同情和接受的重要性。

---

## 9. 五角大楼将终止与埃森哲、德勤的51亿美元IT合同

**原文标题**: Pentagon to terminate $5.1B in IT contracts with Accenture, Deloitte

**原文链接**: [https://www.reuters.com/world/us/pentagon-terminate-51-billion-it-contracts-with-accenture-deloitte-others-2025-04-11/](https://www.reuters.com/world/us/pentagon-terminate-51-billion-it-contracts-with-accenture-deloitte-others-2025-04-11/)

**概要：**

五角大楼计划于2025年终止与埃森哲、德勤和其他公司约51亿美元的IT合同。该决定源于五角大楼希望简化其IT运营，并采取更精简高效的IT服务方式。国防部计划发展内部能力，并将更大、更全面的合同授予更少数量的供应商，而不是依赖多个承包商提供类似的服务。预计此举将减少冗余、提高数据安全性，并有可能从长远来看节省纳税人的钱。虽然目前的合同将持续到2025年终止，但五角大楼将不再续签。据报道，受影响的公司正在与五角大楼沟通，以了解该决定的全部影响，并探索国防部不断发展的IT领域中潜在的未来机会。五角大楼希望这一改变能够带来更敏捷、更具响应性的IT基础设施。

---

## 10. WordPress发布全新免费AI网站构建器

**原文标题**: WordPress launches new free AI website builder

**原文链接**: [https://wordpress.com/blog/2025/04/09/ai-website-builder/](https://wordpress.com/blog/2025/04/09/ai-website-builder/)

WordPress 发布免费 AI 网站构建器，旨在以最小的用户工作量创建功能齐全的网站。该工具面向企业家、小企业主、自由职业者、博主和开发者，他们寻求一种快速简便的方式来建立在线形象。

这款 AI 构建器无需手动选择主题、调整颜色、创建文本和寻找图像。用户只需向 AI 描述他们的网站想法，AI 就会生成一个包含文本、布局和图像的完整 WordPress 网站。用户可以通过聊天提示或手动编辑来完善 AI 生成的内容和设计。

虽然最初在创建电子商务网站或复杂集成方面受到限制，但该工具旨在快速创建美观实用的网站。要使用此构建器，用户需要一个 WordPress.com 帐户，并通过在指定页面上描述他们的网站想法来访问它。目前，该 AI 构建器仅适用于新的 WordPress.com 网站。

该服务提供 30 个免费提示用于调整，而拥有 WordPress.com 托管计划的用户可以获得无限提示，该计划还包括第一年的免费域名。用户可以随时通过 WordPress.com 站点仪表板恢复到 AI 构建器。 虽然 AI 处理初始构建，但用户保留完全控制权，并且可以手动编辑和添加页面、更改设计以及使用开发工具。该 AI 网站构建器旨在简化网站创建，使用户能够快速建立在线形象，而无需广泛的技术技能。

---

## 11. 在小溪玩耍

**原文标题**: Playing in the Creek

**原文链接**: [https://www.lesswrong.com/posts/rLucLvwKoLdHSBTAn/playing-in-the-creek](https://www.lesswrong.com/posts/rLucLvwKoLdHSBTAn/playing-in-the-creek)

获得理解和技能常常会关闭玩乐探索和不受限制努力的途径。童年时，筑坝小溪是一种有趣的挑战。发现“铲子”解决方案（塌岸）提供了一种更有效的方法，但也消除了精巧筑坝的乐趣。这种模式在作者的一生中不断重复：发生事故后，建造 K'Nex 弹射器变得不再无忧无虑；学会了调整技巧后，制作弓箭也不再有趣。

作者将这一概念扩展到职业选择。收到一份利润丰厚的金融工作邀请，虽然最初是一个目标，但却让作者意识到，如果不考虑道德影响，他们就不能再自由地追求“尽可能多地赚钱”。

作者将此与被更大力量所淹没的情况进行对比，例如在潮汐池的出水口玩耍。在这些情景中，他们行为的后果微乎其微，可以自由玩耍。然而，即便如此，不断增长的意识，比如注意到沙蚬，也会缓和他们的行为。

最终，本文通过这些个人轶事来告诫人们不要在不考虑潜在后果的情况下追求人工智能的发展。作者重视探索过程，但担心取得不受约束的成功可能带来的后果，即使这意味着“用隐喻的烟花炸弹炸掉他们的手”，这表明了一种对负责任的开发而非不受约束的进步的偏好。 Anthropic 对伦理考量的关注被视为一个积极的信号。

---

## 12. 如何制作长弓

**原文标题**: How to Make a Longbow

**原文链接**: [https://www.howtomakealongbow.co.uk](https://www.howtomakealongbow.co.uk)

这与其说是一篇文章，不如说是一个关于制作长弓的介绍性占位页面。要点如下：

*   **本页面专注于如何制作长弓这一主题。**
*   **内容是动态且不断扩充的。** 本网站正在积极更新。
*   **重视用户反馈。** 作者鼓励提出与长弓制作相关的建议和特定信息需求。

---

## 13. 展示HN：构建更好的基础镜像

**原文标题**: Show HN: Building better base images

**原文链接**: [https://github.com/avkcode/container-tools](https://github.com/avkcode/container-tools)

容器工具是一个旨在简化创建最小化、定制化和安全Debian容器镜像的项目。它解决了标准Dockerfile构建中常见的存储膨胀、网络效率低下和迭代速度慢等问题。该工具利用`debootstrap`构建仅包含必要组件的基础镜像，从而能够基于通用基础创建专门的变体（例如，Java、Kafka）。

提供的`Makefile`允许用户构建各种Debian镜像，包括精简的Java和GraalVM版本，以及Kafka集成。构建过程生成可以导入Docker的`.tar`文件，通过`docker import`实现。安全扫描也集成在构建后步骤中，使用Trivy进行。

扩展该工具需要添加新组件的配方（例如，通过定义版本、SHA256哈希和URL来配置Kafka），然后在`Makefile`中创建一个新的目标，该目标使用自定义配方和相关脚本。

项目结构包括Debian配置、GPG密钥、各种软件（Java、Maven、Gradle、Kafka）的安装配方、构建后脚本以及已构建镜像的输出目录。它提供了一种创建高效且安全的基础镜像的方法，显著改善容器化工作流程。

---

## 14. 没有加菲猫的加菲猫

**原文标题**: Garfield Minus Garfield

**原文链接**: [https://garfieldminusgarfield.net](https://garfieldminusgarfield.net)

提供的文本描述了“没有加菲猫的加菲猫”，并包括与之相关的两个日期条目：1月27日和11月3日。每个日期条目都链接到“脸书上的G-G”和“推特上的G-G”，表明“没有加菲猫的加菲猫”在这些社交媒体平台上的存在。

本质上，这段文字突出了“没有加菲猫的加菲猫”的存在和在线状态，并提供了两个特定日期的Facebook和Twitter帐户链接。

---

## 15. 求知者的WebRTC

**原文标题**: WebRTC for the Curious

**原文链接**: [https://webrtcforthecurious.com](https://webrtcforthecurious.com)

WebRTC好奇者指南是一本开源书籍，旨在为所有级别的开发者提供对WebRTC技术的全面且公正的理解。与教程不同，本书侧重于协议、API和底层技术细节，总结了RFC和未公开的知识，同时保持厂商中立的视角。

本书结构适用于多次阅读，每章都分三个层次解决一个问题：问题定义、解决方案解释（包括技术细节）以及进一步学习的资源。无需任何先验知识，读者可以从任何地方开始阅读。

本书面向WebRTC新手、寻求更深入理解的现有用户、调试专业人员以及需要澄清的实施者。目标是教授整个WebRTC系统，牺牲专家级的细节以换取更广泛的理解。

本书以ePub和PDF格式在GitHub和WebRTCforTheCurious.com上提供，并采用CC0许可，允许免费使用和分发，无需署名。作者强调他们对隐私的承诺，网站不进行任何分析或跟踪。欢迎通过GitHub贡献，鼓励用户提出问题、建议改进意见并为本书的开发做出贡献。

---

## 16. 我们在2秒内克隆一个运行中的虚拟机

**原文标题**: We clone a running VM in 2 seconds

**原文链接**: [https://codesandbox.io/blog/how-we-clone-a-running-vm-in-2-seconds](https://codesandbox.io/blog/how-we-clone-a-running-vm-in-2-seconds)

CodeSandbox如何实现近乎瞬时(2秒)克隆运行虚拟机(VM)以用于开发环境：利用内存快照加速克隆

---

## 17. “100个Go语言错误及避免方法”背后的故事

**原文标题**: The Story Behind “100 Go Mistakes and How to Avoid Them”

**原文链接**: [https://www.thecoder.cafe/p/100-go-mistakes](https://www.thecoder.cafe/p/100-go-mistakes)

Teiva Harsanyi 分享了他撰写《100个Go语言常见错误以及如何避免》一书的幕后故事。 最初，他为了平衡Scala/Akka而开始探索Go语言，并迅速对这门语言产生了热情。一篇列出Go常见错误的博客文章意外走红，这启发他将这个概念扩展成一本书。

他联系了Manning出版社，并被其高质量所打动。在提案获得积极评价后，他收到了一份合同，其中包括4000美元的预付款和截止日期。一位开发编辑（DE）虽然不是Go专家，但在改进他的写作风格和结构方面发挥了关键作用。这本书的目标读者是已经熟悉Go语言的读者。

Harsanyi的目标是创作他所能创作的最好的Go语言书籍，并致力于提供最高质量的内容。该手稿经历了严格的评审阶段（1P、2P、3P），外部评审人员提供了宝贵的反馈意见。来自Manning出版社的另一位作者Bill Kennedy的建议，即处理每一个评论，无论多么细小，对提高书籍质量都起到了重要作用。 出现了一个小问题，即技术开发编辑（TDE）缺乏足够的Go语言知识，阻碍了他们提供充分的技术指导。 尽管如此，Harsanyi还是坚持不懈，利用MEAP流程继续开发这本书。

---

## 18. 一台2000美元“美国制造”的手机是如何生产的

**原文标题**: How a $2k 'Made in the USA' Phone Is Manufactured

**原文链接**: [https://www.404media.co/how-a-2-000-made-in-the-usa-liberty-phone-phone-is-manufactured/](https://www.404media.co/how-a-2-000-made-in-the-usa-liberty-phone-phone-is-manufactured/)

本文探讨了Purism公司制造“美国制造”的Liberty Phone的努力，这是他们Librem 5手机的一个版本。Purism创始人Todd Weaver解释了该公司的历程，始于2014年，其愿景是在美国进行制造，以确保安全、透明的供应链并满足安全市场的需求。

虽然标准的Librem 5在中国制造，售价800美元，但Liberty Phone在Purism位于加利福尼亚州卡尔斯巴德的工厂组装，售价2000美元。Purism使用表面贴装技术 (SMT) 将组件连接到裸电路板上，从而有效地在美国本土将手机电子产品从原材料制造为成品。这个过程超越了简单的组装，组装仅仅是将预制零件组合在一起。

该公司努力从西方分销商和制造商处采购组件，包括那些拥有美国工厂的制造商。然而，由于供应链的复杂性和Purism相对较小的规模（这降低了他们与供应商的议价能力），采购在美国开采的原材料仍然具有挑战性。某些组件，例如用于计时的特定类型的晶体，主要来自中国，尽管Purism正在探索替代方案。

Weaver承认，与旗舰手机相比，Liberty Phone的规格并非最先进的，但他将此归因于复制中国高科技制造生态系统的难度。将整个过程转移到美国需要大量投资和稳定的未来前景。虽然从中国采购某些组件更便宜并且具有更宽的频段，但Purism为调制解调器等模块提供美国制造的选择。

尽管面临挑战，Purism仍致力于透明化，发布原理图和硬件物料清单，显示组件的来源。

---

## 19. 代理设计中的自主性、控制性和可靠性

**原文标题**: Agency vs. Control vs. Reliability in Agent Design

**原文链接**: [https://fin.ai/research/agency-control-reliability-the-tradeoffs-in-customer-support-agents/](https://fin.ai/research/agency-control-reliability-the-tradeoffs-in-customer-support-agents/)

人工智能客服 Agent 设计中自主性、控制和可靠性 (ACR) 的权衡：提高 Agent 可靠性的策略

---

## 20. Rust CUDA 项目

**原文标题**: Rust CUDA Project

**原文链接**: [https://github.com/Rust-GPU/Rust-CUDA](https://github.com/Rust-GPU/Rust-CUDA)

Rust CUDA 项目旨在使 Rust 成为使用 CUDA 工具包进行高性能 GPU 计算的一流语言。它提供工具和库，用于将 Rust 代码编译为针对 NVIDIA GPU 优化的 PTX 代码，并方便在 Rust 中使用现有的 CUDA 库。这解决了 Rust 与 CUDA 结合使用的历史挑战，即 LLVM PTX 后端证明不可靠。

该项目范围广泛，涵盖 CUDA 生态系统的各个方面，包含多个 crate：

*   **rustc\_codegen\_nvvm:** 一个针对 NVVM IR 的 rustc 后端，用于生成优化的 PTX 代码。
*   **cuda\_std:** GPU 端函数和实用程序。
*   **cudnn:** 用于深度学习的 GPU 加速原语。
*   **cust:** CPU 端 CUDA 功能，如内核启动和内存分配。
*   **gpu\_rand:** GPU 友好的随机数生成。
*   **optix:** CPU 端的硬件光线追踪和降噪。

该项目还包括用于较小 CUDA 库的粘合 crate。

该项目承认 rust-gpu 和其他实验性的 Rust-to-GPU 编译器等相关工作。它提供包含环境变量（例如，OPTIX\_ROOT）和 `cargo build` 的设置说明。 提供了 Dockerfile 用于容器化开发，以 Ubuntu 24.04 为例，并包含用于 VS Code 的示例 `.devcontainer.json`。

该项目在 Apache 2.0 和 MIT 许可下获得许可，鼓励在相同的双重许可条款下进行贡献。

---

## 21. DDoS缓解泄漏

**原文标题**: DDoS Mitigation Leak

**原文链接**: [https://www.kentik.com/blog/beyond-their-intended-scope-ddos-mitigation-leak/](https://www.kentik.com/blog/beyond-their-intended-scope-ddos-mitigation-leak/)

本文分析了由DDoS缓解服务提供商Voxility (AS3223) 于2025年4月1日引发的近期BGP路由泄漏事件。此次泄漏持续约20分钟，将互联网流量错误地导向罗马尼亚布加勒斯特，扰乱了全球服务。

文章将BGP泄漏定义为路由宣告超出其预期范围的传播，区分了错误始发（宣告未经授权的IP地址块）和路径错误（非法插入转发路径）。该事件被归类为路径错误，涉及超过30,000条泄漏路由。

该分析追踪了被篡改的BGP路径，强调了通常通过直接连接对等互连的路由如何被路由通过Voxility的网络，通常是由于较短的AS路径。文章使用Kentik的BGP可视化工具，展示了对特定路由的影响，说明了有限传播的“区域路由”如何因泄漏而广泛传播，从而导致中断。

此外，文章分析了泄漏对流量的影响。通过检查带有AS路径注释的NetFlow数据，文章确定韩国、越南和缅甸是受影响最严重的目的地国家。它还表明，虽然一些流量被错误地引导并最终到达目的地，但由于网络拥塞，很大一部分流量被丢弃。

最后，文章倡导采用RFC 9234，该规范定义了“仅面向客户”（OTC）BGP路径属性。此属性将允许网络发出信号，表明某些路由应仅传播给直接客户，从而可能防止此类泄漏。文章总结说，积极采用这些技术对于减轻不可避免的BGP事故造成的破坏至关重要。

---

## 22. Deno 在 Varnish 中，运行于 TinyKVM 之上

**原文标题**: Deno Under TinyKVM in Varnish

**原文链接**: [https://info.varnish-software.com/blog/tinykvm-in-varnish-and-some-deno](https://info.varnish-software.com/blog/tinykvm-in-varnish-and-some-deno)

本文探讨了TinyKVM，一种具有原生性能的沙盒，作为Varnish Cache中的计算框架，重点关注其速度和按请求隔离能力。Laurence Rowe和Alf-André Walla讨论了将基于Rust的Deno JavaScript运行时嵌入到TinyKVM中并对其性能进行基准测试。

TinyKVM允许运行Linux ELF文件，并提供用于处理HTTP请求的简单API。它支持用于按请求隔离的临时VM，并在每个请求后重置VM状态。一个JSON最小化示例展示了静态缓冲区如何用于非临时程序。一个GBC模拟器示例演示了共享的可变存储，其中请求VM从主VM派生，以进行协作游戏。一个名为“storage”的函数处理共享的可变存储。

Laurence Rowe强调了Deno在TinyKVM中的性能，显示在渲染React页面时，按请求隔离仅增加约0.4毫秒的延迟，使其可能比现有解决方案更快。为了适应Deno，TinyKVM增加了对Rust的crt-static的支持和一个新的`wait_for_requests_paused` API。

文章包括一个gzip基准测试，展示了使用libdeflate和zlib-ng的性能改进。启用巨页导致Deno JS程序在未修改代码的情况下性能提升12%。最后，作者展示了一个小型程序的按请求隔离，在HTTP基准测试中平均耗时14微秒。TinyKVM旨在简化数据处理并提供对Varnish缓存的直接访问。

---

## 23. 废弃核电站成为世界一流声学实验室

**原文标题**: An unused nuclear power plant became home to a world-class acoustics lab

**原文链接**: [https://www.theverge.com/tech/644385/nuclear-power-plant-acoustics-lab](https://www.theverge.com/tech/644385/nuclear-power-plant-acoustics-lab)

艾莉森·约翰逊的文章探讨了华盛顿州萨特索普商业园中一座废弃的核电站如何被改造为世界一流的声学测试机构NWAA实验室。所有者罗恩·索罗利用该电站巨大且隔音的混凝土结构，创建了可控的声学测试环境。

文章详细介绍了命运多舛的华盛顿核项目3号和5号（WNP-3和WNP-5）的历史，突出了它们的财务问题和最终的废弃。前NASA科学家索罗看到了未使用的反应堆建筑在声学测试方面的独特潜力，特别是其厚重的混凝土墙、偏远的位置和稳定的温度。

NWAA实验室利用该设施的混响室来测试隔音材料、产品的噪音水平，甚至包括安全政府通信设施（SCIF）的声音完整性。约翰逊描述了改造现有结构的挑战，例如切割重型钢筋混凝土，以及所需的持续维护，例如处理涡轮机大楼漏水的屋顶。

尽管存在挑战，但这种独特的环境也带来了优势。混凝土提供了卓越的隔音效果，并且配备了自由场扬声器测试装置。索罗强调了他的工作的实践性，需要木工、管道和焊接方面的技能来维护和改造该设施。最终，这篇文章说明了一个不太可能的地方如何成为声学科学的宝贵资产。

---

## 24. 我为什么用Lisp编程

**原文标题**: Why I Program in Lisp

**原文链接**: [http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html](http://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html)

乔·马歇尔在2025年4月10日的一篇博客文章中解释了他偏爱使用 Lisp 编程的原因，尽管它缺乏主流的普及度。他认为 Lisp 相比其他语言有几个优势：由于其统一的语法（剑桥波兰表示法），它更容易记忆；限制更少；并且可以减少思想和程序之间的“摩擦”。他还强调了 Lisp 的函数式编程支持，特别是它的替换模型、代码重构的便利性和 lambda 表达式。

马歇尔强调了 Lisp 的快速原型设计能力、调试器、安全内存模型和 REPL 环境，这些使其能够立即评估和集成代码片段。动态类型虽然是一把双刃剑，但允许自动的特别多态，从而产生适用于各种数据类型的通用代码。

虽然承认其他语言也可能具有其中一些特性，但马歇尔认为 Lisp 以独特的方式将它们结合在一起。他将 Lisp 视为一种用于思考问题的工具，这使得编程过程本身就令人愉快。

评论部分讨论了 Lisp 中多态的细节，与 C++、Haskell 和 Rust 等静态类型语言进行了比较，并提供了阶乘和欧几里德算法实现的示例。 对话涉及动态类型和静态类型之间的权衡，以及不同语言的表达能力。 还讨论了 Lisp 与 C 的用例，以及 Lisp 的审美之美及其在配置 Emacs 中的应用。

---

## 25. 我私人的二进制：Linux内核模块的个性化介绍

**原文标题**: My Own Private Binary: An Idiosyncratic Introduction to Linux Kernel Modules

**原文链接**: [https://www.muppetlabs.com/~breadbox/txt/mopb.html](https://www.muppetlabs.com/~breadbox/txt/mopb.html)

本文讲述了作者在 Linux 上研究可执行文件格式的历程，其动机是创建尽可能小的可执行文件。最初，作者探索了 ELF 文件并显著减小了它们的大小。这引发了对 aout 二进制文件的兴趣，但他们发现由于安全问题，Linux 内核通常禁用 aout 支持。

作者随后思考了 Linux 中二进制格式支持的动态特性，发现可以通过内核模块添加新的格式。由于 Linux 中不存在“扁平”（无元数据）格式，作者考虑实现对 MS-DOS 的 .com 格式的支持，该格式是真正扁平的。

文章随后转为解释内核模块。这些是链接到运行内核中的目标文件，允许动态添加功能，例如硬件支持或新的二进制格式，而无需重新编译整个内核。作者提供了一个简单的“hello kernel”模块示例，包括代码和构建说明，以演示使用 `insmod`、`lsmod`、`dmesg` 和 `rmmod` 创建和管理内核模块的基础知识。虽然承认内核开发的潜在风险，例如由于编码错误导致系统崩溃，但作者鼓励实验，并强调内核模块提供的强大功能和自由。最后，文章指出可以使用自定义内核模块来添加对任何二进制文件格式的支持，包括所需的 .com 格式。

---

## 26. h1元素的默认样式正在更改

**原文标题**: Default styles for h1 elements are changing

**原文链接**: [https://developer.mozilla.org/en-US/blog/h1-element-styles/](https://developer.mozilla.org/en-US/blog/h1-element-styles/)

本文探讨了即将到来的 `<h1>` 元素默认浏览器样式的更改，特别是它们与 `<section>`, `<article>`, `<nav>` 和 `<aside>` 等分节元素之间的交互。 历史上，浏览器使用大纲算法来隐式调整 `<h1>` 样式，基于它们在这些元素中的嵌套，有效地将它们降级为 `<h2>`, `<h3>` 等。

这种行为现在将被移除。 浏览器正在逐步淘汰这些隐式样式，这意味着无论 `<h1>` 位于分节元素的何处，都将始终以其默认样式呈现。 此更改旨在减少混淆，并使浏览器行为与更新的 HTML 规范保持一致，该规范已于 2022 年删除了有问题的轮廓算法。

建议开发人员为 `<h1>` 元素显式定义字体大小和边距，以避免依赖即将移除的默认浏览器样式。 Lighthouse 和其他页面审核工具会将没有指定字体大小的 `<h1>` 实例标记为警告（"H1UserAgentFontSizeInSection"）。 Firefox 和 Chrome 已经开始实施这些更改，预计 Safari 也会效仿。

本文建议：使用 `<h2>`, `<h3>` 等定义清晰的标题层级结构； 始终指定 `<h1>` 字体大小和边距； 考虑更新 CSS 重置； 并使用 Lighthouse 等工具来审核网站的已弃用用法。 使用 `:where(h1)` 可以帮助避免应用样式时的特殊性冲突。

---

## 27. 具有摄像头和屏幕共享功能的Gemini Live

**原文标题**: Gemini Live with camera and screen sharing capabilities

**原文链接**: [https://blog.google/products/gemini/gemini-live-android-tips/](https://blog.google/products/gemini/gemini-live-android-tips/)

Gemini Live 扩大可用性：新增 Pixel 9 和 Samsung Galaxy S25 设备支持

本文宣布 Gemini Live 的可用性进一步扩大。Gemini Live 允许用户通过手机摄像头或屏幕共享与 Gemini AI 进行自然对话。最初仅面向 Android 上的 Gemini Advanced 订阅者开放，现在所有 Pixel 9 和 Samsung Galaxy S25 设备上的 Gemini 应用用户均可使用。Gemini Live 支持超过 45 种语言。

本文重点介绍了用户可以利用 Gemini Live 的五个关键方式：

1.  **整理收纳：** 用户可以将摄像头对准杂乱的空间，获得关于整理、分类和空间最大化的实时建议。
2.  **创意头脑风暴：** 屏幕共享可用于向 Gemini 展示鼓舞人心的图像，激发各种创意项目（如设计或写作）的灵感。
3.  **故障排除：** 摄像头输入允许用户实时向 Gemini 展示技术问题，并获得问题解决的指导。
4.  **个人购物建议：** 屏幕共享使用户能够在 Gemini 的帮助下浏览在线零售商，Gemini 可以提供产品比较、风格建议以及对潜在购买商品的反馈，还可以使用摄像头功能查看商品与现有衣橱的搭配效果。
5.  **技能发展与反馈：** 用户可以分享他们的作品，例如博客文章或社交媒体活动，以获得个性化建议并确定需要改进的领域。

---

## 28. 适用于经典 Macintosh OS 7/8/9 的 Mbed-TLS 移植版本

**原文标题**: A port of Mbed-TLS for the Classic Macintosh OS 7/8/9

**原文链接**: [https://github.com/bbenchoff/MacSSL](https://github.com/bbenchoff/MacSSL)

本文档详细介绍了“MacSSL”，它是Mbed-TLS库针对Classic Macintosh OS 7/8/9的移植版本，使用Metrowerks Codewarrior Pro 4开发。该项目的目标是为一个基于老式数码相机的“Instagram克隆”应用启用HTTPS通信。

该仓库包含Codewarrior项目文件和PolarSSL（Mbed-TLS的一个分支）库的必要子集，版本为2.29.9。由于Mac文件资源问题，该项目以压缩的“Archive.sit”文件形式提供。该移植支持TLS 1.1，具有最小配置，包括特定的密码套件（AES-128-CBC-SHA, AES-256-CBC-SHA），secp256r1椭圆曲线，以及使用SHA-256, SHA-384和SHA-1的RSA签名。还实现了ISRG Root X1和Let's Encrypt R11的证书处理。

移植过程中的主要挑战包括C89/C90的限制（缺少方法重载、可变参数宏），需要进行大量的代码重构，以及缺少原生64位整数支持，这通过结构体和自定义函数进行模拟。该项目还面临由于操作系统限制导致的严重的熵收集问题。实施了一个自定义的熵收集系统，从各种系统源提取熵。

包含一个示例应用程序，它使用HTTPS从指定的API端点获取数据，并在文本框中显示结果，并将其写入名为“SSL-Debug.txt”的调试文件中。调试日志显示成功的TLS握手。

---

## 29. Clojure：无需 ClojureScript 的实时协作 Web 应用

**原文标题**: Clojure: Realtime collaborative web apps without ClojureScript

**原文链接**: [https://andersmurphy.com/2025/04/07/clojure-realtime-collaborative-web-apps-without-clojurescript.html](https://andersmurphy.com/2025/04/07/clojure-realtime-collaborative-web-apps-without-clojurescript.html)

本文介绍 Datastar，一个轻量级 (11.4kb Brotli 压缩) 的超媒体框架，作为使用 Clojure 构建实时协作 Web 应用的 ClojureScript 的可行替代方案。作者通过一个简单的多人在线生命游戏实现来演示这一点。

其核心思想是使用服务器发送事件 (SSE) 每 200 毫秒将页面的整个 `<main>` 元素从服务器流式传输到客户端。然后，Datastar 使用快速的形态算法有效地将新的 HTML 片段与旧的片段合并，仅更新更改的部分。作者认为，尽管发送了整个 `<main>` 元素，但由于 SSE 上 Brotli 压缩提供非常高的压缩率，因此这种方法具有高性能和带宽效率。

作者将 Datastar 与 Phoenix LiveView 进行对比，强调 Datastar 的简洁性和无状态性。他们还反对使用 WebSockets，理由是其存在防火墙问题、缺乏压缩以及断开连接处理不佳等运营挑战，转而提倡使用 SSE（或 UDP/WebTransport 替代方案）。

为了简化操作，作者使用了构建在 Datastar 之上的 `hyperlith` 微型框架来处理 SSE、压缩和其他细节。示例代码展示了如何使用 Clojure 在服务器上处理用户操作，以及 `render-home` 函数如何生成发送给所有客户端的 HTML。由于渲染函数向所有人显示相同的内容，因此使应用程序支持多人游戏无需任何代码更改。

结论强调，Datastar 与 Clojure 结合使用可以轻松构建交互式和协作式 Web 应用程序，而无需 ClojureScript。

---

## 30. 离职：深入剖析Lumon的中世纪野兽派宇宙

**原文标题**: Severance: A closer look into the mid-century, brutalist universe of Lumon

**原文链接**: [https://www.designboom.com/design/severance-closer-look-mid-century-brutalist-retro-futuristic-universe-lumon-03-21-2025/](https://www.designboom.com/design/severance-closer-look-mid-century-brutalist-retro-futuristic-universe-lumon-03-21-2025/)

《离职》因其通过设计构建世界观的精湛技艺而备受赞誉，它为鲁门工业打造了一个既时尚又令人不安的宇宙。该剧巧妙地融合了世纪中期现代主义、粗野主义企业美学和复古未来主义技术，创造出一个反乌托邦环境，其中每个设计元素都服务于心理目的。

文章强调了建筑选择，例如由埃罗·沙里宁设计的贝尔实验室，是如何扭曲成控制机制的，将熟悉的现代主义理想转化为某种不祥之物。通过包含展示现代主义设计的住宅，如杰拉德·卢斯住宅、塔格卡尼克住宅和比尔住宅，创造出对比，强调了企业与个人世界之间的分裂。

家具和物品，尤其是迪特·拉姆斯设计的极简主义工业作品，为公司营造了临床式和令人不安的美学。马克·纽森设计的Fauteuil Nimrod等其他设计也增加了这种高度控制的环境。

色彩、排版和艺术也是至关重要的叙事工具。柔和的色调和鲜明的排版强化了鲁门公司冷酷的官僚作风。鲁门内部令人不安的艺术，尤其是对员工的邪教式描绘以及围绕基尔·伊根的传说，充当了企业宣传，塑造了员工的认知，并培养了一种人为的团结感。即使是鲁门外部的艺术，也暗示着始终存在的焦虑。

---

## 31. 2025年人工智能指数报告

**原文标题**: 2025 AI Index Report

**原文链接**: [https://hai.stanford.edu/ai-index/2025-ai-index-report](https://hai.stanford.edu/ai-index/2025-ai-index-report)

无法访问文章链接。

---

## 32. 3D陆军陆地导航课程

**原文标题**: 3D Army Land Navigation Courses

**原文链接**: [https://oe.tradoc.army.mil/oegames/landnav/index.html](https://oe.tradoc.army.mil/oegames/landnav/index.html)

OE Games推出3D陆军地形导航课程，提供森林和沙漠两种环境。推荐使用Edge、Chrome或Firefox浏览器以获得最佳体验。请注意，本游戏不支持Internet Explorer。如有技术问题，请发送邮件至[邮箱地址]。

---

## 33. R 语言大全

**原文标题**: Big Book of R

**原文链接**: [https://www.bigbookofr.com/](https://www.bigbookofr.com/)

R语言书大全：汇集了400多本免费或平价R语言编程书籍，力求成为用户唯一需要的R语言书签。网站鼓励用户通过GitHub或Google表单贡献书籍（免费和付费）。

作者Oscar感谢Fathom Data将网站转换为Quarto格式。本网站采用知识共享署名-非商业性使用-禁止演绎 3.0 许可协议。

该网站提供由Plausible驱动的实时、注重隐私的使用统计数据，彰显了对GDPR合规性的承诺。Oscar邀请读者在Mastodon或LinkedIn上联系，并订阅他的新闻通讯，以获取数据相关项目和书籍重大更新的最新信息。

---

## 34. 金融科技创始人被控欺诈；人工智能应用被发现是菲律宾人在操作

**原文标题**: Fintech founder charged with fraud; AI app found to be humans in the Philippines

**原文链接**: [https://techcrunch.com/2025/04/10/fintech-founder-charged-with-fraud-after-ai-shopping-app-found-to-be-powered-by-humans-in-the-philippines/](https://techcrunch.com/2025/04/10/fintech-founder-charged-with-fraud-after-ai-shopping-app-found-to-be-powered-by-humans-in-the-philippines/)

人工智能购物应用Nate创始人兼前CEO Albert Saniger 因涉嫌误导投资者关于该应用真实性能，被美国司法部指控犯有欺诈罪。Nate 曾从投资者那里筹集了超过 5000 万美元，声称其“人工智能”允许用户只需单击一下即可从任何电子商务网站购买商品。然而，美国司法部指控 Nate 在很大程度上依赖菲律宾的人工承包商来手动完成购买，自动化率实际上为 0%。

Saniger 被指控虚假宣称 Nate 的运营“没有人为干预”，除非在极端情况下。尽管聘请了数据科学家并收购了一些人工智能技术，但该应用的功能主要由人力驱动。《The Information》杂志 2022 年的一项调查此前曾强调 Nate 对人工承包商的使用。

据报道，Nate 耗尽了资金，并于 2023 年 1 月被迫出售其资产，导致投资者遭受重大损失。Saniger 目前的身份是 Buttercore Partners 的管理合伙人。

文章还指出，Nate 并非唯一一家被指控夸大其人工智能能力的初创公司，并列举了依赖大量人工的“人工智能”免下车软件和法律科技独角兽 EvenUp 的例子。

---

## 35. 揭秘 (Shebang): 内核探险

**原文标题**: Demystifying the (Shebang): Kernel Adventures

**原文链接**: [https://crocidb.com/post/kernel-adventures/demystifying-the-shebang/](https://crocidb.com/post/kernel-adventures/demystifying-the-shebang/)

本文深入探讨Linux内核如何通过Shebang (`#!`)机制处理脚本的执行。与普遍认知相反，Shebang并非由Shell本身解释，而是在`execve`系统调用期间由内核直接解释。

内核函数`fs/exec.c`中的`do_execveat_common`是入口点，进而调用`bprm_execve`和`search_binary_handler`。后者通过读取文件开头（最多256字节，由`BINPRM_BUF_SIZE`确定）并将它与已注册的格式（如ELF、FLAT和SCRIPT (`fs/binfmt_script.c`)）进行比较来识别可执行文件格式。

`binfmt_script.c`模块专门处理Shebang。如果检测到`#!`，内核会解析解释器路径，打开解释器可执行文件，并在进程映像中用解释器替换脚本文件。这意味着对脚本的单个`execve`触发内核查找并执行指定的解释器，并将脚本路径作为参数传递。

本文还涉及`binfmt_misc.c`，这是一种内核特性，允许通过将非本地二进制文件（如Java JAR）与基于魔术字节序列或文件扩展名的特定解释器关联来执行它们。

最后，本文解释了在*没有* Shebang的情况下运行Shell脚本是Shell实现的备用机制。Shell检测到来自失败的`execve`的`ENOEXEC`错误，然后使用`/bin/sh`显式执行脚本。文章最后演示了内核检查执行权限，如果权限被拒绝，则返回`EACCES`错误。

---

## 36. 为什么要轻拍奶酪轮？

**原文标题**: Why Tap a Wheel of Cheese?

**原文链接**: [https://www.cheeseprofessor.com/blog/cheese-wheel-tapping](https://www.cheeseprofessor.com/blog/cheese-wheel-tapping)

本文探讨了“巴提托里”（击打者）在确保帕尔马干酪质量方面发挥的关键作用。这些专业的品鉴师只有24位，他们在奶酪经过至少12个月的成熟期后，用小锤敲击每一块奶酪，仅凭声音来评估其内部结构。

作者克里斯汀·詹努齐在艾米利亚-罗马涅地区与两位巴提托里一起度过了一段时间：一位是年轻的学徒亚历山德罗·斯托基，另一位是经验丰富的资深人士兼前奶酪制造商雷纳托·朱迪奇。她了解到这项技能是通过学徒制传承的，经验丰富的巴提托里会指导新手解读每次敲击的细微差别。他们倾听均匀的声音，这表明内部结构紧密，没有裂缝或空洞。

巴提托里将奶酪分为三个质量等级。最优质的奶酪会获得官方的帕尔马干酪烙印。有轻微缺陷的奶酪仍会被烙印，但也会刻上平行线，以表明其质量较低，适合年轻时食用。有重大缺陷的奶酪会被剥夺所有识别标志，并作为普通餐桌奶酪出售。

虽然缺陷被视为瑕疵，但它们也突出了帕尔马干酪的手工特性，它是用生牛奶制成，并受到自然变化的影响。即使存在这些变化，绝大多数奶酪都能达到最高的质量标准。巴提托里强调，这个职业需要激情、尊重和不断学习的意愿。

---

## 37. Show HN: Koreo – Kubernetes 平台工程工具包

**原文标题**: Show HN: Koreo – A platform engineering toolkit for Kubernetes

**原文链接**: [https://koreo.dev/](https://koreo.dev/)

Koreo 是一款平台工程工具包，旨在简化和增强 Kubernetes 配置管理和资源编排。它通过可编程的工作流程和结构化数据赋能开发者，从而解决了 Helm 和 Kustomize 等工具的局限性。

主要功能包括：

*   **可编程工作流程：** 能够定义复杂的、事件驱动的流程来管理 Kubernetes 资源的生命周期。
*   **结构化配置管理：** 将 Kubernetes 配置视为结构化数据，以便更轻松地进行验证、转换和组合。
*   **动态资源实例化：** 允许注入值并组合来自各种来源的配置，以创建完整的资源视图。
*   **配置即函数：** 利用函数式编程原则来创建可重用的配置构建块。
*   **声明式 Operator 模型：** 通过定义期望状态并自动协调实际状态来简化管理。
*   **一流的测试和工具：** 提供内置的测试框架和 IDE 集成，用于早期错误检测和改进的开发者体验。

Koreo 旨在构建自定义内部开发者平台 (IDP)、自动化基础设施、实施统一控制平面、创建开发者抽象、启用多云基础设施即代码 (IaC)、促进 Operator 组合、编排部署以及强制执行策略即代码。

Koreo 由 Real Kinetic 开发，源于他们为各种组织（包括为 Workiva 构建内部平台）提供平台工程的经验。它还为 Real Kinetic 针对初创企业的预配置平台 Konfigurate 提供支持。

---

## 38. .localhost 域名

**原文标题**: .localhost Domains

**原文链接**: [https://inclouds.space/localhost-domains](https://inclouds.space/localhost-domains)

查尔斯·张伯伦描述了一种为本地Web应用程序创建自定义`.localhost`域的方法，使他能够使用像`appname.localhost`这样的名称访问它们，而不是`localhost:4333`。该设置包括三个步骤：

1. **Launchd守护进程：** 每个应用程序都被配置为监听唯一端口的launchd守护进程。

2. **/etc/hosts配置：** 编辑`/etc/hosts`文件，将来自自定义域（例如，`inclouds.localhost`）的流量重定向到`127.0.0.1`。

3. **Caddy反向代理：** Caddy，一个Web服务器，被配置为充当反向代理，将来自`127.0.0.1`针对指定域的流量重定向到应用程序正在监听的正确端口。例如，`inclouds.localhost`可能代理到`localhost:5050`。Caddy还处理TLS和压缩。

张伯伦表达了简化该过程的愿望，设想使用单个命令来安装或卸载应用程序，并自动配置必要的设置。他还提到了cristóbal的建议，即使用dnsmasq来获得更好的解决方案。

---

## 39. 她在哈佛实验室研究逆转衰老，直到被美国移民海关执法局拘留

**原文标题**: She Worked in a Harvard Lab to Reverse Aging, Until ICE Jailed Her

**原文链接**: [https://www.nytimes.com/2025/04/11/science/russian-scientist-ice-detained-harvard.html](https://www.nytimes.com/2025/04/11/science/russian-scientist-ice-detained-harvard.html)

俄罗斯科学家克谢尼娅·彼得罗娃，现年30岁，曾在哈佛医学院实验室从事细胞再生抗衰老研究，目前被拘留在路易斯安那州的一所监狱里。彼得罗娃因政治原因逃离俄罗斯来到美国。2月16日，她在洛根国际机场被拘留，原因是她应哈佛老板的要求从法国携带青蛙胚胎，但未向海关申报。

虽然这种违规行为通常只处以小额罚款，但海关官员取消了她的签证并启动了驱逐程序。彼得罗娃告知他们，由于她的政治活动，如果返回俄罗斯，她担心会被逮捕。她现在被关押在里奇伍德惩教中心，与大约90名其他移民女性（主要是无证工人）一起，等待美国政府对她案件的裁决。由于无法工作，她只能在允许的情况下读书和下棋来消磨时间。这篇文章突出了她重要的科学工作与她在特朗普政府强硬的移民政策下的困境之间的对比。

---

## 40. 我们为对性能要求极高的桌面应用选择了Tauri而非Electron

**原文标题**: We Chose Tauri over Electron for Our Performance-Critical Desktop App

**原文链接**: [https://gethopp.app/blog/tauri-vs-electron](https://gethopp.app/blog/tauri-vs-electron)

Costa Alexoglou 的文章《我们为何选择 Tauri 而非 Electron 开发对性能要求极高的桌面应用》详细阐述了 Hopp 决定使用 Tauri 开发其低延迟远程结对编程应用的原因。该文章比较了 Tauri 和 Electron，重点介绍了它们的架构差异、功能和性能基准。

Electron 捆绑了 Node.js 运行时并使用 Chromium 进行渲染，导致应用程序体积更大、内存使用率更高。事件处理依赖于 Node.js 事件循环。相反，Tauri 使用 Rust 作为后端，编译为原生二进制文件，并利用操作系统的 WebView 组件（Windows 上为 WebView2，macOS 上为 WKWebView，Linux 上为 WebKitGTK）。这导致更小的应用程序包和更低的内存占用，但也可能由于不同的 WebView 实现而引入潜在的跨平台 UI 不一致性。

基准测试表明，与 Electron 相比，Tauri 应用程序的软件包体积明显更小（8.6 MiB 对比 244 MiB），内存使用率更低（172 MB 对比 409 MB）。启动时间可以忽略不计。由于 Rust 编译，Tauri 的初始构建时间较慢。

Hopp 选择 Tauri 的主要原因是其卓越的视频流后端性能、易于管理用于屏幕共享和远程控制输入的独立进程（sidecar），以及 Tauri 的快速开发，特别是 Tauri v2 弥补了功能差距。虽然文章承认最佳选择取决于具体项目，但它为 Tauri 在对性能要求极高的桌面应用程序中的应用提出了令人信服的理由。

---

## 41. 詹姆斯·卡梅隆谈AI版权：人类是模型

**原文标题**: James Cameron on AI copyright: humans are models

**原文链接**: [https://nitter.space/vitrupo/status/1910484076978725140#m](https://nitter.space/vitrupo/status/1910484076978725140#m)

无法访问文章链接。

---

## 42. 了解美国电力中断

**原文标题**: Understanding US Power Outages

**原文链接**: [https://www.construction-physics.com/p/understanding-us-power-outages](https://www.construction-physics.com/p/understanding-us-power-outages)

本文利用Poweroutage.us的数据，分析了美国停电趋势，重点关注停电频率、区域差异和潜在原因。作者强调，停电很大程度上受到飓风、野火和冬季风暴等极端事件的影响，这些事件会导致停电时间显著增加。这些事件具有高度区域性，对某些地区产生巨大影响，而对其他地区则没有影响。

全国范围内，每个客户的停电时间可能呈上升趋势，由于飓风海伦和米尔顿的影响，2024年尤其糟糕。农村地区的停电情况往往比城市地区更严重。

去除极端事件的影响，可以揭示全国各地“基线”可靠性的差异。阿肯色州、密西西比州和德克萨斯州的部分地区，以及其他地区，始终显示出较高的停电率，而中西部和新英格兰南部的情况较好。达拉斯、费城和湾区等一些大都市地区的基线可靠性似乎正在恶化，而其他地区的基线可靠性相对稳定。菲尼克斯、迈阿密和洛杉矶表现出良好的基线可靠性。

该分析还发现了季节性趋势，停电高峰出现在夏季和冬季，这可能与天气和能源消耗模式有关。最后，作者得出结论，极端事件正变得越来越频繁，停电情况因地区而异。

---

## 43. macOS 9 版 SDL2 “草稿”

**原文标题**: SDL2 for macOS 9 “rough draft”

**原文链接**: [https://macintoshgarden.org/apps/sdl2-macos-9-rough-draft](https://macintoshgarden.org/apps/sdl2-macos-9-rough-draft)

无法访问文章链接。

---

## 44. Rust 编译器中一个令人惊讶的枚举大小优化

**原文标题**: A surprising enum size optimization in the Rust compiler

**原文链接**: [https://jpfennell.com/posts/enum-type-size/](https://jpfennell.com/posts/enum-type-size/)

James Fennell 的博文深入探讨了 Rust 编译器中一个令人惊讶的枚举大小优化，它超越了广为人知的“空指针优化”。枚举作为其变体的“或”组合，其大小通常由最大的变体有效载荷加上一个指示哪个变体处于活动状态的标签来确定。

当只有一个变体具有有效载荷时，例如 `Option<char>`，空指针优化就会起作用。 Rust 重用无效的 `char` 值（空位）来表示 `None`，从而消除了对单独标签的需求。

令人惊讶的优化出现在嵌套枚举中。 考虑具有变体 `A(u32)` 和 `B(u32)` 的 `Inner`，它占用 8 个字节（标签 4 个字节，有效载荷 4 个字节）。 现在，`Outer` 具有变体 `C(u32)` 和 `D(Inner)`。 人们会期望 `Outer` 为 12 字节（`Inner` 为 8 字节，标签为 4 字节）。 然而，Rust 将其优化为 8 个字节。

这种优化之所以有效，是因为编译器识别出 `Inner` 枚举的标签仅使用一小部分值（0 或 1）。 通过巧妙地分配 `Outer` 的标签，编译器在 `Outer` 枚举的表示中重用 `Inner` 枚举的标签空间。 如果 `Outer` 标签与 `Inner` 标签匹配，则该变体为 `Outer::D`，并且整个位模式代表 `Inner` 值。 否则，该值是另一个 `Outer` 变体，有效载荷存储在剩余的位中。 这消除了冗余的标签空间并减少了内存使用。

---

## 45. 大量的YAML

**原文标题**: That's a Lot of YAML

**原文链接**: [https://noyaml.com/](https://noyaml.com/)

这篇题为《YAML太多了》的文章，以幽默且批判的视角审视 YAML 配置语言，突出了其常见的陷阱和怪异之处，这些陷阱和怪异之处常常导致开发人员的沮丧。作者认为，尽管 YAML 得到了广泛应用，尤其是在 DevOps 环境中，但它的模糊性和意想不到的行为可能会导致严重的问题。

文章列举了几个 YAML 问题的例子，包括如何将“NO”误解为布尔值，将看似无害的字符串转换为数字（例如，“08”），并将时间格式视为自午夜以来的秒数。文章还涉及与可执行 YAML 相关的安全漏洞、使用不同 CI/CD 系统的复杂性以及编码八进制数的问题。

作者提供了外部文章和资源的链接，这些文章和资源也表达了对 YAML 缺点的类似看法。这些资源包括对 YAML 在不同实现中解析不一致、过度冗长以及引入难以调试的错误的可能性的批评。文章还指出了替代配置语言和 DevOps 方法，这些方法可能提供更可靠且不易出错的体验。文章最后以自嘲的幽默结束，根据用户反馈，作者有意创建了一个像 YAML 一样难以使用的网站。

---

## 46. 奥地利香烟收藏

**原文标题**: The Austrian Cigarette Collection

**原文链接**: [http://www.zigsam.at](http://www.zigsam.at)

《奥地利香烟收藏》标题表明该文章可能侧重于奥地利香烟相关物品的收藏。鉴于文章内容仅说明“ZIGSAM - 奥地利香烟收藏”，无法提供更详细的摘要。在没有任何进一步信息的情况下，人们只能推断该文章*可能*会讨论奥地利香烟历史、品牌、包装、广告和/或收藏实践的各个方面。ZIGSAM可能是收藏本身的名称，与收藏相关的公司，或奥地利香烟收藏界使用的术语。简而言之，核心要点是存在一个以奥地利香烟为中心的专门收藏。

---

## 47. 用声音悬浮昆虫或可变革科学摄影

**原文标题**: Levitating Bugs with Sound Could Transform Scientific Photography

**原文链接**: [https://petapixel.com/2025/03/25/levitating-bugs-with-sound-could-transform-scientific-photography/](https://petapixel.com/2025/03/25/levitating-bugs-with-sound-could-transform-scientific-photography/)

科学家开发出新型声悬浮摄影测量成像系统，可在不造成损伤的情况下拍摄昆虫标本的详细照片。该系统利用精确控制的声波悬浮昆虫，从而能够从多个角度自动捕获图像。这种方法克服了传统技术（如插针）的局限性，插针会损坏标本，且不适用于最小的昆虫。

德国几家机构的研究人员证明，声悬浮可用于科学摄影，提供了一种可控的方式来操纵标本并以预定义的角度拍摄图像。该系统能够实现自动焦点堆叠，生成具有扩展景深的高度详细的照片，并有助于创建 3D 模型，无需手动重新定位或造成损坏。

该成像系统使用 Olympus OM-D E-M1 III 相机、90 毫米微距镜头和增距镜，在每个标本位置拍摄 40 张照片，并在 72 个视角重复拍摄。这种全面的数据集无需插针，防止损坏，并允许完整查看标本。它还可以对小到无法插针的昆虫进行成像。

尽管承认目前存在单轴旋转等局限性，但研究人员认为，这种非破坏性的自动化成像系统在小型物体的近距离摄影测量方面显示出巨大的潜力，并为 3D 重建奠定了基础。收集的数据对于训练用于昆虫识别和生物多样性研究的人工智能模型非常有价值。

---

## 48. 低成本高速HDMI视频数据采集

**原文标题**: Low cost, high speed data acquisition over HDMI [video]

**原文链接**: [https://media.ccc.de/v/osmodevcon2024-200-low-cost-high-speed-data-acquisition-over-hdmi](https://media.ccc.de/v/osmodevcon2024-200-low-cost-high-speed-data-acquisition-over-hdmi)

史蒂夫·马克格拉夫在osmodevcon2024上的演讲探讨了一种使用现成硬件进行高速数据采集的低成本方法。核心思想是改造廉价的USB 3.2 HDMI视频采集卡，特别是那些基于Macrosilicon MS2130芯片的采集卡，并结合像Sipeed Tang nano系列这样的小型FPGA开发板。 这两种组件的价格都可以控制在每个10美元左右。

该演讲详细介绍了一项逆向工程，该工程允许通过HDMI连接的这些组件用于捕获任意数据。 通过将数据编码为视频信号并通过HDMI传输到采集卡，并使用FPGA创建适当的HDMI输出，用户可以构建各种应用程序。

该演讲提出了潜在的应用，例如低成本、高速逻辑分析仪、ADC采集设备，甚至是DIY软件无线电（SDR）。 演讲者提供了可下载的资源，包括演讲的视频和音频录音。

---

## 49. 通过传输激活值控制语言和扩散模型

**原文标题**: Controlling Language and Diffusion Models by Transporting Activations

**原文链接**: [https://machinelearning.apple.com/research/transporting-activations](https://machinelearning.apple.com/research/transporting-activations)

本文重点介绍了苹果公司用于控制大型生成式语言和文本到图像模型输出的新技术——激活传输(AcT)。AcT以最小的计算开销提供对模型行为的细粒度控制，解决了诸如RLHF和指令微调等资源密集型方法的局限性。

AcT是一个模态无关的框架，它利用最优传输理论来引导模型激活，从而推广了先前的激活引导方法。与可能将激活移出分布的先前方法不同，AcT学习源激活分布和目标激活分布之间的最优传输映射，确保转移后的激活符合目标分布。简化版本Linear-AcT使用线性映射来实现快速推理。

本文展示了Linear-AcT在控制LLM输出方面的有效性，特别是在减少毒性和诱导真实性方面，同时对其他性能指标的影响最小。它还展示了AcT控制文本到图像扩散模型的能力，从而可以对图像细节和艺术风格进行细粒度的调整。一个关键应用是去除不需要的概念，例如防止模型生成包含用户明确指示要避免的元素（例如，“粉色大象”）的图像。

AcT为控制生成模型提供了一种高效且可靠的解决方案，为寻求改进模型输出与用户期望的对齐并减轻潜在滥用的研究人员和从业者提供了一种有价值的工具。

---

## 50. Phoenix 1.8.0-RC 发布

**原文标题**: Phoenix 1.8.0-RC Released

**原文链接**: [https://www.phoenixframework.org/blog/phoenix-1-8-released](https://www.phoenixframework.org/blog/phoenix-1-8-released)

Chris McCord 宣布 Phoenix 1.8 发布候选版，强调改进开发者体验和安全性。主要特性包括：

*   **使用 daisyUI 的 Tailwind 主题：** 增强了 Tailwind 支持，采用 daisyUI 实现灵活的组件主题和一致的样式，可通过配置轻松自定义。
*   **魔法链接认证：** phx.gen.auth 现在默认使用无密码的魔法链接登录/注册，提供用户友好的安全性。 传统的密码认证仍然是可选的。`require_sudo_mode` plug 强制要求对敏感操作进行最近的身份验证。
*   **用于安全数据访问的 Scopes：** 引入 Scopes 作为安全数据访问和授权的一流模式。 生成器现在使用 scopes 来确保默认情况下锁定数据访问。Scopes 还有助于您的接口随着应用程序需求的增长而增长。
*   **简化的 Onboarding：** 简化了代码生成器（phx.gen.live，phx.gen.auth），为经验丰富的开发人员提供更好的基础，并为新手提供更轻松的学习体验。核心组件已精简到主要构建块。
*   **简化的布局：** Phoenix 现在倾向于使用单个布局并辅以函数组件，从而简化了创建和管理布局的过程。 应用布局现在是一个显式的函数组件调用，无论您想要包含动态应用布局的地方。

此次更新还包括新的身份验证/授权指南和弃用。 该版本需要 Erlang/OTP 25+。 开发人员可以通过 mix archive install 或 new.phoenixframework.org 尝试它。

---

## 51. 使用AI Gemini 2.5 Pro构建的雅达利导弹指挥官游戏

**原文标题**: Atari Missile Command Game Built Using AI Gemini 2.5 Pro

**原文链接**: [https://missile-command-game.centminmod.com/](https://missile-command-game.centminmod.com/)

本文介绍了一款使用现代HTML5 Canvas技术重制的经典Atari游戏《导弹司令》。该游戏借助Google Gemini 2.5 Pro和Claude 3.7 Sonnet构建，保留了原作的核心玩法，并进行了现代化的增强。

主要功能包括一个游戏内商店，玩家可以在其中购买诸如声波、巨型炸弹、卫星防御基地等强化道具，以及更快的导弹和更大的爆炸范围等各种升级。玩家通过点击/触摸发射导弹来防御城市免受来袭攻击，并可以通过选择图标然后选择目标区域来使用特殊武器。空格键可以暂停/恢复游戏。

游戏提供难度选择（简单、普通、困难、疯狂），并通过托管在Cloudflare上的排行榜来跟踪高分。游戏还通过Cloudflare AI Gateway与OpenRouter AI相结合，进行游戏分析。该项目由George Liu开发，并托管在Cloudflare Pages上。本文提供了有关游戏控制、制作人员名单和技术细节的信息，包括指向开发者GitHub存储库的链接。

---

## 52. Arroyo (YC W23) 已被 Cloudflare 收购。

**原文标题**: Arroyo (YC W23) has been acquired by Cloudflare

**原文链接**: [https://www.arroyo.dev/blog/arroyo-is-joining-cloudflare](https://www.arroyo.dev/blog/arroyo-is-joining-cloudflare)

"Arroyo (YC W23) 被 Cloudflare 收购" 摘要：

实时数据处理初创公司 Arroyo，致力于构建分布式流处理引擎，已被 Cloudflare 收购。Arroyo 在参与 Y Combinator Winter 2023 批次后成立，旨在简化并普及对强大流处理能力的访问。

该博客文章宣布了此次收购，并表达了 Arroyo 团队加入 Cloudflare 的兴奋之情。他们相信 Cloudflare 的全球基础设施、资源以及构建更好互联网的使命将显著加速他们最初的愿景。虽然收购的具体条款未公开，但文章强调 Arroyo 的技术和团队将整合到 Cloudflare 的生态系统中。

Arroyo 旨在解决的核心问题是构建和维护实时数据管道的复杂性和成本。与现有替代方案相比，他们的流处理引擎提供了一种更高效、更易于访问的解决方案。这与 Cloudflare 提供高性能、安全可靠互联网服务的使命相一致。

此次收购可能意味着 Cloudflare 将利用 Arroyo 的技术来增强其现有的数据处理能力，可能会提供新的服务或提高现有服务的性能。这可能会转化为 Cloudflare 客户的利益，特别是那些依赖实时数据分析和流媒体应用程序的客户。Arroyo 团队对未来以及他们在 Cloudflare 中能够实现的影响表示乐观。

---

## 53. 美国的金融体系一度濒临崩溃。

**原文标题**: America's financial system came close to the brink

**原文链接**: [https://www.economist.com/finance-and-economics/2025/04/10/americas-financial-system-came-close-to-the-brink](https://www.economist.com/finance-and-economics/2025/04/10/americas-financial-system-came-close-to-the-brink)

2025年4月9日，美国的金融体系濒临全面崩溃的边缘。股价的长期下跌因美国国债市场剧烈的不稳定性而加剧。十年期国债收益率在几天内从3.9%飙升至4.5%，表明债券价格大幅下跌。这种风险资产（股票）和通常安全的资产（国债）的同时崩溃，威胁到整个金融体系的稳定。文章强调了局势的危险性，指出债券市场的剧烈波动和其他金融压力信号正在发出红色警报。其他相关文章在更广泛的金融环境下提到了唐纳德·特朗普的关税以及中国潜在的经济武器，如稀土出口。虽然投资者最初因特朗普暂停关税而感到宽慰，但随着中国的回应，现实最终降临。

---

## 54. 树莓派集群现身6000美元音频处理器中

**原文标题**: Raspberry Pi cluster spotted inside $6k audio processor

**原文链接**: [https://www.jeffgeerling.com/blog/2025/raspberry-pi-cluster-spotted-inside-6k-audio-processor](https://www.jeffgeerling.com/blog/2025/raspberry-pi-cluster-spotted-inside-6k-audio-processor)

本文重点介绍了树莓派集群在高端商业产品中的出人意料的应用，特别是价值6,000美元至15,000美元之间的Orban Optimod 5000系列音频处理器。每个处理器都包含一个3节点的树莓派集群。其中一个树莓派管理远程控制、Web UI、固件更新和本地显示。第二个树莓派独立处理多流音频，即使显示/远程访问树莓派出现问题，也能确保持续的功能。第三个可选的树莓派用于为音频流添加水印，用于Luminate/SoundScan评级等数据。

作者认为，使用树莓派计算模块（CM4/CM5）提供了一种经济高效且可靠的方式，可以为现有的音频/视频/射频处理架构添加现代Linux支持和远程控制功能。虽然存在替代方案，但树莓派为强化的Linux镜像提供最低的功耗和长期的供应商支持。文章指出，这并非孤例，在NAB展会上，许多昂贵的设备都在内部使用了树莓派。

评论区揭示了树莓派在其他昂贵设备中的类似应用，例如一台价值30万美元、运行在12个树莓派4上的3D打印机，以及由单个CM4驱动的Formlabs Form 4 3D打印机。

---

## 55. 使用Lit构建WebComponents的理由

**原文标题**: The Case for WebComponents with Lit

**原文链接**: [https://typescript.guru/the-case-for-web-components-with-lit/](https://typescript.guru/the-case-for-web-components-with-lit/)

本文提倡使用 Web Components，特别是 Lit 库，作为一种与框架无关且高效的方式来构建可复用的 UI 元素。Web Components 利用原生浏览器标准，如 Custom Elements、Shadow DOM 和 HTML Templates，具有原生浏览器支持、强大的封装性、框架兼容性（React、Angular、Vue）、可扩展性和可维护性等优势。

Lit 通过诸如响应式属性、声明式模板、快速更新、TypeScript 支持和生命周期钩子等特性简化了 Web Component 的创建。本文强调了将 TypeScript 与 Lit 结合使用的优势，包括类型安全的属性、接口驱动的开发、增强的 IDE 支持和编译时验证。

一个全面的 TypeScript 示例演示了如何构建一个 `UserCard` 组件，展示了属性装饰器、状态管理、生命周期方法、指令和事件处理。本文还介绍了使用插槽进行组件组合、使用响应式控制器进行状态管理以实现可重用逻辑，以及使用 `@open-wc/testing` 测试 Web Components。

文中讨论了诸如高效的属性更新、模板缓存和指令使用等性能优化方法。最后，本文重点介绍了设计系统等实际应用案例，提供了一个 `DSButton` 组件示例，并说明了与 React 和 Vue 的集成。

---

## 56. 市政消防车和机场消防车的区别

**原文标题**: The Difference Between Municipal Fire Trucks and Airport Fire Trucks

**原文链接**: [https://www.piercemfg.com/pierce/blog/difference-between-municipal-and-airport-fire-trucks](https://www.piercemfg.com/pierce/blog/difference-between-municipal-and-airport-fire-trucks)

皮尔斯制造公司博客：市政消防车与机场消防车（ARFF车辆）的主要区别

皮尔斯制造公司的这篇博客文章概述了市政消防车和机场消防车（ARFF车辆）之间的主要区别。虽然两者都服务于紧急消防需求，但它们的设计和功能是根据其特定环境量身定制的。

市政消防车专为城市、郊区和乡村环境设计，水箱大小（500-1000加仑）和隔间数量根据供水基础设施和处理的呼叫类型（建筑物火灾、交通事故等）而有所不同。速度至关重要，需要在25秒内加速到35英里/小时，最高速度为50英里/小时。

另一方面，ARFF车辆专门用于机场紧急情况，包括飞机坠毁、燃料泄漏和航站楼事故。由于航空燃料的易燃性，它们需要快速响应时间（在3分钟内到达现场）和更高的加速标准（0-50英里/小时在25秒内，最高速度为70英里/小时）。ARFF消防车携带更大的水箱（1500-4500加仑），并使用高空延伸炮塔（HRET）进行精确的灭火。它们使用水、消防泡沫和干粉化学品作为灭火剂。

驾驶室设计也大不相同。市政驾驶室优先考虑消防员的运输和舒适性，而ARFF驾驶室则强调在复杂的机场环境中能见度和机动性，通常采用居中的操作员座椅。这两种类型的卡车都配备了存储解决方案，这些解决方案是根据其特定任务所需的设备量身定制的，并纳入了减少致癌物的措施。

---

## 57. 还记得 FastCGI 吗？(2021)

**原文标题**: Remember FastCGI? (2021)

**原文链接**: [https://brokenco.de/2021/06/27/remember-fastcgi.html](https://brokenco.de/2021/06/27/remember-fastcgi.html)

本文回顾了FastCGI，一种用于运行长生命周期进程来处理多个Web请求的协议，并将其与CGI和“无服务器”函数进行对比。尽管FastCGI在PHP社区中仍然在使用，但作者探讨了其在现代Web开发中的相关性，特别是使用Rust的情况。

作者尝试了Rust中的`fastcgi` crate，创建了一个简单的服务器，响应“Hello, world!”。为了测试，他们配置了Docker中的Nginx，将请求代理到FastCGI服务器。

然而，作者得出结论，设置FastCGI涉及大量的进程管理和Web服务器配置。然后，他们提出了一个使用Rust的Tide Web框架的替代方案，演示了一个功能等效的程序，该程序更容易设置和测试，因为它可以在不需要初始反向代理的情况下直接访问。无论代理FastCGI还是标准HTTP服务器，Nginx的配置都类似。

最终，作者认为，FastCGI对于HTTP请求处理速度慢或不安全的脚本语言可能仍然有用。但对于大多数现代应用程序来说，使用嵌入式HTTP Web服务器，如Rust中的Tide，是一种更简单、更有效的方法。文章强调，HTTP已经在通用Web开发中“胜出”。

---

## 58. 如果你的网站有营业时间会怎样？ (2022)

**原文标题**: What if your website had business hours? (2022)

**原文链接**: [https://bobbiechen.com/blog/2022/7/21/what-if-your-website-had-business-hours](https://bobbiechen.com/blog/2022/7/21/what-if-your-website-had-business-hours)

如果你的网站有营业时间会怎样？

Bobbie Chen 的文章“如果你的网站有营业时间会怎样？”探讨了限制网站可用性的非传统想法，并将之与实体店进行了类比。灵感源于 B&H Photo，其在线商店会在周六因宗教原因关闭。

该文章挑战了通过简单地将收入除以停机时间来计算宕机成本的标准电子商务做法，认为并非所有潜在客户都会立即流失。B&H 的成功表明，一些客户会稍后返回。这也让人想起一个 Google SRE 的轶事，即有意触发“Chubby”服务的轻微中断，有助于用户为潜在的故障做好准备。

其他具有有限可用性的网站示例包括 Low-Tech Magazine（太阳能供电）和 Kingdom of Loathing（定期维护）。该文章强调，这些例子之所以能够蓬勃发展，是因为它们提供了独特的服务，并且客户愿意等待。

Chen 随后以一种轻松的方式考察了在计划停机期间缩减服务器规模可能节省的成本。然而，考虑到与潜在收入损失以及持续需要待命支持相比，节省的成本微乎其微，该文章承认了这种想法对于大多数企业来说是不切实际的。最终，作者承认全天候在线模式是有充分理由的主流标准。

---

## 59. 人工清点集会图像显示人数明显偏少。

**原文标题**: Hand-counted images of rallies yield significantly smaller numbers

**原文链接**: [https://www.cbc.ca/news/canada/liberal-conservative-crowd-size-investigation-1.7507222](https://www.cbc.ca/news/canada/liberal-conservative-crowd-size-investigation-1.7507222)

加拿大广播公司新闻调查发现，保守党和自由党在加拿大政治集会上严重夸大了参与人数。调查使用手工计数图像和专家分析，重点关注了四场集会：保守党在不列颠哥伦比亚省萨里和埃德蒙顿附近的活动，以及自由党在多伦多和不列颠哥伦比亚省里士满的活动。

调查显示，声称的参与人数与实际人数之间存在巨大差异。例如，保守党声称埃德蒙顿地区集会有 15,000 名参与者，但加拿大广播公司新闻在一张全景照片中数出大约 1,558 人。人群动力学专家 G. Keith Still 证实了这些发现，称 15,000 人的说法“不可能”。同样，自由党声称里士满有 2,000 名参与者，而实际人数接近 800 人。

该方法包括将图像分成网格并手动计数头部，将竞选照片与社交媒体上的视频进行交叉引用，以统计被遮挡的个人。虽然承认存在误差的可能性，但 Still 证实手工计数是最可靠的方法。

保守党竞选团队为其数字辩护，称其“计算了回复者以及进入场地的人”，并指出皇家骑警对埃德蒙顿集会的“一般估计”为 9,000-12,000 人。自由党声称其“最大限度地利用了活动场地的容量”。 双方均未提供具体证据来支持其说法。

尽管存在差异，但文章的结论是，集会参与人数可能与选举成功没有直接关系，而夸大的数字通常用于公共关系目的，旨在描绘一个拥挤和热情的场景。

---

## 60. Crystal 1.16.0

**原文标题**: Crystal 1.16.0

**原文链接**: [https://crystal-lang.org/2025/04/09/1.16.0-released/](https://crystal-lang.org/2025/04/09/1.16.0-released/)

Crystal 1.16.0于2025年4月9日发布，包含19位贡献者的162项变更。此版本包含多项重大更改，主要用于修复不正确的行为。这些更改包括`File.match?`的更正实现，引入了非贪婪匹配和正确的转义字符识别，弃用了参数名称的`?`和`!`后缀，更改了`Enumerable#sum`和`#product`，要求为联合类型指定显式的初始值类型，修复了`HTTP::Request`中的HTTP资源字符串解析，以及子命令的环境变更。

一个主要的亮点是RFC 0002中执行上下文的预览功能，提供了改进的多线程支持，并在各种操作系统和架构上进行了测试。其他语言增强功能包括`Slice.literal`推断元素类型并在解释器中工作，以及`macro sizeof`和`alignof`提供有关稳定类型的信息。标准库看到了路径处理的改进，尤其是在Windows上，以及新方法`Indexable#find`和`#find!`以及`EventLoop#wait_readable`、`#wait_writable`。编译器CLI现在接受`--output`来指定输出位置，遵循`$MACOSX_DEPLOYMENT_TARGET`，并且文档生成器可以通过`:showdoc:`包含私有/受保护对象和lib绑定。此版本还更新到LLVM 20并弃用了LLVM::ABI。

---

## 61. 用于快速存储的巨像

**原文标题**: Colossus for Rapid Storage

**原文链接**: [https://cloud.google.com/blog/products/storage-data-transfer/how-the-colossus-stateful-protocol-benefits-rapid-storage](https://cloud.google.com/blog/products/storage-data-transfer/how-the-colossus-stateful-protocol-benefits-rapid-storage)

谷歌云快速存储利用谷歌内部文件系统Colossus，在对象存储的可扩展性的基础上，提供亚毫秒级延迟和面向文件的语义。通过使用基于状态的gRPC流式协议，快速存储克服了通常与对象存储相关联的更高延迟和缺乏类文件行为的问题。

关键在于Colossus的状态协议。客户端获取包含文件存储位置信息的句柄，从而能够与磁盘进行直接、优化的通信以进行读写操作。这种架构实现了超低延迟和持久化追加，这对于数据库（如Spanner和Bigtable）以及流式分析（如BigQuery）至关重要。数据跨磁盘复制，并采用基于仲裁的写入方式，以保证持久性。

快速存储在此基础上，在流创建时预先加载授权和元数据访问，从而允许后续的读/写操作直接与Colossus交互。这实现了每秒数百万次的请求，尤其有利于需要快速、范围读取和持久化追加的AI/ML工作负载。新的流可以接管先前客户端的对象所有权，即使出现中断也能确保数据正确性。

将快速存储集成到 Cloud Storage FUSE 中提供了类文件访问，进一步实现了低延迟的面向文件的工作负载。它原生支持分层命名空间，以增强性能和面向文件夹的 API。用例包括 AI/ML 训练、分布式数据库优化、批量和流式分析、视频直播以及日志/监控。

---

## 62. systemd ParticleOS

**原文标题**: systemd ParticleOS

**原文链接**: [https://github.com/systemd/particleos](https://github.com/systemd/particleos)

ParticleOS：一个使用mkosi构建的可定制、不可变Linux发行版。与其他不可变发行版不同，用户可以自行构建和签名镜像，从而完全控制基础发行版（目前支持Arch或Fedora）和已安装的软件包。该过程包括配置`mkosi.local.conf`以定义所需的配置文件（例如，桌面、KDE），然后运行`mkosi -f`来构建镜像。

更新通过克隆ParticleOS存储库、根据需要修改`mkosi.local.conf`以及运行`mkosi -ff sysupdate --update --reboot`来处理。

文章还详细介绍了如何集成更新的systemd版本，可以通过启用Open Build Service systemd存储库的`obs`配置文件，或者从源代码构建systemd，然后配置mkosi以合并构建的工件。

安全是首要考虑，通过用户签名的安全启动镜像来实现，并提供有关生成和管理密钥的说明，这些密钥可能存储在智能卡上。安装涉及从使用`mkosi burn`创建的USB驱动器启动，使用“Installer”UKI配置文件，并运行`systemd-repart`来安装ParticleOS。

最后，文档提供了有关配置systemd-homed以获得最佳性能的指导，包括禁用自动调整大小、启用LUKS discard以及添加用于压缩和子卷管理的BTRFS挂载选项。对于使用mkosi vm的虚拟机部署，为了方便起见，设置了默认的root密码和用户。

---

## 63. 黑客新闻的无声拥抱

**原文标题**: Hacker News Hug of Deaf

**原文链接**: [https://susam.net/hn-bell.html](https://susam.net/hn-bell.html)

Susam Pal 在他的服务器上设置了一个简单的 netcat 循环，创建了一个“Hacker News 的聋子拥抱”。这个循环会接受连接，发送一条“ok”消息，关闭连接，并触发四个终端蜂鸣声。该实验的灵感来自 Hacker News 上关于古怪警报系统的讨论。

在分享了这个一行命令后，HN 社区开始连接到 susam.net:8000，导致 24 小时内超过 4761 个连接和 19044 声蜂鸣。虽然数量不大，但看到人们参与到这个项目中并让他的终端反复发出蜂鸣声，令人感到兴奋。

Pal 强调说，这个实验毫无意义但很有趣，突出了探索计算机领域中那些古怪想法的价值，而不仅仅是解决问题。乐趣在于探索和共享的体验。

五天后的更新显示，在 Pal 在 Hacker News 上分享这篇文章后，出现了第二次连接激增。这次，他收到了超过 30 万个连接，其中许多来自持久的客户端循环。他觉得这种增加的活动令人愉快。这篇文章的标签为 #unix, #shell, #networking, 和 #technology。

---

## 64. Show HN: 我做了一个管理和比较信用卡返利的工具

**原文标题**: Show HN: I built a tool to manage and compare credit card rewards

**原文链接**: [https://rewards.getonecard.io](https://rewards.getonecard.io)

此“Show HN”帖子介绍了一款旨在帮助用户最大化信用卡奖励的工具。其核心功能围绕允许用户将现有信用卡输入工具内的“数字钱包”展开。该工具随后使用人工智能分析用户的信用卡，并推荐用于特定商户的最佳信用卡，确保用户获得尽可能多的奖励。

该界面似乎强调“奖励优化器”，用户可以在其中搜索商户并立即查看钱包中的哪张卡提供最佳奖励率（例如，餐厅消费可获得4倍积分）。示例屏幕截图展示了针对各种商户（如“Home Slice Pizza”、“Powder Room Bar”和“Fairmont Austin”）的推荐，表明该工具涵盖了广泛的消费类别。“商户搜索”中的“旅行”部分暗示了可能专注于旅行相关奖励。本质上，该工具旨在通过提供基于个人卡包的个性化推荐来简化信用卡奖励管理。

---

## 65. 拥有我的数据，第一部分：集成自托管日历解决方案

**原文标题**: Owning my own data, part 1: Integrating a self-hosted calendar solution

**原文链接**: [https://emilygorcenski.com/post/owning-my-own-data-part-1-integrating-a-self-hosted-calendar-solution/](https://emilygorcenski.com/post/owning-my-own-data-part-1-integrating-a-self-hosted-calendar-solution/)

文章“拥有自己的数据，第一部分：集成自托管日历解决方案”详细介绍了 Emily Gorcenski 从 Google 日历迁移到自托管解决方案，以更好地控制其个人数据的过程。她概述了此举背后的动机，主要是对数据隐私的担忧以及对大型科技公司日益增长的依赖。

Emily 选择了 Nextcloud 作为她的自托管平台，该平台包含一个日历应用程序。这篇文章侧重于将 Nextcloud 的日历与其现有工作流程集成的技术方面。这包括：

*   **设置 Nextcloud:** 她概述了在自己的服务器上安装和配置 Nextcloud 的过程。
*   **导入现有事件:** 她描述了将她的日历数据从 Google 日历导出并导入到 Nextcloud 的步骤。这涉及将日历导出为 .ics 格式，并将 .ics 文件导入到她的 Nextcloud 日历中。
*   **同步:** 她讨论了将 Nextcloud 日历与她的设备（手机、笔记本电脑）同步的挑战。她解释了如何配置 CalDAV 以在多个设备上同步她的日历。
*   **未来考虑:** 她暗示未来的文章将深入探讨数据所有权的其他方面，例如联系人、笔记和其他个人数据。

总的来说，自托管日历解决方案是可行的，并且可以更好地控制自己的数据，但这需要技术专业知识以及对服务器管理和同步协议的理解。这篇文章对于那些考虑类似举动的人来说是一份实用的指南，并强调了所涉及的益处和挑战。

---

## 66. 细胞正在交换线粒体。这对我们的健康意味着什么？

**原文标题**: Cells are swapping their mitochondria. What does this mean for our health?

**原文链接**: [https://www.nature.com/articles/d41586-025-01064-5](https://www.nature.com/articles/d41586-025-01064-5)

线粒体转移：多细胞细胞器？

本文探讨了新兴的线粒体转移领域，挑战了传统观念中线粒体作为静态的、仅限于细胞内的细胞器的看法。研究表明，线粒体可以在细胞之间移动，可能发挥着“多细胞细胞器”的作用。

科学家们在不同的生物和细胞类型中观察到了这种转移，但确切原因尚不清楚。可能的假设包括：

*   **细胞损伤控制：** 为受损或受压力的细胞提供能量和支持，帮助组织修复、免疫反应和细胞存活。
*   **癌症优势：** 使癌细胞能够操纵其环境。

虽然尚未在人体内直接观察到线粒体转移，但研究人员正在研究其治疗癌症和中风等疾病的潜力。线粒体除了作为能量生产者外，还参与细胞通讯和免疫反应。它们的细菌起源可能解释了其动态行为，类似于细菌在细胞之间传播。

研究表明，线粒体通过隧道纳米管或囊泡进行转移，并可在血液中自由漂浮。具体例子包括：

*   星形胶质细胞在中风后向神经元捐赠线粒体，提高神经元存活率。
*   间质细胞在肺损伤期间向肺细胞转移线粒体，促进恢复。
*   血小板向干细胞转移线粒体，加速伤口愈合。
*   星形胶质细胞向大脑血管内壁细胞转移线粒体，维持血脑屏障。
*   白色脂肪细胞向巨噬细胞转移线粒体，影响能量消耗。

文章强调了捐赠线粒体对T细胞的抗炎作用，并呼吁进一步研究，以了解其潜在机制以及线粒体转移对人类健康和疾病的更广泛影响。

---

## 67. 英伟达新型Llama-3.1 Nemotron Ultra以一半的规模超越DeepSeek R1。

**原文标题**: Nvidia's new Llama-3.1 Nemotron Ultra outperforms DeepSeek R1 at half the size

**原文链接**: [https://venturebeat.com/ai/nvidias-new-llama-3-1-nemotron-ultra-outperforms-deepseek-r1-at-half-the-size/](https://venturebeat.com/ai/nvidias-new-llama-3-1-nemotron-ultra-outperforms-deepseek-r1-at-half-the-size/)

英伟达发布Llama-3.1-Nemotron-Ultra-253B-v1，一款基于Meta Llama-3.1模型的完全开源大型语言模型(LLM)，专为高级推理、指令遵循和AI助手工作流程而设计。这款拥有2530亿参数的模型在几个关键基准测试中超越了DeepSeek R1，一款拥有6710亿参数的先进混合专家(MoE)模型，尽管其规模不到后者的一半。

英伟达通过神经架构搜索(NAS)优化了模型架构，降低了内存占用和计算需求，同时保持了强大的性能。它支持开启和关闭推理模式，允许开发者在高复杂性推理任务和更简单的输出之间切换。后期训练包括监督微调、强化学习、知识蒸馏和持续预训练，从而提高了其在数学、编码和通用问答等领域的性能。

基准测试结果表明，启用推理后性能显著提升，尤其是在MATH500、AIME25、LiveCodeBench和GPQA中。与DeepSeek R1相比，英伟达的模型在GPQA、IFEval和LiveCodeBench中表现出具有竞争力或更优异的结果，而DeepSeek R1在AIME25和MATH500等数学评估中表现略好。

该模型与Hugging Face Transformers兼容，支持高达128,000个token的序列，适用于各种LLM用例，包括聊天机器人、AI代理、RAG和代码生成。根据Nvidia开放模型许可证发布，并受Llama 3.1社区许可协议管辖，它已准备好用于商业用途，英伟达强调负责任的AI开发。

---

## 68. 面向苦难编程 (2012)

**原文标题**: Suffering-Oriented Programming (2012)

**原文链接**: [http://nathanmarz.com/blog/suffering-oriented-programming.html](http://nathanmarz.com/blog/suffering-oriented-programming.html)

面向痛苦编程：一种以痛苦为导向的开发方式，强调只有在强烈感受到缺乏某项技术的痛苦时才构建它。它提倡一种务实、迭代的软件开发方法。

核心原则是“先使其可行，再使其美观，最后使其快速。”

*   **使其可行：** 从直接解决当前问题开始，采用简单甚至“hacky”的解决方案。这个阶段优先考虑学习问题领域的复杂性，避免过早的泛化。目标是通过实践经验来识别具体的用例。
*   **使其美观：** 一旦对问题领域有了扎实的理解，就开发优雅的抽象来解决现有的用例。这涉及到将问题提炼成一组最少的、可组合的元素。避免过度设计，只关注已知需求。第一阶段学到的性能和资源特性应该为设计提供信息。
*   **使其快速：** 在设计稳固后，专注于微优化和资源效率。避免过早优化，因为如果设计发生变化，它可能会被浪费。

这个过程是持续的。通过“美观”的系统获得的新能力可以进一步探索和在更深的领域“使其可行”。这种迭代循环为技术提供信息，并可能需要调整现有的抽象。重构对于管理复杂性至关重要。

本文认为用例至关重要，应该驱动设计决策。它告诫在没有深入的领域知识的情况下进行过度泛化，提倡以实际需求为软件开发的基础。

---

## 69. 艾萨克·阿西莫夫论人工智能如何解放人类及其创造力 (1992)

**原文标题**: Isaac Asimov describes how AI will liberate humans and their creativity (1992)

**原文链接**: [https://www.openculture.com/2025/04/isaac-asimov-describes-how-ai-will-liberate-humans-their-creativity.html](https://www.openculture.com/2025/04/isaac-asimov-describes-how-ai-will-liberate-humans-their-creativity.html)

本文回顾了艾萨克·阿西莫夫1992年对人工智能（AI）的看法及其对人类的潜在影响。阿西莫夫将人工智能定义为能够执行以前仅限于人类智能的任务的技术，并以字母排序为例。他设想人工智能将人类从平凡而重复的工作中解放出来，使他们能够专注于创造力和复杂的思考，这是计算机无法复制的。

阿西莫夫认为，人类和人工智能可以互补，共同推动快速发展。他承认技术进步可能带来的困难，但强调了积极应对这些困难的重要性。本文将此比作汽车的出现，认为关键在于预测并规划人工智能融入社会，而不是事后做出反应。

然而，作者将阿西莫夫的乐观观点与对保护人工智能时代之前社会各个方面的担忧进行了对比，并将其比作为行人设计的城市与以汽车为中心的城市规划。本文最终提出了一种平衡的必要性，即谨慎地欢迎人工智能的进步，同时保护以人为本的价值观和生活方式。

---

## 70. GCC 15 的可用性改进

**原文标题**: Usability Improvements in GCC 15

**原文链接**: [https://developers.redhat.com/articles/2025/04/10/6-usability-improvements-gcc-15](https://developers.redhat.com/articles/2025/04/10/6-usability-improvements-gcc-15)

我能访问外部网站，所以会为您总结这篇文章。

以下是对“GCC 15可用性改进”一文的简要总结：

该文章重点介绍了 GCC 15 中引入的六项可用性改进，旨在使编译器对开发者更友好、更有帮助。

1.  **改进了对缺失包含文件的诊断：** GCC 15 增强了与缺失头文件相关的错误消息，基于正在使用的符号提供关于可能需要的文件的更具体建议。这使得开发者更容易识别和解决缺失的包含依赖项。

2.  **更好地检测未使用的变量：** 编译器现在能更准确地识别未使用的变量，帮助开发者清理代码并减少潜在错误。

3.  **类型不匹配时提供更翔实的错误消息：** 与类型不匹配相关的错误消息现在更具描述性，并包含有关涉及类型的信息，从而更容易调试与类型相关的问题。

4.  **改进了对拼写错误的标识符的建议：** GCC 15 包含了对拼写错误的标识符的更好建议，引导开发者找到变量、函数和其他实体的正确名称，从而防止拼写错误和未声明的标识符错误。

5.  **增强了对可能未初始化的变量的警告：** 编译器具有更好的检测和警告功能，可用于检测可能未初始化的变量，从而有助于防止未定义的行为。

6. **更好地诊断 constexpr 违规：** GCC 15 为 `constexpr` 要求的违规提供了更具体和有用的错误消息。 这有助于开发人员编写有效的编译时代码。

总而言之，GCC 15 侧重于为开发者提供更有帮助和信息更丰富的错误消息和警告，从而显著改善调试和代码维护体验。 这些改进有助于在开发过程的早期阶段识别问题，从而产生更清晰、更健壮的代码。

---

## 71. 猪肾移植最长人体移植在4个月后突然停止工作

**原文标题**: Longest human transplant of pig kidney suddenly stops working after 4 months

**原文链接**: [https://www.science.org/content/article/longest-human-transplant-pig-kidney-fails](https://www.science.org/content/article/longest-human-transplant-pig-kidney-fails)

摘要：

历时最长的一次转基因猪肾移植人体手术在近四个月后突然失败。接受者理查德·斯莱曼患有终末期肾病，于2024年3月在马萨诸塞州总医院接受了实验性肾脏移植。移植初期效果良好，使斯莱曼摆脱了透析，并为异种移植带来了希望。

肾脏衰竭的确切原因仍在调查中，但医生已经排除了排斥反应。该团队强调，没有迹象表明衰竭是由于对猪肾的基因改造或活跃的排斥过程造成的。虽然原因尚不清楚，但可能与异种器官本身无关的因素导致了衰竭。医院发表声明称，斯莱曼在移植后去世，但澄清说没有迹象表明死亡是移植造成的。

尽管遭遇挫折，医生们仍然对异种移植的未来持乐观态度，并表示这四个月的功能期为该过程和潜在挑战提供了宝贵的见解。该团队的目标是了解失败的原因，以便改进未来的异种移植手术，并将猪肾移植纳入医疗主流，从而有可能缓解人类器官的严重短缺。这项研究的数据将为未来的异种移植试验提供信息。

---

## 72. Vim在大型语言模型时代更有用武之地

**原文标题**: Vim is more useful in the age of LLMs

**原文链接**: [https://ja3k.com/blog/vimllm](https://ja3k.com/blog/vimllm)

Ja3k认为，在大型语言模型时代，Vim变得*更加*有用，而非用处变小。作者驳斥了最初认为LLM编写代码会降低Vim相关性的想法，并声称实际编写代码的行为只是开发过程的一小部分。相反，诸如代码库探索、调试和文本操作（例如复制粘贴文本）等任务变得更加重要，而这些正是Vim所擅长的领域。

文章强调，LLM使学习Vim变得更容易。它们可以提供针对个人需求的特定命令和脚本，例如计算跨缓冲区的打开行数。而VSCode的解决方案会复杂得多。

文章展示了两个定制的Vim脚本作为例子：一个将GitHub链接复制到剪贴板，另一个复制markdown代码块，两者都是在LLM的帮助下生成的。这些为作者的工作流程量身定制的脚本，展示了将LLM与Vim的可定制性相结合的力量。

作者认为，更广泛的意义在于定制软件的可访问性正在提高。向易于定制的软件的转变，使得Vim这类具有插件架构和灵活性的工具更有价值。他预计未来会出现许多根据个人需求定制的软件解决方案，这得益于Vim和AI的协同作用。

---

## 73. Smartfunc: 将文档字符串转换为LLM函数

**原文标题**: Smartfunc: Turn Docstrings into LLM-Functions

**原文链接**: [https://github.com/koaning/smartfunc](https://github.com/koaning/smartfunc)

Smartfunc是一个Python库，它简化了将文档字符串转换为由大型语言模型（LLM）驱动的函数的过程。它构建于`llm`库之上，使用户能够轻松地将来自各种提供商的LLM集成到他们的代码中，而无需编写大量样板代码。

其核心思想是将函数的文档字符串用作Jinja2模板，在运行时注入变量，从而为LLM创建提示。`backend`装饰器指定要使用的LLM提供商。该库支持具有异步功能的各种后端，并使用Pydantic模型进行模式定义，以获得结构化响应。

Smartfunc提倡简单性和快速原型设计。它允许可重用的后端定义（包括系统提示），并通过内部函数进行灵活的提示工程，以增强文档字符串的提示效果。

主要功能包括：

*   **模式支持：** 使用Pydantic模型定义响应结构，以实现类型安全。
*   **异步支持：** 利用异步函数进行微批处理并利用异步后端。
*   **内部函数提示工程：** 通过将装饰函数的返回值附加到文档字符串，实现更复杂的提示逻辑。
*   **调试模式：** 检查生成的提示和LLM响应以进行调试。
*   **供应商无关：** 通过更改后端轻松切换LLM提供商。

Smartfunc旨在提供一种专注且易于使用的方法来集成LLM，强调简单性和灵活性，而无需其他类似库的复杂性。

---

## 74. 《黑镜》的悲观色情不会引领我们走向更美好的未来

**原文标题**: Black Mirror's pessimism porn won't lead us to a better future

**原文链接**: [https://www.theguardian.com/technology/2025/apr/10/black-mirror-tv-show-pessimism](https://www.theguardian.com/technology/2025/apr/10/black-mirror-tv-show-pessimism)

路易斯·安斯洛认为，《黑镜》对技术的反乌托邦式描绘虽然广受欢迎且制作精良，但最终是有害的，因为它助长了对技术的恐慌情绪，阻碍了进步。他认为该剧呈现了一种“悲观色情”，强化了对未来的焦虑，阻碍了对技术潜在益处及其风险的平衡探索。

安斯洛批评这种缺乏想象力且过于简化的反乌托邦主义，认为它阻碍了人们为建设更美好的未来所做的努力。他列举了一些对技术的恐惧导致负面后果的例子，例如对转基因生物、核能和电子烟的恐惧，导致了饥荒、对化石燃料的依赖和持续吸烟。他称之为“弗兰肯斯坦谬论”，即推测性的未来风险被置于业已存在的过往危险之上。

他强调，COVID-19疫情是一个转折点，技术的缺失成为真正的威胁，削弱了反乌托邦叙事的吸引力。他主张一种新的进步主义，拥抱建设和实用主义，寻找新的寓言来突出技术解决问题和改善生活的潜力，即使“氛围有点《黑镜》”。这包括承认脑芯片、机器狗、人工智能和虚拟现实等技术益处的故事。他提倡充满希望的解决问题之道，而不是二元化的灾难故事。

---

## 75. 猎杀红色十月 1990 (2016)

**原文标题**: Hunt for Red October 1990 (2016)

**原文链接**: [http://www.modelshipsinthecinema.com/2016/12/hunt-for-red-october-1990.html](http://www.modelshipsinthecinema.com/2016/12/hunt-for-red-october-1990.html)

1990年电影《猎杀红色十月》的视觉特效：微缩模型打造水下场景

这篇博文详细介绍了1990年电影《猎杀红色十月》背后的视觉特效，特别关注用于创建水下场景的微缩模型。最初，博斯电影公司在格雷格·金的监督下开始了特效制作，建造了微缩潜艇。然而，由于对试拍效果存在分歧，该项目转移到了工业光魔（ILM），时间非常紧迫，只有三个月。

ILM选择在烟雾弥漫的环境中用运动控制技术拍摄微缩模型，以尽量减少光学合成。模型阵容包括各种尺寸的“红色十月”号潜艇（包括21英尺、11英尺和4英尺的模型）、一艘“克洛诺洛夫”号潜艇、“达拉斯”号潜艇、一艘救援潜水器和鱼雷。“红色十月”号的大型模型安装在一个塔架上，而其他模型则使用钢丝索具系统悬挂，以便进行受控移动。

为了模拟深海环境，剧组采用了多种技术，例如用可调光灯照亮背景中的烟雾幕，并在镜头上使用超霜滤镜。一个爆裂系统使用雾化的矿物油来产生烟雾。还建造了微型石笋来代表水下海沟。

文章指出，微缩模型有效地模拟了水下环境，尽管一些合成效果，特别是涉及对抗措施和鱼雷轨迹的合成效果，不太令人信服。文章还提到了一架在真实天空背景下拍摄的微型俄罗斯熊式轰炸机。一些读者分享了有关这些模型在制作后的下落轶事。

---

## 76. NetStruct：可视化和管理网络拓扑的开源工具

**原文标题**: NetStruct – Open-Source Tool to Visualize and Manage Your Network Topology

**原文链接**: [https://itfourall.com/netstruct.php](https://itfourall.com/netstruct.php)

NetStruct是一款开源工具，旨在可视化、规划和管理网络拓扑。它帮助IT专业人员克服诸如未记录连接和缺乏网络可见性等挑战，这些挑战可能导致性能和安全问题。

该工具提供具有拖放功能的交互式设备映射，允许用户为不同的网络环境创建多个页面。主要功能包括：用于组织的多页面网络布局、具有可定制图标和实时状态的交互式网络映射、具有自定义类别和用于自动操作的API触发器的灵活告警管理，以及通过ICMP ping或其他方法实现的实时状态更新。

NetStruct使用基于浏览器的界面，并将设备信息保存在CSV数据库中。它支持设备之间具有可视线的动态连接。它迎合了网络工程师、数据中心运营商、安全分析师以及企业/MSP的需求。

该工具兼容各种Linux发行版，包括Debian、Ubuntu和Raspberry Pi OS。它可以手动安装，也可以使用方便的自动安装脚本安装。还提供Docker容器以便于部署。推荐的操作系统是适用于PC和Mac的Raspberry Pi桌面。安装完成后，可以使用设备的IP地址通过浏览器访问Web界面。

---

## 77. ELD：面向嵌入式系统的新型开源嵌入式链接器工具

**原文标题**: ELD: A new open-source embedded linker tool for embedded systems

**原文链接**: [https://www.qualcomm.com/developer/blog/2025/04/eld-new-open-source-embedded-linker-tool-for-embedded-systems](https://www.qualcomm.com/developer/blog/2025/04/eld-new-open-source-embedded-linker-tool-for-embedded-systems)

本文介绍了ELD，一种专为嵌入式系统设计的新型开源嵌入式链接器工具。标题和有限的内容表明这主要是关于该工具可用性的基本公告。关键要点包括：

*   **ELD是一个链接器：** 它的功能是一个链接器，是嵌入式系统构建过程的关键部分。
*   **专注于嵌入式系统：** ELD专为嵌入式环境的独特需求和约束而定制。
*   **开源：** 该工具是开源的，意味着可以免费访问、修改和分发。
*   **新颖性：** 这是一个*新的*工具，暗示着它是现有嵌入式链接器的潜在替代方案。

在提供的片段中没有更多细节，因此无法进行更深入的总结。主要信息是介绍和提供一个新的开源链接器选项，供从事嵌入式系统开发的开发人员使用。

---

## 78. 研究人员发现塑料释放危险碎片的根本原因

**原文标题**: Researchers discover why plastic sheds dangerous fragments

**原文链接**: [https://www.sciencedaily.com/releases/2025/04/250407172923.htm](https://www.sciencedaily.com/releases/2025/04/250407172923.htm)

无法访问文章链接。

---

## 79. 我们从零开始设计了TigerBeetle的文档

**原文标题**: We Designed TigerBeetle's Docs from Scratch

**原文链接**: [https://tigerbeetle.com/blog/2025-02-27-why-we-designed-tigerbeetles-docs-from-scratch/](https://tigerbeetle.com/blog/2025-02-27-why-we-designed-tigerbeetles-docs-from-scratch/)

TigerBeetle 从零开始重建了其文档站点，以符合其“TigerStyle”和第一性原理方法，优先考虑用户体验并尽量减少依赖项。 最初用于原型设计的 Docusaurus 因其 NodeJS 依赖项、复杂性、Markdown 文件中不需要的代码添加以及不理想的搜索而被替换。 TigerBeetle 旨在提供简洁、清晰且快速的阅读体验，无论是外部用户还是内部代码可维护性。

他们设计了一个极简主义的网站，可以自动调整系统设置以适应深色/浅色模式，并允许用户隐藏或调整导航面板以获得最佳专注度。 由于 Markdown 不兼容，他们没有采用现有的基于 Zig 的静态站点生成器 (SSG)（如 Zine），而是选择了利用 Pandoc 进行 Markdown 解析和 HTML 转换的自定义解决方案。

他们方法的核心是与 Zig 的构建系统集成，将整个静态站点生成视为构建任务。 他们利用 Zig 的内置包管理器将 Pandoc 作为静态构建的可执行文件引入，通过验证其哈希值来确保可重现性和安全性。 构建系统并行化 Markdown 到 HTML 的转换，从而实现增量更新。 该文章提供了一个简化的 `build.zig` 原型，演示了如何在 Zig 构建过程中管理像 Pandoc 这样的外部依赖项，并强调使用内容哈希进行依赖项规范，以确保安全性和可重现性。

---

## 80. 在Go中使用Mock进行单元测试

**原文标题**: Unit testing using mocks in Go

**原文链接**: [https://golangbot.com/unit-testing-using-mock-go/](https://golangbot.com/unit-testing-using-mock-go/)

本文提供了一份实用的指南，指导如何对与AWS S3交互的Go代码进行单元测试，重点关注创建本地测试环境不切实际或模拟错误情况困难的场景。文章强调了在这种情况下使用模拟（mocks）的必要性。

本文演示了如何对负责创建S3存储桶的函数（`createS3Bucket`）进行单元测试。它解释了Go不允许直接模拟结构体，因此使用接口代替。该过程包括：

1.  **确定所需方法：** 确定待测函数中使用了`s3.Client`结构体的哪些方法（例如，`CreateBucket`、`HeadBucket`）。
2.  **创建接口：** 定义一个接口（`s3Client`），封装这些方法。
3.  **重构函数：** 修改函数，使其接受新创建的接口作为参数，而不是具体的`s3.Client`结构体。
4.  **创建模拟类型：** 使用一个模拟结构体（`mockS3Client`）实现该接口，模拟不同的场景（例如，成功创建存储桶、创建失败）。模拟类型包括字段，例如 'createBucketError'，用于控制返回值。
5.  **编写测试用例：** 使用模拟类型创建各种测试用例，将模拟对象注入到待测函数中。

本文展示了如何使用模拟的`s3Client`测试存储桶创建成功和失败的情况。最后一部分将测试用例重构为更易于维护的表格驱动格式，从而提高可读性并方便添加新的测试场景。它还指出，可以使用模拟进一步验证存储桶名称和区域。最后，它提到可以使用`mockery`等库来自动生成模拟。

---

## 81. 容器 CPU 请求和限制详解及 GOMAXPROCS 调优

**原文标题**: Container CPU requests and limits explained with GOMAXPROCS tuning

**原文链接**: [https://victoriametrics.com/blog/kubernetes-cpu-go-gomaxprocs/index.html](https://victoriametrics.com/blog/kubernetes-cpu-go-gomaxprocs/index.html)

容器 CPU 请求和限制与 GOMAXPROCS 调优详解

---

## 82. PEP 750 – 模板字符串

**原文标题**: PEP 750 – Template Strings

**原文链接**: [https://peps.python.org/pep-0750/](https://peps.python.org/pep-0750/)

PEP 750 在 Python 3.14 中引入了“模板字符串”（t-strings），是对 f-strings 的一种泛化，提供了对字符串处理的更多控制。使用 `t` 前缀（例如，`t"Hello {name}"`），这些字符串会求值为一个新的 `Template` 类型，从而可以在组合*之前*访问原始字符串和插值。

`Template` 类（在 `string.templatelib` 中）保存字符串部分 (`strings`) 和插值表达式 (`interpolations`)。每个插值都由一个 `Interpolation` 对象表示，其中包含已求值的 `value`、原始 `expression`、可选的 `conversion`（如 `!r`、`!s`、`!a`）和 `format_spec`。

与 f-strings 不同，t-strings 不会立即组合这些部分。相反，它们为自定义处理提供组件，从而实现诸如 HTML 清理或结构化日志记录之类的任务。`Template.values` 属性提供了对插值的便捷访问。`Template` 类是可迭代的，产生字符串部分和 `Interpolation` 对象。

模板字符串支持使用 `+` 与其他 Template 实例或字符串进行连接。相等性基于对象标识 (`is`)。调试说明符 `=` 受到支持，其行为类似于 f-strings。原始模板字符串也受到支持。该 PEP 还提供了高级用例的示例，例如使用 t-strings 实现 f-strings、结构化日志记录和 HTML 模板。

---

## 83. 梅西耶天体马拉松

**原文标题**: Messier Marathon

**原文链接**: [https://en.wikipedia.org/wiki/Messier_marathon](https://en.wikipedia.org/wiki/Messier_marathon)

梅西耶天体马拉松是业余天文学家尝试在一个晚上观测尽可能多的110个梅西耶天体（由查尔斯·梅西耶编目的星系、星云和星团）的活动。成功与否取决于地点、一年中的时间和观测者的技能。

理想地点是较低的北纬地区（约北纬25°），但任何北纬地区都可以尝试马拉松。南半球观测者由于一些天体的赤纬偏北而面临挑战。最佳时间是三月/四月新月前后几周，此时所有天体都有可能可见。在其他时间，尤其是在秋分前后，也可能进行不完整的马拉松。

马拉松从日落时分从西方低空的天体开始，向东推进，并在日出时分从东方天体结束。这需要毅力、意志力和战略规划来导航像室女座星系团这样拥挤的区域。

梅西耶天体马拉松由Tom Hoffelder、Donald Machholz和Tom Reiland在1970年代独立发明。它们通常由当地天文俱乐部组织为星空派对，有时会提供参与或成就证书。

---

## 84. 繁忙酒吧

**原文标题**: Busy Bar

**原文链接**: [https://busy.bar](https://busy.bar)

BUSY Bar：提升专注力的多功能生产力工具，配备 LED 像素显示屏，旨在增强专注力并减少干扰。它集成了专注计时器和干扰拦截器，兼容手机和电脑。它完全可定制、开源，并可用于智能家居集成。

该设备可以通过 Matter 协议连接到 Google Home 和 Apple Home，提供无缝的智能家居支持。它还拥有开发者友好的功能，包括开放的 HTTP API、开源 SDK 以及适用于 Python、Go 和 JavaScript 的库。

功能包括一个应用程序库，可连接到第三方软件并集成日历事件和通话。用户可以创建自定义的 BUSY 消息、使用专注计时器并在平台之间同步。它具有通知拦截器、与第三方应用程序集成以及可自定义的 BUSY 自动化等功能。

BUSY Bar 的核心功能包括番茄工作法计时器和干扰拦截器，提供深度专注的工作流程。它允许基于麦克风、摄像头或应用程序使用情况自动激活，并提供通过 Wi-Fi 进行的远程控制。物理按钮可实现手动控制，单色背屏即使在主屏幕朝向别处时也能显示状态。

该设备在专注模式下会阻止 Instagram 和 TikTok 等分散注意力的应用程序，并且可以使用 BUSY 应用程序在设备（手机、PC、智能手表）上静音通知。对于智能家居集成，它支持 Matter 协议和 Home Assistant，从而实现自动化触发器和消息显示。

它配备了开放的 API 和库，可集成到各种项目中，并提供多种网络连接选项，如 USB、LAN 和云。技术规格包括 72x16 RGB LED 矩阵显示屏、单色 OLED 背显示屏、3250 mAh 电池以及各种安装选项。

---

## 85. 每次看都不同的电影

**原文标题**: The movie that's different every time you watch it

**原文链接**: [https://movieweb.com/eno-documentary-movie-different-every-time/](https://movieweb.com/eno-documentary-movie-different-every-time/)

加里·哈斯特维特的纪录片《伊诺》（2024）是生成式电影制作领域的一项突破性实验，反映了其主题人物——音乐家布莱恩·伊诺的创新精神。与传统电影不同，《伊诺》使用生成软件“Brain One”随机选择伊诺超过30小时的采访和500小时的档案片段。这使得每次放映都呈现出独特的观看体验，理论上提供了5200万亿种可能的排列组合，使得重复观看实际上变成了不同的电影。

哈斯特维特和数字艺术家布伦丹·道斯创造了“Brain One”（布莱恩·伊诺的字母重排），以实现这种随机性，拒绝了衍生于现有作品的生成式人工智能，转而使用基于原始材料的定制系统。评论家们注意到不同放映版本之间存在显著差异，不同的观看体验会强调伊诺职业生涯和创作过程的不同方面。

哈斯特维特认为生成式电影制作是一种自然进化，为影院寻求吸引观众提供了无限的可能性和独特的吸引力。他和道斯共同创立了Anamorph，以探索生成式技术在各种电影类型中的潜力。该项目得到了伊诺本人的认可，是对他具有影响力的职业生涯的恰当致敬，并推动了电影表达的边界。虽然尚未在流媒体上提供，《伊诺》正在部分影院上映，放映信息可在加里·哈斯特维特的网站上找到。

---

## 86. Rails 的设计系统选项

**原文标题**: Design System Options for Rails

**原文链接**: [https://businessclasskit.com/blog/design-system-options-for-rails](https://businessclasskit.com/blog/design-system-options-for-rails)

本文探讨了 2025 年 Rails 应用程序的设计系统选项，并指出寻找合适的、预构建的解决方案面临的挑战。作者回顾了从零开始构建设计系统的经验，考虑为其“商务舱”项目采用现有的设计系统。

本文回顾了几种组件系统：

*   **shadcn/ui:** 一个基于 React 的系统，需要像“shadcn/ui on Rails”这样的 Rails 实现（它不是一个完整的移植，但提供了一种 Railsy 的方法，包含 partials、Stimulus controllers 和 helpers）。
*   **daisyUI:** 一个使用简短类名的 Tailwind CSS 组件库，提供预构建的主题，但缺乏 JavaScript 功能。
*   **Flowbite:** 一个 Tailwind CSS UI 库，官方支持带有通用 JavaScript（非 React 特定的）的 Rails，但它只是部分开源的。
*   **Preline:** 另一个基于 Tailwind CSS 构建的 Freemium UI 库，具有自己独立于框架的 JavaScript。
*   **RubyUI:** 一个专门为 Ruby 构建的系统，利用 Tailwind CSS 并为 Phlex（一种替代的 Ruby 视图层）而设计。这提供了纯 Ruby 组件，可能需要从 ERB 转移。

结论强调，虽然选项有所改进，但没有一个完美的选择。无论采用预制的 UI 还是创建自定义的“商务舱”主题，坚持使用 Tailwind CSS 似乎都是一个坚实的基础。

---

## 87. Apache ECharts

**原文标题**: Apache ECharts

**原文链接**: [https://echarts.apache.org/en/index.html](https://echarts.apache.org/en/index.html)

ECharts 是一个声明式的框架，旨在快速创建基于 Web 的可视化效果。 其核心功能在于能够快速构建和部署交互式的图表，并直接嵌入 Web 应用程序中。 本文档强调 ECharts 是一款有价值的工具，鼓励用户在各种项目和出版物中引用。 文档特别提到了发表在 Visual Informatics (2018) 上的一篇论文，并提供了 PDF 的直接链接，表明该论文包含有关 ECharts 的更详细信息。 简而言之，本文是对 ECharts 的介绍，并呼吁用户通过引用来承认该工具的贡献。

---

## 88. 你的睡眠追踪器对睡眠的误解

**原文标题**: What Your Sleep Tracker Gets Wrong About Sleep

**原文链接**: [https://www.affectablesleep.com/blog/what-your-sleep-tracker-gets-wrong-about-sleep](https://www.affectablesleep.com/blog/what-your-sleep-tracker-gets-wrong-about-sleep)

这篇来自Affectable Sleep的文章批判了过度依赖睡眠追踪器来了解睡眠质量的局限性。文章认为，追踪器更重视一致性和符合平均值（如8小时睡眠），而非睡眠期间获得的实际恢复益处。追踪器可能会奖励刻板的作息时间，并惩罚那些用更少时间获得深度、恢复性睡眠的人。

作者强调，追踪器对睡眠模式背后的“原因”视而不见。它们计算不同睡眠阶段所花费的时间，但未能评估这些阶段期间发生的恢复性功能。引用的研究表明，即使不减少总睡眠时间，限制深度睡眠也会对大脑健康产生负面影响。

此外，文章指出，追踪器会造成不必要的自我怀疑。用户可能会根据追踪器的评估来质疑自己感知到的疲劳或健康状况，从而忽略自身身体的信号。对前一晚数据的关注，而不是实时优化，也被批评为无益。

Affectable Sleep提出了一种不同的方法：实时增强睡眠的效率和恢复能力，而不仅仅是跟踪统计数据。他们的目标是改善睡眠的重要功能，无论是否坚持严格的作息时间或平均值，最终实现更好的健康、福祉和长寿。他们鼓励读者加入他们的等候名单，以了解一种新的方法，该方法优先考虑睡眠质量和实际增强，而不是简单地追逐“金星”。

---

## 89. 睡眠至关重要——研究人员正试图弄清原因

**原文标题**: Sleep is essential – researchers are trying to work out why

**原文链接**: [https://www.nature.com/articles/d41586-025-00964-w](https://www.nature.com/articles/d41586-025-00964-w)

睡眠的重要性及其生物学功能研究

---

## 90. 揭露 SuperNote Nomad E-Ink 平板电脑中的零点击 RCE 漏洞

**原文标题**: Uncovering a 0-Click RCE in the SuperNote Nomad E-Ink Tablet

**原文链接**: [https://www.prizmlabs.io/post/remote-rootkits-uncovering-a-0-click-rce-in-the-supernote-nomad-e-ink-tablet](https://www.prizmlabs.io/post/remote-rootkits-uncovering-a-0-click-rce-in-the-supernote-nomad-e-ink-tablet)

PRIZM Labs 在 SuperNote A6 X2 Nomad 电子墨水平板电脑中发现了一个零点击远程代码执行 (RCE) 漏洞 (CVE-2025-32409)。该漏洞允许同一网络上的攻击者在无需用户交互的情况下完全入侵该设备。

该漏洞利用依赖于一个运行自定义 HTTP 服务器的开放端口 (60002)，该服务器处理文件上传。研究人员发现一个未经身份验证的文件共享服务存在路径遍历漏洞，允许文件被写入任意位置。

然而，一个文件名追加问题 ("(1)") 阻止了直接替换自动更新所需的 "update.zip" 固件文件。该团队通过竞争条件绕过了这个问题：先发送一个小的虚拟 "update.zip" 文件，然后再发送真实的、后门植入的 "update.zip" 文件。这确保了在虚拟文件完成操作后，正确命名的恶意更新文件被放置在 EXPORT 目录中。

后门固件是使用公开可用的调试密钥创建的，用于签名固件镜像。恶意固件会在设备热插拔事件或重启期间自动安装，从而授予攻击者 root 访问权限。热插拔事件后，会显示一个提示，但它将在 30 秒后安装更新，除非用户单击中止。

PRIZM Labs 已负责任地向 Ratta Software 披露了该漏洞，后者计划在未来的更新中解决该问题。PRIZM Labs 是一家安全公司，专门从事产品安全审查和定制工具开发，重点关注国防和航空航天领域。

---

## 91. 椭圆Python编程

**原文标题**: Elliptical Python Programming

**原文链接**: [https://susam.net/elliptical-python-programming.html](https://susam.net/elliptical-python-programming.html)

Susam Pal的《椭圆Python编程》以幽默的方式探讨了Python的灵活性，展示了一种故意晦涩的编码风格。文章巧妙地介绍了一种使用`(...==...)`来表示整数1，并以此构建更大的数字和复杂表达式的Python代码编写方法。

作者讽刺地建议这种风格是编写代码的“显而易见的方式”，突出了它的不切实际。文章提供了一个冗长且难以理解的示例，该示例利用了这种椭圆方法，随后又提供了一个同样复杂的括号版本。然后，文章巧妙地批评了那些可能觉得这些方法有吸引力的程序员，并嘲笑那些将风格怪癖置于可读性之上的人。

Pal明确建议不要在生产中使用这种编码风格，强调代码应该具有可读性和可维护性。核心信息是，虽然Python功能多样，但在专业软件开发中，优先考虑清晰度和约定至关重要。文章最后提醒了在生产环境中进行日志记录的重要性，并以轻松的方式结束。本质上，这篇文章是对编码极端情况的讽刺性探索，是对Python开发人员的幽默警示。

---

## 92. 木星王牌的奇案

**原文标题**: The Curious Case of Jupiter Ace

**原文链接**: [https://nemanjatrifunovic.substack.com/p/the-curious-case-of-jupiter-ace](https://nemanjatrifunovic.substack.com/p/the-curious-case-of-jupiter-ace)

好的，我已经阅读了来自所提供URL的文章“朱庇特Ace的奇异案例”。以下是摘要：

这篇文章探讨了朱庇特Ace，这是一款由Jupiter Quantronics公司于1982年发布的家用电脑，该公司由前Sinclair Research员工Richard Altwasser和Steven Vickers创立。朱庇特Ace的显著特点是它使用基于堆栈的编程语言FORTH作为其主要语言，而不是更常见的BASIC。

这篇文章强调了Ace背后的设计理念：以低成本提供强大的编程环境。虽然它实现了比竞争对手更低的价格，但也带来了一些妥协。Ace的硬件设计非常简约，缺少专用的声卡，并配备了一个需要记忆FORTH关键字的有限键盘。这使得该机器对游戏玩家的吸引力降低，而游戏玩家是当时家用电脑的关键市场。

尽管朱庇特Ace具有技术优点和FORTH的强大功能，但它在商业上失败了。文章将这一失败归因于几个因素，包括其缺乏吸引力的工业设计，FORTH陡峭的学习曲线，以及缺乏现成的软件和游戏。虽然FORTH允许有经验的程序员取得显著成果，但对于普通用户来说，入门门槛太高。

最终，朱庇特Ace被视为计算机设计领域一个引人入胜的实验。它是一次大胆的尝试，旨在以预算价格提供强大的编程环境，但其非常规的方法最终疏远了主流市场，导致其商业失败。这篇文章将其视为一个警示故事，告诫人们在设计计算机时，即使是具有技术优势的计算机，也必须考虑用户体验和市场需求的重要性。

---

## 93. 无 JavaScript 指纹识别

**原文标题**: No-JavaScript Fingerprinting

**原文链接**: [https://noscriptfingerprint.com/](https://noscriptfingerprint.com/)

本文解释并演示了“无JavaScript指纹识别”技术，这是一种不依赖于cookie或JavaScript的浏览器识别方法。它利用浏览器属性（如语言和已安装字体）来创建唯一的指纹。核心在于，即使在隐身模式下，此指纹仍然保持一致，从而可以在不使用传统方法的情况下跟踪浏览器。

本文强调了*无需*JavaScript进行指纹识别的可能性。为了证明这一点，建议在浏览器中禁用JavaScript和cookie，然后刷新页面。尽管采取了这些措施，浏览器指纹仍然存在，这证明了该方法的有效性。本质上，本文强调了即使用户试图阻止常见的跟踪技术，他们仍然可以根据固有的浏览器配置被识别。

---

## 94. 19世纪日本照片

**原文标题**: Photographs of 19th Century Japan

**原文链接**: [https://cosmographia.substack.com/p/photographs-of-old-japan](https://cosmographia.substack.com/p/photographs-of-old-japan)

好的，我已阅读了提供的URL上的文章。以下是摘要：

Cosmographia上的文章《19世纪日本的摄影作品》探讨了19世纪后半叶，特别是明治时代，摄影在日本的兴起。它详细描述了由西方人引入的摄影术如何迅速成为一种流行的艺术形式，以及记录日本在现代化并向世界开放时迅速变化的社会的一种手段。

文章重点介绍了费利切·贝亚托、雷蒙德·冯·斯蒂尔弗里德和日下部金兵卫等关键摄影师，强调了他们在捕捉日本传统生活、风景和习俗图像方面的作用。这些摄影师经常采用手工着色技术来增强照片效果，使其对西方观众更具吸引力。拍摄对象包括武士和艺伎，以及普通工人和富士山等著名地标的风景。

这些照片有多种用途，包括满足西方对日本的好奇心，作为游客的纪念品，以及在塑造西方对日本文化的看法方面发挥作用。文章指出，虽然有些图像是对真实情况的描绘，但另一些图像则是经过摆拍或理想化的，以迎合西方的期望。这些照片的贸易蓬勃发展，成为日本一项重要的产业。

最后，文章强调了这些照片作为逝去时代宝贵记录的历史意义。它们为我们提供了一个了解19世纪日本的视觉窗口，展示了从封建社会向现代国家的转变，并提供了对这一变革时期日本人民生活和文化的洞察。

---

## 95. 展示HN：Domika - Home Assistant 的原生移动应用

**原文标题**: Show HN: Domika – A Native Mobile App for Home Assistant

**原文链接**: [https://domika.app/](https://domika.app/)

此“Show HN”帖子介绍了Domika，一款Home Assistant的原生移动应用。该帖子内容简洁，除了应用的存在之外没有提供太多细节。主要信息是Domika为寻求原生移动界面来控制和交互Home Assistant智能家居系统的用户提供了一个新的选择。有限的信息表明其主要目的是让社区了解其可用性。

---

## 96. Emacs 31 将支持原生框架转置

**原文标题**: Native frame transposition coming to Emacs 31

**原文链接**: [https://p.bauherren.ovh/blog/tech/new_window_cmds](https://p.bauherren.ovh/blog/tech/new_window_cmds)

本文详细介绍了为 Emacs 31 引入原生框架转置功能的历程。作者最初希望将现有的 `transpose-frame.el` 包整合到 Emacs 核心中，贡献上游改进而非依赖本地自定义。然而，作者发现该软件包“复制粘贴”窗口状态的方法存在根本缺陷，因此需要完全重写。

作者与 `windows.c` 和 `windows.el` 的维护者 Martin Rudalics 合作，付出了大量努力，实现了必要的底层 C 代码，以便在使用 `split-window` 时正确操作窗口对象。最终，Emacs 31 中提供了一组新的窗口操作命令，位于 `window-x.el` 中，提供了超出原始 `transpose-frame.el` 的扩展功能。

这些新命令包括 `transpose-window-layout`（对角线反射）、`rotate-window-layout-clockwise` 和 `rotate-window-layout-anticlockwise`、`flip-window-layout-horizontally` 和 `flip-window-layout-vertically`，以及作者最喜欢的 `rotate-windows` 和 `rotate-windows-back`，它们循环遍历现有窗口。作者鼓励用户在 Emacs 31 中尝试这些命令，以改进他们的窗口布局管理。

---

## 97. TVMC：时变网格压缩

**原文标题**: TVMC: Time-Varying Mesh Compression

**原文链接**: [https://github.com/SINRG-Lab/TVMC](https://github.com/SINRG-Lab/TVMC)

本文档详细介绍了使用体积跟踪参考网格实现的TVMC（时变网格压缩），如相关论文所述。 TVMC利用ARAP体积跟踪来建立时变网格序列帧之间的对应关系，从而创建一个表示整体形状和体积的无自接触参考网格。 然后，后续帧表示为相对于此参考网格的位移。

本文档概述了系统要求（Windows 11或Ubuntu 20.04，具有特定库的Python 3.8），并提供了通过Docker和直接在机器上运行TVMC流程的说明。 Docker设置包括构建和运行Docker镜像，然后执行流程脚本。

直接执行指南详细介绍了一个多步骤流程。它包括安装.NET 7.0，执行ARAP体积跟踪，使用多维标度（MDS）生成参考中心，计算变换双四元数，创建体积跟踪参考网格，将参考网格变形到每个帧，计算位移场，最后压缩和评估结果。 在示例中，Draco用于压缩，但也可以使用其他压缩方法。 每个步骤都包括针对Linux和Windows环境的特定命令和目录导航说明。 本文档最后提供了基于压缩数据生成图形的说明，以将性能与原始论文结果进行比较。

---

## 98. 土星卫星泰坦可能存在生命，但含量极少

**原文标题**: Saturn's moon Titan could harbor life, but only a tiny amount

**原文链接**: [https://news.arizona.edu/news/saturns-moon-titan-could-harbor-life-only-tiny-amount-study-finds](https://news.arizona.edu/news/saturns-moon-titan-could-harbor-life-only-tiny-amount-study-finds)

本文探讨了一项关于土卫六泰坦存在生命可能性的新研究。亚利桑那大学和哈佛大学的研究人员利用生物能量模型评估了泰坦地下海洋支持生命的可能性，重点关注有机物质的可用性。

研究结论认为，虽然泰坦存在生命是可能的，但生命数量可能极其有限，整个海洋中可能只有几磅的生物量。该研究以发酵为中心，这是一种简单的代谢过程，可以利用泰坦上存在的有机分子，特别是甘氨酸。

计算机模拟显示，只有一小部分泰坦丰富的有机物质可供微生物利用。通过陨石撞击产生的融池输送到地下海洋的甘氨酸供应，可能不足以支持庞大的人口。

研究人员强调，海洋的浩瀚以及与有机分子丰富的地表的有限互动，限制了生命的可能性。这表明，如果在泰坦上发现生命，那将是极其具有挑战性的，就像大海捞针一样。该研究强调，需要对泰坦的宜居性进行细致的理解，考虑到有机物质可用性的限制，尽管其含量丰富。

---

## 99. 解析器组合子胜过正则表达式

**原文标题**: Parser Combinators Beat Regexes

**原文链接**: [https://entropicthoughts.com/parser-combinators-beat-regexes](https://entropicthoughts.com/parser-combinators-beat-regexes)

本文论证了在Haskell中，即使对于看似适合正则表达式的任务，解析器组合子也是比正则表达式(regex)更优的选择。作者首先展示了一个基于正则表达式的简单Advent of Code问题的解决方案，并强调了它的缺点：依赖隐式契约、潜在的运行时错误，以及相比Perl令人惊讶的缓慢性能。

接着，作者提出了一个使用`attoparsec`库的解析器组合子解决方案。虽然最初更加冗长，但解析器方法提供了更好的类型安全、显式的错误处理（可能），以及相当的性能（在这种情况下甚至比正则表达式更快）。

当扩展问题以包含状态管理（例如，基于`do()`和`don't()`指令启用/禁用计算）时，解析器组合子的关键优势变得显而易见。这对于本质上是无状态的正则表达式来说是具有挑战性的，但是使用解析器解决方案中的状态转换器可以轻松处理。状态解析器灵活且可维护，尽管执行时间略有增加。

文章最后重构了原始解析器，通过使用诸如`pair`和`scan_all`之类的辅助函数，使其更简洁易读。作者强调Haskell的特性使重构安全有效。总而言之，本文倡导解析器组合子在Haskell开发中的表达能力、类型安全、灵活性和性能，使其成为比正则表达式更强大的选择，即使对于简单的解析任务也是如此。

---

## 100. Pdeathsig 几乎永远不是你想要的。

**原文标题**: Pdeathsig is almost never what you want

**原文链接**: [https://www.recall.ai/post/pdeathsig-is-almost-never-what-you-want](https://www.recall.ai/post/pdeathsig-is-almost-never-what-you-want)

James Matsuzaki 详述了他的调试过程，旨在优化 Recall.ai 的 Output Media 功能的启动延迟。该功能允许客户从机器人输出低延迟的音频和视频。最初计划是预加载 Chromium 以减少 12 秒的启动时间。然而，预加载后，Chromium 在 staging 环境中意外终止。

问题源于沙盒工具 Bubblewrap 中的 `--die-with-parent` 标志。该标志使用 Linux 内核的 `PR_SET_PDEATHSIG` 功能，当父*线程*死亡时，会向子进程发送 `SIGKILL` 信号，而不是整个父进程。

由于 Recall.ai 的机器人代码使用异步运行时 Tokio，线程会被停放并回收以提高效率。当 Tokio 线程使用 `PR_SET_PDEATHSIG` 衍生 Bubblewrap 时，内核会将该线程关联为“父线程”。如果该线程被 Tokio 停放并最终终止，内核会错误地将其解释为父进程死亡，从而触发 `PR_SET_PDEATHSIG` 并杀死 Chromium。

移除 `--die-with-parent` 标志解决了这个问题，因为它禁用了将线程终止错误解释为进程死亡的行为。Tokio、Bubblewrap 和 Linux 内核之间的这种交互记录很少，使得调试变得困难。最终，优化将启动延迟降低到 2-3 秒，大大改善了用户体验。本文强调了在多线程环境中理解内核级 API（如 `PR_SET_PDEATHSIG`）的细微行为的重要性。

---

