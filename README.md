# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-29.md)

*最后自动更新时间: 2025-10-29 17:52:02*
## 1. 保持安卓开放

**原文标题**: Keep Android Open

**原文链接**: [http://keepandroidopen.org/](http://keepandroidopen.org/)

2025年8月，谷歌宣布一项将于明年开始实施的新政策，该政策将要求所有安卓开发者向谷歌注册才能为该平台开发应用。 注册过程将包括支付费用、同意谷歌的条款和条件、提供政府身份证明、上传应用签名密钥的证明以及列出所有应用标识符。

这项政策引发了相当大的反对，人们对其对独立开发者、F-Droid等开源应用商店以及安卓生态系统的整体自由的影响表示担忧。 批评者认为，新的要求将设置准入壁垒，扼杀创新，并使谷歌过度控制应用分发。

“保持安卓开放”倡议应运而生，旨在反对这项政策的实施。 目前推广的行动包括签署致谷歌的公开信、联系各国的相关监管机构（例如，欧盟竞争政策、美国司法部反垄断部门、英国竞争与市场管理局）、通过谷歌的安卓开发者验证调查提供反馈，以及在社交媒体上提高人们的意识。 该倡议还鼓励合作，以收集和传播更多关于该政策及其潜在后果的信息。 提供的信息包括一份全面的资源清单，其中包括文章、视频和论坛讨论，详细说明了新规则的负面影响和潜在的监管挑战。

---

## 2. 光标作曲家：用强化学习构建快速前沿模型

**原文标题**: Cursor Composer: Building a fast frontier model with RL

**原文链接**: [https://cursor.com/blog/composer](https://cursor.com/blog/composer)

Cursor开发了“Composer”，一款专为软件工程的速度和智能而设计的新型智能代理模型。在内部基准测试中，它在编码任务上的表现优于同类模型，生成速度快四倍。这归功于Composer在大型代码库上进行训练，以处理实际的软件工程任务，并利用生产级别的搜索和编辑工具。

Composer是一个混合专家（MoE）语言模型，通过强化学习（RL）在不同的开发环境中进行优化，专用于软件工程。它通过使用文件编辑、终端命令和代码库语义搜索等工具生成代码修改、计划或信息来高效地解决问题。

Cursor开发了一个基于其工程师的实际代理请求的真实基准测试Cursor Bench，以衡量进展。该基准测试评估了正确性以及对现有代码抽象和软件工程实践的遵守情况。强化学习（RL）专门用于优化模型，以提高软件工程效率。

该模型经过训练，可以进行高效的工具选择并最大化并行处理。它还学会避免不必要的响应和没有根据的陈述。此外，它还在强化学习（RL）训练期间自发地获得诸如复杂搜索、修复linter错误和编写单元测试等能力。

Cursor使用PyTorch和Ray构建了一个自定义的训练基础设施，将MXFP8 MoE内核与专家和数据并行性相结合，以在数千个NVIDIA GPU上高效地训练模型，且通信开销低。这允许更快的推理，无需训练后量化。训练环境利用Cursor现有的Background Agents基础设施，在云中运行数十万个隔离的沙盒编码环境。

目标是创建一个Cursor自己的工程师可以每天依赖的智能代理。在Cursor内部的早期采用已被证明是有价值的，他们希望将该价值扩展到他们的用户。

---

## 3. Tailscale 对等节点中继

**原文标题**: Tailscale Peer Relays

**原文链接**: [https://tailscale.com/blog/peer-relays-beta](https://tailscale.com/blog/peer-relays-beta)

Tailscale 发布 Tailscale Peer Relays 公开测试版，这是客户管理的替代方案，用于替代 Tailscale 的 DERP 服务器，以便在 tailnet 内中继网络流量。与优先考虑可靠性和 NAT 穿透的 DERP 不同，Peer Relays 专为高性能连接而设计，在速度和效率上可与直接连接相媲美。

Peer Relays 解决了 DERP 在吞吐量至关重要的环境中的局限性，例如位于严格防火墙或 NAT 网关之后的云基础设施。它们使客户能够部署靠近资源的转发节点，并使用 UDP 来降低延迟。它们还直接集成到 Tailscale 客户端中，从而简化了部署。

管理员可以使用简单的 CLI 命令启用 Peer Relays，配置一个可供连接节点访问的 UDP 端口。Tailscale 仍然优先考虑直接连接，然后回退到 Peer Relays，再回退到 DERP。这实现了一种灵活的网络拓扑，同时通过 WireGuard 保持端到端加密。

其优势包括通过云 NAT 的高吞吐量连接、通过网络防火墙的可预测访问路径、减少对 DERP 的依赖以及更轻松地访问锁定客户网络。Tailscale 的 Peer Relays 旨在为需要在各种网络环境中扩展 Tailscale 使用量的客户提供最佳性能和灵活性。Tailscale 在所有计划中免费提供两个 peer relays。

---

## 4. 我做了一个十分钱的MCU演讲

**原文标题**: I made a 10¢ MCU Talk

**原文链接**: [https://www.atomic14.com/2025/10/29/CH32V003-talking](https://www.atomic14.com/2025/10/29/CH32V003-talking)

作者成功使用16KB闪存使0.1美元的单片机(MCU)，特别是CH32V003，“说话”的尝试。他主要通过两种方法实现了这一点：压缩音频播放和LPC语音合成。

首先，作者探索了使用MCU的PWM输出作为简易DAC播放一段6秒的音频片段。由于内存限制，必须进行激进的音频压缩。作者最终选择了2-bit ADPCM，实现了4:1的压缩比，并将音频片段缩小到12KB以下，使其能够装入闪存。为此，作者还创建了一个自定义工具，用于将WAV文件转换为这种格式。

其次，对于更长的短语和语音，作者基于德州仪器TMS5220/5100架构（想想Speak & Spell），使用Talkie库实现了LPC（线性预测编码）语音合成。LPC通过对人声建模，可以紧凑地存储语音数据。作者还创建了一个简化的在线工具，用于将作者本人的录音转换为LPC数据进行播放。

作者强调了即使是这些超低成本MCU的强大功能，证明了在受到严重限制的内存环境中也可以实现诸如压缩音频和语音合成等复杂的音频功能。该项目的代码已在GitHub上提供，并且有一个视频演示展示了结果。

---

## 5. 刷牙前用牙线

**原文标题**: Floss Before Brushing

**原文链接**: [https://alearningaday.blog/2025/10/29/floss-before-brushing/](https://alearningaday.blog/2025/10/29/floss-before-brushing/)

本文挑战了一种普遍的观念，即刷牙应该先于用牙线。作者叙述了与一位牙科保健师的对话，后者建议将顺序改为先用牙线，然后刷牙。起初作者对此持怀疑态度，但后来逐渐理解了这一建议背后的原理。

先用牙线可以松动并清除牙齿之间的食物残渣和牙菌斑，这些区域是牙刷无法有效触及的。这种预防性的清洁使得牙膏中的氟化物在刷牙时能够接触并保护更多的牙齿表面。作者发现这个逻辑令人信服，并指出了支持性的研究。

本文强调了三个关键要点：首先，习惯总是可以改进的，即使是长期存在的习惯。其次，使用牙线的行为本身至关重要，无论顺序如何，因此养成定期使用牙线的习惯至关重要。最后，如果使用牙线已经成为一种习惯，那么改为先用牙线再刷牙可以为口腔卫生带来最佳益处。

---

## 6. 品牌广告有效吗？Upwave (YC S12) 正在招聘工程师来解答这个问题。

**原文标题**: Does brand advertising work? Upwave (YC S12) is hiring engineers to answer that

**原文链接**: [https://www.upwave.com/job/8228849002/](https://www.upwave.com/job/8228849002/)

Upwave诚聘高级软件工程师，构建并扩展其人工智能驱动平台。Upwave是一家品牌效果衡量平台，获得Y Combinator和其他领先投资者的支持。该平台帮助领先广告商衡量和优化其跨渠道的品牌活动，处理数十亿次的广告展示，以提供洞察力，为数百万美元的营销决策提供信息。

高级软件工程师将是一位具备后端经验的全栈问题解决者，负责开发API、数据管道和驱动平台的系统。主要职责包括集成LLM以实现人工智能驱动的客户体验，设计可扩展的后端系统，构建和运营大规模数据管道，并提高系统的可靠性和性能。

理想的候选人应具有5年以上经验，熟悉全栈技术，并了解现代UI框架、API架构、数据库和云平台。拥有现代人工智能驱动的开发工具和结构化软件开发实践经验者优先考虑。具备Java/Kotlin/Groovy、MySQL/DynamoDB/Presto、AWS/Kubernetes/Terraform以及广告技术/营销技术经验者优先。

Upwave提供远程优先、工程师优先的环境，并采用现代技术栈。公司强调自主性、所有权和协作文化。该职位提供15万美元至17.5万美元的基本工资范围+奖金+股权+福利。

---

## 7. 树莓派之外：其他SoC厂商在做什么 *概要*

**原文标题**: Beyond RaspberryPi: What are all the other SoC vendors up to *summarised*

**原文链接**: [https://sbcwiki.com/news/articles/state-of-embedded-q4-25/](https://sbcwiki.com/news/articles/state-of-embedded-q4-25/)

嵌入式状态：2025年第四季度概览文章摘要：

基于ARM的SBC市场持续繁荣，对x86平台构成强劲竞争。主要进展包括英伟达发布了由GB10 Grace Blackwell Superchip驱动的DGX Spark，但停止了对Jetson的支持。高通凭借Snapdragon Oryon X2的发布取得了显著进展，频率达到5GHz。瑞莎推出了具有主线支持且价格合理的Dragon Q6A SBC，高通收购了Arduino，将SBC引入了Arduino生态系统，推出了Arduino UNO Q。

瑞芯微公布了RK3688和RK3668 SoC的路线图，其特点是下一代Arm Mali Magni GPU和令人印象深刻的性能规格。内核更新持续进行，同时正在为Mali G610积极进行PanVK Vulkan开发。联发科专注于其Genio和Kompanio系列的软件支持，Libre Computer和瑞莎正在开发新的板卡。Dimensity 9500旗舰移动SoC也亮相，获得了出色的Geekbench结果。

CIX的产品可用性有所提高，Radxa Orion-O6N和OrangePi 6 Plus相继上市，同时主线设备树支持方面也取得了进展。树莓派推出了500+桌面电脑。德州仪器继续专注于汽车应用，而Imagination Technologies则进行了驱动程序更新。以U-Boot闻名的DENX正在逐步结束运营。新思科技将与Toradex合作发布一款新的SBC，采用Astra SL1680 SoC。AI NPU正变得越来越经济实惠和容易获得。

---

## 8. 柯林斯宇航：向驾驶舱发送文本消息，测试：测试

**原文标题**: Collins Aerospace: Sending text messages to the cockpit with test:test

**原文链接**: [https://www.ccc.de/en/disclosure/collins-aerospace-mit-test-test-textnachrichten-bis-ins-cockpit-senden](https://www.ccc.de/en/disclosure/collins-aerospace-mit-test-test-textnachrichten-bis-ins-cockpit-senden)

柯林斯宇航ARINC OpCenter消息浏览器发现安全漏洞。该系统用于向飞机驾驶舱发送文本消息。研究人员能够使用容易猜测的凭据“test:test”登录，并获得美国海军舰队后勤支援机翼的访问权限。此访问权限允许他们查看已发送的消息，并且关键的是，能够向驾驶舱发送新的文本消息。出于道德原因，研究人员没有发送任何消息。

该漏洞已报告给RTX公司（柯林斯宇航的母公司），但据报道未收到任何回应。随后，该存在漏洞的帐户被禁用。国防部网络犯罪中心也于2025年9月21日获悉了该漏洞。 这种容易被攻破的登录凭据代表着重大的安全风险，可能会允许未经授权的方发送具有误导性或破坏性的消息给飞机飞行员。

---

## 9. 眼部义眼首次用于恢复黄斑变性导致的视力丧失

**原文标题**: Eye prosthesis is the first to restore sight lost to macular degeneration

**原文链接**: [https://med.stanford.edu/news/all-news/2025/10/eye-prosthesis.html](https://med.stanford.edu/news/all-news/2025/10/eye-prosthesis.html)

新型眼部假体PRIMA有望恢复晚期年龄相关性黄斑变性（地图样萎缩）患者的功能性视力，该疾病是导致不可逆失明的主要原因之一。该设备由斯坦福大学医学院开发，由植入眼部的无线芯片和高科技眼镜组成。眼镜捕捉图像并将它们以红外光的形式投射到芯片上，芯片将它们转换为电刺激，从而取代受损感光细胞的功能。

在一项临床试验中，32名参与者中有27名在接受植入后一年内恢复了阅读能力。通过缩放和对比度调整等数字增强功能，一些人达到了相当于20/42的视力敏锐度。与之前仅提供光敏感度的假体设备不同，PRIMA提供形态视觉，使患者能够感知形状和图案。

该设备结合患者剩余的周边视觉和假体的中心视觉。该芯片是光伏的，无线工作并植入在视网膜下。虽然当前版本提供黑白视觉，但未来的软件更新将启用灰度以改善面部识别。研究人员还在开发具有更小像素的更高分辨率芯片，以期达到20/80的视力，并有可能通过电子变焦达到接近20/20的视力。虽然一些参与者经历了副作用，但通常不危及生命且很快消退。

---

## 10. 从 VS Code 到 Helix

**原文标题**: From VS Code to Helix

**原文链接**: [https://ergaster.org/posts/2025/10/29-vscode-to-helix/](https://ergaster.org/posts/2025/10/29-vscode-to-helix/)

本文详细介绍了作者从使用 VS Code 过渡到以 Helix 作为日常主要编辑器的过程。起初，由于 VS Code 的易用性和熟悉程度，以及 Vim 的复杂性，作者对此犹豫不决，但 Helix 的“开箱即用”功能和直观的选择-然后-操作工作流程最终打动了作者。

作者的转变是出于对微软控制权的担忧以及对更平衡的国际化开源工具的渴望。尽管担心学习曲线陡峭，但他们发现 Helix 出乎意料地容易上手，尤其要归功于它的交互式教程。

本文强调了适当文档的重要性，并赞扬了一个第三方资源以用户为中心的编写方式。文章的很大一部分致力于配置 Helix 以支持 Markdown、Astro 和 YAML，包括安装和配置语言服务器（marksman、harper-ls、rumdl、astro-ls、yaml-language-server）和格式化工具（dprint）。作者提供了集成这些工具的具体说明，从而实现诸如代码完成、语法检查和自动格式化等功能。

作者还解决了宽屏上文本对齐的 UI 问题，并提出了一种通过使用自定义键绑定调整装订线宽度来解决此问题的方法。最后，文章总结说，虽然 Helix 比 VS Code 需要更多的初始配置，但高效编辑、更平衡的工具链以及对编辑器功能的更深入了解使其值得。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 2 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 3 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 4 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 5 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 6 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 7 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 8 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 9 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 10 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 11 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 12 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 13 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 14 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 15 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 16 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 17 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 18 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 19 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 20 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 21 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 22 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 23 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 24 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 25 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 26 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 27 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 28 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 29 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 30 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 31 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 32 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 33 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 34 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 35 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 36 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 37 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 38 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 39 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 40 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 41 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 42 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 43 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 44 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 45 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 46 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 47 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 48 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 49 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 50 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 51 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 52 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 53 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 54 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 55 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 56 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 57 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 58 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 59 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 60 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 61 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 62 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 63 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 64 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 65 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 66 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 67 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 68 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 69 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 70 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 71 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 72 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 73 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 74 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 75 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 76 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 77 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 78 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 79 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 80 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 81 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 82 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 83 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 84 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 85 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 86 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 87 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 88 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 89 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 90 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 91 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 92 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 93 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 94 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 95 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 96 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 97 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 98 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 99 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 100 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 101 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 102 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 103 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 104 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 105 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 106 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 107 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 108 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 109 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 110 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 111 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 112 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 113 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 114 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 115 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 116 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 117 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 118 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 119 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 120 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 121 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 122 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 123 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 124 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 125 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 126 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 127 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 128 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 129 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 130 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 131 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 132 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 133 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 134 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 135 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 136 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 137 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 138 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 139 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 140 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 141 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 142 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 143 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 144 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 145 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 146 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 147 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 148 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 149 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 150 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 151 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 152 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 153 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 154 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 155 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 156 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 157 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 158 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 159 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 160 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 161 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 162 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 163 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 164 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 165 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 166 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 167 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 168 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 169 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 170 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 171 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 172 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 173 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 174 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 175 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 176 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 177 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 178 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 179 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 180 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 181 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 182 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 183 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 184 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 185 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 186 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 187 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 188 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 189 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 190 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 191 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 192 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 193 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 194 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 195 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 196 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 197 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 198 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 199 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 200 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 201 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 202 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 203 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 204 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 205 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 206 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 207 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 208 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 209 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 210 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 211 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 212 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 213 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 214 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 215 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 216 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 217 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 218 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 219 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 220 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 221 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 222 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 223 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
