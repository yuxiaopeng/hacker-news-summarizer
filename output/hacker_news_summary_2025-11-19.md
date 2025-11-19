# Hacker News 热门文章摘要 (2025-11-19)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 针对Cloudflare的问题

**原文标题**: Questions for Cloudflare

**原文链接**: [https://entropicthoughts.com/questions-for-cloudflare](https://entropicthoughts.com/questions-for-cloudflare)

本文分析了 Cloudflare 近期发生的故障，重点关注其系统设计中反馈机制的缺失。尽管 Cloudflare 在故障后的分析中强调了控制问题，但作者认为根本原因是未能理解系统状态。最初的协议不匹配和延迟解决源于缺乏可见性，而非缺乏控制。

作者提出了与 Cloudflare 运维界面和对系统行为的理解相关的关键问题。具体来说，他们问道：Cloudflare 是否刻意设计运维界面？Cloudflare 是否积极考虑运维人员如何更好地理解系统的功能和故障？作者认为 Cloudflare 的博客文章暗示答案是“否”。

文章随后深入探讨了涉及 Cloudflare 机器人管理系统的具体场景，质疑其如何处理超时、系统内已消失的请求以及未运行的情况。此外，作者还探究了 Cloudflare 如何管理内部协议合规性，运维人员如何收到有关过期功能文件的警报，以及功能文件生成器是否收到关于其输出质量的反馈。

最后，作者询问了运维人员重新配置请求流程的流程以及他们用于做出这些决策的信息。他们还质疑了可观察性工具的有效性，并强调了事件期间误导性信息的问题。最终，作者对技术组织事故调查的彻底性不足表示失望。

---

## 2. 表情符号证据错误并未撤销谋杀罪定罪——人民诉哈蒙案

**原文标题**: Emoji Evidence Errors Don't Undo a Murder Conviction–People vs. Harmon

**原文链接**: [https://blog.ericgoldman.org/archives/2025/11/emoji-evidence-errors-dont-undo-a-murder-conviction-people-v-harmon.htm](https://blog.ericgoldman.org/archives/2025/11/emoji-evidence-errors-dont-undo-a-murder-conviction-people-v-harmon.htm)

本文讨论了“人民诉哈蒙案”，其中尽管表情符号证据的呈现方式存在错误，德拉罗萨的谋杀定罪仍被维持。德拉罗萨提出上诉，认为作为证据引入的一条Facebook消息（包含指示他拥有一把枪的表情符号）应该被排除在外。

问题的出现是因为执法调查员对表情符号的描述（“笑脸表情符号和一个魔鬼角表情符号”）含糊不清，因为喜极而泣的表情符号与普通的笑脸表情符号具有不同的含义。作者认为以视觉方式描绘表情符号会更有帮助。

然而，关键的错误发生在德拉罗萨的审前动议中，该动议旨在排除这条消息。作为证据提交的打印件包含的是矩形而不是实际的表情符号，未能充分告知法官这些表情符号对陪审团的潜在影响（特别是暗示了一种“对枪支暴力的轻率态度”）。上诉法院裁定，审判法官不应因驳回该动议而受到指责，因为提交的证据不完整。

作者表示担心德拉罗萨实际上在没有适当的审前挑战的情况下暴露于具有偏见性的证据（带有表情符号的消息）。虽然承认处理大量证据的困难，但作者强调了律师在法庭上准确呈现表情符号证据的重要性。表情符号的正确描绘可能需要了解它们在发送者和接收者眼中是如何显示的，可能涉及重现历史技术环境。然而，该判决既没有显示表情符号，也没有显示矩形替代物。

---

## 3. 发布HN：Mosaic (YC W25) – 代理式视频编辑

**原文标题**: Launch HN: Mosaic (YC W25) – Agentic Video Editing

**原文链接**: [https://mosaic.so](https://mosaic.so)

Mosaic推出代理型AI视频编辑平台

---

## 4. 使用 .NET 为 Commodore 64 编程

**原文标题**: Programming the Commodore 64 with .NET

**原文链接**: [https://retroc64.github.io/](https://retroc64.github.io/)

RetroC64将Commodore 64编程带入现代.NET生态系统。它允许开发者直接在其IDE中构建、汇编、运行和调试C64程序，消除了传统复古开发的阻碍。

主要特性包括：

*   **零阻力开发：** 从.NET轻松生成PRG/D64文件并在VICE模拟器中自动启动代码。
*   **流畅的汇编器 (Asm6502)：** 具有标签、节、数据块、助手和C#的源映射。
*   **精灵工具：** 自动将Skia绘图转换为C64兼容的精灵字节。
*   **SID工具：** 加载、重定位和播放SID音乐，包括目标地址和零页范围配置。
*   **核心助手：** 提供带有零页分配的C64Assembler、光栅IRQ设置、精灵类和PRG/D64镜像文件支持，以实现快速原型设计。
*   **调试：** 与VS Code集成以调试C64代码，包括寄存器/内存/VIC/SID寄存器检查、断点、执行控制和反汇编视图。

本质上，RetroC64提供了一套工具和库来简化C64开发过程，使其对于.NET开发者来说更易于访问和高效。来自.NET Conf 2025的演示展示了其功能。

---

## 5. 你的智能手机，他们的规则：应用商店助长企业-政府审查

**原文标题**: Your Smartphone, Their Rules: App Stores Enable Corporate-Government Censorship

**原文链接**: [https://www.aclu.org/news/free-speech/app-store-oligopoly](https://www.aclu.org/news/free-speech/app-store-oligopoly)

美国公民自由联盟的这篇文章认为，苹果应用商店和谷歌应用商店的垄断地位为审查制度创造了一个危险的环境，因为这些平台可能会受到政府的压力，移除表达异议或批评政府行为的应用。 文章重点提到了ICEBlock和Red Dot等应用的移除，这些应用允许用户报告移民及海关执法局特工的踪迹，作为这种审查制度的例子。

虽然苹果的iOS系统只允许从其应用商店下载应用，使其特别容易受到审查，但谷歌的安卓系统传统上更开放“侧载”，但随着其新的“验证开发者”要求，也变得越来越严格。 这一变化可能使政府能够向谷歌施压，将开发者视为“不良行为者”，从而有效地切断他们的应用。

文章将这种情况与欧盟进行了对比，在欧盟，数字市场法案已迫使苹果允许替代应用商店和侧载。 它还指出，虽然应用商店声称可以提高安全性，但它们通常允许使用监控工具的应用，并且本身就是监控平台。

作者倡导用户选择、开放标准和监管干预，以打破对软件的寡头垄断控制。 他们建议使用Accrescent和F-Droid等替代应用商店，这些应用商店优先考虑隐私和安全，并敦促读者支持自由软件并要求使用开放标准的工具。 文章总结说，用户随身携带的设备应该由他们自己控制，而不是由滥用权力的政府或公司控制。

---

## 6. 升级Proxmox历险记

**原文标题**: Adventures in Upgrading Proxmox

**原文链接**: [https://blog.vasi.li/adventures-in-upgrading-proxmox/](https://blog.vasi.li/adventures-in-upgrading-proxmox/)

The author recounts their experience upgrading a Proxmox cluster from version 8 to 9, focusing on the challenges encountered on a node running an NVR with a Coral TPU. The initial motivation for the upgrade was to resolve an AppArmor issue affecting Docker containers running inside LXC containers, impacting the deployment of Coolify and Dokploy.

While one node upgraded smoothly, the second node, crucial for the NVR, failed after the upgrade. This was due to the Apex TPU drivers, installed as a DKMS module, failing to rebuild for the new kernel, resulting in a non-booting system. The author was able to boot using a previous kernel, but the new kernel consistently kernel panicked with "unable to mount rootfs on unknown-block(0,0)".

After troubleshooting, the author resolved the boot issue by using `proxmox-boot-tool init` to properly initialize the EFI partition, following a Reddit thread suggestion. This allowed the system to boot with the upgraded kernel.

However, the upgrade also broke the Apex TPU drivers, requiring a source code patch to address API changes in the new kernel. The author found a relevant patch online, applied it, rebuilt the driver, and successfully restored functionality to the NVR system, including the Frigate application.


---

## 7. 价值一千美元的AWS错误

**原文标题**: The $1k AWS Mistake

**原文链接**: [https://www.geocod.io/code-and-coordinates/2025-11-18-the-1000-aws-mistake/](https://www.geocod.io/code-and-coordinates/2025-11-18-the-1000-aws-mistake/)

Mathias Hansen讲述了一起因意外的NAT网关数据传输费用导致的价值1000美元的AWS错误，该错误源于从其ETL平台(Hetzner)向S3移动数据。 尽管确认了同一区域内的EC2到S3的免费传输以及 *进入* S3的免费传输，但默认的VPC设置仍会将S3流量通过NAT网关路由，从而产生每GB 0.045美元的费用。 罪魁祸首通过AWS成本异常检测被识别出来，突显了其重要性。

解决方案是使用S3的VPC网关端点，该端点创建了从VPC到S3的直接免费路由，绕过了NAT网关。 使用Terraform实现这一点非常简单。

关键的启示是AWS网络的欺骗性复杂性以及验证假设的必要性。 即使传输费用看起来是免费的，内部路由也可能导致意外费用。 本文强调了在使用NAT网关时使用S3和DynamoDB的VPC端点的重要性，启用AWS成本异常检测以及在扩展之前使用小型数据集进行测试。 作者强调，即使是经验丰富的AWS用户也可能遇到此类问题。 文章最后建议审核VPC端点配置以避免类似问题，并提供了相关资源的链接。

---

## 8. 开源项目中权力的和平转移

**原文标题**: The Peaceful Transfer of Power in Open Source Projects

**原文链接**: [https://shkspr.mobi/blog/2025/11/the-peaceful-transfer-of-power-in-open-source-projects/](https://shkspr.mobi/blog/2025/11/the-peaceful-transfer-of-power-in-open-source-projects/)

本文强调了为开源项目规划领导层继任的重要性，并将历史王国与开源软件中常见的“终身仁慈独裁者”（BDFL）治理模式进行了类比。作者认为，BDFL模式虽然初期有效，但如果“独裁者”变得专横或丧失能力，可能会导致项目不稳定。

作者将BDFL的负面例子与Mastodon项目最近在领导层过渡方面的积极做法进行了对比。Mastodon的首席执行官Eugen Rochko公开承认领导层面临的压力以及他可能成为限制因素的潜力，这表明他采取了一种成熟和无私的方式来确保项目的持续发展。

本文批评了一些创始人的以自我为中心的行为，并呼吁开源项目领导者采取类似于民主治理的做法，强调共同责任、透明度和权力平稳交接的重要性。它尤其敦促大型项目制定继任计划，以防止项目在创始人离开或倒台后崩溃。中心信息是呼吁项目领导者以成熟和积极的态度行事，确保项目的长期健康和稳定，而不是紧抓权力不放，并可能危及其未来。

---

## 9. 双子星3号

**原文标题**: Gemini 3

**原文链接**: [https://blog.google/products/gemini/gemini-3/](https://blog.google/products/gemini/gemini-3/)

Gemini 3：谷歌最新最智能的AI模型，发布以增强推理和多模态能力。它可在谷歌产品（如 Gemini 应用、AI Studio、Vertex AI 以及搜索中的 AI 模式）中使用，Ultra 订阅用户即将迎来“深度思考”模式。

Gemini 3 Pro 在推理、多模态和编码基准测试中优于之前的模型，登顶 LMArena 排行榜，并在各种 AI 基准测试中取得领先成绩，擅长解决科学和数学领域的难题。“深度思考”模式将进一步增强 Gemini 3 解决复杂问题的能力。

Gemini 3 的多模态推理能力和 100 万 token 上下文窗口使用户能够有效地学习，从文本、图像、视频、音频和代码中综合信息。 Gemini 3 可以翻译食谱、分析学术论文并提供专家级别的体育分析。搜索中的 AI 模式利用 Gemini 3 实现沉浸式视觉布局和交互式工具。

对于开发者而言，Gemini 3 在零样本生成方面表现出色，并在代理编码方面表现出色，在编码基准测试中优于之前的模型。开发者可以在 Google AI Studio、Vertex AI、Gemini CLI、Google Antigravity 和第三方平台上使用 Gemini 3 进行构建。Google Antigravity 是一个新的代理开发平台，它利用 Gemini 3 的推理和工具使用来转变 AI 辅助。 Gemini 3 表现出改进的长期规划能力，使用户能够管理复杂的工作流程。 Gemini 应用中的 Gemini Agent 可帮助 Google AI Ultra 订阅用户整理他们的 Gmail 收件箱。

谷歌强调 Gemini 3 是其最安全的模型，已接受广泛的安全评估。 Gemini 3 正在各个平台上推出，Gemini 3 系列还将推出更多模型。

---

## 10. 我做了一个检测器，用来检测down检测器。

**原文标题**: I made a down detector for down detector

**原文链接**: [https://downdetectorsdowndetector.com](https://downdetectorsdowndetector.com)

用户尝试为Down Detector创建“Down Detector”的幽默描述

---

## 11. 用于思考感知的编辑和生成的多模态扩散语言模型

**原文标题**: Multimodal Diffusion Language Models for Thinking-Aware Editing and Generation

**原文链接**: [https://github.com/tyfeld/MMaDA-Parallel](https://github.com/tyfeld/MMaDA-Parallel)

本文介绍了MMaDA-Parallel，一种新颖的并行多模态扩散框架，旨在改进思考感知图像编辑和生成。作者发现现有顺序方法存在一个问题：误差传播会降低性能，尤其是在生成的推理和最终图像不对齐时。为了分析这一点，他们创建了ParaBench，一个用于评估文本和图像输出的基准。

MMaDA-Parallel通过在整个去噪过程中实现文本和图像之间的连续双向交互来解决对齐问题。该模型使用监督微调进行训练，并使用并行强化学习（ParaRL）进一步优化，该方法沿去噪轨迹应用语义奖励，以加强跨模态一致性。

实验表明，MMaDA-Parallel显著提高了跨模态对齐和语义一致性，与现有最先进方法相比，在ParaBench上的输出对齐度提高了6.9%。作者已发布其代码和模型（MMaDA-Parallel-A和MMaDA-Parallel-M，区别在于分词器），供社区使用。提供了一个快速入门指南，并警告说当前模型最适合合成环境，并且可能无法在真实世界图像上达到最佳性能。作者计划扩展他们的训练数据并进一步改进他们的模型。

---

## 12. 澳大利亚一紧急呼叫失败事故疑与过时三星手机有关

**原文标题**: Outdated Samsung handset linked to fatal emergency call failure in Australia

**原文链接**: [https://www.theregister.com/2025/11/18/samsung_emergency_call_failure/](https://www.theregister.com/2025/11/18/samsung_emergency_call_failure/)

悉尼居民因三星旧手机无法拨打澳大利亚紧急号码000而死亡，引发了关于移动软件更新重要性的警告。该居民的运营商TPG Telecom已确认此事，强调其网络运行正常，并指出用户设备运行不兼容的软件。

三星已承认旧设备存在此问题，列出了许多需要更新或更换的型号，以确保紧急呼叫功能。TPG已联系受影响的三星型号用户，包括Galaxy S7和Note 5系列，敦促他们更新。澳大利亚法规规定，在警告期过后，将禁止未打补丁的手机接入网络。

TPG首席执行官Iñaki Berroeta强调了客户安全，并敦促用户立即更新或更换过时的设备。由于公众对紧急呼叫可靠性的担忧，该事件被公开。Telstra此前也曾警告过，较旧的、无法升级的三星设备可能会导致三重零呼叫失败。TPG已通知相关部门，并正在调查此事。

三星在后来的声明中表示慰问，并强调了保持设备更新以确保安全的重要性。他们表示，运营商已通知需要更新或更换设备的客户。此前，Optus的防火墙更新曾导致紧急呼叫失败，并与多起死亡事件有关，突显了可靠的紧急通信基础设施的至关重要性。

---

## 13. Thunderbird新增原生Microsoft Exchange邮件支持

**原文标题**: Thunderbird Adds Native Microsoft Exchange Email Support

**原文链接**: [https://blog.thunderbird.net/2025/11/thunderbird-adds-native-microsoft-exchange-email-support/](https://blog.thunderbird.net/2025/11/thunderbird-adds-native-microsoft-exchange-email-support/)

雷鸟145版本通过Exchange Web Services (EWS) 协议引入了对 Microsoft Exchange 电子邮件的原生支持，无需第三方插件。此更新简化了 Exchange 环境中用户的电子邮件功能，包括完整的文件夹列表、消息同步和附件处理。

设置过程简单直接，尤其是对于 Microsoft 365 或 Office 365 用户。雷鸟使用 Microsoft 的标准 OAuth2 登录方式，并自动检测帐户设置。用户可以在雷鸟中创建一个新帐户，选择“Exchange”，然后让应用程序处理其余操作。

目前，EWS 支持仅限于电子邮件功能。日历和地址簿集成正在开发中，将在未来版本中发布。虽然现在支持 EWS，但 Microsoft 正在过渡到 Microsoft Graph。雷鸟正在开发 Microsoft Graph 支持，以实现未来的兼容性。

本文以表格形式概述了支持和不支持的功能，涵盖帐户设置、消息操作、附件、搜索与过滤、帐户托管、日历支持、地址簿支持以及 Microsoft Graph 支持。

雷鸟的目标是成为 Exchange 用户的全面解决方案，日历和联系人同步已列入路线图。本文鼓励用户关注未来版本的更新，并指导组织管理员查阅 Mozilla wiki 了解更多信息。

---

## 14. 我只想用上能用的RCS消息。

**原文标题**: I just want working RCS messaging

**原文链接**: [https://wt.gd/i-just-want-my-rcs-messaging-to-work](https://wt.gd/i-just-want-my-rcs-messaging-to-work)

2025年11月，作者升级到iOS 26的iPhone 15 Pro后，RCS消息功能失效，对此感到沮丧。之前一切正常，而升级后已经花了一个多月进行故障排除，却面临Apple和运营商（主要是T-Mobile）之间的互相推诿。AppleCare+毫无帮助，作者认为Apple没有承担责任。

作者是一位操作系统无关的用户，拥有在Android上为运营商排除彩信故障的背景，怀疑问题可能源于Apple或Google的Google Jibe，该平台运行RCS基础设施。他们提到了过去因UAProf停用而在LineageOS上为Verizon修复彩信问题的经验。他们还提到Google过去曾有意阻止自定义Android ROM上的RCS。

在他们的iPhone上，T-Mobile和US Mobile两条线路都卡在“等待激活…”状态，但在其他iPhone上可以正常工作。作者进行了广泛的故障排除步骤，包括重置、网络设置调整、eSIM重新发放，甚至使用`idevicesyslog`分析设备日志。日志表明可能存在与T-Mobile的Jibe配置相关的“UserInteractionRequired.xml”问题。

作者批评Apple的客户支持将责任归咎于运营商，并拒绝在另一台设备上测试eSIM。尽管Google Jibe是后端RCS基础设施，但Apple从未提及。

Apple计划出于礼貌更换手机主板，作者认为这是一种临时修复，无法解决根本问题，尤其是AppleCare+提供的劣质客户服务。作者的目标是让Apple调查并解决所有用户的实际问题，而不仅仅是提供快速的临时解决方案。

---

## 15. 谷歌反重力

**原文标题**: Google Antigravity

**原文链接**: [https://antigravity.google/](https://antigravity.google/)

无法访问文章链接。

---

## 16. 编程的未来 (2013) [视频]

**原文标题**: The Future of Programming (2013) [video]

**原文链接**: [https://www.youtube.com/watch?v=8pTEmbeENF4](https://www.youtube.com/watch?v=8pTEmbeENF4)

提供的信息并非文章，而是YouTube上名为“编程的未来 (2013)”的视频。然而，列出的内容是标准的YouTube页脚信息，与视频的实际内容无关。因此，仅凭这些信息无法总结*实际*视频的内容。

我们只知道该视频位于YouTube上，其标题表明讨论的是2013年编程的发展方向。页脚提到标准的YouTube相关项目，例如：

*   版权
*   服务条款
*   隐私政策
*   联系方式
*   创作者资源
*   广告信息
*   新功能
*   NFL Sunday Ticket
*   Google LLC（版权）

在不知道视频实际讨论关于编程未来的内容的情况下，真正的摘要是不可能的。此分析仅描述与视频列表相关的元数据。

---

## 17. 学习从PXE启动

**原文标题**: Learning to Boot from PXE

**原文链接**: [https://blog.imraniqbal.org/learning-to-boot-from-pxe/](https://blog.imraniqbal.org/learning-to-boot-from-pxe/)

作者详细描述了在 USB 驱动器损坏后，如何在家庭网络上设置 PXE 网络引导，以便在新笔记本电脑上安装 NixOS 的经历。 由于苦于等待新的 USB 驱动器，他们决定利用笔记本电脑的 PXE 引导选项。

该过程包括在其 OPNsense 路由器上配置 DHCP，以提供 PXE 所需的信息，包括 TFTP 服务器地址和引导文件。 然后，他们通过 dnsmasq（通过 SSH 访问）启用了 TFTP，用于提供 iPXE 引导加载程序。 iPXE 旨在通过 HTTP 获取 NixOS ISO。

作者最初尝试使用 iPXE 的 `sanboot` 功能直接引导 ISO，但遇到 NixOS 无法找到 ISO 镜像的问题。 意识到这行不通后，他们转而使用 Nix 的 netboot 镜像生成器来创建必要的内核和 initrd 文件。 这些文件随后通过 lighttpd（OPNsense 的 Web 服务器）通过 HTTP 提供。 通过更新 iPXE 脚本以从 HTTP 服务器加载内核和 initrd，作者成功地通过网络引导了 NixOS。

作者回顾了他们在 OPNsense 设备上使用 FreeBSD 的意外积极体验，并表达了未来可能通过网络引导完整图形环境（KDE）的持续兴趣。

---

## 18. 自建还是购买：本周故障应该教会你什么

**原文标题**: Build vs. Buy: What This Week's Outages Should Teach You

**原文链接**: [https://www.toddhgardner.com/blog/build-vs-buy-outages](https://www.toddhgardner.com/blog/build-vs-buy-outages)

托德·加德纳的文章《自建还是购买：本周的故障应该教会你什么》以《侏罗纪公园》灾难性的定制软件为例，说明战略性地选择自建哪些功能以及从第三方供应商购买哪些功能的重要性。Cloudflare、GitHub 和 AWS 等主要基础设施提供商最近发生的故障突显了在不完全理解且无法控制的抽象概念之上构建业务的风险。

核心论点是，如果某项能力对你的业务核心功能至关重要并提供竞争优势，那么你应该拥有它并自行构建。然而，许多公司错误地专注于构建非必要工具，同时依赖外部供应商提供关键基础设施，导致失去控制并可能发生毁灭性故障。

虽然由于专业知识或经济原因，外包基础设施有时是必要的，但加德纳警告不要采用过于复杂、不透明的平台。他主张构建能传递你独特价值的功能，如果构建不可行，则购买更简单的基础设施解决方案。相反，他建议购买现成的解决方案，如分析、CRM、错误监控和 SSL 证书管理，因为这些都是非核心功能且已经解决的问题。

关键在于避免购买过于复杂的抽象概念，这些概念会阻碍你理解和解决问题。理想的方法是构建使你独特的功能，购买使你运行的功能，并始终保持足够的理解能力，以便在问题不可避免地发生时进行修复。

---

## 19. 重返創世紀七

**原文标题**: Ultima VII Revisited

**原文链接**: [https://github.com/ViridianGames/U7Revisited](https://github.com/ViridianGames/U7Revisited)

《重访创世纪七：黑石之门》是一个旨在为经典DOS游戏《创世纪七：黑石之门》创建替代引擎的项目。要运行它，用户需要将原始《创世纪七》游戏文件夹的内容复制到项目结构中的特定目录（`/Data/u7`）。

该文档详细介绍了开发者和最终用户的安装说明。对于开发者，它涵盖了使用Meson（跨平台）和CMake（Windows & Linux）构建项目，并为每个平台提供特定的命令和先决条件。

该文档还提供了游戏内控制列表，使用WASD进行移动，Q/E进行旋转，鼠标滚轮进行缩放。它解释了如何与小地图和NPC互动，并提及了时间控制键（小键盘上的+/-）。

“沙盒模式”被描述为一种调试模式，可实现游戏内编辑和调试。此模式提供各种可切换的调试功能，例如NPC寻路、形状编辑器、Lua调试以及在游戏世界中操纵对象的能力。提供了此模式的热键列表（F1、F7、F8、F9、F10、F11）和功能。

最后，作者通过电子邮件（`anthony.salter@gmail.com`）征求反馈意见，邮件主题请注明“Revisited”。该项目的源代码可在GitHub上找到，地址为`github.com/viridiangames`。

---

## 20. Pebble、Rebble及未来之路

**原文标题**: Pebble, Rebble, and a path forward

**原文链接**: [https://ericmigi.com/blog/pebble-rebble-and-a-path-forward/](https://ericmigi.com/blog/pebble-rebble-and-a-path-forward/)

在2025年的一篇博客文章中，Core Devices（正在重新推出 Pebble 智能手表）的创始人 Eric Migicovsky 回应了 Rebble（一个自 2017 年以来一直支持 Pebble 社区的非营利组织）的指控。他声称 Rebble 正在以虚假指控误导社区。

核心争议围绕 Pebble Appstore 数据展开（在 Fitbit 于 2018 年关闭后，Rebble 抓取了 13,000 个应用程序/表盘）。 Core Devices 认为这些数据应该免费提供，不应由 Rebble 控制，而 Rebble 声称拥有 100% 的所有权。

Eric 反驳了具体的指控：（1）Core“窃取”了 Rebble 资助的开源贡献（特别是关于 NimBLE），他辩称 Core 为开源开发做出了重大贡献，并且所有工作都在开放许可下进行。（2）Core 窃取了 Rebble 的 libpebblecommon 库，他解释说 Core 购买了版权并将其合并到开源 libpebble3 中。（3）Core 承诺 Rebble 将维护开发者网站。（4）Core“抓取”了 Rebble 的应用商店，他澄清说他是手动浏览表盘来选择收藏的。

Eric 对 Rebble 的行为表示失望，并质疑他们的动机，特别是关于他们对应用商店和语音转文本和天气等功能的专有控制。他担心依赖 Rebble 作为关键服务的第三方。

Eric 最后敦促 Rebble 开放应用商店存档，停止声称拥有开发者数据，并优先考虑社区的需求。 他强调了他对一个开放和可持续的 Pebble 生态系统的承诺，该生态系统由热情而非利润驱动。

---

## 21. Show HN：浏览器端交互式三体问题3D模拟器

**原文标题**: Show HN: Browser-based interactive 3D Three-Body problem simulator

**原文链接**: [https://trisolarchaos.com/?pr=O_8(0.6)&n=3&s=5.0&so=0.00&im=rk4&dt=1.00e-4&rt=1.0e-6&at=1.0e-8&bs=0.15&sf=0&sv=0&cm=free&kt=1&st=1&tl=1500&cp=2.5208,1.5125,2.5208&ct=0.0000,0.0000,0.1670](https://trisolarchaos.com/?pr=O_8(0.6)&n=3&s=5.0&so=0.00&im=rk4&dt=1.00e-4&rt=1.0e-6&at=1.0e-8&bs=0.15&sf=0&sv=0&cm=free&kt=1&st=1&tl=1500&cp=2.5208,1.5125,2.5208&ct=0.0000,0.0000,0.1670)

这个“Show HN”帖子介绍了一个基于浏览器的交互式3D模拟器，用于探索三体问题，这是经典物理学中的一个著名难题。该模拟器允许用户使用牛顿万有引力定律来模拟多个物体的引力相互作用，并具有一个软化参数以避免奇点。

主要功能包括实时3D物理、多种积分方法（速度Verlet用于能量守恒和长期稳定性，RK4用于短期精度）、已知三体轨道的预设配置（包括8字形和拉格朗日配置，以及来自最近研究的更复杂轨道）以及用户可调参数。

该模拟器提供了分析轨道行为的工具，包括时间线回放和共享配置的能力。它监测能量守恒并显示能量漂移，提供有关模拟精度的反馈。文章阐明，在引力束缚系统中，负总能量是正常的。

该模拟器使用Three.js和JavaScript构建，允许用户尝试初始条件、质量和模拟速度。它跟踪最多10,000帧的模拟历史。鼓励提供反馈以帮助改进该工具。

---

## 22. Itiner-e: 罗马帝国道路的高分辨率数据集

**原文标题**: Itiner-e: A high-resolution dataset of roads of the Roman Empire

**原文链接**: [https://www.nature.com/articles/s41597-025-06140-z](https://www.nature.com/articles/s41597-025-06140-z)

本文介绍了Itiner-e，一个全新的、全面的、高分辨率的罗马道路开放数字数据集，覆盖整个罗马帝国。它通过数字化从考古和历史资料、地形图和遥感数据中识别出的道路而创建，与巴林顿地图集衍生的数据集等先前资源相比，Itiner-e使已知的罗马道路长度几乎翻了一番。这种增加归功于改进的覆盖范围，特别是在伊比利亚半岛、希腊和北非等地区，以及一种更具空间明确性的方法，考虑了地理特征。

Itiner-e的关键特征包括每个路段的详细元数据、唯一的URI、与Pleiades中古代地点的链接以及道路确定性的分类。该数据集显示，只有很小一部分（2.737%）的道路位置被确定无疑，突显了重建古代道路网络的挑战。虽然主要道路的记录相对完善，但很大一部分由次要道路组成，为未来的研究提供了潜力。

本文还承认缺乏关于道路建设和变化的全面年代数据的局限性。该方法涉及识别现有文献中的道路，使用各种地图和图像资料定位它们，并使用GIS对其进行数字化处理。Itiner-e旨在提高我们对罗马交通、连通性和行政管理的理解，同时也明确识别当前知识中的差距，以指导未来的研究。该数据集是研究陆地交通及其对古代世界影响的变革性资源。

---

## 23. 如何在奖励疯狂的世界里保持理智

**原文标题**: How to Stay Sane in a World That Rewards Insanity

**原文链接**: [https://www.joanwestenberg.com/p/how-to-stay-sane-in-a-world-that-rewards-insanity](https://www.joanwestenberg.com/p/how-to-stay-sane-in-a-world-that-rewards-insanity)

J.A. Westenberg 的文章《如何在奖励疯狂的世界里保持理智》探讨了极端主义作为当今社会一种成功的“增长黑客”现象。作者观察到，采取极端立场的个人往往能获得关注、社群和影响力，而那些拥抱细微差别和理性的人则相对被忽视。

Westenberg 认为，这种趋势虽然会带来短期利益，但最终会导致社会无法适应、妥协或承认复杂性。个人会成为自己品牌的囚徒，如果不冒着失去既定身份和社群的风险，就无法改变自己的想法。

文章随后提出了在这种环境中保持理智的策略：

1.  **多元化你的信息摄取：** 积极寻找你不同意的、有条理的观点，以了解聪明人可以持有不同的看法。
2.  **区分利害关系和真相：** 认识到问题的重要性并不代表对它的每一个主张都是正确的，而且你没有必要为你的阵营所提出的每一个论点辩护。
3.  **寻找奖励谦逊的社群：** 寻找重视探求真相胜过部落忠诚，并且接受改变主意或承认无知的群体。

Westenberg 承认抵制极端主义会带来眼前的损失，但他强调了保持理智的长期收益：清晰的思维、适应性和有意义的关系。最终，作者认为世界奖励疯狂只是因为我们用短期的眼光衡量成功，而理智为长期增长提供了无限的潜力。

---

## 24. 改装过的Amiga 500

**原文标题**: Pimped Amiga 500

**原文链接**: [https://www.pimyretro.org/pimped-amiga-500/](https://www.pimyretro.org/pimped-amiga-500/)

将老式Amiga 500升级为90年代初的“梦想机器”

---

## 25. Blender 5.0

**原文标题**: Blender 5.0

**原文链接**: [https://www.blender.org/download/releases/5-0/](https://www.blender.org/download/releases/5-0/)

无法访问文章链接。

---

## 26. Gemini 3 Pro 模型卡 [pdf]

**原文标题**: Gemini 3 Pro Model Card [pdf]

**原文链接**: [https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf)

该文档似乎是一个已损坏或混淆的PDF文件，与“Gemini 3 Pro 模型卡”相关。内容无法人工读取，主要由编码数据流组成。 从提供的原始数据来看，无法确定实际内容、目的或关键信息。它似乎是一个名为 Gemini 3 Pro 的模型的模型卡（旨在记录和传达有关模型的详细信息），但内容本身无法阅读。

---

## 27. 2025年11月18日 Cloudflare 服务中断事后分析报告

**原文标题**: Cloudflare outage on November 18, 2025 post mortem

**原文链接**: [https://blog.cloudflare.com/18-november-2025-outage/](https://blog.cloudflare.com/18-november-2025-outage/)

2025年11月18日，Cloudflare发生重大网络中断，持续时间从UTC时间11:20至17:06，导致大规模HTTP 5xx错误，并影响Turnstile、Workers KV、Dashboard、Email Security和Access等服务。根本原因并非网络攻击，而是ClickHouse数据库权限变更，导致Bot Management系统的“特征文件”因重复条目而翻倍。这个过大的文件在全网络传播，超出软件的大小限制，导致其故障。

由于系统行为波动，该问题最初被误诊为超大规模DDoS攻击。根本原因在于ClickHouse如何分发查询，特别是对用户权限和元数据访问所做的更改。特征文件生成逻辑没有考虑到对系统表元数据所做的数据库更改，导致行重复，从而导致特征文件大小迅速增加。

补救措施包括停止错误特征文件的传播，用已知良好的版本替换它，并重新启动核心代理。虽然流量在UTC时间14:30左右恢复，但包括重启剩余服务在内的全面恢复在UTC时间17:06完成。

该事件还暴露了Bot Management系统中内存预分配的漏洞，因为软件在遇到过大的特征文件时崩溃。Cloudflare目前正专注于加强内部生成的配置文件的摄取，以防止未来发生类似问题。

---

## 28. 我在512字节的引导扇区中写了一个Pong游戏。

**原文标题**: I wrote a Pong game in a 512-byte boot sector

**原文链接**: [https://akshatjoshi.com/i-wrote-a-pong-game-in-a-512-byte-boot-sector/](https://akshatjoshi.com/i-wrote-a-pong-game-in-a-512-byte-boot-sector/)

Akshat Joshi 详述了他将 Pong 游戏完整塞入 512 字节引导扇区的项目，这是一个极具挑战的约束，因为原始 x86 汇编、BIOS 中断和直接视频内存访问都存在局限性。他成功实现了一个功能齐全的 Pong 游戏，包含以下功能：玩家挡板（由 W/S 控制）、CPU 对手、带速度的球、计分、颜色切换（C 键）和完全重置（R 键）。

该游戏在 80x25 文本模式下运行，使用 `stosw` 直接绘制到 0xB800 的视频内存。CPU 对手使用确定性的球跟踪逻辑。他通过使用直接视频内存访问、使用 `imul` 优化定位计算、使用 BIOS 中断 0x16 进行实时、非阻塞键盘输入、将球的速度存储在单个字节中并在碰撞时反转以及使用 BIOS 定时器进行帧速率控制而不是忙等待来提高效率。颜色循环是通过将绘制颜色递增 0x10 实现的。

整个游戏代码用汇编编写，可在 GitHub 上找到，可以使用 NASM 汇编并在 QEMU 或旧硬件上运行。文章重点介绍了在严格的 512 字节引导扇区限制内放入可玩游戏所需的极致优化。

---

## 29. Mojo-V：RISC-V的秘密计算

**原文标题**: Mojo-V: Secret Computation for RISC-V

**原文链接**: [https://github.com/toddmaustin/mojo-v](https://github.com/toddmaustin/mojo-v)

生成摘要时出错

---

## 30. Cloudflare全球网络出现问题

**原文标题**: Cloudflare Global Network experiencing issues

**原文链接**: [https://www.cloudflarestatus.com/incidents/8gmgl950y3h7](https://www.cloudflarestatus.com/incidents/8gmgl950y3h7)

2025年11月18日，Cloudflare发生全球网络服务降级事件，影响了包括Access、Bot Management、CDN/Cache、Dashboard、Firewall、Network、WARP和Workers在内的多项服务。事件始于UTC时间11:48左右，用户可能间歇性地遇到问题。

Cloudflare团队立即开始调查并着手修复。最初的补救措施包括禁用伦敦的WARP访问。在当天，团队发布了多次更新，努力恢复服务并减轻影响，包括部署修复程序以恢复仪表板服务。

虽然服务逐渐恢复，但全球范围内仍报告了间歇性错误和延迟。在恢复过程中，Bot评分暂时受到影响。团队专注于解决部署后的问题，并恢复对应用程序服务客户的服务。Cloudflare Access和WARP服务已恢复，伦敦的WARP访问已重新启用。

截至UTC时间14:42，修复程序已实施，事件被认为已解决，但持续监控以确保服务恢复正常。截至UTC时间17:44，Cloudflare报告服务运行正常，没有出现异常错误或延迟。计划进行全面的事后调查，并建议用户重新启用任何暂时禁用的Cloudflare服务是安全的。事件于UTC时间19:28正式解决。

---

## 31. 我用来制作科幻选集的代码和开源工具

**原文标题**: The code and open-source tools I used to produce a science fiction anthology

**原文链接**: [https://compellingsciencefiction.com/posts/the-code-and-open-source-tools-i-used-to-produce-a-science-fiction-anthology.html](https://compellingsciencefiction.com/posts/the-code-and-open-source-tools-i-used-to-produce-a-science-fiction-anthology.html)

程序员乔·斯泰克拥有一份全职工作和家庭，但他成功地出版了一本科幻选集《Think Weirder》。他利用编程和开源工具简化了出版流程。面对处理通常由出版部门执行的任务的挑战，他构建了工具来自动化重复性流程，并通过简单的文件格式强调透明性和可调试性。

他使用 YAML 文件和一个自定义的 Python CLI 工具（"se.py"）来跟踪和管理数百个提交的故事，高效地组织元数据、编辑状态并生成选集汇编统计数据。这使他能够快速评估选集的规模、构成和作者代表性。

在排版方面，斯泰克出人意料地选择了 LaTeX，使用 XeLaTeX 和 memoir 文档类。他欣赏 LaTeX 的可重复性、专业的排版、可定制性和版本控制功能。他创建了一个自定义样式包（"compelling.sty"）来控制格式。一个 Python 脚本将各种文档格式（HTML、PDF、Word）转换为 LaTeX，从而自动化了格式化过程。

为了创建电子书，斯泰克利用他的 LaTeX 源代码，并使用 Pandoc 将其转换为 EPUB 格式。然后，他编写了一个后处理脚本来修改 EPUB 的目录，以包括作者署名，从而与印刷选集的格式保持一致。

斯泰克强调了保持组织性、可重复构建、简单文件格式和增量学习的重要性。他认为这种方法对任何考虑出版书籍的人来说都是可行的，并鼓励读者提出问题。

---

## 32. 蓝牙信道探测：蓝牙创新的下一大步

**原文标题**: Bluetooth Channel Sounding: The Next Leap in Bluetooth Innovation

**原文链接**: [https://www.embedded.com/bluetooth-channel-sounding-the-next-leap-in-bluetooth-innovation?_gl=1*8e3cij*_gcl_au*MzQwNzM2NDAxLjE3NjMwMzUwNzA.*_ga*NDc3NjU3MDk3LjE3NjMwMzUwNzA.*_ga_ZLV02RYCZ8*czE3NjMwMzUwNjkkbzEkZzAkdDE3NjMwMzUwNjkkajYwJGwwJGgw](https://www.embedded.com/bluetooth-channel-sounding-the-next-leap-in-bluetooth-innovation?_gl=1*8e3cij*_gcl_au*MzQwNzM2NDAxLjE3NjMwMzUwNzA.*_ga*NDc3NjU3MDk3LjE3NjMwMzUwNzA.*_ga_ZLV02RYCZ8*czE3NjMwMzUwNjkkbzEkZzAkdDE3NjMwMzUwNjkkajYwJGwwJGgw)

好的，我已经访问并阅读了文章：《蓝牙信道探测：蓝牙创新的下一次飞跃》。

以下是摘要：

文章讨论了蓝牙信道探测，这项新技术将显著增强蓝牙的功能，尤其是在定位服务和设备追踪方面。信道探测使蓝牙设备能够精确测量信号的距离和到达角，从而获得比以前基于 RSSI 的蓝牙技术更精确的定位。

其核心优势在于大大提高了定位物体和设备的准确性。这开启了一系列新的应用，包括：

*   **增强的室内导航：** 在建筑物内进行更精确的地图绘制和路径指引。
*   **资产追踪：** 更可靠地追踪工具、设备和其他贵重物品。
*   **AR/VR 中的空间感知：** 实现更具沉浸感和响应性的增强现实和虚拟现实体验。
*   **无钥匙进入系统：** 为车辆和建筑物提供更安全可靠的访问控制。

文章强调，信道探测通过利用一种分析设备之间无线电信道特征的技术来实现这种精度。 通过测量蓝牙信号的飞行时间和相位，它可以精确地确定距离和到达角。 作者强调，将信道探测集成到即将发布的蓝牙规范中将推动新一轮创新，提高蓝牙设备在各个行业的可用性和功能。 预计它将提供厘米级的精度，与目前的方法相比有了相当大的改进。

---

## 33. Bild AI (YC W25) 招聘 – 让住房变得可负担

**原文标题**: Bild AI (YC W25) is hiring – Make housing affordable

**原文链接**: [https://www.ycombinator.com/companies/bild-ai/jobs/m2ilR5L-founding-engineer-applied-ai](https://www.ycombinator.com/companies/bild-ai/jobs/m2ilR5L-founding-engineer-applied-ai)

Bild AI 招聘创始工程师（应用AI），助力提升建筑效率，降低住房成本。该公司是一家 Y Combinator W25 初创公司，正利用计算机视觉、LLMs 和 AI 技术解决蓝图解读、成本估算和许可证申请方面的复杂问题。

理想的候选人需具备 CV/ML 应用经验，是从 0 到 1 的 AI 产品构建者，并拥有成长型思维。他们还应具备良好的沟通能力，能适应早期初创公司的“苦活累活”，最好有创业/创始人经验或建筑行业背景。具有影响力驱动力者优先。

该职位专注于 AI 智能层，快速交付原型，并根据用户反馈进行改进。公司希望求职者渴望应用最新的计算机视觉、LLM 模型和 AI 系统。

该职位位于旧金山，需要全职在办公室工作。Bild AI 是一家采用模型花园方法进行蓝图理解的早期公司。他们在演示日之前获得了顶级风险投资公司的投资，并拥有以客户为中心的产品开发方法。

---

## 34. Strace-macOS：macOS 平台的 strace 命令克隆

**原文标题**: Strace-macOS: A clone of the strace command for macOS

**原文链接**: [https://github.com/Mic92/strace-macos](https://github.com/Mic92/strace-macos)

`strace-macos` 是 macOS 的系统调用跟踪器，旨在复制 Linux `strace` 命令的功能。它利用 LLDB 调试器 API，并比现有的 `dtruss` 工具拥有多个优势，主要是可在启用系统完整性保护 (SIP) 的情况下工作。

该工具目前处于 Beta 版，提供按名称或类别过滤系统调用、参数的符号解码（标志、错误代码、结构体）、多种输出格式（JSON Lines、strace 兼容的文本）、彩色输出和摘要统计等功能。可以通过 Nix Flakes 安装，也可以使用 macOS 系统 Python（LLDB 绑定所必需）手动安装。

使用示例包括跟踪命令、过滤系统调用（文件、网络、进程）、附加到正在运行的进程以及生成摘要统计信息。文档详细介绍了支持的系统调用类别（文件、网络、进程等），并提供了与 Linux `strace` 的比较，强调了功能对等性以及未来开发的领域，如否定过滤、正则表达式过滤、路径过滤和跟踪 fork。

`strace-macos` 需要 macOS 12+（Monterey 或更高版本），最好在 Apple Silicon 上运行。欢迎贡献，并且可以通过作者或 Numtide 获得商业支持。核心功能已经可以工作，涵盖进程生成、附加、系统调用捕获、参数解码、符号标志解码、错误代码解码、结构体解码、系统调用过滤和输出格式化。该项目旨在尽可能与 Linux `strace` 兼容，并且通过在 SIP 下工作和提供更丰富的输出来超越 `dtruss`。

---

## 35. 谷歌老板称人工智能投资热潮存在“非理性因素”

**原文标题**: Google boss says AI investment boom has 'elements of irrationality'

**原文链接**: [https://www.bbc.com/news/articles/cwy7vrd8k4eo](https://www.bbc.com/news/articles/cwy7vrd8k4eo)

谷歌CEO皮查伊：人工智能投资热潮存在“非理性因素”

---

## 36. 伊安尼斯·泽纳基斯算法作曲的严谨方法(2009) [pdf]

**原文标题**: A Rigorous Approach to the Algorithmic Composition of Iannis Xenakis(2009) [pdf]

**原文链接**: [https://monoskop.org/images/3/38/Hoffmann_Peter_Music_Out_of_Nothing_A_Rigorous_Approach_to_Algorithmic_Composition_by_Iannis_Xenakis_2009.pdf](https://monoskop.org/images/3/38/Hoffmann_Peter_Music_Out_of_Nothing_A_Rigorous_Approach_to_Algorithmic_Composition_by_Iannis_Xenakis_2009.pdf)

文章《扬尼斯·泽纳基斯算法作曲的严谨方法》可能介绍了一种使用算法创作扬尼斯·泽纳基斯风格音乐的方法。泽纳基斯以其数学驱动的作曲而闻名，经常采用随机过程、集合论和博弈论来生成音乐结构。

该文章可能详细阐述了用于模仿泽纳基斯作曲技巧的特定算法和数学模型。它可能会讨论这些算法如何用于生成诸如音高、时值、力度和音色等参数，从而模仿泽纳基斯创作复杂且通常不协和的音景的方法。该论文很可能概述了这些算法的特定实现，可能使用专为音乐创作设计的软件或编程语言。

一个关键的重点很可能是算法如何将泽纳基斯抽象的音乐理念转化为具体的乐谱或声音文件。该文章可能会分析由此产生的音乐，评估算法方法在多大程度上成功地捕捉了泽纳基斯风格的独特特征。标题中提到的“严谨”暗示了一种系统且定义明确的方法，用于创作泽纳基斯风格的音乐，强调对作曲过程的精确性和数学控制。它可能探讨了使用算法方法来复制人类作曲家的创造力和表现力的局限性和挑战。

---

## 37. 欧盟委员会数字综合法案是对欧盟数字保护的重大倒退

**原文标题**: EU Commission's Digital Omnibus is a major rollback of EU digital protections

**原文链接**: [https://edri.org/our-work/commissions-digital-omnibus-is-a-major-rollback-of-eu-digital-protections/](https://edri.org/our-work/commissions-digital-omnibus-is-a-major-rollback-of-eu-digital-protections/)

欧盟委员会的“数字综合方案”，包括数字综合方案和人工智能数字综合方案，被批评为对欧盟数字保护的重大倒退，威胁人权和科技政策。EDRi认为这些提案削弱了GDPR、ePrivacy指令和人工智能法案，实际上是在拆除数十年来建立的基于规则的体系。

主要批评包括：
*   **削弱ePrivacy：** 将设备访问条款转移到GDPR，并设置广泛的例外，允许在未经同意的情况下收集数据。
*   **破坏GDPR：** 缩小个人数据的定义，使未经检查的数据可用于人工智能培训，并削弱自动化决策的保障。
*   **稀释人工智能法案：** 允许豁免基本人工智能规则，推迟高风险要求，并削弱透明度和问责制。

EDRi认为，这些改变有利于企业利益，特别是大型科技公司和美国政府，却牺牲了个人权利和保护，尤其是边缘化群体。他们批评欧盟委员会规避民主监督，优先考虑行业投入而非公共利益。“数字适应性检查”进一步预示着对所有数字保护的广泛放松管制议程。

EDRi敦促欧洲理事会和议会否决这些提案，并专注于执行现有的数字法律。他们认为，欧盟需要加强数字权利的执行力度，而不是削弱规则，以保护数字时代的人们。

---

## 38. OrthoRoute – 用于KiCad的GPU加速自动布线器

**原文标题**: OrthoRoute – GPU-accelerated autorouting for KiCad

**原文链接**: [https://bbenchoff.github.io/pages/OrthoRoute.html](https://bbenchoff.github.io/pages/OrthoRoute.html)

OrthoRoute是一款GPU加速的KiCad自动布线插件，旨在处理传统自动布线器难以处理的复杂、高密度PCB。为了布线一个包含超过8,000个网络和17,000个焊盘的大型背板，作者利用KiCad的新IPC API在插件中构建了第二个PCB模型，并实现了一个曼哈顿正交布线引擎。

核心算法是PathFinder，它改编自FPGA布线技术，将PCB视为一个图，节点代表交叉点，边代表走线。该算法迭代地布线网络，考虑拥塞情况并重新布线有问题的走线。通过CUDA进行GPU加速，极大地加快了计算密集型的PathFinder算法，从而能够布线复杂的电路板。

挑战包括管理拥塞、振荡和参数调整。作者开发了板级自适应参数，分析电路板的特性以优化PathFinder的行为，从而解决了依赖单一参数集带来的局限性。

由于目标背板的尺寸很大，自动布线是在租用的GPU服务器上进行的，然后导入回KiCad。该过程虽然耗时41小时，但比传统方法快得多。尽管存在一些需要手动清理的DRC（设计规则检查）问题，但OrthoRoute成功地布线了复杂的背板。

作者希望OrthoRoute的模块化架构能够激发进一步的开发和适应，以用于不同的板类型和布线策略，并强调GPU加速布线在PCB设计中的潜力。

---

## 39. 我将卸任Mastodon CEO。

**原文标题**: I am stepping down as the CEO of Mastodon

**原文链接**: [https://blog.joinmastodon.org/2025/11/my-next-chapter-with-mastodon/](https://blog.joinmastodon.org/2025/11/my-next-chapter-with-mastodon/)

Mastodon创始人兼CEO在职近10年后卸任，将商标及其他资产所有权移交给Mastodon非营利组织。此举旨在确保项目坚守其价值观，避免创始人主导的风险，即创始人个人因素可能使蓬勃发展的社群脱轨。该CEO承认存在一定的个人原因，表示该职位压力巨大，与个人性格不符。在缺乏资源的情况下被拿来与科技亿万富翁比较，加上负面的用户互动和肤浅的批评，都带来了很大的压力。

虽然该CEO不愿评价自己的功绩，但强调了说“不”以保持专注的重要性，即使这可能导致Mastodon失去宣传机会。他们最自豪的成就是该项目从卧室里编写的代码发展成为Fediverse中一个蓬勃发展的、以社区为中心的实体。

虽然卸任CEO，但创始人将继续担任顾问角色，源于对Mastodon和Fediverse的热情。他们认为Fediverse是日益反乌托邦式的资本主义互联网的一个重要替代方案，并相信Mastodon是将这一美好愿景带给更广泛受众的最佳希望。他们相信，在新的领导下，该组织能够更好地朝着最初的愿景前进。

---

## 40. 零错误解决百万步LLM任务

**原文标题**: Solving a million-step LLM task with zero errors

**原文链接**: [https://arxiv.org/abs/2511.09030](https://arxiv.org/abs/2511.09030)

本文于2025年11月12日提交至arXiv，介绍了MAKER，一种旨在克服大型语言模型（LLMs）在执行漫长、多步骤任务方面的局限性的新型系统。虽然LLMs在推理和工具使用方面展现出了前景，但其持续存在的错误率阻碍了它们在复杂流程中的应用，这些流程需要能镜像人类或组织的工作流程。

MAKER通过成功解决一项需要超过一百万个LLM步骤且零误差的任务，实现了突破。其关键创新在于将任务极端分解为大量由专门的“微代理”处理的高度聚焦的子任务。这种模块化允许通过多代理投票机制在每个步骤进行有效的纠错。

作者认为，这种被称为大规模分解代理过程（MDAPs）的方法，为扩展LLM解决复杂、现实世界问题的能力提供了一条更有希望的途径，而不是仅仅依赖于单片LLM的持续改进。该论文强调了MDAPs在高效解决组织和社会规模问题方面的潜力。

该论文共14页（包括参考文献和附录共29页），并被归类为人工智能、计算与语言以及多代理系统。 它包括指向资源的链接，例如论文的PDF版本、实验性HTML版本、TeX源代码，以及指向书目工具、代码存储库和演示平台的链接。

---

## 41. FFmpeg 8.0深度剖析

**原文标题**: Deep Dive into FFmpeg 8.0

**原文链接**: [https://www.rendi.dev/post/ffmpeg-8-0-part-1-using-whisper-for-native-video-transcription-in-ffmpeg](https://www.rendi.dev/post/ffmpeg-8-0-part-1-using-whisper-for-native-video-transcription-in-ffmpeg)

本文深入探讨了FFmpeg 8.0，重点介绍了其与OpenAI开源语音识别库Whisper令人激动的新原生集成。此集成允许用户使用单个工具转录视频和音频、添加字幕以及提取精彩片段。

本文介绍了在Windows上安装带有Whisper的FFmpeg 8.0，解释了新的Whisper滤镜参数（模型、语言、队列、目的地、格式），并回顾了使用不同模型（base、medium、large）进行Whisper转录的基准测试。文章强调，base和medium英语模型还会标注非语音音频事件，如音乐和尖叫。性能基准测试显示了模型大小和GPU使用对转录速度的影响。

本文然后探讨了使用HLS的实时视频流转录，演示了如何将SRT字幕直接输出到终端。最后，本文简要介绍了语音激活检测 (VAD) 功能，讨论了其提高转录准确性和处理幻觉的潜力，尽管测试显示速度没有显著提高。提供的代码片段展示了如何使用FFmpeg命令来执行生成SRT文件和将字幕烧录到视频等任务。

---

## 42. Show HN: RowboatX – 日常自动化任务的开源Claude代码

**原文标题**: Show HN: RowboatX – open-source Claude Code for everyday automations

**原文链接**: [https://github.com/rowboatlabs/rowboat](https://github.com/rowboatlabs/rowboat)

RowboatX 是一个受 Claude Code 启发的开源 CLI 工具，它允许用户创建和管理具有完整 Shell 访问权限的后台代理，用于日常自动化任务。它通过可配置的 `models.json` 文件支持各种 LLM 提供商，例如 OpenAI、Anthropic、Gemini、Ollama 等。

主要功能包括：

*   **具有 Shell 访问权限的后台代理：** 创建代理来执行任务，例如使用 Shell 命令（包括 `ffmpeg`）从文章生成播客。
*   **MCP 服务器集成：** 连接到任何 MCP（机器控制协议）服务器，为您的代理添加功能。RowboatX 处理集成过程。
*   **调度和监控：** 调度代理在特定时间运行，监控它们的执行状态，并在文件系统上检查它们的状态。
*   **手动执行和恢复：** 使用输入手动运行代理，或使用运行 ID 从之前的运行恢复。
*   **轻松配置：** 在 `models.json` 文件中配置 LLM 提供商和模型，包括用于 OpenAI 兼容主机的自定义 baseURL 和标头。

RowboatX 简化了由 LLM 和 Shell 脚本驱动的自动化任务的创建、管理和执行。它提供了一种强大而灵活的方法来自动化日常工作流程。该文档还提到了“Rowboat Classic UI”的存在，这意味着它与基于 CLI 的 RowboatX 不同。

---

## 43. 从跑步机上作画的人身上我学到的关于创造力的事 (2024)

**原文标题**: What I learned about creativity from a man painting on a treadmill (2024)

**原文链接**: [https://quinnmaclay.com/texts/lets-paint](https://quinnmaclay.com/texts/lets-paint)

本文探讨了作者如何通过一个意想不到的来源——约翰·基尔达夫的“让我们画画电视”——克服创作障碍和对失败的恐惧。起初，作者发现传统的灵感来源，如杰作，令人望而却步，倍感沮丧。“让我们画画电视”是一个基尔达夫边运动边（拙劣地）绘画，并在像烦人的来电者和技术困难等混乱中兼顾多项任务的节目，它提供了一种不同的灵感来源。该节目持续的“失败”是其核心吸引力。基尔达夫愿意在不可避免的灾难面前坚持下去，这表明了过程比结果更重要。

作者回顾了基尔达夫在“美国达人秀”上的灾难性亮相，进一步证明了该节目固有的不适合主流成功，然而基尔达夫对该项目的持续投入强调了耐力和实验的价值，无论结果如何。

基尔达夫在Vice采访中引用的哲学强调，激励他人不是创造完美的艺术，而是展示尝试、失败和继续的意愿。作者总结说，“让我们画画电视”提醒人们以轻松的心态对待创作活动，将失败视为学习机会，并在创作过程中找到乐趣。最终，该节目成为了人生挑战的隐喻，鼓励观众在混乱中坚持下去并茁壮成长。

---

## 44. 几乎所有英国司机都表示车头灯太亮。

**原文标题**: Nearly all UK drivers say headlights are too bright

**原文链接**: [https://www.bbc.com/news/articles/c1j8ewy1p86o](https://www.bbc.com/news/articles/c1j8ewy1p86o)

英国政府近期委托的一项研究显示，驾驶员普遍担忧前大灯亮度问题。据交通部（DfT）称，97%的受访驾驶员表示经常或有时会受到迎面车辆前大灯的干扰，96%的人认为某些或大多数前大灯过于明亮。因此，政府宣布将进一步调查前大灯设计。

由交通运输研究所（TRL）进行的研究表明，LED和更白的前照灯可能会导致眩光问题。因此，很大一部分驾驶员（33%）已经减少或停止夜间驾驶，而另有22%的人更愿意减少夜间驾驶，但无法做到。

TRL的研究强调，LED灯越来越多地应用于车辆，它们更亮、更集中，并发出更多的蓝光，这在夜间可能对人眼造成挑战。英国皇家汽车俱乐部（RAC）高级政策官员Rod Dennis对调查结果表示欢迎，并强调需要在有效前照灯和最大限度地减少眩光之间取得平衡。验光师学院的Denise Voon主张立即采取行动并进一步研究以修改前照灯法规。交通部将在其即将发布的道路安全战略中纳入新措施以解决该问题。

---

## 45. GoSign桌面版RCE漏洞影响意大利用户

**原文标题**: GoSign Desktop RCE flaws affecting users in Italy

**原文链接**: [https://www.ush.it/2025/11/14/multiple-vulnerabilities-gosign-desktop-remote-code-execution/](https://www.ush.it/2025/11/14/multiple-vulnerabilities-gosign-desktop-remote-code-execution/)

本文详细描述了GoSign Desktop 2.4.0及更早版本中发现的一个严重远程代码执行(RCE)漏洞，GoSign Desktop是在意大利广泛使用的电子签名解决方案。该漏洞源于TLS验证绕过和一个不安全的更新机制。

具体来说，当配置了代理时，GoSign Desktop会禁用TLS证书验证，从而为中间人(MitM)攻击敞开了大门。这种绕过，加上依赖于未签名清单的更新过程，使得攻击者可以注入恶意更新，导致任意代码执行。攻击场景包括恶意软件安装、凭据窃取和权限提升。该漏洞影响Windows、macOS和Linux版本。

供应商Tinexta InfoCert最初承认了该漏洞，但随后停止了沟通，并在没有适当披露或确认的情况下发布了2.4.1版本。虽然2.4.1版本通过清单签名解决了远程代码执行问题，但使用代理时底层TLS验证绕过问题仍然未修复，导致OAuth密钥容易被拦截。

研究人员使用动态运行时检测来确认TLS证书验证的禁用。该建议包含证明该漏洞的概念验证代码。本文强调了供应商对负责任披露流程的处理不当，以及对意大利用户（包括公共管理部门和企业）的潜在广泛影响。

---

## 46. 短小精悍的难题书

**原文标题**: Short Little Difficult Books

**原文链接**: [https://countercraft.substack.com/p/short-little-difficult-books](https://countercraft.substack.com/p/short-little-difficult-books)

无法访问文章链接。

---

## 47. 金卡纳改装版1978年斯巴鲁Brat：9500转红线，主动气动，超级皮卡

**原文标题**: Gymkhana's 1978 Subaru Brat with 9,500-RPM Redline, Active Aero Is One Super Ute

**原文链接**: [https://www.thedrive.com/news/gymkhanas-1978-subaru-brat-with-9500-rpm-redline-and-active-aero-is-one-super-ute](https://www.thedrive.com/news/gymkhanas-1978-subaru-brat-with-9500-rpm-redline-and-active-aero-is-one-super-ute)

本文介绍了Hoonigan最新的金卡纳战车：斯巴鲁Brataroo 9500 Turbo，该车基于1978年款斯巴鲁BRAT改装而来。 这款经过重度改装的皮卡拥有由Vermont SportsCar打造的涡轮增压2.0升水平对置发动机，可产生670马力和680磅-英尺的扭矩，转速可达惊人的9500转/分。 它采用了源自赛车的全轮驱动系统和一个六速序列式SADEV变速箱，以实现最佳动力传递和轮胎撕裂能力。 主动空气动力学套件非常突出，配备了可调节的翼板和襟翼，旨在增强转弯性能、高速稳定性以及跳跃后的安全着陆。 Brataroo拥有引人注目的涂装和一个巨大的后扰流板。 据称碳纤维内饰与1978年的原始设计相似，但尚未发布任何图片。 Brataroo将于12月初在Hoonigan YouTube频道上的下一集金卡纳剧集“Aussie Shred”中首次亮相。

---

## 48. 欧盟放松人工智能、隐私规定，批评者警告向大型科技公司让步

**原文标题**: EU eases AI, privacy rules as critics warn of caving to Big Tech

**原文链接**: [https://www.reuters.com/sustainability/boards-policy-regulation/eu-ease-ai-privacy-rules-critics-warn-caving-big-tech-trump-2025-11-19/](https://www.reuters.com/sustainability/boards-policy-regulation/eu-ease-ai-privacy-rules-critics-warn-caving-big-tech-trump-2025-11-19/)

据称欧盟正在放松其人工智能和隐私监管，引发了对其屈服于大型科技公司压力的批评。虽然仅从标题无法得知这些改变的具体细节，但这暗示着欧盟正在偏离最初提议或实施的更严格措施。这种放松可能包括削弱执法机制、缩小受监管活动的范围或推迟实施时间表。

批评人士担心，此举将以牺牲个人隐私和合乎道德的人工智能发展为代价，让大型科技公司受益。他们担心，通过放松规则，欧盟可能会创造一种监管环境，让大型科技公司能够在更少的监督和问责制下运营。这一转变正值更广泛的政治讨论之际，包括唐纳德·特朗普可能于2025年重返权力，这可能会影响欧盟的战略重点以及维持对科技监管强硬立场的意愿。文章可能探讨了正在进行的具体修改、修改背后的理由，以及对消费者、企业和欧洲人工智能治理未来的潜在后果。

---

## 49. 研究人员称发现 WhatsApp 枚举漏洞，造成“史上最大泄露”

**原文标题**: Researchers claim 'largest leak ever' after uncovering WhatsApp enumeration flaw

**原文链接**: [https://www.theregister.com/2025/11/19/whatsapp_enumeration_flaw/](https://www.theregister.com/2025/11/19/whatsapp_enumeration_flaw/)

维也纳大学的研究人员发现了一个 WhatsApp 枚举漏洞，使他们能够收集 35 亿用户的数据，这可能成为“历史上最大的数据泄露事件”。通过输入生成的电话号码，他们能够以每小时 1 亿个帐户的速度收集用户详细信息，如电话号码、姓名和头像，利用了该平台缺乏有效速率限制的缺陷。

收集到的数据可能被用于创建反向电话簿，并泄露来自个人资料文本的敏感用户信息，包括性取向、政治观点和职业细节，这可能会影响在 WhatsApp 被禁止的国家/地区的个人。研究人员还强调了网络犯罪分子可能滥用这些数据进行垃圾邮件、网络钓鱼和自动语音电话攻击的可能性。

研究人员发现，2021 年 Facebook 数据泄露事件中很大一部分电话号码仍然在 WhatsApp 上处于活动状态。在通过漏洞赏金计划收到通知后，Meta 声称一直在开发反爬虫系统，研究人员证实这些系统现在可以有效地阻止枚举方法。虽然用户消息仍然是端到端加密的，并且没有访问任何非公开数据，但研究人员指出 Meta 最初的反应很慢，花费了近一年的时间才对这个问题采取有意义的措施。然而，他们承认，一旦意识到问题的严重性，Meta 立即采取了行动。

---

## 50. GitHub: Git 操作失败

**原文标题**: GitHub: Git operation failures

**原文链接**: [https://www.githubstatus.com/incidents/5q7nmlxz30sk](https://www.githubstatus.com/incidents/5q7nmlxz30sk)

2025年11月18日，GitHub发生Git操作故障，影响Git操作和Codespaces。事件始于Git操作可用性下降，于UTC时间20:39开始调查。UTC时间20:52的初步报告提到Git HTTP操作出现故障。进一步的更新显示，包括SSH和HTTP在内的所有Git操作均失败，Codespaces的可用性也随之降低。

GitHub确定了可能的原因并着手修复，于UTC时间21:36左右部署了修复程序。他们开始观察到一些领域的恢复情况，并继续提供更新。到UTC时间21:55，Codespaces已正常运行，GitHub报告所有服务已完全恢复。Git操作也于UTC时间21:56恢复正常运行。事件于UTC时间21:59解决，GitHub承诺分享详细的根本原因分析。在整个事件过程中，GitHub通过其状态页面提供了频繁的更新。

---

## 51. 不用条件语句或布尔值的Fizz Buzz

**原文标题**: Fizz Buzz without conditionals or booleans

**原文链接**: [https://evanhahn.com/fizz-buzz-without-conditionals-or-booleans/](https://evanhahn.com/fizz-buzz-without-conditionals-or-booleans/)

埃文·哈恩提出了一种解决经典 Fizz Buzz 问题的创造性方案，但带有一个独特的约束：不使用布尔值、条件语句或模式匹配。他利用 Python 的 `itertools.cycle` 生成重复的空字符串以及单词 "Fizz" 和 "Buzz" 的序列。然后，这些循环序列与 1 到 100 的数字一起使用 `zip` 函数进行组合。解决方案的核心在于 `string_mask` 函数，如果存在 "Fizz"、"Buzz" 或 "FizzBuzz"，它会将数字字符串的开头替换为这些字符串；否则，它会保持原始数字字符串不变。

这篇文章强调了在没有典型条件逻辑的情况下实现 Fizz Buzz 的巧妙之处，展示了对字符串操作和序列生成的巧妙运用。然而，它也承认一个局限性：由于当生成的字符串（"Fizz"、"Buzz" 等）短于数字字符串时，`string_mask` 函数的行为会导致代码在 10,000 及以上的数字时失效。作者最后邀请读者提出替代解决方案，暗示在这些特定约束下，可能存在更健壮或更优雅的解决方案。

---

## 52. 沃格尔奇迹

**原文标题**: The Miracle of Wörgl

**原文链接**: [https://scf.green/story-of-worgl-and-others/](https://scf.green/story-of-worgl-and-others/)

沃尔格尔的奇迹：探索补充货币及其刺激地方经济的潜力

---

## 53. 瑞贝卡·海尼曼——从无家可归到移植《毁灭战士》(2022)

**原文标题**: Rebecca Heineman – from homelessness to porting Doom (2022)

**原文链接**: [https://corecursive.com/doomed-to-fail-with-burger-becky/](https://corecursive.com/doomed-to-fail-with-burger-becky/)

本文总结了CoRecursive播客节目，该节目以瑞贝卡·“汉堡贝基”·海涅曼为主角，她是一位资深电子游戏行业人士，以其游戏移植方面的专业知识而闻名。文章记录了她从遭受虐待和无家可归的艰难童年到成为一名成功的游戏开发者的历程。

叙述从海涅曼的早年生活开始，详细描述了她所面临的困境，包括食物匮乏，这也使她获得了“汉堡贝基”的绰号。15岁时她离家出走，住在垃圾箱后面，直到她找到工作，最终参加并赢得了雅达利太空侵略者锦标赛，开启了她的职业生涯。

文章强调了她对游戏硬件的理解能力，这是她通过修理街机和逆向工程雅达利2600游戏卡带而培养起来的。她对Apple II和Atari 2600中使用的6502处理器的了解，使她能够反汇编和修改游戏代码。

海涅曼独特的技能使她获得了Avalon Hill的工作，这是她的第一个有偿编程职位。她很快就因精通新平台而声名鹊起，并成为Interplay进行移植的首选人员。

文章随后转向了将《毁灭战士》移植到3DO游戏机的故事，但同时涉及了海涅曼在此之前所拥有的专业知识和经验。

---

## 54. 查克·摩尔：Colorforth 停止工作了 [视频]

**原文标题**: Chuck Moore: Colorforth has stopped working [video]

**原文链接**: [https://www.youtube.com/watch?v=MvkGBWXb2oQ#t=22](https://www.youtube.com/watch?v=MvkGBWXb2oQ#t=22)

此条目为占位符或存根，仅包含YouTube版权声明和标准链接。提及名为“Chuck Moore: Colorforth has stopped working”的视频，但未提供关于该视频内容或背景的任何信息。唯一能获得的信息是该视频可能讨论了查克·摩尔和他的编程语言Colorforth，并可能涉及该语言停止工作的问题。

---

## 55. 安第斯山脉的神秘洞穴或为古代集市

**原文标题**: Mysterious holes in the Andes may have been an ancient marketplace

**原文链接**: [https://www.sydney.edu.au/news-opinion/news/2025/11/10/mysterious-holes-in-the-andes-may-have-been-an-ancient-marketplace-new-research-suggests.html](https://www.sydney.edu.au/news-opinion/news/2025/11/10/mysterious-holes-in-the-andes-may-have-been-an-ancient-marketplace-new-research-suggests.html)

A new study suggests that the mysterious "Band of Holes" (Monte Sierpe) in the Pisco Valley of southern Peru, consisting of over 5000 aligned holes, may have been an ancient marketplace. Researchers from the University of Sydney used drone technology to map the site and discovered numerical patterns in the layout, suggesting an underlying intention in its organization.

Intriguingly, the arrangement of Monte Sierpe is similar to that of an Inca khipu (an ancient accounting device). Soil analysis revealed ancient pollens of maize (corn) and reeds, indicating that people deposited plants in the holes, potentially using baskets for transport.

These findings suggest that Monte Sierpe was a pre-Inca marketplace where mobile traders, specialists, and others exchanged goods like corn and cotton. The researchers believe the holes acted as a "social technology" that brought people together and later evolved into a large-scale accounting system under the Inca Empire.

The site's strategic location between Inca administrative sites and near a network of pre-Hispanic roads, in a transitional ecological zone, further supports the marketplace theory. The research team suggests the pre-Inca Chincha Kingdom initially used Monte Sierpe for regulated barter and exchange, which later developed into an accounting place under Inca rule. The study highlights the modification of landscapes by past communities to facilitate interaction and trade.


---

## 56. 猛禽光环的内存子系统：应对iGPU挑战

**原文标题**: Strix Halo's Memory Subsystem: Tackling iGPU Challenges

**原文链接**: [https://chipsandcheese.com/p/strix-halos-memory-subsystem-tackling](https://chipsandcheese.com/p/strix-halos-memory-subsystem-tackling)

本文分析了AMD Strix Halo APU的内存子系统，重点关注其如何在移动设备中平衡CPU和iGPU需求所面临的挑战。Strix Halo配备了32MB Infinity Cache (MALL)，作为GPU的末级缓存，远大于之前的AMD移动iGPU。虽然Infinity Cache的延迟略高于独立显卡，但带宽测试显示其性能接近1 TB/s。其行为由软件动态控制，缓存策略可能会动态变化。

本文还深入探讨了CPU端的内存性能。虽然Strix Halo CCD的晶片边界写入带宽高于桌面级同类产品，但由于读密集型工作负载，其影响甚微。单个Strix Halo CCD在较低延迟下达到较高带宽，但仅在达到一定带宽负载后才会实现，这是由于LPDDR5X的高基线延迟所致。本文质疑Strix Halo的跨晶片延迟，发现其高于桌面系统，尽管采用了先进的封装，这可能是由于晶片边界之外的延迟增加所致。

最后，本文考察了CPU和GPU之间共享内存访问所面临的挑战。GPU带宽负载会增加CPU内存延迟，并且Strix Halo可能会在极端带宽需求下优先考虑GPU。在CPU密集型工作负载（如Cyberpunk 2077的基准测试）中，Strix Halo与桌面系统之间存在较大差距，突显了内存延迟的影响。最终，Strix Halo的CPU核心需要出色的缓存命中率才能缓解内存子系统的限制。

---

## 57. 尝试使用 Gemini 3 Pro 进行音频转录和一个新的 pelican 基准测试

**原文标题**: Trying out Gemini 3 Pro with audio transcription and a new pelican benchmark

**原文链接**: [https://simonwillison.net/2025/Nov/18/gemini-3/](https://simonwillison.net/2025/Nov/18/gemini-3/)

2025年11月18日，谷歌发布了Gemini 3 Pro。作者拥有预览权限，称其为Gemini 2.5的升级版，现在可以与Claude Sonnet 4.5和GPT-5.1等竞争模型相媲美。Gemini 3 Pro保持了相同的知识截止日期（2025年1月），接受100万个输入token和64,000个输出token，并支持多模态输入。

根据谷歌的数据，基准测试结果显示，Gemini 3 Pro在标准测试中得分略高于Claude Sonnet 4.5和GPT-5.1。虽然比Gemini 2.5 Pro更贵，但它比Claude Sonnet 4.5便宜。

作者通过分析基准数据的屏幕截图，生成准确的alt文本并将其转换为JSON格式，测试了Gemini 3 Pro的多模态功能。

一项更大的测试涉及将一段3小时33分钟的半月湾市议会会议的音频转录成文字。虽然转录有效，但时间戳不准确。作者还指出，该人工智能总结了会议中的西班牙语指示。

最后，作者使用“鹈鹕骑自行车”的SVG生成提示，测试了Gemini 3 Pro的“思考水平”。作者升级了提示，以进行更具挑战性的基准测试，重点关注加州褐鹈鹕的特定细节。虽然所有模型都在鹈鹕的实际颜色上遇到了困难，但具有高思考水平的Gemini 3 Pro产生了最准确的图像。还提供了GPT-5.1和Claude Sonnet 4.5的示例，突出了它们输出的差异。

---

## 58. 丽贝卡·海涅曼去世

**原文标题**: Rebecca Heineman has died

**原文链接**: [https://www.pcgamer.com/gaming-industry/legendary-game-designer-programmer-space-invaders-champion-and-lgbtq-trailblazer-rebecca-heineman-has-died/](https://www.pcgamer.com/gaming-industry/legendary-game-designer-programmer-space-invaders-champion-and-lgbtq-trailblazer-rebecca-heineman-has-died/)

先锋游戏开发者、美国首位正式认可的电子游戏冠军丽贝卡·海涅曼因癌症去世，享年62岁。消息由朋友和她在GoFundMe页面上的最后一条消息公布，该页面最初旨在帮助支付治疗费用，现在将协助她的家人处理葬礼事宜。

海涅曼对游戏行业产生了重大影响，于1983年共同创立了Interplay，并为《废土》、《辐射》和《博德之门》等标志性PC游戏做出了贡献。她是一位杰出的设计师和程序员，尤其以《吟游诗人故事3：命运窃贼》而闻名。晚年，她因其编程工作而获得认可，特别是在诸如《德军总部3D》和《博德之门》的Macintosh版本等移植作品上。她独立编程的3DO《毁灭战士》移植版也堪称传奇。

海涅曼是 LGBTQ+ 包容性、可访问性和科技领域多元化的坚定倡导者。她在2000年代公开宣布自己是跨性别者，并与游戏行业另一位受人尊敬的人物珍内尔·雅奎斯结婚，雅奎斯于2024年去世。海涅曼获得了Gayming颁发的2025年Gayming偶像奖。

其他游戏开发者和同事纷纷表达哀悼和怀念之情，强调了海涅曼的才华、善良以及对行业的影响。海涅曼要求继续向 GoFundMe 捐款，以资助她的葬礼事宜。

---

## 59. Quake.exe 如何获得 TCP/IP 协议栈

**原文标题**: How Quake.exe got its TCP/IP stack

**原文链接**: [https://fabiensanglard.net/quake_chunnel/index.html](https://fabiensanglard.net/quake_chunnel/index.html)

Quake在DOS和Windows 95下实现TCP/IP网络支持的细节

---

## 60. Show HN: Guts – 将 Golang 类型转换为 TypeScript

**原文标题**: Show HN: Guts – convert Golang types to TypeScript

**原文链接**: [https://github.com/coder/guts](https://github.com/coder/guts)

Guts 是一个 Go 语言库，旨在将 Golang 类型转换为 TypeScript 定义，从而促进前端和后端应用程序之间类型使用的一致性。与现有的 Go 转 TypeScript 工具不同，Guts 旨在作为一个库使用，从而在转换过程中提供更大的程序化控制和自定义。

该库的工作原理是解析 Go 包，遍历抽象语法树 (AST) 以识别定义的类型，然后将这些类型映射到 TypeScript AST。它利用官方 TypeScript 编译器 (通过 goja) 来确保生成的 TypeScript 在语法上正确、语义上有效，并且与语言特性保持同步。

Guts 采用最小转换方法，允许开发人员通过突变进一步完善输出。突变的示例包括将 Go 枚举转换为 TypeScript 字符串字面量类型，而不是 `enum` 对象。该工具允许用户保留注释，以提高可读性和可维护性。

Guts 的主要区别在于其程序化接口，它用基于代码的配置取代了命令行工具的 YAML 配置。这允许更动态和灵活的自定义，这是静态生成器难以支持的。提供了如何使用该库的示例，展示了其易于集成和适应性。

---

## 61. 放弃的意外好处

**原文标题**: The surprising benefits of giving up

**原文链接**: [https://nautil.us/the-surprising-benefits-of-giving-up-1248362/](https://nautil.us/the-surprising-benefits-of-giving-up-1248362/)

莫莉·格里克在《鹦鹉螺》杂志上发表的文章《放弃的意外好处》挑战了坚持不懈的传统观念。 这篇文章重点介绍了研究，表明调整或放弃无法实现的目标可能有利于心理和身体健康。

一项对230多项研究的荟萃分析显示，“目标追求灵活性”，即从无成效的目标中脱离并重新投入新目标的能力，通常是对挑战更合适、更有益的回应。 坚持不可能实现的目标与压力增加、幸福感下降和身体健康问题有关。

该研究确定了影响放弃、调整或追求目标决定的因素，包括负面反馈、“行动危机”和乐观等性格特征。 放弃目标与压力、焦虑和抑郁的减轻有关，而采纳新目标则与改善的社会和身体功能以及目标感和个人成长有关。

作者承认与观察性数据和潜在偏差相关的局限性。 他们强调需要进一步研究，以确定重新思考目标的最佳时机，在坚持不懈与调整方向的需求之间取得平衡。

---

## 62. 微软支持的Veir公司正将超导体引入数据中心。

**原文标题**: Microsoft-backed Veir is bringing superconductors to data centers

**原文链接**: [https://techcrunch.com/2025/11/12/microsoft-backed-veir-targets-data-centers-for-its-megawatt-class-superconductors/](https://techcrunch.com/2025/11/12/microsoft-backed-veir-targets-data-centers-for-its-megawatt-class-superconductors/)

微软支持的初创公司Veir正在调整其用于数据中心的超导电缆，以应对人工智能和计算基础设施日益增长的电力需求。数据中心的电力需求正在迅速增长，可能达到多兆瓦机架，这给现有基础设施带来了压力。Veir的技术使用超导电缆，能够以零能量损耗传输3兆瓦的低压电力，所需空间比铜缆少20倍，传输距离远五倍。

超导体需要冷却到极低的温度，Veir使用液氮来管理这一过程。虽然该公司最初的目标是长距离输电线路，但由于该领域的采用速度较慢，他们转而专注于发展更快的数据中心市场。他们已经调整了他们的技术以适应数据中心的低压需求。

Veir已经建立了一个模拟数据中心来展示其技术，并计划明年在数据中心试用这些电缆，预计将于2027年进行商业发布。根据Veir的首席执行官表示，由于竞争压力，人工智能和数据中心社区有动力寻找解决方案并保持领先。

---

## 63. 朗讯7号 R/E 5ESS电话交换机抢修 (2024)

**原文标题**: Lucent 7 R/E 5ESS Telephone Switch Rescue (2024)

**原文链接**: [http://kev009.com/wp/2024/07/Lucent-5ESS-Rescue/](http://kev009.com/wp/2024/07/Lucent-5ESS-Rescue/)

抢救朗讯7 R/E 5ESS电话交换机的纪实：从亚利桑那大学拆迁前夕的拯救行动

---

## 64. Show HN: 一款巧妙而显眼的电子墨水屏室内空气监测器

**原文标题**: Show HN: A subtly obvious e-paper room air monitor

**原文链接**: [https://www.nicolin-dora.ch/blog/en-epaper-room-air-monitor-part-1/](https://www.nicolin-dora.ch/blog/en-epaper-room-air-monitor-part-1/)

这篇“Show HN”帖子详细介绍了如何创建一个微妙但显眼的电子墨水屏室内空气质量监测器，旨在改善室内空气质量，尤其是在寒冷月份窗户经常关闭的情况下。作者强调了升高的二氧化碳浓度和湿度对健康和注意力的负面影响，并引用了ASHRAE和其他研究。

该监测器使用M5Paper电子墨水屏、Sensirion SCD40传感器（二氧化碳/温度/湿度）和一个用于警报的RGB LED。 Raspberry Pi 4主机托管一个用于可视化空气质量趋势的仪表板，Telegram机器人每天向作者的室友发送摘要，以鼓励积极的空气质量管理。

核心思想是在空气质量良好时保持监测器的不显眼，但在二氧化碳或湿度超过预定义阈值时使其引人注意（通过LED）。 电子墨水屏显示当前读数和建议。 仪表板和Telegram机器人提供长期的意识和改善的动力。

作者计划发布第二篇博文，深入探讨代码，发布GitHub存储库，并欢迎各种贡献，包括代码改进、3D外壳设计、传感器建议和一般反馈。

---

## 65. 数学与计算 (2019) [pdf]

**原文标题**: Mathematics and Computation (2019) [pdf]

**原文链接**: [https://www.math.ias.edu/files/Book-online-Aug0619.pdf](https://www.math.ias.edu/files/Book-online-Aug0619.pdf)

很抱歉，我无法总结这篇文章。您提供的文本无法直接阅读。它似乎是PDF文件的原始内容，包括编码的图像数据和对象流。这是一个字符流，而不是文章的实际内容。我需要文章的纯文本才能提供摘要。

---

## 66. Monotype字体授权勒索

**原文标题**: Monotype font licencing shake-down

**原文链接**: [https://www.insanityworks.org/randomtangent/2025/11/14/monotype-font-licencing-shake-down](https://www.insanityworks.org/randomtangent/2025/11/14/monotype-font-licencing-shake-down)

字体爱好者Ameel讲述了他与Monotype的经历，Monotype通过LinkedIn站内信诈骗式营销，错误指控他的雇主使用了未经授权的字体。

Monotype的“业务拓展代表”声称检测到该雇主的网站/应用程序中嵌入了Monotype字体软件，但没有相应的许可。Ameel感到困惑，因为他不知道正在使用Monotype字体，于是进行了调查，发现该雇主主要使用开源字体Open Sans、Roboto、Asap、Public Sans和一种自定义字体（Network Sans）。合作伙伴管理的网站使用了Proxima Nova，但Monotype已不再出售该字体的许可。

Monotype代表的咄咄逼人的接触方式，向包括采购人员在内的多名员工发送信息，类似于网络钓鱼策略。由于潜在的风险，Ameel被采购部门拉入此事后，发现Monotype的声明是基于有缺陷的自动化检测软件。

该报告错误地将公司应用程序中的“Credit Cards”识别为Monotype字体。Ameel证明它实际上是K-Type的“Credit Card”，该字体与Monotype软件的文件名相似，用于显示卡号输入字段。此外，虽然使用了Proxima Nova，但管理该网站的设计机构拥有有效的Adobe许可证。

Ameel向Monotype提交了他的调查结果，但他们随后试图声称该公司也没有Credit Card的许可证。Ameel反驳说，他们几年前直接从K-Type购买了企业许可证。此后，Monotype停止了联系，凸显了自动化版权侵权检测的缺陷以及质疑可疑声明的重要性。

---

## 67. 实验：让 TypeScript 默认不可变

**原文标题**: Experiment: Making TypeScript immutable-by-default

**原文链接**: [https://evanhahn.com/typescript-immutability-experiment/](https://evanhahn.com/typescript-immutability-experiment/)

Evan Hahn 尝试让 TypeScript 默认不可变，以模仿 Rust 等语言的行为。他的目标是完全通过 TypeScript 类型定义来实现这一点，而不依赖于 linter 或外部工具。他成功地让数组和 Records 默认不可变，但未能对普通的 JavaScript 对象实现这一点。

该实验包括：

1.  **移除内置库：** 在 `tsconfig.json` 中使用 `noLib` 标志，以阻止 TypeScript 使用其默认类型定义。
2.  **创建骨架标准库：** 在 `lib.d.ts` 文件中定义核心类型（如 `Array`、`String` 和 `Object`）的基本接口。
3.  **使数组不可变：** 使用 `readonly` 属性访问器 (`readonly [n: number]: T`) 重新定义 `Array` 接口，以防止默认情况下发生突变，并创建 `MutableArray` 接口以在需要时允许可变数组。
4.  **扩展到 Records：** 类似地，他将 `Record` 定义为默认不可变，并创建 `MutableRecord` 用于可变的键值对。
5.  **普通对象尝试失败：** 他无法仅使用类型定义来阻止普通 JavaScript 对象的突变。

Hahn 鼓励读者尝试解决使 TypeScript 中普通对象默认不可变的问题，并分享他们的解决方案。他还建议可以使用 lint 规则来强制执行不可变性，但他追求的是一种基于“纯”类型定义的解决方案。

---

## 68. Show HN: I built a synth for my daughter

**原文标题**: Show HN: I built a synth for my daughter

**原文链接**: [https://bitsnpieces.dev/posts/a-synth-for-my-daughter/](https://bitsnpieces.dev/posts/a-synth-for-my-daughter/)

生成摘要时出错

---

## 69. How do the pros get someone to leave a cult?

**原文标题**: How do the pros get someone to leave a cult?

**原文链接**: [https://www.theguardian.com/science/2025/nov/19/how-to-leave-a-cult-experts-intervention](https://www.theguardian.com/science/2025/nov/19/how-to-leave-a-cult-experts-intervention)

生成摘要时出错

---

## 70. Raccoons are showing early signs of domestication

**原文标题**: Raccoons are showing early signs of domestication

**原文链接**: [https://www.scientificamerican.com/article/raccoons-are-showing-early-signs-of-domestication/](https://www.scientificamerican.com/article/raccoons-are-showing-early-signs-of-domestication/)

生成摘要时出错

---

## 71. DOE gives Microsoft partner $1B loan to restart Three Mile Island reactor

**原文标题**: DOE gives Microsoft partner $1B loan to restart Three Mile Island reactor

**原文链接**: [https://techcrunch.com/2025/11/18/trump-doe-gives-microsoft-partner-1b-loan-to-restart-three-mile-island-reactor/](https://techcrunch.com/2025/11/18/trump-doe-gives-microsoft-partner-1b-loan-to-restart-three-mile-island-reactor/)

生成摘要时出错

---

## 72. 抛弃你的互斥锁，你值得拥有更好的。

**原文标题**: Ditch your mutex, you deserve better

**原文链接**: [https://chrispenner.ca/posts/mutexes](https://chrispenner.ca/posts/mutexes)

生成摘要时出错

---

## 73. How long can it take to become a US citizen?

**原文标题**: How long can it take to become a US citizen?

**原文链接**: [https://usafacts.org/articles/how-long-can-it-take-to-become-a-us-citizen/](https://usafacts.org/articles/how-long-can-it-take-to-become-a-us-citizen/)

生成摘要时出错

---

## 74. I've wanted to play that 'Killer Shark' arcade game briefly seen in 'Jaws'

**原文标题**: I've wanted to play that 'Killer Shark' arcade game briefly seen in 'Jaws'

**原文链接**: [https://www.remindmagazine.com/article/15694/jaws-arcade-video-game-killer-shark-atari-sega-electromechanical/](https://www.remindmagazine.com/article/15694/jaws-arcade-video-game-killer-shark-atari-sega-electromechanical/)

生成摘要时出错

---

## 75. When 1+1+1 Equals 1

**原文标题**: When 1+1+1 Equals 1

**原文链接**: [https://mathenchant.wordpress.com/2024/12/19/when-111-equals-1/](https://mathenchant.wordpress.com/2024/12/19/when-111-equals-1/)

生成摘要时出错

---

## 76. A down detector for down detector's down detector

**原文标题**: A down detector for down detector's down detector

**原文链接**: [https://downdetectorsdowndetectorsdowndetector.com/](https://downdetectorsdowndetectorsdowndetector.com/)

生成摘要时出错

---

## 77. Unofficial "Tier 4" Rust Target for older Windows versions

**原文标题**: Unofficial "Tier 4" Rust Target for older Windows versions

**原文链接**: [https://github.com/rust9x/rust](https://github.com/rust9x/rust)

生成摘要时出错

---

## 78. Free interactive tool that shows you how PCIe lanes work on motherboards

**原文标题**: Free interactive tool that shows you how PCIe lanes work on motherboards

**原文链接**: [https://mobomaps.com](https://mobomaps.com)

生成摘要时出错

---

## 79. Show HN: Parqeye – A CLI tool to visualize and inspect Parquet files

**原文标题**: Show HN: Parqeye – A CLI tool to visualize and inspect Parquet files

**原文链接**: [https://github.com/kaushiksrini/parqeye](https://github.com/kaushiksrini/parqeye)

生成摘要时出错

---

## 80. When Reverse Proxies Surprise You: Hard Lessons from Operating at Scale

**原文标题**: When Reverse Proxies Surprise You: Hard Lessons from Operating at Scale

**原文链接**: [https://www.infoq.com/articles/scaling-reverse-proxies/](https://www.infoq.com/articles/scaling-reverse-proxies/)

生成摘要时出错

---

## 81. Azure hit by 15 Tbps DDoS attack using 500k IP addresses

**原文标题**: Azure hit by 15 Tbps DDoS attack using 500k IP addresses

**原文链接**: [https://www.bleepingcomputer.com/news/microsoft/microsoft-aisuru-botnet-used-500-000-ips-in-15-tbps-azure-ddos-attack/](https://www.bleepingcomputer.com/news/microsoft/microsoft-aisuru-botnet-used-500-000-ips-in-15-tbps-azure-ddos-attack/)

生成摘要时出错

---

## 82. Do not put your site behind Cloudflare if you don't need to

**原文标题**: Do not put your site behind Cloudflare if you don't need to

**原文链接**: [https://huijzer.xyz/posts/123/do-not-put-your-site-behind-cloudflare-if-you-dont](https://huijzer.xyz/posts/123/do-not-put-your-site-behind-cloudflare-if-you-dont)

生成摘要时出错

---

## 83. Ruby 4.0.0 Preview2

**原文标题**: Ruby 4.0.0 Preview2

**原文链接**: [https://www.ruby-lang.org/en/news/2025/11/17/ruby-4-0-0-preview2-released/](https://www.ruby-lang.org/en/news/2025/11/17/ruby-4-0-0-preview2-released/)

生成摘要时出错

---

## 84. How when AWS was down, we were not

**原文标题**: How when AWS was down, we were not

**原文链接**: [https://authress.io/knowledge-base/articles/2025/11/01/how-we-prevent-aws-downtime-impacts](https://authress.io/knowledge-base/articles/2025/11/01/how-we-prevent-aws-downtime-impacts)

生成摘要时出错

---

## 85. Show HN: ESPectre – Motion detection based on Wi-Fi spectre analysis

**原文标题**: Show HN: ESPectre – Motion detection based on Wi-Fi spectre analysis

**原文链接**: [https://github.com/francescopace/espectre](https://github.com/francescopace/espectre)

生成摘要时出错

---

## 86. Exploring the Limits of Large Language Models as Quant Traders

**原文标题**: Exploring the Limits of Large Language Models as Quant Traders

**原文链接**: [https://nof1.ai/blog/TechPost1](https://nof1.ai/blog/TechPost1)

生成摘要时出错

---

## 87. Silverbullet: Personal productivity platform built with Markdown and Lua

**原文标题**: Silverbullet: Personal productivity platform built with Markdown and Lua

**原文链接**: [https://github.com/silverbulletmd/silverbullet](https://github.com/silverbulletmd/silverbullet)

生成摘要时出错

---

## 88. People are using iPad OS features on their iPhones

**原文标题**: People are using iPad OS features on their iPhones

**原文链接**: [https://idevicecentral.com/ios-customization/how-to-enable-ipad-features-like-multitasking-stage-manager-on-iphone-via-mobilegestalt/](https://idevicecentral.com/ios-customization/how-to-enable-ipad-features-like-multitasking-stage-manager-on-iphone-via-mobilegestalt/)

生成摘要时出错

---

## 89. Aldous Huxley predicts Adderall and champions alternative therapies

**原文标题**: Aldous Huxley predicts Adderall and champions alternative therapies

**原文链接**: [https://angadh.com/inkhaven-7](https://angadh.com/inkhaven-7)

生成摘要时出错

---

## 90. How many video games include a marriage proposal? At least one

**原文标题**: How many video games include a marriage proposal? At least one

**原文链接**: [https://32bits.substack.com/p/under-the-microscope-ncaa-basketball](https://32bits.substack.com/p/under-the-microscope-ncaa-basketball)

生成摘要时出错

---

## 91. Windows 11 adds AI agent that runs in background with access to personal folders

**原文标题**: Windows 11 adds AI agent that runs in background with access to personal folders

**原文链接**: [https://www.windowslatest.com/2025/11/18/windows-11-to-add-an-ai-agent-that-runs-in-background-with-access-to-personal-folders-warns-of-security-risk/](https://www.windowslatest.com/2025/11/18/windows-11-to-add-an-ai-agent-that-runs-in-background-with-access-to-personal-folders-warns-of-security-risk/)

生成摘要时出错

---

## 92. My stages of learning to be a socially normal person

**原文标题**: My stages of learning to be a socially normal person

**原文链接**: [https://sashachapin.substack.com/p/my-six-stages-of-learning-to-be-a](https://sashachapin.substack.com/p/my-six-stages-of-learning-to-be-a)

生成摘要时出错

---

## 93. Looking for Hidden Gems in Scientific Literature

**原文标题**: Looking for Hidden Gems in Scientific Literature

**原文链接**: [https://elicit.com/blog/literature-based-discovery](https://elicit.com/blog/literature-based-discovery)

生成摘要时出错

---

## 94. Quantum physicists have shrunk and "de-censored" DeepSeek R1

**原文标题**: Quantum physicists have shrunk and "de-censored" DeepSeek R1

**原文链接**: [https://www.technologyreview.com/2025/11/19/1128119/quantum-physicists-compress-and-deconsor-deepseekr1/](https://www.technologyreview.com/2025/11/19/1128119/quantum-physicists-compress-and-deconsor-deepseekr1/)

生成摘要时出错

---

## 95. A new book about the origins of Effective Altruism

**原文标题**: A new book about the origins of Effective Altruism

**原文链接**: [https://newrepublic.com/article/202433/happened-effective-altruism](https://newrepublic.com/article/202433/happened-effective-altruism)

生成摘要时出错

---

## 96. Beauty in/of mathematics: tessellations and their formulas

**原文标题**: Beauty in/of mathematics: tessellations and their formulas

**原文链接**: [https://www.tandfonline.com/doi/full/10.1080/00036811.2025.2510472](https://www.tandfonline.com/doi/full/10.1080/00036811.2025.2510472)

生成摘要时出错

---

## 97. Better pre-commit, re-engineered in Rust

**原文标题**: Better pre-commit, re-engineered in Rust

**原文链接**: [https://prek.j178.dev/](https://prek.j178.dev/)

生成摘要时出错

---

## 98. A 'small' vanilla Kubernetes install on NixOS

**原文标题**: A 'small' vanilla Kubernetes install on NixOS

**原文链接**: [https://stephank.nl/p/2025-11-17-a-small-vanilla-kubernetes-install-on-nixos.html](https://stephank.nl/p/2025-11-17-a-small-vanilla-kubernetes-install-on-nixos.html)

生成摘要时出错

---

## 99. Show HN: Continuous Claude – run Claude Code in a loop

**原文标题**: Show HN: Continuous Claude – run Claude Code in a loop

**原文链接**: [https://github.com/AnandChowdhary/continuous-claude](https://github.com/AnandChowdhary/continuous-claude)

生成摘要时出错

---

## 100. Jeff Bezos creates A.I. startup where he will be co-chief executive

**原文标题**: Jeff Bezos creates A.I. startup where he will be co-chief executive

**原文链接**: [https://www.nytimes.com/2025/11/17/technology/bezos-project-prometheus.html](https://www.nytimes.com/2025/11/17/technology/bezos-project-prometheus.html)

生成摘要时出错

---

