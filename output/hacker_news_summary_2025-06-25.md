# Hacker News 热门文章摘要 (2025-06-25)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 一个新的PNG规范

**原文标题**: A new PNG spec

**原文链接**: [https://www.programmax.net/articles/png-is-back/](https://www.programmax.net/articles/png-is-back/)

该文章宣布停滞 20 余年的 PNG 规范已焕然一新。此次更新通过多项关键改进，使 PNG 进入现代时代。

首先，它引入了适当的 HDR 支持，利用了一个紧凑的 4 字节扩展。其次，该规范正式认可了广泛支持但先前未被承认的动画 PNG (APNG)。第三，现在正式支持 Exif 数据，包括版权和 GPS 信息。最后，更新包括一般的整理工作，解决勘误并提供澄清。

此次复兴源于 W3C 定时文本工作组对 HDR 支持的需求，促成了 Adobe、Apple、BBC、Comcast/NBCUniversal、Google、MovieLabs 和 W3C 等行业巨头的合作。

新的 PNG 规范已获得 Chrome、Safari、Firefox、iOS/macOS 等主要平台以及 Photoshop 和 DaVinci Resolve 等软件的支持。广播公司也在实施它，有可能使 HDR 新闻滚动条和体育横幅成为现实。

展望未来，下一次更新（第四版）将侧重于提高 HDR 和 SDR 的互操作性。随后的更新（第五版）将专注于先进的压缩技术和平行编码/解码，以进一步增强 PNG 的功能。作者对 PNG 工作组的奉献表示感谢。

---

## 2. Gemini 命令行

**原文标题**: Gemini CLI

**原文链接**: [https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)

Gemini CLI 是一个开源 AI 代理，它将 Gemini 的强大功能直接带入开发者的终端，提供了一个用于编码、内容生成、问题解决、研究和任务管理的多功能工具。它与 Google 的 AI 编码助手 Gemini Code Assist 集成，并免费提供 Gemini 2.5 Pro 的访问权限，拥有 100 万个 token 的上下文窗口，为个人 Google 帐户提供业界领先的每分钟 60 个模型请求和每天 1,000 个请求的配额。

该 CLI 提供了强大的 AI 功能，例如代码理解、文件操作、命令执行和动态故障排除。它可以利用 Google 搜索来支持提示，通过模型上下文协议 (MCP) 和捆绑的扩展来扩展功能，自定义提示以及自动化任务。由于是开源的，它鼓励社区贡献以改进和增强安全性。

Gemini CLI 与 VS Code 中的 Gemini Code Assist 共享技术，支持通过提示驱动的编码，包括多步骤规划和错误恢复。Gemini Code Assist 的代理模式在所有计划中均免费提供，并提供较高的使用上限。Gemini CLI 入门简单，只需一个电子邮件地址即可。

---

## 3. OpenAI按分钟收费，所以要缩短分钟时长

**原文标题**: OpenAI Charges by the Minute, So Make the Minutes Shorter

**原文链接**: [https://george.mand.is/2025/06/openai-charges-by-the-minute-so-make-the-minutes-shorter/](https://george.mand.is/2025/06/openai-charges-by-the-minute-so-make-the-minutes-shorter/)

加速音频转录：一种节省 OpenAI 服务成本和时间的技巧

---

## 4. 可嵌入网页的通用Lisp

**原文标题**: Web Embeddable Common Lisp

**原文链接**: [https://turtleware.eu/static/paste/wecl-test-gl/main.html](https://turtleware.eu/static/paste/wecl-test-gl/main.html)

文章“Web可嵌入Common Lisp”可能探讨在Web浏览器环境中使用Common Lisp的可能性和影响。由于没有提供更多内容，我们只能推断其可能关注的焦点：

该文章可能讨论了传统上用于桌面应用程序和后端开发的Common Lisp如何适应基于Web的应用程序。这可能涉及以下主题：

*   **实现方法：** 它可能详细介绍诸如将Common Lisp编译为JavaScript（例如，使用Parenscript或CL-Web-View等项目）的技术，从而使Lisp代码能够直接在浏览器中运行。或者，它可能讨论在服务器端使用Common Lisp和客户端JavaScript框架。
*   **使用Common Lisp进行Web开发的好处：** 可能会强调潜在的优势，例如Lisp强大的宏系统、表达性、垃圾回收和成熟的生态系统。
*   **挑战和局限性：** 可能会解决诸如性能开销、调试复杂性和对专用工具的需求等问题。
*   **用例：** 该文章可能会展示一些示例应用程序，其中Web可嵌入的Common Lisp方法特别有用，例如复杂的数据操作、符号计算或交互式用户界面。
*   **与其他技术的潜在比较：** 可能会将Lisp的Web嵌入与在Web开发中使用JavaScript、Python或其他后端/前端技术进行比较。

简而言之，该文章可能会评估将Common Lisp的强大功能引入Web浏览器的可行性、优点、缺点和潜在用例。

---

## 5. 准备颁发IP地址证书

**原文标题**: Getting ready to issue IP address certificates

**原文链接**: [https://community.letsencrypt.org/t/getting-ready-to-issue-ip-address-certificates/238777](https://community.letsencrypt.org/t/getting-ready-to-issue-ip-address-certificates/238777)

Let's Encrypt 即将具备在其生产环境中颁发包含 IP 地址使用者可选名称 (SANs) 的证书的能力。然而，此功能初期将仅限于有效期为 6 天的短期配置，并且仅通过允许列表提供。

公告强调，此功能尚未准备好公开发布，目前不接受任何时间表或允许列表请求。

提供了一个示例暂存证书和一个使用该证书的网站以供审查和反馈：abadcafe.txt 和 https://[2602:ff3a:1:abad:c0f:fee:abad:cafe]/。鼓励社区报告遇到的任何问题、异常或错误。作者已经发现 Firefox 处理 IP 地址 SAN 时可能存在一个错误，并提交了一个错误报告 (BZ #1973855)。

---

## 6. 机器人还是人类？打造互联网的无形图灵测试

**原文标题**: Bot or Human? Creating the Invisible Turing Test for the Internet

**原文链接**: [https://research.roundtable.ai/proof-of-human/](https://research.roundtable.ai/proof-of-human/)

本文认为，像 Google reCAPTCHA v3 这样的传统机器人检测方法已经不足以应对，因为人工智能代理可以模仿一般用户行为并绕过这些系统。作者提出了一种新方法，侧重于行为模式和认知特征，利用人类和机器人与计算机交互的内在差异。

他们强调了三个关键领域：按键动力学、鼠标移动分析和认知心理学，特别是斯特鲁普测试。人类的打字和鼠标移动具有不规则性和微调特征，而机器人则表现出不自然的规律性。斯特鲁普测试揭示了人类的认知干扰，其中冲突的文字和颜色刺激会减慢反应时间，而机器人则保持一致的表现。

作者认为，对于机器人来说，复制这些细微的行为和认知特征在计算上是昂贵的，因此与依赖容易被欺骗的静态凭据（如密码）相比，这是一种更有效的防御方法。他们描述了他们的方法，即使用像波士顿温度测试这样的刺激来创建代理类型和行为之间的映射，并利用该知识来开发任何给定用户的置信度分数。

他们的公司 Roundtable Technologies 提供了一种 Proof-of-Human API，该 API 分析在正常网络交互期间收集的行为和认知模式，以确定在线代理是否是人类，从而使机器人面临自然且持续地复制全方位人类认知的经济挑战。该方法旨在改进机器人检测，而无需依赖侵犯隐私的生物识别扫描或 cookie 跟踪。

---

## 7. FurtherAI (YC W24) 正在招聘软件和人工智能职位

**原文标题**: FurtherAI (YC W24) Is Hiring for Software and AI Roles

**原文链接**: [https://www.ycombinator.com/companies/furtherai/jobs](https://www.ycombinator.com/companies/furtherai/jobs)

FurtherAI (YC W24) 正在招聘：为保险业打造AI员工队伍，在旧金山办公室和远程招聘多个职位。他们的目标是创建能够自动化各种保险工作流程的AI队友，从处理非结构化文档到拨打电话，以实现人类水平的可靠性、适应性和持续学习能力。

现有职位包括：前线部署工程师（欢迎应届毕业生）、软件/AI工程师（应届毕业生）、保险领域专家、客户经理、前端工程师 - Web、软件工程师 - 后端/全栈（旧金山和印度）以及销售开发代表。薪资范围因职位和地点而异，并提供股权。

FurtherAI 已从 Y Combinator、South Park Commons、Nexus VP 和 Converge VC 等知名投资者处筹集了 500 万美元的种子轮融资。该公司成立于 2023 年，目前拥有 8 人的团队。创始团队包括 Sashank Gondala（CTO/联合创始人）和 Aman Gour（创始人），Gondala 是前苹果公司的语言建模科学家，Gour 是一位二次创业者。

---

## 8. 如何撰写引人注目的发布公告

**原文标题**: How to Write Compelling Release Announcements

**原文链接**: [https://refactoringenglish.com/chapters/release-announcements/](https://refactoringenglish.com/chapters/release-announcements/)

本文提供撰写引人入胜的、能引起用户共鸣的版本发布公告的指南。它强调关注用户收益，而非简单罗列技术变更。好的发布公告展示了如何改善用户体验，这与详细描述开发者所做工作的变更日志不同。

要点包括：

*   **关注用户收益：** 描述用户可以使用新功能*做什么*，而不是新功能*是什么*。
*   **发布公告 vs. 发行说明：** 公告突出对用户影响重大的变更，而发行说明详尽且技术性强。
*   **功能选择：** 选择使工作流程更轻松或更快捷的功能，重点关注用户价值。
*   **积极措辞：** 将修复描述为用户体验的改进，而不仅仅是删除错误。
*   **介绍您的产品：** 为潜在的新用户简要介绍您的产品。
*   **避免模糊描述：** 摒弃“各种改进和错误修复”之类的短语。
*   **有效的视觉效果：** 使用清晰的屏幕截图和简短、有影响力的动画演示来展示功能。
*   **尽早规划：** 在开发过程中考虑发布公告，以确保包含用户价值。

本文使用来自 Gleam 和 Figma 的示例来说明最佳实践，展示如何根据用户收益和改进的体验来呈现功能。最终目标是围绕新版本创建兴奋感和参与度。

---

## 9. 在 Linux 上读取 NFC 护照芯片

**原文标题**: Reading NFC Passport Chips in Linux

**原文链接**: [https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/](https://shkspr.mobi/blog/2025/06/reading-nfc-passport-chips-in-linux/)

本文详细介绍了如何在Linux系统上读取护照中嵌入的NFC芯片数据，重点在于解决读取机读区(MRZ)损坏的已注销护照的难题。作者在使用其他工具遇到问题后，使用了roeften的pypassport库。

访问数据的关键是MRZ，它相当于一个由护照号码、出生日期和有效期组成的密码，每个部分都有校验和。作者提供了Python代码，通过计算这些校验和来重建损坏的MRZ。

本文探讨了暴力破解MRZ的理论可能性，但指出，虽然在已知其他数据的情况下对有效期进行破解是可行的，但所需的时间投入使其不切实际。文章强调，提取的数据——照片、姓名、性别、国籍、签发国——大部分在护照本身上都是可见的，这降低了破解MRZ的价值。

作者解释了如何安装和使用pypassport，演示了如何访问不同的数据组（如包含个人数据的DG1和包含生物识别数据的DG2-DG4），提取元数据（例如，眼睛位置、性别），以及保存护照照片。最后，文章提醒说，虽然它可以读取护照数据，但它不会验证真伪或检测欺诈护照，仅用于提取容易获得的信息。

---

## 10. 第三空间与社区创业 (2024)

**原文标题**: Third places and neighborhood entrepreneurship (2024)

**原文链接**: [https://www.nber.org/papers/w32604](https://www.nber.org/papers/w32604)

国家经济研究局（NBER）的这份工作论文探讨了“第三空间”（特别是星巴克咖啡馆）与社区创业之间的关系。该研究由Jinkyong Choi、Jorge Guzman和Mario L. Small撰写，调查了在美国没有咖啡馆的社区引入星巴克是否会影响新企业的创建率。

该研究将开设了星巴克的普查区与计划开设但未开设的普查区进行比较，发现前者的新创企业活动显著增加。具体而言，在随后的7年中，开设星巴克的普查区每年新创企业数量增加了9.1%到18%（即2.9到5.7家公司）。该研究还指出，星巴克与魔术师约翰逊在贫困地区的合作产生了更大的影响。

作者认为，这种效应是通过一种网络机制运作的，星巴克充当了“第三空间”，促进了潜在企业家之间的联系和思想交流。

该论文承认哥伦比亚泰默社会企业研究所和考夫曼基金会的资助。一篇题为“‘第三空间’促进当地经济活动”的论文非技术性摘要也已发布。石英网站上的一篇文章“由于气候变化，咖啡价格越来越贵”也提到了这项研究。

---

## 11. 可爱多做错了变现策略吗？

**原文标题**: Is Lovable getting monetization wrong?

**原文链接**: [https://getlago.substack.com/p/lovable-makes-60m-in-6-monthsbut](https://getlago.substack.com/p/lovable-makes-60m-in-6-monthsbut)

好的，我已阅读了提供的URL中的文章《Lovable的盈利模式是否错误？》。以下是摘要：

员工礼品应用 Lovable 实现了令人瞩目的增长，在短短 6 个月内收入达到 6000 万美元。然而，文章质疑他们目前基于礼品成本之上收取统一平台费用的盈利策略是否最佳且可持续。

核心论点是，Lovable 可能因未探索更复杂的定价模式而错失盈利机会，并可能阻碍未来的增长。目前的统一费用使得小团队赠送廉价礼品成本过高，而大型团队赠送昂贵礼品则可能过于便宜。

文章建议 Lovable 可以考虑几种替代定价模式，包括：

*   **基于团队规模或礼品数量的分级定价：** 使 Lovable 能够迎合不同的客户群体。
*   **基于价值的定价：** 根据 Lovable 提供的感知价值（例如，积极的员工士气、员工留任率）收取更高的费用。
*   **免费增值模式：** 提供具有有限功能的免费层级以吸引新用户，并向上销售到付费计划。
*   **基于使用量的定价：** 针对发送的每个礼品收费。

作者认为，虽然当前简单的模式允许最初的快速扩张，但更细致的定价方法可以释放更大的收入潜力，提高客户留存率，并为不同的客户群体提供更大的灵活性。他们总结说，Lovable 应该分析其数据和客户行为，以确定从长远来看，不同的盈利策略是否更有益。

---

## 12. 微软编辑

**原文标题**: Microsoft Edit

**原文链接**: [https://github.com/microsoft/edit](https://github.com/microsoft/edit)

Microsoft Edit 是一款简单的文本编辑器，其灵感来源于经典的 MS-DOS 编辑器，但具有类似 VS Code 的现代界面，专为方便使用而设计，即使是不熟悉终端的人也能轻松上手。它可以通过 WinGet 在 Windows 上安装 (`winget install Microsoft.Edit`)，或者从 Releases 页面下载二进制文件。

要从源代码构建，您需要 Rust（nightly toolchain）和来自存储库的源代码。使用 `cargo build --config .cargo/release.toml --release` 进行发布构建。

软件包维护者应注意，首选的可执行文件名是“edit”，而“msedit”是避免冲突的替代方案。应避免使用“ms-edit”之类的名称，并建议使用“edit”别名。

该编辑器可以选择性地使用 ICU 库进行搜索和替换。如果您的系统对 ICU 库（SONAME）或版本化导出使用不同的命名约定，可以在构建时设置环境变量，例如 `EDIT_CFG_ICUUC_SONAME`、`EDIT_CFGI18N_SONAME`、`EDIT_CFG_ICU_CPP_EXPORTS` 和 `EDIT_CFG_ICU_RENAMING_VERSION` 来配置链接。可以设置 `EDIT_CFG_ICU_RENAMING_AUTO_DETECT` 来尝试自动检测，但不建议这样做。使用 `cargo test -- --ignored` 来测试您的 ICU 设置。

---

## 13. 星际航行：视角与耐心

**原文标题**: Interstellar Flight: Perspectives and Patience

**原文链接**: [https://www.centauri-dreams.org/2025/06/25/interstellar-flight-perspectives-and-patience/](https://www.centauri-dreams.org/2025/06/25/interstellar-flight-perspectives-and-patience/)

保罗·吉尔斯特的《星际航行：远见与耐心》反思了星际旅行的漫长时间尺度和巨大挑战，从约翰·科尔特兰的音乐和近期的太空探索进展中汲取灵感。文章首先提及帕克太阳探测器打破纪录地接近太阳，然后过渡到思考利用太阳引力进行星际旅行。

吉尔斯特探讨了各种航天器所能达到的速度，强调了帕克太阳探测器目前191.2公里/秒的最高速度记录。尽管这个速度令人印象深刻，但仍意味着到达比邻星需要6600年，突出了对更快推进技术的需求。他将其与旅行者1号探测器进行比较，该探测器将于2027年成为第一个到达距离太阳一日光的地球人造物体。

文章强调了星际事业所需的长期视角，将旅行者项目投入的精力等同于建造吉萨大金字塔所需的大部分劳力。 然后它链接到胡夫的“太阳船”，突出了人类连接和梦想星星的悠久历史。

吉尔斯特最后强调，想象力和梦想是技术突破的关键先驱。 虽然当前的速度和技术导致多代人的航行，但这篇文章强调了对更快解决方案（如定向能量推进）的持续探索，这可能只需20年即可到达比邻星。 文章强调，进步始于愿景和对长期目标的持续追求。

---

## 14. 瑟尼克尔

**原文标题**: Thnickels

**原文链接**: [https://thick-coins.net/?_bhlid=8a5736885893b7837e681aa73f890b9805a4673e](https://thick-coins.net/?_bhlid=8a5736885893b7837e681aa73f890b9805a4673e)

西奥多·尼科尔斯致力于创造“厚克尔”，一种更厚更重的硬币，旨在赢得尊重，既能作为货币，也能作为自卫工具。受与嘲笑他少量镍币的窃贼的屈辱遭遇的驱使，西奥多将他的车库改造成了一家铸币厂，以生产这些沉甸甸的硬币。

“厚克尔”正面设计为西奥多头像，并刻有“In Mass We Trust（以重量为信）”、“Respect Me（尊重我）”以及预计铸造日期“2025”。背面则印有一枚坚固的硬币，拉丁文格言“Nummos Crassiores Omnibus（人人拥有更厚的硬币）”、“One Thnickel（一枚厚克尔）”以及“Hefty Coin Nation（厚重硬币国度）”。

西奥多通过有限名额的合作关系接受首批“厚克尔”的预订。起初，他通过分发传单获得了成功，这让他的孙子感到惊讶。然而，他目前正与一位未归还“厚克尔”原型的邻居发生纠纷。

西奥多鼓励支持者通过打印和张贴传单来宣传“厚克尔”，并欢迎大家对他设计的积极反馈。可以通过电子邮件或电话联系他进行预订或咨询。他的网站使用FrontPage 98构建，自豪地宣称他致力于提供“人人拥有更厚的硬币”。

---

## 15. Qodo Gen CLI：在软件开发生命周期的任何阶段构建和运行编码代理

**原文标题**: Introducing Qodo Gen CLI: Build and Run Coding Agents Anywhere in the SDLC

**原文链接**: [https://www.qodo.ai/blog/introducing-qodo-gen-cli-build-run-and-automate-agents-anywhere-in-your-sdlc/](https://www.qodo.ai/blog/introducing-qodo-gen-cli-build-run-and-automate-agents-anywhere-in-your-sdlc/)

Qodo Gen CLI 是一款新的命令行界面工具（目前处于 alpha 阶段），它允许开发者构建、管理和运行 AI 代理，以自动化整个软件开发生命周期 (SDLC) 中的工作流程。它旨在通过提供一个灵活、可编程的层来简化开发，该层可以集成到不同的编辑器和平台中。

主要功能包括：

*   **自定义代理：** 开发者可以使用简单的 .toml 配置文件来定义代理的触发器、输入、操作和结果。
*   **工作流程自动化：** 代理可以由 CI/CD 管道、Webhooks 触发，或者作为托管可调用进程 (MCP) 运行。
*   **终端和 Web UI 交互：** 代理可以在终端中使用，也可以通过基于 Web 的界面使用，该界面具有诸如聊天和代码差异等可视化元素。
*   **智能代理 IDE 支持：** 通过终端将 AI 功能集成到任何 IDE 中。
*   **模型灵活性：** 支持 Claude 和 GPT 等领先的 LLM。
*   **灵活部署：** 提供 SaaS 选项，即将推出本地支持。

用例示例包括可访问性审计、批量错误修复、性能优化、组件生成、智能代码审查、自动发布说明生成以及改进的测试覆盖率。 Qodo Gen CLI 还支持不同的执行模式（CI、Webhook、MCP）以集成到不同的环境中。

可以使用 `npm install -g @qodo/gen` 安装 CLI。未来的计划包括后台代理、并行执行以及整个 SDLC 中的标准化编码实践。

---

## 16. Show HN: Elelem，一个用C编写的Ollama和DeepSeek工具调用CLI

**原文标题**: Show HN: Elelem, a tool-calling CLI for Ollama and DeepSeek in C

**原文链接**: [https://codeberg.org/politebot/elelem](https://codeberg.org/politebot/elelem)

无法访问文章链接。

---

## 17. 使用uv和PEP 723的乐趣

**原文标题**: Fun with uv and PEP 723

**原文链接**: [https://www.cottongeeks.com/articles/2025-06-24-fun-with-uv-and-pep-723](https://www.cottongeeks.com/articles/2025-06-24-fun-with-uv-and-pep-723)

本文重点介绍了 uv (一个快速的 Python 包和项目管理器) 结合 PEP 723 (一个关于 Python 文件内联脚本元数据的提议) 来简化 Python 脚本的执行。作者对管理简单脚本的 Python 环境的传统开销表示不满，并提出了一个利用 uv 和 PEP 723 的解决方案。

uvx 被介绍为一个类似于 npx 的工具，用于创建一次性的虚拟环境来运行 Python 工具。PEP 723 允许使用特殊的注释块在脚本中直接指定脚本依赖和 Python 版本要求。通过结合 uv 的 `run` 命令和 PEP 723 元数据，本文演示了如何在无需手动设置环境的情况下执行具有所需依赖项的 Python 脚本。

文章提供了一个实际的例子：一个提取 YouTube 字幕的脚本。该脚本包含 shebang 行、用于依赖管理的内联 PEP 723 元数据，以及提取字幕的 Python 代码。通过使脚本可执行并直接运行它，uv 自动处理依赖项安装和执行。作者最后强调了这种方法在创建自包含、易于执行的 Python 脚本方面的潜力，将其与 Go 二进制文件的易用性进行了比较。他们还分享了一个 GitHub 仓库，用于一个利用该技术的相关项目。

---

## 18. 深入兔子洞：Bash、OverlayFS 和一个 30 年前的惊喜

**原文标题**: Deep Down the Rabbit Hole: Bash, OverlayFS, and a 30-Year-Old Surprise

**原文链接**: [https://sigma-star.at/blog/2025/06/deep-down-the-rabbit-hole-bash-overlayfs-and-a-30-year-old-surprise/](https://sigma-star.at/blog/2025/06/deep-down-the-rabbit-hole-bash-overlayfs-and-a-30-year-old-surprise/)

客户切换到OverlayFS后，OpenSSH的`scp`失败引发了一段复杂的调试过程。错误信息指向Bash无法确定当前目录，提示“设备不适用的ioctl操作”。

调查显示，Bash出人意料地使用了自己的`getcwd()`实现，而不是glibc的，这是为古老的Unix系统准备的备用方案。发生这种情况的原因是构建环境是一个交叉编译设置，并且配置脚本无法确认零大小缓冲区的内存分配，因此定义了`GETCWD_BROKEN`。

由于OverlayFS对inode号的处理，这个问题才得以显现。Bash的`getcwd()`备用方案依赖于比较从`stat(".")`和`readdir("..")`获得的inode号。出于性能原因，OverlayFS直接从底层返回inode号，而无需通过readdir进行完整查找，从而导致不匹配。这在32位系统上尤其普遍，因为这些系统上没有提供稳定inode号的`xino`功能。

最终，调查发现Bash的`getcwd()`实现中存在一个30年前的bug，它在调用`readdir()`之前没有正确重置`errno`，导致它将EOF误解为错误，从而导致误导性的`ENOTTY`错误。

修复方法包括在构建过程中覆盖测试结果，以防止Bash使用其备用`getcwd()`。这次经历强调了理解遗留代码所做的假设、OverlayFS等文件系统的复杂性以及交叉编译环境中潜在陷阱的重要性。

---

## 19. 比尔·阿特金森：宝丽来照片展示Lisa GUI的演变 [视频]

**原文标题**: Bill Atkinson: Polaroids Showing the Evolution of the Lisa GUI [video]

**原文链接**: [https://www.youtube.com/watch?v=Qg0mHFcB510](https://www.youtube.com/watch?v=Qg0mHFcB510)

比尔·阿特金森：宝丽来照片展示Lisa GUI的演变。
该视频可能包含比尔·阿特金森（苹果公司Lisa图形用户界面（GUI）开发的关键人物）。他可能正在展示或讨论记录Lisa GUI设计和改进迭代过程的宝丽来照片。

YouTube描述本身并没有提供关于视频内容的太多细节，只是与版权、联系方式、创作者、广告、开发者、服务条款、隐私、安全以及关于YouTube运作方式、测试新功能和NFL Sunday Ticket相关的标准YouTube样板文字。

因此，核心信息是该视频可能通过比尔·阿特金森本人分享的宝丽来照片，提供Lisa GUI开发的宝贵视觉历史。可能的关键收获是了解设计选择、迭代以及创建开创性图形用户界面的过程中所进行的的问题解决。YouTube描述本身没有增加任何进一步的具体信息。

---

## 20. 外国诈骗犯利用美国银行诈骗美国人

**原文标题**: Foreign Scammers Use U.S. Banks to Fleece Americans

**原文链接**: [https://www.propublica.org/article/pig-butchering-scam-cybercrime-us-banks-money-laundering](https://www.propublica.org/article/pig-butchering-scam-cybercrime-us-banks-money-laundering)

ProPublica调查揭露，境外诈骗团伙，特别是那些在东南亚运营“杀猪盘”的团伙，正利用美国银行洗钱，金额高达数十亿美元，而这些钱都是从美国人手中诈骗而来。这些骗局包括在网上与受害者建立关系，说服他们投资虚假的加密货币平台，然后榨干他们的账户。

诈骗犯依靠黑市银行账户网络（通常通过中文电报频道获取）来接收受害者的资金。然后，这些账户被用来将资金转换成加密货币，使其难以追踪跨国界流动。尽管银行有防止洗钱的法律义务，但在很大程度上未能阻止非法资金的流动。

文章重点介绍了 Middlesex Truck and Coach 的案例，其名称被欺诈性地用于开设 Chase 银行账户，以接收诈骗所得。文章还详细介绍了受害者 Kevin 的经历，他通过“杀猪盘”诈骗损失了大量资金，该诈骗涉及将资金汇给看似无关的公司，而这些公司在 Chase 银行开有账户。

调查强调了银行在侦测和预防这些复杂诈骗时面临的挑战。虽然银行声称投资于欺诈侦测系统，但法规漏洞和诈骗犯的狡猾手段使得这些骗局得以蓬勃发展。像在柬埔寨西哈努克城运营的国际网络为洗钱过程提供了便利，凸显了问题的全球性。

---

## 21. 信息已被永久删除，只是“永久”的程度很低。

**原文标题**: Information has been permanently deleted, for small values of permanently

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20250625-01/?p=111308](https://devblogs.microsoft.com/oldnewthing/20250625-01/?p=111308)

作者十个月前删除了Contoso的账户，并收到确认函称其个人信息已被永久删除且不可逆转。然而，昨天他们收到Contoso发来的电子邮件，通知隐私政策已更新。这与Contoso之前的确认函相矛盾，暗示他们仍然保留着作者的电子邮件地址，尽管声称已永久删除了所有相关信息。作者强调了Contoso永久删除的承诺与收到隐私政策更新邮件的现实之间的差异。语气表明对Contoso数据删除措施的彻底性持怀疑态度。

---

## 22. 哈希碰撞的概率 (2022)

**原文标题**: The probability of a hash collision (2022)

**原文链接**: [https://kevingal.com/blog/collisions.html](https://kevingal.com/blog/collisions.html)

本文探讨了哈希冲突背后的数学原理。当哈希函数为两个不同的输入分配相同的值时，就会发生哈希冲突。作者使用以书名哈希值将书籍存储在箱子中的类比来阐述这一概念。计算哈希冲突概率的问题被框定为“生日问题”，其目标是确定两个或多个项目（人、书等）共享同一“桶”（生日、箱子等）的概率。

本文提供了计算哈希冲突概率的精确公式，并解释了为什么对于大型数据集而言，其计算成本会变得很高。为了解决这个问题，作者提出了三种近似方法：指数近似、简化版本以及更简单的平方版本。

这些近似方法的准确性与精确计算进行了比较，结果表明，指数近似是最稳健的，而较简单的版本仅适用于较小数据集的粗略估算。文章最后给出了所用近似方法的数学有效性证明。作者还提供了一个哈希冲突计算器。

---

## 23. 破解蒙德里安密码 (2017)

**原文标题**: Cracking the Mondrian Code (2017)

**原文链接**: [https://www.thebeliever.net/logger/cracking-the-mondrian-code/](https://www.thebeliever.net/logger/cracking-the-mondrian-code/)

尼娜·西格尔的《破解蒙德里安密码》探讨了人们对皮特·蒙德里安未完成的杰作《胜利布基伍基》的持久迷恋。文章详细描述了蒙德里安在生命最后时光里对这件作品的倾注，他使用彩色胶带探索他的审美理想，但在1944年去世时，这件作品仍未完成。

七十多年来，人们一直试图破译这幅画的意图，常常使用数学和逻辑公式。然而，蒙德里安的传记作者和策展人汉斯·詹森认为，蒙德里安的作品本质上是直觉的，拒绝僵化的解读。

文章将《胜利布基伍基》置于风格派运动的背景下，强调了其抽象形式和色彩的目标。它深入探讨了这幅画未完成的问题，探讨了这是否是故意的，还是蒙德里安突然去世的结果。胶带的不稳定性导致了保护方面的挑战，包括为了修复而制作副本。

西格尔将人们认为蒙德里安是“枯燥的计算者”的看法与他艺术敏感性的现实进行了对比，注意到他在有限的调色板中运用了微妙的色调和纹理。它突出了将他的作品视为算法和认识到其感性和超然品质之间的张力。

文章最后提到了海牙市立博物馆颇具争议地购买《胜利布基伍基》一事，质疑将大量资金分配给一件未完成的作品是否合理，但强调了它在抽象艺术领域的重要性。

---

## 24. 神秘岛D'ni语词典

**原文标题**: A Dictionary of the Language of Myst's D'ni

**原文链接**: [http://www.eldalamberon.com/dni_dict.htm](http://www.eldalamberon.com/dni_dict.htm)

本文档是Kh'reestrefah编纂的D'ni语词典的引言和初步章节，经Cyan, Inc.许可出版。其旨在列出所有Cyan发布的D'ni语单词，并注明来源和提供语境。推测性的翻译用括号括起来并用问号标示。该词典包含Riven语词汇表、较长文本的转录以及英语释义索引。

该词典解决了D'ni语罗马转写的不一致问题，并采用基于不太含糊变体的统一转录，同时引用Cyan的原始转写。它包括D'ni字母表和修改字母的表格，参考了Jehon的可下载D'ni字体以及Cyan用法中的变化（í的I/ai，eh的e等）。

本文档重点介绍了1996年《Myst日历》中Atrus祈祷文的一种变体D'ni字母表，提出了与后来发布的文本不同的语音值，并讨论了其对DRC破译过程的潜在影响。

该词汇表按罗马转写字母顺序排列，双字母和修改字母分别列出。本文档还提供了基于D'ni字母顺序的词典章节链接。

最后，提供了引用的来源列表（书籍、游戏、网站等），以及D'ni语言和文化各种资源的链接和参考。本文档提供了与第一人称单数“I”相关的动词变位模型。它还有一个部分涵盖介词“ah”的用法。

---

## 25. 网页翻译 API

**原文标题**: Web Translator API

**原文链接**: [https://developer.mozilla.org/en-US/docs/Web/API/Translator](https://developer.mozilla.org/en-US/docs/Web/API/Translator)

本文档介绍了实验性的 Web 翻译器 API，它是翻译器和语言检测器 API 的一部分。它允许开发者直接在浏览器内翻译文本。

主要功能包括：

*   **实验性技术：** 该 API 被标记为实验性的，建议开发者在生产环境中使用前检查浏览器的兼容性。
*   **翻译器接口：** 包含翻译功能，包括 AI 模型可用性检查、翻译器实例创建和翻译生成。
*   **属性：** `inputQuota`、`sourceLanguage` 和 `targetLanguage` 属性分别提供有关资源限制、源语言和目标语言的信息。
*   **静态方法：** `availability()` 方法检查特定配置的翻译模型是否可用，`create()` 方法生成新的 Translator 实例。
*   **实例方法：** `destroy()` 方法销毁 Translator 实例。`measureInputUsage()` 估计翻译将使用的输入配额。`translate()` 方法执行单个翻译，而 `translateStreaming()` 提供一个 ReadableStream 用于流式翻译。
*   **示例：** 提供了示例代码，演示如何创建 Translator 实例、生成简单的翻译以及生成流式翻译。

---

## 26. ChatGPT的企业成功对抗Copilot，加剧OpenAI/微软竞争

**原文标题**: ChatGPT's enterprise success against Copilot fuels OpenAI/Microsoft rivalry

**原文链接**: [https://www.bloomberg.com/news/articles/2025-06-24/chatgpt-vs-copilot-inside-the-openai-and-microsoft-rivalry](https://www.bloomberg.com/news/articles/2025-06-24/chatgpt-vs-copilot-inside-the-openai-and-microsoft-rivalry)

无法访问文章链接。

---

## 27. 对巴拉圭亚松森的思考

**原文标题**: Thoughts on Asunción, Paraguay

**原文链接**: [https://cpsi.media/p/thoughts-on-asuncion-paraguay](https://cpsi.media/p/thoughts-on-asuncion-paraguay)

本文介绍了作者对巴拉圭亚松森的观察，重点在于其缺乏美学连贯性。 尽管有现代建筑和近期贵宾的到访，但由于破旧的建筑与现代发展并存，这座城市给作者留下的印象类似于金边等东南亚城市，突显了城市规划的不足。

作者将此归因于巴拉圭政府与其他拉丁美洲国家和柬埔寨相比的低支出，突显了一种精简的国家模式。 虽然存在现代高层建筑，但当地中产阶级并未推动需求。 相反，外国投资者，主要来自阿根廷，收购了 70% 的新房产作为资本保值策略，主要出租给外国人。 租赁合同通常以美元而非当地货币计价。

房地产开发的供应方由税收激励驱动。 第 60/90 号法律为超过特定投资门槛的批准房地产项目提供显著的税收减免，例如进口资本货物 0% 的关税和增值税，以及向国外支付的利息/佣金 0% 的预扣税。 在亚松森建造和预售 40% 以上的单元还有额外的激励措施。 这些激励措施吸引了开发商和外国买家，导致现代高层建筑与破旧的基础设施并存。 作者最后谈到了巴拉圭的其他方面，例如毁灭性的三国同盟战争，人口的吸引力和友善，以及无处不在的问题“Con factura o sin factura？”（要发票吗？）。

---

## 28. 英国政客质疑富士通在公共部门合同中持续扮演的角色

**原文标题**: Brit politicians question Fujitsu's continued role in public sector contracts

**原文链接**: [https://www.theregister.com/2025/06/25/fujitsu_public_sector_contracts/](https://www.theregister.com/2025/06/25/fujitsu_public_sector_contracts/)

尽管发生“地平线”丑闻，英国政界人士质疑政府为何继续接受富士通竞标公共部门IT合同。作为问题系统“地平线”的供应商，富士通最初承诺在公开调查结束前停止竞标，但仍然赢得了北爱尔兰土地注册局价值1.25亿英镑的合同。

议员们担心，在“地平线”丑闻调查仍在进行，受害者赔偿仍未解决的情况下，富士通继续获得利润丰厚的合同。具体来说，人们对富士通竞标价值3.7亿英镑的“贸易商支持服务”（TSS）合同表示担忧，该公司是该合同的现任供应商，自2020年以来已获得5亿英镑的合同。

考虑到富士通在“地平线”丑闻中的角色和未支付的赔偿金，一些议员已向部长们提出多个议会质询，询问富士通竞标和获得合同是否合适。政府的回应通常表示，采购规则正在得到遵守，并且没有法律依据阻止富士通竞标。一些议员正在推动将富士通指定为高风险供应商，并可能阻止其获得未来的公共部门合同。

---

## 29. XBOW，一款自主渗透测试工具，已登顶HackerOne。

**原文标题**: XBOW, an autonomous penetration tester, has reached the top spot on HackerOne

**原文链接**: [https://xbow.com/blog/top-1-how-xbow-did-it/](https://xbow.com/blog/top-1-how-xbow-did-it/)

本文详细介绍了自主AI驱动的渗透测试工具XBOW如何登上HackerOne美国排行榜榜首。其过程始于使用CTF挑战赛和定制场景进行严格的基准测试。在通过发现零日漏洞（白盒渗透测试）证明其在开源项目中的能力后，团队将重点转移到通过HackerOne的漏洞赏金计划进行真实世界的黑盒环境测试。

XBOW无需人工输入即可运行，并能快速扩展以全面测试Web应用程序。主要挑战包括扩展到HackerOne上大量潜在目标以及最大限度地减少误报。为了解决扩展问题，该团队构建了基础设施，通过解析程序范围和策略，并采用域去重技术（SimHash和视觉相似性分析）来优先处理高价值目标。

为了确保准确性并减少误报，开发了一个“验证器”系统来自动确认漏洞，使用诸如无头浏览器之类的技术来验证XSS发现的JavaScript执行情况。

XBOW的成功在于报告了数千个经过验证的漏洞，影响了知名公司，并使其在HackerOne上名列前茅。 XBOW提交了近1,060个漏洞，从严重到低级别不等，包括 Palo Alto GlobalProtect VPN中的一个重大漏洞。虽然130个已解决，303个已分类，但仍有相当数量（125个）正在审查中，突显了该工具对实时目标的影响。该团队计划发布博客文章，展示XBOW的技术发现。

---

## 30. 微软为Windows 10扩展更新开放免费层级

**原文标题**: Microsoft opens a free tier for Windows 10 extended updates

**原文链接**: [https://www.theregister.com/2025/06/25/microsoft_free_esu_tier/](https://www.theregister.com/2025/06/25/microsoft_free_esu_tier/)

这篇来自The Register的文章讨论了微软针对即将停止支持的Windows 10更新后的扩展安全更新 (ESU) 计划。此前，微软向个人消费者提供每年30美元的ESU。现在，他们推出了两种额外的免费获取ESU的方式：

1.  **使用Windows备份将设置同步到云端：** 此选项会将用户设置备份到Microsoft OneDrive。虽然Windows备份是免费的，但它需要OneDrive存储空间。

2.  **兑换1,000个Microsoft Rewards积分：** 作者开玩笑地指出这个选项不切实际，因为需要几十年才能积累足够的积分。

文章强调，这些“免费”选项本质上是激励用户使用并付费购买微软云服务，特别是OneDrive和Microsoft 365。如果用户已经为额外的OneDrive存储空间付费，他们实际上就有资格获得ESU。文章建议，那些不愿意付费的用户应该考虑Windows 10 LTSC版本或切换到Linux。

对于商业用户，ESU计划第一年每个设备的费用为61美元，后续年份费用会增加（最多三年）。但是，通过Windows 365或虚拟机访问Windows 11云电脑的设备可以免费获得ESU。

---

## 31. 当时间不存在时的时间管理

**原文标题**: Managing time when time doesn't exist

**原文链接**: [https://multiverseemployeehandbook.com/blog/temporal-resources-managing-time-when-time-doesnt-exist/](https://multiverseemployeehandbook.com/blog/temporal-resources-managing-time-when-time-doesnt-exist/)

本文探讨了现代物理学，特别是量子力学视角下的时间管理悖论。文章认为，我们痴迷于优化时间是具有讽刺意味的，因为物理学家越来越怀疑，我们所感知的时间是一种涌现的幻觉。

文章追溯了时间管理的历史，从古代农业日历到牛顿的“绝对时间”和爱因斯坦的相对论，后者打破了普世时间的观念。文章重点介绍了量子力学的视角，特别是惠勒-德维特方程，令人惊讶的是，该方程不包含时间变量，这表明时间在宇宙最深层面上并不存在。

文章介绍了佩奇-伍特斯机制，该机制表明时间是从量子纠缠中涌现出来的；量子系统中的观察者体验时间，而外部观察者则不会。实验支持了这一观点，表明时间确实是为内部观察者涌现的。

文章提出，意识本身可能就是通过量子观测创造我们时间体验的机制。这种观点彻底改变了工作场所的生产力，表明专注和精神投入会改变我们参与时空涌现结构的方式。

文章最后提供了一些实用但幽默的量子时间管理应用，例如“量子叠加日程安排”。核心观点是，通过积极参与任务并集中注意力，我们参与了时间体验本身的持续创造。因此，时间管理是关于有意识地参与产生我们时间感的量子过程。

---

## 32. 古老的X11缩放技术

**原文标题**: Ancient X11 scaling technology

**原文链接**: [https://flak.tedunangst.com/post/forbidden-secrets-of-ancient-X11-scaling-technology-revealed](https://flak.tedunangst.com/post/forbidden-secrets-of-ancient-X11-scaling-technology-revealed)

文章《古老的X11缩放技术》幽默地挑战了X11缺乏适当DPI和分数缩放支持的普遍观点。作者tedu着手在多个具有不同分辨率的显示器上绘制一个大小始终如一的两英寸圆，证明X11确实可以处理缩放。

作者使用OpenGL和着色器绘制圆，重点关注决定圆像素大小的`radius`变量。实现一致缩放的关键在于根据从X服务器通过XRandR检索的显示器DPI信息动态调整`radius`。代码利用`XRRGetScreenResourcesCurrent`、`XRRGetOutputInfo`和`XRRGetCrtcInfo`来获取物理宽度、虚拟宽度和屏幕位置。监控配置事件以检测窗口何时移动或调整大小，从而触发`radius`的重新校准。

作者成功地在其笔记本电脑屏幕、桌面显示器和电视上以大致相同的物理尺寸显示了圆。作者承认电视的测量尺寸与其规格略有偏差，这突出显示了一个小的校准问题，而不是缩放方法的基本缺陷。

总之，这篇文章俏皮地证明了X11可以实现DPI缩放，尽管存在常见的误解。作者鼓励读者不要理会那些声称某些事情不可能的人，并将他们成功的尝试作为概念证明分享。他们还创建了一个基于相同缩放原理的屏幕标尺。

---

## 33. 亚秒：用于 Rust 热重载的运行时热补丁引擎

**原文标题**: Subsecond: A runtime hotpatching engine for Rust hot-reloading

**原文链接**: [https://docs.rs/subsecond/0.7.0-alpha.1/subsecond/index.html](https://docs.rs/subsecond/0.7.0-alpha.1/subsecond/index.html)

Subsecond 是一个 Rust 库，支持热补丁，允许在运行的应用程序中进行代码更改而无需重启，这对于像游戏引擎和服务器这样的长时间运行的进程非常有用。它包含“ThinLinking”以加快开发编译速度。

**主要特性：**

*   **热补丁：** 使用跳转表将函数调用重定向到最新版本，避免不安全的内存修改。补丁在外部编译，更新后的跳转表被发送到运行中的应用程序。
*   **用法：** 通过使用 `call()` 函数实现，该函数会绕行到函数的最新版本。
*   **ThinLink：** 一种链接器，通过动态链接依赖项、生成跳转表和差异化对象文件来加速 Rust 开发。
*   **局限性：** 结构体热重载有限，静态变量会被跟踪但不会被销毁，并且已修补 crate 中的线程局部变量会在更新时重置。 工作区补丁目前仅限于“顶端”crate。
*   **支持平台：** 适用于 Android、iOS、Linux、macOS、Windows 和 WebAssembly。
*   **全局变量和静态变量：** 支持全局变量和静态变量的热重载，但不会调用新全局变量的析构函数，并且忽略对静态初始化程序的更改。
*   **嵌套调用：** 允许对补丁应用进行精细控制，并通过允许调用嵌套来限制状态丢失，从而可以在代码的特定点应用补丁。

推荐使用 Dioxus CLI (`dx serve --hotpatch`)。 框架作者可以与 Subsecond 集成以处理结构体重建和管理状态。 提供了一个徽章来指示库对 Subsecond 的支持。

---

## 34. 编程中如何考虑时间

**原文标题**: How to Think About Time in Programming

**原文链接**: [https://shanrauf.com/archive/how-to-think-about-time-in-programming](https://shanrauf.com/archive/how-to-think-about-time-in-programming)

本文提供了一个理解编程中时间的 conceptual 模型，将其分解为绝对时间和民用时间。

**绝对时间**处理持续时间和瞬时，指的是不考虑日历或时区的特定时刻。它使用“自纪元以来的秒数”模型，其中瞬时由其与参考点（纪元）的持续时间表示。存在不同的纪元，例如 Unix 时间（1970 年 1 月 1 日）或 Apollo_Time。

**民用时间**是一种人类可读的系统，用于标记绝对时间，例如公历。它使用日期时间（年/月/日/小时/分钟/秒）和周期（月、周）来表达瞬时和持续时间。

然后，本文探讨了计算机如何准确跟踪绝对时间。地球的自转不是恒定的，导致出现差异。为了保持同步，使用了 **UTC（协调世界时）**。它是一种基于原子钟的时间标准，并且 IERS 引入闰秒以调整地球自转减慢的情况。

**时区**解决了全球太阳位置的差异。它们定义了如何在当地时间表达方式和 UTC+0 的“基线”之间进行转换。时区是遵循相同民用时间规则的区域，通常基于“标准时间”（UTC 偏移）。许多地区使用“夏令时”，在一年中的不同时间切换到不同的 UTC 偏移。时区的定义不是静态的，地方政府会更改标准时间。

---

## 35. 编写玩具软件是一种乐趣

**原文标题**: Writing toy software is a joy

**原文链接**: [https://blog.jsbarretto.com/post/software-is-joy](https://blog.jsbarretto.com/post/software-is-joy)

《编写玩具软件其乐无穷》一文倡导创建小型个人软件项目，以此来学习、提升技能并重新发现编程的乐趣。作者认为，构建你自己的现有工具和技术版本，即使它们并不完美，也能提供比单纯阅读更深入的理解。

文章强调在这些“玩具”项目中保持简单，避免过度设计，鼓励开发者专注于核心功能并通过实践应用进行学习。好处包括获得适用于专业工作的宝贵知识，并深入了解软件的局限性。

作者提供了一系列玩具程序建议，按难度和预计时间投入进行评级。这些项目包括正则表达式引擎、x86操作系统内核、GameBoy模拟器、物理引擎、动态解释器等等。每个建议都包含指向有用资源的链接。

最后，文章建议不要依赖LLM来完成这些项目，强调独立探索和解决问题的价值。作者认为，从零开始创造东西的挣扎能带来更深刻的理解和更有益的体验。

---

## 36. 如何思考并行编程：非也！[视频] (2021)

**原文标题**: How to Think about Parallel Programming: Not! [video] (2021)

**原文链接**: [https://www.infoq.com/presentations/Thinking-Parallel-Programming/](https://www.infoq.com/presentations/Thinking-Parallel-Programming/)

盖伊·斯蒂尔2011年在Strange Loop大会上的演讲“如何思考并行编程：别想！”，提倡一种关于我们如何处理并行编程的范式转变。他认为程序员不应该承担显式管理并行的负担。相反，编程语言应该被设计成自动且透明地利用并行性。

斯蒂尔提出，语言应该优先考虑基于独立性和“构建与征服”原则构建的算法，而不是传统的线性问题分解。这意味着要从显式定义任务应该如何并行化，转变为指定*需要做什么*，让语言运行时来决定*如何*并行执行它。

该演讲涉及对能够促进这种自动并行化的新语言设计的需求。斯蒂尔当时是Sun Microsystems实验室的Sun Fellow，他认为这需要对语言结构进行根本性的重新思考，以支持本质上适合并行执行的算法。

---

## 37. Framework Laptop 12 媒体评测已上线，Framework Laptop 13 现有库存

**原文标题**: Framework Laptop 12 press reviews are live and Framework Laptop 13 in-stock

**原文链接**: [https://frame.work/blog/framework-laptop-12-press-reviews-are-live-and-framework-laptop-13-in-stock](https://frame.work/blog/framework-laptop-12-press-reviews-are-live-and-framework-laptop-13-in-stock)

Framework笔记本电脑更新简述：

Framework宣布Framework笔记本电脑12的媒体评测已上线，本周开始发货。Laptop 12是一款12.2英寸触摸屏可转换笔记本电脑，因其可维修性、耐用性、可升级性和吸引人的设计而备受赞誉。JerryRigEverything、The Verge和Phoronix的评测突出了其模块化、构建质量和便携性。Q3发货的预购仍在开放中，但向Hack Club捐款250美元以上即可解锁“第0批次”的提前访问权限（本周五结束）。

Framework笔记本电脑13（AMD Ryzen 300系列）现已备货，五个工作日内发货。它正成为电力用户，尤其是在Linux上的用户的热门选择。

Framework正在增加其在活动中的参与度，首先是在丹佛举行的北美开源峰会（6月23日至25日，B2展位）和在圣安东尼奥举行的ISTELive（6月29日至7月2日，3029展位），后者侧重于Framework笔记本电脑12。计划在北美和欧洲举办更多活动。

---

## 38. 在“星蚀”中扮演“初次接触”：为期3天的科幻LARP

**原文标题**: Playing First Contact in Eclipse, a 3-Day Sci-Fi Larp

**原文链接**: [https://mssv.net/2025/06/15/playing-first-contact-in-eclipse-a-spectacular-3-day-sci-fi-larp/](https://mssv.net/2025/06/15/playing-first-contact-in-eclipse-a-spectacular-3-day-sci-fi-larp/)

本文预览了为期3天的科幻LARP游戏“Eclipse”。该游戏设定于2059年，150名玩家在一个人类殖民候选星球上扮演与外星生物进行首次接触的角色。作者探讨了该LARP游戏中关于人类自我毁灭性和存在本质的主题，并将其与电影《降临》和《星际穿越》进行类比。

“Eclipse”是新意大利LARP传统的一部分，强调自上而下的叙事和令人信服的科幻环境。该LARP游戏在波兰的Alvernia Planet（一个由混凝土和玻璃穹顶组成的网络）拥有壮观的场景，并为玩家提供平板电脑、连身衣和3D打印道具。

作者探讨了围绕昂贵的大型LARP游戏的争议，承认了对可及性的担忧，但认为视觉沉浸感可以增强体验，并可以成为通往更经济实惠的LARP游戏的途径。文章详细介绍了费用（890欧元）和LARP游戏前的准备工作，包括角色选择和视频日志。

在剧透警告之前，作者描述了第一天的工作坊，内容涵盖游戏机制（工作、星球探索、社交生活）、期望（没有“赢”，接受失败）、安全（安全词、降级技巧）和主题考虑（殖民）。游戏分为三个部分：硬科学、软科学和探索。作者选择了探索，并被分配了角色Bex，一个游牧民。文章最后介绍了作者对平面设计和结构化游戏前工作坊的印象。

---

## 39. Cloudflare如何拦截了高达7.3 Tbps的DDoS攻击

**原文标题**: How Cloudflare blocked a monumental 7.3 Tbps DDoS attack

**原文链接**: [https://blog.cloudflare.com/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/](https://blog.cloudflare.com/defending-the-internet-how-cloudflare-blocked-a-monumental-7-3-tbps-ddos/)

2025年5月中旬，Cloudflare成功拦截了一次创纪录的7.3 Tbps DDoS攻击，该攻击使用Magic Transit针对一家托管服务提供商。此次攻击比Cloudflare之前的记录大12%，仅在45秒内就传递了37.4 TB的数据，平均针对21,925个目标端口。

虽然99.996%的攻击是UDP flood，但也包括QOTD、Echo、NTP、Mirai UDP flood、Portmap和RIPv1放大攻击。此次攻击源自161个国家的5,433个自治系统（AS）中的超过122,145个源IP地址，其中巴西和越南贡献了近一半的流量。

Cloudflare的自主DDoS检测和缓解系统利用全球任播在477个数据中心分发和缓解攻击，并通过实时指纹识别识别可疑模式。一个启发式引擎dosd分析数据包样本并生成指纹，以精确匹配和阻止攻击流量，而不会影响合法用户。缓解规则被编译为eBPF程序。

Cloudflare在全球范围内共享实时威胁情报，从而提高缓解效果。该公司还为服务提供商提供免费的DDoS僵尸网络威胁信息流，以识别并关闭从其ASN内部发起攻击的滥用帐户。Cloudflare标榜其免费、不限量的DDoS保护是其构建更美好互联网的使命的一部分。

---

## 40. 第二项研究发现优步使用不透明算法大幅提高利润

**原文标题**: Second study finds Uber used opaque algorithm to dramatically boost profits

**原文链接**: [https://www.theguardian.com/technology/2025/jun/25/second-study-finds-uber-used-opaque-algorithm-to-dramatically-boost-profits](https://www.theguardian.com/technology/2025/jun/25/second-study-finds-uber-used-opaque-algorithm-to-dramatically-boost-profits)

近期两项学术研究指责优步利用不透明算法来增加利润，损害司机和乘客的利益。哥伦比亚商学院的一项研究分析了数千次行程，发现优步实施了“算法价格歧视”，提高了乘客的票价，降低了司机的收入。这导致到2024年底，优步的抽成率（优步在支付司机后保留的票价百分比）从大约32%增加到超过42%。

这项研究与牛津大学的一项类似研究相呼应，该研究调查了英国150万次行程。牛津大学的研究发现，自2023年推出“动态定价”算法以来，优步在英国每位司机的平均抽成率从25%增加到29%，甚至在某些行程中超过50%。与此同时，司机每小时的收入“大幅减少”。

根据哥伦比亚大学的研究，优步于2022年在美国推出的“预付定价”是英国“动态定价”的美国版。这些算法是“高峰定价”的迭代，根据实时供需情况调整票价。

这些研究重新点燃了围绕优步运营方式的争议，加上此前的问题，例如2021年英国最高法院裁决授予司机最低工资和带薪假期，以及2022年曝光该公司欺骗性游说行为的“优步文件”泄露事件。

优步坚称其定价透明且公平，预付定价为乘客提供清晰度，并为司机提供知情决策。他们否认使用个人信息进行定价，并驳斥了不公平操纵或歧视的指控。他们还对牛津大学报告中提出的数据提出异议，称保证每位司机至少赚取国家最低生活工资。

---

## 41. 运河船模拟器

**原文标题**: Canal Boat Simulator

**原文链接**: [https://jacobfilipp.com/boat/](https://jacobfilipp.com/boat/)

本文详细介绍了幽默的“粗犷运河船游戏”原型制作过程，该原型源于受电视节目“狭路相逢”启发的一个醉酒后的想法。作者游戏开发经验有限，讲述了他们使用Godot引擎构建游戏时的挣扎和成功。

最初的尝试涉及更简单的方法，但很快失败了，迫使作者学习Godot引擎并与一位开发者朋友合作。该项目耗时两个多月，利用晚上时间进行，包括解决将游戏导出为移动HTML5的挑战。

尽管游戏时长只有短短的三分钟，但作者强调了Godot的强大和用户友好性，游戏开发的乐趣，以及即使存在错误也能实现令人惊讶的润色程度。关键的经验包括将玩家注意力集中以掩盖缺陷的重要性，在停止进一步调整方面的自律必要性，以及艺术家在提高紧张感方面的价值。文章还提到了使用ChatGPT进行船舶动态模拟以及初学者教程出人意料的帮助。

文章最后以幽默的方式列出了不存在的关卡的音乐版权，详细列出了声音和图形版权，并推荐了一款真正的运河船模拟器。作者厚颜无耻地将游戏的不完整性归咎于“原型”，并宣传了启发整个项目的“狭路相逢”人物的YouTube频道。

---

## 42. 在 Dockerized Flask / Django 应用中使用 Uv 替代 Pip

**原文标题**: Switching Pip to Uv in a Dockerized Flask / Django App

**原文链接**: [https://nickjanetakis.com/blog/switching-pip-to-uv-in-a-dockerized-flask-or-django-app](https://nickjanetakis.com/blog/switching-pip-to-uv-in-a-dockerized-flask-or-django-app)

本文阐述了如何在 Docker 化的 Flask 和 Django 应用中使用 `uv` 替代 `pip` 来管理 Python 依赖，从而显著提升速度（约 10 倍）。

关键步骤包括：

1. **将 `requirements.txt` 替换为 `pyproject.toml`：** 作者建议在 `pyproject.toml` 中定义项目依赖，而不是 `requirements.txt`。 `uv` 会自动创建一个包含正确依赖树的锁定文件。

2. **Dockerfile 修改：**
    * 通过从官方 `uv` Docker 镜像复制静态编译的二进制文件来安装 `uv`。
    * 将 `pyproject.toml` 和 `uv.lock*` (锁定文件) 复制到 Docker 镜像中。
    * 设置环境变量： `UV_COMPILE_BYTECODE=1` (预编译字节码) 和 `UV_PROJECT_ENVIRONMENT` 以避免使用 venv。
    * 将 `pip3-install` 替换为 `uv-install`。 `uv-install` 脚本使用 `uv lock` 来确保锁定文件是最新的，并使用 `uv sync` 根据锁定文件安装依赖。 `--frozen` 标志确保在安装过程中不更新锁定文件，`--no-install-project` 阻止将项目本身作为 Python 包安装（对于项目不是可分发包的 Web 应用很有用）。

3. **管理依赖：** 本文提供了使用自定义 shell 脚本添加、更新和删除依赖的快捷方式（例如，`./run deps:install`，`./run uv add mypackage`，`./run uv:outdated`）。 这些脚本卷挂载 `uv.lock` 文件，以便在主机上更新它。 如果未指定版本，`uv add` 将默认使用最新版本。

本文强调了使用 `uv sync` 和锁定文件进行可重现构建的重要性，并提供了一个演示视频以作进一步说明。

---

## 43. 很少有美国人在遇到付费墙时会付费阅读新闻。

**原文标题**: Few Americans pay for news when they encounter paywalls

**原文链接**: [https://www.pewresearch.org/short-reads/2025/06/24/few-americans-pay-for-news-when-they-encounter-paywalls/](https://www.pewresearch.org/short-reads/2025/06/24/few-americans-pay-for-news-when-they-encounter-paywalls/)

皮尤研究中心2025年6月的研究显示，尽管74%的美国人在网上搜索新闻时遇到付费墙，但过去一年中，绝大多数美国人（83%）没有为新闻付费。面对付费墙时，最常见的反应是寻找其他来源（53%），还有相当一部分人（32%）完全放弃访问。仅有1%的人选择付费访问。

不为新闻付费的主要原因是存在免费替代品（49%），其次是缺乏兴趣（32%）。价格和付费新闻的感知质量是相对不重要的因素。

某些人口群体更倾向于为新闻付费，包括受过高等教育的成年人（27%的大学毕业生）、民主党人（21%）、老年人（25%的65岁及以上人群）以及高收入人群（30%的最高收入群体）。与黑人（11%）和西班牙裔美国人（10%）相比，白人（20%）也更倾向于为新闻付费。该研究于2025年3月调查了9482名美国成年人，以了解这些趋势。

---

## 44. PicoEMP – 一种低成本的电磁故障注入 (EMFI) 工具

**原文标题**: PicoEMP – A low-cost Electromagnetic Fault Injection (EMFI) tool

**原文链接**: [https://github.com/newaetech/chipshouter-picoemp](https://github.com/newaetech/chipshouter-picoemp)

PicoEMP：一款低成本开源电磁故障注入工具，专为爱好者和自学设计，填补了高端ChipSHOUTER留下的空白。它以安全性和成本效益为先，提供了一个“简陋”的工具，但尽管简单，其性能却出乎意料地好。用户需自行构建并确保其安全。

PicoEMP使用树莓派Pico作为控制器，需要PWM输出、脉冲引脚和状态引脚。可以通过铣削PCB（提供Gerber文件）从头开始构建，也可以通过使用预制SMD板进行更简单的组装。由于高压元件的存在，塑料屏蔽对于安全操作至关重要。固件可用于编程Pico，用户需要使用铁氧体磁芯和导线创建自己的电磁注入头。

与ChipSHOUTER相比，PicoEMP的高压电路功率较低，恢复时间较慢。它以固定电压（约250V）运行，具有基本的输出脉冲控制。一个关键的安全特性是其隔离的高压侧，减轻了低端开关相关的触电危险。易于组装的版本会经过耐压测试以验证隔离。该项目欢迎社区贡献和混编。

---

## 45. 时间组装理论

**原文标题**: Assembly Theory of Time

**原文链接**: [https://faculty.ucr.edu/~legneref/Assembly%20Theory.htm](https://faculty.ucr.edu/~legneref/Assembly%20Theory.htm)

时间组装理论
时间组装理论提出了对时间理解的根本性转变，认为时间不仅仅是背景或幻觉，而是一个具有可测量属性的物理对象。该理论由莎拉·沃克和李·克罗宁提出，假定时间具有“大小”和方向性，并单向向前流动。

其核心概念是“组装指数”，这是一种衡量物体复杂性的指标，通过量化为创造该物体而排除的替代方案，反映了选择的进化过程。该理论将进化、信息、记忆、因果关系和选择联系起来，使它们成为物体的物理属性。像计算机或大型语言模型这样的复杂物体，需要一系列先前的物体和事件，这表明宇宙的“记忆”和高组装物体的容量随着时间的推移而增加。

组装理论通过暗示未来是确定的但并非完全可预测的，来解决决定论与偶然性之间的争论。随着物体变得更加复杂和信息丰富，未来会扩展并提供新颖性。传统物理学将生命视为“涌现”，但组装理论认为这种“涌现”物体是根本性的，代表了时间深处的起源。

文章总结说，组装理论表明变化被编码在事件链中，宇宙在时间中扩展，而不仅仅是在空间中。因此，未来是开放式的，并且比我们可能预测的更大。

---

## 46. 在Linux或Windows上构建iOS应用

**原文标题**: Build an iOS app on Linux or Windows

**原文链接**: [https://xtool.sh/tutorials/xtool/first-app/](https://xtool.sh/tutorials/xtool/first-app/)

这篇题为“在Linux或Windows上构建iOS应用”的“文章”存根，遗憾的是几乎没有提供任何可用内容。 它仅说明查看文档需要JavaScript。 因此，由于未提供任何内容，因此无法总结文章的内容或要点。 关键在于令人沮丧的事实，即用户需要启用JavaScript才能访问理解如何在Linux或Windows上构建iOS应用所需的实际文档。

---

## 47. 将LLM映射到Excel上拯救了我对游戏开发的热情

**原文标题**: Mapping LLMs over excel saved my passion for game dev

**原文链接**: [https://danieltan.weblog.lol/2025/06/map-llms-excel-saved-my-passion-for-game-dev](https://danieltan.weblog.lol/2025/06/map-llms-excel-saved-my-passion-for-game-dev)

本文讲述了作者如何在游戏开发项目中克服代码难题，具体来说，是在Unity中为卡牌战斗游戏进行繁琐的数据录入。他们最初使用纸笔和Excel制作了游戏原型，但由于数据结构的复杂性和Unity编辑器的限制，难以将法术和特质描述转换为基于Unity的法术系统。

作者意识到可以将游戏资产表示为代码，这样更易于管理、类型检查和编辑。他们探索了各种方法，最终决定直接将资产数据重写为C#代码。考虑到大型语言模型（LLM）擅长模式匹配，他们设计了一个系统，利用LLM自动将数据从Excel转换为C#代码。

至关重要的是，作者强调了向LLM提供结构和分析的重要性，而不是简单地向其提供原始数据。他们创建了一个详细的提示，引导LLM完成解析、分析和映射过程，包括识别模式、建议缺失的功能以及映射到现有的代码结构。此提示包括上下文、输入格式、列映射、分析步骤和输出格式等部分。

通过设计这种结构化的方法，作者成功地自动化了数据录入过程，减轻了倦怠，并使他们能够专注于游戏开发中更令人愉悦的方面：解决问题和编写解决方案。作者使用了Claude Sonnet 4，并包含指向参考提示的链接。

---

## 48. Show HN: Oasis – 开源3D打印智能生态箱

**原文标题**: Show HN: Oasis – An open-source, 3D-printed smart terrarium

**原文链接**: [https://github.com/justbuchanan/oasis](https://github.com/justbuchanan/oasis)

Oasis：一款开源的、主要采用3D打印的智能生态缸，旨在为喜湿植物创造理想环境。该生态缸配备高功率LED照明、用于维持高湿度的喷雾器、用于空气流通的风扇以及温湿度传感器。它还具备WiFi连接功能，允许用户通过手机或电脑监控和控制环境。

该生态缸的设计，包括CAD模型(CadQuery)、电子元件(KiCad)和软件（使用esp-rs库的Rust语言），都是完全开源的，并在链接的存储库中提供。虽然该项目的大部分对于拥有3D打印机的用户来说是DIY友好的，但电子元件需要更高级的技能或访问像JLCPCB这样的PCB组装服务。

创建者正考虑未来提供预组装的电子元件套件，并提供了Google表格链接，供有兴趣表达意愿和接收更新的用户填写。生态缸本身的直径约为8英寸，高约13英寸。感兴趣的用户可以在Oasis生态缸网站上找到更多细节、图片和构建说明。

---

## 49. FICO 将把先买后付贷款纳入信用评分

**原文标题**: FICO to incorporate buy-now-pay-later loans into credit scores

**原文链接**: [https://www.axios.com/2025/06/23/fico-credit-scores-bnpl-buy-now-pay-later](https://www.axios.com/2025/06/23/fico-credit-scores-bnpl-buy-now-pay-later)

无法访问文章链接。

---

## 50. 塑料清单 – 食品中塑料含量

**原文标题**: PlasticList – Plastic Levels in Foods

**原文链接**: [https://www.plasticlist.org/](https://www.plasticlist.org/)

塑胶清单 – 食品中塑胶含量

内容为“塑胶清单”，因此概要如下：

“塑胶清单”可能旨在：

*   探讨食品中塑胶的存在
*   量化塑胶含量
*   提供清单或分类

总而言之，“塑胶清单”可能提供各种食品中塑胶污染程度的信息。缺乏清单实际内容，无法进行更详细的概要。

---

## 51. 北欧半导体收购Memfault

**原文标题**: Nordic Semiconductor Acquires Memfault

**原文链接**: [https://www.nordicsemi.com/Nordic-news/2025/06/Nordic-Semiconductor-acquires-Memfault](https://www.nordicsemi.com/Nordic-news/2025/06/Nordic-Semiconductor-acquires-Memfault)

Nordic Semiconductor 收购互联产品云平台供应商 Memfault，标志着 Nordic 向提供硬件、软件和云服务的完整解决方案合作伙伴转型。此次收购旨在简化开发，加速产品上市时间，并通过贯穿产品整个生命周期的持续软件升级，加强产品安全性、性能和功能。

Memfault 的设备可观测性、管理和安全 OTA 更新将被集成到 Nordic 的产品组合和 nRF Cloud 平台中。Nordic 强调致力于 Memfault 的持续开发，并为所有物联网设备制造商提供支持，无论其硬件选择如何。

整合后的产品将创建一个全栈解决方案，使客户能够管理数百万台现场设备，进行创新，并满足不断发展的行业和监管期望，包括边缘 AI 和欧盟网络弹性法案等安全标准。 Nordic 相信这将缩短产品上市时间，降低运营成本，并实现有效的产品生命周期管理。

---

## 52. 在Power Mac G3 ROM中找到一个27年前的彩蛋

**原文标题**: Finding a 27-year-old easter egg in the Power Mac G3 ROM

**原文链接**: [https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/](https://www.downtowndougbrown.com/2025/06/finding-a-27-year-old-easter-egg-in-the-power-mac-g3-rom/)

2025年6月，道格·布朗详细描述了他发现的Power Mac G3 ROM（1997-1999年型号中使用）中先前未记录的一个彩蛋。在使用Hex Fiend和Mac ROM模板探索ROM时，他发现了G3团队的JPEG图像（HPOE资源）以及“Native 4.3”（SCSI管理器）资源中的Pascal字符串，特别是字符串“secret ROM image”。

受早期PowerPC Mac中类似彩蛋的启发，他使用Ghidra反汇编了SCSI管理器代码。反编译的代码显示，如果RAM磁盘卷命名为“secret ROM image”（不区分大小写），代码将从资源HPOE ID 1加载JPEG图像数据，创建一个名为“The Team”的文件，其创建者为“ttxt”，类型为“JPEG”，将图像数据写入该文件，然后关闭它。

激活需要格式化RAM磁盘并在格式化过程中将其命名为“secret ROM image”。此操作将触发在RAM磁盘中创建包含该图像的“The Team”文件。道格赞扬了Libera上#mac68k的^alex，他发现了格式化RAM磁盘的关键步骤。该彩蛋似乎可以在Mac OS 9.0.4上运行，但在9.1及更高版本中可能已被禁用。道格推测这可能是史蒂夫·乔布斯据报道禁止彩蛋之前的最后一个彩蛋之一，并希望与曾在该团队工作的苹果前员工联系，以了解更多关于这个秘密的信息。

---

## 53. 规则压倒目标

**原文标题**: Rules Clobber Goals

**原文链接**: [https://kupajo.com/rules-clobber-goals/](https://kupajo.com/rules-clobber-goals/)

规则胜于目标：实现持久改变的关键

---

## 54. MCP正在吞噬世界。

**原文标题**: MCP is eating the world

**原文链接**: [https://www.stainless.com/blog/mcp-is-eating-the-world--and-its-here-to-stay](https://www.stainless.com/blog/mcp-is-eating-the-world--and-its-here-to-stay)

无法访问文章链接。

---

## 55. 位于马里兰州学院公园的国家档案馆将成为受限联邦设施。

**原文标题**: National Archives at College Park, MD, will become a restricted federal facility

**原文链接**: [https://www.archives.gov/college-park](https://www.archives.gov/college-park)

位于马里兰州大学园的国家档案馆保存着联邦机构创建的永久记录，包括民事机构的文本记录、军事单位记录、静态图片、电子记录、制图和建筑资料、电影、声音和视频记录，以及诸如肯尼迪遇刺案记录和柏林文献中心缩微胶卷等特定馆藏。

该机构位于马里兰州大学园阿德尔菲路8601号，卡车送货使用梅策罗特路3301号入口。研究室周一至周五上午 9 点至下午 5 点开放，强烈建议通过 Eventbrite 预约研究。也允许直接进入。

研究人员可以联系特定部门进行事先咨询和预约问题：文本咨询，邮箱：archives2reference@nara.gov；研究人员注册，邮箱：visit_archives2@nara.gov；制图，邮箱：consultation.carto@nara.gov；静态图片，邮箱：consultation.stillpix@nara.gov；移动图像和声音，邮箱：mopix@nara.gov。

网站提供了查找辅助工具、军事记录、在线研究工具和订购信息的链接。访问者可以找到路线、研究室政策以及到达后的预期事项。网站提供主要工作人员和部门的联系方式。国家档案馆还提供志愿者和实习机会，以及教育工作者资源。

---

## 56. ReBarUEFI：几乎适用于任何UEFI系统的可调整大小的BAR

**原文标题**: ReBarUEFI: Resizable BAR for almost any UEFI system

**原文链接**: [https://github.com/xCuri0/ReBarUEFI](https://github.com/xCuri0/ReBarUEFI)

ReBarUEFI是一个UEFI DXE驱动，可以在缺乏官方支持的系统上启用Resizable BAR（基址寄存器）功能。Resizable BAR可以提高性能，尤其是在Intel Arc GPU上。

要使用ReBarUEFI，用户必须：

1.  **在BIOS中启用4G解码**。如果该选项被隐藏，维基指南提供了相关说明。至少需要1GB的BAR大小，可能需要通过减少TOLUD来增加到2GB。
2.  **(可选)** 使用UEFIPatch应用BIOS补丁来修复Large BAR支持问题。补丁解决了大小限制（4GB、16GB、64GB）、降级预防、MMIO空间增加、NVRAM白名单移除和USB 3.0问题。
3.  **将ReBarUEFI模块添加到**UEFI固件的DXE卷。维基指南涵盖了该过程。
4.  刷新修改后的固件后，**禁用CSM**。
5.  **使用ReBarState**（可在发布版本中获取或使用CMake构建）来设置Resizable BAR大小。推荐大小为32（无限制），但如果遇到问题，可能需要较小的大小。
6.  报告主板兼容性

ReBarUEFI模块会修改PciHostBridgeResourceAllocationProtocol，以根据ReBarState NVRAM变量中设置的大小启用Resizable BAR。

该文本还提供了常见问题的解决方案、构建说明、常见问题解答，并感谢了为该项目做出贡献的贡献者。值得注意的是，该项目在PCIE Gen2系统上取得了一些成功，并且该项目使得在Linux下无需修改BIOS。

---

## 57. 工程师为什么讨厌他们的经理 (以及该如何解决)

**原文标题**: Why Engineers Hate Their Managers (and What to Do About It)

**原文链接**: [https://terriblesoftware.org/2025/06/24/why-engineers-hate-their-managers-and-what-to-do-about-it/](https://terriblesoftware.org/2025/06/24/why-engineers-hate-their-managers-and-what-to-do-about-it/)

本文探讨了工程师对管理者常见的 frustations，源于作者在双方角色的经验。它指出了低效管理者表现出的关键“反模式”：不必要的会议和打断干扰工程师的专注力（“千次同步之死”），做出不明智的技术决策（“只是一个按钮”问题），窃取工程师的功劳（“隐形工程师综合症”），安排过多的会议（“会议漩涡”），以及在绩效评估中提供泛泛而无用的反馈（“反馈剧场”）。

文章承认管理具有挑战性，管理者常常夹在苛刻的高管和苦苦挣扎的团队之间，并受到他们无法直接控制的指标的衡量。它强调许多有问题的管理行为源于这些压力，而不是恶意。

作者提出，优秀的工程管理者应优先保护专注时间，保持技术能力以做出明智的决策，在承担失败责任的同时将功劳归于团队，并提供有意义的、及时的反馈。 关键在于工程师并非天生讨厌管理者，而是讨厌不良的管理 practices。公开的沟通以及对角色和挑战的相互理解对于创建高性能团队至关重要，在这种团队中，工程师感到被倾听，管理者感到被支持，技术现实与业务需求相符。

---

## 58. 星舰：适用于任何Shell的极简、快速、可定制的提示符

**原文标题**: Starship: A minimal, fast, and customizable prompt for any shell

**原文链接**: [https://starship.rs/](https://starship.rs/)

Starship：极简、快速、高度可定制的 Shell 提示符。其核心价值在于广泛的兼容性，可在各种常见 Shell 和操作系统上运行。这种通用性让用户无论使用何种 Shell 或操作系统，都能获得一致且个性化的提示符体验。总之，Starship 旨在提供一种适用于各种计算环境的多功能高效提示符解决方案。

---

## 59. 循环微型计算机：由再生智能手机组件嵌入和供电

**原文标题**: Circular Microcomputers embedded and powered by repurposed smartphone components

**原文链接**: [https://citronics.eu/](https://citronics.eu/)

Citronics提供“循环微型计算机”，这是一种利用回收智能手机组件供电的嵌入式计算机，为传统计算解决方案提供了一种可持续且经济高效的替代方案。 这些基于Linux的微型计算机拥有4G LTE、WiFi和以太网连接，并且可扩展至1到10,000个设备。

Citronics面向教育、能源和工业等各种应用，提供原型设计、定制嵌入式计算机以及基于云的管理和监控服务解决方案。 他们强调精简的开发周期（“开发 – 部署 – 评估 – 重复”），并支持开源框架。 该公司还提供工程培训和指导。

该文章重点介绍了几个成功的用例，包括Destore的住宅供暖优化、UCLouvain的边缘计算图像识别集群、Karno的区域供暖监控网关以及可持续显示解决方案。

Citronics将其技术定位为具有竞争力，提供高性能价格比、缩短上市时间以及独立于亚洲供应商的安全供应链。 他们还强调使用回收组件带来的品牌和可持续性优势。 他们提供150欧元（不含增值税）的上市价格，并鼓励潜在客户联系他们、预约通话或预订。

---

## 60. 美国国家科学基金会因住房及城市发展部被赶出总部

**原文标题**: NSF getting kicked out of headquarters by HUD

**原文链接**: [https://www.bloomberg.com/news/articles/2025-06-25/hud-plans-to-move-operations-from-washington-to-virginia](https://www.bloomberg.com/news/articles/2025-06-25/hud-plans-to-move-operations-from-washington-to-virginia)

无法访问文章链接。

---

## 61. 关于GPU的基本知识

**原文标题**: Basic Facts about GPUs

**原文链接**: [https://damek.github.io/random/basic-facts-about-gpus/](https://damek.github.io/random/basic-facts-about-gpus/)

本文概述了GPU架构和优化技术，重点在于实现GPU内核中的高性能。它解释了计算和内存层次结构，突出了NVIDIA A100等GPU中快速计算与较慢内存访问之间的不平衡。介绍了Roofline模型，阐述了基于内存带宽和计算吞吐量的性能限制，并定义了算术强度（AI）的概念。

本文指出了两种性能状态：内存受限（受数据传输速度限制）和计算受限（受算术速度限制）。它强调了最大化数据重用以提高AI并将内核转移到计算受限区域的重要性。讨论了两种关键的优化策略：算子融合和分块。算子融合将多个内存受限的操作合并到一个内核中，以消除中间内存流量，而分块涉及划分计算并利用快速片上共享内存来最大化数据重用，以用于诸如矩阵乘法之类的计算密集型任务。

最后，本文简要地将开销作为第三个潜在的性能限制因素进行了讨论，强调需要足够大的内核和异步执行，以最大程度地减少CPU-GPU通信瓶颈。最后，重点介绍了分块的加载、同步和计算模式，其中数据被加载到共享内存中，线程同步，然后执行计算。

---

## 62. 科学家发现细胞内未知细胞器

**原文标题**: Scientists discover unknown organelle inside our cells

**原文链接**: [https://phys.org/news/2025-06-scientists-unknown-organelle-cells.html](https://phys.org/news/2025-06-scientists-unknown-organelle-cells.html)

弗吉尼亚大学医学院和美国国立卫生研究院的科学家们在一项突破性发现中，识别出细胞内一种先前未知的细胞器，并将其命名为“半融合体”。这种新的细胞器在细胞的分拣、回收和物质处理中发挥着关键作用，充当囊泡的“装卸码头”，囊泡负责在细胞内运输货物。

研究人员利用冷冻电子断层扫描技术观察到半融合体，它似乎促进了囊泡和多囊泡体的形成。这一发现意义重大，因为它为我们理解细胞如何管理内部废物和资源提供了新的视角。

科学家们认为，半融合体功能障碍可能导致遗传疾病，如Hermansky-Pudlak综合征，该综合征会破坏细胞货物的正常处理。了解半融合体在健康和患病细胞中的作用，可能为各种遗传疾病的新靶向治疗铺平道路。研究人员计划研究半融合体在健康细胞中的功能以及功能障碍时会发生什么，从而可能带来创新的治疗策略。相关研究结果发表在《自然通讯》杂志上。

---

## 63. 代币化的惨痛教训即将到来

**原文标题**: The bitter lesson is coming for tokenization

**原文链接**: [https://lucalp.dev/bitter-lesson-tokenization-and-blt/](https://lucalp.dev/bitter-lesson-tokenization-and-blt/)

本文认为，分词是当前大型语言模型（LLM）的核心组成部分，但也是阻碍模型性能的瓶颈。“苦涩的教训”原则——倾向于利用大量计算和数据的一般用途方法——表明分词最终将被取代。分词，特别是字节对编码（BPE），将文本压缩成一个token词汇表，虽然影响效率，但也引入了诸如token建模不佳和信息丢失等问题。

尽管诸如思维链和RAG等技术解决了一些分词的缺点，但作者质疑由于次优分词，有多少潜在的模型能力仍未被挖掘。直接删除分词并恢复到字节级别建模已被探索，但像ByT5这样的初步尝试在训练时间和推理速度方面面临挑战，尽管显示出潜力。

本文然后深入研究旨在学习分词并在模型内部压缩表示的架构，例如CANINE、Charformer和Hourglass Transformers。这些方法采用下采样和上采样技术来降低计算复杂度，同时保持信息。最近的进展，如具有动态token池化的高效Transformer，探索学习动态补丁边界以实现更高效的处理。总体方向是创建可以从字节序列直接学习最佳表示的端到端模型，从而可能消除对显式分词的需求，并释放进一步的扩展能力。

---

## 64. 2025年玩《毁灭战士》，或，泥塑

**原文标题**: Playing Doom in 2025, Or, Sculpture from Clay

**原文链接**: [https://rjp.io/blog/2025-06-19-playing-doom-in-2025](https://rjp.io/blog/2025-06-19-playing-doom-in-2025)

2025年，作者发现并乐于体验一张名为“我的房子”的毁灭战士地图，惊叹于其复杂、怪诞和令人不安的设计中所倾注的创造力和努力。受《叶子小屋》启发，这张地图凸显了毁灭战士Mod社区的持久魅力以及旧技术在激发创造力方面的持久力量。

作者反思了什么让一个工具长期具有价值，认为软件的个性化和创造性再利用能力，正如毁灭战士Mod和电子表格颠覆所见，是关键所在。作者想知道开发者是否可以创造更多类似电子表格和毁灭战士引擎的工具，从而赋能非程序员表达他们的创造力。

文章将毁灭战士Mod与80年代的Hypercard应用程序相提并论，两者都是易于使用的创意表达的例子。作者感叹自网络兴起以来（不包括Flash），非程序员构建有趣应用的机会减少，并看到了大型语言模型（LLM）和Scrappy等项目通过简化开发过程来恢复这种自主性的希望。

最终，作者强调了通过易于使用的工具来激发他人创造力的价值，并得出结论：对毁灭战士地图社区的观察凸显了这一目标的重要性。

---

## 65. 简街高管称其受骗资助政变用AK-47步枪

**原文标题**: Jane Street Boss Says He Was Duped into Funding AK-47s for Coup

**原文链接**: [https://www.bloomberg.com/news/articles/2025-06-25/jane-street-s-rob-granieri-says-he-was-duped-into-funding-south-sudan-coup-plot](https://www.bloomberg.com/news/articles/2025-06-25/jane-street-s-rob-granieri-says-he-was-duped-into-funding-south-sudan-coup-plot)

无法访问文章链接。

---

## 66. Show HN: VSCan - 检测恶意 VSCode 扩展

**原文标题**: Show HN: VSCan - Detect Malicious VSCode Extensions

**原文链接**: [https://vscan.dev/](https://vscan.dev/)

VSCan是一款用于检测恶意VSCode扩展的工具。它提供一项服务，基于VSCode Marketplace的名称或ID来分析扩展。该过程包括获取扩展的代码、权限和元数据以进行深度分析。然后，VSCan生成一份报告，详细说明潜在风险和向用户的建议。该平台强调分析过程的透明性。

该工具还提供了一个最近分析的部分，允许用户快速检查常用扩展。VSCan强调其记录，指出已扫描超过10,000个扩展并识别出超过500个漏洞。它还提到全天候监控。

---

## 67. 基于 SQLite 的检索增强生成

**原文标题**: Retrieval Augmented Generation Based on SQLite

**原文链接**: [https://github.com/ggozad/haiku.rag](https://github.com/ggozad/haiku.rag)

Haiku SQLite RAG is a Retrieval-Augmented Generation library built on SQLite, offering a local, serverless RAG solution. It supports various embedding providers like Ollama, VoyageAI, and OpenAI, facilitating hybrid search using vector search (sqlite-vec) and full-text search (FTS5) with Reciprocal Rank Fusion.

Key features include:

*   **Local SQLite Database:** Eliminates the need for external servers.
*   **Diverse Embedding Support:** Integrates with Ollama, VoyageAI, and OpenAI.
*   **Hybrid Search:** Combines vector and full-text search for enhanced retrieval.
*   **File Monitoring:** Automatically indexes files in specified directories.
*   **Extensive File Support:** Parses over 40 file formats and URLs.
*   **MCP Server:** Exposes RAG functionality as tools for AI assistants.
*   **CLI & Python Client:** Offers command-line tools and a Python client for interaction.

The library can be installed using `uv pip install haiku.rag`. Configuration is done through environment variables, allowing users to specify embedding providers, API keys, and monitored directories.

The CLI provides commands for managing documents (add, list, get, delete) and performing searches. The `haiku-rag serve` command starts a file monitoring and MCP server for automatic indexing and tool exposure.

The Python client enables programmatic interaction with the RAG system, providing functionalities for creating, retrieving, updating, deleting, and searching documents.


---

## 68. Gemini Robotics On-Device brings AI to local robotic devices

**原文标题**: Gemini Robotics On-Device brings AI to local robotic devices

**原文链接**: [https://deepmind.google/discover/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/](https://deepmind.google/discover/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/)

生成摘要时出错

---

## 69. SFStreets: History of San Francisco place names

**原文标题**: SFStreets: History of San Francisco place names

**原文链接**: [http://sfstreets.noahveltman.com/](http://sfstreets.noahveltman.com/)

生成摘要时出错

---

## 70. Japan Adventures: A Designer's Perspective

**原文标题**: Japan Adventures: A Designer's Perspective

**原文链接**: [https://www.tombihn.com/blogs/main/tokyo-adventures-a-designers-perspective](https://www.tombihn.com/blogs/main/tokyo-adventures-a-designers-perspective)

生成摘要时出错

---

## 71. Is mathematics mostly chaos or mostly order?

**原文标题**: Is mathematics mostly chaos or mostly order?

**原文链接**: [https://www.quantamagazine.org/is-mathematics-mostly-chaos-or-mostly-order-20250620/](https://www.quantamagazine.org/is-mathematics-mostly-chaos-or-mostly-order-20250620/)

生成摘要时出错

---

## 72. Advanced Python Function Debugging with MCP Integration

**原文标题**: Advanced Python Function Debugging with MCP Integration

**原文链接**: [https://github.com/kordless/gnosis-mystic](https://github.com/kordless/gnosis-mystic)

生成摘要时出错

---

## 73. Solving LinkedIn Queens Using Haskell

**原文标题**: Solving LinkedIn Queens Using Haskell

**原文链接**: [https://imiron.io/post/linkedin-queens/](https://imiron.io/post/linkedin-queens/)

生成摘要时出错

---

## 74. Gemini CLI Accidentally Published

**原文标题**: Gemini CLI Accidentally Published

**原文链接**: [https://web.archive.org/web/20250625051706/https://blog.google/technology/developers/introducing-gemini-cli/](https://web.archive.org/web/20250625051706/https://blog.google/technology/developers/introducing-gemini-cli/)

生成摘要时出错

---

## 75. Vera C. Rubin Observatory first images

**原文标题**: Vera C. Rubin Observatory first images

**原文链接**: [https://rubinobservatory.org/news/rubin-first-look/cosmic-treasure-chest](https://rubinobservatory.org/news/rubin-first-look/cosmic-treasure-chest)

生成摘要时出错

---

## 76. Mid-sized cities outperform major metros at turning economic growth into patents

**原文标题**: Mid-sized cities outperform major metros at turning economic growth into patents

**原文链接**: [https://www.governance.fyi/p/booms-not-busts-drives-innovation](https://www.governance.fyi/p/booms-not-busts-drives-innovation)

生成摘要时出错

---

## 77. The Jumping Frenchmen of Maine

**原文标题**: The Jumping Frenchmen of Maine

**原文链接**: [https://www.amusingplanet.com/2025/06/the-jumping-frenchmen-of-maine.html](https://www.amusingplanet.com/2025/06/the-jumping-frenchmen-of-maine.html)

生成摘要时出错

---

## 78. The economics behind "Basic Economy" – A masterclass in price discrimination

**原文标题**: The economics behind "Basic Economy" – A masterclass in price discrimination

**原文链接**: [https://blog.getjetback.com/the-economics-behind-basic-economy-a-masterclass-in-price-discrimination/](https://blog.getjetback.com/the-economics-behind-basic-economy-a-masterclass-in-price-discrimination/)

生成摘要时出错

---

## 79. Show HN: Autumn – Open-source infra over Stripe

**原文标题**: Show HN: Autumn – Open-source infra over Stripe

**原文链接**: [https://github.com/useautumn/autumn](https://github.com/useautumn/autumn)

生成摘要时出错

---

## 80. A brief history of hardware epidemics

**原文标题**: A brief history of hardware epidemics

**原文链接**: [https://eclecticlight.co/2025/06/21/a-brief-history-of-hardware-epidemics/](https://eclecticlight.co/2025/06/21/a-brief-history-of-hardware-epidemics/)

生成摘要时出错

---

## 81. Lyon Drops Microsoft to Boost Digital Sovereignty

**原文标题**: Lyon Drops Microsoft to Boost Digital Sovereignty

**原文链接**: [https://digitrendz.blog/newswire/business/19813/lyon-drops-microsoft-office-to-boost-digital-sovereignty/](https://digitrendz.blog/newswire/business/19813/lyon-drops-microsoft-office-to-boost-digital-sovereignty/)

生成摘要时出错

---

## 82. The German automotive industry wants to develop open-source software together

**原文标题**: The German automotive industry wants to develop open-source software together

**原文链接**: [https://www.vda.de/en/press/press-releases/2025/250624_PM_Automotive_industry_signs_Memorandum_of_Understanding](https://www.vda.de/en/press/press-releases/2025/250624_PM_Automotive_industry_signs_Memorandum_of_Understanding)

生成摘要时出错

---

## 83. Amoeba: A distributed operating system for the 1990s (1990) [pdf]

**原文标题**: Amoeba: A distributed operating system for the 1990s (1990) [pdf]

**原文链接**: [https://www.cs.cornell.edu/home/rvr/papers/Amoeba1990s.pdf](https://www.cs.cornell.edu/home/rvr/papers/Amoeba1990s.pdf)

生成摘要时出错

---

## 84. The Fairphone (Gen. 6)

**原文标题**: The Fairphone (Gen. 6)

**原文链接**: [https://shop.fairphone.com/the-fairphone-gen-6](https://shop.fairphone.com/the-fairphone-gen-6)

生成摘要时出错

---

## 85. Timdle – Place historical events in chronological order

**原文标题**: Timdle – Place historical events in chronological order

**原文链接**: [https://www.timdle.com/](https://www.timdle.com/)

生成摘要时出错

---

## 86. Marble Blast

**原文标题**: Marble Blast

**原文链接**: [https://marbleblast.vaniverse.io/](https://marbleblast.vaniverse.io/)

生成摘要时出错

---

## 87. Svalboard: Datahand Lives

**原文标题**: Svalboard: Datahand Lives

**原文链接**: [https://svalboard.com/](https://svalboard.com/)

生成摘要时出错

---

## 88. How renewables are saving Texans billions

**原文标题**: How renewables are saving Texans billions

**原文链接**: [https://www.theclimatebrink.com/p/how-renewables-are-saving-texans](https://www.theclimatebrink.com/p/how-renewables-are-saving-texans)

生成摘要时出错

---

## 89. 'Dragon prince' dinosaur discovery 'rewrites' T.rex family tree

**原文标题**: 'Dragon prince' dinosaur discovery 'rewrites' T.rex family tree

**原文链接**: [https://www.bbc.com/news/articles/cy8dzv3vp5jo](https://www.bbc.com/news/articles/cy8dzv3vp5jo)

生成摘要时出错

---

## 90. Why is my Raspberry Pi 4 too slow as a server?

**原文标题**: Why is my Raspberry Pi 4 too slow as a server?

**原文链接**: [https://ergaster.org/posts/2025/06/24-why-restore-raspi-slow/](https://ergaster.org/posts/2025/06/24-why-restore-raspi-slow/)

生成摘要时出错

---

## 91. OpenADP, needs volunteers to help prevent mass secret surveillance

**原文标题**: OpenADP, needs volunteers to help prevent mass secret surveillance

**原文链接**: [https://openadp.org](https://openadp.org)

生成摘要时出错

---

## 92. Fedora 44 Looks to Drop I686 Support: No More Multi-Lib / x86 32-Bit Packages

**原文标题**: Fedora 44 Looks to Drop I686 Support: No More Multi-Lib / x86 32-Bit Packages

**原文链接**: [https://www.phoronix.com/news/Fedora-43-Change-No-i686](https://www.phoronix.com/news/Fedora-43-Change-No-i686)

生成摘要时出错

---

## 93. The Mathematics of Juggling [video]

**原文标题**: The Mathematics of Juggling [video]

**原文链接**: [https://www.youtube.com/watch?v=0FSWzr5kjhg](https://www.youtube.com/watch?v=0FSWzr5kjhg)

生成摘要时出错

---

## 94. Fairphone 6 is switching to a new design that's even more sustainable

**原文标题**: Fairphone 6 is switching to a new design that's even more sustainable

**原文链接**: [https://www.androidcentral.com/phones/fairphone-6-official-render-leaks-showcase-its-sustainable-design](https://www.androidcentral.com/phones/fairphone-6-official-render-leaks-showcase-its-sustainable-design)

生成摘要时出错

---

## 95. Backyard Coffee and Jazz in Kyoto

**原文标题**: Backyard Coffee and Jazz in Kyoto

**原文链接**: [https://thedeletedscenes.substack.com/p/backyard-coffee-and-jazz-in-kyoto](https://thedeletedscenes.substack.com/p/backyard-coffee-and-jazz-in-kyoto)

生成摘要时出错

---

## 96. Battery-electric "Infinity Train" will charge itself using gravity

**原文标题**: Battery-electric "Infinity Train" will charge itself using gravity

**原文链接**: [https://newatlas.com/transport/fortescue-wae-infinity-train-electric/](https://newatlas.com/transport/fortescue-wae-infinity-train-electric/)

生成摘要时出错

---

## 97. A grad student got LHC data to play nice with quantum interference

**原文标题**: A grad student got LHC data to play nice with quantum interference

**原文链接**: [https://arstechnica.com/science/2025/06/how-a-grad-student-got-lhc-data-to-play-nice-with-quantum-interference/](https://arstechnica.com/science/2025/06/how-a-grad-student-got-lhc-data-to-play-nice-with-quantum-interference/)

生成摘要时出错

---

## 98. ChatGPT Is Becoming a Religion

**原文标题**: ChatGPT Is Becoming a Religion

**原文链接**: [https://www.youtube.com/watch?v=zKCynxiV_8I](https://www.youtube.com/watch?v=zKCynxiV_8I)

生成摘要时出错

---

## 99. Early US Intel assessment suggests strikes on Iran did not destroy nuclear sites

**原文标题**: Early US Intel assessment suggests strikes on Iran did not destroy nuclear sites

**原文链接**: [https://www.cnn.com/2025/06/24/politics/intel-assessment-us-strikes-iran-nuclear-sites](https://www.cnn.com/2025/06/24/politics/intel-assessment-us-strikes-iran-nuclear-sites)

生成摘要时出错

---

## 100. Resurrecting flip phone typing as a Linux driver

**原文标题**: Resurrecting flip phone typing as a Linux driver

**原文链接**: [https://github.com/FoxMoss/libt9](https://github.com/FoxMoss/libt9)

生成摘要时出错

---

