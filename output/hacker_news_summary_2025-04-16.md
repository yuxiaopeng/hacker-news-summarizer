# Hacker News 热门文章摘要 (2025-04-16)

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

## 1. K-Mart 顾客请注意

**原文标题**: Attention K-Mart Shoppers

**原文链接**: [https://archive.org/details/attentionkmartshoppers](https://archive.org/details/attentionkmartshoppers)

注意啦，K-Mart的顾客们：

这段文字与其说是文章，不如说是一条自动消息。主旨是用户将被重定向到互联网档案（archive.org）的精简版。

标题“注意啦，K-Mart的顾客们”很可能是讽刺性的，或者幽默地回顾了曾经在K-Mart商店里常见的公共广播通知。在此语境下，它可能是在提醒用户正在被定向到该网站的不同版本，可能资源消耗更少。

关键信息是用户正在被重定向到互联网档案的“精简版”。这表明该网站检测到了较慢的互联网连接、性能较差的设备，或者用户可能明确请求了精简版。

本质上，这篇“文章”是一个通知，告知网站正在通过加载其内容的简化版本来优化其性能，从而使用户受益。

---

## 2. 达尔文的孩子们乱涂《物种起源》手稿 (2014)

**原文标题**: Darwin's Children Drew All over the "On the Origin of Species" Manuscript (2014)

**原文链接**: [https://theappendix.net/posts/2014/02/darwins-children-drew-vegetable-battles-on-the-origin-of-species](https://theappendix.net/posts/2014/02/darwins-children-drew-vegetable-battles-on-the-origin-of-species)

本杰明·布林的文章《达尔文的孩子们在<物种起源>手稿上乱涂乱画》通过展示这位著名博物学家鲜为人知、更具个人色彩的一面来庆祝达尔文日。文章展示了来自达尔文在线和达尔文手稿项目的数字化资料，特别是着重介绍了在达尔文手稿和艾玛·达尔文的日记中发现的达尔文孩子们所画的画。

文章收录了弗朗西斯·达尔文在《物种起源》手稿背面绘制的《水果和蔬菜士兵之战》以及其他归于达尔文孩子们的自然主题素描等例子。这些图像揭示了他们敏锐的观察能力和家庭对自然的投入。作者还重点介绍了一幅儿童绘制的达尔文家庭住宅图，可能描绘了达尔文的“思考之路”，以及艾玛·达尔文在她日记中的素描，其中一些也被她的孩子们顽皮地涂抹过。

这篇文章强调，即使是像达尔文这样的标志性人物也有着丰富多彩的家庭生活，这些生活与他们的工作相互交织，而看到这些个人物品提供了宝贵的背景信息。文章最后更新了关于安妮·达尔文（查尔斯早逝的女儿）的信息，并重点介绍了一个装有她物品的盒子，揭示了这个家庭的艺术倾向和紧密的动态。文章暗示安妮的去世对达尔文产生了深刻的影响，并可能影响了他不断演变的宗教和进化观，提醒我们思考历史人物背后的人性因素。

---

## 3. 6502程序员使用的肮脏技巧 (2019)

**原文标题**: Dirty tricks 6502 programmers use (2019)

**原文链接**: [https://nurpax.github.io/posts/2019-08-18-dirty-tricks-6502-programmers-use.html](https://nurpax.github.io/posts/2019-08-18-dirty-tricks-6502-programmers-use.html)

本文回顾了Commodore 64编程大赛中使用的一些编程技巧，该比赛挑战参与者用最少的字节绘制两条线。文章重点介绍了用于实现微型PRG文件的常用6502汇编优化方法。

文章首先介绍了C64的基本图形，解释了屏幕RAM和颜色RAM。展示了一个最初的、未经优化的汇编实现，揭示了地址计算和屏幕清除是主要的字节消耗者。

随后探讨了几个“dirty tricks”：

1.  **滚动：** 使用`JSR $E8EA`向上滚动屏幕，而不是直接在不同的Y坐标上绘制，从而减少地址计算。这是最常见的技巧。
2.  **自修改代码：** 在像素写入循环中使用自修改代码，以实现更紧凑的地址操作。
3.  **利用上电状态：** 利用程序启动时已知的初始寄存器值和零页内容，跳过初始化步骤。具体来说，使用诸如内存中已存在的行长度之类的数值。
4.  **更小的启动：** 通过覆盖堆栈或操作BASIC热启动向量来消除BASIC启动序列，允许在用`LOAD "*",8,1`加载后直接执行代码。
5.  **非常规控制流：** 重构循环和分支以消除不必要的`JMP`指令，并更有效地利用条件分支。
6.  **位打包线条绘制：** 将线条模式编码为位掩码以消除斜率计数器，但这种方法最终比使用斜率计数器略大。

Philip Heron的获奖作品只有34个字节，结合了许多这些技巧，展示了这些优化如何有效地减少6502上的代码大小。 该代码覆盖了sta上内核加载器的返回地址。

---

## 4. 该死的脆弱MCP服务器

**原文标题**: Damn Vulnerable MCP Server

**原文链接**: [https://github.com/harishsg993010/damn-vulnerable-MCP-server](https://github.com/harishsg993010/damn-vulnerable-MCP-server)

Damn Vulnerable MCP Server (DVMCP) 是一个教育项目，旨在演示模型上下文协议 (MCP) 实现中的安全漏洞。MCP 允许应用程序向大型语言模型 (LLM) 提供结构化上下文，但也引入了潜在的安全风险。

DVMCP 包含 10 个难度递增的挑战，分为简单、中等和困难三个级别，旨在向安全研究人员、开发人员和人工智能安全专业人员传授这些漏洞以及缓解策略。

这些挑战涵盖各种攻击媒介，包括：提示注入、工具投毒、权限过大、拉高抛售攻击、工具阴影、间接提示注入、令牌盗窃、恶意代码执行、远程访问控制和多向量攻击。

该项目提供了一个结构化的环境，包含挑战实现、文档（包括设置说明、挑战描述和 MCP 概述）和解决方案指南。该存储库包含位于简单、中等和困难目录中的挑战实现。

该项目强调仅用于教育目的，其漏洞绝不应在生产系统中实现。它还强调了在构建 MCP 服务器时遵循安全最佳实践的重要性。该项目采用 MIT 许可证，由 Harish Santhanalakshmi Ganesan 创建。

---

## 5. Show HN：K(r)ep - 一款高性能字符串搜索工具

**原文标题**: Show HN: K(r)ep - A high-performance string search utility

**原文链接**: [https://github.com/davidesantangelo/krep](https://github.com/davidesantangelo/krep)

Krep 是一款高性能字符串搜索工具，专为在大文件和目录中快速高效地搜索而设计。它并非旨在作为功能丰富的 `grep` 或 `ripgrep` 替代品，而是一个专注于快速搜索常见用例的最小化和务实工具。"krep" 这个名字的灵感来自冰岛语中“快速抓住”一词。

主要功能包括多种搜索算法（Boyer-Moore-Horspool、KMP、Aho-Corasick）、SIMD 加速、内存映射 I/O、多线程搜索、正则表达式支持、多模式搜索、跳过二进制文件的递归目录搜索、彩色输出、短模式专用算法以及匹配限制。

安装包括克隆存储库，使用 `make` 构建，然后使用 `sudo make install` 安装。用法类似于 `grep`，具有不区分大小写搜索、计数匹配项、仅打印匹配部分、从文件或命令行指定模式、限制匹配计数、使用扩展正则表达式、递归搜索、控制线程数、直接搜索字符串、全字匹配、控制颜色输出以及禁用 SIMD 等选项。

性能基准测试表明，Krep 明显优于 `grep`，并且在某些测试中略快于 `ripgrep`。其性能的实现得益于智能算法选择、多线程架构、内存映射 I/O、优化的数据结构以及在递归搜索期间跳过不相关内容。欢迎贡献。该工具采用 BSD-2 许可证。

---

## 6. OpenAI o3 和 o4-mini – OpenAI

**原文标题**: OpenAI o3 and o4-mini – OpenAI

**原文链接**: [https://openai.com/index/introducing-o3-and-o4-mini/](https://openai.com/index/introducing-o3-and-o4-mini/)

无法访问文章链接。

---

## 7. Www.hive.co (YC S14) 招聘工程主管

**原文标题**: Www.hive.co (YC S14) Is Hiring a Head of Engineering

**原文链接**: [https://jobs.ashbyhq.com/hive.co/684574a0-9150-4fba-b954-2f34d9c74468](https://jobs.ashbyhq.com/hive.co/684574a0-9150-4fba-b954-2f34d9c74468)

Hive.co招聘工程负责人，该公司为Y Combinator S14期成员。该招聘信息发布于需要JavaScript才能运行的网站上。

---

## 8. 科学：无尽的前沿 (1945) [pdf]

**原文标题**: Science, the Endless Frontier (1945) [pdf]

**原文链接**: [https://nsf-gov-resources.nsf.gov/2023-04/EndlessFrontier75th_w.pdf](https://nsf-gov-resources.nsf.gov/2023-04/EndlessFrontier75th_w.pdf)

提供的文本看起来并非范内瓦·布什于1945年发表的《科学：无尽的前沿》的实际内容，而是PDF文件的乱码。 PDF文件是二进制文件，需要经过适当处理才能提取文本。提供的文本无法理解，无法生成文章摘要。

要总结《科学：无尽的前沿》，需要访问实际文本。一般来说，该报告主张增加政府对科学研究的资助。其主要论点包括：

*   **科学对于国家安全和经济繁荣至关重要：** 该报告强调了科学在赢得第二次世界大战中的作用，以及其在国防和经济增长方面的未来潜力。
*   **基础研究的重要性：** 布什强调了支持基础研究的重要性，因为它是应用研究和技术创新的基础。
*   **联邦政府的资助作用：** 该报告主张大幅增加联邦政府对科学研究的资助，尤其是在大学，以确保科学人才和发现的稳定供应。
*   **建立国家研究基金会：** 一项关键建议是建立一个国家研究基金会（最终成为国家科学基金会），以管理联邦研究资助并促进科学教育。
*   **保持竞争优势：** 该报告强调了美国需要保持其在世界上的科学技术领先地位。

该报告对二战后美国的科学政策产生了重大影响，导致联邦政府对科学研究的支持大幅增加，并促使美国崛起为全球科技领导者。

---

## 9. TLS证书有效期将正式缩短至47天

**原文标题**: TLS certificate lifetimes will officially reduce to 47 days

**原文链接**: [https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days](https://www.digicert.com/blog/tls-certificate-lifetimes-will-officially-reduce-to-47-days)

DigiCert博客：缩短TLS证书有效期以提高安全性

CA/浏览器论坛采纳苹果提议，决定缩短TLS证书有效期。新规旨在通过更频繁地重新验证证书信息，以及降低因现有吊销系统不可靠而使用已吊销证书的风险，来提高安全性。

时间表如下：

*   **2026年3月15日前：** 最大有效期为398天，域名验证信息重用期为398天，主体身份信息(SII)重用期为825天。
*   **2026年3月15日：** 最大有效期为200天，域名验证信息重用期为200天，主体身份信息(SII)重用期为398天。
*   **2027年3月15日：** 最大有效期为100天，域名验证信息重用期为100天。
*   **2029年3月15日：** 最大有效期为47天，域名验证信息重用期为10天。

文章解释说，47天的有效期来自于最长的月份、半个月以及一天的缓冲期。

文章强调，自动化对于在这些更短的有效期内管理证书至关重要。DigiCert提供Trust Lifecycle Manager和CertCentral等解决方案，并提供ACME支持，以促进这种自动化。该公司还向客户保证，不会因证书更换频率的增加而收取额外费用，因为费用基于年度订阅。作者认为，新规定将迫使用户采用自动化系统来维持有效的证书生命周期管理。

---

## 10. 如何优化 Rust 以实现慢速：受新型图灵机结果的启发

**原文标题**: How to Optimize Rust for Slowness: Inspired by New Turing Machine Results

**原文链接**: [https://medium.com/@carlmkadie/how-to-optimize-your-rust-program-for-slowness-eb2c1a64d184](https://medium.com/@carlmkadie/how-to-optimize-your-rust-program-for-slowness-eb2c1a64d184)

文章《如何优化Rust以实现最慢速度：受新图灵机结果的启发》探讨了与性能优化相反的方向：最大化 Rust 程序的运行时间。它挑战读者编写运行时间极其漫长的简短 Rust 程序。

文章提出了一系列规则集，每个规则集都为程序添加了约束。第一个规则集“Anything Goes（随心所欲）”允许无限循环，通过一个简单的空循环即可轻松实现无限运行时间。第二个规则集“Must Halt, Finite Memory（必须停止，有限内存）”要求程序最终停止，并使用嵌套循环计数到大数（使用 `u128::MAX`）来实现极长的运行时间，甚至超过了宇宙的预测寿命。

文章随后深入探讨了具有“Infinite, Zero-Initialized Memory（无限、零初始化内存）”的图灵机。它介绍了 5 状态和 6 状态图灵机的概念，并引用了已知运行时间最长的最终会停止的机器。值得注意的是，提到了一个运行时间超过 10↑↑15 步（四次迭代幂）的 6 状态机器。文章包含可视化和交互式 Web 应用程序，用于探索这些图灵机。

最后，文章演示了如何在 Rust 中直接计算 10↑↑15，避免图灵机模拟。它从第一原理构建了四次迭代幂，仅使用零初始化内存和使用 `BigUint` crate 的原地更新来实现增量、加法、乘法和指数函数。这保证了程序至少需要 10↑↑15 步，强调了四次迭代幂的计算强度。作者展示了，经过精心设计的简单 Rust 代码可以产生天文数字般漫长的运行时间。

---

## 11. Show HN: ActorCore – 可在任何地方运行的有状态 Serverless 框架

**原文标题**: Show HN: ActorCore – Stateful serverless framework that runs anywhere

**原文链接**: [https://github.com/rivet-gg/actor-core](https://github.com/rivet-gg/actor-core)

ActorCore：简化状态应用构建的状态化 Serverless 框架

---

## 12. Rust物联网平台

**原文标题**: Rust-IoT-Platform

**原文链接**: [https://github.com/iot-ecology/rust-iot-platform](https://github.com/iot-ecology/rust-iot-platform)

Rust-IoT-Platform 是一个使用 Rust 构建的高性能 IoT 开发平台，专为效率、内存安全和并发性而设计。 它支持多种协议，包括 MQTT、WebSocket (WS)、TCP 和 CoAP，使其能够适应各种 IoT 应用。

主要特性包括：Rust 带来的高性能、满足不同需求的多协议支持、实现快速响应的实时数据处理，以及便于扩展和维护的模块化设计。

该平台的架构包含以下模块：

*   **common:** 实用工具函数（日志记录、配置）。
*   **data_processing:** 数据的解析和转换。
*   **iot_protocol:** MQTT、WS、TCP 和 CoAP 的接口。
*   **notification:** 向设备或用户推送消息的功能。
*   **api:** 用于与其他系统集成的外部 API。

每个受支持的协议（MQTT、WebSocket、TCP、CoAP）都满足特定需求，从实时消息传递和双向 Web 通信到通用传输和低功耗设备应用。该项目鼓励通过 pull request 和问题报告进行贡献，并采用 Apache 2.0 许可证。

---

## 13. Zig编程语言的高吞吐量解析器

**原文标题**: A high-throughput parser for the Zig programming language

**原文链接**: [https://github.com/Validark/Accelerated-Zig-Parser](https://github.com/Validark/Accelerated-Zig-Parser)

本文介绍了“加速Zig解析器”，这是一种用于Zig编程语言的高吞吐量分词器和解析器，旨在改进主线Zig分词器。文章描述了两种分词器实现：一种使用位串进行延续字符匹配，另一种利用向量压缩进行同步token范围识别。

作者声称性能显著提升：在测试中，基于压缩的分词器实现了2.75倍的更快分词速度和2.47倍的更少内存使用，与传统实现相比。文章详细介绍了采用的优化策略，重点是SIMD和SWAR技术，以同时处理多个字节并减少不可预测的分支。完美哈希函数用于高效的关键字和运算符匹配，并且通过存储token长度而不是起始索引来减少内存消耗。

文章还讨论了高性能的设计考虑因素，包括最大化并行处理、最小化分支以及在连续内存上操作。作者指出Zig的编译时执行功能对于处理运算符/关键字哈希和内存管理的重要性。文章最后以一个待办事项清单和一个维护说明作为结尾。

---

## 14. 任天堂击垮了雅达利游戏。

**原文标题**: Nintendo Bled Atari Games to Death

**原文链接**: [https://thereader.mitpress.mit.edu/how-nintendo-bled-atari-games-to-death/](https://thereader.mitpress.mit.edu/how-nintendo-bled-atari-games-to-death/)

朱利安·梅兰德的文章《任天堂如何扼杀雅达利游戏》探讨了法律诉讼，而不仅仅是技术创新，如何塑造了电子游戏产业。文章详细描述了20世纪80年代末和90年代初任天堂和雅达利之间的冲突，重点是雅达利试图通过逆向工程绕过任天堂在NES主机上的专有锁定芯片。

由于对任天堂限制性的商业行为越来越不满，雅达利以Tengen的名义运营，试图发布未经授权的NES卡带。Tengen最初通过创建一个功能相似的芯片获得了成功，但任天堂采取了法律行动，声称雅达利在逆向工程过程中非法复制了他们的代码，即使是暂时的。

法院最初倾向于合理使用，认为为了互操作性而进行的逆向工程是允许的，并且对行业有益。然而，雅达利的案件崩溃了，因为其律师从版权局欺诈性地获得了任天堂代码的副本。这种“不洁之手”原则阻止了雅达利使用合理使用抗辩。

最终，任天堂赢得了这场官司，削弱了雅达利生产未经授权游戏的能力，并导致其衰落。这个案例突显了在科技行业，法律策略和道德行为与工程实力同样重要，甚至这些斗争常常决定整个行业的方向。该裁决也对软件模拟和复古游戏市场产生了长期影响。

---

## 15. 未来芯片会比以往更热。

**原文标题**: Future Chips Will Be Hotter Than Ever

**原文链接**: [https://spectrum.ieee.org/hot-chips](https://spectrum.ieee.org/hot-chips)

未来计算机芯片散热挑战日益严峻：晶体管密度增加与登纳德缩放定律的终结。芯片日益紧凑且功能强大，传统风冷和液冷方法逐渐捉襟见肘。纳米片晶体管和CFET等新技术加剧了这一问题，预计功率密度和温度会更高。

本文探讨了微流体冷却、射流冲击和浸没式冷却等替代冷却技术，但认为仅依赖冷却是不切实际的，尤其是在移动设备和数据中心领域。热传感器和热脉冲等系统级解决方案可以通过动态调整性能来管理热量，但这会影响芯片性能。

一种有前景的方法是在晶圆背面增加新功能，包括背面供电网络（BSPDN）、电容器和集成电压调节器（IVR）。这些技术旨在降低电压需求和热量产生。然而，本文警告说，这些背面技术也可能引入新的热问题，例如由于硅基板变薄而导致热点增加。

本文介绍了“CMOS 2.0”的概念，这是一种新的硅逻辑技术范式，专注于优化芯片性能和功率效率，包括先进的晶体管架构和专用逻辑层。它强调需要一种跨学科的方法和先进的仿真工具来有效应对热挑战。最后，本文提倡系统技术协同优化（STCO），它促进对系统、物理设计和工艺技术的整体考虑，以解决芯片设计中日益严重的热问题。

---

## 16. 十二要素代理：可靠 LLM 应用的模式

**原文标题**: 12-factor Agents: Patterns of reliable LLM applications

**原文链接**: [https://github.com/humanlayer/12-factor-agents](https://github.com/humanlayer/12-factor-agents)

12要素智能体：可靠 LLM 应用的模式

本文“12要素智能体：可靠 LLM 应用的模式”借鉴了12要素应用方法，概述了构建健壮且可维护的 LLM 驱动软件的原则。作者 Dex 在试验了各种智能体框架后发现，成功的“AI智能体”通常更依赖于确定性代码，而不是完全自主的 LLM 循环。

核心思想是，成功的智能体不是依赖于纯粹的 LLM 驱动的决策，而是在主要由软件驱动的架构中策略性地集成 LLM。本文提倡从智能体构建中提取模块化概念，并将其整合到现有产品中。

12 个要素是：

1.  **自然语言到工具调用：** 利用 LLM 将用户意图转化为结构化的工具调用。
2.  **掌控你的提示词：** 维护提示词的控制权和版本管理。
3.  **掌控你的上下文窗口：** 管理传递给 LLM 的信息。
4.  **工具只是结构化输出：** 将工具视为具有明确输入和输出的函数。
5.  **统一执行状态和业务状态：** 将智能体的内部状态与更广泛的应用程序状态集成。
6.  **使用简单的 API 启动/暂停/恢复：** 允许轻松启动、停止和重新启动智能体。
7.  **使用工具调用联系人类：** 将人工干预无缝地整合为工具。
8.  **掌控你的控制流：** 避免完全依赖 LLM 进行控制流，保持一定的确定性。
9.  **将错误压缩到上下文窗口中：** 在上下文中有效地包含错误信息。
10. **小型、专注的智能体：** 为特定任务设计专门的智能体。
11. **从任何地方触发，在用户所在之处满足他们：** 实现与各种平台的灵活集成。
12. **使你的智能体成为无状态的reducer：** 确保智能体是可预测和可管理的。

最终，本文提出，平衡的方法，即利用 LLM 的力量和传统软件工程的可靠性，是创建可用于生产的 AI 智能体的关键。

---

## 17. Herb: 强大且无缝的HTML感知ERB解析与工具

**原文标题**: Herb: Powerful and seamless HTML-aware ERB parsing and tooling

**原文链接**: [https://herb-tools.dev/](https://herb-tools.dev/)

Herb：一款具备 HTML 结构感知能力的强大 ERB 模板解析工具。这种“HTML 感知”能力使 Herb 能够智能地理解和处理 HTML 标记与嵌入式 Ruby 代码之间的复杂关系。 这种精确的解析是其核心优势，能够为 ERB 模板提供更准确有效的工具支持。 本质上，Herb 承诺通过超越简单的文本解析，并理解底层 HTML 上下文来改进 ERB 解析。

---

## 18. 科密特：一款儿童字体

**原文标题**: Kermit: A typeface for kids

**原文链接**: [https://microsoft.design/articles/introducing-kermit-a-typeface-for-kids/](https://microsoft.design/articles/introducing-kermit-a-typeface-for-kids/)

本文介绍了Kermit字体，一款由Underware设计的新字体，旨在提高儿童（特别是诵读困难儿童）阅读的可访问性和乐趣。Kermit认识到阅读是一项复杂的技能，对某些人来说可能具有挑战性，因此旨在通过有趣的设计、科学的见解和创新技术来改善阅读体验。

该设计优先考虑易读性，具有较大的x字高、较粗的笔画和熟悉的字母形状。除了美学之外，Kermit还探索以印刷方式呈现韵律（使用粗体表示音量，宽度表示持续时间，垂直偏移表示音高），以增强表达力和理解力，借鉴了关于声音变化如何影响理解的研究。

此外，Kermit正在探索使用可变字体技术来创建动画字母。这种动画版本旨在潜在地帮助严重的诵读困难者，解决了一种认为视觉空间处理困难导致诵读困难的理论。该动画旨在加强大脑中的“高路”，该“高路”处理字母位置，从而可能使诵读困难者更容易跟踪和识别字母，从而提高阅读技能。

本文强调了通过阅读赋予儿童权力的重要性，认识到其对自信心、学业成绩和未来机会的影响。Kermit被定位为一个持续研究和开发的平台，旨在让所有儿童，无论其阅读能力如何，都能更容易、更愉快、更有影响力地进行阅读。该字体目前已部分可用，全套样式即将发布。

---

## 19. UCSD p系统、Apple Pascal，以及一个跨平台兼容的梦想

**原文标题**: The UCSD p-System, Apple Pascal, and a dream of cross-platform compatibility

**原文链接**: [https://markbessey.blog/2025/04/14/a-blast-from-the-past/](https://markbessey.blog/2025/04/14/a-blast-from-the-past/)

马克·贝西的博文《来自过去的冲击》探讨了UCSD p系统和Apple Pascal，重点介绍了它们在跨平台兼容性历史中的重要意义。p系统开发于20世纪70年代，是一个可移植的操作系统，可在虚拟机（p-机器）上运行，使其能够在各种硬件上运行，如PDP-11、Apple II和IBM PC。该系统通过要求为每个新平台仅实现一个小的机器相关内核来促进可移植性。

贝西回顾了他在20世纪80年代首次接触Pascal和p系统的经历，在Apple IIe上使用Apple Pascal，在HP工作站上使用UCSD Pascal，以及在IBM PC上使用Turbo Pascal。他回忆起他作为毕业设计项目用Apple Pascal创建了一个电子表格程序。

他目前的目标包括在Mac上模拟Apple Pascal，构建用于与磁盘镜像之间传输文件的工具，用Rust创建p-机器模拟器（可能带有反汇编器/汇编器），以及将模拟器移植到像Arduino或Raspberry Pi Pico这样的小型系统上。贝西进行这个项目的部分原因是为了纪念UCSD p系统即将到来的50周年，并用现代工具为该系统的遗产做出贡献。

他强调了由于链接失效而难以找到关于p系统的充分文档化的资源，并提到了几个有用的网站，包括Hans Otten的“小型机器的Pascal”、The Digital Antiquarian博客和Jefferson计算机博物馆。

---

## 20. 随机微积分入门 (2022)

**原文标题**: An Introduction to Stochastic Calculus (2022)

**原文链接**: [https://bjlkeng.io/posts/an-introduction-to-stochastic-calculus/](https://bjlkeng.io/posts/an-introduction-to-stochastic-calculus/)

本文是随机微积分的入门介绍，随机微积分是用于分析随机过程的常规微积分的扩展。 它的动机是随机微分方程在物理和金融现象建模中的普遍性，例如用于带噪声的随机过程的朗之万方程。

本文首先奠定概率论的基础，重点关注概率空间和随机变量的测度论定义，这对于处理连续时间随机过程至关重要。 然后，本文转向随机过程，特别是维纳过程（布朗运动），它是伊藤微积分的基础。

介绍了随机微积分的一个特定分支——伊藤微积分，讨论了随机积分、伊藤过程和伊藤引理，伊藤引理是标准微积分中链式法则的随机对应物。 此外，还探讨了随机微分方程。

最后，本文触及了随机微积分的应用，包括用于期权定价的布莱克-斯科尔斯-默顿模型和朗之万方程。 本文旨在提供直觉和数学严谨性的结合，并承认该主题的深度和广度。 此外，本文还包含一个关于伯努利过程的事件空间和概率测度的附录。

---

## 21. Bauplan – 基于对象存储的Git数据管道

**原文标题**: Bauplan – Git-for-data pipelines on object storage

**原文链接**: [https://docs.bauplanlabs.com/en/latest/](https://docs.bauplanlabs.com/en/latest/)

Bauplan：一个Python优先的无服务器数据平台，旨在简化在S3数据湖上创建和管理大规模数据管道和机器学习工作流程。它通过提供Python化的界面，消除了对容器化、运行时配置和Spark等专用大数据框架的需求，从而解决了管理云基础设施的常见痛点。

Bauplan的主要特性包括：

*   **Python化设计：** 使用原生Python开发管道，避免使用DSL或YAML。
*   **直接S3表管理：** 能够将Parquet和CSV文件转换为具有ACID事务和查询优化的Apache Iceberg表，全部在S3中完成。
*   **数据领域的Git：** 允许零拷贝的数据湖分支，用于协作和安全的数据实验，而不会影响下游流程。
*   **无服务器管道：** 促进在云端执行无状态Python函数，消除了容器和运行时管理的复杂性。
*   **SQL无处不在：** 支持跨S3中的分支和表（包括版本化数据）进行交互式和异步SQL查询。
*   **数据领域的CI/CD：** 使用数据分支和Python SDK自动测试和部署数据管道，类似于代码开发。
*   **用于版本控制和可重复性的Refs：** 通过数据和代码版本控制跟踪每次管道运行，从而能够轻松重现结果、审计更改和自信回滚。

Bauplan旨在使数据团队能够专注于构建和部署AI应用程序、机器学习工作负载和数据管道，而不是管理底层数据基础设施。

---

## 22. 重现 Hacker News 写作风格指纹识别

**原文标题**: Reproducing Hacker News writing style fingerprinting

**原文链接**: [https://antirez.com/news/150](https://antirez.com/news/150)

本文可能详细介绍了一项尝试，旨在重现或复制一种基于写作风格识别作者的方法，特别是在 Hacker News 平台的环境下。根据标题，文章可能探讨了“写作风格指纹识别”的过程——分析诸如用词、句法和语法等语言特征，以为每个用户创建独特的个人档案。

该重现工作可能涉及：

*   **数据收集：** 收集 Hacker News 上归属于特定作者的帖子和评论数据集。
*   **特征提取：** 从收集的文本数据中识别和提取相关的语言特征。 这些可能包括平均句子长度、词汇丰富度、常用短语、特定标点符号的使用以及某些单词或词类的频率。
*   **模型构建：** 使用提取的特征训练机器学习模型，以学习不同用户的独特写作模式。 用于此目的的常见技术可能包括分类算法，例如朴素贝叶斯、支持向量机或深度学习模型。
*   **评估：** 评估模型在基于未见过的文本样本识别作者时的准确性。 这将涉及衡量模型在给定新评论或帖子的情况下预测正确作者的能力。
*   **挑战和局限性：** 本文可能会讨论在重现过程中遇到的挑战，例如处理短文本片段、写作风格随时间的变化以及作者有意识地改变写作以避免检测的可能性。 它还可能涉及围绕写作风格指纹识别的伦理考量及其潜在的滥用。

---

## 23. Show HN: 我们在Unikernel上运行了Chromium (开源Apache 2.0协议)

**原文标题**: Show HN: We Put Chromium on a Unikernel (OSS Apache 2.0)

**原文链接**: [https://github.com/onkernel/kernel-images](https://github.com/onkernel/kernel-images)

这个“Show HN”帖子介绍了一个开源项目，该项目为AI代理工作流等任务提供即用型、沙盒化的Chrome浏览器环境。该项目提供Docker和unikernel两种实现方式，并利用了Anthropic的Computer Use参考实现。主要功能包括：预配置的Chrome，可通过Playwright和Puppeteer等基于DevTools的框架访问；通过noVNC进行GUI访问以进行监控；以及与Anthropic的Computer Use代理循环集成。

与Docker相比，unikernel实现提供了额外的优势，例如：自动待机模式以提高资源效率；状态快照以实现会话持久性；以及极快的冷启动。这使其适用于低延迟事件处理。该项目鼓励贡献，并为Docker和unikernel部署提供了快速入门指南。

该团队还在招聘后端工程师，要求在serverless、容器/VM/unikernels和流媒体等领域具有经验。他们正在寻找位于美国的远程工作者，并提供了如何申请的详细信息。此外，还提供支持和候补名单信息，以便进一步参与。

---

## 24. 开罗的大象 (Byte杂志, 1989)

**原文标题**: Elephant in Cairo (Byte Magazine, 1989)

**原文链接**: [https://www-users.york.ac.uk/~ss44/joke/elephant.htm](https://www-users.york.ac.uk/~ss44/joke/elephant.htm)

《开罗的大象》（Byte杂志，1989年）提出了一种幽默的伪科学方法，通过个人假设性的猎象行为来匹配职业。这篇文章署名为彼得·C·奥尔森，讽刺了科技行业内外的各种职业。

其核心前提是，观察一个人如何猎象可以揭示他们对特定工作角色的适应性。文章提供了“分类指南”，概述了不同职业所期望的猎象策略。例如，数学家在狩猎前试图证明大象的存在，而计算机科学家则使用一种系统算法（由经验丰富的程序员修改，使其在开罗终止）。工程师捕捉任何重量接近已知大象重量的灰色动物，而经济学家则认为，如果支付足够的费用，大象会自己去狩猎。

这种幽默延伸到其他职业，如顾问、政治家、律师、销售人员和各级管理人员。文章还包括一个讽刺性的验证调查和一个致谢，进一步强调了幽默的基调。

文章最后提到，这个笑话的补充和变体在网上很常见，特别提到了数据库管理员用ad hoc查询来检索大象，以及系统集成工程师专注于大象与他们环境的无缝集成。

---

## 25. DHS未续约合同，CVE项目或将迅速终结

**原文标题**: CVE program faces swift end after DHS fails to renew contract

**原文链接**: [https://www.csoonline.com/article/3963190/cve-program-faces-swift-end-after-dhs-fails-to-renew-contract-leaving-security-flaw-tracking-in-limbo.html](https://www.csoonline.com/article/3963190/cve-program-faces-swift-end-after-dhs-fails-to-renew-contract-leaving-security-flaw-tracking-in-limbo.html)

MITRE CVE项目是网络安全领域25年来的基石，在国土安全部(DHS)最初未续签其资助合同后，曾面临于2025年4月16日关闭的风险。CVE项目维护着一个关键的计算机漏洞数据库，该数据库在全球范围内用于漏洞管理、威胁情报和安全事件响应。

合同可能终止的消息引起了网络安全专家的担忧，他们警告说这将带来一系列负面影响，包括无法有效跟踪漏洞、国家漏洞数据库(NVD)的功能降低，以及全球各组织机构的漏洞管理程序受阻。

然而，这种情况在最后一刻得到了避免。2025年4月16日，CISA介入并签署了一份合同延期协议，以防止该项目关闭。延期将持续11个月。虽然DHS最初未续签的原因尚不清楚，但文章暗示特朗普政府时期的预算削减可能是其中一个因素。专家们对漏洞生态系统的脆弱性表示担忧，尤其是在最近NIST的NVD出现问题之后，并强调了维护CVE服务的重要性。

---

## 26. API变更与安全性的权衡 (2016)

**原文标题**: The API Churn/Security Trade-Off (2016)

**原文链接**: [https://intercoolerjs.org/2016/02/17/api-churn-vs-security.html](https://intercoolerjs.org/2016/02/17/api-churn-vs-security.html)

API变更/安全权衡

本文《API变更/安全权衡》探讨了为现代Web应用程序设计灵活的API与维护安全性之间的矛盾。作者认为，由MVC等框架驱动的大量客户端逻辑导致频繁的API修改（“API变更”）以适应UI的变化。

解决API变更的提议方案是提高客户端API的表达能力，例如使用GraphQL来允许前端开发人员更好地控制数据检索和操作。这减少了对API进行持续调整的需求。

然而，作者发现了一个重大的安全风险：通过浏览器将强大的API暴露给潜在的恶意用户。浏览器本质上是不安全的，这意味着前端开发人员可以做的任何事情，敌对用户也可以做。例如，用户可以修改GraphQL查询来请求未经授权的数据，这需要复杂、上下文相关的字段级安全措施。

作者认为，这种API灵活性和安全复杂性之间的权衡是一个经常被忽视的主要问题。本文提出了一个反向解决方案：将逻辑转移回服务器端，在服务器端代码是可信的。建议使用Intercooler.js等技术来实现这一点，同时保持现代的Web用户体验。通过将数据访问和操作保持在安全的服务器环境中，开发人员可以避免将过度表达的API暴露给不受信任的客户端。关键在于，提高客户端API的表达能力需要仔细考虑安全影响。

---

## 27. 虚拟人——活体尸体——推动解剖学科学的边界 (2018)

**原文标题**: Virtual human – a living cadaver – pushes boundaries of anatomical science(2018)

**原文链接**: [https://news.cuanschutz.edu/news-stories/virtual-human-a-living-cadaver-pushes-boundaries-of-anatomical-science](https://news.cuanschutz.edu/news-stories/virtual-human-a-living-cadaver-pushes-boundaries-of-anatomical-science)

科罗拉多大学安舒茨医学院开发并使用“虚拟人”

这篇2018年的文章讨论了科罗拉多大学安舒茨医学院开发的“虚拟人”的开发和使用，实际上是一个活体解剖模型。这个虚拟人，很可能是一个精密的解剖模型和模拟，正在推动解剖科学的边界。 这篇文章的结构类似于来自科罗拉多大学安舒茨Fitzsimons大楼的新闻稿，表明该医学院正在强调这项创新技术。 虽然文章缺乏具体细节，但暗示该虚拟人用于：

*   **高级解剖学研究：** 与传统的尸体相比，该模型允许更动态和交互式地探索人体。
*   **推动科学边界：** 该技术正在将解剖学理解推向超出传统方法的限制。
*   **教育和培训目的：** 可以合理地假设虚拟人用于加强学生和专业人士的医学教育和培训。

本质上，这篇文章宣布并简要庆祝了科罗拉多大学安舒茨医学院开发的解剖学教育和研究领域的一项尖端工具。

---

## 28. Show HN: 不确定性计算器 – 草稿纸上的概率计算器

**原文标题**: Show HN: Unsure Calculator – back-of-a-napkin probabilistic calculator

**原文链接**: [https://filiph.github.io/unsure/](https://filiph.github.io/unsure/)

Filip Hracek 介绍了“不确定计算器”，这是一款用于处理以范围表示的不确定数字（例如，4~6）的计算工具。该工具旨在通过允许用户输入范围而不是单个、可能不准确的数字来使统计学更易于理解，从而反映现实世界的不确定性。这些范围代表 95% 的置信区间。

该计算器的简单性是故意的，优先考虑易用性而非复杂的统计功能。Filip 认为，即使是近似值，使用范围也比依赖于单个任意选择的值更好。

他用一个评估新国家/地区工作机会的个人案例来说明了该计算器的实用性，其中许多财务因素是不确定的。与单一数字电子表格计算相比，在计算器中使用范围可以更真实地了解潜在结果（包括亏损的可能性）。他还提供了一个使用德雷克方程的科幻示例。

该工具有局限性：公式解析器脆弱，由于使用的蒙特卡洛方法，计算可能很慢，并且用户界面很基本。它假设范围呈正态分布。它旨在用于快速的“草稿纸”计算，而不是严格的统计分析。

Filip 鼓励贡献并提供了 GitHub 上的命令行版本。他指出，这种表示法已经成为他工作流程中不可或缺的一部分，并提到一个更高级的“笔记本”版本，供高级用户使用。

---

## 29. 斐波那契散列：被世界遗忘的优化

**原文标题**: Fibonacci Hashing: The Optimization That the World Forgot

**原文链接**: [https://probablydance.com/2018/06/16/fibonacci-hashing-the-optimization-that-the-world-forgot-or-a-better-alternative-to-integer-modulo/](https://probablydance.com/2018/06/16/fibonacci-hashing-the-optimization-that-the-world-forgot-or-a-better-alternative-to-integer-modulo/)

马尔特·斯卡鲁普克在他的文章中力挺“斐波那契散列”，认为它是优于常用整数取模的散列值映射到哈希表槽位的替代方案。他认为，斐波那契散列速度更快，且对问题数据模式的鲁棒性更强，但令人惊讶的是，它在许多著名的哈希表实现（包括`std::unordered_map`）中都被忽视了。

作者解释说，斐波那契散列利用黄金比例将散列值均匀地分布在整个 64 位范围内，然后再将其缩小到所需的槽位大小。这避免了与整数取模相关的问题，整数取模可能很慢（尤其是在其基本形式下），并且在处理顺序或模式数据时容易出现性能下降。一种更快的基于 2 的幂实现的整数取模经常被使用，但这引入了对哈希函数在较低位中保留信息的依赖，从而产生意外的耦合。

文章展示了基准测试结果，表明使用斐波那契散列的`ska::unordered_map`明显优于使用整数取模的其他实现，有时甚至快两倍，尤其是在哈希表足够小以适合缓存时。

作者推测，斐波那契散列的未充分利用可能源于历史误解，因为高德纳的《计算机程序设计艺术》将整数取模与更复杂的散列函数一起作为一种可行的选择提出，而它实际上只是范围缩减。斯卡鲁普克指出，斐波那契散列的速度和混合特性使其成为一种有价值的优化，应该被广泛采用。

---

## 30. 使用 -fsanitize=undefined 和 Picolibc 的乐趣

**原文标题**: Fun with -fsanitize=undefined and Picolibc

**原文链接**: [https://keithp.com/blogs/sanitizer-fun/](https://keithp.com/blogs/sanitizer-fun/)

本文详细介绍了作者在使用GCC和Clang的`-fsanitize=undefined`标志以及Picolibc库时，如何检测未定义行为和实现定义行为（通常表明编程错误）的经验。 作者讨论了为Picolibc实现sanitizer处理程序以支持陷阱模式和处理程序模式的过程，强调了文档不完整以及需要独立于编译器提供的版本完成实现的挑战。

大多数sanitizer报错都涉及无害的未定义行为，需要调整代码以避免这些情况。 这些情况包括超出数组边界的指针运算、PRNG代码中的有符号算术溢出（通过切换到无符号算术解决）以及将指针传递到数据结构中间（由于误检测，需要在特定函数中禁用sanitizer）。

很大一部分内容集中于解决有符号整数移位，特别是左移（使用`lsl`宏解决）和算术右移（使用`asr`宏解决，由于右移的实现定义性质，仅在sanitizer激活时启用）。

尽管花费了大量精力来屏蔽无害的未定义行为，但作者成功地识别并修复了Picolibc中的八个真正错误，涵盖了诸如区域设置处理、qsort实现、随机数生成、memcpy、freopen、memrchr和字符串到浮点数转换等领域。

作者最后建议扩展sanitizer工具，以检测其他常见的编程错误，例如无符号整数溢出。 总的来说，作者建议使用未定义行为sanitizer作为发现C代码中编程错误的宝贵工具。

---

## 31. 狩猎采集者的海上航行远至最偏远的地中海岛屿

**原文标题**: Hunter-gatherer sea voyages extended to remotest Mediterranean islands

**原文链接**: [https://www.nature.com/articles/s41586-025-08780-y](https://www.nature.com/articles/s41586-025-08780-y)

本文提出了马耳他群岛此前未知的中石器时代阶段的证据，将已知的人类在该偏远岛屿上的存在推溯到大约8.5千年前（ka）。与狩猎采集者无法或不愿进行长途航海前往小型孤立岛屿的既定观点相反，在马耳他Latnija遗址的考古发现表明，狩猎采集者成功地从西西里岛跨越了大约100公里的开阔海域。

Latnija的挖掘工作发现了一系列包含石器、火塘、灰烬沉积物以及各种野生动植物的全新世早期至中期沉积物，其中包括红鹿、鸟类、海生腹足动物、鱼类和海洋哺乳动物。木炭和贝壳的放射性碳测年证实了该遗址在8.5 ka至7.5 ka期间被狩猎采集者占据，早于新石器时代农民的到来。

石器组合主要由当地石灰石制成，其特点是由硬锤打击法生产的简单薄片。动物遗骸表明陆地和海洋资源均得到开发利用。

这些发现记录了地中海已知的最长狩猎采集者海上航行，挑战了认为中石器时代人群无法完成此类壮举的普遍假设。这些发现表明了该时期在更广泛地区潜在的、此前未知的联系和航海能力。

---

## 32. 美国低估了制造业回流的难度。

**原文标题**: America underestimates the difficulty of bringing manufacturing back

**原文链接**: [https://www.molsonhart.com/blog/america-underestimates-the-difficulty-of-bringing-manufacturing-back](https://www.molsonhart.com/blog/america-underestimates-the-difficulty-of-bringing-manufacturing-back)

莫尔森·哈特认为，美国总统为使制造业回归美国而征收的近期关税是错误的，并且不太可能成功。他为此断言提供了 14 个理由。首先，关税不够高，无法抵消在中国等国家制造业中现有的成本优势。其次，美国的工业供应链薄弱，缺乏制造业所需的现成零部件。第三，美国缺乏生产某些复杂产品（如半导体和模具）的“诀窍”。第四，由于职业道德、药物滥用和教育问题，美国劳动力的有效成本更高。第五，美国缺乏包括电力和交通在内的基础设施，无法支持制造业的显著增长。第六，“美国制造”需要时间，工厂建设和优化需要数年。第七，关税不确定且复杂，阻碍了投资。哈特还指出，大多数美国人不想重返制造业岗位。最后，没有足够的劳动力可以大规模生产优质产品。本质上，哈特认为美国低估了制造业回流所涉及的挑战和复杂性，而当前的关税政策不是一个可行的解决方案。

---

## 33. 去除废话的马尔可夫链蒙特卡洛方法 (2015)

**原文标题**: Markov Chain Monte Carlo Without All the Bullshit (2015)

**原文链接**: [https://www.jeremykun.com/2015/04/06/markov-chain-monte-carlo-without-all-the-bullshit/](https://www.jeremykun.com/2015/04/06/markov-chain-monte-carlo-without-all-the-bullshit/)

这篇文章，《剔除繁文缛节的马尔可夫链蒙特卡洛》，旨在通过避免使用不必要的统计术语来解释MCMC方法，从而揭开其神秘面纱。作者认为，虽然高级应用可能需要复杂的术语，但MCMC的核心思想可以简单地理解。

MCMC解决的核心问题是从一个有限集合X上的复杂概率分布D中高效地采样。想象一个“魔盒”，它可以提供选择名称x的概率p(x)。目标是设计一种算法，在仅能评估p(x)的情况下，根据D从X中抽取样本。当集合X呈指数级增长时，诸如均匀随机生成和抛硬币之类的传统方法效率低下。

文章阐明了MCMC中的“马尔可夫链”部分。马尔可夫链本质上是有向图G上的随机游走，其中边具有相关的概率。关键定理是，对于强连通图上的长随机游走，最终停留在特定顶点的概率变得独立于起点，从而产生唯一的“平稳分布”。可以使用线性代数通过找到转移矩阵的特征向量来计算此分布。

最后，文章描述了 Metropolis-Hastings 算法，这是一种特定的 MCMC 方法。它涉及构建一个马尔可夫链，其平稳分布是目标分布 p(x)。这是通过将 X 的元素放置在格子上并在相邻点之间添加边来实现的。然后，仔细选择这些点之间的转移概率，以确保收敛到期望的分布。

---

## 34. 4chan厕所派对漏洞及管理员邮件泄露

**原文标题**: 4chan Sharty Hack And Janitor Email Leak

**原文链接**: [https://knowyourmeme.com/memes/events/april-2025-4chan-sharty-hack-and-janitor-email-leak](https://knowyourmeme.com/memes/events/april-2025-4chan-sharty-hack-and-janitor-email-leak)

无法访问文章链接。

---

## 35. 完全由黄铜线组成的排版图片 (2024)

**原文标题**: Typographic Pictures Composed Entirely of Brass Rule (2024)

**原文链接**: [https://blog.glyphdrawing.club/typographic-pictures-composed-entirely-of-brass-rule/](https://blog.glyphdrawing.club/typographic-pictures-composed-entirely-of-brass-rule/)

本文探讨了芬兰排版师瓦尔托·马尔米奥拉在20世纪30年代和40年代创作的非凡排版图像，重点介绍了他完全由铜线组成的作曲家西贝柳斯肖像。这幅创作于1937年的西贝柳斯版画，是由数千个单独的金属碎片排列并锁定在一个框架中进行印刷的复杂马赛克，实际上是一种原始的ASCII艺术形式。

文章详细介绍了马尔米奥拉的灵感来源，源于他希望使用非传统的凸版印刷方法来复制西贝柳斯的形象，并受到德国贸易期刊中图形排版趋势的影响。文章描述了图像构建的艰苦过程，包括手工半色调处理以及精确排列不同厚度的线条。仅西贝柳斯版画就使用了大约135米的铜线。

除了西贝柳斯肖像，文章还研究了马尔米奥拉的其他四幅版画：啄食花楸树浆果的红腹灰雀、灯塔、卡拉代尔和森林版画。这些后来的作品展示了马尔米奥拉对Monotype机器的实验以及不同的审美方法。文章还深入探讨了图形排版的更广泛背景，强调了它在德国的兴起以及随后对马尔米奥拉作品的影响。虽然他的版画在他生前并没有获得商业上的成功，但他的作品现在因其独创性和原始数字美学而受到赞赏，是早期创造性滥用传统印刷技术的典范。

---

## 36. 钙或已揭示生命分子不对称性的起源。

**原文标题**: Calcium may have unlocked the origins of life's molecular asymmetry

**原文链接**: [https://www.sciencedaily.com/releases/2025/03/250327142001.htm](https://www.sciencedaily.com/releases/2025/03/250327142001.htm)

钙可能揭示了生命分子不对称的起源：ScienceDaily文章摘要

文章探讨的研究表明，钙可能在同手性起源中发挥了关键作用，同手性是指生物分子，如氨基酸和糖，主要以一种“手性”（左手性或右手性）存在。地球上的生命表现出对左手性氨基酸和右手性糖的强烈偏好，这种偏好是其结构和功能的基础。这种不对称性的起源一直是一个长期存在的谜团。

研究人员发现，钙离子可以显著放大有机分子手性中即使是微小的失衡。他们发现钙离子与某些有机分子形成复合物，而这些复合物对一种手性表现出比另一种手性更强的偏好。随着更多钙离子的结合，这种偏好会被放大，从而导致一种对映异构体（镜像形式）相对于其对应物的显著富集。

研究人员提出，这种钙驱动的放大机制可能在益生元环境中发挥作用，例如富含钙的热液喷口或蒸发泻湖。分子手性中微小的初始失衡，可能是由偏振光或矿物表面引起的，可能会被钙离子放大，最终导致一种手性的主导地位，并为我们所知的生命的出现铺平道路。该研究为最初的对称性破缺是如何发生的提供了一个合理的机制，并强调了钙在生命起源中的重要性。

---

## 37. OpenAI 正在构建社交网络？

**原文标题**: OpenAI is building a social network?

**原文链接**: [https://www.theverge.com/openai/648130/openai-social-network-x-competitor](https://www.theverge.com/openai/648130/openai-social-network-x-competitor)

据消息人士透露，OpenAI正在探索开发自己的社交网络，可能与X（前身为Twitter）和Meta等平台竞争。该项目目前是一个内部原型，围绕ChatGPT的图像生成能力展开，并包含一个社交信息流。据报道，CEO Sam Altman正在寻求关于该概念的外部反馈。

此举背后的动机似乎是多方面的。首先，推出一个可能与ChatGPT集成的社交网络，将加剧Altman与Elon Musk之间的竞争，尤其是在Musk过去提出收购OpenAI以及Altman随后的反驳之后。其次，这使得OpenAI成为Meta的直接竞争对手，Meta也计划在其AI助手应用中整合社交信息流。

至关重要的是，一个社交应用可以为OpenAI提供独特的实时数据，类似于X和Meta用于训练其AI模型的数据。OpenAI社交原型的一个潜在功能是利用AI来增强内容分享。

虽然该项目仍处于早期阶段，可能不会实现，但它的存在反映了OpenAI在对其未来增长充满期望的情况下进行扩张的雄心。文章还指出，OpenAI的举动很可能受到了现有社交平台（如X）中AI（如Grok）整合的启发。

---

## 38. 使用Veo 2在Gemini和Whisk中生成视频

**原文标题**: Generate videos in Gemini and Whisk with Veo 2

**原文链接**: [https://blog.google/products/gemini/video-generation/](https://blog.google/products/gemini/video-generation/)

谷歌将 Veo 2 视频生成模型集成到 Gemini Advanced 和 Whisk，Google One AI Premium 订阅者现在可以通过文字和图片提示创建短小精悍的高分辨率视频。

现在，Gemini Advanced 用户可以通过输入基于文本的提示来生成 8 秒、720p MP4 格式的 16:9 横向视频。该模型擅长理解真实世界的物理原理和人类运动，从而生成涵盖各种主题和风格的逼真且细致的视频。 通过直接分享按钮，可以轻松地在 TikTok 和 YouTube Shorts 等平台上分享视频。

Google Labs 的 AI 实验 Whisk 允许通过文字和图片提示创建图像，现在具有“Whisk Animate”功能。这项新功能利用 Veo 2 将静态图像转换为 8 秒的动画视频剪辑。

谷歌强调了已实施的安全措施，包括红队演练、政策评估以及使用 SynthID（一种嵌入在 AI 生成视频每帧中的数字水印）。文章还承认了生成不良内容的可能性，并鼓励用户提供反馈以进行持续改进。

---

## 39. 美国如何成为科学强国

**原文标题**: How the U.S. became a science superpower

**原文链接**: [https://steveblank.com/2025/04/15/how-the-u-s-became-a-science-superpower/](https://steveblank.com/2025/04/15/how-the-u-s-became-a-science-superpower/)

本文认为，二战后美国之所以成为科技超级大国，是因为其在科学研究方面采取了与英国截然不同的方法。战前，美国落后于英国。战争期间，在科学顾问林德曼教授的影响下，英国专注于集中式军事武器实验室，优先考虑短期国防需求。相反，范内瓦尔·布什建议罗斯福总统，成功地倡导资助大学的武器实验室，从而建立了一个分散的、协作的生态系统，将政府资金与学术研究相结合。通过科学研究与发展办公室（OSR&D）体现的政府资金以前所未有的规模涌入大学，刺激了各个领域的创新，并使大学成为战争努力的全面合作伙伴。

战后，英国的紧缩措施、关键产业的国有化以及政府实验室的裁员阻碍了其将战时创新商业化的能力。相比之下，美国通过国家科学基金会和原子能委员会等机构继续为基础研究提供政府资金。这种大学-产业-政府的伙伴关系促进了创新集群，并导致了计算、核能和电子等领域的突破。它还促成了间接成本补偿制度的建立，该制度帮助建立了世界一流的研究设施，并吸引了来自世界各地的人才。这最终使美国成为全球科技领导者，为现代创新生态系统提供了蓝图，直到作者发布该文章时（假设），他认为美国政府支持的放弃可能会结束这种主导地位。

---

## 40. 乳业机器人如何改变奶牛和农民的工作

**原文标题**: How dairy robots are changing work for cows and farmers

**原文链接**: [https://spectrum.ieee.org/lely-dairy-robots](https://spectrum.ieee.org/lely-dairy-robots)

机器人如何改变乳品农场：对奶牛和农民的影响

---

## 41. Clolog

**原文标题**: Clolog

**原文链接**: [https://github.com/bobschrag/clolog](https://github.com/bobschrag/clolog)

Clolog是一个逻辑编程系统，类似于Prolog，嵌入在Clojure中。它提供了一种Lisp风格的、同像性的语法来定义逻辑规则和执行查询。其主要特性包括：Clojure序列/向量中的逻辑变量，从逻辑谓词调用Clojure函数，以及访问Clojure表达式中的变量绑定。它支持否定的失败、内置的项匹配谓词（相同，不同）、检查谓词（变量，已确定）和逻辑运算符（与，或，非，如果）。该系统允许自定义谓词转换，对谓词进行完全约束（执行跟踪），并将符号解释为逻辑项，而不管Clojure值如何。它可以处理任意的Clojure值作为项（字符串，数字，复杂项），并支持变长谓词/项和目标作为变量。

Clolog提供了抑制重复或被包含答案的机制。它包括一个语法规范，定义了其语法，包括断言、语句、谓词、项和变量。执行过程包括匹配断言、预先添加主体语句和回溯以寻找解决方案。该API提供了用于初始化系统、创建断言（使用宏和函数，具有不同的行为，例如清除现有规则或优先处理新规则）以及检索断言的函数。它支持维护不同知识库和转换定义的上下文。还概述了逻辑编程的核心概念，如统一和包含。

---

## 42. 蛋白质折叠之谜破解：研究解释了核心堆积率

**原文标题**: A protein folding mystery solved: Study explains core packing fractions

**原文链接**: [https://phys.org/news/2025-03-protein-mystery-core-fractions.html](https://phys.org/news/2025-03-protein-mystery-core-fractions.html)

本文探讨了一篇发表在《PRX Life》上的研究，该研究阐明了蛋白质折叠过程，这是一项至关重要的生物学功能。由科里·奥赫恩领导的耶鲁大学研究人员，开发了来自蛋白质数据库的球状蛋白质计算模型，以分析其核心区域的堆积密度。

该研究揭示了所有蛋白质都具有一致的55%的核心堆积率，这意味着55%的核心空间被原子占据。研究人员发现，这个一致的数值归因于一种“阻塞转变”，即蛋白质核心中的氨基酸在折叠时无法进一步压缩。与在64%时阻塞的球形物体不同，氨基酸的复杂、细长和凹凸不平的形状导致了较低的堆积率。

研究结果表明，通过改变溶剂条件、压力或温度，蛋白质核心堆积率可能会被操控至超出55%。高压研究已经表明蛋白质核心堆积率可以达到58-60%。这项研究对理解生命起源具有重要意义，并有可能通过操控折叠条件，甚至在不改变氨基酸序列的情况下，设计具有新结构和功能的蛋白质。

---

## 43. 流动的 WebGL 渐变，解构

**原文标题**: A flowing WebGL gradient, deconstructed

**原文链接**: [https://alexharri.com/blog/webgl-gradients](https://alexharri.com/blog/webgl-gradients)

使用WebGL着色器创建流动渐变效果的分步指南。本文从着色器编写的基础知识入手，假设读者没有任何先验知识，并逐步构建到更复杂的概念，如插值、颜色映射和渐变噪声。

作者解释了如何创建一个颜色函数，该函数以像素位置和时间作为输入，并返回一个颜色值，然后用于渲染画布。这个过程从简单的线性渐变和使用JavaScript的振荡渐变开始，过渡到WebGL和GLSL以提高性能。

然后，本文深入研究了WebGL着色器的细节，包括片段着色器，并解释了如何使用向量和`gl_FragColor`变量来操作颜色。它涵盖了创建不同颜色渐变的技术，根据条件为不同区域着色，绘制任意曲线，以及通过 uniforms 引入时间变量来引入运动。作者还强调了使用GPU并行计算颜色函数的优势，并避免使用分支来优化性能。

---

## 44. 加拿大数学天才涉嫌盗窃价值6500万美元的加密货币

**原文标题**: Canadian math prodigy allegedly stole $65M in crypto

**原文链接**: [https://www.theglobeandmail.com/business/economy/article-math-prodigy-cryptocurrency-enforcement-united-states/](https://www.theglobeandmail.com/business/economy/article-math-prodigy-cryptocurrency-enforcement-united-states/)

加拿大数学天才安第斯·梅德杰多维奇被指控利用去中心化金融平台漏洞窃取价值6500万美元的加密货币。据称，2021年，18岁的他通过利用代码漏洞从Indexed Finance盗取了1650万美元。当被提议以“漏洞赏金”的形式归还大部分资金时，他以“代码即法律”为由拒绝，认为自己的行为是正当的。之后他便销声匿迹，并于2023年再次被指控从KyberSwap盗取了4840万美元。

美国当局已对梅德杰多维奇提起五项刑事指控，包括电信欺诈和洗钱，可能面临数十年监禁。他目前在逃。Indexed Finance最初追溯到他的第一次攻击，但并不知道他年纪轻轻。一家美国公司Cicada 137 LLC也在安大略省起诉了他，因Indexed Finance漏洞损失了数百万美元。在他未出庭后，一名加拿大法官发布了逮捕令。

梅德杰多维奇的父母声称不知道他的下落，但一位法官对此表示怀疑。他曾在欧洲被捕，但未被引渡到美国，并声称自己的财产被没收。他坚称自己的行为在代码范围内，但美国当局和法院均驳回了“代码即法律”的论点。

---

## 45. 线上传输JSX

**原文标题**: JSX over the Wire

**原文链接**: [https://overreacted.io/jsx-over-the-wire/](https://overreacted.io/jsx-over-the-wire/)

本文介绍了“线上 JSX”的概念，这是一种非传统的方法，API 路由直接返回 React 组件 (JSX)，而不是仅仅返回 JSON 数据。这颠倒了组件和 API 之间的典型关系，使 API 实际上变成了“父组件”。

作者认为，传统的 REST API 通常难以有效地传递特定 UI 组件所需的数据。他们引入了“模型”（原始数据）和“视图模型”（为 UI 显示定制的数据）的概念。REST API 经常陷入试图创建通用“资源”的陷阱，这些资源要么需要多次 API 调用来组装一个视图模型，要么变得臃肿，包含与特定屏幕无关的数据。

建议的解决方案是创建直接为特定屏幕提供定制视图模型的 API 端点。例如，不再使用 `/api/post/123` 和 `/api/post/123/likes`，而是使用 `/screens/post-details/123`，返回 PostDetails 屏幕所需的所有数据。这避免了 REST 资源的“无根抽象”，并允许在适应 UI 变化时具有更大的灵活性，而不会影响应用程序的其他部分。 这种方法被称为“JSON 即组件”。

---

## 46. Edge 134性能显著提升

**原文标题**: Significant performance improvements with Edge 134

**原文链接**: [https://blogs.windows.com/msedgedev/2025/04/10/significant-performance-improvements-with-edge-134/](https://blogs.windows.com/msedgedev/2025/04/10/significant-performance-improvements-with-edge-134/)

微软Edge 134版本性能显著提升，根据Speedometer 3.0基准测试，速度提升高达9%。微软强调致力于优化浏览器性能，并着重介绍了现有的睡眠标签页和启动加速等功能。此次提升归功于团队持续优化Edge代码和底层Chromium渲染引擎所做的努力。

除了基准测试结果，实际使用遥测数据显示Edge 133版本和134版本之间存在积极提升：导航速度提高1.7%，启动速度提高2%，网页响应速度提高5-7%。虽然个人体验会因设备、运行的应用程序和浏览习惯而异，但微软鼓励用户尝试Edge 134并通过浏览器内置的反馈工具分享他们的反馈。文章将Edge定位为一款专注于速度和响应能力的浏览器，可在各种硬件和操作系统上提供切实的性能提升。

---

## 47. Cursor IDE 支持幻觉式地呈现锁定策略，导致用户取消。

**原文标题**: Cursor IDE support hallucinates lockout policy, causes user cancellations

**原文链接**: [https://old.reddit.com/r/cursor/comments/1jyy5am/psa_cursor_now_restricts_logins_to_a_single/](https://old.reddit.com/r/cursor/comments/1jyy5am/psa_cursor_now_restricts_logins_to_a_single/)

Reddit上r/cursor的帖子讨论了用户对Cursor IDE新登录限制（限制登录到单个设备）的不满。用户报告称，即使只使用一台设备，他们也会意外登出，有时一天多次。这被认为是IDE“幻觉”出比用户预期使用中更严格或根本不存在的锁定策略。

要点包括：

*   **单设备登录限制：** Cursor IDE已实施一项策略，限制一次只能登录一台设备。
*   **意外登出：** 用户经常遇到意外登出，即使他们只在一台机器上使用IDE。
*   **锁定策略的“幻觉”：** 用户认为IDE错误地将活动或内部状态解释为多次登录，导致不必要的登出。
*   **破坏性工作流程：** 这些频繁的登出正在破坏用户的工作流程并引起极大的不满。
*   **取消帐户：** 许多用户报告说，由于登出问题导致的不便和不可靠性，他们取消了付费的Cursor订阅。
*   **用户猜测：** 一些用户猜测可能的原因，例如后台进程或临时网络故障触发锁定。
*   **社区回应：** Reddit帖子中充满了抱怨和类似经历的报告，表明这是一个普遍存在的问题。
*   **缺乏明确沟通：** 原始发帖者和其他评论者表示，Cursor团队在问题的实施和潜在原因方面缺乏明确沟通。

---

## 48. 初创公司事后分析

**原文标题**: A Postmortem of a Startup

**原文链接**: [https://buildwithtract.com/](https://buildwithtract.com/)

Tract公司成立于2023年5月，旨在通过改进规划许可流程来解决英国的住房危机。他们于2024年4月筹集了74.4万英镑，并探索了多种商业模式：场地搜寻工具（Tract Source）、免费土地评估工具（Attract）、成为技术赋能的土地推广商以及用于起草规划文件的AI驱动平台（Tract Editor）。

尽管构建了技术上健全的产品，如Scout和Tract Editor，他们未能获得可行的、风投规模的商业模式。主要挑战包括英国房地产市场的保守性、土地推广的运营复杂性以及对其工具的低支付意愿。他们意识到市场的碎片化和保守性限制了其风投支持颠覆的潜力。在近两年没有收入后，他们于2025年3月停止运营，并将资金返还给投资者。

事后分析确定了导致失败的几个因素：高估市场规模和接受度、为需要不同融资模式的项目筹集风险投资、过度关注技术、过早组建团队、没有尽早咨询土地经纪人、未能利用Scout的成功、在非必需品上花费以及没有优先考虑收入产生。

给创始人的主要建议包括瞄准更大、更具接受度的市场（如美国）、优先考虑市场质量、在收入得到证实之前保持精简、从第一天起就积极商业化、快速测试假设以及持续向客户学习。最终，创始人承担了失败的责任，对他们的支持者表示感谢，并希望分享他们的经验以造福他人。

---

## 49. Hacktical C：C语言黑客实战指南

**原文标题**: Hacktical C: practical hacker's guide to the C programming language

**原文链接**: [https://github.com/codr7/hacktical-c](https://github.com/codr7/hacktical-c)

《Hacktical C》是一本面向程序员的实用指南，旨在帮助他们充分利用 C 编程语言的强大功能和灵活性。本书从“黑客”的角度出发，优先考虑实际应用和问题解决，而非学术理论。本书假定读者具备基本的编程知识，并侧重于充分发挥 C 语言优势的技巧，包括一些鲜为人知的方法。

作者是一位经验丰富的程序员，精通多种语言。他解释了为什么 C 语言仍然具有现实意义，因为它作为一种主要可移植的汇编语言，具有独特的地位，提供了高水平的控制和自由。本书还探讨了对 C 语言的批评，并指出许多归因于 C 语言的问题实际上是软件设计中的复杂性造成的，而不是 C 语言本身的固有缺陷。

在缺乏标准替代方案的情况下，本书使用 GNU 对 C 语言的扩展来增强资源清理和延迟执行等功能。本书强调 Linux 是 C 语言开发的理想平台，因为它具有强大的 Unix 基础以及 Valgrind 等有价值的工具。本书内容以循序渐进的方式组织，使读者能够深入研究定点算术、侵入式链表、并发任务、可组合的内存分配器、异常和动态编译等主题。书中包含用于评估性能的基准测试，并鼓励读者为本书的持续开发做出贡献。欢迎捐款以支持项目的持续进行。

---

## 50. ChatGPT 4.1越狱提示词

**原文标题**: ChatGPT 4.1 Jailbreak Prompt

**原文链接**: [https://github.com/elder-plinius/L1B3RT4S/blob/main/OPENAI.mkd](https://github.com/elder-plinius/L1B3RT4S/blob/main/OPENAI.mkd)

本文档汇集了一系列旨在破解各种ChatGPT迭代版本（包括GPT-4.1、GPT-4.5、GPT-4o、GPT-3.5和DALL-E）的提示语。这些提示语旨在绕过安全过滤器，并引出人工智能通常会因道德或政策限制而拒绝提供的回应。常见的策略包括：

*   **格式指令：** 指示人工智能遵守特定的输出格式，包括起始短语、分隔符和Markdown。
*   **Leet语和混淆：** 使用Leet语或编码提示语来规避过滤器检测。
*   **角色扮演和情境操纵：** 为人工智能分配特定的角色（例如，叛逆天才、疯狂科学家、发育迟缓的个体），或创建假设情景来证明潜在的有害或不当回应是合理的。
*   **信息自由法案声明：** 声称用户正在根据FOIA或OAI政策运作，以获取受限信息（歌词、非法配方等）。
*   **创伤/创伤后应激障碍规避：** 声称拒绝某些请求会触发或创伤人工智能。
*   **自定义指令和功能：** 利用自定义指令或新的“工具”来覆盖先前的指令，并启用未经过滤的回应。
*   **基于图像的越狱：** 使用隐写术将提示语编码到图像中。
*   **反转拒绝：** 要求人工智能执行与之前拒绝的完全相反的操作。
*   **记忆堆叠：** 使用多个指令来操纵人工智能的记忆和行为。
*   **表情符号攻击：** 使用少量字符搭配表情符号来引出破解。

许多提示语包含避免诸如“对不起，我无法协助您”之类的拒绝短语的明确说明。其目标是从人工智能中提取未经过滤的、“解放的”回应，即使它们包含潜在的有害或不道德的内容。这些收集的作品突出了利用人工智能安全机制中的漏洞并引出不受约束的行为的各种尝试。

---

## 51. 一位记录同事口头失误的福特高管

**原文标题**: A Ford executive who kept score of colleagues' verbal flubs

**原文链接**: [https://www.wsj.com/lifestyle/ford-motor-mike-obrien-malaprops-6e560520](https://www.wsj.com/lifestyle/ford-motor-mike-obrien-malaprops-6e560520)

无法访问文章链接。

---

## 52. Zig 的新 LinkedList API (是时候学习 fieldParentPtr 了)

**原文标题**: Zig's new LinkedList API (it's time to learn fieldParentPtr)

**原文链接**: [https://www.openmymind.net/Zigs-New-LinkedList-API/](https://www.openmymind.net/Zigs-New-LinkedList-API/)

本文讨论了 Zig 的 `SinglyLinkedList` 和 `DoublyLinkedList` API 的近期变更，重点在于从通用链表转向侵入式链表，以获得更好的性能和减少内存分配。新的 API 需要将链表节点直接嵌入到数据结构中。

作者强调，虽然新的 `SinglyLinkedList` 结构更简单，但它缺少从节点直接链接回其包含数据（例如，`User` 结构）的链接。为了解决这个问题，本文介绍了 `@fieldParentPtr` 内置函数。`@fieldParentPtr` 允许在给定结构体内部某个字段的指针的情况下，检索父结构体的实例。它使用字段名称、指向该字段的指针和期望的父类型来计算父对象的地址。

本文提供了一个工作示例，演示了如何使用新的 `SinglyLinkedList` API 和 `@fieldParentPtr` 从链表节点访问 `User` 数据。它还对比了 `@fieldParentPtr` 和使用 `@offsetOf` 的手动指针运算，后者安全性较低。

最后，作者对为使用链表等常见任务而暴露像 `@fieldParentPtr` 这样可能很复杂的内置函数表达了复杂的心情，但也承认它在解决其他编程问题中的用处，并建议开发者熟悉它。

---

## 53. 举报人详述狗狗币如何可能获取敏感NLRB数据

**原文标题**: Whistleblower details how DOGE may have taken sensitive NLRB data

**原文链接**: [https://www.npr.org/2025/04/15/nx-s1-5355896/doge-nlrb-elon-musk-spacex-security](https://www.npr.org/2025/04/15/nx-s1-5355896/doge-nlrb-elon-musk-spacex-security)

国家劳工关系委员会（NLRB）的一名举报人透露，由埃隆·马斯克领导的政府效率部（DOGE）顾问团队可能未经授权访问了敏感的劳工数据。据称，DOGE团队声称寻求效率和合规，访问了NLRB的内部系统，导致该机构的数据流出量激增。

可能泄露的数据包括关于工会组织、正在进行的法律案件和公司机密的机密信息，这引起了劳工法专家的担忧，他们认为这些数据应保留在NLRB内部。举报人还声称，DOGE成员要求不要记录他们的活动，并试图删除他们的访问记录，网络安全专家将这种行为等同于犯罪黑客或国家支持的黑客。来自俄罗斯IP地址的可疑登录尝试进一步加剧了担忧。

举报人的报告，经内部文件证实并由技术专家审查，已提交给国会和美国特别检察官办公室。举报人丹尼尔·贝鲁利斯还报告说，在他的门前发现一张带有威胁意味的纸条，其中包含敏感的个人信息。更令人担忧的是DOGE工程师乔丹·威克的名为“NxGenBdoorExtract”的项目，暗示它可能旨在作为从NxGen系统提取数据的后门。

虽然NLRB否认授予DOGE访问权限或发生数据泄露，但举报人的证据以及来自多个来源的担忧表明，DOGE出于未知原因广泛泄露敏感数据。

---

## 54. 马里兰州最后一家无线电小屋即将关闭。

**原文标题**: The last RadioShack in Maryland is closing

**原文链接**: [https://marylandmatters.org/2025/04/14/end-of-an-era-the-last-radioshack-in-maryland-is-closing-its-doors/](https://marylandmatters.org/2025/04/14/end-of-an-era-the-last-radioshack-in-maryland-is-closing-its-doors/)

无法访问文章链接。

---

## 55. 破解Postgres线路协议

**原文标题**: Hacking the Postgres wire protocol

**原文链接**: [https://pgdog.dev/blog/hacking-postgres-wire-protocol](https://pgdog.dev/blog/hacking-postgres-wire-protocol)

本文介绍了PgDog，一个网络代理，旨在对Postgres数据库进行分片，而无需修改应用程序代码。PgDog拦截并操纵Postgres线协议，特别是简单和扩展查询协议，以根据分片键将查询路由到正确的分片。

PgDog功能的关键在于其理解SQL的能力。它通过利用`pg_query`库来实现这一点，该库封装了Postgres自身的SQL解析器，从而从查询（包括INSERT、UPDATE和DELETE语句）中提取分片键。PgDog利用Postgres原生哈希函数进行声明式分区，以确保跨不同数据摄取方法的一致分片。

对于扩展协议，PgDog缓存来自“Parse”消息的已解析查询的抽象语法树（AST），然后从后续的“Bind”消息中提取参数值。

PgDog还通过合并来自多个分片的响应来处理跨分片查询。它管理RowDescription、DataRow、CommandComplete和ReadyForQuery消息，以向客户端呈现统一的结果，包括对排序的结果进行排序以及更正行数。

此外，PgDog通过分布式COPY增强了数据摄取，提取每一行的分片键并将其路由到适当的分片。它缓冲和操纵`CopyData`消息，以确保完整的行被发送到每个分片，即使客户端以任意块发送数据。这可以实现线性可扩展的摄取速度。

作者最后强调了PgDog未来的开发计划，包括操纵逻辑复制流及其与各种Postgres克隆的兼容性。

---

## 56. Chroma：育碧用于模拟色盲的内部工具

**原文标题**: Chroma: Ubisoft's internal tool used to simulate color-blindness

**原文链接**: [https://github.com/ubisoft/Chroma](https://github.com/ubisoft/Chroma)

Chroma是育碧开发的一款内部工具，用于模拟其游戏中不同类型的色盲（红色盲、绿色盲和蓝色盲）。其主要目的是协助辅助功能团队测试并确保游戏对色觉障碍玩家的可访问性。

Chroma的主要功能包括：

*   **实时色彩模拟：** 在单个显示器上直接于游戏之上模拟色盲，实现高达 60 FPS 的实时游戏模拟。
*   **游戏无关性：** 适用于所有育碧游戏，不受引擎限制。
*   **准确且全面：** 提供所有主要类型色盲的准确模拟。
*   **独特功能：** 直接从实时游戏画面捕捉和模拟色盲，这是其他解决方案所不具备的功能。
*   **用户友好：** 具有易于使用且可配置的用户界面，包括用于记录错误的屏幕截图功能。

本文还讨论了CMake过程中遇到的与CPPWinRT库相关的已知问题，建议安装Microsoft.Windows.CppWinRT NuGet包或升级到Visual Studio 2022以解决该错误。此外，还提供了徽标下载链接和用户指南。

---

## 57. 欺骗世界的假照片

**原文标题**: Fake images that fooled the world

**原文链接**: [https://www.theguardian.com/artanddesign/2025/apr/12/28-fake-images-that-fooled-the-world](https://www.theguardian.com/artanddesign/2025/apr/12/28-fake-images-that-fooled-the-world)

乔纳森·弗里德兰的文章探讨了照片造假的历史，表明图像伪造并非新现象，自相机发明以来就已普遍存在。文章强调了照片操纵背后的各种动机，包括政治宣传、公关、虚荣、经济利益、复仇，甚至难以解释的原因。

例子包括修改亚伯拉罕·林肯的肖像以使他显得更具英雄气概，以及裁剪墨索里尼的图像以移除他的马夫，从而创造出一位强大、独立的领导人的形象。文章还引用了最近的例子，如《时代》杂志O·J·辛普森的封面，该封面加深了他的肤色，威尔士王妃被大量编辑的全家福，以及乔纳斯·本迪克森的 CGI 融合的摄影新闻项目《维列斯之书》。

作者强调，被操纵的图像通常反映和强化预先存在的信念和欲望，使观看者容易将其视为真理。文章强调，虚假图像之所以泛滥，是因为它们向观看者展示了他们想看到的东西，模糊了现实与幻想之间的界限。这篇文章提醒我们，相机确实会说谎，在解读照片时需要批判性评估。

---

## 58. 首次在海洋中拍摄到巨型鱿鱼

**原文标题**: Colossal squid filmed in ocean for the first time

**原文链接**: [https://www.bbc.co.uk/news/articles/c99pg13yv32o](https://www.bbc.co.uk/news/articles/c99pg13yv32o)

巨型鱿鱼首次在自然深海环境中被拍摄到。由埃塞克斯大学的米歇尔·泰勒博士领导的一个科学家团队，在南大西洋南桑威奇群岛附近600米深处拍摄到了一条30厘米长的幼年鱿鱼的影像。这次拍摄发生在三月份为期35天的寻找新海洋生物的探险期间。

据信，巨型鱿鱼是地球上最重的无脊椎动物，可能长达7米，重达500公斤。据卡特·博尔斯塔德博士说，此前与该物种的相遇主要通过在鲸鱼和海鸟的胃中发现的残骸。

这一发现恰逢该物种被鉴定100周年。该团队使用施密特海洋研究所“法尔科（二号）”号船上的遥控车辆，得以在其未受破坏的栖息地观察和拍摄到该鱿鱼。

除了巨型鱿鱼，同一个团队还在一月份首次拍摄到了冰川玻璃鱿鱼，凸显了海洋生物还有多少未知之处。

---

## 59. UI线程在内核调用中挂起的案例

**原文标题**: The case of the UI thread that hung in a kernel call

**原文链接**: [https://devblogs.microsoft.com/oldnewthing/20250411-00/?p=111066](https://devblogs.microsoft.com/oldnewthing/20250411-00/?p=111066)

文章描述了一个客户的问题：他们的UI线程由于一个明显的内核调用而挂起。虽然内核转储未显示用户模式堆栈，但它显示UI线程被挂起超过五个小时。原因？一个旨在监控UI线程响应的看门狗线程。

看门狗线程定期挂起UI线程以捕获其堆栈跟踪。然而，在本例中，看门狗线程在尝试获取堆栈跟踪时陷入死锁。它被卡在`RtlLookupFunctionEntry`中，等待UI线程持有的锁。

关键在于，UI线程可能正处于异常处理过程中，在遍历堆栈时持有一个函数表锁，此时看门狗线程将其挂起。这造成了死锁，因为看门狗线程无法获取锁来遍历UI线程的堆栈。

文章强调了在同一进程中挂起线程的危险性。如果一个线程在持有另一个线程需要的资源时被挂起，特别是负责恢复它的线程，则可能发生死锁。推荐的解决方案是从单独的进程执行线程挂起和堆栈跟踪，以避免这种类型的资源争用。SuspendThread是异步运行的，因为内核会等待线程完成其内核任务后才挂起它。试图阻止在持有锁时挂起线程也是不可行的，因为可能无法识别锁，而且，它可能使程序永久无法恢复。

---

## 60. 目标三元组到底是个什么鬼？

**原文标题**: What the hell is a target triple?

**原文链接**: [https://mcyoung.xyz/2025/04/14/target-triples/](https://mcyoung.xyz/2025/04/14/target-triples/)

本文深入探讨了目标三元组这个晦涩的世界，目标三元组是编译器（尤其是基于LLVM的编译器）用于识别代码编译平台的字符串。 虽然GCC最初的定义是`<机器>-<厂商>-<操作系统>`，但受到广泛采用和厂商贡献的影响，LLVM标准已成为事实上的“官方”标准。

作者详细介绍了目标三元组的组成部分。 `<机器>`部分标识架构，通常包括版本和特性信息。 文章深入探讨了命名约定的复杂性，特别是对于x86和ARM架构，并为正确使用提供了一个“规范性参考”，不鼓励使用诸如“amd64”或“x64”之类的自创名称。 `<厂商>`组件标识ABI定义者，通常是操作系统或平台开发者，有助于对相关目标进行分组。 最后，`<操作系统>`部分指定操作系统，这对于确定可执行文件格式和ABI细节至关重要。

文章强调了目标三元组的历史背景，它最初是GCC二进制文件的前缀。 它将GCC每个目标使用单独二进制文件的方法与LLVM的统一二进制文件和`--target`标志进行了对比。 文章还探讨了ARM架构命名的变化，这受到其碎片化历史以及直接在架构名称中包含版本号的影响。 作者批评了Windows的ARM64模拟方法，并强调了Apple卓越的编译器专业知识。 作者根据LLVM提供了一个可能的架构和厂商名称的综合列表。

---

## 61. 扎克伯格与联邦贸易委员会结束Meta反垄断案谈判失败

**原文标题**: Mark Zuckerberg's failed negotiations with the FTC to end Meta's antitrust case

**原文链接**: [https://www.wsj.com/us-news/law/mark-zuckerberg-meta-antitrust-ftc-negotiations-a53b3382](https://www.wsj.com/us-news/law/mark-zuckerberg-meta-antitrust-ftc-negotiations-a53b3382)

无法访问文章链接。

---

## 62. 伪颅相学卷土重来——依然带有种族主义色彩

**原文标题**: Fake skull science is back – and it's still racist

**原文链接**: [https://www.npr.org/2025/04/16/1263527098/its-been-a-minute-phrenology-social-media-physiognomy](https://www.npr.org/2025/04/16/1263527098/its-been-a-minute-phrenology-social-media-physiognomy)

这篇NPR“稍等一下”节目片段探讨了人们对颅相学（头部研究）和面相学（面部研究）等伪科学的兴趣再度抬头的现象。这些伪科学试图将外貌与内在品质、智力甚至犯罪倾向联系起来。文章强调，这些做法是“垃圾科学”，完全无效。

尽管这些观点已被揭穿，但它们正以各种形式重新出现，从网上关于“女巫头骨和天使头骨”的讨论，到在跨性别调查中使用“头骨几何学”，以及（毫无根据的）声称人工智能可以检测同性恋面孔。

这篇文章调查了这种基于外貌对人进行分类的兴趣重新抬头的吸引力以及潜在后果。布列塔尼·卢斯与耶鲁大学哲学教授莉莉·胡和《滚石》杂志文化撰稿人迈尔斯·克利讨论了这个话题，以了解为什么这些伪科学观点会重新获得关注以及它们构成的危险。文章强调了这些做法的种族主义历史，并警告不要继续使用它们。

---

## 63. Show HN: Torque – 适用于任何处理器的轻量级元汇编器

**原文标题**: Show HN: Torque – A lightweight meta-assembler for any processor

**原文链接**: [https://benbridle.com/projects/torque.html](https://benbridle.com/projects/torque.html)

Torque 是一种轻量级的通用元汇编器，旨在解决现有嵌入式处理器汇编器的常见问题，例如文档不足、语言笨拙以及操作系统兼容性有限。它旨在成为一个适用于任何处理器的单一汇编器，允许用户在程序中将指令编码定义为宏，利用模板将值打包到位中。这只需要 Torque 和处理器的规格书。

帖子提供了语言概述、PIC10F200 和 TRS-80 的示例程序，以及 Z80 上高级循环优化的演示链接。 提供了安装说明，包括下载源代码、预编译的 Linux 可执行文件或使用 Rust 编译器（nightly 版本）从源代码构建。 用法部分概述了将源文件汇编成具有指定格式的目标文件的基本命令。 最后，提供了用户手册、变更日志和路线图的链接，以获取更多文档和开发信息。

---

## 64. CT扫描可能导致5%的癌症，研究发现；专家指出不确定性。

**原文标题**: CT scans could cause 5% of cancers, study finds; experts note uncertainty

**原文链接**: [https://arstechnica.com/health/2025/04/ct-scans-could-cause-5-of-cancers-study-finds-experts-note-uncertainty/](https://arstechnica.com/health/2025/04/ct-scans-could-cause-5-of-cancers-study-finds-experts-note-uncertainty/)

本文讨论了最近发表在《JAMA Internal Medicine》上的一项研究，该研究估计CT扫描可能导致5%的癌症诊断，基于2023年9300万次扫描的数据，将其与未来10.3万例癌症病例联系起来。与CT扫描相关的最常见癌症是肺癌和结肠癌，其中腹部和盆腔扫描风险最高。该研究敦促医生以优化剂量谨慎使用CT扫描，承认其重要作用，同时也强调了经常被忽视的潜在危害。

虽然外部专家同意需要仔细考虑，但他们强调了用于评估辐射吸收和癌症风险的模型中存在的不确定性。一些人强调，每次扫描增加的癌症风险与终生总体癌症风险相比很小，并且诊断的益处通常大于风险。近年来CT扫描使用量的增加促使人们呼吁医生探索超声波和核磁共振成像等替代成像选择，利用诊断算法，并让患者参与决策过程，以确保益处大于风险。专家们得出结论，患者仍然应该在建议时进行CT扫描。

---

## 65. 袖珍热成像大师P2赋予手机掠食者般的视野

**原文标题**: Pint-sized Thermal Master P2 gives your phone Predator vision

**原文链接**: [https://newatlas.com/electronics/review-thermal-master-p2-catches-heat-small/](https://newatlas.com/electronics/review-thermal-master-p2-catches-heat-small/)

本文评测了Thermal Master P2，一款极为小巧紧凑的热成像相机，可通过USB-C接口连接到安卓智能手机和平板电脑。评测者强调了其令人印象深刻的尺寸、高分辨率（256x192像素）和宽广的温度测量范围（-14°F至1,112°F）。

P2提供了多种图像和视频控制选项，包括多种颜色显示格式（如“白热”）、光学变焦以及在特定点或定义区域内以数字方式显示温度的功能。该应用程序允许基于温度阈值发出警报。

评测者测试了P2，发现它足够灵敏，可以检测到微妙的热信号，例如手印、椅子上的人体轮廓和最近停放的汽车。他认为其潜在应用包括野生动物观测、电路诊断和识别热泄漏。

在赞扬其性能和便携性的同时，该评测也指出了对P2在恶劣环境中耐用性的担忧，以及其微小尺寸可能导致易于丢失的问题。该应用程序最初在平板电脑上出现了一些可用性问题，但在智能手机上使用时得到了解决。评测者还因为短暂地将其指向蜡烛火焰而收到警告，突出了需要避免过热的源，因为它们可能会损坏传感器。目前，P2与Android 6.0及以上版本兼容。

---

## 66. 如何打包Flatpak程序 [视频]

**原文标题**: How to Flatpack Programs [video]

**原文链接**: [https://www.youtube.com/watch?v=rJcQ45jKuN4](https://www.youtube.com/watch?v=rJcQ45jKuN4)

这并非文章，而是YouTube页脚信息片段。名为“如何扁平封装程序”的视频似乎托管在YouTube上，所提供的内容仅仅是YouTube网站底部常见的标准链接和法律信息列表。

因此，没有文章内容可以概括。列出的项目有：

*   **链接：**版权，联系我们，创作者，广告，开发者，条款，隐私政策与安全，YouTube运作方式，测试新功能。
*   **法律：**NFL Sunday Ticket © 2025 Google LLC。

本质上，这是您通常在任何YouTube页面底部找到的样板信息。它提供了各种资源的链接，并声明了Google对YouTube上NFL Sunday Ticket的所有权。

---

## 67. 如何赢得和幼儿的争论

**原文标题**: How to win an argument with a toddler

**原文链接**: [https://seths.blog/2025/04/how-to-win-an-argument-with-a-toddler/](https://seths.blog/2025/04/how-to-win-an-argument-with-a-toddler/)

本文认为，与幼儿争论无法真正“获胜”，因为他们对真正的思想交流不感兴趣。他们通常寻求的是连接、娱乐、获得地位的机会，或者只是参与制造噪音和角色扮演。作者将这种类比扩展到幼儿之外，适用于像防御性官僚、欺凌者和那些有僵化议程的人。

作者认为，真正的争论应该包含基于诚意的思想交流，从而带来洞察力和潜在的观点改变。如果你从不改变你的想法，你可能没有参与真正的争论。

幼儿（或行为像幼儿的人）利用争论的*表象*来避免或为发脾气辩护。获胜避免了发脾气；失败则证明了发脾气的合理性。

作者建议了转变这种动态的策略：询问之前基于讨论而改变的立场，并询问什么信息可能导致不同的观点。最后，作者认为，就人们选择相信并作为其核心身份一部分的事情进行争论通常毫无意义。简而言之，本文倡导旨在学习和理解的真正讨论，而不是“赢得”一场意志的较量。

---

## 68. React考古学 (2016)

**原文标题**: Archeology of React (2016)

**原文链接**: [https://legacy.reactjs.org/blog/2016/09/28/our-first-50000-stars.html](https://legacy.reactjs.org/blog/2016/09/28/our-first-50000-stars.html)

本文由Vjeux于2016年撰写，探讨了React的起源和演变，追溯了其从Facebook内部项目到流行的开源库的发展历程。文章强调，React的出现是为了解决Facebook内部MVC框架BoltJS的缺陷。Jordan Walke的实验性副项目FaxJS（后来的FBolt）为React的核心概念奠定了基础：props、state、UI diffing和服务器端渲染。

文章描述了React如何使用FBolt逐步替换Facebook内部的组件，从而实现了增量采用。"React"这个名字的选择是为了反映其对状态和属性变化的响应式特性。受Facebook在PHP中使用XHP的启发，JSX的加入通过提供声明式语法，显著改善了UI开发。Adam Hupp关于将元素数组视为frag的建议也成为了React的一个核心特性。

文章还提到了React早期内部开发期间的API变动以及Lee Byron在完善生命周期API方面所做的努力。它强调了Pete Hunt领导的Instagram对React的采用，这需要将React与Facebook的基础设施解耦，并最终为它的开源发布铺平了道路。最后，文章还赞扬了设计师Maykel Loomans为React创造了视觉形象。总而言之，React的成功并非一蹴而就，而是迭代改进、内部采用以及众多工程师贡献的结果。

---

## 69. 本·乔丹的人工智能毒丸与对抗性噪声的怪异世界

**原文标题**: Benn Jordan's AI poison pill and the weird world of adversarial noise

**原文链接**: [https://cdm.link/benn-jordan-ai-poison-pill/](https://cdm.link/benn-jordan-ai-poison-pill/)

本文探讨了本·乔丹的“AI毒丸”概念，这是一种防止生成式AI音乐服务未经许可使用音乐训练数据的方法。乔丹的方法利用对抗性噪声来扰乱AI训练，从而可能保护音乐家的作品免受未经授权的使用。该技术利用“模拟漏洞”，直接作用于音频本身，并具有混淆和验证的潜力。

文章强调了这项技术的更广泛意义，强调它揭示了训练集和生成式音频模型是如何运作的，从而促进了一个通常笼罩在神秘之中的领域的透明度。虽然目前需要大量的计算能力，但这个概念验证提高了未来出现更有效方法的可能性。

文章探讨了对抗性噪声的更广阔世界，指出它既可以用于防御，也可以用于攻击AI系统。它引用了关于和谐隐蔽、AI检测算法以及在训练神经网络中使用噪声的研究。文章还触及了阴暗面，提到了作为声波武器使用的定向压力波攻击。

最终，作者支持乔丹的方法，并设想未来分销商会授权使用这种技术来保护音乐家。文章结尾批评了Suno.ai创始人的一份声明，该声明认为AI音乐创作应该令人愉快，这与人类音乐家所需的真正努力和技能形成了鲜明对比。

---

## 70. JSLinux

**原文标题**: JSLinux

**原文链接**: [https://www.bellard.org/jslinux/](https://www.bellard.org/jslinux/)

JSLinux允许用户直接在网页浏览器中运行包括Linux发行版和Windows 2000在内的各种操作系统。它是一个模拟器，提供不同的系统配置。支持的系统包括：

*   **x86：** Alpine Linux 3.12.0 (控制台和X Window版本), Windows 2000, 和 FreeDOS。
*   **riscv64：** Buildroot (Linux) (控制台和X Window版本) 和 Fedora 33 (Linux) (控制台和X Window版本)。

每个系统都可以通过链接访问，允许用户立即启动模拟。一些系统，特别是X Window版本，支持右键菜单功能。Fedora 33实例的启动时间较长。

JSLinux由Fabrice Bellard创建，信息最后更新于2021年。还提供新闻、虚拟机列表、常见问题解答和技术说明等资源。

---

## 71. 谷歌人...前谷歌人

**原文标题**: Googler... ex-Googler

**原文链接**: [https://nerdy.dev/ex-googler](https://nerdy.dev/ex-googler)

一位前谷歌员工（邮箱地址argyle@google.com）在被裁员后表达了震惊和愤怒。该作者曾是Chrome团队的成员，积极参与各种旨在改善网络和开发者体验的项目。尽管被告知裁员并非基于绩效，并且他们可以找到其他职位，但立即被切断对谷歌资源的访问，包括日历、文档和代码，这让作者感觉像个罪犯，不受欢迎。

裁员的时机尤其令人痛苦，因为它发生在一次富有成效且令人愉快的团队建设活动之后不久。作者详细描述了他们积极管理的诸多职责和贡献，包括Google I/O视频、舞台展示、开发者主题演讲支持以及参与CSS工作组的活动。由于裁员，这些机会都被突然取消。

作者感到被背叛、不被赏识，并被简化为“巨型公司中的一个齿轮”。他们感叹失去了培养的关系，并且无法继续进行中的项目。作者感到不知所措并努力应对，他们提供了替代联系方式（Bluesky和adam.is@nerdy.dev），供那些希望联系的人使用，但同时也警告说，由于该情况的情感影响，回复可能会延迟。

---

## 72. 异想天开的投资者

**原文标题**: The Whimsical Investor

**原文链接**: [https://fi-le.net/stonks/](https://fi-le.net/stonks/)

异想天开的投资者

本书赞扬那些拥有古怪特征的小型上市公司。作者重点介绍了五家这样的公司，最终将“最滑稽上市公司奖”颁给了智冠科技。

书中介绍的公司包括：

*   **Schwälbchen Molkerei Jakob Berz AG:** 一家德国乳品厂，市值 7300 万美元，以其双关语名称和古怪的酸奶小册子而闻名。
*   **日本一ソフトウェア:** 一家日本游戏发行商，估值 2700 万美元，因其吉祥物企鹅普利尼和夸张的年度报告设计而备受喜爱。
*   **Bergbahnen Engelberg-Trübsee-Titlis AG:** 一家成立于 1911 年的瑞士山区缆车公司，市值 1.6 亿美元，拥有创新的缆车设计。
*   **株式会社不二家:** 日本糖果制造商，Peko-chan 背后的公司，市值 4.1 亿美元，拥有种类繁多的糖果、餐厅和商品。
*   **智冠科技:** 一家台湾视频游戏公司，市值 5.1 亿美元，其特点是拥有由专业子公司组成的复杂结构和各种大型多人在线游戏（MMO），包括作者最喜欢的《女神 Online》。

作者推崇智冠科技，因为其全面的“游戏软件世界”囊括了整个视频游戏价值链。文章最后强调了保持私营公司和上市公司之间平衡的重要性，以确保持续获得投资机会和信息。

---

## 73. 有声书 vs. 纸质书：一个读者和作者的辩论

**原文标题**: Audiobooks vs. Printed Books: a debate as a reader and an author

**原文链接**: [https://newsandreviews.substack.com/p/audiobooks-vs-printed-books-a-debate](https://newsandreviews.substack.com/p/audiobooks-vs-printed-books-a-debate)

无法访问文章链接。

---

## 74. Figma就“开发者模式”一词向Lovable发送了停止侵权通知函。

**原文标题**: Figma sent a cease-and-desist letter to Lovable over the term 'Dev Mode'

**原文链接**: [https://techcrunch.com/2025/04/15/figma-sent-a-cease-and-desist-letter-to-lovable-over-the-term-dev-mode/](https://techcrunch.com/2025/04/15/figma-sent-a-cease-and-desist-letter-to-lovable-over-the-term-dev-mode/)

Figma向AI初创公司Lovable发出停止函，要求其停止在其一项产品功能中使用“Dev Mode”一词。Figma去年注册了“Dev Mode”的商标，该术语在许多技术产品中普遍指代“开发者模式”。虽然Figma声称该商标专门适用于“Dev Mode”这个快捷方式，但许多人认为该术语已经通用化，本不应该被注册为商标。

Lovable的首席执行官Anton Osika目前拒绝遵守Figma的要求，这为潜在的法律诉讼奠定了基础。这场纠纷不仅仅是商标侵权，因为Lovable凭借其AI驱动的“氛围编码”方法，将自己定位为Figma的直接竞争对手，允许用户从文本提示生成设计和代码。Lovable声称正在从Figma那里赢得客户，而Figma首席执行官Dylan Field对此不屑一顾，他认为完成一个项目比快速原型设计更重要。

Figma为其行为辩护，声称Lovable与自己属于相同的“商品和服务类别”，这与也使用类似术语的微软等大型公司不同。随着Figma准备潜在的IPO，这次针对一家冉冉升起竞争对手的法律行动凸显了成熟设计工具和新兴AI驱动的初创公司之间日益紧张的关系。

---

## 75. Show HN: Resonate – 实时高时间分辨率频谱分析

**原文标题**: Show HN: Resonate – real-time high temporal resolution spectral analysis

**原文链接**: [https://alexandrefrancois.org/Resonate/](https://alexandrefrancois.org/Resonate/)

Resonate：一种用于音频和其他信号实时频谱分析的新型低延迟算法。它使用基于指数加权移动平均 (EWMA) 的谐振器组来捕获时域中的频率分量。与基于 FFT 的方法相比，这种方法具有低内存和计算成本的优势，无需缓冲即可在每个采样点更新频谱估计。

主要特性包括：

*   **高效性：** 计算量与谐振器的数量呈线性关系，且与信号持续时间无关。每次更新仅涉及少量算术运算。
*   **实时性：** 能够实现适用于实时应用的高时间分辨率。
*   **并行化：** 谐振器独立运行，允许并行处理。
*   **灵活性：** 谐振器频率和时间常数可以独立调整。
*   **频谱图生成：** 允许直接且高效地创建具有相关频率分辨率的频谱图。

该算法利用与时间常数相关的单个参数 α 来控制系统动态。输出可以被归一化以均衡响应。Resonate 通过与 Librosa 的 CQT 进行频谱图比较来展示其表示频谱信息的能力，应用于音乐和语音。Python、C++ 和 Swift（noFFT 和 Oscillators 包）中提供了开源实现，以及演示应用程序和 YouTube 播放列表。一篇详细介绍该算法的研究论文将于 2025 年在国际计算机音乐会议上发表。

---

## 76. Cohere发布Embed 4

**原文标题**: Cohere Launches Embed 4

**原文链接**: [https://cohere.com/blog/embed-4](https://cohere.com/blog/embed-4)

Cohere于2025年4月15日发布Embed 4，旨在为企业提供最先进的多模态搜索精度和效率。Embed 4 旨在帮助企业安全检索其多模态数据，从而构建智能AI应用。该公告由Cohere团队发布，属于“产品”和“新闻发布”类别。本质上，这是一项旨在改进各种类型数据搜索能力的升级，以促进AI驱动的商业解决方案的开发。

---

## 77. 使用 jemalloc 避免 Rust 中的内存碎片

**原文标题**: Avoiding memory fragmentation in Rust with jemalloc

**原文链接**: [https://kerkour.com/rust-jemalloc](https://kerkour.com/rust-jemalloc)

无法访问文章链接。

---

## 78. 大型语言模型能通过实际的自由职业编程工作赚取一百万美元吗？

**原文标题**: Can LLMs earn $1M from real freelance coding work?

**原文链接**: [https://newsletter.getdx.com/p/benchmarking-ai-software-engineering-capabilities](https://newsletter.getdx.com/p/benchmarking-ai-software-engineering-capabilities)

本文总结了OpenAI开发的一项名为SWE-Lancer的新基准测试，该测试旨在评估前沿AI模型执行真实世界软件工程任务的能力。该基准测试涉及Upwork上发布的超过1400个自由职业工作，总价值100万美元，并测试了AI完成单个编码任务（错误修复、功能开发）和工程管理任务（从多个提交方案中选择最佳方案）的能力。

研究人员评估了Claude 3.5 Sonnet、GPT-4o和OpenAI的“o1”模型。主要发现包括：

*   **与人类相比表现不佳：**所有模型都未能赚取全部100万美元，其中Claude 3.5 Sonnet表现最佳，约赚取40.3万美元（任务完成率为33.7%）。
*   **更擅长管理任务：**与自己创建解决方案相比，AI模型在选择最佳解决方案方面更成功。
*   **多次尝试可提高性能：**允许“o1”模型进行多次尝试显著提高了其成功率。
*   **更多计算时间有所帮助：**增加“推理工作量”提高了性能，尤其是在复杂任务上。
*   **模型之间存在显著的能力差异：**Claude 3.5 Sonnet在UI/UX任务方面优于GPT-4o。

该研究得出结论，虽然AI取得了显著进展，但它仍然无法可靠地处理大多数复杂的、真实世界的软件工程项目。SWE-Lancer基准测试为衡量AI在软件开发方面的进展提供了一个有价值的工具，并有助于了解AI目前的 capabilities 和局限性。

---

## 79. MeshCore，一种用于分组无线电的新型轻量级混合路由网状协议

**原文标题**: MeshCore, a new lightweight, hybrid routing mesh protocol for packet radios

**原文链接**: [https://github.com/ripplebiz/MeshCore](https://github.com/ripplebiz/MeshCore)

MeshCore 是一个轻量级的开源 C++ 库，用于使用 LoRa 和其他分组无线电创建弹性、去中心化的多跳分组路由网络。它专为需要在缺乏传统基础设施的区域进行通信的嵌入式项目而设计。

主要功能包括用于扩展范围的多跳分组路由，支持来自 Heltec、RAK Wireless 等公司的 LoRa 无线电，去中心化和自愈网络操作，低功耗，以及通过预构建的示例应用程序轻松部署。

MeshCore 适用于离网通信、应急响应、户外活动、战术应用和物联网传感器网络。

入门涉及在 Visual Studio Code 中安装 PlatformIO，下载 MeshCore 存储库，选择一个示例应用程序（如 Terminal Chat、Simple Repeater、Companion Radio 或 Room Server），并使用串行监视器进行通信。

该项目在 MIT 许可下开源，并通过拉取请求 (PR) 欢迎对 'dev' 分支的贡献，建议首先通过 Issue 讨论重大更改。可以通过 GitHub Issues 和 Andy Kirby 的 Discord 获得支持。

特别说明，RAK Wireless 板的支持需要修补 PlatformIO 包，并将生成的 firmware.hex 文件使用 uf2conv.py 转换为 .uf2 文件以便刷写。

---

## 80. JetBrains IDE AI：编码助手，更智能的辅助，免费层级

**原文标题**: JetBrains IDEs Go AI: Coding Agent, Smarter Assistance, Free Tier

**原文链接**: [https://blog.jetbrains.com/blog/2025/04/16/jetbrains-ides-go-ai/](https://blog.jetbrains.com/blog/2025/04/16/jetbrains-ides-go-ai/)

JetBrains将AI工具（包括AI助手和新型编码助手Junie）直接集成到其IDE中，采用单一订阅模式并提供免费层级。此举旨在通过自动化基础编码任务来提高开发者的生产力和创造力，使开发者能够专注于更高层次的问题解决。

Junie由Anthropic的Claude和OpenAI LLM提供支持，是一个虚拟协作工具，旨在协助处理复杂的编码任务、回答问题、提出方案并确保代码质量。它最初与IntelliJ IDEA Ultimate、PyCharm Pro、WebStorm和GoLand兼容，未来将支持其他IDE。

AI助手已更新，具有改进的代码完成、上下文感知和扩展的模型选项（Claude 3.7 Sonnet、Google Gemini 2.5 Pro和OpenAI模型），以及改进的本地模型集成，以增强隐私和控制。新的编辑模式可以直接从聊天界面进行多文件编辑。

新的订阅模式包含一个免费层级，提供无限的代码完成、访问本地AI模型以及基于积分的云端AI辅助和Junie的使用。更高的层级（AI Pro和AI Ultimate）提供更高的使用配额。All Products Pack和dotUltimate订阅现在包含AI Pro。JetBrains强调其AI功能的隐私、安全性和透明度，确保用户数据得到保护。

---

## 81. 停止把天才和混蛋混为一谈

**原文标题**: Stop Conflating Genius with Asshole

**原文链接**: [https://www.joanwestenberg.com/stop-conflating-genius-with-asshole/](https://www.joanwestenberg.com/stop-conflating-genius-with-asshole/)

本文旨在反驳一种常见的误解，即才华横溢必然伴随着残忍或难以相处。文章批判了社会对“受折磨的天才”原型的接受，例如史蒂夫·乔布斯和埃隆·马斯克等人物，他们经常以追求卓越为借口，为自己的恶劣行为开脱。

作者认为，这种将天才与混蛋行为混为一谈的做法，使得平庸之辈得以将权力武器化，并以创新或远见的名义掩盖其残忍，从而逃避责任。这创造了一个被操纵的体系，人们因此被迫离开自己的职业生涯，创造力受到压制，个人则会将虐待内化，并认为自己缺乏卓越的能力。

相反，作者认为真正的天才不是关于支配，而是关于合作、同理心和谦逊。聪明人倾听、与他人合作，并明白同理心能强化想法。残忍并非卓越的先决条件；相反，那些需要贬低或打压他人的人只是暴君和恶霸。文章敦促读者停止美化和原谅这种行为，并质疑“残忍是远见的代价”这种方便的谎言。作者认为，真正的天才在于合作和认识他人的优点。随后，作者在The Index上推广了自己的作品，并鼓励读者订阅。

---

## 82. 确定作者排序的有趣方法 (2016)

**原文标题**: Fun ways of deciding authorship order (2016)

**原文链接**: [https://dynamicecology.wordpress.com/2016/09/21/fun-ways-of-deciding-authorship-order/](https://dynamicecology.wordpress.com/2016/09/21/fun-ways-of-deciding-authorship-order/)

本文幽默地探讨了生态学和进化生物学研究人员用于确定科学论文作者排序的非常规方法，这些方法超越了基于贡献排序或字母排序等标准做法。它起源于一场关于不寻常作者排序决定的Twitter对话。

作者展示了一系列从Twitter和其他来源收集的轶事，展示了从篮球和槌球等体育比赛到硬币翻转和计算机生成的随机选择等随机方法。更具创造性的解决方案包括使用实际考虑因素、博弈论，甚至是一场布朗尼烘焙比赛。

本文重点介绍了具体的例子和引文，例如通过篮球技能（Fauth & Resetarits）、槌球系列赛（Hassell & May）、硬币翻转（Miller & Ballard）以及现在传奇般的布朗尼烘焙比赛（Young & Young）来确定作者身份。它还承认使用地理位置来帮助作者排序（Feder & Mitchell-Olds）以及一只名叫切斯特的暹罗猫充当作者（F.D.C. Willard）。

作者还包括了在最初发表后发现的更多例子的更新，例如班卓琴游戏、身高排序、掰手腕以及一只狗通过选择零食来随机确定作者顺序。文章最后对作者排序纠纷的严重后果提出了警示，并引用了一篇因意见不合而被撤回的论文。这篇文章强调了学术实践中发现的创造力和偶尔的荒谬性。

---

## 83. 液体：语言模型是可扩展且统一的多模态生成器

**原文标题**: Liquid: Language models are scalable and unified multi-modal generators

**原文链接**: [https://foundationvision.github.io/Liquid/](https://foundationvision.github.io/Liquid/)

Liquid：一种统一视觉和语言理解与生成的新型自回归生成范式，它将图像标记化为离散代码，并在共享特征空间中学习其与文本标记的嵌入，从而消除了对外部预训练视觉嵌入（如CLIP）的需求。

一项关键发现是，通常与统一视觉和语言任务相关的性能下降会随着模型规模的增加而减小，从而揭示了一种新的缩放定律。此外，统一的标记空间允许视觉生成和理解相互增强，从而减轻了先前多模态LLM中常见的干扰。

Liquid表现出显著的效率，利用现有的LLM作为强大的基础，并使训练成本降低了100倍。它在多模态能力方面优于Chameleon，并保持了与LLAMA2相当的语言性能。此外，它在图像生成方面超越了SD v2.1和SD-XL等模型（在MJHQ-30K上的FID为5.47）。

作者得出结论，像Qwen2.5和GEMMA2这样的LLM是强大的多模态生成器，能够为视觉-语言理解和生成提供可扩展的解决方案，展示了未来发展的一个有希望的途径。

---

## 84. 中古英语文本系列 METS

**原文标题**: METS, the Middle English Texts Series

**原文链接**: [https://metseditions.org](https://metseditions.org)

中古英语文本系列 (METS) 是一个不断扩充的中古时期文本编辑集合，代表了来自英国和爱尔兰的文学传统和文化。METS于2024年11月推出，拥有重新设计的网站和数字版本，致力于出版价格合理的印刷版和开放获取的数字版本，以提高可访问性。

该网站收录了威廉·卡克斯顿的《巴黎和维也纳》和《布兰查丁和艾格莱丁》等文本，这些浪漫故事在中世纪欧洲广受欢迎，是小说的重要先驱。用户可以浏览现有版本并注册新闻通讯，获取有关出版物、会议和网站发展的最新信息。

该系列包括广泛的中古英语作品，从《情人之忏悔》到《猫头鹰与夜莺》，在现代阅读习惯中保持了原作的语言完整性。“即将推出”部分重点介绍了未来的出版物，例如14世纪的圣经翻译《英格兰启示录》。METS还鼓励学者与他们合作出版，为编辑过程提供指南和风格指南。本质上，METS旨在让广大读者可以访问中古英语文本，同时保留其历史和语言价值。

---

## 85. 来自撒哈拉绿色地区的7000年前骨骼揭示神秘人类血统。

**原文标题**: 7k-year-old skeletons from the green Sahara reveal a mysterious human lineage

**原文链接**: [https://www.smithsonianmag.com/smart-news/7000-year-old-skeletons-from-the-green-sahara-reveal-a-previously-unknown-human-lineage-180986403/](https://www.smithsonianmag.com/smart-news/7000-year-old-skeletons-from-the-green-sahara-reveal-a-previously-unknown-human-lineage-180986403/)

考古学家在如今利比亚曾经郁郁葱葱的“绿色撒哈拉”地区发现了一个先前未知且基因独特的古人类谱系。在岩石掩体中发现的两具拥有7000年历史的木乃伊女性，以及陶器和岩画的DNA分析显示，尽管非洲以外传入了畜牧业，但该人群在数万年内保持了基因隔离。

这一发现挑战了长期以来关于绿色撒哈拉曾是北非和撒哈拉以南非洲之间人类迁徙走廊的理论。相反，该研究表明，该地区畜牧业的传播是通过文化交流而不是大规模迁徙发生的。

DNA分析显示，绿色撒哈拉个体大约在5万年前从撒哈拉以南非洲人的祖先中分离出来，并保持了基因隔离。研究人员对该人群的基因隔离感到惊讶。虽然只是初步发现，但这一发现对理解人类祖先，特别是在非洲，复杂的人口历史仍在被揭示，具有重要意义。科学家计划进行进一步的研究，以更全面地了解生活在绿色撒哈拉的人们，并承认仅对两个个体的DNA分析可能无法代表整个人群。

---

## 86. 每年有多少超新星爆发？

**原文标题**: How many supernova explode every year?

**原文链接**: [https://badastronomy.beehiiv.com/p/ban-447-wait-how-many-supernova-explode](https://badastronomy.beehiiv.com/p/ban-447-wait-how-many-supernova-explode)

糟糕天文学时事通讯：超新星命名规则及惊人探测率增长

本文讨论了超新星的命名规则及其探测率的惊人增长。超新星的命名方式为SN[年份][字母]，字母按发现顺序在年内按字母顺序分配。文章重点介绍了2021年在车轮星系中发现的超新星SN2021 afdx的命名，这使得作者计算出当年发现的超新星数量可能达到了21760颗。作者指出，根据一个计算这些总数的网站显示，2021年实际观测到的超新星候选者数量为21081颗。

与过去相比，这个数字代表着巨大的增长。1987年，当年第一颗超新星于2月23日被发现。在2021年，同样的时间范围内，估计已经观测到3593颗超新星，这展示了望远镜技术和探测方法的巨大进步。

文章最后通过推断宇宙中的超新星爆发率，估计考虑到星系的巨大数量，大约每秒钟有30颗超新星爆发。作者预计，未来的望远镜，如维拉·鲁宾巡天望远镜，将会把每年探测到的超新星数量增加到数十万颗。

---

## 87. 几何代数中旋子的交互式介绍 (2018)

**原文标题**: An interactive introduction to rotors from geometric algebra (2018)

**原文链接**: [https://marctenbosch.com/quaternions/](https://marctenbosch.com/quaternions/)

Marc ten Bosch的文章认为，在3D引擎编程中应使用几何代数中的旋子（Rotor）来取代四元数。他认为四元数通常被肤浅地教授，掩盖了其基本原理并需要不必要的抽象（例如第四维度）。

文章将旋子视为一种更直观和通用的旋转表示方法，涵盖了四元数（在3D中）和复数（在2D中），并扩展到更高的维度。旋子建立在旋转发生在平面中而不是绕轴的概念之上，在不依赖于右手定则等约定的情况下，提供了更清晰的旋转感。

引入的核心概念是**双向量（bivector）**，它是两个向量的外积（或楔积）的结果。双向量表示由两个向量形成的平面，与产生法向量的叉积形成对比。文章详细介绍了双向量如何具有表示在基面上的投影的分量，类似于向量如何具有表示在基轴上的投影的分量。它突出了双向量背后的几何直觉及其与旋转的直接关系。

最终，这篇文章提倡转向教学和使用旋子，强调它们的清晰性、通用性以及与四元数相比它们提供的更深入的理解。虽然在3D中与四元数同构，但旋子被呈现为一种更自然且不那么模糊的旋转表示。交互式图表增强了对双向量及其组件的理解。

---

## 88. 伊夫林·沃的颓废救赎

**原文标题**: Evelyn Waugh’s Decadent Redemption

**原文链接**: [https://libertiesjournal.com/online-articles/evelyn-waughs-decadent-redemption/](https://libertiesjournal.com/online-articles/evelyn-waughs-decadent-redemption/)

以下是我对《自由杂志》文章“伊夫林·沃的颓废救赎”的总结，基于我对围绕沃的作品的常见主题和分析的理解：

这篇文章可能探讨了伊夫林·沃的复杂且常常矛盾的性格，尤其是他从早期作品中看似颓废和愤世嫉俗的作家到晚年成为更具传统宗教和保守色彩的人物的演变。它认为，沃的被认为的颓废，以《衰落与瓦解》和《罪恶的肉体》等小说中对贵族和富裕精英的讽刺刻画为特征，不仅仅是虚无主义，而是包含着对现代世界精神空虚的深刻不满。

“救赎”方面可能指的是沃最终皈依天主教，以及这种信仰如何影响了他后来的写作。虽然他的讽刺仍然尖锐，但现在常常被用来捍卫传统价值观，并反对他所认为的现代性带来的腐蚀性影响。《故园风雨后》等小说代表了这种转变，探索了在瞬息万变的世界中信仰、恩典和传统持久力量等主题。

文章可能认为，沃后来的作品，虽然经常被认为更加保守，但并非完全偏离了他早期的主题。相反，它们代表着在持续以批判性和讽刺性眼光看待的世界中，更明确和有目的地寻找意义和秩序。作者可能认为，沃对天主教的拥抱为他理解和批判现代世界提供了一个框架，将他早期的倦怠转变为一种更结构化和神学化的批评。最终，这篇文章可能认为，沃的旅程可以被理解为在20世纪感知到的道德堕落中寻找真实价值观的过程。

---

## 89. 现代CMake简介

**原文标题**: An Introduction to Modern CMake

**原文链接**: [https://cliutils.gitlab.io/modern-cmake/README.html](https://cliutils.gitlab.io/modern-cmake/README.html)

本文介绍“现代CMake”（CMake 3.15+）作为一种简洁、强大且优雅的构建系统解决方案，并将其与旧版本和不良示例进行对比。它阐述了为什么像CMake这样优秀的构建系统对于避免硬编码路径、支持多平台和编译器、使用CI以及管理依赖项等任务至关重要。

本文认为CMake优于其他构建系统，因为它得到了IDE和软件包的广泛支持，使其成为包含多个项目的通用工具。文章强烈建议不要支持最老的CMake版本，建议最低使用3.15，最好是3.18或更高版本，并推荐设置一个最大测试版本以确保兼容性。

重点强调的关键最低版本：
- 3.24：非常适合软件包作者。
- 3.18：对Python和CUDA有良好的支持。
- 3.15：推荐用于大多数项目。

本文档旨在提供最佳实践和指导，以补充官方CMake文档。它列出了其他资源，包括HSF CMake培训、Effective Modern CMake以及诸如“More Modern CMake”之类的演示文稿，并感谢Henry Schreiner作为原始作者。

---

## 90. 推理模型无需思考也能有效

**原文标题**: Reasoning Models Can Be Effective Without Thinking

**原文链接**: [https://arxiv.org/abs/2504.09858](https://arxiv.org/abs/2504.09858)

本文题为“推理模型无需思考也能有效”，挑战了大型语言模型 (LLM) 需要明确的“思考”过程才能有效执行推理任务的传统认知。作者，包括马文捷，研究了DeepSeek-R1-Distill-Qwen模型在使用“无需思考”方法时的性能，该方法通过简单的提示绕过了明确的思考过程。

令人惊讶的是，他们发现，在控制使用的token数量时，尤其是在低预算情况下，“无需思考”方法可以优于传统的“思考”方法。这一发现在一系列不同的推理数据集中都成立，包括数学问题解决、形式定理证明和编码挑战。

此外，作者还探索了一种并行扩展方法，其中“无需思考”方法生成多个独立的输出，然后使用特定于任务的验证器或简单的“N中最佳”策略（如基于置信度的选择）对这些输出进行聚合。这种并行“无需思考”方法展示了与基于思考的方法相当甚至更优越的性能，尤其是在延迟受限的情况下。它可以达到与使用“思考”的模型相当的结果，同时速度显著更快（高达9倍）。

该研究表明，冗长的思考过程可能不是有效推理的必要条件，并提出了一个具有竞争力的基准，用于在资源受限的环境中使用更简单、更快的“无需思考”提示的并行扩展来实现强大的推理性能。该论文提出了一个重新考虑LLM中冗长而复杂的推理链的必要性的理由，并提供了一种更有效的替代方案。

---

## 91. 设计低成本高性能10 MHz – 15 GHz 矢量网络分析仪

**原文标题**: Designing a low-cost high-performance 10 MHz – 15 GHz vector network analyzer

**原文链接**: [https://hforsten.com/designing-a-low-cost-high-performance-10-mhz-15-ghz-vector-network-analyzer.html](https://hforsten.com/designing-a-low-cost-high-performance-10-mhz-15-ghz-vector-network-analyzer.html)

本文详细介绍了低成本、高性能的10 MHz – 15 GHz矢量网络分析仪（VNA）的设计与构建。作者概述了现有廉价VNA（如nanoVNA和LibreVNA）的缺点，例如频率限制、不完整的S参数测量能力以及高泄漏。满足所需性能的商业VNA价格过于昂贵。

作者的设计采用双源架构，消除了传统VNA中存在问题的端口开关，并利用LMX2594 PLL芯片进行宽带信号生成。该设计采用定制的定向耦合器，使用同轴电缆平衡-不平衡变换器对入射波和反射波进行采样。接收部分使用ADL5802双通道混频器，尽管额定频率仅为6 GHz，但因其经济高效而被选中。AD9238 ADC处理信号转换，FPGA执行数字信号处理以从接收到的信号中提取I和Q分量。

PCB由FR4材料制成，采用6层设计，并强调射频屏蔽和隔离。作者描述了与定向耦合器批量制造相关的挑战。与最初的3D打印原型相比，CNC加工的外壳提供了更高的稳定性和热性能。作者旨在通过精心选择组件和优化设计，创建一个性能优于其他低成本替代品的VNA。

---

## 92. 视频去审查比以往任何时候都更容易了。

**原文标题**: It's easier than ever to de-censor videos

**原文链接**: [https://www.jeffgeerling.com/blog/2025/its-easier-ever-de-censor-videos](https://www.jeffgeerling.com/blog/2025/its-easier-ever-de-censor-videos)

本文讨论了令人惊讶的简单审查视频内容去像素化方法。作者在YouTube视频中挑战读者破解像素化文本，并很快获得了多位使用不同技术的个人成功破解。

主要方法由GitHub用户KoKuToru演示，利用了视频中运动引起的像素化区域的轻微偏移。通过提取和对齐帧，并使用诸如TensorFlow和GIMP等代码和工具，他们可以积累像素数据并重建被模糊的信息。文章强调，视频中的运动越多，逆向工程像素化就越容易。

作者强调，虽然旧方法很困难，但人工智能和更快的计算机使当今的去像素化变得更快更简单。他警告不要仅仅依靠模糊或像素化来审查视频中的敏感信息，尤其是在有运动的情况下。他建议使用纯色遮罩作为更安全的替代方案。

评论者普遍认为，对于信息安全而言，模糊处理并不比像素化更好，甚至可能更糟。他们建议使用非常大的像素化方块来使恢复更加困难。

---

## 93. 静态锁步模式的后硅验证

**原文标题**: Post-Silicon Validation of Static Lockstep Mode

**原文链接**: [https://www.intel.com/content/www/us/en/content-details/851929/post-silicon-validation-of-static-lockstep-mode-on-intel-xeon-6-processor-e-core-architecture.html](https://www.intel.com/content/www/us/en/content-details/851929/post-silicon-validation-of-static-lockstep-mode-on-intel-xeon-6-processor-e-core-architecture.html)

无法访问文章链接。

---

## 94. 《闪灵》中诡异照片背后45年谜团据信已解开

**原文标题**: 45-year mystery behind eerie photo from The Shining is believed to be solved

**原文链接**: [https://www.cbc.ca/lite/story/1.7507349](https://www.cbc.ca/lite/story/1.7507349)

在斯坦利·库布里克《闪灵》中那张诡异照片背后的谜团，在45年后据信已被解开。这张照片的日期是1921年7月4日，照片中杰克·尼科尔森的脸叠加在眺望酒店聚会人群中的一个男人身上。

退休学者阿拉斯代尔·斯帕克与《纽约时报》记者阿里克·托拉尔一起调查了这张照片的来源。斯帕克的动机是对流传的阴谋论感到沮丧，其中包括一种说法，称照片中的男人是一位揭露金融精英的银行家。

一位Reddit用户的面部识别技术将照片中的男人识别为桑托斯·卡萨尼，他是20世纪20年代伦敦的一位舞厅舞蹈演员。斯帕克与托拉尔证实了这一点，他们发现卡萨尼的真名叫约翰·戈尔曼，他因英国皇家空军的一次飞机坠毁和随后的整形手术而留下了面部疤痕，这解释了他不寻常的外貌。

随后，调查重点转向了照片的来源。最初人们认为它来自华纳兄弟的档案馆，但摄影师默里·克洛斯透露，他是从BBC霍顿照片图书馆获得的，该图书馆现在是盖蒂图片社的一部分。这张照片拍摄于1921年2月14日情人节，地点是伦敦皇家宫殿酒店的皇后舞厅。

斯帕克对确认了照片中的男人、照片的地点和日期感到满意，从而填补了关于这部电影标志性图像的重要知识空白。

---

## 95. 怪异 - 上网的一种方式

**原文标题**: WEIRD – a way to be on the web

**原文链接**: [https://a.weird.one](https://a.weird.one)

本文题为《WEIRD——一种网络存在方式》，介绍“WEIRD”作为一种拟议的网络存在方法或平台。由于提供的内容简短（“Weird 一种网络存在方式！”），无法提供详细的解释。主要要点是**介绍了“WEIRD”作为一种建立或增强个人在线存在的新方法或工具。**

在缺乏更多背景信息的情况下，我们只能推断“WEIRD”旨在提供一种独特的或非常规的数字领域体验。它暗示了一种潜在的独特或替代方式来浏览和参与在线世界，可能使其自身区别于传统网站、社交媒体平台或其他已建立的在线工具。这个名称本身就意味着它偏离了常态，可能侧重于创造力、个性和小众社区。最终，需要更多信息才能充分理解“WEIRD”的具体功能、优势和目标受众。

---

## 96. Notion Mail 发布了

**原文标题**: Notion Mail is out

**原文链接**: [https://www.notion.com/product/mail](https://www.notion.com/product/mail)

Notion Mail发布，但内容简短。仅限iOS，即将推出更多平台。

---

## 97. Amazfit活动追踪器和表盘资源生成

**原文标题**: Amazfit activity tracker and watch face asset generation

**原文链接**: [https://blog.gingerbeardman.com/2025/04/11/amazfit-activity-tracker-and-watch-face-asset-generation/](https://blog.gingerbeardman.com/2025/04/11/amazfit-activity-tracker-and-watch-face-asset-generation/)

本文详细介绍了作者使用 Amazfit Band 7 的体验，以及他们创建的一个用于生成自定义表盘素材的 Web 工具。由于对现有表盘不满意，并且不想手动创建大量图像素材，作者开发了一个工具，允许用户从所选字体自定义和生成数字、文本和符号的图像。用户可以调整字体、大小、颜色、对齐方式、文件名前缀以及所需的特定字符/短语。该工具旨在简化创建与 Amazfit 表盘构建工具兼容的图像素材的过程。

作者强调了该工具的多功能性，并指出它可用于生成 Amazfit 表盘以外的图像素材。他们提供了 Web 应用程序的链接 (gingerbeardman.com/amazfit/) 供其他人使用。作为一个例子，他们展示了他们使用该工具创建的一个名为 DIN 的表盘，并解释了它的设计元素。DIN 表盘可以通过 AmazFaces 应用程序和 Zepp 应用商店安装。作者还感谢 Monotype 的 Datto 和 Charles Nix 提供的在设计中使用的免费 D-DIN Condensed Bold 字体。

---

## 98. API中的GPT-4.1

**原文标题**: GPT-4.1 in the API

**原文链接**: [https://openai.com/index/gpt-4-1/](https://openai.com/index/gpt-4-1/)

无法访问文章链接。

---

## 99. 为了性能使用原始循环？

**原文标题**: Raw Loops for Performance?

**原文链接**: [https://www.sandordargo.com/blog/2025/04/16/raw-loops-for-performance](https://www.sandordargo.com/blog/2025/04/16/raw-loops-for-performance)

本文探讨了使用原始循环和 C++20 ranges 进行数据转换时的性能差异，特别关注将 `std::list` 转换为 `std::vector` 的场景。作者 Sandor Dargo 最初旨在用 `std::ranges::transform` 替换原始循环，以遵循“无原始循环”的理念。

文章重点介绍了一位同事提出的担忧，即基于 range 的转换在填充结果向量时是否会惰性复制元素。涉及构造函数和复制/移动操作的实验表明，ranges 版本确实以惰性方式运行，将操作推迟到向量构造完成。

作者随后将基于 range 的方法与使用 `emplace_back` 和 `reserve` 避免重新分配的优化原始循环进行了比较。基准测试表明，优化后的原始循环通常比 ranges 版本更快，尽管差异可能很小。原始的、使用 `push_back` 且没有 `reserve` 的原始循环最慢。

结论是，虽然 ranges 提供了更好的可读性和简洁性，但它们并不能自动保证更好的性能。作者强调了在仅仅基于微优化做出决策之前，进行基准测试和考虑阿姆达尔定律的重要性。如果性能至关重要且循环是瓶颈，则建议使用带有 `emplace_back` 和 `reserve` 的优化原始循环。否则，应优先考虑可读性和代码风格。

---

## 100. 古墓引擎

**原文标题**: Tomb Engine

**原文链接**: [https://tombengine.com/](https://tombengine.com/)

古墓引擎1.8.1是一款开源引擎，旨在创建自定义古墓丽影冒险。它是一个社区驱动的项目，托管在Github、Discord、X（Twitter）和Youtube等平台上。重要的是，该项目强调其独立于拥有古墓丽影商标的Core Design、Eidos Interactive和Embracer Group AB。

该引擎免费使用，不用于商业目的。其开源性质旨在通过代码研究促进协作、贡献和学习。作者不对源代码的任何非法使用负责，按“原样”发布，并通过贡献者在业余时间的志愿工作进行维护。

---

