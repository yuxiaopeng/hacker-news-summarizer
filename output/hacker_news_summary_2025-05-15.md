# Hacker News 热门文章摘要 (2025-05-15)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 一个微型玻尔兹曼机

**原文标题**: A Tiny Boltzmann Machine

**原文链接**: [https://eoinmurray.info/boltzmann-machine](https://eoinmurray.info/boltzmann-machine)

本文介绍了玻尔兹曼机（BM），一种用于无监督学习和生成式AI的神经网络，它模拟了物理学中的能量原理。玻尔兹曼机由可见神经元和隐藏神经元组成，它们之间具有加权连接。通用玻尔兹曼机的神经元之间都有连接，使其功能强大，但训练的计算成本很高。

本文重点介绍受限玻尔兹曼机（RBM），这是一种可见神经元和隐藏神经元之间没有直接连接的特殊情况。这种限制简化了训练。RBM是基于能量的模型，其中网络配置的能量由神经元状态、权重和偏差定义。

训练的目标是调整权重和偏差，以最小化训练数据的能量，从而有效地学习可见单元的概率分布。训练完成后，RBM可以使用吉布斯采样生成与训练数据相似的新数据。

训练过程，即对比散度，包括：将可见单元钳制到训练数据，对隐藏单元进行采样，重建可见单元，重新采样隐藏单元，并根据数据和模型期望之间的差异更新权重。提供的模拟器允许用户可视化训练过程，并观察RBM如何学习重建输入数据。附录提供了对比散度算法的数学推导，详细说明了权重和偏差的更新规则。

---

## 2. Show HN: 利用Min.js风格压缩技术文档以供LLM上下文使用

**原文标题**: Show HN: Min.js style compression of tech docs for LLM context

**原文链接**: [https://github.com/marv1nnnnn/llm-min.txt](https://github.com/marv1nnnnn/llm-min.txt)

本文介绍了llm-min.txt，一种用于压缩技术文档以供大型语言模型(LLM)使用的新方法。它解决了人工智能编码助手因其“知识截止”而缺乏最新库信息的问题。与现有解决方案（如可能过大的llms.txt）和Context7（一种“黑盒”方法）不同，llm-min.txt采用人工智能将文档提炼成一个超浓缩的结构化摘要。

llm-min.txt使用结构化知识格式（SKF），将信息组织成DEFINITIONS、INTERACTIONS和USAGE_PATTERNS部分，针对机器解析而非人类可读性进行了优化。配套的llm-min-guideline.md文件为人工智能解释提供了解码说明。文章声称，与原始文档相比，token减少了90-95%，从而显著提高了人工智能处理和理解信息的能力。

文章提供了一个快速入门指南，包括安装说明和示例命令。它还强调了使用推荐的Gemini AI模型（gemini-2.5-flash-preview-04-17）的重要性，因为它在压缩任务中具有先进的推理能力、大的上下文窗口和成本效益。最后，它简要概述了llm-min工具的内部工作原理。

---

## 3. 预订可用会议室的恶意服从

**原文标题**: Malicious compliance by booking an available meeting room

**原文链接**: [https://www.clientserver.dev/p/malicious-compliance-by-booking-an](https://www.clientserver.dev/p/malicious-compliance-by-booking-an)

2011年，拉里·佩奇作为谷歌新任CEO，试图提高会议效率。他推行了一项政策，规定会议必须有决策者，人数上限为10人，要求积极参与，并且时长设定为50分钟而非1小时，在会议之间留出10分钟的缓冲时间。谷歌日历也更新为50分钟的默认时长。

然而，人们实际上并没有在50分钟后结束会议。纽约办事处的一个团队巧妙地利用了这一点。他们的站立会议只有10分钟，并且他们注意到50分钟默认时长所造成的日历空隙。他们开始预订会议室中那些空闲的10分钟时段，迫使较长的会议在站立团队到达时准时在50分钟结束，这符合佩奇政策的字面规定，但也可能令很多人感到沮丧。作者亲眼目睹了这种情况两次，并赞赏该团队的奉献精神（或恶作剧），但从未了解他们的身份或真正动机。这种行为是恶意合规的完美例证，利用系统设计来打破现状。

---

## 4. 新鲜事更新

**原文标题**: An Update on Fresh

**原文链接**: [https://deno.com/blog/an-update-on-fresh](https://deno.com/blog/an-update-on-fresh)

Fresh 2 最新进展：基于 Deno 的下一代 Web 框架

本文介绍了基于 Deno 构建的下一代 Web 框架 Fresh 2 的最新进展。虽然开发时间比预期要长，但它现在已进入 alpha 阶段，并为 Deno 的主网站和 Deno Deploy 提供支持。

延迟的原因在于需要增强底层 Deno 平台和 JavaScript 注册表 (JSR)，重点关注 Node 和 npm 兼容性，以实现第三方包的无缝集成，并解决 import map 和依赖管理的问题。此外，下一代 Deno Deploy（包括构建步骤）的开发也作为 Fresh 2 的测试用例。

Fresh 2 旨在更具可扩展性、更快且更易于使用。主要特性包括类似 Express/Hono 的 API、真正的异步组件以及用于创建中间件的新插件系统。它还包括对预编译 JSX 的开箱即用支持，从而显著加快渲染速度。

Alpha 版本 (2.0.0-alpha.30) 现已可供测试，欢迎用户提供反馈。建议使用 Deno 2.3 以获得最佳体验，它提供了改进的 `deno compile` 和本地 npm 包。用户可以使用脚手架脚本创建新项目，或使用更新脚本升级现有项目。稳定版本预计将于 2025 年第三季度末（可能在 9 月）发布。

---

## 5. 昂菲姆的世界：历史上的儿童艺术家

**原文标题**: Onfim's world: Child artists in history

**原文链接**: [https://resobscura.substack.com/p/onfims-world-medieval-child-artists](https://resobscura.substack.com/p/onfims-world-medieval-child-artists)

无法访问文章链接。

---

## 6. Fetii (YC S22) 正在招聘

**原文标题**: Fetii (YC S22) Is Hiring

**原文链接**: [https://www.ycombinator.com/companies/fetii/jobs/QDjleWs-senior-operations-manager-fetii](https://www.ycombinator.com/companies/fetii/jobs/QDjleWs-senior-operations-manager-fetii)

Fetii，一家由Y Combinator (S22) 和马克·库班投资的团体拼车初创公司，正在招聘一位高级运营经理，以帮助扩大其运营规模。该职位提供有竞争力的薪资、有意义的股票期权以及与创始人的直接沟通机会，是一个全职职位，工作地点位于德克萨斯州奥斯汀（混合办公优先，可考虑远程），需要能适应不规律的工作时间，包括晚上和周末。

高级运营经理将是Fetii运营的中心人物，负责司机和车辆服务提供商(VSP)的管理、合规和监管监督、质量控制、安全执行（使用Samsara）以及销售运营/活动执行。主要职责包括寻找和管理司机、确保车队合规、维护安全标准以及协调活动物流。

Fetii正在寻找一位高度有组织能力、具有创业精神和经验丰富的个人，该个人应具有强大的职业道德、解决问题的能力，并愿意全身心投入到公司的使命中。理想的候选人应具有运营、物流或初创企业环境的经验。他们必须是系统思考者，能够在压力下茁壮成长，并且对细节有极高的关注度。

Fetii的目标是通过利用由15人座货车组成的网络提供按需团体乘车服务，从而颠覆团体交通运输行业，旨在缓解城市拥堵并减少道路上不必要的车辆。他们已经运送了超过61.7万名乘客，并减少了超过13万辆车辆。

---

## 7. 小波树简介 (2011)

**原文标题**: Wavelet Trees: An Introduction (2011)

**原文链接**: [https://www.alexbowe.com/wavelet-trees/](https://www.alexbowe.com/wavelet-trees/)

本文介绍了小波树（Wavelet Tree），一种用于高效回答大字母表序列上rank查询的数据结构。小波树将字符串组织成一个位向量的层次结构，从而能够以O(log₂A)的时间复杂度执行rank查询，其中A是字母表的大小。

其构造过程涉及递归地将字母表对半分，并将每一半编码为0或1，从而创建一个二叉树。树中的每个节点存储一个位向量，表示它所覆盖的字符串部分的编码。这些位向量可以使用诸如RRR或Sadakane和Okonohara的rank索引之类的结构进行进一步的压缩和索引。

在小波树上执行rank查询涉及遍历树，使用每一层的编码来引导搜索到适当的子树。查询在路径上的每个节点执行二元rank查询，直到到达叶节点，从而提供最终的rank答案。

本文还提到小波树可以与后缀数组结合使用进行模式搜索，实现O(P log₂A)的时间复杂度，其中P是模式长度。作者鼓励读者探索select查询和霍夫曼形状的小波树，并指出了Francisco Claude的libcds中的一个实现。

---

## 8. 模式生物并非一成不变

**原文标题**: Model Organisms Are Not Static

**原文链接**: [https://www.asimov.press/p/model-organisms-are-not-static](https://www.asimov.press/p/model-organisms-are-not-static)

这篇阿西莫夫出版社的文章《模式生物并非静止不变》探讨了科学研究中的可重复性危机，尤其是动物研究方面。文章认为，模式生物体内积累的基因突变会对实验结果产生重大影响。

文章重点介绍了一项2023年的研究，该研究表明脊椎动物物种间的突变率差异很大，实验室小鼠平均每代获得15个新的突变。虽然这些突变大多不会直接影响蛋白质编码基因，但它们可以改变基因调控，从而可能影响实验结果。作者指出，实验室中控制育种的做法，虽然最大限度地减少了遗传多样性，但可能会无意中保留自然选择会在野外淘汰的有害突变。

文章提到了杰克逊实验室通过冷冻保存和定期“重置”小鼠基因组来缓解这个问题的努力，但即使是这些方法也无法完全阻止突变的积累。

文章暗示，科学家们可能在不知不觉中将某些特征归因于这些积累的生殖系错误。文章呼吁研究人员更频繁地对他们的模式生物品系进行测序，并评估基因调控模式，以将基因改变的动物排除在育种计划之外。文章还提到，研究人员开始冷冻保存其他模式生物的胚胎，以限制突变的负担。

文章总结道，研究人员必须积极应对这些突变引起的变异，以避免加剧可重复性危机。认识到基因组变化对可重复性构成的威胁，研究人员开始冷冻保存其他动物模型胚胎，以限制突变的负担。果蝇研究人员已经开发出一种冷冻果蝇胚胎的方法。

---

## 9. Show HN: 实时高斯溅射

**原文标题**: Show HN: Real-Time Gaussian Splatting

**原文链接**: [https://github.com/axbycc/LiveSplat](https://github.com/axbycc/LiveSplat)

LiveSplat 是一款闭源算法，用于利用 RGBD 相机流进行实时高斯溅射，它是 VR 远程机器人系统的一部分。由于社区的兴趣，作者 Mark Liu 将以 alpha 质量公开发布该算法。它需要 Python 3.12+、Windows 或 Ubuntu、x86_64 CPU 和 Nvidia 显卡。安装涉及使用 `pip` 安装 wheel 文件（Ubuntu 和 Windows 的 URL 不同）。要使用 LiveSplat，用户必须创建一个集成脚本来提供 RGBD 流，并且该存储库提供了一个用于 Intel Realsense 设备的示例脚本。尽管是 alpha 软件，但作者希望用户会喜欢尝试 LiveSplat。由于其闭源性质，作者正在探索潜在的商机，并鼓励有兴趣的企业通过 mark@axby.cc 联系他，以咨询许可/集成事宜。支持和讨论可在他们的 Discord 服务器上进行。

---

## 10. Elixir 的 Lua

**原文标题**: Lua for Elixir

**原文链接**: [https://davelucia.com/blog/lua-elixir](https://davelucia.com/blog/lua-elixir)

本文宣布发布Lua v0.1.0，这是一个Elixir库，得益于底层的Luerl库（一个用Erlang编写的Lua解析器、编译器和运行时），它允许直接在BEAM VM上执行沙盒化的Lua代码。该Elixir库通过更好的错误消息和文档增强了Luerl的功能。主要功能包括使用`deflua`宏和`Lua.load_api/2`，用Elixir API扩展Lua的能力，以及使用`~LUA` sigil进行编译时语法验证。

该库起源于TV Labs，在那里它被用于通过将拖放式自动化构建器编译为Lua，在物理设备上执行集成测试。作者重点介绍了Erlang和Luerl的创建者Robert Virding，并解释了Luerl的起源：探索在BEAM上实现一种命令式语言。

未来的计划包括将Elixir Lua库合并到Luerl中，以创建2.0.0版本，其中包含改进的错误消息、堆栈跟踪、文档和沙盒功能，以及与Lua生态系统的更深入集成。作者鼓励通过Slack、Discord或GitHub进行贡献。

---

## 11. 人类

**原文标题**: Human

**原文链接**: [https://quarter--mile.com/Human](https://quarter--mile.com/Human)

这似乎是一个网站或文章的极短片段。基于标题“Human”以及导航元素“Writing”、“Subscribe”和“Contact”，我们可以推断出以下内容：

*   **主题：** 该文章可能探讨与人性、为人或人类经验相关的主题。 在没有实际内容的情况下，我们只能推测具体的角度。

*   **类型：** 鉴于存在“Writing”，它可能是一篇与该主题相关的博客文章、散文或创意写作作品。

*   **目的：** 该网站旨在通过有关此主题的内容吸引读者，并可能通过订阅来建立受众群体。

*   **行动号召：** 鼓励读者订阅更多内容，并且可以通过联系方式与作者或网站管理员联系。

总而言之，“Human”似乎是一篇关于人性的文章或网站版块，可能包含有关人性的创意写作，其目的是吸引读者并建立订阅基础。 导航表明作者提供类似内容并乐于联系。

---

## 12. 互联网遗迹

**原文标题**: Internet Artifacts

**原文链接**: [https://neal.fun/internet-artifacts/](https://neal.fun/internet-artifacts/)

无法访问文章链接。

---

## 13. 寻路

**原文标题**: Pathfinding

**原文链接**: [https://juhrjuhr.itch.io/deep-space-exploitation/devlog/945428/9-pathfinding](https://juhrjuhr.itch.io/deep-space-exploitation/devlog/945428/9-pathfinding)

JuhrJuhr开发日志 #9 详述了他们游戏《深空探索》中实现的寻路系统。该系统旨在处理动态、可破坏的环境，并具有小行星风格的环绕效果。核心算法是A*，并利用空间划分来优化世界查询。

主要特点包括：

*   **空间划分：** 树结构划分游戏区域，以实现高效的碰撞检测。父节点查询确定是否需要单独检查子节点。
*   **动态环境处理：** 节点的阻塞状态被缓存，但会定期（每500毫秒）失效，以适应移动或被破坏的物体。
*   **自然路径：** 基于与物体距离的邻近度评分会影响遍历成本，从而创建倾向于避开障碍物的路径，但在需要时可以近距离导航。
*   **环绕路径：** 系统通过将边界节点分配给对面的邻居来处理游戏区域的环绕。添加屏幕外节点以引导NPC绕过环绕点。
*   **效率：** 寻路被拆分到多个游戏帧中，以防止减速，从而平衡性能和路径请求的异步处理。曾考虑过多线程，但因世界状态管理的复杂性而被放弃。

JuhrJuhr强调了创建自定义解决方案的满足感，并优先考虑性能和自然外观的路径。该系统已经过测试，现在正被集成到NPC行为中。未来的改进包括基于世界变化有选择性地使查询缓存失效。

---

## 14. 受 Python 启发，基于 Serde 的 Rust API

**原文标题**: A Rust API Inspired by Python, Powered by Serde

**原文链接**: [https://ohadravid.github.io/posts/2025-05-serde-reflect/](https://ohadravid.github.io/posts/2025-05-serde-reflect/)

本文探讨了如何创建受 Python 动态功能启发的 Rust API，并利用 `serde` crate 进行（反）序列化。作者旨在提供比原始 API 更友好的界面，使使用者能够更轻松地查询数据。

文章首先展示了 Python WMI 接口如何优雅地抽象系统信息。然后，它将此与一个涉及 `Object` 和 `Value` 枚举的初级 Rust API 进行对比，该 API 需要冗长的手动类型检查。

作者提出了一个更具 Python 风格的设计，允许用户定义表示数据的结构体并直接查询它们。最初的方法涉及创建自定义 `Queryable` trait，但作者随后过渡到使用 `serde` 的 `Deserialize` trait，通过 `derive(Deserialize)` 实现自动实现生成。

核心思想是“欺骗” Serde 从原始 API 数据中创建用户定义的结构体实例，类似于它处理不同的数据格式（如 JSON）的方式。文章随后深入研究了 Serde 的内部 trait（`Deserialize`、`Deserializer`、`Visitor`、`MapAccess`），通过为 `Fan` 结构体手动实现 `Deserialize`，来说明 Serde 如何管理数据转换过程。最终，文章展示了如何以一种非常规的方式使用 `serde` 来创建灵活且直观的 Rust API。

---

## 15. 加州将居民个人健康数据发送给领英。

**原文标题**: California sent residents' personal health data to LinkedIn

**原文链接**: [https://themarkup.org/pixel-hunt/2025/04/28/how-california-sent-residents-personal-health-data-to-linkedin](https://themarkup.org/pixel-hunt/2025/04/28/how-california-sent-residents-personal-health-data-to-linkedin)

标记调查显示，加州全保（该州健康保险市场）通过名为“洞察标签”的追踪工具向领英发送敏感的用户数据。这些数据包括用户对是否失明、怀孕、变性、家暴受害者或大量使用处方药等问题的回答，以及他们的种族、婚姻状况和选择的医疗服务提供者。该数据收集始于2024年2月，是广告宣传活动的一部分。

加州全保此后已删除追踪器，并正在审查其安全协议。他们表示，数据共享是营销机构过渡的一部分。然而，专家们对在未经用户同意的情况下，与领英这样一家营利性公司共享如此敏感的健康数据所带来的隐私影响表示担忧。

这一事件引发了批评和调查呼吁，包括众议员凯文·凯利要求卫生与公众服务部调查潜在的违反 HIPAA 法规的行为。加州全保已承认无意共享数据，并正在审查涉及数据的范围。领英禁止在其收集敏感数据的页面上使用“洞察标签”。

该事件凸显了对网站追踪器普遍存在以及需要更强有力的数据隐私法规来保护消费者健康信息的更广泛担忧。领英已经面临多起与医疗信息收集相关的集体诉讼。

---

## 16. Coinbase称黑客贿赂员工窃取客户数据，勒索2000万美元。

**原文标题**: Coinbase says hackers bribed staff to steal customer data, demanding $20M ransom

**原文链接**: [https://www.cnbc.com/2025/05/15/coinbase-says-hackers-bribed-staff-to-steal-customer-data-and-are-demanding-20-million-ransom.html](https://www.cnbc.com/2025/05/15/coinbase-says-hackers-bribed-staff-to-steal-customer-data-and-are-demanding-20-million-ransom.html)

Coinbase披露，网络罪犯贿赂海外客服人员窃取敏感客户数据，勒索2000万美元。此次泄露可能导致Coinbase损失高达4亿美元用于修复，涉及被盗信息包括姓名、地址、电话号码、电子邮件、经过遮蔽的银行账户详细信息、社安号码后四位、政府ID图像和账户余额。密码和私钥未受损，Coinbase Prime账户保持未受影响。

该公司检测到泄露，解雇了涉事员工，通知了受影响的客户，并加强了欺诈监控。Coinbase正在与执法部门合作，并拒绝支付赎金。相反，他们提供2000万美元赏金，以获取能导致罪犯被捕和定罪的信息。

尽管发生了泄露事件，Coinbase宣布了一项收购以扩大其全球影响力，并将于下周被纳入标准普尔500指数。首席执行官Brian Armstrong的目标是让Coinbase在未来5-10年内成为顶级的金融服务应用程序。该公司将向被骗将资金发送给攻击者的客户进行赔偿。

---

## 17. AlphaEvolve：基于 Gemini 的高级算法设计编码代理

**原文标题**: AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms

**原文链接**: [https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)

AlphaEvolve：利用Gemini模型的新型AI智能体革新算法设计与优化。这种进化编码智能体结合了大型语言模型的创造性问题解决能力与自动化评估器，从而增强数学和实际计算应用的算法。

AlphaEvolve已展示出显著的影响，包括改进谷歌数据中心调度（恢复0.7%的计算资源），协助硬件设计（优化TPU中的算术电路），以及增强AI训练和推理（Gemini中的矩阵乘法速度提升23%，FlashAttention内核速度提升高达32.5%）。

除了内部应用，AlphaEvolve还在推动数学的前沿发展。它发现了一种更快的4x4复值矩阵乘法算法，超越了1969年的解决方案。它还重新发现了75%的50多个开放数学问题的最新解决方案，并改进了20%的已知解决方案，包括推进了11维的亲吻数问题。

AlphaEvolve的通用性使其能够解决可以用算法描述并自动验证的问题，暗示了其在材料科学、药物发现和可持续性方面的潜在应用。谷歌计划为学术用户推出早期访问计划，并正在探索更广泛的可用性。AlphaEvolve团队相信，随着大型语言模型在编码方面变得更好，它将继续改进。

---

## 18. 门户书：一部废止经典的教训

**原文标题**: Gateway Books: The lessons of a defunct canon

**原文链接**: [https://thepointmag.com/examined-life/gateway-books/](https://thepointmag.com/examined-life/gateway-books/)

本文探讨了特定知识青年时期的“入门书籍”，重点关注塞林格、冯内古特和凯鲁亚克等作家，以及日后对他们的复杂情感。作者回忆了自己青少年时期对这些作家的崇敬，却发现他们在大学里不那么受推崇，从而转向了新的经典作品。

在母亲要求清理这些装箱书籍的提示下，作者反思了它们所产生的持久影响，并探讨了其他人是否也有类似的感受。一条关于对“白人男性中产阶级经典”作品喜好的推文引发了大量回应，证实了一种共同的亚文化体验。

本文研究了这些书籍，通常是畅销书和反文化试金石，是如何被发现的，通常是在前互联网时代通过偶然相遇。这些书籍引起了孤独、疏离的青少年的共鸣，提供了安慰，并承诺他们可以加入一个迷人、前卫的社群。它们经常美化反社会行为和男性友谊，吸引了性欲受挫的青少年男性。

最终，这些书籍为超越学校和社会期望的更精彩的生活提供了希望。然而，作者承认，这些书籍中宣扬的“自由”和“经验”往往是模糊的，难以转化为具体的行动。这些入门书籍，由于其内在的矛盾性，充当了暂时的逃避和对不同未来的承诺，使青春期的日常变得可以忍受。

---

## 19. Show HN: Undetectag，用AirTag追踪失窃物品

**原文标题**: Show HN: Undetectag, track stolen items with AirTag

**原文链接**: [https://undetectag.com/](https://undetectag.com/)

Undetectag旨在增强Apple AirTag追踪被盗物品的功能。它声称能显著降低（95%）窃贼发现和移除AirTag的可能性。该产品似乎是现有AirTag的附加组件，但具体性质未作详细说明。

其主要应用场景是保护易被盗的贵重物品，例如汽车、船只、自行车、摩托车、行李箱和背包。该网站通过发现链接推广该产品，并鼓励用户联系他们咨询问题。

本质上，Undetectag将其定位为一种使AirTag在防盗应用中更有效的方式，通过使其更难被检测到来实现。

---

## 20. 在复杂系统工作：我在谷歌的工作经验

**原文标题**: Working on complex systems: What I learned working at Google

**原文链接**: [https://www.thecoder.cafe/p/complex-systems](https://www.thecoder.cafe/p/complex-systems)

本文《复杂系统工作：我在谷歌的工作心得》区分了复杂问题和复杂问题，强调复杂系统需要适应性和创新性的解决方案。作者提出了复杂系统的五个关键特征：涌现行为、延迟后果、局部与全局优化问题、滞后效应和非线性。规模本身并不能使系统变得复杂，关键在于这些行为的存在。

作者提供了在复杂环境中导航的实用策略，包括倾向于可逆决策（亚马逊的双向门框架）、通过考虑局部和全局影响来超越直接指标进行思考、拥抱创新以找到独特的解决方案、实施受控发布（特性开关、金丝雀发布、渐进式发布、影子测试）、优先考虑可观测性以进行系统理解和调试、利用模拟测试（重放过去事件、确定性模拟测试）、考虑使用机器学习进行自适应模式检测，以及培养强大的团队协作。

关键在于认识到您所处理的系统类型（复杂与复杂），并相应地调整您的问题解决方式。许多系统兼具两者，需要对何时结构化解决方案足够，何时适应性至关重要有细致的理解。作者在谷歌的经验强调了在复杂环境中进行非常规思考、数据驱动的决策和协作解决问题的重要性。

---

## 21. 图着色最快方法

**原文标题**: The Fastest Way yet to Color Graphs

**原文链接**: [https://www.quantamagazine.org/the-fastest-way-yet-to-color-graphs-20250512/](https://www.quantamagazine.org/the-fastest-way-yet-to-color-graphs-20250512/)

本文探讨了一种新开发的图着色算法。图着色是一个与多种现实场景（如空中交通管制）相关的问题。其目标是以这样一种方式为图的边（代表路径或连接）分配颜色：连接到同一顶点（点）的任何两条边都不共享相同的颜色，代表避免冲突。

此前，图着色算法速度缓慢且停滞数十年。由Sepehr Assadi、Soheil Behnezhad、Martín Costa等人开发的新算法通过专注于同时着色多条边而不是优化单条边的着色，实现了接近最优的速度。他们使用了一种受家居装修启发的“预处理”技术来准备图，使其更容易着色。这包括对图的大部分进行随机着色，留下一些策略性的边未着色，然后快速地对其进行着色。

新算法的运行时间与m log m成正比，其中m是边的数量，使其“接近线性”且与顶点的数量无关。与以前依赖于顶点数量的算法相比，这是一个显著的改进。专家称之为一项突破，但其实际应用取决于所涉及的常数因子的值。该团队的目标是通过消除对随机化的需求并消除对数项来实现真正的线性时间，从而进一步改进该算法。

---

## 22. 研究人员确定了轻玻色暗物质的根本限制

**原文标题**: Researchers establish fundamental limit on how light bosonic dark matter can be

**原文链接**: [https://phys.org/news/2025-05-fundamental-limit-bosonic-dark.html](https://phys.org/news/2025-05-fundamental-limit-bosonic-dark.html)

研究人员确定超轻玻色子暗物质粒子的质量必须大于2.2 × 10-21电子伏特(eV)，从而建立了其质量的新基本下限。这比之前基于海森堡不确定性原理的估计值大100倍。

该研究发表在《物理评论快报》上，利用对银河系卫星星系狮子座II的观测来推断暗物质的分布。通过分析狮子座II内部恒星的运动，研究人员使用名为GRAVSPHERE的工具创建了5000个与观测到的恒星运动学一致的可能暗物质密度剖面。然后，将这些剖面与利用名为JAXSP的计算工具创建的，代表各种质量的暗物质的量子波函数产生的密度剖面进行比较。

研究小组发现，如果暗物质粒子太轻，它们的量子模糊性（由于不确定性原理）将阻止它们以狮子座II中观察到的方式集中。这使得他们能够建立比以前更严格的暗物质质量下限。

这一发现对现有的模糊暗物质等模型构成了巨大压力，模糊暗物质提出的粒子质量约为10-22 eV。研究人员强调，他们的结论是可靠的，主要依赖于局部宇宙信息和第一性原理物理学。他们计划将他们的分析扩展到混合暗物质模型，该模型假设暗物质由具有不同质量的多个粒子组成。

---

## 23. 快机器，慢机器 (2023)

**原文标题**: Fast machines, slow machines (2023)

**原文链接**: [https://jmmv.dev/2023/06/fast-machines-slow-machines.html](https://jmmv.dev/2023/06/fast-machines-slow-machines.html)

Julio Merino的博客文章《快机器，慢机器(2023)》探讨了现代计算机的悖论：它们比旧机器强大得多，但在基本任务中却表现出明显的UI延迟。作者通过比较上世纪90年代末/本世纪初的Windows NT 3.51机器与运行Windows 11和macOS的现代系统上的应用程序启动时间，引发了一个病毒式的Twitter话题。

Merino承认图形、网络和SSD等方面的进步，但他认为这些进步并未转化为始终如一的响应式UI。他批评将记事本重写为UWP应用程序，以及Windows终端的臃肿，认为这些都是不必要的性能倒退的例子。即使是在高端硬件上，Windows和macOS的用户体验仍然会受到明显的延迟影响。

Merino驳斥了将缓慢归因于图形动画或更高分辨率显示的解释，指出禁用这些功能并不能消除延迟。他认为，核心问题在于优先级从性能转向了开发者时间，并指出Electron等框架的兴起是造成该问题的原因。对跨平台开发和基于Web的解决方案的追求往往会牺牲原生性能，导致应用程序变得缓慢和臃肿。本质上，这篇文章是对现代软件开发格局的批判，在这个格局中，效率和响应性已退居次要地位。

---

## 24. 沃尔玛正准备迎接它的下一位顾客：人工智能购物代理

**原文标题**: Walmart Is Preparing to Welcome Its Next Customer: The AI Shopping Agent

**原文链接**: [https://www.wsj.com/articles/walmart-is-preparing-to-welcome-its-next-customer-the-ai-shopping-agent-6659ef18](https://www.wsj.com/articles/walmart-is-preparing-to-welcome-its-next-customer-the-ai-shopping-agent-6659ef18)

**“沃尔玛准备迎接下一位顾客：AI购物代理”概要 (基于标题推测的可能内容):**

文章可能讨论了沃尔玛为迎接人工智能购物代理（而非个人消费者）成为重要客户群体而做出的努力。沃尔玛预计，人工智能代理将越来越多地处理诸如自动补充食品杂货、比价购物和个性化产品推荐等任务。

为了迎合这些人工智能代理，沃尔玛可能正专注于以下几个关键领域：

*   **数据与API：** 通过强大的API（应用程序编程接口）提供结构化的、机器可读的产品数据，以便人工智能代理能够轻松访问和处理产品信息、定价、可用性和促销活动。

*   **算法优化：** 优化其算法，以准确响应人工智能代理的查询，确保数据格式正确，并防止潜在的系统滥用。

*   **大规模个性化：** 开发系统，以了解和迎合各个AI代理的独特偏好（代表着其人类用户的购买习惯），并提供量身定制的推荐。

*   **合作关系：** 与专注于人工智能和自动化技术的公司合作，将人工智能代理无缝集成到其生态系统中。

*   **供应链与物流：** 调整其供应链和物流基础设施，以应对人工智能代理驱动的潜在订单量增加和自动化采购模式。

文章可能强调了沃尔玛的潜在收益，例如增加销量、提高客户忠诚度以及降低运营成本。文章还可能讨论沃尔玛面临的挑战，包括需要强大的安全措施，确保人工智能代理之间的公平竞争，以及解决自动化可能导致的失业问题。

---

## 25. 到底什么是HDR？

**原文标题**: What is HDR, anyway?

**原文链接**: [https://www.lux.camera/what-is-hdr/](https://www.lux.camera/what-is-hdr/)

好的，根据标题“HDR到底是什么？”，文章很可能解释了高动态范围（HDR）技术，尤其是在显示和成像领域。以下是对文章可能涵盖内容的简要总结：

文章“HDR到底是什么？”可能将HDR定义为一种旨在生成具有比标准动态范围（SDR）图像更宽亮度范围（亮度与暗度）图像的技术。这会产生更逼真、更具视觉吸引力的画面，更接近人眼在现实世界中感知到的景象。

文章很可能解释说，HDR通过显示更亮的亮点、更深的黑色以及更广泛的颜色范围来实现这一点，从而提高对比度和细节。它可能会讨论HDR内容（电影、游戏等）和HDR显示器之间的区别，并强调两者都需要才能体验到完整的效果。

此外，文章可能会涉及不同的HDR标准，例如HDR10、HDR10+和杜比视界，重点介绍它们各自的功能以及动态元数据（逐场景优化画面）的差异。

最后，文章可能会简要提及HDR的优势，例如提高真实感、改善阴影和高光中的细节以及提供更身临其境的观看体验，但也可能会通过指出可见的改进取决于显示器的质量和源内容来缓和预期。

---

## 26. Python库根据使用情况动态生成代码

**原文标题**: Python lib generates its code on-the-fly based on usage

**原文链接**: [https://github.com/cofob/autogenlib](https://github.com/cofob/autogenlib)

AutoGenLib：一个使用 OpenAI API 动态生成代码的 Python 库。它无需预构建模块，而是在您导入 `autogenlib` 命名空间下不存在的模块或函数时创建它们。这实现了动态代码生成、上下文感知开发和无缝添加功能等特性。

该库通过分析导入语句的上下文，结合高级描述和现有代码上下文，向 OpenAI API 发送请求以生成所需的代码。然后，新生成的代码会被验证并执行，从而使导入的模块或函数可用。它强调完整的代码库上下文和调用者代码分析，以更好地保持一致性和理解需求。此外，自动异常处理会将错误发送给 LLM 以进行解释和修复。

AutoGenLib 通过 pip 安装，需要 Python 3.12+ 和 OpenAI API 密钥，后者可以设置为环境变量。它提供了诸如生成 TOTP 生成器和加密/哈希模块等示例。默认情况下，代码不被缓存，导致结果多样；可以使用 `init` 或 `set_caching` 函数启用缓存以保持一致性。

局限性包括需要互联网连接、依赖 OpenAI API 以及生成的代码可能存在质量问题。可以使用 `inspect.getsource()` 检查生成的代码。该库旨在用于原型设计和实验，需要在生产环境中使用之前进行手动审查。由于它是一个概念验证，因此不接受贡献。

---

## 27. ARB汇编着色器编程 (2023)

**原文标题**: ARB Assembly Shader Programming (2023)

**原文链接**: [https://mid.net.ua/posts/glarbasm.html](https://mid.net.ua/posts/glarbasm.html)

本文介绍了ARB汇编着色器编程，它是GLSL等现代着色器语言的前身。文章涵盖了其历史背景，解释了它从纹理组合演变而来，以及随着ARB_vertex_program和ARB_fragment_program的兴起。文章详细介绍了如何将ARB着色器集成到OpenGL应用程序中，包括生成和绑定程序、加载着色器源代码、设置参数（环境和局部参数）以及启用相应的管线阶段。

文章的核心在于ARB汇编语言本身。它描述了数据类型（PARAM、ATTRIB、ADDRESS、TEMP、ALIAS、OUTPUT）、指令语法（目标-源顺序，包含源修饰符和通道选择）以及常用指令（ABS、ADD、DP3等）。文章特别关注不太直观的指令，如DST、LIT和SWZ，解释了它们的目的和用法。

文章还重点介绍了顶点和片段程序特有的功能。顶点程序具有用于索引的ADDRESS变量、部分精度EXP和LOG指令，以及用于延迟顶点变换的OPTION ARB_position_invariant。片段程序获得了三角函数（SIN、COS、SCS）、带有相关纹理间接限制的纹理采样指令（TEX、TXP、TXB）、用于丢弃片段的KIL指令以及用于线性插值的LRP指令。总的来说，它提供了一个全面的，尽管可能不完整的，ARB汇编着色器编程指南。

---

## 28. 我从未对一项技术如此矛盾。

**原文标题**: I've never been so conflicted about a technology

**原文链接**: [https://marcjenkins.co.uk/conflicted-about-ai/](https://marcjenkins.co.uk/conflicted-about-ai/)

作者对人工智能，特别是大型语言模型（LLMs），表达了矛盾的情感。虽然承认像Cursor和GitHub Copilot这样的工具带来的生产力提升，但他们也强调了其显著的负面影响。

作者指出了人工智能对环境的巨大影响，引用了支持人工智能增长所需的数据中心的大量电力和水消耗，这些数据中心通常依赖化石燃料。他们还提出了关于人工智能模型训练方式的伦理问题，指出公司在未经许可或缺乏透明度的情况下从互联网上抓取数据，影响内容创作者并加重Web服务器的负担。

此外，这篇文章批判了“人工智能垃圾”的兴起，即人工智能生成的低质量、通用内容正在泛滥网络，取代原创作品。作者还涉及了人工智能“幻觉”问题，即大型语言模型产生不准确或捏造的信息，加剧了虚假信息的传播。

尽管人工智能具有实用性，但由于这些问题，作者在使用它时越来越感到不安。他们承认，由于害怕被落下或被取代，使用人工智能的压力越来越大，但最终质疑其收益是否大于损害，并得出结论，没有它，网络可能会更好。作者敦促用户在使用人工智能之前，注意其存在的问题。

---

## 29. 纽约拥堵费实施后的变化

**原文标题**: Changes since congestion pricing started in New York

**原文链接**: [https://www.nytimes.com/interactive/2025/05/11/upshot/congestion-pricing.html](https://www.nytimes.com/interactive/2025/05/11/upshot/congestion-pricing.html)

本文分析了2025年1月5日实施的纽约市拥堵费政策的直接影响，该政策对进入曼哈顿60街以南的车辆收取通行费。初步结果表明，该项目正在实现其减少拥堵和产生收入的目标。

拥堵区域内的交通量有所下降，每天进入的车辆减少约7.6万辆，导致交通速度加快，尤其是在高峰通勤时段。当地公交车和快车在区域内的行驶时间也更快。重要的是，拥堵区域外的区域，包括南布朗克斯和新泽西的通勤，交通状况并未恶化，反而有所改善。

包括公共汽车、地铁和通勤铁路在内的所有公共交通工具的乘客量都有所增加，表明人们正在减少驾车出行。黄色出租车在该区域内的行程也在增加。

此外，该项目似乎产生了积极的连锁反应。该区域内的交通事故和由此造成的伤害有所减少，停车违规和与车辆相关的噪音投诉也有所减少。消防部门的响应时间也略有提高。

虽然现在评估对污染和低收入通勤者的长期影响还为时过早，但初步数据显示，这些通勤者正在看到更快的出行时间。产生的收入有望在第一年达到5亿美元，用于资助150亿美元的交通升级。尽管存在持续的政治辩论和诉讼，但初步数据显示，拥堵收费正在带来积极的变化。

---

## 30. 揭秘Ruby (1/3): 线程是关键

**原文标题**: Demystifying Ruby (1/3): It's all about threads

**原文链接**: [https://blog.papey.fr/post/07-demystifying-ruby-01/](https://blog.papey.fr/post/07-demystifying-ruby-01/)

本文旨在揭秘Ruby中的并发与并行，通过解释进程、Ractor、线程和纤程的作用。

**进程：** 这些是由操作系统管理的独立实体，以并行方式运行，并具有隔离的内存。进程间通信需要管道或套接字等机制。

**Ractor：** Ractor在Ruby 3中引入，可在单个Ruby进程中提供并行性。每个Ractor就像一个具有隔离内存的微型虚拟机，通过消息传递进行通信，以避免共享内存问题。它们绕过了GIL对CPU密集型任务的限制。

**线程：** 在MRI Ruby中，线程由解释器管理，并受全局解释器锁（GIL）的约束，允许并发，但对于CPU密集型任务，不能实现真正的并行。它们是轻量级的，但共享内存，如果未正确同步，可能会导致竞争条件。线程对于I/O密集型任务非常有效。

**纤程：** 纤程是最轻量级的并发机制，提供协作式多任务处理，其中控制权在它们之间显式传递。它们也共享内存，最适合构建惰性生成器或协程。

本文强调，线程和纤程是底层接口，通常在Gem的底层使用。进程和Ractor提供真正的并行性，而线程和纤程在单个进程中提供并发性。作者最后以Puma与Unicorn应用服务器的争论为例，以轻松的语气总结，这归根结底是在线程或进程之间做出选择。

---

## 31. 大型语言模型在多轮对话中迷失方向

**原文标题**: LLMs get lost in multi-turn conversation

**原文链接**: [https://arxiv.org/abs/2505.06120](https://arxiv.org/abs/2505.06120)

大型语言模型在多轮对话中迷失方向

这篇arXiv文章“大型语言模型在多轮对话中迷失方向”探讨了大型语言模型(LLMs)在对话环境中的表现。作者Philippe Laban, Hiroaki Hayashi, Yingbo Zhou和Jennifer Neville发现，与单轮、完全指定的指令相比，LLMs在多轮对话中表现出显著降低的性能。具体来说，在六项生成任务中，平均性能下降了39%。

该研究使用了涉及超过20万次模拟对话的大规模模拟实验来分析这种性能下降。作者将性能下降分解为两个部分：能力上的轻微损失和可靠性的大幅增加。他们观察到，LLMs经常在对话早期做出假设，并过早地尝试生成最终解决方案，然后过度依赖这些解决方案。

论文中强调的核心发现是，LLMs难以从对话过程中做出的错误假设或“错误的转弯”中恢复。这表明LLMs在维持上下文、适应变化的信息以及在多轮交流中纠正方向的能力方面存在弱点。该研究强调需要改进评估方法，超越单轮评估，并考虑与LLMs进行的真实世界对话交互的复杂性。该论文与计算与语言(cs.CL)和人机交互(cs.HC)领域的研究人员相关。

---

## 32. Show HN: Muscle-Mem，AI智能体的行为缓存

**原文标题**: Show HN: Muscle-Mem, a behavior cache for AI agents

**原文链接**: [https://github.com/pig-dot-dev/muscle-mem](https://github.com/pig-dot-dev/muscle-mem)

Muscle-Mem是一个Python SDK，旨在通过缓存和重放工具调用模式来优化AI代理，从而有效地为重复性任务创建“肌肉记忆”。 这种方法旨在减少LLM的使用，从而提高速度，降低成本并减少可变性。

其核心概念围绕着缓存代理行为并在再次遇到相同任务时确定性地重放它们。 如果环境发生显著变化，系统将回退到代理的正常操作。 Muscle-Mem本身不是代理框架，而是一种与现有代理实现集成的工具。

安全重用工具的关键在于缓存验证，这通过“检查”来实现。 每个检查都包含一个 `capture` 回调以提取环境特征，以及一个 `compare` 回调以确定当前环境是否与缓存的环境匹配。 检查可以用作工具调用的 `pre_check` 或 `post_check`。

API包含一个 `Engine` 类，它包装代理并管理缓存。 `@engine.tool` 装饰器会检测工具以记录它们的调用和关联的参数。 这篇文章提供了一个使用“hello”函数的实际示例，演示了如何使用检查来实现基于时间戳的缓存验证过期。

作者鼓励反馈和贡献，邀请用户加入 Muscle Mem Discord，测试存储库并提供反馈。

---

## 33. Git Bug: 分布式、离线优先的 Git 内嵌式缺陷跟踪器，带桥接功能

**原文标题**: Git Bug: Distributed, Offline-First Bug Tracker Embedded in Git, with Bridges

**原文链接**: [https://github.com/git-bug/git-bug](https://github.com/git-bug/git-bug)

Git-bug：去中心化、离线优先的问题跟踪器，将问题数据作为对象（而非文件）直接嵌入到 Git 仓库中。这实现了对问题、评论和用户信息进行版本控制、分发以及离线访问。

主要功能包括：

*   **原生 Git 存储：** 所有问题数据都存储在 Git 仓库中，保持版本控制。
*   **分布式与版本化：** 利用 Git 的架构进行离线工作和无缝同步。
*   **闪电般的速度：** 提供快速的问题列表和搜索功能。
*   **第三方桥接：** 支持与 GitHub 和 GitLab 等平台的同步。
*   **灵活的界面：** 提供 CLI、TUI 和 Web 浏览器界面。
*   **轻松集成：** 旨在实现简易的设置和最小的集成工作量。

该项目鼓励用户安装、探索文档、为开发做贡献，并通过 Matrix 和讨论与社区联系。它还感谢赞助者和捐助者的贡献，以及项目最初创建者 Michael Muré 的辛勤工作。该项目采用 GPLv3 或更高版本许可，徽标采用 CC BY 4.0 许可。

---

## 34. 展示HN：语义计算器（国王-男人+女人=？）

**原文标题**: Show HN: Semantic Calculator (king-man+woman=?)

**原文链接**: [https://calc.datova.ai](https://calc.datova.ai)

这个“Show HN”帖子介绍“语义计算器 | Datova”，一个尝试对词语进行算术运算的工具，它利用语义关系。它不是进行字面上的数学运算，而是将词语解释为语义空间中的向量，并进行向量加减来寻找类比关系。例如，标题“国王-男人+女人=？”暗示该工具旨在找到最能完成类比“国王之于男人，犹如x之于女人”的词语——理想情况下，答案会是“王后”。

其核心思想是使用词嵌入（例如word2vec或GloVe），这些词嵌入捕捉了词语的语义含义以及它们彼此之间的关系。通过将词语表示为向量，该工具可以对这些向量执行数学运算，有望产生与所需的类比解决方案相对应的向量。

该帖子是一个“Show HN”，表明创建者正在寻求反馈并将他们的项目展示给Hacker News社区。稀疏的信息意味着用户需要访问提供的链接（Datova）来与计算器互动并探索其功能。该项目旨在提供一种通过数学运算与语言进行交互的更直观和更像人的方式。计算器的成功取决于底层词嵌入的质量和向量算术的鲁棒性。

---

## 35. 忘记IP：使用密码学验证机器人和代理流量

**原文标题**: Forget IPs: using cryptography to verify bot and agent traffic

**原文链接**: [https://blog.cloudflare.com/web-bot-auth/](https://blog.cloudflare.com/web-bot-auth/)

本文探讨了验证机器人和代理流量的挑战，由于人工智能代理的兴起以及用户代理标头和IP地址范围等传统方法的不足，验证工作变得越来越复杂。 Cloudflare提出了两种加密解决方案：HTTP消息签名和请求mTLS，为合法机器人提供了一种更可靠的身份验证方式。

HTTP消息签名是一种已定义的标准，允许机器人使用源服务器已知的公钥对请求进行加密签名。 此签名包括有效窗口、密钥ID（JSON Web Key Thumbprint）以及指示签名用途的标签。 Cloudflare与OpenAI等行业合作伙伴合作，后者已经在使用这种方法。 文中提供了 Chrome 扩展程序中的示例代码。

请求mTLS利用TLS标志来指示客户端支持通过客户端证书进行身份验证。 本文介绍了"req mTLS"标志，该标志由客户端在连接建立期间发送，允许服务器仅从支持mTLS的客户端请求证书，而不会中断常规用户流量。 本文包含如何使用实验性Go代码实现和测试req mTLS的示例。

这两种方法都旨在为代理和机器人提供一种标准化的公开身份验证方式，使网站托管平台能够准确识别它们并根据验证后的身份管理流量。 Cloudflare正在运行一个封闭测试版来测试这些提案。

---

## 36. 一个不该存在的服务器

**原文标题**: A server that wasn't meant to exist

**原文链接**: [https://it-notes.dragas.net/2025/05/13/the_server_that_wasnt_meant_to_exist/](https://it-notes.dragas.net/2025/05/13/the_server_that_wasnt_meant_to_exist/)

网络工程师讲述了一段充满挑战的经历，他在公司老板突然去世后帮助一家家族企业。由于缺乏数字化基础设施，这家公司难以经营，并因财务管理不善而面临破产的风险。该工程师安装了一台带有VMs的NetBSD服务器，以集中数据、提高效率并增加透明度。这遭到了已故老板的得力助手的抵制，此人似乎正从缺乏监督中获利。

此人试图通过要求获得管理员权限并威胁要擦除服务器来破坏新系统。最终，当工程师透露了个人关系时，他退缩了。然而，服务器后来被人为破坏。幸运的是，工程师已经实施了一个秘密备份系统，为这家公司提供了关键数据。

随后，这家公司为工程师提供了一个利润丰厚的职位，负责管理他们的基础设施和彻底改革流程。工程师拒绝了，因为他意识到这家公司不愿直面根本问题，也无意保护自己免受那些剥削他们的人的侵害。工程师意识到，有些情况已经腐烂到无法修复的地步，尤其是当负责人非但不解决问题，反而助长问题时。这个故事强调了诚信胜于利润的重要性，并理解并非所有问题都能解决，无论技术多么精湛。

---

## 37. 轻量级开源 reCaptcha 替代方案

**原文标题**: Lightweight open source reCaptcha alternative

**原文链接**: [https://github.com/altcha-org/altcha](https://github.com/altcha-org/altcha)

ALTCHA：轻量级、开源的 reCAPTCHA 替代方案
ALTCHA 是一种轻量级的开源替代方案，用于替代 reCAPTCHA，它使用工作量证明 (PoW) 机制保护网站、API 和在线服务免受垃圾邮件和滥用。与传统的 CAPTCHA 不同，ALTCHA 优先考虑用户隐私，采用无 Cookie 设计、自托管和 GDPR 合规性。它还符合 WCAG 2.2 AA 级标准和《欧洲可访问性法案》。

ALTCHA 提供流畅的用户体验，利用 PoW 而非视觉谜题。它体积轻巧（gzip 压缩后 17kB），确保页面快速加载。 同时提供自托管和 SaaS 选项。

ALTCHA 小部件以 Web Component 的形式分发，并与各种框架（React、Vue 等）和服务器端语言（TypeScript、PHP、Go、Python 等）集成。它需要通过 `<altcha-widget>` 标签进行配置，指定挑战 URL 或 JSON 编码的挑战。

配置选项允许自定义行为，包括自动验证、人为延迟、UI 外观和垃圾邮件过滤器设置。插件通过分析、数据混淆和文件上传等功能增强了功能。

ALTCHA 提供了一个垃圾邮件过滤器 API，用于分析表单数据以检测垃圾邮件特征。它可以配置为阻止特定国家/地区、强制执行分类器、禁用规则以及检查电子邮件、IP 地址和时区等字段。

本文还讨论了内容安全策略的注意事项、编程配置、自定义提取函数、事件和贡献指南。

---

## 38. 明显错误

**原文标题**: Clearly Incorrect

**原文链接**: [https://quarter--mile.com/Clearly-Incorrect](https://quarter--mile.com/Clearly-Incorrect)

鉴于提供的极其有限的内容：

一篇题为“明显错误”的文章，似乎是某个以写作为主题的博客或网站的一部分。它为读者提供了订阅或联系作者/组织的选择。星号分隔符的存在表明内容可能已经结束或正在过渡到新的部分。

由于没有实际的文章内容，因此无法总结任何具体的论点、数据或叙述。此摘要反映了页面上*存在*的信息，而不是对论点或主题的总结。它完全基于标题和导航元素。我们可以推断它是一篇书面作品，因为它被标记为“写作”。

---

## 39. Databricks 收购 Neon

**原文标题**: Databricks acquires Neon

**原文链接**: [https://www.databricks.com/blog/databricks-neon](https://www.databricks.com/blog/databricks-neon)

Databricks 收购了以开发者为先的 Serverless Postgres 公司 Neon，旨在为开发者和 AI 代理构建开放的 Serverless 数据库基础。Neon 的架构分离了存储和计算，实现了速度、弹性伸缩和数据库的即时分支/派生。

Neon 的创始人，经验丰富的数据库专家和 Postgres 贡献者，创建 Neon 是为了解决传统数据库在现代开发中的局限性。他们观察到 AI 代理越来越多地使用 Neon，创建数据库的速度是人类的四倍。开源 Postgres 生态系统、速度、弹性伸缩/定价以及分支/派生功能使 Neon 非常适合 AI 代理工作流程。

Databricks 和 Neon 都致力于开源和构建核心技术创新。Databricks 计划整合 Neon 的技术，以颠覆由旧技术主导的 1000 亿美元 OLTP 数据库市场。现有的 Neon 客户和合作伙伴将获得持续的支持和创新。更多细节将在六月即将举行的 Data + AI Summit 上分享。

---

## 40. 行进 Forth： Forth 内核编写系列

**原文标题**: Moving Forth: a series on writing Forth kernels

**原文链接**: [https://www.bradrodriguez.com/papers/index.html](https://www.bradrodriguez.com/papers/index.html)

本页面收录了Bradford J. Rodriguez的出版物、演示文稿和计算机程序。其中心主题是Forth编程语言及其应用，尤其是在嵌入式系统和控制领域。

“Moving Forth”系列详细介绍了Forth内核的设计与实现，涵盖设计决策、基准测试、`DOES>`构造、汇编与元编译，以及Z80、8051和6809处理器上的特定实现等主题。

其他主要部分包括一个关于多6809系统多处理的系列文章、Rodriguez关于控制串列加速器的嵌入式时间专家系统的博士论文，以及他关于模式匹配语言PatternForth的硕士论文。

该页面还列出了关于Forth多任务处理、串行I/O、MIDI控制器、面向对象的Forth以及Forth系统硬件实现等方面的其他论文。

几个计算机程序，特别是各种处理器（6809、8051、Z80、8086）的CamelForth实现，可供下载。该页面包括联系方式和CamelForth及T-Recursive Technology等相关项目的链接。

---

## 41. 通行密钥背后的密码学

**原文标题**: The cryptography behind passkeys

**原文链接**: [https://blog.trailofbits.com/2025/05/14/the-cryptography-behind-passkeys/](https://blog.trailofbits.com/2025/05/14/the-cryptography-behind-passkeys/)

本文深入探讨了通行密钥背后的密码学原理，重点介绍了与传统密码相比，通行密钥如何提供更安全的身份验证方法。通行密钥利用密钥对生成数字签名，网站存储公钥和标识符，而私钥验证用户身份，无需传输敏感信息。

本文强调了WebAuthn规范在增强基本密码学之外的安全性方面的作用。WebAuthn增加了源绑定，确保通行密钥仅用于为其创建的网站，从而打击网络钓鱼。它还强制要求请求使用HTTPS。

文章讨论了两种主要的身份验证器类型：平台身份验证器（集成到设备中，提供便利性和云备份）和漫游身份验证器（YubiKeys等硬件设备，提供更高的安全隔离）。

虽然通行密钥可以缓解网络钓鱼和密码重用问题，但它们并非完美的解决方案。本文概述了潜在的攻击途径，包括基于浏览器的攻击、受损的身份验证器和凭据ID冲突。网站应拒绝具有重复凭据ID的注册尝试。

最后，本文探讨了WebAuthn扩展，例如`prf`和`largeBlob`，它们支持HMAC-SHA-256计算以及在身份验证器中安全存储证书或加密密钥等数据。但是，文章警告说，由于基于JavaScript的系统容易受到恶意服务器的攻击，因此不应使用Web密码学进行真正的端到端加密。

---

## 42. 美国国家航空航天局斯坦尼斯航天中心发布首个开源软件

**原文标题**: NASA Stennis Releases First Open-Source Software

**原文链接**: [https://www.nasa.gov/centers-and-facilities/stennis/stennis-first-open-source-software/](https://www.nasa.gov/centers-and-facilities/stennis/stennis-first-open-source-software/)

NASA斯坦尼斯航天中心发布首个开源软件，该对等审查工具旨在提高软件应用开发的效率和效力，尤其适用于火箭推进测试系统。该工具源于用于开发美国宇航局数据采集系统（NDAS）的内部流程，该系统用于监测和分析这些测试的数据。

该对等审查工具简化了协作审查流程，使开发人员能够通过更早地识别和解决问题来构建更好的软件应用程序。它特别适用于National Instruments LabVIEW，一种图形编程语言，在这种语言中，代码比较比基于文本的语言更具挑战性。该工具可自动执行步骤，促进包含图片和其他元素的在线评论，并通过提供专注的环境来优化审查人员的时间。

NASA斯坦尼斯希望开源该工具能够培养一个用户社区，进一步完善和改进它。目标是通过强大的对等审查来创建更强大的软件。文章还强调了NASA斯坦尼斯工程师为能够为开源社区做出贡献而感到的兴奋和自豪，以及对持续贡献的期望。该工具可在NASA GitHub上找到。

---

## 43. Go语言自托管Webhook测试器

**原文标题**: Self-hostable webhook tester in go

**原文链接**: [https://testwebhook.xyz](https://testwebhook.xyz)

本文介绍一款面向开发者的可自托管的Webhook测试工具。它是一个轻量级平台，使开发者能够创建临时的Webhook端点，以实时检查和调试HTTP请求。无论集成何种服务（Stripe、GitHub、Twilio或自定义），该工具都提供对HTTP请求的完全可见性。

主要功能包括捕获标头、查询参数和请求正文，而无需后端代码，从而允许自定义响应、模拟延迟以及将请求重放到个人服务器。

该工具的工作原理是在创建Webhook时生成一个唯一的URL。发送到此URL的任何HTTP请求都将被记录并显示在仪表板中。用户随后可以检查标头、正文、方法和其他请求详细信息，并根据需要重放或转发该请求。

文章还提到，虽然传入的Webhook数据是临时存储的，但创建一个免费帐户可以启用请求日志保留和高级功能，如重放功能。文章还提供了一个curl示例，演示了如何使用JSON有效负载向生成的Webhook URL发送POST请求。

---

## 44. 我的工程技艺退步了

**原文标题**: My Engineering Craft Regressed

**原文链接**: [https://lemmy.ml/post/30100312](https://lemmy.ml/post/30100312)

OsrsNeedsF2P 在 dginovker 博客上发表的题为《我的工程技能退步了》的文章，暗示了作者对自身工程技能或能力下降的个人反思。“arrow-up17”和“arrow-down10”表明该文章受到正面欢迎（17 个赞）和一些异议（10 个踩）。 还有消息、链接帖子和“file-text”功能的指示，可能表明存在与该主题相关的讨论、相关资源和可下载文档。“edit-21 天前”表明该帖子是 21 天前编辑的。 在没有完整文章的情况下，不可能知道退步的具体细节，但核心信息是作者对自身工程能力下降的自我评估，该文章已在线发布并收到褒贬不一的反馈。

---

## 45. 临界点：美国小费制度如何失控

**原文标题**: Tipping Point: How America's Gratuity System Got Out of Hand

**原文链接**: [https://www.scrapstostacks.com/post/tipping-point-how-america-s-gratuity-system-got-out-of-hand](https://www.scrapstostacks.com/post/tipping-point-how-america-s-gratuity-system-got-out-of-hand)

本文认为美国的打赏制度已经失控，需要认真反思。它追溯了该制度在南北战争后美国的起源，强调最初它是如何被用来剥削黑人劳工的，雇主可以通过支付低于标准的工资，并依靠小费来弥补差额。这种剥削行为已经演变成一种根深蒂固的规范，现在在各种情况下都期望给小费，包括自助服务亭和自动结账机。

本文强调，小费已经从自愿的“感谢”变成了强制性的期望，公司利用这一点来支付低于标准的工资，同时将道德负担转移给顾客。靠小费为生的工人合法地可以获得低至每小时 2.13 美元的工资，这造成了经济上的不稳定，并依赖于顾客的慷慨。相比之下，欧洲提供了一种不同的模式，工人可以获得维持生计的工资，消除了过度打赏的必要，并营造了更专业的服务环境。

文章断言，问题的根源在于企业的贪婪。通过依靠小费来补充工资，企业可以节省数十亿美元的劳动力成本、税收和医疗保健福利。文章建议的解决方案不是完全停止打赏，而是推动系统性变革：提高联邦最低工资，取消小费工资制度，支持支付维持生计工资的企业，并揭露服务前打赏提示的荒谬性。它还鼓励工会化和创办公平补偿员工而不依赖小费的企业。最终，目标是重建一个人们获得公平报酬的制度，打赏成为基于卓越服务的选择，而不是生存的必需品。

---

## 46. 如何打造智能手表：芯片选择

**原文标题**: How to Build a Smartwatch: Picking a Chip

**原文链接**: [https://ericmigi.com/blog/how-to-build-a-smartwatch-picking-a-chip/](https://ericmigi.com/blog/how-to-build-a-smartwatch-picking-a-chip/)

本文详细介绍了为新款智能手表“Core Time 2”项目选择微控制器芯片的过程。作者强调，选择合适的芯片至关重要，因为它会影响软件兼容性、功耗和成本。他分享了过去为 Pebble 手表选择芯片的经验，强调了软件兼容性的重要性以及使用熟悉芯片的好处。

对于 Core Time 2，最初坚持使用 Nordic 的 nRF52840（用于 Core 2 Duo）的计划被重新考虑，原因是 Nordic 较新的低端芯片存在局限性。作者探索了来自 Apollo、BES 和 Dialog 的替代方案，但难以找到带有开源 SDK 的选项，而这对于 PebbleOS 来说至关重要。

最终，选择了 SiFli 的 SF32LB52J 芯片。这款芯片具有以下几个优点：充足的 RAM（512K SRAM，16M PSRAM），一个用于手表显示的专用 MIP 外设，低功耗，具有竞争力的价格（低于 2 美元），最重要的是，一个支持移植 PebbleOS 的开源 SDK。作者强调了 SiFli 在为众多现有智能手表提供动力方面的经验，以及 CEO 对支持开源开发的热情。此选择避免了对 FPGA 或昂贵显示接口芯片的需求，从而简化了硬件设计。

---

## 47. 干涉仪设备一英里外识字

**原文标题**: Interferometer Device Sees Text from a Mile Away

**原文链接**: [https://physics.aps.org/articles/v18/99](https://physics.aps.org/articles/v18/99)

该物理杂志文章讨论了一种新的高分辨率成像系统，该系统利用强度干涉法捕获远处物体的图像。该系统由中国科学技术大学张强领导的研究人员开发，采用多束激光照射目标，并用两台望远镜收集反射光。这使得能够在1.36公里的距离上对毫米宽的字母进行成像，与使用单台望远镜相比，空间分辨率有了显著提高。

这项创新的核心在于解决了相干激光带来的挑战，相干激光通常会导致强度波动，而强度波动又被散粒噪声所主导。该团队通过将激光分成八束光束来解决这个问题，每束光束穿过大气层的路径略有不同，从而产生非相干照明，使得可以观察到干涉效应。

该系统通过创建反射字母目标并通过改变望远镜之间的间距和旋转目标来重建它们的图像进行了测试。这证明了3毫米的分辨率，远远超过了单台望远镜的42毫米分辨率。

研究人员计划通过改进激光光控制并将深度学习集成到图像重建软件中来增强该技术。潜在的应用包括空间碎片探测。Shaurya Aarav和Ilya Starshynov等专家赞扬了这一进步，强调了其在远程成像应用（如监测昆虫种群）以及巧妙地将非相干光传递到目标的方法方面的潜力。

---

## 48. 展示HN：Kudos.wiki – 在维基百科上发现最佳电影

**原文标题**: Show HN: Kudos.wiki – Discover the best movies on Wikipedia

**原文链接**: [https://kudos.wiki](https://kudos.wiki)

作者创建了Kudos.wiki，一个通过维基百科文章中提及来发现广受好评电影的平台。作者对传统的电影推荐算法，甚至是烂番茄、Metacritic和Letterboxd上的精选列表感到失望，注意到自己真正喜欢的电影总是在维基百科文章中明确说明受到好评。这促使他们使用Python脚本抓取了整个英文维基百科档案（150GB），从中识别出1910年代至今来自83个国家、涵盖19种类型的1700多部广受好评的电影。一个关键亮点是该平台能够挖掘出传统推荐来源常常忽略的鲜为人知的电影。本质上，Kudos.wiki提供了一种独特且可能更可靠的方式，基于维基百科的验证信息来发现优质电影。

---

## 49. 我们叙事牢笼

**原文标题**: Our narrative prison

**原文链接**: [https://aeon.co/essays/why-does-every-film-and-tv-series-seem-to-have-the-same-plot](https://aeon.co/essays/why-does-every-film-and-tv-series-seem-to-have-the-same-plot)

艾莉安·格拉泽的《我们的叙事牢笼》探讨了“英雄之旅”情节结构在现代电影、电视和文学作品中的普遍存在。她认为，尽管存在多样性的假象，但一种重复的模式占据主导地位：一个平凡世界中的主人公面临一个诱发事件，开始一段旅程，遭遇阻碍，经历低谷，最终经历一次变革性的体验，带着改变回到家园。

格拉泽将这种结构追溯到亚里士多德的《诗学》，以及弗雷塔格等思想家随后的发展，以及沃格勒和麦基等编剧大师的现代改编。她认为，好莱坞之所以延续这种模式，是因为它被认为可以复制以取得票房成功，将传统伪装成多样性，将约束伪装成自由，反映了在有限框架内消费者选择的幻觉。

作者质疑这种叙事主导地位的影响。她认为，虽然英雄之旅反映了根深蒂固的人类需求，但其公式化的应用可能具有微妙的保守性，优先考虑在资产阶级规范范围内个人的转变，而不是对社会结构的真正批判。

格拉泽引用了荣格的“集体无意识”和坎贝尔的“单一神话”作为潜在的影响，区分了真实的人类境况和偏爱救赎和恢复常态的好莱坞改编。她指出叙事塑造公众舆论的力量，引用了李普曼呼吁好莱坞控制大众以及萨尔蒙观察到叙事在各种文化和社会领域传播的现象。最后，她认为，虽然故事提供了愿望的满足和秩序感，但将叙事结构强加于生活可能是一种避免积极主动改变的方式，“英雄之旅”可能是一种体验改变的虚幻方式，而不是实际行动。

---

## 50. 未认证请求的更新速率限制

**原文标题**: Updated rate limits for unauthenticated requests

**原文链接**: [https://github.blog/changelog/2025-05-08-updated-rate-limits-for-unauthenticated-requests/](https://github.blog/changelog/2025-05-08-updated-rate-limits-for-unauthenticated-requests/)

GitHub正在更新未认证请求的速率限制，以应对其API上日益增长的爬取活动。 这将影响诸如通过HTTPS克隆存储库、匿名使用REST API以及从raw.githubusercontent.com下载文件等操作。

此举旨在保护平台并为开发者维护稳定的环境。 依赖未认证访问的用户可能会受到这些新限制的影响。

GitHub鼓励开发者使用已认证请求，这将继续享有更高的速率限制和不间断的访问，从而确保在访问GitHub服务时具有更高的稳定性和可靠性。 本质上，身份验证是实现一致和高流量使用的推荐方法。

---

## 51. 网络拼字游戏俱乐部 (2002-)

**原文标题**: Internet Scrabble Club (2002-)

**原文链接**: [https://isc.ro/](https://isc.ro/)

网络拼字游戏俱乐部 (ISC) 是一个用户可以玩拼字游戏的在线平台。该网站拥有庞大的用户群，随时都有数千名玩家登录，数百场比赛正在进行中。它提供免费的拼字游戏体验，没有广告或下载，允许用户与朋友、全球对手或电脑 AI 对战。玩家还可以分析过去的比赛或观看正在进行的比赛。ISC 使用官方词典进行单词验证。该平台可在 iOS 和 Android 设备以及台式电脑上访问。网站提供联系方式以及帮助和隐私政策的链接。免责声明澄清了 SCRABBLE 一词的商标所有权。

---

## 52. 如何教孩子了解数字隐私的重要性

**原文标题**: How to Teach Kids the Importance of Digital Privacy

**原文链接**: [https://time.com/7282041/teach-kids-digital-privacy/](https://time.com/7282041/teach-kids-digital-privacy/)

本文强调，在一个充斥着人工智能深度伪造、身份盗窃和晒娃等不断演变的在线威胁的世界中，迫切需要对儿童进行数字隐私教育。文章认为，关于数字隐私的讨论现在至关重要，类似于前几代人关于敏感话题的“谈话”，因为儿童的未来越来越与他们的在线数据息息相关。

文章建议家长采取切实可行的步骤，包括遮盖网络摄像头、使用具有定制隐私控制的设备、审查社交媒体设置以及设置Google Alerts来监控孩子的在线活动。文章强烈建议父母注意“晒娃”，限制公开分享孩子的照片和信息。

文章还强调了公开讨论隐私的重要性，培养一种伙伴关系，让孩子们了解其数字足迹的价值，并有权控制自己的在线声誉。文章建议玩OSINT游戏，以说明在线个人信息可以多么容易地被拼凑起来。文章鼓励制定“家庭媒体使用计划”，以培养持久的隐私意识。

最终，文章强调需要教导孩子们有意识且周到地在线分享、尊重他人隐私，并在怀疑发生隐私泄露时立即发声。文章建议家长了解可用的法律保护措施，特别是《儿童在线隐私保护法》（COPPA）对13岁以下儿童的保护，并在权利受到侵犯时联系他们所在州的司法部长办公室。文章的主旨是，认真对待数字隐私并树立良好榜样对于儿童的福祉至关重要。

---

## 53. 多租户经济学原理

**原文标题**: How the economics of multitenancy work

**原文链接**: [https://www.blacksmith.sh/blog/the-economics-of-operating-a-ci-cloud](https://www.blacksmith.sh/blog/the-economics-of-operating-a-ci-cloud)

此页面是一个由Aditya Jayaprakash撰写，于2025年5月13日发表的名为“多租户经济学如何运作”的文章。它出现在提供CI/CD解决方案的Blacksmith Software Inc.公司的博客上。

本文本身并未在此页面摘录中直接显示。相反，该页面主要充当Blacksmith的公告板和导航中心。 它包括诸如Blacksmith在GV和Y Combinator的带领下筹集了350万美元种子资金的公告，以及有关即将到来的DockerHub速率限制的警告。 它还重点介绍了最近的博客文章/指南，包括“在GitHub Actions中管理密钥的最佳实践”、“如何减少在GitHub Actions中的支出”和“使用GitHub Actions的矩阵构建”。

该页面的主要功能是推动用户参与Blacksmith的内容和服务。 它提供指向文档、博客、指南、定价信息、职业机会、联系信息和系统状态的链接。 重复的行动号召，如“免费开始使用”和“预约演示”，突显了该网站获取和支持客户的目标。 内容表明Blacksmith专注于提供高性能和高效的CI/CD解决方案，特别是对于GitHub Actions的用户。

---

## 54. 英国古树名录

**原文标题**: UK's Ancient Tree Inventory

**原文链接**: [https://ati.woodlandtrust.org.uk/](https://ati.woodlandtrust.org.uk/)

英国古树名录项目致力于绘制和保护英国最古老和最重要的树木。该网站强调，英国拥有的古树数量比许多其他欧洲国家都多。该名录依靠公众参与来识别和记录这些树木，目前已登记超过19万棵，但仍有更多有待发现。

该网站鼓励用户使用地图通过“添加树木”和“树木搜索”来探索英国的古树遗产，并查看他们添加的任何树木。它还提供关于名录记录的内容及其背后原因的信息，解释了如何识别古树以及为何将其纳入名录至关重要。网站提供一系列视频，进一步教育用户如何识别和记录这些树木，以便将其纳入名录。最后，一篇精选的博客文章深入探讨了参与该项目的个人所具有的热情和灵感，展示了古树的价值以及保护它们的重要性。

---

## 55. 展示一下：我做了一个物联网设备，让我的家人知道我是否在开会

**原文标题**: Show HN: I’ve built an IoT device to let my family know when I’m in a meeting

**原文链接**: [https://nullonerror.org/2025/05/11/i-have-built-an-iot-device-to-let-my-family-know-when-i-am-in-a-meeting/](https://nullonerror.org/2025/05/11/i-have-built-an-iot-device-to-let-my-family-know-when-i-am-in-a-meeting/)

这个 "Show HN" 帖子介绍了 Tabajara，作者为了在家工作时用视觉信号告知家人自己正在开会而制作的物联网设备。该设备通过摄像头使用情况触发，点亮红色或蓝色 LED 面板。

该设备围绕着一个运行 Arduino 框架的 ESP32 微控制器构建，该微控制器连接到家庭 Wi-Fi 网络并暴露一个 HTTP 服务器。该服务器监听 `/camera` 端点上的 PATCH 请求，接收指示摄像头是“开”还是“关”的 JSON 有效载荷，然后激活相应的 LED 颜色。

为了方便访问设备而无需跟踪其 IP 地址，作者利用 mDNS（Apple 设备上的 Bonjour）为 ESP32 分配了一个 `.local` 主机名。

该系统由一个 Python 守护程序完成，该程序定期查询 Apple API 以确定当前是否有任何摄像头处于活动状态。基于此状态，守护程序向 ESP32 发送 PATCH 请求，从而相应地更新 LED 面板。作者提供了一个 YouTube 链接来观看设备运行情况，以及一个 GitHub 链接来访问源代码。该解决方案被描述为简单但有效，可以防止会议期间被打断。

---

## 56. Ash Framework – 模型化你的领域，导出其余

**原文标题**: Ash Framework – Model your domain, derive the rest

**原文链接**: [https://ash-hq.org/](https://ash-hq.org/)

Ash框架：为开发者效率而生的Elixir后端框架

Ash框架是一个为开发者效率而设计的Elixir后端框架。它提倡“模型化你的领域，推导出其余部分”的理念，强调使用声明式工具来避免重复性任务。Ash与Phoenix LiveView集成以构建Web应用程序，并支持各种前端的快速API开发。

该框架提供安装程序和项目预设，包括Phoenix LiveView、GraphQL、JSON:API和PostgreSQL等选项。除了基础功能外，Ash还支持各种数据层（SQLite、CSV）、认证方法（密码、魔法链接、API密钥、OAuth2），并与AI工具（Tidewave、Ash AI）集成。它还为金融（货币、复式记账）、自动化（后台作业、状态机、事件溯源）、安全&安保（归档、操作日志、加密）、管理&调试（管理UI、实时调试器）和UI组件提供功能。可观测性集成包括AppSignal，并计划支持OpenTelemetry。

该页面强调了安装的简易性，并鼓励用户从预设开始，特别是推荐PostgreSQL。它提供了使用Phoenix LiveView、GraphQL和JSON:API的示例。此外，它还宣传了即将在ElixirConf EU和GOATMIRE举行的演讲，演讲者包括Ash核心团队成员。

---

## 57. 迁移到Postgres

**原文标题**: Migrating to Postgres

**原文链接**: [https://engineering.usemotion.com/migrating-to-postgres-3c93dff9c65d](https://engineering.usemotion.com/migrating-to-postgres-3c93dff9c65d)

由于成本飙升（增长5倍至六位数中段）和性能问题，Motion已从CockroachDB迁移到Postgres。虽然CockroachDB提供了横向扩展和高可用性等优势，但鉴于Motion的单区域设置和简单的事务查询，这些优势并未得到充分利用。

此次迁移由以下几个因素驱动：CockroachDB上频繁的Prisma迁移超时、由于Airbyte连接器问题导致的ETL作业失败，以及查询性能不一致，即复杂查询比Postgres慢得多。CockroachDB中的UI/UX问题，如令人困惑的未使用索引报告和繁琐的查询取消，也促成了这一决定。支持响应速度也是一个问题。

该迁移使用Bun构建的自定义ETL解决方案执行。该过程包括将CockroachDB数据转储到文件，将数据转换为与Postgres兼容的格式，并将数据流式传输到Postgres。迁移本身仅花费15分钟，总停机时间不到一小时。

迁移后，Motion的总请求延迟降低了33%，并使用PGAnalyze等Postgres工具识别了几个未优化的查询。即使采用保守的资源配置，此次迁移也带来了每年超过11万美元的成本节约。作者强调了这项工作的高影响力，并鼓励有兴趣的人士考虑加入Motion团队。

---

## 58. 黑格尔2.0：三元计算的虚构历史 (2018)

**原文标题**: Hegel 2.0: The imaginary history of ternary computing (2018)

**原文链接**: [https://www.cabinetmagazine.org/issues/65/weatherby.php](https://www.cabinetmagazine.org/issues/65/weatherby.php)

莱夫·韦瑟比的《黑格尔2.0：三进制计算的虚构史》通过控制论、德国唯心主义和冷战历史的视角，探讨了三进制计算（使用三进制位而非二进制位）在很大程度上未被实现的潜力。 文章以尼古拉·布鲁森佐夫的SETUN为中心，这是唯一一台基于三进制逻辑构建的计算机，但由于官僚主义障碍和标准化努力，它最终未能获得发展。

该文将现代计算机所基于的二进制逻辑与更细致、更具黑格尔式的“黑格尔2.0”三进制系统的潜力进行了对比。 它深入探讨了冷战时期的哲学辩论，特别是苏联马克思列宁主义与美国控制论之间的冲突，突出了沃伦·麦卡洛克对当时盛行的二元论思维的拒绝。 麦卡洛克没有去莫斯科参观SETUN，而是进行了哲学上的否定，认为有一种超越二元论的黑格尔式后人类主义。

韦瑟比认为，三进制计算的历史在很大程度上是虚构的，更多地是作为仿真存在，而不是实现。 尽管它具有技术前景，但它从未克服硬件开发的局限性。 文章最后提出，三进制计算未被实现的潜力，以及像哥塔德·君特试图综合黑格尔和控制论的努力，提供了一个视角，可以从中批判我们当前二进制驱动的数字文化中固有的局限性和错觉。

---

## 59. 在美国，旋转爆震火箭发动机成功试飞

**原文标题**: In the US, a rotating detonation rocket engine takes flight

**原文链接**: [https://arstechnica.com/space/2025/05/venus-aerospace-flies-its-rotating-detonation-rocket-engine-for-the-first-time/](https://arstechnica.com/space/2025/05/venus-aerospace-flies-its-rotating-detonation-rocket-engine-for-the-first-time/)

美国维纳斯航空公司在新墨西哥州美国航天港成功完成旋转爆震火箭发动机的首次美国飞行测试，取得“历史性”里程碑。这项在学术界讨论已久的科技，有望显著提高从海军舰艇到火箭等应用领域的燃料效率。

此次测试采用了一个由2000磅推力发动机驱动的小型火箭，飞行约30秒，未突破音障。与采用连续燃烧的传统火箭发动机不同，旋转爆震发动机利用在圆形通道中传播的超音速冲击波，由连续的燃料和氧化剂注入驱动。

维纳斯航空公司由Sassie和Andrew Duggleby五年前创立，旨在开发强大的旋转爆震发动机，最终制造出能够在两小时内搭载乘客飞越全球的超音速飞机。虽然这个长期目标还很遥远，但该公司正专注于近期机遇，将自身定位为商业和国防领域经济实惠的超音速飞行的领导者。他们目前正与美国国防、国家安全机构以及商业伙伴合作，探索超音速在物流、航空航天和未来交通领域的应用。

Sassie Duggleby强调了政府持续资助对于维持美国在超音速领域竞争力的重要性。虽然具体客户尚未披露，但这次成功的发动机测试代表着在实现超音速商业飞行潜力方面迈出了重要一步。

---

## 60. 第一个“电子国度”的诞生

**原文标题**: The mak­ing of the first 'elec­tro­state'

**原文链接**: [https://ft.pressreader.com/v99e/20250512/281754160214210](https://ft.pressreader.com/v99e/20250512/281754160214210)

由于提供的内容仅为标题和一个网站地址（"PressReader.com－透过新闻将世界连结"），缺少实际文章内容，我只能根据标题提供非常笼统和推测性的总结：

题为《首个“静电装置”的诞生》的文章可能深入探讨了首个利用静电的设备或技术的历史。静电学研究的是静止电荷及其产生的力。

文章可能探讨以下内容：

*   **发明/发现：** 确定被称为首个“静电装置”的具体设备或系统。这可能是历史上的静电发生器、电容器或实验仪器。
*   **发明者：** 重点介绍负责创造或发现“静电装置”背后原理的个人。
*   **历史背景：** 将该发明置于其科学和社会环境中。它可能讨论当时普遍的电力认知以及推动该发明的动机。
*   **其背后的技术：** 解释该设备所采用的静电学基本原理。
*   **其应用和影响：** 描述“静电装置”的早期用途及其对电力科学技术发展的影响。
*   **挑战和局限性：** 解决设备在开发或使用过程中遇到的任何困难。

由于内容来自 PressReader，因此很可能是一篇面向普通大众的新闻报道，重点在于使这种早期静电技术的历史易于理解和引人入胜。要获得完整准确的总结，需要文章的全部内容。

---

## 61. Show HN: Lumier – 在 Docker 中运行 macOS 虚拟机

**原文标题**: Show HN: Lumier – Run macOS VMs in a Docker

**原文链接**: [https://github.com/trycua/cua/tree/main/libs/lumier](https://github.com/trycua/cua/tree/main/libs/lumier)

"Show HN"：Lumier——在Docker容器中运行macOS虚拟机

Trycua (用户名) 的 Lumier 项目允许用户在 Docker 容器中运行 macOS 虚拟机 (VM)。该项目托管在 GitHub 上，用户名 "cua"，已获得显著关注，拥有 6.7k 星和 267 个 fork。

本质上，Lumier 通过利用 Docker 的容器化能力，简化了创建和管理 macOS VM 的过程。这使得开发人员和用户能够在各种平台上运行 macOS 环境，而无需传统的虚拟化软件。

主要优势在于可移植性和易于部署。用户无需在 hypervisor 上安装和配置 macOS，只需拉取 Docker 镜像并在其中运行 macOS VM 即可。这简化了开发、测试和构建自动化等需要 macOS 环境的任务的工作流程。

大量的 star 和 fork 表明社区对该项目有浓厚的兴趣，这可能是由于它简化了在 Docker 化环境中 macOS VM 的部署和管理。

---

## 62. 凯尔特币入门：粗糙野蛮，还是与众不同？

**原文标题**: Getting Started with Celtic Coins – Crude and Barbarous, or Just Different?

**原文链接**: [https://collectingancientcoins.co.uk/getting-started-with-celtic-coins-crude-and-barbarous-or-just-different/](https://collectingancientcoins.co.uk/getting-started-with-celtic-coins-crude-and-barbarous-or-just-different/)

本文旨在纠正一种误解，即凯尔特硬币因缺乏技艺而显得“粗糙”或“野蛮”。文章认为，这种看法源于将凯尔特抽象艺术与重视现实主义表现的古典风格进行比较。作者认为，凯尔特硬币的设计是有意为之，反映了他们的艺术偏好。

文章指出，早期凯尔特硬币是对希腊硬币的模仿，但随着时间的推移，凯尔特人通过对原始图像的解构、抽象和再整合，发展出了自己的风格。这导致过渡期的硬币可能显得笨拙。

一个关键点是，理解最初的原型有助于欣赏其抽象性。作者以一枚源自马其顿腓力二世斯塔特的凯尔特硬币为例，展示了追溯图像的演变如何揭示阿波罗和战车御夫的潜在形态，这些形态在后来的凯尔特硬币上被高度抽象化。

文章还讨论了“序列图像”，即硬币雕刻师根据先前的设计进行小的、渐进式的改变，从而能够追溯到原始来源。

最后，文章指出，有意使用比坯饼更大的模具，导致单个硬币上的设计不完整。这被解释为一种有意的选择，旨在表现可见图像之外的精神维度，尽管这给寻求完整设计的收藏家带来了挑战。作者强调了重量和合金的精确性，表明模具尺寸是有意为之。

---

## 63. 盒子里的RPG

**原文标题**: RPG in a Box

**原文链接**: [https://rpginabox.com/](https://rpginabox.com/)

RPG in a Box 是一款用户友好的软件，让用户无需编程或建模知识，即可创建游戏和互动体验。 它将游戏开发所需的一切“装在一个盒子里”。

主要功能包括：

*   **体素编辑器：** 创建和动画基于3D像素块（体素）的瓷砖、对象和角色。它还支持从 MagicaVoxel 和 Qubicle 导入。
*   **地图编辑器：** 构建基于网格的世界，并使用直观的导航和交互系统，用可交互的 NPC 和对象填充它们。
*   **可视化脚本：** 使用基于节点的脚本编辑器通过拖放操作或自定义的类 Lua 脚本语言来实现游戏内事件。
*   **对话系统：** 使用可视化流程图创建分支 NPC 对话。
*   **摄像机系统：** 使用预设或可自定义的摄像机来创建动态过场动画。
*   **UI 自定义：** 设计对话框并自定义界面元素，如库存、主菜单和滚动字幕。
*   **基础物品：** 定义玩家可以找到和使用的物品，附加脚本以触发效果。
*   **音效生成器：** 创建复古风格的音效。

该软件允许用户将他们的游戏导出为适用于 Windows 和 MacOS 的独立格式。 鼓励用户加入官方论坛，与社区联系并参与开发过程。

---

## 64. 美国最古老的数字计算机的末日[视频]

**原文标题**: Doom on the Oldest Digital Computer in America [video]

**原文链接**: [https://www.youtube.com/watch?v=no0CkQk7id0](https://www.youtube.com/watch?v=no0CkQk7id0)

这个YouTube视频，标题为“在美国最古老的数字计算机上运行毁灭战士”，很可能展示了经典视频游戏《毁灭战士》在一台极其古老的计算机上运行。然而，该视频的描述只是标准的YouTube样板页脚，包括指向版权信息、广告、开发者资源、服务条款、隐私政策和YouTube运营概述等页面的链接。它还提到了“NFL Sunday Ticket”以及Google LLC在2025年拥有的版权。

标题本身是最具信息量的元素，暗示着一场技术独创性和历史保护的演示。将《毁灭战士》这样一款原本为更现代硬件设计的游戏改编到古董数字计算机上运行，将是一项重大的壮举，突出了计算能力随时间的进步。在没有实际观看视频的情况下，我们只能推断该视频很可能记录了将《毁灭战士》运行在这台历史机器上的过程、挑战以及最终的成功（或失败）。该视频很可能面向对计算机历史、怀旧游戏和技术成就感兴趣的观众。

---

## 65. 大迁徙已经开始了？

**原文标题**: The great displacement is already well underway?

**原文链接**: [https://shawnfromportland.substack.com/p/the-great-displacement-is-already](https://shawnfromportland.substack.com/p/the-great-displacement-is-already)

无法访问文章链接。

---

## 66. Smalltalk-78 Xerox NoteTaker 浏览器内模拟器

**原文标题**: Smalltalk-78 Xerox NoteTaker in-browser emulator

**原文链接**: [https://smalltalkzoo.thechm.org/users/bert/Smalltalk-78.html](https://smalltalkzoo.thechm.org/users/bert/Smalltalk-78.html)

这是一个Smalltalk-78 Xerox NoteTaker的浏览器内模拟器。用户可以加载镜像、单步调试代码、运行、返回、发送、撤销，并访问诸如断点和帮助文件等调试功能。提供调整屏幕亮度、对比度以及启用有序抖动的选项。内容强调用户能够在本地修改和保存Smalltalk镜像，并突出显示这些更改不会影响服务器。

文本还警告用户，JavaScript VM代码的更改将立即影响其他用户，敦促负责任地使用。提供了示例Smalltalk代码片段，用于检查已保存的文件、分析空间使用情况以及启用实验性的32位对象指针。

最后，内容展示了一个加载的JavaScript文件日志，这些文件与模拟器的用户界面和功能相关，包括用于文件系统访问、键盘帮助、日志消息和Lively Web框架组件的模块。日志包括每个模块的加载时间。提供了跟踪、清除和重新附加日志的选项。

---

## 67. Show HN: HelixDB – 用于 AI 应用的开源向量图数据库 (Rust)

**原文标题**: Show HN: HelixDB – Open-source vector-graph database for AI applications (Rust)

**原文链接**: [https://github.com/HelixDB/helix-db/](https://github.com/HelixDB/helix-db/)

HelixDB：基于Rust的开源图向量数据库

---

## 68. Kubernetes上的高可用Mosquitto MQTT

**原文标题**: High Available Mosquitto MQTT on Kubernetes

**原文链接**: [https://raymii.org/s/tutorials/High_Available_Mosquitto_MQTT_Broker_on_Kubernetes.html](https://raymii.org/s/tutorials/High_Available_Mosquitto_MQTT_Broker_on_Kubernetes.html)

本文详细介绍了如何在 Kubernetes 上搭建高可用性的 Mosquitto MQTT 代理，专门针对 k3s 和 Traefik，但也适用于 Nginx。 目标是与单个 Mosquitto Pod 部署相比，最大限度地减少停机时间。

该解决方案涉及部署两个 Mosquitto 代理（主代理和辅助代理），并采用故障转移机制，如果主代理发生故障，该机制会在几秒钟内将流量切换到辅助代理。 这是通过使用 `raymii-mosquitto-failover` Pod 实现的，该 Pod 监视主代理的就绪状态。 这些代理配置为桥接消息，从而确保辅助代理上近乎实时的消息状态。 客户端连接到单个 LoadBalancer 服务 (`raymii-mosquitto-svc`)，该服务会被动态地重新路由。

关键组件包括：

*   **ConfigMaps:** 定义主代理和辅助代理的配置，包括桥接设置。
*   **Deployments:** 部署主 Mosquitto 实例和辅助 Mosquitto 实例，确保它们使用 `podAntiAffinity` 在不同的节点上运行。
*   **Services:** 公开 MQTT 代理，包括具有动态流量路由的主负载均衡器服务。
*   **RBAC:** 授予故障转移 Pod 监视 Pod 状态和修补服务选择器所需的权限。
*   **Traefik IngressRouteTCP:** 路由外部 MQTT 流量。

故障转移 Pod 在循环中运行 `kubectl` 以检查主代理的就绪状态。 失败后，它会修补 `raymii-mosquitto-svc` 以指向辅助代理。 虽然很少见，但如果故障转移 Pod 的节点和主节点同时发生故障，停机时间仍然可能约为 5 分钟。 此设置利用消息桥接来最大限度地减少故障转移期间的消息丢失，并允许客户端自动重新连接到功能正常的代理。 作者还解释了为什么故障转移 Pod 需要 RBAC，以及为什么一个简单的 shell 脚本比一个更复杂的自定义控制器更好。

---

## 69. 地理流动性为何下降？

**原文标题**: Why Is Geographic Mobility Declining?

**原文链接**: [https://www.richmondfed.org/publications/research/economic_brief/2025/eb_25-19](https://www.richmondfed.org/publications/research/economic_brief/2025/eb_25-19)

里士满联邦储备银行经济简报探讨了过去 30 年美国地理流动性下降的现象。作者指出了几个促成因素，大致可分为长期趋势和地理分布变化。

**主要发现：**

*   **总体下降：** 各年龄段的州际迁移率均呈稳步下降趋势。
*   **人口结构变化：**
    *   **人口老龄化：** 年长者的流动性较低，导致总体下降。
    *   **女性收入：** 女性收入和就业机会增加降低了家庭流动性，因为双职工夫妇不太可能搬迁。
*   **地理分布变化：**
    *   **工资趋同：** 各地区工资差异缩小，降低了为获得更高工资而迁移到特定工作的动机。
    *   **集聚效应：** 受过高等教育的人聚集在大型城市（认知中心），以寻求专业的工作机会。
    *   **住房成本：** 理想城市地区的高住房成本限制了迁移，并降低了劳动者居住在生产效率最高地方的能力。此外，人们对住房成本的反应也不如以往。
    *   **年轻人与父母同住：** 由于高住房成本，这种趋势增加，限制了流动性。

**作者的结论是，**迁移的下降是由多种因素共同驱动的，包括家庭需求的变化、公司的招聘策略，以及显著地，限制供应并提高价格的住房法规。虽然家庭需求和公司行为很重要，但住房法规的影响是一个正在进行的研究领域。

---

## 70. 变长开关

**原文标题**: Variadic Switch

**原文链接**: [https://pydong.org/posts/variadic-switch/](https://pydong.org/posts/variadic-switch/)

模拟C++中的可变参数switch语句：多种技巧与编译优化

---

## 71. 上海允许乘客设计自己的公交线路

**原文标题**: Bus stops here: Shanghai lets riders design their own routes

**原文链接**: [https://www.sixthtone.com/news/1017072](https://www.sixthtone.com/news/1017072)

上海推出新型“定制巴士”系统，居民可自行设计公交线路。通过市政府运营的平台，居民可以根据自身需求提出线路，指定起点和终点、首选时间和频率。如果足够多的人（通常为15-20人）选择或投票支持某条线路，该线路就可以获得批准并在短短三天内启动。

上海16个区已开通超过220条定制巴士线路。其中一条成功的试点线路，DZ301，连接地铁站与周边住宅区、学校和办公场所，每天服务约250-260名乘客。在此过程中，公交工作人员会进行现场调研和试运行，以优化发车时间表，然后才会正式开通。

专家认为，该系统通过使公交运力与实际需求更好地匹配，从而提高了效率和资源分配。 “热门定制”页面允许用户为提出的线路争取支持，团体预订可以加快审批速度。票价以市场为基础，并遵循公共交通标准，但目前不提供折扣。

虽然该系统简化了线路开通流程，但仍然存在挑战，包括乘客需求不均衡、公众认知度低以及对人工实地考察的依赖。市政府官员正专注于改进线路规划、升级平台功能以及提高公众知名度，以进一步提高定制巴士系统的有效性。

---

## 72. Uber将在美国主要城市推出固定路线班车

**原文标题**: Uber to introduce fixed-route shuttles in major US cities

**原文链接**: [https://techcrunch.com/2025/05/14/uber-to-introduce-fixed-route-shuttles-in-major-us-cities-other-ways-to-save/](https://techcrunch.com/2025/05/14/uber-to-introduce-fixed-route-shuttles-in-major-us-cities-other-ways-to-save/)

优步推出“路线共享”服务，在巴尔的摩、波士顿、芝加哥、达拉斯、纽约、费城和旧金山推出全新的固定线路班车服务，与UberX相比，乘客最多可节省50%的费用。这些通勤班车将沿着繁忙的交通走廊，每20分钟在预设站点之间运行，站点由优步根据热门出行模式的数据确定，最多可搭载两名额外乘客。乘客可以提前七天或至少提前10分钟进行预订。

此举旨在在经济压力下吸引和留住用户。优步还推出了“乘车通行证”，乘客只需支付少量费用即可锁定特定路线的价格，或购买预付费行程套餐以获得更大幅度的折扣，该服务在特定城市提供，随后将扩大范围。

优步外卖正在扩大与OpenTable的合作，允许用户通过优步应用程序预订餐厅，并获得前往餐厅的乘车折扣。OpenTable会员还可以将积分兑换成优步和优步外卖的优惠。

优步设想了“路线共享”服务在自动驾驶汽车方面的未来应用，可能在2026年之前在洛杉矶使用大众汽车的ID. Buzz AD电动汽车。这些努力，包括新功能和合作关系，旨在提供更实惠的选择，并鼓励优步生态系统内的可预测现金流和用户参与。

---

## 73. 安卓版Nextcloud应用最近丢失的文件上传功能

**原文标题**: The recently lost file upload feature in the Nextcloud app for Android

**原文链接**: [https://nextcloud.com/blog/nextcloud-android-file-upload-issue-google/](https://nextcloud.com/blog/nextcloud-android-file-upload-issue-google/)

Nextcloud安卓应用文件上传功能受限：原因、影响与进展

本文讨论了Nextcloud安卓应用文件上传功能缺失导致的用户不满。核心问题在于谷歌撤销了一项关键权限，该权限曾允许Nextcloud应用同步所有文件类型，但自2024年中以来，上传仅限于照片和视频。

Nextcloud认为谷歌以“安全顾虑”为由的解释值得怀疑，并暗示谷歌正在利用其平台所有权，优先照顾自家服务。尽管多次申诉，谷歌拒绝恢复该权限，迫使Nextcloud遵守，这对用户造成了很大的损害。虽然Android应用在F-Droid等替代应用商店上仍以完整权限运行，但Google Play商店中的大多数用户都受到了影响。

Nextcloud认为这种情况是大型科技公司把关行为的一个例子，阻碍了竞争和创新。他们认为，法律途径的成本太高且耗时太长。

本文以更新结尾：5月15日，谷歌联系了Nextcloud，表示愿意恢复该权限。Nextcloud正在准备一个恢复了该功能的测试版本，如果一切顺利，预计下周初发布最终更新。Nextcloud对用户的支持表示感谢。

---

## 74. Show HN: Data.olllo 的 CSV GB+ – 本地打开和处理 CSV 文件

**原文标题**: Show HN: CSV GB+ by Data.olllo – Open and Process CSVs Locally

**原文链接**: [https://apps.microsoft.com/detail/9pfcrwp46v22?hl=en-US&gl=US](https://apps.microsoft.com/detail/9pfcrwp46v22?hl=en-US&gl=US)

展示HN：Data.olllo 的 CSV GB+ – 本地打开并处理 CSV 文件

---

## 75. 短信双重验证不仅不安全，而且对山区居民不友好。

**原文标题**: SMS 2FA is not just insecure, it's also hostile to mountain people

**原文链接**: [https://blog.stillgreenmoss.net/sms-2fa-is-not-just-insecure-its-also-hostile-to-mountain-people](https://blog.stillgreenmoss.net/sms-2fa-is-not-just-insecure-its-also-hostile-to-mountain-people)

该文章认为，基于短信的双因素认证(2FA)不仅不安全，而且歧视居住在手机信号不佳地区的人们，特别强调了阿巴拉契亚山区居民面临的挑战。

作者以其居住在北卡罗来纳州西部的一位老年朋友为例，由于手机信号不可靠，以及依赖她在家无法接收的短信2FA验证码，她难以访问在线帐户。尽管她有固定电话和互联网服务，但Spectrum不支持短信到固定电话，并且短码短信通常无法通过Wi-Fi通话使用。

该文章强调了在这些情况下绕过短信2FA所需的不便且往往不切实际的解决方案：前往有信号的区域切换到基于时间的一次性密码(TOTP) 2FA（如果可用的话），联系客户服务（通常不可能），将电话号码转移到VOIP提供商，购买昂贵的信号增强器，或者搬家。

作者批评了手机信号覆盖地图的虚假宣传，并指出即使是该地区更年轻、更精通技术的个人也在努力应对短信2FA。他们还指出了TOTP作为替代方案的可用性问题，需要下载应用程序，并且常常造成令人困惑的技术选择。

文章总结道，虽然短信2FA在有效时提供了便捷的用户体验，但它使居住在手机信号不佳的山区的大部分人口处于不利地位，并呼吁采取更具包容性的在线安全方法。

---

## 76. MicroPython v1.25.0

**原文标题**: MicroPython v1.25.0

**原文链接**: [https://github.com/micropython/micropython/releases/tag/v1.25.0](https://github.com/micropython/micropython/releases/tag/v1.25.0)

MicroPython v1.25.0 引入了多项重大功能和改进，标志着三年开发后的重要更新。主要亮点是“ROMFS”功能，使字节码能够直接从只读、内存映射的文件系统中执行。这加快了导入速度并减少了内存使用，尤其有利于资源受限的设备。ROMFS 最初在特定板上启用，并计划进行更广泛的实施。

此版本还包括一个针对 Alif Ensemble MCU 的新“alif”端口，支持多个 ARM 内核和外设，包括 USB、双核支持、八进制 SPI 闪存和 WiFi/BLE。内联汇编现在支持 32 位 RISC-V 代码，并且支持数据报 TLS (DTLS)，用于跨多个端口的安全 UDP 连接。

mpremote 命令行工具获得了递归删除功能和增强的软件包管理。核心解释器改进包括增强的字符串处理、新的构建标识符以及列出已挂载文件系统的功能。引入了 marshal 模块，用于将代码对象转换为字节或从字节转换。本机链接器现在支持静态库，从而可以在本机模块中使用标准 C 函数。

esp32 端口已更新为支持 IDF v5.3 和 v5.4，而 mimxrt 端口添加了 exFAT 和 UF2 引导加载程序支持。在各个端口中添加了许多板定义，以及代码大小优化和错误修复。

总的来说，v1.25.0 专注于提高性能、扩展硬件支持以及添加像 ROMFS 这样的功能，以增强 MicroPython 的功能和可用性。

---

## 77. Replicube：一款通过编写代码来创造形状的解谜游戏

**原文标题**: Replicube: A puzzle game about writing code to create shapes

**原文链接**: [https://store.steampowered.com/app/3401490/Replicube/](https://store.steampowered.com/app/3401490/Replicube/)

这段文字描述了Steam（一个视频游戏平台）上的一个页面。这个页面是关于一个名为“Replicube：一个通过编写代码来创造形状的益智游戏”的游戏的。

这段文字列出了标准的Steam导航元素，例如：

*   **商店板块：**主页、探索队列、愿望单、点数商店、新闻、统计、社区
*   **Steam平台访问：**主页、讨论、创意工坊、市场、直播、关于、客服
*   **用户操作：**安装Steam、登录

最突出的是，这段文字展示了一个语言选择菜单，提供了非常广泛的语言列表。最后，它还包括一个“报告翻译问题”的链接。

简而言之，这个Steam页面片段是关于一款名为Replicube的游戏，并突出了语言选项和通用平台导航。

---

## 78. EM-LLM：无限上下文LLM的人工智能情景记忆

**原文标题**: EM-LLM: Human-Inspired Episodic Memory for Infinite Context LLMs

**原文链接**: [https://github.com/em-llm/EM-LLM-model](https://github.com/em-llm/EM-LLM-model)

EM-LLM：一种受人类情景记忆启发的大语言模型架构，无需微调即可处理几乎无限的上下文长度。它克服了典型大语言模型在处理大量上下文时遇到的局限性。EM-LLM使用贝叶斯惊讶度和图论边界细化，以在线方式将token序列组织成情景事件。这种分割方式模仿了人类的事件认知。

相关信息的检索通过一个两阶段的记忆过程实现：基于相似性的搜索和时间连续事件选择。这使得能够高效且像人类一样地访问信息。

在LongBench和$\infty$-Bench基准测试中的评估表明，EM-LLM的性能优于最先进的检索模型，如InfLLM和RAG，甚至在许多任务中超过了全上下文模型。重要的是，EM-LLM实现了跨越1000万个token的检索，这对于全上下文模型来说在计算上是不可行的。该架构利用配置参数来控制诸如块大小、块数量、内存分配和边界细化等方面。可以使用提供的脚本和下载的数据集进行评估。该论文还强调了EM-LLM的事件分割与人类感知的事件之间存在很强的相关性，表明它与生物记忆机制存在联系。

---

## 79. 了不起的盖茨比如何风靡高中校园

**原文标题**: How “The Great Gatsby” took over high school

**原文链接**: [https://www.newyorker.com/books/page-turner/how-the-great-gatsby-took-over-high-school](https://www.newyorker.com/books/page-turner/how-the-great-gatsby-took-over-high-school)

本文阐述了F. Scott Fitzgerald的《了不起的盖茨比》如何成为美国高中英语课程中的经典读物，从而确保了其持久的流行度和文学意义。尽管菲茨杰拉德最初担心这本书会失败，但《盖茨比》在他去世后逐渐受到欢迎，尤其是在二战期间分发给美国士兵之后。J.D.塞林格的《麦田里的守望者》中对它的提及以及第一部菲茨杰拉德传记的出版进一步巩固了它的吸引力。

带有学习指南和克里夫笔记的学生版问世，巩固了《盖茨比》在课堂上的地位，使学生能够分析其主题和象征意义。本文强调了新批评运动的影响，该运动强调细读和象征性解读，这使得拥有丰富象征意义的《盖茨比》成为教授这些分析技巧的理想文本。

教师们利用这部小说来探索美国梦、物质主义和社会阶层等主题，经常将咆哮的二十年代与当代社会进行对比。本文承认《盖茨比》在课堂上的持久存在，但也注意到教育重点的转变，由于共同核心和AP英语语言与写作项目等举措，对非小说类和信息类文本的关注日益增加。尽管面临这些挑战，《了不起的盖茨比》仍然是数百万高中生学习的重要作品，确保了它的遗产得以延续。

---

## 80. 无障碍更新 – GTK开发博客

**原文标题**: An accessibility update – GTK Development Blog

**原文链接**: [https://blog.gtk.org/2025/05/12/an-accessibility-update/](https://blog.gtk.org/2025/05/12/an-accessibility-update/)

这篇GTK开发博客文章提供了一份可访问性(a11y)更新，重点介绍了过去一年所做的改进。 主要进展是将AccessKit后端合并到GTK 4.18中，这使得GTK应用程序首次可以在Windows和macOS上实现可访问性。

该文章还详细介绍了Wayland可访问性的进展，特别是实现了传统上由Orca屏幕阅读器使用的键盘快捷键，从而弥补了GNOME 48中的一个主要缺口。

Georges Basile Stavracas Neto为使webkitgtk具有可访问性所做的努力，尤其是在flatpak沙箱中，也得到了强调，这使得GNOME Web成为一个完全可访问且经过沙箱处理的浏览器。

此外，还发布了一个名为Elevado的新可访问性工具，它为浏览和探索应用程序在a11y总线上的暴露提供了一个替代Accerciser的方案。

除了这些重大进展之外，该文章还指出了一些较小的改进，包括在文件选择器中添加了可访问的标签、工具提示和按键绑定，改进了Orca的列表框信息，GTK检查器中的按钮大小警告，AT的平台状态更改通知，改进的快捷键和助记符报告，更好的文本属性报告，可访问的libadwaita toast通知，以及改进的libadwaita操作行小部件的可访问表示。作者强调，由于许多人的贡献，GNOME中的可访问性正在不断提高。

---

## 81. 改变我对编程语言思考方式的文章

**原文标题**: Writing that changed how I think about programming languages

**原文链接**: [https://bernsteinbear.com/blog/pl-writing/](https://bernsteinbear.com/blog/pl-writing/)

Max Bernstein的博文重点介绍了一系列深刻影响了他对编程语言和编译器理解的文章、论文和演讲。他提供了一个精选列表，每个条目都为特定领域提供了变革性的视角。

重点介绍的内容涵盖了广泛的主题，包括垃圾回收（Andy Wingo的简单半空间收集器）、编译器优化（CF Bolz-Tereick的玩具优化器系列以及使用Z3的抽象域）、寄存器分配（Chris Fallin的Cranelift正确性方法）、正则表达式引擎（Russ Cox的虚拟机方法）、神经网络（Andrej Karpathy的micrograd）、SSA形式实现（Fil Pizlo的使用Identity标签的方法）、JavaScriptCore的优化技术（Fil Pizlo的JavaScriptCore推测）、针对性能的编译器设计（Chandler Carruth关于Carbon Toolchain的演讲）、字节码解释器（Allison Kaptur的Python解释器）、解析技术（Eli Bendersky的优先级爬升）、代码生成和寄存器分配（Takashi Kokubun的Ruby JIT挑战）、编译器构造策略（Abdulaziz Ghuloum和Fernando Borretti的增量方法）、等式饱和和e-图（egg项目和Chris Fallin的Cranelift使用），以及AST存储和表示（Bob Nystrom和Adrian Sampson关于紧凑AST的想法）。

Bernstein强调了每一部分如何改变了他的视角，通常简化了复杂的概念或引入了新的技术。他包括对Wingo的垃圾收集器代码的一个小修正，并提出了关于代码正确性的哲学问题。这篇文章为那些寻求加深编程语言和编译器设计知识的人提供了一个宝贵的资源。

---

## 82. Coinbase称数据泄露导致客户个人信息被盗

**原文标题**: Coinbase says customers’ personal information stolen in data breach

**原文链接**: [https://techcrunch.com/2025/05/15/coinbase-says-customers-personal-information-stolen-in-data-breach/](https://techcrunch.com/2025/05/15/coinbase-says-customers-personal-information-stolen-in-data-breach/)

Coinbase遭遇重大数据泄露，黑客通过贿赂美国境外客服人员，窃取了包括政府颁发身份证件在内的敏感客户信息。被盗数据包括客户姓名、地址、电话号码、社保号码后四位、屏蔽后的银行账号、交易记录和内部文件。

此次泄露事件在数月前被发现，Coinbase已警告受影响客户。该公司拒绝支付黑客索要的2000万美元赎金。虽然该公司正在开设美国境内的客服中心并加强安全措施，但预计修复和客户赔偿费用将达到1.8亿至4亿美元。

Coinbase声称，受影响的客户不到其每月970万客户总数的1%。TechCrunch的安全编辑Zack Whittaker正在寻求更多关于此次泄露的信息，可通过Signal或电子邮件联系。该文章于2025年6月5日在加利福尼亚州伯克利发表。

---

## 83. 等待你的实验

**原文标题**: It Awaits Your Experiments

**原文链接**: [https://www.rifters.com/crawl/?p=11511](https://www.rifters.com/crawl/?p=11511)

彼得·沃茨反思克里斯蒂安·博克的《异种文本实验》历经漫长等待终于完成，该项目旨在将一首诗编码到一种极其耐辐射的细菌——奇异球菌的基因代码中。博克的这项事业始于21世纪初，涉及将“俄耳甫斯”和“欧律狄刻”之间的对话编码到细菌的DNA中，“欧律狄刻”甚至被设计成发出红色荧光。

文章详细介绍了博克面临的挑战，包括必须掌握遗传学、蛋白质组学和编码，以及招募一个团队来开发新的分子技术。最初在大肠杆菌中遭遇挫折，后来在奇异球菌中也遇到了阻碍，因为奇异球菌对外来代码具有抵抗性。沃茨幽默地描绘了仅为了艺术创作而大胆使用科学的行为。

经过十年的沉寂之后，博克成功地在奇异球菌中实现了《异种文本》，这是一项具有持久艺术意义的壮举。沃茨强调了该细菌的极端耐性和这首诗的潜在寿命，远远超过了典型的艺术不朽。他宣传博克即将出版的书籍《异种文本：第二卷》，该书庆祝了这一成就，融合了科学、小说和古典文学。沃茨还提到了这本书在多伦多举行的发布活动。评论部分讨论了该项目的意义，包括基因组修改的未来以及未来此类实验的可及性。

---

## 84. 降低 Rust 的学习曲线

**原文标题**: Flattening Rust’s learning curve

**原文链接**: [https://corrode.dev/blog/flattening-rusts-learning-curve/](https://corrode.dev/blog/flattening-rusts-learning-curve/)

本文提供了关于如何降低 Rust 学习曲线的建议。作者强调，最重要的是心态：学习者应该接受该语言独特的思维模型，并将借用检查器视为指导，而非对手。

作者建议早期慷慨地使用 `String`、`clone()` 和 `unwrap()`，采取“小步快跑”的方式，并在后期进行重构。同时建议避免在初期阶段使用异步 Rust，并专注于单独掌握核心概念。在 Rust playground 中定期测试代码片段以及能够接受丢弃代码至关重要。

在 Rust 中，代码的准确性至关重要，读者应该努力关注细节。作者告诫不要过度依赖 LLM 和代码补全等工具，而是提倡手动编写代码，以建立肌肉记忆并真正理解概念。

本文鼓励学习者预测代码输出，在寻求解决方案之前独立解决问题，并积极阅读其他人的 Rust 代码。此外，它强调要识别并直面回避的领域，例如过程宏等复杂特性。

作者还建议通过绘制图表来可视化生命周期等概念，从而建立良好的直觉，并通过将熟悉的概念映射到 Rust 等效项来利用现有的编程知识。最后，它鼓励仔细阅读 Rust 错误消息，并通过彻底研究标准库文档和函数签名来依靠类型驱动开发。

---

## 85. 氛围编码的逆向激励

**原文标题**: Perverse incentives of vibe coding

**原文链接**: [https://fredbenenson.medium.com/the-perverse-incentives-of-vibe-coding-23efbaf75aee](https://fredbenenson.medium.com/the-perverse-incentives-of-vibe-coding-23efbaf75aee)

弗雷德·本森的文章深入探讨了使用诸如Claude Code等AI编码助手时固有的“反向激励”。他认为，虽然这些工具由于其变比强化（偶尔的成功会产生多巴胺激增）而令人上瘾，但它们的成本可能高得惊人。一个关键问题是，AI编码代理，特别是Claude 3.7，倾向于生成过于冗长和过度设计的代码。

本森认为，这种冗长不仅仅是由于大型语言模型的不成熟，而是一种经济激励：许多AI编码助手按token数量收费。这造成了一种情况，即AI公司从冗长的代码中获利更多，从而阻碍了他们优化简洁性。作者将此与研究结果进行比较，研究表明，要求大型语言模型给出简洁的回答可能会降低事实准确性。

为了克服这一点，本森提出了以下策略：

*   强制大型语言模型在编码前进行计划。
*   实施严格的“先询问再生成”协议。
*   利用版本控制，无情地删除低效代码。
*   尝试更便宜、更小的模型。

最终，本森认为，应该转变方向，根据代码质量而不是token数量来评估和激励大型语言模型。他认为，货币化和用户需求之间的这种错位导致了低效且昂贵的AI编码辅助。作者最后幽默地承认了使用AI来批判AI冗长的讽刺意味，强调问题不在于AI本身，而在于人类驱动的、优化收入模型的商业决策。

---

## 86. 谷歌正在打造自己的DeX：安卓桌面模式初探

**原文标题**: Google is building its own DeX: First look at Android's Desktop Mode

**原文链接**: [https://www.androidauthority.com/android-desktop-mode-leak-3550321/](https://www.androidauthority.com/android-desktop-mode-leak-3550321/)

这篇文章介绍了谷歌正在开发的安卓“桌面模式”，该功能类似于三星DeX，允许用户将安卓手机连接到外部显示器以获得类似桌面的体验。文章展示了Pixel手机上该功能的早期版本，体现了其目前的未完成状态。

开发中的桌面模式的主要功能包括用于固定和最近使用的应用程序的任务栏，在自由调整大小的窗口中启动多个应用程序的能力，以及应用程序之间拖放功能的支持。该模式将安卓平板电脑的窗口环境调整为外部显示器。

虽然该功能不太可能与Android 16一同发布，但可能会在之后的季度版本或Android 17中出现。谷歌还在开发类似PC的外部显示工具，例如显示排列和屏幕间无缝鼠标移动。作者强调谷歌致力于该项目并确保最终产品完善的重要性，以增强安卓应用在更大屏幕上的可用性并统一谷歌的桌面操作系统工作。

---

## 87. 突破音障第一部分：使用Mach消息模糊测试CoreAudio

**原文标题**: Breaking the Sound Barrier Part I: Fuzzing CoreAudio with Mach Messages

**原文链接**: [https://googleprojectzero.blogspot.com/2025/05/breaking-sound-barrier-part-i-fuzzing.html](https://googleprojectzero.blogspot.com/2025/05/breaking-sound-barrier-part-i-fuzzing.html)

Dillon Franke 详细介绍了他在 MacOS 安全研究领域的探索之旅，重点介绍了如何使用 Mach 消息模糊测试 CoreAudio 以发现沙箱逃逸。他提倡“知识驱动型模糊测试”，这是一种将自动化模糊测试与手动逆向工程相结合的混合方法，以提高代码覆盖率并深入了解目标。

Franke 选择 Mach 消息作为攻击媒介，是因为它们在进程间通信中发挥的作用以及其历史安全问题。他针对了 coreaudiod 守护进程及其 com.apple.audio.audiohald 服务，因为它很复杂，可以从 Safari GPU 进程等沙箱进程访问，处理大量消息，并可能以提升的权限控制音频硬件。

他比较了两种模糊测试 harness 方法：使用 `mach_msg` API 进行进程间模糊测试，以及直接加载和调用消息处理程序的直接 harness。他选择了后者，因为它的速度快且易于进行代码覆盖，尽管存在潜在的误报。

他使用 `otool` 和 IDA Pro 在 CoreAudio 框架中找到了 Mach 消息处理代码，发现 MIG（Mach 接口生成器）子系统管理消息处理。通过找到 `_HALS_HALB_MIGServer_subsystem` 并交叉引用它，他确定了 `_HALB_MIGServer_server` 函数，该函数负责解析传入的 Mach 消息并根据 `msgh_id` 调用特定的处理程序。这个函数成为了他模糊测试工作的重点。

---

## 88. 悬赏2万美元优化Rav1d AV1解码器中的Rust代码

**原文标题**: $20K Bounty Offered for Optimizing Rust Code in Rav1d AV1 Decoder

**原文链接**: [https://www.memorysafety.org/blog/rav1d-perf-bounty/](https://www.memorysafety.org/blog/rav1d-perf-bounty/)

悬赏两万美元，征集能将基于 Rust 的 rav1d AV1 解码器性能提升至或超过基于 C 的 dav1d 解码器性能者。虽然 rav1d 功能完整且通过与 dav1d 相同的测试，但目前速度慢约 5%，阻碍了其应用。

赞助商正在寻求 Rust 社区的帮助，以实现性能对等，并希望深入了解 Rust 与 C 相比的性能。改进必须在 rav1d 的 Rust 代码、Rust 编译器或 Rust 标准库中进行。禁止修改共享汇编代码或将非 Rust 代码引入 rav1d。

竞赛面向来自美国、英国、欧盟、欧洲经济区、瑞士、加拿大、新西兰和澳大利亚的个人或团队开放。参与者必须通过相关项目（rav1d、Rust 编译器或 Rust 标准库）的标准贡献流程提交改进，然后通过电子邮件联系组织者以参加比赛。

奖金将根据组织者在比赛结束后酌情确定的性能提升贡献大小按比例分配。赞助商强调尽早提问以确保资格的重要性。

---

## 89. MetaPost中的各种事项 (2019)

**原文标题**: Various Things in MetaPost (2019)

**原文链接**: [https://habr.com/en/articles/454376/](https://habr.com/en/articles/454376/)

本文讨论了作者使用MetaPost为物理教科书创建插图的经验，重点介绍了程序化方法在生成可调整和视觉上有趣的图表方面的优势。面对创建数百个插图的艰巨任务，作者寻求一种自动化解决方案，并发现MetaPost是一个有价值的工具。

MetaPost的主要优势在于它能够将图片创建为变量的函数，从而可以在不破坏内部关系的情况下轻松进行调整。作者实现了诸如使用贝塞尔曲线绘制不同粗细的曲线，使用虚线在较薄区域绘制可变粗细的笔画，以及用一致的墨水密度绘制球体和管的方法。

本文展示了示例MetaPost代码，演示了这些技术，包括生成球体、管（直的和弯曲的，恒定和可变直径的）、锥体、栏杆、球体、砝码和结。它还涵盖了诸如阴影投射和木纹生成器之类的高级功能。最后，一个更复杂的L'Hôpital滑轮问题的例子展示了MetaPost如何准确地说明涉及可变参数的解决方案。

尽管该教科书被取消了，但作者在GitHub上重写并开源了该库，添加了诸如结之类的新功能。作者承认，由于用于创建细微视觉变化的伪随机数生成器，该代码并不是最快的。

---

## 90. Show HN: Airweave – 让智能体搜索任何应用

**原文标题**: Show HN: Airweave – Let agents search any app

**原文链接**: [https://github.com/airweave-ai/airweave](https://github.com/airweave-ai/airweave)

Airweave 是一款旨在帮助代理在各种应用、数据库和 API 中进行语义数据搜索的工具。它通过 REST 和 MCP 端点将结构化和非结构化数据转化为代理可用的知识，从而简化了代理访问信息的过程。

入门方法包括克隆 Airweave 仓库，并使用 Docker Compose 构建和运行它。UI 可通过 `http://localhost:8080` 访问，并提供连接数据源、配置同步和查询数据的界面。API 文档可通过 Swagger 获取。

Airweave 提供 Python 和 TypeScript/JavaScript 的 SDK，允许以编程方式访问其功能，例如列出数据源和创建同步任务。主要功能包括来自超过 25 个数据源的数据同步、实体提取和转换、多租户架构、增量更新、语义搜索、版本控制和白标支持。

技术栈包括 React/TypeScript 前端、FastAPI (Python) 后端、用于元数据的 PostgreSQL 以及用于向量存储的 Qdrant。部署方面，开发使用 Docker Compose，生产环境使用 Kubernetes。

路线图包括增加更多的数据源集成、实现用于大规模同步的 Redis 工作队列、整合用于事件驱动同步的 Webhooks，以及通过 Helm charts 提供 Kubernetes 支持。该项目欢迎贡献，采用 MIT 许可，并鼓励用户通过 Discord、GitHub Issues 或 Twitter 进行联系。

---

## 91. 用深奥的图论解决编程语言问题

**原文标题**: Using obscure graph theory to solve programming languages problems

**原文链接**: [https://reasonablypolymorphic.com/blog/solving-lcsa/](https://reasonablypolymorphic.com/blog/solving-lcsa/)

本文记录了作者为期一年的解决程序图序列化为一系列高效 let 绑定（共享）问题的历程。最初的解决方案是一个复杂的定制算法，但随着新语言功能的增加，最终崩溃了。

作者随后将问题重新定义为识别程序图中的菱形模式，并在内联源之前立即让绑定菱形的汇聚点。这导致了使用节点可达集，但该方法受到自由变量的阻碍。

性能问题开始显现，揭示了由于可达性计算效率低下导致的二次时间复杂度。作者随后咨询了一位图论专家，引入了最低单公共祖先 (LSCA) 的概念。虽然最低公共祖先 (LCA) 对于有向无环图 (DAG) 来说不是唯一确定的，但 LSCA 是，这提供了解决方案。该论文提出了一种通过构建“最低单祖先” (LSA) 树来计算 LSCA 的预处理方案。

作者发现了 Ed Kmett 的 `lca` 包，它提供了一种计算 LCA 的算法，这是 LSCA 算法的必要组成部分。最后，他们使用 LSA 树来确定在原始程序图中插入 let 绑定的位置。最终的解决方案比最初的临时方法更短、更有效（线性时间），并且被认为更优雅。

作者最后强调，该解决方案并非个人才华的体现，而是协作、研究、利用现有库以及记住晦涩的图论概念的结合。

---

## 92. 奥丁：一款为我而生的编程语言

**原文标题**: Odin: A programming language made for me

**原文链接**: [https://zylinski.se/posts/a-programming-language-for-me/](https://zylinski.se/posts/a-programming-language-for-me/)

卡尔·齐林斯基将Odin描述为一种根据他偏好的编码风格量身定制的编程语言，尤其让人想起他在游戏引擎公司Our Machinery工作时使用的C语言实践。他强调了他们的C语言设置与Odin之间共享的几个特性：

*   **自定义分配器：** Odin将分配器直接整合到基础库集合中，从而实现灵活的动态内存分配策略。
*   **临时分配器：** Odin包含一个内置的临时分配器(`context.temp_allocator`)，用于满足短期的内存需求，类似于游戏开发中使用的基于帧的分配。
*   **跟踪分配器：** Odin提供了一个跟踪分配器来检测内存泄漏，与他们在C语言中用于调试的工具相呼应。
*   **零初始化 (ZII)：** Odin自动将所有变量初始化为零，降低了未初始化内存错误的风险。
*   **指定初始化器：** Odin支持用于结构体构造的指定初始化器，从而提高了代码的可读性和可维护性。
*   **缓存友好编程：** Odin内置了对数组结构体 (SoA) 内存布局的支持，可以优化缓存使用以提高性能。
*   **简洁性：** Odin优先考虑简洁性，继承了C语言的这一特性，同时融入了现代特性，如泛型和重载，而不会变得过于复杂。

齐林斯基总结说，Odin的设计与他的编程背景非常吻合，使其易于学习。他推荐他的书《理解Odin编程语言》作为对这些概念不熟悉的人的有用入门。

---

## 93. E-COM：美国邮政 4000 万美元的纸质电子邮件项目

**原文标题**: E-COM: The $40M USPS project to send email on paper

**原文链接**: [https://buttondown.com/blog/the-e-com-story](https://buttondown.com/blog/the-e-com-story)

文章详述了E-COM的兴衰，这是一个美国邮政于1982年启动的耗资4000万美元的项目，旨在打印和投递电子邮件。面对电子通信将大幅减少邮件量的预测，美国邮政试图通过为没有电脑的人打印并实际投递电子信息，来利用电子邮件革命。

该系统允许企业通过TTY或IBM终端向指定的邮局发送信息，这些信息将被打印、折叠，并装入独特的蓝白信封中寄出。尽管它最初被采用，包括美国银行和西联汇款的使用，但E-COM面临着重大障碍：官僚主义的繁文缛节、高昂的成本以及定制方面的限制。

这项服务难以吸引主流企业，主要被垃圾邮件发送者采用，他们试图利用美国邮政信封的可信度。美国邮政在每封E-COM邮件上都损失了大量资金，导致其在1985年终止，累计损失超过4000万美元。

尽管E-COM失败了，但它无意中帮助推广了“e-mail”一词，并突显了美国邮政为适应技术变革所做的努力。具有讽刺意味的是，虽然E-COM失败了，但邮件量最初继续上升，直到后来随着数字通信的普及才急剧下降。美国邮政继续递送电子商务包裹，而电子邮件已经取代了大部分头等邮件。

---

## 94. 超 hot VR 的剧情被移除了。什么？

**原文标题**: Superhot VR's Story Was Removed. What?

**原文链接**: [https://blog.giovanh.com/blog/2025/05/14/superhot-vrs-story-was-removed-what/](https://blog.giovanh.com/blog/2025/05/14/superhot-vrs-story-was-removed-what/)

本文探讨了2021年《SUPERHOT VR》中故事内容被颇具争议地移除事件，并认为这是游戏史上一个重大事件，但由于文化战争的喧嚣而被 Largely dismissed。

作者详细介绍了《SUPERHOT》的开发历程，从最初的游戏原型、Kickstarter上的成功，到最终发布原版游戏和《SUPERHOT VR》。他们强调，原版游戏关于通过游戏玩法进行虐待式从属关系和心理调节的叙事，对其成功至关重要。故事的黑暗主题和对游戏成瘾本质的元评论，对第一人称射击游戏中典型的力量幻想提出了批评。

文章强调，《SUPERHOT VR》强化了这些主题，特别是其令人身临其境的结局，玩家被迫在VR中射杀自己，从而创造了一种深刻而有影响力的体验。作者认为，VR的沉浸式能力允许更深层次的艺术表达，使游戏能够有效地传达感受和情景。

《SUPERHOT VR》中故事内容的移除被视为关键定义特征的丧失和一种审查形式。作者批评了围绕这一变化的讨论，驳斥了关于“觉醒”的说法，并强调了真正可以理解的艺术和叙事问题。核心论点是，《SUPERHOT VR》作为一款具有历史意义的VR游戏，其一个重要方面在没有适当解释或替代的情况下被移除，从而降低了其整体艺术影响力。

---

## 95. 基于简单数学规则的16x16点阵动画

**原文标题**: A simple 16x16 dot animation from simple math rules

**原文链接**: [https://tixy.land](https://tixy.land)

本文展示了一种创意编程尝试：仅使用简单的数学规则生成一个16x16像素的动画，这很可能是为了代码高尔夫。函数`(t, i, x, y) => "creative code golfing"`表明代码接受四个输入：`t`（推测为时间，驱动动画）、`i`（可能是一个索引或标识符）、`x`（像素的x坐标）和`y`（像素的y坐标）。输出旨在表示该坐标和时间下像素的颜色或状态。

“创意代码高尔夫”一词意味着目标是用尽可能少的代码字符创建一个视觉上有趣的动画。核心挑战在于设计使用`t`、`i`、`x`和`y`的数学公式，当应用于每个像素时，随着`t`的变化，会产生动态且引人入胜的视觉模式。由于输出仅仅被描述为产生“创意代码高尔夫”，动画的具体细节和所使用的确切数学规则被有意地未指明，鼓励读者解释并可能尝试自己解决这一挑战。文章强调了优雅而简洁的代码产生令人惊讶的复杂和迷人的视觉效果的潜力。

---

## 96. 被忽视的杰作：充满关于一战的密码信息

**原文标题**: The overlooked masterpiece full of coded messages about World War One

**原文链接**: [https://www.bbc.com/culture/article/20250423-the-masterpiece-full-of-coded-messages-about-ww1](https://www.bbc.com/culture/article/20250423-the-masterpiece-full-of-coded-messages-about-ww1)

本文重点介绍了伊芙琳·德·摩根被忽视的艺术贡献。作为一位前拉斐尔派画家，她的作品如今因其对战争、灵性和女性自主的富有远见和象征意义的描绘而备受认可。文章以她的画作《屠龙》为例，阐释了第一次世界大战的苦难和束缚，揭示了德·摩根的和平主义立场以及她将艺术作为行动主义的手段。

德·摩根的作品以其对女性的刻画方式区别于传统的被动形象，而是将她们展现为充满希望和力量的强大人物。她的画作常常探讨善与恶、物质与精神、以及内在满足的重要性等主题。文章讨论了她对符号的使用，例如用龙来代表贪婪，用天使来体现和平与救赎。

文章还强调了德·摩根在技术和风格上的创新，包括她对抛光技巧和独特调色板的运用，这些都预示了后来的艺术运动。德·摩根展览的开幕和博物馆的重新开放，标志着人们对她的艺术以及她在黑暗中传递希望的信息的重新欣赏，并承认她是值得迟来的赞誉的先驱。作者指出，她的作品中常常蕴含着平静或希望。

---

## 97. ZJIT已合并至Ruby。

**原文标题**: ZJIT has been merged into Ruby

**原文链接**: [https://railsatscale.com/2025-05-14-merge-zjit/](https://railsatscale.com/2025-05-14-merge-zjit/)

本文宣布将新的即时 (JIT) Ruby 编译器 ZJIT 合并到 YARV Ruby 实现中。ZJIT 由 YJIT 背后的同一团队开发，与 YJIT 的不同之处在于它采用了更传统的编译器架构。ZJIT 不是直接从 YARV 字节码编译到低级 IR，而是使用基于高级 SSA 的中间表示 (HIR)，一次编译整个方法，利用历史类型信息，并具有模块化优化器。这种设计旨在促进社区贡献。

本文详细介绍了 ZJIT 的架构，概述了从 YARV 字节码到 HIR 优化，最终到机器代码生成的流程。它使用一个简单的 Ruby 函数 (`add`) 作为示例来说明此过程，展示了它如何从 YARV 字节码转换为 HIR，然后优化为具有 GuardType 指令的类型专用代码以进行运行时类型检查。代码随后移动到 LIR（低级 IR），最后移动到汇编。

虽然 ZJIT 仍处于早期开发阶段，但该团队的目标是在特性和性能方面与 YJIT 达到同等水平。Ruby 3.5 将同时发布 YJIT 和 ZJIT。未来的计划包括实现侧出口，以便在类型保护失败时跳回解释器，从而实现测试和性能基准测试。最终目标是为 Ruby 创建一个更易于访问且由社区驱动的 JIT 编译器。

---

## 98. 爱彼迎陷入中年危机

**原文标题**: Airbnb is in midlife crisis mode

**原文链接**: [https://www.wired.com/story/airbnb-is-in-midlife-crisis-mode-reinvention-app-services/](https://www.wired.com/story/airbnb-is-in-midlife-crisis-mode-reinvention-app-services/)

本文详述了由首席执行官Brian Chesky 领导的Airbnb雄心勃勃的重塑计划。Chesky受到Sam Altman/OpenAI事件的启发，推动公司超越短租业务，设想Airbnb成为一个预订各种服务的平台，从摄影师和私人教练到水管工和辅导老师，利用其现有的基础设施来审查房东和处理危机。

重塑计划包括重新设计的应用程序，其中包含代表租赁、服务和体验的新图标，以及旨在成为值得信赖的互联网身份的增强型用户配置文件。Airbnb正在为此扩张投资超过2亿美元，并在30个国家的260个城市推出。

一个关键组成部分是重新推出“体验”服务，提供独特的活动并与Conan O'Brien等名人合作。Chesky正在与前苹果设计师Jony Ive合作，并从史蒂夫·乔布斯那里汲取灵感来实现这一转型。他旨在创建一个供用户分享经验的“连接平台”，但并未将其称为社交网络。

现年43岁的Chesky感到自己正处于职业生涯的十字路口，他希望将Airbnb提升到苹果和微软等科技巨头的水平。虽然他承认挑战重重，但他相信Airbnb可以成为现实世界服务的可信赖的店面，从而显著扩大其市场和影响力。

---

## 99. 大卫·希尔伯特的广播讲话 (2014)

**原文标题**: David Hilbert's radio address (2014)

**原文链接**: [https://old.maa.org/press/periodicals/convergence/david-hilberts-radio-address](https://old.maa.org/press/periodicals/convergence/david-hilberts-radio-address)

根据提供的内容，没有文章。你提供的内容似乎是一个网站的结构和一些菜单项。没有实际的文章文本或与大卫·希尔伯特或2014年的广播讲话相关的内容。

因此，无法进行总结。所提供的信息仅表明存在一个网站，其中包含“首页”、“数学职业”、“联系我们”和“登录”等部分。没有关于希尔伯特或任何广播讲话的可供总结的信息。

---

## 100. Mozilla Firefox – 官方 GitHub 仓库

**原文标题**: Mozilla Firefox – Official GitHub repo

**原文链接**: [https://github.com/mozilla-firefox/firefox](https://github.com/mozilla-firefox/firefox)

本文档介绍了 Mozilla Firefox 的官方 GitHub 仓库。该仓库是公开的，包含了 Firefox 网页浏览器的完整源代码，用于开发、错误修复和功能添加。

该页面列出了仓库的关键信息，包括星标数（6.7k）和 Fork 数（177），以及指向 Firefox 网站和仓库许可证的链接。内容组织成目录和文件，这对于构建和理解 Firefox 至关重要。

本文档提供了参与 Firefox 开发的资源链接，包括目录结构、构建说明以及供开发者提问的 Matrix 聊天频道的相关文档。还提供了下载 nightly 开发版本的链接，并警告可能存在不稳定性。

总而言之，此 GitHub 仓库是 Firefox 开发的中心枢纽，提供源代码、构建信息、贡献指南以及访问开发版本。它对于对 Firefox 浏览器感兴趣的开发者和贡献者来说，是一个宝贵的资源。

---

