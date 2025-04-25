# Hacker News 热门文章摘要 (2025-04-25)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 写入“/etc/hosts”文件会破坏 Substack 编辑器。

**原文标题**: Writing "/etc/hosts" breaks the Substack editor

**原文链接**: [https://scalewithlee.substack.com/p/when-etchsts-breaks-your-substack](https://scalewithlee.substack.com/p/when-etchsts-breaks-your-substack)

文章《修改'/etc/hosts'导致Substack编辑器崩溃》详细描述了直接修改`/etc/hosts`文件可能如何意外地破坏Substack编辑器的功能。作者回忆了一段个人经历，为了测试目的，他们修改了`/etc/hosts`文件以重定向一个特定域名，却无意中导致了Substack编辑器崩溃。

关键在于，Substack依赖于某些域名和服务，通过`/etc/hosts`文件干扰它们的解析可能会导致编辑器中出现意外问题，例如无法保存草稿、图片上传问题以及编辑器总体无响应。文章强调，这是因为Substack的编辑器会对其自身的基础设施进行API调用。当域名解析被篡改时，这些调用会失败。

作者的解决方案是恢复对`/etc/hosts`文件所做的更改，从而有效地恢复Substack服务的正确域名解析。这篇文章是对经常修改`/etc/hosts`文件的开发者和高级用户的一个警示，强调了考虑对依赖特定域名解析的Web应用程序的潜在影响的重要性。它强调了现代Web应用程序的隐藏依赖性，以及看似无害的系统级修改可能造成的重大后果。

---

## 2. Eurorack旋钮创意

**原文标题**: Eurorack Knob Idea

**原文链接**: [https://mitxela.com/projects/euroknob](https://mitxela.com/projects/euroknob)

Mitxela详述了他的“Eurorack旋钮创意”，这是一种旨在减少面板杂乱的新型Eurorack模块设计方法。该概念用混合旋钮和跳线系统取代了传统的电位器。该系统使用3.5mm TRS插孔代替电位器，并配有位于插孔下方的磁编码器芯片(AS5600)。一个小的钕磁铁嵌入在TRS插头中，充当旋钮。插入时，磁铁与AS5600相互作用，将旋钮的旋转转化为角度读数，可用于控制模块参数。

作者描述了磁性旋钮的构造、结合了AS5600和用于读取和显示编码器数据的微控制器（CH32V003）的电路板设计以及组装过程。该原型成功地通过场强读数检测到磁性旋钮的存在，将其与标准跳线区分开来。

尽管原型成功，但作者承认在整个Eurorack系统中实施该想法可能不切实际且成本高昂。他设想了一个专门致力于此概念的小众社区，“Euroknobists”。虽然没有申请专利，但他提出了一个更具商业可行性的替代方案：带有同轴TRS插孔的电位器。他最后邀请企业家资助和开发这个想法，并承认他在该领域的局限性。

---

## 3. Show HN: Magnitude – 面向 Web 应用的开源、AI 原生测试框架

**原文标题**: Show HN: Magnitude – open-source, AI-native test framework for web apps

**原文链接**: [https://github.com/magnitudedev/magnitude](https://github.com/magnitudedev/magnitude)

Magnitude：一个AI原生、开源的Web应用测试框架。它允许用户使用自然语言构建和运行端到端测试，利用视觉AI代理理解并适应UI变化。

其工作原理是：用户用简单的步骤、数据输入和自然语言检查编写测试用例。Magnitude使用强大的通用多模态LLM（如Gemini）作为“规划者”来规划测试策略，并使用快速视觉LLM（Moondream）作为“执行者”以像素级精度与UI交互。如果在执行过程中出现问题，推理代理会介入。

要开始使用，用户需要安装`magnitude-test`包，在其项目中初始化Magnitude，并配置规划者和执行者LLM的API密钥。然后通过`npx magnitude`命令运行测试。Magnitude支持并行测试执行。

该框架专注于简化测试用例的创建，使用户能够像向同事描述一样描述测试。测试可以集成到CI/CD管道中。

Magnitude通过使用专门的模型进行规划和执行，区别于 OpenAI Operator/Claude Computer Use 等解决方案。 这种方法旨在提高专门针对测试场景的速度、可靠性和成本效益。

---

## 4. 肿瘤来源的促红细胞生成素作为癌症免疫中的免疫抑制开关

**原文标题**: Tumor-derived erythropoietin acts as immunosuppressive switch in cancer immunity

**原文链接**: [https://www.science.org/doi/10.1126/science.adr3026](https://www.science.org/doi/10.1126/science.adr3026)

无法访问文章链接。

---

## 5. 大型可重复性项目未能验证生物医学研究。

**原文标题**: Huge reproducibility project fails to validate biomedical studies

**原文链接**: [https://www.nature.com/articles/d41586-025-01266-x](https://www.nature.com/articles/d41586-025-01266-x)

巴西可重复性倡议是一项大型可重复性项目，旨在评估巴西生物医学研究的可重复性，重点关注采用三种常用方法的研究：细胞代谢测定、遗传物质扩增技术和啮齿动物迷宫测试。来自 56 个实验室的 200 多名科学家试图重复 1998 年至 2017 年间发表的 47 篇论文中的实验。

结果令人沮丧，只有不到一半的测试实验可重复。使用五个标准，只有 21% 的实验在至少一半的标准上是可重复的。原始论文中的效应量平均也比重复尝试中的大 60%，表明原始研究倾向于高估干预措施的效果。

该研究强调了加强巴西科学实践的必要性，并为在公共政策和大学内部实施变革提供了基础。这项雄心勃勃的项目在 COVID-19 大流行期间面临物流挑战，并且参与团队在遵守协议方面存在差异。

---

## 6. 致相信人的爱之书

**原文标题**: A Love Letter to People Who Believe in People

**原文链接**: [https://www.swiss-miss.com/2025/04/a-love-letter-to-people-who-believe-in-people.html](https://www.swiss-miss.com/2025/04/a-love-letter-to-people-who-believe-in-people.html)

蒂娜的《致相信他人之人的情书》颂扬了热情带来的变革力量以及成为他人“粉丝”的重要性。她强调，相信某人并为他们的生活带来热情具有感染力且能改变人生。蒂娜用个人轶事来说明这一点，着重介绍了对她的旅程产生重大影响的个人。

她将自己大胆生活的灵感归功于古怪的Hugi阿姨，将职场中展现的善良归功于她的第一任老板Matthew Waldman，将激励她创办自己的设计工作室归功于她的女儿Ella，并将向她展示如何将她的想法变为现实归功于Jim Coudal。她还强调了Ben Chestnut (Mailchimp) 和Ruth Ann Harnisch (Harnisch Foundation) 对 CreativeMornings 的影响，强调了支持性伙伴关系和彻底慷慨的力量。

蒂娜强调了创建以心为本、培养慷慨、善良和好奇心的社区的重要性。她认为，相互支持和彼此信任可以赋予个人力量，让他们发挥潜力并为更美好的未来而努力。最终，她鼓励读者拥抱“粉丝心态”，通过大胆、勇敢和热情来激励他人。这篇文章也是一封献给CreativeMornings社区的情书，分享了他们在创建有意义的人际关系空间方面的经验。

---

## 7. 作为思维工具的符号 (1979)

**原文标题**: Notation as a Tool of Thought (1979)

**原文链接**: [https://www.jsoftware.com/papers/tot.htm](https://www.jsoftware.com/papers/tot.htm)

作为思维工具的记号 (1979) 认为，记号不仅仅是被动的记录系统，而是一种积极且强大的工具，能够塑造和影响我们的思维。该文章强调了记号的选择如何显著影响我们理解、操作和发现新想法的能力。

它强调，好的记号可以通过揭示潜在的结构和关系使复杂问题看起来更简单，而差的记号甚至会模糊最基本的概念。作者很可能讨论了数学、逻辑或计算机科学的例子来阐明这一点，展示了特定记号如何促进特定类型的推理和问题解决。

此外，该文章可能探讨了记号的演变以及它们的发展对于科学和数学进步的重要性。它表明，新记号的发明通常先于理解上的突破，使我们能够以新的方式“看到”问题并开发更有效的解决方案。 本质上，这篇文章提倡认真考虑记号的影响，敦促我们选择甚至发明最能支持我们认知过程并促进智力探索的记号。 中心思想是，记号不仅仅是一种记录思想的方式，更是一种塑造和推进思想的强大工具。

---

## 8. 利用C/C++程序中的未定义行为：性能影响 [pdf]

**原文标题**: Exploiting Undefined Behavior in C/C++ Programs: The Performance Impact [pdf]

**原文链接**: [https://web.ist.utl.pt/nuno.lopes/pubs/ub-pldi25.pdf](https://web.ist.utl.pt/nuno.lopes/pubs/ub-pldi25.pdf)

利用 C/C++ 程序中未定义行为：性能影响

---

## 9. 策略傀儡提示：绕过主流大型语言模型的新方法

**原文标题**: The Policy Puppetry Prompt: Novel bypass for major LLMs

**原文链接**: [https://hiddenlayer.com/innovation-hub/novel-universal-bypass-for-all-major-llms/](https://hiddenlayer.com/innovation-hub/novel-universal-bypass-for-all-major-llms/)

HiddenLayer是一家Gartner认可的AI安全提供商，提供独特的平台来保护企业机器学习模型免受各种威胁。他们专注于保护AI模型，无需增加复杂性或访问敏感数据和算法。他们的平台提供开箱即用的安全性，解决推理、绕过、提取攻击和模型窃取问题。

该公司以其安全至上的方法和避免数据访问要求而著称。HiddenLayer获得了包括微软、Moore Strategic Ventures、Booz Allen Ventures、IBM Ventures和Capital One Ventures在内的重要投资者的支持。

本文提供了HiddenLayer网站各个部分的链接，包括预约演示、平台详情、解决方案、服务、学习资源、合作信息、公司信息、职业、以及联系方式。文章还提到了他们的安全隐私政策、漏洞披露政策、网站地图以及Twitter和LinkedIn的个人资料链接。

本质上，HiddenLayer旨在为AI模型提供强大的安全解决方案，专注于易于实施，并避免不必要的数据或算法访问，这使其成为利用机器学习的企业的宝贵资产。

---

## 10. UIT – 云端大规模、高性能、模块化、低内存文件处理

**原文标题**: UIT – performant, modular, low-memory file processing at scale, in the Cloud

**原文链接**: [https://github.com/janwilmake/uit](https://github.com/janwilmake/uit)

UIT (通用信息终端) 是一个为云端大规模文件处理而设计的库，它具有高性能、模块化和低内存占用等特点。它提供了一个四步流程：摄取、过滤/转换、合并和输出，使用户能够从各种来源收集文件层级结构，应用转换，并以所需的格式输出它们。

UIT通过流式处理和并行化来强调性能，使其能够在Cloudflare Workers等低内存环境中高效运行。它的模块化设计确保了可组合性和对构建块的清晰概览，每个模块都可以潜在地在不同的位置运行。

该库利用FormData处理多个文件和二进制数据，并使用Streams API处理中间结果。它提供了几个模块：`uithub.ingestzip`（ZIP摄取）、`uithub.merge`（FormData合并）、`uithub.outputmd`（Markdown输出）、`uithub.outputzip`（ZIP打包）、`uithub.search`（搜索功能）、`uithub.ziptree`（ZIP层级结构提取）、`uithub.otp`（密钥管理）和`uithub`（UI模块）。

UIT协议定义了UIT模块的约定，将其分为摄取、合并、过滤/转换和输出模块。它指定了用于处理文件的必需的和自定义的FormData标头，包括`Content-Disposition`、`Content-Type`、`x-url`和`x-file-hash`。

UIT鼓励贡献，并旨在创建一个插件系统，以简化文件过滤和转换。该项目是开源的，欢迎开发人员添加模块。它目前处于预发布阶段，并正在寻找赞助商。

---

## 11. 诗歌之城：爱荷华州爱荷华城

**原文标题**: "Poetry City": Iowa City, Iowa

**原文链接**: [https://www.publicbooks.org/poetry-city-iowa-city-iowa/](https://www.publicbooks.org/poetry-city-iowa-city-iowa/)

哈里·斯特科波洛斯的《诗歌之城：爱荷华市，爱荷华》探讨了爱荷华市作为联合国教科文组织文学之都的知名形象与其鲜为人知的反文化中心历史之间的张力。文章突出了该市的文学地位，例如爱荷华作家工作室、人行道上的作家铭牌、众多的文学朗读会以及数千名作家的存在。

然而，斯特科波洛斯认为，在这种主流文学身份之下，潜藏着一种充满活力的反文化。他详细描述了该市的反战行动和艺术实验的历史，提到了丹尼斯·约翰逊、维托·阿孔奇和安娜·门迪埃塔等人物。诸如Dave's Fox Head Tavern和George's Buffet等标志性地点也提醒着人们这段历史。

文章强调了这种反文化精神的持续存在，即使城市更新和房地产开发已经抹去了一些它的物理痕迹。诸如Public Space One和由Anaïs Duplan创立的Afrofuturist研究中心等新机构，都表明了对另类艺术表达的持续承诺。诸如《Vetch: A Magazine of Trans Poetry and Poetics》之类的出版物以及诸如Feed Me Weird Things之类的活动，进一步说明了这一点。

斯特科波洛斯最后认为，保护像爱荷华市这样的大学城的“怪异”对于培养智力和艺术创新、抵制现状以及创作突破性的作品至关重要。这些环境为挑战规范和突破界限提供了独特的机会。

---

## 12. 睡前锻炼与睡眠紊乱有关

**原文标题**: Exercise before bed is linked with disrupted sleep

**原文链接**: [https://medicalxpress.com/news/2025-04-bed-linked-disrupted.html](https://medicalxpress.com/news/2025-04-bed-linked-disrupted.html)

蒙纳士大学一项新研究发现，睡前运动与睡眠紊乱之间存在关联。该研究发表在《自然·通讯》上，利用生物识别设备跟踪了14689名个体一年多的运动、睡眠和心血管数据。

研究表明，睡前四小时内运动，特别是高强度运动，与入睡延迟、睡眠时间缩短、睡眠质量下降、静息心率升高和心率变异性降低有关。这些结果已针对年龄、性别和既往睡眠等因素进行了调整。高强度运动包括显著提高心率和呼吸的活动，如高强度间歇训练或长跑。

研究人员建议，旨在改善睡眠健康的人应在睡前至少四小时结束运动。如果在该时间范围内运动，他们建议进行低强度活动，如慢跑或游泳。该研究强调，傍晚运动，特别是高强度运动，会扰乱睡眠并损害身体的恢复过程。这些发现对于公共健康信息中关于运动时间和强度以改善睡眠健康的信息具有重要意义。

---

## 13. 伟易达苏格拉底教学法

**原文标题**: The VTech Socratic Method

**原文链接**: [https://www.leadedsolder.com/2025/04/22/vtech-socrates-pickup.html](https://www.leadedsolder.com/2025/04/22/vtech-socrates-pickup.html)

本文详细介绍了作者对VTech Socrates（一款1988年的混合型游戏机/电脑）的探索和改造。作者从eBay上购得一台肮脏破损的Socrates，首先对其进行了清洁和拆解。内部组件显示，它采用了Z80处理器、东芝芯片和一个集成门阵列，这在低成本机器中很常见。

一个关键的重点是安装AV改造，以改善视频输出，该改造建立在Johnny Blanchard的更简单设计之上。作者设计了一个带有视频放大器和稳压器的定制PCB，但遇到了几个设计缺陷和组装挑战，包括不良的应力释放和困难的焊接。

随后，作者测试了系统，发现视频可接受，但音频过大。Socrates使用红外键盘，由四节AA电池供电。键盘内部开关的用途仍然是个谜。

最后，作者探索了“环游世界”卡带，识别出一个东芝1Mbit掩模ROM。创建了卡带边缘连接器的引脚图，与VTech Precomputer相似。“环游世界”的ROM位于MAME软件列表中，作者计划利用获得的知识在该系统上运行自定义代码。

---

## 14. 如果我们能从头重建 Kafka 会怎样？

**原文标题**: What If We Could Rebuild Kafka from Scratch?

**原文链接**: [https://www.morling.dev/blog/what-if-we-could-rebuild-kafka-from-scratch/](https://www.morling.dev/blog/what-if-we-could-rebuild-kafka-from-scratch/)

Gunnar Morling的博客文章探讨了从头开始重建Kafka的想法，设想一个为云环境优化的“Kafka.next”。受到Diskless Kafka和AutoMQ等项目的启发，这些项目旨在通过利用对象存储来提高Kafka的弹性和成本效益，Morling提出了这个假想系统的功能愿望清单。

关键功能包括：

*   **消除分区：** 用对象存储取代基于分区的扩展，而是侧重于全局或基于键的排序。
*   **以键为中心的访问：** 允许基于键高效访问和重放消息，从而实现数百万个实体级别的流。
*   **主题层次结构：** 实施结构化的主题标识符，以便高效订阅流的子集。
*   **并发控制：** 为消息键引入乐观锁，以防止写入冲突。
*   **Broker端Schema支持：** 将schema管理直接集成到Kafka中，以获得更好的用户体验，并与Apache Iceberg等格式实现互操作性。
*   **可扩展性和可插拔性：** 通过扩展实现自定义的broker端消息过滤器、转换和存储格式。
*   **同步提交回调：** 保证在确认生产请求时，下游数据视图已更新。
*   **快照：** 通过创建实体状态的快照来支持“逻辑压缩”，从而允许删除较旧的增量事件。
*   **多租户：** 从一开始就以多租户为目标来设计系统。

Morling承认其中一些功能已存在于其他系统中，但他强调了统一开源解决方案的潜力。 他最后建议，基于LSM树的架构可能是构建此类系统的可行选择。

---

## 15. 科学家开发人工树叶，利用阳光生产有价值的化学品

**原文标题**: Scientists Develop Artificial Leaf, Uses Sunlight to Produce Valuable Chemicals

**原文链接**: [https://newscenter.lbl.gov/2025/04/24/scientists-develop-artificial-leaf-that-uses-sunlight-to-produce-valuable-chemicals/](https://newscenter.lbl.gov/2025/04/24/scientists-develop-artificial-leaf-that-uses-sunlight-to-produce-valuable-chemicals/)

劳伦斯伯克利国家实验室的科学家与液态阳光联盟(LiSA)合作，开发出一种“人工叶片”，利用阳光将二氧化碳转化为有价值的C2化学品，这些化学品是塑料和航空燃料等产品的前体。该装置模仿光合作用，将钙钛矿（一种太阳能电池板材料）与铜基电催化剂相结合。

该装置由光阳极和光阴极组成。卤化铅钙钛矿光吸收剂像真叶片中的叶绿素一样吸收光，而受天然酶启发的铜电催化剂则促进二氧化碳的转化。与之前使用生物材料的尝试不同，该系统利用无机铜，使其更耐用和稳定。

使用太阳模拟器测试该装置，证明仅利用阳光即可成功将二氧化碳转化为C2分子。这一突破代表着在可持续生产有价值的化学品和液体燃料方面迈出了重要一步，为减少对化石燃料的依赖和减缓碳排放提供了一种潜在途径。研究人员目前专注于提高系统的效率和可扩展性。这项研究有助于LiSA从阳光、二氧化碳和水中开发液体燃料的总体目标。

---

## 16. Show HN: BugStalker - 一款现代 Rust 调试器

**原文标题**: Show HN: BugStalker - a modern Rust debugger

**原文链接**: [https://github.com/godzie44/BugStalker](https://github.com/godzie44/BugStalker)

BugStalker：一款现代 Rust 调试器，专为 Linux x86-64 架构上的 Rust 程序调试而设计。主要功能包括断点、单步执行以及信号/观察点处理等核心调试功能。它提供高级运行时检查，支持完整的多线程、数据查询表达式以及深度 Rust 类型系统集成（包括对集合、智能指针和线程本地存储的支持）。它利用 `core::fmt::Debug` trait 进行变量渲染。

BugStalker 提供灵活的界面，允许用户在控制台和 TUI 模式之间切换，并支持异步 Rust 调试，包括 Tokio 运行时检查。该调试器具有可扩展的架构，带有 Oracle 扩展机制，包括一个内置的 Tokio oracle（类似于 tokio_console，但无需修改代码）。

该项目鼓励贡献、欢迎建议并提供贡献指南。BugStalker 在 MIT 许可证下发布。安装说明可在项目网站上找到。

---

## 17. 我给GPLv2许可协议声明中的地址写了信（2022年）。

**原文标题**: I wrote to the address in the GPLv2 license notice (2022)

**原文链接**: [https://code.mendhak.com/gpl-v2-address-letter/](https://code.mendhak.com/gpl-v2-address-letter/)

2022年，作者出于对GPLv2许可证声明中物理地址（追溯到1991年，当时互联网普及率较低）的好奇，决定写信给自由软件基金会(FSF)，请求一份许可证副本。作者最初咨询了Open Source Stack Exchange，以了解为什么使用物理地址而不是URL。

作者在获取合适的邮资方面遇到了挑战。英国的国际回邮券已经停止使用，因此作者转向eBay购买美国邮票，短暂地接触了集邮的世界。在收到一枚圆形的“非洲雏菊全球永久绿色双联邮票”后，作者准备了请求信，写上FSF的地址，并从英国寄出。

五周后，作者收到了来自FSF的回信，其中包含完整的许可证文本。然而，收到的许可证是GPLv3，而不是GPLv2。印刷文本采用的是美国信纸尺寸，进一步突显了FSF的地理背景。虽然作者在请求中没有明确指定GPLv2，但他们想知道许可证声明中的地址是否应该是一个线索。最终，作者决定不再寻求更正，并对收到任何版本的许可证感到满意，在邮寄这项工作之后需要休息。

---

## 18. 一款两万美元美国产无漆、无音响、无屏幕的电动皮卡

**原文标题**: A $20k American-made electric pickup with no paint, no stereo, no screen

**原文链接**: [https://www.theverge.com/electric-cars/655527/slate-electric-truck-price-paint-radio-bezos](https://www.theverge.com/electric-cars/655527/slate-electric-truck-price-paint-radio-bezos)

Slate卡车：一款价格低于2万美元的美国产电动皮卡（补贴后），将以其极简主义的方式颠覆电动汽车市场。这款由密歇根州Slate Auto生产的双座电动汽车，拥有150英里的续航里程和实用主义设计。主要特点包括无喷漆（采用注塑聚丙烯复合材料）、无音响、无触摸屏，强调耐用性、定制性和经济性。

Slate的设计理念围绕着拥抱不完美，并提供广泛的个性化选项，包括DIY乙烯基贴膜套件和可选的带后排座椅的SUV升级套件。通过取消喷漆车间和使用塑料车身面板，生产过程得到了极大的简化，从而降低了生产成本，并使得在印第安纳州的工厂占地面积更小。

该公司正在采用类似于特斯拉的直销模式，绕过传统的经销商。Slate鼓励用户自行维护，并提供“Slate大学”的支持，当然也会与已建立的服务中心合作，以满足那些喜欢专业帮助的用户的需求。

缺少信息娱乐系统旨在提高可靠性并减少保修索赔。虽然基本款缺乏娱乐功能，但内饰设计便于升级。Slate的目标是获得高安全评级。预计将于2026年末开始交付。该公司已吸引了大量投资，据报道包括杰夫·贝佐斯。Slate卡车的成功取决于消费者是否愿意接受一款精简且高度可定制的电动汽车。

---

## 19. 我为落榜高中生做了个大学出气筒。

**原文标题**: I made a college punching bag for rejected highschoolers

**原文链接**: [https://ex.plor.ing/blog/post/college-punch](https://ex.plor.ing/blog/post/college-punch)

好的，根据标题“我为被大学拒绝的高中生做了一个大学出气筒”以及提到的“PLOR 终端”，以下是一个摘要，假设它很可能是一篇讽刺或带有黑色幽默的作品：

文章可能描述了一个虚构的或比喻性的“大学出气筒”，通过 PLOR 终端（本身暗示着编码或技术背景）创建。这个“出气筒”为被理想大学拒绝的高中生提供了一个发泄渠道。

作者可能使用 PLOR 终端来创建一个数字或互动平台，让这些被拒绝的学生可以发泄他们的沮丧。这个“出气筒”的性质可能有所不同：

*   **一个数字头像：**学生们或许可以创建代表大学申请过程的各个方面，甚至包括招生官的漫画形象的头像，并虚拟地“攻击”他们。

*   **一个数据驱动的模拟：**PLOR 终端可能被用来模拟不同的大学录取场景，允许学生重新审视他们的申请，并探索假设场景（即使是以一种徒劳或幽默的方式）。

*   **一个具有特定目标工具的社区论坛：**“出气筒”可能是一个学生可以分享他们经历的论坛，但 PLOR 终端可能被用来过滤和展示内容，以一种放大负面情绪或强化大学申请过程不公平的方式。

文章可能使用讽刺来评论大学录取的巨大压力和情感损失，特别是被拒绝的失望。它可能探讨应对机制、申请过程的荒谬性以及高中生的情感脆弱性等主题。语气可能黑暗而幽默，使用“出气筒”的概念来突出这个压力时期中的挫折和焦虑。PLOR 终端元素增加了一层技术评论，或许暗示了技术如何被用来加剧和缓解这些焦虑。

---

## 20. OpenAI 在 API 中发布图像生成功能

**原文标题**: OpenAI releases image generation in the API

**原文链接**: [https://openai.com/index/image-generation-api/](https://openai.com/index/image-generation-api/)

OpenAI 通过公共 API 发布图像生成功能，允许开发者使用 DALL·E 3 以编程方式创建和编辑图像。与通过 Web 界面使用 DALL·E 相比，这个新 API 具有显著优势，包括更大的控制力、自动化和可扩展性。

API 的主要特性和优势包括：

*   **直接集成：** 开发者现在可以将 DALL·E 3 图像生成直接无缝地集成到他们的应用程序、工作流程和服务中。
*   **自动化和可扩展性：** 自动化图像创建任务并更高效地生成大量图像。
*   **更大的控制力：** API 可以对图像大小、质量和样式等参数进行精细控制。
*   **文本生成图像和图像编辑：** API 支持从文本提示生成图像（文本生成图像）和基于提示编辑现有图像。
*   **成本节约：** OpenAI 声称，与 Web 界面相比，对于大批量图像生成而言，使用 API 可以更具成本效益。
*   **安全措施：** OpenAI 强调其对安全和负责任的 AI 开发的承诺。API 包含保护措施，以防止生成不适当或有害内容，包括监控和内容审核。
*   **用例：** 该公告强调了各种用例，例如创建营销材料、为电子商务生成图像、为社交媒体设计图形以及开发创意应用程序。
*   **可用性：** 图像生成 API 现在已普遍向开发者开放。

本质上，此公告标志着在普及高级图像生成技术方面迈出了重要一步，使开发者能够在自己的应用程序和工作流程中利用 DALL·E 3 的强大功能。

---

## 21. FBI逮捕威斯康星州法官，指控其妨碍移民逮捕

**原文标题**: FBI arrests Wisconsin judge on charges of obstructing immigrant arrest

**原文链接**: [https://www.washingtonpost.com/national-security/2025/04/25/wisconsin-judge-arrest-fbi-ice-immigration-enforcement/](https://www.washingtonpost.com/national-security/2025/04/25/wisconsin-judge-arrest-fbi-ice-immigration-enforcement/)

无法访问文章链接。

---

## 22. Tarpit想法：什么是Tarpit想法以及如何避免它们 (2023) [视频]

**原文标题**: Tarpit ideas: What are tarpit ideas and how to avoid them (2023) [video]

**原文链接**: [https://www.ycombinator.com/library/Ij-tarpit-ideas-what-are-tarpit-ideas-how-to-avoid-them](https://www.ycombinator.com/library/Ij-tarpit-ideas-what-are-tarpit-ideas-how-to-avoid-them)

Y Combinator 视频《泥潭式创业点子——什么是泥潭式点子以及如何避免》很可能讨论的是那些最初看起来很有希望或有利可图，但实际上会困住创业者并导致失败的创业点子。 这些“泥潭式点子”的特征往往是缺乏经验的创始人容易忽略的常见陷阱。

该视频可能解释了这些点子的吸引力在于它们针对的是一个庞大的市场，具有很高的潜在收入，或者基于个人的挫败感。 然而，它们通常涉及：

*   **高准入门槛：** 需要大量资本、监管障碍或难以获得的合作关系。
*   **来自现有企业的激烈竞争：** 进入一个由资金雄厚的现有企业主导的市场，这些企业可以轻松地击败一家新的初创公司。
*   **需求疲软或缺乏货币化：** 解决人们实际上没有的问题，或者难以找到可行的商业模式来产生收入。
*   **重大的技术挑战：** 依赖未经证实或不成熟的技术，这些技术难以开发或成本高昂。
*   **对客户行为的不切实际的假设：** 假设客户会轻易接受新产品或服务，而没有考虑到现有的习惯和偏好。

为了避免泥潭式点子，该视频很可能建议创业者：

*   **彻底验证他们的想法：** 进行市场调研，与潜在客户交谈，并构建一个最小可行产品（MVP）来测试假设。
*   **专注于为利基市场解决特定问题：** 针对较小、明确的受众群体可以更快地迭代和更容易地验证。
*   **分析竞争格局：** 识别现有竞争对手并了解他们的优势和劣势。
*   **考虑监管环境：** 确保该想法符合所有适用的法律法规。
*   **对挑战和风险保持现实：** 承认潜在的陷阱并制定计划来减轻它们。

---

## 23. OpenVSX宕机24小时，VSCode分支依赖其扩展

**原文标题**: OpenVSX, which VSCode forks rely on for extensions, down for 24 hours

**原文链接**: [https://status.open-vsx.org/](https://status.open-vsx.org/)

OpenVSX注册表（作为VS Code分支的关键扩展市场）已宕机约24小时。 该中断始于4月24日左右（基于更新的时间戳），影响了包括主页、查询API、搜索API和VSCode Assets API在内的多个核心服务。 问题源于OpenVSX后端存储出现问题，导致服务无法正确启动。 OpenVSX团队正在积极解决该问题，并提供最新情况，在4月25日的最新更新之前至少有4次更新。 这次宕机严重影响了依赖OpenVSX来发现、安装和管理替代VS Code编辑器扩展的开发者和用户。 服务至少从4月23日开始就已宕机。

---

## 24. 异步Rust的视觉之旅

**原文标题**: A Visual Journey Through Async Rust

**原文链接**: [https://github.com/alexpusch/rust-magic-patterns/blob/master/visual-journey-through-async-rust/Readme.md](https://github.com/alexpusch/rust-magic-patterns/blob/master/visual-journey-through-async-rust/Readme.md)

异步Rust的并发与并行：可视化探索

本文通过可视化方式探索了异步Rust的并发与并行，强调理解CPU密集型代码如何影响异步执行的重要性。作者通过正弦波计算的可视化演示，表明Tokio futures 以并发方式执行，而非并行方式，除非进行显式管理。

核心要点是，单个Tokio任务中的CPU密集型操作可能会阻塞异步执行器，从而对其他并发任务产生负面影响。即使看似很短的CPU密集型任务也可能导致显著的延迟。然后，作者探讨了使用 `tokio::spawn` 创建新任务，允许 futures 在不同的线程上并行运行，从而利用多个CPU内核并隔离CPU密集型操作。可视化清晰地展示了生成任务如何通过防止一个长时间运行的操作阻塞其他操作来提高整体性能。

然而，本文警告说，生成过多的任务可能会导致竞争并降低性能增益，因为Tokio会在可用线程之间调度任务。最后，介绍了 `tokio::task::spawn_blocking`，作为一种将阻塞（非异步）代码卸载到专用线程池的方法，从而可能实现最大的CPU利用率。 虽然可视化效果令人满意，但作者正确地指出，这些线程之间的上下文切换仍然会影响性能，并建议探索其他处理CPU密集型任务的方案。作者总结说，可视化异步任务有助于掌握异步Rust的细微差别，特别是多核利用率以及并发/并行的权衡。

---

## 25. 用 Ruby 写一个解释器

**原文标题**: Write an Interpreter in Ruby

**原文链接**: [https://speakerdeck.com/marioariasc/write-an-interpreter-in-ruby](https://speakerdeck.com/marioariasc/write-an-interpreter-in-ruby)

无法访问文章链接。

---

## 26. Show HN: Logiquiz – 每日自引用谜题

**原文标题**: Show HN: Logiquiz – Daily Self-Referential Puzzles

**原文链接**: [https://www.logiquiz.com/](https://www.logiquiz.com/)

逻辑测验是一种自指测验，题目会引用测验本身或测验内的其他题目。答案取决于测验的内容和结构，从而构成一个使用逻辑和演绎推理来解决的元谜题。

目标是正确回答所有问题，每个问题旁边的绿色条表示答案正确。点击答案一次标记为错误，点击两次标记为正确；每个问题只有一个正确答案。当所有条都是绿色时，表示逻辑有效，测验完成。

建议的策略包括：

*   阅读所有问题以了解结构。
*   识别并标记明显错误的答案。
*   解决直接的问题或提供线索的问题。
*   跟踪潜在答案并随着进度的推进进行调整。
*   根据新信息重新审视和更新答案。

描述强调了逻辑和演绎推理的重要性，因为每个答案都会影响测验中其他问题的有效性。这些谜题的复杂程度各不相同，需要考虑每个答案对整个测验的影响。

---

## 27. GCC，GNU编译器套件 15.1 发布

**原文标题**: GCC, the GNU Compiler Collection 15.1 released

**原文链接**: [https://gcc.gnu.org/gcc-15/](https://gcc.gnu.org/gcc-15/)

GNU编译器套件（GCC）15.1版本已于2025年4月25日发布。这是一个主要版本，相比GCC 14.x，包含了新的功能和改进。

GCC最初代表GNU C编译器，现在代表GNU编译器套件，因为它支持C语言之外的多种语言。此版本的发布归功于众多志愿者的贡献，他们提供了新的功能、改进、错误修复、测试结果和其他更改。

公告指引用户访问GCC项目网站和邮件列表以获取更多信息和获取软件。它还建议查阅网页和手册以解决使用问题，gcc-help邮件列表可提供进一步的帮助。欢迎在开发者列表上提出对GCC开发的意见和反馈。

---

## 28. 新分析质疑在K2-18B行星上发现的“生物特征”

**原文标题**: New analysis casts doubt on 'biosignatures' found on planet K2-18B

**原文链接**: [https://www.npr.org/2025/04/25/g-s1-62610/biosignatures-k2-18b-james-webb-exoplanet-doubt](https://www.npr.org/2025/04/25/g-s1-62610/biosignatures-k2-18b-james-webb-exoplanet-doubt)

关于系外行星K2-18b大气层中“生物特征”探测结果的争议

---

## 29. 在 DuckDB UI 中实时输入 SQL 语句并获得结果

**原文标题**: Instant SQL for results as you type in DuckDB UI

**原文链接**: [https://motherduck.com/blog/introducing-instant-sql/](https://motherduck.com/blog/introducing-instant-sql/)

本文宣布在 MotherDuck 中发布 Instant SQL 和 DuckDB 本地 UI，这是一项新功能，可在您键入 SQL 查询时提供实时结果集预览。其目标是通过消除传统的编写-运行-等待循环来加快查询构建和调试。

Instant SQL 提供以下几个主要优势：

*   **实时预览：** 在您键入时更新结果集，从而实现即时反馈。
*   **CTE 检查：** 能够即时可视化和调试公共表表达式 (CTE)。
*   **表达式分解：** 允许用户剖析复杂的列公式以查明问题。
*   **广泛的数据源支持：** 适用于 DuckDB 表、MotherDuck、S3、Postgres、SQLite、MySQL、Iceberg 和 Delta。
*   **AI 集成：** 提供 AI 驱动的编辑建议的即时预览。

本文重点介绍了使 Instant SQL 成为可能的技术创新，包括 DuckDB 的本地优先设计和性能、查询重写功能、精密的缓存系统，以及用于预览特定查询部分的游标到 AST 的映射。

此次发布旨在将 SQL 工作流程转变为一个更流畅的探索和发现过程。本文鼓励用户尝试 Instant SQL 并提供反馈，还包括 MotherDuck 招聘数据密集型界面构建人员的招聘广告。

---

## 30. 一次量子跃迁产生21厘米的光

**原文标题**: One quantum transition makes light at 21 cm

**原文链接**: [https://bigthink.com/starts-with-a-bang/21cm-magic-length/](https://bigthink.com/starts-with-a-bang/21cm-magic-length/)

本文阐述了中性氢原子发出的21厘米波长光作为研究宇宙，尤其是其早期阶段的工具的重要性。这种辐射源于一种被称为自旋翻转跃迁的量子跃迁，氢原子中的电子相对于质子从对齐的自旋状态变为反向对齐的自旋状态。这种跃迁非常独特，因为它非常精确，产生的光具有非常窄且定义明确的波长。

作者解释了原子只能存在于特定的能量构型中，从而导致在离散波长处吸收和发射光。虽然“粗结构”跃迁很常见，但“精细”和“超精细”结构，如自旋翻转跃迁，提供了更详细的见解。量子隧穿效应允许这种“禁阻”跃迁发生，尽管每个原子平均需要1000万年。

氢的丰富性（占早期宇宙中原子的92%）使得这种21厘米辐射成为绘制中性氢气分布的强大工具，即使在没有恒星形成的区域也是如此。通过观察来自遥远气体云的红移21厘米信号，天文学家希望探测早期宇宙，并更好地了解其演化，包括第一批恒星和星系的形成。文章最后强调了21厘米天文学在揭示隐藏在宇宙过去深处的秘密方面的潜力。

---

## 31. 避免人工智能时代技能退化

**原文标题**: Avoiding Skill Atrophy in the Age of AI

**原文链接**: [https://addyo.substack.com/p/avoiding-skill-atrophy-in-the-age](https://addyo.substack.com/p/avoiding-skill-atrophy-in-the-age)

无法访问文章链接。

---

## 32. PyGraph：PyTorch中CUDA图的稳健编译器支持

**原文标题**: PyGraph: Robust Compiler Support for CUDA Graphs in PyTorch

**原文链接**: [https://arxiv.org/abs/2503.19779](https://arxiv.org/abs/2503.19779)

PyGraph：PyTorch中CUDA图的稳健编译器支持

这篇arXiv文章“PyGraph：PyTorch中CUDA图的稳健编译器支持”介绍了PyGraph，一种在PyTorch 2框架内自动利用CUDA图的新方法。CUDA图是NVIDIA GPU最近的一项硬件特性，旨在通过将GPU任务捕获并作为DAG启动来减少CPU启动开销。然而，它们的静态结构和数据复制开销通常会导致实际性能下降。

作者通过PyGraph中体现的三个关键优化来应对这些挑战。首先，PyGraph使CUDA图能够更广泛地部署。其次，它减少了GPU内核参数复制开销。第三，它基于成本效益分析选择性地部署CUDA图。这种选择性部署承认CUDA图并非总是受益，并使用性能建模来确定它们何时会提供净收益。

PyGraph与PyTorch 2的编译工具链无缝集成，使开发人员无需手动修改代码即可受益于CUDA图。作者在各种机器学习基准测试中评估了PyGraph，与仅使用PyTorch 2 相比，展示了显著的性能提升。该研究强调了智能编译器支持对于像CUDA图这样的硬件特性至关重要，以充分释放它们在深度学习框架中的潜力。

---

## 33. 孟德尔豌豆的百年遗传谜团已解开

**原文标题**: Century-old genetics mystery of Mendel's peas solved

**原文链接**: [https://www.nature.com/articles/d41586-025-01269-8](https://www.nature.com/articles/d41586-025-01269-8)

围绕孟德尔豌豆实验的百年遗传谜团已解开。研究人员已确定了导致孟德尔研究的豌豆七种性状中的三种的基因，具体来说是豆荚颜色、豆荚形状和花序排列（束生）。

---

## 34. 你可以成为伟大的设计师，而且默默无闻

**原文标题**: You Can Be a Great Designer and Be Completely Unknown

**原文链接**: [https://www.chrbutler.com/you-can-be-a-great-designer-and-be-completely-unknown](https://www.chrbutler.com/you-can-be-a-great-designer-and-be-completely-unknown)

克里斯托弗·巴特勒的文章认为，真正的设计伟大并非由名气或认可来定义，而是由设计本身的有效性和实用性来定义。他挑战了现代“注意力经济”，在其中社交媒体的存在感和奖项常常被误认为是设计成功，他认为许多卓越的设计因为其与日常生活的无缝融合而变得隐形。一个舒适的削皮器或一个直观的高速公路标志等例子都说明了这一点。

巴特勒认为，伟大的设计师往往默默无闻，因为他们的重点是解决问题和满足人类需求，而不是自我宣传。他告诫人们不要将可见性置于实用性之上，这可能导致糟糕的设计选择，而这些选择是出于对关注的渴望而非功能性。他承认应得的认可的价值，但坚持认为质量和名气并非强相关，尤其是在产品迅速过时的快速发展的数字设计领域。作者总结说，最深刻的设计成就恰恰是那些变得如此重要和不引人注目以至于融入背景之中的设计，就像重力或空气一样，突出了那些无名英雄的“隐形伟大”。

---

## 35. SIMD ISA 的根本缺陷 (2021)

**原文标题**: Fundamental flaws of SIMD ISAs (2021)

**原文链接**: [https://www.bitsnbites.eu/three-fundamental-flaws-of-simd/](https://www.bitsnbites.eu/three-fundamental-flaws-of-simd/)

本文 критикует 对 (packed SIMD ISAs) 打包 SIMD 指令集架构 (通常 в потребительских CPUs встречается) 一般在消费级 центральным процессором встречается, 它 (highlighting) 突出 (three fundamental flaws) 三个基本缺陷: (fixed register width) 固定寄存器宽度, (pipelining issues) 流水线问题 и (cumbersome tail handling) 笨拙的尾部处理.

(The fixed register width) 固定寄存器宽度 (necessitates) 需要 (new instructions and registers) 新指令和寄存器 (for increased parallelism) 用于提高并行性, (complicating) 复杂化 (ABI updates) 应用程序二进制接口更新, (OS kernel modifications) 操作系统内核修改, (compiler support) 编译器支持 и (debugger adaptation) 调试器适配. (This also leads to instruction set bloat) 这也导致指令集臃肿, (as older SIMD generations become redundant) 因为较旧的 SIMD 版本变得多余, (forcing developers to target multiple SIMD versions) 迫使开发人员 (to target) 面向 (multiple SIMD versions) 多个 SIMD 版本 (for optimal performance across different CPUs) 以在不同的中央льным процессором на разных производительности обеспечивают.

(Pipelining SIMD operations) 流水线 SIMD 操作, (requiring multiple clock cycles) 需要多个时钟周期, (necessitates loop unrolling) 需要循环展开 (to avoid stalls and keep the pipeline busy) 以避免停顿并保持流水线繁忙. (This, however, increases code size) 然而, 这会增加代码大小, (negatively impacting instruction cache performance) 对指令缓存性能产生负面影响 и (increasing register pressure) 增加寄存器压力, (requiring more SIMD registers to avoid spilling) 需要更多的 SIMD 寄存器以避免溢出.

(Finally, tail handling) 最后, 尾部处理, (where the number of array elements isn't a multiple of the SIMD register size) 其中数组元素的数量不是 SIMD 寄存器大小的倍数, (adds extra code and control logic) 添加额外的代码和控制逻辑 (before and after the main loop) 在主循环之前和之后, (further increasing code size and complexity) 进一步增加代码大小和复杂性.

(The article proposes alternatives) 本文提出了替代方案, (like Vector Processors) 例如向量处理器 (e.g., Cray-1, RISC-V RVV, ARM SVE) (which handle unrolling and tailing in hardware) 它们在硬件中处理展开和尾部处理, (resulting in more compact and efficient code) 从而产生更紧凑和高效的代码. (It also mentions the Virtual Vector Method (VVM) employed by My 66000) 它还提到了 My 66000 采用的虚拟向量方法 (VVM), (enabling vectorization without vector registers) 无需向量寄存器即可实现向量化. (Code examples demonstrate the relative complexity and verbosity of a packed SIMD implementation versus vector and predicated SIMD implementations.) 代码示例展示了打包 SIMD 实现相对于向量和断言 SIMD 实现的相对复杂性和冗长性。

---

## 36. 查询数据的原则性方法——类型安全的搜索DSL

**原文标题**: A Principled Approach to Querying Data – A Type-Safe Search DSL

**原文链接**: [https://www.claudiu-ivan.com/writing/search-dsl](https://www.claudiu-ivan.com/writing/search-dsl)

本文介绍了一种类型安全的搜索系统，该系统使用为查询“问题”而定制的领域特定语言 (DSL) 构建，“问题”是项目管理中常见的概念。其核心思想是利用 DSL 实现富有表现力和可维护的搜索，受益于可控的复杂性、领域对齐、增强的可用性以及简化可维护性和可扩展性的形式语法。

该系统定义了一个 `Issue` 接口来表示数据结构，并利用 `Either` 类型在解析过程中进行稳健的错误处理。Parser combinators，一种函数式编程技术，被用来模块化地构建解析器。这些 combinators，如 `lit`、`word`、`alt`、`seq`、`many` 和 `map`，将解析过程分解为更小的、可组合的单元。

本文强调创建抽象语法树 (AST) 来表示查询的结构，将语法与语义分离，以便进行优化和灵活性。然后，AST 被转换为 `IssuePredicate` 函数以进行过滤。`executeQuery` 函数协调整个过程，处理解析错误并将谓词应用于数据。

虽然适用于中等数据集，但本文承认由于其线性扫描方法，在大型数据集上的性能存在限制。它建议使用索引、查询优化、查询计划和缓存策略来提高性能，并可能利用 IndexedDB 或 SQLite 等数据库解决方案进行存储。结论强调了原则性方法的好处，强调了类型安全、函数式编程和关注点分离，以构建强大且用户友好的搜索体验。

---

## 37. 展示一下：我为文本机器人和迷你应用打造了 Lovable

**原文标题**: Show HN: I built Lovable for text bots and mini apps

**原文链接**: [https://plutonic.dev](https://plutonic.dev)

Show HN: 我构建了用于文本机器人和迷你应用的Lovable

“Show HN: 我构建了用于文本机器人和迷你应用的Lovable”帖子介绍了“Plutonic”，一个旨在帮助用户创建智能文本机器人和迷你应用程序的平台。虽然提供的内容非常简短，但我们可以推断出 Plutonic 旨在简化构建和部署这些类型应用程序的过程，可能提供以下功能：

*   **机器人创建：** 用于设计和开发对话机器人的功能，可能处理诸如理解用户输入、制定响应和管理对话流程等任务。
*   **迷你应用开发：** 用于构建和托管小型、专注的应用程序的工具和基础设施，可能与消息传递平台或其他服务集成。
*   **智能化：** 该平台似乎强调智能能力，可能结合了自然语言处理 (NLP)、机器学习 (ML) 或 AI 驱动的功能，以提高机器人的理解和性能。
*   **用户友好性：** 鉴于名称“Lovable”，该平台可能优先考虑易用性和积极的开发者体验。

本质上，Plutonic 可能将自己定位为用于创建和部署智能文本机器人和迷你应用程序的综合解决方案，提供一系列工具和功能来简化开发过程。

---

## 38. 展示HN：Faasta - 一个用Rust编写的自托管的WASM-wasi-HTTP Serverless平台

**原文标题**: Show HN: Faasta – A self-hosted Serverless platform for WASM-wasi-HTTP in Rust

**原文链接**: [https://github.com/fourlexboehm/faasta](https://github.com/fourlexboehm/faasta)

Faasta是一个高性能、自托管的函数即服务（FaaS）平台，围绕WebAssembly (WASM)构建。它强调速度和效率，通过利用WASI P2和WASIHTTP标准，拥有亚毫秒级的冷启动时间和极小的内存占用。

主要特性包括将代码作为WebAssembly模块运行，安全的沙盒函数隔离，超快速的冷启动，易于自托管，以及由于其标准合规性而带来的可移植性。该平台由Wasmtime驱动，用于高效的WASM执行，并在faasta.xyz提供免费的托管实例。

摘要还强调使用WASI P2和WASIHTTP来标准化HTTP处理，实现基于组件的架构，并促进函数在支持这些标准的不同运行时之间的可移植性。

提供了入门指南，包括安装Faasta CLI，创建和构建项目，使用GitHub登录，以及部署函数。文章明确指出Faasta目前处于实验阶段，可能会有重大更改。

---

## 39. 宁德时代 Naxtra 钠离子电池发布会要点

**原文标题**: Key Takeaways from CATL's Naxtra Sodium-Ion Battery Launch

**原文链接**: [https://www.batterytechonline.com/materials/5-key-takeaways-from-catl-s-naxtra-sodium-ion-battery-launch](https://www.batterytechonline.com/materials/5-key-takeaways-from-catl-s-naxtra-sodium-ion-battery-launch)

无法访问文章链接。

---

## 40. 粗心的人

**原文标题**: Careless People

**原文链接**: [https://pluralistic.net/2025/04/23/zuckerstreisand/#zdgaf](https://pluralistic.net/2025/04/23/zuckerstreisand/#zdgaf)

本文评述了莎拉·温恩-威廉姆斯的回忆录《漫不经心的人》，该书详细描述了她在Facebook从事全球政策方面的工作经历。书评重点介绍了温恩-威廉姆斯从新西兰外交部门的一名小职员，因对Facebook的潜力充满热情，到成为该公司全球扩张的关键人物的历程。

这本书揭露了Facebook高层管理人员，包括马克·扎克伯格、谢丽尔·桑德伯格和乔尔·卡普兰的机能失调和常常不道德的行为。扎克伯格被描绘成不成熟且不愿听取简报，桑德伯格则被描绘成自我推销和玩弄小手段，而卡普兰则被描绘成麻木不仁和笨拙。书评强调了Facebook最初对美国以外的国家不感兴趣，这是因为美国市场因其庞大的人口和缺乏隐私保护而具有盈利能力。

随着Facebook在美国市场饱和，它将注意力转向全球扩张，这使得温恩-威廉姆斯的工作至关重要。然而，由于粗心和傲慢，公司的领导者经常错失机会。书评还强调了卡普兰对温恩-威廉姆斯的性骚扰，这件事没有得到掌权者的处理。

书评讨论了Facebook对中国市场的无情追求，包括扎克伯格试图拉拢习近平但未果，以及该公司为取悦中国政府而愿意提供监控和审查。最终，温恩-威廉姆斯对Facebook的行为感到失望并离开了公司，她亲眼目睹了该公司漫不经心和残酷的行为。作者将这种行为与维持高增长以维持其股价和竞争优势的压力联系起来。

---

## 41. DeepMind发布Lyria 2音乐生成模型

**原文标题**: DeepMind releases Lyria 2 music generation model

**原文链接**: [https://deepmind.google/discover/blog/music-ai-sandbox-now-with-new-features-and-broader-access/](https://deepmind.google/discover/blog/music-ai-sandbox-now-with-new-features-and-broader-access/)

DeepMind发布Lyria 2音乐生成模型，并更新音乐AI沙盒，在美国扩大音乐家访问权限。Lyria 2提供高保真音乐生成和专业级音频输出，捕捉跨流派的细微差别。他们还开发了Lyria RealTime，可实现音乐的交互式创作和实时控制，包括流派混合和即时创意探索。

音乐AI沙盒与音乐家合作开发，提供“创建”（从提示生成音乐样本）、“扩展”（生成现有作品的延续）和“编辑”（使用文本提示和直观控件重塑音乐）等实验性工具。音乐家们正在使用沙盒克服创作瓶颈，产生新的音乐创意，并尝试不同的风格。多位艺术家引用了沙盒的实用性。

Lyria 2和Lyria RealTime生成的所有音乐都使用SynthID技术进行水印标记，以确保负责任的部署。DeepMind强调与音乐社区合作，建立信任并赋能创作者，并鼓励感兴趣的艺术家注册音乐AI沙盒的候补名单。

---

## 42. 作业5：汽车与钥匙扣 (2021)

**原文标题**: Assignment 5: Cars and Key Fobs (2021)

**原文链接**: [https://web.stanford.edu/class/ee26n/Assignments/Assignment5.html](https://web.stanford.edu/class/ee26n/Assignments/Assignment5.html)

本作业深入探讨了汽车钥匙遥控器和遥控无钥匙系统(RKS)的安全漏洞。它以2006款普锐斯钥匙遥控器为例，解释了这些系统的工作原理，以及如何使用SDR识别频率和分析信号。 文中告诫不要过度按压按钮，这可能会导致遥控器失去同步。

作业随后概述了各种攻击，包括重放攻击（记录和重新传输信号）、干扰以及针对被动无钥匙进入和启动（PKES）系统的攻击，这些系统容易受到扩展钥匙遥控器范围的中继设备的攻击。

其中很大一部分内容集中在VW RKS系统上，重点介绍了一个长达20年的漏洞，该漏洞在数百万辆汽车中使用了通用加密密钥。 攻击者可以从汽车的ECU固件中提取密钥并克隆钥匙遥控器。

作业最后列出了四个供学生探索的选择，每个选择都需要一个5页的幻灯片演示：调查Subaru RKS系统，研究Flipper Zero及相关争议，分析工业机器的黑客攻击，或发现并解释另一个有趣的汽车黑客攻击。 学生被引导调查娱乐系统，特别是Jeep上的Uconnect黑客攻击以及特斯拉/本田的漏洞。 最后，欢迎学生向作者发送电子邮件，告知课程进展情况。

---

## 43. 发布HN：Cua (YC X25) – 计算机使用代理的开源Docker容器

**原文标题**: Launch HN: Cua (YC X25) – Open-Source Docker Container for Computer-Use Agents

**原文链接**: [https://github.com/trycua/cua](https://github.com/trycua/cua)

Cua (计算机使用代理) 是一个开源框架，使人工智能代理能够在高性能虚拟容器中控制完整的操作系统，在 Apple Silicon 上实现高达 97% 的原生速度。它提供基于 Lume CLI（基于 Apple 的 Virtualization.Framework）的高性能虚拟化，以及一个计算机使用界面，允许人工智能代理与这些虚拟环境交互并控制它们，以执行浏览、编码和运行复杂工作流等任务。

主要优势包括：通过在虚拟环境中运行代理来增强安全性与隔离性，接近原生性能，运行 macOS 或 Linux 的灵活性，可重现的环境，以及内置的 LLM 集成。

要开始使用，用户可以仅安装用于虚拟化的 Lume CLI，或者安装 Lume 和 Python 库（`cua-computer`，`cua-agent`）以获得完整的代理功能。该项目还提供从源代码构建的选项，以便访问最新功能。该框架构建为一个单体仓库，包含用于 VM 管理（Lume）、计算机使用界面（`cua-computer`）和代理框架（`cua-agent`）的库。提供演示来展示 Cua 的功能，并鼓励用户为项目做出贡献并加入 Discord 社区。Cua 在 MIT 许可证下获得许可，Microsoft 的 OmniParser 使用 CC-BY-4.0 许可证。它需要一台配备 Apple Silicon 的 Mac 和 macOS 15+。

---

## 44. Show HN: Colanode，开源且本地优先的 Slack 和 Notion 替代方案

**原文标题**: Show HN: Colanode, open-source and local-first Slack and Notion alternative

**原文链接**: [https://github.com/colanode/colanode](https://github.com/colanode/colanode)

Colanode：一个开源、本地优先的协作平台，旨在替代 Slack 和 Notion 等工具，通过自托管强调数据隐私和控制。它是一个集实时聊天、富文本页面（类似于 Notion）、可定制数据库（表格、看板、日历）和文件管理于一体的全能工作空间。Colanode 专为个人和团队设计，提供连接到自托管服务器的桌面应用程序，或者为了方便测试，项目方提供免费的 beta 云服务器。

其核心创新在于本地优先的工作流程，所有更改都使用 SQLite 本地保存，然后同步到服务器，从而实现离线工作和即时数据访问。通过 Yjs 驱动的无冲突复制数据类型 (CRDT) 支持并发编辑，确保同时编辑的平稳合并。

要开始使用，用户可以下载桌面应用程序并连接到 Colanode Cloud（欧盟或美国）的 beta 服务器，或者使用 Docker 进行自托管。自托管需要带有 pgvector 扩展的 Postgres、Redis（或 Valkey）和 S3 兼容的存储。Colanode 服务器 API 以 Docker 镜像的形式提供，环境变量在 docker-compose 文件中详细说明。Colanode 采用 Apache 2.0 许可。

---

## 45. 微软从 VS Code 分支中移除 C/C++ 扩展

**原文标题**: Microsoft subtracts C/C++ extension from VS Code forks

**原文链接**: [https://www.theregister.com/2025/04/24/microsoft_vs_code_subtracts_cc_extension/](https://www.theregister.com/2025/04/24/microsoft_vs_code_subtracts_cc_extension/)

微软停止了其Visual Studio Code的C/C++扩展在VS Codium和Cursor等衍生产品上的使用，引发开发者强烈不满。该扩展提供关键的C/C++语言支持功能，在2025年4月3日发布v1.24.5版本后，已停止在这些分支版本中运行。微软的许可条款长期以来禁止在其产品之外使用其扩展，但这是首次通过二进制文件中的环境检查来强制执行C/C++扩展的使用限制。

基于VS Code构建的AI代码助手Cursor，此前一直通过屏蔽其对微软Visual Studio Marketplace的网络请求来规避这些限制。然而，他们现在计划过渡到这些扩展的开源替代方案。

VS Codium用户也在寻求开源解决方案。一位开发者甚至向美国联邦贸易委员会提出申诉，指控微软通过阻止Cursor等竞争对手，将用户锁定在其AI生态系统中，从而从事反竞争行为，尤其是在微软自身竞争性AI代理Copilot中的Agent Mode的背景下。微软尚未对此事发表评论。

---

## 46. Show HN: Infat – macOS声明式应用关联管理器

**原文标题**: Show HN: Infat – Declaritive application assocation manager for macOS

**原文链接**: [https://github.com/philocalyst/infat](https://github.com/philocalyst/infat)

Infat 是一款 macOS 命令行工具，用于声明式地管理文件类型和 URL 协议关联。它允许你轻松设置打开特定文件类型（如 `.txt`、`.md` 或 `.pdf`）和 URL 协议（如 `mailto:` 或 `web`）的默认应用程序，无需在系统偏好设置中进行导航。

主要功能包括：

*   **列出关联：** 查看哪些应用已注册用于给定的文件扩展名或 URL 协议。
*   **设置默认应用：** 为特定的文件类型和 URL 协议定义默认应用程序。
*   **TOML 配置：** 在 TOML 配置文件中定义所有关联，以便于版本控制和共享。
*   **可脚本化：** 旨在用于脚本和自动化流程。
*   **macOS 原生：** 利用原生 macOS 框架进行强大的集成。

Infat 可以通过 Homebrew 安装，也可以使用 Swift 从源代码构建。该工具通过命令行或 TOML 配置文件进行配置，从而实现一种简单且可重复的方式来管理应用程序关联。它是开源的（MIT 许可证），旨在让高级用户和管理员能够更好地控制应用程序处理。

---

## 47. 格林效应席卷互联网。

**原文标题**: The Gruen Transfer is consuming the internet

**原文链接**: [https://sebs.website/blog/the%20gruen-transfer-is-consuming-the-internet](https://sebs.website/blog/the%20gruen-transfer-is-consuming-the-internet)

塞巴斯蒂安·大卫·李斯在他的博客文章中讨论了“格鲁恩转换”现象。格鲁恩转换指的是一种故意制造混乱的布局，使消费者迷失方向，从而导致冲动购买或偏离其最初意图。最初在实体店观察到的格鲁恩转换，现在在网上也很普遍。

作者认为，像Facebook这样的平台，原本旨在简化更新，现在却变成了由广告、表情包和网红营销主导的令人困惑的迷宫，转移了用户与朋友联系的初衷。这种迷失方向不仅限于社交媒体；许多网站的结构都旨在鼓励冲动行为和“兔子洞”探索，比如陷入维基百科的旁枝末节。

这篇文章强调了格鲁恩转换与用户体验暗黑模式的联系，尤其是在删除社交媒体账户、更改保险政策或取消订阅等困难流程中。这些流程是有意设计的繁琐复杂，以阻止用户实现其目标。

李斯质疑这种日益增长的复杂性的长期后果，并认为它可能达到收益递减的临界点，造成过多的摩擦。他赞扬了欧盟立法，该立法规定订阅和取消服务必须同样容易，并将复杂性作为关键衡量标准。他最后表示，希望看到类似的原则应用于实体零售环境。

---

## 48. 马克·扎克伯格称社交媒体已结束。

**原文标题**: Mark Zuckerberg says social media is over

**原文链接**: [https://www.newyorker.com/culture/infinite-scroll/mark-zuckerberg-says-social-media-is-over](https://www.newyorker.com/culture/infinite-scroll/mark-zuckerberg-says-social-media-is-over)

本文分析了美国联邦贸易委员会（FTC）对Meta (Facebook)提起的反垄断诉讼，认为该委员会对社交媒体行业的定义已经过时，未能反映当前的数字环境。 FTC声称，Meta通过收购Instagram和WhatsApp，非法维持了在“个人社交网络服务”领域的垄断地位，扼杀了创新并减少了消费者的选择。

然而，本文强调，社交媒体已经从人际交流演变为消费各种内容的更广泛平台，使得界定一个由Meta主导的特定市场变得困难。Meta辩称，该公司的平台现在是拥挤的市场的一部分，与TikTok和YouTube等竞争对手一同提供类似的内容形式。

文章指出，由于Meta的平台是免费的，因此证明消费者受到损害具有挑战性。文章还质疑，一个独立的WhatsApp是否一定会比Meta拥有的版本更具创新性。

扎克伯格证词中的一个关键披露是一份2018年的备忘录，其中他建议分拆Instagram以避免潜在的反垄断监管。

文章最后指出，FTC可能关注的是一个过时的问题，因为数字环境正随着TikTok、生成式人工智能和新型社交网络的兴起而迅速变化。文章还提到了欧盟最近因反竞争行为对苹果和Meta处以的罚款。

---

## 49. 误认抹大拉的玛丽亚

**原文标题**: Mistaking Mary Magdalene

**原文链接**: [https://www.newyorker.com/culture/the-weekend-essay/mistaking-mary-magdalene](https://www.newyorker.com/culture/the-weekend-essay/mistaking-mary-magdalene)

本文探讨了抹大拉的马利亚这个复杂且经常被误解的人物，深入研究了围绕她身份的历史和宗教争议。文章首先提到埃及的马利亚的圣像，她曾是一名妓女，以及她的形象如何随着时间的推移与抹大拉的马利亚的形象相混淆。

作者考察了《新约》中对抹大拉的马利亚的有限且有时矛盾的描述，并将其与《腓力福音》等其他文本进行对比，后者将她描绘成一位亲密的同伴和神圣智慧的体现。文章强调了教皇格列高利一世错误地将抹大拉的马利亚认定为一位忏悔的妓女，导致了几个世纪的错误描述以及教会内部女性的边缘化。

作者调查了埃及的马利亚的故事，强调了她通过欲望和忏悔实现的转变和精神之旅，并将其与对抹大拉的马利亚的常见看法进行对比。文章进一步探讨了抹大拉的马利亚的艺术表现形式，尤其是在文艺复兴时期，如何促成了将她描绘成一位忏悔的罪人，经常以衣衫不整的状态出现。

最后，作者讨论了被排除在正典之外的《马利亚福音》，以及它将抹大拉的马利亚描绘成一位传递耶稣秘密教义的精神导师。文章最后强调了以开放的心态参与抹大拉的马利亚的故事的重要性，拥抱围绕她的神话和诗歌，以揭示对基督教中这个关键人物更细致和更具力量的理解。抹大拉的马利亚的本质不在于教条式的真理，而在于通过神圣想象力才能获得的“斜向真理”。

---

## 50. 日常使用Linux手机，为了什么？

**原文标题**: Daily driving a Linux phone, but why?

**原文链接**: [https://thefoggiest.dev/2025/04/24/daily-driving-a-linux-phone-but-why](https://thefoggiest.dev/2025/04/24/daily-driving-a-linux-phone-but-why)

本文探讨了作者为何想要日常使用Linux手机，尽管Android系统看似更方便。作者承认，他们仍然需要一部Android手机来处理必要任务。转向Linux并非为了易用性，而是为了质疑社会规范，并将安全和隐私置于Android普遍存在的基于监控的商业模式之上。

作者承认PinePhone Pro速度较慢，但强调其速度足以满足播放视频和运行应用程序等基本任务，并且较慢的节奏可以减少过度刺激。他们还强调了PinePhone Pro的优点，例如其更小的尺寸、更轻的重量和功能正常的耳机插孔。

最终，由于LGv40 Thinq拥有更优秀的硬件规格（更快的处理器、更好的摄像头、无线充电、更小的尺寸和略大的屏幕），同时保留了耳机插孔，作者计划使用解锁后的、运行PostmarketOS的LGv40 Thinq，而非PinePhone Pro。文章结尾的目标是让Linux操作系统在LGv40 Thinq上启动。

---

## 51. 有多少数学知识是可以被知道的？[视频]

**原文标题**: How much math is knowable? [video]

**原文链接**: [https://www.youtube.com/watch?v=VplMHWSZf5c](https://www.youtube.com/watch?v=VplMHWSZf5c)

无法访问文章链接。

---

## 52. Show HN: Zev – 记住（或发现）终端命令

**原文标题**: Show HN: Zev – Remember (or discover) terminal commands

**原文链接**: [https://github.com/dtnewman/zev](https://github.com/dtnewman/zev)

Zev：使用自然语言查询发现终端命令的命令行工具

Zev是一个命令行工具，它帮助用户通过自然语言查询记住或发现终端命令。它利用OpenAI API将自然语言描述翻译成可执行的命令。用户可以通过`pip install zev`安装Zev，然后在交互模式下运行（`zev`），或直接使用查询（`zev '<你想要做什么>'`）。示例包括查找正在运行的Python进程、文件操作、系统信息、网络命令和Git操作。

Zev需要OpenAI API密钥和订阅，可以使用`zev --setup`进行配置。或者，Zev可以配置为使用Ollama在本地运行，从而允许您在不依赖OpenAI API的情况下运行命令。这需要安装并运行Ollama以及合适的模型，然后通过`zev --setup`配置Zev以指向Ollama API端点（例如，`http://localhost:11434/v1`）。

该项目鼓励贡献，并根据MIT许可证获得许可。

---

## 53. AI 无人驾驶汽车

**原文标题**: AI Horseless Carriages

**原文链接**: [https://koomen.dev/essays/horseless-carriages/](https://koomen.dev/essays/horseless-carriages/)

好的，仅根据标题和它位于koomen.dev上的事实，我可以推断出以下简洁的摘要：

这篇发表在koomen.dev上的文章，题为“AI 无马马车”，很可能探讨了历史上从马车到汽车的过渡与当前人工智能技术的开发和应用之间的相似之处。它可能使用“无马马车”的比喻来代表试图取代或增强现有人工流程的人工智能技术。

这篇文章可能深入探讨：

*   **早期汽车最初的怀疑和挑战：** 将这些与当前对人工智能的担忧和犹豫进行比较。
*   **汽车的逐步接受和最终主导地位：** 与人工智能可能成为生活中各个方面不可或缺的一部分的潜在未来进行类比。
*   **人工智能应用的具体例子：** 可能涵盖人工智能正在取代或增强人类能力的领域，就像汽车取代马一样。
*   **伦理和社会影响：** 可能会涉及与汽车和人工智能的兴起相关的失业、安全问题和监管挑战。
*   **作者的观点（Koomen 的）：** 可能会提供关于人工智能的开发和应用的独特观点，并从汽车技术的历史中吸取教训。

本质上，这篇文章使用“无马马车”的比喻来为理解当前人工智能带来的革命提供历史背景，强调机遇和潜在的陷阱。在没有实际内容的情况下，这是我能提供的最准确的推断。

---

## 54. 在人工智能时代，我们必须保护人类创造力，视其为一种自然资源。

**原文标题**: In the age of AI, we must protect human creativity as a natural resource

**原文链接**: [https://arstechnica.com/ai/2025/04/in-the-age-of-ai-we-must-protect-human-creativity-as-a-natural-resource/](https://arstechnica.com/ai/2025/04/in-the-age-of-ai-we-must-protect-human-creativity-as-a-natural-resource/)

面对快速发展的AI，Benj Edwards 在这篇 Ars Technica 文章中认为，人类的创造力正面临被贬值和同质化的风险。AI 模型通过抓取大量在线内容进行训练，可能会用合成媒体充斥数字领域，从而淹没原创的人类表达并耗尽创意生态系统。

Edwards 认为，人类的创造力是一种有限的资源，依赖于生活经验和认知多样性。当前的 AI 行业方法将其视为一种取之不尽用之不竭的商品，类似于早期工业家对自然资源的剥削。这造成了几个威胁，包括 AI 生成的垃圾邮件造成的数字污染、激进的 AI 爬虫造成的 инфраструктура 压力以及“模型崩溃”的可能性，在这种情况下，AI 模型在自身输出上进行训练会降低集体知识。

文章探讨了 AI 训练的道德和法律层面，将 Adobe 的许可模式与 OpenAI 的“合理使用”论点进行了对比。 它强调了艺术家担心失去生计和 AI 开发人员试图利用现有作品之间的紧张关系。版权被视为一种资源管理形式，对于补充公共领域至关重要。

Edwards 提出了几种保护人类创造力的解决方案，包括选择加入 AI 训练立法、特许权使用费制度、受日本“人间国宝”启发的“创意储备”以及集体拥有的公共抓取的 AI 模型的“AI 公共领域”。文章还讨论了针对 AI 爬虫的技术防御。

最终，作者强调了投资于人的重要性，认为培养独特的人类视角并将它们与周到的 AI 增强相结合的组织，将胜过那些仅依赖 AI 自动化的组织。 在一个日益充斥着 AI 生成内容的世界中，人类的洞察力和联系仍然非常宝贵。

---

## 55. OpenAlternative – 流行的软件的开源替代品

**原文标题**: OpenAlternative – open-source Alternatives to Popular Software

**原文链接**: [https://github.com/piotrkulpinski/openalternative](https://github.com/piotrkulpinski/openalternative)

OpenAlternative 是一个社区驱动的倡议，旨在构建一个全面的专有软件的开源替代品目录。该项目鼓励用户贡献和查找替代现有软件的方案，以助力业务增长。它是一个基于 GPL-3.0 许可的开源项目，并由赞助商支持。

该项目构建为一个 Turborepo monorepo，主应用程序使用 Next.js。 它利用多个第三方服务，包括数据库 (Neon)、分析 (Plausible, PostHog)、新闻通讯 (Beehiiv)、后台任务 (Inngest)、文件存储 (AWS S3)、支付 (Stripe) 和屏幕截图 (ScreenshotOne)。

项目结构组织成 `/apps`、`/packages` 等目录，以及 Next.js 应用中的核心文件夹（如 `/components`、`/lib`、`/actions`、`/utils` 等），用于管理应用程序的不同部分。

开发使用 Bun 作为包管理器。 设置项目包括克隆存储库，使用 `bun install` 安装依赖项，基于 `.env.example` 设置环境变量，使用 `bun run db:push` 将 Prisma schema 推送到数据库，并使用 `bun run dev` 启动开发服务器。

该项目包含各种用于开发任务的命令，例如代码检查、格式化、类型检查、数据库管理等等。 部署专为 Vercel 设计，需要使用 `bun run build` 构建项目，并使用 `bun run start` 启动生产服务器，同时确保所有环境变量都已正确设置。

---

## 56. 搜索市场中的非对称内容审核：以成人网站为例

**原文标题**: Asymmetric Content Moderation in Search Markets: The Case of Adult Websites

**原文链接**: [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5106235](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5106235)

搜索引擎市场中的非对称内容审核：以成人网站为例

---

## 57. 展示HN：我做了自己的TRMNL电子墨水设备

**原文标题**: Show HN: I made my own TRMNL e-ink device

**原文链接**: [https://www.stavros.io/posts/making-a-trmnl-device/](https://www.stavros.io/posts/making-a-trmnl-device/)

作者迫不及待地想收到预购的TRMNL电子墨水屏显示器，于是决定使用现成的组件自行构建：一个Waveshare 7.5英寸电子墨水屏和一个ESP32驱动板。他们利用之前在电子墨水屏项目中的经验来解决构建问题。

关键在于让官方的TRMNL固件在通用的Waveshare驱动板上运行。TRMNL已经开源了他们的固件，该固件从服务器获取PNG图像并显示，同时处理睡眠和电池报告。作者fork了TRMNL固件，并在AI的帮助下，通过修改引脚分配并考虑缺少电池和按钮的情况，使其适应Waveshare驱动。

通过修改后的固件，作者成功地通过购买“自带设备”(BYOD)许可证，使用设备的MAC地址声明设备，并让其配置API密钥，将其DIY设备连接到TRMNL的在线服务。这使得他们自制的“HACKRMNL”能够从TRMNL的服务接收图像。

作者对结果感到满意，并计划用类似于他们看到的另一个项目的木质底座来改进构建。他们在GitHub上分享了他们的固件fork，并希望它能帮助其他人进行自己的电子墨水屏显示项目。他们预计官方的TRMNL设备由于其集成设计和没有电缆会更好。

---

## 58. 展示HN：我做了自己的TRMNL电子墨水设备

**原文标题**: Show HN: I made my own TRMNL e-ink device

**原文链接**: [https://www.stavros.io/posts/making-a-trmnl-device/](https://www.stavros.io/posts/making-a-trmnl-device/)

这篇“Show HN”帖子详细介绍了作者受 TRMNL 电子墨水设备启发，创造自己的电子墨水显示设备的历程。由于对 TRMNL 不明确的定价和漫长的等待时间感到不满，作者决定使用来自 AliExpress/Waveshare 的现成组件：一个 7.5 英寸的电子墨水显示屏和一个 ESP32 驱动板，来构建一个类似的设备。

作者利用其之前使用电子墨水显示屏的经验，并承认现有电子墨水项目的局限性，同时强调了 TRMNL 从服务器获取图像以进行显示的独特吸引力。他们详细介绍了他们的硬件设置，然后专注于调整开源的 TRMNL 固件（专为其特定 ESP32 板设计）以使其与通用的 Waveshare ESP32 驱动器配合使用。

通过使用 Aider 和 Gemini 等人工智能工具，作者成功地修改了固件，主要调整了引脚编号并考虑了硬件差异。这使得他们的 DIY 设备在购买了定制设备的“BYOD 许可证”后，能够与 TRMNL 的在线服务进行通信。然后，该设备检索并显示 TRMNL 服务生成的图像，有效地将 DIY 项目变成了一个功能性的“HACKRMNL”。

作者分享了包含修改后固件的 Forked 仓库，并以对项目成果的满意结束，同时期待着实际 TRMNL 设备的到来。他们还计划用木制底座来改善其 DIY 设备的美观性。主要的结论是，用户可以使用现成的组件和 TRMNL 开源固件的修改版本，以极短的时间创建一个与 TRMNL 兼容的电子墨水设备。

---

## 59. 关于Vision Transformer，每个人都应该知道的三件事

**原文标题**: Three things everyone should know about Vision Transformers

**原文链接**: [https://arxiv.org/abs/2203.09795](https://arxiv.org/abs/2203.09795)

Touvron等人的论文《关于Vision Transformer，每个人都应该了解的三件事》探讨了Vision Transformer (ViT) 架构的改进和效率，ViT 架构已在计算机视觉任务中占据重要地位。作者提出了三个关键见解：

1.  **残差层的并行处理：** ViT 中常见的残差层顺序处理，在一定程度上可以并行处理，而不会显着影响准确性。这提供了潜在的速度提升。

2.  **高效微调：** 仅微调注意力层的权重足以使 ViT 适应更高的分辨率或新的分类任务。这种方法显着降低了微调期间的计算成本和内存消耗，同时还允许在不同任务之间进行更大的权重共享。

3.  **改进的自监督训练：** 添加基于 MLP 的 patch 预处理层可提高基于 masking patches 的 Bert 类自监督训练的有效性。

作者使用 ImageNet-1k 数据集验证了这些发现，并在 ImageNet-v2 测试集上证实了它们的稳健性。还在六个较小的数据集上评估了迁移性能。该研究为优化 ViT 架构提供了宝贵的见解，从而实现更高效的训练、微调和改进的性能。

---

## 60. IBM Z17内部探秘

**原文标题**: A Tour Inside the IBM Z17

**原文链接**: [https://community.ibm.com/community/user/ibmz-and-linuxone/blogs/elizabeth-k-joseph1/2025/04/23/a-tour-inside-the-ibm-z17?communityKey=e7b7d299-8509-4572-8cf1-c1112684644f](https://community.ibm.com/community/user/ibmz-and-linuxone/blogs/elizabeth-k-joseph1/2025/04/23/a-tour-inside-the-ibm-z17?communityKey=e7b7d299-8509-4572-8cf1-c1112684644f)

IBM z17 内部一览：

*   **性能提升：** 相比前代，处理器速度、缓存大小和内存带宽的改进，突出 z17 处理高负载的能力。
*   **安全特性：** 增强的安全能力，包括基于硬件的加密、可信执行环境和缓解网络威胁的特性，旨在提供高度安全的平台。
*   **云集成：** z17 如何与混合云环境集成，实现跨主机和云基础设施的无缝部署和管理应用程序。
*   **AI 加速：** 加速人工智能和机器学习工作负载的特性，允许企业直接在主机上运行 AI 应用程序，更接近其数据。
*   **弹性和可用性：** 增强的高可用性和灾难恢复能力，确保业务连续性和最小停机时间。
*   **可持续性：** 能源效率的提高以及其他有助于系统整体可持续性的特性。
*   **工作负载整合：** 将多样化的工作负载整合到单个平台上的能力，从而降低成本和复杂性。
*   **特定硬件组件：** 深入探讨处理器设计、内存架构和其他关键硬件组件。
*   **软件生态系统：** z17 上支持的软件栈，包括 z/OS、Linux on Z 以及各种中间件和应用程序。

---

## 61. “光明圈”与“玛格丽特·富勒”：先验主义女性的崛起

**原文标题**: 'Bright Circle' and 'Margaret Fuller': The Rise of the Transcendental Woman

**原文链接**: [https://www.wsj.com/arts-culture/books/bright-circle-and-margaret-fuller-the-rise-of-the-transcendental-woman-1bacdb10](https://www.wsj.com/arts-culture/books/bright-circle-and-margaret-fuller-the-rise-of-the-transcendental-woman-1bacdb10)

无法访问文章链接。

---

## 62. 芬兰给鹿角涂上反光漆 (2014)

**原文标题**: Finland is painting deer antlers with reflective paint (2014)

**原文链接**: [https://www.smithsonianmag.com/smart-news/avoid-deer-strikes-finland-painting-deer-antlers-reflective-paint-180949792/](https://www.smithsonianmag.com/smart-news/avoid-deer-strikes-finland-painting-deer-antlers-reflective-paint-180949792/)

2014年，芬兰驯鹿牧民协会开始在驯鹿角上测试反光漆，以减少交通事故。每年约有4000只驯鹿在芬兰道路上丧生，造成1500万欧元的损失。反光漆旨在提高驯鹿对驾驶员的可见度，尤其是在11月、12月、7月和8月等危险条件下（冰路、天黑得早、蚊虫活动）。目前正在毛皮上测试这种油漆，但鹿角可能更有效，因为它们从各个角度都可见。虽然传统的解决方案侧重于提高汽车和道路安全，但这种芬兰方法直接针对动物，使其更显眼。

---

## 63. 玛丽·麦克莱恩，来自比尤特的狂野女人

**原文标题**: Mary MacLane, the Wild Woman from Butte

**原文链接**: [https://publicdomainreview.org/essay/i-am-making-the-world-my-confessor/](https://publicdomainreview.org/essay/i-am-making-the-world-my-confessor/)

Hunter Dukes的文章探讨了玛丽·麦克莱恩的生活和引起的轰动。玛丽·麦克莱恩是蒙大拿州比尤特的一位年轻女子，1902年年仅19岁时出版了她那本引人争议的日记《玛丽·麦克莱恩的故事》。这篇文章着重介绍了麦克莱恩坦率和非传统的写作风格，这种风格探索了她的内心世界、双性恋以及对社会规范的不满。

麦克莱恩的写作风格是对话式的、自我赞扬的和自传式虚构的，这挑战了当时的传统。她宣称自己是天才，并公开表达了自己的欲望，包括对男性（拿破仑、魔鬼）和女性（她的老师范妮·科宾）的浪漫兴趣。

这本书立刻引起轰动，第一个月就卖出了近10万册。评论界褒贬不一，但麦克莱恩获得了一批追随者，并引发了一种文化现象，全国各地都成立了“玛丽·麦克莱恩协会”。她被比作玛丽·巴什基尔采娃，并被称为“比尤特的巴什基尔采娃”。

这篇文章还详细介绍了麦克莱恩成功后的情况，包括一些怪诞事件和对其作品的恶搞。麦克莱恩向东旅行，与哈丽雅特·门罗和佐娜·盖尔等人物交往，呈现出对其欲望和自我认知的矛盾描述。这篇文章表明，麦克莱恩有意识地塑造了一个人物形象，承认她从未完全展现她的“真实自我”，而是在“玩一场深刻的游戏”。

---

## 64. 对雇主的忠诚 (2018)

**原文标题**: On loyalty to your employer (2018)

**原文链接**: [https://medium.com/hackernoon/on-loyalty-to-your-employer-c674c4b06b3a](https://medium.com/hackernoon/on-loyalty-to-your-employer-c674c4b06b3a)

史蒂夫·巴克利2018年的文章《关于对雇主的忠诚》将科技行业的短工期与他父亲在一家公司工作30年形成对比，质疑了雇主忠诚的概念。作为一名招聘人员，巴克利承认自己会宣传公司，但同时也确立了一套筛选雇主的基准：合理的薪资、善待员工（通过 Glassdoor 和社交媒体验证）、财务安全（对初创公司尤其重要）以及对新想法的开放性。

巴克利告诫不要盲目拥抱公司文化，提醒读者雇佣关系是一种交易。虽然良好的工作环境是积极的，但员工不应自欺欺人地认为雇主是家人或朋友。他强调了优先考虑家庭、精神健康和个人价值观的重要性，而不是为了迎合雇主，并警告人们不要陷入“奋斗”心态。

这篇文章提倡相互尊重：努力工作以换取公平的报酬，支持员工的福祉，并投资于成长。最终，巴克利强调了平衡工作与生活的重要性，呼应了他父亲的观点，即与亲人共度时光比过度投入工作更有价值。

---

## 65. 创建你自己的联邦微博

**原文标题**: Creating your own federated microblog

**原文链接**: [https://fedify.dev/tutorial/microblog](https://fedify.dev/tutorial/microblog)

本文是一个教程，旨在利用Fedify（一个ActivityPub服务器框架）以及Node.js、npm、Hono和TypeScript，构建一个简单的、联邦化的微博平台。本教程面向熟悉HTML、HTTP、SQL、JSON和JavaScript等Web应用程序基础的开发者，但不需要事先了解TypeScript、JSX、ActivityPub或Fedify。

该微博将包含一个单一用户帐户，其他Fediverse用户可以关注和取消关注，能够创建帖子、关注其他Fediverse帐户，以及查看按时间顺序排列的信息流。 为了简化教程，一些功能（如个人资料定制、帖子编辑/删除、取消关注、点赞、评论、搜索和安全功能）被排除在外。

本教程将引导读者设置开发环境（Node.js、Fedify CLI），初始化Fedify项目，并使用Visual Studio Code进行开发。 其中包括对TypeScript和JSX的简要介绍。

第一步是使用JSX创建一个帐户创建页面，利用布局组件和Pico CSS框架进行样式设置。 目标是构建一个可以与其他ActivityPub服务交互的功能性微博。 完整的源代码可在GitHub上找到，提交被分段以匹配教程的步骤。

---

## 66. 企业代理的代理网格

**原文标题**: Agent Mesh for Enterprise Agents

**原文链接**: [https://www.solo.io/blog/agent-mesh-for-enterprise-agents](https://www.solo.io/blog/agent-mesh-for-enterprise-agents)

本文介绍了一种名为“Agent Mesh”（代理网格）的新型网络范式，旨在支持企业中智能代理系统的兴起。智能代理系统具有动态和涌现行为的特点，需要一种超越传统确定性工作流程的网络基础设施。Agent Mesh旨在解决这些系统中固有的安全性、可观察性、发现和治理挑战。

Agent Mesh通过代理网关运行，该网关是一种专门针对AI通信模式优化的数据平面，侧重于代理到LLM、代理到工具（通过模型上下文协议-MCP）以及代理到代理（A2A）的交互。其关键属性包括默认安全性（mTLS、OIDC）、原生Layer 7支持、细粒度访问控制、端到端可观察性、运行时注册和发现、弹性以及现代声明式配置模型。

本文强调了保护代理到LLM的通信、使用MCP将代理与企业工具集成以及启用多代理工作流程。它强调了代理身份、零信任架构和细粒度授权策略的重要性。Agent Mesh有助于代理和工具的注册和发现，同时防止工具中毒。

一个主要优势是它支持跨任何云环境的代理，避免供应商锁定。Agent Mesh具有可组合性，提供对模型、工具和代理的统一访问，并在每一层嵌入一致的策略执行和语义理解。Solo.io 定位为已准备好交付这种基础设施。

---

## 67. Show HN: 我给我的RSS阅读器项目添加了翻译功能

**原文标题**: Show HN: I Added Translation to My RSS Reader Project

**原文链接**: [https://rahuldshetty.github.io/reader-project/#/translation](https://rahuldshetty.github.io/reader-project/#/translation)

这位“Show HN”帖子介绍了一位开发者为其RSS阅读器项目添加翻译功能。 帖子非常简短，但重点在于开发者已将翻译功能集成到其RSS阅读器（“reader-project”）中，大概允许用户阅读非原始语言的文章。 可以推断出这是一个新实现的功能，开发者正在向Hacker News社区（“Show HN”）展示它。

---

## 68. 你不会盗用字体吧？

**原文标题**: You wouldn't steal a font

**原文链接**: [https://fedi.rib.gay/notes/a6xqityngfubsz0f](https://fedi.rib.gay/notes/a6xqityngfubsz0f)

文章似乎是Rib (@Rib) 在联邦宇宙实例 (fedi.rib.gay) 上发表的短文。 主要内容很简单：“你不会偷字体吧”，暗示反对字体盗版。 该帖子托管在联邦宇宙实例上这一事实表明，它可能是该在线社区内围绕知识产权或数字资产相关伦理考量的更广泛对话的一部分。 “:ms_red_panda:”的存在表明作者使用了一个表情符号，可能用于强调或添加一种俏皮的语气。“Please turn on your JavaScriptLoading...”消息表明该页面在未启用 JavaScript 的情况下无法完全加载。 本质上，这篇文章是对字体盗版的一个简短的，可能是讽刺的或反讽的评论。

---

## 69. PgDog 是一个事务池化逻辑复制管理器，可以对 PostgreSQL 进行分片。

**原文标题**: PgDog is a transaction pooler logical replication manager can shard PostgreSQL

**原文链接**: [https://github.com/pgdogdev/pgdog](https://github.com/pgdogdev/pgdog)

PgDog：用于分片 PostgreSQL 数据库的快速安全、基于 Rust 的事务池化器和逻辑复制管理器。它可以处理大量数据库和连接，提供负载均衡、健康检查、事务池化和分片等功能。PgDog 将事务分发到副本和主节点，并根据轮询或查询检查等策略路由查询。它通过监控主机健康状况并在需要时重新路由查询来支持自动故障转移。

PgDog 通过连接池高效地管理大量客户端，允许它们共享有限数量的 PostgreSQL 连接。分片功能支持基于分片键自动将查询路由到适当的分片，并支持跨分片查询。此外，它还提供 CSV 解析器，用于自动跨分片拆分 COPY 命令，以及用于后台数据分发的逻辑复制。

该系统高度可配置，允许运行时调整。PgDog 可以通过 Helm chart 使用 Kubernetes 部署，也可以使用 Docker Compose 部署。通过 PgBouncer 风格的管理数据库和 OpenMetrics 端点来促进监控，并提供 Datadog 配置。

该项目正在积极开发中，欢迎早期采用者。它采用 AGPL v3 许可，允许内部使用和私下修改，而无需共享源代码。

---

## 70. 一些非字符串湍流

**原文标题**: Some __nonstring__ Turbulence

**原文链接**: [https://lwn.net/SubscriberLink/1018486/1dcd29863655cb25/](https://lwn.net/SubscriberLink/1018486/1dcd29863655cb25/)

LWN.net文章讨论了Linux内核开发过程中最近发生的一场争论，起因是GCC 15中引入了一个新的编译器警告`-Wunterminated-string-initialization`。该警告会标记潜在问题的C声明，即字符数组初始化时缺少终止NUL字节。

虽然旨在发现错误，但该警告在内核代码中产生了误报，因为内核代码中有意将字符数组用作查找表而不是字符串。解决方案是使用`__nonstring__`属性来抑制这些特定情况下的警告。Kees Cook一直在努力整合这些修复。

麻烦始于Linus Torvalds在发布内核版本6.15-rc3之前，升级到了包含GCC 15预发布版本的Fedora 42。新编译器触发了警告，Torvalds在没有与Cook协调或检查"-next"分支的情况下，迅速将修复程序直接应用到主线，导致旧版本GCC的构建中断。

在发布6.15-rc3之后，Torvalds撤销了他的更改并完全禁用了该警告，这导致了他与Cook之间激烈的争论，Cook觉得他预先准备好的修复程序被忽略了。Torvalds为自己的行为辩护，理由是需要修复中断的构建。

文章最后指出，由此产生的负面情绪以及围绕编译器更新需要更好的沟通和协调。文章还提到Torvalds不同意`__nonstring__`属性的实现，更喜欢基于类型的注释。文章强调了将新编译器功能纳入像Linux内核这样复杂的项目中的挑战，以及CI/测试的重要性。

---

## 71. 苹果和Meta因违反欧盟法律被处以数百万美元罚款

**原文标题**: Apple and Meta fined millions for breaching EU law

**原文链接**: [https://ca.finance.yahoo.com/news/apple-fined-570-million-meta-094701712.html](https://ca.finance.yahoo.com/news/apple-fined-570-million-meta-094701712.html)

苹果和Meta因违反《数字市场法》（DMA）受到欧盟反垄断监管机构的罚款，该法案旨在限制大型科技公司的权力。苹果被处以5亿欧元罚款，而Meta被罚款2亿欧元。欧盟的行动是在对这些公司遵守DMA情况进行为期一年的调查之后采取的，该法案旨在允许规模较小的竞争对手进入由最大公司主导的市场。

这些罚款引发了紧张关系，特别是与美国的关系，白宫称其为“经济勒索”。然而，欧盟正在坚定地执行DMA，并受到美国法院对谷歌在线广告技术领域主导地位的裁决的鼓舞。

苹果被指控限制应用程序开发者引导用户到App Store以外的更便宜的交易，并阻碍用户侧载应用程序。Meta的付费或同意模式，即收费提供无广告服务，也被认为不符合规定。两家公司都在质疑欧盟的决定。

尽管有罚款，但一些消息来源表明，由于侧重于合规性、违规行为持续时间短以及希望避免来自美国政府的报复，这些罚款相对较小。这些公司有两个月的时间来遵守欧盟的命令，否则将面临每日罚款。在苹果公司做出改变，允许用户更容易地切换到竞争对手的浏览器或搜索引擎后，欧盟监管机构确实结束了对苹果公司iPhone上浏览器选项的调查。

欧盟反垄断负责人特蕾莎·里贝拉强调，所有在欧盟运营的公司都必须遵守欧盟法律并尊重欧洲价值观。欧盟还被敦促继续对谷歌和X进行调查。

---

## 72. 可观测性 2.0 及其数据库

**原文标题**: Observability 2.0 and the Database for It

**原文链接**: [https://greptime.com/blogs/2025-04-25-greptimedb-observability2-new-database](https://greptime.com/blogs/2025-04-25-greptimedb-observability2-new-database)

本文介绍“可观测性 2.0”，它是基于指标、日志和追踪的传统可观测性的一种演进。“可观测性 2.0”强调使用“宽事件”——富含上下文、高维度和高基数的记录——作为“单一数据源”，以克服复杂现代系统中数据孤岛和预聚合数据的局限性。

文章概述了传统可观测性的缺点，包括数据孤岛、预聚合权衡、非结构化日志、静态插桩和冗余数据。宽事件通过保留原始、高保真度的事件数据来解决这些问题，从而实现追溯分析和指标、日志和追踪的动态推导。

采用“可观测性 2.0”面临与事件生成、数据传输、经济高效的存储、查询灵活性和工具集成相关的挑战。文章强调需要一个专门为这种新范式优化的数据库。关键的数据库需求包括用于扩展性和成本效益的高效云对象存储和列式数据格式、低延迟的实时查询和摄取、用于日常和探索性分析的灵活查询功能以及与现有仪表板和工具的向后兼容性。

文章将 GreptimeDB 定位为一款专为宽事件和“可观测性 2.0”设计的开源分析型可观测性数据库，具有与云基础设施的无缝集成以及可观测性数据的高效管理。它重点介绍了 GreptimeDB 在数据摄取、预处理、查询和持久化方面的关键特性，旨在提供一站式、用户友好的可观测性体验。

---

## 73. 基于MCPEngine的AWS Lambda上的MCP

**原文标题**: MCP on AWS Lambda with MCPEngine

**原文链接**: [https://www.featureform.com/post/deploy-mcp-on-aws-lambda-with-mcpengine](https://www.featureform.com/post/deploy-mcp-on-aws-lambda-with-mcpengine)

使用MCPEngine在AWS Lambda上部署模型上下文协议（MCP）服务器，以实现LLM与外部工具的无服务器、可扩展和生产就绪交互。本文通过利用MCPEngine对流式HTTP和AWS Lambda无状态环境的支持，解决了现有MCP实现（如依赖SSE和持久TCP连接）的局限性。

本文通过三个例子进行说明：

1.  **无状态天气API：** 一个返回预设天气数据的简单工具，演示了基本的Lambda部署。
2.  **有状态类Slack API：** 一个使用Amazon RDS进行持久存储的例子，展示了如何在MCPEngine中管理数据库连接和上下文，从而实现有状态的交互。
3.  **认证API：** 使用Google SSO和OpenID Connect (OIDC) 进行基于令牌的身份验证，从而保护工具的安全，验证用户身份并限制对授权用户的访问。

每个例子都包括代码片段、部署说明（Terraform和手动）以及使用Claude的连接说明。MCPEngine处理令牌验证并将用户身份暴露给工具代码。文章最后强调了使用无状态、Lambda原生方法实现MCP兼容服务器的优势，以及将这些服务器集成到智能体系统（如在共享聊天室中协作的模拟团队）中的潜力。MCPEngine的内置身份验证被强调为一个关键优势。

---

## 74. 更多一切 永恒

**原文标题**: More Everything Forever

**原文链接**: [https://www.nytimes.com/2025/04/23/books/review/more-everything-forever-adam-becker.html](https://www.nytimes.com/2025/04/23/books/review/more-everything-forever-adam-becker.html)

亚当·贝克尔的《更多、一切、永恒》批判了硅谷亿万富翁的技术乌托邦愿景，尤其是他们通过火星殖民和开发先进人工智能等项目“拯救人类”的计划。文章重点阐述了贝克尔反对埃隆·马斯克火星殖民计划的论点，概述了在火星上生存的重大挑战，包括辐射、有毒尘埃以及建立自给自足殖民地的后勤困难。贝克尔认为，即使有了技术进步，火星上的生活也会是痛苦的，而且依赖地球资源。

更广泛地说，贝克尔认为这些项目背后的驱动力是一种“技术救世主义意识形态”，他认为这种意识形态是还原论的、有利可图的，并提供了一种超越的承诺，从而证明可以无视伦理和实践的限制。他认为，这些雄心勃勃的计划，源于科技行业对永久增长的需求，将想象中的未来置于解决地球当前问题之上。最终，这本书表明，这些追求虽然被视为人类生存的解决方案，但却存在着深刻的缺陷，并可能造成危害。

---

## 75. AI编码的隐性成本

**原文标题**: The hidden cost of AI coding

**原文链接**: [https://terriblesoftware.org/2025/04/23/the-hidden-cost-of-ai-coding/](https://terriblesoftware.org/2025/04/23/the-hidden-cost-of-ai-coding/)

AI编码隐藏的代价：失去乐趣与心流

文章《AI编码隐藏的代价》探讨了在软件开发中使用AI的潜在弊端：失去乐趣和“心流”状态。作者在承认AI编码工具带来的生产力提升和优势的同时，也表达了对过度依赖AI可能导致开发者感到疏离和缺乏成就感的担忧。

作者回忆起沉浸式的编码体验，挑战变成了谜题，创造行为本身就带有内在的奖励。这种以深度专注和完全投入为特征的“心流”状态，与创造力、生产力和幸福感息息相关。

然而，随着Cursor等AI工具生成大部分代码，作者发现自己从创造者转变为管理者，提示AI并调整其输出，虽然效率更高，但参与度更低。文章提出的核心问题是，外包核心编码任务是否也外包了获得满足感的机会，以及是否能在AI增强的工作流程中找到一种新的成就感。

作者认为，或许幸福感仍然可以存在，转移到更高层次的系统设计、创造性的提示，或者软件开发的人性化方面。最终，他们主张有意识地保留手动编码和“心流”状态仍然可以发生的空间，强调仅仅为了效率而优化，可能会失去最初吸引许多人从事编程的内在乐趣。文章最后呼吁人们思考AI对开发者幸福感和福祉的影响。

---

## 76. 亨利·李 (1883)：《海怪真面目及海洋传说释义》

**原文标题**: Sea Monsters Unmasked and Sea Fables Explained by Henry Lee (1883)

**原文链接**: [https://publicdomainreview.org/collection/sea-monsters-sea-fables/](https://publicdomainreview.org/collection/sea-monsters-sea-fables/)

亨利·李《海怪真面目揭秘及海上传说解读》(1883年)，来自多伦多大学图书馆互联网档案馆，其目的很可能是为了揭穿围绕海怪和奇幻海洋生物的普遍认知和神话。根据标题，该著作可能探讨了与海蛇、克拉肯、美人鱼和其他水生生物相关的历史记载、目击事件和传说。

核心前提是“揭秘”这些生物，表明对所谓的证据进行批判性审查，并对其起源进行科学解释。李很可能剖析了目击者证词、艺术描绘和民间传说，以确定可能助长这些神话的现实世界来源。这可能包括解释对已知海洋动物（如巨型鱿鱼、鲸鱼或姥鲨）的错误识别或夸大目击事件如何被解读为怪物。

此外，“海上传说解读”部分很可能深入探讨了促成这些神话的产生和延续的文化和历史背景。李可能会讨论对未知的恐惧、航海民间传说，甚至是有意的恶作剧是如何在塑造公众对海怪的看法中发挥作用的。该著作很可能融合了动物学观察、历史研究和批判性分析，从而对传奇海洋生物的持久魅力提供了一种理性和祛魅的视角。它很可能旨在用科学认知的海洋世界理解取代迷信。

---

## 77. 我如何使用 Obsidian、Hugo、GitHub 和 Cloudflare 搭建博客

**原文标题**: How I blog with Obsidian, Hugo, GitHub, and Cloudflare

**原文链接**: [https://ingau.me/blog/how-i-write-my-blogs-in-obsidian-and-publish-instantly/](https://ingau.me/blog/how-i-write-my-blogs-in-obsidian-and-publish-instantly/)

本文概述了一种使用Obsidian作为写作工具、Hugo作为静态站点生成器，以及GitHub和Cloudflare Pages进行部署的博客方法，强调可控性、成本效益和简化的工作流程。

作者利用Obsidian的纯文本、本地优先方法进行写作，并通过iCloud在设备之间同步笔记。Hugo使用极简的Bear Blog主题来生成网站。GitHub管理版本控制，Cloudflare Pages处理托管和部署，所有这些都不需要订阅费或供应商锁定。

该设置包括安装Hugo，创建一个新站点，并添加Bear Blog主题。关键步骤是将Obsidian连接到Hugo，方法是将Hugo站点的content/blog文件夹作为Obsidian库打开。文章强调在Obsidian帖子中使用Front Matter来控制Hugo的构建过程，特别是`draft: true`标志。作者使用Hugo的本地服务器来预览具有草稿可见性的帖子，然后再发布。该过程包括为博客创建一个GitHub存储库，连接本地Hugo站点，并设置Cloudflare Pages，提供有关构建设置的详细信息。

发布工作流程简化为在帖子的Front Matter中将`draft: true`切换为`draft: false`，提交更改，并推送到GitHub，从而触发Cloudflare Pages自动重建和部署更新后的站点。

作者强调，初始设置需要一定的技术努力，但由此产生的工作流程是无缝的，使作者可以专注于内容创建，并通过简单的Git推送来实现发布。

---

## 78. YAGRI：你会读它的

**原文标题**: YAGRI: You are gonna read it

**原文链接**: [https://www.scottantipa.com/yagri](https://www.scottantipa.com/yagri)

本文介绍了“YAGRI”（“你会去读它”）的概念，作为对流行的软件开发建议“YAGNI”（“你不需要它”）的补充。YAGNI警告不要过度设计和构建不必要的功能，而YAGRI则主张存储超出产品规范立即需要的额外上下文数据和元数据。

作者认为，仅仅关注UI中显示的数据可能会导致缺乏有价值的信息，这些信息对于以后的调试、内部分析和理解用户行为至关重要。一个常见的例子是简单地删除用户删除的某些数据，而不是记录谁删除了它、如何删除、何时删除以及为什么删除。

本文建议在大多数表中存储标准字段，如`created_at`、`updated_at`、`deleted_at`、`created_by`，以及CRUD操作期间使用的权限信息。虽然不是每个字段都会被使用，但作者认为，在关键情况下拥有这些信息的潜在回报超过了相对较小的实施成本。他强调，应用程序主要关于存储数据，工程师有责任妥善管理和维护数据。他承认无差别地记录所有内容的风险，但总结说，拥有过多的时间戳很少会成为抱怨。

---

## 79. 秀 HN：我从零开始写的能运行 DOOM 的操作系统内核

**原文标题**: Show HN: My from-scratch OS kernel that runs DOOM

**原文链接**: [https://github.com/UnmappedStack/TacOS](https://github.com/UnmappedStack/TacOS)

此“Show HN”帖子介绍 TacOS，一个完全由 C 和汇编语言编写的业余 UNIX 类操作系统内核。TacOS 是一个个人项目，拥有 VFS、调度器、TempFS、设备驱动程序、上下文切换、虚拟内存管理、物理页面帧分配等功能，甚至移植了经典游戏 DOOM。它可以在真实硬件和 Qemu 模拟器中运行。

作者承认 TacOS 并不完整，并且包含错误，强调其作为一个玩具操作系统的状态。该帖子鼓励用户加入 Discord 服务器，以获取更新、帮助开发自己的操作系统项目以及进行一般讨论。

该帖子提供了清晰的构建和运行 TacOS 的说明，需要 Git、Qemu、NASM 和 Clang。它指导用户克隆 TacOS 和 Limine 引导加载程序存储库，检出适当的 Limine 版本，然后运行 `make` 命令。该操作系统以 Mozilla Public License 2.0 许可发布。

---

## 80. 谷歌合同阻止摩托罗拉将Perplexity设置为默认助手。

**原文标题**: Google contract prevented Motorola from setting Perplexity as default assistant

**原文链接**: [https://www.bloomberg.com/news/articles/2025-04-23/perplexity-executive-says-google-blocked-motorola-s-use-of-ai-assistant](https://www.bloomberg.com/news/articles/2025-04-23/perplexity-executive-says-google-blocked-motorola-s-use-of-ai-assistant)

彭博社文章《谷歌合同阻止摩托罗拉将Perplexity设为默认助手》报道称，一份谷歌合同阻止了摩托罗拉在其安卓手机上预装Perplexity AI作为默认助手。据Perplexity首席商务官德米特里·舍维连科称，摩托罗拉有意将Perplexity设为其设备的默认AI助手，但由于使用安卓操作系统而产生的合同义务禁止了这一点。

该文章强调了像Perplexity这样的小型AI公司在与谷歌竞争时面临的挑战，谷歌严格控制着安卓生态系统，并对依赖该操作系统的硬件制造商拥有巨大的影响力。该合同有效地限制了像摩托罗拉（联想所有）这样的手机制造商推广替代AI助手的能力，从而巩固了谷歌在AI助手领域的统治地位。

这一披露引发了人们对反竞争行为的担忧，以及谷歌对安卓的控制是否正在扼杀创新并限制新兴AI助手市场中的消费者选择。该报道暗示，谷歌利用其对安卓操作系统的控制权，以确保谷歌助手仍然是安卓设备上的首选，即使制造商可能更愿意提供替代的AI解决方案。这种限制阻碍了小型AI初创公司通过在流行的设备上预装来获得显著的吸引力。

---

## 81. 遏制教皇的权力

**原文标题**: Curbing the Power of the Popes

**原文链接**: [https://www.historytoday.com/archive/feature/curbing-power-popes](https://www.historytoday.com/archive/feature/curbing-power-popes)

杰西卡·瓦恩伯格的《遏制教皇权力》探讨了历史上教皇宗教权力和世俗权力之间岌岌可危的平衡，认为失去大片领土可能对教皇来说是一种恩赐而非打击。

文章追溯了教皇权力的演变历程，从罗马卑微的起源，与圣彼得殉难联系在一起，到崛起为控制教皇国的重要的世俗权力。这一转变，由君士坦丁将基督教合法化所推动，带来了公民责任以及与世俗政治的纠缠。虽然教皇在崩溃的西罗马帝国中提供了稳定，但他们面临着来自东罗马皇帝的干预，后来依靠与法兰克国王如丕平和查理曼的联盟，他们承认教皇为意大利中部的统治者。

然而，这种世俗权力导致了内部腐败、暴力的权力斗争以及对政治化的批评，以丑闻、阿维尼翁教廷和西方教会大分裂为代表。尽管进行了改革尝试和复兴时期，但精神角色与世俗角色之间的冲突依然存在。

最终，文章表明，1870年教皇国的丧失，最终在1929年建立了梵蒂冈城，出乎意料地加强了教皇的权力，因为它使其摆脱了世俗统治的负担，并使其能够完全专注于其宗教使命，只服从于上帝。

---

## 82. 我尝试购买一桶原油 (2015)

**原文标题**: I Tried to Buy an Actual Barrel of Crude Oil (2015)

**原文链接**: [https://www.bloomberg.com/news/articles/2015-11-03/that-time-i-tried-to-buy-some-crude-oil](https://www.bloomberg.com/news/articles/2015-11-03/that-time-i-tried-to-buy-some-crude-oil)

我尝试购买一桶原油的经历

文章《我尝试购买一桶原油的经历》讲述了彭博社记者利亚姆·丹宁试图购买一桶西德克萨斯中质原油（WTI）时，遇到的既幽默又出乎意料的复杂经历。他被当时较低的油价所吸引，试图了解市场背后的真相。

丹宁很快发现，仅仅购买一桶原油远非易事。他联系了许多经纪人和石油公司，但处处碰壁。该行业通常以更大的规模运作，涉及数百甚至数千桶的交易。许多潜在卖家直接无视他的询问，而另一些卖家则解释了处理如此少量石油的不切实际和成本过高。

他了解了物流方面的挑战，包括运输、储存以及对专用设备的需求。与这些因素相关的成本将远远超过石油本身的价值，使得在财务上毫无意义。即使他能找到愿意交易的卖家，遵守法规、保险要求和管道连接费用也会进一步使过程复杂化。

最终，丹宁未能买到他的一桶原油。这篇文章突出了新闻中引用的抽象油价概念与石油市场的有形现实之间的脱节，强调了该行业的巨大规模和复杂性。它表明，即使是少量原油的购买，也只有大型专业实体才能真正进行。

---

## 83. 韩国81998家酒吧最短步行路线

**原文标题**: Shortest-possible walking tour to 81,998 bars in South Korea

**原文链接**: [https://www.math.uwaterloo.ca/tsp/korea/index.html](https://www.math.uwaterloo.ca/tsp/korea/index.html)

本文详细介绍了解决一个大规模旅行商问题（TSP）的方案，该问题涉及在韩国步行游览81998家酒吧。研究人员成功计算出最短路线，并验证了其最优性。最终路线需要连续步行178天1小时56分17秒，突显了问题的规模。

计算利用开源路线规划引擎（OSRM）生成所有酒吧之间的旅行时间，并结合LKH和Concorde代码来寻找和验证最优解。这项成就超越了之前TSP的里程碑，如57912站的荷兰之旅。

本文纠正了对TSP难度的一些常见误解，解释说先进的技术，而不是蛮力检查，使得解决如此大规模的实例成为可能。线性规划，特别是割平面法，起着至关重要的作用。

交互式地图允许用户探索该路线，提供区域视图和地图选项。该项目是数学优化的一个实际例子，展示了其在提高各行各业资源效率方面的潜力。该工作感谢个人和组织的贡献，包括IBM提供CPLEX优化器，以及Oum Sang-il博士提供酒吧位置。最后，它提供了其他已解决TSP实例的链接，以及关于TSP、P与NP及相关主题的进一步阅读资料。

---

## 84. 临床试验：新型营养配方治疗肠道菌群过度生长

**原文标题**: Clinical trial: novel nutritional formula treats gut microbial overgrowth

**原文链接**: [https://medicalxpress.com/news/2025-04-clinical-trial-nutritional-formula-effectively.html](https://medicalxpress.com/news/2025-04-clinical-trial-nutritional-formula-effectively.html)

西达-赛奈研究人员的一项临床试验发现，一种新型、适口性好的元素饮食（PED）mBiota Elemental能有效治疗肠道菌群过度生长疾病，如SIBO和IMO。该研究发表在《临床胃肠病学和肝脏病学》杂志上，表明mBiota Elemental显著减少了SIBO和/或IMO患者的肠道菌群过度生长，并改善了症状。

这项开放标签试验纳入了30名被诊断患有SIBO、IMO或两者兼有的成年人，他们接受了为期两周的mBiota Elemental疗程，随后进行了为期两周的食物再引入期。结果显示，73%的受试者呼吸测试恢复正常，83%的受试者症状得到充分缓解。呼出的甲烷和氢气水平显著降低，关键微生物群（如普雷沃菌属9和梭杆菌属）的丰度也显著降低。此外，大多数受试者体内的史密斯甲烷短杆菌水平降低或变得无法检测。

在PED阶段，参与者在腹胀、腹部胀大、腹部不适、便秘和肠胃胀气方面有所改善，在食物再引入期间，症状进一步改善。该配方安全，仅报告了轻微的副作用，没有严重不良事件。重要的是，高依从率归功于该配方改善的口味、气味和质地。该研究表明，mBiota Elemental为管理SIBO和IMO提供了一种有效的、非抗生素的饮食方法。还需要进一步的对照试验来评估长期结果和机制。

---

## 85. AMD发布GPU虚拟化开源驱动，Radeon“计划中”

**原文标题**: AMD Publishes Open-Source Driver for GPU Virtualization, Radeon "In the Roadmap"

**原文链接**: [https://www.phoronix.com/news/AMD-GIM-Open-Source](https://www.phoronix.com/news/AMD-GIM-Open-Source)

AMD发布开源“GPU-IOV模块”(GIM)用于GPU虚拟化，专为Instinct加速卡设计。该模块允许在Linux上使用KVM hypervisor进行基于SR-IOV的硬件虚拟化。GIM管理GPU IOV虚拟化、虚拟功能配置、GPU调度、死锁检测、FLR复位以及PF/VF通信。

AMD GIM驱动程序的初始版本面向Instinct MI300X硬件，并在搭载ROCm 6.4的Ubuntu 22.04 LTS上进行了测试。该代码目前已在GitHub上提供，但AMD尚未宣布将驱动程序上游化到主线Linux内核的明确计划。

重要的是，该文章强调了这种虚拟化支持未来可能扩展到客户端Radeon独立GPU的可能性。AMD工程师Anush Elangovan在X上确认，客户端GPU支持“已在路线图中”，这是Radeon用户高度期待的一项功能。这表明用户最终或许能够在他们的Radeon显卡上使用SR-IOV和类似的虚拟化技术。

---

## 86. Show HN: Index – 新的开源浏览器代理

**原文标题**: Show HN: Index – New Open Source browser agent

**原文链接**: [https://github.com/lmnr-ai/index](https://github.com/lmnr-ai/index)

Index：一款用于自主执行复杂网络任务的全新开源浏览器代理。它利用具有视觉能力的推理LLM，并提供多种模型选择，包括Gemini 2.5 Pro/Flash、Claude 3.7 Sonnet和OpenAI o4-mini，允许用户平衡速度、成本和准确性。

用户可以通过`pip install lmnr-index`安装Index，并通过交互式CLI (`index run`) 运行它，该CLI具有浏览器状态持久性和实时更新功能，或者通过无服务器API使用它。还提供了一个聊天UI，供用户试用Index。

API被强调为在生产环境中使用Index的最简单方式，可管理浏览器会话和基础设施。Laminar用于提供高级浏览器代理可观测性。文章提供了通过API使用Index、使用CLI进行本地快速启动、使用代码运行代理、流式输出、启用可观测性以及自定义浏览器设置（CDP URL和视口大小）的代码示例。这些示例通常涉及导航到像news.ycombinator.com这样的网站并总结内容。该项目由Laminar团队制作。

---

## 87. 停用脸书和照片墙对用户情绪状态的影响

**原文标题**: The effect of deactivating Facebook and Instagram on users' emotional state

**原文链接**: [https://www.nber.org/papers/w33697](https://www.nber.org/papers/w33697)

国家经济研究局（NBER）于2025年4月发布的这份工作论文，调查了停用Facebook和Instagram对用户情绪状态的影响。该研究采用了2020年美国大选前进行的两个大型随机实验。

主要发现是，在选举前六周停用Facebook，与仅停用一周的对照组相比，在幸福感、抑郁和焦虑指标上产生了具有统计学意义的改善（0.060个标准差）。同样，停用Instagram相同的时间也带来了较小但仍显著的改善（0.041个标准差）。

进一步的探索性分析表明，Facebook停用的积极影响在35岁以上的人群中更为明显，而Instagram的影响在25岁以下的女性中更为突出。

该论文承认存在潜在的利益冲突，列出了许多作者曾接受Meta或相关公司提供的资金、旅行或报酬。尽管有这些披露，该研究仍提供了证据，表明暂时停用社交媒体可以积极影响用户的情绪健康，并且对不同人群的影响程度不同。

---

## 88. 找回你的Minitel，COMPUTEL图文电视BBS回归了

**原文标题**: Get your Minitel back, the COMPUTEL videotex BBS is back

**原文链接**: [https://cq94.medium.com/get-your-minitels-back-the-computel-videotex-bbs-is-back-1d8c42f1ea17](https://cq94.medium.com/get-your-minitels-back-the-computel-videotex-bbs-is-back-1d8c42f1ea17)

克里斯蒂安·奎斯特讲述了他复兴其COMPUTEL电视图文BBS的历程，该BBS最初于20世纪80年代在Apple IIe上运行。受到2012年Télétel信息亭“官方”关闭以及Julien即将出版的关于Minitel的书籍的启发，奎斯特开始了一个复活他旧服务器的项目。

他详细介绍了早期使用Minitel和Apple Tell卡的经验，后者使他的Apple IIe能够充当Minitel服务器。然后，他描述了Cristel的创建，这是一个简化电视图文服务器开发的BASIC扩展，以及COMPUTEL，他自己的服务器提供各种服务，如本地计算机俱乐部站点和邮件服务。文章随后详细介绍了向公司JCA的演变，该公司进一步开发了电视图文服务。

然后，重点转移到2017年恢复COMPUTEL的技术挑战。奎斯特收购了一台Apple IIc、Floppyemu和Apple Tell卡，并设法从他的旧软盘中恢复数据。克服了Linksys适配器的VOIP兼容性问题，他成功地使用专用VOIP线路（+33 1 8421 8116）将COMPUTEL重新上线。

奎斯特的动机源于乐趣、技术挑战以及Minitel文化和技术历史的保护。他希望这次复兴能够激励其他人创建微型服务器，并强调使用Raspberry Pi或Arduino与Minitel进行新项目的潜力，包括在法国建立一个潜在的Minitel博物馆。

---

## 89. 《世界大战动物园》影评：炸弹与野兽

**原文标题**: 'World War Zoos' Review: Of Bombs and Beasts

**原文链接**: [https://www.wsj.com/arts-culture/books/world-war-zoos-review-of-bombs-and-beasts-a037c4b6](https://www.wsj.com/arts-culture/books/world-war-zoos-review-of-bombs-and-beasts-a037c4b6)

无法访问文章链接。

---

## 90. Show HN: Rowboat - 多智能体系统的开源IDE

**原文标题**: Show HN: Rowboat – Open-source IDE for multi-agent systems

**原文链接**: [https://github.com/rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat)

Rowboat：一款开源IDE，旨在利用OpenAI的Agents SDK加速多智能体系统的开发。它允许用户从一个简单的想法开始，在几分钟内构建由人工智能驱动的工作流程，Rowboat的副驾驶会将这个想法转化为一个完整的多智能体系统。

主要功能包括连接到MCP（多链协议）服务器、导入工具以及通过HTTP API或Python SDK将生成的智能体集成到应用程序中。HTTP API允许直接交互，而Python SDK则提供了一种更具编程性的方法。

快速入门指南概述了如何使用Docker设置Rowboat、克隆存储库以及访问应用程序。该文档还包括如何使用HTTP API和Python SDK与Rowboat智能体进行交互的示例，说明了如何发送消息和接收响应。核心信息是Rowboat简化了创建和部署多智能体系统的过程。

---

## 91. 展示HN：我构建了一个AI，可以将GitHub代码库变成简易教程

**原文标题**: Show HN: I built an AI that turns GitHub codebases into easy tutorials

**原文链接**: [https://github.com/The-Pocket/Tutorial-Codebase-Knowledge](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge)

这个“Show HN”帖子介绍了一个AI代理，它能从GitHub代码库自动生成适合初学者的教程。该代理使用100行的Pocket Flow LLM框架构建，可以抓取仓库，分析代码结构并识别关键抽象，然后创建清晰、可视化的教程来解释代码的工作原理。

该帖子重点介绍了为AutoGen、FastAPI和NumPy等热门仓库生成的示例教程，展示了AI解释复杂项目的能力。它还提供了关于如何使用该工具的说明，包括克隆仓库、安装依赖项、配置LLM凭证（最好使用像Claude 3.7或O1这样的模型）以及运行`main.py`脚本。该脚本可以分析GitHub仓库URL或本地目录，允许用户指定包含/排除的文件、最大文件大小以及所需的输出语言。

作者强调使用“代理编码”进行开发，即人类设计，AI代理（如Cursor AI）负责编码。他们认为Pocket Flow是这种范式的关键推动者。YouTube开发教程和Substack帖子的链接提供了关于该工具的创建和使用的进一步见解。该帖子提到该项目已登上Hacker News首页，获得超过800个赞。它鼓励用户尝试该工具并分享他们生成的教程。

---

## 92. Show HN：我们做了一个速度极快的开源 GitHub 前端

**原文标题**: Show HN: We made a blazing-fast, open-source GitHub front end

**原文链接**: [https://gitfaster.dev/](https://gitfaster.dev/)

此“Show HN”帖子介绍了`gitfaster`，一个全新的开源、极简 GitHub 客户端，旨在比标准 GitHub 界面快得多。该项目旨在解决 GitHub 感觉像遗留软件的观感。主要功能包括：

*   **速度：** 主要关注速度，被描述为“快如闪电”，并且旨在“感觉很快”。
*   **预测性预取：** Gitfaster 预测用户导航并主动预取文件，从而减少加载时间。
*   **缓存：** 它缓存来自 GitHub API 的响应，通过避免冗余 API 调用来进一步提高性能。
*   **以性能为导向的设计：** 该客户端从一开始就以性能为中心进行构建。

该帖子强调 `gitfaster` 处于“早期 Beta”阶段，并提及 Next.js 和“Global Hackathon 2025”（可能是其开发背景）。主要目的是提供快速且响应灵敏的 GitHub 体验。

---

## 93. 狗狗币矿工代码支持美国国家劳工关系委员会举报人

**原文标题**: DOGE worker’s code supports NLRB whistleblower

**原文链接**: [https://krebsonsecurity.com/2025/04/doge-workers-code-supports-nlrb-whistleblower/](https://krebsonsecurity.com/2025/04/doge-workers-code-supports-nlrb-whistleblower/)

美国国家劳工关系委员会(NLRB)的举报人丹尼尔·贝鲁里斯声称，埃隆·马斯克的政府效率部门(DOGE)的员工非法访问并下载了该机构系统中的敏感案件数据。贝鲁里斯称，DOGE官员获得了具有无限制访问权限且能掩盖其活动的“租户管理员”账户。

调查显示，DOGE账户从GitHub下载了三个代码库，其中一个与DOGE员工马尔科·埃莱兹开发的程序非常相似，埃莱兹有争议的社交媒体帖子历史以及过去在财政部的安全违规记录。该代码“async-ip-rotator”旨在绕过基于IP的速率限制，用于网络爬取和暴力破解攻击。

贝鲁里斯担心，未经授权的数据传输，涉及超过10GB的NLRB案件文件，可能会为参与该机构劳资纠纷的公司提供不公平的优势，可能使他们能够识别并报复工会组织者。下载的代码还包括用于逆向工程API和自动化基于Web任务的工具，引发了进一步的安全问题。GitHub上对埃莱兹代码的详细评论称其“不安全、不可扩展且是根本的工程失败”，进一步突显了潜在风险。自从特朗普总统解雇委员会成员以来，NLRB一直处于瘫痪状态，造成了不确定的法律环境，并使该机构缺乏运作所需的法定人数。

---

## 94. 我在意大利参加创业周末比赛的经历

**原文标题**: My experience participating to a startup weekend competition in Italy

**原文链接**: [https://danielpetrica.com/my-experience-of-participating-to-a-startup-weekend-competition-in-italy/](https://danielpetrica.com/my-experience-of-participating-to-a-startup-weekend-competition-in-italy/)

无法访问文章链接。

---

## 95. CubeCL：用Rust编写的CUDA、ROCm和WGPU GPU内核

**原文标题**: CubeCL: GPU Kernels in Rust for CUDA, ROCm, and WGPU

**原文链接**: [https://github.com/tracel-ai/cubecl](https://github.com/tracel-ai/cubecl)

CubeCL 是一个 Rust 扩展，旨在简化为 CUDA、ROCm/HIP 和 WGPU 编写高性能、多平台 GPU 内核的过程。它利用 Rust 的零成本抽象和过程宏来实现可维护且高效的计算内核的开发。主要特性包括自动向量化、编译时优化（允许动态修改编译器 IR 以实现指令专门化、循环展开等）以及自动调优（在运行时对内核进行基准测试以选择最佳配置）。

CubeCL 专注于“立方体”拓扑，将硬件差异抽象成一个统一的 3D 模型。它支持函数、泛型和结构体，并计划支持更广泛的 Rust 特性。与直接生成 IR 不同，过程宏生成 Rust 函数，这些函数在被调用时创建 IR，从而促进编译时优化和向量化。生成的代码是有效的 Rust 代码，无需特定的运行时依赖项即可进行捆绑。

CubeCL 旨在为 Rust 中的高性能和科学计算创建一个生态系统，包括一个在 NVIDIA 上支持 Tensor Core 的矩阵乘法模块。该项目目前处于 alpha 阶段，但已被用于 Burn 中，提供了一种编写可在各种硬件平台上移植的优化内核的方法。团队鼓励贡献，并通过 Discord 提供支持。

---

## 96. Swift 容器插件

**原文标题**: Swift Container Plugin

**原文链接**: [https://github.com/apple/swift-container-plugin](https://github.com/apple/swift-container-plugin)

Swift容器插件简化了使用Swift包管理器构建和发布Swift服务器应用程序的容器镜像的过程。这使得开发者能够轻松地将其Swift服务器打包，以便部署在任何基于容器的云服务或本地容器运行时上。

该插件专注于`Package.swift`中定义的可执行产品。一个简单的命令(`swift package --swift-sdk ... build-container-image ...`)就能构建容器镜像并将其发布到指定的注册表中。该过程包括构建应用程序、创建必要的层以及将它们上传到注册表。

要运行构建好的镜像，可以使用像`podman`这样的容器运行时。文章提供了一个本地拉取并运行镜像的示例，展示了Swift服务器如何在容器中启动。

该插件兼容macOS和Linux，需要Swift 6.0或更高版本。在macOS上，需要使用Swift SDK（例如Swift Static Linux SDK）进行交叉编译，才能构建与Linux兼容的可执行文件。虽然创建镜像不需要容器运行时，但运行镜像需要。

文章鼓励用户查阅插件文档和示例，以获取详细的设置说明。

---

## 97. 像素是长度和面积的单位。

**原文标题**: Pixel is a unit of length and area

**原文链接**: [https://www.nayuki.io/page/pixel-is-a-unit-of-length-and-area](https://www.nayuki.io/page/pixel-is-a-unit-of-length-and-area)

本文探讨了在数字图像处理中将“像素”作为计量单位时出现的冲突和常常不合逻辑的用法。文章指出，“像素”既被用作线性单位（例如，图像宽度以像素为单位），也被用作面积单位（例如，相机传感器的百万像素），导致在使用面积=宽度×高度等数学公式时出现维度不一致。

作者强调了一个悖论，即如果将像素既视为长度又视为面积，那就意味着像素²=像素，这表明像素是无量纲的。作者提出了两个不完美的解决方案：

1. **将像素定义为一个正方形**，其物理尺寸取决于设备，并使用“像素边长”或“√像素”作为线性单位。
2. **坚持认为像素始终是长度单位**，并将面积称为“平方像素”，这需要更大的数字或别扭的前缀单位（如平方千像素）。

文章承认这个问题并不关键，因为像素很少参与复杂的计算。作者将这种模糊性与“磅”既用作质量单位又用作力的单位进行比较，而公制系统则在千克和牛顿之间保持了明确的区分。最终，作者得出结论，通常将“像素”用作计量单位缺乏科学背景下所期望的精确性和一致性。

---

## 98. 人工智能领域的收购、整合与创新

**原文标题**: Acquisitions, consolidation, and innovation in AI

**原文链接**: [https://frontierai.substack.com/p/acquisitions-consolidation-and-innovation](https://frontierai.substack.com/p/acquisitions-consolidation-and-innovation)

无法访问文章链接。

---

## 99. Show HN: Pomo – 无需代码即可管理 Stripe 促销代码

**原文标题**: Show HN: Pomo – Manage your Stripe promo codes without code

**原文链接**: [https://usecopi.com/69fb5996](https://usecopi.com/69fb5996)

“Show HN: Pomo – 无需代码管理你的Stripe促销码”一文介绍了一个名为Pomo的工具，旨在简化Stripe促销码的创建、管理和分析。其核心价值在于让用户无需编码专业知识即可直接管理他们的促销活动。

虽然文章本身很简短，但我们可以推断出Pomo可能提供了一个用户友好的界面，用于：

*   **创建促销码：** 提供定义促销类型、折扣、资格标准和兑换限制的功能。
*   **管理现有代码：** 允许轻松跟踪代码使用情况、修改现有代码以及停用过期或不需要的促销活动。
*   **分析性能：** 提供关于哪些促销码最有效、用户与折扣相关的行为以及促销活动对收入的总体影响的见解。

Pomo与“Copi - 面向销售团队的安全文件和链接共享”的并列无关，很可能是一个单独的、随机插入的简短说明。因此，总结仅关注Pomo的预期功能和优势。目标是帮助用户更好地利用他们的Stripe促销活动，并减少促销管理的技术负担。

---

## 100. 哈佛大学1869年入学考试——代数

**原文标题**: Harvard Admission Exam 1869 – Algebra

**原文链接**: [https://corca.app/doc/B5r2CVmqXUbnv8WsxD5Fx](https://corca.app/doc/B5r2CVmqXUbnv8WsxD5Fx)

本文实质上仅包含标题和关于存在协作数学编辑器的说明。标题表明主题是“1869年哈佛入学考试 – 代数”。其余内容似乎与数学编辑器本身有关，包括其名称（“Corca”），目的（“协作数学编辑器”），加载消息以及标准样板信息，如“关于”，“常见问题解答”，“服务条款”，“隐私政策”和版权声明。

因此，要点是：

1. **历史背景：** 该文档涉及1869年哈佛入学考试的代数考试。
2. **工具指示：** 它表明存在或计划使用名为“Corca”的协作数学编辑器。
3. **内容有限：** 在提供的资料中没有可见的实际考试内容。这篇文章本质上是一个标题加上关于数学编辑器平台的信息。

---

