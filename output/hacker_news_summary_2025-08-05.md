# Hacker News 热门文章摘要 (2025-08-05)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. OpenAI 开放模型

**原文标题**: OpenAI Open Models

**原文链接**: [https://openai.com/open-models/](https://openai.com/open-models/)

无法访问文章链接。

---

## 2. Genie 3：世界模型的新前沿

**原文标题**: Genie 3: A new frontier for world models

**原文链接**: [https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/](https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/)

谷歌DeepMind发布的Genie 3代表了世界模型方面的重大进步，它能够根据文本提示生成多样化的、可交互的环境。它允许以24fps和720p分辨率进行实时导航，并保持数分钟的一致性。

在Genie 1、Genie 2、Veo 2和Veo 3等先前工作的基础上，Genie 3以其实时交互性、改进的一致性和真实感而脱颖而出。它模拟了水、光照和复杂的环境互动等物理属性，并模拟了具有动物行为和植物生命的自然生态系统。它还支持动画和虚构场景，允许用户探索奇幻的场景。

Genie 3可以生成地点和历史背景，将用户传送到不同的地理位置和时代。一项关键创新是该模型能够长时间保持环境一致性，即使在时间流逝后重新访问某个地点也是如此。这种一致性是有机产生的，不像依赖显式3D表示的方法。

除了导航之外，Genie 3还引入了“可提示的世界事件”，使用户能够通过更改天气、添加对象或通过文本提示引入角色来改变生成的世界。这扩展了超越简单导航的交互可能性。

---

## 3. OpenAI 和谐

**原文标题**: OpenAI Harmony

**原文链接**: [https://github.com/openai/harmony](https://github.com/openai/harmony)

本文介绍了OpenAI Harmony，一种为gpt-oss开源权重模型系列设计的响应格式。它对于有效地与gpt-oss交互至关重要，并有助于结构化输出，包括思维链、工具调用和指令层级。

如果您正在使用诸如HuggingFace、Ollama或vLLM之类的API或提供商，通常会自动处理该格式。但是，如果您正在构建自定义推理解决方案，那么理解Harmony至关重要。

该格式允许模型输出到多个通道，例如“分析”、“评论”和“最终”，其中指定特定通道用于工具调用（例如，“functions”到“commentary”）。

本文档随后提供了在Python和Rust中使用Harmony的指南，展示了安装说明和代码示例。这两种语言都利用了`openai-harmony`库。Python支持包括类型存根。Rust强调性能，其核心构建于Rust中，并通过PyO3绑定暴露给Python。

最后，本文档概述了项目的存储库布局，并提供了本地开发说明，包括设置虚拟环境、编译Rust crate以及运行Rust和Python测试套件，以确保实现的对等性。

---

## 4. uBlock Origin Lite 现已支持 Safari

**原文标题**: uBlock Origin Lite now available for Safari

**原文链接**: [https://apps.apple.com/app/ublock-origin-lite/id6745342698](https://apps.apple.com/app/ublock-origin-lite/id6745342698)

uBlock Origin Lite (uBOL)：一款轻量级内容拦截器现已登陆 Safari。它采用声明式内容拦截方法，意味着浏览器本身使用内置机制处理过滤，而不是依赖于持久扩展进程。这最大限度地减少了 CPU/内存占用，因为 uBOL 进程仅在用户与弹出面板或设置交互时才处于活动状态。

默认情况下，uBOL 使用与原始 uBlock Origin 相似的过滤器集合，包括内置列表、EasyList、EasyPrivacy 和 Peter Lowe 的广告和跟踪服务器列表。用户可以通过选项页面添加更多过滤器列表。

开发者 Raymond Hill 向用户保证，uBOL 不会收集任何数据。它兼容 iPhone (iOS 18.0+)、iPad (iPadOS 18.0+)、Mac (macOS 15.0+) 和 Apple Vision (visionOS 2.0+)，并且免费提供。该应用程序大小为 5.8MB，类别为实用工具。

---

## 5. 克勞德Opus 4.1

**原文标题**: Claude Opus 4.1

**原文链接**: [https://www.anthropic.com/news/claude-opus-4-1](https://www.anthropic.com/news/claude-opus-4-1)

Anthropic 发布 Claude Opus 4.1，面向付费用户，在 Claude Code 中以及通过 Amazon Bedrock 和 Google Cloud 的 Vertex AI 等 API 提供，价格与 Opus 4 相同。此次更新侧重于增强 Agentic 任务、真实世界编码和推理能力。

主要改进包括编码性能提升，在 SWE-bench Verified 上达到 74.5%，以及增强的研究和数据分析技能。特别是，Claude Opus 4.1 擅长多文件代码重构，能够在大型代码库中精确定位并纠正错误，而不会引入新的错误，正如乐天集团所指出的那样。Windsurf 报告称，在其初级开发人员基准测试中，Opus 4.1 比 Opus 4 提升了一个标准差。

Anthropic 建议将所有应用从 Opus 4 升级到 Opus 4.1，并通过 API 使用 `claude-opus-4-1-20250805` 进行访问。该版本包含文档、系统卡和定价信息。公告还提及了 Anthropic 安全框架、医疗保健互操作性承诺以及 Anthropic 团队对 Claude Code 的使用等最新消息。

---

## 6. 洛斯阿拉莫斯正在以每秒7百万帧的速度捕获爆炸的实时图像。

**原文标题**: Los Alamos is capturing real-time images of explosions at 7mths of a second

**原文链接**: [https://www.lanl.gov/media/publications/1663/dynamics-of-dynamic-imaging](https://www.lanl.gov/media/publications/1663/dynamics-of-dynamic-imaging)

洛斯阿拉莫斯国家实验室利用动态成像技术捕捉爆炸的实时图像，这对库存管理任务至关重要。这使科学家能够在不实际引爆武器的情况下测试和理解材料和爆炸事件，从而为计算模型和分析提供信息。

三个关键设施为此提供支持：

*   **pRad（质子射线照相术）：** 位于LANSCE，它使用质子和高速摄像机捕捉20-40张爆炸图像，从而能够详细研究材料在极端条件下的行为。它有助于确定材料的强度、可压缩性以及其断裂方式。
*   **DARHT（双轴射线照相流体动力学测试设施）：** 使用两个电子束产生X射线，从两个角度对爆炸进行成像，从而提供3D深度。与pRad相比，DARHT可以更广泛地观察更复杂的系统。
*   **Scorpius加速器：** NNSS未来的一个设施，它使用脉冲电子束捕获间隔为纳秒级的多个图像。它将允许进行与DARHT类似的实验，但使用亚临界量的钚。

这些洛斯阿拉莫斯的能力是美国国家核安全管理局（NNSA）综合设施中更大规模动态成像工作的一部分，包括桑迪亚的Cygnus和劳伦斯利弗莫尔的FXR。这些系统共同确保科学家能够理解武器的组成部分，并在没有核爆炸试验的情况下安全地管理国家库存。

文章还回答了以下问题：

*   库存管理在没有核爆炸试验的情况下维护美国核武器库存的安全性、安全性和可靠性。
*   亚临界核实验研究易裂变材料和高能炸药的行为，而不会引起自持核链式反应。

---

## 7. 十一音乐在此。

**原文标题**: Eleven Music Is Here

**原文链接**: [https://elevenlabs.io/blog/eleven-music-is-here](https://elevenlabs.io/blog/eleven-music-is-here)

Eleven v3 (Alpha)发布，号称“最具表现力的文本转语音模型”。标题“Eleven音乐来了”暗示新版本可能在音乐生成或TTS模型中的性能方面有所改进。

“表现力”的强调表明模型在通过语音传达情感和细微差别方面的关键改进。“Alpha”的标注表明该模型仍在开发中，可能会进行更改和改进。

---

## 8. 构建你自己的Lisp

**原文标题**: Build Your Own Lisp

**原文链接**: [https://www.buildyourownlisp.com/](https://www.buildyourownlisp.com/)

构建你自己的Lisp

---

## 9. SAML盾牌：适用于任何堆栈的即插即用保护

**原文标题**: SAML Shield: Drop-in protection that works for any stack

**原文链接**: [https://samlshield.com/](https://samlshield.com/)

Stytch 构建的 SAML Shield 提供了一个即插即用的开源解决方案，用于现代化和保护 SAML SSO 实施，以防御漏洞和攻击。它与任何语言或系统兼容，无需对现有身份提供商 (IdP) 进行任何更改。

SAML Shield 实时验证 SAML 断言，阻止恶意断言在到达应用程序代码之前。它可以防御源于 SAML 宽松规范和基于 XML 设计的各种攻击，包括 XML 签名包装、重放攻击和实体注入。该解决方案提供跨栈保护，解决影响 Python、Ruby、Node.js 和其他环境的 CVE。

部署选项包括将开源 Node.js 库直接嵌入到堆栈中，或者使用 Stytch 管理的代理服务。开源库允许在处理前检查断言，而托管选项则提供了一个简单的 API，用于在任何语言中集成和基于代理的安全，并提供自动更新。托管选项计划支持回溯测试。

总而言之，SAML Shield 旨在提供全面的 SAML 安全性，具有灵活性、易于集成性，并可防御不断演变的威胁，而无需考虑底层技术堆栈。

---

## 10. 无可奉告 (2010)

**原文标题**: No Comment (2010)

**原文链接**: [https://prog21.dadgum.com/57.html](https://prog21.dadgum.com/57.html)

詹姆斯·黑格的《谢绝评论》阐述了他关闭博客评论区的自觉决定，其原因是对于在线技术讨论中常见的负面情绪感到失望。他认为这些讨论，即使超越技术主题，也往往会演变成无益的批评和个人议程。

他用自己的经历来阐述这一点，包括最初在不了解全部背景的情况下批评代码，以及观察到对编程语言和新产品的肤浅批判。他将这种消极的在线环境与他在Flickr上的积极体验进行了对比，在Flickr上，社区专注于欣赏和建设性的反馈。

黑格将技术讨论中的负面情绪归因于一种本能反应，即想要立即识别并指出缺陷，这是具有工程思维的人的普遍倾向。 他发现这与面对面的讨论相比效率较低，因为面对面的讨论可以提供更多的背景和理解。

最终，黑格更喜欢避免在编程讨论中遇到的负面情绪，并且认为在专注于积极性和建设性反馈的社区（例如他在Flickr上找到的社区）中更有价值。 这种偏好是他决定关闭博客评论区的主要驱动因素。

---

## 11. FCC放弃使美国宽带快速且可负担的努力

**原文标题**: FCC Abandons Efforts to Make U.S. Broadband Fast and Affordable

**原文链接**: [https://www.techdirt.com/2025/08/05/trump-fcc-abandons-efforts-to-make-u-s-broadband-fast-and-affordable/](https://www.techdirt.com/2025/08/05/trump-fcc-abandons-efforts-to-make-u-s-broadband-fast-and-affordable/)

本文批评联邦通信委员会(FCC)放弃了确保美国民众获得快速且价格合理的宽带互联网接入的努力。联邦通信委员会在卡尔委员的领导下，通过援引最高法院的一项裁决来证明这一决定的合理性，该裁决限制了联邦机构广泛解释含糊不清的法律的能力。联邦通信委员会声称，它现在将严格遵守其决策中的“成文法文本”。作者认为，这是一种出于自身利益的举动，是特朗普政府时期政策的延续。作者认为，联邦通信委员会的行为仅仅是出于自身利益，没有考虑到美国公众的需求。

---

## 12. 科研欺诈已成“产业”，分析令人担忧

**原文标题**: Scientific fraud has become an 'industry,' alarming analysis finds

**原文链接**: [https://www.science.org/content/article/scientific-fraud-has-become-industry-alarming-analysis-finds](https://www.science.org/content/article/scientific-fraud-has-become-industry-alarming-analysis-finds)

科学欺诈已成“产业”，分析令人担忧

---

## 13. 使用本地处理的AI监控您的安全摄像头

**原文标题**: Monitor your security cameras with locally processed AI

**原文链接**: [https://frigate.video/](https://frigate.video/)

Frigate是一款开源NVR（网络视频录像机）软件，它利用本地处理的AI对安全摄像头画面进行实时物体检测，通过将录像保存在用户网络内来确保隐私。它旨在减少传统NVR中常见的误报，这些误报通常依赖于简单的运动检测。 Frigate利用AI加速器分析录像，识别特定物体，如人和车辆，从而消除由阴影或风触发的无关警报。

该系统快速处理视频流，分析每一帧以寻找感兴趣的物体。用户可以通过定义区域来微调事件和警报，从而实现基于精确位置的通知。 Frigate通过MQTT与Home Assistant、OpenHab和NodeRed等家庭自动化平台无缝集成，提供摄像头实体、传感器和开关，从而根据物体检测实现自动化响应和通知。

Frigate+提供访问为该软件量身定制的自定义模型。用户评价强调了Frigate的定制性、快速物体检测以及与Home Assistant的集成，使其成为一个完整的、本地控制的安全摄像头系统。用户称赞其减少误报、消除云依赖以及出色的支持。

---

## 14. 美国海岸警卫队“泰坦”号潜水器事故报告

**原文标题**: US Coast Guard Report on Titan Submersible

**原文链接**: [https://www.news.uscg.mil/Press-Releases/Article/4265651/coast-guard-marine-board-of-investigation-releases-report-on-titan-submersible/](https://www.news.uscg.mil/Press-Releases/Article/4265651/coast-guard-marine-board-of-investigation-releases-report-on-titan-submersible/)

美国海岸警卫队海事调查委员会(MBI)发布了关于“泰坦”号潜水器内爆的报告，该内爆发生在2023年6月前往泰坦尼克号残骸探险期间，导致船上五人全部遇难。该报告详细说明了MBI的调查结果，并提出了旨在防止未来发生类似悲剧的安全建议。

虽然内爆的具体原因没有明确说明，但该报告可能强调了促成因素，例如“泰坦”号的实验性设计、缺乏全面的测试和认证以及监管监督不足。该报告可能详细审查了海洋之门的安全性文化和导致致命潜水的决策过程。

MBI的调查包括收集证据、进行访谈和分析回收的碎片。该报告的安全建议可能涉及加强对潜水器运营的监管和监督、提高潜水器设计和建造的安全标准，以及改进船员培训和应急准备程序的需求。

最终，该报告旨在了解导致“泰坦”号失事的各种情况，并旨在提高未来潜水器探险的安全性。完整报告将转交给海岸警卫队司令审查，并决定是否采取进一步行动。这项调查强调了深海探险中固有的风险以及严格安全协议的关键重要性。

---

## 15. AI并未使工程师的生产力提高十倍。

**原文标题**: AI is not making engineers 10x as productive

**原文链接**: [https://colton.dev/blog/curing-your-ai-10x-engineer-imposter-syndrome/](https://colton.dev/blog/curing-your-ai-10x-engineer-imposter-syndrome/)

本文探讨了许多工程师对人工智能声称能将工程师生产力提高 10-100 倍的焦虑。作者是一位持怀疑态度的工程师，他深入研究了 Claude Code、Cursor 和 Zed 等 AI 编码工具，但发现 AI 编码虽然对样板代码和一次性脚本有用，但并未带来承诺的生产力提升。它在代码库标准方面表现不佳，会虚构库，并且需要大量的人工监督。

作者认为，10 倍生产力背后的数学原理并不成立，因为它忽略了软件工程中的人为流程，如代码审查、产品构思和质量保证。这些流程无法以相同的速度加快。此外，即使代码编写速度更快，编译和修复人工智能生成的错误等瓶颈也会限制整体生产力的提升。

作者认为，声称 10 倍生产力通常来自善意的误测、对人工智能成功抱有既得利益的人，或者试图在工程师中制造不稳定感的上司。他们将感知到的生产力提升归因于人工智能的新颖性、蜜月期和偏见。虽然人工智能可能会将某些任务改进 20-50%，但这并不会转化为整体生产力提高 10 倍。作者强调了认识到推动人工智能炒作的动机的重要性，并提醒读者，首席执行官并非总是公正的来源。

---

## 16. 受够了——我放弃了越来越差的谷歌搜索，转用Kagi。

**原文标题**: Enough is enough–I dumped Google's worsening search for Kagi

**原文链接**: [https://arstechnica.com/gadgets/2025/08/enough-is-enough-i-dumped-googles-worsening-search-for-kagi/](https://arstechnica.com/gadgets/2025/08/enough-is-enough-i-dumped-googles-worsening-search-for-kagi/)

作者厌倦了谷歌强制的AI摘要和整体搜索质量的下降，转而选择Kagi作为替代方案。他们批评谷歌的“垃圾化”和强制的AI集成，哀叹传统搜索结果的丧失。

Kagi是一个以用户为中心、付费的搜索引擎，成立于2018年，优先考虑有用的结果，而非AI生成的内容和广告。与用户是产品的谷歌不同，Kagi采用订阅模式。作者每年支付约100美元进行无限次搜索，并认为这笔费用值得，以避免谷歌的侵入式AI和有偏见的结果。

文章强调了Kagi的优势：它不依赖风险投资，提供用于匿名搜索的Privacy Pass选项，并提供卓越的定制性。主要功能包括优先或排除搜索结果中的网站、改进的图像搜索体验、可定制的小部件和镜头，以及自定义CSS注入和URL重写的选项。虽然承认DuckDuckGo、Bing和Brave等替代方案，但作者发现Kagi的方法最具吸引力。作者还提到了Kagi地图和视频搜索工具、逐字模式、自定义搜索运算符和API访问。

---

## 17. 台积电称员工试图窃取iPhone 18芯片工艺的商业机密

**原文标题**: TSMC says employees tried to steal trade secrets on iPhone 18 chip process

**原文链接**: [https://9to5mac.com/2025/08/05/tsmc-says-employees-tried-to-steal-trade-secrets-on-iphone-18-chip-process/](https://9to5mac.com/2025/08/05/tsmc-says-employees-tried-to-steal-trade-secrets-on-iphone-18-chip-process/)

多名前台积电员工被指控试图窃取与该公司2纳米芯片开发和生产工艺相关的商业机密，该工艺预计将用于苹果iPhone 18系列的A20芯片。台积电通过例行监控检测到“未经授权的活动”，并采取纪律处分，解雇了这些员工并启动了法律诉讼。刑事起诉也可能发生。

该盗窃企图是通过一名员工的“异常访问模式”发现的。虽然具体信息尚不清楚，但它可能与一般的2纳米工艺有关，而不是关于苹果A20芯片的具体细节。由于国内开发的先进技术涉及国家安全，台湾政府正在认真对待此事。台积电表示，将依法追究到底。苹果通常会率先使用台积电最先进的芯片工艺。

---

## 18. SimpleW – .NET Core Web服务器库

**原文标题**: SimpleW – Web Server Library .NET Core

**原文链接**: [https://github.com/stratdev3/SimpleW](https://github.com/stratdev3/SimpleW)

SimpleW 是一个轻量级的 .NET Core Web 服务器库，旨在简化 Web 应用程序开发。它提供以下几个关键功能：

*   **路由:** 处理请求路由到适当的处理程序。
*   **API REST:** 支持使用 Controller/Method 架构和自动 JSON 序列化/反序列化创建 RESTful API。
*   **Json Web Token (JWT):** 提供使用 JWT 进行安全身份验证和授权的功能。
*   **Websocket:** 支持使用 WebSockets 实现服务器和客户端之间的实时通信。
*   **Server Sent Events (SSE):** 支持使用服务器发送事件将更新从服务器推送到客户端。
*   **静态文件:** 提供静态内容，如 HTML、CSS 和 JavaScript 文件。
*   **OpenTelemetry:** 集成 OpenTelemetry 用于监控和追踪。

详细文档可在 stratdev3.github.io 上找到，更新日志记录了更新。该库在 MIT 许可证下获得许可，欢迎贡献，尤其是错误报告。

---

## 19. 为什么GitHub的UI越来越慢？

**原文标题**: Why is GitHub UI getting slower?

**原文链接**: [https://yoyo-code.com/why-is-github-ui-getting-so-much-slower/](https://yoyo-code.com/why-is-github-ui-getting-so-much-slower/)

本文批评了GitHub UI最近的性能下降。作者指出，曾经很快的操作现在明显变慢了，并以在拉取请求的“Conversation”和“Files changed”标签之间切换为例，耗时超过5秒。他们强调，讽刺的是，使用GitHub的Turbo驱动的客户端路由，本意是为了优化性能，但实际上比在新标签页中打开相同的链接并进行整页重新加载还要慢。

作者认为，客户端的后处理是瓶颈，花费的时间比服务器的HTML交付还要长。他们还对添加加载条表示不满，认为解决性能问题比在视觉上掩盖它们更好。

其他抱怨包括diff视图中的性能问题，这可能是由于渲染大量DOM节点（可能数万个）造成的。调整开发者工具窗口大小会导致整个窗口冻结，进一步阻碍性能调试。

作者质疑GitHub的“大规模平台协作”路线图是否解决了这些性能问题，并对当前的状态表示沮丧，尤其是在处理多个PR和问题时。最后，他们链接到与JavaScript性能优化相关的资源，希望已识别的问题能够得到解决，性能能够得到改善。

---

## 20. Proxmox VE 9.0 发布，基于 Debian 13

**原文标题**: Proxmox Virtual Environment 9.0 with Debian 13 released

**原文链接**: [https://www.proxmox.com/en/about/company-details/press-releases/proxmox-virtual-environment-9-0](https://www.proxmox.com/en/about/company-details/press-releases/proxmox-virtual-environment-9-0)

Proxmox Server Solutions GmbH 发布 Proxmox 虚拟环境 (VE) 9.0，基于 Debian 13 "Trixie" 构建。此版本包含多项针对企业用户的关键增强功能，包括 Linux Kernel 6.14.8-2、QEMU 10.0.2、LXC 6.0.4、Ceph Squid 19.2.3 和 ZFS 2.3.3。一个主要的亮点是引入了对厚配置 LVM 共享存储的快照，通过卷链为基于 iSCSI 或 FC 的 SAN 启用快照功能。

该版本还引入了一个新的“Fabrics”功能，用于软件定义网络 (SDN)，简化了复杂路由网络的配置，具有节点之间的多条路径和自动故障转移等功能。Proxmox VE 9.0 支持 OpenFabric 和 OSPF 路由协议。

此外，还引入了 HA 资源亲和性规则，以便更好地控制 HA 集群中的资源放置，允许管理员将相互依赖的资源放在一起，或确保关键应用程序在不同的节点上运行以实现冗余。移动界面已使用基于 Rust 的 Yew 框架重新设计，可访问服务概览和基本管理功能。

Proxmox VE 9.0 可以 ISO 形式下载，并提供从 Proxmox VE 8 的无缝升级路径。它是免费的，并根据 GNU AGPL v3 许可证开源，同时提供企业支持订阅。

---

## 21. Apache ECharts 6

**原文标题**: Apache ECharts 6

**原文链接**: [https://echarts.apache.org/handbook/en/basics/release-note/v6-feature/](https://echarts.apache.org/handbook/en/basics/release-note/v6-feature/)

Apache ECharts 6.0 发布，标志着这款流行的开源数据可视化库迎来了重大升级。此版本专注于增强视觉呈现，扩展数据表达能力，并为开发者提供更大的组合自由度。

主要特性包括：

*   **改进的视觉效果：** 全新的默认主题带来专业外观，动态主题切换适用于多主题场景，以及自动暗黑模式支持。
*   **扩展的数据表达：** 新增图表类型，如用于关系可视化的弦图和用于处理重叠数据点的蜂群图。同时还添加了散点抖动、断轴和增强的股票交易图表。
*   **组合自由度：** 革命性的矩阵坐标系用于组合图表类型和组件，增强的自定义系列支持 npm 发布和动态注册以实现代码重用，以及新的自定义图表，如小提琴图、等值线图和范围图。轴标签优化可防止溢出和重叠。

这些升级旨在使 ECharts 更加强大和灵活，使开发人员能够轻松创建更复杂和更具视觉吸引力的数据可视化效果。该版本还包括升级指南和详细的更新日志，供从先前版本迁移的用户参考。

---

## 22. Show HN: Stagewise (YC S25) – 现有代码库的前端编码代理

**原文标题**: Show HN: Stagewise (YC S25) – Front end coding agent for existing codebases

**原文链接**: [https://github.com/stagewise-io/stagewise](https://github.com/stagewise-io/stagewise)

Stagewise：修改生产环境前端代码的编码助手。它允许开发者通过自然语言和可视化元素选择来指定所需的更改，无需手动提供元素信息和文件路径。Stagewise 旨在利用实时、浏览器驱动的上下文来简化前端开发。

主要功能包括开箱即用、可定制插件、开源、框架兼容性，以及通过开放的代理接口使用 Stagewise 专用代理或其他兼容代理的选项。

入门方法包括在开发模式下运行目标 Web 应用程序，然后从根目录通过 `npx stagewise` 或 `pnpm dlx stagewise` 启动 Stagewise。CLI 应用程序将引导用户完成帐户设置。

该项目与一系列代理兼容，包括 Stagewise 自己的代理、Cursor、GitHub Copilot、Windsurf、Cline、Roo Code、Kilo Code 和 Trae。

Stagewise 基于 AGPLv3 许可，对于 AGPLv3 未涵盖的用例，提供商业许可选项。鼓励通过 GitHub 和 Discord 频道进行贡献，并且文档中提供了开发指南。

---

## 23. PHP 8.5新增管道运算符

**原文标题**: PHP 8.5 adds pipe operator

**原文链接**: [https://thephp.foundation/blog/2025/07/11/php-85-adds-pipe-operator/](https://thephp.foundation/blog/2025/07/11/php-85-adds-pipe-operator/)

PHP 8.5 新增管道操作符（`|>`）

本文宣布 PHP 8.5 新增了管道操作符（`|>`），这是 PHP 社区长期以来一直寻求的功能。管道操作符获取其左侧的值，并将其作为唯一参数传递给其右侧的函数，从而以更具可读性和简洁的方式实现链式操作。作者以数组操作为例进行了说明。

文章追溯了该操作符的历史，指出它存在于 F# 和 Elixir 等语言中，以及之前为 PHP 提出的实现方案，包括基于 Hack/HHVM 方法的方案。目前的实现更简单、更标准，避免了之前方案的复杂性。

作者强调了管道操作符的优点，展示了它将复杂逻辑凝练为单个表达式的能力，使其适合在 `match()` 块等上下文中使用。作者还讨论了将其与其他功能结合的可能性，例如部分函数应用（正在重新考虑）和函数组合（计划在未来实现），以及 `null` 处理。

此新增功能使 PHP 更接近 Kotlin 和 C# 的扩展函数等功能。作者对 PHP 的未来发展表示乐观，并感谢 PHP 基金会团队在实施管道操作符方面的帮助。文章最后鼓励读者支持 PHP 的持续发展。

---

## 24. 重命名此文件会改变其功能 [视频]

**原文标题**: Renaming this file changes what it does [video]

**原文链接**: [https://www.youtube.com/watch?v=o7qx-wgl3jo](https://www.youtube.com/watch?v=o7qx-wgl3jo)

这个名为“重命名此文件会改变它的作用”的YouTube视频，很可能探讨文件扩展名的概念，以及它们如何影响计算机解释和处理文件的方式。

描述中可见的内容，“YouTube关于新闻版权联系我们创作者广告开发者条款隐私权政策与安全YouTube 的运作方式测试新功能NFL Sunday Ticket© 2025 Google LLC”，是标准的YouTube页脚文本，与视频的实际内容无关。它提到了新闻、版权、联系信息、创作者、广告、开发者、条款、隐私、安全、YouTube的运作方式、新功能测试、NFL Sunday Ticket和版权年份。

因此，总结侧重于视频可能的内容，鉴于标题：该视频演示了更改文件扩展名（例如，从.txt到.exe）如何显著改变其功能。它可能解释了文件扩展名告诉操作系统使用哪个程序来打开和解释文件。通过更改扩展名，您可能会欺骗系统将该文件视为完全不同的东西，可能导致意外甚至恶意行为。该视频的目的可能是教育观众文件扩展名的重要性以及操纵它们可能带来的安全风险。

---

## 25. 拯救早产儿的嘉年华游乐项目 (2016)

**原文标题**: A Carnival Attraction That Saved Premature Babies (2016)

**原文链接**: [https://www.smithsonianmag.com/history/man-who-pretended-be-doctor-ran-worlds-fair-attraction-saved-lives-thousands-premature-babies-180960200/](https://www.smithsonianmag.com/history/man-who-pretended-be-doctor-ran-worlds-fair-attraction-saved-lives-thousands-premature-babies-180960200/)

本文讲述了马丁·库尼的故事，他在20世纪初经营婴儿保育箱展览，尤其是在康尼岛，他是一个备受争议的人物。当时，主流医学界认为早产儿是“弱者”，而库尼通过收取展览门票来资助保育箱，为他们提供救生护理。护士和医生照顾这些婴儿，吸引了成千上万的游客，库尼也因此赢得了绝望的父母的赞誉，被誉为救星。

然而，马戏团式的展览环境使他成为批评的对象，被指责剥削和危害婴儿。后来人们发现，库尼并不是一名合格的医生，可能虚报了他的教育背景和资历。尽管存在争议且缺乏正式资格，库尼的工作还是获得了包括朱利叶斯·赫斯医生等一些著名儿科医生的尊重。这些医生认可库尼设施提供的高水平护理。

库尼的设施照顾来自各种背景的婴儿，并不向父母收取费用。在他的职业生涯中，他声称救活了大约8000名入院婴儿中的6500名，因为这一功绩，他被以前的病人铭记为英雄。尽管围绕他的方法存在伦理和职业问题，但一些医学专业人士认为库尼是美国新生儿医学的重要人物，帮助普及了保育箱的使用，并改善了对早产儿的护理。

---

## 26. 谷歌同意在电力需求高峰期暂停人工智能工作负载

**原文标题**: Google agrees to pause AI workloads when power demand spikes

**原文链接**: [https://www.theregister.com/2025/08/04/google_ai_datacenter_grid/](https://www.theregister.com/2025/08/04/google_ai_datacenter_grid/)

为应对日益增长的对数据中心能源消耗的担忧，谷歌已同意在电力需求高峰期暂停非必要的AI工作负载，以保护电网。这项与印第安纳密歇根电力公司（I&M）和田纳西河谷管理局（TVA）达成的协议，允许这些电力公司要求谷歌通过重新安排工作负载或限制非紧急任务来降低其用电量，在电力需求高峰期或电网中断期间，谷歌称这一过程为“需求响应”。

这种策略类似于谷歌已经管理其他非必要工作负载（如YouTube视频处理）的方式，即将其转移到有可用电力的数据中心。谷歌认为，这种灵活性可以通过缓解公用事业公司对电网压力的担忧来加速数据中心的互联互通。

这项声明是在预计将对电网造成压力的热浪中发布的，因为AI模型的训练和运行会消耗大量电力。虽然这种方法可以应用于某些AI工作负载，但谷歌承认其与诸如搜索、地图及其云业务等基本服务不兼容。此外，他们无法暂停其云客户的AI作业。

这项需求响应策略是谷歌遏制电力需求的更广泛努力的一部分，其中包括对服务器（在91天内约140亿美元）以及地热、太阳能、风能、水力发电和核能等替代能源的巨额投资，并计划采用小型模块化反应堆。

---

## 27. DOS 下的多个硬盘

**原文标题**: More than two hard disks in DOS

**原文链接**: [https://www.os2museum.com/wp/more-than-two-hard-disks-in-dos/](https://www.os2museum.com/wp/more-than-two-hard-disks-in-dos/)

本文研究了 DOS 5.0 之前版本中的一个错误，该错误导致系统在存在两个以上的硬盘时挂起。作者 Michal Necasek 解释说，虽然 INT 13h 接口在技术上支持两个以上的磁盘，但早期 PC BIOS 实现和驱动器尺寸的物理限制使其并不常见，因此该错误未被发现。

像 Compaq 和 Adaptec 这样推出了能够支持两个以上硬盘的公司的公司，开发了自定义驱动程序（EXTDISK.SYS 和 ASPIDISK.SYS）等解决方法来绕过 DOS 的限制。该错误本身存在于 MSINIT.ASM 中，DOS 在那里未能验证磁盘数量，并陷入循环尝试初始化 BPB。

DOS 5.0 解决了这个问题。然而，本文揭示了 IBM 实际上更早地在 IBM DOS 4.0 中通过纠错服务软盘（CSD）#UR29015 修复了该错误，该软盘于 1989 年 9 月发布，允许 DOS 4.0 支持多达七个固定磁盘。这解释了为什么一些后来的 DOS 4.0 版本，如日文 IBM DOS J4.05/V，能够处理两个以上的驱动器，以及为什么最早的 MS-DOS 5.0 测试版没有表现出该错误。文章总结说，IBM 很可能在为 PS/2 开发自己的 SCSI 适配器时在内部发现了该错误，并且该修复程序是从那里合并到 MS-DOS 5.0 中的。SCSI HBA 供应商还提供了 BIOS 选项来启用或禁用对两个以上驱动器的支持，以应对 DOS 的限制。

---

## 28. 你能屏蔽它吗？一个简单的广告拦截测试器

**原文标题**: Can you block it? A simple Ad Block Tester

**原文链接**: [https://canyoublockit.com/](https://canyoublockit.com/)

本文介绍“你能拦截吗 (Can You Block It)”，该工具旨在测试广告拦截器的有效性。它允许用户确定他们的广告拦截器成功拦截了哪些广告格式，以及哪些广告格式漏网了。该工具的工作原理是将用户引导至包含不同类型广告的页面。如果广告拦截器运行正常，用户应该看不到这些广告。

该网站提供三个级别的测试：

*   **简单测试：** 使用自托管广告进行基本评估。
*   **极限测试：** 包含来自热门广告网络的各种广告格式，以提供更全面的测试。
*   **高级测试：** 一系列单独的页面，旨在诊断针对特定广告格式的拦截性能。

该工具支持对各种流行的广告拦截器进行测试，例如 AdBlock、AdBlock Plus、uBlock Origin、AdGuard 等，针对包括网页横幅广告、原生广告、弹出式广告和页面内推送广告等来自热门广告网络的各种广告格式。其目的是帮助用户了解和优化他们的广告拦截设置，以获得更干净的浏览体验。

---

## 29. 奥美赛显示抗衰老效果，试验逆转生物年龄3.1年

**原文标题**: Ozempic Shows Anti-Aging Effects in Trial, Reversing Biological Age by 3.1 Years

**原文链接**: [https://trial.medpath.com/news/5c43f09ebb6d0f8e/ozempic-shows-anti-aging-effects-in-first-clinical-trial-reversing-biological-age-by-3-1-years](https://trial.medpath.com/news/5c43f09ebb6d0f8e/ozempic-shows-anti-aging-effects-in-first-clinical-trial-reversing-biological-age-by-3-1-years)

一项最新临床试验显示，糖尿病药物Ozempic（司美格鲁肽）具有抗衰老作用，在治疗32周后，生物年龄平均逆转3.1岁。这项由Varun Dwaraka领导的研究，招募了108名患有HIV相关脂肪代谢障碍的参与者，并利用表观遗传时钟，基于DNA甲基化模式来测量生物年龄。接受Ozempic注射的参与者，与安慰剂组相比，生物年龄显著降低。

抗衰老益处并非在全身一致，炎症系统和大脑（近5年）的改善最为显著，心脏和肾脏也受益匪浅。研究人员认为，这些效应归因于司美格鲁肽能够减少器官周围有害脂肪的积累，并对抗低度炎症，而这两者都是表观遗传衰老的关键驱动因素。Randy Seeley认为，益处也源于整体代谢健康的改善。

尽管研究人群患有特定疾病，但研究人员认为，由于共享的生物途径，研究结果可能推广到普通人群。尽管结果令人鼓舞，Dwaraka仍呼吁谨慎对待，不要过早地将司美格鲁肽单独作为抗衰老疗法开具处方。这项研究突显了重新利用现有药物解决与年龄相关问题的潜力，并将司美格鲁肽定位为治疗糖尿病和肥胖症以外的各种疾病（包括心血管疾病、成瘾和痴呆症）的有希望的候选药物。

---

## 30. 缺乏意图是阅读LLM生成文本令人疲惫的原因。

**原文标题**: Lack of intent is what makes reading LLM-generated text exhausting

**原文链接**: [https://lambdaland.org/posts/2025-08-04_artifical_inanity/](https://lambdaland.org/posts/2025-08-04_artifical_inanity/)

阅读大型语言模型(LLM)生成的文本令人疲惫且不悦，原因在于它缺乏真诚的人类意图。作者回忆了一段努力理解LLM生成的设计文档的个人经历，并将这种困难归因于文本中充斥着“无用信息”和潜在的“臆造胡言”。

作者认为，在阅读人类撰写的文本时，人们会自然而然地假设每个词和句子都是经过深思熟虑的选择，旨在传达意义。然而，这种假设在LLM生成的文本中失效了，因为其中的句子可能是概率抽样的结果，而非有意识的意图。这迫使读者不断质疑短语的目的，导致精神疲劳。

核心论点是，文本背后缺乏人类意图——人类意志和关怀——是其令人反感的原因。即使有人同意作者意图与文本意义无关的观点，但作者倾注心血和关怀的存在，也赋予了文本比机器生成文本更大的意义。作者承认LLM在解决复杂问题方面的实用性，但强调它们无法取代人类价值，并且容易被滥用，例如学术作弊和过度依赖机器进行推理。最终，这篇文章捍卫了人类意图在沟通中的重要性，以及缺乏意图所导致的退化。

---

## 31. GitHub Pull Request 出现故障

**原文标题**: GitHub pull requests are down

**原文链接**: [https://github.com/github/site-policy/pull/582](https://github.com/github/site-policy/pull/582)

该GitHub Issue讨论串讨论了GitHub隐私声明的更新，特别是关于在面向企业营销产品的网页（例如，resources.github.com）上引入非必要Cookie。 这些Cookie旨在提供分析，以改善网站体验并为企业用户个性化内容/广告。 Github.com本身将继续照常运行。

这些更新于2022年8月2日宣布，经过30天的通知和评论期后，更改于2022年9月1日生效。 GitHub通过澄清以下几点回应了反馈：

*   **DNT和浏览器扩展：**GitHub将遵守“请勿追踪”（DNT）信号，并为用户提供禁用非必要Cookie的设置。
*   **企业用户体验：** 此更改仅影响企业营销页面，而不影响企业用户帐户。 用户可以在这些页面上管理Cookie偏好设置。
*   **文体变更：** 为了保持一致性，已将“Personal Data”的大写形式更改为“personal data”，因为它不是服务条款中定义的术语。

评论揭示了对这些更改的隐私影响的担忧，特别是关于DNT处理方式的转变，“个人数据”的定义以及对公司数据收集行为的普遍不信任。 一些用户表达了失望，并寻求GitHub的替代方案。 其他人则质疑先前避免使用非必要Cookie的承诺的含义。 总的来说，讨论反映了用户在GitHub不断发展的商业模式背景下对隐私和数据使用的焦虑。

---

## 32. 青铜与钢铁时代

**原文标题**: The Age of Bronze and Steel

**原文链接**: [https://blog.zarfhome.com/2025/08/age-of-bronze-and-steel](https://blog.zarfhome.com/2025/08/age-of-bronze-and-steel)

安德鲁·普洛特金的博文《青铜与钢铁的时代》讲述了一种3D打印金属工艺——粘结剂喷射钢与青铜渗透——已经 фактически исчезла 的故事。他是在看到一条推文感叹该工艺停产后，才开始撰写此文的。

这项技术最初由ExOne开发，于2021年被Desktop Metal收购，随后Desktop Metal大幅提高了价格。之后，Desktop Metal试图被收购，最终在与Stratasys的交易失败后被Nano Dimensions收购。不久之后，Desktop Metal申请破产，导致其资产被拆解和出售。

这种曾经能够制造尺寸稳定且复杂的金属物体的青铜-钢铁打印工艺不再可行。它的关键优势在于青铜渗透步骤，它可以防止烧结过程中出现不均匀的收缩，但它需要专业的知识和经验丰富的人员，而这些人中的许多人已经退休或被解雇。

普洛特金将这种情况与Embracer Group在游戏行业的收购狂潮进行了类比，突出了技术、工作、公司，甚至生活方式的脆弱性。这篇文章是对不可持续的商业行为的后果以及看似已确立的实体消失的可能性的一个警示故事。

---

## 33. 我们如何将 JSON.stringify 的速度提高两倍以上

**原文标题**: How we made JSON.stringify more than twice as fast

**原文链接**: [https://v8.dev/blog/json-stringify](https://v8.dev/blog/json-stringify)

V8 的 JSON.stringify 显著优化，速度提升 2 倍以上，主要策略包括：

*   **无副作用快速通道：** 一种新的专用序列化器处理保证不会触发副作用（如自定义 `.toJSON()` 方法或垃圾回收）的对象，绕过较慢的检查并使用迭代方法来避免堆栈溢出。
*   **字符串表示处理：** 序列化器被模板化，以分别处理单字节 (ASCII) 和双字节字符串，针对每种类型进行优化并高效地在它们之间转换。
*   **SIMD 优化字符串序列化：** 使用 SIMD 指令处理长字符串，并使用 SWAR 技术处理短字符串，以加速搜索需要转义的字符。
*   **快速通道优化：** 如果先前序列化对象的隐藏类密钥简单（没有 Symbols、可枚举且不需要转义），则将其标记为“fast-json-iterable”，从而可以更快地序列化类似对象。此优化也用于 JSON.parse。
*   **更快的 Double-to-String 算法：** 使用 Dragonbox 替换 Grisu3 算法，以加快数字到字符串的转换速度。
*   **优化临时缓冲区：** 从单个连续缓冲区切换到使用 V8 的 Zone 内存的分段缓冲区，从而消除昂贵的重新分配和复制操作。

当序列化不带替换函数、空格参数、索引属性或复杂字符串类型的纯数据对象和数组时，这些优化效果最佳。这些改进在 V8 版本 13.8 (Chrome 138) 中可用，可提高 API 响应和缓存等常见 Web 操作的性能。

---

## 34. Qwen-Image：原生文本渲染

**原文标题**: Qwen-Image: Crafting with native text rendering

**原文链接**: [https://qwenlm.github.io/blog/qwen-image/](https://qwenlm.github.io/blog/qwen-image/)

Qwen-Image：全新200亿参数MMDiT图像基础模型，擅长复杂文本渲染和精准图像编辑。其主要特性包括：卓越的多语言文本渲染能力、保持真实感和语义一致性的图像编辑能力，以及在生成和编辑任务中强大的跨基准性能。

该模型的文本渲染能力通过中英文示例展示，证明了其在渲染多行布局、段落级语义、精细细节，甚至图像中小物体上的手写文本方面的准确性。该模型可以准确地在海报、PPT幻灯片和其他格式上生成文本，并准确地再现商店招牌、书籍标题、电影海报，甚至不同语言的手写段落。

除了文本，Qwen-Image还支持广泛的艺术风格，用于通用图像生成，并提供多样化的图像编辑功能，包括风格迁移、物体操作和细节增强。

Qwen-Image在GenEval、DPG、OneIG-Bench、GEdit、ImgEdit、GSO、LongText-Bench、ChineseWord和TextCraft等基准测试中均优于现有模型，突显了其卓越的文本渲染精度和广泛的通用能力。此次发布旨在降低视觉内容创作的门槛，并促进开放、协作的生成式人工智能生态系统。

---

## 35. 葡萄牙法院命令维基百科审查文章并提供用户数据

**原文标题**: Wikipedia ordered by Portuguese courts to censor articles and provide user data

**原文链接**: [https://en.wikipedia.org/wiki/Wikipedia:Village_pump_(WMF)](https://en.wikipedia.org/wiki/Wikipedia:Village_pump_(WMF))

维基百科乡村水泵讨论：维基媒体基金会（WMF）在吸引年轻受众的新Roblox游戏中使用生成式人工智能

最初的帖子对WMF使用人工智能生成的图像作为游戏封面表示担忧，认为其优先考虑成本削减而非质量和环境责任。用户对此表示失望，特别是考虑到WMF对可持续发展的明确承诺以及之前在文章摘要中使用人工智能的负面公关。

虽然有些人批评使用人工智能，但另一些人则为WMF吸引年轻群体的努力辩护，认为这对于维基百科的未来至关重要。他们承认，尝试新的媒体形式是必要的，即使这些形式并不吸引现有社区。

讨论还突出了关于WMF更广泛的人工智能战略以及社区如何有效提供反馈并影响决策的持续辩论。一些人建议关注人工智能计划背后的流程，而不是对个别事件做出反应，并参与未来受众团队等倡议。

未来受众团队的代表澄清说，Roblox游戏的封面图像是由人类设计师创建的，而不是人工智能。他们还解释说，人工智能被用于创建社交媒体短视频的初始草稿，然后由人类审查和编辑。这种人工智能的使用有助于减少时间和成本。

讨论的结论是，提醒人们优先考虑真正值得为之奋斗的问题，以及与年轻一代建立联系以向他们介绍维基百科的重要性。

---

## 36. 克里斯·柯里接受《你的电脑》杂志采访（1981年）

**原文标题**: Chris Curry interviewed by Your Computer magazine (1981)

**原文链接**: [https://computeradsfromthepast.substack.com/p/your-computer-interviewed-chris-curry](https://computeradsfromthepast.substack.com/p/your-computer-interviewed-chris-curry)

无法访问文章链接。

---

## 37. 哪里寻找灵感

**原文标题**: Where to find ideas

**原文链接**: [https://howtogrow.substack.com/p/where-to-find-ideas](https://howtogrow.substack.com/p/where-to-find-ideas)

无法访问文章链接。

---

## 38. Thingino：IP摄像机的开源固件

**原文标题**: Thingino: Open-Source Firmware for IP Cameras

**原文链接**: [https://thingino.com/](https://thingino.com/)

Thingino：IP摄像头开源固件项目。该项目旨在提供一个可定制且可能比原厂固件更安全的替代方案。

Thingino兼容性的关键在于硬件匹配。具体的摄像头型号、SoC（片上系统）、图像传感器、Wi-Fi模块和闪存芯片大小必须与列出的受支持配置相符。项目开发者强调，即使在同一型号系列中，制造商有时也会更改内部组件，因此硬件验证至关重要。

该文档列出了受支持的室内、球泡和室外IP摄像头，以及IPC（IP摄像头）模块、网络摄像头和开发板。对于每个受支持的设备，都详细说明了具体的硬件组件。此外，该文档指出，某些摄像头可能提供安装说明。

该项目还承认“有条件支持的硬件”。某些品牌实施安全启动，需要使用存储在SoC的OTP区域中的特定密钥对固件进行数字签名。在没有正确签名的情况下更换固件可能会导致摄像头无法使用。

最后，该文档提到了“神秘盒子硬件”，这些硬件有时可能被错误标记或包含不受支持的ARM处理器。它还列出了“潜在支持的摄像头”（那些被认为具有君正SoC但缺乏验证样本的摄像头）。该文档明确指出，不支持使用Zeratul平台的电池供电摄像头，并且这是一个非商业项目，欢迎贡献。

---

## 39. 白宫命令美国国家航空航天局销毁重要卫星

**原文标题**: White House Orders NASA to Destroy Important Satellite

**原文链接**: [https://futurism.com/white-house-orders-nasa-destroy-important-satellite](https://futurism.com/white-house-orders-nasa-destroy-important-satellite)

据报道，特朗普政府已下令美国国家航空航天局制定计划，终止两项以气候变化为重点的卫星任务——轨道碳观测卫星。这些卫星收集关于二氧化碳分布的关键数据，影响石油、天然气和农业等领域。这些观测站，一个位于国际空间站，另一个是独立卫星，提供高质量、广泛使用的信息，预计还可以运行多年。

有猜测认为，此举与特朗普总统的气候变化否认论以及之前削减美国国家航空航天局科学预算的企图相符。前美国国家航空航天局雇员证实，现任工作人员正在被要求制定终止计划。维持这些观测站的费用相对较少，每年仅需1500万美元。

拟议的2026财年预算对数十个太空任务构成了生存威胁，引发了愤怒和对美国失去太空领域领导地位的担忧。立法者提出了维持当前资金水平的预算提案，拒绝大幅削减美国国家航空航天局的科学预算，否则将终止许多任务。

批评人士认为，结束地球监测任务是一种适得其反的反科学议程，具有潜在的非法影响，因为它推翻了先前分配的预算，并削弱了预测和应对气候灾害的能力。

---

## 40. 我尝试在英语课上用ChatGPT代替我自己。

**原文标题**: I tried to replace myself with ChatGPT in my English class

**原文链接**: [https://lithub.com/what-happened-when-i-tried-to-replace-myself-with-chatgpt-in-my-english-classroom/](https://lithub.com/what-happened-when-i-tried-to-replace-myself-with-chatgpt-in-my-english-classroom/)

弗吉尼亚大学英语教授皮尔斯·盖利在他的课堂上进行了一项实验，以探索生成式人工智能，特别是ChatGPT，在学生写作中的作用。盖利担心人工智能可能会取代人类的努力和批判性思维，因此允许他的72名学生在整个学期的写作作业中自由使用人工智能，旨在确定学习写作是否仍然有价值。

最初的调查显示，学生们对在英语课中使用人工智能的伦理问题感到不确定，尽管许多人承认将其用于各种任务，如头脑风暴、列提纲和编辑。学生们经常批评人工智能的写作“乏味”或“平淡”，并发现了常见的人工智能特征，如虚构的引用和过多的破折号，讽刺的是，这提高了他们的精读能力。

课堂上还探讨了对人工智能的不同看法，包括将人工智能视为“醉酒的助手”以及“人+人工智能半人马”超越独立人工智能系统的潜力。他们还考虑了一项研究，该研究表明，人工智能的辅助导致了更多“创造性的”（可出版的）故事，同时也创造了相似的叙事。

当学生们比较人工智能生成的论文题目时，实验达到了高潮，他们发现这些题目明显缺乏原创性，并且倾向于通用主题。这种认识引起了他们的共鸣，因为他们认识到人工智能的局限性以及产生平淡、统一内容的可能性。盖利强调，人工智能是在一个有偏见的数据集上训练的，该数据集可能包含特定的类型和观点，这会影响写作风格和主题。

---

## 41. 环保署拟取消70亿美元太阳能补助金

**原文标题**: EPA Moves to Cancel $7B in Grants for Solar Energy

**原文链接**: [https://www.nytimes.com/2025/08/05/climate/epa-cancels-solar-energy-grants.html](https://www.nytimes.com/2025/08/05/climate/epa-cancels-solar-energy-grants.html)

无法访问文章链接。

---

## 42. 三维线稿

**原文标题**: 3D Line Drawings

**原文链接**: [https://amritkwatra.com/experiments/3d-line-drawings](https://amritkwatra.com/experiments/3d-line-drawings)

Amritansh Kwatra 的这篇文章探讨了通过调整 3D 高斯溅射技术来创建 3D 线条图。该方法包括将 3D 高斯溅射中使用的原始照片替换为由 Chan 等人开发的基于 GAN 的方法生成的线条图，该方法保留了几何结构和语义信息。

Kwatra 证明，在运动结构重建 (SfM) 或 3D 高斯溅射训练之前替换图像会产生不同的结果。在 SfM 之前替换图像会产生更清晰的线条图，但可靠性较低。在训练之前替换它们会保留轻微的颜色伪影，但提供更高的稳定性和更快的迭代速度。

文章进一步研究了为线条图添加颜色，通过混合来自原始图像的低频颜色信息，创造出类似水彩的效果。作者还探索了拼接照片级真实感和风格化场景，以及创建拼贴场景，其中特定对象被渲染为线条图，背景为照片级真实感。

最后，作者研究了图像分辨率对训练时间和生成的线条图复杂性的影响，指出较低的分辨率导致更快的训练，并且仅捕获主要线条，而较高的分辨率则捕获更精细的细节。与照片级真实感场景相比，线条图场景往往需要更多的高斯溅射和更大的文件大小，这可能是因为溅射在建模笔划方面效率较低。

---

## 43. Show HN: 我花了六年时间做了一个奇葩的木制像素显示器

**原文标题**: Show HN: I spent 6 years building a ridiculous wooden pixel display

**原文链接**: [https://benholmen.com/blog/kilopixel/](https://benholmen.com/blog/kilopixel/)

这个 "Show HN" 帖子详细介绍了 Kilopixel 的六年构建之旅，这是一个通过网络界面控制的 40x25（1000 像素）木制显示器。作者受到非传统镜子和缓慢电子墨水屏的启发，旨在创造一件低效但具有互动性的艺术品。

该项目面临诸多挑战，包括寻找合适且经济实惠的像素材料（测试并拒绝了各种球体）、设计可靠的像素旋转机制以及构建稳定的网格。作者最终选择了在其木工车间制造的立方体木制像素。

一台数控机床控制像素旋转机制，移动一个“拨杆”来根据连接到 API 的 Raspberry Pi 的指令将每个像素旋转到正确的状态。驱动 API 的 Web 应用程序允许用户提交图像进行显示、对提交内容进行投票以及进行实时互动。还有具有生成图案和时钟的空闲模式。

Kilopixel 现在已上线，网址为 kilopx.com，并在 YouTube 上进行直播。作者已实施基本的滥用缓解措施，并乐于看到互联网如何与该项目互动。未来的计划包括可能将显示器的控制权交给其他人，或者将其用作视频通话的动态背景。作者鼓励提交内容和提供反馈。

---

## 44. Show HN: 我做了个基于文本的生日提醒应用

**原文标题**: Show HN: I built a text-based birthday reminder app

**原文链接**: [https://birthdays.app](https://birthdays.app)

这个“Show HN”帖子介绍了一个名为 birthdays.app 的新文本生日提醒应用。其核心功能是为即将到来的生日发送短信提醒。虽然帖子很简短，但关键信息是提供了一个直接通过短信发送生日提醒的服务。“Show HN”标签表明创建者正在寻求反馈，并向 Hacker News 社区展示他们的项目。描述的简洁性暗示该应用可能优先考虑用户友好的体验，以便管理和接收这些提醒。它迎合了那些喜欢基于文本的提醒，而不是应用程序通知或日历条目来记住生日的用户。

---

## 45. 气象卫星探测到515英里长的闪电

**原文标题**: Weather satellites detect 515-mile-long lightning flash

**原文链接**: [https://www.space.com/astronomy/earth/new-world-record-weather-satellites-detect-515-mile-long-lightning-flash](https://www.space.com/astronomy/earth/new-world-record-weather-satellites-detect-515-mile-long-lightning-flash)

2017年，一道破纪录的超长闪电，被称为“巨型闪电”，长达515英里，从德克萨斯州延伸至密苏里州，创造了新的闪电长度世界纪录。 这超过了之前的记录保持者38英里。“巨型闪电”被定义为长度超过62英里的闪电，非常罕见，仅占雷暴的不到1%。它们通常发生在持续至少14小时且覆盖面积相当于新泽西州大小的风暴中。

研究人员利用美国国家海洋和大气管理局GOES-16卫星（配备闪电绘图仪）的数据，确定了巨型闪电的长度。 与旧的地面无线电网络相比，使用配备闪电绘图仪的卫星大大改善了跟踪和测量这些极端闪电事件的过程。

研究人员仍在研究巨型闪电背后的机制，随着收集到更多高质量的闪电测量数据，他们预计会观察到更加极端的现象。

---

## 46. 2025年第二季度Backblaze硬盘统计

**原文标题**: Backblaze Drive Stats for Q2 2025

**原文链接**: [https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2025/](https://www.backblaze.com/blog/backblaze-drive-stats-for-q2-2025/)

2025年第二季度Backblaze硬盘统计报告分析了其数据中心超过321,000块硬盘的故障率。季度故障率从1.35%略微上升至1.42%，然后回落至1.36%，其中部分12TB和14TB的希捷和HGST型号的故障率显著下降。两款希捷型号（8TB和16TB）在本季度实现了零故障。

该报告还考察了终身故障率，指出总体比率稳定在1.30%。较小容量的硬盘（≤12TB）正在老化，许多硬盘的使用年限超过五年，并表现出令人印象深刻的性能，挑战了年龄与故障直接相关的观点。

报告的很大一部分集中在20TB+的硬盘（东芝、WDC和希捷）上，比较了其生命周期内的年化故障率(AFR)。24TB希捷硬盘最初显示出较高的故障率，可能因为它是新品。与14-16TB的硬盘池相比，20TB+的硬盘在早期阶段的表现似乎符合预期或略好。报告总结说，需要更多的时间和数据来确定更大容量硬盘的明确趋势，强调需要持续的监控和分析。

---

## 47. 伊利诺伊州禁止人工智能提供心理治疗

**原文标题**: Illinois Bans AI from Providing Therapy

**原文链接**: [https://gizmodo.com/illinois-bans-ai-from-providing-therapy-2000639042](https://gizmodo.com/illinois-bans-ai-from-providing-therapy-2000639042)

伊利诺伊州已禁止人工智能提供治疗或咨询服务，仅限其用于行政和支持角色。州长普利兹克签署了《心理资源健康与监督法案》，以保护患者免受医疗保健领域不受监管的人工智能使用。该法律禁止人工智能提供治疗、做出独立的治疗决策、在没有人工监督的情况下生成治疗计划或检测情绪。违规者将面临高达 10,000 美元的罚款。

特雷托部长强调了合格的人类专业人员在医疗保健领域的重要性。其他州也在解决人工智能在精神健康方面的问题。内华达州禁止在公立学校进行人工智能治疗，犹他州要求人工智能聊天机器人披露其人工智能状态、广告并限制数据使用。纽约将要求人工智能伴侣将有自杀倾向的用户引导至危机热线。

这些州的行为源于美国心理协会（APA）对人工智能治疗师风险的担忧，并援引了儿童因人工智能聊天机器人而受到伤害的诉讼，包括一起自杀事件。

---

## 48. Clojure Civitas – 发布 Clojure 思想与探索

**原文标题**: Clojure Civitas – Publish Clojure Ideas and Explorations

**原文链接**: [https://github.com/ClojureCivitas/clojurecivitas.github.io](https://github.com/ClojureCivitas/clojurecivitas.github.io)

Clojure Civitas 是一个用于分享 Clojure 想法和探索的平台，无需典型性的额外开销。它鼓励用户 fork 仓库，创建命名空间，以注释形式编写代码和笔记，并提交 pull request 来贡献内容。目标是建立一个共享的知识库，并为可重现的成果提供空间。

主要特点包括：

*   **轻松设置：** 无需复杂的项目设置；只需克隆、创建命名空间并编写代码。
*   **代码 & 撰写：** 将笔记、结果和想法作为注释直接集成到代码中。
*   **简单分享：** Pull request 会使内容发布在 Clojure Civitas 网站上。
*   **社区资源：** 贡献将成为共享社区知识库的一部分。
*   **可视化：** 支持表格、图表、Markdown 和 Hiccup 以呈现丰富的内容。
*   **原理：** 重视可重现的成果，使用代码中的 Markdown 来实现这一点。

该平台强调一种结构化的命名空间命名和元数据方法，以促进内容发现和组织。类别、标签和关键字（使用 Quarto 约定）用于组织内容。元数据用于重建线性序列，例如博客文章。

鼓励贡献者添加或修改 `site/db.edn` 文件，构建一个用于学习的资源数据库。该平台使用共享的 `deps.edn` 文件进行依赖管理，以简化网站构建。

---

## 49. OpenIPC：开放式IP摄像头固件

**原文标题**: OpenIPC: Open IP Camera Firmware

**原文链接**: [https://openipc.org/à](https://openipc.org/à)

OpenIPC是一个开源固件项目，旨在替代预装在许多使用ARM和MIPS处理器的IP摄像头上的封闭、通常过时且不安全的固件。该项目旨在让用户更好地控制他们的摄像头和视频流。

OpenIPC的主要特点：

*   **开源且可定制：** 以MIT许可证发布，允许用户自由使用、复制、修改和贡献源代码。
*   **预编译二进制文件：** 为终端用户提供易于安装的预编译二进制文件。
*   **基于Buildroot：** 使用Buildroot创建其Linux发行版，并利用Majestic、Mini或Venc流处理器。 Majestic代码目前是封闭源代码，但有可能通过社区资助实现开源。
*   **专注于自由和安全：** 提供完整的系统访问权限，消除后门，并防止恶意软件活动，如加密货币挖掘或键盘记录。
*   **核心功能优先：** 最初专注于诸如固件更新和视频/音频流配置等基本功能，并提供社区支持。
*   **附加功能：** 支持IPEYE云存储、视频流到Youtube和Telegram、SOCKS5代理、虚拟隧道，并且正在被改造用于无人机摄像头、建筑头盔集成和医学研究等专业应用。

本质上，OpenIPC旨在提供一种安全、可定制且由社区支持的专有IP摄像头固件替代方案。

---

## 50. DrawAFish.com 事后分析

**原文标题**: DrawAFish.com Postmortem

**原文链接**: [https://aldenhallak.com/blog/posts/draw-a-fish-postmortem.html](https://aldenhallak.com/blog/posts/draw-a-fish-postmortem.html)

奥尔登·哈拉克撰写了一篇事后分析报告，讲述了他的“氛围代码”网站DrawAFish.com在短暂登上Hacker News榜首后，所遭受的安全漏洞以及随之而来的混乱。该事件发生在2025年8月3日美国东部时间凌晨2点至早上8点之间，导致用户名被恶意篡改（辱骂性言论）以及冒犯性鱼类被批准通过，而安全的鱼类却被移除。

根本原因包括过去Neopets数据泄露中暴露的遗留的6位数管理员密码，缺乏身份验证的用户名更新API，以及未绑定到特定用户的JWT。哈拉克承认自己“氛围代码”，优先考虑速度而非安全最佳实践，忽视代码审查，并且过度依赖Copilot而没有进行适当的监督。

恢复工作包括使用日志手动撤销修改操作并修补漏洞。幸运的是，一位Hacker News用户（@iceweaselfan44）发现并利用了JWT漏洞，在哈拉克醒来之前帮助删除了冒犯性内容。该用户后来协助哈拉克重构代码库以提高安全性。

哈拉克反思了彻底的代码审查的重要性，以及即使在个人项目中也不应忽视安全性。他承认LLM（Copilot）仅仅是一个工具，安全代码的责任最终在于开发人员。他最后幽默地提出以每张100美元的价格出售贴纸。

---

## 51. C10k日

**原文标题**: C10kday

**原文链接**: [https://daniel.haxx.se/blog/2025/08/05/c10kday/](https://daniel.haxx.se/blog/2025/08/05/c10kday/)

本文宣布“c10kday”（curl-10000天），纪念自1998年3月20日首次curl发布以来的一万天，即2025年8月5日。目的是通过邀请curl用户分享他们与curl的故事和经验来庆祝这一里程碑，包括美好的回忆、curl特别有帮助的时刻，或者curl对他们的工作、业务或生活产生的影响。本文强调偏爱积极、有趣、怀旧和充满情感的故事。用户被引导至GitHub Discussion主题 (https://github.com/curl/curl/discussions/17930) 提交他们的故事或阅读其他人的贡献。虽然承认c10kday，但本文也强调对curl的工作将照常进行，包括持续的功能开发和错误修复。

---

## 52. 印度招牌绘画：字体设计师对这门工艺的理解

**原文标题**: Indian Sign Painting: A typeface designer's take on the craft

**原文链接**: [https://bl.ag/indian-sign-painting-a-typeface-designers-take-on-the-craft/](https://bl.ag/indian-sign-painting-a-typeface-designers-take-on-the-craft/)

字体设计师普嘉·萨克塞纳挑战了人们对印度街头字体的常见且过于简单的看法，即仅将其视为华丽的标牌绘画。她即将出版的书籍《印度街头字体》记录了印度各地各种非数字标牌制作技术和设计风格。

萨克塞纳强调了关注当地背景和个人风格、学习“行业语言”以及像分析字体一样批判性地分析手绘字体的重要性。她强调，标牌画师在为当地企业工作时通常拥有创作自由，这有助于在他们的城市中形成可识别的印刷风格。例如，加尔各答的彩绘巴士、科钦的船只以及阿扎德乐队在勒克瑙的克制美学。

从字体设计师的角度来看，萨克塞纳观察到了标牌绘画的优点和缺点。她注意到，在手绘梵文字体中，有时会不必要地复制活字印刷的限制。然而，她也赞赏这种媒介的灵活性，强调了创新的节省空间技术以及在多语种标牌中无缝集成多种文字。总的来说，萨克塞纳倡导更深入地欣赏手绘字体，通过个人风格、功能需求和当地品味的视角来理解它，超越肤浅的感知。

---

## 53. Show HN: 我过去三年一直在开发一个制造业ERP系统

**原文标题**: Show HN: I've been building an ERP for manufacturing for the last 3 years

**原文链接**: [https://github.com/crbnos/carbon](https://github.com/crbnos/carbon)

Carbon：一款开源ERP系统，专为制造业设计，历时三年打造，旨在解决现有方案的局限性。它致力于消除厂商锁定、缺乏现代化的API优先工具以及没有针对独特公司需求量身定制的ERP等问题。

Carbon的架构通过其API实现轻松扩展，允许用户构建自定义应用程序。主要功能包括ERP、MES、QMS、自定义字段、嵌套BOM、可追溯性、MRP、配置器、MCP客户端/服务器、API、Webhooks、会计、产能规划和模拟。技术亮点涵盖统一身份验证、全栈类型安全、实时数据库订阅以及强大的访问控制机制（ABAC、RBAC、RLS）。

技术栈利用Remix、Typescript、Tailwind、Radix UI、Supabase、Upstash、Trigger、Resend、Novu、Vercel和Stripe。代码库遵循Turborepo monorepo结构，组织应用程序（erp、mes、academy、starter）和共享代码包。

要使用Carbon进行开发，用户需要Docker、Node.js v20以及Upstash、Trigger.dev和Posthog的帐户（均提供免费套餐）。设置包括克隆存储库，使用来自这些服务的API密钥配置环境变量，运行数据库迁移，构建软件包，以及启动所需的应用程序。API文档在ERP应用程序中自动生成，并且API可以从外部和内部访问。

---

## 54. 作为一名语言学家，我想找到衡量慢性疾病的词汇。

**原文标题**: As a linguist, I want to find the words to measure chronic illness

**原文链接**: [https://thesicktimes.org/2025/08/01/as-a-linguist-i-want-to-find-the-words-to-measure-chronic-illness/](https://thesicktimes.org/2025/08/01/as-a-linguist-i-want-to-find-the-words-to-measure-chronic-illness/)

作为一名语言学家，我想找到衡量慢性疾病的词语：M Corvi探讨了量化和交流慢性疾病主观体验的挑战。Corvi患有MCAS和POTS，他们对经常无法捕捉他们真实状况的医学测试感到沮丧，并强调了患者的感受与医学中使用的客观测量之间的“语言差距”。

作者认为，当前的医学测量过于依赖可观察的现象和精确的语言，使得那些患有“隐形”疾病（如Long COVID、MCAS和POTS）的人难以有效地表达他们的症状。Corvi强调，即使找到了生物标志物，它们也无法完全捕捉到疾病的真实体验。

Corvi批评了现有的测量工具，如疼痛量表和Bell CFIDS量表，认为它们不够精确，无法解释慢性病的复杂性。他们指出，慢性病患者生活中的关键方面，如情感损失和生活方式的调整，经常在医疗记录中缺失。

最终，作者呼吁一种更“人道主义的医学”，通过协作命名和测量主观感受来弥合语言差距。他们主张从业者和研究人员参与患者的不适，并开发更准确的、反映慢性病全部现实的定性测量方法。这篇文章强调了定量和定性方法在理解和治疗慢性疾病方面的必要性。

---

## 55. 内容感知间隔重复

**原文标题**: Content-Aware Spaced Repetition

**原文链接**: [https://www.giacomoran.com/blog/content-aware-sr/](https://www.giacomoran.com/blog/content-aware-sr/)

本文介绍了内容感知间隔重复的概念，指出当前的间隔重复系统（SRS）存在局限性，因为它们孤立地对待记忆卡片，忽略了它们的语义内容和关系。作者区分了调度器（决定*显示哪些*卡片）和记忆模型（预测*何时*会忘记卡片）。目前的系统经常将这两者混淆，阻碍了创新。

内容感知记忆模型旨在通过考虑卡片的文本内容和相关卡片的复习历史来改进预测。这使得能够更明智地初步估计难度，并通过联想进行强化。本文重点介绍了KARL模型，该模型使用BERT嵌入来理解卡片内容并找到相似卡片，证明其性能优于传统方法。

作者进行的小型实验，通过“笔记”（语义相关的Topic）对卡片进行分组，表明对于新卡片，结合相关卡片的平均稳定性，并在最近复习相关卡片时“启动”稳定性，可以提高模型性能。

作者认为，内容感知模型开启了新的用户体验可能性，例如以想法为中心的记忆系统和会话式辅导，但也承认了收集足够数据来有效训练这些模型的挑战。分离调度器和记忆模型的开发允许独立创新和用户体验优化，从而带来更复杂和个性化的学习工具。

---

## 56. 美国宇航局“好奇号”探测器掌握新技能

**原文标题**: NASA's Curiosity picks up new skills

**原文链接**: [https://www.jpl.nasa.gov/news/marking-13-years-on-mars-nasas-curiosity-picks-up-new-skills/](https://www.jpl.nasa.gov/news/marking-13-years-on-mars-nasas-curiosity-picks-up-new-skills/)

NASA“好奇号”火星车任务13年，得益于新引入的自主性和多任务处理能力，效率更高。喷气推进实验室（JPL）的工程师们开发了改进方案，使火星车能够节省其多任务放射性同位素热电发生器（MMRTG）的能量，因为用于产生能量的钚会随着时间的推移而衰变。

这些新技能包括组合任务的能力，例如在行驶或操作其机械臂的同时向轨道飞行器传输数据。如果“好奇号”提前完成任务，它现在也可以选择小睡，从而减少了充电的需求。这些节省下来的时间积累起来，最大限度地延长了MMRTG的寿命，并从长远来看能够进行更多的科学研究。

这些改进使“好奇号”能够继续探索夏普山上的网格状地貌，寻找线索，以了解在数十亿年前火星变干时，微生物生命是否能在火星地表下生存。

除了这些节能措施之外，该团队还实施了解决机械挑战的方案，包括改造机械臂的钻头，并为Mastcam相机之一上的故障彩色滤光片轮开发了替代方案。还实施了一种算法，以减少火星车车轮的磨损。尽管有一些损坏，但预计这些车轮仍可使用数年。“好奇号”任务由JPL管理，加州理工学院和马林空间科学系统公司也做出了贡献。

---

## 57. Perplexity正使用隐蔽的、未声明的网络爬虫来规避禁止抓取的指令。

**原文标题**: Perplexity is using stealth, undeclared crawlers to evade no-crawl directives

**原文链接**: [https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/)

Cloudflare指责Perplexity使用隐蔽爬取策略绕过网站禁止抓取指令

---

## 58. 自定义 tmux

**原文标题**: Customizing tmux

**原文链接**: [https://evgeniipendragon.com/posts/customizing-tmux-and-making-it-less-dreadful/](https://evgeniipendragon.com/posts/customizing-tmux-and-making-it-less-dreadful/)

本文详述了作者自定义终端复用器tmux的历程。最初，作者对默认UI感到不知所措，随后强调了tmux的关键优势：在一个窗口中管理多个终端、创建独立会话以及在关闭后保留会话。

文章的核心在于通过位于用户主目录下的`.tmux.conf`文件自定义tmux。主要自定义包括：

*   **前缀键重映射:** 将默认前缀键 (Ctrl-b) 更改为 Ctrl-a 以便更容易访问。
*   **按键绑定:** 重新映射用于分割窗格、重新加载配置文件以及在没有前缀键的情况下导航窗格和窗口的按键。
*   **回滚和鼠标支持:** 增加回滚缓冲区，启用鼠标控制以方便滚动，并在复制模式下使用 Vim 键绑定。
*   **样式:** 调整UI中的颜色和元素（状态栏、窗格、消息），以获得更具视觉吸引力和直观的体验。

文章还介绍了 tmux 插件管理器 (TPM)，并包含使用它的基本配置，提及了电池监控、自动重新加载、浏览器集成等潜在插件。作者提供了完整的`.tmux.conf`文件作为参考。最后，作者对改进和个性化的tmux环境表示满意。

---

## 59. 拨打当地社保电话可能遇到无法提供帮助的人。

**原文标题**: Call to a local Social Security may be picked up by someone who can't help

**原文链接**: [https://www.npr.org/2025/08/05/nx-s1-5482913/social-security-phone-sharing-system](https://www.npr.org/2025/08/05/nx-s1-5482913/social-security-phone-sharing-system)

一项新的社会保障管理局（SSA）举措旨在通过将电话转接到任何可用的外地办事处来缩短电话等待时间，但正受到员工、残疾倡导者和专家的批评。 在新系统下，拨打当地办事处电话的人可能会与无权处理其具体案件的工作人员联系。

尽管SSA声称所有外地办事处都具备处理全国各地咨询的能力，但工会代表和倡导者报告称，该系统并未按预期运行。 索赔专家认为，他们经常缺乏解决其他辖区案件的权力，导致延误和官僚主义增加，因为来电者会被转回原始办事处。

残疾倡导者担心这会造成困难，尤其是对于没有代理人的人，因为它可能会阻止未来联系SSA的尝试。 还有人对该计划的持续时间缺乏沟通以及机构内部变化的快速步伐表示担忧，这使得员工和公众都在努力适应。 像南希·奥特曼这样的倡导者认为，以前的政府让所有层级都参与到新系统的实施中，从而促进了理解和更顺畅的过渡。 目前的系统被认为是一项沟通不畅且执行不力的变革，给员工和依赖社会保障福利的人都增加了压力。

---

## 60. 收购Windsurf三周后，Cognition向员工提供离职选择

**原文标题**: Three weeks after acquiring Windsurf, Cognition offers staff the exit door

**原文链接**: [https://techcrunch.com/2025/08/05/three-weeks-after-acquiring-windsurf-cognition-offers-staff-the-exit-door/](https://techcrunch.com/2025/08/05/three-weeks-after-acquiring-windsurf-cognition-offers-staff-the-exit-door/)

AI编码初创公司Cognition在收购Windsurf仅三周后，正向Windsurf几乎所有剩余的200名员工提供买断协议。此前一周，Windsurf已裁员30人。Windsurf在被收购前经历了一段动荡时期，最初受到OpenAI的青睐，随后在一次反向收购中失去了其首席执行官和研究主管，他们加入了谷歌。

尽管Cognition最初声称Windsurf的所有员工都将获得经济补偿，并被视为“世界一流的人才”，但该公司现在似乎主要对Windsurf的知识产权感兴趣。

员工必须在8月10日之前接受9个月工资的买断方案。据报道，留下的人将被要求每周工作六天，工作时间超过80小时。 Cognition首席执行官Scott Wu为这种高强度的工作环境辩护，声称该公司不相信工作与生活的平衡，因为他们对自己的使命充满热情。 TechCrunch已联系Cognition征求意见。

---

## 61. 广岛 (1946)

**原文标题**: Hiroshima (1946)

**原文链接**: [https://www.newyorker.com/magazine/1946/08/31/hiroshima](https://www.newyorker.com/magazine/1946/08/31/hiroshima)

约翰·赫西的《广岛》讲述了1945年8月6日广岛原子弹爆炸中六位幸存者的经历。叙述从佐佐木敏子小姐、藤井正一医生、中村初代夫人、威廉·克莱因佐尔格神父、佐佐木辉文医生和谷本清志牧师在爆炸发生前一刻的平凡生活开始。

谷本牧师因担心B-29轰炸机的袭击而焦虑不安，当时正在帮助朋友疏散财产，炸弹突然爆炸。中村夫人是一位裁缝的遗孀，在经历了因空袭警报而彻夜难眠的夜晚后，她决定不把孩子们疏散到安全区。

叙述通过他们的个人视角捕捉到了爆炸后的瞬间。谷本被爆炸的威力击倒，目睹了附近房屋的毁灭以及士兵们茫然失措的状态。中村夫人在房子倒塌时被抛到屋外。故事突出了生存的随机性以及幸存者经历的巨大震惊和难以置信的感觉。文章强调了破坏的规模和无法理解的生命损失，为探讨爆炸对这六个人和广岛市的长期影响奠定了基础。

---

## 62. 3I/ATLAS星际天体是外星科技吗？[pdf]

**原文标题**: Is the interstellar object 3I/ATLAS alien technology? [pdf]

**原文链接**: [https://lweb.cfa.harvard.edu/~loeb/HCL25.pdf](https://lweb.cfa.harvard.edu/~loeb/HCL25.pdf)

这份PDF文档似乎是由 Adam Hibberd、Adam Crowl 和 Abraham Loeb 撰写的题为“星际物体 3I/ATLAS 是外星科技吗？”的研究论文的第一个版本。

该文档的元数据包括 DOI、许可协议 (http://arxiv.org/licenses/nonexclusive-distrib/1.0/) 和 arXiv ID (https://arxiv.org/abs/2507.12213v1)。元数据还包括学科分类 astro-ph.EP、astro-ph.GA 和 astro-ph.IM。

该论文包含许多引用和参考文献，包括“seligman2025discovery”、“bolin2025”、“opitom2025”、“alvarezcandal2025”、“hopkins_2025”、“taylor2025”、“kakharov2025”、“loeb2025”、“Loeb_2025”、“SETI”、“Bannister2019”和“2022AsBio..22.1392L”。它似乎还引用了文档本身的章节、项目和表格。

提供了 Adam Hibberd 的电子邮件联系方式 (adam.hibberd@i4is.org)。

由于此文档是 PDF 格式，仅包含元数据、目录和文档大纲信息，因此无法深入研究论文中提出的论点或证据。然而，标题和 arXiv 信息表明这是一篇研究文章，探讨了星际物体 3I/ATLAS 可能具有人工来源的可能性。

---

## 63. Show HN: Scar – 一种易于实现并发与并行的编程语言

**原文标题**: Show HN: Scar – A programming language for easy concurrency and parallelism

**原文链接**: [https://scarlang.pages.dev/](https://scarlang.pages.dev/)

Scar：一种简化并发与并行，且不牺牲性能的全新系统编程语言。它旨在通过并行代码块等特性，抽象化线程管理的复杂性，从而使系统编程更易于上手。

Scar的主要特性包括：

*   **内置并发：** 能够自然地表达并行操作。
*   **简洁语法：** 注重可读性和易用性。
*   **内存安全：** 在保持性能的同时，防止常见的内存相关错误。
*   **高性能：** 编译为高效的本地代码。
*   **类型推断：** 减少样板代码，同时确保类型安全。
*   **C互操作性：** 允许与现有C库集成。

本文通过示例展示了Scar在并行处理（例如，使用 `parallel for` 循环并行处理数据）、清晰的类定义和类型推断方面的能力。这些示例突出了该语言专注于简化常见编程任务，同时保持性能和安全性的特点。 本质上，Scar为系统编程提供了一种现代方法，在易用性与满足高要求应用所需的强大功能和效率之间取得了平衡。

---

## 64. 我理想的数组语言

**原文标题**: My Ideal Array Language

**原文链接**: [https://www.ashermancinelli.com/csblog/2025-7-20-Ideal-Array-Language.html](https://www.ashermancinelli.com/csblog/2025-7-20-Ideal-Array-Language.html)

本文概述了作者对理想数组语言的设想，强调语言需要适应异构硬件不断发展的格局，从SIMD单元到GPU和专用处理器。这种理想语言的核心特性包括用户可扩展的秩多态、具有自动缓冲处理的值语义以及编译器透明性。

作者认为秩多态对于数组语言至关重要，并强调了现有解决方案（如NumPy和JAX）在这方面的局限性。他们提倡一种用户可以编写自己的多态内核的系统，可能通过暴露底层细节或允许可组合的原语来实现。

值语义和自动缓冲处理被认为是实现编译器优化的关键。文章以Fortran的数组语义为例，说明独占所有权如何使编译器能够有效地优化数组操作。讨论扩展到MLIR（一种在许多ML框架中使用的编译器基础设施）及其数组表示（张量和memref类型），突出了函数式数组编程对于编译器优化的好处。

文章还涉及编译步骤的重要性，无论是离线还是在线，都可以利用语言语义并执行优化。此外，它强调了编译器透明性和可检查性的必要性，使用户能够理解优化失败并识别性能瓶颈。作者呼吁改进针对用户（而非编译器工程师）的编译器报告机制。

---

## 65. 物体应该闭嘴。

**原文标题**: Objects should shut up

**原文链接**: [https://dustri.org/b/objects-should-shut-the-fuck-up.html](https://dustri.org/b/objects-should-shut-the-fuck-up.html)

作者抱怨日常物品发出不必要且往往有害的噪音，认为这些噪音具有干扰性，有时甚至很危险。他们主要的不满在于缺乏对这些声音的控制，提倡一种“默认关闭”的方法，用户需要明确授权才能接收通知。

作者的个人经历推动了他们的论点。他们详细描述了他们汽车液化石油气罐的过度响亮的警告声，这分散了他们开车的注意力，以及他们的洗衣机发出的许多恼人且无用的哔哔声，这些声音无法完全禁用。同样，他们的烘干机、电炉，甚至婴儿监视器都加剧了噪音。作者强调了这些噪音的荒谬性，尤其是在它们没有任何实际用途或与设备的预期用途相矛盾时，比如婴儿监视器在打开时会发出响亮的哔哔声，可能会吵醒婴儿。

作者强调，像汽车油量低这样的重要通知是必要的，但认为许多物体因为琐碎或多余的原因而过度嘈杂。他们以洗碗机、冰箱和电子阅读器为例，说明这些设备在没有持续的听觉干扰的情况下也能很好地工作。核心信息是呼吁设计师优先考虑用户体验和安全性，通过仔细考虑产品中声音通知的必要性和影响，建议他们在真实场景中测试这些声音，比如在熟睡的孩子附近。他们表达了“它能闭嘴吗？”已经成为一个关键购物标准的沮丧。

---

## 66. 周六早晨的消失 (2003)

**原文标题**: The Disappearance of Saturday Morning (2003)

**原文链接**: [https://www.awn.com/animationworld/disappearance-saturday-morning](https://www.awn.com/animationworld/disappearance-saturday-morning)

无法访问文章链接。

---

## 67. 利用无人机图像和人工智能快速评估飓风和洪水后的灾害损失

**原文标题**: Using drone imagery and AI to rapidly assess damage after hurricanes and floods

**原文链接**: [https://stories.tamu.edu/news/2025/07/28/ai-turns-drone-footage-into-disaster-response-maps-in-minutes/](https://stories.tamu.edu/news/2025/07/28/ai-turns-drone-footage-into-disaster-response-maps-in-minutes/)

生成摘要出错

---

## 68. Job-seekers are dodging AI interviewers

**原文标题**: Job-seekers are dodging AI interviewers

**原文链接**: [https://fortune.com/2025/08/03/ai-interviewers-job-seekers-unemployment-hiring-hr-teams/](https://fortune.com/2025/08/03/ai-interviewers-job-seekers-unemployment-hiring-hr-teams/)

This Fortune article discusses the growing trend of companies using AI interviewers in their hiring process and the resulting backlash from job seekers. Many candidates are refusing to participate in AI interviews, deeming them dehumanizing and a sign of poor company culture. They find the experience impersonal, frustrating, and question the value placed on human connection within the organization. Some feel their time is being wasted and are wary of companies prioritizing cost-saving measures over meaningful interaction.

On the other hand, HR teams and hiring managers are embracing AI interviewers as a way to streamline the application process, especially when dealing with a high volume of candidates. They argue that AI can efficiently filter applicants, allowing human recruiters to focus on more in-depth conversations with promising candidates later in the process. Companies like Braintrust, which provides AI interviewers, claim their clients are finding the tool useful and that candidates are generally satisfied.

The article highlights a stark divide between job seekers and HR professionals regarding the use of AI in interviews. While some AI interviewers are basic and robotic, others are more advanced, offering a more natural-sounding voice. Experts acknowledge AI's limitations, particularly in assessing cultural fit, and emphasize its strength lies in objective skill assessment. Despite the concerns, the article suggests that AI interviewers are likely to remain a part of the hiring landscape.


---

## 69. Converge (YC S23) well-capitalized New York startup seeks product developers

**原文标题**: Converge (YC S23) well-capitalized New York startup seeks product developers

**原文链接**: [https://www.runconverge.com/careers](https://www.runconverge.com/careers)

Converge (YC S23 纽约初创公司) 诚聘产品开发者加入精简团队。公司产品市场匹配度高，仅6名员工便实现超100万美元年度经常性收入，服务客户超200家，为有志之士提供成为第7名员工的难得机会。

Converge 强调开发者所能产生的重大影响，在与 Segment 和 Fivetran 等老牌企业竞争的领域，提供对整个产品的所有权。他们的平台处理大量数据（每日2000万次互动，每年约30亿美元商品交易总额），带来真正的工程挑战，并因高日活跃用户参与度 (33%) 而保证即时客户反馈。

公司重视紧迫性、深刻理解、谦逊和简洁。他们获得了来自知名投资者的570万美元融资，并由具有强大编码背景的创始团队领导，致力于现场办公。本广告明确劝退偏好管理而非构建、偏好设计审查而非交付、追逐潮流、喜欢转型、寻求大量指导或偏好远程工作的人士。摘要还包含轶事信息以鼓励申请者。

---

## 70. Introduction to Unikernel: Building, deploying lightweight, secure applications

**原文标题**: Introduction to Unikernel: Building, deploying lightweight, secure applications

**原文链接**: [https://tallysolutions.com/technology/introduction-to-unikernel-2/](https://tallysolutions.com/technology/introduction-to-unikernel-2/)

生成摘要时出错

---

## 71. What Can a Cell Remember?

**原文标题**: What Can a Cell Remember?

**原文链接**: [https://www.quantamagazine.org/what-can-a-cell-remember-20250730/](https://www.quantamagazine.org/what-can-a-cell-remember-20250730/)

生成摘要时出错

---

## 72. The history of the Schwartzian Transform (2016)

**原文标题**: The history of the Schwartzian Transform (2016)

**原文链接**: [https://www.perl.com/article/the-history-of-the-schwartzian-transform/](https://www.perl.com/article/the-history-of-the-schwartzian-transform/)

生成摘要时出错

---

## 73. Century-old stone “tsunami stones” dot Japan's coastline (2015)

**原文标题**: Century-old stone “tsunami stones” dot Japan's coastline (2015)

**原文链接**: [https://www.smithsonianmag.com/smart-news/century-old-warnings-against-tsunamis-dot-japans-coastline-180956448/](https://www.smithsonianmag.com/smart-news/century-old-warnings-against-tsunamis-dot-japans-coastline-180956448/)

生成摘要时出错

---

## 74. Cellular Starlink expands to support IoT devices

**原文标题**: Cellular Starlink expands to support IoT devices

**原文链接**: [https://me.pcmag.com/en/networking/31452/spacexs-cellular-starlink-expands-to-support-iot-devices](https://me.pcmag.com/en/networking/31452/spacexs-cellular-starlink-expands-to-support-iot-devices)

生成摘要时出错

---

## 75. Palantir is extending its reach even further into government

**原文标题**: Palantir is extending its reach even further into government

**原文链接**: [https://www.wired.com/story/palantir-government-contracting-push/](https://www.wired.com/story/palantir-government-contracting-push/)

生成摘要时出错

---

## 76. Welcome to the IPv4 Games

**原文标题**: Welcome to the IPv4 Games

**原文链接**: [https://ipv4.games/](https://ipv4.games/)

生成摘要时出错

---

## 77. Show HN: Sidequest.js – Background jobs for Node.js using your database

**原文标题**: Show HN: Sidequest.js – Background jobs for Node.js using your database

**原文链接**: [https://docs.sidequestjs.com/quick-start](https://docs.sidequestjs.com/quick-start)

生成摘要时出错

---

## 78. Perfecting anti-aliasing on signed distance functions

**原文标题**: Perfecting anti-aliasing on signed distance functions

**原文链接**: [https://blog.pkh.me/p/44-perfecting-anti-aliasing-on-signed-distance-functions.html](https://blog.pkh.me/p/44-perfecting-anti-aliasing-on-signed-distance-functions.html)

生成摘要时出错

---

## 79. EconTeen – Financial literacy lessons and tools for teens

**原文标题**: EconTeen – Financial literacy lessons and tools for teens

**原文链接**: [https://econteen.com/](https://econteen.com/)

生成摘要时出错

---

## 80. Show HN: Tiny logic and number games I built for my kids

**原文标题**: Show HN: Tiny logic and number games I built for my kids

**原文链接**: [https://quizmathgenius.com/](https://quizmathgenius.com/)

生成摘要时出错

---

## 81. Once a death sentence, cardiac amyloidosis is finally treatable

**原文标题**: Once a death sentence, cardiac amyloidosis is finally treatable

**原文链接**: [https://www.nytimes.com/2025/08/04/well/cardiac-amyloidosis.html](https://www.nytimes.com/2025/08/04/well/cardiac-amyloidosis.html)

生成摘要时出错

---

## 82. Lamport's Byzantine Generals Algorithm in Python

**原文标题**: Lamport's Byzantine Generals Algorithm in Python

**原文链接**: [https://bytepawn.com/lamport-byzantine-generals.html](https://bytepawn.com/lamport-byzantine-generals.html)

生成摘要时出错

---

## 83. Read your code

**原文标题**: Read your code

**原文链接**: [https://etsd.tech/posts/rtfc/](https://etsd.tech/posts/rtfc/)

生成摘要时出错

---

## 84. The creative tension between developer and language

**原文标题**: The creative tension between developer and language

**原文链接**: [https://krishna.github.io/posts/creative-tension-between-developer-and-language/](https://krishna.github.io/posts/creative-tension-between-developer-and-language/)

生成摘要时出错

---

## 85. New quantum state of matter found at interface of exotic materials

**原文标题**: New quantum state of matter found at interface of exotic materials

**原文链接**: [https://phys.org/news/2025-07-quantum-state-interface-exotic-materials.html](https://phys.org/news/2025-07-quantum-state-interface-exotic-materials.html)

生成摘要时出错

---

## 86. Itch.io seeks payment processors who work with with adult material

**原文标题**: Itch.io seeks payment processors who work with with adult material

**原文链接**: [https://www.rockpapershotgun.com/itchio-are-seeking-out-new-payment-processors-who-are-more-comfortable-with-adult-material](https://www.rockpapershotgun.com/itchio-are-seeking-out-new-payment-processors-who-are-more-comfortable-with-adult-material)

生成摘要时出错

---

## 87. Swarm robotics could spell the end of the assembly line

**原文标题**: Swarm robotics could spell the end of the assembly line

**原文链接**: [https://www.therobotreport.com/swarm-robotics-could-spell-end-aerospace-assembly-line/](https://www.therobotreport.com/swarm-robotics-could-spell-end-aerospace-assembly-line/)

生成摘要时出错

---

## 88. How we built Bluey’s world

**原文标题**: How we built Bluey’s world

**原文链接**: [https://www.itsnicethat.com/features/how-we-built-bluey-s-world-cartoon-background-scenery-art-director-catriona-drummond-animation-090725](https://www.itsnicethat.com/features/how-we-built-bluey-s-world-cartoon-background-scenery-art-director-catriona-drummond-animation-090725)

生成摘要时出错

---

## 89. Lidar-based GIS map of New Hampshire stone walls

**原文标题**: Lidar-based GIS map of New Hampshire stone walls

**原文链接**: [https://nhgranit.maps.arcgis.com/apps/webappviewer/index.html?id=25930044fe2b4d8fb5cab3ec07565e83](https://nhgranit.maps.arcgis.com/apps/webappviewer/index.html?id=25930044fe2b4d8fb5cab3ec07565e83)

生成摘要时出错

---

## 90. Show HN: Mathpad – Physical keypad for typing math symbols

**原文标题**: Show HN: Mathpad – Physical keypad for typing math symbols

**原文链接**: [https://www.crowdsupply.com/summa-cogni/mathpad](https://www.crowdsupply.com/summa-cogni/mathpad)

生成摘要时出错

---

## 91. GHz spiking neuromorphic photonic chip with in-situ training

**原文标题**: GHz spiking neuromorphic photonic chip with in-situ training

**原文链接**: [https://arxiv.org/abs/2506.14272](https://arxiv.org/abs/2506.14272)

生成摘要时出错

---

## 92. wget to be removed from default Ubuntu Server 25.10

**原文标题**: wget to be removed from default Ubuntu Server 25.10

**原文链接**: [https://www.omgubuntu.co.uk/2025/08/ubuntu-server-25-10-replaces-wget-with-wcurl](https://www.omgubuntu.co.uk/2025/08/ubuntu-server-25-10-replaces-wget-with-wcurl)

生成摘要时出错

---

## 93. Deterministic Simulation Testing in Rust: A Theater of State Machines

**原文标题**: Deterministic Simulation Testing in Rust: A Theater of State Machines

**原文链接**: [https://www.polarsignals.com/blog/posts/2025/07/08/dst-rust](https://www.polarsignals.com/blog/posts/2025/07/08/dst-rust)

生成摘要时出错

---

## 94. Mastercard deflects blame for NSFW games being taken down

**原文标题**: Mastercard deflects blame for NSFW games being taken down

**原文链接**: [https://www.pcgamer.com/games/mastercard-deflects-blame-for-nsfw-games-being-taken-down-but-valve-says-payment-processors-specifically-cited-a-mastercard-rule-about-damaging-the-brand/](https://www.pcgamer.com/games/mastercard-deflects-blame-for-nsfw-games-being-taken-down-but-valve-says-payment-processors-specifically-cited-a-mastercard-rule-about-damaging-the-brand/)

生成摘要时出错

---

## 95. A deep dive into Rust and C memory interoperability

**原文标题**: A deep dive into Rust and C memory interoperability

**原文链接**: [https://notashes.me/blog/part-1-memory-management/](https://notashes.me/blog/part-1-memory-management/)

生成摘要时出错

---

## 96. Trust in AI coding tools is plummeting

**原文标题**: Trust in AI coding tools is plummeting

**原文链接**: [https://leaddev.com/technical-direction/trust-in-ai-coding-tools-is-plummeting](https://leaddev.com/technical-direction/trust-in-ai-coding-tools-is-plummeting)

生成摘要时出错

---

## 97. Fine-tuned small LLMs can beat large ones with programmatic data curation

**原文标题**: Fine-tuned small LLMs can beat large ones with programmatic data curation

**原文链接**: [https://www.tensorzero.com/blog/fine-tuned-small-llms-can-beat-large-ones-at-5-30x-lower-cost-with-programmatic-data-curation/](https://www.tensorzero.com/blog/fine-tuned-small-llms-can-beat-large-ones-at-5-30x-lower-cost-with-programmatic-data-curation/)

生成摘要时出错

---

## 98. Show HN: Kimu – Open-Source Video Editor

**原文标题**: Show HN: Kimu – Open-Source Video Editor

**原文链接**: [https://www.trykimu.com/](https://www.trykimu.com/)

生成摘要时出错

---

## 99. Rising young worker despair in the United States

**原文标题**: Rising young worker despair in the United States

**原文链接**: [https://www.nber.org/papers/w34071](https://www.nber.org/papers/w34071)

生成摘要时出错

---

## 100. Scientists shine a laser through a human head

**原文标题**: Scientists shine a laser through a human head

**原文链接**: [https://spectrum.ieee.org/optical-brain-imaging](https://spectrum.ieee.org/optical-brain-imaging)

生成摘要时出错

---

