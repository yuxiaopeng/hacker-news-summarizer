# Hacker News 热门文章摘要 (2025-10-25)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. Synadia和TigerBeetle向Zig软件基金会捐赠51.2万美元

**原文标题**: Synadia and TigerBeetle Commit $512k USD to the Zig Software Foundation

**原文链接**: [https://www.synadia.com/blog/synadia-tigerbeetle-zig-foundation-pledge](https://www.synadia.com/blog/synadia-tigerbeetle-zig-foundation-pledge)

Synadia和TigerBeetle联合承诺在未来两年内向 Zig 软件基金会 (ZSF) 捐赠 51.2 万美元。 这项承诺表明他们共同相信 Zig 在推动高性能、可靠和可维护软件创新方面的潜力。

NATS.io 平台的创建者 Synadia 旨在安全可靠地连接一切，使组织能够实现系统现代化。 他们认为 Zig 符合他们构建更小、更高效和更具确定性的部署的目标。

金融交易数据库公司 TigerBeetle 与 Synadia 秉持相同的正确性、清晰性和可靠性价值观（“TigerStyle”）。 TigerBeetle 发起了这项联合行动，邀请 Synadia 增加对 Zig 基金会的支持。

两家公司都赞扬 Zig 的控制力、性能和简洁性，以及 ZSF 创始人 Andrew Kelley 的领导力。 他们很自豪能够支持 Zig 社区推进系统编程。 Zig 软件基金会支持 Zig 编程语言的开发，该语言以其性能、可靠性和可维护性而闻名。 Synadia 和 TigerBeetle 认为 Zig 将在下一代可靠的分布式系统中发挥关键作用。

---

## 2. 滚石机使用说明：将粗糙的石头变成美丽的抛光石

**原文标题**: Rock Tumbler Instructions: Turning Rough Rocks into Beautiful Tumbled Stones

**原文链接**: [https://rocktumbler.com/tips/rock-tumbler-instructions/](https://rocktumbler.com/tips/rock-tumbler-instructions/)

本文详细介绍了如何使用旋转式研磨机将粗糙的岩石研磨成抛光的石头。文章强调了使用莫氏硬度为6-7、尺寸为3/8英寸至1 1/2英寸的优质粗糙岩石的重要性，并建议使用玉髓、石英和某些岩石类型。

本指南重点介绍了三个“黄金法则”：“垃圾进意味着垃圾出”（从优质粗糙岩石开始），“避免污染”（步骤之间保持清洁至关重要）以及“好结果需要时间”（不要急于求成）。文章建议检查粗糙岩石的孔隙率或裂缝，因为这些会影响研磨过程。建议混合不同尺寸的岩石以获得更好的研磨效果。

该过程的核心是一个四步研磨过程，针对三磅容量的旋转式研磨机进行了详细说明。每个步骤都涉及使用越来越细的磨料：
*   **第一步（粗磨）：**塑造岩石形状并使其圆润。
*   **第二步（中磨）：**使表面光滑。
*   **第三步（细磨/预抛光）：**进一步精细地打磨光滑度。
*   **第四步（抛光）：**增加最终的光泽。

对于每个步骤，文章都指定了每磅岩石使用的磨料量、水位和持续时间（每个步骤大约七天）。强调在每个步骤之间彻底清洁岩石、桶和盖子，以防止粗磨料的污染。建议使用陶瓷介质作为填充物并缓冲更脆弱的岩石，如石英。文章强烈警告不要将用过的磨料冲入下水道，而是建议使用漏勺和水桶。

---

## 3. 制作微型Linux发行版（2023）

**原文标题**: Making a micro Linux distro (2023)

**原文链接**: [https://popovicu.com/posts/making-a-micro-linux-distro/](https://popovicu.com/posts/making-a-micro-linux-distro/)

本文解释了如何从头构建一个最小化的 Linux 发行版，重点在于底层概念，而非精确的技术指南。文章首先定义了操作系统内核在管理硬件、提供高级编程接口（如文件系统）以及实现多任务处理方面的作用。Linux 作为一个流行的内核，构成了基础，但需要额外的层才能成为一个可用的系统。

一个 Linux 发行版本质上是将 Linux 内核与用户空间代码（基础设施）捆绑在一起，这些代码处理内核不处理的任务，如网络、用户界面和应用程序执行。这种“基础设施之上的基础设施”运行在用户空间中，并通过定义的 ABI 与内核交互。

init 进程，一个进程 ID 为 1 的用户空间程序，是内核加载后启动的第一个程序。然后它启动其他进程，形成一个进程树，从而实现机器的功能。

文章还提到了发行版如何随着时间的推移积累不必要的软件包而变得臃肿。不同的发行版在用户控制级别上也有所不同，例如 Arch Linux 等发行版提供了一个最小的基础安装，将所有后续配置都留给用户。

---

## 4. Python Web 服务的未来：或将摆脱 GIL 限制

**原文标题**: The future of Python web services looks GIL-free

**原文链接**: [https://blog.baro.dev/p/the-future-of-python-web-services-looks-gil-free](https://blog.baro.dev/p/the-future-of-python-web-services-looks-gil-free)

Giovanni Barillari 的博客文章探讨了无 GIL 的 Python 3.14 对 Web 服务的潜在影响，通过在 ASGI (FastAPI) 和 WSGI (Flask) 应用上进行基准测试，比较了其性能与启用 GIL 的版本。基准测试测试了 JSON 响应和模拟的 I/O 密集型端点，由 Granian 提供服务，并使用 rewrk 进行基准测试。

结果表明，对于 ASGI，无 GIL 的 Python 在 CPU 密集型任务中性能下降约 20%，但内存占用更少。对于 I/O 密集型任务，两个版本的性能相似，但无 GIL 版本再次占用更少的内存。

对于 WSGI，无 GIL 版本在 CPU 密集型任务中明显优于启用 GIL 的版本，利用了更多的 CPU 性能，但消耗了更多的内存。I/O 密集型性能在两者中相似。

作者的结论是，无 GIL 的 Python 提供了几个优势，尤其是在 ASGI 应用的内存管理方面。对于 WSGI，对内存使用的担忧可以通过改进 Granian 中的垃圾回收来缓解。总的来说，作者认为无 GIL 的 Python 简化了并发范式和部署，可能会提高开发者和基础设施管理者的生活质量。他们预见到 Python Web 服务的无 GIL 未来，尽管 gilectomy 最初并非针对 Web 应用。

---

## 5. 2025年React与Backbone对比

**原文标题**: React vs. Backbone in 2025

**原文链接**: [https://backbonenotbad.hyperclay.com/](https://backbonenotbad.hyperclay.com/)

本文认为，尽管React经历了15年的发展并拥有庞大的资源支持，但与Backbone等较早的框架相比，我们在简化UI开发方面并没有取得显著进展。虽然React最初看起来更简洁易读，但这种简洁是以增加抽象复杂性为代价的。

作者认为，Backbone虽然冗长，但对其操作坦诚直白，这使得初级开发人员更容易理解和调试。而React则隐藏了其大部分内部运作机制，导致出现意外问题，需要深入了解其协调算法、渲染阶段和调度器。常见的输入清除问题、useEffect中的无限循环以及过期闭包等问题表明，React的“魔力”可能很快就会变成调试噩梦。

作者批评了理解React需要从头开始重建它的观点，认为这种程度的理解对于简单的任务来说是不必要的。文章承认React在极其庞大和复杂的应用程序中的潜在优势，但质疑它对于绝大多数较小应用程序的必要性。文章最后呼吁建立一个更简单、更透明、更易于修改的UI开发模型，使其保持与DOM本身一样坚固和易于理解。关键在于，React的抽象与Backbone等较早框架的明确性之间的权衡可能并不总是值得的，特别是对于较小的项目而言。

---

## 6. 解锁英国航空免费WiFi

**原文标题**: Unlocking free WiFi on British Airways

**原文链接**: [https://www.saxrag.com/tech/reversing/2025/06/01/BAWiFi.html](https://www.saxrag.com/tech/reversing/2025/06/01/BAWiFi.html)

本文详细介绍了作者如何通过利用 TLS 握手中的服务器名称指示 (SNI) 绕过英国航空免费“消息”WiFi 限制。英国航空通过检查 SNI 来允许通过白名单应用程序（Whatsapp、Signal、微信）进行免费消息传递，SNI 会在加密隧道建立*之前*泄露客户端连接的域名。

作者发现，虽然英航阻止直接连接到通用网站，但它将消息应用程序使用的域名列入了白名单。为了规避这一点，他们在 VPS 上设置了一个 HTTPS 代理，使用 stunnel 创建一个带有自签名证书和通用名称 (CN) wa.me（一个 Whatsapp 域名）的 TLS 连接。然后，他们使用 `openssl` 并在后来使用带有 `--resolve` 标志的 `curl`，强制 SNI 为 `wa.me`，同时连接到其代理的 IP 地址，从而欺骗英航允许连接。通过将所有流量通过此代理路由，他们可以访问任意网站，尽管带宽限制导致加载时间缓慢。

作者还探讨了使用加密客户端 Hello (ECH)，这是一种 TLS 扩展，可以加密 SNI，从而有可能绕过基于 SNI 的过滤，而无需伪造域名并使用标准 TLS 证书。最后，本文警告不要盲目信任安全上下文中的 SNI，因为它很容易被恶意行为者欺骗。

---

## 7. 适用于安卓的Swift SDK

**原文标题**: The Swift SDK for Android

**原文链接**: [https://www.swift.org/blog/nightly-swift-sdk-for-android/](https://www.swift.org/blog/nightly-swift-sdk-for-android/)

本文宣布发布Swift SDK for Android的每夜预览版本，标志着Swift向Android平台扩展迈出了重要一步。该SDK由Android工作组开发，允许开发者使用Swift构建原生Android应用程序，从而促进跨平台开发和创新。

Swift SDK for Android现已可供下载，Windows安装程序已捆绑，Linux或macOS则单独提供。我们提供了入门指南和示例应用程序，以帮助开发者开始使用该SDK。该公告强调，Swift Package Index显示，超过25%的Swift软件包与Android兼容。

swift-java项目促进了Java和Swift之间的互操作性，通过自动绑定生成，实现了双向的无缝集成。该公告鼓励开发者在Swift论坛上分享他们的经验、想法和项目。Android工作组还在制定一份愿景文档，以指导未来的开发工作，该文档将在带有官方CI的公共项目看板上进行跟踪。文章最后邀请社区为不断发展的Swift on Android生态系统做出贡献。

---

## 8. 视网膜植入和特制眼镜帮助盲人重见光明

**原文标题**: People with blindness can read again after retinal implant and special glasses

**原文链接**: [https://www.nbcnews.com/health/health-news/tiny-eye-implant-special-glasses-legally-blind-patients-can-read-rcna238488](https://www.nbcnews.com/health/health-news/tiny-eye-implant-special-glasses-legally-blind-patients-can-read-rcna238488)

一种名为PRIMA的新型视网膜植入系统，结合增强现实眼镜，已在帮助患有晚期干性年龄相关性黄斑变性(AMD)的患者恢复部分阅读能力方面显示出令人鼓舞的结果。该系统由Science Corp.开发，包括植入眼内的无线芯片，该芯片接收来自嵌入眼镜中的摄像头的信号，将光转换为电信号，刺激黄斑中剩余的健康细胞。

发表在《新英格兰医学杂志》上的一项涉及38名欧洲患者的研究表明，植入一年后重新评估的患者中，80%的人经历了具有临床意义的视力改善。虽然图像目前是黑白的，但用户可以缩放和放大它们。这项技术并非没有缺点；植入手术存在风险，包括眼压升高之类的不良事件。此外，患者需要大量的培训才能使用该设备，并且长期效果和对生活质量的影响仍在研究中。

像Demetrios Vavvas博士这样的专家警告说，不要过分夸大该技术目前形式的益处。然而，其潜力是巨大的。Science Corp.正在努力进行升级，包括增加芯片的像素密度并实现灰度视觉。研究人员希望这项技术最终可以应用于其他视网膜疾病。需要进一步的试验来评估该设备与现有辅助工具相比的实际益处和长期疗效。尽管存在局限性，PRIMA系统代表了视力恢复方面的一大进步，证明了脑机接口在严重视力障碍方面的潜力。

---

## 9. 魔法尺寸实现可编程壳体的高保真组装

**原文标题**: Magic sizes enable high-fidelity assembly of programmable shells

**原文链接**: [https://arxiv.org/abs/2411.03720](https://arxiv.org/abs/2411.03720)

本文《魔幻尺寸实现可编程壳体最小复杂度、高保真组装》探讨了利用三角形亚单元创建自组装二十面体壳体的设计原则。作者研究了如何在最小化复杂度（不同亚单元类型的数量）的同时，最大化目标产率，从而降低实验成本和缩短动力学时间尺度。

他们利用动力学蒙特卡罗模拟证明，旋转对称位点上的位错是导致非目标组装的主要缺陷。他们推导出基于对称性的规则来识别最佳设计，这些设计是抑制这些位错的最低复杂度、最高对称性设计。这些设计能够实现对具有精确、有限尺寸的壳体（甚至任意大的壳体）的稳健、高保真组装。

研究人员发现，最佳复杂度随目标尺寸的变化呈非单调性，其中“魔幻”尺寸对应于对称轴不与三角形网格顶点相交的高对称性设计。在这些魔幻尺寸下，最佳设计所需的相互作用类型比完全可寻址的构造少得多（少 12 倍），从而大大减少了实验工作量。

作者强调，这种基于对称性的剪除非目标组装的原则可以推广到具有不同拓扑结构的其他体系结构，使其成为设计自组装结构的宝贵指南。该研究提供了一个框架，用于以降低的复杂度实现复杂结构的高保真组装，从而实现更高效和经济高效的创建可编程壳体的方法。

---

## 10. Valetudo：真空机器人云替代方案，实现纯本地操作

**原文标题**: Valetudo: Cloud replacement for vacuum robots enabling local-only operation

**原文链接**: [https://valetudo.cloud/](https://valetudo.cloud/)

Valetudo是一款旨在取代真空吸尘器机器人云服务的开源软件解决方案，从而实现本地化运行。它的目标是让用户掌控自己的设备，摆脱对供应商的依赖和遥测。Valetudo由Sören Beye创建，并由贡献者支持，已经发展成为一个可靠的、一劳永逸的系统。

该项目提供了一种避免与云连接设备相关的潜在隐私问题的方法。该网站提供了资源，供用户了解更多关于使用Valetudo的优点和缺点，以及关于选择兼容机器人和开始安装过程的指导。

Valetudo采用Apache-2.0许可协议，允许用户检查和修改代码。该项目作为一种爱好进行维护，创建者无意将其商业化或扩大其目标受众。它被设想为一个公共花园：可以自由访问，但最终属于私有，用户应尊重其愿景和设计。

该网站提供文档，包括新手指南、安装说明、使用信息和故障排除提示。它还强调了与流行的家庭自动化平台的集成，如MQTT、Home Assistant、Node-RED和openHAB。用户可以通过“dust_announce”邮件列表和Valetudo Telegram群组保持更新。

---

## 11. 第一个被发现的无法穿过自身的凸多面体

**原文标题**: First convex polyhedron found that can't pass through itself

**原文链接**: [https://www.quantamagazine.org/first-shape-found-that-cant-pass-through-itself-20251024/](https://www.quantamagazine.org/first-shape-found-that-cant-pass-through-itself-20251024/)

本文详细介绍了“诺珀特面体”的发现，它是第一个被证明不具备“鲁珀特性质”的凸多面体。“鲁珀特性质”源于17世纪莱茵河鲁珀特王子的一个赌约，指的是一个形状能够被钻出一个足够大的隧道，使其自身的相同副本可以通过。

几个世纪以来，数学家们认为所有凸多面体都可能具备鲁珀特性质。虽然许多，比如立方体、四面体，甚至十二面体，通过分析阴影投影的复杂算法，都被发现具有此性质，但仍有一些“顽固分子”未能被证实。

Jakob Steininger和Sergey Yurkevich开发了一种方法，结合了一个“全局定理”和一个“局部定理”，明确地证明了无论方向如何，诺珀特面体都不能具有鲁珀特通道。他们的方法包括将所有可能方向的空间划分为数百万个小块，并使用他们的定理系统地排除它们。

诺珀特面体，一个具有90个顶点、152个面的形状，专门设计用于满足他们方法的要求，使其易于证明。这一发现推翻了之前的猜想，并为探索其他潜在的“诺珀特”开辟了新的途径，菱角二十面体仍然是一个强有力的候选者。这也证明了将理论进步与计算能力相结合的力量。

---

## 12. iOS 26更新移除了飞马和掠食者间谍软件的关键IOC

**原文标题**: Key IOCs for Pegasus and Predator Spyware Removed with iOS 26 Update

**原文链接**: [https://iverify.io/blog/key-iocs-for-pegasus-and-predator-spyware-cleaned-with-ios-26-update](https://iverify.io/blog/key-iocs-for-pegasus-and-predator-spyware-cleaned-with-ios-26-update)

iVerify 博客：iOS 26 更新对检测 Pegasus 和 Predator 间谍软件的影响

此 iVerify 博客文章讨论了 iOS 26 更新对检测 Pegasus 和 Predator 间谍软件的影响。在 iOS 26 之前，`shutdown.log` 文件包含了这些感染的有价值的取证证据，即使攻击者试图抹去痕迹。安全研究人员使用文件中发现的 IOC（入侵指标），例如特定条目 `/private/var/db/com.apple.xpc.roleaccountd.staging/com.apple.WebKit.Networking` (针对 Pegasus 2022) 以及 `containermanagerd` 日志和 `shutdown.log` 事件之间的差异，来识别受感染的设备。

然而，iOS 26 在每次重启时都会覆盖 `shutdown.log`，从而有效地清除任何先前感染的现有证据。这使得检测 Pegasus 和 Predator 间谍软件变得更加困难，尤其是在攻击越来越频繁且针对知名人士的情况下。

该文章建议用户在更新到 iOS 26 *之前* 立即创建并保存其设备的系统诊断信息，以保存当前的 `shutdown.log` 及其潜在证据。他们还建议推迟更新，直到 Apple 解决该问题，以避免丢失重要的取证数据。该博客强调了间谍软件开发者如何不断发展其规避策略，使得覆盖 shutdown.log 成为安全研究人员的有害发展。

---

## 13. 研究：核磁共振造影剂在部分患者体内导致有害金属积聚

**原文标题**: Study: MRI contrast agent causes harmful metal buildup in some patients

**原文链接**: [https://www.ormanager.com/briefs/study-mri-contrast-agent-causes-harmful-metal-buildup-in-some-patients/](https://www.ormanager.com/briefs/study-mri-contrast-agent-causes-harmful-metal-buildup-in-some-patients/)

发表在《磁共振成像》杂志上的一项新研究表明，使用钆对比剂进行MRI扫描后，某些患者体内长期滞留有毒金属的一个潜在原因。该研究表明，这些对比剂可能与常见的膳食化合物，特别是草酸（存在于食物中并由维生素C产生）发生反应，形成有害的金属纳米颗粒。

注射用于增强MRI图像的钆基对比剂通常能无害地排出体外。然而，多年后在各种器官中发现了钆的痕迹，FDA也将滞留的钆与肾源性系统性纤维化（NSF）联系起来。该研究表明，草酸会导致钆从其螯合剂中分离出来，形成能够渗透细胞的纳米颗粒。

主要作者Brent Wagner博士建议在对比剂增强MRI检查前避免服用维生素C。他推测，个体代谢环境，特别是高草酸水平，可能解释了为什么有些患者出现严重症状，而另一些患者却没有。该研究还显示，近一半有钆痕迹的患者只接受过一次对比剂注射，这表明个体生物学，而非剂量，是风险的关键因素。Wagner博士认为，纳米颗粒的形成可能会引发不成比例的免疫反应。

该研究团队正在建立一个国际患者登记处，以收集样本（血液、尿液、头发、指甲），从而进一步研究钆的积累，识别高危个体，并了解长期滞留模式。

---

## 14. 2019年机器学习框架现状

**原文标题**: The State of Machine Learning Frameworks in 2019

**原文链接**: [https://thegradient.pub/state-of-ml-frameworks-2019-pytorch-dominates-research-tensorflow-dominates-industry/](https://thegradient.pub/state-of-ml-frameworks-2019-pytorch-dominates-research-tensorflow-dominates-industry/)

2019年，PyTorch和TensorFlow主导了机器学习框架格局。文章认为，PyTorch正在迅速发展，尤其是在研究领域，而TensorFlow仍然是工业领域的主导力量。

研究领域偏爱PyTorch，因为它简单、具有Pythonic特性、API设计良好，并且据称性能与TensorFlow相当。顶级会议的数据表明，研究论文的实现方式正显著转向PyTorch。TensorFlow的多次API更改造成了混乱，阻碍了其采用。

TensorFlow在工业领域的采用得益于惯性、其生产就绪的功能（如无Python依赖、移动支持（TensorFlow Lite）和Serving能力（TensorFlow Serving））。然而，PyTorch正在通过引入TorchScript来解决这些问题，从而实现基于图的优化和部署。TensorFlow引入了eager模式以提高可用性。

未来取决于几个因素：研究人员偏好对行业招聘的影响、TensorFlow的eager模式的可用性和性能，以及PyTorch开发生产就绪功能的能力。谷歌专注于在其云服务中使用TensorFlow，这可能会激励竞争对手支持PyTorch。

文章还介绍了Jax，这是一种具有高级自动微分功能的框架，有可能带来新的研究机会。最终，这些框架之间的竞争将塑造机器学习研究和开发的未来。

---

## 15. 抓住美国热泵发展的机遇

**原文标题**: Harnessing America's heat pump moment

**原文链接**: [https://www.heatpumped.org/p/harnessing-america-s-heat-pump-moment](https://www.heatpumped.org/p/harnessing-america-s-heat-pump-moment)

本文《抓住美国热泵机遇》探讨了为何美国热泵普及滞后，尽管该技术已被证明具有效率高、环境友好、成本效益高等优点，尤其是在《通货膨胀削减法案》(IRA)等激励措施的推动下。作者约瑟夫·德纳塔莱认为，障碍并非技术性的，而是文化、经济和人为的。

尽管热泵已经存在了几十年，并且提供了比传统炉子和空调更清洁、更安静、更高效的替代方案，但挑战依然存在。承包商通常默认使用熟悉的系统，房主缺乏教育和指导，并且市场分散，充斥着虚假信息。

文章强调了热泵普及势头正在增强的四个关键原因：人们对电气化的文化意识日益增强，联邦和州政策协同支持转型，私人资本在该领域的投资以及消除热泵无法应对寒冷天气的迷思。

德纳塔莱提出了加速热泵普及的五个关键：教育房主、培训劳动力、利用更好的工具和数据进行尺寸选择和安装、优先考虑质量和信任，以及协调政策以逐步淘汰单向空调。他总结说，执行，而非进一步的发明，对于使热泵成为美国家庭的默认选择至关重要。本文是解决这些挑战和解决方案的五部分系列文章的第一篇。

---

## 16. 上下文工程忽略了不起眼的超链接。

**原文标题**: Context engineering is sleeping on the humble hyperlink

**原文链接**: [https://mbleigh.dev/posts/context-engineering-with-links/](https://mbleigh.dev/posts/context-engineering-with-links/)

本文认为，超链接是大型语言模型（LLM）中一种未被充分利用但功能强大的上下文工程工具。它强调了为 LLM 提供足够上下文，同时避免无关信息淹没它们的紧张关系。讨论了常见的解决方案，如 RAG 和子代理，但作者提倡超链接的简单性和效率。

作者将此比作人类学习，我们通过链接和标签浏览信息。他们提出了“超文本作为代理状态的引擎”，并解释了 LLM 如何有效地解析和导航超链接数据。

本文概述了实现的简易性，仅需一个接受 URI 的工具和一个至少带有一个 URI 的入口点。一个 Genkit 示例展示了模型如何动态加载和按需应用相关上下文。

使用超链接的好处包括：易于实现、灵活性、token 效率、工具效率，以及通过提供即时上下文来缓解上下文腐烂和近因偏差。

本文强调需要使 MCP 资源能够通过 `read_resources` 工具被模型消耗，并给出了一个为 Firebase MCP Server 构建此类工具的示例。作者最后建议，开发者在为他们的代理构建多个专用工具之前，应考虑超链接。

---

## 17. 什么是智能？ (2024)

**原文标题**: What is intelligence? (2024)

**原文链接**: [https://whatisintelligence.antikythera.org/](https://whatisintelligence.antikythera.org/)

在没有Blaise Agüera y Arcas的文章内容的情况下，无法提供具体的摘要。但是，根据标题（“什么是智能？”）和副标题（“关于进化、计算和心灵的AI启示”），我们可以推断出其主要观点并生成一个概括性摘要：

这篇文章，很可能由Blaise Agüera y Arcas撰写，探讨了构成智能的复杂问题，尤其是在人工智能（AI）取得进展的背景下。它可能通过比较和对比AI、生物进化和人类思维来探讨智能的多面性。

文章可能认为，理解AI的发展可以为智能如何自然进化提供见解，迫使我们重新思考传统的定义。它可能会讨论AI的成功和局限性如何阐明不同的智能方法，从基于规则的系统到模仿生物大脑的神经网络。

文章可能还会探讨计算在理解和复制智能中的作用。它可能会深入研究创建和维持智能系统所需的计算能力，以及复制人类大脑复杂性的挑战。

最后，文章可能探讨了AI的哲学意义，挑战我们对意识、创造力以及使人类思维独一无二之处的理解。它可能会提出关于智能的未来，包括人工智能和生物智能，以及对社会潜在影响的问题。本质上，它试图通过AI、进化和心灵的视角来定义智能，从而引发对我们自己对这一基本概念的理解的反思。

---

## 18. 我邀请陌生人通过小票打印机给我发消息。

**原文标题**: I invited strangers to message me through a receipt printer

**原文链接**: [https://aschmelyun.com/blog/i-invited-strangers-to-message-me-through-a-receipt-printer/](https://aschmelyun.com/blog/i-invited-strangers-to-message-me-through-a-receipt-printer/)

本文详细介绍了作者将收据打印机连接到其网站的项目，允许任何人向其发送匿名消息，这些消息会以物理形式打印在他们的桌面上。受到朋友匿名消息系统的启发，作者使用了一台从 eBay 购得的价值 50 美元的 Epson TM-T88IV 热敏收据打印机。由于打印机的年代久远且缺乏现代驱动程序支持，树莓派 4 充当了中间媒介，接收命令并通过 USB 与打印机通信。

作者使用 PHP 和 Laravel 框架构建了一个网站，其中包含一个用于提交消息的简单表单。消息经过验证，以确保它们仅包含收据打印机可打印的标准字符。提交后，消息使用 ESC/POS 命令（通过 PHP 包）进行格式化，打印带有标题和交易编号，然后进行切割。

为了处理托管，整个网站都部署在树莓派上，在 Docker 容器中运行。Cloudflare Tunnels 用于安全地将网站暴露给互联网，将树莓派的内部端口映射到子域。

作者收到了来自世界各地的一千多条消息，包括 ASCII 艺术、诗歌和地点问候语，这些消息被映射到物理世界地图上。他们对积极和富有创意的回应表示欣喜，强调了通过物理媒介促进匿名连接的乐趣。该项目的源代码可在 GitHub 上找到。

---

## 19. Windows 10 截止日期 促进 Mac 销量

**原文标题**: Windows 10 Deadline Boosts Mac Sales

**原文链接**: [https://www.macrumors.com/2025/10/25/windows-10-deadline-boosts-mac-sales/](https://www.macrumors.com/2025/10/25/windows-10-deadline-boosts-mac-sales/)

哈特利·查尔顿的文章报道称，即将于2025年10月到期的Windows 10停止支持期限正在推动重要的PC更换周期，从而使苹果公司受益，Mac销量有所增长。Counterpoint Research表明，全球近40%的PC仍运行Windows 10，这促使商业和消费领域提前升级。

苹果公司的Mac出货量在2025年第三季度同比增长了14.9%，这得益于对新款MacBook型号的需求以及企业采用率的提高。联想仍然是最大的PC供应商，增长了17.4%，华硕也实现了14.1%的强劲增长。惠普的出货量增长了10.3%，这得益于商业销售的推动。戴尔是唯一一家出货量下降的主要供应商，下降了0.9%。

前五大PC供应商共同控制着全球市场约75%的份额。文章还强调了配备神经处理单元和人工智能功能的PC的出现。虽然人工智能功能尚未成为主要的销售驱动力，但企业买家开始在采购决策中优先考虑人工智能能力，以面向未来做好硬件准备。

---

## 20. 公立蒙台梭利项目以更低的成本提高学习成果：研究

**原文标题**: Public Montessori programs strengthen learning outcomes at lower costs: study

**原文链接**: [https://phys.org/news/2025-10-national-montessori-early-outcomes-sharply.html](https://phys.org/news/2025-10-national-montessori-early-outcomes-sharply.html)

一项由弗吉尼亚大学、宾夕法尼亚大学和美国研究所的研究人员领导的全国性研究发现，公立蒙台梭利幼儿园项目（3-6岁）能显著提高儿童的早期学习成果，且比传统幼儿园项目更具成本效益。这项发表在《美国国家科学院院刊》上的随机对照试验跟踪了24个公立蒙台梭利项目的近600名儿童。

研究表明，到幼儿园结束时，蒙台梭利学生在阅读、执行功能、短期记忆和社会理解方面均优于同龄人。值得注意的是，这些益处能够长期保持，这与许多学前教育项目的收益往往会消退的情况不同。

一项关键发现是蒙台梭利项目相关的成本节约，与传统的公立幼儿园相比，每个儿童在三年内（3-6岁）的费用大约减少了13000美元。这种效率归因于更有效的课堂结构，包括跨年龄组的同伴互助学习。研究人员还强调，由于蒙台梭利项目中教师士气和留任率的提高，可能会带来额外的成本节约。

蒙台梭利教育的益处在所有儿童身上都得到了体现，但在来自低收入家庭的儿童身上尤其明显，这与蒙台梭利方法的最初意图相符。研究人员希望这项研究能够为寻求以有限资源改善教育成果的政策制定者和教育领导者提供参考。

---

## 21. 像外科医生一样编程

**原文标题**: Code like a surgeon

**原文链接**: [https://www.geoffreylitt.com/2025/10/24/code-like-a-surgeon](https://www.geoffreylitt.com/2025/10/24/code-like-a-surgeon)

作者在2025年10月的文章中倡导一种“像外科医生一样编码”的软件开发方法，即利用人工智能工具来增强，而不是取代人类程序员。核心思想是将次要的、“繁重”的任务委托给人工智能代理，从而使人类开发人员能够专注于核心的、创造性的编码方面，例如设计原型。

作者概述了几项非常适合人工智能辅助的任务：编写代码指南、快速实现变更、修复明显的错误以及编写文档。这些任务可以异步运行，甚至可以通宵运行，以最大限度地提高开发人员的效率。这与主要任务形成对比，在主要任务中，作者更喜欢亲自动手编码，并更谨慎地使用人工智能，例如使用标签补全，以实现更快的反馈循环。

他强调了“自主滑块”的重要性，根据任务调整人工智能的参与程度。他承认了《人月神话》中的“首席程序员”概念，但指出人工智能现在使这种方法在经济上可行，并避免了围绕繁重工作的地位等级问题。

作者感谢在Notion工作，该公司支持人工智能编码工具，并将Notion的产品视为旨在通过委派次要任务并专注于核心职责来使知识工作者能够“像外科医生一样工作”。他最后建议阅读有关人机协作的相关读物。

---

## 22. 数学方法几何

**原文标题**: The geometry of mathematical methods

**原文链接**: [https://books.physics.oregonstate.edu/GMM/book.html](https://books.physics.oregonstate.edu/GMM/book.html)

无法访问文章链接。

---

## 23. 钻石导热性：芯片散热新纪元

**原文标题**: Diamond Thermal Conductivity: A New Era in Chip Cooling

**原文链接**: [https://spectrum.ieee.org/diamond-thermal-conductivity](https://spectrum.ieee.org/diamond-thermal-conductivity)

本文探讨了芯片冷却技术的一项突破，即在半导体器件上直接生长一层微米级厚度的多晶金刚石。随着晶体管变得更小、密度更高，散热管理成为一项关键挑战，会导致性能下降和潜在的损坏。对于先进的芯片架构，特别是3D堆叠设计，目前的散热方法（如散热片和液体冷却）正变得不足。

斯坦福大学的研究人员开发了一种在低温（400°C）下生长金刚石涂层的方法，使其与敏感的芯片组件兼容。金刚石具有高导热性和电绝缘性，非常适合散热。这种新方法解决了传统金刚石生长需要高温的局限性。

该团队发现，在生长过程中添加氧气可以防止烟尘形成，并且他们能够制造出有效散热的大颗粒金刚石涂层。他们还发现，在金刚石和半导体之间的边界处形成一层碳化硅，充当声子的“桥梁”，从而改善热传递。

对氮化镓HEMT进行的金刚石涂层测试表明，温度显著下降（70°C），信号放大能力得到改善。研究团队认为，金刚石层也可以应用于CMOS芯片，尤其是在3D堆叠架构中，热提取是一项重大挑战。这项技术引起了应用材料、三星和台积电等芯片行业领导者的兴趣。

---

## 24. 传统的延续：亨利·西梅奥尼斯案例研究 (2023)

**原文标题**: The persistence of tradition: the curious case of Henry Symeonis (2023)

**原文链接**: [https://blogs.bodleian.ox.ac.uk/archivesandmanuscripts/2023/12/13/the-persistence-of-tradition-the-curious-case-of-henry-symeonis/](https://blogs.bodleian.ox.ac.uk/archivesandmanuscripts/2023/12/13/the-persistence-of-tradition-the-curious-case-of-henry-symeonis/)

无法访问文章链接。

---

## 25. 快速 TypeScript (代码复杂度) 分析器

**原文标题**: Fast TypeScript (Code Complexity) Analyzer

**原文链接**: [https://ftaproject.dev/](https://ftaproject.dev/)

FTA (快速 TypeScript 分析器) 是一个基于 Rust 的静态分析工具，旨在快速评估 TypeScript 和 JavaScript 代码的复杂性和可维护性。它利用 swc 进行解析，然后应用各种分析例程。

FTA 速度极快，在典型硬件上每秒能够分析多达 1600 个文件。用户可以使用简单的 `npx fta-cli path/to/project` 命令，通过 `fta-cli` 命令行界面轻松集成它。

该工具提供一个摘要表，突出显示每个文件的关键指标，包括行数、FTA 分数（越低越好）和总体评估（例如，“需要改进”、“良好”）。正如针对 Redux 项目的示例输出所展示的那样，FTA 提供特定于文件的评估。

除了摘要之外，FTA 还公开详细指标，包括圈复杂度和 Halstead 指标，从而可以进行深入分析。它以 JSON 格式呈现这些指标，包含 "file_name"、"cyclo"、"halstead"、"line_count"、"fta_score" 和 "assessment"。 有一个在线演示环境可供查看 FTA 如何分析代码。

FTA 是开源的，并鼓励通过其 GitHub 存储库进行社区参与。

---

## 26. 沉迷屏幕的真实现状：老年人

**原文标题**: Meet the real screen addicts: the elderly

**原文链接**: [https://www.economist.com/international/2025/10/23/meet-the-real-screen-addicts-the-elderly](https://www.economist.com/international/2025/10/23/meet-the-real-screen-addicts-the-elderly)

无法访问文章链接。

---

## 27. Twake Drive – Google Drive 的开源替代方案

**原文标题**: Twake Drive – An open-source alternative to Google Drive

**原文链接**: [https://github.com/linagora/twake-drive](https://github.com/linagora/twake-drive)

Twake Drive：Google Drive的开源替代方案。本文概述了该项目，并提供了在本地和开发环境中运行它的说明。

本地设置包括克隆Git仓库，进入`tdrive`目录，并使用带有`docker-compose.minimal.yml`文件的Docker Compose。这允许用户在`http://localhost/`访问该应用程序。

对于开发环境，先决条件是Node.js (版本18或更高)，MongoDB和Yarn。 说明详细介绍了使用Docker启动MongoDB，然后使用Yarn分别启动前端和后端。后端需要设置几个环境变量，包括数据库连接详细信息和存储路径，这些变量也可以使用`development.json`文件进行配置。 然后，该应用程序将在端口3000上运行。

本文还包括指向该项目的Telegram频道、网站、问题跟踪器和路线图的链接。 该软件在Affero GPL v3下获得许可。

---

## 28. 陆奥的表演

**原文标题**: Luau's performance

**原文链接**: [https://luau.org/performance](https://luau.org/performance)

本文详细介绍了Luau的性能优化，重点在于其使惯用代码更快并支持通过调整实现更高性能的目标。与LuaJIT不同，由于平台限制，Luau优先考虑稳定的解释执行性能，尽管现在它包含一个可选的JIT组件，用于支持类型注解的x64/arm64架构。

主要优化包括高度优化的字节码解释器、多趟优化编译器（具有常量折叠和过程间优化）以及避免断点行钩子的 epsilon 开销调试器。

Luau 利用内联缓存来实现快速的表和全局访问，尤其是在编译时已知字段名称且元表结构高效时。 它还实现了“imports”来优化全局函数链，如 `math.max`，在脚本加载期间对其进行优化，但此优化会被 `loadstring` 或 `getfenv/setfenv` 等函数失效。

方法调用通过编译器/VM优化进行专门化，特别是对于通过“namecall”机制反映的用户数据。 内置函数调用通过“fastcall”机制进行优化，该机制直接从解释器核心调用专门的实现，并且对 assert、bit32.extract 和 select 的部分专门化减少了常见情况的开销。 Luau 还通过为标准 `ipairs`、`pairs` 和 `next` 模式定制的迭代器提供优化的表迭代。

---

## 29. 为何形式化数学——不仅仅是为了发现错误

**原文标题**: Why formalize mathematics – more than catching errors

**原文链接**: [https://rkirov.github.io/posts/why_lean/](https://rkirov.github.io/posts/why_lean/)

本文认为，数学形式化，尤其是借助Lean等工具，带来的好处不仅仅是发现证明中的错误。虽然错误检测很有价值，但作者借鉴了软件工程中TypeScript的应用，来说明其他优势。

TypeScript的价值不仅在于发现错误，还包括为开发者工具提供支持（CTRL-点击跳转定义、重构）、作为早期规范的设计语言，以及在编码过程中提供即时正确性反馈。 同样，数学形式化也提供以下好处：

*   **增强数学工具：** 为数学家提供类似IDE的支持，包括点击跳转定义、自动生成文档和非字符串搜索，这些在非正式的数学实践（如使用LaTeX）中基本上是不可用的。

*   **元数学分析：** 能够更容易地生成数学证明结构，帮助发现替代证明路径和可视化依赖关系图。

*   **数学的版本控制：** 促进将数学结果作为具有版本和依赖关系的库进行管理，简化数学知识的演进，尤其是在出现撤回时。

作者承认，形式化需要证明即使是“微不足道”的陈述，这会带来一个学习曲线。 然而，策略的不断增强简化了这个过程。 此外，仅形式化陈述本身，正如文艺复兴慈善项目所展示的那样，就已经是一项有价值的努力。 作者最后表示希望，尽管需要最初的投入，这些综合优势将鼓励数学家采用形式化方法。

---

## 30. DNA揭示了导致拿破仑军队覆灭的真凶

**原文标题**: DNA reveals the real killers that brought down Napoleon's army

**原文链接**: [https://www.gavi.org/vaccineswork/dna-reveals-real-killers-brought-down-napoleons-army](https://www.gavi.org/vaccineswork/dna-reveals-real-killers-brought-down-napoleons-army)

DNA分析改写拿破仑军队溃败原因：肠热病和回归热或为主因

本文探讨了对士兵遗骸进行DNA分析如何改写了对1812年拿破仑大军从俄罗斯撤退期间遭受重创原因的理解。两个多世纪以来，斑疹伤寒一直被认为是造成数万人死亡的主要原因。然而，一项由尼古拉斯·拉斯科万博士领导的新研究，利用下一代DNA测序技术分析了在立陶宛埋葬的士兵的牙齿，发现了*肠道沙门氏菌*和*回归热疏螺旋体*的痕迹，这两种细菌分别是引起肠热（副伤寒）和回归热的罪魁祸首。

虽然斑疹伤寒被认为是主要原因，但研究小组几乎没有发现其存在的证据。 *肠道沙门氏菌*通过受污染的食物和水传播，而*回归热疏螺旋体*则通过体虱传播。该研究表明，这些病原体的存在，加上寒冷、饥饿和疲惫的极端条件，极大地促成了军队的溃败。

这项研究强调了古代DNA技术在揭示历史传染病以及提供对其进化、传播和消失的见解方面的力量。 这些信息对于更好地理解和应对当今的传染病具有重要价值。 最初的研究发表在《当代生物学》上。

---

## 31. DNA揭示了导致拿破仑军队覆灭的真凶

**原文标题**: DNA reveals the real killers that brought down Napoleon's army

**原文链接**: [https://www.gavi.org/vaccineswork/dna-reveals-real-killers-brought-down-napoleons-army](https://www.gavi.org/vaccineswork/dna-reveals-real-killers-brought-down-napoleons-army)

本文探讨了一项最新研究，该研究重新审视了拿破仑的“大军”在1812年从俄罗斯撤退期间遭受惨重损失的原因。 尽管历史学家传统上将大量伤亡归因于斑疹伤寒、寒冷和饥饿，但一项从埋葬在立陶宛的士兵牙齿中提取的DNA新分析表明情况更为复杂。

该研究由尼古拉斯·拉斯科凡博士领导，利用先进的DNA测序技术来鉴定遗骸中存在的病原体。 与预期相反，研究人员发现了鼠伤寒沙门氏菌（引起肠热/副伤寒）和回归热疏螺旋体（引起回归热）的证据，而不是斑疹伤寒。 这两种细菌都会引起高烧、疲劳和消化问题等症状。

虽然这项研究无法明确量化这些病原体对军队覆灭的贡献，但它提出，它们的同时存在可能加剧了士兵因精疲力竭、极度寒冷和饥饿而已经虚弱的状况。 该发现突显了古代DNA技术在揭示传染病历史以及为理解和应对现代传染病提供宝贵见解方面的力量。 这项发表在《当代生物学》上的研究强调了在分析历史疾病爆发时考虑多种因素的重要性。

---

## 32. 欧洲警方捣毁拥有4900万虚假账户的网络犯罪团伙

**原文标题**: Euro cops take down cybercrime network with 49M fake accounts

**原文链接**: [https://www.itnews.com.au/news/euro-cops-take-down-cybercrime-network-with-49-million-fake-accounts-621174](https://www.itnews.com.au/news/euro-cops-take-down-cybercrime-network-with-49-million-fake-accounts-621174)

欧洲刑警组织主导的“SIM卡联盟”行动瓦解大型网络犯罪服务网络，该网络协助创建约4900万个虚假在线账户。该行动于10月10日在拉脱维亚展开，拉脱维亚、奥地利、爱沙尼亚和芬兰的警察部队参与其中，逮捕了七名个人。

该网络提供来自80多个国家的临时电话号码，使犯罪分子能够绕过双重身份验证，并在社交媒体和通信平台上创建欺诈账户。这些虚假账户随后被用于各种诈骗活动，包括投资诈骗、虚假在线商店、网络钓鱼攻击、敲诈勒索、偷运移民以及传播儿童性虐待材料。采用的策略包括“冒充子女诈骗”和冒充警务人员。

当局查获了1200个包含40000张有效SIM卡的SIM卡盒、五台互联网服务器，并关闭了两个提供非法服务的网站（gogetsms.com和apisim.com）。该网络在奥地利造成的经济损失达到450万欧元，在拉脱维亚造成的经济损失达到42万欧元。查获了约43.1万欧元和51.6万美元的加密货币。

欧洲刑警组织提供了分析支持、情报和法证专业知识，并与Shadowserver基金会合作拆除技术基础设施。文章还提到纽约市类似的一次“SIM卡农场”突袭行动，涉及300台设备和超过10万张SIM卡，可能由国家行为者操控。

---

## 33. 我在代码审查中看到的工程师常犯的错误

**原文标题**: Mistakes I see engineers making in their code reviews

**原文链接**: [https://www.seangoedecke.com/good-code-reviews/](https://www.seangoedecke.com/good-code-reviews/)

本文讨论了工程师在代码审查过程中常犯的错误，尤其是在人工智能生成代码的时代。作者认为，有效的代码审查不仅仅是检查差异（代码中的变更）。它需要理解更广泛的代码库，以确保一致性并防止重复。

要点包括：

*   **不要只审查差异：** 关注代码在更大系统中的整体上下文。
*   **不要留下太多评论：** 专注于最重要的问题，并提出一般风格的更改建议，而不是大量的逐行评论。避免过多的吹毛求疵。
*   **不要以“我会怎么写？”的视角进行审查：** 接受不同的方法，只要它们是有效的。
*   **如果你想阻止，留下阻止审查：** 明确表明更改是否不可接受。
*   **大多数审查应该是批准：** 阻止审查可能表明更深层次的结构问题或过度的把关。倾向于批准即使是细微改进的变更。

作者强调了优先考虑团队知识共享、发现错误和强制执行代码风格的重要性，同时平衡个人偏好。文章还指出，基于LLM的审查工具与人工审查员相比存在局限性，尤其是在将一般上下文引入审查过程方面。这里提出的原则是软件工程师进行有效、全面的代码审查的重要考量。

---

## 34. 如何制作史密斯圆图

**原文标题**: How to make a Smith chart

**原文链接**: [https://www.johndcook.com/blog/2025/10/23/smith-chart/](https://www.johndcook.com/blog/2025/10/23/smith-chart/)

本文阐述了创建史密斯圆图的数学基础，史密斯圆图是电气工程中使用的一种工具。文章通过描述使用函数f(z) = (z − 1)/(z + 1)（一种特定的莫比乌斯变换）将直角坐标网格从右半平面（z平面）变换到单位圆（w平面）的过程来进行说明。

作者侧重于*如何*创建圆图，而非*如何*使用它。要点包括：

*   莫比乌斯变换将广义圆（圆或直线）映射到广义圆。
*   z平面中的虚轴映射到w平面中的单位圆，右半平面映射到单位圆内部。
*   z平面中的垂直线（实部恒定）映射到w平面中单位圆内的圆，所有圆都与单位圆在w = 1处相切。
*   z平面中的水平线（虚部恒定），除去实轴，映射到w平面中与单位圆相交并穿过w = 1的圆。实轴映射到区间[-1,1]。
*   该映射是保角的，意味着它保留了相交的角度。

w平面中生成的网格间距不均匀，右侧拥挤。实用的史密斯圆图需要更均匀的分布，这通过映射来自z平面中不均匀间隔的网格来实现。作者指出后续文章将讨论间距问题。

---

## 35. Mesh2Motion – 开源的3D模型动画Web应用

**原文标题**: Mesh2Motion – Open-source web application to animate 3D models

**原文链接**: [https://mesh2motion.org/](https://mesh2motion.org/)

Mesh2Motion：一款用于动画3D模型的免费开源Web应用。它允许用户将他们的3D创作栩栩如生，并支持类人、四足动物和鸟类生物。该工具支持导入常见的3D模型格式，如GLB、GLTF和FBX，并提供人类和动物骨骼选项。

主要功能包括直观的骨骼定位，以及用于纠正错误的撤销/重做系统。用户可以一次性导出多种动画，格式为广泛支持的GLB格式，并可以访问来自Quaternius的人类动画库。

该项目旨在为个人和商业用途提供一个易于访问的免费动画工具，并随着3D动画和建模的进步而不断发展。源代码可在GitHub上获取。用户可以在GitHub页面上或通过开发者的社交媒体渠道报告错误并提供反馈。

---

## 36. 现代完美哈希

**原文标题**: Modern Perfect Hashing

**原文链接**: [https://blog.sesse.net/blog/tech/2025-10-23-21-23_modern_perfect_hashing.html](https://blog.sesse.net/blog/tech/2025-10-23-21-23_modern_perfect_hashing.html)

Steinar Gunderson探讨了他实现的现代完美字符串哈希，旨在将一组固定的字符串映射到整数。与典型的哈希表不同，完美哈希利用预先已知的字符串集合进行优化。他的用例涉及大约一千个字符串，允许几分钟的构建时间。

他首先按字符串长度分割字符串，以优化`memcmp`操作。由于潜在的表大小问题和缺乏Arm支持，他避免使用PEXT（位提取）。相反，他采用了一种“魔术乘法”技术，灵感来自电脑象棋，其中`(value & mask) * magic`生成无冲突的高位。他展示了使用这种方法的代码示例，强调了魔术数字和位移如何为字符串创建不同的索引，需要验证以避免冲突。他强调了选择乘法位和数据类型的灵活性。

对于只有少数值的情况，简单的`memcmp`就足够了。找到最佳魔术值涉及一种反复试验的方法，通过优先检查先前冲突的值对的“杀手启发式”来加速。当找不到合适的魔术值时，他尝试拆分问题。与Wojciech Muła建议的基于字符的拆分不同，他基于单个字符的存在或不存在将字符串集分成两组，这产生了更可预测的分支和更有效的哈希计算。然后，他通过评估两个拆分生成的完美哈希的成本来选择最佳拆分。

最终，他的实现实现了gperf两倍的运行时速度，代码大小只有一半，但搜索拆分和魔术值的复杂性使其速度较慢。他建议有兴趣创建更现代的gperf的人进一步探索这个领域。

---

## 37. Conductor (YC S24) 正在旧金山招聘创始工程师

**原文标题**: Conductor (YC S24) Is Hiring a Founding Engineer in San Francisco

**原文链接**: [https://www.ycombinator.com/companies/conductor/jobs/MYjJzBV-founding-engineer](https://www.ycombinator.com/companies/conductor/jobs/MYjJzBV-founding-engineer)

Conductor，一家YC S24创业公司，专注于并行化编码代理（主要使用Claude），正在旧金山寻找一位创始工程师。包括YC、Linear、Vercel等公司的工程师都在使用该公司，该公司也在构建用于协调AI团队的新界面。

创始人Charlie和Jackson在布朗大学相识，他们强调快节奏、低官僚的环境，新员工可以在其中产生重大影响。团队目前由三人组成。他们正在寻找一位能够设计、原型设计和构建的“万事通”。TypeScript经验加分，但并非必需。

薪酬包括中位数工资（14万至20万美元）以及高于同阶段公司的股权（0.50%至1.50%）。福利包括Aetna PPO健康保险、Guardian牙科和视力保险、6% 401k匹配以及健康和福祉资源。公司鼓励员工对福利提出建议，并提供用于工作相关费用的信用卡，以消除费用报销。

面试流程包括初步电话沟通，可能需要在旧金山一起工作一两天，然后是offer。Conductor由顶级投资者支持，并拥有充足的资金。他们强调在旧金山办公室进行面对面工作。

---

## 38. 古惑仔

**原文标题**: The Goon Squad

**原文链接**: [https://harpers.org/archive/2025/11/the-goon-squad-daniel-kolitz-porn-masturbation-loneliness/](https://harpers.org/archive/2025/11/the-goon-squad-daniel-kolitz-porn-masturbation-loneliness/)

丹尼尔·科利茨的《恶棍小队》探索了新兴的“gooning”亚文化，这是一种旨在达到自我死亡或极乐状态（称为“goonstate”）的新型长时间手淫形式。文章以诺提卡·马龙的故事开篇，他的公共性犯罪和随后的自杀，被戏称为“Goonicide”，讽刺地将他变成了这场运动的殉道者。

科利茨深入研究了gooning的起源，追溯到4chan等在线社区和Rabbit等平台。他描述了专门用于观看色情片的“gooncaves”（恶棍洞穴）以及gooners聚集的在线空间，特别是像GoonVerse这样的Discord服务器。这些空间揭示了令人惊讶的清醒意识和露骨内容的混合。

作者试图通过采访“Gooncultist”（恶棍邪教徒）并向一百多名gooners分发问卷来理解gooner现象。数据表明，虽然“goonstate”是亚文化身份的核心，但很少有人能达到这种状态。问卷调查的回复将理想状态描述为一种自我消解的形式。

最终，这篇文章描绘了一个复杂而多样的亚文化，它是由在线色情内容的泛滥所驱动的，并提供了一个潜在的视角，让我们得以窥见技术和性行为以意想不到的方式相交的未来，从而引发了关于孤独和人类状况的思考。

---

## 39. Debian技术委员会否决systemd变更

**原文标题**: Debian Technical Committee overrides systemd change

**原文链接**: [https://lwn.net/Articles/1041316/](https://lwn.net/Articles/1041316/)

2025年10月，Debian技术委员会(TC)否决了一项systemd变更，该变更破坏了依赖于全局可写`/run/lock`目录的软件。 Systemd v258将`/run/lock`设置为仅root可写，导致UUCP和cu等程序无法正常工作，并可能影响alsa-utils。这与Debian策略相悖，Debian策略仍然引用文件系统层级标准(FHS)，该标准要求`/var/lock`（指向`/run/lock`的符号链接）用于锁文件。

Systemd维护者认为全局可写的`/run/lock`存在安全风险，建议发行版可以通过tmpfiles.d自行管理该目录。但是，Debian维护者Marco d'Itri认为Debian策略强制要求符合FHS，因此向TC提出了请求。

TC同意systemd必须遵守Debian策略，直到受影响的软件迁移到像flock()这样的现代锁定机制。他们决定systemd必须提供具有宽松权限的`/var/lock`，以使现有软件能够正常运行。虽然TC同情锁定机制的现代化，但他们强调Debian开发人员有责任确保策略合规性。计划发布一个补丁来恢复systemd的行为。文章还涉及从UUCP风格锁定过渡的复杂性，特别是涉及第三方和潜在的闭源软件。

---

## 40. 为什么Transformer学不会乘法？

**原文标题**: Why can't transformers learn multiplication?

**原文链接**: [https://arxiv.org/abs/2510.00184](https://arxiv.org/abs/2510.00184)

本文《为什么Transformer无法学会乘法？逆向工程揭示长程依赖的陷阱》研究了Transformer模型尽管能力不断增强，但在多位数乘法方面仍然存在困难的原因。作者通过逆向工程一个*能够*成功通过隐式链式思考学习乘法的模型，来理解其底层机制。

他们确定了三个关键发现：首先，成功的模型编码了多位数乘法所需的必要长程依赖。其次，该模型利用注意力机制构建了一个有向无环图，有效地缓存和检索成对的中间结果。第三，该模型使用傅里叶基表示数字，并通过注意力头中的闵可夫斯基和实现中间结果，从而创建了标准微调模型所缺乏的有效表示。

然后，作者分析了标准微调的学习动态，揭示了它通常会收敛到缺乏所需长程依赖的次优解。为了验证这一点，他们引入了一个辅助损失函数，该函数使用线性回归预测“运行总和”，从而有效地提供了一个归纳偏置。这种偏置使模型能够成功学习多位数乘法。

总之，该研究揭示了Transformer在标准微调期间学习长程依赖的一个关键陷阱，并展示了适当的归纳偏置如何克服这一限制，特别是通过使用“运行总和”辅助损失。该论文强调了理解底层机制和表示选择对于在需要复杂推理的任务上有效训练Transformer的重要性。

---

## 41. 新晋首席技术个人贡献者的一些建议（即，写给自己的备忘录）

**原文标题**: Advice for new principal tech ICs (i.e., notes to myself)

**原文链接**: [https://eugeneyan.com/writing/principal/](https://eugeneyan.com/writing/principal/)

本文为新任首席技术专家 (Principal Technical IC) 提供建议，主要基于作者在亚马逊中心环境中的观察和经验，但也适用于其他类似职位。其核心信息在于从个人贡献向更广泛的影响力、沟通和战略思维转变。

关键建议包括：

*   **找到你的“特色”**: 认识到不同的首席专家擅长不同的领域 (深度钻研、横向影响力、开拓创新、协调一致)，并找到你的优势。
*   **优先考虑影响力而非编码**: 核心角色从亲身编码转变为技术愿景、设计反馈、支持指导和连接各方，尽管编码对于保持联系仍然重要。
*   **成为“兼职全才”**: 承担工程以外的职责，包括产品、设计、财务、文化等。
*   **掌握影响力和沟通**: 有效地协调不同层级的团队，并使他人信服你的想法。
*   **教学和指导**: 指导他人提高效率，并委派任务以促进组织内的成长。
*   **连接各方**: 促进团队之间的协作，并识别能够为特定项目做出贡献的个人。
*   **平衡广度和深度**: 了解全局的同时，也要考虑局部解决方案，并咨询一线专家。
*   **保护你的时间**: 学会拒绝不必要的会议，并专注于高杠杆活动。
*   **章程对齐**: 定义你的角色（所有者、赞助者、顾问），并使其与领导层的期望保持一致。
*   **建立支持网络**: 与其他首席专家建立联系，以进行开放式沟通和支持。
*   **优先考虑自我关怀**: 确保有时间进行个人学习、成长和幸福，以防止倦怠。

---

## 42. 科技行业男性接受整形手术的年龄提前数十年

**原文标题**: Tech industry men getting plastic surgery decades earlier

**原文链接**: [https://www.wsj.com/style/fashion/why-tech-bros-are-getting-face-lifts-now-94278bb7](https://www.wsj.com/style/fashion/why-tech-bros-are-getting-face-lifts-now-94278bb7)

无法访问文章链接。

---

## 43. 修复并不容易，C语言优先级惹的祸。

**原文标题**: The fix wasn't easy, or C precedence bites

**原文链接**: [https://boston.conman.org/2025/10/20.1](https://boston.conman.org/2025/10/20.1)

作者讨论了mod_blog软件的万圣节版本发布，其中涉及移除一些长期存在的功能。具有讽刺意味的是，这个版本的发布源于修复一个错误，而这个错误又引入了另一个更为隐蔽的错误。

最初的错误涉及URL解码，特别是处理'%'之后的十六进制字符。"修复"后的版本在检查字符是否为有效的十六进制数字时，运算符优先级出现了错误。作者错误地写成了`!isxdigit(*src+1)`，这被解释为`!isxdigit(src[0] + 1)`，而不是`!isxdigit(src[1])`。由于很少使用Web界面（该错误出现的地方），因此这个错误没有被注意到。

作者还移除了处理输入以自动添加`<P>`标签的功能（因为他们目前使用自定义标记语言），以及新文章的电子邮件通知。电子邮件通知最初被添加，但垃圾邮件和低兴趣导致了它们的移除。虽然大多数电子邮件功能都被移除，但实现了一个钩子机制，以继续支持少数现有订阅者（包括作者及其合作伙伴）。

总共移除了超过3000行代码，作者发现这有点吓人，但最终在减少维护方面是有益的。文章最后链接到Lemmy和Hacker News上的讨论。

---

## 44. Typst 0.14

**原文标题**: Typst 0.14

**原文链接**: [https://typst.app/blog/2025/typst-0.14/](https://typst.app/blog/2025/typst-0.14/)

Typst 0.14 版本发布于 2025 年 10 月 24 日，重点在于扩展可访问性、扩大在生产环境中的应用以及用于改进文档创建的新功能。主要功能包括：

*   **默认启用可访问性：** Typst 现在生成可访问的 PDF，并为辅助技术自动添加标签。 新的 `alt` 参数允许为图形提供替代描述，从而提高视力障碍用户的可访问性。 支持 PDF/UA-1 导出，用于更严格的可访问性检查以及符合 EAA 和 ADA Title II 等法规。
*   **扩展的 PDF 标准支持：** Typst 支持多个 PDF 版本（1.4 到 2.0）以及 PDF/A 标准的所有四个部分，为特定用例提供优化的文档创建。
*   **PDF 作为原生图像：** 借助新的 hayro PDF 处理库，PDF 文件现在可以直接作为图像嵌入到 Typst 文档中，适用于所有导出目标（PDF、HTML、SVG、PNG），而无需系统依赖项。
*   **字符级对齐：** 此功能通过调整字符之间的间距来增强段落排版，从而产生视觉上平衡的段落。
*   **更丰富的 HTML 导出：** 改进的 HTML 导出现在包含许多内置元素的显示规则，从而可以将 Typst 元素语义映射到 HTML。 新的类型化 HTML 接口简化了 HTML 元素的构建。

该版本还包括一些小的突破性更改和弃用，详情请参见更新日志。 Typst Web 应用程序现在提供更好的版本升级体验，并具有自动兼容性检查功能。 计划于 11 月 7 日举行社区电话会议，讨论新版本并收集用户反馈。

---

## 45. 前往黑洞的星际任务

**原文标题**: Interstellar Mission to a Black Hole

**原文链接**: [https://www.centauri-dreams.org/2025/10/23/interstellar-mission-to-a-black-hole/](https://www.centauri-dreams.org/2025/10/23/interstellar-mission-to-a-black-hole/)

探索黑洞：星际任务的新目标

保罗·吉尔斯特的文章探讨了针对黑洞而非仅关注诸如比邻星等系外行星的星际任务的潜力。他强调了科西莫·班比的研究，后者认为银河系可能包含大量恒星质量黑洞，其中一些可能位于20-25光年内。

寻找这些黑洞，特别是孤立的黑洞，是一项挑战，但诸如微引力透镜、通过升级后的LIGO设施进行的引力波探测以及来自平方公里阵列（SKA）、ALMA和JWST的观测等技术前景广阔。

文章提出，一旦确定了附近的黑洞，就可以发射束缚帆船来研究其对时空的影响。可以部署两个纳米飞船，一个观察黑洞附近的另一个，以分析由克尔时空度规（对于旋转黑洞）引起的信号扭曲。任务还可以测试极端引力场中的基本常数，并确定黑洞是否具有事件视界，或者是否更适合描述为“无视界致密天体”。

吉尔斯特认为，探索黑洞可能会揭示意想不到的科学突破，就像过去的太空任务给我们带来惊喜一样。他还引用了一篇论文，该论文表明系外行星内的暗物质相互作用可能导致黑洞的形成，从而可能使这些物体更加丰富且可检测。文章最后强调，一旦星际旅行变得可行，黑洞探索就应该被视为一个值得考虑的任务目标。

---

## 46. 阿拉斯加航空关于IT系统故障的声明

**原文标题**: Alaska Airlines' statement on IT outage

**原文链接**: [https://news.alaskaair.com/on-the-record/alaska-statement-on-it-outage/](https://news.alaskaair.com/on-the-record/alaska-statement-on-it-outage/)

阿拉斯加航空于10月23日星期四遭遇重大IT故障，导致阿拉斯加航空和地平线航空的航班在全系统范围内停飞。故障源于太平洋时间下午3:30左右航空公司主数据中心发生故障。夏威夷航空的航班未受影响。

地面停飞于星期四太平洋时间晚上11:30解除，但中断造成了严重的延误和取消。截至10月25日星期六，该航空公司已取消阿拉斯加和地平线航空的400多架航班，影响了近5万名乘客的出行计划。

阿拉斯加航空对中断表示道歉，并向乘客保证他们正在努力尽快、安全地恢复正常运营。他们鼓励旅客在前往机场前查询航班状态，并实施了灵活的旅行政策。航空公司还增加了客户服务人员，以处理大量查询，并承认等待时间较长。

阿拉斯加航空强调，乘客安全从未受到威胁，且此次故障并非网络安全事件。他们承认，尽管今年早些时候发生类似中断后，他们曾努力“强化”系统，但仍需要做更多工作以确保系统稳定性。该航空公司正在引入外部技术专家来诊断其IT基础设施并增强其弹性。他们承诺会提供有关其进展的进一步更新。

---

## 47. 与克劳德的危险生活

**原文标题**: Living Dangerously with Claude

**原文链接**: [https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/](https://simonwillison.net/2025/Oct/22/living-dangerously-with-claude/)

Simon Willison的博文《与Claude共舞的危险：YOLO模式》探讨了以不受限制的权限运行像Claude Code这样的编码代理的风险与收益，他称之为“YOLO模式”。YOLO模式虽然释放了编码代理的全部潜力，使其能够在后台进行复杂的难题解决，但也带来了重大的安全风险。

文章重点介绍了在YOLO模式下完成的三个项目，展示了其效率：让DeepSeek-OCR在NVIDIA Spark上运行，在WebAssembly沙箱中运行服务器端Python代码，以及在WebAssembly中运行Perl工具SLOCCount。然而，这种自由是有代价的。

主要的危险是提示注入，注入到代理上下文中的恶意代码可能会危及系统安全，尤其是当它与访问私有数据和外部通信能力（“致命三要素”）结合使用时。攻击者可以诱骗代理泄露敏感信息，如API密钥。

Willison认为，依靠人工智能来检测提示注入攻击是不可靠的。唯一可信的解决方案是沙箱，最好是在第三方的计算机上。他讨论了控制文件系统访问，更重要的是，限制网络连接以防止数据泄露。

Claude Code CLI现在包含了使用Apple的`sandbox-exec`命令的沙箱功能，允许通过HTTP代理控制网络访问。尽管`sandbox-exec`已被弃用，但它仍然是一个便捷的解决方案。

总而言之，Willison提倡使用YOLO模式的编码代理，因为它功能强大，但强调必须在强大的沙箱中进行操作，以减轻提示注入和数据泄露的风险。

---

## 48. 阿拉斯加航空IT系统再次中断，寻求外部援助

**原文标题**: After another IT outage, Alaska Airlines is bringing in outside help

**原文链接**: [https://www.seattletimes.com/business/boeing-aerospace/alaska-airlines-to-review-it-systems-after-2-outages-in-four-months/](https://www.seattletimes.com/business/boeing-aerospace/alaska-airlines-to-review-it-systems-after-2-outages-in-four-months/)

阿拉斯加航空公司将在过去四个月内发生两次重大系统故障后，引入外部顾问来审查其IT系统。最近一次故障发生在1月20日，导致航班停飞，并扰乱了该航空公司网络中数千名乘客的旅行。此前在2023年4月也发生过类似事件。

该航空公司承认这些故障造成了不可接受的混乱，并旨在找出根本原因并实施预防措施。首席执行官Ben Minicucci表示，重点是加强其技术基础设施的可靠性。虽然有关外部公司的具体细节尚未披露，但预计审查将是全面的，并涵盖阿拉斯加航空公司IT运营的各个方面。

这些故障突显了航空业对复杂IT系统日益增长的依赖，以及即使是短暂的中断也可能对运营和客户体验产生的重大影响。该航空公司希望外部审查能够防止未来事件的发生，并恢复对其平稳运营能力的信心。与此同时，阿拉斯加航空公司还在努力整合其与夏威夷航空公司的运营，这增加了其IT需求的复杂性。

---

## 49. ChatGPT说这话是懒惰的表现

**原文标题**: "ChatGPT said this" Is Lazy

**原文链接**: [https://terriblesoftware.org/2025/10/24/chatgpt-said-this-is-lazy/](https://terriblesoftware.org/2025/10/24/chatgpt-said-this-is-lazy/)

本文批判了在诸如代码审查、设计文档和团队沟通等专业场合，直接使用ChatGPT输出作为反馈的懒惰做法。作者认为，简单地粘贴人工智能生成的文本，而没有上下文或个人思考，是无益的，并且会给他人带来更多的工作。

核心问题在于，“ChatGPT这么说”缺乏人类理解和应用于具体情况的关键要素。ChatGPT不对结果负责，不了解团队的背景，也无法掌握技术债务或业务约束的细微之处。

作者认为，有效的反馈应该是具体的、了解上下文的，并且展现出对问题的个人理解。它包括清晰地阐述问题，解释其与项目的相关性，并提供切实可行的解决方案。例如，一个好的审查应该指出导致O(n²)复杂度的特定嵌套循环，并建议使用哈希表作为替代方案，而不是粘贴一个通用的AI算法复杂度解释。

虽然承认人工智能在产生想法和学习方面的用处，但作者强调了使用人工智能作为工具来增强人类思考的重要性，而不是取代它。审查者的责任是认真参与工作，理解背景，并提供反映自己理解和判断的反馈。最终，你需要对你的反馈负责，所以要负责任地提供有意义的反馈。

---

## 50. ChunkLLM：加速LLM推理的轻量级可插拔框架

**原文标题**: ChunkLLM: A Lightweight Pluggable Framework for Accelerating LLMs Inference

**原文链接**: [https://arxiv.org/abs/2510.02361](https://arxiv.org/abs/2510.02361)

这篇arXiv论文，题为“ChunkLLM：一种用于加速LLM推理的轻量级可插拔框架”，介绍了一种旨在提高大型语言模型（LLM）在推理过程中效率的新框架。作者旨在解决自注意力机制的二次复杂度所造成的计算瓶颈。

ChunkLLM提出了一种轻量级可插拔训练框架，包含两个主要组件：QK适配器和Chunk适配器。QK适配器连接到每个Transformer层，执行特征压缩和chunk注意力获取。Chunk适配器位于底层，基于上下文语义信息检测chunk边界。

在训练期间，仅训练适配器，而骨干模型保持冻结。采用注意力蒸馏方法训练QK适配器，提高重要chunk的召回率。在推理期间，仅在检测到chunk边界时才触发chunk选择，从而加速处理。

在长文本和短文本基准测试上的实验表明，ChunkLLM在短文本上取得了相当的性能，并在保留48.58%的键值缓存的同时，保持了长文本上下文中98.64%的性能。重要的是，在处理12万字的长文本时，该框架实现了高达4.48倍于原始Transformer的加速。这表明ChunkLLM显著提高了LLM的推理速度，尤其是在长上下文任务中。

---

## 51. Apple II 上的 VisiCalc

**原文标题**: VisiCalc on the Apple II

**原文链接**: [https://stonetools.ghost.io/visicalc-apple2/](https://stonetools.ghost.io/visicalc-apple2/)

本文深入探讨了Apple II上开创性的电子表格软件VisiCalc，及其对计算机世界的影响。它揭穿了关于其引入的迷思，突出了它如何推动Apple II的销量。作者强调了VisiCalc出人意料的精心设计的界面和功能，证明了Dan Bricklin和Bob Frankston的远见卓识，尽管以现代标准来看它显得“笨拙”。

本文详细介绍了作者在AppleWin模拟器中使用VisiCalc的实践经验，探索了它的斜杠菜单、内存管理和教程。它解释了VisiCalc如何向新用户展示自己，并将这种方法与SuperCalc等更现代的程序进行了对比。特别是，该教程展示了VisiCalc的易用性和直观设计，即使在20世纪70年代的技术背景下也是如此。

涵盖的一个关键方面是VisiCalc的创新复制功能，它是现代复制粘贴的前身。本文还进一步解释了VisiCalc的影响，考察了大量模仿其布局和功能的“VisiClone”是如何出现的。

本文还深入探讨了VisiCalc的一个特定应用：“动物营养和饲养的电子表格应用”，说明了它如何扩大了计算机的可访问性和应用范围，超越了典型的办公环境。这个例子有助于展示该程序对农业社区产生的实际影响。作者最后强调了VisiCalc的设计理念的重要性，强调其用户友好性及其对数据处理的影响。

---

## 52. Normalize.css

**原文标题**: Normalize.css

**原文链接**: [https://csstools.github.io/normalize.css/](https://csstools.github.io/normalize.css/)

Normalize.css 旨在使浏览器更一致地按照现代 Web 标准渲染元素，是一种 CSS 重置方案。与更激进的 CSS 重置不同，它只针对需要在不同浏览器之间进行规范化的样式。

该文章强调了其与现代浏览器的兼容性（Chrome、Edge、Firefox ESR+、IE 9+、Safari 8+、Opera），并指出版本为 11.0.0。它鼓励用户下载该库或通过 npm 安装（`npm install @csstools/normalize.css`）。

文章还推广了关于 normalize.css 的进一步阅读，并提及其被 Twitter、GitHub、Bootstrap 和 HTML5 Boilerplate 等知名网站和框架广泛采用，表明其可靠性和有效性。 源代码可在 GitHub 上轻松获取。

---

## 53. “Attention is all you need”合著者称他“厌倦”了 Transformer

**原文标题**: 'Attention is all you need' coauthor says he's 'sick' of transformers

**原文链接**: [https://venturebeat.com/ai/sakana-ais-cto-says-hes-absolutely-sick-of-transformers-the-tech-that-powers](https://venturebeat.com/ai/sakana-ais-cto-says-hes-absolutely-sick-of-transformers-the-tech-that-powers)

好的，这是根据VentureBeat文章标题的摘要：

文章讨论了AI奠基性论文《Attention is All You Need》（介绍了Transformer架构）的合著者Llion Jones，表达了他对Transformer的沮丧和厌倦之情。作为Sakana AI的首席技术官，Jones表示他“绝对厌恶”目前驱动着大多数现代AI（包括大型语言模型LLM）的技术。

虽然文章可能没有详细说明他“厌恶”它们的*原因*（我基于典型的批评进行推断），但暗示了这可能是由于当前架构的局限性。Transformer虽然强大，但在扩展性、效率、可解释性和泛化方面面临挑战。文章可能暗示Jones和Sakana AI正在探索Transformer模型之外的替代AI架构。

文章强调了这项革命性技术的核心发明者之一现在对其表达不满的讽刺意味。这表明了AI研究界更广泛的情绪——认识到虽然Transformer已经取得了巨大的成功，但该领域需要探索新的方法来克服固有的局限性，并在人工智能方面取得进一步的进展。文章将Sakana AI定位为可能正在追求AI开发的新途径，暗示着摆脱基于Transformer的模型。

---

## 54. 早期宇宙或曾存在“结支配时代”：研究

**原文标题**: A “knot dominated era” may have existed in the early universe: study

**原文链接**: [https://phys.org/news/2025-10-key-universe-1800s-idea-science.html](https://phys.org/news/2025-10-key-universe-1800s-idea-science.html)

本文探讨了一个新理论，该理论提出早期宇宙中形成的“宇宙结”可以解释物质与反物质之间的不平衡，这是物理学中一个尚未解决的重大难题。广岛大学的研究人员将规范化的重子数减去轻子数(B-L)对称性与Peccei–Quinn (PQ)对称性相结合，认为这些结自然产生，并在早期宇宙中短暂地占据主导地位。

B-L对称性引入了重型右手中微子，而PQ对称性解决了强CP问题，并引入了轴子，一种暗物质候选者。这些对称性的相互作用可以从磁通管弦和超流体涡旋中产生稳定的结孤子。与辐射不同，这些结能量损失缓慢，导致了“结主导时代”。它们最终通过量子隧穿解开，产生右手中微子，这些中微子在衰变时偏向物质，从而产生了我们今天观察到的物质盈余。

该模型表明，这个过程产生的重加热温度为100 GeV，这是物质创造的关键窗口。这种情况也可以通过引力波进行探测，未来可以通过LISA、Cosmic Explorer和DECIGO等观测站进行探测。研究人员的目标是改进他们的模型，以预测这些结的形成和衰变，将它们的特征与观测信号联系起来，并最终了解这些结是否在宇宙的起源中发挥了关键作用。

---

## 55. Xubuntu 网站遭入侵并传播恶意软件

**原文标题**: Xubuntu website hacked and served malware

**原文链接**: [https://old.reddit.com/r/xubuntu/comments/1oa43gt/xubuntuorg_might_be_compromised/](https://old.reddit.com/r/xubuntu/comments/1oa43gt/xubuntuorg_might_be_compromised/)

无法访问该文章链接。

---

## 56. SuperSonic – Web AudioWorklet 中的 SuperCollider 音频引擎

**原文标题**: SuperSonic – SuperCollider's audio engine in a Web AudioWorklet

**原文链接**: [https://www.patreon.com/posts/introducing-in-141953467](https://www.patreon.com/posts/introducing-in-141953467)

无法访问文章链接。

---

## 57. 基于 Rust 的 coreutils 中的日期错误影响 Ubuntu 25.10 自动更新

**原文标题**: Date bug in Rust-based coreutils affects Ubuntu 25.10 automatic updates

**原文链接**: [https://lwn.net/Articles/1043103/](https://lwn.net/Articles/1043103/)

LWN.net文章报道，uutils coreutils包中基于Rust的`date`命令存在一个bug，导致Ubuntu 25.10系统无法自动更新。受影响的系统包括云部署、容器镜像以及桌面和服务器安装。该bug存在于rust-coreutils软件包0.2.2-0ubuntu2及更早版本中，已在0.2.2-0ubuntu2.1或更高版本中修复。使用`apt`手动更新不受影响。

Ubuntu 25.10包含基于Rust的uutils和sudo-rs，这是将发行版“氧化”并评估Rust实用程序长期适用性的项目的一部分。文章包含来自订阅者的各种评论，他们争论用Rust重写已建立的C实用程序的优点、uutils使用的MIT许可证相对于GPL的潜在好处和缺点，以及在稳定的操作系统中替换核心实用程序的总体策略。一些评论员认为这是一个类似于KDE 4.0发布的过早举动，而另一些人则认为这是提高安全性和实现代码库现代化的必要步骤。人们对uutils中潜在的数据损坏和接口更改表示担忧，强调需要对该项目进行谨慎管理。

---

## 58. 语言和思维并非同一事物：来自神经影像学的证据

**原文标题**: Language and thought are not the same thing: evidence from neuroimaging

**原文链接**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC4874898/](https://pmc.ncbi.nlm.nih.gov/articles/PMC4874898/)

Evelina Fedorenko和Rosemary Varley的《语言和思维并非同一事物：来自神经影像学和神经病患的证据》一文认为，复杂的人类思维与语言不同，并且可以在没有语言的情况下存在。他们利用功能磁共振成像研究和患有完全性失语症的个体的证据来支持他们的论点。

作者提出，虽然在缺乏语言的非人类动物身上也能观察到复杂的认知和行为，但诸如算术、音乐和心智理论等复杂的认知能力是否依赖于语言仍然是一个问题。他们着重研究语言与五种认知能力之间的关系：算术运算、执行功能、心智理论、音乐处理和空间导航。

对健康成年人的功能磁共振成像研究表明，语言处理会激活特定的脑区（左侧额叶和颞叶皮层的外侧面），而在算术、工作记忆、抑制或音乐等非语言任务中，这些脑区不会被激活。此外，患有完全性失语症、语言能力严重缺陷的个体仍然可以执行非语言任务。

作者得出结论，高级语言处理区域与支持复杂思维的区域是不同的。对语言区域的损伤会损害语言能力，但不一定会影响其他认知功能。

---

## 59. 大鹏相机

**原文标题**: Roc Camera

**原文链接**: [https://roc.camera/](https://roc.camera/)

Roc Camera 旨在解决人工智能生成图像时代下的真实性问题。该产品强调，传统照片作为真实瞬间的代表，拥有独特的魔力，而这种魔力已被易于分享和创建人工智能图像所削弱，导致现实模糊和迷失方向。

Roc Camera 旨在通过利用经过验证的传感器数据、零知识证明和防篡改环境来重新捕捉可验证的真实照片。 这种创新方法确保每张拍摄的照片都对相机来说是独一无二的真实，并且可以被证明。

该相机配备 4 英寸 IPS LCD 触摸屏、带广角镜头的 16MP 索尼 IMX519 CMOS 传感器、树莓派 4、4GB RAM、4000mAh LiPo 电池和不间断电源。

该相机采用三个步骤进行操作：捕获、证明和验证。它捕获一张独特的照片，创建传感器数据和元数据的零知识证明，并允许通过 Roc Photo SDK 验证照片的真实性。

Roc Camera 目前接受第二批订单，预计在 2-3 周内发货，售价为 399 美元。

---

## 60. 文件系统设计哲学

**原文标题**: File system design philosophy

**原文链接**: [https://deyaa1251.github.io/deyaa1251/posts/b_tree/](https://deyaa1251.github.io/deyaa1251/posts/b_tree/)

本文探讨了二叉搜索树(BST)在文件系统和数据库中由于磁盘I/O成本而存在的实际局限性。虽然理论上BST提供O(log n)的搜索复杂度，但当考虑磁盘访问时间时，这一优势会减弱。BST中每次节点访问都相当于一次磁盘读取，这比RAM访问慢得多，因此对于存储在磁盘上的大型数据集来说效率低下。

本文提倡使用B树作为更优的选择。B树是“更胖”的树，每个节点可以存储多个键和子指针。这种设计允许单次磁盘读取访问更大的数据量，从而减少搜索所需的磁盘读取总数。B树只需3次磁盘读取即可搜索数百万个文件，而BST则需要20次。

作者提供了经验证据，包括基准测试结果，证明了BST和B树在各种场景下的性能差异，尤其是在模拟磁盘I/O的情况下。 提供了代码、场景和可视化。

此外，本文还强调了B树及其变体在实际系统中的广泛应用，如文件系统(ext4, NTFS)、数据库(MySQL, MongoDB)和数据存储(Git, AWS S3)。它解释了理解像B树这样的底层数据结构如何帮助开发人员优化数据库查询并避免性能陷阱，例如在SQL查询中使用前导通配符，这会阻止索引的使用。 关键的要点是，在系统工程中，最小化像磁盘读取这样昂贵的操作通常比理论上的算法效率更重要。

---

## 61. 朝日 Linux 仍在开发 Apple M3 支持，M1n1 引导加载器转向 Rust

**原文标题**: Asahi Linux Still Working on Apple M3 Support, M1n1 Bootloader Going Rust

**原文链接**: [https://www.phoronix.com/news/Asahi-Linux-M3-m1n1-Update](https://www.phoronix.com/news/Asahi-Linux-M3-m1n1-Update)

本文报道了为苹果芯片设备开发的 Asahi Linux 的最新进展。虽然 Linux 6.17 和 6.18 的内核补丁（包括 Apple M2 Pro/Max/Ultra 芯片的设备树）的提交工作仍在进行中，但开发人员仍在努力为 Apple M3 提供支持。目前，M3 的支持非常基础，仅能启动到闪烁的光标。

主要进展还包括 m1n1 引导加载程序过渡到 Rust 编程语言，以提高可维护性、安全性和正确性。

此外，Asahi Linux 团队在苹果芯片上的游戏兼容性方面取得了进展，Wine 现在可以在 muvm 之外运行，并且他们的图形驱动程序支持也在不断改进。

虽然提交工作的重点主要集中在 M1 和 M2 芯片上，但该团队认识到需要解决较新的 M3（以及潜在的 M4 和 M5）问题，并正在积极努力改进 M3 的支持。完整的进展报告可在 AsahiLinux.org 上找到。

---

## 62. Clojure拉链 (2021)

**原文标题**: Clojure Zippers (2021)

**原文链接**: [https://grishaev.me/en/clojure-zippers/](https://grishaev.me/en/clojure-zippers/)

本文介绍 Clojure Zipper，一种用于遍历、修改和搜索复杂数据结构（包括向量、映射、XML 和树）的强大工具。Zipper 是 Clojure 核心库的一部分，并利用了不可变集合。

核心概念涉及“位置”，它结合了数据和指向数据结构中特定位置的指针。`zip/down`、`zip/up`、`zip/left` 和 `zip/right` 等导航函数创建新的位置，而不修改原始数据。

要创建 Zipper，您需要提供数据和函数，以确定元素是否为分支 (`branch?`) 以及如何检索其子元素 (`children`)。 像 `zip/vector-zip` 这样的预定义 Zipper 简化了常见数据结构的创建。

虽然手动导航是可能的，但对于复杂、未知的数据结构来说通常是不切实际的。`zip/next` 函数提供自动遍历，仅访问每个节点一次。`iterate` 函数允许生成位置的惰性无限序列，但需要使用 `zip/end?` 检查完成标志以避免无限循环。当您需要搜索或修改结构未预先知道的数据时，Zipper 非常出色。

---

## 63. 你计算机教育缺失的一学期 (2020)

**原文标题**: The Missing Semester of Your CS Education (2020)

**原文链接**: [https://missing.csail.mit.edu/](https://missing.csail.mit.edu/)

本文档介绍了“计算机科学教育中缺失的一学期”课程，该课程旨在弥补传统计算机科学课程中的一个关键缺口：对基本工具的熟练掌握。虽然计算机科学课程侧重于高级主题，但它们往往忽略了实用技能，例如命令行精通、文本编辑器熟练使用（特别是Vim）、版本控制（Git）以及调试/分析技术。

本课程旨在使学生能够有效地利用这些工具，从而节省时间并更有效地解决复杂问题。课程内容包括 shell 导航和脚本编写、数据处理、命令行环境配置、Git 使用、调试、元编程、安全性以及各种有用的技巧。

该课程由 Anish、Jon 和 Jose 在 MIT 教授，并且录像可在 YouTube 上观看。这些材料也在 MIT 之外分享，以使更广泛的受众受益，并提供指向 Hacker News 和 Reddit 等平台上的讨论链接。课程笔记已被翻译成多种语言，反映了全球对该主题的兴趣。该课程感谢 MIT 的许多个人和部门在录制和后勤方面的帮助。这些材料已根据 CC BY-NC-SA 许可发布，鼓励贡献和翻译。

---

## 64. Deepagent：强大的桌面AI助手

**原文标题**: Deepagent: A powerful desktop AI assistant

**原文链接**: [https://deepagent.abacus.ai](https://deepagent.abacus.ai)

DeepAgent是由Abacus.AI开发的强大AI助手，旨在处理构建应用程序、撰写报告、制作演示文稿以及连接各种系统等复杂任务。它以每月每用户10美元的价格提供，并且包含在ChatLLM Teams中。

DeepAgent通过各种示例进行展示，证明其在以下领域的强大能力：

*   **应用开发：** 构建具有Stripe集成的网站、AI驱动的简历分析器、HR SaaS应用程序和互动游戏。
*   **内容创作：** 生成研究报告、PowerPoint演示文稿和AI生成的视频，包括具有逼真唇形同步的播客。
*   **聊天机器人：** 从PDF库创建RAG驱动的聊天机器人、模仿历史人物或影响者的基于角色的聊天机器人，以及用于餐厅推荐或正念指导等任务的专业聊天机器人。
*   **智能体任务：** 自动化诸如寻找廉价机票、自动化支出报告、进行市场调查和管理社交媒体等任务。
*   **数据分析：** 构建具有预测分析的基于Excel的仪表板、揭示客户流失模式以及分析财务报告。
*   **代码开发：** 在代码库中开发端到端的功能并提出PR，以及审查PR和添加评论。

订阅者还可以获得ChatLLM的额外访问权限，该平台拥有LLM、网络搜索和图像生成等各种AI工具。每周一次的竞赛为DeepAgent订阅者提供赢取2500美元奖金的机会。

---

## 65. Show HN: MacOS实时屏保 – 一款播放实时视频流的屏保

**原文标题**: Show HN: MacOS Live Screensaver – A screensaver that plays live video streams

**原文链接**: [https://github.com/hauxir/macos-live-screensaver](https://github.com/hauxir/macos-live-screensaver)

这个“Show HN”帖子介绍 MacOS Live Screensaver，这是一个macOS屏幕保护程序应用，可以播放实时视频流。它支持 YouTube 直播流（需要 `yt-dlp`）和直接 HLS 流。作者强调这是一个“凭感觉编写”的项目，测试仅限于 M2 MacBook 上的 macOS Tahoe。

安装包括使用 Homebrew 或 pip 安装 `yt-dlp`（可选，但推荐用于 YouTube 支持），然后使用 `make install` 构建和安装屏幕保护程序，或按照文档中提供的步骤手动安装。还提供了其他 `make` 命令用于清理、卸载和启动屏幕保护程序。

用户可以通过系统偏好设置 -> 屏幕保护程序配置屏幕保护程序，选择“Live Screensaver”并点击“选项”来输入 YouTube 直播流 URL 或 HLS 流 URL。作者指出，由于 macOS 漏洞，“选项”按钮可能无响应，并鼓励提交 pull request 来修复此问题。

其中包括故障排除提示，解决了常见问题，例如 YouTube 视频无法播放（与 `yt-dlp` 或使用非直播视频有关）和黑屏（建议耐心等待或尝试其他 URL）。

---

## 66. The Great Butterfly Heist

**原文标题**: The Great Butterfly Heist

**原文链接**: [https://www.theguardian.com/global/2025/oct/04/great-butterfly-heist-how-collector-stole-thousands-butterflies-from-australian-museums](https://www.theguardian.com/global/2025/oct/04/great-butterfly-heist-how-collector-stole-thousands-butterflies-from-australian-museums)

Walter Marsh's article, "The Great Butterfly Heist," unravels the story of Colin Wyatt, a charismatic English adventurer and butterfly collector who infiltrated the Australian entomological community in the 1930s and 40s. Wyatt, leveraging his charm and apparent expertise, gained access to museum collections and proceeded to steal thousands of rare butterfly specimens from major Australian museums, including those in Sydney, Melbourne, and Adelaide.

The theft was discovered in 1947, leading to an international investigation that ultimately found a massive collection of butterflies in Wyatt's possession at his mother's home in England. He confessed, blaming marital troubles for his actions. The recovered specimens were returned to Australia, but the impact of Wyatt's actions reverberated for decades.

The article highlights the case of the flame hairstreak butterfly, whose holotype (the first specimen used to define the species) was replaced with a painted fake by Wyatt. This deception went unnoticed for over 70 years. The article also examines the broader implications of the theft, raising questions about museum security, the trustworthiness of amateur collectors, and the ethical dimensions of collecting practices during the age of empire. The article shows that museums, like other organizations during the colonial era, had participated in controversial specimen collecting. Finally, the author shows that scientists are still grappling with the repercussions of Wyatt's crimes, as stolen specimens continue to surface and be repatriated.


---

## 67. New OSM file format: 30% smaller than PBF, 5x faster to import

**原文标题**: New OSM file format: 30% smaller than PBF, 5x faster to import

**原文链接**: [https://community.openstreetmap.org/t/new-osm-file-format-30-smaller-than-pbf-5x-faster-to-import/137151](https://community.openstreetmap.org/t/new-osm-file-format-30-smaller-than-pbf-5x-faster-to-import/137151)

生成摘要时出错

---

## 68. 为什么你的Social.org文件可以包含没有问题的行？

**原文标题**: Why Your Social.org Files Can Have Lines Without Issues?

**原文链接**: [https://en.andros.dev/blog/4e12225f/why-your-socialorg-files-can-have-millions-of-lines-without-any-performance-issues/](https://en.andros.dev/blog/4e12225f/why-your-socialorg-files-can-have-millions-of-lines-without-any-performance-issues/)

生成摘要时出错

---

## 69. Traffic Light Protocol

**原文标题**: Traffic Light Protocol

**原文链接**: [https://www.first.org/tlp/](https://www.first.org/tlp/)

生成摘要时出错

---

## 70. /dev/null is an ACID compliant database

**原文标题**: /dev/null is an ACID compliant database

**原文链接**: [https://jyu.dev/blog/why-dev-null-is-an-acid-compliant-database/](https://jyu.dev/blog/why-dev-null-is-an-acid-compliant-database/)

生成摘要时出错

---

## 71. JupyterGIS breaks through to the next level

**原文标题**: JupyterGIS breaks through to the next level

**原文链接**: [https://eo4society.esa.int/2025/10/16/jupytergis-breaks-through-to-the-next-level/](https://eo4society.esa.int/2025/10/16/jupytergis-breaks-through-to-the-next-level/)

生成摘要时出错

---

## 72. When is it better to think without words?

**原文标题**: When is it better to think without words?

**原文链接**: [https://www.henrikkarlsson.xyz/p/wordless-thought](https://www.henrikkarlsson.xyz/p/wordless-thought)

生成摘要时出错

---

## 73. The 996 Schedule Just Means You Have No Leverage

**原文标题**: The 996 Schedule Just Means You Have No Leverage

**原文链接**: [https://www.joanwestenberg.com/p/996-just-means-you-have-no-leverage](https://www.joanwestenberg.com/p/996-just-means-you-have-no-leverage)

生成摘要时出错

---

## 74. Counter-Strike's player economy is in a freefall

**原文标题**: Counter-Strike's player economy is in a freefall

**原文链接**: [https://www.polygon.com/counter-strike-cs-player-economy-multi-billion-dollar-freefall/](https://www.polygon.com/counter-strike-cs-player-economy-multi-billion-dollar-freefall/)

生成摘要时出错

---

## 75. US probes Waymo robotaxis over school bus safety

**原文标题**: US probes Waymo robotaxis over school bus safety

**原文链接**: [https://www.yahoo.com/news/articles/us-investigates-waymo-robotaxis-over-102015308.html](https://www.yahoo.com/news/articles/us-investigates-waymo-robotaxis-over-102015308.html)

生成摘要时出错

---

## 76. LightlyStudio – an open-source multimodal data curation and labeling tool

**原文标题**: LightlyStudio – an open-source multimodal data curation and labeling tool

**原文链接**: [https://github.com/lightly-ai/lightly-studio](https://github.com/lightly-ai/lightly-studio)

生成摘要时出错

---

## 77. A sharded DuckDB on 63 nodes runs 1T row aggregation challenge in 5 sec

**原文标题**: A sharded DuckDB on 63 nodes runs 1T row aggregation challenge in 5 sec

**原文链接**: [https://gizmodata.com/blog/gizmoedge-one-trillion-row-challenge](https://gizmodata.com/blog/gizmoedge-one-trillion-row-challenge)

生成摘要时出错

---

## 78. TextEdit and the relief of simple software

**原文标题**: TextEdit and the relief of simple software

**原文链接**: [https://www.newyorker.com/culture/infinite-scroll/textedit-and-the-relief-of-simple-software](https://www.newyorker.com/culture/infinite-scroll/textedit-and-the-relief-of-simple-software)

生成摘要时出错

---

## 79. Google flags Immich sites as dangerous

**原文标题**: Google flags Immich sites as dangerous

**原文链接**: [https://immich.app/blog/google-flags-immich-as-dangerous](https://immich.app/blog/google-flags-immich-as-dangerous)

生成摘要时出错

---

## 80. SierraDB: A distributed event store built in Rust

**原文标题**: SierraDB: A distributed event store built in Rust

**原文链接**: [https://tqwewe.com/blog/building-sierradb/](https://tqwewe.com/blog/building-sierradb/)

生成摘要时出错

---

## 81. How memory maps (mmap) deliver faster file access in Go

**原文标题**: How memory maps (mmap) deliver faster file access in Go

**原文链接**: [https://info.varnish-software.com/blog/how-memory-maps-mmap-deliver-25x-faster-file-access-in-go](https://info.varnish-software.com/blog/how-memory-maps-mmap-deliver-25x-faster-file-access-in-go)

生成摘要时出错

---

## 82. The game theory of how algorithms can drive up prices

**原文标题**: The game theory of how algorithms can drive up prices

**原文链接**: [https://www.quantamagazine.org/the-game-theory-of-how-algorithms-can-drive-up-prices-20251022/](https://www.quantamagazine.org/the-game-theory-of-how-algorithms-can-drive-up-prices-20251022/)

生成摘要时出错

---

## 83. That Time Ken Thompson Wrote a Backdoor into the C Compiler

**原文标题**: That Time Ken Thompson Wrote a Backdoor into the C Compiler

**原文链接**: [https://micahkepe.com/blog/thompson-trojan-horse/](https://micahkepe.com/blog/thompson-trojan-horse/)

生成摘要时出错

---

## 84. Claude Memory

**原文标题**: Claude Memory

**原文链接**: [https://www.anthropic.com/news/memory](https://www.anthropic.com/news/memory)

生成摘要时出错

---

## 85. Trump pardons convicted Binance founder

**原文标题**: Trump pardons convicted Binance founder

**原文链接**: [https://www.wsj.com/finance/currencies/trump-pardons-convicted-binance-founder-7509bd63](https://www.wsj.com/finance/currencies/trump-pardons-convicted-binance-founder-7509bd63)

生成摘要时出错

---

## 86. Automating Algorithm Discovery: A Case Study in MoE Load Balancing

**原文标题**: Automating Algorithm Discovery: A Case Study in MoE Load Balancing

**原文链接**: [https://adrs-ucb.notion.site/moe-load-balancing](https://adrs-ucb.notion.site/moe-load-balancing)

生成摘要时出错

---

## 87. Carmack on Operating Systems (1997)

**原文标题**: Carmack on Operating Systems (1997)

**原文链接**: [https://rmitz.org/carmack.on.operating.systems.html](https://rmitz.org/carmack.on.operating.systems.html)

生成摘要时出错

---

## 88. Antislop: A framework for eliminating repetitive patterns in language models

**原文标题**: Antislop: A framework for eliminating repetitive patterns in language models

**原文链接**: [https://arxiv.org/abs/2510.15061](https://arxiv.org/abs/2510.15061)

生成摘要时出错

---

## 89. WebDAV Isn't Dead Yet

**原文标题**: WebDAV Isn't Dead Yet

**原文链接**: [https://blog.feld.me/posts/2025/09/webdav-isnt-dead-yet/](https://blog.feld.me/posts/2025/09/webdav-isnt-dead-yet/)

生成摘要时出错

---

## 90. Introduction to the concept of likelihood and its applications (2018)

**原文标题**: Introduction to the concept of likelihood and its applications (2018)

**原文链接**: [https://journals.sagepub.com/doi/10.1177/2515245917744314](https://journals.sagepub.com/doi/10.1177/2515245917744314)

生成摘要时出错

---

## 91. Rust Contagious Borrow Issue

**原文标题**: Rust Contagious Borrow Issue

**原文链接**: [https://qouteall.fun/qouteall-blog/2025/How%20to%20Avoid%20Fighting%20Rust%20Borrow%20Checker#contagious-borrow-issue](https://qouteall.fun/qouteall-blog/2025/How%20to%20Avoid%20Fighting%20Rust%20Borrow%20Checker#contagious-borrow-issue)

生成摘要时出错

---

## 92. Linux disk I/O diagram (2024)

**原文标题**: Linux disk I/O diagram (2024)

**原文链接**: [https://zenodo.org/records/15234151](https://zenodo.org/records/15234151)

生成摘要时出错

---

## 93. VST3 audio plugin format is now MIT

**原文标题**: VST3 audio plugin format is now MIT

**原文链接**: [https://forums.steinberg.net/t/vst-3-8-0-sdk-released/1011988](https://forums.steinberg.net/t/vst-3-8-0-sdk-released/1011988)

生成摘要时出错

---

## 94. Technical experts have zero customers

**原文标题**: Technical experts have zero customers

**原文链接**: [https://www.ivan.codes/thoughts/technical-experts-have-zero-customers](https://www.ivan.codes/thoughts/technical-experts-have-zero-customers)

生成摘要时出错

---

## 95. Poker fraud used X-ray tables, high-tech glasses and NBA players

**原文标题**: Poker fraud used X-ray tables, high-tech glasses and NBA players

**原文链接**: [https://www.bbc.com/news/articles/cz6nd9wnzn6o](https://www.bbc.com/news/articles/cz6nd9wnzn6o)

生成摘要时出错

---

## 96. Fast-DLLM: Training-Free Acceleration of Diffusion LLM

**原文标题**: Fast-DLLM: Training-Free Acceleration of Diffusion LLM

**原文链接**: [https://arxiv.org/abs/2505.22618](https://arxiv.org/abs/2505.22618)

生成摘要时出错

---

## 97. Radios, how do they work? (2024)

**原文标题**: Radios, how do they work? (2024)

**原文链接**: [https://lcamtuf.substack.com/p/radios-how-do-they-work](https://lcamtuf.substack.com/p/radios-how-do-they-work)

生成摘要时出错

---

## 98. React Flow, open source libraries for node-based UIs with React or Svelte

**原文标题**: React Flow, open source libraries for node-based UIs with React or Svelte

**原文链接**: [https://github.com/xyflow/xyflow](https://github.com/xyflow/xyflow)

生成摘要时出错

---

## 99. FocusTube: A Chrome extension that hides YouTube Shorts

**原文标题**: FocusTube: A Chrome extension that hides YouTube Shorts

**原文链接**: [https://github.com/CaptainYouz/FocusTube](https://github.com/CaptainYouz/FocusTube)

生成摘要时出错

---

## 100. Scripts I wrote that I use all the time

**原文标题**: Scripts I wrote that I use all the time

**原文链接**: [https://evanhahn.com/scripts-i-wrote-that-i-use-all-the-time/](https://evanhahn.com/scripts-i-wrote-that-i-use-all-the-time/)

生成摘要时出错

---

