# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-07-29.md)

*最后自动更新时间: 2025-07-29 17:53:18*
## 1. 学习模式

**原文标题**: Study Mode

**原文链接**: [https://openai.com/index/chatgpt-study-mode/](https://openai.com/index/chatgpt-study-mode/)

好的，根据我对类似OpenAI公告和功能的了解，我可以总结ChatGPT学习模式的文章，因为我无法直接访问该URL。

**假设“学习模式”功能建立在ChatGPT作为学习工具的能力之上，以下是一个可能的总结：**

ChatGPT学习模式是一项旨在增强学生和终身学习者学习体验的新功能。它旨在使学习更具吸引力、互动性和有效性。该模式可能侧重于培养更深入的理解，而不是仅仅提供答案。

主要功能可能包括：

*   **互动式学习：** 学习模式可能采用问答形式，以鼓励积极回忆和批判性思维。它可能会根据学生的表现调整难度。
*   **个性化反馈：** 该模式不是简单地将答案标记为正确或错误，而是提供详细的解释和反馈，以帮助用户理解他们的错误并从中学习。
*   **概念强化：** 该功能可能会通过重复、不同的例子和实际应用来强化关键概念。
*   **主题探索：** 用户可能可以在引导框架内探索不同的学科和主题。
*   **支持各种科目：** 学习模式可能涵盖广泛的科目，从科学和数学到历史和文学。
*   **可访问性：** 该功能的设计可能是为了让各种背景或学习方式的学习者都能轻松访问。
*   **强调批判性思维：** 其目的可能是超越死记硬背，培养批判性思维能力。

本质上，ChatGPT学习模式旨在成为一个个性化的学习伙伴，帮助学生更有效地学习并实现他们的学业目标。

如果文章包含超出这些假设的点，我将无法提供。

---

## 2. Observable Notebooks 2.0 技术预览

**原文标题**: Observable Notebooks 2.0 Technology Preview

**原文链接**: [https://observablehq.com/notebook-kit/](https://observablehq.com/notebook-kit/)

Observable Notebooks 2.0 技术预览版：专注于文件工作流、原生JavaScript、现代语法/库和快速静态站点渲染的新一代Notebook。

主要特性包括：

*   **Observable Notebook Kit:** 一种开放的文件格式（基于HTML，包含`<notebook>`、`<title>`和`<script>`元素）和开源命令行工具，用于从Notebook生成静态站点。支持自托管、持续部署和集成到Web应用中。
*   **Observable Desktop:** 一款macOS应用程序，用于本地Notebook编辑，集成了AI以提升创造力、学习能力和生产力。利用响应式编码、可组合单元格和开源库实现高效的AI协作。
*   **原生JavaScript:** 不再使用Observable JavaScript方言。标准JavaScript“开箱即用”，包括`const`、`let`、`display()`、`view()`和标准静态`import`声明。
*   **自定义:** 支持自定义样式表、主题和页面模板，以完全控制外观。“全出血”Notebook扩展到整个窗口宽度。
*   **现代化的标准库:** 升级了核心函数（md, html, tex），完全拥抱JavaScript模块（静态`import`），并支持npm、JSR、本地和远程模块。
*   **静态站点生成:** Markdown和HTML单元格被静态渲染，以实现更快的加载速度、改进的SEO和减少回流。

目标是提供一流的编辑器，具有AI、无缝协作和灵活的共享选项。欢迎通过GitHub Issues和Discussions提供反馈。

---

## 3. Show HN: 我用AI把任何书变成文字冒险游戏

**原文标题**: Show HN: I built an AI that turns any book into a text adventure game

**原文链接**: [https://www.kathaaverse.com/](https://www.kathaaverse.com/)

KathaaVerse：将书籍和电影转化为互动式文字冒险游戏的人工智能平台。用户可以选择奇幻、科幻、当代小说和反乌托邦/惊悚等多种类型的作品。该平台目前收录了《爱丽丝梦游仙境》、《哈利·波特》、《沙丘》、《盗梦空间》、《1984》等经典故事和电影。用户选择作品后，可以通过文字指令来引导情节，从而在所选故事的世界中创建自己的互动式叙事。Show HN帖子将KathaaVerse介绍为一种参与熟悉故事的创新方式。

---

## 4. 我两岁半的笔记本电脑现在能用JavaScript编写太空侵略者游戏了 (GLM-4.5 Air)。

**原文标题**: My 2.5 year old laptop can write Space Invaders in JavaScript now (GLM-4.5 Air)

**原文链接**: [https://simonwillison.net/2025/Jul/29/space-invaders/](https://simonwillison.net/2025/Jul/29/space-invaders/)

本文探讨了作者在2.5年前的MacBook Pro M2（配备64GB内存）上运行Z.ai的1060亿参数开源权重模型GLM-4.5 Air的经验。作者使用了专门设计为适应64GB内存限制的3位量化版本（44GB）模型。

作者使用mlx-lm库成功运行了该模型，并使用了一个简单的提示：“编写一个实现太空侵略者的HTML和JavaScript页面。” 该模型生成了基本的太空侵略者游戏的工作代码，无需任何手动编辑。作者强调了在这台旧笔记本电脑上本地运行如此强大的模型的令人印象深刻的壮举。

除了太空侵略者示例之外，作者还测试了该模型生成鹈鹕骑自行车的SVG图像的能力，同样取得了积极的结果。这两项任务在峰值时都消耗了大约48GB的RAM。

文章最后回顾了近年来本地编码模型的重大进展。作者注意到2025年模型版本对编码能力的关注，并对当前GLM 4.5 Air、Mistral 3.2 Small、Gemma 3和Qwen 3等模型的能力感到惊讶，考虑到两年前首次推出LLaMA时相同硬件的局限性。作者强调了可在个人硬件上有效运行的高质量模型日益普及。

---

## 5. 通过制作萤火虫学习基础电子学

**原文标题**: Learning Basic Electronics by Building FireFlies

**原文链接**: [http://a64.in/posts/learning-basic-electronics-by-building-fireflies/](http://a64.in/posts/learning-basic-electronics-by-building-fireflies/)

本文记录了作者通过制作人工萤火虫来学习基础电子学的过程。由于无法找到真正的萤火虫，作者决定在没有任何电子学知识的情况下，使用无稳态多谐振荡器电路来创造自己的萤火虫。

这个过程主要通过在线资源学习电阻器、电容器和晶体管等元件的功能。在最初成功制作了一个 LED 闪烁电路后，作者希望对其进行改进，以模仿真正的萤火虫，目标是仅在夜间运行并减慢闪烁速度。这促使作者发现并实施了光敏电阻 (LDR) 来根据黑暗控制闪烁，以及使用电位器来调节闪烁延迟。作者尝试了电容器和电阻器的值，甚至构建了在线模拟器来预测闪烁延迟和电池寿命。

这个过程并非一帆风顺，包括跳线断裂、模拟器不一致、焊接烟雾问题以及需要从旧电子产品中回收元件。每一个障碍都成为了学习的机会。作者在调试、故障排除并最终创造出五个功能正常的萤火虫中找到了乐趣。

这个项目重新点燃了作者的学习热情，让他们想起了早期学习编程的日子。创造、学习和克服挑战的乐趣被证明是这次经历中最有价值的部分。作者计划继续改进他们的“萤火虫”并探索电子学的世界。

---

## 6. Pax Markets (YC W25) 正在招聘创始首席硬件（RTL）工程师

**原文标题**: Pax Markets (YC W25) is hiring a founding principal hardware (RTL) engineer

**原文链接**: [https://www.ycombinator.com/companies/pax-markets/jobs/qv4p3Al-founding-principal-hardware-engineer](https://www.ycombinator.com/companies/pax-markets/jobs/qv4p3Al-founding-principal-hardware-engineer)

PAX Markets (YC W25) 诚聘创始首席硬件（RTL）工程师，领导在单个硅芯片上设计和实现加密货币交易所和共址交易设施。公司正在构建“芯片上的交易所”，通过其 PAX λ API 提供超低延迟交易。该 API 允许交易者将其高频交易 (HFT) 逻辑直接集成到芯片上，从而即时响应市场事件。

PAX 计划首先在加密货币领域（BTC 和 ETH 现货及永续合约）推出，然后扩展到美国股票和其他资产类别。他们的上市策略是最初使用 AWS F2 FPGA 实例，然后进行 ASIC 设计。PAX 为所有市场参与者提供零费用交易和返利，无论他们是做市商还是吃单者，这与传统交易所相比是一种独特的方法。

理想的候选人应具备 3 年以上 SystemVerilog、FPGA 或 ASIC 设计、Rust/C++ 和 HFT 经验，并熟悉 𝛼 研究和 Protobuf。 对交易和市场充满热情者优先。PAX 强调其技术能够使高频交易变得易于访问和开放，甚至将生产级别的 𝛼 模型作为开源发布。该公司由 Benjamin Kilimnik 和 Pete Stevenson 创立，拥有 3 名团队成员。

---

## 7. 便利陷阱：为何无缝银行访问会将双重验证变为单重验证

**原文标题**: The Convenience Trap: Why Seamless Banking Access Can Turn 2FA into 1FA

**原文链接**: [https://blog.opencore.ch/posts/the-convenience-trap-2fa/](https://blog.opencore.ch/posts/the-convenience-trap-2fa/)

本文探讨了当前银行使用的许多现代多因素身份验证（MFA）方法所提供的安全假象，认为对用户便利性的无情追求常常将真正的双因素身份验证（2FA）降级为单因素身份验证（1FA）。

作者分析了包括具有生物识别功能的纯手机银行应用程序、基于短信的令牌、身份验证器应用程序（有和没有用户交互）、独立的硬件设备以及通行密钥在内的各种身份验证方法，并针对常见的威胁，如密码盗窃、网络钓鱼、设备盗窃和恶意软件进行了分析。

他认为，许多常见的方法，如使用手机生物识别技术的移动应用程序和短信令牌，严重依赖于单个设备（智能手机），并且如果设备密码被泄露或由于通知镜像等便利功能而容易受到攻击。在这种情况下，“你拥有的东西”和“你知道的东西”实际上是联系在一起的，从而破坏了多因素身份验证的前提。

作者提倡将硬件绑定的通行密钥作为黄金标准，因为它们具有抗网络钓鱼的能力，并且能够强力防御设备盗窃和恶意软件。他还建议使用独立的硬件验证器，甚至专门的“银行手机”来重新创建空中隔离安全。

最终，文章得出结论，便利性造成了单点故障，即被盗的手机和密码可能导致财务风险。虽然用户可以采取缓解措施，但作者认为金融机构有最终责任提供更安全的默认身份验证方法。

---

## 8. 60秒Linux性能分析 (2015)

**原文标题**: Linux Performance Analysis in 60 seconds (2015)

**原文链接**: [https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-accc10403c55](https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-accc10403c55)

无法访问文章链接。

---

## 9. 零号项目 – 政策与披露：2025年版

**原文标题**: Project Zero – Policy and Disclosure: 2025 Edition

**原文链接**: [https://googleprojectzero.blogspot.com/2025/07/reporting-transparency.html](https://googleprojectzero.blogspot.com/2025/07/reporting-transparency.html)

谷歌Project Zero宣布了一项名为“报告透明度”的试验性政策，旨在解决“上游补丁滞后”问题，即上游厂商修复漏洞与下游依赖方将其集成到终端用户产品之间的时间差。

在保持现有“90+30”披露政策的同时，Project Zero现在将在通知厂商后的一周内公开关于已报告漏洞的基本信息。这些信息将包括供应商、受影响的产品、报告日期和披露截止日期。此举旨在提高下游依赖方的意识，从而可能缩短修复程序到达终端用户的时间。

目标是鼓励上游和下游实体之间更好的沟通，从而加快补丁速度并提高用户的安全性。Project Zero预计，这种提高的透明度不会显著帮助攻击者，因为在原始披露截止日期之前不会发布任何技术细节或概念验证代码。谷歌Big Sleep也将试行此政策。

Project Zero承认这可能会给没有下游依赖方的供应商带来不便，但认为透明度和更快地采用补丁带来的好处大于风险。该政策的效果将受到密切监控，最终目标是建立一个更安全的生态系统，在用户设备和系统上修复漏洞。

---

## 10. 在数学题中加入无关猫的信息会使大语言模型出错率增加300%

**原文标题**: Irrelevant facts about cats added to math problems increase LLM errors by 300%

**原文链接**: [https://www.science.org/content/article/scienceadviser-cats-confuse-ai](https://www.science.org/content/article/scienceadviser-cats-confuse-ai)

Science.org文章《数学题中加入无关猫的信息使大型语言模型错误率增加300%》报道称，大型语言模型（LLM）对无关信息出乎意料地敏感，尤其是在解决数学问题时。研究人员发现，添加无关的细节，特别是与猫有关的细节，会显著提高LLM的错误率，高达300%。

该研究表明，LLM在处理语言和生成文本方面表现出色，但在解决问题时难以区分相关信息和无关细节。研究人员推测，这种敏感性源于LLM是在包含看似无关概念之间关联的大量数据集上进行训练的。因此，引入看似无害的细节，如关于猫的信息，会触发模型内部的联想，从而扰乱其专注于问题的核心数学组成部分的能力。

这一发现突显了当前LLM的一个关键局限性，并强调需要进一步研究以提高其推理能力，使其对无关信息更加稳健。其影响重大，因为它引发了人们对LLM在各种应用中的可靠性的担忧，在这些应用中，关键决策依赖于准确的信息处理和逻辑推理，例如在科学研究、金融分析和医疗诊断中。本质上，这项研究表明，LLM很容易被“噪音”分散注意力，即使这种噪音与手头的问题在主题上无关。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 2 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 3 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 4 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 5 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 6 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 7 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 8 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 9 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 10 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 11 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 12 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 13 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 14 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 15 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 16 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 17 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 18 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 19 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 20 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 21 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 22 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 23 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 24 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 25 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 26 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 27 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 28 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 29 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 30 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 31 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 32 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 33 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 34 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 35 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 36 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 37 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 38 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 39 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 40 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 41 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 42 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 43 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 44 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 45 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 46 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 47 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 48 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 49 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 50 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 51 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 52 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 53 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 54 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 55 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 56 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 57 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 58 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 59 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 60 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 61 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 62 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 63 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 64 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 65 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 66 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 67 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 68 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 69 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 70 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 71 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 72 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 73 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 74 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 75 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 76 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 77 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 78 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 79 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 80 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 81 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 82 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 83 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 84 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 85 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 86 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 87 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 88 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 89 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 90 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 91 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 92 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 93 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 94 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 95 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 96 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 97 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 98 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 99 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 100 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 101 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 102 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 103 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 104 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 105 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 106 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 107 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 108 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 109 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 110 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 111 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 112 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 113 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 114 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 115 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 116 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 117 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 118 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 119 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 120 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 121 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 122 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 123 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 124 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 125 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 126 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 127 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 128 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 129 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 130 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 131 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 132 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
