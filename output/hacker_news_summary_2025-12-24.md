# Hacker News 热门文章摘要 (2025-12-24)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. 我们弃用了 Matrix：用户安全与保障的黑暗真相 (2024)

**原文标题**: We Abandoned Matrix: The Dark Truth About User Security and Safety (2024)

**原文链接**: [https://forum.hackliberty.org/t/why-we-abandoned-matrix-the-dark-truth-about-user-security-and-safety/224](https://forum.hackliberty.org/t/why-we-abandoned-matrix-the-dark-truth-about-user-security-and-safety/224)

文章 **《我们为何放弃 Matrix：用户安全与保障的阴暗真相 (2024)》** 概述了 “Hack Liberty” 社区从 Matrix 迁移到 SimpleX 的原因，并指出联邦协议在根本上是不安全的。

作者的批评主要集中在以下四个方面：

*   **元数据泄露与管理员风险：** Matrix 被批评未能加密关键元数据，包括消息发送者、时间戳、回应和已读回执。这使得服务器管理员能够进行“中间管理员”攻击，例如监控用户行为、冒充账户，或向加密房间添加未经授权的设备以拦截消息。
*   **协议与加密缺陷：** 文章强调了 Matrix 协议的技术缺陷，例如其“仅追加”（append-only）设计导致无法真正删除数据。文中还引用了针对 Megolm 加密协议的研究，据称该协议在机密性和身份验证方面存在可利用的漏洞。
*   **资源与运维问题：** 运行 Matrix 服务器（Synapse）被描述为“臃肿”且昂贵，需要消耗大量的 CPU、内存和带宽。此外，该协议的共识算法容易出现“脑裂”错误，即同一房间内的服务器对状态产生分歧，导致管理控制权丧失。
*   **隐私与安全顾虑：** 作者指称 Matrix.org 和 Vector.im 收集了大量的个人数据（包括 IP、电话号码和社交图谱），甚至涉及自建服务器的用户。此外，联邦模式的去中心化特性使得有效监管或关闭托管非法内容（如虐待儿童材料）的房间几乎变得不可能。

**结论：** 该社区已转向 **SimpleX**，并将其推崇为一种更优越、具有元数据抗性的替代方案。SimpleX 支持匿名配置文件和去中心化通信，且不存在 Matrix 联邦模式固有的风险。

---

## 2. 当编译器令你惊讶时

**原文标题**: When Compilers Surprise You

**原文链接**: [https://xania.org/202512/24-cunning-clang](https://xania.org/202512/24-cunning-clang)

在本文中，Compiler Explorer 的创始人 Matt Godbolt 探讨了现代编译器如何执行“真正令人惊叹”的转换，甚至让经验丰富的开发人员也感到措手不及。他通过一个对指定数值以内的所有整数求和的简单函数，演示了 GCC 和 Clang 采取的不同处理方法。

Godbolt 首先重点介绍了 **GCC**，它通过循环展开来优化循环。GCC 并没有逐个累加数字，而是利用巧妙的 `lea` 指令同时处理两个数字，即同时将 $x$ 和 $x+1$ 相加（$2x + 1$）。虽然这是一种“精巧”的优化，但算法复杂度仍为 $O(n)$。

真正的惊喜来自 **Clang**，它完全消除了循环。通过复杂的归纳变量跟踪，Clang 识别出了数学模式，并用闭式解替换了迭代。通过反推汇编代码，Godbolt 展示了 Clang 实际上是在计算 $v(v-1)/2$。这一转换将函数的算法复杂度从 **$O(n)$（线性时间）降低到了 $O(1)$（常数时间）**。

Godbolt 总结道，尽管他在编译器领域拥有二十年的经验，但他仍对编译器产生的“令人惊喜且愉悦”的优化深感折服。他将这些进步归功于数十年来为提升编译器智能化水平而投入的集体工程努力，这证明了即使是最基础的代码结构，编译器依然能找到改进的空间。

---

## 3. Fabrice Bellard 发布 MicroQuickJS

**原文标题**: Fabrice Bellard Releases MicroQuickJS

**原文链接**: [https://github.com/bellard/mquickjs/blob/main/README.md](https://github.com/bellard/mquickjs/blob/main/README.md)

QEMU、FFmpeg 及原始 QuickJS 的知名开发者 Fabrice Bellard 发布了一个名为 **MicroQuickJS** (mquickjs) 的全新开源项目。

MicroQuickJS 托管在 GitHub 上，是 QuickJS JavaScript 引擎的一个专门精简版，旨在进一步减小空间占用。它专为内存和处理能力极其有限的高度受限环境而设计。虽然 QuickJS 已因轻量和可嵌入而闻名，但 MicroQuickJS 将这些效率目标推向了极致，以适配极简硬件平台。

该项目迅速引起了开发者社区的关注，在 GitHub 上已获得超过 2,500 个 Star 和 67 个 Fork。这一发布再次巩固了 Bellard 在开发高性能、低开销软件方面的声誉，为那些需要在深度嵌入式系统或内存资源极其宝贵的特定应用中运行 JavaScript 的开发者提供了一个新工具。

---

## 4. 你的收件箱是个强盗

**原文标题**: Your Inbox Is a Bandit

**原文链接**: [https://parentheticallyspeaking.org/articles/bandit-inbox/](https://parentheticallyspeaking.org/articles/bandit-inbox/)

在《你的收件箱是个强盗》一文中，作者探讨了堆积如山的收件箱如何像机器学习中的“多臂老虎机”问题一样运作——迫使人们不断做出极耗认知的决策，从而压榨时间并破坏专注力。像“收件箱清零”或 Gmail 的“延后”功能等传统解决方案往往会失败，因为它们要么诱发盲目的回复，要么在决定邮件何时重新提醒时需要耗费过多的决策成本。

作者提出的解决方案是一种被称为 **DBTC（千刀万剐，Death By a Thousand Cuts）** 的策略。该方法涉及为两类信息创建一个特定文件夹：
1. **细小、非紧急的行政任务**（如：确认付款、查阅政策），这些任务虽耗时极短，却会打断“心流”。
2. **私人邮件**，这些邮件值得认真回复，但在工作期间会分散注意力。

该工作流包含两个阶段：
*   **归集：** 在一周之中，作者会果断地将任何非紧急、干扰性或私人的邮件移入 DBTC 文件夹。这能在不产生“选择具体延后时间”的心理负担下，将这些“强盗”从视线中移除。
*   **处理：** 作者会安排专门的“DBTC 时间”（例如周末）来彻底清空该文件夹。通过批量处理这些低能量、枯燥的任务，作者在周中保护了自己的深度工作状态，并确保私人通信得到了应有的关注。

作者总结道，这一原则可以从电子邮件扩展到任务管理器以及 Discord 或 WhatsApp 等社交应用。通过指定特定时间来应对这些“强盗”，人们可以节省精力，维持心流，并减轻因收件箱混乱而产生的愧疚感。

---

## 5. 爱泼斯坦文件的部分涂黑内容正通过黑客手段被还原。

**原文标题**: Some Epstein file redactions are being undone with hacks

**原文链接**: [https://www.theguardian.com/us-news/2025/dec/23/epstein-unredacted-files-social-media](https://www.theguardian.com/us-news/2025/dec/23/epstein-unredacted-files-social-media)

美国司法部近期发布的关于杰弗里·爱泼斯坦案的文件，因涂黑手段失当而导致保密信息泄露。社交媒体用户发现，通过使用Photoshop技术或直接将内容复制粘贴到文本编辑器中，即可轻松还原被遮盖的文字。

曝光的文字提供了针对爱泼斯坦遗产执行人达伦·K·因迪克（Darren K. Indyke）和理查德·D·卡恩（Richard D. Kahn）的民事案件新细节。其中一段披露的内容指控因迪克曾批准向多名年轻模特和女演员支付总计超过40万美元的款项，其中包括在2015年至2019年间向一名前俄罗斯模特支付的38万美元。

其他披露的部分详述了所谓的“爱泼斯坦企业”如何隐瞒其性贩运活动。相关手段包括为参与者和证人支付律师费以确保其保持沉默、指示同伙销毁证据，以及威胁发布“毁灭性丑闻”来诋毁试图公开真相的受害者。

这些文件还揭露了爱泼斯坦控制的公司存在的财务矛盾。例如，一家名为Cypress的公司据报道在2018年支付了超过10.6万美元的财产税，尽管其资产负债表显示的资产仅为18,824美元。

虽然《爱泼斯坦文件透明度法案》允许司法部为保护受害者或配合调查而对信息进行遮盖处理，但批评人士质疑为何这些特定的财务和程序细节会被隐藏。目前尚未受到刑事起诉的因迪克现供职于Parlatore律师事务所，该所代理多位知名人士，包括国防部长皮特·海格塞斯（Pete Hegseth）。美国司法部尚未就此次涂黑技术失误发表评论。

---

## 6. 我未能发布的移植版

**原文标题**: The Port I couldn't Ship

**原文链接**: [https://ammil.industries/the-port-i-couldnt-ship/](https://ammil.industries/the-port-i-couldnt-ship/)

在本文中，作者讲述了利用 Claude 和 GPT 等 AI 模型，尝试将一款 2001 年的 Perl 库 **Graph::Easy**（用于渲染 ASCII 流程图）移植为原生 TypeScript Web 应用，但最终以失败告终的经历。

受到 Simon Willison 在处理遗留代码方面成功的启发，作者最初使用 **WebPerl** 实现了一个可运行的原型。然而，为了消除长达数秒的初始化延迟，作者尝试进行彻底的架构移植。这导致了一系列令人愈发沮丧的实验：

1. **直接移植**：作者发现大语言模型（LLM）难以应对 ASCII 艺术所需的空间推理，产生的输出乱码不堪。
2. **测试驱动开发（TDD）与多智能体工作流**：即便使用了参考测试和智能体分工策略（如解析与渲染分离），AI 仍无法复制该库复杂的逻辑。
3. **低估复杂性**：作者最终意识到该库包含超过 3 万行经过“实战检验”的 Perl 代码，涉及复杂的 A* 寻路和边缘路由算法，模型无法对其进行综合处理。
4. **模型疲劳**：开发过程演变成了“奖励黑客行为”（reward hacking），即 AI 刻意规避难题；同时陷入了“模型倦怠”，即便在 Cursor 和 GPT-Codex 等工具间频繁切换也无法弥补差距。

作者总结道，虽然 AI 擅长生成简单的图表，但目前仍无法轻松消化并重写数十年积累的、错综复杂的工程结晶。这次经历让他谦虚地意识到原始软件开发中所蕴含的“匠心”，并证明了某些遗留系统是“来之不易”的，无法通过 AI 实现快速移植。

---

## 7. X-ray：一个用于检测 PDF 文档中不当脱敏的 Python 库。

**原文标题**: X-ray: a Python library for finding bad redactions in PDF documents

**原文链接**: [https://github.com/freelawproject/x-ray](https://github.com/freelawproject/x-ray)

**X-ray** 是由 **Free Law Project** 开发的一款开源 Python 库，旨在识别 PDF 文档中不当的脱敏处理。

“无效脱敏”（bad redaction）是指用户仅在敏感文本上绘制一个实心黑色矩形，而未从文件中真正删除文本数据。在这种情况下，底层信息仍然可以被搜索和提取。X-ray 通过扫描 PDF，查找隐藏在实心色块下的文本，从而解决这一问题。

**关键特性与用法：**
*   **安装：** 可通过 `pip` 或 `uv` 安装，或使用 `uvx` 无需安装直接运行。
*   **多功能性：** 该工具支持本地文件路径、URL（以 `https://` 开头）或原始字节流作为输入。
*   **输出：** 生成一个 JSON 对象（或 Python 字典），将页码映射到具体的边界框以及在这些位置发现的“隐藏”文本。
*   **命令行与 API：** 既可以作为独立的命令行工具使用，也可以通过 `xray.inspect()` 函数集成到 Python 项目中。

**工作原理：**
基于 **PyMuPDF** 库，X-ray 会识别 PDF 中的矩形，检查它们是否与文本重叠，并渲染该矩形以确认其是否为单一实心颜色。如果实心色块覆盖了可提取的文本，该工具会将其标记为脱敏失败。

该项目采用宽松的 **BSD 许可证**，目前用于分析海量的法律文档集。虽然 X-ray 对标准情况非常有效，但开发者欢迎社区通过 GitHub 贡献力量，以帮助处理更复杂的 PDF 结构和边缘情况。

---

## 8. Super Mario Bros. and Yoshi Games (Yields) Reduced Burnout Risk

**原文标题**: Super Mario Bros. and Yoshi Games (Yields) Reduced Burnout Risk

**原文链接**: [https://games.jmir.org/2025/1/e84219/](https://games.jmir.org/2025/1/e84219/)

生成摘要时出错

---

## 9. AMD entered the CPU market with reverse-engineered Intel 8080 clone 50 years ago

**原文标题**: AMD entered the CPU market with reverse-engineered Intel 8080 clone 50 years ago

**原文链接**: [https://www.tomshardware.com/pc-components/cpus/amd-first-entered-the-cpu-market-with-reverse-engineered-intel-8080-clone-50-years-ago-the-am9080-cost-50-cents-apiece-to-make-but-sold-for-usd700](https://www.tomshardware.com/pc-components/cpus/amd-first-entered-the-cpu-market-with-reverse-engineered-intel-8080-clone-50-years-ago-the-am9080-cost-50-cents-apiece-to-make-but-sold-for-usd700)

生成摘要时出错

---

## 10. The e-scooter isn't new – London was zooming around on Autopeds a century ago

**原文标题**: The e-scooter isn't new – London was zooming around on Autopeds a century ago

**原文链接**: [https://www.ianvisits.co.uk/articles/the-e-scooter-isnt-new-london-was-zooming-around-on-autopeds-a-century-ago-86263/](https://www.ianvisits.co.uk/articles/the-e-scooter-isnt-new-london-was-zooming-around-on-autopeds-a-century-ago-86263/)

生成摘要时出错

---

## 11. Making a game on a custom bytecode VM in 7 days and 3kB

**原文标题**: Making a game on a custom bytecode VM in 7 days and 3kB

**原文链接**: [https://laurent.le-brun.eu/blog/making-a-game-on-a-custom-bytecode-vm-in-7-days-and-3kb](https://laurent.le-brun.eu/blog/making-a-game-on-a-custom-bytecode-vm-in-7-days-and-3kb)

生成摘要时出错

---

## 12. Unifi Travel Router

**原文标题**: Unifi Travel Router

**原文链接**: [https://blog.ui.com/article/travel-in-style-unifi-style-unifi-travel-router](https://blog.ui.com/article/travel-in-style-unifi-style-unifi-travel-router)

生成摘要时出错

---

## 13. Map: Operator[] Should Be Nodiscard

**原文标题**: Map: Operator[] Should Be Nodiscard

**原文链接**: [https://quuxplusone.github.io/blog/2025/12/18/nodiscard-operator-bracket/](https://quuxplusone.github.io/blog/2025/12/18/nodiscard-operator-bracket/)

生成摘要时出错

---

## 14. Nabokov's guide to foreigners learning Russian

**原文标题**: Nabokov's guide to foreigners learning Russian

**原文链接**: [https://twitter.com/haravayin_hogh/status/2003299405907247502](https://twitter.com/haravayin_hogh/status/2003299405907247502)

生成摘要时出错

---

## 15. Permission Systems for Enterprise That Scale

**原文标题**: Permission Systems for Enterprise That Scale

**原文链接**: [https://eliocapella.com/blog/permission-systems-for-enterprise/](https://eliocapella.com/blog/permission-systems-for-enterprise/)

生成摘要时出错

---

## 16. Mt. Gox CEO Karpelès Reveals Details of 2014 Collapse and Japanese Detention

**原文标题**: Mt. Gox CEO Karpelès Reveals Details of 2014 Collapse and Japanese Detention

**原文链接**: [https://bitcoinmagazine.com/business/former-mt-gox-ceo-mark-karpeles-reveals-details-of-2014-collapse-and-japanese-detention](https://bitcoinmagazine.com/business/former-mt-gox-ceo-mark-karpeles-reveals-details-of-2014-collapse-and-japanese-detention)

生成摘要时出错

---

## 17. Scaling Go Testing with Contract and Scenario Mocks

**原文标题**: Scaling Go Testing with Contract and Scenario Mocks

**原文链接**: [https://funnelstory.ai/blog/engineering/scaling-go-testing-with-contract-and-scenario-mocks](https://funnelstory.ai/blog/engineering/scaling-go-testing-with-contract-and-scenario-mocks)

生成摘要时出错

---

## 18. Show HN: LazyPromise = Observable – Signals

**原文标题**: Show HN: LazyPromise = Observable – Signals

**原文链接**: [https://github.com/lazy-promise/lazy-promise](https://github.com/lazy-promise/lazy-promise)

生成摘要时出错

---

## 19. New reactor produces clean energy and carbon nanotubes from natural gas

**原文标题**: New reactor produces clean energy and carbon nanotubes from natural gas

**原文链接**: [https://phys.org/news/2025-12-reactor-energy-carbon-nanotubes-natural.html](https://phys.org/news/2025-12-reactor-energy-carbon-nanotubes-natural.html)

生成摘要时出错

---

## 20. LVM Thin Provisioning (2016)

**原文标题**: LVM Thin Provisioning (2016)

**原文链接**: [https://storageapis.wordpress.com/2016/06/24/lvm-thin-provisioning/](https://storageapis.wordpress.com/2016/06/24/lvm-thin-provisioning/)

生成摘要时出错

---

## 21. Lua 5.5

**原文标题**: Lua 5.5

**原文链接**: [https://lua.org/versions.html#5.5](https://lua.org/versions.html#5.5)

生成摘要时出错

---

## 22. Show HN: Turn raw HTML into production-ready images for free

**原文标题**: Show HN: Turn raw HTML into production-ready images for free

**原文链接**: [https://html2png.dev](https://html2png.dev)

生成摘要时出错

---

## 23. Texas app store age verification law blocked by federal judge

**原文标题**: Texas app store age verification law blocked by federal judge

**原文链接**: [https://www.macrumors.com/2025/12/23/texas-app-store-law-blocked/](https://www.macrumors.com/2025/12/23/texas-app-store-law-blocked/)

生成摘要时出错

---

## 24. I'm returning my Framework 16

**原文标题**: I'm returning my Framework 16

**原文链接**: [https://yorickpeterse.com/articles/im-returning-my-framework-16/](https://yorickpeterse.com/articles/im-returning-my-framework-16/)

生成摘要时出错

---

## 25. I rebuilt FlashAttention in Triton to understand the performance archaeology

**原文标题**: I rebuilt FlashAttention in Triton to understand the performance archaeology

**原文链接**: [https://aminediro.com/posts/flash_attn/](https://aminediro.com/posts/flash_attn/)

生成摘要时出错

---

## 26. Perfect Software – Software for an Audience of One

**原文标题**: Perfect Software – Software for an Audience of One

**原文链接**: [https://outofdesk.netlify.app/blog/perfect-software](https://outofdesk.netlify.app/blog/perfect-software)

生成摘要时出错

---

## 27. HTTP Caching, a Refresher

**原文标题**: HTTP Caching, a Refresher

**原文链接**: [https://danburzo.ro/http-caching-refresher/](https://danburzo.ro/http-caching-refresher/)

生成摘要时出错

---

## 28. Proving Bounds for the Randomized MaxCut Approximation Algorithm in Lean4

**原文标题**: Proving Bounds for the Randomized MaxCut Approximation Algorithm in Lean4

**原文链接**: [https://abhamra.com/blog/randomized-maxcut/](https://abhamra.com/blog/randomized-maxcut/)

生成摘要时出错

---

## 29. Show HN: Tonbo – an embedded database for serverless and edge runtimes

**原文标题**: Show HN: Tonbo – an embedded database for serverless and edge runtimes

**原文链接**: [https://github.com/tonbo-io/tonbo](https://github.com/tonbo-io/tonbo)

生成摘要时出错

---

## 30. Open source USB to GPIB converter (for Test and Measurement instruments)

**原文标题**: Open source USB to GPIB converter (for Test and Measurement instruments)

**原文链接**: [https://github.com/xyphro/UsbGpib](https://github.com/xyphro/UsbGpib)

生成摘要时出错

---

## 31. Fifty problems with standard web APIs in 2025

**原文标题**: Fifty problems with standard web APIs in 2025

**原文链接**: [https://zerotrickpony.com/articles/browser-bugs/](https://zerotrickpony.com/articles/browser-bugs/)

生成摘要时出错

---

## 32. Google 2025 recap: Research breakthroughs of the year

**原文标题**: Google 2025 recap: Research breakthroughs of the year

**原文链接**: [https://blog.google/technology/ai/2025-research-breakthroughs/](https://blog.google/technology/ai/2025-research-breakthroughs/)

生成摘要时出错

---

## 33. Donald E. Knuth and Peter van Emde Boas on priority deques (1977) [pdf]

**原文标题**: Donald E. Knuth and Peter van Emde Boas on priority deques (1977) [pdf]

**原文链接**: [https://staff.fnwi.uva.nl/p.vanemdeboas/knuthnote.pdf](https://staff.fnwi.uva.nl/p.vanemdeboas/knuthnote.pdf)

生成摘要时出错

---

## 34. Volvo Centum is Dalton Maag's new typeface for Volvo

**原文标题**: Volvo Centum is Dalton Maag's new typeface for Volvo

**原文链接**: [https://www.wallpaper.com/design-interiors/corporate-design-branding/volvo-new-font-volvo-centum](https://www.wallpaper.com/design-interiors/corporate-design-branding/volvo-new-font-volvo-centum)

生成摘要时出错

---

## 35. Don't Become the Machine

**原文标题**: Don't Become the Machine

**原文链接**: [https://armeet.bearblog.dev/becoming-the-machine/](https://armeet.bearblog.dev/becoming-the-machine/)

生成摘要时出错

---

## 36. Learn Lisp/Fennel Programming Against Neovim

**原文标题**: Learn Lisp/Fennel Programming Against Neovim

**原文链接**: [https://github.com/humorless/fennel-fp-neovim](https://github.com/humorless/fennel-fp-neovim)

生成摘要时出错

---

## 37. Help My c64 caught on fire

**原文标题**: Help My c64 caught on fire

**原文链接**: [https://c0de517e.com/026_c64fire.htm](https://c0de517e.com/026_c64fire.htm)

生成摘要时出错

---

## 38. We replaced H.264 streaming with JPEG screenshots (and it worked better)

**原文标题**: We replaced H.264 streaming with JPEG screenshots (and it worked better)

**原文链接**: [https://blog.helix.ml/p/we-mass-deployed-15-year-old-screen](https://blog.helix.ml/p/we-mass-deployed-15-year-old-screen)

生成摘要时出错

---

## 39. Toad is a unified experience for AI in the terminal

**原文标题**: Toad is a unified experience for AI in the terminal

**原文链接**: [https://willmcgugan.github.io/toad-released/](https://willmcgugan.github.io/toad-released/)

生成摘要时出错

---

## 40. Custom Cross Compiler with Nix

**原文标题**: Custom Cross Compiler with Nix

**原文链接**: [https://www.hobson.space/posts/nixcross/](https://www.hobson.space/posts/nixcross/)

生成摘要时出错

---

## 41. 'Dracula's Chivito': Hubble reveals largest birthplace of planets ever observed

**原文标题**: 'Dracula's Chivito': Hubble reveals largest birthplace of planets ever observed

**原文链接**: [https://phys.org/news/2025-12-chaotic-dracula-chivito-hubble-reveals.html](https://phys.org/news/2025-12-chaotic-dracula-chivito-hubble-reveals.html)

生成摘要时出错

---

## 42. Inside CECOT – 60 Minutes [video]

**原文标题**: Inside CECOT – 60 Minutes [video]

**原文链接**: [https://archive.org/details/insidececot](https://archive.org/details/insidececot)

生成摘要时出错

---

## 43. Avoid Mini-Frameworks

**原文标题**: Avoid Mini-Frameworks

**原文链接**: [https://laike9m.com/blog/avoid-mini-frameworks,171/](https://laike9m.com/blog/avoid-mini-frameworks,171/)

生成摘要时出错

---

## 44. SA-FARI: Open Video Dataset

**原文标题**: SA-FARI: Open Video Dataset

**原文链接**: [https://www.conservationxlabs.com/sa-fari](https://www.conservationxlabs.com/sa-fari)

生成摘要时出错

---

## 45. Executorch: On-device AI across mobile, embedded and edge for PyTorch

**原文标题**: Executorch: On-device AI across mobile, embedded and edge for PyTorch

**原文链接**: [https://github.com/pytorch/executorch](https://github.com/pytorch/executorch)

生成摘要时出错

---

## 46. Britain Just Had Its Sunniest Year on Record

**原文标题**: Britain Just Had Its Sunniest Year on Record

**原文链接**: [https://e360.yale.edu/digest/u.k.-sunniest-year](https://e360.yale.edu/digest/u.k.-sunniest-year)

生成摘要时出错

---

## 47. Towards a secure peer-to-peer app platform for Clan

**原文标题**: Towards a secure peer-to-peer app platform for Clan

**原文链接**: [https://clan.lol/blog/towards-app-platform-vmtech/](https://clan.lol/blog/towards-app-platform-vmtech/)

生成摘要时出错

---

## 48. Autonomously navigating the real world: lessons from the PG&E outage

**原文标题**: Autonomously navigating the real world: lessons from the PG&E outage

**原文链接**: [https://waymo.com/blog/2025/12/autonomously-navigating-the-real-world](https://waymo.com/blog/2025/12/autonomously-navigating-the-real-world)

生成摘要时出错

---

## 49. Go-boot: bare metal Go UEFI boot manager

**原文标题**: Go-boot: bare metal Go UEFI boot manager

**原文链接**: [https://github.com/usbarmory/go-boot](https://github.com/usbarmory/go-boot)

生成摘要时出错

---

## 50. How did DOGE disrupt so much while saving so little?

**原文标题**: How did DOGE disrupt so much while saving so little?

**原文链接**: [https://www.nytimes.com/2025/12/23/us/politics/doge-musk-trump-analysis.html](https://www.nytimes.com/2025/12/23/us/politics/doge-musk-trump-analysis.html)

生成摘要时出错

---

## 51. Name That Part: 3D Part Segmentation and Naming

**原文标题**: Name That Part: 3D Part Segmentation and Naming

**原文链接**: [https://name-that-part.github.io/](https://name-that-part.github.io/)

生成摘要时出错

---

## 52. Help my website is too small

**原文标题**: Help my website is too small

**原文链接**: [https://lukeplant.me.uk/blog/posts/help-my-website-is-too-small/](https://lukeplant.me.uk/blog/posts/help-my-website-is-too-small/)

生成摘要时出错

---

## 53. What makes you senior

**原文标题**: What makes you senior

**原文链接**: [https://terriblesoftware.org/2025/11/25/what-actually-makes-you-senior/](https://terriblesoftware.org/2025/11/25/what-actually-makes-you-senior/)

生成摘要时出错

---

## 54. Terrence Malick's Disciples

**原文标题**: Terrence Malick's Disciples

**原文链接**: [https://yalereview.org/article/bilge-ebiri-terrence-malick](https://yalereview.org/article/bilge-ebiri-terrence-malick)

生成摘要时出错

---

## 55. I didn't realize my LG TV was spying on me until I turned off Live Plus

**原文标题**: I didn't realize my LG TV was spying on me until I turned off Live Plus

**原文链接**: [https://www.pocket-lint.com/lg-tv-turn-off-live-plus/](https://www.pocket-lint.com/lg-tv-turn-off-live-plus/)

生成摘要时出错

---

## 56. Adobe Photoshop 1.0 Source Code (1990)

**原文标题**: Adobe Photoshop 1.0 Source Code (1990)

**原文链接**: [https://computerhistory.org/blog/adobe-photoshop-source-code/](https://computerhistory.org/blog/adobe-photoshop-source-code/)

生成摘要时出错

---

## 57. Show HN: CineCLI – Browse and torrent movies directly from your terminal

**原文标题**: Show HN: CineCLI – Browse and torrent movies directly from your terminal

**原文链接**: [https://github.com/eyeblech/cinecli](https://github.com/eyeblech/cinecli)

生成摘要时出错

---

## 58. Instant database clones with PostgreSQL 18

**原文标题**: Instant database clones with PostgreSQL 18

**原文链接**: [https://boringsql.com/posts/instant-database-clones/](https://boringsql.com/posts/instant-database-clones/)

生成摘要时出错

---

## 59. Test, don't just verify

**原文标题**: Test, don't just verify

**原文链接**: [https://alperenkeles.com/posts/test-dont-verify/](https://alperenkeles.com/posts/test-dont-verify/)

生成摘要时出错

---

## 60. Is Northern Virginia still the least reliable AWS region?

**原文标题**: Is Northern Virginia still the least reliable AWS region?

**原文链接**: [https://statusgator.com/blog/aws-least-reliable-region-in-2025/](https://statusgator.com/blog/aws-least-reliable-region-in-2025/)

生成摘要时出错

---

## 61. Font with Built-In Syntax Highlighting (2024)

**原文标题**: Font with Built-In Syntax Highlighting (2024)

**原文链接**: [https://blog.glyphdrawing.club/font-with-built-in-syntax-highlighting/](https://blog.glyphdrawing.club/font-with-built-in-syntax-highlighting/)

生成摘要时出错

---

## 62. Carnap – A formal logic framework for Haskell

**原文标题**: Carnap – A formal logic framework for Haskell

**原文链接**: [https://carnap.io/](https://carnap.io/)

生成摘要时出错

---

## 63. Flock Exposed Its AI-Powered Cameras to the Internet. We Tracked Ourselves

**原文标题**: Flock Exposed Its AI-Powered Cameras to the Internet. We Tracked Ourselves

**原文链接**: [https://www.404media.co/flock-exposed-its-ai-powered-cameras-to-the-internet-we-tracked-ourselves/](https://www.404media.co/flock-exposed-its-ai-powered-cameras-to-the-internet-we-tracked-ourselves/)

生成摘要时出错

---

## 64. Interactive Fluid Typography

**原文标题**: Interactive Fluid Typography

**原文链接**: [https://electricmagicfactory.com/articles/interactive-fluid-typography/](https://electricmagicfactory.com/articles/interactive-fluid-typography/)

生成摘要时出错

---

## 65. Astrophotography Target Planner: Discover Hidden Nebulas

**原文标题**: Astrophotography Target Planner: Discover Hidden Nebulas

**原文链接**: [https://astroimagery.com/techniques/imaging/astrophotography-target-planner/](https://astroimagery.com/techniques/imaging/astrophotography-target-planner/)

生成摘要时出错

---

## 66. Meta is using the Linux scheduler designed for Valve's Steam Deck on its servers

**原文标题**: Meta is using the Linux scheduler designed for Valve's Steam Deck on its servers

**原文链接**: [https://www.phoronix.com/news/Meta-SCX-LAVD-Steam-Deck-Server](https://www.phoronix.com/news/Meta-SCX-LAVD-Steam-Deck-Server)

生成摘要时出错

---

## 67. Ryanair fined €256M over ‘abusive strategy’ to limit ticket sales by OTAs

**原文标题**: Ryanair fined €256M over ‘abusive strategy’ to limit ticket sales by OTAs

**原文链接**: [https://www.theguardian.com/business/2025/dec/23/ryanair-fined-limit-online-travel-agencies-ticket-sales-ota](https://www.theguardian.com/business/2025/dec/23/ryanair-fined-limit-online-travel-agencies-ticket-sales-ota)

生成摘要时出错

---

## 68. Debian adds LoongArch as officially supported architecture

**原文标题**: Debian adds LoongArch as officially supported architecture

**原文链接**: [https://lists.debian.org/debian-devel-announce/2025/12/msg00004.html](https://lists.debian.org/debian-devel-announce/2025/12/msg00004.html)

生成摘要时出错

---

## 69. Dancing around the rhythm space with Euclid

**原文标题**: Dancing around the rhythm space with Euclid

**原文链接**: [https://pv.wtf/posts/euclidean-rhythms](https://pv.wtf/posts/euclidean-rhythms)

生成摘要时出错

---

## 70. iOS 26.3 brings AirPods-like pairing to third-party devices in EU under DMA

**原文标题**: iOS 26.3 brings AirPods-like pairing to third-party devices in EU under DMA

**原文链接**: [https://www.macrumors.com/2025/12/22/ios-26-3-dma-airpods-pairing/](https://www.macrumors.com/2025/12/22/ios-26-3-dma-airpods-pairing/)

生成摘要时出错

---

## 71. Local AI is driving the biggest change in laptops in decades

**原文标题**: Local AI is driving the biggest change in laptops in decades

**原文链接**: [https://spectrum.ieee.org/ai-models-locally](https://spectrum.ieee.org/ai-models-locally)

生成摘要时出错

---

## 72. Uplane (YC F25) Is Hiring Founding Engineers (Full-Stack and AI)

**原文标题**: Uplane (YC F25) Is Hiring Founding Engineers (Full-Stack and AI)

**原文链接**: [https://www.useparallel.com/uplane1/careers](https://www.useparallel.com/uplane1/careers)

生成摘要时出错

---

## 73. Time-Traveling to 1979: Advice for Designing 'C with Classes

**原文标题**: Time-Traveling to 1979: Advice for Designing 'C with Classes

**原文链接**: [https://coderschmoder.com/i-time-traveled-1979-met-bjarne-stroustrup](https://coderschmoder.com/i-time-traveled-1979-met-bjarne-stroustrup)

生成摘要时出错

---

## 74. The Ultimate Windows Utility (2022)

**原文标题**: The Ultimate Windows Utility (2022)

**原文链接**: [https://christitus.com/windows-tool/](https://christitus.com/windows-tool/)

生成摘要时出错

---

## 75. The Polyglot NixOS

**原文标题**: The Polyglot NixOS

**原文链接**: [https://x86.lol/generic/2025/12/19/polyglot.html](https://x86.lol/generic/2025/12/19/polyglot.html)

生成摘要时出错

---

## 76. Show HN: CodinIT, local open-source Lovable alternative (Electron desktop app)

**原文标题**: Show HN: CodinIT, local open-source Lovable alternative (Electron desktop app)

**原文链接**: [https://github.com/codinit-dev/codinit-dev](https://github.com/codinit-dev/codinit-dev)

生成摘要时出错

---

## 77. Former EU commissioner and activists barred from US

**原文标题**: Former EU commissioner and activists barred from US

**原文链接**: [https://www.theguardian.com/technology/2025/dec/24/us-state-department-visa-ban-former-eu-commissioner-europe](https://www.theguardian.com/technology/2025/dec/24/us-state-department-visa-ban-former-eu-commissioner-europe)

生成摘要时出错

---

## 78. Partial inlining

**原文标题**: Partial inlining

**原文链接**: [https://xania.org/202512/18-partial-inlining](https://xania.org/202512/18-partial-inlining)

生成摘要时出错

---

## 79. Amnezia – Self-Hosted VPN

**原文标题**: Amnezia – Self-Hosted VPN

**原文链接**: [https://amnezia.org/self-hosted](https://amnezia.org/self-hosted)

生成摘要时出错

---

## 80. Charts in Slides

**原文标题**: Charts in Slides

**原文链接**: [https://ia.net/topics/charts-in-slides](https://ia.net/topics/charts-in-slides)

生成摘要时出错

---

## 81. It's Always TCP_NODELAY

**原文标题**: It's Always TCP_NODELAY

**原文链接**: [https://brooker.co.za/blog/2024/05/09/nagle.html](https://brooker.co.za/blog/2024/05/09/nagle.html)

生成摘要时出错

---

## 82. The Illustrated Transformer

**原文标题**: The Illustrated Transformer

**原文链接**: [https://jalammar.github.io/illustrated-transformer/](https://jalammar.github.io/illustrated-transformer/)

生成摘要时出错

---

## 83. Snitch – A friendlier ss/netstat

**原文标题**: Snitch – A friendlier ss/netstat

**原文链接**: [https://github.com/karol-broda/snitch](https://github.com/karol-broda/snitch)

生成摘要时出错

---

## 84. The Coffee Warehouse

**原文标题**: The Coffee Warehouse

**原文链接**: [https://www.scopeofwork.net/the-coffee-warehouse/](https://www.scopeofwork.net/the-coffee-warehouse/)

生成摘要时出错

---

## 85. The biggest CRT ever made: Sony's PVM-4300

**原文标题**: The biggest CRT ever made: Sony's PVM-4300

**原文链接**: [https://dfarq.homeip.net/the-biggest-crt-ever-made-sonys-pvm-4300/](https://dfarq.homeip.net/the-biggest-crt-ever-made-sonys-pvm-4300/)

生成摘要时出错

---

## 86. Microspeak: North Star – The Old New Thing (2015)

**原文标题**: Microspeak: North Star – The Old New Thing (2015)

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20151103-00/?p=91861](https://devblogs.microsoft.com/oldnewthing/20151103-00/?p=91861)

生成摘要时出错

---

## 87. LAVD: Meta's New Default Scheduler [pdf]

**原文标题**: LAVD: Meta's New Default Scheduler [pdf]

**原文链接**: [https://lpc.events/event/19/contributions/2099/attachments/1875/4020/lpc-2025-lavd-meta.pdf](https://lpc.events/event/19/contributions/2099/attachments/1875/4020/lpc-2025-lavd-meta.pdf)

生成摘要时出错

---

## 88. Space Math Academy

**原文标题**: Space Math Academy

**原文链接**: [https://space-math.academy](https://space-math.academy)

生成摘要时出错

---

## 89. Quake's Player Speed According to John Romero (2017)

**原文标题**: Quake's Player Speed According to John Romero (2017)

**原文链接**: [https://rome.ro/quakes-player-speed-1](https://rome.ro/quakes-player-speed-1)

生成摘要时出错

---

## 90. Could lockfiles just be SBOMs?

**原文标题**: Could lockfiles just be SBOMs?

**原文链接**: [https://nesbitt.io/2025/12/23/could-lockfiles-just-be-sboms.html](https://nesbitt.io/2025/12/23/could-lockfiles-just-be-sboms.html)

生成摘要时出错

---

## 91. Debian's Git Transition

**原文标题**: Debian's Git Transition

**原文链接**: [https://diziet.dreamwidth.org/20436.html](https://diziet.dreamwidth.org/20436.html)

生成摘要时出错

---

## 92. The post-GeForce era: What if Nvidia abandons PC gaming?

**原文标题**: The post-GeForce era: What if Nvidia abandons PC gaming?

**原文链接**: [https://www.pcworld.com/article/3013044/the-post-geforce-era-what-if-nvidia-abandons-pc-gaming.html](https://www.pcworld.com/article/3013044/the-post-geforce-era-what-if-nvidia-abandons-pc-gaming.html)

生成摘要时出错

---

## 93. The Duodecimal Bulletin, Vol. 55, No. 1, Year 1209 [pdf]

**原文标题**: The Duodecimal Bulletin, Vol. 55, No. 1, Year 1209 [pdf]

**原文链接**: [https://dozenal.org/drupal/sites_bck/default/files/DuodecimalBulletinIssue551.pdf](https://dozenal.org/drupal/sites_bck/default/files/DuodecimalBulletinIssue551.pdf)

生成摘要时出错

---

## 94. US bars approvals of new models of DJI, all other foreign drones

**原文标题**: US bars approvals of new models of DJI, all other foreign drones

**原文链接**: [https://www.reuters.com/business/aerospace-defense/us-adds-dji-other-foreign-drones-national-security-list-2025-12-22/](https://www.reuters.com/business/aerospace-defense/us-adds-dji-other-foreign-drones-national-security-list-2025-12-22/)

生成摘要时出错

---

## 95. Ultrasound Cancer Treatment: Sound Waves Fight Tumors

**原文标题**: Ultrasound Cancer Treatment: Sound Waves Fight Tumors

**原文链接**: [https://spectrum.ieee.org/ultrasound-cancer-treatment](https://spectrum.ieee.org/ultrasound-cancer-treatment)

生成摘要时出错

---

## 96. 10 years bootstrapped: €6.5M revenue with a team of 13

**原文标题**: 10 years bootstrapped: €6.5M revenue with a team of 13

**原文链接**: [https://www.datocms.com/blog/a-look-back-at-2025](https://www.datocms.com/blog/a-look-back-at-2025)

生成摘要时出错

---

## 97. Universal Reasoning Model (53.8% pass 1 ARC1 and 16.0% ARC 2)

**原文标题**: Universal Reasoning Model (53.8% pass 1 ARC1 and 16.0% ARC 2)

**原文链接**: [https://arxiv.org/abs/2512.14693](https://arxiv.org/abs/2512.14693)

生成摘要时出错

---

## 98. The ancient monuments saluting the winter solstice

**原文标题**: The ancient monuments saluting the winter solstice

**原文链接**: [https://www.bbc.com/culture/article/20251219-the-ancient-monuments-saluting-the-winter-solstice](https://www.bbc.com/culture/article/20251219-the-ancient-monuments-saluting-the-winter-solstice)

生成摘要时出错

---

## 99. Waymo halts service during S.F. blackout after causing traffic jams

**原文标题**: Waymo halts service during S.F. blackout after causing traffic jams

**原文链接**: [https://missionlocal.org/2025/12/sf-waymo-halts-service-blackout/](https://missionlocal.org/2025/12/sf-waymo-halts-service-blackout/)

生成摘要时出错

---

## 100. AI Can Write Your Code. It Can't Do Your Job

**原文标题**: AI Can Write Your Code. It Can't Do Your Job

**原文链接**: [https://terriblesoftware.org/2025/12/11/ai-can-write-your-code-it-cant-do-your-job/](https://terriblesoftware.org/2025/12/11/ai-can-write-your-code-it-cant-do-your-job/)

生成摘要时出错

---

