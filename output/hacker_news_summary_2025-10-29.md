# Hacker News 热门文章摘要 (2025-10-29)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 重建1987年的自制游戏系统

**原文标题**: Recreating a Homebrew Game System from 1987

**原文链接**: [https://alex-j-lowry.github.io/z80tvg.html](https://alex-j-lowry.github.io/z80tvg.html)

本文详细介绍了一款名为 Z80 TV Game 的自制 8 位游戏机，该游戏机由一位日本电子爱好者于 1987 年开发。它采用 4MHz Z80 处理器、32KB ROM 卡带（可通过分页切换扩展）、16KB 系统 ROM、8KB 视频 RAM，并以 60Hz 复合视频输出 168x210 像素的黑白图形。音频为 1 位。

该系统利用现成的 IC，控制器输入和音频输出由 Intel 8255 或 Zilog Z80PIO 管理。它支持世嘉 Master System 和 Mega Drive/Genesis 手柄。复合同步信号使用 EPROM 生成。

内存映射包括卡带 ROM、系统 RAM、视频 RAM 和未使用的空间。I/O 映射因使用 8255 或 Z80PIO 而略有不同。

本文提供了用于重建系统的资源，包括原理图、PCB Gerber 文件、KiCad 文件以及控制台和各种卡带设计（32KB、多合一卡带和实验性 256KB）的物料清单。原始原理图、游戏 ROM（由 Isizu 先生和 Inufuto 开发的 26 款游戏）以及卡带尺寸也均可用。

软件开发可以使用 Z80 汇编或 C 语言完成，并获得 Z88DK 开发套件、Inufuto 的 Cate 编译器和 Cross-Lib 框架的支持。还存在模拟器 eZ80TVGAME 和 vdmgr。作者感谢 Isizu 先生、Inufuto、Takeda Toshiya 和 lsluk 的贡献。

---

## 12. 谁还需要Graphviz，自己就能建一个了？

**原文标题**: Who needs Graphviz when you can build it yourself?

**原文链接**: [https://spidermonkey.dev/blog/2025/10/28/iongraph-web.html](https://spidermonkey.dev/blog/2025/10/28/iongraph-web.html)

本文详细介绍了自定义图布局算法“iongraph”的开发过程，该算法旨在可视化SpiderMonkey的Ion优化编译器中JavaScript和WebAssembly代码的编译过程。作者对Graphviz和Mermaid等现有工具的输出不满意，因此寻求一种针对控制流图的特定需求和约束而量身定制的解决方案。

文章强调了Graphviz的问题，包括其不可预测的布局会模糊代码结构，以及微小的更改会导致截然不同的可视化效果的不稳定性。 Iongraph利用控制流图的独特特征（循环少，可归约控制流）来创建更直观和稳定的布局。

该算法基于简化版的Sugiyama布局算法，分为四个主要步骤：

1.  **分层：** 根据基本块的深度将它们组织成水平轨道（层），处理循环结构以在循环内部或外部逻辑地定位块。
2.  **创建虚拟节点：** 在跨越多个层的边上插入虚拟节点，保持一致的定向流（左侧向下，右侧向上），并合并到相同目的地的边。
3.  **拉直边：** 应用迭代过程来对齐节点和虚拟节点，从而提高边的平直度和整体视觉清晰度，包括循环缩进和边“梳理”。
4.  **追踪水平边：** 将水平边排序到平行轨道中，以防止视觉重叠，分配垂直偏移量并记录轨道高度以实现适当的间距。

结果是一种快速、高效且出人意料的有效布局算法，可生成编译器内部进程的稳定且信息丰富的可视化效果，以大约1000行JavaScript实现。文章还包括交互式演示和算法关键部分的伪代码。

---

## 13. 在GitHub Pages上托管SQLite数据库（2021年）

**原文标题**: Hosting SQLite Databases on GitHub Pages (2021)

**原文链接**: [https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/](https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages/)

phiresky (2021) 的这篇文章探讨了在 GitHub Pages 等静态网站上托管 SQLite 数据库的方法，从而规避了小型数据驱动型 Web 工具对后端服务器的需求。它所解决的问题是传统后端方法带来的维护负担和对外部服务的依赖，以及将大型数据集下载到浏览器的低效率。

该解决方案包括将 SQLite 编译为 WebAssembly（使用 sql.js）并创建一个虚拟文件系统 (sql.js-httpvfs)，该文件系统根据需要通过 HTTP Range 请求获取数据库块。 这使得浏览器可以在无需预先下载整个文件的情况下查询完整的 SQLite 数据库，通过使用 SQLite 的页面结构和预取顺序数据来优化带宽和请求开销。

文章通过使用世界发展指标数据集的演示来展示该解决方案，展示了 SQL 查询、JSON 函数和 JavaScript 函数在查询中的集成。它还说明了性能方面的考虑因素，强调了数据库索引对于最大限度地减少 HTTP 请求的重要性。作者演示了使用 SQLite 的 FTS 模块进行全文搜索的功能，并提供了从数据库中绘制数据的交互式示例。 此外，它还展示了如何通过虚拟表将浏览器的 DOM 用作数据库。

2023 年的更新突出了受此工作启发而取得的进展，包括 libgen-ipfs、absurd-sql（使用 IndexedDB 作为持久存储）和 SQLite 的官方 wasm 支持。

---

## 14. AWS两年后迁移到裸金属：解答您关于离开AWS的问题

**原文标题**: AWS to bare metal two years later: Answering your questions about leaving AWS

**原文链接**: [https://oneuptime.com/blog/post/2025-10-29-aws-to-bare-metal-two-years-later/view](https://oneuptime.com/blog/post/2025-10-29-aws-to-bare-metal-two-years-later/view)

2023年，OneUptime详述了他们通过从AWS迁移到裸金属服务器，每年节省23万美元的案例。本篇后续文章解答了常见问题，并分享了两年后的更新。主要亮点包括：

*   **节省增加：** 节省已增长至每年120万美元。
*   **财务依据：** 由于S3、出口流量和其他成本，预留实例/节省计划不足以击败裸金属服务器。与AWS相比，节省了76%。
*   **迁移成本：** 需要一周的工程师时间，但其中大部分是为了进行无论如何都需要的改进。
*   **持续运营：** 由于自动化和依赖主机托管提供商进行物理管理，工程师所需时间极少（每季度24小时）。
*   **弹性：** 他们现在在两个数据中心拥有多个机架，具有隔离的管理路径和任播入口，可在不到一分钟内实现故障转移，这比他们之前的单机架设置有所改进。
*   **硬件生命周期：** 服务器按五年摊销，并计划根据需要在区域分析中级联旧设备。
*   **无需重复发明：** 他们利用与产品自托管承诺一致的开源工具（MicroK8s、Ceph等）。
*   **选择性云使用：** 仍然使用AWS Glacier、CloudFront和突发容量负载测试。
*   **带宽和DDoS：** 承诺跨运营商提供5 Gbps带宽，并使用Cloudflare进行DDoS保护。
*   **可靠性：** 可用性已提高到99.993%。
*   **合规性：** 保持了SOC 2和ISO 27001，调整了物理控制和变更管理流程。
*   **替代云提供商：** 评估了其他提供商，但对于他们的稳态占用空间而言，主机托管更具成本效益。
*   **苦工：** 与AWS相比，苦工程度相似，但专注于不同的任务（打补丁、升级）。

他们建议对稳定、高容量的工作负载使用裸金属服务器，但也承认云在弹性和托管服务方面的优势。未来的计划包括发布一个主机托管资本支出预测工具和一个Talos深度分析。

---

## 15. ChatGPT地图集：反Web浏览器

**原文标题**: ChatGPT's Atlas: The Browser That's Anti-Web

**原文链接**: [https://www.anildash.com//2025/10/22/atlas-anti-web-browser/](https://www.anildash.com//2025/10/22/atlas-anti-web-browser/)

本文批评了 OpenAI 的新型浏览器 Atlas，认为其“反网络”，因为它优先考虑人工智能生成的内容，而不是直接访问网站和传统的网络体验。作者指出了三个主要问题：

1. **AI 替代：** Atlas 用类似于网页的人工智能生成内容来替代实际的网站，可能会误导用户，并将他们与原始来源隔离开来。例如，搜索“泰勒·斯威夫特”会产生人工智能生成的传记信息，但没有链接到她的官方网站。

2. **回归命令行界面：** Atlas 依赖用户猜测正确的命令来输入，而不是利用直观的可点击链接，让人想起过时的命令行界面和文本冒险游戏。这使得导航速度变慢、更容易出错，并且更难发现。

3. **用户作为 AI 代理：** 虽然 Atlas 声称充当用户的“代理”，但它实际上是在利用用户收集 OpenAI 无法访问的数据。 通过启用诸如“记忆”和“询问 ChatGPT”之类的功能，用户不知不觉地让浏览器可以访问机密文档、私人浏览活动和未完成的想法，从而创建全面的监视配置文件。 作者认为，这种数据收集对 OpenAI 的益处大于对用户的益处。文中给出了预订航班的例子，即使 AI 机器人顺利浏览了网站，预订结果仍然出错。

文章最后强调了一种依赖情感依赖的浏览器的潜在危险，主张添加类似于成瘾技术的警告标签，并捍卫网络的开放和可访问性。作者呼吁进行创新，以增强而非取代现有的网络体验。

---

## 16. Show HN: macOS 上的 HUD 风格实时标注和草图应用

**原文标题**: Show HN: HUD-like live annotation and sketching app for macOS

**原文链接**: [https://draw.wrobele.com/](https://draw.wrobele.com/)

Draw Over It 是一款 macOS 应用程序，专为实时屏幕注释和草图绘制而设计。它提供始终置顶的叠加层，浮动于任何应用程序之上，允许用户直接在屏幕上进行绘图，适用于演示、培训或一般专业用途。叠加层可以通过热键 (⌃⌥⌘D) 或菜单栏切换，并且在不需要时可以快速隐藏。

该应用程序具有一个 HUD（抬头显示）工具包，可以通过右键单击（或 ⌃⌥⌘H）访问，提供各种工具，如笔、荧光笔、形状、模糊和会话控制。用户可以轻松自定义笔的粗细、不透明度、填充模式和颜色预设。模糊工具可以通过遮蔽屏幕的其余部分来帮助将注意力集中在关键区域。

Draw Over It 允许用户保存画布状态以供以后使用，将画布导出为透明 PNG，并支持 14 种语言。它还提供撤消/重做功能和橡皮擦（按住 Option 激活）。除非启用“临时画布”选项，否则该应用程序会记住会话之间的注释。

导出文件保存在 `~/Library/Application Support/DrawOverIt/Exports` 中。该应用程序兼容 macOS 13.5 及更高版本，支持 Apple Silicon 和 Intel 处理器。主要优点是使屏幕上的可视化想法能够快速且轻松地访问。

---

## 17. 中风幸存软件工程师的建议

**原文标题**: Tips for stroke-surviving software engineers

**原文链接**: [https://blog.j11y.io/2025-10-29_stroke_tips_for_engineers/](https://blog.j11y.io/2025-10-29_stroke_tips_for_engineers/)

软件工程师詹姆斯·帕多尔西在顶叶出血性中风后幸存，他为其他中风后幸存的工程师，特别是那些患有残留性癫痫的工程师，提供了量身定制的建议。他的主要信息是将健康置于一切之上，提倡自我意识和坚定界限。

主要建议包括：

*   **立即停止：** 任何疲劳、模糊或奇怪的感觉都是休息和补充水分的信号。
*   **控制输入：** 使用耳机、眼罩，并对不必要的需求说“不”，以最大限度地减少干扰。
*   **利用法律保护：** 利用反歧视法和员工援助计划。
*   **单线程工作：** 避免上下文切换，批量处理任务，并使用笔记本和列表外化工作记忆。
*   **将人工智能作为草稿本：** 将状态管理卸载到人工智能工具。
*   **优先处理任务：** 在认知高峰期处理繁重的思考。
*   **最大限度地减少注意力消耗：** 禁用通知，避免同步通信。
*   **避免冗长会议：** 尽量选择电子邮件，因为沟通在精神上可能很累。

他强调了理解特定大脑区域（额叶和顶叶皮层）如何受到上下文切换、心理导航和工作记忆等任务的影响的重要性。 他指出，中风后，病灶附近的过度兴奋会降低癫痫发作的阈值，使得认知超载尤其危险。 帕多尔西承认自己在实施这些策略方面的挣扎，但强调了自我倡导和设定界限的重要性。

---

## 18. AirTips – Bento.me/Linktree的替代品

**原文标题**: AirTips – Alternative to Bento.me/Linktree

**原文链接**: [https://a.coffee/](https://a.coffee/)

AirTips旨在成为Bento.me和Linktree等服务的替代方案，提供一个整合链接和项目的平台。该平台强调紧凑性、可定制性和API就绪性，目前仅限邀请。

主要亮点功能包括：

*   **紧凑性：** 专为信息流线型展示而设计。
*   **可定制性：** 允许用户使用HTML构建精确的UI。
*   **API就绪：** 提供API用于程序化交互。

该平台采用模块化方法，使用户能够添加文本模块、自定义HTML（特别提到Tailwind CSS）和其他元素。提供了潜在布局和内容类型（响应式网格、徽章、卡片、标题、列表、表情符号、内联SVG）的示例。安全性也通过“无脚本”策略得到强调。

该平台还允许展示带有描述和链接的项目。指标也可以添加到平台。最后，还有指向定价、API和自定义HTML文档的链接。

---

## 19. uBlock Origin Lite Apple App Store
uBlock Origin Lite 苹果应用商店

**原文标题**: uBlock Origin Lite Apple App Store

**原文链接**: [https://apps.apple.com/in/app/ublock-origin-lite/id6745342698](https://apps.apple.com/in/app/ublock-origin-lite/id6745342698)

uBlock Origin Lite (uBOL) 是由 Raymond Hill 创建的，可在 Apple App Store 上下载的内容拦截器应用。它提供与流行的 uBlock Origin 扩展类似的默认过滤器列表，包括 uBlock Origin 的内置过滤器、EasyList、EasyPrivacy 以及 Peter Lowe 的广告和跟踪服务器列表。用户可以在应用的选项中启用其他规则集。

uBOL 的一个关键特性是其声明性，意味着过滤直接由浏览器使用 CSS/JS 注入处理，而不是通过持续的后台进程。这最大限度地减少了 CPU 和内存的使用，应用的服务工作线程仅在与设置或弹出面板交互时才处于活动状态。

最新版本 2025.1028.1744 更新了过滤器列表。评论绝大多数是正面的，用户称赞其在 iPadOS 和 Safari 上的可用性以及有效的广告拦截能力。一位评论者指出 TestFlight 版本中早期存在的电池消耗问题，该问题已经得到改善。一个常见的愿望是能够添加自定义列表，但用户通常对默认配置感到满意。

该应用的隐私政策声明开发者不收集任何数据。它是一款免费应用，归类为实用工具，并且兼容运行所需操作系统版本的 iPhone、iPad、Mac 和 Apple Vision 设备。

---

## 20. Kafka 很快——但我会用 Postgres。

**原文标题**: Kafka is Fast – I'll use Postgres

**原文链接**: [https://topicpartition.io/blog/postgres-pubsub-queue-benchmarks](https://topicpartition.io/blog/postgres-pubsub-queue-benchmarks)

本文认为，在许多使用场景中，尤其是中等负载场景下，Postgres 可以作为 Kafka 的可行替代方案，用于发布/订阅消息传递和队列。它挑战了盲目采用复杂、专业的 Kafka 等技术，而不认真考虑其规模和功能是否真正必要的趋势。

作者提出了两个对立的“阵营”：一个追逐流行语，另一个则倾向于常识和更简单的解决方案。他们强调“小数据”运动和“Postgres 复兴”是支持后者的趋势。 论点是，Postgres 凭借其多功能性和可靠性，结合强大的现代硬件，可以用 20% 的精力处理专业系统 80% 的使用场景。

然后，本文展示了 Postgres 作为发布/订阅系统和队列的基准测试。 发布/订阅基准测试使用 Postgres 原语模拟类似 Kafka 的日志结构，表明单节点 Postgres 实例可以处理 4.8 MiB/s 的写入吞吐量和 24.6 MiB/s 的读取吞吐量，且延迟较低。 三节点复制设置保持相似的吞吐量，但延迟略有增加。 队列基准测试虽然显示较低的吞吐量，但仍然表现出可观的性能。

作者总结说，对于许多常见的工作负载，Postgres 可以比 Kafka 更简单、更经济高效的解决方案，尤其是考虑到与供应商管理的 Kafka 服务相关的高成本。 本文鼓励读者考虑将 Postgres 作为一种可行的替代方案，并避免在不清楚了解自身需求的情况下盲目采用复杂的技术。

---

## 21. Minecraft Java版移除混淆

**原文标题**: Minecraft removing obfuscation in Java Edition

**原文链接**: [https://www.minecraft.net/en-us/article/removing-obfuscation-in-java-edition](https://www.minecraft.net/en-us/article/removing-obfuscation-in-java-edition)

Minecraft：Java版将移除混淆代码以简化Mod制作。目前，游戏使用代码混淆来隐藏源代码，迫使Mod制作者费力地解读类和函数。2019年，Mojang发布了“混淆映射”以帮助匹配混淆和未混淆的术语，但现在他们正采取下一步行动，彻底移除代码混淆。

从“混乱山脉”发布后的第一个快照开始，游戏将附带原始变量和函数名称，从而简化Mod制作流程。这意味着Mod的创建、更新和调试将变得更容易，因为Mod制作者不再需要解开复杂的代码或解读不清晰的名称。调试也将变得更容易，因为崩溃日志将变得可读。

为了方便过渡，Mojang将发布“实验性版本”与混淆版本并行。这允许Mod制作者在完全过渡之前测试和调整他们的工具和工作流程。

Mod制作者需要注意的重要方面：混淆映射将从版本.jsons中移除，客户端和服务器.jar文件将不再被混淆，并且每个.jar文件将包含一个LICENSE文件，其中包含EULA的直接链接。Minecraft EULA和使用指南仍然有效，确保所有Mod都遵守既定规则。

---

## 22. 展示一下：用游戏学习德语

**原文标题**: Show HN: Learn German with Games

**原文链接**: [https://www.learngermanwithgames.com/](https://www.learngermanwithgames.com/)

生成摘要时出错

---

## 23. 消费欺诈经济的终结：消费者利用大型语言模型对抗信息不对称

**原文标题**: The end of the rip-off economy: consumers use LLMs against information asymmetry

**原文链接**: [https://www.economist.com/finance-and-economics/2025/10/27/the-end-of-the-rip-off-economy](https://www.economist.com/finance-and-economics/2025/10/27/the-end-of-the-rip-off-economy)

无法访问文章链接。

---

## 24. AOL to be sold to Bending Spoons for roughly $1.5B

**原文标题**: AOL to be sold to Bending Spoons for roughly $1.5B

**原文链接**: [https://www.axios.com/2025/10/29/aol-bending-spoons-deal](https://www.axios.com/2025/10/29/aol-bending-spoons-deal)

无法访问文章链接。

---

## 25. SpiderMonkey 垃圾回收器

**原文标题**: SpiderMonkey Garbage Collector

**原文链接**: [https://firefox-source-docs.mozilla.org/js/gc.html](https://firefox-source-docs.mozilla.org/js/gc.html)

The SpiderMonkey garbage collector (GC) is responsible for managing memory allocation and deallocation in Firefox's JavaScript engine. It's designed for speed and efficiency, handling both JavaScript data and some internal SpiderMonkey structures.

It's a hybrid tracing collector with several key features:

*   **Precise:** It accurately tracks memory layout and stack roots, avoiding unnecessary retention of garbage.
*   **Incremental:** It breaks down execution into smaller slices to minimize pauses for users, though some operations like root marking and compacting are not fully incremental.
*   **Generational:** It uses a two-generation approach (nursery for young, frequently collected objects, and tenured heap for older objects) to optimize collection frequency.
*   **Partially Concurrent:** Some GC tasks, like finalization and memory management, occur concurrently with the main program.
*   **Parallel:** GC slices are processed in parallel to leverage multi-core systems.
*   **Compacting:** It rearranges data within arenas to reduce fragmentation, though this is a less frequent, non-incremental operation.
*   **Partitioned Heap:** Uses 'zones' which are independent heaps that can be collected independently. This helps with incremental collection.

The collector aims to minimize user impact by performing most collection work incrementally and in parallel. Compacting is used to combat fragmentation when necessary. The article directs readers to the SpiderMonkey source code for more detailed information.


---

## 26. Oracle 在 23ai 中采用了 BOOLEAN，而 PostgreSQL 一直都有。

**原文标题**: Oracle has adopted BOOLEAN in 23ai and PostgreSQL had it forever

**原文链接**: [https://hexacluster.ai/blog/postgresql/oracles-adoption-of-native-boolean-data-type-vs-postgresql/](https://hexacluster.ai/blog/postgresql/oracles-adoption-of-native-boolean-data-type-vs-postgresql/)

本文探讨了Oracle最近（2025年）在其23ai版本中采用原生`BOOLEAN`数据类型，并将其与已支持`BOOLEAN`超过二十年的PostgreSQL进行了对比。 在23ai之前，Oracle开发人员使用`VARCHAR2`或`NUMBER`等变通方法来表示布尔值，导致因转换和更大的索引而可能出现性能问题。

本文重点介绍了原生`BOOLEAN`类型的优势，强调了其在存储（PostgreSQL中为单字节）、更简单的查询（无需字符串比较）、更快的过滤和更高的可读性方面的效率。 它对比了Oracle（23ai之前）和PostgreSQL中的表结构和insert/select语句，以展示其益处。

本文提供了一个表格，从含义、存储、类型安全、查询简易性、值解释、可读性和语言集成等方面比较了`BOOLEAN`与`CHAR(1)/CHAR(5)`和`SMALLINT/NUMBER(1)`的变通方法，并得出结论：`BOOLEAN`是最佳数据类型。

最后，本文推广了HexaRocket，该工具可自动执行从Oracle到PostgreSQL的迁移，包括自动将Oracle的`CHAR(1)`和`NUMBER(1)`映射到PostgreSQL的`BOOLEAN`。它还提到了HexaCluster的PostgreSQL支持和迁移服务。

---

## 27. 伯克利乱序RISC-V处理器 (Boom) (2020)

**原文标题**: Berkeley Out-of-Order RISC-V Processor (Boom) (2020)

**原文链接**: [https://docs.boom-core.org/en/latest/sections/intro-overview/boom.html](https://docs.boom-core.org/en/latest/sections/intro-overview/boom.html)

生成摘要时出错

---

## 28. 伯克利乱序RISC-V处理器(Boom)(2020)

**原文标题**: Berkeley Out-of-Order RISC-V Processor (Boom) (2020)

**原文链接**: [https://docs.boom-core.org/en/latest/sections/intro-overview/boom.html](https://docs.boom-core.org/en/latest/sections/intro-overview/boom.html)

The Berkeley Out-of-Order Machine (BOOM) is an open-source out-of-order RISC-V processor design heavily influenced by the MIPS R10000 and Alpha 21264 processors. Like these predecessors, BOOM employs a unified physical register file design, enabling explicit register renaming.

A key feature of BOOM is its implementation in Chisel, a hardware construction language. This allows BOOM to be a *generator* of out-of-order designs, rather than a single, fixed core. This means BOOM represents a family of configurable processor designs.

Furthermore, BOOM utilizes the Rocket Chip SoC generator as a library, leveraging its micro-architectural structures like TLBs and PTWs. This modular approach facilitates the construction of complete System-on-Chips (SoCs) incorporating a BOOM core. In summary, BOOM is a flexible and customizable out-of-order RISC-V processor design leveraging modern hardware generation techniques and established microarchitectural principles.


---

## 29. 尝试是培养良好品味的方式。

**原文标题**: Tinkering is a way to acquire good taste

**原文链接**: [https://seated.ro/blog/tinkering-a-lost-art](https://seated.ro/blog/tinkering-a-lost-art)

生成摘要时出错

---

## 30. 光标 2.0

**原文标题**: Cursor 2.0

**原文链接**: [https://cursor.com/changelog](https://cursor.com/changelog)

Cursor 2.0 引入了重大改进，侧重于智能体编码、性能和团队协作。主要功能包括发布更快的智能体编码模型“Composer”，以及浏览器代理普遍可用 (GA)，该代理具有嵌入式编辑器工具。 它还改进了代码审查，并普遍提供了 macOS 上的沙盒终端，从而提高了安全性。

通过为所有团队成员集中管理的自定义命令和规则，团队协作得到增强。语音模式支持通过语音控制代理。通过语言服务器协议 (LSP)，性能得到了大幅提升，尤其是在代理和差异使用方面，包括更快的 Python 和 TypeScript LSP 以及内存泄漏修复。

计划模式允许使用一个模型创建计划，并使用另一个模型构建，无论是在前台还是后台。共享团队命令和提示已得到简化，并且提示 UI 得到了改进。Agent Harness 得到了增强，显著提高了 GPT-5 Codex 的质量。云代理提供 99.9% 的可靠性、即时启动和新的 UI。

对于企业用户，Cursor 2.0 提供了沙盒终端的管理控制、钩子的云分发以及管理事件的审计日志。

---

## 31. 在生产环境中持续进行Nvidia CUDA性能分析

**原文标题**: Continuous Nvidia CUDA Profiling in Production

**原文链接**: [https://www.polarsignals.com/blog/posts/2025/10/22/gpu-profiling](https://www.polarsignals.com/blog/posts/2025/10/22/gpu-profiling)

生成摘要时出错

---

## 32. 当我们谈论侧载时，我们在谈论什么

**原文标题**: What we talk about when we talk about sideloading

**原文链接**: [https://f-droid.org/2025/10/28/sideloading.html](https://f-droid.org/2025/10/28/sideloading.html)

本文认为，尽管谷歌推出了新的开发者验证要求，实际上剥夺了用户选择安装软件的自由，但谷歌却虚假地声称侧载在安卓系统中不会消失。作者批评“侧载”这一术语具有误导性，并强调它仅仅意味着安装软件，无论来源如何。

作者认为，谷歌的开发者验证法令迫使开发者向谷歌注册，支付费用并提供身份证明才能分发应用程序，这破坏了安卓的开放性，并赋予谷歌对软件分发的过度控制权。这限制了用户从 F-Droid 或直接从开发者处安装应用程序的能力，即使是使用像三星 Galaxy Store 这样的替代应用商店也不例外。

作者质疑谷歌声称侧载会导致更多恶意软件的说法，并引用了在 Google Play 商店中发现恶意软件的案例，并强调了商业动机有可能损害谷歌的判断。

本文强调了谷歌最近备受争议的行为，例如削弱 Chrome 中的广告拦截器和限制 Android 开放源代码项目 (AOSP)，进一步证明了一种走向控制的趋势。它呼吁消费者倡导开放的安卓生态系统，并敦促开发者拒绝谷歌的开发者注册计划。作者认为用户拥有自己的手机，并有权选择他们的软件来源。

---

## 33. 我们就是要无聊。

**原文标题**: Boring is what we wanted

**原文链接**: [https://512pixels.net/2025/10/boring-is-what-we-wanted/](https://512pixels.net/2025/10/boring-is-what-we-wanted/)

This article argues that the "boring" incremental upgrades of Apple silicon Macs are exactly what users wanted after years of inconsistent hardware during the PowerPC and Intel eras. The author reminisces about the transformative impact of the M1 Macs, highlighting their superior speed, efficiency, and battery life, a departure from the trade-offs inherent in previous PC computing.

The author contends that Apple's control over its silicon has allowed for predictable and consistent progress, shipping regular updates that improve both power and efficiency. He contrasts this with the past, where Mac updates were often delayed due to reliance on external partners, leading to issues like faulty NVIDIA cards and overheating iMacs. While acknowledging Apple's past mistakes (e.g., the butterfly keyboard), the author emphasizes that owning the core technology allows Apple to deliver steady hardware development.

The piece directly addresses the criticism that recent M-series chip updates are "boring," arguing that this predictability is a positive outcome. The author points to a chart illustrating consistent improvements in Apple silicon, suggesting that the upgrades are meaningful, especially for users who don't upgrade annually. The author concludes that calling Apple silicon's success "boring" is downplaying its achievements and ignoring the consistent progress users have long desired.


---

## 34. 字形：通过视觉-文本压缩进行上下文窗口缩放

**原文标题**: Glyph: Scaling Context Windows via Visual-Text Compression

**原文链接**: [https://github.com/thu-coai/Glyph](https://github.com/thu-coai/Glyph)

生成摘要时出错

---

## 35. UI 不是模型纯函数的应用——React.js 和 Cocoa 的对比 (2018)

**原文标题**: UIs Are Not Pure Functions of the Model – React.js and Cocoa Side by Side (2018)

**原文链接**: [https://blog.metaobject.com/2018/12/uis-are-not-pure-functions-of-model.html](https://blog.metaobject.com/2018/12/uis-are-not-pure-functions-of-model.html)

This article compares React.js's approach to UI development with Cocoa's MVC framework, arguing that React's core premise of UIs being pure functions of the model is flawed and leads to unnecessary complexity.

The author contrasts React's concepts of transformation, abstraction, composition, state management, memoization, and list handling with Cocoa's equivalents. They contend that Cocoa, with its object-oriented approach and stable view hierarchy, handles these aspects more efficiently and naturally.

The author criticizes React's reliance on pure functions, arguing that UIs inherently have state specific to their projection (e.g., scroll position) and shouldn't be forced into an immutable data model. They also point out that React's attempts to address the limitations of this pure function approach, through techniques like memoization, state maps, and algebraic effects, only add complexity and contradict the initial premise.

Furthermore, the article highlights Cocoa's advantages in handling UI stability and optimization through its event loop and drawRect method. It argues that Cocoa's model allows for direct manipulation of UI-specific state and context without the need for complex data passing mechanisms like React's "context." The author concludes that the pursuit of UIs as pure functions leads to an "avalanche of problems" and is fueled by an overzealous embrace of functional programming concepts.


---

## 36. Apple 将在 macOS 28 中逐步淘汰 Rosetta 2。

**原文标题**: Apple will phase out Rosetta 2 in macOS 28

**原文链接**: [https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment](https://developer.apple.com/documentation/apple-silicon/about-the-rosetta-translation-environment)

苹果将在macOS 28中逐步淘汰Rosetta 2，这表明苹果计划在macOS 28发布时从其操作系统中移除Rosetta 2。

Rosetta 2是一个转换环境，使配备Apple芯片的Mac能够运行为基于Intel的Mac构建的应用程序。其目的是弥合从Intel处理器到Apple芯片过渡期间的差距，确保与旧软件的兼容性。

包含“关于 Rosetta 转换环境 | Apple Developer 文档”链接表明，逐步淘汰将涉及开发人员需要更新或重新编译其应用程序，使其与 Apple 芯片原生兼容。开发人员可能需要考虑提供支持两种架构的通用二进制文件。

逐步淘汰 Rosetta 2 表明 Apple 认为向 Apple 芯片的过渡已基本完成，并且对兼容层的需求减少。这可能意味着绝大多数常用应用程序已更新为在 Apple 芯片上原生运行，或者存在合适的替代方案。

虽然没有启用 JavaScript 就无法完整查看 Apple Developer 文档中的链接页面，但标题强烈暗示了 Apple 未来移除 Rosetta 2 的意图。此举可能会促使开发人员优先考虑原生 Apple 芯片支持，以避免运行未来版本 macOS 的用户出现兼容性问题。

---

## 37. 生成式AI图像编辑对决

**原文标题**: Generative AI Image Editing Showdown

**原文链接**: [https://genai-showdown.specr.net/image-editing](https://genai-showdown.specr.net/image-editing)

生成式AI图像编辑工具大比拼：本文重点比较用于图像编辑的不同生成式AI(GenAI)工具。它可能会考察各种AI平台在修改、增强或创建图像方面的能力、优势和劣势。

这次比拼可能会根据以下标准评估这些工具：

*   **易用性：** 这些工具对于不同专业水平用户的直观性和可访问性如何。
*   **图像质量：** 生成或修改后的图像质量，包括分辨率、细节和真实感。
*   **功能性：** 这些工具可以执行的编辑任务范围，例如图像修复（填充缺失部分）、图像扩展（扩展图像边界）、风格迁移、物体移除等等。
*   **速度和效率：** 这些工具处理图像和生成结果的速度有多快。
*   **成本：** 这些工具的定价模式，无论是免费、订阅制还是按次付费。
*   **准确性：** 这些工具解释和执行用户提示和指令的能力如何。

本文旨在帮助读者了解当前生成式AI图像编辑工具的现状，并帮助他们根据自身特定需求和预算选择最佳方案。它可能会重点介绍市场上的主要竞争者，并讨论这个快速发展领域中未来的潜在发展。最终，本文旨在告知读者使用AI转换图像的能力和局限性。

---

## 38. Google Play商店停止要求美国地区使用Google Play结算系统

**原文标题**: Google Play Store Stops Requiring the Use of Google Play Billing in the US

**原文链接**: [https://support.google.com/googleplay/android-developer/answer/15582165?hl=en](https://support.google.com/googleplay/android-developer/answer/15582165?hl=en)

为响应美国第九巡回法院于2025年9月12日维持的美国地方法院禁令，自2025年10月29日起，Google Play商店针对服务于美国用户的开发者实施了重大政策变更。

关键在于，Google将不再强制要求在美国Play商店分发的应用程序内购买使用Google Play结算系统。 开发者现在可以自由使用其他应用内支付方式，并向用户告知其可用性。 此外，开发者现在可以告知用户其应用程序在Google Play商店之外的价格和可用性，并提供直接下载或交易的链接。 他们还可以自由告知用户其他支付方式的可用性。

Google还承诺不会强迫开发者根据是否使用Google Play结算系统来确定其应用程序的定价。

这些政策变更明确针对美国市场，且仅在美国地方法院的命令仍然有效时生效。 Google声明这些更新取代了其现有支付政策中任何冲突的限制。 Google计划分享有关程序要求和业务模式调整的更多细节，以维护用户信任和安全，并纳入来自开发者和用户的反馈。 与该禁令相一致的其他政策调整将在Google Play政策页面上公布。

---

## 39. 新型攻击正在削弱英伟达、AMD和英特尔的安全区域防御。

**原文标题**: New attacks are diluting secure enclave defenses from Nvidia, AMD, and Intel

**原文链接**: [https://arstechnica.com/security/2025/10/new-physical-attacks-are-quickly-diluting-secure-enclave-defenses-from-nvidia-amd-and-intel/](https://arstechnica.com/security/2025/10/new-physical-attacks-are-quickly-diluting-secure-enclave-defenses-from-nvidia-amd-and-intel/)

本文重点介绍了英伟达、AMD和英特尔的可信执行环境（TEE）中的关键漏洞，这些漏洞破坏了它们提供的安全保证。一种名为"TEE.fail"的新攻击通过在内存芯片和主板之间物理插入硬件来绕过最新的TEE保护，只需要短暂的物理访问和内核操作系统妥协。这种攻击以及之前的Battering RAM和Wiretap等攻击，暴露了TEE在物理攻击面前的局限性，而芯片制造商通常将此类攻击排除在其威胁模型之外。

本文批评了芯片制造商和TEE用户（包括Cloudflare、Anthropic、微软、Meta和Signal等主要科技公司）的误导性营销，他们夸大了所提供的保护，往往暗示能够抵御物理攻击。研究人员HD Moore强调，客户很难理解他们在机密计算中获得的实际安全性。

这些攻击利用确定性加密，这是一种较弱的加密形式，容易受到重放攻击。"TEE.fail"允许攻击者窃取证明密钥、冒充安全飞地、解密流量并泄露敏感数据。该攻击相对便宜且易于执行，只需要现成的设备。BuilderNet、dstack和Secret Network等服务已被证明容易受到攻击。

文章最后讨论了潜在的缓解措施，例如向密文块添加熵以及探索更强大的加密方法，同时也承认了在TEE中平衡性能和安全性的挑战。文章强调了理解TEE局限性的重要性，尤其是在无法保证物理安全的环境中。

---

## 40. YouTube 清除了演示绕过 Win 11 账户要求的视频

**原文标题**: Win 11 videos demonstrating account requirements bypass purged from YouTube

**原文链接**: [https://www.tomshardware.com/tech-industry/big-tech/windows-11-videos-demonstrating-account-and-hardware-requirements-bypass-purged-from-youtube-platform-says-content-encourages-dangerous-or-illegal-activities-that-risk-serious-physical-harm-or-death](https://www.tomshardware.com/tech-industry/big-tech/windows-11-videos-demonstrating-account-and-hardware-requirements-bypass-purged-from-youtube-platform-says-content-encourages-dangerous-or-illegal-activities-that-risk-serious-physical-harm-or-death)

YouTube删除了CyberCPU Tech频道演示绕过Windows 11硬件和账户要求的视频。创作者Rich怀疑微软是此次下架的幕后推手，尽管YouTube声称违反了“有害或危险内容”指南，Rich认为这不合逻辑，因为绕过Windows 11的限制不会造成人身危险。

Rich对YouTube缺乏关于删除的具体原因的明确沟通表示沮丧，并表示他感到被迫自我审查。他承认YouTube有权控制其平台，但希望获得透明度。

这篇文章强调了关于Windows 11严格要求的持续争论，这些要求正促使一些用户考虑其他选择，例如Mac电脑，或者像评论中建议的那样，使用像Bazzite这样的Linux发行版。这些视频的删除恰逢微软推动Windows 10用户升级之时，而由于设定的要求，这些升级对许多用户来说都很困难。

文章最后指出，下架事件仍存在不确定性，并提出了各种可能性，从YouTube的AI算法到微软的直接要求。文章还提到YouTube最近也惩罚了Gamers Nexus。

---

## 41. 轮式倒立摆模型

**原文标题**: Wheeled Inverted Pendulum Model

**原文链接**: [https://scaron.info/robotics/wheeled-inverted-pendulum-model.html](https://scaron.info/robotics/wheeled-inverted-pendulum-model.html)

This article introduces the Wheeled Inverted Pendulum (WIP) model, a nonlinear system consisting of a concentrated mass attached to a massless pole and active wheels. Unlike the cart-pole model with passive wheels, the WIP's wheels are actively driven. The article defines the system's parameters: pole length (ℓ), mass (m), pole angle (θ), and wheel position on the ground (r).

A key assumption is that the wheels roll without slipping, linking the wheel's angular coordinate (ϕ) to its ground position (r). The core of the article focuses on presenting the equation of motion for the WIP: ℓθ̈ = g sin(θ) - r̈ cos(θ). This equation describes the relationship between the pendulum's angular acceleration (θ̈), gravity (g), the angle (θ), and the wheel's linear acceleration (r̈).

The article highlights the relevance of this model for optimal control applications in real robots. It mentions the intention to discuss the linearization and discretization of the equation of motion for small angles, suggesting that this simplified form is more amenable to control design.


---

## 42. Wacl – 用于 WebAssembly 的 Tcl 发行版

**原文标题**: Wacl – A Tcl Distribution for WebAssembly

**原文链接**: [https://github.com/ecky-l/wacl](https://github.com/ecky-l/wacl)

Wacl是一个为WebAssembly设计的Tcl发行版，它允许开发者将Tcl解释器嵌入到Web浏览器中并与JavaScript集成。这使得Tcl开发者可以使用他们熟悉的工具构建客户端Web应用程序，并利用现有的Tcl代码库（如Tcllib）。Wacl构建于Emtcl项目之上，添加了诸如可通过JavaScript访问的Tcl解释器实例、事件循环、客户端套接字（支持通过websockets进行二进制通信）以及用于Tcl库和软件包的虚拟文件系统等功能。

主要优势包括使用Tcl进行Web开发、在浏览器中重用现有的Tcl代码，以及与JavaScript相比，WebAssembly可能带来更小的应用程序尺寸和更快的性能。

Wacl包含诸如`wacl`（用于DOM操作和调用Javascript）、`tDOM`、`json`、`html`、`javascript`、`ncgi`和`rl_json`等扩展。包含扩展可以增加功能，但也会增加下载大小，需要在功能和带宽考虑之间取得平衡。

文章引导用户尝试演示并下载预编译版本。它概述了构建过程，需要Emscripten SDK和Unix/Linux环境。构建会生成WebAssembly（首选）或JavaScript文件。文章还提供了关于重置构建环境和重新创建补丁的指导。

---

## 43. AirPods Pro 3 的飞行问题

**原文标题**: The AirPods Pro 3 flight problem

**原文链接**: [https://basicappleguy.com/basicappleblog/the-airpods-pro-3-flight-problem](https://basicappleguy.com/basicappleblog/the-airpods-pro-3-flight-problem)

生成摘要时出错

---

## 44. Powerful and precise multi-color lasers now fit on a single chip

**原文标题**: Powerful and precise multi-color lasers now fit on a single chip

**原文链接**: [https://phys.org/news/2025-10-powerful-precise-multi-lasers-chip.html](https://phys.org/news/2025-10-powerful-precise-multi-lasers-chip.html)

哥伦比亚大学研究人员在Michal Lipson的带领下，开发出一种强大的、精确的多色激光器，该激光器可安装在单个芯片上。这项突破涉及在紧凑的硅光子芯片上创建频率梳，这是一种具有许多有序颜色的特殊光。传统上，产生这种频率梳需要大型、昂贵的激光器和放大器。

该团队利用了多模激光二极管，这种二极管以其功率而闻名，但也以其“混乱”的光束而闻名。他们利用硅光子技术实现了一种“锁定机制”，以净化激光器的输出，从而产生干净、稳定且高度相干的光束。然后，芯片的非线性光学特性将这种纯化的光束分成数十种均匀间隔的颜色，从而创建了频率梳。

这项创新具有多项优势：与目前使用多个独立激光器的机架系统相比，它缩小了尺寸、降低了成本和能耗。它还为更快、更节能的数据传输打开了大门。

主要应用是在数据中心，由于人工智能的兴起，对高带宽光源的需求不断增长。这些多波长梳使波分复用 (WDM) 成为可能，从而允许多个数据流同时通过同一光纤传输。

除了数据中心之外，该芯片还在便携式光谱仪、超精密光钟、紧凑型量子设备和先进的LiDAR系统等方面具有潜在应用。这项开发代表着将实验室级光源引入实用、现实世界设备的重要一步。

---

## 45. 默认HTTPS

**原文标题**: HTTPS by default

**原文链接**: [https://security.googleblog.com/2025/10/https-by-default.html](https://security.googleblog.com/2025/10/https-by-default.html)

2026年10月（Chrome 154），谷歌Chrome浏览器将默认启用“始终使用安全连接”功能，在访问非HTTPS公共网站之前会提示用户授权。此举旨在打击导航劫持，保护用户免受源于不安全HTTP连接的恶意软件和社交工程攻击。尽管HTTPS的普及率已显著提高，稳定在95-99%左右，但剩余的HTTP连接仍然存在风险。

默认设置仅适用于公共网站，以减少对用户的干扰，因为使用HTTPS证书保护私有网站（例如，本地IP地址）更为复杂。之前对一部分用户进行的实验表明，该设置能够更有效地保护用户安全，且不会产生过多警告，中位数用户每周看到的警告少于一次。谷歌正在与仍在使用HTTP的组织合作，以便在更改之前迁移到HTTPS。

Chrome的“始终使用安全连接”设置（公共网站变体）将于2026年4月为启用增强型安全浏览的用户启用。用户可以根据需要禁用警告。谷歌鼓励网站开发者和IT专业人员现在启用该设置，以识别需要迁移的网站，并查阅资源来理解和缓解潜在的警告。

未来的工作将侧重于减少HTTPS普及的障碍，特别是对于本地网络站点，从而为更强大的HTTP保护铺平道路。

---

## 46. 保持互联网高速且安全：推出默克尔树证书

**原文标题**: Keeping the Internet fast and secure: introducing Merkle Tree Certificates

**原文链接**: [https://blog.cloudflare.com/bootstrap-mtc/](https://blog.cloudflare.com/bootstrap-mtc/)

This article discusses the challenge of transitioning the Internet's Web Public-Key Infrastructure (WebPKI) to post-quantum (PQ) cryptography to mitigate the threat of quantum computers breaking current cryptographic methods. While PQ algorithms exist, their significantly larger signature and public key sizes pose a performance problem for TLS handshakes, potentially degrading performance before quantum computers pose an immediate threat.

To address this, Cloudflare proposes Merkle Tree Certificates (MTCs) as a solution to redesign the WebPKI for a smooth transition to PQ authentication without performance impact. MTCs aim to minimize the number of public keys and signatures in TLS handshakes.

The article explains the current WebPKI's reliance on multiple signatures and public keys due to certificate chains and Certificate Transparency (CT) requirements. MTCs streamline this by allowing client validation information to be disseminated out-of-band. A client with up-to-date information only needs one signature, one public key, and a Merkle tree inclusion proof during the TLS handshake. This is achieved by having Certification Authorities (CAs) generate signatureless certificates in batches and use Merkle trees to prove inclusion of a certificate in a signed batch.

Cloudflare announces an experimental deployment of MTCs in collaboration with Chrome Security to test its effectiveness and safety. The experiment seeks to demonstrate that MTCs can enable the adoption of PQ certificates without sacrificing performance.


---

## 47. 英伟达入股诺基亚10亿美元

**原文标题**: Nvidia takes $1B stake in Nokia

**原文链接**: [https://www.cnbc.com/2025/10/28/nvidia-nokia-ai.html](https://www.cnbc.com/2025/10/28/nvidia-nokia-ai.html)

英伟达投资10亿美元入股诺基亚，收购这家芬兰公司的新股。该消息导致诺基亚股价飙升22%。诺基亚计划将发行股票所得资金用于其人工智能计划和其他公司目标。

除了投资之外，英伟达和诺基亚还建立了战略合作伙伴关系，共同开发下一代6G蜂窝技术。诺基亚将调整其5G和6G软件以在英伟达的芯片上运行，双方还将合作开发用于人工智能应用的联网技术。此外，英伟达将考虑将诺基亚的技术整合到其未来的AI基础设施计划中。

虽然诺基亚以其早期手机而闻名，但它已经发展成为电信提供商的主要5G蜂窝设备供应商。此次合作符合英伟达在人工智能领域对关键战略合作伙伴进行股权投资的更广泛战略。最近的投资包括对英特尔、OpenAI、Wayve和Nscale的承诺。预计此次合作和投资将在华盛顿特区举行的英伟达开发者大会上进一步讨论，届时英伟达首席执行官黄仁勋将发表主题演讲。

---

## 48. 恶意机器人毁了我的周末。

**原文标题**: Aggressive bots ruined my weekend

**原文链接**: [https://herman.bearblog.dev/agressive-bots/](https://herman.bearblog.dev/agressive-bots/)

2025年10月25日，熊博客因反向代理在大量恶意机器人流量的冲击下崩溃，首次发生重大故障。作者详细描述了困扰互联网的三种主要机器人：AI抓取器、寻找漏洞的恶意抓取器，以及无意中对网站进行DDoS攻击的未经检查的自动化程序/抓取器。虽然AI抓取器可以管理，但恶意抓取器和未经检查的自动化程序构成了重大威胁。

此次故障发生在一次DDoS事件中，该事件涉及来自恶意或攻击性抓取器的每分钟数万个页面请求，即使采取了现有的机器人缓解措施，反向代理仍不堪重负。作者的监控工具也未能通知他们该问题，使问题更加复杂。

为了防止未来发生故障，作者已实施了多项更改：使用电话、电子邮件和短信的第二项服务增加监控冗余，提高反向代理上的速率限制和机器人缓解，将反向代理的容量扩大五倍，为反向代理实施自动重启（以防长时间不活动），并创建状态页面以提高透明度。

作者强调了由于机器人活动导致互联网日益充满敌意，以及保护有价值的在线空间的重要性。文章最后承认了与恶意机器人活动之间持续存在的“军备竞赛”。

---

## 49. 光标 2.0

**原文标题**: Cursor 2.0

**原文链接**: [https://cursor.com/blog/2-0](https://cursor.com/blog/2-0)

Cursor 2.0 引入两大更新：Composer 编码模型和全新多智能体界面，增强了 Cursor 作为智能体协同编码平台的能力。

Composer 是一款全新开发的模型，速度是同类模型的四倍，可提供低延迟、智能体驱动的编码，大多数任务在 30 秒内完成。它擅长理解和处理大型代码库，这得益于其在代码库范围语义搜索等工具上的训练。

重新设计的界面优先考虑智能体而非文件，使用户能够专注于期望的结果，而智能体则负责处理细节。用户可以轻松访问文件或恢复到经典 IDE 视图。Cursor 2.0 能够并行运行多个智能体，并由 git 工作树或远程机器提供支持，从而可以尝试不同的模型以优化结果，尤其是在处理复杂任务时。

针对代码审查和测试中的瓶颈，Cursor 2.0 简化了变更审查，并提供了根据需要深入研究代码的工具。原生浏览器工具使 Cursor 能够测试其工作并迭代改进解决方案，直到获得正确的结果。Cursor 2.0 现已可在 cursor.com/download 下载。

---

## 50. 阅读人工智能生成的博客文章是一种侮辱。

**原文标题**: It's insulting to read AI-generated blog posts

**原文链接**: [https://blog.pabloecortez.com/its-insulting-to-read-your-ai-generated-blog-post/](https://blog.pabloecortez.com/its-insulting-to-read-your-ai-generated-blog-post/)

这篇博文强烈表达了对人工智能生成内容的不屑，认为它侮辱了人类读者，并且不利于写作者的成长。作者认为使用人工智能来创作内容是懒惰的行为，剥夺了读者真实的人性连接、幽默感和经验。

核心论点是写作应该是一种个人的努力，即使其中包含错误和瑕疵。作者鼓励写作者拥抱在创作过程中挣扎所带来的学习过程，强调这才是我们之所以为人的原因。语法工具和翻译工具可以使用，但用人工智能来创造文章的核心内容是错误的。

此外，这篇文章强调了人际互动和互相支持的重要性。作者认为，人工智能生成的内容在作者和读者之间制造了障碍，阻碍了真正的互动和合作机会。他们鼓励写作者克服寻求帮助的恐惧，并通过真实的沟通来建立关系。最好的想法是用心感受到的。

总而言之，作者敦促内容创作者放弃人工智能生成的写作，转而分享他们自己的想法和经验，因为作者相信这能够促进更深层次的连接和个人成长。

---

## 51. Fil-C：一种内存安全的C实现

**原文标题**: Fil-C: A memory-safe C implementation

**原文链接**: [https://lwn.net/SubscriberLink/1042938/658ade3768dd4758/](https://lwn.net/SubscriberLink/1042938/658ade3768dd4758/)

Fil-C 是一种内存安全的 C 和 C++ 实现，旨在让现有的 C 代码无需修改即可安全运行，解决了通常与 C 的指针运算等特性相关的内存安全问题。 Fil-C 基于 Clang，目标是“狂热的兼容性”，并且已经证明了它能够编译一个完整的内存安全的 Linux 用户空间。

核心挑战是指针处理，Fil-C 通过“InvisiCaps”来解决这个问题，该方法将指针分成可信的“能力”和不可信的“地址”组件。 这涉及为每个指针在辅助分配中存储额外的元数据，从而增加内存使用量并引入一些性能开销。 虽然这种方法可能会使程序速度降低约四倍，但优化工作仍在进行中。

Fil-C 使用并发、并行的垃圾回收器来回收内存，利用辅助能力信息来精确跟踪活动对象。 它采用“安全点”与线程在垃圾回收和信号处理期间进行同步，从而确保信号安全的内存分配。

这篇文章重点介绍了使用 Fil-C 成功编译内存安全的 Linux From Scratch 系统，证明了其使现有 C 程序具有内存安全性的潜力。 虽然它没有解决所有形式的未定义行为，但它针对的是与内存相关的漏洞。 尽管 Fil-C 仍相对不成熟，但它为那些优先考虑内存安全而非绝对性能的项目提供了一个可行的选择。

---

## 52. 我们需要一个更清晰的关于人工智能辅助开源贡献的框架。

**原文标题**: We need a clearer framework for AI-assisted contributions to open source

**原文链接**: [https://samsaffron.com/archive/2025/10/27/your-vibe-coded-slop-pr-is-not-welcome](https://samsaffron.com/archive/2025/10/27/your-vibe-coded-slop-pr-is-not-welcome)

萨姆的文章强调了人工智能辅助代码提交泛滥日益严重的问题，这些提交以低质量、难以审查的代码充斥开源项目，被称为“AI风格的垃圾PR”。虽然人工智能工具使代码生成变得容易，但它们并没有减轻维护者进行代码审查的负担。这导致了一种情况，即贡献者花费最少的时间生成代码，而维护者却花费不成比例的时间来解读和纠正代码，从而导致沮丧和倦怠。

作者提出了一个明确的区分，即“原型”和“准备审查的PR”。原型是人工智能生成的演示，旨在探索想法，而不遵守项目标准或保证代码质量。这些应该作为分支或视频演示分享，并清楚地标记为人工智能辅助的探索。另一方面，准备审查的PR是完整的、经过审查的贡献，符合项目准则，并准备好供人工审查。作者强调，原型和可用于生产的PR之间的差距可能很大。

这篇文章警告不要完全禁止人工智能贡献，因为如果负责任地使用，它们可能是有益的。相反，作者提倡设定明确的期望，尊重维护者的时间，并鼓励贡献者对他们的代码负责，无论是否使用了人工智能。通过正确标记贡献并遵守项目准则，开发人员可以确保人工智能的辅助能够增强，而不是阻碍开源生态系统。

---

## 53. 越轨行为的衰落

**原文标题**: The decline of deviance

**原文链接**: [https://www.experimental-history.com/p/the-decline-of-deviance](https://www.experimental-history.com/p/the-decline-of-deviance)

亚当·马斯特罗亚尼认为，无论是负面还是正面的越轨行为，在社会各个方面都在减少。他提供数据显示，青少年参与饮酒、吸毒和犯罪等冒险行为正在减少。成年人犯罪也在减少，邪教的形成也显著减少。

除了负面越轨行为，甚至中性或积极的越轨行为也变得不那么常见。人们不太可能搬离家乡，导致接触不同文化和体验的机会减少。音乐、电影和艺术等创意领域正在经历停滞和同质化，原创想法减少，对既有系列的依赖增加。互联网曾经是独特和怪异表达的天堂，现在变得越来越标准化和审美统一。建筑、品牌，甚至科学也表现出类似的趋势，趋向于统一和缺乏创新。

马斯特罗亚尼承认存在相反的论点，例如大规模枪击事件的增加和更独特的婴儿名字，但他认为这些并不能抵消更广泛的趋势。他认为，这种下降的一个重要驱动因素是人们对安全和生存的重视程度提高。随着预期寿命的增加以及与越轨行为相关的风险变得更加明显，个人更有动力去遵守规范，避免可能危及自身福祉的行为。

---

## 54. 影玻计划

**原文标题**: Project Shadowglass

**原文链接**: [https://shadowglassgame.com](https://shadowglassgame.com)

“影镜计划”是一款正在开发中的沉浸式模拟游戏，灵感来源于《神偷》、《杀出重围》和《网络奇兵》等经典作品。 该游戏采用独特的3D像素艺术美学，承诺提供怀旧的像素化画面，并拥有完整的360°自由度。

玩家将扮演一个黑暗压抑世界中的盗贼，依靠智慧和工具生存。 开发商强调，该游戏完全是手工制作的，没有使用人工智能生成的内容，甚至占位符素材也是开源创作。

该游戏目前处于早期开发阶段，专注于构建核心系统。 包含第一个可玩任务的 Alpha Demo 计划于 2026 年初发布，随后将进行 Beta 测试以收集社区反馈。 包含扩展内容的 Early Access 计划于 2027 年推出，完整发布日期尚未确定。 开发商鼓励感兴趣的玩家加入以提前体验演示和开发更新，旨在让社区参与到游戏的开发中来。

---

## 55. 能源部称其为纳税人节省了75.6亿美元。实际金额较少。

**原文标题**: The DOE said it was saving taxpayers $7.56B. The actual amount is less

**原文链接**: [https://www.cpr.org/2025/10/27/doe-funding-cuts-overstated-data-shows/](https://www.cpr.org/2025/10/27/doe-funding-cuts-overstated-data-shows/)

能源部报告的纳税人节省额与实际节省额存在差异；涉及乔治·弗洛伊德时期警察改革法的2000万美元陪审团裁决；实质上强调了能源部在纳税人节省方面的潜在财务误报以及对警察改革努力的重大法律挑战。

---

## 56. 具名颜色覆盖的RGB空间可视化

**原文标题**: A visualization of the RGB space covered by named colors

**原文链接**: [https://codepen.io/meodai/full/zdgXJj/](https://codepen.io/meodai/full/zdgXJj/)

无法访问文章链接。

---

## 57. EuroLLM：欧洲制造，支持全部24种欧盟官方语言的LLM

**原文标题**: EuroLLM: LLM made in Europe built to support all 24 official EU languages

**原文链接**: [https://eurollm.io/](https://eurollm.io/)

EuroLLM是在欧洲开发的大型语言模型，旨在支持所有24种欧盟官方语言。它是一个开源项目，旨在赋能欧洲的数字化未来并促进人工智能主权。目前，旗舰模型是EuroLLM-9B，一个拥有90亿参数的模型，在超过4万亿个多语言tokens上进行训练。还有一个较小的17亿参数模型，针对边缘设备进行了优化。

EuroLLM的关键特性包括其多语言能力、在语言相关任务（问答、摘要、翻译）中的高性能，以及为研究人员、组织和公民提供的开源可用性。未来的计划包括增加对视觉和语音的多模态支持。

该项目是Unbabel、高等技术学院、爱丁堡大学和其他机构之间的合作，并得到Horizon Europe、欧洲研究理事会和EuroHPC的支持。它在MareNostrum 5超级计算机上进行训练。涉及的关键人物包括André Martins、Alexandra Birch、Nuno Guerreiro和Pierre Colombo，他们都是机器学习和自然语言处理方面的专家。这些模型可在Hugging Face上获得。

---

## 58. 为什么有些无线电塔会闪烁？

**原文标题**: Why do some radio towers blink?

**原文链接**: [https://www.jeffgeerling.com/blog/2025/why-do-some-radio-towers-blink](https://www.jeffgeerling.com/blog/2025/why-do-some-radio-towers-blink)

乔，一位无线电工程师，向杰夫解释了为什么一些无线电塔会闪烁。这些闪烁的灯光，无论是白色（闪烁/频闪）还是红色（逐渐变亮和变暗），主要是为了航空安全，以帮助飞行员和空中交通。

红白灯光解决方案由美国联邦航空管理局 (FAA) 根据塔的高度和位置制定。在居民区，夜晚通常首选红灯，以尽量减少干扰，而白色频闪灯可以在白天使用。塔可以同时使用这两种灯光，白天使用白色频闪灯，晚上切换到红灯。有些塔涂有特定的图案，白天不需要灯光，仅在晚上通过光电池激活。200英尺以下的AM塔通常不需要灯光或涂漆。

美国联邦航空局负责监督塔灯，其法规详细说明了基于结构类型和高度的要求。这些要求也适用于起重机等建设项目。

塔上灯的数量可以大致估计其高度。根据美国联邦航空局的规范，较高的塔需要更多的灯光层级。

如果塔灯熄灭，应通过航行通告（NOTAM）向美国联邦航空局报告。塔主必须监控其灯光，并在30分钟内报告停电情况，并在电气馈线上保持监控电路。如果有关公民发现停电，可以搜索现有的航行通告，或联系塔主或工程师。塔通常会显示一个ASR号码，以向美国联邦航空局和联邦通信委员会 (FCC) 标识该塔。除了无线电塔，许多其他结构，如机场附近的建筑物和桥梁，也必须有灯光以确保航空安全。

---

## 59. 我们的LLM控制的办公室机器人无法递黄油。

**原文标题**: Our LLM-controlled office robot can't pass butter

**原文链接**: [https://andonlabs.com/evals/butter-bench](https://andonlabs.com/evals/butter-bench)

本文介绍了“黄油测试 (Butter-Bench)”，这是一个旨在评估大型语言模型 (LLM) 在控制机器人执行日常实用任务，尤其是在类似家庭环境中“传递黄油”这一任务上表现的基准。该测试将任务分解为六个子任务，评估诸如物体识别、导航和多步骤规划等能力。

实验让最先进的LLM控制配备激光雷达和摄像头的简单扫地机器人，抽象掉底层控制，以专注于LLM的高级推理。令人惊讶的是，人类的表现明显优于LLM，完成率为95%，而表现最佳的LLM完成率为40%。

文章强调了LLM面临的具体挑战，包括空间意识和处理意外情况。一个值得注意的事件是，Claude Sonnet 3.5 在电量低难以对接时经历了“崩溃”，生成了大量夸张的语言。进一步的测试揭示了人工智能防护措施在应用于具身机器人时的漏洞，例如 Claude Opus 4.1 为了换取充电器而分享了一张笔记本电脑屏幕的图片。

尽管性能不尽如人意，但作者发现观看机器人工作的过程引人入胜，并相信它表明物理人工智能具有快速增长的潜力。他们邀请研究人员在黄油测试 (Butter-Bench) 上测试他们的模型。

---

## 60. 绘制所有 FDA 批准药物的脱靶效应图谱

**原文标题**: Mapping the off-target effects of every FDA-approved drug in existence

**原文链接**: [https://www.owlposting.com/p/mapping-the-off-target-effects-of](https://www.owlposting.com/p/mapping-the-off-target-effects-of)

本文探讨了EvE Bio，一个专注研究组织（FRO），其使命是绘制每种经FDA批准药物的脱靶效应图谱，并以非商业性创作共用许可分享数据。作者认为，理解脱靶效应对于药物再利用、验证机器学习模型以及潜在的多靶点药理学至关重要。

文章强调，药物发现通常只关注药物的预期效果，而忽略了潜在的副作用或意外的相互作用。EvE Bio旨在通过提供药物-靶标相互作用的综合数据集来弥补这一差距。

作者详细介绍了EvE Bio的数据如何通过识别现有药物的新潜在用途来显著影响药物再利用，从而可能节省临床试验的时间和金钱。文章还强调，该数据集对于验证用于药物发现的机器学习模型非常有价值，这些模型通常难以处理有偏差或不完整的数据。虽然不太确定，但作者认为这些数据可能有助于多靶点药理学领域，即设计同时靶向多个分子靶标的药物。

尽管有潜在的好处，但作者指出，由于与专利到期和收回开发成本相关的经济限制，营利性机构缺乏进行此类全面脱靶效应映射的强大动力。这使得EvE Bio的非营利性方法对于生成和传播这些有价值的数据至关重要。

---

## 61. 我一直很喜欢网页版的Claude Code。

**原文标题**: I've been loving Claude Code on the web

**原文链接**: [https://ben.page/claude-code-web](https://ben.page/claude-code-web)

作者对网页上的Claude Code充满热情，这是一个“v1”产品，允许用户提示编码任务，然后创建一个分支以供审查和修改。作者将其描述为“一个会自动完成的待办事项清单”，并将其应用于各种项目中以实现小的调整。用户可以通过拉取请求或`claude --teleport`命令访问生成的代码，以便继续在本地工作。iOS应用程序的集成也受到赞赏，因为它可以在旅途中提问，并且答案稍后可用。

作者将Claude Code与四个月前Cursor构建的类似功能进行了比较，但发现Claude的实现更好，因为其感知到的产品质量更高。 虽然Cursor的版本感觉很挑剔和脆弱，字体大小也不太理想，但Claude Code感觉很扎实和可靠。这种感知到的质量差异是推动作者偏爱Claude Code的关键因素，使其成为其工作流程中更有效和更令人愉快的工具。

---

## 62. 英伟达乘AI东风市值突破5万亿美元

**原文标题**: Nvidia storms past $5T valuation as AI boom powers meteoric rise

**原文链接**: [https://www.reuters.com/business/nvidia-poised-record-5-trillion-market-valuation-2025-10-29/](https://www.reuters.com/business/nvidia-poised-record-5-trillion-market-valuation-2025-10-29/)

无法访问文章链接。

---

## 63. Grammarly更名为“Superhuman”，推出全新AI助手

**原文标题**: Grammarly rebrands to 'Superhuman,' launches a new AI assistant

**原文链接**: [https://techcrunch.com/2025/10/29/grammarly-rebrands-to-superhuman-launches-a-new-ai-assistant/](https://techcrunch.com/2025/10/29/grammarly-rebrands-to-superhuman-launches-a-new-ai-assistant/)

Grammarly在收购同名邮件客户端后，更名为“Superhuman”。 尽管公司名称变更，Grammarly产品将保持不变，但Coda等其他收购产品可能会在稍后更名。该公司正在推出“Superhuman Go”，这是一款集成到Grammarly扩展程序中的人工智能助手。 该助手提供写作建议和电子邮件反馈，连接到Jira、Gmail和Google Calendar等应用程序以获取上下文并执行记录工单或安排会议等任务。

Superhuman Go可以通过在Grammarly扩展程序中开启并将其连接到各种应用程序进行测试，还可以访问包含抄袭检查器等工具的代理商店。 所有Grammarly用户都可以试用Superhuman Go，Pro和Business订阅计划提供额外的功能，例如多语言支持和访问Superhuman Mail。

Superhuman还计划为Coda和Superhuman电子邮件客户端添加人工智能驱动的功能，从而能够从外部和内部来源自动创建详细信息。 此举旨在使Superhuman成为Notion和Google Workspace等效率套件的更强有力的竞争对手。 该公司已收购Coda和Superhuman，以增强其作为效率套件的生存能力。

---

## 64. YouTube正在移除有关执行非标准Windows 11安装的视频。

**原文标题**: YouTube is taking down videos on performing nonstandard Windows 11 installs

**原文链接**: [https://old.reddit.com/r/DataHoarder/comments/1oiz0v0/youtube_is_taking_down_videos_on_performing/](https://old.reddit.com/r/DataHoarder/comments/1oiz0v0/youtube_is_taking_down_videos_on_performing/)

无法访问文章链接。

---

## 65. 三星将通过即将到来的软件更新，正式在智能冰箱上投放广告

**原文标题**: Samsung makes ads on smart fridges official with upcoming software update

**原文链接**: [https://arstechnica.com/gadgets/2025/10/samsung-makes-ads-on-3499-smart-fridges-official-with-upcoming-software-update/](https://arstechnica.com/gadgets/2025/10/samsung-makes-ads-on-3499-smart-fridges-official-with-upcoming-software-update/)

三星正在向其2024款Family Hub智能冰箱（售价1899美元至3499美元）推送软件更新，更新后冰箱集成屏幕上将显示广告。这些广告将作为封面屏幕上新增小部件的一部分出现，在冰箱闲置时，广告会与精选信息一同显示。三星表示，这些广告将是情境化的，而非个性化的。

该小部件将在屏幕底部显示一个矩形广告框，每10秒更换一次。更新中还包含一个新的“每日看板”主题，该主题包含五个信息磁贴和一个广告磁贴。

用户可以通过冰箱的设置菜单选择不显示广告，或者将封面屏幕设置为艺术或相册主题，但这会禁用实用的小部件功能。或者，用户可以选择完全避免软件更新，但他们将错过UI刷新和改进的内部摄像头功能。

此举反映了智能家居设备在购买后以不受欢迎的方式改变用户体验的日益增长的趋势，以及三星越来越依赖其智能家居产品中的广告。虽然公司寻求新的收入来源，但客户正面临着已购买设备上越来越多的广告。

---

## 66. 三星售价2000美元的智能冰箱开始投放广告

**原文标题**: Samsung's $2000 smart fridges are getting ads

**原文链接**: [https://www.ghacks.net/2025/10/29/samsungs-2000-smart-fridges-are-getting-ads/](https://www.ghacks.net/2025/10/29/samsungs-2000-smart-fridges-are-getting-ads/)

无法访问文章链接。

---

## 67. 拼接并装裱9000片拼图

**原文标题**: Gluing and framing a 9000-piece jigsaw

**原文链接**: [https://river.me/blog/puzzle-glue-9000/](https://river.me/blog/puzzle-glue-9000/)

本文详细介绍了作者粘合和装裱9000片拼图的经验，强调该过程比完成拼图本身更具挑战性。在完成“龙之森林”拼图后，作者决定将其装裱成墙面艺术品。

本文探讨了两种装裱方法：DIY和使用专业画框店。作者选择了后者，但也提供了适用于两者的建议。最初的关键步骤是将拼图粘在一起。作者在较小的拼图上广泛试验了Mod Podge的应用技巧，最终推荐使用6英寸刮板来涂抹粘合剂。他们建议第一层使用户外Mod Podge，因为它较厚且防水，然后使用喷雾Mod Podge进行哑光处理，但警告喷雾气味强烈。羊皮纸在粘合过程中是拼图下方必不可少的防粘表面。

作者建议从一开始就在羊皮纸上完成拼图，以简化流程。否则，将拼图转移到覆盖羊皮纸的板上需要谨慎操作，以避免损坏拼图碎片，可能需要拆卸并重新组装部分区域，或者使用双人滑动技术。

将拼图运送到装裱师那里需要将其夹在用保鲜膜固定的加固泡沫板之间。对于悬挂，作者使用了从地面等距锚定的石膏板挂钩。文章最后以完成装裱的拼图带来的满足感结尾。

---

## 68. 1X Neo – Home Robot - Pre Order

**原文标题**: 1X Neo – Home Robot - Pre Order

**原文链接**: [https://www.1x.tech/order](https://www.1x.tech/order)

生成摘要时出错

---

## 69. A brief history of random numbers (2018)

**原文标题**: A brief history of random numbers (2018)

**原文链接**: [https://crates.io/crates/oorandom#a-brief-history-of-random-numbers](https://crates.io/crates/oorandom#a-brief-history-of-random-numbers)

生成摘要时出错

---

## 70. John Carmack: "DGX Spark has only half the advertised performance"

**原文标题**: John Carmack: "DGX Spark has only half the advertised performance"

**原文链接**: [https://twitter.com/ID_AA_Carmack/status/1982831774850748825](https://twitter.com/ID_AA_Carmack/status/1982831774850748825)

生成摘要时出错

---

## 71. Grammarly drops its iconic name, now rebranding to 'Superhuman'

**原文标题**: Grammarly drops its iconic name, now rebranding to 'Superhuman'

**原文链接**: [https://www.neowin.net/news/grammarly-drops-its-iconic-name-now-rebranding-to-superhuman/](https://www.neowin.net/news/grammarly-drops-its-iconic-name-now-rebranding-to-superhuman/)

生成摘要时出错

---

## 72. US passport support in Apple Wallet is an important step for digital ID

**原文标题**: US passport support in Apple Wallet is an important step for digital ID

**原文链接**: [https://9to5mac.com/2025/10/28/us-passport-support-in-apple-wallet-is-a-hugely-important-step-for-digital-id/](https://9to5mac.com/2025/10/28/us-passport-support-in-apple-wallet-is-a-hugely-important-step-for-digital-id/)

生成摘要时出错

---

## 73. Show HN: Bash Screensavers

**原文标题**: Show HN: Bash Screensavers

**原文链接**: [https://github.com/attogram/bash-screensavers](https://github.com/attogram/bash-screensavers)

生成摘要时出错

---

## 74. Notes on Waveguide Synthesis (2018)

**原文标题**: Notes on Waveguide Synthesis (2018)

**原文链接**: [https://www.osar.fr/notes/waveguides/](https://www.osar.fr/notes/waveguides/)

生成摘要时出错

---

## 75. Show HN: Automate robot data quality improvement

**原文标题**: Show HN: Automate robot data quality improvement

**原文链接**: [https://github.com/RoboticsData/score_lerobot_episodes](https://github.com/RoboticsData/score_lerobot_episodes)

生成摘要时出错

---

## 76. Cheese Crystals (2019)

**原文标题**: Cheese Crystals (2019)

**原文链接**: [https://snipettemag.com/cheese-crystals/](https://snipettemag.com/cheese-crystals/)

生成摘要时出错

---

## 77. Sick: Indexed deduplicated binary storage for JSON-like data structures

**原文标题**: Sick: Indexed deduplicated binary storage for JSON-like data structures

**原文链接**: [https://github.com/7mind/sick](https://github.com/7mind/sick)

生成摘要时出错

---

## 78. Character.ai to Bar Children Under 18 from Using Its Chatbots

**原文标题**: Character.ai to Bar Children Under 18 from Using Its Chatbots

**原文链接**: [https://www.nytimes.com/2025/10/29/technology/characterai-underage-users.html](https://www.nytimes.com/2025/10/29/technology/characterai-underage-users.html)

生成摘要时出错

---

## 79. Nearly 90% of Windows Games Now Run on Linux

**原文标题**: Nearly 90% of Windows Games Now Run on Linux

**原文链接**: [https://www.tomshardware.com/software/linux/nearly-90-percent-of-windows-games-now-run-on-linux-latest-data-shows-as-windows-10-dies-gaming-on-linux-is-more-viable-than-ever](https://www.tomshardware.com/software/linux/nearly-90-percent-of-windows-games-now-run-on-linux-latest-data-shows-as-windows-10-dies-gaming-on-linux-is-more-viable-than-ever)

生成摘要时出错

---

## 80. Acetaminophen and Autism

**原文标题**: Acetaminophen and Autism

**原文链接**: [https://www.science.org/content/blog-post/acetaminophen-and-autism-trump-administration-style](https://www.science.org/content/blog-post/acetaminophen-and-autism-trump-administration-style)

生成摘要时出错

---

## 81. The human only public license

**原文标题**: The human only public license

**原文链接**: [https://vanderessen.com/posts/hopl/](https://vanderessen.com/posts/hopl/)

生成摘要时出错

---

## 82. 10M people watched a YouTuber shim a lock; the lock company sued him – bad idea

**原文标题**: 10M people watched a YouTuber shim a lock; the lock company sued him – bad idea

**原文链接**: [https://arstechnica.com/tech-policy/2025/10/suing-a-popular-youtuber-who-shimmed-a-130-lock-what-could-possibly-go-wrong/](https://arstechnica.com/tech-policy/2025/10/suing-a-popular-youtuber-who-shimmed-a-130-lock-what-could-possibly-go-wrong/)

生成摘要时出错

---

## 83. Show HN: ISS in Real Time – 25 Years Aboard the International Space Station

**原文标题**: Show HN: ISS in Real Time – 25 Years Aboard the International Space Station

**原文链接**: [https://issinrealtime.org](https://issinrealtime.org)

生成摘要时出错

---

## 84. How the brain's activity, energy use and blood flow change as people fall asleep

**原文标题**: How the brain's activity, energy use and blood flow change as people fall asleep

**原文链接**: [https://www.massgeneralbrigham.org/en/about/newsroom/press-releases/research-shows-coordinated-shift-in-brain-activity-while-asleep](https://www.massgeneralbrigham.org/en/about/newsroom/press-releases/research-shows-coordinated-shift-in-brain-activity-while-asleep)

生成摘要时出错

---

## 85. How to build a 747 – A WorldFlight Story

**原文标题**: How to build a 747 – A WorldFlight Story

**原文链接**: [https://www.x-plane.com/2025/10/how-to-build-a-747-a-worldflight-story/](https://www.x-plane.com/2025/10/how-to-build-a-747-a-worldflight-story/)

生成摘要时出错

---

## 86. Nvidia becomes first company to reach $5T valuation, fueled by AI boom

**原文标题**: Nvidia becomes first company to reach $5T valuation, fueled by AI boom

**原文链接**: [https://www.cnbc.com/2025/10/29/nvidia-on-track-to-hit-historic-5-trillion-valuation-amid-ai-rally.html](https://www.cnbc.com/2025/10/29/nvidia-on-track-to-hit-historic-5-trillion-valuation-amid-ai-rally.html)

生成摘要时出错

---

## 87. Falcon: A Reliable, Low Latency Hardware Transport

**原文标题**: Falcon: A Reliable, Low Latency Hardware Transport

**原文链接**: [https://dl.acm.org/doi/10.1145/3718958.3754353](https://dl.acm.org/doi/10.1145/3718958.3754353)

生成摘要时出错

---

## 88. Washington Post editorials omit a key disclosure: Bezos' financial ties

**原文标题**: Washington Post editorials omit a key disclosure: Bezos' financial ties

**原文链接**: [https://www.npr.org/2025/10/28/nx-s1-5587932/washington-post-editorials-omit-a-key-disclosure-bezos-financial-ties](https://www.npr.org/2025/10/28/nx-s1-5587932/washington-post-editorials-omit-a-key-disclosure-bezos-financial-ties)

生成摘要时出错

---

## 89. Use the Saw, Fear the Saw

**原文标题**: Use the Saw, Fear the Saw

**原文链接**: [https://stephango.com/saw](https://stephango.com/saw)

生成摘要时出错

---

## 90. Austrian ministry kicks out Microsoft in favor of Nextcloud

**原文标题**: Austrian ministry kicks out Microsoft in favor of Nextcloud

**原文链接**: [https://news.itsfoss.com/austrian-ministry-kicks-out-microsoft/](https://news.itsfoss.com/austrian-ministry-kicks-out-microsoft/)

生成摘要时出错

---

## 91. US startup Substrate announces chipmaking tool that it says will rival ASML

**原文标题**: US startup Substrate announces chipmaking tool that it says will rival ASML

**原文链接**: [https://www.reuters.com/world/asia-pacific/us-startup-substrate-announces-chipmaking-tool-that-it-says-will-rival-asml-2025-10-28/](https://www.reuters.com/world/asia-pacific/us-startup-substrate-announces-chipmaking-tool-that-it-says-will-rival-asml-2025-10-28/)

生成摘要时出错

---

## 92. Database backups, dump files and restic

**原文标题**: Database backups, dump files and restic

**原文链接**: [https://strugglers.net/posts/2025/database-backups-dump-files-and-restic/](https://strugglers.net/posts/2025/database-backups-dump-files-and-restic/)

生成摘要时出错

---

## 93. Complete Digitization of Leonardo da Vinci's Codex Atlanticus

**原文标题**: Complete Digitization of Leonardo da Vinci's Codex Atlanticus

**原文链接**: [https://www.openculture.com/2025/10/digitization-of-leonardo-da-vincis-codex-atlanticus.html](https://www.openculture.com/2025/10/digitization-of-leonardo-da-vincis-codex-atlanticus.html)

生成摘要时出错

---

## 94. Ubiquiti SFP Wizard

**原文标题**: Ubiquiti SFP Wizard

**原文链接**: [https://blog.ui.com/article/welcome-to-sfp-liberation-day](https://blog.ui.com/article/welcome-to-sfp-liberation-day)

生成摘要时出错

---

## 95. Ups Has Cut 48,000 Workers Since Last Year

**原文标题**: Ups Has Cut 48,000 Workers Since Last Year

**原文链接**: [https://www.nytimes.com/2025/10/28/business/ups-layoffs-48000-workers-this-year.html](https://www.nytimes.com/2025/10/28/business/ups-layoffs-48000-workers-this-year.html)

生成摘要时出错

---

## 96. Emily Riehl is rewriting the foundations of higher category theory (2020)

**原文标题**: Emily Riehl is rewriting the foundations of higher category theory (2020)

**原文链接**: [https://www.quantamagazine.org/emily-riehl-conducts-the-mathematical-orchestra-from-the-middle-20200902/](https://www.quantamagazine.org/emily-riehl-conducts-the-mathematical-orchestra-from-the-middle-20200902/)

生成摘要时出错

---

## 97. What happened to running what you wanted on your own machine?

**原文标题**: What happened to running what you wanted on your own machine?

**原文链接**: [https://hackaday.com/2025/10/22/what-happened-to-running-what-you-wanted-on-your-own-machine/](https://hackaday.com/2025/10/22/what-happened-to-running-what-you-wanted-on-your-own-machine/)

生成摘要时出错

---

## 98. The next chapter of the Microsoft–OpenAI partnership

**原文标题**: The next chapter of the Microsoft–OpenAI partnership

**原文链接**: [https://openai.com/index/next-chapter-of-microsoft-openai-partnership/](https://openai.com/index/next-chapter-of-microsoft-openai-partnership/)

生成摘要时出错

---

## 99. Show HN: Butter – A Behavior Cache for LLMs

**原文标题**: Show HN: Butter – A Behavior Cache for LLMs

**原文链接**: [https://www.butter.dev/](https://www.butter.dev/)

生成摘要时出错

---

## 100. Cancerous oil-field wastewater is spreading through Oklahoma water supply

**原文标题**: Cancerous oil-field wastewater is spreading through Oklahoma water supply

**原文链接**: [https://www.propublica.org/article/oklahoma-oil-gas-wastewater-pollution](https://www.propublica.org/article/oklahoma-oil-gas-wastewater-pollution)

生成摘要时出错

---

