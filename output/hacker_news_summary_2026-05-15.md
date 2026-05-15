# Hacker News 热门文章摘要 (2026-05-15)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. Kairos: The ancient Greek art of knowing when to act

**原文标题**: Kairos: The ancient Greek art of knowing when to act

**原文链接**: [https://bigthink.com/mini-philosophy/kairos-the-ancient-greek-art-of-knowing-when-to-act/](https://bigthink.com/mini-philosophy/kairos-the-ancient-greek-art-of-knowing-when-to-act/)

生成摘要时出错

---

## 12. Tesla Wall Connector bootloader bypasses the firmware downgrade ratchet

**原文标题**: Tesla Wall Connector bootloader bypasses the firmware downgrade ratchet

**原文链接**: [https://www.synacktiv.com/en/publications/exploiting-the-tesla-wall-connector-from-its-charge-port-connector-part-2-bypassing](https://www.synacktiv.com/en/publications/exploiting-the-tesla-wall-connector-from-its-charge-port-connector-part-2-bypassing)

生成摘要时出错

---

## 13. Omnisearch – A lightweight metasearch engine written in C

**原文标题**: Omnisearch – A lightweight metasearch engine written in C

**原文链接**: [https://git.bwaaa.monster/omnisearch/about/](https://git.bwaaa.monster/omnisearch/about/)

生成摘要时出错

---

## 14. Waymo因驶入积水路段召回3800辆自动驾驶出租车

**原文标题**: Waymo recalls 3,800 robotaxis after they drive into flood waters

**原文链接**: [https://www.cnbc.com/2026/05/12/waymo-recalls-3800-robotaxis-after-able-drive-into-standing-water.html](https://www.cnbc.com/2026/05/12/waymo-recalls-3800-robotaxis-after-able-drive-into-standing-water.html)

生成摘要时出错

---

## 15. HDD Firmware Hacking

**原文标题**: HDD Firmware Hacking

**原文链接**: [https://icode4.coffee/?p=1465](https://icode4.coffee/?p=1465)

生成摘要时出错

---

## 16. RISC-V Router

**原文标题**: RISC-V Router

**原文链接**: [https://router.start9.com/](https://router.start9.com/)

生成摘要时出错

---

## 17. UK government replaces Palantir software with internally-built refugee system

**原文标题**: UK government replaces Palantir software with internally-built refugee system

**原文链接**: [https://www.bbc.com/news/articles/c2l2j1lxdk5o](https://www.bbc.com/news/articles/c2l2j1lxdk5o)

生成摘要时出错

---

## 18. Solar-based sleep patterns compared to modern norms

**原文标题**: Solar-based sleep patterns compared to modern norms

**原文链接**: [https://dylan.gr/1775146616](https://dylan.gr/1775146616)

生成摘要时出错

---

## 19. What's in a GGUF, besides the weights – and what's still missing?

**原文标题**: What's in a GGUF, besides the weights – and what's still missing?

**原文链接**: [https://nobodywho.ooo/posts/whats-in-a-gguf/](https://nobodywho.ooo/posts/whats-in-a-gguf/)

生成摘要时出错

---

## 20. Nordstjernen Web Browser

**原文标题**: Nordstjernen Web Browser

**原文链接**: [https://github.com/nordstjernen-web/nordstjernen](https://github.com/nordstjernen-web/nordstjernen)

生成摘要时出错

---

## 21. Porting 3D Movie Maker to Linux

**原文标题**: Porting 3D Movie Maker to Linux

**原文链接**: [https://benstoneonline.com/posts/porting-3d-movie-maker-to-linux/](https://benstoneonline.com/posts/porting-3d-movie-maker-to-linux/)

生成摘要时出错

---

## 22. Bitwarden scrubs 'Always free' and 'Inclusion' values from its site

**原文标题**: Bitwarden scrubs 'Always free' and 'Inclusion' values from its site

**原文链接**: [https://www.fastcompany.com/91542655/bitwarden-scrubs-always-free-and-inclusion-values-from-its-website-as-longtime-execs-step-down](https://www.fastcompany.com/91542655/bitwarden-scrubs-always-free-and-inclusion-values-from-its-website-as-longtime-execs-step-down)

生成摘要时出错

---

## 23. DeepSeek V4: The Open-Source Model Frontier Labs Feared

**原文标题**: DeepSeek V4: The Open-Source Model Frontier Labs Feared

**原文链接**: [https://helloai.com/articles/deepseek-v4-open-source-frontier-parity](https://helloai.com/articles/deepseek-v4-open-source-frontier-parity)

生成摘要时出错

---

## 24. OpenAI's KOSA Endorsement Is Regulatory Capture with a Smiley Face

**原文标题**: OpenAI's KOSA Endorsement Is Regulatory Capture with a Smiley Face

**原文链接**: [https://www.techdirt.com/2026/05/14/openais-kosa-endorsement-is-regulatory-capture-with-a-smiley-face/](https://www.techdirt.com/2026/05/14/openais-kosa-endorsement-is-regulatory-capture-with-a-smiley-face/)

生成摘要时出错

---

## 25. New arXiv policy: 1-year ban for hallucinated references

**原文标题**: New arXiv policy: 1-year ban for hallucinated references

**原文链接**: [https://twitter.com/tdietterich/status/2055000956144935055](https://twitter.com/tdietterich/status/2055000956144935055)

生成摘要时出错

---

## 26. From PDFs to AI-ready structured data: a deep dive (2024)

**原文标题**: From PDFs to AI-ready structured data: a deep dive (2024)

**原文链接**: [https://explosion.ai/blog/pdfs-nlp-structured-data](https://explosion.ai/blog/pdfs-nlp-structured-data)

生成摘要时出错

---

## 27. OVMS: Open source electric vehicle remote monitoring, diagnosis and control

**原文标题**: OVMS: Open source electric vehicle remote monitoring, diagnosis and control

**原文链接**: [https://www.openvehicles.com/home](https://www.openvehicles.com/home)

生成摘要时出错

---

## 28. WinUI 3 Performance: A Leap Forward

**原文标题**: WinUI 3 Performance: A Leap Forward

**原文链接**: [https://github.com/microsoft/microsoft-ui-xaml/discussions/11096](https://github.com/microsoft/microsoft-ui-xaml/discussions/11096)

生成摘要时出错

---

## 29. Fossils show millipede and centipede ancestors evolved legs underwater

**原文标题**: Fossils show millipede and centipede ancestors evolved legs underwater

**原文链接**: [https://phys.org/news/2026-05-ancient-sea-fossils-millipede-centipede.html](https://phys.org/news/2026-05-ancient-sea-fossils-millipede-centipede.html)

生成摘要时出错

---

## 30. UCF Commencement Speaker Draws Boos After A.I. Remarks

**原文标题**: UCF Commencement Speaker Draws Boos After A.I. Remarks

**原文链接**: [https://www.nytimes.com/2026/05/14/style/ucf-commencement-ai-booed-gloria-caulfield.html](https://www.nytimes.com/2026/05/14/style/ucf-commencement-ai-booed-gloria-caulfield.html)

生成摘要时出错

---

## 31. Plato's Cave and the Rise of the Highly Educated Radical

**原文标题**: Plato's Cave and the Rise of the Highly Educated Radical

**原文链接**: [https://www.thefp.com/p/platos-cave-and-the-rise-of-the-highly](https://www.thefp.com/p/platos-cave-and-the-rise-of-the-highly)

生成摘要时出错

---

## 32. Access to frontier AI will soon be limited by economic and security constraints

**原文标题**: Access to frontier AI will soon be limited by economic and security constraints

**原文链接**: [https://writing.antonleicht.me/p/cut-off](https://writing.antonleicht.me/p/cut-off)

生成摘要时出错

---

## 33. Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model

**原文标题**: Show HN: Needle: We Distilled Gemini Tool Calling into a 26M Model

**原文链接**: [https://github.com/cactus-compute/needle](https://github.com/cactus-compute/needle)

生成摘要时出错

---

## 34. Ontario auditors find doctors' AI note takers routinely blow basic facts

**原文标题**: Ontario auditors find doctors' AI note takers routinely blow basic facts

**原文链接**: [https://www.theregister.com/ai-ml/2026/05/14/ontario-auditors-find-doctors-ai-note-takers-routinely-blow-basic-facts/5240771](https://www.theregister.com/ai-ml/2026/05/14/ontario-auditors-find-doctors-ai-note-takers-routinely-blow-basic-facts/5240771)

生成摘要时出错

---

## 35. Drone Mishap with XM183 MiniBlast Redacted

**原文标题**: Drone Mishap with XM183 MiniBlast Redacted

**原文链接**: [https://www.documentcloud.org/documents/28124600-drone-mishap-with-xm183-miniblast-redacted/](https://www.documentcloud.org/documents/28124600-drone-mishap-with-xm183-miniblast-redacted/)

生成摘要时出错

---

## 36. Saying Goodbye to one line of APL

**原文标题**: Saying Goodbye to one line of APL

**原文链接**: [https://homewithinnowhere.com/posts/2026-05-10-one-line.html](https://homewithinnowhere.com/posts/2026-05-10-one-line.html)

生成摘要时出错

---

## 37. How Claude Code works in large codebases

**原文标题**: How Claude Code works in large codebases

**原文链接**: [https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start)

生成摘要时出错

---

## 38. The Emacsification of Software

**原文标题**: The Emacsification of Software

**原文链接**: [https://sockpuppet.org/blog/2026/05/12/emacsification/](https://sockpuppet.org/blog/2026/05/12/emacsification/)

生成摘要时出错

---

## 39. DIY open-source ultrasound hardware on the rp2040/rp2350

**原文标题**: DIY open-source ultrasound hardware on the rp2040/rp2350

**原文链接**: [http://un0rick.cc/pic0rick](http://un0rick.cc/pic0rick)

生成摘要时出错

---

## 40. Rewrite Bun in Rust has been merged

**原文标题**: Rewrite Bun in Rust has been merged

**原文链接**: [https://github.com/oven-sh/bun/pull/30412](https://github.com/oven-sh/bun/pull/30412)

生成摘要时出错

---

## 41. UK sovereign LLM inference

**原文标题**: UK sovereign LLM inference

**原文链接**: [https://relax.ai/docs](https://relax.ai/docs)

生成摘要时出错

---

## 42. 60fps Video on a CGA? – The GlyphBlaster

**原文标题**: 60fps Video on a CGA? – The GlyphBlaster

**原文链接**: [https://martypc.blogspot.com/2026/05/60fps-video-on-cga-glyphblaster.html](https://martypc.blogspot.com/2026/05/60fps-video-on-cga-glyphblaster.html)

生成摘要时出错

---

## 43. A Claude Code and Codex Skill for Deliberate Skill Development

**原文标题**: A Claude Code and Codex Skill for Deliberate Skill Development

**原文链接**: [https://github.com/DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities)

生成摘要时出错

---

## 44. Build a Radio Wave Detector with Balls of Aluminum Foil

**原文标题**: Build a Radio Wave Detector with Balls of Aluminum Foil

**原文链接**: [https://www.wired.com/story/build-a-radio-wave-detector-with-balls-of-aluminum-foil/](https://www.wired.com/story/build-a-radio-wave-detector-with-balls-of-aluminum-foil/)

生成摘要时出错

---

## 45. Leaving the Physical World

**原文标题**: Leaving the Physical World

**原文链接**: [https://www.eff.org/pages/leaving-physical-world](https://www.eff.org/pages/leaving-physical-world)

生成摘要时出错

---

## 46. The Power of a Free Popsicle (2018)

**原文标题**: The Power of a Free Popsicle (2018)

**原文链接**: [https://www.gsb.stanford.edu/insights/power-free-popsicle](https://www.gsb.stanford.edu/insights/power-free-popsicle)

生成摘要时出错

---

## 47. Linux gaming is faster because Windows APIs are becoming Linux kernel features

**原文标题**: Linux gaming is faster because Windows APIs are becoming Linux kernel features

**原文链接**: [https://www.xda-developers.com/linux-gaming-is-getting-faster-because-windows-apis-are-becoming-linux-kernel-features/](https://www.xda-developers.com/linux-gaming-is-getting-faster-because-windows-apis-are-becoming-linux-kernel-features/)

生成摘要时出错

---

## 48. The Biochemical Beauty of Retatrutide: How GLP-1s Work

**原文标题**: The Biochemical Beauty of Retatrutide: How GLP-1s Work

**原文链接**: [https://acesounderglass.com/2025/10/13/the-biochemical-beauty-of-retatrutide-how-glp-1s-actually-work/](https://acesounderglass.com/2025/10/13/the-biochemical-beauty-of-retatrutide-how-glp-1s-actually-work/)

生成摘要时出错

---

## 49. Show HN: GridTravel – A community based travel app for users to share routes

**原文标题**: Show HN: GridTravel – A community based travel app for users to share routes

**原文链接**: [https://www.gridtravel.app](https://www.gridtravel.app)

生成摘要时出错

---

## 50. Int a = 5; a = a++ + ++a; a =? (2011)

**原文标题**: Int a = 5; a = a++ + ++a; a =? (2011)

**原文链接**: [https://gynvael.coldwind.pl/?id=372](https://gynvael.coldwind.pl/?id=372)

生成摘要时出错

---

## 51. Coldkey – Post-quantum age key generation and paper backup tool

**原文标题**: Coldkey – Post-quantum age key generation and paper backup tool

**原文链接**: [https://github.com/pike00/coldkey](https://github.com/pike00/coldkey)

生成摘要时出错

---

## 52. Safari and Firefox change how big sites render based on the domain

**原文标题**: Safari and Firefox change how big sites render based on the domain

**原文链接**: [https://denodell.com/blog/browsers-treat-big-sites-differently](https://denodell.com/blog/browsers-treat-big-sites-differently)

生成摘要时出错

---

## 53. Iran's Internet Shutdown Enters Its 77th Day

**原文标题**: Iran's Internet Shutdown Enters Its 77th Day

**原文链接**: [https://mastodon.social/@netblocks/116577450970712439](https://mastodon.social/@netblocks/116577450970712439)

生成摘要时出错

---

## 54. Amazonbot is finally respecting robots.txt

**原文标题**: Amazonbot is finally respecting robots.txt

**原文链接**: [https://xeiaso.net/notes/2026/amazonbot-respecting-robots-txt/](https://xeiaso.net/notes/2026/amazonbot-respecting-robots-txt/)

生成摘要时出错

---

## 55. QEMUtiny - QEMU escape vulnerability if cxl is used

**原文标题**: QEMUtiny - QEMU escape vulnerability if cxl is used

**原文链接**: [https://github.com/v12-security/pocs/tree/main/qemu](https://github.com/v12-security/pocs/tree/main/qemu)

生成摘要时出错

---

## 56. Show HN: Find the best local LLM for your hardware, ranked by benchmarks

**原文标题**: Show HN: Find the best local LLM for your hardware, ranked by benchmarks

**原文链接**: [https://github.com/Andyyyy64/whichllm](https://github.com/Andyyyy64/whichllm)

生成摘要时出错

---

## 57. Show HN: Vibe Coding a $20k /Year Enterprise Logistics Platform

**原文标题**: Show HN: Vibe Coding a $20k /Year Enterprise Logistics Platform

**原文链接**: [https://trmnl.com/blog/vibe-coding-shiphero](https://trmnl.com/blog/vibe-coding-shiphero)

生成摘要时出错

---

## 58. UFerris a Versatile Learner Board for Rust Embedded Beginners

**原文标题**: UFerris a Versatile Learner Board for Rust Embedded Beginners

**原文链接**: [https://www.theembeddedrustacean.com/uferris](https://www.theembeddedrustacean.com/uferris)

生成摘要时出错

---

## 59. AI is making me dumb

**原文标题**: AI is making me dumb

**原文链接**: [https://jpain.io/god-damn-ai-is-making-me-dumb/](https://jpain.io/god-damn-ai-is-making-me-dumb/)

生成摘要时出错

---

## 60. Claude for Small Business

**原文标题**: Claude for Small Business

**原文链接**: [https://www.anthropic.com/news/claude-for-small-business](https://www.anthropic.com/news/claude-for-small-business)

生成摘要时出错

---

