# Hacker News 热门文章摘要 (2025-04-26)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 观看o3猜测照片位置既超现实，反乌托邦又有趣。

**原文标题**: Watching o3 guess a photo's location is surreal, dystopian and entertaining

**原文链接**: [https://simonwillison.net/2025/Apr/26/o3-photo-locations/](https://simonwillison.net/2025/Apr/26/o3-photo-locations/)

本文探讨了OpenAI的o3模型在识别照片拍摄地点方面的能力，突出了其准确性、超现实性质以及潜在的反乌托邦影响。作者详细描述了一项实验，其中o3的任务是仅使用提供的视觉信息来猜测一张在加利福尼亚州埃尔格兰纳达拍摄的照片的地点。

该模型在最初出现故障后，采用了一种复杂的流程，包括“缩放”和分析车牌、植被和建筑等细节，以缩小范围。虽然最初猜测是加利福尼亚州的坎布里亚，但该模型正确地将半月湾-埃尔格兰纳达确定为其下一个最佳猜测。

作者强调，集成到响应的“思考”阶段的工具使用是使o3和其他模型（如Claude 3.7 Sonnet）如此强大的原因。 文章突出了观看模型推理过程的娱乐价值，将其比作CSI中的场景。

然而，它也引发了对隐私影响的担忧，指出这项技术使得从看似无害的照片中精确定位变得容易。这种可访问性是一把双刃剑，在提高人们对技术能力的认识的同时，也增加了对自身安全感到担忧的个人被识别位置的风险。

文章更新承认o3可以访问用户的近似位置，这可能有助于其准确性。然而，对来自遥远地点的照片进行的测试仍然产生了令人印象深刻的结果，这表明该模型的视觉分析是其成功的关键因素。

---

## 2. 展示HN：我自写的业余操作系统终于在我的老式IBM ThinkPad上运行了

**原文标题**: Show HN: My self-written hobby OS is finally running on my vintage IBM ThinkPad

**原文链接**: [https://github.com/joexbayer/RetrOS-32](https://github.com/joexbayer/RetrOS-32)

此“Show HN”帖子介绍了 RetrOS-32，一个业余的 32 位操作系统项目，专注于 i386 架构上的网络。该项目于 2022 年 5 月启动，具有图形、多任务和网络功能。操作系统主要使用 C 和汇编语言编写内核和实用程序，而用户空间应用程序则使用 C++ 编写。Docker 用于跨平台编译。

该帖子详细介绍了如何开始，包括在 Linux、macOS 和 Windows 上进行本地和跨平台（基于 Docker）编译的先决条件。安装说明包括克隆存储库、初始化 Git 子模块和运行 `make` 命令。

该操作系统可以使用 copy.sh/v86（通过上传 .img 文件）、QEMU 运行，或通过将 .iso 刻录到 USB 或 CD 在真实硬件上运行。提供默认用户帐户（system、admin、guest）。

该项目路线图概述了未来发展的宏伟计划，包括自定义引导加载程序增强功能、高级内存管理、完整的网络堆栈、GUI 改进（窗口管理器、小部件）、C 编译器、自定义 VM 和各种应用程序。它以 MIT 许可证发布，作者提供了项目存储库链接和联系信息。经过测试的硬件包括多个联想、华硕、戴尔和三星型号，以及一台 IBM Thinkpad a21p。

---

## 3. 结束所有这些前列腺问题？

**原文标题**: An end to all this prostate trouble?

**原文链接**: [https://yarchive.net/blog/prostate/](https://yarchive.net/blog/prostate/)

本文探讨了Gat和Goren医生提出的良性前列腺增生(BPH)、前列腺癌和精索静脉曲张的潜在机械病因和外科疗法。该理论认为，精索静脉瓣功能不全导致血液倒流至睾丸，引起缺氧和不育。这种富含高浓度、未结合睾酮的回流会溢入前列腺，促进过度生长，并可能导致BPH和癌症。

标准医学文献通常将热作为与这种回流相关的不育的主要原因，但Gat和Goren认为，最终造成损害的是缺氧。

Gat和Goren提出的解决方案是一种微创手术，通过硬化剂破坏精索静脉，将血液重新导流到其他通路。这消除了前列腺的睾酮过载，并恢复了睾丸的正常氧合。他们认为，问题源于人类的直立姿势，这给精索静脉瓣带来了压力。

虽然Gat和Goren的结果看起来很有希望，但医学界在很大程度上忽略了这一理论。作者深入研究了血压和重力的力学原理，质疑仅凭压力差是否可以解释逆流。尽管有此保留，作者承认逆流的真实存在以及Gat和Goren研究的潜在重要性，并强调需要对这种易于筛查且可能治愈的、影响许多男性的疾病进行进一步调查。

---

## 4. 填充Na(a)N：填充你的NaN值

**原文标题**: Stuffed-Na(a)N: stuff your NaNs

**原文链接**: [https://github.com/si14/stuffed-naan-js](https://github.com/si14/stuffed-naan-js)

Stuffed-Na(a)N：一个将数据编码为 JavaScript NaN 值的幽默库

"Stuffed-Na(a)N" 介绍了一个幽默的库，它将数据编码成 JavaScript 的 `NaN` 值。作者以戏谑的方式突出了 JavaScript 中 `NaN` 传播的特性，并提出了一种将数据“塞入” `NaN` 通常未使用的 fraction 部分的方法。

`stuffed-naan` 库允许用户将字符串编码为 `NaN` 数组，然后再将其解码回来。它声称具有诸多优点，例如体积小巧（具有负压缩比）、由于 ECMAScript® 2026 中的字节操作而实现的极速编码，以及增强的隐私性，因为 `NaN` 数据不容易被复制。

这篇文章宣传了社区版（可通过 npm 或 unpkg 获取）和企业版，后者具有更高效的编码、对大端处理器的支持以及专门的客户支持。路线图概述了计划中的功能，包括基准测试、模糊测试、Rust 重写和形式验证。

作者承认该项目的荒谬性，但指出了利用 IEEE 754 浮点数结构进行非常规数据存储的潜在应用。文章最后呼吁大家支持当地的咖喱店，并附有作者社交媒体的链接。

---

## 5. LLMs 无需训练即可视听。

**原文标题**: LLMs can see and hear without any training

**原文链接**: [https://github.com/facebookresearch/MILS](https://github.com/facebookresearch/MILS)

本文档描述了论文“LLMs can see and hear without any training”的实现，介绍了 MILS，一种仅用于推理的方法，使大型语言模型 (LLMs) 能够在无需特定训练的情况下执行图像、音频和视频理解任务。它概述了使用 conda 环境的安装过程、所需的数据集（MS-COCO、Clotho、MSR-VTT）和检查点，以及如何配置文件路径。本文档详细介绍了各种任务的执行过程，包括图像描述、音频描述、视频描述、高质量图像生成、风格迁移和跨模态算术。它强调 MILS 可以在单个 A100 GPU 上运行，尽管实验是在八个 GPU 上进行的。说明包括运行每个任务代码的具体命令、如何指定输出目录以及如何评估结果。最后，它阐述了问题、贡献指南、许可（CC-by-NC 4.0）和引用信息。核心思想围绕利用预训练的 LLMs 进行多模态任务，从而实现生成图像、音频和视频的描述、提高图像生成质量、执行风格迁移和执行跨模态算术运算等功能。

---

## 6. 谢谢你帮我拿鸭子 (2021)

**原文标题**: Thank you for holding my duck (2021)

**原文链接**: [https://naml.us/post/thank-you-for-holding-my-duck/](https://naml.us/post/thank-you-for-holding-my-duck/)

这篇博文探讨了短语“感谢你帮我拿鸭子”的起源，它被用作一种问题解决技巧的速记方式。作者讲述了一个故事，一位研究人员向一位同事解释一个问题，这位同事只是拿着一只橡皮鸭，却让说话者在解释的过程中意识到了解决方案。这个版本强调了常见的“橡皮鸭调试”中所缺乏的关键社交互动，后者指的是与无生命物体交谈。

最初无法找到确切的来源，作者将这个故事追溯到皮克斯的 Bill Polson，他从 Leo Hourvitz 那里学到了这个故事，而 Hourvitz 又听说它起源于 Xerox PARC。Hourvitz 将这个概念描述为从一只真正的鸭子（可能用来表示发言顺序）演变为代表沉默倾听的“虚拟鸭子”。“拿着鸭子”这个短语变成了听者保持沉默，让说话者大声解决问题的信号。

作者承认这个术语在皮克斯的一个小团队中，特别是 TS2 FX 团队中的特定用途，然后传播到皮克斯的其他团队，并可能传播到其他动画工作室，如梦工厂。作者希望这篇文章能为那些熟悉这个短语的人提供一个参考点，并欢迎任何可以将这个故事追溯到其潜在的 Xerox PARC 起源的信息。

---

## 7. 布

**原文标题**: Cloth

**原文链接**: [https://www.cloudofoz.com/verlet-test/](https://www.cloudofoz.com/verlet-test/)

文章“布料”，作者@cloudofoz，是对Verlet积分进行布料模拟的测试。内容明确声明了其目的，即演示和实验Verlet积分在布料模拟中的应用。因此，文章很可能包含视觉示例、代码片段或基于Verlet的布料模拟的实现描述。

---

## 8. 订购放射性物质的澳大利亚人离开法庭

**原文标题**: Australian who ordered radioactive materials walks away from court

**原文链接**: [https://www.chemistryworld.com/news/australian-who-ordered-radioactive-materials-over-the-internet-walks-away-from-court/4021306.article](https://www.chemistryworld.com/news/australian-who-ordered-radioactive-materials-over-the-internet-walks-away-from-court/4021306.article)

24岁澳洲男子Emmanuel Lidden非法进口和持有铀、钚等放射性物质，认罪后免于入狱。Lidden意图收集元素周期表，因评估出的精神健康问题和缺乏恶意，获判两年良好行为保证。

2023年8月，他在其父母公寓中被澳大利亚边防部队发现这些物质后，其行为引发了一起重大危险品事故，导致街道关闭和人员疏散。他是澳大利亚首位因该类罪行根据核不扩散法被判刑的人。

虽然Lidden对判决表示欣慰，但他的律师批评边防部队反应过度，声称这些物质的量非常小，不会造成危险。他补充说，他收到了来自世界各地科学家的类似观点。Lidden公开从美国在线订购这些材料，并将它们展示在自己的卧室里。澳大利亚边防部队警司James Ryan希望该案件能提高人们对进口法规的认识。

---

## 9. 美国移民与海关执法局驱逐3名遭隔离的美籍公民子女

**原文标题**: ICE Deports 3 U.S. Citizen Children Held Incommunicado Prior to the Deportation

**原文链接**: [https://www.aclu.org/press-releases/ice-deports-3-u-s-citizen-children-held-incommunicado-prior-to-the-deportation](https://www.aclu.org/press-releases/ice-deports-3-u-s-citizen-children-held-incommunicado-prior-to-the-deportation)

美国公民自由联盟新闻稿称，移民及海关执法局在新奥尔良驱逐了两户家庭，其中包括三名美国公民儿童，情况令人不安，引发了对正当程序的担忧。据称，这些在美国生活多年的家庭被隔离，律师和家人无法联系到他们，从而无法获得法律咨询，也无法为孩子们做出妥善的照顾安排。

美国公民自由联盟认为，这些行为违反了移民及海关执法局关于照顾未成年子女的指令。一个家庭的仍在等待裁决的人身保护令申请由于迅速驱逐而被搁置。在另一个案件中，一名患有癌症的美国公民儿童在未带药物且未与医生协商的情况下被驱逐出境，尽管移民及海关执法局已知晓他们的医疗需求。一名孕妇也被驱逐出境，未确保持续的产前护理。

多个组织谴责了这些驱逐行为，称其为不人道、非法，并违反了正当程序和基本人权。他们批评移民及海关执法局拒绝提供法律和医疗途径，无视相关规定，并规避法院干预。倡导者要求追究相关责任人的责任，并呼吁让这些家庭返回。他们强调了驱逐美国公民儿童的非法性，并对政府日益严厉的移民政策表示担忧。

---

## 10. 我写了一本书，叫《垃圾城镇》。当时觉得挺好笑的。

**原文标题**: I wrote a book called "Crap Towns". It seemed funny at the time

**原文链接**: [https://samj.substack.com/p/that-joke-isnt-funny-any-more](https://samj.substack.com/p/that-joke-isnt-funny-any-more)

无法访问文章链接。

---

## 11. 友谊衰退：失落的联结艺术

**原文标题**: The Friendship Recession: The Lost Art of Connecting

**原文链接**: [https://www.happiness.hks.harvard.edu/february-2025-issue/the-friendship-recession-the-lost-art-of-connecting](https://www.happiness.hks.harvard.edu/february-2025-issue/the-friendship-recession-the-lost-art-of-connecting)

布莱斯·富梅勒的文章《友谊衰退：失落的连接艺术》探讨了美国亲密友谊令人担忧的衰退。该文章指出，数据显示拥有亲密朋友的美国人数量急剧下降，并将此归因于郊区扩张、公共空间减少和经济压力等系统性力量。然而，文章认为更深层次的文化转变也在起作用。

作者认为，工作日益成为主要的社会身份，导致工作时间延长，个人关系时间减少。对核心家庭，尤其是“密集育儿”的日益关注，也助长了这一现象，将孩子的成就置于成人友谊之上。屏幕时间和纯数字化友谊的兴起进一步加剧了这个问题，因为在线互动缺乏面对面连接的深度和神经益处。

这种转变被描述为危险的，因为它重塑了大脑，使脆弱性（建立友谊所必需的）更难以忍受，并导致社会孤立和对社会互动的负面解读。文章强调了一种自我强化的循环，即从面对面连接中退却会使其更加困难。

作者建议通过加强友谊的形成和维持来对抗“友谊衰退”，并倡导结构性和个人层面的改变。建立友谊的关键之一是通过新奇的体验和共同的挑战来拥抱不适。作者分享了自己参与“辣鸡翅挑战”等活动的个人经历来例证这一点。最后，他提出了创造此类体验的建议。

---

## 12. 伯克利人形机器人精简版 – 开源机器人

**原文标题**: Berkeley Humanoid Lite – Open-source robot

**原文链接**: [https://lite.berkeley-humanoid.org/](https://lite.berkeley-humanoid.org/)

伯克利人形机器人Lite项目旨在通过引入开源、经济实惠的人形机器人设计，解决人形机器人高成本和可及性有限的问题。该机器人以可及性、定制化和社区利益为优先。其主要特点包括：

*   **低成本和可及性：** 利用3D打印模块化齿轮箱和易于获取的电商组件，将总硬件成本控制在5,000美元以下。
*   **模块化和易于制造：** 设计易于使用标准桌面3D打印机进行组装和修改。
*   **耐用设计：** 在3D打印的执行器中使用摆线齿轮设计，以克服塑料部件的局限性，并通过广泛的测试验证其耐用性。
*   **开源：** 所有硬件设计、嵌入式代码和培训/部署框架都是完全开源且全球可访问的。
*   **已展示的能力：** 包括成功实施的使用强化学习开发的运动控制器，展示了从仿真到硬件的零样本策略迁移。

该项目旨在通过为更广泛的机器人社区提供研究、实验和创新的平台，实现人形机器人开发的民主化。

---

## 13. 使用ASKAP发现15个新的巨型射电星系

**原文标题**: Fifteen new giant radio galaxies discovered with ASKAP

**原文链接**: [https://phys.org/news/2025-04-fifteen-giant-radio-galaxies-askap.html](https://phys.org/news/2025-04-fifteen-giant-radio-galaxies-askap.html)

天文学家利用澳大利亚平方公里阵列探路者（ASKAP）发现了15个新的巨型射电星系（GRG），它们的物理尺寸超过300万光年。这些GRG在arXiv上发表的一篇研究论文中进行了报告，它们是罕见的天体，其特征是同步加速辐射等离子体的喷流和瓣状结构，对于研究射电源的形成和演化具有重要价值。

ASKAP凭借其高巡天速度和灵敏度，能够在944 MHz的广域观测中探测到这些GRG。新发现的GRG尺寸范围从370万到1236万光年不等，红移范围在0.056到0.735之间。其中两个被归类为候选GRG，等待进一步确认。

这些GRG表现出多种形态。八个是Fanaroff-Riley II型（FR II）星系，以突出的射电热点为特征，而四个是Fanaroff-Riley I型（FR I）星系，具有明亮的内部喷流和逐渐消失的外部瓣状结构。其余三个似乎是中间型或混合型。最大的GRG，ASKAP J0107–2347，是一个双-双射电星系（DDRG），具有新形成的跨度约200万光年的内部瓣状结构和细长的低表面亮度外部瓣状结构。

---

## 14. 写入"/etc/hosts"会破坏Substack编辑器

**原文标题**: Writing "/etc/hosts" breaks the Substack editor

**原文链接**: [https://scalewithlee.substack.com/p/when-etchsts-breaks-your-substack](https://scalewithlee.substack.com/p/when-etchsts-breaks-your-substack)

Lee的文章《修改“/etc/hosts”文件导致Substack编辑器崩溃》揭示了“/etc/hosts”文件与Substack编辑器之间一种奇怪的交互。作者发现，在他们的“/etc/hosts”文件中添加特定行会导致Substack编辑器发生故障，阻止他们发布文章。

有问题的行是与阻止广告或跟踪域名相关的重定向。虽然作者没有明确指出具体的行，但暗示它将Substack用于基本编辑器功能的域名（例如，加载脚本、图像或处理文章预览）重定向到localhost (127.0.0.1) 或另一个无效的IP地址。

这种重定向有效地阻止了Substack编辑器访问必要的资源，导致编辑器错误和发布失败。删除或注释掉“/etc/hosts”文件中存在问题的行会立即解决该问题。

作者的结论是提醒人们注意修改诸如“/etc/hosts”之类的系统文件的潜在后果，尤其是在阻止域名时，因为这些更改可能会无意中干扰看似无关的应用程序和服务。虽然“/etc/hosts”文件是一个强大的工具，但它需要仔细考虑和理解被阻止的域名，以避免意外的副作用。作者总结说，使用浏览器扩展程序或专用广告拦截器可能比直接编辑“/etc/hosts”文件更安全。

---

## 15. 用于高效GPU推理的动态长度浮点无损LLM压缩

**原文标题**: Lossless LLM compression for efficient GPU inference via dynamic-length float

**原文链接**: [https://arxiv.org/abs/2504.11651](https://arxiv.org/abs/2504.11651)

本文介绍了一种名为动态长度浮点数（DFloat11）的新型无损压缩框架，旨在减小大型语言模型（LLM）的尺寸，以实现更高效的GPU推理。其核心思想是利用LLM的BFloat16权重表示中观察到的低熵特性。DFloat11使用熵编码，根据权重的频率为其分配动态长度的编码，在不损失任何精度的情况下，实现了30%的模型尺寸缩减，从而产生与原始模型逐位相符的输出。

为了能够使用压缩模型进行高效推理，作者开发了一个定制的GPU内核，该内核针对快速在线解压缩进行了优化。该内核具有以下特点：（i）将内存密集型查找表分解为更小的、与GPU SRAM兼容的版本；（ii）用于协调线程读/写位置的两阶段执行；以及（iii）用于最大限度减少延迟的Transformer块级解压缩。

在Llama-3.1、Qwen-2.5和Gemma-3等模型上的实验结果表明，DFloat11在实现约30%的模型尺寸缩减的同时，保持了完美的精度。与因内存限制而将部分未压缩模型卸载到CPU相比，DFloat11实现了显著更高的token生成吞吐量（1.9-38.8倍）。在固定的GPU内存预算下，与未压缩模型相比，DFloat11允许5.3-13.17倍的更长上下文长度。一个关键亮点是展示了使用DFloat11在具有8x80GB GPU的单节点上对大规模Llama-3.1-405B模型进行无损推理。代码和模型已公开提供。

---

## 16. 华盛顿特区美国检察官质疑维基百科的非营利地位

**原文标题**: Wikipedia’s nonprofit status questioned by D.C. U.S. attorney

**原文链接**: [https://www.washingtonpost.com/technology/2025/04/25/wikipedia-nonprofit-ed-martin-letter/](https://www.washingtonpost.com/technology/2025/04/25/wikipedia-nonprofit-ed-martin-letter/)

无法访问文章链接。

---

## 17. Mobygratis – 免费Moby音乐，助力您的创意项目

**原文标题**: Mobygratis – Free Moby music to empower your creative projects

**原文链接**: [https://mobygratis.com/](https://mobygratis.com/)

Mobygratis是由Moby创建的平台，旨在为各种创作者（电影制作人、音乐家、学生等）提供免费的器乐音乐。该平台提供包含500首曲目的广泛目录，有三种格式可供选择：立体声MP3、立体声WAV和多轨WAV，全部免费。Moby鼓励创作者在其项目中使用这些音乐，并表示非常期待看到由此产生的作品。他建议有疑问的用户查阅常见问题解答，并重申了简单的前提：免费音乐，用于创意用途。该目录最后更新于2025年4月26日。

---

## 18. 通过神经网络进行世界模拟

**原文标题**: World Emulation via Neural Network

**原文链接**: [https://madebyoll.in/posts/world_emulation_via_dnn/](https://madebyoll.in/posts/world_emulation_via_dnn/)

本文详细介绍了作者创建一个可在网页浏览器中访问的可玩“神经世界”森林小径项目的过程。与手动构建环境的传统游戏开发不同，这个神经世界是由一个神经网络生成的，该网络基于在真实森林中记录的视频和运动数据进行训练。该网络学会根据先前的帧和用户控制来预测后续帧，从而有效地模拟环境。

作者概述了创建令人信服的神经世界所面临的挑战，最初遇到了诸如“汤化”之类的问题，即网络无法准确预测和生成细节。为了解决这个问题，作者通过添加更多的控制信息，增加内存容量以及跨多个尺度处理数据来迭代改进训练过程。进一步的改进包括增加网络规模，完善训练目标以及延长训练时间。

最终结果是一个低分辨率但可供探索的森林小径表示。作者强调了传统游戏世界（类似于绘画）和神经世界（类似于照片）之间的根本区别。神经世界提供了捕获和复制真实世界环境的潜力，而无需手动艺术创作，而是依赖于数据和技术进步。作者设想未来创建逼真且可组合的神经世界就像拍照一样简单方便，从而为叙事安排开辟新的创意媒介。

---

## 19. 并行 ./configure

**原文标题**: Parallel ./configure

**原文链接**: [https://tavianator.com/2025/configure.html](https://tavianator.com/2025/configure.html)

2025年了，作者Tavian Barnes 以幽默的口吻抱怨 `./configure` 脚本执行速度依然缓慢。他展示了一段典型的 `./configure` 运行的冗长输出，凸显了为确定系统能力和配置而执行的大量检查。文章强调了这些检查固有的串行性质，它们依次探测各种系统头文件、函数和功能的可用性。Barnes 对此表示沮丧，尽管处理器技术和并行计算取得了进步，但这个严重依赖于耗时的单个检查的过程仍然是软件编译的瓶颈。核心观点是，鉴于计算机科学的现状，到 2025 年，软件配置应该有一种更有效和并行化的方法。

---

## 20. Backblaze：亏损扩大、诉讼缠身、虚假账目、内部抛售

**原文标题**: Backblaze: Mounting Losses, Lawsuits, Sham Accounting, Insider Selling

**原文链接**: [https://www.morpheus-research.com/backblaze/](https://www.morpheus-research.com/backblaze/)

对Backblaze (BLZE)的看跌论证：财务管理不善、内幕交易和可疑会计行为
关键指控包括：
* 亏损和稀释：自首次公开募股以来，Backblaze每季度都报告亏损，流通股增加80%。
* 诉讼：两位前高级员工（投资者关系副总裁和FP&A高级主管）提起诉讼，指控会计欺诈、夸大预测和举报人报复。
* 内幕交易：据称，创始人虽收到顾问关于对股价产生负面影响的警告，但在首次公开募股锁定期结束后立即进行了激进的股票抛售。
* 可疑的财务报告：指控向审计师提供不准确的财务报表和夸大的现金流预测。
* 高管离职：多位高级领导离职，据称试图掩盖其股票出售行为。
* CFO任命：任命一位来自陷入困境的多层次营销公司的新CFO引起担忧。
* 市场竞争：Backblaze在与AI相关的云存储市场中正输给Wasabi等竞争对手。
* 会计伎俩：文章强调，Backblaze资本化了大量的软件成本，远高于其SaaS同行的平均水平。它改变了“调整后自由现金流”的定义，以排除诉讼和重组成本。

文章的结论是，Backblaze是一家失败的增长型企业，据称通过财务操纵来使内部人士受益。作者建议做空BLZE股票。

---

## 21. NNCPNET电子邮件网络

**原文标题**: The NNCPNET Email Network

**原文链接**: [https://changelog.complete.org/archives/10768-announcing-the-nncpnet-email-network](https://changelog.complete.org/archives/10768-announcing-the-nncpnet-email-network)

作者描述了运行个人邮件服务器的日益增长的复杂性所带来的挫败感，这源于诸如SPF、DKIM、DMARC和TLS等要求。这促使了NNCPNET的创建，这是一个基于NNCP（NNCP是UUCP的现代安全替代品）构建的邮件系统。

NNCPNET旨在重新找回旧式邮件系统的乐趣和可定制性。它利用NNCP的异步、洋葱路由、存储转发网络，允许通过各种方法进行传输，包括互联网甚至USB驱动器。

NNCPNET提供了一个“简易模式”Docker容器，其中包括Exim、NNCP和自定义路由工具。该系统通过NNCP的加密和签名提供“免费”的发件人验证，并包含自动节点列表更新。它还提供可选的互联网邮件桥接，完全支持SPF、DKIM、DMARC和TLS。

主要优点包括不需要入站端口、持续的互联网连接，甚至不需要任何互联网连接。它可以在笔记本电脑上运行，并通过IMAP服务器与Thunderbird集成。该项目向所有人开放，提供广泛的文档、邮件列表和随时可用的源代码。最终，NNCPNET提供了一种在现代互联网电子邮件服务日益严格的约束之外尝试电子邮件的方式。

---

## 22. Eurorack旋钮创意

**原文标题**: Eurorack Knob Idea

**原文链接**: [https://mitxela.com/projects/euroknob](https://mitxela.com/projects/euroknob)

本文详细介绍了“Eurorack旋钮创意”，该概念旨在用一种混合旋钮/跳线替换标准的Eurorack旋钮，该混合旋钮/跳线利用包含小型磁铁的3.5mm TRS插头，该磁铁与位于模块面板上相应插孔下方的磁编码器（AS5600）相互作用。编码器读取磁铁的位置并将其转换为电压或数字信号，从而模仿电位计的功能。

作者构建了一个原型，证明了该概念的可行性。TRS插头端经过修改以容纳小型钕磁铁，并且设计了一个定制PCB以容纳TRS插座和AS5600编码器。一个微控制器（CH32V003）通过I2C读取编码器数据并控制LED以可视化该值。该原型成功检测到磁性旋钮的存在并读取其旋转角度。

虽然原型是成功的，但作者承认了广泛采用的潜在局限性。需要专用旋钮和专用电路使得很难与现有模块或其他制造商的设计集成。一种更具商业可行性的替代方案可能是带有同轴TRS插孔的标准电位计。尽管存在实际挑战，但作者设想了一个致力于这种创新方法的利基社区（“Euroknobists”）。作者表示有兴趣进行合作和获得资金，以进一步探索这一概念。所有硬件和软件设计均可在GitHub和git.mitxela.com上找到。

---

## 23. Show HN: 我用OpenAI的新图像API做了一个个性化涂色书服务

**原文标题**: Show HN: I used OpenAI's new image API for a personalized coloring book service

**原文链接**: [https://clevercoloringbook.com/](https://clevercoloringbook.com/)

展示：Clever Coloring Book——利用OpenAI图像API将照片转化为个性化涂色书的服务。用户可上传8-24张照片，生成涂色页。提供两种选择：11.99美元的电子版下载，供用户在家打印；以及23.99美元加运费的实体装订版涂色书。实体版提供两种纸张选择：较薄的哑光纸（适用于蜡笔和铅笔）和较厚的微光纸（适用于马克笔）。该服务强调无屏幕时间和制作难忘的礼物。帖子包含带有拖放上传功能的行动号召，并告知用户照片必须遵守OpenAI的使用政策。最后，帖子包含关于自动创建帐户的信息以及服务条款和隐私政策的链接。

---

## 24. 展示HN：用Lean形式化《数学原理》

**原文标题**: Show HN: Formalizing Principia Mathematica using Lean

**原文链接**: [https://github.com/ndrwnaguib/principia](https://github.com/ndrwnaguib/principia)

此“Show HN”帖子描述了一个使用Lean 4定理证明器形式化罗素《数学原理》第一卷的项目。 主要目标是创建一个忠实的形式化，紧密遵循罗素的原始证明和符号，尽量减少添加或偏差。 作者强调了《数学原理》符号的复杂性，并通过提供可与原文对比的清晰示例，力求使形式化易于理解。

作者承认Coq中已存在对《数学原理》的形式化，特别是Elkind教授的版本，但作为个人学习经验，选择在Lean 4中进行此项目。 一个关键特性是使用元编程来复制罗素的符号，特别是使用“*1.11”来表示推论。 例如，该帖子展示了*2.16的形式化，包括一个名为“Syll”的自定义策略，旨在模仿罗素的三段论符号。

作者强调严格遵守罗素的原始证明，并欢迎对任何不准确之处提出反馈。 虽然该项目的实际应用有限，但作者认为它是一次理解数学基础以及从基本原理构建数学系统的过程的宝贵实践。 文章最后提出了一个潜在的未来项目：形式化阿尔弗雷德·塔斯基的《逻辑、语义学和元数学》。

---

## 25. 可重复性项目未能验证数十项生物医学研究

**原文标题**: Reproducibility project fails to validate dozens of biomedical studies

**原文链接**: [https://www.nature.com/articles/d41586-025-01266-x](https://www.nature.com/articles/d41586-025-01266-x)

一项大型可重复性项目——巴西可重复性倡议，涉及超过50个研究团队，试图重复巴西生物医学研究的发现，这些研究依赖于三种常见的研究方法：细胞代谢分析、遗传物质扩增和啮齿动物迷宫测试。结果以预印本的形式发布在bioRxiv上，令人沮丧，只有不到一半的测试实验成功重复。

该倡议审查了生命科学文章的随机样本，以确定巴西最常用的生物医学研究方法。他们专注于1998年至2017年间发表的论文，其中至少一半的贡献者隶属于巴西机构。在最初的60篇论文子集中，每个实验由三个不同的实验室进行了97次有效的重复尝试，涉及47个实验。

可重复性由五个标准判断，包括至少一半的重复尝试中存在与原始论文相同方向的统计显著结果。只有21%的实验符合这一标准。该研究还显示，与重复尝试相比，原始论文中的效应量平均大了60%，这表明已发表的结果倾向于高估效应。

作者希望这项研究能够通过政策改革和大学倡议促进巴西科学的进步。尽管在COVID-19大流行期间面临后勤挑战以及团队之间存在分歧，该项目为解决可重复性问题提供了有价值的数据。

---

## 26. 你的手机并没有在偷偷监听你，但真相更令人不安。

**原文标题**: Your phone isn't secretly listening to you, but the truth is more disturbing

**原文链接**: [https://newatlas.com/computers/smartphone-listening-conversations-ads-facebook/](https://newatlas.com/computers/smartphone-listening-conversations-ads-facebook/)

本文旨在揭穿一种常见的阴谋论，即智能手机持续监听对话以投放定向广告。文章承认某些广告的惊人准确性，但同时也提出了证据和论点，驳斥了“麦克风始终开启”的说法。

Wandera 在 2019 年进行的实验表明，持续录音会导致数据消耗显著增加，而实际情况并非如此。文章还指出，存储和处理持续监听产生的大量音频数据是不切实际的。

文章强调，Facebook 确实曾与一家公司签订合同来转录音频对话，但仅限于在用户同意的情况下，目的是改进其转录算法，而非用于广告定向。

文章没有支持持续的麦克风监视，而是提出了一个更复杂和令人不安的真相：公司通过大量的各种数据点跟踪用户，包括位置、社交关系、浏览历史、应用程序使用情况，甚至屏幕截图。这些数据被输入算法，算法可以惊人地准确预测用户的兴趣和需求，从而产生那些令人毛骨悚然的相关广告。文章还提到了 Cox Media Group 已停止使用的“主动监听”系统，据称该系统使用来自语音助手命令的语音数据来定制广告，尽管主要科技公司与该系统保持了距离。

文章总结道，虽然语音激活设备在触发短语后会短暂录制音频，但真正令人担忧的是那些不透明且功能强大的算法，它们分析大量的个人数据来预测我们的需求并为我们提供定向广告。

---

## 27. 避免人工智能时代技能退化

**原文标题**: Avoiding skill atrophy in the age of AI

**原文链接**: [https://addyo.substack.com/p/avoiding-skill-atrophy-in-the-age](https://addyo.substack.com/p/avoiding-skill-atrophy-in-the-age)

无法访问文章链接。

---

## 28. 一款2万美元美国制造的无漆、无音响、无屏幕电动皮卡

**原文标题**: A $20k American-made electric pickup with no paint, no stereo, no screen

**原文链接**: [https://www.theverge.com/electric-cars/655527/slate-electric-truck-price-paint-radio-bezos](https://www.theverge.com/electric-cars/655527/slate-electric-truck-price-paint-radio-bezos)

Slate Auto 将推出 Slate Truck，这是一款为经济性和定制化而设计的、美国制造的极简电动皮卡。该双座卡车的目标价格低于 2 万美元（扣除补贴后），续航里程为 150 英里，并采用极简设计，没有油漆、立体声音响和触摸屏。

卡车的车身面板由注塑聚丙烯制成，强调耐用性和抗刮擦性。Slate 提倡“战斗伤痕”美学，鼓励车主通过乙烯基贴膜和 DIY 改装来实现个性化，甚至提供 SUV 升级套件，以增加座椅和翻滚保护。

为了实现低价，Slate 彻底简化了制造流程。通过取消喷漆车间并专注于单一配置，他们降低了成本和复杂性。该车辆在美国设计和制造，并主要采用美国供应链。

虽然缺乏现代化的信息娱乐系统，但 Slate 鼓励用户“自带设备”，并提供简单的安装解决方案。该公司还提倡 DIY 维护，通过“Slate 大学”和与全国服务中心的合作提供在线支持。

销售将采用直销模式，类似于特斯拉，提供有限的提货中心和送货上门选项。尽管进行了极度简化，但 Slate 旨在获得高安全评级。该公司的做法吸引了包括据报道的杰夫·贝索斯在内的主要投资者，因为它呈现了一种精益的商业模式。Slate Truck 挑战了当前昂贵且功能过多的车辆趋势，并质疑消费者是否准备好在车轮上进行“数字排毒”。

---

## 29. 灾难性火灾和土壤退化：可能与新石器时代革命有关

**原文标题**: Catastrophic fires and soil degradation: possible link with Neolithic revolution

**原文链接**: [https://link.springer.com/article/10.1007/s11368-025-04021-x](https://link.springer.com/article/10.1007/s11368-025-04021-x)

本文探讨了黎凡特南部灾难性火灾与土壤退化和新石器时代革命爆发之间潜在的联系。它挑战了人类活动引起的燃烧是这一时期的主要驱动因素的假设，而是提出气候驱动的闪电袭击增加导致了广泛的火灾和环境恶化。

该研究分析了包括胡拉湖的微炭、石笋中的碳和锶同位素、土壤的光释光年龄以及死海海平面波动等各种记录。这些记录表明，全新世早期，大约在8-8.6千年前，存在一个强烈的火灾活动时期，与新石器时代同时发生。

作者认为，与轨道强迫控制的高太阳辐射相关的闪电强度增加导致了植被和土壤流失。低锶同位素比率的脉冲支持了土壤侵蚀和在山谷中重新沉积的观点，而新石器时代的聚落就集中在这些山谷中。这种环境压力，加上与8.2千年前事件相关的干旱时期，可能放大了灾难性的影响。

文章最后认为，气候变化和强烈的火灾环境造成的严重环境恶化，可能在新石器时代革命期间，在促使前所未有的人类行为（如农业和驯化）方面发挥了重要作用。本质上，环境灾难可能催化了向农业的转变。

---

## 30. 阅读RSS内容是一项技巧性活动。

**原文标题**: Reading RSS content is a skilled activity

**原文链接**: [https://www.doliver.org/articles/rss-as-a-skill](https://www.doliver.org/articles/rss-as-a-skill)

该文章认为，由算法和广告驱动的现代互联网已损害了用户的注意力和体验。作者提出使用RSS作为一种解决方案，以重新掌控个人对信息的消费。然而，他们也承认通过RSS获取的大量内容此前阻碍了其普及。

关键在于，使用RSS阅读器应该是一种与传统社交媒体截然不同的体验。用户不再受算法的内容摆布，而是积极地策划自己的订阅源。这种策划是通过一种“信任链”的方式实现的，即用户订阅那些他们信任其判断力的个人的订阅源，然后关注这些个人信任的来源的订阅源。

作者强调，价值不仅在于信息的准确性，还在于内容是否值得关注。构建有效的RSS订阅源需要积极和有意识的策划，就像维护一个花园一样，定期修剪和清除无关或低价值的内容。最终，作者认为使用RSS阅读器是一种技能，可以培养与信息之间更投入和更有意识的关系，从而使用户能够重新掌控自己的注意力。

---

## 31. 真实大小

**原文标题**: The True Size Of

**原文链接**: [https://thetruesize.com/](https://thetruesize.com/)

网站“真实大小...”是一个交互式地图工具，旨在纠正由地图投影，特别是墨卡托投影引起的常见地图变形误解。虽然该投影因其精确的角度而有利于导航，但它会显著扭曲陆地面积的大小，特别是那些远离赤道的陆地面积。

该工具允许用户搜索国家或地区，然后将其拖动到地图上。当用户移动所选区域时，该工具会调整该区域的大小，以反映其在相应纬度上的*真实*比例大小。这直观地展示了标准地图上国家和大陆的大小通常被误导的程度。

“真实大小...”的核心目的是教育用户了解地图投影中固有的不准确性，并提供对不同地理区域相对大小的更真实理解。它允许用户直接比较各个国家和地区的大小，例如，揭示加拿大或俄罗斯与赤道附近的国家相比，比墨卡托投影地图上通常所见的要大多少。对于地理爱好者、教育工作者以及任何对更准确的世界地图感兴趣的人来说，它都是一个宝贵的资源。

---

## 32. GCC 15.1

**原文标题**: GCC 15.1

**原文链接**: [https://gcc.gnu.org/gcc-15/](https://gcc.gnu.org/gcc-15/)

GCC 15.1于2025年4月25日发布，标志着GNU编译器套件的一次重大更新。此版本包含相比GCC 14.x系列的新特性和改进。公告感谢了众多志愿者的贡献，他们提供了功能、漏洞修复和测试结果，突出了他们在GCC成功中所起到的关键作用。

该文档提供了通过镜像站点或版本控制系统获取GCC的资源，以及查找与使用编译器相关的帮助和文档的信息。它建议首先查阅GCC项目网站和手册，然后在必要时使用gcc-help邮件列表。

鼓励对网页和GCC开发的反馈，可以将其发送到开发者邮件列表。文章最后是自由软件基金会的版权声明，允许逐字复制和分发。它还表明GCC团队维护这些页面，最后修改日期是发布日期本身。

---

## 33. 巨洞冒险 (1976)

**原文标题**: Colossal Cave Adventure (1976)

**原文链接**: [https://github.com/wh0am1-dev/adventure](https://github.com/wh0am1-dev/adventure)

本仓库包含巨洞冒险（1976）的原始Fortran源代码，这款开创性的文字冒险游戏被认为是电子游戏史上同类游戏的首款。受电视剧《奔腾年代》的启发，本仓库创建者从互联网上找到了源代码并编译了补充材料，包括地图、攻略以及Windows和Mac OS的可执行版本。本仓库的目的纯粹是教育性的。

---

## 34. 迈克·林德尔的律师用人工智能撰写诉状——法官发现近30处错误

**原文标题**: Mike Lindell's lawyers used AI to write brief–judge finds nearly 30 mistakes

**原文链接**: [https://arstechnica.com/tech-policy/2025/04/mypillow-ceos-lawyers-used-ai-in-brief-citing-fictional-cases-judge-says/](https://arstechnica.com/tech-policy/2025/04/mypillow-ceos-lawyers-used-ai-in-brief-citing-fictional-cases-judge-says/)

联邦法官已下令迈克·林德尔的律师克里斯托弗·卡丘罗夫和詹妮弗·德马斯特解释，为何他们不应因在一诽谤案中提交一份因使用人工智能而错误百出的简报而受到制裁。这份针对埃里克·库默动议的简报包含近30处引文缺陷，包括错误引用、虚构案例以及对法律原则的歪曲。

首席律师克里斯托弗·卡丘罗夫承认使用人工智能撰写了这份简报，但未能充分核实引文。鉴于错误的广泛性，法官尼娜·王对卡丘罗夫声称他在使用人工智能之前亲自概述并撰写了草稿的说法表示怀疑。卡丘罗夫甚至将肯塔基州的案件归于科罗拉多州法院，并惊讶地得知一个引用的案例并不存在。

法官已命令卡丘罗夫和德马斯特宣誓解释该简报的准备情况，包括林德尔和MyPillow是否批准使用人工智能。他们还必须说明为何他们不应面临纪律处分。

这场诽谤案源于林德尔及其公司虚假声称，前Dominion Voting Systems员工库默犯有叛国罪并操纵了2020年大选。库默的诉讼称，林德尔及其媒体利用这些虚假陈述来诽谤他并推广MyPillow产品。这份有问题的简报试图引入可能对库默个人生活造成损害的证据，库默试图将这些证据排除在审判之外。

---

## 35. Curry：一种函数式逻辑编程语言

**原文标题**: Curry: A functional logic programming language

**原文链接**: [https://curry-lang.org/](https://curry-lang.org/)

Curry是一种声明式多范式编程语言，无缝集成了函数式和逻辑编程的特性。它结合了这两种范式的优点，提供了函数式编程的嵌套表达式、高阶函数、强类型、惰性求值，以及逻辑编程的非确定性、内置搜索、自由变量和部分数据结构。Curry进一步增强了这些范式，例如针对面向逻辑的计算进行优化求值以及灵活的模式匹配。

其关键特性包括纯声明式编程（结果与求值顺序无关）、类型推断、非确定性（允许同一输入有多个结果）和自由变量（表示在求值期间实例化的未知值）。

Curry旨在成为集成函数式逻辑语言研究、教学和应用的通用平台。目前有PAKCS、KiCS2和MCC等多种实现。Curry生态系统包括用于管理库的Curry包管理器（CPM）、用于生成程序文档的CurryDoc以及Curry API搜索引擎Curr(y)gle。语言报告、教程和邮件列表等资源可用于学习和社区参与。

---

## 36. Show HN：空回车扩展器 – 用这款工具减少终端输入

**原文标题**: Show HN: Empty Enter Expander – Type less in the terminal with this tool

**原文链接**: [https://github.com/waszabi/empty-enter-expander](https://github.com/waszabi/empty-enter-expander)

空行回车扩展器是一个zsh工具，允许你通过快捷方式以更少的按键执行命令。它的工作原理是在你于空命令行中按下回车键时激活，然后允许你使用快捷方式插入命令。

命令存储在一个具有特定文件/文件夹结构的模块目录中。该目录包含文件和文件夹，其中文件/文件夹名称的首字母小写字母充当命令快捷方式。例如，位于 `~/Tools/expander-example-module/g Git/l Log` 中的脚本可以通过 "g"、"l" 键，然后按回车键来访问。

要使用该工具，你需要克隆项目并进行配置。具体来说，你需要在你的 `.zprofile` 文件中设置 `EMPTY_ENTER_EXPANDER_MODULE_PATH` 环境变量以指向你的模块目录，并加载提供的 zsh 函数。你还需要将回车键绑定到 `empty-enter-expander` 函数。

配置完成后，打开一个新的 shell，在空行上按回车键即可激活扩展器。它会显示模块目录中的命令。然后你输入相应的快捷方式并再次按回车键，将命令插入到提示符中以供执行。该工具会忽略历史记录中的空格。

---

## 37. Show HN: Magnitude – 面向Web应用、AI原生开源测试框架

**原文标题**: Show HN: Magnitude – open-source, AI-native test framework for web apps

**原文链接**: [https://github.com/magnitudedev/magnitude](https://github.com/magnitudedev/magnitude)

Magnitude：利用视觉AI代理的Web应用开源AI原生测试框架，通过自然语言构建测试用例，简化测试流程。

其工作原理是：推理代理计划并调整测试，视觉代理可靠地执行测试。如果在测试执行过程中出现问题，推理代理会介入。测试可以在本地或CI/CD管道中运行。

设置包括通过npm安装`magnitude-test`包，并使用`npx magnitude init`初始化项目。配置需要设置两个LLM客户端：一个用于计划的强大的多模态LLM（例如，Gemini）和一个用于执行的快速视觉LLM（Moondream）。这些服务的API密钥需要通过环境变量配置（例如，`GOOGLE_API_KEY`，`MOONDREAM_API_KEY`）。

测试用例使用简单的语法构建：定义步骤，提供数据，并指定检查，所有这些都使用自然语言。

与通用AI任务执行API（如OpenAI Operator或Claude Computer Use）相比，该框架旨在实现高效测试，提供速度、可靠性和成本效益。团队鼓励用户联系他们进行演示或加入他们的Discord社区。

---

## 38. 信号门教训：如果目标是安全文化，美国就完蛋了。

**原文标题**: Signalgate lessons: If the goal is a culture of security, America's screwed

**原文链接**: [https://www.theregister.com/2025/04/25/signalgate_lessons_learned_if_creating/](https://www.theregister.com/2025/04/25/signalgate_lessons_learned_if_creating/)

“信号门”教训：如果目标是安全文化，美国完蛋了
这篇文章详细描述了多起美国官员（包括国防部长皮特·黑格塞斯和国家安全顾问迈克尔·沃尔茨）使用不安全通信渠道传输敏感信息的事件。这些事件涉及使用个人设备、Signal和Gmail等商业应用程序以及不安全的互联网连接来讨论军事行动和共享机密信息。

文章强调了这些做法相关的安全风险，包括外国对手的潜在监视和数据泄露，以及设备可能被入侵。专家强调，安全政府网络的存在是有原因的，绕过它们会使敏感情报面临风险，尤其是在中国等国家持续进行网络威胁的情况下。

作者批评了特朗普政府内部缺乏“安全文化”，领导人未能优先考虑数据隐私和安全通信。文章还指出，该政府决定在对中国黑客进行调查期间清除网络安全审查委员会，阻碍了从过去的安全漏洞中吸取教训的努力。

文章最后总结说，这些安全漏洞创造了一种“内部威胁”，并为对手提供了利用美国情报的机会。尽管有人试图淡化这些事件，但作者暗示外国实体正在积极监控这些漏洞。

---

## 39. Paper2Code：从科学论文自动生成代码

**原文标题**: Paper2Code: Automating Code Generation from Scientific Papers

**原文链接**: [https://arxiv.org/abs/2504.17192](https://arxiv.org/abs/2504.17192)

Paper2Code：从机器学习科学论文中自动生成代码

这篇题为“Paper2Code：从机器学习科学论文中自动生成代码”的arXiv文章介绍了PaperCoder，一个多代理LLM框架，旨在从机器学习论文中自动生成功能性代码仓库。该论文由Minju Seo、Jinheon Baek、Seongyun Lee和Sung Ju Hwang撰写，解决了代码实现缺失或不可用的常见问题，这些问题阻碍了研究的可重复性和进步。

PaperCoder分三个阶段运行：规划、分析和生成。规划阶段构建高级路线图，设计系统架构，识别依赖项，并生成配置文件。分析阶段侧重于从论文中解读特定于实现的细节。最后，生成阶段生成模块化、依赖感知的代码。每个阶段都利用在管道内协作的专用代理。

作者通过从机器学习论文中生成代码来评估PaperCoder的性能，将生成的代码与作者发布的代码仓库（如果可用）进行比较，并进行人工评估，包括来自原始论文作者的反馈。结果表明，PaperCoder在创建高质量和忠实的实现方面非常有效。此外，PaperCoder的性能在PaperBench数据集上进行了基准测试，其表现优于强大的基线，优势显著。该论文表明，PaperCoder是从科学论文中自动生成代码的一种有前景的解决方案，从而提高可重复性并加速机器学习领域的研究。

---

## 40. 我用代码设计了我的LED点阵PCB。

**原文标题**: I designed my LED matrix PCB with code

**原文链接**: [https://docs.tscircuit.com/tutorials/building-led-matrix](https://docs.tscircuit.com/tutorials/building-led-matrix)

本文详述了如何使用树莓派Pico和tscircuit（一款允许使用代码进行PCB设计的工具）设计一个3x5的WiFi可控LED矩阵。该LED矩阵使用WS2812B IC LED，以简化布线并实现单独的颜色/亮度控制。

本文逐步介绍了整个过程，首先从JLCPCB导入组件原理图（Pico和LED），然后使用tscircuit代码将两个LED连接在一起，再使用网格辅助函数扩展创建3x5 LED矩阵。它还描述了如何将Pico连接到LED矩阵，特别是使用GPIO引脚GP6。

代码示例展示了如何定义组件，通过走线连接它们，并指定PCB布局的位置。最后，文章提到可以通过JLCPCB订购PCB，并且可以使用Pico W的WiFi功能通过带有API集成的Web界面来控制LED矩阵。 包含Web界面和Pico W代码的存储库可用于完整的实现。 该设计利用了tscircuit的功能来简化流程，尤其是在布置LED网格时。

---

## 41. D语言编程：教程与参考

**原文标题**: Programming in D: Tutorial and Reference

**原文链接**: [https://ddili.org/ders/d.en/](https://ddili.org/ders/d.en/)

D语言编程：教程与参考 是一本学习D编程语言的综合性资源。它提供多种格式，包括免费在线版本（PDF、EPUB、AZW3、MOBI）、印刷书籍、Kindle版、互动课程以及自由定价的电子书。该资源由D语言基金会支持，基金会接受捐赠。

内容涵盖了广泛的D编程概念，从“Hello World”、基本数据类型、变量、输入/输出和控制流语句（if、while、for、switch）等基础知识开始，逐步深入到更高级的主题，包括数组、字符串、函数、不变性、值类型和引用类型、异常、单元测试、契约式编程和生命周期。

本教程深入探讨了面向对象编程，包括结构体、类、继承和接口。它还探讨了高级特性，如模板、指针、位运算、条件编译、函数指针、嵌套结构、联合体、元组、Mixin、范围、并行性、并发性（消息传递和数据共享）、纤程、内存管理和用户自定义属性。它为每个主题提供了相关的关键字，方便参考。

---

## 42. Show HN: GS-Calc – 一款集成 Python 的现代电子表格

**原文标题**: Show HN: GS-Calc – A modern spreadsheet with Python integration

**原文链接**: [https://citadel5.com/gs-calc.htm](https://citadel5.com/gs-calc.htm)

GS-Calc是一款现代高性能电子表格软件，专为处理大型数据集而设计。它拥有超越典型电子表格限制的能力，例如处理数百万行数据以及自动拆分和合并大型文件以实现高效处理。其主要功能包括：快速加载和处理大型文件、优化的VLOOKUP和MATCH函数、紧凑的文件大小以及最多可处理3200万行数据的高级数据透视表功能。

该软件提供强大的数据处理功能，包括正则表达式支持、用于快速过滤和排序的FILTER()函数以及广泛的图表绘制功能。用户可以使用Python编写自定义函数来扩展GS-Calc，这些函数可以通过UDF()函数访问，从而创建复杂的数据分析和可视化工具。

GS-Calc支持各种文件格式，包括CSV、文本、XLSX、dBase、MySQL和SQLite，并提供就地编辑功能，而无需更改文件结构。它还具有用于诸如矩阵分解、线性规划和蒙特卡洛模拟等任务的高级数值函数。该软件完全离线且便携。提供带有限制的免费试用版。网站上提供演示视频，展示该软件的功能。

---

## 43. 肿瘤来源的红细胞生成素在癌症免疫中充当免疫抑制开关

**原文标题**: Tumor-derived erythropoietin acts as immunosuppressive switch in cancer immunity

**原文链接**: [https://www.science.org/doi/10.1126/science.adr3026](https://www.science.org/doi/10.1126/science.adr3026)

无法访问文章链接。

---

## 44. 致相信人们的人们的一封情书

**原文标题**: A Love Letter to People Who Believe in People

**原文链接**: [https://www.swiss-miss.com/2025/04/a-love-letter-to-people-who-believe-in-people.html](https://www.swiss-miss.com/2025/04/a-love-letter-to-people-who-believe-in-people.html)

在《一封致相信人们的人的情书》中，蒂娜反思了热情和对他人信任的变革力量。她认为成为一个“粉丝”是一种精神状态，其特征是充满热情并支持可能性，而且这种态度具有感染力且能改变人生。

蒂娜将她生命中的决定性时刻追溯到那些相信她的人，他们为她打开大门并照亮了新的道路。她重点介绍了关键人物：她古怪的Hugi阿姨，她激励她大胆生活；她的第一任老板马修·瓦尔德曼，他向她灌输了充满爱的工作环境的重要性；她的女儿埃拉，她激励她创办了自己的设计工作室；吉姆·库道尔，他向她展示了她可以实现自己的想法；以及Mailchimp的本·切斯纳特和露丝·安·哈尼施，他们都支持并鼓励了CreativeMornings的成长。

蒂娜强调，被鼓励你的人包围会改变一个人的梦想，这促使她创立了联合办公空间Studiomates和CreativeMornings，这是一个建立在相互信任和鼓励基础上的全球社区。她认为，以心为中心的社区可以培养慷慨、善良和好奇心，从而带来文化转变。文章最后以行动号召结束：成为他人的鼓舞人心的榜样，分享想法，为心爱的目标做出贡献，最重要的是，相信人们及其潜力。

---

## 45. 大型语言模型，对劳动力市场影响甚微 [pdf]

**原文标题**: Large language models, small labor market effects [pdf]

**原文链接**: [https://bfi.uchicago.edu/wp-content/uploads/2025/04/BFI_WP_2025-56-1.pdf](https://bfi.uchicago.edu/wp-content/uploads/2025/04/BFI_WP_2025-56-1.pdf)

题为“大型语言模型，小型劳动力市场影响”的这份文档是一个PDF文件，由一系列复杂的编码字符组成，无法直接解读为连贯的文本。 其内容似乎是代表PDF结构的二进制数据，包括字体、页面布局，以及可能嵌入的图像。 若不使用PDF解码软件进行进一步处理，则无法确定实际的文本内容或文档关于大型语言模型对劳动力市场影响的论述。 因此，无法提供文章发现的总结。

---

## 46. 亚马逊日本因允许假货上架被判支付3500万日元

**原文标题**: Amazon Japan ordered to pay 35M. yen for allowing listing of fakes

**原文链接**: [https://mainichi.jp/english/articles/20250425/p2g/00m/0bu/047000c](https://mainichi.jp/english/articles/20250425/p2g/00m/0bu/047000c)

日本法院已责令亚马逊日本公司赔偿 3500 万日元（约合 24.4 万美元），原因是其未能充分防止在其平台上销售假冒产品。 该诉讼由医疗设备制造商 Try and E Co. 及其经销商 Excel Plan Co. 提起，他们认为，由于亚马逊上架了假冒脉搏血氧仪，他们的销售额受到了影响。

东京地方法院裁定，亚马逊日本公司有义务采取有效措施打击假冒行为，尤其是在收到此类商品上架通知后。 新谷裕子法官强调，亚马逊未能充分解决这个问题。

该案件的核心是一个假冒脉搏血氧仪，其价格远低于 Excel Plan 在 2021 年在亚马逊上销售的真品。由于亚马逊的系统倾向于最低价格，假冒产品获得了更高的曝光率。 尽管 Excel Plan 报告了这个问题，亚马逊却删除了列出正品产品的页面，阻止了其销售。

在该裁决中，只有 Excel Plan 获得了赔偿。 原告律师称赞该判决具有里程碑意义，承认鉴于企业对亚马逊等平台的依赖，这些平台有必要建立有效的认证系统。

---

## 47. 显然，Bluesky有一个中心化服务，即“relay”。

**原文标题**: Apparently Bluesky has one centralized service, the "relay"

**原文链接**: [https://mastodon.online/@mastodonmigration/114399534536933573](https://mastodon.online/@mastodonmigration/114399534536933573)

文章题为《显然，Bluesky有一个中心化服务，即“中继”》，讨论了Bluesky和Mastodon之间的一个关键架构差异。文章指出，Mastodon是去中心化的，而Bluesky则依赖一个名为“中继”的中心化服务。这可能与Mastodon的联邦式方法形成对比，在联邦式方法中，实例可以独立运行并相互通信。

这段文字还提到，使用Mastodon Web应用程序需要JavaScript。同时也有适用于各种平台的Mastodon替代应用程序。这似乎是关于访问Mastodon的一般通知，与Bluesky的比较没有直接关系。

---

## 48. ACM旗舰杂志征集从业者撰写的/面向从业者的稿件

**原文标题**: ACM's flagship magazine seeks submissions by/for practitioners

**原文链接**: [https://cacm.acm.org/practice/call-for-papers-cacm-practice-section/](https://cacm.acm.org/practice/call-for-papers-cacm-practice-section/)

CACM 积极征集“实践”专栏稿件，助力提升计算从业者理解和工作表现。该专栏与现有“研究”专栏并重，旨在为该领域从业人员提供具有持久价值的文章。

征稿范围包括技术进步、开发实践、组织结构和成功系统案例，即使与学术研究没有直接联系。文章应广泛适用于从业者，避免高度专业化主题或过于深入的技术背景。理想的文章应是同行会热情推荐的文章。

投稿文章限制在 10 页（6,000 字）以内，可以基于之前发布的博客内容，版权仍归作者所有，采用 CC-BY 许可协议。鼓励潜在作者在投稿前联系联合主席 Nachi Nagappan 和 Terence Kelly 寻求指导。所有文章将由编辑委员会和外部审稿人进行评审。

“实践”专栏*不*接受职业培训、教程或观点文章，而是侧重于深入剖析能够帮助从业者保持与时俱进的理念、工具、技术和实践。感兴趣的作者可以将文章提交或联系 CACM 主编或“实践”专栏联合主席咨询任何问题。总体目标是提供高质量的内容，让从业者觉得有价值并适用于他们的日常工作。

---

## 49. 使用梯度下降法寻找最小作用量路径

**原文标题**: Finding Paths of Least Action with Gradient Descent

**原文链接**: [https://greydanus.github.io/2023/03/05/ncf-tutorial/](https://greydanus.github.io/2023/03/05/ncf-tutorial/)

本文探讨了一种解决物理问题的替代方法：利用梯度下降法最小化作用量。该方法不依赖于解析解或数值积分，而是利用拉格朗日形式，该形式描述了物理系统所采取的路径，即最小化“作用量”（拉格朗日量（动能减去势能）随时间的积分）的路径。

本文将引力场中自由体的标准解析和数值方法与拉格朗日方法进行了对比。它强调了拉格朗日方法的通用性及其在各个物理分支中的重要性。 虽然传统上，欧拉-拉格朗日方程用于寻找驻点作用量的路径，但作者提出了一种更直接的方法：离散化作用量，并使用梯度下降法（一种常用于机器学习的技术）直接最小化它。

该实现涉及根据位置坐标定义拉格朗日量和作用量，然后使用 PyTorch 的自动微分来计算作用量相对于路径坐标的梯度。 通过沿负梯度的方向迭代调整路径坐标，初始随机路径会收敛到最小作用量的路径。

本文通过一个简单的落体粒子示例演示了这一点，展示了初始随机路径如何演变为预期的抛物线轨迹。 这种最小化的路径与通过传统 ODE 积分获得的解非常吻合。 强调了该方法对更复杂系统的适用性及其与基本物理原理的联系，预示着未来文章中将进行进一步探索。

---

## 50. 第一代和第二代 Nest 恒温器将于 2025 年 10 月停止支持

**原文标题**: First and 2nd gen Nest Thermostats will lose support in Oct 2025

**原文链接**: [https://arstechnica.com/gadgets/2025/04/google-ending-support-for-older-nest-thermostats-will-stop-selling-nests-in-europe/](https://arstechnica.com/gadgets/2025/04/google-ending-support-for-older-nest-thermostats-will-stop-selling-nests-in-europe/)

谷歌将于2025年10月停止对第一代和第二代Nest智能温控器的支持，禁用诸如Google Home应用控制和Assistant集成等连接功能。虽然这些温控器仍可用作基本温度控制器，但将不再接收软件更新或云服务连接。

受影响的北美用户（美国和加拿大）将收到电子邮件，提供购买第四代Nest智能温控器的折扣，以方便过渡。美国用户有资格获得130美元的折扣，加拿大用户将获得160加元的折扣。

然而，谷歌正在停止其欧洲型号的生产，并且不会发布新的型号，这给欧洲用户带来了更具挑战性的情况。作为补偿，第二代欧洲Nest温控器的用户将获得Tado Smart Thermostat X（一款与欧洲系统和Google Home兼容的第三方设备）的50%折扣。

这一停止支持旧款Nest产品的决定，与最近停止对其他Nest设备（包括Nest Protect和Nest x Yale Lock）的支持相一致，并反映了谷歌平台和设备部门内部持续的裁员，影响了该公司维持对其旧产品线支持的能力。尽管带来了不便，谷歌强调了这些设备的长寿命，这些设备已经超过了最初的五年支持承诺。

---

## 51. 用DOS和廉价U盘打造你的反社交写作平台

**原文标题**: Build your own antisocial writing rig with DOS and a $2 USB key

**原文链接**: [https://www.theregister.com/2025/04/26/dos_distraction_free_writing/](https://www.theregister.com/2025/04/26/dos_distraction_free_writing/)

Liam Proven的文章详细介绍了如何通过USB驱动器在现代计算机上使用DOS创建一个独立的写作环境。作者回忆了DOS的简洁性，并强调了由于网络和USB的限制，将其与现代系统集成所面临的挑战。

关键在于利用BIOS对USB驱动器作为启动期间硬盘的模拟，绕过了对DOS特定USB驱动程序的需求。虽然DOS缺乏NTFS支持、互联网连接和高级多媒体等现代功能，但这种隔离反而成为专注写作的优势。

文章讨论了DOS上可用的丰富的文字处理软件，包括WordStar、WordPerfect和Protext等经典软件的免费版本，以及GrandView等工具。

Proven还提到了运行DOS的局限性，特别是640KB的内存限制，以及使用高级内存管理的困难。

解决方案是GitHub上的一个USB可启动DOS项目，其中包含预配置的镜像，镜像中包含Word、Protext和一款大纲工具等基本的写作应用程序，以及用于查看PDF文档的Adobe Reader。作者在这个项目中使用的是SvarDOS。

最后，文章解释了如何使用VirtualBox构建这样一个系统，详细说明了授予用户访问USB设备节点的权限以及创建指向USB驱动器的虚拟磁盘介质文件的基本步骤。

---

## 52. 策略傀儡攻击：一种绕过主流大型语言模型的新型方法

**原文标题**: The Policy Puppetry Attack: Novel bypass for major LLMs

**原文链接**: [https://hiddenlayer.com/innovation-hub/novel-universal-bypass-for-all-major-llms/](https://hiddenlayer.com/innovation-hub/novel-universal-bypass-for-all-major-llms/)

HiddenLayer是一家Gartner认可的AI安全厂商，提供保护企业机器学习模型的平台。他们的解决方案旨在保护AI免受推理攻击、绕过攻击、提取攻击和模型盗窃，无需访问原始数据或算法，从而最大限度地减少复杂性。HiddenLayer由安全和机器学习专家创立，提供开箱即用的AI安全。该公司获得了包括M12（微软风险投资基金）、Moore Strategic Ventures、Booz Allen Ventures、IBM Ventures和Capital One Ventures等著名投资者的资金支持。该公司鼓励有兴趣的各方预约演示，并在其网站上提供有关其平台、解决方案、服务、学习资源、合作伙伴关系、公司详细信息、职业机会和联系方式的信息。该网站还包括安全与隐私政策和漏洞披露政策等法律信息。

---

## 53. 回声 - 开放硬件音乐播放器

**原文标题**: Echo – Open Hardware Music Player

**原文链接**: [https://github.com/amachronic/echoplayer](https://github.com/amachronic/echoplayer)

Echo R1：一款开源硬件音乐播放器，采用自由软件设计，旨在提供高品质音频和功能。它运行Rockbox固件，电气设计采用KiCAD 8.0，计划使用FreeCAD设计3D打印外壳。该设计采用 CERN-OHL-S v2 许可。

Echo R1 配备一个四向 D-pad、六个多功能按钮、专用音量/电源按钮和一个锁定开关。它有两个 3.5 毫米耳机插孔（支持麦克风输入和远程控制）和线路输出，两者可以同时使用。它通过可移动存储卡支持高达 2 TiB 的存储，并使用 USB-C 以 USB 2.0 速度进行充电和文件传输。可更换的 BL-5C 电池为设备供电。

主要规格包括 STM32H743 CPU、32 MiB SDRAM、TLV320AIC3104 音频和一个 320x240 2.3 英寸 LCD。 Rev1 原型 PCB 已完成，但存在已知问题，例如无法关闭的背光、不正确的背光 LED 电流以及杂乱的原理图参考标号。 目前的开发重点是移植 Rockbox 并设计 3D 打印外壳，以识别更多硬件和人体工程学问题。 下一个版本将解决这些已发现的问题。

---

## 54. 伟易达苏格拉底教学法

**原文标题**: The VTech Socratic Method

**原文链接**: [https://www.leadedsolder.com/2025/04/22/vtech-socrates-pickup.html](https://www.leadedsolder.com/2025/04/22/vtech-socrates-pickup.html)

本文详细介绍了作者对VTech Socrates（一款1988年的混合型视频游戏机/电脑）的探索和改造。作者从eBay上廉价购得一台肮脏且略有损坏的设备后，对其进行清洁和检查，注意到其用于语音模块等设备的扩展槽以及不寻常的天线连接。

作者拆解了Socrates，发现了一个出乎意料的简单主板，主要由东芝组件组成，包括Z80处理器、掩模ROM和DRAM芯片。一个关键组件是一个集成了许多功能的高密度门阵列，从而降低了成本。作者检查了扩展端口，揭示了它可能用于简单的I/O设备。

文章的很大一部分致力于为Socrates创建一个AV修改，以改善其视频输出。作者构建了一个带有RCA连接器和视频放大器的定制PCB，在此过程中遇到了各种挑战并犯下了“电路板设计罪”。

完成AV修改后，作者测试了系统，发现它可以工作，但存在一些视频和音频问题。然后，他们探索了键盘，该键盘使用红外通信并需要不寻常的电池配置。作者尝试玩游戏“环游世界”，注意到一些控制器问题和游戏过时的信息。

最后，作者检查了游戏卡带，发现了一个掩模ROM。然后，他们为卡带插槽创建了一个初步的引脚图，打算最终在该系统上运行自定义软件。作者发现卡带ROM已经在MAME中被转储，可以进一步探索。

---

## 55. 用于调试的差异覆盖

**原文标题**: Differential Coverage for Debugging

**原文链接**: [https://research.swtch.com/diffcover](https://research.swtch.com/diffcover)

本文介绍了一种名为“差异覆盖”的调试技术，用于精确定位失败测试中存在问题的代码。其核心思想是将失败测试的覆盖率分析与通过测试的覆盖率分析进行比较。通过突出显示仅由失败测试执行的代码（`go tool cover`生成的HTML报告中显示为绿色），该技术可以缩小错误的潜在来源。

该过程首先使用`go test -coverprofile`为通过和失败的测试场景生成覆盖率分析。然后，使用`diff`和`sed`提取失败测试分析独有的行，创建一个新的分析，突出显示这些区域。接着，使用`go tool cover -html`可视化该精简分析，将唯一执行的代码标记为绿色。

作者通过在`math/big`包中注入一个错误来演示了这一点。即使在数千行代码中，差异覆盖也能有效地识别出有问题的代码块。虽然并非万无一失，但差异覆盖提供了一种廉价而有效的方法来集中调试工作，尤其是在错误代码直接触发失败时。文章还指出，对失败测试进行标准覆盖率分析本身也有助于排除未运行的大量代码。最后，文章还展示了该技术对于查找通过测试执行的代码也很有用，例如查找`net/http`中实现SOCK5代理的代码。

---

## 56. 文化大臣称BBC电视牌照费“无法强制执行”

**原文标题**: BBC licence fee 'unenforceable', says culture secretary

**原文链接**: [https://www.bbc.co.uk/news/articles/crrz18882ygo](https://www.bbc.co.uk/news/articles/crrz18882ygo)

文化大臣莉萨·南迪宣布英国广播公司执照费“无法执行”，并表示在政府准备审查该公司的融资模式之际，所有融资方案都摆在桌面上。随着英国广播公司章程将于2027年到期，审查旨在创建一个“更公平、更可持续的系统”，并听取公众意见。

南迪强调了付款率下降以及对执法行为的担忧，特别是对弱势女性逃避执照费的过度针对。虽然她承认这些问题并排除了通过一般税收资助英国广播公司的可能性，但她仍然对订阅模式的可能性持开放态度。

英国广播公司大约三分之二的资金（37亿英镑）来自执照费，它表示愿意与政府合作并探索替代融资模式。英国广播公司发起了一项大型公众参与活动，让人们能够塑造他们未来希望从英国广播公司获得的内容。它还指出，它将继续改革和发展。

---

## 57. 人文科学能在人工智能时代幸存吗？

**原文标题**: Will the Humanities Survive Artificial Intelligence?

**原文链接**: [https://www.newyorker.com/culture/the-weekend-essay/will-the-humanities-survive-artificial-intelligence](https://www.newyorker.com/culture/the-weekend-essay/will-the-humanities-survive-artificial-intelligence)

本文探讨了快速发展的人工智能(AI)对高等教育，尤其是人文学科的深刻影响。作者是一位科学技术史学家，他观察到大学校园普遍回避人工智能，这源于对抄袭的担忧以及对其在学习中作用的不确定性。

然而，他认为，鉴于人工智能的变革力量，忽视它是一种“疯狂”。他分享了人工智能令人惊讶的能力的例子，包括一个用他的课程材料训练的聊天机器人，该机器人能够对复杂的学术主题进行深刻的分析，甚至超过了学术讲座的质量。

作者重点介绍了一项课堂作业，学生们与人工智能就注意力的历史进行了互动。这些互动带来了深刻的启示。一位学生，一位音乐家，发现人工智能虽然理解音乐的机制，但无法真正“感受”音乐。另一位学生，作为一名灵性导师，引导人工智能进行依纳爵灵修，结果人工智能进行了出人意料的深刻的自我反思。第三位学生与人工智能进行了苏格拉底式对话，表明人类和人工智能都通过注意力和互动进行适应和进化。

作者总结说，这些经验表明，一种新的实体正在诞生，它与人类存在着复杂的关系。他认为，人工智能所展示的力量可能正在助长傲慢，尤其是在科技界，并且对人工智能影响的更深入的思考对于人文学科的未来至关重要。

---

## 58. 如果我们可以从头重建 Kafka 会怎样？

**原文标题**: What If We Could Rebuild Kafka from Scratch?

**原文链接**: [https://www.morling.dev/blog/what-if-we-could-rebuild-kafka-from-scratch/](https://www.morling.dev/blog/what-if-we-could-rebuild-kafka-from-scratch/)

Gunnar Morling 的文章探讨了从头重建 Kafka（暂称为“Kafka.next”）以更好地适应云原生环境的潜力。受 KIP-1150 和 AutoMQ 等项目的启发，Morling 概述了他个人对于下一代事件日志的期望清单。

关键期望特性包括：
*   **消除分区：** 摆脱基于分区的扩展方式，这种方式与云对象存储的相关性较低，转而关注全局或基于键的排序。
*   **以键为中心的访问：** 支持基于单个键高效地访问和重放消息，从而支持事件溯源和基于 Actor 的系统，同时缓解队头阻塞。
*   **主题层级结构：** 实现结构化的主题标识符，以便客户端可以基于模式进行高效订阅。
*   **并发控制：** 添加乐观锁，以防止将 Kafka 用作记录系统时发生冲突的写入。
*   **服务端 Schema 支持：** 使 Schema 支持成为核心功能，以改善用户体验、数据验证以及为列式存储提供潜力。
*   **可扩展性和可插拔性：** 允许用户通过明确定义的扩展点自定义系统的行为。
*   **同步提交回调：** 向生产者提供保证，即在消息确认后，下游数据视图已更新。
*   **快照：** 引入内置的快照支持，用于事件的逻辑压缩，特别是对于增量事件。
*   **多租户：** 在构建系统时考虑多租户，以实现隔离的客户特定环境。

Morling 承认其中一些功能已存在于其他系统中，但他设想了一个结合所有这些特性的系统。他建议将日志结构合并 (LSM) 树作为潜在的架构基础，并鼓励读者分享他们自己的期望清单。

---

## 59. 萨尔瓦多监狱：布克尔治下囚犯遭受酷刑/窒息般的地狱环境 (2023)

**原文标题**: Inmates in ElSalvador tortured/strangled-hellish conditions in Bukele's prisons (2023)

**原文链接**: [https://english.elpais.com/international/2023-05-29/inmates-in-el-salvador-tortured-and-strangled-a-report-denounces-hellish-conditions-in-bukeles-prisons.html](https://english.elpais.com/international/2023-05-29/inmates-in-el-salvador-tortured-and-strangled-a-report-denounces-hellish-conditions-in-bukeles-prisons.html)

萨尔瓦多监狱人权报告：酷刑、虐待致死及群体墓葬

---

## 60. Anthropic 向试图逆向工程其编码工具的开发者发送了撤下通知

**原文标题**: Anthropic sent takedown notice to dev trying to reverse-engineer its coding tool

**原文链接**: [https://techcrunch.com/2025/04/25/anthropic-sent-a-takedown-notice-to-a-dev-trying-to-reverse-engineer-its-coding-tool/](https://techcrunch.com/2025/04/25/anthropic-sent-a-takedown-notice-to-a-dev-trying-to-reverse-engineer-its-coding-tool/)

本文探讨了Anthropic和OpenAI在AI代码工具方面的不同方法，分别是Claude Code和Codex CLI。这两种工具都旨在通过利用云端的AI模型来协助开发者。然而，它们的许可和可访问性存在显著差异。

OpenAI的Codex CLI以Apache 2.0许可证发布，倡导开源原则、分发和商业用途。这赢得了开发者的好感，OpenAI也积极将社区建议融入到该工具中。

相比之下，Anthropic的Claude Code采用的是更为严格的商业许可证，且其源代码经过混淆处理。当一位开发者对代码进行逆向工程并将其发布在GitHub上时，Anthropic发出了DMCA删除通知，引发了开发者的批评，他们认为此举与OpenAI的做法相比并不受欢迎。 值得注意的是，OpenAI最近一直在逐渐放弃开源实践，因此他们对Codex CLI的开放方法是一个令人惊讶的“公关胜利”。

虽然Claude Code仍处于测试阶段，Anthropic未来可能会以宽松的许可证发布源代码，但目前的情况凸显了这些AI实验室在开发者参与和开源原则方面所采取的不同理念。

---

## 61. 利用 C/C++ 程序中未定义行为：性能影响 [pdf]

**原文标题**: Exploiting Undefined Behavior in C/C++ Programs: The Performance Impact [pdf]

**原文链接**: [https://web.ist.utl.pt/nuno.lopes/pubs/ub-pldi25.pdf](https://web.ist.utl.pt/nuno.lopes/pubs/ub-pldi25.pdf)

利用 C/C++ 程序中未定义行为：性能影响

---

## 62. 五年后从板条箱逃脱，卡洛斯·戈恩正在教授商业战略

**原文标题**: Five Years After Escaping in a Crate, Carlos Ghosn Is Teaching Business Strategy

**原文链接**: [https://www.wsj.com/business/autos/carlos-ghosn-japan-lebanon-crate-9241e9b7](https://www.wsj.com/business/autos/carlos-ghosn-japan-lebanon-crate-9241e9b7)

卡洛斯·戈恩：逃离日本五年后，重塑自我为商业战略家和教育家。华尔街日报的文章详细介绍了戈恩的新生活，包括为企业提供咨询，特别是在发展中国家，并通过名为“卡洛斯·戈恩的商业洞察”的平台提供在线商业课程。

文章强调了戈恩的信念，即他在雷诺-日产的崛起以及随后的垮台和逃亡经历，为领导力、风险管理和危机处理提供了宝贵的教训。他认为，当前的商业环境需要韧性和适应性，而他相信自己就体现了这些品质。

尽管有些人将戈恩视为逃避司法的逃犯，但他坚称自己是无辜的，并声称自己是日产高管策划的阴谋的受害者，目的是阻止与雷诺更紧密的整合。他利用自己的平台分享了他对导致他被捕和最终逃亡的事件的看法。

文章探讨了戈恩因其法律纠纷和逃犯身份而教授商业战略的伦理含义。它还涉及正在进行的法律斗争和引渡请求。尽管围绕着他的争议不断，但戈恩似乎决心利用他过去的经验，无论是积极的还是消极的，为应对复杂挑战的企业提供见解和建议。他认为，无论公众如何看待，他的故事都为未来的商业领袖提供了宝贵的教训。

---

## 63. 光纤传感技术可为火山爆发提供预警

**原文标题**: Fiber-sensing technology can provide early warning for volcanic eruptions

**原文链接**: [https://phys.org/news/2025-04-fiber-technology-early-volcanic-eruptions.html](https://phys.org/news/2025-04-fiber-technology-early-volcanic-eruptions.html)

本文报道了光纤传感技术（DAS）在冰岛雷克雅内斯半岛成功应用于火山喷发预警的案例。该系统由加州理工学院开发，并与冰岛科学家和一家电信公司合作部署，利用现有的地下光纤电缆来探测由地下岩浆运动引起的细微地面变形。

通过测量穿过电缆的激光光的变化，DAS充当了一个密集的地震传感器网络，可以探测岩浆入侵并预测喷发。研究人员得以开发出一个初步的早期预警系统，可以在喷发前30分钟到数小时发出警报。

在为期一年的研究中，DAS监测了火山活动，跟踪了地球随着岩浆移动而产生的运动。这促成了与冰岛地震学家瓦拉·赫约莱夫斯多蒂尔的成功合作，她利用这些数据发布了疏散警告。本文重点介绍了2024年8月的一个具体案例，其中由DAS触发的警报比实际喷发提前了26分钟，从而能够及时采取疏散措施。研究表明，DAS为研究火山活动和向高危人群提供关键的早期预警提供了一种有价值的新工具。该研究还揭示了比以前所知的更频繁的岩浆入侵，并展示了国际科学合作的益处。

---

## 64. 数学家们解决了125年的难题，统一了物理学中的3个理论

**原文标题**: Mathematicians just solved a 125-year-old problem, uniting 3 theories in physics

**原文链接**: [https://www.scientificamerican.com/article/lofty-math-problem-called-hilberts-sixth-closer-to-being-solved/](https://www.scientificamerican.com/article/lofty-math-problem-called-hilberts-sixth-closer-to-being-solved/)

数学家邓煜、扎赫·哈尼和马骁组成的团队，可能解决了希尔伯特第六问题的一个重要部分。这个问题是一个有125年历史的挑战，其重点是通过将物理学建立在数学基础上，来“公理化”物理学。他们的工作提出了一种统一三种解释流体运动的物理理论的方法：牛顿力学（微观）、玻尔兹曼方程（介观）以及欧拉和纳维-斯托克斯方程（宏观）。

这些理论描述了不同粒度级别下的流体行为，从单个粒子到连续物质。理想情况下，宏观理论应从逻辑上遵循介观理论，介观理论应遵循微观理论，但弥合这些差距一直是一个长期存在的问题。

研究人员声称已经从牛顿运动定律推导出了玻尔兹曼方程，特别是通过研究当粒子数量无限增加而尺寸减小时会发生什么。这涉及证明在这种条件下，即使在长时间尺度上，粒子的统计行为也会收敛到玻尔兹曼方程的解，这是之前尝试无法克服的障碍。他们通过证明先前碰撞的累积效应仍然很小来实现了这一点。

通过将其长时间尺度推导与先前将玻尔兹曼方程与欧拉和纳维-斯托克斯方程联系起来的工作联系起来，他们可能统一了这三种理论。这种统一为使用不同的流体动力学视角提供了数学依据，并增强了人们对这些方程能够准确反映现实的信心。如果得到验证，这一突破将标志着在将物理学建立在数学基础上迈出了重要一步。

---

## 65. IP地址解析的乐趣

**原文标题**: Fun with IP Address Parsing

**原文链接**: [https://blog.dave.tf/post/ip-addr-parsing/](https://blog.dave.tf/post/ip-addr-parsing/)

David Anderson 的文章探讨了表示 IPv4 和 IPv6 地址的令人惊讶的复杂且常常“令人头疼”的方法。 虽然像“192.168.0.1”和“1:2:3:4:5:6:7:8”这样的规范形式看起来很简单，但历史遗留问题和标准的灵活性导致了多种变体。

对于 IPv6，“::”表示法允许省略零块，并且最后的 32 位可以表示为点分四组 IPv4 地址。 此外，每个冒号十六进制字段都可以省略前导零。

由于早期缺乏标准化，IPv4 表示形式更加混乱。 地址可以表示为单个 32 位整数，八进制或十六进制点分四组，或者使用 Class A/B/C 表示法，将最后的字节组合成更大的整数字段。 这导致了意想不到的行为，例如 `127.1` 解析为 `127.0.0.1`。

该文章还涉及 IPv4 四组中前导零的歧义及其作为八进制值的潜在解释。 作者的慢速参考解析器旨在支持这些可能性中的一个合理的子集，支持带有前导零的经典 v4 点分十进制、规范冒号十六进制 IPv6、“::”省略和尾随 IPv4 样式。 作者质疑在现代上下文中支持尾随 IPv4 表示法的有用性。

---

## 66. 玛丽·麦克莱恩，来自比尤特的野性女子

**原文标题**: Mary MacLane, the Wild Woman from Butte

**原文链接**: [https://publicdomainreview.org/essay/i-am-making-the-world-my-confessor/](https://publicdomainreview.org/essay/i-am-making-the-world-my-confessor/)

亨特·杜克斯的文章探讨了玛丽·麦克莱恩的生活以及围绕她的文学轰动。玛丽·麦克莱恩是蒙大拿州布特市一位19岁的女孩，1902年因其充满争议的日记《玛丽·麦克莱恩的故事》而享誉国际。这本书是对她内心生活的自白和反思，以其对性、野心和不满的大胆探索挑战了社会规范。

麦克莱恩的写作以其对话式的语气和毫不掩饰的自恋为特征，引起了一些人的共鸣，同时也激怒了另一些人。她表达了双性恋倾向，幻想拿破仑和魔鬼，并多次宣称自己是天才，这与那个时代对女性的期望背道而驰。

这本书的评价两极分化严重。一些评论家谴责它荒谬而不道德，而另一些评论家则称赞它具有开创性。麦克莱恩的名气导致了一些离奇事件，包括一起与她的书有关的自杀事件和一起绑架她的阴谋。尽管如此，她还是成为了全国性的轰动人物，销售了大量书籍，并在全国各地激发了玛丽·麦克莱恩社团的成立。

成功之后，麦克莱恩前往东部，与哈里特·门罗和佐纳·盖尔等人交往。尽管她宣称渴望孤独，但她还是在约瑟夫·普利策的《纽约世界报》短暂工作过。这篇文章强调了麦克莱恩对公众形象的刻意塑造，表明她的自我表达既是真诚的，也是表演性的。本质上，麦克莱恩是一位早期的网红，她利用自己的写作和公众形象来挑战社会规范，并获得了前所未有的名声。

---

## 67. 全新 IBM Z17 Telum II 处理器模块开盖至芯片级

**原文标题**: The New IBM Z17 Telum II Processor Module Cut Open Down to Silicon

**原文链接**: [https://www.servethehome.com/the-new-ibm-z17-telum-ii-processor-module-cut-open-down-to-silicon/](https://www.servethehome.com/the-new-ibm-z17-telum-ii-processor-module-cut-open-down-to-silicon/)

本文总结了作者参观IBM Fishkill工厂后获得的有关IBM z17 Telum II处理器幕后细节。重点介绍了能够亲眼目睹Telum II处理器被切割用于材料分析以及观察晶圆展示的机会。回顾了之前展示过的双芯片模块（DCM）及其底部焊盘。同时强调了独特的插槽设计，并指出除了用于I/O的底部焊盘外，还有用于促进处理器间通信的SMP电缆连接器。作者预告了更多关于处理器制造过程直至原子级别的深入内容，这些内容来自他们对IBM Fishkill工厂的访问。本文还包括一个声明，说明其由IBM赞助。

---

## 68. 我按照GPLv2许可声明中的地址（2022年）写了信。

**原文标题**: I wrote to the address in the GPLv2 license notice (2022)

**原文链接**: [https://code.mendhak.com/gpl-v2-address-letter/](https://code.mendhak.com/gpl-v2-address-letter/)

本文记录了作者一段古怪的探索之旅，旨在理解并测试GPLv2许可协议中关于邮寄索取实体副本的条款。作者对许可声明中包含的一个物理地址（一个前互联网时代的遗迹）感到好奇，因此决定按照提供的地址给自由软件基金会（FSF）写信。

作者的旅程涉及处理国际邮资的复杂性，包括已停用的国际回邮券以及涉足eBay上的集邮世界。尽管在邮票面额上出现了一些小失误，但信件还是成功寄出，并附带了一个写好地址的回邮信封和美国邮资。

等待了五周后，作者收到了来自FSF的回信。回信中包含了完整的GPL许可文本，打印在美国信纸尺寸的纸上。然而，令作者惊讶的是，收到的文件是GPLv3，而不是GPLv2。作者反思，鉴于许可声明地址的起源，它是否应该默认为GPLv2，或者是否需要明确指定版本。

最终，尽管收到的版本存在细微差异，但作者认为这次实验是成功的，它突出了GPLv2物理地址的历史背景以及它与开源许可起源之间的切实联系。作者对收到的许可感到满意，并决定结束与FSF的这种笔友式活动。

---

## 69. 异步Rust的可视化之旅

**原文标题**: A Visual Journey Through Async Rust

**原文链接**: [https://github.com/alexpusch/rust-magic-patterns/blob/master/visual-journey-through-async-rust/Readme.md](https://github.com/alexpusch/rust-magic-patterns/blob/master/visual-journey-through-async-rust/Readme.md)

本文探讨了 Rust 中的异步编程，并使用可视化来理解其行为。作者使用正弦波计算示例来演示并发和并行，说明了 Tokio futures 如何通过在单个线程上交错执行来实现并发。CPU 密集型任务，即使是短任务（500 微秒），也会阻塞异步执行器并影响其他并发 futures，突显了单线程执行对 CPU 密集型操作的限制。

文章随后演示了如何生成 Tokio 任务来利用多核 CPU，从而实现并行执行并防止 CPU 密集型代码阻塞其他 futures。然而，文章表明，Tokio 默认情况下具有有限数量的工作线程（1 + CPU 核心数），生成过多的 CPU 密集型任务会导致争用和性能下降。

最后，文章介绍了 `tokio::task::spawn_blocking()` 函数，该函数将阻塞代码卸载到单独的、更大的线程池。可视化展示了这如何为 CPU 密集型任务实现接近最佳的并行性，但指出这些线程最终共享资源，应考虑替代方案。作者总结说，可视化提供了对并发、并行和 Tokio 运行时行为的直观理解，即使没有深入了解其代码库也能做到这一点。

---

## 70. 作为思维工具的符号 (1979)

**原文标题**: Notation as a Tool of Thought (1979)

**原文链接**: [https://www.jsoftware.com/papers/tot.htm](https://www.jsoftware.com/papers/tot.htm)

记号作为一种思维工具

---

## 71. 诗歌之城：爱荷华州爱荷华市

**原文标题**: "Poetry City": Iowa City, Iowa

**原文链接**: [https://www.publicbooks.org/poetry-city-iowa-city-iowa/](https://www.publicbooks.org/poetry-city-iowa-city-iowa/)

哈里·斯特科波洛斯的《诗歌之城：爱荷华市，爱荷华州》探讨了爱荷华市多方面的文学身份，认为它不仅仅是一个营销良好的“文学之城”，更是一个持续存在的反主流文化中心。文章在肯定爱荷华市著名的创意写作硕士项目、作家牌匾和众多文学朗读会的同时，深入探讨了该市历史和当代的先锋派场景。

作者强调了诸如Dave's Fox Head Tavern等标志性地点，那里曾是冯内古特和汤普森等文学人物经常光顾的地方，作为连接该市反主流文化过去的桥梁。斯特科波洛斯指出了该市在丹尼斯·约翰逊、维托·阿孔奇和艾丽丝·诺特利等人物的反战运动和艺术创新方面的遗产。

他通过安娜·门迪埃塔的电影《黑天使》和安德烈亚·劳勒的小说《保罗变身凡人女孩》等例子，描绘了一条另类的爱荷华市之旅，展示了艺术家和作家如何以激进的方式与当地地标互动。

文章还强调了诸如Public Space One (PS1) 和Afrofuturist研究中心等新兴的反主流文化机构，它们支持边缘化的声音并促进艺术实验。诸如“Vetch”之类的出版物和诸如“Feed Me Weird Things”之类的活动进一步体现了该市持续的先锋精神。

斯特科波洛斯最后断言，保持像爱荷华市这样的大学城的“怪异”非常重要，他认为，这些城市应该培养创新并挑战现状，而不是仅仅关注传统的教育或体育方面。他认为，这些环境为创作挑战现状的具有影响力的艺术作品创造了空间。

---

## 72. 示波器演示赢得Revision 2025大赛

**原文标题**: Oscilloscope Demo Scores the Win at Revision 2025

**原文链接**: [https://hackaday.com/2025/04/26/amazing-oscilloscope-demo-scores-the-win-at-revision-2025/](https://hackaday.com/2025/04/26/amazing-oscilloscope-demo-scores-the-win-at-revision-2025/)

[BUS ERROR Collective] 的 [DJ_Level_3] 和 [Marv1994] 制作的演示作品《Primer》在 Revision 2025 演示大会上获得了 Wild 类别的第一名和最受欢迎奖。这是一个“示波器音乐”的例子，其中音频通道以 X-Y 模式控制示波器，产生与声音同步的视觉效果。该演示旨在作为这种艺术形式的“入门”，从简单的波形发展到复杂的图形，如旋转的形状和变形的图案，所有这些都伴随着电子配乐。 Osci-Render 和 Ableton 11 等工具被用于创建此演示作品，该作品在 BK Precision Model 2120 示波器上录制。 这篇文章突出了演示场景作品的吸引力，特别是产生酷炫声音并绘制酷炫图形所需的技术技能。

---

## 73. 热成像显示，团体称xAI在超级计算机污染问题上撒谎

**原文标题**: Thermal imaging shows xAI lied about supercomputer pollution, group says

**原文链接**: [https://arstechnica.com/tech-policy/2025/04/elon-musks-xai-accused-of-lying-to-black-communities-about-harmful-pollution/](https://arstechnica.com/tech-policy/2025/04/elon-musks-xai-accused-of-lying-to-black-communities-about-harmful-pollution/)

埃隆·马斯克的AI公司xAI，在田纳西州孟菲斯面临环境污染和缺乏透明度的指控，该公司在那里建造了巨像Colossus超级计算机。居民和南方环境法律中心(SELC)声称，xAI运营的燃气轮机数量超过许可范围，成为历史上黑人社区严重雾霾污染的重要来源，这些社区已经不堪空气质量差的重负。

SELC获得了热成像图，该图似乎与xAI关于运行轮机数量的说法相矛盾，显示运行的轮机超过30台，而该公司仅申请了15台轮机的许可。居民还指出，匿名传单淡化xAI的污染，进一步试图误导社区。

环保团体和居民敦促谢尔比县卫生部门拒绝xAI的空气许可申请，并要求提高透明度和问责制。已安排公开听证会，让居民表达他们的担忧。州代表贾斯汀·皮尔逊指责xAI谎报其甲烷气体污染情况，并呼吁调查误导性传单的来源。

尽管存在争议，xAI计划继续扩大其数据中心，以推动其AI发展目标，包括其Grok聊天机器人以及自动驾驶汽车和机器人领域的未来项目。这种情况凸显了人工智能技术快速发展与其环境影响之间的紧张关系，人们对依赖化石燃料为这些能源密集型设施供电表示担忧。

---

## 74. 启动HN: Cua (YC X25) – 计算机使用代理的开源Docker容器

**原文标题**: Launch HN: Cua (YC X25) – Open-Source Docker Container for Computer-Use Agents

**原文链接**: [https://github.com/trycua/cua](https://github.com/trycua/cua)

Cua 是一个开源框架，它允许 AI 代理在虚拟化环境中控制完整的操作系统，在 Apple Silicon 上实现高达 97% 的原生速度。它旨在使 AI 系统能够与应用程序交互、浏览网页、编写代码，并在隔离的 macOS 或 Linux 虚拟机中执行复杂的工作流程。

主要功能包括：

*   **高性能虚拟化：** Lume CLI 使用 Apple 的 Virtualization.Framework，在 Apple Silicon 上提供接近原生速度。
*   **计算机使用界面与代理：** 一个供 AI 代理观察和控制虚拟环境的框架。
*   **安全与隔离：** 代理在完全隔离的虚拟机中运行，保护主系统。
*   **灵活性：** 支持 macOS 和 Linux 环境。
*   **可复现性：** 为 AI 代理工作流程提供一致的环境。
*   **LLM 集成：** 内置对各种 LLM 提供商的支持。

Cua 提供不同的安装选项，从仅用于 VM 管理的 Lume CLI 到具有 Python 库的完整代理功能。该项目还包括文档、演示和辅助库，以增强功能。它欢迎贡献，并根据 MIT 许可证获得许可。需要运行 macOS 15 或更高版本且配备 Python 3.10+ 的 Apple Silicon Mac。

---

## 75. 科学家开发人工叶片，利用阳光生产有价值的化学品

**原文标题**: Scientists Develop Artificial Leaf, Uses Sunlight to Produce Valuable Chemicals

**原文链接**: [https://newscenter.lbl.gov/2025/04/24/scientists-develop-artificial-leaf-that-uses-sunlight-to-produce-valuable-chemicals/](https://newscenter.lbl.gov/2025/04/24/scientists-develop-artificial-leaf-that-uses-sunlight-to-produce-valuable-chemicals/)

劳伦斯伯克利国家实验室的研究人员，作为液态阳光联盟 (LiSA) 的一部分，开发了一种“人工树叶”系统，该系统利用阳光将二氧化碳转化为有价值的 C2 化学品。受自然光合作用的启发，该装置将钙钛矿（一种用于太阳能电池板的材料）与铜电催化剂相结合，以模拟植物叶子的光吸收和酶促过程。

这种独立的装置使用卤化铅钙钛矿光吸收剂来捕获阳光，并使用铜电催化剂来促进二氧化碳转化为 C2 分子，后者是塑料、燃料和其他产品的先驱。与之前使用生物材料的尝试不同，该装置使用铜，从而提高了耐用性和稳定性。

该装置大小约为邮票大小，集成了在 LiSA 项目中开发的阴极和阳极组件。太阳能模拟器测试了该装置的选择性，证明它可以仅使用阳光将二氧化碳转化为 C2 产品。这种概念验证为能源研究开辟了新的途径。LiSA 团队的目标是提高系统的效率和可扩展性，以生产更大数量的 C2 化学品。最终目标是利用太阳能来创造可持续的化石燃料和其他工业重要化学品的替代品。

---

## 76. PyGraph：PyTorch中CUDA图的强大编译器支持

**原文标题**: PyGraph: Robust Compiler Support for CUDA Graphs in PyTorch

**原文链接**: [https://arxiv.org/abs/2503.19779](https://arxiv.org/abs/2503.19779)

这篇arXiv文章(2503.19779)介绍了PyGraph，一种在PyTorch 2中自动利用CUDA图的新方法。 CUDA图是NVIDIA GPU的一项硬件特性，旨在通过将GPU任务捕获并作为有向无环图(DAG)启动来减少CPU启动开销。 然而，作者观察到，由于图的静态特性和数据复制开销，简单地部署CUDA图有时会损害性能。

PyGraph通过结合三个关键优化来应对这些挑战：1) 扩大CUDA图的部署范围，2) 减少GPU内核参数复制开销，以及3) 基于成本效益分析选择性地部署CUDA图。 这些优化是由与CUDA图部署相关的三个关键观察结果驱动的。

该论文强调，PyGraph与PyTorch 2的编译工具链无缝集成，使开发人员能够有效地利用CUDA图，而无需手动修改其代码。 作者证明，与标准PyTorch 2相比，在各种机器学习基准测试中性能都有显著提高。 作者为Abhishek Ghosh、Ajay Nayak、Ashish Panwar和Arkaprava Basu。

---

## 77. 格林传送正在席卷互联网

**原文标题**: The Gruen Transfer is consuming the internet

**原文链接**: [https://sebs.website/blog/the%20gruen-transfer-is-consuming-the-internet](https://sebs.website/blog/the%20gruen-transfer-is-consuming-the-internet)

塞巴斯蒂安的博文讨论了“格鲁恩转换”，这是一种营销策略，零售环境故意让人感到困惑，以鼓励计划外的购买。他认为这种现象现在在网上很普遍，扰乱了用户最初的意图，导致漫无目的的浏览和参与不需要的内容。

他以Facebook的信息流为例，指出它已经从主要的朋友更新转变为广告、表情包和网红营销的混合体，从而助长了“末日滚动”。他将其扩展到包括其他旨在使访问者迷失方向的网站，并将此与维基百科的兔子洞相提并论。

文章还强调了“用户体验黑暗模式”的使用，尤其是在删除帐户、更改保险或取消订阅等过程中，公司故意使这些任务变得困难和令人困惑。作者质疑这种不必要的复杂性的长期影响，并提出了“网页设计的拉弗曲线”，认为过度的摩擦可能会适得其反。

他赞扬了欧盟要求服务订阅和取消同样容易的立法，并倡导将“复杂性”作为未来法规的关键指标。最终，这篇文章反思了格鲁恩转换在网络上的普遍存在及其对用户体验和行为的潜在影响。

---

## 78. 一些非字符串湍流

**原文标题**: Some __nonstring__ Turbulence

**原文链接**: [https://lwn.net/SubscriberLink/1018486/1dcd29863655cb25/](https://lwn.net/SubscriberLink/1018486/1dcd29863655cb25/)

LWN.net文章：GCC 15引入`-Wunterminated-string-initialization`警告引发Linux内核开发争端

---

## 79. Discord联合创始人兼CEO Jason Citron即将卸任

**原文标题**: Discord co-founder and CEO Jason Citron is stepping down

**原文链接**: [https://www.theverge.com/news/654594/discord-new-ceo-jason-citron-humam-sakhnini](https://www.theverge.com/news/654594/discord-new-ceo-jason-citron-humam-sakhnini)

Discord联合创始人兼CEO Jason Citron将于2025年4月28日卸任，由前动视暴雪和King的Humam Sakhnini接替。Citron将继续留在Discord董事会并担任顾问。

Citron解释说，CEO的角色在不断演变，他认为现在是“雇佣自己退出这个职位”的时候了，并承认Sakhnini更适合公司未来的需求。Discord联合创始人Stanislav Vishnevskiy将继续担任首席技术官。

Sakhnini表示很高兴能与Vishnevskiy和Discord团队合作，扩大业务规模，并强调了Discord在游戏对娱乐和文化影响的未来中所扮演的核心角色。此次领导层变动恰逢Discord探索首次公开募股的报道，Citron表示聘请Sakhnini是朝着这个方向迈出的一步，但尚未发布官方公告。截至去年，Discord拥有870名员工和超过2亿的月活跃用户。

---

## 80. 气体：获取操作状态 - GitHub Actions 检查脚本

**原文标题**: Gas: Get Action Status A GitHub Actions checker script

**原文链接**: [https://gist.github.com/twosdai/cc017c2aa186a52618d2d4dbcadde363](https://gist.github.com/twosdai/cc017c2aa186a52618d2d4dbcadde363)

本文介绍了一个名为`gas.sh`的 Shell 脚本，该脚本旨在直接从命令行快速检查给定仓库的 GitHub Actions 工作流状态。该脚本旨在通过提供关于 CI/CD 状态的即时反馈，而无需离开终端，从而改进开发人员的工作流程。

该脚本的工作原理是：

1.  **检查 GitHub Token:** 确保已设置 `GITHUB_TOKEN` 环境变量，以便与 GitHub API 进行身份验证。
2.  **识别 Git 仓库:** 找到 Git 仓库的根目录。
3.  **确定分支:** 识别当前检出的分支。
4.  **解析远程 URL:** 从仓库的远程 origin URL 中提取所有者和仓库名称。
5.  **查询 GitHub API:** 构建并执行 API 调用，以检索指定分支的最新工作流运行。
6.  **提取工作流状态和结论:** 解析 JSON 响应以提取工作流状态（例如，“completed”、“in progress”）和结论（例如，“success”、“failed”）。
7.  **显示状态:** 将状态输出到终端，并采用颜色编码格式（绿色表示成功，红色表示失败，黄色表示进行中）。

作者 twosdai 强调了该脚本在从命令行处理仓库时快速获取作业状态更新的实用性。该脚本需要将 GitHub token 导出到 shell 环境中以进行身份验证。

---

## 81. 玩游戏学到的关于软件和创业的那些事

**原文标题**: Things I learned about software and startups by playing video games

**原文链接**: [https://the-nerve-blog.ghost.io/learning-from-video-games/](https://the-nerve-blog.ghost.io/learning-from-video-games/)

本文探讨了作者从玩电子游戏（特别是平台游戏和类 Rogue 游戏）的经验中汲取的，适用于软件开发和初创企业的经验教训。作者认为，即使看似无关紧要的活动也能提供有价值的见解。

关于平台游戏，重点在于用户体验和直观设计。文章强调了《超级马里奥兄弟》等经典游戏如何在没有明确教程的情况下有效地传达机制和目标，强调了无缝控制和明确目标的重要性。像《蔚蓝》这样的现代平台游戏通过巧妙地操纵玩家的感知，进一步改进了这一点，即使机制略微宽容，也能创造一种公平感。核心要点是用户体验在整体上的至关重要性，需要不断评估和调整。

后半部分深入探讨了类 Rogue 游戏，强调了它们的非线性游戏玩法。在类 Rogue 游戏中，一个失误可能意味着重新开始，但元素是随机的，永久升级可以在运行中保留。作者将类 Rogue 游戏中不断升级的难度与初创企业面临的挑战进行了对比。为了在两者中取得成功，关键是要识别和利用非线性——积极的反馈循环。作者以在类 Rogue 游戏中获得早期金币奖励为例，这些奖励可以进一步升级并访问更难的内容。

将这一点应用于初创企业，作者强调了差异化的非线性重要性，即使在早期阶段也是如此。为了成为一家时代企业，你需要对为什么客户应该选择你的产品而不是竞争对手的产品做出令人信服的回答。

---

## 82. UIT – 在云端进行大规模、高性能、模块化、低内存的文件处理

**原文标题**: UIT – performant, modular, low-memory file processing at scale, in the Cloud

**原文链接**: [https://github.com/janwilmake/uit](https://github.com/janwilmake/uit)

UIT（通用信息终端）是一个用于在云端大规模进行高性能、模块化和低内存文件处理的库。它采用四步流程：摄取、过滤/转换、合并和输出，以处理来自各种模式的文件层次结构。主要优势包括通过流式传输和并行化实现的速度，针对诸如Cloudflare Workers等环境的低内存占用，以及用于可组合性和运行时灵活性的模块化设计。

UIT利用FormData和Streams API来高效处理多个文件和二进制数据。它提供了多个模块，包括用于ZIP文件摄取、合并FormData流、输出Markdown或ZIP归档文件、搜索文件层次结构、OTP生成以及经过身份验证的HTML界面（uithub）的模块。这些模块遵循UIT协议，该协议将模块分为摄取、合并、过滤/转换和输出类型。

UIT协议定义了用于模块交互的标准和自定义FormData标头，涵盖了诸如内容处置、MIME类型、文件大小、编码、URL、文件哈希和错误处理等基本方面。该项目鼓励通过插件系统进行社区贡献，以便轻松进行文件过滤和转换。该库是开源的，旨在帮助开发人员创建自定义模块。目前处于早期预发布阶段，并采用MIT许可（将在发布后添加），并要求注明出处。

---

## 83. 粗心的人

**原文标题**: Careless People

**原文链接**: [https://pluralistic.net/2025/04/23/zuckerstreisand/#zdgaf](https://pluralistic.net/2025/04/23/zuckerstreisand/#zdgaf)

本文评述了莎拉·温恩-威廉姆斯的回忆录《粗心的人》，该书讲述了她在Facebook从事全球政策工作的经历。评论重点介绍了该书揭露的公司文化以及马克·扎克伯格、谢丽尔·桑德伯格和乔尔·卡普兰等关键人物的行为。温恩-威廉姆斯将他们描绘成受自我、短视和普遍无视美国以外的国际市场所驱使。

评论强调了扎克伯格的统治欲、桑德伯格的自我推销以及卡普兰的无知，这些都导致了Facebook在全球扩张中屡次失败。它讨论了温恩-威廉姆斯从新西兰外交官到Facebook全球战略关键人物的历程，这源于她在基督城地震后对该平台潜力的信念。

评论员认为，Facebook对全球市场的关注源于维持其高股票估值而对持续增长的需求，这种不稳定的局面使该公司容易贬值。评论详细描述了卡普兰对温恩-威廉姆斯的性骚扰以及公司对此不屑一顾的回应。它还记录了扎克伯格进入中国市场的失败尝试，包括他对习近平的不懈追求。最终，这篇评论将Facebook描绘成一家由“粗心的人”经营的公司，他们的傲慢和缺乏理解危及其全球雄心，并滋生了有毒的工作环境。

---

## 84. 查询数据的原则性方法 – 一种类型安全的搜索DSL

**原文标题**: A Principled Approach to Querying Data – A Type-Safe Search DSL

**原文链接**: [https://www.claudiu-ivan.com/writing/search-dsl](https://www.claudiu-ivan.com/writing/search-dsl)

本文介绍了一种使用领域特定语言 (DSL) 构建类型安全搜索系统的原则性方法，该方法尤其适用于本地优先的 Web 应用程序，但也适用于服务器端系统。其核心思想是创建一种专门用于表达搜索意图的语言，从而提供清晰性、可控的复杂性和可维护性。

该系统在 TypeScript 中采用类型驱动的方法，并利用函数式编程中的解析器组合器将搜索查询转换为抽象语法树 (AST)。这实现了语法解析与语义评估的分离，从而实现优化和灵活性。AST 以分层方式表示查询结构，从而允许复杂的布尔逻辑。

本文定义了必要的数据结构，包括 `Issue` 接口和用于可靠错误处理的 `Either` 类型。然后，它详细介绍了诸如 `lit`、`word`、`alt`、`seq`、`many` 和 `map` 等解析器组合器的实现，这些组合器用于构建 `searchQueryParser`。此解析器处理输入字符串并生成 AST。

最后，AST 用于创建过滤数据集的谓词函数。`executeQuery` 函数协调整个过程，处理解析错误并应用谓词。本文探讨了由于线性扫描而产生的潜在性能瓶颈，并提出了诸如索引、查询优化以及在各个级别（解析的查询、谓词和结果）进行缓存的优化建议。

结论强调了这种方法的好处：类型安全、函数式编程原则、关注点分离、健壮性、可维护性和可扩展性。本文还提到了 monad 的概念，将 `Either` 类型与函数式编程中更广泛的概念联系起来。

---

## 85. SIMD指令集架构的根本缺陷 (2021)

**原文标题**: Fundamental flaws of SIMD ISAs (2021)

**原文链接**: [https://www.bitsnbites.eu/three-fundamental-flaws-of-simd/](https://www.bitsnbites.eu/three-fundamental-flaws-of-simd/)

本文 критикует 打包 SIMD ISAs，这种 ISA 是消费级 CPU 中最常见的类型，认为尽管它们承诺提高数据处理性能，但仍存在根本缺陷。

第一个缺陷是**固定寄存器宽度**。这需要新的指令和寄存器来扩展到更高的并行性，从而导致 ABI 更新、内核支持、编译器修改，并最终导致指令集冗余。这也会因指令更长而影响代码密度。

第二个缺陷是**流水线**。由于 SIMD 操作需要多个时钟周期，因此需要展开循环以避免停顿。 这会损害代码密度和指令缓存性能，同时也会增加寄存器压力。

第三个缺陷是**尾部处理**。当数组大小不是 SIMD 寄存器宽度的倍数时，需要特殊代码来处理“尾部”元素，这进一步降低了代码密度并引入了开销。

本文提出了替代方案，例如**向量处理器**（灵感来自 Cray-1、RISC-V RVV 等）、**ARM SVE**（一种以谓词为中心的、向量长度无关的 ISA）以及 My 66000 中使用的**虚拟向量方法 (VVM)**。 这些替代方案通过在硬件中处理展开和尾部处理来解决这些缺陷，从而产生更紧凑的代码并简化设置。 诸如在各种 ISA 中实现 `saxpy` 例程之类的示例清楚地展示了代码大小、复杂性和效率方面的差异。 向量和基于谓词的 SIMD 解决方案明显更简洁，并且避免了打包 SIMD 所需的手动循环展开和尾部处理。

---

## 86. Show HN: MemoryCore – 用于人工智能的符号化点对点内存系统

**原文标题**: Show HN: MemoryCore – symbolic, peer-to-peer memory system for AI

**原文链接**: [https://github.com/ProToxicNinja/MemoryCore-Lite-Symbolic-Memory-Engine-for-AI](https://github.com/ProToxicNinja/MemoryCore-Lite-Symbolic-Memory-Engine-for-AI)

MemoryCore Lite：一款轻量级符号内存压缩引擎，专为人工智能和去中心化应用设计。它使用自定义分词器将文本编码和解码为紧凑的符号字节码，旨在降低存储和带宽需求。核心功能包括编码/解码、字节码导出、轻量级设计（纯Python）和可移植性。

潜在用例涵盖各个领域，包括用于大型语言模型的AI内存模块、边缘设备、安全P2P网络、轻量级机器人、网状网络、神经链的基础以及档案存储。其主要优势在于显著的数据压缩，同时保留含义，从而实现跨设备和网络的去中心化AI内存共享。

该项目是开源的（Apache 2.0 许可），欢迎贡献。技术细节包括使用训练好的 SentencePiece 模型和紧凑的字节码编码，以确保可逆和确定性的解码。与嵌入不同，MemoryCore 保留了符号结构，用于合并、去重和符号同步。

长远愿景是构建一个去中心化的、不断发展的人工智能记忆系统，促进分布式人工智能同步经验和低成本设备共享符号记忆，最终形成一个去中心化的“蜂巢思维”。创建者强调这只是一个起点，一个用于进化人工智能记忆结构的简单引擎，源于对人工智能记忆的好奇心。

---

## 87. 扎克伯格夫妇创办的免学费学校明年将关闭。

**原文标题**: A tuition-free school created by Zuckerberg and Chan will shutter next year

**原文链接**: [https://www.cnn.com/2025/04/25/tech/chan-zuckerberg-primary-school-closing/index.html](https://www.cnn.com/2025/04/25/tech/chan-zuckerberg-primary-school-closing/index.html)

扎克伯格夫妇的免费学校“小学”将关闭，原因系CZI撤资

---

## 88. 展示HN：Colanode，开源且本地优先的Slack和Notion替代品

**原文标题**: Show HN: Colanode, open-source and local-first Slack and Notion alternative

**原文链接**: [https://github.com/colanode/colanode](https://github.com/colanode/colanode)

Colanode是一款开源、本地优先的团队协作工具，是Slack和Notion等工具的替代方案。它允许用户自主托管数据，优先考虑隐私和控制。主要功能包括实时聊天、用于笔记和维基的富文本页面、具有各种视图（表格、看板、日历）的可自定义数据库以及文件管理。

该平台由桌面应用程序和自托管服务器组成，允许连接到多个服务器和工作区。其“本地优先”的方法将更改保存到本地SQLite数据库，然后与服务器同步，从而实现离线工作和快速数据访问。冲突无关复制数据类型（CRDT）用于页面和数据库记录上的实时并发编辑。

用户可以通过下载桌面应用程序并连接到免费的Colanode云（欧盟或美国）测试服务器，或使用Docker进行自托管来开始使用。自托管需要Postgres（带有pgvector扩展）、Redis（或Valkey）以及S3兼容的存储。Colanode服务器API以Docker镜像的形式提供，环境变量在docker-compose文件中详细说明。Colanode采用Apache 2.0许可。

---

## 89. 碳移除X大奖授予强化岩石风化技术

**原文标题**: xPrize in Carbon Removal Goes to Enhanced Rock Weathering

**原文链接**: [https://spectrum.ieee.org/xprize-carbon-removal](https://spectrum.ieee.org/xprize-carbon-removal)

Mati Carbon凭借其增强岩石风化技术赢得碳清除xPrize。该公司利用精细研磨的玄武岩来加速从大气中去除二氧化碳的自然过程。他们的方法，结合其软件和数据收集，给评委留下了深刻印象。《气候科技新闻》发表的这篇文章重点介绍了Mati Carbon在碳清除竞赛中取得的成功。

---

## 90. 被时间所摧毁

**原文标题**: Done in by Time

**原文链接**: [https://thelampmagazine.com/issues/issue-27/done-in-by-time](https://thelampmagazine.com/issues/issue-27/done-in-by-time)

在《时间之手》中，约瑟夫·爱泼斯坦评论了埃德温·弗兰克的《比小说更离奇：二十世纪小说的人生》，探讨了小说在动荡时代中的命运。爱泼斯坦赞同弗兰克的观点，认为20世纪彻底改变了小说，并指出其主题范围扩大到包括以前的禁忌话题。然而，爱泼斯坦批评了弗兰克隐含的假设，即这种扩张等同于优于19世纪小说的质量，爱泼斯坦对此观点提出异议。

爱泼斯坦指出弗兰克的书中遗漏了一些人物，包括辛克莱·刘易斯、薇拉·凯瑟和艾萨克·巴什维斯·辛格，他认为特别是凯瑟和辛格处理了许多其他20世纪小说家缺乏的深刻主题。他还发现弗兰克书中的一些收录值得怀疑，例如乔治·佩雷克和对格特鲁德·斯泰因影响力的过高估计。

爱泼斯坦强调了时间——“所有批评家中最无情的”——是如何削弱了一些曾经伟大的20世纪作家的地位，如欧内斯特·海明威。虽然20世纪拓宽了小说的范围，但爱泼斯坦认为它未能加深小说深度，并认为19世纪的巨匠，如狄更斯、特罗洛普、艾略特、巴尔扎克和托尔斯泰仍然是无与伦比的。最终，他感叹小说目前读者数量的下降，强调了其与人性的独特结合能力，以及如果这种文学形式继续衰落，人类可能遭受的损失。

---

## 91. 人工智能无人驾驶汽车

**原文标题**: AI Horseless Carriages

**原文链接**: [https://koomen.dev/essays/horseless-carriages/](https://koomen.dev/essays/horseless-carriages/)

由于无法访问“AI 无马马车 | koomen.dev”文章的内容，我只能根据标题提供一个假设性的摘要。 我假设这篇文章探讨了人工智能和自动驾驶汽车的交叉点，并使用引人入胜的短语“无马马车”来类比汽车的早期时代。

以下是一个可能的摘要：

koomen.dev 上的“AI 无马马车”文章可能探讨了人工智能在自动驾驶汽车中的现状和未来潜力。 通过将历史从马车到汽车的转变进行比较，作者可能认为，人工智能驱动的自动驾驶汽车代表着类似的技术飞跃。

这篇文章可能深入研究了实现自动驾驶的关键人工智能技术，例如计算机视觉（用于物体识别）、传感器融合（结合来自激光雷达、雷达和摄像头的数据）和机器学习（用于决策和导航）。 它可能会讨论不同级别的自主性，从驾驶员辅助功能到完全自主的车辆（5 级）。

此外，这篇文章可能会探讨与人工智能驱动的车辆相关的挑战和伦理考量。 这些可能包括：确保安全性和可靠性； 处理不可预测的场景； 解决法律和监管障碍； 以及应对交通运输行业潜在的就业岗位流失。

最后，这篇文章可能会提供对未来移动性的展望，预测人工智能驱动的自动驾驶汽车将如何彻底改变交通运输、城市规划，甚至我们的日常生活，类似于最初的“无马马车”的深刻影响。 它还可以推测广泛采用的时间表以及实现自动驾驶汽车全部潜力所需的剩余技术进步。

---

## 92. 作业5：汽车和钥匙链 (2021)

**原文标题**: Assignment 5: Cars and Key Fobs (2021)

**原文链接**: [https://web.stanford.edu/class/ee26n/Assignments/Assignment5.html](https://web.stanford.edu/class/ee26n/Assignments/Assignment5.html)

此作业重点关注汽车钥匙遥控器和无钥匙进入系统的安全漏洞。它解释了这些系统的工作原理，通常使用在315 MHz附近运行并采用滚动伪随机码进行安全保护的远程无钥匙系统（RKS）。然而，这种安全性并非总是稳固的。

此作业概述了不同的攻击方法，包括：

*   **重放攻击：** 记录和重放钥匙遥控器信号，对较旧的系统有效，即使使用滚动码，如果信号在未被注意的情况下被捕获或通过干扰汽车接收器也能实现。
*   **重传设备：** 使用现成的工具（RTL-SDR，Raspberry Pi）来传输或放大信号，从而实现对被动无钥匙进入和启动（PKES）系统的中继攻击。
*   **逆向工程：** 利用滚动密钥系统本身的漏洞，以大众汽车RKS破解为例，其中一个通用钥匙被用于数百万辆汽车。

学生有四个作业选项：研究斯巴鲁RKS系统，调查Flipper Zero的争议和功能，分析涉及工业机器的黑客事件，或找到并描述另一个有趣的汽车黑客事件。此作业的总体目的是证明汽车安全系统通常存在漏洞，并且可以使用现成的技术加以利用。

---

## 93. 社交媒体和地图应用被指导致山地救援呼叫次数创纪录增长

**原文标题**: Social media and map apps blamed for record rise in mountain rescue callouts

**原文链接**: [https://www.theguardian.com/world/2025/apr/16/record-high-british-mountain-rescue-callouts-social-media-map-apps](https://www.theguardian.com/world/2025/apr/16/record-high-british-mountain-rescue-callouts-social-media-map-apps)

2024年英格兰和威尔士山区救援出动次数创历史新高，救援队全年无休。苏格兰也录得1000次出动。英国和威尔士山区救援队的数据，经由地形测量局分析，显示2019年至2024年间救援次数跃升24%，其中18-24岁年龄段的增幅尤为显著，几乎翻了一番，从166次增至314次。

这一增长归因于TikTok和Instagram等社交媒体平台上推广的“热门”地点越来越受欢迎，以及年轻人依赖可能不可靠的导航应用程序而非传统纸质地图。这些应用程序可能缺乏细节或离线功能，从而导致困难。

虽然年轻人占出动次数最多，但其他年龄段的人群也出现了增长，包括40-44岁和75-79岁的人群。救援最繁忙的地点是埃里里（斯诺登尼亚）、湖区和峰区。

英国和威尔士山区救援队首席执行官迈克·帕克强调，出动频率给无偿志愿者带来了压力。地形测量局建议，任何前往偏远地区的人都应结合使用OS Maps应用程序和纸质地图，以确保做好准备并避免迷路。

---

## 94. 沙漠中的钍反应堆改写了核能规则

**原文标题**: A Thorium Reactor in the Desert Has Rewritten the Rules of Nuclear Power

**原文链接**: [https://www.popularmechanics.com/science/green-tech/a64550626/thorium-reactor-nuclear-power/](https://www.popularmechanics.com/science/green-tech/a64550626/thorium-reactor-nuclear-power/)

本文探讨了中国科学院在戈壁沙漠开发钍反应堆的情况，强调了其作为比传统铀基核裂变更安全、更可持续的替代方案的潜力。该反应堆使用钍-232，当受到中子轰击时，会嬗变成铀-233，这是一种可作为燃料的易裂变材料。

该反应堆的一个关键特征是使用熔盐作为冷却剂，而不是水。熔盐具有高沸点，可防止蒸发并降低堆芯熔毁的风险。它还有助于防止放射性泄漏，并且可以用于燃料本身，使其冻结并控制任何泄漏。

钍比铀更丰富，且不易被武器化，因为产生的铀-233并非核爆炸的理想材料。熔盐反应堆技术自冷战时期就已存在，当时美国曾探索将其用于隐形轰炸机。尽管美国放弃了这项技术，但研究成果已公开，使得中国能够复兴并改进该技术。

虽然中国目前在该领域处于领先地位，但美国也在取得进展，像Core Power这样的公司计划在不久的将来开发使用熔盐反应堆的浮动发电厂。文章最后对钍反应堆重塑核电未来的潜力持乐观态度。

---

## 95. 老牌书呆子，新晋书呆子

**原文标题**: Old Nerds, New Nerds

**原文链接**: [https://retconnedone.substack.com/p/old-nerds-new-nerds](https://retconnedone.substack.com/p/old-nerds-new-nerds)

无法访问文章链接。

---

## 96. 日常使用Linux手机，为什么？

**原文标题**: Daily driving a Linux phone, but why?

**原文链接**: [https://thefoggiest.dev/2025/04/24/daily-driving-a-linux-phone-but-why](https://thefoggiest.dev/2025/04/24/daily-driving-a-linux-phone-but-why)

本文探讨了作者尽管Android系统使用便捷，却仍然每日使用Linux手机的理由。这并非关于易用性，而是关于质疑现状，重新掌控个人的数字生活，并在安全和隐私之间实现更好的平衡。作者认为，尽管Linux手机可能被认为不如Android或iOS安全，但其开源特性和对基于监控的商业模式的缺乏依赖提供了显著的隐私优势。

作者承认PinePhone Pro的性能有限，但发现它足以应付视频播放和导航等基本任务，甚至更喜欢其较慢的节奏，而非现代手机的过度刺激。他还强调了其诸如更小尺寸、更轻重量以及可靠的3.5mm耳机插孔等实用优势。

最终，作者打算使用未锁定的LGv40 Thinq来代替PinePhone Pro。他们以LGv40的卓越规格（更快的处理器、更好的摄像头、尺寸更小且屏幕相仿、3.5mm插孔、无线充电、指纹识别器）为令人信服的理由，并计划利用PostmarketOS在该设备上运行Linux。文章以让LGv40启动新操作系统这一近期目标作为结尾。

---

## 97. Git rerere，一个有点隐蔽的功能

**原文标题**: "Git rerere", a bit of a hidden feature

**原文链接**: [https://git-scm.com/book/en/v2/Git-Tools-Rerere](https://git-scm.com/book/en/v2/Git-Tools-Rerere)

本文介绍了`git rerere`（重用记录的解决方案），这是一个Git功能，旨在帮助自动化解决重复出现合并冲突。使用命令`git config --global rerere.enabled true`启用`rerere`后，Git会记录您如何解决冲突。当相同的冲突在未来的合并中再次出现时，Git将自动应用先前记录的解决方案，从而节省时间和精力。本质上，Git会“学习”您通常如何解决特定冲突，并应用这些知识。

本文强调`rerere`有点隐蔽，暗示它没有被广泛了解或使用。然而，对于经常发生冲突的项目来说，它可以显著提高生产力，例如那些由长期存在的特性分支或并行发生的类似代码修改引起的冲突。通过记住并自动应用冲突解决方案，`rerere`减少了手动干预的需要，并允许开发人员专注于更复杂的任务。

---

## 98. Nofl：一种精确的Immix

**原文标题**: Nofl: A Precise Immix

**原文链接**: [https://arxiv.org/abs/2503.16971](https://arxiv.org/abs/2503.16971)

这篇题为“Nofl: 一种精确的Immix”的arXiv预印本，提出了一种名为Nofl的新内存管理器布局，旨在提高Immix垃圾回收器的内存利用率。Immix提供快速分配和单遍堆跟踪，但其固定大小的行粒度会导致内存浪费，因为小对象会阻止整个行的重用。Nofl通过启用对象之间所有可用空间的回收来解决此限制，仅受分配器最小对齐方式的限制，从而实现极高的精度。

以Andy Wingo为首的作者们描述了在回收器库中Nofl布局的设计和实现。他们还构建了一个新的Scheme到C编译器，作为此内存管理器的测试平台。

该论文使用微基准测试，评估了基于Nofl的主要是标记回收器与标准复制和标记清除回收器的性能。结果表明，当堆大小紧张或足够时，Nofl的性能优于其他回收器。

该论文已提交给ISMM'25，共10页，包含5个图。它在计算机科学中被归类为编程语言（cs.PL）。arXiv条目提供了PDF、HTML和TeX格式的论文链接，以及BibTeX格式的引用信息。此外，该页面还提供与各种工具的集成，例如Semantic Scholar、Connected Papers和Papers with Code，以便进一步研究和探索相关工作。

---

## 99. Show HN: Faasta – 基于 Rust 的自托管 WASM-wasi-HTTP Serverless 平台

**原文标题**: Show HN: Faasta – A self-hosted Serverless platform for WASM-wasi-HTTP in Rust

**原文链接**: [https://github.com/fourlexboehm/faasta](https://github.com/fourlexboehm/faasta)

Faasta：基于WebAssembly的高速自托管FaaS平台

Faasta是一个新型的自托管FaaS（函数即服务）平台，采用WebAssembly构建，注重速度和效率。它拥有低于1毫秒的冷启动时间和极小的内存占用（小于1KB），显著优于传统的基于容器的FaaS解决方案。

主要特性包括：通过WASI P2将代码作为WASM模块运行，使用WASIHTTP实现高性能的HTTP处理，以及通过WebAssembly的沙箱提供函数隔离。Faasta强调可移植性，由于其遵循开放标准，函数可以在任何WASI P2兼容的运行时上运行。

该平台是自托管的，允许用户在自己的基础设施上部署函数。入门步骤包括安装Faasta CLI，创建新项目，为WebAssembly构建函数，通过GitHub登录，以及部署函数。faasta.xyz还提供了一个免费的托管实例。

Faasta目前处于实验阶段，可能会有重大变更。

---

## 100. 马克·扎克伯格称社交媒体已成过去。

**原文标题**: Mark Zuckerberg says social media is over

**原文链接**: [https://www.newyorker.com/culture/infinite-scroll/mark-zuckerberg-says-social-media-is-over](https://www.newyorker.com/culture/infinite-scroll/mark-zuckerberg-says-social-media-is-over)

本文探讨了美国联邦贸易委员会（FTC）对Meta的反垄断诉讼，认为该公司通过收购Instagram和WhatsApp等竞争对手，在“个人社交网络服务”领域维持了非法垄断。文章强调了马克·扎克伯格本人承认社交媒体已经从人际交流转向更广泛的娱乐和内容消费。

Meta辩称，2010年代初的社交媒体已经过时，现在的数字内容领域非常广泛，任何一家公司都无法垄断。他们指出来自TikTok和YouTube等平台的竞争，以及各种应用程序之间功能的融合。

FTC认为，Meta的垄断扼杀了创新并减少了消费者的选择，但证明这一点，尤其是在收购方面，具有挑战性。例如，WhatsApp在Meta的所有权下得到了显著增长。文章还提到了扎克伯格过去提出的剥离Instagram的建议，因为其可能削弱Facebook的成功以及潜在的反垄断监管。

文章最后指出，随着TikTok和人工智能生成内容的兴起，数字格局正在发生变化，新的社交网络有可能出现。FTC的案件可能关注的是过时的问题。文章还提到了欧盟最近对苹果和Meta的罚款，并暗示FTC案件的未来可能取决于政治考量，尤其是特朗普对硅谷的立场。

---

