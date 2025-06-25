# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-06-25.md)

*最后自动更新时间: 2025-06-25 17:50:02*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 2 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 3 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 4 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 5 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 6 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 7 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 8 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 9 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 10 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 11 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 12 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 13 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 14 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 15 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 16 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 17 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 18 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 19 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 20 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 21 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 22 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 23 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 24 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 25 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 26 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 27 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 28 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 29 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 30 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 31 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 32 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 33 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 34 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 35 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 36 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 37 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 38 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 39 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 40 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 41 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 42 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 43 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 44 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 45 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 46 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 47 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 48 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 49 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 50 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 51 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 52 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 53 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 54 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 55 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 56 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 57 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 58 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 59 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 60 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 61 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 62 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 63 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 64 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 65 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 66 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 67 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 68 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 69 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 70 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 71 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 72 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 73 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 74 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 75 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 76 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 77 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 78 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 79 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 80 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 81 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 82 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 83 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 84 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 85 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 86 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 87 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 88 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 89 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 90 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 91 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 92 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 93 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 94 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 95 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 96 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 97 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 98 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
