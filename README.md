# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-04-26.md)

*最后自动更新时间: 2025-04-26 17:44:56*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 2 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 3 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 4 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 5 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 6 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 7 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 8 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 9 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 10 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 11 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 12 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 13 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 14 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 15 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 16 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 17 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 18 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 19 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 20 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 21 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 22 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 23 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 24 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 25 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 26 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 27 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 28 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 29 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 30 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 31 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 32 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 33 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 34 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 35 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 36 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 37 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 38 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
