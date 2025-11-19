# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-19.md)

*最后自动更新时间: 2025-11-19 17:51:49*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 2 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 3 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 4 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 5 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 6 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 7 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 8 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 9 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 10 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 11 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 12 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 13 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 14 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 15 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 16 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 17 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 18 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 19 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 20 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 21 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 22 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 23 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 24 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 25 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 26 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 27 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 28 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 29 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 30 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 31 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 32 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 33 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 34 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 35 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 36 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 37 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 38 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 39 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 40 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 41 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 42 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 43 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 44 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 45 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 46 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 47 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 48 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 49 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 50 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 51 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 52 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 53 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 54 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 55 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 56 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 57 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 58 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 59 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 60 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 61 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 62 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 63 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 64 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 65 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 66 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 67 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 68 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 69 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 70 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 71 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 72 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 73 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 74 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 75 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 76 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 77 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 78 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 79 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 80 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 81 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 82 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 83 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 84 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 85 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 86 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 87 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 88 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 89 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 90 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 91 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 92 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 93 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 94 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 95 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 96 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 97 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 98 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 99 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 100 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 101 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 102 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 103 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 104 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 105 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 106 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 107 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 108 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 109 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 110 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 111 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 112 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 113 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 114 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 115 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 116 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 117 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 118 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 119 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 120 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 121 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 122 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 123 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 124 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 125 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 126 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 127 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 128 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 129 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 130 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 131 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 132 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 133 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 134 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 135 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 136 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 137 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 138 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 139 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 140 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 141 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 142 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 143 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 144 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 145 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 146 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 147 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 148 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 149 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 150 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 151 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 152 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 153 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 154 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 155 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 156 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 157 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 158 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 159 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 160 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 161 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 162 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 163 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 164 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 165 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 166 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 167 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 168 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 169 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 170 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 171 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 172 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 173 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 174 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 175 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 176 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 177 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 178 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 179 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 180 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 181 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 182 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 183 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 184 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 185 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 186 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 187 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 188 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 189 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 190 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 191 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 192 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 193 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 194 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 195 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 196 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 197 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 198 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 199 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 200 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 201 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 202 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 203 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 204 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 205 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 206 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 207 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 208 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 209 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 210 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 211 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 212 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 213 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 214 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 215 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 216 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 217 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 218 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 219 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 220 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 221 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 222 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 223 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 224 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 225 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 226 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 227 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 228 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 229 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 230 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 231 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 232 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 233 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 234 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 235 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 236 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 237 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 238 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 239 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 240 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 241 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 242 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 243 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 244 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
