# Hacker News 热门文章摘要 (2025-09-15)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 移除FASTA文件中换行符可将ZSTD压缩率提高10倍。

**原文标题**: Removing newlines in FASTA file increases ZSTD compression ratio by 10x

**原文链接**: [https://log.bede.im/2025/09/12/zstandard-long-range-genomes.html](https://log.bede.im/2025/09/12/zstandard-long-range-genomes.html)

本文探讨了使用 Zstandard 的 `--long` 范围匹配查找器来压缩大型细菌基因组装配 FASTA 文件。作者 Bede Constantinides 发现，旨在通过增加搜索窗口来提高去重的 `--long` 选项，最初仅在 66.1 万个细菌基因组数据集（2.46 TiB）上产生了适度的压缩改进。Constantinides 假设 FASTA 文件中存在的修饰性换行符（每 60 个字符）干扰了 Zstandard 的长程模式匹配。

使用 `seqtk seq -l 0` 删除这些换行符显著提高了压缩率，使用 `--long` 后压缩率 (CR) 提高了三倍。进一步将窗口大小增加到最大值（使用 `--long=31`）再次使压缩率提高了三倍，最终文件大小为 80GiB，压缩率为 31。这使得 Zstandard 的压缩性能达到了专用、较慢的 DNA 序列压缩器的数量级内。

作者强调，虽然增加窗口大小会降低兼容性（解压缩时需要相同的 `--long=xx` 参数），但使用 `--long` 可以在速度和压缩率之间提供有价值的折衷方案。关键在于，在使用 Zstandard 和 `--long` 时，从 FASTA 文件中删除修饰性空白，尤其是换行符，以最大程度地提高压缩效率。此技术在具有高度相似序列的数据集上特别有效。作者还提到，结果因数据集而异，但 `--long` 似乎值得考虑。

---

## 12. Show HN：Daffodil – 连接任何平台的开源电商框架

**原文标题**: Show HN: Daffodil – Open-Source Ecommerce Framework to connect to any platform

**原文链接**: [https://github.com/graycoreio/daffodil](https://github.com/graycoreio/daffodil)

Daffodil是一个开源的电商开发框架，旨在构建可连接任何电商后端的、适应性强的店面。该框架通过利用其软件包集合，提供了一种创建高质量店面的方法。

主要特性和信息包括：

*   **适应性：** Daffodil的主要优势在于其连接各种电商后端的能力。
*   **快速启动：** 使用Angular应用中的`npx ng add @daffodil/commerce`命令可以简化安装过程。
*   **文档：** 提供丰富的文档，帮助开发者入门并探索该框架的功能。
*   **社区：** Daffodil鼓励社区参与，通过贡献指南、行为准则、Discord服务器和YouTube频道。
*   **软件包：** 提供了一个全面的可用Daffodil软件包列表，涵盖了诸如分析、身份验证、购物车管理、结账、产品目录、搜索、SEO等功能。“结账”软件包已被标记为遗留，目前不建议使用。
*   **贡献：** 鼓励开发者通过报告错误、贡献代码或改进文档来为项目做出贡献。
*   **GitHub：** 鼓励用户通过给Daffodil仓库加星来表达他们的支持。

---

## 13. 生命游戏逆向：自组装实现自动化

**原文标题**: Self-Assembly Gets Automated in Reverse of 'Game of Life'

**原文链接**: [https://www.quantamagazine.org/self-assembly-gets-automated-in-reverse-of-game-of-life-20250910/](https://www.quantamagazine.org/self-assembly-gets-automated-in-reverse-of-game-of-life-20250910/)

本文探讨了神经元胞自动机（NCAs），这是一种受生命游戏启发，由谷歌的亚历山大·莫德温采夫开发的新型自组装方法。与传统元胞自动机利用简单规则来支配复杂结构不同，NCAs 颠倒了这一过程，从期望的模式开始，学习产生该模式的规则。

NCAs 使用神经网络来定义每个细胞的“物理特性”，根据其邻居的状态来确定自身状态。这使得创建复杂的自组装系统成为可能，莫德温采夫的虚拟蝴蝶就是例证，它们可以再生受损的翅膀。生物学家对 NCAs 作为形态发生的模型很感兴趣，形态发生是指生物细胞形成组织和身体的过程，因为细胞仅对其邻居做出反应，并且可以自我重组。

NCAs 在医学领域具有潜在应用，可能有助于再生失去的肢体，在工程领域，它们可以启发完全分布式的计算机。研究人员正在探索促成 NCA 再生能力的因素，例如不可预测性和冗余性。他们发现，对噪声具有弹性的系统通常更灵活。

虽然 NCAs 为理解自组织和问题解决提供了一个有前景的模型，但它们在编码和抽象方面也带来了挑战。本文强调了 NCAs 通过实现更节能、大规模分布式并行系统来彻底改变计算的潜力。

---

## 14. 苹果拥有一个私有CSS属性，用于向Web内容添加液态玻璃效果。

**原文标题**: Apple has a private CSS property to add Liquid Glass effects to web content

**原文链接**: [https://alastair.is/apple-has-a-private-css-property-to-add-liquid-glass-effects-to-web-content/](https://alastair.is/apple-has-a-private-css-property-to-add-liquid-glass-effects-to-web-content/)

本文深入探讨了 Apple WebKit 引擎中一个隐藏的 CSS 属性 `-apple-visual-effect`，它允许开发者使用 WKWebView 在 iOS 应用中将“液态玻璃”效果应用于 Web 内容。作者通过监控 WebKit Github 仓库发现了这一点。

虽然令人兴奋，但目前该属性无法公开使用。它需要启用一个名为 `useSystemAppearance` 的私有 WKPreferences 设置，这很可能导致 App Store 拒绝。作者通过绕过该设置进行了实验，并成功实现了液态玻璃效果。

使用 CSS 实现此效果的优势在于可以使用 `@supports` 查询为不支持它的环境提供备用样式。

尽管目前存在局限性，但作者认为这一发现具有更广泛的意义。他提出了“阿拉斯泰尔的应用程序内 Webview 大头毛理论”，表明无缝集成的 Webview 往往不被注意。此属性的存在暗示 Apple 正在内部使用带有这些效果的 Webview，可能以用户没有意识到是基于 Web 的方式，微妙地影响着 iOS 的用户界面。文章的结论是，应用程序中的 Webview 之所以声名狼藉，主要是因为你不会注意到那些无缝集成的 Webview。

---

## 15. 微软将于十月强制安装 Microsoft 365 Copilot 应用。

**原文标题**: Microsoft to force install the Microsoft 365 Copilot app in October

**原文链接**: [https://www.bleepingcomputer.com/news/microsoft/microsoft-to-force-install-the-microsoft-365-copilot-app-in-october/](https://www.bleepingcomputer.com/news/microsoft/microsoft-to-force-install-the-microsoft-365-copilot-app-in-october/)

微软将于2025年10月开始在装有Microsoft 365桌面应用程序的Windows设备上自动安装Microsoft 365 Copilot应用。此应用为整个Microsoft 365套件（包括Word、Excel、PowerPoint、笔记本和AI助手）提供Copilot功能和AI驱动功能的中心访问点。

虽然该应用将被添加到Windows“开始”菜单并默认启用，但IT管理员可以选择通过应用管理中心选择退出。微软建议管理员在强制安装之前通知其用户和帮助台，以减少困惑和支持请求。

该部署计划于2025年10月初开始，11月中旬结束。但是，安装不会在位于欧洲经济区（EEA）内的系统上进行。微软强调，此举旨在简化Copilot的访问，并确保用户可以轻松发现和使用其提高生产力的功能。部分用户可能已经安装了该应用，因此这一变化可能不会被注意到。

此举是微软为提高Copilot可访问性而采取的更大举措的一部分，微软还将Microsoft 365 Copilot代理集成到Edge侧边栏中，并引入了一个设置，供管理员将该应用固定到Windows任务栏。

---

## 16. 各位，我们有最好的π。

**原文标题**: Folks, we have the best π

**原文链接**: [https://lcamtuf.substack.com/p/folks-we-have-the-best](https://lcamtuf.substack.com/p/folks-we-have-the-best)

无法访问文章链接。

---

## 17. 一个用65行C++代码实现的字符串格式化库

**原文标题**: A string formatting library in 65 lines of C++

**原文链接**: [https://riki.house/fmt](https://riki.house/fmt)

本文介绍了一个轻量级的 C++ 字符串格式化库，它用大约 65 行代码实现。该库旨在提供一个简单高效的替代方案，以取代更复杂且编译耗时的选项，如 `{fmt}` 或 `std::print`。

其核心功能围绕着 `fmt::format` 函数，该函数接受一个 `String_Buffer`（一个包含预分配的字符缓冲区、其容量和当前长度的结构）和一个格式化字符串。该格式化字符串使用 ` {}` 作为参数的占位符。该库处理 `{{` 的转义，以表示文字 `{`，并通过将占位符呈现为空字符串来优雅地处理缺失的格式化参数。

该库的关键组件包括：

*   `String_Buffer`：表示输出缓冲区。
*   `write`：执行边界检查的写入到缓冲区，必要时进行截断并更新缓冲区的长度。
*   `write_value`：重载函数，用于将各种数据类型（例如，string、int、bool）转换为字符串并将它们写入缓冲区。
*   `next_hole`：解析格式化字符串，识别并提取 ` {}` 占位符之间的文字部分。
*   `format_value`：如果找到空位，则将值插入到输出中。
*   `format`：主要格式化函数，它迭代格式化字符串，使用折叠表达式为每个参数调用 `format_value`。

本文重点介绍了所做的设计选择，包括使用 `{}` 作为占位符（这解决了转义歧义）以及通过截断和报告所需长度来处理缓冲区溢出的方法。该库优先考虑简单性、速度和易于集成，使开发人员可以轻松地扩展和修改它以满足其特定需求。

---

## 18. Mac App 舊貨市場

**原文标题**: The Mac App Flea Market

**原文链接**: [https://blog.jim-nielsen.com/2025/mac-app-flea-market/](https://blog.jim-nielsen.com/2025/mac-app-flea-market/)

文章幽默地批评了Mac App Store上搜索“AI聊天”的结果，将其比作充斥着仿冒商品的跳蚤市场。作者注意到大量类似ChatGPT的应用图标，其中许多是与真正ChatGPT标志几乎相同的黑白仿制品，还有一些则使用了不同的颜色。OpenAI的官方ChatGPT桌面应用甚至没有在Mac App Store上架，突显了误导性仿冒品的问题。

文章还着重指出了这些AI聊天机器人应用程式名称的通用性和重复性，并指出了使用各种“AI”、“聊天”和“机器人”的组合来引诱用户。作者提供了一长串此类富有“创意”名称的应用列表，突显了其荒谬性。

作者将此情况与假冒Nike商品进行类比，以说明这些仿冒应用如何对Mac App Store本身产生负面影响。最终，作者的观点是，Mac App Store充斥着低质量的仿冒AI聊天应用，使得很难找到真正可靠的软件。

---

## 19. 语言模型将数十亿概念压缩到1.2万维度中

**原文标题**: Language Models Pack Billions of Concepts into 12k Dimensions

**原文链接**: [https://nickyoder.com/johnson-lindenstrauss/](https://nickyoder.com/johnson-lindenstrauss/)

本文探讨了语言模型如何将数十亿的概念压缩到相对较小的嵌入空间中（如GPT-3的12,288维）。文章深入研究了Johnson-Lindenstrauss (JL) 引理，该引理保证了高维数据可以投影到低维空间，同时保持距离不变。受3Blue1Brown视频的启发，作者的研究表明，向量压缩的极限比之前假设的要高，尤其是在使用优化的投影而不是随机投影时。

作者发现并纠正了视频实验中使用的损失函数的一个问题，从而更深入地理解了准正交向量在高维空间中是如何排列的。通过实验，他们发现，工程投影实现了远低于JL引理常数C的值，这意味着更大的嵌入容量。

本文重点介绍了JL引理的两个主要应用：高维数据（如电子商务中的客户偏好）的高效计算的降维，以及理解嵌入空间容量，解释了语言模型如何表示数百万概念之间细微的关系。研究表明，当前的嵌入维度可能已经足够，挑战在于优化这些空间内概念的排列。最后，文章强调了数学发现中合作的重要性。

---

## 20. Show HN: 我逆向工程了 macOS，实现了自定义锁屏壁纸

**原文标题**: Show HN: I reverse engineered macOS to allow custom Lock Screen wallpapers

**原文链接**: [https://cindori.com/backdrop](https://cindori.com/backdrop)

此“Show HN”帖子介绍了Backdrop，一款macOS壁纸应用，允许用户在桌面以及独特的锁屏上设置动画或视频壁纸。该应用具有流畅的4K视频播放、多显示器支持和智能电源优化功能。

主要特性和卖点包括：

*   **锁屏支持：** 全球首创功能，允许在macOS锁屏上使用自定义视频壁纸。
*   **4K视频壁纸：** 用于桌面定制的高质量视频背景。
*   **多显示器支持：** 在多个显示器上无缝工作。
*   **Backdrop社区：** 访问数千个社区创建的背景。
*   **自定义创建：** 用户可以使用自己的视频和Rive动画创建自己的背景。
*   **性能优化：** 专为macOS设计，具有硬件加速、节能和Retina显示屏支持。
*   **试用版：** 提供7天试用期，带有水印。购买即可解锁对社区平台的完全访问权限。
*   **Apple iCloud集成：** 社区平台功能需要iCloud登录。
*   **订阅/永久购买：** 用户可以选择订阅或永久许可证进行访问。

该帖子还解决了关于性能影响、电池使用和取消政策的常见问题。最后，它号召大家下载或购买该应用程序，并随时关注新版本。

---

## 21. 在Hubris中创建VGA信号

**原文标题**: Creating a VGA Signal in Hubris

**原文链接**: [https://lasernoises.com/blog/hubris-vga/](https://lasernoises.com/blog/hubris-vga/)

本文详细介绍了作者尝试使用运行 Hubris (Oxide 的嵌入式操作系统) 的 STM32 Nucleo-H753ZI 开发板生成 VGA 信号的过程。目标是通过直接控制 GPIO 引脚，将视频输出到旧的 4:3 VGA 显示器。

最初，作者试图消除 Hubris 的 "sys" 任务以直接控制 GPIO 引脚，担心上下文切换的开销。然而，Hubris 内的内存保护限制迫使重新考虑这种方法。作者成功地使用定时器和脉冲宽度调制 (PWM) 来闪烁 LED，然后生成 VGA 所需的水平同步 (H-Sync) 和垂直同步 (V-Sync) 信号。

在尝试输出纯绿色屏幕时出现了挑战，导致作者探索数模转换器 (DAC) 和直接内存访问 (DMA) 来生成单条重复的线。Hubris 内的内存区域配置问题需要仔细关注，以确保 DMA 功能正常运行。最终，使用 DMA 持续更新 DAC 实现了渐变效果。

然后，作者的目标是实现完整的 2D 图像，这需要使用功能更强大的主直接内存访问控制器 (MDMA)。然而，由于内存区域耗尽，作者重新引入了 "sys" 任务以释放资源。虽然 MDMA 成功地复制了数据，但在撰写本文时尚未实现完全正常工作的帧缓冲区。作者计划继续该项目，并在未来实现一个可用的帧缓冲区。

---

## 22. Meta绕过苹果隐私保护，前雇员称

**原文标题**: Meta bypassed Apple privacy protections, claims former employee

**原文链接**: [https://9to5mac.com/2025/08/21/meta-allegedly-bypassed-apple-privacy-measure-and-fired-employee-who-flagged-it/](https://9to5mac.com/2025/08/21/meta-allegedly-bypassed-apple-privacy-measure-and-fired-employee-who-flagged-it/)

前Meta产品经理萨姆贾尔·普尔卡亚斯塔声称，Meta规避了苹果的应用跟踪透明度（ATT）隐私措施。苹果于2021年推出了ATT，要求用户授权跨应用追踪。普尔卡亚斯塔称，即使苹果用户拒绝跟踪，Meta也找到了识别他们的方法，旨在避免估计每年100亿美元的收入损失。

普尔卡亚斯塔向劳资审裁处提出索赔，声称他因在内部提出对该做法的担忧而被非法解雇。他指控Meta的一个“封闭且隐秘”的团队使用“确定性匹配”来链接用户数据，并在未经同意的情况下跟踪不同网站上的活动，违反了苹果的政策。他还指责Meta虚报广告销售额。

Meta否认有任何不当行为，并声称解雇普尔卡亚斯塔的原因与此无关。审裁处无法立即做出裁决，并安排在今年晚些时候进行全面听证。文章强调，苹果的ATT对Meta的个性化广告模式产生了重大影响，该模式依赖于跨应用跟踪用户。这导致了对变通方法的指控以及针对Meta的隐私侵犯集体诉讼。

---

## 23. 类型类的末日

**原文标题**: Death to type classes

**原文链接**: [https://jappie.me/death-to-type-classes.html](https://jappie.me/death-to-type-classes.html)

本文提出用Backpack模块签名取代Haskell的类型类，以实现更像OCaml的模块系统。作者认为类型类是“谎言”，并提倡使用模块签名而不是类型类来约束值的系统。

其核心思想围绕为`Functor`等概念定义签名，并使用模块实现它们。`Death.Functor.Signature`签名定义了`Functor`类型和`map`函数。然后，诸如`Death.Functor.Maybe`之类的具体模块实现此签名，为`Maybe`提供特定的`Functor`实例。

本文重点介绍了Cabal的Backpack系统如何在构建可执行文件时强制所有签名都有实现，从而解决与缺少模块相关的潜在错误。RebindableSyntax用于指定要用于`do`表示法的`Monad`。

作者提出了一个使用Backpack构建效果系统的例子。签名定义了像`readFile`和`writeFile`这样的效果，不同的模块提供实现（例如，使用IO或状态单子进行测试）。

作者总结说，所提出的基于Backpack的效果系统可以提供诸如单态效果带来的改进的错误消息、潜在的编译时性能提升以及与IO相当的运行时速度等好处。尽管不建议取代类型类，但这种替代方法能够进行探索。

---

## 24. 猪盘骗局的定性分析

**原文标题**: A qualitative analysis of pig-butchering scams

**原文链接**: [https://arxiv.org/abs/2503.20821](https://arxiv.org/abs/2503.20821)

本文题为“你好，是安娜吗？”：剖析“杀猪盘”诈骗的生命周期，对“杀猪盘”诈骗这种融合了情感、投资欺诈和社会工程学的复杂欺诈形式进行了定性分析。作者Rajvardhan Oak和Zubair Shafiq对26名受害者进行了深入的半结构化访谈，以了解诈骗的生命周期及其影响。

研究表明，“杀猪盘”诈骗遵循结构化的生命周期，其特征是情感操纵、分阶段的金融剥削和持续的重新诱导尝试。诈骗者采用诸如建立信任、使用欺诈性金融平台、捏造投资回报以及施加高压等手段，随着时间的推移来利用受害者的信任和财务资源。

该研究强调了受害者所面临的复杂的心理和财务后果，包括更容易受到二次诈骗的影响。基于这些发现，作者为社交媒体和金融平台提出了可行的干预点，以减少此类诈骗的发生率。他们还强调了使用非污名化术语的重要性，以鼓励受害者举报犯罪并寻求帮助。本文已被USENIX SOUPS 2025接收。

---

## 25. 哪个NPM包的版本号最高？

**原文标题**: Which NPM package has the largest version number?

**原文链接**: [https://adamhl.dev/blog/largest-number-in-npm-package/](https://adamhl.dev/blog/largest-number-in-npm-package/)

本文详细介绍了作者寻找具有最大版本号的NPM包的过程。最初，作者在使用NPM API时遇到了挑战，最终通过`replicate.npmjs.com`利用复制API，并从`registry.npmjs.org`获取包元数据。由于NPM注册表的速率限制和规模，作者使用TypeScript脚本分批获取包ID和元数据。

搜索结果显示`latentflip-test`具有一个巨大的版本号，但这被认为是不切实际的。随后，作者改进了标准，以寻找符合语义化版本控制的包，并排除那些版本号超过已发布版本总数的包。作者还手动排除了那些由于自动化或配置错误的发布流程而导致重复或无意义版本递增的包。

最终，“真正的”赢家被确定为`all-the-package-names`，版本号为2.0.2401。文章还根据已发布版本总数和找到的最大版本号，同时考虑符合语义化版本控制并排除已知的“坏”包，展示了包的排名。文章末尾包含了用于执行分析的脚本。由于涉及的数据量巨大，该项目花费了相当长的时间。

---

## 26. Pgstream: 带有DDL变更的Postgres流式逻辑复制

**原文标题**: Pgstream: Postgres streaming logical replication with DDL changes

**原文链接**: [https://github.com/xataio/pgstream](https://github.com/xataio/pgstream)

Pgstream 是一个开源命令行工具和库，用于 Postgres 逻辑复制，关键在于支持 DDL 变更。它可以将数据从 Postgres 流式传输到各种目标，包括 Elasticsearch/OpenSearch、Webhooks 和其他 Postgres 数据库，并且还提供初始和按需快照。主要功能包括列值转换、模块化配置以及具有基于模式的分区的 Kafka 支持，并可扩展到自定义目标。

该工具可以通过 CLI 或作为库使用。可以通过二进制文件、源代码或 Homebrew 安装。配置灵活，允许通过 CLI 标志、YAML 文件或环境变量指定。

Pgstream 提供复制和快照两种模式。`run` 命令启动持续流式传输，并复制 DDL 变更。`snapshot` 命令允许按需数据复制。数据库初始化和清理分别由 `init` 和 `destroy` 命令处理。

文档涵盖架构、配置选项（YAML、环境变量）、示例、快照、转换器、可观察性和 CLI 用法。

虽然 pgstream 提供了强大的功能，但它也存在一些限制，包括仅支持单个 Kafka 主题、仅支持 wal2json，以及对过滤和数据序列化的一些限制。欢迎在 Apache 2.0 许可下贡献代码，并可以通过存储库或 Discord 获得支持。

---

## 27. Show HN: Semlib – 语义数据处理

**原文标题**: Show HN: Semlib – Semantic Data Processing

**原文链接**: [https://github.com/anishathalye/semlib](https://github.com/anishathalye/semlib)

Semlib是一个Python库，旨在通过利用大型语言模型（LLM）的能力，并借助`map`、`reduce`、`sort`和`filter`等熟悉的函数式编程原语，来简化数据处理和分析。其主要创新在于这些操作是使用自然语言描述定义的，而不是传统的代码。 Semlib处理LLM交互的底层复杂性，包括提示、解析、并发、缓存和成本管理。

该库解决了直接将大型数据集输入LLM进行复杂任务的局限性，这通常会导致较低质量的结果。 通过将任务分解为更小的、语义操作，Semlib提供了以下几个优点：

*   **质量：** 通过简化LLM的子任务，实现更高质量的结果。
*   **可行性：** 通过将任务分解为可管理的部分，从而能够处理任意大的数据集。
*   **延迟：** 通过并发执行子任务来减少处理时间。
*   **成本：** 允许使用更小、更便宜的模型来执行更简单的子任务，从而优化总体成本。
*   **安全性：** 方便使用开源的、自托管的模型来处理敏感数据。
*   **灵活性：** 将基于LLM的代码和传统的Python代码无缝集成到同一数据管道中。

Semlib提倡一种结构化的LLM数据处理方法，使开发人员能够构建稳健、高效且经济高效的数据分析管道。 该库以MIT许可证开源。

---

## 28. 文化小说作为反乌托邦

**原文标题**: The Culture novels as a dystopia

**原文链接**: [https://www.boristhebrave.com/2025/09/14/the-culture-novels-as-a-dystopia/](https://www.boristhebrave.com/2025/09/14/the-culture-novels-as-a-dystopia/)

本文对伊恩·M·班克斯的“文化”系列小说提出了一种反主流的观点，认为“文化”并非乌托邦，而是一种微妙压迫的反乌托邦。作者通过“对抗性阅读”挑战了普遍的看法，质疑了“文化”公民普遍接受的叙事。

中心论点是，“文化”表面上田园诗般的社会是通过操纵而非真正的自由实现的。“文化”中的人类异常同质化，缺乏如此规模的人口应有的多样性和偏差。作者认为，这很可能是由于基因工程或“心智”使用的复杂宣传来控制行为和强制顺从。人口增长的缺乏或对“效用怪兽”式改造的追求被认为是受控选择的证据。

尽管“心智”声称仁慈，但也受到了审视。它们偶尔出现的流氓行为以及维持它们之间秩序所需的武力表明缺乏真正的统一。本文认为，“文化”受限于其创始“心智”的价值体系，导致了不一致和停滞。

“特殊情况部” (SC) 被认为是宣传，作者认为“心智”完全可以通过不那么引人注目的手段来实现其目标。总体结论是，“文化”将其公民视为宠物，提供物质上的舒适，但扼杀了自决和真正的影响力。作者警告说，不要盲目地接受技术进步的承诺就足以实现真正的乌托邦，并认为正义和自决同样重要。

---

## 29. 并非所有浏览器都执行撤销检查。

**原文标题**: Not all browsers perform revocation checking

**原文链接**: [https://revoked-isrgrootx1.letsencrypt.org/](https://revoked-isrgrootx1.letsencrypt.org/)

本文强调了浏览器安全的一个关键点：并非所有浏览器都会持续执行证书吊销检查。该页面本身旨在演示这一点，它使用了一个由 Let's Encrypt 颁发、链接回其 ISRG Root X1 证书的已吊销证书。作者明确警告说，由于不同浏览器对吊销检查机制的实施和支持程度不同，因此吊销可能并非在所有浏览器中都可见。本质上，本文作为一个实际例子，说明了网络浏览中潜在的安全漏洞。最后，它鼓励读者通过贡献、社区支持和赞助参与 Let's Encrypt 项目。

---

## 30. 葡萄藤蔓可以转化为可分解的塑料样材料。

**原文标题**: Grapevine canes can be converted into plastic-like material that will decompose

**原文链接**: [https://www.sdstate.edu/news/2025/08/can-grapevines-help-slow-plastic-waste-problem](https://www.sdstate.edu/news/2025/08/can-grapevines-help-slow-plastic-waste-problem)

利用葡萄藤蔓解决塑料废弃物问题：一项有前景的方案

本文重点介绍了一种利用葡萄藤蔓解决塑料废弃物问题的有前景的方案。由 Srinivas Janaswamy 领导的南达科他州立大学的研究人员发现，从葡萄藤蔓中提取的纤维素可以转化为一种类似塑料的材料，这种材料比传统塑料更坚固且更具生物降解性。

这项研究的动机源于对塑料污染日益增长的担忧，包括海洋中塑料废弃物的积累和环境中微塑料的扩散。Janaswamy 与 Anne Fennell 合作，认识到葡萄藤蔓作为一种容易获得的农业副产品，具有作为纤维素来源的潜力。Fennell 建议，由于农民每年都会修剪藤蔓，因此这些藤蔓可以用来制造薄膜，而不是被堆肥或焚烧。

由此产生的葡萄藤蔓衍生薄膜是透明的、坚固的（比塑料袋更坚固），并且在土壤中可在 17 天内分解，不留下有害残留物。这使得它们成为一次性包装，特别是塑料袋的一种有前景的替代品，塑料袋是塑料废弃物的主要来源。该研究团队遵循已发布的协议来开发薄膜，包括干燥和研磨藤蔓并提取纤维素残留物。然后将残留物溶解并浇铸到玻璃板上以制造薄膜。

Janaswamy 的工作代表着在开发可持续和环保的包装材料方面迈出了重要一步，解决了废物管理和环境问题。该研究由美国农业部国家食品和农业研究所以及国家科学基金会资助。

---

## 31. 美国宇航局“守护者”海啸探测技术实时捕捉海浪

**原文标题**: NASA's Guardian Tsunami Detection Tech Catches Wave in Real Time

**原文链接**: [https://www.jpl.nasa.gov/news/nasas-guardian-tsunami-detection-tech-catches-wave-in-real-time/](https://www.jpl.nasa.gov/news/nasas-guardian-tsunami-detection-tech-catches-wave-in-real-time/)

NASA的GUARDIAN实验系统于七月末在俄罗斯沿海探测到一次海啸，该海啸由8.8级地震引发，比传统验潮仪提前了最多45分钟。GUARDIAN（全球导航卫星系统高层大气实时灾害信息与警报网络）利用海啸对大气层的影响导致电离层内无线电信号的扭曲来识别和追踪这些海浪。它可以在接收到数据后约10分钟内提供海啸存在的快照，并在最初地震发生后20分钟内向专家发出警报。

该系统旨在通过提供更快的探测和确认海啸的产生来补充现有的海啸早期预警系统，填补深海压力传感器局限性所留下的空白。GUARDIAN通过近乎实时地从太空感知海面运动，提供了一种独特的视角，且不受海啸起因的影响。该系统使用来自全球350多个全球导航卫星系统地面站的数据。

在堪察加事件中，新部署的人工智能和消息传递系统成功地标记了大气畸变，证明了该技术提供关键早期预警的潜力。该技术可能为沿海社区提供长达1小时20分钟的疏散时间。

专家强调，GUARDIAN的开放数据访问和全球覆盖对于有效海啸预警系统至关重要，超越了国界，从而保护脆弱的海岸线。

---

## 32. SaaS退款乱象

**原文标题**: The madness of SaaS chargebacks

**原文链接**: [https://medium.com/@citizenblr/the-10-payment-that-cost-me-43-95-the-madness-of-saas-chargebacks-5c308d5a49cc](https://medium.com/@citizenblr/the-10-payment-that-cost-me-43-95-the-madness-of-saas-chargebacks-5c308d5a49cc)

文章《SaaS退款请求之疯狂》详细描述了作者因一笔看似简单的10美元退款请求而产生的令人沮丧的经历，最终为此付出了更多的时间和资源。他强调了退款请求对小型SaaS企业产生的巨大影响。

作者描述了一位客户如何针对一笔有效的10美元SaaS订阅付款发起退款请求。尽管作者拥有服务交付的证据（使用日志等），但他还是被迫花费数小时收集文件并回复退款请求。他强调，与处理退款请求相关的管理费用，包括直接成本和他时间的价值，远远超过了10美元的金额。

文章批评了客户发起退款请求的便捷性，有时甚至是欺诈性的，以及小企业在反驳这些请求时面临的困难。他认为，目前的系统严重偏袒客户，通常不考虑他们索赔的合法性。作者质疑花费可能数百美元的管理时间来追回少量收入的逻辑，突出了退款请求系统在SaaS企业应用中的低效率和不公平性。他最后建议，需要一个更好、更平衡的系统，考虑到SaaS公司在处理退款请求时面临的独特挑战。

---

## 33. 人类作者一直都在使用长破折号。

**原文标题**: Human writers have always used the em dash

**原文链接**: [https://www.theringer.com/2025/08/20/pop-culture/em-dash-use-ai-artificial-intelligence-chatgpt-google-gemini](https://www.theringer.com/2025/08/20/pop-culture/em-dash-use-ai-artificial-intelligence-chatgpt-google-gemini)

布莱恩·菲利普斯撰文为破折号辩护，反驳了其使用标志着人工智能写作的指责。菲利普斯认为这种说法毫无根据，且对人类表达有害。他驳斥了人工智能过度使用破折号的观点，指出如果人工智能使用破折号，那是因为人工智能的训练数据来自有效使用破折号的人类作者。

菲利普斯认为，破折号是一种有价值的标点符号，对于捕捉人类思想的细微流动至关重要。它允许作者扩展想法、创造停顿，并以反映人类认知复杂性的方式连接思想。他将破折号视为一种用于精巧写作的工具，是古老修辞风格的现代演变。

文章警告说，阻止破折号的使用会扼杀创造力，并限制表达复杂思想的能力。菲利普斯批评了语法极简主义的趋势，认为这会导致思想的简化。他支持将破折号作为一种抵制这种简化并保持人类表达丰富性的手段。

最终，菲利普斯主张拥抱破折号，将其视为一种独特的人类标点符号，应该被赞扬，而不是因为害怕被误认为是机器而避之唯恐不及。他坚持认为，破折号反映思想复杂性的能力使其对于真正的、非机器人式的写作至关重要。

---

## 34. 科里·多克托罗：“半人马”和“逆向半人马”

**原文标题**: Cory Doctorow: "centaurs" and "reverse-centaurs"

**原文链接**: [https://locusmag.com/2025/09/commentary-cory-doctorow-reverse-centaurs/](https://locusmag.com/2025/09/commentary-cory-doctorow-reverse-centaurs/)

科里·多克托罗在他的文章中论述道，围绕技术（尤其是人工智能）的社会安排比技术本身更重要。他用“人头马”和“反向人头马”的比喻来说明这一点。“人头马”是指人类借助技术的力量更有效地完成任务，正如多克托罗在使用人工智能转录播客时所体验到的。相反，“反向人头马”是指人类被迫以机器的速度工作，往往承受着巨大的压力且几乎没有支持。

多克托罗用一个自由职业者的例子来说明“反向人头马”的概念，这位自由职业者使用人工智能为一家报纸创建暑期阅读清单，结果出现了大量错误和不存在的书籍。多克托罗认为，这位自由职业者本质上被用作人工智能错误的“责任承担者”，取代了一个由实习生、记者和事实核查员组成的团队的工作。

多克托罗批评了人工智能推广者所宣扬的观点，他们声称利用人工智能的唯一方法就是解雇工人并迫使剩余员工以不可持续的速度工作。他否定了这种观点，并断言我们没有义务安排社会来确保人工智能投资的盈利能力。相反，他建议社会影响以及技术影响人类劳动的方式应优先于利润动机。他总结说，“街头自有妙用”，暗示个人将会找到将人工智能融入生活的替代且更好的方法。

---

## 35. PythonBPF – 使用纯 Python 编写 eBPF 程序

**原文标题**: PythonBPF – Writing eBPF Programs in Pure Python

**原文链接**: [https://xeon.me/gnome/pythonbpf/](https://xeon.me/gnome/pythonbpf/)

PythonBPF 是一个新的开源 Python 库，允许开发者直接用 Python 编写 eBPF (扩展伯克利包过滤) 程序，并将其编译成实际的目标文件。这消除了像 bcc 这样的库中常见的将 C 代码嵌入 Python 字符串的需要。

在 PythonBPF 出现之前，用 Python 编写 eBPF 程序涉及到使用多行 C 字符串，这缺乏 Python 开发工具的适当支持。虽然 C 语言通过 clang 编译提供了生产就绪的选项，但这需要熟悉 C 语言和内核头文件。

PythonBPF 通过允许使用原生 Python 语法创建 eBPF 程序来解决这个问题，利用装饰器来定义 BPF 函数、映射、全局变量和节。它利用 Python `ast` 模块生成抽象语法树，然后使用来自 Numba 的 `llvmlite` 发射 LLVM 中间表示 (IR)。然后，使用 `llc` 将此 IR 编译为 eBPF 目标文件。

支持的关键特性包括控制流、哈希映射、二进制操作、用于映射操作的辅助函数、内核跟踪打印、时间戳辅助函数和全局变量。该库旨在提供一种生产质量的替代方案，以取代现有方法，扩展 C 和 Rust (aya) 之外的选择。尽管目前正在开发中且“hacky”，但 PythonBPF 提供了一种简化且更符合 Python 风格的 eBPF 开发方法。

---

## 36. 杰夫·拉斯金的死胡同与对人道化电脑的探索

**原文标题**: Jef Raskin's cul-de-sac and the quest for the humane computer

**原文链接**: [https://arstechnica.com/gadgets/2025/09/jef-raskins-cul-de-sac-and-the-quest-for-the-humane-computer/](https://arstechnica.com/gadgets/2025/09/jef-raskins-cul-de-sac-and-the-quest-for-the-humane-computer/)

本文探讨了杰夫·拉斯金对人性化计算机界面的愿景，将其与Macintosh的演变进行了对比，并详细介绍了他的后续项目Swyft。作为Macintosh项目的创始人，拉斯金认为计算机应优先考虑功能和认知局限性，而不是复杂的视觉隐喻。他最初设想Macintosh是一款低成本、独立的计算机，专注于文本和键盘输入，并拒绝使用鼠标。

然而，在史蒂夫·乔布斯接管该项目后，Macintosh转向了带有鼠标的图形用户界面，导致拉斯金离开了苹果公司。拉斯金随后创立了Information Appliance, Inc.，开发Swyft，这是一款一体机，具有围绕单一、统一文档工作区构建的独特界面。

Swyft使用LEAP键进行导航，无需鼠标或复杂的文件系统。该系统设计为始终开启且可立即访问，将用户的整个工作区冻结到软盘上，以便无缝恢复。虽然大约制作了60个原型，但IAI将该设计授权给了佳能，并交给了他们的电子打字机部门，最终扼杀了该产品的进一步开发。在合作之前，IAI发布了SwyftCard，这是一款Apple IIe扩展卡，用于实现Swyft的部分技术。

---

## 37. 丹麦司法部长称加密通讯为虚假的公民自由。

**原文标题**: Denmark's Justice Minister calls encrypted messaging a false civil liberty

**原文链接**: [https://mastodon.social/@chatcontrol/115204439983078498](https://mastodon.social/@chatcontrol/115204439983078498)

此 Mastodon 帖子表明丹麦司法部长认为加密通信是一种“虚假的公民自由”。虽然提供的背景信息非常有限，但暗示该部长认为强大的加密技术，尤其是在即时通讯应用中，可能对执法和安全工作不利。“Fight Chat Control”可能指的是与监管或限制端到端加密通信使用相关的持续辩论和立法努力，可能旨在打击儿童性虐待材料或其他非法活动。该帖子本身似乎强调了部长在此次辩论中的立场。在没有更多背景信息的情况下，无法了解该部长立场背后的全部原因或正在倡导的具体政策。该帖子只是标记了部长颇具争议的观点。

---

## 38. 一套流畅的、由fzf驱动的systemctl shell别名和函数

**原文标题**: A set of smooth, fzf-powered shell aliases&functions for systemctl

**原文链接**: [https://silverrainz.me/blog/2025-09-systemd-fzf-aliases.html](https://silverrainz.me/blog/2025-09-systemd-fzf-aliases.html)

本文介绍了一组 shell 别名和函数，旨在利用模糊查找器 `fzf` 来简化 systemd 服务管理。作者的动机源于重复键入冗长的 `systemctl` 命令以及缓慢的 shell 补全效率低下，尤其是在资源受限的设备上。他们发现 TUI 工具 `sysz` 具有启发性，但不适合频繁的单命令操作。

该解决方案包括 `systemctl` 和 `journalctl` 的简短别名 (`s`、`sj`、`u`、`uj`)，以及利用 `fzf` 模糊搜索 systemd 单元的函数。核心函数 `_sysls` 合并 `systemctl list-units` 和 `systemctl list-unit-files` 的输出，使用 `column` 将其格式化为表格，并将其提供给 `fzf` 以进行交互式选择，同时还提供状态预览。

为了增强错误处理，本文介绍了一种模式，如 `s start foo.service && s status $_ || sj -xeu $_`，如果启动命令失败，该模式会自动显示服务状态或日志。为了提高可重复性，启动的命令会被推送到 shell 历史记录中。

最后，为了避免使用 `--system` 和 `--user` 标志重复定义 `start`、`stop` 和 `restart` 函数，该脚本使用数组和中央执行函数 `_sysexec` 动态生成这些函数。这种方法允许用户键入诸如 `sstart` 之类的命令，模糊选择服务，然后启动该服务，其中包含错误处理和命令历史记录更新。作者发现这种方法显着提高了生产力。

---

## 39. 政治定义的过时 (1991)

**原文标题**: The Obsolescence of Political Definitions (1991)

**原文链接**: [http://vmchale.com/static/serve/taxonomy.html](http://vmchale.com/static/serve/taxonomy.html)

孔迪利斯认为，诸如“保守主义”、“自由主义”和“社会主义”等传统政治定义已经过时且含糊不清，失去了其最初的历史意义，尤其是在冷战之后。他指出了这些术语在使用上的不一致性，并举例说明了“保守派”支持相互对立的政策。

他追溯了这些定义的历史演变，指出它们最初代表了1848年左右的不同社会选择（贵族、资产阶级、无产阶级）。然而，随着贵族和资产阶级的融合，以及资本主义的活力，界限变得模糊。“保守主义”主要被定义为反对左派，而不是捍卫传统的等级秩序。

反过来，自由主义者也采用了“保守主义”来将自己与自由主义的平等主义解释区分开来。社会主义也分裂了，由于布尔什维克革命而分裂，并被民族主义独裁政权采用作为标签。

冷战进一步混淆了局势，“自由主义”被等同于反极权主义、自由资本主义和民主。“保守主义”在反共言论中，捍卫着永恒的价值观。孔迪利斯认为，在后冷战时代，鉴于西方在技术和社会进步方面的发展，左派对西方作为“保守派”的批判是站不住脚的。

虽然西方表面上“赢得”了冷战，但这并不是真正的保守主义或自由主义的胜利，传统的定义已经失去了其实质意义。

---

## 40. 沙箱化浏览器AI代理

**原文标题**: Sandboxing Browser AI Agents

**原文链接**: [https://www.earlence.com/blog.html#/post/cellmate](https://www.earlence.com/blog.html#/post/cellmate)

好的，我已阅读了来自所提供URL的文章《沙盒化浏览器AI代理》。以下是一个简明扼要的总结：

该文章讨论了安全部署直接在Web浏览器中运行的AI代理所面临的挑战和潜在解决方案。 它强调了授予AI代理无限制访问用户浏览器环境的风险，包括数据泄露、恶意活动和意外行为的可能性。

作者介绍了“Cellmate”，一种针对基于浏览器的AI代理的沙盒架构方案。 Cellmate旨在通过创建一个受限的执行环境来降低这些风险，该环境限制了代理对敏感浏览器功能和用户数据的访问。

Cellmate的关键要素包括：

*   **隔离的执行环境：** 代理在严格控制的Web Worker或类似容器中运行，限制了它们对主浏览器上下文的直接访问。

*   **API介导的通信：** 代理与外部世界（例如，访问网站、与DOM交互）之间的通信通过精心设计的API进行介导。 该API强制执行访问控制并清理输入/输出，以防止漏洞利用。

*   **资源限制：** 对代理的资源消耗（CPU、内存、网络）施加限制，以防止拒绝服务攻击或浏览器性能下降。

*   **权限系统：** 细粒度的权限系统允许用户仅在必要时授予代理特定的功能，从而最大限度地减少滥用的可能性。

文章认为，沙盒化对于负责任地开发和部署强大的基于浏览器的AI代理至关重要。 Cellmate代表了朝着为这些代理构建安全和值得信赖的生态系统迈出的一步。 它承认仍然存在挑战，但强调在开发周期的早期解决安全问题的重要性。 作者鼓励在该领域进行进一步的研究和合作。

---

## 41. 空气污染如何影响你的大脑？

**原文标题**: How does air pollution impact your brain?

**原文链接**: [https://neurofrontiers.blog/how-does-air-pollution-impact-your-brain/](https://neurofrontiers.blog/how-does-air-pollution-impact-your-brain/)

无法访问文章链接。

---

## 42. 星图 - 实时3D空间可视化

**原文标题**: Celestia – Real-time 3D visualization of space

**原文链接**: [https://celestiaproject.space/](https://celestiaproject.space/)

本文描述了在一个网站（可能与“Celestia - 空间实时3D可视化”相关）上实施的Anubis系统，以保护其免受AI公司过度抓取。抓取行为可能导致网站崩溃并阻止合法用户访问。

Anubis使用类似于Hashcash的工作量证明机制。这要求用户执行少量计算以证明他们不是机器人。虽然对单个用户而言微不足道，但累积成本使得大规模抓取更加困难。

本文强调Anubis是一个临时解决方案。网站管理员正在积极研究更复杂的方法来识别和阻止用于抓取的无头浏览器，例如分析它们的字体渲染。最终目标是消除合法用户对工作量证明页面的需求。

本文还指出，Anubis依赖于现代JavaScript特性，这意味着JShelter等插件可能会干扰其功能，需要禁用才能使网站正常工作。最后，本文承认给用户带来的不便，并提到由于不断变化的在线环境以及对防止AI抓取的需要，正在开发一种无JavaScript解决方案。

---

## 43. 展示HN: 基于CachyOS的Omarchy

**原文标题**: Show HN: Omarchy on CachyOS

**原文链接**: [https://github.com/mroboff/omarchy-on-cachyos](https://github.com/mroboff/omarchy-on-cachyos)

这个"Show HN"帖子介绍了一个脚本，用于在CachyOS（一个性能优化的Arch Linux发行版）之上安装基于Hyprland的个人定制桌面环境Omarchy。该脚本自动化了克隆Omarchy仓库、调整CachyOS的安装脚本以及启动Omarchy安装的过程。

重要的是，该脚本**不安装CachyOS本身**，也不处理分区、引导加载程序设置、显卡驱动或显示管理器安装；这些必须在CachyOS安装期间预先配置。

该脚本优先考虑CachyOS和Omarchy之间的无缝融合，尽量减少对其默认配置之外的修改。它通过选择Yay作为AUR助手（Omarchy默认）、保留Fish作为默认shell（CachyOS默认）、保留Tealdeer TLDR实现（CachyOS默认）以及确保Mise在Fish shell中正常工作来解决潜在的冲突。该脚本假定显示管理器的存在，并将全盘加密留给用户的CachyOS安装选择。

**先决条件包括：**带有Snapper文件系统的BTRFS、Fish shell以及最小化或Hyprland CachyOS桌面环境（无GNOME/KDE）。NVIDIA用户应通过CachyOS安装他们的驱动程序。

安装过程包括克隆仓库，导航到`bin`目录，使`install.sh`可执行，并运行它。作者强调这是面向有经验的Arch Linux用户的，并包含免责声明，敦促用户备份他们的数据。欢迎通过fork、创建特性分支、提交更改、推送到fork以及打开pull request来进行贡献。

---

## 44. 适合新手的好议题——社会影响力和开源项目仓库

**原文标题**: For Good First Issue – A repository of social impact and open source projects

**原文链接**: [https://forgoodfirstissue.github.com/](https://forgoodfirstissue.github.com/)

标题“适合新手参与的项目”的网页，是一个精选的开源项目仓库，专注于为数字公共产品（DPGs）贡献力量，并最终创造更美好的未来。它鼓励开发者将他们的技能贡献给这些项目，这些项目旨在解决气候变化和世界饥饿等关键的全球问题，并通过“每次提交一点贡献”来推动积极影响。

该页面允许用户浏览 DPG 仓库，并按编程语言和可持续发展目标（SDG）进行筛选。它列出了几个开源项目，每个项目都有简要描述、关于未解决问题数量的信息（所有列出的项目均超过 10 个）、使用的主要编程语言、任何相关标签（如特定的 SDG）以及上次活动日期。

精选项目示例包括：

*   **Decidim:** 一个参与式民主框架。
*   **ODK Central & Collect:** 数据收集工具，常用于充满挑战的环境。
*   **Querido Diario:** 一个使巴西政府公报易于访问的项目。
*   **Cboard:** 一种增强和替代沟通系统。
*   **OpenFn/Lightning:** 一个用于管理复杂工作流程自动化的平台。

该仓库为希望为符合联合国可持续发展目标的、具有影响力的开源项目做出贡献的开发者提供了一个清晰的切入点。

---

## 45. 谷歌将关闭其Airtable竞品Tables。

**原文标题**: Google is shutting down Tables, its Airtable rival

**原文链接**: [https://techcrunch.com/2025/09/11/google-is-shutting-down-tables-its-airtable-rival/](https://techcrunch.com/2025/09/11/google-is-shutting-down-tables-its-airtable-rival/)

谷歌将于2025年12月16日关闭其工作跟踪工具Tables，该产品是Airtable的竞争对手。建议用户将其数据迁移到Google Sheets或AppSheet。Tables于2020年由谷歌的Area 120孵化器推出，旨在通过自动化简化项目跟踪，并于2021年成为正式的Google Cloud产品，面向项目管理和CRM等多种用例。

关闭Tables的决定是在2022年重组之后做出的，该重组严重影响了Area 120，导致项目取消和裁员。虽然Tables在最初的裁减中幸存下来，但最终还是在Google Cloud下Google Workspace团队中面临终结。

谷歌鼓励用户将数据导出到Google Sheets以进行基本的工作流程管理，或利用新的迁移工具将数据导入到AppSheet，该工具保留格式并允许使用自动化和Workspace集成来管理工作流程。Tables背后的团队在AppSheet中创建了一种新的数据体验，于2023年6月推出，使用户能够为自定义应用程序和工作流程构建数据模型。

---

## 46. 在生机勃勃的天空下：与夜重逢 (2022)

**原文标题**: In the Land of Living Skies: Reacquainting ourselves with the night (2022)

**原文链接**: [https://harpers.org/archive/2022/05/in-the-land-of-living-skies-reacquainting-ourselves-with-the-night/](https://harpers.org/archive/2022/05/in-the-land-of-living-skies-reacquainting-ourselves-with-the-night/)

苏珊娜·肖勒的散文《在活天之国：重识黑夜》探讨了日益严重的光污染及其生态和文化后果。肖勒叙述了她在萨斯喀彻温省里贾纳生活时对黑暗的个人迷恋，以及她最终渴望体验“真正的”——格拉斯兰国家公园未经污染的黑暗，这是一个经过认证的暗夜保护区。

这篇散文强调了全球人工照明的惊人增长，导致了生态破坏（影响鸟类、昆虫和海龟）和人类健康问题（如心血管疾病、肥胖和抑郁症）。除了生理影响之外，肖勒认为，光污染模糊了我们与夜空的联系，而夜空是人类文化、历史和我们对宇宙理解的重要组成部分。

她将国际暗夜协会的保护工作与加拿大更严格的暗夜指定进行了对比，强调了保护自然黑暗的重要性。肖勒深入研究了关于光明与黑暗的哲学和神话视角，揭示了黑暗不仅仅是光明的缺失，而且具有自身的意义，代表着神秘、潜力和另一种真理。她即将前往格拉斯兰的旅程源于对某种基本而永恒事物的渴望，沉浸在一种可能提供清晰感和与世界更深层次联系的黑暗中。她试图重新发现，如果重新夺回黑暗，它可能会揭示什么。

---

## 47. USB-A不会消失，别再移除这个接口了

**原文标题**: USB-A isn't going anywhere, so stop removing the port

**原文链接**: [https://www.pocket-lint.com/usb-a-isnt-going-anywhere/](https://www.pocket-lint.com/usb-a-isnt-going-anywhere/)

本文认为，虽然USB-C因其速度、正反插拔性和多功能性而必然是连接的未来，但制造商过早地在笔记本电脑上淘汰USB-A端口。作者认为，由于许多外围设备（如鼠标、适配器和外部驱动器）继续使用USB-A，因此它仍然至关重要。移除这些端口迫使用户依赖适配器，从而增加了成本和不便。

文章追溯了USB-A的历史，强调了它对PC连接的革命性影响，取代了PS/2、串行和并行等旧端口。它承认USB-C的优势，包括更快的速度和传输显示信号的能力。

然而，作者批评了苹果和戴尔等品牌，因为它们为了优先考虑轻薄设计而限制了USB端口的数量，特别是USB-A端口。他们指出，即使在昂贵的笔记本电脑上，可用的端口通常也不足以连接必要的设备。文章认为，淘汰USB-A为时尚早，特别是当带有USB-A连接的新外围设备仍在生产和广泛使用时。作者认为，制造商应该优先考虑用户需求，在笔记本电脑上包含USB-A和USB-C端口的合理组合，而不是强迫升级和购买适配器。结论是，制造商通过过早地移除过多的USB-A端口，将利润置于用户体验之上。

---

## 48. 电影海报主导颜色是什么？为什么？

**原文标题**: Which colours dominate movie posters and why?

**原文链接**: [https://stephenfollows.com/p/which-colours-dominate-movie-posters-and-why](https://stephenfollows.com/p/which-colours-dominate-movie-posters-and-why)

本文分析了过去一百年间58,687张电影海报中使用的主要颜色，并探讨了颜色选择如何反映电影类型和观众期望。文章首先量化海报的“色彩鲜艳度”和“亮度对比度”，揭示了色彩强度随时间推移而降低以及特定类型电影的视觉风格趋势。悬疑、惊悚和恐怖电影海报偏爱低亮度和对比度，而喜剧、家庭电影和音乐剧则使用高色彩和对比度。

接下来，分析深入到各个颜色。橙色是最常用的“颜色”，通常与蓝色搭配，象征温暖、亲和力以及高风险冲突（尤其是在动作、科幻和冒险电影中）。红色用于表示危险、激情或紧迫感，尤其是在恐怖、动作、爱情和喜剧电影中，但其使用在不同类型之间几乎没有差异。白色是一种灵活的背景色，在浪漫喜剧中传达新鲜感，在恐怖电影中传达无菌感，在科幻电影中传达极简主义。蓝色在海洋、天空和霓虹科技等场景中很突出，尤其是在动画、家庭电影、科幻和惊悚片中。棕色将故事置于历史、战争和衰败之中。绿色可以表示郁郁葱葱的自然环境或有毒的不安感。紫色用于表示非主流的事物。粉色带有浓厚的文化色彩，在爱情片中象征爱意，在青少年电影中象征青春，在恐怖片中象征令人不安的甜蜜。

文章强调了电影海报中色彩的战略性使用，旨在快速传达电影类型并唤起观众特定的情感反应，这得益于营销团队在过去一个世纪中的不断适应。

---

## 49. 贝蒂妙厨通过缩小包装盒来减少食谱用量。

**原文标题**: Betty Crocker broke recipes by shrinking boxes

**原文链接**: [https://www.cubbyathome.com/boxed-cake-mix-sizes-have-shrunk-80045058](https://www.cubbyathome.com/boxed-cake-mix-sizes-have-shrunk-80045058)

文章“贝蒂妙厨通过缩小包装盒来破坏食谱”讨论了盒装蛋糕粉（尤其是贝蒂妙厨）的尺寸如何随着时间的推移而缩小，从而影响了食谱的成功率。作者指出，较早的食谱通常要求使用“一盒蛋糕粉”，但没有指定重量。由于包装盒尺寸减小，在较早的食谱中使用现代的、较小的包装盒可能会导致不令人满意的结果，因为配料比例被打乱了。

具体来说，蛋糕粉包装盒已经从过去的超过18盎司缩小到今天的约15.25盎司。这种“缩水式通胀”虽然看起来微不足道，但可能会导致成品的显着差异。作者强调了蛋糕更干燥、糖霜与蛋糕的比例不正确以及整体口感发生变化等问题。

文章强调，为了避免问题，烘焙师应密切关注食谱中要求的蛋糕粉重量，而不是仅仅依赖“一盒”。在使用较早的食谱时，可能需要用额外的配料（如面粉或糖）来补充现代的、较小的包装盒，以达到预期的稠度和风味。这篇文章是对产品尺寸变化对烘焙结果产生微妙但重大影响的警示。

---

## 50. 分析苹果M1的内存排序模型

**原文标题**: Analyzing the memory ordering models of the Apple M1

**原文链接**: [https://www.sciencedirect.com/science/article/pii/S1383762124000390](https://www.sciencedirect.com/science/article/pii/S1383762124000390)

无法访问文章链接。

---

## 51. 网站托管在一次性电子烟上

**原文标题**: Website is hosted on a disposable vape

**原文链接**: [http://ewaste.fka.wtf/](http://ewaste.fka.wtf/)

无法访问文章链接。

---

## 52. 我没有iPhone的第一年

**原文标题**: My First Year Without an iPhone

**原文链接**: [https://ktklp.substack.com/p/my-first-year-without-an-iphone](https://ktklp.substack.com/p/my-first-year-without-an-iphone)

无法访问文章链接。

---

## 53. OCSP服务已停止服务

**原文标题**: OCSP Service Has Reached End of Life

**原文链接**: [https://letsencrypt.org/2025/08/06/ocsp-service-has-reached-end-of-life](https://letsencrypt.org/2025/08/06/ocsp-service-has-reached-end-of-life)

Let's Encrypt 将于 2025 年 8 月 6 日正式停止在线证书状态协议 (OCSP) 服务，该公告已于 2024 年 12 月发布。他们早在 90 天前就已停止在证书中包含 OCSP URL，以确保所有包含这些 URL 的证书均已过期。今后，撤销信息将仅通过证书撤销列表 (CRL) 分发。

此决定的主要原因是隐私。OCSP 会将用户浏览活动暴露给证书颁发机构 (CA)，因为每个请求都会从特定 IP 地址揭示用户正在访问哪个网站。虽然 Let's Encrypt 并非有意保留此数据，但意外保留或法律强制收集它的可能性仍然令人担忧。CRL 不存在此隐私问题。

此外，简化 Let's Encrypt 的基础设施对于长期的合规性、可靠性和效率至关重要。运营 OCSP 服务消耗了大量资源，现在可以将这些资源分配给其他关键领域。在 CRL 支持建立后，OCSP 变得多余。

本文重点介绍了 Let's Encrypt 的 OCSP 服务的巨大规模，每月处理约 3400 亿个请求（通过 CDN 每秒 14 万个请求）。Let's Encrypt 感谢 Akamai 十年来为 OCSP 捐赠 CDN 服务。

---

## 54. 学习透镜模糊场

**原文标题**: Learning Lens Blur Fields

**原文链接**: [https://blur-fields.github.io/](https://blur-fields.github.io/)

本文介绍了一种新颖的镜头模糊场方法，用于建模镜头系统中固有的复杂光学模糊。其核心思想是将镜头的点扩散函数（PSF）表示为一个高维神经网络（MLP），该网络捕获图像平面位置、焦点设置和深度上的变化。这种表示考虑了散焦、衍射、像差、像素滤色片和微透镜，从而有效地创建了一个设备特定的“模糊签名”。

作者提出了一种获取这些模糊场的实用方法。该过程包括使用简单的设置捕获监视器图案的焦距堆叠，并使用非盲反卷积训练MLP。这种相对轻量级的流程可以快速生成连续的PSF模型。

镜头模糊场的关键应用包括：基于光学器件的细微差异区分“相同”的设备（例如，智能手机），渲染逼真的设备特定景深效果，以及通过结合设备的独特模糊特性来改善图像恢复。本文重点介绍了使用不同的模糊签名区分相同型号iPhone的能力。

最后，作者宣布发布一个新数据集，其中包含智能手机和单反镜头的5D和6D镜头模糊场，以及训练捕获，以促进该领域的进一步研究。

---

## 55. Show HN: Dagger.js – 无需构建，纯运行时 JavaScript 微框架

**原文标题**: Show HN: Dagger.js – A buildless, runtime-only JavaScript micro-framework

**原文链接**: [https://daggerjs.org](https://daggerjs.org)

无法访问文章链接。

---

## 56. 我们为何陷入恶性循环

**原文标题**: Why We Spiral

**原文链接**: [https://behavioralscientist.org/why-we-spiral/](https://behavioralscientist.org/why-we-spiral/)

格雷戈里·沃尔顿的《为何我们陷入恶性循环》探讨了自我挫败思维模式背后的机制以及如何扭转它们。文章提出，恶性循环始于一个触发事件，该事件引发了关于个人身份、归属感或能力的根本性问题。这些通常潜伏的“核心问题”会被一个“糟糕”的事件（例如，老板的尖刻评论）激活。

这进而影响我们的“构建”，即我们如何解释周围的世界。当这些核心问题未解决时，我们倾向于对模糊的证据做出负面解释，从而证实我们悲观的假设。这受到证实偏差的推动。

最后，“钙化”发生，因为这些消极的想法和感受通过我们自己的行为变得根深蒂固。 例如，基于消极假设采取行动只会加强最初的焦虑，并创造一个自我实现的预言。

沃尔顿认为，这些恶性循环并非不可避免。 我们可以通过理解起作用的核心问题并提供“明智的干预”来打破它们，这些干预为这些问题提供替代的、积极的答案。 通过认识到我们的解释如何塑造我们的现实，并通过有意识地选择更具建设性的回应，我们可以启动通往幸福、成功和繁荣的良性循环。 关键是解决驱动负面解释的潜在焦虑，并在循环钙化之前打破它。 作者用错过In-N-Out的轶事来说明微小的事实如何引发更大的焦虑。

---

## 57. 从零开始编写操作系统内核

**原文标题**: Writing an operating system kernel from scratch

**原文链接**: [https://popovicu.com/posts/writing-an-operating-system-kernel-from-scratch/](https://popovicu.com/posts/writing-an-operating-system-kernel-from-scratch/)

本文详细介绍了使用 Zig 语言在 RISC-V 架构上实现的一个极简时间分片操作系统内核，重点关注虚拟化、线程以及内核/用户空间分离等概念。

作者旨在提供一个底层系统软件的实践案例，尤其对计算机体系结构专业的学生有益。该项目实现了一个单内核 (unikernel)，应用程序代码直接与内核链接。它利用了 RISC-V 的分层权限模型（M、S 和 U 模式），内核在 S 模式下运行，用户线程在 U 模式下运行，并使用 SBI 层 (OpenSBI) 进行控制台打印和定时器管理。

目标是支持静态定义的、永不结束的线程，这些线程在用户模式下运行，进行时间分片，并且可以进行系统调用到内核。本文强调虚拟化的概念，特别是通过管理架构寄存器和分配私有堆栈，为每个线程虚拟化一个 CPU 核心。

该实现利用中断机制，特别是定时器中断，来无缝地在线程之间切换。中断例程保存和恢复寄存器，但通过交换堆栈指针，它可以切换到另一组寄存器值，从而有效地实现上下文切换。

本文引导读者了解汇编启动、主内核文件（包括 I/O 驱动程序）、用于上下文切换的 S 模式处理程序以及用户空间线程。

---

## 58. 高盛称人工智能尚未在公司业绩中显现。

**原文标题**: Goldman Sachs says AI still not showing up in companies' bottom lines

**原文链接**: [https://www.businessinsider.com/ai-company-earnings-calls-corporate-profits-bottom-line-goldman-sachs-2025-9](https://www.businessinsider.com/ai-company-earnings-calls-corporate-profits-bottom-line-goldman-sachs-2025-9)

商业内幕文章《高盛称人工智能尚未体现在公司盈利上》报道称，尽管围绕人工智能（AI）的宣传和投资甚嚣尘上，但高盛分析师观察到，迄今为止，人工智能尚未对公司收益产生明显的财务影响。

该文章可能详细说明，尽管各行业的公司都在积极探索和实施人工智能解决方案，但这些举措尚未转化为财务报表中可见的显著收入增长或成本降低。高盛认为，这种滞后可能是由于多种因素造成的，包括人工智能应用的起步阶段、有效整合人工智能所需的时间以及衡量人工智能项目真实投资回报率 (ROI) 的挑战。

该报告可能强调，公司正在人工智能开发、培训和基础设施上投入大量资源，但其益处仍主要集中在提高效率或改善客户体验等领域，而不是直接的盈利能力。它也可能提及人工智能在长期内对公司的潜在影响，但告诫投资者不要期望短期内盈利出现立即或显著的改善。最终，这篇文章对人工智能目前对企业业绩的影响提出了一种更为谨慎和现实的看法，与围绕该技术的广泛热情和乐观情绪形成对比。

---

## 59. 提泰妮娅编程语言

**原文标题**: Titania Programming Language

**原文链接**: [https://github.com/gingerBill/titania](https://github.com/gingerBill/titania)

Titania 是一种基于 Oberon-07 的新型编程语言，旨在作为编译器开发的教学工具。“Titania”这个名称的灵感来源于莎士比亚的《仲夏夜之梦》，其中 Titania 是 Oberon 的妻子。这只是一个代号。

本文档使用形式化符号详细描述了 Titania 的语法，概述了模块、导入列表、声明（常量、类型、变量、过程）、表达式、语句和其他语言构造的结构。关键要素包括：

*   **模块：** 编译的基本单元。
*   **数据类型：** 包括整数、实数、字符串、布尔值、数组、记录和指针。
*   **过程：** 支持形式参数、局部声明和可选返回值。
*   **语句：** 包括赋值、过程调用、条件语句（if, case）、循环（while, repeat, for）。
*   **运算符：** 定义算术、逻辑和关系运算符。

本文档还列出了关键字，并提供了分号插入规则以简化 tokenizer 的解析。最后，它包含了一个内置过程的列表，用于执行绝对值计算、位操作、类型转换、内存分配、打印和长度确定等任务。这些内置过程将随着编译器的开发而扩展。

---

## 60. 加州称不再信任华盛顿的新冠疫苗。

**原文标题**: California says it can no longer trust Washington on Covid vaccines

**原文链接**: [https://www.latimes.com/california/story/2025-09-15/california-covid-surge-is-peaking-but-the-battle-over-vaccine-access-is-just-beginning](https://www.latimes.com/california/story/2025-09-15/california-covid-surge-is-peaking-but-the-battle-over-vaccine-access-is-just-beginning)

2025年9月，由于对特朗普政府领导下的疾控中心和食品药品监督管理局缺乏信任，尤其是在小罗伯特·F·肯尼迪就任卫生与公众服务部部长并解散疾控中心免疫实践咨询委员会之后，加利福尼亚州正在背离联邦政府的新冠疫苗指导方针。该州与医疗机构一道，现在正将其疫苗建议与儿科医生、家庭医生和产科医生等值得信赖的专业医疗团体保持一致，发布的建议比疾控中心更为广泛。

加州正通过与华盛顿州、俄勒冈州和夏威夷州组成的西海岸健康联盟等举措进行反击，以确保基于科学的免疫指导。这包括建议所有成年人、孕妇和儿童（特别是那些患有基础疾病的儿童）接种新冠疫苗，这与美国食品药品监督管理局更侧重于老年人和患有基础疾病者的有限批准形成对比。州议会还通过了一项法案，允许加州公共卫生部在疫苗覆盖要求方面考虑医学学会的指导意见。

这一转变发生在夏末新冠疫情再次抬头并出现见顶迹象、废水中新冠病毒含量高企以及对某些地区疫苗获取渠道的担忧之际。流感、呼吸道合胞病毒和百日咳等其他呼吸道疾病也在受到监测，针对高危年轻成年人的新呼吸道合胞病毒疫苗建议已经出台。

---

## 61. 萨姆·奥特曼的延寿初创公司正在测试一种使大脑更年轻的药丸。

**原文标题**: Sam Altman's longevity startup is testing a pill for a younger brain

**原文链接**: [https://www.businessinsider.com/retro-biosciences-sam-altman-antiaging-brain-pill-longevity-healthspan-2025-9](https://www.businessinsider.com/retro-biosciences-sam-altman-antiaging-brain-pill-longevity-healthspan-2025-9)

商业内幕文章报道了OpenAI的CEO萨姆·奥特曼投资并测试一家长寿初创公司开发的新型药丸，该药丸旨在改善认知功能并可能逆转与年龄相关的脑功能衰退。虽然文章未提及该初创公司的名称或药丸的确切成分，但它强调了奥特曼对长寿领域的兴趣以及他个人参与实验性治疗的试用。

关键在于“大脑健康”作为抗衰老领域的前沿。该药丸旨在针对与认知衰退相关的机制，希望增强记忆力、注意力和整体大脑性能。虽然细节很少，但文章暗示了该配方背后的科学研究和开发。

文章强调了对长寿研究日益增长的兴趣和投资，这受到了像奥特曼这样渴望探索延长寿命和改善健康寿命的个人的推动。该药丸的测试代表着一项早期努力，治疗的有效性和安全性仍然未知。该报告旨在强调长寿领域正在进行的创新和投资，特别是关注认知增强以及药物干预解决与年龄相关的大脑变化的潜力。

---

## 62. 展示 HN: 一个能根据你的搜索内容生成产品的商店

**原文标题**: Show HN: A store that generates products from anything you type in search

**原文链接**: [https://anycrap.shop/](https://anycrap.shop/)

无法访问文章链接。

---

## 63. 页面对象 (2013)

**原文标题**: Page Object (2013)

**原文链接**: [https://martinfowler.com/bliki/PageObject.html](https://martinfowler.com/bliki/PageObject.html)

Martin Fowler 的“页面对象”定义了一种 UI 测试模式，旨在提高可维护性和降低脆弱性。页面对象封装了一个 HTML 页面或片段，提供一个特定于应用程序的 API 来与 UI 元素交互，而无需直接操作 HTML。这可以保护测试免受 UI 更改的影响。

页面对象应该模仿用户交互，提供用于访问元素的方法（文本字段的字符串，复选框的布尔值，按钮的面向操作的方法名称），隐藏底层 UI 小部件。

页面对象不应代表整个页面，而应代表重要的元素，例如页面中的专辑列表。它们应该模拟与用户相关的结构。当导航到新页面时，初始页面对象应返回该页面的新页面对象。

关于页面对象中的断言存在争议。Fowler 提倡使用无断言的页面对象，更喜欢使用断言库来防止重复并改善诊断。他对检查页面不变性的断言做出了例外。

虽然页面对象通常用于测试，但它们也可以提供脚本接口。它们封装了诸如异步操作或线程之类的并发问题。应该在页面对象之上分层一个领域特定语言 (DSL)。

将逻辑移出 UI 元素的模式减少了对页面对象的需求。页面对象体现了封装，隐藏了 UI 细节，从而更容易进行 UI 修改，并使客户端（测试）代码更简洁、更专注于意图。“页面对象”这个名称可能具有误导性，“面板对象”可能更合适。

---

## 64. 老年人认知衰退相关的重复性消极思维

**原文标题**: Repetitive negative thinking associated with cognitive decline in older adults

**原文链接**: [https://bmcpsychiatry.biomedcentral.com/articles/10.1186/s12888-025-06815-2](https://bmcpsychiatry.biomedcentral.com/articles/10.1186/s12888-025-06815-2)

本研究调查了武汉424名社区居住老年人（60岁以上）的重复性消极思维（RNT）与认知功能之间的关系。研究采用横断面设计，使用持续性思维问卷（PTQ）评估RNT水平，并使用蒙特利尔认知评估（MoCA）评估认知功能。

研究发现RNT与认知功能呈负相关。即使在调整了年龄、教育程度、职业、婚姻状况、居住安排、收入和爱好等协变量后，RNT评分较高（在Q3和Q4四分位数）的参与者，其MoCA评分显著低于最低四分位数（Q1）的参与者。具体而言，较高的RNT与较差的视觉空间功能、命名、抽象思维和记忆力有关。

亚组分析表明，RNT与认知功能之间的负相关关系在60-79岁和至少具有初中学历的个体中更为明显。

该研究得出结论，RNT与老年人的认知功能呈负相关，强调RNT可能是认知衰退的一个潜在可改变的危险因素。作者建议未来进行多中心、长时间跨度的队列研究，以进一步探讨其潜在机制。

---

## 65. Nicu's test website made with SVG (2007)

**原文标题**: Nicu's test website made with SVG (2007)

**原文链接**: [https://svg.nicubunu.ro/](https://svg.nicubunu.ro/)

Nicu's SVG test website, created in 2007, aimed to evaluate Google's ability to index SVG files. The author, nicubunu.ro, sought to determine if Google could fully index the text content of SVG files or treat them solely as images. A crucial test was to see if Google would follow the links within the SVG and index those linked files as well.

The author was interested in exploring the feasibility of using Inkscape as the primary tool for website creation. The site's creation entirely within Inkscape served as a practical demonstration of this concept.

The website, built with advanced SVG features like Gaussian Blur, acknowledged browser compatibility limitations, suggesting Firefox 3.0 or later for the best user experience. It included a navigation menu with links to "Home," "Stuf," and "About."

The inclusion of the text "lmtbk4mh" was specifically intended to be a test for search engine indexing, to see if the arbitrary string would be found. Ultimately, the project served as a testbed to assess the effectiveness of SVG for web content and Google's ability to process and index such content. The author also welcomed information from readers on the subject.


---

## 66. Trigger Crossbar

**原文标题**: Trigger Crossbar

**原文链接**: [https://serd.es/2025/09/14/Trigger-crossbar.html](https://serd.es/2025/09/14/Trigger-crossbar.html)

This article details the design and construction of a "Trigger Crossbar," a device intended to simplify trigger signal routing between various lab instruments. The author, facing cable clutter and voltage incompatibility issues in their rack-mounted electronics lab, envisioned a 1U device with multiple coaxial trigger inputs and outputs connected to an FPGA-based switch fabric.

The device aims to allow complex multi-instrument setups without needing to manually reroute cables, and address voltage level differences. The crossbar is designed with 12x12 configuration: eight inputs, eight outputs, and four bidirectional ports. Inputs feature attenuators and comparators for variable thresholding, while outputs are either directly driven by the FPGA for low jitter (1.8V swing) or buffered by level shifters with adjustable VCCIO for compatibility with various voltage levels.

The core components include a Xilinx XC7K70T FPGA and an STM32H735 MCU. The project leverages the FPGA's SERDES lanes for functionalities like BERT, 10GbE connectivity via an SFP+, and deskew reference.

The PCB was fabricated at Multech, and the article details some of the bring-up challenges faced, including power connection issues due to mirrored pinouts, soldering problems with DC-DC modules, and issues with the comparators not functioning well at low amplitudes. The article describes the problems with the comparators Vcm, ultimately needing manual fixes instead of a complete board re-spin.


---

## 67. Samsung 870 QVO 4TB SATA SSD-s: how are they doing after 4 years of use?

**原文标题**: Samsung 870 QVO 4TB SATA SSD-s: how are they doing after 4 years of use?

**原文链接**: [https://ounapuu.ee/posts/2025/09/15/samsung-870-qvo/](https://ounapuu.ee/posts/2025/09/15/samsung-870-qvo/)

生成摘要时出错

---

## 68. AMD Turin PSP binaries analysis from open-source firmware perspective

**原文标题**: AMD Turin PSP binaries analysis from open-source firmware perspective

**原文链接**: [https://blog.3mdeb.com/2025/2025-09-11-gigabyte-mz33-ar1-blob-analysis/](https://blog.3mdeb.com/2025/2025-09-11-gigabyte-mz33-ar1-blob-analysis/)

This article details the author's journey to get coreboot running on a Gigabyte MZ33-AR1 server board with an AMD Turin CPU, focusing on the challenges faced with AMD's Platform Security Processor (PSP) firmware and the solutions developed. The publicly available PSP blobs were insufficient to release the CPU from reset, forcing a workaround of injecting coreboot into the vendor firmware.

The author analyzes the structure of AMD PSP firmware, including the Embedded Firmware Structure (EFS) and PSP/BIOS directories, using the modified `amdfwtool` to compare vendor and coreboot images. Differences in SPI speeds, eSPI configuration, and the Multi Gen EFS value were identified and corrected by adjusting Kconfig values in the board code.

However, even after addressing these discrepancies, the system still failed to boot with the public blobs. The author then extracted blobs from the vendor firmware using `PSPTool` and integrated them into the coreboot build, requiring modifications to `fw.cfg` and extensions to `amdfwtool`. This resulted in a bootable coreboot image.

Further investigation revealed a critical difference: the AMD Root Key ID used for signing PSP blobs differed between the public blobs and the vendor firmware. It was found that the latest AMD PSP blobs available to AMD partners contained the same key ID as the vendor firmware. Therefore, the issue preventing coreboot from booting with the public blobs was due to the public key being the wrong one. The author is planning to publish the PSPTool modifications soon.


---

## 69. 阅读以忘却

**原文标题**: Read to forget

**原文链接**: [https://mo42.bearblog.dev/read-to-forget/](https://mo42.bearblog.dev/read-to-forget/)

生成摘要时出错

---

## 70. 你反应慢，那又怎样？

**原文标题**: You’re a slow thinker. Now what?

**原文链接**: [https://chillphysicsenjoyer.substack.com/p/youre-a-slow-thinker-now-what](https://chillphysicsenjoyer.substack.com/p/youre-a-slow-thinker-now-what)

生成摘要时出错

---

## 71. Proxmox delivers datacenter manager beta for more viable VMware contender

**原文标题**: Proxmox delivers datacenter manager beta for more viable VMware contender

**原文链接**: [https://www.theregister.com/2025/09/12/proxmox_datacenter_manager/](https://www.theregister.com/2025/09/12/proxmox_datacenter_manager/)

Proxmox正在进行其数据中心管理器（Datacenter Manager）的Beta测试，该工具旨在集中管理多个Proxmox虚拟环境（PVE）集群。此举使Proxmox成为VMware更强大的竞争对手，特别是对于寻求经济高效的虚拟化解决方案的组织而言。

目前，PVE集群作为独立的实体运行。数据中心管理器通过提供一个控制台来监控各个节点和集群，从而解决了这一限制，简化了跨集群的虚拟机迁移等任务。此功能对于扩展其超融合基础设施的组织至关重要。

由于Broadcom所有权下的VMware被认为正在转移对小型客户的关注，因此这个时机尤其重要。 Proxmox凭借其开源性质和具有竞争力的定价，提供了一个有吸引力的替代方案。虽然VMware被认为是更成熟且功能丰富的平台，但其不断上涨的成本正在推动一些用户探索Proxmox、Hyper-V和Nutanix等选项来处理特定工作负载。数据中心管理器的推出预计将进一步增强Proxmox作为可行的VMware替代方案的吸引力。预计今年晚些时候将发布稳定版本。

---

## 72. Models of European metro stations

**原文标题**: Models of European metro stations

**原文链接**: [http://stations.albertguillaumes.cat/](http://stations.albertguillaumes.cat/)

生成摘要时出错

---

## 73. Korea's major US investment projects halted

**原文标题**: Korea's major US investment projects halted

**原文链接**: [https://www.kedglobal.com/business-politics/newsView/ked202509080002](https://www.kedglobal.com/business-politics/newsView/ked202509080002)

生成摘要时出错

---

## 74. The PC was never a true 'IBMer'

**原文标题**: The PC was never a true 'IBMer'

**原文链接**: [https://thechipletter.substack.com/p/the-pc-was-never-a-true-ibmer](https://thechipletter.substack.com/p/the-pc-was-never-a-true-ibmer)

生成摘要时出错

---

## 75. Xrust – XPath, XQuery, and XSLT for Rust

**原文标题**: Xrust – XPath, XQuery, and XSLT for Rust

**原文链接**: [https://gitlab.gnome.org/World/Rust/markup-rs/xrust](https://gitlab.gnome.org/World/Rust/markup-rs/xrust)

生成摘要时出错

---

## 76. The AI-Scraping Free-for-All Is Coming to an End

**原文标题**: The AI-Scraping Free-for-All Is Coming to an End

**原文链接**: [https://nymag.com/intelligencer/article/ai-scraping-free-for-all-by-openai-google-meta-ending.html](https://nymag.com/intelligencer/article/ai-scraping-free-for-all-by-openai-google-meta-ending.html)

生成摘要时出错

---

## 77. High Altitude Living – 8,000 ft and above (2021)

**原文标题**: High Altitude Living – 8,000 ft and above (2021)

**原文链接**: [https://studioq.com/blog/2021/5/30/high-altitude-living-8000-ft-and-above-2450-meters](https://studioq.com/blog/2021/5/30/high-altitude-living-8000-ft-and-above-2450-meters)

生成摘要时出错

---

## 78. China's Snub of U.S. Soybeans Is a Crisis for American Farmers

**原文标题**: China's Snub of U.S. Soybeans Is a Crisis for American Farmers

**原文链接**: [https://www.nytimes.com/2025/09/15/business/china-us-soybeans-farming.html](https://www.nytimes.com/2025/09/15/business/china-us-soybeans-farming.html)

生成摘要时出错

---

## 79. Observable Notebooks 数据加载器

**原文标题**: Observable Notebooks Data Loaders

**原文链接**: [https://observablehq.com/notebook-kit/data-loaders](https://observablehq.com/notebook-kit/data-loaders)

Observable Notebooks Data Loaders are special cells that execute code "ahead of time" during the build process using interpreters like Node.js or Python, rather than "live" in the browser. This is ideal for preparing static data, ensuring consistency, boosting performance, and expanding beyond SQL-based database connections.

Supported formats include text-based (text, JSON, CSV, TSV, XML) and binary formats (Arrow, Parquet, Blob, Buffer), as well as image (jpeg, gif, webp, png, svg) and HTML. The output of these cells is cached in a `.observable/cache` directory, updating only when the data loader cell is re-run.

The article provides examples of both Python (printing a greeting and version) and Node.js (fetching npm download statistics) data loader cells.

Specific requirements for Node.js data loaders include Node.js 22.12+ installation in standard locations, read-only file access within the notebook directory, and package installation within the same directory. Python data loaders require Python 3.12+ in standard locations and support virtual environments. Installed packages are not implicit, you have to install them via pip.


---

## 80. MIT-MC CP/M archive files, 1979-1984

**原文标题**: MIT-MC CP/M archive files, 1979-1984

**原文链接**: [https://github.com/MITDDC/cpmarchive-1979-1984](https://github.com/MITDDC/cpmarchive-1979-1984)

生成摘要时出错

---

## 81. China's Snub of U.S. Soybeans Is a Crisis for American Farmers

**原文标题**: China's Snub of U.S. Soybeans Is a Crisis for American Farmers

**原文链接**: [https://www.nytimes.com/2025/09/15/business/chinas-snub-of-us-soybeans-is-a-crisis-for-american-farmers.html](https://www.nytimes.com/2025/09/15/business/chinas-snub-of-us-soybeans-is-a-crisis-for-american-farmers.html)

生成摘要时出错

---

## 82. La-Proteina

**原文标题**: La-Proteina

**原文链接**: [https://github.com/NVIDIA-Digital-Bio/la-proteina](https://github.com/NVIDIA-Digital-Bio/la-proteina)

生成摘要时出错

---

## 83. Cex.C – Comprehensively EXtended C Language

**原文标题**: Cex.C – Comprehensively EXtended C Language

**原文链接**: [https://github.com/alexveden/cex](https://github.com/alexveden/cex)

生成摘要时出错

---

## 84. CorentinJ: Real-Time Voice Cloning (2021)

**原文标题**: CorentinJ: Real-Time Voice Cloning (2021)

**原文链接**: [https://github.com/CorentinJ/Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning)

生成摘要时出错

---

## 85. macOS Tahoe is certified Unix 03 [pdf]

**原文标题**: macOS Tahoe is certified Unix 03 [pdf]

**原文链接**: [https://www.opengroup.org/openbrand/certificates/1223p.pdf](https://www.opengroup.org/openbrand/certificates/1223p.pdf)

生成摘要时出错

---

## 86. The unreasonable effectiveness of modern sort algorithms

**原文标题**: The unreasonable effectiveness of modern sort algorithms

**原文链接**: [https://github.com/Voultapher/sort-research-rs/blob/main/writeup/unreasonable/text.md](https://github.com/Voultapher/sort-research-rs/blob/main/writeup/unreasonable/text.md)

生成摘要时出错

---

## 87. Introduction to GrapheneOS

**原文标题**: Introduction to GrapheneOS

**原文链接**: [https://dataswamp.org/~solene/2025-01-12-intro-to-grapheneos.html](https://dataswamp.org/~solene/2025-01-12-intro-to-grapheneos.html)

生成摘要时出错

---

## 88. Celery salt wound up on the Chicago dog

**原文标题**: Celery salt wound up on the Chicago dog

**原文链接**: [https://wgntv.com/chicago-food/how-celery-salt-wound-up-on-the-chicago-dog/](https://wgntv.com/chicago-food/how-celery-salt-wound-up-on-the-chicago-dog/)

生成摘要时出错

---

## 89. Dynamic Bird Migration Map

**原文标题**: Dynamic Bird Migration Map

**原文链接**: [https://explorer.audubon.org/explore/species?sidebar=expand](https://explorer.audubon.org/explore/species?sidebar=expand)

生成摘要时出错

---

## 90. Decentralized YouTube alternative adds livestream scheduling in new release

**原文标题**: Decentralized YouTube alternative adds livestream scheduling in new release

**原文链接**: [https://news.itsfoss.com/peertube-7-3/](https://news.itsfoss.com/peertube-7-3/)

生成摘要时出错

---

## 91. Patela: A basement full of amnesic servers

**原文标题**: Patela: A basement full of amnesic servers

**原文链接**: [https://osservatorionessuno.org/blog/2025/05/patela-a-basement-full-of-amnesic-servers/](https://osservatorionessuno.org/blog/2025/05/patela-a-basement-full-of-amnesic-servers/)

生成摘要时出错

---

## 92. Geedge and MESA leak: Analyzing the great firewall’s largest document leak

**原文标题**: Geedge and MESA leak: Analyzing the great firewall’s largest document leak

**原文链接**: [https://gfw.report/blog/geedge_and_mesa_leak/en/](https://gfw.report/blog/geedge_and_mesa_leak/en/)

生成摘要时出错

---

## 93. Gleam is my new obsession

**原文标题**: Gleam is my new obsession

**原文链接**: [https://ericcodes.io/blog/gleam-my-new-obsession.html](https://ericcodes.io/blog/gleam-my-new-obsession.html)

生成摘要时出错

---

## 94. Implementing namespaces and coding standards in WordPress plugin development

**原文标题**: Implementing namespaces and coding standards in WordPress plugin development

**原文链接**: [https://developer.wordpress.org/news/2025/09/implementing-namespaces-and-coding-standards-in-wordpress-plugin-development/](https://developer.wordpress.org/news/2025/09/implementing-namespaces-and-coding-standards-in-wordpress-plugin-development/)

生成摘要时出错

---

## 95. FreeBSD 15.0 Alpha 2 Released with Builds Now Being Properly Reproducible

**原文标题**: FreeBSD 15.0 Alpha 2 Released with Builds Now Being Properly Reproducible

**原文链接**: [https://www.phoronix.com/news/FreeBSD-15.0-Alpha-2](https://www.phoronix.com/news/FreeBSD-15.0-Alpha-2)

生成摘要时出错

---

## 96. FakeIt: C++ Mocking Made Easy

**原文标题**: FakeIt: C++ Mocking Made Easy

**原文链接**: [https://github.com/eranpeer/FakeIt](https://github.com/eranpeer/FakeIt)

生成摘要时出错

---

## 97. Bank of Thailand freezes 3M accounts, sets daily transfer limits to curb fraud

**原文标题**: Bank of Thailand freezes 3M accounts, sets daily transfer limits to curb fraud

**原文链接**: [https://www.thaienquirer.com/57752/bot-freezes-3-million-accounts-sets-daily-transfer-limits-of-50000-200000-baht-to-curb-6-billion-baht-scam-losses/](https://www.thaienquirer.com/57752/bot-freezes-3-million-accounts-sets-daily-transfer-limits-of-50000-200000-baht-to-curb-6-billion-baht-scam-losses/)

生成摘要时出错

---

## 98. ChatControl update: blocking minority held but Denmark is moving forward anyway

**原文标题**: ChatControl update: blocking minority held but Denmark is moving forward anyway

**原文链接**: [https://disobey.net/@yawnbox/115203365485529363](https://disobey.net/@yawnbox/115203365485529363)

生成摘要时出错

---

## 99. Cannabis use associated with quadrupled risk of developing type 2 diabetes

**原文标题**: Cannabis use associated with quadrupled risk of developing type 2 diabetes

**原文链接**: [https://medicalxpress.com/news/2025-09-cannabis-quadrupled-diabetes-million-adults.html](https://medicalxpress.com/news/2025-09-cannabis-quadrupled-diabetes-million-adults.html)

生成摘要时出错

---

## 100. Gentoo AI Policy

**原文标题**: Gentoo AI Policy

**原文链接**: [https://wiki.gentoo.org/wiki/Project:Council/AI_policy](https://wiki.gentoo.org/wiki/Project:Council/AI_policy)

生成摘要时出错

---

