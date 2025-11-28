# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-11-28.md)

*最后自动更新时间: 2025-11-28 17:48:48*
## 1. 荷兰大学能否摆脱微软？

**原文标题**: Can Dutch universities do without Microsoft?

**原文链接**: [https://dub.uu.nl/en/news/can-dutch-universities-do-without-microsoft](https://dub.uu.nl/en/news/can-dutch-universities-do-without-microsoft)

荷兰大学能否摆脱微软？（一篇Hoger Onderwijs Persbureau文章探讨荷兰大学减少或消除对微软产品和服务依赖的可能性和挑战，可能深入探讨以下因素：

*   微软的主导地位：荷兰大学目前在教育、研究和行政任务方面对微软软件（如Windows、Office 365、Teams）的依赖程度。
*   成本考量：使用微软产品的财务影响，包括许可费以及切换到替代解决方案可能节省的成本。
*   隐私担忧：与使用微软云服务相关的数据隐私和安全担忧，尤其是在欧洲数据保护法规（GDPR）的背景下。
*   替代方案的可用性：文章可能讨论现有的开源或其他商业替代方案，这些方案可能满足大学的需求。它可能会提到具体的软件套件，如LibreOffice，或协作平台，如Nextcloud。
*   技术可行性：迁移离开微软的技术挑战，包括兼容性问题、员工培训以及新系统的集成。
*   对研究的影响：文章将考虑摆脱微软对研究活动的潜在影响，特别是那些依赖于特定微软工具或平台的研究。
*   利益相关者的观点：它可能包括大学管理人员、IT人员、研究人员和学生关于减少对微软依赖的可行性和愿望的观点。
*   赞成和反对的论点：文章可能提出了一个平衡的论点，概述了这种转变的优点（例如，节省成本、提高数据隐私）和缺点（例如，技术挑战、用户采用）。
*   大学试点/案例：它可能会提到已经采取措施减少对微软依赖或正在考虑这样做的具体荷兰大学。）

---

## 2. 基于Yggdrasil网络的真正P2P邮件

**原文标题**: True P2P Email on Top of Yggdrasil Network

**原文链接**: [https://github.com/JB-SelfCompany/Tyr](https://github.com/JB-SelfCompany/Tyr)

Tyr：一款利用Yggdrasil网络的真正点对点电子邮件通讯安卓应用。与传统电子邮件不同，Tyr无需中心化邮件服务器、消息加密层（Yggdrasil已处理）和端口转发。它具有抗审查性，并允许用户控制其电子邮件基础设施。

主要功能包括与DeltaChat和ArcaneChat集成、本地SMTP/IMAP服务器、用于电子邮件身份的自动Ed25519密钥生成、可配置的Yggdrasil对等连接、开机自启动、加密备份/恢复以及自动从Android Keystore问题中恢复。

Tyr直接在Android设备上运行一个完整的电子邮件服务器（Yggmail，用Go编写），在localhost上暴露标准SMTP/IMAP协议。电子邮件地址通过用户的公钥加密派生（`<64位十六进制字符>@yggmail`），确保可验证的身份并防止欺骗。

将Tyr与DeltaChat/ArcaneChat配合使用，可以实现完全去中心化的消息传递体验，消息通过Yggdrasil直接在用户之间发送，绕过中心服务器。可以通过按钮自动设置，也可以通过配置DeltaChat/ArcaneChat配置文件以指向本地Tyr服务器来手动设置。

该项目包括安全功能，如用于密码的Android Keystore加密、自动Keystore恢复、Yggdrasil网络加密、本地专用端口访问、加密身份以及加密备份。Tyr是开源的。

---

## 3. 别拽那个，你永远不知道它连着什么。

**原文标题**: Don't tug on that, you never know what it might be attached to

**原文链接**: [https://blog.plover.com/2016/07/01/#tmpdir](https://blog.plover.com/2016/07/01/#tmpdir)

马克·多米努斯讲述了他的调试历程：他的 `also` 脚本（使用 `emacsclient` 在 Emacs 中打开文件）停止工作，并显示错误信息，指示无法找到服务器套接字。问题根源在于 Emacs 和 `emacsclient` 查找套接字的位置不匹配。

他发现，系统管理员脚本设置的 `TMPDIR` 环境变量导致 `emacsclient` 在 `/mnt/tmp` 中查找套接字，而 Emacs 则在 `/tmp` 中创建它。 最初，他怀疑 Emacs 不尊重 `TMPDIR`，但进一步调查显示，通过 Git 调用的 Perl 脚本 `git-re-edit` 以某种方式取消设置了 `TMPDIR`。

核心问题是为什么 Perl 会删除 `TMPDIR`。 令人困惑的是，它只影响 `TMPDIR`，而不影响其他环境变量。 最终，在其他人的帮助下，问题被追溯到 Perl 安装中的一项安全措施，该措施会剥离 `TMPDIR` 以防止权限提升攻击。 设置 `TMPDIR` 可能会诱使程序将临时文件写入攻击者控制的位置，从而可能覆盖重要文件。

多米努斯设计了两种解决方法：使用 TCP 套接字代替 Unix 域套接字用于 Emacs，以及设置自定义环境变量 `EMACS_SERVER_SOCKET`，以明确告诉 `emacsclient` 在哪里找到 Unix 域套接字。

---

## 4. 200行Python代码胜过5000万美元的超级计算机 – Re=10⁸下的Navier-Stokes方程 [pdf]

**原文标题**: 200 Lines of Python beats $50M supercomputer – Navier-Stokes at Re=10⁸ [pdf]

**原文链接**: [https://philpapers.org/archive/CAMIIA-3.pdf](https://philpapers.org/archive/CAMIIA-3.pdf)

基于标题，该文章做出了大胆的声明：仅用200行Python代码实现的基于纳维-斯托克斯方程的流体动力学模拟，其性能可以媲美价值5000万美元的超级计算机。雷诺数(Re)为10⁸表明存在高度湍流状态，使得模拟在计算上具有挑战性。

然而，所提供的文档似乎是一个被截断和损坏的PDF文档，主要由二进制数据和PDF对象定义组成，没有实际的文本内容来证实或反驳标题的声明。 无法确定模拟的准确性、所采用的方法、所使用的具体硬件，或者与超级计算机进行比较的细节。

因此，由于缺少文本内容，无法总结文章的内容。 唯一显而易见的是文章的标题以及PDF文档的格式。

---

## 5. Atuin 的新 Runbook 执行引擎

**原文标题**: Atuin’s New Runbook Execution Engine

**原文链接**: [https://blog.atuin.sh/introducing-the-new-runbook-execution-engine/](https://blog.atuin.sh/introducing-the-new-runbook-execution-engine/)

Atuin Desktop发布重大架构更新，重新设计了runbook执行引擎，解决了诸如上下文不稳定和执行不一致等问题。新引擎提供持久且可复现的runbook，在应用程序重启后保持状态并确保可预测的行为。

主要改进包括：

*   **持久上下文：** Runbook保留执行状态，无需重新运行代码块。
*   **可复现执行：** 代码块仅影响其下方的代码块，从而创建可预测的工作流程。
*   **模板无处不在：** 模板系统应用于所有用户输入，包括变量名和上下文代码块。
*   **自引用变量：** 变量可以引用自身以进行转换。
*   **两种类型的上下文：** 被动上下文（工作目录、环境变量）自动持久化。 主动上下文（代码块输出）在执行期间设置。

此次更新移除了全局上下文依赖性，并将编辑器变量同步替换为手动更新。 脚本变量现在仅捕获stdout。

未来的计划包括一个用于在没有Atuin Desktop的情况下执行runbook的CLI运行器、改进的串行执行、秘密管理以及基于Markdown的runbook。 新引擎为实时协作执行奠定了基础，并已在v0.2.0中提供。

---

## 6. Meta用高等几何隐藏270亿美元债务

**原文标题**: Meta hiding $27B in debt using advanced geometry

**原文链接**: [https://stohl.substack.com/p/exclusive-credit-report-shows-meta](https://stohl.substack.com/p/exclusive-credit-report-shows-meta)

无法访问文章链接。

---

## 7. Show HN: 用眼镜检测带摄像头的智能眼镜

**原文标题**: Show HN: Glasses to detect smart-glasses that have cameras

**原文链接**: [https://github.com/NullPxl/banrays](https://github.com/NullPxl/banrays)

这个“Show HN”帖子详细介绍了“Ban-Rays”的开发，这是一款旨在检测带有摄像头的智能眼镜（如Meta Raybans）的眼镜。该项目探索了两种主要的检测方法：光学和网络。

光学方法利用相机镜头的逆反射性，红外（IR）光会直接反射回光源。使用红外LED和光电二极管的初步实验表明，在区分相机镜头和其他反射表面方面效果不稳定。虽然测试了不同的波长和扫描模式，但产生的信号微弱且不可靠。

网络方法侧重于低功耗蓝牙（BLE）指纹识别。开发者发现Meta Raybans在配对和开机期间会广播可检测的BLE广播，其中包含Meta特定的标识符。挑战在于在使用过程中检测这些广播，这需要捕获特定的通信数据包。开发者正在探索使用nRF模块进行更高级的蓝牙分析。蓝牙经典（BTC）流量分析也在考虑之中，但需要更专业且昂贵的硬件。

作者以日志形式更新，详细介绍了迄今为止的挑战和发现，并概述了两种方法的未来步骤，包括试验扫描模式、来自不同波长的数据以及主动探测。该帖子最后感谢了为测试提供指导和借用设备的人员。

---

## 8. 人工智能采纳率开始趋于平缓

**原文标题**: AI Adoption Rates Starting to Flatten Out

**原文链接**: [https://www.apolloacademy.com/ai-adoption-rates-starting-to-flatten-out/](https://www.apolloacademy.com/ai-adoption-rates-starting-to-flatten-out/)

人工智能普及率趋于平缓

这篇文章由阿波罗首席经济学家托斯滕·斯洛克于2025年11月28日发表，报告指出各种规模的公司采用人工智能的比率开始趋于平缓。该分析使用了美国人口普查局和Ramp的数据，特别是Ramp人工智能指数，该指数衡量了超过4万家美国企业对人工智能产品和服务的采用情况。Ramp人工智能指数利用公司信用卡和账单支付数据，涵盖数十亿美元的支出。这些数据以双周调查的六次调查移动平均线形式呈现。

文章强调，未经阿波罗全球管理公司明确同意，不得分发所提供的信息。 它还包括一份全面的免责声明，声明阿波罗不保证信息的准确性，这些信息可能会发生变化。它明确指出，该演示文稿不是投资建议，读者应咨询自己的顾问。 最后，它提醒读者注意前瞻性陈述及其固有的不确定性。

---

## 9. 请愿书：正式承认开源工作为德国公民服务

**原文标题**: Petition to formally recognize open source work as civic service in Germany

**原文链接**: [https://www.openpetition.de/petition/online/anerkennung-von-open-source-arbeit-als-ehrenamt-in-deutschland#petition-main](https://www.openpetition.de/petition/online/anerkennung-von-open-source-arbeit-als-ehrenamt-in-deutschland#petition-main)

德国请愿活动呼吁正式承认开源工作为志愿服务

---

## 10. 重塑性感：网络监控扼杀了情色。

**原文标题**: Bringing Sexy Back. Internet surveillance has killed eroticism

**原文链接**: [https://lux-magazine.com/article/privacy-eroticism/](https://lux-magazine.com/article/privacy-eroticism/)

无法访问文章链接。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 2 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 3 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 4 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 5 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 6 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 7 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 8 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 9 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 10 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 11 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 12 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 13 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 14 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 15 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 16 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 17 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 18 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 19 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 20 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 21 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 22 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 23 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 24 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 25 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 26 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 27 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 28 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 29 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 30 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 31 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 32 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 33 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 34 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 35 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 36 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 37 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 38 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 39 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 40 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 41 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 42 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 43 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 44 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 45 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 46 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 47 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 48 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 49 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 50 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 51 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 52 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 53 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 54 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 55 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 56 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 57 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 58 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 59 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 60 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 61 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 62 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 63 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 64 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 65 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 66 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 67 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 68 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 69 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 70 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 71 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 72 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 73 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 74 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 75 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 76 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 77 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 78 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 79 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 80 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 81 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 82 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 83 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 84 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 85 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 86 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 87 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 88 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 89 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 90 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 91 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 92 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 93 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 94 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 95 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 96 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 97 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 98 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 99 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 100 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 101 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 102 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 103 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 104 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 105 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 106 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 107 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 108 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 109 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 110 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 111 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 112 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 113 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 114 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 115 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 116 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 117 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 118 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 119 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 120 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 121 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 122 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 123 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 124 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 125 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 126 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 127 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 128 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 129 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 130 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 131 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 132 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 133 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 134 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 135 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 136 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 137 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 138 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 139 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 140 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 141 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 142 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 143 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 144 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 145 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 146 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 147 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 148 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 149 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 150 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 151 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 152 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 153 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 154 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 155 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 156 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 157 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 158 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 159 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 160 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 161 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 162 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 163 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 164 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 165 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 166 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 167 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 168 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 169 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 170 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 171 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 172 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 173 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 174 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 175 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 176 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 177 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 178 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 179 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 180 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 181 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 182 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 183 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 184 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 185 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 186 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 187 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 188 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 189 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 190 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 191 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 192 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 193 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 194 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 195 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 196 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 197 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 198 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 199 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 200 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 201 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 202 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 203 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 204 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 205 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 206 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 207 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 208 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 209 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 210 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 211 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 212 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 213 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 214 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 215 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 216 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 217 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 218 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 219 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 220 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 221 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 222 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 223 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 224 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 225 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 226 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 227 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 228 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 229 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 230 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 231 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 232 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 233 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 234 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 235 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 236 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 237 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 238 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 239 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 240 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 241 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 242 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 243 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 244 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 245 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 246 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 247 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 248 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 249 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 250 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 251 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 252 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 253 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
