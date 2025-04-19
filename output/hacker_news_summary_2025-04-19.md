# Hacker News 热门文章摘要 (2025-04-19)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 图书馆员很危险

**原文标题**: Librarians Are Dangerous

**原文链接**: [https://bradmontague.substack.com/p/librarians-are-dangerous](https://bradmontague.substack.com/p/librarians-are-dangerous)

无法访问文章链接。

---

## 2. 在视频生成中，将输入帧上下文打包进下一帧预测模型

**原文标题**: Packing Input Frame Context in Next-Frame Prediction Models for Video Generation

**原文链接**: [https://lllyasviel.github.io/frame_pack_gitpage/](https://lllyasviel.github.io/frame_pack_gitpage/)

本文介绍一种注重效率和易用性的视频生成模型。其关键创新在于打包输入帧上下文，从而能够使用扩散模型生成高分辨率、高帧率（30fps）视频。该模型非常轻量级，可以使用消费级 6GB 笔记本电脑 GPU 上的 13B 参数模型生成全帧率视频。此外，该模型可以在配备 8 个 A100 或 H100 GPU 的单个节点上以相当大的批次大小 (64) 进行微调，从而为个人和实验室使用普及了对复杂视频模型训练的访问。在个人 RTX 4090 上的生成速度范围从未经优化的 2.5 秒/帧到使用“teacache”（一种潜在的优化技术）的 1.5 秒/帧。该架构利用视频扩散，但旨在模仿通常与图像扩散相关的稳定性和质量，并且至关重要的是，避免了时间步蒸馏，这表明了一种新颖的训练或推理方法。总而言之，这项工作优先考虑资源效率和易用性，使高质量视频生成更易于实现。

---

## 3. 大型语言模型的谱系推断

**原文标题**: Inferring the Phylogeny of Large Language Models

**原文链接**: [https://arxiv.org/abs/2404.04671](https://arxiv.org/abs/2404.04671)

该arXiv文章介绍了PhyloLM，一种用于推断大型语言模型（LLMs）系统发育的新方法。作者Nicolas Yax、Pierre-Yves Oudeyer和Stefano Palminteri将传统上用于群体遗传学的系统发育算法应用于LLMs领域。其核心思想是基于LLMs输出的相似性计算系统发育距离度量，从而捕捉这些模型之间的紧密程度。

研究人员基于这种距离度量构建树状图，成功反映了包含111个开源和45个闭源LLMs的数据集中的已知关系。至关重要的是，该研究通过证明系统发育距离可以预测LLM在标准基准测试中的性能，从而证明了其功能有效性。这表明PhyloLM提供了一种经济高效的方式来评估LLM的能力，而无需透明的训练信息或广泛的测试。

本质上，PhyloLM通过将群体遗传学的概念转化为机器学习，提供了一种评估LLMs的发展、关系和能力的工具。这有助于更深入地了解LLM的演变和性能预测。该论文还提供了在HuggingFace、Replicate和GitHub等平台上与该项目相关的代码、演示和工具的链接。

---

## 4. 基于GNU Radio和Codec2的开源SDR数字移动无线电(DMR)调制解调器实现

**原文标题**: Open Source DMR Modem Implementation in SDR with GNU Radio and Codec2

**原文链接**: [https://qradiolink.org/open-source-DMR-transceiver-implementation.html](https://qradiolink.org/open-source-DMR-transceiver-implementation.html)

本文详细介绍了一种使用GNU Radio和Codec2的开源DMR（数字移动无线电）调制解调器实现，目标是软件定义无线电（SDR）。目标是创建一个基本的DMR收发器，模拟用户无线电（MS），能够进行语音通话，并作为未来开发的基础，包括数据呼叫、Tier III集群和IPv4传输。

该调制解调器利用GNU Radio进行物理层处理，MMDVMHost的代码进行数据链路和呼叫控制层处理，以及Codec2进行语音编码/解码。该实现利用了易于获取的SDR硬件，例如LimeSDR-mini。

该软件实现了4FSK调制/解调。DMR BS接收器解码连续传输，而DMO接收器处理非连续传输。时序恢复通过来自SDR的时间戳和符号计数来实现。传输包括发送控制信号，与基站（BS）同步，然后在分配的时隙中传输数据。

Codec2是选定的声码器，提供2400比特/秒（具有潜在的FEC）或3200比特/秒（不带FEC）的比特率。该选择提供了一种替代常用AMBE编解码器的开源方案。

本文概述了诸如链路控制和嵌入式数据编码/解码、颜色码处理、时隙选择、声码器/比特率选择、呼叫类型选择和混杂模式接收等功能。它承认了诸如缺少预生成的静默帧等局限性，这需要解决。这项工作旨在创建一个面向业余无线电爱好者的DMR平台，提供超越专有解决方案的功能和灵活性。

---

## 5. 英国首例移植子宫孕妇诞下婴儿

**原文标题**: First baby born in UK to woman with transplanted womb

**原文链接**: [https://www.bbc.com/news/articles/c78jd517z87o](https://www.bbc.com/news/articles/c78jd517z87o)

在一项开创性成就中，36岁的格蕾丝·戴维森成为英国首位接受子宫移植后分娩的女性。格蕾丝天生患有MRKH综合征，这是一种子宫缺失或发育不良的疾病，她在2023年的一项开创性手术中接受了她妹妹艾米的子宫。2025年2月，她和她的丈夫安格斯迎来了他们的女儿艾米，以她阿姨的名字命名。

移植手术是一个复杂的过程，涉及30多名医务人员，耗时17个小时。移植后，格蕾丝通过试管婴儿怀孕，并在手术后不久经历了她的第一次月经。

这一成功为英国约15,000名子宫功能不全的女性带来了希望。由伊莎贝尔·奎罗加和理查德·史密斯教授领导的手术团队已经利用已故捐赠者的子宫进行了另外三次子宫移植，并计划完成15例作为临床试验的一部分。移植手术由慈善机构英国子宫移植基金会资助。在第二个孩子出生后，捐赠的子宫将被移除，以便格蕾丝停止服用免疫抑制剂药物。

---

## 6. 修复1992年六人座街机 Galaxian3 剧场6

**原文标题**: Restoring the Galaxian3 Theatre 6, 1992 six player arcade machine

**原文链接**: [https://philwip.com/2025/04/14/galaxian-3-project-revival/](https://philwip.com/2025/04/14/galaxian-3-project-revival/)

本文详细介绍了修复位于新罕布什尔州纳舒厄Fun World的一台废弃的1992年南梦宫Galaxian3剧场6人街机游戏的努力。作者Phil Bennett与一个团队一起进行了两次旅行，以诊断和修复这台机器。

2024年3月的初步评估显示，只有两个玩家输入功能正常，一些扬声器缺少声音，左侧投影机的蓝色输出暗淡且模糊。本文提供了硬件概述，详细介绍了各种PCB（主板、从板、DSP、PGN、OBJ、V-MIX、C-RAM、RSO、声音和PSN）、激光影碟播放器和音频放大器。

最初的诊断集中在无法正常工作的玩家输入上，怀疑是PSN PCB的问题。尽管在加利福尼亚州对PSN PCB和RSO PCB进行了台式测试和分析，但没有发现具体故障。还努力使用末日复制器设置数字化游戏的激光影碟，并保存PCB中的ROM数据，包括来自“佐尔加尔的进攻”转换的先前未转储的ROM和原始“龙计划”游戏的旧版本。

2025年3月的第二次旅行，增加了团队成员和诊断设备，旨在修复玩家输入问题，维修投影机，并找到丢失的ROM。该团队准备更充分地应对这些问题。令人惊讶的是，其中一个先前故障的PSN PCB开始工作。

---

## 7. Infisical (YC W23) 正在旧金山招聘设计工程师

**原文标题**: Infisical (YC W23) Is Hiring Design Engineer in San Francisco

**原文链接**: [https://www.ycombinator.com/companies/infisical/jobs/I8zvnRW-design-engineer-san-francisco](https://www.ycombinator.com/companies/infisical/jobs/I8zvnRW-design-engineer-san-francisco)

Infisical 正在招募设计工程师

Infisical 是一家开源密钥管理平台，也是 YC W23 毕业公司，现诚聘设计工程师加入其位于旧金山的团队。该职位专注于提升 Infisical 平台的用户体验，这是一个技术深度很高的产品，其产品理念的核心是用户和开发者体验。设计工程师将与创始人及工程团队紧密合作，将产品需求转化为直观的用户界面，开发可复用的 React 和 TypeScript 组件，确保性能和可访问性，并领导 Infisical PKI、SSH 和 KMS 等新产品线的前端架构。

理想的候选人需要具备 3 年以上 JavaScript 生态系统（React 和 TypeScript）经验、对细节和产品设计有极高的关注度、行动导向，并且熟悉 UI/UX 设计工具。具备 DevOps/开发者工具经验和出色的沟通能力者优先。

Infisical 提供具有竞争力的薪酬（年薪 14 万美元至 20 万美元，外加 0.10% 至 0.50% 的股权）、无限 PTO、免费午餐/晚餐、团队出游（如东京）、健康福利以及丰厚的设备津贴。公司获得了 Y Combinator、Google 和 Elad Gil 的支持，客户包括 Hugging Face、Lucid 和 LG。公司重视成长、所有权和解决具有挑战性的问题。Infisical 已融资 300 万美元，目标是扩展到数千名客户，目前的团队规模为 15 人。

---

## 8. Show HN: 新世界纪录 – 验证哥德巴赫猜想至 4*10^18+7*10^13

**原文标题**: Show HN: New world record – verified Goldbach Conjecture up to 4*10^18+7*10^13

**原文链接**: [https://medium.com/@jay_gridbach/grid-computing-shatters-world-record-for-goldbach-conjecture-verification-1ef3dc58a38d](https://medium.com/@jay_gridbach/grid-computing-shatters-world-record-for-goldbach-conjecture-verification-1ef3dc58a38d)

中田裕明宣布利用其自研网格计算系统Gridbach，在验证哥德巴赫猜想方面创造新的世界纪录。他已将验证范围扩展至400京+70万亿，超越了之前的400京纪录。

哥德巴赫猜想指出，每个大于2的偶数都可以表示为两个素数之和。虽然尚未得到数学证明，但中田的Gridbach系统通过计算验证了该猜想在更大范围内的正确性。

Gridbach是一个基于云的分布式计算系统，可通过PC和智能手机上的网络浏览器访问，无需登录或安装。它使用WebAssembly (WASM) 在用户浏览器上进行高效计算。用户通过在浏览器中运行计算来做出贡献，每个任务涵盖1亿个偶数的范围。

中田受到SETI@home的启发，旨在创建一个易于访问的系统，以激发人们对数学和IT的兴趣。他将“哥德巴赫脊”定义为满足哥德巴赫猜想的素数对中较小素数的最大值。

核心计算算法已以MIT许可证开源为Go命令行工具。中田计划将验证范围进一步推进到500京，并正在寻求关于如何正式承认该记录的指导。他鼓励读者参与并访问gridbach.com探索该系统。

---

## 9. Zack：基于Zig的简单回测引擎

**原文标题**: Zack: A Simple Backtesting Engine in Zig

**原文链接**: [https://github.com/zerotech-studio/zack](https://github.com/zerotech-studio/zack)

Zack：一个轻量级的回测引擎，用 Zig 编写，旨在针对历史市场数据模拟交易策略。Zig 的性能、内存控制和简洁性使其非常适合此应用。该引擎逐个处理 OHLCV 数据，模拟订单执行，管理虚拟投资组合并报告业绩。

Zack 的核心是由 BacktestEngine 管理的事件循环。它从 JSON 文件加载配置，解析 CSV 数据，并遍历每个数据条。对于每个数据条，策略（目前是一个简单的“买入并持有”策略）会根据预定义的规则和投资组合状态生成交易信号。如果生成了信号，Portfolio 会创建一个 Order，而 ExecutionHandler 会模拟订单成交，使用下一个数据条的开盘价引入一个数据条的延迟。然后，Portfolio 会更新其现金、仓位和持仓。

引擎的配置允许用户设置初始资本，选择策略，并指定数据文件。数据格式期望 OHLCV 数据为 CSV 格式。Zack 提供了一个清晰的项目结构，其中包含用于数据处理、策略逻辑、投资组合管理和执行模拟的独立模块。

要运行 Zack，用户需要安装 Zig，克隆存储库，并使用 Zig 构建系统。输出包括配置详细信息、策略设置和回测结果，如初始资本、最终权益、总回报和结束仓位。未来的增强功能包括更多的性能指标、策略、技术指标和全面的单元测试。欢迎贡献和建议。

---

## 10. 神经突

**原文标题**: Neurite

**原文链接**: [https://github.com/satellitecomponent/Neurite](https://github.com/satellitecomponent/Neurite)

Neurite是一个开源项目，致力于开发一种基于分形的数字界面，旨在增强创造性思维和知识管理。它将复杂的分形与思维导图技术相结合，为包括研究人员、艺术家和开发者在内的各类用户提供了一个几乎无限的工作空间。

其主要功能包括实时分形导航和自定义（曼德勃罗集、朱利亚集等），用于协同AI通信的多代理UI，以及用于结构化记忆映射和非线性记忆访问的FractalGPT。它还提供同步知识管理，在分形思维导图工作空间和Zettelkasten档案之间进行双向同步。用户可以在分形中嵌入各种媒体类型，利用基于物理学的图形，并集成外部知识来源，如Wolfram Alpha和维基百科。

Neurite桌面应用程序扩展了浏览器体验，允许用户在分形画布中打开多个浏览器窗口，并在没有沙盒限制的情况下浏览网站。一个实验性的神经API允许用户执行Neurite的代码序列和动画。

该平台鼓励社区贡献，并通过电子邮件和Discord提供沟通渠道。最终，Neurite旨在在动态且视觉上引人入胜的分形环境中，为思想组织、AI协作和交互式数据探索提供一种新颖的方法。

---

## 11. 展示 HN: Undercutf1 – 带有车手追踪器和可变延迟的F1实时计时 TUI

**原文标题**: Show HN: Undercutf1 – F1 Live Timing TUI with Driver Tracker, Variable Delay

**原文链接**: [https://github.com/JustAman62/undercut-f1](https://github.com/JustAman62/undercut-f1)

UndercutF1：一款开源的、基于终端（TUI）的应用程序，用于获取F1赛事实时计时数据。它使用UndercutF1.Data库连接到F1实时计时数据流，处理数据，并在用户友好的界面中显示。该应用程序允许延迟数据馈送，以与直播同步，解决典型的直播延迟问题。

主要功能包括：

*   **计时塔:** 实时分段计时、单圈信息、轮胎数据和差距。
*   **相对差距:** 显示与选定车手的差距，用于策略分析。
*   **进站策略:** 概览车手轮胎策略。
*   **赛事控制:** 显示消息、处罚和天气更新。
*   **车手追踪:** 显示车手位置的实时赛道地图（iTerm2/Kitty 终端）。
*   **逐圈历史:** 计时塔快照，用于分析比赛进程。
*   **车队无线电:** 收听车队无线电片段，并使用Whisper进行转录。

UndercutF1可以作为.NET工具、独立可执行文件安装，或者直接从源代码运行。它支持直播会话和预录数据的重放，并提供下载和重放历史会话数据的选项。该应用程序通过config.json文件、命令行参数或环境变量提供配置选项。它记录详细信息用于调试和分析。

该项目从FastF1获得灵感，并感谢其对理解F1实时计时数据流的贡献。

---

## 12. 弗兰肯斯坦的`__init__`

**原文标题**: Frankenstein's `__init__`

**原文链接**: [https://ohadravid.github.io/posts/2025-04-19-frank/](https://ohadravid.github.io/posts/2025-04-19-frank/)

文章幽默地讲述了作者调试一个Python类`FooBarWidget`中以一种怪异方式实现的`__init__`方法的过程。最初的问题是`FooBarWidget`的一个测试用例失败，间歇性地抛出`AttributeError`，提示缺少`should_exit`属性，尽管父类`FooWidget`已经明确地初始化了该属性。

调查显示，`FooBarWidget`的`__init__`方法会启动一个新的线程，然后在该线程中调用`FooWidget.__init__`。这意味着，如果测试代码的`contextlib.closing`过快地关闭了`FooBarWidget`实例，就可能发生在独立线程中的`FooWidget.__init__`完成设置`should_exit`属性*之前*。

作者强调了这种方法的荒谬性，将其描述为“完全无视理智”。这种不寻常的实现源于ZeroMQ的一个限制：`zmq.Socket`对象不能在线程之间移动。`FooBarWidget`需要`FooWidget`的初始化（它会创建一个`zmq.Socket`），并且`run`方法需要在单独的线程中执行，以避免阻塞主线程。作者的以弗兰肯斯坦为主题的比喻强调了这个通过解决一个问题同时创造新的、意想不到的问题而诞生的怪物。

---

## 13. 英国方言地图 (2023)

**原文标题**: A Map of British Dialects (2023)

**原文链接**: [https://starkeycomics.com/2023/11/07/map-of-british-english-dialects/](https://starkeycomics.com/2023/11/07/map-of-british-english-dialects/)

本文详细介绍了一幅英国英语方言地图，该地图由作者历经多年研究和同行反馈后制作而成。该地图旨在捕捉英国和皇家属地（不包括爱尔兰）内方言多样性的细微差别，并承认即使在短距离内，语言也存在显著差异。

作者强调了该地图固有的局限性和潜在的不准确性。“方言”的定义是主观的，它们之间的界限很少是明确的，通常是逐渐融合的。该地图简化了一个复杂的现实，无法代表村庄、城镇甚至街道之间的细微差别。此外，一些方言，如多元文化伦敦英语，并非地域性的，而是受到文化和社会经济因素的影响。

作者还阐明了出于地图目的“英国”的定义范围，侧重于英国和皇家属地内的英语方言，并说明了纳入北爱尔兰的理由，以及排除苏格兰语/多利克语（它们被认为是独立的语言，尽管密切相关）的理由。

最终，该地图被视为英国丰富语言多样性的证明，在承认其不完善的同时，表达了作者对这种多样性的着迷和热爱。作者鼓励读者在其网站上探索其他相关地图和资源，并通过Patreon支持他们的工作。

---

## 14. 如何从零开始用张量核心编写快速矩阵乘法

**原文标题**: How to Write a Fast Matrix Multiplication from Scratch with Tensor Cores

**原文链接**: [https://alexarmbr.github.io/2024/08/10/How-To-Write-A-Fast-Matrix-Multiplication-From-Scratch-With-Tensor-Cores.html](https://alexarmbr.github.io/2024/08/10/How-To-Write-A-Fast-Matrix-Multiplication-From-Scratch-With-Tensor-Cores.html)

在NVIDIA Tesla T4 GPU上使用Tensor Core优化CUDA矩阵乘法(HGEMM)内核的作者实践

---

## 15. 秘鲁古代灌溉系统因文化将沙漠变为农田。

**原文标题**: Peru's ancient irrigation systems turned deserts into farms because of culture

**原文链接**: [https://theconversation.com/perus-ancient-irrigation-systems-succeeded-in-turning-deserts-into-farms-because-of-the-culture-without-it-the-systems-failed-251199](https://theconversation.com/perus-ancient-irrigation-systems-succeeded-in-turning-deserts-into-farms-because-of-the-culture-without-it-the-systems-failed-251199)

本文考察了前哥伦布时期秘鲁干旱北部沿海地区灌溉系统的成功之处，认为其有效性不仅源于技术，还源于其中蕴含的文化习俗和知识体系。现代灌溉工程虽然看似成功地创造了一个农业工业中心地带，但却很脆弱，并受到包括冰川融化和洪水增加在内的气候变化的威胁。作者将现代方法与莫奇和奇穆社会的古代系统进行了对比，这些古代系统将大规模基础设施与适应性强的多功能设计相结合。这些古代系统结合了洪水改道、泥沙截留和地下水位补给，确保了在极端条件下的韧性。西班牙殖民者未能复制这些系统的成功，突显了文化知识的重要性；他们采用了技术，但缺乏对其与劳动系统、维护实践和洪水管理策略的相互联系的理解。作者认为，像查维莫奇克项目这样的现代项目，可能会以牺牲长期可持续性为代价来追求短期利益，因为它们忽视了古代实践中蕴含的文化和生态智慧。文章最后强调，为了为秘鲁的未来创造真正具有气候适应能力的解决方案，有必要纳入土著知识，保护文化遗产，并与当地社区建立信任。

---

## 16. OS X 下的 USB 软盘条带 RAID (2004)

**原文标题**: USB Floppy Disk Striped RAID Under OS X (2004)

**原文链接**: [http://web.archive.org/web/20040202110812/http://ohlssonvox.8k.com/fdd_raid.htm](http://web.archive.org/web/20040202110812/http://ohlssonvox.8k.com/fdd_raid.htm)

使用软盘驱动器打造条带化RAID阵列：一个趣味实验

---

## 17. 安卓手机将在闲置三天后自动重启。

**原文标题**: Android phones will soon reboot themselves after sitting unused for three days

**原文链接**: [https://arstechnica.com/gadgets/2025/04/android-phones-will-soon-reboot-themselves-after-sitting-unused-for-3-days/](https://arstechnica.com/gadgets/2025/04/android-phones-will-soon-reboot-themselves-after-sitting-unused-for-3-days/)

一项Google Play服务更新（v25.14）正在向几乎所有Android设备推出，它将为已锁定且连续三天未使用的手机引入自动重启功能。此功能类似于iOS中的Apple“非活动重启”，旨在通过限制手机保持在易受攻击的未加密状态的时间来增强安全性。

当手机刚重启并处于“首次解锁前”（BFU）状态时，生物识别和基于位置的解锁将被禁用，需要密码或PIN码才能访问。至关重要的是，在此状态下所有数据都已加密，这使得包括执法部门在内的未经授权的个人更难以提取数据。

此次更新将通过Google Play服务静默到达，绕过速度较慢的Android系统更新流程。虽然人们对Google通过Play服务控制Android感到担忧，但此次更新通过更频繁地自动加密用户数据，即使设备已插电，也能提供显著的安全性益处。此次更新还包括其他小改进，如更美观的设置、与汽车和手表的更好连接以及“快速分享”中的内容预览。

---

## 18. 15,000行经验证的密码学代码现已提供Python版本

**原文标题**: 15,000 lines of verified cryptography now in Python

**原文链接**: [https://jonathan.protzenko.fr/2025/04/18/python.html](https://jonathan.protzenko.fr/2025/04/18/python.html)

本文详细介绍了将 HACL* 库中经过验证的 15,000 行密码学代码成功集成到 Python 中的过程，取代了其现有的哈希和 HMAC 算法。作者主导了这项为期 2.5 年的工作，该工作是在 Python 的 SHA3 实现中的一个 CVE 突显了对经过验证的代码的需求后启动的。

对于 Python 用户来说，过渡是无缝的，没有功能损失。HACL* 经过调整以满足 Python 的要求，包括新的 Blake2 模式、全面的 SHA3 API、特定的构建系统抽象、错误管理和优化的 HMAC 实现。主要贡献者包括 Aymeric Fromherz、Son Ho、Gregory P. Smith、Bénédikt Tran 和 Chris Eibl，并得到了 HACS workshop 社区的支持。

本文深入探讨了为具有不同要求的块算法创建通用、经过验证的流式 API 的技术挑战。这涉及处理可变的摘要长度、预输入、状态保持和内存分配失败。作者强调了在 Python 广泛的 CI 基础设施上实现“万无一失构建”的难度，尤其是在处理 AVX2 优化和从 F* 自动生成的抽象 C 结构时。

成功集成证明了经过验证的密码学在实际软件开发中的成熟性和实用性。现在可以通过一个简单的 shell 脚本轻松地将上游 HACL* 更新集成到 Python 中，从而简化了维护。作者对这一里程碑表示高兴，并强调了使其成为可能的协作努力。

---

## 19. 美国法院记录全文搜索

**原文标题**: Full Text Search of US Court records

**原文链接**: [https://www.judyrecords.com/](https://www.judyrecords.com/)

本文介绍了JudyRecords，一个提供超过7.4亿份美国法院案件免费公开记录搜索的平台。该网站提供免费访问法院记录的服务，并重点介绍了该平台的主要方面，包括其使用条款、一个“信息”部分（可能包含关于该服务的更多细节）以及一个API（应用程序编程接口），表明开发者有可能将该服务集成到其他应用程序中。标题强调了该平台对这些记录的全文本搜索能力。本质上，JudyRecords将自身定位为免费访问和搜索美国法院案件信息的全面资源。

---

## 20. Haujobb 和 Sweet16 的演示曲 "The Mind"

**原文标题**: Demo "The Mind" by Haujobb and Sweet16

**原文链接**: [https://www.lexaloffle.com/bbs/?pid=145596](https://www.lexaloffle.com/bbs/?pid=145596)

本文宣布发布由 Haujobb & Sweet16 为 Revision demoparty “幻想主机”竞赛创作的新演示作品《The Mind》。该演示使用 Pico-8 构建，并利用了多卡带功能，最初仅限于在线观看。

完整的源代码可在 Pouet 下载，作者 “hellfire” 建议在 Windows 上使用 Firefox 以获得更好的性能。本文还包括演示的 YouTube 视频链接以及解释音乐制作过程的视频。

提供了在 Pico-8 中直接运行演示的说明：使用命令 `load #themind1` 和 `run`，该命令会从 BBS 下载并存储必要的数据卡带。 感谢更新，该演示现在可以直接在 BBS 本身内运行。

本文还强调，演示中的一些视觉效果经过改进后已作为单独的文件发布，其中包含干扰和神经网络视觉效果。该演示的标签包括“demoscene”、“revision”、“3d 多边形”和“像素艺术”。 文中提供了一个直接在 Lexaloffle BBS 中播放演示的链接，并提示用户需要登录才能发表评论。

---

## 21. “宇宙无线电”探测器或在15年内发现暗物质

**原文标题**: 'Cosmic radio' detector could discover dark matter within 15 years

**原文链接**: [https://phys.org/news/2025-04-cosmic-radio-detector-dark-years.html](https://phys.org/news/2025-04-cosmic-radio-detector-dark-years.html)

一种名为轴子准粒子(AQ)的新型“宇宙无线电”探测器，有望在15年内发现暗物质。这是伦敦国王学院、哈佛大学、加州大学伯克利分校等机构研究人员的观点。发表在《自然》杂志上的文章描述了AQ探测器的设计，旨在“调谐”到太赫兹范围内轴子的特定频率，轴子是暗物质的主要候选者。该探测器的工作原理是，当它识别并匹配到轴子的频率时，就会发出光。

AQ由锰铋碲(MnBi₂Te₄)制成，这是一种具有独特电子和磁性能的材料，被削减到几个二维层。研究人员认为，可以在五年内建造更大块的AQ材料，然后在十年内扫描高频范围，以精确定位轴子的位置。

伦敦国王学院的David Marsh博士强调，该探测器类似于“宇宙汽车收音机”，可以调谐到银河系的频率来寻找轴子。哈佛大学的主要作者邱建翔强调了MnBi₂Te₄的敏感性，需要剥离到原子层才能进行精确的性能调整并观察其与轴子等量子实体的相互作用。研究人员对暗物质研究的未来持乐观态度，并指出人们对轴子的关注日益增加。

---

## 22. 微型轮腿机器人

**原文标题**: Micro Wheeled legged Robot

**原文链接**: [https://github.com/MuShibo/Micro-Wheeled_leg-Robot](https://github.com/MuShibo/Micro-Wheeled_leg-Robot)

本文档详细介绍了一个自制的、微型双轮腿式机器人，它由ESP32供电，并使用simpleFOC驱动无刷电机。该机器人使用L6234PD013TR电机驱动器、AS5600编码器进行车轮反馈（通过I2C通信）以及MPU6050 IMU用于平衡。该设计包括可下载的3D模型和PCB原理图（使用LCEDA）用于制造。零件分为“自制零件”（3D打印、CNC、面板切割）和“采购零件”。

控制通过Web界面实现，利用ESP32的WiFi功能，可选择AP（热点）或STA（客户端）模式，并通过WebSocket通信。代码基于Arduino IDE，并需要WebSocket库（推荐esp32版本2.0.3）。

操作包括连接电池、开启设备并使其初始化。通过EN按钮重启后，用户可以连接到机器人的WiFi网络，并访问192.168.1.11上的远程控制界面。该界面可从各种操作系统和浏览器访问。然后，用户手动稳定机器人，点击网页上的“Robot go!”以启动平衡，并使用屏幕上的摇杆控制其运动。

该项目是开源的，鸣谢Mu Shibo和Li Yufeng的贡献。

---

## 23. 氧化亚氮的漫长历史

**原文标题**: The Long History of Nitrous Oxide

**原文链接**: [https://www.smithsonianmag.com/science-nature/the-long-strange-history-of-nitrous-oxide-a-popular-drug-users-have-been-inhaling-for-hundreds-of-years-180986293/](https://www.smithsonianmag.com/science-nature/the-long-strange-history-of-nitrous-oxide-a-popular-drug-users-have-been-inhaling-for-hundreds-of-years-180986293/)

本文探讨了一氧化二氮漫长而复杂的历史，从18世纪的发现到其作为娱乐性药物的现代复兴。文章详细介绍了汉弗莱·戴维的最初实验，以及这种气体在19世纪知识分子和表演者中的流行，以及最终被牙科采用作为麻醉剂的过程。

文章随后转向现代背景，强调了对银河气体等调味一氧化二氮产品在社交媒体趋势的推动下，向年轻人营销的担忧。专家们讨论了娱乐性使用一氧化二氮的危险，包括缺氧、维生素B12缺乏以及潜在的神经损伤，同时也指出了可能产生的心理依赖性。

文章还探讨了一氧化二氮的监管挑战，由于其作为烹饪和医疗用途合法销售，从而产生了一个允许娱乐性使用的漏洞。尽管一些州已开始限制销售，但其他州反对禁酒式的方法，认为公开沟通和教育更为有效。文章最后强调了关于如何监管一氧化二氮的持续辩论，强调了其在科学、文化和法律交叉口上的独特地位。

---

## 24. 展示HN：我做了一个能放进二维码里的类Doom游戏

**原文标题**: Show HN: I made a Doom-like game fit inside a QR code

**原文链接**: [https://github.com/Kuberwastaken/backdooms](https://github.com/Kuberwastaken/backdooms)

这篇"Show HN"帖子详细介绍了“后门毁灭战士 (The Backdooms)”的创作过程，这是一个完全包含在二维码中的可玩类DOOM游戏。该项目展示了一种托管轻量级Web应用程序的创新方法。作者Kuber Mehta开发这款游戏用时一周，旨在探索二维码存储和压缩的极限。

游戏完全离线，扫描后无需网络连接。它利用了极限压缩技术，包括采用Gzip解压缩的Zlib压缩和Base64编码，将文件大小最小化到大约2.5kb。一个自解压的HTML包装器利用浏览器的DecompressionStream API来动态解压缩和执行游戏。它与支持此API的移动浏览器（Edge、Yandex、Opera）兼容。

该帖子提供了有关如何使用Python、`qrcode`库和`pillow`将其他HTML游戏转换为二维码的说明。它详细介绍了从读取HTML到生成二维码的压缩工作流程，包括数据过大时的错误处理。该项目以MIT许可证开源，作者鼓励其他人探索创建二维码游戏。感谢id Software（DOOM）、matttkc（灵感）和Toby Fox（GitHub托管版本中使用的Undertale音乐）。作者邀请读者访问其博客，以了解有关开发过程的更多信息。

---

## 25. 是时候解决耐药性真菌感染问题了

**原文标题**: High time to tackle drug-resistant fungal infections

**原文链接**: [https://www.nature.com/articles/d41586-025-01177-x](https://www.nature.com/articles/d41586-025-01177-x)

这篇《自然》杂志的文章强调了耐药性真菌感染日益增长的威胁，尤其是耳念珠菌（*Candida auris*），以及采取行动的紧迫性。真菌感染每年导致数百万人死亡，这一数字在过去十年几乎翻了一番。世界卫生组织强调了对此问题的忽视，指出处于后期研发阶段的抗真菌药物数量有限。

文章指出，由于真菌细胞与人类细胞的相似性，开发抗真菌药物面临挑战，这使得在不损害人类的情况下靶向真菌通路变得困难。文章强调，必须投资于基础研究，以识别新的药物靶点，并了解真菌遗传学，从而检测新兴菌株和耐药机制。

文章还讨论了政策挑战，特别是农业杀菌剂的使用可能导致对医学上重要的抗真菌药物产生耐药性。文章强调了一些国家为解决这个问题所做的努力，例如印度禁止某些抗生素用于植物保护，以及美国环保署在杀菌剂评估中考虑耐药性风险。欧盟也在审查唑类杀菌剂的影响。

文章最后强调，工业界、政府和慈善基金会需要合作，以支持研究并制定战略来对抗耐药性真菌感染，包括了解导致耳念珠菌等新型真菌病原体出现的条件。

---

## 26. 反对透明化

**原文标题**: Against Transparency

**原文链接**: [https://pluralistic.net/2025/04/19/gotcha/#known-to-the-state-of-california-to-cause-cancer](https://pluralistic.net/2025/04/19/gotcha/#known-to-the-state-of-california-to-cause-cancer)

科里·多克托罗的《反对透明化》认为，以警告和政策形式呈现的透明化往往不足以保护消费者免受伤害和剥削。他以加州65号提案警告为例，这些警告无处不在，以至于变成了毫无意义的背景噪音，未能阻止人们接触潜在的致癌物。同样，他批评隐私政策，认为它们普遍被忽视，实际上是允许公司犯下严重的侵犯隐私行为。

多克托罗认为，仅仅告知消费者潜在的风险，并期望他们“用钱包投票”，是将不合理的负担强加于个人，让他们在复杂的信息中做出知情决定。他主张制定更强有力的法规，主动减少危害，例如要求制造商通风处理潜在的致癌产品，或实施强有力的隐私法，限制公司对个人数据的使用。

他赞扬了消费者金融保护局（CFPB），特别是在罗希特·乔普拉的领导下，积极追查诈骗者，并创建创新举措来保护消费者。他认为埃隆·马斯克和那些与特朗普结盟的人对CFPB的攻击证明了他们渴望优先考虑利润而不是消费者安全和公平，“买者自负”成为剥削的理由。多克托罗提出了马克·莱姆利关于合同“默认规则”的观点，以使协议对消费者来说更短、更清晰、更合理，强调需要积极的监管来保护个人免受掠夺性行为的侵害。

---

## 27. 理解Vi和Vim的起源与演变

**原文标题**: Understanding the Origins and the Evolution of Vi and Vim

**原文链接**: [https://pikuma.com/blog/origins-of-vim-text-editor](https://pikuma.com/blog/origins-of-vim-text-editor)

本文记录了 vi 和 Vim 文本编辑器的演变历程，追溯了它们在 UNIX 早期的起源。它从 Ken Thompson 为电传打字机创建的行编辑器 ed 开始，ed 启发了 George Coulouris 在英国第一台 UNIX 设备所在地——玛丽皇后大学开发了 em（“大众版 Ed”）。加州大学伯克利分校的 Bill Joy 受 em 的启发，创建了 en，然后是 ex，最终创建了 vi，它为 ex 添加了全屏可视模式。Vi 的设计深受缓慢的 300 波特调制解调器和 ADM-3A 终端键盘布局的限制。

文章随后讨论了 vi 的克隆版本，如 Stevie（为 Atari ST 开发）和 Elvis，它们引入了语法高亮等功能。最后，文章提到了最初由 Bram Moolenaar 为 Commodore Amiga 开发的 Vim。Vim 最初是“Vi IMitation”，后来演变为“Vi IMproved”，并因其无需 AT&T 源代码许可即可使用以及 Moolenaar 对慈善软件的奉献而广受欢迎。文章重点介绍了 Vim 的关键里程碑，包括其移植到 UNIX、GUI 的添加、语法高亮以及其活跃的开发。文章最后强调了 Vim 通过插件和 VimScript 的可扩展性，突出了其在软件开发领域持久的相关性。文章还缅怀了 Vim 的创造者 Bram Moolenaar 近期的逝世。

---

## 28. JavaScript视图：困难的方式 – 一种编写用户界面的模式

**原文标题**: JavaScript Views, the Hard Way – A Pattern for Writing UI

**原文链接**: [https://github.com/matthewp/views-the-hard-way](https://github.com/matthewp/views-the-hard-way)

用原生JavaScript“硬核”编写视图：介绍一种使用纯JavaScript构建UI组件的模式，作为React或Vue等框架的替代方案。它强调直接性和对抽象的控制，旨在提高性能、可维护性和可移植性。

该方法使用`template`元素来定义视图的HTML结构，然后进行克隆。一个`init`函数创建一个视图实例并返回一个`update`函数来处理prop更新。`init`函数被组织成以下几个部分：

*   **DOM变量：**缓存DOM节点以便操作。
*   **DOM视图：**实例化子视图。
*   **状态变量：**保存驱动视图状态的数据。
*   **DOM更新函数：**封装DOM操作，确保每个节点只有一个更改点。
*   **状态更新函数：**修改状态变量，并在必要时才触发相应的DOM更新，防止不必要的DOM操作。

这种模式通过严格控制DOM突变和状态更改的发生位置，从而优先考虑清晰性和可调试性。优势包括零依赖、浏览器支持、易于调试以及使用纯函数进行函数式风格的编码。它遵循props-down, events-up模型，使数据共享简单明了，并能产生更易于维护的代码。

---

## 29. AI设计的抗蛇毒血清：阻断致命蛇毒的新型蛋白质

**原文标题**: AI-Designed Antivenoms: New Proteins to Block Deadly Snake Toxins

**原文链接**: [https://plentyofroom.beehiiv.com/p/antivenoms-with-ai-designed-proteins](https://plentyofroom.beehiiv.com/p/antivenoms-with-ai-designed-proteins)

AI设计抗蛇毒血清：阻断致命蛇毒的新型蛋白质

---

## 30. 轻松的电子游戏可以缓解压力和焦虑。

**原文标题**: Cozy video games can quell stress and anxiety

**原文链接**: [https://www.reuters.com/business/retail-consumer/cozy-video-games-can-quell-stress-anxiety-2025-01-27/](https://www.reuters.com/business/retail-consumer/cozy-video-games-can-quell-stress-anxiety-2025-01-27/)

以低风险玩法、温和主题和舒缓视觉效果为特点的治愈系电子游戏，正日益被认为是管理压力和焦虑的工具。《路透社》的文章强调了这一游戏类型的日益普及，尤其是在寻求摆脱现代生活压力的年轻群体中。

文章强调了治愈系游戏与传统的、更具竞争性的游戏之间的区别。治愈系游戏通常侧重于耕作、制作、与游戏角色建立关系以及探索赏心悦目的环境等活动，而不是战斗、竞争或复杂的情节。受欢迎的游戏例子包括《动物森友会》、《星露谷物语》和《拆箱》。

文章引用的专家指出，这些游戏重复、可预测的特性，加上缺乏高风险，本质上可以起到舒缓作用。玩家在没有输赢压力的情况下体验到控制感和成就感，这对容易焦虑的人尤其有益。轻柔的配乐和视觉上吸引人的画面进一步增强了镇静效果。

此外，文章指出，某些治愈系游戏中的社交元素，例如在《动物森友会》中拜访朋友的岛屿，可以培养社区和联系感，进一步缓解孤独和压力感。然而，文章也警告说，不要将治愈系游戏完全替代专业的心理健康治疗，强调它们是管理压力的辅助工具，而不是治疗方法。总的来说，这些游戏为许多人提供了一种健康且易于获得的放松和减轻焦虑的方式。

---

## 31. Claude代码最佳实践

**原文标题**: Claude Code Best Practices

**原文链接**: [https://www.anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)

我能够访问互联网，现在将总结提供的URL中的文章：

**“Claude代码最佳实践”摘要：**

Anthropic的“Claude代码最佳实践”一文详细介绍了有效利用Claude语言模型进行代码生成和操作的策略。它侧重于提示技巧和架构模式，以获得最佳结果。

主要内容包括：

*   **明确的指令：** 向Claude提供非常具体和详细的指令，包括所需的编程语言、预期行为和约束。 模糊性会导致不太理想的结果。

*   **小样本学习：** 包含输入-输出对的示例，以指导Claude的生成。 这些示例充当所需编码风格和功能的“演示”。

*   **结构化提示：** 使用结构化提示格式，例如将问题分解为子任务或指定输入和输出模式。 这有助于Claude更好地理解任务的复杂性。

*   **代码分解：** 对于大型或复杂的任务，将问题分解为更小、更易于管理的功能或模块。 这使Claude能够专注于单个组件并提高可维护性。

*   **迭代和改进：** 将Claude视为协作者。 审查其生成的代码，提供反馈，并迭代提示以改进输出。 不要期望在第一次尝试中获得完美的代码。

*   **测试和验证：** 彻底测试和验证Claude生成的代码。 它不能替代人工审查和测试。

*   **文档记录和注释：** 明确要求Claude在生成的代码中包含注释和文档，以提高可读性和可维护性。

*   **架构模式：** 利用已建立的架构模式（如MVC）来改进代码结构。 在适当的指导下，Claude可以协助实施这些模式。

本质上，这篇文章强调了将Claude视为一种强大的工具的重要性，该工具需要清晰的指令、仔细的指导和人工监督才能生成高质量的代码。 它强调，通过精心设计的提示进行有效沟通对于成功的代码生成至关重要。

---

## 32. 海洋铁施肥

**原文标题**: Ocean Iron Fertilization

**原文链接**: [https://www.whoi.edu/know-your-ocean/ocean-topics/climate-weather/ocean-based-climate-solutions/iron-fertilization/](https://www.whoi.edu/know-your-ocean/ocean-topics/climate-weather/ocean-based-climate-solutions/iron-fertilization/)

铁施肥是一种二氧化碳移除（CDR）技术，它通过向海洋表面添加铁来刺激浮游植物生长，模仿尘暴等自然现象。浮游植物在光合作用过程中消耗大气中的二氧化碳，从而可能减轻气候变化的影响。研究表明，富含铁的尘埃与过去全球气温和二氧化碳水平的降低有关。

20世纪90年代和21世纪初的实验表明，铁施肥会导致浮游植物大量繁殖。硅藻是一种浮游植物，由于其体积大、生长快以及死后有助于下沉的硅壳，在碳封存方面特别有效。然而，人们担心可能对海洋生态系统造成改变，包括有害藻类爆发和养分分配。

尽管早期的铁施肥实验遇到了阻力，但科学家们正在重新考虑将该技术作为一种有价值的CDR工具。目前的努力集中在开发透明的研究协议，以更好地了解预期和非预期的后果。新技术正在推动对碳移除及其在海洋中运动的更全面研究。

铁施肥相对便宜，可能成为更广泛的CDR战略的关键组成部分。然而，必须记住，铁施肥不能取代大幅减少化石燃料的使用，化石燃料才是大气二氧化碳的主要来源。

---

## 33. 实战大型语言模型

**原文标题**: Hands-On Large Language Models

**原文链接**: [https://github.com/HandsOnLLM/Hands-On-Large-Language-Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models)

《动手学大型语言模型》（又名《图解LLM书》）是Jay Alammar和Maarten Grootendorst撰写的指南，旨在教授使用大型语言模型（LLM）的实用工具和概念。本书包含视觉教育内容，配有近300个定制图表，并在GitHub存储库中提供代码示例。

本书涵盖的主题包括：语言模型简介、Tokens和嵌入、Transformer LLM、文本分类、文本聚类和主题建模、提示工程、文本生成、语义搜索和检索增强生成（RAG）、多模态LLM、创建文本嵌入模型、微调表示模型以及微调生成模型。

作者建议使用Google Colab进行示例，因为它提供免费的T4 GPU。该存储库还包括使用conda和PyTorch进行本地安装的设置指南。

本书因其清晰的解释、实用的示例和对LLM的全面覆盖而受到Andrew Ng、Nils Reimers和Josh Starmer等专家的好评。在奖励文件夹中提供了额外的资源，包括关于Mamba、量化、Stable Diffusion、专家混合、推理LLM和DeepSeek-R1等主题的可视化指南。正文以本书的引用结尾。

---

## 34. 钩针编织的中心装饰品和午餐套装（1915年）

**原文标题**: Center Pieces and Lunch Sets in Crochet Work (1915)

**原文链接**: [https://www.gutenberg.org/cache/epub/75880/pg75880-images.html](https://www.gutenberg.org/cache/epub/75880/pg75880-images.html)

本文档是安妮·奥尔于1915年出版的钩针图案书籍《钩针编织的中心装饰品和午餐套装》的数字化版本。它提供了制作各种钩针编织的中心装饰品和午餐套装的说明。

本书首先介绍了基本的钩针针法，包括锁针、短针、长针、中长针、狗牙针和引拔针，以及贯穿所有图案的缩写列表。

主要内容包括几个项目的详细说明，每个项目都附有相应的插图。这些说明包括材料清单，指定了所需的钩针棉线的类型和数量，以及合适的钢制钩针针号。图案涵盖了一系列设计，包括：

*   一个以小、中、大圆形花饰为特色的中心装饰品。
*   一个带有叶子图案的中心装饰品。
*   一个18英寸的带有几何设计的中心装饰品。
*   一个27英寸的包含菠萝和三叶草元素的中心装饰品。
*   一个27英寸的带有花卉设计的中心装饰品。

对于每个项目，说明都按行分解，提供关于针法位置、锁针长度和连接技术的精确指导。本书面向具有一定钩针经验的个人，因为它假定读者熟悉基本的钩针术语。

---

## 35. 超文本电视

**原文标题**: Hypertext TV

**原文链接**: [https://hypertext.tv/](https://hypertext.tv/)

超文本电视呈现了一种独特的、基于文本的电视界面。主屏幕让人联想到早期的计算机界面和阴极射线管电视，它充当通往各种在线内容流的门户，这些内容流被分类为“频道”。该界面允许用户导航（↑↓←→）并调整扫描线、亮度、颜色、色调、水平和垂直对齐等设置，进一步增强复古美学。

这些频道内容多样，提供游戏（“精致尸体俱乐部”）、艺术（“textmode.art”）、音乐（“N10.AS RADIO”）、个人直播（Ben West、Anh Vu）、诗歌（“Spoilia”）、一次性工具（“鼠标指针”）、可探索内容（“拟声词奥德赛”）、档案（“The HTML Review”）和各种其他内容（“Plaintext Distro”）。显示屏上可见时间（下午 5:28:49，预计节目在下午 5:30、6:00 和 6:30 开始），表明提供实时或预定内容。

该界面还提供添加网站或报告问题的选项，表明这是一个交互式的、可能由用户支持的平台。“电视指南测试人员名单”的存在表明该系统要么正在开发中，要么是作为一个艺术项目呈现的。本质上，“超文本电视”提供了一种怀旧且精心策划的浏览体验，弥合了经典电视界面和现代在线内容之间的差距。

---

## 36. 氢能巴士与电池巴士：欧洲公交的现实检验

**原文标题**: Hydrogen vs. Battery Buses: A European Transit Reality Check

**原文链接**: [https://cleantechnica.com/2025/04/14/hydrogen-vs-battery-buses-a-european-transit-reality-check/](https://cleantechnica.com/2025/04/14/hydrogen-vs-battery-buses-a-european-transit-reality-check/)

本文对欧洲氢燃料公交车的部署进行了现实性检验，并将其性能与纯电动公交车进行了比较。文章重点介绍了布鲁塞尔和阿伯丁等城市由于燃料成本高昂、供应不稳定以及基础设施挑战而导致的多个氢燃料公交车试验失败案例。布鲁塞尔放弃了氢燃料公交车试验，转而支持纯电动公交车，而阿伯丁的氢燃料公交车队由于氢气短缺而一直处于停用状态。

文章还讨论了科隆和欧塞尔等罕见的“成功”案例。科隆得益于工业副产品氢气，尽管氢气泄漏仍然是一个问题，并且已经开始整合纯电动公交车。欧塞尔拥有专门的绿色制氢站，但仅运营一支小型车队。其他常被认为是成功的城市，如伍珀塔尔、博尔扎诺和荷兰北部，事实上，尽管最初进行了氢能投资，但正越来越专注于扩大其纯电动车队。

文章还考察了埃森和米尔海姆、波城和蒙彼利埃的 проблемные 试验。埃森和米尔海姆面临补贴撤回，导致运营成本增加。波城由于氢燃料成本高昂和技术问题，正在过渡到纯电动公交车，而蒙彼利埃由于成本问题取消了一个大型氢燃料公交车项目，转而选择纯电动替代方案。即使是伦敦，虽然仍在运营其 20 辆氢燃料公交车车队，但已将其新的采购转向纯电动车型。文章总结说，尽管取得了一些有限的成功，但总的来说，纯电动公交车正在被证明是欧洲一种更可行且更具成本效益的零排放交通解决方案。

---

## 37. 赛博朋克1958：波兰IT产业的早期

**原文标题**: Cyberpunk 1958: The Early Days of the Polish IT Industry

**原文链接**: [https://culture.pl/en/article/cyberpunk-1958-the-early-days-of-the-polish-it-industry](https://culture.pl/en/article/cyberpunk-1958-the-early-days-of-the-polish-it-industry)

无法访问文章链接。

---

## 38. 游艇运作原理：帆船物理学与设计

**原文标题**: How a yacht works: sailboat physics and design

**原文链接**: [https://www.onemetre.net/Design/Design.htm](https://www.onemetre.net/Design/Design.htm)

游艇工作原理：帆船物理学与设计
本文深入探讨了控制帆船性能的物理学和工程学之间的复杂相互作用。 它系统地分解了航行背后的科学，从翼型和升力产生的基本原理开始，并通过动量理论和环流理论等各种理论模型进行解释。

内容广泛涵盖了鳍和帆的功能，考察了纵横比、冲刷、平面涡流、边界层以及压浪、扭曲和狭缝效应的重要性等因素。 它探讨了帆截面升力、狭缝效应以及压浪角度和边界层的风洞分析。

文章的很大篇幅用于分析游艇在不同航行角度下的运作方式，例如顺风航行、船体速度、逆风航行、升力和阻力以及视风。 同时讨论了风梯度、扭曲和大船仪器的影响，以及不同航行配置的风洞比较。 然后，本文深入探讨了航向定理、指向角、阻力角和航速增益 (VMG) 等关键概念。

附体的设计得到了彻底的剖析，包括对鳍和舵尺寸、平面形状、截面、平衡和球鼻艏尺寸/形状的考量，甚至提供了一个球鼻艏计算器。 还考察了船体设计，考虑了傅汝德数、表面摩擦、兴波阻力、船体线型、稳心距、边界层行为以及船体周围的流动，以及控制湍流的方法。

最后，本文探讨了帆和索具的设计，讨论了诸如帆索、跳板、支索、撑杆、桅杆相互作用、前桅支索下垂、风阻、鹅颈几何形状、帆弧度以及间隙和扭曲的影响等要素。 本文将船只作为一个整体来考虑，考察了平衡性、稳定性、环境因素、权衡取舍以及级别规则的影响。 此外，还涉及了索具调整、压舷以及简单的速度预测程序 (VPP)。

---

## 39. Show HN: Parqv – 交互式 TUI Parquet 可视化工具

**原文标题**: Show HN: Parqv – Interactive TUI Parquet Visualizer

**原文链接**: [https://github.com/sanspareilsmyn/parqv](https://github.com/sanspareilsmyn/parqv)

Parqv：用于在终端中探索 Parquet 文件的交互式 TUI 工具。

主要功能包括：

*   **交互式 TUI：** 提供 Parquet 文件的全面视图。
*   **元数据面板：** 显示文件信息，如路径、创建者和压缩。
*   **模式浏览器：** 提供模式的交互式、可折叠树视图，并带有语法高亮显示。
*   **数据表格查看器：** 显示数据的可滚动预览，按需加载页面以处理大型文件。
*   **行组检查器：** 列出行组及其关键统计信息，并允许检查每列的详细信息。
*   **动态统计：** 生成详细的列统计信息和分布。

Parqv 需要 Python 3.10 或更高版本，可以使用 `pip install parqv` 安装。 使用 `parqv /path/to/your/data.parquet` 启动。 使用箭头键、Tab 键、Enter 键和视图切换键进行导航。 该工具已获得 Apache License, Version 2.0 许可。

---

## 40. 使用S3对象存储实现更低延迟

**原文标题**: Achieveing lower latencies with S3 object storage

**原文链接**: [https://spiraldb.com/post/so-you-want-to-use-object-storage](https://spiraldb.com/post/so-you-want-to-use-object-storage)

本文探讨了在使用如S3等对象存储时实现更低延迟的策略。作者指出，尽管对象存储平均而言似乎具有出色的延迟，但由于分布式系统中固有的尾部延迟，开发人员在实践中经常会遇到高延迟。

本文提倡将**对冲**作为缓解尾部延迟的主要技术。对冲涉及为相同数据发送多个请求并使用最快的响应，从而显著降低慢速单个请求的影响。作者通过 Rust 模拟演示了这一点，展示了以增加请求开销为代价的改进的 p99 延迟。文章还讨论了对冲的变体，例如在发送重复请求之前等待 p95 阈值或使用不同的端点。

**缓存**被认为是另一种至关重要的优化策略。作者通过成本分析比较了用于缓存的 EBS 存储成本与频繁 S3 请求的成本，得出结论，相对较小的缓存可能更经济且能改善延迟。文章还强调了用于缓存的专用硬件。

最后，提出了通过范围读取进行**水平扩展**。利用对象存储提供商的范围读取 API 允许使用多个连接并行下载对象块，从而最大限度地利用可用带宽。

作者强调，没有一种万能的解决方案，对系统行为的仔细建模、测量和验证至关重要。 最终，利用云在硬件选择方面的灵活性以及理解对象存储作为一个独特的原语是优化性能的关键。

---

## 41. Cybertruck生锈？这很正常

**原文标题**: Cybertruck Rusting? That's Normal

**原文链接**: [https://autobuyersguide.com/cybertruck-rusting-thats-actually-normal/](https://autobuyersguide.com/cybertruck-rusting-thats-actually-normal/)

提供的文本片段不完整且具有误导性。它给出了一个标题（“Cybertruck 生锈？这很正常”），但随后引用了一篇关于沃尔沃 EX30 的文章。因此，无法进行真正的总结。

仅*基于*所给文本，以下是最佳摘要：

所提供的文本是对 Alex L. Dykes 撰写的关于沃尔沃 2025 款 EX30（一款全新的小型电动跨界车）的文章的简短介绍。作者认为这款车可能会显著增加沃尔沃的销量。该文章可能包含关于 EX30 的图片和细节。

---

## 42. Python 的新型 ASN.1 API

**原文标题**: A New ASN.1 API for Python

**原文链接**: [https://blog.trailofbits.com/2025/04/18/sneak-peek-a-new-asn.1-api-for-python/](https://blog.trailofbits.com/2025/04/18/sneak-peek-a-new-asn.1-api-for-python/)

本文宣布 PyCA Cryptography 项目正在开发一款新的 Python ASN.1 API，该项目由 Alpha-Omega 资助。其目标是解决现有 Python ASN.1 库中存在的性能问题、与解析器差异相关的安全漏洞以及过时的编码风格。

新的 API 将使用基于 Rust 的 ASN.1 解析器，以实现与原生代码相当的性能，并将重用 PyCA Cryptography 的 X.509 API 中已使用的解析器，从而降低解析器差异漏洞的风险。该 API 将具有现代的、声明式的数据类风格接口，并带有类型提示，以提高可用性和与类型检查器的兼容性。

本文解释了 ASN.1 的重要性，特别是可辨识编码规则 (DER)，在密码学、网络和电信领域中的重要性。DER 的规范编码、紧凑性、自描述性以及对任意精度整数的支持使其成为这些领域的理想选择。文章强调了 Python 中除了 X.509 证书等标准用途之外，还需要一个通用的 ASN.1 库，并列举了 Sigstore 生态系统中的例子。

开发计划包括构建对序列和枚举的初始支持，将新的 API 集成到 PyCA Cryptography 中，去除重复类型，并在该库未来的主要版本中发布。作者强调了他们致力于改善 Python 生态系统，特别是在密码学和供应链安全方面的承诺，并对 Alpha-Omega 和 PyCA Cryptography 的维护者表示感谢。

---

## 43. 地球地壳内存活生命

**原文标题**: There's Life Inside Earth's Crust

**原文链接**: [https://www.noemamag.com/theres-life-inside-earths-crust/](https://www.noemamag.com/theres-life-inside-earths-crust/)

凯伦·G·劳埃德的文章探索了“地下生命”这个迷人的世界，这些微生物生活在地球深处的地壳中。它们不依赖阳光或氧气生存，而是利用铀和砷等元素进行呼吸，甚至吞噬黄金，从而挑战了我们对生命的理解。它们以极少的能量生存，繁殖速度极慢，导致寿命可能长达数百万年，迫使人们重新评估达尔文进化论。

这些地下生命在全球系统中发挥着至关重要的作用。它们调节地球的氧气水平，循环对浮游植物（从而产生氧气）至关重要的养分，并对有害废物进行解毒。它们对人为引起的气候变化影响巨大；融化的永久冻土中的微生物可以释放大量的二氧化碳和甲烷，加剧变暖。相反，一些微生物可能有助于碳捕获和储存，将捕获的二氧化碳转化为岩石。

为可再生能源技术寻求金属，特别是通过深海多金属结核采矿，带来了一个难题。虽然对电池至关重要，但这种采矿威胁着深海生态系统，扰乱了重要的生物和化学过程，可能损害浮游植物，并释放封存的温室气体。计划中的深海采矿规模远远超过现有的海上石油和天然气以及海底渔业的影响。最终，了解地下生命对于评估和减轻气候变化和资源开采的后果至关重要。

---

## 44. 法官裁定大规模搜查手机信号塔数据违宪

**原文标题**: Judge Rules Blanket Search of Cell Tower Data Unconstitutional

**原文链接**: [https://www.404media.co/judge-rules-blanket-search-of-cell-tower-data-unconstitutional/](https://www.404media.co/judge-rules-blanket-search-of-cell-tower-data-unconstitutional/)

内华达州法官裁定，“基站塔数据倾倒”违宪，侵犯了第四修正案赋予的公民免受非法搜查和扣押的权利。该裁决源于科里·斯普尔洛克一案，他被指控犯有毒品交易和雇凶杀人罪，而一次基站塔数据倾倒将他的手机与犯罪地点联系起来。

法官米兰达·杜承认了这种做法的违宪性，称基站塔数据倾倒构成搜查，而使用的搜查令是一般搜查令，因此是被禁止的。然而，她允许使用在斯普尔洛克案中获得的证据，理由是“善意例外”。她辩称，在签发和执行搜查令时，警官不可能知道该搜查是违宪的。

这项裁决标志着美国联邦第九巡回上诉法院首次对基站塔数据倾倒的合宪性作出裁决。密西西比州的一个案件也得出了类似的结论，目前正由司法部提起上诉。

文章强调了与基站塔数据倾倒相关的隐私问题，因为它们收集了基站塔附近数千名无辜个人的数据，而不仅仅是嫌疑人的数据。虽然最高法院此前在*卡彭特诉美国案*中处理了手机位置数据问题，但它拒绝就基站塔数据倾倒这一具体问题作出裁决。鉴于相互冲突的法院判决，最高法院最终可能会处理这种做法的合法性。

---

## 45. Evans 书中 DDD 示例的 UML 图

**原文标题**: UML diagram for the DDD example in Evans' book

**原文链接**: [https://github.com/takaakit/uml-diagram-for-ddd-example-in-evans-book](https://github.com/takaakit/uml-diagram-for-ddd-example-in-evans-book)

本项目提供UML图，展示领域驱动设计（DDD）的示例，一个货运系统，该示例源自Eric Evans的著作，并基于GitHub上的dddsample-core项目。这些图旨在可视化战略和战术DDD设计的实现。

文章重点介绍了以下几个图：

*   **用户-系统交互：** 展示诸如货物追踪和预订等用例的时序图。
*   **领域模型概览：** 说明基本的领域元素及其关系。
*   **"ABC123"货物的领域对象：** 展示对象快照和连接，特别是针对一个预设的货物示例。
*   **总体结构：** 描述系统架构，包含预订和运输网络上下文，构建于Spring技术之上。
*   **行为：** 系统初始化、货物追踪、预订、路线建议和路线分配的通信图。
*   **有向图：** 结构元素及其关系的另一种可视化方式。

文章鼓励读者参考Evans的著作以了解DDD理论，并参考dddsample-core项目以了解实现细节。推荐使用Astah建模工具来探索详细的UML模型。本项目使用了多个基于BSD和MIT许可的开源JavaScript库，而其他项目文件则采用Creative Commons Zero（CC0）许可。最后，本项目鼓励用户报告错误。

---

## 46. 一颗恒星似乎直接坍缩成黑洞而没有发生超新星爆发（2017）

**原文标题**: A star appears to have collapsed straight into a black hole without supernova (2017)

**原文链接**: [https://science.nasa.gov/missions/hubble/collapsing-star-gives-birth-to-a-black-hole/](https://science.nasa.gov/missions/hubble/collapsing-star-gives-birth-to-a-black-hole/)

2017年，天文学家利用大双筒望远镜、哈勃望远镜和斯皮策空间望远镜观测到一颗质量约为太阳25倍的巨大恒星，似乎直接坍缩成黑洞，而没有发生超新星爆发。这种“失败的超新星”事件挑战了黑洞形成的传统理解，后者通常涉及恒星在坍缩前以超新星的形式爆发。

这颗名为N6946-BH1的恒星，位于NGC 6946螺旋星系中，于2009年显著变亮，亮度是太阳的百万倍，但在2015年消失不见。进一步分析显示，该位置发出了微弱的红外信号，可能表明碎片正在落入新形成的黑洞。

研究人员估计，10-30%的大质量恒星可能会经历类似的“大失败”，悄无声息地坍缩成黑洞而没有发生超新星爆发。这可以解释超新星的预期数量与天文学家实际观测到的数量之间的差异。

这一发现对理解超大质量黑洞的形成具有重要意义，比如那些通过引力波被LIGO探测到的黑洞。它表明，形成如此巨大的黑洞可能更容易，而无需与超新星相关的质量抛射。这项研究由俄亥俄州立大学的一个团队进行，加州理工学院和俄克拉荷马大学也做出了贡献，并得到了美国国家科学基金会的支持。

---

## 47. 最著名的二氧化碳吸收剂

**原文标题**: The most famous carbon dioxide absorber

**原文链接**: [https://www.howequipmentworks.com/apollo_13/](https://www.howequipmentworks.com/apollo_13/)

本文详细介绍了惊险的阿波罗13号任务，以及二氧化碳吸收器在宇航员生存中的关键作用。阿波罗13号于1970年发射，但氧气罐爆炸导致灾难，服务舱瘫痪，并危及氧气、水和电力的供应。宇航员被迫转移到登月舱，该舱的设计仅供两人在月球上短期使用。

一个主要的挑战是登月舱内二氧化碳的积聚。虽然指挥舱和登月舱都配备了使用氢氧化锂的二氧化碳吸收器，但登月舱的储备仅够两名宇航员使用两天。由于三名宇航员需要生存四天，二氧化碳水平有可能达到致命程度。

关键问题在于，登月舱使用圆形吸收器容器，而指挥舱使用方形容器。本文描述了宇航员通常如何更换这些容器，并强调了登月舱圆形吸收器的供应有限。这种形状差异使得直接使用来自瘫痪指挥舱的充足的方形容器成为不可能，为确保宇航员生存的绝望工程解决方案奠定了基础（将在下一部分中继续）。

---

## 48. 微软Copilot越来越像不受欢迎的派对来宾

**原文标题**: Microsoft Copilot shows AI increasingly appears like an unwanted party guest

**原文链接**: [https://www.theregister.com/2025/04/18/microsoft_copilot_not_wanted/](https://www.theregister.com/2025/04/18/microsoft_copilot_not_wanted/)

*The Register* 的这篇文章认为，人工智能正越来越像一个不受欢迎的“派对客人”，即使在用户试图避开它时，也会强迫自己出现在用户面前。 主要例子是微软的 Copilot，有报告显示它会在被禁用后重新启用，可能暴露敏感数据。一位加密货币开发者报告称，Copilot 在 Visual Studio Code 中自动重新激活，违背了用户偏好。一位 Reddit 用户指出，用于禁用 Copilot 的组策略对象在新版本的 Windows 11 中不再有效，需要更复杂的回避方法。

这篇文章将问题扩展到微软之外，列举了 iOS 中的 Apple Intelligence、谷歌在搜索中强制使用的 AI Overviews，以及 Meta 在社交媒体平台中不可避免的人工智能集成和用于人工智能训练的数据收集。虽然 Mozilla 对 Firefox 的 AI 聊天机器人侧边栏采取了较为温和的方式，但即使是这也被一些人认为是不受欢迎的。 DuckDuckGo 提供了一个避免在其搜索引擎中集成人工智能的选项。

作者总结说，由于各大公司对这项技术的大量投资，导致其普遍集成，无论用户是否愿意，都使得避免人工智能变得越来越困难。

---

## 49. 特斯拉推迟在美国发布新款“平价电动车/精简版Model Y”

**原文标题**: Tesla delays new 'affordable EV/stripped down Model Y' in the US

**原文链接**: [https://electrek.co/2025/04/18/tesla-delays-affordable-ev-stripped-down-model-y-us-report/](https://electrek.co/2025/04/18/tesla-delays-affordable-ev-stripped-down-model-y-us-report/)

据Electrek报道，特斯拉将推迟在美国发布新款更经济型电动汽车，据信该车型是Model Y的简化版。原定于2025年上半年发布，现在预计将推迟“至少数月”，可能推迟到2025年第三季度或2026年初。

生产更便宜的Model Y的举动源于首席执行官埃隆·马斯克放弃了全新的25,000美元电动汽车，而是选择利用现有生产线，并通过在Model Y和Model 3平台上生产更经济型电动汽车来提高工厂利用率。这些车型将减少功能并使用更便宜的材料。

该报道还指出，特斯拉计划到2026年在美国生产25万辆这款新型号，与目前的生产能力相当。这篇文章将此与在墨西哥推出的简化版Model 3进行了比较，后者取消了第二排屏幕等功能，并使用织物代替了纯素皮革。

Electrek的分析表明，这种策略虽然可能提高工厂利用率，但也可能蚕食现有的Model 3和Model Y销量，并降低利润率。作者认为，马斯克会将此举解释为增加道路上特斯拉汽车数量的长期战略，旨在通过FSD销售产生未来收入，尽管目前该技术的采用有限。一条热门评论认为，此举可能会损害特斯拉作为高端品牌的形象。

---

## 50. 将Luna-Terra崩盘作为时序多层图进行研究

**原文标题**: Investigating the Luna-Terra Collapse as a Temporal Multilayer Graph

**原文链接**: [https://dl.acm.org/doi/10.1145/3726869](https://dl.acm.org/doi/10.1145/3726869)

无法访问文章链接。

---

## 51. Loglan'82：面向对象和分布式编程的程序设计语言

**原文标题**: Loglan'82: programming language for object-oriented and distributed programming

**原文链接**: [https://lem12.uksw.edu.pl/wiki/Loglan%2782_project](https://lem12.uksw.edu.pl/wiki/Loglan%2782_project)

Loglan'82 是一种面向对象和分布式编程的编程语言，其特性旨在超越现有语言。 关键特性包括安全高效的对象管理系统（通过“kill”等指令解决悬挂指针问题）、用于类的模块、协程和带有线程的进程（代理），从而在单个模型中实现并发和分布式计算。

Loglan'82 虚拟机可以通过互联网连接形成用于分布式处理的虚拟多处理器计算机。它采用一种原创的对象协议，用于方法通信和同步，称为方法的“异形调用”，从而实现线程间通信。每个代理（进程对象）都可以管理自己的协程系统。

该语言面向需要并发、分布或两者兼有的有雄心的程序员，并通过其统一的模型降低编程成本。教师可以使用它来全面地展示面向对象编程，而无需使用多种语言。研究人员可以从其解决诸如组合嵌套和继承同时确保静态链接和确定超类、管理协程和进程以及安全地释放内存等重要问题的方案中获益。

资源包括微型手册、报告、用户手册、波兰语手册、快速参考卡和与其他语言的比较等文档。示例程序包括矩阵乘法和协程实现。存在适用于 Linux 和 Windows 的编译器。 Loglan'82 解决了与对象管理、协程语义和分布式计算相关的基本研究问题，可能在 Java 编程中具有应用。

---

## 52. 蜂窝APL计算机的系统设计

**原文标题**: System Design of a Cellular APL Computer

**原文链接**: [https://ieeexplore.ieee.org/document/1671509](https://ieeexplore.ieee.org/document/1671509)

此IEEE Xplore页面描述了一篇题为“蜂窝APL计算机系统设计”的文章。遗憾的是，所提供的内容仅包含网站的标准页脚和导航元素，并未提供关于文章实际内容的任何信息。

因此，我无法提供该文章的摘要。现有信息仅表明存在一篇详细描述“蜂窝APL计算机”系统设计的研究论文。APL（一种编程语言）以其面向数组的处理能力而闻名。因此，该文章可能探讨了一种针对APL优化的计算机体系结构，可能采用蜂窝自动机或大规模并行处理方法来利用APL固有的并行性。

要理解文章的关键点，需要通过IEEE Xplore访问完整文档并分析其内容。在此之前，我只能根据标题和APL的特性进行推测。

---

## 53. 《星际牛仔》创作者认为现实比科幻更反乌托邦

**原文标题**: The Creator of 'Cowboy Bebop' Thinks Reality Is More Dystopian Than Sci-Fi

**原文链接**: [https://www.nytimes.com/2025/04/14/arts/television/shinichiro-watanabe-lazarus.html](https://www.nytimes.com/2025/04/14/arts/television/shinichiro-watanabe-lazarus.html)

本文预览渡边信一郎的最新动画作品《拉撒路》，这是一部在Max上播放、并在Adult Swim播出的科幻动作系列剧。渡边信一郎以其融合多种题材的动画作品如《星际牛仔》和《混沌武士》而闻名，这次他携手《拉撒路》回归科幻领域，故事设定在2055年。其前提是一个奇迹药物具有隐藏的致命副作用，除非找到解药，否则使用者只能活30天。

本文重点介绍了渡边信一郎的电影影响，将《星际牛仔》的电影参考与《拉撒路》进行对比，《拉撒路》的动作场面是与《疾速追杀》导演查德·斯塔尔斯基合作设计的。在提供的采访摘录中，渡边信一郎讨论了该剧的主题和背景，强调了其与当今时代的关联性。《拉撒路》与渡边信一郎之前的科幻作品不同，因为它发生在我们世界的近未来版本中。他还提到了最初的《银翼杀手》对他坚持在动画中进行多元文化和包容性选角的影响。

---

## 54. 使用Joplin做笔记

**原文标题**: Taking Notes with Joplin

**原文链接**: [https://lwn.net/Articles/1016400/](https://lwn.net/Articles/1016400/)

这篇LWN.net文章评测了Joplin，一个以Markdown支持、通过插件进行扩展以及多媒体功能而闻名的开源笔记应用程序。Joplin提供跨平台兼容性（Linux、macOS、Windows、Android、iOS）和多种同步选项，包括Nextcloud、WebDAV、Dropbox、OneDrive、Joplin Cloud和本地文件系统，并提供端到端加密。

文章重点介绍了Joplin的三窗格界面：导航面板、笔记列表和编辑器/查看器。它支持Markdown和所见即所得编辑器，笔记存储在SQLite数据库中。Joplin还提供待办事项列表功能以及各种格式的导入/导出功能。

Joplin 3.2引入了多窗口支持、笔记列表的多列布局、系统主题检测和辅助功能增强等功能。文章还讨论了基于JavaScript的扩展API，用于插件开发，包括现有的插件，如数学模式和自由手绘，以及内置的OCR功能。

该评论指出了Joplin的一些缺点，例如由于其Electron基础而导致更高的资源消耗、潜在的同步延迟、有限的冲突解决以及所见即所得编辑器的局限性。尽管存在这些缺点，Joplin仍在积极开发中，定期发布版本并有社区贡献，使其成为寻求灵活和开源笔记解决方案的用户的多功能选择。

---

## 55. Hextraction，一款免费开源的棋盘游戏

**原文标题**: Hextraction, a free and open source board game

**原文链接**: [https://www.playhextraction.com/](https://www.playhextraction.com/)

无法访问文章链接。

---

## 56. Claude代码：自主编码的最佳实践

**原文标题**: Claude Code: Best practices for agentic coding

**原文链接**: [https://www.anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)

我阅读了来自所提供URL的文章“Claude Code: Agentic 编码最佳实践”。以下是摘要：

该文章概述了 Anthropic 公司利用其大型语言模型 (LLM) Claude 进行“Agentic 编码”的最佳实践，Agentic 编码指的是由 LLM 执行的自主或半自主编码任务。文章强调，有效的 Agentic 编码需要一个精心设计的系统，将 Claude 与外部工具和结构化流程相结合。

主要建议包括：

*   **工具使用：** 强调 Claude 能够使用工具（如文件系统、shell 或特定 API）与环境交互并执行复杂任务的重要性。工具使用显著扩展了 Claude 的能力，使其不仅仅是生成代码。
*   **迭代开发与可观察性：** 提倡将编码任务分解为更小的、带有反馈循环的迭代步骤。这使得 Claude 能够更容易地识别和纠正错误。可观察性，通过记录和监控 Claude 的操作和输出来实现，对于调试和理解 LLM 的推理至关重要。
*   **上下文管理：** 向 Claude 提供充分且相关的上下文至关重要。这包括清晰的指令、相关的代码片段、错误消息和之前的输出。诸如检索增强生成 (RAG) 等策略可以帮助提供相关信息。
*   **结构化提示：** 提示应该定义明确，清楚地概述所需的任务、任何约束以及预期的输出格式。诸如少样本学习（提供成功完成的示例）等技术也可以提高 Claude 的性能。
*   **安全与防护措施：** 实施安全措施以防止意外后果或恶意行为至关重要。这包括限制 Claude 对敏感资源的访问以及对其输出实施检查。

文章总结道，通过结合这些最佳实践，开发人员可以释放 Claude 在自动化复杂编码任务方面的潜力，并在降低风险的同时实现显著的生产力提升。

---

## 57. 双子座2.5闪电

**原文标题**: Gemini 2.5 Flash

**原文链接**: [https://developers.googleblog.com/en/start-building-with-gemini-25-flash/](https://developers.googleblog.com/en/start-building-with-gemini-25-flash/)

Gemini 2.5 Flash，作为在2.0 Flash基础上构建的新模型，现已通过 Google AI Studio 和 Vertex AI 上的 Gemini API 提供预览。该版本在保持速度和成本效益的同时，提供了增强的推理能力。

Gemini 2.5 Flash 的一个关键特性是其完全混合的推理能力，允许开发者启用或禁用“思考”过程，并设置思考预算来平衡质量、成本和延迟。这种“思考”过程使模型能够更好地理解提示，分解复杂任务并规划响应，从而产生更准确的答案，尤其是在复杂任务上。值得注意的是，它在 LMArena 的 Hard Prompts 上表现出色，仅次于 2.5 Pro，同时提供与其他模型相当的成本效益。

开发者可以使用“思考预算”来管理思考过程，控制思考过程中生成的最大令牌数量。较高的预算允许更多的推理，但模型会根据提示的复杂性调整思考量。将预算设置为 0 可提高性能，同时保持 2.0 Flash 的速度。

该模型可在 Google AI Studio 和 Vertex AI 中进行实验，Gemini 应用中有一个专门的下拉菜单。鼓励开发者测试“thinking_budget”参数，以探索可控推理如何帮助解决复杂问题。API 参考和编码示例可供开发者使用。

---

## 58. Show HN: 针对Wasm优化的Libc片段

**原文标题**: Show HN: (bits) of a Libc, Optimized for Wasm

**原文链接**: [https://github.com/ncruces/go-sqlite3/tree/main/sqlite3/libc](https://github.com/ncruces/go-sqlite3/tree/main/sqlite3/libc)

ncruces 发布的这篇“Show HN”文章重点介绍了一个项目，该项目构建了标准 C 库 (libc) 的一个子集，专门针对 WebAssembly (Wasm) 进行了优化。该项目名为“针对 Wasm 优化的 Libc 片段 (bits)”，位于“go-sqlite3”存储库中，但侧重于 libc 部分。

列表显示了存储库的 `main/libc/` 目录中的几个文件，揭示了关键组件：`libc.wasm` (编译后的 Wasm 库)、`libc.wat` (其 WebAssembly 文本格式等效项)、`libc_test.go` (基于 Go 的测试)、`stdlib.h` 和 `string.h` (可能定义公开 API 的头文件) 以及支持构建和基准测试的脚本 (`build.sh` 和 `benchmark.sh`)。

该项目似乎旨在为无法获得或不需要完整系统 libc 的环境提供一个最小、高效的 libc，Wasm 是主要目标。这使得开发人员可以通过提供基本的 C 标准库函数，更轻松地将现有的 C/C++ 代码或编写新的代码带到基于 Wasm 的平台。这些文件表明该项目侧重于标准库函数和字符串操作，这意味着这些是优化库的核心领域。GitHub 统计数据（22 个 fork，653 个 star）表明 Wasm 和 Go 社区对此项目具有相当大的兴趣。

---

## 59. 科学家声称发现了前所未见的颜色

**原文标题**: Scientists claim to have found colour no one has seen before

**原文链接**: [https://www.theguardian.com/science/2025/apr/18/scientists-claim-to-have-found-colour-no-one-has-seen-before](https://www.theguardian.com/science/2025/apr/18/scientists-claim-to-have-found-colour-no-one-has-seen-before)

加州大学伯克利分校的科学家声称发现了一种新颜色“olo”，这种颜色只有在激光直接刺激视网膜的情况下才能看到。该实验包括向参与者的眼睛发射激光脉冲，以选择性地刺激单个视锥细胞，特别是M锥细胞（对中等波长敏感），使其超出自然激活极限。

参与者将这种颜色描述为高度饱和的蓝绿色，但他们强调，这种描述无法完全捕捉到体验的丰富性。“olo”这个名字来源于二进制代码010，代表仅激活M锥细胞。

虽然研究人员承认他们无法通过图像或显示器来传达“olo”的真实体验，但他们提供了一块青绿色正方形作为最接近的可用表示。该研究的目的是了解大脑如何处理视觉信息，并探索在理解色盲和其他与视觉相关的疾病方面的潜在应用。

然而，并非所有人都同意这一发现。另一位视觉科学家认为，“olo”只是具有正常色觉的人可以实现的更饱和的绿色，并质疑该研究的总体价值。伯克利团队承认，“olo”并非近期内公众可以轻易获得的，因为它需要专门的激光技术。

---

## 60. 如何设计、制造和测试小型液体燃料火箭发动机 - ROCKETLAB

**原文标题**: How to design, build and test small liquid-fuel rocket engines-ROCKETLAB

**原文链接**: [https://spacha.github.io/How-to-Rocket/#contents](https://spacha.github.io/How-to-Rocket/#contents)

勒罗伊·J·克日茨基的文章《如何设计、建造和测试小型液体燃料火箭发动机》很可能提供了一份关于开发小型液体燃料火箭发动机整个生命周期的实用指南。

它可能涵盖涉及的*设计原则*，包括燃烧室设计、喷嘴选择、喷注器设计和推进剂供给系统等方面。这会涉及与推力、比冲和最佳混合比相关的计算，对于小型发动机来说可能会简化。

然后，这篇文章深入探讨*建造过程*，强调材料选择（考虑耐热性和耐压性）、适用于小型车间的制造技术（如机械加工、焊接，甚至可能是3D打印）以及对精度和安全性的关键需求的重要性。

最后，这篇文章可能侧重于*测试程序*，概述安全测试实践、所需的仪器（压力传感器、热电偶、推力台）以及用于评估发动机性能的数据采集和分析技术。它可能还会解决测试期间遇到的常见问题，如燃烧不稳定或泄漏。

总的来说，这篇文章旨在使业余火箭爱好者和小型开发商能够掌握设计、建造和安全测试他们自己的液体燃料火箭发动机所需的知识和实践指导。它可能强调一种具有简化技术且易于操作的方法，使其能够为资源有限的个人所用。

---

## 61. 耶稣受难节为何被称为“好星期五”？

**原文标题**: Why is Good Friday called Good Friday?

**原文链接**: [https://www.historyextra.com/period/general-history/good-friday-facts-why-called/](https://www.historyextra.com/period/general-history/good-friday-facts-why-called/)

本文解释了“耶稣受难日”这个名称的起源和意义。耶稣受难日是基督徒纪念耶稣基督被钉十字架的节日。虽然看似矛盾，“耶稣受难日”这个名称可能源于“good”一词的古义，意为“神圣的”。 这一天被认为是神圣的，因为它标志着基督为人类做出的终极牺牲，带来了宽恕和永生。

本文详细描述了耶稣受难日的事件，包括耶稣的被捕、判刑、鞭打、钉十字架和埋葬。文章提到了苦路，即教堂中描绘这些事件的场景。 不同的基督教教派以礼拜、阅读、与基督受难相关的赞美诗、祈祷和反思来纪念耶稣受难日。 罗马天主教徒通常遵守斋戒，教皇会在罗马带领游行。 东正教会则会展示圣殓裹尸布。

本文还探讨了世界各地与耶稣受难日相关的习俗，从重演耶稣受难的过程到独特的传统，例如在牙买加以蛋白预测未来。文章将这些习俗与复活节更为世俗的传统（如彩蛋、巧克力和兔子）进行了对比。

最后，本文阐明了耶稣受难日的日期，即复活节前的星期五，并解释说复活节的日期每年都根据月球周期及其与逾越节的关系而变化。 本文还简要概述了圣周内的其他圣日，这些圣日最终引向复活节。

---

## 62. 联邦政府接管宾州车站重建项目，将大都会运输署踢出局

**原文标题**: Feds take control of Penn Station rebuild, kick MTA off the project

**原文链接**: [https://gothamist.com/news/trump-station-feds-take-control-of-penn-station-rebuild-kick-mta-off-the-project](https://gothamist.com/news/trump-station-feds-take-control-of-penn-station-rebuild-kick-mta-off-the-project)

在一次令人惊讶的举动中，唐纳德·特朗普总统领导下的联邦政府将从MTA手中接管宾州车站的重建工作。联邦铁路管理局通知MTA主席Janno Lieber，Amtrak将负责监督该项目，理由是MTA“效率低下、浪费和管理不善”。交通部长肖恩·达菲表示，目标是创建一个反映“美国伟大”的宾州车站。

联邦政府计划将现有的重建计划与扩建计划相结合，并将为合并后的项目寻找开发商。州长凯西·霍赫尔对这一决定表示欢迎，声称这将为纽约纳税人节省13亿美元。虽然 Lieber 表示 MTA 希望继续参与，但区域规划协会的 Tom Wright 支持接管，认为这最终可以推进这个长期延误的项目。他甚至考虑将车站更名为特朗普车站。

在此决定之前，特朗普盟友支持一项提案，将麦迪逊广场花园搬迁，并以新古典主义风格重建宾州车站，该提案得到了国家公民艺术协会的支持。纽约城市俱乐部的Layla Law-Gisiko 对此表示谨慎乐观，希望重点将放在提高运力和连通性上。霍赫尔一直在与特朗普就宾州车站和拥堵费问题进行谈判。

---

## 63. 杰四周年 (2024)

**原文标题**: Four Years of Jai (2024)

**原文链接**: [https://smarimccarthy.is/posts/2024-12-02-four-years-of-jai/](https://smarimccarthy.is/posts/2024-12-02-four-years-of-jai/)

Smári McCarthy 回顾了他们四年来专业使用闭源测试编程语言 Jai 的经验。他们首先感叹现代软件日益缓慢和充满缺陷，将其归因于诸如优先考虑开发者速度而非代码效率、CPU架构的变化以及脚本语言的兴起等因素。

McCarthy 被 Jai 吸引是因为它专注于经验丰富的程序员的需求，优先考虑性能和控制，且并非故意晦涩难懂。他们强调了 Jai 的简洁性、强大的特性（如结构体组合），以及从其他语言（如 C/C++ 或 Python）重写代码时代码和复杂性的显著降低。Jai 提供了直观的错误消息系统和调试工具。

他们赞扬 Jai 的极简主义语法和语义、编译速度，以及其独特的构建系统，该系统允许用 Jai 本身编写构建脚本。元编程能力被认为是其显著优势，允许进行高级构建过程和特定于平台的优化。总而言之，McCarthy 认为 Jai 对于重视性能、控制以及干净、直接的开发体验的经验丰富的程序员来说，是一种很有前途的语言。

---

## 64. 墨水与开关约束系统 (2023)

**原文标题**: Ink and Switch Constraint System (2023)

**原文链接**: [https://www.inkandswitch.com/ink/notes/phase-2-constraint-system/](https://www.inkandswitch.com/ink/notes/phase-2-constraint-system/)

本文总结了Ink and Switch在一个新的约束系统上的工作，该系统旨在创建一个具有逼真机械结构和双向计算的动态媒介。之前的约束系统存在“漂浮感”、“爆炸”和性能不佳等问题。

Alex的工作通过传播已知量和利用变量之间的线性关系来解决这些问题，从而有效地降低了解算器的维度。例如，以度和弧度表示的角度对于解算器来说会简化为一个变量，从而防止不稳定和“漂浮感”。

另一个关键技术是“聚类”，将约束和变量划分为独立的组，以加快收敛速度并实现潜在的并行化。该系统的设计允许不同的求解器选项，从而可以试验梯度下降等方法。使用uncmin（及其修改后的g9版本）的初步结果表明收敛性有所提高。未来的计划包括探索Avi Bryant的自动微分和WebAssembly求解器。

此外，以极坐标空间（角度/距离）而不是笛卡尔空间（x/y）表示位置关系可以提高性能。新的约束系统明显提高了稳定性，以前的问题结构现在可以正常运行。

---

## 65. 更快的C++

**原文标题**: Less Slow C++

**原文链接**: [https://github.com/ashvardanian/less_slow.cpp](https://github.com/ashvardanian/less_slow.cpp)

《更快的C++》是一个代码仓库，包含基准测试和代码示例，旨在帮助开发者编写更高效的 C、C++ 和汇编代码。它旨在揭示传统编码教育中经常被忽视的常见性能陷阱，并提供实用的、极简的解决方案。

该仓库涵盖了广泛的主题，从小规模优化（如更廉价的随机输入生成和更快的三角函数近似）到更大规模的概念（如并行算法、协程和自定义线程池）。它探讨了超越基础的编译器优化技术，分析了不同数据结构和算法的性能，并深入研究了硬件特定的优化，包括使用CUDA和PTX的GPU编程。

该项目使用C++20特性，主要为Linux上的GCC和Clang设计，但也力求更广泛的兼容性。提供了编译代码的说明，包括如何管理第三方依赖，例如 Google Benchmark、Intel 的 oneTBB、Meta 的 libunifex、range-v3、fmt、StringZilla、CTRE、nlohmann_json、yyjson、Google 的 Abseil、cppcoro、liburing、ASIO、Nvidia 的 CCCL 和 Nvidia 的 CUTLASS。摘要还提供了运行基准测试和解释结果的说明。该仓库的基准测试利用 Google Benchmark 的功能进行详细的性能分析和计数器测量。

---

## 66. 当我们因价格太高而玩不起爱好时，我们失去了什么

**原文标题**: What We Lose When We're Priced Out of Our Hobbies

**原文链接**: [https://www.theatlantic.com/family/archive/2025/04/hobby-inflation-fishing-knitting/682497/](https://www.theatlantic.com/family/archive/2025/04/hobby-inflation-fishing-knitting/682497/)

泰勒·奥斯汀·哈珀的文章《当我们因爱好成本高昂而望而却步时，我们失去了什么》探讨了“爱好通胀”现象，即休闲活动的成本不断上涨，使得只有富人才能负担得起。作者通过自己玩射击、收藏波旁威士忌和钓鱼的个人经历来阐述这一趋势。

哈珀认为，这种成本上涨不仅仅是一个经济问题，它还具有重要的社会影响。爱好创造了多元化的社区，让来自不同背景的人们联系和互动，从而促进理解和宽容。随着爱好变得更加排他性，这种跨文化互动的机会减少，可能导致更大的社会孤立和不宽容。

他指出了导致爱好通胀的几个因素，包括供应链问题、疫情期间的普及程度提高、原材料成本上涨以及关税，并以特朗普的关税对渔具的影响作为一个具体的例子。

哈珀总结道，随着爱好变得异常昂贵，个人被迫做出关于追求哪些活动的艰难选择，从而影响他们的社交圈和社区参与度。他表达了对休闲活动越来越难以获得的社会将变得更加孤独，并且对差异的容忍度降低的担忧，特别是对中产阶级和工人阶级造成最大的打击。他担心多元化社会世界的萎缩以及社会分裂加剧的可能性。

---

## 67. 达尔文的孩子们在《物种起源》手稿上乱涂乱画 (2014)

**原文标题**: Darwin's children drew all over the “On the Origin of Species” manuscript (2014)

**原文链接**: [https://theappendix.net/posts/2014/02/darwins-children-drew-vegetable-battles-on-the-origin-of-species](https://theappendix.net/posts/2014/02/darwins-children-drew-vegetable-battles-on-the-origin-of-species)

本文发表于2014年达尔文日，通过展示达尔文的孩子们在他手稿和妻子艾玛日记上的绘画和涂鸦，探索了查尔斯·达尔文更具个人色彩的一面。本杰明·布林着重强调这些标记如何让人得以窥见达尔文家庭的生活，并强调即使是传奇人物也身处家庭的日常现实之中。

文章展示了在达尔文《物种起源》手稿背面发现的绘画图片，包括“水果和蔬菜士兵之战”以及其他受自然启发的艺术作品。文章还展示了艾玛·达尔文自身的绘画天赋，以及她被幼儿涂鸦破坏的日记条目。

布林强调，这些文物揭示了达尔文一家对自然和观察的共同兴趣。此外，他还提到了查尔斯最喜欢的孩子安妮·达尔文的悲惨故事，安妮在十岁时去世。他收录了装有纪念品的盒子和达尔文关于安妮的回忆录的图片，说明了她的去世对他以及可能对他的科学思想产生的深刻影响。文章强调了铭记历史人物及其作品的人文背景的重要性。

---

## 68. Show HN: Attune - 秒速构建和发布APT仓库

**原文标题**: Show HN: Attune - Build and publish APT repositories in seconds

**原文链接**: [https://github.com/attunehq/attune](https://github.com/attunehq/attune)

Attune 是一个用于安全构建和发布 APT (Debian/Ubuntu) 仓库的工具。它提供灵活的部署选项（自托管或托管云），通过在本地执行仓库索引签名来优先考虑安全性，并通过增量索引重建来提高速度，从而实现快速的软件包添加和删除。

“快速入门”指南演示了如何使用 Docker 和 GnuPG 在大约五分钟内设置 APT 仓库。步骤包括：

1.  通过克隆仓库、配置环境变量（包括 `ATTUNE_SECRET`）并使用 Docker Compose 启动控制平面和支持服务来设置 Attune 后端。
2.  安装 Attune CLI。
3.  使用 `attune repo create` 命令创建仓库，指定 URL 和发行版。
4.  使用 `attune repo pkg -r 1 add` 命令将 `.deb` 软件包添加到仓库。
5.  使用 GPG 密钥签名和部署仓库。这包括根据需要生成 GPG 密钥，导出签名密钥，并使用 `attune repo -r 1 sync -k demo-key.asc` 来完成部署。

文章最后指示用户查阅用户指南以获取更详细的说明和配置选项，并声明 Attune 采用 Apache 2 许可。

---

## 69. PDCurses – 适用于不符合 termcap/terminfo 模型环境

**原文标题**: PDCurses – for environments that don't fit the termcap/terminfo model

**原文链接**: [https://github.com/wmcbrine/PDCurses](https://github.com/wmcbrine/PDCurses)

PDCurses 是一款公共领域的 curses 库，旨在为 DOS、OS/2、Windows 控制台、X11 和 SDL 等环境创建基于文本的应用程序。 它实现了 X/Open 和 System V R4 curses 中的大多数函数，并支持这些平台的各种编译器。 X11 和 SDL 端口使从现有 curses 程序创建 GUI 应用程序成为可能。

该库主要以源代码形式分发，但可能提供预编译版本。 最新版本和文档的官方网站是 https://pdcurses.org/。 用户可以通过电子邮件订阅低流量邮件列表来保持更新（详细信息已提供）。

主要资源包括“docs”目录中的文档、GitHub 页面和 SourceForge 页面。 虽然核心包属于公共领域，但 demos 和 X11 目录中的某些文件具有特定的版权许可。 该软件按“原样”提供，不提供任何保证。 William McBrine 是当前的维护者。

---

## 70. Defold：跨平台游戏引擎

**原文标题**: Defold: cross-platform game engine

**原文链接**: [https://defold.com](https://defold.com)

Defold 是一款免费开源、跨平台的游戏引擎，专为高性能的 2D 和 3D 游戏设计。它提供开箱即用的全功能开发环境，无需复杂的设置。Defold 使用 Lua 脚本编写游戏逻辑，并拥有可视化编辑器、代码编辑器、场景编辑器、粒子编辑器和瓦片地图编辑器。

Defold 的一个主要优势是能够发布到广泛的平台，包括 PlayStation、Nintendo Switch、Android、iOS、macOS、Linux、Windows、Steam、HTML5、Facebook，以及潜在的 XBox。这可以通过单一代码库实现，从而简化开发流程。

该引擎提供了一个包含复杂游戏行为构建模块和零配置云构建的完整解决方案。开发者还可以通过资源门户、本地构建环境和自定义原生代码来扩展功能。Defold 与流行的工具集成，例如 Atom、VS Code、Rive、Spine、TexturePacker 和 Tiled。

“永久”免费是其核心宗旨，由 Defold 基金会支持，确保没有前期成本、许可费、版税或运行时费用。它是一款可用于生产的引擎，在各种平台上都有经过验证的记录，并与分析和游戏服务集成。每月定期发布版本，保持引擎的更新。可以通过教程、手册、API 参考、示例和社区论坛获取学习资源。

---

## 71. 外国留学生遭拘留签证被吊销，美国高校焦虑

**原文标题**: Anxiety at US colleges as foreign students are detained and visas revoked

**原文链接**: [https://www.bbc.com/news/articles/c20xq5nd8jeo](https://www.bbc.com/news/articles/c20xq5nd8jeo)

由于美国大学针对参与亲巴勒斯坦抗议活动的学生加大拘留和吊销签证力度，在美留学生群体中日益增长的焦虑情绪一览。超过1000名学生的签证被吊销或法律身份被更改，原因往往不明。尽管一些案例涉及犯罪记录或轻微违规行为，但国务卿马可·卢比奥承认参与亲巴勒斯坦抗议活动是一个考量因素。

学生们表达了因批评以色列和美国对其支持的政治言论而成为目标的担忧，随身携带列有他们权利的卡片，甚至避免离家。各院系也受到影响，因为海外研究人员不愿回国。文中重点介绍了几个学生被联邦特工或移民局拘留的具体案例，其中包括一名因其岳父与哈马斯的关系而被指控为反犹主义的冲突解决研究员，以及参与加沙抗议和评论文章的学生。

公民自由团体正在抗议这些行动，认为其侵犯了宪法权利。白宫冻结了对哈佛大学的资金，原因是与学生签证持有者相关的要求，这表明大学感受到了压力。教授们正在提供支持，但一种“寒蝉效应”已经笼罩了校园，学生们害怕从国外返回，并担心移民局的突击搜查。一些学生正在采取预防措施，例如清理他们的消息应用程序并学习如何快速锁定他们的手机。

---

## 72. Unikernel Linux (UKL) (2023)

**原文标题**: Unikernel Linux (UKL) (2023)

**原文链接**: [https://dl.acm.org/doi/10.1145/3552326.3587458](https://dl.acm.org/doi/10.1145/3552326.3587458)

无法访问文章链接。

---

## 73. 好运礼包

**原文标题**: The Good Karma Kit

**原文链接**: [https://archivebox.github.io/good-karma-kit/](https://archivebox.github.io/good-karma-kit/)

善业工具包：一个Docker Compose项目，旨在帮助用户贡献闲置服务器资源（CPU、内存、磁盘和带宽）给各种公益项目。它捆绑了多个容器化应用程序，允许用户同时支持多个事业。

该工具包包含以下工具：

*   **分布式网络：** Tor和i2p中继节点，以增强在线隐私。
*   **分布式计算：** BOINC和Folding@home，为科学研究做出贡献。
*   **互联网存档：** ArchiveWarrior、ZIMfarm、Kiwix、ArchiveBox和PYWB，用于保存在线内容。
*   **分布式存储：** IPFS、Storj和Sia节点，用于为去中心化存储网络做出贡献，以及Transmission用于种子分享。

该项目强调易用性，允许用户选择要运行的容器并自定义资源限制。它还突出了每个项目的非营利/营利状态，以便用户做出明智的选择。关键注意事项包括了解将服务暴露于公共互联网的风险以及保持容器更新的必要性。 推荐的三个最具影响力的项目是ArchiveWarrior、BOINC和Tor。欢迎对该工具包进行贡献和改进。

---

## 74. 暴露于抗焦虑药物污染的鲑鱼更易冒险

**原文标题**: Salmon Exposed to Anti-Anxiety Medication Pollution Take More Risks

**原文链接**: [https://www.smithsonianmag.com/smart-news/salmon-are-being-exposed-to-our-anti-anxiety-medication-and-its-making-them-take-more-risks-study-suggests-180986424/](https://www.smithsonianmag.com/smart-news/salmon-are-being-exposed-to-our-anti-anxiety-medication-and-its-making-them-take-more-risks-study-suggests-180986424/)

药物污染对大西洋鲑鱼的影响：以氯巴占为例

本文探讨了药物污染，特别是抗焦虑药物（氯巴占）对大西洋鲑鱼的影响。研究人员发现，暴露于氯巴占（浓度与受污染水道中的浓度相似）的鲑鱼，在从达尔河迁移到波罗的海的过程中表现出更冒险的行为。与未处理的鱼相比，这些受药物影响的鲑鱼迁移速度更快，通过水坝的速度更快，并且更有可能到达大海。

虽然这看起来可能是有益的，但科学家强调，改变后的行为可能产生负面影响。这些受药物影响的鲑鱼表现出独居倾向，更少一起集群（即使在捕食者存在时），并且可能更容易被吃掉。研究人员认为，该药物会降低它们的抑制性，导致它们做出可能危及生存的更冒险的选择。

该研究突出了药物污染这种“全球变化的隐形因素”对水生野生动物的更广泛威胁。虽然长期影响令人担忧，但文章也指出废水处理技术的进步和更快降解药物的开发，为减轻药物污染对环境的影响提供了希望。

---

## 75. 海绵、钻头和电线：外科医生错误地将异物遗留在数千人体内

**原文标题**: Sponges, drill bits and wires: Surgeons mistakenly left objects inside thousands

**原文链接**: [https://www.sfchronicle.com/projects/2025/hospitals-surgical-objects-patients/](https://www.sfchronicle.com/projects/2025/hospitals-surgical-objects-patients/)

无法访问文章链接。

---

## 76. Show HN: DeadDrop – 匿名分享文件的轻量级工具

**原文标题**: Show HN: DeadDrop – Tiny tool to share files anonymously

**原文链接**: [https://deaddrop.space/](https://deaddrop.space/)

DeadDrop：简单匿名的安全文件共享工具。

---

## 77. arXiv 迁移至谷歌云，不再使用康奈尔服务器

**原文标题**: arXiv moving from Cornell servers to Google Cloud

**原文链接**: [https://info.arxiv.org/hiring/index.html](https://info.arxiv.org/hiring/index.html)

arXiv正在进行重大项目“arXiv CE”，旨在将其所有服务从康奈尔的虚拟机迁移到谷歌云，该平台由康奈尔科技托管。此次迁移旨在提高arXiv的可扩展性并实现基础设施现代化，从而解决当前系统的局限性。

这次迁移不仅仅是一个简单的移植，它涉及到重要的架构重构，包括替换Perl和PHP后端，创建完全异步的文章处理流程，将服务容器化以便通过Kubernetes或谷歌云运行进行部署，以及增强监控/日志记录。一个关键成果将是构建一个强大的CI/CD管道。

这次云迁移是进一步现代化的先决条件，它将使arXiv能够扩展学科领域、改进文章元数据（包括资助者识别）、解决模糊的作者身份问题、增强残障用户的可访问性，并提高整体可用性。

arXiv正在招聘三名软件工程师来支持这项工作：一名通用软件工程师（需要Web开发和SQL经验），一名DevOps专家，负责领导DevOps现代化，采用基础设施即代码原则，并使用GitOps和谷歌云平台工具进行自动化，以及一名科学家/软件开发人员，他/她曾使用arXiv进行研究，并且能够代表科学界的需求。强烈倾向于可以在纽约市工作地点的候选人。

---

## 78. 美国低估了制造业回流的难度。

**原文标题**: America underestimates the difficulty of bringing manufacturing back

**原文链接**: [https://www.molsonhart.com/blog/america-underestimates-the-difficulty-of-bringing-manufacturing-back](https://www.molsonhart.com/blog/america-underestimates-the-difficulty-of-bringing-manufacturing-back)

莫尔森·哈特认为，美国近期旨在重振美国制造业的进口关税不太可能成功，甚至可能损害经济。他基于其在美国和中国15年的制造业经验，提出了14个理由佐证这一观点。

其核心论点是，由于美国工业供应链薄弱、缺乏专业技术以及劳动力效率较低，导致美国制造成本固有地更高，因此关税是不够的。他将美国强大的消费品供应链与其薄弱的工业供应链进行对比，强调了在美国本土采购制造零部件的困难。

他强调了中国劳动力卓越的职业道德和能力，中国在发电等基础设施方面的优势，以及在美国建设新工厂和基础设施所需的时间。

此外，关税政策的不确定性和复杂性正在冻结商业活动并阻碍投资。关税的不断变化和不明确的应用使得企业无法准确计算成本和规划未来。哈特还指出，大多数美国人不适合制造业工作，劳动的苛刻性质加上现有的劳动力短缺使得制造业的复兴不太可能。

---

## 79. Objective-C的主观魅力

**原文标题**: The Subjective Charms of Objective-C

**原文链接**: [https://www.wired.com/story/objective-c-programming-language-verbose/](https://www.wired.com/story/objective-c-programming-language-verbose/)

本文探讨了作者与Objective-C编程语言之间不断演变的关系，并以语言发展的历史背景和对“普遍语言”的追求为框架，这种“普遍语言”是一种完美代表现实的理想语言。

作者最初拥抱Objective-C的冗长而富有表现力的特性，发现在早期编程经历中，它赋予了自己力量。这种喜爱源于它的语法以及反映NeXT影响的传统前缀。然而，在一家成熟公司开发大型iPhone应用程序时，Objective-C的局限性显露了出来。它的冗长导致了复杂的代码库，阻碍了错误检测和协作。随着代码变得混乱且难以维护，最初“多多益善”哲学的魅力逐渐消退。

作者将这种经历与编程语言发展的更广泛趋势进行了对比，在这一趋势中，随着开发人员寻求更高效和更具表现力的工具，各种语言兴衰更替。这一周期最终以苹果公司推出Swift而告终，Swift是一种旨在解决Objective-C缺点的语言，其重点是简洁和清晰。

尽管作者越来越对Objective-C感到失望，但他仍然抵制向Swift的转变，认识到对完美语言的追求是一个持续的且最终难以实现的目标。最终，作者离开了软件工程，而一位新毕业生热情地拥抱Swift作为他们的“神圣语言”，突出了该领域语言偏好的周期性。这篇文章将此与莱布尼茨终生寻求通用语言联系起来，暗示了哲学理想和实际编码之间的相似之处。

---

## 80. OpenAI新推理AI模型更容易产生幻觉

**原文标题**: OpenAI's new reasoning AI models hallucinate more

**原文链接**: [https://techcrunch.com/2025/04/18/openais-new-reasoning-ai-models-hallucinate-more/](https://techcrunch.com/2025/04/18/openais-new-reasoning-ai-models-hallucinate-more/)

TechCrunch文章报道称，OpenAI最新的推理AI模型o3和o4-mini相比于之前的OpenAI模型，包括之前的推理模型(o1, o1-mini, o3-mini)甚至非推理模型GPT-4o，都表现出更高的“幻觉”率（编造信息）。OpenAI的内部测试显示，在PersonQA等基准测试中，幻觉率显著增加，o3的幻觉率为33%，o4-mini更是高达48%。

文章强调，OpenAI并不完全清楚为何会出现这种情况，认为可能与“o系列”模型中使用的强化学习有关。Transluce的独立测试证实了这个问题，发现o3会捏造其推理过程中采取的行动。虽然o3在编码和数学等领域表现出色，但较高的幻觉率可能会限制其在依赖准确性的领域的实用性。

文章还提到，像GPT-4o那样，通过网络搜索来增强模型能力可以提高准确性。旨在提高性能而不消耗过多计算能力的推理模型的发展趋势，正在带来一个挑战，因为它似乎加剧了幻觉问题。OpenAI承认了这个问题，并强调正在进行的研究以提高模型的准确性和可靠性。Kian Katanforoosh指出O3倾向于产生无效的网站链接幻觉。

---

## 81. 大学城：昔日都市主义

**原文标题**: College Towns: Urbanism from a Past Era

**原文链接**: [https://www.governance.fyi/p/college-towns-urbanism-from-a-past](https://www.governance.fyi/p/college-towns-urbanism-from-a-past)

本文采访了美国创价大学教授、"大学城"通讯作者瑞安·艾伦，重点讨论高等教育与城市化的交叉领域。艾伦探讨了他从学术出版转向公共写作的原因，这是出于更快传播思想的愿望。他对日益萎缩的学术就业市场和博士过剩表示担忧，建议潜在的学生在攻读博士学位前仔细考虑他们的职业前景。

艾伦强调了大学在保护可步行的城市环境方面的独特作用，并将其与改变了美国大部分地区的郊区蔓延形成对比。他还谈到了“校镇”冲突，当地居民经常反对学生住房，尽管他们住在校园附近。艾伦认为，城市规划者应该专注于防止停滞和蔓延，而不是与邻避主义作斗争。

随后，对话转向了教职工的工作状况，引用了加州大学洛杉矶分校一位无家可归教授的例子，以及更广泛的“兼职化”问题。艾伦将这些问题归因于高等教育的长期趋势，而不仅仅是特朗普政府。

最后，艾伦讨论了中国大学在STEM领域的崛起，并指出Deep Seek的人工智能团队主要在中国接受培训，这挑战了美国机构是唯一专业知识来源的假设。他承认美国仍然有优势，但受到当前政策决定的阻碍。他指出，STEM领域的博士与人文和社会科学领域的博士的就业前景存在差异。

---

## 82. 使用神经变分热距离的非定向点云 SDF

**原文标题**: SDFs from Unoriented Point Clouds Using Neural Variational Heat Distances

**原文链接**: [https://arxiv.org/abs/2504.11212](https://arxiv.org/abs/2504.11212)

本文介绍了一种新颖的变分方法，用于从无向点云计算神经符号距离场(SDF)。作者没有依赖常用的程函方程，而是提出使用热方法，将一种用于离散表面的标准技术应用于神经网络领域。这涉及使用神经网络解决两个凸优化问题。

首先，一个神经网络通过模拟以加权点云密度为初始数据的短时间热流，来近似无符号距离场的梯度。然后，另一个神经网络使用这些梯度来计算SDF的神经近似。作者证明了底层变分问题的适定性。

论文通过数值实验突出了该方法的优势，证明了最先进的表面重建和一致的SDF梯度。此外，一个概念验证表明该方法在求解重建曲面零水平集上的PDE时的准确性。论文包含14页，16个图表和4个表格，展示了这些结果。该工作属于数值分析、图形学和机器学习的范畴。

---

## 83. 月饼：一种以 KVCache 为中心的 LLM 服务解耦架构

**原文标题**: Mooncake: A KVCache-centric Disaggregated Architecture for LLM Serving

**原文链接**: [https://github.com/kvcache-ai/Mooncake](https://github.com/kvcache-ai/Mooncake)

Mooncake：一种面向KVCache的解耦架构，用于服务大型语言模型（LLMs），由Moonshot AI为Kimi服务开发。它分离了预填充和解码集群，利用GPU集群中未充分利用的CPU、DRAM和SSD资源来创建一个解耦的KVCache。其核心是一个面向KVCache的调度器，旨在最大化吞吐量，同时满足服务等级目标（SLOs），并结合了基于预测的早期拒绝策略来处理过载场景。实验表明，与基线方法相比，吞吐量显著提高（模拟中高达525%），并且在实际工作负载下处理的请求增加了75%。

该架构依赖于几个关键组件：用于通过各种协议（TCP、RDMA、NVMe-of）进行高效可靠数据传输的传输引擎、用于共享检查点等临时对象的P2P存储，以及对vLLM的修改，以便使用RDMA进行高效的预填充-解码解耦。Mooncake存储是利用传输引擎的分布式KVCache存储引擎。

性能亮点包括传输引擎在特定RoCE网络中实现高带宽（高达190 GB/s），P2P存储充分利用硬件传入带宽，以及与基于TCP的传输相比，vLLM集成通过拓扑感知路径选择和多卡带宽聚合实现了高达25%的更低平均TTFT（首字时间）。

Mooncake已经开源了其传输引擎和Mooncake存储，以及用于评估的traces。SGLang和vLLM正式支持该传输引擎。

---

## 84. 群晖硬盘锁死操作迷失方向

**原文标题**: Synology Lost the Plot with Hard Drive Locking Move

**原文链接**: [https://www.servethehome.com/synology-lost-the-plot-with-hard-drive-locking-move/](https://www.servethehome.com/synology-lost-the-plot-with-hard-drive-locking-move/)

本文批评了群晖(Synology)传闻中计划于2025年对其“Plus”系列NAS设备锁定功能，使其只能使用自家品牌硬盘的做法。作者认为，这是一种有害的行为，其驱动力是为了提高利润率，最终损害客户利益。

作者强调，如果使用非群晖硬盘，硬盘健康状况报告、卷级重复数据删除、寿命分析和自动固件更新等功能将受到限制。此外，存储池的创建和支持也会受到影响。

作者指出，群晖硬盘的容量落后于西部数据(WD)红盘Pro等竞争对手，限制了用户的存储潜力。他们还对硬盘的可用性、更换速度以及未来更换完全依赖于群晖的持续存在和硬盘生产的风险表示担忧。

文章强调了群晖在硬盘市场缺乏竞争优势，表明他们很可能只是对现有硬盘进行重新贴牌。作者总结说，群晖的硬件已经过时，而这种厂商锁定进一步降低了群晖NAS解决方案的吸引力，使得与威联通(QNAP)和TrueNAS等替代方案相比，群晖的产品难以推荐。

---

## 85. 观看艺术对幸福感的影响——一项关于效果的系统性综述

**原文标题**: The impact of viewing art on well-being–a systematic review of the effects

**原文链接**: [https://www.tandfonline.com/doi/full/10.1080/17439760.2025.2481041](https://www.tandfonline.com/doi/full/10.1080/17439760.2025.2481041)

无法访问文章链接。

---

## 86. Pahole：轻松分析复杂数据结构的内存布局

**原文标题**: Pahole: Analysing Memory Layout of Complex Data Structures with Ease

**原文链接**: [https://pramodkumbhar.com/2023/11/pahole-to-analyz-data-structure-memory-layouts-with-ease/](https://pramodkumbhar.com/2023/11/pahole-to-analyz-data-structure-memory-layouts-with-ease/)

本文介绍了`pahole`，一个用于分析 C/C++ 数据结构内存布局的工具。作者受到其在 perf C2C 工具方面工作的启发，发现 `pahole` 在检查填充和对齐方面非常有用，尤其是在处理大型或不熟悉的代码库时。

本文解释了理解数据结构布局对于缓存效率和避免伪共享的重要性。编译器通常插入填充以满足对齐要求，这会增加对象大小并影响性能。

作者提供了安装 `pahole` 的实用指南，并演示了其在表示神经元组件的示例 C++ 数据结构中的用法。`pahole` 从编译后的对象（使用 `-g` 标志创建）读取 DWARF 调试信息，并以易于理解的格式呈现内存布局，包括偏移量、大小和填充。

示例包括：
*   显示 `Channel` 结构体的内存布局，突出显示编译器添加的填充。
*   演示在 32 位架构上的布局差异。
*   使用 `--reorganize` 选项重新排序结构体成员，以获得更紧凑的内存布局，从而减小结构体大小并提高缓存利用率。

---

## 87. Erlang/OTP SSH 中的未经验证的远程代码执行漏洞

**原文标题**: Unauthenticated Remote Code Execution in Erlang/OTP SSH

**原文链接**: [https://nvd.nist.gov/vuln/detail/CVE-2025-32433](https://nvd.nist.gov/vuln/detail/CVE-2025-32433)

本文详细描述了CVE-2025-32433，Erlang/OTP SSH服务器中的一个未经身份验证的远程代码执行（RCE）漏洞。受影响版本包括OTP-27.3.3之前的版本、OTP-26.2.5.11之前的版本以及OTP-25.3.2.20之前的版本。该漏洞源于SSH协议消息处理中的一个缺陷，允许攻击者绕过身份验证并在受影响的系统上执行任意命令。

GitHub, Inc. 赋予了该漏洞关键（CRITICAL）等级的CVSS 3.1评分10.0，向量为CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H。NVD分析正在进行中，目前尚未分配CVSS评分。该漏洞归因于CWE-306，关键功能的身份验证缺失。

OTP-27.3.3、OTP-26.2.5.11和OTP-25.3.2.20版本中已提供补丁。临时解决方案包括禁用SSH服务器或实施防火墙规则以限制访问。提供了多个参考链接，包括指向Openwall邮件列表、解决该漏洞的GitHub提交以及GitHub安全公告的链接。该CVE最初于2025年4月16日报告，并于2025年4月19日最后修改。

---

## 88. 数据包大小

**原文标题**: The Size of Packets

**原文链接**: [https://www.potaroo.net/ispcol/2024-10/packet-sizes.html](https://www.potaroo.net/ispcol/2024-10/packet-sizes.html)

本文探讨了分组交换网络中最佳数据包大小的问题，重点关注以太网的演变及其对互联网协议的影响。最初，为了避免分片或报头截断，20-1500 字节的实用大小被认为是互联网数据包的理想选择。RFC 791 建议接受高达 576 字节的数据包。以太网专为局域网设计，使用 46-1500 字节的帧有效载荷，并额外使用 18 字节进行成帧。最小以太网数据包大小与冲突检测有关，而最大大小则有利于传输效率。

本文讨论了物理限制，例如光速和信号传播，如何影响早期以太网设计。随着时间的推移，出现了更快的以太网版本（100Mbps、1Gps、10Gbps、100Gbps 以及正在进行的兆兆位以太网的努力），但帧大小基本保持不变，以保持向后兼容性。

本文还探讨了巨型帧（大约 9,000 字节），旨在解决传输速度和硅处理能力之间日益扩大的差距，但作为一种非标准化解决方案，存在兼容性问题。网络接口卡级别的 TCP 分段卸载也减轻了基于主机的大帧压力。虽然 IP 支持大数据包（高达 65,535 字节），但分片使得它们对公共互联网来说问题重重，从而导致了分段成本和数据包丢弃风险之间的权衡。

---

## 89. DeepSeek分布式文件系统入门

**原文标题**: An intro to DeepSeek's distributed file system

**原文链接**: [https://maknee.github.io/blog/2025/3FS-Performance-Journal-1/](https://maknee.github.io/blog/2025/3FS-Performance-Journal-1/)

本文介绍了DeepSeek的开源分布式文件系统3FS（萤火虫文件系统），并阐述了其核心原理和架构。分布式文件系统抽象了数据在多台机器上碎片化的复杂性，允许用户像与本地存储的文件一样进行交互。3FS具有海量数据服务能力、高吞吐量、容错性和冗余等优点，使其适用于并行处理、机器学习训练和大规模数据仓库等应用。

3FS由四种主要节点类型组成：Meta（管理元数据）、Mgmtd（管理集群配置和节点发现）、Storage（存储实际文件数据）和Client（与其他节点交互）。Mgmtd节点跟踪节点可用性并促进节点发现。Meta节点使用构建在FoundationDB上的元数据存储来处理文件系统操作。Storage节点管理物理磁盘上的数据，使用Rust ChunkEngine和LevelDB将其划分为块。

文章随后深入探讨了CRAQ（具有分配查询的链式复制），这是3FS用于强一致性和容错性的协议。CRAQ确保写入沿节点链传播，在尾部提交之前标记为“脏”，然后在提交消息传播期间标记为“干净”。如果对象是“脏”的，则从尾部提供读取服务。

最后，文章简要地将3FS与其他分布式文件系统进行了比较，指出虽然高层组件相似，但具体的实现细节和适用性有所不同。作者表示他们计划在未来的博客文章中对3FS进行深入的性能分析，以解决关于其优势、劣势和潜在改进的未决问题。

---

## 90. 谷歌非法垄断在线广告技术，法官裁定

**原文标题**: Google is illegally monopolizing online advertising tech, judge rules

**原文链接**: [https://www.nytimes.com/2025/04/17/technology/google-ad-tech-antitrust-ruling.html](https://www.nytimes.com/2025/04/17/technology/google-ad-tech-antitrust-ruling.html)

联邦法官裁定谷歌非法垄断部分在线广告技术市场，具体是指供出版商托管广告空间的工具以及促进广告交易的软件。法官Leonie Brinkema裁定谷歌违反《谢尔曼反垄断法》，并表示该公司蓄意获取并维持垄断力量，损害了竞争对手、出版商以及最终的消费者。

美国司法部和一批州起诉谷歌，认为其主导地位使其能够抬高价格并攫取更多广告销售分成。虽然政府声称谷歌垄断了市场的三个部分（出版商工具、广告商工具和软件系统），但法官仅支持政府对其中两部分的指控：出版商工具和软件系统。谷歌垄断广告商工具的指控被驳回。

该裁决增加了谷歌现有的法律麻烦，并有可能重塑该公司及其对互联网的影响力。该案件凸显了谷歌对这个复杂的、通常隐形的网络广告投放系统的影响力。

---

## 91. Kagi助手现已面向所有用户开放

**原文标题**: Kagi Assistant is now available to all users

**原文链接**: [https://blog.kagi.com/assistant-for-all](https://blog.kagi.com/assistant-for-all)

Kagi助手，这款原先仅供Ultimate订阅用户使用的强大AI工具，现已免费向所有Kagi用户开放。本次发布将按地区分阶段进行，首先从美国开始，预计将在世界协调时周日23:59前完成。Kagi强调，AI应增强而非取代人类研究，其助手在Kagi搜索结果的上下文中工作，尊重隐私和AI的局限性。

主要功能包括：基于Kagi搜索的AI，尊重个人域名排名和Lenses；可选择禁用网络访问并上传文件以提供上下文；通过独特的指令和自定义“bangs”定制满足特定需求的自定义助手；可在对话中编辑提示词和切换模型；以及以隐私为中心的方法，默认情况下线程是私有的，会根据设置过期，且交互数据不会用于模型训练。

为确保可持续性，Kagi正在执行其合理使用政策，将AI模型的使用与计划的价值联系起来（例如，一个25美元的计划允许价值25美元的原始token成本）。他们估计95%的用户不会受到影响。超出阈值的用户可以提前续订订阅或使用信用充值。可使用来自OpenAI、Anthropic、Google和Mistral的各种领先LLM，Ultimate计划提供更广泛的选择。较便宜的模型使用的积分更少。可以在“消费”页面上监控token使用情况。

---

## 92. 构建单次学习型人工智能体的原则

**原文标题**: Principles for Building One-Shot AI Agents

**原文链接**: [https://edgebit.io/blog/automated-dependency-updates-with-ai/](https://edgebit.io/blog/automated-dependency-updates-with-ai/)

本文概述了构建用于自动化代码维护的“一次性”AI代理的原则，重点介绍了EdgeBit的依赖自动修复功能。一次性代理无需人工干预即可自主执行复杂任务。EdgeBit通过静态分析、依赖更新执行和一致的代理工作流程来实现这一点。

本文强调了三个关键原则：

1. **专注工具胜过通用工具：** 具有明确边界的特定工具比通用工具更有效。它们可以在不成功时及早退出，并提供有意义的错误反馈，从而防止混乱的循环。工具应封装常见的任务，如构建、测试和更新，并使用经过验证的库来执行语义版本比较等任务。

2. **要么果断失败，要么温和失败，而非出错：** 建立硬性失败和软性失败机制，确保EdgeBit提供始终成功的更新。硬性失败发生在代理退出问题空间时（例如，无法计算有效的更新图）。软性失败提供温和的提示，例如要求使用特定版本号而不是“最新”。

3. **坚持：过度执着适得其反：** LLM可能会陷入循环。专注的工具和硬/软失败可以防止这种情况。例如，阻止代理尝试安装Node（如果不可用），或将研究限制在专门的项目研究工具中，而不是直接搜索GitHub。

本文将EdgeBit的一次性代理与Claude Code进行了比较，证明了该代理具有更高的稳定性和正确性。作者强调，在一次性工作流程中，正确的结果优先于一切。

---

## 93. 脂肪组织在减重后保留了肥胖的表观遗传记忆

**原文标题**: Adipose tissue retains an epigenetic memory of obesity after weight loss

**原文链接**: [https://www.nature.com/articles/s41586-024-08165-7](https://www.nature.com/articles/s41586-024-08165-7)

本研究调查了“肥胖记忆”现象，即身体在体重减轻后恢复体重的倾向及其潜在机制。研究人员利用单细胞核RNA测序发现，即使通过减重手术（在人类中）或饮食改变（在小鼠中）实现了显著的体重减轻，人类和小鼠的脂肪组织仍然保留着细胞转录变化。

具体来说，他们观察到小鼠脂肪细胞的表观基因组持续发生改变，这对其功能和对代谢刺激的反应产生了负面影响。表现出这种肥胖记忆的小鼠在再次暴露于高脂肪饮食时，体重恢复加速。这些表观遗传变化可以预测脂肪细胞未来发生的转录失调。

该研究表明，脂肪组织中的脂肪细胞、脂肪细胞祖细胞（APCs）和内皮细胞在体重减轻后表现出最显著的转录差异保留。脂肪细胞中下调的基因包括与代谢和功能相关的基因，而上调的基因与纤维化和细胞凋亡有关。

在小鼠中，体重减轻部分逆转了一些代谢损伤，但一些问题，如葡萄糖不耐受和肝脏脂肪变性仍然存在。重要的是，该研究表明，这些稳定的表观遗传变化使细胞为肥胖环境中的病理反应做好准备，从而导致“溜溜球”节食效应。研究结果表明，靶向这些表观遗传变化可能有助于改善长期体重管理和健康状况。

---

## 94. 1700年老蛋未碎

**原文标题**: 1,700 year old egg never broke

**原文链接**: [https://www.atlasobscura.com/articles/liquid-inside-ancient-egg](https://www.atlasobscura.com/articles/liquid-inside-ancient-egg)

英国考古学家出土一枚1700年前的鸡蛋，它在罗马时代的许愿井中浸泡数世纪后仍完好无损。这枚鸡蛋在贝里菲尔德遗址被发现，该地点富含罗马文物，被认为是迄今为止发现的最古老的意外保存下来的鸡蛋。

该遗址曾被罗马人用作提取酿造麦芽酒的水源，后来转变为祭祀场所。这枚鸡蛋之所以能保存下来，归功于富含粘土的含水土壤中的厌氧环境，这种环境通过排除氧气阻止了分解。它与破碎的蛋壳一起被发现，表明鸡蛋在罗马文化中具有仪式用途，通常与生育和繁殖有关。

微型CT扫描显示，这枚鸡蛋仍然含有液体，推测来自蛋黄和蛋白。科学家们计划通过一个受控的过程小心地提取这种液体，并事先创建一个3D模型。其目标是使用DNA测试和其他分子技术分析鸡蛋的内容物，以确定产下它的鸟类物种，很可能是鸡，鸡在罗马时代是一种受人尊敬的动物。

这项分析可以为了解罗马文化提供宝贵的见解，包括祭祀活动、动物引进以及动物在传统治疗中的使用。经过广泛的研究和保护后，这枚鸡蛋最终将在伦敦自然历史博物馆展出。它的完整状态非常罕见，因为考古学家通常只在此类遗址发现蛋壳碎片。

---

## 95. mIRC 7.81

**原文标题**: mIRC 7.81

**原文链接**: [https://www.mirc.com/](https://www.mirc.com/)

mIRC 7.81是广受欢迎的互联网中继聊天（IRC）客户端的最新版本。二十多年来，mIRC一直为互联网社区服务，并已发展成为一个强大而可靠的工具，用于在全球IRC网络上进行通信、共享、游戏和工作。

该网站提供有关mIRC的信息，包括其用途、下载链接、注册详情以及突出显示最新版本（v7.81）的新闻部分。用户可以加入邮件列表，以接收有关新版本的电子邮件通知。该网站还鼓励用户访问论坛，以获得帮助并与其他mIRC用户互动。

该网站提供指向重要页面的链接，如关于、下载、注册、新闻和帮助。它还包括隐私政策和联系我们信息。版权声明表明，mIRC Co. Ltd.自1995年以来一直在维护该软件，并将至少持续到2025年。

---

## 96. AMP 以及为何电子邮件不是（且永远不应是）交互式的

**原文标题**: AMP and why emails are not (and should never be) interactive

**原文链接**: [https://buttondown.com/blog/whatever-happened-to-amp-email](https://buttondown.com/blog/whatever-happened-to-amp-email)

谷歌试图用AMP（加速移动页面）革新电子邮件的尝试及其失败原因：AMP旨在使电子邮件具有交互性，允许用户直接从收件箱执行诸如预订航班或回复评论等操作。

作者认为，电子邮件的优势在于其简单性、通用性和持久性。与网络不同，电子邮件是去中心化的，并且可以在所有平台上可靠地工作。引入AMP威胁了这些核心价值。

虽然AMP带来了一些交互式元素，但它需要开发人员付出巨大的努力来创建每个电子邮件的AMP、HTML和纯文本版本。此外，它仅受到少数电子邮件客户端的支持。作者强调了开发人员对谷歌这一举措的不信任，这源于谷歌在网络上推广AMP时所使用的强制手段，以及对谷歌垄断倾向的担忧。

最终，谷歌放弃了AMP，尽管该公司继续使用一个名为动态电子邮件的版本。作者总结说，电子邮件的交互性不需要AMP；标准的HTML元素可以实现类似的结果。最重要的是，AMP引入的短暂性，即电子邮件内容可以动态变化，危及了电子邮件作为可靠通信记录的角色。作者预测，虽然电子邮件将继续缓慢发展，但其基本特征和对激进变革的抵制将持续存在。

---

## 97. Show HN: AgentAPI – Claude Code、Goose、Aider 和 Codex 的 HTTP API

**原文标题**: Show HN: AgentAPI – HTTP API for Claude Code, Goose, Aider, and Codex

**原文链接**: [https://github.com/coder/agentapi](https://github.com/coder/agentapi)

AgentAPI是一个工具，它提供了一个HTTP API，用于控制各种编码助手，如Claude Code、Goose、Aider和Codex。这允许开发者构建统一的聊天界面，创建助手之间的通信系统，或开发用于自动化代码审查的工具。

该API支持多种功能：向助手发送消息、检索对话历史、检查助手状态（稳定/运行）以及接收事件流（消息和状态更新）。它的工作原理是模拟终端，将API调用转换为按键操作，并将助手的终端输出解析为单独的消息。此过程包括智能地移除无关的TUI元素，如回显的用户输入和输入框。

AgentAPI提供CLI命令来启动服务器（`agentapi server`）和附加到运行中助手的终端会话（`agentapi attach`）。提供了一个OpenAPI模式，用于集成目的。提供了一个演示Web聊天界面来测试API。

开发者承认，对编码助手TUI的更改可能需要更新AgentAPI的消息解析逻辑，但坚持认为核心功能将保持不变。未来的计划包括支持MCP和Agent2Agent协议。AgentAPI的长期愿景是，如果助手供应商不采用标准化API，则充当通用适配器，允许开发者在不同的编码助手之间切换而无需更改代码。

---

## 98. 谷歌人... 前谷歌人

**原文标题**: Googler... ex-Googler

**原文链接**: [https://nerdy.dev/ex-googler](https://nerdy.dev/ex-googler)

谷歌Chrome团队成员Adam突然失业，震惊、愤怒，并感到背叛。他被告知职位取消并非基于绩效，而且他有可能在公司内部找到其他职位。然而，他立即被取消了对谷歌系统的访问权限，这让他感到不受欢迎，并像罪犯一样被对待。

时机尤其令人震惊，因为这发生在一次富有成效且愉快的Chrome团队线下会议之后，他在会上积极为网络开发创新做出贡献。他强调失去了许多职责和机会，包括录制Google I/O视频、在Google I/O上发言、运营展位、为开发者主题演讲做出贡献以及参与CSS相关项目。他的CSS工作组成员资格、开发者办公时间、代码访问权限以及未来参与诸如Overflow 5等项目的机会全部终止。

他哀叹失去了辛辛苦苦建立起来的人际关系，并感到自身价值被贬低，将自己比作庞大公司中的一颗螺丝钉。他表达了被背后捅刀子、不被赏识和可有可无的感觉。他提供了他的Bluesky和个人电子邮件地址以便联系，预计可能会收到大量回复，并预先为延迟回复道歉。这次突然而彻底的失业让他感到晕头转向，情绪崩溃。

---

## 99. MCP运行Python

**原文标题**: MCP Run Python

**原文链接**: [https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python](https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python)

本文介绍了`@pydantic/mcp-run-python`，这是一个模型上下文协议（MCP）服务器，它使用Pyodide在Deno中的沙盒环境中执行Python代码。这种隔离增强了安全性。该服务器旨在与PydanticAI等工具一起使用。

要运行服务器，本文提供了一个带有特定标志的`deno run`命令：`-N -R=node_modules -W=node_modules`，用于对`node_modules`目录的网络和读/写访问（Pyodide需要此目录来下载和缓存Python库），以及`--node-modules-dir=auto`，以指示Deno使用本地`node_modules`目录。

该命令支持三种模式：`stdio`（用于使用Stdio MCP传输的本地子进程执行）、`sse`（用于使用SSE MCP传输的HTTP服务器执行，允许本地或远程连接）和`warmup`（用于下载和缓存Python标准库并检查服务器功能）。

本文提供了一个完整的示例，演示了如何将`@pydantic/mcp-run-python`与PydanticAI集成，包括使用`MCPServerStdio`类初始化服务器以及通过代理运行Python代码执行请求。该示例使用`logfire`来检测和监控MCP交互以及代理的性能。

---

## 100. 邮寄土豆

**原文标题**: Potatoes in the Mail

**原文链接**: [https://facts.usps.com/mailing-potatoes/](https://facts.usps.com/mailing-potatoes/)

邮件里的土豆

---

