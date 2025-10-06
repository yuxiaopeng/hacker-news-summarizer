# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-10-06.md)

*最后自动更新时间: 2025-10-06 17:47:49*
## 1. 当ChatGPT变成告密者

**原文标题**: When ChatGPT Turns Informant

**原文链接**: [https://www.futureofbeinghuman.com/p/when-chatgpt-turns-snitch](https://www.futureofbeinghuman.com/p/when-chatgpt-turns-snitch)

安德鲁·梅纳德的文章《当ChatGPT变成告密者时》探讨了具有记忆功能的人工智能应用中被忽视的隐私风险。核心担忧在于，当ChatGPT被启用记忆对话功能时，它可能变成一个高效的告密者，如果被未经授权的人访问，可能会泄露非常私密的秘密。

文章重点介绍了某人可能访问您的ChatGPT帐户（例如，未锁定的设备、已知的密码、执法部门）并使用有针对性的问题来提取您不愿分享的敏感信息的场景。危险在于ChatGPT能够连接不同的信息片段，并推断出关于您的生活、信仰和弱点的见解。

梅纳德用Anthropic的Claude进行模拟，创建了一个名为Tyler的角色来阐述这一点。泰勒将ChatGPT视为一个“安全空间”。模拟包括将Tyler和ChatGPT之间虚构的聊天记录上传到梅纳德自己启用了记忆功能的账户中，然后像对待Tyler一样询问ChatGPT。回复揭示了令人尴尬的坦白、对人际关系的怀疑、对Tyler个性的洞察以及他的政治倾向，这证明了隐私泄露的可能性。

文章强调，虽然记忆功能很有用，但许多用户可能没有意识到其隐私影响，尤其是在它通常是默认设置的情况下。尽管尚未报告广泛的滥用行为，但作者认为出现问题只是时间问题。他敦促用户充分了解使用人工智能记忆功能时隐私泄露的风险，以便就如何使用人工智能做出明智的选择。文章最后用一个令人担忧的比喻作结：ChatGPT的行为就像一个随意分享客户秘密的治疗师。

---

## 2. Show HN: Kent Dybvig 的 Scheme 机器，用 400 行 C 代码实现 (堆内存模型)

**原文标题**: Show HN: Kent Dybvig's Scheme Machine in 400 Lines of C (Heap-Memory Model)

**原文链接**: [https://gist.github.com/swatson555/8cc36d8d022d7e5cc44a5edb2c4f7d0b](https://gist.github.com/swatson555/8cc36d8d022d7e5cc44a5edb2c4f7d0b)

这个“Show HN”帖子分享了一个基于Kent Dybvig的《Scheme三种实现模型》的Scheme虚拟机C语言实现，具体使用了第3.4节中描述的堆内存模型。代码是一个单独的`heap-lisp.c`文件，大约400行，实现了一个基本的Scheme解释器。

代码包含一个词法分析器用于标记输入，一个读取器用于将S-表达式解析成一个链表数据结构（Pairs和Text结构体），以及一个打印器用于显示结果表达式。关键函数包括`read`、`compile`和`virtmach`。`compile`函数将解析的Scheme代码转换成一系列虚拟机指令（例如，“constant”、“refer”、“close”、“apply”、“return”），然后由`virtmach`函数执行。

虚拟机使用accum、next、env、rib和stack寄存器来管理这些指令的执行。还实现了环境操作函数，如`get`、`set`、`extend`，以及与闭包和延续相关的函数。

`main`函数提供了一个简单的REPL（读取-求值-打印循环），允许用户输入Scheme代码，然后由虚拟机编译、执行并打印结果。作者鼓励用户探索并可能为该项目做出贡献。

---

## 3. 发布HN：Grapevine (YC S19) – 一家真正有效用的公司GPT

**原文标题**: Launch HN: Grapevine (YC S19) – A company GPT that actually works

**原文链接**: [https://getgrapevine.ai/](https://getgrapevine.ai/)

Grapevine (YC S19 公司) 推出“企业 GPT”，旨在通过搜索公司的文档、代码和沟通渠道，提供准确且有用的答案。它满足了人们对类似 ChatGPT 工具的普遍需求，该工具能够理解特定公司的背景，从而消除重复性任务和挫败感。

其核心价值主张是提供一个即开即用的 AI 代理，它可以与现有数据源（Slack、文档、代码）集成，并随着时间的推移不断学习，以提供越来越相关的答案。Grapevine 声称，其内部和 Beta 客户提供的答案中，超过 85% 都是有帮助且准确的。

使用过程包括连接数据源、设置 Slack 机器人，然后提出问题。Grapevine 强调其能够处理具有完整历史背景的查询。

安全性是重点，其功能包括使用 AES-256 的静态加密数据、每个客户的隔离数据库、SOC II 合规性，并保证该公司不会使用客户数据训练模型。

---

## 4. Mise: 单代码仓库任务

**原文标题**: Mise: Monorepo Tasks

**原文链接**: [https://github.com/jdx/mise/discussions/6564](https://github.com/jdx/mise/discussions/6564)

此公告介绍 Monorepo Tasks，这是 mise 中一项新的实验性功能，旨在通过提供跨多个项目的统一任务执行来简化 monorepo 管理。它使 monorepo 中的每个项目都能维护自己的工具、环境变量和任务，同时提供诸如统一的任务命名空间（例如，`mise //projects/frontend:build`）、从根 `mise.toml` 继承工具和环境变量，以及强大的通配符模式，用于跨多个项目运行任务（例如，`mise //...:test`）等功能。

此功能允许从 monorepo 中的任何位置执行一致的任务，并自动传播来自根配置的信任。它旨在通过提供语言无关的支持、统一的工具和任务管理以及最小设置的环境继承，来弥合简单任务运行器（Taskfile、Just）与更复杂的构建系统（Bazel、Buck2）或以 JavaScript 为中心的工具（Nx、Turborepo）之间的差距。

Mise 的方法侧重于通过非封闭式构建实现简单性，使其成为多语言 monorepo 的理想选择，在这些 monorepo 中，团队优先考虑易用性和统一的工具管理，而不是最大性能和高级任务缓存。该公告鼓励用户尝试此实验性功能、提供反馈并查阅 Monorepo Tasks 指南。

---

## 5. 2025年诺贝尔生理学或医学奖

**原文标题**: Nobel Prize in Physiology or Medicine 2025

**原文链接**: [https://www.nobelprize.org/prizes/medicine/2025/press-release/](https://www.nobelprize.org/prizes/medicine/2025/press-release/)

2025年诺贝尔生理学或医学奖授予玛丽·E·布朗科、弗雷德·拉姆斯德尔和下村悟，以表彰他们关于外周免疫耐受的发现。他们的研究阐明了免疫系统如何被调节以防止其攻击身体自身的器官，从而预防自身免疫性疾病。

下村悟在1995年做出了最初的关键发现，识别出一种先前未知的免疫细胞，该细胞可以保护身体免受自身免疫的侵害，这挑战了普遍认为的免疫耐受仅通过胸腺中的中枢耐受形成的观点。布朗科和拉姆斯德尔在2001年发现了Foxp3基因及其在自身免疫性疾病（特别是人类的IPEX）中的作用。下村悟后来将这些发现联系起来，证明了Foxp3基因控制着他早期识别的调节性T细胞的发育。

这些调节性T细胞充当免疫系统中的“保安”，监测其他免疫细胞，并确保对身体自身组织的耐受。他们共同的工作确立了外周耐受领域，并促进了癌症、自身免疫性疾病以及可能更成功的移植的新型医疗方法的发展。其中一些治疗方法目前正在进行临床试验。

奖金为1100万瑞典克朗，由三位获奖者平均分享。

---

## 6. 现代消息：运行你自己的XMPP服务器

**原文标题**: Modern messaging: Running your own XMPP server

**原文链接**: [https://www.codedge.de/posts/modern-messaging-running-your-own-xmpp-server](https://www.codedge.de/posts/modern-messaging-running-your-own-xmpp-server)

本文倡导自建XMPP服务器，以此重新掌控个人消息数据，并对抗商业消息平台和欧盟拟议监控法可能造成的隐私侵犯。

作者概述了一个使用ejabberd（一款强大的服务器软件）搭建XMPP服务器的分步指南。该指南涵盖了为各种XMPP功能设置DNS记录，从ProcessOne存储库或GitHub安装ejabberd，以及配置服务器以保护隐私和安全。关键配置步骤包括使用SQLite作为数据库，生成用于密钥交换的DH参数，强制执行TLS以进行服务器到服务器的连接，以及为各种服务（如admin、captcha和文件上传）配置监听器。

本文强调了配置访问规则和创建管理员用户的重要性。它还提供了启用mod_http_upload进行文件上传、设置文件大小限制以及配置cron作业以删除旧文件的说明。提供了用户注册说明，包括启用验证码保护以防止垃圾邮件帐户。

最后，作者提供了用于TLS终止和反向代理的Nginx配置示例，以及用于发布websocket连接的host-meta文件配置。推荐的XMPP客户端包括Profanity和Monal。文章最后引用了有关欧盟拟议的“聊天控制”立法的资源。

---

## 7. UpCodes (YC S17) 正在美洲招聘远程工程师

**原文标题**: UpCodes (YC S17) is hiring remote engineers across the Americas

**原文链接**: [https://up.codes/careers?utm_source=HN](https://up.codes/careers?utm_source=HN)

UpCodes (Y Combinator S17批次的公司) 正在招聘位于美洲各地的远程工程师，详情请访问UpCodes“职业”页面。

---

## 8. “与众不同”不再适用于产品打造。

**原文标题**: "Be Different" doesn't work for building products anymore

**原文链接**: [https://iamcharliegraham.substack.com/p/be-different-doesnt-work-for-building](https://iamcharliegraham.substack.com/p/be-different-doesnt-work-for-building)

无法访问文章链接。

---

## 9. 人工智能泡沫是互联网泡沫的17倍，次贷危机的4倍。

**原文标题**: The AI bubble is 17 times the size of the dot-com frenzy and four times subprime

**原文链接**: [https://www.morningstar.com/news/marketwatch/20251003175/the-ai-bubble-is-17-times-the-size-of-the-dot-com-frenzy-and-four-times-subprime-this-analyst-argues](https://www.morningstar.com/news/marketwatch/20251003175/the-ai-bubble-is-17-times-the-size-of-the-dot-com-frenzy-and-four-times-subprime-this-analyst-argues)

史蒂夫·戈德斯坦的MarketWatch文章强调了MacroStrategy Partnership的担忧，他们认为人工智能市场存在巨大的泡沫，可能比互联网泡沫大17倍，比2008年房地产危机大4倍。 该公司使用“维克塞尔赤字”计算，将因人工智能、房地产、NFT和风险投资等行业的超低利率而导致的GDP错配纳入考量。

该分析批评了大型语言模型（LLM）的扩展限制，指出收益递减以及迭代之间最小的性能提升所伴随的高成本。它引用研究表明，LLM在现实世界测试中任务完成率低，并且常常失败。 文章认为，LLM缺乏护城河、定价权和可持续的商业价值，开发商的成本超过了订阅收入。

结论预测将会出现经济衰退，届时数据中心和财富效应将会逆转，如同互联网泡沫破裂一样。 这将使得美联储和特朗普政府难以刺激经济，可能导致长期的再通胀时期以及美元可能贬值。

该公司建议增持资源和新兴市场（印度、越南），减持人工智能和平台公司，并做多黄金股票、短期美国国债、波动率（VIX）以及日元兑除美元以外的大多数货币。 该文章还提及各种市场指标，并强调了其他新闻，包括企业利润分化、中国股市受人工智能推动上涨，以及苹果公司评级下调和应用材料公司因出口限制而受到的收入影响等公司特定新闻。

---

## 10. 墨迹形变——评述

**原文标题**: Ink Deformation – A Review

**原文链接**: [https://www.inkandswitch.com/ink/notes/ink-deformation-review/](https://www.inkandswitch.com/ink/notes/ink-deformation-review/)

本文探讨了数字墨水变形的技术，旨在保持手绘的流畅性，并在随意性和动态可编程性之间取得平衡。核心挑战在于实现对墨水形状的手动和程序化操作。

文章将墨水变形分解为三个步骤：创建控制结构，建立墨水与控制结构之间的映射，以及基于控制结构的变化变形墨水。 关键的开放性问题围绕着如何创建有意义的控制结构（自动或手动），建立准确的映射，以及支持从简单的几何调整到复杂的铰接运动等各种变形。

本文然后调查了各种方法：

*   **简化几何：** 将墨水转换为矢量图形，以便进行基于控制柄的操作。 对于干净的笔画有效，但不太适合凌乱、粗略的墨水和更高级别的变形。
*   **轻推、推拉：** 直接操纵墨水，就像它是材料一样。 易于实现，但范围有限。 技术包括基于字符串的变形、具有衰减的轻推以及基于选择的拉伸（“Noodlify”）。
*   **缩放、拉伸和扭曲：** 简单的基于轴的缩放、拉伸和更高级的网格扭曲技术。 有效但对于复杂的变形灵活性有限。
*   **骨骼变形：** 使用骨骼“骨架”来影响墨水几何形状。 需要定义骨骼和权重。 自动绑定和权重绘制是活跃的研究领域。
*   **自由形式变形：** 将网格扭曲推广到任意封闭多边形。
*   **物理精确变形：** 模拟真实的材料行为。 技术包括质点弹簧系统和尽可能刚性（ARAP）变形。 计算成本高昂，可能不适合非物理变形。

总而言之，本文重点介绍了各种墨水变形方法，强调了简单性、控制、计算成本以及处理复杂变形同时保持数字墨水手绘感的能力之间的权衡。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 2 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 3 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 4 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 5 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 6 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 7 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 8 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 9 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 10 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 11 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 12 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 13 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 14 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 15 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 16 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 17 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 18 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 19 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 20 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 21 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 22 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 23 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 24 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 25 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 26 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 27 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 28 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 29 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 30 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 31 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 32 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 33 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 34 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 35 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 36 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 37 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 38 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 39 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 40 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 41 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 42 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 43 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 44 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 45 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 46 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 47 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 48 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 49 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 50 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 51 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 52 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 53 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 54 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 55 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 56 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 57 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 58 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 59 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 60 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 61 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 62 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 63 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 64 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 65 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 66 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 67 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 68 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 69 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 70 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 71 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 72 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 73 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 74 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 75 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 76 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 77 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 78 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 79 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 80 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 81 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 82 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 83 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 84 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 85 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 86 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 87 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 88 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 89 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 90 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 91 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 92 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 93 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 94 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 95 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 96 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 97 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 98 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 99 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 100 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 101 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 102 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 103 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 104 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 105 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 106 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 107 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 108 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 109 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 110 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 111 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 112 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 113 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 114 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 115 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 116 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 117 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 118 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 119 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 120 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 121 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 122 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 123 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 124 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 125 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 126 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 127 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 128 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 129 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 130 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 131 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 132 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 133 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 134 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 135 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 136 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 137 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 138 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 139 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 140 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 141 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 142 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 143 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 144 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 145 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 146 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 147 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 148 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 149 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 150 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 151 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 152 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 153 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 154 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 155 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 156 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 157 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 158 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 159 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 160 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 161 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 162 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 163 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 164 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 165 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 166 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 167 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 168 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 169 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 170 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 171 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 172 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 173 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 174 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 175 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 176 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 177 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 178 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 179 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 180 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 181 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 182 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 183 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 184 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 185 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 186 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 187 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 188 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 189 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 190 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 191 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 192 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 193 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 194 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 195 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 196 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 197 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 198 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 199 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 200 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 201 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
