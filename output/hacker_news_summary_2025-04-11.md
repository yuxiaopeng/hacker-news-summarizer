# Hacker News 热门文章摘要 (2025-04-11)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

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

## 11. 一部售价2000美元的“美国制造”手机是如何生产的

**原文标题**: How a $2k 'Made in the USA' Phone Is Manufactured

**原文链接**: [https://www.404media.co/how-a-2-000-made-in-the-usa-liberty-phone-phone-is-manufactured/](https://www.404media.co/how-a-2-000-made-in-the-usa-liberty-phone-phone-is-manufactured/)

本文探讨了Purism的Liberty Phone，这款售价2000美元的智能手机由于Purism在美国本土制造的努力，符合“美国制造”的标准。创始人Todd Weaver解释了这项工作背后的挑战和动机，包括安全供应链、透明度以及服务于安全市场。

Purism最初从笔记本电脑起步，然后利用中国的制造经验来设计和生产最初的Librem 5手机。这段经历使他们得以在加利福尼亚州卡尔斯巴德建立了自己的表面贴装技术（SMT）生产线，从而能够将Liberty Phone的电子产品从原材料到成品进行制造。

文章强调了组装和制造之间的区别，强调Purism进行的是完整的电子产品制造，将元件焊接在裸板上。他们从西方分销商和制造商处采购元件，包括那些在美国生产的制造商。虽然他们努力争取美国制造的材料，但在可用性和与供应商的谈判筹码方面仍然存在挑战。

Weaver承认Liberty Phone的规格并非最前沿，并且从美国采购所有组件非常困难。例如，某些晶体只能从中国或韩国获得。模块化设计允许从不同国家采购调制解调器等组件，从而影响成本和蜂窝频段支持。虽然先进的芯片组目前在美国境外制造，但Weaver认为，通过大量的投资和稳定性，有可能在美国制造它们。Purism优先考虑透明度，发布原理图和硬件物料清单。

---

## 12. 拥有我的数据，第一部分：集成自托管日历解决方案

**原文标题**: Owning my own data, part 1: Integrating a self-hosted calendar solution

**原文链接**: [https://emilygorcenski.com/post/owning-my-own-data-part-1-integrating-a-self-hosted-calendar-solution/](https://emilygorcenski.com/post/owning-my-own-data-part-1-integrating-a-self-hosted-calendar-solution/)

Emily Gorcenski 的文章《拥有我自己的数据，第一部分：集成自托管日历解决方案》详细介绍了作者通过自托管日历解决方案来重新获得个人数据控制权的过程。她厌倦了依赖像 Google 这样的大公司来存储和访问她的日历信息，因此决定实施一个能够让她完全拥有和控制的系统。

文章主要关注她为集成 Nextcloud（一个自托管平台）进行日历管理所采取的实际步骤。她强调了拥有专用服务器或虚拟专用服务器 (VPS) 来托管 Nextcloud 的重要性，并概述了安装过程。她选择 Nextcloud 是因为它的功能丰富、社区支持以及与其他服务集成的能力。

作者描述了设置 Nextcloud、配置日历应用程序以及将其与各种设备（桌面和移动设备）同步的过程。她还解决了集成过程中遇到的挑战，例如配置 SSL 证书以实现安全连接以及排除同步问题。

文章的一个关键要点是理解自托管所涉及的技术方面的重要性，包括服务器管理和维护。虽然自托管提供了更多的隐私和控制，但也需要一定的技术专业知识。作者强调了数据所有权的长期利益以及控制个人数字足迹所带来的力量。“第一部分”表明这是该系列的第一篇文章，她打算在其中探索日历管理之外的数据所有权的其他方面。

---

## 13. Clojure：无需 ClojureScript 的实时协作 Web 应用

**原文标题**: Clojure: Realtime collaborative web apps without ClojureScript

**原文链接**: [https://andersmurphy.com/2025/04/07/clojure-realtime-collaborative-web-apps-without-clojurescript.html](https://andersmurphy.com/2025/04/07/clojure-realtime-collaborative-web-apps-without-clojurescript.html)

本文介绍了一种使用Clojure构建实时协作Web应用的方法，无需依赖ClojureScript。作者展示了一个多人“生命游戏”应用，该应用通过SSE（服务器发送事件）每200毫秒将整个`<main>`元素从服务器流式传输到客户端。 关键在于，这种方法避免了客户端Javascript，而是使用了一个名为Datastar（压缩后11.4kb）的小型超媒体框架。

核心思想围绕流压缩（Brotli）的效率，它可以通过SSE实现高压缩率（100-230:1），在网络效率和性能方面可能优于使用差异的细粒度更新。 这种方法简化了视图和会话维护。

作者认为，SSE在防火墙、负载均衡、压缩、自动重新连接和工具方面具有优于WebSockets的优势。Datastar 实现了 `view = f(state)` 模型，将 `f(state)` 保留在服务器上。一个使用hyperlith（一个基于Datastar构建的框架）的代码示例，展示了一个简单的渲染函数和动作处理器如何在渲染函数中没有明确的用户区分，但具有用户特定的动作的情况下，创建一个多人游戏体验。

结论强调了Datastar可以轻松地仅使用Clojure实现交互式和协作式Web应用程序。

---

## 14. Show HN: Koreo – Kubernetes平台工程工具包

**原文标题**: Show HN: Koreo – A platform engineering toolkit for Kubernetes

**原文链接**: [https://koreo.dev/](https://koreo.dev/)

Koreo是一个平台工程工具包，旨在简化 Kubernetes 配置管理和资源编排，通过可编程工作流和结构化数据赋能开发者。它允许用户定义复杂的多步骤流程，这些流程能够响应事件并通过工作流和函数管理 Kubernetes 资源，其灵感来源于函数式编程。这些工作流是平台操作的蓝图，而函数是特定任务的可重用构建块。

Koreo 提供结构化的配置管理，支持验证、转换和组合来自多个来源的配置。动态资源物化允许注入值和覆盖定义以创建完整的资源视图，从而确保一致性并执行组织标准。它支持声明式操作符模型、一流测试和 IDE 集成等特性。

Koreo 构建于 Helm、Kustomize、Argo 和 Crossplane 等现有工具之上，充当元控制器编程语言和运行时，将现成的操作符组合成具有凝聚力的平台。用例包括构建内部开发者平台 (IDP)、自动化基础设施、实施统一控制平面、创建开发者抽象、支持多云基础设施即代码 (IaC)、组合操作符、编排部署和定义策略即代码。

Koreo 由 Real Kinetic 开发，拥有多年的平台工程经验，旨在加速产品交付、提高效率并降低复杂性。它还为 Konfigurate 提供支持，Konfigurate 是一个预配置平台，专注于简化初创公司和规模化公司的开发。

---

## 15. 特斯拉加拿大公司称其可疑的4300万加元激励金获取是一场误解。

**原文标题**: Tesla Canada says its shady $43M incentive grab was a misunderstanding

**原文链接**: [https://electrek.co/2025/04/09/tesla-canada-says-its-shady-43-million-incentive-grab-was-a-misunderstanding/](https://electrek.co/2025/04/09/tesla-canada-says-its-shady-43-million-incentive-grab-was-a-misunderstanding/)

特斯拉加拿大公司回应涉嫌不当申领4300万加元电动汽车补贴指控

---

## 16. Parity (YC S24) 正在招聘创始工程师，构建 AI SRE（旧金山现场办公）

**原文标题**: Parity (YC S24) is hiring founding engineers to build an AI SRE (in-person SF)

**原文链接**: [https://www.ycombinator.com/companies/parity/jobs](https://www.ycombinator.com/companies/parity/jobs)

Parity (YC S24) 正在招聘创始工程师（旧金山现场办公），以构建用于事件响应的 AI SRE 平台。 他们有两个职位空缺：创始工程师 - 应用 AI 和创始工程师 - 全栈，均提供 12 万美元至 17 万美元的薪资和 0.25% 至 2.00% 的股权，要求 1 年以上经验。

Parity 旨在通过使用 AI 代理自主地进行分类、根本原因分析和修复基础设施问题来消除值班的痛苦。他们正在经历强劲的早期采用，并相信他们的产品可以定义一个新的类别。

该公司获得了 Y Combinator、General Catalyst 和 Sugar Free Capital 等知名投资者的支持，以及来自 Midjourney 和 Crusoe 等公司的天使投资人。Parity 成立于 2024 年，是 S24 YC 批次的一部分，拥有一支由 3 人组成的团队，并正在积极开发其 AI SRE 解决方案。创始人是 Coleman Smith、Wilson Spearman（首席执行官）和 Jeffrey Tsaw。

---

## 17. 如果你的网站有营业时间会怎么样？ (2022)

**原文标题**: What if your website had business hours? (2022)

**原文链接**: [https://bobbiechen.com/blog/2022/7/21/what-if-your-website-had-business-hours](https://bobbiechen.com/blog/2022/7/21/what-if-your-website-had-business-hours)

陈柏逸的文章《如果你的网站也有营业时间会怎样？》探讨了限制网站可用性的非常规想法，并将之与实体店进行了类比。作者质疑了24/7全天候运行的行业标准及其相关成本，特别是工程师的随叫随到责任。

文章以B&H Photo为例，指出这家成功的企业因宗教原因周六不接受订单，表明虽然一些客户可能会去别处，但许多人稍后会回来，从而最大限度地减少收入损失。这与常见的按年收入除以一年中的分钟数来计算停机成本的方法形成对比，陈柏逸认为这种计算方法过于高估。

作者还引用了Google SRE书中关于“Chubby”的一个轶事，其中故意触发小的中断，以确保用户有备用计划，这表明偶尔的不可用可以管理用户期望。诸如Low-Tech Magazine（太阳能供电）和Kingdom of Loathing（有夜间维护）之类的例子进一步说明了在特定领域限制可用性的可行性。

最终，陈柏逸承认，对于大多数网站，特别是那些提供紧急服务的网站来说，实施营业时间存在实际困难。作者幽默地计算了潜在的云节省与实际收银员成本相比的微薄成本节省。虽然承认减少随叫随到时间的吸引力，但结论倾向于理解为什么网站保持永久开放状态，并引用了客户期望和竞争格局。

---

## 18. Crystal 1.16.0 发布

**原文标题**: Crystal 1.16.0 Is Released

**原文链接**: [https://crystal-lang.org/2025/04/09/1.16.0-released/](https://crystal-lang.org/2025/04/09/1.16.0-released/)

Crystal 1.16.0 已发布，自 1.15.1 版本以来，共有 19 位贡献者提交了 162 项更改。此版本包含新功能、缺陷修复和性能改进。

**重大变更：** `File.match?` 的实现已通过新的 globbing 行为得到纠正，参数名称后缀 '?' 和 '!' 已弃用，`Enumerable#sum` 和 `#product` 要求为联合类型指定显式初始值类型，`HTTP::Request` 现在可以正确解析资源字符串，并且编译器不再为子命令设置 `$CRYSTAL` 环境变量，而是替换为 `$CRYSTAL_EXEC_PATH`。

**新功能/改进：** 提供执行上下文的预览功能，`Slice.literal` 可以推断元素类型并可以在解释器中使用，`macro sizeof` 和 `alignof` 提供有关稳定类型的信息，Path 处理的错误修复和性能改进，新方法 `Indexable#find` 和 `#find!`，新方法 `EventLoop#wait_readable` 和 `#wait_writable`，编译器 CLI 接受带有目录的 `--output`，并且编译器尊重 `$MACOSX_DEPLOYMENT_TARGET`。

文档生成器可以选择包含私有和受保护的对象，以及带有 `:showdoc:` 指令的 lib 绑定中的对象。 现在支持 LLVM 20，并且 LLVM::ABI 已弃用。此次发布由 84codes 等赞助商提供支持。

---

## 19. macOS 9版SDL2“草稿”

**原文标题**: SDL2 for macOS 9 “rough draft”

**原文链接**: [https://macintoshgarden.org/apps/sdl2-macos-9-rough-draft](https://macintoshgarden.org/apps/sdl2-macos-9-rough-draft)

无法访问文章链接。

---

## 20. 本网站使用cookies来存储您已点击“接受Cookies”的事实。

**原文标题**: This site uses cookies to store the fact you clicked “Accept Cookies”

**原文链接**: [https://rodyne.com/?p=2368](https://rodyne.com/?p=2368)

这篇博文是对《通用数据保护条例》(GDPR) 及其对小型网站所有者影响的略带讽刺的评论。 作者身处欧盟以外，幽默地承认其网站可能因使用Cookie而非法，并且可能不符合欧盟法律。

作者对GDPR的有效性表示怀疑，认为大型公司很可能找到规避规则的方法，而小型网站运营者则感到困惑并可能承担责任。 他们承认对WordPress网站和托管设置的内部运作缺乏了解，突显了互联网架构中固有的信任层。 他们相信这些系统没有做任何有害的事情。

作者认为，用户常常被迫盲目接受Cookie政策，而不了解其条款和条件，这可能导致GDPR失效。 他们质疑这些法规的真正影响，认为它们主要使官僚和律师受益。 作者最终主张对互联网使用采取“买者自慎”的态度，认为法规不足以保护在线用户。 他们将互联网定义为“狂野西部”，个人必须谨慎行事。

---

## 21. GCC 15 的可用性改进

**原文标题**: Usability Improvements in GCC 15

**原文链接**: [https://developers.redhat.com/articles/2025/04/10/6-usability-improvements-gcc-15](https://developers.redhat.com/articles/2025/04/10/6-usability-improvements-gcc-15)

我能够访问外部网站，并且可以总结关于GCC 15中可用性改进的文章。

以下是文章的总结：

这篇文章重点介绍了GCC 15中的六项关键可用性改进，旨在使编译器更加用户友好，并有助于诊断问题。

1.  **改进的诊断信息：** GCC 15提供了更精确和信息更丰富的错误消息，包括富含上下文的代码片段，突出显示错误的确切位置和可能的原因。这有助于开发人员快速理解和修复问题。

2.  **`-fdiagnostics-show-caret=always` 成为默认设置：** 编译器现在默认显示指向代码中错误和警告确切位置的插入符号(^)。 这以前是通过标志启用的，但现在是标准行为。

3.  **更精确的诊断位置：** GCC 15增强了报告的错误位置的精度，指向导致问题的确切字符或符号，而不是一般的行。

4.  **标准化的诊断风格：** 编译器采用更一致和可读的诊断消息风格，使其更容易解析和理解。

5.  **彩色诊断消息：** 在适当的终端支持下，GCC 15现在对错误消息、警告和注释进行彩色显示，进一步增强可读性并吸引对重要信息的注意。

6.  **改进了对拼写建议的支持：** GCC 15为代码中的常见拼写错误提供了更好的拼写建议，特别是对于函数名和变量，有助于快速纠正错误。

本质上，这些改进的重点是通过提供更清晰、更精确和更易于阅读的诊断信息，使GCC 15更具沟通性和开发人员友好性。 目标是减少调试时间并改善整体开发体验。

---

## 22. 通过迁移激活控制语言和扩散模型

**原文标题**: Controlling Language and Diffusion Models by Transporting Activations

**原文链接**: [https://machinelearning.apple.com/research/transporting-activations](https://machinelearning.apple.com/research/transporting-activations)

本文介绍了激活传输 (AcT)，这是一种由苹果研究人员开发的新颖的、模态无关的技术，用于对大型生成模型（如语言模型 (LLM) 和文本到图像 (T2I) 扩散模型）进行细粒度控制。 AcT 解决了现有方法（如使用人类反馈的强化学习 (RLHF) 和指令微调，这些方法资源密集，以及提示工程，这种方法提供的控制有限）的局限性。

AcT 利用最优传输理论来引导模型激活，从而学习源激活分布和目标激活分布之间的映射。 这种方法最大限度地减少了对模型自然动态的干扰，并允许通过强度参数进行可解释的控制。 简化版本 Linear-AcT 计算效率高，并且开箱即用地适用于 LLM 和 T2I 模型。

本文重点介绍了 AcT 在控制 LLM 输出方面的有效性，通过减轻毒性和诱导真实性，与其它激活引导方法相比，在这些领域取得了显著改进。 AcT 还允许对 T2I 模型进行细粒度控制，从而可以对图像生成进行增量更改并控制艺术风格。 展示的一个关键应用是从生成的图像中删除不需要的概念，例如“粉红色大象”问题，即使模型被明确指示要避免它们。 AcT 提供了一种实用且高效的方式来控制生成模型，从而确保可靠性、安全性和与用户期望的一致性。 AcT 的代码已公开提供。

---

## 23. Rust编译器中令人惊讶的枚举大小优化

**原文标题**: A surprising enum size optimization in the Rust compiler

**原文链接**: [https://jpfennell.com/posts/enum-type-size/](https://jpfennell.com/posts/enum-type-size/)

James Fennell 的博文探讨了 Rust 编译器中一个令人惊讶的枚举大小优化，超越了广为人知的空指针优化。枚举代表着变体的“或”组合，通常占据的内存大小取决于最大的变体载荷加上一个标签。

该博文首先用 `Foo` 枚举（Int 或 Char）来说明基本的枚举表示，它占据 8 个字节（4 个字节用于载荷，4 个字节用于标签）。然后它解释了空指针优化，以 `Option<char>` 为例，它巧妙地使用无效的 `char` 值作为 `None` 变体，从而将其大小减小到 4 个字节。

令人惊讶的优化出现在嵌套枚举中。一个 `Inner` 枚举（A 或 B，两者都带有 u32 载荷）按预期使用 8 个字节。但是，当 `Inner` 用作 `Outer` 枚举（C 带有 u32，D 带有 Inner）中的一个变体时，`Outer` 意外地保持在 8 个字节，而不是 12 个字节。

编译器在 `Outer` 中重用了 `Inner` 枚举的标签空间。它利用了 `Inner` 的标签只使用 0 或 1 这一事实。`Outer` 将一个新的标签值（在本例中为 2）分配给其另一个变体 (C)。然后，它将 `Outer::D` 表示为与底层 `Inner` 值相同。这使得 `Outer` 能够在现有的标签空间内编码其变体信息，并重用剩余的字节作为载荷，从而有效地避免了预期的大小增加。

---

## 24. 椭圆Python编程

**原文标题**: Elliptical Python Programming

**原文链接**: [https://susam.net/elliptical-python-programming.html](https://susam.net/elliptical-python-programming.html)

椭圆式Python编程

这是一篇幽默的文章，介绍了一种非常规且晦涩难懂的Python代码编写方式，通过布尔比较和`exec`函数实现。作者Susam Pal开玩笑地建议使用诸如`(...==...)`之类的表达式来表示数字1，然后构建复杂的算术运算来生成字符的ASCII码。

这篇文章讽刺了编写极简且技术上有效的、但完全无法阅读的代码的想法。作者承认Python中存在“一种明显的做事方式”原则，但故意提出了一个迟钝的替代方案。

这篇文章强调了主要为机器执行而不是为人类理解而编写代码的荒谬性。在为那些重新映射Tab键的人提供了一个充满括号的替代方案的同时，作者最终提倡“椭圆式”风格，认为其点的形式在避免括号带来的令人不安的“空虚感”方面微妙地更胜一筹。

作者强烈建议不要在生产环境中使用这种风格，并强调可读、可维护的代码以及在不可避免地出错时进行全面日志记录的重要性。这篇文章轻松地提醒我们，代码应该优先考虑清晰性和协作，而不是隐秘的效率，最后以幽默的警告结束，即如果你真的使用它，请添加日志记录。

---

## 25. 《黑镜》的悲观色情不会引领我们走向更美好的未来

**原文标题**: Black Mirror's pessimism porn won't lead us to a better future

**原文链接**: [https://www.theguardian.com/technology/2025/apr/10/black-mirror-tv-show-pessimism](https://www.theguardian.com/technology/2025/apr/10/black-mirror-tv-show-pessimism)

路易斯·安斯洛认为，《黑镜》对科技的悲观描绘虽然引人入胜，但最终是有害的，因为它会助长恐惧并阻碍进步。他认为该剧过度强调反乌托邦叙事，忽视了技术进步的潜在益处和二元性。

安斯洛批评这种“悲观主义色情”助长了“弗兰肯斯坦谬误”，导致基于恐惧的决策，从而产生有害的现实后果。他举例说，对转基因作物（导致饥荒）、核能（导致依赖化石燃料）和电子烟（同时允许传统香烟）的抵制就是例子。

作者认为，这种反乌托邦心态在 1960 年代后的科幻小说中很常见，它阻碍我们想象和积极建设更美好的未来。他指出，在 COVID-19 大流行期间，当技术对于连接和生存至关重要时，反乌托邦叙事失去了吸引力。

安斯洛呼吁一种新的“进步主义”，拥抱建设和实用主义，倡导承认科技风险和机遇的寓言。他强调需要“充满希望的解决方案主义”，承认脑芯片帮助截瘫患者、机器狗清除地雷、人工智能预防超级细菌以及虚拟现实连接人们的潜力。我们不应助长恐惧，而应找到管理风险并利用技术优势，从而创造更美好未来的方法。

---

## 26. PEP 750 – 模板字符串

**原文标题**: PEP 750 – Template Strings

**原文链接**: [https://peps.python.org/pep-0750/](https://peps.python.org/pep-0750/)

PEP 750 在 Python 3.14 中引入了“模板字符串”（t-字符串），解决了 f-字符串在需要于最终字符串组合之前进行值转换的场景下的局限性。 以 `t` 为前缀的 t-字符串求值为 `Template` 对象，从而可以访问字符串的各个部分和插值。

主要特点包括：

*   **模板类：** `Template` 类将字符串部分（`strings`）和插值部分（`interpolations`）作为元组保存。
*   **插值类：** `Interpolation` 类表示模板中的表达式，公开求值后的 `value`、原始 `expression`、可选 `conversion` (a, r, s) 和 `format_spec`。
*   **灵活性：**  开发者可以使用任意代码来处理模板。 T-字符串支持诸如 HTML 清理、结构化日志记录和特定领域语言等用例。
*   **连接：** 模板字符串支持使用 `+` 运算符与其他模板或字符串进行显式连接。
*   **迭代：** `__iter__` 方法提供了一种按顺序访问字符串和插值的方法。
*   **调试说明符支持：** 调试说明符 (=) 的行为类似于 f-字符串，同时打印表达式及其值。
*   **相等性：** Template 和 Interpolation 实例与对象标识进行比较。
*   **不支持排序：** Template 和 Interpolation 类型不支持排序。

此 PEP 旨在通过公开插值的中间值来提供更灵活和安全的字符串处理机制，这有助于防止诸如 SQL 注入和 XSS 攻击之类的漏洞。 该 PEP 还解释了如何使用新的 `Template` 和 `Interpolation` 类、如何处理模板字符串，并提供了示例用例。

---

## 27. 每次看都有不同的感受的电影

**原文标题**: The movie that's different every time you watch it

**原文链接**: [https://movieweb.com/eno-documentary-movie-different-every-time/](https://movieweb.com/eno-documentary-movie-different-every-time/)

本文探讨了名为“Eno”的突破性纪录片，该片讲述了极具影响力的音乐家、制作人兼视觉艺术家布莱恩·伊诺的生活和作品。这部纪录片的独特之处在于，每次观看都是不同的。这是通过导演加里·哈斯特维特创作的生成式软件实现的。该软件动态地组装不同的场景、音乐提示和档案片段，确保非线性和不可预测的观看体验。

这部纪录片并非传统的按时间顺序叙事的传记片。相反，它旨在捕捉伊诺的创作过程和他不断演变的艺术愿景的精髓。哈斯特维特利用伊诺大量的访谈、视觉实验和音乐档案，创建了一个实时混音和重新组装这些元素的系统。这反映了伊诺本人对生成音乐的迷恋以及他对拥抱偶然和实验的哲学。

本文强调了这种创新方法带来的挑战和机遇。虽然有些人可能会觉得缺乏传统的叙事方式令人困惑，但它最终旨在提供对伊诺艺术世界更真实和沉浸式的体验。这部纪录片有效地体现了伊诺的哲学，并让观众以一种像伊诺本人一样不可预测且不断变化的方式参与他的作品。从本质上讲，“Eno”被呈现为一种真正独特的电影体验，旨在成为一件生成式艺术品本身，而不是一部简单的传记。

---

## 28. 市政消防车与机场消防车的区别

**原文标题**: The Difference Between Municipal Fire Trucks and Airport Fire Trucks

**原文链接**: [https://www.piercemfg.com/pierce/blog/difference-between-municipal-and-airport-fire-trucks](https://www.piercemfg.com/pierce/blog/difference-between-municipal-and-airport-fire-trucks)

本文重点介绍了市政消防车和机场救援消防车(ARFF)之间的主要区别。虽然两者都设计用于灭火，但其专门设计针对不同的紧急情况。

市政消防车适用于城市、郊区和乡村环境，根据可用基础设施的不同，水箱大小各异。美国消防协会标准要求它们在 25 秒内加速到 35 英里/小时，最高时速达到 50 英里/小时。出警范围包括建筑物火灾和机动车辆事故。

机场救援消防车专门设计用于应对机场紧急情况，包括飞机坠毁、燃油泄漏和航站楼事故。它们必须在三分钟内到达现场，经常面临危险的环境。机场救援消防车遵循更严格的加速标准，需要在 25 秒内达到 50 英里/小时，并达到 70 英里/小时的最高时速。由于消防栓接入有限，它们携带大量的水（1500-4500 加仑）。一个显著的特点是高空伸缩炮塔 (HRET)，用于刺穿飞机机身并输送水或灭火剂。

灭火系统也不同。市政消防车使用水和灭火泡沫，而机场救援消防车依靠水、灭火泡沫（用于燃油泄漏）和干粉化学品（作为最后的手段）。

存储解决方案对于这两种类型都至关重要，重点是减少消防员接触致癌物的机会。市政消防车携带软管、工具和医疗用品，而机场救援消防车则存放牵引设备、通信设备、救援工具和医疗包。

最后，驾驶室的设计也截然不同。市政消防车驾驶室最多可容纳 10 名消防员，并且通常优先考虑清洁性。机场救援消防车驾驶室则优先考虑视野和机动性，具有更大的操作区域和一个倾斜的车身，以适应越野能力。操作员通常从中央座椅控制卡车的所有功能。

---

## 29. Arroyo (YC W23) 已被 Cloudflare 收购

**原文标题**: Arroyo (YC W23) has been acquired by Cloudflare

**原文链接**: [https://www.arroyo.dev/blog/arroyo-is-joining-cloudflare](https://www.arroyo.dev/blog/arroyo-is-joining-cloudflare)

专注于流处理的Y Combinator 2023冬季孵化项目公司Arroyo已被Cloudflare收购。Arroyo团队在一篇博文中宣布了此次收购，表示他们将加入Cloudflare，共同构建数据流处理的未来。

Arroyo的技术使开发人员能够构建具有低延迟和高可靠性的实时数据管道。它旨在简化复杂的流处理任务，使其对欺诈检测、物联网数据分析和实时分析等各种用例更易于访问和高效。

该博文强调，加入Cloudflare将使Arroyo能够利用Cloudflare的全球基础设施和资源来加速其流处理平台的开发和部署。此次收购很可能会将Arroyo的技术集成到Cloudflare现有的服务套件中，从而可能增强Cloudflare在边缘计算、数据分析和安全等领域的能力。

虽然未披露此次收购的具体财务条款，但该公告强调了Arroyo和Cloudflare在提供强大且易于访问的数据处理解决方案方面的共同愿景。Arroyo团队对有机会为Cloudflare构建更美好互联网的使命做出贡献感到兴奋。此次收购表明Cloudflare将继续投资于扩展其在数据流处理和实时处理领域的能力。

---

## 30. 具备摄像头和屏幕共享功能的 Gemini Live

**原文标题**: Gemini Live with camera and screen sharing capabilities

**原文链接**: [https://blog.google/products/gemini/gemini-live-android-tips/](https://blog.google/products/gemini/gemini-live-android-tips/)

本文宣布 Gemini Live 功能将更广泛地推出。该功能允许用户通过手机的摄像头和屏幕共享功能与 Gemini AI 进行互动。最初仅面向 Android 上的 Gemini Advanced 订阅者开放，现在正推广到 Pixel 9 和 Samsung Galaxy S25 设备上的所有 Gemini 应用程序用户。

本文重点介绍了 Gemini Live 的五个主要用例：

1.  **整理收纳：** 使用摄像头向 Gemini 展示杂乱的空间，并获得关于整理、分类物品和最大化空间利用的实时建议。

2.  **创意头脑风暴：** 与 Gemini 分享屏幕上鼓舞人心的图片，从而激发创意写作、设计或工艺品的灵感。

3.  **问题排查：** 使用摄像头实时向 Gemini 展示物品问题，并获得关于如何解决的建议。

4.  **个人购物建议：** 在浏览在线零售商时分享你的屏幕，并获得比较、风格建议以及对你选择的反馈。你也可以使用摄像头向 Gemini 展示你的衣橱，并获得关于搭配单品的建议。

5.  **技能发展和反馈：** 与 Gemini 分享你的屏幕，以获得对各种类型工作的反馈，例如博客文章、社交媒体活动或照片，并获得关于布局、设计和整体改进的建议。

Gemini Live 旨在提供更自然和互动的 AI 体验，为用户在生活的各个方面提供即时反馈和指导。该功能目前支持超过 45 种语言。

---

## 31. Pdeathsig 几乎永远不是你想要的。

**原文标题**: Pdeathsig is almost never what you want

**原文链接**: [https://www.recall.ai/post/pdeathsig-is-almost-never-what-you-want](https://www.recall.ai/post/pdeathsig-is-almost-never-what-you-want)

该博文详细介绍了优化Recall.ai的“输出媒体”功能启动延迟所进行的调试过程。该功能在沙盒环境中将网页渲染成音频和视频，供人工智能代理使用。

最初的目标是在机器人启动时预加载用于渲染的浏览器Chromium，以减少12秒的延迟。然而，在实施此更改后，Chromium在集成测试期间意外终止。

根本原因在于Bubblewrap（一种轻量级沙盒工具）使用的`--die-with-parent`标志。该标志利用Linux内核的`PR_SET_PDEATHSIG`特性，该特性旨在在其父进程死亡时终止子进程。然而，关键的细节是`PR_SET_PDEATHSIG`跟踪的是父*线程*，而不是整个父*进程*。

Recall.ai使用Tokio（一个异步运行时），它管理一个工作线程池。当一个使用`PR_SET_PDEATHSIG`启动Bubblewrap的线程被Tokio的调度器暂停或回收时，内核错误地将其解释为父进程的死亡，从而触发一个SIGKILL信号给Bubblewrap进程（并因此传递给Chromium）。

移除`--die-with-parent`标志通过禁用错误的机制解决了该问题。Tokio的线程管理、Bubblewrap的进程隔离和Linux内核内部机制之间这种微妙的交互是未被记录的。成功的优化显著降低了启动延迟，从12秒降至2-3秒。作者强调了在调试时理解底层细节的重要性。

---

## 32. 梅西耶马拉松

**原文标题**: Messier Marathon

**原文链接**: [https://en.wikipedia.org/wiki/Messier_marathon](https://en.wikipedia.org/wiki/Messier_marathon)

梅西耶马拉松是一项天文活动，观测者（通常是业余天文学家）尝试在一个晚上尽可能多地找到所有110个梅西耶天体（由查尔斯·梅西耶编目的明亮深空天体）。

马拉松的成功取决于地点、一年中的时间和天气。较低的北纬地区（大约北纬25度）是最佳选择，因为所有天体的可见度更好。最佳时间是三月中旬到四月初的新月前后，尽管在其他时间，特别是秋分前后，也能进行不太完整的马拉松。

这个概念在20世纪70年代由几位美国天文学家独立发明。观测者通常在日落时开始，向东横扫天空，在西方地平线上的天体落下之前找到它们，然后在日出前捕捉东方地平线上的最后几个天体。这既是对耐力的考验，也是对观测技巧的考验，尤其是在航行于拥挤的区域，比如室女座星系团和银河中心时。

梅西耶马拉松通常由当地天文俱乐部组织，作为一种星空派对。这些活动为业余天文爱好者提供了友谊、竞争和学习的机会。一些俱乐部甚至为参与或取得成就者提供奖励。

---

## 33. 路易斯安那州监狱委员会使用算法来确定假释资格

**原文标题**: Louisiana prison board uses algorithms to determine eligility for parole

**原文链接**: [https://www.propublica.org/article/tiger-algorithm-louisiana-parole-calvin-alexander](https://www.propublica.org/article/tiger-algorithm-louisiana-parole-calvin-alexander)

在路易斯安那州，一项新法律利用TIGER算法来决定假释资格，禁止风险评分为“中等”或“高”的囚犯出现在假释委员会面前。 这影响了该州近一半的监狱人口，约13,000人。 这项由州长杰夫·兰德里倡导的法律，反映了一种“严厉打击犯罪”的立场，限制了提前释放，并且与路易斯安那州累犯率下降的证据相悖。

最初旨在作为识别囚犯需求的改造工具的TIGER算法，现在成为了假释资格的严格决定因素。 该算法对过去犯罪历史、就业和首次被捕年龄等不可改变因素的依赖，引发了对种族偏见的担忧，因为由于系统性不平等，这些因素不成比例地影响着黑人。 民权律师认为，该法律可能违宪，因为它追溯性地增加了刑期，并忽视了囚犯的改造努力。

刑事司法专家批评路易斯安那州将风险评分专门用于假释资格的做法，因为这些算法不够精确，无法预测个人行为。 前假释委员会成员也表示担忧，该算法取代了人为判断，削弱了假释委员会的权力。 在这项法律之前，像阿隆佐·艾伦这样风险评分为“中等”的囚犯可以证明自己的改造并获得假释。 现在，仅算法的评分就可以阻止假释资格，而不管个人的进步如何。 卡尔文·亚历山大是一名近乎失明的 70 岁囚犯，就是一个这样的例子，在因他的 TIGER 分数而被取消假释听证会后，他感到“背叛”。

---

## 34. 面向痛苦编程 (2012)

**原文标题**: Suffering-Oriented Programming (2012)

**原文链接**: [http://nathanmarz.com/blog/suffering-oriented-programming.html](http://nathanmarz.com/blog/suffering-oriented-programming.html)

本文介绍了“痛苦驱动编程”，这是一种基于已体验到的痛点来构建技术，而非过早优化或通用解决方案的开发风格。其核心思想是，只有当你深切感受到需要时才构建技术，从而确保相关性以及对问题领域的深刻理解。

本文概述了三个步骤：

1. **让它可行：** 拼凑出一个可行的解决方案来解决当前问题，专注于直接完成任务。这个阶段是关于获得经验并理解问题空间的复杂性。

2. **让它美观：** 将从第一阶段获得的知识提炼成简单、可组合的抽象概念，以解决现有的用例。避免过度设计，只关注具体的需求。设计应考虑早期学习到的性能和资源特性。

3. **让它快速：** 在一个坚实而美观的设计基础上，专注于微优化和资源效率。这个阶段是关于优化代码，而不是高层次的架构变更。

作者强调，这个过程是迭代的，从而带来持续的改进和对问题领域的更深刻理解。他强调了重构的重要性，以防止意外的复杂性，并强调用例对于推动开发至关重要。痛苦驱动编程拒绝过早的泛化，提倡由实际用例驱动的设计，而不是预期的未来需求。

---

## 35. 每周八杯或以上饮品与脑损伤有关

**原文标题**: Eight or more drinks per week linked to brain lesions

**原文链接**: [https://www.aan.com/PressRoom/Home/PressRelease/5251](https://www.aan.com/PressRoom/Home/PressRelease/5251)

神经病学研究：饮酒与大脑健康关联

这项发表在《神经病学》上的研究调查了饮酒与大脑健康之间的联系。研究人员检查了1781名平均死亡年龄为75岁的个体的脑部尸检，分析了脑组织中是否存在诸如透明样动脉硬化（血管性脑损伤）和tau蛋白缠结等损伤迹象。他们根据家庭报告将参与者分为不饮酒者、适度饮酒者（每周7杯或以下）、大量饮酒者（每周8杯或以上）和以前的大量饮酒者。

研究发现，与从不饮酒者相比，大量饮酒者患血管性脑损伤的风险显著更高（几率高133%）。以前的大量饮酒者也表现出风险增加（几率高89%），适度饮酒者也是如此（几率高60%）。大量饮酒者和以前的大量饮酒者患tau蛋白缠结（阿尔茨海默病的一种生物标志物）的几率也更高。以前的大量饮酒与较低的脑质量比和较差的认知能力有关。值得注意的是，大量饮酒者的平均死亡时间比从不饮酒者早13年。

虽然这项研究并未证明因果关系，但它表明大量饮酒与脑损伤之间存在很强的关联。这种损伤可能导致记忆和思维问题，突出了公众健康意识和预防措施以减少大量饮酒的重要性。该研究的局限性在于缺乏死前信息和关于饮酒持续时间的数据。

---

## 36. 你的睡眠追踪器对睡眠的误解

**原文标题**: What Your Sleep Tracker Gets Wrong About Sleep

**原文链接**: [https://www.affectablesleep.com/blog/what-your-sleep-tracker-gets-wrong-about-sleep](https://www.affectablesleep.com/blog/what-your-sleep-tracker-gets-wrong-about-sleep)

来自Affectable Sleep的文章批判了睡眠追踪器的局限性。虽然追踪器可以提供睡眠时长、阶段和规律性的数据，但它们往往无法准确反映睡眠的质量和恢复性，从而可能导致误导性的结果。

作者认为，追踪器过于强调规律性（相同的就寝时间，相同的睡眠时长），而忽略了实际的恢复性睡眠，即使睡眠并非真正有益，也会奖励对作息时间的遵守。他们还强调，追踪器专注于深度睡眠或快速眼动睡眠的数量，而没有考虑到这些阶段中发生的*质量*或恢复功能。文章指出，研究表明，即使睡眠时间充足，人为地减少深度睡眠也会对大脑产生负面影响。

此外，文章认为，追踪器可能会对睡眠质量的感知产生负面影响。当追踪器报告睡眠良好，但人们仍然感到疲倦时，他们可能会怀疑自己的主观体验。文章还批评对过去睡眠的关注毫无帮助，因为它没有提供任何实时指导来改善当晚的睡眠。

Affectable Sleep提倡一种不同的方法，专注于实时优化睡眠，以增强其恢复能力。他们不只是简单地跟踪和分析数据，而是旨在改善睡眠期间发生的生理和神经过程，最终实现更有效和恢复性的睡眠，而与时间无关。文章最后邀请读者加入他们的等候名单，探索一种更有效的睡眠增强方法。

---

## 37. 艾萨克·阿西莫夫描述人工智能将如何解放人类及其创造力 (1992)

**原文标题**: Isaac Asimov describes how AI will liberate humans and their creativity (1992)

**原文链接**: [https://www.openculture.com/2025/04/isaac-asimov-describes-how-ai-will-liberate-humans-their-creativity.html](https://www.openculture.com/2025/04/isaac-asimov-describes-how-ai-will-liberate-humans-their-creativity.html)

本文总结了 1992 年对艾萨克·阿西莫夫的采访，他在采访中将人工智能（AI）定义为任何执行先前与人类智能相关的任务的设备。他设想人工智能将人类从单调、重复的工作中解放出来，使他们能够专注于计算机无法处理的创造性和复杂任务。阿西莫夫认为，人工智能和人类智能将协同合作，以推动人类进步。

文章强调了阿西莫夫对人工智能整合的前瞻性观点，将其与汽车的出现进行比较，并敦促人们积极规划以减轻潜在问题。虽然承认潜在的困难，但阿西莫夫对人工智能的总体益处持乐观态度。

然而，文章作者增加了一丝警惕，将阿西莫夫的愿景与以汽车为中心的城市规划的现实进行对比，认为保留前人工智能时代的一些元素可能对后代有利。本质上，这篇文章呈现了阿西莫夫对人工智能在解放人类创造力方面的乐观愿景，同时也促使人们反思未经控制的技术进步的潜在弊端。

---

## 38. ELD: 一款用于嵌入式系统的新型开源嵌入式链接器工具

**原文标题**: ELD: A new open-source embedded linker tool for embedded systems

**原文链接**: [https://www.qualcomm.com/developer/blog/2025/04/eld-new-open-source-embedded-linker-tool-for-embedded-systems](https://www.qualcomm.com/developer/blog/2025/04/eld-new-open-source-embedded-linker-tool-for-embedded-systems)

ELD：一款面向嵌入式系统的新型开源链接器

---

## 39. Smartfunc: 将文档字符串转化为LLM函数

**原文标题**: Smartfunc: Turn Docstrings into LLM-Functions

**原文链接**: [https://github.com/koaning/smartfunc](https://github.com/koaning/smartfunc)

Smartfunc 是一个 Python 库，它通过利用文档字符串简化了由大型语言模型 (LLM) 驱动的函数的创建。它的工作原理是解析函数的文档字符串，并将其用作 Jinja2 模板，以生成通过 `llm` 库发送到 LLM 的提示。`llm` 库提供了一个维护良好的基础、一个用于不同 LLM 提供商的后端生态系统、异步支持以及使用 Pydantic 模型的模式支持。

主要特性和优势：

*   **文档字符串即提示：** 直接在函数文档字符串中定义 LLM 提示，增强可读性和可维护性。
*   **后端装饰器：** 使用装饰器（`backend` 和 `async_backend`）来指定 LLM 提供商（例如，“gpt-4”）以及可选参数，如系统提示和温度。
*   **模式支持：** 允许使用 Pydantic 模型定义预期的响应格式，从而能够从 LLM 输出中提取结构化数据。
*   **内部函数提示工程：** 允许使用函数体来进一步操纵和改进从文档字符串返回的提示。
*   **异步支持：** 支持异步函数以提高性能，尤其是在使用微批处理时。
*   **调试模式：** 提供调试模式，显示生成的提示、LLM 响应以及其他相关信息以进行故障排除。
*   **专注于简洁：** 旨在实现简洁性和快速原型设计，提供基本功能，而没有其他 LLM 集成库的复杂性。

---

## 40. 黑客新闻无声拥抱

**原文标题**: Hacker News Hug of Deaf

**原文链接**: [https://susam.net/hn-bell.html](https://susam.net/hn-bell.html)

苏珊·帕尔的文章描述了一个名为“Hacker News失聪之拥”的有趣实验。受Hacker News上关于DIY警报系统的讨论启发，帕尔在Debian服务器上设置了一个简单的netcat循环，该循环在收到连接时，会发送“ok”消息，关闭连接，并触发四个终端蜂鸣声。

该实验在Hacker News上宣布，邀请用户连接到susam.net:8000服务器。在接下来的24小时内，帕尔收到了超过4761个连接，导致超过19000次终端蜂鸣。虽然连接数量相对较少，但它表明了HN社区参与古怪想法的意愿。帕尔强调了该项目的乐趣和探索性，认为计算不仅仅是解决问题，还在于探索新颖的概念。

在五天后发布的文章更新中，帕尔分享了他在Hacker News上的文章后，连接再次激增。这一次，服务器收到了超过30万个连接，这主要归因于持久的客户端循环。帕尔对Hacker News社区的活跃和持续参与表示感谢。这篇文章突出了计算的乐趣以及与他人分享和探索不寻常想法所带来的乐趣。

---

## 41. 从零开始设计 TigerBeetle 的文档

**原文标题**: We Designed TigerBeetle's Docs from Scratch

**原文链接**: [https://tigerbeetle.com/blog/2025-02-27-why-we-designed-tigerbeetles-docs-from-scratch/](https://tigerbeetle.com/blog/2025-02-27-why-we-designed-tigerbeetles-docs-from-scratch/)

TigerBeetle从零开始重建了他们的文档站点，旨在为用户提供更快、更简洁、更清晰的阅读体验，体现了他们的“TigerStyle”理念。由于Docusaurus的NodeJS依赖、复杂性、Markdown文件中不必要的代码以及次优的搜索体验，他们对其并不满意，因此寻求一种与数据库本身融为一体的解决方案。

他们的主要目标是提供像书一样简洁的阅读体验，最大限度地减少干扰。他们移除了面包屑导航和页脚等元素，将顶部导航集成到侧边导航中，并实现了基于系统设置的自动暗/亮模式。

他们考虑过基于Zig的静态站点生成器（SSG）Zine，但最终选择使用Pandoc进行Markdown解析，创建自己的解决方案，因为Zine的SuperMD与GitHub风格的Markdown（GFM）不兼容。

他们利用Zig的内置包管理器，将Pandoc作为静态构建的可执行文件引入，通过内容哈希验证确保了可重现性，并降低了供应链攻击的风险。整个静态站点生成都在Zig的构建系统中作为构建任务实现，从而实现了增量更新。他们对Pandoc二进制文件使用惰性依赖，仅下载基于主机操作系统所需的版本。文章包含了一个详细的代码示例，展示了他们如何使用Zig的构建系统集成Pandoc，将Markdown文件转换为HTML，并创建任务图以实现高效的、缓存的网站生成。

---

## 42. 无夸克超对撞机或可揭示暗物质之谜

**原文标题**: A quarkless supercollider may finally shed light on dark matter

**原文链接**: [https://spectrum.ieee.org/supercolliders](https://spectrum.ieee.org/supercolliders)

本文探讨大型强子对撞机（LHC）之后粒子物理研究的未来，重点介绍了四个拟议的下一代超级对撞机。这些对撞机旨在解决标准模型的缺陷，并可能揭示新的物理现象，例如暗物质的本质。

本文概述了四个主要提案：国际直线对撞机（ILC）、μ子对撞机、未来环形对撞机（FCC-ee/hh）和环形正负电子对撞机（CEPC）。每种对撞机都具有独特的优势和挑战，涉及以高于LHC的能量或更高的精度碰撞不同的粒子（电子、正电子、μ子、质子）。

ILC使用电子和正电子，技术上已经成熟，但面临日本的政治延误。μ子对撞机是一个更具推测性的选择，提供高能量和精度，但需要重大的技术发展。欧洲核子研究中心的FCC-ee/hh和中国的CEPC，最初都设计用于电子-正电子碰撞，之后可能会进行质子升级，被认为是建造最有可能的候选者。

本文深入探讨了所涉及的工程难题，包括建造大型隧道（长达100公里）、克服复杂的地质构造，以及开发高效的超导射频（SRF）腔体和强大的速调管。它还涉及地缘政治方面的考虑，如国际融资和政府批准。这些项目的时间表很长，最早的潜在启动日期在2030年代后期，因此当前的规划和决策至关重要。

---

## 43. 可能有助于治疗创伤性脑损伤的被忽视的迷幻剂

**原文标题**: The overlooked psychedelic that may help treat traumatic brain injury

**原文链接**: [https://bigthink.com/health/ibogaine-traumatic-brain-injury/](https://bigthink.com/health/ibogaine-traumatic-brain-injury/)

伊博格碱治疗创伤性脑损伤及创伤后应激障碍的潜力

---

## 44. 用于快速存储的巨像

**原文标题**: Colossus for Rapid Storage

**原文链接**: [https://cloud.google.com/blog/products/storage-data-transfer/how-the-colossus-stateful-protocol-benefits-rapid-storage](https://cloud.google.com/blog/products/storage-data-transfer/how-the-colossus-stateful-protocol-benefits-rapid-storage)

Google Cloud 快速存储利用 Google 内部的 Colossus 文件系统，在保持对象存储可扩展性的同时，提供亚毫秒级延迟和可追加写入。这通过使用基于状态的 gRPC 流协议来实现。

Colossus 是许多 Google 产品的底层基础，它使用先进的 SSD 放置技术和一种状态协议。借助快速存储，Google Cloud 客户可以直接使用此 Colossus 协议。当客户端创建一个流时，会获得一个包含文件存储信息的句柄，从而可以通过优化的网络协议直接访问磁盘。这有助于实现超低延迟的持久追加，有利于数据库和流式分析。

快速存储在此基础上，预先加载像流创建时的授权等操作，允许后续的读/写操作直接访问 Colossus。这种架构在一个存储桶内支持高请求速率（2000 万次/秒），适用于涉及范围读取和持久写入的 AI/ML 工作负载。

为了处理客户端或服务器中断，快速存储使用句柄进行流重建，并保证一次只有一个 gRPC 流可以写入对象，锁定先前的流，并通过偏移量跟踪确保数据正确性。通过更新的 SDK、Cloud Storage FUSE 和原生分层命名空间支持，集成得到了简化。

快速存储结合了低延迟、高吞吐量和可扩展性，适用于 AI/ML 数据准备、分布式数据库、批处理/流式分析、视频直播和日志/监控等用例。

---

## 45. 任何程度的饮酒都对我们的健康有害 (2023)

**原文标题**: No level of alcohol consumption is safe for our health (2023)

**原文链接**: [https://www.who.int/europe/news/item/04-01-2023-no-level-of-alcohol-consumption-is-safe-for-our-health](https://www.who.int/europe/news/item/04-01-2023-no-level-of-alcohol-consumption-is-safe-for-our-health)

世界卫生组织2023年声明：任何程度的饮酒对健康均不安全。

---

## 46. 细胞正在交换线粒体。这对我们的健康意味着什么？

**原文标题**: Cells are swapping their mitochondria. What does this mean for our health?

**原文链接**: [https://www.nature.com/articles/d41586-025-01064-5](https://www.nature.com/articles/d41586-025-01064-5)

本文探讨线粒体转移这一新兴领域——线粒体在细胞间的惊人移动。与传统观点认为线粒体是静态的、完全位于细胞内的细胞器相反，研究表明它们可以在细胞之间移动，可能充当一种“多细胞细胞器”。这种现象已在多种生物中观察到，但由于技术限制，其在人类中的发生仍未得到证实。

研究人员认为线粒体转移可能是一种细胞通讯和支持的形式。在细胞压力时期，健康的线粒体可能会被捐赠给邻近细胞，以启动组织修复、增强免疫系统或防止细胞死亡。相反，一些研究表明癌细胞将线粒体转移用作一种武器。小鼠研究表明，星形胶质细胞在中风后将线粒体捐赠给神经元，从而提高它们的存活率。同样，间质细胞在急性肺损伤期间将线粒体转移到肺细胞，帮助恢复。血小板也可以将线粒体转移到干细胞，从而加速伤口愈合。

此外，线粒体转移可能在维持健康组织和免疫功能方面发挥作用。星形胶质细胞将线粒体捐赠给大脑中的血管细胞，从而维持血脑屏障。白色脂肪细胞将线粒体转移到巨噬细胞，从而影响能量消耗。在免疫系统中，捐赠的线粒体可以对T细胞产生抗炎作用。尽管有这些发现，关于转移的线粒体在心血管疾病和肥胖症等各种疾病中的机制、寿命和具体作用，仍然存在许多问题。研究人员正在积极探索利用这一过程进行治疗干预的潜力。

---

## 47. 繁忙酒吧

**原文标题**: Busy Bar

**原文链接**: [https://busy.bar](https://busy.bar)

BUSY Bar是一款提高效率的多功能设备，配有LED像素显示屏，旨在增强专注力并最大限度地减少干扰。它提供可定制的忙碌消息、番茄工作法定时器，并与各种应用程序和智能家居系统集成。

主要功能包括：带有手机和PC干扰拦截器的专注定时器、可定制的BUSY消息、跨平台同步以及开源开发工具。BUSY Bar对开发者友好，提供开放的HTTP API、Python、Go和JavaScript的SDK、MQTT支持，且无厂商锁定。

该设备通过Matter协议与Google Home和Apple Home集成，并提供智能家居支持。它还具有应用程序库，可连接到第三方软件，并与日历事件和通话集成。Busy Bar提供通知阻止、智能家居集成、可定制的自动化以及可定制的LED状态显示等功能。

BUSY Bar的设计结合了物理按钮以进行手动控制，包括开始/暂停按钮、返回按钮、滚轮和模式选择器。它拥有单色背屏，方便查看状态。该设备包括间隔专注定时器、干扰拦截，并与免费的基于云的BUSY应用程序集成，以实现多设备静音功能。

它还提供基于麦克风或摄像头活动的自动状态更新，并支持Windows、macOS和Linux。BUSY Bar具有多种连接选项，包括USB、LAN和云，并附带安装硬件。

---

## 48. 没有可信数据，也能实现可信人工智能

**原文标题**: Trustworthy AI Without Trusted Data

**原文链接**: [https://actu.epfl.ch/news/trustworthy-ai-without-trusted-data/](https://actu.epfl.ch/news/trustworthy-ai-without-trusted-data/)

EPFL研究人员开发了ByzFL，一种旨在提高使用联邦学习的人工智能系统可信度的新工具。联邦学习在分散的数据源上训练AI模型，无需集中原始数据。这种方法解决了安全性、隐私和数据所有权问题，但也引入了来自各个来源的“坏”数据（不正确、恶意或故障数据）损害AI可靠性的风险。

Rachid Guerraoui教授及其团队创建了ByzFL，用于对联邦学习模型进行基准测试并增强其对抗对抗性威胁（特别是坏数据）的能力。ByzFL不直接识别坏数据，而是使用强大的聚合方法来最大限度地减少极端输入的影响。该库允许用户模拟坏数据进行测试，并包含用于增强鲁棒性的安全过滤器。

研究人员认为，目前的人工智能虽然对电影推荐等简单任务有用，但对于医疗保健或自动驾驶汽车等关键应用而言还不够安全。他们认为ByzFL可以帮助弥合这一差距，确保下一代人工智能的可靠性。他们提出，瑞士凭借其在质量和可靠性方面的声誉，可以通过ByzFL等工具在认证AI安全方面发挥关键作用。ByzFL软件旨在证明，无需信任单个数据源即可实现AI安全。

---

## 49. 猎杀红色十月1990 (2016)

**原文标题**: Hunt for Red October 1990 (2016)

**原文链接**: [http://www.modelshipsinthecinema.com/2016/12/hunt-for-red-october-1990.html](http://www.modelshipsinthecinema.com/2016/12/hunt-for-red-october-1990.html)

本文详细介绍了1990年电影《猎杀红色十月》的视觉特效制作，特别关注了所使用的小型潜艇模型和技术。 最初，格雷格·杰恩领导下的Boss Films开始了微缩模型的工作，但由于创作分歧和时间紧迫，该项目转移到了ILM。

ILM使用运动控制来拍摄潜艇模型，主要是在烟雾弥漫的环境中进行，以最大限度地减少光学合成。 微缩舰队包括各种尺寸的红色十月号、克洛诺洛夫号和达拉斯号潜艇，以及一艘救援潜艇和鱼雷。

一个线缆操纵系统，从之前的项目中改进而来，被用于悬挂和控制模型的运动，允许俯仰和偏航。 该操纵系统安装在一个运动控制的起重机和轨道系统上。 通过调暗背景灯的光线技巧，营造出令人信服的水下氛围。 近距离拍摄时使用了镜子，以避免相机碰撞。

烟雾效果是通过一个雾化矿物油的裂解系统实现的。 大约建造了40个微型岩石尖塔来模拟水下海沟。 该文章指出，虽然水下环境模拟效果令人信服，但一些光学合成，特别是对抗措施和鱼雷尾迹，效果不太理想。

此外，文章还提到了一架微型俄罗斯熊轰炸机，并包含了关于拍摄结束后处理微缩模型的信息，并提到了它们在拍卖会上出售的情况。 它还引用了Cinefex杂志作为来源，并指出了各种模型制作者和特效主管的参与。

---

## 50. 土星卫星泰坦可能存在生命，但含量极少

**原文标题**: Saturn's moon Titan could harbor life, but only a tiny amount

**原文链接**: [https://news.arizona.edu/news/saturns-moon-titan-could-harbor-life-only-tiny-amount-study-finds](https://news.arizona.edu/news/saturns-moon-titan-could-harbor-life-only-tiny-amount-study-finds)

本文探讨了一项关于土卫六泰坦上存在生命可能性的新研究。研究人员使用生物能量模型评估了泰坦的地下海洋是否能支持以有机物为食的生命形式。虽然泰坦富含有机化合物，但研究结论表明，它只能支持非常少量的生物量，可能只有几公斤，或相当于一只小型犬的质量。

该研究侧重于发酵作用，将其作为假想泰坦微生物的一种合理代谢过程，并以甘氨酸（一种简单的氨基酸）作为潜在的食物来源。然而，模拟显示，只有一小部分可用的有机物可能适合消耗。通过陨石撞击形成的融化池从地表输送来的甘氨酸供应有限，这将导致微生物种群稀疏，平均每升水中不足一个细胞。

研究结果表明，尽管泰坦有机物丰富，但合适食物来源的可用性以及地表和海洋之间有限的交换限制了其形成大量生物圈的潜力。这对未来的任务（如NASA的“蜻蜓”）提出了挑战，如果泰坦上存在生命，它们将需要搜索广阔的区域才能找到证据。该研究强调，泰坦的有机物库存可能不如先前认为的那样有助于其宜居性。

---

## 51. IRIX 6.5.17 源代码

**原文标题**: IRIX 6.5.17 Source Code

**原文链接**: [https://github.com/calmsacibis995/irix-6517-src](https://github.com/calmsacibis995/irix-6517-src)

IRIX 6.5.17 源代码发布简讯

---

## 52. 睡眠至关重要——研究人员正试图弄清原因

**原文标题**: Sleep is essential – researchers are trying to work out why

**原文链接**: [https://www.nature.com/articles/d41586-025-00964-w](https://www.nature.com/articles/d41586-025-00964-w)

睡眠的生物学功能：探索生命的奥秘

本文探讨了睡眠至关重要但仍然神秘的生物学功能。研究人员正在使用光遗传学和聚焦超声等工具来了解睡眠除了提供休息之外的作用。一个关键的研究领域是睡眠如何通过稳态维持大脑的可靠性，通过重置大脑的“临界点”来防止“灾难性遗忘”。睡眠还可以调节基因、代谢和激素。

对果蝇和小鼠的研究表明，睡眠不足会导致肠道中产生有毒水平的活性氧（ROS），这表明睡眠的作用不仅限于大脑。对大鼠的研究表明，与能量代谢和激素受体相关的基因会受到睡眠不足的影响。此外，睡眠质量，尤其是深度睡眠，对于记忆巩固至关重要，而使用粉红噪声进行声学刺激可以增强记忆巩固。

另一种理论侧重于睡眠在通过脑淋巴系统清除大脑中的神经毒素方面的作用，这种清除过程是由深度睡眠期间的去甲肾上腺素振荡促进的。然而，这一理论面临挑战，一些研究表明睡眠期间的大脑清除率会降低。尽管存在持续的争论，突触稳态假说认为睡眠可以恢复大脑细胞在日常活动后的状态。即使是像水螅这样没有中枢神经系统的生物也会表现出类似睡眠的行为，而睡眠不足会扰乱激素释放并增加患心血管疾病的风险，这都突显了睡眠的重要性。

---

## 53. 木星王牌的奇案

**原文标题**: The Curious Case of Jupiter Ace

**原文链接**: [https://nemanjatrifunovic.substack.com/p/the-curious-case-of-jupiter-ace](https://nemanjatrifunovic.substack.com/p/the-curious-case-of-jupiter-ace)

无法访问文章链接。

---

## 54. 展示一下：我做了一个应用，能减少95%以上的播客准备工作量

**原文标题**: Show HN: I built an app that reduces podcast preparation effort by 95% +

**原文链接**: [https://www.podcast-prepper.com/](https://www.podcast-prepper.com/)

PodcastPrepper：一款人工智能工具，于2025年3月30日上线，旨在大幅缩短播客准备时间，声称可为用户节省高达95%的调研精力。该服务提供关于播客嘉宾的详细报告，包括其背景、主要兴趣、职业里程碑、成就、当前项目、在线形象以及建议的采访问题。

该工具旨在缓解耗时的嘉宾调研过程，该过程通常涉及挖掘各种资源、收听过往采访以及安排采访前会议。 PodcastPrepper允许用户专注于创建引人入胜的内容，而不是被准备工作所困扰。

要使用PodcastPrepper，用户只需输入嘉宾的姓名、姓氏和相关背景信息。在24小时内，他们将收到一份详细报告到他们的电子邮件收件箱。虽然由于测试阶段，报告目前在24小时内交付，但人工智能只需3分钟即可生成它们，并计划在未来实现即时交付。

网站提供储蓄计算器，以帮助用户估算使用PodcastPrepper可以额外制作的剧集数量。定价模式为按需付费，目前在测试期间提供 60% 的折扣，每个报告的费用为 4 美元（原价 10 美元）。

---

## 55. TVMC：时变网格压缩

**原文标题**: TVMC: Time-Varying Mesh Compression

**原文链接**: [https://github.com/SINRG-Lab/TVMC](https://github.com/SINRG-Lab/TVMC)

本文介绍了TVMC，一种使用体积跟踪参考网格的时变网格压缩技术，该技术已在2025年ACM MMSys会议上发表。本仓库提供了作者的实现代码和运行说明，支持在Docker环境以及Windows 11或Ubuntu 20.04系统上直接运行。

该过程涉及几个关键步骤：首先，使用C# .NET 7.0应用程序执行ARAP体积跟踪，以跟踪网格序列中体积中心的移动。可以选择应用全局优化来细化这些中心。接下来，基于体积中心位置使用多维尺度分析（MDS）创建参考空间。然后，计算变换以将原始体积中心位置映射到此参考空间。之后，创建无自接触的参考网格，然后将其变形为序列中的每个网格。计算位移场，表示变形的参考网格与原始网格之间的差异。最后，使用Draco压缩参考网格和位移场。

本文档概述了系统要求、依赖项（Python 3.8、numpy、open3d、scikit-learn、scipy、trimesh）以及每个步骤的详细说明，包括构建和运行ARAP体积跟踪应用程序，执行用于MDS、变换计算、位移场生成的Python脚本，以及使用C#应用程序在tvm-editing目录中执行网格变形。它还包括克隆和构建Draco的说明。最后，本文档介绍了如何运行评估脚本来测量压缩性能并生成图表，以重现原始研究论文中的结果。

---

## 56. .localhost 域名

**原文标题**: .localhost Domains

**原文链接**: [https://inclouds.space/localhost-domains](https://inclouds.space/localhost-domains)

查尔斯·张伯伦描述了一种使用自定义`.localhost`域名访问本地运行的Web应用程序的系统，从而避免记忆和输入`localhost:端口`。

该过程包括以下步骤：

1.  每个应用程序都作为launchd守护程序运行，监听唯一的端口。
2.  配置`/etc/hosts`文件，将自定义域名（例如，`appname.localhost`）指向`127.0.0.1`。
3.  配置反向代理Caddy，将来自自定义域名上`127.0.0.1`的流量重定向到应用程序的正确端口。Caddyfile包含反向代理、TLS（内部）以及压缩的配置。

他以一个端口为5050的应用程序为例，`/etc/hosts`条目类似于`127.0.0.1 inclouds.localhost`，并且有一个相应的Caddyfile部分将`inclouds.localhost`反向代理到`localhost:5050`。

他表达了进一步简化此过程的愿望，设想使用单个命令来安装或卸载应用程序，并自动配置必要的文件，而不是手动编辑三个单独的文件。他最后更新提到了来自cristóbal的贡献，该贡献使用dnsmasq来改进设置。

---

## 57. Rails 的设计系统方案

**原文标题**: Design System Options for Rails

**原文链接**: [https://businessclasskit.com/blog/design-system-options-for-rails](https://businessclasskit.com/blog/design-system-options-for-rails)

2025年Rails应用程序设计系统方案探索：作者惊讶地发现这个问题尚未得到良好解决。最初作者在其项目中使用纯Tailwind CSS，但现在重新评估现有的设计系统。

文章考察了几个免费增值或免费选项：

*   **shadcn/ui:** 一个基于React的组件库，需要定制的Rails实现。作者重点介绍了“Rails上的shadcn/ui”，这是一个带有辅助函数和Stimulus控制器的部分实现，并指出了它的潜力但不够完整。

*   **daisyUI:** 一个Tailwind CSS组件库，为UI组件和主题提供快捷方式。其主要缺点是缺乏内置的JavaScript功能。

*   **Flowbite:** 一个Tailwind CSS UI库，提供官方Rails支持和框架独立的JavaScript，无需重新实现。但是，它并非完全开源。

*   **Preline:** 另一个基于Tailwind CSS构建的免费增值UI库，带有自己的框架独立的JavaScript。

*   **RubyUI:** 一个直接为Ruby构建的设计系统，使用Phlex（一种替代视图层）和Tailwind CSS。虽然前景广阔，但它对Phlex的依赖以及与ERB的偏离可能对某些人来说是一个障碍。

结论指出，虽然现有的选择有所改进，但没有明显的赢家。作者重申了使用Tailwind CSS的决定，并建议继续在此基础上构建，无论是使用预制的UI还是自定义的Business Class主题。

---

## 58. 大量的YAML

**原文标题**: That's a Lot of YAML

**原文链接**: [https://noyaml.com/](https://noyaml.com/)

这篇文章，题为《YAML 真多啊》，幽默地批判了 YAML 数据序列化格式，强调了它在 DevOps 环境中潜在的缺陷和不一致性。文章认为，虽然 YAML 被广泛采用，尤其是在 Kubernetes 中，但它带来了许多挑战，可能导致意外错误和调试难题。

作者列举了 YAML 的几个怪癖，例如将 "NO" 解析为布尔值，将以零开头的数字解释为八进制，自动将明显的时间转换为自午夜以来的秒数，以及 8 个字符的 SHA 容易被解释为数字的漏洞。

文章还涉及了与可执行 YAML 相关的安全风险，并展示了不同 CI/CD 提供商之间配置的不一致性。随后，文章列出了一系列链接，指向进一步探讨 YAML 缺点的文章和 Twitter 帖子，包括其冗长、解析不一致以及由于细微语法错误而引入 bug 的可能性。

最后，作者提出了替代的 DevOps 配置方法，如 Nickel、Dhall、CUE 和 Jsonnet。整体语调是讽刺的，作者似乎对 YAML 普遍存在但存在缺陷感到沮丧，最终创建了一个像他们认为 YAML 一样故意不可用的网站。

---

## 59. 魔鬼的形，人心

**原文标题**: "The Form of a Demon and the Heart of a Person"

**原文链接**: [https://publicdomainreview.org/collection/yamauba-and-kintaro/](https://publicdomainreview.org/collection/yamauba-and-kintaro/)

在没有“各种”栏目下题为《魔之形，人之心》的文章内容的情况下，无法提供具体的摘要。然而，仅凭标题，我们可以推测并提供一个*可能的*摘要，概述文章*可能*探讨的主题和论点：

这篇题为《魔之形，人之心》的文章很可能探讨了外表与内在本质的二元性。它可能考察了外表怪异或可怕（“魔之形”），而内心却拥有同情心、共情或道德（“人之心”）等积极品质的角色或概念。

这篇文章可能深入探讨偏见和以貌取人的主题，暗示外表具有欺骗性，真正的性格在于内心。它可能会探索对典型怪物形象的颠覆，挑战读者超越肤浅的判断。

此外，这篇文章可能会分析被认为是怪物所带来的心理影响，以及调和这种认知与内在人性的挣扎。它可能会探讨个人为何采用“恶魔”伪装作为防御机制或对社会压力的回应。

最后，这篇文章可能会考虑成为人类的哲学含义，以及外在形式是否真正决定身份。它很可能会主张同情和理解，鼓励读者考虑那些可能看起来不同甚至可怕的人的内心生活和动机。“各种”内容标签表明，这种探索可能涉及文学分析、哲学论证、社会学观察，或这些的结合。

---

## 60. Show HN: Pledge – 一个轻量级的 Swift 响应式框架 (无 Rx 负担)

**原文标题**: Show HN: Pledge – A Lightweight Reactive Framework for Swift (No Rx Overhead)

**原文链接**: [https://github.com/gokulnair2001/Pledge](https://github.com/gokulnair2001/Pledge)

Pledge：一个轻量级、线程安全的 Swift 响应式编程框架，旨在简化状态管理和事件传播。它提供了一个简洁的观察者模式实现，而没有其他响应式框架的复杂性。主要特性包括线程安全的 observables、基于优先级的通知、可自定义的传递队列、批量更新以及速率限制（节流和防抖）。

该框架围绕着 `PLObservable` 展开，这是一个用于可观察值的线程安全容器。订阅者按优先级顺序收到更改通知，可以选择进行转换和使用传递队列以确保线程安全。速率限制可以控制通知频率。`PLGlobalStore` 为 observables 提供了一个集中的存储库，充当一个轻量级的状态管理解决方案。

Pledge 提供了创建 observables、订阅更改（带有取消订阅选项）、控制传递队列和订阅优先级、修改值（带/不带通知）以及执行批量更新的方法。它还支持通过节流和防抖进行速率限制。

该框架包含函数式操作符，例如 `map`、`flatMap`、`compactMap`、`filter`、`skip`、`distinctUntilChanged`、`merge` 和 `zip`，用于数据转换、过滤和组合。

用法示例展示了使用派生状态进行表单验证、使用枚举进行网络状态管理以表示不同的状态，以及用于防止过度 API 调用的节流搜索。

Pledge 可通过 Swift Package Manager 获取，并使用 MIT 许可证授权。

---

## 61. Emacs 31 将原生支持窗口对换功能

**原文标题**: Native frame transposition coming to Emacs 31

**原文链接**: [https://p.bauherren.ovh/blog/tech/new_window_cmds](https://p.bauherren.ovh/blog/tech/new_window_cmds)

本文详细介绍了将窗口转置功能引入Emacs 31的历程。受向上游贡献原则的启发，作者最初提议将`transpose-frame.el`包集成到Emacs核心中。然而，该包的架构依赖于“复制粘贴”窗口状态，这被证明存在根本缺陷，无法修复，只能完全重写。

一个正确的实现需要修改Emacs的C代码，特别是要在`split-window`操作期间启用窗口对象的“复活”。作者进行了重写，并与Emacs窗口系统代码的维护者Martin Rudalics进行了广泛合作。

经过四个月的工作，Emacs 31现在包含了先前由`transpose-frame.el`提供的功能，以及在`window-x.el`中实现的附加功能。新命令包括：

*   `transpose-window-layout`（对角线反射）
*   `rotate-window-layout-clockwise`和`rotate-window-layout-anticlockwise`
*   `flip-window-layout-horizontally`和`flip-window-layout-vertically`
*   `rotate-windows`和`rotate-windows-back`（循环窗口旋转）

作者鼓励Emacs 31的用户尝试这些命令，并强调它们适用于任何窗口布局。

---

## 62. 揭露SuperNote Nomad E-Ink平板电脑中的零点击RCE漏洞

**原文标题**: Uncovering a 0-Click RCE in the SuperNote Nomad E-Ink Tablet

**原文链接**: [https://www.prizmlabs.io/post/remote-rootkits-uncovering-a-0-click-rce-in-the-supernote-nomad-e-ink-tablet](https://www.prizmlabs.io/post/remote-rootkits-uncovering-a-0-click-rce-in-the-supernote-nomad-e-ink-tablet)

PRIZM Labs发现SuperNote Nomad E-Ink平板电脑存在零点击远程代码执行漏洞(CVE-2025-32409)。攻击者通过利用开放端口(60002)和SuperNoteLauncher应用程序中的缺陷，可在同一网络上完全控制该设备，无需任何用户交互。

该漏洞源于未经身份验证的文件共享功能。研究人员发现，他们可以通过自定义HTTP请求将文件上传到平板电脑的INBOX目录。路径遍历漏洞允许将文件写入其他目录，包括用于固件更新的EXPORT目录。

该漏洞利用了SuperNote设备会自动从EXPORT目录安装固件更新（如果存在有效的“update.zip”文件），以及该设备使用公开的调试密钥来签署固件映像这一事实。但是，文件上传过程会将数字附加到重复文件名，从而阻止直接覆盖“update.zip”。

为了绕过此命名问题，研究人员设计了一种“竞争条件”漏洞。他们首先发送一个小的、虚拟的“update.zip”文件，紧接着发送真实的、后门化的“update.zip”文件。虚拟文件的快速完成会创建并删除初始“update.zip”，从而允许合法的后门映像被复制并正确命名。这会触发在热插拔事件或重新启动时自动安装恶意固件，从而授予攻击者root访问权限。

PRIZM Labs于2024年7月首次向Ratta Software负责任地披露了该漏洞，并在供应商计划发布补丁后，于2024年12月进行了协同披露。

---

## 63. 解析器组合子胜过正则表达式

**原文标题**: Parser Combinators Beat Regexes

**原文链接**: [https://entropicthoughts.com/parser-combinators-beat-regexes](https://entropicthoughts.com/parser-combinators-beat-regexes)

本文论述了在Haskell中使用解析器组合子优于正则表达式(regexes)的理由，即使正则表达式最初看起来更简单。作者使用一个“代码降临节”问题作为示例，展示了基于正则表达式和基于解析器组合子的解决方案，用于从字符串中提取和处理数值数据。

基于正则表达式的解决方案虽然简洁，但因其正则表达式和处理函数之间存在隐式约定而受到批评，缺乏关于捕获组和数据类型的编译时保证。使用`attoparsec`库的解析器组合子解决方案，最初看起来更复杂，但提供了更好的错误处理、类型安全性和编译器检查。

然后，作者解决了问题的第二部分，引入了状态管理（启用/禁用`mul`贡献）。这对正则表达式来说是一个巨大的挑战，因为它们的无状态性。然而，解析器组合子解决方案通过结合状态转换器，优雅地适应了这一新需求，使其成为一个有状态的解析器。

有状态的解析器在更复杂的场景中展示了优于正则表达式的灵活性和可维护性优势。虽然`attoparsec`的回溯在处理状态时可能会带来挑战，但作者指出，这可以通过仔细的解析器设计来解决，甚至可能在库中使用“cut”原语。文章总结说，解析器组合子尽管具有较高的初始学习曲线，但提供了更好的表达性、灵活性和可维护性，尤其是在问题复杂性增加时。附录演示了如何将初始解析器重构为更简洁和applicative的风格，进一步突出了解析器组合子的可组合性。

---

## 64. 对他人小动作的敏感在普通人群中普遍存在。

**原文标题**: Misokinesia, sensitivity to seeing others fidget prevalent in general population

**原文链接**: [https://www.nature.com/articles/s41598-021-96430-4](https://www.nature.com/articles/s41598-021-96430-4)

本文调查了轻动恐惧症（一种对他人烦躁动作敏感的现象）的普遍性和性质。尽管越来越多的人认识到它带来的挑战，但针对该现象的科学研究仍然不足，本研究旨在弥补这一缺憾。

通过对 4100 多名参与者进行的三项研究，研究人员证实了轻动恐惧症敏感性普遍存在于普通人群中，大约影响了三分之一的参与者。第一项研究是一项初步研究，也表明其与恐音症存在共病性。第二项研究（研究 1）改编了恐音症评估问卷 (MpAQ)，创建了轻动恐惧症评估问卷 (MkAQ)，用于衡量与视觉刺激相关的负面情绪程度。它还探讨了轻动恐惧症与视觉注意力表现改变之间的潜在联系。参与者完成了一项干扰物干扰任务和一项反射性注意线索任务。反射性注意线索任务使用了动态或闪光线索，以探索对基于动态的视觉事件的敏感性。最后一项研究评估了非大学人群中的患病率和变异性。

研究结果表明，很大一部分人对他人烦躁的动作很敏感，突显了一种视觉-社交敏感性，值得进一步研究。报告的敏感程度的个体差异表明，负面的社会-情感影响可能会随着年龄的增长而加剧。

---

## 65. 杰拉德·'特霍夫特称量子物理学走错了方向

**原文标题**: Quantum Physics Is on the Wrong Track, Says Gerard 'T Hooft

**原文链接**: [https://www.scientificamerican.com/article/breakthrough-prize-winner-gerard-t-hooft-says-quantum-mechanics-is-nonsense/](https://www.scientificamerican.com/article/breakthrough-prize-winner-gerard-t-hooft-says-quantum-mechanics-is-nonsense/)

本文介绍了对诺贝尔奖得主、理论物理学家杰拉德·特·霍夫特的采访，此前他获得了基础物理学特别突破奖。特·霍夫特讨论了他的职业成就，特别是他对重整化非阿贝尔规范理论的研究，这是粒子物理学标准模型的基石。

在肯定标准模型的成功的同时，特·霍夫特对当前粒子物理学的现状表示不满，认为由于缺乏真正新颖和大胆的想法，进展已经停滞。他认为研究人员对已建立的理论过于满意，需要探索非常规的方法。

特·霍夫特认为，量子力学虽然有用，但可能不是粒子相互作用的最终描述。他提倡一种更合乎逻辑、更“脚踏实地”的方法，强调局域性，并需要理解决定粒子散射的精确机制，而不是仅仅依靠统计概率。他设想的未来是，粒子相互作用可以像两架三角钢琴的碰撞一样可预测，所有潜在的规律都清晰明确。他对未来的突破保持乐观，前提是科学家们愿意挑战传统思维。

---

## 66. 《哥伦比亚演说家》教授十九世纪美国人如何演讲

**原文标题**: The Columbian Orator taught nineteenth-century Americans how to speak

**原文链接**: [https://www.neh.gov/article/columbian-orator-taught-nineteenth-century-americans-how-speak](https://www.neh.gov/article/columbian-orator-taught-nineteenth-century-americans-how-speak)

《哥伦比亚演说家》是19世纪美国一本流行的修辞学教科书，深刻影响了弗雷德里克·道格拉斯和亚伯拉罕·林肯等人物。该书由迦勒·宾厄姆于1797年出版，旨在教导美国人如何有效地讲话，这项技能在一个语言对于个人和政治进步至关重要的社会中备受重视。

道格拉斯，一个花费50美分购买此书的被奴役男孩，认为《哥伦比亚演说家》塑造了他强大的演说能力和废奴主义领袖地位。缺乏正规教育的林肯也学习了这本书，从中汲取了古典和启蒙时代演讲的灵感。

该书的影响力源于其内容的多样性，从古希腊文本到当代政治辩论，让读者接触到各种修辞风格。它还包含促进进步思想的对话，例如“主人与奴隶之间的对话”，该对话倡导废除奴隶制，尽管其所有白人男性贡献者反映了时代的偏见。这段对话引起了道格拉斯的深刻共鸣，表明可以通过论证来挑战奴隶制。

宾厄姆强调了演讲的内容和表达方式，旨在为这个年轻的国家培养出既精致又民主的演讲者。虽然现在有些选段显得过时，但该书的废奴主义立场和对平等的关注导致其在奴隶制危机期间在南方被禁。它的遗产继续被学者和像奥西·戴维斯和亨利·路易斯·盖茨 Jr. 这样的人物所认可，他们强调它在塑造美国身份和话语中的重要性。

---

## 67. 十九世纪日本照片

**原文标题**: Photographs of 19th Century Japan

**原文链接**: [https://cosmographia.substack.com/p/photographs-of-old-japan](https://cosmographia.substack.com/p/photographs-of-old-japan)

以下是Cosmographia Substack上《十九世纪日本照片》一文的摘要：

该文章展示了一组手绘蛋白照片，让人们得以一窥 19 世纪的日本，这些照片主要拍摄于江户时代末期和明治时代初期（大约 1860 年代至 1890 年代）。文章强调了日本在经历了几个世纪的闭关锁国之后，迅速实现现代化并向西方开放的变革时代。

这些照片描绘了日本生活的各个方面，包括武士、艺伎、商人和普通民众的肖像。它们还展示了富士山、寺庙、花园和繁华的城市景观等标志性地标。

文章强调了这些图像作为历史文献的重要性，它们提供了对当时服装、习俗、建筑和社会结构的见解。手绘过程虽然有时理想化，但也为照片增添了独特的审美维度。这些手绘图像通常是为西方消费而制作的，激发了人们的好奇心并塑造了西方对日本的认知。

作者注意到早期摄影的技术挑战以及创作这些照片所涉及的艺术性。文章最后强调了这些照片的价值，它们是了解一个快速变化的社会的窗口，捕捉了日本转型为现代国家过程中转瞬即逝的时刻。

---

## 68. 埃隆·马斯克的狗狗币正接受美国政府问责署审计

**原文标题**: Elon Musk's DOGE Is Getting Audited by GAO

**原文链接**: [https://www.wired.com/story/gao-audit-elon-musk-doge-government-agencies/](https://www.wired.com/story/gao-audit-elon-musk-doge-government-agencies/)

政府问责署(GAO)正在对埃隆·马斯克的“政府效率部”(DOGE)进行审计，调查其在包括劳工部、教育部、国土安全部、卫生与公众服务部、财政部和社会保障管理局等多个联邦机构处理数据的情况。 该审计于三月份启动，重点关注DOGE是否遵守隐私和数据保护法律法规。

人们对DOGE工作人员表示担忧，他们中的许多人与马斯克旗下的公司有联系，但政府经验有限，他们获得了敏感数据的访问权限，并可能整合不同的数据系统，据称是为了打击欺诈和浪费。 GAO正在具体审查DOGE被授予的机构系统访问权限，包括访问类型（读取、写入、执行）、已实施的保障措施以及确保数据保密性、完整性和可用性的流程。

此次审计是由于民主党官员表达的担忧以及众议员Bobby Scott和Richard Neal的正式请求而引发的，此前有报道称DOGE入侵联邦系统。 GAO正在调查DOGE对系统和数据的访问是否适当，数据是否被不当导出，以及未经培训的人员是否正在修改代码或抓取数据。 审计结果预计将在春季末公布，并将公开发布。 关键问题是DOGE的运营是否充分保障了个人数据的安全。

---

## 69. 用Haiku学习编程

**原文标题**: Learning to Program with Haiku

**原文链接**: [https://www.haiku-os.org/development/learning_to_program_with_haiku](https://www.haiku-os.org/development/learning_to_program_with_haiku)

本网页是DarkWyrm创建的题为“用Haiku学习编程”的课程集合，旨在向初学者教授编程，特别是针对Haiku操作系统。这些课程始于2010年，根据知识共享许可协议免费提供，仅供非商业用途。

该系列涵盖了广泛的主题，从基本编程概念（如数据类型、屏幕打印、循环、条件语句、数组、字符串和指针）开始，然后逐步发展到更高级的主题，包括内存管理、二进制数学、命令行交互、数据结构和使用C++的面向对象编程（OOP）。该系列的后半部分侧重于Haiku API、GUI编程、消息传递、菜单、列表框、资源和存储套件。

这些课程提供可下载的PDF文件，通常包括源代码示例。它们还包含单元复习和复习答案，以加强学习。该系列最终以开发一个名为“HaikuFortune”的实用Haiku应用程序告终，涵盖了GUI设计、可用性、资源集成、许可和用于分发的打包等方面。作者计划创建一个后续系列，用于介绍更高级的Haiku特定编码主题。

---

## 70. Apache ECharts

**原文标题**: Apache ECharts

**原文链接**: [https://echarts.apache.org/en/index.html](https://echarts.apache.org/en/index.html)

Apache ECharts是一个声明式的框架，旨在快速创建基于Web的可视化图表。 请在研究、开发、产品、报告、新闻、书籍、演示文稿、教学和专利等各种项目中使用ECharts时，引用“Visual Informatics, 2018”论文。 本文主要介绍了ECharts，并要求在使用该库时进行适当的署名。它强调了该框架的目的：简化Web环境中的可视化图表创建。

---

## 71. 搜索嵌套

**原文标题**: Searchception

**原文链接**: [https://blog.mojeek.com/2025/04/searchception.html](https://blog.mojeek.com/2025/04/searchception.html)

文章《搜索欺骗》认为，浏览器和搜索引擎的融合，以谷歌Chrome浏览器的多功能地址栏为代表，巧妙地操控用户依赖搜索引擎进行导航，即使他们知道确切的网站地址。这种被称为“搜索欺骗”的做法，通过增加广告收入和数据收集，同时削弱用户自主性，使大型科技公司受益。

作者详细描述了几种促成“搜索欺骗”的机制，包括：多功能地址栏将URL和搜索查询同等对待，预测搜索优先显示搜索词，默认搜索引擎锁定，搜索的深度操作系统集成，偏好搜索建议的移动设计，以及视觉模仿模糊了搜索结果和目标内容之间的界限。

这种趋势的后果包括用户忘记URL、假设第一个搜索结果总是最好的、越来越依赖过滤和广告驱动的内容，以及通过提供更多数据而成为产品。

文章建议通过以下方式摆脱“搜索欺骗”：使用带有独立URL和搜索栏的浏览器，有意识地使用地址栏进行直接导航，向他人普及这种现象，以及使用“!Bangs”或搜索选择扩展程序。作者总结说，理解“搜索欺骗”可以让用户重新获得控制权，并按照自己的意愿探索开放的网络。

---

## 72. Show HN: 我用 Mermaidjs 做了一个生成故事关系的应用

**原文标题**: Show HN: I built an app to generate story relationships using Mermaidjs

**原文链接**: [https://github.com/herol3oy/austen](https://github.com/herol3oy/austen)

Austen 是一个由 AI 驱动的 Web 应用程序，使用 Angular (基于 Analogjs) 构建，可利用 Mermaidjs 从书籍中生成人物关系图。用户可以通过 Open Library API 搜索书籍，Austen 则利用 AI (DeepSeek 和 OpenAI) 分析人物及其关系，自动生成 Mermaid 图表以可视化这些连接。

主要功能包括保存、下载 (SVG 或 PNG 格式) 和管理生成的图表，以及公开分享或私密保存的选项。用户还可以发现其他人公开分享的图表。

该应用程序使用包括 Angular、Analog、TypeScript、Supabase、Cloudflare Pages、Angular Material 和 Mermaid 在内的技术栈构建。Supabase 用于数据存储 (图表、用户数据) 和身份验证。提供的说明详细介绍了如何克隆存储库、安装依赖项、设置包含 API 密钥的环境变量、配置 Supabase，以及运行开发服务器或构建生产版本。

计划的未来改进包括实现图表的点赞/取消点赞功能，以及发现页面的“加载更多”功能。应用程序的 UI 包括用于生成图表的首页、“我的图表”页面，以及用于浏览公共图表的“发现”页面。

---

## 73. 你认为在亚洲生产一双耐克鞋的成本是多少？

**原文标题**: How much do you think it costs to make a pair of Nike shoes in Asia?

**原文链接**: [https://twitter.com/dieworkwear/status/1909741170953273353](https://twitter.com/dieworkwear/status/1909741170953273353)

提供的文本并非关于在亚洲生产耐克鞋成本的文章，而是来自 X (原 Twitter) 的一段代码片段，表明 JavaScript 已禁用，平台无法正常运行。它提供了帮助中心、服务条款、隐私政策、Cookie 政策、版本说明和广告信息的链接，并声明 X Corp 拥有内容版权，版权年份为 2025 年。

因此，所提供的文本中没有关于在亚洲生产耐克鞋成本的信息可供总结。这仅仅是一个网站功能无法正常工作的通知。

---

## 74. 骰子与队列

**原文标题**: Dice and Queues

**原文链接**: [https://justincartwright.com/2025/02/25/dice-and-queues.html](https://justincartwright.com/2025/02/25/dice-and-queues.html)

本文通过一个基于掷骰子的仿真来探讨排队论，旨在直观地理解队列如何在不同的到达率和离开率下运作。作者强调了利用率（ρ）的重要性，它表示服务器繁忙的时间百分比。虽然低利用率会导致小队列，但本文强调，当利用率接近 100% 时，队列大小会急剧增加，当到达率等于或超过服务率时，可能会达到无穷大。

该仿真模拟了一个 M/D/1 队列，其中到达遵循泊松分布（通过每分钟掷骰子 60 次来近似），并且服务率是确定的。作者演示了如何使用 Python 函数生成随机到达，并计算每分钟的队列大小变化。本文将仿真结果与 M/D/1 队列中平均队列大小的理论公式进行比较，观察到定性的一致性：平均队列大小随着利用率接近 100% 而急剧增加。

文章测试了几个具有不同到达率和服务率的场景，说明了在不同利用率因子下队列的行为。当到达率超过服务率时，队列增长迅速。相反，当服务率较高时，队列会缩小并在零附近波动。作者还指出，即使在接近 100% 的利用率下，由于到达的内在变化，队列大小也会出现显着波动。结论强调了到达变化和队列长度的非负性对平均队列大小的影响。

---

## 75. 俄罗斯悖论：教育程度如此之高，人力资本却如此之低

**原文标题**: The Russian Paradox: So Much Education, So Little Human Capital

**原文链接**: [https://theamericanenterprise.com/the-russian-paradox-so-much-education-so-little-human-capital/](https://theamericanenterprise.com/the-russian-paradox-so-much-education-so-little-human-capital/)

尼古拉斯·埃伯斯塔特的文章《俄罗斯悖论：教育程度高，人力资本少》突显了俄罗斯高教育水平与其糟糕的健康状况和有限的知识生产之间存在的巨大脱节。

尽管俄罗斯的平均受教育年限与发达的欧洲国家相当，但其预期寿命却低得惊人，与世界上一些最不发达的国家相当。这归因于心血管疾病和损伤造成的高死亡率，这违背了教育与健康之间的典型联系。

此外，俄罗斯在知识生产方面表现不佳，以专利申请衡量。尽管拥有一支庞大且受过高等教育的劳动力队伍，但其专利产出明显低于其他发达国家，甚至一些发展中国家。同样，其服务部门出口（衡量人力资本贸易的标准）相对于其教育水平而言也很薄弱。

埃伯斯塔特强调，社会科学家需要了解为什么俄罗斯对教育的大量投资在健康和知识生产方面产生的回报如此微薄。他还认为，这种悖论应为国际安全评估提供信息，告诫人们不要因为俄罗斯的高教育水平而高估其经济和战略潜力，因为其存在潜在的局限性。自入侵乌克兰以来，技术精湛的年轻人的“人才流失”进一步加剧了这个问题。理解这一悖论对于避免低估和高估俄罗斯在不断变化的全球格局中的能力至关重要。

---

## 76. 中微子最大可能质量进一步缩小

**原文标题**: Neutrinos' maximum possible mass shrinks further

**原文链接**: [https://www.sciencenews.org/article/neutrino-mass-shrinks-katrin-electron](https://www.sciencenews.org/article/neutrino-mass-shrinks-katrin-electron)

卡尔斯鲁厄氚中微子实验(KATRIN)最新结果进一步缩小了中微子的可能质量范围，表明它们比之前认为的还要微小。该实验确定中微子的质量小于0.45电子伏特，几乎是KATRIN之前上限的一半。

中微子是独特的，因为它们的质量，一种基本粒子属性，是未知的。 它们极其轻，不到电子质量的百万分之一，因此理解它们的质量是粒子物理学中的一个主要难题。

KATRIN位于德国，研究氚放射性衰变过程中产生的电子反中微子。通过观察这些衰变中发射的电子的能量（分析了3600万个电子），研究人员可以推断出中微子的质量，因为它限制了电子可以拥有的最大能量。

KATRIN将继续收集数据到2025年底，并计划分析现有的、未分析的数据，以进一步约束中微子的可能质量。

虽然宇宙学观测也对中微子的质量进行了限制，但这些估计依赖于对宇宙的假设。KATRIN的发现独立于这些假设，使其成为对中微子质量的直接测量。

---

## 77. 大学生如何使用Claude

**原文标题**: How University Students Use Claude

**原文链接**: [https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude](https://www.anthropic.com/news/anthropic-education-report-how-university-students-use-claude)

我能够访问互联网，并可以总结来自提供的URL的文章。

**“大学生如何使用Claude”摘要:**

Anthropic报告详细介绍了大学生如何使用Claude人工智能助手。研究表明，学生主要使用Claude来**辅助学习过程，而不是直接作弊**。常见的用例包括**总结研究论文、为作业集思广益、改进写作以及理解复杂的概念**。学生们欣赏Claude**以不同的风格和详细程度提供解释**的能力，使他们能够更有效地掌握具有挑战性的材料。

该报告强调了学生对人工智能伦理使用的细致理解。尽管他们认识到滥用的可能性，但他们主要将Claude视为一种**增强学习和生产力的工具**，而不是取代他们自己的努力。许多学生积极尝试通过释义Claude的输出并正确引用其辅助来**避免抄袭**。

该研究还探讨了担忧和局限性。学生偶尔会遇到来自Claude的**不准确或有偏见的信息**，这突显了批判性思维和事实核查的必要性。该报告表明，将**人工智能素养纳入教育课程**非常重要，从而教导学生如何负责任和有效地使用这些工具。

总而言之，该报告描绘了一幅大学生谨慎地将Claude视为有价值的学习伙伴的图景，重点是补充他们的学习并加深对课程材料的理解。它呼吁继续研究和教育，以指导人工智能在高等教育中的伦理和有效整合。

---

## 78. FDA裁员辞职威胁基本运营，撤回远程办公政策

**原文标题**: FDA reverses on telework after layoffs and resignations threaten basic operation

**原文链接**: [https://federalnewsnetwork.com/workforce/2025/04/fda-reverses-course-on-telework-after-layoffs-and-resignations-threaten-basic-operations/](https://federalnewsnetwork.com/workforce/2025/04/fda-reverses-course-on-telework-after-layoffs-and-resignations-threaten-basic-operations/)

FDA因裁员和辞职导致劳动力锐减，威胁机构基本运作而推翻远程办公政策。

---

## 79. 从零开始构建Y组合子

**原文标题**: Baking the Y Combinator from Scratch

**原文链接**: [https://the-nerve-blog.ghost.io/baking-the-y-combinator-from-scratch-part-1/](https://the-nerve-blog.ghost.io/baking-the-y-combinator-from-scratch-part-1/)

从零开始构建 Y 组合子
        
本文“从零开始构建 Y 组合子”旨在全面解释 Y 组合子，详细介绍其目的、机制和历史背景。它探讨了 Y 组合子是什么、为什么它看起来是这样、它的用途是什么，以及为什么它仍然具有相关性等问题。

Y 组合子是一种数学结构，用于在缺乏显式自引用的函数式语言中实现递归。文章认为，理解 Y 组合子的最佳方式是关注它如何产生不动点。函数 `f` 的不动点是指一个值 `x`，使得 `f(x) = x`。 Y 组合子，也称为不动点组合子，将一个函数作为输入并返回其不动点。

文章详细阐述了为什么在 lambda 演算中，由于缺乏命名函数和无法创建无限大项，一个简单的自引用 Y 实现会失败。然后，它引导读者了解 Omega 组合子（一个自我复制的项）的发现过程，并将其用作推导出 Y 组合子的垫脚石。

最终的 Y 组合子表示为：`Y = λf. (λx. f(x x)) (λx. f(x x))`。

文章还提供了历史背景，解释说 Y 组合子的创建者 Haskell Curry 可能是在形式主义和形式系统（20 世纪早期数学领域的重要组成部分）的框架内看待它的。 lambda 演算以其最小性和对符号操作的关注，为函数式编程语言奠定了基础。

---

## 80. GPD Pocket 4 扬声器 DSP：配置 PipeWire 以改善笔记本电脑扬声器音质

**原文标题**: GPD Pocket 4 Speaker DSP: Configuring PipeWire so laptop speakers sound better

**原文链接**: [https://kittenlabs.de/blog/2025/04/06/gpd-pocket-4-speaker-dsp/](https://kittenlabs.de/blog/2025/04/06/gpd-pocket-4-speaker-dsp/)

本文详细介绍了如何使用 PipeWire 和数字信号处理 (DSP) 改进 GPD Pocket 4 笔记本电脑扬声器的音质。作者 Manawyrm 的灵感来自于 Asahi Linux 等项目使用的 DSP 技术，这些技术旨在优化 Apple Silicon MacBook 上的音频。

该方法包括使用 Room EQ Wizard (REW) 测量内置扬声器的频率和脉冲响应。测量结果显示在 4kHz 左右存在一个明显的峰值，这导致声音刺耳和失真。

为了纠正这个问题，作者在 REW 中创建了一个滤波器曲线，以补偿倾斜的低音响应和 4kHz 的峰值。然后，将此曲线反转并导出为 .wav 脉冲响应文件。此 .wav 文件是 PipeWire 中卷积 DSP 滤波器的关键部分。

之后，作者从 14 英寸 MacBook Pro（从 Asahi Linux 的工作中获得）改编了一个 DSP 配置，用于 GPD Pocket 4 的立体声扬声器，并将 MacBook 的脉冲响应替换为新生成的 .wav 文件。本文链接到一个 GitHub 存储库和一个 AUR 包 ("gpd-pocket-4-pipewire")，其中包含用于复制此设置的最终 PipeWire 配置，以及用于测量的 REW 软件。目标是使用卷积来校正扬声器的频率响应并提高整体音质。

---

## 81. Show HN: Obelisk - 基于 WASM 的确定性工作流引擎

**原文标题**: Show HN: Obelisk – a WASM-based deterministic workflow engine

**原文链接**: [https://obeli.sk/](https://obeli.sk/)

Obelisk：基于 Rust 和 WebAssembly 组件模型的全新开源确定性工作流引擎，其核心价值在于为工作流增加弹性和确定性。

主要特性和优势包括：

*   **架构简单：** 单进程运行时，使用 SQLite 数据库，最大限度地降低基础设施复杂性。
*   **WASM 驱动：** 利用 WASM 实现互操作性、确定性执行、隔离和安全性。工作流使用真实代码编写（而非 YAML）。
*   **确定性工作流：** 提供结构化并发，简化错误处理和清理，并对参数、步骤和结果进行完整日志记录，以确保崩溃恢复能力和可重放性。
*   **安全的 WASI 活动：** 安全的 HTTP 客户端，具有限制和跟踪功能，并在超时或失败时重试活动。
*   **WASI Webhooks：** 支持通过 Webhooks、CLI、gRPC 或 Web UI 触发工作流和活动。
*   **开源：** 采用 AGPL 许可，源代码可在 GitHub 上获取。

本质上，Obelisk 旨在提供一个健壮且可靠的平台来执行工作流，通过确保确定性执行、崩溃恢复和与传统工作流引擎相比更简化的架构来实现。开发者邀请用户通过邮件列表关注他们的进展。

---

## 82. Firebase 工作室

**原文标题**: Firebase Studio

**原文链接**: [https://firebase.studio](https://firebase.studio)

Firebase Studio：利用生成式AI加速应用开发的新环境

Firebase Studio是一个旨在通过利用生成式AI和基于浏览器的workspace加速应用开发的新环境。它允许开发者从任何地方快速构建和部署应用程序，可以使用来自GitHub等平台的现有存储库，也可以借助App原型代理创建新的存储库。该代理使用自然语言、模型和绘图工具来创建应用程序，并为流行的框架提供模板。

一个关键特性是Gemini在Firebase中的集成，为编码、调试、测试和文档编写等任务提供AI驱动的辅助。新的Gemini代码助手代理将进一步简化开发流程。

Firebase Studio还提供端到端测试能力，可以访问来自Open VSX Registry的扩展程序，用于API和后端测试。内置的Web预览和Android模拟器允许开发者查看他们的应用程序对用户来说是什么样子。通过一键发布到Firebase App Hosting，部署得以简化，监控工具提供了使用情况和行为洞察。应用程序还可以部署到Firebase Hosting、Cloud Run或自定义基础设施。

Firebase Studio目前处于预览阶段，免费提供3个workspace，Google开发者计划成员最多可获得30个workspace。该平台旨在帮助开发者利用生成式AI进行创新，更高效地构建API、后端、Web和移动应用程序以及自定义代理。

---

## 83. 展示HN：我搭建了一个AI驱动的系统，帮助你30天学会任何技能

**原文标题**: Show HN: I Built an AI-Powered System to Help You Learn Any Skill in 30 Days

**原文链接**: [https://30daysmethod.com/](https://30daysmethod.com/)

"Show HN"：30天速成法Notion模板，助您一月内掌握任何技能。该系统利用人工智能根据用户选择的技能和经验水平创建个性化学习计划。

此模板借鉴了“原子习惯”中的1%法则、改善哲理（Kaizen）、习惯养成原则（Maltz规则）、刻意练习（Ericsson的研究）以及基于连续性的激励（“不要打破链条”）。它旨在提供结构、跟踪进度，并通过将学习分解为可管理的步骤来消除压力。

该系统不提供完整的课程，而是提供路线图和指导，指导用户专注于何处以及练习什么。它强调纪律和日常练习是成功的关键组成部分。提供的技能示例包括语言学习、设计、摄影、绘画、音乐和瑜伽。

帖子中包含许多据称是用户的评价，赞扬了该模板的直观性、可定制性以及在提高注意力、效率和纪律方面的有效性。创建者强调该模板能够构建“大脑肌肉”，培养决心，并最终通过持续学习带来个人改变和成功。

---

## 84. 减少流感和单纯疱疹病毒传播的抗病毒口香糖

**原文标题**: Antiviral chewing gum to reduce influenza and herpes simplex virus transmission

**原文链接**: [https://penntoday.upenn.edu/news/penn-dental-antiviral-chewing-gum-reduce-influenza-and-herpes-simplex-virus-transmission](https://penntoday.upenn.edu/news/penn-dental-antiviral-chewing-gum-reduce-influenza-and-herpes-simplex-virus-transmission)

本文重点介绍了塞内加尔的达喀尔绿化带项目，这是一项雄心勃勃的计划，旨在应对达喀尔及其周边地区的荒漠化，并促进可持续的城市发展。该项目力求创建一个生态基础设施网络，以解决环境问题并改善城市生活。

宾夕法尼亚大学魏茨曼设计学院的学生在David Gouverneur和Ellen Neises以及博士候选人Rob Levinthal的带领下参与了该项目，并通过课程作业进行。这些课程包括前往达喀尔的实地考察，学生们在那里亲身参与了该项目。

他们工作的最终成果是学生们展示了他们对绿化带特定区域的愿景和方案，为这项大规模生态和基础设施建设的整体设计和实施做出了贡献。本文强调了该项目将该地区从类似沙漠的环境转变为可持续绿洲的重要意义，展示了宾夕法尼亚大学在萨赫勒地区全球绿化工作中的参与。

---

## 85. 你的手机会在2025年把你拒之美国境外吗？

**原文标题**: Can Your Phone Ban You from the U.S. in 2025?

**原文链接**: [https://ctcnews.ca/2025/04/09/can-your-phone-ban-you-from-the-u-s/](https://ctcnews.ca/2025/04/09/can-your-phone-ban-you-from-the-u-s/)

2025年4月，加拿大政府发布旅行警告，提醒公民在美国边境面临更严格的审查。美国海关与边境保护局（CBP）官员有权在无需理由的情况下搜查智能手机和笔记本电脑等电子设备，这源于凌驾于第四修正案保护之上的“边境搜查例外”条款。拒绝配合可能导致设备被没收、延误或被拒绝入境。

该警告强调了个人数据泄露的风险，并引用了Rasha Alawieh博士的案例，她因边境官员在她手机上发现已删除的照片而被驱逐出境。为降低风险，建议加拿大人在过境前将设备调至飞行模式，以防止意外数据下载。

该政策引发了国家安全和隐私倡导者之间的辩论。美国当局辩称，此举对于打击数字威胁是必要的，而公民自由团体则批评其为严重越权行为。最高法院已站在政府一边，赋予CBP广泛的搜查权。

该警告为经常前往美国旅游、学习和商务的加拿大人敲响了警钟。它也影响着任何进入该国的非美国公民。专家建议备份数据、携带“干净”的设备，并承认非公民在边境享有的权利有限。该警告引发了人们对美国公民出国旅行可能面临的对等审查的质疑，并预示着国际旅行中安全与隐私之间日益紧张的全球局势。

---

## 86. 男人的怪异收藏启发了现代博物馆：珍奇柜

**原文标题**: Men's Weird Collections Inspired the Modern Museum: Cabinets of Curiosities

**原文链接**: [https://worldhistory.substack.com/p/how-strange-mens-weird-collections](https://worldhistory.substack.com/p/how-strange-mens-weird-collections)

无法访问文章链接。

---

## 87. 欺骗宝可梦交易

**原文标题**: Spoofing a Pokemon Trade

**原文链接**: [https://blog.nitwhiz.xyz/posts/002-pokemon-red-trade/](https://blog.nitwhiz.xyz/posts/002-pokemon-red-trade/)

使用模拟器在《精灵宝可梦 红》中欺骗宝可梦交换的方法

这篇文章解释了如何使用模拟器在《精灵宝可梦 红》中欺骗宝可梦交换。作者详细介绍了他们的设置，包括使用 SameBoy 模拟器和一个 Unix 套接字来通过 Go 程序与其通信。

该项目的核心在于拦截和操纵模拟器在交换过程中交换的串行数据。文章概述了 Game Boy 如何处理串行数据，以及如何配置 SameBoy 来接入串行传输过程。作者在 SameBoy 中实现了自定义回调，以通过套接字发送和接收作为字节的串行数据。

文章随后深入探讨了宝可梦交换协议，重点介绍了关键步骤，如建立领导者/跟随者状态、交换随机种子，以及最重要的是交换包含宝可梦队伍数据的“交换块”。文章使用 Go 结构详细描述了交换块的结构，包括宝可梦数据、训练师名称和昵称。

一个重要的挑战是 Game Boy 对 0xFE 字节的敏感性，这是使用“补丁列表”处理的。作者解释了补丁列表如何识别交换块中预期出现 0xFE 并用 0xFF 替换的位置。文章提供了使用这些列表解析、编组和修补交换块的代码片段。

最后，文章概述了选择宝可梦和接受交换的过程，并附带了一个协议转储，说明了数据流。最终结果是一个系统，作者可以操纵交换块数据，将任何想要的宝可梦注入到交换中。

---

## 88. 日本乡下小镇中年男子交易卡片走红

**原文标题**: Middle-aged man trading cards go viral in rural Japan town

**原文链接**: [https://www.tokyoweekender.com/entertainment/middle-aged-man-trading-cards-go-viral-in-japan/](https://www.tokyoweekender.com/entertainment/middle-aged-man-trading-cards-go-viral-in-japan/)

在日本乡村小镇河原，一种以当地中年男子（“叔叔”）为主角的独特集换式卡牌游戏（TCG）在儿童中风靡一时，超越了宝可梦卡牌的受欢迎程度。“叔叔卡牌游戏”包含47张卡牌（截至2025年3月18日），其中28张描绘了来自才藤庄社区的当地男子，并根据他们在现实生活中的贡献赋予了独特的属性和能力。例如，本田先生，一位前消防队队长，拥有一张“防火墙”卡牌；以及竹下先生，一位荞麦面制作指导员。

该游戏由才藤庄社区委员会秘书长宫原绘里创建，旨在加强儿童与老一辈人之间的联系。自推出以来，这款卡牌游戏成功地鼓励孩子们参加当地活动和做志愿者，据说参与人数增加了一倍。

最初设计用于收藏，孩子们很快将叔叔卡牌游戏变成了一种竞技游戏。引入了新的规则，可以根据角色的技能和能力进行战斗。卡牌的稀有度与现实世界的贡献相关联，积极参与的叔叔更有可能获得令人垂涎的“闪卡”版本。这些手工制作的卡牌仅在才藤庄社区中心出售，3张100日元，6张500日元，其中包括一张闪卡。这款游戏的流行反映了年轻人对当地社区人物的重新认识和欣赏。

---

## 89. 长篇创意写作大语言模型基准

**原文标题**: LLM Benchmark for 'Longform Creative Writing'

**原文链接**: [https://eqbench.com/creative_writing_longform.html](https://eqbench.com/creative_writing_longform.html)

EQ-Bench长篇创意写作排行榜：评估大型语言模型（LLM）在短篇小说和中篇小说创作方面的能力，是更广泛的EQ-Bench基准测试套件中的创意写作基准的第三版（v3），该套件旨在测试LLM的情感智能和其他能力。

该基准评估模型从最简提示中进行头脑风暴和规划叙事、反思和修改计划，以及在8轮约1000字的长篇叙事中写作的能力。 模型使用Openrouter进行评估，并采用特定的温度和概率设置。

评估由评判LLM（Claude Sonnet 3.7）使用评分标准进行，重点关注以下指标：

*   **长度：** 平均章节长度（字符）。
*   **冗余得分：** 过度使用的LLM特定词语/短语的频率（越低越好）。
*   **重复度指标：** 衡量多个任务中单词/短语的重复情况（越低越好）。
*   **衰退度：** 可视化8个章节的质量趋势，表明模型的写作质量是否随着时间推移而下降。 表示为迷你图，衰退度得分是趋势线梯度的绝对值。
*   **得分：** 由评判LLM分配的总体最终评分，范围为0-100（越高越好）。

该排行榜根据这些指标对不同的LLM进行排名，从而可以比较和改进长篇创意写作能力。“冗余概况”也可用于可视化和理解过度使用的特定类型的单词和短语。

---

## 90. 基于 Rockchip RK3399 ARM SoC 的三星 Chromebook Plus (Kevin) 上的 Linux (2024)

**原文标题**: Linux on Samsung Chromebook Plus (Kevin) with Rockchip RK3399 ARM SoC (2024)

**原文链接**: [https://www.devkitsune.net/blog/wordpress/2024/01/04/linux-on-arm-chromebooks/](https://www.devkitsune.net/blog/wordpress/2024/01/04/linux-on-arm-chromebooks/)

本文详细介绍了作者在一款搭载瑞芯微RK3399 ARM SoC的三星Chromebook Plus (Kevin) 上安装Linux的经验。作者尝试了三种专门为ARM Chromebook设计的Linux发行版：Arch Linux ARM、PrawnOS和Cadmium。

Arch Linux ARM最初看起来很有希望，因为它有专门针对该Chromebook型号的文档，但作者遇到了需要手动干预的WiFi问题。解决WiFi问题、安装XFCE并升级系统后，安装失败，无法启动。

PrawnOS是一个基于Debian的发行版，专注于自由和开源软件(FOSS)，但事实证明它过于严格。它对FOSS的强调意味着像WiFi这样的基本功能被有意省略，这使得它对作者的需求来说不切实际。尝试添加WiFi支持导致了与Arch类似的启动失败。

最终，另一个基于Debian的发行版Cadmium被证明是最成功的。尽管Cadmium不再积极维护，但它可以“开箱即用”，包括WiFi和手写笔支持。作者最初使用了Cadmium的默认桌面环境Sway，但最终切换到了XFCE。他们在使用Firefox时遇到了一些小的视觉故障，但发现Cadmium足够稳定，可以进行轻量级的3D游戏和使用手写笔进行笔记。作者的结论是，Cadmium是重振旧ARM Chromebook的最佳选择。

---

## 91. Show HN: DrawDB – 开源在线数据库图表编辑器（复古风）

**原文标题**: Show HN: DrawDB – open-source online database diagram editor (a retro)

**原文链接**: [https://www.drawdb.app/](https://www.drawdb.app/)

这个"Show HN"帖子介绍 DrawDB，一个开源的在线数据库图表编辑器。 该工具允许用户以可视化方式创建数据库图表，并根据这些图表生成 SQL 代码。 帖子强调 DrawDB 是一个 Web 应用程序，需要 JavaScript 才能运行。 本质上，它是一个通过提供可视化界面和自动化 SQL 生成过程来简化数据库设计的工具。

---

## 92. 时空数据库

**原文标题**: SpacetimeDB

**原文链接**: [https://spacetimedb.com/](https://spacetimedb.com/)

SpacetimeDB 是一种数据库，因其能够存储应用程序的完整事务历史而得名。它的核心特性是将数据库回溯到过去的任何时间点，并从该时刻重放事务的能力。这种固有的“时间旅行”功能可以轻松地进行重放，并简化调试或恢复过程。该数据库本质上提供了所有更改的完整审计跟踪，使开发人员能够准确地了解数据库是如何达到当前状态的。

---

## 93. 减少屏幕时间指南

**原文标题**: A guide to reduce screen time

**原文链接**: [https://speedbumpapp.com/en/blog/how-to-reduce-screen-time/](https://speedbumpapp.com/en/blog/how-to-reduce-screen-time/)

如何减少屏幕时间：终极指南

本文“如何减少屏幕时间：终极指南”提供了一种全面的方法来减少手机使用，将重点从限制转向积极参与其他活动。它强调理解过度使用屏幕时间的根本原因，例如无聊或焦虑，并承认偶尔需要在线应对机制。

该指南提供了实用的工具和策略，包括iOS（屏幕使用时间）和Android（数字健康）的内置功能，用于使用情况跟踪和应用限制。它还回顾了第三方应用程序，如One Sec、Opal、SpeedBump、Clearspace、ScreenZen、Focus Plant和Forest，突出了它们在解决冲动、数据驱动跟踪、沉迷浏览负面新闻和专注等特定问题方面的独特优势。

除了应用程序之外，本文还推荐了各种技巧，例如管理通知、组织应用程序布局、使用灰度模式、创建无屏幕区域、订阅新闻摘要以及选择报纸和笔记本等模拟替代品。它建议利用TikTok和Instagram等特定应用程序中的内置屏幕使用时间选项，使用浏览器而不是专用应用程序，并拥抱无聊来激发创造力。作为最后的手段，它提到了卸载应用程序或使用功能手机。

作者最后敦促读者慢慢开始，尝试不同的策略，并保持坚持，承认社交媒体平台的成瘾性。最初的几周将充满挑战，但持续实施这些策略将带来更健康的习惯和更高的幸福感。最后，本文回答了有关桌面计时器使用、通知和健康屏幕时间限制的常见问题解答。

---

## 94. 我认识的最优秀的程序员

**原文标题**: The best programmers I know

**原文链接**: [https://endler.dev/2025/best-programmers/](https://endler.dev/2025/best-programmers/)

本文概述了作者根据其职业生涯的观察，认为卓越程序员所具备的特质。作者强调**深入理解工具**的重要性，即通过阅读文档，了解工具的历史、局限性和生态系统，而不是依赖在线论坛或大型语言模型的快速修复。

主要特质包括：

*   **问题解决能力**: 掌握将复杂问题分解为可管理步骤的艺术。
*   **阅读错误信息**: 透彻分析错误信息，从中推断信息并独立解决问题。
*   **务实方法**: 乐于亲身实践代码，学习新技能，并在需要的地方做出贡献。
*   **帮助他人**: 分享知识并为同事提供支持。
*   **写作**: 通过写作进行有效沟通，反映清晰的思维和结构化的编码风格。
*   **持续学习**: 持续更新新技术，批判性地评估它们，并避免停滞不前。
*   **无我**: 平等地对待所有同事，无论地位如何，并向所有人学习。
*   **建立声誉**: 通过分享您的工作来产生影响，例如，为开源软件做贡献，撰写书籍或交付关键服务。
*   **耐心**: 对计算机、人和自己保持耐心，同时保持专注和投入。
*   **永不责怪电脑**: 理解每个问题都有逻辑上的解释，即使在调试“不稳定”的代码时也是如此。
*   **承认无知**: 坦然地说“我不知道”，并将其作为学习的机会。
*   **避免猜测**: 拒绝做出假设，并始终寻求透彻的理解。
*   **简洁**: 优先考虑简单、可维护的代码，而不是过于聪明的解决方案。

作者总结说，这些品质不是竞争，而是一种持续改进的指南，并强调成为卓越程序员的道路上没有捷径。

---

## 95. 蓝盾数据泄露 (Google Ads)

**原文标题**: Blue Shield Data Breach (Google Ads)

**原文链接**: [https://news.blueshieldca.com/notice-of-data-breach](https://news.blueshieldca.com/notice-of-data-breach)

加州蓝盾宣布潜在数据泄露，影响2021年4月至2024年1月期间在蓝盾网站上访问信息的会员。此次泄露是由于 Google Analytics 配置不当，导致会员数据（可能包括受保护的健康信息）与 Google Ads 共享。

共享的信息可能包括保险计划详情、城市、邮政编码、性别、家庭规模、蓝盾标识符、医疗理赔详情（服务日期、提供者、患者姓名和财务责任）以及“查找医生”搜索条件。重要的是，社会安全号码、驾驶执照号码和财务信息未被泄露。

蓝盾于 2025 年 2 月 11 日发现了该问题，并于 2024 年 1 月切断了 Google Analytics 与 Google Ads 之间的连接。他们认为 Google 可能已将该数据用于定向广告活动，但尚未共享该信息。蓝盾正在审查其安全协议，以防止未来发生类似事件。

建议会员查看账户对账单是否存在可疑活动，并将任何疑虑报告给执法部门。蓝盾建议从三大信用报告机构获取免费信用报告，并考虑在其信用报告上设置欺诈警报。如有疑问，会员可拨打蓝盾免费帮助热线 1-833-918-5064。

---

## 96. 我女儿准备好拥有她的第一部智能手机了，但我还没准备好给她。

**原文标题**: My Daughter Is Ready for Her First Smartphone. I'm Not Ready to Give It to Her

**原文链接**: [https://www.wsj.com/tech/personal-tech/my-daughter-is-ready-for-her-first-smartphone-im-not-ready-to-give-it-to-her-fb038e6f](https://www.wsj.com/tech/personal-tech/my-daughter-is-ready-for-her-first-smartphone-im-not-ready-to-give-it-to-her-fb038e6f)

无法访问文章链接。

---

## 97. chroot 技术 – Linux 系统的瑞士军刀

**原文标题**: The chroot Technique – a Swiss army multitool for Linux systems

**原文链接**: [https://livesys.se/posts/the-chroot-technique/](https://livesys.se/posts/the-chroot-technique/)

本文介绍了一种强大的修复无法启动的Linux系统的工具——"chroot"技术。作者讲述了在标准重装方法失败后，成功使用该技术修复Nanopore GridION设备的案例。

其核心思想是访问损坏系统的硬盘（通过Live USB或其他计算机），并将它的根分区挂载到工作系统上的一个目录中。关键在于，来自工作环境的必要系统目录，如`/sys`、`/proc`和`/dev`，也会被挂载到这个新的根目录中。然后，`chroot`命令有效地将当前会话的活动根文件系统切换到这个新组装的结构。

这允许用户运行直接与损坏系统的文件结构交互的命令，从而进行诊断和修复。例如，对基于Debian的系统使用`apt upgrade`或`dpkg-reconfigure`。

本文提供了该过程的逐步指南，包括：从替代操作系统启动，识别根分区和`/boot`分区，创建必要的目录，挂载分区和特殊系统文件夹，以及最终执行`chroot`命令。作者强调了拥有此过程作为紧急情况下的“速查表”的重要性。

作者还提到了一个真实场景，其中通过在chroot环境中运行`apt update`和`dpkg-reconfigure`，解决了损坏的符号链接和不完整的内核更新文件。

---

## 98. 视觉推理即将到来

**原文标题**: Visual Reasoning Is Coming Soon

**原文链接**: [http://arcturus-labs.com/blog/2025/03/31/visual-reasoning-is-coming-soon/](http://arcturus-labs.com/blog/2025/03/31/visual-reasoning-is-coming-soon/)

大型语言模型中视觉推理的激动人潜力：以OpenAI的图像处理进展为基础

本文探讨了大型语言模型(LLM)中视觉推理的激动人潜力，基于OpenAI最近在图像处理方面的进展。作者认为，传统的LLM在图像处理方面存在困难，因为它们依赖文本描述与外部图像生成工具进行通信，导致不一致。然而，OpenAI的新型GPT-4o模型直接集成了图像生成，从而实现了更具上下文相关性的图像处理。

作者认为这只是视觉推理的垫脚石，模型可以可视化场景并对其进行视觉推理，从而提高它们对世界的理解。他用一个弹珠在杯子里的问题来证明这一点，表明当模型生成图像来表示每个步骤时，其推理能力会得到提高。

文章建议，使用来自真实世界和合成场景的图像和文本序列，通过监督式微调来专门训练模型进行视觉推理至关重要。视频被强调为丰富的训练数据来源。作者还借鉴了LLM中思维链推理的演变，并预测视觉推理将提高模型在机器人技术和理解社交线索等领域的性能。虽然图像生成速度是当前的限制，但他相信这种情况会得到改善。最终，作者乐观地认为，视觉推理将彻底改变模型理解世界和与之互动的方式。

---

## 99. Agent2Agent 协议 (A2A)

**原文标题**: The Agent2Agent Protocol (A2A)

**原文链接**: [https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)

谷歌开发者博客宣布推出Agent2Agent协议 (A2A)，这是一种新的开放协议，旨在使人工智能代理能够跨不同的企业平台和应用程序进行通信、交换信息和协调行动，而无论构建它们的供应商或框架如何。谷歌将在超过 50 家技术合作伙伴和服务提供商的支持下推出 A2A。

A2A 背后的核心思想是促进一个动态的多代理生态系统，使人工智能代理能够协作以自动化复杂的工作流程、提高生产力并降低成本。A2A 补充了 Anthropic 的模型上下文协议 (MCP)。

A2A 遵循五个关键设计原则：拥抱代理能力（非结构化模式），构建在现有标准之上（HTTP、SSE、JSON-RPC），默认安全（OpenAPI 身份验证），支持长时间运行的任务，以及模式无关性（文本、音频、视频）。

该协议定义了“客户端”代理和“远程”代理之间的交互，包括能力发现（代理卡片）、任务管理、通过消息协作以及用户体验协商（内容类型、UI 功能）。

文章以候选人寻访为例，展示了多个代理如何协同工作以简化招聘流程。谷歌将以开源方式发布 A2A，并计划在今年晚些时候推出生产就绪版本。多家合作伙伴提供了引言，强调了代理互操作性对于在企业中扩展人工智能的重要性。

---

## 100. Linux内核防御图 – 安全加固概念

**原文标题**: Linux Kernel Defence Map – Security Hardening Concepts

**原文链接**: [https://github.com/a13xp0p0v/linux-kernel-defence-map](https://github.com/a13xp0p0v/linux-kernel-defence-map)

本文介绍了 Linux 内核防御地图，它以图形化的方式展示了 Linux 内核安全概念及其关系。该地图由 a13xp0p0v 创建，连接了漏洞类别（带有 CWE 编号）、利用技术、漏洞检测机制以及防御技术（包括内核内和内核外）。节点连接表示一种关系，不一定是完全缓解。

该地图旨在帮助浏览与内核安全加固相关的内核文档和源代码。它专门关注内核安全加固，不包括攻击面缩减、用户空间安全特性和 Linux 安全模块策略。

该地图以 DOT 语言编写，方便维护和通过 Git 进行版本控制，并使用 GraphViz 生成。该项目在 GitHub、Codeberg 和 GitFlic 上以 GPL-3.0 许可证发布。

作者还提供了一个名为 "kernel-hardening-checker" 的工具，用于自动验证 Linux 内核配置中的安全加固选项，解决了许多关键选项在主要发行版中默认情况下经常被禁用的问题。

最后，本文档提供了 Linux 内核安全相关的参考资料和文章、工具链接列表。此地图适用于 Linux 内核 v6.10。

---

