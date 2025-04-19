# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-04-19.md)

*最后自动更新时间: 2025-04-19 17:45:24*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 2 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 3 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 4 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 5 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 6 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 7 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 8 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 9 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 10 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 11 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 12 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 13 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 14 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 15 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 16 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 17 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 18 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 19 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 20 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 21 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 22 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 23 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 24 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 25 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 26 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 27 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 28 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 29 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 30 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 31 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
