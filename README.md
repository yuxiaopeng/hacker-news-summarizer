# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-09-06.md)

*最后自动更新时间: 2025-09-06 17:42:32*
## 1. 996

**原文标题**: 996

**原文链接**: [https://lucumr.pocoo.org/2025/9/4/996/](https://lucumr.pocoo.org/2025/9/4/996/)

Armin Ronacher 的博文《996》讨论了公司推崇“996”工作文化（早 9 点到晚 9 点，每周工作 6 天）这种有问题的趋势。他承认自己热爱高强度工作和深夜编程，但认为这不应成为常态或公司的积极标志。

Ronacher 强调了工作与生活平衡的重要性，特别是对于有家庭和个人兴趣的人来说。他区分了创始人的奉献精神（他们的风险和杠杆与员工不同）以及期望员工遵守如此艰苦的作息时间之间的区别。他批评那些推崇这种模式的创始人是不负责任的。

他认为成功是一场马拉松，而不是短跑，可持续的生产力比在办公室里花费的时间更重要。虽然他喜欢偶尔通宵，但他强调这应该是个人的选择，而不是公司文化的要求，并承认它们造成的生产力低下后果。最终，Ronacher 倡导抵制对 996 工作文化的推崇，强调这种模式的不可持续性和潜在危害性。他认为产出和满足感比单纯的工作时长更重要。

---

## 2. DuckDuckGo创始人：应禁止人工智能监控

**原文标题**: DuckDuckGo founder: AI surveillance should be banned

**原文链接**: [https://gabrielweinberg.com/p/ai-surveillance-should-be-banned](https://gabrielweinberg.com/p/ai-surveillance-should-be-banned)

本文中，DuckDuckGo的创始人主张禁止人工智能监控，强调其相比传统在线追踪放大了隐私风险。他认为，由于人工智能聊天机器人的对话特性和收集详细个人信息的能力，它们会创建全面的性格侧写，容易受到商业和政治操纵。他指出，这些侧写可能被利用，通过定制化的论点和微妙的产品推荐来影响用户。

他强调，围绕搜索引擎的隐私辩论更适用于人工智能聊天。虽然DuckDuckGo提供受保护的聊天机器人对话和匿名人工智能辅助搜索，但他指出，隐私泄露已经发生，并引用了Grok泄露的对话和Perplexity易受黑客攻击等例子。他警告说，OpenAI设想的全面“超级助手”以及Anthropic默认对用户对话的训练。

鉴于美国缺乏通用的在线隐私法，作者呼吁国会迅速采取行动，确保受保护的聊天成为标准做法。他警告说，进一步拖延将巩固有害的隐私实践，重蹈在线追踪的覆辙。他总结说，DuckDuckGo将继续为寻求在线效率而不牺牲隐私的用户提供尊重隐私的服务，包括人工智能。他主张在为时已晚之前禁止人工智能监控。

---

## 3. Qwen3 30B A3B 在 4 个树莓派 5 上达到 13 token/s

**原文标题**: Qwen3 30B A3B Hits 13 token/s on 4xRaspberry Pi 5

**原文链接**: [https://github.com/b4rtaz/distributed-llama/discussions/255](https://github.com/b4rtaz/distributed-llama/discussions/255)

本文详细描述了一项实验，该实验成功地在由四台树莓派5 8GB设备组成的集群上运行了Qwen3 30B A3B语言模型。该实验使用了Distributed Llama框架（版本0.16.0），并将模型量化到Q40。树莓派通过TP-Link交换机连接并分配工作负载。

主要结果强调了所实现的性能：系统在评估期间达到了14.33 tokens/秒，在预测期间达到了13.04 tokens/秒。本文档提供了用于运行推理的具体命令，并展示了详细的输出，包括网络初始化、权重加载和令牌生成过程。它指出了模型的内存需求、正在使用的CPU特性以及分布式工作节点之间的同步时间。用于推理的提示是一个关于波兰位置的简单问题。模型生成的响应将波兰置于相对于其他国家的地理环境中。

本文档还展示了模型的架构和配置（Qwen3 MoE，包括隐藏维度、层数和头数以及rope theta等参数），并提供了分布式llama设置的版本信息。

---

## 4. 理解大型语言模型所需的数学基础

**原文标题**: The maths you need to start understanding LLMs

**原文链接**: [https://www.gilesthomas.com/2025/09/maths-for-llms](https://www.gilesthomas.com/2025/09/maths-for-llms)

Giles 的这篇博文解释了理解大型语言模型 (LLM) 如何运作所需的基本数学知识，重点在于推理（使用现有 AI），而非训练过程。它面向具有基本技术背景但没有深入 AI 知识的读者。

涵盖的核心概念是向量和高维空间。向量不仅仅是数字数组，还代表 n 维空间中的距离和方向，在 LLM 中，它们代表 logits 和含义。Giles 介绍了“词汇空间”，其中 logits（下一个 token 的可能性）被表示为向量，并重点介绍了“混乱”（未归一化）和整洁（归一化）版本的词汇空间。独热向量，即只有一个元素设置为 1 的向量，也被作为一个概念引入。

该文章随后深入探讨了“嵌入空间”，其中向量代表含义，相似的概念聚集在一起。这些向量的长度并不总是关键；方向更重要。

接下来，Giles 解释了矩阵（堆叠的向量）如何通过矩阵乘法用于不同多维空间之间的投影。具体来说，一个 d1×d2 矩阵将 d1 维空间投影到 d2 维空间。他强调，这种投影可能是有损的，这意味着信息可能在降维过程中丢失。

最后，该文章将矩阵乘法与神经网络联系起来，表明一个单层计算，在简化后，本质上是一个矩阵乘法，从而强调了矩阵在理解 LLM 中的重要性。神经网络中的权重矩阵的作用类似于投影矩阵，有助于转换和抽象。

---

## 5. 最早记录的交易

**原文标题**: Oldest Recorded Transaction

**原文链接**: [https://avi.im/blag/2025/oldest-txn/](https://avi.im/blag/2025/oldest-txn/)

这篇文章探讨了现代数据库在处理极其古老日期时的局限性，起因是一张5000年前的苏美尔交易记录图片。作者调查了MySQL、Postgres和SQLite支持的最早时间戳。MySQL的限制是公元1000年，而Postgres和SQLite利用儒略历，可以追溯到公元前4713年1月1日。

作者成功地将公元前4713年插入到Postgres和SQLite中，但在尝试插入公元前4714年时遇到错误，表明了这些数据库的下限。这一限制引发了如何存储和管理比公元前4713年更早的日期的问题，例如英国博物馆等机构的历史记录。

文章考虑了潜在的解决方案，包括将日期存储为 epoch 时间戳、文本字符串或使用自定义系统。一个关键的挑战是在使用这些替代存储方法时，如何保持标准 TIMESTAMP 操作的功能。作者最后感谢了贡献者，并引用了初始图片来源和 Joran Dirk Greef 的相关演讲。

---

## 6. Anthropic 同意支付 15 亿美元与图书作者达成和解

**原文标题**: Anthropic agrees to pay $1.5B to settle lawsuit with book authors

**原文链接**: [https://www.nytimes.com/2025/09/05/technology/anthropic-settlement-copyright-ai.html?unlocked_article_code=1.jk8.bTTt.Zir9wmtPaTp2&smid=url-share](https://www.nytimes.com/2025/09/05/technology/anthropic-settlement-copyright-ai.html?unlocked_article_code=1.jk8.bTTt.Zir9wmtPaTp2&smid=url-share)

无法访问文章链接。

---

## 7. 扎克伯格在白宫晚宴上被意外录到私下谈话

**原文标题**: Zuckerberg Caught in Revealing Hot Mic Moment During White House Dinner

**原文链接**: [https://www.pcmag.com/news/zuckerberg-caught-in-revealing-hot-mic-moment-during-white-house-dinner](https://www.pcmag.com/news/zuckerberg-caught-in-revealing-hot-mic-moment-during-white-house-dinner)

白宫晚宴：科技巨头与特朗普讨论AI投资，扎克伯格或夸大Meta投资额

---

## 8. 我们黑了汉堡王：认证绕过如何导致了得来速音频监控

**原文标题**: We Hacked Burger King: How Auth Bypass Led to Drive-Thru Audio Surveillance

**原文链接**: [https://bobdahacker.com/blog/rbi-hacked-drive-thrus/](https://bobdahacker.com/blog/rbi-hacked-drive-thrus/)

好的，以下是基于所提供URL内容对“我们入侵了汉堡王：认证绕过如何导致得来速语音监控”文章的总结作者BobDaHacker详细描述了他们如何发现并利用Restaurant Brands International (RBI) 在线订购平台上的一个漏洞，该漏洞影响了汉堡王的得来速服务。该漏洞使他们能够绕过身份验证，访问敏感的客户数据，甚至可以收听来自得来速对讲机的实时音频流。

最初的漏洞源于一个未正确实施的API端点，该端点用于员工身份验证和菜单更新。通过操纵API请求，作者能够在不需要有效凭据的情况下冒充餐厅经理。这种未经授权的访问使他们能够查看餐厅的特定数据，包括销售额、员工信息（用户名、哈希密码），以及关键的得来速通信系统的配置设置。

该漏洞利用最令人担忧的方面是能够收听来自得来速的实时音频。作者发现了为远程监控和维护得来速系统而设计的API端点，其中包括访问实时音频流的权限。这使他们能够窃听顾客在得来速窗口的订单和对话，引发了严重的隐私问题。

作者负责任地向RBI披露了这些漏洞，RBI承认了这个问题并实施了修复。该博客文章详细介绍了识别和利用这些漏洞的技术步骤，强调了在线系统中正确身份验证和授权机制的重要性，特别是那些处理敏感客户数据并可能启用音频监控的系统。作者还建议RBI进行定期的安全审计和渗透测试，以防止将来出现类似的漏洞。

---

## 9. 让我们摆脱它，愤怒的GitHub用户们如是说，针对强制Copilot功能。

**原文标题**: Let us git rid of it, angry GitHub users say of forced Copilot features

**原文链接**: [https://www.theregister.com/2025/09/05/github_copilot_complaints/](https://www.theregister.com/2025/09/05/github_copilot_complaints/)

本文报道了GitHub用户对强制整合微软AI服务Copilot日益增长的不满。一个热门社区讨论帖要求提供一种方法来阻止Copilot生成问题和拉取请求，而另一个则指出无法禁用Copilot代码审查。这些请求尚未得到回应，加剧了用户的沮丧。

开发者Andi McClure对Copilot基于GitHub发布的代码进行训练以及Copilot“广告”入侵其工作流程表示担忧。其他开发者也对Copilot传播不准确信息、代码建议引发的版权问题以及缺乏代码正确性保证表示担忧。包括Servo、GNOME的Loupe、FreeBSD、Gentoo、NetBSD和QEMU在内的多个项目已禁止AI代码贡献，原因正是这些问题。

文章指出，对Copilot整合的不满，加上GitHub整合到微软CoreAI集团，正推动开发者转向替代平台，如Codeberg和自托管的Forgejo实例。软件自由保护协会(SFC)长期以来一直倡导远离GitHub。一些开发者已经迁移了他们的代码，并用搬迁通知替换了他们的GitHub仓库。

文章最后提到McClure的观察，即微软默认启用功能并在用户禁用后反复重新引入这些功能的策略正在加剧问题。她认为，避免Copilot的唯一方法是停止使用任何出现它的微软产品，尽管由于GitHub近乎垄断和网络效应，这很困难。最终，开发者担心微软对AI指标的推动正在掩盖客户保留。

---

## 10. 宝宝的第一个类型检查器

**原文标题**: Baby's first type checker

**原文链接**: [https://austinhenley.com/blog/babytypechecker.html](https://austinhenley.com/blog/babytypechecker.html)

本文介绍了一个Python中“婴儿类型检查器”的实现，逐步讲解构建一个基本类型检查工具的过程。它解释了类型检查的工作原理，强调了它在及早发现错误和充当文档方面的作用。与C++等语言不同，Python没有内置的类型检查器，而是依赖于运行时错误或第三方工具。

本文概述了该方法：使用`ast`模块解析Python代码，识别类型注解，并验证类型兼容性。它介绍了`SymbolCollector`类，一个`ast.NodeVisitor`子类，用于查找和保存函数和变量的类型注解。核心逻辑围绕检查赋值和函数调用展开。

本文涵盖了处理原始类型、列表、字典和类型联合等基本方面。它定义了一个兼容性检查(`is_compatible`)，以确保分配的类型与声明的类型匹配。代码示例展示了如何扩展类型检查器以支持各种数据结构和操作，例如索引和字面量的类型推断。它演示了类型检查器如何在示例Python代码片段中识别类型错误。本文引导读者逐步开发类型检查器，强调了类型检查中涉及的挑战和复杂性，并提供了GitHub上完整代码的链接。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 2 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 3 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 4 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 5 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 6 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 7 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 8 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 9 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 10 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 11 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 12 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 13 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 14 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 15 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 16 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 17 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 18 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 19 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 20 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 21 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 22 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 23 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 24 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 25 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 26 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 27 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 28 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 29 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 30 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 31 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 32 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 33 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 34 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 35 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 36 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 37 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 38 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 39 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 40 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 41 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 42 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 43 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 44 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 45 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 46 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 47 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 48 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 49 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 50 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 51 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 52 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 53 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 54 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 55 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 56 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 57 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 58 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 59 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 60 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 61 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 62 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 63 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 64 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 65 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 66 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 67 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 68 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 69 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 70 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 71 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 72 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 73 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 74 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 75 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 76 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 77 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 78 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 79 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 80 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 81 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 82 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 83 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 84 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 85 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 86 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 87 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 88 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 89 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 90 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 91 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 92 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 93 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 94 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 95 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 96 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 97 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 98 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 99 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 100 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 101 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 102 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 103 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 104 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 105 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 106 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 107 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 108 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 109 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 110 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 111 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 112 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 113 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 114 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 115 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 116 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 117 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 118 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 119 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 120 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 121 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 122 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 123 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 124 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 125 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 126 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 127 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 128 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 129 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 130 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 131 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 132 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 133 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 134 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 135 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 136 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 137 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 138 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 139 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 140 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 141 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 142 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 143 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 144 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 145 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 146 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 147 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 148 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 149 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 150 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 151 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 152 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 153 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 154 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 155 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 156 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 157 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 158 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 159 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 160 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 161 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 162 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 163 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 164 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 165 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 166 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 167 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 168 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 169 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 170 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 171 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
