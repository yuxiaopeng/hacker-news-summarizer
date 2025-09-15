# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-15.md)

*最后自动更新时间: 2025-09-15 17:46:17*
## 1. 在一次性电子烟上托管网站

**原文标题**: Hosting a website on a disposable vape

**原文链接**: [https://bogdanthegeek.github.io/blog/projects/vapeserver/](https://bogdanthegeek.github.io/blog/projects/vapeserver/)

本文详细介绍了如何在一次性电子烟中发现的、性能出人意料的微控制器上托管网站的过程。作者Bogdan Ionescu从电子烟中拆解了一块PUYA PY32F002B微控制器，该芯片具有24MHz Cortex M0+内核、24KB闪存和3KB内存。

核心思想是使用半主机模式，这是一种ARM微控制器与调试器通信的方法，实际上是将调试器变成一个网络接口。通过利用pyOCD和socat，作者创建了一个模拟调制解调器的虚拟串行连接。该连接使用SLIP（串行线路IP协议）来传输IP数据包。

为了处理TCP/IP通信，作者选择了轻量级的uIP协议栈，该协议栈最初是为8位和16位机器设计的。在解决了uIP中的对齐问题后，一个最小的HTTP服务器被成功实现。最初的性能很差，ping时间和页面加载速度都很慢。然而，通过实现一个环形缓冲区来有效地管理微控制器和主机之间的数据传输，性能得到了极大的改善，实现了20ms的ping时间和大约160ms的页面加载速度。

最终的结果是一个功能性的Web服务器，托管在一次性电子烟的微控制器上，大约有20KB的存储空间可用于网站内容。作者甚至为了好玩，还添加了一个JSON API端点。该项目代码可供其他人探索。

---

## 2. PayPal将支持以太坊和比特币

**原文标题**: PayPal to support Ethereum and Bitcoin

**原文链接**: [https://newsroom.paypal-corp.com/2025-09-15-PayPal-Ushers-in-a-New-Era-of-Peer-to-Peer-Payments,-Reimagining-How-Money-Moves-to-Anyone,-Anywhere](https://newsroom.paypal-corp.com/2025-09-15-PayPal-Ushers-in-a-New-Era-of-Peer-to-Peer-Payments,-Reimagining-How-Money-Moves-to-Anyone,-Anywhere)

PayPal推出“PayPal链接”，一项新功能，允许美国用户通过个性化的一次性链接在任何通信平台上收发款项。此举旨在简化P2P支付并扩展PayPal生态系统。计划于2025年9月晚些时候扩展到英国、意大利和其他市场。

关键的是，PayPal将把加密货币直接整合到其P2P支付流程中，使用户能够将比特币、以太坊和PYUSD（PayPal美元稳定币）发送给其他PayPal和Venmo用户，以及支持加密货币和稳定币的外部数字钱包。

新闻稿还强调，Venmo和PayPal亲友转账仍然免于1099-K报告，确保个人支付的私密性。 PayPal链接的推出被认为是PayPal发展中的重要一步，建立在25年革新资金流动的基础上。

该公司强调P2P支付量的强劲增长，并将其归功于改善的用户体验和可发现性。 凭借新宣布的旨在连接各种支付系统和数字钱包的“PayPal World”平台，PayPal预计P2P支付将进一步增长。文章还提到了与十大联盟和十二大联盟在学生运动员支付方面的合作。

---

## 3. 想监视我的狗，结果监视了TP-Link。

**原文标题**: Wanted to spy on my dog, ended up spying on TP-Link

**原文链接**: [https://kennedn.com/blog/posts/tapo/](https://kennedn.com/blog/posts/tapo/)

本文详细介绍了作者对Tapo室内摄像头工作原理的深入研究，该摄像头最初用于宠物监控。由于难以将摄像头与Frigate集成以及烦人的“Tapo Care”提示，作者开始了一项逆向工程之旅，以实现无云上线。

作者使用Frida和mitmproxy等工具，拦截并分析了Tapo应用程序与摄像头在上线期间的通信。这表明摄像头在与用户的云密码同步之前，使用默认密码（“TPL075526460603”）进行初始登录。作者发现了`securePassthrough`通道，该通道用于加密初始登录后的API调用，需要解密才能理解正在进行的通信。

通过使用JADX反编译Tapo应用程序APK并利用PyTapo库进行参考，作者成功解密了这些加密消息。此分析揭示了上线所涉及的关键步骤，包括Wi-Fi扫描、启用RTSP/ONVIF以及更改管理员密码。不必要的步骤被识别为干扰项。

这项努力的最终成果是一个Bash脚本，`tapo_onboard.sh`，它自动化了上线过程，而无需依赖云。该脚本使用默认密码登录，连接到Wi-Fi，禁用OSD徽标，启用RTSP/ONVIF，更改管理员密码，并加入Wi-Fi网络。

作者还指出了TP-Link安全实践中的不一致之处，例如同时使用SHA-256和MD5哈希，以及使用两个不同的公钥来加密密码。最后，作者实现了最初的目标：确认狗大部分时间都在睡觉。

---

## 4. 立方星是迷人的太空学习工具。

**原文标题**: CubeSats are fascinating learning tools for space

**原文链接**: [https://www.jeffgeerling.com/blog/2025/cubesats-are-fascinating-learning-tools-space](https://www.jeffgeerling.com/blog/2025/cubesats-are-fascinating-learning-tools-space)

本文探索了CubeSat这个迷人的世界。CubeSat是一种小型、标准化的卫星，由微控制器或树莓派供电，正日益成为太空探索和教育领域中越来越容易获得的工具。作者强调了他们对CubeSat的热情，因为它们带来了复杂的工程挑战，例如电源效率、小型化以及恶劣环境下的安全性。

本文涵盖了CubeSat构建的基础知识，并指出其模块化设计允许定制有效载荷，如相机和传感器。它将CubeSat项目的成本与传统卫星进行了比较，显示出大幅降低，使其更易于教育机构和业余爱好者使用。作者讨论了几个CubeSat项目，包括Mark Rober的SatGus和Manuel的“构建CubeSat”项目，该项目记录了开发CubeSat的挑战和学习经验。

本文介绍了两个面向STEM教育的CubeSat套件：MySat Kit和RASCube。这些套件提供了构建和编程CubeSat的实践经验，培养了对太空、电子和硬件集成领域的兴趣。最后，作者重点介绍了即将发射的SilverSat，这是一颗由学生建造的CubeSat，并鼓励读者了解如何使用廉价设备从后院跟踪卫星。本文强调了CubeSat社区在学习、教学和分享知识方面的极具感染力的热情。

---

## 5. 我需要多大的太阳能电池来储存我家所有的电力？

**原文标题**: How big a solar battery do I need to store all my home's electricity?

**原文链接**: [https://shkspr.mobi/blog/2025/09/how-big-a-solar-battery-do-i-need-to-store-all-my-homes-electricity/](https://shkspr.mobi/blog/2025/09/how-big-a-solar-battery-do-i-need-to-store-all-my-homes-electricity/)

本文探讨了使用电池储能实现伦敦郊区典型住宅100%太阳能自给自足的假设情景。作者利用自家住宅的能源数据（3,800千瓦时年消耗量和太阳能电池板的发电量）来计算所需的电池容量。

文章强调，简单的每日盈余计算不足以确定电池需求。相反，需要考虑产生的峰值过剩电力。作者使用2024年3月至2025年3月一整年的数据，计算了能源生产和使用之间的累积差额，揭示了需要高达1,068千瓦时（1兆瓦时）的巨型电池，才能储存所有夏季剩余的太阳能供冬季使用。

作者承认，以当前的技术和经济状况来看，如此大型的电池是不切实际的，并指出成本在10万英镑到50万英镑之间。然而，他们对电池价格迅速下降表示乐观，特别是像钠离子电池这样的新兴技术可能会将成本降低到与太阳能电池板安装相当的水平。

文章最后倡导家用太阳能，并设想了一个未来，届时家庭可以通过经济实惠的大规模电池储能实现完全的太阳能自给自足，从而使能源生产更接近消费，并减少对集中式电网的依赖。

---

## 6. 编程通缩

**原文标题**: Programming Deflation

**原文链接**: [https://tidyfirst.substack.com/p/programming-deflation](https://tidyfirst.substack.com/p/programming-deflation)

无法访问文章链接。

---

## 7. 枯燥的工作需要压力

**原文标题**: Boring Work Needs Tension

**原文链接**: [https://iaziz786.com/blog/boring-work-needs-tension/](https://iaziz786.com/blog/boring-work-needs-tension/)

本文认为，软件开发常被认为枯燥乏味、重复单调，但通过迎接挑战并扮演解决问题的英雄角色，可以变得令人兴奋。作者认为，开发者应该像引人入胜的故事中的主角一样，积极寻找并解决日常任务中固有的“张力”。

核心思想是通过识别和解决常见问题，如缓慢的CI/CD管道、数据库连接问题、内存泄漏、编写糟糕的代码、用户高延迟、数据库性能问题以及API响应不一致等，将平凡的工作转变为一系列迷你任务。这些问题被视为需要克服的“反派”。

作者强调，发现并解决这些问题可以为工作注入目标和兴奋感。鼓励开发者主动改进他们的系统和代码，无论项目经理或客户是否明确要求这些改进。这种积极主动的方法可以应用于专业和个人项目。通过积极应对这些挑战，开发者可以创造更具吸引力和成就感的工作体验，解决“张力”会带来更引人入胜和令人满意的成就“故事”。

---

## 8. 如何自托管 Google Fonts 的 Web 字体

**原文标题**: How to self-host a web font from Google Fonts

**原文链接**: [https://blog.velocifyer.com/Posts/3,0,0,2025-8-13,+how+to+self+host+a+font+from+google+fonts.html](https://blog.velocifyer.com/Posts/3,0,0,2025-8-13,+how+to+self+host+a+font+from+google+fonts.html)

无法访问文章链接。

---

## 9. RustGPT：纯 Rust 从零构建的 Transformer LLM

**原文标题**: RustGPT: A pure-Rust transformer LLM built from scratch

**原文链接**: [https://github.com/tekaratzas/RustGPT](https://github.com/tekaratzas/RustGPT)

RustGPT：纯 Rust 实现的 Transformer 大型语言模型，完全从零开始构建，仅使用 `ndarray` crate 进行矩阵运算，避免了 PyTorch 或 TensorFlow 等传统机器学习框架。该项目旨在展示如何构建 LLM，涵盖事实文本的预训练、会话 AI 的指令调优以及交互式聊天功能。

该架构采用标准的 Transformer 组件：分词、嵌入、Transformer 块（自注意力机制和前馈神经网络）、输出投影和词汇表管理。训练包括两个阶段：事实陈述的预训练和会话数据的指令调优。该模型使用 Adam 优化器和梯度裁剪。

要探索的关键文件包括 `src/main.rs` (训练流程和交互模式) 和 `src/llm.rs` (核心 LLM 实现)。该项目包含所有组件的全面测试。该实现强调模块化、清晰的接口，并避免外部 ML 依赖。

该项目鼓励贡献，尤其是在模型持久化（保存/加载）、性能优化、改进的采样方法（束搜索）和评估指标等领域。它概述了针对初级、中级和高级开发人员的各种贡献级别，侧重于模型保存/加载、位置编码、多头注意力和并行化等功能。该项目坚持“从零开始”的理念，强调纯 Rust 实现。

---

## 10. Asciinema CLI 3.0：用Rust重写，新增直播功能，升级文件格式

**原文标题**: Asciinema CLI 3.0 rewritten in Rust, adds live streaming, upgrades file format

**原文链接**: [https://blog.asciinema.org/post/three-point-o/](https://blog.asciinema.org/post/three-point-o/)

Asciinema CLI 3.0 发布，采用 Rust 全面重写，引入全新 asciicast v3 文件格式和实时终端流式传输。Rust 重写提升了性能，简化了安装，并实现了 asciinema 虚拟终端集成等新功能。

asciicast v3 格式使用时间间隔记录事件，简化了编辑并增加了对退出状态的支持，还重构了头部以获得更好的组织结构。新 CLI 支持两种模式的实时流式传输：本地（通过内置 HTTP 服务器）和远程（通过 asciinema 服务器）。asciinema 播放器包含自适应缓冲，提供流畅的观看体验。

本次更新优先考虑本地文件保存。`asciinema rec` 命令现在始终需要指定文件名进行本地存储，移除了自动上传行为。发布现在需要显式使用 `asciinema upload <filename>` 命令。新增服务器 URL 提示，允许用户显式选择 asciinema 服务器实例（默认为 asciinema.org），从而增强了自托管能力和数据隐私。总而言之，3.0 版本在功能、性能和用户数据处理控制方面提供了显著改进。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 2 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 3 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 4 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 5 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 6 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 7 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 8 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 9 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 10 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 11 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 12 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 13 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 14 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 15 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 16 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 17 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 18 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 19 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 20 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 21 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 22 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 23 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 24 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 25 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 26 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 27 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 28 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 29 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 30 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 31 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 32 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 33 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 34 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 35 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 36 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 37 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 38 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 39 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 40 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 41 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 42 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 43 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 44 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 45 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 46 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 47 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 48 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 49 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 50 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 51 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 52 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 53 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 54 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 55 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 56 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 57 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 58 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 59 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 60 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 61 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 62 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 63 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 64 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 65 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 66 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 67 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 68 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 69 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 70 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 71 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 72 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 73 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 74 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 75 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 76 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 77 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 78 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 79 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 80 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 81 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 82 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 83 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 84 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 85 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 86 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 87 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 88 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 89 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 90 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 91 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 92 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 93 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 94 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 95 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 96 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 97 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 98 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 99 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 100 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 101 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 102 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 103 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 104 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 105 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 106 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 107 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 108 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 109 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 110 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 111 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 112 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 113 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 114 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 115 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 116 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 117 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 118 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 119 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 120 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 121 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 122 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 123 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 124 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 125 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 126 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 127 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 128 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 129 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 130 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 131 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 132 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 133 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 134 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 135 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 136 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 137 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 138 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 139 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 140 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 141 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 142 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 143 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 144 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 145 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 146 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 147 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 148 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 149 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 150 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 151 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 152 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 153 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 154 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 155 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 156 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 157 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 158 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 159 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 160 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 161 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 162 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 163 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 164 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 165 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 166 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 167 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 168 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 169 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 170 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 171 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 172 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 173 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 174 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 175 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 176 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 177 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 178 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 179 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 180 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
