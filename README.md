# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-25.md)

*最后自动更新时间: 2025-10-25 17:45:15*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 2 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 3 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 4 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 5 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 6 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 7 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 8 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 9 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 10 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 11 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 12 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 13 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 14 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 15 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 16 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 17 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 18 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 19 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 20 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 21 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 22 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 23 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 24 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 25 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 26 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 27 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 28 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 29 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 30 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 31 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 32 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 33 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 34 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 35 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 36 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 37 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 38 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 39 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 40 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 41 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 42 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 43 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 44 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 45 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 46 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 47 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 48 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 49 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 50 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 51 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 52 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 53 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 54 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 55 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 56 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 57 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 58 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 59 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 60 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 61 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 62 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 63 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 64 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 65 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 66 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 67 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 68 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 69 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 70 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 71 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 72 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 73 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 74 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 75 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 76 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 77 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 78 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 79 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 80 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 81 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 82 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 83 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 84 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 85 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 86 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 87 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 88 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 89 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 90 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 91 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 92 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 93 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 94 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 95 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 96 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 97 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 98 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 99 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 100 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 101 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 102 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 103 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 104 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 105 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 106 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 107 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 108 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 109 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 110 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 111 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 112 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 113 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 114 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 115 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 116 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 117 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 118 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 119 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 120 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 121 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 122 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 123 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 124 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 125 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 126 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 127 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 128 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 129 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 130 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 131 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 132 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 133 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 134 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 135 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 136 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 137 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 138 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 139 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 140 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 141 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 142 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 143 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 144 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 145 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 146 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 147 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 148 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 149 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 150 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 151 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 152 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 153 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 154 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 155 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 156 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 157 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 158 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 159 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 160 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 161 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 162 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 163 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 164 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 165 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 166 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 167 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 168 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 169 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 170 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 171 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 172 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 173 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 174 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 175 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 176 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 177 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 178 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 179 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 180 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 181 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 182 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 183 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 184 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 185 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 186 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 187 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 188 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 189 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 190 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 191 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 192 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 193 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 194 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 195 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 196 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 197 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 198 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 199 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 200 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 201 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 202 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 203 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 204 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 205 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 206 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 207 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 208 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 209 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 210 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 211 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 212 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 213 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 214 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 215 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 216 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 217 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 218 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 219 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 220 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
