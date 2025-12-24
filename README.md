# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-12-24.md)

*最后自动更新时间: 2025-12-24 17:46:21*
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

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-12-24](output/hacker_news_summary_2025-12-24.md) |
| 2 | [2025-12-23](output/hacker_news_summary_2025-12-23.md) |
| 3 | [2025-12-19](output/hacker_news_summary_2025-12-19.md) |
| 4 | [2025-12-21](output/hacker_news_summary_2025-12-21.md) |
| 5 | [2025-12-22](output/hacker_news_summary_2025-12-22.md) |
| 6 | [2025-12-20](output/hacker_news_summary_2025-12-20.md) |
| 7 | [2025-12-16](output/hacker_news_summary_2025-12-16.md) |
| 8 | [2025-12-15](output/hacker_news_summary_2025-12-15.md) |
| 9 | [2025-12-13](output/hacker_news_summary_2025-12-13.md) |
| 10 | [2025-12-18](output/hacker_news_summary_2025-12-18.md) |
| 11 | [2025-12-17](output/hacker_news_summary_2025-12-17.md) |
| 12 | [2025-12-12](output/hacker_news_summary_2025-12-12.md) |
| 13 | [2025-12-14](output/hacker_news_summary_2025-12-14.md) |
| 14 | [2025-12-07](output/hacker_news_summary_2025-12-07.md) |
| 15 | [2025-12-06](output/hacker_news_summary_2025-12-06.md) |
| 16 | [2025-12-08](output/hacker_news_summary_2025-12-08.md) |
| 17 | [2025-12-11](output/hacker_news_summary_2025-12-11.md) |
| 18 | [2025-12-09](output/hacker_news_summary_2025-12-09.md) |
| 19 | [2025-12-10](output/hacker_news_summary_2025-12-10.md) |
| 20 | [2025-12-04](output/hacker_news_summary_2025-12-04.md) |
| 21 | [2025-12-05](output/hacker_news_summary_2025-12-05.md) |
| 22 | [2025-12-02](output/hacker_news_summary_2025-12-02.md) |
| 23 | [2025-12-03](output/hacker_news_summary_2025-12-03.md) |
| 24 | [2025-11-29](output/hacker_news_summary_2025-11-29.md) |
| 25 | [2025-11-30](output/hacker_news_summary_2025-11-30.md) |
| 26 | [2025-12-01](output/hacker_news_summary_2025-12-01.md) |
| 27 | [2025-11-28](output/hacker_news_summary_2025-11-28.md) |
| 28 | [2025-11-27](output/hacker_news_summary_2025-11-27.md) |
| 29 | [2025-11-25](output/hacker_news_summary_2025-11-25.md) |
| 30 | [2025-11-26](output/hacker_news_summary_2025-11-26.md) |
| 31 | [2025-11-23](output/hacker_news_summary_2025-11-23.md) |
| 32 | [2025-11-24](output/hacker_news_summary_2025-11-24.md) |
| 33 | [2025-11-21](output/hacker_news_summary_2025-11-21.md) |
| 34 | [2025-11-22](output/hacker_news_summary_2025-11-22.md) |
| 35 | [2025-11-19](output/hacker_news_summary_2025-11-19.md) |
| 36 | [2025-11-20](output/hacker_news_summary_2025-11-20.md) |
| 37 | [2025-11-18](output/hacker_news_summary_2025-11-18.md) |
| 38 | [2025-11-17](output/hacker_news_summary_2025-11-17.md) |
| 39 | [2025-11-16](output/hacker_news_summary_2025-11-16.md) |
| 40 | [2025-11-15](output/hacker_news_summary_2025-11-15.md) |
| 41 | [2025-11-14](output/hacker_news_summary_2025-11-14.md) |
| 42 | [2025-11-12](output/hacker_news_summary_2025-11-12.md) |
| 43 | [2025-11-13](output/hacker_news_summary_2025-11-13.md) |
| 44 | [2025-11-11](output/hacker_news_summary_2025-11-11.md) |
| 45 | [2025-11-10](output/hacker_news_summary_2025-11-10.md) |
| 46 | [2025-11-08](output/hacker_news_summary_2025-11-08.md) |
| 47 | [2025-11-09](output/hacker_news_summary_2025-11-09.md) |
| 48 | [2025-11-06](output/hacker_news_summary_2025-11-06.md) |
| 49 | [2025-11-07](output/hacker_news_summary_2025-11-07.md) |
| 50 | [2025-11-05](output/hacker_news_summary_2025-11-05.md) |
| 51 | [2025-11-04](output/hacker_news_summary_2025-11-04.md) |
| 52 | [2025-11-03](output/hacker_news_summary_2025-11-03.md) |
| 53 | [2025-11-01](output/hacker_news_summary_2025-11-01.md) |
| 54 | [2025-11-02](output/hacker_news_summary_2025-11-02.md) |
| 55 | [2025-10-31](output/hacker_news_summary_2025-10-31.md) |
| 56 | [2025-10-30](output/hacker_news_summary_2025-10-30.md) |
| 57 | [2025-10-29](output/hacker_news_summary_2025-10-29.md) |
| 58 | [2025-10-26](output/hacker_news_summary_2025-10-26.md) |
| 59 | [2025-10-27](output/hacker_news_summary_2025-10-27.md) |
| 60 | [2025-10-24](output/hacker_news_summary_2025-10-24.md) |
| 61 | [2025-10-25](output/hacker_news_summary_2025-10-25.md) |
| 62 | [2025-10-22](output/hacker_news_summary_2025-10-22.md) |
| 63 | [2025-10-23](output/hacker_news_summary_2025-10-23.md) |
| 64 | [2025-10-21](output/hacker_news_summary_2025-10-21.md) |
| 65 | [2025-10-20](output/hacker_news_summary_2025-10-20.md) |
| 66 | [2025-10-19](output/hacker_news_summary_2025-10-19.md) |
| 67 | [2025-10-18](output/hacker_news_summary_2025-10-18.md) |
| 68 | [2025-10-16](output/hacker_news_summary_2025-10-16.md) |
| 69 | [2025-10-17](output/hacker_news_summary_2025-10-17.md) |
| 70 | [2025-10-14](output/hacker_news_summary_2025-10-14.md) |
| 71 | [2025-10-15](output/hacker_news_summary_2025-10-15.md) |
| 72 | [2025-10-12](output/hacker_news_summary_2025-10-12.md) |
| 73 | [2025-10-11](output/hacker_news_summary_2025-10-11.md) |
| 74 | [2025-10-13](output/hacker_news_summary_2025-10-13.md) |
| 75 | [2025-10-09](output/hacker_news_summary_2025-10-09.md) |
| 76 | [2025-10-10](output/hacker_news_summary_2025-10-10.md) |
| 77 | [2025-10-07](output/hacker_news_summary_2025-10-07.md) |
| 78 | [2025-10-08](output/hacker_news_summary_2025-10-08.md) |
| 79 | [2025-10-06](output/hacker_news_summary_2025-10-06.md) |
| 80 | [2025-10-05](output/hacker_news_summary_2025-10-05.md) |
| 81 | [2025-10-04](output/hacker_news_summary_2025-10-04.md) |
| 82 | [2025-10-03](output/hacker_news_summary_2025-10-03.md) |
| 83 | [2025-10-02](output/hacker_news_summary_2025-10-02.md) |
| 84 | [2025-10-01](output/hacker_news_summary_2025-10-01.md) |
| 85 | [2025-09-30](output/hacker_news_summary_2025-09-30.md) |
| 86 | [2025-09-29](output/hacker_news_summary_2025-09-29.md) |
| 87 | [2025-09-28](output/hacker_news_summary_2025-09-28.md) |
| 88 | [2025-09-27](output/hacker_news_summary_2025-09-27.md) |
| 89 | [2025-09-26](output/hacker_news_summary_2025-09-26.md) |
| 90 | [2025-09-25](output/hacker_news_summary_2025-09-25.md) |
| 91 | [2025-09-24](output/hacker_news_summary_2025-09-24.md) |
| 92 | [2025-09-23](output/hacker_news_summary_2025-09-23.md) |
| 93 | [2025-09-21](output/hacker_news_summary_2025-09-21.md) |
| 94 | [2025-09-22](output/hacker_news_summary_2025-09-22.md) |
| 95 | [2025-09-19](output/hacker_news_summary_2025-09-19.md) |
| 96 | [2025-09-20](output/hacker_news_summary_2025-09-20.md) |
| 97 | [2025-09-18](output/hacker_news_summary_2025-09-18.md) |
| 98 | [2025-09-17](output/hacker_news_summary_2025-09-17.md) |
| 99 | [2025-09-16](output/hacker_news_summary_2025-09-16.md) |
| 100 | [2025-09-15](output/hacker_news_summary_2025-09-15.md) |
| 101 | [2025-09-14](output/hacker_news_summary_2025-09-14.md) |
| 102 | [2025-09-12](output/hacker_news_summary_2025-09-12.md) |
| 103 | [2025-09-13](output/hacker_news_summary_2025-09-13.md) |
| 104 | [2025-09-11](output/hacker_news_summary_2025-09-11.md) |
| 105 | [2025-09-10](output/hacker_news_summary_2025-09-10.md) |
| 106 | [2025-09-08](output/hacker_news_summary_2025-09-08.md) |
| 107 | [2025-09-09](output/hacker_news_summary_2025-09-09.md) |
| 108 | [2025-09-07](output/hacker_news_summary_2025-09-07.md) |
| 109 | [2025-09-06](output/hacker_news_summary_2025-09-06.md) |
| 110 | [2025-09-04](output/hacker_news_summary_2025-09-04.md) |
| 111 | [2025-09-05](output/hacker_news_summary_2025-09-05.md) |
| 112 | [2025-09-03](output/hacker_news_summary_2025-09-03.md) |
| 113 | [2025-09-02](output/hacker_news_summary_2025-09-02.md) |
| 114 | [2025-09-01](output/hacker_news_summary_2025-09-01.md) |
| 115 | [2025-08-31](output/hacker_news_summary_2025-08-31.md) |
| 116 | [2025-08-30](output/hacker_news_summary_2025-08-30.md) |
| 117 | [2025-08-29](output/hacker_news_summary_2025-08-29.md) |
| 118 | [2025-08-28](output/hacker_news_summary_2025-08-28.md) |
| 119 | [2025-08-26](output/hacker_news_summary_2025-08-26.md) |
| 120 | [2025-08-27](output/hacker_news_summary_2025-08-27.md) |
| 121 | [2025-08-25](output/hacker_news_summary_2025-08-25.md) |
| 122 | [2025-08-24](output/hacker_news_summary_2025-08-24.md) |
| 123 | [2025-08-22](output/hacker_news_summary_2025-08-22.md) |
| 124 | [2025-08-23](output/hacker_news_summary_2025-08-23.md) |
| 125 | [2025-08-20](output/hacker_news_summary_2025-08-20.md) |
| 126 | [2025-08-21](output/hacker_news_summary_2025-08-21.md) |
| 127 | [2025-08-19](output/hacker_news_summary_2025-08-19.md) |
| 128 | [2025-08-18](output/hacker_news_summary_2025-08-18.md) |
| 129 | [2025-08-17](output/hacker_news_summary_2025-08-17.md) |
| 130 | [2025-08-16](output/hacker_news_summary_2025-08-16.md) |
| 131 | [2025-08-15](output/hacker_news_summary_2025-08-15.md) |
| 132 | [2025-08-14](output/hacker_news_summary_2025-08-14.md) |
| 133 | [2025-08-12](output/hacker_news_summary_2025-08-12.md) |
| 134 | [2025-08-13](output/hacker_news_summary_2025-08-13.md) |
| 135 | [2025-08-11](output/hacker_news_summary_2025-08-11.md) |
| 136 | [2025-08-10](output/hacker_news_summary_2025-08-10.md) |
| 137 | [2025-08-09](output/hacker_news_summary_2025-08-09.md) |
| 138 | [2025-08-08](output/hacker_news_summary_2025-08-08.md) |
| 139 | [2025-08-07](output/hacker_news_summary_2025-08-07.md) |
| 140 | [2025-08-05](output/hacker_news_summary_2025-08-05.md) |
| 141 | [2025-08-06](output/hacker_news_summary_2025-08-06.md) |
| 142 | [2025-08-04](output/hacker_news_summary_2025-08-04.md) |
| 143 | [2025-08-03](output/hacker_news_summary_2025-08-03.md) |
| 144 | [2025-08-02](output/hacker_news_summary_2025-08-02.md) |
| 145 | [2025-08-01](output/hacker_news_summary_2025-08-01.md) |
| 146 | [2025-07-31](output/hacker_news_summary_2025-07-31.md) |
| 147 | [2025-07-30](output/hacker_news_summary_2025-07-30.md) |
| 148 | [2025-07-28](output/hacker_news_summary_2025-07-28.md) |
| 149 | [2025-07-29](output/hacker_news_summary_2025-07-29.md) |
| 150 | [2025-07-26](output/hacker_news_summary_2025-07-26.md) |
| 151 | [2025-07-27](output/hacker_news_summary_2025-07-27.md) |
| 152 | [2025-07-25](output/hacker_news_summary_2025-07-25.md) |
| 153 | [2025-07-24](output/hacker_news_summary_2025-07-24.md) |
| 154 | [2025-07-22](output/hacker_news_summary_2025-07-22.md) |
| 155 | [2025-07-23](output/hacker_news_summary_2025-07-23.md) |
| 156 | [2025-07-20](output/hacker_news_summary_2025-07-20.md) |
| 157 | [2025-07-19](output/hacker_news_summary_2025-07-19.md) |
| 158 | [2025-07-21](output/hacker_news_summary_2025-07-21.md) |
| 159 | [2025-07-17](output/hacker_news_summary_2025-07-17.md) |
| 160 | [2025-07-18](output/hacker_news_summary_2025-07-18.md) |
| 161 | [2025-07-15](output/hacker_news_summary_2025-07-15.md) |
| 162 | [2025-07-16](output/hacker_news_summary_2025-07-16.md) |
| 163 | [2025-07-13](output/hacker_news_summary_2025-07-13.md) |
| 164 | [2025-07-14](output/hacker_news_summary_2025-07-14.md) |
| 165 | [2025-07-12](output/hacker_news_summary_2025-07-12.md) |
| 166 | [2025-07-11](output/hacker_news_summary_2025-07-11.md) |
| 167 | [2025-07-09](output/hacker_news_summary_2025-07-09.md) |
| 168 | [2025-07-10](output/hacker_news_summary_2025-07-10.md) |
| 169 | [2025-07-07](output/hacker_news_summary_2025-07-07.md) |
| 170 | [2025-07-06](output/hacker_news_summary_2025-07-06.md) |
| 171 | [2025-07-08](output/hacker_news_summary_2025-07-08.md) |
| 172 | [2025-07-05](output/hacker_news_summary_2025-07-05.md) |
| 173 | [2025-07-04](output/hacker_news_summary_2025-07-04.md) |
| 174 | [2025-07-02](output/hacker_news_summary_2025-07-02.md) |
| 175 | [2025-07-03](output/hacker_news_summary_2025-07-03.md) |
| 176 | [2025-06-30](output/hacker_news_summary_2025-06-30.md) |
| 177 | [2025-07-01](output/hacker_news_summary_2025-07-01.md) |
| 178 | [2025-06-29](output/hacker_news_summary_2025-06-29.md) |
| 179 | [2025-06-28](output/hacker_news_summary_2025-06-28.md) |
| 180 | [2025-06-26](output/hacker_news_summary_2025-06-26.md) |
| 181 | [2025-06-27](output/hacker_news_summary_2025-06-27.md) |
| 182 | [2025-06-25](output/hacker_news_summary_2025-06-25.md) |
| 183 | [2025-06-24](output/hacker_news_summary_2025-06-24.md) |
| 184 | [2025-06-22](output/hacker_news_summary_2025-06-22.md) |
| 185 | [2025-06-23](output/hacker_news_summary_2025-06-23.md) |
| 186 | [2025-06-21](output/hacker_news_summary_2025-06-21.md) |
| 187 | [2025-06-20](output/hacker_news_summary_2025-06-20.md) |
| 188 | [2025-06-19](output/hacker_news_summary_2025-06-19.md) |
| 189 | [2025-06-17](output/hacker_news_summary_2025-06-17.md) |
| 190 | [2025-06-18](output/hacker_news_summary_2025-06-18.md) |
| 191 | [2025-06-16](output/hacker_news_summary_2025-06-16.md) |
| 192 | [2025-06-15](output/hacker_news_summary_2025-06-15.md) |
| 193 | [2025-06-14](output/hacker_news_summary_2025-06-14.md) |
| 194 | [2025-06-13](output/hacker_news_summary_2025-06-13.md) |
| 195 | [2025-06-12](output/hacker_news_summary_2025-06-12.md) |
| 196 | [2025-06-11](output/hacker_news_summary_2025-06-11.md) |
| 197 | [2025-06-10](output/hacker_news_summary_2025-06-10.md) |
| 198 | [2025-06-09](output/hacker_news_summary_2025-06-09.md) |
| 199 | [2025-06-08](output/hacker_news_summary_2025-06-08.md) |
| 200 | [2025-06-07](output/hacker_news_summary_2025-06-07.md) |
| 201 | [2025-06-05](output/hacker_news_summary_2025-06-05.md) |
| 202 | [2025-06-06](output/hacker_news_summary_2025-06-06.md) |
| 203 | [2025-06-04](output/hacker_news_summary_2025-06-04.md) |
| 204 | [2025-06-02](output/hacker_news_summary_2025-06-02.md) |
| 205 | [2025-06-03](output/hacker_news_summary_2025-06-03.md) |
| 206 | [2025-05-31](output/hacker_news_summary_2025-05-31.md) |
| 207 | [2025-06-01](output/hacker_news_summary_2025-06-01.md) |
| 208 | [2025-05-30](output/hacker_news_summary_2025-05-30.md) |
| 209 | [2025-05-28](output/hacker_news_summary_2025-05-28.md) |
| 210 | [2025-05-29](output/hacker_news_summary_2025-05-29.md) |
| 211 | [2025-05-26](output/hacker_news_summary_2025-05-26.md) |
| 212 | [2025-05-27](output/hacker_news_summary_2025-05-27.md) |
| 213 | [2025-05-25](output/hacker_news_summary_2025-05-25.md) |
| 214 | [2025-05-23](output/hacker_news_summary_2025-05-23.md) |
| 215 | [2025-05-24](output/hacker_news_summary_2025-05-24.md) |
| 216 | [2025-05-22](output/hacker_news_summary_2025-05-22.md) |
| 217 | [2025-05-20](output/hacker_news_summary_2025-05-20.md) |
| 218 | [2025-05-21](output/hacker_news_summary_2025-05-21.md) |
| 219 | [2025-05-19](output/hacker_news_summary_2025-05-19.md) |
| 220 | [2025-05-18](output/hacker_news_summary_2025-05-18.md) |
| 221 | [2025-05-17](output/hacker_news_summary_2025-05-17.md) |
| 222 | [2025-05-15](output/hacker_news_summary_2025-05-15.md) |
| 223 | [2025-05-16](output/hacker_news_summary_2025-05-16.md) |
| 224 | [2025-05-14](output/hacker_news_summary_2025-05-14.md) |
| 225 | [2025-05-12](output/hacker_news_summary_2025-05-12.md) |
| 226 | [2025-05-13](output/hacker_news_summary_2025-05-13.md) |
| 227 | [2025-05-11](output/hacker_news_summary_2025-05-11.md) |
| 228 | [2025-05-09](output/hacker_news_summary_2025-05-09.md) |
| 229 | [2025-05-10](output/hacker_news_summary_2025-05-10.md) |
| 230 | [2025-05-08](output/hacker_news_summary_2025-05-08.md) |
| 231 | [2025-05-06](output/hacker_news_summary_2025-05-06.md) |
| 232 | [2025-05-07](output/hacker_news_summary_2025-05-07.md) |
| 233 | [2025-05-05](output/hacker_news_summary_2025-05-05.md) |
| 234 | [2025-05-04](output/hacker_news_summary_2025-05-04.md) |
| 235 | [2025-05-03](output/hacker_news_summary_2025-05-03.md) |
| 236 | [2025-05-02](output/hacker_news_summary_2025-05-02.md) |
| 237 | [2025-05-01](output/hacker_news_summary_2025-05-01.md) |
| 238 | [2025-04-30](output/hacker_news_summary_2025-04-30.md) |
| 239 | [2025-04-29](output/hacker_news_summary_2025-04-29.md) |
| 240 | [2025-04-28](output/hacker_news_summary_2025-04-28.md) |
| 241 | [2025-04-27](output/hacker_news_summary_2025-04-27.md) |
| 242 | [2025-04-25](output/hacker_news_summary_2025-04-25.md) |
| 243 | [2025-04-26](output/hacker_news_summary_2025-04-26.md) |
| 244 | [2025-04-24](output/hacker_news_summary_2025-04-24.md) |
| 245 | [2025-04-22](output/hacker_news_summary_2025-04-22.md) |
| 246 | [2025-04-23](output/hacker_news_summary_2025-04-23.md) |
| 247 | [2025-04-21](output/hacker_news_summary_2025-04-21.md) |
| 248 | [2025-04-20](output/hacker_news_summary_2025-04-20.md) |
| 249 | [2025-04-19](output/hacker_news_summary_2025-04-19.md) |
| 250 | [2025-04-17](output/hacker_news_summary_2025-04-17.md) |
| 251 | [2025-04-18](output/hacker_news_summary_2025-04-18.md) |
| 252 | [2025-04-16](output/hacker_news_summary_2025-04-16.md) |
| 253 | [2025-04-15](output/hacker_news_summary_2025-04-15.md) |
| 254 | [2025-04-14](output/hacker_news_summary_2025-04-14.md) |
| 255 | [2025-04-13](output/hacker_news_summary_2025-04-13.md) |
| 256 | [2025-04-12](output/hacker_news_summary_2025-04-12.md) |
| 257 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 258 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 259 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 260 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 261 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 262 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 263 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 264 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 265 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 266 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 267 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 268 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 269 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 270 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 271 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 272 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 273 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 274 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 275 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
| 276 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 277 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 278 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 279 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
