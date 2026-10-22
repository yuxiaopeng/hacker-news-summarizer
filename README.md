# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-10-22.md)

*最后自动更新时间: 2026-10-22 20:51:00*
## 1. Quad9 (DNS 解析器) 退出法国

**原文标题**: Quad9 (DNS Resolver) to Exit France

**原文链接**: [https://quad9.net/news/blog/au-revoir-france/](https://quad9.net/news/blog/au-revoir-france/)

**摘要：Quad9 将停止在法国提供服务**

总部位于瑞士的非营利性 DNS 解析服务商 Quad9 宣布，将于 **2026 年 11 月 24 日**起正式停止在法国的业务。这一决定源于法国法院的一项裁决，该裁决支持 beIN Sports 的诉求，要求 Quad9 屏蔽与版权侵权相关的特定域名。

**核心冲突与原则**
Quad9 坚持认为 DNS 解析是一种中立、被动的服务。该机构拒绝修改 DNS 响应或向用户“撒谎”，认为此类强制指令违反了其保护互联网完整性、隐私和网络安全的使命。尽管法院已将每日罚金降至 1,000 欧元，但 Quad9 断言这是一个原则问题，而非财务问题。

**技术与法律挑战**
该机构辩称，在技术上无法实现合规。实施“全球屏蔽”会不当地将法国法律强加于国际用户，而“地理屏蔽”则很容易通过 VPN 绕过——这一方式此前曾导致 Quad9 在德国因蔑视法庭而被罚款。此外，由于 Quad9 不收集用户数据，识别并隔离法国用户与其“隐私优先”的架构背道而驰。

**影响与展望**
Quad9 强调，其在法国正面临约 20 起类似的未决诉讼。他们认为，DNS 屏蔽是打击盗版的无效工具，既无法移除源内容，又会让数百万法国用户暴露在原本可由其服务过滤的网络威胁之下。

**呼吁采取行动**
Quad9 将撤出法国视为保护其全球生存的必要步骤，并敦促法国公民联系立法机构和监管机构 ARCOM。他们警告称，允许私营公司主导 DNS 过滤将为审查制度开创危险先例，并损害法国的数字主权和互联网自由。

---

## 2. OpenShell – 面向自主 AI 智能体集群的安全私密运行时

**原文标题**: OpenShell – A safe, private runtime for fleets of autonomous AI agents

**原文链接**: [https://github.com/NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)

**OpenShell** is an open-source, private runtime (under the Apache License 2.0) designed by NVIDIA to securely manage fleets of autonomous AI agents. It addresses the security risks associated with agents performing tasks like file manipulation, package installation, and API calls by providing a restricted environment that prevents unauthorized access to sensitive data and networks.

The platform relies on two core security pillars:
1.  **Kernel-Level Enforcement:** Each agent operates within an isolated sandbox. OpenShell instruments the kernel to monitor and restrict system calls, file access, and network connections. Notably, agents never see raw credentials; OpenShell injects them only into requests destined for pre-approved endpoints.
2.  **Formally Verified Policies:** Before any policy changes are applied, the system uses formal verification to identify potential security risks, such as unauthorized host access, requiring human approval for high-risk changes.

**Key Features and Ecosystem:**
*   **Architecture:** Comprises a gateway (control plane), supervisor, and sandboxes.
*   **Extensibility:** Supports "Skills" that teach agents to manage the CLI and write their own policies, plus middleware and compute driver intercepts.
*   **Deployment:** Compatible with Linux, macOS (Apple Silicon), and Windows (WSL 2). It supports Kubernetes via Helm and provides SDKs for Python, TypeScript, Go, and Rust.
*   **Development:** Built using agent-driven workflows, it includes optional anonymous telemetry and a robust community framework for bug reports and feature requests.

In summary, OpenShell provides the infrastructure necessary to grant AI agents significant operational utility while maintaining strict enterprise-grade security and human oversight.

---

## 3. 准备在德国运营 GNU Taler

**原文标题**: Getting ready to operate GNU Taler in Germany

**原文链接**: [https://www.taler.net/en/news/2026-13.html](https://www.taler.net/en/news/2026-13.html)

生成摘要时出错

---

## 4. Show HN：在安卓设备上运行完整的 iOS 16.5 固件

**原文标题**: Show HN: Run full iOS 16.5 firmware on Android Devices

**原文链接**: [https://github.com/oosexgang/hackios-xnu-kernel](https://github.com/oosexgang/hackios-xnu-kernel)

**HackiOS** 是由 **OOSEX GANG** 发起的一项独立研究项目，旨在让苹果开源的 XNU 内核（16.5 版本）在安卓硬件和 QEMU 上引导运行。该项目已成功在 **POCO X5 Pro 5G**（骁龙 778G）及 aarch64 Linux 环境下运行了未经修改的 iOS 16.5 用户空间——包括 launchd、SpringBoard 及原生应用。

项目的技术核心涉及自定义 EFI 加载器、UEFI 移植以及专用驱动替代方案。为了桥接硬件差异，团队利用 Linux Wi-Fi 驱动兼容层以及 Mesa/freedreno 驱动，使 Adreno 642L GPU 能够支持 CoreAnimation。在 POCO 设备上，系统通过 `fastboot boot` 完全在 RAM 中运行，不向手机的永久存储写入任何文件，重启后即可恢复至安卓系统。

**关键状态：**
*   **正常工作：** 锁屏、系统手势、Wi-Fi、音频、相机（拍照）以及 Safari、时钟和备忘录等原生应用。
*   **开发中：** Metal 支持（GPU 着色器）已部分实现。
*   **暂不可用：** 蜂窝网络、蓝牙、充电，以及 Apple ID/App Store（由于缺少安全隔区 Secure Enclave/FairPlay 支持）。

HackiOS 的定位是“研究平台”而非日常使用的 ROM。为遵守法律规范，其代码仓库不包含任何苹果拥有版权的文件，而是提供脚本从苹果官方服务器直接下载并提取必要组件。该项目采用苹果公共源代码许可证（APSL）2.0 协议开源，并提供了将内核移植到其他安卓设备的文档。

---

## 5. 人工智能与科学公地的圈地

**原文标题**: AI and the Enclosure of the Scientific Commons

**原文链接**: [https://arxiv.org/abs/2610.27251](https://arxiv.org/abs/2610.27251)

在《人工智能与科学公地围蔽》（AI and the Enclosure of the Scientific Commons）一文中，哈佛-史密松天体物理中心的 P. K. G. Williams 将科学文献的现状与工业化前英国的农业“公地”进行了历史类比。

Williams 将科学文献定义为一种“信息公地”——这是一项共享的、无形的资源，也是人类最伟大的成就之一。然而，他警告说，这一资源目前正面临类似于历史上“圈地运动”（1600–1800年）的威胁，在那段时期，公有土地被系统性地转变为私有财产。

作者将众所周知的“公地悲剧”（资源因过度使用而枯竭）与“围蔽”（资源被攫取为私人财富）进行了关键区分。他认为，人工智能提供了围蔽数字信息公地所需的特定技术能力，而在此之前，这些信息因过于庞大和分散而难以被有效私有化。

根据 Williams 的观点，这种由人工智能驱动的围蔽主要表现为两种方式：
1. **财富攫取：** 将科学界的集体产出转化为私有的、专有的人工智能模型。
2. **系统性退化：** 通过“人工智能垃圾内容”（slop spam）或人工智能生成的低质量内容的泛滥，削弱科学的社会结构（如同行评审和信任机制）。

最终，本文提供了一个框架，用于理解科学界许多人共同感到的那种“不祥的预感”。它指出，人工智能不仅代表着一种技术转变，更是对数世纪以来定义了科学进步的开放、共有生活方式的根本性攻击。

---

## 6. Show HN：UI 微交互 AI 提示词

**原文标题**: Show HN: UI micro interactions prompts for AI

**原文链接**: [https://www.typeui.sh/micro-interactions](https://www.typeui.sh/micro-interactions)

**TypeUI: Micro-interactions** 是一项专业资源，旨在帮助开发者和设计师利用 v0、Claude Artifacts、Cursor 和 Bolt.new 等 AI 代码助手，创作高质量的 UI 动画。

该平台提供了一个精选的“即插即用”提示词库，专门用于生成复杂的微交互效果。其中包括磁性按钮、发光悬停状态、动态导航标签、流畅的加载序列以及交互式卡片。这些组件主要针对现代 Web 技术栈进行了优化，利用了 **React、Tailwind CSS 和 Framer Motion**。

TypeUI 的核心价值在于弥合“描述差距”。虽然 AI 模型擅长编写代码，但除非给出极其具体的技术指令，否则往往难以生成精致且专业级的动画。TypeUI 提供了这些优化后的提示词，让用户无需手动编写复杂的 CSS 或动画逻辑，即可实现具有“高级感”的 UI 细节。

**主要特性包括：**
*   **开箱即用的提示词：** 经过精细调整的技术描述，旨在从大语言模型（LLM）中获得最佳输出效果。
*   **可视化预览：** 交互效果的实时示例，让用户明确 AI 应该生成的内容。
*   **专注于精致的 UX：** 针对设计的“最后 10%”——即那些让界面更具响应感和高端感的细微动作。

最终，该网站充当了创意意图与 AI 执行之间的桥梁，为希望快速提升应用审美深度的开发者简化了工作流程。

---

## 7. eMudhra将退出全球SSL/TLS证书业务

**原文标题**: eMudhra to exit global SSL/TLS certificate business

**原文链接**: [https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business](https://emudhra.com/en/press-release/emudhra-to-exit-global-ssl-tls-certificate-business)

2026年10月22日，eMudhra Limited宣布决定自愿退出全球SSL/TLS证书业务，以进一步专注于其核心企业解决方案及其他数字信任服务。

这一决定是在近期发生一起涉及其全球SSL/TLS证书的安全事件后做出的。尽管该公司在14小时内解决了该问题——撤销了受影响的证书颁发机构（CA），且未发生任何数据泄露或终端实体证书受损的情况——但董事会认为，过度且不成比例的社交媒体舆论压力已超过了该业务的实际价值。

从战略层面看，SSL/TLS证书仅占eMudhra全球营收的1%。公司指出，日益增加的合规成本、高度的复杂性以及免费证书提供商的普及，均显著降低了该特定领域的投资回报率。

为确保平稳过渡，eMudhra将：
*   与浏览器项目合作，在过渡完成前维持G1 RSA根证书。
*   联系受影响的客户，通过合作伙伴提供免费的更换证书。
*   维持撤销及状态查询服务，直至所有现有证书过期。
*   履行对浏览器根证书项目的所有剩余承诺，包括提交完整的根因分析报告。

公司强调，其核心业务运营不受影响。这包括全球数字签名证书（DSC）、eSign服务、企业级PKI解决方案（emCA、CertiNext）、emSigner以及身份认证平台（SecurePass、emAS）。这些服务在独立的基础设施上运行，将继续正常运作。展望未来，eMudhra计划将其资源重新投入到高价值的数字身份和安全解决方案中，为遍布35个多国家的全球客户提供服务。

---

## 8. Award-Winning AI Literature

**原文标题**: Award-Winning AI Literature

**原文链接**: [https://jamesyu.org/award-winning-ai-literature/](https://jamesyu.org/award-winning-ai-literature/)

生成摘要时出错

---

## 9. What Is Gridifcation

**原文标题**: What Is Gridifcation

**原文链接**: [https://musicalform.substack.com/p/what-is-gridifcation](https://musicalform.substack.com/p/what-is-gridifcation)

In the article "What Is Gridification," the author explores the transition of music production from fluid, human-driven performances to rigid, mathematically precise sequences aligned with a digital "grid." 

**Definition and Context**
Gridification refers to the process of using Digital Audio Workstations (DAWs) to quantize MIDI and audio so that every note falls exactly on the beat. While early music was recorded live with natural fluctuations in tempo, the rise of drum machines and sequencers in the 1980s introduced a level of rhythmic perfection that has since become the industry standard.

**The Benefits**
The author notes that gridification offers significant practical advantages. It simplifies the editing process, allows for seamless looping and layering, and makes it easy for producers to collaborate across different locations. In genres like EDM, pop, and hip-hop, the "perfect" timing of the grid defines the modern aesthetic and ensures tracks are "club-ready."

**The Aesthetic Cost**
The primary critique presented is the loss of "groove" or "human feel." By eliminating micro-timing—the subtle tendency of a musician to play slightly ahead of or behind the beat—gridification can make music sound sterile, robotic, and repetitive. This "push and pull" is historically what gave genres like jazz, soul, and rock their emotional energy.

**Conclusion**
The article suggests that gridification has fundamentally altered our ears; modern listeners have become so accustomed to rhythmic perfection that natural human timing can now sound "wrong" or "unprofessional." Ultimately, the author views the grid as a powerful tool but warns that over-reliance on it risks stripping music of the organic imperfections that make it feel alive. To maintain musicality, producers must learn when to use the grid and when to let the music breathe.

---

## 10. Woman faces six years in prison over Cash App account she never opened

**原文标题**: Woman faces six years in prison over Cash App account she never opened

**原文链接**: [https://www.techspot.com/news/114296-woman-spends-three-nights-jail-faces-six-years.html](https://www.techspot.com/news/114296-woman-spends-three-nights-jail-faces-six-years.html)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-10-22](output/hacker_news_summary_2026-10-22.md) |
| 2 | [2026-10-21](output/hacker_news_summary_2026-10-21.md) |
| 3 | [2026-10-20](output/hacker_news_summary_2026-10-20.md) |
| 4 | [2026-10-17](output/hacker_news_summary_2026-10-17.md) |
| 5 | [2026-10-18](output/hacker_news_summary_2026-10-18.md) |
| 6 | [2026-10-15](output/hacker_news_summary_2026-10-15.md) |
| 7 | [2026-10-16](output/hacker_news_summary_2026-10-16.md) |
| 8 | [2026-10-19](output/hacker_news_summary_2026-10-19.md) |
| 9 | [2026-10-13](output/hacker_news_summary_2026-10-13.md) |
| 10 | [2026-10-14](output/hacker_news_summary_2026-10-14.md) |
| 11 | [2026-10-12](output/hacker_news_summary_2026-10-12.md) |
| 12 | [2026-10-10](output/hacker_news_summary_2026-10-10.md) |
| 13 | [2026-10-09](output/hacker_news_summary_2026-10-09.md) |
| 14 | [2026-10-11](output/hacker_news_summary_2026-10-11.md) |
| 15 | [2026-10-08](output/hacker_news_summary_2026-10-08.md) |
| 16 | [2026-10-07](output/hacker_news_summary_2026-10-07.md) |
| 17 | [2026-10-06](output/hacker_news_summary_2026-10-06.md) |
| 18 | [2026-10-04](output/hacker_news_summary_2026-10-04.md) |
| 19 | [2026-10-05](output/hacker_news_summary_2026-10-05.md) |
| 20 | [2026-10-01](output/hacker_news_summary_2026-10-01.md) |
| 21 | [2026-09-28](output/hacker_news_summary_2026-09-28.md) |
| 22 | [2026-09-29](output/hacker_news_summary_2026-09-29.md) |
| 23 | [2026-09-30](output/hacker_news_summary_2026-09-30.md) |
| 24 | [2026-10-02](output/hacker_news_summary_2026-10-02.md) |
| 25 | [2026-10-03](output/hacker_news_summary_2026-10-03.md) |
| 26 | [2026-09-24](output/hacker_news_summary_2026-09-24.md) |
| 27 | [2026-09-23](output/hacker_news_summary_2026-09-23.md) |
| 28 | [2026-09-26](output/hacker_news_summary_2026-09-26.md) |
| 29 | [2026-09-27](output/hacker_news_summary_2026-09-27.md) |
| 30 | [2026-09-22](output/hacker_news_summary_2026-09-22.md) |
| 31 | [2026-09-25](output/hacker_news_summary_2026-09-25.md) |
| 32 | [2026-09-21](output/hacker_news_summary_2026-09-21.md) |
| 33 | [2026-09-20](output/hacker_news_summary_2026-09-20.md) |
| 34 | [2026-09-16](output/hacker_news_summary_2026-09-16.md) |
| 35 | [2026-09-17](output/hacker_news_summary_2026-09-17.md) |
| 36 | [2026-09-19](output/hacker_news_summary_2026-09-19.md) |
| 37 | [2026-09-18](output/hacker_news_summary_2026-09-18.md) |
| 38 | [2026-09-13](output/hacker_news_summary_2026-09-13.md) |
| 39 | [2026-09-14](output/hacker_news_summary_2026-09-14.md) |
| 40 | [2026-09-11](output/hacker_news_summary_2026-09-11.md) |
| 41 | [2026-09-12](output/hacker_news_summary_2026-09-12.md) |
| 42 | [2026-09-15](output/hacker_news_summary_2026-09-15.md) |
| 43 | [2026-09-09](output/hacker_news_summary_2026-09-09.md) |
| 44 | [2026-09-10](output/hacker_news_summary_2026-09-10.md) |
| 45 | [2026-09-08](output/hacker_news_summary_2026-09-08.md) |
| 46 | [2026-09-05](output/hacker_news_summary_2026-09-05.md) |
| 47 | [2026-09-07](output/hacker_news_summary_2026-09-07.md) |
| 48 | [2026-09-06](output/hacker_news_summary_2026-09-06.md) |
| 49 | [2026-09-03](output/hacker_news_summary_2026-09-03.md) |
| 50 | [2026-09-02](output/hacker_news_summary_2026-09-02.md) |
| 51 | [2026-08-31](output/hacker_news_summary_2026-08-31.md) |
| 52 | [2026-09-04](output/hacker_news_summary_2026-09-04.md) |
| 53 | [2026-09-01](output/hacker_news_summary_2026-09-01.md) |
| 54 | [2026-08-25](output/hacker_news_summary_2026-08-25.md) |
| 55 | [2026-08-28](output/hacker_news_summary_2026-08-28.md) |
| 56 | [2026-08-29](output/hacker_news_summary_2026-08-29.md) |
| 57 | [2026-08-24](output/hacker_news_summary_2026-08-24.md) |
| 58 | [2026-08-30](output/hacker_news_summary_2026-08-30.md) |
| 59 | [2026-08-26](output/hacker_news_summary_2026-08-26.md) |
| 60 | [2026-08-22](output/hacker_news_summary_2026-08-22.md) |
| 61 | [2026-08-19](output/hacker_news_summary_2026-08-19.md) |
| 62 | [2026-08-20](output/hacker_news_summary_2026-08-20.md) |
| 63 | [2026-08-23](output/hacker_news_summary_2026-08-23.md) |
| 64 | [2026-08-21](output/hacker_news_summary_2026-08-21.md) |
| 65 | [2026-08-14](output/hacker_news_summary_2026-08-14.md) |
| 66 | [2026-08-16](output/hacker_news_summary_2026-08-16.md) |
| 67 | [2026-08-17](output/hacker_news_summary_2026-08-17.md) |
| 68 | [2026-08-18](output/hacker_news_summary_2026-08-18.md) |
| 69 | [2026-08-15](output/hacker_news_summary_2026-08-15.md) |
| 70 | [2026-08-12](output/hacker_news_summary_2026-08-12.md) |
| 71 | [2026-08-11](output/hacker_news_summary_2026-08-11.md) |
| 72 | [2026-08-10](output/hacker_news_summary_2026-08-10.md) |
| 73 | [2026-08-09](output/hacker_news_summary_2026-08-09.md) |
| 74 | [2026-08-08](output/hacker_news_summary_2026-08-08.md) |
| 75 | [2026-08-13](output/hacker_news_summary_2026-08-13.md) |
| 76 | [2026-08-04](output/hacker_news_summary_2026-08-04.md) |
| 77 | [2026-08-07](output/hacker_news_summary_2026-08-07.md) |
| 78 | [2026-08-05](output/hacker_news_summary_2026-08-05.md) |
| 79 | [2026-08-02](output/hacker_news_summary_2026-08-02.md) |
| 80 | [2026-08-03](output/hacker_news_summary_2026-08-03.md) |
| 81 | [2026-07-28](output/hacker_news_summary_2026-07-28.md) |
| 82 | [2026-08-01](output/hacker_news_summary_2026-08-01.md) |
| 83 | [2026-07-30](output/hacker_news_summary_2026-07-30.md) |
| 84 | [2026-07-29](output/hacker_news_summary_2026-07-29.md) |
| 85 | [2026-07-31](output/hacker_news_summary_2026-07-31.md) |
| 86 | [2026-07-27](output/hacker_news_summary_2026-07-27.md) |
| 87 | [2026-07-26](output/hacker_news_summary_2026-07-26.md) |
| 88 | [2026-07-22](output/hacker_news_summary_2026-07-22.md) |
| 89 | [2026-07-25](output/hacker_news_summary_2026-07-25.md) |
| 90 | [2026-07-24](output/hacker_news_summary_2026-07-24.md) |
| 91 | [2026-07-23](output/hacker_news_summary_2026-07-23.md) |
| 92 | [2026-07-20](output/hacker_news_summary_2026-07-20.md) |
| 93 | [2026-07-16](output/hacker_news_summary_2026-07-16.md) |
| 94 | [2026-07-18](output/hacker_news_summary_2026-07-18.md) |
| 95 | [2026-07-17](output/hacker_news_summary_2026-07-17.md) |
| 96 | [2026-07-21](output/hacker_news_summary_2026-07-21.md) |
| 97 | [2026-07-19](output/hacker_news_summary_2026-07-19.md) |
| 98 | [2026-07-12](output/hacker_news_summary_2026-07-12.md) |
| 99 | [2026-07-14](output/hacker_news_summary_2026-07-14.md) |
| 100 | [2026-07-10](output/hacker_news_summary_2026-07-10.md) |
| 101 | [2026-07-15](output/hacker_news_summary_2026-07-15.md) |
| 102 | [2026-07-13](output/hacker_news_summary_2026-07-13.md) |
| 103 | [2026-07-11](output/hacker_news_summary_2026-07-11.md) |
| 104 | [2026-07-07](output/hacker_news_summary_2026-07-07.md) |
| 105 | [2026-07-05](output/hacker_news_summary_2026-07-05.md) |
| 106 | [2026-07-06](output/hacker_news_summary_2026-07-06.md) |
| 107 | [2026-07-09](output/hacker_news_summary_2026-07-09.md) |
| 108 | [2026-07-08](output/hacker_news_summary_2026-07-08.md) |
| 109 | [2026-07-04](output/hacker_news_summary_2026-07-04.md) |
| 110 | [2026-06-29](output/hacker_news_summary_2026-06-29.md) |
| 111 | [2026-07-02](output/hacker_news_summary_2026-07-02.md) |
| 112 | [2026-07-03](output/hacker_news_summary_2026-07-03.md) |
| 113 | [2026-06-30](output/hacker_news_summary_2026-06-30.md) |
| 114 | [2026-07-01](output/hacker_news_summary_2026-07-01.md) |
| 115 | [2026-06-28](output/hacker_news_summary_2026-06-28.md) |
| 116 | [2026-06-24](output/hacker_news_summary_2026-06-24.md) |
| 117 | [2026-06-23](output/hacker_news_summary_2026-06-23.md) |
| 118 | [2026-06-27](output/hacker_news_summary_2026-06-27.md) |
| 119 | [2026-06-22](output/hacker_news_summary_2026-06-22.md) |
| 120 | [2026-06-25](output/hacker_news_summary_2026-06-25.md) |
| 121 | [2026-06-26](output/hacker_news_summary_2026-06-26.md) |
| 122 | [2026-06-18](output/hacker_news_summary_2026-06-18.md) |
| 123 | [2026-06-16](output/hacker_news_summary_2026-06-16.md) |
| 124 | [2026-06-21](output/hacker_news_summary_2026-06-21.md) |
| 125 | [2026-06-19](output/hacker_news_summary_2026-06-19.md) |
| 126 | [2026-06-17](output/hacker_news_summary_2026-06-17.md) |
| 127 | [2026-06-20](output/hacker_news_summary_2026-06-20.md) |
| 128 | [2026-06-13](output/hacker_news_summary_2026-06-13.md) |
| 129 | [2026-06-12](output/hacker_news_summary_2026-06-12.md) |
| 130 | [2026-06-14](output/hacker_news_summary_2026-06-14.md) |
| 131 | [2026-06-15](output/hacker_news_summary_2026-06-15.md) |
| 132 | [2026-06-11](output/hacker_news_summary_2026-06-11.md) |
| 133 | [2026-06-06](output/hacker_news_summary_2026-06-06.md) |
| 134 | [2026-06-07](output/hacker_news_summary_2026-06-07.md) |
| 135 | [2026-06-05](output/hacker_news_summary_2026-06-05.md) |
| 136 | [2026-06-08](output/hacker_news_summary_2026-06-08.md) |
| 137 | [2026-06-10](output/hacker_news_summary_2026-06-10.md) |
| 138 | [2026-06-09](output/hacker_news_summary_2026-06-09.md) |
| 139 | [2026-06-04](output/hacker_news_summary_2026-06-04.md) |
| 140 | [2026-06-03](output/hacker_news_summary_2026-06-03.md) |
| 141 | [2026-05-31](output/hacker_news_summary_2026-05-31.md) |
| 142 | [2026-06-01](output/hacker_news_summary_2026-06-01.md) |
| 143 | [2026-06-02](output/hacker_news_summary_2026-06-02.md) |
| 144 | [2026-05-30](output/hacker_news_summary_2026-05-30.md) |
| 145 | [2026-05-27](output/hacker_news_summary_2026-05-27.md) |
| 146 | [2026-05-28](output/hacker_news_summary_2026-05-28.md) |
| 147 | [2026-05-25](output/hacker_news_summary_2026-05-25.md) |
| 148 | [2026-05-26](output/hacker_news_summary_2026-05-26.md) |
| 149 | [2026-05-29](output/hacker_news_summary_2026-05-29.md) |
| 150 | [2026-05-20](output/hacker_news_summary_2026-05-20.md) |
| 151 | [2026-05-24](output/hacker_news_summary_2026-05-24.md) |
| 152 | [2026-05-23](output/hacker_news_summary_2026-05-23.md) |
| 153 | [2026-05-21](output/hacker_news_summary_2026-05-21.md) |
| 154 | [2026-05-22](output/hacker_news_summary_2026-05-22.md) |
| 155 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 156 | [2026-05-17](output/hacker_news_summary_2026-05-17.md) |
| 157 | [2026-05-16](output/hacker_news_summary_2026-05-16.md) |
| 158 | [2026-05-18](output/hacker_news_summary_2026-05-18.md) |
| 159 | [2026-05-19](output/hacker_news_summary_2026-05-19.md) |
| 160 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 161 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 162 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 163 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 164 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 165 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 166 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 167 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 168 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 169 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 170 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 171 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 172 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 173 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 174 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 175 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 176 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 177 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 178 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 179 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 180 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 181 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 182 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 183 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 184 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 185 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 186 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 187 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 188 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 189 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 190 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 191 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 192 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 193 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 194 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 195 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 196 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 197 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 198 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 199 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 200 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 201 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 202 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 203 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 204 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 205 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 206 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 207 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 208 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 209 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 210 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 211 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 212 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 213 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 214 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 215 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 216 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 217 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 218 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 219 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 220 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 221 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 222 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 223 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 224 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 225 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 226 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 227 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 228 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 229 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 230 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 231 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 232 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 233 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 234 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 235 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 236 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 237 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 238 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 239 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 240 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 241 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 242 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 243 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 244 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 245 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 246 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 247 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 248 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 249 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 250 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 251 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 252 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 253 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 254 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 255 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 256 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 257 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 258 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 259 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 260 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 261 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 262 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 263 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 264 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 265 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 266 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 267 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 268 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 269 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 270 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 271 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 272 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 273 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 274 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 275 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 276 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 277 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 278 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 279 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 280 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 281 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 282 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 283 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 284 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 285 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 286 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 287 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 288 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 289 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 290 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 291 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 292 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 293 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 294 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 295 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 296 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 297 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 298 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 299 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 300 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 301 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 302 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 303 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 304 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 305 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 306 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 307 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 308 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 309 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 310 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 311 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 312 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 313 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 314 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 315 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 316 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 317 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 318 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 319 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 320 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 321 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 322 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 323 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 324 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 325 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 326 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 327 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 328 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 329 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 330 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 331 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 332 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 333 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 334 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 335 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 336 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 337 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 338 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 339 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 340 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 341 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 342 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 343 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 344 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 345 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 346 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 347 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 348 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 349 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 350 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 351 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 352 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 353 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 354 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 355 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 356 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 357 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 358 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 359 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 360 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 361 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 362 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 363 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 364 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 365 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 366 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 367 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 368 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 369 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 370 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 371 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 372 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 373 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 374 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 375 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 376 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 377 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 378 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 379 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 380 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 381 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 382 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 383 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 384 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 385 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 386 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 387 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 388 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 389 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 390 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 391 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 392 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 393 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 394 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 395 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 396 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 397 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 398 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 399 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 400 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 401 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 402 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 403 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 404 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 405 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 406 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 407 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 408 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 409 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 410 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 411 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 412 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 413 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 414 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 415 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 416 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 417 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 418 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 419 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 420 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 421 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 422 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 423 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 424 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 425 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 426 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 427 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 428 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 429 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 430 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 431 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 432 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 433 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 434 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 435 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 436 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 437 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 438 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 439 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 440 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 441 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 442 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 443 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 444 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 445 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 446 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 447 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 448 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 449 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 450 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 451 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 452 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 453 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 454 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 455 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 456 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 457 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 458 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 459 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 460 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 461 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 462 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 463 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 464 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 465 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 466 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 467 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 468 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 469 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 470 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 471 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 472 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 473 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 474 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 475 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 476 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 477 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 478 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 479 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 480 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 481 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 482 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 483 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 484 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 485 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 486 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 487 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 488 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 489 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 490 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 491 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 492 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 493 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 494 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 495 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 496 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 497 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 498 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 499 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 500 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 501 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 502 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 503 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 504 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 505 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 506 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 507 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 508 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 509 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 510 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 511 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 512 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 513 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 514 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 515 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 516 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 517 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 518 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 519 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 520 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 521 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 522 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 523 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 524 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 525 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 526 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 527 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 528 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 529 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 530 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 531 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 532 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 533 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 534 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 535 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 536 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 537 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 538 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 539 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 540 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 541 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 542 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 543 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 544 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 545 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 546 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 547 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 548 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 549 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 550 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 551 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 552 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 553 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 554 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 555 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 556 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 557 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 558 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 559 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 560 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 561 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 562 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 563 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 564 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 565 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 566 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 567 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 568 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 569 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 570 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 571 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 572 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 573 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 574 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 575 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 576 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 577 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 578 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 579 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
