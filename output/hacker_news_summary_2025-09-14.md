# Hacker News 热门文章摘要 (2025-09-14)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 泰国央行冻结300万账户，设定每日转账限额以遏制诈骗

**原文标题**: Bank of Thailand Freezes 3MM Accounts, Sets Daily Transfer Limits to Curb Fraud

**原文链接**: [https://www.thaienquirer.com/57752/bot-freezes-3-million-accounts-sets-daily-transfer-limits-of-50000-200000-baht-to-curb-6-billion-baht-scam-losses/](https://www.thaienquirer.com/57752/bot-freezes-3-million-accounts-sets-daily-transfer-limits-of-50000-200000-baht-to-curb-6-billion-baht-scam-losses/)

泰国银行冻结了与诈骗活动相关的300万个银行账户，并实施了更严格的每日交易限额，以打击激增的诈骗活动，这些活动已使泰国人损失估计达60亿泰铢。新的每日转账限额设定在5万至20万泰铢之间，远低于之前的限额。

此举旨在扰乱诈骗分子的运作，并减少对受害者的潜在经济损失。泰国银行的行动是在公众压力日益增加以及政府为解决日益严重的网络诈骗问题采取行动之后进行的。这些被冻结的账户涉嫌被用作通过各种诈骗获得的非法资金的中转点。

虽然降低转账限额的目的是保护消费者，但人们担心这可能会给经常进行较大交易的合法用户带来不便。预计泰国银行将提供进一步的指导和支持，以确保真正的交易不会受到不当影响。这项举措是泰国银行和泰国当局为加强网络安全和提高公众对网络诈骗的认识而做出的更广泛努力的一部分。

---

## 2. 从零开始编写操作系统内核

**原文标题**: Writing an operating system kernel from scratch

**原文链接**: [https://popovicu.com/posts/writing-an-operating-system-kernel-from-scratch/](https://popovicu.com/posts/writing-an-operating-system-kernel-from-scratch/)

本文详细介绍了使用 Zig 语言为 RISC-V 架构编写一个极简的时间片操作系统内核的过程。它面向那些旨在了解底层系统软件、驱动程序和系统调用的个人。作者重新审视了一个操作系统项目，重点关注现代工具以及以其可理解性和普及性而闻名的 RISC-V 架构。

该内核设计为 unikernel，将应用程序代码直接与 OS 内核链接，从而简化了用户代码加载。它利用 RISC-V 分层权限模型（M、S 和 U 模式），并利用 OpenSBI 进行控制台打印和计时器控制，绕过手动实现以提高可移植性。

该内核旨在支持在用户模式（U-mode）下运行的静态定义的、永不终止的线程，这些线程能够向内核（S-mode）发送系统调用。时间片轮转通过计时器中断实现，用于在单核机器上进行上下文切换。

核心概念涉及虚拟化内核，使得每个线程“感觉”好像拥有一个虚拟内核。这是通过提供相同的编程模型来实现的，但每个线程只能访问其自身的堆栈和架构寄存器，而内存是共享的。

该实现利用中断处理机制在线程之间进行切换。它通过使用中断例程将堆栈指针交换到不同的内存块来实现，从而恢复不同的架构寄存器值，从而实现上下文切换。

---

## 3. 欧洲地铁站模型

**原文标题**: Models of European Metro Stations

**原文链接**: [http://stations.albertguillaumes.cat/](http://stations.albertguillaumes.cat/)

本文概述了欧洲各城市以及布宜诺斯艾利斯和波士顿的地铁和快速 transit 系统，重点介绍了车站布局、换乘设计和历史背景。

它详细介绍了每个城市系统的具体特征。例如，阿利坎特的 TRAM 拥有带夹层和侧式站台的地下线路，而阿姆斯特丹的地铁则包括地下和地上部分。安特卫普的 premetro 连接着城市的各个部分，在换乘枢纽处有复杂的车站布局。巴塞罗那以其长长的换乘通道和“西班牙式解决方案”站台设计而闻名。柏林的 U-Bahn 通常位于地下，而 S-Bahn 位于地上，具有简单的换乘拓扑结构。

本文还介绍了独特的方面，例如波士顿由于早期施工方法而产生的不同寻常的市中心车站，以及布鲁塞尔计划从 premetro 过渡到完整地铁线路的系统。布达佩斯的地铁是欧洲大陆最古老的地铁，拥有狭窄的隧道，而布加勒斯特的系统则采用明挖回填法建造。

本文重点介绍了建设过程中面临的挑战，例如巴塞罗那的地铁扩建滞后于城市发展，以及适应城市地形，例如在毕尔巴鄂。文章还介绍了现代系统，如哥本哈根的自动地铁和汉诺威的 Stadtbahn。

---

## 4. 我们盘旋

**原文标题**: We Spiral

**原文链接**: [https://behavioralscientist.org/why-we-spiral/](https://behavioralscientist.org/why-we-spiral/)

我们螺旋式下降：探讨自我破坏性螺旋，解释看似微小的事件如何触发负面思维模式并导致不利的结果。文章以一名初级员工Zoom会议迟到，并将老板的评论解读为讽刺为例，说明了如何引发一连串的怀疑和悲观推断。

文章将这种螺旋式下降分解为三个关键组成部分，即“三个C”：**核心问题**、**构建**和**固化**。核心问题与身份、归属感和能力有关，当这些问题未解决时，会像透镜一样影响我们对世界的解读。构建是解释事件的过程，我们容易受到证实偏差的影响，寻求支持我们预先存在的信念的证据。固化是指消极的想法和感受变得根深蒂固，往往导致自我破坏行为。

作者强调，这些消极的螺旋式下降并非不可避免，并提倡“明智干预”——采取积极措施来中断这些模式。通过理解潜在的核心问题并提供替代性的、积极的视角，我们可以转向向上螺旋，从而促进幸福、成功和福祉。作者最后分享了一个关于在大学活动中感到被排斥的个人轶事，突出了看似微不足道的经历如何引发更深层次的不安全感，以及认识和解决这些潜在焦虑的重要性。

---

## 5. Observable Notebooks 数据加载器

**原文标题**: Observable Notebooks Data Loaders

**原文链接**: [https://observablehq.com/notebook-kit/data-loaders](https://observablehq.com/notebook-kit/data-loaders)

Observable Notebooks 数据加载器是特殊的单元格，它们在构建时使用解释器（Node.js 或 Python）执行，而不是在浏览器中实时运行。它们对于预处理静态数据、确保一致性、稳定性和提高性能非常有用，可以看作是数据库连接器的推广。

目前支持 Node.js 和 Python，并计划支持更多解释器。数据加载器支持多种输出格式，包括文本、JSON、CSV、XML、Arrow、Parquet、Blob、Buffer、图像（JPEG、GIF、WebP、PNG、SVG）和服务器端渲染的 HTML。

数据加载器单元格的输出缓存在笔记本旁边的 `.observable/cache` 目录中，仅在重新运行单元格时更新。在 Observable Desktop 中，重新运行通过“播放”按钮或 Shift-Return 完成。在 Notebook Kit 中，从缓存中删除文件，或通过持续部署自动刷新。

Node.js 数据加载器需要安装在特定位置的 Node.js 22.12+，并支持 TypeScript（有局限性）。通过限制文件访问到笔记本的目录来强制执行安全性。安装的软件包必须位于同一目录中。

Python 数据加载器需要安装在特定位置的 Python 3.12+，如果存在虚拟环境（.venv），则自动使用。软件包安装通过 pip 手动进行，建议使用 `pip freeze` 生成 `requirements.txt` 文件。

---

## 6. GrapheneOS 简介

**原文标题**: Introduction to GrapheneOS

**原文链接**: [https://dataswamp.org/~solene/2025-01-12-intro-to-grapheneos.html](https://dataswamp.org/~solene/2025-01-12-intro-to-grapheneos.html)

本文介绍了GrapheneOS (GOS)，一个注重安全的Android操作系统，专为Google Pixel设备设计。GOS通过使用配置文件来优先考虑用户控制和隐私。每个配置文件都像一个独立的手机实例，彼此隔离，具有单独的加密和权限设置。用户可以为每个配置文件定制权限，包括网络访问和联系人访问。

作者强调了通过Web界面安装的便捷性和无缝的OTA更新，这比他们在LineageOS上的体验有了显著的改进。一个关键特性是细粒度的权限管理，允许用户定义存储和联系人访问的范围，以及Google Play服务的沙盒化。

作者详细介绍了他们的个人工作流程，为各种活动（如工作、多媒体、游戏和不受信任的应用）使用单独的配置文件。这种方法隔离了数据并限制了后台活动。Pixel 8a的OLED屏幕、Wi-Fi 6和电池续航能力受到称赞，但缺少SD卡支持也被指出。

与原生Android相比，GrapheneOS提供了广泛的安全增强功能，尽管没有root权限。作者总结说，GOS为智能手机用户提供了前所未有的控制和安全性，但也承认它可能不会吸引所有对当前操作系统感到满意的人。文章建议探索Android内置的配置文件功能，虽然安全性较低，但可能提供有限的隔离。

---

## 7. 环保署试图取消关键的全氟/多氟烷基物质饮用水保护措施

**原文标题**: EPA Seeks to Eliminate Critical PFAS Drinking Water Protections

**原文链接**: [https://earthjustice.org/press/2025/epa-seeks-to-roll-back-pfas-drinking-water-rules-keeping-millions-exposed-to-toxic-forever-chemicals-in-tap-water](https://earthjustice.org/press/2025/epa-seeks-to-roll-back-pfas-drinking-water-rules-keeping-millions-exposed-to-toxic-forever-chemicals-in-tap-water)

2025年9月12日的一篇“地球正义”文章报道，环保署正试图取消对饮用水中PFAS“永久化学品”的关键保护措施。环保署要求联邦法院推翻去年实施的法律保护措施，特别是针对GenX、PFHxS、PFNA和PFBS的监管规定。他们还试图延长PFOA和PFOS标准的合规期限。

“地球正义”组织和其他环保团体，如NRDC，批评这一举动，认为它将行业利润置于公众健康之上，并试图规避《安全饮用水法》的反滑坡条款，该条款旨在防止削弱现有的水质标准。他们声称，环保署署长泽尔丁违背了他保护美国人免受PFAS污染的承诺。

文章强调，PFAS广泛存在，污染了美国约2亿人的饮用水，并与包括癌症和荷尔蒙紊乱在内的多种健康问题有关。“地球正义”组织代表多个社区团体，正在介入，以在法庭上捍卫当前的标准，对抗来自化学公司和自来水公司的挑战。最初的规则于2024年4月最终确定，对六种PFAS化学品设定了限制，并要求供水系统在2029年4月之前监测和报告其合规情况。

---

## 8. 福岛昆虫认知测试

**原文标题**: Fukushima Insects Tested for Cognition

**原文链接**: [https://news.cnrs.fr/articles/fukushima-insects-tested-for-cognition](https://news.cnrs.fr/articles/fukushima-insects-tested-for-cognition)

科学家正在研究福岛灾难的放射性对授粉昆虫，特别是蜜蜂和巨型大黄蜂认知能力的影响。研究人员奥利维尔·阿尔芒和马修·利奥罗正在合作，以了解电离辐射如何影响这些昆虫的学习和记忆。

利奥罗的团队开发了一种自动化系统，包括一个带有彩色LED灯的Y形迷宫，用于测试蜜蜂的认知能力。蜜蜂学会将特定颜色与糖水奖励联系起来。该系统使用二维码单独追踪每只蜜蜂，并实时分析它们的学习过程。对于体型过大无法使用自动化迷宫的巨型大黄蜂，则进行手动测试。

该研究正在福岛周围的污染区域进行，该区域因铯-137土壤污染梯度而被选中。该团队与福岛大学的环境放射性研究所合作，以获得访问权限和专业知识。

初步结果表明，在污染区域昆虫的认知能力有所下降。虽然尚未明确建立与放射性污染的直接因果关系，但研究人员认为这可能是一个因素，因为在无人居住的区域内没有其他常见的污染物（如农药）。这项研究旨在了解辐射暴露对授粉媒介和生态系统更广泛的生态影响。

---

## 9. CorentinJ：实时语音克隆 (2021)

**原文标题**: CorentinJ: Real-Time Voice Cloning (2021)

**原文链接**: [https://github.com/CorentinJ/Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning)

CorentinJ的仓库提供了一个基于迁移学习的实时语音克隆实现，该实现将说话人验证迁移到多说话人文本到语音合成（SV2TTS）。这个项目源于作者的硕士论文，允许用户使用三阶段深度学习框架实时克隆语音，该框架从短音频样本中创建数字语音表示，然后使用该表示从任何给定的文本生成语音。

该项目实现了几个关键论文，包括SV2TTS、WaveRNN (声码器)、Tacotron (合成器) 和GE2E (编码器)。作者承认，更新、通常是付费的SaaS解决方案提供更卓越的音频质量，但该仓库提供了一个开源替代方案。对于寻求最先进的开源解决方案的用户，建议使用Chatterbox和Paperswithcode。

该仓库支持Windows和Linux，推荐使用Python 3.7和GPU以获得最佳性能。设置包括安装ffmpeg、PyTorch以及`requirements.txt`中列出的其他依赖项。预训练模型会自动下载，但如果需要，也可以手动下载。可以使用`python demo_cli.py`测试配置。用户可以选择下载LibriSpeech等数据集进行实验，或者使用他们自己的音频数据。工具箱通过`python demo_toolbox.py`启动，可以选择指定数据集根目录。

---

## 10. 网站就是一个SVG (2007)

**原文标题**: Website Is Just an SVG (2007)

**原文链接**: [https://svg.nicubunu.ro/](https://svg.nicubunu.ro/)

2007年，Nicu在一个名为“网站就是一个SVG”的项目中，探索了使用SVG（可缩放矢量图形）作为构建网站的唯一技术的可行性。其核心动机是测试谷歌对SVG文件的索引能力，特别是全文索引和链接跟踪。Nicu想确定谷歌是否能够识别和索引SVG内的文本内容，而不是将文件视为一个简单的图像。至关重要的是，该实验旨在确定谷歌是否会抓取并索引嵌入在SVG文件中的链接到其他链接资源的链接。

其根本目标是评估使用矢量图形编辑器Inkscape来创作整个网站的有效性。Nicu承认了不当使用SVG可能带来的缺点，可能会导致文件臃肿和不良的用户体验。他还强调SVG是万维网联盟 (W3C) 的标准。

测试网站使用了高级SVG功能，例如高斯模糊，并指出较旧的浏览器可能无法完全支持这些功能。他建议用户使用Gecko 1.9驱动的浏览器（如Firefox 3.0或更高版本）获得最佳体验。文章还包含一段特定的文本字符串("lmtbk4mh")，旨在被搜索引擎发现，以此作为索引能力的实际测试。最终，该项目是对仅仅依靠SVG进行网站创建的实用性和有效性的调查，重点关注搜索引擎优化方面。

---

## 11. 以读忘忧

**原文标题**: Read to Forget

**原文链接**: [https://mo42.bearblog.dev/read-to-forget/](https://mo42.bearblog.dev/read-to-forget/)

以读致忘

---

## 12. Geedge 与 MESA 泄露：分析防火长城最大规模文件泄露事件

**原文标题**: Geedge and MESA leak: Analyzing the great firewall’s largest document leak

**原文链接**: [https://gfw.report/blog/geedge_and_mesa_leak/en/](https://gfw.report/blog/geedge_and_mesa_leak/en/)

文章《Geedge和MESA泄露：分析中国防火墙最大规模的文件泄露》详细描述了Geedge网络公司和MESA实验室超过500GB内部文件的巨大泄露事件，这两家机构是中国防火墙（GFW）的关键技术贡献者。此次泄露发生在2025年9月11日，包括源代码、工作日志和内部通信，揭示了GFW的研究、开发和运营细节。

Geedge网络公司以方滨兴为首席科学家，为中国各地区提供服务，并将审查/监控技术出口到“一带一路”倡议下的国家。MESA实验室隶属于中国科学院信息工程研究所（IIE, CAS）。 文章追溯了MESA的起源和发展，突出了它与方滨兴的联系及其在GFW开发中的作用。

文章提供了泄露文件的下载链接，并提醒读者注意数据的敏感性和潜在风险，建议在隔离环境中进行分析。虽然非源代码文件已被分析，但源代码仍在调查中。GFW报告承诺在GFW报告网站和Net4People上提供持续的分析和更新。

---

## 13. SpikingBrain 7B – 比经典LLM更高效

**原文标题**: SpikingBrain 7B – More efficient than classic LLMs

**原文链接**: [https://github.com/BICLab/SpikingBrain-7B](https://github.com/BICLab/SpikingBrain-7B)

SpikingBrain 7B 是一款受大脑机制启发的新型大型语言模型，与传统 LLM 相比，效率更高。它集成了混合高效注意力机制、MoE 模块和脉冲编码，并由通用转换管道支持，与开源模型生态系统兼容。这使其能够以明显更少的数据（少于 2%）进行持续预训练，同时保持与主流模型相当的性能。

该项目包括 SpikingBrain-7B 的完整实现和权重，包括 HuggingFace、vLLM 和量化版本，以便灵活部署。一个关键组件是 vLLM-HyMeta，它是 vLLM 推理框架的插件，可在 NVIDIA GPU 上实现高效推理。这提供了一种模块化的方式来集成硬件后端，解耦代码库并加速新功能的集成。

SpikingBrain 利用伪脉冲进行量化推理，将激活近似为类似脉冲的信号，以降低推理成本并探索脉冲神经网络 (SNN) 的潜力。虽然目前的实现侧重于张量级别的近似，但该项目为未来在神经形态硬件上的真实脉冲实现奠定了基础。

性能评估表明，与其他模型相比，SpikingBrain 具有具有竞争力的困惑度分数，尤其是考虑到 SpikingBrain 有限的训练数据需求。该项目在 ModelScope 上提供预训练、聊天和量化模型权重。包含用于使用 Hugging Face 和 vLLM 运行模型的示例脚本。开发者强调，SpikingBrain 的进步为下一代神经形态芯片的设计提供了宝贵的见解，并鼓励引用该工作以表彰其价值。

---

## 14. 一个“裸露”黑洞，挑战早期宇宙理论

**原文标题**: A single, 'naked' black hole confounds theories of the young cosmos

**原文链接**: [https://www.quantamagazine.org/a-single-naked-black-hole-rewrites-the-history-of-the-universe-20250912/](https://www.quantamagazine.org/a-single-naked-black-hole-rewrites-the-history-of-the-universe-20250912/)

詹姆斯·韦伯太空望远镜（JWST）在早期宇宙中发现了一个“裸露”黑洞QSO1，挑战了现有的星系形成理论。 这个黑洞质量高达5000万个太阳，周围没有星系，这与之前认为的黑洞在星系形成后形成的观点不同。它的发现表明，黑洞可能独立形成，甚至早于星系。

天文学家利用引力透镜效应发现了QSO1，引力透镜放大了它的三个反射。进一步研究证实了它的质量，并揭示它主要由氢组成，这表明它是在大规模恒星形成和重元素产生之前形成的。

QSO1的存在支持了关于超大质量黑洞形成的其他理论。一种可能性是，这些黑洞是“原始的”，起源于大爆炸中的密度波动。其他理论包括致密气体云的直接坍缩，或早期星系的快速形成和消失，留下了一个巨大的黑洞。

QSO1是JWST发现的众多“小红点”之一，表明早期宇宙混乱不堪，并给天体物理学家理解宇宙最初十亿年的历史带来了新的挑战。这一发现有必要重新评估现有的星系和黑洞形成模型，并探索黑洞在早期宇宙结构中发挥根本作用的可能性。

---

## 15. 翻新周末：硅谷图形 Indigo² Impact 10000

**原文标题**: Refurb Weekend: Silicon Graphics Indigo² Impact 10000

**原文链接**: [http://oldvcr.blogspot.com/2025/09/refurb-weekend-silicon-graphics-indigo.html](http://oldvcr.blogspot.com/2025/09/refurb-weekend-silicon-graphics-indigo.html)

无法访问文章链接。

---

## 16. MIT-MC CP/M 存档文件，1979-1984

**原文标题**: MIT-MC CP/M archive files, 1979-1984

**原文链接**: [https://github.com/MITDDC/cpmarchive-1979-1984](https://github.com/MITDDC/cpmarchive-1979-1984)

此仓库包含1979-1984年的CP/M操作系统代码、软件和文件，最初托管于麻省理工学院的MIT-MC计算机，并通过ARPANET访问。该合集由Frank J. Wancho和Keith Petersen整理，是一个免费/共享软件档案，在Macsyma联盟解散后转移到了SIMTEL20。

这些文件是麻省理工学院图书馆的Tapes of Tech Square (ToTS) 系列的一部分。“cpm”目录包含使用`itstar`程序从24个ToTS磁带镜像中提取的文件，文件名已改编为Unix约定。原始ITS文件名格式（例如，FJW; LMODEM 258）为了可用性已被更改。“cpm”目录中的子文件夹对应于`tapeimagelist.txt`中列出的磁带名称。

使用`itsarc`程序将提取集合中的221个ITS存档文件进一步提取到同名目录中。提取期间的文件修改，例如将“/”替换为“{”以及将空格替换为“~”，导致了一些时间戳不准确。

该仓库还包括：

*   `codemeta.json`: 关于CP/M存档文件的元数据。
*   `README.md`: 仓库内容的详细描述。
*   `tree.txt`: 列出`cpm`目录中文件的文件树，带有原始时间戳。
*   `tapeimagelist.txt`: 文件来源的磁带镜像列表。
*   `ITSarchivefilelist.txt`: 仓库中ITS存档文件的列表。

提供了首选的引用格式，并包含了有关版权和许可的信息，将查询发送至permissions-lib@mit.edu。感谢Lars Brinkhoff对文件识别的帮助。

---

## 17. 展示HN：一个能根据你的搜索输入生成产品的商店

**原文标题**: Show HN: A store that generates products from anything you type in search

**原文链接**: [https://anycrap.shop/](https://anycrap.shop/)

无法访问文章链接。

---

## 18. 仅两像素高的字体：Two Slice

**原文标题**: Two Slice, a font that's only 2px tall

**原文链接**: [https://joefatula.com/twoslice.html](https://joefatula.com/twoslice.html)

Two Slice 是一款独特的字体，设计得非常小巧，高度仅为 2 像素。尽管尺寸微型，但该字体出人意料地具有可读性，尤其是在较小的显示设置下。

该字体在大小写字母之间具有明显的差异，为用户提供了可读性偏好的选择。除了字母，Two Slice 还包含一组数字（虽然简化了）和一些标点符号。

创作者承认该字体的非常规性，并开玩笑地指出，读者可能会发现它具有可读性，即使他们不愿意。

Two Slice 在 Creative Commons BY-SA 许可下提供下载，允许商业和非商业用途，但需注明创作者的出处。

---

## 19. 双子座 (2023)

**原文标题**: Gemini (2023)

**原文链接**: [https://geminiquickst.art/](https://geminiquickst.art/)

本文档是 Gemini 入门指南，Gemini 是一个比万维网更简单、更注重隐私的替代方案。它解释了 Gemini 是什么，强调其简洁性、对人类规模开发的关注、无干扰体验以及隐私保护。

本指南提供了在各种操作系统（Windows、macOS、iOS、Android、Linux/Unix）上安装 Gemini 客户端（类似于 Web 浏览器）的入门说明。它为每个平台推荐了特定的客户端，并提供了替代方案。

然后，它引导用户找到本文档在 Geminispace 中的地址，以便在 Gemini 客户端中完成教程。它讨论了如何在 Gemini 上查找内容，包括 gemlog（博客）、精选目录和 Geminispace.info 搜索引擎。它强调订阅和跨站点链接是发现新内容的关键方式。

最后，它解释了如何在 Gemini 上发布和分享内容，承认这目前比在 Web 上更复杂。它列出了提供用于发布 Web 应用程序的 Gemini 站点（如 The Midnight Pub 和 Gemlog.Blue）以及具有公共帐户注册的站点，用于共享托管，类似于早期的 Web 托管。它提到 pubnix（公共 Unix 服务器）作为另一种选择。它简要地提到了自托管选项，但指出其中涉及的技术挑战。

本指南最后鼓励大家探索 Gemini，强调社区和分享。它还提供了联系邮箱，以便获得帮助和建议。

---

## 20. 个人电脑从未真正成为“IBM人”。

**原文标题**: The PC was never a true 'IBMer'

**原文链接**: [https://thechipletter.substack.com/p/the-pc-was-never-a-true-ibmer](https://thechipletter.substack.com/p/the-pc-was-never-a-true-ibmer)

好的，我读了The Chip Letter上发表的文章《PC从来都不是真正的“IBM产品”》。以下是摘要：

文章认为，IBM PC虽然无疑是IBM的产品，但它代表着与该公司传统的垂直整合模式和企业文化的重大背离。 IBM历来以其专有硬件、软件以及对其生态系统的严格控制而闻名，但为了加速其进入市场和普及，它有意为PC采用了开放式架构。

要点包括：

*   **开放式架构：** IBM选择使用英特尔（处理器）和微软（操作系统）的现成组件，而不是自行开发所有东西。这是一个根本性的转变。
*   **第三方生态系统：** 这种开放式架构允许其他公司创建兼容的硬件和软件，从而围绕PC培育了一个庞大且快速增长的生态系统。这种快速扩张正是IBM希望看到的。
*   **失去控制：** 虽然有利于市场份额，但开放式方法意味着IBM失去了对关键组件和PC市场整体方向的控制。竞争对手迅速出现，生产克隆产品并压低IBM的价格。
*   **文化转变：** PC项目的成功与IBM既定的保密、垂直整合和控制文化背道而驰。PC开发的“臭鼬工厂”性质进一步强调了这种差异。
*   **最终是必要的权衡：** 文章表明，PC的成功取决于IBM是否愿意接受这种非传统的方法。虽然它最终导致了IBM在PC市场中地位的下降，但这是建立PC作为主导计算平台所必须付出的代价。如果没有开放式架构，其他平台可能会崛起并占据主导地位。

本质上，文章认为，IBM PC虽然被贴上了IBM产品的标签，但却是IBM传统价值观妥协的产物，其设计有意创建一个庞大的生态系统，而这种设计虽然带来了短期的成功，但最终导致了IBM失去控制。

---

## 21. Pass: Unix密码管理器

**原文标题**: Pass: Unix Password Manager

**原文链接**: [https://www.passwordstore.org/](https://www.passwordstore.org/)

Pass是一个遵循Unix哲学的简单命令行密码管理器。它将密码存储在以网站或资源名称镜像的目录结构（~/.password-store）中，并使用GPG加密文件。用户可以使用标准Unix工具以及`pass`命令来管理这些文件。

主要功能包括轻松添加、编辑、生成（使用/dev/urandom）和检索密码，具有临时剪贴板存储和可选的Git版本控制用于同步。`pass`命令文档完善，并提供bash、zsh和fish补全。

设置包括使用GPG密钥初始化密码存储库（`pass init`），以及可选地将其初始化为Git仓库（`pass git init`）。该工具可通过各种Linux发行版（apt、yum、zypper、pacman）、macOS（brew）和FreeBSD（pkg）上的软件包管理器获得。

Pass在数据组织方面具有灵活性，允许用户存储其他信息，如URL、用户名和安全问题，以及密码，可以存储在多行文件中，也可以存储在同一文件夹中的单独文件中。

该工具支持扩展程序，以增加功能，如Tomb集成、密码更新、导入工具、OTP支持，并通过各种平台（Android、iOS、Windows、浏览器等）上可用的兼容客户端和GUI与其他应用程序集成。存在许多用于从其他密码管理器迁移密码的脚本。

---

## 22. 动态鸟类迁徙地图

**原文标题**: Dynamic Bird Migration Map

**原文链接**: [https://explorer.audubon.org/explore/species?sidebar=expand](https://explorer.audubon.org/explore/species?sidebar=expand)

“动态鸟类迁徙地图”是一个互动的在线工具，专注于探索和理解鸟类迁徙。它的核心功能是允许用户探索与鸟类物种的分类群、地点、保护状况和保护挑战相关的数据。

主要功能包括：

*   **分类探索：** 用户可以按字母顺序或分类群浏览鸟类物种。
*   **地理数据：** 地图允许用户选择地点、搜索特定地点或使用其当前位置来查看相关的鸟类物种。
*   **保护重点：** 该平台突出显示了不同鸟类物种面临的保护统计数据和挑战。
*   **物种追踪：** “最近浏览过的鸟类物种”功能可帮助用户跟踪他们之前的搜索。
*   **参与：** 该平台还提供了“采取行动”的途径来支持鸟类保护。

该网站提供了关于鸟类迁徙探索者、其支持者以及美国国家奥杜邦协会的联系信息。它还包括指向您附近的奥杜邦、服务条款和隐私政策的链接。

本质上，该地图是一个学习鸟类迁徙模式、保护问题以及参与保护鸟类物种机会的资源。

---

## 23. 全球排放量创新高，但欧盟引领趋势逆转。

**原文标题**: World emissions hit record high, but the EU leads trend reversal

**原文链接**: [https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/world-emissions-hit-record-high-eu-leads-trend-reversal-2025-09-09_en](https://joint-research-centre.ec.europa.eu/jrc-news-and-updates/world-emissions-hit-record-high-eu-leads-trend-reversal-2025-09-09_en)

欧盟委员会EDGAR数据库的最新报告显示，2024年全球温室气体（GHG）排放量达到创纪录的532亿吨二氧化碳当量，比上一年增加1.3%。但欧盟呈现趋势逆转，同期温室气体排放量减少1.8%。

报告强调，自1990年以来，人为活动导致温室气体排放量每年增加约1.5%，使得2024年的排放量比1990年高出65%。中国、美国、印度、欧盟、俄罗斯、印度尼西亚、巴西和日本占全球温室气体排放量的66.2%。只有欧盟和日本的排放量同比下降，而印度则在绝对值上增幅最大。

尽管总体排放量有所增加，但大多数主要排放国的排放强度相对于GDP均有所下降。欧盟、美国、俄罗斯和日本实现了排放与经济增长的绝对脱钩。中国和印度在GDP快速增长的同时，排放量也在上升。

电力行业在2024年的绝对排放增幅最大，而燃料开采行业的相对增幅最大。在全球范围内，土地利用、土地利用变化和林业（LULUCF）部门作为一个净碳汇，在不包括野火的情况下，消除了13亿吨二氧化碳当量，但森林砍伐和野火贡献了大量排放。报告强调，欧盟致力于在2050年前实现气候中和。

---

## 24. 苏格拉底式日记法：一种简单有效的日记方法

**原文标题**: The Socratic Journal Method: A Simple Journaling Method That Works

**原文链接**: [https://mindthenerd.com/the-socratic-journal-method-a-simple-journaling-method-that-actually-works/](https://mindthenerd.com/the-socratic-journal-method-a-simple-journaling-method-that-actually-works/)

苏格拉底式日记法：一种简单有效的自我反思方法，灵感源于苏格拉底对自我审视的强调。其核心在于将日记页面视为一场访谈，向自己提出问题并诚实作答。

文章强调了日记的书写对心理的益处，引用研究表明其可以减轻压力、改善情绪、并提升元认知能力。文章也承认维持日记习惯的常见困难，并提出苏格拉底方法作为解决方案，因为它提供了结构，并消除了面对空白页面的压力。

文章探讨了不同的日记工具（纸笔、数字打字、录音/视频），强调坚持是关键，最好的工具就是你会使用的工具。文章详细介绍了如何实施苏格拉底方法，重点在于提出有意义的问题并自由回答，不带自我评判。该方法强调个人发现、识别思维模式，并根据需要调整日记提示。

文章警告不要将日记变成自我批评的练习，强调保持支持性和好奇语气的必要性。该方法被描述为一种通过持续、专注的反思来获得清晰、追踪进度并培养自我意识的方式，并以一个简单的初学者指南结束，以便立即开始。

---

## 25. 用机器人而非按钮设计用户界面

**原文标题**: Designing user interfaces with bots not buttons

**原文链接**: [https://interconnected.org/home/2022/05/09/npcs](https://interconnected.org/home/2022/05/09/npcs)

本文探讨了用“机器人”或非玩家角色 (NPC) 取代按钮和对话框等传统用户界面元素的概念，尤其是在 VR 和元宇宙的背景下。作者引用了虚拟活动平台 Skittish 和笔记应用程序 Subconscious 作为这种趋势的例子。 Skittish 使用动物 NPC 在其虚拟世界中引导用户并提供信息。 Subconscious 使用 “Geists”（AI 机器人）通过查找连接和生成提示来协助笔记。

作者认为，这种向机器人的转变是回归到用户界面更具“戏剧性”的视角，借鉴了 Brenda Laurel 的《计算机即剧场》理论，该理论认为计算机屏幕是人类和软件代理互动的舞台。 Laurel 的框架强调“共同基础”——用户和机器之间的共同理解。与对话框不同，NPC 感觉已融入虚拟世界，并有助于建立这种共同基础。

作者预测，VR 和元宇宙的兴起将加速在用户界面中采用机器人和 NPC，不仅在 VR 环境中，而且在台式机和手机上也是如此。这些机器人将提供一种更具沉浸感和直观的方式与软件交互，摆脱僵化的“桌面隐喻”，转向更具协作性和吸引力的体验。最后，作者征集其他实施这些低保真机器人或 NPC 的软件示例。

---

## 26. 人工智能会成为未来许多产业财富的基础，还是最终的净亏损？

**原文标题**: Will AI be the basis of many future industrial fortunes, or a net loser?

**原文链接**: [https://joincolossus.com/article/ai-will-not-make-you-rich/](https://joincolossus.com/article/ai-will-not-make-you-rich/)

本文认为，虽然生成式人工智能是一项革命性技术，但它可能不会像个人电脑等以往的技术浪潮那样为投资者和企业家创造广泛的财富。作者将此比作集装箱运输，一项变革性的创新，但为大多数参与者带来的财务收益甚微。

核心问题是，人工智能会像个人电脑革命那样创造无数财富，还是像集装箱运输那样主要使终端用户受益，并将权力集中在少数主导企业手中？作者倾向于后者，认为人工智能模型构建者和应用公司可能会展开激烈竞争，导致形成寡头垄断，主要受益者是客户，而非投资者。

文章强调了技术浪潮中的时机和阶段（爆发、狂热、协同、成熟）的重要性。它认为，人工智能正被现有的信息通信技术公司所掌控，使得新进入者难以有效竞争，并对专注于早期、高增长机会的传统风险投资模式提出了挑战。作者将个人电脑革命的意外性（需要时间才能获得发展）与人工智能获得的即时和广泛关注进行了对比，表明颠覆性创新的空间较小。

最终，作者建议保持谨慎，认为许多人工智能投资都在错误的地方进行，早期退出策略可能对财务成功至关重要。文章强调了人工智能改变社会的潜力，但质疑其为投资者创造广泛财富的能力，并提请注意技术浪潮的历史背景以及理解决定谁能获得价值的力量的重要性。

---

## 27. 古代巴比伦的修复如何吸引游客重返伊拉克

**原文标题**: How the restoration of ancient Babylon is drawing tourists back to Iraq

**原文链接**: [https://www.theartnewspaper.com/2025/09/12/how-the-restoration-of-ancient-babylon-is-helping-to-draw-tourists-back-to-iraq](https://www.theartnewspaper.com/2025/09/12/how-the-restoration-of-ancient-babylon-is-helping-to-draw-tourists-back-to-iraq)

伊拉克古巴比伦城的复兴：修复工程与文化旅游的兴起。

---

## 28. AI抓取数据混战即将结束

**原文标题**: The AI-Scraping Free-for-All Is Coming to an End

**原文链接**: [https://nymag.com/intelligencer/article/ai-scraping-free-for-all-by-openai-google-meta-ending.html](https://nymag.com/intelligencer/article/ai-scraping-free-for-all-by-openai-google-meta-ending.html)

人工智能数据抓取的演变：从无序实验到版权争议

---

## 29. AMD 的 RDNA4 GPU 架构

**原文标题**: AMD’s RDNA4 GPU architecture

**原文链接**: [https://chipsandcheese.com/p/amds-rdna4-gpu-architecture-at-hot](https://chipsandcheese.com/p/amds-rdna4-gpu-architecture-at-hot)

本文概述了AMD的RDNA4 GPU架构，重点介绍了其在媒体引擎、显示引擎、计算和内存子系统方面的改进。媒体引擎拥有更快的解码速度以及对H.264、H.265和AV1更好的编码质量，尤其是在低延迟流媒体场景中。显示引擎引入了“Radeon图像锐化”，并通过利用FreeSync显示器上的可变刷新率来降低内存带宽需求，从而优化了多显示器空闲功耗。

计算方面的改进包括扩展标量浮点指令卸载以节省功耗和降低延迟，以及用于更好线程同步的分裂屏障。内存子系统具有更大的L2缓存（8MB），有利于光线追踪工作负载，并改进了透明压缩以降低带宽需求。值得注意的是，缺少中级L1缓存，这可能是由于前几代产品中的命中率较低。

RDNA4还集成了RAS（可靠性、可用性、可维护性）特性，包括用于错误检测和纠正的奇偶校验和ECC，以及诸如私有总线和受保护的寄存器访问机制等安全特性，目标是DRM。本文还涉及SoC特性和Infinity Fabric。总而言之，RDNA4旨在提高光栅化、计算、光线追踪和机器学习方面的效率，从而增强游戏和通用GPU性能。

---

## 30. macOS Tahoe 通过了 Unix 03 认证 [pdf]

**原文标题**: macOS Tahoe is certified Unix 03 [pdf]

**原文链接**: [https://www.opengroup.org/openbrand/certificates/1223p.pdf](https://www.opengroup.org/openbrand/certificates/1223p.pdf)

提供的文档似乎是一个损坏的PDF文件，内容主要由二进制数据组成。无法从中提取任何有意义的文本或关于macOS Tahoe或Unix 03认证的信息。“标题”字段表明预期主题是关于macOS Tahoe符合Unix 03标准的认证，但损坏的内容阻止了进一步的理解或确认。

---

## 31. 现代排序算法的惊人有效性

**原文标题**: The unreasonable effectiveness of modern sort algorithms

**原文链接**: [https://github.com/Voultapher/sort-research-rs/blob/main/writeup/unreasonable/text.md](https://github.com/Voultapher/sort-research-rs/blob/main/writeup/unreasonable/text.md)

GitHub仓库“Voultapher/sort-research-rs”探索了现代排序算法令人惊讶的高性能，其在实际场景中往往超越理论预期。“现代排序算法的非理性有效性”这一标题暗示了这样一种现象：这些算法在实际应用中的表现比其理论最坏情况复杂度所暗示的要好得多。

该仓库可能包含用Rust编写的研究和实现（如"sort-research-rs"所示），重点关注各种排序算法，可能包括优化和基准测试。它旨在理解导致这种“非理性有效性”的因素。这些因素可能包括：

*   **硬件考量：** 算法被设计为利用CPU缓存、分支预测和其他架构特性，从而显著提高性能。
*   **数据特征：** 真实世界的数据通常不是均匀分布的。自适应算法利用预排序或近乎排序的数据等模式来加快排序速度。
*   **混合方法：** 现代排序实现通常结合不同的算法，根据数据大小和特征利用每种算法的优势。例如，对大型分区使用快速排序，对较小分区使用插入排序。
*   **优化后的实现：** 对代码细节的细致关注，例如最小化内存访问和使用向量化指令，可以显著提高性能。

本质上，该仓库调查了现代排序算法为何通过巧妙的设计、硬件感知和数据适应的结合，实现了与它们的理论最坏情况界限相比，性能似乎“非理性地”良好的原因。

---

## 32. 线性变换反向传播的一个技巧

**原文标题**: A Trick for Backpropagation of Linear Transformations

**原文链接**: [https://tripplyons.com/blog/backprop-trick](https://tripplyons.com/blog/backprop-trick)

本文介绍了一种通过爱因斯坦求和 (einsum) 表示的线性变换进行反向传播的简单技巧。Einsum 可以表达诸如矩阵乘法、点积和哈达玛积等运算。

关键思想是在前向传递中，将涉及的张量与损失相对于输出张量的梯度在反向传递中进行交换，同时保持每个张量的相同索引符号（字母）。

例如，如果前向传递计算 C = einsum('ij,jk->ik', A, B)，则反向传递计算 dL/dA（损失 L 相对于 A 的梯度）可以执行为 dL_dA = einsum('ik,jk->ij', dL_dC, B)，其中 dL_dC 是损失相对于 C 的梯度。

本文通过矩阵乘法示例演示了此技巧，并解释了如何使用索引符号验证结果梯度的形状。 它还展示了如何通过重新排列索引来帮助将反向传播 einsum 解释为更熟悉的操作，例如矩阵转置。

最后，本文使用 JAX 的自动微分功能来验证使用 einsum 反向传播技巧计算的值与自动计算的梯度是否匹配，从而确认了该方法的有效性。 作者总结说，这种交换技巧简化了通过 einsum 的反向传播。

---

## 33. 486Tang – 信用卡大小的FPGA开发板上的486

**原文标题**: 486Tang – 486 on a credit-card-sized FPGA board

**原文链接**: [https://nand2mario.github.io/posts/2025/486tang_486_on_a_credit_card_size_fpga_board/](https://nand2mario.github.io/posts/2025/486tang_486_on_a_credit_card_size_fpga_board/)

486Tang是将ao486 MiSTer PC核心移植到Sipeed Tang Console 138K FPGA上的项目，标志着ao486首次成功运行在非Altera FPGA上。由于Tang的硬件限制相比MiSTer更大，该项目面临挑战，需要进行调整，例如使用SDRAM作为主内存而非DDR3，并由于缺乏高速MCU-FPGA接口而实现SD卡支持的IDE。为此创建了一个启动加载模块，用于从SD卡加载BIOS、VGA BIOS、CMOS设置和IDE IDENTIFY数据。

Verilator在整个系统仿真中发挥了作用，这对于调试复杂的486 PC架构至关重要，从而辅助了系统启动。工具挂钩、调试信息和子系统跟踪简化了调试过程。

性能优化集中在通过解决长组合路径来提高时钟速度。 这些优化包括减少复位树扇出、通过消除解码器中的依赖性来优化指令提取，以及将TLB转换为4路组相联缓存。 这些改进带来了 35% 的性能提升，达到了与 486SX-20 相似的性能。

作者反思了时钟速度在系统性能中的重要性，并将x86架构的复杂性与ARM的简单性进行了对比，突出了兼容性和架构优雅性之间的权衡。

---

## 34. 心肌梗塞可能是一种传染病

**原文标题**: Myocardial infarction may be an infectious disease

**原文链接**: [https://www.tuni.fi/en/news/myocardial-infarction-may-be-infectious-disease](https://www.tuni.fi/en/news/myocardial-infarction-may-be-infectious-disease)

芬兰和英国研究人员的一项突破性研究表明，心肌梗塞（心脏病发作）可能由感染引发。该研究挑战了对心脏病发作发展的传统理解，认为冠状动脉内富含胆固醇的斑块中无症状的细菌生物膜起着关键作用。这些生物膜由休眠细菌组成，免受免疫系统和抗生素的影响，并可能被病毒感染或其他触发因素激活。这种激活会导致细菌增殖，并随之引发炎症反应。

炎症会导致斑块的纤维帽破裂，从而导致血栓形成，最终导致心脏病发作。研究人员在这些斑块中发现了来自口腔细菌的遗传物质，并开发出一种抗体，揭示了动脉组织中的生物膜结构。他们观察到，从生物膜中释放的细菌会引发炎症，从而在心肌梗塞期间导致富含胆固醇的斑块破裂。

这一发现为治疗、诊断和预防心脏病开辟了新的途径，包括开发疫苗的可能性。这项由多个机构合作开展、并由多个组织资助的研究分析了死于心脏性猝死个体的组织样本以及正在接受动脉粥样硬化手术的患者的组织样本。该研究结果发表在《美国心脏协会杂志》上。

---

## 35. 反对社交媒体的理由比你想象的更充分

**原文标题**: The case against social media is stronger than you think

**原文链接**: [https://arachnemag.substack.com/p/the-case-against-social-media-is](https://arachnemag.substack.com/p/the-case-against-social-media-is)

无法访问文章链接。

---

## 36. 安息吧，pthread_cancel

**原文标题**: RIP pthread_cancel

**原文链接**: [https://eissing.org/icing/posts/rip_pthread_cancel/](https://eissing.org/icing/posts/rip_pthread_cancel/)

本文探讨了作者在 curl 库（特别是 8.16.0 版本）中添加然后移除 `pthread_cancel` 功能以改进 DNS 解析的经验。最初的目标是通过将 `getaddrinfo()` 调用卸载到单独的线程，来防止 libcurl 在可能长时间的 `getaddrinfo()` 调用期间阻塞。 引入 `pthread_cancel` 是为了在需要时终止该线程，避免无限等待或不受控制的线程累积。

然而，发布后，报告了一个内存泄漏问题（#18532）。调查显示，glibc 的 `getaddrinfo()` 实现读取 `/etc/gai.conf` 进行地址排序，这涉及文件操作（例如 `fopen()`、`open()`），这些操作是取消点。 如果线程在此文件访问期间被取消，则为已解析地址分配的内存会泄漏。 作者指出，glibc 似乎没有设计成防止在这种情况下发生泄漏。

由于存在重复内存泄漏的可能性，作者决定从 libcurl 中移除 `pthread_cancel`。 现在，该库将容忍 `getaddrinfo()` 期间的阻塞。 文章建议，需要非阻塞 DNS 解析的应用程序应考虑使用 c-ares，但它承认 c-ares 可能无法提供 glibc DNS 解析的全部功能。 作者总结说，DNS 解析仍然是一个具有挑战性的领域。

---

## 37. 我对Gleam的第一印象

**原文标题**: My first impressions of Gleam

**原文链接**: [https://mtlynch.io/notes/gleam-first-impressions/](https://mtlynch.io/notes/gleam-first-impressions/)

本文记录了一位程序员通过构建一个简单的AIM日志解析器来学习Gleam的初体验。作者熟悉Go和Python等语言，分享了他们在适应函数式编程概念时的最初障碍和发现。

该项目涉及解析纯文本AIM日志以提取聊天消息。早期的挑战包括弄清楚如何处理命令行参数（使用`argv`库）以及理解`gleam build`的用途（它产生BEAM字节码而不是直接可执行文件）。

本文的核心重点是实现解析逻辑。作者最初对缺乏熟悉的工具（如`if`语句、循环和列表索引）感到困难。他们逐渐学会利用模式匹配和`list.map`和`string.split`等函数来处理日志数据。文章详细介绍了编写测试、实现代码和重构的迭代过程。探索的关键概念包括用于解析行的模式匹配、处理`Result`类型以及使用`list.filter`删除空字符串。

作者还使用`string.split_once`和用于元组的模式匹配来重构字符串拆分逻辑，突出了函数式编程方法的优雅性。文章最后成功实现了一个简单的AIM日志解析器，展示了作者在Gleam方面的初步尝试，并为其他初学者提供了见解。

---

## 38. 猫咪水族馆

**原文标题**: Cat Aquariums

**原文链接**: [https://cataquariums.com/](https://cataquariums.com/)

本文推介“猫咪水族箱”，这是一种专为猫咪设计的安全互动鱼缸。这些水族箱为猫科动物提供视觉刺激和引人入胜的体验，旨在提升它们的心理健康并提供娱乐。该水族箱融合了优雅和功能性，采用高品质超白玻璃制造，确保安全性和最佳观赏效果。提供内部隧道、前入口和底部入口等不同设计，售价399.98美元（原价1300.00美元）。

文章强调安全性，指出其采用手工抛光边缘、无毒材料和严格测试。除了娱乐之外，猫咪水族箱还被认为是一种减少猫咪压力、无聊和破坏性行为的工具。来自鱼的视觉刺激可以促进平静，激发好奇心，并改善睡眠质量。它们采用优质材料制造，经久耐用且美观，使其成为任何家庭的时尚补充，同时丰富猫咪的生活。本质上，猫咪水族箱被描绘成一种为猫咪提供娱乐和精神刺激的方式，从而促进它们的整体健康。

---

## 39. 四年婚礼闯入者之谜已解

**原文标题**: Four-year wedding crasher mystery solved

**原文链接**: [https://www.theguardian.com/uk-news/2025/sep/12/wedding-crasher-mystery-solved-four-years-bride-scotland](https://www.theguardian.com/uk-news/2025/sep/12/wedding-crasher-mystery-solved-four-years-bride-scotland)

婚礼四年后，神秘宾客身份终揭晓。新娘米歇尔和约翰·怀利的婚礼照片中出现一名高个子、略显局促的男子，但无人知晓其身份。脸书寻人未果。

最终，米歇尔求助于苏格兰内容创作者达扎，扩大搜索范围。安德鲁·希尔豪斯主动承认，他误将怀利婚礼的地点当成自己应该参加的另一场婚礼，不小心闯入了婚礼现场。当时他迟到了，便跟着其他宾客进入了普雷斯蒂克卡尔顿酒店，并未意识到自己走错了地方。

在仪式进行到一半时，希尔豪斯意识到自己犯了错，但又觉得离开会引起骚动，便尴尬地坐着参加完了整个仪式。之后，他还被婚礼摄影师拉入了合影。随后，他赶到了正确的婚礼现场，并成为了大家取笑的对象。

米歇尔·怀利对终于知道该男子的身份感到释怀，现在她与希尔豪斯已是脸书好友，甚至见过面。她承认多年来这个谜团一直萦绕在心，她甚至考虑过他可能是个跟踪者。她表达了在经历了这么长时间后，对故事最终结局的难以置信和好笑。

---

## 40. 加入OR逻辑迫使我们面对用户为何偏爱原始SQL。

**原文标题**: Adding OR logic forced us to confront why users preferred raw SQL

**原文链接**: [https://signoz.io/blog/query-builder-v5/](https://signoz.io/blog/query-builder-v5/)

本文详细介绍了查询构建器工具的演变过程，该工具旨在统一日志、追踪和指标的数据查询。最初，基于简单AND逻辑的v3版本无法满足需求，尤其是在需要复杂布尔表达式（包含OR逻辑）的日志查询方面，导致用户不得不求助于原始ClickHouse SQL。

通过大量的支持电话，团队意识到即使是高级工程师也很难发现看似显而易见的功能，这突显了可发现性和直观设计的重要性。这促使v5版本的设计理念发生了根本性转变：优先考虑用户控制，避免过于巧妙的假设。

v5更新不仅仅是添加了OR支持；它成了一次架构大修，影响了所有浏览器、仪表板面板和警报创建流程。关键功能包括：像Google一样工作的全文搜索、具有正确优先级的复杂布尔逻辑、跨源查询可移植性以及即时建议。还实施了重要的用户体验改进，例如使按时间顺序排列变得易于访问。

最终，这个查询构建器非常有效，用户纷纷替换了他们的原始SQL查询，理由是不需要学习SQL语法、自动模式更新、自动完成以及跨数据类型查询可移植性。本文还预览了即将推出的功能，例如子查询和跨源连接，以增强数据关联。核心教训是：没有可发现性，技术上的优雅毫无用处。现在的架构旨在进行增量改进。

---

## 41. 安全C++提案不再继续。

**原文标题**: Safe C++ proposal is not being continued

**原文链接**: [https://sibellavia.lol/posts/2025/09/safe-c-proposal-is-not-being-continued/](https://sibellavia.lol/posts/2025/09/safe-c-proposal-is-not-being-continued/)

旨在为C++添加具有强大内存、类型和线程安全保证的、类似Rust的安全子集的“安全C++”提案已被终止。该提案涉及引入新的语法和安全/不安全上下文，使其成为C++的一个可选扩展，不会破坏现有代码。

其终止的主要原因是C++委员会更倾向于“Profiles”——一种改进安全的更为温和的方法。Profiles定义了C++的约束使用模式，限制现有功能以保证某些安全属性，主要通过编译时检查。与安全C++不同，Profiles不引入新的语言结构，而是限制现有的结构，旨在提供更安全的默认C++体验，而无需强制采用完整的Rust风格模型。

委员会认为，安全C++的雄心勃勃的性质（引入新的语法和上下文）过于沉重，而Profiles提供了一条更务实和更易于采用的道路。社区内对Rust模型的抵制也发挥了一定的作用。文章总结说，虽然安全C++受到了赞赏，但Profiles是改进C++安全性的更现实的方法，代表了现有实践的标准化和统一。尽管它们将比安全C++弱，但总比在安全性方面毫无进展要好。

---

## 42. Lexy: 一个 C++17 的解析器组合子库

**原文标题**: Lexy: A parser combinator library for C++17

**原文链接**: [https://github.com/foonathan/lexy](https://github.com/foonathan/lexy)

Lexy：一个用于C++17及更高版本的仅头文件解析器组合子库，提供了一种DSL，用于创建具有手写代码的灵活性但无需手动操作的解析器。它避免了隐式回溯和前瞻，从而可以精确控制解析过程。Lexy提供了一个“逃生舱口”来集成手写解析器，并包括用于调试的跟踪功能。

主要功能包括：直接将结果存储在用户定义的类型中，完全的constexpr解析，最小的标准库依赖，Unicode支持，用于常见解析任务的内置规则，自动跳过空格，关键字/标识符/运算符解析支持以及自动错误恢复。它还支持解析二进制输入。

Lexy与Boost.Spirit（更冗长，专为更大的语法而设计，零拷贝解析）和PEGTl（使用运算符重载而不是模板继承）等类似库有所不同。它旨在提供控制、性能以及集成到现有代码库中，避免了对外部语法文件的需求。虽然编译时间可能令人担忧，但lexy可以隔离在转换单元中并拆分为子语法。该库提供了全面的文档，其中包含教程和一个交互式playground，网址为lexy.foonathan.net。

---

## 43. Ruby 如何执行 JIT 代码

**原文标题**: How Ruby executes JIT code

**原文链接**: [https://railsatscale.com/2025-09-08-how-ruby-executes-jit-code-the-hidden-mechanics-behind-the-magic/](https://railsatscale.com/2025-09-08-how-ruby-executes-jit-code-the-hidden-mechanics-behind-the-magic/)

本文解释了 Ruby 的 JIT (即时) 编译器，特别是 ZJIT 和 YJIT 的工作原理。它解答了关于 JIT 编译代码的存储位置、Ruby 如何执行它、什么触发编译以及代码有时会还原为解释器的原因等问题。

Ruby 将方法编译成包含 YARV 字节码的指令序列 (ISEQ)。JIT 编译的代码不会替换字节码，而是与字节码一起存储在 ISEQ 中，可通过 `jit_entry` 字段访问。Ruby 在执行 ISEQ 之前会检查此字段；如果为 NULL，则解释执行字节码，否则，执行编译后的本机代码。

方法基于重复使用进行编译。ZJIT 使用两阶段方法：在一定数量的调用后进行性能分析，然后在达到更高的阈值后进行编译。这个“预热”期对于 JIT 有效优化是必要的。

JIT 编译器会做出假设来优化代码。如果这些假设被违反，Ruby 会“反优化”并还原为解释器。这可能是由于类型不匹配（例如，期望整数但收到浮点数）、TracePoint 激活（这需要字节码执行）、重新定义的内核方法或 Ractor 的使用造成的。这些“保护”或“补丁点”确保了正确性。

编译所有方法是低效的，因为存在很少调用的方法，并且需要进行性能分析才能做出明智的优化决策。TracePoint 会降低性能，因为它强制禁用 JIT 编译的代码，还原为解释器以执行字节码。

---

## 44. 重现美国/*时区状况

**原文标题**: Recreating the US/* time zone situation

**原文链接**: [https://rachelbythebay.com/w/2025/09/12/tz/](https://rachelbythebay.com/w/2025/09/12/tz/)

无法访问文章链接。

---

## 45. 我可以给你一些建议吗？

**原文标题**: Can I Give You Some Advice?

**原文链接**: [https://nautil.us/can-i-give-you-some-advice-1237219/](https://nautil.us/can-i-give-you-some-advice-1237219/)

这篇鹦鹉螺杂志的文章，查尔斯·迪格斯撰写的《我能给你一些建议吗？》，探讨了心理学家伊戈尔·格罗斯曼领导的一项研究，该研究揭示了一种普遍存在的决策自力更生倾向。这项研究涉及来自不同文化的3500多名成年人，发现人们更倾向于相信自己的直觉和推理，而不是寻求或听从他人的建议，即使是在那些重视群体和谐的文化中也是如此。

参与者被呈现了假设的困境，从金融投资到社交场景，并被问及他们将如何处理这个决定。结果始终表明，个人更喜欢独自深思熟虑或相信自己的直觉，而不是咨询朋友、家人或专家。

有趣的是，该研究还发现，人们期望别人比自己更依赖建议。我们倾向于认为自己的判断更胜一筹，这意味着其他人更需要指导。

神经生物学家罗伯特·萨波尔斯基认为，这源于我们对自己内部思维过程的了解，而我们无法了解他人的思维过程。这篇文章强调了讽刺之处，即我们最不可能在压力大的时候听取建议，而那时我们可能最需要建议。

尽管有这种倾向，格罗斯曼认为，提供建议仍然有价值，但应谨慎措辞，提供替代视角，同时尊重个人的自主权。最终，这篇文章表明，虽然建议可能有用，但人们通常更喜欢依靠自己的判断。

---

## 46. 为修复情绪代码混乱而买单的软件工程师

**原文标题**: The Software Engineers Paid to Fix Vibe Coded Messes

**原文链接**: [https://www.404media.co/the-software-engineers-paid-to-fix-vibe-coded-messes/](https://www.404media.co/the-software-engineers-paid-to-fix-vibe-coded-messes/)

伊曼纽尔·迈贝格的文章探讨了一种新兴趋势：软件工程师和公司专门修复“氛围代码”软件，这类软件是使用AI编码工具快速构建的，很少关注代码质量。虽然氛围代码承诺快速简便地创建软件，但现实往往是错误百出、效率低下且不安全的应用程序，需要人工干预。

一些个人和公司，如Fiverr上的哈米德·西迪奇和乌拉姆实验室，现在提供清理这些“氛围代码烂摊子”的服务。他们解决诸如UI/UX不一致、代码优化不良、品牌错位和功能繁琐等问题。斯瓦坦特拉·索尼创建了VibeCodeFixers.com，将开发者与需要帮助其氛围代码项目的客户联系起来。

索尼的研究强调了非技术“氛围编码者”面临的常见问题，包括功能冲突以及尝试改进项目时浪费的AI使用费（“信用消耗”）。许多人是产品经理、销售专业人士或小企业主，他们主要使用氛围代码进行原型设计。尽管存在缺陷，索尼认为氛围代码将持续存在，但人类开发者仍将至关重要，以指导和改进AI生成的代码，防止其完全失控。他将开发者视为AI的“缰绳”。

---

## 47. 展示 HN：CLAVIER-36 – 一个生成音乐的编程环境

**原文标题**: Show HN: CLAVIER-36 – A programming environment for generative music

**原文链接**: [https://clavier36.com/p/LtZDdcRP3haTWHErgvdM](https://clavier36.com/p/LtZDdcRP3haTWHErgvdM)

这篇“Show HN”帖子展示了CLAVIER-36，一个专为生成音乐设计的编程环境。虽然帖子非常简短，但暗示了CLAVIER-36允许用户以编程方式创作音乐，很可能是使用代码来定义音乐模式、节奏、和声和旋律。

“Show HN”标签表明创建者正在展示一个个人项目，并邀请Hacker News社区的反馈。在没有更多细节的情况下，很难了解该环境的具体情况。可能相关但未明确说明的关键方面包括：

*   **编程语言:** 用于与CLAVIER-36交互的语言。它可能是一种专门的音乐编程语言，或是一种带有音乐特定库的更通用的语言。
*   **功能:** 功能可能包括生成音符、节奏和和声；操纵这些元素；并将生成的音乐以可播放的格式（例如，MIDI）输出。
*   **目标受众:** 目标用户可能是音乐家、程序员或任何对探索音乐和代码的交叉领域感兴趣的人。
*   **潜在用例:** 这些可能包括创作原创音乐、创建音景、开发算法音乐系统或尝试生成艺术。

本质上，CLAVIER-36被呈现为一种用于以编程方式创作音乐的工具，为音乐探索和创作提供了一种新途径。该帖子的成功可能取决于文档、示例和一个支持性社区的可用性。

---

## 48. Rust 函数背后的规则

**原文标题**: The rules behing Rust functions

**原文链接**: [https://blog.cuongle.dev/p/the-hidden-rules-behind-rust-functions](https://blog.cuongle.dev/p/the-hidden-rules-behind-rust-functions)

本文深入探讨 Rust 的函数和闭包系统，揭开令新手困惑的概念。它解释了函数项和函数指针之间的区别：函数项是零大小类型，支持静态分发和优化，而函数指针使用动态分发以实现灵活性。

文章的核心集中在闭包及其三个 trait：`FnOnce`、`FnMut` 和 `Fn`。这些 trait 决定了闭包如何从其环境中捕获变量：`FnOnce` 移动变量（只能调用一次），`FnMut` 改变它们，而 `Fn` 仅读取它们。编译器会智能地选择侵入性最小的捕获模式。

一个重要的结论是 trait 层次结构：`Fn` 继承自 `FnMut`，而 `FnMut` 继承自 `FnOnce`。这允许在需要 `FnMut` 或 `FnOnce` 的地方使用 `Fn` 闭包。 Rust 内部将闭包转换为带有捕获变量的匿名结构体，并实现相应的闭包 trait。

最后，本文强调了函数指针和闭包之间的集成。非捕获闭包可以强制转换为函数指针，并且函数指针实现了所有三个闭包 trait，从而实现无缝互操作性。 理解这些底层机制使开发人员能够编写更高效和正确的 Rust 代码。

---

## 49. 锁起来的商品正在赶走顾客。

**原文标题**: Locked-up merchandise is driving customers away

**原文链接**: [https://ktla.com/news/nationworld/locked-up-merchandise-is-driving-customers-away/](https://ktla.com/news/nationworld/locked-up-merchandise-is-driving-customers-away/)

无法访问文章链接。

---

## 50. 开源SDR业余无线电收发器原型

**原文标题**: Open Source SDR Ham Transceiver Prototype

**原文链接**: [https://m17project.org/2025/08/18/first-linht-tests/](https://m17project.org/2025/08/18/first-linht-tests/)

本文宣布LinHT（一个开源的软件定义无线电(SDR)业余无线电手持机原型）首次启动成功。该项目旨在将SDR技术引入业余无线电手持机(HT)。perens.com的Bruce Perens认为它是业余无线电领域最重要的硬件项目。

目前的测试装置在420-450MHz (UHF) 频段工作，输出功率约为5dBm。虽然目前缺少射频放大器，但下一个版本将包含GRF5604射频放大器。该设备是开源硬件，PCB设计文件可在网上获取。

通过PCBWay制造和组装5个单元的PCB成本约为490美元，5个单元的SoM（系统模块）成本为469美元。Retevis C62（也以Chierda UV58D的名称销售）被用作捐赠无线电，用于提供外壳和可能的电池等组件。

本文感谢Vlastimil OK5VAS和Andreas OE3ANC的贡献。评论区显示了对该项目的兴趣，讨论了外壳和电池类型，以及对SDR手持机前景的一些怀疑和兴奋。

---

## 51. 可视化编程困于形式

**原文标题**: Visual programming is stuck on the form

**原文链接**: [https://interjectedfuture.com/visual-programming-is-stuck-on-the-form/](https://interjectedfuture.com/visual-programming-is-stuck-on-the-form/)

本文认为，可视化编程因过度依赖节点连线范式而陷入局部最优，这种形式无法有效表达编程的底层功能。作者建议将重点从形式转移到功能，并从卢·威尔逊的CellPond中汲取灵感，该项目使用一个包含四个运算的简单虚拟机来支撑复杂的视觉模式。

核心原则是“形式追随功能”，意味着视觉表示（形式）应自然地从底层逻辑和代数（功能）中产生。作者将功能解释为包含设计的环境、合理性和代数，强调了良好定义的功能如何产生更直观和一致的形式。

本文警告了两种常见的错误：优先考虑形式而忽略功能，以及关注功能而忽视用户。作者批评了这样一种假设，即可视化编程应该仅仅以视觉方式表示现有的文本编程结构，特别是纯函数式编程。

相反，作者提出了一个新的方向：以利用人类视觉皮层能力的方式对问题进行建模。目标是创建一个可视化编程语言，在该语言中，程序的整体结构和状态在任何抽象级别都能一目了然，从而利用视觉皮层的模式识别能力。最终，本文倡导对可视化编程进行根本性的重新思考，优先考虑底层功能及其与用户认知能力的联系。

---

## 52. 北极荒野现橙色河流，预示有毒物质转移

**原文标题**: Orange rivers signal toxic shift in Arctic wilderness

**原文链接**: [https://news.ucr.edu/articles/2025/09/08/orange-rivers-signal-toxic-shift-arctic-wilderness](https://news.ucr.edu/articles/2025/09/08/orange-rivers-signal-toxic-shift-arctic-wilderness)

北极荒野现橙色河流，预示毒性转变

文章详细描述了阿拉斯加布鲁克斯山脉一个令人担忧的环境问题：由于永久冻土融化，河流变成橙色，并受到有毒金属的污染。融化暴露了富含硫化物的岩石，引发化学反应，释放硫酸，并将铁、镉和铝等金属浸出到水中。

研究人员在研究北极森林向北迁移时发现了这一现象。萨蒙河中的金属浓度现已超过美国环保署对水生生物的毒性阈值，通过减少光照穿透和窒息昆虫幼虫，危及鱼类种群。虽然目前鱼类中的金属含量对人类尚未构成危害，但这种污染对自给自足的捕鱼和整体生态系统健康构成了间接威胁。大马哈鱼是土著社区的重要食物来源，由于沉积物的积累，其产卵面临挑战。

这个问题并非萨蒙河独有；研究人员警告说，类似的变化正在其他北极流域发生。与可以实施缓解措施的酸性矿山排水不同，这些偏远的流域缺乏基础设施，并且有许多污染源，使得修复几乎不可能。阻止这一过程的唯一方法是恢复永久冻土，但在目前的变暖趋势下，这不太可能。该研究强调了气候变化的深远影响，即使在偏远和未受破坏的地区也是如此，并强调需要采取积极措施来预测和准备未来的影响。

---

## 53. Show HN: Ultraplot - matplotlib 的简洁封装

**原文标题**: Show HN: Ultraplot – A succint wrapper for matplotlib

**原文链接**: [https://github.com/Ultraplot/UltraPlot](https://github.com/Ultraplot/UltraPlot)

Ultraplot：一个精简现代的Matplotlib封装，旨在简化出版质量图形的创建。它基于ProPlot，并更新以兼容Matplotlib 3.9.0及更高版本。其核心价值是“少写代码，多出成果”，强调在生成复杂且具有视觉吸引力的绘图时的易用性和效率。

该工具提供创建复杂多面板布局、简洁笛卡尔坐标图、投影和地理绘图、可定制图例和颜色条、嵌入图和面板布局以及感知均匀的色彩映射的功能。文档托管在ReadTheDocs上。

可以通过`pip`或`conda`轻松安装，并提供升级说明。开发者也可以从GitHub安装开发版本。作者请求在使用Ultraplot进行研究时，使用提供的BibTeX条目进行引用。

---

## 54. Logfire – 基于 OpenTelemetry 的追踪 SaaS

**原文标题**: Logfire – OpenTelemetry based tracing SaaS

**原文链接**: [https://pydantic.dev/logfire](https://pydantic.dev/logfire)

Logfire 是一个基于 OpenTelemetry 的 SaaS 平台，旨在为应用程序（包括 LLM）提供从开发到生产的全面可观测性。它提供日志、追踪和指标，使开发人员能够了解其应用程序的内部运作并进行有效调试。与仅关注 LLM 调用的解决方案不同，Logfire 提供完整的应用程序可见性，包括网络调用、数据库查询和第三方 API 交互。

主要功能包括直观的设置、与常用库（如 OpenAI、FastAPI 和数据库）的集成以及强大的 SQL 查询功能，使开发人员和 AI 工具都能分析应用程序执行情况。Logfire 允许开发人员在整个开发生命周期中使用同一平台，从而最大限度地减少工具切换和上下文丢失。

Logfire 构建于 OpenTelemetry 之上，为 Python、Rust 和 Typescript 提供简化的 SDK，与直接使用 OTel SDK 相比，简化了集成。它强调全面的可观测性，集成分析功能以将性能指标与业务成果（如客户降级或支付量）相关联。

Logfire 与众多工具和框架集成，确保在不同堆栈中保持一致的视图。该平台旨在通过提供强大而灵活的可观测性解决方案来简化开发人员的生活。Python SDK 是开源的（MIT 许可证），支持将数据发送到任何符合 OTLP 的端点。文档、GitHub 存储库和 Slack 社区等资源可供用户使用。

---

## 55. 奇特的CPU架构，只有MOV指令的CPU (2020)

**原文标题**: Weird CPU architectures, the MOV only CPU (2020)

**原文链接**: [https://justanotherelectronicsblog.com/?p=771](https://justanotherelectronicsblog.com/?p=771)

本文探讨了传输触发架构（TTA），一种CPU架构，其唯一的指令是“移动”，所有操作都通过在内存位置之间移动数据来执行，包括ALU输入和程序计数器。作者深入研究了这个概念，强调了它与具有寄存器和ALU的传统CPU设计的区别。

TTA的核心思想是CPU只移动数据，而计算是这些移动的副作用。例如，将两个数字相加涉及到将它们移动到ALU输入内存位置，触发加法运算，然后将结果从ALU输出位置移动到另一个内存位置。

作者随后详细介绍了在数字逻辑模拟器Digital中构建一个简单的16位TTA CPU的过程。该设计包括：

*   **CPU：** 处理指令地址（源地址和目标地址）的获取以及它们之间的数据移动。
*   **程序计数器：** 内存映射，通过将新地址移动到其中来更新，从而实现跳转。
*   **ALU：** 由74_181芯片构建，当数据移动到其输入寄存器时执行计算。
*   **流程控制块：** 通过比较两个值并输出两个地址之一来进行有条件的分支，以便跳转到该地址。

最后，作者通过实现斐波那契数列的计算来演示CPU的功能，展示了需要大量“移动”指令才能完成相对简单的任务。文章的结论是，虽然TTA可能不是最高效或最快的架构，但它们提供了一种有趣且紧凑的替代方案，并且这个过程是对一种古怪的CPU设计的有趣探索。

---

## 56. Mago: 用 Rust 编写的快速 PHP 工具链

**原文标题**: Mago: A fast PHP toolchain written in Rust

**原文链接**: [https://github.com/carthage-software/mago](https://github.com/carthage-software/mago)

Mago：一款快速全面的 PHP 工具链

Mago 是一款使用 Rust 编写的快速且全面的 PHP 工具链，旨在提高代码质量和开发者体验。它提供代码检查、格式化和静态分析功能，力求成为现有 PHP 工具的现代高效替代方案。

其主要特性包括基于 Rust 的速度优势、可定制的代码检查规则、用于捕获类型错误和漏洞的静态分析、自动化修复、代码格式化、语义检查和 AST 可视化。

该工具链的灵感来源于 Rust 项目，如 Clippy 和 OXC，以及 PHP 静态分析工具，如 Hakana。在肯定 PHP-CS-Fixer、Psalm、PHPStan 和 PHP_CodeSniffer 等工具的基础性贡献的同时，Mago 旨在提供一种更快且统一的解决方案。

macOS 和 Linux 平台的安装说明通过 shell 脚本提供，其他选项可在官方文档中找到。Mago 是一个社区驱动的项目，欢迎通过错误报告、功能建议、文档和代码提交来贡献。它采用 MIT 和 Apache 2.0 双重许可。

---

## 57. 感知年龄 (2024)

**原文标题**: Perceived Age (2024)

**原文链接**: [https://sdan.io/blog/perceived-age](https://sdan.io/blog/perceived-age)

本文探讨了感知年龄的现象以及随着年龄增长时间加速流逝的感觉。文章认为，时间感知并非固定不变，而是受到神经生物学，特别是多巴胺水平，以及我们心理体验的影响。

作者解释说，新鲜感是一个关键因素：年轻人感觉时间更慢，是因为他们经历了很多“第一次”，使他们的大脑充满了多巴胺。随着年龄的增长，体验变得不再新鲜，多巴胺水平降低，时间似乎加速流逝。这与“回忆高峰期”有关，我们青年时期的重大事件塑造了我们的身份，并且被更生动地记住，从而进一步延长了感知到的时间。

本文借鉴了研究，展示了不同年龄段的人如何感知时间以及多巴胺在这个过程中的作用。它还涉及外部因素，如兴奋剂、抗精神病药物，甚至单调的日常活动，对我们时间感知的影响。

“感知年龄”的概念被引入，以量化这种体验，说明每一年相对于我们总的人生经历感觉成比例地缩短。作者认为，虽然我们无法阻止时间，但我们可以通过寻求新鲜感、拥抱变化、接受认知挑战以及采取新的生活方式来打破单调的常规，从而影响我们的感知。作者鼓励读者拥抱充满活力的生活，即使在资本主义和社会期望的压力下，并强调浪费的时间会导致浪费的岁月。文章以作者自己的经历和一个重新燃起的乐观感作为结尾。

---

## 58. 魔法系统思维

**原文标题**: Magical systems thinking

**原文链接**: [https://worksinprogress.co/issue/magical-systems-thinking/](https://worksinprogress.co/issue/magical-systems-thinking/)

本文批判了“系统思维”在现代政府中的应用，认为尽管其流行和拥有复杂的工具，但它往往导致失败。文章强调了诸如HealthCare.gov和澳大利亚的残疾改革等历史案例，在这些案例中，善意的系统性设计适得其反。

作者将此与电力网等成功复杂系统的逐步演进式发展进行了对比，电力网通过渐进式改进从简单的起点发展而来。文章引用了杰伊·福雷斯特失败的“世界模型”作为对预测建模过度自信的例子，同时强调了他早期通过关注较小、更易于管理的系统内的反馈循环来提高工厂效率的成功。

文章介绍了勒夏特列原理——系统会抵抗强加的改变——以及约翰·盖尔的《系统论》，该书幽默地概述了系统容易发生故障的方式。盖尔定律被认为是关键的见解：有效的复杂系统总是从有效的简单系统演变而来。

作者以游戏Factorio为例，说明了成功的系统构建过程，玩家从简单的、可以工作的组件开始，通过迭代学习逐步扩展到复杂的、功能齐全的工厂。文章总结说，虽然现有的政府系统不容易被取代，但创建新的、简单的、平行的系统提供了一条更有效的改进途径。

---

## 59. 为什么这么多年轻、健康、不吸烟的女性会得肺癌？

**原文标题**: Why are so many young, fit, non-smoking women getting lung cancer?

**原文链接**: [https://www.theguardian.com/society/2025/sep/14/lung-cancer-young-fit-non-smoking-women](https://www.theguardian.com/society/2025/sep/14/lung-cancer-young-fit-non-smoking-women)

年轻、健康、不吸烟女性肺癌发病率令人担忧的上升
这篇文章探讨了年轻、健康、不吸烟女性肺癌发病率令人担忧的上升，这一人群在历史上被认为是低风险人群。长期以来，肺癌一直被认为是“吸烟者的疾病”，导致资金不足和污名化。然而，数据显示非吸烟病例显著增加，主要集中在女性中。

文章重点介绍了贝卡·史密斯和李莎两位年轻女性的故事，她们虽然生活方式健康，却被诊断出患有晚期肺癌。医生们对这一趋势感到困惑，指出潜在因素包括荷尔蒙影响、空气污染和基因突变，尤其是EGFR。室外和室内空气污染（燃烧炉/生物质燃料）被认为是潜在的风险因素，女性较小的肺活量可能会增加污染物浓度。

文章强调了吸烟者和非吸烟肺癌患者在症状表现、诊断途径和癌症生物学方面的差异。非吸烟者通常在晚期才被诊断出来，并且脑转移的发生率更高。研究和临床试验历来侧重于男性吸烟者，导致对女性疾病的了解存在差距。

文章还探讨了肺癌治疗的进展，特别是针对基因突变的靶向疗法，以及解决肺癌对女性生育能力和整体健康影响的重要性。尽管面临挑战，像史密斯和李莎这样的女性正在充实地生活，在日常生活中寻找快乐，并倡导研究和提高认识。

---

## 60. 赤道几内亚对举行抗议活动的岛屿实施长达一年的互联网封锁。

**原文标题**: Equatorial Guinea enforces yearlong internet outage for island that protested

**原文链接**: [https://apnews.com/article/equatorial-guinea-internet-shutdown-africa-d7daacc641475743972b33eaffffa4fc](https://apnews.com/article/equatorial-guinea-internet-shutdown-africa-d7daacc641475743972b33eaffffa4fc)

在安诺本岛居民抗议摩洛哥建筑公司Somagec的活动后，赤道几内亚对该岛实施了为期一年的互联网中断。居民指控该公司炸药爆炸污染了他们的土地和水源。抗议后，数十名居民被监禁近一年。居民和人权组织证实，互联网中断仍在生效，瘫痪了银行和医疗保健服务，迫使居民依赖昂贵且受监控的电话。

安诺本岛是一个偏远且贫困的岛屿，寻求赤道几内亚赋予其更大的自治权，历史上与中央政府存在冲突。活动人士表示，互联网中断是最新的压制措施，加剧了该岛的边缘化，并摧毁了关键基础设施。

据称与总统有关联的 Somagec 公司否认参与互联网中断，并声称炸药爆破对于其建筑项目是必要的。活动人士认为，政府的行为表明非洲使用互联网中断来压制异议的趋势日益增长。尽管 Somagec 公司于 2013 年在该岛建造了新机场，但由于互联网中断，生活条件恶化。活动人士称，互联网中断使该岛与世隔绝，处于“失联”状态。

---

## 61. L1TTL3 PAWS – 13kb猫咪滑翔游戏，拥有程序生成艺术和关卡

**原文标题**: L1TTL3 PAWS – Cat glider with procedural art and levels in only 13kb

**原文链接**: [https://github.com/KilledByAPixel/JS13K2025](https://github.com/KilledByAPixel/JS13K2025)

L1TTL3 PAWS 是一款由 Frank Force 为 JS13K 2025 竞赛创作的猫咪滑翔游戏，令人印象深刻地将其大小控制在 13kb 文件内。玩家操控一只猫咪滑翔机，在程序生成的地形中穿梭于 13 个岛屿之间。游戏包含 13 个可解锁的猫咪角色。

游戏玩法包括使用鼠标、触摸或键盘控制来管理猫咪在斜坡上的速度（按下加速下坡，松开加速上坡）。玩家收集鲜花来购买新猫咪，并吃披萨来获得速度提升。

游戏提供两种模式：具有一致关卡的经典模式，以及在通关经典模式后解锁的随机关卡混音模式。游戏具有继续系统，保存收集到的硬币以供将来使用，并在没有继续的情况下获胜时记录最佳时间。它还包括视差背景效果、一天中的时间系统，并适应各种屏幕分辨率。

控制方式很简单：空格键、鼠标或触摸控制按下，'R' 重新开始关卡，'Escape' 返回。开发者声明代码仅用于教育目的，不可重新分发。游戏还提供了一个加密货币捐赠链接，用于帮助无家可归的宠物。该游戏献给开发者的猫咪 Baldy。

---

## 62. UTF-8 是一个绝妙的设计。

**原文标题**: UTF-8 is a brilliant design

**原文链接**: [https://iamvishnu.com/posts/utf8-is-brilliant-design](https://iamvishnu.com/posts/utf8-is-brilliant-design)

本文赞颂了UTF-8编码的卓越性，强调了其在表示广泛字符范围的同时，保持与ASCII向后兼容的能力。UTF-8采用可变宽度编码方案，每个字符使用1到4个字节。前128个字符（ASCII）用单个字节编码，确保了兼容性。多字节字符通过首字节中的前导位来识别，这些前导位指示后续延续字节的数量。

本文详细介绍了UTF-8解码的工作原理：通过检查每个字节的前导位来确定字符的长度，然后组合剩余的位来推导字符的代码点（其唯一标识符）。然后使用此代码点在Unicode字符集中查找相应的字符。

作者提供了实际示例，演示了印地语字母“अ”和表情符号“👋”如何在UTF-8中编码。这些示例阐明了解码过程如何识别字节数并提取代码点。本文强调，仅包含ASCII字符的文件是有效的UTF-8文件，展示了向后兼容性。包含非ASCII字符的文件是有效的UTF-8文件，但不向后兼容ASCII。

最后，作者提到了其他与ASCII兼容的编码，如GB 18030和ISO/IEC 8859，但指出它们与UTF-8相比存在局限性。UTF-8的同胞兄弟UTF-16和UTF-32与ASCII不向后兼容。作者还介绍了UTF-8 Playground，这是一个用于可视化和实验UTF-8编码的实用工具。本文最后提供了进一步阅读和关于该主题的讨论的参考资料。

---

## 63. Show HN: Vicinae - 一款原生、兼容 Raycast 的 Linux 启动器

**原文标题**: Show HN: Vicinae – A native, Raycast-compatible launcher for Linux

**原文链接**: [https://github.com/vicinaehq/vicinae](https://github.com/vicinaehq/vicinae)

Vicinae 是一款高性能的 Linux 原生启动器，旨在提供类似 Raycast 的体验，同时避免 Electron 的开销。它使用 C++ 和 Qt 构建，专注于速度和键盘优先访问，面向开发者和高级用户。

主要功能包括：

*   **应用程序启动：** 启动并查找已安装的应用程序的信息。
*   **文件索引：** 对数百万个文件进行全文搜索。
*   **表情符号选择器：** 带有自定义关键字的智能表情符号选择。
*   **计算器：** 带有历史记录和多个后端的内联计算器。
*   **剪贴板历史记录：** 具有全文搜索功能的加密剪贴板跟踪。
*   **快捷方式：** 使用动态链接快速打开任何内容。
*   **窗口管理器集成：** 与焦点窗口直接交互。
*   **主题：** 内置浅色和深色主题，并支持自定义主题。

一个值得注意的特点是其 Raycast 兼容模块，该模块允许用户直接从 Raycast 商店安装扩展程序。虽然由于 API 差异和 Linux 不兼容性，并非所有扩展程序都完全兼容，但 Vicinae 旨在为 Raycast 用户提供无缝过渡。

扩展程序在服务器端使用 React/TypeScript 开发，避免使用浏览器或 Electron。安装、使用、配置、扩展程序开发和贡献的文档可以在 docs.vicinae.com 找到。

---

## 64. 日本百岁老人近十万，创历史新高

**原文标题**: Japan sets record of nearly 100k people aged over 100

**原文链接**: [https://www.bbc.com/news/articles/cd07nljlyv0o](https://www.bbc.com/news/articles/cd07nljlyv0o)

日本百岁老人连续55年创新高，逼近10万人，其中女性占比88%。这一里程碑凸显了日本世界领先的预期寿命以及作为老龄化速度最快的社会之一的地位。日本最年长的女性为114岁，最年长的男性为111岁。

百岁老人人数的增加归功于更健康的饮食（红肉摄入量低，鱼类和蔬菜摄入量高，盐和糖摄入量低）、较低的肥胖率以及积极的生活方式，包括定期散步和广播体操等集体锻炼。这些因素有助于减少死于心脏病和常见癌症的人数。

然而，文章还指出，一些研究质疑全球百岁老人数据的准确性，原因在于潜在的数据错误和不可靠的记录。日本2010年的一次审计显示，存在已故人士被虚报为百岁老人的情况，这可能是由于记录保存问题和养老金欺诈造成的。尽管存在这些担忧，日本的显著成就仍然突显了该国在促进长寿方面的成功。

---

## 65. 内联缓存不仅仅是缓存

**原文标题**: An Inline Cache Isn't Just a Cache

**原文链接**: [https://www.mgaudet.ca/technical/2018/6/5/an-inline-cache-isnt-just-a-cache](https://www.mgaudet.ca/technical/2018/6/5/an-inline-cache-isnt-just-a-cache)

本文探讨了内联缓存，阐明它不仅仅是通常理解的简单缓存。文章追溯了该概念至Deutsch和Schiffman在1984年发表的论文，其中内联缓存被引入作为方法分发的一种自修改代码，基于局部性假设，即调用点通常解析为相同的方法。

文章随后解释了SpiderMonkey (JavaScript引擎) 如何实现内联缓存。它没有直接修改代码，而是使用“桩(stubs)”，即链式连接的小段可执行代码。 这些桩包含健全性检查（guard）和所需的操作。当第一次遇到一个操作时，会创建一个桩。 如果guard失败（例如，当存在整数加法桩时，将字符串添加到整数），则该桩跳转到链中的下一个桩或回退路径，后者使用通用VM处理计算。如果回退成功，则为观察到的情况创建一个新的桩。

文章用JavaScript中两个数字相加的例子说明了这个过程。第一次两个整数相加时，会创建一个 `Int32 + Int32` 桩。 随后的整数加法会命中这个缓存，避免了完整的JavaScript加法算法。 不同类型的加法（例如，字符串）会导致创建额外的桩，形成一个链。

文章总结说，SpiderMonkey中使用的内联缓存是一种强大的优化技术，涉及自修改控制流和运行时特化。作者指出，SpiderMonkey的内联缓存中看到的通用性出现在1983年至2004年之间的某个时间，并且它是一项关键的优化，尤其是在优化编译器IonMonkey无法找到更好的方法的情况下。

---

## 66. 这是词典的末日吗？

**原文标题**: Is This the End of the Dictionary?

**原文链接**: [https://www.theatlantic.com/magazine/archive/2025/10/dictionary-survival-language-evolution/683976/](https://www.theatlantic.com/magazine/archive/2025/10/dictionary-survival-language-evolution/683976/)

斯蒂芬·法特西斯的文章《字典的末日到了吗？》探讨了现代字典的悖论：语言研究蓬勃发展，字典唾手可得，但字典生意却举步维艰。由于算法变更、免费在线释义的竞争以及对传统权威的不信任，字典面临着收入下降的问题。兰登书屋和韦氏新世界词典等主要参与者已经衰退。

文章重点关注了作为剩余关键参与者的韦氏词典和Dictionary.com。韦氏词典在最初的挣扎之后，通过社交媒体、游戏和算法导航进行了调整。Dictionary.com被丹·吉尔伯特收购后，通过俚语和趋势驱动的内容进行了创新。然而，谷歌的“知识框”显著减少了Dictionary.com的流量，导致了财务压力，并最终出售给了IXL Learning，这导致了其词典编纂团队的裁员。

法特西斯认为，传统的字典商业模式正在失败。他认为，科技巨头的收购和亿万富翁资助的项目是不可持续的。虽然一个协作式的国家字典项目是理想的，但在当前的气候下是不太可能的。他最后强调了保护字典的紧迫性，以及词典编纂者在定义和解释有争议的词语方面所起的关键作用，尤其是在“假新闻”和其他两极分化术语盛行的时代。他曾为韦氏词典贡献词条，定义了诸如“微侵犯”和“蜂拥而上”等词语。

---

## 67. Perrinn 424 – 一款为赛车设计的开放式电动超级跑车

**原文标题**: Perrinn 424 – An open access electric hyper car designed for racing

**原文链接**: [https://discover.perrinn.com/home](https://discover.perrinn.com/home)

Perrinn 424 是由工程师尼科·佩兰领导的一项雄心勃勃的计划，旨在打造一款全电动超级跑车，目标是打破纽博格林北环赛道纪录，并最终使用氢能源技术参加勒芒 24 小时耐力赛。佩兰是一位 F1 和勒芒老将，他将 424 视为不仅仅是一辆破纪录的赛车，更是对电动性能未来的宣言，以及对突破工程界限的证明。

424 拥有来自两个 Formula E 电动机的 700 千瓦功率，并采用先进的 Formula 1 灵感来源的空气动力学设计。关键合作伙伴包括 Formula E 动力系统供应商、米其林轮胎供应商、Formula 1 复合材料供应商、Dynisma 虚拟测试供应商以及 PTC 设计和数字基础设施供应商。

可持续性是核心原则，该项目利用分布式网络和数字工具来最大限度地减少环境影响。车队正在社交媒体上透明地记录开发过程，旨在激发全球合作，使赛车运动更易于参与。

目前，该项目正处于详细设计阶段，概念设计和虚拟测试已经完成。车队正在积极筹集资金，以便在 18 个月内完成建造，包括测试和打破纪录的尝试。他们已经拥有一个忠实的追随者和贡献者社区。佩兰在赛车运动方面的丰富经验，包括他最近在 Jaguar TCS Racing Formula E 世界锦标赛中的角色，为该项目的可信度和雄心勃勃的目标奠定了基础。

---

## 68. How to get samples back from Mars

**原文标题**: How to get samples back from Mars

**原文链接**: [https://caseyhandmer.wordpress.com/2025/09/13/how-to-get-samples-back-from-mars/](https://caseyhandmer.wordpress.com/2025/09/13/how-to-get-samples-back-from-mars/)

生成摘要时出错

---

## 69. SkiftOS: A hobby OS built from scratch using C/C++ for ARM, x86, and RISC-V

**原文标题**: SkiftOS: A hobby OS built from scratch using C/C++ for ARM, x86, and RISC-V

**原文链接**: [https://skiftos.org](https://skiftos.org)

生成摘要时出错

---

## 70. Ollee Watch: Turn your classic Casio watch into a smartwatch

**原文标题**: Ollee Watch: Turn your classic Casio watch into a smartwatch

**原文链接**: [https://www.olleewatch.com](https://www.olleewatch.com)

生成摘要时出错

---

## 71. I used standard Emacs extension-points to extend org-mode

**原文标题**: I used standard Emacs extension-points to extend org-mode

**原文链接**: [https://edoput.it/2025/04/16/emacs-paradigm-shift.html](https://edoput.it/2025/04/16/emacs-paradigm-shift.html)

生成摘要时出错

---

## 72. Child's Death Shows How Measles in the Brain Can Kill Years After an Infection

**原文标题**: Child's Death Shows How Measles in the Brain Can Kill Years After an Infection

**原文链接**: [https://www.scientificamerican.com/article/measles-death-shows-how-virus-can-hide-in-the-brain-for-years/](https://www.scientificamerican.com/article/measles-death-shows-how-virus-can-hide-in-the-brain-for-years/)

生成摘要时出错

---

## 73. EFF to court: The Supreme Court must rein in secondary copyright liability

**原文标题**: EFF to court: The Supreme Court must rein in secondary copyright liability

**原文链接**: [https://www.eff.org/deeplinks/2025/09/eff-court-supreme-court-must-rein-expansive-secondary-copyright-liability](https://www.eff.org/deeplinks/2025/09/eff-court-supreme-court-must-rein-expansive-secondary-copyright-liability)

生成摘要时出错

---

## 74. Does All Semiconductor Manufacturing Depend on Spruce Pine Quartz? (2024)

**原文标题**: Does All Semiconductor Manufacturing Depend on Spruce Pine Quartz? (2024)

**原文链接**: [https://www.construction-physics.com/p/does-all-semiconductor-manufacturing](https://www.construction-physics.com/p/does-all-semiconductor-manufacturing)

生成摘要时出错

---

## 75. Many hard LeetCode problems are easy constraint problems

**原文标题**: Many hard LeetCode problems are easy constraint problems

**原文链接**: [https://buttondown.com/hillelwayne/archive/many-hard-leetcode-problems-are-easy-constraint/](https://buttondown.com/hillelwayne/archive/many-hard-leetcode-problems-are-easy-constraint/)

生成摘要时出错

---

## 76. An open-source maintainer's guide to saying “no”

**原文标题**: An open-source maintainer's guide to saying “no”

**原文链接**: [https://www.jlowin.dev/blog/oss-maintainers-guide-to-saying-no](https://www.jlowin.dev/blog/oss-maintainers-guide-to-saying-no)

生成摘要时出错

---

## 77. Tips for installing Windows 98 in QEMU/UTM

**原文标题**: Tips for installing Windows 98 in QEMU/UTM

**原文链接**: [https://sporks.space/2025/08/28/tips-for-installing-windows-98-in-qemu-utm/](https://sporks.space/2025/08/28/tips-for-installing-windows-98-in-qemu-utm/)

生成摘要时出错

---

## 78. AI coding

**原文标题**: AI coding

**原文链接**: [https://geohot.github.io//blog/jekyll/update/2025/09/12/ai-coding.html](https://geohot.github.io//blog/jekyll/update/2025/09/12/ai-coding.html)

生成摘要时出错

---

## 79. Raspberry Pi Synthesizers – How the Pi is transforming synths

**原文标题**: Raspberry Pi Synthesizers – How the Pi is transforming synths

**原文链接**: [https://www.gearnews.com/raspberry-pi-synthesizers-how-the-pi-is-transforming-synths/](https://www.gearnews.com/raspberry-pi-synthesizers-how-the-pi-is-transforming-synths/)

生成摘要时出错

---

## 80. Life, work, death and the peasant: Rent and extraction

**原文标题**: Life, work, death and the peasant: Rent and extraction

**原文链接**: [https://acoup.blog/2025/09/12/collections-life-work-death-and-the-peasant-part-ivc-rent-and-extraction/](https://acoup.blog/2025/09/12/collections-life-work-death-and-the-peasant-part-ivc-rent-and-extraction/)

生成摘要时出错

---

## 81. Lessons in disabling RC4 in Active Directory (2021)

**原文标题**: Lessons in disabling RC4 in Active Directory (2021)

**原文链接**: [https://syfuhs.net/lessons-in-disabling-rc4-in-active-directory](https://syfuhs.net/lessons-in-disabling-rc4-in-active-directory)

生成摘要时出错

---

## 82. Design Principles for Precision Mechatronics

**原文标题**: Design Principles for Precision Mechatronics

**原文链接**: [https://www.dspe.nl/knowledge/dppm-cases/](https://www.dspe.nl/knowledge/dppm-cases/)

生成摘要时出错

---

## 83. New Bill Would Give Marco Rubio "Thought Police" Power to Revoke U.S. Passports

**原文标题**: New Bill Would Give Marco Rubio "Thought Police" Power to Revoke U.S. Passports

**原文链接**: [https://theintercept.com/2025/09/13/marco-rubio-revoke-us-passports-terrorism/](https://theintercept.com/2025/09/13/marco-rubio-revoke-us-passports-terrorism/)

生成摘要时出错

---

## 84. How to use Claude Code subagents to parallelize development

**原文标题**: How to use Claude Code subagents to parallelize development

**原文链接**: [https://zachwills.net/how-to-use-claude-code-subagents-to-parallelize-development/](https://zachwills.net/how-to-use-claude-code-subagents-to-parallelize-development/)

生成摘要时出错

---

## 85. ‘Overworked, underpaid’ humans train Google’s AI

**原文标题**: ‘Overworked, underpaid’ humans train Google’s AI

**原文链接**: [https://www.theguardian.com/technology/2025/sep/11/google-gemini-ai-training-humans](https://www.theguardian.com/technology/2025/sep/11/google-gemini-ai-training-humans)

生成摘要时出错

---

## 86. Energy-Based Transformers [video]

**原文标题**: Energy-Based Transformers [video]

**原文链接**: [https://www.youtube.com/watch?v=LUQkWzjv2RM](https://www.youtube.com/watch?v=LUQkWzjv2RM)

生成摘要时出错

---

## 87. Mozilla Firefox Is Officially Getting MKV Video Support

**原文标题**: Mozilla Firefox Is Officially Getting MKV Video Support

**原文链接**: [https://windowsreport.com/mozilla-firefox-is-officially-getting-mkv-video-support/](https://windowsreport.com/mozilla-firefox-is-officially-getting-mkv-video-support/)

生成摘要时出错

---

## 88. Show HN: Small Transfers – charge from 0.000001 USD per request for your SaaS

**原文标题**: Show HN: Small Transfers – charge from 0.000001 USD per request for your SaaS

**原文链接**: [https://smalltransfers.com/](https://smalltransfers.com/)

生成摘要时出错

---

## 89. How FOSS Projects Handle Legal Takedown Requests

**原文标题**: How FOSS Projects Handle Legal Takedown Requests

**原文链接**: [https://f-droid.org/2025/09/10/how-foss-projects-handle-legal-takedown-requests.html](https://f-droid.org/2025/09/10/how-foss-projects-handle-legal-takedown-requests.html)

生成摘要时出错

---

## 90. New bacteria, and two potential antibiotics, discovered in soil

**原文标题**: New bacteria, and two potential antibiotics, discovered in soil

**原文链接**: [https://phys.org/news/2025-09-hundreds-bacteria-potential-antibiotics-soil.html](https://phys.org/news/2025-09-hundreds-bacteria-potential-antibiotics-soil.html)

生成摘要时出错

---

## 91. Meow: Yet another modal editing on Emacs

**原文标题**: Meow: Yet another modal editing on Emacs

**原文链接**: [https://github.com/meow-edit/meow](https://github.com/meow-edit/meow)

生成摘要时出错

---

## 92. Legal win

**原文标题**: Legal win

**原文链接**: [https://ma.tt/2025/09/legal-win/](https://ma.tt/2025/09/legal-win/)

生成摘要时出错

---

## 93. Corporations are trying to hide job openings from US citizens

**原文标题**: Corporations are trying to hide job openings from US citizens

**原文链接**: [https://thehill.com/opinion/finance/5498346-corporate-america-has-been-trying-to-hide-job-openings-now-it-is-failing/](https://thehill.com/opinion/finance/5498346-corporate-america-has-been-trying-to-hide-job-openings-now-it-is-failing/)

生成摘要时出错

---

## 94. Social media promised connection, but it has delivered exhaustion

**原文标题**: Social media promised connection, but it has delivered exhaustion

**原文链接**: [https://www.noemamag.com/the-last-days-of-social-media/](https://www.noemamag.com/the-last-days-of-social-media/)

生成摘要时出错

---

## 95. QGIS is a free, open-source, cross platform geographical information system

**原文标题**: QGIS is a free, open-source, cross platform geographical information system

**原文链接**: [https://github.com/qgis/QGIS](https://github.com/qgis/QGIS)

生成摘要时出错

---

## 96. Java 25's new CPU-Time Profiler

**原文标题**: Java 25's new CPU-Time Profiler

**原文链接**: [https://mostlynerdless.de/blog/2025/06/11/java-25s-new-cpu-time-profiler-1/](https://mostlynerdless.de/blog/2025/06/11/java-25s-new-cpu-time-profiler-1/)

生成摘要时出错

---

## 97. Can you help us crack the Dickens Code?

**原文标题**: Can you help us crack the Dickens Code?

**原文链接**: [https://dickenscode.org/](https://dickenscode.org/)

生成摘要时出错

---

## 98. Windows-Use: an AI agent that interacts with Windows at GUI layer

**原文标题**: Windows-Use: an AI agent that interacts with Windows at GUI layer

**原文链接**: [https://github.com/CursorTouch/Windows-Use](https://github.com/CursorTouch/Windows-Use)

生成摘要时出错

---

## 99. Resizing images in Rust, now with EXIF orientation support

**原文标题**: Resizing images in Rust, now with EXIF orientation support

**原文链接**: [https://alexwlchan.net/2025/create-thumbnail-is-exif-aware/](https://alexwlchan.net/2025/create-thumbnail-is-exif-aware/)

生成摘要时出错

---

## 100. Ancient DNA solves Plague of Justinian mystery to rewrite pandemic history

**原文标题**: Ancient DNA solves Plague of Justinian mystery to rewrite pandemic history

**原文链接**: [https://phys.org/news/2025-08-ancient-dna-plague-justinian-mystery.html](https://phys.org/news/2025-08-ancient-dna-plague-justinian-mystery.html)

生成摘要时出错

---

