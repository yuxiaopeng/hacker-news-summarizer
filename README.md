# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_2025-04-11.md)

*最后自动更新时间: 2025-04-11 03:35:09*
## 1. H1元素的默认样式正在更改

**原文标题**: Default styles for H1 elements are changing

**原文链接**: [https://developer.mozilla.org/en-US/blog/h1-element-styles/](https://developer.mozilla.org/en-US/blog/h1-element-styles/)

本文讨论了浏览器中 `<h1>` 元素默认样式的即将到来的变化，特别是它们在分节元素（`<section>`、`<article>`、`<nav>` 和 `<aside>`）中嵌套时的渲染方式。 以前，浏览器会根据嵌套级别自动调整 `<h1>` 的字体大小和边距，模仿 `<h2>`、`<h3>` 等。 这种行为源于现在已删除的 HTML 大纲算法。

现在，浏览器正在删除这些 UA 样式，这意味着 `<h1>` 将始终以其默认样式呈现，而与其在分节元素中的位置无关。 此更改正在 Firefox 和 Chrome 中推出，预计 Safari 也会效仿。

本文强调，依赖这些自动标题级别调整现在被认为是糟糕的做法。 Lighthouse 以及浏览器 DevTools 将标记 `<h1>` 元素缺少明确定义的 `font-size` 和 `margin` 的情况。 具体的 Lighthouse 警告是“H1UserAgentFontSizeInSection”。

为了解决这个问题，开发人员应该：

*   **明确定义** 所有 `<h1>` 元素的 `font-size` 和 `margin`。
*   **使用** `<h2>`、`<h3>` 等，来创建清晰的标题层次结构。
*   **更新 CSS reset** 以应对此变化。
*   **使用 Lighthouse 和 DevTools 审核网站**。
*   **参考 MDN** 以获取更新的 HTML 分节标题文档。

通过采取这些步骤，开发人员可以确保他们的网站按预期呈现，并避免与 `<h1>` 样式相关的 Lighthouse 警告。

---

## 2. “100个Go语言常见错误”背后的故事

**原文标题**: The Story Behind “100 Go Mistakes and How to Avoid Them”

**原文链接**: [https://www.thecoder.cafe/p/100-go-mistakes](https://www.thecoder.cafe/p/100-go-mistakes)

泰瓦·哈萨尼的文章详细介绍了撰写《100个Go语言常见错误与避免方法》的历程。最初，他为了平衡之前工作中的Scala而开始接触Go语言。换了工作后，每天使用Go语言，他注意到同事们重复着他早期的错误。这促使他写了一篇广受欢迎的博客文章《我在Go项目中见过的十大最常见错误》，并由此萌生了写书的想法。

经过16个月从各种来源收集了100个错误后，他向Manning出版社提交了图书提案。该提案需要回答21个问题，并接受Go语言专家的评审。积极的评价促成了合同的签订，版税为10%，并预付了稿费。

写作过程包括定义最低合格读者(MQR)，并与一位开发编辑(DE)密切合作，后者极大地改进了他为图书格式而进行的写作风格。他讨论了他创造“最好的Go语言书籍”的心态。这本书经历了多个评审周期，外部审阅者提供了详尽的反馈以提高书籍质量。哈萨尼提到了Manning出版社的一个小插曲，他的技术开发编辑(TDE)缺乏MQR所期望的Go语言基础知识。尽管如此，他还是采纳了比尔·肯尼迪的反馈意见并坚持了下来。

---

## 3. 没有加菲猫的加菲猫

**原文标题**: Garfield Minus Garfield

**原文链接**: [https://garfieldminusgarfield.net](https://garfieldminusgarfield.net)

提供的文本描述了一个名为“没有加菲猫的加菲猫”(G-G)的东西。 它还提到这个“G-G”在Facebook和Twitter上都有，并附有具体的日期（1月27日和11月3日）。

本质上，这是一个名为“没有加菲猫的加菲猫”的项目/实体的广告或引用，该项目/实体在Facebook和Twitter等社交媒体平台上存在并可能正在推广。 这些日期可能表明该项目在这些平台上活跃或推广的时间。

如果没有更多的背景信息，很难确定“没有加菲猫的加菲猫”本身的具体性质。 然而，这段文字强烈暗示它是一个在线分享和讨论的项目或概念。

---

## 4. R 语言大全

**原文标题**: Big Book of R

**原文链接**: [https://www.bigbookofr.com/](https://www.bigbookofr.com/)

R语言巨著：汇集400余本R语言免费书籍，无需书签，搜索方便，欢迎贡献。本站感谢Fathom Data转换为Quarto，采用CC BY-NC-ND 3.0协议。数据透明，统计每日独立访客。欢迎捐赠，关注作者Mastodon、LinkedIn，订阅时讯。

---

## 5. 我自己的私有二进制：Linux内核模块的个性化介绍

**原文标题**: My Own Private Binary: An Idiosyncratic Introduction to Linux Kernel Modules

**原文链接**: [https://www.muppetlabs.com/~breadbox/txt/mopb.html](https://www.muppetlabs.com/~breadbox/txt/mopb.html)

本文以一种独特的方式介绍了Linux内核模块，其动机源于作者寻求创建尽可能小的可执行文件。文章首先回顾了作者之前缩小ELF可执行文件的尝试，并遇到了已弃用的aout格式。这引发了对Linux如何动态处理二进制格式的调查。

作者发现Linux使用可加载内核模块来管理二进制格式支持，允许添加和删除格式而无需重新编译内核。然后，文章转而解释如何创建一个基本的“hello kernel”模块，涵盖必要的头文件、模块元数据、init和exit函数以及Makefile。它演示了如何使用`insmod`和`rmmod`加载和卸载模块，并使用`dmesg`验证其操作。

文章承认编写有用的内核模块需要专门的知识，但鼓励实验。它强调了内核模块的强大功能和潜在危险，强调了它们在低级别访问和操作系统的能力。

最后，文章将内核模块与最初的动机联系起来，解释说内核中接受的二进制文件格式列表是动态的。这是通过已注册的回调函数列表进行管理的，当执行二进制文件时，内核会调用这些回调函数。第一个识别文件的回调函数会处理将其加载到内存中，否则会显示“Exec format error”。作者暗示了创建支持.com文件格式的内核模块的意图，从而能够创建更小的可执行文件。

---

## 6. 金融科技创始人被控欺诈；人工智能应用被发现实为菲律宾人工操作

**原文标题**: Fintech founder charged with fraud; AI app found to be humans in the Philippines

**原文链接**: [https://techcrunch.com/2025/04/10/fintech-founder-charged-with-fraud-after-ai-shopping-app-found-to-be-powered-by-humans-in-the-philippines/](https://techcrunch.com/2025/04/10/fintech-founder-charged-with-fraud-after-ai-shopping-app-found-to-be-powered-by-humans-in-the-philippines/)

前AI购物应用Nate创始人兼前CEO阿尔伯特·萨尼格(Albert Saniger)被美国司法部指控欺诈，原因是他误导投资者。Nate筹集了超过5000万美元，声称其“AI”允许用户一键从任何电商网站购物。然而，司法部指控Nate严重依赖菲律宾的人工承包商手动完成购买，尽管萨尼格声称几乎没有人为干预。

司法部声称Nate的实际自动化率实际上为0%。这与基于Nate人工智能能力而筹集的数百万美元风险投资相矛盾。《The Information》在2022年进行的一项调查此前曾强调Nate对人工承包商的依赖。

该公司最终耗尽资金，于2023年1月出售了其资产，导致投资者遭受重大损失。萨尼格现在是风险投资公司Buttercore Partners的执行合伙人。

这篇文章还强调了一种初创企业夸大其人工智能能力的趋势，并列举了一些例子，例如一个“AI”汽车穿梭点餐软件和法律科技独角兽EvenUp，都发现它们严重依赖人工。这种趋势表明，公司面临着比实际情况更具有技术先进性的压力。

---

## 7. Show HN: 我做了一个管理和比较信用卡奖励的工具

**原文标题**: Show HN: I built a tool to manage and compare credit card rewards

**原文链接**: [https://rewards.getonecard.io](https://rewards.getonecard.io)

此“Show HN”帖子介绍了一款旨在帮助用户管理和最大化信用卡奖励的工具。该工具允许用户将现有信用卡添加到虚拟“钱包”中，然后利用人工智能识别在任何指定商家处使用哪张卡片最佳。此推荐基于优化奖励积分积累。

着陆页包含一个“奖励优化器”，它会根据商家类型推荐最佳卡片。提供的示例包括：使用美国运通金卡在餐厅（如“Home Slice Pizza”和“Powder Room”）消费可赚取 4 倍积分，以及使用大通蓝宝石卡在酒店（如“Fairmont Austin”）消费可赚取 3 倍积分。

该工具被宣传为能够提供即时推荐，突出了速度和易用性。 其关键功能围绕着为特定商家识别最具奖励性的卡片，并帮助用户避免错过奖励。 核心优势是最大化奖励积分和简化信用卡使用方面的决策。

---

## 8. 解密Shebang：内核探险

**原文标题**: Demystifying the (Shebang): Kernel Adventures

**原文链接**: [https://crocidb.com/post/kernel-adventures/demystifying-the-shebang/](https://crocidb.com/post/kernel-adventures/demystifying-the-shebang/)

本文深入探讨了Linux系统中 Shebang (`#!`) 机制的内部运作原理，揭示了内核而非 Shell 负责处理其解释。作者首先阐述了 Shebang 如何指定脚本执行的解释器，并通过 Shell 和 Python 脚本示例说明了这一点，并阐明了它在识别 Linux 实用程序（如 `useradd` 和 `adduser`）底层实现方面的作用。

作者使用 `strace` 跟踪执行流程，并展示了 `execve` 系统调用是入口点，最终导向内核中的 `do_execveat_common` 函数。该函数初始化一个 `linux_binprm` 结构，读取文件内容，并利用 `search_binary_handler` 来识别文件的可执行格式。文章探讨了 `binfmt_elf.c`、`binfmt_script.c` 和 `binfmt_misc.c` 等模块。

`binfmt_script.c` 模块负责处理 Shebang，验证 `#!` 签名，然后定位并调用指定的解释器。内核更新 `bprm->file` 以指向解释器，并有效地替换进程映像。

文章还阐明，虽然 Shebang 是指定解释器的主要方式，但 Shell 通常提供回退机制，如果由于缺少或错误的 Shebang 导致 `execve` 调用失败，则会尝试直接执行脚本。这涉及到 Shell 读取脚本、检测其类型，并显式调用适当的解释器。

最后，作者简要地提到了权限检查，表明内核在调用脚本之前会验证执行权限，如果缺少执行权限，则会触发 `EACCES (Permission denied)` 错误。

---

## 9. 用声音悬浮昆虫或将变革科学摄影

**原文标题**: Levitating Bugs with Sound Could Transform Scientific Photography

**原文链接**: [https://petapixel.com/2025/03/25/levitating-bugs-with-sound-could-transform-scientific-photography/](https://petapixel.com/2025/03/25/levitating-bugs-with-sound-could-transform-scientific-photography/)

科学家开发出一种新型摄影测量成像系统，利用声悬浮技术在不损伤昆虫标本的情况下捕捉其详细照片。这种创新方法使用精确控制的声波悬浮昆虫，允许多角度图像采集，无需传统的针插固定方法，从而避免损害脆弱的标本。

来自多家德国机构的研究人员创建了一个系统，该系统包括由FPGA控制的声悬浮装置和一个三脚架上的微距相机。这使得他们能够自动操纵标本，以在预定义角度拍摄特定图像，从而实现焦点堆叠以获得扩展的景深并创建高度详细的3D模型。该团队使用了带有 90 毫米微距镜头和增距镜的 Olympus OM-D E-M1 III 相机。

这种方法对于生物多样性研究特别有价值，昆虫在其中发挥着关键作用，但由于识别挑战而难以研究。通过提供经济高效、易于获取且可重复的成像系统，研究人员可以收集训练昆虫识别人工智能模型所需的详细数据。

该系统在每个标本位置捕获 40 张照片，并从 72 个不同的角度重复该过程。研究团队承认存在单轴旋转等局限性，但强调了这种非破坏性方法在小型、轻型物体的多角度成像和 3D 重建方面的巨大潜力。该方法还有助于 DNA 测序，因为标本不会受到损坏或干燥。

---

## 10. 为什么要敲击奶酪轮？

**原文标题**: Why Tap a Wheel of Cheese?

**原文链接**: [https://www.cheeseprofessor.com/blog/cheese-wheel-tapping](https://www.cheeseprofessor.com/blog/cheese-wheel-tapping)

帕尔马干酪的质量由一小队“敲击师”（drummers）保证，他们在奶酪经过至少12个月的陈酿期后，用锤子敲击每一块奶酪。这些专家，如亚历山德罗·斯托基和他的导师雷纳托·朱迪奇，仅凭声音就能在几秒钟内检测到内部缺陷。这项技能传统上通过学徒制代代相传，依靠第一手经验。

敲击过程包括聆听奶酪表面均匀的声音。一块完美的奶酪具有紧实的质地，没有空洞或裂缝。声音的变化表明内部存在缺陷，敲击师可以检测到这些缺陷，从而形成奶酪的心理“X光片”。

帕尔马干酪分为三个质量等级：顶级（带有火印）、轻微缺陷（标有平行线）和重大缺陷（作为普通奶酪出售）。虽然缺陷可能被认为是负面的，但它们被认为是奶酪制作工艺的手工性质的标志，该工艺使用未经防腐剂处理的生牛奶，并且会受到自然变化的影响。尽管存在缺陷，但存在缺陷的奶酪数量仍然很少。敲击师强调激情、尊重、谦逊和持续学习在他们职业中的重要性。

---

## 历史记录

| 序号 | 文件 |
| --- | --- |
| 1 | [2025-04-11](output/hacker_news_summary_2025-04-11.md) |
| 2 | [2025-04-09](output/hacker_news_summary_2025-04-09.md) |
| 3 | [2025-04-07](output/hacker_news_summary_2025-04-07.md) |
| 4 | [2025-04-08](output/hacker_news_summary_2025-04-08.md) |
| 5 | [2025-04-05](output/hacker_news_summary_2025-04-05.md) |
| 6 | [2025-04-04](output/hacker_news_summary_2025-04-04.md) |
| 7 | [2025-04-06](output/hacker_news_summary_2025-04-06.md) |
| 8 | [2025-03-31](output/hacker_news_summary_2025-03-31.md) |
| 9 | [2025-03-30](output/hacker_news_summary_2025-03-30.md) |
| 10 | [2025-04-01](output/hacker_news_summary_2025-04-01.md) |
| 11 | [2025-04-02](output/hacker_news_summary_2025-04-02.md) |
| 12 | [2025-04-03](output/hacker_news_summary_2025-04-03.md) |
| 13 | [2025-03-24](output/hacker_news_summary_2025-03-24.md) |
| 14 | [2025-03-26](output/hacker_news_summary_2025-03-26.md) |
| 15 | [2025-03-29](output/hacker_news_summary_2025-03-29.md) |
| 16 | [2025-03-28](output/hacker_news_summary_2025-03-28.md) |
| 17 | [2025-03-25](output/hacker_news_summary_2025-03-25.md) |
| 18 | [2025-03-23](output/hacker_news_summary_2025-03-23.md) |
| 19 | [2025-03-22](output/hacker_news_summary_2025-03-22.md) |
| 20 | [2025-03-27](output/hacker_news_summary_2025-03-27.md) |
| 21 | [2025-03-21](output/hacker_news_summary_2025-03-21.md) |
| 22 | [2025-03-20](output/hacker_news_summary_2025-03-20.md) |
| 23 | [2025-03-19](output/hacker_news_summary_2025-03-19.md) |
