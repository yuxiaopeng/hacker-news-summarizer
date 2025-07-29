# Hacker News 热门文章摘要 (2025-07-29)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 展示一下：ELF注入器

**原文标题**: Show HN: ELF Injector

**原文链接**: [https://github.com/dillstead/elf_injector](https://github.com/dillstead/elf_injector)

本文是一篇“Show HN”帖子，介绍了`elf_injector`，一个可以将可重定位的代码块注入到32位ARM系统上的ELF可执行文件中的工具。被注入的代码会在原始入口点之前运行。

帖子详细介绍了`elf_injector`和示例代码块（`greeting`、`startup_dump`、`copy_chunk`）的构建过程。它解释了如何使用`elf_injector`，通过命令行参数指定目标可执行文件、代码块文件以及代码块中的入口点偏移。

被注入的代码是位置无关的，不能依赖于绝对地址或标准库。本文提供了创建这种可重定位代码的技术，包括使用系统调用、嵌入静态数据（通过手动编辑汇编或使用堆栈字符串）以及确定入口偏移。

`elf_injector`的工作原理是利用ELF可执行文件的文本段和数据段之间的填充空间。对于较大的代码块，会在填充空间中插入一个小的*短桩程序*。这个短桩程序会定位、内存映射并执行代码块，通过`inject_info`结构体传递信息（包含代码块的位置、长度和入口偏移）。代码块执行完毕后，短桩程序会跳转到原始入口点。本文包含短桩程序的汇编代码。

示例代码块演示了诸如打印“Hello World”、转储命令行参数和环境变量，甚至将注入器的副本注入到其他可执行文件中的功能。

---

## 12. Coverage.py 的正则表达式指令

**原文标题**: Coverage.py Regex Pragmas

**原文链接**: [https://nedbatchelder.com/blog/202507/coveragepy_regex_pragmas.html](https://nedbatchelder.com/blog/202507/coveragepy_regex_pragmas.html)

Coverage.py 使用正则表达式来识别要从覆盖率测量中排除的代码，从而提供了一种灵活的替代方案，以取代固定的语法编译指示。这允许排除匹配定义模式的行、多行语句或整个代码块。最初用于简单的编译指示注释，后来发展为支持无编译指示的排除，例如忽略所有 `__repr__` 方法。

第三方插件进一步扩展了这一点，能够基于环境实现平台特定的排除或注释语法。一项重大改进允许正则表达式匹配多行模式，从而实现更强大的排除，例如排除整个文件或由“start”和“end”注释分隔的代码块。

虽然功能强大，但正则表达式方法并不完美，在处理包含编译指示文本的字符串文字时会遇到困难，或者需要复杂的模式来避免误报，排除空占位符方法的工作就证明了这一点。尽管存在这些局限性，但基于正则表达式的方法在灵活性和强大性之间取得了宝贵的平衡，证明在配置实际场景中的代码排除方面非常有效。

---

## 13. 现在我将入眠 (1927)

**原文标题**: Now I Lay Me (1927)

**原文链接**: [https://storyoftheweek.loa.org/2025/07/now-i-lay-me.html](https://storyoftheweek.loa.org/2025/07/now-i-lay-me.html)

本文介绍了欧内斯特·海明威的短篇小说《现在我躺下祈祷》，重点介绍了其与海明威在第一次世界大战期间自身经历的半自传式联系。1918年，海明威在意大利担任红十字会志愿者时身负重伤，这件事深刻地影响了他的生活和作品。

《现在我躺下祈祷》以海明威笔下反复出现的人物尼克·亚当斯为主角，探讨了战争带来的创伤和战后应对机制的主题。故事讲述了尼克躺在蚕室的地板上，本文概述了该故事如何被广泛解读为反映了海明威的战后压力和失眠。

本文承认了一种普遍的倾向，即认为尼克·亚当斯是海明威的直接替身，尤其是在这个故事中，并指出一些学者指出，早期草稿中尼克被称为“厄尼”是自传式联系的证据。它还强调了与另一篇故事《在异乡》的关系，该故事也以米兰的一名受伤士兵为主角。然而，它也告诫人们不要进行过于字面的解读，强调并非故事的所有元素都可以直接证实为个人历史。本文强调，虽然存在自传元素，但这个故事也应被视为具有自身艺术价值的虚构作品。

本文通过提及海明威的经历和相关的历史细节来提供背景信息。它还提供了相关资源的链接，并提供《现在我躺下祈祷》的全文供免费阅读。本文最后提到该选段在课堂和教育方面的用途。

---

## 14. Pony：一种actor模型、具备能力安全、高性能的编程语言

**原文标题**: Pony: An actor-model, capabilities-secure, high-performance programming language

**原文链接**: [https://www.ponylang.io/discover/](https://www.ponylang.io/discover/)

Pony：高性能、高安全性并发编程语言简介

---

## 15. Show HN: Terminal-Bench-RL：用强化学习训练长程终端代理

**原文标题**: Show HN: Terminal-Bench-RL: Training Long-Horizon Terminal Agents with RL

**原文链接**: [https://github.com/Danau5tin/terminal-bench-rl](https://github.com/Danau5tin/terminal-bench-rl)

本项目“Show HN”介绍Terminal-Bench-RL，一个专注于使用强化学习(RL)训练长期、基于终端的编程智能体的项目。作者成功构建了可扩展到32x H100 GPU的稳定RL训练基础设施，用于训练Qwen3-32B。该智能体在未经训练的情况下，在Terminal Bench排行榜上取得了Qwen3智能体中的最高分。

该项目使用自定义环境和基础设施扩展了rLLM框架，用于终端智能体训练。一个关键方面是开发了特定工具（待办事项管理、文件操作、搜索工具、Bash执行、草稿纸、任务完成）来帮助智能体完成复杂的编码任务，以及鼓励结构化解决问题的系统提示。该智能体通过结构化的XML/YAML进行通信，以实现类型安全和错误恢复。

奖励系统结合了使用Python单元测试进行答案验证（65%权重）和LLM作为裁判（Claude-4-Sonnet，35%权重）来评估动作输出、规划、阶段遵守和工具使用。作者评估了多个LLM裁判，突出了Claude Sonnet 4的卓越表现。支持动态LLM裁判切换，以处理API限制和性能问题。

该项目集成了rLLM的架构，使用`TerminalBenchAgent`和`DockerIsolatedEnv`进行智能体-环境交互。训练利用具有可配置数量rollout的群体相对策略优化(GRPO)。该基础设施为不同的硬件设置提供了训练配置预设，并包含一个使用多智能体合成数据管道生成和验证的包含331个任务的数据集。

---

## 16. 变量名对AI代码补全重要吗？（2025）

**原文标题**: Do variable names matter for AI code completion? (2025)

**原文链接**: [https://yakubov.org/blogs/2025-07-25-variable-naming-impact-on-ai-code-completion](https://yakubov.org/blogs/2025-07-25-variable-naming-impact-on-ai-code-completion)

本研究（2025年）调查了变量命名风格对AI代码补全模型性能的影响。该实验测试了8种不同的AI模型，参数规模从0.5B到8B不等，使用了500个Python代码样本，这些样本被转换为7种不同的命名约定：描述性、标准风格（snake_case、PascalCase、SCREAM_SNAKE_CASE）、极简和混淆。模型为每个样本补全了25个token，性能通过完全匹配、莱文斯坦相似度和由LLM判断的语义正确性来衡量。

结果表明，描述性变量名能够显著提高AI代码补全的性能。在所有模型中，描述性名称始终优于其他命名风格，实现了更高的完全匹配率（34.2% vs. 混淆型的16.6%）、更高的莱文斯坦相似度（0.786 vs. 0.666）以及更好的语义相似度（0.874 vs. 0.802）。清晰的性能排名结果为：描述性 > SCREAM_SNAKE_CASE > snake_case > PascalCase > 极简 > 混淆。

虽然描述性名称使用的token数量多出41%，但其语义性能提升了8.9%，表明AI模型优先考虑清晰性而非token压缩。研究结果表明，在代码中使用描述性变量名可以显著提高AI代码补全的性能，这与人类可读性的最佳实践相一致，并表明清晰的命名有利于人类和AI。这种模式适用于不同的模型架构。

---

## 17. 盐鳄：桌面型软胶囊注射成型机

**原文标题**: The Saltgator: A Desktop SoftGel Injection Molding Machine

**原文链接**: [https://www.core77.com/posts/137875/The-Saltgator-A-Desktop-SoftGel-Injection-Molding-Machine](https://www.core77.com/posts/137875/The-Saltgator-A-Desktop-SoftGel-Injection-Molding-Machine)

Core77文章介绍了一种名为“Saltgator”的桌面式软胶囊注射成型机，该机器旨在制作软塑料制品，如手柄和外壳。Saltgator面向已熟悉硬塑料3D打印机的用户，使他们能够扩展其能力以包含柔性材料。

该机器将软塑料（从Saltgator或其他供应商处购买）模制成体积高达250mL、长度达276mm的部件。该过程包括加热材料、将其注入模具（树脂或3D打印）并固化，整个过程大约需要15分钟，其中固化仅需3分钟。注射由内置注射器促进。

Saltgator已在Kickstarter上成功获得资金，售价为230美元。预计发货日期为九月。文章通过一张展示成型过程的图片突出了其易用性。文章结尾是典型的Core77特色：订阅其新闻通讯的号召以及工业设计公司目录。

---

## 18. 使用 Biff 构建大型 Clojure 代码库

**原文标题**: Structuring large Clojure codebases with Biff

**原文链接**: [https://biffweb.com/p/structuring-large-codebases/](https://biffweb.com/p/structuring-large-codebases/)

本文概述了Jacob O'Bryant基于重写Yakread的经验，使用Biff框架构建大型Clojure代码库的方法。他重点介绍了三个主要的架构改进：

1.  **物化视图：** 为了解决慢查询（如订阅页面），他为XTDB实现了物化视图，存储在RocksDB中。纯粹的“反规范化器”函数将XTDB事务日志条目和RocksDB状态转换为RocksDB的键值对。Biff处理设置和一致性。他使用Fugato生成测试数据，并与“oracle”函数进行比较以进行验证。

2.  **将应用逻辑与副作用分离：** 为了确保代码的纯洁性，具有应用逻辑的函数被设计为状态机。这些机器在纯计算单元和副作用处理程序之间交替。纯逻辑返回描述副作用（如HTTP请求或数据库保存）的数据，从而触发到有副作用状态的转换。这种集中化简化了测试并增强了可观察性。

3.  **Pathom：** 代码库使用Pathom解析器构建。他使用Pathom分离模型和视图代码。GET请求处理程序定义Pathom查询，中间件运行查询，并将结果传递给处理程序函数。这使得请求处理程序保持专注和纯粹。Pathom解析器还生成UI片段，保持各个解析器的小型和可管理性。他将Pathom比作OOP中的模型代码概念，但强调其模型代码和应用程序代码的分离。

O'Bryant计划在完成Yakread重写后，提取并发布这些功能作为Biff的一部分。

---

## 19. 维基媒体基金会质疑英国网络安全法案条例

**原文标题**: Wikimedia Foundation Challenges UK Online Safety Act Regulations

**原文链接**: [https://wikimediafoundation.org/news/2025/07/17/wikimedia-foundation-challenges-uk-online-safety-act-regulations/](https://wikimediafoundation.org/news/2025/07/17/wikimedia-foundation-challenges-uk-online-safety-act-regulations/)

维基媒体基金会将就英国《网络安全法案》(OSA)分类条例于2025年7月22日至23日在伦敦高等法院提起诉讼。基金会认为，这些条例可能会迫使维基百科履行一级义务，即《网络安全法案》中最严格的义务，从而危及其志愿者贡献者并阻碍其运营。

基金会认为，这些条例将要求进行身份验证，从而损害志愿者的隐私和安全，并可能使他们面临数据泄露、跟踪或法律后果等风险。它还会转移资源，使其无法用于维护百科全书的准确性和可访问性。

一位居住在英国的维基百科志愿者贡献者，用户：Zzuuzz，也加入了此次挑战，以强调这些条例对个人贡献者隐私权、安全、言论自由和结社自由的潜在影响。这是首次有志愿者参与的针对《网络安全法案》分类条例的法律挑战。

维基媒体基金会并非要挑战整个《网络安全法案》，而是专门针对可能迫使维基百科承担一级义务的分类条例。他们认为，维基百科作为一个全球数百万用户依赖的重要非营利性知识资源，不应受到为风险更高的商业网站设计的规则的约束。他们希望法院能够通过做出有利于他们的裁决来保护维基百科的志愿者和开放互联网。此案的结果可能会为保护在线公共利益项目树立全球先例。

---

## 20. 学习比你想象的更慢

**原文标题**: Learning Is Slower Than You Think

**原文链接**: [https://nisheethvishnoi.substack.com/p/learning-is-slower-than-you-think](https://nisheethvishnoi.substack.com/p/learning-is-slower-than-you-think)

无法访问文章链接。

---

## 21. Show HN: Xorq – AI开放计算目录

**原文标题**: Show HN: Xorq – open compute catalog for AI

**原文链接**: [https://github.com/xorq-labs/xorq](https://github.com/xorq-labs/xorq)

Xorq 是一个旨在简化和改进 ML 管道开发和部署的开源框架。它解决了诸如混合使用 pandas 和 SQL、浪费计算、手动部署流程、调试沿袭、引擎锁定和可重复性问题等常见痛点。

Xorq 提供了一个统一的、声明式的 API，可以通过 pandas 风格的语法和 Ibis 访问，从而促进 DuckDB、Snowflake 和 DataFusion 等各种引擎之间的可重用计算。主要功能包括基于表达式哈希的透明缓存、表达式的轻松部署、用于调试的可视化沿袭树、可移植的用户定义函数 (UDF) 以及编译时模式验证，以确保数据完整性。

该框架利用基于 YAML 的表达式格式进行可重复计算。构建管道后，Xorq 会生成诸如 `expr.yaml`（可重复的表达式图）、`deferred_reads.yaml`（源元数据）和相应的 SQL 文件等工件，从而能够进行检查并与 CI 系统集成。

Xorq 利用 Apache Arrow 实现高效的数据传输，并采用 Ibis 和 DataFusion 进行高效计算。虽然目前处于 beta（pre-1.0）阶段，但 Xorq 正在快速发展，并通过其网站、Discord 和 GitHub 寻求社区参与。

---

## 22. 在 Chrome 中使用 Google 帐号登录

**原文标题**: Sign in with Google in Chrome

**原文链接**: [https://underpassapp.com/news/2025/7/5.html](https://underpassapp.com/news/2025/7/5.html)

这篇由Underpass App Company的Jeff Johnson撰写的文章讨论了谷歌的“使用Google账号登录”提示，特别是One Tap用户体验。虽然像StopTheMadness Pro这样的扩展程序可以在Safari和Firefox上隐藏网站上的“使用Google账号登录”横幅，但谷歌Chrome根本不显示这些横幅。相反，如果你已经登录了你的Google账号，Chrome会使用一个原生的One Tap对话框。

一个关键的区别是，这个Chrome对话框是浏览器界面的一部分，而不是网页的一部分，这使得Web浏览器扩展无法屏蔽它。它还会阻止扩展程序在显示时弹出。但是，这种行为可以在Chrome的设置中禁用，通过导航到`chrome://settings/content/federatedIdentityApi`并选择“阻止来自身份服务的登录提示”。

作者最后指出，这是谷歌偏袒自家Chrome浏览器、而非竞争对手的另一个例子，因为它实现了一种不同的、并且可以说更具侵入性的登录体验，这种体验不受与其他浏览器中横幅相同的基于扩展程序的屏蔽的影响。他强调，虽然这种体验可以通过设置禁用，但这种实现方式让Chrome获得了不公平的优势。

---

## 23. KernelScript 以 eBPF 为中心的编程语言

**原文标题**: KernelScript eBPF-centric programming language

**原文链接**: [https://github.com/multikernel/kernelscript](https://github.com/multikernel/kernelscript)

KernelScript 是一种新型的、类型安全的、领域特定编程语言，旨在通过将用户空间、eBPF 和内核空间代码统一到单个代码库中，从而简化 eBPF 开发。它旨在成为传统内核模块接口的现代替代方案。

为了解决现有 eBPF 开发方法（原始 C、Rust、bpftrace、Python/Go 库）的复杂性，KernelScript 提供了诸如单文件多目标编译、自动尾调用编排、透明 dynptr 集成、一流的程序生命周期安全性、零样板共享状态、自定义内核函数 (@kfunc)、统一的错误处理和经过验证器优化的类型系统等功能。它会自动生成 Makefiles、用户空间加载器和构建系统。

KernelScript 支持各种 eBPF 程序类型（XDP、TC、kprobe），具有类型化的上下文，并提供丰富的类型系统、内置的 map 支持、简洁的函数语法和辅助函数、模式匹配和多程序协调。

该语言提供了一个命令行工具，用于项目初始化和编译。示例涵盖数据包过滤、多程序协调、map 使用、函数定义、类型系统特性和错误处理。KernelScript 旨在将底层 eBPF 编程的强大功能与现代语言的生产力相结合，使 eBPF 开发变得易于访问和高效。然而，它目前处于测试阶段，语法和功能可能会发生变化。

---

## 24. 关于过度劳累护士的这部热门电影在欧洲引起警觉

**原文标题**: The hit film about overworked nurses that's causing alarm across Europe

**原文链接**: [https://www.theguardian.com/film/2025/jul/29/late-shift-swiss-hospital-nurses-overworked-healthcare](https://www.theguardian.com/film/2025/jul/29/late-shift-swiss-hospital-nurses-overworked-healthcare)

《深夜轮班》这部由佩特拉·沃尔佩执导的瑞士电影，因其对过度劳累的护士和资金不足的医疗保健系统的现实描绘，在欧洲引起轰动。影片聚焦于由莱奥妮·贝尼希饰演的敬业护士弗洛里亚，当一位同事请病假时，她面临着不堪重负的工作量，突出了潜在的失误和护士所承受的巨大压力。

沃尔佩的灵感来自于她的室友，一位护士，以及玛德琳·卡尔维拉格关于医疗保健系统的书。她强调了“女性工作”在该行业中的贬值。贝尼希沉浸在角色中，与真正的护士一起接受训练，以准确地描绘她们繁重的任务和所承担的重大医疗责任。

这部电影在德语地区的成功引发了政策改革的辩论。护士们参加了柏林首映式，举着写有“我们是弗洛里亚”的标语，一位嘉宾强调了这部电影对护理人员短缺的“恶性循环”的准确描绘。像弗朗西斯卡·奥里希这样的护士也认为这部电影真实地描绘了她们的职业生涯。沃尔佩希望这部电影能够培养人们对护士的欣赏，并促使观众成为更体谅他人的患者。她看到了更广泛的影响，批评了社会上同情心的贬值，并提倡重视那些提供护理的人，尤其是在医疗保健削减的情况下。她认为她的电影是“一封写给这个职业的情书”。

---

## 25. 展示 HN：CUDA 分形渲染器

**原文标题**: Show HN: CUDA Fractal Renderer

**原文链接**: [https://github.com/tripplyons/cuda-fractal-renderer](https://github.com/tripplyons/cuda-fractal-renderer)

此“Show HN”帖子介绍了一个 CUDA 分形渲染器，它是一个使用 NVIDIA 的 CUDA 平台快速生成分形图像的工具。

该渲染器允许用户通过指定种子值（默认为 0）来创建不同的分形。它还支持使用 `--grid-size` 参数（默认为 1，表示单个分形）并行渲染分形网格。渲染的图像保存为 `output.png`。

该帖子提供了简单的设置说明：用户需要 CUDA 和 `uv` (一个 Python 包管理器)。包含安装依赖项和使用 `uv sync` 创建虚拟环境的说明，然后使用 `uv run cuda_fractal_renderer` 运行渲染器。

最后，该帖子描述了如何使用提供的 `format.sh` 脚本（该脚本使用 `ruff`）来格式化和检查代码。

---

## 26. 我设计了自己的快速游戏流媒体视频编解码器——PyroWave。

**原文标题**: I designed my own fast game streaming video codec – PyroWave

**原文链接**: [https://themaister.net/blog/2025/06/16/i-designed-my-own-ridiculously-fast-game-streaming-video-codec-pyrowave/](https://themaister.net/blog/2025/06/16/i-designed-my-own-ridiculously-fast-game-streaming-video-codec-pyrowave/)

作者设计了一款名为PyroWave的定制低延迟视频编解码器，专为本地游戏流媒体设计，优先考虑速度和简洁性，而非高压缩比。PyroWave通过以下几个激进的设计选择来实现这一点：它是帧内编码（无运动预测），无熵编码，并使用离散小波变换(DWT)而非更常见的离散余弦变换(DCT)。

该设计牺牲了带宽效率以实现极高的编码和解码速度，运行速度超过100+ Mbit/s，使其不适合超出本地网络的互联网流媒体。该编解码器的结构针对GPU计算着色器进行了优化，将帧分解为32x32块，并进一步细分以实现高效的线程处理。

通过预先计算每个块内丢弃比特的失真和比特成本，实现了一个快速而精确的码率控制系统，从而能够在固定的预算内实现最佳的比特率分配。

基准测试结果表明，即使与硬件加速的H.264/HEVC/AV1编码器(NVENC)相比，PyroWave的编码和解码时间也明显更快，在高端AMD GPU上，1080p的编码时间低至0.13ms，4K的编码时间低至0.25ms。虽然在相似的比特率下，质量低于传统编解码器，但作者认为它足以满足本地流媒体的需求，特别是考虑到许多现代游戏固有的模糊性。作者还发现VMAF指标对于判断编解码器的质量并不可靠。最终，PyroWave是一项成功的实验，通过高度专业化的编解码器设计，实现了游戏流媒体的最低延迟。

---

## 27. 无片可看 – 实验画廊呈现五万张电影海报

**原文标题**: Nothing to watch – Experimental gallery visualizing 50k film posters

**原文链接**: [https://nothing-to-watch.port80.ch](https://nothing-to-watch.port80.ch)

文章《无物可观——实验画廊可视化五万张电影海报》描述了一个将五万张电影海报进行可视化的项目。其核心理念是，尽管如今视觉内容过载，人们却常常感到“无物可观”。

“实验画廊”这一方面暗示着该项目可能超越了简单的海报展示，很可能涉及创新或艺术性的方法来呈现和交互数据，或许探索电影海报中的模式、趋势或视觉相似性。这种可视化旨在评论选择悖论以及被海量电影淹没的感觉。该项目可能使用电影海报作为代表性数据集来进行更广泛的评论。文章暗示了对数据可视化、实验艺术以及在庞大内容库中导航体验的潜在探索。

---

## 28. 利用废弃硬件中的零日漏洞

**原文标题**: Exploiting zero days in abandoned hardware

**原文链接**: [https://blog.trailofbits.com/2025/07/25/exploiting-zero-days-in-abandoned-hardware/](https://blog.trailofbits.com/2025/07/25/exploiting-zero-days-in-abandoned-hardware/)

本文详细介绍了作者在DistrictCon垃圾场竞赛中成功利用两个已停产 (EOL) 网络设备（Netgear WGR614v9 路由器和 Bitdefender Box V1）漏洞的经历。他们凭借其创新的漏洞利用技术获得了亚军，凸显了不受支持硬件相关的安全风险。

他们通过串联多个局域网侧 UPnP 漏洞，包括身份验证绕过、缓冲区溢出和命令注入，成功攻破了 Netgear 路由器，最终获得远程 root shell。 他们利用了诸如 “bashsledding” 的新型技术，将 shell 命令喷射到 NVRAM 中执行。

Bitdefender Box V1，讽刺的是一个安全设备，通过局域网侧未经身份验证的固件降级漏洞以及固件验证过程中的命令注入被攻破，同样导致远程 root shell。 这涉及到在移动应用程序 APK 中找到一个旧的、易受攻击的固件版本，并利用其 MD5 参数验证中的命令注入缺陷。

作者强调了更广泛的安全影响，指出 UPnP 缺陷和固件降级漏洞在物联网设备中很常见。 他们敦促消费者谨慎对待 EOL 设备，并考虑制造商的支持时间表，同时鼓励研究人员探索这些设备以获得学习机会。 本文还提供了选择适合安全研究的 EOL 设备的实用建议，重点关注固件提取的简易性和可用的调试接口。

---

## 29. 加沙的饥荒令人羞耻。需要对以色列实施严厉制裁。

**原文标题**: The starvation of Gaza is shameful. Crippling sanctions on Israel are needed

**原文链接**: [https://www.theguardian.com/world/2025/jul/29/the-starvation-of-gaza-is-shameful-crippling-sanctions-on-israel-are-needed](https://www.theguardian.com/world/2025/jul/29/the-starvation-of-gaza-is-shameful-crippling-sanctions-on-israel-are-needed)

这封公开信由三十一位来自新闻、电影、学术界和政界等不同领域的以色列人士签署，表达了他们对加沙局势的“羞耻、愤怒和痛苦”。他们指责以色列“将加沙人民饿死”并考虑强迫巴勒斯坦人流离失所。

签署者呼吁国际社会对以色列实施“严厉制裁”，以迫使该国结束其“残酷行动”并实现永久停火。这封信强调了加沙人道主义危机的严重性，并将责任完全归咎于以色列的行为。签署者将自己定位为致力于以色列和巴勒斯坦邻国和平未来的以色列人，强调他们的批评源于对公正解决方案的渴望。他们包括许多获得过国际和以色列著名奖项的杰出人士，这增加了他们谴责的分量。

---

## 30. Rotring 600 圆珠笔

**原文标题**: Rotring 600 Ballpoint Pen

**原文链接**: [https://www.shellshore.com/review-rotring-600-ballpoint-pen/](https://www.shellshore.com/review-rotring-600-ballpoint-pen/)

文具爱好者内森·马评测了红环600圆珠笔，这是一款金属笔身的圆珠笔，是经典红环600自动铅笔的圆珠笔版本。 它使用标准的派克式笔芯和按动机构。

他强调了这款笔坚固、可靠的全金属结构和令人满意的按动机构，但也指出它可能声音较大。 这款笔的设计与红环600自动铅笔非常相似，只是笔尖和笔杆上的文字略有不同。

内森在赞扬红环的质量声誉的同时，也提到过去曾出现过红环自带的笔芯导致笔的机构损坏的问题，但通过更换不同的笔芯（凝胶笔芯）解决了该问题。 他认为这是一个小问题，因为他本来就更喜欢凝胶笔芯。

他总结说，红环600圆珠笔是一款值得购买的高品质工具，尤其是在打折的时候。 由于书写体验很大程度上取决于使用的笔芯，因此这款笔的价值在于其耐用且结构精良的笔身，使其成为寻求可靠圆珠笔的人的持久之选。

---

## 31. 孔雀羽毛可作激光器

**原文标题**: Peacock feathers can be lasers

**原文链接**: [https://www.science.org/content/article/peacock-feathers-can-be-lasers](https://www.science.org/content/article/peacock-feathers-can-be-lasers)

无法访问文章链接。

---

## 32. 美国宇航局发现了18种最适合自然净化室内空气的植物

**原文标题**: NASA found the 18 best plants for naturally filtering the air in your home

**原文链接**: [https://www.good.is/nasas-favorite-houseplants-ex1](https://www.good.is/nasas-favorite-houseplants-ex1)

本文重点介绍了一项NASA研究，该研究确定了18种最适合自然过滤室内空气的植物。它表明植物是改善室内空气质量的有效且自然的方法，尤其是在较小的居住空间中。本文引导读者参考NASA的清单，以选择最适合其家庭的空气净化植物。

---

## 33. 环法自行车赛面临新威胁：自行车手是否使用微型马达？

**原文标题**: Tour de France confronts a new threat: Are cyclists using tiny motors?

**原文链接**: [https://www.washingtonpost.com/world/2025/07/25/tour-france-bikes-hidden-motors/](https://www.washingtonpost.com/world/2025/07/25/tour-france-bikes-hidden-motors/)

无法访问文章链接。

---

## 34. Futurehome智能中枢用户需支付117美元新订阅费，否则将失去访问权限。

**原文标题**: Futurehome smart hub owners must pay new $117 subscription or lose access

**原文链接**: [https://arstechnica.com/gadgets/2025/07/bankrupt-futurehome-suddenly-makes-its-smart-home-hub-a-subscription-service/](https://arstechnica.com/gadgets/2025/07/bankrupt-futurehome-suddenly-makes-its-smart-home-hub-a-subscription-service/)

智能家居设备制造商Futurehome现要求其Smarthub及相关设备的基本功能支付每年117美元的订阅费，实际上是将未付费用户的设备变为“哑巴”设备。这一突变影响了设备控制、自动化甚至支持等核心功能。

该公司声称，订阅费是由于最近的破产和随后的平台收购所必需的，并承诺改进功能、安全性和支持。然而，之前购买Futurehome产品并认为这些功能包含在初始价格中的客户，对此感到沮丧是可以理解的。一些人正在考虑将他们的设备转移到开放标准，以避免订阅。

Futurehome过去的举动使情况进一步复杂化，包括关闭用户论坛和阻止破解其固件的努力。这一举动与其他苦于寻找可持续商业模式的物联网公司的类似行为相呼应，引发了人们对智能家居生态系统长期可行性和可信度的担忧。 Futurehome产品页面上缺乏关于订阅的透明度，加剧了客户的不满。

---

## 35. 展示HN：公司用人工智能接听你的电话。我做了个人工智能帮你打。

**原文标题**: Show HN: Companies use AI to take your calls. I built AI to make them for you

**原文链接**: [https://www.pipervoice.com/](https://www.pipervoice.com/)

Piper：一款人工智能电话服务，帮你自动拨打电话，处理预订、取消订阅、解决客服问题和获取报价等任务。它旨在通过自主处理电话事务，消除拨打电话的烦恼体验。

其工作原理是：一个Chrome扩展程序允许用户点击在网上找到的任何电话号码，并输入他们的请求。然后，Piper会拨打电话，浏览电话菜单，等待接听，并完成任务。用户会收到实时状态更新和完整文字记录。

该服务定位为“以更好的自动化对抗自动化”，用其自身的人工智能代理应对公司电话树和人工智能接待员。Piper的目标是比典型的客户服务互动听起来更像人类，并且更有耐心。

该系统优先考虑安全性，使用银行级别的加密，并在转录后自动删除录音。

Piper目前处于测试阶段，为测试人员提供60分钟的免费通话时间。测试版用户还可以享受折扣价格，并可直接与创始人联系。创建者强调他们来自AssemblyAI（一家专注于语音人工智能技术的公司）的经验。他们的目标是普及人工智能电话助手，将其提供给个人，而不仅仅是大型企业。

---

## 36. RP2350 A4、RP2354及一项新的黑客挑战

**原文标题**: RP2350 A4, RP2354, and a New Hacking Challenge

**原文链接**: [https://www.raspberrypi.com/news/rp2350-a4-rp2354-and-a-new-hacking-challenge/](https://www.raspberrypi.com/news/rp2350-a4-rp2354-and-a-new-hacking-challenge/)

以下是树莓派新闻文章“RP2350 A4、RP2354 及全新黑客挑战”的摘要：

文章宣布发布两款新的树莓派硅产品：RP2350 A4 和 RP2354。RP2350 A4 是一款四核微控制器单元 (MCU)，采用 RP2040 架构，拥有更大的 RAM 和额外的功能。RP2354 似乎与之相关，可能是 RP2040 系列 MCU 的另一个迭代版本或变体。摘要文本未提供关于 RP2354 的具体细节，这意味着完整文章中会对其进行详细阐述。

除了硬件公告外，文章的核心是围绕这些新硅芯片展开的全新黑客挑战。该挑战邀请参与者发现漏洞并利用新硬件的安全功能。树莓派团队旨在鼓励安全研究人员和爱好者测试并提高其产品的安全性。

文章强调了嵌入式系统中安全的重要性，并强调了树莓派致力于确保其硬件产品稳健性的承诺。黑客挑战是一种积极主动地识别和解决潜在安全漏洞的实用方法，最终使整个树莓派社区受益。文章鼓励有兴趣的人参与挑战，并为 RP2350 A4 和 RP2354 的安全加固做出贡献。

---

## 37. 四十岁重塑Amiga

**原文标题**: Modernising the Amiga at Forty

**原文链接**: [https://benjamin.computer/posts/2025-07-28-amiga40.html](https://benjamin.computer/posts/2025-07-28-amiga40.html)

本文详细介绍了在2025年Amiga 500迎来40周年之际，对其进行硬件和软件现代化的过程。作者首先回顾了Amiga的首次亮相以及它在爱好者中持久的遗产。

硬件升级包括Vampire A500 V2加速卡、内存升级、ENC28J60以太网适配器和Gotek USB软盘驱动器模拟器。 Vampire卡提供更快的处理器、硬盘仿真、以太网控制器插槽和HDMI输出。

作者探索了使用像CoffinOS这样的预制设置，但最终决定构建一个自定义设置以获得更大的控制权。文章概述了所使用的基本工具（xdftool、Samba服务器）以及令人困惑的Amiga OS版本，最终选择了Amiga OS 3.2。

该过程包括使用HDToolBox和Professional File System 3对compact flash卡进行分区，安装Workbench，并配置Amiga Shell。还安装了诸如LHA之类的用于解压缩文件的关键实用程序。 提供了安装Vampire卡以太网适配器和可重定向图形的SAGA驱动程序的具体说明，然后使用Roadshow设置TCP/IP协议栈。然后配置Samba以启用Amiga和现代文件服务器之间的文件共享，从而简化了将文件传输到Amiga的过程。作者最后总结了所取得的进展，并暗示了未来的步骤，例如配置Picasso96。

---

## 38. 不同的时钟

**原文标题**: Different Clocks

**原文链接**: [https://ianto-cannon.github.io/clock.html](https://ianto-cannon.github.io/clock.html)

本文题为“不同的时钟”，展示了Ianto Cannon使用JavaScript渲染的可缩放矢量图形创建的各种时间可视化表示。 这些时钟以非传统和艺术的方式显示当前时间，超越了标准的模拟或数字格式。

不同的时钟图形包括：

*   **二进制:** 使用二进制方块表示Unix时间。
*   **多边形:** 时间由一系列多边形显示，分别表示年、月、周、日、时、分和秒。
*   **斑点:** 一系列动画斑点通过行波显示时间，这些行波的频率对应于千年、年、日、时、分和秒。
*   **太阳系:** 描绘了地球和月亮绕太阳的轨道，包括夜间黄道符号。
*   **峰值:** 使用移动的峰值来表示千年、年、日、时和分。
*   **波浪:** 类似于峰值，但使用贝塞尔曲线。

作者Ianto Cannon鼓励用户自由使用和修改提供的源代码。 太阳系时钟被指出需要适当的同步。 本文版权归Ianto Cannon所有，2025年7月29日。

---

## 39. Anthropic 接近达成协议，将以 1700 亿美元估值融资

**原文标题**: Anthropic Nears Deal to Raise Funding at $170B Valuation

**原文链接**: [https://www.bloomberg.com/news/articles/2025-07-29/anthropic-nears-deal-to-raise-funding-at-170-billion-valuation](https://www.bloomberg.com/news/articles/2025-07-29/anthropic-nears-deal-to-raise-funding-at-170-billion-valuation)

无法访问文章链接。

---

## 40. Show HN: 揭穿选举舞弊指控 – 交互式数据可视化与模拟

**原文标题**: Show HN: Debunking Election Fraud Claims – Interactive Data Viz and Simulations

**原文链接**: [https://sullivan.zip/clark-county-election-analysis/](https://sullivan.zip/clark-county-election-analysis/)

此"Show HN"提交展示了一个互动数据可视化项目，旨在驳斥关于2024年美国总统选举舞弊的说法，特别是针对“选举真相联盟”(ETA)的分析。作者使用互动抛硬币模拟来阐释大数定律，论证投票数据中的模式可能是由于样本量（每台机器的选票数）增加而自然产生的，而非人为操纵。

ETA声称内华达州的投票记录显示机器在一定数量的选票后被篡改以支持特朗普。作者重现了ETA的图表，并证明他们的分析存在缺陷，因为他们将投票数高的早期投票机器与投票数低得多的选举日机器进行了比较。当早期投票数据被截断以匹配选举日机器的较低投票数时，模式变得相似，从而驳斥了操纵的说法。

然后，作者展示了实际投票数据的互动可视化，显示了单个机器的投票历史。这些可视化表明，机器在不同的地点（城市与乡村）稳定在不同的平均值，没有证据表明存在选票翻转。逆转投票历史也未显示任何操纵。

最后，文章探讨了ETA关于特朗普在机器上的百分比分布中存在“俄罗斯尾巴”的说法，认为应用正态分布是不恰当的，因为样本量和人口（投票地点）各不相同。核心论点是，ETA的结论是基于对统计原则的误解和对关键数据特征的忽略。互动可视化允许用户探索数据并自行评估这些说法。

---

## 41. 够了AI副驾驶，我们需要AI抬头显示器。

**原文标题**: Enough AI copilots, we need AI HUDs

**原文链接**: [https://www.geoffreylitt.com/2025/07/27/enough-ai-copilots-we-need-ai-huds](https://www.geoffreylitt.com/2025/07/27/enough-ai-copilots-we-need-ai-huds)

在其题为《别再迷恋AI副驾，我们需要AI平视显示器》的文章中，作者反对过度依赖“副驾”式AI界面，并倡导“平视显示器”（HUD）设计，以扩展人类的感知和理解。他从马克·维泽尔1992年对AI代理的批判中汲取灵感，强调让技术融入背景，成为用户的延伸的重要性。

文章对比了直接与用户互动的虚拟助手“副驾”和将信息直接叠加到用户视野中，增强意识的“平视显示器”。 软件中平视显示器的例子包括拼写检查（立即突出显示错误）和自定义调试器（可视化程序行为）。作者认为，平视显示器可以对任务产生更深入、更环境化的理解，从而产生超越直接目标的新见解和机会。

虽然承认副驾在常规、可预测的任务中有其用武之地，但作者认为平视显示器更适合需要专家人工判断的复杂情况。 他总结道，设计师应该探索类似平视显示器的界面来增强人类智能，尤其是在追求非凡成果时。文章还提供了有关AI和人类增强主题的进一步阅读链接。

---

## 42. 优化数独解法

**原文标题**: Optimi-Zi(n)g Sudoku-Solving

**原文链接**: [https://log.pfad.fr/2025/optimi-zig-sudoku-solving/](https://log.pfad.fr/2025/optimi-zig-sudoku-solving/)

奥利维尔的日志详细记录了他使用 Dancing Links (DLX) 算法优化基于 Zig 的数独解算器的过程。DLX 算法通过将约束和部分解表示为 0 和 1 的矩阵，高效地解决精确覆盖问题，例如数独。

最初，奥利维尔专注于减少内存分配，这显著提高了性能。他从分配单个单元格改为一次性分配整行，最终预先分配解决方案数组的大小。

然后，他使用 Hotspot 性能分析器来识别性能瓶颈，发现求模运算出乎意料地慢。将 `comptime` 添加到相关参数解决了这个问题。启用 Zig 的 `-Doptimize=ReleaseFast` 标志也带来了相当大的性能提升。

进一步的优化包括通过采用“非托管”DLX 结构来消除剩余的分配，在这种结构中，调用者负责单元格的内存分配。这消除了堆的使用，并将计算转移到堆栈上。

最后，他通过跳过不必要的部分解的设置，标记列为已覆盖，并避免添加包含这些已覆盖列的行，从而优化了数独准备阶段。

这些优化使得解算器速度显著提升，升级到 Zig 0.14.1 后，每个谜题的平均求解时间达到 0.061 毫秒。多线程进一步提高了吞吐量，使解算器能够每秒处理约 138,000 个谜题。奥利维尔最后提到可以将逻辑调整以解决 N 皇后问题。

---

## 43. 年龄验证法案导致VPN使用激增，并威胁开放互联网

**原文标题**: Age Verification Laws Send VPN Use Soaring–and Threaten the Open Internet

**原文链接**: [https://www.wired.com/story/vpn-use-spike-age-verification-laws-uk/](https://www.wired.com/story/vpn-use-spike-age-verification-laws-uk/)

英国实施《网络安全法案》（要求成人内容网站进行年龄验证）后，英国VPN和其他规避工具的使用激增。专家们预测到了这一趋势，与拥有年龄检查法的其他国家的情况类似。该法案要求进行“高度有效”的年龄检查，包括身份验证和自拍上传，这导致用户寻求VPN来掩盖其位置并探索创造性的规避方法，例如使用视频游戏《死亡搁浅》。

虽然监管机构报告称，数千个色情网站和主要社交平台在实施年龄检查方面取得了进展，但数字权利倡导者警告说，未来可能会更积极地执行这些机制。美国公民自由联盟强调，技术不是快速解决方案，强大的支持网络和情感关系对儿童的福祉至关重要。

几款VPN应用程序经历了爆炸式增长，iOS下载量显着飙升。Proton VPN、Windscribe和AdGuard VPN都报告称，来自英国的注册和安装量大幅增加。Nord Security的订阅购买量增长了1000%。

文章强调了越来越多的国家正在考虑或采纳年龄验证法律的趋势，即使是那些历史上拥护互联网自由的国家，这也引发了关于数字权利的复杂问题。美国公民自由联盟指出，各国政府面临着两难境地：要么在全球范围内实施这些检查，要么鼓励使用规避审查的工具。这一发展模糊了保护儿童和可能破坏开放互联网之间的界限。

---

## 44. 化繁为简，再添乐趣：儿童设计之道

**原文标题**: Simplify, then add delightness: On designing for children

**原文链接**: [https://shaneosullivan.wordpress.com/2025/07/28/on-designing-for-children/](https://shaneosullivan.wordpress.com/2025/07/28/on-designing-for-children/)

Shane O'Sullivan，《Kidz Fun Art》开发者，分享了为儿童设计引人入胜且用户友好的应用程序的见解，强调这与为成人设计截然不同。他的重点在于简化和乐趣。

**关键原则：**

*   **减少文本：** 尽可能依赖视觉效果，因为许多幼儿阅读能力有限。
*   **展示、共置、提示：** 工具应易于发现，并直接放置在它们所操作的对象上或附近。用非文字的方式提示隐藏功能。
*   **容错性：** 实施撤销/重做功能和软删除，以避免用户沮丧。
*   **成人参与：** 对于更高级的功能，通过图形提示让父母参与，但每个功能只请求一次帮助。
*   **减少精细动作控制：** 使用大型触摸目标，并倾向于长按交互而非精确拖动。
*   **手掌误触屏蔽：** 实施手掌误触屏蔽，以防止意外交互，使用触摸类型属性等技术。
*   **先简化，再增添乐趣：** 融入鲜艳的色彩、彩虹、音效和触觉互动（例如，戳破泡泡）等元素，以增强参与度。
*   **保持视觉上下文：** 使用半透明对话框、动画过渡，并避免叠加对话框，以防止状态更改时产生混淆。
*   **道德变现：** 由于不当内容问题，避免第三方广告。考虑免费增值模式或可选订阅。向父母发送电子邮件营销可能可以接受。
*   **优先考虑隐私：** 限制社交分享，以保护儿童的数据和安全。安全分享选项包括直接发送电子邮件至拥有帐户，以及使用预填充令牌分享AI生成的图像。

总的来说，在为年轻用户开发应用程序时，应优先考虑儿童安全、直观设计和引人入胜的体验。

---

## 45. SQLx – Rust SQL 工具包

**原文标题**: SQLx – Rust SQL Toolkit

**原文链接**: [https://github.com/launchbadge/sqlx](https://github.com/launchbadge/sqlx)

SQLx 是一个纯 Rust SQL 工具包，提供具有编译时检查查询且无需 DSL 的异步数据库交互。它支持 PostgreSQL、MySQL/MariaDB 和 SQLite（依赖 C 库），并可在不同的运行时（async-std、tokio、actix）和 TLS 后端工作。计划在未来版本中支持 MSSQL。

主要功能包括内置连接池、行流式传输、自动语句准备、TLS、异步通知 (PostgreSQL) 和嵌套事务。它还提供了一个 `Any` 驱动程序，用于动态切换数据库驱动程序。

安装涉及在 Cargo.toml 中选择适当的运行时和 TLS 功能（例如，`runtime-tokio`、`tls-native-tls`）。功能标志控制数据库支持（postgres、mysql、sqlite、mssql）和附加功能（例如，UUID、chrono、json 支持）。

SQLx 的独特之处在于它能够针对开发数据库启用编译时查询验证，确保 SQL 语法和语义有效。这是通过 `sqlx::query!` 和 `sqlx::query_as!` 等宏实现的。可以启用离线模式来缓存查询分析结果。

该工具包为预备语句和非预备语句提供低级和高级查询接口。高级功能包括用于轻松执行和获取结果的终结器。它还强调使用 `FromRow` derive 宏将数据库行映射到 Rust 类型。

SQLx 优先考虑安全性，使用 `#![forbid(unsafe_code)]`，除非启用 `sqlite` 功能，在这种情况下，它允许对 SQLite C API 进行特定的 `unsafe` 调用。它采用 Apache 2.0 和 MIT 双重许可。

---

## 46. Meta 将允许求职者在编程测试中使用人工智能

**原文标题**: Meta Is Going to Let Job Candidates Use AI During Coding Tests

**原文链接**: [https://www.wired.com/story/meta-ai-job-interview-coding/](https://www.wired.com/story/meta-ai-job-interview-coding/)

Meta准备允许编码职位应聘者在面试过程中使用AI助手，这反映了行业将AI融入软件工程岗位的更广泛趋势。该公司还在招募员工志愿者进行“模拟AI赋能面试”，以完善这种新方法。

此举符合Meta CEO马克·扎克伯格关于AI成为软件开发核心组成部分的愿景，可能催生能够独立编写代码的“AI编码代理”。他预计最早在2025年AI就能像中级工程师一样工作，在12-18个月内就可以用于AI相关项目，并最终在Meta生态系统中生成大部分代码。

虽然许多科技公司鼓励工程师使用AI工具，但Meta在面试中拥抱AI相对具有前瞻性，因为像Anthropic这样的一些公司明确禁止在申请过程中使用AI。 这一转变引发了辩论，人们担心未来的编码员是否会优先考虑AI提示而不是基本的软件工程技能以及他们调试AI生成代码的能力。 Meta发言人表示，为申请者测试这些AI工具是他们专注于使用AI协助工程师日常工作的一个自然进展。

---

## 47. 不良行为者付费购买谷歌广告来安装虚假的Oh My Zsh版本

**原文标题**: Bad actors are paying for Google ads to install bogus version of Oh My Zsh

**原文链接**: [https://twitter.com/robbyrussell/status/1949985205260837268](https://twitter.com/robbyrussell/status/1949985205260837268)

警告：恶意行为者利用谷歌广告推广Oh My Zsh的虚假版本，该版本是流行的开源Zsh配置管理框架。这些伪造版本可能包含恶意软件，从而危及用户系统。请谨慎下载Oh My Zsh，确保从可信来源获取。警惕推广下载的谷歌广告，它们可能链接到恶意版本。

---

## 48. Copyparty – 将几乎任何设备变成文件服务器

**原文标题**: Copyparty – Turn almost any device into a file server

**原文链接**: [https://github.com/9001/copyparty](https://github.com/9001/copyparty)

Copyparty是一款轻量级的跨平台文件服务器，可以将几乎任何设备转化为可通过网页浏览器访问的文件共享中心。它支持断点续传上传/下载，并且服务器端仅需Python。

主要特性包括支持多种协议（HTTP、WebDAV、FTP、TFTP、SMB/CIFS），可选的Android应用和iPhone快捷方式，以及上传文件大小无限制。它支持各种服务器配置，包括反向代理设置以及与systemd和其他init系统的集成。

该服务器提供一系列功能，例如文件索引（按内容、名称、日期、大小搜索）、音频/视频播放与转码、缩略图生成、Markdown查看和编辑、文件管理（剪切/粘贴、重命名、删除）、可共享链接、RSS订阅和事件钩子。它还提供可选功能，如文件去重、上传压缩以及与云存储（如AWS S3）的集成。

安全功能包括基于IP的身份验证、用户可更改密码以及隐藏于搜索引擎的选项。它提供可定制的主题和浏览器UI调整，以及通过参数或配置文件进行广泛配置的选项。

Copyparty优先考虑易用性和最小依赖性，旨在成为一个快速、适应性强的文件传输解决方案。它有多种安装选项，包括自包含的可执行文件、pypi以及通过Arch和NixOS上的软件包管理器安装。它强调支持旧版浏览器和Python版本，同时提供可选的依赖项以增强功能。

---

## 49. GLM-4.5：推理、编码与自主能力

**原文标题**: GLM-4.5: Reasoning, Coding, and Agentic Abililties

**原文链接**: [https://z.ai/blog/glm-4.5](https://z.ai/blog/glm-4.5)

无法访问文章链接。

---

## 50. 显示 HN：使用他们的身份 – 使用你当地英国议员的身份来反对网络安全法

**原文标题**: Show HN: Use Their ID – Use your local UK MP’s ID for the Online Safety Act

**原文链接**: [https://use-their-id.com/](https://use-their-id.com/)

“使用他们的身份”——用你当地英国议员的身份来对抗《网络安全法案》：这篇文章可能提出了一种针对英国《网络安全法案》的抗议形式。其核心思想似乎是鼓励个人在在线服务需要年龄验证时，提交他们当地议会议员（MP）的身份证明。

其含义是，广泛提交议员的身份证明将会：

*   **使系统过载：** 可能扰乱年龄验证过程，使合法用户难以访问在线服务。
*   **凸显该法律的荒谬性：** 展示了年龄验证措施是多么容易被规避或滥用。
*   **引起对议员的关注：** 可能会针对特定的议员或整个议会，追究他们对《网络安全法案》的缺陷所应负的责任。

本质上，这篇文章建议采取一种公民不服从的形式，通过使用那些通过该法律的人的身份证明，来突出《网络安全法案》的年龄验证要求的问题和被认为的侵入性。

---

## 51. 英国技术大臣：反对《网络安全法案》者站在掠食者一边

**原文标题**: UK Technology Secretary: Online Safety Act opponents are on the predators's side

**原文链接**: [https://twitter.com/peterkyle/status/1950092871614230571](https://twitter.com/peterkyle/status/1950092871614230571)

根据标题，该文章报道英国技术大臣正对《网络安全法案》采取强硬立场。 关键要点是，该大臣认为任何反对该法案的人实际上都是在与网络掠食者为伍。 这表明该大臣认为该法案对于保护在线用户至关重要，并将对该法案的批评或抵制视为纵容有害的在线行为。 “JavaScript不可用”消息以及诸如“服务条款”和“隐私政策”之类的通用页脚链接表明该文章源自X（前身为Twitter）。 由于无法获得完整的文章内容，因此该摘要主要基于标题的隐含信息，该信息表明英国技术大臣就反对《网络安全法案》发表了一项有争议且可能具有煽动性的声明。

---

## 52. Cucumber让你用自然语言编写自动化测试。

**原文标题**: Cucumber lets you write automated tests in plain language

**原文链接**: [https://cucumber.io/](https://cucumber.io/)

Cucumber：让团队通过自然语言编写自动化验收测试，使所有相关人员（无论技术水平如何）都能理解和使用。这能改善团队内部的沟通、协作和信任。Cucumber提倡行为驱动开发（BDD），一种强调协作和对需求共享理解的开发过程。本文提供了一个Cucumber入门教程链接，以及学习BDD的更多资源。文章通过一个取款场景的功能文件示例，展示了Cucumber的用法。该功能用自然语言编写，规定了规则和场景，例如余额内的成功取款和超过余额的拒绝取款，概述了Cucumber测试典型的“Given-When-Then”结构。

---

## 53. 陶论“蓝队”对“红队”大语言模型

**原文标题**: Tao on “blue team” vs. “red team” LLMs

**原文链接**: [https://mathstodon.xyz/@tao/114915604830689046](https://mathstodon.xyz/@tao/114915604830689046)

陶哲轩论“蓝队”对“红队”大语言模型

鉴于提供的文本不完整且被截断（“陶哲轩：在网络安全领域，一个区别是……” - Mathstodon），因此无法进行全面的总结。然而，我们可以根据现有的上下文推断出大致的主题。

标题“陶哲轩论'蓝队'对'红队'大语言模型”表明陶哲轩正在讨论网络安全背景下的大语言模型 (LLM)，特别是对比“蓝队”和“红队”方法。这表明讨论的是关于 LLM 的攻防策略。

以下是根据可能的主题进行的潜在的简要总结：

陶哲轩的 Mastodon 帖子可能涉及 LLM 安全背景下的“蓝队”与“红队”的区别。“蓝队”通常侧重于防御策略，例如修补漏洞、监控威胁以及保护系统免受攻击。在 LLM 环境中，这可能涉及使模型更能抵抗对抗性提示、检测恶意输出并确保负责任地使用等技术。相反，“红队”采用进攻性方法，积极探测并试图利用系统（包括 LLM）中的弱点。这可能涉及精心设计对抗性提示以引发有害响应、发现偏见或寻找绕过安全机制的方法。讨论可能探讨了两种方法对于开发安全可靠的 LLM 的重要性。如果没有全文，则无法进行更详细的总结。

---

## 54. 英国将在九月承认巴勒斯坦国地位，除非停火。

**原文标题**: U.K. Will Recognize Palestinian Statehood in September, Barring Cease-Fire

**原文链接**: [https://www.nytimes.com/2025/07/29/world/europe/uk-palestinian-statehood.html](https://www.nytimes.com/2025/07/29/world/europe/uk-palestinian-statehood.html)

无法访问文章链接。

---

## 55. 梵蒂冈天文台仰望星空

**原文标题**: The Vatican observatory looks to the heavens

**原文链接**: [https://www.newyorker.com/magazine/2025/08/04/the-vatican-observatory-looks-to-the-heavens](https://www.newyorker.com/magazine/2025/08/04/the-vatican-observatory-looks-to-the-heavens)

本文探讨了梵蒂冈天文台及其台长盖伊·孔索尔马尼奥，一位致力于科学研究星空的耶稣会修士。该天文台成立于1891年，旨在调和信仰与科学，消除两者不相容的观念。孔索尔马尼奥，绰号“教皇的天文学家”，花费大量时间与公众互动，强调科学不需要证明宗教，而是两者可以共存。

该天文台在意大利的冈道夫堡运作，并在亚利桑那州拥有一座配备有梵蒂冈先进技术望远镜（VATT）的研究机构。耶稣会工作人员摆脱了世俗压力，如终身教职和科研经费，专注于长期研究，与美国宇航局等机构合作，进行如分析小行星贝努样本等项目。他们的研究包括研究陨石和柯伊伯带中的天体，其中一些暗示了冥王星之外可能存在一颗巨大的行星。

该天文台的历史可以追溯到16世纪末，对历法改革和创建天空摄影地图做出了重大贡献。虽然之前的教皇，如庇护十二世，试图在科学和圣经之间找到一致性，但孔索尔马尼奥和他的同事们专注于科学探究，他们的工作独立于梵蒂冈的教义。他们在私人捐助者和圣座的支持下运作，这使他们能够追求“中庸之道科学”和“中庸之道宗教”，证明信仰和科学可以和谐共存。

---

## 56. MCP Auth 指南：身份、许可和代理安全

**原文标题**: The Guide to MCP Auth: Identity, Consent, and Agent Security

**原文链接**: [https://www.permit.io/blog/the-ultimate-guide-to-mcp-auth](https://www.permit.io/blog/the-ultimate-guide-to-mcp-auth)

本文重点介绍了在生产环境中实施模型上下文协议（MCP）所面临的挑战，着重关注身份、许可和安全问题。MCP允许AI代理访问上下文相关的工具并做出决策，但这会引入更大的攻击面，并需要强大的身份验证和授权机制。

作者确定了五个关键的身份验证层级：代理身份、委托人身份验证、委托人对代理的许可、对MCP服务器的访问以及对上游服务的访问。复杂性源于上下文不仅是元数据，而且是可执行的意图，这可能导致提示注入、混淆代理问题和工具链泄漏。

当前的MCP实现存在局限性，例如脆弱的远程服务器支持、笨拙的配置、糟糕的文档以及缺失的策略执行。本文倡导使用中间件来验证代理身份、评估委托、过滤工具列表并记录操作。

至关重要的是，作者强调MCP中的许可不仅仅是一个简单的OAuth复选框；它需要明确定义范围、关系和运行时访问，并且是可审计和可撤销的。

核心建议是为代理分配唯一的身份，将许可作为主要的控制面，实施中间件以增强控制和可观察性，利用细粒度的权限而不是仅仅依赖于令牌，并在执行之前询问代理以了解其意图。本文最后呼吁采用上下文感知的控制系统，以确保MCP的安全性和可靠性。

---

## 57. 同时呼吸氧气和硫的细胞

**原文标题**: Cells that breathe oxygen and sulfur at the same time

**原文链接**: [https://www.quantamagazine.org/the-cells-that-breathe-two-ways-20250723/](https://www.quantamagazine.org/the-cells-that-breathe-two-ways-20250723/)

本文探讨了在黄石国家公园的温泉中发现的一种细菌——氢氧化细菌RSW1，该细菌可以同时进行有氧和硫呼吸，这在以前被认为是不可思议的。有氧和厌氧呼吸通常是分开进行的，因为氧气会破坏厌氧过程。然而，RSW1通过同时运行这两种代谢方式而茁壮成长，使其能够从两种过程的能量中获益。

由蒙大拿州立大学的埃里克·博伊德领导的研究人员发现，RSW1可以在没有氧气的情况下处理氢气和硫，从而产生硫化氢，但不会生长。当引入氧气时，细菌生长得更快，并继续产生硫化氢，表明同时存在有氧和厌氧呼吸。这种混合代谢在温泉中氧气水平波动的环境中是有利的。

这一发现挑战了关于细胞呼吸极限的假设，并为理解微生物生命在大氧化事件期间（地球上氧气水平上升时）如何适应提供了模型。据推测，RSW1可能使用特殊的化学复合物来保护其厌氧机制免受氧气的影响。作者还认为，这种双重代谢可能比以前认为的更广泛，尤其是在具有氧气梯度的环境中。

---

## 58. 同时呼吸氧气和硫的细胞

**原文标题**: Cells that breathe oxygen and sulfur at the same time

**原文链接**: [https://www.quantamagazine.org/the-cells-that-breathe-two-ways-20250723/](https://www.quantamagazine.org/the-cells-that-breathe-two-ways-20250723/)

本文探讨了在黄石国家公园温泉中发现的一种细菌——氢杆菌RSW1，它能同时进行有氧呼吸和无氧呼吸，同时呼吸氧气和硫。这非常不寻常，因为氧气通常对厌氧过程有毒。

研究人员对即使在有氧气存在的情况下，细菌也能产生硫化物（一种无氧呼吸的产物）的报告很感兴趣。RSW1在火山温泉中很常见，人们发现它在富氧和无氧条件下都能茁壮成长。虽然它能单独依靠硫存活，但当添加氧气时，它的生长速度会更快，同时仍然产生硫化氢。

这种双重代谢挑战了关于细胞呼吸极限的假设。通常，暴露于氧气会为厌氧生物产生有害的活性氧化合物，但RSW1似乎有一种机制可以防止这种情况。据推测，这种细菌可能使用化学超复合物来隔离并快速消耗氧气，从而防止对硫基呼吸的干扰。

这一发现意义重大，因为它表明双重代谢可能比之前认为的更普遍，尤其是在氧气水平波动的环境中。它也为了解微生物生命在大氧化事件期间是如何适应的提供了见解。在大氧化事件期间，地球大气层从厌氧转变为有氧，能够处理甚至利用氧气的生物体将在那个变革时期具有显著优势。

---

## 59. 全息图 v0.5.0

**原文标题**: Hologram v0.5.0

**原文链接**: [https://hologram.page/blog/hologram-v0-5-0-released](https://hologram.page/blog/hologram-v0-5-0-released)

Hologram v0.5.0 是一项重大发布，重点在于性能、新功能以及架构改进，旨在提升开发者体验和未来能力。主要亮点包括显著的性能提升，将执行时间缩短至微秒级，适用于 SVG 绘图演示中展示的实时交互绘图应用。

新功能包括全面的会话和 Cookie 管理，具备完整的服务器端支持和 Phoenix 集成，新增指针和鼠标移动事件，用于开发的带有错误覆盖和 Phoenix 集成的实时重新加载，以及用于分布式状态管理的基础 CRDT 实现。

增强功能包括重写的位串实现，可实现更快的渲染，用于实现 2 到 10 倍更快构建的增量编译，具有全面坐标跟踪的增强型事件系统，以及跨各种功能和组件的广泛性能优化。此版本还包括传输层迁移到具有 WebSocket 连接管理的 HTTP、序列化改进以及通过新的 Erlang 函数端口扩展的运行时支持。

错误修复解决了模板和解析问题、事件和导航问题以及运行时错误。此版本引入了向后不兼容的事件命名更改。作者感谢 GitHub 赞助者的支持，并鼓励其他人做出贡献，并邀请用户加入新闻邮件以获取每月更新。

---

## 60. 食品科技阻止腐烂：不再有棕色香蕉或软烂牛油果 (2019)

**原文标题**: Food tech stops rot: No more brown bananas or squishy avocados (2019)

**原文链接**: [https://www.latimes.com/business/story/2019-12-27/food-tech-could-stop-rot-brown-bananas-or-squishy-avocados](https://www.latimes.com/business/story/2019-12-27/food-tech-could-stop-rot-brown-bananas-or-squishy-avocados)

芝加哥论坛报2019年的一篇文章探讨了蓬勃发展的食品科技行业，该行业专注于延长农产品和其他易腐食品的保质期，以对抗食物浪费。总部位于芝加哥的Hazel Technologies公司因其释放乙烯抑制剂的小袋而备受关注，该小袋可减缓水果和蔬菜的腐烂过程。该公司针对各种易腐食品，并正在研发用于包装的抗菌内衬。

文章强调了美国食物浪费的严重问题，高达40%的食物未被食用，每年给家庭和超市造成数十亿美元的损失。保质期延长技术被认为是关键的解决方案，可带来巨大的经济和环境效益。Apeel Sciences、Cambridge Crops和It's Fresh等其他几家公司也被提及为该领域的创新者，吸引了大量的风险投资。

像大型鳄梨分销商Mission Produce这样的公司正在使用Hazel的技术来延长其产品的保质期并减少浪费，从而带来潜在的成本节约和环境效益。 广泛采用的挑战包括：供应商付费但零售商受益的商业模式、消费者为保质期更长的农产品支付更多费用的意愿，以及将新技术整合到现有供应链中的复杂性。 Hazel还在探索将废弃的测试水果升级回收为烈酒和精酿啤酒的方法。

---

## 61. 无用的 useCallback

**原文标题**: The Useless UseCallback

**原文链接**: [https://tkdodo.eu/blog/the-useless-use-callback](https://tkdodo.eu/blog/the-useless-use-callback)

本文认为`useCallback`和`useMemo`常被不必要地使用，导致代码复杂化而没有实际的性能提升。作者指出了memoization的两个主要原因：性能优化（避免重新渲染）和防止effect触发过于频繁。

本文提出了这些Hook变得毫无意义的两种常见情况：

1.  **没有Memoized组件：** 当memoized的函数或值被传递给常规函数式组件时，`useCallback`或`useMemo`实现的引用稳定性是无关紧要的，因为无论如何组件都会重新渲染。这也适用于将结果传递给不关心引用稳定性的React内置组件。
2.  **Props作为依赖项：** 在内部`useCallback`或`useMemo`调用中直接使用非原始类型的props作为依赖项是有问题的，因为组件失去了对prop引用稳定性的控制。这种情况常常因为消费者使用内联函数作为props而被破坏。

来自Sentry代码库的一个真实案例说明了由于上游单个非memoized的值，链式memoization很容易被破坏。本文强调了维护跨组件memoization的难度，并提倡使用替代模式。

作者建议使用“最新引用”模式或等待React的`useEffectEvent`来处理effect内部对最新值的命令式访问，而不会导致不必要的重新渲染。这些解决方案避免了与广泛使用`useCallback`和`useMemo`相关的复杂性和潜在陷阱。

---

## 62. 三星 One UI 8 移除引导程序解锁

**原文标题**: Samsung Removes Bootloader Unlocking with One UI 8

**原文链接**: [https://sammyguru.com/breaking-samsung-removes-bootloader-unlocking-with-one-ui-8/](https://sammyguru.com/breaking-samsung-removes-bootloader-unlocking-with-one-ui-8/)

2025年7月，有猜测称三星的One UI 8.5可能会随Galaxy S26系列一同首次亮相。这一猜测的依据是一个测试版本，该版本表明One UI 8.5 对现有的One UI 8 有显著改进。

然而，文章标题提出了一项令人担忧的进展：据报道，三星将在One UI 8中移除引导加载程序解锁功能。对于那些依赖引导加载程序解锁进行自定义ROM、内核和其他修改的爱好者和开发者来说，这是一个重大转变。如果属实，这将大大限制运行One UI 8及更高版本的三星设备的定制性。

One UI 8.5潜在的软件改进与One UI 8中引导加载程序解锁的限制之间的冲突，给用户带来了一种喜忧参半的感觉。虽然One UI 8.5可能提供增强的功能和性能，但对于那些寻求更深层次地控制其设备和操作系统的人来说，无法解锁引导加载程序可能是一个决定性因素。这一变化的影响还有待观察，但它很可能在Android爱好者社区中引起争议。

---

## 63. 英国启用新的网络安全规则后，VPN使用量激增

**原文标题**: VPN use surges in UK as new online safety rules kick in

**原文链接**: [https://www.ft.com/content/356674b0-9f1d-4f95-b1d5-f27570379a9b](https://www.ft.com/content/356674b0-9f1d-4f95-b1d5-f27570379a9b)

《金融时报》文章“英国新在线安全法规生效，VPN使用量激增”报道称，英国实施新的在线安全法规后，虚拟专用网络 (VPN) 的使用量显着增加。该文章暗示，新法规正在推动这种增长，但法规的具体性质以及 VPN 使用量激增的原因隐藏在付费墙后，需要订阅才能进一步阅读。该文章推广不同的订阅级别以访问完整内容，从基本数字访问到高级数字和印刷选项。它强调了每种订阅的好处，包括全球新闻分析、专家意见、访问金融时报应用程序、时事通讯和独家内容。本质上，该标题表明，英国互联网用户越来越担心与新法规相关的在线隐私和自由，这导致他们采用 VPN 来规避潜在的限制或监控。

---

## 64. 生产型人工智能代理的原则

**原文标题**: Principles for production AI agents

**原文链接**: [https://www.app.build/blog/six-principles-production-ai-agents](https://www.app.build/blog/six-principles-production-ai-agents)

构建有效AI代理的六个关键原则：基于代理开发的实践经验

1. 投资于系统提示：现代LLM对清晰、直接和详细的指令反应最好，而不是操纵技巧。使用LLM生成的草稿进行引导，并保持系统提示静态以获得缓存优势。
2. 分割上下文：提供最少的初始上下文，并允许代理根据需要通过工具获取更多信息，以避免注意力衰减、高成本和延迟。上下文压缩和封装至关重要。
3. 精心设计工具：像API设计一样对待工具设计，但要更加仔细。工具应该简单明了，参数有限，并且在相似的粒度级别上运行。强烈建议使用幂等性。考虑使用DSL方法。
4. 设计反馈循环：实施一个两阶段的演员-评论家方法，其中演员（LLM）采取行动，而评论家根据特定领域的标准（例如，编译、测试、复式记账）验证它们。此循环包括护栏和恢复策略。
5. LLM驱动的错误分析：使用一个元代理循环，包括基线代理、另一个LLM（如具有1M上下文的Gemini）的日志分析，以及基于LLM见解的迭代改进。
6. 令人沮丧的行为表明系统问题：不要立即责怪LLM犯愚蠢的错误。相反，调查潜在的系统错误，例如缺少工具、不清晰的提示或不充分的上下文。

本文强调，构建可靠的AI代理依赖于坚实的系统设计、清晰的指令、精简的上下文管理、强大的工具和自动化验证循环。在LLM的帮助下进行的错误分析对于识别和迭代解决故障模式至关重要。

---

## 65. SRAM Has No Chill: Exploiting Power Domain Separation to Steal On-Chip Secrets

**原文标题**: SRAM Has No Chill: Exploiting Power Domain Separation to Steal On-Chip Secrets

**原文链接**: [https://cacm.acm.org/research-highlights/sram-has-no-chill-exploiting-power-domain-separation-to-steal-on-chip-secrets/](https://cacm.acm.org/research-highlights/sram-has-no-chill-exploiting-power-domain-separation-to-steal-on-chip-secrets/)

生成摘要时出错

---

## 66. Fintech dystopia

**原文标题**: Fintech dystopia

**原文链接**: [https://fintechdystopia.com/](https://fintechdystopia.com/)

生成摘要时出错

---

## 67. Interstellar Comet 3I/Atlas: What We Know Now

**原文标题**: Interstellar Comet 3I/Atlas: What We Know Now

**原文链接**: [https://skyandtelescope.org/astronomy-news/interstellar-comet-3i-atlas-what-we-know-now/](https://skyandtelescope.org/astronomy-news/interstellar-comet-3i-atlas-what-we-know-now/)

生成摘要时出错

---

## 68. ‘I witnessed war crimes’ in Gaza – former worker at GHF aid site [video]

**原文标题**: ‘I witnessed war crimes’ in Gaza – former worker at GHF aid site [video]

**原文链接**: [https://www.bbc.com/news/videos/cy8k8045nx9o](https://www.bbc.com/news/videos/cy8k8045nx9o)

生成摘要时出错

---

## 69. Show HN: Color Me Same – A new kind of logic game

**原文标题**: Show HN: Color Me Same – A new kind of logic game

**原文链接**: [https://color-me-same.franzai.com/](https://color-me-same.franzai.com/)

生成摘要时出错

---

## 70. Shrinkle – Shrink words, find hidden phrase

**原文标题**: Shrinkle – Shrink words, find hidden phrase

**原文链接**: [https://www.shrinkle.org/](https://www.shrinkle.org/)

生成摘要时出错

---

## 71. The Biggest Passenger Planes Keep Breaking Down

**原文标题**: The Biggest Passenger Planes Keep Breaking Down

**原文链接**: [https://www.bloomberg.com/news/articles/2025-07-28/the-world-s-biggest-passenger-planes-keep-breaking-down](https://www.bloomberg.com/news/articles/2025-07-28/the-world-s-biggest-passenger-planes-keep-breaking-down)

生成摘要时出错

---

## 72. FDA has approved Yeztugo, a drug that provides protection against HIV infection

**原文标题**: FDA has approved Yeztugo, a drug that provides protection against HIV infection

**原文链接**: [https://newatlas.com/infectious-diseases/hiv-prevention-fda-lenacapavir/](https://newatlas.com/infectious-diseases/hiv-prevention-fda-lenacapavir/)

This article announces the FDA's approval of Yeztugo (lenacapavir), the first HIV prevention drug offering nearly 100% protection against infection. Administered as a twice-yearly injection, Yeztugo, a capsid inhibitor, prevents HIV from replicating within host cells. Gilead Sciences, the drug's maker, emphasizes its potential to transform HIV prevention and contribute significantly to ending the HIV epidemic, which affects 1.3 million people annually.

Beyond the US, Gilead has filed for regulatory approval in several other countries and partnered with the Global Fund to Fight AIDS, Tuberculosis and Malaria to ensure affordable access in low- and middle-income countries. Gilead will provide the drug at no profit to itself, aiming to reach up to two million people over three years. License-free generics will also be manufactured for use in 120 high-incidence, resource-limited countries. This commitment to global accessibility is highlighted as a crucial step in ensuring that the benefits of this scientific breakthrough reach those who need it most, regardless of location or economic status.


---

## 73. Microsoft Introduces 'Copilot Mode' in Edge

**原文标题**: Microsoft Introduces 'Copilot Mode' in Edge

**原文链接**: [https://blogs.windows.com/msedgedev/2025/07/28/introducing-copilot-mode-in-edge-a-new-way-to-browse-the-web/](https://blogs.windows.com/msedgedev/2025/07/28/introducing-copilot-mode-in-edge-a-new-way-to-browse-the-web/)

生成摘要时出错

---

## 74. RP2350 E9 GPIO erratum fixed in new A4 stepping

**原文标题**: RP2350 E9 GPIO erratum fixed in new A4 stepping

**原文链接**: [https://www.cnx-software.com/2025/07/29/raspberry-pi-rp2350-a4-stepping-fixes-e9-gpio-erratum-9-glitching-bugs-introduces-2mb-flash-variants/](https://www.cnx-software.com/2025/07/29/raspberry-pi-rp2350-a4-stepping-fixes-e9-gpio-erratum-9-glitching-bugs-introduces-2mb-flash-variants/)

生成摘要时出错

---

## 75. Amazon's AI Coding Revealed a Dirty Little Secret

**原文标题**: Amazon's AI Coding Revealed a Dirty Little Secret

**原文链接**: [https://www.bloomberg.com/opinion/articles/2025-07-29/amazon-ai-coding-revealed-a-dirty-little-secret](https://www.bloomberg.com/opinion/articles/2025-07-29/amazon-ai-coding-revealed-a-dirty-little-secret)

生成摘要时出错

---

## 76. Iron Law of Oligarchy

**原文标题**: Iron Law of Oligarchy

**原文链接**: [https://en.wikipedia.org/wiki/Iron_law_of_oligarchy](https://en.wikipedia.org/wiki/Iron_law_of_oligarchy)

生成摘要时出错

---

## 77. Uranium-based catalyst turns air nitrogen into ammonia

**原文标题**: Uranium-based catalyst turns air nitrogen into ammonia

**原文链接**: [https://phys.org/news/2025-07-uranium-based-catalyst-air-nitrogen.html](https://phys.org/news/2025-07-uranium-based-catalyst-air-nitrogen.html)

生成摘要时出错

---

## 78. The Driver of Apple's Exploding Valuation Is Under Threat

**原文标题**: The Driver of Apple's Exploding Valuation Is Under Threat

**原文链接**: [https://www.wsj.com/tech/apple-stock-service-value-growth-analysis-f265a5e7](https://www.wsj.com/tech/apple-stock-service-value-growth-analysis-f265a5e7)

生成摘要时出错

---

## 79. What would an efficient and trustworthy meeting culture look like?

**原文标题**: What would an efficient and trustworthy meeting culture look like?

**原文链接**: [https://abitmighty.com/posts/the-ultimate-meeting-culture](https://abitmighty.com/posts/the-ultimate-meeting-culture)

生成摘要时出错

---

## 80. Robot hand could harvest blackberries better than humans

**原文标题**: Robot hand could harvest blackberries better than humans

**原文链接**: [https://news.uark.edu/articles/79750/robot-hand-could-harvest-blackberries-better-than-humans](https://news.uark.edu/articles/79750/robot-hand-could-harvest-blackberries-better-than-humans)

生成摘要时出错

---

## 81. Show HN: 433 – How to make a font that says nothing

**原文标题**: Show HN: 433 – How to make a font that says nothing

**原文链接**: [https://untested.sonnet.io/notes/433-how-to-make-a-font-that-says-nothing/](https://untested.sonnet.io/notes/433-how-to-make-a-font-that-says-nothing/)

生成摘要时出错

---

## 82. US science left out in the cold amid plans to retire Antarctic icebreaker

**原文标题**: US science left out in the cold amid plans to retire Antarctic icebreaker

**原文链接**: [https://www.theregister.com/2025/07/29/us_icebreaker_funding/](https://www.theregister.com/2025/07/29/us_icebreaker_funding/)

生成摘要时出错

---

## 83. Blackstone executive among four people killed in Midtown NYC shooting

**原文标题**: Blackstone executive among four people killed in Midtown NYC shooting

**原文链接**: [https://nypost.com/2025/07/29/us-news/blackstone-executive-and-nypd-officer-among-four-killed-in-midtown-office-shooting-spree/](https://nypost.com/2025/07/29/us-news/blackstone-executive-and-nypd-officer-among-four-killed-in-midtown-office-shooting-spree/)

生成摘要时出错

---

## 84. LLM Embeddings Explained: A Visual and Intuitive Guide

**原文标题**: LLM Embeddings Explained: A Visual and Intuitive Guide

**原文链接**: [https://huggingface.co/spaces/hesamation/primer-llm-embedding](https://huggingface.co/spaces/hesamation/primer-llm-embedding)

生成摘要时出错

---

## 85. Interview with the US military's chief orbital traffic cop

**原文标题**: Interview with the US military's chief orbital traffic cop

**原文链接**: [https://arstechnica.com/science/2025/07/ars-spoke-with-the-militarys-chief-orbital-traffic-cop-heres-what-we-learned/](https://arstechnica.com/science/2025/07/ars-spoke-with-the-militarys-chief-orbital-traffic-cop-heres-what-we-learned/)

生成摘要时出错

---

## 86. Performance and telemetry analysis of Trae IDE, ByteDance's VSCode fork

**原文标题**: Performance and telemetry analysis of Trae IDE, ByteDance's VSCode fork

**原文链接**: [https://github.com/segmentationf4u1t/trae_telemetry_research](https://github.com/segmentationf4u1t/trae_telemetry_research)

生成摘要时出错

---

## 87. The Geological Sublime

**原文标题**: The Geological Sublime

**原文链接**: [https://harpers.org/archive/2025/07/the-geological-sublime-lewis-hyde-deep-time/](https://harpers.org/archive/2025/07/the-geological-sublime-lewis-hyde-deep-time/)

生成摘要时出错

---

## 88. Show HN: Same prompt tested across Replit, Bolt, v0, Lovable and Raq.com

**原文标题**: Show HN: Same prompt tested across Replit, Bolt, v0, Lovable and Raq.com

**原文链接**: [https://raq.com/real-world-test](https://raq.com/real-world-test)

生成摘要时出错

---

## 89. Félix Nadar: the first celebrity photographer (2019)

**原文标题**: Félix Nadar: the first celebrity photographer (2019)

**原文链接**: [https://www.bbc.com/culture/article/20190114-flix-nadar-the-worlds-first-celebrity-photographer](https://www.bbc.com/culture/article/20190114-flix-nadar-the-worlds-first-celebrity-photographer)

生成摘要时出错

---

## 90. Debian switches to 64-bit time for everything

**原文标题**: Debian switches to 64-bit time for everything

**原文链接**: [https://www.theregister.com/2025/07/25/y2k38_bug_debian/](https://www.theregister.com/2025/07/25/y2k38_bug_debian/)

生成摘要时出错

---

## 91. Dumb Pipe

**原文标题**: Dumb Pipe

**原文链接**: [https://www.dumbpipe.dev/](https://www.dumbpipe.dev/)

生成摘要时出错

---

## 92. LLMs can now identify public figures in images

**原文标题**: LLMs can now identify public figures in images

**原文链接**: [https://minimaxir.com/2025/07/llms-identify-people/](https://minimaxir.com/2025/07/llms-identify-people/)

生成摘要时出错

---

## 93. The leverage arbitrage: Why everything feels broken

**原文标题**: The leverage arbitrage: Why everything feels broken

**原文链接**: [https://tushardadlani.com/the-leverage-arbitrage-why-everything-feels-broken](https://tushardadlani.com/the-leverage-arbitrage-why-everything-feels-broken)

生成摘要时出错

---

## 94. 200k Flemish drivers can turn traffic lights green

**原文标题**: 200k Flemish drivers can turn traffic lights green

**原文链接**: [https://www.vrt.be/vrtnws/en/2025/07/24/200-000-flemish-drivers-can-turn-traffic-lights-green-but-waze/](https://www.vrt.be/vrtnws/en/2025/07/24/200-000-flemish-drivers-can-turn-traffic-lights-green-but-waze/)

生成摘要时出错

---

## 95. Terminal app can now run full graphical Linux apps in the latest Android Canary

**原文标题**: Terminal app can now run full graphical Linux apps in the latest Android Canary

**原文链接**: [https://www.androidauthority.com/linux-terminal-graphical-apps-3580905/](https://www.androidauthority.com/linux-terminal-graphical-apps-3580905/)

生成摘要时出错

---

## 96. Structural-Demographic Theory

**原文标题**: Structural-Demographic Theory

**原文链接**: [https://peterturchin.com/structural-demographic-theory/](https://peterturchin.com/structural-demographic-theory/)

生成摘要时出错

---

## 97. Claude Code Router

**原文标题**: Claude Code Router

**原文链接**: [https://github.com/musistudio/claude-code-router](https://github.com/musistudio/claude-code-router)

生成摘要时出错

---

## 98. A Photonic SRAM with Embedded XOR Logic for Ultra-Fast In-Memory Computing

**原文标题**: A Photonic SRAM with Embedded XOR Logic for Ultra-Fast In-Memory Computing

**原文链接**: [https://arxiv.org/abs/2506.22707](https://arxiv.org/abs/2506.22707)

生成摘要时出错

---

## 99. How I fixed my blog's performance issues by writing a new Jekyll plugin

**原文标题**: How I fixed my blog's performance issues by writing a new Jekyll plugin

**原文链接**: [https://arclight.run/how-i-fixed-my-blogs-performance-issues-by-writing-a-new-jekyll-plugin-jekyll-skyhook/](https://arclight.run/how-i-fixed-my-blogs-performance-issues-by-writing-a-new-jekyll-plugin-jekyll-skyhook/)

生成摘要时出错

---

## 100. Show HN: I made a tool to generate photomosaics with your pictures

**原文标题**: Show HN: I made a tool to generate photomosaics with your pictures

**原文链接**: [https://pictiler.com](https://pictiler.com)

生成摘要时出错

---

