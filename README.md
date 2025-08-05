# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-08-05.md)

*最后自动更新时间: 2025-08-05 17:52:11*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 2 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 3 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 4 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 5 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 6 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 7 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 8 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 9 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 10 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 11 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 12 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 13 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 14 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 15 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 16 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 17 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 18 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 19 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 20 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 21 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 22 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 23 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 24 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 25 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 26 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 27 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 28 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 29 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 30 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 31 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 32 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 33 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 34 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 35 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 36 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 37 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 38 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 39 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 40 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 41 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 42 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 43 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 44 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 45 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 46 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 47 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 48 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 49 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 50 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 51 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 52 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 53 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 54 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 55 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 56 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 57 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 58 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 59 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 60 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 61 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 62 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 63 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 64 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 65 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 66 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 67 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 68 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 69 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 70 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 71 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 72 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 73 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 74 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 75 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 76 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 77 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 78 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 79 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 80 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 81 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 82 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 83 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 84 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 85 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 86 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 87 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 88 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 89 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 90 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 91 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 92 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 93 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 94 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 95 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 96 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 97 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 98 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 99 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 100 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 101 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 102 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 103 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 104 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 105 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 106 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 107 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 108 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 109 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 110 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 111 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 112 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 113 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 114 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 115 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 116 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 117 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 118 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 119 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 120 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 121 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 122 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 123 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 124 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 125 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 126 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 127 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 128 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 129 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 130 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 131 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 132 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 133 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 134 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 135 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 136 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 137 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 138 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 139 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
