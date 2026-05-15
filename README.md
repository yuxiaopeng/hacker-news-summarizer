# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2026-05-15.md)

*最后自动更新时间: 2026-05-15 18:39:52*
## 1. Codex 现已上线 ChatGPT 移动端

**原文标题**: Codex is now in the ChatGPT mobile app

**原文链接**: [https://openai.com/index/work-with-codex-from-anywhere/](https://openai.com/index/work-with-codex-from-anywhere/)

OpenAI 宣布将 **Codex 集成至 ChatGPT 移动端应用**，使用户能够随时随地管理和监督智能体（agentic）工作流。该更新目前已在 iOS 和 Android 平台开启预览，提供“全功能的移动体验”，支持用户连接到本地或远程机器（如笔记本电脑、Mac mini 或开发机），以实时监控活跃线程。

**核心功能与特性：**
*   **实时同步：** 应用程序可同步反映连接环境的实时状态，包括屏幕截图、终端输出、代码差异（diffs）和测试结果。
*   **远程监督：** 用户可以通过手机审批命令、切换模型、为 Bug 提供说明或启动新任务，确保长期运行的项目在无需用户守在电脑前的情况下持续推进。
*   **安全保障：** 安全的中继层可保持机器的可访问性并在不同设备间同步，且无需将其直接暴露在公网中。

**企业与开发者更新：**
*   **远程 SSH：** 现已正式发布（GA），允许 Codex 直接连接到受管理的远程环境，并从 SSH 配置中识别主机。
*   **自动化与定制：** 新增的“Hooks”允许团队扫描敏感信息或记录对话，同时程序化访问令牌支持与 CI/CD 流水线集成。
*   **符合 HIPAA 标准：** ChatGPT 企业版工作空间现在可以在本地环境中使用 Codex 处理医疗相关工作流。

**可用性：**
移动端预览版正向所有用户（包括免费版和 Go 方案）推出。用户需同时更新 ChatGPT 移动端应用和 Codex macOS 应用方可参与。对 Windows 环境的支持预计也将很快推出。

---

## 2. OpenAI 正通过 Plaid 将 ChatGPT 与银行账户关联。

**原文标题**: OpenAI is connecting ChatGPT to bank accounts via Plaid

**原文链接**: [https://firethering.com/chatgpt-bank-account-plaid-openai/](https://firethering.com/chatgpt-bank-account-plaid-openai/)

根据2026年5月15日的报道，OpenAI宣布了一项新集成，允许ChatGPT用户通过Plaid连接其银行账户。该功能目前面向每月200美元的Pro订阅者提供预览版，具有支出仪表板、个性化理财建议以及异常交易模式警报等功能。

通过Plaid进行关联后，ChatGPT可以访问全面的财务数据，包括账户余额、交易历史、投资组合以及抵押贷款和信用卡债务等负债。虽然AI可以分析这些数据，但OpenAI明确表示，ChatGPT无法执行交易，也无法查看完整的账号。

文章重点提到了几项隐私和安全担忧：
*   **数据保留：** 尽管用户可以随时断开连接，但OpenAI保留在用户“切断连接”后最长30天内删除数据的权利。
*   **训练选择权：** 关于使用财务数据来“改进模型”的默认设置存在模糊性，作者将其描述为针对重大数据共享决策的“友好话术”。
*   **商业用途：** 继1月份推出ChatGPT Health之后，此举标志着OpenAI收集高度敏感个人数据的模式。文章指出，OpenAI尚未明确回答将如何保护这些数据免受泄露，以及公司未来可能如何利用这些详细的财务画像来实现盈利。

归根结底，虽然该工具在财务管理方面确实具有实用价值，但缺乏长期的商业保障措施仍是主要的争议点。

---

## 3. 我们将停止漏洞奖励计划

**原文标题**: We are retiring our bug bounty program

**原文链接**: [https://turso.tech/blog/the-wonders-of-ai](https://turso.tech/blog/the-wonders-of-ai)

Turso 宣布停止其漏洞赏金计划，该计划曾为任何导致数据损坏的漏洞提供 1,000 美元的奖励。这一决定直接源于大量“垃圾信息”（slop）的涌入——即由 AI 生成的低质量漏洞报告和拉取请求（PR），这些内容已让项目维护者筋疲力尽。

最初，该计划非常成功，吸引了技术精湛的研究人员利用先进方法发现真实问题，甚至揭露了 SQLite 本身的漏洞。然而，大语言模型（LLM）的兴起让不良行为者可以毫不费力地生成无穷无尽且毫无意义的提交。这些“垃圾信息”的例子包括：用户手动注入垃圾数据以谎称数据损坏，甚至辩称数据库具备执行 SQL 语句的能力也是一种漏洞。

核心问题在于精力的极度不对称：机器人生成一份看似合理的报告只需几秒钟，而人类维护者却要花费数小时进行调查和驳斥。尽管 Turso 尝试过通过担保系统和自动化门禁进行缓解，但随着 AI 机器人开始反驳关闭理由并更换账号重新提交相同问题，这些措施最终均告失败。

Turso 强调，“开放贡献”是其基因的一部分。在向公众关闭项目和移除经济激励之间，他们选择了后者。通过取消赏金计划，他们旨在消除驱动自动化干扰的获利动机，使维护者能够专注于真正的贡献，并在 AI 时代维持项目的长期健康发展。

---

## 4. 新的 Nginx 漏洞利用

**原文标题**: New Nginx Exploit

**原文链接**: [https://github.com/DepthFirstDisclosures/Nginx-Rift](https://github.com/DepthFirstDisclosures/Nginx-Rift)

所提供的文本描述了 NGINX 中的一个严重堆缓冲区溢出漏洞，编号为 CVE-2026-42945（以及相关漏洞 CVE-2026-42946、CVE-2026-40701 和 CVE-2026-42934）。该问题存在于 `ngx_http_rewrite_module` 模块中，影响使用 `rewrite` 和 `set` 指令的服务器。

**技术根源**
该漏洞源于 NGINX 双阶段脚本引擎中的一个逻辑错误。在第一阶段，引擎使用一个子引擎计算所需的缓冲区大小，此时 `is_args` 标志被初始化为零，从而进行标准的长度计算。然而，在第二阶段（复制阶段），如果重写替换包含问号，引擎会在 `is_args` 设置为 1 的情况下处理数据。这会触发带有 `NGX_ESCAPE_ARGS` 标志的 `ngx_escape_uri` 函数，导致数据膨胀（例如，将特殊字符转义为 3 字节序列）。由于缓冲区大小是基于未膨胀的长度确定的，复制操作会导致堆缓冲区溢出。

**影响与利用**
该溢出允许实现未经身份验证的远程代码执行 (RCE)。报告详细说明了一种利用方法，涉及通过跨请求堆风水 (heap feng shui) 来破坏相邻 `ngx_pool_t` 结构的清理指针。通过将这些指针重定向到受控内存区域，攻击者可以在内存池销毁时触发任意系统命令。

**受影响版本与缓解措施**
该漏洞影响 NGINX 开源版本 0.6.27 至 1.30.0，以及 NGINX Plus 版本 R32 至 R36。

*   **修复版本：**
    *   **NGINX 开源版：** 1.31.0, 1.30.1
    *   **NGINX Plus：** R36 P4, R35 P2, R32 P6

敦促管理员立即升级到修复版本，以降低未经身份验证的 RCE 风险。详细的技术公告可通过 F5 和原始研究人员获取。

---

## 5. Gyroflow：基于陀螺仪数据的视频增稳

**原文标题**: Gyroflow: Video stabilization using gyroscope data

**原文链接**: [https://github.com/gyroflow/gyroflow](https://github.com/gyroflow/gyroflow)

**Gyroflow** 是一款开源、跨平台的应用程序，旨在利用陀螺仪和加速度计元数据进行高级视频增稳。与依赖视觉分析的传统增稳软件不同，Gyroflow 利用相机内部记录或外部日志中的运动数据，以实现高精度的处理结果。

**核心功能与特性**
该软件支持广泛的设备，包括 GoPro、索尼、大疆、Insta360 以及 RED 和 Blackmagic 等电影机品牌。它还可以处理来自飞行控制器（Betaflight、ArduPilot）和移动应用程序的外部数据。其核心能力包括：
*   **实时处理：** 采用多线程算法，支持 GPU 加速的预览和渲染。
*   **高级校正：** 提供果冻效应（滚动快门）校正、地平线增稳、自适应缩放（动态裁剪）和镜头标定工具。
*   **高保真度：** 支持 10 位视频（OpenEXR 最高支持 32 位浮点），以保持最佳图像质量。
*   **工作流集成：** 拥有适用于 Adobe Premiere/After Effects、DaVinci Resolve 和 Final Cut Pro 等主流视频剪辑软件的插件，允许用户无需转码即可在时间线上直接增稳素材。

**技术规格**
Gyroflow 主要使用 **Rust** 语言编写，并采用 **QML** 用户界面，专为高效运行而设计。其核心引擎是一个独立库，主要算法不依赖于 ffmpeg 或 OpenCV 等大型框架。该项目采用 GPLv3 开源协议，由社区高度驱动，支持 20 多种语言，并为开发者提供详尽的文档。

**可用性**
Gyroflow 是电影制作者和 FPV 无人机飞手的多功能工具，支持 Windows、macOS、Linux、Android 和 iOS 系统。它保持免费使用，其活跃的开发路线图托管在 GitHub 上。

---

## 6. Sigmoid 函数救不了你

**原文标题**: The sigmoids won't save you

**原文链接**: [https://www.astralcodexten.com/p/the-sigmoids-wont-save-you](https://www.astralcodexten.com/p/the-sigmoids-wont-save-you)

在《S型曲线救不了你》（The Sigmoids Won't Save You）一文中，作者批判了这样一种普遍观点：即人工智能的增长在达到危险的能力水平之前，必然会放缓并陷入“S型（Sigmoid）”曲线。虽然任何指数级增长确实都不可能永远持续，但作者指出，预测者经常陷入“S型曲线误判”——即即便趋势没有理由立即停止，他们也会在进行分析的那一刻预测增长将进入平台期。

文章重点介绍了一系列此类失败预测的“名人堂”，包括联合国的人口出生率预测、太阳能部署，以及沃顿商学院最近的 AI 能力模型。在这些案例中，专家们都预测了增速放缓，但指数级增长的趋势依然在持续。

为了更好地预测 AI 的未来，作者建议采用两种方法：
1. **深度建模：** 理解具体的运作机制，如数据中心的扩张、经济激励措施以及算法的突破。
2. **林迪定律（Lindy’s Law）：** 在缺乏明确模型的情况下，应当假设一个过程将持续与其已经存在的时间大致相当的长短。鉴于当前的 AI 规模化时代至少自 2017-2019 年以来一直保持稳定，林迪定律表明，我们应该预期至少还会有数年的显著增长。

作者总结道，举证责任在于那些声称 AI 进展将陷入停滞的人。质疑者必须提供具体的机制模型来解释为什么当前的趋势会失败，或者解释为什么基于历史持续性的“持续增长”这一默认假设是不正确的。仅仅指出“指数增长最终会变成 S型曲线”，并不足以反驳快速发展的 AI 所带来的风险。

---

## 7. 欢迎来到开源安全的露天开采时代

**原文标题**: Welcome to the Strip Mining Era of OSS Security

**原文链接**: [https://www.metabase.com/blog/strip-mining-era-of-open-source-security](https://www.metabase.com/blog/strip-mining-era-of-open-source-security)

在《欢迎来到开源软件（OSS）安全的“露天开采”时代》一文中，Metabase 首席执行官 Sameer Al-Sakran 指出，大语言模型（LLM）驱动的代码扫描已从根本上改变了安全格局。这一“露天开采”时代的特征是，针对公开代码库进行大规模、高效率且自动化的漏洞挖掘。

**核心观察：**
*   **报告激增：** Metabase 及其他开发者见证了安全报告数量的剧增——从每月约 10 份跃升至每周约 10 份，其中许多报告既真实有效又是通过 AI 生成的。
*   **“透明即安全”的终结：** 历史上，开源软件受益于社区审计。如今，AI 扫描器让任何人都能瞬间发现整个代码库中的深层漏洞。由于代码是公开的，维护者必须假定任何被发现的漏洞都已立即暴露在野外，迫使他们陷入持续、被动的“紧急模式”。
*   **转向闭源：** 应对这些持续发现的漏洞所带来的压力，正促使一些商业开源项目（如 Cal.com）转向闭源，以重新掌控补丁修复的节奏。

**建议：**
*   **针对维护者：** 假定每个漏洞都会立即被攻击者知晓。应主动使用 AI 扫描器，构建多层防护的系统架构，并过渡到高频、积极的补丁发布周期。
*   **针对用户：** 将每个开源依赖项视为高风险负债。组织必须为频繁升级预留预算，锁定所有依赖版本，提升日志记录与可观测性，并严格遵循最小权限原则。

尽管 Al-Sakran 指出这种转变对维护者而言将是“艰难”且“糟糕”的，但他总结认为，一旦现有的首批漏洞被清理干净，长期来看，软件生态系统将会变得更加安全。

---

## 8. 结束访华行程后，空军一号随行人员被要求丢弃礼品和手机

**原文标题**: Travelers on Air Force One ordered to throw away gifts, phones after China trip

**原文链接**: [https://techcrunch.com/2026/05/15/us-orders-travelers-on-air-force-one-to-throw-away-gifts-pins-and-burner-phones-after-china-trip/](https://techcrunch.com/2026/05/15/us-orders-travelers-on-air-force-one-to-throw-away-gifts-pins-and-burner-phones-after-china-trip/)

Following a high-level summit in Beijing in May 2026, members of the U.S. delegation—including President Trump, senior officials, and tech leaders like Tim Cook and Jensen Huang—were ordered to discard all items collected during the trip before boarding Air Force One.

According to reports from the White House press pool, travelers were required to surrender gifts, credential badges, lapel pins, and burner phones into a bin at the bottom of the plane’s stairs. The directive was summarized by New York Post correspondent Emily Goodin, who noted that "nothing from China" was allowed on the aircraft.

While the White House did not issue an official statement, the measure is attributed to heightened security and operational security (OPSEC) protocols. Given China’s advanced espionage and cyber-intelligence capabilities, U.S. security experts treat physical items and temporary electronic devices as potential vectors for "bugs" or surveillance software. The disposal of burner phones is a standard practice for high-level officials traveling in adversarial environments, as these devices are intended to be used temporarily and then destroyed to prevent long-term security breaches. 

Despite the professional tone of the talks between Trump and President Xi Jinping, the incident highlights the deep-seated mistrust and ongoing concerns regarding Chinese state-sponsored spying and cyberattacks.

---

## 9. Claude for Legal

**原文标题**: Claude for Legal

**原文链接**: [https://github.com/anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal)

生成摘要时出错

---

## 10. Mullvad exit IPs are surprisingly identifying

**原文标题**: Mullvad exit IPs are surprisingly identifying

**原文链接**: [https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/](https://tmctmt.com/posts/mullvad-exit-ips-as-a-fingerprinting-vector/)

生成摘要时出错

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2026-05-15](output/hacker_news_summary_2026-05-15.md) |
| 2 | [2026-05-14](output/hacker_news_summary_2026-05-14.md) |
| 3 | [2026-05-12](output/hacker_news_summary_2026-05-12.md) |
| 4 | [2026-05-13](output/hacker_news_summary_2026-05-13.md) |
| 5 | [2026-05-11](output/hacker_news_summary_2026-05-11.md) |
| 6 | [2026-05-08](output/hacker_news_summary_2026-05-08.md) |
| 7 | [2026-05-09](output/hacker_news_summary_2026-05-09.md) |
| 8 | [2026-05-10](output/hacker_news_summary_2026-05-10.md) |
| 9 | [2026-05-07](output/hacker_news_summary_2026-05-07.md) |
| 10 | [2026-05-05](output/hacker_news_summary_2026-05-05.md) |
| 11 | [2026-05-04](output/hacker_news_summary_2026-05-04.md) |
| 12 | [2026-05-06](output/hacker_news_summary_2026-05-06.md) |
| 13 | [2026-05-03](output/hacker_news_summary_2026-05-03.md) |
| 14 | [2026-05-02](output/hacker_news_summary_2026-05-02.md) |
| 15 | [2026-04-29](output/hacker_news_summary_2026-04-29.md) |
| 16 | [2026-04-28](output/hacker_news_summary_2026-04-28.md) |
| 17 | [2026-05-01](output/hacker_news_summary_2026-05-01.md) |
| 18 | [2026-04-30](output/hacker_news_summary_2026-04-30.md) |
| 19 | [2026-04-23](output/hacker_news_summary_2026-04-23.md) |
| 20 | [2026-04-26](output/hacker_news_summary_2026-04-26.md) |
| 21 | [2026-04-24](output/hacker_news_summary_2026-04-24.md) |
| 22 | [2026-04-22](output/hacker_news_summary_2026-04-22.md) |
| 23 | [2026-04-25](output/hacker_news_summary_2026-04-25.md) |
| 24 | [2026-04-27](output/hacker_news_summary_2026-04-27.md) |
| 25 | [2026-04-21](output/hacker_news_summary_2026-04-21.md) |
| 26 | [2026-04-18](output/hacker_news_summary_2026-04-18.md) |
| 27 | [2026-04-17](output/hacker_news_summary_2026-04-17.md) |
| 28 | [2026-04-20](output/hacker_news_summary_2026-04-20.md) |
| 29 | [2026-04-19](output/hacker_news_summary_2026-04-19.md) |
| 30 | [2026-04-15](output/hacker_news_summary_2026-04-15.md) |
| 31 | [2026-04-16](output/hacker_news_summary_2026-04-16.md) |
| 32 | [2026-04-14](output/hacker_news_summary_2026-04-14.md) |
| 33 | [2026-04-13](output/hacker_news_summary_2026-04-13.md) |
| 34 | [2026-04-10](output/hacker_news_summary_2026-04-10.md) |
| 35 | [2026-04-12](output/hacker_news_summary_2026-04-12.md) |
| 36 | [2026-04-11](output/hacker_news_summary_2026-04-11.md) |
| 37 | [2026-04-09](output/hacker_news_summary_2026-04-09.md) |
| 38 | [2026-04-07](output/hacker_news_summary_2026-04-07.md) |
| 39 | [2026-04-08](output/hacker_news_summary_2026-04-08.md) |
| 40 | [2026-04-05](output/hacker_news_summary_2026-04-05.md) |
| 41 | [2026-04-04](output/hacker_news_summary_2026-04-04.md) |
| 42 | [2026-04-06](output/hacker_news_summary_2026-04-06.md) |
| 43 | [2026-04-03](output/hacker_news_summary_2026-04-03.md) |
| 44 | [2026-03-31](output/hacker_news_summary_2026-03-31.md) |
| 45 | [2026-04-02](output/hacker_news_summary_2026-04-02.md) |
| 46 | [2026-03-30](output/hacker_news_summary_2026-03-30.md) |
| 47 | [2026-04-01](output/hacker_news_summary_2026-04-01.md) |
| 48 | [2026-03-27](output/hacker_news_summary_2026-03-27.md) |
| 49 | [2026-03-28](output/hacker_news_summary_2026-03-28.md) |
| 50 | [2026-03-29](output/hacker_news_summary_2026-03-29.md) |
| 51 | [2026-03-25](output/hacker_news_summary_2026-03-25.md) |
| 52 | [2026-03-24](output/hacker_news_summary_2026-03-24.md) |
| 53 | [2026-03-26](output/hacker_news_summary_2026-03-26.md) |
| 54 | [2026-03-23](output/hacker_news_summary_2026-03-23.md) |
| 55 | [2026-03-22](output/hacker_news_summary_2026-03-22.md) |
| 56 | [2026-03-21](output/hacker_news_summary_2026-03-21.md) |
| 57 | [2026-03-20](output/hacker_news_summary_2026-03-20.md) |
| 58 | [2026-03-18](output/hacker_news_summary_2026-03-18.md) |
| 59 | [2026-03-17](output/hacker_news_summary_2026-03-17.md) |
| 60 | [2026-03-19](output/hacker_news_summary_2026-03-19.md) |
| 61 | [2026-03-15](output/hacker_news_summary_2026-03-15.md) |
| 62 | [2026-03-16](output/hacker_news_summary_2026-03-16.md) |
| 63 | [2026-03-13](output/hacker_news_summary_2026-03-13.md) |
| 64 | [2026-03-14](output/hacker_news_summary_2026-03-14.md) |
| 65 | [2026-03-12](output/hacker_news_summary_2026-03-12.md) |
| 66 | [2026-03-11](output/hacker_news_summary_2026-03-11.md) |
| 67 | [2026-03-10](output/hacker_news_summary_2026-03-10.md) |
| 68 | [2026-03-07](output/hacker_news_summary_2026-03-07.md) |
| 69 | [2026-03-06](output/hacker_news_summary_2026-03-06.md) |
| 70 | [2026-03-09](output/hacker_news_summary_2026-03-09.md) |
| 71 | [2026-03-08](output/hacker_news_summary_2026-03-08.md) |
| 72 | [2026-03-02](output/hacker_news_summary_2026-03-02.md) |
| 73 | [2026-03-03](output/hacker_news_summary_2026-03-03.md) |
| 74 | [2026-03-05](output/hacker_news_summary_2026-03-05.md) |
| 75 | [2026-03-04](output/hacker_news_summary_2026-03-04.md) |
| 76 | [2026-02-28](output/hacker_news_summary_2026-02-28.md) |
| 77 | [2026-02-27](output/hacker_news_summary_2026-02-27.md) |
| 78 | [2026-03-01](output/hacker_news_summary_2026-03-01.md) |
| 79 | [2026-02-25](output/hacker_news_summary_2026-02-25.md) |
| 80 | [2026-02-26](output/hacker_news_summary_2026-02-26.md) |
| 81 | [2026-02-24](output/hacker_news_summary_2026-02-24.md) |
| 82 | [2026-02-23](output/hacker_news_summary_2026-02-23.md) |
| 83 | [2026-02-20](output/hacker_news_summary_2026-02-20.md) |
| 84 | [2026-02-21](output/hacker_news_summary_2026-02-21.md) |
| 85 | [2026-02-22](output/hacker_news_summary_2026-02-22.md) |
| 86 | [2026-02-17](output/hacker_news_summary_2026-02-17.md) |
| 87 | [2026-02-16](output/hacker_news_summary_2026-02-16.md) |
| 88 | [2026-02-18](output/hacker_news_summary_2026-02-18.md) |
| 89 | [2026-02-19](output/hacker_news_summary_2026-02-19.md) |
| 90 | [2026-02-11](output/hacker_news_summary_2026-02-11.md) |
| 91 | [2026-02-12](output/hacker_news_summary_2026-02-12.md) |
| 92 | [2026-02-15](output/hacker_news_summary_2026-02-15.md) |
| 93 | [2026-02-13](output/hacker_news_summary_2026-02-13.md) |
| 94 | [2026-02-14](output/hacker_news_summary_2026-02-14.md) |
| 95 | [2026-02-10](output/hacker_news_summary_2026-02-10.md) |
| 96 | [2026-02-07](output/hacker_news_summary_2026-02-07.md) |
| 97 | [2026-02-08](output/hacker_news_summary_2026-02-08.md) |
| 98 | [2026-02-05](output/hacker_news_summary_2026-02-05.md) |
| 99 | [2026-02-06](output/hacker_news_summary_2026-02-06.md) |
| 100 | [2026-02-09](output/hacker_news_summary_2026-02-09.md) |
| 101 | [2026-02-02](output/hacker_news_summary_2026-02-02.md) |
| 102 | [2026-01-31](output/hacker_news_summary_2026-01-31.md) |
| 103 | [2026-02-01](output/hacker_news_summary_2026-02-01.md) |
| 104 | [2026-02-03](output/hacker_news_summary_2026-02-03.md) |
| 105 | [2026-02-04](output/hacker_news_summary_2026-02-04.md) |
| 106 | [2026-01-27](output/hacker_news_summary_2026-01-27.md) |
| 107 | [2026-01-26](output/hacker_news_summary_2026-01-26.md) |
| 108 | [2026-01-30](output/hacker_news_summary_2026-01-30.md) |
| 109 | [2026-01-28](output/hacker_news_summary_2026-01-28.md) |
| 110 | [2026-01-29](output/hacker_news_summary_2026-01-29.md) |
| 111 | [2026-01-22](output/hacker_news_summary_2026-01-22.md) |
| 112 | [2026-01-24](output/hacker_news_summary_2026-01-24.md) |
| 113 | [2026-01-23](output/hacker_news_summary_2026-01-23.md) |
| 114 | [2026-01-25](output/hacker_news_summary_2026-01-25.md) |
| 115 | [2026-01-21](output/hacker_news_summary_2026-01-21.md) |
| 116 | [2026-01-16](output/hacker_news_summary_2026-01-16.md) |
| 117 | [2026-01-18](output/hacker_news_summary_2026-01-18.md) |
| 118 | [2026-01-17](output/hacker_news_summary_2026-01-17.md) |
| 119 | [2026-01-19](output/hacker_news_summary_2026-01-19.md) |
| 120 | [2026-01-20](output/hacker_news_summary_2026-01-20.md) |
| 121 | [2026-01-11](output/hacker_news_summary_2026-01-11.md) |
| 122 | [2026-01-12](output/hacker_news_summary_2026-01-12.md) |
| 123 | [2026-01-13](output/hacker_news_summary_2026-01-13.md) |
| 124 | [2026-01-15](output/hacker_news_summary_2026-01-15.md) |
| 125 | [2026-01-14](output/hacker_news_summary_2026-01-14.md) |
| 126 | [2026-01-10](output/hacker_news_summary_2026-01-10.md) |
| 127 | [2026-01-06](output/hacker_news_summary_2026-01-06.md) |
| 128 | [2026-01-05](output/hacker_news_summary_2026-01-05.md) |
| 129 | [2026-01-07](output/hacker_news_summary_2026-01-07.md) |
| 130 | [2026-01-08](output/hacker_news_summary_2026-01-08.md) |
| 131 | [2026-01-09](output/hacker_news_summary_2026-01-09.md) |
| 132 | [2026-01-01](output/hacker_news_summary_2026-01-01.md) |
| 133 | [2026-01-03](output/hacker_news_summary_2026-01-03.md) |
| 134 | [2025-12-31](output/hacker_news_summary_2025-12-31.md) |
| 135 | [2026-01-04](output/hacker_news_summary_2026-01-04.md) |
| 136 | [2026-01-02](output/hacker_news_summary_2026-01-02.md) |
| 137 | [2025-12-27](output/hacker_news_summary_2025-12-27.md) |
| 138 | [2025-12-26](output/hacker_news_summary_2025-12-26.md) |
| 139 | [2025-12-30](output/hacker_news_summary_2025-12-30.md) |
| 140 | [2025-12-29](output/hacker_news_summary_2025-12-29.md) |
| 141 | [2025-12-28](output/hacker_news_summary_2025-12-28.md) |
| 142 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 143 | [2025-12-25](output/hacker_news_summary_2025-12-25.md) |
| 144 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 145 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 146 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 147 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 148 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 149 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 150 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 151 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 152 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 153 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 154 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 155 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 156 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 157 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 158 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 159 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 160 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 161 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 162 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 163 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 164 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 165 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 166 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 167 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 168 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 169 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 170 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 171 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 172 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 173 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 174 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 175 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 176 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 177 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 178 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 179 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 180 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 181 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 182 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 183 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 184 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 185 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 186 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 187 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 188 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 189 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 190 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 191 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 192 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 193 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 194 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 195 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 196 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 197 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 198 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 199 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 200 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 201 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 202 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 203 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 204 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 205 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 206 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 207 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 208 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 209 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 210 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 211 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 212 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 213 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 214 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 215 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 216 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 217 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 218 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 219 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 220 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 221 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 222 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 223 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 224 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 225 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 226 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 227 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 228 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 229 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 230 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 231 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 232 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 233 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 234 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 235 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 236 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 237 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 238 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 239 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 240 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 241 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 242 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 243 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 244 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 245 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 246 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 247 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 248 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 249 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 250 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 251 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 252 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 253 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 254 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 255 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 256 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 257 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 258 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 259 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 260 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 261 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 262 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 263 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 264 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 265 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 266 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 267 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 268 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 269 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 270 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 271 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 272 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 273 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 274 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 275 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 276 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 277 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 278 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 279 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 280 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 281 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 282 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 283 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 284 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 285 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 286 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 287 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 288 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 289 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 290 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 291 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 292 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 293 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 294 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 295 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 296 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 297 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 298 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 299 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 300 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 301 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 302 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 303 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 304 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 305 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 306 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 307 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 308 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 309 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 310 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 311 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 312 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 313 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 314 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 315 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 316 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 317 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 318 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 319 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 320 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 321 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 322 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 323 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 324 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 325 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 326 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 327 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 328 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 329 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 330 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 331 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 332 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 333 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 334 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 335 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 336 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 337 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 338 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 339 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 340 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 341 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 342 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 343 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 344 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 345 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 346 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 347 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 348 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 349 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 350 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 351 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 352 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 353 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 354 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 355 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 356 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 357 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 358 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 359 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 360 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 361 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 362 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 363 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 364 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 365 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 366 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 367 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 368 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 369 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 370 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 371 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 372 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 373 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 374 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 375 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 376 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 377 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 378 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 379 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 380 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 381 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 382 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 383 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 384 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 385 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 386 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 387 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 388 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 389 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 390 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 391 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 392 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 393 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 394 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 395 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 396 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 397 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 398 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 399 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 400 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 401 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 402 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 403 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 404 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 405 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 406 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 407 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 408 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 409 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 410 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 411 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 412 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 413 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 414 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 415 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 416 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 417 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 418 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 419 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 420 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 421 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
