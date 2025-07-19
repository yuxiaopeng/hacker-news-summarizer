# Hacker News 热门文章摘要 (2025-07-19)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 重新思考人工智能的命令行界面

**原文标题**: Rethinking CLI Interfaces for AI

**原文链接**: [https://www.notcheckmark.com/2025/07/rethinking-cli-interfaces-for-ai/](https://www.notcheckmark.com/2025/07/rethinking-cli-interfaces-for-ai/)

本文认为，当前的命令行工具和API在设计上不适合LLM代理有效使用，特别是那些受限于小上下文窗口的代理。作者重点指出了在开发IDA Pro MCP接口时遇到的问题，即API需要在便利性和完整性之间取得平衡，需要诸如详细的文档字符串等变通方法来指导LLM的行为。

命令行工具也存在类似问题。LLM通常使用低效的方法，如`head -n100`，或者难以处理目录上下文。作者回顾了使用Claude Code的经历，它绕过了预提交钩子，尽管有指令和linter，甚至试图修改这些钩子本身。为了解决这个问题，作者实现了一个git wrapper，可以防止绕过这些钩子。

作者提倡采用“信息架构”方法进行CLI设计，认为观察代理对现有工具的困惑可以揭示它们的不足。我们不应仅仅训练LLM使用现有工具，而应该用上下文信息增强它们并调整它们的输出。

具体建议包括包装像`head`这样的命令以缓存输出、提供结构化数据并指示剩余行数。Shell钩子还可以通过在命令失败时建议正确的目录来帮助目录导航。

最终，作者建议创建LLM增强的CLI工具或自定义LLM Shell，这可能会在UX领域产生一个新的“AI体验”分支，专注于为AI代理定制的信息架构。目标是减少不必要的工具调用，优化上下文窗口，并提高整体LLM代理的效率。

---

## 2. 向人们展示人工智能生成的内容是不礼貌的。

**原文标题**: It's rude to show AI output to people

**原文链接**: [https://distantprovince.by/posts/its-rude-to-show-ai-output-to-people/](https://distantprovince.by/posts/its-rude-to-show-ai-output-to-people/)

Alex Martsinovich认为，与他人分享人工智能生成的内容本质上是粗鲁且可能有害的，他将此比作彼得·沃茨的小说《盲视》中外星物种，后者认为人类交流是一种攻击，因为其信噪比太低。他提出，人工智能生成的文本缺乏“思考证明”，这种品质以前是书面材料固有的，因为它包含人类的创作努力。现在人工智能使得生成文本变得极其廉价，它可能变成一种“毒药”，浪费接收者的时间和认知资源。

Martsinovich强调，虽然将人工智能用于个人目的是可以接受的，但在未经他人同意或未将其视为自己想法的情况下，传播其输出内容会使其合法化，并侵犯接收者的认知空间。他提倡制定“人工智能礼仪”，建议只有在发送者真正采纳人工智能的输出内容作为自己的想法，或者接收者明确同意接收的情况下，才能分享人工智能的输出内容。他用对话场景的例子来说明他认为将人工智能生成的内容纳入交流中的粗鲁和可接受的方式。核心论点是，尊重他人的注意力和认知资源需要仔细考虑何时以及如何分享人工智能生成的文本。

---

## 3. OpenAI声称在2025年国际数学奥林匹克竞赛中获得金牌

**原文标题**: OpenAI claims gold-medal performance at IMO 2025

**原文链接**: [https://twitter.com/alexwei_/status/1946477742855532918](https://twitter.com/alexwei_/status/1946477742855532918)

“OpenAI 声称在 2025 年 IMO 获得金牌”这篇文章实际上是来自 X (前身为 Twitter) 的一条由于 JavaScript 被禁用而无法访问的消息。提供的内容仅包含此错误消息和标准的 X 样板法律和版权信息。

因此，**没有实际的文章内容可以概括。** 标题暗示 OpenAI 声称在 2025 年国际数学奥林匹克竞赛中获得金牌，但由于无法访问 X 帖子，因此无法确认这一说法，了解上下文，或提供任何有意义的总结。提供的文本只是一个阻止访问预期内容的错误消息。

---

## 4. 放弃Element和Matrix.org

**原文标题**: Giving Up on Element and Matrix.org

**原文链接**: [https://xn--gckvb8fzb.com/giving-up-on-element-and-matrixorg/](https://xn--gckvb8fzb.com/giving-up-on-element-and-matrixorg/)

作者在使用五年后对 Matrix.org/Element 生态系统的幻灭：重返 XMPP

---

## 5. Linux和安全启动证书过期

**原文标题**: Linux and Secure Boot certificate expiration

**原文链接**: [https://lwn.net/SubscriberLink/1029767/43b62a7a7408c2a9/](https://lwn.net/SubscriberLink/1029767/43b62a7a7408c2a9/)

这篇2025年7月16日LWN.net的文章讨论了微软用于签署Linux系统安全启动shim引导程序的2011年密钥即将于2025年9月到期的问题。在此日期之后，除非存在新的微软2023密钥，否则使用旧密钥签署的安装介质将无法在启用安全启动的系统上启动。

固件更新的分散状态使问题变得复杂。许多系统可能未安装新密钥。供应商需要提供固件更新来添加它，可能通过LVFS和fwupd的“密钥交换密钥”(KEK)更新。旧版本的fwupd存在问题，但新版本有所改进。一些较旧的系统可能需要重置BIOS，因为用于更新的EFI变量空间有限。

文章强调了潜在的问题，例如供应商更新失败以及一家制造商失去对其平台密钥的访问权限。关于固件是否会实际执行2011年密钥的到期日也存在不确定性。虽然具有工作信任链的现有系统可能会继续启动，但使用旧密钥签署的更新将不再可能。

文章讨论了一种可能的解决方法，即为没有新密钥的系统提供旧版本的shim，但由于未修补的漏洞，这会带来安全问题。总的来说，这篇文章强调了由于供应商控制根信任密钥以及支持的硬件范围广泛，因此在Linux上维护安全启动兼容性的困难。

---

## 6. 目前还没有人知道如何用人工智能进行构建。

**原文标题**: Nobody knows how to build with AI yet

**原文链接**: [https://worksonmymachine.substack.com/p/nobody-knows-how-to-build-with-ai](https://worksonmymachine.substack.com/p/nobody-knows-how-to-build-with-ai)

无法访问文章链接。

---

## 7. 已知存在问题的邮件客户端

**原文标题**: Known Bad Email Clients

**原文链接**: [https://www.emailprivacytester.com/badClients](https://www.emailprivacytester.com/badClients)

本文列出了因隐私漏洞而被认为是“不良”的电子邮件客户端，特别是 linkPreconnect 和 dnsLink，这些漏洞可能导致追踪。截至 2025 年 7 月 19 日，列出的客户端包括 Evolution Mail、Balsa 和 Geary。

Evolution Mail 因同时存在这两种漏洞而被标记。作者批评开发人员在已知问题一年多的情况下仍未采取行动，并且不愿警告用户使用“加载远程内容”功能的风险。即使漏洞得到修复，作者也表示对该团队及时进行隐私更新的承诺缺乏信心。

Balsa 和 Geary 都容易受到 linkPreconnect 攻击。作者批评了与 GNOME 相关的开发文化，声称他们否认对源自其所用库的安全漏洞负有责任。据报道，关于 Balsa 和 Geary 中问题的错误报告已被关闭，且未进行修复。

作者强调，在特定漏洞得到解决以及据称逃避安全问题责任的底层开发文化得到改革之前，不建议使用这些电子邮件客户端。作者鼓励联系以提交其他不良客户端，并为项目提供在被列出之前纠正问题的机会。

---

## 8. 我的自托管配置

**原文标题**: My Self-Hosting Setup

**原文链接**: [https://codecaptured.com/blog/my-ultimate-self-hosting-setup/](https://codecaptured.com/blog/my-ultimate-self-hosting-setup/)

本文详细介绍了作者的自托管设置，旨在掌控个人数据和服务。作者重点介绍了从尝试不同方法到实现一个稳定、“足够好”的解决方案的旅程，该解决方案平衡了安全性、可用性和复杂性。

该设置优先考虑将服务与公共互联网隔离，最大限度地减少因配置错误导致的基础设施停机时间，并通过开源选项拥有核心组件。面向家人和朋友的用户友好性也是一个关键考虑因素，目标是每个人只需一次登录即可实现 SSO。

核心技术包括：

*   **NixOS:** 一种用于声明式配置管理的 Linux 发行版。
*   **ZFS:** 一种具有数据保护功能和快照的文件系统。
*   **Tailscale:** 一种用于安全私有网络访问的网状 VPN（使用开源后端 headscale 进行自托管）。
*   **Authelia & LLDAP:** 具有 LDAP 用户管理功能的身份验证和授权服务。

该布局包含一个主要的公共服务器（“taris”），用于 Headscale 和 Authelia 等基本服务，以及博客和 Foundry VTT 代理等面向公众的服务。一个主要的私有服务器（“kuat”）运行带有 NixOS VM（“bespin”用于主要服务，“alderaan”用于测试）和 ZFS 数据集的 TrueNAS，用于存储文件和媒体。Home Assistant OS、Matrix、电子邮件和密码管理由单独的设备（“tython”和“coruscant”）处理，或者为了可靠性和避免依赖问题而外包。

本文还讨论了诸如创建起始页（使用 Flame）以便轻松访问服务，以及将 Tailscale 与另一个 VPN（使用 Gluetun）结合使用，以增强某些操作系统上的隐私等特定问题。还讨论了身份验证注意事项，突出了对 OpenID Connect 的偏好。

---

## 9. 凯悦酒店使用算法驱动的休息“吸烟探测器”

**原文标题**: Hyatt Hotels are using algorithmic Rest “smoking detectors”

**原文链接**: [https://twitter.com/_ZachGriff/status/1945959030851035223](https://twitter.com/_ZachGriff/status/1945959030851035223)

提供的文本并非关于凯悦酒店使用算法“烟雾探测器”的文章。它实际上是用户浏览器禁用JavaScript时，X（前身为Twitter）上显示的默认错误信息。其中包含：

* **JavaScript已禁用的通知：** 这是重点，解释了用户可能无法访问网站完整功能的原因。
* **启用JavaScript或更换浏览器的建议：** 这为用户提供了解决问题的故障排除建议。
* **链接到各种X法律和政策文件：** 这包括链接到帮助中心、服务条款、隐私政策、Cookie政策、版本说明和广告信息。
* **版权信息：** 这标识了X平台的拥有者（X Corp.）和版权年份。

因此，提供的文本中没有关于凯悦酒店或“烟雾探测器”的信息可以总结。标题与内容无关。

---

## 10. 使用三个人DNA制造的婴儿出生时没有线粒体疾病。

**原文标题**: Babies made using three people's DNA are born free of mitochondrial disease

**原文链接**: [https://www.bbc.com/news/articles/cn8179z199vo](https://www.bbc.com/news/articles/cn8179z199vo)

本文报道了英国成功利用三人 DNA 技术诞生的八名婴儿，该技术旨在预防遗传性线粒体疾病。这项创新方法在英国合法化已有十年，它将准父母的遗传物质与捐赠女性卵子的健康线粒体相结合。

线粒体疾病由母亲传给孩子，会导致细胞层面的能量匮乏，从而导致严重的残疾和死亡。三人 DNA 技术确保孩子从父母那里继承大部分 DNA，同时也从捐赠者那里继承一小部分（0.1%），捐赠者提供健康的线粒体。

接受手术的家庭表达了极大的感激之情，强调了这种治疗带来的解脱和希望。利用这种方法出生的婴儿没有表现出线粒体疾病的迹象，并且正在达到他们的发育里程碑。虽然观察到了一些轻微的健康问题（癫痫、心律失常），但这些与该手术无关。

研究人员正在继续监测这些儿童，并调查在过程中转移的任何剩余缺陷线粒体的存在和行为。该技术的成功为受线粒体疾病影响的家庭带来了希望，使后代有可能过上无疾病的生活。英国是世界上唯一允许这项手术的国家。

---

## 11. Fstrings.wtf
=>
Fstrings.wtf

**原文标题**: Fstrings.wtf

**原文链接**: [https://fstrings.wtf/](https://fstrings.wtf/)

Fstrings.wtf 是一个网站，旨在通过测验测试用户对 Python f-strings 的了解，特别是它们在 Python 3.13 中的行为。测验形式包含一个进度跟踪器，显示当前问题编号、总问题数和用户的当前分数。用户可以使用“下一题”按钮浏览问题，或随时结束测验。还提供一个重新开始选项。

完成测验后，会显示用户的最终分数，并允许他们将其分享到 X 和 Bluesky 等社交媒体平台。提供重新测验或访问帮助的选项。

该网站注明由 @mitsuhiko 与 Claude 共同创建，源代码可在 GitHub 上找到。可以使用数字键和方向键进行导航快捷方式来选择答案。

该网站还具有保存进行中测验的机制，允许用户继续或重新开始之前开始的测验。这使该网站更方便用户使用，并使用户在参加测验时具有灵活性。

---

## 12. YouTube 无需翻译

**原文标题**: YouTube No Translation

**原文链接**: [https://addons.mozilla.org/en-US/firefox/addon/youtube-no-translation/](https://addons.mozilla.org/en-US/firefox/addon/youtube-no-translation/)

"YouTube禁止翻译"是一款开源的Firefox插件，旨在阻止YouTube上的自动翻译，使平台保持原始语言。它拥有超过12000名用户并获得高评分。

主要功能包括保持原始语言的视频标题，优先使用原始音轨（包括在短视频上），阻止描述翻译，以及仅显示所选语言的真实字幕，忽略自动生成的字幕。

该插件免费使用，开发者请求通过KO-FI自愿捐款以支持进一步开发。它也可用于Chrome/Chromium浏览器。用户可以通过GitHub链接报告问题或请求功能。需要注意的是，该插件不适用于Android版Firefox或YouTube移动版。

该插件需要访问youtube.com和youtube-nocookie.com域名数据的权限（某些是可选的）。最新版本（2.10.0）最近已更新。它被归类为语言支持、社交与通讯以及游戏与娱乐，并采用GNU Affero通用公共许可证v3.0授权。

---

## 13. Valve证实信用卡公司曾施压，要求其下架某些成人游戏

**原文标题**: Valve confirms credit card companies pressured it to delist certain adult games

**原文链接**: [https://www.pcgamer.com/software/platforms/valve-confirms-credit-card-companies-pressured-it-to-delist-certain-adult-games-from-steam/](https://www.pcgamer.com/software/platforms/valve-confirms-credit-card-companies-pressured-it-to-delist-certain-adult-games-from-steam/)

由于万事达卡和维萨等支付处理商的压力，Valve已确认从Steam平台下架了几款成人游戏。这些处理商表示，这些游戏违反了他们的规则和标准，促使Valve将其下架，以避免整个Steam商店失去支付方式支持。

Valve正向受影响的开发者提供应用程序积分，用于符合支付处理商要求的其他游戏。虽然Valve没有具体说明哪些游戏被移除，但文章暗示它们涉及乱伦主题。文章强调，此次移除是对支付处理商担忧的直接回应，原因是与在线成人内容相关的诈骗和退款历史，尤其是在PornHub等网站涉及真人内容的丑闻之后。

作者对这种审查表示担忧，认为这开了一个坏的先例，允许支付处理商决定消费者可以在Steam上购买什么，即使Steam上的成人内容是动画。 另一款游戏《Trials of Innocence》的下架已被证实与此事无关，而是源于DMCA索赔。

---

## 14. 改装我的卡西欧：第二部

**原文标题**: Pimping My Casio: Part Deux

**原文链接**: [https://blog.jgc.org/2025/07/pimping-my-casio-part-deux.html](https://blog.jgc.org/2025/07/pimping-my-casio-part-deux.html)

作者在一篇后续文章中详细介绍了如何使用Oddly Specific Objects的新款“Sensor Watch Pro”套件升级卡西欧F-91W手表。与使用标准卡西欧显示屏的原始Sensor Watch不同，这款更新后的套件配备了加速度计和定制LCD屏幕。“Pro”版本的一个主要优势是无需焊接，从而简化了升级过程。

作者描述了拆卸卡西欧、安装新内部组件（包括用于电池连接的一小块金属）以及添加可选加速度计的过程，后者需要一块Kapton胶带。Micro USB接口用于刷写固件。

作者通过移除英制单位和12小时制，并选择要显示的特定屏幕（计数、加速度计和光传感器）来定制固件。这篇文章提供了构建和上传固件的确切命令，使用了诸如`gcc-arm-embedded`和`emscripten`等工具。

最后，作者重点介绍了基于浏览器的模拟器，它对于在刷写固件之前进行测试至关重要，可以使用`emmake`和一个简单的Python Web服务器构建和运行。这篇文章提供了一个全面的指南，介绍如何使用现代功能修改和升级经典的卡西欧F-91W。

---

## 15. 一个14kb的页面可能比一个15kb的页面加载更快 (2022)

**原文标题**: A 14kb page can load much faster than a 15kb page (2022)

**原文链接**: [https://endtimes.dev/why-your-website-should-be-under-14kb-in-size/](https://endtimes.dev/why-your-website-should-be-under-14kb-in-size/)

为什么14kB的网页比稍大的15kB网页加载更快：TCP慢启动原理

---

## 16. Linux 和安全启动证书过期

**原文标题**: Linux and Secure Boot certificate expiration

**原文链接**: [https://lwn.net/SubscriberLink/1029767/08f1d17c020e8292/](https://lwn.net/SubscriberLink/1029767/08f1d17c020e8292/)

2025年9月微软密钥过期对Linux安全启动的影响

---

## 17. Piramidal (YC W24) 招聘全栈工程师

**原文标题**: Piramidal (YC W24) Is Hiring a Full Stack Engineer

**原文链接**: [https://www.ycombinator.com/companies/piramidal/jobs/JfeI3uE-full-stack-engineer](https://www.ycombinator.com/companies/piramidal/jobs/JfeI3uE-full-stack-engineer)

Piramidal，一家Y Combinator W24孵化的初创公司，致力于构建电生理脑数据的底层模型，现于纽约市招聘全栈工程师。该职位涉及构建和维护其专注于神经数据的旗舰平台的基础设施和后端系统，与机器学习工程师协作，并与产品团队合作实施有效的解决方案。

理想的候选人将拥有在产品驱动型公司5年以上的工程经验，精通Python和其他后端语言，熟悉Kubernetes等容器化/编排技术、关系数据库（Postgres/MySQL）和Web技术（JavaScript、React）。快速且独立地工作能力至关重要。薪资范围为12万美元至27万美元。不提供签证担保。

Piramidal旨在创建可扩展的神经解码器，以理解和控制神经语法，并致力于重定向技术以最大限度地发挥人类潜力，重点关注认知自由。

面试流程包括初步筛选、技术筛选（居家或现场）以及包括架构可扩展系统和问答环节的最后一轮面试。创始人为Dimitris Fotis Sakellariou和Kris Pahuja。

---

## 18. 我避免作为出版者和作家使用大型语言模型。

**原文标题**: I avoid using LLMs as a publisher and writer

**原文链接**: [https://lifehacky.net/prompt-0b953c089b44](https://lifehacky.net/prompt-0b953c089b44)

图书出版商兼技术爱好者托马斯·巴拉内克阐述了为什么他避免使用大型语言模型（LLM）来完成大多数写作和出版任务，尽管他承认它们在编码和某些技术问题解决方面很有用。

他认为，虽然LLM在某些领域有帮助，但会导致认知上的懒惰，降低原创性和大脑连通性，正如研究表明的那样。他担心当依赖人工智能生成的摘要或内容时，独立思考能力的下降和个人见解的丧失。他觉得LLM生成的文本不带感情、 "人工化"，缺乏真实性，并且担心人们将其视为真理的来源。

巴拉内克强调了LLM不准确性日益常态化以及错误信息被永久传播的风险。他认为，核实LLM的输出结果至关重要，但许多用户，尤其是那些不太懂技术的用户，可能不会这样做。他强调了人类智慧、批判性思维和咨询专家的重要性，尤其是在写作、创造力和健康咨询等领域。虽然他承认LLM在某些情况下很有用，比如润色电子邮件交流，但他最终珍视来自创作自己思想和文字的独特个性和更深层次的学习。他担心由于依赖人工智能生成的信息，各种社区内对来源验证和批判性思维的重视程度可能会降低。

---

## 19. 北美已知最古老的翼龙

**原文标题**: North America's Oldest Known Pterosaur

**原文链接**: [https://www.si.edu/newsdesk/releases/smithsonian-led-team-discovers-north-americas-oldest-known-pterosaur](https://www.si.edu/newsdesk/releases/smithsonian-led-team-discovers-north-americas-oldest-known-pterosaur)

由史密森尼学会领导的团队在亚利桑那州石化林国家公园发现了北美已知最古老的翼龙，一种海鸥大小的带翼爬行动物。 这块化石可追溯到2.09亿年前，与数百块其他化石一起出土于一个偏远的化石层中，其中包括世界上最古老的龟类化石之一。 这一发现填补了三叠纪末灭绝 (ETE) 之前的化石记录空白，为了解一个充满活力的生态系统提供了一个缩影，在这个生态系统中，较老的动物群体与青蛙、乌龟和翼龙等进化新手共存。

该化石层于 2011 年被发现，揭示了一个多样化的生态系统，其中有淡水鲨鱼、古代两栖动物、带甲食草动物和早期青蛙，它们都生活在一个容易发生季节性洪水的半干旱环境中。 新翼龙物种被命名为 *Eotephradactylus mcintireae*，是通过一块保存完好的带牙齿的颌骨鉴定的，这表明它以该地点的鱼类为食。 这一发现突显了乌龟在泛大陆的快速传播以及欧洲以外地区早期翼龙的存在。 这项研究涉及对化石的细致挖掘和准备，博物馆志愿者做出了重大贡献。 国家自然历史博物馆与石化林国家公园之间正在进行的合作，为了解三叠纪以及各种动物群体的进化提供了宝贵的见解。

---

## 20. 没有信号的广告：骗子均衡的崛起

**原文标题**: Advertising without signal: The rise of the grifter equilibrium

**原文链接**: [https://www.gojiberries.io/advertising-without-signal-whe-amazon-ads-confuse-more-than-they-clarify/](https://www.gojiberries.io/advertising-without-signal-whe-amazon-ads-confuse-more-than-they-clarify/)

本文认为，在线广告已进入“骗子均衡”状态，品牌声誉和广告支出等传统产品质量信号不再是可靠的指标。互联网降低了搜索成本，但也削弱了质量信号，原因包括可抛弃的品牌身份、按每次转化费用 (CPA) 定价（消除了低质量产品广告投资的风险）、宽松的退货政策、压缩的星级评定以及依赖价格作为质量指标的启发式驱动购物者。

作者提出了一个模型，证明了CPA竞价如何破坏广告信号。高质量和低质量的卖家都能负担得起广告费用，因为他们只在发生销售时才付费。这消除了低质量卖家在传统模式下所面临的劣势，在传统模式下，由于客户留存率较低，他们无法收回高昂的广告成本。在收到负面反馈后能够快速重新启动店面的能力进一步加剧了这个问题。

作者提出了解决此问题的补救措施，包括持久的制造商 ID、退货调整后的 CPA 附加费、托管广告保证金和重新启动检测，以增加销售低质量商品的成本并降低其净现值。虽然这些解决方案无法完全恢复传统信号，但它们可以阻止最严重的违规者。市场没有崩溃，原因是退货政策、低单位成本（即使有退货也能让劣质产品保持盈利能力）以及异质性需求（买家愿意为了便利和价格而接受不确定性）。平台也受益于市场的拥堵以及由此产生的广告收入，因此它们在打击该问题方面的动力有限。

---

## 21. Zig 接口再探

**原文标题**: Zig Interface Revisited

**原文链接**: [https://williamw520.github.io/2025/07/13/zig-interface-revisited.html](https://williamw520.github.io/2025/07/13/zig-interface-revisited.html)

本文探讨了如何在 Zig 中使用 VTable 接口实现多态，这种模式允许动态分发，即使 Zig 缺乏内置的接口结构。文章将此方法与 Zig 中其他形式的多态（如泛型和标记联合）进行对比，强调了统一类型的使用场景，特别是将多个实现存储在单个集合中。

文章的核心部分提供了一个逐步指南，通过一个日志系统示例来创建 VTable 接口，说明了如何实现一个带有 `DbgLogger` 和 `FileLogger` 实现的 `Logger` 接口。关键组件包括：

1.  用于存储实现的不透明指针 (`*anyopaque`)。
2.  作为动态分发表的 VTable 的函数指针。
3.  用于将实现对象连接到接口的 `implBy()` 函数。
4.  通过不透明指针调用 VTable 的接口方法。
5.  用于重建原始类型并调用其方法的委托结构体 (`LoggerDelegate`)，以确保类型安全。

这种方法的优点是接口和实现的清晰分离、可扩展性以及所有接口实例的统一类型。缺点包括定义 VTable 方法和委托结构体的样板代码，以及由于函数指针间接调用而导致的轻微性能开销。尽管存在样板代码，但文章总结认为，这种模式提供了对 Zig 中抽象的灵活性和控制，从而允许解耦和富有表现力的 API。

---

## 22. 如何在 Linux 内核中编写 Rust：第三部分

**原文标题**: How to write Rust in the Linux kernel: part 3

**原文链接**: [https://lwn.net/SubscriberLink/1026694/3413f4b43c862629/](https://lwn.net/SubscriberLink/1026694/3413f4b43c862629/)

这篇 LWN.net 文章“如何在内核中编写 Rust：第三部分”重点介绍了内核 Rust 代码常用的关键 Rust 绑定，用于诸如内存分配、处理不可移动结构以及使用锁等任务。它解释说，虽然可以直接进行 C 的 FFI 调用，但每个子系统最好使用一组集中化的 Rust 绑定，以便实现标准化、文档化、安全性和更易于审查。

文章详细介绍了 `kernel::alloc` 模块，提供了三种内存分配方法：Kmalloc、Vmalloc 和 KVmalloc。 这些映射到熟悉的 C 内存管理范例。 像 KBox、VVec 和 Arc 这样的简短别名提供了使用 boxes、vectors 和引用计数来分配和管理内存的符合人体工程学的方式。 文章还涵盖了通过 `kernel::alloc::flags` 的分配标志和用于处理分配失败的 `Result` 类型。

然后，这篇文章讨论了处理自引用结构，例如内核中常见的双向链表。 引入了 Rust 的“pinning”概念，以防止这些结构的不安全重定位。 `Pin` 类型和相关宏（`pin_init!` 和 `try_pin_init!`）用于安全地管理此类结构。

最后，文章涵盖了 Rust 内核代码中的锁定机制。 包含受保护数据的传统 Rust 互斥锁可用，以及用于处理与数据分离的锁的 `LockedBy` 和 `GlobalLockedBy` 类型。 支持自旋锁、互斥锁和 RCU 锁。

作者撰写该系列文章（特别是本文）的目标是帮助 C 内核开发人员过渡到 Rust，重点关注他们在常用内核绑定时会遇到的实际差异。

---

## 23. 异步非并发

**原文标题**: Asynchrony is not concurrency

**原文链接**: [https://kristoff.it/blog/asynchrony-is-not-concurrency/](https://kristoff.it/blog/asynchrony-is-not-concurrency/)

Loris Cro认为，并发编程讨论中缺失的一个关键区别是“异步性”，而将其与并发性混淆导致了软件生态系统中的问题。他定义如下：

*   **异步性:** 任务可以乱序运行但仍然保持正确的可能性。
*   **并发性:** 系统能够同时处理多个任务的能力，通过并行或任务切换实现。
*   **并行性:** 在物理层面上同时执行多个任务的能力。

Cro认为，当前的语言生态系统经常迫使库作者重复工作（同步与异步版本），并创建病毒式“异步”代码，要求用户放弃同步编程。为了缓解这些问题而创建的逃生舱会导致次优行为和死锁。

Zig通过将异步性与并发性解耦来解决这个问题。使用`io.async`并不自动意味着并发性；使用它的代码可以在单线程阻塞模式下运行。反之，同步代码仍然可以利用并发性。这是通过事件驱动的 I/O 系统调用和任务切换原语实现的。

关键的见解是，“异步”应该只关注乱序执行的*可能性*，而不是并发执行的*要求*。他在Zig中引入了`io.asyncConcurrent`来明确表示正确性需要并发性的情况，从而允许在非并发的`Io`实现上运行时进行错误检测。这允许库提供异步功能，而无需强迫用户进入异步环境。

---

## 24. Meta表示不会签署欧洲人工智能协议，称其为过度干预。

**原文标题**: Meta says it won’t sign Europe AI agreement, calling it an overreach

**原文链接**: [https://www.cnbc.com/2025/07/18/meta-europe-ai-code.html](https://www.cnbc.com/2025/07/18/meta-europe-ai-code.html)

Meta宣布将不签署欧盟人工智能行为准则，全球事务主管乔尔·卡普兰称其为过度干预，将扼杀增长并制造法律不确定性。该行为准则旨在帮助企业遵守人工智能法案，该法案旨在提高人工智能技术的透明度和安全性。

卡普兰认为，该准则的措施超出了人工智能法案的范围，并将阻碍欧洲先进人工智能模型的开发和部署，从而损害欧洲企业。Meta并非唯一反对者；ASML控股和空中客车此前曾呼吁将该准则推迟两年实施。

欧盟委员会发布了通用人工智能模型的最终版行为准则，允许企业自行决定是否签署。这些规则将于下个月生效。尽管OpenAI承诺签署该准则，但Meta与其他企业一样，担心欧盟的做法会扼杀欧洲人工智能的创新和部署。

---

## 25. 2025年最富有的国家是哪个？

**原文标题**: What is the richest country in 2025?

**原文链接**: [https://www.economist.com/graphic-detail/2025/07/18/what-is-the-richest-country-in-the-world-in-2025](https://www.economist.com/graphic-detail/2025/07/18/what-is-the-richest-country-in-the-world-in-2025)

该文章发表于2025年7月，探讨了超越简单收入的国家财富概念，考虑了购买力平价（薪水在一个国家的购买力）和工作与生活平衡（每小时工作产生的收入）等因素。文章认为，仅仅赚更多钱并不一定等同于真正的富有。文章宣布将每年基于这些更广泛的经济考量对各国进行排名。

该文章还链接到其他文章，涵盖了诸如美国饮酒指南的潜在变化、特朗普的对外援助削减、俄罗斯在乌克兰的攻势、德克萨斯州的洪水、特朗普的税收法案以及伊朗的互联网访问等主题。这些相关文章可能涉及影响全球经济和社会格局的因素。

---

## 26. N78频段5G NR记录

**原文标题**: N78 band 5G NR recordings

**原文链接**: [https://destevez.net/2025/07/n78-band-5g-nr-recordings/](https://destevez.net/2025/07/n78-band-5g-nr-recordings/)

本文详细介绍了作者记录和分析n78频段（3.3-3.8 GHz）5G新空口（NR）信号的努力，该频段因其大带宽和在欧洲的普遍使用而备受关注。作者概述了记录该频段所面临的挑战，包括低端SDR的带宽限制以及需要多个天线来演示MIMO技术。

作者与穆尔西亚大学的研究人员合作，使用他们的高端USRP进行记录。他们在使用USRP X410时遇到了问题，原因是B3频段的杂散信号干扰了n78的接收，最终选择了USRP N310。他们还面临着数据记录速度的挑战，最终因GNU Radio和直接写入磁盘的限制而选择记录到tmpfs。

作者成功记录了西班牙Movistar、Orange和Vodafone基站的数据，频率分别为3.55 GHz、3.65 GHz和3.75 GHz。文中介绍了对小区利用率、TDD模式、SSB重复和波束成形效果的观察结果，突出了不同运营商之间信号强度和行为的差异。作者还讨论了每个运营商的频谱分配情况，其中Vodafone运行90MHz小区，而Movistar和Orange运行100MHz小区。最后，记录的数据集已发布在Zenodo上供公众访问。

---

## 27. 天文学家利用海王星外天体的颜色追踪古老的恒星飞越事件

**原文标题**: Astronomers use colors of trans-Neptunian objects to track ancient stellar flyby

**原文链接**: [https://phys.org/news/2025-07-astronomers-trans-neptunian-track-ancient.html](https://phys.org/news/2025-07-astronomers-trans-neptunian-track-ancient.html)

天文学家利用海王星外天体(TNO)的颜色来研究可能影响早期太阳系的远古恒星飞越事件。海王星外天体，即在海王星之外轨道上运行的矮行星，表现出从灰色到红色的复杂颜色分布，这与表面类托林等不同化学物质有关，并表明它们的形成位置和轨道动力学。

即将发表在《天体物理学杂志快报》上的新研究表明，太阳系早期历史中的一次恒星飞越事件是造成海王星外天体异常轨道和颜色分布的原因。研究人员使用超级计算机模拟，模拟了一颗恒星飞越早期太阳系的过程，观察了它对包含颜色梯度粒子的原行星盘的影响。

模拟表明，这次飞越改变了粒子的轨道，将它们引导到螺旋臂中，并成功地再现了在海王星外天体中观察到的动态分组。重要的是，模拟将颜色与轨道倾角相关联，红色粒子出现在较低的倾角处，这与观察到的海王星外天体颜色分布相呼应。

即将到来的薇拉·鲁宾天文台的遗产巡天空间和时间调查 (LSST) 预计将使已知海王星外天体的数量增加十倍，从而可以进一步验证这些发现。该研究预测，LSST将发现遥远的海王星外天体主要为淡红色到灰色，缺乏鲜红色的天体。这项研究进一步加强了恒星飞越显著塑造了外太阳系结构的观点。

---

## 28. Ramsey下界的指数级改进

**原文标题**: An exponential improvement for Ramsey lower bounds

**原文链接**: [https://arxiv.org/abs/2507.12926](https://arxiv.org/abs/2507.12926)

这篇 arXiv 文章 (arXiv:2507.12926) 于 2025 年 7 月 17 日提交，属于组合数学领域，在 Ramsey 理论方面提出了重大进展。该论文题为《Ramsey 下界的指数改进》，作者 Jie Ma、Wujie Shen 和 Shengjie Xie 建立了一个 Ramsey 数 $r(\ell, C\ell)$ 的新下界，其中 $C > 1$ 是一个常数，$\ell$ 足够大。

关键结果是存在一个正值 $\varepsilon$（取决于 $C$），使得 $r(\ell, C\ell) \geq \left(p_C^{-1/2} + \varepsilon\right)^\ell$，其中 $p_C$ 是方程 $C = \frac{\log p_C}{\log(1 - p_C)}$ 在区间 $(0, 1/2)$ 中的唯一解。这一发现标志着对 Erdős 于 1947 年建立的 Ramsey 数经典下界的首次指数改进。

该论文共 41 页，包含 3 个图，深入探讨了支持这个新下界的数学细节。作者提供了论文的 PDF 版本和一个用于查看的实验性 HTML 版本。该论文在 arXiv 上被归类于组合数学 (math.CO) 主题领域。

---

## 29. 二手电脑的CarFax：惠普希望让旧笔记本电脑焕发新生

**原文标题**: A CarFax for Used PCs: Hewlett Packard wants to give old laptops new life

**原文链接**: [https://spectrum.ieee.org/carfax-used-pcs](https://spectrum.ieee.org/carfax-used-pcs)

惠普(HP)计划为二手笔记本电脑赋予新生，打造一套类似于汽车CarFax的系统，为二手PC市场提供透明度和可信度。这项由惠普的Abu Baker、Sal Vasi、Barbara Spitzer和John Hong领导的计划，旨在为二手惠普笔记本电脑建立可验证的历史记录，详细说明其规格、维修历史、先前所有权和整体状况。

这种“二手PC的CarFax”将为潜在买家提供有价值的信息，使他们在购买二手笔记本电脑时能够做出更明智的决定。通过提供关于笔记本电脑过去的详细报告，惠普希望提高消费者对二级市场的信心，并鼓励现有设备的再利用。

该计划旨在标准化二手笔记本电脑的评估，降低购买有缺陷或被虚报产品的风险。这项举措符合惠普对可持续发展的承诺，通过促进其产品的寿命和通过增加再利用来减少电子垃圾。

---

## 30. Bun 添加了 pnpm 风格的隔离安装模式

**原文标题**: Bun adds pnpm-style isolated installation mode

**原文链接**: [https://github.com/oven-sh/bun/pull/20440](https://github.com/oven-sh/bun/pull/20440)

本文探讨了Bun（一种JavaScript运行时）的隔离安装模式的实现，类似于pnpm的做法。通过将`nodeLinker`设置为"isolated"来启用此新功能，旨在防止幽灵依赖并实现并行包安装。

该实现的关键方面包括：

*   **隔离结构:** 包被安装在`node_modules/.bun/`下的隔离结构中。
*   **符号链接:** 创建从`node_modules/<package>`到`.bun`目录中实际包位置的符号链接 (`.bun/<package>@<version>/node_modules/<package>`)。
*   **工作区支持:** 该实现支持工作区，允许它管理单个存储库中多个项目之间的依赖关系。
*   **配置:** `linker = "isolated"`设置最初在`bunfig.toml`中配置，但将来也会识别`.npmrc`中的配置。

该拉取请求包含针对各种场景的测试，例如：单个依赖、作用域包、传递依赖、循环依赖、文件夹依赖和工作区。

讨论强调了传递依赖项在`.bun`目录中被符号链接。用户还询问了类似于`nohoist`的行为，即将传递依赖项直接放置在项目的`node_modules`目录中。这种新模式旨在提供更好的依赖管理，尤其是在monorepo环境中。

---

## 31. Browser先生 - 直接在68k Mac上运行的Macintosh Repository文件下载器

**原文标题**: Mr Browser – Macintosh Repository file downloader that runs directly on 68k Macs

**原文链接**: [https://www.macintoshrepository.org/44146-mr-browser](https://www.macintoshrepository.org/44146-mr-browser)

MR浏览器是一款实用程序应用，专为90年代较老的68k Macintosh电脑设计，使其无需现代电脑作为中介，即可直接访问和下载Macintosh Repository上的文件。该软件专为System 7环境量身定制，且文件大小限制为小于1GB。

本文重点介绍了故障排除技巧，包括确保足够的硬盘空间以防止崩溃、解决与Basilisk II模拟器相关的问题、通过分配更多RAM来解决Mac OS 9.1至9.2.2中的锁定问题，以及确保存在“MacTCP DNR”文件以实现System 6兼容性。

详细的更新日志列出了MR浏览器中实现的众多更新和错误修复，从0.04版（2025-06-08）到0.36版（2025-06-18），包括在“浏览”中添加一个“页面信息”按钮，该按钮会弹出一个窗口显示给定的软件页面描述，防止用户在没有足够可用空间的情况下开始下载，修复了一个导致下载文件在重启前无法释放以进行删除的错误等等。 它还描述了新增功能、生活质量改进以及为增强性能和用户体验而进行的优化。 欢迎用户提出建议，并且这些建议已融入到开发过程中。

---

## 32. Debcraft - 修改和构建Debian软件包的最简方式

**原文标题**: Debcraft – Easiest way to modify and build Debian packages

**原文链接**: [https://optimizedbyotto.com/post/debcraft-easy-debian-packaging/](https://optimizedbyotto.com/post/debcraft-easy-debian-packaging/)

Debcraft 旨在简化 Debian 软件包的创建和维护，这个过程通常被认为复杂而令人生畏。它解决了常见的抱怨，例如工具过多、文档过时以及不清楚修改如何影响最终软件包。

Debcraft 利用 Git、git-buildpackage 和 Linux 容器 (Docker/Podman) 来创建更易于访问和更简化的工作流程。它消除了在 Debian 系统上开发的必要性，允许使用其他操作系统的开发人员参与。该工具提供简单的命令，如 `debcraft build`、`debcraft test` 和 `debcraft release`，以自动构建、测试和发布软件包。输出采用颜色编码，并包含有用的解释和相关文档的链接。

一个关键特性是清晰地分离构建工件和日志，从而方便比较更改。`debcraft shell` 命令有助于调试失败的构建。`debcraft improve` 自动修复问题并将软件包更新为遵循最新的 Debian 策略，而 `debcraft update` 帮助将软件包更新到最新的上游版本。

Debcraft 可通过 `apt install debcraft` 在 Debian/Ubuntu 上使用。对于其他发行版或最新功能，用户可以从 Git 存储库安装。该项目欢迎贡献，代码有意用 shell 脚本编写，以降低入门门槛。作者 Otto Kekalainen 是一位有远见的领导者，为有抱负的 Debian 开发人员提供指导。

---

## 33. 吾死之愿

**原文标题**: Wishes Upon My Demise

**原文链接**: [https://vale.rocks/posts/regarding-my-death](https://vale.rocks/posts/regarding-my-death)

Declan Chidlow的《我死后的愿望》概述了他死后的愿望，强调接受死亡的必然性并据此进行规划的重要性。他优先考虑自主权和精神清晰，声明如果这些能力不可挽回地丧失，特别是由于脑死亡，他希望被实施安乐死。他特别害怕像运动神经元疾病、阿尔茨海默病和痴呆症这样的退行性疾病，并打算在这种情况下寻求自愿辅助死亡。

他已登记为器官捐献者，希望他的器官被采集，无需考虑外貌。他明确拒绝土葬，倾向于捐献给科学研究、火葬或其他替代方法。葬礼安排应简单且非宗教，可以包含飞面神教的元素。

Chidlow要求在他去世后，他的社交媒体渠道上分享特定信息，包括死因，以便了结。他认为他的网站 Vale.Rocks 是他的遗产，详细说明了如何维护和将其保存在互联网档案馆中。在他去世后，网站上的所有内容将致力于公共领域，并指示保持网站可访问性，但避免进行超出必要维护的重大修改。他强调维护他在其他地方发布的内容的现有许可。该文件以反映他渴望充实而真实地生活，尽管他害怕浪费生命的引言结尾。

---

## 34. 博通将停止免费提供Bitnami Helm charts

**原文标题**: Broadcom to discontinue free Bitnami Helm charts

**原文链接**: [https://github.com/bitnami/charts/issues/35164](https://github.com/bitnami/charts/issues/35164)

博通将于2025年8月28日起停止提供免费的Bitnami Helm charts和容器镜像。公共目录将过渡到一套有限的、强化的、安全的镜像，这些镜像将在`https://hub.docker.com/u/bitnamisecure`上以“latest”标签提供，用于开发目的。

所有现有容器镜像，包括旧版本，将被移至Bitnami Legacy仓库（`docker.io/bitnamilegacy`），该仓库将不再接收更新或支持。 这仅作为临时迁移方案。

对于生产环境使用，建议用户订阅Bitnami Secure Images，它提供强化镜像、持续安全更新（SLSA Level 3）、CVE透明度、SBOM、企业支持、LTS分支以及对完整应用目录的访问权限。

用户应更新其CI/CD管道和Helm仓库以反映这些更改。作为临时解决方案，用户可以将Helm charts指向Bitnami Legacy仓库，但由于缺乏更新和支持，不建议长期使用。免费镜像仍将可用，但仅限于一小部分应用程序的最新版本。 底层开源代码仍可在GitHub上以Apache 2许可获得。

---

## 35. 伊万·伊里奇：《沉默是公共资源》(1983)

**原文标题**: Silence Is a Commons by Ivan Illich (1983)

**原文链接**: [http://www.davidtinapple.com/illich/1983_silence_commons.html](http://www.davidtinapple.com/illich/1983_silence_commons.html)

在《沉默即公共地》一书中，伊万·伊利奇认为现代技术，尤其是电子通信，正在侵蚀重要的“公共地”——对人类福祉至关重要的共享环境要素——将其转变为由机构管理和控制的资源。他将像牧场和道路等有形公共地的圈占，与像沉默和言语等更微妙的公共地的圈占进行类比。

伊利奇认为，扬声器和其他通信技术的兴起降低了个人声音的价值，将权力集中在那些控制这些技术的人手中，实际上使其他人噤声。这种转变反映了历史上公共地的圈占，土地从维持生计的共享资源转变为用于商业利益的私有财产，导致普遍贫困和对商品的依赖。

他强调，政治生态学必须认识到这种将公共地转变为资源的行为是一种环境退化。传统的反资本主义政治，侧重于资源的私人利用，无意中助长了这种转变。伊利奇呼吁出现一种新型的“大众知识分子”，来认识到这种将人重新定义为消费者的环境转变，从而引发捍卫剩余公共地的运动。

他强调，捍卫这些公共地，特别是沉默，对于人的出现和自治至关重要。依赖机器进行交流和思考，威胁到人类的尊严和福祉，导致一个要求被管理而不是自我管理的社会。

---

## 36. C++：零成本静态初始化

**原文标题**: C++: Zero-cost static initialization

**原文链接**: [https://cofault.com/zero-cost-static.html](https://cofault.com/zero-cost-static.html)

本文探讨了一种消除C++中块级静态变量运行时初始化开销的技术。 传统上，这些变量使用内部标志和同步机制（例如`__cxa_guard_acquire`）来确保初始化仅发生一次，即使在多线程环境中也是如此。 这会在每次访问时增加性能成本，即使在初始化之后也是如此。

作者提出了一种零成本静态初始化方法，该方法利用了UNIX链接器的一个鲜为人知的特性：创建标记section起始和结束的符号的能力（例如，`__start_SECNAME`和`__stop_SECNAME`）。 该方法包括：

1. 使用`__attribute__((section))`在自定义section（例如，`STATIC_Bar`）中定义占位符对象。 这些占位符足够大，可以容纳预期的静态对象。
2. 在全局静态初始化期间，使用链接器提供的start/stop符号扫描占位符范围，并使用placement new在占位符的内存中就地构造实际的静态对象。

最初的尝试在使用内联函数时遇到了section属性冲突的挑战。 作者通过使用嵌入式汇编（`__asm__`）与`.pushsection`和`.popsection`手动将指向占位符的指针放置在专用section中来克服了这个问题，从而规避了编译器管理的section属性。 为了避免符号名称冲突，使用`__COUNTER__`宏为每个占位符生成唯一的符号名称。 这确保了在调用包含静态变量的函数时，静态对象已经初始化，从而消除了运行时检查和同步开销。 本文最后提供了一个可行的实现，演示了在汇编中直接访问静态变量，证实了该优化的零成本性质。

---

## 37. Zig 的新作者

**原文标题**: Zig's New Writer

**原文链接**: [https://www.openmymind.net/Zigs-New-Writer/](https://www.openmymind.net/Zigs-New-Writer/)

本文讨论了Zig的`std.Io.Writer`接口的重大重构，这是处理输入/输出操作的关键组件。新的设计用围绕`drain`函数的统一接口取代了之前令人困惑且性能不足的系统。现在，自定义writer实现`drain`函数，该函数处理字符串切片数组 (`[]const []const u8`)，因为Writer接口包含内置缓冲。

`drain`函数负责将数据写入底层资源（例如，文件），而`std.Io.Writer`处理缓冲和部分写入。文章展示了一个简化的`drain`实现，通常在过渡期间使用，该实现忽略`splat`参数并仅写入数据数组中的第一个切片。

文章强调，`file.writer(&buffer)`返回一个`File.Writer`结构体，其中包含一个`interface: std.Io.Writer`字段，必须显式访问。预计这种约定将在Zig生态系统中普遍存在。迁移到新系统涉及用`Writer.printInt`替换诸如`std.fmt.formatIntBuf`之类的方法，并对先前直接在缓冲区上工作的函数使用`Writer.fixed([]u8)`。

文章通过解释说较旧的writer必须实现`adaptToNewApi`以公开一个`new_interface: std.Io.Writer`字段来解决常见的迁移错误`no field or member function named 'adaptToNewApi'`，从而实现与更新后的`std.fmt.format`的兼容性。

作者对直接将缓冲嵌入到`Writer`接口中表示保留意见，并建议组合（例如，使用单独的`BufferedWriter`）可能是一种更灵活和易于理解的方法，这与其它语言中的常见做法相符。

---

## 38. Claude代码如何生成状态消息

**原文标题**: How Claude Code Generates Status Messages

**原文链接**: [https://twitter.com/dmartincy/status/1941833382649864246](https://twitter.com/dmartincy/status/1941833382649864246)

这并非一篇关于Claude Code如何生成状态信息的文章。相反，这是一条当用户浏览器禁用JavaScript时在x.com（原Twitter）上显示的出错信息。

该信息告知用户**使用本网站需要JavaScript，且JavaScript当前已被禁用**。它指示用户**启用JavaScript或切换到受支持的浏览器**。

此外，该信息还提供了以下链接：

*   **帮助中心：** 推测是关于如何启用JavaScript或查找受支持浏览器的说明。
*   **服务条款、隐私政策、Cookie政策、版本说明、广告信息：** 在许多网站上都能找到的标准法律和信息链接。
*   **版权信息：** 表明网站内容受X Corp.在2025年拥有的版权保护。

总而言之，所提供的文本是来自x.com的JavaScript出错信息，提醒用户一项必要功能已被禁用，并提供关于如何解决该问题的指导，以及相关网站政策和信息的链接。它与Claude的代码生成无关。

---

## 39. Wii U SDBoot1 漏洞“一命呜呼”

**原文标题**: Wii U SDBoot1 Exploit “paid the beak”

**原文链接**: [https://consolebytes.com/wii-u-sdboot1-exploit-paid-the-beak/](https://consolebytes.com/wii-u-sdboot1-exploit-paid-the-beak/)

本文详细介绍了Wii U中名为“paid the beak”的boot1漏洞的发现与利用，以及复制触发该漏洞所需的工厂测试夹具的努力。作者回顾了其参与从损坏的任天堂工厂SD卡中恢复数据的过程，这导致了SDBoot1函数的发现。开发者Rairii在SDBoot1中发现了一个漏洞，该漏洞允许在启动时运行自定义代码，从而有可能从大多数软件砖块中恢复。

触发SDBoot1需要一个特殊的测试夹具来激活UNSTBL_PWR标志。本文详细介绍了Jan和Deadly使用Raspberry Pi Pico复制此夹具的努力，并提供了代码和说明。此外，作者还开发了一种使用PICAXE 08M2微控制器的解决方案，提供了一种更便宜、更小的替代方案。

该漏洞可与SD卡镜像SDBoot1-Minute.bin一起使用。刷入SD卡并使用测试夹具或克隆夹具即可在Wii U启动时运行自定义代码。作者强调了“paid the beak”的优势，强调了其与Defuse等其他方法相比，在可访问性和易用性方面的潜力，因为它最大限度地减少了焊接或打开主机的需要。本文感谢WiiCurious对该项目的资助和支持。

---

## 40. 菲利克斯·鲍姆加特纳，曾从平流层跳伞，在意大利去世

**原文标题**: Felix Baumgartner, who jumped from stratosphere, dies in Italy

**原文链接**: [https://www.theinternational.at/felix-baumgartner-who-jumped-from-stratosphere-dies-in-italy/](https://www.theinternational.at/felix-baumgartner-who-jumped-from-stratosphere-dies-in-italy/)

本文将两个不相关的议题混淆并列：菲利克斯·鲍姆加特纳（平流层跳伞者）的虚假死亡报道和2023年奥地利学生会（ÖH）选举信息。

**关于鲍姆加特纳的不实标题：** 这表明文章*最初*以捏造的菲利克斯·鲍姆加特纳死亡新闻故事开头。这种说法是不真实的；截至2023年10月26日，菲利克斯·鲍姆加特纳仍然健在。该标题很可能是一种耸人听闻的点击诱饵或错误。

**关于2023年ÖH选举：** 提供的内容表明，文章的核心实际上是关于2023年举行的奥地利学生会（ÖH）选举。“你需要知道的一切”这句话意味着这篇文章提供了关于这些选举的全面信息。可能涵盖的关键细节包括：

*   **什么是ÖH：** 解释奥地利学生会的功能和作用。
*   **为什么选举很重要：** 概述ÖH对学生生活和大学政策的影响。
*   **谁可以投票：** 详细说明选举投票的资格标准。
*   **涉及的主要政治团体/党派：** 描述争夺ÖH席位的不同派别。
*   **正在辩论的重要议题：** 突出竞选期间涉及的关键政策领域和关切。

“office 07/05/2023”可能指的是发布日期或与选举相关的相关日期。

**总之：** 这篇文章是将错误信息（鲍姆加特纳的虚假标题）和关于奥地利学生会（ÖH）2023年选举的真实信息奇怪地混合在一起。

---

## 41. 首个空间引力波探测器开始建造

**原文标题**: First Space-Based Gravitational Wave Detector Begins Construction

**原文链接**: [https://spectrum.ieee.org/laser-interferometer-space-antenna](https://spectrum.ieee.org/laser-interferometer-space-antenna)

首个空间引力波探测器开始建造

---

## 42. Ccusage: 一个从本地 JSONL 文件分析 Claude 代码用量的 CLI 工具

**原文标题**: Ccusage: A CLI tool for analyzing Claude Code usage from local JSONL files

**原文链接**: [https://github.com/ryoppippi/ccusage](https://github.com/ryoppippi/ccusage)

`ccusage` 是一款命令行工具，旨在直接从本地 JSONL 文件分析 Claude 代码令牌使用情况和相关成本。 它提供了一种快速且信息丰富的方式来跟踪您的 Claude 费用，而无需大型安装。 您可以使用 `bunx`、`npx` 或 `deno` 直接运行它。

该工具提供多种报告类型：每日、每月、会话（基于对话）和 5 小时计费块报告。 它还支持实时监控，并提供实时仪表板。 `ccusage` 提供过滤选项，例如日期范围（`--since`、`--until`）和特定项目（`--project`）。 您还可以以 JSON 格式输出数据（`--json`）。

主要功能包括模型跟踪、按模型划分的成本细分、自定义数据目录支持、色彩丰富且响应迅速的输出以及使用预缓存定价数据的离线模式。 它还具有模型上下文协议 (MCP) 集成，并支持按项目/实例对使用情况进行分组。一个值得注意的方面是，与其他类似工具相比，它的捆绑包体积非常小。

---

## 43. 何时制作LOD (2021)

**原文标题**: When to make LODs (2021)

**原文链接**: [https://medium.com/@jasonbooth_86226/when-to-make-lods-c3109c35b802](https://medium.com/@jasonbooth_86226/when-to-make-lods-c3109c35b802)

本文挑战了优化3D模型时传统上对多边形数量的关注，认为这是一个过时的指标。作者强调了最小化“微小三角形”的重要性——即屏幕上覆盖面积小于10x10像素的三角形。这些三角形的代价很高，因为GPU以2x2的像素块处理像素，即使只有一个像素被一个小三角形覆盖，也必须计算所有四个像素。这导致单像素几何体的渲染成本呈指数级增长。

文章批评了出于过时多边形数量考虑而过度使用LOD（细节层次），认为这可能导致跳变、破坏批处理、消耗内存并降低视觉质量。作者建议专注于微小三角形密度，并在线框视图看起来几乎完全实心时切换到较低的LOD。文章提到Unity的HDRP“顶点密度”热图是对此有用的工具。在许多情况下，使用单个LOD和一个用于远距离的imposter比多个LOD更好。

文章还谈到了渲染的未来，提到Epic的Nanite技术，作为一个通过使用连续LOD系统和屏幕空间着色器方法来避免微小三角形问题的例子，将繁重的片段工作转移到屏幕空间，并使用计算着色器处理微小三角形。这表明优化策略将随着GPU架构和渲染技术的进步而不断发展。

---

## 44. 多平台矩阵乘法内核

**原文标题**: Multiplatform Matrix Multiplication Kernels

**原文链接**: [https://burn.dev/blog/sota-multiplatform-matmul/](https://burn.dev/blog/sota-multiplatform-matmul/)

本文探讨了在不同硬件平台上实现高性能矩阵乘法的挑战，尤其是在人工智能工作负载中，矩阵乘法是一项基本操作。研究表明，关键瓶颈在于数据移动而非计算本身，因此需要融合操作的定制内核。虽然NVIDIA的cuBLAS/cuDNN提供了优化内核，但它们缺乏灵活性和可扩展性。CUTLASS提供了更多的定制功能，但它是NVIDIA专用的，阻碍了跨平台优化。

为了解决这个问题，作者开发了CubeCL，一个用于为各种GPU和CPU生成优化矩阵乘法内核的系统。一个核心思想是，没有单一算法适合所有矩阵形状，因此需要可配置的算法。作者强调了理解GPU架构（SM、线程/单元、warp/plane、线程块/工作组）和内存资源（共享内存、寄存器）以优化内核设计的重要性。诸如合并内存访问、占用率以及平衡硬件调度与软件流水线等关键概念被重点强调。

CubeCL的核心是一个四级抽象层次结构：Tile Matmul（最低级别，处理单个乘加运算，可能使用Tensor Core或类似的加速器）、Stage Matmul（管理共享内存）、Global Matmul（累积来自Stage Matmuls的结果）和Batch Matmul（协调多个Global Matmuls）。这种分层结构支持一种分而治之的方法，以实现优化的数据局部性和移动。该系统将“plane”（warp/子组）作为最小的计算原语来优先处理，以避免分支并最大限度地提高性能。Tile Matmul层直接与硬件交互，并着重于高效利用硬件加速器（如果可用）。

---

## 45. 尝试 Guix：一个 Nix 使用者的印象

**原文标题**: Trying Guix: A Nixer's impressions

**原文链接**: [https://tazj.in/blog/trying-guix](https://tazj.in/blog/trying-guix)

本文详细介绍了 Nix 用户首次尝试 Guix 的体验，旨在在一台基于兆芯处理器的笔记本电脑上复制其标准桌面设置。作者是一位长期使用 Nix 且熟悉 Lisp 的用户，重点介绍了关键差异和观察结果。

一个主要区别是架构分层：与将 nixpkgs 作为数据结构导入的 Nix 不同，Guix 将 CLI 与包含所有软件包和模块的固定配置文件紧密集成。这使得 Guix 中的版本切换速度较慢，需要 `guix pull` 来重建 CLI。

作者赞扬 Guix 的卓越文档，这得益于其专注的文化，但也指出需要 Scheme 知识带来的挑战，以及需要使用 `nonguix` 来启用专有硬件支持所带来的复杂性。

Guix 中的性能明显较慢，`guix pull` 比 Nix 中更新 nixpkgs 花费的时间更长。虽然作者在一台强大的服务器上构建了系统配置，但将其部署到笔记本电脑上证明是困难的。

作者欣赏 Guix 使用 Shepherd（一种基于 Scheme 的 init 系统）而不是 systemd。

最终，作者成功安装了 Guix，但没有图形界面，这归因于缺少硬件配置以及缺乏与 `nixos-generate-config` 等效的功能。尽管存在挑战，但作者发现 Guix 由于 Lisp 集成和更具凝聚力的生态系统而引人入胜，并表达了希望实现与其 NixOS 桌面配置同等水平并提高迭代速度的愿望。作者承认 Guix 社区提出的潜在解决方案，但尚未对其进行测试。

---

## 46. 微软 Office 正在使用人为复杂的 XML 模式作为锁定工具。

**原文标题**: Microsoft Office is using an artificially complex XML schema as a lock-in tool

**原文链接**: [https://blog.documentfoundation.org/blog/2025/07/18/artificially-complex-xml-schema-as-lock-in-tool/](https://blog.documentfoundation.org/blog/2025/07/18/artificially-complex-xml-schema-as-lock-in-tool/)

本文认为，微软 Office 在其文档格式中使用了人为复杂的 XML 模式，作为一种锁定策略，阻碍互操作性，并将用户困在微软生态系统中。作者声称，XML 本应通过其简洁性促进知识共享，但微软故意引入不必要的复杂性，使得其他开发者难以创建兼容的软件。

这种“人为复杂性”包括深度嵌套的标签、过度抽象、非直观的命名、扩展点的广泛使用以及多个命名空间导入。尽管文档详尽，但整体的复杂性使得微软以外的人难以实现。

本文将此比作一个铁路系统，其中可访问的轨道因复杂的控制系统而受到破坏，从而有效地垄断了列车服务。 同样，微软利用其复杂的 XML 模式来控制对文档格式的访问，迫使用户接受他们的条款，例如从 Windows 10 切换到 Windows 11。

作者批评用户不加批判地接受微软的说法，并助长了这些锁定策略。他们认为，缺乏批判性评估使得微软得以巩固其垄断地位。文章最后倡导基于 XML 的系统的简洁性和清晰性，并警告说，复杂性会导致厂商锁定并限制用户自由。

---

## 47. 爱因斯坦相对论的新几何

**原文标题**: A New Geometry for Einstein's Theory of Relativity

**原文链接**: [https://www.quantamagazine.org/a-new-geometry-for-einsteins-theory-of-relativity-20250716/](https://www.quantamagazine.org/a-new-geometry-for-einsteins-theory-of-relativity-20250716/)

本文探讨了维也纳的一个数学家团队开发的一种爱因斯坦广义相对论的新方法。标准理论在奇点和非光滑时空（例如黑洞中心）处会遇到困难，其方程在那里失效。由Clemens Sämann、Michael Kunzinger和Roland Steinbauer领导的维也纳团队正在设计新的几何技术来扩展该理论的范围。

他们最初的方法包括通过比较时空表面上绘制的三角形与具有已知曲率的参考表面上的三角形来估计截面曲率，从而绕过对微积分和平滑性假设的需求。这使他们能够在非光滑环境中证明霍金奇点定理的一个版本。

后来，受Gaspard Monge工作的启发，Robert McCann关于最优传输的工作为估计Ricci曲率（一种更平均的曲率测量方法）提供了另一种工具，方法是检查体积在时空中移动时如何变化。随后，Andrea Mondino和Stefan Suhr借鉴Kunzinger和Sämann的研究成果，调整了最优传输技术，使其能够在非光滑环境中工作。

最终目标是开发一种新的几何框架，该框架可以处理“边缘化”和“表现不佳”的时空，从而使数学家能够在标准广义相对论的限制之外探索宇宙，并在不依赖光滑时空假设的情况下理解奇点的本质。

---

## 48. Show HN: OrioleDB Beta12 功能与基准测试

**原文标题**: Show HN: OrioleDB Beta12 Features and Benchmarks

**原文链接**: [https://www.orioledb.com/blog/orioledb-beta12-benchmarks](https://www.orioledb.com/blog/orioledb-beta12-benchmarks)

OrioleDB是一个PostgreSQL存储扩展，旨在通过替换默认的堆存储引擎来提高可扩展性和性能。Beta12引入了诸如非B树索引、重放近期更改、表空间、填充因子、空间利用率统计以及超过32列的表等新功能。

性能方面的显著改进包括使用稀疏文件进行更高效的存储分配、撤销日志的分离、避免插入操作产生撤销记录的优化、用于主键查找的自定义扫描节点以及更快的B树导航。

使用TPC-C (go-tpc)、sysbench和OLTP工作负载进行的基准测试表明，OrioleDB的性能优于标准PostgreSQL堆存储引擎。

*   **go-tpc (TPC-C):** OrioleDB在各种实例大小的每分钟事务处理量（tpmC）方面显著优于堆，吞吐量最多可达两倍。
*   **sysbench:** OrioleDB平均约为19,000 QPS，而堆为9,500 QPS。
*   **OLTP:** OrioleDB平均约为37,000 QPS，而堆约为32,000 QPS。

本文提供了复制基准测试的说明。提供了一个Docker镜像以开始使用OrioleDB。本质上，OrioleDB Beta12被定位为PostgreSQL的重大性能升级，尤其是在事务和读密集型工作负载中。

---

## 49. 人工智能资本支出规模巨大，正在影响经济统计数据。

**原文标题**: AI capex is so big that it's affecting economic statistics

**原文链接**: [https://paulkedrosky.com/honey-ai-capex-ate-the-economy/](https://paulkedrosky.com/honey-ai-capex-ate-the-economy/)

大规模AI数据中心资本支出正在显著影响美国经济，可能掩盖了潜在的疲软并扭曲了经济数据。作者认为，主要由英伟达向超大规模企业销售驱动的AI资本支出已大幅增加，超过了互联网泡沫时期的电信支出峰值，并接近19世纪铁路基础设施支出占GDP的峰值比例。

文章强调，这笔巨额资本来自多个渠道，包括科技巨头的内部现金流、债务发行、股权发行、风险投资、特殊目的公司(SPV)和云消费承诺。然而，这种资本的重新分配正在削弱其他行业，例如非AI风险投资、云计算产品、制造业和一般基础设施，导致裁员和潜在的长期后果。

作者认为，AI资本支出正在充当一项实质性的，尽管是无意的，私营部门刺激计划，掩盖了经济疲软。作者估计，如果没有AI数据中心投资，第一季度GDP的萎缩可能会更加严重。文章最后强调了将如此大量的资本部署到快速贬值的AI基础设施中的非凡性和潜在的不可持续性。作者还指出了AI投资在广泛部署之前就导致裁员的讽刺之处。

---

## 50. Show HN: Molab，云端托管的 Marimo 笔记本工作区

**原文标题**: Show HN: Molab, a cloud-hosted Marimo notebook workspace

**原文链接**: [https://molab.marimo.io/notebooks](https://molab.marimo.io/notebooks)

Molab是Marimo Notebook的云端托管工作空间。Marimo被描述为下一代编程环境，专为数据设计，以Python存储，并针对快速实验进行了优化。Molab允许用户创建、运行和分享这些Marimo Notebook。该平台提供示例Notebook帮助用户入门，展示了诸如markdown写作、绘图、SQL使用、UI元素、Hugging Face推理、嵌入可视化、向量搜索、Polars机器人检测、使用anywidget的自定义小部件以及PyTorch集成等功能。这些示例展示了Marimo在Molab环境中的能力和多功能性。本质上，Molab提供了一个协作且易于访问的平台，用于使用Marimo Notebook开发和部署数据驱动的应用程序。

---

## 51. 魔法门之巅峰年

**原文标题**: The year of peak might and magic

**原文链接**: [https://www.filfre.net/2025/07/the-year-of-peak-might-and-magic/](https://www.filfre.net/2025/07/the-year-of-peak-might-and-magic/)

本文探讨了新世界计算公司“魔法门之英雄无敌巅峰之年”，特别关注1999年《魔法门之英雄无敌III：埃拉西亚的光复》的开发和发行。作者解释说，尽管创始人乔恩·范·卡内亨对游戏开发的兴趣逐渐减退，但该公司仍然成功地制作出商业上成功的游戏。

《英雄无敌III》在有限的预算和时间框架内开发，旨在进化而非彻底变革《英雄无敌II》的成功模式。相对的新人格雷格·富尔顿担任联合设计师，负责扩展游戏的内容和功能，同时保持其核心机制。游戏进行了图形更新，扩大了战斗地图，增加了派系、单位、建筑物，并增强了RPG元素。战役通过更丰富的故事情节和连续性得到了扩展。

虽然《英雄无敌III》被广泛认为是该系列的巅峰之作，但作者表示略微偏爱《英雄无敌II》，理由是其更具魅力的美学和更简单的派系结构。尽管如此，作者承认《英雄无敌III》是一款令人非常满意的游戏，赞扬其巧妙的设计以及增加的元素，这些元素增强了多样性而又不会使游戏玩法过于复杂。本文详细介绍了作者对这两款游戏的个人体验。文章最后指出，该游戏凭借扩展包和附加功能的缓慢燃烧式的成功，巩固了其作为该系列中一个决定性条目的地位。

---

## 52. 新加坡积极应对针对关键基础设施的持续网络攻击

**原文标题**: Singapore actively dealing with ongoing cyberattack on critical infrastructure

**原文链接**: [https://www.channelnewsasia.com/singapore/unc3886-cyber-security-threat-actor-attack-singapore-5245791](https://www.channelnewsasia.com/singapore/unc3886-cyber-security-threat-actor-attack-singapore-5245791)

新加坡正积极应对针对其关键基础设施的网络攻击，该攻击由被谷歌旗下网络安全公司Mandiant认定为“中国关联间谍组织”的“高度复杂的威胁行为者”UNC3886发起。国家安全统筹部长尚穆根强调了这一威胁的严重性，并指出其有可能破坏国家安全。

新加坡网络安全局（CSA）正在主导调查，为受影响的组织提供支持，并监测能源、水务、银行和通信等关键领域。由于调查仍在进行中，为维护行动安全，详细信息暂不公开。

UNC3886部署先进工具，逃避侦测，并维持持续访问，针对高价值战略目标。2021年至2024年期间，针对新加坡的APT攻击显著增加。尚穆根强调，实际冲突正日益蔓延至网络空间，新加坡因其地缘政治重要性和作为数字枢纽的地位而成为攻击目标。

尚穆根还指出，很大一部分新加坡组织遭受过网络攻击，威胁来自网络犯罪分子和外国行为者。政府认识到攻击有时不可避免地会成功，因此致力于加强网络防御，重新审查供应商，并专注于预防和遏制，以维护对新加坡系统的信任和信心。

---

## 53. 当 root 遇上不可变：OpenBSD chflags 与日志篡改

**原文标题**: When root meets immutable: OpenBSD chflags vs. log tampering

**原文链接**: [https://rsadowski.de/posts/2025/openbsd-immutable-system-logs/](https://rsadowski.de/posts/2025/openbsd-immutable-system-logs/)

本文介绍如何使用`chflags`命令在OpenBSD上实现日志完整性的ISO 27001合规性，以利用文件系统级别的不可变性。作者强调，虽然ISO 27001没有明确要求不可变的日志，但保护日志免受篡改对于安全漏洞后的取证分析至关重要。

OpenBSD的默认日志记录设置是有效的，但容易受到root访问权限泄露的影响。拥有root权限的攻击者可以轻松修改或删除日志文件，从而破坏其可信度。本文重点介绍了`chflags`中的`sappnd`（系统仅追加）和`schg`（系统不可变）标志，作为一种解决方案。

所提出的实现方案包括禁用默认的`newsyslog` cron作业，并为存档日志创建一个专用的`/var/log/archive`目录。然后，将活动日志文件设置为`sappnd`标志，防止修改但允许追加。`/var/log/archive`中的存档日志设置为`schg`标志，使其完全不可变。

为了管理日志轮换，作者介绍了`/etc/rc.securelevel`，这是一个在安全级别提高之前启动时执行的脚本。该脚本删除`sappnd`和`schg`标志，将日志轮换到存档中，然后立即恢复这些标志，确保保持不可变性。此过程无需手动干预即可自动完成，从而增强合规性和安全性。

---

## 54. Kimi研究员的苦涩品味

**原文标题**: The Bitter Lessons Behind Kimi Researcher's Taste

**原文链接**: [https://medium.com/@xinyijin715/maker-story-the-bitter-lessons-behind-kimi-researchers-ui-6654ec66662c](https://medium.com/@xinyijin715/maker-story-the-bitter-lessons-behind-kimi-researchers-ui-6654ec66662c)

Kimi研究员的文章详细介绍了创造美观且实用的AI界面所面临的挑战性和迭代过程，力求摆脱“平庸”的设计。 这一过程包括在团队内部定义共同的审美愿景，平衡美学与功能和数据准确性，以及关注用户体验。

主要收获包括：

*   **反平庸设计：** 不满足于简单的复制，努力创造独特且具有冲击力的设计，灵感来源于文艺复兴艺术和顶级出版物等多种来源。
*   **团队一致性：** 创建“平庸设计评估”文档，以标准化审美理解，并确保团队在设计原则上达成一致。
*   **不可能的三角：** 平衡美学、交互和数据准确性是一个持续的挑战，需要不断迭代和妥协。
*   **迭代过程：** 实验、记录和改进对于实现理想的平衡至关重要。 使用特定的前缀来跟踪实验迭代。
*   **用户体验至上：** 融入视觉元素（图表、示意图）和交互功能（JS动画、带有导航的网格布局），以增强深度研究用户的参与度和可访问性。
*   **团队合作的重要性：** 协作和不同的视角对于应对复杂的挑战至关重要，特别是准确性评估。

文章强调，设计是一个不断发展的过程，需要不断的质疑、改进和协作，才能创造真正卓越且实用的体验。 它还强调了不满足于现状并不断突破美学界限的重要性。 该团队集成了一个AI评判工具来帮助评估设计决策，从而加快了流程并保持了准确性。

---

## 55. 大乌龙：三十五年错误的剖析

**原文标题**: The Big Oops: Anatomy of a Thirty-Five Year Mistake

**原文链接**: [https://www.computerenhance.com/p/the-big-oops-anatomy-of-a-thirty](https://www.computerenhance.com/p/the-big-oops-anatomy-of-a-thirty)

Casey Muratori 在 Better Software Conference 上发表了题为“大型 OOPs：三十五年错误的剖析”的演讲，并对此进行了讨论。 根据标题判断，该演讲可能批判了面向对象编程 (OOP)。 他原本希望运行时长在两小时之内，但不得不省略细节和故事，特别是关于 Smalltalk 的发展。

Muratori 通过回顾大量的原始资料进行了准备，并表示有兴趣通过潜在的直播来分享更多见解，以讨论演讲中未提及的文件。

他为那些想进一步探索该主题的人推荐了四部“历史”著作：Alan Kay 的《Smalltalk 的早期历史》、Bjarne Stroustrup 的《C++ 的历史》、Ole-Johan Dahl 和 Kristen Nygaard 的《Simula 语言的发展》以及 Douglass T. Ross 的《自动编程工具 APT 语言的起源》。

他强调了使用历史论文的特定版本的重要性，并强调存在内容各异的多种扫描版本（尤其是附录）。 他指出，1956 年 APT 语言的“plex”实现是他发现的最早的编程实例，其中使用高度结构化的数据来促进程序运行，而不仅仅是数据仓库。 他鼓励任何知道更早例子的人与他联系。

---

## 56. lsr: 使用io_uring的ls

**原文标题**: lsr: ls with io_uring

**原文链接**: [https://rockorager.dev/log/lsr-ls-but-with-io-uring/](https://rockorager.dev/log/lsr-ls-but-with-io-uring/)

作者创建了`lsr`，一个利用`io_uring`接口优化I/O操作的自定义`ls`命令实现。`lsr`在执行时间和系统调用次数方面均显著优于标准`ls`以及其他替代方案，如`eza`、`lsd`和`uutils ls`。基准测试表明，`lsr`始终更快，尤其是在处理大型目录时，并且系统调用次数减少了一个数量级。

`lsr`通过为所有可能的I/O操作（包括打开目录、读取用户/组数据和执行`stat`调用）使用`io_uring`来实现这一点。它还采用了一个带有1MB预分配的`StackFallbackAllocator`来最大限度地减少`mmap`调用，进一步降低了系统调用开销。此外，`lsr`避免了动态链接和相关的libc开销。

作者指出，`lsr`的大部分运行时间都花在了排序上，这表明存在进一步优化的潜力。他们对`lsd`发出的`clock_gettime`调用次数之多感到惊讶。作者使用tangled.sh，并欢迎通过该仓库提交错误报告和更改。

---

## 57. 癌症DNA在确诊前数年即可在血液中检测到

**原文标题**: Cancer DNA is detectable in blood years before diagnosis

**原文链接**: [https://www.sciencenews.org/article/cancer-tumor-dna-blood-test-screening](https://www.sciencenews.org/article/cancer-tumor-dna-blood-test-screening)

癌症发现：在诊断前数年即可在血液中检测到癌细胞DNA

---

## 58. 我如何跟上人工智能的进展

**原文标题**: How I keep up with AI progress

**原文链接**: [https://blog.nilenso.com/blog/2025/06/23/how-i-keep-up-with-ai-progress/](https://blog.nilenso.com/blog/2025/06/23/how-i-keep-up-with-ai-progress/)

Atharva Raykar 的文章概述了一种策略，用于随时了解快速发展的生成式人工智能领域，强调通过关注主要来源和值得信赖的评论员来避免虚假信息的重要性。他告诫不要低估或高估人工智能的能力，敦促读者培养对该技术的扎实理解。

Raykar 的信息管道以 **Simon Willison's Blog** 为中心，重点介绍了其对人工智能能力、应用和伦理考量的评论。他还建议关注 **Andrej Karpathy**，以了解人工智能模型内部的见解。建议使用 **Every's Chain of Thought** 来了解模型的实际应用和“氛围检查”。

一个核心原则是优先考虑 **来自 OpenAI、Google DeepMind 和 Anthropic 等人工智能实验室的官方公告、博客和论文**，绕过二手解读。他强调，将人工智能投入生产的个人经验甚至胜过官方建议。

Raykar 提供了一份经过筛选的 **高价值人士** 名单，这些人都在积极为人工智能工程生态系统做出贡献，提供有关评估、RAG、人工智能工具以及在生产中构建人工智能系统等主题的详细见解。主要人物包括 Hamel Husain、Shreya Shankar、Jason Liu、Eugene Yan、Chip Huyen 等。

对于新闻和媒体，Raykar 推荐 **Twitter/X**，尽管它具有潜在的毒性，但他指出它的价值，并建议 **Shawn Wang (swyx)** 或他的 AI 新闻网站 **smol.ai** 作为避免使用 Twitter 的替代方案。他还提到 **Dwarkesh Patel 的播客** 是一个很好的来源。

最后，他强调了更深奥的来源，例如 **LessWrong/AI Alignment Forum** 和 **Gwern**，以更深入地研究人工智能对齐、治理和技术讨论。他还提到了探索 LLM 行为的“提示工程师”的工作。

---

## 59. 奔奔：一个用 Common Lisp 编写的终端音频播放器

**原文标题**: Benben: An audio player for the terminal, written in Common Lisp

**原文链接**: [https://chiselapp.com/user/MistressRemilia/repository/benben/home](https://chiselapp.com/user/MistressRemilia/repository/benben/home)

Benben：Linux和类Unix系统的命令行音频播放器和转换器，以其速度、效率和老式风格界面而闻名。它支持多种音频格式，包括VGM、MP3、Ogg Vorbis、FLAC、MIDI和模块格式。它专为喜欢基于终端的界面并在文件夹中组织音乐的用户而设计。

最新版本是v0.6.1，但0.7.0版本正在开发中，它代表了用Common Lisp进行的完全重写。以前的版本是用Crystal编写的。

主要功能包括ALSA、libout123和libao后端、高性能播放、快速多线程S-Lang UI、循环播放、TCP输出、播放列表支持（XSPF、JSPF）、高质量重采样和强大的配置文件系统。它还提供并行音频渲染到WAV或Au、可定制的VU表、键盘控制、ReplayGain支持、远程控制功能和ListenBrainz集成。可选效果包括软削波、参数均衡器、立体声增强、混响和直流偏移滤波器。

该程序主要由Remilia Scarlet开发和维护，她欢迎通过Ko-Fi或Liberapay提供支持。鼓励通过Fossil存储库进行贡献，并提供有关分支、捆绑更改和联系Remilia的说明。Benben根据GNU Affero通用公共许可证第3版获得许可。

---

## 60. 用VIC-20、算盘和狗复制量子因式分解记录

**原文标题**: Replication of Quantum Factorisation Records with a VIC-20, an Abacus, and a Dog

**原文链接**: [https://eprint.iacr.org/2025/1237](https://eprint.iacr.org/2025/1237)

这篇预印本发表于密码学电子预印本库，幽默地宣称奥克兰大学的Peter Gutmann和苏黎世应用科技大学的Stephan Neuhaus已成功复制甚至超越了当前的量子分解记录，他们使用的非常规计算方法包括：一台VIC-20 8位家用电脑、一个算盘和一条狗。

作者声明他们的工作旨在激励未来在匹配任何潜在量子分解进展方面的努力。论文标题和摘要显然是讽刺性的，暗示了对量子计算炒作或缺乏实际进展的批评。虽然摘要提到修订说明了使用sqrt(n)进行分解，但这可能进一步增加了幽默意图，暗示以一种微不足道的方法解决复杂问题。

该论文被归类为“攻击和密码分析”，关键词包括“pqc”（后量子密码学）和“量子分解”，这意味着可能评论量子计算对现有密码算法构成的安全威胁以及对后量子替代方案的需求。该论文以PDF格式提供，并包含BibTeX信息，表明具有一定程度的学术规范性，或许是为了传递其讽刺信息的载体。

---

## 61. 特朗普将签署稳定币法案，这或将使贿赂总统变得更容易。

**原文标题**: Trump to sign stablecoin bill that may make it easier to bribe the president

**原文链接**: [https://arstechnica.com/tech-policy/2025/07/stablecoin-bill-heads-to-trumps-desk-without-blocks-on-presidential-grifting/](https://arstechnica.com/tech-policy/2025/07/stablecoin-bill-heads-to-trumps-desk-without-blocks-on-presidential-grifting/)

特朗普即将签署《天才法案》，该法案为稳定币建立联邦框架，标志着他在加密货币相关立法方面取得的首个重大胜利。支持者声称这将刺激加密货币的更广泛采用，但像众议员玛克辛·沃特斯这样的批评者警告说，该法案缺乏消费者保护，并可能助长腐败，特别是允许总统不受限制地从加密货币风险投资中获利。《天才法案》要求稳定币发行商公布月度储备和年度报表，但人们仍然担心公司可能会将稳定币与高风险资产挂钩，从而可能损害投资者。消费者权益倡导者担心在缺乏类似监督的情况下出现“类似银行的活动”。包括《清晰法案》（旨在将监管权力从美国证券交易委员会转移到商品期货交易委员会）和一项禁止央行数字货币的法案在内的其他加密货币立法，在参议院面临重大障碍。分析人士预测这些法案不太可能获得通过，这表明《天才法案》可能是近期内加密货币领域的最后一次胜利。沃特斯警告说，该法案允许特朗普个人获利，同时可能引发金融危机。文章还指出，由于特朗普家族参与加密货币风险投资，可能存在利益冲突。

---

## 62. 环保署称将取消其科学研究部门。

**原文标题**: EPA says it will eliminate its scientific research arm

**原文链接**: [https://www.nytimes.com/2025/07/18/climate/epa-firings-scientific-research.html](https://www.nytimes.com/2025/07/18/climate/epa-firings-scientific-research.html)

无法访问文章链接。

---

## 63. OpenAI声称将在2025年国际数学奥林匹克竞赛中获得金牌标准

**原文标题**: OpenAI claiming gold medal standard at IMO 2025

**原文链接**: [https://github.com/aw31/openai-imo-2025-proofs](https://github.com/aw31/openai-imo-2025-proofs)

OpenAI评估实验性推理LLM挑战2025国际数学奥林匹克竞赛，并公开证明过程。

---

## 64. CP/M 创始人盖瑞·基尔代尔回忆录免费下载

**原文标题**: CP/M creator Gary Kildall's memoirs released as free download

**原文链接**: [https://spectrum.ieee.org/cpm-creator-gary-kildalls-memoirs-released-as-free-download](https://spectrum.ieee.org/cpm-creator-gary-kildalls-memoirs-released-as-free-download)

本文宣布 CP/M 创始人盖瑞·基尔代尔的回忆录可供免费下载。文章强调了基尔代尔在技术领域的先锋作用，并认为他的故事体现了早期创业文化精神。文章还提到了作者，前 IEEE Spectrum 编辑 Tekla S. Perry，并包含照片来源信息。重点是基尔代尔的回忆录现已发布，让人们可以深入了解 CP/M 背后的这位有影响力人物的生活和工作。

---

## 65. 我们不破坏用户空间（2012）

**原文标题**: We do not break userspace (2012)

**原文链接**: [https://lore.kernel.org/all/CA+55aFy98A+LJK4+GWMcbzaa1zsPBRo76q+ioEjbx-uaMKH6Uw@mail.gmail.com/](https://lore.kernel.org/all/CA+55aFy98A+LJK4+GWMcbzaa1zsPBRo76q+ioEjbx-uaMKH6Uw@mail.gmail.com/)

本页解释了网站使用 Anubis 安全系统的原因。Anubis 是一种工作量证明 (PoW) 系统，旨在防止人工智能公司过度抓取网站，这可能导致普通用户出现停机和资源无法访问的情况。它是一种临时解决方案，同时也在开发更复杂的方法，例如通过字体渲染分析来指纹识别无头浏览器，从而区分合法用户和抓取工具。

Anubis 旨在通过要求用户在访问网站之前执行少量工作（类似于 Hashcash），使人工智能公司的抓取行为在计算上更加昂贵。虽然个人负载很小，但在大规模抓取时会变得非常显著。

该系统需要 JavaScript 才能运行，因为人工智能公司从根本上改变了网站托管的动态。用户可能需要禁用诸如 JShelter 等注重隐私的浏览器扩展程序才能通过 Anubis 挑战。该页面还表明正在开发一种无 JavaScript 的解决方案。当前 Anubis 版本为 1.20.0。

---

## 66. 哈提信托数字图书馆

**原文标题**: HathiTrust Digital Library

**原文链接**: [https://www.hathitrust.org/](https://www.hathitrust.org/)

无法访问文章链接。

---

## 67. Fully homomorphic encryption and the dawn of a private internet

**原文标题**: Fully homomorphic encryption and the dawn of a private internet

**原文链接**: [https://bozmen.io/fhe](https://bozmen.io/fhe)

This article explores Fully Homomorphic Encryption (FHE) and its potential to revolutionize internet privacy. FHE allows computations to be performed on encrypted data without decryption, ensuring data remains private "in use," addressing a critical vulnerability in current security models.

While FHE isn't widely adopted due to performance overhead (1,000x-10,000x slower than plaintext operations), its speed is improving exponentially, roughly 8x faster each year, reminiscent of Moore's Law. This "Moore's Law of FHE" suggests an impending inflection point where FHE becomes practical for applications like encrypted cloud computing, LLM inference, and confidential smart contracts.

The article details how FHE works, focusing on lattice-based cryptography and concepts like Learning With Errors (LWE) to maintain quantum-resistance. It explains the challenges of noise management during homomorphic operations and highlights "bootstrapping" as a solution to refresh ciphertexts and enable unlimited computations. Relinearization and modulus switching are also introduced as techniques to manage ciphertext complexity and noise.

The piece differentiates between partial, somewhat, and fully homomorphic encryption, providing a Paillier example to illustrate additive homomorphism. Ultimately, the article argues that FHE could shift the internet from a "spy by default" paradigm to a "privacy by default" one, obsoleting business models reliant on user data harvesting.


---

## 68. eslint-config-prettier npm package compromised

**原文标题**: eslint-config-prettier npm package compromised

**原文链接**: [https://www.stepsecurity.io/blog/supply-chain-security-alert-eslint-config-prettier-package-shows-signs-of-compromise](https://www.stepsecurity.io/blog/supply-chain-security-alert-eslint-config-prettier-package-shows-signs-of-compromise)

生成摘要时出错

---

## 69. Teufel Mynd open source / open hardware Bluetooth speaker

**原文标题**: Teufel Mynd open source / open hardware Bluetooth speaker

**原文链接**: [https://lu.teufelaudio.com/mynd-107002004](https://lu.teufelaudio.com/mynd-107002004)

生成摘要时出错

---

## 70. How to Get Foreign Keys Horribly Wrong

**原文标题**: How to Get Foreign Keys Horribly Wrong

**原文链接**: [https://hakibenita.com/django-foreign-keys](https://hakibenita.com/django-foreign-keys)

生成摘要时出错

---

## 71. Cats as Horror Movie Villains

**原文标题**: Cats as Horror Movie Villains

**原文链接**: [https://gwern.net/cat-horror](https://gwern.net/cat-horror)

生成摘要时出错

---

## 72. How a Florida Pension Fund manager produced 50 years of market-beating returns

**原文标题**: How a Florida Pension Fund manager produced 50 years of market-beating returns

**原文链接**: [https://www.barrons.com/articles/florida-pension-plan-50-years-of-market-beating-returns-b9f78df9](https://www.barrons.com/articles/florida-pension-plan-50-years-of-market-beating-returns-b9f78df9)

生成摘要时出错

---

## 73. Psilocybin decreases depression and anxiety in cancer patients (2016)

**原文标题**: Psilocybin decreases depression and anxiety in cancer patients (2016)

**原文链接**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC5367557/](https://pmc.ncbi.nlm.nih.gov/articles/PMC5367557/)

生成摘要时出错

---

## 74. Inspect ANSI control codes and escape sequences

**原文标题**: Inspect ANSI control codes and escape sequences

**原文链接**: [https://ansi.tools](https://ansi.tools)

生成摘要时出错

---

## 75. 光环效应

**原文标题**: The Halo Effect

**原文链接**: [https://kwokchain.com/2025/07/15/the-halo-effect/](https://kwokchain.com/2025/07/15/the-halo-effect/)

生成摘要时出错

---

## 76. 15 Years of Building Jefit

**原文标题**: 15 Years of Building Jefit

**原文链接**: [https://www.jefit.com/our-story](https://www.jefit.com/our-story)

Ying, the founder of Jefit, recounts the company's 15-year journey from a personal project to a workout tracking platform with over 13 million users. Started in his dad's living room to solve his own workout accountability issues, Jefit evolved into a social workout platform driven by user feedback. After incorporating in 2010, the company bootstrapped its growth with a small team, focusing on providing valuable tools for purposeful training.

A significant turning point was the decision to relocate to Silicon Valley to find the right talent, a difficult process that took two years. The core team values training, quality, and discipline, fostering a culture of continuous improvement and user-centric development.

Ying acknowledges challenges like COVID lockdowns, rejections from VCs, and product missteps that led to engineering debt. However, user loyalty motivated them to improve.

Looking ahead, Jefit is focusing on platform modernization, including a refreshed mobile app, improved logging, progress reports, goal-setting tools, and AI-driven features, all while maintaining a focus on quality control. Ying expresses gratitude to the Jefit community, highlighting their consistency and dedication. The article concludes with a message of encouragement and continued commitment to the power of long-term effort, not just for lifters, but anyone committed to self-improvement.


---

## 77. ChatGPT agent: bridging research and action

**原文标题**: ChatGPT agent: bridging research and action

**原文链接**: [https://openai.com/index/introducing-chatgpt-agent/](https://openai.com/index/introducing-chatgpt-agent/)

生成摘要时出错

---

## 78. Mistral Releases Deep Research, Voice, Projects in Le Chat

**原文标题**: Mistral Releases Deep Research, Voice, Projects in Le Chat

**原文链接**: [https://mistral.ai/news/le-chat-dives-deep](https://mistral.ai/news/le-chat-dives-deep)

生成摘要时出错

---

## 79. Winaero Tweaker: All-in-one app for tuning Windows

**原文标题**: Winaero Tweaker: All-in-one app for tuning Windows

**原文链接**: [https://winaerotweaker.com/](https://winaerotweaker.com/)

生成摘要时出错

---

## 80. Evaluating publicly available LLMs on IMO 2025

**原文标题**: Evaluating publicly available LLMs on IMO 2025

**原文链接**: [https://matharena.ai/imo/](https://matharena.ai/imo/)

生成摘要时出错

---

## 81. Show HN: Simulating autonomous drone formations

**原文标题**: Show HN: Simulating autonomous drone formations

**原文链接**: [https://github.com/sushrut141/ketu](https://github.com/sushrut141/ketu)

生成摘要时出错

---

## 82. LibreOffice slams Microsoft for locking in Office users w/ complex file formats

**原文标题**: LibreOffice slams Microsoft for locking in Office users w/ complex file formats

**原文链接**: [https://www.neowin.net/news/libreoffice-calls-out-microsoft-for-using-complex-file-formats-to-lock-in-office-users/](https://www.neowin.net/news/libreoffice-calls-out-microsoft-for-using-complex-file-formats-to-lock-in-office-users/)

生成摘要时出错

---

## 83. Hundred Rabbits – Low-tech living while sailing the world

**原文标题**: Hundred Rabbits – Low-tech living while sailing the world

**原文链接**: [https://100r.co/site/home.html](https://100r.co/site/home.html)

生成摘要时出错

---

## 84. Show HN: I built library management app for those who outgrew spreadsheets

**原文标题**: Show HN: I built library management app for those who outgrew spreadsheets

**原文链接**: [https://www.librari.io/](https://www.librari.io/)

生成摘要时出错

---

## 85. Fibonacci(50) as a Fractal Sequence Diagram

**原文标题**: Fibonacci(50) as a Fractal Sequence Diagram

**原文链接**: [https://app.ilograph.com/demo.ilograph.Fibonacci%2520Sequence/Fib(50)](https://app.ilograph.com/demo.ilograph.Fibonacci%2520Sequence/Fib(50))

生成摘要时出错

---

## 86. The Great Unracking: Saying goodbye to the servers at our physical datacenter

**原文标题**: The Great Unracking: Saying goodbye to the servers at our physical datacenter

**原文链接**: [https://stackoverflow.blog/2025/07/16/the-great-unracking-saying-goodbye-to-the-servers-at-our-physical-datacenter/](https://stackoverflow.blog/2025/07/16/the-great-unracking-saying-goodbye-to-the-servers-at-our-physical-datacenter/)

生成摘要时出错

---

## 87. TCP-in-UDP Solution (eBPF)

**原文标题**: TCP-in-UDP Solution (eBPF)

**原文链接**: [https://blog.mptcp.dev/2025/07/14/TCP-in-UDP.html](https://blog.mptcp.dev/2025/07/14/TCP-in-UDP.html)

生成摘要时出错

---

## 88. Show HN: Mochi Invaders – Like Space Invaders but for Practicing Japanese Kana

**原文标题**: Show HN: Mochi Invaders – Like Space Invaders but for Practicing Japanese Kana

**原文链接**: [https://xenodium.com/mochi-invaders-now-on-the-app-store](https://xenodium.com/mochi-invaders-now-on-the-app-store)

生成摘要时出错

---

## 89. NIH is cheaper than the wrong dependency

**原文标题**: NIH is cheaper than the wrong dependency

**原文链接**: [https://lewiscampbell.tech/blog/250718.html](https://lewiscampbell.tech/blog/250718.html)

生成摘要时出错

---

## 90. Extending That XOR Trick to Billions of Rows

**原文标题**: Extending That XOR Trick to Billions of Rows

**原文链接**: [https://nochlin.com/blog/extending-that-xor-trick](https://nochlin.com/blog/extending-that-xor-trick)

生成摘要时出错

---

## 91. My favorite use-case for AI is writing logs

**原文标题**: My favorite use-case for AI is writing logs

**原文链接**: [https://newsletter.vickiboykis.com/archive/my-favorite-use-case-for-ai-is-writing-logs/](https://newsletter.vickiboykis.com/archive/my-favorite-use-case-for-ai-is-writing-logs/)

生成摘要时出错

---

## 92. DIY Telescope Mods That Transformed My Astrophotography

**原文标题**: DIY Telescope Mods That Transformed My Astrophotography

**原文链接**: [https://www.youtube.com/watch?v=Efmzr_K4ApQ](https://www.youtube.com/watch?v=Efmzr_K4ApQ)

生成摘要时出错

---

## 93. Row Polymorphic Programming

**原文标题**: Row Polymorphic Programming

**原文链接**: [https://www.stranger.systems/posts/by-slug/row-polymorphic-programming.html](https://www.stranger.systems/posts/by-slug/row-polymorphic-programming.html)

生成摘要时出错

---

## 94. Converting Integers to Floats Using Hyperfocus (2022)

**原文标题**: Converting Integers to Floats Using Hyperfocus (2022)

**原文链接**: [https://blog.m-ou.se/floats/](https://blog.m-ou.se/floats/)

This article recounts the author's humorous and determined journey to create a faster `u128` to `f64` conversion than the built-in Rust compiler (Rustc). Initially, the author, spurred by a pull request review, implemented a custom conversion using bit manipulation and `f64::from_bits`, bypassing the inefficient string-based conversion.

The author details the process, including fixing bugs related to edge cases like zero, refining rounding, and simplifying the bit-twiddling code. The "trick" was to manually calculate the floating point representation's sign, exponent and mantissa and construct the f64 from that. The author then realised that a simpler `x as f64` already existed, triggering a pursuit for performance gains out of spite and to "prove" it was fun.

The article then explains the IEEE 754 binary64 standard, breaking down the f64 bit structure into sign, exponent, and mantissa, and how these components represent floating-point values.

The author then details the steps of their implementation, including handling the zero edge case, calculating the exponent, extracting the mantissa, and implementing proper rounding to adhere to the IEEE 754 standard, which involves checking the "dropped bits" to decide whether to round up or down, and also implement "round to even" for tie-breaking. Finally, the author simplifies the code for conciseness, resulting in a refined, potentially faster, conversion.


---

## 95. A look at IBM's short-lived "butterfly" ThinkPad 701 of 1995

**原文标题**: A look at IBM's short-lived "butterfly" ThinkPad 701 of 1995

**原文链接**: [https://www.fastcompany.com/91356463/ibm-thinkpad-701-butterfly-keyboard](https://www.fastcompany.com/91356463/ibm-thinkpad-701-butterfly-keyboard)

生成摘要时出错

---

## 96. Run TypeScript code without worrying about configuration

**原文标题**: Run TypeScript code without worrying about configuration

**原文链接**: [https://tsx.is/](https://tsx.is/)

生成摘要时出错

---

## 97. Third patient dies from acute liver failure caused by a Sarepta gene therapy

**原文标题**: Third patient dies from acute liver failure caused by a Sarepta gene therapy

**原文链接**: [https://www.biocentury.com/article/656520/third-death-from-a-sarepta-gene-therapy](https://www.biocentury.com/article/656520/third-death-from-a-sarepta-gene-therapy)

生成摘要时出错

---

## 98. The Art of Roland-Garros

**原文标题**: The Art of Roland-Garros

**原文链接**: [https://www.garros.gallery/](https://www.garros.gallery/)

生成摘要时出错

---

## 99. Firefox-patch-bin, librewolf-fix-bin AUR packages contain malware

**原文标题**: Firefox-patch-bin, librewolf-fix-bin AUR packages contain malware

**原文链接**: [https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/thread/7EZTJXLIAQLARQNTMEW2HBWZYE626IFJ/](https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/thread/7EZTJXLIAQLARQNTMEW2HBWZYE626IFJ/)

生成摘要时出错

---

## 100. In the long run, GPL code becomes irrelevant (2015)

**原文标题**: In the long run, GPL code becomes irrelevant (2015)

**原文链接**: [https://josephg.com/blog/in-the-long-run-gpl-code-becomes-irrelevant/](https://josephg.com/blog/in-the-long-run-gpl-code-becomes-irrelevant/)

生成摘要时出错

---

